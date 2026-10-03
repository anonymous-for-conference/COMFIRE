#!/usr/bin/env python3
"""Independent atomic heartbeat for the full RIPPLE run."""
from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import time
from collections import deque
from pathlib import Path

import mutation_pipeline as mp


def alive(pid: int | None) -> bool:
    if not pid:
        return False
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def atomic_text(path: Path, text: str) -> None:
    tmp = path.with_name(path.name + f".tmp.{os.getpid()}")
    tmp.write_text(text)
    os.replace(tmp, path)


def live_evaluation_count(path: Path) -> int:
    """Count current-attempt harness completions from its own progress log."""
    try:
        with path.open("rb") as handle:
            handle.seek(0, os.SEEK_END)
            handle.seek(max(0, handle.tell() - 65536))
            tail = handle.read().decode("utf-8", errors="replace")
    except FileNotFoundError:
        return 0
    matches = re.findall(r"(\d+) ran successfully,\s*(\d+) failed", tail)
    return sum(map(int, matches[-1])) if matches else 0


def infrastructure_error(event: dict) -> bool:
    message = str(event.get("error", "")).lower()
    return any(marker in message for marker in (
        "upstream_error", "temporarily unavailable", "error code: 429",
        "error code: 502", "error code: 503", "error code: 504",
        "connection error", "connection reset", "api timeout",
        "codex exploration timed out", "no space left on device",
    ))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--runner-pid", type=int, required=True)
    parser.add_argument("--attempt-label", default="")
    args = parser.parse_args()
    root = args.run_root.resolve()
    config = read_json(root / "RUN_CONFIG.json")
    run_id = config["run_id"]
    attempt = read_json(root / f"ATTEMPT_{args.attempt_label}.json") if args.attempt_label else {}
    started = attempt.get("started_at", config["started_at"])
    log = root / (f"RUN_{args.attempt_label}.log" if args.attempt_label else "RUN.log")
    baseline = int(attempt.get("cache_hit", 0))
    cached_cases = {tuple(key) for key in attempt.get("cached_cases", [])}
    if not cached_cases and attempt.get("cache_source_attempt"):
        source = attempt["cache_source_attempt"]
        try:
            cached_cases = {(e["agent"], e["instance_id"])
                            for e in (json.loads(line) for line in (root / "events.jsonl").read_text().splitlines())
                            if e.get("attempt") == source and e.get("kind") == "case"
                            and e.get("stage") == "mutation" and e.get("result") == "success"}
        except FileNotFoundError:
            pass
    if baseline != len(cached_cases):
        raise RuntimeError(f"cache manifest mismatch: recorded={baseline}, cases={len(cached_cases)}")
    total = config["total"]
    samples = deque(maxlen=8)
    previous = -1
    last_event = started
    last_progress = started
    while True:
        stamp = mp.now()
        events = []
        try:
            events = [json.loads(line) for line in (root / "events.jsonl").read_text().splitlines() if line.strip()]
        except FileNotFoundError:
            pass
        if args.attempt_label:
            events = [item for item in events if item.get("attempt") == args.attempt_label]
        mutation_by_case = {(e.get("agent"), e.get("instance_id")): e for e in events
                            if e.get("kind") == "case" and e.get("stage") == "mutation"}
        mutation_events = list(mutation_by_case.values())
        completed = len(mutation_events)
        success = sum(e.get("result") == "success" for e in mutation_events)
        failed = sum(e.get("result") == "error" for e in mutation_events)
        cached_completed = sum(e.get("result") == "success" and
                               (e.get("agent"), e.get("instance_id")) in cached_cases
                               for e in mutation_events)
        executed = success - cached_completed
        verified_patches = baseline + executed
        pending_patches = max(0, total - verified_patches)
        phase_events = [e for e in events if e.get("kind") in ("phase", "terminal")]
        phase = phase_events[-1]["phase"] if phase_events else "starting"
        if events:
            last_event = events[-1]["at"]
        eta = "unknown"
        harness = read_json(root / "status.json")
        harness_active = bool(harness.get("agents"))
        if harness_active and harness.get("agents"):
            evaluation = harness.get("agents", {})
            infer_completed = harness.get("completed", 0)
            phase = harness.get("phase", phase)
            evaluated = sum(max(int(item.get("evaluation_completed", 0))
                                + int(item.get("evaluation_empty", 0))
                                + int(item.get("evaluation_errors", 0)),
                                live_evaluation_count(root / agent / f"evaluation_{args.attempt_label}.log"))
                            for agent, item in evaluation.items())
            resolved = sum(int(item.get("evaluation_resolved", 0)) for item in evaluation.values())
            unresolved = sum(int(item.get("evaluation_unresolved", 0)) for item in evaluation.values())
            errors = int(harness.get("errors", 0))
            summary = (f"inference `{infer_completed}/{total}`, evaluation `{evaluated}/{total}`, "
                       f"resolved `{resolved}`, unresolved `{unresolved}`, outstanding infrastructure errors `{errors}`")
            completed = infer_completed
            if completed != previous:
                samples.append((time.monotonic(), completed))
                previous = completed
                last_progress = stamp
            success = int(harness.get("success", 0))
            failed = int(harness.get("failed", 0))
            last_event = harness.get("updated_at", last_event)
            eta = "unknown"
            if len(samples) >= 2 and completed < total:
                rates = [(b[1] - a[1]) / (b[0] - a[0]) for a, b in zip(samples, list(samples)[1:])
                         if b[0] > a[0] and b[1] > a[1]]
                if rates:
                    elapsed = max(1, time.time() - __import__("datetime").datetime.fromisoformat(started).timestamp())
                    cumulative = executed / elapsed
                    rate = min(statistics.median(rates), cumulative) if cumulative > 0 else statistics.median(rates)
                    eta = f"{(total - completed) / rate / 3600:.1f}h (conservative of cumulative and {len(rates)} recent inference intervals)"
            elif completed == total and evaluated < total:
                eta = "unknown (evaluation in progress)"
        else:
            if executed != previous:
                samples.append((time.monotonic(), executed))
                previous = executed
                last_progress = stamp
            if len(samples) >= 2 and pending_patches:
                rates = [(b[1] - a[1]) / (b[0] - a[0]) for a, b in zip(samples, list(samples)[1:])
                         if b[0] > a[0] and b[1] > a[1]]
                if rates:
                    eta = f"{pending_patches / statistics.median(rates) / 3600:.1f}h (median new patch rate)"
            summary = (f"current-attempt events `{completed}/{total}`, successful `{success}`, failed `{failed}`; "
                       f"verified patches `{verified_patches}/{total}`")
            errors = sum(infrastructure_error(e) for e in mutation_events
                         if e.get("result") == "error")
            if not harness_active:
                mp.write_json(root / "status.json", {
                    "updated_at": stamp, "phase": phase, "started_at": started,
                    "completed": completed, "total": total, "remaining": total - completed,
                    "success": success, "failed": failed, "errors": errors, "eta": eta,
                    "pid": args.runner_pid if alive(args.runner_pid) else None,
                    "log": str(log), "output_dir": str(root),
                    "last_event_at": last_event, "cache_hit": baseline,
                    "cache_hits_completed": cached_completed,
                    "executed_this_run": executed, "verified_patches": verified_patches,
                    "mutation_remaining_patches": pending_patches, "run_id": run_id,
                })
        running = alive(args.runner_pid)
        stale = (time.time() - __import__("datetime").datetime.fromisoformat(last_progress).timestamp()) > 120
        note = "stalled: no new case event in over 120 seconds" if stale and running else "waiting" if running else "stopped"
        if stale and running and phase == "mutation":
            eta = "unknown (no new patch in over 120 seconds)"
            current = read_json(root / "status.json")
            if not harness_active:
                current["eta"] = eta
                mp.write_json(root / "status.json", current)
        terminal = not running
        if not running and phase not in {"complete", "failed", "mutation_failed", "harness_failed"}:
            phase = "failed"
        if terminal and not harness_active:
            final_state = read_json(root / "status.json")
            final_state.update({"updated_at": stamp, "phase": phase, "pid": None,
                                "eta": "unknown", "ended_at": stamp})
            mp.write_json(root / "status.json", final_state)
        if harness_active:
            harness.update({"updated_at": stamp, "phase": phase, "started_at": started,
                            "completed": completed, "total": total,
                            "remaining": max(0, total - completed), "eta": eta,
                            "pid": args.runner_pid if running else None, "log": str(log),
                            "run_id": run_id, "cache_hit": baseline,
                            "cache_hits_completed": cached_completed,
                            "executed_this_run": executed,
                            "verified_patches": verified_patches,
                            "mutation_remaining_patches": pending_patches,
                            "last_event_at": last_event, "last_progress_at": last_progress,
                            "activity": note, "mutation_completed": len(mutation_events),
                            "evaluation_live_completed": evaluated})
            mp.write_json(root / "status.json", harness)
        lines = ["# RIPPLE full mutation run", "", f"- run: `{run_id}`",
                 f"- started_at: `{started}`", f"- updated_at: `{stamp}`",
                 f"- phase: **{phase}**", f"- progress: {summary}",
                 f"- remaining cases: `{max(0, total - completed)}`",
                 f"- infrastructure errors: `{errors}`", f"- ETA: `{eta}`",
                 f"- recent activity: `{note}`", f"- last event: `{last_event}`",
                 f"- runner PID: `{args.runner_pid if running else 'stopped'}`",
                 f"- verified cache available: `{baseline}`; cache successes recorded: `{cached_completed}`; newly executed successes: `{executed}`",
                 f"- verified patches: `{verified_patches}/{total}`; still lacking mutation patches: `{pending_patches}`",
                 f"- RUN log: `{log}`",
                 f"- output: `{root}`", ""]
        if terminal:
            lines.extend([f"- ended_at: `{stamp}`", f"- monitor exit: `terminal phase {phase}`",
                          f"- result export: `{root / 'export'}`", ""])
        atomic_text(root / "LIVE_PROGRESS.md", "\n".join(lines))
        if terminal:
            break
        time.sleep(5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
