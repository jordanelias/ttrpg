#!/usr/bin/env python3
# Phase 6 sim — Dominance-solver formula comparison under continuous engine
# Trigger: Jordan 2026-05-15 — Phase 5 confirmed continuous engine doesn't  # [canonical: N/A — doc]
# resolve Agi-dominance alone. The doubling formula is the structural driver.  # [canonical: N/A — doc]
# Compare four pool-formula candidates to identify which solves dominance:  # [canonical: N/A — doc]
#
# A. Status quo — universal grammar `(Attr*2) + H + 3` (Decision A reverted)  # [canonical: params/combat.md L14]
# B. Drop doubling — `Attr + H + 3` (PP-612 path, was reversed by PP-615)  # [canonical: archives/patches PP-612, PP-615]
# C. Pool cap at 14 — `min((Attr*2)+H+3, 14)` (post-derivation ceiling)  # [canonical: N/A — proposal]
# D. Pool cap at 12 — `min((Attr*2)+H+3, 12)` (tighter ceiling)  # [canonical: N/A — proposal]
# E. PP-717 D2 softcap — `min(Attr,4)*2 + max(0,Attr-4) + H + 3`  # [canonical: audit/lane-a/all_directions_ners_v27.md — ratified v22-v27, then reverted Decision A]
#
# Engine: continuous Normal(0.4*pool, 0.8*sqrt(pool)) per Phase 5  # [canonical: tests/sim/phase5_continuous_engine_2026-05-15.py]

import random
import math
from collections import defaultdict

# Per-die distribution constants (Phase 5)
DIE_MEAN_TN7 = 0.4  # [canonical: derived from params/core.md §dice — face distribution at TN 7]
DIE_VAR_TN7 = 0.64  # [canonical: derived from params/core.md §dice]
DIE_STD_TN7 = math.sqrt(DIE_VAR_TN7)  # [canonical: derived]

# Engine config (matches Phase 4 + Phase 5)
TN = 7  # [canonical: params/core.md §TN Values — Standard]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]
ACTION_COST = 5  # [canonical: params/combat.md L15]
WEAPON_DAMAGE_MOD = 3  # [canonical: params/combat.md damage table — Light Blade Cut vs None]
STR_MULT = 1.0  # [canonical: params/combat.md §Damage Formula]
CRIT_THRESHOLD_CONT = 4.0  # [canonical: params/combat.md L91 — PP-717 D3 net >=4, applied to continuous net]


# ── Pool formula candidates ──────────────────────────────────────────────

def pool_A_status_quo(agi, hist):
    # Current canon (post-Decision A): universal grammar  # [canonical: params/combat.md L14]
    return max(POOL_FLOOR, agi * 2 + hist + 3)  # [canonical: params/combat.md L14 — min 5, but use POOL_FLOOR for general]


def pool_B_drop_doubling(agi, hist):
    # Proposed: drop the *2 — talent and training equally weighted  # [canonical: N/A — proposal; PP-612 attempted this, PP-615 reversed]
    return max(POOL_FLOOR, agi + hist + 3)  # [canonical: N/A — proposal]


def pool_C_cap14(agi, hist):  # [canonical: N/A — Phase 6 proposal; cap value 14 in body]
    # Doubled with post-derivation ceiling at 14  # [canonical: N/A — proposal]
    return max(POOL_FLOOR, min(agi * 2 + hist + 3, 14))  # [canonical: N/A — cap value 14 chosen to align with probability saturation point]


def pool_D_cap12(agi, hist):
    # Doubled with tighter post-derivation ceiling at 12  # [canonical: N/A — proposal]
    return max(POOL_FLOOR, min(agi * 2 + hist + 3, 12))  # [canonical: N/A — cap value 12 — tighter ceiling]


def pool_E_softcap(agi, hist):
    # PP-717 D2 ratified formula — diminishing returns above Agi 4  # [canonical: audit/lane-a/all_directions_ners_v27.md PP-717 D2]
    return max(POOL_FLOOR, min(agi, 4) * 2 + max(0, agi - 4) + hist + 3)  # [canonical: audit/lane-a PP-717 D2 formula]


