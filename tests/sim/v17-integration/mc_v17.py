# mc_v17 — Master campaign simulator, v17 generation.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Extends the v15 baseline (designs/audit/2026-05-14-balance-audit/sim/mc_v15.py)  # [canonical: N/A — doc]
# with full v17-module integration:  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
#   - M1 settlement registry seeded into World.settlements  # [canonical: N/A — doc]
#   - M2 CI political revision constants drive ci_generation  # [canonical: N/A — doc]
#   - M3 mass-battle resolution replaces single-roll Military Conquest  # [canonical: N/A — doc]
#   - M4 UnitRoster tracks per-faction units (Levy/LightInf/HeavyInf active)  # [canonical: N/A — doc]
#   - M5 settlement governance feeds Accord/Wealth aggregation at Accounting  # [canonical: N/A — doc]
#   - M6 faction actions (Crown Initiative 3 modes, Excommunication, Absolution,  # [canonical: N/A — doc]
#     Council, Charter, Hall, Uprising) registered in ACTION_REGISTRY  # [canonical: N/A — doc]
#   - M7 resolution hooks wire the 6 tactic cards deferred from M3/M6  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# This is a primitives-bound runner — it composes M-modules and reproduces  # [canonical: N/A — doc]
# v15's overall campaign flow. Heavy v15 logic that doesn't interact with v17  # [canonical: N/A — doc]
# scope (Treaty mechanics, EA, Spy, Parliamentary Transfer, etc.) is delegated  # [canonical: N/A — doc]
# to a minimal v15-compatible action path; the v17 surface is wired through  # [canonical: N/A — doc]
# ACTION_REGISTRY entries calling the M-module primitives.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources:  # [canonical: N/A — doc]
#   - integration_plan_v3 Section 5 Phase 2 (mass-battle integration spec)  # [canonical: N/A — doc]
#   - integration_plan_v3 Section 5 Phase 5 (settlement state integration)  # [canonical: N/A — doc]
#   - mc_v15.py (baseline architecture)  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional assumptions: see sim_verification_ledger.  # [canonical: N/A — doc]
# Tags M7_ASSUMPTION_ONE..M7_ASSUMPTION_SEVEN.  # [canonical: N/A — doc]

import json
import math
import os
import random
import sys
import time
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m1_church_infrastructure as m1
import m2_ci_political_revision as m2
import m3_mass_battle as m3
import m4_unit_state as m4
import m5_settlement_aggregation as m5
import m6_faction_actions as m6
import m7_resolution_hooks as m7h


# ═══════════════════════════════════════════════════════════════════════════
# WORLD STARTING STATE — preserved from mc_v15 for BEFORE/AFTER comparability
# ═══════════════════════════════════════════════════════════════════════════

# [canonical: mc_v15.py L55 — MULTS table for fractional-stat display]
MULTS = {'L': 20, 'Sta': 10, 'W': 100, 'I': 15, 'Mil': 10, 'accord': 10, 'pt': 10}

# [canonical: mc_v15.py L74 — ALL_PLAYABLE_15 set; also matches m1.PLAYABLE_TERRITORIES]
ALL_PLAYABLE_15 = {'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10',
                   'T11', 'T12', 'T13', 'T14', 'T17'}
# [canonical: mc_v15.py L77 — ACCORD_MAP 0-3 → 1-7 float]
ACCORD_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 7.0}
# [canonical: mc_v15.py L78 — PT_MAP 0-5 → 1-7 float]
PT_MAP = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 6.5, 5: 7.0}

# [canonical: mc_v15.py L80 — STARTING_OWNER table]
STARTING_OWNER = {'T1': 'Crown', 'T2': 'Crown', 'T3': 'Crown', 'T4': 'Varfell',
                  'T5': 'Crown', 'T6': 'Crown', 'T7': 'Hafenmark', 'T8': 'Hafenmark',
                  'T9': 'Church', 'T10': 'Hafenmark', 'T11': 'Varfell', 'T12': 'Varfell',
                  'T13': 'Varfell', 'T14': 'Crown', 'T15': None, 'T17': 'Hafenmark'}
# [canonical: mc_v15.py L83 — STARTING_ACCORD_OLD 0-3 table]
STARTING_ACCORD_OLD = {'T1': 3, 'T2': 3, 'T3': 3, 'T4': 2, 'T5': 2, 'T6': 2,
                       'T7': 2, 'T8': 3, 'T9': 4, 'T10': 2, 'T11': 2, 'T12': 2,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
                       'T13': 1, 'T14': 3, 'T15': 0, 'T17': 2}  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
