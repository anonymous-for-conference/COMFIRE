#!/usr/bin/env python3
"""Wait for a run to complete, summarize it, then launch a dependent run."""
from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path


def atomic(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--exit-code", required=True)
    parser.add_argument("--next-run", required=True)
    parser.add_argument("--poll-seconds", type=int, default=60)
    args = parser.parse_args()
    log = args.run_root / "CONTINUATION.log"
    exit_path = args.run_root / args.exit_code
    while not exit_path.exists():
        time.sleep(args.poll_seconds)
    code = exit_path.read_text().strip()
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    if code != "0":
        atomic(log, f"[{stamp}] prerequisite failed with exit code {code}; next run not launched\n")
        return 1
    status = json.loads((args.run_root / "status.json").read_text())
    evaluations = {}
    for agent in ("swe-agent", "opencode", "codex"):
        path = args.run_root / agent / "evaluation_result.json"
        if not path.exists():
            atomic(log, f"[{stamp}] missing {path}; next run not launched\n")
            return 1
        evaluations[agent] = json.loads(path.read_text())
    if status.get("phase") != "complete" or any(
            result.get("status") != "complete" for result in evaluations.values()):
        atomic(log, f"[{stamp}] completion validation failed; next run not launched\n")
        return 1
    scripts = Path(__file__).resolve().parent
    with (args.run_root / "FINAL_SUMMARY.log").open("w") as handle:
        subprocess.run(
            ["python", str(scripts / "summarize_run.py"), "--run-root", str(args.run_root)],
            check=True, stdout=handle, stderr=subprocess.STDOUT,
        )
    atomic(log, f"[{stamp}] prerequisite complete; launching {args.next_run}\n")
    result = subprocess.run(
        ["bash", str(scripts / "launch_relational_preserve_one_full.sh"), args.next_run],
        text=True, capture_output=True,
    )
    with log.open("a") as handle:
        handle.write(result.stdout)
        handle.write(result.stderr)
        handle.write(f"launch_returncode={result.returncode}\n")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
