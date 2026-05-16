#!/usr/bin/env python3
# Phase 7 sim — Action triangle (Strike/Feint/Full Guard) impact on dominance
# Trigger: Phase 6 showed pool formula alone doesn't solve dominance; the  # [canonical: N/A — doc]
# action triangle is the most under-tested lever. This sim adds Feint and  # [canonical: N/A — doc]
# Full Guard alongside Strike, with AI strategies for each side, to see  # [canonical: N/A — doc]
# whether tactical depth closes the gap.  # [canonical: N/A — doc]
#
# Mechanics modeled (canon):  # [canonical: N/A — doc]
#   - Initiative declaration order (PP-232 — initiative holder declares last)  # [canonical: params/combat.md L119-124]
#   - Strike: standard attack with Off/Def split  # [canonical: params/combat.md L207]
#   - Feint (PP-294): commit N>=3 to Off; on hit opponent loses margin dice  # [canonical: params/combat.md L252-261]
#     next round, floor 1D, non-stacking  # [canonical: params/combat.md PP-294]
#   - Full Guard: all pool to Defence, no Offence  # [canonical: params/combat.md L185]
#   - Take a Breath: restores Stamina to max (uses turn)  # [canonical: params/combat.md L185]
#
# Three strategy modes compared:  # [canonical: N/A — doc]
#   STRIKE_ONLY — both sides Strike every round (Phase 6 baseline)  # [canonical: N/A — sim config]
#   SMART — both sides use optimal action selection  # [canonical: N/A — sim config]
#   UNDERDOG_FEINT — disadvantaged side uses Feint actively to close gap  # [canonical: N/A — sim config]

import random
import math
from collections import defaultdict

# Per-die distribution (Phase 5)
DIE_MEAN_TN7 = 0.4  # [canonical: derived from params/core.md §dice — face dist at TN 7]
DIE_STD_TN7 = 0.8  # [canonical: derived from params/core.md §dice — variance 0.64]

# Engine constants
TN = 7  # [canonical: params/core.md §TN Values]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]
COMBAT_POOL_FLOOR = 5  # [canonical: params/combat.md L14 — combat pool min 5]
FEINT_POOL_FLOOR_AFTER = 1  # [canonical: params/combat.md PP-294 — Min 1D]
FEINT_MIN_COMMIT = 3  # [canonical: params/combat.md PP-294 — N>=3]
ACTION_COST = 5  # [canonical: params/combat.md L15]
TAKE_BREATH_COST = 3  # [canonical: params/combat.md L15 — defensive 3]
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


# ── AI Strategy ──────────────────────────────────────────────────────────

# Action selection per build, considering: own pool, opp pool, own HP%, opp HP%,
# own stam, init holder, pending feint reduction

def choose_action_strike_only(state):
    return 'strike'  # [canonical: N/A — sim baseline mode]


def choose_action_smart(state):
    own_pool = state['own_pool']  # [canonical: N/A — state]
    opp_pool = state['opp_pool']  # [canonical: N/A — state]
    own_hp_pct = state['own_hp_pct']  # [canonical: N/A — state]
    own_stam = state['own_stam']  # [canonical: N/A — state]

    # Low stamina: take a breath
    if own_stam <= ACTION_COST and own_stam >= TAKE_BREATH_COST:  # [canonical: params/combat.md L15]
        return 'take_breath'  # [canonical: N/A — action choice]

    # Low HP: full guard if no other choice
    if own_hp_pct < 0.25 and own_pool < opp_pool:  # [canonical: N/A — sim heuristic]
        return 'full_guard'  # [canonical: N/A — action choice]

    # Pool disadvantage: feint to close the gap (Feint is a force multiplier)
    pool_gap = opp_pool - own_pool  # [canonical: N/A — state]
    if pool_gap >= 3 and own_pool >= FEINT_MIN_COMMIT + 2:  # [canonical: PP-294 min 3 + 2 def reserve]
        return 'feint'  # [canonical: N/A — action choice]

    # Otherwise strike
    return 'strike'  # [canonical: N/A — default]


