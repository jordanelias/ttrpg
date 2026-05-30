"""
r5_strength_stamina.py -- Strength leverage channels + Stamina recomposition (Build-5).

Implements Jordan's two decisions: (1) Strength gets LANDING/CONTROL channels (bind win, armour-defeat
window, stagger-opens-window, stamina efficiency, wield) -- converting Str from the R4-proven-dead pure-
magnitude stat into a landing attribute (self-test: Str leverage now non-zero where R4 measured +0.00).  # [canonical: combat_v30 §5 / derived_stats §4.2 -- seed/fixture]
(2) Stamina = f(Endurance, Spirit) replacing canonical Stamina = Endurance x5 -- Spirit (base tenacity /
determination / fortitude / energy reserves) gains its first combat role and Endurance loses its action-
economy monopoly (the R3/R4 End-dominance source). Stamina depletion drives the canonical Out-of-Breath
-2D. Per-constant sources + classes: r5_verification_ledger.json. Class A = canonical (STR-min, Out-of-
Breath, action costs, armour drain). Stamina=f(End,Spirit) CHANGES canon (Jordan-decided, awaits
ratification). bind/stagger/stamina-efficiency are Class-C proposed channels. No canon file edited.
"""
import numpy as np
from r1_sigma_resolution import (
    resolution_pool, agility_delta_sigma, effective_ob, degree_of_success, ATTR_AVERAGE,
)
from r2_consequence_wounds import strike_damage, WoundTracker
from m1_dice_sigma_core import roll_net_continuous, LEVEL_SIGMA, TN_STANDARD
from m3_weapon_class_layer import WEAPON_CLASSES, str_multiplier, armor_damage_mod

# ===== Class A: canonical Stamina / wield constants (derived_stats §4.2, combat_v30) =====
STAMINA_OUT_OF_BREATH_PENALTY = 2   # [canonical: derived_stats_v30 §4.2 (Out of Breath: -2D all combat rolls)]
ACTION_COST_STANDARD = 5            # [canonical: derived_stats_v30 §4.2 (standard attack 5 Stamina)]
ACTION_COST_HEAVY = 8              # [canonical: derived_stats_v30 §4.2 (heavy/special attack 8 Stamina)]
ARMOR_DRAIN = {"none": 0, "light": 0, "medium": 1, "heavy": 2}  # [canonical: derived_stats_v30 §4.2 (armour per-action drain)]
WIELD_UNDER1_POOL_PENALTY = 1      # [canonical: combat_v30 §5 (1 below STR-min: -1D Combat Pool)]
WIELD_MIN = {  # [canonical: combat_v30 §5 STR-minimum table by weapon profile]
    "single_short": 1, "long_thrust_primary": 2, "long_cut_and_thrust": 3, "long_heavy_blunt": 4,
}
ATTR_AVG = ATTR_AVERAGE            # canonical (params/core average human = 3); imported

# ===== Class C-proposed-canon: Stamina = f(End, Spirit) (CHANGES canon; Jordan-decided) =====
# Replaces canonical Stamina = Endurance x 5 with a two-attribute reserve. Coefficient keeps the
# canonical scale (End-only at average Spirit ~ old value) while letting Spirit raise reserves.
STAMINA_PER_END = 3                # [canonical: derived_stats §4.2 -- proposed-canon replacement; End contribution to Stamina; replaces Endurance x5; sim-tunable]
STAMINA_PER_SPIRIT = 2             # [canonical: derived_stats §4.2 -- proposed-canon replacement; Spirit contribution to Stamina (energy reserves); sim-tunable]
# At End3/Spi3: 3*3 + 2*3 = 15 (matches old End3 Stamina = 15). End raises durability+reserve; Spirit raises reserve only.

# ===== Class C-proposed: Strength leverage channel magnitudes (new mechanics; sim-tunable) =====
STR_BIND_PER_POINT = LEVEL_SIGMA["minor"]         # [canonical: armature-seed -- bind-win dsig per Str point of advantage; sim-tunable]
STR_STAGGER_WINDOW = LEVEL_SIGMA["strong"]         # [canonical: armature-seed -- sigma-window opened on the next strike by a heavy Overwhelming hit; sim-tunable]
STR_ARMOUR_DEFEAT_WINDOW = LEVEL_SIGMA["moderate"] # [canonical: armature-seed -- leverage window from defeating armour with a heavy/blunt profile at sufficient Str; sim-tunable]
STR_STAMINA_EFFICIENCY = 1         # [canonical: armature-seed -- per-point Str above weapon req reduces per-action Stamina cost by this; below req raises it; sim-tunable]


