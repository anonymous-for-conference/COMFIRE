#!/usr/bin/env bash
set -euo pipefail
ROOT=<local-data>/coding_agent/EviFuzz
AGENT=${AGENT:?set AGENT to swe_lite, codex, or opencode}
KEY=${OPENAI_API_KEY:?set OPENAI_API_KEY}
BASE=${OPENAI_BASE_URL:?set OPENAI_BASE_URL}
RUN=1
if [[ "$AGENT" == swe_lite ]]; then
  OUT=${EVIFUZZ_OUTPUT_NAME:-sweagent_gpt56_luna_clean_run1}; SOCKET=${EVIFUZZ_SOCKET:-/tmp/evifuzz-swe-luna-clean1.sock}
  DATA=<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json
  export VERIFIED_OUTPUT=$OUT VERIFIED_SANDBOX=<local-data>/efl_sweagent_luna_clean1 VERIFIED_WORKERS=2
  export SWE_DATA_ROOT=<local-data>/coding_agent_big_files/swe-bench-lite SWE_DATASET_FILE=$DATA SWE_AGENT_MODEL=openai/gpt-5.6-luna SWE_HARNESS_DATASET=SWE-bench/SWE-bench_Lite SWE_BENCHMARK_LABEL=Lite SWE_MODEL_TAG=gpt56luna AUTHORITATIVE_MONITOR=1
  CMD=(python "$ROOT/script/verified_local_orchestrator.py" "$RUN")
else
  OUT=${EVIFUZZ_OUTPUT_NAME:-${AGENT}_gpt56_luna_clean_run1}; SOCKET=${EVIFUZZ_SOCKET:-/tmp/evifuzz-${AGENT}-luna-clean1.sock}
  DATA=<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json
  export EVIFUZZ_OUTPUT_ROOT=$ROOT/$OUT EVIFUZZ_SANDBOX_ROOT=${EVIFUZZ_SANDBOX_ROOT:-<local-data>/efl_${AGENT}_luna_clean1} EVIFUZZ_RECORDS_FILE=$DATA EVIFUZZ_RUN_ID=${EVIFUZZ_RUN_ID:-${AGENT}-gpt56luna-clean1}
  CMD=(python "$ROOT/script/cli_lite_runner_luna.py" orchestrate "$AGENT" "$RUN" "$SOCKET" --workers 2)
fi
export OPENAI_API_KEY=$KEY OPENAI_BASE_URL=$BASE
mkdir -p "$ROOT/$OUT"; chmod 755 "$ROOT/$OUT"
cat > "$ROOT/$OUT/RUN_CONFIG.md" <<EOF
# GPT-5.6 Luna clean run 1 configuration
- agent: $AGENT
- run: 1
- started_at: $(date --iso-8601=seconds)
- workers: 2
- model: gpt-5.6-luna
- reasoning effort: disabled (no reasoning-effort argument is sent)
- input cases: 300 (complete SWE-bench Lite test split)
- benchmark: SWE-bench Lite, test split
- evaluation: official SWE-bench harness, max_workers=2, cache_level=instance, clean=False
- api_base: $BASE
- api_key: supplied through environment; not persisted
- output_root: $ROOT/$OUT
EOF
podman system service --time=0 "unix://$SOCKET" >"$ROOT/$OUT/podman_service.log" 2>&1 & SERVICE=$!
trap 'kill $SERVICE 2>/dev/null || true; rm -f "$SOCKET"' EXIT
for i in $(seq 1 100); do [[ -S "$SOCKET" ]] && break; sleep .2; done
if [[ ! -S "$SOCKET" ]]; then echo "podman socket did not start" >&2; exit 1; fi
DOCKER_HOST="unix://$SOCKET" "${CMD[@]}" >>"$ROOT/$OUT/RUN.log" 2>&1
