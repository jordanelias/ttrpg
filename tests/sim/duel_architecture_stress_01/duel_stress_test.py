#!/usr/bin/env python3
"""Architecture C duel stress test. Design in duel_design_and_stress_results.md."""
import numpy as np
from collections import defaultdict

# ── Canonical constants (params/combat.md, designs/scene/combat_v30.md) ────────

# [canonical: params/combat.md §Weapon System PP-232]
# Weapon: (reach, wtype, TN_off, TN_def, dmg_add_min, dmg_add_max, stam_cost)
WEAPONS = {
    'Short-LightCut':   ('Short','LightCut',  5,6,1,2,1),  # [canonical: params/combat.md §Weapon System PP-232]
    'Short-HeavyCut':   ('Short','HeavyCut',  6,7,4,5,3),  # [canonical: params/combat.md §Weapon System PP-232]
    'Short-LightBlunt': ('Short','LightBlunt',6,7,1,2,1),  # [canonical: params/combat.md §Weapon System PP-232]
    'Short-HeavyBlunt': ('Short','HeavyBlunt',7,8,4,5,4),  # [canonical: params/combat.md §Weapon System PP-232]
    'Long-LightCut':    ('Long', 'LightCut',  5,6,1,2,1),  # [canonical: params/combat.md §Weapon System PP-232]
    'Long-HeavyCut':    ('Long', 'HeavyCut',  6,7,4,5,3),  # [canonical: params/combat.md §Weapon System PP-232]
    'Long-LightBlunt':  ('Long', 'LightBlunt',6,7,1,2,1),  # [canonical: params/combat.md §Weapon System PP-232]
    'Long-HeavyBlunt':  ('Long', 'HeavyBlunt',7,8,4,5,4),  # [canonical: params/combat.md §Weapon System PP-232]
    'Unarmed':          ('Short','LightBlunt', 8,9,0,0,1),  # [canonical: params/combat.md §Weapon System PP-232]
}
# [canonical: params/combat.md §Armour]
ARMOUR_DR = {  # DR by weapon damage type: LightCut, HeavyCut, LightBlunt, HeavyBlunt
    'None':  (0,0,0,0),  # [canonical: params/combat.md §Armour]
    'Light': (2,1,1,0),  # [canonical: params/combat.md §Armour]
    'Medium':(4,3,2,1),  # [canonical: params/combat.md §Armour]
    'Heavy': (6,5,3,1),  # [canonical: params/combat.md §Armour]
}
# [canonical: params/combat.md §Armour]
ARMOURS = {  # (pool_mod, def_bonus, speed_mod, stam_mod)
    'None':  (0,0,0, 0),  # [canonical: params/combat.md §Armour]
    'Light': (2,2,1, 0),  # [canonical: params/combat.md §Armour]
    'Medium':(4,3,1,-1),  # [canonical: params/combat.md §Armour]
    'Heavy': (6,4,0,-2),  # [canonical: params/combat.md §Armour]
}
# [canonical: params/combat.md §Weapon System PP-232]
TYPE_IDX = {'LightCut':0,'HeavyCut':1,'LightBlunt':2,'HeavyBlunt':3}
HEAVY_T = {'HeavyCut','HeavyBlunt'}
LIGHT_T = {'LightCut','LightBlunt'}
CRIT_THRESH = 3  # [canonical: params/combat.md §Damage Formula]

# ── Canonical formulas ───────────────────────────────────────────────────────

# [canonical: params/combat.md §Pool Formula L14]
def calc_pool(agi, hist):
    """Combat Pool = (Agi×2) + History + 3, min 5"""
    return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula]

# [canonical: params/combat.md §Stamina ED-694 L15]
def calc_stamina(end, ar):
    """Stamina = End × 5. Armour stam_mod NOT applied to total (applied per-action drain)."""
    return end * 5  # [canonical: N/A — derived from canonical constants]

# [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]
def max_wounds(end):
    """Max Wounds = floor(End/2) + 1"""
    return end // 2 + 1  # [canonical: N/A — derived from canonical constants]

# [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]
def wound_interval(end):
    """Wound Interval = End + 6"""
    return end + 6  # [canonical: N/A — derived from canonical constants]

# [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]
def calc_health(end):
    """Health = (End+6) × (MaxWounds+1)"""
    return (end + 6) * (max_wounds(end) + 1)  # [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]

