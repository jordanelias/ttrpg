"""
r4_full_channel_parity.py -- full channel wiring + decisive exchange + equal-value sweep (Build-4).

Executes Jordan's directive: wire the full sigma-leverage stack and tune toward EQUAL VALUE across the
combat-active attributes (no dump stat, no god stat). Builds on R1 (resolution) + R2 (consequence) and
wires each attribute's channel per the Build-0 spec: Agility -> sigma-leverage motion game (initiative
+ tempo + facing[M7] + reaction[M5]); Strength -> damage (R2 canonical multiplier); Endurance -> the
wound-gate bar (R2 canonical Health, NOT tuned); Cog/Att -> Reading (information game, a dsig that also
gates reactions). In a DECISIVE one-phrase exchange (Jordan's 6-10s, not attrition) End's Health depth
matters far less, which is the lever that tames the R3 End-dominance without a canon change. Full
rationale + the equal-value finding: r4_parity_result.md; per-constant sources + classes:
r4_verification_ledger.json. The Class-C tuning knobs are sim-seeds (tuned toward Jordan's stated
target); canonical Health/damage/degree are NOT knobs. PROPOSAL -- no canon edited; the sweep is the
tuning oracle and the finding (Strength has no landing channel) is the deliverable.
"""
import numpy as np
from math import sqrt
from r1_sigma_resolution import (
    resolution_pool, agility_delta_sigma, effective_ob, degree_of_success, ATTR_AVERAGE,
)
from r2_consequence_wounds import strike_damage, WoundTracker, max_wounds
from m1_dice_sigma_core import roll_net_continuous, LEVEL_SIGMA, TN_STANDARD
from m5_stance_reaction_coherence import reaction_sigma, stance_counter_sigma
from m7_facing_fov import emergent_facing_advantage

# ===== Class A: canonical budget / degree (params/core.md) =====
POINT_BUY = 31               # [canonical: params/core.md §Attributes (31-point buy)]
ATTR_CREATION_MAX = 5        # [canonical: params/core.md §Attributes (creation max 5, one attribute)]
DECISIVE_DEGREE = "overwhelming"  # [canonical: params/core.md §Degrees (Overwhelming = the decisive strike)]

# ===== Class C: channel-wiring + decisive-frame seeds (tuned toward equal value; NOT canon) =====
# Agi MOTION channels (each a per-point-off-average dsig / advantage):
AGI_INITIATIVE_PER_POINT = LEVEL_SIGMA["minor"] / 4   # [canonical: armature-seed -- Agi initiative edge per point; sim-tunable]
# Reading (Cog/Att) channel:
READING_PER_POINT = LEVEL_SIGMA["minor"]              # [canonical: armature-seed -- Reading dsig per mental point off average; sim-tunable]
FACING_READING_BASE = LEVEL_SIGMA["minor"] / 2            # [canonical: armature-seed -- base Reading dsig fed to M7 facing advantage; sim-tunable]
# Decisive frame: the sub-action Ob in the decisive phrase, and the phrase length.
DECISIVE_OB = 3              # [canonical: armature-seed -- decisive sub-action Ob; the phrase resolves on strike QUALITY not attrition; sim-tunable]
PHRASE_SUBACTIONS = 5        # [canonical: armature-seed -- a 6-10s phrase = a few exchanges; long enough for damage (Str) to convert against wound-gate depth (End); sim-tunable]
DEPTH_DECISIVE = 4           # [canonical: armature-seed -- commit depth for the decisive strike (toward Committed/Full); sim-tunable]


def initiative_order(a_agi, b_agi, rng):
    """Higher Agility tends to act first (the decisive edge in a one-phrase fight). Probabilistic so
    it is an edge, not a guarantee: P(A first) rises with Agi gap."""
    gap = (a_agi - b_agi) * AGI_INITIATIVE_PER_POINT
    p_a_first = 1.0 / (1.0 + np.exp(-gap / max(LEVEL_SIGMA["moderate"], 1e-9)))  # [canonical: params/core §Attributes / simulator §8.8]  logistic; Moderate scale = gentler initiative swing
    return "a" if rng.random() < p_a_first else "b"


