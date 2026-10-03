#!/usr/bin/env bash
set -euo pipefail

ROOT=<local-data>/coding_agent/EviFuzz
OUT="$ROOT/codex_opencode_gpt54_mini_pipeline"
mkdir -p "$OUT"
chmod 755 "$OUT"
exec python "$ROOT/script/cli_lite_pipeline.py" run >> "$OUT/RUN.log" 2>&1
