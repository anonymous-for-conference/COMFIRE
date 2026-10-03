#!/usr/bin/env python3
"""Run SWE-Agent and OpenCode RIPPLE batches strictly in sequence."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
BATCH = HERE / "batch_all_clean_staged.py"


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def atomic_text(path: Path, value: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(value)
    temporary.replace(path)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError, json.JSONDecodeError):
        return {}


def update_parent(root: Path, agent: str, child: Path, pid: int | None,
                  finished: list[str], error: str | None = None) -> None:
    child_status = read_json(child / "status.json")
    phase = child_status.get("phase", "waiting")
    status = {
        "updated_at": now(), "phase": "failed" if error else f"{agent}:{phase}",
        "started_at": read_json(root / "SEQUENCE_CONFIG.json").get("started_at"),
        "current_agent": agent, "completed_agents": finished,
        "completed": child_status.get("completed", 0),
        "total": child_status.get("total", 0),
        "remaining": child_status.get("remaining", 0),
        "success": child_status.get("success", 0),
        "failed": child_status.get("failed", 0),
        "errors": child_status.get("errors", 0),
        "eta": child_status.get("eta", "unknown"),
        "pid": pid, "process_alive": bool(pid and Path(f"/proc/{pid}").exists()),
        "log": str(root / "SEQUENCE.log"), "output_dir": str(root),
        "child_output": str(child), "child_log": str(child / "RUN.log"),
        "child_progress": str(child / "LIVE_PROGRESS.md"), "error": error,
    }
    atomic_json(root / "status.json", status)
    atomic_text(root / "LIVE_PROGRESS.md", "\n".join([
        "# RIPPLE Remaining Agents 顺序实验进度", "",
        f"- 更新时间：`{status['updated_at']}`",
        f"- 当前 Agent：`{agent}`；阶段：`{phase}`",
        f"- 当前批次：{status['completed']}/{status['total']} terminal；"
        f"成功 {status['success']}，失败 {status['failed']}，剩余 {status['remaining']}",
        f"- 已完成 Agent：`{finished}`",
        f"- 主进程存活：`{str(status['process_alive']).lower()}`；ETA：`{status['eta']}`",
        f"- 错误：`{error or 'none'}`", "",
        f"- Sequence 日志：`{status['log']}`",
        f"- 当前子批次日志：`{status['child_log']}`",
        f"- 当前子批次进度：`{status['child_progress']}`",
        f"- 输出根目录：`{root}`", "",
        "统计口径：当前数字直接镜像当前 Agent 子批次的权威 status.json；"
        "SWE-Agent 完全 terminal 后才启动 OpenCode。", "",
    ]))


def run_child(root: Path, agent: str, child: Path, session: str,
              workers: int, timeout: int, finished: list[str]) -> int:
    monitor_log = (child / "MONITOR.log").open("a")
    monitor = subprocess.Popen([
        sys.executable, str(BATCH), "--agent", agent, "--output", str(child),
        "--monitor", "--monitor-interval", "20",
    ], stdout=monitor_log, stderr=subprocess.STDOUT, start_new_session=True)
    command = [
        sys.executable, str(BATCH), "--agent", agent, "--output", str(child),
        "--workers", str(workers), "--command-timeout", str(timeout),
        "--tmux-session", session, "--monitor-pid", str(monitor.pid),
    ]
    with (child / "RUN.log").open("a") as run_log:
        process = subprocess.Popen(
            command, stdout=run_log, stderr=subprocess.STDOUT, start_new_session=True,
        )
        while process.poll() is None:
            update_parent(root, agent, child, process.pid, finished)
            time.sleep(20)
        returncode = process.wait()
    deadline = time.time() + 60
    while monitor.poll() is None and time.time() < deadline:
        update_parent(root, agent, child, process.pid, finished)
        time.sleep(2)
    if monitor.poll() is None:
        monitor.terminate()
        try:
            monitor.wait(timeout=15)
        except subprocess.TimeoutExpired:
            monitor.kill()
            monitor.wait(timeout=10)
    monitor_log.close()
    summary = read_json(child / "BATCH_SUMMARY.json")
    if not summary:
        raise RuntimeError(f"{agent} exited {returncode} without BATCH_SUMMARY.json")
    return returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--session", required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--command-timeout", type=int, default=4 * 60 * 60)
    args = parser.parse_args()
    root = args.root.resolve()
    finished: list[str] = []
    exit_codes = {}
    try:
        for agent, directory in (("sweagent", "sweagent"), ("opencode", "opencode")):
            child = root / directory
            update_parent(root, agent, child, os.getpid(), finished)
            exit_codes[agent] = run_child(
                root, agent, child, args.session, args.workers,
                args.command_timeout, finished,
            )
            finished.append(agent)
        atomic_json(root / "SEQUENCE_SUMMARY.json", {
            "finished_at": now(), "agents": finished, "exit_codes": exit_codes,
            "outputs": {agent: str(root / agent) for agent in finished},
        })
        update_parent(root, "none", root / "opencode", None, finished)
        return 0 if all(code == 0 for code in exit_codes.values()) else 1
    except Exception as exc:
        update_parent(root, "failed", root / (finished[-1] if finished else "sweagent"),
                      None, finished, f"{type(exc).__name__}: {exc}")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
