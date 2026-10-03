#!/usr/bin/env python3
"""Atomically mirror authoritative experiment/interface status for users."""

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
    tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
    tmp.write_text(text)
    tmp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_root", type=Path)
    parser.add_argument("--interval", type=int, default=20)
    args = parser.parse_args()
    root = args.run_root.resolve()
    while True:
        outer_path = root / "status.json"
        outer = json.loads(outer_path.read_text()) if outer_path.exists() else {}
        inner_path = root / "interface/status.json"
        inner = json.loads(inner_path.read_text()) if inner_path.exists() else {}
        active = inner if outer.get("phase") == "inference_and_evaluation" and inner else outer
        phase = outer.get("phase", "initializing")
        if inner and phase == "inference_and_evaluation":
            phase = f"inference_and_evaluation/{inner.get('phase', 'unknown')}"
        updated = now()
        lines = [
            "# RIPPLE Mutation Live Progress", "", f"- run: `{root.name}`",
            f"- phase: `{phase}`", f"- started_at: `{outer.get('started_at', 'unknown')}`",
            f"- completed/total: `{active.get('completed', 0)}/{active.get('total', 1)}`",
            f"- remaining: `{active.get('remaining', 1)}`", f"- success: `{active.get('success', 0)}`",
            f"- failed: `{active.get('failed', 0)}`", f"- infrastructure errors: `{active.get('errors', 0)}`",
            f"- updated_at: `{updated}`", f"- last event: `{active.get('last_event_at', 'unknown')}`",
            f"- ETA: `{active.get('eta', 'unknown')}`", f"- PID: `{outer.get('pid', 'unknown')}`",
            f"- main log: `{root / 'RUN.log'}`", f"- output: `{root}`", "",
            "统计口径：completed 为当前单 case 已完成 inference/evaluation 或已终止；",
            "success/failed/errors 分别表示流水线成功、任务失败、基础设施错误。",
        ]
        atomic(root / "LIVE_PROGRESS.md", "\n".join(lines) + "\n")
        if outer.get("phase") in {"completed", "failed"}:
            atomic(root / "monitor_exit.json", json.dumps({"time": updated, "reason": outer["phase"]}, indent=2) + "\n")
            return 0
        time.sleep(args.interval)


if __name__ == "__main__":
    raise SystemExit(main())
