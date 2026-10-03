#!/usr/bin/env bash
set -u
ROOT=<local-data>/coding_agent/EviFuzz/verified_gpt56_luna_4
while pgrep -f 'verified_local_orchestrator.py 4' >/dev/null 2>&1; do
  if [[ -f "$ROOT/PROGRESS.md" ]]; then cp "$ROOT/PROGRESS.md" "$ROOT/LIVE_PROGRESS.md"; fi
  sleep 10
done
[[ -f "$ROOT/PROGRESS.md" ]] && cp "$ROOT/PROGRESS.md" "$ROOT/LIVE_PROGRESS.md"
