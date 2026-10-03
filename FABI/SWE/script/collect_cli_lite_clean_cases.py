#!/usr/bin/env python3
"""Archive a CLI agent's three-run SWE-bench Lite clean intersection."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path("<local-data>/coding_agent/EviFuzz")
EVAL_ROOT = Path("<local-data>/coding_agent/SWE-bench-eval")
DATASET = Path("<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json")


def load(path: Path):
    return json.loads(path.read_text())


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("agent", choices=("codex", "opencode"))
    args = parser.parse_args()
    display = "Codex" if args.agent == "codex" else "OpenCode"
    source = ROOT / f"{args.agent}_gpt54_mini"
    dest = ROOT / f"original_passed_cases/{display}/gpt54mini_lite"
    dest.parent.mkdir(parents=True, exist_ok=True)
    lock = (dest.parent / "collect_gpt54mini_lite.lock").open("w")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    records = {row["instance_id"]: row for row in load(DATASET)}
    resolved = []
    summaries = {}
    predictions = {}
    for run in (1, 2, 3):
        root = source / f"run_{run}"
        summary_path = root / "evaluation_summary/official_summary.json"
        if not summary_path.exists():
            run_id = f"evifuzz-lite-{args.agent}-gpt54mini-run{run}"
            summary_path = EVAL_ROOT / f"evifuzz-{args.agent}-gpt-5.4-mini-run{run}.{run_id}.json"
        summary = load(summary_path)
        summaries[run] = summary
        resolved.append(set(summary["resolved_ids"]))
        rows = [json.loads(line) for line in (root / "predictions.jsonl").read_text().splitlines() if line]
        predictions[run] = {row["instance_id"]: row for row in rows}
        if len(rows) != 300 or set(predictions[run]) != set(records):
            raise RuntimeError(f"run {run} predictions failed cardinality validation")
        if summary.get("unstopped_containers") not in (0, []) or summary.get("unremoved_images") not in (0, []):
            raise RuntimeError(f"run {run} official cleanup is incomplete")
        classified = sum(int(summary.get(key, 0)) for key in (
            "resolved_instances", "unresolved_instances", "empty_patch_instances", "error_instances"
        ))
        if classified != 300:
            raise RuntimeError(f"run {run} official summary classified {classified}/300 instances")
    clean = sorted(set.intersection(*resolved))
    if dest.exists():
        shutil.rmtree(dest)
    (dest / "cases").mkdir(parents=True)
    case_index = []
    for iid in clean:
        case_dest = dest / "cases" / iid
        case_dest.mkdir()
        write_json(case_dest / "task.json", records[iid])
        outcome = {"instance_id": iid, "resolved_in_all_three_runs": True, "runs": {}}
        for run in (1, 2, 3):
            attempts = sorted((source / f"run_{run}/cases" / iid).glob("attempt_*"), reverse=True)
            selected = next((p for p in attempts if (
                (p / "prediction.json").exists()
                and load(p / "prediction.json").get("model_patch") == predictions[run][iid]["model_patch"]
            )), None)
            if selected is None:
                raise RuntimeError(f"no evaluated {args.agent} attempt for clean case {iid} run {run}")
            archived = case_dest / f"run_{run}"
            shutil.copytree(selected, archived, copy_function=shutil.copy2)
            pred = load(selected / "prediction.json")
            if pred["model_patch"] != predictions[run][iid]["model_patch"]:
                raise RuntimeError(f"patch mismatch for {iid} run {run}")
            validation = load(selected / "validation.json")
            outcome["runs"][f"run_{run}"] = {
                "official_resolved": True, "selected_attempt": validation["attempt"],
                "inference_validation_valid": validation.get("valid"),
                "source": str(selected), "archived": str(archived),
                "model_patch_sha256": hashlib.sha256(pred["model_patch"].encode()).hexdigest(),
            }
        write_json(case_dest / "outcome.json", outcome)
        case_index.append(outcome)
    (dest / "clean_case_ids.txt").write_text("\n".join(clean) + "\n")
    write_json(dest / "RUN_RESULTS.json", {f"run_{run}": {
        "resolved": summaries[run]["resolved_instances"],
        "unresolved": summaries[run]["unresolved_instances"],
        "errors": summaries[run]["error_instances"],
        "empty_patches": summaries[run]["empty_patch_instances"],
    } for run in (1, 2, 3)})
    write_json(dest / "INDEX.json", {
        "agent": display, "model": "gpt-5.4-mini", "reasoning_effort": "medium",
        "benchmark": "SWE-bench Lite", "execution_mode": "official_instance_container_cli_v1",
        "resolved_intersection_all_three": len(clean), "clean_case_ids": clean, "cases": case_index,
    })
    (dest / "README.md").write_text(
        f"# {display} gpt-5.4-mini on SWE-bench Lite\n\n"
        f"The official three-run resolved intersection contains **{len(clean)} clean cases**. "
        "Each case contains the selected valid inference attempt from all three runs, the frozen task, and outcome metadata.\n"
    )
    print(json.dumps({"agent": display, "clean_cases": len(clean), "destination": str(dest)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
