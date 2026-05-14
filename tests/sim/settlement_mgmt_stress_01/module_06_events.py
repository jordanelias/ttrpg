# module_06_events.py — Settlement events, Thread operations, Local Actors
#
# Mode G Module six of settlement_mgmt_stress_01.
#
# Approach: BOTTOM-UP GRANULAR EMERGENT.
#
# Each event-trigger condition is a pure predicate on settlement state.
# Events do NOT know about each other. The full event-firing surface for
# a settlement at a given season is the set of predicates that evaluate
# to True against that settlement's current state. The Scene Slate at
# Priority four (Territorial) consumes the firing set.
#
# Emergence comes from chains: a Famine event mutates Order to drive a
# Revolt event next season; a Cathedral install (M4) shifts CV which fires
# a Religious-Event predicate; an RM-Takeover triggers the
# Governance-Transition scene which the player resolves via one of three
# canonical modes (Disestablishment / Accommodation / Transformation) —
# each mode mutates settlement state differently, and the next season's
# event-predicate sweep responds to that mutation.
#
# Module six does NOT pre-author event chains. It exposes:
#   - pure predicates (event-firing conditions)
#   - resolution handlers (player or NPC choice handlers)
#   - per-season event sweep over the registry
#   - the Templar interrupt action surface (canceling rival Domain Actions)
#   - the Inquisitor surveillance Concealment test (Thread practitioners)
#   - Local Actor generation + Disposition tracking
#
# Composition emerges from the season-by-season sweep, not from authored
# sequences.
#
# Encodes:
#   §4.1 Scene Slate Settlement Anchoring (travel cost rules)
#   §4.2 Subnational Faction Visibility (where + how each subnational
#        shows up in player-visible texture)
#   §4.3 Settlement Events (9 canonical event-trigger predicates +
#        resolution actions)
#   §4.4 Thread Operations at settlement scope (8 operation effects;
#        ±1-per-stat-per-season emergence-safety cap)
#   §4.5 Local Actors (per-settlement-type counts; Disposition drivers)
#
# Canonical source (full read this session):
#   designs/territory/settlement_layer_v30.md (§4.1, §4.2, §4.3, §4.4, §4.5)
#
# Out of scope (deferred):
#   - Scene Slate priority-band integration with player_agency_v30 §4.2 —
#     Module twelve (faction integration) wires Priority 4 entries
#   - Conviction reveal effect of Administer action — Module 5 surfaces the
#     flag; Module 7 (military) or Module 12 consumes it for NPC behavior
#   - Mass Battle resolution (settlement under raid/siege event) —
#     Module 7 (military granularity)
#   - Mandate spend + Presence-marker loss for Consensus-Delay waiver —
#     Module 12

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional, Tuple

from module_01_primitives import (
    Settlement, SettlementStats, by_id, STAT_MAX, STAT_MIN, REGISTRY,
)
from module_02_hierarchy import neighbors
from module_03_facilities import ActionResult
from module_04_church import (
    ChurchInfrastructure, ReligiousBuilding,
)
from module_05_governance import (
    GovernorState, SubnationalFaction, MANAGEMENT_EFFECTS,
)


# ── §4.1 Scene Slate Settlement Anchoring — travel costs ────────────────────

# [canonical: settlement_layer_v30 §4.1 —
#  "Moving between settlements in the same province costs no scene action"]
INTRA_PROVINCE_TRAVEL_SCENE_COST: int = 0
# [canonical: settlement_layer_v30 §4.1 —
#  "Moving between provinces costs 1 scene per province traversed"]
INTER_PROVINCE_TRAVEL_SCENE_COST_PER_PROVINCE: int = 1


def travel_scene_cost(
    from_settlement_id: str,
    to_settlement_id: str,
    provinces_traversed: int = 1,
) -> int:
    """§4.1 travel-cost. provinces_traversed >= 1 when crossing province
    boundary; 0 for intra-province moves."""
    if provinces_traversed == 0:
        return INTRA_PROVINCE_TRAVEL_SCENE_COST
    return provinces_traversed * INTER_PROVINCE_TRAVEL_SCENE_COST_PER_PROVINCE


# ── §4.2 Subnational visibility — which factions show up where ──────────────

# [canonical: settlement_layer_v30 §4.2 visibility table]
# Module 6 surfaces visibility *targets* (settlement types). Whether the
# subnational is ACTUALLY managing the settlement is M5's GovernorState
# territory. Visibility means "the player sees evidence of this faction
# when at this settlement type, IF the faction has any presence." Covert
# factions (Niflhel) require Investigation to reveal.
SUBNATIONAL_VISIBILITY_TYPES: Dict[SubnationalFaction, Tuple[str, ...]] = {
    SubnationalFaction.MINISTRY:     ('Seat', 'City'),
    SubnationalFaction.GUILDS:       ('City', 'Port', 'Mine'),   # Market omitted per F11
    SubnationalFaction.NIFLHEL:      ('Seat', 'City', 'Town', 'Fortress', 'Port',
                                       'Cathedral', 'Mine', 'Outpost'),  # "Any settlement (covert)"
    SubnationalFaction.RM:           ('Town', 'Outpost'),
    SubnationalFaction.LOEWENRITTER: ('Fortress',),
    SubnationalFaction.WARDENS:      ('Outpost',),
    SubnationalFaction.CHURCH:       ('Cathedral',),
}


# ── §4.3 atomic event-trigger predicates ────────────────────────────────────
# Each is a pure function (Settlement, SettlementStats, optional context) -> bool.
# No predicate depends on another predicate's state. Composition emerges
# in the per-season sweep.

class SettlementEvent(Enum):
    """Enumerated set of §4.3 event types. Each maps to a predicate +
    resolution handler."""
    FAMINE_ECONOMIC_COLLAPSE   = 'famine_economic_collapse'
    RAID_OR_SIEGE              = 'raid_or_siege'
    LOCAL_REVOLT               = 'local_revolt'
    FLOURISHING_FESTIVAL       = 'flourishing_festival'
    GOVERNANCE_TRANSITION_RM   = 'governance_transition_rm'
    CONSENSUS_DELAY            = 'consensus_delay'
    RELIGIOUS_EVENT            = 'religious_event'
    MINE_RESOURCE_SURPLUS      = 'mine_resource_surplus'
    FORTRESS_GARRISON_MOBILIZE = 'fortress_garrison_mobilize'


# §4.3 Famine threshold (Prosperity 0)
# [canonical: settlement_layer_v30 §4.3 —
#  "Prosperity 0 | Famine or economic collapse. ... Order −1 automatic."]
FAMINE_PROSPERITY_THRESHOLD: int = 0
FAMINE_ORDER_AUTO_PENALTY: int = 1   # subtracted from Order automatically


def predicate_famine(stats: SettlementStats) -> bool:
    """§4.3 Famine fires when Prosperity == 0."""
    return stats.prosperity == FAMINE_PROSPERITY_THRESHOLD


# §4.3 Raid-or-Siege threshold (Defense 0 + adjacent hostile military)
# [canonical: settlement_layer_v30 §4.3 —
#  "Defense 0 + adjacent hostile military | Raid or siege."]
RAID_DEFENSE_THRESHOLD: int = 0