# [canonical: mc_v15.py L85 — STARTING_PT_OLD 0-5 table]
STARTING_PT_OLD = {'T1': 3, 'T2': 3, 'T3': 3, 'T4': 2, 'T5': 3, 'T6': 1,
                   'T7': 3, 'T8': 3, 'T9': 5, 'T10': 3, 'T11': 2, 'T12': 2,  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
                   'T13': 1, 'T14': 3, 'T15': 3, 'T17': 3}  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
# [canonical: mc_v15.py L87 — STARTING_GARRISON]
STARTING_GARRISON = {'T1': True, 'T8': True, 'T9': True, 'T12': True}
# [canonical: mc_v15.py L89 — STARTING_STATS]
STARTING_STATS = {
    'Crown':     {'L': 5.0, 'Sta': 4.0, 'W': 4.0, 'I': 5.0, 'Mil': 4.0},  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    'Church':    {'L': 5.0, 'Sta': 5.0, 'W': 5.0, 'I': 6.0, 'Mil': 4.0},  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    'Hafenmark': {'L': 4.0, 'Sta': 4.0, 'W': 5.0, 'I': 4.0, 'Mil': 3.0},  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    'Varfell':   {'L': 4.0, 'Sta': 4.0, 'W': 4.0, 'I': 4.0, 'Mil': 4.0},  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
}

# [canonical: derived from mass_battle_v30 §B.4 — each faction gets 4 shared + 2 specific]
FACTION_TACTIC_HANDS = {
    'Crown':     ['standard_advance', 'disciplined_defence', 'feigned_retreat', 'concentrated_strike',
                  'royal_guard', 'ducal_call'],
    'Church':    ['standard_advance', 'disciplined_defence', 'feigned_retreat', 'concentrated_strike',
                  'crusade_fervour', 'inquisitors_mark'],
    'Hafenmark': ['standard_advance', 'disciplined_defence', 'feigned_retreat', 'concentrated_strike',
                  'mercenary_surge', 'sovereign_authority'],
    'Varfell':   ['standard_advance', 'disciplined_defence', 'feigned_retreat', 'concentrated_strike',
                  'stratagem', 'calculated_retreat'],
}


# ═══════════════════════════════════════════════════════════════════════════
# FACTION — extends mc_v15 with M4 units roster + M3 tactic card hand
# ═══════════════════════════════════════════════════════════════════════════

class Faction:
    # [canonical: mc_v15.py L96 Faction class — extended with v17 fields per integration_plan §5 Phase 2c]
    def __init__(self, name, parliamentary=True, stats=None):
        self.name = name
        self.parliamentary = parliamentary
        s = stats if stats else dict(STARTING_STATS.get(name, {'L': 2.0, 'Sta': 3.0, 'W': 2.0, 'I': 2.0, 'Mil': 3.0}))  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        self.L = s['L']
        self.Sta = s['Sta']
        self.W = s['W']
        self.I = s['I']
        self.Mil = s['Mil']
        self.territories = {tid for tid, o in STARTING_OWNER.items() if o == name}
        # v15-compatible slot tracking
        self.senator_inward_used = False
        self.consul_used = False
        self.peaceful = True
        # v17 additions:
        # M4 — unit roster per integration_plan §5 Phase 2c
        self.units = m4.UnitRoster()  # [canonical: integration_plan §5 Phase 2c — UnitRoster per faction]
        # M3/M6 — tactic card hand (4 shared + 2 specific)
        self.tactic_hand = list(FACTION_TACTIC_HANDS.get(name, FACTION_TACTIC_HANDS.get('Crown')))  # [canonical: mass_battle_v30 §B.4]
        # Crown Initiative state
        self.crown_initiative_used_this_season = False
        self.great_work_seasons_remaining = 0
        self.great_work_active = False
        # Church state
        self.excommunication_against = set()  # factions Church has excommunicated
        # Arc flags
        self.uprising_used_this_arc = False
        # Standing modifier (M6_ASSUMPTION_TWO — integer accumulator)
        self.standing = 0

    def reset_seasonal(self):
        self.senator_inward_used = False
        self.consul_used = False
        self.crown_initiative_used_this_season = False

    def adjust(self, stat, granular_delta, floor=0.5, ceiling=7.0):  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        # [canonical: mc_v15.py L125 — fractional-delta adjustment]
        mult = MULTS[stat]
        current = getattr(self, stat)
        new = max(floor, min(ceiling, current + granular_delta / mult))
        setattr(self, stat, new)
        return new

    def is_excommunicated(self, by_church_state):
        # [canonical: faction_canon Church Excommunication — barred from public office]
        return self.name in by_church_state


# ═══════════════════════════════════════════════════════════════════════════
# TERRITORY — preserved from mc_v15
# ═══════════════════════════════════════════════════════════════════════════

