#!/usr/bin/env python3
"""Resumable four-worker SWE-bench Verified run and official evaluation."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

import verified_local_runner as runner

STATUS = runner.FIXED / 'status.json'
PROGRESS = runner.FIXED / 'PROGRESS.md'
LIVE_PROGRESS = runner.FIXED / 'LIVE_PROGRESS.md'
ROOT_PROGRESS = runner.ROOT / f'{runner.FIXED.name}.md'


def counts(run: int) -> tuple[int, int]:
    ids = runner.target_ids()
    return sum(runner.latest_valid(run, iid) is not None for iid in ids), len(ids)


def update(phase: str, detail: str, **extra) -> None:
    run = int(extra.get('run', 1))
    valid, expected = counts(run)
    state = {'updated_at': runner.now(), 'phase': phase, 'detail': detail,
             'valid': valid, 'expected': expected}
    runner.FIXED.mkdir(parents=True, exist_ok=True)
    target_status = STATUS
    state.update({
        'started_at': __import__('os').environ.get('EVIFUZZ_STARTED_AT', state['updated_at']),
        'completed': valid,
        'total': expected,
        'remaining': expected - valid,
        'success': valid,
        'failed': 0,
        'errors': 0,
        'eta': '0s' if phase == 'complete' else 'unknown',
        'pid': __import__('os').getpid(),
        'process_alive': phase not in {'complete', 'failed'},
        'log': str(runner.FIXED / 'RUN.log'),
        'output_dir': str(runner.FIXED),
    })
    # Caller-supplied terminal/error fields override the generic defaults.
    state.update(extra)
    tmp = target_status.with_suffix('.tmp')
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(target_status)
    text = '\n'.join([
        f'# SWE-bench {runner.BENCHMARK_LABEL} {runner.MODEL} 实时进度', '',
        f"- 更新时间：`{state['updated_at']}`", f'- 阶段：**{phase}**',
        f'- 说明：{detail}', f'- 有效 inference：`{valid}/{expected}`', '',
        '每个 case 的 repo、runtime、trajectory、prediction、validation 和 metrics 均保留。',
    ]) + '\n'
    PROGRESS.write_text(text)
    # Keep the user-facing canonical filename in sync with the historical
    # PROGRESS.md.  Both files are visible in the run root; LIVE_PROGRESS.md
    # is the name used by the common monitoring standard.
    LIVE_PROGRESS.write_text(text)
    if __import__('os').environ.get('AUTHORITATIVE_MONITOR') != '1':
        ROOT_PROGRESS.write_text(text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('run', type=int)
    args = ap.parse_args()
    run = args.run
    runner.FIXED.mkdir(parents=True, exist_ok=True)
    (runner.FIXED / 'logs').mkdir(parents=True, exist_ok=True)
    update('starting', f'启动 run={run} 的 {runner.N_WORKERS} 路隔离本地推理')
    procs = [subprocess.Popen([sys.executable, str(Path(runner.__file__)), 'worker', str(run), str(w)],
                              stdout=(runner.FIXED / 'logs' / f'worker_{w}.stdout.log').open('a'),
                              stderr=subprocess.STDOUT) for w in range(1, runner.N_WORKERS + 1)]
    while any(p.poll() is None for p in procs):
        update('inference', f'{runner.N_WORKERS} 路并发；已完成 case 会在恢复时跳过', run=run, exit_codes=[p.poll() for p in procs])
        time.sleep(20)
    valid, expected = counts(run)
    update('inference_complete', f'推理进程结束，valid={valid}/{expected}', run=run, exit_codes=[p.returncode for p in procs])
    if valid != expected:
        update('rescue', f'发现 {expected - valid} 个未完成 case，自动补跑并修复已知镜像缓存问题', run=run)
        rescue_rc = runner.rescue(run)
        valid, expected = counts(run)
        update('rescue_complete', f'补跑结束，valid={valid}/{expected}', run=run, rescue_rc=rescue_rc)
        if valid != expected:
            raise RuntimeError(f'inference incomplete after rescue: {valid}/{expected}')
    update('evaluation', '使用官方 SWE-bench harness 和官方 Docker 评测', run=run)
    evaluation = subprocess.Popen([sys.executable, str(Path(runner.__file__)), 'evaluate', str(run)])
    while evaluation.poll() is None:
        update('evaluation', '官方 Docker 评测运行中；详细 case 进度见 evaluation log', run=run,
               evaluation_pid=evaluation.pid)
        time.sleep(20)
    if evaluation.returncode:
        raise RuntimeError(f'evaluation exit={evaluation.returncode}')
    update('complete', '本地隔离推理和官方 Docker 评测完成', run=run,
           finished_at=runner.now(), exit_code=0, process_alive=False)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        # Persist a terminal failure instead of leaving a stale running phase.
        update('failed', f'运行失败：{exc}', finished_at=runner.now(), exit_code=1,
               process_alive=False, errors=1, last_error=str(exc))
        raise
