"""
mc_v15 — FRACTIONAL STATS + QUASIBINOMIAL DICE

Per Jordan direction (2026-05-14):
  - Stats are continuous floats 1.0–7.0
  - Dice pools are fractional ("2.5 dice")
  - Successes sampled from quasibinomial: mean=N*p, var=φ*N*p*(1-p)
  - Derived scores are player-facing display only (granularity, not buffer)
  - Single mechanical layer — no separate buffer/depletion logic

Display multipliers (rendering only):
  Mandate    = L × 20     (10–140 with L floor at 0.5)
  Stability  = Sta × 10   (5–70)
  Wealth     = W × 100    (50–700)
  Influence  = I × 15     (7.5–105)
  Military   = Mil × 10   (5–70)
  Accord     = a × 10     (10–70 per territory)
  Piety      = p × 10     (10–70 per territory)

Same underlying mechanic at every scale (faction stats, territory Accord, territory Piety):
  float value 1.0-7.0, modified by granular events, used in fractional dice pools.
"""
import sys, json, random, math, os, time
from collections import defaultdict, Counter

# ═══════════════════════════════════════════════════════════════════════════
# QUASIBINOMIAL DICE
# ═══════════════════════════════════════════════════════════════════════════

def quasibinomial_successes(pool, p_hit=0.5, dispersion=1.0):
    """Sample continuous success count from quasibinomial.
    Mean = pool * p_hit; Variance = dispersion * pool * p_hit * (1 - p_hit).
    Works for fractional pool. Returns float (may be non-integer).
    [canonical: Jordan 2026-05-14 quasibinomial]"""
    if pool <= 0: return 0.0
    mean = pool * p_hit
    var = dispersion * pool * p_hit * (1 - p_hit)
    sd = math.sqrt(max(var, 1e-6))
    sample = random.gauss(mean, sd)
    return max(0.0, min(pool, sample))

def resolve_degree(net):
    """Net float successes → Degree. Thresholds remain integer-valued.
    [canonical: peninsular_strain_v30 §3.2]"""
    if net >= 3.0: return 'Overwhelming'
    if net >= 1.0: return 'Success'
    if net >= 0.0: return 'Partial'
    return 'Failure'


# ═══════════════════════════════════════════════════════════════════════════
# DISPLAY HELPERS
# ═══════════════════════════════════════════════════════════════════════════

MULTS = {'L': 20, 'Sta': 10, 'W': 100, 'I': 15, 'Mil': 10, 'accord': 10, 'pt': 10}

def disp(key, val): return round(val * MULTS.get(key, 1), 1)


# ═══════════════════════════════════════════════════════════════════════════
# WORLD / FACTIONS / TERRITORIES
# ═══════════════════════════════════════════════════════════════════════════

ADJACENCY = {
    'T1':{'T2','T5','T14','T16'}, 'T2':{'T1','T3','T9','T14'},
    'T3':{'T2','T9','T17'}, 'T4':{'T7','T12','T14'},
    'T5':{'T1','T6','T14'}, 'T6':{'T5','T13','T15'},
    'T7':{'T4','T8'}, 'T8':{'T7','T9','T10','T17'},
    'T9':{'T2','T3','T8','T14','T17'}, 'T10':{'T8','T11'},
    'T11':{'T10','T12'}, 'T12':{'T4','T11','T13'},
    'T13':{'T6','T12','T15'}, 'T14':{'T1','T2','T4','T5','T9'},
    'T15':{'T6','T13'}, 'T17':{'T3','T8','T9'},
}
ALL_PLAYABLE_15 = {'T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T17'}

# Map old Accord (0-3) and PT (0-5) to new 1-7 floats
ACCORD_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 7.0}
PT_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 6.5, 5: 7.0}

STARTING_OWNER = {'T1':'Crown','T2':'Crown','T3':'Crown','T4':'Varfell','T5':'Crown',
                  'T6':'Crown','T7':'Hafenmark','T8':'Hafenmark','T9':'Church','T10':'Hafenmark',
                  'T11':'Varfell','T12':'Varfell','T13':'Varfell','T14':'Crown','T15':None,'T17':'Hafenmark'}
STARTING_ACCORD_OLD = {'T1':3,'T2':3,'T3':3,'T4':2,'T5':2,'T6':2,'T7':2,'T8':3,'T9':4,
                       'T10':2,'T11':2,'T12':2,'T13':1,'T14':3,'T15':0,'T17':2}
STARTING_PT_OLD = {'T1':3,'T2':3,'T3':3,'T4':2,'T5':3,'T6':1,'T7':3,'T8':3,'T9':5,
                   'T10':3,'T11':2,'T12':2,'T13':1,'T14':3,'T15':3,'T17':3}
STARTING_GARRISON = {'T1':True,'T8':True,'T9':True,'T12':True}

STARTING_STATS = {
    'Crown':    {'L': 5.0, 'Sta': 4.0, 'W': 4.0, 'I': 5.0, 'Mil': 4.0},
    'Church':   {'L': 5.0, 'Sta': 5.0, 'W': 5.0, 'I': 6.0, 'Mil': 4.0},
    'Hafenmark':{'L': 4.0, 'Sta': 4.0, 'W': 5.0, 'I': 4.0, 'Mil': 3.0},
    'Varfell':  {'L': 4.0, 'Sta': 4.0, 'W': 4.0, 'I': 4.0, 'Mil': 4.0},
}