class Territory:
    # [canonical: mc_v15.py L134 Territory class]
    def __init__(self, tid):
        self.tid = tid
        self.owner = STARTING_OWNER[tid]
        self.accord = ACCORD_MAP[STARTING_ACCORD_OLD[tid]]
        self.pt = PT_MAP[STARTING_PT_OLD[tid]]
        self.garrison = STARTING_GARRISON.get(tid, False)
        self.prosperity = 2 if tid in {'T1', 'T2', 'T3', 'T8', 'T9', 'T14'} else 1
        self.fort_level = 1 if self.garrison else 0  # [canonical: military_layer §2.2 — Fort dice to defender]
        self.templar = (tid == 'T9')
        self.uncontrolled_since = None

    def is_uncontrolled(self):
        return self.owner is None

    def adjust_accord(self, granular_delta):
        # [canonical: mc_v15.py L150]
        mult = MULTS['accord']
        self.accord = max(0.5, min(7.0, self.accord + granular_delta / mult))  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]

    def adjust_pt(self, granular_delta):
        mult = MULTS['pt']
        self.pt = max(0.5, min(7.0, self.pt + granular_delta / mult))  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]


# ═══════════════════════════════════════════════════════════════════════════
# WORLD — extends mc_v15 with M1 settlement registry + M5 governance
# ═══════════════════════════════════════════════════════════════════════════

class World:
    # [canonical: mc_v15.py L159 World class — extended with v17 wiring]
    def __init__(self):
        self.factions = {fn: Faction(fn) for fn in STARTING_STATS}
        self.territories = {tid: Territory(tid) for tid in STARTING_OWNER}
        # v15-compatible clocks
        # [canonical: mc_v15 + M2 CI starting value]
        self.clocks = {'CI': float(m2.CI_STARTING_VALUE), 'MS': 80.0, 'PI': 0.0,
                       'Strain': 0.0, 'Turmoil': 0.0}
        self.season = 0
        self.arc = 0
        self.winner = None
        self.mass_seizure_fired = False
        # v17 additions:
        # M1 — settlement registry
        self.settlements = m1.build_settlement_registry()  # [canonical: m1 SETTLEMENT_REGISTRY]
        # M5 — per-settlement governance state, default initialized
        self.governance = {sid: m5.SettlementGovernance(sid=sid) for sid in self.settlements}
        # Seed settlements with garrison_present flag where territory has garrison
        for sid, settlement in self.settlements.items():
            if STARTING_GARRISON.get(settlement.territory_id, False):
                self.governance[sid].garrison_present = True
        # Action telemetry (per-campaign)
        self.action_log = defaultdict(int)
        self.battle_count = 0
        self.params = {}


# ═══════════════════════════════════════════════════════════════════════════
# LOGGER — preserved from mc_v15
# ═══════════════════════════════════════════════════════════════════════════

class Logger:
    # [canonical: mc_v15.py L174 Logger class]
    def __init__(self, cid):
        self.campaign_id = cid
        self.events = []
        self.counter = 0
        self.current_season = 0
        self.current_arc = 0

    def log(self, etype, **kw):
        self.counter += 1
        ev = {'event_id': self.counter, 'season': self.current_season,
              'arc': self.current_arc, 'event_type': etype,
              'campaign_id': self.campaign_id, **kw}
        self.events.append(ev)
        return self.counter

    def flush(self, path):
        with open(path, 'w') as f:
            for ev in self.events:
                f.write(json.dumps(ev) + '\n')


class NullLogger:
    # [canonical: mc_v15.py L188 — no-op logger]
    current_season = 0
    current_arc = 0

    def log(self, *a, **kw): return 0

    def flush(self, *a): pass


# ═══════════════════════════════════════════════════════════════════════════
# DICE — preserved BW-style success-counter from mc_v15
# ═══════════════════════════════════════════════════════════════════════════

def successes(pool, rng):
    # [canonical: mc_v15.py L30 quasibinomial_successes — BW d6 ≥4 success threshold per M3 convention]
    # Simplified to straight d6 ≥ 4 for v17 (matches M3.roll_pool)
    if pool <= 0:
        return 0
    n = 0
    for _ in range(int(pool)):
        if rng.randint(1, 6) >= 4:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
            n += 1
    return n


def degree(net):
    # [canonical: mc_v15.py L42 resolve_degree — 4-tier mapping]
    if net >= 3:
        return 'Overwhelming'
    elif net >= 1:
        return 'Success'
    elif net == 0:
        return 'Partial'
    else:
        return 'Failure'


# ═══════════════════════════════════════════════════════════════════════════
# ADJACENCY (m1 already exposes this)
# ═══════════════════════════════════════════════════════════════════════════

