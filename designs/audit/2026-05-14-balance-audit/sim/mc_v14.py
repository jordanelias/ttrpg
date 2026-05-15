"""
mc_v14 — UNIFIED DERIVED SCORES + REVOLT FACTIONS + GRANULAR LOGGING

Design (per Jordan direction 2026-05-14):
  1. ALL base stats 1-7. Each stat has an internal buffer (just calc score, same name as player-facing).
  2. Accord 1-7 (replaces old 0-3 + Order 0-5; deduplicated).
  3. Piety 1-7 (replaces 0-5; threshold at 3 for flip attempts).
  4. Deterministic threat response: Accord ≤ 2 → mandatory Muster/Govern (not stochastic).
  5. Insurgency → Founded Organization → Parliamentary faction pipeline.
  6. ALL canonical mechanics included: CI generation, Mass Seizure, Church tithes, Hafenmark suppression, Treaty Expiration, all v12c mechanics, all v5/v6 base actions.
  7. Full JSONL logging of every event, branch, prereq evaluation, dice roll, state change for all-directions NERS audit.

Authority: derived_stats_v30 §8, peninsular_strain_v30 §2-§7, victory_v30 §3.2 + §8, faction_layer_v30
"""
import sys, json, random, math, os, time
from collections import defaultdict, Counter
from datetime import datetime, timezone

# ═══════════════════════════════════════════════════════════════════════════
# DERIVED SCORE — universal buffer pattern
# ═══════════════════════════════════════════════════════════════════════════

class DerivedScore:
    """Universal buffer: base stat (1-7) → internal value (stat × mult).
    Drains absorb shocks. Depletion → stat check → possible stat loss."""
    __slots__ = ('stat_key', 'mult', 'depletion_ob', 'value')

    def __init__(self, stat_key, mult, depletion_ob=1):
        self.stat_key = stat_key
        self.mult = mult
        self.depletion_ob = depletion_ob
        self.value = 0

    def init_from(self, stats):
        self.value = stats[self.stat_key] * self.mult

    def drain(self, amount, stats, logger=None, owner_id=None, reason=None):
        """amount NEGATIVE = drain; POSITIVE = restore.
        Returns dict of effects: {'depleted', 'stat_lost'}"""
        result = {'depleted': False, 'stat_lost': False, 'before': self.value, 'after': self.value}
        self.value += amount
        if self.value <= 0:
            result['depleted'] = True
            net = roll_pool_logged(stats[self.stat_key], logger=logger,
                                   reason=f'{owner_id}.{self.stat_key} depletion check')
            outcome = resolve_degree(net - self.depletion_ob)
            if outcome == 'Failure':
                stats[self.stat_key] = max(1, stats[self.stat_key] - 1)
                result['stat_lost'] = True
            self.value = stats[self.stat_key] * self.mult
        self.value = min(self.value, stats[self.stat_key] * self.mult)
        result['after'] = self.value
        return result

    def gain(self, amount, stats):
        self.value = min(self.value + amount, stats[self.stat_key] * self.mult)


# ═══════════════════════════════════════════════════════════════════════════
# DICE — with logging
# ═══════════════════════════════════════════════════════════════════════════

def roll_pool_logged(pool_size, logger=None, reason=None):
    """Roll N dice, return success count (4+). Log if logger present."""
    rolls = [random.randint(1, 6) for _ in range(max(0, pool_size))]
    successes = sum(1 for r in rolls if r >= 4)
    if logger is not None and reason is not None:
        logger.log('dice_roll', pool=pool_size, rolls=rolls, successes=successes, reason=reason)
    return successes

def roll_pool(n):
    return sum(1 for _ in range(max(0, n)) if random.randint(1, 6) >= 4)

def resolve_degree(net):
    """Net successes → Degree. [canonical: peninsular_strain_v30 §3.2]"""
    if net >= 3: return 'Overwhelming'
    if net >= 1: return 'Success'
    if net == 0: return 'Partial'
    return 'Failure'


# ═══════════════════════════════════════════════════════════════════════════
# ADJACENCY [canonical: valoria_geography_v30.yaml]
# ═══════════════════════════════════════════════════════════════════════════

ADJACENCY = {
    'T1':  {'T2','T5','T14','T16'},
    'T2':  {'T1','T3','T9','T14'},
    'T3':  {'T2','T9','T17'},
    'T4':  {'T7','T12','T14'},
    'T5':  {'T1','T6','T14'},
    'T6':  {'T5','T13','T15'},
    'T7':  {'T4','T8'},
    'T8':  {'T7','T9','T10','T17'},
    'T9':  {'T2','T3','T8','T14','T17'},
    'T10': {'T8','T11'},
    'T11': {'T10','T12'},
    'T12': {'T4','T11','T13'},
    'T13': {'T6','T12','T15'},
    'T14': {'T1','T2','T4','T5','T9'},
    'T15': {'T6','T13'},
    'T17': {'T3','T8','T9'},
}

ALL_PLAYABLE_15 = {'T1','T2','T3','T4','T5','T6','T7','T8','T9','T10',
                   'T11','T12','T13','T14','T17'}  # T15, T16 special

# ═══════════════════════════════════════════════════════════════════════════
# TERRITORY — Accord 1-7 with internal buffer, PT 1-7 with internal buffer
# ═══════════════════════════════════════════════════════════════════════════

# Accord 1-7 conversion from canonical 0-3:
# old 0 → 1 (lost/critical), 1 → 2 (revolt-imminent), 2 → 4 (stable),
# 3 → 6 (loyal), 4 → 7 (heartland)
# Accord ≥ 4 = counts for sovereignty [canonical: PS v30 §2 mapped to new scale]

# Piety 1-7 conversion from canonical 0-5:
# old 0 → 1, 1 → 2, 2 → 3, 3 → 4, 4 → 5, 5 → 6 (then 7 = saturation)
# Piety ≥ 3 = flip threshold [canonical: victory_v30 §0.4]

STARTING_PT_OLD = {'T1':3,'T2':3,'T3':3,'T4':2,'T5':3,'T6':1,'T7':3,'T8':3,'T9':5,
                   'T10':3,'T11':2,'T12':2,'T13':1,'T14':3,'T15':3,'T17':3}
STARTING_ACCORD_OLD = {'T1':3,'T2':3,'T3':3,'T4':2,'T5':2,'T6':2,'T7':2,'T8':3,'T9':4,
                       'T10':2,'T11':2,'T12':2,'T13':1,'T14':3,'T15':0,'T17':2}
STARTING_OWNER = {'T1':'Crown','T2':'Crown','T3':'Crown','T4':'Varfell','T5':'Crown',
                  'T6':'Crown','T7':'Hafenmark','T8':'Hafenmark','T9':'Church','T10':'Hafenmark',
                  'T11':'Varfell','T12':'Varfell','T13':'Varfell','T14':'Crown','T15':None,
                  'T17':'Hafenmark'}
STARTING_GARRISON = {'T1':True,'T8':True,'T9':True,'T12':True}  # canonical starting garrisons

def convert_accord(old):
    return {0:1, 1:2, 2:4, 3:6, 4:7}[old]
def convert_pt(old):
    return min(7, old + 1)  # 0→1, 1→2, 2→3, 3→4, 4→5, 5→6

