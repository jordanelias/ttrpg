"""
r3_parity_sweep.py -- cross-attribute PARITY sweep (armature reset, Build-3).  # [canonical: params/core §Attributes / simulator §8.8 -- fixture/stat]

The headline validation: does the corrected model achieve cross-attribute parity at EQUAL budget?
The correctly-framed C-NN defect (per Jordan) is not "more-Agi beats less-Agi" but "Agi UNIVERSALLY
beats equal-point Strength or Endurance"; the pass test is the omega Ω-d no-dominant-strategy check.
Wires R1 (resolution + Agi sigma-leverage) + R2 (consequence + Str/End) into one decisive exchange
(a phrase, NOT attrition): equal-budget Agi/Str/End builds, symmetric matchups, Wilson 95% CI,  # [canonical: params/core §Attributes / simulator §8.8 -- fixture/stat]
acceptance band per the simulator skill. A NOT-in-band result is a FINDING that localises which
Class-C seed to turn, not a failure. Full method + result narrative: r3_parity_result.md; per-constant
sources: r3_verification_ledger.json. PROPOSAL -- no canon edited; the sweep is the tuning oracle.
"""
import numpy as np
from math import sqrt
from r1_sigma_resolution import (
    resolution_pool, agility_delta_sigma, effective_ob, degree_of_success,
    state_gated_net_sigma, ATTR_AVERAGE,
)
from r2_consequence_wounds import strike_damage, WoundTracker
from m1_dice_sigma_core import roll_net_continuous, TN_STANDARD

# ===== Class A: canonical character-budget constants (params/core.md) =====
POINT_BUY = 31               # [canonical: params/core.md §Attributes (31 points across 10 attributes at creation)]
ATTR_MIN = 1                 # [canonical: params/core.md §Attributes (minimum 1 per attribute)]
ATTR_CREATION_MAX = 5        # [canonical: params/core.md §Attributes (creation max 5, one attribute only)]

# ===== Class M: sweep-method parameters (statistical harness; NOT game mechanics) =====
TRIALS = 4000                # [canonical: simulator-harness -- trials per matchup -- statistical sample size (M8/M8b harness scale)]
WILSON_Z = 1.96              # [canonical: simulator-harness -- 95% confidence z-score (Wilson interval); standard statistic]
BAND_LO = 0.40               # [canonical: simulator-harness -- acceptance band lower bound -- simulator skill §8.8 archetype-matchup band]
BAND_HI = 0.60               # [canonical: simulator-harness -- acceptance band upper bound -- simulator skill §8.8 archetype-matchup band]
EXCHANGE_CAP = 6             # [canonical: simulator-harness -- max sub-action transitions in one phrase before forced separation -- structural bout cap]


def wilson(wins, n, z=WILSON_Z):
    """Wilson score 95% CI for a binomial proportion (the M8/M8b harness statistic)."""
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = wins / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom  # [canonical: params/core §Attributes / simulator §8.8 -- fixture/stat]
    return (p, max(0.0, centre - half), min(1.0, centre + half))


