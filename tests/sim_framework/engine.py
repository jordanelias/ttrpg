"""
Valoria Campaign Simulation — Season Resolution Engine (Phase 4.2)
Implements the season loop from workplan §4.0.
"""
import math, random
from state import GameState, init_game_state

def roll_pool(pool: int, tn: int = 7) -> int:
    """Roll pool d10s against TN, return successes."""
    return sum(1 for _ in range(pool) if random.randint(1, 10) >= tn)

def check(pool: int, ob: int, tn: int = 7) -> tuple:
    """Roll check. Returns (passed, net_successes, degree)."""
    successes = roll_pool(pool, tn)
    net = successes - ob
    if net >= 3:
        degree = 'overwhelming'
    elif net >= 0:
        degree = 'success' if net >= 0 else 'failure'
    elif net == -1:
        degree = 'partial'
    else:
        degree = 'failure'
    if successes >= ob:
        degree = 'overwhelming' if net >= 3 else 'success'
    else:
        degree = 'partial' if successes == ob - 1 else 'failure'
    return successes >= ob, net, degree


# ─── PHASE 1a: DUTY ASSIGNMENT ───

def duty_assignment(gs: GameState):
    if gs.pc.standing == 0:
        gs.log.append(f"S{gs.season}: Initiation Duty assigned")
        gs.features_fired.add('duty_assignment')
    else:
        gs.log.append(f"S{gs.season}: Duty assigned (Standing {gs.pc.standing})")
        gs.features_fired.add('duty_assignment')


# ─── PHASE 1b: SCENE SLATE GENERATION ───

def generate_scene_slate(gs: GameState) -> list:
    """Generate scene slate per player_agency §4.2."""
    scenes = []
    # Priority 0: Mandatory crisis
    if any(gs.get_province_accord(t) == 0 for t in gs.factions.get(gs.pc.faction, gs.factions['Crown']).territories):
        scenes.append(('crisis', 0, 'Accord 0 revolt'))
        gs.features_fired.add('scene_slate_p0')
    # Priority 1: Crisis events
    if gs.strain >= 5:
        scenes.append(('crisis', 1, 'Strain crisis'))
        gs.features_fired.add('scene_slate_p1')
    # Priority 2: Duty-aligned
    scenes.append(('duty', 2, 'Faction duty'))
    gs.features_fired.add('scene_slate_p2')
    # Priority 3: Conviction + NPC outreach
    if gs.pc.convictions:
        scenes.append(('conviction', 3, 'Conviction pursuit'))
        gs.features_fired.add('scene_slate_p3')
    for npc in gs.npcs.values():
        if npc.disposition >= 2 and npc.alive:
            scenes.append(('outreach', 3, f'{npc.name} outreach'))
        elif npc.disposition <= -2 and npc.alive:
            scenes.append(('demand', 3, f'{npc.name} demand'))
    # Priority 4: Territorial
    scenes.append(('territorial', 4, 'Territory event'))
    gs.features_fired.add('scene_slate_p4')
    # Priority 5: Ambient
    scenes.append(('ambient', 5, 'Ambient scene'))
    gs.features_fired.add('scene_slate_p5')
    return scenes


# ─── PHASE 1c: PERSONAL PHASE (player policy selects scenes) ───

def resolve_fieldwork(gs: GameState, action_type: str):
    """Resolve a fieldwork scene action."""
    pool = gs.pc.attunement * 2 + gs.pc.recall
    if action_type == 'investigate':
        passed, net, degree = check(pool, 3)
        gs.features_fired.add('investigation')
        if passed:
            gs.log.append(f"S{gs.season}: Investigation {degree}")
    elif action_type == 'socialize':
        target_npc = next((n for n in gs.npcs.values() if n.alive and n.faction != gs.pc.faction), None)
        if target_npc:
            passed, net, degree = check(gs.pc.charisma * 2, 2)
            if passed:
                target_npc.disposition = min(5, target_npc.disposition + 1)
                gs.features_fired.add('disposition_change')
            gs.log.append(f"S{gs.season}: Socialize with {target_npc.name}: {degree} (Disp {target_npc.disposition})")
    elif action_type == 'explore':
        passed, net, degree = check(pool, 2)
        gs.features_fired.add('exploration')