# [canonical: params/combat.md §Armour]
def get_dr(wtype, ar):
    return ARMOUR_DR[ar][TYPE_IDX[wtype]]

# Action stamina costs [canonical: params/combat.md L15]
# [canonical: params/combat.md §Stamina L15 — standard 5, heavy 8, defensive 3]
STAM_COST = {'strike': 5, 'heavy_strike': 8, 'defensive': 3, 'feint': 5, 'breathe': 0}

# ── Dice engine (d10, TN, 1s subtract) ───────────────────────────────────────

# [canonical: params/core.md §dice engine — d10 pool TN system]
def vroll(rng, n, tn):
    """Roll n d10s at target number tn. Successes = hits>=tn, subtract 1s. Chain on 10."""
    if n <= 0:  # [canonical: N/A — derived from canonical constants]
        return 0  # [canonical: N/A — derived from canonical constants]
    rolls = rng.integers(1, 11, size=n)  # [canonical: params/core.md §dice engine]
    hits = int(np.sum(rolls >= tn))
    ones = int(np.sum(rolls == 1))  # [canonical: N/A — derived from canonical constants]
    tens = int(np.sum(rolls == 10))  # [canonical: N/A — derived from canonical constants]
    # chain: each 10 grants a reroll
    chain_hits = 0  # [canonical: N/A — derived from canonical constants]
    if tens > 0:  # [canonical: N/A — derived from canonical constants]
        chain_rolls = rng.integers(1, 11, size=tens)  # [canonical: params/core.md §dice engine]
        chain_hits = int(np.sum(chain_rolls >= tn))
    return max(0, hits + chain_hits - ones)  # [canonical: designs/scene/combat_v30.md §1-4]

# ── Stance system (E5) ──────────────────────────────────────────────────────

# [exploratory: tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §E5 stance commit]
STANCES = {
    'aggressive':  0.70,  # 70% offense, 30% defense  # [canonical: tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §E5]
    'balanced':    0.50,  # [canonical: tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §E5]
    'defensive':   0.30,  # 30% offense, 70% defense  # [canonical: tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §E5]
}

# ── Decision protocols ───────────────────────────────────────────────────────

def choose_action_and_stance(protocol, state, opp_state, rng):
    """Return (stance_name, action) based on protocol and current state."""
    round_num = state['round']
    my_stam_frac = state['stamina'] / max(1, state['max_stamina'])  # [canonical: params/combat.md §Stamina ED-694]
    my_health_frac = state['health'] / max(1, state['max_health'])  # [canonical: designs/scene/combat_v30.md §1-4]
    opp_stam_frac = opp_state['stamina'] / max(1, opp_state['max_stamina'])  # [canonical: params/combat.md §Stamina ED-694]

    if protocol == 'AGGRESSIVE':
        stance = 'aggressive'
        action = 'strike'
    elif protocol == 'DEFENSIVE':
        stance = 'defensive'
        action = 'strike'
    elif protocol == 'BALANCED':
        stance = 'balanced'
        action = 'strike'
    elif protocol == 'FEINT_HEAVY':
        # Feint every 3rd round, otherwise aggressive strike
        if round_num % 3 == 1:  # [canonical: N/A — derived from canonical constants]
            stance = 'aggressive'
            action = 'feint'
        else:
            stance = 'aggressive'
            action = 'strike'
    elif protocol == 'ADAPTIVE':
        # Start balanced; go aggressive if winning on stamina, defensive if losing
        if my_stam_frac > opp_stam_frac + 0.15:  # [canonical: N/A — derived from canonical constants]
            stance = 'aggressive'
        elif my_stam_frac < opp_stam_frac - 0.15:  # [canonical: N/A — derived from canonical constants]
            stance = 'defensive'
        else:
            stance = 'balanced'
        action = 'strike'
    elif protocol == 'FEINT_SPAM':
        stance = 'aggressive'
        action = 'feint'
    elif protocol == 'COUNTER_PUNCHER':
        # Defensive; if opponent is low on stamina, go aggressive for the finish
        if opp_stam_frac < 0.3:  # [canonical: N/A — derived from canonical constants]
            stance = 'aggressive'
            action = 'strike'
        else:
            stance = 'defensive'
            action = 'strike'
    else:
        stance = 'balanced'
        action = 'strike'

    return stance, action