class Faction:
    def __init__(self, name, parliamentary=True, stats=None):
        self.name = name
        self.parliamentary = parliamentary
        s = stats if stats else dict(STARTING_STATS.get(name, {'L':2.0,'Sta':3.0,'W':2.0,'I':2.0,'Mil':3.0}))
        self.L, self.Sta, self.W, self.I, self.Mil = s['L'], s['Sta'], s['W'], s['I'], s['Mil']
        self.territories = {tid for tid, o in STARTING_OWNER.items() if o == name}
        self.treaties = {}; self.casus_belli = set()
        self.tokens_held = defaultdict(int); self.inquisitors = set()
        self.revelation_tokens = 0; self.submitted = False
        self.sovereignty_history = 0; self.peaceful = True
        # Card slots (cleared per season)
        self.diplomat_used = False; self.cardinal_used = False
        self.senator_inward_used = False; self.tribune_used = False
        self.legacy_used = False; self.hall_used = False
        self.consul_used = False; self.seizure_used = False
        # Arc-scoped flags
        self.ea_arc_used = False; self.einhir_arc_used = False; self.parl_arc_used = False
        self.is_insurgency = not parliamentary; self.persistence_seasons = 0
        self.founded_season = 0

    def reset_seasonal(self):
        self.diplomat_used = self.cardinal_used = self.senator_inward_used = False
        self.tribune_used = self.legacy_used = self.hall_used = False
        self.consul_used = self.seizure_used = False

    def reset_arc(self):
        self.ea_arc_used = self.einhir_arc_used = self.parl_arc_used = False

    def adjust(self, stat, granular_delta, floor=0.5, ceiling=7.0):
        """Apply a granular (display-units) delta. e.g. adjust('L', -15) drops L by 0.75."""
        mult = MULTS[stat]
        current = getattr(self, stat)
        new = max(floor, min(ceiling, current + granular_delta / mult))
        setattr(self, stat, new)
        return new


class Territory:
    def __init__(self, tid):
        self.tid = tid
        self.owner = STARTING_OWNER[tid]
        self.accord = ACCORD_MAP[STARTING_ACCORD_OLD[tid]]
        self.pt = PT_MAP[STARTING_PT_OLD[tid]]
        self.garrison = STARTING_GARRISON.get(tid, False)
        self.prosperity = 2 if tid in {'T1','T2','T3','T8','T9','T14'} else 1
        self.templar = (tid == 'T9'); self.inquisitor = False
        self.uncontrolled_since = None; self.last_hostile_season = -10
        self.consec_passive_seasons = 0

    def is_uncontrolled(self):
        return self.owner is None or (isinstance(self.owner, str) and
            self.owner.startswith(('Insurgency_', 'Founded_', 'RM_')))

    def adjust_accord(self, granular_delta):
        mult = MULTS['accord']
        self.accord = max(0.5, min(7.0, self.accord + granular_delta / mult))

    def adjust_pt(self, granular_delta):
        mult = MULTS['pt']
        self.pt = max(0.5, min(7.0, self.pt + granular_delta / mult))


class World:
    def __init__(self):
        self.factions = {fn: Faction(fn) for fn in STARTING_STATS}
        self.territories = {tid: Territory(tid) for tid in STARTING_OWNER}
        self.clocks = {'CI': 0.0, 'MS': 80.0, 'PI': 0.0, 'Strain': 0.0, 'Turmoil': 0.0}
        self.season = 0; self.arc = 0; self.winner = None
        self.mass_seizure_fired = False
        self.insurgencies = {}
        self.params = {}


# ═══════════════════════════════════════════════════════════════════════════
# LOGGER
# ═══════════════════════════════════════════════════════════════════════════

class Logger:
    def __init__(self, cid):
        self.campaign_id = cid; self.events = []; self.counter = 0
        self.current_season = 0; self.current_arc = 0
    def log(self, etype, **kw):
        self.counter += 1
        ev = {'event_id': self.counter, 'season': self.current_season,
              'arc': self.current_arc, 'event_type': etype,
              'campaign_id': self.campaign_id, **kw}
        self.events.append(ev); return self.counter
    def flush(self, path):
        with open(path, 'w') as f:
            for ev in self.events: f.write(json.dumps(ev) + '\n')

class NullLogger:
    current_season = 0; current_arc = 0
    def log(self, *a, **kw): return 0
    def flush(self, *a): pass


# ═══════════════════════════════════════════════════════════════════════════
# THREAT RESPONSE — deterministic
# ═══════════════════════════════════════════════════════════════════════════

def mandatory_actions(faction, world, logger):
    threats = []
    for tid in faction.territories:
        t = world.territories.get(tid)
        if not t: continue
        if t.accord <= 3.0 and not t.garrison:
            threats.append(('Muster', tid, 100 - t.accord))
        elif t.accord <= 2.5 and t.garrison:
            threats.append(('Govern', tid, 90 - t.accord))
    threats.sort(key=lambda x: -x[2])
    mand = [(n, tid) for n, tid, _ in threats[:3]]
    if mand: logger.log('mandatory_response', faction=faction.name, actions=mand)
    return mand


# ═══════════════════════════════════════════════════════════════════════════
# ACTION GENERATION & SCORING
# ═══════════════════════════════════════════════════════════════════════════

