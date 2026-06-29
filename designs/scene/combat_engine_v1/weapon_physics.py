"""weapon_physics.py — derive a weapon's COMBAT DYNAMICS from its physical PRIMITIVES.

Implements designs/proposals/weapon_physics_and_concentration_model.md §4 (Jordan, 2026-06-05). A weapon is NOT a
bundle of hand-authored aggregates (spd, wt='light'/'heavy', closes_poorly, HEFT class, GATE caps). It is a set of
PRIMITIVES — mass, point-of-balance, blade/grip lengths, handedness, blade geometry — and every combat-relevant
quantity DERIVES from them, ONCE, here, as documented physics (Le Chevalier/Johnsson dynamics; ARMA-GTA).

This is the single basis the engine consumers wire to. It REPLACES, in one place, the top-down tables scattered
through the engine:
    core.HEFT={'light':0,'heavy':3}      -> authority (impact)        [issue #4]
    systems.GATE={weapon:{mode:cap}}     -> defense affinities         [issue #2]
    WEAPONS[*]['spd'] (hand-authored)    -> agility (1/MoI)            [issue #3]
    WEAPONS[*]['closes_poorly'] (flag)   -> close-quarters from reach  [issue #1]

PRIMITIVES consumed (from combatant.WEAPONS + combatant.GEOMETRY):
    mass (kg), pob_frac (PoB as a forward-balance fraction), head_len, grip_len (length units), hands,
    hand_guard, blade_guard, reach_adj, and the raw geometry curvature/edge_keenness/point_concentration/
    cross_section/strike_concentration.

DERIVED (the bottom-up basis):
    total_len, static_moment, MoI (handling/tempo), agility (speed = 1/MoI), authority (impact),
    reach, blade_presence, and the three defense-mode affinities {parry, dodge, wind} from geometry + dynamics.

CALIBRATION DISCIPLINE (spec §4, §9): the derived quantities are scaled to REPRODUCE the validated orderings the
engine was tuned against (so balance is preserved), and the continuous physics then refines on top. Where the
derivation DISAGREES with a hand-authored value, that is a top-down error surfaced — see __main__ (e.g. the staff
is light and centre-balanced, so it derives FAST, while the hand-set spd=0.0 called it slow).
"""
import math


# physical constants / calibration (spec §4; the K's are sim-calibrated, [RE-VERIFY] at wiring)
HANDS2_REACH = 0.8        # two-handed extension added to reach (the eff_head 2H bonus)
MOI_LEN = 'head_len'      # the lever arm for MoI about the hand is the forward (blade) length
AUTH_MASS_EXP = 0.5       # impact momentum ~ sqrt(mass) (kinetic; matches core.p_auth's sqrt-mass)


def derive(w, geom=None):
    """Derive the combat dynamics of one weapon from its primitives. `w` is a WEAPONS entry; `geom` is its
    GEOMETRY entry (raw geometric primitives — needed for the defense affinities). Pure; returns a dict."""
    geom = geom or {}
    mass = w.get('mass', 1.0)
    pob = w.get('pob_frac', 0.15)              # forward-balance fraction (0 = at the hand, ->1 = at the tip)
    head_len = w.get('head_len', 2.0)
    grip_len = w.get('grip_len', 0.8)
    hands = w.get('hands', 1)
    total_len = head_len + grip_len

    # ---- mass distribution -> handling (documented physics) ----
    static_moment = mass * pob                                  # forward torque: "wants to continue" (recoverability basis)
    MoI = mass * pob * head_len                                 # rotational inertia about the hand -> handling/tempo

    # ---- speed: a high-MoI weapon is slow to bring to bear. agility in (0,1] ----
    agility = 1.0 / (1.0 + MoI)                                 # rapier/dagger ~ high; spear/poleaxe ~ low

    # ---- impact authority: forward momentum (sqrt-mass x forwardness). Head-specific DELIVERY stays in coupling. ----
    authority = (mass ** AUTH_MASS_EXP) * (0.30 + pob)         # cut/thrust/blunt all scale with this; perc_conc multiplies blunt

    # ---- reach: effective forward length + 2H extension (replaces reach=='long' + HEAD_REACH[head]) ----
    reach = head_len + (HANDS2_REACH if hands == 2 else 0.0) + w.get('reach_adj', 0.0)

    # ---- blade presence: how tip-forward the mass sits (predicts the measured blade-weight ratio) ----
    blade_presence = pob                                        # the measured forward-balance IS the presence proxy

    # ---- defense-mode affinities (the GATE replacement) — DERIVED from geometry + dynamics ----
    cross_section = geom.get('cross_section', 0.6)              # rigidity (whippy 0 -> rigid 1)
    rigidity = 0.30 + 0.70 * cross_section
    hand_guard = w.get('hand_guard', 0.4)
    blade_guard = w.get('blade_guard', 0.4)
    lever_norm = MoI / (1.0 + MoI)                             # bind-leverage in (0,1): heavy/forward dominates the bind
    onehand = 1.0 if hands == 1 else 0.78                       # a one-handed weapon voids more freely (footwork)

    # WIND: meet + dominate the bind — blade-catching utility x rigidity x bind-leverage (edge length via head_len).
    wind = blade_guard * rigidity * (0.45 + 0.55 * lever_norm) * (0.7 + 0.3 * min(1.0, head_len / 3.0))
    # DODGE: void with footwork — lightness (agility) x handedness. A heavy two-hander roots you.
    dodge = agility * onehand
    # PARRY: deflect with the weapon — a guarded hand commits the parry safely; a handy weapon parries fast.
    parry = (0.45 + 0.55 * hand_guard) * (0.55 + 0.45 * agility / 0.6 if agility < 0.6 else 1.0)

    # normalise the three affinities into the old GATE's ~[0.4,1.0] band (calibrate-to-reproduce, then refine)
    def _band(x, lo, hi):
        return round(0.4 + 0.6 * max(0.0, min(1.0, (x - lo) / (hi - lo))), 2)

    return dict(
        total_len=round(total_len, 2), static_moment=round(static_moment, 3), MoI=round(MoI, 3),
        agility=round(agility, 3), authority=round(authority, 3), reach=round(reach, 2),
        blade_presence=round(blade_presence, 3),
        parry=_band(parry, 0.55, 1.0), dodge=_band(dodge, 0.2, 0.95), wind=_band(wind, 0.08, 0.5),
    )


