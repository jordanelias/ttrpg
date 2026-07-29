"""THE SHARED STRIKE-POINT LEVER — E2a guards (M1/F1, ED-PC-0047).

DEFECT (verified on the pre-fix tree): `weapon_physics.percussion_authority` used the whole-weapon
**PoB_frac** — the centre-of-balance offset about the working hand — as its lever. A rear
counterweight therefore SUBTRACTS from percussive authority, and a symmetric, centre-gripped haft
cancels to EXACTLY zero regardless of mass:

    staff   perc_auth 0.0000  puncture 0.0000  adef_cap 0.0  percussion_stagger (0.0, 0.0)
    mace    perc_auth 8.0000     goedendag 8.0000  poleaxe 7.4843  lucerne 6.5392  bec 6.3629

A rear counterweight does not weaken a blow — it is mass you carry, not mass you cancel. The repair
re-points the lever from "the whole mass at the centre of balance" to "the DELIVERED mass at the
STRIKE POINT" (`weapon_physics.strike_point_lever`, the single owner shared with E2b).

THESE ARE THE GUARDS, and each is scoped to what it can actually observe:

  1. `test_no_blunt_native_weapon_derives_zero_percussion` — R-1 as SCOPED by the adversarial review.
     The unscoped form ("no weapon with mass > 0") goes red on 37/51 weapons, 36 correct by design
     (`reversed_grip_percussion` returns 0.0 for every 1H weapon and every hafted non-blunt head).
     Scoped to BLUNT-NATIVE heads, only the staff failed on the pre-fix tree.
  2. `test_staff_percussion_lands_in_the_anchor_band` — R-11: a NON-ZERO assertion is gameable by an
     epsilon, so the staff is pinned to a BAND. Both edges are load-bearing and independently
     grounded: the FLOOR is the last measured staff authority before the Phase-B located-part model
     introduced this defect (2.52, recorded in `percussion_authority`'s own docstring), the CEILING
     keeps the bare-wood staff strictly the weakest percussor of the blunt-native family (it must
     not reach the steel-hammer ceiling PERC_CAP).
  3. `test_staff_stagger_is_a_real_fraction_of_the_maces` — asserted THROUGH `percussion_stagger`
     with a constructed wound, i.e. through the consumer that ED-PC-0031's headline mechanic
     actually runs on, not through the physics function alone.
  4. `test_strike_point_lever_is_nonzero_at_the_hand` — the property that makes this form usable by
     **E2b**: a strike delivered AT the working hand (a guard-mounted crescent, a pommel) has the
     hand/hilt's own lever, never zero. E2b's `percussion_element_authority` (`|x|/Lt`) is defective
     for exactly this reason and MUST be routed through this function; that is E2b's commit, not
     this one, so this test guards the shared form's contract rather than E2b's consumer.
  5. `test_strike_point_lever_shape` — monotonicity in both arguments + the exactness pin
     `lambda(m_total, Lt) == 1.0` (all of the weapon's mass at its tip IS the maximum swing moment).

FALSIFIERS (CLAUDE.md §0.1 point 3) — the mutations run against these guards, each naming its target:
  · revert the lever to `derive(w)['PoB_frac']`  -> guard 1 red, naming the staff.
  · return a token 0.1 authority for the staff   -> guard 2 red on the FLOOR (the band, not non-zero).
  · let the staff reach PERC_CAP                 -> guard 2 red on the CEILING.
  · drop STRIKE_HAND_LEVER to 0.0                -> guard 4 red (the E2b-serving property).
"""
import math
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S      # noqa: E402
import combatant as C           # noqa: E402
import vocabulary as V          # noqa: E402
import weapon_physics as WP     # noqa: E402
from config import CFG          # noqa: E402

# The anchor band. FLOOR: the last measured staff percussion authority before the Phase-B
# located-part mass model zeroed it (2.52 — percussion_authority's docstring records the
# 2026-06-30 anchor set "mace 7.45 > poleaxe 5.83 > staff 2.52"), rounded down. This is also the
# order of core.py's own recorded intent, "a wooden staff (p_auth ~4) is largely absorbed".
# CEILING: strictly below the steel-hammer ceiling PERC_CAP=8.0, with margin — a bare-wood tip is
# not a steel hammer.
STAFF_BAND = (2.5, 6.5)


def _blunt_native():
    """The weapons whose NATIVE head is blunt — the only scope in which 'zero percussion authority'
    is a defect rather than the designed `reversed_grip_percussion` gate (review R-1)."""
    return {n: w for n, w in C.WEAPONS.items() if w.get('head') == V.HEAD_BLUNT}


def test_blunt_native_scope_is_what_the_review_scoped_it_to():
    """Test premise, pinned: the scoped roster is the six weapons R-1 names. If a blunt-native
    weapon is added or removed this fails LOUDLY rather than silently narrowing guard 1."""
    assert set(_blunt_native()) == {
        'staff', 'mace', 'poleaxe', 'bec_de_corbin', 'lucerne_hammer', 'goedendag'}


