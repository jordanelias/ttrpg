"""
Valoria 4-Faction Monte Carlo Simulator v4 — Canonical Rule Corrections

Six canonical rule violations found in v3 simulator (see Part 6 §5 + canonical
re-verification 2026-05-14). v4 corrections:

1. §6.2 STRUCK: faction-specific victory paths removed → universal Peninsular
   Sovereignty (§6.1) replaces v3's per-faction VP formulas
2. ED-322: Active Inquisition threshold AP ≥ 3 (not AP ≥ 2)
3. ED-632/§7 Step 4c: Accord 0 → Popular Uprising → Uncontrolled (NOT transfer
   to Inquisitor-holder; my v3 transfer-to-Church rule was invented)
4. §2.4 Accord losing: Inquisitor presence is NOT listed as Accord-decreasing
   trigger; v3's ad-hoc Inquisitor → Accord drain removed
5. §5.2 + §7c: Seizure pool = Influence + floor(CI/15), Ob = 10 − PT − infra,
   available CI ≥ 40, requires Mandate ≥ 4 + Prominence
6. §2.1: canonical starting territory split is Crown 6 / Hafenmark 4 /
   Church 1 / Varfell 4 (NOT uniform 3/3/3/3 as v3); Crown starts strongly
   advantaged (40% of map)

Also: §5.4 Varfell Cultural Reformation STRUCK; Varfell has no canonical
non-military acquisition path. Investigated separately as canonical balance
question.

Victory path differentiation: now ALL factions share Peninsular Sovereignty
target; they differ only in approach (Crown: Treaty diplomacy; Church: Seizure;
Hafenmark: Dynastic Proclamation + Treaties; Varfell: Military conquest only).
"""
import sys, json, math, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from prob_engine import summary

VFIVE = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 2]

def roll_pool(n):
    return sum(random.choice(VFIVE) for _ in range(max(1, n)))

def resolve_degree(net):
    if net <= -1: return 'Failure'
    if net == 0: return 'Partial'
    if 1 <= net <= 2: return 'Success'
    return 'Overwhelming'


# ============================================================
# Canonical starting state (§2.1 peninsular_strain_v30)
# ============================================================

# Map: (territory_id, controller, starting_accord, starting_pt, prosperity)
# PT = Piety Track (5 = Church-friendly, 1 = Church-hostile)
CANONICAL_TERRITORIES = [
    # Crown territories (6 total)
    ('T1',  'Crown',     3, 3, 4),  # Valorsplatz capital
    ('T2',  'Crown',     3, 3, 3),  # Kronmark
    ('T3',  'Crown',     3, 3, 3),  # Lowenskyst
    ('T5',  'Crown',     2, 3, 3),  # Feldmark
    ('T6',  'Crown',     2, 3, 2),  # Stillhelm
    ('T14', 'Crown',     3, 3, 3),  # Ehrenfeld
    # Hafenmark territories (4)
    ('T7',  'Hafenmark', 2, 3, 2),  # Rendstad
    ('T8',  'Hafenmark', 3, 3, 4),  # Gransol capital
    ('T10', 'Hafenmark', 2, 3, 3),  # Spartfell
    ('T17', 'Hafenmark', 2, 3, 2),  # Halvarshelm
    # Church territory (1)
    ('T9',  'Church',    4, 5, 4),  # Himmelenger cathedral city
    # Varfell territories (4)
    ('T4',  'Varfell',   2, 2, 2),  # Grauwald
    ('T11', 'Varfell',   2, 2, 2),  # Halvardshelm
    ('T12', 'Varfell',   2, 2, 3),  # Sigurdshelm capital
    ('T13', 'Varfell',   1, 1, 2),  # Oastad (RM-influenced)
    # Uncontrolled / out-of-play (handled separately)
    # T15 Askeheim Uncontrolled
    # T16 Schoenland not in play
]

PLAYABLE_TERRITORIES = [t[0] for t in CANONICAL_TERRITORIES]
ALL_PLAYABLE_15 = PLAYABLE_TERRITORIES + ['T15']  # T15 Uncontrolled for victory check

# ============================================================
# State classes
# ============================================================

