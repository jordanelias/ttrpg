#!/usr/bin/env python3
# Phase 12 — Mass battle archetype test (Reframing 2 verification)
# Question: does heavy/Strong/Tough archetype dominate at mass scale?
# Canonical engine: params/mass_combat.md Core Formula (PP-233).
#   Pool = min(Size, Command) + Command  # [canonical: params/mass_combat.md §Core Formula PP-233]
#   H = min(Discipline, Command) + DR  # [canonical: params/mass_combat.md §Core Formula]
#   Damage = successes * (1 + Power)  # [canonical: params/mass_combat.md §Core Formula]
#   Size after = floor(remaining_health / H)  # [canonical: params/mass_combat.md §Core Formula]

import random, math

DIE_MEAN_TN7 = 0.4  # [canonical: params/core.md §Expected Value TN 7]
DIE_STD_TN7 = 0.8  # [canonical: params/core.md §Expected Value TN 7]
POOL_FLOOR = 1  # [canonical: params/core.md L185-187]

# DR table from params/mass_combat.md §DR Table — Mass Combat (melee).
# Row = armour, col = weapon (LC/HC/LB/HB).
# [canonical: params/mass_combat.md §DR Table — Mass Combat PP-104]
DR_TABLE = {
    'none':   {'LC': 0, 'HC': 0, 'LB': 0, 'HB': 0},
    'light':  {'LC': 2, 'HC': 1, 'LB': 1, 'HB': 0},
    'medium': {'LC': 4, 'HC': 3, 'LB': 2, 'HB': 1},
    'heavy':  {'LC': 6, 'HC': 5, 'LB': 3, 'HB': 1},
}

# Weapon effectiveness — whether attacker can damage at all.
# [canonical: params/mass_combat.md §Weapon Effectiveness combined]
# True = can deal damage, False = no effect.
WEAPON_EFFECTIVE = {
    'LC': {'none': True,  'light': False, 'medium': False, 'heavy': False},
    'HC': {'none': True,  'light': True,  'medium': True,  'heavy': False},
    'LB': {'none': True,  'light': False, 'medium': False, 'heavy': False},
    'HB': {'none': True,  'light': True,  'medium': True,  'heavy': True},
}

def continuous_roll(n):
    if n <= 0: return 0.0
    return random.gauss(DIE_MEAN_TN7 * n, DIE_STD_TN7 * math.sqrt(n))

def make_unit(name, size, command, discipline, power, weapon, armour, dmg_mod):
    dr = DR_TABLE[armour][weapon]  # [canonical: params/mass_combat.md DR table lookup]
    h = min(discipline, command) + 2  # H per Size — baseline +2 per worked example  [canonical: params/mass_combat.md §Core Formula worked example DR baseline 2]
    return {
        'name': name, 'size': size, 'command': command,
        'discipline': discipline, 'power': power, 'weapon': weapon,
        'armour': armour, 'dmg_mod': dmg_mod, 'dr': dr, 'h': h,
        'total_health': size * h,
        'current_health': size * h,
    }

def round_pool(unit):
    return max(POOL_FLOOR, min(unit['size'], unit['command']) + unit['command'])

