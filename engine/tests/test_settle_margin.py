"""
engine/tests/test_settle_margin.py -- CP-T01-04: `sigma_leverage.settle_margin`, the fraction of a
margin settled by the act's own draw, and `band_odds` enumerating that SAME rule.

THE RULE UNDER TEST: the roll's net is an integer (`roll_net`) plus the mu-shift `boost`; the obstacle
may be fractional. With `q = boost - ob`, the settled margin is
    m = raw_net + floor(q) + [u < frac(q)]
an integer, and the ladder reads `degree_from_net(m, 0)`. The extra uniform `u` is drawn ONLY when
`frac(q) > 0`, so every whole-Ob roll (the whole realm) keeps its stream.

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * expected margin is preserved exactly: over pools 1-8, Ob 1 to 4 in quarter steps, boost 0 to 3,
    the mean settled margin is `0.4*pool + boost - ob` to 1e-12 -- a rule that rounds, floors or
    ceilings the fraction misses it by the fraction.
  * P(Partial or better) is strictly increasing in boost and strictly decreasing in Ob wherever it lies
    in (0, 1) -- a cell flat across a fraction step is the integer collapse this rule exists to end.
  * the identity on a whole q: no uniform is drawn and the margin is `raw_net + q`.
  * `band_odds` is the same rule enumerated, not a second copy: it equals a brute-force walk of the face
    table graded through `settle_margin` itself, and agrees with 200,000 seeded draws of the real
    path (`roll_pool` then `settle_margin` with the generator's own uniform).
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


def _no_draw():
    raise AssertionError("a uniform was drawn for a whole margin")


def _expected_margin(pool: int, boost: float, ob: float) -> float:
    """E[settled margin | pool, boost, ob] over the exact net distribution, using ONLY `settle_margin`:
    for a fractional q the two outcomes are read at u = 1.0 (never below the fraction) and u = 0.0
    (always below it), weighted by `1 - f` and `f`."""
    q = boost - ob
    f = q - math.floor(q)
    total = 10 ** pool
    mean = 0.0
    for net, n in SL._net_counts(pool):
        if f == 0.0:
            m = SL.settle_margin(net, boost, ob, _no_draw)
            mean += m * n / total
        else:
            lo = SL.settle_margin(net, boost, ob, lambda: 1.0)
            hi = SL.settle_margin(net, boost, ob, lambda: 0.0)
            assert hi == lo + 1, (net, boost, ob, lo, hi)
            mean += (lo * (1 - f) + hi * f) * n / total
    return mean


OBS = [1 + 0.25 * i for i in range(13)]          # 1 to 4 in quarter steps
BOOSTS = [0.25 * i for i in range(13)]           # 0 to 3


def test_mean_settled_margin_is_the_unrounded_margin():
    checked = 0
    for pool in range(1, 9):
        for ob in OBS:
            for boost in BOOSTS:
                got = _expected_margin(pool, boost, ob)
                want = 0.4 * pool + boost - ob
                assert abs(got - want) < 1e-12, (pool, ob, boost, got, want)
                checked += 1
    assert checked == 8 * 13 * 13


def test_partial_or_better_is_strictly_monotonic_in_boost_and_in_ob():
    steps = 0
    for pool in range(1, 9):
        for ob in OBS:
            row = [1.0 - SL.band_odds(pool, ob, b)[0] for b in BOOSTS]
            for a, b in zip(row, row[1:]):
                if 0.0 < a < 1.0 and 0.0 < b < 1.0:
                    assert b > a, ("boost", pool, ob, a, b)
                    steps += 1
        for boost in BOOSTS:
            col = [1.0 - SL.band_odds(pool, o, boost)[0] for o in OBS]
            for a, b in zip(col, col[1:]):
                if 0.0 < a < 1.0 and 0.0 < b < 1.0:
                    assert b < a, ("ob", pool, boost, a, b)
                    steps += 1
    assert steps > 500, steps       # the loop asserted: most cells are interior


def test_a_whole_margin_draws_nothing_and_is_the_identity():
    for net in (-1, 0, 1, 2, 5):
        for ob in (1, 2, 3.0):
            assert SL.settle_margin(net, 0.0, ob, _no_draw) == net - int(ob)
            assert isinstance(SL.settle_margin(net, 0.0, ob, _no_draw), int)
    # a whole boost against a whole Ob is whole too
    assert SL.settle_margin(2, 1.0, 2.0, _no_draw) == 1


def test_a_fractional_margin_draws_exactly_one_uniform_and_pays_its_fraction():
    q = 0.0 - 1.5                                     # floor -2, fraction 0.5
    drawn = []

    def u(value):
        def draw():
            drawn.append(value)
            return value
        return draw

    assert SL.settle_margin(3, 0.0, 1.5, u(0.49)) == 3 - 2 + 1       # u < fraction: the extra success
    assert SL.settle_margin(3, 0.0, 1.5, u(0.50)) == 3 - 2           # u == fraction: not below it
    assert SL.settle_margin(3, 0.0, 1.5, u(0.99)) == 3 - 2
    assert drawn == [0.49, 0.50, 0.99]                               # one draw per call
    assert math.floor(q) == -2


def test_band_odds_at_the_homes_worked_cases():
    """Pool 2, no advantage: Ob 1.5 reads between Ob 1 and Ob 2; the figures are hand-enumerated."""
    for got, want in zip(SL.band_odds(2, 1.5), (0.58, 0.255, 0.16, 0.005)):
        assert math.isclose(got, want, abs_tol=1e-12), (got, want)
    assert SL.band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0)             # a whole Ob is unchanged, exactly
    assert SL.band_odds(2, 1) == (0.42, 0.32, 0.25, 0.01)


def test_band_odds_equals_a_brute_force_walk_through_settle_margin():
    """Pool 3, every one of the 10**3 face combinations, each graded by `settle_margin` at the two
    extreme uniforms and weighted by the fraction: an independent route to the same tuple."""
    for ob, boost in ((1.5, 0.0), (2.25, 0.7), (3, 0.0), (2, 0.5)):
        q = boost - ob
        f = q - math.floor(q)
        tally = [0.0, 0.0, 0.0, 0.0]
        for faces in itertools.product(range(1, 11), repeat=3):
            net = sum(DE._die_result(face) for face in faces)
            if f == 0.0:
                outcomes = [(SL.settle_margin(net, boost, ob, _no_draw), 1.0)]
            else:
                outcomes = [(SL.settle_margin(net, boost, ob, lambda: 1.0), 1 - f),
                            (SL.settle_margin(net, boost, ob, lambda: 0.0), f)]
            for m, w in outcomes:
                tally[DE.DEGREE_ORDINAL[DE.degree_from_net(m, 0)]] += w
        for got, want in zip(SL.band_odds(3, ob, boost), (t / 1000 for t in tally)):
            assert math.isclose(got, want, abs_tol=1e-12), (ob, boost, got, want)


@pytest.mark.parametrize("pool,ob,boost", [(2, 1.5, 0.0), (3, 2.25, 0.6), (4, 2.0, 0.8), (1, 1.75, 0.3)])
def test_the_200000_draw_arm_agrees_within_three_standard_errors(pool, ob, boost):
    """The dealt distribution through the real path: `roll_pool`, then `settle_margin` with the SAME
    generator's own uniform, graded by the one ladder at a zero obstacle."""
    n = 200_000
    rng = random.Random(20261101)
    tally = [0, 0, 0, 0]
    for _ in range(n):
        net = DE.roll_pool(pool, rng=rng).net
        m = SL.settle_margin(net, boost, ob, rng.random)
        tally[DE.DEGREE_ORDINAL[DE.degree_from_net(m, 0)]] += 1
    seen = 0
    for band, p in enumerate(SL.band_odds(pool, ob, boost)):
        se = math.sqrt(max(p * (1 - p), 1e-12) / n)
        assert abs(tally[band] / n - p) <= 3 * se + 1e-9, (pool, ob, boost, band, tally[band] / n, p)
        seen += 1
    assert seen == 4