class Faction:
    def __init__(self, name, stats):
        self.name = name
        self.stats = dict(stats)
        self.territories = set()
        self.tokens_held = defaultdict(int)
        self.tokens_received = defaultdict(int)
        self.charters = set()
        self.inquisitors = set()
        self.cardinal_focus = None
        self.cardinal_focus_used_this_season = False
        self.royal_guard_available = True
        self.pa_session_arc_used = False
        self.influence_surge_arc_used = False
        self.consec_decree = 0
        self.revelation_tokens = 0
        self.treaties = defaultdict(str)  # {target_faction: treaty_type}
        self.submitted = False  # Stability 0 + formal submission
        self.sovereignty_history = 0  # consecutive Accountings at victory

    def reset_seasonal(self):
        self.royal_guard_available = True
        self.cardinal_focus_used_this_season = False

    def reset_annual(self):
        self.consec_decree = 0
        self.cardinal_focus = None

    def reset_arc(self):
        self.pa_session_arc_used = False
        self.influence_surge_arc_used = False

    def mandate(self):
        return self.stats['L']


class Territory:
    def __init__(self, tid, owner, accord, pt, prosperity):
        self.id = tid
        self.owner = owner
        self.accord = accord    # 0-3 (province-level)
        self.pt = pt            # 1-5 (Piety Track)
        self.prosperity = prosperity  # 0-5
        self.order = pt         # 0-5 (settlement-level proxy, derived from PT initially)
        self.ap = 0             # Counter-Narrative / Heresy AP
        self.inquisitor_holder = None
        self.garrison = False   # Mil unit present
        self.last_hostile_season = -10
        self.consec_passive_seasons = 0
        self.cb_against = set()  # factions holding Casus Belli vs us
        self.first_cn_attempted_this_arc = False
        self.last_govern_season = -10

    def is_uncontrolled(self):
        return self.owner is None or self.owner == 'Uncontrolled'


class World:
    def __init__(self, tweaks=None):
        self.season = 0
        self.year = 1
        self.arc = 1
        self.factions = {}
        self.territories = {}
        # Canonical clocks
        self.clocks = dict(CI=28, MS=72, IP=20, PI=5, Strain=0, Turmoil=0)
        self.tweaks = tweaks or set()
        # T15 Askeheim (Uncontrolled — playable but no controller)
        self.territories['T15'] = Territory('T15', None, 0, 1, 1)
        for tid, owner, accord, pt, prosp in CANONICAL_TERRITORIES:
            self.territories[tid] = Territory(tid, owner, accord, pt, prosp)
        self.winner = None  # set when Peninsular Sovereignty held 2 Accountings

    def turmoil(self):
        return self.clocks.get('Turmoil', self.clocks.get('Strain', 0))

    def all_player_factions(self):
        return list(self.factions.values())

    def territories_owned_by(self, faction_name):
        return {tid for tid, t in self.territories.items() if t.owner == faction_name}


# ============================================================
# Peninsular Sovereignty Victory Check (§6.1)
# ============================================================

def check_effective_hegemony(world, hegemon_name):
    """Does this faction satisfy Peninsular Sovereignty (§6.1)?"""
    hegemon = world.factions[hegemon_name]
    # All 15 playable territories controlled directly or via effective hegemony
    territories_controlled = set()
    for tid in ALL_PLAYABLE_15:
        t = world.territories.get(tid)
        if t is None: continue
        if t.owner == hegemon_name:
            territories_controlled.add(tid)
        elif t.owner in world.factions:
            rival = world.factions[t.owner]
            # Treaty-bound? (qualifying types per ED-791: Peace, Alliance, Capit, Tributary, Crown Treaty)
            treaty_type = hegemon.treaties.get(rival.name, '')
            if treaty_type in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                territories_controlled.add(tid)
            # Submitted?
            elif rival.submitted:
                territories_controlled.add(tid)
            # Institutionally dominated?
            elif rival.stats['L'] <= 1 and hegemon.stats['L'] >= 5:
                territories_controlled.add(tid)
    # Need all 15
    if len(territories_controlled) < len(ALL_PLAYABLE_15):
        return False
    # Accord ≥ 2 in directly-controlled territories
    directly_controlled = world.territories_owned_by(hegemon_name)
    for tid in directly_controlled:
        if world.territories[tid].accord < 2:
            return False
    # Turmoil ≤ 6 (peninsula not in Crisis)
    if world.turmoil() > 6:
        return False
    return True


