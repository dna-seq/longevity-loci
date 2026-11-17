"""Draw the README's two figures from the repository itself.

Tiers are read from rows/*.yaml; the curation pace from the git history (the day each row file was added).
Run from the repository root:

    uv run --no-project --with matplotlib --with pyyaml python -I scripts/readme_figures.py

Writes docs/figures/tiers.png and docs/figures/curation_pace.png.
"""

import subprocess
from collections import Counter
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import yaml  # noqa: E402

ROOT = Path.cwd()
OUT = ROOT / "docs" / "figures"
TIER_LABELS = {
    "A": "A\ngenome-wide,\nreplicated",
    "B": "B\ngenome-wide,\none shortfall",
    "C": "C\nsuggestive",
    "D": "D\ncontradicted",
}
TIER_COLOURS = {"A": "#2e7d32", "B": "#7cb342", "C": "#f9a825", "D": "#c62828"}


def tiers() -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in sorted((ROOT / "rows").glob("*.yaml")):
        row = yaml.safe_load(path.read_text())
        counts[row["axes"]["tier"]["value"]] += 1
    return counts


def rows_added_per_day() -> list[tuple[date, int]]:
    log = subprocess.run(
        ["git", "log", "--reverse", "--diff-filter=A", "--format=@%ad", "--date=short", "--name-only",
         "--", "rows/*.yaml"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout
    per_day: Counter[date] = Counter()
    day: date | None = None
    for line in log.splitlines():
        if line.startswith("@"):
            day = date.fromisoformat(line[1:])
        elif line.endswith(".yaml") and day is not None:
            per_day[day] += 1
    return sorted(per_day.items())


def draw_tiers(counts: Counter[str]) -> None:
    total = sum(counts.values())
    keys = sorted(TIER_LABELS)
    fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
    bars = ax.bar([TIER_LABELS[k] for k in keys], [counts[k] for k in keys],
                  color=[TIER_COLOURS[k] for k in keys])
    for bar, k in zip(bars, keys):
        ax.annotate(f"{counts[k]} ({counts[k] / total:.0%})",
                    (bar.get_x() + bar.get_width() / 2, counts[k]),
                    textcoords="offset points", xytext=(0, 4), ha="center", fontsize=9)
    ax.set_title(f"Only {counts['A']} of {total} loci reach tier A; most fall short on replication")
    ax.set_ylabel("locus rows (count)")
    ax.set_ylim(0, max(counts.values()) * 1.15)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "tiers.png")


def draw_pace(per_day: list[tuple[date, int]]) -> None:
    labels = [d.strftime("%d %b") for d, _ in per_day]
    added = [n for _, n in per_day]
    total = [sum(added[: i + 1]) for i in range(len(added))]
    fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
    ax.bar(labels, added, color="#9db8d9", label="rows added that day")
    ax.plot(labels, total, color="#1f4e79", marker="o", lw=2, label="rows in total")
    for label, t in zip(labels, total):
        ax.annotate(str(t), (label, t), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8)
    ax.set_title(f"All {total[-1]} locus rows curated in {len(per_day)} days")
    ax.set_ylabel("curated rows (count)")
    ax.set_xlabel(f"day ({per_day[0][0].year})")
    ax.set_ylim(0, total[-1] * 1.13)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.82), frameon=False, fontsize=8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "curation_pace.png")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    draw_tiers(tiers())
    draw_pace(rows_added_per_day())


if __name__ == "__main__":
    main()
