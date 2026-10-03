#!/usr/bin/env python3
"""Authoritative live monitor for the enhancement experiment."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import time
from pathlib import Path


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pid", type=int, required=True)
    parser.add_argument("--interval", type=int, default=15)
    args = parser.parse_args()
    root = args.output.resolve()
    config_path = root / "RUN_CONFIG.json"
    while not config_path.exists() and alive(args.pid):
        time.sleep(1)
    if not config_path.exists():
        return 1
    config = json.loads(config_path.read_text())
    staged_config = root / "RUN_CONFIG_STAGED.json"
    if staged_config.exists():
        config = json.loads(staged_config.read_text())
    total = int(config["total_jobs"])
    started = dt.datetime.fromisoformat(config["started_at"])
    while True:
        try:
            authoritative = json.loads((root / "status.json").read_text())
        except (OSError, ValueError, json.JSONDecodeError):
            authoritative = {}
        completed = int(authoritative.get("completed", 0))
        errors = int(authoritative.get("errors", 0))
        failed = int(authoritative.get("failed", 0))
        success = int(authoritative.get("success", completed))
        process_alive = alive(args.pid)
        phase = str(authoritative.get("phase", "starting"))
        phase_total = int(authoritative.get("total", total))
        remaining = max(0, phase_total - completed)
        eta = str(authoritative.get("eta", "unknown"))
        last_event = None
        events = root / "events.jsonl"
        if events.exists():
            lines = events.read_text(errors="replace").splitlines()
            if lines:
                try:
                    last_event = json.loads(lines[-1]).get("time")
                except json.JSONDecodeError:
                    pass
        if not process_alive and phase not in {"completed", "inference_blocked", "evaluation_blocked"}:
            phase = "failed"
        status = {**authoritative, "process_alive": process_alive, "last_event_at": last_event}
        elapsed = (dt.datetime.now().astimezone() - started).total_seconds()
        text = "\n".join([
            "# Enhancement live progress", "",
            f"- Phase: `{phase}`", f"- Started: `{config['started_at']}`",
            f"- Updated: `{authoritative.get('updated_at', now())}`", f"- Current stage progress: `{completed}/{phase_total}`",
            f"- Remaining: `{remaining}`", f"- Successful executions: `{success}`",
            f"- Unresolved evaluations: `{failed}`", f"- Infrastructure errors: `{errors}`",
            f"- Last event: `{last_event or 'none'}`", f"- ETA: `{eta}`",
            "- Stage order: `all inference -> validated barrier -> all official evaluation`",
            f"- Elapsed seconds: `{round(elapsed, 1)}`", f"- Main PID: `{args.pid}`",
            f"- Main log: `{root / 'RUN.log'}`", f"- Results: `{root / 'SUMMARY.md'}`", "",
            "During inference, `completed` counts validated combined predictions. During evaluation, it counts official resolved/unresolved results. Evaluation cannot begin until `INFERENCE_BARRIER.json` validates every job.", "",
        ])
        atomic(root / "LIVE_PROGRESS.md", text)
        if not process_alive:
            (root / "MONITOR_EXIT.json").write_text(json.dumps({"time": now(), "reason": "main process exited", "status": status}, ensure_ascii=False, indent=2) + "\n")
            return 0 if phase == "completed" else 1
        time.sleep(args.interval)


if __name__ == "__main__":
    raise SystemExit(main())