def universal_victory_check(world):
    """Returns winner name if Peninsular Sovereignty held for 2 consecutive Accountings."""
    for fname, f in world.factions.items():
        if check_effective_hegemony(world, fname):
            f.sovereignty_history += 1
            if f.sovereignty_history >= 2:
                return fname
        else:
            f.sovereignty_history = 0
    return None


# ============================================================
# Actions — canonical rules
# ============================================================

def make_action(name, actor, target=None, **params):
    return dict(name=name, actor=actor, target=target, **params)


def prereqs_met(action, world):
    name = action['name']; actor = action['actor']; target = action.get('target')

    if name == 'Royal Decree':
        return actor.name == 'Crown'
    if name == 'Royal Charter':
        return actor.name == 'Crown' and target in actor.territories
    if name == 'Crown Treaty':
        # Crown can sue any faction for Treaty
        if actor.name != 'Crown' or target not in world.factions: return False
        if actor.name == target: return False
        return actor.treaties.get(target, '') == ''  # no existing treaty
    if name == 'Outreach to Schoenland':
        return actor.name == 'Crown' and world.clocks['IP'] < 30
    if name == 'Cardinal Focus':
        return actor.name == 'Church' and not actor.cardinal_focus_used_this_season
    if name == 'Piety Spread':
        return (actor.name == 'Church' and target in world.territories and
                world.territories[target].owner not in (None, 'Church'))
    if name == 'Active Inquisition':
        # ED-322: First Inquisitor AP ≥ 3
        if actor.name != 'Church' or target not in world.territories: return False
        t = world.territories[target]
        # Justice cardinal focus modifies threshold
        threshold = 3
        if actor.cardinal_focus == 'Justice' and len(actor.inquisitors) == 0:
            threshold = 2  # Justice reduces first Inquisitor threshold −1
        # Second Inquisitor AP ≥ 6 (combined? per-territory? assume per-territory)
        if t.ap < threshold: return False
        if t.inquisitor_holder: return False
        # T-09c tweak: max 2 Inquisitors peninsula-wide
        if 'T-09c' in world.tweaks and len(actor.inquisitors) >= 2: return False
        return True
    if name == 'Church Seizure':
        # §5.2 + §7c: requires Mandate ≥ 4, Prominence (Mandate > controller), CI ≥ 40,
        # cannot target Uncontrolled (ED-704)
        if actor.name != 'Church' or target not in world.territories: return False
        t = world.territories[target]
        if t.is_uncontrolled(): return False
        if world.clocks['CI'] < 40: return False
        if actor.stats['L'] < 4: return False
        controller = world.factions.get(t.owner)
        if controller is None: return False
        if actor.stats['L'] <= controller.stats['L']: return False  # Prominence required
        return True
    if name == 'Excommunication':
        return (actor.name == 'Church' and target in world.factions and
                target != 'Church')
    if name == 'Ecclesiastical Appointment':
        return actor.name == 'Church' and actor.stats['L'] < 7
    if name == 'Diplomat Card':
        return (actor.name == 'Hafenmark' and target in world.factions and
                target != 'Hafenmark')
    if name == 'Parliamentary Session':
        return actor.name == 'Hafenmark' and not actor.pa_session_arc_used
    if name == 'Dynastic Proclamation':
        # Hafenmark territorial acquisition; Haf L > target L
        if actor.name != 'Hafenmark': return False
        if actor.stats['L'] < 4: return False
        if target not in world.factions: return False
        return actor.stats['L'] > world.factions[target].stats['L']
    if name == 'Counter-Narrative':
        return actor.name == 'Varfell' and target in world.territories
    if name == 'Cultural Reformation':
        # STRUCK CR-STRIKE-2026-04-19
        return False
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
        # Conquer Uncontrolled or rival-held territory via Mil
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner == actor.name: return False
        # Need Mil ≥ 3 to conquer
        return actor.stats['Mil'] >= 3
    return False


