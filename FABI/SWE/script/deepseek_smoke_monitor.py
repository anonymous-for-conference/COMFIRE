#!/usr/bin/env python3
"""Maintain one visible aggregate progress page for the DeepSeek smoke test."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import time
from pathlib import Path


ROOT = Path(os.environ.get(
    "DEEPSEEK_SMOKE_ROOT",
    "<local-data>/coding_agent/EviFuzz/deepseek_v4_flash_smoke",
))
AGENTS = ("sweagent", "codex", "opencode")
STARTED_AT = os.environ.get("DEEPSEEK_SMOKE_STARTED_AT", dt.datetime.now().astimezone().isoformat(timespec="seconds"))


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic_text(path: Path, value: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(value)
    tmp.replace(path)


def load_state(agent: str) -> dict:
    path = ROOT / agent / "status.json"
    if not path.exists():
        return {"phase": "starting", "completed": 0, "total": 2, "success": 0, "failed": 0, "errors": 0, "eta": "unknown"}
    try:
        state = json.loads(path.read_text())
        if agent == "sweagent" and state.get("phase") == "evaluation":
            # The historical SWE-Agent orchestrator reports inference-valid
            # counts during evaluation. Rebase the aggregate page on current
            # official harness artifacts so stage counters cannot be confused.
            report_root = Path(
                "<local-data>/coding_agent/SWE-bench-eval/logs/run_evaluation/"
                "evifuzz-lite-deepseekv4flash-smoke-run1/evifuzz-deepseekv4flash-smoke-run1"
            )
            reports = list(report_root.glob("*/report.json")) if report_root.exists() else []
            resolved = 0
            for report in reports:
                try:
                    row = json.loads(report.read_text())
                    resolved += int(bool(row.get(report.parent.name, {}).get("resolved")))
                except (OSError, json.JSONDecodeError):
                    pass
            log = ROOT / agent / "logs/run_1_evaluation.log"
            errors = 0
            eta = "unknown"
            if log.exists():
                matches = re.findall(r"Evaluation:.*?(\d+)\s*/\s*(\d+).*?error=(\d+).*?✓=(\d+).*?✖=(\d+).*?\[.*?<([^,\]]+)", log.read_text(errors="replace"))
                if matches:
                    _, _, errors_raw, _, _, eta = matches[-1]
                    errors = int(errors_raw)
            state.update({
                "updated_at": now(), "completed": len(reports), "total": 2,
                "remaining": 2 - len(reports), "success": resolved,
                "failed": len(reports) - resolved, "errors": errors, "eta": eta,
            })
        return state
    except (OSError, json.JSONDecodeError) as exc:
        return {"phase": "inconsistent", "completed": 0, "total": 2, "success": 0, "failed": 0, "errors": 1, "eta": "unknown", "last_error": str(exc)}


def tmux_alive(agent: str) -> bool:
    result = subprocess.run(
        ["tmux", "-L", f"ds_smoke_{agent}", "has-session", "-t", f"ds_smoke_{agent}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def render(states: dict[str, dict]) -> str:
    stamp = now()
    lines = [
        "# DeepSeek v4 Flash Three-Agent Smoke Test", "",
        f"- updated_at: `{stamp}`", f"- started_at: `{STARTED_AT}`",
        "- benchmark: `SWE-bench Lite`", "- cases: `2`",
        "- workers per agent: `2`", "- pipeline: `inference -> official Docker evaluation`", "",
        "| Agent | Phase | Progress | Success/Resolved | Failed/Unresolved | Errors | ETA | tmux |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for agent in AGENTS:
        state = states[agent]
        lines.append(
            f"| {agent} | {state.get('phase', 'unknown')} | "
            f"{state.get('completed', 0)}/{state.get('total', 2)} | "
            f"{state.get('success', state.get('valid', 0))} | "
            f"{state.get('failed', 0)} | {state.get('errors', 0)} | "
            f"{state.get('eta', 'unknown')} | {'alive' if tmux_alive(agent) else 'exited'} |"
        )
    lines += ["", "## Paths", ""]
    for agent in AGENTS:
        lines.append(f"- {agent}: `{ROOT / agent / 'LIVE_PROGRESS.md'}`")
        lines.append(f"- {agent} log: `{ROOT / agent / 'RUN.log'}`")
    lines += ["", "Progress is read from each current run's status file, not inferred from directory counts.", ""]
    return "\n".join(lines)


def main() -> int:
    ROOT.mkdir(parents=True, exist_ok=True)
    while True:
        states = {agent: load_state(agent) for agent in AGENTS}
        atomic_text(ROOT / "LIVE_PROGRESS.md", render(states))
        terminal = all(state.get("phase") in {"complete", "failed"} for state in states.values())
        sessions = any(tmux_alive(agent) for agent in AGENTS)
        if terminal and not sessions:
            return 0
        time.sleep(20)


if __name__ == "__main__":
    raise SystemExit(main())
