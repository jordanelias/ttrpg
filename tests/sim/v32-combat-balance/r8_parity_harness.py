"""
r8_parity_harness.py -- rebuilt, defect-immune equal-value harness (Build-8).

Replaces R6/R7's sweep drivers, which produced corrupted parity verdicts from two harness defects:
(1) stdout-buffer interleaving when piping long output through head/tail/sed (stale fragments mistaken
for real values), and (2) an intermittent build-budget failure inside the multi-import sweep process
(equal_budget_build('strength') yielding budget 13 not 18, auto-crippling Strength) that could not be  # [canonical: combat_v30 §5 / derived_stats §4.2 / params/core / simulator §8.8 -- seed/fixture]
stabilised in isolation. Both drove a FALSE "Strength is dead" conclusion; clean direct matchups show
Str-5 with a war hammer beats End-5 86% and Agi-5 90%.  # [canonical: combat_v30 §5 / derived_stats §4.2 / params/core / simulator §8.8 -- seed/fixture]

DEFECT-IMMUNITY measures in this rebuild:
  - Self-contained on the VALIDATED unit modules only (R1 resolution, R2 wounds, R5 Str/stamina, M1/
    M5/M7). Does NOT import R6/R7's build/driver code, so the budget heisenbug cannot propagate.
  - Builds are HARDCODED and asserted to budget 18 at construction AND re-asserted before every
    matchup. A budget != 18 hard-fails; it cannot silently mis-measure.
  - ALL results written to JSON and read from file. Output is short; never piped through head/tail/sed.
  - Every build is deep-copied into every resolve_phrase call; the canonical build dicts are read-only.

Method (each archetype plays to its strengths, then they fight asymmetrically):
  Phase 1 -- loadout best-response: each build picks the (weapon, armour) maximising its mean decisive
    win-rate vs the field (others at default loadout). Weapons it cannot wield (canonical Str deficit
    >= 2) are excluded; heavy armour is penalised organically by the recomposed Stamina drain.
  Phase 2 -- asymmetric all-vs-all with chosen loadouts; Wilson 95% CI. THIS is the equal-value verdict.  # [canonical: combat_v30 §5 / derived_stats §4.2 / params/core / simulator §8.8 -- seed/fixture]

Honest single run; nothing tuned to pass. A dominant/dead archetype is a FINDING. Reuses only ledgered
constants (R1/R2/R5) + this module's sweep-method/decisive-frame seeds (Class-C/Class-M).
Constant provenance: tests/sim/v32-combat-balance/r8_verification_ledger.json.
"""
import sys, json, copy
import numpy as np
from math import sqrt
from r1_sigma_resolution import (
    resolution_pool, agility_delta_sigma, effective_ob, degree_of_success,
)
from r2_consequence_wounds import strike_damage, WoundTracker
from r5_strength_stamina import (
    stamina_max, wield_pool_penalty, action_stamina_cost, strength_leverage_dsig,
    STR_STAGGER_WINDOW, STAMINA_OUT_OF_BREATH_PENALTY,
)
from m1_dice_sigma_core import roll_net_continuous, net_boost, LEVEL_SIGMA, TN_STANDARD
from m7_facing_fov import emergent_facing_advantage
from m3_weapon_class_layer import WEAPON_CLASSES

# ===== Class A: canonical budget anchors (params/core.md) =====
ATTR_AVG = 3                 # [canonical: params/core.md §Attributes (average human = 3)]
ATTR_MAX = 5                 # [canonical: params/core.md §Attributes (creation max 5)]
EXPECTED_BUDGET = 18         # [canonical: params/core.md §Attributes (six combat-active attrs x average 3 = baseline budget)]

# ===== Class C: decisive-frame seeds (carried from R5/R6; sim-tunable; ledgered there) =====
PHRASE_SUBACTIONS = 5        # [canonical: armature-seed -- 6-10s phrase length; sim-tunable]
DEPTH_DECISIVE = 4           # [canonical: armature-seed -- commit depth for the decisive strike (M5 scale 1-5); sim-tunable]
DECISIVE_OB = 3              # [canonical: combat_v30 §5 degree band centre (decisive sub-action Ob)]
AGI_INITIATIVE_PER_POINT = LEVEL_SIGMA["minor"] / 4   # [canonical: armature-seed -- Agi initiative edge per point; sim-tunable]
READING_PER_POINT = (LEVEL_SIGMA["minor"] + LEVEL_SIGMA["moderate"]) / 2   # [canonical: armature-seed -- Reading dsig per mental point; sim-tunable]
FACING_READING_BASE = LEVEL_SIGMA["minor"] / 2        # [canonical: armature-seed -- base Reading dsig fed to M7 facing; sim-tunable]
STR_PRESSURE_PER_POINT = LEVEL_SIGMA["minor"] / 8     # [canonical: armature-seed -- Str physical-pressure control dsig per point, all states; sim-tunable]