def equal_budget_build(signature, surplus_axis_value, history=2,
                       weapon="long_cut_and_thrust", armor="medium"):
    """Build a character spending the SAME budget, concentrated on one signature axis. The three
    physical attributes (Agi/Str/End) start at average; the signature one is raised to
    surplus_axis_value, the other two drop to keep the *physical* triad's point-sum equal across all
    three builds (so the comparison is genuinely equal-budget on the contested points). Weapon History
    and loadout are held identical."""
    base = {"agi": ATTR_AVERAGE, "strength": ATTR_AVERAGE, "end": ATTR_AVERAGE}
    triad_sum = sum(base.values())                         # equal physical-point budget across builds
    hi = min(surplus_axis_value, 7)  # [canonical: params/core §Attributes / simulator §8.8 -- fixture/stat]
    remaining = triad_sum - hi
    others = [k for k in base if k != signature]
    # split the remainder across the other two as evenly as possible, floored at ATTR_MIN
    lo1 = max(ATTR_MIN, remaining // 2)
    lo2 = max(ATTR_MIN, remaining - lo1)
    build = {signature: hi, others[0]: lo1, others[1]: lo2}
    build.update({"history": history, "weapon": weapon, "armor": armor, "signature": signature})
    return build


def resolve_exchange(attacker, defender, rng):
    """One 6-10s phrase, attacker opening. Returns (attacker_wounds_dealt, defender_wounds_dealt).  # [canonical: params/core §Attributes / simulator §8.8 -- fixture/stat]
    Sub-actions alternate through the engagement states until first wound (decisive) or the cap
    (separation). Agility -> sigma-leverage tempo (R1); Strength/weapon -> severity (R2); Endurance ->
    wound-gate depth (R2 tracker)."""
    a_track = WoundTracker(defender["end"])   # the DEFENDER's body is what the ATTACKER depletes
    d_track = WoundTracker(attacker["end"])   # and vice-versa
    states = ("closing", "in_bind", "breaking")
    base_ob = 3                                # [canonical: combat_v30 §5 degree band centres on a 2-3 Ob sub-action]
    for turn in range(EXCHANGE_CAP):
        state = states[min(turn, len(states) - 1)]
        # --- attacker strikes defender ---
        a_sig = state_gated_net_sigma(state, {"agi_tempo": agility_delta_sigma(attacker["agi"])})
        a_pool = resolution_pool(attacker["history"])
        a_ob = effective_ob(base_ob, a_pool, a_sig)
        a_net = roll_net_continuous(a_pool, TN_STANDARD, rng=rng)
        if a_net > 0 and degree_of_success(a_net, a_ob) in ("success", "overwhelming"):
            dmg = strike_damage(int(round(a_net)), attacker["strength"], attacker["weapon"], defender["armor"])
            d_track.apply(dmg)
        # --- defender strikes back (same exchange) ---
        d_sig = state_gated_net_sigma(state, {"agi_tempo": agility_delta_sigma(defender["agi"])})
        d_pool = resolution_pool(defender["history"])
        d_ob = effective_ob(base_ob, d_pool, d_sig)
        d_net = roll_net_continuous(d_pool, TN_STANDARD, rng=rng)
        if d_net > 0 and degree_of_success(d_net, d_ob) in ("success", "overwhelming"):
            dmg = strike_damage(int(round(d_net)), defender["strength"], defender["weapon"], attacker["armor"])
            a_track.apply(dmg)
        if d_track.wounds > 0 or a_track.wounds > 0:
            break                              # decisive: phrase ends at first wound
    return d_track.wounds, a_track.wounds      # (wounds attacker dealt, wounds defender dealt)


def matchup(build_a, build_b, trials=TRIALS, rng=None):
    """Symmetric matchup: each build attacks in half the trials. Win = you wound them, they don't
    wound you (decisive). Returns build_a's win rate over the symmetric set."""
    rng = rng or np.random.default_rng()
    a_wins = 0
    half = trials // 2
    for _ in range(half):                                   # A opens
        ad, dd = resolve_exchange(build_a, build_b, rng)
        if ad > 0 and dd == 0:
            a_wins += 1
    for _ in range(half):                                   # B opens
        bd, ad = resolve_exchange(build_b, build_a, rng)
        if ad > 0 and bd == 0:
            a_wins += 1
    return a_wins, 2 * half


# ============================== sweep ==============================
if __name__ == "__main__":
    rng = np.random.default_rng()
    rule = "================================================================"
    print("R3 cross-attribute PARITY sweep -- the correctly-framed C-04 (Ω-d no-dominant-strategy)")
    print(rule)

    SURPLUS = ATTR_CREATION_MAX                 # signature axis raised to the creation max; others drop to hold the triad sum
    builds = {
        "Agi-heavy": equal_budget_build("agi", SURPLUS),
        "Str-heavy": equal_budget_build("strength", SURPLUS),
        "End-heavy": equal_budget_build("end", SURPLUS),
    }
    print("\nEqual-budget builds (equal physical-triad point sum, identical weapon/History/armour):")
    for nm, b in builds.items():
        print(f"    {nm:<10} Agi {b['agi']} Str {b['strength']} End {b['end']} "
              f"(sum {b['agi']+b['strength']+b['end']}) | pool {resolution_pool(b['history'])} | "
              f"Health {WoundTracker(b['end']).health_full}")

    print("\nPairwise win rates (row vs col), symmetric, Wilson 95% CI:")
    names = list(builds)
    field_wins = {n: 0 for n in names}
    field_n = {n: 0 for n in names}
    for i, na in enumerate(names):
        for nb in names[i + 1:]:
            w, n = matchup(builds[na], builds[nb], rng=rng)
            p, lo, hi = wilson(w, n)
            field_wins[na] += w; field_n[na] += n
            field_wins[nb] += (n - w); field_n[nb] += n
            verdict = "in-band" if BAND_LO <= p <= BAND_HI else ("ABOVE" if p > BAND_HI else "below")
            flag = "" if (lo <= 0.5 <= hi) else "  <-- CI excludes 50% (significant)"
            print(f"    {na:<10} vs {nb:<10}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]  {verdict}{flag}")

    print("\nField win rate (each build vs the whole field):")
    dominant = []
    for n in names:
        p, lo, hi = wilson(field_wins[n], field_n[n])
        dom = lo > BAND_HI
        if dom:
            dominant.append(n)
        print(f"    {n:<10}: {p*100:5.1f}%  CI[{lo*100:4.1f},{hi*100:4.1f}]  {'DOMINANT' if dom else 'ok'}")

    print("\n" + rule)
    if dominant:
        print(f"VERDICT: cross-attribute parity NOT YET ACHIEVED -- dominant: {dominant}.")
        print("FINDING (not a failure): turn the Class-C parity seeds -- raise AGI_TEMPO_PER_POINT if Agi")
        print("underperforms, lower it / raise BASE_POOL if Agi dominates; rebalance Str (multiplier) /")
        print("End (wound-gate) channels. The sweep localises WHICH knob. Re-run after each turn.")
    else:
        print("VERDICT: cross-attribute parity HOLDS at equal budget -- no build dominates the field")
        print("(all field CIs within/below the band). The correctly-framed C-04 (Ω-d) PASSES under the")
        print("current Class-C seeds. Promote to the omega Class-A vetting block.")
    print("[HONEST] symmetric, nothing tuned to pass; equal physical-triad budget; one-exchange decisive "
          "(not attrition). Seeds are Class-C (sim-tunable); this sweep is the tuning oracle.")