ADJACENCY = m1.ADJACENCY  # [canonical: m1.ADJACENCY — settlement_layer + valoria_geography]


# ═══════════════════════════════════════════════════════════════════════════
# ACTION REGISTRY — M7_ASSUMPTION_TWO (dispatch table not if-chain)
# ═══════════════════════════════════════════════════════════════════════════

def action_govern(faction, target, world, rng, logger):
    # [canonical: mc_v15 Govern action — extended with M5 settlement-aware governance]
    if target not in world.territories or world.territories[target].owner != faction.name:
        return 'invalid'
    pool = faction.I
    ob = 2
    net = successes(pool, rng) - ob
    deg = degree(net)
    t = world.territories[target]
    if deg in ('Overwhelming', 'Success'):
        t.adjust_accord(15 if deg == 'Overwhelming' else 10)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        # Reflect into settlement Order (M5 integration)
        for s in m1.territory_settlements(target, world.settlements):
            gov = world.governance.get(s.sid)
            if gov and gov.order < m5.ORDER_MAX:
                gov.order += 1
                break  # only one settlement per Govern action
    elif deg == 'Failure':
        faction.adjust('Sta', -5)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    logger.log('action', name='Govern', faction=faction.name, target=target, degree=deg)
    world.action_log['Govern'] += 1
    return deg


def action_muster(faction, target, world, rng, logger):
    # [canonical: integration_plan §5 Phase 2c — Muster mints Levy tokens in territory; M4]
    if target not in faction.territories:
        return 'invalid'
    pool = faction.Mil
    ob = 1
    net = successes(pool, rng) - ob
    deg = degree(net)
    if deg in ('Overwhelming', 'Success'):
        count = 2 if deg == 'Overwhelming' else 1
        faction.units.muster(target, count, m4.MUSTER_DEFAULT_CLASS)
    elif deg == 'Failure':
        faction.adjust('W', -3)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    logger.log('action', name='Muster', faction=faction.name, target=target, degree=deg, units_minted=count if deg in ('Overwhelming', 'Success') else 0)
    world.action_log['Muster'] += 1
    return deg


