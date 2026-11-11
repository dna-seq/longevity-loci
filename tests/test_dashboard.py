"""The dashboard's moving averages (scripts/dashboard.py): a steady rate comes back as itself, recent events weigh
more than old ones, and a quota step across a window's reset is not read as burn."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location("dashboard", Path(__file__).resolve().parent.parent / "scripts" / "dashboard.py")
dashboard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dashboard)


def test_a_steady_rate_comes_back() -> None:
    now = 1_000_000.0
    times = [now - i * 900 for i in range(2000)]  # one every 15 minutes, a long way back
    assert dashboard.event_rate(times, now) == pytest.approx(4.0, rel=0.06)


def test_recent_rows_weigh_more() -> None:
    now = 1_000_000.0
    recent = [now - i * 600 for i in range(6)]
    old = [now - 12 * 3600 - i * 600 for i in range(6)]
    assert dashboard.event_rate(recent, now) > 8 * dashboard.event_rate(old, now)
    assert dashboard.event_rate([], now) is None


def test_burn_skips_a_reset_and_needs_two_readings() -> None:
    h = 3600.0
    r1, r2 = 10 * h, 200 * h
    samples = [(0, 40.0, r1), (h, 42.0, r1), (2 * h, 44.0, r1), (3 * h, 1.0, r2), (4 * h, 3.0, r2)]
    assert dashboard.burn_rate(samples) == pytest.approx(2.0)  # every step +2/h; the drop at the reset is not read
    assert dashboard.burn_rate(samples[:1]) is None
    assert dashboard.burn_rate([(0, 40.0, r1), (h, 1.0, r2)]) is None


def test_bar_is_proportional() -> None:
    assert dashboard.bar(0, 161).count("█") == 0
    assert dashboard.bar(161, 161).count("█") == dashboard.BAR
    assert dashboard.bar(17, 161).count("█") == round(dashboard.BAR * 17 / 161)
