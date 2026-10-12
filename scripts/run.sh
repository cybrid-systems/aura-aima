#!/usr/bin/env bash
# Run one Aura file in Soft mode with the repo lib on AURA_PATH.
set -euo pipefail
source "$(dirname "$0")/env.sh"
exec "$AURA_BIN" "$@"
