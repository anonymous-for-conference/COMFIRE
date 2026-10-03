#!/usr/bin/env python3
"""Archive the three-run SWE-Agent Lite clean intersection."""

from __future__ import annotations

import hashlib
import json
import shutil
import fcntl
from pathlib import Path


ROOT = Path("<local-data>/coding_agent/EviFuzz")
DATASET = Path("<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json")
DEST = ROOT / "original_passed_cases/SWE-Agent/gpt54mini_lite"
RUNS = {
    1: ROOT / "lite_gpt54_mini/run_1",
    2: ROOT / "lite_gpt54_mini_2/run_2",
    3: ROOT / "lite_gpt54_mini_3/run_3",
}
EXPECTED_MODE = "lite_local_repo_long_lived_official_container_v1_call100_out4096"


def read_json(path: Path):
    return json.loads(path.read_text())


def atomic_json(path: Path, value) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def latest_valid(run_root: Path, instance_id: str) -> Path:
    attempts = sorted((run_root / "cases" / instance_id).glob("attempt_*"), reverse=True)
    for attempt in attempts:
        validation_path = attempt / "validation.json"
        if not validation_path.exists():
            continue
        validation = read_json(validation_path)
        if validation.get("valid") is not True or validation.get("execution_mode") != EXPECTED_MODE:
            continue
        if len(list((attempt / "agent").rglob("*.traj"))) != 1:
            continue
        if len(list((attempt / "agent").rglob("*.pred"))) != 1:
            continue
        return attempt
    raise RuntimeError(f"no valid attempt for {instance_id} in {run_root}")


def validate_predictions(run_root: Path, expected_ids: set[str]) -> dict[str, dict]:
    rows = [json.loads(line) for line in (run_root / "predictions.jsonl").read_text().splitlines() if line.strip()]
    indexed = {row["instance_id"]: row for row in rows}
    if len(rows) != 300 or len(indexed) != 300 or set(indexed) != expected_ids:
        raise RuntimeError(f"invalid predictions set in {run_root}: rows={len(rows)}, unique={len(indexed)}")
    if any("model_patch" not in row for row in rows):
        raise RuntimeError(f"prediction without model_patch in {run_root}")
    return indexed


def main() -> int:
    lock_path = DEST.parent / ".collect_gpt54mini_lite.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock = lock_path.open("w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise RuntimeError("another gpt54mini_lite collector is already running") from exc
    dataset = read_json(DATASET)
    records = {row["instance_id"]: row for row in dataset}
    expected_ids = set(records)
    if len(expected_ids) != 300:
        raise RuntimeError(f"expected 300 unique dataset instances, got {len(expected_ids)}")

    summaries = {}
    predictions = {}
    resolved_sets = []
    for run, run_root in RUNS.items():
        summary = read_json(run_root / "evaluation_summary/official_summary.json")
        summaries[run] = summary
        predictions[run] = validate_predictions(run_root, expected_ids)
        resolved = set(summary["resolved_ids"])
        if summary["resolved_instances"] != len(resolved):
            raise RuntimeError(f"run {run} resolved count does not match resolved_ids")
        if summary.get("unstopped_containers") not in (0, []) or summary.get("unremoved_images") not in (0, []):
            raise RuntimeError(f"run {run} evaluation cleanup was incomplete")
        resolved_sets.append(resolved)

    clean_ids = sorted(set.intersection(*resolved_sets))
    if DEST.exists():
        shutil.rmtree(DEST)
    (DEST / "cases").mkdir(parents=True)

    index_cases = []
    for iid in clean_ids:
        case_root = DEST / "cases" / iid
        case_root.mkdir(parents=True)
        task = records[iid]
        atomic_json(case_root / "task.json", task)
        outcome = {"instance_id": iid, "resolved_in_all_three_runs": True, "runs": {}}
        for run, run_root in RUNS.items():
            attempt = latest_valid(run_root, iid)
            target = case_root / f"run_{run}"
            shutil.copytree(attempt, target, copy_function=shutil.copy2)
            validation = read_json(attempt / "validation.json")
            pred_file = next((attempt / "agent").rglob("*.pred"))
            attempt_pred = read_json(pred_file)
            official_pred = predictions[run][iid]
            if (attempt_pred.get("model_patch") or "") != (official_pred.get("model_patch") or ""):
                raise RuntimeError(f"run {run} patch mismatch for {iid}")
            outcome["runs"][f"run_{run}"] = {
                "official_resolved": iid in set(summaries[run]["resolved_ids"]),
                "selected_attempt": validation["attempt"],
                "source": str(attempt),
                "archived": str(target),
                "model_patch_sha256": hashlib.sha256((official_pred.get("model_patch") or "").encode()).hexdigest(),
                "metrics": read_json(attempt / "metrics.json") if (attempt / "metrics.json").exists() else None,
            }
        atomic_json(case_root / "outcome.json", outcome)
        index_cases.append(outcome)

    (DEST / "clean_case_ids.txt").write_text("\n".join(clean_ids) + "\n")
    run_results = {
        f"run_{run}": {
            "resolved": summaries[run]["resolved_instances"],
            "unresolved": summaries[run]["unresolved_instances"],
            "empty_patches": summaries[run]["empty_patch_instances"],
            "errors": summaries[run]["error_instances"],
            "unstopped_containers": len(summaries[run]["unstopped_containers"]) if isinstance(summaries[run]["unstopped_containers"], list) else summaries[run]["unstopped_containers"],
            "unremoved_images": len(summaries[run]["unremoved_images"]) if isinstance(summaries[run]["unremoved_images"], list) else summaries[run]["unremoved_images"],
            "source": str(RUNS[run]),
        }
        for run in RUNS
    }
    atomic_json(DEST / "RUN_RESULTS.json", run_results)
    atomic_json(DEST / "INDEX.json", {
        "benchmark": "SWE-bench Lite",
        "model": "openai/gpt-5.4-mini",
        "agent": "SWE-Agent",
        "reasoning_effort": "not exposed by SWE-Agent model configuration",
        "execution_mode": EXPECTED_MODE,
        "dataset": str(DATASET),
        "dataset_sha256": hashlib.sha256(DATASET.read_bytes()).hexdigest(),
        "resolved_intersection_all_three": len(clean_ids),
        "clean_case_ids": clean_ids,
        "cases": index_cases,
    })
    (DEST / "README.md").write_text(
        "# SWE-Agent gpt-5.4-mini on SWE-bench Lite\n\n"
        f"The official three-run resolved intersection contains **{len(clean_ids)} clean cases**. "
        "Each case directory contains the frozen task record, an outcome map, and the complete selected valid attempt from each run.\n\n"
        "The source runs used four inference workers, a 100-call limit, a 4096-token model output limit, "
        "one case-private repository/runtime, one long-lived official instance container per trajectory, and official SWE-bench Lite evaluation.\n\n"
        "See `INDEX.json` for the machine-readable case map, `RUN_RESULTS.json` for aggregate results, "
        "and `clean_case_ids.txt` for the intersection IDs.\n"
    )
    (DEST / "TRACE_FORMAT.md").write_text(
        "# Trace Format\n\n"
        "`cases/<instance_id>/run_<n>/` is the complete selected valid attempt directory. It includes "
        "the SWE-Agent trajectory, prediction, trace/debug logs, batch configuration, validation, metrics, and case configuration. "
        "`outcome.json` records the original source, selected attempt number, official resolved status, and patch digest.\n"
    )
    print(json.dumps({"destination": str(DEST), "clean_cases": len(clean_ids)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
