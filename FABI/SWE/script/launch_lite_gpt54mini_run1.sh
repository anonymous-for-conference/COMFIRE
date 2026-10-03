#!/usr/bin/env bash
set -euo pipefail

ROOT=<local-data>/coding_agent/EviFuzz
RUN="${LITE_RUN:-1}"
if [[ "$RUN" == "1" ]]; then
    OUTPUT_NAME=lite_gpt54_mini
else
    OUTPUT_NAME="lite_gpt54_mini_${RUN}"
fi
OUT="$ROOT/$OUTPUT_NAME"
LOG="$OUT/RUN.log"
SOCKET="/tmp/evifuzz-lite-gpt54mini-run${RUN}-podman.sock"
STARTED_AT="$(date --iso-8601=seconds)"

mkdir -p "$OUT/logs" "$OUT/run_${RUN}"
chmod 755 "$OUT" "$OUT/logs" "$OUT/run_${RUN}"

export VERIFIED_OUTPUT="$OUTPUT_NAME"
export VERIFIED_SANDBOX="<local-data>/efl_lite_gpt54mini_run${RUN}"
export VERIFIED_WORKERS=4
export VERIFIED_MAX_ATTEMPTS=3
export VERIFIED_RESCUE_ATTEMPTS=3
export VERIFIED_PODMAN_SOCKET="$SOCKET"
export FIXED_LOCAL_CALL_LIMIT=100
export SWE_DATA_ROOT=<local-data>/coding_agent_big_files/swe-bench-lite
export SWE_DATASET_FILE=<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json
export SWE_AGENT_MODEL=openai/gpt-5.4-mini
export SWE_HARNESS_DATASET=SWE-bench/SWE-bench_Lite
export SWE_BENCHMARK_LABEL=Lite
export SWE_MODEL_TAG=gpt54mini
export AUTHORITATIVE_MONITOR=1

exec python "$ROOT/script/verified_local_orchestrator.py" "$RUN" >> "$LOG" 2>&1
