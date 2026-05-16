#!/usr/bin/env python3
# STR and Stamina reform sim
# Tests:
#   STR_MODE: 'none' (current), 'mild' (floor(STR/4) bonus dice), 'strong' (floor(STR/3)), 'pool_add' (floor(STR/2))
#   STAM_MODE: 'current' (15 + End*2), 'canon' (End*5, TB=End*2 partial restore, +1 stam cost per wound)

import random
import math

DIE_MEAN_TN7 = 0.4  # [canonical: params/core.md §Expected Value, TN 7 row, post-F13]
DIE_STD_TN7 = 0.8  # [canonical: params/core.md §Expected Value, TN 7 row, post-F13]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]
COMBAT_POOL_FLOOR = 5  # [canonical: params/combat.md L14]
FEINT_MIN_COMMIT = 3  # [canonical: params/combat.md PP-294]
DISARM_MIN_COMMIT = 3  # [canonical: N/A - Phase 10 proxy mechanic; combat_v30 Disarm full detail not extracted]
DISARM_NET_THRESHOLD = 2.0  # [canonical: N/A - Phase 10 proxy: net >=2 to disarm]
ACTION_COST = 5  # [canonical: params/combat.md L15]
TAKE_BREATH_COST = 3  # [canonical: params/combat.md L15 - defensive 3]
TAKE_BREATH_TRIGGER = 8  # [canonical: N/A - Phase 8 AI calibration]
CRIT_MAGNITUDE = 4.0  # [canonical: params/combat.md L91 - PP-717 D3]


def continuous_roll(n):
    if n <= 0: return 0.0
    return random.gauss(DIE_MEAN_TN7 * n, DIE_STD_TN7 * math.sqrt(n))


def combat_pool_undoubled(agi, hist):
    return max(COMBAT_POOL_FLOOR, agi + hist + 3)  # [canonical: N/A - Phase 10 reform: undoubled pool]


def str_bonus_dice(strength, mode):
    if mode == 'none': return 0
    elif mode == 'mild': return strength // 4  # [canonical: N/A - Phase 10 reform: STR mild]
    elif mode == 'strong': return strength // 3  # [canonical: N/A - Phase 10 reform: STR strong, recommended]
    elif mode == 'pool_add': return strength // 2  # [canonical: N/A - Phase 10 reform: STR pool_add]
    return 0


def stamina_max(end, mode):
    if mode == 'current': return 15 + end * 2  # [canonical: N/A - SIM ERROR, prior Phase 4-9 formula; corrected per ED-694]
    elif mode == 'canon': return end * 5  # canonical ED-694  # [canonical: params/combat.md ED-694 - Stamina = End * 5]
    return end * 5  # [canonical: params/combat.md ED-694 - Stamina = End * 5]


def stamina_recover(end, mode):
    if mode == 'current': return 20  # full restore proxy  # [canonical: N/A - SIM ERROR prior; canonical TB restore is partial End*2]
    elif mode == 'canon': return end * 2  # partial restore  # [canonical: params/combat.md Stamina section - TB restores End*2 partial]
    return end * 2  # [canonical: params/combat.md Stamina section - TB restores End*2 partial]


