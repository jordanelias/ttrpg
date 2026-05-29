"""
m4b_subaction_mechanics.py -- Module 4b of the v32 combat-balance sim (sub-action mechanics).

The per-sub-action resolution detail that runs inside M4a's bout state graph:
  - sub-action Pool composition (relevant-attribute x2 + Aspect Proficiency + History; wound penalty)
  - sigma-space Effective Ob (reuses M1: soft cap + Ob shift), state-gated per engagement state
  - degree of success (Failure / Partial / Success / Overwhelming) and per-sub-action effects
  - strike damage (canonical combat_v30 weapon system, via M3); Targeted-line anti-armor path

Imports M1 (sigma-space + roll_net), M2 (Combat Pool floor), M3 (weapon TN / STR mult / armour mod).

THREE design decisions are surfaced as flagged drafts, NOT silently resolved (prep-doc Jordan calls):
  [DECISION]   modifiers live in sigma-space (Option A, per proposal + M1) vs dice-space (Option B) -- Jordan
  [ASSUMPTION] Yield uses Focus (canonical Will is absent; the proposal substitutes Foc) -- Jordan call
  [ASSUMPTION] Displace relevant-attribute = mean(Str, Agi) composite (proposal: "Str+Agi composite, sim-tunable")

TWO proposal discrepancies flagged for Jordan:
  [DRIFT] the worked example computes a net-5 hit WITHOUT crit doubling (10 dmg) while the degree
          table makes an Overwhelming hit a Critical (the doubled figure). This fn applies the canonical crit rule.
  [DRIFT] Targeted-line "tier -1" is stated as Heavy->Light explicitly (skips Medium); Medium/Light
          downgrades are unspecified and drafted here.

Constant provenance: tests/sim/v32-combat-balance/m4b_verification_ledger.json
  Class A = canonical (combat_v30 weapon system / params/core pool grammar).
  Class B = v32 draft sim-seeds (combat_v32_proposal sub-action sections); sim-tunable, NOT canonical.
"""
import numpy as np
from m1_dice_sigma_core import soft_cap, sigma_n, eff_ob, roll_net, LEVEL_SIGMA, p_success
from m2_attribute_pool_builder import COMBAT_POOL_FLOOR
from m3_weapon_class_layer import str_multiplier, armor_damage_mod, WEAPON_CLASSES

# ===== Class A: pool grammar + degree/crit thresholds (canonical) =====
SUBACTION_POOL_ATTR_MULT = 2      # [canonical: params/core.md §Derived Scores (relevant-attribute x2, echoes Combat Pool PP-615)]
DEGREE_OVERWHELMING_OB_MULT = 2   # [canonical: combat_v30 §5 / combat_v32 §12.4 (Overwhelming: net >= 2*Ob)]
OVERWHELMING_NET_MIN = 3          # [canonical: combat_v30 §5 Degree Table (3+ Overwhelming; §12.4 net >= 3)]
CRITICAL_NET_MIN = 3              # [canonical: combat_v30 §5 Damage Resolution (PP-211: net >= 3 doubles weapon mod)]

# ===== Class B: §12.4 sub-action effect magnitudes (drafts) =====
TARGETED_LINE_PRECISION_SIGMA = -0.75   # [canonical: combat_v32_proposal §12.4 -- draft (Strong adverse precision penalty)]
PRESS_HELD_OB = 0.5                     # [canonical: combat_v32_proposal §12.4 -- draft (Press Partial: opponent +0.5 Ob)]
PROBE_TELEGRAPH_OB = 0.5                # [canonical: combat_v32_proposal §12.4 -- draft (Probe Failure: opponent +0.5 Ob)]
NEXT_STEP_BONUS_D = 1                   # [canonical: combat_v32_proposal §12.4 -- draft (+1D next step; Yield -1D; Displace stance -1)]
# Targeted-line armour downgrade: Heavy->Light is the proposal's explicit mapping; Medium/Light drafted.
TARGETED_LINE_DOWNGRADE = {"heavy": "light", "medium": "light", "light": "none", "none": "none"}  # [canonical: combat_v32_proposal §12.4 -- draft (explicit Heavy->Light; Medium/Light drafted)]

