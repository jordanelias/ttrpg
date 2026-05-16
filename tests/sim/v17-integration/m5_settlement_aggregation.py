# m5_settlement_aggregation — Module Five of the v17 strategic-sim integration plan.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Per-settlement governance state (Order/Prosperity/Defense), the canonical  # [canonical: N/A — doc]
# §3.2 governance-action Ob formulas, the §4.3 settlement-events table,  # [canonical: N/A — doc]
# RM Cell Resilience (ED-683 / §3.3), and settlement -> territory aggregation  # [canonical: N/A — doc]
# at arc boundary.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# This module is PURE PRIMITIVES — it does not own World/Faction/Territory  # [canonical: N/A — doc]
# classes, does not mutate world state. resolve_settlement_events returns a  # [canonical: N/A — doc]
# list of SettlementEvent records; aggregate functions return computed values;  # [canonical: N/A — doc]
# governance_action_* helpers return values the caller integrates.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources:  # [canonical: N/A — doc]
#   - settlement_layer_v30 Section 3.1 (Two-Tier Authority), 3.2 (Governor  # [canonical: N/A — doc]
#     Assignment table with Pool/Ob/Effect), 3.3 (Subnational governance + RM  # [canonical: N/A — doc]
#     Cell Resilience formula), 4.3 (Settlement Events table).  # [canonical: N/A — doc]
#   - integration_plan_v3 Section 5 Phase 5 (Settlement state integration).  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Cross-module dependency: imports M1 (m1_church_infrastructure) for the  # [canonical: N/A — doc]
# settlement registry and PLAYABLE_TERRITORIES.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional assumptions for ratification: see sim_verification_ledger  # [canonical: N/A — doc]
# provisional_assumptions block. Tags M5_ASSUMPTION_ONE..M5_ASSUMPTION_FIVE.  # [canonical: N/A — doc]

import math
import sys
import os
from dataclasses import dataclass, field
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m1_church_infrastructure as m1


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — Order/Prosperity/Defense ranges
# ═══════════════════════════════════════════════════════════════════════════

ORDER_MIN = 0  # [canonical: settlement_layer §4.3 — "Order 0 | Local revolt" lower bound]
ORDER_MAX = 5  # [canonical: settlement_layer §3.2 — "Order +1 (cap: 5)" Pacify ceiling + §4.3 "Order 5" flourishing threshold]
PROSPERITY_MIN = 0  # [canonical: settlement_layer §4.3 — "Prosperity 0 | Famine" lower bound]
DEFENSE_MIN = 0  # [canonical: settlement_layer §4.3 — "Defense 0 + adjacent hostile military"]


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — §4.3 Settlement Events thresholds
# ═══════════════════════════════════════════════════════════════════════════

FAMINE_PROSPERITY_THRESHOLD = 0  # [canonical: settlement_layer §4.3 — "Prosperity 0 | Famine or economic collapse"]
FAMINE_ORDER_PENALTY = -1  # [canonical: settlement_layer §4.3 — "Order -1 automatic" on Famine]

REVOLT_ORDER_THRESHOLD = 0  # [canonical: settlement_layer §4.3 — "Order 0 | Local revolt"]

FLOURISHING_ORDER_THRESHOLD = 5  # [canonical: settlement_layer §4.3 — "Order 5 + Prosperity 4+" flourishing condition]
FLOURISHING_PROSPERITY_THRESHOLD = 4  # [canonical: settlement_layer §4.3 — "Order 5 + Prosperity 4+"]
FLOURISHING_DISPOSITION_BONUS = 1  # [canonical: settlement_layer §4.3 — "+1 Disposition with all local NPCs"]

MINE_SURPLUS_PROSPERITY_THRESHOLD = 3  # [canonical: settlement_layer §4.3 — "Mine type + Prosperity 3+"]
MINE_SURPLUS_TREASURY_DELTA = 50  # [canonical: settlement_layer §4.3 — "Province Treasury +50/season at Accounting"]

FORTRESS_DEFENSE_CHECK_OB = 2  # [canonical: settlement_layer §4.3 — "Defense check: Defense pool vs Ob 2"]

