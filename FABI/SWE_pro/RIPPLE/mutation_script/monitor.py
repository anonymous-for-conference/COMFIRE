#!/usr/bin/env python3
"""Independent atomic monitor for one RIPPLE smoke run."""

from __future__ import annotations

import argparse
import json
import statistics
import time
from datetime import datetime
from pathlib import Path


TERMINAL = {"complete", "failed", "inconsistent"}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def atomic(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


def alive(pid) -> bool:
    return isinstance(pid, int) and Path(f"/proc/{pid}").exists()


def evaluation_summary(run_root: Path) -> dict:
    agents = {}
    for agent in ("swe-agent", "opencode", "codex"):
        try:
            result = json.loads((run_root / agent / "evaluation_result.json").read_text())
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            continue
        agents[agent] = {
            "status": result.get("status"),
            "completed": int(result.get("completed", 0)),
            "total": int(result.get("total", 0)),
            "input_total": int(result.get("input_total", result.get("total", 0))),
            "officially_excluded": int(result.get("officially_excluded", 0)),
            "resolved": int(result.get("resolved", 0)),
            "unresolved": int(result.get("unresolved", 0)),
            "errors": int(result.get("errors", 0)),
        }
    return {
        "agents": agents,
        "completed": sum(item["completed"] for item in agents.values()),
        "total": sum(item["total"] for item in agents.values()),
        "input_total": sum(item["input_total"] for item in agents.values()),
        "officially_excluded": sum(item["officially_excluded"] for item in agents.values()),
        "resolved": sum(item["resolved"] for item in agents.values()),
        "unresolved": sum(item["unresolved"] for item in agents.values()),
        "errors": sum(item["errors"] for item in agents.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--interval", type=int, default=20)
    parser.add_argument("--attempt", type=int, default=1)
    args = parser.parse_args()
    args.run_root = args.run_root.resolve()
    status_path = args.run_root / "status.json"
    samples: list[tuple[float, int]] = []
    sampled_phase = None
    while True:
        try:
            state = json.loads(status_path.read_text())
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            time.sleep(1)
            continue
        phase = state.get("phase", "unknown")
        if phase != sampled_phase:
            sampled_phase = phase
            samples = []
        completed = int(state.get("completed", 0))
        if not samples or samples[-1][1] != completed:
            samples.append((time.time(), completed))
            samples = samples[-8:]
        rates = [(right[1] - left[1]) / (right[0] - left[0])
                 for left, right in zip(samples, samples[1:]) if right[1] > left[1]]
        eta = "unknown"
        total = int(state.get("total", 0))
        if len(rates) >= 2 and completed < total:
            rate = statistics.median(rates)
            if rate > 0:
                eta = f"{int((total - completed) / rate)}s (median recent completion rate)"
        process_alive = alive(state.get("pid"))
        if phase not in TERMINAL and phase != "prepared" and not process_alive:
            phase = "inconsistent"
            state.update(phase=phase, updated_at=now())
            state.setdefault("error_details", []).append({
                "stage": sampled_phase, "error": "orchestrator process stopped",
            })
            state["errors"] = int(state.get("errors", 0)) + 1
            atomic(status_path, json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        agents = []
        mutation_progress = state.get("mutation_by_agent", {})
        evaluation = state.get("evaluation") or evaluation_summary(args.run_root)
        if evaluation and state.get("evaluation") != evaluation:
            state["evaluation"] = evaluation
            atomic(status_path, json.dumps(state, ensure_ascii=False, indent=2) + "\n")
        evaluation_agents = evaluation.get("agents", {})
        for agent in ("swe-agent", "opencode", "codex"):
            if phase == "mutation" and agent in mutation_progress:
                value = mutation_progress[agent]
                agents.append(
                    f"- {agent}: mutation `{value.get('completed', 0)}/{value.get('total', 0)}`; "
                    f"remaining `{value.get('remaining', 0)}`; active `{value.get('active', 0)}`; "
                    f"success `{value.get('success', 0)}`; failed `{value.get('failed', 0)}`; "
                    f"cases `{value.get('active_cases', {})}`"
                )
                continue
            if phase in {"evaluation", "complete"} and agent in evaluation_agents:
                value = evaluation_agents[agent]
                agents.append(
                    f"- {agent}: evaluation `{value.get('completed', 0)}/{value.get('total', 0)}`; "
                    f"resolved `{value.get('resolved', 0)}`; unresolved `{value.get('unresolved', 0)}`; "
                    f"officially excluded `{value.get('officially_excluded', 0)}`; "
                    f"errors `{value.get('errors', 0)}`"
                )
                continue
            try:
                value = json.loads((args.run_root / agent / "status.json").read_text())
                agents.append(
                    f"- {agent}: `{value.get('phase')}`; "
                    f"`{value.get('completed', 0)}/{value.get('total', 2)}`; "
                    f"errors `{value.get('errors', 0)}`"
                )
            except (FileNotFoundError, json.JSONDecodeError, OSError):
                agents.append(f"- {agent}: no inference status yet")
        live = f"""# RIPPLE SWE-bench Pro Mutation Run

- Phase: **{phase}**
- Stage order: `mutation -> inference -> evaluation`
- Started: `{state.get('started_at', 'unknown')}`
- Worker status updated: `{state.get('updated_at', 'unknown')}`
- Monitor sampled: `{now()}`
- Current stage completed: `{completed}/{total}`
- Current stage remaining: `{state.get('remaining', 'unknown')}`
- Current stage success: `{state.get('success', 0)}`
- Current stage failed: `{state.get('failed', 0)}`
- Infrastructure errors: `{state.get('errors', 0)}`
- ETA: `{eta}`
- Orchestrator PID: `{state.get('pid', 'unknown')}` ({'alive' if process_alive else 'stopped'})
- Active child PIDs: `{state.get('worker_pids', {})}`
- Main log: `{state.get('log', args.run_root / 'RUN.log')}`
- Output: `{args.run_root}`

## Official Evaluation

- Evaluated: `{evaluation.get('completed', 0)}/{evaluation.get('total', 0)}`
- Input agent-case pairs: `{evaluation.get('input_total', 0)}`
- Officially excluded before execution: `{evaluation.get('officially_excluded', 0)}`
- Resolved: `{evaluation.get('resolved', 0)}`
- Unresolved: `{evaluation.get('unresolved', 0)}`
- Harness errors: `{evaluation.get('errors', 0)}`

## Agents

{chr(10).join(agents)}
"""
        atomic(args.run_root / "LIVE_PROGRESS.md", live)
        if phase in TERMINAL:
            exit_name = "MONITOR_EXIT.json" if args.attempt == 1 else f"MONITOR_EXIT_attempt_{args.attempt:02d}.json"
            atomic(args.run_root / exit_name, json.dumps({
                "exited_at": now(), "reason": f"terminal phase {phase}", "phase": phase,
            }, indent=2) + "\n")
            return 0 if phase == "complete" else 1
        time.sleep(args.interval)


if __name__ == "__main__":
    raise SystemExit(main())