# ===== sigma-space state-gating (combat_v32_proposal §12.3 -- draft) =====
# Only modifiers physically relevant to the current engagement state are live (the rest zero).
STATE_LIVE_MODIFIERS = {
    "out_of_contact": ["perception", "reading", "weapon_phase", "set_bonus"],                            # [canonical: combat_v32_proposal §12.3 -- draft]
    "closing":        ["stance_counter", "reaction", "perception", "reading", "weapon_phase", "set_bonus"],  # [canonical: combat_v32_proposal §12.3 -- draft]
    "in_bind":        ["reaction", "tactile_reading", "grip_weapon_phase", "set_bonus"],                  # [canonical: combat_v32_proposal §12.3 -- draft (Stance Counter + sight-perception drop in the bind)]
    "breaking":       ["perception", "reaction", "reading"],                                              # [canonical: combat_v32_proposal §12.3 -- draft]
}

# ===== relevant-attribute per sub-action (combat_v32_proposal §12.2 -- draft) =====
SUBACTION_ATTR = {
    "cut": "by_weight", "thrust": "by_weight",
    "press": "str", "wind": "str", "press_the_bind": "str",
    "yield": "foc", "yield_to_bind": "foc",
    "void": "agi", "void_and_counter": "agi",
    "displace": "composite",
    "grip_change": "str", "break_bind": "str", "throw_strike": "str",
    "probe_cut": "agi", "probe_thrust": "agi", "step_around": "agi",
    "disengage": "agi", "targeted_line": "agi", "pursue": "agi", "release": "agi",
}  # [canonical: combat_v32_proposal §12.2 -- draft (Yield=Foc and Displace composite are flagged Jordan calls)]


def relevant_attr_value(subaction, agi, strength, focus, weapon_weight):
    """Resolve which attribute value feeds a sub-action's Pool (§12.2 draft)."""
    kind = SUBACTION_ATTR[subaction]
    if kind == "agi":
        return agi
    if kind == "str":
        return strength
    if kind == "foc":
        return focus
    if kind == "by_weight":
        return strength if weapon_weight == "heavy" else agi
    if kind == "composite":
        return (strength + agi) // 2   # [ASSUMPTION: Displace composite = mean(Str, Agi); proposal sim-tunable]
    raise ValueError(f"unknown sub-action: {subaction}")


def subaction_pool(attr_value, asp_prof, history_mod, wounds=0):
    """Sub-action Pool (§12.2): (attr x2) + Aspect Proficiency + History - wound penalty, floored at Combat Pool floor."""
    raw = attr_value * SUBACTION_POOL_ATTR_MULT + asp_prof + history_mod
    return max(COMBAT_POOL_FLOOR, raw - wounds)


def net_sigma_from_levels(levels):
    """Sum advantage levels (Minor/Moderate/Strong/Major) into net delta-sigma (M1 LEVEL_SIGMA)."""
    return sum(LEVEL_SIGMA[l] for l in levels)


def live_modifiers(state):
    """The delta-sigma contributors active at an engagement state (§12.3 state-gating)."""
    return STATE_LIVE_MODIFIERS[state]


def effective_ob(base_ob, pool, net_sigma):
    """State-gated sigma-space Effective Ob (§12.3) = base Ob - softcap(net_sigma)*sigma_N (M1); floored at 0."""
    return max(0, eff_ob(base_ob, pool, net_sigma))


def degree(net, base_ob):
    """Degree of success (combat_v30 + combat_v32):
    Overwhelming if net >= 2*Ob AND net >= 3; Success if net >= Ob; Partial if 0 < net < Ob; else Failure."""
    if net <= 0:
        return "failure"
    if net >= base_ob * DEGREE_OVERWHELMING_OB_MULT and net >= OVERWHELMING_NET_MIN:
        return "overwhelming"
    if net >= base_ob:
        return "success"
    return "partial"


def strike_damage(net, strength, weapon_class, armor_tier, crit=False):
    """Damage on a landing Cut/Thrust (canonical combat_v30 §5 Damage Resolution):
    net + (STR x multiplier) + weapon-modifier-vs-armour; weapon modifier doubled on crit.
    Crit fires at the Overwhelming degree (canonical Critical Hit rule). NOTE [DRIFT]: the worked
    example omits the crit doubling for that hit (base figure, not the doubled one); pass crit=False to reproduce it."""
    c = WEAPON_CLASSES[weapon_class]
    mult = str_multiplier(c["weight"], c["wtype"])
    wmod = armor_damage_mod(c["damage_class"], armor_tier)
    if crit:
        wmod = wmod * 2   # weapon modifier doubled  [canonical: combat_v30 §5 PP-211 Critical Hit]
    return int(net + strength * mult + wmod)