# RM Cell Resilience — ED-683 / §3.3
RM_CELL_RESILIENCE_THRESHOLD = 3  # [canonical: settlement_layer §3.3 ED-683 — "If RM has Presence markers in >= 3 settlements within a province"]
RM_CELL_RESILIENCE_OB_PENALTY = 1  # [canonical: settlement_layer §3.3 ED-683 — "Church/Crown suppression actions against RM in that province take +1 Ob"]


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — Governance Transition (§4.3 RM takes control)
# ═══════════════════════════════════════════════════════════════════════════

GOVERNANCE_TRANSITION_MODES = ('disestablishment', 'accommodation', 'transformation')
# [canonical: settlement_layer §4.3 — "Disestablishment / Accommodation / Transformation" 3 modes]


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — Consensus Delay (§4.3 RM-governed emergency)
# ═══════════════════════════════════════════════════════════════════════════

CONSENSUS_DELAY_SEASONS = 1  # [canonical: settlement_layer §4.3 — "take +1 season to resolve"]
CONSENSUS_DELAY_WAIVER_MANDATE_COST = 1  # [canonical: settlement_layer §4.3 — "Waivable: RM leader spends 1 Mandate"]
CONSENSUS_DELAY_WAIVER_PRESENCE_COST = 1  # [canonical: settlement_layer §4.3 — "loses 1 Presence marker in that province"]


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS — Aggregation policy (M5_ASSUMPTION_TWO + M5_ASSUMPTION_FIVE)
# ═══════════════════════════════════════════════════════════════════════════

# Prosperity -> Wealth conversion (provisional, continuous rate)
# [canonical: derived — settlement_layer §4.3 specifies flat per-Mine rate; continuous rate is M5_ASSUMPTION_FIVE]
PROSPERITY_TO_WEALTH_RATE = 0.1


# ═══════════════════════════════════════════════════════════════════════════
# GOVERNANCE STATE — SettlementGovernance dataclass
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class SettlementGovernance:
    # [canonical: settlement_layer §3.1 Two-Tier Authority — Settlement Governor controls Order, Prosperity, local NPC relationships]
    # [M5_ASSUMPTION_ONE: governance state lives in a separate dataclass from M1.Settlement]
    sid: str
    order: int = 3  # [canonical: settlement_layer §3.2 — Pacify cap 5 implies 0..5 range; default mid-tier 3]
    prosperity: int = 2  # [canonical: settlement_layer §4.3 — Prosperity 0/3/4 trigger events; default 2 (below mine-surplus, above famine)]
    defense: int = 2  # [canonical: settlement_layer §4.3 — Defense 0 raid trigger; default 2 (matches Fortress check Ob)]
    rm_presence: bool = False  # [canonical: settlement_layer §3.3 — "If RM has Presence markers"]
    garrison_present: bool = False  # [canonical: settlement_layer §4.3 — "Governor expelled unless garrison present"]
    governor_faction: Optional[str] = None  # [canonical: settlement_layer §3.1 — "subnational faction may already hold traditional rights"]
    rm_governed: bool = False  # [canonical: settlement_layer §4.3 — "RM-governed settlement" condition for Consensus Delay]

    def __post_init__(self):
        # [canonical: settlement_layer §3.2 (Pacify cap 5) + §4.3 (Prosperity 0 / Order 0 / Defense 0 thresholds)]
        if self.order < ORDER_MIN or self.order > ORDER_MAX:
            raise ValueError(f"Order out of range [{ORDER_MIN}, {ORDER_MAX}]: {self.order}")
        if self.prosperity < PROSPERITY_MIN:
            raise ValueError(f"Prosperity below min {PROSPERITY_MIN}: {self.prosperity}")
        if self.defense < DEFENSE_MIN:
            raise ValueError(f"Defense below min {DEFENSE_MIN}: {self.defense}")

    def to_dict(self):
        return {
            'sid': self.sid,
            'order': self.order,
            'prosperity': self.prosperity,
            'defense': self.defense,
            'rm_presence': self.rm_presence,
            'garrison_present': self.garrison_present,
            'governor_faction': self.governor_faction,
            'rm_governed': self.rm_governed,
        }