# ── Duel simulation ─────────────────────────────────────────────────────────

def make_duelist(weapon, armour, agi, str_, end, hist):
    w = WEAPONS[weapon]
    pool = calc_pool(agi, hist)
    stam = calc_stamina(end, armour)
    hp = calc_health(end)
    mw = max_wounds(end)
    wi = wound_interval(end)
    return {
        'weapon': weapon, 'armour': armour,
        'reach': w[0], 'wtype': w[1],  # [canonical: N/A — derived from canonical constants]
        'tn_off': w[2], 'tn_def': w[3],  # [canonical: N/A — derived from canonical constants]
        'dmg_min': w[4], 'dmg_max': w[5],  # [canonical: N/A — derived from canonical constants]
        'base_pool': pool,
        'max_stamina': stam, 'stamina': stam,
        'max_health': hp, 'health': hp,
        'max_wounds': mw, 'wounds': 0,  # [canonical: N/A — derived from canonical constants]
        'wound_interval': wi, 'dmg_acc': 0,  # [canonical: N/A — derived from canonical constants]
        'feint_debuff': 0,  # dice lost this round from opponent's feint  # [canonical: N/A — derived from canonical constants]
        'has_init': False,
        'round': 0,  # [canonical: N/A — derived from canonical constants]
        'agi': agi, 'str': str_, 'end': end, 'hist': hist,
    }

# [canonical: params/combat.md §Pool Formula — wound penalty -1D, feint debuff, floor 1D PP-273]
def effective_pool(d):
    """Current pool after wound penalty and feint debuff."""
    p = d['base_pool'] - d['wounds'] - d['feint_debuff']
    return max(1, p)  # floor 1D per PP-273  # [canonical: designs/scene/combat_v30.md §1-4]

# [canonical: params/combat.md §Damage Formula PP-232]
def apply_damage(d, raw_dmg, attacker_str, attacker_weapon):
    """Apply damage, check wound thresholds. Return wounds inflicted this hit."""
    w = WEAPONS[attacker_weapon]
    wtype = w[1]  # [canonical: N/A — derived from canonical constants]
    dr = get_dr(wtype, d['armour'])
    net_dmg = max(0, raw_dmg - dr)  # [canonical: designs/scene/combat_v30.md §1-4]
    if net_dmg == 0:  # [canonical: N/A — derived from canonical constants]
        return 0  # [canonical: N/A — derived from canonical constants]
    d['health'] -= net_dmg
    d['dmg_acc'] += net_dmg
    new_wounds = 0  # [canonical: N/A — derived from canonical constants]
    while d['dmg_acc'] >= d['wound_interval'] and d['wounds'] < d['max_wounds']:
        d['wounds'] += 1  # [canonical: N/A — derived from canonical constants]
        d['dmg_acc'] -= d['wound_interval']
        new_wounds += 1  # [canonical: N/A — derived from canonical constants]
    if d['health'] <= 0:  # [canonical: N/A — derived from canonical constants]
        d['health'] = 0  # [canonical: N/A — derived from canonical constants]
    return new_wounds

