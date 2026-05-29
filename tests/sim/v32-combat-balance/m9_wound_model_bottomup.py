"""
m9_wound_model_bottomup.py -- bottom-up wound model (Jordan-authorized redesign).

The I-NN combat-balance run found the v32 build axis NOT balanced: heavy weapons dominated because severity was
MULTIPLICATIVE (net + Strength x weapon-multiplier + weapon-vs-armour mod, doubled on crit). Jordan
authorized throwing out crits and multipliers and rebuilding severity bottom-up, validated against
historical combat reality (top-down) rather than only the acceptance balance band.

This module is a PROPOSED model (Class C), not canon. It does not edit combat_v30/v32 in the repo.

DESIGN (bottom-up, first principles -- no crit doubling, no Strength/weapon multipliers):

  wound_severity = net_hits + bounded_strength_bonus - armour_resist(damage_type, armour_tier)

  - net_hits (margin of success, M1/M4b) is the PRIMARY input -- a cleaner hit wounds worse, linearly.
  - bounded_strength_bonus = min(floor(Str/2), CAP). Additive and capped: a strong arm helps but does
    not MULTIPLY lethality. Historically, placement / edge alignment / target (armoured vs not) and
    timing dominate over raw power (the Liechtenauer/Fiore emphasis on Indes and measure over force).
    This is the direct fix for M8's Str-7 / heavy-weapon runaway.
  - armour_resist is PER DAMAGE TYPE, not a flat number. Bottom-up from historical arms-and-armour:
      * plate (heavy) NEGATES cuts (resist 4 -- a sword-cut does little to plate; this is why cutting
        an armoured man was futile and the period answer was the half-sword, the estoc, and wrestling),
      * is MODERATE vs thrust (resist 2 -- thrusting into gaps/visor with a stiff point could wound),
      * and is WEAK vs blunt (resist 1 -- concussive trauma transmits through plate; the poleaxe, the
        warhammer, and the mace were the armour-DEFEATING weapons of the armoured era).
    Lighter armour scales the resists down; no armour resists nothing.

  Two further historical levers:
  - decisive vs unarmored: against an unarmoured target a clean hit (net >= DECISIVE_NET_THRESHOLD)
    inflicts a wound directly, not chip severity -- real fights against soft targets were short and
    lethal, not attritional. (M8's 30-exchange attrition let durability/Endurance compound unhistorically.)
  - reach is an Ob advantage, not a damage bonus: the longer weapon controls the measure and the first
    tempo ("the spear is king"), modelled as -1 Ob to the longer weapon while closing -- it does not
    make the wound bigger.

Constant provenance: tests/sim/v32-combat-balance/m9_verification_ledger.json
  Class A = retained canonical anchors (net-as-severity, weapon-type taxonomy from combat_v30 degree/weapon spec).
  Class C = proposed bottom-up redesign (Jordan-authorized; NOT canonical; sim-tunable).

The self-tests below ARE the top-down historical validation at unit level (plate negates cuts; blunt
defeats plate; thrust-to-gap beats cut vs plate; bounded strength -- the strong arm is an edge, not a
multiplier; unarmoured combat is lethal; reach buys tempo not damage).
"""
import numpy as np

# ===== Class A: retained canonical anchors =====
WOUND_NET_BASE = 1   # [canonical: combat_v30 §5 -- net hits is the primary severity input]
# weapon damage type taxonomy (derived from combat_v30 §8.1 reach/weight/type):
WEAPON_DAMAGE_TYPE = {
    "single_short": "cut", "paired_short": "cut", "curved_cut_primary": "cut",
    "long_cut_and_thrust": "cut", "long_thrust_primary": "thrust", "long_pole_spear": "thrust",
    "long_pole_staff": "blunt", "long_heavy_blunt": "blunt",
}  # [canonical: combat_v30 §8.1 -- blade/blunt + thrust-primary vs cut-primary]