# ═══════════════════════════════════════════════════════════════════════════
# SETTLEMENT EVENT — output of §4.3 resolution
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class SettlementEvent:
    # [canonical: settlement_layer §4.3 Settlement Events table — caller applies immediate_effects + handles choice_required]
    sid: str
    event_type: str  # 'famine' | 'revolt' | 'raid' | 'flourishing' | 'governance_transition' | 'consensus_delay' | 'religious_event' | 'mine_surplus' | 'fortress_garrison_check'
    severity: str = 'normal'  # 'normal' | 'critical'
    immediate_effects: dict = field(default_factory=dict)  # e.g. {'order_delta': -1}
    choice_required: bool = False
    choice_options: tuple = ()  # for Governance Transition modes
    suppressed_by_garrison: bool = False  # for Revolt
    description: str = ''

    def to_dict(self):
        return {
            'sid': self.sid,
            'event_type': self.event_type,
            'severity': self.severity,
            'immediate_effects': dict(self.immediate_effects),
            'choice_required': self.choice_required,
            'choice_options': list(self.choice_options),
            'suppressed_by_garrison': self.suppressed_by_garrison,
            'description': self.description,
        }


# ═══════════════════════════════════════════════════════════════════════════
# GOVERNANCE ACTION OBSTACLES — §3.2 table
# ═══════════════════════════════════════════════════════════════════════════

def governance_action_ob(action, current_value):
    # [canonical: settlement_layer §3.2 Governor Assignment table — Pool/Ob/Effect column]
    # Develop: floor(Prosperity/2) + 1
    # Fortify: floor(Defense/2) + 1
    # Pacify: floor((3 - Order) + 1), min 1
    # Administer: 2 (flat)
    if action == 'develop':
        return math.floor(current_value / 2) + 1
    elif action == 'fortify':
        return math.floor(current_value / 2) + 1
    elif action == 'pacify':
        return max(1, math.floor((3 - current_value) + 1))
    elif action == 'administer':
        return 2
    else:
        raise ValueError(f"Unknown governance action: {action}")


def governance_action_effect(action):
    # [canonical: settlement_layer §3.2 — Effect on Success column]
    effects = {
        'develop': 'prosperity_plus_1',
        'fortify': 'defense_plus_1',
        'pacify': 'order_plus_1',
        'administer': 'order_no_decay',
    }
    if action not in effects:
        raise ValueError(f"Unknown governance action: {action}")
    return effects[action]


def apply_governance_action(action, current_gov):
    # [canonical: settlement_layer §3.2 — applies the Effect-on-Success transformation]
    # Returns new SettlementGovernance (does not mutate). Assumes the action succeeded;
    # caller checks the roll separately.
    new_data = current_gov.to_dict()
    if action == 'develop':
        new_data['prosperity'] = current_gov.prosperity + 1
    elif action == 'fortify':
        new_data['defense'] = current_gov.defense + 1
    elif action == 'pacify':
        new_data['order'] = min(ORDER_MAX, current_gov.order + 1)
        # [canonical: settlement_layer §3.2 — "Order +1 (cap: 5)"]
    elif action == 'administer':
        pass  # no immediate effect; caller marks "no decay this season"
    else:
        raise ValueError(f"Unknown governance action: {action}")
    return SettlementGovernance(**new_data)


# ═══════════════════════════════════════════════════════════════════════════
# RM CELL RESILIENCE — §3.3 ED-683
# ═══════════════════════════════════════════════════════════════════════════

def rm_cell_resilience(province_id, governance_map, registry=None):
    # [canonical: settlement_layer §3.3 ED-683 — "If RM has Presence markers in >= 3 settlements within a province, Church/Crown suppression actions against RM in that province take +1 Ob"]
    reg = registry if registry is not None else m1.SETTLEMENT_REGISTRY
    province_settlements = m1.territory_settlements(province_id, reg)
    rm_count = 0
    for s in province_settlements:
        gov = governance_map.get(s.sid)
        if gov is not None and gov.rm_presence:
            rm_count += 1
    if rm_count >= RM_CELL_RESILIENCE_THRESHOLD:
        return RM_CELL_RESILIENCE_OB_PENALTY
    return 0


