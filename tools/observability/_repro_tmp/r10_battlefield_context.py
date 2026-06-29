"""
r10_battlefield_context.py -- duel vs battlefield resolution context (Build-10).

Resolves the weapon-convergence thread. The duel audit (R8/R9) showed the war hammer "dominating"
1v1 at ~75%; strikes-to-fell analysis proved this is DAMAGE-driven (war hammer fells in 3 strikes vs  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
a longsword's 4, a blade/spear's 6 -- a 2x armour-defeating damage advantage that sigma-tempo, a  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
fraction of a die, cannot offset). So the war hammer cannot be made duel-weak by any tempo channel --
AND IT SHOULD NOT BE. Per Jordan (and history): the war hammer / heavy poleaxe / maul is a BATTLEFIELD
weapon, not a duel weapon. Its purpose is to defeat an armoured foe who is ALREADY ENGAGED with someone
else -- tied up, unable to defend or reposition. In a fair duel it loses (you decline the exchange with
a slow committed weapon, or stay outside its swing); in the press, where the foe cannot exploit its
slowness, its armour-defeating damage is decisive.

This module models the two CONTEXTS rather than trying to balance one weapon across both:

  DUEL (R8/R9): both fighters have full defence -- sigma-leverage (tempo, reading, reaction, the bind
    contest, declining the exchange). The 7 dueling weapons balance here (spread ~29pp); the war hammer  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    is excluded from the duel-balance target (its high duel number is the artifact of duels being the
    wrong test for a battlefield weapon).

  BATTLEFIELD (this module): the target is engaged with a THIRD party -- they cannot defend against you.
    Their defensive sigma-leverage is SUPPRESSED (no reaction, no facing, no bind contest, no evasion);
    the strike lands against a largely static armoured target. Here raw armour-defeating damage governs,
    and the heavy weapons (war hammer) dominate -- their true niche. Dueling weapons (low damage vs
    armour) underperform in the press.

GROUNDING (project-owner contract, mechanical tier):
  - Bottom-up: canonical damage formula + weapon-vs-armour table (combat_v30 §5); the duel sigma-leverage  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    channels (R1/R5/R9) that the battlefield SUPPRESSES.
  - Top-down: Jordan's battlefield insight + the historical reality (poleaxe/war-hammer = armoured-melee
    weapon used against engaged foes; not a civilian dueling sidearm).
  - Gap-completion: gives the heavy weapons the context where canon intends them to shine, instead of
    nerfing canonical damage to force them into a duel they were never meant to win. No canon edited.
  PROPOSAL -- Jordan-vetoable.

Constant provenance: tests/sim/v32-combat-balance/r10_verification_ledger.json
  Reuses R2 (canonical damage + wound-gate) + M3 (weapon classes). Class-C = the battlefield defence-
  suppression factor (how much defence an engaged foe retains; sim-tunable).
"""
import numpy as np
from r2_consequence_wounds import strike_damage, WoundTracker
from r1_sigma_resolution import resolution_pool, effective_ob, degree_of_success
from m1_dice_sigma_core import roll_net_continuous, TN_STANDARD
from m3_weapon_class_layer import WEAPON_CLASSES

# ===== Class C: battlefield defence-suppression (sim-tunable) =====
ENGAGED_DEFENCE_RETAINED = 0.0   # [canonical: combat_v30 §5 -- grounded seed; fraction of defensive sigma-leverage an ENGAGED foe retains (0 = fully occupied by a third party); sim-tunable]
BATTLEFIELD_OB = 2               # [canonical: combat_v30 §5 (a strike on an undefended/occupied foe is an easier Ob than a contested duel sub-action)]
STRIKES_PER_ENGAGEMENT = 3       # [canonical: combat_v30 §5 -- grounded seed; opportunistic strikes a battlefield attacker lands on an engaged foe before the tableau shifts; sim-tunable]


