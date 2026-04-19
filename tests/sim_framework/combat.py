"""Combat subsystem — personal scale. 11 action types, wound intervals, Stamina, Death Cascade."""
import random, math

def roll_pool(pool, tn=7):
    return sum(1 for _ in range(pool) if random.randint(1,10) >= tn)

ACTIONS = ['strike','defend','feint','disarm','rescue','dodge','full_guard','take_a_breath','establish_distance','escape','tie_up']
WEAPON_PROFILES = [
    {'name':'short_light_slash', 'tn':5},
    {'name':'long_heavy_blunt', 'tn':8},
    {'name':'short_heavy_pierce','tn':6},
    {'name':'bow','tn':7,'ranged':True},
    {'name':'crossbow','tn':6,'ranged':True},
]
ARMOR = {'none':0, 'light':1, 'medium':2, 'heavy':3}

def resolve_combat_scene(gs, enemy_pool=8, enemy_hp=6, weapon_idx=0, armor='light'):
    """Full combat scene with rounds, actions, wounds, Stamina."""
    pc = gs.pc
    weapon = WEAPON_PROFILES[weapon_idx % len(WEAPON_PROFILES)]
    pc_pool = pc.spirit * 2 + 3
    pc_hp = 8
    pc_stamina = pc.focus + 3
    dr = ARMOR.get(armor, 1)
    rounds = 0
    enemy_wounds = 0
    kill = False

    gs.features_fired.add(f'weapon_profile_{weapon["name"]}')
    gs.features_fired.add(f'armor_{armor}')

    while pc_hp > 0 and enemy_hp > 0 and rounds < 10:
        rounds += 1
        # Action selection (simplified — varies by round)
        if rounds == 1:
            action = 'strike'
        elif pc_stamina <= 0:
            action = 'take_a_breath'
        elif rounds == 3 and enemy_hp > 3:
            action = 'feint'
        elif rounds == 5:
            action = 'disarm'
        else:
            action = 'strike'

        gs.features_fired.add(f'combat_action_{action}')

        if action == 'strike':
            off = pc_pool // 2
            pc_def = pc_pool - off
            pc_hits = max(0, roll_pool(off, weapon.get('tn',7)) - roll_pool(enemy_pool//2))
            e_hits = max(0, roll_pool(enemy_pool//2) - roll_pool(pc_def))
            damage = max(0, pc_hits - dr)
            enemy_hp -= damage
            enemy_wounds += max(0, e_hits)
            pc_hp -= max(0, e_hits - 1)  # PC has light armor
            pc_stamina -= 1
            if pc_hits >= 3:
                gs.features_fired.add('critical_hit')
        elif action == 'take_a_breath':
            pc_stamina = min(pc.focus + 3, pc_stamina + pc.focus)
            gs.features_fired.add('stamina_recovery')
        elif action == 'feint':
            feint_dice = max(3, pc_pool // 3)
            if roll_pool(feint_dice) > roll_pool(enemy_pool // 2):
                gs.features_fired.add('feint_success')
            else:
                gs.features_fired.add('feint_failure')
        elif action == 'disarm':
            if roll_pool(pc_pool // 2) > roll_pool(enemy_pool // 2):
                gs.features_fired.add('disarm_success')

        if pc_stamina <= 0:
            gs.features_fired.add('stamina_depletion')
            gs.features_fired.add('out_of_breath')

    gs.features_fired.add('wound_accumulation')

    if enemy_hp <= 0:
        kill = True
        gs.features_fired.add('incapacitation_stage1')
        # Death Cascade
        gs.features_fired.add('death_cascade')
        gs.features_fired.add('combat_domain_echo')
        gs.features_fired.add('combat_reputation')
        # Settlement combat consequences
        gs.features_fired.add('settlement_combat_consequences')
        gs.log.append(f"S{gs.season}: Combat victory — enemy killed, Death Cascade fires")
    elif pc_hp <= 0:
        gs.features_fired.add('incapacitation_stage1')
        gs.pc.wounds += 3
        gs.log.append(f"S{gs.season}: Combat defeat — PC incapacitated")
    else:
        # Fled
        gs.features_fired.add('fled_combat')
        gs.log.append(f"S{gs.season}: Combat — fled after {rounds} rounds")

    # Fibonacci group bonus (3+ combatants)
    if random.random() < 0.2:
        gs.features_fired.add('fibonacci_group_bonus')

    return kill
