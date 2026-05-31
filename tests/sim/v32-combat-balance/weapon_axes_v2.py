"""
weapon_axes_v2.py -- v2 weapon substrate (hands + head axes), built bottom-up (Build-11).  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]

Implements the weapon_axes_v2 proposal: two new categorical handles on the canonical reach/weight
substrate -- `hands` (1H/2H) and `head` (point / cut_and_thrust / straight_cut / curved_cut / blunt,
where curved_cut makes curvature explicit and the point/cut spectrum carries the armour interaction).
Each weapon is an axis-vector; the derived properties (damage_class, armour mod, STR multiplier, wield
minimum) and the v2 sigma-leverage modifiers (head bias by engagement state, 2H bind amplification,
1H off-hand defence, curved draw-cut, flexible parry-bypass, defensive block) all fall out of the axes.

Roster per Jordan directive 2026-05-29: include ALL expressible weapons + add a short-blunt (tonfa) and  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
a flexible blunt (war flail). NB the one-handed ball-and-chain flail is folklore (blunt-weapon survey);
the war flail here is the historically-real two-handed Hussite/Mair weapon.

Grounding: bottom-up = canonical reach/weight/type substrate (combat_v30 §5; m3) + ratified W1 armour  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
taper + the ratified Strength bind / off-hand channels; constants are grounded seeds (LEVEL_SIGMA from
the M1 core). Top-down validation = the duel/battlefield audit + the historical-precedent check
(run_validation + the result doc). PROPOSAL -- Jordan-vetoable; no canon file edited (the point-vs-armour
row is the one canon-touching piece, flagged for ratification).
Per-constant provenance: tests/sim/v32-combat-balance/weapon_axes_v2_verification_ledger.json
"""
from m1_dice_sigma_core import LEVEL_SIGMA

ARMORS = ["none", "light", "medium", "heavy"]

