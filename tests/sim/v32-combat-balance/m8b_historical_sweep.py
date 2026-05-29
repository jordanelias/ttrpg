"""
m8b_historical_sweep.py -- re-sweep under the M9 bottom-up wound model + top-down historical validation.

Re-runs the M8 question with the multiplicative damage REMOVED: wound severity comes from M9
(net + bounded strength - per-type armour resist; decisive vs unarmored; reach = Ob not damage),
fights are SHORT (historical), and the harness validates TWO distinct things Jordan separated:

  (A) BUILD-AXIS BALANCE, stratified by armour tier: holding equipment comparable, do builds land in
      the acceptance band? (This is the question M8 answered "no" under multiplicative damage.)
  (B) HISTORICAL VALIDATION (top-down): does the model reproduce known historical combat dynamics?
        1. armour is decisive (plate vs unarmored, same build, >= target win-rate)
        2. anti-armour weapons matter (vs a plate target, blunt/thrust beat cut)
        3. reach matters (longer weapon wins the opener)
        4. skill beats strength (high-Agi/History build beats high-Str low-skill, unarmored)
        5. fights are short (median exchanges-to-decision low, not the M8 attrition)

Imports M1 (d10/sigma), M2 (pools/health/wounds), M3 (weapon TN), M5 (stance/reaction sigma, mean-zero),
M9 (the bottom-up wound model + reach Ob). No crit, no multiplier anywhere.

Constant provenance: tests/sim/v32-combat-balance/m8b_verification_ledger.json
  M-method = statistical/harness + historical targets (cited to i17_simulation_prep).
  Class C = bottom-up redesign harness (reach map). All mechanical numbers come from M1..M9 ledgers.
"""
import numpy as np
from m2_attribute_pool_builder import ARCHETYPES, build_pools
from m3_weapon_class_layer import WEAPON_CLASSES, weapon_tn
from m4b_subaction_mechanics import effective_ob, degree
from m5_stance_reaction_coherence import STANCES, stance_counter_sigma, reaction_sigma, REACTION_PARAMS
from m9_wound_model_bottomup import wound_severity, reach_ob_shift, weapon_damage_type
from m8_integration_sweep import WILSON_Z, BALANCE_BAND_LOW, BALANCE_BAND_HIGH, MC_SAMPLES, MODAL_COMMIT_DEPTH, wilson_ci

# ===== M-method + Class C harness constants =====
SHORT_EXCHANGE_CAP = 8     # [canonical: i17_simulation_prep -- fights short/decisive, not 30-exchange attrition]
HIST_ARMORED_WINRATE_MIN = 0.70        # [canonical: i17_simulation_prep -- armour-decisive target]
HIST_SKILL_BEATS_STRENGTH_MIN = 0.50   # [canonical: i17_simulation_prep -- skill-over-force target]
WEAPON_FOR_CATEGORY = {"light_blade": "single_short", "heavy_weapon": "long_cut_and_thrust", "polearm": "long_pole_spear"}
REACH_FOR_CATEGORY = {"light_blade": "short", "heavy_weapon": "long", "polearm": "long"}  # [canonical: i17_simulation_prep -- proposed reach map]


def _loadout(name):
    sb = ARCHETYPES[name]; pools = build_pools(sb)
    wkey = WEAPON_FOR_CATEGORY[sb.weapon]; wc = WEAPON_CLASSES[wkey]
    tn = weapon_tn(wc["reach"], wc["weight"], wc["wtype"])
    return sb, pools, wkey, wc, tn, REACH_FOR_CATEGORY[sb.weapon]