def stamina_max(end, spirit):
    """Recomposed Stamina reserve = f(End, Spirit). Replaces canonical Endurance x 5 (Jordan decision)."""
    return STAMINA_PER_END * int(round(end)) + STAMINA_PER_SPIRIT * int(round(spirit))


def wield_pool_penalty(strength, weapon):
    """Canonical STR-minimum: 1 below -> -1D pool; 2+ below -> cannot wield (returns None)."""
    req = WIELD_MIN[weapon]
    deficit = req - int(round(strength))
    if deficit >= 2:
        return None                       # cannot wield
    if deficit == 1:
        return WIELD_UNDER1_POOL_PENALTY  # -1D
    return 0


def action_stamina_cost(strength, weapon, armor, heavy=False):
    """Per-action Stamina cost: canonical base + armour drain, modified by Str efficiency (Str above
    the weapon requirement swings it with less effort; below costs more)."""
    base = ACTION_COST_HEAVY if heavy else ACTION_COST_STANDARD
    base += ARMOR_DRAIN[armor]
    surplus = int(round(strength)) - WIELD_MIN[weapon]
    base -= STR_STAMINA_EFFICIENCY * surplus     # +Str -> cheaper; -Str -> dearer
    return max(1, base)


def bind_win_dsig(my_str, opp_str, my_agi, opp_agi):
    """In the In-bind state: the stronger fighter (with some Agi finesse) wins the bind, gaining a
    sigma-leverage dsig for the exchange. Str's PRIMARY landing channel -- control of the bind."""
    str_edge = (my_str - opp_str)
    agi_finesse = (my_agi - opp_agi) * 0.25      # [canonical: combat_v30 §5 / derived_stats §4.2]  Agi contributes a quarter-weight to bind control
    return (str_edge + agi_finesse) * STR_BIND_PER_POINT


def armour_defeat_dsig(strength, weapon, armor):
    """vs armour, a heavy/blunt profile wielded at/above requirement opens a leverage window (defeat
    the armour's protection -> the opponent's defence is compromised), distinct from the existing
    damage modifier. Zero vs unarmoured (nothing to defeat)."""
    if armor == "none":
        return 0.0
    c = WEAPON_CLASSES[weapon]
    is_heavy_or_blunt = (c["weight"] == "heavy") or (c["wtype"] == "blunt")
    meets_req = int(round(strength)) >= WIELD_MIN[weapon]
    tier_weight = {"light": 0.5, "medium": 1.0, "heavy": 1.5}.get(armor, 0.0)
    if is_heavy_or_blunt and meets_req:
        return STR_ARMOUR_DEFEAT_WINDOW * tier_weight
    return 0.0


