#!/usr/bin/env bash
set -euo pipefail

OUTPUT=${1:-/data/zlyuaj/coding_agent/EviFuzz/RIPPLE/mutation_result/enhancement}
SESSION=${2:-ripple-enhancement-20260916}
TMUX_SOCKET=${RIPPLE_ENHANCEMENT_TMUX_SOCKET:-$SESSION}
INFERENCE_WORKERS=${RIPPLE_ENHANCEMENT_WORKERS:-3}
EVALUATION_WORKERS=${RIPPLE_ENHANCEMENT_EVALUATION_WORKERS:-1}

if [[ -z "${RIPPLE_ENHANCEMENT_API_KEY:-}" ]]; then
  echo "RIPPLE_ENHANCEMENT_API_KEY is required" >&2
  exit 2
fi
if tmux -L "$TMUX_SOCKET" has-session -t "$SESSION" 2>/dev/null; then
  echo "tmux session already exists: $SESSION" >&2
  exit 3
fi
mkdir -p "$OUTPUT"
chmod 755 "$OUTPUT"
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
RUN_LOG="$OUTPUT/RUN.log"
MONITOR_LOG="$OUTPUT/MONITOR.log"
STAMP=$(date +%Y%m%d_%H%M%S)
HISTORY="$OUTPUT/run_history/$STAMP"
mkdir -p "$HISTORY"
for OLD in "$RUN_LOG" "$MONITOR_LOG" "$OUTPUT/status.json" "$OUTPUT/LIVE_PROGRESS.md" \
           "$OUTPUT/RUN_CONFIG_STAGED.json" "$OUTPUT/RUN_CONFIG_STAGED.md" \
           "$OUTPUT/INFERENCE_BLOCKERS.json" "$OUTPUT/EVALUATION_BLOCKERS.json"; do
  if [[ -e "$OLD" ]]; then
    mv "$OLD" "$HISTORY/$(basename "$OLD")"
  fi
done
tmux -L "$TMUX_SOCKET" new-session -d -s "$SESSION" \
  "cd /data/zlyuaj/coding_agent/EviFuzz/RIPPLE && python '$SCRIPT_DIR/staged_experiment.py' --output '$OUTPUT' --inference-workers '$INFERENCE_WORKERS' --evaluation-workers '$EVALUATION_WORKERS' 2>&1 | tee '$RUN_LOG'"
sleep 2
MAIN_PID=$(tmux -L "$TMUX_SOCKET" list-panes -t "$SESSION" -F '#{pane_pid}' | head -1)
tmux -L "$TMUX_SOCKET" new-window -t "$SESSION" -n monitor \
  "python '$SCRIPT_DIR/monitor.py' --output '$OUTPUT' --pid '$MAIN_PID' 2>&1 | tee '$MONITOR_LOG'"
cat > "$OUTPUT/PROCESS.md" <<EOF
# Enhancement processes

- tmux session: \`$SESSION\`
- tmux socket: \`$TMUX_SOCKET\`
- attach command: \`tmux -L $TMUX_SOCKET attach -t $SESSION\`
- main pane PID: \`$MAIN_PID\`
- main log: \`$RUN_LOG\`
- monitor log: \`$MONITOR_LOG\`
- launched at: \`$(date --iso-8601=seconds)\`
EOF
echo "$SESSION $TMUX_SOCKET $MAIN_PID $OUTPUT"
