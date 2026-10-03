#!/usr/bin/env python3
"""Evaluate Codex Lite run 2/3 concurrently, then archive the clean intersection."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from cli_lite_concurrent_pipeline import atomic, now, start_service, stop_service


ROOT = Path("<local-data>/coding_agent/EviFuzz")
OUTPUT = ROOT / "codex_gpt54_mini/evaluation_finalize"
RUNNER = ROOT / "script/cli_lite_runner.py"
COLLECTOR = ROOT / "script/collect_cli_lite_clean_cases.py"


def update(status: dict[str, object]) -> None:
    status["updated_at"] = now()
    atomic(OUTPUT / "status.json", status)
    lines = [
        "# Codex gpt-5.4-mini Evaluation Finalizer", "",
        f"- updated_at: `{status['updated_at']}`",
        f"- started_at: `{status['started_at']}`",
        f"- phase: **{status['phase']}**",
        f"- completed evaluations: `{status['completed']}/2`",
        f"- remaining evaluations: `{status['remaining']}`",
        f"- failed evaluations: `{status['failed']}`",
        f"- ETA: `{status['eta']}`",
        f"- PID: `{os.getpid()}`",
        f"- log: `{OUTPUT / 'RUN.log'}`",
        f"- final clean archive: `{ROOT / 'original_passed_cases/Codex/gpt54mini_lite'}`", "",
    ]
    for run in (2, 3):
        item = status["runs"][str(run)]
        lines.append(
            f"- run {run}: `{item['state']}`, PID `{item.get('pid', 'n/a')}`, "
            f"log `{item['log']}`, progress `{ROOT / f'codex_gpt54_mini/run_{run}/LIVE_PROGRESS.md'}`"
        )
    atomic(OUTPUT / "LIVE_PROGRESS.md", "\n".join(lines) + "\n")


def archive(status: dict[str, object]) -> None:
    status["phase"] = "archiving"
    update(status)
    archive_log = OUTPUT / "archive.log"
    with archive_log.open("w") as log:
        subprocess.run([sys.executable, str(COLLECTOR), "codex"], check=True, stdout=log, stderr=subprocess.STDOUT)
    result = json.loads(archive_log.read_text().splitlines()[-1])
    status["phase"] = "complete"
    status["process_alive"] = False
    status["finished_at"] = now()
    status["clean_cases"] = result["clean_cases"]
    status["archive"] = result["destination"]
    update(status)
    with (OUTPUT / "RUN.log").open("a") as log:
        log.write(f"{now()} COMPLETE clean_cases={result['clean_cases']} archive={result['destination']}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-only", action="store_true")
    args = parser.parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    started = now()
    status: dict[str, object] = {
        "updated_at": started, "started_at": started, "phase": "starting",
        "completed": 0, "total": 2, "remaining": 2, "success": 0,
        "failed": 0, "errors": 0, "eta": "unknown", "pid": os.getpid(),
        "process_alive": True, "log": str(OUTPUT / "RUN.log"),
        "output_dir": str(OUTPUT), "runs": {},
    }
    atomic(OUTPUT / "RUN_CONFIG.md", f"""# Evaluation Finalizer Configuration

- started_at: `{started}`
- task: Codex gpt-5.4-mini SWE-bench Lite run 2 and run 3 official evaluation
- mode: two evaluations concurrent, evaluation-only
- evaluation workers per run: `1`
- cache: official harness `cache_level=instance`, `clean=False`
- post-action: archive the official three-run resolved intersection
- runner: `{RUNNER}`
- collector: `{COLLECTOR}`
""")
    services = {}
    processes = {}
    try:
        if args.archive_only:
            status["phase"] = "archiving"
            status["completed"] = 2
            status["remaining"] = 0
            status["success"] = 2
            status["eta"] = "0s"
            for run in (2, 3):
                status["runs"][str(run)] = {
                    "state": "complete", "log": str(OUTPUT / f"run_{run}_evaluation.log")
                }
            archive(status)
            return 0
        for run in (2, 3):
            socket = Path(f"/tmp/evifuzz-codex-lite54-eval-run{run}.sock")
            service = start_service(socket, OUTPUT / f"podman_run_{run}.log")
            log_path = OUTPUT / f"run_{run}_evaluation.log"
            handle = log_path.open("w")
            proc = subprocess.Popen(
                [sys.executable, str(RUNNER), "evaluate", "codex", str(run), str(socket), "--workers", "1"],
                stdout=handle, stderr=subprocess.STDOUT,
            )
            services[run] = (service, socket)
            processes[run] = (proc, handle)
            status["runs"][str(run)] = {
                "state": "evaluation", "pid": proc.pid, "socket": str(socket), "log": str(log_path),
            }
        status["phase"] = "evaluation"
        update(status)
        with (OUTPUT / "RUN.log").open("a") as log:
            log.write(f"{started} START run_2/run_3 evaluation-only workers=1\n")
        while processes:
            for run in list(processes):
                proc, handle = processes[run]
                if proc.poll() is None:
                    continue
                handle.close()
                service, socket = services.pop(run)
                stop_service(service, socket)
                processes.pop(run)
                if proc.returncode == 0:
                    status["runs"][str(run)]["state"] = "complete"
                    status["completed"] += 1
                    status["success"] += 1
                else:
                    status["runs"][str(run)]["state"] = f"failed(exit={proc.returncode})"
                    status["failed"] += 1
                    status["errors"] += 1
            status["remaining"] = len(processes)
            status["eta"] = "unknown" if processes else "0s"
            update(status)
            if processes:
                time.sleep(20)
        if status["failed"]:
            raise RuntimeError(f"{status['failed']} Codex evaluations failed")
        archive(status)
        return 0
    except Exception as exc:
        for proc, handle in processes.values():
            if proc.poll() is None:
                proc.terminate()
            handle.close()
        for service, socket in services.values():
            stop_service(service, socket)
        status["phase"] = "failed"
        status["process_alive"] = False
        status["last_error"] = f"{type(exc).__name__}: {exc}"
        update(status)
        with (OUTPUT / "RUN.log").open("a") as log:
            log.write(f"{now()} FAILED {status['last_error']}\n")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
