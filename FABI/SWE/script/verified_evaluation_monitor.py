#!/usr/bin/env python3
"""Write a human-readable live progress file for one official SWE-bench eval."""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
from pathlib import Path


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: verified_evaluation_monitor.py OUTPUT_ROOT RUN")
    root = Path(sys.argv[1])
    run = int(sys.argv[2])
    run_root = root / f"run_{run}"
    log = root / "logs" / f"run_{run}_evaluation.log"
    progress = root / "LIVE_PROGRESS.md"
    started_file = root / "evaluation_started_at.txt"
    started = started_file.read_text().strip() if started_file.exists() else now()
    # A retry can be launched after the old monitor died.  Use the durable
    # start marker, rather than this monitor's process start time, so logs from
    # the current invocation remain authoritative.
    try:
        started_epoch = dt.datetime.fromisoformat(started).timestamp()
    except ValueError:
        started_epoch = 0.0
    last_done = 0
    last_time = time.monotonic()
    rate = 0.0
    while True:
        text = log.read_text(errors="replace") if log.exists() else ""
        # Official harness emits one result line per instance log and a final
        # report only after all instances finish. Count completed instance logs
        # from the durable harness output tree, not the tqdm display line.
        base = Path("<local-data>/coding_agent/logs/run_evaluation")
        matches = list(base.glob(f"*/evifuzz-gpt56luna-*-run{run}*/*/run_instance.log"))
        total = 498
        done = 0
        errors = 0
        for p in matches:
            if p.stat().st_mtime < started_epoch:
                continue
            s = p.read_text(errors="replace")
            if "Test results:" in s or "Result:" in s or "RESOLVED" in s or "UNRESOLVED" in s:
                done += 1
            if "Traceback" in s or "ERROR" in s or "error" in s.lower():
                errors += 1
        # Cache hits may reuse old instance logs without changing mtime. The
        # harness tqdm line is authoritative for the number dispatched and
        # completed in this evaluation invocation.
        display_lines = re.findall(r"Evaluation:[^\r\n]*", text)
        parsed = []
        for display in display_lines:
            fraction = re.search(r"(\d+)/(\d+)", display)
            counters = {k: int(v) for k, v in re.findall(r"(✓|✖|error)=(\d+)", display)}
            if fraction and {"✓", "✖", "error"} <= counters.keys():
                parsed.append((fraction.group(1), fraction.group(2), counters["✓"], counters["✖"], counters["error"]))
        if parsed:
            dispatched, total_text, successes, failures, harness_errors = parsed[-1]
            total = int(total_text)
            done = int(successes) + int(failures) + int(harness_errors)
            errors = int(harness_errors)
        if done > last_done:
            if last_done > 0:
                elapsed = time.monotonic() - last_time
                rate = (done - last_done) / elapsed if elapsed > 0 else rate
            last_done, last_time = done, time.monotonic()
        remaining = max(total - done, 0)
        eta = "unknown"
        if rate > 0:
            eta = f"{remaining / rate / 60:.1f} min"
        phase = "evaluation"
        # A harness can terminate before producing a final report.  Never
        # leave the user-facing file looking live in that case.
        failed_marker = any(marker in text for marker in (
            "DockerException:", "RuntimeError: evaluation exit=", "conda.cli.main_run:execute"
        ))
        if failed_marker and done < total:
            phase = "failed"
        if done >= total and ("Evaluation complete" in text or "Report" in text):
            phase = "completed"
        status = {
            "updated_at": now(), "phase": phase, "run": run,
            "started_at": started, "completed": done, "total": total,
            "remaining": remaining, "errors_seen": errors, "eta": eta,
            "log": str(log),
        }
        (root / "evaluation_status.json").write_text(json.dumps(status, indent=2) + "\n")
        progress.write_text(
            "# SWE-bench Verified gpt-5.6-luna evaluation 实时进度\n\n"
            f"- 开始时间：`{started}`\n"
            f"- 更新时间：`{status['updated_at']}`\n"
            f"- 阶段：**{phase}**\n"
            f"- 已完成 case：`{done}/{total}`\n"
            f"- 剩余 case：`{remaining}`\n"
            f"- 已观察到错误的 instance log：`{errors}`\n"
            f"- 预计剩余时间：`{eta}`\n"
            f"- 运行日志：`{log}`\n"
        )
        if phase == "completed" or (done >= total and re.search(r"Report written to|Instances resolved:", text)):
            return 0
        if phase == "failed":
            return 2
        time.sleep(20)


if __name__ == "__main__":
    raise SystemExit(main())
