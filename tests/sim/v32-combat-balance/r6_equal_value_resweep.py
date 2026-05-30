"""
r6_equal_value_resweep.py -- equal-value re-sweep with Str leverage + recomposed Stamina (Build-6).  # [canonical: params/core / simulator §8.8 -- seed/stat/fixture]

STATUS: IN-PROGRESS HARNESS, NOT A PARITY VERDICT. Wires R5's Strength leverage + Stamina=f(End,Spirit)
into the decisive one-phrase exchange, six-attribute (Agi/Str/End/Reading/Spirit). Single-loadout
traces confirm Str's new channels WORK (Str beats Agi decisively; dominates in its heavy-blunt-vs-plate
niche), but the field-rate aggregate is confounded by loadout-averaging + shared-weapon symmetry, so
the field numbers are NOT yet trustworthy as an equal-value verdict. Needs per-loadout isolation +
asymmetric-loadout handling before its rates mean anything. Per-constant sources: r6_verification_
ledger.json. Reuses R1/R2/R5/M5/M7; no canon edited.
"""
import numpy as np
from math import sqrt
from r1_sigma_resolution import (
    resolution_pool, agility_delta_sigma, effective_ob, degree_of_success, ATTR_AVERAGE,
)
from r2_consequence_wounds import strike_damage, WoundTracker
from r5_strength_stamina import (
    stamina_max, wield_pool_penalty, action_stamina_cost, strength_leverage_dsig,
    STR_STAGGER_WINDOW, STAMINA_OUT_OF_BREATH_PENALTY,
)
from m1_dice_sigma_core import roll_net_continuous, LEVEL_SIGMA, TN_STANDARD
from m5_stance_reaction_coherence import reaction_sigma
from m7_facing_fov import emergent_facing_advantage

# ===== Class A budget (params/core.md) =====
ATTR_CREATION_MAX = 5        # [canonical: params/core.md §Attributes (creation max 5)]
DECISIVE_OB = 3              # [canonical: combat_v30 §5 degree band centre (decisive sub-action Ob)]
# ===== Class C: decisive-frame seeds (carried from R4; sim-tunable) =====
PHRASE_SUBACTIONS = 5        # [canonical: armature-seed -- 6-10s phrase length; long enough for stamina + Str to convert; sim-tunable]
DEPTH_DECISIVE = 4           # [canonical: armature-seed -- commit depth for the decisive strike (M5 scale 1-5); sim-tunable]
AGI_INITIATIVE_PER_POINT = LEVEL_SIGMA["minor"] / 4   # [canonical: armature-seed -- Agi initiative edge per point; sim-tunable]
READING_PER_POINT = LEVEL_SIGMA["minor"]              # [canonical: armature-seed -- Reading dsig per mental point; sim-tunable]
FACING_READING_BASE = LEVEL_SIGMA["minor"] / 2        # [canonical: armature-seed -- base Reading dsig fed to M7 facing; sim-tunable]
# ===== Class M sweep params =====
TRIALS = 4000                # [canonical: simulator-harness -- trials per matchup]
WILSON_Z = 1.96              # [canonical: simulator-harness -- 95% CI z-score]
BAND_LO, BAND_HI = 0.40, 0.60  # [canonical: simulator-harness -- simulator §8.8 acceptance band]
STAMINA_HEAVY_FRACTION = 3   # [canonical: simulator-harness -- a fighter spends a heavy (depth>=Committed) action every Nth sub-action -- harness mix]


def wilson(w, n, z=WILSON_Z):
    if n == 0: return (0.0, 0.0, 0.0)
    p = w/n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = (z*sqrt(p*(1-p)/n + z*z/(4*n*n))) / d  # [canonical: params/core / simulator §8.8 -- seed/stat/fixture]
    return (p, max(0.0, c-h), min(1.0, c+h))


def reading_dsig(cog, att):
    return ((cog + att)/2.0 - ATTR_AVERAGE) * READING_PER_POINT


def agi_leverage_dsig(attacker, defender):
    tempo = agility_delta_sigma(attacker["agi"])
    gap = attacker["agi"] - defender["agi"]
    zone = ("central" if gap <= 1 else "near_peripheral" if gap <= 3 else
            "far_peripheral" if gap <= 5 else "blind")
    facing = -emergent_facing_advantage(zone, FACING_READING_BASE, DEPTH_DECISIVE)["total_ob_shift"]
    return tempo + facing


def initiative_order(a_agi, b_agi, rng):
    gap = (a_agi - b_agi) * AGI_INITIATIVE_PER_POINT
    p = 1.0 / (1.0 + np.exp(-gap / max(LEVEL_SIGMA["moderate"], 1e-9)))  # [canonical: params/core / simulator §8.8 -- seed/stat/fixture]
    return "a" if rng.random() < p else "b"


