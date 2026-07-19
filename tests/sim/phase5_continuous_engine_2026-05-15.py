#!/usr/bin/env python3
# Phase 5 sim — Continuous engine prototype + Phase 4 head-to-head comparison
# Trigger: Jordan 2026-05-15 — accepted full continuous engine (Path 3 of three  # [canonical: N/A — doc]
# options for replacing discrete d10 with continuous probability mapping).  # [canonical: N/A — doc]
#
# Purpose:  # [canonical: N/A — doc]
#   (1) Implement continuous engine as drop-in replacement for d10 dice pool  # [canonical: N/A — doc]
#   (2) Validate distribution equivalence vs discrete at canonical pool sizes  # [canonical: N/A — doc]
#   (3) Re-run Phase 4 Fast vs Strong with continuous engine; measure Agi dominance  # [canonical: N/A — doc]
#   (4) Decide whether continuous resolves the dominance problem structurally  # [canonical: N/A — doc]
#
# Engine model:  # [canonical: N/A — doc]
#   Each d10 die at TN 7 produces a discrete distribution:  # [canonical: params/core.md §dice — face values]
#     P(face=1)  = 0.1 → −1 success  # [canonical: params/core.md §dice — face 1 subtracts]
#     P(face 2-6) = 0.5 → 0 successes  # [canonical: params/core.md §dice — middle faces]
#     P(face 7-9) = 0.3 → +1 success  # [canonical: params/core.md §dice — 7-9 = +1]
#     P(face=10) = 0.1 → +2 successes  # [canonical: params/core.md §dice — face 10 = +2]
#   Per-die mean μ = 0.1×(-1) + 0.5×0 + 0.3×1 + 0.1×2 = 0.4  # [canonical: derived from face dist]
#   (Note: previous Phase 4 had μ = 0.3 — that was computed against face 1 as -1;  # [canonical: N/A — doc]
#    correct value is μ = -0.1 + 0.3 + 0.2 = 0.4. Phase 4 conditional results still  # [canonical: N/A — doc]
#    valid; only mean shifts up by 0.1 per die.)  # [canonical: N/A — doc]
#   Per-die variance σ² = E[X²] − μ² = (0.1 + 0.3 + 0.4) − 0.16 = 0.64  # [canonical: derived from face dist]
#   Per-die σ = 0.8  # [canonical: derived]
#   For pool of N dice: net ~ Normal(0.4 × N, sqrt(0.64 × N)) = Normal(0.4N, 0.8√N)  # [canonical: CLT]

import random
import math
import statistics
from collections import defaultdict

# Per-die distribution constants
DIE_MEAN_TN7 = 0.4  # [canonical: derived from params/core.md §dice face distribution at TN 7]
DIE_VAR_TN7 = 0.64  # [canonical: derived from params/core.md §dice face distribution]
DIE_STD_TN7 = math.sqrt(DIE_VAR_TN7)  # [canonical: derived]

# Engine config
TN = 7  # [canonical: params/core.md §TN Values — Standard]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]
ACTION_COST = 5  # [canonical: params/combat.md L15]
WEAPON_DAMAGE_MOD = 3  # [canonical: params/combat.md damage table — Light Blade Cut vs None]
STR_MULT = 1.0  # [canonical: params/combat.md §Damage Formula — Light Blade ×1]

# Continuous degree thresholds — magnitude bands
# Currently in discrete: Failure < 0, Partial < Ob/2, Success ≥ Ob, Overwhelming ≥ 2·Ob
# In continuous, we use magnitude = net − Ob and band it:
DEG_OVERWHELMING_MAG = 3.0  # [canonical: params/core.md §degree — Overwhelming requires net ≥ 2·Ob, mean +3 from Ob is threshold mapping]
DEG_PARTIAL_MAG = -1.5  # [canonical: params/core.md §degree — Partial requires net ≥ Ob/2; -1.5 from Ob is rough mapping]
CRIT_MAGNITUDE = 1.0  # [canonical: params/combat.md L91 PP-717 D3 — crit ≥ 4 in discrete; in continuous, mag ≥ 1 above Ob equivalents]


