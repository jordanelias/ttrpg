"""
m3_weapon_class_layer.py -- Module 3 of the v32 combat-balance sim (weapon-class layer).

The weapon layer Modules 1-2 feed into: maps the canonical 3-axis melee matrix
(combat_v30, Class A: base TN, STR multiplier/minimum, weapon-vs-armour damage) onto
the v32 weapon classes (combat_v32_proposal, Class B: handling profiles, Weapon Speed,
sub-action availability).

Constant provenance: tests/sim/v32-combat-balance/m3_verification_ledger.json
  Class A = canonical (combat_v30 §5 Weapon System, §6 Armour).
  Class B = v32 draft sim-seeds (combat_v32_proposal); sim-tunable, NOT canonical.
"""

# ===== Class A: canonical weapon TN axes (combat_v30 §5) =====
WEAPON_BASE_TN = 7        # [canonical: combat_v30 §5 Weapon TN Matrix (Base TN = 7)]
REACH_SHORT_MOD = -1      # [canonical: combat_v30 §5 Weapon TN Matrix (Short -1)]
REACH_LONG_MOD = 0        # [canonical: combat_v30 §5 Weapon TN Matrix (Long +0)]
WEIGHT_LIGHT_MOD = -1     # [canonical: combat_v30 §5 Weapon TN Matrix (Light -1)]
WEIGHT_HEAVY_MOD = 0      # [canonical: combat_v30 §5 Weapon TN Matrix (Heavy +0)]
TYPE_BLADE_MOD = 0        # [canonical: combat_v30 §5 Weapon TN Matrix (Blade +0)]
TYPE_BLUNT_MOD = 1        # [canonical: combat_v30 §5 Weapon TN Matrix (Blunt +1)]
REACH_MOD = {"short": REACH_SHORT_MOD, "long": REACH_LONG_MOD}
WEIGHT_MOD = {"light": WEIGHT_LIGHT_MOD, "heavy": WEIGHT_HEAVY_MOD}
TYPE_MOD = {"blade": TYPE_BLADE_MOD, "blunt": TYPE_BLUNT_MOD}

# ===== Class A: STR multiplier (combat_v30 §5 Damage Resolution) =====
STR_MULT_HEAVY = 2        # [canonical: combat_v30 §5 Damage Resolution (Heavy x2)]
STR_MULT_LIGHT = 1        # [canonical: combat_v30 §5 Damage Resolution (Light x1)]
STR_MULT_BLUNT = 1.5      # [canonical: combat_v30 §5 Damage Resolution (Blunt x1.5; Heavy Blunt x3)]
STR_MULT_BLADE = 1        # [canonical: combat_v30 §5 Damage Resolution (Blade x1)]

# ===== Class A: STR minimum by combination (combat_v30 §5) =====
STR_MIN_SHORT_LIGHT = 1          # [canonical: combat_v30 §5 (Short Light = 1)]
STR_MIN_ONE_HEAVY_OR_LONG = 2    # [canonical: combat_v30 §5 (Short Heavy or Long Light = 2)]
STR_MIN_LONG_HEAVY = 3           # [canonical: combat_v30 §5 (Long Heavy = 3)]
STR_MIN_LONG_HEAVY_BLUNT = 4     # [canonical: combat_v30 §5 (Long Heavy Blunt = 4)]
WIELD_UNDER_MIN_PENALTY = 1      # [canonical: combat_v30 §5 (1 below min -> -1D Combat Pool)]