if __name__ == '__main__':
    import sys
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    from combatant import WEAPONS, GEOMETRY

    rows = {n: derive(w, GEOMETRY.get(n)) for n, w in WEAPONS.items()}

    print("DERIVED weapon dynamics (from primitives — no hand-authored spd/wt/HEFT/GATE):")
    print(f"{'weapon':12} {'MoI':>6} {'agility':>7} {'authority':>9} {'reach':>6} | {'spd(hand)':>9} {'wt(hand)':>8}")
    for n in sorted(rows, key=lambda k: rows[k]['MoI']):
        d = rows[n]
        print(f"  {n:10} {d['MoI']:6.2f} {d['agility']:7.3f} {d['authority']:9.3f} {d['reach']:6.2f} | "
              f"{WEAPONS[n].get('spd', 0):9} {WEAPONS[n].get('wt', '?'):>8}")

    print("\nDERIVED defense affinities vs the hand-authored GATE (does the derivation reproduce the ordering?):")
    GATE = {  # the current hand table, for comparison only
        'rapier': {'parry': 1.0, 'dodge': 0.8, 'wind': 0.4}, 'arming': {'parry': 0.9, 'dodge': 0.8, 'wind': 0.7},
        'longsword': {'parry': 0.9, 'dodge': 0.7, 'wind': 1.0}, 'greatsword': {'parry': 0.7, 'dodge': 0.6, 'wind': 0.9},
        'sabre': {'parry': 0.9, 'dodge': 0.9, 'wind': 0.6}, 'dagger': {'parry': 0.6, 'dodge': 0.9, 'wind': 0.5},
        'paired_short': {'parry': 1.0, 'dodge': 0.9, 'wind': 0.4}, 'spear': {'parry': 0.8, 'dodge': 0.9, 'wind': 0.8},
        'staff': {'parry': 0.9, 'dodge': 0.8, 'wind': 0.8}, 'mace': {'parry': 0.7, 'dodge': 0.7, 'wind': 0.7},
        'poleaxe': {'parry': 0.8, 'dodge': 0.5, 'wind': 1.0}, 'longsword_halfsword': {'parry': 1.0, 'dodge': 0.5, 'wind': 1.0},
    }
    print(f"{'weapon':12} {'parry der/hand':>16} {'dodge der/hand':>16} {'wind der/hand':>16}")
    for n in sorted(rows):
        d = rows[n]; g = GATE[n]
        print(f"  {n:10} {d['parry']:6.2f}/{g['parry']:<4}      {d['dodge']:6.2f}/{g['dodge']:<4}      {d['wind']:6.2f}/{g['wind']:<4}")

    # validation (recreates the deleted stress harness): monotonicity + boundedness
    print("\nVALIDATION:")
    ag = [(n, rows[n]['agility']) for n in rows]
    print(f"  agility bounded (0,1]:  {all(0 < a <= 1 for _, a in ag)}")
    print(f"  fastest -> slowest:     {' > '.join(n for n, _ in sorted(ag, key=lambda x: -x[1]))}")
    moi = sorted(rows.items(), key=lambda kv: kv[1]['MoI'])
    print(f"  lightest-handling:      {moi[0][0]} (MoI {moi[0][1]['MoI']})   heaviest: {moi[-1][0]} (MoI {moi[-1][1]['MoI']})")
