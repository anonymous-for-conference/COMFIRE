#!/usr/bin/env bash
set -euo pipefail

ROOT=<local-data>/coding_agent/EviFuzz/deepseek_v4_flash_smoke
SCRIPT=<local-data>/coding_agent/EviFuzz/script
DATASET="$ROOT/dataset/first_2_lite.json"
MODEL=deepseek-v4-flash
BASE_URL=https://rightapi.ai/deepseek/v1
IDS=astropy__astropy-12907,astropy__astropy-14182
STARTED_AT=$(date --iso-8601=seconds)

: "${OPENAI_API_KEY:?OPENAI_API_KEY must be supplied through the environment}"
mkdir -p "$ROOT/dataset" "$ROOT/sweagent/logs" "$ROOT/codex" "$ROOT/opencode"
chmod 755 "$ROOT" "$ROOT/dataset" "$ROOT/sweagent" "$ROOT/codex" "$ROOT/opencode"

DATASET_SOURCE=<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json
jq '[.[] | select(.instance_id == "astropy__astropy-12907" or .instance_id == "astropy__astropy-14182")]' \
  "$DATASET_SOURCE" > "$DATASET.tmp"
test "$(jq length "$DATASET.tmp")" -eq 2
mv "$DATASET.tmp" "$DATASET"
chmod 644 "$DATASET"

for agent in sweagent codex opencode; do
  cat > "$ROOT/$agent/RUN_CONFIG.md" <<EOF
# Run Configuration

- task: DeepSeek v4 Flash smoke test
- agent: $agent
- model: $MODEL
- endpoint: $BASE_URL
- reasoning effort: provider default (no explicit reasoning-effort parameter)
- benchmark: SWE-bench Lite test
- cases: $IDS
- inference workers: 2
- automatic evaluation workers: 2
- start time: $STARTED_AT
- raw log: $ROOT/$agent/RUN.log
- progress: $ROOT/$agent/LIVE_PROGRESS.md

The API credential is injected only through the process environment and is not stored here.
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

start_session ds_smoke_sweagent ds_smoke_sweagent \
  "bash -lc \"'$SCRIPT/run_deepseek_smoke_agent.sh' sweagent >> '$ROOT/sweagent/RUN.log' 2>&1\""
start_session ds_smoke_codex ds_smoke_codex \
  "bash -lc \"'$SCRIPT/run_deepseek_smoke_agent.sh' codex >> '$ROOT/codex/RUN.log' 2>&1\""
start_session ds_smoke_opencode ds_smoke_opencode \
  "bash -lc \"'$SCRIPT/run_deepseek_smoke_agent.sh' opencode >> '$ROOT/opencode/RUN.log' 2>&1\""

start_session ds_smoke_monitor ds_smoke_monitor \
  "bash -lc \"DEEPSEEK_SMOKE_ROOT='$ROOT' DEEPSEEK_SMOKE_STARTED_AT='$STARTED_AT' python '$SCRIPT/deepseek_smoke_monitor.py' >> '$ROOT/MONITOR.log' 2>&1\""

echo "Started DeepSeek smoke sessions at $STARTED_AT"