# ===== Class A: weapon modifier vs armour tier (combat_v30 §5 Damage Resolution) =====
LIGHT_BLADE_VS_NONE = 3     # [canonical: combat_v30 §5 Damage Resolution]
LIGHT_BLADE_VS_LIGHT = 2    # [canonical: combat_v30 §5 Damage Resolution]
LIGHT_BLADE_VS_MEDIUM = 1   # [canonical: combat_v30 §5 Damage Resolution]
LIGHT_BLADE_VS_HEAVY = 0    # [canonical: combat_v30 §5 Damage Resolution]
HEAVY_BLADE_VS_NONE = 6     # [canonical: combat_v30 §5 Damage Resolution]
HEAVY_BLADE_VS_LIGHT = 4    # [canonical: combat_v30 §5 Damage Resolution]
HEAVY_BLADE_VS_MEDIUM = 2   # [canonical: combat_v30 §5 Damage Resolution]
HEAVY_BLADE_VS_HEAVY = 0    # [canonical: combat_v30 §5 Damage Resolution]
LIGHT_BLUNT_ALL = 3         # [canonical: combat_v30 §5 Damage Resolution (Light Blunt +3 all tiers)]
HEAVY_BLUNT_ALL = 5         # [canonical: combat_v30 §5 Damage Resolution (Heavy Blunt +5 all tiers)]
WEAPON_ARMOR_MOD = {
    "light_blade": {"none": LIGHT_BLADE_VS_NONE, "light": LIGHT_BLADE_VS_LIGHT, "medium": LIGHT_BLADE_VS_MEDIUM, "heavy": LIGHT_BLADE_VS_HEAVY},
    "heavy_blade": {"none": HEAVY_BLADE_VS_NONE, "light": HEAVY_BLADE_VS_LIGHT, "medium": HEAVY_BLADE_VS_MEDIUM, "heavy": HEAVY_BLADE_VS_HEAVY},
    "light_blunt": {"none": LIGHT_BLUNT_ALL, "light": LIGHT_BLUNT_ALL, "medium": LIGHT_BLUNT_ALL, "heavy": LIGHT_BLUNT_ALL},
    "heavy_blunt": {"none": HEAVY_BLUNT_ALL, "light": HEAVY_BLUNT_ALL, "medium": HEAVY_BLUNT_ALL, "heavy": HEAVY_BLUNT_ALL},
}

# ===== Class A: armour tier STR minimum (combat_v30 §6 Armour); None has no requirement =====
ARMOR_STR_MIN_LIGHT = 2    # [canonical: combat_v30 §6 Armour (Light min STR 2)]
ARMOR_STR_MIN_MEDIUM = 3   # [canonical: combat_v30 §6 Armour (Medium min STR 3)]
ARMOR_STR_MIN_HEAVY = 4    # [canonical: combat_v30 §6 Armour (Heavy min STR 4)]
ARMOR_STR_MIN = {"none": 0, "light": ARMOR_STR_MIN_LIGHT, "medium": ARMOR_STR_MIN_MEDIUM, "heavy": ARMOR_STR_MIN_HEAVY}

# ===== Class A: combat degree table (combat_v30 §5 Degree Table) =====
DEGREE_PARTIAL_MIN = 1       # [canonical: combat_v30 §5 Degree Table (1 = Partial)]
DEGREE_SUCCESS_MIN = 2       # [canonical: combat_v30 §5 Degree Table (2 = Success)]
DEGREE_OVERWHELMING_MIN = 3  # [canonical: combat_v30 §5 Degree Table (3+ = Overwhelming)]

# ===== Class B: v32 weapon handling profiles (combat_v32_proposal §8.2 -- draft) =====
HANDLING_FORGIVING_BONUS = 1    # [canonical: combat_v32_proposal §8.2 -- draft (Forgiving min(P+1,3))]
HANDLING_FORGIVING_CAP = 3      # [canonical: combat_v32_proposal §8.2 -- draft]
HANDLING_STANDARD_CAP = 4       # [canonical: combat_v32_proposal §8.2 -- draft (Standard min(P,4))]
HANDLING_DEMANDING_PENALTY = 1  # [canonical: combat_v32_proposal §8.2 -- draft (Demanding min(max(P-1,0),5))]
HANDLING_DEMANDING_CAP = 5      # [canonical: combat_v32_proposal §8.2 -- draft]

# ===== Class B: v32 Weapon Speed per class (combat_v32_proposal §8.4 -- draft) =====
SPEED_LONG_THRUST = 1.5       # [canonical: combat_v32_proposal §8.4 -- draft]
SPEED_LONG_CUT_THRUST = 0.5   # [canonical: combat_v32_proposal §8.4 -- draft]
SPEED_CURVED = 2              # [canonical: combat_v32_proposal §8.4 -- draft]
SPEED_POLE = 0               # [canonical: combat_v32_proposal §8.4 -- draft (spear/staff)]
SPEED_PAIRED_SHORT = 2.5      # [canonical: combat_v32_proposal §8.4 -- draft]
SPEED_SINGLE_SHORT = 3       # [canonical: combat_v32_proposal §8.4 -- draft]
SPEED_LONG_HEAVY_BLUNT = -0.5 # [canonical: combat_v32_proposal §8.4 -- draft]


def weapon_tn(reach, weight, wtype):
    """Canonical Hit TN (combat_v30 §5): base + reach + weight + type modifiers."""
    return WEAPON_BASE_TN + REACH_MOD[reach] + WEIGHT_MOD[weight] + TYPE_MOD[wtype]


