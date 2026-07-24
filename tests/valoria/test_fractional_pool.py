"""ED-MB-0032 — fractional combat pool (Jordan directive 2026-07-23: "pool must be fractional").
The live path floors the continuous pool to an integer die count before rolling, discarding the
fractional remainder. roll_pool_fractional keeps the pool at full precision: the integer part rolls
real d10s, the fractional remainder contributes its expected net (PER_DIE_NET_EV per full die).
"""
import os
import statistics
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import random  # noqa: E402
import mass_battle.config as C  # noqa: E402
import mass_battle.resolution as R  # noqa: E402


def test_default_gated_off():
    assert C.PC_FRACTIONAL_POOL is False, "fractional pool must default OFF (moves goldens when on)"


def test_per_die_ev_is_tn7_expectation():
    # face rule 1=-1, 2-6=0, 7-9=+1, 10=+2 -> EV = (-1 + 3 + 2)/10 = 0.4
    assert C.PER_DIE_NET_EV == pytest.approx(0.4)


def test_sub_one_pool_is_fractional_ev():
    # a pool below 1 contributes ONLY its fractional EV (no spurious floor to a guaranteed die)
    assert R.roll_pool_fractional(0.5) == pytest.approx(0.5 * C.PER_DIE_NET_EV)
    assert R.roll_pool_fractional(0.0) == pytest.approx(0.0)


def test_fractional_remainder_shifts_the_mean():
    # pool 3.0 vs 3.7 should differ in mean net by ~ 0.7 * PER_DIE_NET_EV (the fractional die's EV)
    random.seed(42)
    m30 = statistics.mean(R.roll_pool_fractional(3.0) for _ in range(4000))
    m37 = statistics.mean(R.roll_pool_fractional(3.7) for _ in range(4000))
    assert (m37 - m30) == pytest.approx(0.7 * C.PER_DIE_NET_EV, abs=0.08)


def test_integer_pool_matches_roll_pool_plus_zero_frac():
    # at an exact integer pool the fractional term is 0, so it reduces to the discrete roll
    random.seed(7)
    a = R.roll_pool_fractional(4.0)
    random.seed(7)
    b = R.roll_pool(4)
    assert a == b


def test_monotone_in_pool():
    # larger fractional pool -> larger expected net (no quantization plateau between integers)
    random.seed(11)
    means = [statistics.mean(R.roll_pool_fractional(p) for _ in range(3000))
             for p in (2.0, 2.25, 2.5, 2.75, 3.0)]
    for i in range(len(means) - 1):
        assert means[i + 1] >= means[i] - 0.05  # non-decreasing within noise
    assert means[-1] > means[0] + 0.2           # and clearly rising across the integer gap