def generate_candidates(faction, world):
    cands = []
    name = faction.name
    for tid in faction.territories:
        t = world.territories.get(tid)
        if t and t.accord < 7.0 and not faction.consul_used:
            cands.append(('Govern', tid))
        if t and not t.garrison: cands.append(('Muster', tid))
    cands.append(('Trade', None))
    for fn in world.factions:
        if fn != name: cands.append(('Spy', fn))
    for tid, t in world.territories.items():
        if t.owner != name and t.pt >= 4.0:
            cands.append(('Counter-Narrative', tid))

    if name == 'Crown':
        if not faction.diplomat_used:
            for fn in world.factions:
                if fn != 'Crown' and fn not in faction.treaties:
                    cands.append(('Crown Treaty', fn))
        if not faction.senator_inward_used and faction.W >= 3.0:
            cands.append(('Crown Initiative', None))

    if name == 'Church':
        if not faction.cardinal_used and not faction.ea_arc_used and faction.L < 7.0:
            cands.append(('Ecclesiastical Appointment', None))
        # Church Seizure removed — only Mass Seizure (auto-fire at CI ≥ 60) is canonical
        if not faction.cardinal_used:
            for tid, t in world.territories.items():
                if t.pt < 7.0: cands.append(('Piety Spread', tid))
        if not faction.consul_used: cands.append(('Assert', None))

    if name == 'Hafenmark':
        if not faction.diplomat_used:
            for tid, t in world.territories.items():
                if t.owner and t.owner != 'Hafenmark' and t.owner in world.factions:
                    cands.append(('Dynastic Proclamation', tid))
        if not faction.legacy_used and faction.W >= 1.0:
            cands.append(('Charter of Liberties', None))
        if not faction.consul_used and world.clocks.get('CI', 0) > 0:
            cands.append(('Suppress', None))

    if name == 'Varfell':
        if not faction.tribune_used:
            for tid in faction.territories:
                t = world.territories.get(tid)
                if t and t.accord < 5.5: cands.append(("Vaynard's Settlement", tid))
        if not faction.hall_used: cands.append(("Vaynard's Hall", None))
        if not faction.einhir_arc_used and faction.I >= 4.0:
            adj = set()
            for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
            adj -= faction.territories
            for tid in adj:
                t = world.territories.get(tid)
                if t and t.owner != 'Varfell' and t.pt <= 6.0:
                    cands.append(('Einhir Revival', tid))

    adj = set()
    for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
    adj -= faction.territories
    for tid in adj:
        if tid in world.territories: cands.append(('Military Conquest', tid))
    if not faction.parl_arc_used and faction.casus_belli:
        for cb_target in faction.casus_belli:
            if cb_target in world.factions:
                for tid in list(world.factions[cb_target].territories):
                    cands.append(('Parliamentary Transfer', tid))
    for tid in adj:
        t = world.territories.get(tid)
        if t and t.is_uncontrolled(): cands.append(('Reclaim Uncontrolled', tid))
    return cands


def score(name, faction, target, world):
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None
    if name == 'Govern':
        if t and t.accord <= 3.0: return 12
        if t and t.accord <= 5.0: return 6
        return 3
    if name == 'Muster':
        if t and t.accord <= 2.5: return 14
        if t and t.accord <= 4.0: return 7
        return 3
    if name == 'Crown Treaty': return 10
    if name == 'Crown Initiative': return 6 + max(0, 5 - faction.L)
    if name == 'Ecclesiastical Appointment': return 13 + max(0, 5 - faction.L) * 3
    if name == 'Church Seizure': return 12
    if name == 'Piety Spread': return 8 if t and t.pt < 5.0 else 4
    if name == 'Assert': return 5
    if name == 'Suppress': return 6
    if name == 'Dynastic Proclamation': return 11
    if name == 'Charter of Liberties': return 9 + max(0, 6 - faction.L)
    if name == "Vaynard's Settlement": return 11
    if name == "Vaynard's Hall": return 7
    if name == 'Einhir Revival':
        if t and t.pt <= 3.0: return 13
        if t and t.pt <= 4.0: return 8
        return 3
    if name == 'Military Conquest': return 11 if t and t.is_uncontrolled() else 6
    if name == 'Parliamentary Transfer': return 10
    if name == 'Reclaim Uncontrolled': return 9
    if name == 'Counter-Narrative':
        if t and t.owner == 'Church' and t.pt >= 6.0: return 7  # only Church capital
        return 2
    if name == 'Trade': return 4
    if name == 'Spy': return 3
    return 2