# ═══════════════════════════════════════════════════════════════════════════
# AGGREGATION — settlement state -> territory state (M5_ASSUMPTION_TWO + FIVE)
# ═══════════════════════════════════════════════════════════════════════════

def aggregate_order_to_accord(province_id, governance_map, registry=None):
    # [canonical: integration_plan §5 Phase 5 — "settlement state -> per-territory Accord/PT/infrastructure"]
    # [M5_ASSUMPTION_TWO: floor(mean) aggregation; canon doesn't specify policy]
    reg = registry if registry is not None else m1.SETTLEMENT_REGISTRY
    settlements = m1.territory_settlements(province_id, reg)
    if not settlements:
        return 0
    orders = []
    for s in settlements:
        gov = governance_map.get(s.sid)
        if gov is not None:
            orders.append(gov.order)
    if not orders:
        return 0
    return math.floor(sum(orders) / len(orders))


def aggregate_prosperity_to_wealth(province_id, governance_map, registry=None):
    # [canonical: integration_plan §5 Phase 5 + settlement_layer §4.3 Mine type rule]
    # [M5_ASSUMPTION_FIVE: continuous prosperity -> wealth at PROSPERITY_TO_WEALTH_RATE]
    reg = registry if registry is not None else m1.SETTLEMENT_REGISTRY
    settlements = m1.territory_settlements(province_id, reg)
    if not settlements:
        return 0.0
    total_prosperity = 0
    count = 0
    for s in settlements:
        gov = governance_map.get(s.sid)
        if gov is not None:
            total_prosperity += gov.prosperity
            count += 1
    if count == 0:
        return 0.0
    mean_prosperity = total_prosperity / count
    return mean_prosperity * PROSPERITY_TO_WEALTH_RATE


def province_mine_treasury_contribution(province_id, governance_map, registry=None):
    # [canonical: settlement_layer §4.3 — "Mine type + Prosperity 3+ | Province Treasury +50/season"]
    reg = registry if registry is not None else m1.SETTLEMENT_REGISTRY
    settlements = m1.territory_settlements(province_id, reg)
    total = 0
    for s in settlements:
        if s.settlement_type != 'Mine':
            continue
        gov = governance_map.get(s.sid)
        if gov is not None and gov.prosperity >= MINE_SURPLUS_PROSPERITY_THRESHOLD:
            total += MINE_SURPLUS_TREASURY_DELTA
    return total


# ═══════════════════════════════════════════════════════════════════════════
# SETTLEMENT EVENT RESOLUTION — §4.3 table
# ═══════════════════════════════════════════════════════════════════════════

