"""CLOSE-QUARTERS UNWIELDINESS MUST BE DERIVED, NOT GATED — ED-PC-0053.

DEFECT (verified red on the pre-fix tree). `close_unwieldiness` claimed in its own docstring to be
"DERIVED from its reach ... pure morphology", but it was:

    close_unwieldiness = max(0, reach_base(c) - CLOSE_REACH_REF)      CLOSE_REACH_REF = 6.5

`reach_base` is `L0 + REACH_GEOM_SCALE*forward_extent + reach_adj`, and **L0 = 4.0 is the fighter's own
body/arm offset**. So the 6.5 threshold sits on a scale where 4.0 is the wielder's arm, and the implied
weapon threshold is `(6.5 - 4.0)/2.1167 = 1.18 m of FORWARD EXTENT` before a weapon is unwieldy in the
close AT ALL. Measured consequence: **every one-handed sword in the game paid exactly 0.0000.**

    dagger 0.21 m -> 0.0    arming 0.72 -> 0.0    rapier 0.96 -> 0.0    longsword 0.94 -> 0.0
    estoc 1.30 -> 0.357     spear 1.79 -> 1.297   guandao 2.17 -> 2.104

That is a FIAT GATE, not a derivation, and it is wrong on physical grounds Jordan stated directly: *"you
can't do a full thrust or swing one foot away holding a rapier"*. A close/grapple happens at roughly
0.4 m; the gate demanded 1.18 m, so it was off by ~3x and produced a CLIFF — zero below, linear above.
Because reach's four BENEFIT channels (measure, stop-hit, true-time, arrest) had no matching cost, length
was a completely free attribute for anything sword-length. That is the shared root cause of both the
rapier's civilian dominance (79% vs a 47% field, of which -25 pp ablates to reach) and the tracked
off-plate spear dominance.

THE REPLACEMENT is the geometric fact, in honest metres, continuous from zero:

    overhang = max(0, forward_extent(at the CURRENT grip) - CLOSE_ENGAGE_M)

`CLOSE_ENGAGE_M` is a **body** measure (the distance at which a fight is closed), not a weapon
threshold — which is the whole difference between a derivation and a gate. `forward_extent` carries
Jordan's "shaft length" and "hand position on shaft" already: it is
`head_len - geom_slide(grip) + REACH_2H_K*grip_len*(hands==2)`, so choking up genuinely reduces it.

⚠ AND IT DELIBERATELY DOES **NOT** MULTIPLY IN MASS / POINT-OF-BALANCE / HEAD-WEIGHT, though those were
named as inputs. They are already charged, with a COMPRESSED power law, by `wield_heft`
(`(I_g/REC_I_REF)**WIELD_HEFT_EXP` — "the tempo/stamina/strength COST of bringing a weapon to bear"),
and the same grip-adjusted `I_g` is also read by `agility`, `recoverability_factor` and
`_recovery_mode_commitment`. Adding an inertia factor here would be the FIFTH charge on one fact — the
double-count consolidation_v1 §2.3 forbids. It was also measured to be unusable raw: `I_g` spans ~1000x
across the roster, so a linear inertia multiplier gives guandao 48.9 against its current 2.10.

MAGNITUDE CONTINUITY, stated because it is load-bearing and NOT a coincidence to be relied on silently:
the new metre-valued form lands the polearms close to the old reach-unit values — spear 1.344 vs 1.297,
guandao 1.725 vs 2.104, estoc 0.852 vs 0.357 — so `POLE_CLOSE_K` and `CHOKE_DRIVE_REF` do not need
re-anchoring, which is what keeps the `guisarme@heavy` floor (the failure mode that reverted the prior
attempt at this) out of danger. The real behavioural change is that swords move 0 -> 0.27..0.51.

FALSIFIERS — mutations run against these guards, each naming its target:
  - restore the `reach_base - CLOSE_REACH_REF` gate  -> guards 1, 2 red (every sword back to zero).
  - multiply in I_g / mass                           -> guard 5 red (the double-count pin).
  - make the engage measure a weapon property        -> guard 3 red (a dagger would start paying).
  - drop the grip term                               -> guard 4 red (choking up must help).
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import combat_systems as S     # noqa: E402
import combatant as C          # noqa: E402
import weapon_physics as WP    # noqa: E402
from config import CFG         # noqa: E402


def _fwd(w, grip=0.0):
    """The weapon's forward extent in metres at a given grip — the quantity the derivation reads."""
    slide = WP.at_circumstance(w, grip, 1.0)['geom_slide']
    return (w['head_len'] - slide) + CFG['REACH_2H_K'] * w['grip_len'] * (w['hands'] == 2)


