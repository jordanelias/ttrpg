#!/usr/bin/env python3
# Phase 8 sim — Better-tuned Smart AI v2; resolves WS-H-3 and WS-H-4
# Trigger: workstream meta-audit 2026-05-15 flagged that Phase 7 Smart AI was  # [canonical: N/A — doc]
# under-tuned (Smart-vs-Smart produced sim artifacts: 100% Fast in Fast/Strong;  # [canonical: N/A — doc]
# 6.8% Tough in Tough/Strong). WS-H-4 specifically: same-pool End-dominance  # [canonical: N/A — doc]
# collapse from 82% to 7% likely caused by Take Breath threshold + Full Guard  # [canonical: N/A — doc]
# interaction. This sim fixes both AI defects and re-runs the same matchups.  # [canonical: N/A — doc]
#
# Smart v2 AI changes from Phase 7:  # [canonical: N/A — doc]
#   1. Take Breath threshold raised from <=5 to <=8 (fixes high-stam skip)  # [canonical: N/A — sim refinement]
#   2. Full Guard rule: genuine last-stand only (hp<15% AND wounds==MW)  # [canonical: N/A — sim refinement]
#   3. Feint trigger: when own pool is disadvantaged AND own pool >=5  # [canonical: N/A — sim refinement]
#   4. Pool-advantaged side defaults to Strike (efficient closeout)  # [canonical: N/A — sim refinement]

import random
import math
from collections import defaultdict

# Per-die distribution (Phase 5; F13-corrected — params/core.md §EV table post-721acc15)
DIE_MEAN_TN7 = 0.4  # [canonical: params/core.md §Expected Value, TN 7 row, post-F13]
DIE_STD_TN7 = 0.8  # [canonical: params/core.md §Expected Value, TN 7 row, post-F13]

TN = 7  # [canonical: params/core.md §TN Values — Standard]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]
COMBAT_POOL_FLOOR = 5  # [canonical: params/combat.md L14]
FEINT_MIN_COMMIT = 3  # [canonical: params/combat.md PP-294]
ACTION_COST = 5  # [canonical: params/combat.md L15]
TAKE_BREATH_COST = 3  # [canonical: params/combat.md L15 — defensive 3]
TAKE_BREATH_TRIGGER = 8  # [canonical: N/A — Phase 8 raised from 5; addresses Phase 7 discrete-action skip artifact for high-stam builds]
WEAPON_DAMAGE_MOD = 3  # [canonical: params/combat.md damage table — Light Blade Cut vs None]
STR_MULT = 1.0  # [canonical: params/combat.md §Damage Formula]
CRIT_MAGNITUDE = 4.0  # [canonical: params/combat.md L91 — PP-717 D3]


def continuous_roll(n):
    if n <= 0:  # [canonical: N/A — structural]
        return 0.0  # [canonical: N/A — structural]
    return random.gauss(DIE_MEAN_TN7 * n, DIE_STD_TN7 * math.sqrt(n))  # [canonical: see DIE constants]


def combat_pool(agi, hist):
    return max(COMBAT_POOL_FLOOR, agi * 2 + hist + 3)  # [canonical: params/combat.md L14]


