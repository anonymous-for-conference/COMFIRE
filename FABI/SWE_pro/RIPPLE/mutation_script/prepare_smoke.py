#!/usr/bin/env python3
"""Prepare smoke or full token-stable cases for the three agents."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path


WORKSPACE = Path("/data/zlyuaj/coding_agent/EviFuzz_SWE_pro")
RIPPLE = WORKSPACE / "RIPPLE"
RESULTS = RIPPLE / "mutation_result"
STABLE = WORKSPACE / "original_passed_cases_luna/token_stable_cases.csv"
PLACEMENT = WORKSPACE / "original_passed_cases_luna/placement/clean_runs"
CANONICAL = Path("/data/zlyuaj/coding_agent_big_files/swebench-pro/dataset/swebench_pro_python_test.jsonl")
AGENTS = {"Codex": "codex", "OpenCode": "opencode", "SWE_Agent": "swe-agent"}


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-name", required=True)
    parser.add_argument("-k", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260921)
    parser.add_argument("--all", action="store_true", help="select every qualifying stable case")
    parser.add_argument("--operator-mode", choices=("local", "relational"), default="local")
    parser.add_argument("--stop-after", choices=("mutation", "evaluation"), default="evaluation")
    parser.add_argument("--documents-per-cluster", type=int, default=0,
                        help="random mutable documentation locations per selected cluster; 0 keeps all")
    parser.add_argument("--preserve-documents-per-cluster", type=int, default=0,
                        help="random claims kept consistent in each selected cluster")
    args = parser.parse_args()
    run_root = RESULTS / args.run_name
    if run_root.exists():
        raise SystemExit(f"refusing to overwrite run directory: {run_root}")
    canonical = {row["instance_id"]: row for line in CANONICAL.read_text().splitlines()
                 if line.strip() for row in [json.loads(line)]}
    stable = list(csv.DictReader(STABLE.open()))
    selection = {}
    for display, agent in AGENTS.items():
        candidates = [row for row in stable if row["agent"] == display and row.get("token_stable_cv_le_0_30") == "True"]
        if len(candidates) < 2:
            raise RuntimeError(f"{display} has fewer than two token-stable cases")
        dataset = []
        selected = []
        chosen = candidates if args.all else candidates[:2]
        for row in chosen:
            iid = row["instance_id"]
            task = canonical[iid]
            case_dir = PLACEMENT / display / iid
            for required in ("clustered_doc.jsonl", "all_doc.jsonl"):
                if not (case_dir / required).is_file():
                    raise FileNotFoundError(case_dir / required)
            dataset.append(task)
            task_path = run_root / agent / "tasks" / f"{iid}.json"
            atomic(task_path, json.dumps(task, ensure_ascii=False, indent=2) + "\n")
            selected.append({
                "instance_id": iid, "display_agent": display, "repo": task["repo"],
                "case_dir": str(case_dir), "task": str(task_path),
                "mutation_output": str(run_root / "mutations" / agent / iid),
                "three_round_mean_tokens": float(row["three_round_mean_tokens"]),
                "three_round_token_cv": float(row["three_round_token_cv"]),
            })
        dataset_text = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in dataset)
        atomic(run_root / agent / "dataset.jsonl", dataset_text)
        (run_root / agent / "logs").mkdir(parents=True, exist_ok=True)
        selection[agent] = selected
        selection[agent][0]["dataset_sha256"] = hashlib.sha256(dataset_text.encode()).hexdigest()
    socket = RIPPLE / "podman" / f"{args.run_name}.sock"
    total = sum(len(cases) for cases in selection.values())
    scope = "full" if args.all else "smoke"
    enabled_operators = (["L1", "L2", "L3"] if args.operator_mode == "local"
                         else ["R1", "R2", "R3"])
    config = {
        "task": f"RIPPLE SWE-bench Pro documentation-mutation {scope} run",
        "run_id": args.run_name,
        "prepared_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "working_directory": str(RIPPLE),
        "input": str(STABLE),
        "selection_policy": ("all qualifying CSV rows per agent" if args.all
                             else "first two qualifying CSV rows per agent"),
        "scope": scope, "total_agent_cases": total,
        "model": "gpt-5.6-luna", "selector_reasoning": "medium",
        "operator_mode": args.operator_mode,
        "enabled_mutation_operators": enabled_operators,
        "local_mutation_reasoning": "medium",
        "relational_mutation_reasoning": "high",
        "relational_cluster_attempts": 5,
        "relational_initial_tool_budget": 8,
        "relational_max_tool_budget": 24,
        "clusters_per_case": args.k, "random_seed": args.seed,
        "documents_per_cluster": args.documents_per_cluster,
        "preserve_documents_per_cluster": args.preserve_documents_per_cluster,
        "stages": (["mutation"] if args.stop_after == "mutation"
                   else ["mutation", "inference", "evaluation"]),
        "stop_after": args.stop_after, "global_stage_barriers": True,
        "agents": selection, "agents_concurrent": 3, "mutation_workers_per_agent": 2,
        "inference_workers_per_agent": 2,
        "evaluation_workers_per_agent": 2, "case_timeout_seconds": 3600,
        "mutation_case_timeout_seconds": 7200,
        "mutation_case_attempts": 5 if args.operator_mode == "relational" else 3,
        "inference_attempts": 3, "evaluation_attempts": 2,
        "cache_policy": "no cross-run mutation, inference, or evaluation cache",
        "api_config": "/data/zlyuaj/coding_agent/luna_key.txt (key omitted)",
        "podman_socket": str(socket), "output": str(run_root),
    }
    atomic(run_root / "RUN_CONFIG.md", "# Run configuration\n\n```json\n" + json.dumps(config, ensure_ascii=False, indent=2) + "\n```\n")
    atomic(run_root / "SELECTION.json", json.dumps(selection, ensure_ascii=False, indent=2) + "\n")
    atomic(run_root / "RUN.log", "")
    atomic(run_root / "status.json", json.dumps({
        "updated_at": config["prepared_at"], "phase": "prepared", "started_at": None,
        "completed": 0, "total": total, "remaining": total, "success": 0, "failed": 0,
        "errors": 0, "eta": "unknown", "pid": None, "log": str(run_root / "RUN.log"),
        "output_dir": str(run_root),
    }, indent=2) + "\n")
    print(run_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
