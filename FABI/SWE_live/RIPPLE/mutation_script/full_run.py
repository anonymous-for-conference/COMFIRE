#!/usr/bin/env python3
"""Run all token-stable LIVE cases with two mutation lanes per agent."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import signal
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import mutation_pipeline as mp

AGENTS = ("SWE_Agent", "OpenCode", "Codex")
AGENT_SLUG = {"SWE_Agent": "swe-agent", "OpenCode": "opencode", "Codex": "codex"}
STOP = False


def stop(_signum, _frame):
    global STOP
    STOP = True


def selected_rows() -> list[dict[str, str]]:
    rows = list(csv.DictReader(mp.CSV_PATH.open()))
    selected = []
    for agent in AGENTS:
        for index, row in enumerate(item for item in rows if item["agent"] == agent):
            task = json.loads((Path(row["round_1_artifact"]) / "task.json").read_text())
            current = dict(row)
            current.update(repo=task["repo"], base_commit=task["base_commit"],
                           lane=index % 2 + 1)
            selected.append(current)
    keys = [(row["agent"], row["instance_id"]) for row in selected]
    if len(keys) != len(set(keys)) or not selected:
        raise ValueError("duplicate or empty selection")
    return selected


def event(root: Path, **data):
    with (root / "events.jsonl").open("a") as handle:
        handle.write(json.dumps({"at": mp.now(),
                                 "attempt": os.environ.get("RIPPLE_ATTEMPT_LABEL", "attempt_01"),
                                 **data}, ensure_ascii=False) + "\n")
        handle.flush()


def mutate_case(row: dict[str, str], root: Path, k: int, seed: int,
                enabled_operators: tuple[str, ...]) -> dict:
    target = root / "patches" / row["agent"] / row["instance_id"]
    existing = target / "mutation.json"
    if existing.is_file():
        meta = json.loads(existing.read_text())
        patch = target / "mutation.patch"
        if patch.is_file() and hashlib.sha256(patch.read_bytes()).hexdigest() == meta.get("sha256"):
            return meta
    errors = []
    for attempt in range(1, 9):
        if STOP:
            raise RuntimeError("termination requested")
        try:
            clusters, docs = mp.clusters_for(row, k, seed + attempt - 1)
            if not clusters:
                target.mkdir(parents=True, exist_ok=True)
                patch = target / "mutation.patch"
                patch.write_text("")
                meta = {"status": "no_documentation", "case": {key: row[key] for key in ("agent", "instance_id", "repo", "base_commit")},
                        "clusters": [], "changes": [], "files": [], "patch": str(patch), "sha256": hashlib.sha256(b"").hexdigest()}
                mp.write_json(target / "mutation.json", meta)
                return meta
            return mp.make_patch(row, clusters, docs, root, enabled_operators)
        except Exception as exc:
            if "no nonoverlapping clusters" in str(exc):
                case_dir = mp.PLACEMENT_ROOT / row["agent"] / row["instance_id"]
                if not (case_dir / "all_doc.jsonl").read_text().strip() and not (case_dir / "clustered_doc.jsonl").read_text().strip():
                    target.mkdir(parents=True, exist_ok=True)
                    patch = target / "mutation.patch"
                    patch.write_text("")
                    meta = {"status": "no_documentation", "case": {key: row[key] for key in ("agent", "instance_id", "repo", "base_commit")},
                            "clusters": [], "changes": [], "files": [], "patch": str(patch), "sha256": hashlib.sha256(b"").hexdigest()}
                    mp.write_json(target / "mutation.json", meta)
                    return meta
            errors.append({"attempt": attempt, "error": f"{type(exc).__name__}: {exc}"})
            mp.write_json(target / f"mutation_attempt_{attempt:02d}.error.json", errors[-1])
            time.sleep(2 * attempt)
    raise RuntimeError(f"mutation failed after eight attempts: {errors[-1]['error']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260927)
    parser.add_argument("--operators", nargs="+", choices=("L1", "L2", "L3", "R1", "R2", "R3"),
                        default=("L1", "L2", "L3"))
    args = parser.parse_args()
    enabled_operators = tuple(args.operators)
    if not enabled_operators:
        raise ValueError("at least one mutation operator is required")
    root = args.run_root.resolve()
    if not (root / "RUN_CONFIG.md").is_file():
        raise RuntimeError("RUN_CONFIG.md must be written before launch")
    rows = selected_rows()
    manifest = [{key: row[key] for key in ("agent", "instance_id", "repo", "base_commit")}
                for row in rows]
    mp.write_json(root / "selection_manifest.json", {"count": len(rows), "cases": manifest,
                                                      "input_csv": str(mp.CSV_PATH),
                                                      "input_sha256": hashlib.sha256(mp.CSV_PATH.read_bytes()).hexdigest()})
    event(root, kind="phase", phase="mutation", total=len(rows), pid=os.getpid())
    errors = []
    metadata = []
    executors = {(agent, lane): ThreadPoolExecutor(max_workers=1,
                 thread_name_prefix=f"mutation-{agent}-{lane}")
                 for agent in AGENTS for lane in (1, 2)}
    try:
        futures = {executors[(row["agent"], row["lane"])].submit(mutate_case, row, root, args.k, args.seed,
                                                   enabled_operators): row
                   for row in rows}
        for future in as_completed(futures):
            row = futures[future]
            try:
                meta = future.result()
                metadata.append(meta)
                event(root, kind="case", stage="mutation", result="success",
                      agent=row["agent"], lane=row["lane"], instance_id=row["instance_id"], patch=meta["patch"],
                      operators=[item["operator"] for item in meta["clusters"]], status=meta.get("status", "validated"))
                print(f"[{mp.now()}] mutation {len(metadata) + len(errors)}/{len(rows)} OK {row['agent']} lane={row['lane']} {row['instance_id']}", flush=True)
            except Exception as exc:
                error = {"agent": row["agent"], "instance_id": row["instance_id"],
                         "error": f"{type(exc).__name__}: {exc}"}
                errors.append(error)
                event(root, kind="case", stage="mutation", result="error", lane=row["lane"], **error)
                print(f"[{mp.now()}] mutation {len(metadata) + len(errors)}/{len(rows)} ERROR {error}", flush=True)
    finally:
        for executor in executors.values():
            executor.shutdown(wait=True, cancel_futures=STOP)
    mp.write_json(root / "mutation_summary.json", {"total": len(rows), "success": len(metadata),
                                                    "errors": errors, "operators": list(enabled_operators)})
    if errors or STOP:
        event(root, kind="terminal", phase="mutation_failed", exit_code=1, errors=len(errors))
        return 1
    flat = root / "worker_patches"
    for meta in metadata:
        target = flat / AGENT_SLUG[meta["case"]["agent"]] / meta["case"]["instance_id"]
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(meta["patch"], target / "mutation.patch")
        source_metadata = root / "patches" / meta["case"]["agent"] / meta["case"]["instance_id"] / "mutation.json"
        shutil.copy2(source_metadata, target / "mutation.json")
    if len(list(flat.glob("*/*/mutation.patch"))) != len(rows):
        raise RuntimeError("patch count mismatch before inference")
    for row in rows:
        target = flat / AGENT_SLUG[row["agent"]] / row["instance_id"]
        metadata = json.loads((target / "mutation.json").read_text())
        patch = target / "mutation.patch"
        if metadata.get("status") == "no_documentation":
            if patch.stat().st_size != 0:
                raise RuntimeError(f"no_documentation patch must be empty: {patch}")
        elif patch.stat().st_size == 0:
            raise RuntimeError(f"validated mutation patch is empty: {patch}")
    event(root, kind="phase", phase="inference_evaluation", total=len(rows))
    print(f"[{mp.now()}] starting three Agent coordinators, two inference/evaluation workers each", flush=True)
    rc = mp.run_harness(rows, root, flat)
    event(root, kind="terminal", phase="complete" if rc == 0 else "harness_failed", exit_code=rc)
    return rc


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[{mp.now()}] FATAL {type(exc).__name__}: {exc}", flush=True)
        raise
