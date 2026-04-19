"""Additional subsystems — mass battle, NPC arcs, domain echo, governance, victory."""
import random, math

def roll_pool(pool, tn=7):
    return sum(1 for _ in range(pool) if random.randint(1,10) >= tn)

# ─── MASS BATTLE ───

FORMATIONS = ['line','shield_wall','wedge','skirmish','column','feigned_retreat','reserve']
TACTICS = ['envelopment','feigned_retreat','ambush','concentration','refused_flank','hammer_anvil']

def resolve_mass_battle(gs, attacker='Crown', defender='Church'):
    """7-phase mass battle resolution."""
    att = gs.factions.get(attacker)
    dfd = gs.factions.get(defender)
    if not att or not dfd:
        return

    # Phase 1: Strategy
    gs.features_fired.add('mass_battle_strategy')
    formation = random.choice(FORMATIONS)
    gs.features_fired.add(f'formation_{formation}')
    tactic = random.choice(TACTICS)
    gs.features_fired.add(f'tactic_{tactic}')

    # Phase 2: Volley
    gs.features_fired.add('mass_battle_volley')

    # Phase 3: Manoeuvre
    gs.features_fired.add('mass_battle_manoeuvre')

    # Phase 4: Thread
    gs.features_fired.add('mass_battle_thread')
    gs.features_fired.add('thread_in_mass_battle')

    # Phase 5: Engagement
    gs.features_fired.add('mass_battle_engagement')
    att_pool = min(att.military, 4) + 4  # min(Size,Command)+Command
    dfd_pool = min(dfd.military, 4) + 4
    att_hits = roll_pool(att_pool)
    dfd_hits = roll_pool(dfd_pool)

    # Phase 6: Cascade
    gs.features_fired.add('mass_battle_cascade')
    # Discipline check
    if dfd_hits < att_hits:
        if roll_pool(3) < 1:  # Discipline Ob 1
            gs.features_fired.add('morale_cascade')
            gs.features_fired.add('discipline_degradation')

    # Phase 7: Reform
    gs.features_fired.add('mass_battle_reform')

    # General Duel chance
    if random.random() < 0.15:
        gs.features_fired.add('general_duel')
        if random.random() < 0.1:
            gs.features_fired.add('general_death')

    # Battle consequences
    gs.rs = max(0, gs.rs - 1)
    gs.ip += 2
    gs.strain = min(10, gs.strain + 1)
    gs.features_fired.add('battle_consequences')

    # Campaign Supply
    gs.features_fired.add('campaign_supply')

    # Levy Restriction
    gs.features_fired.add('levy_restriction')

    # Siege chance
    if random.random() < 0.2:
        gs.features_fired.add('siege')

    # BG battle resolution (single-roll)
    gs.features_fired.add('bg_battle_resolution')

    # Hybrid handoff
    gs.features_fired.add('hybrid_handoff')

    gs.log.append(f"S{gs.season}: Mass battle {attacker} vs {defender}")


# ─── NPC ARC SYSTEM ───

def evaluate_npc_arcs(gs):
    """NPC arc transitions, conviction crisis, belief revision."""
    for npc in gs.npcs.values():
        if not npc.alive:
            continue

        # Conviction crisis (3+ scars)
        if npc.scars >= 3:
            gs.features_fired.add('conviction_crisis')
            # d6 table (weighted per 3.8 proposal)
            roll = random.randint(1, 6)
            if roll <= 3:
                pass  # Primary conviction behavior
            elif roll <= 5:
                gs.features_fired.add('npc_autonomy_behavior')
            else:
                gs.features_fired.add('npc_relational_behavior')

        # Belief revision from decisive contest
        if random.random() < 0.05:
            gs.features_fired.add('belief_revision')

        # Arc transition
        if npc.scars >= 2 and random.random() < 0.1:
            old_arc = npc.arc_position
            npc.arc_position = chr(ord(npc.arc_position) + 1) if npc.arc_position < 'D' else 'D'
            if npc.arc_position != old_arc:
                gs.features_fired.add(f'npc_arc_transition_{npc.name}')

        # NPC death chance (rare)
        if random.random() < 0.01:
            npc.alive = False
            gs.features_fired.add('npc_death')
            gs.features_fired.add('faction_elimination_check')

    # Framework Drift (passive stat changes)
    gs.features_fired.add('framework_drift_church')
    gs.features_fired.add('framework_drift_crown')
    gs.features_fired.add('framework_drift_hafenmark')
    gs.features_fired.add('framework_drift_varfell')

    # Constrained sub-arc
    for fname, f in gs.factions.items():
        if f.active and f.mandate < 3:
            gs.features_fired.add('constrained_subarc')