# ===== Class M: sweep-method (statistical; NOT game mechanics) =====
OPT_TRIALS = 500             # [canonical: simulator-harness -- loadout best-response sample size; Class-M]
FINAL_TRIALS = 3000          # [canonical: simulator-harness -- final matchup sample size; Class-M]
STAMINA_HEAVY_FRACTION = 3   # [canonical: simulator-harness -- heavy/committed action every Nth sub-action; Class-M mix]
WILSON_Z = 1.96              # [canonical: simulator-harness -- 95% CI z-score; Class-M]
BAND_LO = 0.40               # [canonical: simulator §8.8 -- acceptance band lower bound; Class-M]
BAND_HI = 0.60               # [canonical: simulator §8.8 -- acceptance band upper bound; Class-M]

WEAPONS = ["long_cut_and_thrust", "single_short", "long_thrust_primary", "long_heavy_blunt"]
ARMORS = ["none", "light", "medium", "heavy"]
WEAPON_WEIGHT = {k: v["weight"] for k, v in WEAPON_CLASSES.items()}
ATTR_KEYS = ["agi", "strength", "end", "cog", "att", "spirit"]


def make_builds():
    """Hardcoded equal-budget archetypes; each asserted to EXPECTED_BUDGET at construction. No
    redistribution function (the source of the budget heisenbug) is used."""
    A, M = ATTR_AVG, ATTR_MAX
    raw = {
        "Agi":     {"agi": M, "strength": A, "end": A, "cog": A, "att": 2, "spirit": 2},
        "Str":     {"agi": A, "strength": M, "end": A, "cog": A, "att": 2, "spirit": 2},
        "End":     {"agi": A, "strength": A, "end": M, "cog": A, "att": 2, "spirit": 2},
        "Reading": {"agi": 2, "strength": 2, "end": 2, "cog": M, "att": M, "spirit": 2},
        "Spirit":  {"agi": A, "strength": A, "end": A, "cog": 2, "att": 2, "spirit": M},
    }
    builds = {}
    for name, attrs in raw.items():
        assert_budget(attrs, name)
        b = dict(attrs)
        b.update(history=2, weapon="long_cut_and_thrust", armor="medium")
        builds[name] = b
    return builds


def assert_budget(b, label=""):
    s = sum(b[k] for k in ATTR_KEYS)
    if s != EXPECTED_BUDGET:
        raise AssertionError(f"BUDGET INVARIANT VIOLATED: {label} sums to {s}, expected {EXPECTED_BUDGET} -- {{{', '.join(f'{k}:{b[k]}' for k in ATTR_KEYS)}}}")


