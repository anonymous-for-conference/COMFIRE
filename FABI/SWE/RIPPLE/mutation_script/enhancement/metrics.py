"""Extract model-call and token metrics from enhancement run artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError, json.JSONDecodeError):
        return None


def extract(run: Path, agent: str) -> dict[str, int | None]:
    input_tokens = output_tokens = calls = 0
    found = False
    if agent == "codex":
        for path in run.glob("interface/cases/*/attempt_*/codex.jsonl"):
            for line in path.read_text(errors="replace").splitlines():
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
                    usage = event["usage"]
                    input_tokens += int(usage.get("input_tokens", 0) or 0)
                    output_tokens += int(usage.get("output_tokens", 0) or 0)
                    found = True
                if event.get("type") == "item.completed" and isinstance(event.get("item"), dict):
                    # Codex emits one commentary/final agent_message for each
                    # assistant action batch. Unlike turn.completed (one per
                    # top-level task), this tracks internal model rounds.
                    calls += event["item"].get("type") == "agent_message"
    elif agent == "opencode":
        for path in run.glob("interface/cases/*/attempt_*/opencode.jsonl"):
            previous_total = 0
            for line in path.read_text(errors="replace").splitlines():
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") not in ("step_finish", "step_finished"):
                    continue
                part = event.get("part", event)
                tokens = part.get("tokens", {}) if isinstance(part, dict) else {}
                total = int(tokens.get("total", 0) or 0)
                input_tokens += int(tokens.get("input", 0) or 0)
                output_tokens += int(tokens.get("output", 0) or 0)
                if total and total < previous_total:
                    pass
                previous_total = max(previous_total, total)
                calls += 1
                found = True
    else:
        for path in run.glob("interface/**/*.traj"):
            data = read_json(path)
            trajectory = data.get("trajectory", []) if isinstance(data, dict) else []
            latest: dict[str, Any] = {}
            for event in trajectory:
                if not isinstance(event, dict):
                    continue
                info = event.get("info", {})
                stats = info.get("model_stats", {}) if isinstance(info, dict) else {}
                if stats:
                    latest = stats
            if latest:
                input_tokens += int(latest.get("tokens_sent", 0) or 0)
                output_tokens += int(latest.get("tokens_received", 0) or 0)
                calls += int(latest.get("api_calls", 0) or 0)
                found = True
    return {
        "input_tokens": input_tokens if found else None,
        "output_tokens": output_tokens if found else None,
        "total_tokens": input_tokens + output_tokens if found else None,
        "model_calls": calls if found else None,
        "model_calls_source": (
            "codex assistant action batches" if agent == "codex" else
            "opencode step_finish events" if agent == "opencode" else
            "SWE-Agent model_stats.api_calls"
        ) if found else None,
    }