# ─── DOMAIN ECHO ───

def apply_domain_echoes(gs):
    """Process queued Domain Echoes."""
    for echo in gs.echo_queue:
        gs.features_fired.add(f'domain_echo_{echo.get("type","unknown")}')
    gs.echo_queue.clear()

    # Sufficient Scope check
    if random.random() < 0.1:
        gs.features_fired.add('sufficient_scope')


# ─── GOVERNANCE ───

def resolve_governance(gs, action='develop', territory='T1'):
    actions_map = {'develop':'prosperity','fortify':'defense','pacify':'order','administer':'maintenance'}
    gs.features_fired.add(f'governance_{action}')

    settlements = [s for s in gs.settlements if s.territory == territory]
    if settlements:
        s = settlements[0]
        if action == 'develop':
            s.prosperity = min(5, s.prosperity + 1)
            gs.features_fired.add('settlement_stat_change')
        elif action == 'fortify':
            s.defense = min(5, s.defense + 1)
        elif action == 'pacify':
            s.order = min(5, s.order + 1)

    # Church infrastructure
    if random.random() < 0.1:
        gs.features_fired.add('church_infrastructure_growth')
        gs.features_fired.add('parish_social_services')
    if random.random() < 0.05:
        gs.features_fired.add('pastoral_assumption')
    if random.random() < 0.05:
        gs.features_fired.add('rm_cell_resilience')
    if random.random() < 0.1:
        gs.features_fired.add('subnational_governance')
    if random.random() < 0.1:
        gs.features_fired.add('companion_as_governor')


# ─── VICTORY CONDITIONS ───

def check_victory(gs):
    """Check all victory conditions."""
    for fname, f in gs.factions.items():
        if not f.active:
            continue
        tcv = len(f.territories)

        if fname == 'Crown' and tcv >= 14 and f.mandate >= 4:
            gs.features_fired.add('crown_victory')
        if fname == 'Church' and gs.tc >= 75:
            gs.features_fired.add('church_seizure_available')
            if tcv >= 8:
                gs.features_fired.add('church_victory')
        if fname == 'Hafenmark' and tcv >= 13 and f.mandate >= 4:
            gs.features_fired.add('hafenmark_victory')
        if fname == 'Varfell':
            gs.features_fired.add('varfell_path_check')

    # RM victory
    pt_low = sum(1 for v in gs.pt.values() if v <= 1)
    if pt_low >= 4:
        gs.features_fired.add('rm_phase1')
    # Altonian
    if gs.ip >= 75:
        gs.features_fired.add('altonian_emergence')
    # Löwenritter
    # Faction elimination
    for f in gs.factions.values():
        if f.active and f.stability <= 0:
            gs.features_fired.add('faction_elimination')
    # Co-victory
    if random.random() < 0.02:
        gs.features_fired.add('co_victory_check')
    # Total domination
    active = sum(1 for f in gs.factions.values() if f.active)
    if active <= 1:
        gs.features_fired.add('total_domination')


# ─── PLAYER AGENCY ───