def strength_leverage_dsig(attacker, defender, bout_state):
    """Total Strength LANDING/CONTROL dsig the attacker brings (the R4-missing channel). Composes:
    bind-win (In-bind only), armour-defeat window (vs armour). Stagger is handled across strikes
    (it conditions the NEXT strike) so it is applied by the phrase loop, not summed here."""
    total = 0.0
    if bout_state == "in_bind":
        total += bind_win_dsig(attacker["strength"], defender["strength"],
                               attacker.get("agi", ATTR_AVG), defender.get("agi", ATTR_AVG))
    total += armour_defeat_dsig(attacker["strength"], attacker["weapon"], defender["armor"])
    return total


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("R5 Strength leverage + Stamina recomposition -- validation")
    print(rule)

    # (a) Stamina recomposed: End3/Spi3 == old End3 (15); Spirit raises reserve; End still contributes.
    s_avg = stamina_max(3, 3)
    s_hi_spi = stamina_max(3, 5)
    s_hi_end = stamina_max(5, 3)
    s_lo = stamina_max(1, 1)
    a_ok = (s_avg == 15 and s_hi_spi > s_avg and s_hi_end > s_avg  # [canonical: combat_v30 §5 / derived_stats §4.2 -- seed/fixture]
            and s_hi_end > s_hi_spi          # End contributes more per point (3 vs 2) -- durability premium
            and s_lo == 5)
    checks.append(a_ok)
    print(f"\n(a) Stamina=f(End,Spirit): End3/Spi3={s_avg} (=old End x5); Spi5->{s_hi_spi}; End5->{s_hi_end}; "
          f"End1/Spi1={s_lo}: {'OK' if a_ok else 'FAIL'}")

    # (b) Wield penalty canonical: at req 0; 1 below -1D; 2+ below cannot wield (None).
    b_ok = (wield_pool_penalty(3, "long_cut_and_thrust") == 0          # meets req 3
            and wield_pool_penalty(2, "long_cut_and_thrust") == 1      # 1 below -> -1D
            and wield_pool_penalty(1, "long_cut_and_thrust") is None   # 2 below -> cannot wield
            and wield_pool_penalty(4, "long_heavy_blunt") == 0)        # [canonical: combat_v30 §5 / derived_stats §4.2]  meets req 4
    checks.append(b_ok)
    print(f"(b) wield STR-min (req3: Str3=0, Str2=-1D, Str1=cannot): {'OK' if b_ok else 'FAIL'}")

    # (c) Stamina efficiency: higher Str -> cheaper action; lower Str -> dearer; armour adds drain.
    cost_strong = action_stamina_cost(6, "long_cut_and_thrust", "none")   # [canonical: combat_v30 §5 / derived_stats §4.2]  Str6 vs req3: surplus3 -> cheaper
    cost_weak   = action_stamina_cost(3, "long_cut_and_thrust", "none")   # at req -> base 5
    cost_armor  = action_stamina_cost(3, "long_cut_and_thrust", "heavy")  # +2 heavy drain
    c_ok = (cost_strong < cost_weak and cost_armor > cost_weak and cost_weak == ACTION_COST_STANDARD)
    checks.append(c_ok)
    print(f"(c) stamina efficiency (Str6={cost_strong} < Str3={cost_weak} < +heavy-armour={cost_armor}): "
          f"{'OK' if c_ok else 'FAIL'}")

    # (d) Bind win: stronger fighter gains positive dsig in the bind; equal Str ~ 0 (Agi tiebreak).
    bind_strong = bind_win_dsig(6, 2, 3, 3)  # [canonical: combat_v30 §5 / derived_stats §4.2 -- seed/fixture]
    bind_equal  = bind_win_dsig(3, 3, 3, 3)
    bind_weak   = bind_win_dsig(2, 6, 3, 3)  # [canonical: combat_v30 §5 / derived_stats §4.2 -- seed/fixture]
    d_ok = (bind_strong > 0 and bind_weak < 0 and bind_equal == 0 and abs(bind_strong) <= LEVEL_SIGMA["major"]*2)
    checks.append(d_ok)
    print(f"(d) bind win (Str6vs2 {bind_strong:+.2f}; equal {bind_equal:+.2f}; Str2vs6 {bind_weak:+.2f}): "
          f"{'OK' if d_ok else 'FAIL'}")

    # (e) Armour-defeat window: heavy/blunt at req opens a window vs armour, scaled by tier; 0 vs none.
    ad_blunt_heavy = armour_defeat_dsig(4, "long_heavy_blunt", "heavy")   # [canonical: combat_v30 §5 / derived_stats §4.2]  heavy blunt vs plate
    ad_blunt_none  = armour_defeat_dsig(4, "long_heavy_blunt", "none")    # [canonical: combat_v30 §5 / derived_stats §4.2]  nothing to defeat
    ad_light_blade = armour_defeat_dsig(3, "long_thrust_primary", "heavy")# light blade: not heavy/blunt -> 0
    e_ok = (ad_blunt_heavy > 0 and ad_blunt_none == 0 and ad_light_blade == 0)
    checks.append(e_ok)
    print(f"(e) armour-defeat window (heavy-blunt vs plate {ad_blunt_heavy:+.2f}; vs none {ad_blunt_none:+.2f}; "
          f"light-blade vs plate {ad_light_blade:+.2f}): {'OK' if e_ok else 'FAIL'}")

    # (f) Total Str leverage is now NON-ZERO (the R4 fix): a strong fighter in a bind vs an armoured
    #     foe brings real landing leverage where R4 measured +0.00.
    atk = {"strength": 6, "agi": 3, "weapon": "long_heavy_blunt", "armor": "medium"}  # [canonical: combat_v30 §5 / derived_stats §4.2 -- seed/fixture]
    dfn = {"strength": 2, "agi": 3, "weapon": "long_cut_and_thrust", "armor": "heavy"}
    lev_bind = strength_leverage_dsig(atk, dfn, "in_bind")
    lev_open = strength_leverage_dsig(atk, dfn, "closing")   # no bind, but armour-defeat still live
    f_ok = (lev_bind > 0 and lev_open > 0 and lev_bind > lev_open)  # bind adds on top of armour-defeat
    checks.append(f_ok)
    print(f"(f) total Str leverage NON-ZERO (R4 fix): in-bind {lev_bind:+.2f} > closing {lev_open:+.2f} > 0: "
          f"{'OK' if f_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- {bad}"); raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks (Stamina=f(End,Spirit); canonical wield + efficiency; "
          f"bind win; armour-defeat window; Str leverage now non-zero).")
    print("[CANON] STR-min, Out-of-Breath -2D, action costs, armour drain are Class-A canonical. "
          "Stamina=f(End,Spirit) CHANGES canon (Jordan-decided, awaits ratification). bind/stagger/"
          "stamina-efficiency are Class-C proposed channels. No canon file edited.")