def predicate_raid_or_siege(stats: SettlementStats, adjacent_hostile: bool) -> bool:
    """§4.3 Raid/Siege fires when Defense == 0 AND adjacent hostile military
    is present. `adjacent_hostile` is supplied by upstream military layer."""
    return stats.defense == RAID_DEFENSE_THRESHOLD and adjacent_hostile


# §4.3 Local revolt threshold (Order 0)
# [canonical: settlement_layer_v30 §4.3 —
#  "Order 0 | Local revolt ... Governor expelled unless garrison present."]
REVOLT_ORDER_THRESHOLD: int = 0


def predicate_local_revolt(stats: SettlementStats) -> bool:
    """§4.3 Local revolt fires when Order == 0."""
    return stats.order == REVOLT_ORDER_THRESHOLD


# §4.3 Flourishing thresholds (Order 5 + Prosperity ≥ 4)
# [canonical: settlement_layer_v30 §4.3 —
#  "Order 5 + Prosperity 4+ | Flourishing. Local festival ... +1 Disposition"]
FLOURISHING_ORDER_THRESHOLD: int = 5
FLOURISHING_PROSPERITY_THRESHOLD: int = 4
FLOURISHING_DISPOSITION_BONUS: int = 1


def predicate_flourishing(stats: SettlementStats) -> bool:
    """§4.3 Flourishing fires when Order == 5 AND Prosperity ≥ 4."""
    return (stats.order >= FLOURISHING_ORDER_THRESHOLD
            and stats.prosperity >= FLOURISHING_PROSPERITY_THRESHOLD)


# §4.3 Religious event — settlement is Cathedral type + CV changed
def predicate_religious_event(
    settlement: Settlement,
    cv_changed_this_season: bool,
) -> bool:
    """§4.3 Religious event fires when settlement type is Cathedral AND
    province-level CV changed this season."""
    # [canonical: §4.3 — "Cathedral type + CV change in province"]
    return settlement.type == 'Cathedral' and cv_changed_this_season


# §4.3 Mine resource surplus — Mine type + Prosperity ≥ 3
# [canonical: settlement_layer_v30 §4.3 —
#  "Mine type + Prosperity 3+ | Resource surplus. Province Treasury +50/season"]
MINE_SURPLUS_PROSPERITY_THRESHOLD: int = 3
MINE_SURPLUS_TREASURY_PER_SEASON: int = 50


def predicate_mine_surplus(settlement: Settlement, stats: SettlementStats) -> bool:
    """§4.3 Mine resource surplus fires when settlement type is Mine AND
    Prosperity ≥ MINE_SURPLUS_PROSPERITY_THRESHOLD."""
    return (settlement.type == 'Mine'
            and stats.prosperity >= MINE_SURPLUS_PROSPERITY_THRESHOLD)


# §4.3 Fortress garrison mobilization — Fortress + hostile in province
# [canonical: settlement_layer_v30 §4.3 —
#  "Fortress type + hostile military in province | Garrison mobilization.
#  Defense check: Defense pool vs Ob 2."]
FORTRESS_MOBILIZE_DEFENSE_OB: int = 2


def predicate_fortress_mobilize(
    settlement: Settlement,
    hostile_in_province: bool,
) -> bool:
    """§4.3 Fortress garrison mobilization fires when settlement type is
    Fortress AND hostile military in province."""
    return settlement.type == 'Fortress' and hostile_in_province


# §4.3 Governance Transition (RM takes control)
# Triggered by an EXTERNAL event (RM acquires governor); not a state
# predicate but a discrete trigger. Module 6 exposes the trigger function.

# §4.3 Consensus Delay — RM-governed settlement, emergency action attempted
# Same: triggered by an external action attempt, not a state predicate.
# Module 6 exposes the trigger function.


# ── §4.3 event sweep — per-season composition ───────────────────────────────

@dataclass(frozen=True)
class FiredEvent:
    """A single event firing in a single settlement at a single season.
    Carries the event type + the settlement ID. Multiple FiredEvents per
    settlement per season are possible (a Mine-type at Prosperity 3 facing
    a hostile force can fire both Mine-Resource-Surplus AND Fortress-
    Mobilize if it's also somehow Fortress-typed; in practice mutually
    exclusive type fields make this rare, but Famine + Religious can co-fire
    if a Cathedral hits Prosperity 0)."""
    settlement_id: str
    event: SettlementEvent


def sweep_season_events(
    state_by_id: Dict[str, SettlementStats],
    adjacent_hostile_by_id: Optional[Dict[str, bool]] = None,
    hostile_in_province_by_id: Optional[Dict[str, bool]] = None,
    cv_changed_by_province: Optional[Dict[str, bool]] = None,
) -> List[FiredEvent]:
    """Per-season event sweep over the full registry.

    Bottom-up: each predicate evaluates independently against each
    settlement. Emergence comes from the cumulative list and from the
    NEXT season's state-update (which is downstream of these events'
    resolutions).

    `state_by_id` is the mutable per-settlement state map.
    Optional dicts carry context the predicates need (hostile presence,
    province CV change). Default empty = no upstream context = those
    predicates evaluate False.
    """
    fired: List[FiredEvent] = []
    adj_hostile = adjacent_hostile_by_id or {}
    prov_hostile = hostile_in_province_by_id or {}
    cv_changed = cv_changed_by_province or {}

    for s in REGISTRY:
        stats = state_by_id.get(s.id)
        if stats is None:
            continue   # settlement has no tracked state this season
        sid = s.id
        if predicate_famine(stats):
            fired.append(FiredEvent(sid, SettlementEvent.FAMINE_ECONOMIC_COLLAPSE))
        if predicate_raid_or_siege(stats, adj_hostile.get(sid, False)):
            fired.append(FiredEvent(sid, SettlementEvent.RAID_OR_SIEGE))
        if predicate_local_revolt(stats):
            fired.append(FiredEvent(sid, SettlementEvent.LOCAL_REVOLT))
        if predicate_flourishing(stats):
            fired.append(FiredEvent(sid, SettlementEvent.FLOURISHING_FESTIVAL))
        if predicate_religious_event(s, cv_changed.get(s.province, False)):
            fired.append(FiredEvent(sid, SettlementEvent.RELIGIOUS_EVENT))
        if predicate_mine_surplus(s, stats):
            fired.append(FiredEvent(sid, SettlementEvent.MINE_RESOURCE_SURPLUS))
        if predicate_fortress_mobilize(s, prov_hostile.get(sid, False)):
            fired.append(FiredEvent(sid, SettlementEvent.FORTRESS_GARRISON_MOBILIZE))

    return fired


# ── §4.3 event resolution handlers ──────────────────────────────────────────

def resolve_famine(stats: SettlementStats) -> ActionResult:
    """§4.3 Famine resolution — automatic Order -1.
    [canonical: §4.3 — 'Order −1 automatic']
    """
    new_order = max(STAT_MIN, stats.order - FAMINE_ORDER_AUTO_PENALTY)
    delta = new_order - stats.order
    stats.order = new_order
    return ActionResult(
        success=True,
        reason='famine_order_decrement',
        state_mutated=(delta != 0),
        faction_standing_delta=-1,   # famine signals governance failure
        renown_delta=-1,
    )