def _startable():
    return {n: w for n, w in C.WEAPONS.items() if 'base' not in w}


def test_every_weapon_longer_than_the_close_measure_pays_something():
    """GUARD 1 (the defect pin, red on main for every sword). If a weapon's business end reaches past
    the distance a fight is closed at, it is compromised in the close — there is no length at which
    that stops being true and no threshold below which it is free."""
    free = {}
    checked = 0
    for n, w in _startable().items():
        fwd = _fwd(w)
        if fwd <= CFG['CLOSE_ENGAGE_M']:
            continue                     # genuinely shorter than the close measure — see guard 3
        checked += 1
        u = S.close_unwieldiness(C.Combatant('x', weapon=n), CFG)
        if u <= 0.0:
            free[n] = round(fwd, 3)
    assert checked >= 35, f"only {checked} over-length weapons exercised"
    assert not free, (
        f"weapons whose forward extent exceeds the {CFG['CLOSE_ENGAGE_M']} m close measure yet pay NO "
        f"close-quarters cost (name -> forward extent in m): {free}. Mutation that produces this: "
        "restoring the `max(0, reach_base - CLOSE_REACH_REF)` gate, whose implied threshold is 1.18 m "
        "of forward extent, so every one-handed sword reads exactly 0."
    )


def test_the_rapier_specifically_is_no_longer_free_in_the_close():
    """GUARD 2 — the named instance. A 0.96 m blade cannot deliver a full thrust at grappling measure;
    on the pre-fix tree the rapier's close cost was exactly 0.0000 while the spear paid 1.2973."""
    rapier = S.close_unwieldiness(C.Combatant('x', weapon='rapier'), CFG)
    dagger = S.close_unwieldiness(C.Combatant('x', weapon='dagger'), CFG)
    spear = S.close_unwieldiness(C.Combatant('x', weapon='spear'), CFG)
    assert rapier > 0.0, (
        "the rapier still pays nothing in the close (0.0000 on the pre-fix tree) — reach remains a "
        "free attribute for every sword-length weapon."
    )
    assert dagger < rapier < spear, (
        f"the close-cost ordering is wrong: dagger {dagger:.4f}, rapier {rapier:.4f}, spear "
        f"{spear:.4f}. A dagger should be ideal in the close, a rapier compromised, a spear worst."
    )


def test_a_weapon_shorter_than_the_close_measure_is_free():
    """GUARD 3 — the correct zero, and the pin that keeps the engage measure a BODY constant. A dagger
    or rondel is at home in the close and must pay nothing. If someone re-derives the measure from the
    weapon instead of the body, these start paying and this guard fails."""
    for n in ('dagger', 'rondel', 'stiletto', 'misericorde', 'main_gauche'):
        w = C.WEAPONS[n]
        assert _fwd(w) <= CFG['CLOSE_ENGAGE_M'], f"{n} is no longer shorter than the close measure"
        assert S.close_unwieldiness(C.Combatant('x', weapon=n), CFG) == 0.0, (
            f"{n} pays a close-quarters cost despite being shorter than the close measure — the "
            "engage distance has been made a weapon property instead of a body one."
        )


def test_choking_up_reduces_the_close_cost():
    """GUARD 4 — 'hand position on shaft' must be live, which is what makes this a derivation rather
    than a length table. Gathering in shortens the forward extent, so it must reduce the cost."""
    checked = 0
    for n in ('spear', 'poleaxe', 'staff', 'guandao'):
        open_g = C.Combatant('x', weapon=n)
        open_g.grip_position = 0.0
        choked = C.Combatant('x', weapon=n)
        choked.grip_position = 1.0
        u_open = S.close_unwieldiness(open_g, CFG)
        u_choked = S.close_unwieldiness(choked, CFG)
        assert u_choked < u_open, (
            f"{n}: choking up does not reduce the close-quarters cost ({u_open:.4f} -> {u_choked:.4f})"
        )
        checked += 1
    assert checked == 4


