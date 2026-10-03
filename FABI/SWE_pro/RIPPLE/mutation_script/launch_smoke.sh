#!/usr/bin/env bash
set -euo pipefail

scripts=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_script
results=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_result
run_name="${1:-smoke_$(date +%Y%m%d_%H%M%S)}"
scope="${2:-smoke}"
operator_mode="${3:-local}"
stop_after="${4:-evaluation}"
documents_per_cluster="${5:-0}"
preserve_documents_per_cluster="${6:-0}"
run_root="$results/$run_name"
# Keep the tmux socket path well below the Unix-domain socket pathname limit.
run_hash="$(printf '%s' "$run_name" | sha256sum | cut -c1-12)"
tmux_socket="ripple-${run_hash}"
podman_session="podman-$run_name"
pipeline_session="pipeline-$run_name"
monitor_session="monitor-$run_name"
# Keep below the Unix-domain socket pathname limit for descriptive run names.
socket="/tmp/ripple-${run_name}.sock"

for session in "$podman_session" "$pipeline_session" "$monitor_session"; do
  if tmux -L "$tmux_socket" has-session -t "$session" 2>/dev/null; then
    echo "duplicate tmux session: $tmux_socket/$session" >&2
    exit 1
  fi
done

prepare_args=(--run-name "$run_name" -k 3 --operator-mode "$operator_mode" --stop-after "$stop_after" --documents-per-cluster "$documents_per_cluster" --preserve-documents-per-cluster "$preserve_documents_per_cluster")
if [[ "$scope" == "full" ]]; then
  prepare_args+=(--all)
elif [[ "$scope" != "smoke" ]]; then
  echo "scope must be smoke or full: $scope" >&2
  exit 2
fi
if [[ "$operator_mode" != "local" && "$operator_mode" != "relational" ]]; then
  echo "operator mode must be local or relational: $operator_mode" >&2
  exit 2
fi
if [[ "$stop_after" != "mutation" && "$stop_after" != "evaluation" ]]; then
  echo "stop-after must be mutation or evaluation: $stop_after" >&2
  exit 2
fi
python "$scripts/prepare_smoke.py" "${prepare_args[@]}"
mkdir -p "$run_root/podman" "$(dirname "$socket")"
cleanup_startup() {
  tmux -L "$tmux_socket" kill-session -t "$podman_session" 2>/dev/null || true
  tmux -L "$tmux_socket" kill-session -t "$monitor_session" 2>/dev/null || true
}
trap cleanup_startup ERR

tmux -L "$tmux_socket" new-session -d -s "$monitor_session" \
  "python '$scripts/monitor.py' --run-root '$run_root' 2>&1 | tee '$run_root/MONITOR.log'"
tmux -L "$tmux_socket" new-session -d -s "$podman_session" \
  "exec python '$scripts/podman_service.py' --socket '$socket' --output '$run_root/podman' --run-root '$run_root'"

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
  python - "$run_root/status.json" "$run_root" <<'PY'
import json
import sys
from datetime import datetime
from pathlib import Path

path = Path(sys.argv[1])
state = json.loads(path.read_text())
state.update({
    "updated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "phase": "failed", "completed": 0, "remaining": state["total"], "success": 0,
    "failed": 0, "errors": 1, "eta": "unknown",
    "error_details": [{"stage": "startup", "error": "Podman API socket did not become ready"}],
})
path.write_text(json.dumps(state, indent=2) + "\n")
PY
  cleanup_startup
  exit 1
fi

tmux -L "$tmux_socket" new-session -d -s "$pipeline_session" \
  "exec python '$scripts/orchestrate_smoke.py' --run-root '$run_root' --socket '$socket' >>'$run_root/RUN.log' 2>&1"
sleep 2

pipeline_pid="$(tmux -L "$tmux_socket" display-message -p -t "$pipeline_session:0.0" '#{pane_pid}')"
monitor_pid="$(tmux -L "$tmux_socket" display-message -p -t "$monitor_session:0.0" '#{pane_pid}')"
podman_pid="$(tmux -L "$tmux_socket" display-message -p -t "$podman_session:0.0" '#{pane_pid}')"
python - "$run_root/PROCESS.json" "$tmux_socket" "$pipeline_session" "$monitor_session" "$podman_session" "$pipeline_pid" "$monitor_pid" "$podman_pid" <<'PY'
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