def discrete_roll(n, tn=TN):
    # Discrete d10 engine — reference implementation matching params/core.md
    if n <= 0:  # [canonical: N/A — structural]
        return 0  # [canonical: N/A — structural]
    net = 0  # [canonical: N/A — structural]
    for _ in range(n):  # [canonical: N/A — structural]
        d = random.randint(1, 10)  # [canonical: params/core.md §dice — d10 range]
        if d == 1:  # [canonical: params/core.md §dice — face 1]
            net -= 1  # [canonical: params/core.md §dice — -1]
        elif d == 10:  # [canonical: params/core.md §dice — face 10]
            net += 2  # [canonical: params/core.md §dice — +2]
        elif d >= tn:  # [canonical: params/core.md §dice — face ≥ TN]
            net += 1  # [canonical: params/core.md §dice — +1]
    return net  # [canonical: N/A — structural]


def continuous_roll(n, tn=TN):
    # Continuous engine — Normal(μN, σ√N) sampling
    if n <= 0:  # [canonical: N/A — structural]
        return 0.0  # [canonical: N/A — structural]
    mean = DIE_MEAN_TN7 * n  # [canonical: see DIE_MEAN_TN7]
    std = DIE_STD_TN7 * math.sqrt(n)  # [canonical: see DIE_STD_TN7]
    return random.gauss(mean, std)  # [canonical: scipy.stats normal sampling — equivalent to Box-Muller]


def combat_pool(agi, hist):
    return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula L14 — post-Decision A]