def max_wounds(end): return min(end // 2 + 1, 3)  # [canonical: params/combat.md L138]
def wound_interval(end): return end + 6  # [canonical: derived_stats §4.1]
def max_health(end): return wound_interval(end) * (max_wounds(end) + 1)  # [canonical: derived_stats §4.1 max_health]


WEAPONS = {
    'light_blade': {'damage_mod': 3, 'str_mult': 1.0},  # [canonical: params/combat.md damage table - Light Blade]
    'heavy_weapon': {'damage_mod': 5, 'str_mult': 2.0},  # [canonical: params/combat.md damage table - Heavy class x2]
    'unarmed': {'damage_mod': 0, 'str_mult': 0.5},  # [canonical: N/A - Phase 10 proxy: disarmed damage output]
}


def wound_net_penalty(wounds, end):
    return wounds * (1.0 / end)  # [canonical: N/A - Phase 10 reform: 1/End Ob wound]


def stam_cost(action, wounds, stam_mode):
    base = TAKE_BREATH_COST if action in ('full_guard', 'take_breath', 'retrieve_weapon') else ACTION_COST
    if stam_mode == 'canon':
        return base + wounds  # +1 stam cost per wound  # [canonical: params/combat.md ED-694 - +1 stam cost per wound]
    return base


def choose_action(state):
    own_pool = state['own_pool']
    opp_pool = state['opp_pool']
    own_stam = state['own_stam']
    own_wounds = state['own_wounds']
    own_mw = state['own_max_wounds']
    own_hp_pct = state['own_hp_pct']
    opp_weapon_mod = state['opp_weapon_mod']
    opp_disarmed = state['opp_disarmed']

    if TAKE_BREATH_COST <= own_stam <= TAKE_BREATH_TRIGGER:
        return 'take_breath'
    if own_hp_pct < 0.15 and own_wounds >= own_mw:  # [canonical: N/A - Phase 8 last-stand AI heuristic]
        return 'full_guard'

    pool_gap = opp_pool - own_pool
    # Disarm: vs ANY armed opponent when disadvantaged (fixed AI bug)
    if (pool_gap >= 2 and opp_weapon_mod >= 3 and not opp_disarmed
        and own_pool >= DISARM_MIN_COMMIT + 2 and state['rd'] % 4 == 1):  # [canonical: N/A - Phase 10 AI: Disarm cadence]
        return 'disarm'
    if pool_gap >= 2 and own_pool >= FEINT_MIN_COMMIT + 2 and state['rd'] % 2 == 0:  # [canonical: N/A - Phase 8 AI: Feint alternation PP-294]
        return 'feint'
    return 'strike'


def choose_action_disarmed(state):
    return 'retrieve_weapon'


def default_split(action, pool):
    if action == 'strike': return pool/2, pool/2
    elif action in ('feint', 'disarm'):
        c = max(FEINT_MIN_COMMIT, int(pool * 0.6))  # [canonical: N/A - AI commit fraction for Feint/Disarm]
        return c, max(POOL_FLOOR, pool - c)
    return 0, pool


def reactive_split(own_action, own_pool, opp_action, opp_off, opp_def):
    opp_total = opp_off + opp_def
    if opp_total <= 0: return default_split(own_action, own_pool)
    opp_off_frac = opp_off / opp_total
    if own_action == 'strike':
        if opp_action in ('feint', 'disarm'): return 0.2*own_pool, 0.8*own_pool  # [canonical: N/A - reactive: heavy def vs Feint/Disarm]
        elif opp_off_frac > 0.6: return 0.3*own_pool, 0.7*own_pool  # [canonical: N/A - reactive: moderate def vs off-heavy]
        elif opp_off_frac < 0.4: return 0.7*own_pool, 0.3*own_pool  # [canonical: N/A - reactive: off-heavy vs def-heavy opp]
        else: return 0.5*own_pool, 0.5*own_pool  # [canonical: N/A - reactive: balanced]
    return default_split(own_action, own_pool)


def simulate_duel(a, b, str_mode, stam_mode, max_rounds=40):  # [canonical: N/A - sim termination ceiling]
    hp_a, hp_b = a['max_hp'], b['max_hp']
    stam_a, stam_b = stamina_max(a['end'], stam_mode), stamina_max(b['end'], stam_mode)
    wounds_a, wounds_b = 0, 0
    wi_a, wi_b = a['wi'], b['wi']
    pending_a, pending_b = 0, 0
    disarmed_a, disarmed_b = False, False

    if a['attn'] > b['attn']: init_holder = 'a'
    elif b['attn'] > a['attn']: init_holder = 'b'
    else: init_holder = 'a' if a['agi'] >= b['agi'] else 'b'

    for rd in range(max_rounds):
        if stam_a < TAKE_BREATH_COST and stam_b < TAKE_BREATH_COST: return 'draw'
        if stam_a < TAKE_BREATH_COST: return 'b'
        if stam_b < TAKE_BREATH_COST: return 'a'

        eff_a = max(POOL_FLOOR, a['base_pool'] - pending_a)
        eff_b = max(POOL_FLOOR, b['base_pool'] - pending_b)
        pending_a, pending_b = 0, 0
        a_net_pen = wound_net_penalty(wounds_a, a['end'])
        b_net_pen = wound_net_penalty(wounds_b, b['end'])

        weapon_a = WEAPONS['unarmed'] if disarmed_a else a['weapon']
        weapon_b = WEAPONS['unarmed'] if disarmed_b else b['weapon']

        st_a = {'own_pool': eff_a, 'opp_pool': eff_b, 'own_hp_pct': hp_a/a['max_hp'],
                'own_stam': stam_a, 'rd': rd, 'own_wounds': wounds_a, 'own_max_wounds': a['mw'],
                'opp_weapon_mod': weapon_b['damage_mod'], 'opp_disarmed': disarmed_b}
        st_b = {'own_pool': eff_b, 'opp_pool': eff_a, 'own_hp_pct': hp_b/b['max_hp'],
                'own_stam': stam_b, 'rd': rd, 'own_wounds': wounds_b, 'own_max_wounds': b['mw'],
                'opp_weapon_mod': weapon_a['damage_mod'], 'opp_disarmed': disarmed_a}

        action_a_fn = choose_action_disarmed if disarmed_a else choose_action
        action_b_fn = choose_action_disarmed if disarmed_b else choose_action

        if init_holder == 'a':
            action_b = action_b_fn(st_b)
            off_b, def_b = default_split(action_b, eff_b)
            action_a = action_a_fn(st_a)
            off_a, def_a = reactive_split(action_a, eff_a, action_b, off_b, def_b)
        else:
            action_a = action_a_fn(st_a)
            off_a, def_a = default_split(action_a, eff_a)
            action_b = action_b_fn(st_b)
            off_b, def_b = reactive_split(action_b, eff_b, action_a, off_a, def_a)

        # STR bonus dice on Strike/Disarm (not Feint — that's about deception)
        str_bonus_a = str_bonus_dice(a['str'], str_mode) if action_a in ('strike', 'disarm') else 0
        str_bonus_b = str_bonus_dice(b['str'], str_mode) if action_b in ('strike', 'disarm') else 0

        a_off_hits = continuous_roll(off_a + str_bonus_a) if action_a in ('strike', 'feint', 'disarm') else 0
        b_def_hits = continuous_roll(def_b)
        a_net = a_off_hits - b_def_hits - a_net_pen if action_a in ('strike', 'feint', 'disarm') else 0

        b_off_hits = continuous_roll(off_b + str_bonus_b) if action_b in ('strike', 'feint', 'disarm') else 0
        a_def_hits = continuous_roll(def_a)
        b_net = b_off_hits - a_def_hits - b_net_pen if action_b in ('strike', 'feint', 'disarm') else 0

        dmg_a, dmg_b = 0, 0
        if action_a == 'strike' and a_net > 0:
            mod = weapon_a['damage_mod']
            if a_net >= CRIT_MAGNITUDE: mod *= 2
            d = max(0, a_net + a['str'] * weapon_a['str_mult'] + mod)
            dmg_a = d; hp_b -= d
            wounds_b = min(int((b['max_hp'] - hp_b) // wi_b), b['mw'] + 1)
        if action_b == 'strike' and b_net > 0:
            mod = weapon_b['damage_mod']
            if b_net >= CRIT_MAGNITUDE: mod *= 2
            d = max(0, b_net + b['str'] * weapon_b['str_mult'] + mod)
            dmg_b = d; hp_a -= d
            wounds_a = min(int((a['max_hp'] - hp_a) // wi_a), a['mw'] + 1)
        if action_a == 'feint' and a_net > 0:
            pending_b = max(pending_b, int(a_net))
        if action_b == 'feint' and b_net > 0:
            pending_a = max(pending_a, int(b_net))
        if action_a == 'disarm' and a_net >= DISARM_NET_THRESHOLD:
            disarmed_b = True
        if action_b == 'disarm' and b_net >= DISARM_NET_THRESHOLD:
            disarmed_a = True
        if action_a == 'retrieve_weapon': disarmed_a = False
        if action_b == 'retrieve_weapon': disarmed_b = False

        # Stamina with mode-dependent cost
        if action_a == 'take_breath':
            stam_a = min(stamina_max(a['end'], stam_mode), stam_a + stamina_recover(a['end'], stam_mode) - TAKE_BREATH_COST)
        else:
            stam_a -= stam_cost(action_a, wounds_a, stam_mode)
        if action_b == 'take_breath':
            stam_b = min(stamina_max(b['end'], stam_mode), stam_b + stamina_recover(b['end'], stam_mode) - TAKE_BREATH_COST)
        else:
            stam_b -= stam_cost(action_b, wounds_b, stam_mode)

        if dmg_a > dmg_b: init_holder = 'a'
        elif dmg_b > dmg_a: init_holder = 'b'

        if hp_a <= 0 or wounds_a > a['mw']:
            if hp_b <= 0 or wounds_b > b['mw']: return 'draw'
            return 'b'
        if hp_b <= 0 or wounds_b > b['mw']: return 'a'

    return 'draw'


def build(name, agi, end, strength, weapon='light_blade', attn=None, hist=2):
    return {'name': name, 'agi': agi, 'end': end, 'str': strength, 'attn': attn if attn is not None else agi,
            'weapon': WEAPONS[weapon], 'hist': hist,
            'base_pool': combat_pool_undoubled(agi, hist),
            'wi': wound_interval(end), 'mw': max_wounds(end), 'max_hp': max_health(end)}


def run(a, b, str_mode, stam_mode, n=3000):  # [canonical: N/A - Phase 10 trial count]
    wa = wb = dr = 0
    for _ in range(n):
        r = simulate_duel(a, b, str_mode, stam_mode)
        if r == 'a': wa += 1
        elif r == 'b': wb += 1
        else: dr += 1
    decisive = wa + wb
    cond = (wa / decisive) if decisive > 0 else 0.5
    return wa/n, cond, dr/n


def main():
    random.seed(42)  # [canonical: N/A - deterministic seed for reproducibility]
    print("=" * 100)
    print("STR + Stamina reform sim")
    print("=" * 100)
    print()
    print("Builds (Agi + Hist + 3 pool, undoubled):")

    fast = build('Fast (Agi 6, End 4, STR 4, light)', 6, 4, 4, 'light_blade', attn=3)  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    strong = build('Strong (Agi 3, End 4, STR 4, light)', 3, 4, 4, 'light_blade', attn=3)  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    mighty = build('Mighty (Agi 3, End 4, STR 7, light)', 3, 4, 7, 'light_blade', attn=3)  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    mighty_heavy = build('Mighty-heavy (Agi 3, End 4, STR 7, heavy)', 3, 4, 7, 'heavy_weapon', attn=3)  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    tough = build('Tough (Agi 3, End 6, STR 4, light)', 3, 6, 4, 'light_blade', attn=3)  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    tough_heavy = build('Tough-heavy (Agi 3, End 6, STR 6, heavy)', 3, 6, 6, 'heavy_weapon', attn=3)  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    titan = build('Titan (Agi 3, End 6, STR 7, heavy)', 3, 6, 7, 'heavy_weapon', attn=3)  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    fast_strong = build('Fast-strong (Agi 5, End 4, STR 5, light)', 5, 4, 5, 'light_blade', attn=3)  # balanced build  # [canonical: N/A - Phase 10 test build, attributes per build matrix]

    print(f"  {'Build':45} {'pool':>5} {'HP':>4} {'stam(End*5)':>12} {'STR bonus(strong)':>18}")
    for b in [fast, strong, mighty, mighty_heavy, tough, tough_heavy, titan, fast_strong]:
        stam_canon = b['end'] * 5
        str_bonus = b['str'] // 3
        print(f"  {b['name']:45} {b['base_pool']:>4}D {b['max_hp']:>4} {stam_canon:>11} {str_bonus:>+15} dice")
    print()

    # Run a comparison matrix
    configs = [
        ('Baseline (corrected): STR=none, stam=current', 'none', 'current'),
        ('+ Canonical stam (End×5, partial TB recovery, +1/wound)', 'none', 'canon'),
        ('+ STR mild (floor(STR/4) bonus dice)', 'mild', 'canon'),
        ('+ STR strong (floor(STR/3) bonus dice)', 'strong', 'canon'),
        ('+ STR pool_add (floor(STR/2) bonus dice)', 'pool_add', 'canon'),
    ]

    matchups = [
        ('Fast vs Strong', fast, strong),
        ('Fast vs Mighty', fast, mighty),
        ('Fast vs Mighty-heavy', fast, mighty_heavy),
        ('Fast vs Tough', fast, tough),
        ('Fast vs Tough-heavy', fast, tough_heavy),
        ('Fast vs Titan', fast, titan),
        ('Fast vs Fast-strong (balanced)', fast, fast_strong),
        ('Mighty-heavy vs Titan (STR vs End)', mighty_heavy, titan),
        ('Sym: Strong vs Strong', strong, build('S2', 3, 4, 4, 'light_blade', attn=3)),  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
        ('Sym: Fast vs Fast', fast, build('F2', 6, 4, 4, 'light_blade', attn=3)),  # [canonical: N/A - Phase 10 test build, attributes per build matrix]
    ]

    # Print header
    print(f"  {'Matchup':40}", end='')
    for cfg_label, _, _ in configs:
        short = cfg_label.split(':')[0][:6] if ':' in cfg_label else cfg_label[:6]  # [canonical: N/A - display label truncation, not mechanical]
        if 'baseline' in cfg_label.lower(): short = 'BASE'
        elif 'canonical stam' in cfg_label.lower(): short = '+stam'
        elif 'mild' in cfg_label.lower(): short = '+mild'
        elif 'strong' in cfg_label.lower() and 'STR' in cfg_label: short = '+str'
        elif 'pool_add' in cfg_label.lower(): short = '+pool'
        print(f" {short:>7}", end='')
    print()
    print(f"  {'-'*40}", end='')
    for _ in configs:
        print(f" {'-'*7}", end='')
    print()

    for label, a, b in matchups:
        # A is first-listed; first row is A cond win rate
        print(f"  {label:40}", end='')
        for cfg_label, sm, stm in configs:
            wa, cond, dr = run(a, b, sm, stm)
            print(f" {cond:>6.1%} ", end='')
        print()
    print()

    # Detailed table for the best-looking config
    print("=" * 100)
    print("DETAILED RUN — best config: canonical stam + STR-strong (floor(STR/3) bonus dice)")
    print("=" * 100)
    print(f"  {'Matchup':40} {'A win%':>8} {'A cond':>8} {'Draws':>8}")
    print(f"  {'-'*40} {'-'*8} {'-'*8} {'-'*8}")
    for label, a, b in matchups:
        wa, cond, dr = run(a, b, 'strong', 'canon')
        print(f"  {label:40} {wa:>7.1%} {cond:>7.1%} {dr:>7.1%}")


if __name__ == '__main__':
    main()