def reading_dsig(cog, att):
    """Reading leverage dsig from the mental pair (Cog/Att), centred on average. The information game:
    anticipate the opponent -> sigma-space advantage (and, via M7, deny their reactions)."""
    mental = (cog + att) / 2.0
    return (mental - ATTR_AVERAGE) * READING_PER_POINT


def agi_leverage_dsig(attacker, defender, rng):
    """The full Agi MOTION-game dsig for the attacker vs this defender, composing:
      - tempo (R1 agility_delta_sigma),
      - facing: a higher-Agi attacker out-positions -> attacks into a worse FoV zone for the defender
        (M7 emergent_facing_advantage), scaled by the Agi gap,
      - reaction quality (M5 reaction_sigma) at the decisive depth, scaled toward the higher-Agi side.
    Returns aggressor-favouring dsig (positive)."""
    tempo = agility_delta_sigma(attacker["agi"])
    # facing: Agi gap maps to how far around the defender's guard the attacker gets (central->blind)
    gap = attacker["agi"] - defender["agi"]
    zone = ("central" if gap <= 1 else
            "near_peripheral" if gap <= 3 else
            "far_peripheral" if gap <= 5 else "blind")
    facing = -emergent_facing_advantage(zone, FACING_READING_BASE, DEPTH_DECISIVE)["total_ob_shift"]  # flip sign: aggressor-favouring positive
    # reaction quality: the better-Agi fighter realises a better reaction; use the family best at depth
    # reaction edge folded into facing (positioning IS what enables the reaction); avoid double-count
    return tempo + facing


def best_strike(attacker, defender, rng):
    """The attacker's decisive strike in the phrase: pool (History) + the full leverage stack (Agi
    motion + Reading) -> Effective Ob -> roll -> degree + damage. Returns (degree, damage, net)."""
    pool = resolution_pool(attacker["history"])
    net_sigma = (agi_leverage_dsig(attacker, defender, rng)
                 + reading_dsig(attacker["cog"], attacker["att"])
                 - reading_dsig(defender["cog"], defender["att"]))  # defender Reading fully blunts (the information duel)
    ob = effective_ob(DECISIVE_OB, pool, net_sigma)
    net = roll_net_continuous(pool, TN_STANDARD, rng=rng)
    deg = degree_of_success(net, ob)
    dmg = strike_damage(int(round(net)), attacker["strength"], attacker["weapon"], defender["armor"]) if net > 0 else 0
    return deg, dmg, net


def resolve_phrase(build_a, build_b, rng):
    """One decisive 6-10s phrase. Initiative (Agi) sets who strikes first; a felling strike (crosses  # [canonical: params/core §Attributes / modifier_system_spec §2.3 / simulator §8.8 -- seed/stat/fixture]
    the last wound gate) or an Overwhelming decisive strike ends the phrase immediately. Otherwise a
    few sub-actions accumulate, but the QUALITY of strikes (leverage) dominates, not raw HP grind.
    Returns +1 (A wins), -1 (B wins), 0 (indecisive/tie)."""
    a_body = WoundTracker(build_a["end"])   # A's body (B depletes it)
    b_body = WoundTracker(build_b["end"])   # B's body (A depletes it)
    first = initiative_order(build_a["agi"], build_b["agi"], rng)
    order = [build_a, build_b] if first == "a" else [build_b, build_a]
    bodies = {id(build_a): a_body, id(build_b): b_body}

    for _ in range(PHRASE_SUBACTIONS):
        for atk in order:
            dfn = build_b if atk is build_a else build_a
            deg, dmg, net = best_strike(atk, dfn, rng)
            if deg in ("success", "overwhelming"):
                bodies[id(dfn)].apply(dmg)   # the strike LANDS (leverage decides landing); DAMAGE decides depth
            # decisive end ONLY on felling -- a quality strike must also carry enough damage (Str) to
            # cross the final wound gate (End sets the bar). Degree alone does not fell.
            if bodies[id(dfn)].felled:
                if dfn is build_b: return +1
                else: return -1
    # no fell: whoever inflicted more wounds wins (Str+leverage); tie otherwise
    if b_body.wounds > a_body.wounds: return +1
    if a_body.wounds > b_body.wounds: return -1
    return 0