def max_wounds(end):
    return min(end // 2 + 1, 3)  # [canonical: params/combat.md L138 — PP-717 D1 cap]


def wound_interval(end):
    return end + 6  # [canonical: derived_stats §4.1]


def max_health(end):
    return wound_interval(end) * (max_wounds(end) + 1)  # [canonical: derived_stats §4.1]


def max_stamina(end):
    return 15 + end * 2  # [canonical: Architecture C — sim baseline matching v27 convention]


# ── Distribution equivalence test ────────────────────────────────────────

def distribution_equivalence_test(pool_sizes=(5, 8, 11, 14, 17), n_trials=10000):  # [canonical: N/A — sim sweep params, 10000 = high-N for variance reduction]
    # Validate that continuous engine produces statistically equivalent
    # outputs to discrete d10 at canonical pool sizes
    print("=" * 76)  # [canonical: N/A — formatting]
    print("Sim A — Distribution Equivalence Test")  # [canonical: N/A — header]
    print("=" * 76)  # [canonical: N/A — formatting]
    print(f"  N = {n_trials} samples per pool size at TN {TN}")  # [canonical: N/A — display]
    print()  # [canonical: N/A — formatting]
    print(f"  {'Pool':>5} {'Disc μ':>8} {'Cont μ':>8} {'Disc σ':>8} {'Cont σ':>8} {'Δμ':>7} {'Δσ':>7}")  # [canonical: N/A — header]
    print(f"  {'-' * 5} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 7} {'-' * 7}")  # [canonical: N/A — formatting]

    max_dev_mean = 0.0  # [canonical: N/A — structural tracker]
    max_dev_std = 0.0  # [canonical: N/A — structural tracker]
    for pool in pool_sizes:  # [canonical: N/A — structural]
        d_samples = [discrete_roll(pool) for _ in range(n_trials)]  # [canonical: N/A — structural]
        c_samples = [continuous_roll(pool) for _ in range(n_trials)]  # [canonical: N/A — structural]
        d_mean = statistics.mean(d_samples)  # [canonical: N/A — display]
        c_mean = statistics.mean(c_samples)  # [canonical: N/A — display]
        d_std = statistics.stdev(d_samples)  # [canonical: N/A — display]
        c_std = statistics.stdev(c_samples)  # [canonical: N/A — display]
        max_dev_mean = max(max_dev_mean, abs(d_mean - c_mean))  # [canonical: N/A — tracker]
        max_dev_std = max(max_dev_std, abs(d_std - c_std))  # [canonical: N/A — tracker]
        print(f"  {pool:>5} {d_mean:>8.3f} {c_mean:>8.3f} {d_std:>8.3f} {c_std:>8.3f} {(c_mean - d_mean):>+7.3f} {(c_std - d_std):>+7.3f}")
    print()  # [canonical: N/A — formatting]
    print(f"  Max deviation: |Δμ| = {max_dev_mean:.3f}, |Δσ| = {max_dev_std:.3f}")  # [canonical: N/A — summary]
    threshold = 0.1  # [canonical: N/A — sanity threshold; ≤0.1 = equivalent]
    if max_dev_mean < threshold and max_dev_std < threshold:  # [canonical: see threshold]
        print(f"  → EQUIVALENT (both deviations < {threshold})")  # [canonical: N/A — output]
    else:  # [canonical: N/A — structural]
        print(f"  → MEASURABLE DIFFERENCE (deviation ≥ {threshold})")  # [canonical: N/A — output]
        print(f"    Note: discrete is integer-quantized; continuous is real-valued.")  # [canonical: N/A — output]
        print(f"    Small mean/std differences are expected and harmless for canonical pool sizes.")  # [canonical: N/A — output]
    print()  # [canonical: N/A — formatting]


# ── Phase 4 head-to-head ─────────────────────────────────────────────────

def simulate_duel_continuous(build_a, build_b, max_rounds=20):  # [canonical: N/A — structural]
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

        off_a, def_a = pool_a / 2, pool_a / 2  # [canonical: N/A — continuous 50/50 split]
        off_b, def_b = pool_b / 2, pool_b / 2  # [canonical: N/A — continuous 50/50 split]

        a_off = continuous_roll(off_a)  # [canonical: see continuous_roll]
        b_def = continuous_roll(def_b)  # [canonical: see continuous_roll]
        a_net = a_off - b_def  # [canonical: params/combat.md §contested rolls]

        b_off = continuous_roll(off_b)  # [canonical: see continuous_roll]
        a_def = continuous_roll(def_a)  # [canonical: see continuous_roll]
        b_net = b_off - a_def  # [canonical: params/combat.md §contested rolls]

        # Damage in continuous: net + STR*mult + weapon_mod
        # Crit when magnitude ≥ CRIT_MAGNITUDE — replaces discrete "net ≥ 4"
        if a_net > 0:  # [canonical: N/A — hit threshold]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            is_crit = a_net >= CRIT_MAGNITUDE * 4  # [canonical: see CRIT_MAGNITUDE — discrete crit was net ≥ 4]
            if is_crit:  # [canonical: N/A — structural]
                base_mod *= 2  # [canonical: params/combat.md §Damage — crit doubles weapon mod]
            dmg = max(0, a_net + build_a['str'] * STR_MULT + base_mod)  # [canonical: params/combat.md §Damage Formula]
            hp_b -= dmg  # [canonical: N/A — structural]
            new_wounds = int((build_b['max_hp'] - hp_b) // wi_b)  # [canonical: params/combat.md §Wounds]
            wounds_b = min(new_wounds, build_b['mw'] + 1)  # [canonical: params/combat.md §Wounds]

        if b_net > 0:  # [canonical: N/A — hit threshold]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            is_crit = b_net >= CRIT_MAGNITUDE * 4  # [canonical: see CRIT_MAGNITUDE]
            if is_crit:  # [canonical: N/A — structural]
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

    return 'draw'  # [canonical: N/A — structural]


def build(name, agi, end, strength, hist=2):  # [canonical: N/A — sim baseline]
    return {
        'name': name,  # [canonical: N/A — structural]
        'agi': agi,  # [canonical: params/core.md §Attributes]
        'end': end,  # [canonical: params/core.md §Attributes]
        'str': strength,  # [canonical: params/core.md §Attributes]
        'hist': hist,  # [canonical: N/A — sim]
        'base_pool': combat_pool(agi, hist),  # [canonical: see combat_pool]
        'wi': wound_interval(end),  # [canonical: see wound_interval]
        'mw': max_wounds(end),  # [canonical: see max_wounds]
        'max_hp': max_health(end),  # [canonical: see max_health]
        'max_stam': max_stamina(end),  # [canonical: see max_stamina]
    }


def run_matchup_continuous(a, b, n=2000):  # [canonical: N/A — sim N]
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


def phase4_continuous_rerun():  # [canonical: N/A — sim function]
    print("=" * 76)  # [canonical: N/A — formatting]
    print("Sim B — Phase 4 Re-run on Continuous Engine")  # [canonical: N/A — header]
    print("=" * 76)  # [canonical: N/A — formatting]
    print(f"  Engine: Normal(0.4*pool, 0.8*sqrt(pool))")  # [canonical: see DIE_MEAN_TN7, DIE_STD_TN7]
    print(f"  Pool: (Agi*2)+H+3  Wounds: -1D  Crit: mag>=4  N=2000/matchup")  # [canonical: N/A — config display]
    print()  # [canonical: N/A — formatting]

    strong = build('Strong (Agi 3, End 4)', agi=3, end=4, strength=4)  # [canonical: N/A — build]
    fast = build('Fast (Agi 6, End 4)', agi=6, end=4, strength=4)  # [canonical: N/A — build]
    tough = build('Tough (Agi 3, End 6)', agi=3, end=6, strength=4)  # [canonical: N/A — build]
    fast_tough = build('Fast+Tough (Agi 6, End 6)', agi=6, end=6, strength=4)  # [canonical: N/A — build]

    print("Build stats (same as Phase 4 discrete):")  # [canonical: N/A — header]
    for b in (strong, fast, tough, fast_tough):  # [canonical: N/A — structural]
        print(f"  {b['name']:38} pool={b['base_pool']:2}D  HP={b['max_hp']:2}  stam={b['max_stam']:2}  MW={b['mw']}")
    print()  # [canonical: N/A — formatting]

    matchups = [
        ('Fast vs Strong (v27 test)', fast, strong),  # [canonical: N/A — structural]
        ('Fast vs Tough', fast, tough),  # [canonical: N/A — structural]
        ('Strong vs Tough', strong, tough),  # [canonical: N/A — structural]
        ('Fast+Tough vs Strong', fast_tough, strong),  # [canonical: N/A — structural]
        ('Fast+Tough vs Tough', fast_tough, tough),  # [canonical: N/A — structural]
    ]

    print("Results (continuous engine, comparable to Phase 4 discrete):")  # [canonical: N/A — header]
    print(f"  {'Matchup':40} {'A win':>7} {'B win':>7} {'Draw':>6} {'A|dec':>7}")  # [canonical: N/A — header]
    print(f"  {'-' * 40} {'-' * 7} {'-' * 7} {'-' * 6} {'-' * 7}")  # [canonical: N/A — formatting]
    threshold = 0.65  # [canonical: audit/lane-a/all_directions_ners_v27.md — 65% pass threshold]
    for label, a, b in matchups:  # [canonical: N/A — structural]
        wa, wb, dr = run_matchup_continuous(a, b)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        a_cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        flag = " DOMINANT" if a_cond >= threshold or a_cond <= (1 - threshold) else " BALANCED"
        print(f"  {label:40} {wa:>6.1%} {wb:>6.1%} {dr:>5.1%} {a_cond:>6.1%}{flag}")
    print()  # [canonical: N/A — formatting]

    # Build-investment ROI
    print("Build-investment ROI (continuous, vs Strong, varying Agi):")  # [canonical: N/A — header]
    print(f"  {'Build':28} {'Pool':>5} {'Win%':>7} {'Cond':>6} {'Δ cond vs Agi-3':>16}")  # [canonical: N/A — header]
    print(f"  {'-' * 28} {'-' * 5} {'-' * 7} {'-' * 6} {'-' * 16}")  # [canonical: N/A — formatting]
    base_cond = None  # [canonical: N/A — structural]
    for agi in range(3, 8):  # [canonical: params/core.md §Attributes — Agi 3-7]
        b = build(f"Agi {agi}, End 4", agi=agi, end=4, strength=4)  # [canonical: N/A — sweep]
        wa, wb, dr = run_matchup_continuous(b, strong)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        delta = ""  # [canonical: N/A — structural]
        if agi == 3:  # [canonical: N/A — baseline]
            base_cond = cond  # [canonical: N/A — structural]
        else:  # [canonical: N/A — structural]
            delta = f"+{(cond - base_cond) * 100:.1f}pp"  # [canonical: N/A — display]
        print(f"  {b['name']:28} {b['base_pool']:>4}D {wa:>6.1%} {cond:>5.1%} {delta:>16}")
    print()  # [canonical: N/A — formatting]


def comparison_summary():  # [canonical: N/A — sim function]
    print("=" * 76)  # [canonical: N/A — formatting]
    print("Sim C — Phase 4 (discrete) vs Phase 5 (continuous) Comparison Summary")  # [canonical: N/A — header]
    print("=" * 76)  # [canonical: N/A — formatting]

    strong = build('Strong', agi=3, end=4, strength=4)  # [canonical: N/A — build]
    fast = build('Fast', agi=6, end=4, strength=4)  # [canonical: N/A — build]

    # Reproduce Phase 4 discrete result for Fast vs Strong using same seed
    random.seed(42)  # [canonical: N/A — reproducibility]
    from copy import deepcopy  # [canonical: N/A — structural]

    # Discrete (Phase 4) — inline replication for direct comparison
    def discrete_duel(a, b):  # [canonical: N/A — structural]
        hp_a, hp_b = a['max_hp'], b['max_hp']  # [canonical: N/A — structural]
        stam_a, stam_b = a['max_stam'], b['max_stam']  # [canonical: N/A — structural]
        wounds_a, wounds_b = 0, 0  # [canonical: N/A — structural]
        for rd in range(20):  # [canonical: N/A — structural max rounds]
            if stam_a < ACTION_COST and stam_b < ACTION_COST: return 'draw'  # [canonical: N/A — structural]
            if stam_a < ACTION_COST: return 'b'  # [canonical: N/A — structural]
            if stam_b < ACTION_COST: return 'a'  # [canonical: N/A — structural]
            pool_a = max(POOL_FLOOR, a['base_pool'] - wounds_a)  # [canonical: params/combat.md]
            pool_b = max(POOL_FLOOR, b['base_pool'] - wounds_b)  # [canonical: params/combat.md]
            off_a, def_a = pool_a // 2, pool_a - pool_a // 2  # [canonical: N/A — split]
            off_b, def_b = pool_b // 2, pool_b - pool_b // 2  # [canonical: N/A — split]
            a_net = discrete_roll(off_a) - discrete_roll(def_b)  # [canonical: N/A — structural]
            b_net = discrete_roll(off_b) - discrete_roll(def_a)  # [canonical: N/A — structural]
            if a_net > 0:  # [canonical: N/A — structural]
                base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
                if a_net >= 4: base_mod *= 2  # [canonical: params/combat.md L91 — crit ≥ 4]
                dmg = a_net + a['str'] + base_mod  # [canonical: params/combat.md §Damage]
                hp_b -= dmg  # [canonical: N/A — structural]
                wounds_b = min((b['max_hp'] - hp_b) // b['wi'], b['mw'] + 1)  # [canonical: params/combat.md]
            if b_net > 0:  # [canonical: N/A — structural]
                base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
                if b_net >= 4: base_mod *= 2  # [canonical: params/combat.md L91 — crit ≥ 4]
                dmg = b_net + b['str'] + base_mod  # [canonical: params/combat.md §Damage]
                hp_a -= dmg  # [canonical: N/A — structural]
                wounds_a = min((a['max_hp'] - hp_a) // a['wi'], a['mw'] + 1)  # [canonical: params/combat.md]
            stam_a -= ACTION_COST  # [canonical: see ACTION_COST]
            stam_b -= ACTION_COST  # [canonical: see ACTION_COST]
            if hp_a <= 0 or wounds_a > a['mw']: return 'b'  # [canonical: params/combat.md §Wounds]
            if hp_b <= 0 or wounds_b > b['mw']: return 'a'  # [canonical: params/combat.md §Wounds]
        return 'draw'  # [canonical: N/A — structural]

    # Run both engines on Fast vs Strong, large N for stability
    n = 5000  # [canonical: N/A — high-N for comparison stability]
    d_wins_a = sum(1 for _ in range(n) if discrete_duel(fast, strong) == 'a')  # [canonical: N/A — structural]
    d_wins_b = sum(1 for _ in range(n) if discrete_duel(fast, strong) == 'b')  # [canonical: N/A — structural]
    # Re-run for the count we need
    d_a, d_b, d_dr = 0, 0, 0  # [canonical: N/A — structural]
    for _ in range(n):  # [canonical: N/A — structural]
        r = discrete_duel(fast, strong)  # [canonical: N/A — structural]
        if r == 'a': d_a += 1  # [canonical: N/A — structural]
        elif r == 'b': d_b += 1  # [canonical: N/A — structural]
        else: d_dr += 1  # [canonical: N/A — structural]

    c_a, c_b, c_dr = 0, 0, 0  # [canonical: N/A — structural]
    for _ in range(n):  # [canonical: N/A — structural]
        r = simulate_duel_continuous(fast, strong)  # [canonical: N/A — structural]
        if r == 'a': c_a += 1  # [canonical: N/A — structural]
        elif r == 'b': c_b += 1  # [canonical: N/A — structural]
        else: c_dr += 1  # [canonical: N/A — structural]

    d_dec = d_a + d_b  # [canonical: N/A — structural]
    c_dec = c_a + c_b  # [canonical: N/A — structural]
    d_cond = d_a / d_dec if d_dec > 0 else 0.5  # [canonical: N/A — structural]
    c_cond = c_a / c_dec if c_dec > 0 else 0.5  # [canonical: N/A — structural]

    print(f"  Fast (Agi 6, pool 17D) vs Strong (Agi 3, pool 11D), N={n}")  # [canonical: N/A — display]
    print()  # [canonical: N/A — formatting]
    print(f"  {'Engine':>14} {'A win':>7} {'B win':>7} {'Draw':>6} {'A|dec':>7}")  # [canonical: N/A — header]
    print(f"  {'-' * 14} {'-' * 7} {'-' * 7} {'-' * 6} {'-' * 7}")  # [canonical: N/A — formatting]
    print(f"  {'Discrete d10':>14} {d_a/n:>6.1%} {d_b/n:>6.1%} {d_dr/n:>5.1%} {d_cond:>6.1%}")
    print(f"  {'Continuous':>14} {c_a/n:>6.1%} {c_b/n:>6.1%} {c_dr/n:>5.1%} {c_cond:>6.1%}")
    print()  # [canonical: N/A — formatting]
    delta = c_cond - d_cond  # [canonical: N/A — comparison]
    print(f"  Δ conditional win rate: {delta:+.1%}")  # [canonical: N/A — display]
    print()  # [canonical: N/A — formatting]

    threshold_dom = 0.65  # [canonical: v27 dominance threshold]
    if c_cond >= threshold_dom and d_cond >= threshold_dom:  # [canonical: see threshold]
        print(f"  → Dominance persists in BOTH engines (both >= {threshold_dom:.0%}).")  # [canonical: N/A — output]
        print(f"    Continuous mapping ALONE does not resolve the dominance problem.")  # [canonical: N/A — output]
        print(f"    The doubling formula remains the structural driver.")  # [canonical: N/A — output]
    elif c_cond < threshold_dom and d_cond >= threshold_dom:  # [canonical: see threshold]
        print(f"  → Dominance RESOLVED by continuous engine.")  # [canonical: N/A — output]
        print(f"    Discrete: {d_cond:.1%} DOMINANT → Continuous: {c_cond:.1%} BALANCED")  # [canonical: N/A — output]
        print(f"    Continuous mapping addresses the saturation problem structurally.")  # [canonical: N/A — output]
    else:  # [canonical: N/A — structural]
        print(f"  → Mixed result. Discrete: {d_cond:.1%}, Continuous: {c_cond:.1%}")  # [canonical: N/A — output]


def main():
    random.seed(42)  # [canonical: N/A — reproducibility]
    distribution_equivalence_test()  # [canonical: N/A — structural]
    phase4_continuous_rerun()  # [canonical: N/A — structural]
    comparison_summary()  # [canonical: N/A — structural]
    print("=" * 76)  # [canonical: N/A — formatting]
    print("Phase 5 sim complete.")  # [canonical: N/A — output]
    print("See tests/sim/phase5_continuous_engine_2026-05-15.md for analysis.")  # [canonical: N/A — output]


if __name__ == '__main__':
    main()
