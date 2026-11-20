"""[ED-MB-0051 / plan v2 §3 A2] A 1-ulp float error must not move a damage degree.

B05.03: the field grades on the owner's ladder (`dice_engine.degree_label`, which quantises the margin once to
milli-units, `MARGIN_SCALE`) and boosts with the owner's `sigma_leverage.net_boost`; `resolution.compute_degree`,
its `_DEGREE_EPS` and `_sigma_net_boost` are gone. This file's claims are unchanged and now observe the owner's
ladder: the ulp recovery is the quantisation, and its reach is half a milli-unit instead of 1e-9.

The ladder's three comparisons are hard steps into `DAMAGE_BY_DEGREE`, and `net` is
continuous (fractional pools, the sigma mu-shift). A value that is MATHEMATICALLY on a boundary can
therefore arrive one ulp on the wrong side of it. The documented consequence:
`3 + net_boost(-1e-16, 9)` returned `Partial` -> 0 damage at the universal `dr=1`, where the
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

from engine.dice_engine import dice_engine                          # noqa: E402
from engine.dice_engine.dice_engine import degree_label as compute_degree   # noqa: E402  the owner's ladder, string labels
from engine.dice_engine.sigma_leverage import net_boost             # noqa: E402
from modules.mass_battle.resolution import _SIGMA_ZERO_SNAP, _snap_sigma   # noqa: E402

# One milli-unit: the margin the ladder resolves (`round(MARGIN_SCALE * margin)`); the ladder's reach is half of it.
_MILLI = 1 / dice_engine.MARGIN_SCALE


from modules.mass_battle.resolution import _net_boost as _sigma_net_boost   # noqa: E402  -- the field's chokepoint itself, as the orchestration calls it

_OBS = (1, 3, 6, 9)


def test_the_documented_repro_no_longer_zeroes_an_exchange():
    """The exact failure from the audit, verbatim — and it still bites the same way after the
    2026-08-14 ruling, which is why this case survives the reband rather than being retired.

    `net` lands a hair under `ob`, i.e. a margin of mathematically zero with NEGATIVE dust. Under
    the ruled ladder a zero margin is Partial (the obstacle met, not exceeded); unguarded, the dust
    pushes it to Failure. `DAMAGE_BY_DEGREE` pays 1 for Partial and 0 for Failure, so the exchange
    is zeroed by arithmetic error exactly as the audit recorded. The intended BAND changed with the
    ruling; the defect and the fix did not.

    ⚠ AND THE ORIGINAL REPRO NO LONGER CONTAINS ANY DUST, which an adversarial pass caught. The
    `_SIGMA_ZERO_SNAP` chokepoint (asserted below) snaps `_sigma_net_boost(-1e-16, 9)` to exactly
    0.0, so `3 + that` is exactly 3.0 and the margin is exactly 0 — the case passes with
    the ladder's quantisation removed, i.e. it exercises the BAND, not the epsilon. Both forms are kept and
    labelled: the historical repro as a band case, and a genuine one-ulp-below margin as the
    epsilon case.
    """
    historical = 3 + _sigma_net_boost(-1e-16, 9)
    assert historical == 3.0, "the sigma chokepoint should have snapped this to exactly 3.0"
    assert compute_degree(historical, 3) == "Partial"

    # The epsilon case: a margin genuinely one ulp below zero. THIS is what needs the tolerance —
    # it reads Failure without it, and Failure pays 0 damage where Partial pays 1.
    dusty = math.nextafter(3.0, -math.inf)
    assert dusty - 3.0 < 0, "precondition: the margin must actually be below zero"
    assert compute_degree(dusty, 3) == "Partial"


@pytest.mark.parametrize('ob', _OBS)
def test_partial_boundary_survives_one_ulp_below(ob):
    """Margin 0 — the Failure/Partial step. New with the 2026-08-14 ruling: meeting the obstacle
    exactly is a Partial, so this boundary now carries a band change and needs the same guard the
    other two have always had.

    nextafter, not `ob - 1e-16`: at ob=3 and ob=6 the latter IS ob in float64, so that form of the
    assertion would test nothing (see the vacuity proof at the bottom of this file).
    """
    just_under = math.nextafter(float(ob), -math.inf)
    assert just_under < ob, "nextafter must produce a strictly smaller float"
    assert compute_degree(just_under, ob) == "Partial"


@pytest.mark.parametrize('ob', _OBS)
def test_success_boundary_survives_one_ulp_below(ob):
    """Margin 1 — the Partial/Success step under the ruled ladder (`net >= ob + 1`)."""
    target = float(ob) + 1.0
    just_under = math.nextafter(target, -math.inf)
    assert just_under < target, "nextafter must produce a strictly smaller float"
    assert compute_degree(just_under, ob) in ("Success", "Overwhelming")


@pytest.mark.parametrize('ob', _OBS)
def test_overwhelming_boundary_survives_one_ulp_below(ob):
    """Margin 3 — the Success/Overwhelming step (`net >= ob + 3`).

    The ruled ladder replaced the old two-conjunct bar (`net >= 2*ob AND net >= 3`) with a single
    margin test, so there is one boundary here rather than two. The guard is correspondingly
    simpler, NOT weaker: the one comparison that exists is the one that is pinned.
    """
    target = float(ob) + 3.0
    just_under = math.nextafter(target, -math.inf)
    assert just_under < target, "nextafter must produce a strictly smaller float"
    assert compute_degree(just_under, ob) == "Overwhelming"


def test_failure_boundary_is_guarded_too_and_symmetrically():
    """The asymmetry that guarding only `Success` would institutionalise.

    `net <= 0` fails a mathematically-zero net whose ulp error is NEGATIVE, and passes the identical
    net whose error is POSITIVE — a silent, attacker-favouring correction.

    ⚠ REBANDED 2026-08-14. This used to feed `net = 0` at every Ob, which under the ruled ladder is
    a margin of `-ob` — three bands from any boundary, so the epsilon could not have reached it
    however wide it was, and the test would have passed against arbitrarily broken code. It now
    probes the actual Failure/Partial step (margin 0) from both sides, which is where the asymmetry
    it was written to prevent can still occur.
    """
    for ob in _OBS:
        # dust BELOW the boundary must be recovered up to Partial...
        assert compute_degree(math.nextafter(float(ob), -math.inf), ob) == "Partial"
        # ...and dust ABOVE it must not be promoted past Partial. Same magnitude, both directions:
        # a tolerance that only ever helps one side is the silent, one-sided correction this guards.
        assert compute_degree(math.nextafter(float(ob), math.inf), ob) == "Partial"
        assert compute_degree(float(ob), ob) == "Partial"
        # and a genuine shortfall is still a Failure — the band below must remain reachable.
        assert compute_degree(ob - 1.0, ob) == "Failure"


def test_the_epsilon_cannot_promote_a_real_decrement():
    """The ceiling, which is the half of this that stops the fix becoming a balance change.

    A tolerance that recovers lost boundaries can also invent them. Pin the reach: a net a
    full milli-unit below the boundary (twice the ladder's reach) must still be demoted. The smallest
    DESIGNED sigma decrement in this engine is a morale step through `_morale_sigma` (~1e-1), orders
    above the ladder's half milli-unit, so nothing designed lives in the guarded band.
    """
    for ob in _OBS:
        # Each assertion names the band IMMEDIATELY below the boundary it is testing, never a
        # distant one. `!= "Success"` at a margin of -1e-6 would be true however far the epsilon
        # reached — Success is three bands away — so it would exclude nothing. Under the ruled
        # ladder the adjacent pairs are Failure/Partial at margin 0 and Partial/Success at 1.
        assert compute_degree(ob - _MILLI, ob) == "Failure", ob
        assert compute_degree(ob + 1 - _MILLI, ob) == "Partial", ob
        assert compute_degree(ob + 3 - _MILLI, ob) == "Success", ob
        # ...and the epsilon DOES reach at one ulp, so the pair above is a ceiling, not a floor.
        assert compute_degree(math.nextafter(float(ob), -math.inf), ob) == "Partial", ob
    # and a genuinely small-but-designed sigma still moves the verdict
    designed = _sigma_net_boost(-0.1, 9)
    assert abs(designed) > 10 * _MILLI, (
        f"a designed sigma decrement ({designed}) must sit far outside the guarded band")


def test_sigma_chokepoint_snaps_dust_but_not_a_designed_modifier():
    """`|sigma| < 1e-12 -> exactly 0.0`, stated once where every producer's value passes through.

    The snap threshold is far TIGHTER than the ladder's half milli-unit on purpose: it says "this value is
    arithmetically zero", not "this value is small enough to ignore". One tolerance doing both jobs
    is how the next confound gets built.
    """
    assert _SIGMA_ZERO_SNAP < 0.5 * _MILLI
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