def choose_action_underdog_feint(state):
    own_pool = state['own_pool']  # [canonical: N/A — state]
    opp_pool = state['opp_pool']  # [canonical: N/A — state]
    own_stam = state['own_stam']  # [canonical: N/A — state]

    if own_stam <= ACTION_COST and own_stam >= TAKE_BREATH_COST:  # [canonical: params/combat.md L15]
        return 'take_breath'  # [canonical: N/A — action choice]

    # Aggressive feinting if disadvantaged
    if own_pool < opp_pool and own_pool >= FEINT_MIN_COMMIT + 2:  # [canonical: PP-294]
        # Feint every other round (mix with strike to maintain pressure)
        return 'feint' if state['rd'] % 2 == 0 else 'strike'  # [canonical: N/A — heuristic]

    return 'strike'  # [canonical: N/A — default]


STRATEGY_FNS = {
    'strike_only': choose_action_strike_only,  # [canonical: N/A — structural]
    'smart': choose_action_smart,  # [canonical: N/A — structural]
    'underdog_feint': choose_action_underdog_feint,  # [canonical: N/A — structural]
}


# ── Combat simulation with action triangle ──────────────────────────────

def simulate_duel(build_a, build_b, strategy_a='strike_only', strategy_b='strike_only', max_rounds=20):  # [canonical: N/A — structural cutoff]
    hp_a, hp_b = build_a['max_hp'], build_b['max_hp']  # [canonical: N/A — initial state]
    stam_a, stam_b = build_a['max_stam'], build_b['max_stam']  # [canonical: N/A — initial state]
    wounds_a, wounds_b = 0, 0  # [canonical: N/A — initial state]
    wi_a, wi_b = build_a['wi'], build_b['wi']  # [canonical: N/A — structural]

    # Initiative: higher Attunement; if no Attn stat, use Agi (proxy)
    init_a = build_a.get('attn', build_a['agi'])  # [canonical: params/combat.md L116 — Attunement drives initiative]
    init_b = build_b.get('attn', build_b['agi'])  # [canonical: params/combat.md L116]
    init_holder = 'a' if init_a > init_b else ('b' if init_b > init_a else 'a')  # [canonical: PP-239 — tiebreak Agility, sim defaults to a]

    # Feint state — pool reduction pending for next round
    pending_reduction_a, pending_reduction_b = 0, 0  # [canonical: params/combat.md PP-294 — non-stacking, resets next round]

    fn_a = STRATEGY_FNS[strategy_a]  # [canonical: see STRATEGY_FNS]
    fn_b = STRATEGY_FNS[strategy_b]  # [canonical: see STRATEGY_FNS]

    for rd in range(max_rounds):  # [canonical: N/A — structural cap]
        # Stamina exhaustion check
        if stam_a < TAKE_BREATH_COST and stam_b < TAKE_BREATH_COST:  # [canonical: params/combat.md — min stam]
            return 'draw'  # [canonical: N/A — structural]
        if stam_a < TAKE_BREATH_COST:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if stam_b < TAKE_BREATH_COST:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

        # Apply pool reductions from prior round's Feint hits
        eff_pool_a = max(POOL_FLOOR, build_a['base_pool'] - wounds_a - pending_reduction_a)  # [canonical: PP-294 floor + params/combat wound penalty]
        eff_pool_b = max(POOL_FLOOR, build_b['base_pool'] - wounds_b - pending_reduction_b)  # [canonical: PP-294 floor]
        # Reset reductions — Feint is non-stacking, applies one round only
        pending_reduction_a, pending_reduction_b = 0, 0  # [canonical: params/combat.md PP-294 — non-stacking]

        # Build state for AI strategy
        state_a = {  # [canonical: N/A — structural]
            'own_pool': eff_pool_a, 'opp_pool': eff_pool_b,  # [canonical: N/A — state]
            'own_hp_pct': hp_a / build_a['max_hp'],  # [canonical: N/A — state]
            'opp_hp_pct': hp_b / build_b['max_hp'],  # [canonical: N/A — state]
            'own_stam': stam_a, 'rd': rd,  # [canonical: N/A — state]
        }
        state_b = {  # [canonical: N/A — structural]
            'own_pool': eff_pool_b, 'opp_pool': eff_pool_a,  # [canonical: N/A — state]
            'own_hp_pct': hp_b / build_b['max_hp'],  # [canonical: N/A — state]
            'opp_hp_pct': hp_a / build_a['max_hp'],  # [canonical: N/A — state]
            'own_stam': stam_b, 'rd': rd,  # [canonical: N/A — state]
        }

        # Action selection (lower init declares first per PP-232)
        # We'll just gather both; init order matters more for pool allocation
        action_a = fn_a(state_a)  # [canonical: N/A — structural]
        action_b = fn_b(state_b)  # [canonical: N/A — structural]

        # Resolve actions
        # Compute Off/Def allocations per action
        def allocate(action, pool):  # [canonical: N/A — structural]
            if action == 'strike':  # [canonical: params/combat.md L207]
                # 50/50 split if not init holder; init holder can over-commit defensive
                return pool / 2, pool / 2  # [canonical: N/A — sim heuristic, simple split]
            elif action == 'feint':  # [canonical: params/combat.md PP-294]
                # Commit min 3 to Off; rest to Def
                feint_commit = max(FEINT_MIN_COMMIT, int(pool * 0.6))  # [canonical: PP-294 — N>=3]
                return feint_commit, max(POOL_FLOOR, pool - feint_commit)  # [canonical: PP-294 — Def with remainder]
            elif action == 'full_guard':  # [canonical: params/combat.md L185]
                return 0, pool  # [canonical: N/A — full pool to defence]
            elif action == 'take_breath':  # [canonical: params/combat.md L185]
                return 0, pool  # [canonical: N/A — defensive while restoring]
            return pool / 2, pool / 2  # [canonical: N/A — default fallback]

        off_a, def_a = allocate(action_a, eff_pool_a)  # [canonical: see allocate]
        off_b, def_b = allocate(action_b, eff_pool_b)  # [canonical: see allocate]

        # Resolve Strikes/Feints (Strike resolution and Feint resolution similar)
        # Both sides roll Off vs opponent's Def
        # Resolution order matters: higher init declared last in canon, but here
        # we already have both choices — execute simultaneously in this sim layer
        a_off_hits = continuous_roll(off_a) if action_a in ('strike', 'feint') else 0  # [canonical: N/A — structural]
        b_def_hits = continuous_roll(def_b)  # [canonical: N/A — structural]
        a_net = a_off_hits - b_def_hits if action_a in ('strike', 'feint') else 0  # [canonical: params/combat.md §contested]

        b_off_hits = continuous_roll(off_b) if action_b in ('strike', 'feint') else 0  # [canonical: N/A — structural]
        a_def_hits = continuous_roll(def_a)  # [canonical: N/A — structural]
        b_net = b_off_hits - a_def_hits if action_b in ('strike', 'feint') else 0  # [canonical: params/combat.md §contested]

        # Apply Strike damage
        if action_a == 'strike' and a_net > 0:  # [canonical: N/A — hit threshold]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            if a_net >= CRIT_MAGNITUDE:  # [canonical: see CRIT_MAGNITUDE]
                base_mod *= 2  # [canonical: params/combat.md §Damage — crit doubles weapon mod]
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

        # Apply Feint pool reduction (next round) — PP-294
        if action_a == 'feint' and a_net > 0:  # [canonical: PP-294 — Feint applies on margin > 0]
            pending_reduction_b = max(pending_reduction_b, int(a_net))  # [canonical: PP-294 — margin dice, non-stacking via max]

        if action_b == 'feint' and b_net > 0:  # [canonical: PP-294]
            pending_reduction_a = max(pending_reduction_a, int(b_net))  # [canonical: PP-294]

        # Stamina cost
        if action_a == 'take_breath':  # [canonical: params/combat.md L185]
            stam_a = min(build_a['max_stam'], stam_a + 20 - TAKE_BREATH_COST)  # [canonical: Take a Breath restores up to base]
        else:  # [canonical: N/A — structural]
            stam_a -= ACTION_COST  # [canonical: see ACTION_COST]

        if action_b == 'take_breath':  # [canonical: params/combat.md L185]
            stam_b = min(build_b['max_stam'], stam_b + 20 - TAKE_BREATH_COST)  # [canonical: Take a Breath restores]
        else:  # [canonical: N/A — structural]
            stam_b -= ACTION_COST  # [canonical: see ACTION_COST]

        # Felled checks
        a_felled = hp_a <= 0 or wounds_a > build_a['mw']  # [canonical: params/combat.md §Wounds — felled at MW+1]
        b_felled = hp_b <= 0 or wounds_b > build_b['mw']  # [canonical: params/combat.md §Wounds]
        if a_felled and b_felled:  # [canonical: N/A — structural]
            return 'draw'  # [canonical: N/A — structural]
        if a_felled:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if b_felled:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

    return 'draw'  # [canonical: N/A — structural max-rounds]