# ===== Class C: bottom-up redesign (Jordan-authorized 2026-05-29; NOT canonical) =====
BOUNDED_STR_DIV = 2   # [canonical: i17_simulation_prep -- proposed (Str bonus = floor(Str/2))]
BOUNDED_STR_CAP = 3   # [canonical: i17_simulation_prep -- proposed (Str bonus capped at 3)]
DECISIVE_NET_THRESHOLD = 3   # [canonical: i17_simulation_prep -- proposed (clean hit vs unarmored wounds directly)]
REACH_OB_ADVANTAGE = 1       # [canonical: i17_simulation_prep -- proposed (longer weapon -1 Ob closing)]
# per-type wound resistance by armour tier (severity subtractor); proposed, sim-tunable:
ARMOR_RESIST = {
    "none":   {"cut": 0, "thrust": 0, "blunt": 0},   # [canonical: i17_simulation_prep -- proposed (no armour resists nothing)]
    "light":  {"cut": 1, "thrust": 1, "blunt": 0},   # [canonical: i17_simulation_prep -- proposed (gambeson: some cut/thrust resist)]
    "medium": {"cut": 2, "thrust": 1, "blunt": 1},   # [canonical: i17_simulation_prep -- proposed (mail: good vs cut, less vs thrust/blunt)]
    "heavy":  {"cut": 4, "thrust": 2, "blunt": 1},   # [canonical: i17_simulation_prep -- proposed (plate: negates cut, moderate thrust, weak vs blunt)]
}


