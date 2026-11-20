"""
engine/tests/test_band_odds.py -- B05.02: `sigma_leverage.band_odds`, the band odds of one roll of THE ONE SAMPLER
(`dice_engine.continuous_engine_sample`: Normal(MU_PER_DIE * pool, SIGMA_PER_DIE * sqrt(pool)), plus the roll's
boost), as its Normal closed form graded on `dice_engine`'s OWN ladder edges (`BAND_FLOORS`, quantised once at
`MARGIN_SCALE`).

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * IT IS THE DEALT DISTRIBUTION, TO A STATED TOLERANCE (an approximation claim, so a tolerance is honest):
    `N_SAMPLED` seeded rolls of the real sampler plus the real boost, graded by the real ladder, agree with
    `band_odds` in every band within `K_SE` standard errors, over a grid of pools (whole, fractional and
    below one die), obstacles (whole and fractional) and boosts (both signs). A wrong mean, a wrong spread,
    a wrong edge or a floor the sampler does not have moves a band by many standard errors.
  * IT READS THE LADDER'S TABLE, NOT A COPY OF IT: when `BAND_FLOORS` is mutated the tuple MOVES, and it
    moves to the closed form written out independently in this file.
  * IT IS A DISTRIBUTION AND IS MONOTONE: P(Partial or better) strictly falls in the obstacle and strictly
    rises in the pool on a 0.25 grid; and, below the `chance_floor` cap the social module solves on it, no
    pool's chance falls under the one-die floor at the largest lawful disadvantage (`-M_MAX`).
  * BELOW ONE DIE THERE IS ONE RULE: the pool is taken as it is for `pool > 0`; the odds are the sampler's.
  * the boost is the mu-shift the roll adds (`roll_net_continuous(pool) + net_boost(...)`), never an Ob change.
"""
from __future__ import annotations

import importlib
import math
import os
import random
from engine.dice_engine import draw
import sys

import pytest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from engine.dice_engine import dice_engine as DE  # noqa: E402
from engine.dice_engine import sigma_leverage as SL  # noqa: E402
from engine.substrate import composition  # noqa: E402

N_SAMPLED = 40_000      # rolls per cell
K_SE = 4.0              # the stated tolerance: four standard errors of the band's own share, in every band