def resolve_local_revolt(
    stats: SettlementStats,
    governor_state: GovernorState,
    garrison_present: bool,
) -> ActionResult:
    """§4.3 Local revolt resolution — Governor expelled UNLESS garrison
    present.
    [canonical: §4.3 — 'Governor expelled unless garrison present']
    """
    if garrison_present:
        return ActionResult(
            success=True,
            reason='revolt_contained_by_garrison',
            state_mutated=False,
            faction_standing_delta=-1,
            renown_delta=0,
        )
    # Governor expelled
    governor_state.has_governor = False
    governor_state.governor_standing = 0
    governor_state.managing_subnational = None
    return ActionResult(
        success=True,
        reason='revolt_expelled_governor',
        state_mutated=True,
        faction_standing_delta=-2,
        renown_delta=-2,
    )


def resolve_flourishing(stats: SettlementStats) -> ActionResult:
    """§4.3 Flourishing resolution — +1 Disposition with all local NPCs.
    Local Actor Disposition is tracked separately (see LocalActor below);
    this handler returns the structural signal that triggers the bonus.
    """
    return ActionResult(
        success=True,
        reason='flourishing_festival',
        state_mutated=False,   # stat-level no change; Disposition is separate
        faction_standing_delta=+1,
        renown_delta=+1,
    )


# §4.3 RM Governance Transition — three modes
class GovernanceTransitionMode(Enum):
    """§4.3 RM Governance Transition — three canonical resolution modes."""
    DISESTABLISHMENT = 'disestablishment'
    ACCOMMODATION    = 'accommodation'
    TRANSFORMATION   = 'transformation'


# [canonical: settlement_layer_v30 §4.3 — Disestablishment mode —
#  "−1 Order for 2 seasons, then Accord growth +0.5/season; PT −1 immediate"]
DISESTABLISHMENT_ORDER_PENALTY_PER_SEASON: int = 1
DISESTABLISHMENT_PENALTY_SEASON_COUNT: int = 2
DISESTABLISHMENT_PT_IMMEDIATE_COST: int = 1   # half-units? canon says "−1" not "−0.5"
DISESTABLISHMENT_ACCORD_HALF_PER_SEASON_POST: int = 1   # +0.5/season encoded as half-units

# [canonical: settlement_layer_v30 §4.3 — Accommodation mode —
#  "no penalty, PT drops 0.5 only, standard Accord"]
ACCOMMODATION_PT_HALF_COST: int = 1   # 0.5 PT = 1 half-unit (per M4 encoding)

# [canonical: settlement_layer_v30 §4.3 — Transformation mode —
#  "4-season gradual conversion; no penalty during transition; PT −1 and
#  Accord +0.5/season after completion"]
TRANSFORMATION_DURATION_SEASONS: int = 4
TRANSFORMATION_PT_POST_COST: int = 1
TRANSFORMATION_ACCORD_HALF_PER_SEASON_POST: int = 1


@dataclass
class GovernanceTransitionState:
    """Per-settlement state tracking a Disestablishment or Transformation
    mode in progress. Accommodation is one-shot — no state retention
    needed beyond the immediate effects."""
    settlement_id: str
    mode: GovernanceTransitionMode
    seasons_remaining_in_penalty: int = 0   # Disestablishment: 2 → 1 → 0
    seasons_remaining_in_transition: int = 0  # Transformation: 4 → ... → 0
    accord_growth_active: bool = False


def resolve_rm_governance_transition(
    stats: SettlementStats,
    mode: GovernanceTransitionMode,
) -> Tuple[ActionResult, Optional[GovernanceTransitionState]]:
    """§4.3 RM Governance Transition — player chooses one of three modes.
    Returns (immediate action result, optional persistent state object).

    Persistent state is returned for Disestablishment and Transformation
    (their effects span multiple seasons); None for Accommodation (one-shot).
    """
    if mode == GovernanceTransitionMode.DISESTABLISHMENT:
        # Immediate: Order -1 (next 2 seasons handled by state); PT -1
        return (
            ActionResult(
                success=True,
                reason='governance_transition_disestablishment',
                state_mutated=False,   # state-level pending is the new tracker object
                faction_standing_delta=-1,
                renown_delta=-1,
            ),
            GovernanceTransitionState(
                settlement_id='',   # caller fills in
                mode=mode,
                seasons_remaining_in_penalty=DISESTABLISHMENT_PENALTY_SEASON_COUNT,
                accord_growth_active=False,   # activates after penalty period
            ),
        )
    if mode == GovernanceTransitionMode.ACCOMMODATION:
        # Immediate: 0.5 PT cost; no Order penalty; standard Accord
        return (
            ActionResult(
                success=True,
                reason='governance_transition_accommodation',
                state_mutated=False,
                faction_standing_delta=0,
                renown_delta=0,
            ),
            None,
        )
    if mode == GovernanceTransitionMode.TRANSFORMATION:
        # No immediate penalty; 4-season transition, then PT -1 + Accord growth
        return (
            ActionResult(
                success=True,
                reason='governance_transition_transformation',
                state_mutated=False,
                faction_standing_delta=0,
                renown_delta=+1,   # patient governance gains renown
            ),
            GovernanceTransitionState(
                settlement_id='',
                mode=mode,
                seasons_remaining_in_transition=TRANSFORMATION_DURATION_SEASONS,
                accord_growth_active=False,
            ),
        )
    raise ValueError(f'unknown mode: {mode}')


def advance_transition_state(
    state: GovernanceTransitionState,
    stats: SettlementStats,
) -> None:
    # Per-season advance for an in-flight Governance Transition (§4.3 spec).
    # Called by the Module-nine timeline layer at each season's Accounting tick.
    if state.mode == GovernanceTransitionMode.DISESTABLISHMENT:
        if state.seasons_remaining_in_penalty > 0:
            # Apply -1 Order this season
            new_order = max(STAT_MIN, stats.order - DISESTABLISHMENT_ORDER_PENALTY_PER_SEASON)
            stats.order = new_order
            state.seasons_remaining_in_penalty -= 1
            if state.seasons_remaining_in_penalty == 0:
                state.accord_growth_active = True
        # accord_growth_active period continues indefinitely until canonical
        # closure (Module 12 territory). Provincial Accord +0.5/season
        # accrues there.
        return
    if state.mode == GovernanceTransitionMode.TRANSFORMATION:
        if state.seasons_remaining_in_transition > 0:
            state.seasons_remaining_in_transition -= 1
            if state.seasons_remaining_in_transition == 0:
                # Transition completes — apply post-completion costs/bonuses
                # Module 12 binds the PT -1 to faction Piety; Accord growth
                # active for Module 12 timeline consumer.
                state.accord_growth_active = True
        return


# §4.3 Consensus Delay — RM-governed settlement, emergency action
# [canonical: settlement_layer_v30 §4.3 —
#  "Emergency Domain Actions (Muster, Fortify, Emergency Diplomacy) in RM
#  settlements take +1 season to resolve. Waivable: RM leader spends 1
#  Mandate + loses 1 Presence marker in that province"]
CONSENSUS_DELAY_SEASONS: int = 1
CONSENSUS_DELAY_WAIVER_MANDATE_COST: int = 1
CONSENSUS_DELAY_WAIVER_PRESENCE_LOSS: int = 1

EMERGENCY_ACTIONS_AFFECTED_BY_DELAY: Tuple[str, ...] = (
    'Muster', 'Fortify', 'Emergency Diplomacy',
)