def resolve_combat(gs: GameState):
    """Resolve a personal combat scene."""
    # Simplified: pool split, roll, damage
    pc_pool = gs.pc.spirit * 2 + 3  # weapon skill
    enemy_pool = 8  # average NPC
    pc_off = pc_pool // 2
    pc_def = pc_pool - pc_off
    e_off = enemy_pool // 2
    e_def = enemy_pool - e_off
    pc_hits = max(0, roll_pool(pc_off) - roll_pool(e_def))
    e_hits = max(0, roll_pool(e_off) - roll_pool(pc_def))
    gs.pc.wounds += e_hits
    gs.features_fired.add('combat_action_strike')
    gs.features_fired.add('wound_accumulation')
    gs.log.append(f"S{gs.season}: Combat — PC deals {pc_hits}, takes {e_hits} (wounds: {gs.pc.wounds})")
    if pc_hits >= 3:
        gs.features_fired.add('combat_domain_echo')

def resolve_contest(gs: GameState):
    """Resolve a social contest."""
    pc_pool = gs.pc.charisma * 2 + gs.pc.recall
    npc_pool = 10
    track = 5  # center
    resistance = 1
    for exchange in range(5):
        pc_succ = roll_pool(pc_pool)
        npc_succ = roll_pool(npc_pool)
        margin = pc_succ - npc_succ
        movement = max(0, abs(margin) - resistance)
        if margin > 0:
            track += movement
        elif margin < 0:
            track -= movement
        if track >= 7 or track <= 3:
            break
    gs.features_fired.add('contest_clash')
    if track >= 7:
        gs.features_fired.add('contest_decisive_win')
        gs.log.append(f"S{gs.season}: Contest — Decisive win (track {track})")
    elif track <= 3:
        gs.features_fired.add('contest_decisive_loss')
        gs.log.append(f"S{gs.season}: Contest — Decisive loss (track {track})")
    else:
        gs.features_fired.add('contest_compromise')
        gs.log.append(f"S{gs.season}: Contest — Compromise (track {track})")

def resolve_thread_op(gs: GameState):
    """Resolve a Thread operation."""
    if gs.pc.ts < 30:
        return
    # Leap
    pool = gs.pc.spirit * 2 + gs.pc.ts // 10
    passed, net, degree = check(pool, 2)
    gs.features_fired.add(f'leap_{degree}')
    # Coherence loss
    gs.pc.coherence = max(0, gs.pc.coherence - 1)
    gs.features_fired.add('coherence_degradation')
    # Co-Movement card draw
    if gs.cm_drawn >= len(gs.cm_deck):
        random.shuffle(gs.cm_deck)
        gs.cm_drawn = 0
    card = gs.cm_deck[gs.cm_drawn]
    gs.cm_drawn += 1
    gs.features_fired.add(f'cm_card_{card}')
    # RS change (simplified: cards 1-4,6,8,9,13-15 negative, 5,10,12 positive)
    rs_changes = {1:-1, 2:-2, 3:-1, 4:-1, 5:+1, 6:-2, 7:0, 8:-1, 9:-3, 10:+2,
                  11:0, 12:+1, 13:-1, 14:-3, 15:-2, 16:+1, 17:+1, 18:+1}
    gs.rs = max(0, min(100, gs.rs + rs_changes.get(card, 0)))
    gs.log.append(f"S{gs.season}: Thread op — {degree}, Coherence {gs.pc.coherence}, RS {gs.rs}, CM-{card:02d}")


# ─── PHASE 2: FACTION AI ───

