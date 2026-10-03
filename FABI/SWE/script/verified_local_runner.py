#!/usr/bin/env python3
"""Local-repo SWE-Agent inference in the official per-instance container.

The host clone is the durable patch carrier, but every command in one agent
trajectory runs in one long-lived official SWE-bench instance container.  This
avoids the invalid nested ``bubblewrap -> rootless podman`` architecture while
retaining independent, inspectable local repositories for every attempt.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path('<local-data>/coding_agent/EviFuzz')
FIXED = ROOT / os.environ.get('VERIFIED_OUTPUT', 'verified_gpt56_luna')
SANDBOX_ROOT = Path(os.environ.get('VERIFIED_SANDBOX', '<local-data>/efl_verified_gpt56'))
SWE_ROOT = Path('<local-data>/coding_agent/SWE-Agent')
DATA_ROOT = Path(os.environ.get('SWE_DATA_ROOT', '<local-data>/coding_agent/swe-bench-verified'))
DATASET = Path(os.environ.get('SWE_DATASET_FILE', str(DATA_ROOT / 'dataset/swebench_verified_test.json')))
BASE_WORKTREES = DATA_ROOT / 'worktrees'
API_CONFIG = Path('<local-data>/coding_agent/key.txt')
MODEL = os.environ.get('SWE_AGENT_MODEL', 'openai/gpt-5.6-luna')
BENCHMARK_DATASET = os.environ.get('SWE_HARNESS_DATASET', 'SWE-bench/SWE-bench_Verified')
BENCHMARK_LABEL = os.environ.get('SWE_BENCHMARK_LABEL', 'Verified')
MODEL_TAG = os.environ.get('SWE_MODEL_TAG', 'gpt56luna')
CALL_LIMIT = int(os.environ.get('FIXED_LOCAL_CALL_LIMIT', '100'))
N_WORKERS = int(os.environ.get('VERIFIED_WORKERS', '4'))
MAX_ATTEMPTS = int(os.environ.get('VERIFIED_MAX_ATTEMPTS', '3'))
RESCUE_ATTEMPTS = int(os.environ.get('VERIFIED_RESCUE_ATTEMPTS', '3'))
CASE_TIMEOUT = int(os.environ.get('SWE_CASE_TIMEOUT', '3600'))
PODMAN_SOCKET = os.environ.get('VERIFIED_PODMAN_SOCKET', '/tmp/swebench-podman.sock')
SWEREX_ENV = Path('<local-data>/anaconda3/envs/swe-agent')
TASK_PATH = '/opt/miniconda3/envs/testbed/bin:/opt/miniconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
EXECUTION_MODE = f'{BENCHMARK_LABEL.lower()}_local_repo_long_lived_official_container_v1_call{CALL_LIMIT}_out4096'
EXPERIMENT_TAG = os.environ.get(
    'SWE_EXPERIMENT_TAG', re.sub(r'[^a-zA-Z0-9_.-]+', '-', FIXED.name)
)
INFRA_ERROR_PATTERNS = (
    'newuidmap: write to uid_map failed', 'invalid internal status',
    'failed to clean repository', 'bridge failed',
    'container process terminated', 'runtime did not start',
    '<local-data>/coding_agent/swe-agent/.swe-runtime',
)
SUCCESS_EXIT_STATUSES = {'submitted', 'submitted (exit_cost)'}


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec='seconds')


def read_json(path: Path):
    return json.loads(path.read_text())


def api_config() -> tuple[str, str]:
    env_key = os.environ.get('OPENAI_API_KEY', '').strip()
    env_base = os.environ.get('OPENAI_BASE_URL', '').strip()
    if env_key or env_base:
        if not env_key or not env_base:
            raise RuntimeError('OPENAI_API_KEY and OPENAI_BASE_URL must be set together')
        return env_key, env_base
    text = API_CONFIG.read_text()
    key = re.search(r'api_key\s*=\s*["\']([^"\']+)["\']', text)
    base = re.search(r'base_url\s*=\s*["\']([^"\']+)["\']', text)
    if not key or not base:
        raise RuntimeError(f'Invalid API config: {API_CONFIG}')
    return key.group(1), base.group(1)


def full_target_ids() -> list[str]:
    return [x['instance_id'] for x in read_json(DATASET)]


def target_ids() -> list[str]:
    override = os.environ.get('FIXED_LOCAL_IDS', '').strip()
    if override:
        ids = [x.strip() for x in override.split(',') if x.strip()]
        unknown = set(ids) - set(full_target_ids())
        if not ids or unknown:
            raise RuntimeError(f'Invalid FIXED_LOCAL_IDS: empty={not ids}, unknown={sorted(unknown)}')
        return ids
    return full_target_ids()


def records() -> dict[str, dict]:
    return {x['instance_id']: x for x in read_json(DATASET)}


def source_repo(iid: str) -> Path:
    matches = list(BASE_WORKTREES.glob(f'full-shard*/{iid}'))
    if len(matches) != 1 or not (matches[0] / '.git').exists():
        raise RuntimeError(f'Expected one source repo for {iid}, got {matches}')
    return matches[0]


def repo_overrides() -> dict[str, Path]:
    value = os.environ.get('SWE_REPO_OVERRIDES', '').strip()
    if not value:
        return {}
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise RuntimeError('SWE_REPO_OVERRIDES must be valid JSON') from exc
    if not isinstance(parsed, dict):
        raise RuntimeError('SWE_REPO_OVERRIDES must be an object')
    return {str(key): Path(path).resolve() for key, path in parsed.items()}


def attempt_dir(run: int, iid: str, attempt: int) -> Path:
    return FIXED / f'run_{run}' / 'cases' / iid / f'attempt_{attempt:02d}'


def sandbox_dir(run: int, iid: str, attempt: int) -> Path:
    """Return a short, unique path for the live repo and SWE-ReX runtime.

    SWE-ReX's local terminal uses a shell prompt in command output.  Very long
    cwd values can wrap that prompt into the response, corrupting commands
    such as ``cd <cwd>``.  Keep only the live paths short; retain all logs and
    metadata in the descriptive artifact tree above.
    """
    index = full_target_ids().index(iid)
    return SANDBOX_ROOT / f'r{run}' / f'c{index:02d}' / f'a{attempt:02d}'


def valid_attempt(path: Path, iid: str) -> bool:
    agent = path / 'agent'
    return len(list(agent.rglob('*.traj'))) == 1 and len(list(agent.rglob('*.pred'))) == 1 and (path / 'validation.json').exists()


def latest_valid(run: int, iid: str) -> Path | None:
    root = FIXED / f'run_{run}' / 'cases' / iid
    if not root.exists():
        return None
    for p in sorted(root.glob('attempt_*'), reverse=True):
        if valid_attempt(p, iid):
            try:
                if read_json(p / 'validation.json').get('valid') is True:
                    validation = read_json(p / 'validation.json')
                    if validation.get('execution_mode') == EXECUTION_MODE:
                        return p
            except Exception:
                pass
    return None


def write_case_file(path: Path, iid: str, repo: Path, runtime: Path, record: dict) -> None:
    # The server uses host Python 3.11 from a read-only mount.  The bash session
    # immediately restores TASK_PATH, so agent commands use the image's native
    # testbed Python and dependencies.
    server_path = f'{SWEREX_ENV}/bin:{TASK_PATH}'
    container_label = re.sub(r'[^a-zA-Z0-9_.-]+', '-', str(runtime.relative_to(SANDBOX_ROOT)))
    path.write_text(json.dumps([{
        'env': {
            'deployment': {
                'type': 'docker', 'image': official_image(iid),
                'docker_args': [
                    '--volume', f'{repo}:/testbed:rw',
                    '--volume', f'{runtime}:{runtime}:rw',
                    '--volume', f'{SWEREX_ENV}:{SWEREX_ENV}:ro',
                    '--env', f'PATH={server_path}',
                    '--label', f'evifuzz.attempt={container_label}',
                ],
                'container_runtime': 'podman', 'pull': 'never',
                'remove_container': True, 'python_standalone_dir': None,
                'startup_timeout': 180,
            },
            # prepare_repo already establishes the exact clean synthetic base.
            # reset=False is essential: its origin is a host path intentionally
            # not visible inside the isolated container, so `git fetch` cannot
            # and should not run here.
            'repo': {'type': 'preexisting', 'repo_name': 'testbed',
                     'base_commit': 'HEAD', 'reset': False},
            'post_startup_commands': [
                f'export SWE_RUNTIME_ROOT={runtime} EVIFUZZ_SESSION_PERSISTENCE=confirmed',
                f'bash {runtime}/container_healthcheck.sh',
            ],
            'post_startup_command_timeout': 120,
        },
        'problem_statement': {'type': 'text', 'id': iid, 'text': record['problem_statement']},
    }], ensure_ascii=False, indent=2) + '\n')


def container_label(runtime: Path) -> str:
    return re.sub(r'[^a-zA-Z0-9_.-]+', '-', str(runtime.relative_to(SANDBOX_ROOT)))


def labeled_containers(runtime: Path) -> list[str]:
    env = os.environ.copy(); env['DOCKER_HOST'] = f'unix://{PODMAN_SOCKET}'
    result = subprocess.check_output(
        ['podman', 'ps', '-aq', '--filter', f'label=evifuzz.attempt={container_label(runtime)}'],
        env=env, text=True,
    )
    return [line for line in result.splitlines() if line]


def prepare_repo(dst: Path, iid: str, dataset_base_commit: str) -> tuple[str, str, str]:
    """Extract the official image repo locally, retaining its real Git history."""
    override = repo_overrides().get(iid)
    if override is not None:
        if not override.is_dir() or not (override / '.git').exists():
            raise RuntimeError(f'mutation repository is not a git worktree: {override}')
        source_head = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], cwd=override, text=True,
        ).strip()
        if source_head != dataset_base_commit:
            raise RuntimeError(
                f'mutation repository head mismatch: {source_head} != {dataset_base_commit}'
            )
        mutation_patch = subprocess.check_output(
            ['git', 'diff', '--binary', '--'], cwd=override,
        )
        strategy = os.environ.get('RIPPLE_ENHANCEMENT_STRATEGY', '')
        if not mutation_patch.strip() and strategy != 'remove_docs':
            raise RuntimeError(f'mutation repository has no tracked diff: {override}')
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(override, dst, symlinks=True)
        hook = os.environ.get('EVIFUZZ_MUTATION_HOOK', '')
        if hook:
            subprocess.run(
                [sys.executable, hook, str(dst), iid, '1', str(dst.parent), 'sweagent'],
                env=os.environ.copy(), check=True, timeout=900,
            )
        subprocess.run(['git', 'add', '-A'], cwd=dst, check=True)
        commit_env = os.environ.copy()
        commit_env.update({
            'GIT_AUTHOR_NAME': 'RIPPLE Mutation',
            'GIT_AUTHOR_EMAIL': 'ripple@localhost',
            'GIT_COMMITTER_NAME': 'RIPPLE Mutation',
            'GIT_COMMITTER_EMAIL': 'ripple@localhost',
        })
        subprocess.run(
            ['git', 'commit', '-q', '-m', 'RIPPLE private mutation baseline'],
            cwd=dst, env=commit_env, check=True,
        )
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=dst, text=True).strip()
        if subprocess.check_output(['git', 'status', '--porcelain'], cwd=dst, text=True).strip():
            raise RuntimeError(f'private mutation baseline is dirty: {dst}')
        (dst.parent / 'mutation_baseline.json').write_text(json.dumps({
            'source': str(override),
            'dataset_base_commit': dataset_base_commit,
            'mutation_baseline_commit': head,
            'mutation_patch_bytes': len(mutation_patch),
        }, ensure_ascii=False, indent=2) + '\n')
        return head, dataset_base_commit, 'RIPPLE private mutation baseline'
    dst.parent.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy(); env['DOCKER_HOST'] = f'unix://{PODMAN_SOCKET}'
    image = official_image(iid)
    container_id = subprocess.check_output(
        ['podman', 'create', '--network=none', image, 'true'], env=env, text=True,
    ).strip()
    try:
        subprocess.run(
            ['podman', 'cp', f'{container_id}:/testbed/.', str(dst)],
            env=env, check=True, timeout=600, stdout=subprocess.DEVNULL,
        )
    finally:
        subprocess.run(
            ['podman', 'rm', '-f', container_id], env=env, timeout=60,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    image_head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=dst, text=True).strip()
    image_subject = subprocess.check_output(['git', 'log', '-1', '--format=%s'], cwd=dst, text=True).strip()
    # Official instance images may intentionally ship with tracked-file
    # compatibility edits in the working tree (for example dependency pins in
    # Sphinx setup.py/tox.ini).  SWE-Agent's official reset discards those
    # edits before checking out the task base.  Mirror that order exactly;
    # otherwise checkout can carry the image modifications into the local
    # patch carrier and every preflight attempt is rejected as dirty.
    subprocess.run(['git', 'restore', '.'], cwd=dst, check=True, timeout=120)
    subprocess.run(
        ['git', 'reset', '--hard', 'HEAD'], cwd=dst, check=True, timeout=120,
        stdout=subprocess.DEVNULL,
    )
    subprocess.run(
        ['git', 'cat-file', '-e', f'{dataset_base_commit}^{{commit}}'],
        cwd=dst, check=True, timeout=120,
    )
    subprocess.run(
        ['git', 'checkout', '--detach', '-q', dataset_base_commit],
        cwd=dst, check=True, timeout=120,
    )
    # Match SWE-Agent's official Docker reset semantics exactly.  Do NOT use
    # -x here: official instance images intentionally contain ignored build
    # products (compiled extensions, generated files, etc.) required by their
    # prebuilt test environment.  Removing them makes the bind-mounted local
    # repo observably weaker than the image's native /testbed.
    subprocess.run(['git', 'clean', '-fd'], cwd=dst, check=True, timeout=120, stdout=subprocess.DEVNULL)
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=dst, text=True).strip()
    if head != dataset_base_commit:
        raise RuntimeError(f'official image base mismatch: {head} != {dataset_base_commit}')
    status = subprocess.check_output(['git', 'status', '--porcelain'], cwd=dst, text=True)
    if status.strip():
        raise RuntimeError(f'extracted official repo is dirty: {dst}: {status}')
    return head, image_head, image_subject


def prepare_runtime(runtime: Path) -> None:
    """Create a case-private shell home without host prompt side effects.

    The cluster-wide /etc/bashrc installs a PROMPT_COMMAND that prints an OSC
    terminal-title sequence ending in BEL.  SWE-ReX's pexpect protocol treats
    that asynchronous prompt output as command output.  A private HOME plus a
    minimal .bashrc makes local execution match the clean shell used in the
    official containers.
    """
    runtime.mkdir(parents=True, exist_ok=True)
    (runtime / '.bashrc').write_text(
        "unset PROMPT_COMMAND\n"
        "export PS1='SHELLPS1PREFIX'\n"
        "export PS2=''\n"
        "export PS0=''\n"
        "export PAGER=cat\n"
        "export GIT_PAGER=cat\n"
        f"export PATH={TASK_PATH}\n"
    )


def official_image(iid: str) -> str:
    normalized = iid.lower().replace('__', '_1776_')
    return f'docker.io/swebench/sweb.eval.x86_64.{normalized}:latest'


def ensure_official_image(iid: str, retries: int = 5) -> None:
    image = official_image(iid)
    env = os.environ.copy(); env['DOCKER_HOST'] = f'unix://{PODMAN_SOCKET}'
    if subprocess.run(['podman', 'image', 'exists', image], env=env).returncode == 0:
        return
    last: subprocess.CalledProcessError | None = None
    for _ in range(retries):
        try:
            subprocess.run(
                ['podman', '--storage-opt', 'ignore_chown_errors=true', 'pull', image],
                env=env, check=True, timeout=3600,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            if subprocess.run(['podman', 'image', 'exists', image], env=env).returncode == 0:
                return
        except subprocess.CalledProcessError as exc:
            last = exc
            time.sleep(10)
    raise RuntimeError(f'official instance image is not cached and pull failed: {image}') from last


def prepare_container_healthcheck(runtime: Path, repo: Path, iid: str, expected_head: str) -> None:
    """Install a pre-model health check executed in the actual agent container."""
    image = official_image(iid)
    ensure_official_image(iid)
    (runtime / 'host_tmp_sentinel').write_text('must-not-be-visible-in-container-tmp\n')
    script = f'''#!/usr/bin/env bash
set -euo pipefail
test "$EVIFUZZ_SESSION_PERSISTENCE" = confirmed
test "$SWE_RUNTIME_ROOT" = {runtime}
test "$(pwd -P)" = /testbed
test "$(git rev-parse HEAD)" = {shlex.quote(expected_head)}
test -z "$(git status --porcelain)"
test "$(command -v python)" = /opt/miniconda3/envs/testbed/bin/python
python -c 'import sys; assert sys.executable == "/opt/miniconda3/envs/testbed/bin/python"; print(sys.version)'
test ! -e /tmp/host_tmp_sentinel
# The read-only SWE-ReX environment and this case-private runtime are mounted
# below <local-data>, so their parent directories legitimately exist.  Verify
# that unrelated host repositories and clean-run artifacts are not exposed.
test ! -e <local-data>/coding_agent/Real_inconsistency_mining
test ! -e <local-data>/coding_agent/EviFuzz/original_passed_cases
test ! -e /cases
marker=.evifuzz_mount_write_test
printf container-write > "$marker"
test "$(cat "$marker")" = container-write
rm "$marker"
printf '%s\n' \
  'valid=true' \
  'image={image}' \
  'repo=/testbed' \
  'head={expected_head}' \
  "python=$(command -v python)" \
  "python_version=$(python --version 2>&1)" \
  'shell_state_persistent=true' \
  'tmp_container_private=true' \
  'host_workspace_hidden=true' \
  > {runtime}/container_health.env
'''
    entry = runtime / 'container_healthcheck.sh'; entry.write_text(script); entry.chmod(0o755)


def direct_container_preflight(runtime: Path, repo: Path, iid: str, expected_head: str) -> None:
    """Prove mounts and both Python environments work before spending tokens."""
    image = official_image(iid)
    ensure_official_image(iid)
    env = os.environ.copy(); env['DOCKER_HOST'] = f'unix://{PODMAN_SOCKET}'
    cmd = [
        'podman', 'run', '--rm', '--network=none',
        '--volume', f'{repo}:/testbed:rw',
        '--volume', f'{SWEREX_ENV}:{SWEREX_ENV}:ro', image, '/bin/bash', '-lc',
        f'cd /testbed && test "$(git rev-parse HEAD)" = {shlex.quote(expected_head)} '
        f'&& test -z "$(git status --porcelain)" '
        f'&& test "$(/opt/miniconda3/envs/testbed/bin/python --version 2>&1)" != "" '
        f'&& {SWEREX_ENV}/bin/python -c "import swerex"',
    ]
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=120)
    (runtime / 'direct_preflight.log').write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f'direct official-container preflight exit={result.returncode}')


def extract_metrics(agent: Path, trajectory: Path) -> dict:
    trace_logs = list(agent.rglob('*.trace.log'))
    totals = None
    pattern = re.compile(
        r'total_tokens_sent=([\d,]+), total_tokens_received=([\d,]+), '
        r'total_cost=([\d.]+), total_api_calls=(\d+)'
    )
    if len(trace_logs) == 1:
        for match in pattern.finditer(trace_logs[0].read_text(errors='replace')):
            totals = match
    traj = read_json(trajectory)
    metrics = {
        'trajectory_steps': len(traj.get('trajectory', [])),
        'history_messages': len(traj.get('history', [])),
        'exit_status': traj.get('info', {}).get('exit_status'),
    }
    if totals:
        metrics.update({
            'input_tokens': int(totals.group(1).replace(',', '')),
            'output_tokens': int(totals.group(2).replace(',', '')),
            'reported_cost': float(totals.group(3)),
            'api_calls': int(totals.group(4)),
        })
    return metrics


def validate_submission_artifacts(agent: Path, trajectory: Path, prediction: Path) -> dict:
    """Reject structurally present outputs that do not contain a real submission."""
    traj = read_json(trajectory)
    pred = read_json(prediction)
    info = traj.get('info') or {}
    exit_status = info.get('exit_status')
    submission = info.get('submission') or ''
    model_patch = pred.get('model_patch') or ''
    api_calls = (info.get('model_stats') or {}).get('api_calls', 0)
    try:
        api_calls = int(api_calls)
    except (TypeError, ValueError):
        api_calls = 0
    errors = []
    if exit_status not in SUCCESS_EXIT_STATUSES:
        errors.append(f'unsuccessful trajectory exit_status={exit_status!r}')
    if not submission.strip():
        errors.append('trajectory submission is empty')
    if not model_patch.strip():
        errors.append('prediction model_patch is empty')
    if submission.strip() != model_patch.strip():
        errors.append('trajectory submission and prediction model_patch differ')
    if api_calls <= 0:
        errors.append(f'non-positive trajectory api_calls={api_calls}')
    batch_status = agent / 'run_batch_exit_statuses.yaml'
    if not batch_status.exists():
        errors.append('run_batch_exit_statuses.yaml is missing')
    else:
        status_text = batch_status.read_text(errors='replace').lower()
        if 'exit_error' in status_text:
            errors.append('batch exit status contains exit_error')
    if errors:
        raise RuntimeError('; '.join(errors))
    return {
        'exit_status': exit_status,
        'api_calls': api_calls,
        'submission_bytes': len(submission.encode()),
        'prediction_patch_bytes': len(model_patch.encode()),
    }


def run_case(run: int, worker: int, iid: str, record: dict, key: str, base_url: str,
             attempt_numbers: list[int] | None = None) -> dict:
    root = FIXED / f'run_{run}' / 'cases' / iid
    root.mkdir(parents=True, exist_ok=True)
    if attempt_numbers is None:
        attempt_numbers = list(range(1, MAX_ATTEMPTS + 1))
    for attempt in attempt_numbers:
        if latest_valid(run, iid):
            return {'instance_id': iid, 'status': 'already_complete'}
        out = attempt_dir(run, iid, attempt)
        if out.exists():
            continue
        out.mkdir(parents=True)
        sandbox = sandbox_dir(run, iid, attempt)
        repo = sandbox / 'repo'
        runtime = sandbox / 'runtime'
        agent = out / 'agent'
        agent.mkdir()
        # A retry can reuse the same deterministic sandbox path even though its
        # visible artifact directory is new.  Remove only this case/attempt's
        # private sandbox so stale repo/runtime files cannot poison copytree or
        # the SWE-ReX health check.
        if sandbox.exists():
            shutil.rmtree(sandbox)
        sandbox.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        started = time.time()
        status = 'ok'
        error = ''
        try:
            prepare_runtime(runtime)
            env.update({
                'OPENAI_API_KEY': key,
                # LiteLLM otherwise rejects SWE-Agent's default top_p before
                # sending any request to GPT-5.4-mini-ca.
                'LITELLM_DROP_PARAMS': 'true',
                'SWE_RUNTIME_ROOT': str(runtime),
                'TERM': 'dumb',
                'PROMPT_COMMAND': '',
                'PAGER': 'cat',
                'GIT_PAGER': 'cat',
                'DOCKER_HOST': f'unix://{PODMAN_SOCKET}',
            })
            ensure_official_image(iid)
            head, image_repo_head, image_repo_subject = prepare_repo(repo, iid, record['base_commit'])
            ignored_artifact_count = len(subprocess.check_output(
                ['git', 'ls-files', '--others', '--ignored', '--exclude-standard'],
                cwd=repo, text=True,
            ).splitlines())
            prepare_container_healthcheck(runtime, repo, iid, head)
            direct_container_preflight(runtime, repo, iid, head)
            write_case_file(out / 'case.json', iid, repo, runtime, record)
            config_path = SWE_ROOT / 'config/default.yaml'
            system_prompt = os.environ.get('EVIFUZZ_SYSTEM_PROMPT', '').strip()
            if system_prompt:
                import yaml
                config = yaml.safe_load(config_path.read_text())
                original = config['agent']['templates']['system_template']
                config['agent']['templates']['system_template'] = original.rstrip() + '\n\n' + system_prompt
                config_path = runtime / 'enhancement_sweagent.yaml'
                config_path.write_text(yaml.safe_dump(config, sort_keys=False, allow_unicode=True))
            sweagent_cmd = [
                '<local-data>/anaconda3/bin/conda', 'run', '--no-capture-output', '-n', 'swe-agent', 'sweagent', 'run-batch',
                '--config', str(config_path), f'--agent.model.name={MODEL}',
                f'--agent.model.api_base={base_url}', '--agent.model.api_key=$OPENAI_API_KEY',
                '--agent.model.per_instance_cost_limit=0', '--agent.model.total_cost_limit=0',
                f'--agent.model.per_instance_call_limit={CALL_LIMIT}', '--agent.model.max_input_tokens=0',
                '--agent.model.max_output_tokens=4096', '--instances.type=expert_file',
                f'--instances.path={out / "case.json"}', '--num_workers=1', '--progress_bar=False',
                f'--output_dir={agent}',
            ]
            cmd = sweagent_cmd
            with (out / 'run.log').open('w') as log:
                proc = subprocess.Popen(cmd, cwd=SWE_ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                try:
                    rc = proc.wait(timeout=CASE_TIMEOUT)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, 15)
                    try: proc.wait(timeout=30)
                    except subprocess.TimeoutExpired: os.killpg(proc.pid, 9); proc.wait(timeout=30)
                    raise RuntimeError(f'case timeout after {CASE_TIMEOUT}s')
            if rc != 0:
                raise RuntimeError(f'run-batch exit={rc}')
            for _ in range(120):
                if not labeled_containers(runtime):
                    break
                time.sleep(0.5)
            else:
                stale = labeled_containers(runtime)
                for container_id in stale:
                    subprocess.run(
                        ['podman', 'rm', '-f', container_id], env=env,
                        timeout=60, stdout=subprocess.DEVNULL,
                    )
                if labeled_containers(runtime):
                    raise RuntimeError(f'container cleanup failed: {labeled_containers(runtime)}')
            trajs = list(agent.rglob('*.traj')); preds = list(agent.rglob('*.pred'))
            if len(trajs) != 1 or len(preds) != 1:
                raise RuntimeError(f'expected one trajectory and prediction, got traj={len(trajs)} pred={len(preds)}')
            blob = trajs[0].read_text(errors='replace')
            run_blob = (out / 'run.log').read_text(errors='replace')
            bad_signatures = [p for p in INFRA_ERROR_PATTERNS if p in (blob + '\n' + run_blob).lower()]
            if bad_signatures:
                raise RuntimeError(f'infrastructure signatures in artifacts: {bad_signatures}')
            submission_validation = validate_submission_artifacts(agent, trajs[0], preds[0])
            health = runtime / 'container_health.env'
            if not health.exists() or 'valid=true' not in health.read_text():
                raise RuntimeError('actual trajectory container health check is missing or invalid')
            if subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip() != head:
                raise RuntimeError('host patch carrier HEAD changed unexpectedly')
            metrics = extract_metrics(agent, trajs[0])
            (out / 'metrics.json').write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + '\n')
            validation = {'valid': True, 'instance_id': iid, 'worker': worker, 'run': run, 'attempt': attempt,
                          'execution_mode': EXECUTION_MODE,
                          'official_test_image': official_image(iid),
                          'container_runtime': 'podman',
                          'container_lifetime': 'one_long_lived_container_per_trajectory',
                          'host_swerex_env_read_only': str(SWEREX_ENV),
                          'task_python': '/opt/miniconda3/envs/testbed/bin/python',
                          'max_output_tokens': 4096,
                          'repo': str(repo), 'runtime': str(runtime), 'artifact_dir': str(out),
                          'repo_head': head, 'dataset_base_commit': record['base_commit'],
                          'official_image_initial_repo_head': image_repo_head,
                          'official_image_initial_repo_subject': image_repo_subject,
                          'real_git_history_preserved': True,
                          'official_ignored_artifact_count_preserved': ignored_artifact_count,
                          'initial_repo_clean': True,
                          'direct_preflight': str(runtime / 'direct_preflight.log'),
                          'actual_container_health': str(health),
                          'container_cleanup_confirmed': True,
                          'submission_validation': submission_validation,
                          'trajectory': str(trajs[0]), 'prediction': str(preds[0]),
                          'metrics': str(out / 'metrics.json'),
                          'elapsed_seconds': round(time.time() - started, 2)}
            (out / 'validation.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2) + '\n')
            return {'instance_id': iid, 'status': 'ok', 'attempt': attempt}
        except Exception as exc:
            status = 'infrastructure_error'; error = f'{type(exc).__name__}: {exc}'
            (out / 'validation.json').write_text(json.dumps({'valid': False, 'instance_id': iid, 'run': run, 'attempt': attempt,
                'error': error, 'elapsed_seconds': round(time.time() - started, 2)}, ensure_ascii=False, indent=2) + '\n')
        (root / 'last_error.txt').write_text(error + '\n')
    return {'instance_id': iid, 'status': 'failed_after_attempts'}


def rescue_case(run: int, iid: str, record: dict, key: str, base_url: str, worker: int = 0) -> dict:
    root = FIXED / f'run_{run}' / 'cases' / iid
    existing = sorted(
        int(p.name.split('_')[1]) for p in root.glob('attempt_*')
        if p.name.startswith('attempt_') and p.name.split('_')[1].isdigit()
    )
    start = (max(existing) if existing else 0) + 1
    attempts = list(range(start, start + RESCUE_ATTEMPTS))
    return run_case(run, worker, iid, record, key, base_url, attempt_numbers=attempts)


def worker(run: int, worker_id: int) -> int:
    ids = target_ids()[worker_id - 1::N_WORKERS]
    recs = records(); key, base_url = api_config()
    log = FIXED / 'logs' / f'run_{run}_worker_{worker_id}.jsonl'; log.parent.mkdir(parents=True, exist_ok=True)
    failures = 0
    with log.open('a') as handle:
        progress = FIXED / 'LIVE_PROGRESS.md'
        for index, iid in enumerate(ids, 1):
            if os.environ.get('AUTHORITATIVE_MONITOR') != '1':
                progress.write_text(
                '# 官方容器本地推理实时进度\n\n'
                f'- 更新时间：`{now()}`\n- run：`{run}`\n- worker：`{worker_id}`\n'
                f'- 当前 case：`{iid}`\n- worker 内进度：`{index - 1}/{len(ids)}`\n'
            )
            result = run_case(run, worker_id, iid, recs[iid], key, base_url)
            handle.write(json.dumps({'time': now(), **result}, ensure_ascii=False) + '\n'); handle.flush()
            failures += result['status'] not in ('ok', 'already_complete')
            if os.environ.get('AUTHORITATIVE_MONITOR') != '1':
                progress.write_text(
                '# 官方容器本地推理实时进度\n\n'
                f'- 更新时间：`{now()}`\n- run：`{run}`\n- worker：`{worker_id}`\n'
                f'- 最近 case：`{iid}`（`{result["status"]}`）\n- worker 内进度：`{index}/{len(ids)}`\n'
            )
    return 1 if failures else 0


def collect_predictions(run: int) -> Path:
    rows = []
    for iid in target_ids():
        p = latest_valid(run, iid)
        if not p:
            raise RuntimeError(f'missing valid case {iid}')
        pred = read_json(next(p.joinpath('agent').rglob('*.pred')))
        rows.append({'model_name_or_path': f'evifuzz-{MODEL_TAG}-{EXPERIMENT_TAG}-run{run}', 'instance_id': iid,
                     'model_patch': pred.get('model_patch', '') or ''})
    out = FIXED / f'run_{run}' / 'predictions.jsonl'; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows))
    return out


def cleanup_evaluation_containers(run_id: str) -> None:
    """Remove stale containers for exactly one evaluation namespace."""
    env = os.environ.copy(); env['DOCKER_HOST'] = f'unix://{PODMAN_SOCKET}'
    subprocess.run(
        ['podman', 'version'], env=env, check=True, timeout=30,
        stdout=subprocess.DEVNULL,
    )
    ids = subprocess.check_output(
        ['podman', 'ps', '-aq', '--filter', f'name={run_id}'],
        env=env, text=True, timeout=30,
    ).split()
    for container_id in ids:
        subprocess.run(
            ['podman', 'rm', '-f', container_id], env=env, check=True,
            timeout=60, stdout=subprocess.DEVNULL,
        )
    remaining = subprocess.check_output(
        ['podman', 'ps', '-aq', '--filter', f'name={run_id}'],
        env=env, text=True, timeout=30,
    ).split()
    if remaining:
        raise RuntimeError(f'stale evaluation containers remain for {run_id}: {remaining}')


def evaluate(run: int) -> None:
    evaluation_predictions = os.environ.get('SWE_EVALUATION_PREDICTIONS')
    pred = Path(evaluation_predictions) if evaluation_predictions else collect_predictions(run)
    if not pred.is_file():
        raise FileNotFoundError(f'evaluation predictions missing: {pred}')
    report = FIXED / f'run_{run}' / 'evaluation_summary'; report.mkdir(parents=True, exist_ok=True)
    run_id = f'evifuzz-{BENCHMARK_LABEL.lower()}-{MODEL_TAG}-{EXPERIMENT_TAG}-run{run}'
    env = os.environ.copy(); env['DOCKER_HOST'] = f'unix://{PODMAN_SOCKET}'
    # A failed/restarted harness can leave containers whose deterministic
    # names collide with the next invocation.  Clean only this run namespace
    # and verify the Docker-compatible endpoint before doing any evaluation.
    cleanup_evaluation_containers(run_id)
    cmd = ['<local-data>/anaconda3/bin/conda', 'run', '--no-capture-output', '-n', 'swebench-eval', 'python', '-m', 'swebench.harness.run_evaluation',
           '--dataset_name', BENCHMARK_DATASET, '--split', 'test', '--predictions_path', str(pred), '--max_workers', str(N_WORKERS),
           '--cache_level', 'instance', '--clean', 'False', '--run_id', run_id, '--report_dir', str(report)]
    try:
        with (FIXED / 'logs' / f'run_{run}_evaluation.log').open('w') as log:
            rc = subprocess.run(cmd, cwd='<local-data>/coding_agent/SWE-bench-eval', env=env, stdout=log, stderr=subprocess.STDOUT).returncode
    finally:
        cleanup_evaluation_containers(run_id)
    if rc != 0: raise RuntimeError(f'evaluation exit={rc}')
    source = Path('<local-data>/coding_agent/SWE-bench-eval') / f'evifuzz-{MODEL_TAG}-{EXPERIMENT_TAG}-run{run}.{run_id}.json'
    if not source.exists(): raise RuntimeError(f'missing summary {source}')
    shutil.copy2(source, report / 'official_summary.json')


def missing_valid_cases(run: int) -> list[str]:
    return [iid for iid in target_ids() if latest_valid(run, iid) is None]


def rescue(run: int) -> int:
    recs = records(); key, base_url = api_config()
    missing = missing_valid_cases(run)
    if not missing:
        return 0
    log = FIXED / 'logs' / f'run_{run}_rescue.jsonl'
    with log.open('a') as handle:
        for iid in missing:
            result = rescue_case(run, iid, recs[iid], key, base_url, worker=0)
            handle.write(json.dumps({'time': now(), **result}, ensure_ascii=False) + '\n'); handle.flush()
    return 0 if not missing_valid_cases(run) else 1


def main() -> int:
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest='cmd', required=True)
    for name in ('worker',):
        p=sub.add_parser(name); p.add_argument('run',type=int); p.add_argument('worker',type=int,choices=tuple(range(1, N_WORKERS + 1)))
    p=sub.add_parser('predictions'); p.add_argument('run',type=int)
    p=sub.add_parser('evaluate'); p.add_argument('run',type=int)
    p=sub.add_parser('rescue'); p.add_argument('run',type=int)
    a=ap.parse_args()
    if a.cmd=='worker': return worker(a.run,a.worker)
    if a.cmd=='predictions': print(collect_predictions(a.run)); return 0
    if a.cmd=='rescue': return rescue(a.run)
    evaluate(a.run); return 0


if __name__ == '__main__': raise SystemExit(main())
