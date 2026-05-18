#!/usr/bin/env python3
# Phase 11 — C4 mechanics test: M1 (reach gate) + M2 (stance counter) + M3 (init preempt)
# Baseline: Phase 10 best-stack (undoubled pool + 1/End Ob wound + Disarm + canonical stam + STR-strong)
# Question: does C4 break Agi pool-dominance to ~50/50 at canonical attribute differences?

import random
import math

# Canonical constants (from Phase 10)
DIE_MEAN_TN7 = 0.4  # [canonical: params/core.md §Expected Value, TN 7 row]
DIE_STD_TN7 = 0.8  # [canonical: params/core.md §Expected Value, TN 7 row]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]
COMBAT_POOL_FLOOR = 5  # [canonical: params/combat.md L14]
ACTION_COST = 5  # [canonical: params/combat.md L15]
TAKE_BREATH_COST = 3  # [canonical: params/combat.md L15 - defensive 3]
TAKE_BREATH_TRIGGER = 8  # [canonical: N/A - Phase 8 AI calibration]
CRIT_MAGNITUDE = 4.0  # [canonical: params/combat.md L91 - PP-717 D3]
DISARM_NET_THRESHOLD = 2.0  # [canonical: N/A - Phase 10 proxy: net >=2 to disarm]

# === M1: Reach/Distance gate ===
# Distance band 0=close, 1=near, 2=mid, 3=far. Round starts at distance=2.
# Weapon reach: out-of-range attacks cut effective pool to 1D + History.
WEAPONS = {
    'light_blade':  {'damage_mod': 3, 'str_mult': 1.0, 'reach': 1},  # [canonical: params/combat.md damage table - Light Blade; reach 1 = N/A Phase 11 reform]
    'heavy_weapon': {'damage_mod': 5, 'str_mult': 2.0, 'reach': 2},  # [canonical: params/combat.md damage table - Heavy class x2; reach 2 = N/A Phase 11 reform]
    'polearm':      {'damage_mod': 4, 'str_mult': 1.5, 'reach': 3},  # [canonical: N/A - Phase 11 proxy: medium-heavy weapon class, reach 3 reform]
    'unarmed':      {'damage_mod': 0, 'str_mult': 0.5, 'reach': 0},  # [canonical: N/A - Phase 10 proxy: disarmed damage output]
}
STARTING_DISTANCE = 2  # [canonical: N/A - Phase 11 reform: M1 starting distance band]


# === M2 magnitudes: empirical guesses per Phase 11 reform; tune in Phase 12+ ===
# [canonical: N/A - Phase 11 reform tuning targets; all M2 effect magnitudes provisional]

# === M2: Stance counter-table ===
# Both fighters declare stance simultaneously each round.
# Stance modifies pool split (offense/defense). Counter-table applies additional effects.
STANCES = ['pressure', 'patience', 'decisive', 'cautious']