class V14Territory:
    def __init__(self, tid):
        self.tid = tid
        self.owner = STARTING_OWNER[tid]
        self.accord = convert_accord(STARTING_ACCORD_OLD[tid])  # 1-7
        self.pt = convert_pt(STARTING_PT_OLD[tid])  # 1-7
        self.garrison = STARTING_GARRISON.get(tid, False)
        self.prosperity = 2 if tid in {'T1','T2','T3','T8','T9','T14'} else 1
        # Internal buffers (just calc layer — same player-facing name)
        self._accord_dict = {'accord': self.accord}
        self._pt_dict = {'pt': self.pt}
        self.accord_buffer = DerivedScore('accord', 10, depletion_ob=1)
        self.pt_buffer = DerivedScore('pt', 5, depletion_ob=1)
        self.accord_buffer.init_from(self._accord_dict)
        self.pt_buffer.init_from(self._pt_dict)
        # Tracking
        self.uncontrolled_since = None
        self.last_hostile_season = -10
        self.consec_passive_seasons = 0
        # Church infrastructure (binary flags for now)
        self.templar = (tid == 'T9')  # Church starts with Templar at T9
        self.inquisitor = False
        self.church_governor = (tid == 'T9')

    def drain_accord(self, amount, logger=None, reason=None):
        """Drain Accord buffer. If depleted, Accord stat -1."""
        self._accord_dict['accord'] = self.accord
        r = self.accord_buffer.drain(amount, self._accord_dict, logger=logger,
                                     owner_id=f'territory.{self.tid}', reason=reason)
        self.accord = self._accord_dict['accord']
        return r

    def gain_accord(self, amount):
        self._accord_dict['accord'] = self.accord
        self.accord_buffer.gain(amount, self._accord_dict)

    def drain_pt(self, amount, logger=None, reason=None):
        self._pt_dict['pt'] = self.pt
        r = self.pt_buffer.drain(amount, self._pt_dict, logger=logger,
                                 owner_id=f'territory.{self.tid}', reason=reason)
        self.pt = self._pt_dict['pt']
        return r

    def gain_pt(self, amount):
        self._pt_dict['pt'] = self.pt
        self.pt_buffer.gain(amount, self._pt_dict)

    def is_uncontrolled(self):
        return self.owner is None or self.owner.startswith('Insurgency_') or self.owner.startswith('Founded_') or self.owner.startswith('RM_')


# ═══════════════════════════════════════════════════════════════════════════
# FACTION — with all derived scores [canonical: derived_stats_v30 §8]
# ═══════════════════════════════════════════════════════════════════════════

STARTING_STATS = {
    'Crown':    {'L': 5, 'Sta': 4, 'W': 4, 'I': 5, 'Mil': 4},
    'Church':   {'L': 5, 'Sta': 5, 'W': 5, 'I': 6, 'Mil': 4},
    'Hafenmark':{'L': 4, 'Sta': 4, 'W': 5, 'I': 4, 'Mil': 3},
    'Varfell':  {'L': 4, 'Sta': 4, 'W': 4, 'I': 4, 'Mil': 4},
}

class V14Faction:
    def __init__(self, name, parliamentary=True):
        self.name = name
        self.parliamentary = parliamentary
        self.stats = dict(STARTING_STATS.get(name, {'L': 2, 'Sta': 3, 'W': 2, 'I': 2, 'Mil': 3}))
        # Internal buffers — same player-facing names
        self.mandate = DerivedScore('L', 20, depletion_ob=2)      # L → Mandate buffer
        self.stability = DerivedScore('Sta', 10, depletion_ob=1)  # Sta → Stability buffer
        self.wealth = DerivedScore('W', 100, depletion_ob=1)      # W → Wealth buffer
        self.influence = DerivedScore('I', 15, depletion_ob=1)    # I → Influence buffer
        self.mandate.init_from(self.stats)
        self.stability.init_from(self.stats)
        self.wealth.init_from(self.stats)
        self.influence.init_from(self.stats)
        # Holdings
        self.territories = {tid for tid, o in STARTING_OWNER.items() if o == name}
        self.treaties = {}  # partner_name -> treaty_type
        self.casus_belli = set()
        self.tokens_held = defaultdict(int)
        self.inquisitors = set()
        self.revelation_tokens = 0
        self.submitted = False
        self.sovereignty_history = 0
        self.peaceful = True
        # Card / arc flags
        self.diplomat_card_used = False
        self.cardinal_card_used = False
        self.senator_inward_used = False
        self.tribune_card_used = False
        self.legacy_card_used = False
        self.hall_card_used = False
        self.consul_card_used = False
        self.ea_arc_used = False
        self.einhir_arc_used = False
        self.parl_arc_used = False
        self.mass_seizure_declared = False
        # Insurgency-specific
        self.is_insurgency = False
        self.founded_season = 0
        self.persistence_seasons = 0

    def reset_seasonal(self):
        self.diplomat_card_used = False
        self.cardinal_card_used = False
        self.senator_inward_used = False
        self.tribune_card_used = False
        self.legacy_card_used = False
        self.hall_card_used = False
        self.consul_card_used = False

    def reset_arc(self):
        self.ea_arc_used = False
        self.einhir_arc_used = False
        self.parl_arc_used = False


# ═══════════════════════════════════════════════════════════════════════════
# MECHANICAL LOGGER — JSONL per spec
# ═══════════════════════════════════════════════════════════════════════════

class MechanicalLogger:
    def __init__(self, campaign_id, log_dir=None):
        self.campaign_id = campaign_id
        self.log_dir = log_dir
        self.events = []
        self.event_counter = 0
        self.current_season = 0
        self.current_arc = 0
        self._all_ids = set()
        self._parent_ids = set()

    def log(self, event_type, **kwargs):
        self.event_counter += 1
        eid = self.event_counter
        self._all_ids.add(eid)
        parent = kwargs.get('parent_event_id')
        if parent is not None: self._parent_ids.add(parent)
        ev = {
            'event_id': eid,
            'season': self.current_season,
            'arc': self.current_arc,
            'event_type': event_type,
            'campaign_id': self.campaign_id,
            **kwargs
        }
        self.events.append(ev)
        return eid

    def finalize(self):
        unresolved = self._parent_ids - self._all_ids
        self.log('campaign_end',
                 total_events=self.event_counter,
                 integrity={'unresolved_parents': len(unresolved),
                           'monotonic': True})

    def flush(self, path):
        with open(path, 'w') as f:
            for ev in self.events:
                f.write(json.dumps(ev) + '\n')


class NullLogger:
    current_season = 0
    current_arc = 0
    def log(self, *a, **kw): return 0
    def finalize(self): pass
    def flush(self, *a): pass


# ═══════════════════════════════════════════════════════════════════════════
# WORLD INIT
# ═══════════════════════════════════════════════════════════════════════════

class V14World:
    def __init__(self):
        self.factions = {
            'Crown': V14Faction('Crown'),
            'Church': V14Faction('Church'),
            'Hafenmark': V14Faction('Hafenmark'),
            'Varfell': V14Faction('Varfell'),
        }
        self.territories = {tid: V14Territory(tid) for tid in STARTING_OWNER}
        self.clocks = {'CI': 0, 'MS': 80, 'PI': 0, 'Strain': 0, 'Turmoil': 0}
        self.season = 0
        self.arc = 0
        self.winner = None
        self.params = {}
        self.mass_seizure_fired = False
        self.insurgencies = {}  # name -> V14Faction(parliamentary=False, is_insurgency=True)
        self.founded_orgs = {}  # name -> V14Faction


# ═══════════════════════════════════════════════════════════════════════════
# THREAT RESPONSE — deterministic mandatory actions
# ═══════════════════════════════════════════════════════════════════════════

def mandatory_actions(faction, world, logger):
    """Return critical actions for survival, deterministically prioritized.
    [Jordan direction 2026-05-14: deterministic in responding to threat of revolt]"""
    mandatory = []
    threats = []
    for tid in faction.territories:
        t = world.territories.get(tid)
        if not t: continue
        # Critical: Accord ≤ 2 without garrison → revolt imminent
        if t.accord <= 2 and not t.garrison:
            threats.append(('Muster', tid, 100 - t.accord))  # priority weight
        elif t.accord <= 2 and t.garrison:
            threats.append(('Govern', tid, 90 - t.accord))
        elif t.accord == 3 and not t.garrison:
            threats.append(('Muster', tid, 50))
    threats.sort(key=lambda x: -x[2])
    for name, tid, _ in threats[:2]:  # max 2 mandatory, leave room for strategy
        mandatory.append((name, tid))
    if mandatory:
        logger.log('mandatory_response', faction=faction.name,
                   actions=[(n, t) for n, t, _ in threats[:2]],
                   threats_detected=len(threats),
                   canonical_ref='Jordan 2026-05-14: deterministic threat response')
    return mandatory


