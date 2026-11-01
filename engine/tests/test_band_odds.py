"""
engine/tests/test_band_odds.py -- CP-T01-03: `sigma_leverage.band_odds`, the exact band odds of one
d10 pool roll, enumerated over `dice_engine`'s OWN face table and graded by `dice_engine`'s OWN ladder.

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * the worked case `band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)` -- hand-derived from the face table
    (-1 / 0 / +1 / +2 at 10 / 50 / 30 / 10 per cent), exact because the arithmetic is integer counts
    over 10**pool.
  * it IS the dealt distribution: 200,000 seeded `roll_pool` rolls settled by `settle_margin` (CP-T01-04:
    the margin's fraction paid by the act's own draw) and graded by `degree_from_net` agree in every band
    within three standard errors. A wrong face table, a wrong pool rounding or a wrong boost shift moves
    a band by many standard errors.
  * it is an enumeration and not a copy: it equals a brute-force walk of every face combination
    (`_die_result` over 10**3) with the fraction rule written out here independently, and when the
    ladder's edges are swapped (a mutant `degree_from_net`) the tuple MOVES -- so the test can observe a
    copy of the ladder, which would not. `test_settle_margin.py` walks the same table through
    `settle_margin` itself.
  * the boost is the mu-shift the roll adds (`roll_net(pool) + net_boost(...)`), never an Ob change.
"""
from __future__ import annotations

import itertools
import math
import os
import random
import sys

import pytest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from engine.dice_engine import dice_engine as DE  # noqa: E402
from engine.dice_engine import sigma_leverage as SL  # noqa: E402


def test_the_worked_case_pool_2_ob_2_is_exact():
    assert SL.band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)


def test_the_four_numbers_are_a_distribution_over_a_sweep():
    checked = 0
    for pool in (1, 2, 3, 5, 8):
        for ob in (0.5, 1, 1.25, 2, 3.5, 6):
            for boost in (0.0, 0.3, 1.0, 2.5):
                odds = SL.band_odds(pool, ob, boost)
                assert len(odds) == 4 and all(0.0 <= p <= 1.0 for p in odds), odds
                assert math.isclose(sum(odds), 1.0, abs_tol=1e-12), (pool, ob, boost, odds)
                checked += 1
    assert checked == 5 * 6 * 4


def test_it_equals_a_brute_force_walk_of_the_face_table():
    """Pool 3 over every one of the 10**3 face combinations, graded by the owner's ladder: an
    independent route to the same tuple (no convolution, no shared helper). The fraction rule is
    written out here, not read from `settle_margin`: the margin's whole part counts for certain and one
    more with probability equal to its fraction (CP-T01-04); a whole margin is graded as it always was."""
    for ob, boost in ((2, 0.0), (1.5, 0.7), (3, 0.0)):
        q = boost - ob
        fraction = q - math.floor(q)
        tally = [0.0, 0.0, 0.0, 0.0]
        for faces in itertools.product(range(1, 11), repeat=3):
            net = sum(DE._die_result(f) for f in faces)
            tally[DE.DEGREE_ORDINAL[DE.degree_from_net(net + math.floor(q), 0)]] += 1 - fraction
            if fraction:
                tally[DE.DEGREE_ORDINAL[DE.degree_from_net(net + math.floor(q) + 1, 0)]] += fraction
        for got, want in zip(SL.band_odds(3, ob, boost), (c / 1000 for c in tally)):
            assert math.isclose(got, want, abs_tol=1e-12), (ob, boost, got, want)
        if fraction == 0:               # a whole margin is the old grading, exactly
            whole = [0, 0, 0, 0]
            for faces in itertools.product(range(1, 11), repeat=3):
                net = sum(DE._die_result(f) for f in faces)
                whole[DE.DEGREE_ORDINAL[DE.degree_from_net(net + boost, ob)]] += 1
            assert SL.band_odds(3, ob, boost) == tuple(c / 1000 for c in whole), (ob, boost)