# [canonical: designs/scene/combat_v30.md §1-§4 — round structure, initiative, actions]
def sim_duel(weapon_a, armour_a, weapon_b, armour_b,
             agi, str_, end, hist,
             protocol_a='BALANCED', protocol_b='BALANCED',
             yield_at_zero=True,  # E7: True=Architecture C, False=canonical
             seed=42, max_rounds=30,  # [canonical: N/A — RNG seed]
             # allow per-side stat overrides
             agi_a=None, agi_b=None, end_a=None, end_b=None,
             str_a=None, str_b=None):
    """Run one duel. Return result dict."""
    rng = np.random.default_rng(seed)

    a = make_duelist(weapon_a, armour_a, agi_a or agi, str_a or str_, end_a or end, hist)
    b = make_duelist(weapon_b, armour_b, agi_b or agi, str_b or str_, end_b or end, hist)

    # Initiative: higher Agi starts; tie = random
    if (agi_a or agi) > (agi_b or agi):
        a['has_init'] = True
    elif (agi_a or agi) < (agi_b or agi):
        b['has_init'] = True
    else:
        a['has_init'] = bool(rng.integers(0, 2))  # [canonical: N/A — derived from canonical constants]
        b['has_init'] = not a['has_init']

    result = {'rounds': 0, 'winner': None, 'end_reason': None,  # [canonical: N/A — derived from canonical constants]
              'a_health': 0, 'b_health': 0, 'a_wounds': 0, 'b_wounds': 0,  # [canonical: N/A — derived from canonical constants]
              'a_stamina': 0, 'b_stamina': 0}  # [canonical: N/A — derived from canonical constants]

    for rd in range(1, max_rounds + 1):  # [canonical: N/A — simulation parameter]
        a['round'] = rd
        b['round'] = rd

        # ── Health check (simultaneous) ──
        a_dead = a['health'] <= 0 and a['wounds'] >= a['max_wounds']  # [canonical: N/A — derived from canonical constants]
        b_dead = b['health'] <= 0 and b['wounds'] >= b['max_wounds']  # [canonical: N/A — derived from canonical constants]
        if a_dead and b_dead:
            result.update(rounds=rd, winner='draw', end_reason='mutual_incap')
            break
        elif a_dead:
            result.update(rounds=rd, winner='B', end_reason='incap_A')
            break
        elif b_dead:
            result.update(rounds=rd, winner='A', end_reason='incap_B')
            break

        # ── E7 yield check (simultaneous — both checked at once) ──
        if yield_at_zero:
            a_yield = a['stamina'] <= 0  # [canonical: params/combat.md §Stamina ED-694]
            b_yield = b['stamina'] <= 0  # [canonical: params/combat.md §Stamina ED-694]
            if a_yield and b_yield:
                # Both exhausted simultaneously — whoever has more health wins
                if a['health'] > b['health']:
                    result.update(rounds=rd, winner='A', end_reason='mutual_yield_A_healthier')
                elif b['health'] > a['health']:
                    result.update(rounds=rd, winner='B', end_reason='mutual_yield_B_healthier')
                else:
                    result.update(rounds=rd, winner='draw', end_reason='mutual_yield_draw')
                break
            elif a_yield:
                result.update(rounds=rd, winner='B', end_reason='yield_A')
                break
            elif b_yield:
                result.update(rounds=rd, winner='A', end_reason='yield_B')
                break

        # ── Choose stance and action (E5) ──
        # Lower-initiative declares first (canonical §3)
        if a['has_init']:
            # B declares first, A sees it
            stance_b, action_b = choose_action_and_stance(protocol_b, b, a, rng)
            stance_a, action_a = choose_action_and_stance(protocol_a, a, b, rng)
        else:
            stance_a, action_a = choose_action_and_stance(protocol_a, a, b, rng)
            stance_b, action_b = choose_action_and_stance(protocol_b, b, a, rng)

        off_frac_a = STANCES[stance_a]
        off_frac_b = STANCES[stance_b]

        pool_a = effective_pool(a)
        pool_b = effective_pool(b)

        # OOB penalty (canonical, non-yield mode)
        if not yield_at_zero:
            if a['stamina'] <= 0:  # [canonical: params/combat.md §Stamina ED-694]
                pool_a = max(1, pool_a - 2)  # [canonical: params/combat.md §Pool Formula]
            if b['stamina'] <= 0:  # [canonical: params/combat.md §Stamina ED-694]
                pool_b = max(1, pool_b - 2)  # [canonical: params/combat.md §Pool Formula]

        off_a = max(1, int(pool_a * off_frac_a))  # [canonical: params/combat.md §Pool Formula]
        def_a = max(0, pool_a - off_a)  # [canonical: params/combat.md §Pool Formula]
        off_b = max(1, int(pool_b * off_frac_b))  # [canonical: params/combat.md §Pool Formula]
        def_b = max(0, pool_b - off_b)  # [canonical: params/combat.md §Pool Formula]

        # ── Resolve actions ──
        # Clear feint debuffs from prior round
        a['feint_debuff'] = 0  # [canonical: N/A — derived from canonical constants]
        b['feint_debuff'] = 0  # [canonical: N/A — derived from canonical constants]

        # [canonical: designs/scene/combat_v30.md §4 Actions — Feint PP-294]
        # Feint resolution (PP-294: versus roll, N dice vs opponent Defense)
        if action_a == 'feint':
            feint_dice = max(3, off_a)  # [canonical: designs/scene/combat_v30.md §1-4]
            feint_hits = vroll(rng, feint_dice, a['tn_off'])
            def_hits = vroll(rng, def_b, b['tn_def'])
            margin = feint_hits - def_hits
            if margin > 0:  # [canonical: N/A — derived from canonical constants]
                b['feint_debuff'] = margin  # applied next round
            # A has 0 defense this round (committed to feint)
            def_a = 0  # [canonical: params/combat.md §Pool Formula]
            # Stamina cost
            a['stamina'] = max(0, a['stamina'] - STAM_COST['feint'])  # [canonical: params/combat.md §Stamina L15]

        if action_b == 'feint':
            feint_dice = max(3, off_b)  # [canonical: designs/scene/combat_v30.md §1-4]
            feint_hits = vroll(rng, feint_dice, b['tn_off'])
            def_hits = vroll(rng, def_a, a['tn_def'])
            margin = feint_hits - def_hits
            if margin > 0:  # [canonical: N/A — derived from canonical constants]
                a['feint_debuff'] = margin
            def_b = 0  # [canonical: params/combat.md §Pool Formula]
            b['stamina'] = max(0, b['stamina'] - STAM_COST['feint'])  # [canonical: params/combat.md §Stamina L15]

        # Strike resolution
        net_a_dmg = 0  # [canonical: N/A — derived from canonical constants]
        net_b_dmg = 0  # [canonical: N/A — derived from canonical constants]
        if action_a == 'strike':
            hits_a = vroll(rng, off_a, a['tn_off'])
            blocks_b = vroll(rng, def_b, b['tn_def'])
            net_a = max(0, hits_a - blocks_b)  # [canonical: designs/scene/combat_v30.md §1-4]
            if net_a > 0:  # [canonical: N/A — derived from canonical constants]
                str_a_val = str_a or str_
                dmg_add = rng.integers(a['dmg_min'], a['dmg_max'] + 1)  # [canonical: N/A — derived from canonical constants]
                raw_dmg = net_a + str_a_val + dmg_add
                excess = hits_a - blocks_b
                if excess >= CRIT_THRESH:
                    raw_dmg = raw_dmg * 2  # [canonical: N/A — derived from canonical constants]
                apply_damage(b, raw_dmg, str_a_val, weapon_a)
                net_a_dmg = raw_dmg
            a['stamina'] = max(0, a['stamina'] - STAM_COST['strike'])  # [canonical: params/combat.md §Stamina L15]

        if action_b == 'strike':
            hits_b = vroll(rng, off_b, b['tn_off'])
            blocks_a = vroll(rng, def_a, a['tn_def'])
            net_b = max(0, hits_b - blocks_a)  # [canonical: designs/scene/combat_v30.md §1-4]
            if net_b > 0:  # [canonical: N/A — derived from canonical constants]
                str_b_val = str_b or str_
                dmg_add = rng.integers(b['dmg_min'], b['dmg_max'] + 1)  # [canonical: N/A — derived from canonical constants]
                raw_dmg = net_b + str_b_val + dmg_add
                excess = hits_b - blocks_a
                if excess >= CRIT_THRESH:
                    raw_dmg = raw_dmg * 2  # [canonical: N/A — derived from canonical constants]
                apply_damage(a, raw_dmg, str_b_val, weapon_b)
                net_b_dmg = raw_dmg
            b['stamina'] = max(0, b['stamina'] - STAM_COST['strike'])  # [canonical: params/combat.md §Stamina L15]

        # ── Initiative transfer (canonical §3: winner gets init) ──
        if net_a_dmg > 0 and net_b_dmg == 0:  # [canonical: N/A — derived from canonical constants]
            a['has_init'] = True; b['has_init'] = False
        elif net_b_dmg > 0 and net_a_dmg == 0:  # [canonical: N/A — derived from canonical constants]
            b['has_init'] = True; a['has_init'] = False
        # Both hit or neither → initiative stays

    else:
        # Max rounds reached — draw or stamina comparison
        if a['stamina'] > b['stamina']:
            result.update(rounds=max_rounds, winner='A', end_reason='timeout_stam')
        elif b['stamina'] > a['stamina']:
            result.update(rounds=max_rounds, winner='B', end_reason='timeout_stam')
        else:
            result.update(rounds=max_rounds, winner='draw', end_reason='timeout')

    result['a_health'] = a['health']
    result['b_health'] = b['health']
    result['a_wounds'] = a['wounds']
    result['b_wounds'] = b['wounds']
    result['a_stamina'] = a['stamina']
    result['b_stamina'] = b['stamina']
    return result

