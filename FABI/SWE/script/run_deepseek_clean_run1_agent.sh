#!/usr/bin/env bash
set -euo pipefail

AGENT=${1:?agent is required}
ROOT=<local-data>/coding_agent/EviFuzz/deepseek_v4_flash_clean_run1
SCRIPT=<local-data>/coding_agent/EviFuzz/script
DATASET=<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json
MODEL=deepseek-v4-flash
BASE_URL=https://rightapi.ai/deepseek/v1
SOCKET="/tmp/evifuzz-deepseek-clean1-$AGENT.sock"

: "${OPENAI_API_KEY:?OPENAI_API_KEY must be inherited through the environment}"
export OPENAI_BASE_URL=$BASE_URL
export EVIFUZZ_STARTED_AT=${EVIFUZZ_STARTED_AT:-$(date --iso-8601=seconds)}

# Each agent owns exactly one Podman API service. The trap prevents a completed
# or failed pipeline from leaving a service or socket that can collide later.
rm -f "$SOCKET"
podman system service --time=0 "unix://$SOCKET" >> "$ROOT/$AGENT/podman_service.log" 2>&1 &
PODMAN_PID=$!
cleanup() {
  kill "$PODMAN_PID" 2>/dev/null || true
  wait "$PODMAN_PID" 2>/dev/null || true
  rm -f "$SOCKET"
}
trap cleanup EXIT INT TERM

for _ in $(seq 1 100); do
  if DOCKER_HOST="unix://$SOCKET" podman version >/dev/null 2>&1; then
    break
  fi
  sleep 0.1
done
DOCKER_HOST="unix://$SOCKET" podman version >/dev/null

if [[ $AGENT == sweagent ]]; then
  export SWE_AGENT_MODEL=deepseek/deepseek-v4-flash
  export SWE_MODEL_TAG=deepseekv4flash
  export SWE_EXPERIMENT_TAG=clean-run1
  export SWE_DATA_ROOT=<local-data>/coding_agent_big_files/swe-bench-lite
  export SWE_DATASET_FILE=$DATASET
  export SWE_HARNESS_DATASET=SWE-bench/SWE-bench_Lite
  export SWE_BENCHMARK_LABEL=Lite
  export VERIFIED_OUTPUT=deepseek_v4_flash_clean_run1/sweagent
  export VERIFIED_SANDBOX=<local-data>/efl_deepseek_clean1_sweagent
  export VERIFIED_WORKERS=2
  export VERIFIED_MAX_ATTEMPTS=3
  export VERIFIED_RESCUE_ATTEMPTS=2
  export SWE_CASE_TIMEOUT=3600
  export VERIFIED_PODMAN_SOCKET=$SOCKET
  export AUTHORITATIVE_MONITOR=1
  python "$SCRIPT/verified_local_orchestrator.py" 1
  exit $?
fi

export EVIFUZZ_MODEL=$MODEL
export EVIFUZZ_REASONING_EFFORT=
export EVIFUZZ_MODEL_PROVIDER=deepseek
export EVIFUZZ_OPENCODE_PROVIDER=openai
export EVIFUZZ_WORKERS=2
export EVIFUZZ_RECORDS_FILE=$DATASET
export EVIFUZZ_MAX_ATTEMPTS=3
export EVIFUZZ_CASE_TIMEOUT=1200
export EVIFUZZ_RUN_ID="deepseek-clean1-$AGENT"
export EVIFUZZ_OUTPUT_ROOT="$ROOT/$AGENT"
export EVIFUZZ_SANDBOX_ROOT="<local-data>/efl_deepseek_clean1_$AGENT"

python "$SCRIPT/cli_lite_runner_luna.py" orchestrate "$AGENT" 1 "$SOCKET" --workers 2
