#!/usr/bin/env python3
"""Architecture C duel stress test v3b — rebalanced triangle + END-based bind."""
import numpy as np
from collections import defaultdict

# ── Canonical constants ──────────────────────────────────────────────────────
# [canonical: params/combat.md §Weapon System PP-232]
WEAPONS = {
    'Short-LightCut':   ('Short','LightCut',  5,6,1,2,1),  # [canonical: params/combat.md §Weapon System PP-232]
    'Short-HeavyCut':   ('Short','HeavyCut',  6,7,4,5,3),  # [canonical: params/combat.md §Weapon System PP-232]
    'Long-LightCut':    ('Long', 'LightCut',  5,6,1,2,1),  # [canonical: params/combat.md §Weapon System PP-232]
    'Long-HeavyCut':    ('Long', 'HeavyCut',  6,7,4,5,3),  # [canonical: params/combat.md §Weapon System PP-232]
    'Short-LightBlunt': ('Short','LightBlunt',6,7,1,2,1),  # [canonical: params/combat.md §Weapon System PP-232]
    'Long-HeavyBlunt':  ('Long', 'HeavyBlunt',7,8,4,5,4),  # [canonical: params/combat.md §Weapon System PP-232]
    'Unarmed':          ('Short','LightBlunt', 8,9,0,0,1),  # [canonical: params/combat.md §Weapon System PP-232]
}
# [canonical: params/combat.md §Armour]
ARMOUR_DR = {'None':(0,0,0,0),'Light':(2,1,1,0),'Medium':(4,3,2,1),'Heavy':(6,5,3,1)}
TYPE_IDX = {'LightCut':0,'HeavyCut':1,'LightBlunt':2,'HeavyBlunt':3}  # [canonical: params/combat.md §Weapon System PP-232]
CRIT_THRESH = 3  # [canonical: params/combat.md §Damage Formula]

# [canonical: params/combat.md §Pool Formula L14]
def calc_pool(agi, hist):
    return max(5, agi * 2 + hist + 3)  # [canonical: params/combat.md §Pool Formula]

# [canonical: params/combat.md §Stamina ED-694 L15]
def calc_stamina(end):
    return end * 5  # [canonical: params/combat.md §Stamina ED-694]

# [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]
def max_wounds(end):
    return end // 2 + 1  # [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]

def wound_interval(end):
    return end + 6  # [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]

def calc_health(end):
    return (end + 6) * (max_wounds(end) + 1)  # [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]

def get_dr(wtype, armour):
    return ARMOUR_DR[armour][TYPE_IDX[wtype]]  # [canonical: params/combat.md §Armour]

# [canonical: params/combat.md §Stamina L15 — standard 5, heavy 8, defensive 3]
STAM_COST = {'pulsativa': 5, 'stabile': 3, 'instabile': 4, 'advance': 2, 'retreat': 2, 'bind_contest': 2}

# [canonical: params/core.md §dice engine — d10 pool TN system]
def vroll(rng, n, tn):
    if n <= 0:
        return 0  # [canonical: N/A — floor]
    rolls = rng.integers(1, 11, size=n)  # [canonical: params/core.md §dice engine]
    hits = int(np.sum(rolls >= tn))
    ones = int(np.sum(rolls == 1))  # [canonical: params/core.md §dice engine — 1s subtract]
    tens = int(np.sum(rolls == 10))  # [canonical: params/core.md §dice engine — chain on 10]
    chain_hits = 0
    if tens > 0:
        chain_hits = int(np.sum(rng.integers(1, 11, size=tens) >= tn))  # [canonical: params/core.md §dice engine]
    return max(0, hits + chain_hits - ones)

# ── Fiore stance triangle (EXPLORATORY — replaces v1 Aggressive/Balanced/Defensive) ──
# [canonical: Fiore dei Liberi, Fior di Battaglia ~1410 — Stabile/Pulsativa/Instabile classification]
#
# PULSATIVA (Striking) — committed attack. High offense pool.
#   Beats INSTABILE (attack lands before counter forms)
#   Loses to STABILE (absorbed → riposte)
#
# STABILE (Stable) — strong defensive guard. Moderate offense.
#   On successful defense vs Pulsativa: RIPOSTE (free counter at half-defense-pool bonus)
#   Beats PULSATIVA (absorb → riposte)
#   Loses to INSTABILE (provoked out of guard → Meisterhau)
#
# INSTABILE (Mutable) — provocative, baiting. Lower immediate threat.
#   On correct read vs Stabile: MEISTERHAU (simultaneous parry+strike, bonus dice)
#   Beats STABILE (draws out → counter)
#   Loses to PULSATIVA (committed attack arrives first)

