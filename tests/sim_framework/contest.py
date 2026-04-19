"""Social contest subsystem — exchanges, interaction types, adjudicators, outcomes."""
import random, math

def roll_pool(pool, tn=7):
    return sum(1 for _ in range(pool) if random.randint(1,10) >= tn)

INTERACTIONS = ['clash','reinforce','cross','tie']
ADJUDICATORS = ['expert_judge','crowd','no_adjudicator']

def resolve_contest(gs, target_npc=None):
    pc = gs.pc
    adj = random.choice(ADJUDICATORS)
    gs.features_fired.add(f'adjudicator_{adj}')

    # Pool by adjudicator type
    if adj == 'expert_judge':
        pc_pool = pc.cognition * 2 + pc.recall
    elif adj == 'crowd':
        pc_pool = pc.charisma * 2 + pc.recall
    else:
        pc_pool = pc.attunement * 2 + pc.recall

    npc_pool = 10
    track = 5  # center
    resistance = 1 + (1 if random.random() < 0.3 else 0)  # R1 or R2
    composure = pc.charisma + 6
    concentration = 3
    exchanges = 0
    zero_streak = 0
    genre_bonus = 1 if random.random() < 0.5 else 0
    audience_bonus = 1 if random.random() < 0.3 else 0

    gs.features_fired.add('genre_bonus' if genre_bonus else 'no_genre_bonus')
    if genre_bonus and audience_bonus:
        gs.features_fired.add('genre_plus_audience')

    # Recall bonus
    recall_bonus = 2 if random.random() < 0.2 else 0
    if recall_bonus:
        gs.features_fired.add('recall_bonus')
        if random.random() < 0.3:
            gs.features_fired.add('grand_contest_recall')

    while 1 <= track <= 9 and exchanges < 8:
        exchanges += 1
        interaction = random.choice(INTERACTIONS)
        gs.features_fired.add(f'contest_{interaction}')

        effective_pool = pc_pool + genre_bonus + audience_bonus + recall_bonus
        a_succ = roll_pool(effective_pool)
        d_succ = roll_pool(npc_pool)

        if interaction == 'clash':
            margin = a_succ - d_succ
            movement = max(0, abs(margin) - resistance)
            if margin > 0: track += movement
            elif margin < 0: track -= movement
        elif interaction == 'reinforce':
            movement = max(0, a_succ - resistance)
            track += movement
        elif interaction == 'cross':
            margin = math.floor(a_succ / 2)
            movement = max(0, margin - resistance)
            track += movement
        elif interaction == 'tie':
            margin = a_succ - d_succ
            movement = max(0, abs(margin))
            if margin > 0: track += movement
            elif margin < 0: track -= movement

        # Composure
        composure -= 1
        if composure <= 0:
            gs.features_fired.add('composure_rattled')

        # Concentration
        if random.random() < 0.15:
            concentration -= 1
            if concentration <= 0:
                gs.features_fired.add('concentration_spent')

        # Forfeit actions
        if concentration <= 0 and random.random() < 0.5:
            gs.features_fired.add('forfeit_regroup')
            concentration = 2
        if random.random() < 0.1:
            gs.features_fired.add('forfeit_concede_point')

        # Deadlock stall-break (ED-582)
        if movement == 0:
            zero_streak += 1
            if zero_streak == 2:
                resistance = max(1, resistance - 1)
                gs.features_fired.add('deadlock_resistance_drop')
            elif zero_streak >= 3:
                gs.features_fired.add('deadlock_forced_compromise')
                track = 5
                break
        else:
            zero_streak = 0

        track = max(1, min(9, track))

    # Outcome
    if track >= 7:
        gs.features_fired.add('contest_decisive_win')
        gs.features_fired.add('obligation_generated')
        # Conviction Scar
        if target_npc and random.random() < 0.4:
            target_npc.scars += 1
            gs.features_fired.add('conviction_scar')
            rs = random.choice(['evidence','consequence','authority','solidarity'])
            gs.features_fired.add(f'resonant_style_{rs}')
        # Domain Echo
        gs.features_fired.add('debate_domain_echo')
        gs.log.append(f"S{gs.season}: Contest — Decisive win (track {track})")
    elif track <= 3:
        gs.features_fired.add('contest_decisive_loss')
        gs.features_fired.add('conviction_strain_player')
        gs.log.append(f"S{gs.season}: Contest — Decisive loss")
    else:
        gs.features_fired.add('contest_compromise')
        gs.features_fired.add('chain_contest_generated')
        gs.log.append(f"S{gs.season}: Contest — Compromise (track {track})")

    # Total Victory check
    if track >= 9 or track <= 1:
        gs.features_fired.add('total_victory')