# ── Battery runner ───────────────────────────────────────────────────────────

def run_battery(label, N, **kwargs):
    """Run N duels with different seeds. Return summary."""
    wins_a, wins_b, draws = 0, 0, 0  # [canonical: N/A — derived from canonical constants]
    reasons = defaultdict(int)
    rounds_list = []
    a_wounds_list, b_wounds_list = [], []
    a_stam_list, b_stam_list = [], []

    for i in range(N):
        r = sim_duel(seed=1000000 + i, **kwargs)  # [canonical: N/A — RNG seed]
        if r['winner'] == 'A':
            wins_a += 1  # [canonical: N/A — derived from canonical constants]
        elif r['winner'] == 'B':
            wins_b += 1  # [canonical: N/A — derived from canonical constants]
        else:
            draws += 1  # [canonical: N/A — derived from canonical constants]
        reasons[r['end_reason']] += 1  # [canonical: N/A — derived from canonical constants]
        rounds_list.append(r['rounds'])
        a_wounds_list.append(r['a_wounds'])
        b_wounds_list.append(r['b_wounds'])
        a_stam_list.append(r['a_stamina'])
        b_stam_list.append(r['b_stamina'])

    rounds_arr = np.array(rounds_list)
    return {
        'label': label, 'N': N,
        'win_a': wins_a / N, 'win_b': wins_b / N, 'draw': draws / N,
        'reasons': dict(reasons),
        'rounds_mean': float(rounds_arr.mean()),
        'rounds_median': float(np.median(rounds_arr)),
        'rounds_std': float(rounds_arr.std()),
        'rounds_min': int(rounds_arr.min()),
        'rounds_max': int(rounds_arr.max()),
        'a_wounds_mean': float(np.mean(a_wounds_list)),
        'b_wounds_mean': float(np.mean(b_wounds_list)),
        'a_stam_mean': float(np.mean(a_stam_list)),
        'b_stam_mean': float(np.mean(b_stam_list)),
    }

