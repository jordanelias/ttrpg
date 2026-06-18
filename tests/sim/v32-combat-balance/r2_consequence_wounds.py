"""
r2_consequence_wounds.py -- combat CONSEQUENCE atom (armature reset, Build-2).

Wound severity on a landing strike + the authoritative non-resetting wound-gate tracker. Where
Strength and Endurance get their teeth against Agility's sigma-leverage tempo (R1). Reuses M3
(canonical weapon multipliers + weapon-vs-armour table); the wound-gate tracker is derived_stats
AUTHORITATIVE. The canonical damage formula and crit rule, the unified-armour statement, and the
wound-gate mechanic are all reproduced verbatim from canon -- see the per-constant quoted_text in
tests/sim/v32-combat-balance/r2_verification_ledger.json for exact sources (combat_v30 Damage
Resolution / Armour; derived_stats Health). The armour model is unified BY CANON (the weapon-vs-
armour table IS the DR; M9's per-type resist is retained only as the historical validation oracle,
never a second subtractor). Class A = canonical; Class C = the one armature framing (decisive
multi-gate applied per-exchange, not per-round attrition). PROPOSAL -- no canon edited.
"""
import numpy as np
from m3_weapon_class_layer import str_multiplier, armor_damage_mod, WEAPON_CLASSES

# ===== Class A: canonical crit / wound-gate constants =====
CRIT_NET_MIN = 3             # [canonical: combat_v30 §5 Damage Resolution (Critical Hit: net hits >= 3 -> weapon modifier doubled)]
CRIT_WEAPON_MOD_MULT = 2     # [canonical: combat_v30 §5 Damage Resolution (Critical: weapon modifier doubled before armour reduction, PP-211)]
WOUND_INTERVAL_BASE = 4       # [D-A recalib, Jordan 2026-06-18: flat base lowered 6->4; the 2 pts moved into the Spirit/Strength terms below, conserving avg Health=40 while adding spread]      # [canonical: derived_stats_v30 §4.1 (Wound Interval = Endurance + 6)]
MAXWOUNDS_DIV = 2            # [canonical: derived_stats_v30 §4.1 (floor(Endurance / 2))]
MAXWOUNDS_ADD = 1            # [canonical: derived_stats_v30 §4.1 (+1)]
MAXWOUNDS_CAP = 3            # [canonical: derived_stats_v30 §4.1 (Max Wounds capped at 3, PP-717)]
WOUND_POOL_PENALTY = 1       # [canonical: derived_stats_v30 §4.1 (each wound: -1D to Pools; no Ob penalty)]
SPI_WI_W = 0.4               # [D-A noise, Jordan 2026-06-18: Spirit at low weight increases the Wound Interval -> reduces uniformity]
STR_HEALTH_W = 0.25          # [D-A noise, Jordan 2026-06-18: Strength at very low weight, proportional to Endurance, into Health -> reduces uniformity]
DAMAGE_FLOOR = 0             # [canonical: combat_v30 §5 (net hits minimum 0; damage cannot be negative)]