def build(name, agi, end, strength, hist=2, attn=None):  # [canonical: N/A — sim baseline]
    return {
        'name': name,  # [canonical: N/A — structural]
        'agi': agi,  # [canonical: params/core.md §Attributes]
        'end': end,  # [canonical: params/core.md §Attributes]
        'str': strength,  # [canonical: params/core.md §Attributes]
        'hist': hist,  # [canonical: N/A — sim]
        'attn': attn if attn is not None else agi,  # [canonical: params/combat.md L116 — Attunement; sim proxy = Agi when unspecified]
        'base_pool': combat_pool(agi, hist),  # [canonical: see combat_pool]
        'wi': wound_interval(end),  # [canonical: see wound_interval]
        'mw': max_wounds(end),  # [canonical: see max_wounds]
        'max_hp': max_health(end),  # [canonical: see max_health]
        'max_stam': max_stamina(end),  # [canonical: see max_stamina]
    }


def run_matchup(a, b, strat_a='strike_only', strat_b='strike_only', n=3000):  # [canonical: N/A — sim N]
    wins_a, wins_b, draws = 0, 0, 0  # [canonical: N/A — structural]
    for _ in range(n):  # [canonical: N/A — structural]
        r = simulate_duel(a, b, strat_a, strat_b)  # [canonical: N/A — structural]
        if r == 'a':  # [canonical: N/A — structural]
            wins_a += 1  # [canonical: N/A — structural]
        elif r == 'b':  # [canonical: N/A — structural]
            wins_b += 1  # [canonical: N/A — structural]
        else:  # [canonical: N/A — structural]
            draws += 1  # [canonical: N/A — structural]
    return wins_a / n, wins_b / n, draws / n  # [canonical: N/A — structural]


