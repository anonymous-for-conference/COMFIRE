#!/usr/bin/env python3
"""Authoritative, atomic live monitor for isolated SWE-Agent inference."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import statistics
import time
from pathlib import Path


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic(path: Path, text: str) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def valid_attempts(root: Path, run: int, mode: str) -> dict[str, Path]:
    found: dict[str, Path] = {}
    cases = root / f"run_{run}" / "cases"
    if not cases.exists():
        return found
    for case in cases.iterdir():
        if not case.is_dir():
            continue
        for attempt in sorted(case.glob("attempt_*"), reverse=True):
            p = attempt / "validation.json"
            try:
                row = json.loads(p.read_text())
                if row.get("valid") is True and row.get("execution_mode") == mode:
                    found[case.name] = attempt
                    break
            except Exception:
                pass
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--run", type=int, default=1)
    ap.add_argument("--total", type=int, required=True)
    ap.add_argument("--mode", required=True)
    ap.add_argument("--pid", type=int, required=True)
    ap.add_argument("--started-at", required=True)
    ap.add_argument("--log", type=Path, required=True)
    args = ap.parse_args()
    samples: list[tuple[float, int]] = []
    while True:
        stamp = time.time()
        valid = valid_attempts(args.root, args.run, args.mode)
        completed = len(valid)
        failures = 0
        errors = 0
        active_cases = []
        for case in sorted((args.root / f"run_{args.run}" / "cases").glob("*")):
            if case.is_dir() and case.name not in valid:
                attempts = sorted(case.glob("attempt_*"), reverse=True)
                if attempts and (attempts[0] / "run.log").exists():
                    active_cases.append(case.name)
        for p in args.root.glob(f"run_{args.run}/cases/*/attempt_*/validation.json"):
            try:
                if json.loads(p.read_text()).get("valid") is False:
                    errors += 1
            except Exception:
                errors += 1
        alive = Path(f"/proc/{args.pid}").exists()
        samples.append((stamp, completed)); samples = samples[-12:]
        rates = [(b[1]-a[1])/(b[0]-a[0]) for a,b in zip(samples,samples[1:]) if b[0] > a[0] and b[1] > a[1]]
        # One positive delta is not enough to estimate a stable throughput.
        # Require at least two independent completion intervals, as mandated
        # by the workspace runtime standard.
        rate = statistics.median(rates) if len(rates) >= 2 else 0.0
        remaining = max(0, args.total-completed)
        eta = f"{remaining/rate/60:.1f} min" if rate > 0 and remaining else ("0 min" if not remaining else "unknown")
        orchestrator_phase = ""
        try:
            orchestrator_phase = json.loads((args.root / "orchestrator_status.json").read_text()).get("phase", "")
        except Exception:
            pass
        phase = orchestrator_phase or ("inference" if alive else ("complete" if completed == args.total else "failed"))
        if not alive and phase != "complete":
            phase = "failed"
        last_event = max((p.stat().st_mtime for p in valid.values()), default=stamp)
        waiting = alive and completed < args.total and stamp-last_event > 1800
        state = {
            "updated_at": now(), "phase": "stalled" if waiting and phase == "inference" else phase,
            "run": args.run, "started_at": args.started_at, "completed": completed, "total": args.total,
            "remaining": remaining, "success": completed, "failed": failures,
            "errors": errors, "eta": eta, "pid": args.pid, "process_alive": alive,
            "log": str(args.log), "output_dir": str(args.root),
            "progress_definition": "completed = validation.json valid=true for this execution mode",
        }
        atomic(args.root / "status.json", json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        text = "\n".join([
            "# SWE-Agent SWE-bench Lite inference 实时进度", "",
            f"- 开始时间：`{args.started_at}`", f"- 更新时间：`{state['updated_at']}`",
            f"- run：`{args.run}`",
            f"- 阶段：**{state['phase']}**", f"- 主进程：`{args.pid}`（{'存活' if alive else '已退出'}）",
            f"- 已完成 case：`{completed}/{args.total}`", f"- 剩余 case：`{remaining}`",
            f"- 成功：`{completed}`", f"- 当前未完成：`{remaining}`",
            f"- 当前活跃 case：`{', '.join(active_cases) if active_cases else 'preparing/unknown'}`",
            f"- 已记录基础设施失败 attempt：`{errors}`", f"- ETA：`{eta}`",
            "- 统计口径：只计入本 run、且 validation.json 的 valid=true 与 execution_mode 匹配的 case；失败 attempt 不计为完成。",
            f"- 原始日志：`{args.log}`", f"- 输出目录：`{args.root}`", "",
        ])
        atomic(args.root / "LIVE_PROGRESS.md", text)
        if not alive:
            return 0 if completed == args.total else 1
        time.sleep(20)


if __name__ == "__main__":
    raise SystemExit(main())
