#!/usr/bin/env python3
"""Strictly serial Codex then OpenCode three-run Lite supervisor."""

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
PIPE = ROOT / "codex_opencode_gpt54_mini_pipeline"
RUNNER = ROOT / "script/cli_lite_runner.py"
ORDER = [(agent, run) for agent in ("codex", "opencode") for run in (1, 2, 3)]
MAX_RUN_ATTEMPTS = 3


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def update(phase: str, index: int, current: str, started: str, error: str | None = None) -> None:
    state = {
        "updated_at": now(), "phase": phase, "started_at": started,
        "completed_runs": index, "total_runs": len(ORDER), "remaining_runs": len(ORDER) - index,
        "current_run": current, "pid": os.getpid(), "process_alive": phase not in ("complete", "failed"),
        "log": str(PIPE / "RUN.log"), "output_dir": str(PIPE), "error": error,
    }
    atomic(PIPE / "status.json", json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    atomic(PIPE / "LIVE_PROGRESS.md", "\n".join([
        "# Codex then OpenCode gpt-5.4-mini Pipeline", "",
        f"- updated_at: `{state['updated_at']}`", f"- started_at: `{started}`",
        f"- phase: **{phase}**", f"- completed runs: `{index}/6`",
        f"- remaining runs: `{6-index}`", f"- current run: `{current}`",
        f"- pipeline PID: `{os.getpid()}`", f"- pipeline log: `{PIPE / 'RUN.log'}`",
        f"- current run progress: `{ROOT / current / 'LIVE_PROGRESS.md' if current else 'none'}`",
        "", "Order: Codex run_1 -> run_2 -> run_3 -> OpenCode run_1 -> run_2 -> run_3.",
        *( ["", f"- error: `{error}`"] if error else []),
    ]) + "\n")


def start_service(socket: Path, log: Path) -> subprocess.Popen:
    if socket.exists():
        socket.unlink()
    handle = log.open("w")
    proc = subprocess.Popen(["podman", "system", "service", "--time=0", f"unix://{socket}"], stdout=handle, stderr=subprocess.STDOUT)
    for _ in range(100):
        if socket_healthy(socket):
            proc._evifuzz_log_handle = handle  # type: ignore[attr-defined]
            return proc
        if proc.poll() is not None:
            break
        time.sleep(0.1)
    handle.close()
    raise RuntimeError(f"Podman service failed for {socket}")


def socket_healthy(path: Path) -> bool:
    if not path.exists():
        return False
    client = socket_module.socket(socket_module.AF_UNIX, socket_module.SOCK_STREAM)
    client.settimeout(2)
    try:
        client.connect(str(path))
        client.sendall(b"GET /_ping HTTP/1.0\r\nHost: localhost\r\n\r\n")
        response = client.recv(256)
        return b"200 OK" in response
    except OSError:
        return False
    finally:
        client.close()


def stop_service(proc: subprocess.Popen, socket: Path) -> None:
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait(timeout=10)
    handle = getattr(proc, "_evifuzz_log_handle", None)
    if handle:
        handle.close()
    if socket.exists():
        socket.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("run",), help="start or resume the six-run serial pipeline")
    parser.parse_args()
    PIPE.mkdir(parents=True, exist_ok=True)
    started = now()
    atomic(PIPE / "RUN_CONFIG.md", f"""# Pipeline Configuration

- started_at: `{started}`
- model: `gpt-5.4-mini`
- reasoning effort: `medium`
- benchmark: `SWE-bench Lite`
- order: `Codex run_1..3`, then `OpenCode run_1..3`
- concurrency: `4` inference workers and `4` official evaluation workers per run
- serialization boundary: the previous official evaluation must succeed and its labeled containers must be zero before the next run starts
- runner: `{RUNNER}`
""")
    update("starting", 0, "", started)
    current_index = 0
    current_relative = ""
    for index, (agent, run) in enumerate(ORDER):
        current_index = index
        relative = f"{agent}_gpt54_mini/run_{run}"
        current_relative = relative
        summary = ROOT / relative / "evaluation_summary/official_summary.json"
        if summary.exists():
            data = json.loads(summary.read_text())
            if (
                not data.get("error_ids")
                and int(data.get("error_instances", 0)) == 0
                and int(data.get("resolved_instances", 0)) + int(data.get("unresolved_instances", 0)) == 300
            ):
                with (PIPE / "RUN.log").open("a") as log:
                    log.write(f"{now()} RESUME-SKIP complete {agent} run_{run}\n")
                update("between_runs", index + 1, relative, started)
                continue
        run_succeeded = False
        last_error = "unknown"
        for attempt in range(1, MAX_RUN_ATTEMPTS + 1):
            socket = Path(f"/tmp/evifuzz-{agent}-lite54-run{run}-attempt{attempt:02d}-podman.sock")
            service = start_service(socket, PIPE / f"podman_{agent}_run_{run}_attempt_{attempt:02d}.log")
            try:
                update("running", index, relative, started)
                with (PIPE / "RUN.log").open("a") as log:
                    log.write(f"{now()} START {agent} run_{run} attempt={attempt}\n"); log.flush()
                    run_log_path = ROOT / relative / "RUN.log"
                    run_log_path.parent.mkdir(parents=True, exist_ok=True)
                    run_log = run_log_path.open("a")
                    proc = subprocess.Popen(
                        [sys.executable, str(RUNNER), "orchestrate", agent, str(run), str(socket)],
                        stdout=run_log, stderr=subprocess.STDOUT,
                    )
                    service_failure = None
                    while proc.poll() is None:
                        update("running", index, relative, started)
                        if service.poll() is not None or not socket_healthy(socket):
                            service_failure = "Podman service/socket became unavailable"
                            proc.terminate()
                            try:
                                proc.wait(timeout=30)
                            except subprocess.TimeoutExpired:
                                proc.kill(); proc.wait(timeout=10)
                            break
                        time.sleep(20)
                    run_log.close()
                    if service_failure:
                        raise RuntimeError(service_failure)
                    if proc.returncode:
                        raise RuntimeError(f"{agent} run_{run} failed with exit {proc.returncode}")
                    log.write(f"{now()} COMPLETE {agent} run_{run} attempt={attempt}\n"); log.flush()
                    run_succeeded = True
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                with (PIPE / "RUN.log").open("a") as log:
                    log.write(f"{now()} RETRY {agent} run_{run} attempt={attempt} reason={last_error}\n")
                update("retrying", index, relative, started, last_error)
            finally:
                stop_service(service, socket)
            if run_succeeded:
                break
        if not run_succeeded:
            raise RuntimeError(f"{agent} run_{run} exhausted retries: {last_error}")
        if not summary.exists():
            raise RuntimeError(f"missing official summary after {agent} run_{run}")
        update("between_runs", index + 1, relative, started)
        if run == 3:
            with (PIPE / "RUN.log").open("a") as log:
                subprocess.run(
                    [sys.executable, str(ROOT / "script/collect_cli_lite_clean_cases.py"), agent],
                    stdout=log, stderr=subprocess.STDOUT, check=True,
                )
    update("complete", len(ORDER), "", started)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        started = json.loads((PIPE / "status.json").read_text()).get("started_at", now()) if (PIPE / "status.json").exists() else now()
        index = locals().get("current_index", 0)
        relative = locals().get("current_relative", "")
        update("failed", index, relative, started, f"{type(exc).__name__}: {exc}")
        raise