def resolve_settlement_events(governance_map, registry=None,
                              hostile_military_per_province=None,
                              ci_change_per_province=None,
                              emergency_action_provinces=None):
    # [canonical: settlement_layer §4.3 — fires all conditions from the Settlement Events table]
    # [M5_ASSUMPTION_FOUR: returns event records; caller applies state changes at arc boundary]
    #
    # governance_map: {sid: SettlementGovernance}
    # hostile_military_per_province: set of province IDs with adjacent hostile military
    # ci_change_per_province: {province_id: int delta} for Cathedral religious-event firing
    # emergency_action_provinces: set of provinces where emergency Domain Actions are pending
    reg = registry if registry is not None else m1.SETTLEMENT_REGISTRY
    hostile = hostile_military_per_province or set()
    ci_changes = ci_change_per_province or {}
    emergencies = emergency_action_provinces or set()

    events = []

    for sid, gov in governance_map.items():
        settlement = reg.get(sid)
        if settlement is None:
            continue
        province = settlement.territory_id

        # Famine (Prosperity 0) — Order -1 automatic
        # [canonical: settlement_layer §4.3 — "Prosperity 0 | Famine ... Order -1 automatic"]
        if gov.prosperity <= FAMINE_PROSPERITY_THRESHOLD:
            events.append(SettlementEvent(
                sid=sid,
                event_type='famine',
                severity='critical',
                immediate_effects={'order_delta': FAMINE_ORDER_PENALTY},
                description='Famine or economic collapse. Population leaving.',
            ))

        # Raid/Siege (Defense 0 + adjacent hostile)
        # [canonical: settlement_layer §4.3 — "Defense 0 + adjacent hostile military | Raid or siege"]
        if gov.defense <= DEFENSE_MIN and province in hostile:
            events.append(SettlementEvent(
                sid=sid,
                event_type='raid',
                severity='critical',
                immediate_effects={},  # mandatory scene; caller resolves
                description='Raid or siege. Mandatory scene if player is present.',
            ))

        # Revolt (Order 0)
        # [canonical: settlement_layer §4.3 — "Order 0 | Local revolt. Governor expelled unless garrison present"]
        if gov.order <= REVOLT_ORDER_THRESHOLD:
            suppressed = gov.garrison_present
            events.append(SettlementEvent(
                sid=sid,
                event_type='revolt',
                severity='critical' if not suppressed else 'normal',
                immediate_effects={'governor_expelled': not suppressed},
                suppressed_by_garrison=suppressed,
                description='Local revolt. Governor expelled unless garrison present.',
            ))

        # Flourishing (Order 5 + Prosperity 4+)
        # [canonical: settlement_layer §4.3 — "Order 5 + Prosperity 4+ | Flourishing ... +1 Disposition"]
        if (gov.order >= FLOURISHING_ORDER_THRESHOLD
                and gov.prosperity >= FLOURISHING_PROSPERITY_THRESHOLD):
            events.append(SettlementEvent(
                sid=sid,
                event_type='flourishing',
                severity='normal',
                immediate_effects={'disposition_delta_all_local_npcs': FLOURISHING_DISPOSITION_BONUS},
                description='Flourishing. Local festival, trade fair, or cultural event.',
            ))

        # Mine surplus (Mine type + Prosperity 3+)
        # [canonical: settlement_layer §4.3 — "Mine type + Prosperity 3+ | Resource surplus. Province Treasury +50/season"]
        if (settlement.settlement_type == 'Mine'
                and gov.prosperity >= MINE_SURPLUS_PROSPERITY_THRESHOLD):
            events.append(SettlementEvent(
                sid=sid,
                event_type='mine_surplus',
                severity='normal',
                immediate_effects={'province_treasury_delta': MINE_SURPLUS_TREASURY_DELTA},
                description='Resource surplus. Mine contributes to provincial treasury.',
            ))

        # Fortress garrison check (Fortress type + hostile military in province)
        # [canonical: settlement_layer §4.3 — "Fortress type + hostile military in province | Garrison mobilization. Defense check: Defense pool vs Ob 2"]
        if (settlement.settlement_type in ('Fortress', 'Fortress-City')
                and province in hostile):
            events.append(SettlementEvent(
                sid=sid,
                event_type='fortress_garrison_check',
                severity='critical',
                immediate_effects={
                    'defense_pool': gov.defense,
                    'ob': FORTRESS_DEFENSE_CHECK_OB,
                },
                description='Garrison mobilization. Defense check Ob 2.',
            ))

        # Cathedral religious event (Cathedral type + CV change in province)
        # [canonical: settlement_layer §4.3 — "Cathedral type + CV change in province | Religious event"]
        # Settlement type 'Cathedral-City' carries Cathedral religious building per M1.
        # CV change source: caller passes per-province CV delta map.
        cv_delta = ci_changes.get(province, 0)
        if (settlement.religious_building == m1.RB_CATHEDRAL and cv_delta != 0):
            events.append(SettlementEvent(
                sid=sid,
                event_type='religious_event',
                severity='normal',
                immediate_effects={'cv_direction': 'rising' if cv_delta > 0 else 'falling'},
                description='Religious event: sermon, ceremony, procession, or protest.',
            ))

        # Consensus Delay (RM-governed + emergency action in province)
        # [canonical: settlement_layer §4.3 — "RM-governed settlement, emergency action | Consensus Delay"]
        if gov.rm_governed and province in emergencies:
            events.append(SettlementEvent(
                sid=sid,
                event_type='consensus_delay',
                severity='normal',
                immediate_effects={
                    'delay_seasons': CONSENSUS_DELAY_SEASONS,
                    'waiver_mandate_cost': CONSENSUS_DELAY_WAIVER_MANDATE_COST,
                    'waiver_presence_cost': CONSENSUS_DELAY_WAIVER_PRESENCE_COST,
                },
                description='Emergency Domain Actions in RM settlements take +1 season to resolve.',
            ))

    return events


