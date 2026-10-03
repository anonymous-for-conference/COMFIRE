#!/usr/bin/env bash
set -euo pipefail

scripts=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_script
results=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_result
run_name="${1:?usage: resume_run.sh RUN_NAME [ATTEMPT]}"
attempt="${2:-2}"
attempt_tag="$(printf '%02d' "$attempt")"
run_root="$results/$run_name"
# tmux stores -L sockets below /tmp/tmux-UID. Long run names can exceed the
# Unix-domain socket pathname limit and make an otherwise live server vanish.
run_hash="$(printf '%s' "$run_name" | sha256sum | cut -c1-12)"
tmux_socket="ripple-${run_hash}-a${attempt_tag}"
podman_session="podman-$run_name-attempt-$attempt_tag"
pipeline_session="pipeline-$run_name-attempt-$attempt_tag"
monitor_session="monitor-$run_name-attempt-$attempt_tag"
# Unix-domain sockets have a platform pathname limit (typically 108 bytes).
# Keep the runtime socket in /tmp so long run names cannot exceed it.
socket="/tmp/ripple-${run_name}-${attempt_tag}.sock"
exit_code="$run_root/EXIT_CODE_attempt_${attempt_tag}"

test -d "$run_root"
test ! -e "$exit_code"
for session in "$podman_session" "$pipeline_session" "$monitor_session"; do
  if tmux -L "$tmux_socket" has-session -t "$session" 2>/dev/null; then
    echo "duplicate tmux session: $tmux_socket/$session" >&2
    exit 1
  fi
done

cp -n "$run_root/status.json" "$run_root/status_attempt_01.json"
cp -n "$run_root/LIVE_PROGRESS.md" "$run_root/LIVE_PROGRESS_attempt_01.md"
mkdir -p "$run_root/podman_attempt_$attempt_tag" "$(dirname "$socket")"

python - "$run_root/RUN_ATTEMPT_${attempt_tag}_CONFIG.md" "$run_root/RUN_CONFIG.md" "$run_name" "$attempt" "$socket" <<'PY'
import json
import sys
from datetime import datetime
from pathlib import Path

path, original_path, run_name, attempt, socket = sys.argv[1:]
original_text = Path(original_path).read_text()
original = json.loads(original_text.split("```json\n", 1)[1].split("\n```", 1)[0])
config = {
    "run_id": run_name,
    "attempt": int(attempt),
    "started_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "reason": "resume validated mutations and retry only missing or invalid cases",
    "reuse": "validated mutation manifests only",
    "operator_mode": original.get("operator_mode", "local"),
    "enabled_mutation_operators": original.get("enabled_mutation_operators", ["L1", "L2", "L3"]),
    "mutation_workers_per_agent": original.get("mutation_workers_per_agent", 2),
    "mutation_case_attempts": original.get("mutation_case_attempts", 3),
    "relational_cluster_attempts": original.get("relational_cluster_attempts", 5),
    "relational_initial_tool_budget": original.get("relational_initial_tool_budget", 8),
    "relational_max_tool_budget": original.get("relational_max_tool_budget", 24),
    "inference_workers_per_agent": original.get("inference_workers_per_agent", 2),
    "inference_attempts": max(6, int(original.get("inference_attempts", 3))),
    "evaluation_attempts": original.get("evaluation_attempts", 2),
    "excluded_policy": "exclude agent-case pairs with no mutable documentation",
    "podman_socket": socket,
}
Path(path).write_text("# Resume configuration\n\n```json\n" + json.dumps(config, indent=2) + "\n```\n")
PY

cleanup_startup() {
  tmux -L "$tmux_socket" kill-session -t "$podman_session" 2>/dev/null || true
  tmux -L "$tmux_socket" kill-session -t "$monitor_session" 2>/dev/null || true
}
trap cleanup_startup ERR

tmux -L "$tmux_socket" new-session -d -s "$podman_session" \
  "exec python '$scripts/podman_service.py' --socket '$socket' --output '$run_root/podman_attempt_$attempt_tag' --run-root '$run_root' --exit-code '$exit_code'"

ready=0
for _ in $(seq 1 300); do
  if curl --silent --fail --unix-socket "$socket" http://d/_ping >/dev/null 2>&1; then
    ready=1
    break
  fi
  sleep 0.5
done
if [[ "$ready" -ne 1 ]]; then
  echo "Podman API socket did not become ready: $socket" >&2
  cleanup_startup
  exit 1
fi

previous_pid="$(python -c 'import json,sys; print(json.load(open(sys.argv[1])).get("pid", 0))' "$run_root/status.json" 2>/dev/null || echo 0)"
tmux -L "$tmux_socket" new-session -d -s "$pipeline_session" \
  "exec python '$scripts/orchestrate_smoke.py' --run-root '$run_root' --socket '$socket' --attempt '$attempt' >>'$run_root/RUN_attempt_${attempt_tag}.log' 2>&1"

ready=0
for _ in $(seq 1 600); do
  read -r phase status_pid < <(python -c 'import json,sys; s=json.load(open(sys.argv[1])); print(s.get("phase", ""), s.get("pid", 0))' "$run_root/status.json" 2>/dev/null || echo " 0")
  if [[ "$phase" != "failed" && "$phase" != "inconsistent" && "$status_pid" != "$previous_pid" ]] && kill -0 "$status_pid" 2>/dev/null; then
    ready=1
    break
  fi
  sleep 0.1
done
if [[ "$ready" -ne 1 ]]; then
  echo "Pipeline did not publish a live status in time" >&2
  cleanup_startup
  exit 1
fi

tmux -L "$tmux_socket" new-session -d -s "$monitor_session" \
  "python '$scripts/monitor.py' --run-root '$run_root' --attempt '$attempt' 2>&1 | tee '$run_root/MONITOR_attempt_${attempt_tag}.log'"
sleep 2

pane_pid() {
  local session="$1"
  local value
  value="$(tmux -L "$tmux_socket" display-message -p -t "$session:0.0" '#{pane_pid}' 2>/dev/null || true)"
  echo "${value:-0}"
}
pipeline_pid="$(pane_pid "$pipeline_session")"
monitor_pid="$(pane_pid "$monitor_session")"
podman_pid="$(pane_pid "$podman_session")"
python - "$run_root/PROCESS_attempt_${attempt_tag}.json" "$tmux_socket" "$pipeline_session" "$monitor_session" "$podman_session" "$pipeline_pid" "$monitor_pid" "$podman_pid" <<'PY'
import json
import sys
from datetime import datetime
from pathlib import Path

Path(sys.argv[1]).write_text(json.dumps({
    "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "tmux_socket": sys.argv[2],
    "sessions": {"pipeline": sys.argv[3], "monitor": sys.argv[4], "podman": sys.argv[5]},
    "pids": {"pipeline": int(sys.argv[6]), "monitor": int(sys.argv[7]), "podman": int(sys.argv[8])},
}, indent=2) + "\n")
PY

tmux -L "$tmux_socket" has-session -t "$pipeline_session"
tmux -L "$tmux_socket" has-session -t "$monitor_session"
trap - ERR
echo "$run_root"
