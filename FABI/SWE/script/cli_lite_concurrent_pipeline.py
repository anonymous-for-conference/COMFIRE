#!/usr/bin/env python3
"""Run Codex run 2/3 and OpenCode run 1/2/3 concurrently, one worker each."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import socket as socket_module
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path("<local-data>/coding_agent/EviFuzz")
PIPE = ROOT / "codex_opencode_gpt54_mini_concurrent_pipeline"
RUNNER = ROOT / "script/cli_lite_runner.py"
TARGETS = [("codex", 2), ("codex", 3), ("opencode", 1), ("opencode", 2), ("opencode", 3)]
MAX_ATTEMPTS = 3


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    if isinstance(value, str):
        tmp.write_text(value)
    else:
        tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def socket_healthy(path: Path) -> bool:
    if not path.exists():
        return False
    client = socket_module.socket(socket_module.AF_UNIX, socket_module.SOCK_STREAM)
    client.settimeout(2)
    try:
        client.connect(str(path))
        client.sendall(b"GET /_ping HTTP/1.0\r\nHost: localhost\r\n\r\n")
        return b"200 OK" in client.recv(256)
    except OSError:
        return False
    finally:
        client.close()


def start_service(socket_path: Path, log_path: Path) -> subprocess.Popen:
    if socket_path.exists():
        socket_path.unlink()
    handle = log_path.open("w")
    proc = subprocess.Popen(
        ["podman", "system", "service", "--time=0", f"unix://{socket_path}"],
        stdout=handle, stderr=subprocess.STDOUT,
    )
    for _ in range(100):
        if socket_healthy(socket_path):
            proc._evifuzz_log_handle = handle  # type: ignore[attr-defined]
            return proc
        if proc.poll() is not None:
            break
        time.sleep(0.1)
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=10)
    handle.close()
    if socket_path.exists():
        socket_path.unlink()
    raise RuntimeError(f"Podman service failed: {socket_path}")


def stop_service(proc: subprocess.Popen, socket_path: Path) -> None:
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=10)
    handle = getattr(proc, "_evifuzz_log_handle", None)
    if handle:
        handle.close()
    if socket_path.exists():
        socket_path.unlink()


def update(status: dict[str, object], phase: str, error: str | None = None) -> None:
    status["updated_at"] = now()
    status["phase"] = phase
    status["error"] = error
    atomic(PIPE / "status.json", status)
    lines = [
        "# Codex/OpenCode gpt-5.4-mini Concurrent Pipeline", "",
        f"- updated_at: `{status['updated_at']}`",
        f"- started_at: `{status['started_at']}`",
        f"- phase: **{phase}**",
        f"- completed runs: `{status['completed_runs']}/{status['total_runs']}`",
        f"- active runs: `{status['active_runs']}`",
        f"- failed runs: `{status['failed_runs']}`",
        f"- pipeline PID: `{os.getpid()}`",
        f"- pipeline log: `{PIPE / 'RUN.log'}`", "",
        "Targets (all concurrent, one inference worker and one evaluation worker per run):",
    ]
    for target in status["targets"]:
        lines.append(
            f"- `{target['agent']}_gpt54_mini/run_{target['run']}`: "
            f"{target['state']} (PID `{target.get('pid', 'n/a')}`), "
            f"progress: `{ROOT / target['relative'] / 'LIVE_PROGRESS.md'}`"
        )
    if error:
        lines += ["", f"- error: `{error}`"]
    atomic(PIPE / "LIVE_PROGRESS.md", "\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("run",))
    parser.parse_args()
    PIPE.mkdir(parents=True, exist_ok=True)
    started = now()
    targets = [
        {"agent": agent, "run": run, "relative": f"{agent}_gpt54_mini/run_{run}", "state": "pending"}
        for agent, run in TARGETS
    ]
    status: dict[str, object] = {
        "updated_at": started, "started_at": started, "phase": "starting",
        "completed_runs": 0, "total_runs": len(TARGETS), "remaining_runs": len(TARGETS),
        "active_runs": 0, "failed_runs": 0, "pid": os.getpid(), "process_alive": True,
        "targets": targets, "log": str(PIPE / "RUN.log"), "output_dir": str(PIPE),
    }
    atomic(PIPE / "RUN_CONFIG.md", f"""# Concurrent Pipeline Configuration

