#!/usr/bin/env python3
"""Bounded, progress-gated retry for one relational mutation run."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INFRA_MARKERS = ("upstream_error", "temporarily unavailable", "error code: 429",
                 "error code: 502", "error code: 503", "error code: 504",
                 "connection error", "connection reset", "api timeout",
                 "codex exploration timed out", "no space left on device")


def timestamp() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text())


def write_state(path: Path, **fields) -> None:
    tmp = path.with_name(path.name + f".tmp.{os.getpid()}")
    tmp.write_text(json.dumps({"updated_at": timestamp(), **fields}, indent=2) + "\n")
    os.replace(tmp, path)


def alive(pid: int | None) -> bool:
    if not pid:
        return False
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False


def verified_patch_count(root: Path) -> int:
    count = 0
    for meta_path in root.glob("patches/*/*/mutation.json"):
        meta = read_json(meta_path)
        patch = meta_path.with_name("mutation.patch")
        if hashlib.sha256(patch.read_bytes()).hexdigest() != meta.get("sha256"):
            raise RuntimeError(f"cached patch checksum mismatch: {patch}")
        count += 1
    return count


def attempt_events(root: Path, label: str) -> list[dict]:
    return [item for item in (json.loads(line) for line in (root / "events.jsonl").read_text().splitlines())
            if item.get("attempt") == label]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--first-attempt", type=int, default=4)
    parser.add_argument("--max-attempt", type=int, default=7)
    args = parser.parse_args()
    root = args.run_root.resolve()
    status = root / "AUTO_RECOVERY_STATUS.json"
    for number in range(args.first_attempt, args.max_attempt + 1):
        label = f"attempt_{number:02d}"
        record = read_json(root / f"ATTEMPT_{label}.json")
        pid = record["runner_pid"]
        baseline = record["cache_hit"]
        if not pid:
            raise RuntimeError(f"runner PID absent for {label}")
        print(f"[{timestamp()}] watching {label} runner={pid} cached={baseline}", flush=True)
        while alive(pid):
            write_state(status, run_id=root.name, phase="watching", attempt=label,
                        runner_pid=pid, baseline_verified_patches=baseline,
                        next_action="wait for exact runner PID to exit")
            time.sleep(15)
        record = read_json(root / f"ATTEMPT_{label}.json")
        for _ in range(6):
            if not alive(record.get("monitor_pid")):
                break
            time.sleep(5)
        if alive(record.get("monitor_pid")):
            reason = f"previous monitor did not exit for {label}"
            write_state(status, run_id=root.name, phase="needs_review", attempt=label,
                        runner_pid=None, reason=reason)
            print(f"[{timestamp()}] needs_review: {reason}", flush=True)
            return 1
        events = attempt_events(root, label)
        terminal = next((event for event in reversed(events) if event.get("kind") == "terminal"), None)
        try:
            count = verified_patch_count(root)
        except Exception as exc:
            write_state(status, run_id=root.name, phase="needs_review", attempt=label,
                        runner_pid=None, reason=f"{type(exc).__name__}: {exc}")
            raise
        if not terminal:
            reason = "runner exited without a terminal event"
        elif terminal["phase"] != "mutation_failed":
            reason = f"terminal phase {terminal['phase']}; automatic mutation retry not applicable"
        elif any(any(marker in str(e.get("error", "")).lower() for marker in INFRA_MARKERS)
                 for e in events if e.get("stage") == "mutation" and e.get("result") == "error"):
            reason = "infrastructure/API error; manual root-cause review required"
        elif count <= baseline:
            reason = f"no increase in verified patches: {count} <= {baseline}"
        elif number >= args.max_attempt:
            reason = f"bounded retry limit reached at {label}"
        else:
            reason = ""
        if reason:
            phase = "complete" if terminal and terminal.get("phase") == "complete" else "needs_review"
            write_state(status, run_id=root.name, phase=phase, attempt=label,
                        runner_pid=None, verified_patches=count, reason=reason)
            print(f"[{timestamp()}] {phase}: {reason}", flush=True)
            return 0 if phase == "complete" else 1
        next_label = f"attempt_{number + 1:02d}"
        write_state(status, run_id=root.name, phase="restarting", attempt=label,
                    verified_patches=count, next_attempt=next_label)
        env = os.environ.copy()
        env["RIPPLE_RETRY_REASON"] = f"Automatic progress-gated retry: {count - baseline} new verified patches in {label}"
        command = ["bash", str(ROOT / "mutation_script/retry_relational.sh"), root.name, next_label]
        print(f"[{timestamp()}] launching {next_label}: {count} verified patches", flush=True)
        try:
            subprocess.run(command, cwd=ROOT, env=env, check=True)
        except subprocess.CalledProcessError as exc:
            write_state(status, run_id=root.name, phase="needs_review", attempt=label,
                        runner_pid=None, verified_patches=count,
                        reason=f"retry launcher failed with exit code {exc.returncode}")
            raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