def faction_ai_turn(gs: GameState, faction_name: str):
    """Execute faction AI priority tree for one season."""
    f = gs.factions[faction_name]
    if not f.active:
        return

    if faction_name == 'Church':
        if f.stability <= 2:
            action = 'Consul Inward (stability)'
            if check(f.influence, 2)[0]:
                f.cohesion += 10
        elif gs.tc < 75 and f.mandate >= 4:
            action = 'Assert'
            gs.tc = min(100, gs.tc + 1)
        else:
            action = 'Piety governance'
    elif faction_name == 'Crown':
        if f.stability <= 2:
            action = 'Consul Inward (stability)'
        elif random.random() < 0.4:
            action = 'Royal Decree'
            weakest = min(['mandate','wealth','military','influence','stability'],
                         key=lambda a: getattr(f, a))
            setattr(f, weakest, min(7, getattr(f, weakest) + 1))
        else:
            action = 'Govern'
    elif faction_name == 'Hafenmark':
        if f.stability <= 2:
            action = 'Consul Inward (stability)'
        elif gs.tc >= 50 and f.mandate >= 4:
            action = 'Suppress TC'
            gs.tc = max(0, gs.tc - 1)
        else:
            action = 'Trade + Govern'
    elif faction_name == 'Varfell':
        if f.stability <= 2:
            action = 'Consul Inward (stability)'
        elif random.random() < 0.5:
            action = 'Tribune Investigate'
        else:
            action = 'VTM advancement'
    else:
        action = 'Pass'

    gs.features_fired.add(f'faction_ai_{faction_name}')


# ─── PHASE 3: ACCOUNTING ───

def run_accounting(gs: GameState):
    """13-step Accounting sequence (simplified)."""
    # Step 1: Derived value income/drain
    for fname, f in gs.factions.items():
        if not f.active:
            continue
        # Treasury income from settlements
        prosperity_income = sum(s.prosperity * 10 for s in gs.settlements if s.controller == fname)
        f.treasury += prosperity_income
        # Unit upkeep (assume 2 professional per faction)
        f.treasury -= 50
        # Legitimacy from governed territories
        accord_territories = sum(1 for t in f.territories if gs.get_province_accord(t) >= 2)
        f.legitimacy += accord_territories * 5
        # Cohesion from peaceful seasons
        f.cohesion += 10

    # Step 2: Stat damage checks
    for f in gs.factions.values():
        if not f.active:
            continue
        if f.treasury <= 0:
            f.wealth = max(1, f.wealth - 1)
            f.treasury = f.wealth * 100
            gs.features_fired.add('stat_damage_treasury')
        if f.legitimacy <= 0:
            f.mandate = max(1, f.mandate - 1)
            f.legitimacy = f.mandate * 20
            gs.features_fired.add('stat_damage_legitimacy')

    # Step 4a: TC calculation
    gs.tc = min(100, gs.tc)  # Church Assert already added

    # Step 4d: Strain advancement
    if any(gs.get_province_accord(t) <= 1 for t in
           [t for f in gs.factions.values() if f.active for t in f.territories]):
        gs.strain = min(10, gs.strain + 1)

    # Step 5: RS update (drift)
    gs.rs = max(0, gs.rs)

    # Step 6: NPC arc evaluation
    for npc in gs.npcs.values():
        if not npc.alive:
            continue
        if npc.scars >= 3:
            gs.features_fired.add('conviction_crisis')

    # Step 8: Victory condition check
    for fname, f in gs.factions.items():
        if not f.active:
            continue
        tcv = len(f.territories)
        if fname == 'Crown' and tcv >= 14:
            gs.features_fired.add('crown_victory_check')
        if fname == 'Church' and gs.tc >= 75:
            gs.features_fired.add('church_seizure_available')

    # Step 10: Seasonal clock ticks
    gs.ip = min(100, gs.ip + (2 if gs.tc >= 60 else 0))

    # Step 11: Coherence recovery
    # (simplified: if PC didn't do Thread ops this season, +1)

    # Step 12: Seasonal events
    for s in gs.settlements:
        roll = random.randint(1, 6)
        if roll == 1:
            s.prosperity = max(0, s.prosperity - 1) if random.random() < 0.5 else s.prosperity
            if random.random() >= 0.5:
                s.order = max(0, s.order - 1)
            gs.features_fired.add('settlement_negative_event')
        elif roll == 6:
            s.prosperity = min(5, s.prosperity + 1)
            gs.features_fired.add('settlement_positive_event')

    # Step 13: Standing advancement
    if gs.pc.standing < 7:
        # Duty success check (simplified)
        if check(10, 2)[0]:
            gs.pc.standing += 1
            gs.features_fired.add('standing_advancement')
            gs.log.append(f"S{gs.season}: Standing → {gs.pc.standing}")

    gs.features_fired.add('accounting_complete')


