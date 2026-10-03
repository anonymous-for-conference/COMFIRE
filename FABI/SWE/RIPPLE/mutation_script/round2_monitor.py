#!/usr/bin/env python3
"""Write user-facing live summaries without modifying authoritative worker status."""
from __future__ import annotations

import datetime
import json
import os
import sys
import time
from pathlib import Path

root = Path(sys.argv[1])
interval = 30


def timestamp() -> str:
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic_text(path: Path, value: str) -> None:
    temporary = path.with_name(path.name + f".{os.getpid()}.tmp")
    temporary.write_text(value)
    temporary.replace(path)


def read_status(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


while True:
    status = read_status(root / "status.json")
    heartbeat = timestamp()
    pid = status.get("pid")
    running = False
    if isinstance(pid, int):
        try:
            os.kill(pid, 0)
            running = True
        except OSError:
            pass
    atomic_text(
        root / "LIVE_PROGRESS.md",
        f"# RIPPLE 第二轮进度\n\n"
        f"- 当前阶段：`{status.get('phase', 'unknown')}`\n"
        f"- 已完成：{status.get('completed', 0)}/{status.get('total', 0)}\n"
        f"- 成功：{status.get('success', 0)}；失败：{status.get('failed', 0)}；剩余：{status.get('remaining', 0)}\n"
        f"- 主进程：PID `{pid}`；运行中：`{running}`\n"
        f"- 权威事件更新时间：`{status.get('updated_at', 'unknown')}`\n"
        f"- Monitor 心跳：`{heartbeat}`\n"
        f"- ETA：`{status.get('eta', 'unknown')}`\n"
        f"- 主日志：`{status.get('log', root / 'RUN.log')}`\n"
        f"- 输出目录：`{root}`\n",
    )
    for agent in ("codex", "sweagent", "opencode"):
        agent_status = read_status(root / agent / "status.json")
        if not agent_status:
            continue
        atomic_text(
            root / agent / "LIVE_PROGRESS.md",
            f"# {agent} live progress\n\n"
            f"- 阶段：`{agent_status.get('phase', 'unknown')}`\n"
            f"- 完成：{agent_status.get('completed', 0)}/{agent_status.get('total', 0)}\n"
            f"- 成功：{agent_status.get('success', 0)}\n"
            f"- 失败/基础设施错误：{agent_status.get('failed', 0)}/{agent_status.get('errors', 0)}\n"
            f"- 剩余：{agent_status.get('remaining', 0)}\n"
            f"- Worker：{agent_status.get('workers', 'unknown')}\n"
            f"- 最近 case：`{agent_status.get('last_instance_id', 'none')}`\n"
            f"- 主进程：PID `{pid}`；运行中：`{running}`\n"
            f"- 权威事件更新时间：`{agent_status.get('updated_at', 'unknown')}`\n"
            f"- Monitor 心跳：`{heartbeat}`\n"
            f"- 输出目录：`{root / agent}`\n",
        )
    if status.get("phase") in {"completed", "failed", "completed_with_failures"} or (pid and not running):
        break
    time.sleep(interval)