def simulate_battle(a, b, max_rounds=40):  # [canonical: N/A - Phase 12 sim limit]
    """One Phase 5 engagement. Returns 'a', 'b', or 'draw'."""
    # Pool split default: 1/2 to offence, remainder to defence (PP-104 default)
    # [canonical: params/mass_combat.md §Pool Split Phase 5 default ½ offence rounded down]
    a = dict(a); b = dict(b)
    for rd in range(max_rounds):
        if a['size'] <= 0 and b['size'] <= 0: return 'draw'
        if a['size'] <= 0: return 'b'
        if b['size'] <= 0: return 'a'

        pool_a = round_pool(a)
        pool_b = round_pool(b)
        off_a = pool_a // 2  # [canonical: params/mass_combat.md default ½ pool to offence rounded down]
        def_a = pool_a - off_a
        off_b = pool_b // 2  # [canonical: params/mass_combat.md default ½ pool to offence rounded down]
        def_b = pool_b - off_b

        # Roll
        a_off = continuous_roll(off_a)
        b_def = continuous_roll(def_b)
        b_off = continuous_roll(off_b)
        a_def = continuous_roll(def_a)

        a_net = max(0, a_off - b_def)  # net hits to apply to b
        b_net = max(0, b_off - a_def)

        # Damage if attacker's weapon effective vs defender's armour
        # Size loss = max(0, net + dmg_mod - DR)  # [canonical: params/mass_combat.md §Damage Formula PARAMS-GAP-05]
        a_can_hit = WEAPON_EFFECTIVE[a['weapon']][b['armour']]
        b_can_hit = WEAPON_EFFECTIVE[b['weapon']][a['armour']]

        # Canon: Damage = successes × (1 + Power)  [params/mass_combat.md §Core Formula PP-233]
        # DR mitigates net hits before damage multiplication (per worked-example logic).
        # WEAPON_EFFECTIVE gate is binary; if False, damage = 0.  [params/mass_combat.md §Weapon Effectiveness]
        # DR lookup uses attacker-weapon vs defender-armour table.  [params/mass_combat.md §DR Table]
        damage_to_b = 0
        damage_to_a = 0
        if a_can_hit:
            dr_a_vs_b = DR_TABLE[b['armour']][a['weapon']]  # [canonical: DR table lookup]
            mitigated = max(0, a_net - dr_a_vs_b)
            damage_to_b = mitigated * (1 + a['power'])
        if b_can_hit:
            dr_b_vs_a = DR_TABLE[a['armour']][b['weapon']]  # [canonical: DR table lookup]
            mitigated = max(0, b_net - dr_b_vs_a)
            damage_to_a = mitigated * (1 + b['power'])

        # Simultaneous resolution  # [canonical: params/mass_combat.md §Key rules]
        a['current_health'] = max(0, a['current_health'] - damage_to_a)
        b['current_health'] = max(0, b['current_health'] - damage_to_b)
        a['size'] = a['current_health'] // a['h']
        b['size'] = b['current_health'] // b['h']

    # Both still standing — judge by remaining health
    if a['current_health'] > b['current_health'] * 1.2: return 'a'
    if b['current_health'] > a['current_health'] * 1.2: return 'b'
    return 'draw'

def run(a_proto, b_proto, n=2000):  # [canonical: N/A - Phase 12 trial count]
    wa = wb = dr = 0
    for _ in range(n):
        a = make_unit(**a_proto)
        b = make_unit(**b_proto)
        r = simulate_battle(a, b)
        if r == 'a': wa += 1
        elif r == 'b': wb += 1
        else: dr += 1
    decisive = wa + wb
    cond = (wa / decisive) if decisive > 0 else 0.5
    return wa/n, cond, dr/n