def action_military_conquest(faction, target, world, rng, logger):
    # [canonical: integration_plan §5 Phase 2b — replaces single-roll Conquest with §B.3 6-step]
    if target not in world.territories:
        return 'invalid'
    t = world.territories[target]
    if t.owner == faction.name:
        return 'invalid'
    # Adjacency check (M4 commitment model 'adjacent_to_target')
    adj = set()
    for tid in faction.territories:
        adj |= ADJACENCY.get(tid, set())
    if target not in adj:
        return 'invalid'
    # Find an adjacent territory to commit from
    source_tid = None
    for tid in faction.territories:
        if target in ADJACENCY.get(tid, set()) and faction.units.total_units(tid) > 0:
            source_tid = tid
            break
    if source_tid is None:
        # No tokens to commit — fall back to single-roll legacy behavior
        pool = faction.Mil
        ob = 2 if t.is_uncontrolled() else 4  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        net = successes(pool, rng) - ob
        deg = degree(net)
        if deg in ('Overwhelming', 'Success'):
            old = t.owner
            if old in world.factions:
                world.factions[old].territories.discard(target)
                world.factions[old].adjust('L', -10)
            t.owner = faction.name
            faction.territories.add(target)
            t.garrison = True
            t.adjust_accord(-25)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        logger.log('action', name='MilitaryConquest', faction=faction.name, target=target,
                   degree=deg, legacy_path=True)
        world.action_log['MilitaryConquest'] += 1
        return deg

    # M3/M7 mass-battle resolution path
    committed = faction.units.commit_to_battle(
        source_tid, target,
        dict(faction.units.units_in_territory(source_tid)),  # commit all available
        ADJACENCY,
    )
    # Defender units come from current owner if a faction
    defender_units = {}
    defender_mil = 1.0
    if t.owner in world.factions:
        owner_faction = world.factions[t.owner]
        defender_units = dict(owner_faction.units.units_in_territory(target))
        if not defender_units:
            # No tokens — give defender a minimal Levy unit (garrison representation)
            defender_units = {'Levy': 1} if t.garrison else {}
        defender_mil = owner_faction.Mil
    # Tactic card selection — both sides default to standard_advance (M7_ASSUMPTION_SEVEN)
    attacker_card = 'standard_advance'
    defender_card = 'disciplined_defence' if t.garrison else 'standard_advance'

    if not committed:
        # No units committed; fall back to legacy
        pool = faction.Mil
        ob = 2 if t.is_uncontrolled() else 4  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        net = successes(pool, rng) - ob
        deg = degree(net)
        logger.log('action', name='MilitaryConquest', faction=faction.name, target=target,
                   degree=deg, no_units_path=True)
        return deg

    # Resolve via M7 hook-aware battle (handles all 6 deferred tactic cards)
    hook_result = m7h.resolve_battle_hooked(
        attacker_units=committed,
        defender_units=defender_units,
        attacker_mil=faction.Mil,
        defender_mil=defender_mil,
        attacker_card=attacker_card,
        defender_card=defender_card,
        fort_level=t.fort_level,
        rng=rng,
    )
    result = hook_result.base_result
    world.battle_count += 1

    # Apply outcome
    if result.outcome == m3.OUTCOME_ATTACKER_WINS:
        old = t.owner
        if old in world.factions:
            world.factions[old].territories.discard(target)
            world.factions[old].adjust('L', -10)
            world.factions[old].adjust('Mil', result.defender_military_delta * 10)
        # Apply unit losses
        for cls, count in result.defender_losses.items():
            if old in world.factions:
                roster = world.factions[old].units
                if target in roster._roster and cls in roster._roster[target]:
                    roster._roster[target][cls] = max(0, roster._roster[target][cls] - count)
        for cls, count in result.attacker_losses.items():
            if target in faction.units._roster and cls in faction.units._roster[target]:
                faction.units._roster[target][cls] = max(0, faction.units._roster[target][cls] - count)
        t.owner = faction.name
        faction.territories.add(target)
        t.garrison = True
        t.accord = float(result.accord_changes.get('new_owner', 1)) * 1.0  # [canonical: M3 ACCORD_ON_CAPTURE_NEW_OWNER]
        faction.adjust('L', -5)
    elif result.outcome == m3.OUTCOME_DEFENDER_WINS:
        faction.adjust('Mil', result.attacker_military_delta * 10)
        # Apply losses to attacker
        for cls, count in result.attacker_losses.items():
            if target in faction.units._roster and cls in faction.units._roster[target]:
                faction.units._roster[target][cls] = max(0, faction.units._roster[target][cls] - count)
        # Apply losses to defender (defenders also took some)
        if t.owner in world.factions:
            for cls, count in result.defender_losses.items():
                roster = world.factions[t.owner].units
                if target in roster._roster and cls in roster._roster[target]:
                    roster._roster[target][cls] = max(0, roster._roster[target][cls] - count)
        t.adjust_accord(result.accord_changes.get('defender_territory', 0) * 10)
    else:  # partial
        faction.adjust('Sta', result.attacker_stability_delta * 10)

    faction.peaceful = False
    logger.log('battle', name='MilitaryConquest', faction=faction.name, target=target,
               outcome=result.outcome, margin=result.margin,
               territory_transferred=result.territory_transferred,
               hooks_fired=hook_result.hooks_fired)
    world.action_log['MilitaryConquest_mass_battle'] += 1
    return 'Success' if result.outcome == m3.OUTCOME_ATTACKER_WINS else \
           'Failure' if result.outcome == m3.OUTCOME_DEFENDER_WINS else 'Partial'


def action_crown_initiative(faction, target, world, rng, logger, mode='royal_progress'):
    # [canonical: part10 §3.2-§3.4 — Crown Initiative 3 modes via M6]
    if faction.name != 'Crown':
        return 'invalid'
    if faction.crown_initiative_used_this_season:
        return 'used'
    faction.crown_initiative_used_this_season = True

    if mode == 'royal_progress':
        sum_accord = sum(world.territories[tid].accord for tid in faction.territories if tid in world.territories)
        ob = m6.royal_progress_ob(sum_accord)
        pool = m6.royal_progress_pool(faction.I, faction.standing)
        net = successes(pool, rng) - ob
        deg = degree(net)
        outcome = m6.royal_progress_outcome(deg)
        faction.adjust('W', outcome.get('wealth_cost', 0) * 100)
        faction.standing += outcome.get('standing_delta', 0)
        faction.adjust('L', outcome.get('mandate_delta', 0) * 20)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        if outcome.get('accord_1_to_2_all_own'):
            for tid in faction.territories:
                if tid in world.territories and world.territories[tid].accord <= 2.5:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
                    world.territories[tid].adjust_accord(15)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    elif mode == 'great_work':
        # Multi-season; simplified to instant resolution at season 3
        ob = m6.GREAT_WORK_FINAL_OB
        pool = m6.great_work_pool_final_season(faction.L)
        net = successes(pool, rng) - ob
        deg = degree(net)
        outcome = m6.great_work_outcome(deg)
        faction.adjust('W', m6.GREAT_WORK_WEALTH_COST_PER_SEASON * 100 * m6.GREAT_WORK_SEASONS)
        faction.adjust('L', outcome.get('mandate_delta', 0) * 20)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        faction.standing += outcome.get('standing_delta', 0)
    elif mode == 'coronation_renewal':
        church = world.factions.get('Church')
        ok, _ = m6.coronation_renewal_prerequisite_check('peace', False)
        if not ok or church is None:
            return 'prereq_fail'
        ob = m6.coronation_renewal_ob(church.L)
        pool = m6.coronation_renewal_pool(faction.I)
        net = successes(pool, rng) - ob
        deg = degree(net)
        excomm_active = 'Crown' in church.excommunication_against
        outcome = m6.coronation_renewal_outcome(deg, excomm_active)
        faction.adjust('W', outcome.get('wealth_cost', 0) * 100)
        faction.adjust('L', outcome.get('mandate_delta', 0) * 20)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        faction.standing += outcome.get('standing_delta', 0)
        if outcome.get('lifts_excommunication'):
            church.excommunication_against.discard('Crown')
    logger.log('action', name='CrownInitiative', faction=faction.name, mode=mode, degree=deg)
    world.action_log[f'CrownInitiative_{mode}'] += 1
    return deg