def stance_split(stance, pool):
    """Base pool split per stance.  # [canonical: N/A - Phase 11 reform M2 magnitudes empirical]"""
    if stance == 'pressure':  return (pool + 2, max(POOL_FLOOR, pool - 1))  # [canonical: N/A - Phase 11 reform M2]
    if stance == 'patience':  return (max(POOL_FLOOR, pool - 1), pool + 2)  # [canonical: N/A - Phase 11 reform M2]
    if stance == 'decisive':  return (pool + 1, POOL_FLOOR)                  # [canonical: N/A - Phase 11 reform M2]
    if stance == 'cautious':  return (max(POOL_FLOOR, pool // 2), pool + 1)  # [canonical: N/A - Phase 11 reform M2]
    return (pool, pool)

# M2 counter effects (mine, theirs) -> dict of effects
def stance_counter(mine, theirs):
    """Returns effects dict: 'pool_pen', 'degree_cap', 'no_breath', 'commit_punish', 'commit_bypass_cap'"""
    eff = {}
    # Pressure vs Patience: Patience cannot Take Breath this round
    if theirs == 'pressure' and mine == 'patience': eff['no_breath'] = True
    # Patience vs Decisive: Decisive loses 3D (overcommit punished)
    if mine == 'decisive' and theirs == 'patience': eff['pool_pen'] = 3
    # Cautious vs Pressure: Pressure capped at Partial Success degree (net <= 1)
    if mine == 'pressure' and theirs == 'cautious': eff['degree_cap'] = 1.0
    # Decisive vs Cautious: Decisive bypasses degree cap (commitment beats hedging)
    if mine == 'decisive' and theirs == 'cautious': eff['commit_bypass_cap'] = True
    # Pressure mirror: both lose 1 extra stamina (drain race)
    if mine == 'pressure' and theirs == 'pressure': eff['stam_pen'] = 1
    return eff

# === M3: Initiative preemption ===
# Higher Attunement (init proxy in Phase 10) may preempt for 2 Stamina.
# Effect: cancel opponent's action this round (no pool roll). Opp loses 3 stam penalty.
M3_PREEMPT_STAM_COST = 2  # [canonical: N/A - Phase 11 reform: M3 preempt stam cost]
M3_OPP_FRUSTRATION_STAM = 3  # [canonical: N/A - Phase 11 reform: M3 frustration penalty]
M3_PREEMPT_TRIGGER_HP_PCT = 0.6  # [canonical: N/A - Phase 11 AI heuristic]
M3_PREEMPT_MIN_INIT_GAP = 2  # [canonical: N/A - Phase 11 AI heuristic]

# === STR + stam (Phase 10 canonical) ===
def str_bonus_dice(strength): return strength // 3  # [canonical: N/A - Phase 10 reform STR strong]

def stamina_max(end): return end * 5  # [canonical: params/combat.md ED-694]
def stamina_recover(end): return end * 2  # [canonical: params/combat.md ED-694 - TB partial End*2]

def max_wounds(end): return min(end // 2 + 1, 3)  # [canonical: params/combat.md L138]
def wound_interval(end): return end + 6  # [canonical: derived_stats §4.1]
def max_health(end): return wound_interval(end) * (max_wounds(end) + 1)
def wound_net_penalty(wounds, end): return wounds * (1.0 / end)  # [canonical: N/A - Phase 10 reform 1/End Ob wound]

def stam_cost(action, wounds): return (TAKE_BREATH_COST if action in ('full_guard','take_breath','retrieve_weapon','close','open') else ACTION_COST) + wounds

def combat_pool(agi, hist): return max(COMBAT_POOL_FLOOR, agi + hist + 3)  # [canonical: N/A - Phase 10 reform undoubled pool]

def continuous_roll(n):
    if n <= 0: return 0.0
    return random.gauss(DIE_MEAN_TN7 * n, DIE_STD_TN7 * math.sqrt(n))

# === AI: stance choice ===
def choose_stance(state, opp_last_stance=None):
    """Heuristic stance selection."""
    hp_pct = state['own_hp_pct']
    stam = state['own_stam']
    own_pool = state['own_pool']
    opp_pool = state['opp_pool']
    own_reach = state['own_reach']
    opp_reach = state['opp_reach']
    distance = state['distance']
    in_range = distance <= own_reach
    opp_in_range = distance <= opp_reach
    pool_advantage = own_pool > opp_pool
    pool_deficit = own_pool < opp_pool - 1

    if not in_range and opp_in_range:  # they can hit me, I can't hit them — defensive
        return 'cautious'
    if pool_deficit and hp_pct < 0.6:  # losing — patience (recover) or cautious (cap their damage)
        return 'cautious' if stam < 8 else 'patience'
    if pool_advantage and hp_pct > 0.5:  # winning — pressure
        return 'pressure'
    if stam < 6: return 'patience'  # need breath
    if hp_pct < 0.3 and pool_advantage: return 'decisive'  # last gasp
    return random.choice(['pressure', 'patience'])  # default mid

# === AI: action choice (given stance) ===
def choose_action(state, my_stance):
    own_stam = state['own_stam']
    own_pool = state['own_pool']
    opp_pool = state['opp_pool']
    own_reach = state['own_reach']
    distance = state['distance']
    in_range = distance <= own_reach
    opp_disarmed = state.get('opp_disarmed', False)

    if own_stam < TAKE_BREATH_TRIGGER and not state.get('no_breath', False):
        return 'take_breath'
    if not in_range:  # need to close (or open if pool deficit and range advantage)
        return 'close'  # move toward opponent
    if opp_disarmed:
        return 'strike'  # exploit
    if my_stance == 'patience':
        return 'feint' if state.get('rd', 0) % 2 == 0 and own_pool < opp_pool else 'strike'
    if my_stance == 'decisive':
        return 'strike'
    if my_stance == 'cautious':
        return 'feint' if own_pool < opp_pool else 'strike'
    # pressure
    if own_pool < opp_pool and state.get('rd', 0) % 2 == 0:
        return 'feint'
    return 'strike'

# === Simulation ===
def simulate_duel(a, b, max_rounds=40):
    """One duel a vs b. Returns 'a', 'b', or 'draw'."""
    hp_a = a['max_hp']; hp_b = b['max_hp']
    wounds_a = 0; wounds_b = 0
    stam_a = stamina_max(a['end']); stam_b = stamina_max(b['end'])
    disarmed_a = False; disarmed_b = False
    distance = STARTING_DISTANCE  # M1: both start at mid range
    pending_a = 0; pending_b = 0  # PP-294 Feint pending pool reductions

    init_holder = 'a' if a['attn'] >= b['attn'] else 'b'
    last_stance_a = None; last_stance_b = None
    has_preempted_a = False; has_preempted_b = False  # one preempt per duel

    for rd in range(max_rounds):
        if stam_a <= 0 and stam_b <= 0: return 'draw'
        if stam_a <= 0: return 'b'
        if stam_b <= 0: return 'a'

        # Effective pool with PP-294 pending reductions
        eff_a = max(POOL_FLOOR, a['base_pool'] - pending_a); pending_a = 0
        eff_b = max(POOL_FLOOR, b['base_pool'] - pending_b); pending_b = 0

        # M2: Both declare stance simultaneously
        st_a_view = {'own_pool': eff_a, 'opp_pool': eff_b, 'own_hp_pct': hp_a/a['max_hp'],
                     'own_stam': stam_a, 'rd': rd, 'own_reach': a['weapon']['reach'],
                     'opp_reach': b['weapon']['reach'], 'distance': distance}
        st_b_view = {'own_pool': eff_b, 'opp_pool': eff_a, 'own_hp_pct': hp_b/b['max_hp'],
                     'own_stam': stam_b, 'rd': rd, 'own_reach': b['weapon']['reach'],
                     'opp_reach': a['weapon']['reach'], 'distance': distance}

        stance_a = choose_stance(st_a_view, last_stance_b)
        stance_b = choose_stance(st_b_view, last_stance_a)

        eff_a_counter = stance_counter(stance_a, stance_b)
        eff_b_counter = stance_counter(stance_b, stance_a)

        # Apply pool penalties from counter
        if 'pool_pen' in eff_a_counter:
            eff_a = max(POOL_FLOOR, eff_a - eff_a_counter['pool_pen'])
        if 'pool_pen' in eff_b_counter:
            eff_b = max(POOL_FLOOR, eff_b - eff_b_counter['pool_pen'])

        # Base off/def split per stance
        off_a_base, def_a_base = stance_split(stance_a, eff_a)
        off_b_base, def_b_base = stance_split(stance_b, eff_b)

        # M3: Init preemption decision (only Init holder can preempt)
        preempted = None
        if init_holder == 'a' and not has_preempted_a:
            # preempt if losing hp, init gap >= 2, can afford 2 stam
            if (hp_a / a['max_hp'] <= M3_PREEMPT_TRIGGER_HP_PCT
                and (a['attn'] - b['attn']) >= M3_PREEMPT_MIN_INIT_GAP
                and stam_a >= M3_PREEMPT_STAM_COST + 3):
                preempted = 'b'
                stam_a -= M3_PREEMPT_STAM_COST
                stam_b -= M3_OPP_FRUSTRATION_STAM
                has_preempted_a = True
        elif init_holder == 'b' and not has_preempted_b:
            if (hp_b / b['max_hp'] <= M3_PREEMPT_TRIGGER_HP_PCT
                and (b['attn'] - a['attn']) >= M3_PREEMPT_MIN_INIT_GAP
                and stam_b >= M3_PREEMPT_STAM_COST + 3):
                preempted = 'a'
                stam_b -= M3_PREEMPT_STAM_COST
                stam_a -= M3_OPP_FRUSTRATION_STAM
                has_preempted_b = True

        # Choose actions given stance + counter effects (pass no_breath if applicable)
        st_a_view['no_breath'] = eff_a_counter.get('no_breath', False)
        st_b_view['no_breath'] = eff_b_counter.get('no_breath', False)
        st_a_view['opp_disarmed'] = disarmed_b
        st_b_view['opp_disarmed'] = disarmed_a

        action_a = choose_action(st_a_view, stance_a) if preempted != 'a' else 'preempted'
        action_b = choose_action(st_b_view, stance_b) if preempted != 'b' else 'preempted'

        # M1: distance changes from close/open moves
        if action_a == 'close': distance = max(0, distance - 1)
        if action_b == 'close': distance = max(0, distance - 1)
        if action_a == 'open':  distance = min(3, distance + 1)
        if action_b == 'open':  distance = min(3, distance + 1)

        # Compute actual offense pools after disarmed override
        weapon_a = WEAPONS['unarmed'] if disarmed_a else a['weapon']
        weapon_b = WEAPONS['unarmed'] if disarmed_b else b['weapon']

        # M1: reach gate — if out of range, attack pool collapses to 1D + History
        a_attacks = action_a in ('strike', 'feint', 'disarm')
        b_attacks = action_b in ('strike', 'feint', 'disarm')
        a_in_range = distance <= weapon_a['reach']
        b_in_range = distance <= weapon_b['reach']

        off_a_use = off_a_base if a_in_range else (POOL_FLOOR + a['hist'])  # M1: 1D + Hist
        off_b_use = off_b_base if b_in_range else (POOL_FLOOR + b['hist'])

        # STR bonus dice (STR-strong; only on Strike/Disarm)
        str_a = str_bonus_dice(a['str']) if action_a in ('strike', 'disarm') else 0
        str_b = str_bonus_dice(b['str']) if action_b in ('strike', 'disarm') else 0

        # Wound penalty
        a_net_pen = wound_net_penalty(wounds_a, a['end'])
        b_net_pen = wound_net_penalty(wounds_b, b['end'])

        # Roll
        a_off_hits = continuous_roll(off_a_use + str_a) if a_attacks else 0
        b_def_hits = continuous_roll(def_b_base) if b_attacks else 0
        a_net = a_off_hits - b_def_hits - a_net_pen if a_attacks else 0

        b_off_hits = continuous_roll(off_b_use + str_b) if b_attacks else 0
        a_def_hits = continuous_roll(def_a_base) if a_attacks else 0
        b_net = b_off_hits - a_def_hits - b_net_pen if b_attacks else 0

        # M2: degree cap from counter
        if eff_a_counter.get('degree_cap') is not None and not eff_a_counter.get('commit_bypass_cap'):
            a_net = min(a_net, eff_a_counter['degree_cap'])
        if eff_b_counter.get('degree_cap') is not None and not eff_b_counter.get('commit_bypass_cap'):
            b_net = min(b_net, eff_b_counter['degree_cap'])

        # Damage application
        dmg_a, dmg_b = 0, 0
        if action_a == 'strike' and a_net > 0:
            mod = weapon_a['damage_mod']
            if a_net >= CRIT_MAGNITUDE: mod *= 2
            d = max(0, a_net + a['str'] * weapon_a['str_mult'] + mod)
            dmg_a = d; hp_b -= d
            wounds_b = min(int((b['max_hp'] - hp_b) // wound_interval(b['end'])), b['mw'] + 1)
        if action_b == 'strike' and b_net > 0:
            mod = weapon_b['damage_mod']
            if b_net >= CRIT_MAGNITUDE: mod *= 2
            d = max(0, b_net + b['str'] * weapon_b['str_mult'] + mod)
            dmg_b = d; hp_a -= d
            wounds_a = min(int((a['max_hp'] - hp_a) // wound_interval(a['end'])), a['mw'] + 1)
        if action_a == 'feint' and a_net > 0:
            pending_b = max(pending_b, int(a_net))
        if action_b == 'feint' and b_net > 0:
            pending_a = max(pending_a, int(b_net))
        if action_a == 'disarm' and a_net >= DISARM_NET_THRESHOLD: disarmed_b = True
        if action_b == 'disarm' and b_net >= DISARM_NET_THRESHOLD: disarmed_a = True
        if action_a == 'retrieve_weapon': disarmed_a = False
        if action_b == 'retrieve_weapon': disarmed_b = False

        # Stamina with M2 stam_pen and counter effects
        a_stam_extra = eff_a_counter.get('stam_pen', 0)
        b_stam_extra = eff_b_counter.get('stam_pen', 0)
        if action_a == 'take_breath':
            stam_a = min(stamina_max(a['end']), stam_a + stamina_recover(a['end']) - TAKE_BREATH_COST)
        elif action_a != 'preempted':
            stam_a -= (stam_cost(action_a, wounds_a) + a_stam_extra)
        if action_b == 'take_breath':
            stam_b = min(stamina_max(b['end']), stam_b + stamina_recover(b['end']) - TAKE_BREATH_COST)
        elif action_b != 'preempted':
            stam_b -= (stam_cost(action_b, wounds_b) + b_stam_extra)

        if dmg_a > dmg_b: init_holder = 'a'
        elif dmg_b > dmg_a: init_holder = 'b'

        last_stance_a = stance_a; last_stance_b = stance_b

        if hp_a <= 0 or wounds_a > a['mw']:
            if hp_b <= 0 or wounds_b > b['mw']: return 'draw'
            return 'b'
        if hp_b <= 0 or wounds_b > b['mw']: return 'a'

    return 'draw'

def build(name, agi, end, strength, weapon='light_blade', attn=None, hist=2):
    return {'name': name, 'agi': agi, 'end': end, 'str': strength,
            'attn': attn if attn is not None else agi,
            'weapon': WEAPONS[weapon], 'hist': hist,
            'base_pool': combat_pool(agi, hist),
            'wi': wound_interval(end), 'mw': max_wounds(end), 'max_hp': max_health(end)}

def run(a, b, n=3000):  # [canonical: N/A - Phase 11 trial count]
    wa = wb = dr = 0
    for _ in range(n):
        r = simulate_duel(a, b)
        if r == 'a': wa += 1
        elif r == 'b': wb += 1
        else: dr += 1
    decisive = wa + wb
    cond = (wa / decisive) if decisive > 0 else 0.5
    return wa/n, cond, dr/n

def main():
    random.seed(42)  # [canonical: N/A - deterministic seed for reproducibility]
    print("=" * 80)  # [canonical: N/A - display width]
    print("Phase 11 — C4 scene combat sim: M1 (reach gate) + M2 (stance) + M3 (preempt)")
    print("Baseline: undoubled pool + 1/End Ob + Disarm + canon stam + STR-strong")
    print("=" * 80)  # [canonical: N/A - display width]

    matchups = [
        ('Fast (Agi6 light) vs Strong (Agi3 light)',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Strong', 3, 4, 4, 'light_blade', attn=3)),
        ('Fast (Agi6 light) vs Tough (Agi3 End6 light)',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Tough', 3, 6, 4, 'light_blade', attn=3)),
        ('Fast (Agi6 light) vs Tough-heavy (Agi3 End6 STR6 heavy)',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Tough-h', 3, 6, 6, 'heavy_weapon', attn=3)),
        ('Fast (Agi6 light) vs Titan (Agi3 End6 STR7 heavy)',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Titan', 3, 6, 7, 'heavy_weapon', attn=3)),  # [canonical: N/A - Phase 10 archetype STR=7 max specialization]
        ('Fast (Agi6 light) vs Mighty-heavy (Agi3 End4 STR7 heavy)',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Mighty-h', 3, 4, 7, 'heavy_weapon', attn=3)),  # [canonical: N/A - Phase 10 archetype STR=7]
        ('Fast (Agi6 light) vs Mighty-light (Agi3 End4 STR7 light) [F3-gap test]',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Mighty-l', 3, 4, 7, 'light_blade', attn=3)),  # [canonical: N/A - Phase 10 archetype STR=7 F3 gap test]
        ('Fast (Agi6 light) vs Polearm (Agi3 End5 STR5 polearm) [reach-counter test]',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Polearm', 3, 5, 5, 'polearm', attn=3)),
        ('Fast (Agi6 light) vs Init-build (Agi3 End5 STR4 Att8 light) [M3 preempt test]',
            build('Fast', 6, 4, 4, 'light_blade', attn=5),
            build('Init-build', 3, 5, 4, 'light_blade', attn=8)),
        ('Balanced Fast-strong (Agi5 STR5 light) vs Fast (Agi6 light)',
            build('Balanced', 5, 4, 5, 'light_blade', attn=5),
            build('Fast', 6, 4, 4, 'light_blade', attn=5)),
        ('Calibration: Strong vs Strong (symmetric)',
            build('S1', 3, 4, 4, 'light_blade', attn=3),
            build('S2', 3, 4, 4, 'light_blade', attn=3)),
        ('Calibration: Fast vs Fast (symmetric)',
            build('F1', 6, 4, 4, 'light_blade', attn=5),
            build('F2', 6, 4, 4, 'light_blade', attn=5)),
    ]

    print(f"\n{'Matchup':<70} {'A win%':>8} {'A cond%':>8} {'Draw%':>8}")
    print("-" * 96)  # [canonical: N/A - display width]
    for label, a, b in matchups:
        wa, cond, dr = run(a, b)
        print(f"{label:<70} {wa*100:>7.1f}% {cond*100:>7.1f}% {dr*100:>7.1f}%")

if __name__ == '__main__':
    main()
