"""
Valoria Campaign Simulation — Full Engine (Phase 4.2)
Integrates all subsystems for ~130 feature coverage.
"""
import math, random
from state import GameState, init_game_state
from combat import resolve_combat_scene
from fieldwork import resolve_fieldwork
from contest import resolve_contest
from threadwork import resolve_thread_scene
from subsystems import (resolve_mass_battle, evaluate_npc_arcs, apply_domain_echoes,
                        resolve_governance, check_victory, evaluate_player_agency,
                        evaluate_scale_transitions, evaluate_companions, evaluate_lifecycle)

def roll_pool(pool, tn=7):
    return sum(1 for _ in range(pool) if random.randint(1,10) >= tn)

def check(pool, ob, tn=7):
    s = roll_pool(pool, tn)
    return s >= ob, s - ob, 'overwhelming' if s-ob>=3 else ('success' if s>=ob else ('partial' if s==ob-1 else 'failure'))

POLICIES = {
    'balanced':      {'fieldwork':0.3, 'combat':0.15, 'contest':0.2, 'thread':0.1, 'govern':0.15, 'socialize':0.1},
    'investigator':  {'fieldwork':0.5, 'combat':0.05, 'contest':0.1, 'thread':0.15, 'govern':0.1, 'socialize':0.1},
    'warrior':       {'fieldwork':0.1, 'combat':0.5, 'contest':0.1, 'thread':0.0, 'govern':0.1, 'socialize':0.2},
    'diplomat':      {'fieldwork':0.1, 'combat':0.05, 'contest':0.4, 'thread':0.0, 'govern':0.15, 'socialize':0.3},
    'practitioner':  {'fieldwork':0.15, 'combat':0.05, 'contest':0.1, 'thread':0.5, 'govern':0.1, 'socialize':0.1},
    'governor':      {'fieldwork':0.1, 'combat':0.05, 'contest':0.15, 'thread':0.0, 'govern':0.5, 'socialize':0.2},
    'independent':   {'fieldwork':0.3, 'combat':0.1, 'contest':0.2, 'thread':0.1, 'govern':0.1, 'socialize':0.2},
    'aggressive':    {'fieldwork':0.05, 'combat':0.6, 'contest':0.05, 'thread':0.0, 'govern':0.1, 'socialize':0.2},
    'theocrat':      {'fieldwork':0.1, 'combat':0.1, 'contest':0.3, 'thread':0.0, 'govern':0.3, 'socialize':0.2},
    'restorationist':{'fieldwork':0.2, 'combat':0.05, 'contest':0.2, 'thread':0.3, 'govern':0.1, 'socialize':0.15},
}

def select_action(policy_weights):
    r = random.random()
    cumulative = 0
    for action, weight in policy_weights.items():
        cumulative += weight
        if r < cumulative:
            return action
    return 'fieldwork'