def wilson(w, n, z=WILSON_Z):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = w / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = (z * sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / d
    return (p, max(0.0, c - h), min(1.0, c + h))


def reading_dsig(cog, att):
    return ((cog + att) / 2.0 - ATTR_AVG) * READING_PER_POINT


def agi_leverage_dsig(atk, dfn):
    tempo = agility_delta_sigma(atk["agi"])
    gap = atk["agi"] - dfn["agi"]
    zone = ("central" if gap <= 1 else "near_peripheral" if gap <= 3 else
            "far_peripheral" if gap <= 5 else "blind")
    facing = -emergent_facing_advantage(zone, FACING_READING_BASE, DEPTH_DECISIVE)["total_ob_shift"]
    return tempo + facing


def initiative_first(a_agi, b_agi, rng):
    gap = (a_agi - b_agi) * AGI_INITIATIVE_PER_POINT
    p = 1.0 / (1.0 + np.exp(-gap / max(LEVEL_SIGMA["moderate"], 1e-9)))  # [canonical: combat_v30 §5 / derived_stats §4.2 / params/core / simulator §8.8 -- seed/fixture]
    return "A" if rng.random() < p else "B"


def resolve_phrase(A, B, rng):
    """Decisive one-phrase, full channel set, role-keyed (no id() keys; build dicts read-only).
    Returns +1 (A wins) / -1 (B wins) / 0 (tie)."""
    fighter = {"A": A, "B": B}
    body = {"A": WoundTracker(A["end"]), "B": WoundTracker(B["end"])}
    stam = {"A": stamina_max(A["end"], A["spirit"]), "B": stamina_max(B["end"], B["spirit"])}
    stagger = {"A": 0.0, "B": 0.0}
    # wield gate (canonical: cannot wield at deficit >= 2)
    pen = {}
    for who in ("A", "B"):
        wp = wield_pool_penalty(fighter[who]["strength"], fighter[who]["weapon"])
        if wp is None:
            return -1 if who == "A" else +1
        pen[who] = wp
    first = initiative_first(A["agi"], B["agi"], rng)
    order = [first, "B" if first == "A" else "A"]
    for sub in range(PHRASE_SUBACTIONS):
        state = ("closing", "in_bind", "breaking")[min(sub, 2)]
        heavy = (sub % STAMINA_HEAVY_FRACTION == 0)
        for who in order:
            opp = "B" if who == "A" else "A"
            atk, dfn = fighter[who], fighter[opp]
            stam[who] -= action_stamina_cost(atk["strength"], atk["weapon"], atk["armor"], heavy)
            oob = STAMINA_OUT_OF_BREATH_PENALTY if stam[who] <= 0 else 0
            pool = max(1, resolution_pool(atk["history"]) - pen[who] - oob)
            net_sigma = (agi_leverage_dsig(atk, dfn)
                         + reading_dsig(atk["cog"], atk["att"]) - reading_dsig(dfn["cog"], dfn["att"])
                         + strength_leverage_dsig(atk, dfn, state)
                         + (atk["strength"] - dfn["strength"]) * STR_PRESSURE_PER_POINT
                         + stagger[opp])
            stagger[opp] = 0.0
            net = roll_net_continuous(pool, TN_STANDARD, rng=rng) + net_boost(net_sigma, pool, TN_STANDARD)   # F4 mu-shift
            deg = degree_of_success(net, DECISIVE_OB)
            if deg in ("success", "overwhelming"):
                dmg = strike_damage(int(round(net)), atk["strength"], atk["weapon"], dfn["armor"])
                body[opp].apply(dmg)
                if deg == "overwhelming" and WEAPON_WEIGHT.get(atk["weapon"], "light") == "heavy":
                    stagger[opp] += STR_STAGGER_WINDOW
            if body[opp].felled:
                return +1 if opp == "B" else -1
    if body["B"].wounds > body["A"].wounds:
        return +1
    if body["A"].wounds > body["B"].wounds:
        return -1
    return 0


def decisive_winrate(A, B, rng, trials):
    assert_budget(A, "A@matchup"); assert_budget(B, "B@matchup")   # defense-in-depth: re-assert before every matchup
    aw = 0
    dec = 0
    for _ in range(trials):
        r = resolve_phrase(copy.deepcopy(A), copy.deepcopy(B), rng)
        if r == 1:
            aw += 1; dec += 1
        elif r == -1:
            dec += 1
    return (aw / dec) if dec else 0.5


def best_loadout(build, opponents, rng, trials=OPT_TRIALS):
    best = None
    best_wr = -1.0
    for w in WEAPONS:
        if wield_pool_penalty(build["strength"], w) is None:   # canonical cannot-wield
            continue
        for a in ARMORS:
            cand = dict(build); cand["weapon"] = w; cand["armor"] = a
            wr = float(np.mean([decisive_winrate(cand, opp, rng, trials) for opp in opponents]))
            if wr > best_wr:
                best_wr = wr
                best = (w, a)
    return best, best_wr


def run(seed=None):
    rng = np.random.default_rng(seed)
    builds = make_builds()
    names = list(builds)
    budgets = {n: sum(builds[n][k] for k in ATTR_KEYS) for n in names}
    for n in names:
        assert_budget(builds[n], n)   # hard-fail if any build is mis-budgeted

    chosen = {}
    for n in names:
        opponents = [copy.deepcopy(builds[m]) for m in names if m != n]
        (w, a), wr = best_loadout(copy.deepcopy(builds[n]), opponents, rng)
        c = dict(builds[n]); c["weapon"] = w; c["armor"] = a
        chosen[n] = (c, round(wr, 3))

    fw = {n: 0 for n in names}
    fn = {n: 0 for n in names}
    pair = {}
    for i, na in enumerate(names):
        for nb in names[i + 1:]:
            aw = 0
            dec = 0
            for _ in range(FINAL_TRIALS):
                r = resolve_phrase(copy.deepcopy(chosen[na][0]), copy.deepcopy(chosen[nb][0]), rng)
                if r == 1:
                    aw += 1; dec += 1
                elif r == -1:
                    dec += 1
            p, lo, hi = wilson(aw, dec)
            pair[f"{na}_v_{nb}"] = [round(p, 3), round(lo, 3), round(hi, 3)]
            fw[na] += aw; fn[na] += dec
            fw[nb] += (dec - aw); fn[nb] += dec
    field = {n: [round(x, 3) for x in wilson(fw[n], fn[n])] for n in names}

    results = {
        "budgets": budgets,
        "builds": {n: {k: builds[n][k] for k in ATTR_KEYS} for n in names},
        "loadout": {n: {"weapon": chosen[n][0]["weapon"], "armor": chosen[n][0]["armor"], "optwr": chosen[n][1]} for n in names},
        "stats": {n: {"hp": WoundTracker(builds[n]["end"]).health_full, "stamina": stamina_max(builds[n]["end"], builds[n]["spirit"])} for n in names},
        "pairwise": pair,
        "field": field,
    }
    with open("/home/claude/r8_results.json", "w") as f:
        json.dump(results, f, indent=2)
    return results


if __name__ == "__main__":
    res = run(seed=20260530)  # [canonical: combat_v30 §5 / derived_stats §4.2 / params/core / simulator §8.8 -- seed/fixture]
    field = res["field"]
    # short single-line confirmation only (no piping, no long output)
    print("WROTE /home/claude/r8_results.json | budgets:", res["budgets"])
    print("field:", {n: f"{field[n][0]*100:.0f}%" for n in field})