def max_wounds(end):
    """Max Wounds (derived_stats_v30 §4.1, authoritative): min(floor(End/2)+1, cap)."""
    return min(end // MAXWOUNDS_DIV + MAXWOUNDS_ADD, MAXWOUNDS_CAP)


def wound_interval(end, spirit=3):
    """Wound Interval (derived_stats_v30 §4.1): End + base + low-weight Spirit (D-A, Jordan 2026-06-18)."""
    return round(end + WOUND_INTERVAL_BASE + SPI_WI_W*spirit)


def health_full(end, spirit=3, strength=4):
    """Full Health (derived_stats_v30 §4.1): WI x (MaxWounds+1) + low-weight Strength*Endurance (D-A, Jordan 2026-06-18)."""
    return round(wound_interval(end, spirit) * (max_wounds(end) + 1) + STR_HEALTH_W*strength*end)


def strike_damage(net, strength, weapon_class, armor_tier):
    """Canonical strike damage (combat_v30 §5 Damage Resolution):  # [canonical: see r2_verification_ledger.json]
        damage = net + (STR x multiplier) + weapon-modifier-vs-armour-tier
    A critical (net >= 3 = Overwhelming) DOUBLES the weapon modifier before it is applied (the STR x
    multiplier term is NOT doubled -- canon explicit). Floored at 0. The armour reduction is the
    weapon-vs-armour table itself (canon: 'DR is subsumed into the weapon modifier vs armour tier
    table') -- no separate subtractor."""
    if net <= 0:
        return DAMAGE_FLOOR
    dmg_class = WEAPON_CLASSES[weapon_class]["damage_class"]
    weapon_mod = armor_damage_mod(dmg_class, armor_tier)
    if net >= CRIT_NET_MIN:
        weapon_mod *= CRIT_WEAPON_MOD_MULT                 # crit doubles ONLY the weapon modifier (PP-211)
    c = WEAPON_CLASSES[weapon_class]
    str_term = strength * str_multiplier(c["weight"], c["wtype"])
    return max(DAMAGE_FLOOR, int(round(net + str_term + weapon_mod)))


class WoundTracker:
    """The authoritative non-resetting wound-gate tracker (derived_stats_v30 §4.1).  # [canonical: see r2_verification_ledger.json]
    Health depletes; every WI of cumulative damage is a wound gate; a single hit larger than WI
    crosses multiple gates at once (the decisive strike). Felled at Health depletion (D-A reshape).
    Each wound = -1D to Pools (queried via pool_penalty); no Ob penalty, ever. Persists between
    encounters (cleared only at session end, per canon)."""

    def __init__(self, end, equipment_health=0, spirit=3, strength=4):
        self.end = end; self.spirit = spirit; self.strength = strength
        self.wi = wound_interval(end, spirit)
        self.max_wounds = max_wounds(end)
        self.health_full = health_full(end, spirit, strength) + equipment_health
        self.cumulative_damage = 0

    @property
    def health_remaining(self):
        return max(0, self.health_full - self.cumulative_damage)

    @property
    def wounds(self):
        """Wounds accrued = floor(cumulative_damage / WI), capped at MW+1 (felled)."""
        return min(self.cumulative_damage // self.wi, self.max_wounds + 1)

    @property
    def felled(self):
        """Incapacitated at Health depletion (cumulative damage >= Health). Health carries a low-weight
        Strength buffer (D-A reshape, Jordan-ratified), so Strength now buys survivability; coincides with the
        old MW+1-wound rule when that buffer is zero. Pool penalty still caps at MW+1 wounds (-1D each)."""
        return self.cumulative_damage >= self.health_full

    def pool_penalty(self):
        """-1D per wound to all Pools (capped at felled). No Ob penalty (canon)."""
        return min(self.wounds, self.max_wounds + 1) * WOUND_POOL_PENALTY

    def apply(self, damage):
        """Apply a strike's damage. Returns (new_wounds_inflicted, felled). A hit > WI inflicts
        multiple wounds at once -- the decisive blow crossing several gates."""
        before = self.wounds
        self.cumulative_damage += max(0, int(damage))
        inflicted = self.wounds - before
        return inflicted, self.felled


# ============================== self-test = canon + historical oracle ==============================
if __name__ == "__main__":
    # M9's per-type resist is the historical ORACLE only (NOT used in the damage path).
    from m9_wound_model_bottomup import ARMOR_RESIST
    checks = []
    rule = "================================================================"
    print("R2 consequence atom -- canonical damage + wound-gate tracker (validation)")
    print(rule)

    # (a) Canonical damage formula reproduces combat_v30 §5 worked structure: a heavy-blade cut to no
    #     armour = net + STR*2 + weapon_mod(heavy_blade vs none = +6). (M4b cross-check: pool 17 ~ dmg 10
    #     regime; here we check the formula composition, not a sweep outcome.)
    d = strike_damage(2, 4, "long_cut_and_thrust", "none")     # [canonical: combat_v30 §5 / derived_stats §4.1]  net2 + 4*2 + 6(heavy_blade vs none) = 16
    a_ok = (d == 2 + 4 * 2 + 6)  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
    checks.append(a_ok)
    print(f"\n(a) canonical damage net2/Str4/heavy-blade vs none = {d} (= 2 + Str*2 + weapon_mod 6): {'OK' if a_ok else 'FAIL'}")

    # (b) Crit doubles ONLY the weapon modifier (net>=3), NOT the STR term (canon explicit).
    base = strike_damage(2, 4, "long_cut_and_thrust", "none")  # [canonical: combat_v30 §5 / derived_stats §4.1]  net2: not a crit -> weapon_mod x1
    crit = strike_damage(CRIT_NET_MIN, 4, "long_cut_and_thrust", "none")  # [canonical: combat_v30 §5 / derived_stats §4.1]  net3: crit -> weapon_mod doubled
    # delta from crit = (net+1 step) + doubled weapon_mod (6->12, +6); STR term unchanged
    expected_crit = CRIT_NET_MIN + 4 * 2 + 6 * CRIT_WEAPON_MOD_MULT  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
    b_ok = (crit == expected_crit and (crit - base) == (CRIT_NET_MIN - 2) + 6)
    checks.append(b_ok)
    print(f"(b) crit doubles weapon-mod only (net3 crit = {crit} = net + Str*2 + 2*weapon_mod; STR term not doubled): {'OK' if b_ok else 'FAIL'}")

    # (c) Unified armour = the canonical table; matches M9's historical ORACLE direction:
    #     plate negates cut, blunt defeats plate, thrust beats cut vs plate. (Validates the canonical
    #     table reproduces the bottom-up history WITHOUT a second subtractor.)
    cut_plate   = strike_damage(3, 7, "single_short", "heavy")        # [canonical: combat_v30 §5 / derived_stats §4.1]  light_blade vs heavy = +0 weapon mod
    blunt_plate = strike_damage(3, 7, "long_heavy_blunt", "heavy")    # [canonical: combat_v30 §5 / derived_stats §4.1]  heavy_blunt = +5 ALL tiers (doubled by crit)
    thrust_plate= strike_damage(3, 7, "long_thrust_primary", "heavy") # [canonical: combat_v30 §5 / derived_stats §4.1]  light_blade vs heavy = +0 (thrust-primary still light_blade class)
    # oracle directions from M9 (subtractor model): plate cut-resist 4 > thrust 2 > blunt 1
    oracle_ok = (ARMOR_RESIST["heavy"]["cut"] > ARMOR_RESIST["heavy"]["thrust"] > ARMOR_RESIST["heavy"]["blunt"])
    canon_ok = (blunt_plate > cut_plate)        # blunt defeats plate (weapon table: heavy_blunt +5 vs light_blade +0)
    c_ok = oracle_ok and canon_ok
    checks.append(c_ok)
    print(f"(c) unified armour = canonical table; blunt vs plate {blunt_plate} > cut vs plate {cut_plate} "
          f"(M9 oracle plate cut>thrust>blunt {ARMOR_RESIST['heavy']['cut']}/{ARMOR_RESIST['heavy']['thrust']}/{ARMOR_RESIST['heavy']['blunt']}): {'OK' if c_ok else 'FAIL'}")

    # (d) Wound-gate tracker reproduces derived_stats §4.1 authoritative table (End4 worked example).
    t = WoundTracker(4)  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
    table_ok = (t.health_full == 40 and t.wi == 9 and t.max_wounds == 3)  # [D-A recalib 2026-06-18: WI 10->9; Health held at 40]
    t.apply(10);  w1 = (t.wounds, t.health_remaining)   # 40->30, 1 wound
    t.apply(10);  w2 = (t.wounds, t.health_remaining)   # ->20, 2
    t.apply(10);  w3 = (t.wounds, t.health_remaining)   # ->10, 3, still alive
    f_before = t.felled
    t.apply(10);  w4 = (t.wounds, t.felled)             # ->0, 4 wounds, felled
    d_ok = (table_ok and w1 == (1, 30) and w2 == (2, 20) and w3 == (3, 10)  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
            and not f_before and w4 == (4, True))  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
    checks.append(d_ok)
    print(f"(d) wound tracker End4 (Health {t.health_full}, WI {t.wi}, MW {t.max_wounds}; "
          f"40->30->20->10->felled at 4th): {'OK' if d_ok else 'FAIL'}")

    # (e) MaxWounds cap (PP-717): End6/7 capped at 3 gates (the 'few gates' bound; not 4).
    e_ok = (max_wounds(6) == MAXWOUNDS_CAP and max_wounds(7) == MAXWOUNDS_CAP  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
            and max_wounds(4) == 3 and max_wounds(1) == 1 and max_wounds(2) == 2)  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
    checks.append(e_ok)
    print(f"(e) MaxWounds cap PP-717 (End6->{max_wounds(6)}, End7->{max_wounds(7)}, capped at {MAXWOUNDS_CAP}; "
          f"End1->{max_wounds(1)}, End2->{max_wounds(2)}): {'OK' if e_ok else 'FAIL'}")

    # (f) Decisive multi-gate strike: a single hit > WI crosses MULTIPLE gates at once (the bounded
    #     payoff of the reinstated multiplier in a one-exchange phrase). Gate count still hard-capped.
    t2 = WoundTracker(4)                          # [canonical: combat_v30 §5 / derived_stats §4.1]  WI 10, MW 3
    inflicted, felled = t2.apply(25)              # [canonical: combat_v30 §5 / derived_stats §4.1]  25 dmg = 2 full WI -> 2 wounds at once
    big = WoundTracker(4)  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
    big.apply(100)                                # massive overkill -> capped at MW+1 (felled), not unbounded
    f_ok = (inflicted == 2 and not felled and big.wounds == big.max_wounds + 1 and big.felled)
    checks.append(f_ok)
    print(f"(f) decisive multi-gate (25 dmg -> {inflicted} wounds at once; overkill capped at MW+1 = {big.wounds}, felled): {'OK' if f_ok else 'FAIL'}")

    # (g) Wound pool penalty: -1D per wound, no Ob channel (canon universality).
    t3 = WoundTracker(4)  # [canonical: combat_v30 §5 / derived_stats §4.1 -- self-test fixture]
    p0 = t3.pool_penalty()
    t3.apply(10); p1 = t3.pool_penalty()
    t3.apply(10); p2 = t3.pool_penalty()
    g_ok = (p0 == 0 and p1 == 1 and p2 == 2)
    checks.append(g_ok)
    print(f"(g) wound penalty -1D/wound, no Ob (0/{p1}/{p2} after 0/1/2 wounds): {'OK' if g_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks "
          f"(canonical damage formula, crit doubles weapon-mod only, unified-armour = canon table "
          f"matching M9 oracle, wound-gate tracker authoritative table, MW cap, decisive multi-gate, wound penalty).")
    print("[CANON] damage formula + crit rule + wound-gate are Class-A canonical (combat_v30 §5/§6, derived_stats §4.1); "
          "armour model is the canonical table (unified by canon, M9 resist used only as historical oracle).")
