"""Fieldwork subsystem — exploration, investigation, socializing, Exposure, Knot formation."""
import random, math

def roll_pool(pool, tn=7):
    return sum(1 for _ in range(pool) if random.randint(1,10) >= tn)

INVESTIGATE_ACTIONS = ['examine','interview','research','surveil','thread_read','reconstruct']
SOCIAL_ACTIONS = ['read','converse','connect','impress','rumour','negotiate','gift_bribe']
EVIDENCE_THRESHOLDS = {'simple':3, 'complex':5, 'structural':8}

def resolve_fieldwork(gs, action_type='investigate', depth=2, territory='T1'):
    pc = gs.pc
    pool = pc.attunement * 2 + pc.recall

    if action_type == 'explore':
        depth = min(5, max(0, depth))
        ob = [1,1,2,3,5,8][depth]
        passed = roll_pool(pool) >= ob
        gs.features_fired.add(f'exploration_depth_{depth}')
        if passed:
            gs.features_fired.add('poi_discovery')
        else:
            # Desperate Trail
            gs.pc.exposure = gs.pc.exposure or {}
            gs.pc.exposure[territory] = gs.pc.exposure.get(territory, 0) + 1
            if gs.pc.exposure.get(territory, 0) >= 3:
                gs.features_fired.add('desperate_trail')

    elif action_type == 'investigate':
        inv_action = random.choice(INVESTIGATE_ACTIONS)
        gs.features_fired.add(f'investigation_{inv_action}')
        ob = 3
        passed = roll_pool(pool) >= ob
        if passed:
            gs.features_fired.add('evidence_progress')
            # Track completion check
            for name, threshold in EVIDENCE_THRESHOLDS.items():
                if random.random() < 0.15:
                    gs.features_fired.add(f'evidence_complete_{name}')
        if inv_action == 'reconstruct' and not passed:
            gs.features_fired.add('failed_reconstruct')
        if inv_action == 'thread_read' and pc.ts >= 30:
            gs.features_fired.add('thread_read_investigation')
            gs.features_fired.add('investigation_domain_echo')
        gs.pc.exposure = gs.pc.exposure or {}
        gs.pc.exposure[territory] = gs.pc.exposure.get(territory, 0) + 1

    elif action_type == 'socialize':
        social_action = random.choice(SOCIAL_ACTIONS)
        gs.features_fired.add(f'social_{social_action}')
        target = next((n for n in gs.npcs.values() if n.alive), None)
        if target:
            ob = 2
            charisma_pool = pc.charisma * 2
            passed = roll_pool(charisma_pool) >= ob
            if passed:
                old_disp = target.disposition
                target.disposition = min(5, target.disposition + 1)
                gs.features_fired.add('disposition_change')
                if target.disposition >= 5:
                    gs.features_fired.add('disposition_max')
                if target.disposition <= -3:
                    gs.features_fired.add('disposition_min')
            # Sincerity Gate
            if social_action in ['impress','negotiate'] and random.random() < 0.2:
                spirit_check = roll_pool(pc.spirit * 2) >= 2
                if not spirit_check:
                    gs.features_fired.add('sincerity_gate_failure')

            # NPC-initiated checks
            if target.disposition >= 2:
                gs.features_fired.add('npc_outreach')
            if target.disposition <= -2:
                gs.features_fired.add('npc_demand')
                # Deflection attempt
                deflect_ob = max(1, target.certainty // 2 + 2)
                if roll_pool(pool) >= deflect_ob:
                    gs.features_fired.add('demand_deflection_success')
                else:
                    gs.features_fired.add('demand_deflection_failure')

    # Exposure thresholds
    exp = gs.pc.exposure.get(territory, 0) if gs.pc.exposure else 0
    cover = pc.cognition + 2
    if exp >= cover:
        gs.features_fired.add('exposure_noticed')
    if exp >= cover + 2:
        gs.features_fired.add('exposure_watched')
    if exp >= cover + 4:
        gs.features_fired.add('exposure_compromised')

    # Knot formation check
    if any(n.disposition >= 5 and (pc.ts >= 30 or n.ts >= 30) for n in gs.npcs.values() if n.alive):
        if len(pc.knots) < pc.bonds // 2:
            gs.features_fired.add('knot_formation_eligible')
            if roll_pool(pc.spirit * 2) >= 2:
                gs.features_fired.add('knot_formation_success')
                eligible = [n for n in gs.npcs.values() if n.disposition >= 5 and n.alive]
                if eligible:
                    pc.knots.append(eligible[0].name)

    # Combined Findings in contest
    if random.random() < 0.1:
        gs.features_fired.add('combined_findings_in_contest')
