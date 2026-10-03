#!/usr/bin/env bash
set -euo pipefail

scripts=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_script
results=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_result
run_name="${1:?usage: recover_then_continue.sh RUN_NAME ATTEMPT NEXT_RUN PID...}"
attempt="${2:?missing attempt}"
next_run="${3:?missing next run name}"
shift 3
if [[ "$#" -eq 0 ]]; then
  echo "at least one orphan runner PID is required" >&2
  exit 2
fi

run_root="$results/$run_name"
attempt_tag="$(printf '%02d' "$attempt")"
log="$run_root/RECOVERY_attempt_${attempt_tag}.log"

while true; do
  alive=0
  for pid in "$@"; do
    if kill -0 "$pid" 2>/dev/null; then
      alive=$((alive + 1))
    fi
  done
  if [[ "$alive" -eq 0 ]]; then
    break
  fi
  printf '[%s] waiting for %s orphan inference runner(s)\n' "$(date '+%F %T')" "$alive" >>"$log"
  sleep 30
done

printf '[%s] orphan inference runners complete; resuming pipeline\n' "$(date '+%F %T')" >>"$log"
bash "$scripts/resume_run.sh" "$run_name" "$attempt" >>"$log" 2>&1
exec python "$scripts/continue_after_round.py" \
  --run-root "$run_root" \
  --exit-code "EXIT_CODE_attempt_${attempt_tag}" \
  --next-run "$next_run" \
  --poll-seconds 30 >>"$log" 2>&1