@pytest.mark.parametrize("pool,ob,boost", [(2, 2, 0.0), (3, 1.5, 0.0), (4, 3, 0.8), (1, 1, 0.0)])
def test_the_200000_roll_arm_agrees_within_three_standard_errors(pool, ob, boost):
    """The dealt distribution, sampled through the real roll (`roll_pool`, the margin settled by the same
    generator's own uniform, `degree_from_net`), seeded."""
    n = 200_000
    rng = random.Random(20261031)
    tally = [0, 0, 0, 0]
    for _ in range(n):
        net = DE.roll_pool(pool, rng=rng).net
        m = SL.settle_margin(net, boost, ob, rng.random)
        tally[DE.DEGREE_ORDINAL[DE.degree_from_net(m, 0)]] += 1
    exact = SL.band_odds(pool, ob, boost)
    seen = 0
    for band, p in enumerate(exact):
        se = math.sqrt(max(p * (1 - p), 1e-12) / n)
        assert abs(tally[band] / n - p) <= 3 * se + 1e-9, (pool, ob, boost, band, tally[band] / n, p)
        seen += 1
    assert seen == 4


def test_swapping_two_band_edges_moves_the_tuple(monkeypatch):
    """MUTATION: a `degree_from_net` whose Partial and Success edges are swapped. If `band_odds` held
    its own copy of the ladder the tuple would not move; it reads the owner, so it does."""
    base = SL.band_odds(2, 2)

    def swapped(net, ob, extension=None, **context):
        margin = net - ob
        if margin < 0:
            return DE.Degree.FAILURE
        if margin < 2:                                   # was 1: the Partial/Success edge moved
            return DE.Degree.PARTIAL
        return DE.Degree.SUCCESS if margin < 3 else DE.Degree.OVERWHELMING

    monkeypatch.setattr(DE, "degree_from_net", swapped)
    assert SL.band_odds(2, 2) != base
    assert SL.band_odds(2, 2) == (0.74, 0.25, 0.01, 0.0)    # net 3 (.06) now reads Partial; net 4 Success


def test_the_boost_shifts_the_roll_and_never_the_obstacle():
    """A boost b at Ob o grades `net + b` against `o`: the tuple at (o, b) is the tuple of a roll whose
    every net is b higher, and a larger boost never lowers the chance of clearing."""
    prev = -1.0
    for boost in (0.0, 0.25, 0.5, 1.0, 1.5, 2.0):
        failure = SL.band_odds(2, 2, boost)[0]
        clear = 1.0 - failure
        assert clear >= prev - 1e-12, (boost, clear, prev)
        prev = clear
    assert SL.band_odds(2, 2, 1.0)[0] < SL.band_odds(2, 2, 0.0)[0]
    # the roll's own composition, `net_boost(level, pool)`, is what a caller passes
    # (at pool 2 the whole boost is 0.989 -- under one success: the whole-dice roll alone paid it nothing,
    #  the gap CP-T01-04's fraction rule closes -- so it now pays in proportion; pool 4 pays as before.)
    b = SL.net_boost(SL.LEVEL_SIGMA["major"], 4)
    assert b > 1.0 and SL.band_odds(4, 2, b)[0] < SL.band_odds(4, 2)[0]
    assert SL.band_odds(2, 2, SL.net_boost(SL.LEVEL_SIGMA["major"], 2))[0] < SL.band_odds(2, 2)[0]


def test_the_pool_is_rounded_and_floored_as_the_roll_does():
    """`roll_net` deals `max(1, int(round(pool)))` whole dice; the odds are for the dice dealt."""
    assert SL.band_odds(0.2, 1) == SL.band_odds(1, 1)
    assert SL.band_odds(0, 1) == SL.band_odds(1, 1)
    assert SL.band_odds(2.6, 2) == SL.band_odds(3, 2)


def test_it_does_not_touch_the_gaussian_path():
    """`p_success` stays the closed form combat reads; `band_odds` is a different, exact quantity."""
    gaussian = SL.p_success(2, 2)
    exact_clear = 1.0 - SL.band_odds(2, 2)[0]
    assert abs(gaussian - exact_clear) > 0.05, (gaussian, exact_clear)
