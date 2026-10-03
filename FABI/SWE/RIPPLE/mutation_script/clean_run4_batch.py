#!/usr/bin/env python3
"""Run unmutated clean inference/evaluation and archive each result as run_4."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import threading
from pathlib import Path

ROOT = Path('/data/zlyuaj/coding_agent/EviFuzz')
REPOS = Path('/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories')
SPECIAL = {'pytest-dev/pytest': Path('/data/zlyuaj/coding_agent/Real_inconsistency_mining/pytest'),
           'scikit-learn/scikit-learn': Path('/data/zlyuaj/coding_agent/sklearn')}
SANDBOXES = {
    'codex': Path('/data/zlyuaj/efl_codex_lite54_run3'),
    'sweagent': Path('/data/zlyuaj/efl_lite_gpt54mini_run3'),
    'opencode': Path('/data/zlyuaj/efl_opencode_lite54_run3'),
}
SETTINGS = {
    'codex': ('Codex', 149), 'sweagent': ('SWE-Agent', 74), 'opencode': ('OpenCode', 144),
}
DATASET = Path('/data/zlyuaj/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json')


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec='seconds')


def atomic_json(path: Path, value: object) -> None:
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


def repo_for(slug: str) -> Path:
    return SPECIAL.get(slug, REPOS / slug.split('/', 1)[1])


def private_repo(staging: Path, iid: str, base: Path, commit: str, candidate: Path | None = None) -> Path:
    """Materialize an unmodified repository exactly at the task base commit."""
    target = staging / 'repositories' / iid
    if (target / '.git').exists():
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=target, text=True).strip()
        if head == commit:
            return target
        raise RuntimeError(f'{iid}: existing clean repository head {head} != {commit}')
    target.parent.mkdir(parents=True, exist_ok=True)
    # Always materialize a fresh isolated worktree from the canonical local
    # repository.  Run3 agent sandboxes can have missing Git blobs after
    # concurrent mutation/evaluation; reusing one makes a nominal clean run
    # fail before inference starts.  A worktree shares immutable objects but
    # has its own index and working files, so cases cannot interfere.
    try:
        subprocess.run(['git', 'worktree', 'add', '--detach', str(target), commit],
                       cwd=base, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True, check=True)
        return target
    except (OSError, subprocess.CalledProcessError):
        if target.exists():
            shutil.rmtree(target, ignore_errors=True)
    clone_source = base
    candidates = [candidate] if candidate and candidate.exists() else []
    if candidate and candidate.parent.parent.exists():
        candidates.extend(sorted(candidate.parent.parent.parent.glob('c*/a01/repo')))
    for option in candidates:
        try:
            subprocess.run(['git', 'cat-file', '-e', f'{commit}^{{commit}}'], cwd=option,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            subprocess.run(['git', 'reset', '--hard', commit], cwd=option,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            return option
        except (OSError, subprocess.CalledProcessError):
            continue
    # Existing run3 sandboxes are one-repository-per-case and already at the
    # exact commit. Reuse them directly to avoid hundreds of expensive clones;
    # run_agent restores each path to this commit after interface completion.
    if clone_source != base:
        return clone_source
    raise RuntimeError(f'{iid}: no clean sandbox repository contains base commit {commit}')


def prepare_agent(agent: str, root: Path) -> tuple[list[str], Path, Path]:
    display, expected = SETTINGS[agent]
    cases = ROOT / 'original_passed_cases' / display / 'gpt54mini_lite' / 'cases'
    dataset_order = {row['instance_id']: index for index, row in enumerate(json.loads(DATASET.read_text()))}
    records = []
    mapping = {}
    case_paths = sorted((path for path in cases.iterdir() if (path / 'task.json').is_file()),
                        key=lambda path: dataset_order.get(path.name, 10**9))
    for index, case in enumerate(case_paths):
        task = case / 'task.json'
        if not task.is_file():
            continue
        row = json.loads(task.read_text())
        iid = row['instance_id']
        base = repo_for(row['repo'])
        if not (base / '.git').exists():
            raise FileNotFoundError(f'{agent} {iid}: local repo missing: {base}')
        target = case / 'run_4'
        if target.exists():
            raise FileExistsError(f'run_4 already exists: {target}')
        records.append(row)
        candidate = None
        if agent == 'sweagent':
            validation = case / 'run_3' / 'validation.json'
            if validation.is_file():
                try: candidate = Path(json.loads(validation.read_text()).get('repo', ''))
                except Exception: candidate = None
        else:
            candidate = SANDBOXES[agent] / f'c{index:03d}' / 'a01' / 'repo'
        mapping[iid] = str(private_repo(root / agent, iid, base, row['base_commit'], candidate).resolve())
    if len(records) != expected:
        raise RuntimeError(f'{agent}: expected {expected} cases, found {len(records)}')
    staging = root / agent
    staging.mkdir(parents=True, exist_ok=True)
    records_path = staging / 'records.json'; records_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    map_path = staging / 'repo_map.json'; map_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + '\n')
    atomic_json(staging / 'status.json', {'phase': 'prepared', 'total': len(records), 'completed': 0,
                                          'remaining': len(records), 'success': 0, 'failed': 0,
                                          'updated_at': now(), 'output_dir': str(staging)})
    return [r['instance_id'] for r in records], records_path, map_path


def archive(agent: str, staging: Path) -> dict:
    display, _ = SETTINGS[agent]
    source_cases = ROOT / 'original_passed_cases' / display / 'gpt54mini_lite' / 'cases'
    interface_cases = staging / 'interface' / 'cases'
    archived = 0
    errors = []
    for case in sorted(source_cases.iterdir()):
        if not (case / 'task.json').exists():
            continue
        iid = case.name
        src = interface_cases / iid
        attempts = sorted(src.glob('attempt_*'), reverse=True)
        selected = next((p for p in attempts if (p / 'prediction.json').is_file() and (p / 'validation.json').is_file()), None)
        if selected is None:
            errors.append({'instance_id': iid, 'error': 'missing terminal attempt artifact'})
            continue
        target = case / 'run_4'
        shutil.copytree(selected, target)
        archived += 1
    return {'archived': archived, 'errors': errors, 'total': len(list(source_cases.glob('*/task.json')))}


def run_agent(agent: str, root: Path, workers: int) -> None:
    ids, records, repo_map = prepare_agent(agent, root)
    staging = root / agent
    interface = ROOT / 'RIPPLE/swe-bench-lite_interface.py'
    output = staging / 'interface'
    socket = Path(f'/tmp/ripple-clean-run4-{root.name}-{agent}.sock')
    cmd = [os.environ.get('PYTHON', 'python'), str(interface), 'run', '--agent', agent,
           '--ids', ','.join(ids), '--repo-map', str(repo_map), '--output', str(output),
           '--workers', str(workers), '--run', '4', '--socket', str(socket)]
    (staging / 'COMMAND.txt').write_text(' '.join(cmd) + '\n')
    with (staging / 'RUN.log').open('w') as log:
        proc = subprocess.Popen(cmd, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, env=os.environ.copy())
        atomic_json(staging / 'process.json', {'pid': proc.pid, 'started_at': now(), 'command': cmd})
        rc = proc.wait()
    # Restore every direct run3 sandbox repository after inference/evaluation.
    commit_by_id = {row['instance_id']: row['base_commit'] for row in json.loads(records.read_text())}
    for iid, repo in json.loads(repo_map.read_text()).items():
        try:
            subprocess.run(['git', 'reset', '--hard', commit_by_id[iid]], cwd=repo,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        except Exception:
            pass
    result = {'agent': agent, 'returncode': rc, 'finished_at': now()}
    if rc == 0:
        result['archive'] = archive(agent, staging)
    atomic_json(staging / 'RESULT.json', result)
    atomic_json(staging / 'status.json', {'phase': 'completed' if rc == 0 else 'failed',
                                          'total': len(ids), 'completed': result.get('archive', {}).get('archived', 0),
                                          'remaining': len(ids) - result.get('archive', {}).get('archived', 0),
                                          'success': result.get('archive', {}).get('archived', 0),
                                          'failed': len(result.get('archive', {}).get('errors', [])) if rc == 0 else len(ids),
                                          'updated_at': now(), 'returncode': rc, 'output_dir': str(staging)})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(); root = args.output.resolve(); root.mkdir(parents=True, exist_ok=False)
    atomic_json(root / 'RUN_CONFIG.json', {'run_id': root.name, 'started_at': now(), 'agents': SETTINGS,
                                           'workers': {'codex': 1, 'sweagent': 1, 'opencode': 1},
                                           'mutation': 'none; original local repositories supplied via repo-map',
                                           'inference_model': 'gpt-5.4-mini', 'evaluation': 'official SWE-bench Lite',
                                           'output_dir': str(root)})
    for agent in SETTINGS:
        prepare_agent(agent, root)
    threads = [threading.Thread(target=run_agent, args=(agent, root, 1), name=agent) for agent in SETTINGS]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    results = {agent: json.loads((root / agent / 'RESULT.json').read_text()) if (root / agent / 'RESULT.json').exists() else {'error': 'no result'} for agent in SETTINGS}
    atomic_json(root / 'SUMMARY.json', {'finished_at': now(), 'results': results})
    return 0 if all(item.get('returncode') == 0 and not item.get('archive', {}).get('errors') for item in results.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