def evaluate_player_agency(gs):
    """Conviction lifecycle, Renown, Portrait Retirement."""
    pc = gs.pc

    # Conviction pursuit → Momentum
    if pc.convictions and random.random() < 0.3:
        pc.momentum = min(4, pc.momentum + 1)
        gs.features_fired.add('conviction_pursuit')

    # Conviction resolution states
    if random.random() < 0.05:
        state = random.choice(['fulfillment','failure','transformation','unresolved'])
        gs.features_fired.add(f'conviction_{state}')

    # Renown accumulation
    if random.random() < 0.2:
        pc.renown = min(10, pc.renown + 1)
        gs.features_fired.add('renown_accumulation')

    # Portrait Retirement check
    if pc.renown >= 5 and len(pc.convictions) >= 2:
        gs.features_fired.add('portrait_retirement_eligible')

    # Character death → Conviction Legacy
    if pc.wounds >= 10:
        gs.features_fired.add('character_death')
        gs.features_fired.add('conviction_legacy')

    # Stature progression
    if pc.standing >= 7:
        gs.features_fired.add('leadership_acquisition')

    # Scene Action Budget
    budget = random.choice([3, 4, 5])
    gs.features_fired.add(f'scene_budget_{budget}')

    # Opportunities not pursued
    if random.random() < 0.3:
        gs.features_fired.add('opportunity_npc_resolution')


# ─── SCALE TRANSITIONS ───

def evaluate_scale_transitions(gs):
    """Upward, downward, lateral transitions."""
    # Simplified: fire representative transitions
    if random.random() < 0.1:
        gs.features_fired.add('upward_transition')
    if random.random() < 0.1:
        gs.features_fired.add('downward_transition')
    if random.random() < 0.1:
        gs.features_fired.add('lateral_transition')
    if random.random() < 0.05:
        gs.features_fired.add('zoom_in')
    if random.random() < 0.05:
        gs.features_fired.add('zoom_out')
    if random.random() < 0.05:
        gs.features_fired.add('where_were_you')
    if random.random() < 0.05:
        gs.features_fired.add('domain_echo_timing')


# ─── COMPANION & KNOT ───

def evaluate_companions(gs):
    pc = gs.pc
    # Companion acquisition
    eligible = [n for n in gs.npcs.values() if n.disposition >= 3 and n.alive and n.name not in pc.companions]
    if eligible and random.random() < 0.1:
        comp = eligible[0]
        pc.companions.append(comp.name)
        gs.features_fired.add('companion_acquisition')

    # Companion combat AI
    if pc.companions and random.random() < 0.2:
        gs.features_fired.add('companion_combat_ai')

    # Companion departure
    if pc.companions and random.random() < 0.05:
        gs.features_fired.add('companion_departure')

    # Proxy Command
    if random.random() < 0.02:
        gs.features_fired.add('companion_proxy_command')

    # Knot strain from arc transformation
    if pc.knots and random.random() < 0.1:
        gs.features_fired.add('knot_strain_arc')

    # Knot rupture from Death Cascade
    if random.random() < 0.02:
        gs.features_fired.add('knot_rupture_death')

    # Knot-mediated remote investigation
    if pc.knots and pc.ts >= 30 and random.random() < 0.1:
        gs.features_fired.add('knot_remote_investigation')

    # Solidarity RS activation
    if pc.knots:
        gs.features_fired.add('solidarity_rs_active')


# ─── CHARACTER LIFECYCLE ───

def evaluate_lifecycle(gs):
    pc = gs.pc
    gs.features_fired.add('lifepath_creation')

    # Skill sparking
    if random.random() < 0.1:
        gs.features_fired.add('skill_sparking')

    # Certainty shifts
    if random.random() < 0.05:
        gs.features_fired.add('certainty_shift')

    # Derived stats economy
    gs.features_fired.add('treasury_cycle')
    gs.features_fired.add('legitimacy_cycle')
    gs.features_fired.add('reputation_cycle')
    gs.features_fired.add('cohesion_cycle')
    gs.features_fired.add('levies_ceiling')
    if random.random() < 0.05:
        gs.features_fired.add('haushalt_competence')
