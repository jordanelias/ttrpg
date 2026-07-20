"""
Simulator v5 — Card-slot caps + canonical Crown Treaty + Appease defense + 36s campaigns

v4 → v5 corrections:
- Dynastic Proclamation: 1× per season (canonical "once per season")
- Crown Treaty: 1× per season (Senator Outward card)
- Diplomat Card (place Tokens): 1× per season (Diplomat card slot — shared with DP slot)
- Cardinal Focus: 1× per season (already had)
- Crown Treaty Ob: floor(target Mandate / 2) + 1 (canonical §5.1, not target L)
- Defensive Appease: target faction with Mandate ≥ 4 can cancel Crown Treaty / DP
  at cost of Mandate −1
- PT ≤ 1 modifier on DP: +1 Ob
- 36-season campaigns (was 24) — Peninsular Sovereignty harder to reach
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (CANONICAL_TERRITORIES, ALL_PLAYABLE_15, Faction, Territory,
                   World, make_action, init_world, roll_pool, resolve_degree,
                   universal_victory_check)


def reset_seasonal_v5(self):
    self.royal_guard_available = True
    self.cardinal_focus_used_this_season = False
    self.diplomat_card_used = False  # NEW: 1× per season slot shared by DP + Token
    self.senator_card_used = False  # NEW: 1× per season slot for Crown Treaty
Faction.reset_seasonal = reset_seasonal_v5


def prereqs_met_v5(action, world):
    name = action['name']; actor = action['actor']; target = action.get('target')
    if name == 'Royal Decree':
        return actor.name == 'Crown'
    if name == 'Royal Charter':
        return actor.name == 'Crown' and target in actor.territories
    if name == 'Crown Treaty':
        if actor.name != 'Crown' or target not in world.factions: return False
        if actor.name == target: return False
        # 1× per season Senator slot
        if getattr(actor, 'senator_card_used', False): return False
        return actor.treaties.get(target, '') == ''
    if name == 'Outreach to Schoenland':
        return actor.name == 'Crown' and world.clocks['IP'] < 30
    if name == 'Cardinal Focus':
        return actor.name == 'Church' and not actor.cardinal_focus_used_this_season
    if name == 'Piety Spread':
        return (actor.name == 'Church' and target in world.territories and
                world.territories[target].owner not in (None, 'Church'))
    if name == 'Active Inquisition':
        if actor.name != 'Church' or target not in world.territories: return False
        t = world.territories[target]
        threshold = 3
        if actor.cardinal_focus == 'Justice' and len(actor.inquisitors) == 0:
            threshold = 2
        if t.ap < threshold: return False
        if t.inquisitor_holder: return False
        if 'T-09c' in world.tweaks and len(actor.inquisitors) >= 2: return False
        return True
    if name == 'Church Seizure':
        if actor.name != 'Church' or target not in world.territories: return False
        t = world.territories[target]
        if t.is_uncontrolled(): return False
        if world.clocks['CI'] < 40: return False
        if actor.stats['L'] < 4: return False
        controller = world.factions.get(t.owner)
        if controller is None: return False
        if actor.stats['L'] <= controller.stats['L']: return False
        return True
    if name == 'Excommunication':
        return (actor.name == 'Church' and target in world.factions and target != 'Church')
    if name == 'Ecclesiastical Appointment':
        return actor.name == 'Church' and actor.stats['L'] < 7
    if name == 'Diplomat Card':
        if actor.name != 'Hafenmark': return False
        if target not in world.factions: return False
        if target == 'Hafenmark': return False
        # 1× per season Diplomat slot (shared with DP)
        if getattr(actor, 'diplomat_card_used', False): return False
        return True
    if name == 'Parliamentary Session':
        return actor.name == 'Hafenmark' and not actor.pa_session_arc_used
    if name == 'Dynastic Proclamation':
        if actor.name != 'Hafenmark': return False
        # 1× per season Diplomat slot (canonical)
        if getattr(actor, 'diplomat_card_used', False): return False
        if actor.stats['L'] < 4: return False
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner is None or t.owner not in world.factions: return False
        controller = world.factions[t.owner]
        if actor.stats['L'] <= controller.stats['L']: return False
        # Adjacency: simplification — assume Hafenmark can reach if they have any territory
        # (proper modeling needs adjacency graph; for now require Hafenmark holds adjacent
        # territory of similar number-range)
        return True
    if name == 'Counter-Narrative':
        return actor.name == 'Varfell' and target in world.territories
    if name == 'Spy':
        return target in world.factions and target != actor.name
    if name == 'Trade':
        return actor.stats['W'] < 8 and len(actor.territories) > 0
    if name == 'Govern':
        return target in actor.territories
    if name == 'Muster':
        return target in actor.territories
    if name == 'Tribune Network':
        return actor.name == 'Varfell'
    if name == 'Military Conquest':
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner == actor.name: return False
        return actor.stats['Mil'] >= 3
    return False


def pool_and_ob_v5(action, world):
    name = action['name']; actor = action['actor']; target = action.get('target')
    if name == 'Royal Decree':
        return actor.stats['I'], 2 + actor.consec_decree
    if name == 'Royal Charter':
        t = world.territories[target]
        ob = (t.prosperity // 2) + 1
        if 'T-01a' in world.tweaks: ob += len(actor.charters)
        return actor.stats['L'], max(1, ob)
    if name == 'Crown Treaty':
        # §5.1 CANONICAL: Pool=I, Ob=floor(target Mandate/2)+1
        return actor.stats['I'], (world.factions[target].stats['L'] // 2) + 1
    if name == 'Outreach to Schoenland':
        return actor.stats['I'], 2
    if name == 'Cardinal Focus':
        return actor.stats['L'], 1
    if name == 'Piety Spread':
        return actor.stats['L'], 2
    if name == 'Active Inquisition':
        t = world.territories[target]
        return actor.stats['L'], (t.order // 2) + 1
    if name == 'Church Seizure':
        t = world.territories[target]
        pool = actor.stats['I'] + (world.clocks['CI'] // 15)
        ob = max(1, 10 - t.pt - 0)
        if world.clocks['CI'] >= 80: ob = max(1, ob - 1)
        return pool, ob
    if name == 'Excommunication':
        return actor.stats['L'], world.factions[target].stats['L']
    if name == 'Ecclesiastical Appointment':
        return actor.stats['L'], 2
    if name == 'Diplomat Card':
        return actor.stats['I'], (world.factions[target].stats['L'] // 2) + 1
    if name == 'Parliamentary Session':
        return actor.stats['L'], 3
    if name == 'Dynastic Proclamation':
        # §5.3: Ob = floor(target faction Sta/2) + 1; PT ≤ 1: +1 Ob; Token on target: -1 Ob
        t = world.territories[target]
        target_faction = world.factions.get(t.owner)
        if target_faction is None: return actor.stats['I'], 3
        ob = (target_faction.stats['Sta'] // 2) + 1
        if t.pt <= 1: ob += 1
        if actor.tokens_held.get(t.owner, 0) > 0: ob -= 1
        return actor.stats['I'], max(1, ob)
    if name == 'Counter-Narrative':
        t = world.territories[target]
        if t.owner not in world.factions: return actor.stats['I'], 3
        owner = world.factions[t.owner]
        base = (owner.stats['L'] // 2) + 1 - 1
        if t.inquisitor_holder:
            if 'T-02a' in world.tweaks and t.first_cn_attempted_this_arc:
                pass
            else:
                base += 2
                t.first_cn_attempted_this_arc = True
        return actor.stats['I'], max(1, base)
    if name == 'Spy':
        return actor.stats['Int'], (world.factions[target].stats['Int'] // 2) + 1
    if name == 'Trade':
        return actor.stats['W'] + 1, 2
    if name == 'Govern':
        t = world.territories[target]
        ob = (t.prosperity // 2) + 1
        if target in actor.charters: ob = max(1, ob - 2)
        return actor.stats['L'], ob
    if name == 'Muster':
        return actor.stats['Mil'], 2
    if name == 'Tribune Network':
        return actor.stats['Int'], 3
    if name == 'Military Conquest':
        t = world.territories[target]
        return actor.stats['Mil'], 3 if t.garrison else 2
    return 3, 3


def appease_choice(target_faction, action_type, world):
    """Defensive Appease (PP-189): target with Mandate ≥ 4 can pay −1 Mandate to cancel.
    AI decision: appease if losing the Mandate is better than losing the action's effect.
    """
    if target_faction.stats['L'] < 4: return False  # can't appease
    # Appease if: action would cost more than 1 Mandate or 1 territory
    if action_type in ('Crown Treaty', 'Dynastic Proclamation'):
        # Appease — likely a good trade vs becoming Treaty-bound or losing a territory
        target_faction.stats['L'] -= 1
        return True
    return False


def apply_outcome_v5(action, degree, world):
    """Apply effects, with card-slot tracking + Appease defense."""
    name = action['name']; actor = action['actor']; target = action.get('target')
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Royal Decree':
        actor.consec_decree += 1
        if success: actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
    elif name == 'Royal Charter':
        if success: actor.charters.add(target)
    elif name == 'Crown Treaty':
        actor.senator_card_used = True  # consume slot
        # Defensive Appease check (target may cancel)
        if success and target in world.factions:
            tf = world.factions[target]
            if appease_choice(tf, 'Crown Treaty', world):
                return  # cancelled
            # GAP-05 consent gap also still applies (target may refuse)
            if random.random() < 0.5:  # 50% consent (no canonical rule yet)
                actor.treaties[target] = 'CrownTreaty'
                tf.treaties[actor.name] = 'CrownTreaty'
                actor.stats['L'] = min(7, actor.stats['L'] + 1)
    elif name == 'Outreach to Schoenland':
        if success: world.clocks['IP'] = max(0, world.clocks['IP'] - 2)
    elif name == 'Cardinal Focus':
        actor.cardinal_focus = random.choice(['Justice', 'Prudence', 'Temperance', 'Fortitude'])
        actor.cardinal_focus_used_this_season = True
    elif name == 'Piety Spread':
        if overwhelming: world.territories[target].ap += 3
        elif degree == 'Success': world.territories[target].ap += 2
        elif degree == 'Partial': world.territories[target].ap += 1
    elif name == 'Active Inquisition':
        if success:
            t = world.territories[target]
            t.inquisitor_holder = 'Church'
            actor.inquisitors.add(target)
            t.ap = 0
            t.last_hostile_season = world.season
            t.order = max(0, t.order - 1)
        elif degree == 'Partial':
            world.territories[target].ap += 1
    elif name == 'Church Seizure':
        t = world.territories[target]
        # Defensive: Institutional Mandate Appease (PP-189) — controller may cancel
        controller = world.factions.get(t.owner)
        if controller and controller.stats['L'] >= 4 and random.random() < 0.7:
            # 70% likely to Appease when Mandate ≥ 4 (Seizure costs territory; Appease costs L)
            controller.stats['L'] -= 1
            return
        if overwhelming:
            new_accord = min(3, (t.pt // 2) + 2)
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
            t.owner = 'Church'; actor.territories.add(target)
            t.accord = new_accord
            if old: t.cb_against.add(old)
        elif degree == 'Success':
            new_accord = max((t.pt // 2) + 1, 2)
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
            t.owner = 'Church'; actor.territories.add(target)
            t.accord = new_accord
            if old: t.cb_against.add(old)
        elif degree == 'Partial':
            t.accord = 1
            if t.owner: t.cb_against.add(actor.name)
        elif degree == 'Failure':
            if t.owner: t.cb_against.add(actor.name)
    elif name == 'Excommunication':
        if success: world.factions[target].stats['L'] = max(1, world.factions[target].stats['L'] - 1)
        else: actor.stats['Sta'] = max(0, actor.stats['Sta'] - 1)
    elif name == 'Ecclesiastical Appointment':
        if success: actor.stats['L'] = min(7, actor.stats['L'] + 1)
    elif name == 'Diplomat Card':
        actor.diplomat_card_used = True  # consume Diplomat slot
        if 'T-03c' in world.tweaks:
            actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if success:
            actor.tokens_held[target] += 1
            world.factions[target].tokens_received[actor.name] += 1
            world.clocks['PI'] += 1
    elif name == 'Parliamentary Session':
        actor.pa_session_arc_used = True
        support = 1
        for f in world.factions.values():
            if f.name == actor.name: continue
            if actor.tokens_held.get(f.name, 0) > 0:
                if random.random() < 0.6: support += 1
            elif f.name == 'Church': pass
            else:
                if random.random() < 0.4: support += 1
        if support >= 3:
            l_gain = 2 if 'T-X4' in world.tweaks else 1
            actor.stats['L'] = min(7, actor.stats['L'] + l_gain)
            world.clocks['PI'] += 2
            if 'T-X4' in world.tweaks:
                opps = [f for f in world.factions if f != actor.name]
                if opps:
                    tgt = random.choice(opps)
                    actor.tokens_held[tgt] += 1
                    world.factions[tgt].tokens_received[actor.name] += 1
    elif name == 'Dynastic Proclamation':
        actor.diplomat_card_used = True  # consume Diplomat slot
        t = world.territories[target]
        target_faction = world.factions.get(t.owner)
        if target_faction is None: return
        # Defensive: target may Appease (PP-189)
        if appease_choice(target_faction, 'Dynastic Proclamation', world):
            return
        if overwhelming:
            target_faction.territories.discard(target)
            t.owner = 'Hafenmark'
            actor.territories.add(target)
            t.accord = 2
            target_faction.stats['L'] = max(1, target_faction.stats['L'] - 1)
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        elif degree == 'Success':
            target_faction.territories.discard(target)
            t.owner = 'Hafenmark'
            actor.territories.add(target)
            t.accord = 2
            target_faction.stats['L'] = max(1, target_faction.stats['L'] - 1)
        elif degree == 'Partial':
            t.accord = max(0, t.accord - 1)
            t.cb_against.add(actor.name)
    elif name == 'Counter-Narrative':
        t = world.territories[target]
        if overwhelming:
            t.ap = max(0, t.ap - 3)
            if t.inquisitor_holder == 'Church' and 'T-02c' in world.tweaks:
                world.factions['Church'].inquisitors.discard(target)
                t.inquisitor_holder = None
            actor.revelation_tokens += 1
        elif degree == 'Success':
            t.ap = max(0, t.ap - 2)
        elif degree == 'Partial':
            t.ap = max(0, t.ap - 1)
    elif name == 'Spy':
        if target == 'Crown':
            v = world.factions['Crown']
            if v.royal_guard_available:
                v.royal_guard_available = False; return
        if success:
            world.factions[target].stats['Sta'] = max(0, world.factions[target].stats['Sta'] - 1)
            if actor.name == 'Varfell': actor.revelation_tokens += 1
        elif degree in ('Partial', 'Failure'):
            if 'T-09b' in world.tweaks and target == 'Varfell':
                v = world.factions['Varfell']
                if v.stats['Int'] >= 4:
                    if (roll_pool(v.stats['Int']) - 3) >= 1:
                        v.tokens_held[actor.name] += 1
    elif name == 'Trade':
        if success: actor.stats['W'] = min(8, actor.stats['W'] + 1)
    elif name == 'Govern':
        t = world.territories[target]
        t.last_govern_season = world.season
        if overwhelming:
            t.prosperity = min(5, t.prosperity + 1)
            actor.stats['W'] = min(8, actor.stats['W'] + 1)
            t.order = min(5, t.order + 2)
            t.accord = min(3, t.accord + 1)
        elif degree == 'Success':
            t.prosperity = min(5, t.prosperity + 1)
            actor.stats['W'] = min(8, actor.stats['W'] + 1)
            t.order = min(5, t.order + 1)
            t.accord = min(3, t.accord + 1)
    elif name == 'Muster':
        if success:
            t = world.territories[target]
            t.garrison = True
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
    elif name == 'Tribune Network':
        if success: actor.revelation_tokens += 1
    elif name == 'Military Conquest':
        if success:
            t = world.territories[target]
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
            t.owner = actor.name
            actor.territories.add(target)
            t.accord = 1
            world.clocks['MS'] = max(0, world.clocks['MS'] - 2)
            world.clocks['IP'] += 2


def score_action_v5(action, world):
    """v5 scoring — same as v4 conceptually."""
    name = action['name']; actor = action['actor']; target = action.get('target')
    s = 1
    if actor.name == 'Crown':
        if name == 'Royal Charter':
            if target not in actor.charters: s += 6
        elif name == 'Royal Decree':
            if actor.stats['Sta'] < 5: s += 6 - actor.consec_decree * 2
        elif name == 'Govern':
            t = world.territories[target]
            if target in actor.charters: s += 6
            if t.accord < 2: s += 9
            if t.prosperity < 4: s += 3
        elif name == 'Muster':
            t = world.territories[target]
            if t.accord <= 1 or not t.garrison: s += 7
        elif name == 'Crown Treaty':
            s += 11  # critical for hegemony
        elif name == 'Outreach to Schoenland':
            if world.clocks['IP'] > 25: s += 6
        elif name == 'Military Conquest':
            t = world.territories[target]
            if t.is_uncontrolled(): s += 8
    elif actor.name == 'Church':
        if name == 'Cardinal Focus': s += 6
        elif name == 'Piety Spread':
            t = world.territories[target]
            if not t.inquisitor_holder and not t.is_uncontrolled():
                s += 8
                if t.ap >= 3: s -= 3
        elif name == 'Active Inquisition':
            if world.territories[target].ap >= 3: s += 12
            if 'T-09c' in world.tweaks and len(actor.inquisitors) >= 2: s = -100
        elif name == 'Church Seizure':
            if world.clocks['CI'] >= 40 and actor.stats['L'] >= 4: s += 13
        elif name == 'Excommunication':
            if world.factions[target].stats['L'] < 5: s += 4
            else: s += 1
        elif name == 'Ecclesiastical Appointment':
            if actor.stats['L'] < 7: s += 9
        elif name == 'Govern':
            if world.territories[target].accord < 2: s += 7
            else: s += 3
        elif name == 'Trade': s += 3
    elif actor.name == 'Hafenmark':
        if name == 'Parliamentary Session':
            if not actor.pa_session_arc_used: s += 11
        elif name == 'Diplomat Card':
            tgt = world.factions[target]
            if tgt.stats['L'] == 4: s += 7
            elif tgt.stats['L'] == 5: s += 5
        elif name == 'Dynastic Proclamation':
            t = world.territories[target]
            target_faction = world.factions.get(t.owner)
            if target_faction:
                # Strong if mandate gap + adjacent + not too high PT
                gap = actor.stats['L'] - target_faction.stats['L']
                s += 8 + gap
                if t.pt <= 1: s -= 1
        elif name == 'Trade':
            if actor.stats['W'] < 7: s += 7
            else: s += 3
        elif name == 'Govern':
            if world.territories[target].accord < 2: s += 8
            else: s += 4
        elif name == 'Muster':
            t = world.territories[target]
            if not t.garrison: s += 6
    elif actor.name == 'Varfell':
        if name == 'Counter-Narrative':
            t = world.territories[target]
            if t.inquisitor_holder:
                if 'T-02a' in world.tweaks and t.first_cn_attempted_this_arc: s += 10
                else: s += 6
            elif t.ap >= 2: s += 8
            else: s += 2
        elif name == 'Spy':
            tgt = world.factions[target]
            if tgt.stats['Int'] <= 3: s += 8
            elif tgt.stats['Int'] == 4: s += 5
            else: s += 2
        elif name == 'Tribune Network': s += 6
        elif name == 'Govern':
            if world.territories[target].accord < 2: s += 9
            else: s += 3
        elif name == 'Muster':
            t = world.territories[target]
            if not t.garrison: s += 6
            if t.accord <= 1: s += 4
        elif name == 'Military Conquest':
            t = world.territories[target]
            if t.is_uncontrolled() and actor.stats['Mil'] >= 4: s += 9
            elif actor.stats['Mil'] >= 5: s += 5
        elif name == 'Trade': s += 3
    return s


def list_candidate_actions_v5(faction, world):
    cands = []
    name = faction.name
    if name == 'Crown':
        for tid in faction.territories:
            for an in ('Royal Charter', 'Govern', 'Muster'):
                cands.append(make_action(an, faction, target=tid))
        cands.append(make_action('Royal Decree', faction))
        for f in world.factions:
            if f != name:
                cands.append(make_action('Crown Treaty', faction, target=f))
                cands.append(make_action('Spy', faction, target=f))
        cands.append(make_action('Outreach to Schoenland', faction))
        for tid, t in world.territories.items():
            if t.is_uncontrolled():
                cands.append(make_action('Military Conquest', faction, target=tid))
    elif name == 'Church':
        cands.append(make_action('Cardinal Focus', faction))
        for tid, t in world.territories.items():
            if t.owner not in (None, 'Church'):
                cands.append(make_action('Piety Spread', faction, target=tid))
                if t.ap >= 3 and not t.inquisitor_holder:
                    cands.append(make_action('Active Inquisition', faction, target=tid))
                if (world.clocks['CI'] >= 40 and faction.stats['L'] >= 4 and
                    faction.stats['L'] > world.factions.get(t.owner, faction).stats['L']):
                    cands.append(make_action('Church Seizure', faction, target=tid))
        for f in world.factions:
            if f != 'Church':
                cands.append(make_action('Excommunication', faction, target=f))
                cands.append(make_action('Spy', faction, target=f))
        cands.append(make_action('Ecclesiastical Appointment', faction))
        if faction.territories:
            cands.append(make_action('Trade', faction))
        for tid in faction.territories:
            cands.append(make_action('Govern', faction, target=tid))
            cands.append(make_action('Muster', faction, target=tid))
    elif name == 'Hafenmark':
        if not faction.pa_session_arc_used:
            cands.append(make_action('Parliamentary Session', faction))
        for f in world.factions:
            if f != 'Hafenmark':
                cands.append(make_action('Diplomat Card', faction, target=f))
                cands.append(make_action('Spy', faction, target=f))
        # Dynastic Proclamation against any rival territory
        for tid, t in world.territories.items():
            if t.owner not in (None, 'Hafenmark'):
                controller = world.factions.get(t.owner)
                if (controller and faction.stats['L'] >= 4 and
                    faction.stats['L'] > controller.stats['L']):
                    cands.append(make_action('Dynastic Proclamation', faction, target=tid))
        cands.append(make_action('Trade', faction))
        for tid in faction.territories:
            cands.append(make_action('Govern', faction, target=tid))
            cands.append(make_action('Muster', faction, target=tid))
    elif name == 'Varfell':
        for tid, t in world.territories.items():
            if t.owner != 'Varfell' and not t.is_uncontrolled():
                cands.append(make_action('Counter-Narrative', faction, target=tid))
            if t.is_uncontrolled() and faction.stats['Mil'] >= 3:
                cands.append(make_action('Military Conquest', faction, target=tid))
        for f in world.factions:
            if f != 'Varfell':
                cands.append(make_action('Spy', faction, target=f))
        cands.append(make_action('Tribune Network', faction))
        cands.append(make_action('Trade', faction))
        for tid in faction.territories:
            cands.append(make_action('Govern', faction, target=tid))
            cands.append(make_action('Muster', faction, target=tid))
    return [a for a in cands if prereqs_met_v5(a, world)]


def select_actions_v5(faction, world, n_actions=3):
    selected = []
    used_targets = set()
    for _ in range(n_actions):
        cands = list_candidate_actions_v5(faction, world)
        cands = [a for a in cands if (a['name'], a.get('target')) not in used_targets]
        if not cands: break
        scored = [(score_action_v5(a, world), a) for a in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used_targets.add((chosen['name'], chosen.get('target')))
    return selected


def end_of_season_v5(world):
    world.clocks['CI'] += 1
    world.clocks['MS'] = max(0, world.clocks['MS'] - 1)
    revolts = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        if t.accord == 1 and not t.garrison:
            t.accord = 0
        if t.accord == 0:
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolts += 1
            if t.garrison:
                controller = world.factions[t.owner]
                if (roll_pool(controller.stats['Mil']) - 2) >= 1:
                    t.accord = 1
                else:
                    if t.owner in world.factions:
                        world.factions[t.owner].territories.discard(tid)
                    t.owner = None; t.garrison = False; t.inquisitor_holder = None
                    for f in world.factions.values(): f.inquisitors.discard(tid)
            else:
                if t.owner in world.factions:
                    world.factions[t.owner].territories.discard(tid)
                t.owner = None; t.inquisitor_holder = None
                for f in world.factions.values(): f.inquisitors.discard(tid)
        if (t.garrison and world.season - t.last_hostile_season >= 2):
            t.consec_passive_seasons += 1
            if t.consec_passive_seasons >= 2 and t.accord < 2:
                t.accord += 1; t.consec_passive_seasons = 0
        else:
            t.consec_passive_seasons = 0
    if revolts == 0:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - 1)
    world.clocks['Strain'] = world.clocks['Turmoil']
    for fname, f in world.factions.items():
        if f.stats['Sta'] <= 2:
            for tid in list(f.territories):
                world.territories[tid].accord = max(0, world.territories[tid].accord - 1)
    winner = universal_victory_check(world)
    if winner: world.winner = winner


def run_season_v5(world):
    if world.winner: return
    for f in world.factions.values(): f.reset_seasonal()
    all_acts = []
    for f in world.factions.values():
        all_acts.extend(select_actions_v5(f, world, n_actions=3))
    for action in all_acts:
        if not prereqs_met_v5(action, world): continue
        pool, ob = pool_and_ob_v5(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        apply_outcome_v5(action, degree, world)
    end_of_season_v5(world)
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            f.reset_arc(); f.reset_annual()
        world.arc += 1


def run_campaign_v5(tweaks=None, seasons=36, seed=None):
    if seed is not None: random.seed(seed)
    world = init_world(tweaks=tweaks)
    for _ in range(seasons):
        run_season_v5(world)
        if world.winner: break
    winner = world.winner
    if winner is None:
        scores = {}
        for fname, f in world.factions.items():
            hegemony = 0
            for tid in ALL_PLAYABLE_15:
                t = world.territories.get(tid)
                if t and t.owner == fname: hegemony += 1
                elif t and t.owner in world.factions:
                    treaty_type = f.treaties.get(t.owner, '')
                    if treaty_type in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                        hegemony += 0.5
            scores[fname] = hegemony * 10 + f.stats['L'] + len(f.territories)
        winner = max(scores, key=scores.get)
    return dict(winner=winner, world=world)


def run_mc_v5(n, tweaks=None, seasons=36):
    wins = Counter(); terr = defaultdict(list); inq = []; turmoil = 0
    direct = 0; lengths = []
    treaties = defaultdict(list)
    for i in range(n):
        r = run_campaign_v5(tweaks=tweaks, seasons=seasons, seed=i)
        wins[r['winner']] += 1
        for fname in r['world'].factions:
            terr[fname].append(len(r['world'].factions[fname].territories))
            treaties[fname].append(len(r['world'].factions[fname].treaties))
        inq.append(len(r['world'].factions['Church'].inquisitors))
        turmoil += r['world'].clocks['Turmoil']
        if r['world'].winner: direct += 1
        lengths.append(r['world'].season)
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total * 100, 1) for k in
                   ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        territory_means={k: round(sum(v)/len(v), 2) for k, v in terr.items()},
        treaty_means={k: round(sum(v)/len(v), 2) for k, v in treaties.items()},
        inq_mean=round(sum(inq)/len(inq), 2),
        turmoil_mean=round(turmoil/n, 2),
        direct_sovereignty_rate=round(direct/n * 100, 1),
        avg_length=round(sum(lengths)/len(lengths), 1),
    )


if __name__ == '__main__':
    N = 500
    SEASONS = 36
    configs = [
        ('canon-v5 (canonical rules + slot caps)', set()),
        ('T-09c only (cap Inq)', {'T-09c'}),
        ('T-02a only (Inq familiarity)', {'T-02a'}),
        ('T-X4 only (PA Session +2L+Token)', {'T-X4'}),
        ('parts 3-5 set (T-09c+T-02a+T-09b)', {'T-09c','T-02a','T-09b'}),
        ('all corrections (full Parts 3-5 + emergent)', 
         {'T-09c','T-02a','T-09b','T-02c','T-X4','T-01a','T-03c'}),
    ]
    results = {}
    print(f"v5 sweep — {N} campaigns × {SEASONS} seasons, canonical rules + card slot caps")
    print("=" * 80)
    for label, tw in configs:
        r = run_mc_v5(N, tweaks=tw, seasons=SEASONS)
        results[label] = r
        ws = r['win_share']
        sp = max(ws.values()) - min(ws.values())
        print(f"\n{label}")
        print(f"  Win share: Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%  (spread {sp:.1f}pp)")
        print(f"  Direct sovereignty: {r['direct_sovereignty_rate']}% | "
              f"Avg length: {r['avg_length']}s")
        print(f"  Territories end: {r['territory_means']}")
        print(f"  Treaties: {r['treaty_means']} | Inq: {r['inq_mean']} | "
              f"Turmoil: {r['turmoil_mean']}")
    open('/home/claude/mc_v5.json', 'w').write(json.dumps(results, indent=2))