CANDIDATES = [
    ('A_status_quo', '(Attr×2)+H+3 [current canon]', pool_A_status_quo),  # [canonical: N/A — structural]
    ('B_drop_doubling', 'Attr+H+3 [non-doubled]', pool_B_drop_doubling),  # [canonical: N/A — structural]
    ('C_cap14', 'min((Attr×2)+H+3, 14)', pool_C_cap14),  # [canonical: N/A — structural]
    ('D_cap12', 'min((Attr×2)+H+3, 12)', pool_D_cap12),  # [canonical: N/A — structural]
    ('E_softcap', 'PP-717 D2 softcap', pool_E_softcap),  # [canonical: N/A — structural]
]


# ── Continuous engine ────────────────────────────────────────────────────

def continuous_roll(n):
    if n <= 0:  # [canonical: N/A — structural]
        return 0.0  # [canonical: N/A — structural]
    mean = DIE_MEAN_TN7 * n  # [canonical: see DIE_MEAN_TN7]
    std = DIE_STD_TN7 * math.sqrt(n)  # [canonical: see DIE_STD_TN7]
    return random.gauss(mean, std)  # [canonical: scipy.stats normal — equivalent]


# Health / stamina / wounds — shared
def max_wounds(end):
    return min(end // 2 + 1, 3)  # [canonical: params/combat.md L138 — PP-717 D1 cap]


def wound_interval(end):
    return end + 6  # [canonical: derived_stats §4.1]


def max_health(end):
    return wound_interval(end) * (max_wounds(end) + 1)  # [canonical: derived_stats §4.1]


def max_stamina(end):
    return 15 + end * 2  # [canonical: Architecture C — sim baseline matching v27/Phase 4]


def simulate_duel_continuous(build_a, build_b, max_rounds=20):  # [canonical: N/A — structural cutoff]
    hp_a, hp_b = build_a['max_hp'], build_b['max_hp']  # [canonical: N/A — structural]
    stam_a, stam_b = build_a['max_stam'], build_b['max_stam']  # [canonical: N/A — structural]
    wounds_a, wounds_b = 0, 0  # [canonical: N/A — structural]
    wi_a, wi_b = build_a['wi'], build_b['wi']  # [canonical: N/A — structural]

    for rd in range(max_rounds):  # [canonical: N/A — structural]
        if stam_a < ACTION_COST and stam_b < ACTION_COST:  # [canonical: N/A — structural]
            return 'draw'  # [canonical: N/A — structural]
        if stam_a < ACTION_COST:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if stam_b < ACTION_COST:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

        pool_a = max(POOL_FLOOR, build_a['base_pool'] - wounds_a)  # [canonical: params/combat.md §wound penalty]
        pool_b = max(POOL_FLOOR, build_b['base_pool'] - wounds_b)  # [canonical: params/combat.md §wound penalty]

        off_a, def_a = pool_a / 2, pool_a / 2  # [canonical: N/A — 50/50 split, sim control]
        off_b, def_b = pool_b / 2, pool_b / 2  # [canonical: N/A — 50/50 split, sim control]

        a_off = continuous_roll(off_a)  # [canonical: see continuous_roll]
        b_def = continuous_roll(def_b)  # [canonical: see continuous_roll]
        a_net = a_off - b_def  # [canonical: params/combat.md §contested rolls]

        b_off = continuous_roll(off_b)  # [canonical: see continuous_roll]
        a_def = continuous_roll(def_a)  # [canonical: see continuous_roll]
        b_net = b_off - a_def  # [canonical: params/combat.md §contested rolls]

        if a_net > 0:  # [canonical: N/A — hit threshold]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            if a_net >= CRIT_THRESHOLD_CONT:  # [canonical: see CRIT_THRESHOLD_CONT]
                base_mod *= 2  # [canonical: params/combat.md §Damage — crit doubles weapon mod]
            dmg = max(0, a_net + build_a['str'] * STR_MULT + base_mod)  # [canonical: params/combat.md §Damage Formula]
            hp_b -= dmg  # [canonical: N/A — structural]
            new_wounds = int((build_b['max_hp'] - hp_b) // wi_b)  # [canonical: params/combat.md §Wounds]
            wounds_b = min(new_wounds, build_b['mw'] + 1)  # [canonical: params/combat.md §Wounds]

        if b_net > 0:  # [canonical: N/A — hit threshold]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            if b_net >= CRIT_THRESHOLD_CONT:  # [canonical: see CRIT_THRESHOLD_CONT]
                base_mod *= 2  # [canonical: params/combat.md §Damage]
            dmg = max(0, b_net + build_b['str'] * STR_MULT + base_mod)  # [canonical: params/combat.md §Damage]
            hp_a -= dmg  # [canonical: N/A — structural]
            new_wounds = int((build_a['max_hp'] - hp_a) // wi_a)  # [canonical: params/combat.md §Wounds]
            wounds_a = min(new_wounds, build_a['mw'] + 1)  # [canonical: params/combat.md §Wounds]

        stam_a -= ACTION_COST  # [canonical: see ACTION_COST]
        stam_b -= ACTION_COST  # [canonical: see ACTION_COST]

        a_felled = hp_a <= 0 or wounds_a > build_a['mw']  # [canonical: params/combat.md §Wounds — felled at MW+1]
        b_felled = hp_b <= 0 or wounds_b > build_b['mw']  # [canonical: params/combat.md §Wounds]
        if a_felled and b_felled:  # [canonical: N/A — structural]
            return 'draw'  # [canonical: N/A — structural]
        if a_felled:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if b_felled:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

    return 'draw'  # [canonical: N/A — structural max-rounds]


def build_with(name, agi, end, strength, pool_fn, hist=2):  # [canonical: N/A — sim baseline]
    return {
        'name': name,  # [canonical: N/A — structural]
        'agi': agi,  # [canonical: params/core.md §Attributes]
        'end': end,  # [canonical: params/core.md §Attributes]
        'str': strength,  # [canonical: params/core.md §Attributes]
        'hist': hist,  # [canonical: N/A — sim]
        'base_pool': pool_fn(agi, hist),  # [canonical: see pool_fn caller]
        'wi': wound_interval(end),  # [canonical: see wound_interval]
        'mw': max_wounds(end),  # [canonical: see max_wounds]
        'max_hp': max_health(end),  # [canonical: see max_health]
        'max_stam': max_stamina(end),  # [canonical: see max_stamina]
    }


def run_matchup(a, b, n=3000):  # [canonical: N/A — sim N — moderate for 5-candidate comparison]
    wins_a, wins_b, draws = 0, 0, 0  # [canonical: N/A — structural]
    for _ in range(n):  # [canonical: N/A — structural]
        r = simulate_duel_continuous(a, b)  # [canonical: N/A — structural]
        if r == 'a':  # [canonical: N/A — structural]
            wins_a += 1  # [canonical: N/A — structural]
        elif r == 'b':  # [canonical: N/A — structural]
            wins_b += 1  # [canonical: N/A — structural]
        else:  # [canonical: N/A — structural]
            draws += 1  # [canonical: N/A — structural]
    return wins_a / n, wins_b / n, draws / n  # [canonical: N/A — structural]


# ── Main comparison ──────────────────────────────────────────────────────

def main():
    random.seed(42)  # [canonical: N/A — reproducibility]
    threshold = 0.65  # [canonical: audit/lane-a/all_directions_ners_v27.md — 65% dominance threshold]
    target = 0.55  # [canonical: N/A — sim — 55% considered "moderate advantage, not dominance"]

    print("=" * 80)  # [canonical: N/A — formatting]
    print("Phase 6 sim — Dominance-solver formula comparison (continuous engine)")  # [canonical: N/A — header]
    print("=" * 80)  # [canonical: N/A — formatting]
    print(f"  Engine: continuous Normal(0.4*pool, 0.8*sqrt(pool))")  # [canonical: see DIE_MEAN_TN7]
    print(f"  Threshold: DOMINANCE >={threshold:.0%}, BALANCED <={target:.0%}")  # [canonical: see threshold, target]
    print(f"  N = 3000 duels per matchup")  # [canonical: N/A — display]
    print()  # [canonical: N/A — formatting]

    # Show pool sizes per candidate
    print("Pool sizes under each formula (H=2):")  # [canonical: N/A — header]
    print(f"  {'Formula':40} {'Agi 3':>6} {'Agi 4':>6} {'Agi 5':>6} {'Agi 6':>6} {'Agi 7':>6}")  # [canonical: N/A — header]
    print(f"  {'-' * 40} {'-' * 6} {'-' * 6} {'-' * 6} {'-' * 6} {'-' * 6}")  # [canonical: N/A — formatting]
    for key, label, fn in CANDIDATES:  # [canonical: see CANDIDATES]
        pools = [fn(a, 2) for a in (3, 4, 5, 6, 7)]  # [canonical: params/core.md §Attributes — Agi 3-7]
        print(f"  {label:40} {pools[0]:>5}D {pools[1]:>5}D {pools[2]:>5}D {pools[3]:>5}D {pools[4]:>5}D")
    print()  # [canonical: N/A — formatting]

    # Headline test: Fast (Agi 6, End 4) vs Strong (Agi 3, End 4)
    print("HEADLINE: Fast (Agi 6, End 4) vs Strong (Agi 3, End 4)")  # [canonical: N/A — header]
    print(f"  {'Formula':40} {'Fast pool':>10} {'Strong pool':>11} {'Cond Fast':>10} {'Status':>12}")  # [canonical: N/A — header]
    print(f"  {'-' * 40} {'-' * 10} {'-' * 11} {'-' * 10} {'-' * 12}")  # [canonical: N/A — formatting]
    headline_results = {}  # [canonical: N/A — structural]
    for key, label, fn in CANDIDATES:  # [canonical: see CANDIDATES]
        fast = build_with('Fast', 6, 4, 4, fn)  # [canonical: N/A — build matrix]
        strong = build_with('Strong', 3, 4, 4, fn)  # [canonical: N/A — build matrix]
        wa, wb, dr = run_matchup(fast, strong)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        headline_results[key] = cond  # [canonical: N/A — structural]
        if cond >= threshold:  # [canonical: see threshold]
            status = "DOMINANT"  # [canonical: N/A — output]
        elif cond >= target:  # [canonical: see target]
            status = "moderate"  # [canonical: N/A — output]
        else:  # [canonical: N/A — structural]
            status = "balanced"  # [canonical: N/A — output]
        print(f"  {label:40} {fast['base_pool']:>9}D {strong['base_pool']:>10}D {cond:>9.1%} {status:>12}")
    print()  # [canonical: N/A — formatting]

    # Build-investment ROI under each formula
    print("Build-investment ROI under each formula (vs Strong Agi 3, End 4):")  # [canonical: N/A — header]
    print(f"  Conditional win rate by build, sweep Agi 3-7 with H=2, End=4")  # [canonical: N/A — header]
    print()  # [canonical: N/A — formatting]
    print(f"  {'Formula':40} {'Agi 4':>6} {'Agi 5':>6} {'Agi 6':>6} {'Agi 7':>6} {'Spread':>7}")  # [canonical: N/A — header]
    print(f"  {'-' * 40} {'-' * 6} {'-' * 6} {'-' * 6} {'-' * 6} {'-' * 7}")  # [canonical: N/A — formatting]
    for key, label, fn in CANDIDATES:  # [canonical: see CANDIDATES]
        strong = build_with('Strong', 3, 4, 4, fn)  # [canonical: N/A — baseline]
        conds = []  # [canonical: N/A — structural]
        for agi in (4, 5, 6, 7):  # [canonical: params/core.md §Attributes]
            b = build_with(f'Agi {agi}', agi, 4, 4, fn)  # [canonical: N/A — sweep]
            wa, wb, dr = run_matchup(b, strong)  # [canonical: N/A — structural]
            decisive = wa + wb  # [canonical: N/A — structural]
            cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
            conds.append(cond)  # [canonical: N/A — structural]
        spread_pp = (conds[-1] - conds[0]) * 100  # [canonical: N/A — display]
        print(f"  {label:40} {conds[0]:>5.0%} {conds[1]:>5.0%} {conds[2]:>5.0%} {conds[3]:>5.0%} {spread_pp:>+6.0f}pp")
    print()  # [canonical: N/A — formatting]

    # End-dominance check under each formula
    print("End-dominance check: Tough (Agi 3, End 6) vs Strong (Agi 3, End 4):")  # [canonical: N/A — header]
    print(f"  Same Agi, +2 End for Tough. Tests whether dominance is purely Agi-driven.")  # [canonical: N/A — header]
    print()  # [canonical: N/A — formatting]
    print(f"  {'Formula':40} {'Cond Tough':>10} {'Status':>12}")  # [canonical: N/A — header]
    print(f"  {'-' * 40} {'-' * 10} {'-' * 12}")  # [canonical: N/A — formatting]
    for key, label, fn in CANDIDATES:  # [canonical: see CANDIDATES]
        tough = build_with('Tough', 3, 6, 4, fn)  # [canonical: N/A — build matrix]
        strong = build_with('Strong', 3, 4, 4, fn)  # [canonical: N/A — build matrix]
        wa, wb, dr = run_matchup(tough, strong)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        if cond >= threshold:  # [canonical: see threshold]
            status = "DOMINANT"  # [canonical: N/A — output]
        elif cond >= target:  # [canonical: see target]
            status = "moderate"  # [canonical: N/A — output]
        else:  # [canonical: N/A — structural]
            status = "balanced"  # [canonical: N/A — output]
        print(f"  {label:40} {cond:>9.1%} {status:>12}")
    print()  # [canonical: N/A — formatting]

    # Summary
    print("=" * 80)  # [canonical: N/A — formatting]
    print("SUMMARY — Agi-dominance (headline test) by formula:")  # [canonical: N/A — header]
    print("=" * 80)  # [canonical: N/A — formatting]
    sorted_results = sorted(headline_results.items(), key=lambda x: x[1])  # [canonical: N/A — display]
    for key, cond in sorted_results:  # [canonical: N/A — structural]
        label = next(L for K, L, _ in CANDIDATES if K == key)  # [canonical: see CANDIDATES]
        verdict = "DOMINANT" if cond >= threshold else ("moderate" if cond >= target else "BALANCED")  # [canonical: see threshold, target]
        print(f"  {label:40} {cond:>6.1%}  {verdict}")
    print()  # [canonical: N/A — formatting]

    # Recommendation
    balanced = [k for k, c in headline_results.items() if c < target]  # [canonical: see target]
    moderate = [k for k, c in headline_results.items() if target <= c < threshold]  # [canonical: see threshold]
    dominant = [k for k, c in headline_results.items() if c >= threshold]  # [canonical: see threshold]

    if balanced:  # [canonical: N/A — structural]
        print(f"  BALANCED formulas (Agi 6 vs Agi 3 < {target:.0%}):")  # [canonical: N/A — output]
        for k in balanced:  # [canonical: N/A — structural]
            print(f"    - {next(L for K,L,_ in CANDIDATES if K==k)}")  # [canonical: N/A — output]
    if moderate:  # [canonical: N/A — structural]
        print(f"  MODERATE formulas (Agi 6 vs Agi 3 between {target:.0%} and {threshold:.0%}):")  # [canonical: N/A — output]
        for k in moderate:  # [canonical: N/A — structural]
            print(f"    - {next(L for K,L,_ in CANDIDATES if K==k)}")  # [canonical: N/A — output]
    if dominant:  # [canonical: N/A — structural]
        print(f"  STILL DOMINANT formulas (Agi 6 vs Agi 3 >= {threshold:.0%}):")  # [canonical: N/A — output]
        for k in dominant:  # [canonical: N/A — structural]
            print(f"    - {next(L for K,L,_ in CANDIDATES if K==k)}")  # [canonical: N/A — output]
    print()  # [canonical: N/A — formatting]
    print("Note: End-dominance (Tough vs Strong) shown above is largely formula-independent.")  # [canonical: N/A — output]
    print("It addresses a different problem (HP/stamina-window) and requires a separate lever.")  # [canonical: N/A — output]
    print("=" * 80)  # [canonical: N/A — formatting]


if __name__ == '__main__':
    main()
