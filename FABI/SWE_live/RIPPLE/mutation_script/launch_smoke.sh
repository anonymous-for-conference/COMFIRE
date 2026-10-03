#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_ID="${1:-mutation-smoke-$(date +%Y%m%d_%H%M%S)}"
OUT="$ROOT/mutation_result/$RUN_ID"
SOCKET="$OUT/tmux.sock"
SESSION="ripple-$RUN_ID"
mkdir -p "$OUT"
test ! -e "$SOCKET" || { echo "tmux socket exists: $SOCKET" >&2; exit 3; }
CMD="cd '$ROOT' && exec /data/zlyuaj/anaconda3/bin/python '$ROOT/mutation_script/mutation_pipeline.py' --run-id '$RUN_ID' --output '$ROOT/mutation_result' 2>&1 | tee -a '$OUT/RUN.log'"
tmux -S "$SOCKET" new-session -d -s "$SESSION" "$CMD"
sleep 2
tmux -S "$SOCKET" has-session -t "$SESSION"
PANE_PID="$(tmux -S "$SOCKET" display-message -p -t "$SESSION" '#{pane_pid}')"
/data/zlyuaj/anaconda3/bin/python - <<PY
import json
from pathlib import Path
Path("$OUT/launch.json").write_text(json.dumps({
  "run_id": "$RUN_ID", "started_at": __import__('datetime').datetime.now().astimezone().isoformat(),
  "tmux_socket": "$SOCKET", "tmux_session": "$SESSION", "pane_pid": int("$PANE_PID"),
  "run_log": "$OUT/RUN.log", "progress": "$OUT/LIVE_PROGRESS.md", "status": "$OUT/status.json"
}, indent=2) + "\n")
PY
printf '%s\n' "run=$RUN_ID" "tmux_socket=$SOCKET" "tmux_session=$SESSION" "pane_pid=$PANE_PID" "log=$OUT/RUN.log" "status=$OUT/status.json"