def compute_consensus_delay(
    action_name: str,
    rm_governs_settlement: bool,
    waiver_used: bool = False,
) -> int:
    """§4.3 Consensus Delay computation.
    Returns the additional season-delay (0 or CONSENSUS_DELAY_SEASONS).
    """
    if not rm_governs_settlement:
        return 0
    if action_name not in EMERGENCY_ACTIONS_AFFECTED_BY_DELAY:
        return 0
    if waiver_used:
        return 0
    return CONSENSUS_DELAY_SEASONS


# ── §4.4 Thread operations at settlement scope ──────────────────────────────

# [canonical: settlement_layer_v30 §4.4 —
#  "Cap: ±1 per settlement stat per season from Thread operations."]
THREAD_OP_PER_STAT_PER_SEASON_CAP: int = 1


class ThreadOperation(Enum):
    """§4.4 Thread operations at Relational+ scope."""
    WEAVING                = 'weaving'
    PULLING                = 'pulling'
    PAST_ORIENTED_PULLING  = 'past_oriented_pulling'
    DISSOLUTION            = 'dissolution'
    MENDING                = 'mending'
    COMMUNITY_ORGANIZING   = 'community_organizing'
    LOCK                   = 'lock'


@dataclass(frozen=True)
class ThreadOpEffect:
    """§4.4 effects table. Each operation has effects on success AND failure
    (some have effects only on one side)."""
    success_order_delta:       int = 0
    success_defense_delta:     int = 0
    success_prosperity_delta:  int = 0
    failure_order_delta:       int = 0
    failure_defense_delta:     int = 0
    failure_prosperity_delta:  int = 0


# [canonical: settlement_layer_v30 §4.4 Thread operations table]
THREAD_OP_EFFECTS: Dict[ThreadOperation, ThreadOpEffect] = {
    # Weaving — success: Order +1; failure: no effect
    ThreadOperation.WEAVING:               ThreadOpEffect(success_order_delta=+1),
    # Pulling — success: no positive; failure: Order -1
    ThreadOperation.PULLING:               ThreadOpEffect(failure_order_delta=-1),
    # Past-Oriented Pulling — success: no positive; failure: Prosperity -1
    ThreadOperation.PAST_ORIENTED_PULLING: ThreadOpEffect(failure_prosperity_delta=-1),
    # Dissolution — success: no positive; failure: Defense -1 AND Order -1
    ThreadOperation.DISSOLUTION:           ThreadOpEffect(failure_defense_delta=-1,
                                                          failure_order_delta=-1),
    # Mending — success: Prosperity +1; failure: no effect
    ThreadOperation.MENDING:               ThreadOpEffect(success_prosperity_delta=+1),
    # Community Organizing — success: Order +1 AND Prosperity +1 (only if
    # PT ≤ 2 in province); failure: no effect
    ThreadOperation.COMMUNITY_ORGANIZING:  ThreadOpEffect(success_order_delta=+1,
                                                          success_prosperity_delta=+1),
    # Lock — success: Defense +1; failure: no effect
    ThreadOperation.LOCK:                  ThreadOpEffect(success_defense_delta=+1),
}


def apply_thread_op(
    op: ThreadOperation,
    stats: SettlementStats,
    succeeded: bool,
    delta_already_applied_this_season: Dict[str, int],
    province_pt: int = 0,
) -> ActionResult:
    """§4.4 Apply a Thread operation result at settlement scope.

    Honors the §4.4 cap: ±1 per stat per season. The caller passes
    `delta_already_applied_this_season` as a {stat_name: cumulative_delta}
    dict; this function refuses to apply a delta that would push the
    cumulative beyond ±THREAD_OP_PER_STAT_PER_SEASON_CAP.

    For Community Organizing, the success effect only fires if
    province_pt <= RM_NATURAL_PT_THRESHOLD (= 2) per §4.4.
    """
    from module_05_governance import RM_NATURAL_PT_THRESHOLD

    effect = THREAD_OP_EFFECTS[op]

    # Special case for Community Organizing — gated by province PT
    if op == ThreadOperation.COMMUNITY_ORGANIZING and succeeded:
        if province_pt > RM_NATURAL_PT_THRESHOLD:
            return ActionResult(
                success=False,
                reason='community_organizing_blocked_high_pt',
                state_mutated=False,
            )

    if succeeded:
        deltas = {
            'order':       effect.success_order_delta,
            'defense':     effect.success_defense_delta,
            'prosperity':  effect.success_prosperity_delta,
        }
    else:
        deltas = {
            'order':       effect.failure_order_delta,
            'defense':     effect.failure_defense_delta,
            'prosperity':  effect.failure_prosperity_delta,
        }

    mutated = False
    capped_stats: List[str] = []
    for stat_name, delta in deltas.items():
        if delta == 0:
            continue
        # Check the cap
        cumulative = delta_already_applied_this_season.get(stat_name, 0)
        proposed_cumulative = cumulative + delta
        # Cap is ±THREAD_OP_PER_STAT_PER_SEASON_CAP
        if abs(proposed_cumulative) > THREAD_OP_PER_STAT_PER_SEASON_CAP:
            capped_stats.append(stat_name)
            continue
        # Apply delta to stats with clamp at [STAT_MIN, STAT_MAX]
        current_value = getattr(stats, stat_name)
        new_value = max(STAT_MIN, min(STAT_MAX, current_value + delta))
        if new_value != current_value:
            setattr(stats, stat_name, new_value)
            mutated = True
        delta_already_applied_this_season[stat_name] = proposed_cumulative

    return ActionResult(
        success=succeeded,
        reason=(f'thread_op_{op.value}_capped_{",".join(capped_stats)}'
                if capped_stats else f'thread_op_{op.value}'),
        state_mutated=mutated,
        faction_standing_delta=(+1 if succeeded and mutated else
                                -1 if not succeeded and mutated else 0),
        renown_delta=0,   # Thread ops are not visible work; no renown
    )


# ── §1.5 Axis 3 Inquisitor surveillance — Concealment test ─────────────────

# [canonical: settlement_layer_v30 §1.5 Axis 3 —
#  "Surveillance Zone: Thread practitioners make Concealment test each season"]
INQUISITOR_SURVEILLANCE_CONCEALMENT_FIRES_EVERY_SEASON: bool = True


def inquisitor_concealment_test_required(
    infra: ChurchInfrastructure,
    is_thread_practitioner: bool,
) -> bool:
    """§1.5 Axis 3 — Thread practitioners in Inquisitor-surveilled
    settlements must make a Concealment test each season."""
    return infra.inquisitor_base and is_thread_practitioner


# ── §1.5 Axis 2 Templar interrupt — action surface ──────────────────────────

@dataclass(frozen=True)
class TemplarInterruptResult:
    """§1.5 Axis 2 — Church interrupts rival Domain Action.
    On apply: rival's Ob is increased by TEMPLAR_INTERRUPT_OB_DELTA; Church
    spends TEMPLAR_INTERRUPT_CI_COST CI."""
    applied: bool
    rival_ob_delta: int
    ci_spent: int