def select_actions(faction, world, logger):
    actions = mandatory_actions(faction, world, logger)
    used = set(actions)
    for n, _ in actions:
        if n == 'Govern': faction.consul_used = True
    remaining = 3 - len(actions)
    if remaining <= 0: return actions
    cands = [(n, t) for n, t in generate_candidates(faction, world) if (n, t) not in used]
    for _ in range(remaining):
        if not cands: break
        scored = [(score(n, faction, t, world), n, t) for n, t in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        _, n, t = random.choices(top, weights=weights, k=1)[0]
        actions.append((n, t)); used.add((n, t))
        cands = [(nn, tt) for nn, tt in cands if (nn, tt) not in used]
    return actions


# ═══════════════════════════════════════════════════════════════════════════
# PREREQS
# ═══════════════════════════════════════════════════════════════════════════

def prereqs(name, faction, target, world):
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None
    if name == 'Govern':
        if faction.consul_used: return False, 'consul_used'
        if not t or t.owner != faction.name: return False, 'not_own'
        return True, 'ok'
    if name == 'Muster':
        if not t or t.owner != faction.name: return False, 'not_own'
        if t.garrison: return False, 'already'
        return True, 'ok'
    if name == 'Crown Treaty':
        if faction.diplomat_used: return False, 'diplomat'
        if target not in world.factions or target in faction.treaties: return False, 'invalid_or_exists'
        return True, 'ok'
    if name == 'Crown Initiative':
        if faction.senator_inward_used or faction.W < 3.0: return False, 'senator_or_W'
        return True, 'ok'
    if name == 'Ecclesiastical Appointment':
        if faction.cardinal_used or faction.ea_arc_used or faction.L >= 7.0: return False, 'card_or_arc_or_cap'
        return True, 'ok'
    if name == 'Church Seizure':
        if faction.seizure_used or faction.L < 4.0: return False, 'card_or_mandate'
        if not t or t.owner not in world.factions: return False, 'target'
        if faction.L <= world.factions[t.owner].L: return False, 'prominence'
        if t.pt < 4.0: return False, 'pt<4'
        return True, 'ok'
    if name == 'Piety Spread':
        if faction.cardinal_used or not t or t.pt >= 7.0: return False, 'card_or_cap'
        return True, 'ok'
    if name == 'Assert' or name == 'Suppress':
        if faction.consul_used: return False, 'consul'
        return True, 'ok'
    if name == 'Dynastic Proclamation':
        if faction.diplomat_used: return False, 'diplomat'
        if not t or t.owner not in world.factions: return False, 'target'
        return True, 'ok'
    if name == 'Charter of Liberties':
        if faction.legacy_used or faction.W < 1.0: return False, 'legacy_or_W'
        return True, 'ok'
    if name == "Vaynard's Settlement":
        if faction.tribune_used: return False, 'tribune'
        if not t or t.owner != 'Varfell' or t.accord >= 5.5: return False, 'target'
        return True, 'ok'
    if name == "Vaynard's Hall":
        if faction.hall_used: return False, 'hall'
        return True, 'ok'
    if name == 'Einhir Revival':
        if faction.einhir_arc_used or faction.I < 4.0: return False, 'arc_or_I'
        if not t or t.owner == 'Varfell' or t.pt > 6.0: return False, 'target'
        adj = set()
        for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
        if target not in adj: return False, 'not_adj'
        return True, 'ok'
    if name == 'Military Conquest':
        if not t: return False, 'invalid'
        adj = set()
        for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
        if target not in adj: return False, 'not_adj'
        if t.owner == faction.name: return False, 'own'
        return True, 'ok'
    if name == 'Parliamentary Transfer':
        if faction.parl_arc_used or not t or t.owner not in faction.casus_belli: return False, 'arc_or_cb'
        return True, 'ok'
    if name == 'Reclaim Uncontrolled':
        if not t or not t.is_uncontrolled(): return False, 'not_unc'
        adj = set()
        for tid in faction.territories: adj |= ADJACENCY.get(tid, set())
        if target not in adj: return False, 'not_adj'
        return True, 'ok'
    return True, 'ok'


# ═══════════════════════════════════════════════════════════════════════════
# POOL & OB — fractional pools, integer Ob
# ═══════════════════════════════════════════════════════════════════════════

def pool_and_ob(name, faction, target, world):
    """Returns (pool: float, ob: int).
    Pool uses faction's float stats directly. Ob remains integer."""
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None

    if name == 'Govern': return faction.I, 2
    if name == 'Muster': return faction.Mil, 1
    if name == 'Crown Treaty': return faction.I + 1.0, 2  # +1 diplomat slot bonus
    if name == 'Crown Initiative':
        sum_accord = sum(world.territories[tid].accord for tid in faction.territories if tid in world.territories)
        return faction.I, max(1, int(sum_accord // 8))
    if name == 'Ecclesiastical Appointment': return faction.L + faction.I, 4
    if name == 'Church Seizure':
        ci = world.clocks.get('CI', 0)
        pool = faction.I + ci / 10.0  # fractional CI bonus
        ob = max(2, int(8 - t.pt)) if t else 4
        if t and t.templar: ob = max(2, ob - 1)
        return pool, ob
    if name == 'Piety Spread': return faction.I, 3
    if name == 'Assert': return faction.I, 2
    if name == 'Suppress':
        church = world.factions.get('Church')
        return faction.L, max(1, int(church.L / 2 + 1)) if church else 3
    if name == 'Dynastic Proclamation': return faction.I + 1.0, 2  # diplomat bonus
    if name == 'Charter of Liberties':
        tokens = sum(1 for v in faction.tokens_held.values() if v > 0)
        return faction.I + 2.0 + tokens, 2  # legacy slot bonus + tokens
    if name == "Vaynard's Settlement": return faction.Mil + faction.W / 2.0, 3
    if name == "Vaynard's Hall":
        bonus = 1.0 if faction.revelation_tokens >= 1 else 0.0
        return faction.Mil + bonus, 3
    if name == 'Einhir Revival':
        return faction.I + 1.0, max(1, int(t.pt / 2 + 1)) if t else 2
    if name == 'Military Conquest':
        ob = 2 if t and t.owner is None else 4
        if t and t.garrison: ob += 1
        return faction.Mil, ob
    if name == 'Parliamentary Transfer':
        holder = world.factions.get(t.owner) if t and t.owner in world.factions else None
        return faction.I, int(holder.L + 2) if holder else 4
    if name == 'Reclaim Uncontrolled': return faction.Mil, 2
    if name == 'Trade': return faction.W, 2
    if name == 'Spy': return faction.I, 3
    if name == 'Counter-Narrative': return faction.I, 3
    return faction.I, 3


# ═══════════════════════════════════════════════════════════════════════════
# APPLY OUTCOMES
# ═══════════════════════════════════════════════════════════════════════════

def apply(name, faction, target, degree, world, logger, parent_id):
    """All stat changes use granular display units (Mandate ±15, Stability ±10).
    Internally divides by multiplier for the float stat delta."""
    t = world.territories.get(target) if isinstance(target, str) and target in world.territories else None
    success = degree in ('Success', 'Overwhelming')
    ow = degree == 'Overwhelming'

    def log_change(target_type, tid, attr, before, after, reason):
        if isinstance(before, (int, float)) and isinstance(after, (int, float)):
            if abs(before - after) > 0.001:
                logger.log('state_change', parent_event_id=parent_id,
                           target_type=target_type, target_id=tid, attribute=attr,
                           before=round(before, 3), after=round(after, 3),
                           delta=round(after - before, 3), reason=reason)
        else:
            if before != after:
                logger.log('state_change', parent_event_id=parent_id,
                           target_type=target_type, target_id=tid, attribute=attr,
                           before=before, after=after, reason=reason)

    if name == 'Govern' and t:
        faction.consul_used = True
        if ow:
            b = t.accord; t.adjust_accord(20)
            log_change('territory', target, 'accord', b, t.accord, 'Govern OW')
            faction.adjust('Sta', 5); faction.adjust('L', 4)
        elif success:
            b = t.accord; t.adjust_accord(10)
            log_change('territory', target, 'accord', b, t.accord, 'Govern Success')
            faction.adjust('Sta', 3); faction.adjust('L', 2)
        elif degree == 'Partial':
            b = t.accord; t.adjust_accord(3)
            log_change('territory', target, 'accord', b, t.accord, 'Govern Partial')
        faction.peaceful = True

    elif name == 'Muster' and t:
        if success:
            t.garrison = True
            b = t.accord; t.adjust_accord(5)
            log_change('territory', target, 'garrison', False, True, 'Muster')

    elif name == 'Crown Treaty':
        faction.diplomat_used = True
        if success and target in world.factions:
            partner = world.factions[target]
            if random.random() < world.params.get('CONSENT_RATE', 0.5):
                faction.treaties[target] = 'CrownTreaty'
                partner.treaties[faction.name] = 'CrownTreaty'
                faction.adjust('L', 10)
                logger.log('treaty_formed', faction=faction.name, partner=target, parent_event_id=parent_id)

    elif name == 'Crown Initiative':
        faction.senator_inward_used = True
        faction.adjust('W', -200)  # cost
        if ow:
            b = faction.L; faction.adjust('L', 25)
            log_change('faction', faction.name, 'L', b, faction.L, 'CI OW')
            for tid in faction.territories:
                t2 = world.territories.get(tid)
                if t2: t2.adjust_accord(8)
        elif success:
            faction.adjust('L', 15)
            if faction.territories:
                worst = min(faction.territories, key=lambda tid: world.territories[tid].accord if tid in world.territories else 99)
                if worst in world.territories: world.territories[worst].adjust_accord(8)
        elif degree == 'Partial':
            faction.adjust('Sta', 5)

    elif name == 'Ecclesiastical Appointment':
        faction.cardinal_used = True; faction.ea_arc_used = True
        if success:
            b = faction.L
            # EA is a major institutional event — granular gain of +20 (= +1.0 L)
            faction.adjust('L', 20)
            log_change('faction', faction.name, 'L', b, faction.L, f'EA {degree}')

    elif name == 'Church Seizure' and t:
        faction.seizure_used = True
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].adjust('L', -15)  # lost territory
            t.owner = 'Church'; faction.territories.add(target)
            # Accord set per PT (1-7 scale): max(2, pt//2 + 1)
            new_accord = max(2.5, min(7.0, t.pt / 2 + 1))
            if ow: new_accord = min(7.0, new_accord + 1)
            t.accord = new_accord
            log_change('territory', target, 'owner', old, 'Church', 'Church Seizure')
            if ow: t.adjust_pt(10)

    elif name == 'Piety Spread' and t:
        faction.cardinal_used = True
        if success:
            t.adjust_pt(8 if ow else 5)

    elif name == 'Assert':
        faction.consul_used = True
        if success:
            world.clocks['CI'] = min(100, world.clocks.get('CI', 0) + 1.0)
        else:
            faction.adjust('Sta', -10)

    elif name == 'Suppress':
        faction.consul_used = True
        if success:
            world.clocks['_suppress'] = 1
        else:
            faction.adjust('Sta', -10)

    elif name == 'Dynastic Proclamation' and t:
        faction.diplomat_used = True
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].adjust('L', -10)
            t.owner = faction.name; faction.territories.add(target); t.garrison = True
            t.accord = 5.0 if ow else 4.0
            log_change('territory', target, 'owner', old, faction.name, f'DP {degree}')

    elif name == 'Charter of Liberties':
        faction.legacy_used = True; faction.adjust('W', -50)
        if ow:
            b = faction.L; faction.adjust('L', 25)
            log_change('faction', faction.name, 'L', b, faction.L, 'Charter OW')
            world.clocks['PI'] = max(0, world.clocks.get('PI', 0) - 2)
        elif success:
            faction.adjust('L', 15)
            world.clocks['PI'] = max(0, world.clocks.get('PI', 0) - 1)
        elif degree == 'Partial':
            faction.adjust('L', 10)

    elif name == "Vaynard's Settlement" and t:
        faction.tribune_used = True; faction.adjust('W', -50)
        if ow:
            t.adjust_accord(15); faction.adjust('Mil', 5)
        elif success:
            t.adjust_accord(10)

    elif name == "Vaynard's Hall":
        faction.hall_used = True; faction.adjust('Mil', -5); faction.adjust('W', -50)
        if ow: faction.adjust('L', 25)
        elif success: faction.adjust('L', 15)
        elif degree == 'Partial': faction.adjust('Mil', 5)

    elif name == 'Einhir Revival' and t:
        faction.einhir_arc_used = True
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].adjust('L', -10)
            t.owner = 'Varfell'; faction.territories.add(target); t.garrison = True
            t.accord = 5.0 if ow else 3.0
            t.adjust_pt(-5)
            log_change('territory', target, 'owner', old, 'Varfell', 'Einhir')
        elif degree == 'Partial':
            t.adjust_pt(-3)

    elif name == 'Military Conquest' and t:
        faction.peaceful = False
        if success:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].adjust('L', -10)
                world.factions[old].peaceful = False
            elif old in world.insurgencies:
                world.insurgencies[old].territories.discard(target)
            t.owner = faction.name; faction.territories.add(target); t.garrison = True
            t.accord = 3.0 if ow else 2.0
            faction.adjust('L', -5)  # war is costly
            log_change('territory', target, 'owner', old, faction.name, 'Conquest')

    elif name == 'Parliamentary Transfer' and t:
        faction.parl_arc_used = True
        if success:
            old = t.owner; faction.casus_belli.discard(old)
            if old in world.factions:
                world.factions[old].territories.discard(target)
                if ow: world.factions[old].adjust('L', -15)
            t.owner = faction.name; faction.territories.add(target); t.accord = 4.0
            log_change('territory', target, 'owner', old, faction.name, 'ParlXfer')
        elif degree == 'Partial':
            faction.casus_belli.add(t.owner)
        else:
            faction.adjust('Sta', -10)

    elif name == 'Reclaim Uncontrolled' and t and t.is_uncontrolled():
        if success:
            old = t.owner
            if old in world.insurgencies:
                world.insurgencies[old].territories.discard(target)
            t.owner = faction.name; faction.territories.add(target); t.garrison = True
            t.accord = 3.0 if ow else 2.0

    elif name == 'Trade':
        if success: faction.adjust('W', 60 if ow else 40)

    elif name == 'Spy':
        if success: faction.adjust('I', 10 if ow else 5)

    elif name == 'Counter-Narrative' and t:
        if success: t.adjust_pt(-5 if not ow else -10)


