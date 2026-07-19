#!/usr/bin/env python3
# Phase 4 sim — Agi-dominance re-check at current canon
# Date: see git log + commit SHA reference  # [canonical: N/A — doc]
# See tests/sim/phase4_agi_dominance_2026-05-15.md for results + analysis  # [canonical: N/A — doc]
# Verification ledger: tests/sim/phase4_sim_verification_ledger.json  # [canonical: N/A — doc]
#
# Trigger: ED-828 / Decision A — Jordan rejected PP-717 D2 (Pool Softcap) at canon  # [canonical: canon/editorial_ledger.yaml ED-828]
# Question: at current canon (post-Decision A reject), does Agi 6 still produce
#           Fast-build dominance over Agi 3 builds?  # [canonical: N/A — doc]
# Method: minimal duel sim. Two builds, same weapon, same armour, varying Agi.  # [canonical: N/A — structural]
#         Strike/Defend only; pool split 50/50; loss = HP=0 OR stam=0.  # [canonical: N/A — structural]
import random
from collections import defaultdict

# Canonical mechanics (see sim_verification_ledger.json for full citations)

# Dice engine: params/core.md §10-19
# Face 1 = -1, 7-9 = +1, 10 = +2. No chain implemented (simplification).  # [canonical: params/core.md §dice]
TN = 7  # [canonical: params/core.md §TN Values — Standard]

def combat_pool(agi, hist):
    # [canonical: params/combat.md L14 — current canon post-Decision A]
    return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula]