def _phi(z: float) -> float:
    return (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0


def _tail(pool: float, ob: float, boost: float, floor: int, floors=None) -> float:
    """P(round(MARGIN_SCALE * (net - ob)) >= floor), written out here from the sampler's two moments: the
    independent route to `band_odds` (it shares no helper with the owner)."""
    mean = 0.4 * pool + boost
    sd = 0.8 * math.sqrt(pool)
    edge = (floor - 0.5) / 1000.0          # a margin rounds to `floor` milli-units from `floor - 0.5`
    return 1.0 - _phi((ob + edge - mean) / sd)


def _by_hand(pool, ob, boost=0.0, floors=None):
    f = floors or {"partial": 0, "success": 1000, "overwhelming": 3000}
    p, s, o = (_tail(pool, ob, boost, f[k]) for k in ("partial", "success", "overwhelming"))
    return (1.0 - p, p - s, s - o, o)


def _sampled(pool, ob, boost, n=N_SAMPLED, seed=1) -> list:
    """`n` rolls of the one sampler plus the boost, graded by the one ladder: the bands a roll deals."""
    rng = draw.seeded(draw.H2("test_band_odds", seed))
    tally = [0, 0, 0, 0]
    for _ in range(n):
        net = SL.roll_net_continuous(pool, rng=rng) + boost
        tally[DE.DEGREE_ORDINAL[DE.degree_from_net(net, ob)]] += 1
    return tally


def test_closed_form_matches_a_sampled_check():
    """N_SAMPLED seeded rolls per cell, K_SE standard errors, every band of every cell."""
    cells = [(1, 2, 0.0), (1, 0.5, 0.0), (2.6, 2, 0.0), (5, 1, 0.0), (5, 3.5, 0.0), (8, 3, 0.7), (8, 6, 0.0),
             (12, 4.25, 0.0), (12, 6, -1.2 * math.sqrt(12)), (3, 2, SL.net_boost(1.0, 3)), (0.5, 1, 0.0), (0.25, 0.5, 0.0)]
    checked = 0
    for pool, ob, boost in cells:
        odds = SL.band_odds(pool, ob, boost)
        tally = _sampled(pool, ob, boost)
        for band, p in enumerate(odds):
            se = math.sqrt(max(p * (1 - p), 1e-12) / N_SAMPLED)
            assert abs(tally[band] / N_SAMPLED - p) <= K_SE * se + 1e-9, (pool, ob, boost, band, tally[band] / N_SAMPLED, p)
            checked += 1
    assert checked == len(cells) * 4


def test_it_equals_the_closed_form_written_out_independently():
    checked = 0
    for pool in (1, 2.6, 5, 12, 0.5):
        for ob in (0.5, 1, 1.25, 2, 3.5, 6):
            for boost in (-1.0, 0.0, 0.3, 2.5):
                got = SL.band_odds(pool, ob, boost)
                want = _by_hand(pool, ob, boost)
                assert all(math.isclose(g, w, abs_tol=1e-12) for g, w in zip(got, want)), (pool, ob, boost, got, want)
                assert len(got) == 4 and all(0.0 <= p <= 1.0 for p in got), got
                assert math.isclose(sum(got), 1.0, abs_tol=1e-12), (pool, ob, boost, got)
                checked += 1
    assert checked == 5 * 6 * 4


def test_swapping_a_band_edge_moves_the_tuple(monkeypatch):
    """MUTATION: the Partial/Success edge moved in `BAND_FLOORS`, the table `degree_from_net` reads. If
    `band_odds` held its own copy of the ladder the tuple would not move; it reads the owner's table, so it
    does, and to the closed form with that edge. This is the falsifier that the ladder reads the table."""
    base = SL.band_odds(5, 2)
    monkeypatch.setattr(DE, "BAND_FLOORS", {**DE.BAND_FLOORS, "success": 2000})        # was 1000: the edge moved
    moved = SL.band_odds(5, 2)
    assert moved != base
    want = _by_hand(5, 2, 0.0, {"partial": 0, "success": 2000, "overwhelming": 3000})
    assert all(math.isclose(g, w, abs_tol=1e-12) for g, w in zip(moved, want)), (moved, want)


def test_the_boost_shifts_the_roll_and_never_the_obstacle():
    """A boost b at Ob o is a roll whose every net is b higher: a larger boost never lowers the chance of
    clearing, and the tuple at (o, b) is the tuple of mean `MU * pool + b` at Ob `o`."""
    prev = -1.0
    for boost in (-1.0, 0.0, 0.25, 0.5, 1.0, 1.5, 2.0):
        clear = 1.0 - SL.band_odds(2, 2, boost)[0]
        assert clear >= prev - 1e-12, (boost, clear, prev)
        prev = clear
    assert SL.band_odds(2, 2, 1.0)[0] < SL.band_odds(2, 2, 0.0)[0]
    b = SL.net_boost(SL.LEVEL_SIGMA["major"], 4)
    assert b > 1.0 and SL.band_odds(4, 2, b)[0] < SL.band_odds(4, 2)[0]
    assert SL.record_odds(4, 2, SL.LEVEL_SIGMA["major"]) == SL.band_odds(4, 2, b)


def test_below_one_die_there_is_one_rule():
    """DOE row 5: `continuous_engine_sample` and `net_boost` take the pool as it is for `pool > 0` (spread and
    boost both scale with `sqrt(pool)`); nothing floors it to one die, so the odds below one die are the
    sampler's, not a one-die roll's."""
    assert SL.net_boost(1.0, 0.25) == pytest.approx(SL.soft_cap(1.0) * 0.8 * math.sqrt(0.25))
    assert SL.net_boost(1.0, 0.25) != SL.net_boost(1.0, 1)
    assert SL.band_odds(0.25, 1) != SL.band_odds(1, 1)
    mean = sum(SL.roll_net_continuous(0.25, rng=r) for r in [draw.seeded(draw.H2("test_band_odds", 3))] for _ in range(40_000)) / 40_000
    assert abs(mean - 0.4 * 0.25) < 4 * 0.8 * math.sqrt(0.25) / math.sqrt(40_000)       # not the one-die mean 0.4
    # no pool at all: nothing is rolled and the roll is the boost alone (net 0); the ladder grades it as such
    assert SL.roll_net_continuous(0, rng=draw.seeded(draw.H2("test_band_odds", 0))) == 0.0
    assert SL.band_odds(0, 1) == (1.0, 0.0, 0.0, 0.0)
    assert SL.band_odds(0, 0) == (0.0, 1.0, 0.0, 0.0)


def _module():
    """The social contest module, found the way the host finds it (`engine/` never imports module code by name)."""
    target = composition.ROLES["social_contest.roll"]["target"]
    return importlib.import_module(target.split(":", 1)[0])


def _partial_or_better(pool: float, ob: float, boost: float = 0.0) -> float:
    return 1.0 - SL.band_odds(pool, ob, boost)[0]


def test_partial_or_better_is_monotone_and_floored():
    """Gate (3): P(Partial or better) strictly falls in the obstacle and strictly rises in the pool on a 0.25 grid
    (read where neither end has saturated to a float 0 or 1); below the cap the social module solves on the closed
    form, no pool's chance falls under the one-die floor at the largest lawful disadvantage, `-M_MAX`."""
    pools = [1 + 0.25 * i for i in range(0, 45)]                  # 1.0 .. 12.0
    obs = [0.25 * i for i in range(0, 41)]                        # 0.0 .. 10.0
    live = lambda p: 1e-9 < p < 1 - 1e-9
    falling = rising = 0
    for pool in pools:
        for lo, hi in zip(obs, obs[1:]):
            a, b = _partial_or_better(pool, lo), _partial_or_better(pool, hi)
            if live(a) and live(b):
                assert a > b, (pool, lo, hi, a, b)
                falling += 1
    for ob in obs:
        for lo, hi in zip(pools, pools[1:]):
            a, b = _partial_or_better(lo, ob), _partial_or_better(hi, ob)
            if live(a) and live(b):
                assert a < b, (ob, lo, hi, a, b)
                rising += 1
    assert falling >= 800 and rising >= 800, (falling, rising)
    # the floor: the cap is solved against the largest lawful disadvantage, for every pool from one die up
    ceiling = 2.0
    mod = _module()
    floor = _partial_or_better(1, ceiling, SL.net_boost(-SL.M_MAX, 1))
    assert 0.0 < floor < 0.01, floor
    prev_cap = 0.0
    checked = 0
    for pool in pools:
        cap = mod._chance_floor_cap(pool, ceiling)
        assert cap >= prev_cap - 1e-12, (pool, cap, prev_cap)       # a larger pool is never worse for the cap
        prev_cap = cap
        worst = SL.net_boost(-SL.M_MAX, pool)
        assert _partial_or_better(pool, cap, worst) >= floor * (1 - 1e-6), (pool, cap)      # the cap itself holds it
        for ob in (0.25 * i for i in range(0, int(cap / 0.25) + 1)):                         # and so does everything under it
            assert _partial_or_better(pool, ob, worst) >= floor * (1 - 1e-6), (pool, ob, cap)
            checked += 1
        assert _partial_or_better(pool, cap + 0.05, worst) < floor, (pool, cap)             # the cap is where it ends
    assert math.isclose(mod._chance_floor_cap(1, ceiling), ceiling, abs_tol=1e-9)           # at one die the cap is the ceiling
    assert checked >= 400, checked