# ═══════════════════════════════════════════════════════════════════════════
# CI GENERATION
# ═══════════════════════════════════════════════════════════════════════════

def ci_generation(world, logger):
    church = world.factions.get('Church')
    if not church or church.name not in world.factions: return
    momentum = 1.0
    if world.clocks.get('_suppress', 0) >= 1:
        momentum = 0.0; world.clocks['_suppress'] = 0
    piety_yield = 0.0
    for tid, t in world.territories.items():
        prom = (t.owner == 'Church') or (t.owner in world.factions and church.L > world.factions[t.owner].L)
        if prom:
            if t.pt >= 6.0: piety_yield += 1.0
            elif t.pt >= 5.0: piety_yield += 0.5
    templar_count = sum(1 for t in world.territories.values() if t.templar)
    haf = world.factions.get('Hafenmark')
    haf_suppress = -1.0 if (haf and haf.L >= 4.0) else 0.0  # [canonical: victory_v30 §3.2 flat -1]
    total = momentum + piety_yield + templar_count + haf_suppress
    world.clocks['CI'] = max(0.0, min(100.0, world.clocks.get('CI', 0) + total))
    logger.log('ci_gen', momentum=momentum, piety=piety_yield,
               templars=templar_count, haf=haf_suppress,
               total=round(total, 2), new_ci=round(world.clocks['CI'], 2))


