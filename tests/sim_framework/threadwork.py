"""Threadwork subsystem — operations, Coherence, Co-Movement, Rendering Crisis."""
import random, math

def roll_pool(pool, tn=7):
    return sum(1 for _ in range(pool) if random.randint(1,10) >= tn)

OPERATIONS = ['weaving','pulling','pop','locking','dissolution']

def resolve_thread_scene(gs, op_type=None):
    pc = gs.pc
    if pc.ts < 30:
        return

    if op_type is None:
        op_type = random.choice(OPERATIONS)

    pool = pc.spirit * 2 + pc.recall + (pc.ts // 10)
    tn = 7 if op_type in ['weaving','pulling','pop'] else 8  # Locking/Dissolution harder

    # Leap
    leap_succ = roll_pool(pool, 7)
    if leap_succ >= 3:
        degree = 'overwhelming'
    elif leap_succ >= 2:
        degree = 'success'
    elif leap_succ >= 1:
        degree = 'partial'
    else:
        degree = 'failure'
    gs.features_fired.add(f'leap_{degree}')
    gs.features_fired.add(f'operation_{op_type}')

    # Contact duration = Focus
    contact_rounds = pc.focus

    # Operation resolution
    if op_type == 'weaving':
        ob = 3  # Relational depth
        passed = roll_pool(pool, tn) >= ob
        if passed and random.random() < 0.3:
            gs.features_fired.add('over_actualisation')
    elif op_type == 'pulling':
        ob = 3
        passed = roll_pool(pool, tn) >= ob
    elif op_type == 'pop':
        ob = 5  # Past-oriented is harder
        passed = roll_pool(pool, tn) >= ob
        gs.rs = max(0, gs.rs - 3)  # POP always costs RS
    elif op_type == 'locking':
        ob = 4
        passed = roll_pool(pool, 8) >= ob
        if passed:
            gs.rs = max(0, gs.rs - 2)
    elif op_type == 'dissolution':
        ob = 3
        passed = roll_pool(pool, 8) >= ob
        if passed:
            gs.rs = max(0, gs.rs - 5)
            gs.features_fired.add('dissolution_residue')
            gs.features_fired.add('thread_domain_echo')
            gs.features_fired.add('thread_cv_drift')  # PT -1

    # Coherence loss
    coherence_cost = 1 if op_type in ['weaving','pulling'] else 2
    pc.coherence = max(0, pc.coherence - coherence_cost)
    gs.features_fired.add('coherence_degradation')

    # Coherence thresholds
    if pc.coherence <= 8: gs.features_fired.add('coherence_threshold_stable')
    if pc.coherence <= 5: gs.features_fired.add('coherence_threshold_fragmented')
    if pc.coherence <= 3: gs.features_fired.add('coherence_threshold_fractured')
    if pc.coherence <= 1: gs.features_fired.add('coherence_threshold_severed')
    if pc.coherence == 0:
        gs.features_fired.add('rendering_crisis')
        # 4-beat resolution
        gs.features_fired.add('rendering_crisis_withdrawal')
        gs.features_fired.add('rendering_crisis_knot_anchoring')
        gs.features_fired.add('rendering_crisis_place_anchoring')
        gs.features_fired.add('rendering_crisis_the_choice')
        # Recovery or permanent loss
        if roll_pool(pc.spirit * 2) >= 2:
            pc.coherence = 3
            gs.features_fired.add('coherence_recovery')
        else:
            pc.coherence = 1
            pc.ts = max(0, pc.ts - 5)

    # Co-Movement card draw
    if gs.cm_drawn >= len(gs.cm_deck):
        random.shuffle(gs.cm_deck)
        gs.cm_drawn = 0
    card = gs.cm_deck[gs.cm_drawn]
    gs.cm_drawn += 1
    gs.features_fired.add(f'cm_card_{card}')
    rs_changes = {1:-1, 2:-2, 3:-1, 4:-1, 5:+1, 6:-2, 7:0, 8:-1, 9:-3, 10:+2,
                  11:0, 12:+1, 13:-1, 14:-3, 15:-2, 16:+1, 17:+1, 18:+1}
    gs.rs = max(0, min(100, gs.rs + rs_changes.get(card, 0)))

    # TS advancement
    if random.random() < 0.05:
        old_ts = pc.ts
        pc.ts += 5
        if old_ts < 30 and pc.ts >= 30:
            gs.features_fired.add('ts_cross_30')
        if old_ts < 50 and pc.ts >= 50:
            gs.features_fired.add('ts_cross_50')
        gs.features_fired.add('ts_advancement')

    # Collective operation chance
    if random.random() < 0.15:
        gs.features_fired.add('collective_operation')

    # Opposing operation chance
    if random.random() < 0.1:
        gs.features_fired.add('opposing_operation')

    # Wound disruption during contact
    if pc.wounds > 0 and random.random() < 0.2:
        gs.features_fired.add('wound_disruption_during_contact')

    # Thread perception visibility
    gs.features_fired.add(f'thread_perception_ts_{min(70, (pc.ts // 10) * 10)}')

    # Mending chance
    if random.random() < 0.2 and op_type == 'weaving':
        gs.features_fired.add('mending_operation')
        severity = random.choice(['shifting_object','micro_gap','standard_gap','entrenched'])
        gs.features_fired.add(f'mending_{severity}')
        if passed:
            gs.features_fired.add('thread_domain_echo_mending')

    gs.log.append(f"S{gs.season}: Thread {op_type} — {degree}, Coh {pc.coherence}, RS {gs.rs}, CM-{card:02d}")
