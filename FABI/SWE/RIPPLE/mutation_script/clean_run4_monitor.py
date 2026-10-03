#!/usr/bin/env python3
from __future__ import annotations
import json, os, sys, time
from datetime import datetime
from pathlib import Path

root = Path(sys.argv[1]); interval = 30

def atomic(path: Path, text: str) -> None:
    tmp = path.with_name(path.name + f'.{os.getpid()}.tmp'); tmp.write_text(text); tmp.replace(path)

def read(path: Path) -> dict:
    try: return json.loads(path.read_text())
    except Exception: return {}

while True:
    lines = [f'# Clean run_4 progress', '', f'- 更新时间：`{datetime.now().astimezone().isoformat(timespec="seconds")}`', '']
    terminal = 0; total = 0
    for agent in ('codex', 'sweagent', 'opencode'):
        status = read(root / agent / 'interface' / 'status.json')
        if not status: status = read(root / agent / 'status.json')
        total += int(status.get('total', 0)); done = int(status.get('completed', 0)); terminal += done
        lines.extend([f'## {agent}', f'- 阶段：`{status.get("phase", "starting")}`',
                      f'- 完成：{done}/{status.get("total", 0)}',
                      f'- 成功：{status.get("success", status.get("inference_success", 0))}',
                      f'- 失败：{status.get("failed", status.get("inference_invalid_or_empty", 0))}',
                      f'- 最近更新时间：`{status.get("updated_at", "unknown")}`',
                      f'- 输出：`{root / agent}`', ''])
    lines[2] = f'- 总进度：{terminal}/{total}；monitor 心跳：`{datetime.now().astimezone().isoformat(timespec="seconds")}`'
    atomic(root / 'LIVE_PROGRESS.md', '\n'.join(lines))
    for agent in ('codex', 'sweagent', 'opencode'):
        status = read(root / agent / 'interface' / 'status.json') or read(root / agent / 'status.json')
        if status:
            atomic(root / agent / 'LIVE_PROGRESS.md', '\n'.join([
                f'# {agent} clean run_4 progress', '', f'- 阶段：`{status.get("phase", "starting")}`',
                f'- 完成：{status.get("completed", 0)}/{status.get("total", 0)}',
                f'- 成功：{status.get("success", status.get("inference_success", 0))}',
                f'- 失败：{status.get("failed", status.get("inference_invalid_or_empty", 0))}',
                f'- 更新时间：`{status.get("updated_at", "unknown")}`',
                f'- 输出：`{root / agent}`', '']))
    if all((root / a / 'RESULT.json').exists() for a in ('codex', 'sweagent', 'opencode')): break
    time.sleep(interval)
