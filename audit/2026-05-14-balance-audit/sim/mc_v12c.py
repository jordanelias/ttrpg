"""
v12c — CORRECTED BALANCE VECTORS

Design corrections from Jordan:

1. PARLIAMENTARY TRANSFER: requires Casus Belli (CB) against target faction.
   Must then win a majority vote (I-based). Much harder than military action.
   Crown special: auto-justified when territories < 6 (constitutional restoration).

2. RESTORATION MOVEMENT (RM): independent world-level clock that degrades PT.
   Fires every arc. RM strength grows over time. Varfell can co-opt RM for
   Einhir Revival but doesn't control it.

3. EINHIR REVIVAL: gated by Varfell I (national Influence), not L.
   Represents peninsula-wide political reach needed to make cultural claim stick.

4. ALTONIAN REINFORCEMENTS: automatic at arc boundary (no action slot).
   Hafenmark's foreign diplomacy produces military support passively.

5. TREATY EXPIRATION: per RC-v1.
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (ALL_PLAYABLE_15, CANONICAL_TERRITORIES, Faction, Territory,
                   World, init_world, roll_pool, resolve_degree)
from mc_v5 import (prereqs_met_v5, pool_and_ob_v5, score_action_v5,
                   list_candidate_actions_v5)
from mc_v6 import apply_outcome_v6, PARAMS
from mc_v8 import reset_seasonal_v8

Faction.reset_seasonal = reset_seasonal_v8

ADJACENCY = {
    'T1':  {'T2', 'T5', 'T14', 'T16'},
    'T2':  {'T1', 'T3', 'T9', 'T14'},
    'T3':  {'T2', 'T9', 'T17'},
    'T4':  {'T7', 'T12', 'T14'},
    'T5':  {'T1', 'T6', 'T14'},
    'T6':  {'T5', 'T13', 'T15'},
    'T7':  {'T4', 'T8'},
    'T8':  {'T7', 'T9', 'T10', 'T17'},
    'T9':  {'T2', 'T3', 'T8', 'T14', 'T17'},
    'T10': {'T8', 'T11'},
    'T11': {'T10', 'T12'},
    'T12': {'T4', 'T11', 'T13'},
    'T13': {'T6', 'T12', 'T15'},
    'T14': {'T1', 'T2', 'T4', 'T5', 'T9'},
    'T15': {'T6', 'T13'},
    'T16': {'T1'},
    'T17': {'T3', 'T8', 'T9'},
}

# Starting territory counts (for Crown constitutional restoration check)
STARTING_TERRITORIES = {'Crown': 6, 'Hafenmark': 4, 'Church': 1, 'Varfell': 4}

V12_PARAMS = dict(PARAMS)
V12_PARAMS.update(
    CONSENT_RATE=0.5,
    TURMOIL_CAP=12,
    CAMPAIGN_SEASONS=50,
    TREATY_LAPSE_RATE=0.5,
    # Einhir Revival — gated by Varfell national Influence
    EINHIR_I_GATE=4,              # Varfell I must reach this (starts at 4)
    EINHIR_PT_OB_WEIGHT=1,        # Each PT point adds this to Ob
    # Restoration Movement — independent PT decay
    RM_BASE_STRENGTH=1,           # Starting RM strength
    RM_GROWTH_PER_ARC=1,          # RM gets stronger each arc
    RM_PT_DECAY_CHANCE=0.3,       # Per-territory chance of PT decay per arc
    RM_VARFELL_COOPTION_BONUS=0.1,# Extra decay chance if Varfell adjacent + I >= gate
    # Altonian Reinforcements — automatic at arc boundary
    ALTONIAN_I_GATE=5,            # Harder gate — real diplomatic weight needed
    ALTONIAN_MIL_GAIN=1,          # Mil gain on Overwhelming only
    # Parliamentary Transfer — requires CB + majority
    PARL_REQUIRE_CB=True,
    PARL_MAJORITY_OB_BONUS=2,     # Extra Ob vs military (harder to convince majority)
)


def adjacent_territories(faction, world):
    adj = set()
    for tid in faction.territories:
        for neighbor in ADJACENCY.get(tid, set()):
            if neighbor not in faction.territories and neighbor in world.territories:
                adj.add(neighbor)
    return adj


def has_cb_against(actor, target_faction, world):
    """Check if actor has Casus Belli against target faction."""
    # CB sources: existing CB flag, or prior hostile action, or diplomatic incident
    cbs = getattr(actor, 'casus_belli', set())
    if target_faction.name in cbs:
        return True
    # Crown special: auto-justified when below starting territory count
    if actor.name == 'Crown' and len(actor.territories) < STARTING_TERRITORIES.get('Crown', 6):
        return True
    return False


# ============================================================
# PREREQS
# ============================================================
def v12_prereqs(action, world):
    actor = action['actor']
    name = action['name']
    p = world.params

    if name == 'Ecclesiastical Appointment':
        if actor.name != 'Church': return False
        if actor.stats['L'] >= 7: return False
        if getattr(actor, 'ecclesiastical_appointment_arc_used', False): return False
        if getattr(actor, 'ea_last_arc', -10) >= world.arc: return False
        return True

    if name == 'Crown Initiative':
        if actor.name != 'Crown': return False
        if getattr(actor, 'senator_inward_used', False): return False
        if actor.stats['W'] < 3: return False
        return True

    if name == "Vaynard's Settlement":
        if actor.name != 'Varfell': return False
        if getattr(actor, 'tribune_card_used', False): return False
        target = action.get('target')
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner != 'Varfell' or t.accord >= 2: return False
        if actor.stats['Mil'] < 3 or actor.stats['W'] < 1: return False
        return True

    if name == "Vaynard's Hall":
        if actor.name != 'Varfell': return False
        if getattr(actor, 'hall_card_used', False): return False
        if actor.stats['Mil'] < 3 or actor.stats['W'] < 1: return False
        return True

    if name == 'Charter of Liberties':
        if actor.name != 'Hafenmark': return False
        if getattr(actor, 'legacy_card_used', False): return False
        if actor.stats['W'] < 1: return False
        return True

    if name == 'Einhir Revival':
        if actor.name != 'Varfell': return False
        if getattr(actor, 'einhir_arc_used', False): return False
        # Gated by national Influence, not Legitimacy
        if actor.stats['I'] < p.get('EINHIR_I_GATE', 4): return False
        target = action.get('target')
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner == 'Varfell': return False
        if target not in adjacent_territories(actor, world): return False
        return True

    if name == 'Parliamentary Transfer':
        if getattr(actor, 'parl_transfer_arc_used', False): return False
        target = action.get('target')
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner == actor.name or t.owner is None: return False
        holder = world.factions.get(t.owner)
        if not holder: return False
        if len(holder.territories) <= 1: return False  # Can't strip last territory
        # MUST have Casus Belli against holder
        if p.get('PARL_REQUIRE_CB', True):
            if not has_cb_against(actor, holder, world):
                return False
        return True

    return prereqs_met_v5(action, world)


# ============================================================
# POOL / OB
# ============================================================
def v12_pool_ob(action, world):
    actor = action['actor']
    name = action['name']
    p = world.params

    if name == 'Crown Initiative':
        sum_accord = sum(world.territories[tid].accord
                         for tid in actor.territories if tid in world.territories)
        return actor.stats['I'], max(1, sum_accord // 2)
    if name == "Vaynard's Settlement":
        return actor.stats['Mil'] + (actor.stats['W'] // 2), 3
    if name == "Vaynard's Hall":
        return actor.stats['Mil'] + (1 if getattr(actor, 'revelation_tokens', 0) >= 1 else 0), 3
    if name == 'Charter of Liberties':
        token_bonus = sum(1 for v in actor.tokens_held.values() if v > 0)
        return actor.stats['I'] + token_bonus, 4

    if name == 'Einhir Revival':
        target_tid = action['target']
        t = world.territories[target_tid]
        pt_weight = p.get('EINHIR_PT_OB_WEIGHT', 1)
        if t.owner is None:
            # Uncontrolled — base Ob + PT resistance
            return actor.stats['I'], max(1, 1 + t.pt * pt_weight)
        holder = world.factions.get(t.owner)
        holder_sta = holder.stats['Sta'] if holder else 2
        # Ob = holder defense + PT resistance (Church-influenced territories harder)
        return actor.stats['I'], max(1, holder_sta // 2 + 1 + t.pt * pt_weight)

    if name == 'Parliamentary Transfer':
        target_tid = action['target']
        t = world.territories[target_tid]
        holder = world.factions.get(t.owner)
        holder_l = holder.stats['L'] if holder else 3
        majority_bonus = p.get('PARL_MAJORITY_OB_BONUS', 2)
        # I vs holder L + majority burden — much harder than military
        return actor.stats['I'], holder_l + majority_bonus

    return pool_and_ob_v5(action, world)


# ============================================================
# APPLY OUTCOMES
# ============================================================
def v12_apply(action, degree, world):
    actor = action['actor']
    name = action['name']
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Ecclesiastical Appointment':
        actor.ecclesiastical_appointment_arc_used = True
        actor.ea_last_arc = world.arc
        if success: actor.stats['L'] = min(7, actor.stats['L'] + 1)
        return

    if name == 'Crown Initiative':
        actor.senator_inward_used = True
        actor.stats['W'] = max(0, actor.stats['W'] - 3)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
            for tid in actor.territories:
                t = world.territories[tid]
                if t.accord == 1: t.accord = 2
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            if actor.territories:
                worst = min((world.territories[tid] for tid in actor.territories),
                            key=lambda t: t.accord)
                worst.accord = min(3, worst.accord + 1)
        elif degree == 'Partial':
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        return

    if name == "Vaynard's Settlement":
        actor.tribune_card_used = True
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        t = world.territories[action['target']]
        if overwhelming:
            t.accord = min(3, t.accord + 2); t.order = min(5, t.order + 1)
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
        elif degree == 'Success':
            t.accord = min(3, t.accord + 1); t.order = min(5, t.order + 1)
        elif degree == 'Partial':
            t.order = min(5, t.order + 1)
        return

    if name == "Vaynard's Hall":
        actor.hall_card_used = True
        actor.stats['Mil'] = max(1, actor.stats['Mil'] - 1)
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            rivals = [(f, f.stats['L']) for f in world.factions.values() if f.name != actor.name]
            if rivals:
                victim = max(rivals, key=lambda x: x[1])[0]
                victim.stats['L'] = max(1, victim.stats['L'] - 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            if getattr(actor, 'revelation_tokens', 0) >= 1:
                actor.revelation_tokens -= 1
                actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Partial':
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
        return

    if name == 'Charter of Liberties':
        actor.legacy_card_used = True
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 2)
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 1)
            token_count = sum(1 for v in actor.tokens_held.values() if v > 0)
            if token_count >= 2:
                actor.stats['L'] = min(7, actor.stats['L'] + 1)
        elif degree == 'Partial':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        return

    if name == 'Einhir Revival':
        actor.einhir_arc_used = True
        target_tid = action['target']
        t = world.territories[target_tid]
        old_owner = t.owner
        if overwhelming:
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
                world.factions[old_owner].stats['L'] = max(1, world.factions[old_owner].stats['L'] - 1)
            t.owner = 'Varfell'; actor.territories.add(target_tid)
            t.accord = 2; t.pt = max(0, t.pt - 1)
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        elif degree == 'Success':
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
            t.owner = 'Varfell'; actor.territories.add(target_tid)
            t.accord = 1; t.pt = max(0, t.pt - 1)
        elif degree == 'Partial':
            t.pt = max(0, t.pt - 1)  # RM cultural influence spreads
            if not hasattr(actor, 'casus_belli'): actor.casus_belli = set()
            if old_owner: actor.casus_belli.add(old_owner)
        # Failure: population wasn't ready. No backlash — cultural play.
        return

    if name == 'Parliamentary Transfer':
        actor.parl_transfer_arc_used = True
        target_tid = action['target']
        t = world.territories[target_tid]
        old_owner = t.owner
        # Consume CB
        if hasattr(actor, 'casus_belli') and old_owner in actor.casus_belli:
            actor.casus_belli.discard(old_owner)
        if overwhelming:
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
                world.factions[old_owner].stats['L'] = max(1, world.factions[old_owner].stats['L'] - 1)
            t.owner = actor.name; actor.territories.add(target_tid); t.accord = 1
        elif degree == 'Success':
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
            t.owner = actor.name; actor.territories.add(target_tid); t.accord = 1
        elif degree == 'Partial':
            # Failed but close — generates CB for next attempt
            if not hasattr(actor, 'casus_belli'): actor.casus_belli = set()
            if old_owner: actor.casus_belli.add(old_owner)
        else:
            actor.stats['Sta'] = max(1, actor.stats['Sta'] - 1)
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].stats['L'] = min(7, world.factions[old_owner].stats['L'] + 1)
        return

    apply_outcome_v6(action, degree, world)


# ============================================================
# SCORING
# ============================================================
def v12_score(action, world):
    name = action['name']; actor = action['actor']
    if name == 'Crown Initiative':
        return 4 + max(0, 6 - actor.stats['L']) + (3 if actor.stats['L'] <= 3 else 0)
    if name == "Vaynard's Settlement": return 12
    if name == "Vaynard's Hall": return 9 + max(0, 6 - actor.stats['L'])
    if name == 'Charter of Liberties': return 8 + max(0, 6 - actor.stats['L'])
    if name == 'Einhir Revival':
        t = world.territories[action['target']]
        # Only attempt when PT is genuinely low — "little to no piety"
        if t.pt >= 3: return 1  # Almost never choose against high-PT
        if t.pt == 2: return 5  # Low priority
        # PT 0-1: high priority — RM has done its work
        return 14 + (4 if t.owner is None else 0) + (3 if t.pt == 0 else 0)
    if name == 'Parliamentary Transfer':
        holder = world.factions.get(world.territories[action['target']].owner)
        weakness = max(0, 5 - (holder.stats['L'] if holder else 3))
        return 10 + weakness
    return score_action_v5(action, world)


# ============================================================
# CANDIDATE LISTING
# ============================================================
def v12_list_candidates(faction, world):
    cands = list_candidate_actions_v5(faction, world)
    if faction.name == 'Crown':
        a = dict(name='Crown Initiative', actor=faction, target=None)
        if v12_prereqs(a, world): cands.append(a)
    elif faction.name == 'Varfell':
        for tid, t in world.territories.items():
            if t.owner == 'Varfell' and t.accord < 2:
                a = dict(name="Vaynard's Settlement", actor=faction, target=tid)
                if v12_prereqs(a, world): cands.append(a)
        a2 = dict(name="Vaynard's Hall", actor=faction, target=None)
        if v12_prereqs(a2, world): cands.append(a2)
        for tid in adjacent_territories(faction, world):
            a = dict(name='Einhir Revival', actor=faction, target=tid)
            if v12_prereqs(a, world): cands.append(a)
    elif faction.name == 'Hafenmark':
        a = dict(name='Charter of Liberties', actor=faction, target=None)
        if v12_prereqs(a, world): cands.append(a)
    # Parliamentary Transfer — all factions (requires CB)
    for tid, t in world.territories.items():
        if t.owner and t.owner != faction.name and t.owner in world.factions:
            a = dict(name='Parliamentary Transfer', actor=faction, target=tid)
            if v12_prereqs(a, world): cands.append(a)
    return cands


def v12_select_actions(faction, world, n_actions=3):
    selected = []; used = set()
    for _ in range(n_actions):
        cands = v12_list_candidates(faction, world)
        cands = [a for a in cands if (a['name'], a.get('target')) not in used]
        if not cands: break
        scored = [(v12_score(a, world), a) for a in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used.add((chosen['name'], chosen.get('target')))
    return selected


# ============================================================
# VICTORY
# ============================================================
def universal_victory_v12(world, turmoil_cap, threshold):
    for fname, f in world.factions.items():
        territories_controlled = set()
        for tid in ALL_PLAYABLE_15:
            t = world.territories.get(tid)
            if t is None: continue
            if t.owner == fname:
                territories_controlled.add(tid)
            elif t.owner in world.factions:
                rival = world.factions[t.owner]
                tt = f.treaties.get(rival.name, '')
                if tt in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                    territories_controlled.add(tid)
                elif rival.submitted: territories_controlled.add(tid)
                elif rival.stats['L'] <= 1 and f.stats['L'] >= 5:
                    territories_controlled.add(tid)
        if len(territories_controlled) < threshold:
            f.sovereignty_history = 0; continue
        if not all(world.territories[tid].accord >= 2
                   for tid in world.territories_owned_by(fname)):
            f.sovereignty_history = 0; continue
        if world.turmoil() > turmoil_cap:
            f.sovereignty_history = 0; continue
        f.sovereignty_history += 1
        if f.sovereignty_history >= 2: return fname
    return None


# ============================================================
# ARC BOUNDARY — Treaty Expiration, RM, Altonian
# ============================================================
def arc_boundary_v12(world):
    p = world.params

    # Treaty Expiration
    crown = world.factions.get('Crown')
    if crown:
        lapse_rate = p.get('TREATY_LAPSE_RATE', 0.5)
        for rival_name in list(crown.treaties.keys()):
            if crown.treaties[rival_name] == 'CrownTreaty':
                if random.random() < lapse_rate:
                    del crown.treaties[rival_name]
                    rival = world.factions.get(rival_name)
                    if rival and 'Crown' in rival.treaties:
                        del rival.treaties['Crown']

    # Restoration Movement — independent PT decay
    rm_base = p.get('RM_BASE_STRENGTH', 1)
    rm_growth = p.get('RM_GROWTH_PER_ARC', 1)
    rm_chance = p.get('RM_PT_DECAY_CHANCE', 0.3)
    cooption_bonus = p.get('RM_VARFELL_COOPTION_BONUS', 0.1)
    # RM gets stronger over time
    rm_strength = rm_base + rm_growth * (world.arc - 1)
    # Scale chance by strength (capped at 0.8 to avoid certainty)
    effective_chance = min(0.8, rm_chance * rm_strength)

    varfell = world.factions.get('Varfell')
    varfell_adj = adjacent_territories(varfell, world) if varfell else set()
    varfell_coopts = (varfell and varfell.stats['I'] >= p.get('EINHIR_I_GATE', 4))

    for tid, t in world.territories.items():
        if t.pt <= 0: continue
        if t.owner == 'Church': continue  # Church holds the line in own territories
        # Inquisitors resist RM in their territory
        if any(tid in f.inquisitors for f in world.factions.values()
               if f.name == 'Church'): continue
        chance = effective_chance
        # Varfell co-option bonus
        if varfell_coopts and tid in varfell_adj:
            chance = min(0.9, chance + cooption_bonus * rm_strength)
        if random.random() < chance:
            t.pt = max(0, t.pt - 1)

    # Altonian Reinforcements — automatic for Hafenmark
    ha = world.factions.get('Hafenmark')
    if ha and ha.stats['I'] >= p.get('ALTONIAN_I_GATE', 4):
        pool = ha.stats['I']
        net = roll_pool(pool) - 3
        degree = resolve_degree(net)
        mil_gain = p.get('ALTONIAN_MIL_GAIN', 1)
        if degree == 'Overwhelming':
            ha.stats['Mil'] = min(7, ha.stats['Mil'] + mil_gain)
        # Success/Partial: no permanent gain (temporary support only)

    # Generate CB from existing hostile situations
    for fname, f in world.factions.items():
        if not hasattr(f, 'casus_belli'): f.casus_belli = set()
        # Factions with territories under low accord generate CB for the territory holder
        for tid in f.territories:
            t = world.territories.get(tid)
            if t and t.accord <= 1:
                # Adjacent factions gain CB (instability = justification)
                for neighbor_tid in ADJACENCY.get(tid, set()):
                    nt = world.territories.get(neighbor_tid)
                    if nt and nt.owner and nt.owner != fname and nt.owner in world.factions:
                        other = world.factions[nt.owner]
                        if not hasattr(other, 'casus_belli'): other.casus_belli = set()
                        other.casus_belli.add(fname)

    # Reset arc-level flags
    for f in world.factions.values():
        f.pa_session_arc_used = False
        f.influence_surge_arc_used = False
        f.ecclesiastical_appointment_arc_used = False
        f.parl_transfer_arc_used = False
        f.einhir_arc_used = False


# ============================================================
# END OF SEASON
# ============================================================
def end_of_season_v12(world, turmoil_cap, threshold):
    world.clocks['CI'] += 1
    world.clocks['MS'] = max(0, world.clocks['MS'] - 1)
    revolts = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        if t.accord == 1 and not t.garrison: t.accord = 0
        if t.accord == 0:
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolts += 1
            if t.garrison:
                c = world.factions.get(t.owner)
                if c and (roll_pool(c.stats['Mil']) - 2) >= 1: t.accord = 1
                else:
                    if t.owner in world.factions:
                        world.factions[t.owner].territories.discard(tid)
                    t.owner = None; t.garrison = False; t.inquisitor_holder = None
                    for ff in world.factions.values(): ff.inquisitors.discard(tid)
            else:
                if t.owner in world.factions:
                    world.factions[t.owner].territories.discard(tid)
                t.owner = None; t.inquisitor_holder = None
        if t.garrison and world.season - getattr(t, 'last_hostile_season', 0) >= 2:
            t.consec_passive_seasons = getattr(t, 'consec_passive_seasons', 0) + 1
            if t.consec_passive_seasons >= 2 and t.accord < 2:
                t.accord += 1; t.consec_passive_seasons = 0
        else: t.consec_passive_seasons = 0
    if revolts == 0:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - 1)
    world.clocks['Strain'] = world.clocks['Turmoil']
    for fname, f in world.factions.items():
        if f.stats['Sta'] <= 2:
            for tid in list(f.territories):
                world.territories[tid].accord = max(0, world.territories[tid].accord - 1)
    winner = universal_victory_v12(world, turmoil_cap, threshold)
    if winner: world.winner = winner


# ============================================================
# RUN
# ============================================================
def run_season_v12(world, threshold):
    if world.winner: return
    for f in world.factions.values():
        f.reset_seasonal()
        f.hall_card_used = False
    acts = []
    for f in world.factions.values():
        acts.extend(v12_select_actions(f, world, n_actions=3))
    for action in acts:
        if not v12_prereqs(action, world): continue
        pool, ob = v12_pool_ob(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        v12_apply(action, degree, world)
    end_of_season_v12(world, world.params['TURMOIL_CAP'], threshold)
    world.season += 1
    if world.season % 4 == 0:
        arc_boundary_v12(world)
        world.arc += 1


def run_campaign_v12(params=None, seed=None, threshold=11):
    if seed is not None: random.seed(seed)
    p = dict(V12_PARAMS); p.update(params or {})
    world = init_world(tweaks=set())
    world.params = p
    # Init CB sets
    for f in world.factions.values():
        f.casus_belli = set()
    almud_history = []
    for _ in range(p['CAMPAIGN_SEASONS']):
        if world.winner: break
        run_season_v12(world, threshold)
        crown = world.factions['Crown']
        almud_history.append(dict(Sta=crown.stats['Sta'], L=crown.stats['L']))
    winner = world.winner
    if winner is None:
        scores = {}
        for fname, f in world.factions.items():
            h = 0
            for tid in ALL_PLAYABLE_15:
                t = world.territories.get(tid)
                if t and t.owner == fname: h += 1
                elif t and t.owner in world.factions:
                    if f.treaties.get(t.owner, '') in ('CrownTreaty', 'Peace', 'Alliance',
                                                        'Capitulation', 'Tributary'):
                        h += 0.5
            scores[fname] = h * 10 + f.stats['L'] + len(f.territories)
        winner = max(scores, key=scores.get)
    almud_state = 'stable'
    if any(h['Sta'] == 0 for h in almud_history):
        almud_state = 'deposed-submission'
    elif sum(1 for h in almud_history[-6:] if h['L'] <= 1) >= 2:
        almud_state = 'deposed-mandate-collapse'
    elif almud_history and almud_history[-1]['Sta'] >= 4 and almud_history[-1]['L'] >= 5:
        almud_state = 'strong'
    elif almud_history and (almud_history[-1]['Sta'] <= 2 or almud_history[-1]['L'] <= 2):
        almud_state = 'weak'
    return dict(winner=winner, almud_state=almud_state, world=world)


def run_mc_v12(n, params=None, threshold=11):
    wins = Counter(); states = Counter()
    L = defaultdict(list); terr = defaultdict(list)
    direct = 0; turmoil = []
    for i in range(n):
        r = run_campaign_v12(params=params, seed=i, threshold=threshold)
        wins[r['winner']] += 1; states[r['almud_state']] += 1
        for fname, f in r['world'].factions.items():
            L[fname].append(f.stats['L']); terr[fname].append(len(f.territories))
        if r['world'].winner: direct += 1
        turmoil.append(r['world'].clocks['Turmoil'])
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total*100, 1)
                   for k in ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        L_mean={k: round(sum(v)/len(v), 2) for k, v in L.items()},
        terr_mean={k: round(sum(v)/len(v), 2) for k, v in terr.items()},
        direct_rate=round(direct/n*100, 1),
        turmoil_mean=round(sum(turmoil)/len(turmoil), 2),
        almud_strong=round(states.get('strong', 0)/n*100, 1),
        almud_deposed=round(sum(v for k, v in states.items()
                                if k.startswith('deposed'))/n*100, 1),
    )


def deviation_from_equal(ws):
    return sum(abs(v - 25.0) for v in ws.values())
