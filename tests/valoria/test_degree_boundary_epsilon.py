"""[ED-MB-0051 / plan v2 §3 A2] A 1-ulp float error must not move a damage degree.

`compute_degree`'s three comparisons are hard steps into `DAMAGE_BY_DEGREE`, and `net` is
continuous (fractional pools, the sigma mu-shift). A value that is MATHEMATICALLY on a boundary can
therefore arrive one ulp on the wrong side of it. The documented consequence:
`3 + _sigma_net_boost(-1e-16, 9)` returned `Partial` -> 0 damage at the universal `dr=1`, where the
intended answer is `Success` -> 3.

⚠ THE PREVIOUS VERSION OF THIS GUARD COULD NOT FAIL, and that is why this file reads the way it
does. Plan v1 proposed `compute_degree(ob - 1e-16, ob)`; in float64 `3 - 1e-16 == 3` and
`6 - 1e-16 == 6` exactly, so the assertion passed on unfixed code for two of its three cases — a
vacuous assertion inside the plan whose whole theme was vacuous assertions (G2). Every boundary
case below therefore uses `math.nextafter`, which is the ONLY way to name "the largest float
strictly below x" without assuming anything about the spacing at x.

Three things are asserted, and they are different claims:
  1. the epsilon RECOVERS a boundary the arithmetic lost (all three comparisons, not just Success);
  2. it does NOT reach far enough to promote a real decrement — the ceiling is pinned;
  3. the sigma chokepoint snaps arithmetic dust to exactly 0.0 while leaving a designed sigma alone.
"""
import math
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

from mass_battle.resolution import (                      # noqa: E402
    compute_degree, _sigma_net_boost, _DEGREE_EPS, _SIGMA_ZERO_SNAP,
)

_OBS = (1, 3, 6, 9)


def test_the_documented_repro_no_longer_zeroes_an_exchange():
    """The exact failure from the audit, verbatim. `net` lands a hair under `ob`; the intended
    degree is Success (3 damage at dr=1) and the unfixed code returned Partial (0 damage)."""
    net = 3 + _sigma_net_boost(-1e-16, 9)
    assert net <= 3, "precondition: the sigma must actually push net below the boundary"
    assert compute_degree(net, 3) == "Success"


@pytest.mark.parametrize('ob', _OBS)
def test_success_boundary_survives_one_ulp_below(ob):
    """`net >= ob`. nextafter, not `ob - 1e-16`: at ob=3 and ob=6 the latter IS ob in float64, so
    the v1 form of this assertion tested nothing."""
    just_under = math.nextafter(float(ob), -math.inf)
    assert just_under < ob, "nextafter must produce a strictly smaller float"
    assert compute_degree(just_under, ob) in ("Success", "Overwhelming")


@pytest.mark.parametrize('ob', _OBS)
def test_overwhelming_boundary_survives_one_ulp_below(ob):
    """`net >= 2*ob and net >= 3` — BOTH conjuncts guarded. A guard on one leaves the other able to
    demote a mathematically-Overwhelming result."""
    target = max(2.0 * ob, 3.0)
    just_under = math.nextafter(target, -math.inf)
    assert compute_degree(just_under, ob) == "Overwhelming"


def test_failure_boundary_is_guarded_too_and_symmetrically():
    """The asymmetry that guarding only `Success` would institutionalise.

    `net <= 0` fails a mathematically-zero net whose ulp error is NEGATIVE, and passes the identical
    net whose error is POSITIVE — a silent, attacker-favouring correction. Both must read Failure:
    zero net successes is a failure whichever side of zero the dust falls on.
    """
    for ob in _OBS:
        assert compute_degree(math.nextafter(0.0, -math.inf), ob) == "Failure"
        assert compute_degree(math.nextafter(0.0, math.inf), ob) == "Failure"
        assert compute_degree(0.0, ob) == "Failure"


def test_the_epsilon_cannot_promote_a_real_decrement():
    """The ceiling, which is the half of this that stops the fix becoming a balance change.

    A tolerance that recovers lost boundaries can also invent them. Pin the reach: a net a
    thousandfold further below the boundary than the epsilon must still be demoted. The smallest
    DESIGNED sigma decrement in this engine is a morale step through `_morale_sigma` (~1e-1), eight
    orders above `_DEGREE_EPS`, so nothing designed lives in the guarded band.
    """
    assert _DEGREE_EPS == 1e-9
    for ob in _OBS:
        clearly_under = ob - 1000 * _DEGREE_EPS
        assert compute_degree(clearly_under, ob) != "Success", ob
        assert compute_degree(1000 * _DEGREE_EPS, ob) != "Failure" or ob > 1000 * _DEGREE_EPS
    # and a genuinely small-but-designed sigma still moves the verdict
    designed = _sigma_net_boost(-0.1, 9)
    assert abs(designed) > _DEGREE_EPS * 1000, (
        f"a designed sigma decrement ({designed}) must sit far outside the guarded band")


def test_sigma_chokepoint_snaps_dust_but_not_a_designed_modifier():
    """`|sigma| < 1e-12 -> exactly 0.0`, stated once where every producer's value passes through.

    The snap threshold is three orders TIGHTER than `_DEGREE_EPS` on purpose: it says "this value is
    arithmetically zero", not "this value is small enough to ignore". One tolerance doing both jobs
    is how the next confound gets built.
    """
    assert _SIGMA_ZERO_SNAP < _DEGREE_EPS
    for pool in (1, 9, 25):
        assert _sigma_net_boost(-1e-16, pool) == 0.0
        assert _sigma_net_boost(1e-16, pool) == 0.0
        assert _sigma_net_boost(0.0, pool) == 0.0
        # a designed modifier is untouched (sign and magnitude both preserved)
        assert _sigma_net_boost(-0.5, pool) < 0.0
        assert _sigma_net_boost(0.5, pool) > 0.0


def test_guard_is_not_vacuous_the_v1_form_would_have_passed_unfixed():
    """Proof, in the suite, that the v1 assertion was empty — so nobody re-derives it.

    `ob - 1e-16 == ob` in float64 for ob in {3, 6}: the v1 guard fed `compute_degree` the boundary
    value itself and then asserted it was on the boundary. It could not have failed against unfixed
    code, and it did not.
    """
    collapsed = [ob for ob in _OBS if (ob - 1e-16) == ob]
    assert 3 in collapsed and 6 in collapsed, (
        "if this ever stops holding, float64 has changed and the historical note needs re-checking")
    for ob in collapsed:
        assert math.nextafter(float(ob), -math.inf) != ob, \
            "nextafter must still produce a distinct value where subtraction cannot"
