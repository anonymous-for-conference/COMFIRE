#!/usr/bin/env bash
set -euo pipefail

ROOT=<local-data>/coding_agent/EviFuzz/deepseek_v4_flash_clean_run1
SCRIPT=<local-data>/coding_agent/EviFuzz/script
DATASET=<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json
MODEL=deepseek-v4-flash
BASE_URL=https://rightapi.ai/deepseek/v1
STARTED_AT=$(date --iso-8601=seconds)

: "${OPENAI_API_KEY:?OPENAI_API_KEY must be supplied through the environment}"
test "$(jq length "$DATASET")" -eq 300
if [[ -e $ROOT ]]; then
  echo "Refusing to overwrite existing output root: $ROOT" >&2
  exit 1
fi

mkdir -p "$ROOT" "$ROOT/sweagent/logs" "$ROOT/codex" "$ROOT/opencode"
chmod 755 "$ROOT" "$ROOT/sweagent" "$ROOT/codex" "$ROOT/opencode"

for agent in sweagent codex opencode; do
  touch "$ROOT/$agent/RUN.log" "$ROOT/$agent/podman_service.log"
  chmod 644 "$ROOT/$agent/RUN.log" "$ROOT/$agent/podman_service.log"
  cat > "$ROOT/$agent/RUN_CONFIG.md" <<EOF
# DeepSeek v4 Flash clean run 1

- agent: $agent
- model: $MODEL
- endpoint: $BASE_URL
- reasoning effort: disabled (no reasoning-effort parameter is sent)
- benchmark: SWE-bench Lite test split
- input: $DATASET
- cases: 300 (complete test split)
- inference workers: 2
- inference attempts: at most 3 per case
- automatic evaluation: official SWE-bench harness
- evaluation workers: 2
- evaluation cache: instance
- evaluation clean: false
- start time: $STARTED_AT
- raw log: $ROOT/$agent/RUN.log
- progress: $ROOT/$agent/LIVE_PROGRESS.md
- status: $ROOT/$agent/status.json

The API credential is inherited through the process environment and is not stored here.
EOF
  chmod 644 "$ROOT/$agent/RUN_CONFIG.md"
done

start_session() {
  local socket=$1 session=$2 command=$3
  if tmux -L "$socket" has-session -t "$session" 2>/dev/null; then
    echo "Refusing duplicate session $socket/$session" >&2
    return 1
  fi
  tmux -L "$socket" new-session -d -s "$session" "$command"
}

start_session ds_clean1_sweagent ds_clean1_sweagent \
  "bash -lc \"'$SCRIPT/run_deepseek_clean_run1_agent.sh' sweagent >> '$ROOT/sweagent/RUN.log' 2>&1\""
start_session ds_clean1_codex ds_clean1_codex \
  "bash -lc \"'$SCRIPT/run_deepseek_clean_run1_agent.sh' codex >> '$ROOT/codex/RUN.log' 2>&1\""
start_session ds_clean1_opencode ds_clean1_opencode \
  "bash -lc \"'$SCRIPT/run_deepseek_clean_run1_agent.sh' opencode >> '$ROOT/opencode/RUN.log' 2>&1\""

start_session ds_clean1_monitor ds_clean1_monitor \
  "bash -lc \"DEEPSEEK_CLEAN_ROOT='$ROOT' DEEPSEEK_CLEAN_STARTED_AT='$STARTED_AT' python '$SCRIPT/deepseek_clean_run1_monitor.py' >> '$ROOT/MONITOR.log' 2>&1\""

echo "Started DeepSeek clean run 1 at $STARTED_AT"