# Archetype prototypes mapped from personal-scale equivalents
# Size 5, Command 5, Discipline 5 = baseline 'Professional' unit per Power Tier table
# [canonical: params/mass_combat.md §Power Tier Reference & §Unit Stats]
LIGHT_INF    = {'name': 'LightInf',   'size': 5, 'command': 5, 'discipline': 4, 'power': 2, 'weapon': 'LC', 'armour': 'light',  'dmg_mod': 2}  # [canonical: params/mass_combat.md Power 2 Militia tier; LightCut LightArmor LI Dmg Mod +2]
HEAVY_INF    = {'name': 'HeavyInf',   'size': 5, 'command': 5, 'discipline': 5, 'power': 3, 'weapon': 'HC', 'armour': 'heavy',  'dmg_mod': 4}  # [canonical: params/mass_combat.md Power 3 Professional; HeavyCut Heavy armour HI Dmg Mod +4]
VETERAN_HI   = {'name': 'VetHeavy',   'size': 5, 'command': 5, 'discipline': 6, 'power': 4, 'weapon': 'HC', 'armour': 'heavy',  'dmg_mod': 4}  # [canonical: params/mass_combat.md Power 4 Veteran tier; same kit as HI]
LEVY         = {'name': 'Levy',       'size': 5, 'command': 5, 'discipline': 2, 'power': 1, 'weapon': 'LC', 'armour': 'none',   'dmg_mod': 1}  # [canonical: params/mass_combat.md Power 1 Levy tier; LightCut no armour Levy Dmg Mod +1]
KNIGHTS_T    = {'name': 'KnightsT',   'size': 4, 'command': 5, 'discipline': 6, 'power': 5, 'weapon': 'HB', 'armour': 'heavy',  'dmg_mod': 5}  # [canonical: params/mass_combat.md Power 5 Elite; HeavyBlunt Knights Templar Dmg Mod +5]
LIGHT_CAV    = {'name': 'LightCav',   'size': 4, 'command': 5, 'discipline': 4, 'power': 3, 'weapon': 'LC', 'armour': 'light',  'dmg_mod': 2}  # [canonical: params/mass_combat.md Cavalry-class proxy LightCut Light armor]
HEAVY_CAV    = {'name': 'HeavyCav',   'size': 4, 'command': 5, 'discipline': 5, 'power': 4, 'weapon': 'HC', 'armour': 'heavy',  'dmg_mod': 5}  # [canonical: params/mass_combat.md Cavalry Power 4 Veteran HeavyCut Heavy armor Dmg Mod +5]

def main():
    random.seed(42)  # [canonical: N/A - deterministic seed]
    print("=" * 88)  # [canonical: N/A - display width]
    print("Phase 12 — Mass-battle archetype test (Reframing 2 verification)")
    print("Canonical engine: params/mass_combat.md Core Formula (PP-233)")
    print("=" * 88)  # [canonical: N/A - display width]

    matchups = [
        ('Calibration: HeavyInf vs HeavyInf (symmetric)',          HEAVY_INF, HEAVY_INF),
        ('Calibration: LightInf vs LightInf (symmetric)',          LIGHT_INF, LIGHT_INF),
        ('LightInf vs HeavyInf [Fast-light vs Strong-heavy]',       LIGHT_INF, HEAVY_INF),
        ('LightInf vs VetHeavy [Fast-light vs Tough]',              LIGHT_INF, VETERAN_HI),
        ('LightInf vs KnightsT [Fast-light vs Anti-armor Elite]',   LIGHT_INF, KNIGHTS_T),
        ('LightInf vs Levy [Light vs lower-tier]',                  LIGHT_INF, LEVY),
        ('LightCav vs HeavyInf [mobile-light vs Strong]',           LIGHT_CAV, HEAVY_INF),
        ('LightCav vs VetHeavy',                                    LIGHT_CAV, VETERAN_HI),
        ('HeavyCav vs HeavyInf [Strong-heavy parity]',              HEAVY_CAV, HEAVY_INF),
        ('HeavyInf vs VetHeavy [Strong vs Tough]',                  HEAVY_INF, VETERAN_HI),
        ('HeavyInf vs Levy',                                        HEAVY_INF, LEVY),
        ('KnightsT vs HeavyCav [Elite Anti-armor vs Heavy Cav]',    KNIGHTS_T, HEAVY_CAV),
        ('VetHeavy vs Levy [Tough vs Weak — magnitude floor]',      VETERAN_HI, LEVY),
        ('Levy vs Levy [symmetric, weapon penetrates]',             LEVY, LEVY),
        ('LightInf vs Levy [weapon penetrates, Power diff]',         LIGHT_INF, LEVY),
        ('LightCav vs LightInf [LC vs Light armour: NO damage]',     LIGHT_CAV, LIGHT_INF),
    ]

    print(f"\n{'Matchup':<62} {'A win%':>8} {'A cond%':>8} {'Draw%':>8}")
    print("-" * 88)  # [canonical: N/A - display width]
    for label, a, b in matchups:
        wa, cond, draw = run(a, b)
        print(f"{label:<62} {wa*100:>7.1f}% {cond*100:>7.1f}% {draw*100:>7.1f}%")

if __name__ == '__main__':
    main()