def apply_templar_interrupt(
    infra: ChurchInfrastructure,
    rival_action_in_progress: bool,
    church_ci_available: int,
) -> TemplarInterruptResult:
    """§1.5 Axis 2 — Templar interrupts rival Domain Action.
    Requires: Templar Station present in settlement; rival action in progress;
    Church has ≥ TEMPLAR_INTERRUPT_CI_COST CI to spend.
    """
    from module_04_church import TEMPLAR_INTERRUPT_OB_DELTA, TEMPLAR_INTERRUPT_CI_COST
    if not infra.templar_station:
        return TemplarInterruptResult(applied=False, rival_ob_delta=0, ci_spent=0)
    if not rival_action_in_progress:
        return TemplarInterruptResult(applied=False, rival_ob_delta=0, ci_spent=0)
    if church_ci_available < TEMPLAR_INTERRUPT_CI_COST:
        return TemplarInterruptResult(applied=False, rival_ob_delta=0, ci_spent=0)
    return TemplarInterruptResult(
        applied=True,
        rival_ob_delta=TEMPLAR_INTERRUPT_OB_DELTA,
        ci_spent=TEMPLAR_INTERRUPT_CI_COST,
    )


# ── §3.3 Niflhel detection action ───────────────────────────────────────────

def attempt_niflhel_detection(
    investigation_evidence_track: int,
) -> bool:
    """§3.3 Niflhel detection — Investigation Evidence Track ≥
    NIFLHEL_DETECTION_EVIDENCE_THRESHOLD reveals Niflhel presence."""
    from module_05_governance import NIFLHEL_DETECTION_EVIDENCE_THRESHOLD
    return investigation_evidence_track >= NIFLHEL_DETECTION_EVIDENCE_THRESHOLD


# ── §4.5 Local Actors ───────────────────────────────────────────────────────

# [canonical: settlement_layer_v30 §4.5 — Local Actor count by settlement type]
LOCAL_ACTOR_COUNT_BY_TYPE: Dict[str, int] = {
    'Seat':      2,
    'City':      2,
    'Town':      1,
    'Fortress':  1,
    'Port':      2,
    'Cathedral': 1,
    'Mine':      1,
    'Outpost':   0,
}


# [FINDING F12] §4.5 Local Actor table omits §2.1 extra types (Village,
# Fortress-City, Cathedral-City). Same gap pattern as F1/F7/F10/F11.
# Module 6 surfaces the gap — local_actor_count() returns None for extras,
# preventing silent-zero. Provisional sim-side mapping below.
PROVISIONAL_EXTRA_TYPE_ACTOR_COUNT: Dict[str, int] = {
    'Village':         1,   # Town-equivalent (smallest-canonical-analogue)
    'Fortress-City':   2,   # composite Fortress + City -> sum or max
    'Cathedral-City':  2,   # composite Cathedral + Seat -> Seat-equivalent
}


# [FINDING F13] §4.5 prose states "Total: ~45-50 across 36 settlements".
# Two errors:
# 1) "36 settlements" is the pre-PP-rebuild count. Post-rebuild canonical
#    count is 37 (35 Kingdom + Himmelenger + Schoenland) per §2.1 summary.
# 2) Computing the canonical-eight per-type counts × actual registry shows
#    only 25 Local Actors land via the §4.5 table (because the registry
#    has no settlements of types Port, Cathedral, Mine, or Outpost
#    standalone — those types were folded into composite types or
#    sub-features by PP-rebuild). The "~45-50" total appears to be a
#    pre-PP-rebuild estimate.
# Module 6 documents both errors. Editorial decision needed: refresh
# §4.5 actor counts to match the post-rebuild §2.1 registry.

# Worked value: actors via canonical-eight types only
# [canonical: derived sum from §4.5 table × §2.1 registry counts]
ACTORS_FROM_CANONICAL_EIGHT_ONLY: int = 25


def local_actor_count(settlement: Settlement) -> Optional[int]:
    """§4.5 Local Actor count for a settlement.
    Returns the canonical count for §1.2 canonical-eight types;
    returns None for §2.1 extra types (Village / Fortress-City / Cathedral-City)
    per F12. Caller may fall back to PROVISIONAL_EXTRA_TYPE_ACTOR_COUNT."""
    return LOCAL_ACTOR_COUNT_BY_TYPE.get(settlement.type)


def effective_local_actor_count(settlement: Settlement) -> int:
    """Sim-side effective count using provisional fallback for extras."""
    direct = local_actor_count(settlement)
    if direct is not None:
        return direct
    return PROVISIONAL_EXTRA_TYPE_ACTOR_COUNT.get(settlement.type, 0)


@dataclass
class LocalActor:
    """§4.5 Local Actor profile."""
    settlement_id: str
    name: str
    role: str                       # Elder/Magistrate/Merchant/Priest/etc.
    conviction: str
    disposition_by_party: Dict[str, int] = field(default_factory=dict)
    # starting +1 toward governor, 0 toward all others per §4.5


# Local Actor Disposition drivers from §4.5
# [canonical: settlement_layer_v30 §4.5 Disposition drivers]
DISPOSITION_DRIVER_GOVERNS_ORDER_IMPROVES: int = +1
DISPOSITION_DRIVER_ORDER_DECLINES: int = -1
DISPOSITION_DRIVER_SPONSOR_EVENT: int = +1
DISPOSITION_DRIVER_PUBLIC_COMBAT: int = -2
DISPOSITION_DRIVER_DEFEND_FROM_INVASION: int = +2
DISPOSITION_DRIVER_FULFILL_CONVICTION: int = +1
# "Settlement changes controller: reset to 0" — handled by reset_disposition_on_controller_change


def adjust_disposition(
    actor: LocalActor,
    party: str,
    driver: str,
) -> int:
    """Apply a §4.5 Disposition driver. Returns the new disposition value."""
    driver_map = {
        'governs_order_improves': DISPOSITION_DRIVER_GOVERNS_ORDER_IMPROVES,
        'order_declines':         DISPOSITION_DRIVER_ORDER_DECLINES,
        'sponsor_event':          DISPOSITION_DRIVER_SPONSOR_EVENT,
        'public_combat':          DISPOSITION_DRIVER_PUBLIC_COMBAT,
        'defend_invasion':        DISPOSITION_DRIVER_DEFEND_FROM_INVASION,
        'fulfill_conviction':     DISPOSITION_DRIVER_FULFILL_CONVICTION,
    }
    if driver not in driver_map:
        raise ValueError(f'unknown driver: {driver}')
    current = actor.disposition_by_party.get(party, 0)
    new_value = current + driver_map[driver]
    actor.disposition_by_party[party] = new_value
    return new_value


def reset_disposition_on_controller_change(actor: LocalActor) -> None:
    """§4.5: 'Settlement changes controller: reset to 0'."""
    actor.disposition_by_party = {}


# §4.5 Stage 2->3 recruitment threshold
# [canonical: settlement_layer_v30 §4.5 —
#  "Recruitment pool for faction emergence (Stage 2→3 at Disposition +3)"]
FACTION_EMERGENCE_DISPOSITION_THRESHOLD: int = 3


def is_recruitment_candidate(actor: LocalActor, party: str) -> bool:
    """§4.5 — Local Actor is a recruitment candidate for `party` if
    Disposition >= FACTION_EMERGENCE_DISPOSITION_THRESHOLD."""
    return actor.disposition_by_party.get(party, 0) >= FACTION_EMERGENCE_DISPOSITION_THRESHOLD