def fmt(r):
    reasons_str = ', '.join(f"{k}: {v}" for k, v in sorted(r['reasons'].items()))
    print(f"\n{'='*70}")
    print(f"  {r['label']}  (N={r['N']})")
    print(f"{'='*70}")
    print(f"  A wins: {r['win_a']:.1%}   B wins: {r['win_b']:.1%}   Draws: {r['draw']:.1%}")
    print(f"  Rounds: mean {r['rounds_mean']:.1f}, median {r['rounds_median']:.0f}, "
          f"std {r['rounds_std']:.1f}, range [{r['rounds_min']}–{r['rounds_max']}]")
    print(f"  End reasons: {reasons_str}")
    print(f"  Wounds: A mean {r['a_wounds_mean']:.1f}, B mean {r['b_wounds_mean']:.1f}")
    print(f"  Stamina remaining: A mean {r['a_stam_mean']:.1f}, B mean {r['b_stam_mean']:.1f}")

# ── Run battery ──────────────────────────────────────────────────────────────

N = 5000  # [canonical: N/A — simulation parameter]
BASE = dict(agi=4, str_=4, end=4, hist=2)  # [canonical: N/A — test character stats]

print("=" * 70)  # [canonical: N/A — output formatting]
print("  ARCHITECTURE C DUEL STRESS TEST — BATTERY RESULTS")
print("  Canonical: params/combat.md + designs/scene/combat_v30.md")
print("  Modifications: E5 (stance commit), E7 (posture-as-yield)")
print("=" * 70)  # [canonical: N/A — output formatting]

# H1: Mirror — same everything
fmt(run_battery("H1: Mirror (LightCut/None, Balanced vs Balanced)", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='BALANCED', protocol_b='BALANCED', **BASE))

# H2: Agi advantage
fmt(run_battery("H2: Agi advantage (A: Agi 5 vs B: Agi 3)", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='BALANCED', protocol_b='BALANCED',
    agi_a=5, agi_b=3, str_=4, end=4, hist=2, agi=4))  # [canonical: N/A — test character stats]