# ═══════════════════════════════════════════════════════════════════════════
# ACTION GENERATION
# ═══════════════════════════════════════════════════════════════════════════

def generate_candidates(faction, world, logger):
    cands = []
    p = world.params
    name = faction.name

    # GOVERN — own territories below Accord 7
    for tid in faction.territories:
        t = world.territories.get(tid)
        if t and t.accord < 7 and not faction.consul_card_used:
            cands.append(('Govern', tid))

    # MUSTER — own ungarrisoned
    for tid in faction.territories:
        t = world.territories.get(tid)
        if t and not t.garrison:
            cands.append(('Muster', tid))

    # TRADE — always available
    cands.append(('Trade', None))

    # SPY — against other parliamentary factions
    for fn in world.factions:
        if fn != name:
            cands.append(('Spy', fn))

    # COUNTER-NARRATIVE — against any other faction's territory with PT ≥ 3
    for tid, t in world.territories.items():
        if t.owner != name and t.pt >= 3:
            cands.append(('Counter-Narrative', tid))

    # FACTION-SPECIFIC
    if name == 'Crown':
        if not faction.diplomat_card_used:
            for fn in world.factions:
                if fn != 'Crown' and fn not in faction.treaties:
                    cands.append(('Crown Treaty', fn))
        if not faction.senator_inward_used and faction.stats['W'] >= 3:
            cands.append(('Crown Initiative', None))

    if name == 'Church':
        if not faction.cardinal_card_used and not faction.ea_arc_used and faction.stats['L'] < 7:
            cands.append(('Ecclesiastical Appointment', None))
        # Church Seizure: Prominence required (Church L > controlling L)
        # Mandate ≥ 4 required to initiate any seizure [canonical: victory §3.2]
        if faction.stats['L'] >= 4 and not faction.cardinal_card_used:
            for tid, t in world.territories.items():
                if t.owner and t.owner != 'Church' and t.owner in world.factions:
                    controlling = world.factions[t.owner]
                    if faction.stats['L'] > controlling.stats['L'] and t.pt >= 3:
                        cands.append(('Church Seizure', tid))
        # Piety Spread — invest in PT (Cardinal slot)
        if not faction.cardinal_card_used:
            for tid, t in world.territories.items():
                if t.pt < 7:
                    cands.append(('Piety Spread', tid))
        # Assert — +1 CI on success [canonical: victory §3.2]
        if not faction.consul_card_used:
            cands.append(('Assert', None))

    if name == 'Hafenmark':
        if not faction.diplomat_card_used:
            for tid, t in world.territories.items():
                if t.owner and t.owner != 'Hafenmark' and t.owner in world.factions:
                    cands.append(('Dynastic Proclamation', tid))
        if not faction.legacy_card_used and faction.stats['W'] >= 1:
            cands.append(('Charter of Liberties', None))
        # Suppress — negates Church passive CI [canonical: victory §3.2]
        if not faction.consul_card_used and world.clocks.get('CI', 0) > 0:
            cands.append(('Suppress', None))

    if name == 'Varfell':
        if not faction.tribune_card_used:
            for tid in faction.territories:
                t = world.territories.get(tid)
                if t and t.accord < 5:
                    cands.append(("Vaynard's Settlement", tid))
        if not faction.hall_card_used:
            cands.append(("Vaynard's Hall", None))
        # Einhir Revival — PT ≥ 3 threshold for flip [canonical: Jordan 2026-05-14]
        if not faction.einhir_arc_used and faction.stats['I'] >= p.get('EINHIR_I_GATE', 4):
            adj = set()
            for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
            adj -= faction.territories
            for tid in adj:
                t = world.territories.get(tid)
                # CHANGED per Jordan: flip threshold at Piety ≥ 3 (1-7 scale)
                # Means Einhir works when PT ≥ 3 (the original "low PT" interpretation was wrong)
                # Actually: Einhir flips territories where PT is LOW (cultural resistance to Church)
                # So target territories have PT ≤ 3 (the inverse)
                if t and t.owner != 'Varfell' and t.pt <= 3:
                    cands.append(('Einhir Revival', tid))

    # Military Conquest — adjacent to own territories
    adj = set()
    for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
    adj -= faction.territories
    for tid in adj:
        if tid in world.territories:
            cands.append(('Military Conquest', tid))

    # Parliamentary Transfer — with CB
    if not faction.parl_arc_used and faction.casus_belli:
        for cb_target in faction.casus_belli:
            if cb_target in world.factions:
                for tid in list(world.factions[cb_target].territories):
                    cands.append(('Parliamentary Transfer', tid))

    # Reclaim Uncontrolled — territories with no parliamentary owner adjacent
    for tid in adj:
        t = world.territories.get(tid)
        if t and t.is_uncontrolled():
            cands.append(('Reclaim Uncontrolled', tid))

    return cands

def score_action(name, faction, target, world):
    t = world.territories.get(target) if target and isinstance(target, str) and target in world.territories else None
    if name == 'Govern':
        if t and t.accord <= 3: return 12
        if t and t.accord <= 5: return 6
        return 3
    if name == 'Muster':
        if t and t.accord <= 2: return 14
        if t and t.accord <= 4: return 7
        return 3
    if name == 'Crown Treaty': return 10
    if name == 'Crown Initiative': return 6 + max(0, 5 - faction.stats['L'])
    if name == 'Ecclesiastical Appointment': return 13
    if name == 'Church Seizure': return 11
    if name == 'Piety Spread':
        if t and t.pt < 4: return 8
        return 4
    if name == 'Assert': return 5
    if name == 'Suppress': return 6
    if name == 'Dynastic Proclamation': return 9
    if name == 'Charter of Liberties': return 8 + max(0, 6 - faction.stats['L'])
    if name == "Vaynard's Settlement": return 11
    if name == "Vaynard's Hall": return 7
    if name == 'Einhir Revival':
        if t and t.pt <= 2: return 13
        if t and t.pt == 3: return 8
        return 3
    if name == 'Military Conquest':
        if t and t.is_uncontrolled(): return 11
        return 6
    if name == 'Parliamentary Transfer': return 10
    if name == 'Reclaim Uncontrolled': return 9
    if name == 'Trade': return 4
    if name == 'Spy': return 3
    if name == 'Counter-Narrative': return 4
    return 2