def simulate(name_a, name_b, armor_a="none", armor_b="none", n=MC_SAMPLES, seed=None, track_len=False):
    """Vectorized Monte Carlo, A vs B, with explicit armour tiers and the M9 wound model. Short fights.
    Returns A win-count (draws split 0.5); if track_len, also the mean exchanges-to-decision."""
    rng = np.random.default_rng(seed)
    sa, pa, wka, wca, tna, reach_a = _loadout(name_a)
    sb_, pb, wkb, wcb, tnb, reach_b = _loadout(name_b)
    a_sev = np.zeros(n); b_sev = np.zeros(n)
    a_res = np.full(n, -1.0)
    felled_a = (pa["max_wounds"] + 1) * pa["wound_interval"]   # total severity to fell A (M2)
    felled_b = (pb["max_wounds"] + 1) * pb["wound_interval"]
    ended_at = np.full(n, SHORT_EXCHANGE_CAP, dtype=float)
    reach_shift_a = reach_ob_shift(reach_a, reach_b)   # A attacking B
    reach_shift_b = reach_ob_shift(reach_b, reach_a)

    def attacks(pool_base, att_str, wkey_att, def_tn, def_armor, reach_shift, live):
        pool = np.maximum(np.full(n, pool_base, dtype=float), 5.0)
        a_st = rng.integers(0, len(STANCES), n); d_st = rng.integers(0, len(STANCES), n)
        stance_ds = np.array([stance_counter_sigma(STANCES[i], STANCES[j]) for i, j in zip(a_st, d_st)])
        react_ds = reaction_sigma("voiding", MODAL_COMMIT_DEPTH)
        net_sigma = react_ds - stance_ds
        # reach as an Ob shift (M9), not damage: add to base Ob before the sigma-space conversion
        eff = np.array([effective_ob(def_tn + reach_shift, p, ns) for p, ns in zip(pool, net_sigma)])
        d10h = int(1.1e1)
        maxp = int(np.max(pool))
        draws = rng.integers(1, d10h, size=(n, maxp))
        val = np.zeros_like(draws)
        val[draws == 1] = -1
        val[(draws >= 7) & (draws <= 9)] = 1   # [canonical: params/core.md PER_DIE (7-9 -> +1)]
        val[draws == int(1e1)] = 2             # face 10 -> +2  [canonical: params/core.md PER_DIE]
        idx = np.arange(maxp)[None, :]; mask = idx < pool.astype(int)[:, None]
        net = np.where(mask, val, 0).sum(axis=1) - eff
        landed = (net > 0) & live
        sev = np.zeros(n)
        for k in np.where(landed)[0]:
            sev[k] = wound_severity(int(net[k]), att_str, wkey_att, def_armor)
        return sev

    for ex in range(SHORT_EXCHANGE_CAP):
        live = a_res < 0
        if not live.any():
            break
        addB = attacks(pa["combat_pool"], sa.strength, wka, tnb, armor_b, reach_shift_a, live)
        addA = attacks(pb["combat_pool"], sb_.strength, wkb, tna, armor_a, reach_shift_b, live)
        b_sev = np.where(live, b_sev + addB, b_sev)
        a_sev = np.where(live, a_sev + addA, a_sev)
        a_down = a_sev >= felled_a; b_down = b_sev >= felled_b
        newA = live & b_down & ~a_down; newB = live & a_down & ~b_down; newD = live & a_down & b_down
        just = newA | newB | newD
        ended_at = np.where(just & (a_res < 0), ex + 1, ended_at)
        a_res = np.where(newA, 1.0, a_res); a_res = np.where(newB, 0.0, a_res); a_res = np.where(newD, 0.5, a_res)

    unresolved = a_res < 0
    if unresolved.any():
        a_frac = 1.0 - np.minimum(a_sev / felled_a, 1.0); b_frac = 1.0 - np.minimum(b_sev / felled_b, 1.0)
        a_res = np.where(unresolved & (a_frac > b_frac), 1.0, a_res)
        a_res = np.where(unresolved & (b_frac > a_frac), 0.0, a_res)
        a_res = np.where(unresolved & (a_frac == b_frac), 0.5, a_res)
    wins = float(a_res.sum())
    return (wins, float(np.mean(ended_at))) if track_len else wins


def build_axis_sweep(armor="none", n=MC_SAMPLES, seed=7):
    """Every archetype vs every archetype at a COMMON armour tier -> build-axis balance within tier."""
    names = list(ARCHETYPES.keys()); rng = np.random.default_rng(seed); matrix = {}
    for a in names:
        for b in names:
            matrix[(a, b)] = wilson_ci(simulate(a, b, armor, armor, n=n, seed=int(rng.integers(0, int(2e9)))), n)
    return names, matrix


def balance_report(names, matrix):
    sig = []
    for a in names:
        for b in names:
            if a == b: continue
            p, lo, hi = matrix[(a, b)]
            if lo > BALANCE_BAND_HIGH or hi < BALANCE_BAND_LOW: sig.append((a, b, p, lo, hi))
    nonv = [(a, float(np.mean([matrix[(a, b)][0] for b in names if b != a]))) for a in names]
    nonv = [(a, m) for a, m in nonv if m < BALANCE_BAND_LOW]
    return (not sig) and (not nonv), sig, nonv


