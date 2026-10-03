#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_ID="${1:?provide an existing relational run ID}"
LABEL="${2:?provide a new attempt label, e.g. attempt_02}"
ATTEMPT_N=$((10#${LABEL##*_}))
SEED=$((20260929 + (ATTEMPT_N > 4 ? ATTEMPT_N - 4 : 0) * 8))
OUT="$ROOT/mutation_result/$RUN_ID"
SOCKET="$OUT/t${LABEL##*_}.sock"
SESSION="ripple-run-$RUN_ID-$LABEL"
MONITOR_SESSION="ripple-monitor-$RUN_ID-$LABEL"
test -f "$OUT/RUN_CONFIG.md"
test ! -e "$OUT/ATTEMPT_$LABEL.json"
test ! -e "$SOCKET"
/data/zlyuaj/anaconda3/bin/python - "$OUT" "$LABEL" "$SEED" <<'PY'
import datetime, hashlib, json, os, sys
from pathlib import Path
root, label, seed = Path(sys.argv[1]), sys.argv[2], int(sys.argv[3])
number = int(label.rsplit('_', 1)[1])
previous_label = f'attempt_{number - 1:02d}'
previous_path = root/f'ATTEMPT_{previous_label}.json'
prior = json.loads(previous_path.read_text() if previous_path.exists() else (root/'launch.json').read_text())
try:
    os.kill(prior['runner_pid'], 0)
except ProcessLookupError:
    pass
else:
    raise RuntimeError(f"previous runner still alive: {prior['runner_pid']}")
cached_cases = []
for case in root.glob('patches/*/*'):
    meta_path = case/'mutation.json'
    if meta_path.is_file():
        meta = json.loads(meta_path.read_text())
        patch = case/'mutation.patch'
        if not patch.is_file() or hashlib.sha256(patch.read_bytes()).hexdigest() != meta['sha256']:
            raise RuntimeError(f"cached mutation failed checksum: {case}")
        cached_cases.append([case.parent.name, case.name])
        continue
    diagnostics = case/f'diagnostics_{previous_label}'
    diagnostics.mkdir(exist_ok=True)
    logs = case/'agent_logs'
    if logs.exists():
        logs.rename(diagnostics/'agent_logs')
    for error in case.glob('mutation_attempt_*.error.json'):
        error.rename(diagnostics/error.name)
stamp = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
record = {'run_id':root.name,'attempt':label,'started_at':stamp,'cache_hit':len(cached_cases),
          'cached_cases':sorted(cached_cases),'seed':seed,
          'reason':os.environ.get('RIPPLE_RETRY_REASON', 'Retry verified mutation patches after case failures'),
          'operators':['R1','R2','R3'],'runner_pid':None}
(root/f'ATTEMPT_{label}.json').write_text(json.dumps(record,indent=2)+'\n')
history = root/'RETRY_HISTORY.md'
old = history.read_text() if history.exists() else '# Relational run retry history\n'
history.write_text(old+f'\n- {stamp}: {label} starts after stopping {previous_label}; cached verified patches={len(cached_cases)}. See incident record for the repair. Attempt log: RUN_{label}.log.\n')
print(f'cached_verified_patches={len(cached_cases)}')
PY
touch "$OUT/RUN_$LABEL.log" "$OUT/MONITOR_$LABEL.log"
ln -sfn "RUN_$LABEL.log" "$OUT/RUN.log"
CMD="cd '$ROOT/mutation_script' && exec env RIPPLE_ATTEMPT_LABEL='$LABEL' RIPPLE_CODEX_TIMEOUT=360 RIPPLE_API_TIMEOUT=45 /data/zlyuaj/anaconda3/bin/python -u '$ROOT/mutation_script/full_run.py' --run-root '$OUT' --k 3 --seed '$SEED' --operators R1 R2 R3 > '$OUT/RUN_$LABEL.log' 2>&1"
tmux -S "$SOCKET" new-session -d -s "$SESSION" "$CMD"
sleep 2
tmux -S "$SOCKET" has-session -t "$SESSION"
RUNNER_PID="$(tmux -S "$SOCKET" display-message -p -t "$SESSION" '#{pane_pid}')"
test -n "$RUNNER_PID" && kill -0 "$RUNNER_PID"
MONITOR_CMD="cd '$ROOT/mutation_script' && exec /data/zlyuaj/anaconda3/bin/python '$ROOT/mutation_script/full_monitor.py' --run-root '$OUT' --runner-pid '$RUNNER_PID' --attempt-label '$LABEL' >>'$OUT/MONITOR_$LABEL.log' 2>&1"
tmux -S "$SOCKET" new-session -d -s "$MONITOR_SESSION" "$MONITOR_CMD"
sleep 2
tmux -S "$SOCKET" has-session -t "$MONITOR_SESSION"
MONITOR_PID="$(tmux -S "$SOCKET" display-message -p -t "$MONITOR_SESSION" '#{pane_pid}')"
/data/zlyuaj/anaconda3/bin/python - "$OUT" "$LABEL" "$RUNNER_PID" "$MONITOR_PID" "$SESSION" "$MONITOR_SESSION" "$SOCKET" <<'PY'
import json,sys
from pathlib import Path
root,label,runner,monitor,session,monitor_session,socket=sys.argv[1:]
root=Path(root); path=root/f'ATTEMPT_{label}.json'; record=json.loads(path.read_text())
record.update(runner_pid=int(runner),monitor_pid=int(monitor),session=session,
              monitor_session=monitor_session,tmux_socket=socket,log=str(root/f'RUN_{label}.log'))
path.write_text(json.dumps(record,indent=2)+'\n')
PY
printf '%s\n' "run=$RUN_ID" "attempt=$LABEL" "runner_pid=$RUNNER_PID" "monitor_pid=$MONITOR_PID" "tmux_session=$SESSION" "monitor_session=$MONITOR_SESSION" "tmux_socket=$SOCKET" "log=$OUT/RUN_$LABEL.log" "progress=$OUT/LIVE_PROGRESS.md"