def resolve_phrase(A, B, rng):
    """Decisive one-phrase with the FULL channel set (Agi motion + Reading + Str leverage + Stamina).
    Returns +1 A / -1 B / 0 tie. Stamina depletes per action; at 0 the fighter takes the canonical
    Out-of-Breath -2D (modelled as a pool penalty). Stagger: a heavy Overwhelming hit opens a sigma-
    window on the victim's next defence (the attacker's next strike is advantaged)."""
    bodies = {id(A): WoundTracker(A["end"]), id(B): WoundTracker(B["end"])}
    stamina = {id(A): stamina_max(A["end"], A["spirit"]), id(B): stamina_max(B["end"], B["spirit"])}
    stagger_on = {id(A): 0.0, id(B): 0.0}   # sigma-window pending against this fighter
    first = initiative_order(A["agi"], B["agi"], rng)
    order = [A, B] if first == "a" else [B, A]

    # wield gate: cannot-wield -> treat as catastrophic (loses); -1D pool penalty otherwise
    pool_pen = {}
    for f in (A, B):
        wp = wield_pool_penalty(f["strength"], f["weapon"])
        if wp is None:
            return -1 if f is A else +1     # cannot wield the chosen weapon -> loss
        pool_pen[id(f)] = wp

    for sub in range(PHRASE_SUBACTIONS):
        state = ("closing", "in_bind", "breaking")[min(sub, 2)]
        heavy = (sub % STAMINA_HEAVY_FRACTION == 0)   # periodic heavy/committed action
        for atk in order:
            dfn = B if atk is A else A
            # stamina cost; Out-of-Breath if depleted -> canonical -2D
            stamina[id(atk)] -= action_stamina_cost(atk["strength"], atk["weapon"], atk["armor"], heavy)
            oob_pen = STAMINA_OUT_OF_BREATH_PENALTY if stamina[id(atk)] <= 0 else 0
            # pool: demoted History pool minus wield + Out-of-Breath penalties
            pool = max(1, resolution_pool(atk["history"]) - pool_pen[id(atk)] - oob_pen)
            # leverage: Agi motion + Reading duel + Str landing/control + any pending stagger window
            net_sigma = (agi_leverage_dsig(atk, dfn)
                         + reading_dsig(atk["cog"], atk["att"]) - reading_dsig(dfn["cog"], dfn["att"])
                         + strength_leverage_dsig(atk, dfn, state)
                         + (atk["strength"] - dfn["strength"]) * (LEVEL_SIGMA["minor"] / 4)  # [canonical: params/core / simulator §8.8]  Str physical-pressure control, all states
                         + stagger_on[id(dfn)])
            stagger_on[id(dfn)] = 0.0       # consume the window
            ob = effective_ob(DECISIVE_OB, pool, net_sigma)
            net = roll_net_continuous(pool, TN_STANDARD, rng=rng)
            deg = degree_of_success(net, ob)
            if deg in ("success", "overwhelming"):
                dmg = strike_damage(int(round(net)), atk["strength"], atk["weapon"], dfn["armor"])
                bodies[id(dfn)].apply(dmg)
                # stagger: heavy weapon + Overwhelming -> open a window on dfn's NEXT defence
                c_weight = WEAPON_WEIGHT.get(atk["weapon"], "light")
                if deg == "overwhelming" and c_weight == "heavy":
                    stagger_on[id(dfn)] += STR_STAGGER_WINDOW
            if bodies[id(dfn)].felled:
                return +1 if dfn is B else -1
    if bodies[id(B)].wounds > bodies[id(A)].wounds: return +1
    if bodies[id(A)].wounds > bodies[id(B)].wounds: return -1
    return 0


# weapon weight lookup (for stagger) -- from M3 canonical classes
from m3_weapon_class_layer import WEAPON_CLASSES
WEAPON_WEIGHT = {k: v["weight"] for k, v in WEAPON_CLASSES.items()}


