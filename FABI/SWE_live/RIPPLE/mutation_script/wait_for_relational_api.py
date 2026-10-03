#!/usr/bin/env python3
"""Wait for Luna recovery, then start one verified relational retry attempt."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from openai import OpenAI

import mutation_pipeline as mp


def write_progress(root: Path, started: str, checks: int, successes: int,
                   last_error: str, phase: str, pid: int | None) -> None:
    stamp = mp.now()
    state = {
        "updated_at": stamp, "phase": phase, "started_at": started,
        "completed": 6, "total": 172, "remaining": 166,
        "success": 6, "failed": 0, "errors": int(bool(last_error)),
        "eta": "unknown (waiting for Luna API)", "pid": pid,
        "log": str(root / "API_WATCH.log"), "output_dir": str(root),
        "run_id": root.name, "cache_hit": 6, "executed_this_run": 0,
        "api_checks": checks, "consecutive_api_successes": successes,
        "last_api_error": last_error,
    }
    mp.write_json(root / "status.json", state)
    text = "\n".join([
        "# RIPPLE relational run", "", f"- run: `{root.name}`",
        f"- started_at: `{started}`", f"- updated_at: `{stamp}`",
        f"- phase: **{phase}**", "- mutation completed: `6/172`; cached verified patches: `6`",
        "- remaining cases: `166`", "- case failures in pending attempt: `0`",
        f"- API checks: `{checks}`; consecutive successes: `{successes}`",
        f"- last API error: `{last_error or 'none'}`", "- ETA: `unknown (waiting for Luna API)`",
        f"- watcher PID: `{pid if pid else 'stopped'}`",
        f"- watcher log: `{root / 'API_WATCH.log'}`",
        f"- run log: `{root / 'RUN.log'}`", f"- output: `{root}`", "",
    ])
    target = root / "LIVE_PROGRESS.md"
    temporary = target.with_name(f"{target.name}.tmp.{os.getpid()}")
    temporary.write_text(text)
    os.replace(temporary, target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--attempt-label", default="attempt_02")
    parser.add_argument("--interval", type=int, default=60)
    parser.add_argument("--max-checks", type=int, default=120)
    args = parser.parse_args()
    root = args.run_root.resolve()
    started = mp.now()
    checks = 0
    consecutive = 0
    last_error = "Luna upstream 502 before watcher launch"
    while checks < args.max_checks:
        checks += 1
        try:
            key, base = mp.read_key()
            client = OpenAI(api_key=key, base_url=base, timeout=15, max_retries=0)
            response = client.chat.completions.create(
                model=mp.MODEL, messages=[{"role": "user", "content": "Reply ok."}], max_tokens=20)
            if not response.choices:
                raise RuntimeError("empty provider response")
            consecutive += 1
            last_error = ""
            print(f"[{mp.now()}] API health check {checks}: success {consecutive}/2", flush=True)
        except Exception as exc:
            consecutive = 0
            last_error = f"{type(exc).__name__}: {str(exc)[:240]}"
            print(f"[{mp.now()}] API health check {checks}: {last_error}", flush=True)
        if consecutive >= 2:
            write_progress(root, started, checks, consecutive, "", "launching_retry", os.getpid())
            command = ["bash", str(Path(__file__).with_name("retry_relational.sh")),
                       root.name, args.attempt_label]
            result = subprocess.run(command, text=True, capture_output=True)
            print(result.stdout, end="", flush=True)
            if result.returncode:
                last_error = f"retry launcher exited {result.returncode}: {result.stderr[:240]}"
                print(f"[{mp.now()}] {last_error}", flush=True)
                write_progress(root, started, checks, consecutive, last_error, "failed", None)
                return result.returncode
            print(f"[{mp.now()}] launched {args.attempt_label}; watcher exits", flush=True)
            return 0
        write_progress(root, started, checks, consecutive, last_error, "waiting_api", os.getpid())
        for _ in range(args.interval // 10):
            time.sleep(10)
            write_progress(root, started, checks, consecutive, last_error, "waiting_api", os.getpid())
    write_progress(root, started, checks, consecutive, last_error, "api_unavailable", None)
    print(f"[{mp.now()}] API remained unavailable after {checks} bounded checks", flush=True)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