# Pool allocation ratios: (offense_fraction, defense_fraction)
# [canonical: derived from Fiore guard classification — not canonical]
STANCE_POOLS = {
    'pulsativa': (0.75, 0.25),  # [canonical: committed attack — high offense]
    'stabile':   (0.35, 0.65),  # [canonical: defensive guard — high defense]
    'instabile': (0.50, 0.50),  # [canonical: balanced but reactive — moderate both]
}

# Triangle payoff matrix: (stance_a, stance_b) → effect
# 'normal': standard exchange
# 'riposte_a'/'riposte_b': defender gets free counter-attack
# 'meisterhau_a'/'meisterhau_b': counter-attacker gets bonus dice
# 'bind': both committed, neither clean → Fühlen contested roll
TRIANGLE = {
    ('pulsativa', 'pulsativa'): 'bind',          # both commit → blades meet
    ('pulsativa', 'stabile'):   'riposte_b',      # B absorbs, ripostes
    ('pulsativa', 'instabile'): 'pulsativa_a',    # A's attack lands before B's counter
    ('stabile',   'pulsativa'): 'riposte_a',      # A absorbs, ripostes
    ('stabile',   'stabile'):   'probing',         # both wait → minimal exchange
    ('stabile',   'instabile'): 'meisterhau_b',    # B provokes A out, counters
    ('instabile', 'pulsativa'): 'pulsativa_b',     # B's attack lands first
    ('instabile', 'stabile'):   'meisterhau_a',    # A provokes B out, counters
    ('instabile', 'instabile'): 'probing',         # both bait → minimal exchange
}

# Riposte bonus: fraction of defense pool added as bonus offense dice
RIPOSTE_BONUS_FRAC = 0.5  # [canonical: "good parries apply a thrust in opposition" — Liechtenauer]
# Meisterhau bonus: flat dice bonus for correct read
MEISTERHAU_BONUS = 2  # [canonical: Meisterhau — reduced from +3; defender keeps full defense in v3]

# ── 2D Distance (fluid, limited positioning) ─────────────────────────────────
# [canonical: Zufechten/Krieg/Abzug — Liechtenauer three phases of measure]
# Distance is a float 0.0–3.0:
#   0.0–1.0 = KRIEG (close/bind range — grappling possible, bind contests happen here)
#   1.0–2.0 = STRIKING (standard combat range — full exchanges)
#   2.0–3.0 = ZUFECHTEN (approach — must close before attacking; only feints/provocations)
DIST_KRIEG = 1.0  # [canonical: Krieg threshold]
DIST_STRIKING = 2.0  # [canonical: striking range threshold]
DIST_MAX = 3.0  # [canonical: max distance]
DIST_START = 2.5  # [canonical: duels start at approach range]
ADVANCE_STEP = 0.8  # [canonical: distance closed per advance]
RETREAT_STEP = 0.6  # [canonical: distance gained per retreat — slower than advance]

# ── Duelist state ────────────────────────────────────────────────────────────

def make_duelist(weapon, armour, agi, str_, end, hist):
    w = WEAPONS[weapon]  # [canonical: params/combat.md §Weapon System PP-232]
    return {
        'weapon': weapon, 'armour': armour,
        'reach': w[0], 'wtype': w[1],
        'tn_off': w[2], 'tn_def': w[3],  # [canonical: N/A — derived]
        'dmg_min': w[4], 'dmg_max': w[5],  # [canonical: N/A — derived]
        'base_pool': calc_pool(agi, hist),
        'max_stamina': calc_stamina(end), 'stamina': calc_stamina(end),
        'max_health': calc_health(end), 'health': calc_health(end),
        'max_wounds': max_wounds(end), 'wounds': 0,
        'wound_interval': wound_interval(end), 'dmg_acc': 0,
        'has_init': False,
        'agi': agi, 'str': str_, 'end': end, 'hist': hist,
        'bind_advantage': 0,  # +dice from winning a bind contest
    }