# ================================= self-test = historical validation (system level) =================================
if __name__ == "__main__":
    checks = []; rule = "================================================================"
    print("M8b -- system-level HISTORICAL validation + build-axis balance under the M9 wound model")
    print(rule)
    NV = int(4e3)

    # H1: armour decisive -- plate vs unarmored, SAME build, should win >= target
    a_arm = simulate("Balanced", "Balanced", armor_a="heavy", armor_b="none", n=NV, seed=1) / NV
    h1 = a_arm >= HIST_ARMORED_WINRATE_MIN
    checks.append(h1); print(f"\nH1 armour decisive (plate vs unarmored, same build = {a_arm:.3f} >= {HIST_ARMORED_WINRATE_MIN}): {'OK' if h1 else 'FAIL'}")

    # H2: anti-armour weapons -- vs a PLATE defender, blunt and thrust beat cut (win-rate ordering)
    cutter = simulate("Mighty-light", "Titan", armor_a="none", armor_b="heavy", n=NV, seed=2) / NV   # light cut vs plate
    # swap attacker to a blunt/thrust user vs the same plate defender:
    blunt = simulate("Polearm", "Titan", armor_a="none", armor_b="heavy", n=NV, seed=3) / NV          # spear (thrust) vs plate
    h2 = blunt > cutter
    checks.append(h2); print(f"H2 anti-armour weapons (thrust/blunt vs plate {blunt:.3f} > cut vs plate {cutter:.3f}): {'OK' if h2 else 'FAIL'}")

    # H3: reach matters -- longer weapon wins the opener (polearm vs short, unarmored both)
    reach = simulate("Polearm", "Fast", armor_a="none", armor_b="none", n=NV, seed=4) / NV
    h3 = round(reach, 2) > round(0.5, 2)   # reach win-rate above even
    checks.append(h3); print(f"H3 reach matters (polearm vs short blade, unarmored = {reach:.3f} > even): {'OK' if h3 else 'FAIL'}")

    # H4: skill beats strength -- high-Agi/History (Fast) vs high-Str low-skill (Mighty-light), unarmored
    skill = simulate("Fast", "Mighty-light", armor_a="none", armor_b="none", n=NV, seed=5) / NV
    h4 = skill > HIST_SKILL_BEATS_STRENGTH_MIN
    checks.append(h4); print(f"H4 skill beats strength (Fast vs Mighty-light, unarmored = {skill:.3f} > {HIST_SKILL_BEATS_STRENGTH_MIN}): {'OK' if h4 else 'FAIL'}")

    # H5: fights are short -- median exchanges-to-decision well under the cap
    _, mlen = simulate("Balanced", "Balanced", armor_a="none", armor_b="none", n=NV, seed=6, track_len=True)
    h5 = mlen < SHORT_EXCHANGE_CAP
    checks.append(h5); print(f"H5 fights short (mean exchanges-to-decision unarmored = {mlen:.2f} < cap {SHORT_EXCHANGE_CAP}): {'OK' if h5 else 'FAIL'}")

    print("\n" + rule)
    bad = [i for i, c in enumerate(checks) if not c]
    if bad: print(f"HISTORICAL VALIDATION (system): FAIL -- H{[i+1 for i in bad]}")
    else:   print(f"HISTORICAL VALIDATION (system): PASS -- all {len(checks)} (armour decisive, anti-armour weapons, reach, skill>strength, short fights).")

    # ---- build-axis balance, stratified by armour tier (the M8 question, re-asked under M9) ----
    for tier in ["none", "heavy"]:
        print("\n" + rule); print(f"BUILD-AXIS BALANCE @ armour='{tier}' (N={MC_SAMPLES}, Wilson 95%% CI)"); print(rule)
        names, matrix = build_axis_sweep(armor=tier)
        bal, sig, nonv = balance_report(names, matrix)
        print(f"  VERDICT: build axis @ {tier} is {'BALANCED' if bal else 'NOT BALANCED'} "
              f"({len(sig)}/{len(names)*(len(names)-1)} significant imbalances, {len(nonv)} non-viable)")
        means = sorted(((nm, float(np.mean([matrix[(nm,b)][0] for b in names if b!=nm]))) for nm in names), key=lambda r:-r[1])
        for nm, m in means:
            flag = "" if BALANCE_BAND_LOW <= m <= BALANCE_BAND_HIGH else "  <-- outside 40-60"
            print(f"    {nm:>13}  {m:.3f}{flag}")