def mass_seizure_check(world, logger):
    if world.mass_seizure_fired: return
    ci = world.clocks.get('CI', 0)
    if ci < 60: return
    church = world.factions.get('Church')
    if not church or church.L < 4.0: return
    p = min(1.0, ((ci - 60) / 40) ** 3.3)
    roll = random.random()
    logger.log('mass_seizure_check', ci=round(ci, 2), p=round(p, 3), roll=round(roll, 3), fired=(roll < p))
    if roll >= p: return
    world.mass_seizure_fired = True
    seized = []
    pool = church.I + ci / 10.0
    for tid, t in list(world.territories.items()):
        if t.owner == 'Church' or t.pt <= 0: continue
        if t.owner in world.factions and church.L <= world.factions[t.owner].L: continue
        ob = max(2, int(8 - t.pt))
        if t.templar: ob = max(2, ob - 1)
        successes = quasibinomial_successes(pool)
        if successes - ob >= 1.0:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(tid)
            t.owner = 'Church'; church.territories.add(tid)
            t.accord = max(3.0, min(7.0, t.pt / 2 + 1))
            seized.append((tid, old))
    logger.log('mass_seizure_event', seized=seized, total=len(seized))


# ═══════════════════════════════════════════════════════════════════════════
# REVOLT → INSURGENCY → FOUNDED ORG
# ═══════════════════════════════════════════════════════════════════════════