- started_at: `{started}`
- benchmark: `SWE-bench Lite`
- model: `gpt-5.4-mini`
- reasoning effort: `medium`
- targets: Codex run 2/3 and OpenCode run 1/2/3
- scheduling: all five runs concurrent
- inference workers per run: `1`
- official evaluation workers per run: `1`
- maximum service/evaluation recovery attempts per run: `{MAX_ATTEMPTS}`
- each run has a unique Podman socket, service log, sandbox, and output root
- Codex run 1 is preserved and excluded from this supervisor
- runner: `{RUNNER}`
""")
    update(status, "starting")
    with (PIPE / "RUN.log").open("a") as pipeline_log:
        pipeline_log.write(f"{started} START concurrent targets={TARGETS} workers=1\n")
    services: dict[str, tuple[subprocess.Popen, Path]] = {}
    runners: dict[str, tuple[subprocess.Popen, object]] = {}
    attempts = {f"{agent}_run_{run}": 0 for agent, run in TARGETS}
    try:
        def launch(target: dict[str, object], key: str) -> None:
            attempt = attempts[key]
            socket_path = Path(
                f"/tmp/evifuzz-concurrent-{target['agent']}-run{target['run']}-attempt{attempt:02d}.sock"
            )
            service = start_service(
                socket_path,
                PIPE / f"podman_{target['agent']}_run{target['run']}_attempt{attempt:02d}.log",
            )
            services[key] = (service, socket_path)
            run_log_path = ROOT / target["relative"] / "RUN.log"
            run_log_path.parent.mkdir(parents=True, exist_ok=True)
            run_log = run_log_path.open("a")
            try:
                proc = subprocess.Popen(
                    [sys.executable, str(RUNNER), "orchestrate", target["agent"], str(target["run"]),
                     str(socket_path), "--workers", "1"],
                    stdout=run_log, stderr=subprocess.STDOUT,
                )
            except Exception:
                run_log.close()
                stop_service(service, socket_path)
                services.pop(key, None)
                raise
            runners[key] = (proc, run_log)
            target.update({"state": "running", "pid": proc.pid, "socket": str(socket_path), "attempt": attempt})

        def launch_with_retries(target: dict[str, object], key: str) -> bool:
            while attempts[key] < MAX_ATTEMPTS:
                attempts[key] += 1
                target["state"] = f"starting(attempt={attempts[key]})"
                try:
                    launch(target, key)
                    return True
                except Exception as exc:
                    target["state"] = f"retrying(start error: {type(exc).__name__}: {exc})"
                    with (PIPE / "RUN.log").open("a") as pipeline_log:
                        pipeline_log.write(
                            f"{now()} RETRY {key} attempt={attempts[key]} "
                            f"reason={type(exc).__name__}: {exc}\n"
                        )
            target["state"] = "failed(start attempts exhausted)"
            status["failed_runs"] = int(status["failed_runs"]) + 1
            return False

        for target in targets:
            key = f"{target['agent']}_run_{target['run']}"
            launch_with_retries(target, key)
        update(status, "running")
        while runners:
            for target in targets:
                key = f"{target['agent']}_run_{target['run']}"
                if key not in runners:
                    continue
                proc, run_log = runners[key]
                service, socket_path = services[key]
                if proc.poll() is None:
                    if service.poll() is not None or not socket_healthy(socket_path):
                        target["state"] = "service_lost"
                        proc.terminate()
                        try:
                            proc.wait(timeout=30)
                        except subprocess.TimeoutExpired:
                            proc.kill(); proc.wait(timeout=10)
                        run_log.close()
                        stop_service(service, socket_path)
                        del runners[key]; del services[key]
                        if attempts[key] < MAX_ATTEMPTS:
                            launch_with_retries(target, key)
                        else:
                            target["state"] = "failed(service lost; attempts exhausted)"
                            status["failed_runs"] = int(status["failed_runs"]) + 1
                    continue
                run_log.close()
                stop_service(service, socket_path)
                del runners[key]
                del services[key]
                if proc.returncode == 0:
                    target["state"] = "complete"
                    status["completed_runs"] = int(status["completed_runs"]) + 1
                else:
                    if attempts[key] < MAX_ATTEMPTS:
                        target["state"] = f"retrying(exit={proc.returncode})"
                        launch_with_retries(target, key)
                    else:
                        target["state"] = f"failed(exit={proc.returncode})"
                        status["failed_runs"] = int(status["failed_runs"]) + 1
            status["active_runs"] = len(runners)
            status["remaining_runs"] = len(TARGETS) - int(status["completed_runs"])
            terminal_phase = "running" if runners else ("failed" if status["failed_runs"] else "complete")
            update(status, terminal_phase)
            if runners:
                time.sleep(20)
        final_phase = "failed" if status["failed_runs"] else "complete"
        with (PIPE / "RUN.log").open("a") as pipeline_log:
            pipeline_log.write(f"{now()} {final_phase.upper()} all concurrent targets\n")
        status["process_alive"] = False
        update(status, final_phase)
        return 1 if status["failed_runs"] else 0
    except Exception as exc:
        for proc, run_log in runners.values():
            if proc.poll() is None:
                proc.terminate()
            run_log.close()
        for service, socket_path in services.values():
            stop_service(service, socket_path)
        with (PIPE / "RUN.log").open("a") as pipeline_log:
            pipeline_log.write(f"{now()} FAILED {type(exc).__name__}: {exc}\n")
        status["process_alive"] = False
        update(status, "failed", f"{type(exc).__name__}: {exc}")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