def targeted_line_armor(armor_tier, overwhelming=False):
    """Targeted-line (I-13b): recompute damage vs one armour tier lower; Overwhelming -> vs None.
    Explicit canon mapping Heavy->Light; Medium/Light downgrades drafted."""
    if overwhelming:
        return "none"
    return TARGETED_LINE_DOWNGRADE[armor_tier]


# ===== degree-of-success effect table (combat_v32_proposal §12.4 -- draft; magnitudes sim-tunable) =====
SUBACTION_EFFECTS = {
    "cut":          {"failure": "misses; exposed to counter", "partial": "glances; no wound", "success": "lands; wound check per damage formula", "overwhelming": "critical (weapon modifier doubled)"},      # [canonical: combat_v32_proposal §12.4 -- draft]
    "thrust":       {"failure": "misses; exposed to counter", "partial": "glances; no wound", "success": "lands; wound check per damage formula", "overwhelming": "critical (weapon modifier doubled)"},      # [canonical: combat_v32_proposal §12.4 -- draft]
    "press":        {"failure": "pushed back", "partial": "held; opponent +0.5 Ob next step", "success": "opponent off-line; aggressor +1D next step", "overwhelming": "opponent stance broken (forced to Phase 1)"},  # [canonical: combat_v32_proposal §12.4 -- draft]
    "wind":         {"failure": "slip; opponent gains Tactile read", "partial": "held bind position", "success": "bind improved; +1D next sub-action", "overwhelming": "bind controlled; opponent must break or accept disadvantage"},  # [canonical: combat_v32_proposal §12.4 -- draft]
    "yield":        {"failure": "overrun", "partial": "partial redirect", "success": "force redirected; opponent commit -1D", "overwhelming": "reversal; aggressor becomes initiator"},                          # [canonical: combat_v32_proposal §12.4 -- draft]
    "void":         {"failure": "caught by attack", "partial": "partial evasion (half consequence)", "success": "clean evasion", "overwhelming": "counter-position (free probe-depth commit next pass)"},        # [canonical: combat_v32_proposal §12.4 -- draft]
    "displace":     {"failure": "no movement", "partial": "half-zone shift", "success": "full zone displacement", "overwhelming": "opponent off-balance (Stance Pool reduced one pass)"},                       # [canonical: combat_v32_proposal §12.4 -- draft]
    "grip_change":  {"failure": "weapon dropped", "partial": "partial change (half-effective grip)", "success": "grip changed; new sub-action options surface", "overwhelming": "grip changed + free probe commit"},  # [canonical: combat_v32_proposal §12.4 -- draft]
    "break_bind":   {"failure": "bind held", "partial": "partial separation (still in bind)", "success": "bind broken; state -> Out-of-contact", "overwhelming": "clean break + free disengage to Phase 7"},     # [canonical: combat_v32_proposal §12.4 -- draft]
    "probe":        {"failure": "telegraphed; opponent +0.5 Ob", "partial": "light contact; no wound", "success": "probe lands; minor wound check", "overwhelming": "probe + counter info revealed"},            # [canonical: combat_v32_proposal §12.4 -- draft]
    "targeted_line":{"failure": "misses gap; slides off plate; exposed", "partial": "hits plate; armour not bypassed (glances)", "success": "gap hit; damage recomputed vs armour tier -1", "overwhelming": "deep gap thrust; recompute vs None + critical"},  # [canonical: combat_v32_proposal §12.4 -- draft (I-13b)]
}


def subaction_effect(subaction, degree_str):
    """Look up the §12.4 effect for a sub-action at a degree of success."""
    key = subaction
    if subaction in ("probe_cut", "probe_thrust"):
        key = "probe"
    if subaction in ("yield_to_bind",):
        key = "yield"
    if subaction in ("press_the_bind",):
        key = "press"
    if subaction in ("void_and_counter",):
        key = "void"
    return SUBACTION_EFFECTS.get(key, {}).get(degree_str)