# [canonical: params/combat.md §Pool Formula — wound penalty -1D, floor 1D PP-273]
def effective_pool(d):
    p = d['base_pool'] - d['wounds'] + d['bind_advantage']
    return max(1, p)

# [canonical: params/combat.md §Damage Formula PP-232]
def apply_damage(defender, raw_dmg, attacker):
    dr = get_dr(attacker['wtype'], defender['armour'])
    net_dmg = max(0, raw_dmg - dr)
    if net_dmg == 0:
        return 0
    defender['health'] -= net_dmg
    defender['dmg_acc'] += net_dmg
    new_wounds = 0
    while defender['dmg_acc'] >= defender['wound_interval'] and defender['wounds'] < defender['max_wounds']:
        defender['wounds'] += 1  # [canonical: designs/scene/derived_stats_v30.md §4.1 PP-716]
        defender['dmg_acc'] -= defender['wound_interval']
        new_wounds += 1
    if defender['health'] <= 0:
        defender['health'] = 0
    return new_wounds

def resolve_strike(rng, attacker, defender, off_dice, def_dice, bonus_off=0):
    """Resolve one strike: attacker rolls off_dice + bonus, defender rolls def_dice."""
    total_off = max(1, off_dice + bonus_off)  # [canonical: designs/scene/combat_v30.md §4 Actions]
    hits = vroll(rng, total_off, attacker['tn_off'])
    blocks = vroll(rng, def_dice, defender['tn_def'])
    net = max(0, hits - blocks)
    dmg_dealt = 0
    if net > 0:
        dmg_add = rng.integers(attacker['dmg_min'], attacker['dmg_max'] + 1)  # [canonical: params/combat.md §Damage Formula]
        raw_dmg = net + attacker['str'] + dmg_add
        if hits - blocks >= CRIT_THRESH:  # [canonical: params/combat.md §Damage Formula]
            raw_dmg *= 2  # [canonical: params/combat.md §Damage Formula — crit]
        apply_damage(defender, raw_dmg, attacker)
        dmg_dealt = raw_dmg
    return net, dmg_dealt

# ── Decision protocols ───────────────────────────────────────────────────────

def choose_stance(protocol, me, opp, distance, rng):
    """Return stance name based on protocol and state."""
    my_stam_frac = me['stamina'] / max(1, me['max_stamina'])
    opp_stam_frac = opp['stamina'] / max(1, opp['max_stamina'])

    if protocol == 'PULSATIVA':
        return 'pulsativa'
    elif protocol == 'STABILE':
        return 'stabile'
    elif protocol == 'INSTABILE':
        return 'instabile'
    elif protocol == 'MIXED_RANDOM':
        return rng.choice(['pulsativa', 'stabile', 'instabile'])
    elif protocol == 'MIXED_WEIGHTED':
        # Weight toward pulsativa at close range, stabile at far, instabile in between
        if distance <= DIST_KRIEG:  # [canonical: close range favors commitment]
            return rng.choice(['pulsativa', 'pulsativa', 'instabile'])
        elif distance >= DIST_STRIKING:  # [canonical: far range favors patience]
            return rng.choice(['stabile', 'stabile', 'instabile'])
        else:
            return rng.choice(['pulsativa', 'stabile', 'instabile'])
    elif protocol == 'ADAPTIVE':
        # Read opponent's stamina and health to pick stance
        if opp_stam_frac < 0.3:  # [canonical: finish wounded opponent]
            return 'pulsativa'
        elif my_stam_frac < 0.3:  # [canonical: conserve when low]
            return 'stabile'
        elif me['has_init']:  # [canonical: press initiative advantage]
            return 'pulsativa'
        else:
            return 'instabile'  # [canonical: try to steal initiative back]
    elif protocol == 'COUNTER_FIGHTER':
        # Always try to read and counter — stabile if opponent aggressive, instabile otherwise
        if opp['has_init']:
            return 'stabile'  # [canonical: absorb their attack]
        else:
            return 'instabile'  # [canonical: provoke them out]
    elif protocol == 'BERSERKER':
        return 'pulsativa'  # [canonical: always attack — tests whether triangle punishes]
    elif protocol == 'TURTLE':
        return 'stabile'  # [canonical: always defend — tests whether turtle is viable]
    elif protocol == 'TRICKSTER':
        return 'instabile'  # [canonical: always bait — tests Meisterhau viability]
    elif protocol == 'NASH_EQUILIBRIUM':
        # If triangle is balanced RPS, Nash equilibrium is 1/3 each
        return rng.choice(['pulsativa', 'stabile', 'instabile'])
    else:
        return 'stabile'