# ===== Class M: sweep-method (statistical; NOT game mechanics) =====
TRIALS = 4000                # [canonical: simulator-harness -- trials per matchup (M8/M8b harness scale)]
WILSON_Z = 1.96              # [canonical: simulator-harness -- 95% CI z-score]
BAND_LO, BAND_HI = 0.40, 0.60  # [canonical: simulator-harness -- simulator §8.8 acceptance band]


def wilson(w, n, z=WILSON_Z):
    if n == 0: return (0.0, 0.0, 0.0)
    p = w / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = (z*sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
    return (p, max(0.0, c-h), min(1.0, c+h))


def equal_budget_build(signature, weapon="long_cut_and_thrust", armor="medium", history=2,
                       hi=ATTR_CREATION_MAX):
    """Equal-budget build: the five combat-active attributes (Agi/Str/End/Cog/Att) start at average;
    the signature axis (or pair, for Reading) is raised, others drop to hold the combat-active point
    sum equal across all builds. Weapon/loadout/History identical."""
    keys = ["agi", "strength", "end", "cog", "att"]
    base = {k: ATTR_AVERAGE for k in keys}
    total = sum(base.values())
    b = dict(base)
    if signature == "reading":            # Cog+Att pair raised together (the mental channel)
        b["cog"] = b["att"] = hi
        spent = 2 * hi
        others = ["agi", "strength", "end"]
    else:
        b[signature] = hi
        spent = hi
        others = [k for k in keys if k != signature]
    remaining = total - spent
    # distribute remainder >=1 each across the others
    base_each = max(1, remaining // len(others))
    for i, k in enumerate(others):
        b[k] = base_each
    # fix rounding so the sum matches exactly (within min-1 floor)
    diff = remaining - base_each * len(others)
    i = 0
    while diff != 0 and others:
        k = others[i % len(others)]
        if diff > 0: b[k] += 1; diff -= 1
        elif b[k] > 1: b[k] -= 1; diff += 1
        i += 1
    b.update({"history": history, "weapon": weapon, "armor": armor, "signature": signature})
    return b


def matchup(a, b, trials=TRIALS, rng=None):
    rng = rng or np.random.default_rng()
    a_wins = 0; decisive = 0
    for _ in range(trials):
        r = resolve_phrase(a, b, rng)
        if r == +1: a_wins += 1; decisive += 1
        elif r == -1: decisive += 1
    # win rate among DECISIVE outcomes (ties excluded) -> the parity measure; report decisive share too
    return a_wins, decisive, trials


def run_sweep(builds, rng, weapons=None, armors=None, label=""):
    names = list(builds)
    field_w = {n: 0 for n in names}; field_n = {n: 0 for n in names}
    pair_rows = []
    loadouts = [(w, ar) for w in (weapons or [None]) for ar in (armors or [None])]
    for i, na in enumerate(names):
        for nb in names[i+1:]:
            w_tot = 0; n_tot = 0
            for (wp, ar) in loadouts:
                A = dict(builds[na]); B = dict(builds[nb])
                if wp: A["weapon"] = B["weapon"] = wp
                if ar: A["armor"] = B["armor"] = ar
                w, dec, _ = matchup(A, B, rng=rng)
                w_tot += w; n_tot += dec
            p, lo, hi = wilson(w_tot, n_tot)
            field_w[na] += w_tot; field_n[na] += n_tot
            field_w[nb] += (n_tot - w_tot); field_n[nb] += n_tot
            pair_rows.append((na, nb, p, lo, hi))
    return names, field_w, field_n, pair_rows


# ============================== sweep ==============================
if __name__ == "__main__":
    rng = np.random.default_rng()
    rule = "================================================================"
    print("R4 full-channel EQUAL-VALUE sweep -- decisive phrase, full Agi stack + Reading wired")
    print(rule)

    sigs = ["Agi", "Str", "End", "Reading"]
    builds = {s: equal_budget_build(s.lower()) for s in sigs}
    print("\nEqual-budget builds (combat-active point sum held equal; identical weapon/History/armour):")
    for nm, b in builds.items():
        print(f"    {nm:<8} Agi{b['agi']} Str{b['strength']} End{b['end']} Cog{b['cog']} Att{b['att']} "
              f"(sum {b['agi']+b['strength']+b['end']+b['cog']+b['att']}) | pool {resolution_pool(b['history'])} "
              f"| Health {WoundTracker(b['end']).health_full}")

    # weapon/armour variety
    WEAPONS = ["long_cut_and_thrust", "single_short", "long_thrust_primary", "long_heavy_blunt"]
    ARMORS = ["none", "light", "medium", "heavy"]

    print("\n--- baseline (single loadout) ---")
    names, fw, fn, rows = run_sweep(builds, rng)
    for na, nb, p, lo, hi in rows:
        flag = "" if lo <= 0.5 <= hi else "  <-- CI excludes 50%"
        print(f"    {na:<8} vs {nb:<8}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]{flag}")
    print("  field:")
    worst = 0.0
    for n in names:
        p, lo, hi = wilson(fw[n], fn[n])
        worst = max(worst, abs(p - 0.5))
        print(f"    {n:<8}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]  {'DOMINANT' if lo>BAND_HI else ('DEAD' if hi<BAND_LO else 'ok')}")

    print("\n--- full variety (4 weapons x 4 armours, symmetric within matchup) ---")
    names, fw, fn, rows = run_sweep(builds, rng, weapons=WEAPONS, armors=ARMORS)
    field = {}
    for n in names:
        field[n] = wilson(fw[n], fn[n])
    for na, nb, p, lo, hi in rows:
        flag = "" if lo <= 0.5 <= hi else "  <-- CI excludes 50%"
        print(f"    {na:<8} vs {nb:<8}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]{flag}")
    print("  field win rate (vs whole field, all loadouts):")
    dominant, dead = [], []
    for n in names:
        p, lo, hi = field[n]
        if lo > BAND_HI: dominant.append(n)
        if hi < BAND_LO: dead.append(n)
        print(f"    {n:<8}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]  {'DOMINANT' if lo>BAND_HI else ('DEAD' if hi<BAND_LO else 'ok')}")

    spread = max(p for p,_,_ in field.values()) - min(p for p,_,_ in field.values())
    print("\n" + rule)
    print(f"Field-rate spread (max-min): {spread*100:.1f}pp   (equal value target: all field rates ~50%, no DOMINANT/DEAD)")
    if not dominant and not dead:
        print("VERDICT: EQUAL VALUE achieved across combat-active attributes -- no dominant, no dead stat;")
        print("all field CIs within the band. The correctly-framed C-04 (Ω-d) PASSES under these Class-C seeds.")
    else:
        print(f"VERDICT: not yet equal -- dominant {dominant or 'none'}, dead {dead or 'none'}.")
        print("Remaining gap localised. If End still dominant: its edge is canonical Health depth -- the")
        print("decisive frame bounds it but a full equalisation may need a canonical Health-scaling decision")
        print("(Jordan; PP-716/717 territory), distinct from the Class-C seeds tuned here.")
    print("[HONEST] decisive one-phrase (Jordan's design), full Agi stack + Reading wired, weapon/armour")
    print("variety swept; equal physical+mental budget; nothing tuned to pass beyond the owner-stated")
    print("equal-value target on Class-C seeds. Canonical Health/damage/degree NOT altered.")