def check_insurgencies(world, logger):
    plain_uc = {tid for tid, t in world.territories.items() if t.owner is None}
    if len(plain_uc) < 2:
        # Still check existing insurgencies for promotion
        pass
    visited = set(); groups = []
    for tid in plain_uc:
        if tid in visited: continue
        group = set(); queue = [tid]
        while queue:
            curr = queue.pop()
            if curr in visited or curr not in plain_uc: continue
            visited.add(curr); group.add(curr)
            for adj in ADJACENCY.get(curr, set()):
                if adj in plain_uc and adj not in visited: queue.append(adj)
        if len(group) >= 2: groups.append(group)

    for group in groups:
        persistent = all(world.territories[tid].uncontrolled_since is not None and
                        world.season - world.territories[tid].uncontrolled_since >= 2
                        for tid in group)
        if not persistent: continue
        avg_pt = sum(world.territories[tid].pt for tid in group) / len(group)
        is_rm = avg_pt < 3.0  # Piety < 3 flip threshold
        prefix = 'RM' if is_rm else 'Insurgency'
        name = f'{prefix}_{world.season}_{min(group)}'
        ins = Faction(name, parliamentary=False, stats={'L':1.0,'Sta':2.0,'W':1.0,'I':2.0,'Mil':2.5})
        ins.territories = set(group); ins.is_insurgency = True; ins.founded_season = world.season
        for tid in group:
            world.territories[tid].owner = name; world.territories[tid].accord = 3.0
        world.insurgencies[name] = ins
        logger.log('insurgency_formed', name=name, territories=sorted(group), avg_pt=round(avg_pt, 2))

    # Promotion: Mandate ≥ 3 + 2+ territories + Accord ≥ 4 sustained 2 seasons
    for ins_name, ins in list(world.insurgencies.items()):
        if len(ins.territories) < 2: continue
        if ins.L < 3.0: continue
        accord_ok = all(world.territories[tid].accord >= 4.0 for tid in ins.territories if tid in world.territories)
        if not accord_ok: continue
        ins.persistence_seasons += 1
        if ins.persistence_seasons >= 2:
            ins.parliamentary = True; ins.is_insurgency = False
            del world.insurgencies[ins_name]
            world.factions[ins_name] = ins
            logger.log('promoted', name=ins_name, mandate=round(ins.L, 2))


# ═══════════════════════════════════════════════════════════════════════════
# ACCOUNTING
# ═══════════════════════════════════════════════════════════════════════════

def accounting(world, logger):
    season = world.season
    # Revolts (Accord < 2.0 = revolt threshold)
    revolts = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        if t.accord < 2.0:
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(tid)
                world.factions[old].adjust('Sta', -15)
                world.factions[old].peaceful = False
            elif old in world.insurgencies:
                world.insurgencies[old].territories.discard(tid)
            t.owner = None; t.garrison = False
            t.uncontrolled_since = season
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolts += 1
            logger.log('revolt', territory=tid, lost_by=old)

    # Garrison passive recovery / neglect drain
    for tid, t in world.territories.items():
        if t.is_uncontrolled():
            if t.uncontrolled_since is None: t.uncontrolled_since = season
            continue
        t.uncontrolled_since = None
        if t.garrison and season - t.last_hostile_season >= 2:
            t.consec_passive_seasons += 1
            if t.consec_passive_seasons >= 2:
                t.adjust_accord(5); t.consec_passive_seasons = 0
        else:
            t.consec_passive_seasons = 0
        if not t.garrison:
            t.adjust_accord(-2)

    if revolts == 0:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - 1)
    world.clocks['Strain'] = world.clocks['Turmoil']

    # Treaty Strain decay
    pairs = set()
    for fn, f in world.factions.items():
        for partner, tt in f.treaties.items():
            if tt == 'CrownTreaty':
                pairs.add(tuple(sorted([fn, partner])))
    if pairs:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - min(len(pairs), 2))

    # Strain thresholds
    strain = world.clocks['Strain']
    if 3 <= strain <= 4:
        for f in world.factions.values(): f.adjust('L', -10)
    elif strain >= 7:
        for f in world.factions.values():
            for tid in list(f.territories):
                t = world.territories.get(tid)
                if t: t.adjust_accord(-5)

    # Faction income
    for fn, f in world.factions.items():
        high = sum(1 for tid in f.territories if tid in world.territories and world.territories[tid].accord >= 4.0)
        if high: f.adjust('L', high * 1.5)
        if f.peaceful: f.adjust('Sta', 3)
        prosp = sum(world.territories[tid].prosperity * 10 for tid in f.territories if tid in world.territories)
        f.adjust('W', prosp)
        f.adjust('I', 2)
        f.peaceful = True

    # Church tithe
    church = world.factions.get('Church')
    if church:
        total_pt = sum(t.pt for t in world.territories.values())
        church.adjust('L', total_pt * 0.5)
        church.adjust('W', total_pt * 2)

    ci_generation(world, logger)
    mass_seizure_check(world, logger)
    check_insurgencies(world, logger)


# ═══════════════════════════════════════════════════════════════════════════
# VICTORY — Universal Peninsular Sovereignty (the only path)
# [canonical: peninsular_strain_v30 §6.1]
# ═══════════════════════════════════════════════════════════════════════════

def victory_check(world, logger, threshold=11):
    turmoil = world.clocks.get('Turmoil', 0)
    if turmoil > world.params.get('TURMOIL_CAP', 12): return None
    for fn, f in world.factions.items():
        if not f.parliamentary: continue
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
                elif rival.submitted or (rival.L <= 1.5 and f.L >= 5.0):
                    controlled.add(tid)
        if len(controlled) < threshold:
            f.sovereignty_history = 0; continue
        own = [tid for tid in controlled if world.territories.get(tid) and world.territories[tid].owner == fn]
        if not all(world.territories[tid].accord >= 4.0 for tid in own):
            f.sovereignty_history = 0; continue
        f.sovereignty_history += 1
        if f.sovereignty_history >= 2:
            logger.log('victory', faction=fn, season=world.season, controlled=len(controlled))
            return fn
    return None


# ═══════════════════════════════════════════════════════════════════════════
# SEASON + CAMPAIGN
# ═══════════════════════════════════════════════════════════════════════════