def max_wounds(end):
    return min(end // 2 + 1, 3)  # [canonical: params/combat.md L138]


def wound_interval(end):
    return end + 6  # [canonical: derived_stats §4.1]


def max_health(end):
    return wound_interval(end) * (max_wounds(end) + 1)  # [canonical: derived_stats §4.1]


def max_stamina(end):
    return 15 + end * 2  # [canonical: Architecture C sim baseline]


# ── Smart AI v2 ──────────────────────────────────────────────────────────

def choose_action_strike_only(state):
    return 'strike'  # [canonical: N/A — baseline]


def choose_action_smart_v2(state):
    own_pool = state['own_pool']  # [canonical: N/A — state]
    opp_pool = state['opp_pool']  # [canonical: N/A — state]
    own_hp_pct = state['own_hp_pct']  # [canonical: N/A — state]
    own_stam = state['own_stam']  # [canonical: N/A — state]
    own_wounds = state['own_wounds']  # [canonical: N/A — state]
    own_max_wounds = state['own_max_wounds']  # [canonical: N/A — state]

    # (1) Stamina recovery — raised threshold so high-stam builds also trigger
    if TAKE_BREATH_COST <= own_stam <= TAKE_BREATH_TRIGGER:  # [canonical: see TAKE_BREATH_TRIGGER]
        return 'take_breath'  # [canonical: N/A — action choice]

    # (2) Last-stand Full Guard: only when truly low and out of wounds budget
    if own_hp_pct < 0.15 and own_wounds >= own_max_wounds:  # [canonical: N/A — Phase 8 refinement]
        return 'full_guard'  # [canonical: N/A — action choice]

    # (3) Pool-disadvantaged: alternate Feint (setup pool reduction) then Strike (exploit)
    # Feinting every round wastes the reduction per PP-294 non-stacking rule
    pool_gap = opp_pool - own_pool  # [canonical: N/A — state]
    if pool_gap >= 2 and own_pool >= FEINT_MIN_COMMIT + 2:  # [canonical: PP-294 min 3 + 2 def reserve]
        # Even rounds: setup with Feint. Odd rounds: exploit reduction with Strike.
        return 'feint' if state['rd'] % 2 == 0 else 'strike'  # [canonical: PP-294 non-stacking implies alternation]

    # (4) Default: Strike (especially when pool-advantaged)
    return 'strike'  # [canonical: N/A — default]


def choose_action_underdog_feint(state):
    # Phase 7 baseline retained for direct comparison
    own_pool = state['own_pool']  # [canonical: N/A — state]
    opp_pool = state['opp_pool']  # [canonical: N/A — state]
    own_stam = state['own_stam']  # [canonical: N/A — state]
    if TAKE_BREATH_COST <= own_stam <= ACTION_COST:  # [canonical: params/combat.md L15]
        return 'take_breath'  # [canonical: N/A — action choice]
    if own_pool < opp_pool and own_pool >= FEINT_MIN_COMMIT + 2:  # [canonical: PP-294]
        return 'feint' if state['rd'] % 2 == 0 else 'strike'  # [canonical: N/A — heuristic alternation]
    return 'strike'  # [canonical: N/A — default]


STRATEGY_FNS = {
    'strike_only': choose_action_strike_only,  # [canonical: N/A — structural]
    'smart_v2': choose_action_smart_v2,  # [canonical: N/A — structural]
    'underdog_feint': choose_action_underdog_feint,  # [canonical: N/A — structural]
}


# ── Combat simulation (same as Phase 7) ──────────────────────────────────

def simulate_duel(build_a, build_b, strategy_a='strike_only', strategy_b='strike_only', max_rounds=30):  # [canonical: N/A — Phase 8 raised max from 20 to 30 to let longer fights play out]
    hp_a, hp_b = build_a['max_hp'], build_b['max_hp']  # [canonical: N/A — structural]
    stam_a, stam_b = build_a['max_stam'], build_b['max_stam']  # [canonical: N/A — structural]
    wounds_a, wounds_b = 0, 0  # [canonical: N/A — structural]
    wi_a, wi_b = build_a['wi'], build_b['wi']  # [canonical: N/A — structural]
    pending_reduction_a, pending_reduction_b = 0, 0  # [canonical: params/combat.md PP-294]

    fn_a = STRATEGY_FNS[strategy_a]  # [canonical: see STRATEGY_FNS]
    fn_b = STRATEGY_FNS[strategy_b]  # [canonical: see STRATEGY_FNS]

    for rd in range(max_rounds):  # [canonical: N/A — structural]
        if stam_a < TAKE_BREATH_COST and stam_b < TAKE_BREATH_COST:  # [canonical: params/combat.md L15]
            return 'draw'  # [canonical: N/A — structural]
        if stam_a < TAKE_BREATH_COST:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if stam_b < TAKE_BREATH_COST:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

        eff_pool_a = max(POOL_FLOOR, build_a['base_pool'] - wounds_a - pending_reduction_a)  # [canonical: PP-294 + params/combat wound penalty]
        eff_pool_b = max(POOL_FLOOR, build_b['base_pool'] - wounds_b - pending_reduction_b)  # [canonical: PP-294]
        pending_reduction_a, pending_reduction_b = 0, 0  # [canonical: PP-294 non-stacking]

        state_a = {  # [canonical: N/A — structural]
            'own_pool': eff_pool_a, 'opp_pool': eff_pool_b,  # [canonical: N/A — state]
            'own_hp_pct': hp_a / build_a['max_hp'],  # [canonical: N/A — state]
            'opp_hp_pct': hp_b / build_b['max_hp'],  # [canonical: N/A — state]
            'own_stam': stam_a, 'rd': rd,  # [canonical: N/A — state]
            'own_wounds': wounds_a, 'own_max_wounds': build_a['mw'],  # [canonical: N/A — state]
        }
        state_b = {  # [canonical: N/A — structural]
            'own_pool': eff_pool_b, 'opp_pool': eff_pool_a,  # [canonical: N/A — state]
            'own_hp_pct': hp_b / build_b['max_hp'],  # [canonical: N/A — state]
            'opp_hp_pct': hp_a / build_a['max_hp'],  # [canonical: N/A — state]
            'own_stam': stam_b, 'rd': rd,  # [canonical: N/A — state]
            'own_wounds': wounds_b, 'own_max_wounds': build_b['mw'],  # [canonical: N/A — state]
        }

        action_a = fn_a(state_a)  # [canonical: N/A — structural]
        action_b = fn_b(state_b)  # [canonical: N/A — structural]

        def allocate(action, pool):  # [canonical: N/A — structural]
            if action == 'strike':  # [canonical: params/combat.md L207]
                return pool / 2, pool / 2  # [canonical: N/A — 50/50 split sim baseline]
            elif action == 'feint':  # [canonical: params/combat.md PP-294]
                feint_commit = max(FEINT_MIN_COMMIT, int(pool * 0.6))  # [canonical: PP-294 N>=3]
                return feint_commit, max(POOL_FLOOR, pool - feint_commit)  # [canonical: PP-294]
            elif action == 'full_guard':  # [canonical: params/combat.md L185]
                return 0, pool  # [canonical: N/A — all pool to defence]
            elif action == 'take_breath':  # [canonical: params/combat.md L185]
                return 0, pool  # [canonical: N/A — defensive while restoring]
            return pool / 2, pool / 2  # [canonical: N/A — default]

        off_a, def_a = allocate(action_a, eff_pool_a)  # [canonical: see allocate]
        off_b, def_b = allocate(action_b, eff_pool_b)  # [canonical: see allocate]

        a_off_hits = continuous_roll(off_a) if action_a in ('strike', 'feint') else 0  # [canonical: N/A — structural]
        b_def_hits = continuous_roll(def_b)  # [canonical: N/A — structural]
        a_net = a_off_hits - b_def_hits if action_a in ('strike', 'feint') else 0  # [canonical: params/combat.md §contested]

        b_off_hits = continuous_roll(off_b) if action_b in ('strike', 'feint') else 0  # [canonical: N/A — structural]
        a_def_hits = continuous_roll(def_a)  # [canonical: N/A — structural]
        b_net = b_off_hits - a_def_hits if action_b in ('strike', 'feint') else 0  # [canonical: params/combat.md §contested]

        if action_a == 'strike' and a_net > 0:  # [canonical: N/A — hit threshold]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            if a_net >= CRIT_MAGNITUDE:  # [canonical: see CRIT_MAGNITUDE]
                base_mod *= 2  # [canonical: params/combat.md §Damage]
            dmg = max(0, a_net + build_a['str'] * STR_MULT + base_mod)  # [canonical: params/combat.md §Damage Formula]
            hp_b -= dmg  # [canonical: N/A — structural]
            new_wounds = int((build_b['max_hp'] - hp_b) // wi_b)  # [canonical: params/combat.md §Wounds]
            wounds_b = min(new_wounds, build_b['mw'] + 1)  # [canonical: params/combat.md §Wounds]

        if action_b == 'strike' and b_net > 0:  # [canonical: N/A — hit threshold]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            if b_net >= CRIT_MAGNITUDE:  # [canonical: see CRIT_MAGNITUDE]
                base_mod *= 2  # [canonical: params/combat.md §Damage]
            dmg = max(0, b_net + build_b['str'] * STR_MULT + base_mod)  # [canonical: params/combat.md §Damage]
            hp_a -= dmg  # [canonical: N/A — structural]
            new_wounds = int((build_a['max_hp'] - hp_a) // wi_a)  # [canonical: params/combat.md §Wounds]
            wounds_a = min(new_wounds, build_a['mw'] + 1)  # [canonical: params/combat.md §Wounds]

        if action_a == 'feint' and a_net > 0:  # [canonical: PP-294]
            pending_reduction_b = max(pending_reduction_b, int(a_net))  # [canonical: PP-294 non-stacking]
        if action_b == 'feint' and b_net > 0:  # [canonical: PP-294]
            pending_reduction_a = max(pending_reduction_a, int(b_net))  # [canonical: PP-294]

        if action_a == 'take_breath':  # [canonical: params/combat.md L185]
            stam_a = min(build_a['max_stam'], stam_a + 20 - TAKE_BREATH_COST)  # [canonical: Take a Breath restores]
        else:  # [canonical: N/A — structural]
            stam_a -= ACTION_COST  # [canonical: see ACTION_COST]
        if action_b == 'take_breath':  # [canonical: params/combat.md L185]
            stam_b = min(build_b['max_stam'], stam_b + 20 - TAKE_BREATH_COST)  # [canonical: Take a Breath restores]
        else:  # [canonical: N/A — structural]
            stam_b -= ACTION_COST  # [canonical: see ACTION_COST]

        a_felled = hp_a <= 0 or wounds_a > build_a['mw']  # [canonical: params/combat.md §Wounds]
        b_felled = hp_b <= 0 or wounds_b > build_b['mw']  # [canonical: params/combat.md §Wounds]
        if a_felled and b_felled:  # [canonical: N/A — structural]
            return 'draw'  # [canonical: N/A — structural]
        if a_felled:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if b_felled:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

    return 'draw'  # [canonical: N/A — max-rounds]


def build(name, agi, end, strength, hist=2):
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


def run_matchup(a, b, strat_a='strike_only', strat_b='strike_only', n=3000):  # [canonical: N/A — sim N, matches Phases 4-7 baseline]
    wins_a, wins_b, draws = 0, 0, 0  # [canonical: N/A — structural]
    for _ in range(n):  # [canonical: N/A — structural]
        r = simulate_duel(a, b, strat_a, strat_b)  # [canonical: N/A — structural]
        if r == 'a': wins_a += 1  # [canonical: N/A — structural]
        elif r == 'b': wins_b += 1  # [canonical: N/A — structural]
        else: draws += 1  # [canonical: N/A — structural]
    return wins_a / n, wins_b / n, draws / n  # [canonical: N/A — structural]


def main():
    random.seed(42)  # [canonical: N/A — reproducibility]
    threshold = 0.65  # [canonical: audit/lane-a/all_directions_ners_v27.md — 65% dominance threshold]

    print("=" * 84)  # [canonical: N/A — formatting]
    print("Phase 8 sim — Better-tuned Smart AI v2 — resolves WS-H-3 and WS-H-4")  # [canonical: N/A — header]
    print("=" * 84)  # [canonical: N/A — formatting]
    print(f"  Smart v2 changes from Phase 7:")  # [canonical: N/A — display]
    print(f"    Take Breath threshold raised <=5 to <=8 (fixes high-stam skip)")  # [canonical: N/A — display]
    print(f"    Full Guard: last-stand only (hp<15% AND wounds==MW)")  # [canonical: N/A — display]
    print(f"    Feint triggers when own pool disadvantaged AND >=5D")  # [canonical: N/A — display]
    print(f"  Engine: continuous Normal(0.4*pool, 0.8*sqrt(pool))")  # [canonical: see DIE constants]
    print(f"  N = 3000 duels per matchup, seed=42, max_rounds=30")  # [canonical: N/A — display]
    print()  # [canonical: N/A — formatting]

    fast = build('Fast (Agi 6, End 4)', 6, 4, 4)  # [canonical: N/A — build matrix]
    strong = build('Strong (Agi 3, End 4)', 3, 4, 4)  # [canonical: N/A — build matrix]
    tough = build('Tough (Agi 3, End 6)', 3, 6, 4)  # [canonical: N/A — build matrix]

    # AGI dominance test
    print("AGI dominance: Fast (Agi 6) vs Strong (Agi 3)")  # [canonical: N/A — header]
    print(f"  {'Mode':36} {'A=Fast':>8} {'B=Strong':>10} {'Fast cond':>10} {'Status':>10}")  # [canonical: N/A — header]
    print(f"  {'-' * 36} {'-' * 8} {'-' * 10} {'-' * 10} {'-' * 10}")  # [canonical: N/A — formatting]
    agi_modes = [  # [canonical: N/A — structural]
        ('Strike-only baseline', 'strike_only', 'strike_only'),  # [canonical: N/A — sim]
        ('Smart v2 both sides', 'smart_v2', 'smart_v2'),  # [canonical: N/A — sim]
        ('Underdog Feints (Phase 7 reference)', 'strike_only', 'underdog_feint'),  # [canonical: N/A — sim]
    ]
    agi_results = {}  # [canonical: N/A — structural]
    for label, sa, sb in agi_modes:  # [canonical: N/A — structural]
        wa, wb, dr = run_matchup(fast, strong, sa, sb)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        agi_results[label] = cond  # [canonical: N/A — structural]
        if cond >= threshold:  # [canonical: see threshold]
            status = "DOMINANT"  # [canonical: N/A — output]
        elif cond <= 1 - threshold:  # [canonical: see threshold]
            status = "B-domin"  # [canonical: N/A — output]
        elif 0.4 <= cond <= 0.6:  # [canonical: N/A — balanced band]
            status = "BALANCED"  # [canonical: N/A — output]
        else:  # [canonical: N/A — structural]
            status = "tilted"  # [canonical: N/A — output]
        print(f"  {label:36} {sa:>8} {sb:>10} {cond:>9.1%} {status:>10}")
    print()  # [canonical: N/A — formatting]

    # END dominance test
    print("END dominance: Tough (Agi 3, End 6) vs Strong (Agi 3, End 4)")  # [canonical: N/A — header]
    print(f"  {'Mode':36} {'Tough cond':>11} {'Status':>10}")  # [canonical: N/A — header]
    print(f"  {'-' * 36} {'-' * 11} {'-' * 10}")  # [canonical: N/A — formatting]
    end_results = {}  # [canonical: N/A — structural]
    for label, sa, sb in agi_modes:  # [canonical: N/A — structural]
        wa, wb, dr = run_matchup(tough, strong, sa, sb)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        end_results[label] = cond  # [canonical: N/A — structural]
        if cond >= threshold:  # [canonical: see threshold]
            status = "DOMINANT"  # [canonical: N/A — output]
        elif cond <= 1 - threshold:  # [canonical: see threshold]
            status = "B-domin"  # [canonical: N/A — output]
        elif 0.4 <= cond <= 0.6:  # [canonical: N/A — balanced band]
            status = "BALANCED"  # [canonical: N/A — output]
        else:  # [canonical: N/A — structural]
            status = "tilted"  # [canonical: N/A — output]
        print(f"  {label:36} {cond:>10.1%} {status:>10}")
    print()  # [canonical: N/A — formatting]

    # Build-investment ROI with Smart v2
    print("Build-investment ROI vs Strong (Smart v2 both sides):")  # [canonical: N/A — header]
    print(f"  {'Build':28} {'Pool':>5} {'Win%':>7} {'Cond':>7} {'Δ cond vs Agi-3':>17}")  # [canonical: N/A — header]
    print(f"  {'-' * 28} {'-' * 5} {'-' * 7} {'-' * 7} {'-' * 17}")  # [canonical: N/A — formatting]
    base_cond = None  # [canonical: N/A — structural]
    for agi in (3, 4, 5, 6, 7):  # [canonical: params/core.md §Attributes — Agi 3-7]
        b = build(f"Agi {agi}, End 4", agi, 4, 4)  # [canonical: N/A — sweep]
        wa, wb, dr = run_matchup(b, strong, 'smart_v2', 'smart_v2')  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        delta = ""  # [canonical: N/A — structural]
        if agi == 3:  # [canonical: N/A — baseline]
            base_cond = cond  # [canonical: N/A — structural]
        else:  # [canonical: N/A — structural]
            sign = "+" if cond >= base_cond else ""  # [canonical: N/A — formatting]
            delta = f"{sign}{(cond - base_cond) * 100:.1f}pp"  # [canonical: N/A — display]
        print(f"  {b['name']:28} {b['base_pool']:>4}D {wa:>6.1%} {cond:>6.1%} {delta:>17}")
    print()  # [canonical: N/A — formatting]

    # Verdict
    print("=" * 84)  # [canonical: N/A — formatting]
    print("Verdict:")  # [canonical: N/A — output]
    p7_under = 0.349  # [canonical: tests/sim/phase7_action_triangle_2026-05-15.md — Phase 7 Underdog result]
    p7_smart_agi = 1.000  # [canonical: tests/sim/phase7_action_triangle_2026-05-15.md — Phase 7 Smart anomaly]
    p7_smart_end = 0.068  # [canonical: tests/sim/phase7_action_triangle_2026-05-15.md — Phase 7 End anomaly]
    smart_agi = agi_results['Smart v2 both sides']  # [canonical: N/A — comparison]
    smart_end = end_results['Smart v2 both sides']  # [canonical: N/A — comparison]
    print(f"  Phase 7 Smart-vs-Smart Fast/Strong (artifact):  {p7_smart_agi:.1%}")  # [canonical: see p7_smart_agi]
    print(f"  Phase 8 Smart-v2 Fast/Strong:                  {smart_agi:.1%}")  # [canonical: N/A — display]
    print(f"  Phase 7 Underdog Feints Fast/Strong:           {p7_under:.1%}")  # [canonical: see p7_under]
    print()  # [canonical: N/A — formatting]
    print(f"  Phase 7 Smart-vs-Smart Tough/Strong (artifact): {p7_smart_end:.1%}")  # [canonical: see p7_smart_end]
    print(f"  Phase 8 Smart-v2 Tough/Strong:                 {smart_end:.1%}")  # [canonical: N/A — display]
    print()  # [canonical: N/A — formatting]
    if 0.4 <= smart_agi <= 0.6:  # [canonical: N/A — balanced band]
        print("  → Agi-dominance: Smart v2 produces BALANCED outcome.")  # [canonical: N/A — output]
        print("    Phase 7 Underdog finding (~35%) replicates with symmetric AI.")  # [canonical: N/A — output]
    elif smart_agi >= 0.65:  # [canonical: see threshold]
        print("  → Agi-dominance: Smart v2 still shows Fast dominance.")  # [canonical: N/A — output]
        print("    Phase 7 Underdog inversion was strategy-specific, not balance-level.")  # [canonical: N/A — output]
    else:  # [canonical: N/A — structural]
        print(f"  → Agi-dominance: Smart v2 gives Fast {smart_agi:.1%} — tilted but not dominant.")  # [canonical: N/A — output]
    if 0.4 <= smart_end <= 0.6:  # [canonical: N/A — balanced band]
        print("  → End-dominance: Smart v2 produces BALANCED outcome.")  # [canonical: N/A — output]
    elif smart_end >= 0.65:  # [canonical: see threshold]
        print("  → End-dominance: Smart v2 confirms Tough dominance (real, not artifact).")  # [canonical: N/A — output]
    elif smart_end <= 0.35:  # [canonical: N/A — inverted band]
        print(f"  → End-dominance: Smart v2 still shows Strong winning ({smart_end:.1%}).")  # [canonical: N/A — output]
        print("    Phase 7 inversion was not artifact; needs further investigation.")  # [canonical: N/A — output]
    else:  # [canonical: N/A — structural]
        print(f"  → End-dominance: Smart v2 gives Tough {smart_end:.1%} — tilted but not dominant.")  # [canonical: N/A — output]
    print("=" * 84)  # [canonical: N/A — formatting]


if __name__ == '__main__':
    main()