def test_the_rule_is_a_mu_shift_never_an_ob_change():
    """The obstacle is only the fraction's source: an Ob and a boost with the same `boost - ob` deal
    the same settled margins (advantage is a shift of the roll, `resolution-diagnostic` section 2)."""
    for net in (-1, 0, 2):
        assert SL.settle_margin(net, 0.5, 2.0, lambda: 0.25) == SL.settle_margin(net, 0.0, 1.5, lambda: 0.25)


def test_the_record_forms_are_the_two_owners_over_a_records_fields():
    """`record_odds` and `settle_record` take a contest record's fields (pool, ob, leverage, the entry's net)
    so a host names no boost arithmetic; each is the existing pure function over the roll's own boost."""
    for pool, ob, lev in ((2, 1.5, 0.0), (4, 2.0, 0.5), (3, 2.25, 1.0)):
        boost = SL.net_boost(lev, pool)
        assert SL.record_odds(pool, ob, lev) == SL.band_odds(pool, ob, boost)
        for raw in (-1, 0, 2, 5):
            entry_net = raw + boost                     # what the entry returns: the roll plus its boost
            for u in (0.0, 0.5, 0.999):
                assert SL.settle_record(entry_net, lev, pool, ob, lambda: u) == \
                    SL.settle_margin(raw, boost, ob, lambda: u)
    assert SL.settle_record(3.0, 0.0, 2, 2.0, _no_draw) == 1        # whole: the identity, nothing drawn
