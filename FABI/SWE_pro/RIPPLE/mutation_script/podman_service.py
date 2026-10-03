#!/usr/bin/env python3
"""Start a run-private Podman API service with bounded, logged retries."""

from __future__ import annotations

import argparse
import json
import signal
import subprocess
import time
from datetime import datetime
from pathlib import Path


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--socket", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--exit-code", type=Path)
    parser.add_argument("--attempts", type=int, default=10)
    args = parser.parse_args()
    exit_code = args.exit_code or (args.run_root / "EXIT_CODE")
    args.output.mkdir(parents=True, exist_ok=True)
    summary = args.output / "PODMAN.log"
    child: subprocess.Popen | None = None

    def terminate(*_args) -> None:
        if child and child.poll() is None:
            child.terminate()

    signal.signal(signal.SIGTERM, terminate)
    signal.signal(signal.SIGINT, terminate)
    for attempt in range(1, args.attempts + 1):
        log = args.output / f"PODMAN_attempt_{attempt:02d}.log"
        with summary.open("a") as handle:
            handle.write(f"[{now()}] attempt={attempt} log={log}\n")
        with log.open("w") as handle:
            child = subprocess.Popen(
                ["podman", "system", "service", "--time=0", f"unix://{args.socket}"],
                stdout=handle, stderr=subprocess.STDOUT,
            )
            while child.poll() is None and not exit_code.exists():
                time.sleep(2)
            if child.poll() is None:
                child.terminate()
                try:
                    child.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    child.kill()
                    child.wait()
                with summary.open("a") as summary_handle:
                    summary_handle.write(
                        f"[{now()}] pipeline terminal; service stopped pid={child.pid}\n"
                    )
                return 0
            returncode = child.returncode
        with summary.open("a") as handle:
            handle.write(f"[{now()}] attempt={attempt} pid={child.pid} exit={returncode}\n")
        if returncode == 0:
            return 0
        if attempt < args.attempts:
            time.sleep(min(5 * attempt, 30))
    failure = {
        "failed_at": now(), "attempts": args.attempts,
        "error": "Podman API service attempts exhausted", "socket": str(args.socket),
    }
    (args.output / "PODMAN_FAILURE.json").write_text(json.dumps(failure, indent=2) + "\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
