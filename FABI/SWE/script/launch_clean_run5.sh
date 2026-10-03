#!/usr/bin/env bash
set -euo pipefail
ROOT=<local-data>/coding_agent/EviFuzz
AGENT=${AGENT:?set AGENT to swe_lite, codex, or opencode}
KEY=${OPENAI_API_KEY:?set OPENAI_API_KEY}
BASE=${OPENAI_BASE_URL:?set OPENAI_BASE_URL}
RUN=5
if [[ "$AGENT" == swe_lite ]]; then
  OUT=${EVIFUZZ_OUTPUT_NAME:-sweagent_gpt54_mini_run5}; SOCKET=/tmp/evifuzz-swe-lite54-run5-podman.sock
  DATA=$ROOT/original_passed_cases/SWE-Agent/gpt54mini_lite/run4_records.json
  export VERIFIED_OUTPUT=$OUT VERIFIED_SANDBOX=<local-data>/efl_sweagent_lite54_run5 VERIFIED_WORKERS=2
  export SWE_DATA_ROOT=<local-data>/coding_agent_big_files/swe-bench-lite SWE_DATASET_FILE=$DATA SWE_AGENT_MODEL=openai/gpt-5.4-mini SWE_HARNESS_DATASET=SWE-bench/SWE-bench_Lite SWE_BENCHMARK_LABEL=Lite SWE_MODEL_TAG=gpt54mini AUTHORITATIVE_MONITOR=1
  CMD=(python "$ROOT/script/verified_local_orchestrator.py" "$RUN")
else
  OUT=${AGENT}_gpt54_mini_run5; SOCKET=${EVIFUZZ_SOCKET:-/tmp/evifuzz-${AGENT}-lite54-run5-podman.sock}
  DATA=$ROOT/original_passed_cases/$([[ $AGENT == codex ]] && echo Codex || echo OpenCode)/gpt54mini_lite/run4_records.json
  export EVIFUZZ_OUTPUT_ROOT=$ROOT/$OUT EVIFUZZ_SANDBOX_ROOT=<local-data>/efl_${AGENT}_lite54_run5 EVIFUZZ_RECORDS_FILE=$DATA
  CMD=(python "$ROOT/script/cli_lite_runner.py" orchestrate "$AGENT" "$RUN" "$SOCKET" --workers 2)
fi
export OPENAI_API_KEY=$KEY OPENAI_BASE_URL=$BASE
mkdir -p "$ROOT/$OUT"; chmod 755 "$ROOT/$OUT"
cat > "$ROOT/$OUT/RUN_CONFIG.md" <<EOF
# Clean run 5 configuration
- agent: $AGENT
- run: 5
- started_at: $(date --iso-8601=seconds)
- workers: 2
- model: gpt-5.4-mini, reasoning effort: medium
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
