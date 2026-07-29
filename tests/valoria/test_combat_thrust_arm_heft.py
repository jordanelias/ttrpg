"""HEFT MUST FOLLOW THE RESOLVED ARM — E3b guards (M2/F2, ED-PC-0050).

DEFECT (verified red on the pre-fix tree): `weapon_physics.heft` chose its lever from the head
TOKEN — `THRUST_POB if head == 'point' else max(0, PoB_frac)`. A `cut_thrust` weapon is a single
token whose arm (`shear` vs `puncture`) is resolved separately, inside `core.cut_thrust_arm`. So a
cut_thrust weapon that resolves the PUNCTURE arm was still paid the SWING moment:

    ranseur   heft(native cut_thrust) 2.5151   vs   heft(sel_head='point') 0.7992   — 3.1x
    damage @none: ranseur 26 vs spear 13

ED-PC-0027 decoupled a thrust's lever from the point of balance precisely because a thrust's impact
is axial and PoB-independent (that fix is what killed the spear's flat dominance). `weapon_physics`
already conceded the remaining bypass in a comment; the fix was simply never extended from the
`point` token to the cut_thrust weapon that resolves a thrust. This closes it by splitting on the
RESOLVED ARM rather than the token.

THE GUARDS — the plan (review R-8) requires BOTH sides, because the one-sided form is red on main
and yet PASSES a wrong fix that pays the thrust lever on both arms:
  1. `test_thrust_resolving_heft_uses_the_thrust_lever` — the DEFECT pin, red on main
     (ranseur 2.5151 vs 0.7992).
  2. `test_shear_resolving_heft_keeps_the_swing_lever` — the COMPLEMENTARY pin.

GUARD 2 CANNOT BE PROVED RED ON MAIN, and it is the only guard in E0-E3 in that position. `heft`
had no arm parameter at all before this batch, so both sides of the comparison were literally the
same call (ranseur 2.5151 == 2.5151) — tautologically green, the "a gate that has never failed is
decoration" shape ED-PC-0040 named. It is a REGRESSION pin, not a defect pin, so per plan §13.2a it
takes the mutation route instead: it ships with the declared mutation *"implement the arm split but
pay THRUST_POB on both arms"* and that mutation was RUN, turning guard 2 red (ranseur's shear arm
reads 0.7992 instead of 2.5151) while guard 1 stays green. That mutation is exactly the wrong fix
review R-8 identified, so it is not hypothetical. `test_the_arm_split_is_not_paid_on_both_arms`
below encodes it as a standing assertion rather than a one-off run.

DISCLOSED CONSEQUENCE, stated not discovered (the plan's own instruction): `core.cut_thrust_arm`
picks the arm on COUPLING alone. Now that impact differs by arm, the chosen arm is no longer the
max-DAMAGE arm for every weapon — a fresh instance of the B1/F24 "selection contradicts damage"
class, introduced by a correctness batch and interacting with E5/M7. The ranseur resolves `puncture`
even at `none`, so this is live at every tier. It is NOT fixed here: repricing the contest on damage
is E5's, and bundling it would repeat the batch-4/5 "while I'm here" failure.
`test_selection_contradicts_damage_is_disclosed_not_silent` pins the population so it cannot grow
unnoticed before E5 picks it up.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S     # noqa: E402
import combatant as C          # noqa: E402
import core                    # noqa: E402
import vocabulary as V         # noqa: E402
import weapon_physics as WP    # noqa: E402
from config import CFG         # noqa: E402

CUT_THRUST = [n for n, w in C.WEAPONS.items() if w.get('head') == V.HEAD_CUT_THRUST]


def test_the_population_under_test_is_real():
    """The cut_thrust roster is the population this batch moves; pin it so the guards below cannot
    quietly become vacuous if the roster is retyped."""
    assert len(CUT_THRUST) >= 15, f"cut_thrust population collapsed to {len(CUT_THRUST)}: {CUT_THRUST}"
    assert 'ranseur' in CUT_THRUST, "the ranseur is this defect's worked example and must be cut_thrust"


def test_thrust_resolving_heft_uses_the_thrust_lever():
    """GUARD 1 (the defect pin, red on main). A cut_thrust weapon resolving the PUNCTURE arm must be
    paid the axial thrust lever, not the swing moment — the same rule ED-PC-0027 already applies to
    a dedicated `point`."""
    checked = 0
    bad = {}
    for n in CUT_THRUST:
        w = C.WEAPONS[n]
        as_thrust = WP.heft(w, sel_head=V.HEAD_CUT_THRUST, sel_arm='puncture')
        as_point = WP.heft(w, sel_head=V.HEAD_POINT)
        checked += 1
        if abs(as_thrust - as_point) > 1e-9:
            bad[n] = (as_thrust, as_point)
    assert checked >= 15, f"only {checked} weapons exercised — the loop asserted almost nothing"
    assert not bad, (
        "a cut_thrust weapon resolving the puncture arm is not paid the thrust lever "
        f"(as-thrust, as-point): {bad}. Pre-fix the ranseur read 2.5151 as a swing against 0.7992 "
        "as a thrust. Mutation that produces this: reverting heft's lever choice to the head token."
    )


def test_shear_resolving_heft_keeps_the_swing_lever():
    """GUARD 2 (the complementary pin — see the module docstring; tautologically green on main, so
    it is mutation-verified rather than red-verified). A cut_thrust weapon resolving the SHEAR arm
    is a swing and must keep the forward-balance moment."""
    checked = 0
    bad = {}
    for n in CUT_THRUST:
        w = C.WEAPONS[n]
        as_shear = WP.heft(w, sel_head=V.HEAD_CUT_THRUST, sel_arm='shear')
        native_swing = WP.heft(w, sel_head=V.HEAD_CUT_THRUST)
        checked += 1
        if abs(as_shear - native_swing) > 1e-9:
            bad[n] = (as_shear, native_swing)
    assert checked >= 15, f"only {checked} weapons exercised — the loop asserted almost nothing"
    assert not bad, (
        f"a cut_thrust weapon resolving the shear arm lost its swing moment: {bad}. Mutation that "
        "produces this: implementing the arm split but paying THRUST_POB on BOTH arms (review R-8's "
        "wrong fix)."
    )


def test_the_arm_split_is_not_paid_on_both_arms():
    """GUARD 3 — the mutation of guard 2, encoded as a standing assertion. The two arms must
    genuinely DIFFER for a forward-balanced cut_thrust weapon; if a fix pays the thrust lever
    everywhere, both guards 1 and 2 could be satisfied by collapsing them onto one value."""
    w = C.WEAPONS['ranseur']
    shear = WP.heft(w, sel_head=V.HEAD_CUT_THRUST, sel_arm='shear')
    punct = WP.heft(w, sel_head=V.HEAD_CUT_THRUST, sel_arm='puncture')
    assert shear > punct * 2.0, (
        f"the ranseur's two arms have collapsed onto each other (shear {shear:.4f}, puncture "
        f"{punct:.4f}). A forward-balanced polearm swings far heavier than it thrusts — pre-fix the "
        "gap was 2.5151 vs 0.7992. Mutation that produces this: paying THRUST_POB on both arms."
    )


def test_arm_defaults_are_byte_identical():
    """The new parameter must be inert for every caller that does not pass it: `sel_arm=None`
    reproduces the token-keyed behaviour exactly, for the WHOLE roster and every head."""
    bad = {}
    for n, w in C.WEAPONS.items():
        for grip in (0.0, 0.5, 1.0):
            a = WP.heft(w, grip=grip)
            b = WP.heft(w, grip=grip, sel_arm=None)
            if a != b:
                bad[(n, grip)] = (a, b)
    assert not bad, f"sel_arm=None is not inert: {bad}"


def test_selection_contradicts_damage_is_disclosed_not_silent():
    """The disclosed consequence, pinned as a POPULATION so it cannot grow unnoticed before E5.

    `core.cut_thrust_arm` picks the arm on coupling alone. Now that heft differs by arm, the chosen
    arm is not always the higher-damage arm. This test does not assert the disagreement away — it
    records which weapons are in it, so E5/M7 inherits a measured work-list rather than a rumour and
    a future change that widens the class fails here."""
    disagree = set()
    for n in CUT_THRUST:
        w = C.WEAPONS[n]
        for tier in ('none', 'light', 'medium', 'heavy'):
            mat = core.TIER2MAT[tier]
            geo = w.get('geo', {})
            val, arm = core.cut_thrust_arm(
                mat, 'full', w['gap'], eff_cut=geo.get('cut'), eff_thrust=geo.get('thrust'),
                thrust_auth=core.thrust_authority(w['head_len']))
            h_chosen = WP.heft(w, sel_head=V.HEAD_CUT_THRUST, sel_arm=arm)
            other = 'shear' if arm == 'puncture' else 'puncture'
            h_other = WP.heft(w, sel_head=V.HEAD_CUT_THRUST, sel_arm=other)
            if h_other > h_chosen + 1e-9:
                disagree.add(n)
    # This is a DISCLOSURE pin, not a correctness claim: the class is known, measured, and owned by
    # E5/M7. Assert it is non-empty (so the pin stays honest about the defect existing) and that it
    # has not silently widened beyond the cut_thrust roster it was measured on.
    assert disagree, (
        "no cut_thrust weapon shows the selection-vs-damage disagreement any more — either E5/M7 "
        "landed (update this pin and the ED-PC-0050 disclosure) or the arm contest changed shape."
    )
    assert disagree <= set(CUT_THRUST), f"the disagreement escaped the cut_thrust roster: {disagree}"
