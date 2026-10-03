#!/usr/bin/env bash
set -euo pipefail

scripts=/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/RIPPLE/mutation_script
run_name="${1:-full_relational6_$(date +%Y%m%d_%H%M%S)}"
documents_per_cluster="${2:-0}"
preserve_documents_per_cluster="${3:-0}"
exec "$scripts/launch_smoke.sh" "$run_name" full relational evaluation "$documents_per_cluster" "$preserve_documents_per_cluster"
