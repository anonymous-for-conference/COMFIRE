#!/usr/bin/env python3
"""Adapter that accepts the official harness's validated raw-sample subset."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


SOURCE = Path("/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/naive_mutation/mutation_scripts/evaluate_agent.py")
BENCH = Path("/data/zlyuaj/coding_agent/OpenHands/.pr/swebench_verified_eval/benchmarks")
HARNESS = Path("/data/zlyuaj/coding_agent_big_files/swebench-pro/SWE-bench_Pro-os")


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def atomic(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--socket", type=Path, required=True)
    parser.add_argument("--attempt", type=int, default=1)
    args = parser.parse_args()
    result_path = args.output / "evaluation_result.json"
    result_path.unlink(missing_ok=True)

    command = [
        sys.executable, str(SOURCE), "--run-id", args.run_id, "--agent", args.agent,
        "--dataset", str(args.dataset), "--output", str(args.output),
        "--socket", str(args.socket), "--attempt", str(args.attempt),
    ]
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode == 0 and result_path.is_file():
        if result.stdout:
            print(result.stdout, end="")
        return 0

    expected = {
        json.loads(line)["instance_id"]
        for line in args.dataset.read_text().splitlines() if line.strip()
    }
    evaluation_run = f"{args.run_id}-{args.agent}-attempt-{args.attempt:02d}"
    report_path = args.output / f"predictions.{evaluation_run}.report.json"
    if not report_path.is_file():
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        return result.returncode or 1
    report = json.loads(report_path.read_text())
    submitted = set(report.get("submitted_ids", []))
    completed = set(report.get("completed_ids", []))
    missing = sorted(expected - submitted)
    valid_remote_subset = (
        submitted <= expected
        and completed == submitted
        and report.get("total_instances") == len(submitted)
        and report.get("submitted_instances") == len(submitted)
        and report.get("completed_instances") == len(submitted)
        and report.get("incomplete_instances") == 0
        and report.get("error_instances") == 0
    )
    if not valid_remote_subset:
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        return result.returncode or 1

    # The public dataset can remove tasks that remain supported by the checked-out
    # official harness. Re-run against the exact local task rows used for inference
    # so every prediction receives an evaluation result.
    if missing:
        local_run = f"{evaluation_run}-local-dataset"
        local_log = args.output / f"evaluation_attempt_{args.attempt:02d}_local_dataset.log"
        command = [
            "uv", "run", "--project", str(BENCH), "swebenchpro-eval",
            str(args.output / "predictions.jsonl"), "--dataset", str(args.dataset),
            "--split", "test", "--workers", "2", "--official-harness-dir", str(HARNESS),
            "--use-local-docker", "--run-id", local_run, "--dockerhub-username", "jefzda",
        ]
        env = os.environ.copy()
        env["DOCKER_HOST"] = f"unix://{args.socket}"
        with local_log.open("w") as handle:
            local_result = subprocess.run(
                command, env=env, stdout=handle, stderr=subprocess.STDOUT, timeout=86400
            )
        report_path = args.output / f"predictions.{local_run}.report.json"
        if not report_path.is_file():
            print(f"local-dataset evaluation report missing; exit={local_result.returncode}", file=sys.stderr)
            return local_result.returncode or 1
        report = json.loads(report_path.read_text())
        submitted = set(report.get("submitted_ids", []))
        completed = set(report.get("completed_ids", []))

    complete = (
        submitted == expected
        and completed == expected
        and report.get("total_instances") == len(expected)
        and report.get("submitted_instances") == len(expected)
        and report.get("completed_instances") == len(expected)
        and report.get("incomplete_instances") == 0
        and report.get("error_instances") == 0
    )
    if not complete:
        print(f"evaluation did not cover the full inference set: {report_path}", file=sys.stderr)
        return 1

    summary = {
        "status": "complete",
        "completed_at": now(),
        "agent": args.agent,
        "attempt": args.attempt,
        "wrapper_returncode": result.returncode,
        "completed": len(completed),
        "total": len(submitted),
        "input_total": len(expected),
        "officially_excluded": 0,
        "officially_excluded_ids": [],
        "resolved": report.get("resolved_instances"),
        "unresolved": report.get("unresolved_instances"),
        "errors": report.get("error_instances"),
        "completed_ids": report.get("completed_ids"),
        "resolved_ids": report.get("resolved_ids"),
        "report": str(report_path),
        "log": str(args.output / f"evaluation_attempt_{args.attempt:02d}.log"),
    }
    atomic(result_path, json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(
        f"Accepted complete evaluation set: {len(completed)}/{len(expected)} completed; "
        "0 harness errors."
    )
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