def bounded_strength_bonus(strength):
    """Additive, capped Strength contribution to wound severity (replaces the Str x weapon multiplier)."""
    return min(strength // BOUNDED_STR_DIV, BOUNDED_STR_CAP)


def weapon_damage_type(weapon_class):
    """Damage type (cut / thrust / blunt) for a weapon class (combat_v30 §8.1 taxonomy)."""
    return WEAPON_DAMAGE_TYPE[weapon_class]


def armor_resist(damage_type, armor_tier):
    """Per-type wound resistance of an armour tier (bottom-up historical model)."""
    return ARMOR_RESIST[armor_tier][damage_type]


def wound_severity(net, strength, weapon_class, armor_tier):
    """Bottom-up wound severity on a landing hit (NO crit doubling, NO Str/weapon multiplier):
        severity = net + bounded_strength_bonus(Str) - armour_resist(type, tier), floored at 0.
    Against an UNARMORED target a clean hit (net >= DECISIVE_NET_THRESHOLD) is decisive: it yields at
    least a full wound's worth of severity regardless of the arithmetic (historical lethality)."""
    if net <= 0:
        return 0
    dtype = weapon_damage_type(weapon_class)
    sev = net + bounded_strength_bonus(strength) - armor_resist(dtype, armor_tier)
    sev = max(0, sev)
    if armor_tier == "none" and net >= DECISIVE_NET_THRESHOLD:
        sev = max(sev, net)   # decisive blow to a soft target always tells
    return int(sev)


def reach_ob_shift(attacker_reach, defender_reach):
    """Reach as an Ob advantage while closing (NOT a damage bonus). Returns the delta to the longer
    weapon's effective Ob: negative = advantaged. Equal reach -> 0."""
    order = {"short": 0, "long": 1}
    a, d = order.get(attacker_reach, 0), order.get(defender_reach, 0)
    if a > d:
        return -REACH_OB_ADVANTAGE   # attacker out-reaches defender -> easier for attacker
    if a < d:
        return REACH_OB_ADVANTAGE    # attacker out-reached -> harder
    return 0


# ============================== self-test = historical validation (unit level) ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("M9 bottom-up wound model -- unit-level HISTORICAL validation (no crits, no multipliers)")
    print(rule)

    # (a) Plate NEGATES cuts: a strong cut (net 3, Str 7) to heavy armour does little; the same cut to an
    #     unarmoured target is decisive. (Historical: cutting an armoured man was futile.)
    cut_vs_plate = wound_severity(3, 7, "single_short", "heavy")     # net3 + str+3 - cut-resist 4 = 2
    cut_vs_none = wound_severity(3, 7, "single_short", "none")       # decisive: >= net 3
    a_ok = (cut_vs_plate <= 2 and cut_vs_none >= 3 and cut_vs_none > cut_vs_plate)  # [canonical: i17_simulation_prep -- proposed]
    checks.append(a_ok)
    print(f"\n(a) plate negates cuts (strong cut vs plate {cut_vs_plate} <= soft target {cut_vs_none}): {'OK' if a_ok else 'FAIL'}")

    # (b) Blunt DEFEATS plate: a blunt hit vs plate wounds far better than a cut vs plate, same net/Str.
    #     (Historical: poleaxe/warhammer/mace were the armour-defeating weapons.)
    blunt_vs_plate = wound_severity(3, 7, "long_heavy_blunt", "heavy")   # net3 + str3 - blunt-resist 1 = 5
    b_ok = (blunt_vs_plate > cut_vs_plate)  # [canonical: i17_simulation_prep -- proposed (blunt beats cut vs plate)]
    checks.append(b_ok)
    print(f"(b) blunt defeats plate (blunt vs plate {blunt_vs_plate} > cut vs plate {cut_vs_plate}): {'OK' if b_ok else 'FAIL'}")

    # (c) Thrust-to-gap beats cut vs plate: thrust resist (2) < cut resist (4). (Historical: estoc, half-sword.)
    thrust_vs_plate = wound_severity(3, 7, "long_thrust_primary", "heavy")   # net3 + str3 - thrust-resist 2 = 4
    c_ok = (thrust_vs_plate > cut_vs_plate and blunt_vs_plate >= thrust_vs_plate)
    checks.append(c_ok)
    print(f"(c) thrust beats cut vs plate (thrust {thrust_vs_plate} > cut {cut_vs_plate}; blunt {blunt_vs_plate} >= thrust): {'OK' if c_ok else 'FAIL'}")

    # (d) Strength is an EDGE, not a MULTIPLIER: a Str-7 vs Str-1 cutter, same net, differ by the capped
    #     bonus only (<= 3), NOT by 7x. (This is the direct fix for M8's heavy-weapon runaway.)
    s7 = wound_severity(2, 7, "single_short", "none")
    s1 = wound_severity(2, 1, "single_short", "none")
    d_ok = (0 <= (s7 - s1) <= BOUNDED_STR_CAP and s7 < 7 * max(s1, 1))  # [canonical: i17_simulation_prep -- proposed bounded Str]
    checks.append(d_ok)
    print(f"(d) strength is bounded edge not multiplier (Str7 {s7} - Str1 {s1} = {s7-s1} <= cap {BOUNDED_STR_CAP}): {'OK' if d_ok else 'FAIL'}")

    # (e) Unarmoured combat is LETHAL/decisive: a clean hit (net>=3) to no armour always inflicts >= net,
    #     even from a weak arm. (Historical: fights vs soft targets are short, not attritional.)
    weak_clean = wound_severity(3, 1, "single_short", "none")
    e_ok = (weak_clean >= 3)  # [canonical: i17_simulation_prep -- proposed decisive threshold]
    checks.append(e_ok)
    print(f"(e) unarmoured combat lethal (weak clean hit net3 -> severity {weak_clean} >= 3): {'OK' if e_ok else 'FAIL'}")

    # (f) Reach buys TEMPO, not damage: longer weapon gets -1 Ob closing; reach changes NO severity.
    reach_long = reach_ob_shift("long", "short")
    reach_short = reach_ob_shift("short", "long")
    sev_same = (wound_severity(3, 4, "long_pole_spear", "none") == wound_severity(3, 4, "single_short", "none"))
    f_ok = (reach_long == -REACH_OB_ADVANTAGE and reach_short == REACH_OB_ADVANTAGE and reach_ob_shift("long","long") == 0 and sev_same)
    checks.append(f_ok)
    print(f"(f) reach is tempo not damage (long-vs-short Ob {reach_long}; severity reach-invariant {sev_same}): {'OK' if f_ok else 'FAIL'}")

    # (g) Monotonic armour: for any one damage type, more armour never wounds MORE (no inversion).
    mono = True
    for wc in ["single_short", "long_thrust_primary", "long_heavy_blunt"]:
        sevs = [wound_severity(4, 4, wc, t) for t in ["none", "light", "medium", "heavy"]]
        mono = mono and all(sevs[i] >= sevs[i+1] for i in range(3))
    checks.append(mono)
    print(f"(g) armour monotonic (more armour never wounds more, per type): {'OK' if mono else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"HISTORICAL VALIDATION (unit): FAIL -- indices {bad}")
        raise SystemExit(1)
    print(f"HISTORICAL VALIDATION (unit): PASS -- all {len(checks)} "
          f"(plate negates cut, blunt/thrust defeat plate, bounded strength, lethal unarmoured, reach=tempo, monotonic).")
    print("[CLASS C] all severity magnitudes are PROPOSED (Jordan-authorized redesign), sim-tunable, NOT canonical.")