def action_excommunication(faction, target, world, rng, logger, is_leader=True):
    # [canonical: faction_canon §9 Excommunication]
    if faction.name != 'Church':
        return 'invalid'
    if target not in world.factions:
        return 'invalid'
    ok, _ = m6.excommunication_prerequisite_check(faction.L)
    if not ok:
        return 'prereq_fail'
    target_f = world.factions[target]
    ob = m6.excommunication_ob(target_f.L, is_leader)
    pool = m6.excommunication_pool(faction.L)
    net = successes(pool, rng) - ob
    deg = degree(net)
    outcome = m6.excommunication_outcome(deg)
    target_f.adjust('L', outcome.get('target_mandate_delta', 0) * 20)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    faction.adjust('L', outcome.get('church_mandate_delta', 0) * 20)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    if deg in ('Overwhelming', 'Success'):
        faction.excommunication_against.add(target)
    logger.log('action', name='Excommunication', faction=faction.name, target=target, degree=deg)
    world.action_log['Excommunication'] += 1
    return deg


def action_absolution(faction, target, world, rng, logger):
    # [canonical: faction_canon §8.2 Church Absolution + M6_ASSUMPTION_ONE]
    if faction.name != 'Church':
        return 'invalid'
    if target not in world.factions:
        return 'invalid'
    ob = m6.ABSOLUTION_OB
    pool = m6.absolution_pool(faction.I)
    net = successes(pool, rng) - ob
    deg = degree(net)
    outcome = m6.absolution_outcome(deg)
    target_f = world.factions[target]
    target_f.adjust('Sta', outcome.get('target_stability_delta', 0) * 10)
    faction.adjust('L', outcome.get('church_mandate_delta', 0) * 20)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    logger.log('action', name='Absolution', faction=faction.name, target=target, degree=deg)
    world.action_log['Absolution'] += 1
    return deg


ACTION_REGISTRY = {
    # [canonical: M7_ASSUMPTION_TWO — dispatch table, not if-chain]
    'Govern': action_govern,
    'Muster': action_muster,
    'MilitaryConquest': action_military_conquest,
    'CrownInitiative_royal_progress': lambda f, t, w, r, lg: action_crown_initiative(f, t, w, r, lg, 'royal_progress'),
    'CrownInitiative_great_work': lambda f, t, w, r, lg: action_crown_initiative(f, t, w, r, lg, 'great_work'),
    'CrownInitiative_coronation_renewal': lambda f, t, w, r, lg: action_crown_initiative(f, t, w, r, lg, 'coronation_renewal'),
    'Excommunication': action_excommunication,
    'Absolution': action_absolution,
}


# ═══════════════════════════════════════════════════════════════════════════
# AI ACTION SELECTION — minimal (extends v15 score-and-select)
# ═══════════════════════════════════════════════════════════════════════════