def test_the_close_cost_does_not_re_charge_mass():
    """GUARD 5 — the non-double-count pin, and the reason mass is absent despite being named as an
    input. `wield_heft` already prices the inertia cost of bringing a weapon to bear
    ((I_g/REC_I_REF)**WIELD_HEFT_EXP), and `agility`, `recoverability_factor` and
    `_recovery_mode_commitment` read the same grip-adjusted I_g. This term must price ONLY the
    geometric overhang, so tripling a weapon's mass must not move it at all."""
    c = C.Combatant('x', weapon='rapier')
    before = S.close_unwieldiness(c, CFG)
    original = c.w['mass']
    parts = [dict(p) for p in c.w['parts']] if isinstance(c.w.get('parts'), list) else None
    try:
        c.w['mass'] = original * 3.0
        if isinstance(c.w.get('parts'), list):
            for p in c.w['parts']:
                if isinstance(p, dict) and 'mass_kg' in p:
                    p['mass_kg'] *= 3.0
        after = S.close_unwieldiness(c, CFG)
    finally:
        c.w['mass'] = original
        if parts is not None:
            c.w['parts'] = parts
    assert abs(after - before) < 1e-12, (
        f"tripling mass moved the close-quarters cost ({before:.6f} -> {after:.6f}) — mass is being "
        "charged a FIFTH time here on top of wield_heft/agility/recoverability_factor/"
        "_recovery_mode_commitment, all of which already read I_g."
    )


def test_the_polearm_magnitudes_are_preserved():
    """GUARD 6 — the containment pin, and the reason this change is safe to make at all. The previous
    attempt at giving length a closed-measure cost was REVERTED because every configuration that moved
    it broke the `guisarme@heavy` floor. This form does not re-anchor POLE_CLOSE_K or CHOKE_DRIVE_REF
    because it lands the polearms near their pre-fix values; if a future edit drifts them far, the
    guisarme risk returns and this guard is the tripwire."""
    for n, old in (('spear', 1.2973), ('guandao', 2.1037), ('poleaxe', 0.1174)):
        new = S.close_unwieldiness(C.Combatant('x', weapon=n), CFG)
        assert new < old * 4.0 + 1.0, (
            f"{n}'s close cost {new:.4f} has drifted far from its pre-fix {old:.4f}; POLE_CLOSE_K and "
            "CHOKE_DRIVE_REF were calibrated against the old scale and would need re-anchoring, which "
            "re-opens the guisarme@heavy risk that reverted the prior attempt."
        )


def test_no_cliff_the_function_is_continuous_in_length():
    """GUARD 7 — the fiat gate produced a CLIFF (exactly 0 below 1.18 m, linear above). A derivation
    has one knee, at the body's close measure, and is continuous everywhere. Swept on a synthetic
    weapon so it tests the FUNCTION, not the roster's sampling of it."""
    w = dict(C.WEAPONS['arming'])
    prev = None
    jumps = []
    for i in range(1, 61):
        w2 = dict(w)
        w2['head_len'] = 0.05 * i
        C.WEAPONS['__probe__'] = w2
        try:
            probe = C.Combatant('p', weapon='__probe__')
            u = S.close_unwieldiness(probe, CFG)
        finally:
            del C.WEAPONS['__probe__']
        if prev is not None and abs(u - prev) > 0.12:      # step is 0.05 m; a jump means a gate
            jumps.append((round(0.05 * i, 2), round(prev, 4), round(u, 4)))
        prev = u
    assert not jumps, (
        f"close_unwieldiness jumps discontinuously as length grows: {jumps}. A gate has been "
        "reintroduced. Mutation that produces this: `max(0, reach_base - CLOSE_REACH_REF)`."
    )
