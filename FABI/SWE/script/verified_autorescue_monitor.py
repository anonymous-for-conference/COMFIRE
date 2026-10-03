#!/usr/bin/env python3
"""Watch a finished Verified run and automatically rescue missing cases."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import verified_local_runner as runner


STATUS = runner.FIXED / 'status.json'
PROGRESS = runner.FIXED / 'RESCUE_PROGRESS.md'
ROOT_PROGRESS = runner.ROOT / f'{runner.FIXED.name}_rescue.md'


def counts() -> tuple[int, int]:
    ids = runner.target_ids()
    return sum(runner.latest_valid(1, iid) is not None for iid in ids), len(ids)


def write_progress(phase: str, detail: str, state: dict | None = None) -> None:
    state = state or {}
    text = '\n'.join([
        '# SWE-bench Verified 自动补跑进度', '',
        f"- 更新时间：`{runner.now()}`",
        f'- 阶段：**{phase}**',
        f'- 说明：{detail}',
        f"- 有效 inference：`{state.get('valid', 0)}/{state.get('expected', 0)}`",
        '',
        '该监视器只在主推理结束后自动补跑缺失 case，然后触发官方 evaluation。',
    ]) + '\n'
    PROGRESS.write_text(text)
    ROOT_PROGRESS.write_text(text)


def load_state() -> dict | None:
    if not STATUS.exists():
        return None
    try:
        return json.loads(STATUS.read_text())
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('run', type=int)
    ap.add_argument('--poll-seconds', type=int, default=60)
    args = ap.parse_args()
    run = args.run
    PROGRESS.parent.mkdir(parents=True, exist_ok=True)
    write_progress('watching', f'监视 run={run} 的主推理状态')
    last_phase = None
    while True:
        state = load_state()
        if state:
            phase = state.get('phase')
            valid = state.get('valid', 0)
            expected = state.get('expected', 0)
            if phase != last_phase:
                write_progress(phase or 'unknown', f'当前状态：{phase}', state)
                last_phase = phase
            if phase == 'complete' and valid == expected:
                write_progress('complete', f'run={run} 已完成，valid={valid}/{expected}', state)
                return 0
            if phase == 'inference_complete':
                if valid == expected:
                    write_progress('evaluation', f'run={run} inference 已满额，开始 evaluation', state)
                    runner.evaluate(run)
                    write_progress('complete', f'run={run} evaluation 已完成', {'valid': valid, 'expected': expected})
                    return 0
                write_progress('rescue', f'run={run} 发现缺失 case，开始自动补跑', state)
                rc = runner.rescue(run)
                state = load_state() or state
                valid, expected = counts()
                write_progress('rescue_complete', f'补跑结束，rc={rc}，valid={valid}/{expected}', state | {'valid': valid, 'expected': expected})
                if valid == expected:
                    write_progress('evaluation', f'run={run} 补跑后开始 evaluation', state | {'valid': valid, 'expected': expected})
                    runner.evaluate(run)
                    write_progress('complete', f'run={run} evaluation 已完成', {'valid': valid, 'expected': expected})
                    return 0
        time.sleep(args.poll_seconds)


if __name__ == '__main__':
    raise SystemExit(main())
