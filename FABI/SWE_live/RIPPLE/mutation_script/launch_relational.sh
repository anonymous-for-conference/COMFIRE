#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_ID="${1:?provide a unique relational run ID}"
OUT="$ROOT/mutation_result/$RUN_ID"
TMUX_SOCKET="$OUT/tmux.sock"
PODMAN_SOCKET="/tmp/ripple-$RUN_ID.sock"
SESSION="ripple-run-$RUN_ID"
MONITOR_SESSION="ripple-monitor-$RUN_ID"
test ! -e "$OUT" || { echo "run output already exists: $OUT" >&2; exit 3; }
test ! -e "$PODMAN_SOCKET" || { echo "podman socket already exists: $PODMAN_SOCKET" >&2; exit 3; }
test "${#PODMAN_SOCKET}" -lt 100 || { echo "podman socket path is too long" >&2; exit 3; }
mkdir -p "$OUT"
/data/zlyuaj/anaconda3/bin/python - "$OUT" "$RUN_ID" "$ROOT" <<'PY'
import csv, datetime, hashlib, json, sys
from pathlib import Path
out, run_id, root = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
source = root.parent / 'original_passed_cases_luna/token_stable_cases.csv'
rows = list(csv.DictReader(source.open()))
stamp = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
config = {
 'task':'SWE-bench Live Lite relational documentation mutation',
 'run_id':run_id, 'started_at':stamp, 'workdir':str(root), 'total':len(rows),
 'counts':{agent:sum(r['agent']==agent for r in rows) for agent in ('SWE_Agent','OpenCode','Codex')},
 'input_csv':str(source), 'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'model':'gpt-5.6-luna', 'api_config':'luna_key.txt (secret omitted)',
 'operators':['R1','R2','R3'], 'clusters_per_case':3,
 'mutation_workers_per_agent':2, 'inference_workers_per_agent':2,
 'evaluation_workers_per_agent':2, 'mutation_attempts':3,
 'model_timeout_seconds':45, 'codex_mutation_timeout_seconds':360,
 'case_timeout_seconds':3600, 'evaluation_timeout_seconds':1800,
 'cache_policy':'run-local validated relational patches only',
 'evaluation':'official SWE-bench Live Lite Docker harness via private copy',
 'output':str(out), 'podman_socket':'/tmp/ripple-'+run_id+'.sock',
 'retry_policy':'7 model attempts; 3 unit and 3 case retries',
}
(out/'RUN_CONFIG.json').write_text(json.dumps(config,indent=2)+'\n')
(out/'RUN_CONFIG.md').write_text('# Relational operator mutation run\n\n'+''.join(f'- {k}: `{v}`\n' for k,v in config.items()))
(out/'RUN_attempt_01.log').touch()
(out/'MONITOR.log').touch()
(out/'LIVE_PROGRESS.md').write_text(f'# RIPPLE full mutation run\n\n- phase: starting\n- started_at: `{stamp}`\n- progress: `0/{len(rows)}`\n- ETA: `unknown`\n')
(out/'status.json').write_text(json.dumps({'updated_at':stamp,'phase':'starting','started_at':stamp,'completed':0,'total':len(rows),'remaining':len(rows),'success':0,'failed':0,'errors':0,'eta':'unknown','pid':None,'log':str(out/'RUN.log'),'output_dir':str(out)},indent=2)+'\n')
PY
CMD="cd '$ROOT/mutation_script' && exec env RIPPLE_CODEX_TIMEOUT=360 RIPPLE_API_TIMEOUT=45 /data/zlyuaj/anaconda3/bin/python -u '$ROOT/mutation_script/full_run.py' --run-root '$OUT' --k 3 --seed 20260929 --operators R1 R2 R3 > '$OUT/RUN_attempt_01.log' 2>&1"
tmux -S "$TMUX_SOCKET" new-session -d -s "$SESSION" "$CMD"
sleep 2
tmux -S "$TMUX_SOCKET" has-session -t "$SESSION"
RUNNER_PID="$(tmux -S "$TMUX_SOCKET" display-message -p -t "$SESSION" '#{pane_pid}')"
test -n "$RUNNER_PID" && kill -0 "$RUNNER_PID"
ln -s RUN_attempt_01.log "$OUT/RUN.log"
MONITOR_CMD="cd '$ROOT/mutation_script' && exec /data/zlyuaj/anaconda3/bin/python '$ROOT/mutation_script/full_monitor.py' --run-root '$OUT' --runner-pid '$RUNNER_PID' >>'$OUT/MONITOR.log' 2>&1"
tmux -S "$TMUX_SOCKET" new-session -d -s "$MONITOR_SESSION" "$MONITOR_CMD"
sleep 2
tmux -S "$TMUX_SOCKET" has-session -t "$MONITOR_SESSION"
MONITOR_PID="$(tmux -S "$TMUX_SOCKET" display-message -p -t "$MONITOR_SESSION" '#{pane_pid}')"
/data/zlyuaj/anaconda3/bin/python - "$OUT" "$RUNNER_PID" "$MONITOR_PID" "$SESSION" "$MONITOR_SESSION" "$TMUX_SOCKET" "$PODMAN_SOCKET" <<'PY'
import json,sys
from pathlib import Path
out=Path(sys.argv[1]); values=dict(zip(('runner_pid','monitor_pid','session','monitor_session','tmux_socket','podman_socket'),sys.argv[2:]))
values['runner_pid']=int(values['runner_pid']); values['monitor_pid']=int(values['monitor_pid'])
values['run_log']=str(out/'RUN.log'); values['attempt_log']=str(out/'RUN_attempt_01.log'); values['monitor_log']=str(out/'MONITOR.log')
(out/'launch.json').write_text(json.dumps(values,indent=2)+'\n')
PY
printf '%s\n' "run=$RUN_ID" "runner_pid=$RUNNER_PID" "monitor_pid=$MONITOR_PID" "tmux_session=$SESSION" "monitor_session=$MONITOR_SESSION" "tmux_socket=$TMUX_SOCKET" "log=$OUT/RUN.log" "progress=$OUT/LIVE_PROGRESS.md"
