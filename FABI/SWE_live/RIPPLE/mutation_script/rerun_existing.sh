#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}" )/.." && pwd)"
SOURCE="${1:?source failed run directory}"
RUN_ID="${2:-mutation-smoke-rerun-$(date +%Y%m%d_%H%M%S)}"
OUT="$ROOT/mutation_result/$RUN_ID"
SOCKET="/tmp/ripple-$RUN_ID.sock"
SESSION="ripple-$RUN_ID"
mkdir -p "$OUT"
cp -a "$SOURCE/worker_patches" "$OUT/"
cp -a "$SOURCE/patch_index.json" "$OUT/" 2>/dev/null || true
CMD="cd '$ROOT/mutation_script' && exec /data/zlyuaj/anaconda3/bin/python '$ROOT/mutation_script/rerun_harness.py' '$OUT' 2>&1 | tee -a '$OUT/RUN.log'"
tmux -S "$OUT/tmux.sock" new-session -d -s "$SESSION" "$CMD"
sleep 2
tmux -S "$OUT/tmux.sock" has-session -t "$SESSION"
PANE_PID="$(tmux -S "$OUT/tmux.sock" display-message -p -t "$SESSION" '#{pane_pid}')"
/data/zlyuaj/anaconda3/bin/python - <<PY
import json
from pathlib import Path
Path("$OUT/launch.json").write_text(json.dumps({"run_id":"$RUN_ID","source":"$SOURCE","tmux_socket":"$OUT/tmux.sock","tmux_session":"$SESSION","pane_pid":int("$PANE_PID"),"podman_socket":"$SOCKET","run_log":"$OUT/RUN.log"},indent=2)+"\n")
PY
printf '%s\n' "run=$RUN_ID" "tmux_socket=$OUT/tmux.sock" "tmux_session=$SESSION" "pane_pid=$PANE_PID" "podman_socket=$SOCKET"