def choose_movement(protocol, me, opp, distance, rng):
    """Return 'advance', 'retreat', or 'hold'."""
    if distance > DIST_STRIKING:  # [canonical: must close to fight]
        return 'advance'
    if protocol in ('BERSERKER', 'PULSATIVA'):
        if distance > DIST_KRIEG + 0.3:  # [canonical: aggressive closer wants Krieg range]
            return 'advance'
    if protocol in ('TURTLE', 'STABILE', 'COUNTER_FIGHTER'):
        if distance < DIST_KRIEG:
            return 'retreat'  # [canonical: defensive fighter wants striking range, not grapple]
    return 'hold'

# ── Duel simulation v2 ──────────────────────────────────────────────────────

# [canonical: designs/scene/combat_v30.md §1-§4 — round structure, initiative, actions]
def sim_duel_v2(weapon_a, armour_a, weapon_b, armour_b,
                agi=4, str_=4, end=4, hist=2,  # [canonical: N/A — test character stats]
                protocol_a='ADAPTIVE', protocol_b='ADAPTIVE',
                yield_at_zero=True,
                seed=42, max_rounds=30,  # [canonical: N/A — test battery]
                agi_a=None, agi_b=None, end_a=None, end_b=None,
                str_a=None, str_b=None):
    rng = np.random.default_rng(seed)  # [canonical: N/A — RNG]

    ea, eb = end_a or end, end_b or end
    sa, sb = str_a or str_, str_b or str_
    aa, ab = agi_a or agi, agi_b or agi

    a = make_duelist(weapon_a, armour_a, aa, sa, ea, hist)
    b = make_duelist(weapon_b, armour_b, ab, sb, eb, hist)

    # Initiative: higher Agi starts
    if aa > ab:
        a['has_init'] = True
    elif ab > aa:
        b['has_init'] = True
    else:
        a['has_init'] = bool(rng.integers(0, 2))  # [canonical: N/A — tiebreak]
        b['has_init'] = not a['has_init']

    distance = DIST_START  # [canonical: start at approach range]
    result = {'rounds': 0, 'winner': None, 'end_reason': None,
              'a_health': 0, 'b_health': 0, 'a_wounds': 0, 'b_wounds': 0,
              'a_stamina': 0, 'b_stamina': 0, 'binds': 0, 'ripostes': 0,
              'meisterhau': 0, 'stance_counts_a': defaultdict(int),
              'stance_counts_b': defaultdict(int)}

    for rd in range(1, max_rounds + 1):  # [canonical: N/A — sim loop]
        # ── End checks (simultaneous) ──
        a_dead = a['health'] <= 0 and a['wounds'] >= a['max_wounds']
        b_dead = b['health'] <= 0 and b['wounds'] >= b['max_wounds']
        if a_dead and b_dead:
            result.update(rounds=rd, winner='draw', end_reason='mutual_incap')
            break
        elif a_dead:
            result.update(rounds=rd, winner='B', end_reason='incap_A')
            break
        elif b_dead:
            result.update(rounds=rd, winner='A', end_reason='incap_B')
            break

        if yield_at_zero:
            ay, by = a['stamina'] <= 0, b['stamina'] <= 0
            if ay and by:
                w = 'A' if a['health'] > b['health'] else ('B' if b['health'] > a['health'] else 'draw')
                result.update(rounds=rd, winner=w, end_reason='mutual_yield')
                break
            elif ay:
                result.update(rounds=rd, winner='B', end_reason='yield_A')
                break
            elif by:
                result.update(rounds=rd, winner='A', end_reason='yield_B')
                break

        # ── Movement phase ──
        move_a = choose_movement(protocol_a, a, b, distance, rng)
        move_b = choose_movement(protocol_b, b, a, distance, rng)

        if move_a == 'advance':
            distance = max(0, distance - ADVANCE_STEP)
            a['stamina'] = max(0, a['stamina'] - STAM_COST['advance'])  # [canonical: params/combat.md §Stamina]
        elif move_a == 'retreat':
            distance = min(DIST_MAX, distance + RETREAT_STEP)
            a['stamina'] = max(0, a['stamina'] - STAM_COST['retreat'])
        if move_b == 'advance':
            distance = max(0, distance - ADVANCE_STEP)
            b['stamina'] = max(0, b['stamina'] - STAM_COST['advance'])
        elif move_b == 'retreat':
            distance = min(DIST_MAX, distance + RETREAT_STEP)
            b['stamina'] = max(0, b['stamina'] - STAM_COST['retreat'])

        # ── Stance declaration (lower-init declares first per canonical §3) ──
        if a['has_init']:
            stance_b = choose_stance(protocol_b, b, a, distance, rng)
            stance_a = choose_stance(protocol_a, a, b, distance, rng)
        else:
            stance_a = choose_stance(protocol_a, a, b, distance, rng)
            stance_b = choose_stance(protocol_b, b, a, distance, rng)

        result['stance_counts_a'][stance_a] += 1
        result['stance_counts_b'][stance_b] += 1

        # ── If out of striking range, no exchange this round ──
        if distance > DIST_STRIKING:
            continue

        # ── Determine pool splits ──
        pool_a = effective_pool(a)
        pool_b = effective_pool(b)
        a['bind_advantage'] = 0  # reset each round
        b['bind_advantage'] = 0

        off_frac_a, def_frac_a = STANCE_POOLS[stance_a]
        off_frac_b, def_frac_b = STANCE_POOLS[stance_b]

        off_a = max(1, int(pool_a * off_frac_a))  # [canonical: designs/scene/combat_v30.md §1 pool split]
        def_a = max(0, pool_a - off_a)
        off_b = max(1, int(pool_b * off_frac_b))
        def_b = max(0, pool_b - off_b)

        # ── Resolve triangle outcome ──
        outcome = TRIANGLE[(stance_a, stance_b)]
        bonus_a, bonus_b = 0, 0

        if outcome == 'riposte_a':
            # A absorbs B's pulsativa, then ripostes
            # B attacks A with full offense; A defends with high pool
            # Then A gets bonus counter-attack
            net_b, _ = resolve_strike(rng, b, a, off_b, def_a)
            bonus_a = max(1, int(def_a * RIPOSTE_BONUS_FRAC))  # [canonical: riposte bonus]
            resolve_strike(rng, a, b, off_a, def_b, bonus_off=bonus_a)
            result['ripostes'] += 1
            a['stamina'] = max(0, a['stamina'] - STAM_COST['stabile'])
            b['stamina'] = max(0, b['stamina'] - STAM_COST['pulsativa'])
            # Initiative: riposte winner gets Vor
            a['has_init'] = True; b['has_init'] = False

        elif outcome == 'riposte_b':
            net_a, _ = resolve_strike(rng, a, b, off_a, def_b)
            bonus_b = max(1, int(def_b * RIPOSTE_BONUS_FRAC))
            resolve_strike(rng, b, a, off_b, def_a, bonus_off=bonus_b)
            result['ripostes'] += 1
            a['stamina'] = max(0, a['stamina'] - STAM_COST['pulsativa'])
            b['stamina'] = max(0, b['stamina'] - STAM_COST['stabile'])
            b['has_init'] = True; a['has_init'] = False

        elif outcome == 'pulsativa_a':
            # A's committed attack has priority + momentum — B defends at full pool, no counter
            resolve_strike(rng, a, b, off_a, def_b, bonus_off=1)  # [canonical: v3b — +1 momentum]
            # B gets no attack this round (caught mid-transition)
            a['stamina'] = max(0, a['stamina'] - STAM_COST['pulsativa'])
            b['stamina'] = max(0, b['stamina'] - STAM_COST['instabile'])
            a['has_init'] = True; b['has_init'] = False

        elif outcome == 'pulsativa_b':
            resolve_strike(rng, b, a, off_b, def_a, bonus_off=1)  # [canonical: v3b — +1 momentum]
            a['stamina'] = max(0, a['stamina'] - STAM_COST['instabile'])
            b['stamina'] = max(0, b['stamina'] - STAM_COST['pulsativa'])
            b['has_init'] = True; a['has_init'] = False

        elif outcome == 'meisterhau_a':
            # A (instabile) provokes B (stabile) out of guard — Meisterhau counter-strike
            # A gets bonus dice; B defense reduced to 2/3 (drawn out of guard, not halved)
            drawn_def_b = max(1, int(def_b * 2 / 3))  # [canonical: v3b — 2/3 defense, "provoked out"]
            resolve_strike(rng, a, b, off_a, drawn_def_b, bonus_off=MEISTERHAU_BONUS)
            resolve_strike(rng, b, a, max(1, off_b // 2), def_a)  # [canonical: B disrupted]
            result['meisterhau'] += 1
            a['stamina'] = max(0, a['stamina'] - STAM_COST['instabile'])
            b['stamina'] = max(0, b['stamina'] - STAM_COST['stabile'])
            a['has_init'] = True; b['has_init'] = False

        elif outcome == 'meisterhau_b':
            drawn_def_a = max(1, int(def_a * 2 / 3))  # [canonical: v3b — 2/3 defense]
            resolve_strike(rng, b, a, off_b, drawn_def_a, bonus_off=MEISTERHAU_BONUS)
            resolve_strike(rng, a, b, max(1, off_a // 2), def_b)  # [canonical: A disrupted]
            result['meisterhau'] += 1
            a['stamina'] = max(0, a['stamina'] - STAM_COST['stabile'])
            b['stamina'] = max(0, b['stamina'] - STAM_COST['instabile'])
            b['has_init'] = True; a['has_init'] = False

        elif outcome == 'bind':
            # [canonical: Fühlen — contested roll in the bind per Liechtenauer]
            # Both committed (pulsativa vs pulsativa) → blades meet
            # First: both strike simultaneously (reduced by mutual interference)
            resolve_strike(rng, a, b, off_a, def_b)
            resolve_strike(rng, b, a, off_b, def_a)
            # Then: Fühlen bind contest — Agi-based contested roll
            # Winner gets +2D bind advantage next round AND initiative
            bind_a = vroll(rng, ea, 7)  # [canonical: v3 — bind uses END (physical) not AGI]
            bind_b = vroll(rng, eb, 7)
            if bind_a > bind_b:
                a['bind_advantage'] = 2  # [canonical: bind advantage bonus]
                a['has_init'] = True; b['has_init'] = False
            elif bind_b > bind_a:
                b['bind_advantage'] = 2
                b['has_init'] = True; a['has_init'] = False
            # Tie: both stay, no advantage
            result['binds'] += 1
            a['stamina'] = max(0, a['stamina'] - STAM_COST['pulsativa'] - STAM_COST['bind_contest'])
            b['stamina'] = max(0, b['stamina'] - STAM_COST['pulsativa'] - STAM_COST['bind_contest'])
            # Bind also closes distance
            distance = min(distance, DIST_KRIEG)  # [canonical: bind pulls to Krieg range]

        elif outcome == 'probing':
            # Both cautious — minimal exchange
            # Light probing attacks at reduced pools
            resolve_strike(rng, a, b, max(1, off_a // 2), def_b)  # [canonical: probing — half offense]
            resolve_strike(rng, b, a, max(1, off_b // 2), def_a)
            a['stamina'] = max(0, a['stamina'] - 2)  # [canonical: v3 — probing drains less]
            b['stamina'] = max(0, b['stamina'] - 2)
            # No initiative change on probing

    else:
        # Max rounds
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
    result['final_distance'] = distance
    return result

# ── Battery runner ───────────────────────────────────────────────────────────

def run_battery(label, N, **kwargs):
    wins_a, wins_b, draws = 0, 0, 0
    reasons = defaultdict(int)
    rounds_list, binds_list, ripostes_list, meisterhau_list = [], [], [], []
    a_wounds_list, b_wounds_list, a_stam_list, b_stam_list = [], [], [], []
    stance_totals_a, stance_totals_b = defaultdict(int), defaultdict(int)

    for i in range(N):  # [canonical: N/A — sim loop]
        r = sim_duel_v2(seed=1000000 + i, **kwargs)  # [canonical: N/A — RNG seed]
        if r['winner'] == 'A': wins_a += 1
        elif r['winner'] == 'B': wins_b += 1
        else: draws += 1
        reasons[r['end_reason']] += 1
        rounds_list.append(r['rounds'])
        binds_list.append(r['binds'])
        ripostes_list.append(r['ripostes'])
        meisterhau_list.append(r['meisterhau'])
        a_wounds_list.append(r['a_wounds'])
        b_wounds_list.append(r['b_wounds'])
        a_stam_list.append(r['a_stamina'])
        b_stam_list.append(r['b_stamina'])
        for k, v in r['stance_counts_a'].items(): stance_totals_a[k] += v
        for k, v in r['stance_counts_b'].items(): stance_totals_b[k] += v

    ra = np.array(rounds_list)
    return {
        'label': label, 'N': N,
        'win_a': wins_a / N, 'win_b': wins_b / N, 'draw': draws / N,
        'reasons': dict(reasons),
        'rounds_mean': float(ra.mean()), 'rounds_std': float(ra.std()),
        'rounds_min': int(ra.min()), 'rounds_max': int(ra.max()),
        'a_wounds_mean': float(np.mean(a_wounds_list)),
        'b_wounds_mean': float(np.mean(b_wounds_list)),
        'a_stam_mean': float(np.mean(a_stam_list)),
        'b_stam_mean': float(np.mean(b_stam_list)),
        'binds_mean': float(np.mean(binds_list)),
        'ripostes_mean': float(np.mean(ripostes_list)),
        'meisterhau_mean': float(np.mean(meisterhau_list)),
        'stance_a': dict(stance_totals_a), 'stance_b': dict(stance_totals_b),
    }

def fmt(r):
    reasons_str = ', '.join(f"{k}: {v}" for k, v in sorted(r['reasons'].items()))
    print(f"\n{'='*74}")
    print(f"  {r['label']}  (N={r['N']})")
    print(f"{'='*74}")
    print(f"  A wins: {r['win_a']:.1%}   B wins: {r['win_b']:.1%}   Draws: {r['draw']:.1%}")
    print(f"  Rounds: mean {r['rounds_mean']:.1f} ±{r['rounds_std']:.1f}, range [{r['rounds_min']}–{r['rounds_max']}]")
    print(f"  End reasons: {reasons_str}")
    print(f"  Wounds: A {r['a_wounds_mean']:.1f}, B {r['b_wounds_mean']:.1f}")
    print(f"  Stamina left: A {r['a_stam_mean']:.1f}, B {r['b_stam_mean']:.1f}")
    print(f"  Binds/duel: {r['binds_mean']:.1f}  Ripostes/duel: {r['ripostes_mean']:.1f}  Meisterhau/duel: {r['meisterhau_mean']:.1f}")

# ── Run battery ──────────────────────────────────────────────────────────────

N = 5000  # [canonical: N/A — simulation parameter]
BASE = dict(agi=4, str_=4, end=4, hist=2)  # [canonical: N/A — test character stats]

print("=" * 74)  # [canonical: N/A — output]
print("  ARCHITECTURE C v2 — FIORE TRIANGLE + FÜHLEN BIND + 2D DISTANCE")
print("=" * 74)  # [canonical: N/A — output]

# ── TRIANGLE VALIDATION (core RPS balance) ──
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  SECTION 1: TRIANGLE VALIDATION — pure stance vs pure stance")
print("~" * 74)  # [canonical: N/A — output]

for pa, pb in [('PULSATIVA','STABILE'), ('STABILE','INSTABILE'), ('INSTABILE','PULSATIVA'),
               ('PULSATIVA','PULSATIVA'), ('STABILE','STABILE'), ('INSTABILE','INSTABILE')]:
    fmt(run_battery(f"T: {pa} vs {pb}", N,
        weapon_a='Short-LightCut', armour_a='None',
        weapon_b='Short-LightCut', armour_b='None',
        protocol_a=pa, protocol_b=pb, **BASE))

# ── PROTOCOL COMPARISON ──
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  SECTION 2: PROTOCOL COMPARISON — strategic approaches")
print("~" * 74)  # [canonical: N/A — output]

for pa, pb, label in [
    ('ADAPTIVE', 'ADAPTIVE', 'H1: Mirror — Adaptive vs Adaptive'),
    ('BERSERKER', 'TURTLE', 'H2: Berserker vs Turtle'),
    ('BERSERKER', 'COUNTER_FIGHTER', 'H3: Berserker vs Counter-fighter'),
    ('TRICKSTER', 'ADAPTIVE', 'H4: Trickster vs Adaptive'),
    ('COUNTER_FIGHTER', 'ADAPTIVE', 'H5: Counter-fighter vs Adaptive'),
    ('NASH_EQUILIBRIUM', 'NASH_EQUILIBRIUM', 'H6: Nash (1/3 each) vs Nash'),
    ('MIXED_WEIGHTED', 'ADAPTIVE', 'H7: Distance-weighted vs Adaptive'),
]:
    fmt(run_battery(label, N,
        weapon_a='Short-LightCut', armour_a='None',
        weapon_b='Short-LightCut', armour_b='None',
        protocol_a=pa, protocol_b=pb, **BASE))

# ── STAT ASYMMETRY ──
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  SECTION 3: STAT ASYMMETRY — does End still dominate?")
print("~" * 74)  # [canonical: N/A — output]

fmt(run_battery("S1: Agi 5 vs Agi 3 (Adaptive)", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='ADAPTIVE', protocol_b='ADAPTIVE',
    agi_a=5, agi_b=3, **BASE))  # [canonical: N/A — test character stats]

fmt(run_battery("S2: End 6 vs End 3 (Adaptive)", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='ADAPTIVE', protocol_b='ADAPTIVE',
    end_a=6, end_b=3, **BASE))  # [canonical: N/A — derived]

fmt(run_battery("S3: End 5 vs End 4 (Adaptive — mild gap)", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='ADAPTIVE', protocol_b='ADAPTIVE',
    end_a=5, end_b=4, **BASE))  # [canonical: N/A — derived]

fmt(run_battery("S4: STR 6 vs STR 3 (Adaptive)", N,
    weapon_a='Short-LightCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='ADAPTIVE', protocol_b='ADAPTIVE',
    str_a=6, str_b=3, **BASE))  # [canonical: N/A — test character stats]

# ── WEAPON ASYMMETRY ──
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  SECTION 4: WEAPON ASYMMETRY")
print("~" * 74)  # [canonical: N/A — output]

fmt(run_battery("W1: HeavyCut vs LightCut (Adaptive)", N,
    weapon_a='Short-HeavyCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='ADAPTIVE', protocol_b='ADAPTIVE', **BASE))

fmt(run_battery("W2: Long-HeavyCut vs Short-LightCut (Adaptive)", N,
    weapon_a='Long-HeavyCut', armour_a='None',
    weapon_b='Short-LightCut', armour_b='None',
    protocol_a='ADAPTIVE', protocol_b='ADAPTIVE', **BASE))

# ── E7 COMPARISON ──
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  SECTION 5: E7 ON vs OFF (yield vs canonical -2D)")
print("~" * 74)  # [canonical: N/A — output]

for yaz, label in [(True, "E7 ON"), (False, "E7 OFF")]:
    fmt(run_battery(f"E7: {label} — Berserker vs Turtle", N,
        weapon_a='Short-LightCut', armour_a='None',
        weapon_b='Short-LightCut', armour_b='None',
        protocol_a='BERSERKER', protocol_b='TURTLE',
        yield_at_zero=yaz, **BASE))

# ── DURATION TABLE ──
print("\n" + "~" * 74)  # [canonical: N/A — output]
print("  SECTION 6: DURATION BY ENDURANCE")
print("~" * 74)  # [canonical: N/A — output]
print(f"  {'End':>4}  {'Stam':>5}  {'HP':>4}  {'MW':>3}  {'Rnds':>6}  {'Yield%':>7}  {'Incap%':>7}  {'Binds':>6}")
for e in [2, 3, 4, 5, 6, 7]:  # [canonical: N/A — End range for duration sweep]
    r = run_battery(f"dur_{e}", 3000,  # [canonical: N/A — simulation parameter]
        weapon_a='Short-LightCut', armour_a='None',
        weapon_b='Short-LightCut', armour_b='None',
        protocol_a='ADAPTIVE', protocol_b='ADAPTIVE',
        agi=4, str_=4, end=e, hist=2)  # [canonical: N/A — test character stats]
    yield_pct = sum(v for k, v in r['reasons'].items() if 'yield' in k) / 3000  # [canonical: N/A — derived]
    incap_pct = sum(v for k, v in r['reasons'].items() if 'incap' in k) / 3000  # [canonical: N/A — derived]
    print(f"  {e:>4}  {e*5:>5}  {calc_health(e):>4}  {max_wounds(e):>3}  {r['rounds_mean']:>6.1f}  {yield_pct:>7.1%}  {incap_pct:>7.1%}  {r['binds_mean']:>6.1f}")

print("\n" + "=" * 74)  # [canonical: N/A — output]
print("  FINDINGS")
print("=" * 74)  # [canonical: N/A — output]