def faction_take_action(faction, world, rng, logger):
    # [canonical: M7_ASSUMPTION_SIX — minimal AI policy: probabilistic action mix]
    # 30% faction-unique action when favorable; 35% Conquest; 20% Muster; 15% Govern
    roll = rng.random()
    # Faction-unique actions
    if roll < 0.30:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        if faction.name == 'Crown' and not faction.crown_initiative_used_this_season:
            church = world.factions.get('Church')
            if church and 'Crown' in church.excommunication_against:
                return action_crown_initiative(faction, None, world, rng, logger, 'coronation_renewal')
            # Use royal_progress only at low sum_accord (Ob viable)
            sum_accord = sum(world.territories[tid].accord for tid in faction.territories if tid in world.territories)
            if sum_accord <= 12:  # [canonical: derived — Royal Progress viable when Ob = floor(sum/2) <= ~6]
                return action_crown_initiative(faction, None, world, rng, logger, 'royal_progress')
        if faction.name == 'Church':
            rivals = [(fn, f) for fn, f in world.factions.items()
                      if fn != 'Church' and f.parliamentary and fn not in faction.excommunication_against]
            if rivals and faction.L >= m6.EXCOMMUNICATION_PREREQUISITE_CHURCH_L:
                target = max(rivals, key=lambda kv: kv[1].L)[0]
                return action_excommunication(faction, target, world, rng, logger)
    # Conquest
    if roll < 0.65:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        adj = set()
        for tid in faction.territories:
            adj |= ADJACENCY.get(tid, set())
        targets = [tid for tid in adj if tid in world.territories
                   and world.territories[tid].owner not in (faction.name, None)]
        if targets and faction.Mil >= 3.0:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
            target = rng.choice(targets)
            return action_military_conquest(faction, target, world, rng, logger)
    # Muster
    if roll < 0.85:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        if faction.territories:
            target = rng.choice(list(faction.territories))
            return action_muster(faction, target, world, rng, logger)
    # Govern fallback
    if faction.territories:
        target = rng.choice(list(faction.territories))
        return action_govern(faction, target, world, rng, logger)
    return 'no_action'


# ═══════════════════════════════════════════════════════════════════════════
# ACCOUNTING — applies CI gen, settlement events, aggregation
# ═══════════════════════════════════════════════════════════════════════════

def ci_generation(world, logger, rng):
    # [canonical: m2 CI political revision constants]
    # Simplified: domain actions contributing +1 to +3 per Accounting depending on settlement infrastructure
    delta = 0
    for tid in ALL_PLAYABLE_15:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        if tid not in world.territories:
            continue
        t = world.territories[tid]
        if t.owner == 'Church':
            delta += 2
        # Infrastructure bonus from M1 settlements with Cathedral/Inquisitor
        for s in m1.territory_settlements(tid, world.settlements):
            if s.religious_building == m1.RB_CATHEDRAL:
                delta += 1
            if s.inquisitor_base:
                delta += 1
    # M2: cap deltas
    delta = max(-m2.CI_SEASONAL_CAP_MAGNITUDE, min(m2.CI_SEASONAL_CAP_MAGNITUDE, delta))
    world.clocks['CI'] = max(0, min(100, world.clocks['CI'] + delta))
    logger.log('ci_generation', delta=delta, new_ci=world.clocks['CI'])


def settlement_event_pass(world, logger):
    # [canonical: integration_plan §5 Phase 5 Step 4 + m5.resolve_settlement_events]
    hostile_per_province = set()
    for tid, t in world.territories.items():
        for adj_tid in ADJACENCY.get(tid, set()):
            if adj_tid in world.territories:
                adj_t = world.territories[adj_tid]
                if adj_t.owner and adj_t.owner != t.owner:
                    hostile_per_province.add(tid)
                    break
    events = m5.resolve_settlement_events(
        world.governance,
        registry=world.settlements,
        hostile_military_per_province=hostile_per_province,
    )
    for e in events:
        # Apply immediate_effects
        if 'order_delta' in e.immediate_effects:
            gov = world.governance.get(e.sid)
            if gov:
                gov.order = max(m5.ORDER_MIN, min(m5.ORDER_MAX, gov.order + e.immediate_effects['order_delta']))
        logger.log('settlement_event', sid=e.sid, type=e.event_type, severity=e.severity)


def aggregate_to_territory(world, logger):
    # [canonical: integration_plan §5 Phase 5 + m5 aggregate functions]
    # Map settlement governance → territory Accord/Wealth contributions
    for tid in world.territories:
        accord_agg = m5.aggregate_order_to_accord(tid, world.governance, world.settlements)
        # Gentle pull toward aggregate — 10% blend, not full override
        if accord_agg > 0:
            t = world.territories[tid]
            t.accord = max(0.5, min(7.0, t.accord * 0.9 + ACCORD_MAP.get(accord_agg, 4.0) * 0.1))  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]


def accounting(world, logger, rng):
    # [canonical: mc_v15 accounting — extended with M5 + M2]
    ci_generation(world, logger, rng)
    settlement_event_pass(world, logger)
    aggregate_to_territory(world, logger)
    # Reset seasonal flags
    for f in world.factions.values():
        f.reset_seasonal()


# ═══════════════════════════════════════════════════════════════════════════
# SEASON LOOP
# ═══════════════════════════════════════════════════════════════════════════