def pool_and_ob(action, world):
    name = action['name']; actor = action['actor']; target = action.get('target')
    if name == 'Royal Decree':
        return actor.stats['I'], 2 + actor.consec_decree
    if name == 'Royal Charter':
        t = world.territories[target]
        ob = (t.prosperity // 2) + 1
        if 'T-01a' in world.tweaks: ob += len(actor.charters)
        return actor.stats['L'], max(1, ob)
    if name == 'Crown Treaty':
        # I vs target L (canonical, GAP-08 ceiling)
        return actor.stats['I'], world.factions[target].stats['L']
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
        # §5.2: Pool = Influence + floor(CI/15); Ob = 10 − PT − infrastructure (floor 1)
        t = world.territories[target]
        pool = actor.stats['I'] + (world.clocks['CI'] // 15)
        ob = max(1, 10 - t.pt - 0)  # infrastructure = 0 (not modeled)
        if world.clocks['CI'] >= 80: ob = max(1, ob - 1)  # §7c CI 80 effect
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
        return actor.stats['L'], (world.factions[target].stats['Sta'] // 2) + 1
    if name == 'Counter-Narrative':
        t = world.territories[target]
        if t.owner not in world.factions: return actor.stats['I'], 3
        owner = world.factions[t.owner]
        base = (owner.stats['L'] // 2) + 1 - 1  # Consequentialism −1
        if t.inquisitor_holder:
            if 'T-02a' in world.tweaks and t.first_cn_attempted_this_arc:
                pass  # familiarity active
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
        # Pool: Mil; Ob: target garrison strength (proxy via prosperity)
        t = world.territories[target]
        return actor.stats['Mil'], 3 if t.garrison else 2
    return 3, 3


def apply_outcome(action, degree, world):
    name = action['name']; actor = action['actor']; target = action.get('target')
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Royal Decree':
        actor.consec_decree += 1
        if success:
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
    elif name == 'Royal Charter':
        if success: actor.charters.add(target)
    elif name == 'Crown Treaty':
        # GAP-05 consent: 50% chance target accepts (per Part 3 assumption)
        if success and random.random() < 0.5:
            tgt = world.factions[target]
            actor.treaties[target] = 'CrownTreaty'
            tgt.treaties[actor.name] = 'CrownTreaty'
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            # Treaty-bound for hegemony
    elif name == 'Outreach to Schoenland':
        if success: world.clocks['IP'] = max(0, world.clocks['IP'] - 2)
    elif name == 'Cardinal Focus':
        actor.cardinal_focus = random.choice(['Justice', 'Prudence', 'Temperance', 'Fortitude'])
        actor.cardinal_focus_used_this_season = True
    elif name == 'Piety Spread':
        # Per faction_actions.md L33-37: Overwhelming = AP +3 + immediate Inquisitor if at threshold
        if overwhelming:
            world.territories[target].ap += 3
        elif degree == 'Success':
            world.territories[target].ap += 2
        elif degree == 'Partial':
            world.territories[target].ap += 1
    elif name == 'Active Inquisition':
        if success:
            t = world.territories[target]
            t.inquisitor_holder = 'Church'
            actor.inquisitors.add(target)
            t.ap = 0
            # Mark territory as receiving hostile action (Heresy investigation)
            t.last_hostile_season = world.season
            t.order = max(0, t.order - 1)  # §2.4b: Heresy Investigation drops Order
        elif degree == 'Partial':
            world.territories[target].ap += 1
    elif name == 'Church Seizure':
        t = world.territories[target]
        if overwhelming:
            # Accord = floor(PT/2) + 2, max 3
            new_accord = min(3, (t.pt // 2) + 2)
            old_owner = t.owner
            if old_owner in world.factions:
                world.factions[old_owner].territories.discard(target)
            t.owner = 'Church'
            actor.territories.add(target)
            t.accord = new_accord
            # CB granted (PP-510)
            if old_owner: t.cb_against.add(old_owner)
        elif degree == 'Success':
            new_accord = max((t.pt // 2) + 1, 2)
            old_owner = t.owner
            if old_owner in world.factions:
                world.factions[old_owner].territories.discard(target)
            t.owner = 'Church'
            actor.territories.add(target)
            t.accord = new_accord
            if old_owner: t.cb_against.add(old_owner)
        elif degree == 'Partial':
            # Contested seizure fails; Accord set to 1; CB granted
            t.accord = 1
            if t.owner: t.cb_against.add(actor.name)
        elif degree == 'Failure':
            # Discipline penalty (not modeled). CB to controller.
            if t.owner: t.cb_against.add(actor.name)
    elif name == 'Excommunication':
        if success:
            world.factions[target].stats['L'] = max(1, world.factions[target].stats['L'] - 1)
        else:
            actor.stats['Sta'] = max(0, actor.stats['Sta'] - 1)
    elif name == 'Ecclesiastical Appointment':
        if success:
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
    elif name == 'Diplomat Card':
        if 'T-03c' in world.tweaks:
            actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if success:
            actor.tokens_held[target] += 1
            world.factions[target].tokens_received[actor.name] += 1
            world.clocks['PI'] += 1
    elif name == 'Parliamentary Session':
        actor.pa_session_arc_used = True
        support = 1  # self
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
        # §5.3: Overwhelming = transfer + Accord 2 + target L−1 + Haf L+1
        # Success = transfer + Accord 2 + target L−1
        # Partial = no transfer + CB + target territory Accord −1
        # Pick a target territory
        target_faction = world.factions[target]
        if not target_faction.territories: return
        tid = random.choice(list(target_faction.territories))
        t = world.territories[tid]
        if overwhelming:
            target_faction.territories.discard(tid)
            t.owner = 'Hafenmark'
            actor.territories.add(tid)
            t.accord = 2
            target_faction.stats['L'] = max(1, target_faction.stats['L'] - 1)
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        elif degree == 'Success':
            target_faction.territories.discard(tid)
            t.owner = 'Hafenmark'
            actor.territories.add(tid)
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
                v.royal_guard_available = False
                return
        if success:
            world.factions[target].stats['Sta'] = max(0, world.factions[target].stats['Sta'] - 1)
            if actor.name == 'Varfell':
                actor.revelation_tokens += 1
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
            # +1 Accord on seat; if territory was Accord 1, removes garrison requirement 1 season
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
        # §2.4: Military conquest sets Accord to 1
        if success:
            t = world.territories[target]
            old_owner = t.owner
            if old_owner in world.factions:
                world.factions[old_owner].territories.discard(target)
            t.owner = actor.name
            actor.territories.add(target)
            t.accord = 1
            t.cb_against.add(actor.name)  # conquerors get CB against themselves later
            world.clocks['MS'] = max(0, world.clocks['MS'] - 2)  # Battle MS impact
            world.clocks['IP'] += 2


# ============================================================
# Decision Layer — utility scoring (canonical-aware)
# ============================================================

def score_action(action, world):
    name = action['name']; actor = action['actor']; target = action.get('target')
    s = 1
    own_territories = len(actor.territories)
    map_size = len(ALL_PLAYABLE_15)
    sovereignty_gap = map_size - own_territories  # how far from outright sovereignty

    if actor.name == 'Crown':
        # Crown's path: defensive (already 6/15); add territories via Treaty + maintain Accord
        if name == 'Royal Charter':
            if target not in actor.charters: s += 6
        elif name == 'Royal Decree':
            if actor.stats['Sta'] < 5: s += 6 - actor.consec_decree * 2
        elif name == 'Govern':
            t = world.territories[target]
            if target in actor.charters: s += 6
            if t.accord < 2: s += 9  # defensive priority — keep Accord ≥ 2 (victory cond)
            if t.prosperity < 4: s += 3
        elif name == 'Muster':
            t = world.territories[target]
            if t.accord <= 1: s += 9
            if not t.garrison: s += 5
        elif name == 'Crown Treaty':
            # Critical for Peninsular Sovereignty via hegemony
            s += 10
        elif name == 'Outreach to Schoenland':
            if world.clocks['IP'] > 25: s += 6
        elif name == 'Military Conquest':
            # Crown can conquer Uncontrolled (T15) or weak rival territories
            t = world.territories[target]
            if t.is_uncontrolled(): s += 8
            else: s += 3

    elif actor.name == 'Church':
        # Church path: aggressive Seizure (starts with 1/15; needs to gain 14)
        if name == 'Cardinal Focus':
            s += 6
        elif name == 'Piety Spread':
            t = world.territories[target]
            if not t.inquisitor_holder and not t.is_uncontrolled():
                s += 8
                if t.ap >= 3: s -= 3
        elif name == 'Active Inquisition':
            t = world.territories[target]
            if t.ap >= 3: s += 12
            if 'T-09c' in world.tweaks and len(actor.inquisitors) >= 2: s = -100
        elif name == 'Church Seizure':
            # Available CI ≥ 40 (canonical); high priority for territory acquisition
            if world.clocks['CI'] >= 40 and actor.stats['L'] >= 4:
                s += 13
        elif name == 'Excommunication':
            if world.factions[target].stats['L'] < 5: s += 4
            else: s += 1
        elif name == 'Ecclesiastical Appointment':
            if actor.stats['L'] < 7: s += 9
        elif name == 'Trade':
            s += 3
        elif name == 'Govern':
            t = world.territories[target]
            if t.accord < 2: s += 7
            else: s += 3

    elif actor.name == 'Hafenmark':
        # Hafenmark path: Dynastic Proclamation + Treaties (Crown Treaty if available)
        if name == 'Parliamentary Session':
            if not actor.pa_session_arc_used: s += 11
        elif name == 'Diplomat Card':
            tgt = world.factions[target]
            if tgt.stats['L'] == 4: s += 8
            elif tgt.stats['L'] == 5: s += 5
        elif name == 'Dynastic Proclamation':
            tgt = world.factions[target]
            if actor.stats['L'] > tgt.stats['L'] and len(tgt.territories) > 0:
                s += 12  # PRIMARY territorial acquisition vector
        elif name == 'Trade':
            if actor.stats['W'] < 7: s += 7
            else: s += 3
        elif name == 'Govern':
            t = world.territories[target]
            if t.accord < 2: s += 8
            else: s += 4
        elif name == 'Muster':
            t = world.territories[target]
            if not t.garrison and t.accord <= 2: s += 6

    elif actor.name == 'Varfell':
        # Varfell path: Cultural Reformation STRUCK — only Military Conquest for acquisition
        if name == 'Counter-Narrative':
            t = world.territories[target]
            if t.inquisitor_holder:
                if 'T-02a' in world.tweaks and t.first_cn_attempted_this_arc:
                    s += 10
                else: s += 6
            elif t.ap >= 2: s += 8
            else: s += 2
        elif name == 'Spy':
            tgt = world.factions[target]
            if tgt.stats['Int'] <= 3: s += 8
            elif tgt.stats['Int'] == 4: s += 5
            else: s += 2
        elif name == 'Tribune Network':
            s += 6
        elif name == 'Govern':
            t = world.territories[target]
            if t.accord < 2: s += 9  # Keep own territories at Accord ≥ 2
            else: s += 3
        elif name == 'Muster':
            t = world.territories[target]
            if not t.garrison: s += 6
            if t.accord <= 1: s += 4
        elif name == 'Military Conquest':
            t = world.territories[target]
            if t.is_uncontrolled() and actor.stats['Mil'] >= 4: s += 9
            elif actor.stats['Mil'] >= 5: s += 5
        elif name == 'Trade':
            s += 3
    return s


def list_candidate_actions(faction, world):
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
        # Conquer Uncontrolled
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
                if (faction.stats['L'] >= 4 and
                    faction.stats['L'] > world.factions[f].stats['L']):
                    cands.append(make_action('Dynastic Proclamation', faction, target=f))
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
    return [a for a in cands if prereqs_met(a, world)]


def select_actions(faction, world, n_actions=3):
    selected = []
    used_targets = set()
    for _ in range(n_actions):
        cands = list_candidate_actions(faction, world)
        cands = [a for a in cands if (a['name'], a.get('target')) not in used_targets]
        if not cands: break
        scored = [(score_action(a, world), a) for a in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used_targets.add((chosen['name'], chosen.get('target')))
    return selected


# ============================================================
# World lifecycle
# ============================================================

def init_world(tweaks=None):
    w = World(tweaks=tweaks)
    # Canonical starting stats
    w.factions['Crown'] = Faction('Crown',
        dict(L=5, PS=5, M=5, I=5, W=4, Mil=4, Int=3, Sta=4))
    w.factions['Church'] = Faction('Church',
        dict(L=5, PS=5, M=5, I=6, W=5, Mil=4, Int=4, Sta=5))
    w.factions['Hafenmark'] = Faction('Hafenmark',
        dict(L=4, PS=4, M=4, I=4, W=5, Mil=3, Int=3, Sta=4))
    w.factions['Varfell'] = Faction('Varfell',
        dict(L=4, PS=4, M=4, I=4, W=4, Mil=4, Int=4, Sta=4))
    # Assign territories per canonical starting state
    for tid, t in w.territories.items():
        if t.owner in w.factions:
            w.factions[t.owner].territories.add(tid)
    # Set some initial garrisons (capital cities have garrisons by default)
    capitals = {'T1', 'T8', 'T9', 'T12'}
    for tid in capitals:
        if tid in w.territories:
            w.territories[tid].garrison = True
    return w


def end_of_season(world):
    """Phase 5 Accounting per §7 canonical."""
    # Step 4a: Clocks tick
    world.clocks['CI'] += 1
    world.clocks['MS'] = max(0, world.clocks['MS'] - 1)
    
    # Step 4c — Accord checks (§7):
    revolts_this_season = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        # 1. Accord 1 + no garrison → Accord 0
        if t.accord == 1 and not t.garrison:
            t.accord = 0
        # 2. Accord 0 → Popular Uprising. Win=hold (Accord 1); Lose=Uncontrolled. Turmoil +1.
        if t.accord == 0:
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolts_this_season += 1
            if t.garrison:
                # Garrison fights Popular Uprising (Mil vs Ob 2)
                controller = world.factions[t.owner]
                if (roll_pool(controller.stats['Mil']) - 2) >= 1:
                    # Win: hold, Accord → 1
                    t.accord = 1
                else:
                    # Lose: territory becomes Uncontrolled
                    if t.owner in world.factions:
                        world.factions[t.owner].territories.discard(tid)
                    t.owner = None
                    t.garrison = False
                    t.inquisitor_holder = None
                    # Inquisitor recalled if was there
                    for f in world.factions.values():
                        f.inquisitors.discard(tid)
            else:
                # No garrison → directly Uncontrolled
                if t.owner in world.factions:
                    world.factions[t.owner].territories.discard(tid)
                t.owner = None
                t.inquisitor_holder = None
                for f in world.factions.values():
                    f.inquisitors.discard(tid)
        # 3. Passive normalisation: 2 consecutive seasons no hostile + garrison → Accord +1
        if (t.garrison and world.season - t.last_hostile_season >= 2):
            t.consec_passive_seasons += 1
            if t.consec_passive_seasons >= 2 and t.accord < 2:
                t.accord += 1
                t.consec_passive_seasons = 0
        else:
            t.consec_passive_seasons = 0

    # Step 4d — Turmoil update
    # If no instability and no battles: Strain/Turmoil −1
    if revolts_this_season == 0:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - 1)
    # Strain alias to Turmoil
    world.clocks['Strain'] = world.clocks['Turmoil']

    # Controller Stability check (§2.4: Sta ≤ 2 → Accord −1 in all controlled)
    for fname, f in world.factions.items():
        if f.stats['Sta'] <= 2:
            for tid in list(f.territories):
                world.territories[tid].accord = max(0, world.territories[tid].accord - 1)

    # PI/Crisis check
    if world.clocks['PI'] >= 8:
        # Crisis active — but we don't model freezes
        pass

    # Step 12: Victory check
    winner = universal_victory_check(world)
    if winner: world.winner = winner


def run_season(world):
    if world.winner: return
    for f in world.factions.values(): f.reset_seasonal()
    all_acts = []
    for f in world.factions.values():
        all_acts.extend(select_actions(f, world, n_actions=3))
    for action in all_acts:
        if not prereqs_met(action, world): continue
        pool, ob = pool_and_ob(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        apply_outcome(action, degree, world)
    end_of_season(world)
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            f.reset_arc(); f.reset_annual()
        world.arc += 1


def run_campaign(tweaks=None, seasons=24, seed=None):
    """24 seasons (6 years) — longer than v3 since Peninsular Sovereignty is harder."""
    if seed is not None: random.seed(seed)
    world = init_world(tweaks=tweaks)
    for _ in range(seasons):
        run_season(world)
        if world.winner: break
    winner = world.winner
    if winner is None:
        # No outright winner. Closest to sovereignty wins by territory count + treaties.
        scores = {}
        for fname, f in world.factions.items():
            hegemony = 0
            for tid in ALL_PLAYABLE_15:
                t = world.territories.get(tid)
                if t and t.owner == fname:
                    hegemony += 1
                elif t and t.owner in world.factions:
                    treaty_type = f.treaties.get(t.owner, '')
                    if treaty_type in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                        hegemony += 0.5
            scores[fname] = hegemony * 10 + f.stats['L'] + len(f.territories)
        winner = max(scores, key=scores.get)
    return dict(winner=winner, world=world)


def run_mc(n, tweaks=None, seasons=24):
    wins = Counter()
    terr = defaultdict(list)
    inq = []; crisis = 0; revolts = 0
    direct_sovereignty = 0
    seasons_run = []
    for i in range(n):
        r = run_campaign(tweaks=tweaks, seasons=seasons, seed=i)
        wins[r['winner']] += 1
        for fname in r['world'].factions:
            terr[fname].append(len(r['world'].factions[fname].territories))
        inq.append(len(r['world'].factions['Church'].inquisitors))
        if r['world'].clocks['PI'] >= 8: crisis += 1
        revolts += r['world'].clocks['Turmoil']
        if r['world'].winner: direct_sovereignty += 1
        seasons_run.append(r['world'].season)
    total = sum(wins.values())
    return dict(
        n=n,
        win_share={k: round(wins.get(k, 0)/total * 100, 1) for k in
                   ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        territory_means={k: round(sum(v)/len(v), 2) for k, v in terr.items()},
        inq_mean=round(sum(inq)/len(inq), 2),
        crisis_rate=round(crisis/n * 100, 1),
        turmoil_mean=round(revolts/n, 2),
        direct_sovereignty_rate=round(direct_sovereignty/n * 100, 1),
        avg_campaign_seasons=round(sum(seasons_run)/len(seasons_run), 1),
    )


if __name__ == '__main__':
    N = 500
    SEASONS = 24
    configs = [
        ('canon-v4 (canonical rules, no tweaks)', set()),
        ('T-09c only (cap Inquisitor 2)', {'T-09c'}),
        ('T-02a only (Inq familiarity)', {'T-02a'}),
        ('T-X4 only (PA Session +2L+Token)', {'T-X4'}),
        ('combined Parts 3-5 (T-09c+T-02a+T-09b)', {'T-09c','T-02a','T-09b'}),
        ('all corrections (T-09c+T-02a+T-09b+T-02c+T-X4)', 
         {'T-09c','T-02a','T-09b','T-02c','T-X4'}),
    ]
    results = {}
    print(f"Running v4 sweep — {N} campaigns × {SEASONS} seasons each")
    print(f"Canonical rules: Peninsular Sovereignty victory, AP≥3, Accord→Uncontrolled")
    print(f"Starting: Crown 6 / Hafenmark 4 / Church 1 / Varfell 4 territories (canonical)")
    print("=" * 80)
    for label, tw in configs:
        r = run_mc(N, tweaks=tw, seasons=SEASONS)
        results[label] = r
        ws = r['win_share']
        sp = max(ws.values()) - min(ws.values())
        print(f"\n{label}")
        print(f"  Win share: Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%  (spread {sp:.1f}pp)")
        print(f"  Direct sovereignty rate: {r['direct_sovereignty_rate']}%")
        print(f"  Avg territories at end: {r['territory_means']}")
        print(f"  Inq mean: {r['inq_mean']} | Crisis: {r['crisis_rate']}% | "
              f"Turmoil mean: {r['turmoil_mean']}")
        print(f"  Avg campaign length: {r['avg_campaign_seasons']} seasons (max {SEASONS})")
    open('/home/claude/mc_v4.json', 'w').write(json.dumps(results, indent=2))
    print("\n[saved /home/claude/mc_v4.json]")