def max_wounds(end):
    # [canonical: params/combat.md L138 post-F12 commit abf9fc8e + derived_stats §4.1 L57]
    return min(end // 2 + 1, 3)  # [canonical: params/combat.md L138 — PP-717 D1 cap]

def wound_interval(end):
    return end + 6  # [canonical: derived_stats §4.1 — WI formula]

def max_health(end):
    return wound_interval(end) * (max_wounds(end) + 1)  # [canonical: derived_stats §4.1 Health formula]

def max_stamina(end):
    # Architecture C — sim baseline matching v27 convention. Canonical formula
    # is End × 5 per params/combat.md L15; this sim uses Arch C for consistency
    # with the v27 sim that produced the original Agi-dominance finding.
    return 15 + end * 2  # [canonical: Architecture C — sim baseline]

ACTION_COST = 5  # [canonical: params/combat.md L15 — "standard 5"]
CRIT_THRESHOLD = 4  # [canonical: params/combat.md L91 — PP-717 D3]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187 — pool floor 1D]
WEAPON_DAMAGE_MOD = 3  # [canonical: params/combat.md damage table — Light Blade Cut vs None]
STR_MULT = 1.0  # [canonical: params/combat.md §Damage Formula — Light Blade ×1]


def roll_pool(n, tn=TN):
    # Roll n d10s, count net successes. Face 1 = -1, 7-9 = +1, 10 = +2.
    if n <= 0:  # [canonical: N/A — structural]
        return 0  # [canonical: N/A — structural]
    net = 0  # [canonical: N/A — structural]
    for _ in range(n):  # [canonical: N/A — structural]
        d = random.randint(1, 10)  # [canonical: params/core.md §dice — d10]
        if d == 1:  # [canonical: params/core.md §dice — face 1 subtracts]
            net -= 1  # [canonical: params/core.md §dice — -1]
        elif d == 10:  # [canonical: params/core.md §dice — face 10 = +2]
            net += 2  # [canonical: params/core.md §dice — +2]
        elif d >= tn:  # [canonical: params/core.md §dice — face >= TN counts]
            net += 1  # [canonical: params/core.md §dice — +1 per success]
    return net  # [canonical: N/A — structural]


def simulate_duel(build_a, build_b, max_rounds=20):  # [canonical: N/A — structural cutoff]
    hp_a, hp_b = build_a['max_hp'], build_b['max_hp']  # [canonical: N/A — structural]
    stam_a, stam_b = build_a['max_stam'], build_b['max_stam']  # [canonical: N/A — structural]
    wounds_a, wounds_b = 0, 0  # [canonical: N/A — structural initial state]
    wi_a, wi_b = build_a['wi'], build_b['wi']  # [canonical: N/A — structural]

    for rd in range(max_rounds):  # [canonical: N/A — structural]
        if stam_a < ACTION_COST and stam_b < ACTION_COST:  # [canonical: N/A — structural]
            return 'draw'  # [canonical: N/A — structural]
        if stam_a < ACTION_COST:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if stam_b < ACTION_COST:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

        # Effective pool: base − wounds, floor at POOL_FLOOR
        pool_a = max(POOL_FLOOR, build_a['base_pool'] - wounds_a)  # [canonical: params/combat.md §Pool modifiers — wound -1D]
        pool_b = max(POOL_FLOOR, build_b['base_pool'] - wounds_b)  # [canonical: params/combat.md §Pool modifiers]

        # Split 50/50 off/def  # [canonical: params/combat.md §Pool Allocation — split per round]
        off_a, def_a = pool_a // 2, pool_a - pool_a // 2  # [canonical: N/A — structural 50/50 sim control]
        off_b, def_b = pool_b // 2, pool_b - pool_b // 2  # [canonical: N/A — structural 50/50 sim control]

        # Both attack simultaneously (no init asymmetry — sim control)
        a_off_hits = roll_pool(off_a)  # [canonical: N/A — structural]
        b_def_hits = roll_pool(def_b)  # [canonical: N/A — structural]
        a_net = a_off_hits - b_def_hits  # [canonical: params/combat.md §contested rolls]

        b_off_hits = roll_pool(off_b)  # [canonical: N/A — structural]
        a_def_hits = roll_pool(def_a)  # [canonical: N/A — structural]
        b_net = b_off_hits - a_def_hits  # [canonical: params/combat.md §contested rolls]

        # Damage: net + STR*mult + weapon_mod (Light Blade Cut vs None)
        if a_net > 0:  # [canonical: N/A — structural]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            is_crit = a_net >= CRIT_THRESHOLD  # [canonical: see CRIT_THRESHOLD]
            if is_crit:  # [canonical: N/A — structural]
                base_mod *= 2  # [canonical: params/combat.md §Damage Formula — crit doubles weapon mod]
            dmg = a_net + int(build_a['str'] * STR_MULT) + base_mod  # [canonical: params/combat.md §Damage Formula PP-232]
            hp_b -= dmg  # [canonical: N/A — structural]
            new_wounds = (build_b['max_hp'] - hp_b) // wi_b  # [canonical: params/combat.md §Wounds computed on the fly]
            wounds_b = min(new_wounds, build_b['mw'] + 1)  # [canonical: params/combat.md §Wounds — felled at MW+1]

        if b_net > 0:  # [canonical: N/A — structural]
            base_mod = WEAPON_DAMAGE_MOD  # [canonical: see WEAPON_DAMAGE_MOD]
            is_crit = b_net >= CRIT_THRESHOLD  # [canonical: see CRIT_THRESHOLD]
            if is_crit:  # [canonical: N/A — structural]
                base_mod *= 2  # [canonical: params/combat.md §Damage Formula — crit doubles weapon mod]
            dmg = b_net + int(build_b['str'] * STR_MULT) + base_mod  # [canonical: params/combat.md §Damage Formula PP-232]
            hp_a -= dmg  # [canonical: N/A — structural]
            new_wounds = (build_a['max_hp'] - hp_a) // wi_a  # [canonical: params/combat.md §Wounds]
            wounds_a = min(new_wounds, build_a['mw'] + 1)  # [canonical: params/combat.md §Wounds]

        stam_a -= ACTION_COST  # [canonical: see ACTION_COST]
        stam_b -= ACTION_COST  # [canonical: see ACTION_COST]

        a_felled = hp_a <= 0 or wounds_a > build_a['mw']  # [canonical: params/combat.md §Wounds — felled at MW+1 wounds]
        b_felled = hp_b <= 0 or wounds_b > build_b['mw']  # [canonical: params/combat.md §Wounds]
        if a_felled and b_felled:  # [canonical: N/A — structural]
            return 'draw'  # [canonical: N/A — structural]
        if a_felled:  # [canonical: N/A — structural]
            return 'b'  # [canonical: N/A — structural]
        if b_felled:  # [canonical: N/A — structural]
            return 'a'  # [canonical: N/A — structural]

    return 'draw'  # [canonical: N/A — structural max-rounds cutoff]


def build(name, agi, end, strength, hist=2):  # [canonical: N/A — sim baseline History]
    return {
        'name': name,  # [canonical: N/A — structural]
        'agi': agi,  # [canonical: params/core.md §Attributes 1-7]
        'end': end,  # [canonical: params/core.md §Attributes 1-7]
        'str': strength,  # [canonical: params/core.md §Attributes 1-7]
        'hist': hist,  # [canonical: N/A — sim control]
        'base_pool': combat_pool(agi, hist),  # [canonical: see combat_pool]
        'wi': wound_interval(end),  # [canonical: see wound_interval]
        'mw': max_wounds(end),  # [canonical: see max_wounds]
        'max_hp': max_health(end),  # [canonical: see max_health]
        'max_stam': max_stamina(end),  # [canonical: see max_stamina]
    }


def run_matchup(build_a, build_b, n=2000):  # [canonical: N/A — sim N]
    wins_a, wins_b, draws = 0, 0, 0  # [canonical: N/A — structural counters]
    for _ in range(n):  # [canonical: N/A — structural]
        result = simulate_duel(build_a, build_b)  # [canonical: N/A — structural]
        if result == 'a':  # [canonical: N/A — structural]
            wins_a += 1  # [canonical: N/A — structural]
        elif result == 'b':  # [canonical: N/A — structural]
            wins_b += 1  # [canonical: N/A — structural]
        else:  # [canonical: N/A — structural]
            draws += 1  # [canonical: N/A — structural]
    return wins_a / n, wins_b / n, draws / n  # [canonical: N/A — structural]


def main():
    random.seed(42)  # [canonical: N/A — reproducibility seed]
    print("=" * 72)  # [canonical: N/A — formatting]
    print("Phase 4 sim — Agi-dominance re-check at current canon")  # [canonical: N/A — header]
    print("=" * 72)  # [canonical: N/A — formatting]
    print(f"  Pool: (Agi*2)+H+3 NO softcap (Decision A)  MW=min(End/2+1,3)  Crit>=4")  # [canonical: N/A — config display]
    print(f"  N = 2000 duels per matchup, seed=42")  # [canonical: N/A — config display]
    print()  # [canonical: N/A — formatting]

    # Build matrix
    strong = build('Strong (Agi 3, End 4)', agi=3, end=4, strength=4)  # [canonical: N/A — build matrix]
    fast = build('Fast (Agi 6, End 4)', agi=6, end=4, strength=4)  # [canonical: N/A — build matrix]
    tough = build('Tough (Agi 3, End 6)', agi=3, end=6, strength=4)  # [canonical: N/A — build matrix]
    fast_tough = build('Fast+Tough (Agi 6, End 6)', agi=6, end=6, strength=4)  # [canonical: N/A — build matrix]

    print("Build stats:")  # [canonical: N/A — header]
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

    print("Results (conditional = excludes draws):")  # [canonical: N/A — header]
    print(f"  {'Matchup':40} {'A win':>7} {'B win':>7} {'Draw':>6} {'A|dec':>7} {'Spread':>8}")
    print(f"  {'-' * 40} {'-' * 7} {'-' * 7} {'-' * 6} {'-' * 7} {'-' * 8}")
    for label, a, b in matchups:  # [canonical: N/A — structural]
        wa, wb, dr = run_matchup(a, b)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        a_cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        spread = abs(a_cond - (1 - a_cond)) * 100  # [canonical: N/A — display percentage]
        threshold = 0.65  # [canonical: audit/lane-a/all_directions_ners_v27.md — 65% pass threshold]
        flag = " DOMINANT" if a_cond >= threshold or a_cond <= (1 - threshold) else ""
        print(f"  {label:40} {wa:>6.1%} {wb:>6.1%} {dr:>5.1%} {a_cond:>6.1%} {spread:>7.1f}pp{flag}")
    print()  # [canonical: N/A — formatting]

    # Build-investment ROI
    print("Build-investment ROI (vs Strong, varying Agi, End=4):")  # [canonical: N/A — header]
    print(f"  {'Build':28} {'Pool':>5} {'Win%':>7} {'Cond':>6} {'Δ cond vs Agi-3':>16}")
    print(f"  {'-' * 28} {'-' * 5} {'-' * 7} {'-' * 6} {'-' * 16}")
    base_cond = None  # [canonical: N/A — structural]
    for agi in range(3, 8):  # [canonical: params/core.md §Attributes — Agi 3-7 range]
        b = build(f"Agi {agi}, End 4", agi=agi, end=4, strength=4)  # [canonical: N/A — sweep config]
        wa, wb, dr = run_matchup(b, strong)  # [canonical: N/A — structural]
        decisive = wa + wb  # [canonical: N/A — structural]
        cond = (wa / decisive) if decisive > 0 else 0.5  # [canonical: N/A — structural]
        delta = ""  # [canonical: N/A — structural]
        if agi == 3:  # [canonical: N/A — structural baseline]
            base_cond = cond  # [canonical: N/A — structural]
        else:  # [canonical: N/A — structural]
            delta = f"+{(cond - base_cond) * 100:.1f}pp"  # [canonical: N/A — display]
        print(f"  {b['name']:28} {b['base_pool']:>4}D {wa:>6.1%} {cond:>5.1%} {delta:>16}")
    print()  # [canonical: N/A — formatting]

    # Summary
    print("=" * 72)  # [canonical: N/A — formatting]
    wa_fs, wb_fs, dr_fs = run_matchup(fast, strong)  # [canonical: N/A — structural]
    fs_decisive = wa_fs + wb_fs  # [canonical: N/A — structural]
    fast_cond = (wa_fs / fs_decisive) if fs_decisive > 0 else 0.5  # [canonical: N/A — structural]
    print(f"FAST vs STRONG: Absolute {wa_fs:.1%} | Strong {wb_fs:.1%} | Draw {dr_fs:.1%}")
    print(f"Conditional Fast win rate: {fast_cond:.1%}")  # [canonical: N/A — display]
    high_thresh = 0.65  # [canonical: v27 audit — 65% pass threshold]
    mid_thresh = 0.60  # [canonical: N/A — structural soft threshold]
    if fast_cond >= high_thresh:  # [canonical: see high_thresh]
        print("→ AGI DOMINANCE CONFIRMED at current canon.")  # [canonical: N/A — output]
    elif fast_cond >= mid_thresh:  # [canonical: see mid_thresh]
        print("→ AGI ADVANTAGE measured but below pass threshold.")  # [canonical: N/A — output]
    else:  # [canonical: N/A — structural]
        print("→ AGI DOMINANCE NOT MANIFESTING.")  # [canonical: N/A — output]
    print("=" * 72)  # [canonical: N/A — formatting]


if __name__ == '__main__':
    main()