def run_season(world, logger):
    logger.current_season = world.season
    logger.current_arc = world.arc
    logger.log('season_start', season=world.season,
               faction_L={fn: round(f.L, 2) for fn, f in world.factions.items()},
               faction_terr={fn: len(f.territories) for fn, f in world.factions.items()},
               clocks={k: round(v, 2) for k, v in world.clocks.items() if not k.startswith('_')})

    for f in world.factions.values(): f.reset_seasonal()
    for f in world.insurgencies.values(): f.reset_seasonal()

    all_factions = list(world.factions.values()) + list(world.insurgencies.values())
    for f in all_factions:
        actions = select_actions(f, world, logger)
        for action_name, target in actions:
            ok, reason = prereqs(action_name, f, target, world)
            attempt_id = logger.log('action_attempt', actor=f.name, action=action_name,
                                     target=target, ok=ok, reason=reason)
            if not ok: continue
            pool, ob = pool_and_ob(action_name, f, target, world)
            successes = quasibinomial_successes(pool)
            net = successes - ob
            degree = resolve_degree(net)
            resolve_id = logger.log('action_resolved', parent_event_id=attempt_id,
                                     actor=f.name, action=action_name, target=target,
                                     pool=round(pool, 3), ob=ob,
                                     successes=round(successes, 3), net=round(net, 3),
                                     degree=degree)
            apply(action_name, f, target, degree, world, logger, resolve_id)

    accounting(world, logger)
    winner = victory_check(world, logger, threshold=world.params.get('VICTORY_THRESHOLD', 11))
    if winner: world.winner = winner

    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values(): f.reset_arc()
        for f in world.insurgencies.values(): f.reset_arc()
        world.arc += 1
        # Treaty Expiration at arc boundary
        for fn, f in world.factions.items():
            for partner, tt in list(f.treaties.items()):
                if tt == 'CrownTreaty' and random.random() < world.params.get('TREATY_LAPSE_RATE', 0.5):
                    del f.treaties[partner]
                    if partner in world.factions and fn in world.factions[partner].treaties:
                        del world.factions[partner].treaties[fn]


def run_campaign(params=None, seed=None, log_dir=None, test_id='v15'):
    if seed is not None: random.seed(seed)
    world = World()
    world.params = dict(DEFAULT_PARAMS)
    if params: world.params.update(params)
    cid = f'{test_id}_{seed:06d}' if seed is not None else f'{test_id}_{int(time.time())}'
    logger = Logger(cid) if log_dir else NullLogger()
    logger.log('campaign_start', params=world.params)
    for _ in range(world.params['CAMPAIGN_SEASONS']):
        if world.winner: break
        run_season(world, logger)
    if not world.winner:
        scores = {}
        for fn, f in world.factions.items():
            if not f.parliamentary: continue
            h = sum(1 for tid in ALL_PLAYABLE_15 if world.territories.get(tid) and world.territories[tid].owner == fn)
            scores[fn] = h * 10 + f.L + len(f.territories)
        world.winner = max(scores, key=scores.get) if scores else None
    surviving = sum(1 for f in world.factions.values() if len(f.territories) > 0)
    uncontrolled = sum(1 for t in world.territories.values() if t.is_uncontrolled())
    logger.log('campaign_end', winner=world.winner, surviving=surviving,
               uncontrolled=uncontrolled, insurgencies=len(world.insurgencies),
               final={fn: {'L': round(f.L, 2), 'terr': len(f.territories)}
                     for fn, f in world.factions.items()})
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        logger.flush(os.path.join(log_dir, f'{cid}.jsonl'))
    return dict(winner=world.winner, world=world, surviving=surviving,
                uncontrolled=uncontrolled, insurgencies=len(world.insurgencies))


DEFAULT_PARAMS = {
    'CAMPAIGN_SEASONS': 50, 'CONSENT_RATE': 0.5, 'TURMOIL_CAP': 12,
    'TREATY_LAPSE_RATE': 0.5, 'VICTORY_THRESHOLD': 11,
}


def run_batch(n, params=None, log_dir=None, test_id='v15'):
    wins = Counter(); surv_dist = Counter(); uc_list = []; ins_list = []
    L_acc = defaultdict(list); terr_acc = defaultdict(list)
    for i in range(n):
        r = run_campaign(params=params, seed=i, log_dir=log_dir if i < 3 else None, test_id=test_id)
        wins[r['winner']] += 1; surv_dist[r['surviving']] += 1
        uc_list.append(r['uncontrolled']); ins_list.append(r['insurgencies'])
        for fn, f in r['world'].factions.items():
            L_acc[fn].append(f.L); terr_acc[fn].append(len(f.territories))
    tot = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/tot*100, 1) for k in ['Crown','Church','Hafenmark','Varfell']},
        L_mean={k: round(sum(v)/len(v), 2) for k, v in L_acc.items()},
        terr_mean={k: round(sum(v)/len(v), 2) for k, v in terr_acc.items()},
        surv_dist=dict(surv_dist),
        uc_mean=round(sum(uc_list)/n, 1),
        ins_mean=round(sum(ins_list)/n, 1),
        all_winners=dict(wins),
    )


if __name__ == '__main__':
    print("v15 smoke test — 20 campaigns")
    r = run_batch(20, log_dir='/home/claude/v15_logs')
    print(f"Wins: {r['win_share']}")
    print(f"All winners: {r['all_winners']}")
    print(f"Surviving: {r['surv_dist']}  Uncontrolled: {r['uc_mean']}  Insurgencies: {r['ins_mean']}")
    print(f"L: {r['L_mean']}")
    print(f"Terr: {r['terr_mean']}")