def main():
    random.seed(42)  # [canonical: N/A — reproducibility]
    threshold = 0.65  # [canonical: tests/audit/all_directions_ners_v27.md — 65% dominance threshold]

    print("=" * 84)  # [canonical: N/A — formatting]
    print("Phase 7 sim — Action triangle (Strike/Feint/Full Guard) impact on dominance")  # [canonical: N/A — header]
    print("=" * 84)  # [canonical: N/A — formatting]
    print(f"  Engine: continuous Normal(0.4*pool, 0.8*sqrt(pool))")  # [canonical: see DIE constants]
    print(f"  Pool: (Agi*2)+H+3 current canon  Crit: mag>=4  N=3000/matchup")  # [canonical: N/A — config]
    print(f"  Modes: strike_only (Phase 6 baseline), smart (both AI), underdog_feint (B uses Feint)")  # [canonical: N/A — modes]
    print()  # [canonical: N/A — formatting]

    fast = build('Fast (Agi 6, End 4)', 6, 4, 4)  # [canonical: N/A — build matrix]
    strong = build('Strong (Agi 3, End 4)', 3, 4, 4)  # [canonical: N/A — build matrix]
    tough = build('Tough (Agi 3, End 6)', 3, 6, 4)  # [canonical: N/A — build matrix]

    print("Build stats:")  # [canonical: N/A — header]
    for b in (fast, strong, tough):  # [canonical: N/A — structural]
        print(f"  {b['name']:32} pool={b['base_pool']:2}D HP={b['max_hp']:2} stam={b['max_stam']:2} MW={b['mw']}")
    print()  # [canonical: N/A — formatting]

    # AGI DOMINANCE TESTS — Fast vs Strong, three strategy modes
    print("AGI dominance: Fast (Agi 6) vs Strong (Agi 3), three strategy modes")  # [canonical: N/A — header]
    print(f"  {'Mode':30} {'A=Fast strat':>16} {'B=Strong strat':>18} {'Fast cond':>10}")  # [canonical: N/A — header]
    print(f"  {'-' * 30} {'-' * 16} {'-' * 18} {'-' * 10}")  # [canonical: N/A — formatting]

    mode_configs = [  # [canonical: N/A — structural]
        ('Strike-only (Phase 6 baseline)', 'strike_only', 'strike_only'),  # [canonical: N/A — sim]
        ('Smart both sides', 'smart', 'smart'),  # [canonical: N/A — sim]
        ('Underdog uses Feint (B)', 'strike_only', 'underdog_feint'),  # [canonical: N/A — sim]
        ('Both underdog_feint', 'underdog_feint', 'underdog_feint'),  # [canonical: N/A — sim]
    ]

    agi_results = {}  # [canonical: N/A — structural]
    for label, sa, sb in mode_configs:  # [canonical: N/A — structural]
        wa, wb, dr = run_matchup(fast, strong, sa, sb)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        agi_results[label] = cond  # [canonical: N/A — structural]
        flag = " DOMINANT" if cond >= threshold else " moderate"  # [canonical: see threshold]
        if cond < 0.55:  # [canonical: N/A — balanced threshold]
            flag = " BALANCED"  # [canonical: N/A — output]
        print(f"  {label:30} {sa:>16} {sb:>18} {cond:>9.1%}{flag}")
    print()  # [canonical: N/A — formatting]

    # END DOMINANCE — Tough vs Strong
    print("END dominance: Tough (Agi 3, End 6) vs Strong (Agi 3, End 4), three strategy modes")  # [canonical: N/A — header]
    print(f"  {'Mode':30} {'Tough cond':>11}")  # [canonical: N/A — header]
    print(f"  {'-' * 30} {'-' * 11}")  # [canonical: N/A — formatting]

    end_results = {}  # [canonical: N/A — structural]
    for label, sa, sb in mode_configs:  # [canonical: N/A — structural]
        wa, wb, dr = run_matchup(tough, strong, sa, sb)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        end_results[label] = cond  # [canonical: N/A — structural]
        flag = " DOMINANT" if cond >= threshold else " moderate"  # [canonical: see threshold]
        if cond < 0.55:  # [canonical: N/A — balanced]
            flag = " BALANCED"  # [canonical: N/A — output]
        print(f"  {label:30} {cond:>10.1%}{flag}")
    print()  # [canonical: N/A — formatting]

    # Summary table
    print("=" * 84)  # [canonical: N/A — formatting]
    print("SUMMARY — Conditional win for dominant side")  # [canonical: N/A — header]
    print("=" * 84)  # [canonical: N/A — formatting]
    print(f"  {'Mode':30} {'Fast vs Strong':>16} {'Tough vs Strong':>18}")  # [canonical: N/A — header]
    print(f"  {'-' * 30} {'-' * 16} {'-' * 18}")  # [canonical: N/A — formatting]
    for label, _, _ in mode_configs:  # [canonical: N/A — structural]
        a_cond = agi_results.get(label, 0.5)  # [canonical: N/A — structural]
        e_cond = end_results.get(label, 0.5)  # [canonical: N/A — structural]
        print(f"  {label:30} {a_cond:>15.1%} {e_cond:>17.1%}")
    print()  # [canonical: N/A — formatting]

    # Verdict
    print("Verdict:")  # [canonical: N/A — output]
    baseline = agi_results['Strike-only (Phase 6 baseline)']  # [canonical: N/A — comparison]
    smart = agi_results['Smart both sides']  # [canonical: N/A — comparison]
    underdog = agi_results['Underdog uses Feint (B)']  # [canonical: N/A — comparison]

    improvement_smart = (baseline - smart) * 100  # [canonical: N/A — display]
    improvement_underdog = (baseline - underdog) * 100  # [canonical: N/A — display]
    print(f"  Baseline (Strike-only): Fast {baseline:.1%}")  # [canonical: N/A — output]
    print(f"  With Smart play: Fast {smart:.1%} (Δ {improvement_smart:+.1f}pp toward balance)")  # [canonical: N/A — output]
    print(f"  With Underdog Feint: Fast {underdog:.1%} (Δ {improvement_underdog:+.1f}pp toward balance)")  # [canonical: N/A — output]
    print()  # [canonical: N/A — output]
    if smart < threshold:  # [canonical: see threshold]
        print(f"  → Action triangle (Smart) brings Agi dominance below {threshold:.0%} threshold.")  # [canonical: N/A — output]
        print(f"    Skilled tactical play closes the gap. Current canon is balanced under real play.")  # [canonical: N/A — output]
    elif underdog < threshold:  # [canonical: see threshold]
        print(f"  → Action triangle alone insufficient; underdog must actively Feint to close gap.")  # [canonical: N/A — output]
    else:  # [canonical: N/A — structural]
        print(f"  → Action triangle does NOT solve dominance even with active Feint play.")  # [canonical: N/A — output]
        print(f"    Next lever: wound-spiral cap (Lever B) or HP/stamina compression (Lever D).")  # [canonical: N/A — output]
    print("=" * 84)  # [canonical: N/A — formatting]


if __name__ == '__main__':
    main()