# ─── PLAYER POLICIES ───

POLICIES = {
    'balanced': lambda gs, scenes: ['fieldwork', 'contest', 'fieldwork', 'duty'],
    'investigator': lambda gs, scenes: ['fieldwork', 'fieldwork', 'fieldwork', 'duty'],
    'warrior': lambda gs, scenes: ['combat', 'combat', 'duty', 'fieldwork'],
    'diplomat': lambda gs, scenes: ['contest', 'socialize', 'contest', 'duty'],
    'practitioner': lambda gs, scenes: ['thread', 'thread', 'fieldwork', 'duty'],
    'governor': lambda gs, scenes: ['govern', 'govern', 'fieldwork', 'duty'],
    'independent': lambda gs, scenes: ['fieldwork', 'contest', 'fieldwork', 'fieldwork'],
    'aggressive': lambda gs, scenes: ['combat', 'combat', 'combat', 'duty'],
    'theocrat': lambda gs, scenes: ['contest', 'govern', 'duty', 'fieldwork'],
    'restorationist': lambda gs, scenes: ['thread', 'fieldwork', 'contest', 'duty'],
}


# ─── MAIN SEASON LOOP ───

def run_season(gs: GameState, policy: str = 'balanced'):
    """Run one complete season."""
    gs.season += 1

    # Phase 1a: Duty Assignment
    duty_assignment(gs)

    # Phase 1b: Scene Slate
    scenes = generate_scene_slate(gs)

    # Phase 1c: Personal Phase (3-4 actions based on policy)
    actions = POLICIES.get(policy, POLICIES['balanced'])(gs, scenes)
    for action in actions[:4]:
        if action == 'fieldwork':
            resolve_fieldwork(gs, 'investigate')
        elif action == 'combat':
            resolve_combat(gs)
        elif action == 'contest':
            resolve_contest(gs)
        elif action == 'thread':
            resolve_thread_op(gs)
        elif action == 'socialize':
            resolve_fieldwork(gs, 'socialize')
        elif action == 'govern':
            # Governance action
            gs.features_fired.add('governance_action')
        elif action == 'duty':
            gs.features_fired.add('duty_action')

    # Phase 2: Faction AI
    for fname in ['Crown', 'Church', 'Hafenmark', 'Varfell']:
        faction_ai_turn(gs, fname)

    # Phase 3: Accounting
    run_accounting(gs)


def run_campaign(policy: str = 'balanced', seed: int = 42, seasons: int = 120) -> GameState:
    """Run a full campaign simulation."""
    gs = init_game_state(seed=seed)
    for _ in range(seasons):
        run_season(gs, policy)
        # Victory check
        if gs.season >= 60:
            for f in gs.factions.values():
                if len(f.territories) >= 15 and f.active:
                    gs.log.append(f"S{gs.season}: {f.name} achieves Peninsular Sovereignty")
                    gs.features_fired.add('victory_achieved')
                    return gs
    return gs


if __name__ == '__main__':
    # Quick test
    gs = run_campaign('balanced', seed=42, seasons=10)
    print(f"Season {gs.season}")
    print(f"RS: {gs.rs}, TC: {gs.tc}, IP: {gs.ip}")
    print(f"Features fired: {len(gs.features_fired)}")
    for f in ['Crown', 'Church', 'Hafenmark', 'Varfell']:
        fac = gs.factions[f]
        print(f"  {f}: Man={fac.mandate} Wea={fac.wealth} Mil={fac.military} Inf={fac.influence} Sta={fac.stability} Treasury={fac.treasury:.0f}")
