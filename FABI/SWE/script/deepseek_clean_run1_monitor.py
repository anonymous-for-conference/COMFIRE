#!/usr/bin/env python3
"""Maintain visible aggregate progress for the three-agent clean run."""

from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import tempfile
import time
import re
from pathlib import Path


ROOT = Path(os.environ.get(
    "DEEPSEEK_CLEAN_ROOT",
    "<local-data>/coding_agent/EviFuzz/deepseek_v4_flash_clean_run1",
))
AGENTS = ("sweagent", "codex", "opencode")
TOTAL = 300
WORKERS = (1, 2)
STARTED_AT = os.environ.get(
    "DEEPSEEK_CLEAN_STARTED_AT",
    dt.datetime.now().astimezone().isoformat(timespec="seconds"),
)


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic_text(path: Path, value: str) -> None:
    """Replace progress atomically, using a unique temp file per writer."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        os.fchmod(descriptor, 0o644)
        with os.fdopen(descriptor, "w") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        try:
            os.unlink(name)
        except FileNotFoundError:
            pass


def tmux_alive(agent: str) -> bool:
    session = f"ds_clean1_{agent}"
    result = subprocess.run(
        ["tmux", "-L", session, "has-session", "-t", session],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def load_state(agent: str) -> dict:
    path = ROOT / agent / "status.json"
    fallback = {
        "phase": "starting", "completed": 0, "total": TOTAL,
        "remaining": TOTAL, "success": 0, "failed": 0,
        "errors": 0, "eta": "unknown", "updated_at": now(),
    }
    if not path.exists():
        return fallback
    try:
        state = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return {**fallback, "phase": "inconsistent", "errors": 1, "last_error": str(exc)}
    for key, value in fallback.items():
        state.setdefault(key, value)
    # During evaluation, all runners may still expose inference/report-file
    # counts in status.json. Rebase every agent on the current official harness
    # progress line, whose numerator is processed cases and whose checkmarks
    # separately classify resolved/unresolved/error outcomes.
    if state.get("phase") == "evaluation":
        log = (ROOT / agent / "logs" / "run_1_evaluation.log") if agent == "sweagent" else (ROOT / agent / "evaluation.log")
        try:
            text = log.read_text(errors="replace")
        except OSError:
            text = ""
        matches = re.findall(
            r"Evaluation:\s*.*?(\d+)\s*/\s*300.*?✓=(\d+).*?✖=(\d+).*?error=(\d+)",
            text,
        )
        if matches:
            completed, resolved, unresolved, errors = map(int, matches[-1])
            state.update({
                "completed": completed,
                "total": TOTAL,
                "remaining": TOTAL - completed,
                "success": resolved,
                "failed": unresolved,
                "errors": errors,
                "evaluation_completed": completed,
                "evaluation_total": TOTAL,
                "evaluation_resolved": resolved,
                "evaluation_unresolved": unresolved,
                "evaluation_errors": errors,
            })
        else:
            # Evaluation has started but has not emitted its first progress
            # sample yet. Preserve a truthful waiting state.
            state.update({
                "completed": 0, "total": TOTAL, "remaining": TOTAL,
                "success": 0, "failed": 0,
                "evaluation_completed": 0, "evaluation_total": TOTAL,
            })
    return state


def valid_worker_evidence(agent: str) -> dict[int, dict]:
    """Return the earliest persisted valid inference for each worker."""
    case_root = ROOT / agent / ("run_1/cases" if agent == "sweagent" else "cases")
    evidence: dict[int, dict] = {}
    if not case_root.exists():
        return evidence
    for path in case_root.glob("*/attempt_*/validation.json"):
        try:
            row = json.loads(path.read_text())
            worker = int(row.get("worker", 0))
            if row.get("valid") is not True or worker not in WORKERS:
                continue
            item = {
                "instance_id": row.get("instance_id", path.parents[1].name),
                "attempt": row.get("attempt"),
                "mtime": path.stat().st_mtime,
            }
            if worker not in evidence or item["mtime"] < evidence[worker]["mtime"]:
                evidence[worker] = item
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            continue
    return evidence


def render(states: dict[str, dict], worker_evidence: dict[str, dict[int, dict]]) -> str:
    stamp = now()
    lines = [
        "# DeepSeek v4 Flash Three-Agent Clean Run 1", "",
        f"- updated_at: `{stamp}`", f"- started_at: `{STARTED_AT}`",
        "- benchmark: `SWE-bench Lite test (300 cases)`",
        "- model: `deepseek-v4-flash`", "- reasoning effort: `disabled`",
        "- workers per agent: `2`",
        "- pipeline: `local inference -> official Docker evaluation`", "",
        "| Agent | Phase | Completed | Success | Failed | Errors | Remaining | ETA | tmux |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for agent in AGENTS:
        state = states[agent]
        alive = tmux_alive(agent)
        phase = state.get("phase", "unknown")
        if not alive and phase not in {"complete", "failed"}:
            phase = "stopped/error"
        lines.append(
            f"| {agent} | {phase} | {state['completed']}/{state['total']} | "
            f"{state['success']} | {state['failed']} | {state['errors']} | "
            f"{state['remaining']} | {state['eta']} | {'alive' if alive else 'exited'} |"
        )
    lines += ["", "## Worker First-Valid Evidence", ""]
    for agent in AGENTS:
        for worker in WORKERS:
            item = worker_evidence[agent].get(worker)
            description = (
                f"yes: `{item['instance_id']}` attempt `{item['attempt']}`"
                if item else "waiting"
            )
            lines.append(f"- {agent} worker {worker}: {description}")
    lines += ["", "## Paths", ""]
    for agent in AGENTS:
        lines.append(f"- {agent} progress: `{ROOT / agent / 'LIVE_PROGRESS.md'}`")
        lines.append(f"- {agent} raw log: `{ROOT / agent / 'RUN.log'}`")
    lines += [
        "",
        "`Completed` follows each runner's current status.json. A worker is marked first-valid only after a validation.json with valid=true is durably written.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ROOT.mkdir(parents=True, exist_ok=True)
    while True:
        states = {agent: load_state(agent) for agent in AGENTS}
        evidence = {agent: valid_worker_evidence(agent) for agent in AGENTS}
        atomic_text(ROOT / "LIVE_PROGRESS.md", render(states, evidence))
        all_terminal = all(state.get("phase") in {"complete", "failed"} for state in states.values())
        any_session = any(tmux_alive(agent) for agent in AGENTS)
        if all_terminal and not any_session:
            return 0
        time.sleep(20)


if __name__ == "__main__":
    raise SystemExit(main())