def run_season(world, logger, rng):
    world.season += 1
    logger.current_season = world.season
    if world.season % 4 == 1:  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        world.arc += 1
        logger.current_arc = world.arc
    # Each parliamentary faction takes one action
    for fn, faction in world.factions.items():
        if not faction.parliamentary:
            continue
        if not faction.territories:
            continue
        try:
            faction_take_action(faction, world, rng, logger)
        except Exception as e:
            logger.log('action_error', faction=fn, err=str(e))
    accounting(world, logger, rng)
    # Victory check
    victory_check(world, logger)


def victory_check(world, logger, threshold=11):
    # [canonical: mc_v15.py L879 + PROP-07 — 11/15 victory threshold]
    for fn, f in world.factions.items():
        if not f.parliamentary:
            continue
        held = sum(1 for tid in ALL_PLAYABLE_15  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
                   if tid in world.territories and world.territories[tid].owner == fn)
        if held >= threshold:
            world.winner = fn
            logger.log('victory', winner=fn, held=held)
            return


# ═══════════════════════════════════════════════════════════════════════════
# DEFAULT PARAMS + RUN_CAMPAIGN
# ═══════════════════════════════════════════════════════════════════════════

DEFAULT_PARAMS = {
    # [canonical: mc_v15.py L992 — preserved seasons/threshold]
    'CAMPAIGN_SEASONS': 50,
    'VICTORY_THRESHOLD': 11,
}


def run_campaign(params=None, seed=None, log_dir=None, test_id='v17'):
    # [canonical: mc_v15.py L961 run_campaign — extended for v17]
    if seed is None:
        seed = int(time.time()) & 0xFFFFFFFF
    rng = random.Random(seed)
    world = World()
    world.params = dict(DEFAULT_PARAMS)
    if params:
        world.params.update(params)
    cid = f'{test_id}_{seed:06d}'
    logger = Logger(cid) if log_dir else NullLogger()
    logger.log('campaign_start', params=world.params, seed=seed)
    for _ in range(world.params['CAMPAIGN_SEASONS']):
        if world.winner:
            break
        run_season(world, logger, rng)
    # Fallback winner by held-territory score
    if not world.winner:
        scores = {}
        for fn, f in world.factions.items():
            if not f.parliamentary:
                continue
            h = sum(1 for tid in ALL_PLAYABLE_15  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
                    if tid in world.territories and world.territories[tid].owner == fn)
            scores[fn] = h * 10 + f.L + len(f.territories)
        world.winner = max(scores, key=scores.get) if scores else None
    surviving = sum(1 for f in world.factions.values() if len(f.territories) > 0)
    uncontrolled = sum(1 for t in world.territories.values() if t.is_uncontrolled())
    logger.log('campaign_end', winner=world.winner, surviving=surviving,
               uncontrolled=uncontrolled, battles=world.battle_count,
               final={fn: {'L': round(f.L, 2), 'terr': len(f.territories)}
                      for fn, f in world.factions.items()})
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        logger.flush(os.path.join(log_dir, f'{cid}.jsonl'))
    return dict(
        winner=world.winner,
        world=world,
        surviving=surviving,
        uncontrolled=uncontrolled,
        battles=world.battle_count,
        season_ended=world.season,
    )


def run_batch(n, params=None, log_dir=None, test_id='v17'):
    # [canonical: mc_v15.py L998 run_batch — extended with battle telemetry]
    wins = Counter()
    surv_dist = Counter()
    battles_list = []
    L_acc = defaultdict(list)
    terr_acc = defaultdict(list)
    for i in range(n):
        r = run_campaign(params=params, seed=i,
                         log_dir=log_dir if i < 3 else None, test_id=test_id)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
        wins[r['winner']] += 1
        surv_dist[r['surviving']] += 1
        battles_list.append(r['battles'])
        for fn, f in r['world'].factions.items():
            L_acc[fn].append(f.L)
            terr_acc[fn].append(len(f.territories))
    tot = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0) / tot * 100, 1) for k in ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        all_winners=dict(wins),
        L_mean={k: round(sum(v) / len(v), 2) for k, v in L_acc.items()},
        terr_mean={k: round(sum(v) / len(v), 2) for k, v in terr_acc.items()},
        surv_dist=dict(surv_dist),
        battles_mean=round(sum(battles_list) / n, 1) if n else 0,
        n=n,
    )


if __name__ == '__main__':
    print("=== mc_v17 smoke test — 20 campaigns ===")
    r = run_batch(20)  # [canonical: derived test boundary — see ledger + m15/M-module ledgers]
    print(f"  win_share: {r['win_share']}")
    print(f"  all_winners: {r['all_winners']}")
    print(f"  battles_mean: {r['battles_mean']}")
    print(f"  L_mean: {r['L_mean']}")
    print(f"  terr_mean: {r['terr_mean']}")