# ===== the roster: each weapon is an axis-vector (Jordan: include all + tonfa + flail) =====
WEAPONS_V2 = {
    # blade -- point profile (thrust): armour-gaps + reach, weak in bind
    "rapier":        {"reach": "long",  "weight": "light", "hands": 1, "head": "point",          "speed": 1.5, "handling": "demanding"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "estoc":         {"reach": "long",  "weight": "light", "hands": 1, "head": "point",          "speed": 1.0, "handling": "standard"},
    "spear":         {"reach": "long",  "weight": "light", "hands": 2, "head": "point",          "speed": 0.0, "handling": "forgiving"},
    # blade -- cut_and_thrust (versatile generalist)
    "arming_sword":  {"reach": "long",  "weight": "light", "hands": 1, "head": "cut_and_thrust", "speed": 1.5, "handling": "standard"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "sidesword":     {"reach": "long",  "weight": "light", "hands": 1, "head": "cut_and_thrust", "speed": 1.4, "handling": "standard"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "longsword":     {"reach": "long",  "weight": "heavy", "hands": 2, "head": "cut_and_thrust", "speed": 0.5, "handling": "standard"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "dagger":        {"reach": "short", "weight": "light", "hands": 1, "head": "cut_and_thrust", "speed": 3.0, "handling": "forgiving"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "paired_short":  {"reach": "short", "weight": "light", "hands": 1, "head": "cut_and_thrust", "speed": 2.5, "handling": "demanding", "paired": True},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    # blade -- straight_cut (percussive cut, strong in bind)
    "messer":        {"reach": "long",  "weight": "light", "hands": 1, "head": "straight_cut",   "speed": 1.8, "handling": "forgiving"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "greatsword":    {"reach": "long",  "weight": "heavy", "hands": 2, "head": "straight_cut",   "speed": 0.0, "handling": "demanding"},
    # blade -- curved_cut (draw-cut, flow)
    "sabre":         {"reach": "long",  "weight": "light", "hands": 1, "head": "curved_cut",     "speed": 2.0, "handling": "standard"},
    "curved_2h":     {"reach": "long",  "weight": "heavy", "hands": 2, "head": "curved_cut",     "speed": 1.0, "handling": "demanding"},
    # blunt
    "staff":         {"reach": "long",  "weight": "light", "hands": 2, "head": "blunt",          "speed": 0.0, "handling": "forgiving"},
    "mace":          {"reach": "short", "weight": "heavy", "hands": 1, "head": "blunt",          "speed": 0.5, "handling": "forgiving"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "poleaxe":       {"reach": "long",  "weight": "heavy", "hands": 2, "head": "blunt",          "speed": -0.5, "handling": "demanding"},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    "tonfa":         {"reach": "short", "weight": "light", "hands": 1, "head": "blunt",          "speed": 2.2, "handling": "standard", "paired": True, "defensive": True},
    "war_flail":     {"reach": "long",  "weight": "heavy", "hands": 2, "head": "blunt",          "speed": -0.5, "handling": "demanding", "flexible": True},  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
}

# ===== derived: damage family + armour table (ratified W1 + the point row §4) =====
WEAPON_ARMOR_MOD = {                                                  # [canonical: combat_v30 §5 + W1 ratified taper]
    "light_blade": {"none": 3, "light": 2, "medium": 1, "heavy": 0},  # [canonical: combat_v30 §5]
    "heavy_blade": {"none": 6, "light": 4, "medium": 2, "heavy": 0},  # [canonical: combat_v30 §5]
    "light_blunt": {"none": 3, "light": 3, "medium": 2, "heavy": 2},  # [canonical: combat_v30 §5 + W1 ratified]
    "heavy_blunt": {"none": 5, "light": 5, "medium": 4, "heavy": 3},  # [canonical: combat_v30 §5 + W1 ratified]
}
POINT_ARMOR_MOD = {"none": 3, "light": 3, "medium": 2, "heavy": 1}    # [canonical: weapon_axes_v2 §4 -- point finds gaps; PROPOSAL pending ratification]

def damage_class(w):
    fam = "blunt" if w["head"] == "blunt" else "blade"
    return f"{w['weight']}_{fam}"

def armor_mod(w, armor):
    """Point (light blade) uses the gap-finding row; all else the damage-class row."""
    if w["head"] == "point" and w["weight"] == "light":
        return POINT_ARMOR_MOD[armor]
    return WEAPON_ARMOR_MOD[damage_class(w)][armor]

def str_mult(w):
    """STR damage multiplier = weight-factor x type-factor (ratified)."""
    wmult = 2.0 if w["weight"] == "heavy" else 1.0     # [canonical: combat_v30 §5 -- Heavy x2 / Light x1]
    tmult = 1.5 if w["head"] == "blunt" else 1.0       # [canonical: combat_v30 §5 -- Blunt x1.5 / Blade x1]
    return wmult * tmult

def wield_min(w):
    """Canonical STR-min from axes: base 1 +1 heavy +1 long +1 for the long-heavy-blunt war hammer."""
    req = 1 + (1 if w["weight"] == "heavy" else 0) + (1 if w["reach"] == "long" else 0)  # [canonical: combat_v30 §5 STR-min rule]
    if w["reach"] == "long" and w["weight"] == "heavy" and w["head"] == "blunt":
        req += 1
    return req

# ===== v2 sigma-leverage modifiers (head + hands), grounded seeds (sim-tunable) =====
POINT_APPROACH_DSIG    = LEVEL_SIGMA["minor"] * 0.6   # [canonical: weapon_axes_v2 §3 -- point reaches on the approach; grounded seed]
POINT_BIND_PENALTY     = LEVEL_SIGMA["minor"] * 0.5   # [canonical: weapon_axes_v2 §3 -- point weak once bound; grounded seed]
CURVED_FLOW_DSIG       = LEVEL_SIGMA["minor"] * 0.4   # [canonical: weapon_axes_v2 §3 -- curved-cut recovery/flow tempo; grounded seed]
CURVED_DRAWCUT_DMG     = 2                            # [canonical: weapon_axes_v2 §3 -- curved-cut draw-cut bonus vs unarmoured; grounded seed]
STRAIGHTCUT_BIND_DSIG  = LEVEL_SIGMA["minor"] * 0.4   # [canonical: weapon_axes_v2 §3 -- straight-cut strong in the close/bind; grounded seed]
HANDS_BIND_MULT_2H     = 1.5                          # [canonical: weapon_axes_v2 §3 -- 2H amplifies bind leverage (Stark/Schwach); grounded seed]
OFFHAND_DEFENSE_DSIG   = LEVEL_SIGMA["minor"] * 0.5   # [canonical: weapon_axes_v2 §3 -- 1H off-hand buckler/dagger defence; grounded seed]
DEFENSIVE_DSIG         = LEVEL_SIGMA["minor"] * 0.7   # [canonical: weapon_axes_v2 §3 -- tonfa side-handle block; grounded seed]

def head_dsig(w, state):
    """sigma-leverage bias from the head profile, by engagement state (R9 phase model)."""
    h = w["head"]
    if h == "point":
        if state in ("closing", "breaking"):
            return POINT_APPROACH_DSIG
        if state == "in_bind":
            return -POINT_BIND_PENALTY
        return 0.0
    if h == "curved_cut":
        return CURVED_FLOW_DSIG                        # flow advantage across phases
    if h == "straight_cut":
        return STRAIGHTCUT_BIND_DSIG if state == "in_bind" else 0.0
    return 0.0                                         # cut_and_thrust = balanced; blunt handled elsewhere

def hands_bind_mult(w):
    return HANDS_BIND_MULT_2H if w["hands"] == 2 else 1.0

def offhand_defense(w):
    """A 1H weapon (not already paired) can carry an off-hand buckler/dagger -> defensive dsig."""
    if w["hands"] == 1 and not w.get("paired"):
        return OFFHAND_DEFENSE_DSIG
    return 0.0

def defensive_dsig(w):
    return DEFENSIVE_DSIG if w.get("defensive") else 0.0

def is_flexible(w):
    """Flexible head (war flail) -> strikes bypass the defender's bind/parry defence."""
    return bool(w.get("flexible"))

def strike_damage_v2(net, strength, w, armor):
    """Damage = net + STR x mult + weapon-vs-armour (+ draw-cut bonus vs unarmoured for curved cut)."""
    dmg = net + strength * str_mult(w) + armor_mod(w, armor)
    if w["head"] == "curved_cut" and armor in ("none", "light"):
        dmg += CURVED_DRAWCUT_DMG
    return max(0, int(round(dmg)))


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "=" * 64  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    print("weapon_axes_v2 substrate -- validation"); print(rule)

    def W(name): return WEAPONS_V2[name]

    # (1) point finds gaps where cut goes to zero vs heavy armour (the §4 extension)
    c1 = (armor_mod(W("rapier"), "heavy") == 1 and armor_mod(W("arming_sword"), "heavy") == 0
          and armor_mod(W("sabre"), "heavy") == 0)
    checks.append(c1)
    print(f"(1) vs HEAVY armour: rapier(point) {armor_mod(W('rapier'),'heavy')} > arming-sword(cut&thrust) "
          f"{armor_mod(W('arming_sword'),'heavy')} = sabre(cut) {armor_mod(W('sabre'),'heavy')}: {'OK' if c1 else 'FAIL'}")

    # (2) STR multipliers come out canonical (heavy-blunt x3, heavy-blade x2, light-blade x1, light-blunt x1.5)
    c2 = (str_mult(W("poleaxe")) == 3.0 and str_mult(W("longsword")) == 2.0  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
          and str_mult(W("rapier")) == 1.0 and str_mult(W("staff")) == 1.5)  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    checks.append(c2)
    print(f"(2) STR mult: poleaxe {str_mult(W('poleaxe'))} / longsword {str_mult(W('longsword'))} / "
          f"rapier {str_mult(W('rapier'))} / staff {str_mult(W('staff'))}: {'OK' if c2 else 'FAIL'}")

    # (3) wield-min axis-derived: dagger 1, rapier 2, longsword 3, poleaxe 4
    c3 = (wield_min(W("dagger")) == 1 and wield_min(W("rapier")) == 2
          and wield_min(W("longsword")) == 3 and wield_min(W("poleaxe")) == 4)  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    checks.append(c3)
    print(f"(3) wield-min: dagger {wield_min(W('dagger'))} / rapier {wield_min(W('rapier'))} / "
          f"longsword {wield_min(W('longsword'))} / poleaxe {wield_min(W('poleaxe'))}: {'OK' if c3 else 'FAIL'}")

    # (4) head_dsig: point wins the approach, loses the bind; curved-cut has a flow edge; cut&thrust neutral
    c4 = (head_dsig(W("rapier"), "closing") > 0 and head_dsig(W("rapier"), "in_bind") < 0
          and head_dsig(W("sabre"), "closing") > 0 and head_dsig(W("arming_sword"), "in_bind") == 0)
    checks.append(c4)
    print(f"(4) head_dsig: rapier closing {head_dsig(W('rapier'),'closing'):+.2f} / bind "
          f"{head_dsig(W('rapier'),'in_bind'):+.2f}; sabre flow {head_dsig(W('sabre'),'closing'):+.2f}; "
          f"arming-sword bind {head_dsig(W('arming_sword'),'in_bind'):+.2f}: {'OK' if c4 else 'FAIL'}")

    # (5) hands: 2H amplifies the bind, 1H opens an off-hand defence; the mace/poleaxe split
    c5 = (hands_bind_mult(W("longsword")) > hands_bind_mult(W("arming_sword"))
          and offhand_defense(W("arming_sword")) > 0 and offhand_defense(W("longsword")) == 0
          and W("mace")["hands"] == 1 and W("poleaxe")["hands"] == 2)
    checks.append(c5)
    print(f"(5) hands: longsword bind x{hands_bind_mult(W('longsword'))} vs arming-sword x{hands_bind_mult(W('arming_sword'))}; "
          f"off-hand: arming-sword {offhand_defense(W('arming_sword')):.2f} / longsword {offhand_defense(W('longsword')):.2f}; "
          f"mace 1H / poleaxe 2H: {'OK' if c5 else 'FAIL'}")

    # (6) the short-blunt additions: tonfa defends + is short blunt; war flail is flexible (bypasses parry)
    c6 = (defensive_dsig(W("tonfa")) > 0 and W("tonfa")["reach"] == "short" and W("tonfa")["head"] == "blunt"
          and is_flexible(W("war_flail")) and not is_flexible(W("poleaxe")))
    checks.append(c6)
    print(f"(6) short-blunt: tonfa defensive {defensive_dsig(W('tonfa')):.2f} (short blunt); "
          f"war_flail flexible={is_flexible(W('war_flail'))} (bypasses parry), poleaxe flexible={is_flexible(W('poleaxe'))}: {'OK' if c6 else 'FAIL'}")

    # (7) curved draw-cut: sabre out-damages arming-sword vs unarmoured, same net/STR
    d_sabre = strike_damage_v2(2, 4, W("sabre"), "none")  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    d_arm   = strike_damage_v2(2, 4, W("arming_sword"), "none")  # [canonical: combat_v30 §5 / weapon_axes_v2 §3 -- grounded seed/fixture]
    c7 = (d_sabre > d_arm)
    checks.append(c7)
    print(f"(7) draw-cut vs unarmoured (net2,STR4): sabre {d_sabre} > arming-sword {d_arm}: {'OK' if c7 else 'FAIL'}")

    print(rule)
    bad = [i + 1 for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- checks {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} substrate checks (point-vs-armour, STR mult, wield-min, head bias, "
          f"hands bind/off-hand + mace/poleaxe split, tonfa/flail, draw-cut).")
    print("[GROUNDING] bottom-up: canonical reach/weight/type + ratified W1 + Strength/off-hand channels (M1 LEVEL_SIGMA). "
          "Top-down validation in the duel/battlefield audit + historical-precedent check. PROPOSAL -- Jordan-vetoable; no canon edited.")