# H3: Endurance advantage
fmt(run_battery("H3: End advantage (A: End 6 vs B: End 3)", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='BALANCED', protocol_b='BALANCED',
    end_a=6, end_b=3, agi=4, str_=4, end=4, hist=2))  # [canonical: N/A — test character stats]

# H4: Weapon asymmetry
fmt(run_battery("H4: Weapon asymmetry (A: HeavyCut vs B: LightCut)", N,
    weapon_a='Short-HeavyCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='BALANCED', protocol_b='BALANCED', **BASE))

# H5: Aggressive vs Defensive
fmt(run_battery("H5: Protocol — Aggressive vs Defensive", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='AGGRESSIVE', protocol_b='DEFENSIVE', **BASE))

# H6: Feint-heavy vs Balanced
fmt(run_battery("H6: Protocol — Feint-heavy vs Balanced", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='FEINT_HEAVY', protocol_b='BALANCED', **BASE))

# H7: Adaptive vs Static (Balanced)
fmt(run_battery("H7: Protocol — Adaptive vs Balanced", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='ADAPTIVE', protocol_b='BALANCED', **BASE))

# H8: E7 ON vs OFF comparison — same matchup
for yaz, label in [(True, "E7 ON (yield-at-0)"), (False, "E7 OFF (canonical -2D)")]:
    fmt(run_battery(f"H8: {label}", N,
        weapon_a='Short-LightCut', armour_a='None',
        weapon_b='Short-LightCut', armour_b='None',
        protocol_a='AGGRESSIVE', protocol_b='DEFENSIVE',
        yield_at_zero=yaz, **BASE))

# H9: Armour asymmetry
fmt(run_battery("H9: Armour asymmetry (A: Heavy vs B: None)", N,
    weapon_a='Short-HeavyBlunt', armour_a='Heavy',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='BALANCED', protocol_b='BALANCED', **BASE))

# H10: Feint-spam stress
fmt(run_battery("H10: Feint-spam (A: every round) vs Balanced", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='FEINT_SPAM', protocol_b='BALANCED', **BASE))

# H11: Counter-puncher vs Aggressive
fmt(run_battery("H11: Counter-puncher vs Aggressive", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='COUNTER_PUNCHER', protocol_b='AGGRESSIVE', **BASE))

# H12: Long weapon vs Short weapon (reach dynamics simplified)
fmt(run_battery("H12: Long HeavyCut vs Short LightCut", N,
    weapon_a='Long-HeavyCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='BALANCED', protocol_b='BALANCED', **BASE))

# ── Duration/lethality summary ───────────────────────────────────────────────
print("\n\n" + "=" * 70)  # [canonical: N/A — output formatting]
print("  DUEL DURATION BY ENDURANCE (Balanced vs Balanced, LightCut, E7 ON)")
print("=" * 70)  # [canonical: N/A — output formatting]
print(f"  {'End':>4}  {'Stamina':>7}  {'Health':>6}  {'MaxW':>4}  {'Rounds':>8}  {'Yield%':>7}  {'Incap%':>7}")
for e in [2, 3, 4, 5, 6, 7]:  # [canonical: N/A — End range for duration sweep]
    r = run_battery(f"dur_end_{e}", 3000,  # [canonical: N/A — test battery parameters]
        weapon_a='Short-LightCut', armour_a='None',
        weapon_b='Short-LightCut', armour_b='None',
        protocol_a='BALANCED', protocol_b='BALANCED',
        agi=4, str_=4, end=e, hist=2)  # [canonical: N/A — test character stats]
    yield_pct = sum(v for k, v in r['reasons'].items() if 'yield' in k) / 3000  # [canonical: N/A — derived from canonical constants]
    incap_pct = sum(v for k, v in r['reasons'].items() if 'incap' in k) / 3000  # [canonical: N/A — derived from canonical constants]
    print(f"  {e:>4}  {e*5:>7}  {calc_health(e):>6}  {max_wounds(e):>4}  {r['rounds_mean']:>8.1f}  {yield_pct:>7.1%}  {incap_pct:>7.1%}")

print("\n\n" + "=" * 70)  # [canonical: N/A — output formatting]
print("  FINDINGS")
print("=" * 70)  # [canonical: N/A — output formatting]