def test_no_blunt_native_weapon_derives_zero_percussion():
    """R-1 (SCOPED): a weapon whose native head is BLUNT is a percussor by construction — deriving
    exactly 0.0 authority from it means the lever, not the weapon, is broken. RED ON THE PRE-FIX
    TREE, naming the staff (the other five read 6.36–8.00)."""
    zeros = {n: WP.percussion_authority(w) for n, w in _blunt_native().items()
             if WP.percussion_authority(w) <= 0.0}
    assert not zeros, (
        f"blunt-native weapon(s) derive ZERO percussion authority: {zeros}. A blunt head with mass "
        f"and a lever cannot be a non-percussor; the lever is measuring the wrong thing.")
    # and the same must hold through the two derived consumers the zero propagated into
    for n, w in _blunt_native().items():
        assert WP.puncture_pressure(w) >= 0.0
        assert WP.percussion_authority(w, grip=0.0, room=1.0) > 0.0, n


def test_staff_percussion_lands_in_the_anchor_band():
    """R-11: a BAND, not non-zero. An epsilon fails the floor; a cap-saturating value fails the
    ceiling; and the ordering pin keeps the bare-wood staff the weakest of the blunt-native family."""
    lo, hi = STAFF_BAND
    staff = WP.percussion_authority(C.WEAPONS['staff'])
    assert lo <= staff <= hi, (
        f"staff percussion_authority {staff:.4f} outside the anchor band {STAFF_BAND} — the ~4 "
        f"intent recorded in core.py's FIX-1b comment and the 2.52 pre-Phase-B measurement")
    assert staff < WP.PERC_CAP, "a bare-wood tip must not reach the steel-hammer ceiling"
    others = {n: WP.percussion_authority(w) for n, w in _blunt_native().items() if n != 'staff'}
    assert all(staff < v for v in others.values()), (
        f"the staff ({staff:.4f}) must stay the WEAKEST blunt-native percussor: {others}")


def _stagger(weapon, armor='medium', deg='success', wound=6):
    """percussion_stagger through a constructed exchange — the ED-PC-0031 consumer path."""
    striker = C.Combatant('a', weapon=weapon, strength=4)
    striker.sel_head = V.HEAD_BLUNT
    striker.sel_perc = WP.percussion_authority(C.WEAPONS[weapon], grip=0.0)
    victim = C.Combatant('b', weapon='arming', armor=armor)
    return S.percussion_stagger(striker, victim, wound, deg, CFG)


def test_staff_stagger_is_a_real_fraction_of_the_maces():
    """The headline ED-PC-0031 mechanic, asserted where it is CONSUMED: a staff that draws no blood
    still winds and staggers. Pinned as a BAND fraction of the mace's stagger — an epsilon authority
    (0.1/8 = 1.3% of the mace) fails the floor; mace-parity fails the ceiling."""
    s_drain, s_poise = _stagger('staff')
    m_drain, m_poise = _stagger('mace')
    assert s_drain > 0.0 and s_poise > 0.0, (
        "a landed staff blow delivers NO wind and NO stagger — percussion_stagger's own docstring "
        "cites the staff as the worked example of the mechanic")
    for label, s, m in (('stamina', s_drain, m_drain), ('poise', s_poise, m_poise)):
        frac = s / m
        assert 0.30 <= frac <= 0.85, (
            f"staff/mace {label} stagger fraction {frac:.4f} outside [0.30, 0.85] "
            f"(staff {s:.5f}, mace {m:.5f})")


def test_strike_point_lever_is_nonzero_at_the_hand():
    """THE PROPERTY THAT SERVES E2b. A striking element mounted AT the working hand (x = 0) — a
    hook_sword's guard crescent, a pommel — still swings on the hand/hilt's own lever. The bare
    `|x| / Lt` form E2b currently uses returns 0 here, which is why E2b must consume THIS function."""
    w = C.WEAPONS['hook_sword']
    lam = WP.strike_point_lever(w, 0.30, 0.0)
    assert lam > 0.0, "a strike delivered at the hand must not derive a zero lever"
    # and it must be the STRICTLY smallest lever, not a flat floor that erases geometry
    assert lam < WP.strike_point_lever(w, 0.30, 0.20) < WP.strike_point_lever(w, 0.30, 0.60)


def test_strike_point_lever_shape():
    """Monotone in the delivered mass and in |x|, symmetric in the sign of x (a rear-facing fluke
    has a lever too), and EXACTLY 1.0 when the whole weapon's mass sits at its tip — the definition
    of the normaliser (`the maximum swing moment this weapon could present`)."""
    w = C.WEAPONS['poleaxe']
    Lt = WP.derive(w)['length_m']
    m_strike, _x, m_total = WP.delivered_strike(w)
    # EXACTNESS, not approx (CLAUDE.md §0.1 point 2): the normaliser is the function's OWN m_total, so
    # "all the mass at the tip" must reproduce 1.0 to the bit. (w['mass'] agrees to 1e-9 — the authored
    # primitive and the located-part sum are the same weapon — but they are not the same FLOAT, and
    # asserting on the authored one would be asserting a rounding, not the identity.)
    assert abs(m_total - w['mass']) < 1e-9, "premise: located parts sum to the authored mass"
    assert WP.strike_point_lever(w, m_total, Lt) == 1.0
    assert 0.0 < m_strike < m_total, "the poleaxe carries a real rear counterweight (butt + rear haft)"
    assert WP.strike_point_lever(w, 0.2, 0.5) < WP.strike_point_lever(w, 0.4, 0.5)
    assert WP.strike_point_lever(w, 0.2, 0.3) < WP.strike_point_lever(w, 0.2, 0.7)
    assert WP.strike_point_lever(w, 0.2, -0.4) == WP.strike_point_lever(w, 0.2, 0.4)
    assert math.isfinite(WP.strike_point_lever(w, 0.0, 0.0))
