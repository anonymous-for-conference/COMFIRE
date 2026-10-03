#!/usr/bin/env bash
set -euo pipefail

scripts=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_script
run_name="${1:-full_$(date +%Y%m%d_%H%M%S)}"
exec "$scripts/launch_smoke.sh" "$run_name" full