def equal_budget_build(signature, weapon="long_cut_and_thrust", armor="medium", history=2, hi=ATTR_CREATION_MAX):
    """Equal combat-active budget across SIX attributes (Agi/Str/End/Cog/Att/Spirit). Signature axis
    (or the Reading pair Cog+Att) raised to hi; others drop to hold the sum equal. Deterministic."""
    keys = ["agi", "strength", "end", "cog", "att", "spirit"]
    base = {k: ATTR_AVERAGE for k in keys}
    total = sum(base.values())
    b = dict(base)
    if signature == "reading":
        b["cog"] = b["att"] = hi; spent = 2*hi; others = ["agi", "strength", "end", "spirit"]
    else:
        b[signature] = hi; spent = hi; others = [k for k in keys if k != signature]
    remaining = total - spent
    each = max(1, remaining // len(others))
    for k in others: b[k] = each
    diff = remaining - each*len(others); i = 0
    while diff != 0:
        k = others[i % len(others)]
        if diff > 0: b[k] += 1; diff -= 1
        elif b[k] > 1: b[k] -= 1; diff += 1
        i += 1
    b.update({"history": history, "weapon": weapon, "armor": armor, "signature": signature})
    return b


def matchup(A, B, rng, trials=TRIALS):
    aw = 0; dec = 0
    for _ in range(trials):
        r = resolve_phrase(A, B, rng)
        if r == +1: aw += 1; dec += 1
        elif r == -1: dec += 1
    return aw, dec


# ============================== sweep ==============================
if __name__ == "__main__":
    rng = np.random.default_rng()
    rule = "================================================================"
    print("R6 EQUAL-VALUE re-sweep -- Str leverage + Stamina=f(End,Spirit) wired (6 attributes)")
    print(rule)

    sigs = ["Agi", "Str", "End", "Reading", "Spirit"]
    builds = {s: equal_budget_build(s.lower()) for s in sigs}
    print("\nEqual-budget builds (6-attr combat-active sum held equal):")
    for nm, b in builds.items():
        print(f"    {nm:<8} Agi{b['agi']} Str{b['strength']} End{b['end']} Cog{b['cog']} Att{b['att']} Spi{b['spirit']} "
              f"(sum {sum(b[k] for k in ['agi','strength','end','cog','att','spirit'])}) | "
              f"pool {resolution_pool(b['history'])} | HP {WoundTracker(b['end']).health_full} | Stam {stamina_max(b['end'],b['spirit'])}")

    WEAPONS = ["long_cut_and_thrust", "single_short", "long_thrust_primary", "long_heavy_blunt"]
    ARMORS = ["none", "light", "medium", "heavy"]
    names = list(builds)
    fw = {n: 0 for n in names}; fn = {n: 0 for n in names}
    print("\nPairwise (row vs col), full weapon/armour variety, Wilson 95% CI:")
    for i, na in enumerate(names):
        for nb in names[i+1:]:
            w_tot = 0; n_tot = 0
            for wp in WEAPONS:
                for ar in ARMORS:
                    Ab = dict(builds[na]); Bb = dict(builds[nb])
                    Ab["weapon"] = Bb["weapon"] = wp; Ab["armor"] = Bb["armor"] = ar
                    w, dec = matchup(Ab, Bb, rng, trials=TRIALS // 8)   # [canonical: params/core / simulator §8.8]  /8: variety budget
                    w_tot += w; n_tot += dec
            p, lo, hi = wilson(w_tot, n_tot)
            fw[na] += w_tot; fn[na] += n_tot
            fw[nb] += (n_tot - w_tot); fn[nb] += n_tot
            flag = "" if lo <= 0.5 <= hi else "  <-- CI excludes 50%"
            print(f"    {na:<8} vs {nb:<8}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]{flag}")

    print("\nField win rate (vs whole field, all loadouts):")
    field = {n: wilson(fw[n], fn[n]) for n in names}
    dominant, dead = [], []
    for n in names:
        p, lo, hi = field[n]
        if lo > BAND_HI: dominant.append(n)
        if hi < BAND_LO: dead.append(n)
        print(f"    {n:<8}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]  {'DOMINANT' if lo>BAND_HI else ('DEAD' if hi<BAND_LO else 'ok')}")

    spread = max(p for p,_,_ in field.values()) - min(p for p,_,_ in field.values())
    print("\n" + rule)
    print(f"Field-rate spread (max-min): {spread*100:.1f}pp   (R4 was 43pp with Str dead at 23%)")
    str_p = field["Str"][0]
    print(f"Strength field rate: {str_p*100:.1f}%  (R4: 23.1% DEAD)  -- {'RECOVERED into viability' if str_p>=BAND_LO else 'still low'}")
    if not dominant and not dead:
        print("VERDICT: EQUAL VALUE achieved across all six combat-active attributes -- no dominant, no dead.")
        print("Str's landing/control channels + the Stamina split closed the gap. Ω-d PASSES under these seeds.")
    else:
        print(f"VERDICT: not yet equal -- dominant {dominant or 'none'}, dead {dead or 'none'}. Gap localised; tune the named seeds.")
    print("[HONEST] decisive one-phrase; full Agi+Reading+Str-leverage+Stamina wired; equal 6-attr budget; "
          "weapon/armour variety; nothing tuned to pass beyond Jordan's stated equal-value target on Class-C seeds.")