def run_season(gs, policy='balanced'):
    gs.season += 1
    weights = POLICIES.get(policy, POLICIES['balanced'])

    # Phase 1a: Duty
    gs.features_fired.add('duty_assignment')

    # Phase 1c: Personal Phase (3-5 actions)
    n_actions = random.choice([3, 4, 4, 5])
    for _ in range(n_actions):
        action = select_action(weights)
        if action == 'fieldwork':
            resolve_fieldwork(gs, random.choice(['explore','investigate','socialize']),
                            depth=random.randint(0,5), territory=random.choice(list(gs.pt.keys())))
        elif action == 'combat':
            resolve_combat_scene(gs, weapon_idx=random.randint(0,4),
                               armor=random.choice(['none','light','medium','heavy']))
        elif action == 'contest':
            target = next((n for n in gs.npcs.values() if n.alive), None)
            resolve_contest(gs, target)
        elif action == 'thread':
            resolve_thread_scene(gs)
        elif action == 'govern':
            resolve_governance(gs, random.choice(['develop','fortify','pacify','administer']),
                             random.choice(gs.factions.get(gs.pc.faction, gs.factions['Crown']).territories))
        elif action == 'socialize':
            resolve_fieldwork(gs, 'socialize', territory=random.choice(list(gs.pt.keys())))

    # Mass battle chance (increases with IP and season)
    if gs.season > 10 and random.random() < 0.05 + gs.season * 0.002:
        fnames = [f for f in ['Crown','Church','Hafenmark','Varfell'] if gs.factions[f].active]
        if len(fnames) >= 2:
            att, dfd = random.sample(fnames, 2)
            resolve_mass_battle(gs, att, dfd)

    # Phase 2: Faction AI
    for fname in ['Crown','Church','Hafenmark','Varfell']:
        f = gs.factions[fname]
        if not f.active:
            continue
        if fname == 'Church':
            if f.stability <= 2:
                f.cohesion += 10
            elif gs.tc < 75 and f.mandate >= 4:
                gs.tc = min(100, gs.tc + 1)
        elif fname == 'Crown':
            if f.stability > 2 and random.random() < 0.4:
                weakest = min(['mandate','wealth','military','influence','stability'], key=lambda a: getattr(f,a))
                setattr(f, weakest, min(7, getattr(f, weakest) + 1))
        elif fname == 'Hafenmark':
            if gs.tc >= 50 and f.mandate >= 4:
                gs.tc = max(0, gs.tc - 1)
        elif fname == 'Varfell':
            pass
        gs.features_fired.add(f'faction_ai_{fname}')

    # Phase 3: Accounting
    for fname, f in gs.factions.items():
        if not f.active: continue
        income = sum(s.prosperity * 10 for s in gs.settlements if s.controller == fname)
        f.treasury += income - 50
        f.legitimacy += sum(1 for t in f.territories if gs.get_province_accord(t) >= 2) * 5
        f.cohesion += 10
        if f.treasury <= 0:
            f.wealth = max(1, f.wealth - 1)
            f.treasury = f.wealth * 100
            gs.features_fired.add('stat_damage_treasury')

    # RS drift
    gs.rs = max(0, gs.rs - random.choice([0, 0, 0, 1]))

    # Subsystem evaluations
    evaluate_npc_arcs(gs)
    apply_domain_echoes(gs)
    check_victory(gs)
    evaluate_player_agency(gs)
    evaluate_scale_transitions(gs)
    evaluate_companions(gs)
    evaluate_lifecycle(gs)

    # Standing advancement
    if gs.pc.standing < 7 and check(10, 2)[0]:
        gs.pc.standing += 1
        gs.features_fired.add('standing_advancement')

    # Coherence recovery (if no Thread ops this season)
    if 'operation_weaving' not in gs.features_fired and 'operation_pulling' not in gs.features_fired:
        if gs.pc.coherence < 10:
            gs.pc.coherence = min(10, gs.pc.coherence + 1)
            gs.features_fired.add('coherence_recovery_passive')

    # Seasonal events
    for s in gs.settlements:
        r = random.randint(1, 6)
        if r == 1:
            s.prosperity = max(0, s.prosperity - 1) if random.random() < 0.5 else s.prosperity
            s.order = max(0, s.order - 1) if random.random() < 0.5 else s.order
            gs.features_fired.add('settlement_negative_event')
        elif r == 6:
            s.prosperity = min(5, s.prosperity + 1)
            gs.features_fired.add('settlement_positive_event')

    gs.features_fired.add('accounting_complete')


def run_campaign(policy='balanced', seed=42, seasons=120):
    gs = init_game_state(seed=seed)
    if policy in ('practitioner', 'restorationist'):
        gs.pc.ts = 35  # Practitioner origin — Einhir Descendant
    for _ in range(seasons):
        run_season(gs, policy)
    return gs


if __name__ == '__main__':
    # Run baseline
    policies = ['balanced','investigator','warrior','diplomat','practitioner',
                'governor','independent','aggressive','theocrat','restorationist']
    all_features = set()
    for pol in policies:
        for seed in range(5):
            gs = run_campaign(pol, seed=seed*100+42, seasons=120)
            all_features |= gs.features_fired
    print(f"Total features: {len(all_features)}")
    for f in sorted(all_features):
        print(f"  {f}")