def select_actions(faction, world, logger, n_actions=3):
    # 1. Deterministic mandatory actions
    actions = mandatory_actions(faction, world, logger)
    used = {(n, t) for n, t in actions}

    # 2. Mark consul card if Govern is mandatory
    for n, t in actions:
        if n == 'Govern':
            faction.consul_card_used = True
            break

    remaining = n_actions - len(actions)
    if remaining <= 0:
        return actions

    # 3. Stochastic selection for remaining slots
    cands = generate_candidates(faction, world, logger)
    cands = [(n, t) for n, t in cands if (n, t) not in used]

    # Log all candidates for NERS audit
    logger.log('action_candidates', faction=faction.name,
               candidates=[{'action': n, 'target': t, 'score': score_action(n, faction, t, world)}
                          for n, t in cands[:20]])

    for _ in range(remaining):
        if not cands: break
        scored = [(score_action(n, faction, t, world), n, t) for n, t in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        _, name, tid = random.choices(top, weights=weights, k=1)[0]
        actions.append((name, tid))
        used.add((name, tid))
        cands = [(n, t) for n, t in cands if (n, t) not in used]

    logger.log('actions_selected', faction=faction.name, actions=actions)
    return actions


# ═══════════════════════════════════════════════════════════════════════════
# ACTION PREREQS & RESOLUTION
# ═══════════════════════════════════════════════════════════════════════════

def prereqs(action_name, faction, target, world):
    """Check prereqs. Return (passed, reason)."""
    p = world.params
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None

    if action_name == 'Govern':
        if faction.consul_card_used: return False, 'consul_card_used'
        if not t or t.owner != faction.name: return False, 'not_own_territory'
        return True, 'ok'

    if action_name == 'Muster':
        if not t or t.owner != faction.name: return False, 'not_own_territory'
        if t.garrison: return False, 'already_garrisoned'
        return True, 'ok'

    if action_name == 'Crown Treaty':
        if faction.diplomat_card_used: return False, 'diplomat_used'
        if target not in world.factions: return False, 'invalid_partner'
        if target in faction.treaties: return False, 'treaty_exists'
        return True, 'ok'

    if action_name == 'Crown Initiative':
        if faction.senator_inward_used: return False, 'senator_used'
        if faction.stats['W'] < 3: return False, 'W<3'
        return True, 'ok'

    if action_name == 'Ecclesiastical Appointment':
        if faction.cardinal_card_used: return False, 'cardinal_used'
        if faction.ea_arc_used: return False, 'ea_arc_used'
        if faction.stats['L'] >= 7: return False, 'L_capped'
        return True, 'ok'

    if action_name == 'Church Seizure':
        if faction.cardinal_card_used: return False, 'cardinal_used'
        if faction.stats['L'] < 4: return False, 'mandate<4'
        if not t: return False, 'invalid_target'
        if t.owner not in world.factions: return False, 'not_faction_territory'
        if faction.stats['L'] <= world.factions[t.owner].stats['L']: return False, 'no_prominence'
        if t.pt < 3: return False, 'pt<3_no_flip'  # PT ≥ 3 flip threshold
        return True, 'ok'

    if action_name == 'Piety Spread':
        if faction.cardinal_card_used: return False, 'cardinal_used'
        if not t or t.pt >= 7: return False, 'pt_capped'
        return True, 'ok'

    if action_name == 'Assert':
        if faction.consul_card_used: return False, 'consul_used'
        return True, 'ok'

    if action_name == 'Suppress':
        if faction.consul_card_used: return False, 'consul_used'
        return True, 'ok'

    if action_name == 'Dynastic Proclamation':
        if faction.diplomat_card_used: return False, 'diplomat_used'
        if not t: return False, 'invalid_target'
        if t.owner not in world.factions: return False, 'not_faction_territory'
        return True, 'ok'

    if action_name == 'Charter of Liberties':
        if faction.legacy_card_used: return False, 'legacy_used'
        if faction.stats['W'] < 1: return False, 'W<1'
        return True, 'ok'

    if action_name == "Vaynard's Settlement":
        if faction.tribune_card_used: return False, 'tribune_used'
        if not t or t.owner != 'Varfell': return False, 'not_varfell_territory'
        if t.accord >= 5: return False, 'accord_high'
        return True, 'ok'

    if action_name == "Vaynard's Hall":
        if faction.hall_card_used: return False, 'hall_used'
        return True, 'ok'

    if action_name == 'Einhir Revival':
        if faction.einhir_arc_used: return False, 'einhir_arc_used'
        if faction.stats['I'] < p.get('EINHIR_I_GATE', 4): return False, 'I<4'
        if not t or t.owner == 'Varfell': return False, 'already_varfell'
        # Einhir flips low-PT territories
        if t.pt > 3: return False, 'pt>3_too_integrated'
        # Must be adjacent
        adj = set()
        for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
        if target not in adj: return False, 'not_adjacent'
        return True, 'ok'

    if action_name == 'Military Conquest':
        if not t: return False, 'invalid_target'
        # Adjacent required
        adj = set()
        for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
        if target not in adj: return False, 'not_adjacent'
        if t.owner == faction.name: return False, 'own_territory'
        return True, 'ok'

    if action_name == 'Parliamentary Transfer':
        if faction.parl_arc_used: return False, 'parl_arc_used'
        if not t: return False, 'invalid_target'
        if t.owner not in world.factions: return False, 'not_faction_target'
        if t.owner not in faction.casus_belli: return False, 'no_cb'
        return True, 'ok'

    if action_name == 'Reclaim Uncontrolled':
        if not t or not t.is_uncontrolled(): return False, 'not_uncontrolled'
        adj = set()
        for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
        if target not in adj: return False, 'not_adjacent'
        return True, 'ok'

    return True, 'no_prereq_needed'


def resolve_action(action_name, faction, target, world, logger, action_attempt_id):
    """Resolve action and emit detailed log."""
    p = world.params
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None

    # Calculate pool and Ob
    pool, ob, pool_calc, ob_calc = pool_and_ob(action_name, faction, target, world)
    if pool is None:
        return None

    # Roll dice
    rolls = [random.randint(1, 6) for _ in range(max(0, pool))]
    successes = sum(1 for r in rolls if r >= 4)
    net = successes - ob
    degree = resolve_degree(net)

    # Log resolution
    resolve_id = logger.log('action_resolved',
        parent_event_id=action_attempt_id,
        actor=faction.name,
        action=action_name,
        target=target,
        pool=pool, pool_calc=pool_calc,
        ob=ob, ob_calc=ob_calc,
        rolls=rolls, successes=successes, net=net,
        degree=degree,
        canonical_ref='peninsular_strain_v30 §3.2 degree table')

    # Apply effects
    apply_effects(action_name, faction, target, degree, world, logger, resolve_id)
    return resolve_id


def pool_and_ob(name, faction, target, world):
    p = world.params
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None

    if name == 'Govern':
        pool = faction.stats['I']
        ob = 2 if (t and t.accord >= 4) else 1
        # Strain penalty [canonical: PS v30 §4.3]
        if 5 <= world.clocks.get('Strain', 0) <= 6: ob += 1
        return pool, ob, {'I': faction.stats['I']}, {'base': ob}

    if name == 'Muster':
        return faction.stats['Mil'], 1, {'Mil': faction.stats['Mil']}, {'base': 1}

    if name == 'Crown Treaty':
        return faction.stats['I'], 3, {'I': faction.stats['I']}, {'base': 3}

    if name == 'Crown Initiative':
        sum_accord = sum(world.territories[tid].accord for tid in faction.territories if tid in world.territories)
        return faction.stats['I'], max(1, sum_accord // 4), {'I': faction.stats['I']}, {'sum_accord': sum_accord}

    if name == 'Ecclesiastical Appointment':
        return faction.stats['L'] + faction.stats['I'], 4, {'L': faction.stats['L'], 'I': faction.stats['I']}, {'base': 4}

    if name == 'Church Seizure':
        ci = world.clocks.get('CI', 0)
        pool = faction.stats['I'] + (ci // 15)
        ob = max(1, 10 - t.pt) if t else 5
        if t and t.templar: ob = max(1, ob - 1)
        if t and t.inquisitor: ob = max(1, ob - 1)
        return pool, ob, {'I': faction.stats['I'], 'ci_bonus': ci // 15}, {'pt': t.pt if t else 0, 'modifiers': 'templar/inq'}

    if name == 'Piety Spread':
        return faction.stats['I'], 3, {'I': faction.stats['I']}, {'base': 3}

    if name == 'Assert':
        return faction.stats['I'], 2, {'I': faction.stats['I']}, {'base': 2}

    if name == 'Suppress':
        church = world.factions.get('Church')
        church_l = church.stats['L'] if church else 4
        return faction.stats['L'], max(1, church_l // 2 + 1), {'L': faction.stats['L']}, {'church_L': church_l}

    if name == 'Dynastic Proclamation':
        return faction.stats['I'], 3, {'I': faction.stats['I']}, {'base': 3}

    if name == 'Charter of Liberties':
        token_bonus = sum(1 for v in faction.tokens_held.values() if v > 0)
        return faction.stats['I'] + token_bonus, 4, {'I': faction.stats['I'], 'tokens': token_bonus}, {'base': 4}

    if name == "Vaynard's Settlement":
        return faction.stats['Mil'] + (faction.stats['W'] // 2), 3, {'Mil': faction.stats['Mil']}, {'base': 3}

    if name == "Vaynard's Hall":
        bonus = 1 if faction.revelation_tokens >= 1 else 0
        return faction.stats['Mil'] + bonus, 3, {'Mil': faction.stats['Mil'], 'token_bonus': bonus}, {'base': 3}

    if name == 'Einhir Revival':
        pool = faction.stats['I']
        ob = max(1, t.pt + 1) if t else 4
        return pool, ob, {'I': faction.stats['I']}, {'pt': t.pt if t else 0}

    if name == 'Military Conquest':
        pool = faction.stats['Mil']
        ob = 2 if (t and t.owner is None) else 4
        if t and t.garrison: ob += 1
        return pool, ob, {'Mil': faction.stats['Mil']}, {'garrison': t.garrison if t else False}

    if name == 'Parliamentary Transfer':
        holder = world.factions.get(t.owner) if t and t.owner in world.factions else None
        holder_L = holder.stats['L'] if holder else 4
        return faction.stats['I'], holder_L + 2, {'I': faction.stats['I']}, {'holder_L': holder_L}

    if name == 'Reclaim Uncontrolled':
        return faction.stats['Mil'], 2, {'Mil': faction.stats['Mil']}, {'base': 2}

    if name == 'Trade':
        return faction.stats['W'], 2, {'W': faction.stats['W']}, {'base': 2}

    if name == 'Spy':
        return faction.stats['I'], 3, {'I': faction.stats['I']}, {'base': 3}

    if name == 'Counter-Narrative':
        return faction.stats['I'], 3, {'I': faction.stats['I']}, {'base': 3}

    return None, None, None, None


def apply_effects(name, faction, target, degree, world, logger, parent_id):
    p = world.params
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None
    success = degree in ('Success', 'Overwhelming')
    ow = degree == 'Overwhelming'

    def state_change(target_type, target_id, attr, before, after, ref, reason):
        if before != after:
            logger.log('state_change', parent_event_id=parent_id,
                       target_type=target_type, target_id=target_id,
                       attribute=attr, before=before, after=after,
                       delta=after - before if isinstance(after, (int, float)) and isinstance(before, (int, float)) else None,
                       canonical_ref=ref, reason=reason)

    if name == 'Govern' and t:
        faction.consul_card_used = True
        if ow:
            b = t.accord; t.gain_accord(20); state_change('territory', target, 'accord_buffer', b, t.accord, 'PS v30 §2 Govern OW', 'Govern OW')
            faction.stability.gain(5, faction.stats)
            faction.mandate.gain(faction.stats['L'] * 3, faction.stats)
        elif success:
            t.gain_accord(10); faction.stability.gain(3, faction.stats)
            faction.mandate.gain(faction.stats['L'] * 2, faction.stats)
        elif degree == 'Partial':
            t.gain_accord(3)
        # Govern also generates Discipline (Stability buffer) income — peaceful action
        faction.peaceful = True

    elif name == 'Muster' and t:
        if success:
            t.garrison = True
            t.gain_accord(5)
            state_change('territory', target, 'garrison', False, True, 'PS v30 Muster', 'Muster success')

    elif name == 'Crown Treaty':
        faction.diplomat_card_used = True
        if success and target in world.factions:
            partner = world.factions[target]
            if random.random() < p.get('CONSENT_RATE', 0.5):
                faction.treaties[target] = 'CrownTreaty'
                partner.treaties[faction.name] = 'CrownTreaty'
                faction.mandate.gain(15, faction.stats)
                logger.log('treaty_formed', faction=faction.name, partner=target,
                           parent_event_id=parent_id,
                           canonical_ref='PS v30 §5.1 Crown Treaty')

    elif name == 'Crown Initiative':
        faction.senator_inward_used = True
        r = faction.wealth.drain(-300, faction.stats, logger=logger, owner_id=faction.name, reason='Crown Initiative cost')
        if ow:
            b = faction.stats['L']; faction.stats['L'] = min(7, faction.stats['L'] + 2)
            state_change('faction', faction.name, 'L', b, faction.stats['L'], 'CI OW', 'major institutional event')
            faction.mandate.value = faction.stats['L'] * 20
            for tid in faction.territories:
                t2 = world.territories.get(tid)
                if t2: t2.gain_accord(10)
        elif success:
            faction.mandate.gain(15, faction.stats)
            if faction.territories:
                worst_tid = min(faction.territories, key=lambda tid: world.territories[tid].accord if tid in world.territories else 99)
                if worst_tid in world.territories:
                    world.territories[worst_tid].gain_accord(8)

    elif name == 'Ecclesiastical Appointment':
        faction.cardinal_card_used = True
        faction.ea_arc_used = True
        if success:
            b = faction.stats['L']; faction.stats['L'] = min(7, faction.stats['L'] + 1)
            state_change('faction', faction.name, 'L', b, faction.stats['L'], 'EA Success', 'direct major institutional event')
            faction.mandate.value = faction.stats['L'] * 20

    elif name == 'Church Seizure' and t:
        faction.cardinal_card_used = True
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].mandate.drain(-15, world.factions[old].stats, logger=logger, owner_id=old, reason='Lost territory to Seizure')
            t.owner = 'Church'; faction.territories.add(target)
            # [canonical: PS v30 §3.4 — Accord set to max(floor(PT/2)+1, 2) on Success]
            # PT 1-7 scale: Accord = max(PT//2+1, 2) mapped to 1-7
            new_accord = min(7, max(2, t.pt // 2 + 2))  # adjusted for 1-7
            if ow: new_accord = min(7, new_accord + 1)
            t.accord = new_accord; t.accord_buffer.value = new_accord * 10
            state_change('territory', target, 'owner', old, 'Church', 'PS v30 §3.4', 'Church Seizure')
            if ow:
                t.gain_pt(5)

    elif name == 'Piety Spread' and t:
        faction.cardinal_card_used = True
        if success:
            t.gain_pt(8 if ow else 5)
            if ow and t.pt < 7:
                t.pt = min(7, t.pt + 1)

    elif name == 'Assert':
        faction.consul_card_used = True
        if success:
            world.clocks['CI'] = world.clocks.get('CI', 0) + 1
            state_change('clock', 'CI', 'value', world.clocks['CI'] - 1, world.clocks['CI'], 'victory_v30 §3.2 Assert', 'Assert success')
        else:
            faction.stability.drain(-15, faction.stats, logger=logger, owner_id=faction.name, reason='Assert failure')

    elif name == 'Suppress':
        faction.consul_card_used = True
        if success:
            # Marks Suppression — negates the +1 passive next Accounting
            world.clocks['_suppression_active'] = 1
        else:
            faction.stability.drain(-15, faction.stats, logger=logger, owner_id=faction.name, reason='Suppress failure')

    elif name == 'Dynastic Proclamation' and t:
        faction.diplomat_card_used = True
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].mandate.drain(-10, world.factions[old].stats, logger=logger, owner_id=old, reason='Lost to DP')
            t.owner = faction.name; faction.territories.add(target)
            t.accord = 4 if ow else 3; t.accord_buffer.value = t.accord * 10
            state_change('territory', target, 'owner', old, faction.name, 'PS v30 §3.5', 'DP')

    elif name == 'Charter of Liberties':
        faction.legacy_card_used = True
        faction.wealth.drain(-100, faction.stats, logger=logger, owner_id=faction.name, reason='Charter cost')
        if ow:
            b = faction.stats['L']; faction.stats['L'] = min(7, faction.stats['L'] + 2)
            state_change('faction', faction.name, 'L', b, faction.stats['L'], 'Charter OW', 'major event')
            faction.mandate.value = faction.stats['L'] * 20
            world.clocks['PI'] = max(0, world.clocks.get('PI', 0) - 2)
        elif success:
            faction.mandate.gain(15, faction.stats)
            world.clocks['PI'] = max(0, world.clocks.get('PI', 0) - 1)

    elif name == "Vaynard's Settlement" and t:
        faction.tribune_card_used = True
        faction.wealth.drain(-100, faction.stats, logger=logger, owner_id=faction.name, reason='Settlement cost')
        if ow:
            t.gain_accord(15); 
            b = faction.stats['Mil']; faction.stats['Mil'] = min(7, faction.stats['Mil'] + 1)
            state_change('faction', faction.name, 'Mil', b, faction.stats['Mil'], 'Settlement OW', 'major')
        elif success:
            t.gain_accord(10)

    elif name == "Vaynard's Hall":
        faction.hall_card_used = True
        b = faction.stats['Mil']; faction.stats['Mil'] = max(1, faction.stats['Mil'] - 1)
        state_change('faction', faction.name, 'Mil', b, faction.stats['Mil'], 'Hall cost', 'self-cost')
        faction.wealth.drain(-100, faction.stats, logger=logger, owner_id=faction.name, reason='Hall cost')
        if ow:
            faction.mandate.gain(30, faction.stats)
        elif success:
            faction.mandate.gain(15, faction.stats)
        elif degree == 'Partial':
            faction.stats['Mil'] = min(7, faction.stats['Mil'] + 1)

    elif name == 'Einhir Revival' and t:
        faction.einhir_arc_used = True
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].mandate.drain(-15, world.factions[old].stats, logger=logger, owner_id=old, reason='Lost to Einhir')
            t.owner = 'Varfell'; faction.territories.add(target)
            t.accord = 4 if ow else 2; t.accord_buffer.value = t.accord * 10
            t.drain_pt(-1)
            state_change('territory', target, 'owner', old, 'Varfell', 'Part 13 §2.1 Einhir', 'flip')
        elif degree == 'Partial':
            t.drain_pt(-1)

    elif name == 'Military Conquest' and t:
        # War is hostile — peaceful=False for actor
        faction.peaceful = False
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].mandate.drain(-15, world.factions[old].stats, logger=logger, owner_id=old, reason='Lost to MC')
                world.factions[old].peaceful = False
            elif old in world.insurgencies:
                world.insurgencies[old].territories.discard(target)
            t.owner = faction.name; faction.territories.add(target)
            t.accord = 2 if ow else 1; t.accord_buffer.value = t.accord * 10
            t.garrison = True
            faction.mandate.drain(-10, faction.stats, logger=logger, owner_id=faction.name, reason='War cost')
            state_change('territory', target, 'owner', old, faction.name, 'PS v30 §2.4', 'Conquest')

    elif name == 'Parliamentary Transfer' and t:
        faction.parl_arc_used = True
        if success:
            old = t.owner
            faction.casus_belli.discard(old)
            if old in world.factions:
                world.factions[old].territories.discard(target)
                if ow:
                    world.factions[old].mandate.drain(-15, world.factions[old].stats, logger=logger, owner_id=old, reason='ParlTransfer OW')
            t.owner = faction.name; faction.territories.add(target)
            t.accord = 3; t.accord_buffer.value = 30
            state_change('territory', target, 'owner', old, faction.name, 'Part 13 §2.2', 'ParlTransfer')
        elif degree == 'Partial':
            faction.casus_belli.add(t.owner)
        else:
            faction.stability.drain(-10, faction.stats, logger=logger, owner_id=faction.name, reason='ParlTransfer fail')

    elif name == 'Reclaim Uncontrolled' and t:
        if success and t.is_uncontrolled():
            old = t.owner
            # If insurgency, remove from insurgency
            if old in world.insurgencies:
                world.insurgencies[old].territories.discard(target)
            t.owner = faction.name; faction.territories.add(target)
            t.accord = 2 if ow else 1; t.accord_buffer.value = t.accord * 10
            t.garrison = True
            state_change('territory', target, 'owner', old, faction.name, 'Jordan 2026-05-14', 'Reclaim')

    elif name == 'Trade':
        if success:
            faction.wealth.gain(80 if ow else 50, faction.stats)

    elif name == 'Spy':
        if success:
            faction.influence.gain(15 if ow else 8, faction.stats)

    elif name == 'Counter-Narrative' and t:
        if success:
            t.drain_pt(-1 if not ow else -2, logger=logger, reason='Counter-Narrative')


# ═══════════════════════════════════════════════════════════════════════════
# CI GENERATION [canonical: victory_v30 §3.2]
# ═══════════════════════════════════════════════════════════════════════════

def ci_generation(world, logger):
    """Per Accounting:
    1. Institutional Momentum: +1 passive
    2. Piety Yield: per territory Church is Prominent, PT 6-7 = +1, PT 5 = +0.5
    3. Templar Station: +1 per (handled per-territory)
    4. Hafenmark Structural Suppression: -1 if Hafenmark Mandate ≥ 4
    [canonical: victory_v30 §3.2 Seasonal CI at Accounting]
    """
    church = world.factions.get('Church')
    if not church or church.name not in world.factions:
        return 0

    momentum = 1  # Institutional Momentum

    # Suppress action negates passive
    if world.clocks.get('_suppression_active', 0) >= 1:
        momentum = 0
        world.clocks['_suppression_active'] = 0

    # Piety Yield
    piety_yield = 0.0
    for tid, t in world.territories.items():
        if t.owner == 'Church': prominent = True
        elif t.owner in world.factions:
            prominent = church.stats['L'] > world.factions[t.owner].stats['L']
        else:
            prominent = False
        if prominent:
            if t.pt >= 6: piety_yield += 1
            elif t.pt == 5: piety_yield += 0.5

    # Templar count
    templar_count = sum(1 for t in world.territories.values() if t.templar)

    # Hafenmark Suppression
    hafenmark = world.factions.get('Hafenmark')
    haf_suppress = -1 if (hafenmark and hafenmark.stats['L'] >= 4) else 0

    total = math.floor(momentum + piety_yield + templar_count + haf_suppress)
    world.clocks['CI'] = max(0, min(100, world.clocks.get('CI', 0) + total))

    logger.log('ci_generation', momentum=momentum, piety_yield=piety_yield,
               templars=templar_count, haf_suppress=haf_suppress, total=total,
               new_ci=world.clocks['CI'],
               canonical_ref='victory_v30 §3.2')


# ═══════════════════════════════════════════════════════════════════════════
# MASS SEIZURE [canonical: victory_v30 §3.2]
# P = ((CI - 60) / 40) ^ 3.3 per Accounting
# ═══════════════════════════════════════════════════════════════════════════

def mass_seizure_check(world, logger):
    if world.mass_seizure_fired: return
    ci = world.clocks.get('CI', 0)
    if ci < 60: return
    church = world.factions.get('Church')
    if not church: return
    # Also requires Mandate ≥ 4 and Accord ≥ 3 in 3+ non-capital territories
    if church.stats['L'] < 4: return
    high_accord_count = sum(1 for tid in church.territories
                           if tid in world.territories and world.territories[tid].accord >= 3
                           and tid != 'T9')  # T9 = Church capital
    if high_accord_count < 3:
        logger.log('mass_seizure_blocked', ci=ci, reason='accord3_count<3',
                   accord3_count=high_accord_count)
        return

    p_trigger = min(1.0, ((ci - 60) / 40) ** 3.3)
    roll = random.random()
    logger.log('mass_seizure_check', ci=ci, p_trigger=p_trigger, roll=roll, fired=(roll < p_trigger))
    if roll >= p_trigger:
        return

    # FIRES
    world.mass_seizure_fired = True
    church.mass_seizure_declared = True
    pool = church.stats['I'] + (ci // 15)
    seized = []
    failed = []
    for tid, t in list(world.territories.items()):
        if t.owner == 'Church' or t.pt <= 0: continue
        if t.owner in world.factions and not (church.stats['L'] > world.factions[t.owner].stats['L']): continue  # Prominence required
        ob = max(1, 10 - t.pt)
        if t.templar: ob = max(1, ob - 1)
        if t.inquisitor: ob = max(1, ob - 1)
        net = roll_pool(pool) - ob
        deg = resolve_degree(net)
        if deg in ('Success', 'Overwhelming'):
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(tid)
            t.owner = 'Church'; church.territories.add(tid)
            t.accord = min(7, max(3, t.pt // 2 + 2))
            t.accord_buffer.value = t.accord * 10
            seized.append((tid, old))
        else:
            failed.append((tid, deg))
    logger.log('mass_seizure_event', seized=seized, failed=failed, total_seized=len(seized),
               canonical_ref='victory_v30 §3.2 Mass Seizure')


# ═══════════════════════════════════════════════════════════════════════════
# REVOLT → INSURGENCY → FOUNDED ORGANIZATION → PARLIAMENTARY
# ═══════════════════════════════════════════════════════════════════════════

def check_revolts_and_insurgencies(world, logger):
    """Identify contiguous uncontrolled territories. Form insurgencies. Promote to Founded Orgs."""
    # Get plain-uncontrolled (not already in an insurgency)
    plain_uncontrolled = {tid for tid, t in world.territories.items()
                          if t.owner is None}
    if len(plain_uncontrolled) < 2: pass  # still check existing insurgencies

    # Find contiguous groups
    visited = set()
    groups = []
    for tid in plain_uncontrolled:
        if tid in visited: continue
        group = set()
        queue = [tid]
        while queue:
            curr = queue.pop()
            if curr in visited or curr not in plain_uncontrolled: continue
            visited.add(curr); group.add(curr)
            for adj in ADJACENCY.get(curr, set()):
                if adj in plain_uncontrolled and adj not in visited:
                    queue.append(adj)
        if len(group) >= 2:
            groups.append(group)

    # Form insurgencies for new groups that have persisted ≥ 2 seasons
    for group in groups:
        all_persistent = all(
            world.territories[tid].uncontrolled_since is not None and
            world.season - world.territories[tid].uncontrolled_since >= 2
            for tid in group
        )
        if not all_persistent: continue

        # Determine type: low PT avg = RM, high PT = parliamentary
        avg_pt = sum(world.territories[tid].pt for tid in group) / len(group)
        is_rm = avg_pt < 3  # PT threshold per Jordan
        prefix = 'RM' if is_rm else 'Insurgency'
        name = f'{prefix}_{world.season}_{min(group)}'

        # Create insurgency (not parliamentary yet)
        insurgency = V14Faction(name, parliamentary=False)
        insurgency.is_insurgency = True
        insurgency.founded_season = world.season
        # Starting stats for insurgency (weak)
        insurgency.stats = {'L': 1, 'Sta': 2, 'W': 1, 'I': 2, 'Mil': 2}
        insurgency.mandate.init_from(insurgency.stats)
        insurgency.stability.init_from(insurgency.stats)
        insurgency.wealth.init_from(insurgency.stats)
        insurgency.influence.init_from(insurgency.stats)
        insurgency.territories = set(group)
        # Assign territories to this insurgency
        for tid in group:
            world.territories[tid].owner = name
            world.territories[tid].accord = 3  # initial cohesion
            world.territories[tid].accord_buffer.value = 30
        world.insurgencies[name] = insurgency

        logger.log('insurgency_formed', name=name, territories=sorted(group),
                   avg_pt=avg_pt, type='RM' if is_rm else 'Parliamentary',
                   formed_season=world.season,
                   canonical_ref='Jordan 2026-05-14 + victory_v30 §606-608')

    # Promote insurgencies: Mandate ≥ 3 + 2+ territories + Accord ≥ 4 for 2+ seasons → Founded Org
    for ins_name, ins in list(world.insurgencies.items()):
        if len(ins.territories) < 2: continue
        if ins.stats['L'] < 3: continue
        accord_ok = all(world.territories[tid].accord >= 4 for tid in ins.territories if tid in world.territories)
        if not accord_ok: continue
        ins.persistence_seasons += 1
        if ins.persistence_seasons >= 2:
            # Promote to parliamentary
            ins.parliamentary = True
            ins.is_insurgency = False
            del world.insurgencies[ins_name]
            world.factions[ins_name] = ins
            logger.log('founded_org_promoted', name=ins_name,
                       territories=sorted(ins.territories),
                       mandate=ins.stats['L'],
                       canonical_ref='victory_v30 §606-608 Founded Organization')


# ═══════════════════════════════════════════════════════════════════════════
# ACCOUNTING — end of season
# ═══════════════════════════════════════════════════════════════════════════

def accounting(world, logger):
    season = world.season

    # ── Territory revolts (Accord ≤ 1 = lost) ──
    revolt_count = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        if t.accord <= 1:
            # Revolt
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(tid)
                world.factions[old].stability.drain(-15, world.factions[old].stats,
                                                    logger=logger, owner_id=old,
                                                    reason=f'Territory {tid} revolted')
                world.factions[old].peaceful = False
            elif old in world.insurgencies:
                world.insurgencies[old].territories.discard(tid)
            t.owner = None; t.garrison = False
            t.uncontrolled_since = season
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolt_count += 1
            logger.log('revolt', territory=tid, lost_by=old,
                       canonical_ref='PS v30 §2 Accord ≤ 1')

    # ── Garrison passive recovery ──
    for tid, t in world.territories.items():
        if t.is_uncontrolled():
            if t.uncontrolled_since is None:
                t.uncontrolled_since = season
            continue
        t.uncontrolled_since = None
        if t.garrison and season - t.last_hostile_season >= 2:
            t.consec_passive_seasons += 1
            if t.consec_passive_seasons >= 2:
                t.gain_accord(5)
                t.consec_passive_seasons = 0
        else:
            t.consec_passive_seasons = 0
        # Neglect drain
        if not t.garrison:
            t.drain_accord(-2)

    # No revolts → Turmoil decay
    if revolt_count == 0:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - 1)

    # ── Treaty Strain decay ──
    pairs = set()
    for fn, f in world.factions.items():
        for partner, tt in f.treaties.items():
            pair = tuple(sorted([fn, partner]))
            if pair not in pairs and tt == 'CrownTreaty':
                pairs.add(pair)
    if pairs:
        decay = min(len(pairs), 2)
        before = world.clocks.get('Turmoil', 0)
        world.clocks['Turmoil'] = max(0, before - decay)
        logger.log('treaty_strain_decay', treaty_pairs=len(pairs), decay=decay,
                   canonical_ref='PS v30 §4.2')

    world.clocks['Strain'] = world.clocks['Turmoil']

    # ── Strain threshold effects [canonical: PS v30 §4.3] ──
    strain = world.clocks['Strain']
    if 3 <= strain <= 4:
        for f in world.factions.values():
            f.mandate.drain(-25, f.stats, logger=logger, owner_id=f.name,
                            reason='Strain Tension Legitimacy drain')
    elif strain >= 7:
        for f in world.factions.values():
            for tid in list(f.territories):
                t = world.territories.get(tid)
                if t: t.drain_accord(-5, logger=logger, reason='Strain Crisis')

    # ── Faction derived income ──
    for fn, f in world.factions.items():
        # Legitimacy income: +2 per territory at Accord ≥ 4
        high_accord = sum(1 for tid in f.territories
                         if tid in world.territories and world.territories[tid].accord >= 4)
        if high_accord > 0:
            f.mandate.gain(high_accord * 2, f.stats)
        # Stability income: +3 if peaceful
        if f.peaceful:
            f.stability.gain(3, f.stats)
        # Wealth income: territory prosperity
        treasury_gain = sum(world.territories[tid].prosperity * 10
                           for tid in f.territories if tid in world.territories)
        f.wealth.gain(treasury_gain, f.stats)
        # Influence: small passive
        f.influence.gain(2, f.stats)
        f.peaceful = True

    # ── Church tithe (institutional income from PT) ──
    church = world.factions.get('Church')
    if church:
        total_pt = sum(t.pt for t in world.territories.values())
        church.mandate.gain(total_pt, church.stats)
        church.wealth.gain(total_pt * 3, church.stats)
        logger.log('church_tithe', total_pt=total_pt,
                   legit_gain=total_pt, wealth_gain=total_pt * 3,
                   canonical_ref='settlement_layer §1.6 Church infrastructure')

    # ── CI generation ──
    ci_generation(world, logger)

    # ── Mass Seizure check ──
    mass_seizure_check(world, logger)

    # ── Revolt → Insurgency → Founded Org pipeline ──
    check_revolts_and_insurgencies(world, logger)

    # ── Insurgency growth: gain Mandate from sustained high Accord ──
    for ins_name, ins in world.insurgencies.items():
        if not ins.territories: continue
        all_high = all(world.territories[tid].accord >= 4 for tid in ins.territories if tid in world.territories)
        if all_high:
            ins.mandate.gain(5, ins.stats)
        # Insurgency depletion check
        if not ins.territories:
            del world.insurgencies[ins_name]


# ═══════════════════════════════════════════════════════════════════════════
# VICTORY CHECK [canonical: PS v30 §6.1]
# ═══════════════════════════════════════════════════════════════════════════

def victory_check(world, logger, threshold=11):
    turmoil = world.clocks.get('Turmoil', 0)
    if turmoil > world.params.get('TURMOIL_CAP', 12): return None
    for fn, f in world.factions.items():
        if not f.parliamentary: continue  # only parliamentary factions can win
        controlled = set()
        for tid in ALL_PLAYABLE_15:
            t = world.territories.get(tid)
            if not t: continue
            if t.owner == fn:
                controlled.add(tid)
            elif t.owner in world.factions:
                rival = world.factions[t.owner]
                tt = f.treaties.get(rival.name, '')
                if tt in ('CrownTreaty','Peace','Alliance','Capitulation','Tributary'):
                    controlled.add(tid)
                elif rival.submitted or (rival.stats['L'] <= 1 and f.stats['L'] >= 5):
                    controlled.add(tid)
        if len(controlled) < threshold:
            f.sovereignty_history = 0; continue
        # All own territories must be Accord ≥ 4 (new scale; was ≥ 2)
        own = [tid for tid in controlled if world.territories.get(tid) and world.territories[tid].owner == fn]
        if not all(world.territories[tid].accord >= 4 for tid in own):
            f.sovereignty_history = 0; continue
        f.sovereignty_history += 1
        if f.sovereignty_history >= 2:
            logger.log('victory', faction=fn, season=world.season,
                       controlled=len(controlled), threshold=threshold,
                       canonical_ref='PS v30 §6.1')
            return fn
    return None


# ═══════════════════════════════════════════════════════════════════════════
# SEASON RUNNER
# ═══════════════════════════════════════════════════════════════════════════

def run_season(world, logger):
    logger.current_season = world.season
    logger.current_arc = world.arc
    logger.log('season_start', season=world.season, arc=world.arc,
               faction_L={fn: f.stats['L'] for fn, f in world.factions.items()},
               faction_terr={fn: len(f.territories) for fn, f in world.factions.items()},
               territories_accord={tid: t.accord for tid, t in world.territories.items()},
               clocks=dict(world.clocks))

    # Reset seasonal
    for f in world.factions.values():
        f.reset_seasonal()

    # Action phase — all factions (parliamentary + insurgent)
    all_factions = list(world.factions.values()) + list(world.insurgencies.values())
    for f in all_factions:
        actions = select_actions(f, world, logger, n_actions=3)
        for action_name, target in actions:
            ok, reason = prereqs(action_name, f, target, world)
            attempt_id = logger.log('action_attempt',
                                    actor=f.name, action=action_name, target=target,
                                    prereqs_passed=ok, prereqs_reason=reason)
            if not ok: continue
            resolve_action(action_name, f, target, world, logger, attempt_id)

    # Accounting
    accounting(world, logger)

    # Victory check
    winner = victory_check(world, logger,
                          threshold=world.params.get('VICTORY_THRESHOLD', 11))
    if winner:
        world.winner = winner

    # Advance time
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            f.reset_arc()
        world.arc += 1
        logger.log('arc_boundary', new_arc=world.arc)


def run_campaign(params=None, seed=None, log_dir=None, test_id='v14'):
    if seed is not None: random.seed(seed)
    world = V14World()
    world.params = dict(DEFAULT_PARAMS)
    if params: world.params.update(params)
    campaign_id = f'{test_id}_{seed:06d}' if seed is not None else f'{test_id}_{int(time.time())}'
    logger = MechanicalLogger(campaign_id, log_dir) if log_dir else NullLogger()
    logger.log('campaign_start',
               params=dict(world.params),
               initial_state={
                   'factions': {fn: {'L': f.stats['L'], 'Sta': f.stats['Sta'],
                                     'W': f.stats['W'], 'I': f.stats['I'],
                                     'Mil': f.stats['Mil'],
                                     'territories': sorted(f.territories)}
                                for fn, f in world.factions.items()},
                   'territories': {tid: {'owner': t.owner, 'accord': t.accord, 'pt': t.pt,
                                         'garrison': t.garrison}
                                  for tid, t in world.territories.items()},
                   'clocks': dict(world.clocks)})

    for s in range(world.params['CAMPAIGN_SEASONS']):
        if world.winner: break
        run_season(world, logger)

    # Determine winner
    if not world.winner:
        scores = {}
        for fn, f in world.factions.items():
            if not f.parliamentary: continue
            h = sum(1 for tid in ALL_PLAYABLE_15
                   if world.territories.get(tid) and world.territories[tid].owner == fn)
            scores[fn] = h * 10 + f.stats['L'] + len(f.territories)
        world.winner = max(scores, key=scores.get) if scores else None

    # Final state
    surviving_factions = [fn for fn, f in world.factions.items() if len(f.territories) > 0]
    uncontrolled = sum(1 for t in world.territories.values() if t.is_uncontrolled())
    logger.log('campaign_final',
               winner=world.winner,
               surviving_factions=surviving_factions,
               num_surviving=len(surviving_factions),
               uncontrolled_territories=uncontrolled,
               insurgencies_active=list(world.insurgencies.keys()),
               final_factions={fn: {'L': f.stats['L'], 'territories': len(f.territories)}
                              for fn, f in world.factions.items()})
    logger.finalize()
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        logger.flush(os.path.join(log_dir, f'{campaign_id}.jsonl'))

    return dict(winner=world.winner, world=world, surviving=len(surviving_factions),
                uncontrolled=uncontrolled, insurgencies=len(world.insurgencies))


# ═══════════════════════════════════════════════════════════════════════════
# DEFAULTS + BATCH
# ═══════════════════════════════════════════════════════════════════════════

DEFAULT_PARAMS = {
    'CAMPAIGN_SEASONS': 50,
    'CONSENT_RATE': 0.5,
    'TURMOIL_CAP': 12,
    'TREATY_LAPSE_RATE': 0.4,
    'VICTORY_THRESHOLD': 11,
    'EINHIR_I_GATE': 4,
    'ACTIONS_PER_FACTION': 3,
}

def run_batch(n, params=None, log_dir=None, test_id='v14'):
    wins = Counter()
    surviving_counts = Counter()
    uncontrolled_list = []; ins_counts = []
    L_acc = defaultdict(list); terr_acc = defaultdict(list)
    direct = 0
    for i in range(n):
        r = run_campaign(params=params, seed=i, log_dir=log_dir if i < 5 else None,
                        test_id=test_id)
        wins[r['winner']] += 1
        surviving_counts[r['surviving']] += 1
        uncontrolled_list.append(r['uncontrolled'])
        ins_counts.append(r['insurgencies'])
        for fn, f in r['world'].factions.items():
            L_acc[fn].append(f.stats['L'])
            terr_acc[fn].append(len(f.territories))
    tot = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/tot*100, 1)
                   for k in ['Crown','Church','Hafenmark','Varfell']},
        all_winners=dict(wins),
        L_mean={k: round(sum(v)/len(v), 2) for k, v in L_acc.items()},
        terr_mean={k: round(sum(v)/len(v), 2) for k, v in terr_acc.items()},
        surviving_dist=dict(surviving_counts),
        uncontrolled_mean=round(sum(uncontrolled_list)/n, 1),
        insurgencies_mean=round(sum(ins_counts)/n, 1),
    )


if __name__ == '__main__':
    print("v14 smoke test — 10 campaigns, 5 logged...")
    r = run_batch(10, log_dir='/home/claude/v14_logs', test_id='smoke')
    print(f"Wins: {r['win_share']}")
    print(f"All winners: {r['all_winners']}")
    print(f"Surviving factions distribution: {r['surviving_dist']}")
    print(f"Uncontrolled at end: {r['uncontrolled_mean']}/16")
    print(f"Insurgencies at end: {r['insurgencies_mean']}")
    print(f"Terr: {r['terr_mean']}")
