#!/usr/bin/env bash
set -euo pipefail
ROOT=<local-data>/coding_agent/EviFuzz
AGENT=${AGENT:?set AGENT (swe_lite, codex, or opencode)}
KEY=${OPENAI_API_KEY:?set OPENAI_API_KEY}
BASE=${OPENAI_BASE_URL:?set OPENAI_BASE_URL}
if [[ "$AGENT" == swe_lite ]]; then
 OUT=${EVIFUZZ_OUTPUT_NAME:-sweagent_gpt54_mini_run4}; SOCKET=/tmp/evifuzz-swe-lite54-run4-podman.sock
 DATA=$ROOT/original_passed_cases/SWE-Agent/gpt54mini_lite/run4_records.json
 export VERIFIED_OUTPUT=$OUT VERIFIED_SANDBOX=<local-data>/efl_sweagent_lite54_run4 VERIFIED_WORKERS=2
 export SWE_DATA_ROOT=<local-data>/coding_agent_big_files/swe-bench-lite SWE_DATASET_FILE=$DATA SWE_AGENT_MODEL=openai/gpt-5.4-mini SWE_HARNESS_DATASET=SWE-bench/SWE-bench_Lite SWE_BENCHMARK_LABEL=Lite SWE_MODEL_TAG=gpt54mini AUTHORITATIVE_MONITOR=1
 CMD=(python $ROOT/script/verified_local_orchestrator.py 4)
else
 OUT=${AGENT}_gpt54_mini_run4; SOCKET=/tmp/evifuzz-${AGENT}-lite54-run4-podman.sock
 DATA=$ROOT/original_passed_cases/$([[ $AGENT == codex ]] && echo Codex || echo OpenCode)/gpt54mini_lite/run4_records.json
 export EVIFUZZ_OUTPUT_ROOT=$ROOT/$OUT EVIFUZZ_SANDBOX_ROOT=<local-data>/efl_${AGENT}_lite54_run4 EVIFUZZ_RECORDS_FILE=$DATA
 CMD=(python $ROOT/script/cli_lite_runner.py orchestrate $AGENT 4 $SOCKET --workers 2)
fi
export OPENAI_API_KEY=$KEY OPENAI_BASE_URL=$BASE
mkdir -p $ROOT/$OUT; chmod 755 $ROOT/$OUT
cat > $ROOT/$OUT/RUN_CONFIG.md <<EOF
# Clean run 4 configuration
- agent: $AGENT
- run: 4
- started_at: $(date --iso-8601=seconds)
- workers: 2
- evaluation: official SWE-bench harness, max_workers=2, cache_level=instance, clean=False
- api_base: $BASE
- api_key: supplied through environment; not persisted
- output_root: $ROOT/$OUT
EOF
podman system service --time=0 unix://$SOCKET >/dev/null 2>&1 &
SERVICE=$!
trap 'kill $SERVICE 2>/dev/null || true; rm -f $SOCKET' EXIT
for i in $(seq 1 100); do [[ -S $SOCKET ]] && break; sleep .2; done
DOCKER_HOST=unix://$SOCKET "${CMD[@]}" >> $ROOT/$OUT/RUN.log 2>&1
python $ROOT/script/archive_clean_run4.py "$AGENT" >> $ROOT/$OUT/RUN.log 2>&1