# ═══════════════════════════════════════════════════════════════════════════
# GOVERNANCE TRANSITION — §4.3 RM takes control
# ═══════════════════════════════════════════════════════════════════════════

def governance_transition_event(sid):
    # [canonical: settlement_layer §4.3 — "RM takes control of settlement | Governance Transition scene"]
    # Caller invokes when RM transitions to controlling a settlement; returns the 3-mode choice event.
    return SettlementEvent(
        sid=sid,
        event_type='governance_transition',
        severity='normal',
        immediate_effects={},
        choice_required=True,
        choice_options=GOVERNANCE_TRANSITION_MODES,
        description='RM takes control of settlement. Player or Vossen chooses transition mode.',
    )


def governance_transition_effects(mode):
    # [canonical: settlement_layer §4.3 — three transition modes with explicit effects]
    if mode == 'disestablishment':
        # "-1 Order for 2 seasons, then Accord growth +0.5/season; PT -1 immediate"
        return {
            'order_delta': -1,
            'order_decay_seasons': 2,
            'accord_growth_per_season': 0.5,
            'pt_delta': -1,
            'pt_delta_immediate': True,
        }
    elif mode == 'accommodation':
        # "no penalty, PT drops 0.5 only, standard Accord"
        return {
            'order_delta': 0,
            'pt_delta': -0.5,
            'pt_delta_immediate': True,
            'accord_growth_per_season': 0.0,
        }
    elif mode == 'transformation':
        # "4-season gradual conversion; no penalty during transition; PT -1 and Accord +0.5/season after completion"
        return {
            'order_delta': 0,
            'transition_seasons': 4,
            'pt_delta_after_completion': -1,
            'accord_growth_per_season_after_completion': 0.5,
        }
    else:
        raise ValueError(f"Unknown governance transition mode: {mode} (expected one of {GOVERNANCE_TRANSITION_MODES})")


# ═══════════════════════════════════════════════════════════════════════════
# CONVENIENCE — per-province governance summary
# ═══════════════════════════════════════════════════════════════════════════

def province_settlement_summary(province_id, governance_map, registry=None):
    # [canonical: derived — aggregates governance state for logging]
    reg = registry if registry is not None else m1.SETTLEMENT_REGISTRY
    settlements = m1.territory_settlements(province_id, reg)
    summary = {
        'province': province_id,
        'settlement_count': len(settlements),
        'mean_order': 0.0,
        'mean_prosperity': 0.0,
        'mean_defense': 0.0,
        'rm_presence_count': 0,
        'rm_resilience_ob_penalty': rm_cell_resilience(province_id, governance_map, reg),
        'accord_aggregate': aggregate_order_to_accord(province_id, governance_map, reg),
        'wealth_contribution': aggregate_prosperity_to_wealth(province_id, governance_map, reg),
        'mine_treasury_contribution': province_mine_treasury_contribution(province_id, governance_map, reg),
    }
    if settlements:
        orders, prosps, defs = [], [], []
        for s in settlements:
            gov = governance_map.get(s.sid)
            if gov is not None:
                orders.append(gov.order)
                prosps.append(gov.prosperity)
                defs.append(gov.defense)
                if gov.rm_presence:
                    summary['rm_presence_count'] += 1
        if orders:
            summary['mean_order'] = sum(orders) / len(orders)
            summary['mean_prosperity'] = sum(prosps) / len(prosps)
            summary['mean_defense'] = sum(defs) / len(defs)
    return summary
