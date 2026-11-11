#!/bin/sh
# The curation dashboard's refresh: every 10 minutes, a quota reading through the kit, the dashboard's text from
# scripts/dashboard.py, and one message kept up to date by `watchdog.sh keep` (edited in place, never reposted).
# Run as the lead seat's watcher `dashboard` (.blueprints.toml), which hands it the kit's py.sh as its argument;
# it prints nothing on success, so it wakes no one. A failure prints one line, which does reach the lead.
#   sh scripts/dashboard-loop.sh <kit>/bin/py.sh [TO]
set -u
PY="$1"
KIT=$(dirname "$(dirname "$PY")")
TO="${2:-#dashboards>longevity-loci curation}"
ROOT=$(cd "$(dirname "$0")/.." && pwd)
while :; do
  out=$(cd "$ROOT" && sh "$PY" "$KIT/drivers/claude-code/quota.py" --json 2>/dev/null \
        | uv run python scripts/dashboard.py --quota - 2>&1) \
    && printf '%s\n' "$out" | sh "$KIT/bin/watchdog.sh" keep lead curation "$TO" - >/dev/null 2>&1 \
    || echo "dashboard: not refreshed: $(printf '%s' "$out" | tail -1 | cut -c1-200)"
  sleep 600
done
