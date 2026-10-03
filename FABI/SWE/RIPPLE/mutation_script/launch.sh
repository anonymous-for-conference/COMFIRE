#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 || $# -gt 6 ]]; then
  echo "usage: $0 RUN_ROOT RUN_ID [LEVEL] [K] [INSTANCE_ID] [BASE_REPO]" >&2
  exit 2
fi

run_root=$(realpath -m "$1")
run_id=$2
level=${3:-level_1}
k=${4:-}
instance_id=${5:-astropy__astropy-6938}
script_root=$(cd "$(dirname "$0")" && pwd)
case_root=/data/zlyuaj/coding_agent/EviFuzz/original_passed_cases/Codex/gpt54mini_lite/cases/$instance_id
base_repo=${6:-/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories/astropy}
mkdir -p "$run_root"
if [[ -n "$(find "$run_root" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "run root must be new and empty: $run_root" >&2
  exit 1
fi

started_at=$(date --iso-8601=seconds)
cat > "$run_root/RUN_CONFIG.md" <<EOF
# RUN CONFIG

- task: $instance_id ${level} documentation mutation
- run_id: $run_id
- started_at: $started_at
- working_directory: /data/zlyuaj/coding_agent/EviFuzz
- input: $case_root (base commit c76af9ed6bb89bfba45b9f5bc1e635188278e2fa)
- local_base_repo: $base_repo (read-only source; a private clone is mutated)
- mutation models: selector gpt-5.6-luna medium; local gpt-5.6-terra medium; relational Codex gpt-5.6-luna high
- inference: Codex gpt-5.4-mini medium via existing RIPPLE interface
- workers: 1
- timeout: mutation API 300s; inference case 3600s
- retries: OpenAI transport 2; interface inference max 6 attempts
- cache: official evaluation instance cache; no mutation response cache
- evaluation: RIPPLE/swe-bench-lite_interface.py automatic official harness
- output: $run_root
- secret policy: API key intentionally omitted
- selected_cluster_count: ${k:-all}
EOF
cat > "$run_root/status.json" <<EOF
{
  "updated_at": "$started_at", "phase": "initializing", "started_at": "$started_at",
  "completed": 0, "total": 1, "remaining": 1, "success": 0, "failed": 0,
  "errors": 0, "eta": "unknown", "pid": null, "log": "$run_root/RUN.log",
  "output_dir": "$run_root"
}
EOF
: > "$run_root/RUN.log"
: > "$run_root/MONITOR.log"

tmux_socket="$run_root/tmux.sock"
pipeline_session="ripple-${run_id}-pipeline"
monitor_session="ripple-${run_id}-monitor"
experiment_args=(--output "$run_root" --base-repo "$base_repo" --case-dir "$case_root" --level "$level")
if [[ -n "$k" ]]; then experiment_args+=(--k "$k"); fi
experiment_args_text=$(printf '%q ' "${experiment_args[@]}")
pipeline_command="cd /data/zlyuaj/coding_agent/EviFuzz && python '$script_root/experiment.py' $experiment_args_text 2>&1 | tee -a '$run_root/RUN.log'"
monitor_command="cd /data/zlyuaj/coding_agent/EviFuzz && python '$script_root/monitor.py' '$run_root' >> '$run_root/MONITOR.log' 2>&1"
tmux -S "$tmux_socket" new-session -d -s "$pipeline_session" "$pipeline_command"
pipeline_pid=$(tmux -S "$tmux_socket" list-panes -t "$pipeline_session" -F '#{pane_pid}')
tmux -S "$tmux_socket" new-session -d -s "$monitor_session" "$monitor_command"
monitor_pid=$(tmux -S "$tmux_socket" list-panes -t "$monitor_session" -F '#{pane_pid}')
python - "$run_root" "$pipeline_pid" "$monitor_pid" "$tmux_socket" "$pipeline_session" "$monitor_session" <<'PY'
import json, os, sys
from pathlib import Path
root = Path(sys.argv[1])
status = json.loads((root / "status.json").read_text())
status["pid"] = int(sys.argv[2])
tmp = root / f"status.json.{os.getpid()}.tmp"
tmp.write_text(json.dumps(status, indent=2) + "\n")
tmp.replace(root / "status.json")
(root / "process_registry.json").write_text(json.dumps({
    "pipeline_pid": int(sys.argv[2]), "monitor_pid": int(sys.argv[3]),
    "tmux_socket": sys.argv[4], "pipeline_session": sys.argv[5],
    "monitor_session": sys.argv[6],
}, indent=2) + "\n")
PY
echo "$run_root"