# ============================== self-test ==============================
if __name__ == "__main__":
    checks = []
    rule = "================================================================"
    print("Module 4b (sub-action mechanics) -- validation against canon + §12.7 worked example")
    print(rule)

    # (a) Pool grammar reproduces the §12.7 worked example
    a_ok = (subaction_pool(5, 4, 3) == 17 and subaction_pool(3, 4, 3) == 13)  # [canonical: combat_v32_proposal §12.7 (Ilse Thrust (Agi5x2)+4+3=17; Press/Yield (3x2)+4+3=13)]
    checks.append(a_ok)
    print(f"\n(a) sub-action Pool grammar vs §12.7 (Thrust {subaction_pool(5,4,3)}=17; Press/Yield {subaction_pool(3,4,3)}=13): {'OK' if a_ok else 'FAIL'}")

    # (b) relevant-attribute branching (Yield=Foc, by-weight Cut, Displace composite)
    b_ok = (relevant_attr_value("yield", 5, 3, 3, "light") == 3
            and relevant_attr_value("cut", 5, 3, 3, "light") == 5
            and relevant_attr_value("cut", 5, 3, 3, "heavy") == 3
            and relevant_attr_value("displace", 6, 4, 3, "light") == 5)  # [canonical: combat_v32_proposal §12.2 -- draft (Yield=Foc; by-weight; Displace mean(Str,Agi))]
    checks.append(b_ok)
    print(f"(b) relevant-attribute (Yield->Foc, Cut by-weight, Displace mean(Str,Agi)): {'OK' if b_ok else 'FAIL'}")

    # (c) degree bands (combat_v30 §5 + §12.4)
    DEG = {(5,2):"overwhelming", (2,2):"success", (1,2):"partial", (0,2):"failure", (-1,2):"failure", (2,1):"success", (3,1):"overwhelming"}  # [canonical: combat_v30 §5 + combat_v32 §12.4 degree bands]
    c_ok = all(degree(net, ob) == v for (net, ob), v in DEG.items())
    checks.append(c_ok)
    print(f"(c) degree bands (Failure/Partial/Success/Overwhelming, net>=2*Ob and >=3): {'OK' if c_ok else 'FAIL'}")

    # (d) sigma-space Effective Ob reproduces the §12.3 worked conversion
    eff = effective_ob(2, 6, 1.5)  # [canonical: combat_v32_proposal §12.3 worked conversion (base Ob 2, Pool 6, net_sigma 1.5 -> -0.24 floored 0)]
    d_ok = (eff == 0)  # [canonical: combat_v32_proposal §12.3 (Effective Ob floored at 0)]
    checks.append(d_ok)
    print(f"(d) sigma-space Effective Ob (§12.3 worked: base 2, Pool 6, net_sigma 1.5 -> {eff}, floored 0): {'OK' if d_ok else 'FAIL'}")

    # (e) strike damage reproduces §12.7 step 3 (base, no crit) + canonical crit doubling
    base_dmg = strike_damage(5, 3, "single_short", "light", crit=False)  # [canonical: combat_v32_proposal §12.7 (net5 + Str3x1 + LightBlade-vs-Light +2 = 10)]
    crit_dmg = strike_damage(5, 3, "single_short", "light", crit=True)   # [canonical: combat_v30 §5 PP-211 crit doubles weapon mod -> 12]
    e_ok = (base_dmg == 10 and crit_dmg == 12)
    checks.append(e_ok)
    print(f"(e) strike damage: §12.7 base {base_dmg}=10 (example) / canonical crit {crit_dmg}=12 [DRIFT: example omits crit]: {'OK' if e_ok else 'FAIL'}")

    # (f) Targeted-line armour downgrade (explicit Heavy->Light; Overwhelming->None)
    f_ok = (targeted_line_armor("heavy") == "light"
            and targeted_line_armor("light") == "none"
            and targeted_line_armor("heavy", overwhelming=True) == "none")
    checks.append(f_ok)
    print(f"(f) Targeted-line armour (Heavy->Light, Light->None, Overwhelming->None): {'OK' if f_ok else 'FAIL'}")

    # (g) sigma-space state-gating (Stance Counter at Closing, drops In-bind; Tactile reading In-bind)
    g_ok = ("stance_counter" in live_modifiers("closing")
            and "stance_counter" not in live_modifiers("in_bind")
            and "tactile_reading" in live_modifiers("in_bind"))
    checks.append(g_ok)
    print(f"(g) state-gating (Stance Counter Closing-only; Tactile reading In-bind): {'OK' if g_ok else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad:
        print(f"RESULT: FAIL -- check indices failing: {bad}")
        raise SystemExit(1)
    print(f"RESULT: PASS -- all {len(checks)} checks match canon + spec "
          f"(Pool grammar §12.7, relevant-attr, degree bands, sigma-space §12.3, strike damage, Targeted-line, state-gating).")