def str_multiplier(weight, wtype):
    """STR damage multiplier (combat_v30 §5): weight factor x type factor (multiplicative)."""
    w = STR_MULT_HEAVY if weight == "heavy" else STR_MULT_LIGHT
    t = STR_MULT_BLUNT if wtype == "blunt" else STR_MULT_BLADE
    return w * t


def str_minimum(reach, weight, wtype):
    """Minimum STR to wield (combat_v30 §5): one step per Heavy/Long axis; Long Heavy Blunt special."""
    if reach == "long" and weight == "heavy" and wtype == "blunt":
        return STR_MIN_LONG_HEAVY_BLUNT
    if reach == "long" and weight == "heavy":
        return STR_MIN_LONG_HEAVY
    if reach == "long" or weight == "heavy":
        return STR_MIN_ONE_HEAVY_OR_LONG
    return STR_MIN_SHORT_LIGHT


def armor_damage_mod(damage_class, armor_tier):
    """Weapon-modifier-vs-armour-tier (combat_v30 §5 Damage Resolution table)."""
    return WEAPON_ARMOR_MOD[damage_class][armor_tier]


def handling(profile, proficiency):
    """Effective handling H(P) from per-weapon Proficiency (combat_v32_proposal §8.2, draft)."""
    p = proficiency
    if profile == "forgiving":
        return min(p + HANDLING_FORGIVING_BONUS, HANDLING_FORGIVING_CAP)
    if profile == "standard":
        return min(p, HANDLING_STANDARD_CAP)
    if profile == "demanding":
        return min(max(p - HANDLING_DEMANDING_PENALTY, 0), HANDLING_DEMANDING_CAP)
    raise ValueError(f"unknown handling profile: {profile}")


# ===== Class B: the v32 weapon classes (combat_v32_proposal §8.1/§8.2/§8.4 -- draft) =====
# §8 says "Seven weapon classes" but enumerates eight rows (Long Heavy Blunt = the plate-breaker
# addition); all eight encoded. base TN / min STR are DERIVED from the canonical axes (not hardcoded).
WEAPON_CLASSES = {
    "long_thrust_primary": {"reach": "long",  "weight": "light", "wtype": "blade", "damage_class": "light_blade", "handling": "demanding", "speed": SPEED_LONG_THRUST},      # [canonical: combat_v32_proposal §8 -- draft]
    "long_cut_and_thrust": {"reach": "long",  "weight": "heavy", "wtype": "blade", "damage_class": "heavy_blade", "handling": "standard",  "speed": SPEED_LONG_CUT_THRUST},   # [canonical: combat_v32_proposal §8 -- draft]
    "curved_cut_primary":  {"reach": "long",  "weight": "light", "wtype": "blade", "damage_class": "light_blade", "handling": "standard",  "speed": SPEED_CURVED},            # [canonical: combat_v32_proposal §8 -- draft]
    "long_pole_spear":     {"reach": "long",  "weight": "light", "wtype": "blade", "damage_class": "light_blade", "handling": "forgiving", "speed": SPEED_POLE},              # [canonical: combat_v32_proposal §8 -- draft]
    "long_pole_staff":     {"reach": "long",  "weight": "light", "wtype": "blunt", "damage_class": "light_blunt", "handling": "forgiving", "speed": SPEED_POLE},              # [canonical: combat_v32_proposal §8 -- draft]
    "paired_short":        {"reach": "short", "weight": "light", "wtype": "blade", "damage_class": "light_blade", "handling": "demanding", "speed": SPEED_PAIRED_SHORT},      # [canonical: combat_v32_proposal §8 -- draft]
    "single_short":        {"reach": "short", "weight": "light", "wtype": "blade", "damage_class": "light_blade", "handling": "forgiving", "speed": SPEED_SINGLE_SHORT},      # [canonical: combat_v32_proposal §8 -- draft]
    "long_heavy_blunt":    {"reach": "long",  "weight": "heavy", "wtype": "blunt", "damage_class": "heavy_blunt", "handling": "demanding", "speed": SPEED_LONG_HEAVY_BLUNT},  # [canonical: combat_v32_proposal §8 -- draft]
}