# ── Isolation tests ─────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — travel cost intra-province == 0
    r['T1_travel_intra_province_free'] = (
        'PASS' if travel_scene_cost('S-001', 'S-002', 0) == 0 else 'FAIL'
    )

    # T2 — travel cost inter-province == 1 per province
    # [canonical: §4.1 — 1 scene per province traversed]
    expected_inter_province_cost = 1
    r['T2_travel_inter_province_1'] = (
        'PASS' if travel_scene_cost('S-001', 'S-004', 1) == expected_inter_province_cost
        else 'FAIL'
    )

    # T3 — 3-province traversal == 3 scenes
    # [canonical: §4.1 — 1 scene per province traversed]
    expected_three_province_cost = 3
    r['T3_travel_three_provinces'] = (
        'PASS' if travel_scene_cost('S-001', 'S-031', 3) == expected_three_province_cost
        else 'FAIL'
    )

    # T4 — Famine predicate fires at Prosperity 0
    stats_famine = SettlementStats(prosperity=0, defense=2, order=3)
    r['T4_famine_at_prosperity_0'] = (
        'PASS' if predicate_famine(stats_famine) else 'FAIL'
    )

    # T5 — Famine predicate negative at Prosperity 1
    stats_no_famine = SettlementStats(prosperity=1, defense=2, order=3)
    r['T5_famine_negative_at_prosperity_1'] = (
        'PASS' if not predicate_famine(stats_no_famine) else 'FAIL'
    )

    # T6 — Local revolt predicate fires at Order 0
    stats_revolt = SettlementStats(prosperity=2, defense=2, order=0)
    r['T6_revolt_at_order_0'] = (
        'PASS' if predicate_local_revolt(stats_revolt) else 'FAIL'
    )

    # T7 — Flourishing predicate requires BOTH Order 5 AND Prosperity ≥ 4
    stats_flourish = SettlementStats(prosperity=4, defense=2, order=5)
    stats_no_flourish_low_pros = SettlementStats(prosperity=3, defense=2, order=5)
    stats_no_flourish_low_order = SettlementStats(prosperity=4, defense=2, order=4)
    ok = (predicate_flourishing(stats_flourish)
          and not predicate_flourishing(stats_no_flourish_low_pros)
          and not predicate_flourishing(stats_no_flourish_low_order))
    r['T7_flourishing_compound_predicate'] = 'PASS' if ok else 'FAIL'

    # T8 — Mine surplus predicate requires Mine type AND Prosperity ≥ 3
    # Note: no settlement in registry has type 'Mine' post-rebuild
    # (per F12 — Mine is in §1.2 canonical eight but is not in §2.1 actually).
    # Test via synthetic Settlement.
    fake_mine = Settlement(id='S-XXX', name='TestMine', type='Mine',
                           province='Test', duchy='Test', role='test')
    stats_high_pros = SettlementStats(prosperity=3, defense=1, order=2)
    stats_low_pros = SettlementStats(prosperity=2, defense=1, order=2)
    ok = (predicate_mine_surplus(fake_mine, stats_high_pros)
          and not predicate_mine_surplus(fake_mine, stats_low_pros))
    r['T8_mine_surplus_predicate'] = 'PASS' if ok else 'FAIL'

    # T9 — Raid/Siege predicate: Defense 0 + adjacent hostile
    stats_raid = SettlementStats(prosperity=2, defense=0, order=3)
    ok = (predicate_raid_or_siege(stats_raid, adjacent_hostile=True)
          and not predicate_raid_or_siege(stats_raid, adjacent_hostile=False))
    r['T9_raid_predicate_requires_both'] = 'PASS' if ok else 'FAIL'

    # T10 — Sweep over registry produces multiple firings emergent from
    # mixed state without authoring
    state_by_id = {
        'S-001': SettlementStats(prosperity=0, defense=2, order=3),  # famine
        'S-002': SettlementStats(prosperity=4, defense=2, order=5),  # flourishing
        'S-003': SettlementStats(prosperity=2, defense=0, order=2),  # raid (with adjacent)
        'S-004': SettlementStats(prosperity=2, defense=2, order=0),  # revolt
    }
    adj_hostile = {'S-003': True}
    fired = sweep_season_events(state_by_id, adjacent_hostile_by_id=adj_hostile)
    event_types_fired = {fe.event for fe in fired}
    ok = (SettlementEvent.FAMINE_ECONOMIC_COLLAPSE in event_types_fired
          and SettlementEvent.FLOURISHING_FESTIVAL in event_types_fired
          and SettlementEvent.RAID_OR_SIEGE in event_types_fired
          and SettlementEvent.LOCAL_REVOLT in event_types_fired)
    r['T10_sweep_emergent_multi_firing'] = (
        'PASS' if ok else f'FAIL ({event_types_fired})'
    )

    # T11 — Famine resolution applies Order -1 automatically
    stats_famine_resolve = SettlementStats(prosperity=0, defense=2, order=3)
    result = resolve_famine(stats_famine_resolve)
    # [canonical: §4.3 Famine — "Order −1 automatic"]
    expected_post_famine_order = 2
    r['T11_famine_auto_order_decrement'] = (
        'PASS' if result.success and stats_famine_resolve.order == expected_post_famine_order
        else f'FAIL ({result}, order={stats_famine_resolve.order})'
    )

    # T12 — Famine order clamps at STAT_MIN
    stats_already_zero = SettlementStats(prosperity=0, defense=2, order=0)
    result = resolve_famine(stats_already_zero)
    r['T12_famine_clamps_at_zero'] = (
        'PASS' if stats_already_zero.order == STAT_MIN else 'FAIL'
    )

    # T13 — Local revolt with garrison: governor stays
    gov_garrisoned = GovernorState(
        settlement_id='S-001', has_governor=True, current_order=0,
        governor_standing=3,
    )
    stats_garrisoned = SettlementStats(prosperity=2, defense=3, order=0)
    result = resolve_local_revolt(stats_garrisoned, gov_garrisoned, garrison_present=True)
    r['T13_revolt_garrison_contains'] = (
        'PASS' if result.success and gov_garrisoned.has_governor
        else f'FAIL ({result}, has_gov={gov_garrisoned.has_governor})'
    )

    # T14 — Local revolt without garrison: governor expelled
    gov_undefended = GovernorState(
        settlement_id='S-001', has_governor=True, current_order=0,
        governor_standing=3,
    )
    stats_undefended = SettlementStats(prosperity=2, defense=0, order=0)
    result = resolve_local_revolt(stats_undefended, gov_undefended, garrison_present=False)
    r['T14_revolt_no_garrison_expels'] = (
        'PASS' if result.success and not gov_undefended.has_governor
        else f'FAIL ({result}, has_gov={gov_undefended.has_governor})'
    )

    # T15 — RM Governance Transition: Disestablishment returns persistent state
    stats_diss = SettlementStats(prosperity=3, defense=2, order=3)
    result, state = resolve_rm_governance_transition(
        stats_diss, GovernanceTransitionMode.DISESTABLISHMENT)
    ok = (result.success
          and state is not None
          and state.mode == GovernanceTransitionMode.DISESTABLISHMENT
          and state.seasons_remaining_in_penalty == DISESTABLISHMENT_PENALTY_SEASON_COUNT)
    r['T15_disestablishment_returns_state'] = 'PASS' if ok else f'FAIL ({result}, {state})'

    # T16 — Accommodation: no persistent state
    result, state = resolve_rm_governance_transition(
        stats_diss, GovernanceTransitionMode.ACCOMMODATION)
    r['T16_accommodation_no_state'] = (
        'PASS' if result.success and state is None else 'FAIL'
    )

    # T17 — Transformation: persistent state with 4 seasons remaining
    result, state = resolve_rm_governance_transition(
        stats_diss, GovernanceTransitionMode.TRANSFORMATION)
    ok = (result.success
          and state is not None
          and state.seasons_remaining_in_transition == TRANSFORMATION_DURATION_SEASONS)
    r['T17_transformation_returns_state'] = 'PASS' if ok else f'FAIL'

    # T18 — advance_transition_state Disestablishment: 2 seasons drain
    stats_t = SettlementStats(prosperity=3, defense=2, order=3)
    state_diss = GovernanceTransitionState(
        settlement_id='S-001', mode=GovernanceTransitionMode.DISESTABLISHMENT,
        seasons_remaining_in_penalty=DISESTABLISHMENT_PENALTY_SEASON_COUNT,
    )
    advance_transition_state(state_diss, stats_t)
    # [canonical: §4.3 — "−1 Order for 2 seasons"]
    expected_order_after_first_season = 2
    expected_seasons_remaining = 1
    ok = (stats_t.order == expected_order_after_first_season
          and state_diss.seasons_remaining_in_penalty == expected_seasons_remaining
          and not state_diss.accord_growth_active)
    r['T18_disestablishment_first_season'] = (
        'PASS' if ok else f'FAIL (order={stats_t.order}, remaining={state_diss.seasons_remaining_in_penalty})'
    )

    # T19 — advance_transition_state Disestablishment: 2nd season activates accord
    advance_transition_state(state_diss, stats_t)
    # [canonical: §4.3 — "−1 Order for 2 seasons, then Accord growth +0.5/season"]
    expected_order_after_two_seasons = 1
    ok = (stats_t.order == expected_order_after_two_seasons
          and state_diss.seasons_remaining_in_penalty == 0
          and state_diss.accord_growth_active)
    r['T19_disestablishment_second_season_activates_accord'] = (
        'PASS' if ok else f'FAIL (order={stats_t.order}, active={state_diss.accord_growth_active})'
    )

    # T20 — Consensus Delay: emergency action in RM settlement, no waiver
    delay = compute_consensus_delay('Muster',
                                     rm_governs_settlement=True,
                                     waiver_used=False)
    r['T20_consensus_delay_applies'] = (
        'PASS' if delay == CONSENSUS_DELAY_SEASONS else f'FAIL ({delay})'
    )

    # T21 — Consensus Delay: non-emergency action, no delay
    delay = compute_consensus_delay('Develop',
                                     rm_governs_settlement=True,
                                     waiver_used=False)
    r['T21_consensus_delay_non_emergency_no_delay'] = (
        'PASS' if delay == 0 else f'FAIL ({delay})'
    )

    # T22 — Consensus Delay: waived
    delay = compute_consensus_delay('Muster',
                                     rm_governs_settlement=True,
                                     waiver_used=True)
    r['T22_consensus_delay_waived'] = (
        'PASS' if delay == 0 else f'FAIL ({delay})'
    )

    # T23 — Thread op cap: applying same delta twice respects ±1 per stat
    stats_thread = SettlementStats(prosperity=3, defense=3, order=3)
    season_deltas: Dict[str, int] = {}
    # First Weaving: success → Order +1
    apply_thread_op(ThreadOperation.WEAVING, stats_thread, succeeded=True,
                    delta_already_applied_this_season=season_deltas)
    first_order = stats_thread.order
    # Second Weaving: would push Order +2 cumulative, exceeds cap of +1
    apply_thread_op(ThreadOperation.WEAVING, stats_thread, succeeded=True,
                    delta_already_applied_this_season=season_deltas)
    second_order = stats_thread.order
    # [canonical: §4.4 — "Cap: ±1 per settlement stat per season"]
    r['T23_thread_op_cap_per_stat_per_season'] = (
        'PASS' if first_order == 4 and second_order == 4 else
        f'FAIL (first={first_order}, second={second_order})'
    )

    # T24 — Mending success applies Prosperity +1
    stats_mend = SettlementStats(prosperity=2, defense=2, order=3)
    season_deltas = {}
    apply_thread_op(ThreadOperation.MENDING, stats_mend, succeeded=True,
                    delta_already_applied_this_season=season_deltas)
    # [canonical: §4.4 Mending — "Prosperity +1 on success"]
    r['T24_mending_success_prosperity_plus_1'] = (
        'PASS' if stats_mend.prosperity == 3 else f'FAIL ({stats_mend.prosperity})'
    )

    # T25 — Dissolution failure: Defense -1 AND Order -1
    stats_diss_op = SettlementStats(prosperity=2, defense=3, order=3)
    season_deltas = {}
    apply_thread_op(ThreadOperation.DISSOLUTION, stats_diss_op, succeeded=False,
                    delta_already_applied_this_season=season_deltas)
    # [canonical: §4.4 Dissolution — "Defense −1 AND Order −1 on failure"]
    expected_defense_post_diss = 2
    expected_order_post_diss = 2
    ok = (stats_diss_op.defense == expected_defense_post_diss
          and stats_diss_op.order == expected_order_post_diss)
    r['T25_dissolution_failure_both'] = (
        'PASS' if ok else f'FAIL (def={stats_diss_op.defense}, ord={stats_diss_op.order})'
    )

    # T26 — Community Organizing gated by PT ≤ 2
    stats_co_low_pt = SettlementStats(prosperity=2, defense=2, order=2)
    season_deltas = {}
    result = apply_thread_op(ThreadOperation.COMMUNITY_ORGANIZING, stats_co_low_pt,
                              succeeded=True,
                              delta_already_applied_this_season=season_deltas,
                              province_pt=2)
    # [canonical: §4.4 Community Organizing — "if PT ≤ 2 in province"]
    expected_co_order_low_pt = 3
    r['T26_community_organizing_low_pt_succeeds'] = (
        'PASS' if result.success and stats_co_low_pt.order == expected_co_order_low_pt
        else f'FAIL ({result}, order={stats_co_low_pt.order})'
    )

    # T27 — Community Organizing blocked at PT > 2
    stats_co_high_pt = SettlementStats(prosperity=2, defense=2, order=2)
    season_deltas = {}
    result = apply_thread_op(ThreadOperation.COMMUNITY_ORGANIZING, stats_co_high_pt,
                              succeeded=True,
                              delta_already_applied_this_season=season_deltas,
                              province_pt=4)
    r['T27_community_organizing_high_pt_blocked'] = (
        'PASS' if not result.success and stats_co_high_pt.order == 2 else 'FAIL'
    )

    # T28 — Inquisitor surveillance fires for Thread practitioner
    infra_inq = ChurchInfrastructure(settlement_id='S-001', inquisitor_base=True)
    r['T28_inquisitor_surveillance_thread'] = (
        'PASS' if inquisitor_concealment_test_required(infra_inq,
                                                        is_thread_practitioner=True)
        else 'FAIL'
    )

    # T29 — Inquisitor surveillance: non-practitioner unaffected
    r['T29_inquisitor_surveillance_non_practitioner'] = (
        'PASS' if not inquisitor_concealment_test_required(infra_inq,
                                                            is_thread_practitioner=False)
        else 'FAIL'
    )

    # T30 — No Inquisitor: surveillance does NOT fire
    infra_no_inq = ChurchInfrastructure(settlement_id='S-001', inquisitor_base=False)
    r['T30_no_inquisitor_no_surveillance'] = (
        'PASS' if not inquisitor_concealment_test_required(infra_no_inq,
                                                            is_thread_practitioner=True)
        else 'FAIL'
    )

    # T31 — Templar interrupt applies when Templar present + rival action + CI
    infra_tmp = ChurchInfrastructure(settlement_id='S-001', templar_station=True)
    result_tmp = apply_templar_interrupt(infra_tmp,
                                          rival_action_in_progress=True,
                                          church_ci_available=5)
    ok = (result_tmp.applied
          and result_tmp.rival_ob_delta == 1
          and result_tmp.ci_spent == 1)
    r['T31_templar_interrupt_applies'] = 'PASS' if ok else f'FAIL ({result_tmp})'

    # T32 — Templar interrupt blocked when no Templar
    infra_no_tmp = ChurchInfrastructure(settlement_id='S-001', templar_station=False)
    result_tmp = apply_templar_interrupt(infra_no_tmp,
                                          rival_action_in_progress=True,
                                          church_ci_available=5)
    r['T32_templar_interrupt_no_templar'] = (
        'PASS' if not result_tmp.applied else 'FAIL'
    )

    # T33 — Templar interrupt blocked when insufficient CI
    result_tmp = apply_templar_interrupt(infra_tmp,
                                          rival_action_in_progress=True,
                                          church_ci_available=0)
    r['T33_templar_interrupt_no_ci'] = (
        'PASS' if not result_tmp.applied else 'FAIL'
    )

    # T34 — Niflhel detection at Evidence Track ≥ 3
    r['T34_niflhel_detection_at_3'] = (
        'PASS' if attempt_niflhel_detection(investigation_evidence_track=3)
        and not attempt_niflhel_detection(investigation_evidence_track=2)
        else 'FAIL'
    )

    # T35 — Local Actor count for canonical types
    fake_seat = Settlement(id='S-XXX', name='Test', type='Seat',
                           province='X', duchy='X', role='x')
    fake_outpost = Settlement(id='S-XXX', name='Test', type='Outpost',
                              province='X', duchy='X', role='x')
    # [canonical: §4.5 — "Seat: 2 ... Outpost: 0"]
    ok = (local_actor_count(fake_seat) == 2
          and local_actor_count(fake_outpost) == 0)
    r['T35_local_actor_canonical_counts'] = 'PASS' if ok else 'FAIL'

    # T36 — F12: extra types return None directly
    fake_village = Settlement(id='S-XXX', name='Test', type='Village',
                              province='X', duchy='X', role='x')
    r['T36_extra_types_unmapped'] = (
        'PASS' if local_actor_count(fake_village) is None else 'FAIL'
    )

    # T37 — F12: provisional sim-side fallback for extras
    r['T37_extras_provisional_fallback'] = (
        'PASS' if effective_local_actor_count(fake_village) == 1 else 'FAIL'
    )

    # T38 — F13: canonical-eight-only count from registry is 25 (not ~45-50)
    actors_from_registry = sum(
        LOCAL_ACTOR_COUNT_BY_TYPE.get(s.type, 0) for s in REGISTRY
    )
    r['T38_F13_registry_actor_count'] = (
        'PASS' if actors_from_registry == ACTORS_FROM_CANONICAL_EIGHT_ONLY
        else f'FAIL ({actors_from_registry})'
    )

    # T39 — Local Actor disposition driver: governs + order improves = +1
    actor = LocalActor(settlement_id='S-001', name='Test', role='Elder',
                       conviction='loyalty')
    new_val = adjust_disposition(actor, 'Crown', 'governs_order_improves')
    r['T39_disposition_governs_improves'] = (
        'PASS' if new_val == DISPOSITION_DRIVER_GOVERNS_ORDER_IMPROVES else 'FAIL'
    )

    # T40 — Public combat: Disposition -2
    actor2 = LocalActor(settlement_id='S-001', name='Test', role='Elder',
                        conviction='loyalty')
    new_val = adjust_disposition(actor2, 'Crown', 'public_combat')
    r['T40_disposition_public_combat'] = (
        'PASS' if new_val == DISPOSITION_DRIVER_PUBLIC_COMBAT else 'FAIL'
    )

    # T41 — Controller change resets all dispositions
    actor3 = LocalActor(settlement_id='S-001', name='Test', role='Elder',
                        conviction='loyalty',
                        disposition_by_party={'Crown': 3, 'Church': -2})
    reset_disposition_on_controller_change(actor3)
    r['T41_controller_change_resets'] = (
        'PASS' if actor3.disposition_by_party == {} else 'FAIL'
    )

    # T42 — Recruitment candidate at Disposition >= 3
    actor4 = LocalActor(settlement_id='S-001', name='Test', role='Elder',
                        conviction='loyalty',
                        disposition_by_party={'Crown': 3})
    actor5 = LocalActor(settlement_id='S-001', name='Test', role='Elder',
                        conviction='loyalty',
                        disposition_by_party={'Crown': 2})
    ok = (is_recruitment_candidate(actor4, 'Crown')
          and not is_recruitment_candidate(actor5, 'Crown'))
    r['T42_recruitment_threshold'] = 'PASS' if ok else 'FAIL'

    # T43 — emergent chain test: Famine fires → Order drops → next-season
    # sweep fires Revolt (emergence from atomic predicates)
    state_chain = {
        'S-001': SettlementStats(prosperity=0, defense=2, order=1),
    }
    # Season N: famine fires
    fired_n = sweep_season_events(state_chain)
    # Resolve famine (Order -1 auto)
    if any(fe.event == SettlementEvent.FAMINE_ECONOMIC_COLLAPSE for fe in fired_n):
        resolve_famine(state_chain['S-001'])
    # Season N+1: predicate sweep again — Order should now be 0
    fired_n_plus_1 = sweep_season_events(state_chain)
    famine_in_n = any(fe.event == SettlementEvent.FAMINE_ECONOMIC_COLLAPSE for fe in fired_n)
    revolt_in_n_plus_1 = any(fe.event == SettlementEvent.LOCAL_REVOLT for fe in fired_n_plus_1)
    famine_in_n_plus_1 = any(fe.event == SettlementEvent.FAMINE_ECONOMIC_COLLAPSE for fe in fired_n_plus_1)
    ok = famine_in_n and revolt_in_n_plus_1 and famine_in_n_plus_1
    r['T43_emergent_famine_to_revolt_chain'] = (
        'PASS' if ok else
        f'FAIL (n: famine={famine_in_n}; n+1: famine={famine_in_n_plus_1}, revolt={revolt_in_n_plus_1})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 06 — settlement events + thread ops + local actors — isolation tests"
    bar_width = max(width, len(header))
    print("=" * bar_width)
    print(header)
    print("=" * bar_width)
    fail = False
    for k, v in results.items():
        marker = '✓' if v == 'PASS' else '✗'
        print(f"  {marker} {k:<{width}} {v}")
        if v != 'PASS':
            fail = True
    print("=" * bar_width)
    print(f"Event types: {len(SettlementEvent)}")
    print(f"Thread operations: {len(ThreadOperation)}")
    print(f"Governance Transition modes: {len(GovernanceTransitionMode)}")
    print(f"Local Actor canonical-types count from registry: {sum(LOCAL_ACTOR_COUNT_BY_TYPE.get(s.type, 0) for s in REGISTRY)}")
    sys.exit(1 if fail else 0)
