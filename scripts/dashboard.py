"""The curation dashboard: one message, kept up to date in the repository's channel by the kit's `watchdog.sh keep`.

It prints the dashboard's text (Zulip markdown) to stdout:
- progress against the seed list's loci;
- the tiers set so far;
- the rate of rows and the burn of the account's 7-day quota window, each a moving average with exponential decay
  (recent hours count most, older ones fade with a half-life);
- what that leaves before the person's cap (90 % of the weekly window, the curator's priming) and its reset.

Inputs:
- the rows and the seed list in the repository;
- the git log, for the time each row was first committed;
- a quota reading, the kit's `quota.py --json`, on stdin or by `--quota FILE`.

Each run appends its quota reading to a history file outside the repository (`$XDG_STATE_HOME/longevity-loci/
quota-history.jsonl`), from which the burn is averaged. The measurements stay out of git, as the person asked
(2026-11-11): only this script is committed.

    sh <kit>/bin/py.sh <kit>/drivers/claude-code/quota.py --json | uv run python scripts/dashboard.py --quota -
"""

from __future__ import annotations

import csv
import json
import math
import os
import subprocess
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import typer
import yaml

ROOT = Path(__file__).resolve().parent.parent
SEED = ROOT / "docs" / "longevitymap_v2" / "data" / "seed_variants.csv"
CAP = 90.0  # % of the 7-day window: the person, 2026-11-12, "Increase spending expectation to 90% of weekly" (80 before)
HALF_LIFE_H = 3.0  # hours: a row or a quota step this old counts half as much as one now
WINDOW = "7-day"
BAR = 30

app = typer.Typer(add_completion=False)


def history_file() -> Path:
    state = os.environ.get("XDG_STATE_HOME") or str(Path.home() / ".local" / "state")
    return Path(state) / "longevity-loci" / "quota-history.jsonl"


def seed_loci() -> set[int]:
    with SEED.open(encoding="utf-8") as f:
        return {int(r["locus_id"]) for r in csv.DictReader(f) if r["locus_id"]}


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def rows() -> list[dict]:
    """The rows as committed at HEAD: a row the curator is editing in the working tree may not parse yet, and the
    board counts what landed."""
    names = sorted(n for n in git("ls-tree", "--name-only", "HEAD", "rows/").splitlines() if n.endswith(".yaml"))
    return [yaml.safe_load(git("show", f"HEAD:{n}")) for n in names]


def row_times() -> list[float]:
    """When each row file was first committed (epoch seconds), oldest first."""
    out = git("log", "--diff-filter=A", "--format=%ct", "--name-only", "--", "rows/*.yaml")
    times, current = [], None
    for line in out.splitlines():
        if line.isdigit():
            current = float(line)
        elif line.endswith(".yaml") and current is not None:
            times.append(current)
    return sorted(times)


def decay(age_h: float) -> float:
    return 0.5 ** (age_h / HALF_LIFE_H)


def event_rate(times: list[float], now: float) -> float | None:
    """Events per hour, each weighted by its age's decay. The weights' integral over all time is HALF_LIFE_H /
    ln 2, so a steady rate r gives back r. None with no event."""
    if not times:
        return None
    return sum(decay((now - t) / 3600) for t in times) / (HALF_LIFE_H / math.log(2))


def burn_rate(samples: list[tuple[float, float, float]]) -> float | None:
    """Points of the window an hour, from (time, pct, resets_at) samples: each step between two readings of one
    window (the same reset time) weighted by its age's decay. A step across a reset is dropped. None with fewer
    than two readings of one window."""
    now = samples[-1][0] if samples else 0.0
    num = den = 0.0
    for (t0, p0, r0), (t1, p1, r1) in zip(samples, samples[1:]):
        if abs(r1 - r0) > 120 or t1 <= t0:
            continue
        w = decay((now - t1) / 3600)
        num += w * (p1 - p0)
        den += w * (t1 - t0) / 3600
    return num / den if den else None


def bar(done: int, total: int) -> str:
    filled = round(BAR * done / total) if total else 0
    return "█" * filled + "░" * (BAR - filled)


def hours(h: float) -> str:
    return f"{h:.0f} h" if h >= 10 else f"{h:.1f} h"


def render(quota: dict | None, now: float) -> str:
    seed = seed_loci()
    held = rows()
    covered = {r["locus_id"] for r in held} | {i for r in held for i in r.get("also_loci", [])}
    done = len(covered & seed)
    tiers = Counter(r["axes"]["tier"]["value"] for r in held)
    rate = event_rate(row_times(), now)
    lines = [f"**Curation**: {done} of {len(seed)} seed loci ({100 * done / len(seed):.0f} %), {len(held)} rows",
             f"`{bar(done, len(seed))}`",
             "Tiers: " + ", ".join(f"{t} {tiers[t]}" for t in "ABCD" if tiers[t]) if tiers else "Tiers: none yet"]
    lines.append(f"Rate: {rate:.1f} rows/h (moving average, half-life {HALF_LIFE_H:g} h)" if rate is not None
                 else "Rate: unknown, no rows yet")
    window = next((w for w in (quota or {}).get("windows", []) if w["name"] == WINDOW), None)
    if window is None:
        lines.append("Quota: unknown (no reading)")
        return "\n".join(lines) + "\n"
    hist = history_file()
    hist.parent.mkdir(parents=True, exist_ok=True)
    with hist.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"t": now, "pct": window["pct"], "resets_at": window["resets_at"]}) + "\n")
    samples = [(s["t"], s["pct"], s["resets_at"]) for s in map(json.loads, hist.read_text(encoding="utf-8").splitlines())]
    burn = burn_rate(samples[-500:])
    left = CAP - window["pct"]
    to_reset = (window["resets_at"] - now) / 3600
    reset = datetime.fromtimestamp(window["resets_at"], UTC).strftime("%a %H:%M UTC")
    lines.append(f"Weekly quota: {window['pct']:.0f} % used, cap {CAP:.0f} %, resets {reset} (in {hours(to_reset)})")
    if burn is None or burn <= 0:
        lines.append("Burn: unknown yet (needs two readings of this window)")
    else:
        lines.append(f"Burn: {burn:.2f} points/h, whole account (moving average)")
        if left <= 0:
            lines.append("**At the cap: curation waits for the reset.**")
        elif left / burn < to_reset:
            lines.append(f"Cap in about {hours(left / burn)}, then idle {hours(to_reset - left / burn)} until the reset")
        else:
            lines.append("Cap not reached before the reset at this burn")
        if rate:
            per_row = burn / rate
            lines.append(f"Cost: about {per_row:.2f} points of the week per row; "
                         f"{max(0, left) / per_row:.0f} rows fit under the cap")
    stamp = datetime.fromtimestamp(now, UTC).strftime("%Y-%m-%d %H:%M UTC")
    lines.append(f"_updated {stamp}_")
    return "\n".join(lines) + "\n"


@app.command()
def main(quota: str = typer.Option("", help="a quota.py --json reading: a file, or - for stdin; empty for none")) -> None:
    """Print the curation dashboard's text."""
    reading = None
    if quota:
        raw = sys.stdin.read() if quota == "-" else Path(quota).read_text(encoding="utf-8")
        reading = json.loads(raw) if raw.strip() else None
    typer.echo(render(reading, datetime.now(UTC).timestamp()), nl=False)


if __name__ == "__main__":
    app()