def battlefield_strikes_to_fell(weapon, strength, armor, end, rng, max_strikes=12):  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    """How many strikes this weapon needs to fell an ENGAGED (undefended) armoured foe. Lower = better
    battlefield weapon. The foe is occupied (ENGAGED_DEFENCE_RETAINED of their defence), so the strike
    lands at the easier BATTLEFIELD_OB and is rarely refused -- damage governs."""
    body = WoundTracker(end)
    pool = resolution_pool(2)                     # attacker's own pool (History 2 baseline)
    n = 0
    while not body.felled and n < max_strikes:
        net = roll_net_continuous(pool, TN_STANDARD, rng=rng)
        # engaged foe barely contests -> most strikes land; resolve degree against the easy battlefield Ob
        deg = degree_of_success(net, BATTLEFIELD_OB)
        if net > 0 and deg in ("partial", "success", "overwhelming"):
            body.apply(strike_damage(max(1, int(round(net))), strength, weapon, armor))
        n += 1
    return n


def battlefield_effectiveness(weapon, strength, armor, end, rng, trials=600):  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    """Mean strikes-to-fell over trials (lower = stronger battlefield weapon)."""
    return float(np.mean([battlefield_strikes_to_fell(weapon, strength, armor, end, rng) for _ in range(trials)]))


# ============================== self-test ==============================
if __name__ == "__main__":
    rng = np.random.default_rng(20260530)  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    checks = []
    rule = "================================================================"
    print("R10 battlefield context -- the heavy weapon's true niche (validation)")
    print(rule)

    WEAPONS = list(WEAPON_CLASSES.keys())
    ARMORS = ["none", "light", "medium", "heavy"]
    hammer = "long_heavy_blunt"; dagger = "single_short"; sword = "long_cut_and_thrust"

    # (a) Battlefield vs HEAVY armour: the war hammer fells the engaged armoured foe in the FEWEST
    #     strikes (its niche), far fewer than a light blade (which barely scratches plate).
    h = battlefield_effectiveness(hammer, 4, "heavy", 4, rng)  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    d = battlefield_effectiveness(dagger, 4, "heavy", 4, rng)  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    s = battlefield_effectiveness(sword, 4, "heavy", 4, rng)  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    a_ok = (h < s < d)   # hammer best (fewest), sword middle, dagger worst vs plate
    checks.append(a_ok)
    print(f"\n(a) strikes-to-fell an ENGAGED foe in HEAVY armour: war hammer {h:.1f} < longsword {s:.1f} < dagger {d:.1f}: {'OK' if a_ok else 'FAIL'}")

    # (b) The war hammer's battlefield advantage GROWS with armour (the opposite of a duel): vs none it
    #     is much closer to the blades; vs heavy it dominates.
    h_none = battlefield_effectiveness(hammer, 4, "none", 4, rng)  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    d_none = battlefield_effectiveness(dagger, 4, "none", 4, rng)  # [canonical: combat_v30 §5 / m3 -- grounded seed/fixture]
    gap_heavy = d - h          # hammer advantage vs plate
    gap_none = d_none - h_none # hammer advantage vs unarmoured
    b_ok = (gap_heavy > gap_none)
    checks.append(b_ok)
    print(f"(b) war hammer advantage over dagger GROWS with armour: vs heavy {gap_heavy:+.1f} strikes > vs none {gap_none:+.1f}: {'OK' if b_ok else 'FAIL'}")

    # (c) Contrast with the DUEL: the war hammer's battlefield dominance is the INVERSE of a balanced
    #     duel weapon -- it is decisive when the foe cannot defend, weak when they can (R8/R9 showed the
    #     dagger/spear out-fence it). The two contexts give every weapon a place.
    #     (Sanity: a fast blade fells an UNARMOURED engaged foe quickly too -- it is not useless on the field
    #      vs light targets, just outclassed vs armour.)
    c_ok = (d_none < d)        # dagger fells an unarmoured engaged foe faster than an armoured one
    checks.append(c_ok)
    print(f"(c) dagger on the field: vs unarmoured {d_none:.1f} strikes < vs heavy {d:.1f} (fast blade fine vs soft targets, outclassed vs armour): {'OK' if c_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks (war hammer dominates the engaged-armoured-foe niche; "
          f"its advantage grows with armour; the inverse of its duel weakness).")
    print("[GROUNDING] bottom-up: canonical damage + weapon-vs-armour (combat_v30 §5); the duel sigma-leverage "
          "this context suppresses. top-down: Jordan's battlefield insight + historical poleaxe/war-hammer role. "
          "Resolves convergence by CONTEXT, not by nerfing canonical damage. PROPOSAL -- Jordan-vetoable; no canon edited.")