def build_weapon(class_name, proficiency):
    """Resolve a weapon class to its effective profile for the engine."""
    c = WEAPON_CLASSES[class_name]
    return {
        "class": class_name,
        "tn": weapon_tn(c["reach"], c["weight"], c["wtype"]),
        "min_str": str_minimum(c["reach"], c["weight"], c["wtype"]),
        "str_mult": str_multiplier(c["weight"], c["wtype"]),
        "handling": handling(c["handling"], proficiency),
        "speed": c["speed"],
        "damage_class": c["damage_class"],
    }


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("Module 3 (weapon-class layer) -- validation against canon")
    print(rule)

    # (a) Canonical 3-axis TN matrix
    TN_TABLE = {("short","light","blade"):5, ("short","light","blunt"):6, ("short","heavy","blade"):6, ("long","light","blade"):6, ("short","heavy","blunt"):7, ("long","heavy","blade"):7, ("long","light","blunt"):7, ("long","heavy","blunt"):8}  # [canonical: combat_v30 §5 Weapon TN Matrix combination table]
    a_ok = all(weapon_tn(*k) == v for k, v in TN_TABLE.items())
    checks.append(a_ok)
    print(f"\n(a) 3-axis TN matrix vs combat_v30 §5 ({len(TN_TABLE)} combinations): {'OK' if a_ok else 'FAIL'}")

    # (b) STR multiplier (multiplicative; Heavy Blunt = x3)
    MULT_CHECKS = {("light","blade"):1, ("heavy","blade"):2, ("light","blunt"):1.5, ("heavy","blunt"):3.0}  # [canonical: combat_v30 §5 Damage Resolution (Light×1/Heavy×2/Blade×1/Blunt×1.5)]
    b_ok = all(str_multiplier(w, t) == v for (w, t), v in MULT_CHECKS.items())
    checks.append(b_ok)
    print(f"(b) STR multiplier (Heavy Blunt -> {str_multiplier('heavy','blunt')}; canon x3): {'OK' if b_ok else 'FAIL'}")

    # (c) weapon modifier vs armour tier
    ARMOR_MOD_CHECKS = {("heavy_blade","none"):6, ("heavy_blade","heavy"):0, ("light_blade","none"):3, ("light_blade","heavy"):0, ("heavy_blunt","heavy"):5, ("light_blunt","medium"):3}  # [canonical: combat_v30 §5 weapon-modifier-vs-armour-tier table]
    c_ok = all(armor_damage_mod(c, a) == v for (c, a), v in ARMOR_MOD_CHECKS.items())
    checks.append(c_ok)
    print(f"(c) weapon-vs-armour table (Heavy Blade None/Heavy {armor_damage_mod('heavy_blade','none')}/{armor_damage_mod('heavy_blade','heavy')}; canon +6/+0): {'OK' if c_ok else 'FAIL'}")

    # (d) handling H(P) reproduces the v32 §8.2 verified table
    HANDLING_TABLE = {1:(2,1,0), 2:(3,2,1), 3:(3,3,2), 4:(3,4,3), 5:(3,4,4), 6:(3,4,5), 7:(3,4,5)}  # [canonical: combat_v32_proposal §8.2 verified handling table]
    d_ok = all((handling("forgiving", p), handling("standard", p), handling("demanding", p)) == v for p, v in HANDLING_TABLE.items())
    cross = handling("forgiving", 4) == handling("demanding", 4)   # crossover at P=4 (Forgiving == Demanding)
    d_ok = d_ok and cross
    checks.append(d_ok)
    print(f"(d) handling H(P) vs §8.2 table + crossover at P4 (F==D=={handling('forgiving',4)}): {'OK' if d_ok else 'FAIL'}")

    # (e) each v32 class's base TN matches the canonical 3-axis matrix
    CLASS_TN = {"long_thrust_primary":6, "long_cut_and_thrust":7, "curved_cut_primary":6, "long_pole_spear":6, "long_pole_staff":7, "paired_short":5, "single_short":5, "long_heavy_blunt":8}  # [canonical: combat_v32_proposal §8.1 base Hit TN]
    e_ok = all(weapon_tn(c["reach"], c["weight"], c["wtype"]) == CLASS_TN[n] for n, c in WEAPON_CLASSES.items())
    checks.append(e_ok)
    print(f"(e) v32 §8.1 class -> canonical TN consistency ({len(WEAPON_CLASSES)} classes): {'OK' if e_ok else 'FAIL'}")

    # weapon-class profile summary
    print("\n(weapon-class profiles, Proficiency 4):")
    print(f"    {'class':<20}{'TN':>3}{'minSTR':>7}{'STRmult':>9}{'H(P4)':>7}{'speed':>7}  dmg-class")
    for n in WEAPON_CLASSES:
        w = build_weapon(n, 4)
        print(f"    {n:<20}{w['tn']:>3}{w['min_str']:>7}{w['str_mult']:>9}{w['handling']:>7}{w['speed']:>7}  {w['damage_class']}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match canon "
          f"(3-axis TN matrix, STR multiplier, weapon-vs-armour table, handling H(P), class->TN consistency).")
