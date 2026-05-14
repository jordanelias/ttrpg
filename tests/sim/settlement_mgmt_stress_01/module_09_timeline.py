# module_09_timeline.py — Extended timeline + pressure clocks + Accounting hook
#
# Mode G Module nine of settlement_mgmt_stress_01.
#
# Approach: BOTTOM-UP GRANULAR EMERGENT (continued from M6/M7/M8) with
# explicit THROUGHLINE BINDINGS.
#
# THROUGHLINE BINDINGS (per references/throughlines_meta_infill.md §3.1):
#
#   T-04 MS Decay — PRIMARY. М-1 PRESSURE IS CONTINUOUS.
#   Load-bearing systems: clocks, ms_trajectory, peninsular_strain, threadwork.
#   Module 9 implements the canonical -1/year MS decay tick.
#
#   T-05 CI Accumulation — PRIMARY. М-1 PRESSURE IS CONTINUOUS.
#   Load-bearing: clocks, tc_political, faction_layer. Module 9 implements
#   the +1/season Church Influence accumulation (conditional on Church
#   Mandate >= 3 per the recalibrated rule in §7.1).
#
#   T-06 IP Accumulation — PRIMARY. М-1 PRESSURE IS CONTINUOUS.
#   Load-bearing: clocks, peninsular_strain, victory. Module 9 implements
#   the recalibrated +1/2-seasons IP rate per §7.1 (was +1/season).
#
#   T-07 Turmoil — PRIMARY. М-1 PRESSURE IS CONTINUOUS.
#   Load-bearing: peninsular_strain, clocks, victory, tensions_deck,
#   royal_assassination_fuse. Module 9 implements per-season Turmoil
#   accumulation gated on inter-faction battle events.
#
#   T-25 Generational Arc — SECONDARY. М-5 SCALES CONNECT.
#   "30-year clock transforms personal standings into institutional reality."
#   Module 9 implements the Generational Shift 0-10 track with the §7.1
#   thresholds (Year 10 -1, Year 20 -2, Year 30 -3 to highest attribute
#   of original leaders) and the TS-50 exemption.
#
# META-THROUGHLINE BINDINGS (per references/throughlines_meta.md §3):
#
#   М-1 PRESSURE IS CONTINUOUS — PRIMARY. This module IS the pressure-tick
#   substrate. T-04, T-05, T-06, T-07 all subordinate to М-1.
#
#   М-5 SCALES CONNECT THROUGH SUBSTRATE — SECONDARY. T-25 generational
#   wraps personal-standing accumulation into institutional reality at
#   30-year scale.
#
# Module 9 closes the major М-1 gap identified by M8's retroactive audit.
#
# Encodes:
#   §7.1 Clock recalibration for 10-30 year games (MS, CI, IP rates +
#        Generational Shift new clock with TS-50 exemption)
#   §7.2 Succession System (Settlement / Province / Cross-generational)
#
# This module also supplies the per-season ACCOUNTING HOOK that composes
# all prior modules' per-season effects:
#   - M4 Chapel half-Order accumulator advancement
#   - M5 Ministry order_decay_modifier consumption
#   - M6 GovernanceTransitionState advancement
#   - M6 sweep_season_events orchestration call
#   - M7 SiegeState tick advancement
#   - M3 advance_decade reset (when 10-season cycles)
#
# Bottom-up: the Accounting hook is a pure composition function. Each
# sub-system advances independently; the hook is the per-season clock
# tick that calls them in canonical order.
#
# Canonical sources (full read this session):
#   designs/territory/settlement_layer_v30.md (§7.1, §7.2)
#   designs/provincial/clock_registry_v30.md (canonical clock registry)
#   params/bg/clocks.md (canonical clock environmental effects)
#
# Out of scope (deferred):
#   - calamity_radiation_v30 MS-band effects table at Accounting — Module 12
#   - Mass Seizure Declaration cascade at CI=100 — Module 12
#   - Altonian Vanguard advance mechanics — Module 12
#   - Battle Consequences cascades (MS -1, IP +2 per inter-faction battle) —
#     surfaced as constants here but applied at the faction-state layer (M12)
#   - faction-leader attribute mechanics for Generational Shift —
#     Module 12; Module 9 surfaces the penalty schedule
#   - Solmund vs Thread certainty mechanics for protégé inheritance —
#     Module 12

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional, Tuple

from module_01_primitives import REGISTRY, Settlement, SettlementStats
from module_03_facilities import (
    ActionResult, FacilityState, advance_decade,
)
from module_04_church import (
    ChurchInfrastructure, accrue_parish_bonus_per_season,
)
from module_05_governance import (
    GovernorState, SubnationalFaction, MANAGEMENT_EFFECTS,
)
from module_06_events import (
    sweep_season_events, FiredEvent, SettlementEvent,
    GovernanceTransitionState, advance_transition_state,
)
from module_07_military import (
    Garrison, resolve_siege_tick, SiegeState, BypassState,
)
from module_08_progression import (
    StatureState, apply_renown_delta,
)


# ── Canonical clock starting values + ranges ────────────────────────────────

# §clock_registry MS row: range 0-100, start 72, direction decay
# [canonical: clock_registry_v30.md Shared Clocks table —
#  "| Mending Stability (MS) | 0–100 | 72 | ↓ (decay) | params_threadwork.md §MS."]
MS_START: int = 72
MS_MAX: int = 100
MS_MIN: int = 0
MS_RUPTURE_VALUE: int = 0   # campaign-ends value

# §clock_registry CI row: range 0-100, start 28, direction up
# [canonical: clock_registry_v30.md — "Church Influence (CI) | 0–100 | 28 | ↑"]
CI_START: int = 28
CI_MAX: int = 100
CI_MIN: int = 0

# §clock_registry IP row: range 0-100, start 20, direction up
# [canonical: clock_registry_v30.md —
#  "Institutional Pressure (IP) | 0–100 | 20 | ↑"]
IP_START: int = 20
IP_MAX: int = 100
IP_MIN: int = 0

# §clock_registry Turmoil row: range 0-10, start 0, direction up
# [canonical: clock_registry_v30.md — "Turmoil | 0–10 | 0 | ↑ (bad)"]
TURMOIL_START: int = 0
TURMOIL_MAX: int = 10
TURMOIL_MIN: int = 0


# ── §7.1 recalibrated clock rates for 10-30 year games ──────────────────────

# §7.1 MS decay: -1/year baseline (unchanged from pre-recalibration)
# [canonical: settlement_layer_v30 §7.1 MS row —
#  "MS decay | −1/year baseline | −1/year baseline (unchanged)"]
MS_DECAY_PER_YEAR: int = 1   # subtracted from MS per game-year

# §7.1 Year-to-seasons conversion (canonical 4 seasons per year)
# [canonical: implied by §7.1 — "30-year game = 120 seasons"]
SEASONS_PER_YEAR: int = 4

# §7.1 CI accumulation: +1/season if Church Mandate ≥ 3
# [canonical: settlement_layer_v30 §7.1 CI row —
#  "Passive +1/season if Church Mandate ≥ 3 (existing conditional). 28 start."]
CI_ACCUMULATION_PER_SEASON: int = 1
CI_ACCUMULATION_CHURCH_MANDATE_THRESHOLD: int = 3

# §7.1 CI 75 phase transition threshold
# [canonical: settlement_layer_v30 §7.1 CI row —
#  "CI caps at 75 (phase transition)"]
CI_PHASE_TRANSITION_THRESHOLD: int = 75

# §7.1 IP accumulation: RECALIBRATED to +1/2 seasons (halved)
# [canonical: settlement_layer_v30 §7.1 IP row —
#  "+1/2 seasons baseline (halved)"]
IP_ACCUMULATION_PER_SEASONS: int = 1   # accumulates 1 unit
IP_ACCUMULATION_SEASON_PERIOD: int = 2  # ...every 2 seasons

# [FINDING F17] clock_registry_v30.md and params/bg/clocks.md do not reflect
# the §7.1 recalibration of IP to +1/2 seasons. clock_registry still lists
# IP start 20 (matches) but neither file documents the rate change.
# settlement_layer §7.1 is the post-recalibration canonical source. Editorial
# decision needed to propagate the §7.1 recalibration into clock_registry +
# params/bg/clocks (or to mark §7.1 itself as governing).

# §battle-consequence — peninsular_strain_v1 §3 (cited by params/bg/clocks)
# [canonical: params/bg/clocks.md —
#  "All battles on Valorian soil: MS −1 (MS −2 for Campaign/War scale).
#  Each season with inter-faction battle: IP +2.
#  Each season with inter-faction battle: Turmoil +1.
#  Faction elimination: Strain +2.
#  Territory Revolt (Accord 0): Strain +1."]
BATTLE_MS_PENALTY_NORMAL: int = 1
BATTLE_MS_PENALTY_CAMPAIGN_WAR: int = 2
INTER_FACTION_BATTLE_IP_DELTA: int = 2
INTER_FACTION_BATTLE_TURMOIL_DELTA: int = 1
FACTION_ELIMINATION_STRAIN_DELTA: int = 2
TERRITORY_REVOLT_STRAIN_DELTA: int = 1


# ── §7.1 Generational Shift — new clock ─────────────────────────────────────

# [canonical: settlement_layer_v30 §7.1 —
#  "New clock: Generational Shift (0–10)."]
GENERATIONAL_SHIFT_MIN: int = 0
GENERATIONAL_SHIFT_MAX: int = 10
GENERATIONAL_SHIFT_START: int = 0

# [canonical: settlement_layer_v30 §7.1 — "Rate: +1 per 5 years of game time."]
GENERATIONAL_SHIFT_YEARS_PER_TICK: int = 5

# §7.1 Generational Shift thresholds + attribute penalties
# [canonical: settlement_layer_v30 §7.1 Generational Shift —
#  "Threshold 2 (Year 10): -1 to highest attribute"]
GEN_SHIFT_THRESHOLD_FIRST_PENALTY: int = 2
GEN_SHIFT_FIRST_ATTRIBUTE_PENALTY: int = 1
GEN_SHIFT_FIRST_YEAR_MARKER: int = 10

# [canonical: settlement_layer_v30 §7.1 —
#  "Threshold 4 (Year 20): -2 to highest attribute"]
GEN_SHIFT_THRESHOLD_SECOND_PENALTY: int = 4
GEN_SHIFT_SECOND_ATTRIBUTE_PENALTY: int = 2
GEN_SHIFT_SECOND_YEAR_MARKER: int = 20

# [canonical: settlement_layer_v30 §7.1 —
#  "Threshold 6 (Year 30): -3 to highest attribute"]
GEN_SHIFT_THRESHOLD_THIRD_PENALTY: int = 6
GEN_SHIFT_THIRD_ATTRIBUTE_PENALTY: int = 3
GEN_SHIFT_THIRD_YEAR_MARKER: int = 30

# [canonical: settlement_layer_v30 §7.1 — "Characters (NPC or PC) with
#  Thread Sensitivity ≥ 50 are exempt"]
TS_EXEMPTION_FROM_AGE_PENALTY_THRESHOLD: int = 50


# ── Canonical clock state ───────────────────────────────────────────────────

@dataclass
class ClockState:
    # Canonical pressure-clock state per Module-nine ownership.
    # Mutable. The Module-twelve faction layer consumes these for effect resolution.
    ms: int = MS_START
    ci: int = CI_START
    ip: int = IP_START
    turmoil: int = TURMOIL_START
    generational_shift: int = GENERATIONAL_SHIFT_START
    # Internal counters
    seasons_elapsed: int = 0
    ip_partial_accumulator: int = 0   # accumulates 1 every 2 seasons


# ── Per-season pressure-tick functions (pure transforms on ClockState) ─────

def tick_ms_decay(state: ClockState, is_year_boundary: bool) -> int:
    # Throughline-MS-Decay tick. -1/year on year boundaries. Returns the new MS value.
    # Mutates state in place. Clamps at [MS_MIN, MS_MAX].
    if is_year_boundary:
        new_ms = max(MS_MIN, state.ms - MS_DECAY_PER_YEAR)
        state.ms = new_ms
    return state.ms


def tick_ci_accumulation(
    state: ClockState,
    church_mandate: int,
) -> int:
    # Throughline-CI-Accumulation tick. +one-per-season if Church Mandate >= threshold.
    # Clamps at [CI_MIN, CI_MAX]. Returns the new CI value.
    if church_mandate >= CI_ACCUMULATION_CHURCH_MANDATE_THRESHOLD:
        new_ci = min(CI_MAX, state.ci + CI_ACCUMULATION_PER_SEASON)
        state.ci = new_ci
    return state.ci


def tick_ip_accumulation(state: ClockState) -> int:
    # Throughline-IP-Accumulation tick. RECALIBRATED to +one-per-two-seasons per §7.1.
    # Uses ip_partial_accumulator: increments per call; emits +one-IP when
    # accumulator reaches IP_ACCUMULATION_SEASON_PERIOD then drains.
    # Clamps at [IP_MIN, IP_MAX]. Returns the new IP value.
    state.ip_partial_accumulator += 1
    if state.ip_partial_accumulator >= IP_ACCUMULATION_SEASON_PERIOD:
        state.ip_partial_accumulator -= IP_ACCUMULATION_SEASON_PERIOD
        new_ip = min(IP_MAX, state.ip + IP_ACCUMULATION_PER_SEASONS)
        state.ip = new_ip
    return state.ip


def tick_turmoil(state: ClockState, inter_faction_battle_this_season: bool) -> int:
    # Throughline-Turmoil tick. +one per season with inter-faction battle.
    # Clamps at [TURMOIL_MIN, TURMOIL_MAX]. Returns the new Turmoil value.
    if inter_faction_battle_this_season:
        new_turmoil = min(TURMOIL_MAX, state.turmoil + INTER_FACTION_BATTLE_TURMOIL_DELTA)
        state.turmoil = new_turmoil
    return state.turmoil


def tick_generational_shift(state: ClockState, is_five_year_boundary: bool) -> int:
    """T-25 Generational Shift tick. +1 per 5 years.
    Returns the new value. Clamps at [GENERATIONAL_SHIFT_MIN, GENERATIONAL_SHIFT_MAX]."""
    if is_five_year_boundary:
        new_gs = min(GENERATIONAL_SHIFT_MAX,
                     state.generational_shift + 1)
        state.generational_shift = new_gs
    return state.generational_shift


# ── §7.1 attribute penalty lookup for Generational Shift ────────────────────

def attribute_penalty_for_age(
    generational_shift: int,
    character_thread_sensitivity: int,
) -> int:
    """§7.1 attribute penalty: -1 at threshold 2, -2 at threshold 4, -3 at
    threshold 6. TS >= 50 exempt.
    Returns the penalty as a positive integer (caller subtracts from
    highest attribute)."""
    # TS-50 exemption per §7.1 P-15 metaphysical justification
    if character_thread_sensitivity >= TS_EXEMPTION_FROM_AGE_PENALTY_THRESHOLD:
        return 0
    if generational_shift >= GEN_SHIFT_THRESHOLD_THIRD_PENALTY:
        return GEN_SHIFT_THIRD_ATTRIBUTE_PENALTY
    if generational_shift >= GEN_SHIFT_THRESHOLD_SECOND_PENALTY:
        return GEN_SHIFT_SECOND_ATTRIBUTE_PENALTY
    if generational_shift >= GEN_SHIFT_THRESHOLD_FIRST_PENALTY:
        return GEN_SHIFT_FIRST_ATTRIBUTE_PENALTY
    return 0


# ── §7.2 Succession System ──────────────────────────────────────────────────

# §7.2 Settlement succession - Order -1 per season until governor assigned
# [canonical: settlement_layer_v30 §7.2 —
#  "the settlement becomes unmanaged (Order −1 per season until a governor
#  is assigned)"]
UNMANAGED_SETTLEMENT_ORDER_DECREMENT_PER_SEASON: int = 1


def unmanaged_settlement_tick(stats: SettlementStats) -> int:
    """§7.2 Settlement succession — Order -1 per season for unmanaged
    settlements. Caller must check has_governor==False before calling.
    Clamps at STAT_MIN."""
    from module_01_primitives import STAT_MIN
    new_order = max(STAT_MIN, stats.order - UNMANAGED_SETTLEMENT_ORDER_DECREMENT_PER_SEASON)
    stats.order = new_order
    return stats.order


# §7.2 Cross-generational protégé inheritance
# [canonical: settlement_layer_v30 §7.2 —
#  "if the player has a protégé (a named NPC companion or officer with
#  Disposition +4 and Standing 4+), the player may transfer their governance
#  to the protégé and create a new character — starting at Standing 0 but
#  inheriting Renown ÷ 2 (round down) from their predecessor's reputation"]
PROTEGE_DISPOSITION_THRESHOLD: int = 4
PROTEGE_STANDING_THRESHOLD: int = 4
PROTEGE_RENOWN_DIVISOR: int = 2


def is_eligible_protege(
    disposition: int,
    standing: int,
) -> bool:
    """§7.2 — protégé eligibility for cross-generational transfer."""
    return (disposition >= PROTEGE_DISPOSITION_THRESHOLD
            and standing >= PROTEGE_STANDING_THRESHOLD)


def cross_generational_inheritance(
    predecessor_renown: int,
) -> int:
    """§7.2 — successor starts at Standing 0, inherits Renown ÷ 2 (round down)."""
    return predecessor_renown // PROTEGE_RENOWN_DIVISOR


# ── Per-season Accounting hook (the canonical composition function) ─────────

@dataclass
class SeasonContext:
    """Context bundled for the per-season Accounting hook. Module 9 uses
    this as a pure-function aggregator; downstream modules consume the
    return value (post-Accounting state snapshot)."""
    season_number: int                                 # absolute season counter, 1+
    clock_state: ClockState
    settlement_stats_by_id: Dict[str, SettlementStats]
    church_infra_by_id: Dict[str, ChurchInfrastructure]
    governor_state_by_id: Dict[str, GovernorState]
    facility_state_by_id: Dict[str, FacilityState]
    governance_transitions: Dict[str, GovernanceTransitionState]
    active_sieges: Dict[str, SiegeState]
    church_mandate: int                                # for CI gate
    inter_faction_battle_this_season: bool
    adjacent_hostile_by_id: Dict[str, bool] = field(default_factory=dict)
    hostile_in_province_by_id: Dict[str, bool] = field(default_factory=dict)
    cv_changed_by_province: Dict[str, bool] = field(default_factory=dict)


@dataclass(frozen=True)
class AccountingReport:
    # Output of one Accounting tick. The Module-twelve faction layer
    # consumes this to apply province-level effects.
    season_number: int
    is_year_boundary: bool
    is_five_year_boundary: bool
    fired_events: List[FiredEvent]
    sieges_surrendered: List[str]                     # settlement IDs
    governance_transitions_completed: List[str]
    parish_ticks_triggered: List[str]                 # settlement IDs where +1 Order tick fired
    unmanaged_settlements: List[str]
    clock_state_snapshot: ClockState                  # post-tick clock state


def per_season_accounting(ctx: SeasonContext) -> AccountingReport:
    # Per-season Accounting tick. Canonical composition function.
    #
    # Order of operations (canonical sequence):
    #   1. Advance season counter, determine year/five-year boundaries
    #   2. Pressure-clock ticks (MS, CI, IP, Turmoil, Generational Shift)
    #      — М-one PRESSURE IS CONTINUOUS substrate
    #   3. Per-settlement state advances (parish accumulators, transitions,
    #      siege ticks, unmanaged decrement) — bottom-up composition
    #   4. Event sweep over registry — pressure + state composes into
    #      emergent events (the four M-one throughlines surface as event firings)
    #   5. Decade-boundary resets (Module-three facility expansion cap)
    is_year_boundary = (ctx.season_number % SEASONS_PER_YEAR == 0)
    years_elapsed_so_far = ctx.season_number // SEASONS_PER_YEAR
    is_five_year_boundary = (
        is_year_boundary
        and years_elapsed_so_far > 0
        and years_elapsed_so_far % GENERATIONAL_SHIFT_YEARS_PER_TICK == 0
    )
    is_decade_boundary = (
        is_year_boundary
        and years_elapsed_so_far > 0
        and years_elapsed_so_far % 10 == 0
    )

    # 2. Pressure-clock ticks
    tick_ms_decay(ctx.clock_state, is_year_boundary)
    tick_ci_accumulation(ctx.clock_state, ctx.church_mandate)
    tick_ip_accumulation(ctx.clock_state)
    tick_turmoil(ctx.clock_state, ctx.inter_faction_battle_this_season)
    tick_generational_shift(ctx.clock_state, is_five_year_boundary)

    # 3. Per-settlement state advances (composition with prior modules)
    parish_ticks_triggered: List[str] = []
    for sid, infra in ctx.church_infra_by_id.items():
        stats = ctx.settlement_stats_by_id.get(sid)
        if stats is None:
            continue
        (_acc, triggered) = accrue_parish_bonus_per_season(infra, stats)
        if triggered:
            parish_ticks_triggered.append(sid)

    governance_transitions_completed: List[str] = []
    for sid, trans in list(ctx.governance_transitions.items()):
        stats = ctx.settlement_stats_by_id.get(sid)
        if stats is None:
            continue
        advance_transition_state(trans, stats)
        # Disestablishment completes when seasons_remaining_in_penalty == 0
        # AND accord_growth_active. Transformation completes when
        # seasons_remaining_in_transition == 0 AND accord_growth_active.
        if trans.accord_growth_active:
            governance_transitions_completed.append(sid)

    sieges_surrendered: List[str] = []
    for sid, siege in list(ctx.active_sieges.items()):
        stats = ctx.settlement_stats_by_id.get(sid)
        if stats is None:
            continue
        (_res, surrender) = resolve_siege_tick(siege, stats)
        if surrender:
            sieges_surrendered.append(sid)

    # §7.2 Unmanaged settlement decrement
    unmanaged_settlements: List[str] = []
    for sid, gov in ctx.governor_state_by_id.items():
        if not gov.has_governor:
            stats = ctx.settlement_stats_by_id.get(sid)
            if stats is None:
                continue
            unmanaged_settlement_tick(stats)
            unmanaged_settlements.append(sid)

    # 4. Event sweep (M6 composition — emergent events fire from state)
    fired_events = sweep_season_events(
        ctx.settlement_stats_by_id,
        adjacent_hostile_by_id=ctx.adjacent_hostile_by_id,
        hostile_in_province_by_id=ctx.hostile_in_province_by_id,
        cv_changed_by_province=ctx.cv_changed_by_province,
    )

    # 5. Decade boundary — reset M3 facility-expansion caps
    if is_decade_boundary:
        for fac in ctx.facility_state_by_id.values():
            advance_decade(fac)

    ctx.clock_state.seasons_elapsed = ctx.season_number

    return AccountingReport(
        season_number=ctx.season_number,
        is_year_boundary=is_year_boundary,
        is_five_year_boundary=is_five_year_boundary,
        fired_events=fired_events,
        sieges_surrendered=sieges_surrendered,
        governance_transitions_completed=governance_transitions_completed,
        parish_ticks_triggered=parish_ticks_triggered,
        unmanaged_settlements=unmanaged_settlements,
        clock_state_snapshot=ctx.clock_state,
    )


# ── Throughline coverage (audit-facing) ─────────────────────────────────────

THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[str, str] = {
    'T-04': 'PRIMARY — tick_ms_decay implements canonical -1/year MS decay (closes М-1 gap).',
    'T-05': 'PRIMARY — tick_ci_accumulation implements +1/season conditional on Church Mandate >= 3.',
    'T-06': 'PRIMARY — tick_ip_accumulation implements §7.1 recalibrated +1/2-seasons rate.',
    'T-07': 'PRIMARY — tick_turmoil implements +1/season-with-inter-faction-battle.',
    'T-25': 'SECONDARY — tick_generational_shift + attribute_penalty_for_age realize the 30-year clock.',
}

META_THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[str, str] = {
    'М-1': 'PRIMARY — Module 9 IS the pressure-tick substrate. Closes the unbound-primary gap surfaced by M8 retroactive audit.',
    'М-5': 'SECONDARY — Generational Arc (T-25) scales personal-standing accumulation into institutional reality at 30-year horizon.',
}


# ── Isolation tests ─────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — ClockState defaults match canonical clock_registry start values
    cs = ClockState()
    # [canonical: clock_registry_v30.md — MS 72, CI 28, IP 20, Turmoil 0]
    ok = (cs.ms == MS_START and cs.ci == CI_START
          and cs.ip == IP_START and cs.turmoil == TURMOIL_START
          and cs.generational_shift == GENERATIONAL_SHIFT_START)
    r['T1_clock_defaults_canonical'] = (
        'PASS' if ok else f'FAIL (ms={cs.ms}, ci={cs.ci}, ip={cs.ip}, turmoil={cs.turmoil})'
    )

    # T2 — tick_ms_decay only on year boundary
    cs2 = ClockState(ms=72)
    tick_ms_decay(cs2, is_year_boundary=False)
    # [canonical: §7.1 — "-1/year baseline"]
    expected_no_change = 72
    r['T2_ms_no_decay_mid_year'] = (
        'PASS' if cs2.ms == expected_no_change else f'FAIL ({cs2.ms})'
    )

    # T3 — tick_ms_decay on year boundary
    tick_ms_decay(cs2, is_year_boundary=True)
    # 72 - 1 = 71
    # [canonical: derived from §7.1 MS row — 72 start - 1 year decay = 71]
    expected_post_year = 71
    r['T3_ms_decay_on_year_boundary'] = (
        'PASS' if cs2.ms == expected_post_year else f'FAIL ({cs2.ms})'
    )

    # T4 — MS clamps at min (rupture value)
    cs3 = ClockState(ms=0)
    tick_ms_decay(cs3, is_year_boundary=True)
    r['T4_ms_clamps_at_rupture'] = (
        'PASS' if cs3.ms == MS_RUPTURE_VALUE else f'FAIL ({cs3.ms})'
    )

    # T5 — CI accumulation requires Church Mandate >= 3
    cs4 = ClockState(ci=50)
    tick_ci_accumulation(cs4, church_mandate=3)
    # 50 + 1 = 51
    # [canonical: derived from §7.1 CI row — 50 + 1/season = 51]
    expected_ci_post = 51
    r['T5_ci_accumulates_at_threshold'] = (
        'PASS' if cs4.ci == expected_ci_post else f'FAIL ({cs4.ci})'
    )

    # T6 — CI does not accumulate below Church Mandate threshold
    cs5 = ClockState(ci=50)
    tick_ci_accumulation(cs5, church_mandate=2)
    r['T6_ci_blocked_below_mandate'] = (
        'PASS' if cs5.ci == 50 else f'FAIL ({cs5.ci})'
    )

    # T7 — CI clamps at max
    cs6 = ClockState(ci=CI_MAX)
    tick_ci_accumulation(cs6, church_mandate=5)
    r['T7_ci_clamps_at_max'] = (
        'PASS' if cs6.ci == CI_MAX else f'FAIL ({cs6.ci})'
    )

    # T8 — IP recalibration: +1 every 2 seasons (NOT every season)
    cs7 = ClockState(ip=20)
    tick_ip_accumulation(cs7)   # season 1: accumulator 1, IP 20
    after_one = cs7.ip
    tick_ip_accumulation(cs7)   # season 2: accumulator 2 → drains → IP 21
    after_two = cs7.ip
    # [canonical: §7.1 — "+1/2 seasons baseline (halved)"]
    expected_after_one = 20
    # [canonical: derived from §7.1 IP row — 20 start + 1/2-season after 2 ticks = 21]
    expected_after_two = 21
    ok = (after_one == expected_after_one and after_two == expected_after_two)
    r['T8_ip_recalibrated_rate'] = (
        'PASS' if ok else f'FAIL (s1={after_one}, s2={after_two})'
    )

    # T9 — IP accumulation continues correctly across 4 seasons
    # state after T8: cs7.ip=21, accumulator=0
    tick_ip_accumulation(cs7)   # s3: accumulator 1
    tick_ip_accumulation(cs7)   # s4: accumulator 2 → drains → IP 22
    # 4 ticks total since reset = 2 IP ticks
    # [canonical: derived from §7.1 IP row — 20 + 2 (two 2-season ticks) = 22]
    expected_after_four_seasons_two_ticks = 22
    r['T9_ip_four_seasons_two_ticks'] = (
        'PASS' if cs7.ip == expected_after_four_seasons_two_ticks
        else f'FAIL ({cs7.ip})'
    )

    # T10 — Turmoil accumulates on inter-faction battle
    cs8 = ClockState(turmoil=0)
    tick_turmoil(cs8, inter_faction_battle_this_season=True)
    # [canonical: params/bg/clocks.md battle consequences —
    #  "Each season with inter-faction battle: Turmoil +1"]
    r['T10_turmoil_accumulates_on_battle'] = (
        'PASS' if cs8.turmoil == 1 else f'FAIL ({cs8.turmoil})'
    )

    # T11 — Turmoil does not accumulate without battle
    cs9 = ClockState(turmoil=2)
    tick_turmoil(cs9, inter_faction_battle_this_season=False)
    r['T11_turmoil_blocked_no_battle'] = (
        'PASS' if cs9.turmoil == 2 else f'FAIL ({cs9.turmoil})'
    )

    # T12 — Turmoil clamps at max (10)
    cs10 = ClockState(turmoil=TURMOIL_MAX)
    tick_turmoil(cs10, inter_faction_battle_this_season=True)
    r['T12_turmoil_clamps_at_max'] = (
        'PASS' if cs10.turmoil == TURMOIL_MAX else f'FAIL ({cs10.turmoil})'
    )

    # T13 — Generational Shift only ticks on 5-year boundaries
    cs11 = ClockState(generational_shift=0)
    tick_generational_shift(cs11, is_five_year_boundary=False)
    r['T13_gen_shift_blocked_non_5yr'] = (
        'PASS' if cs11.generational_shift == 0 else f'FAIL ({cs11.generational_shift})'
    )

    # T14 — Generational Shift ticks on 5-year boundary
    tick_generational_shift(cs11, is_five_year_boundary=True)
    # [canonical: §7.1 — "Rate: +1 per 5 years of game time"]
    expected_gen_shift_post = 1
    r['T14_gen_shift_ticks_5yr'] = (
        'PASS' if cs11.generational_shift == expected_gen_shift_post
        else f'FAIL ({cs11.generational_shift})'
    )

    # T15 — attribute_penalty_for_age: GS 0 (Year <10) → no penalty
    r['T15_age_penalty_zero_pre_threshold'] = (
        'PASS' if attribute_penalty_for_age(generational_shift=0,
                                              character_thread_sensitivity=0) == 0
        else 'FAIL'
    )

    # T16 — attribute_penalty_for_age: GS 2 (Year 10) → -1
    # [canonical: §7.1 — "Threshold 2 (Year 10): ... -1 to highest attribute"]
    expected_first_penalty = GEN_SHIFT_FIRST_ATTRIBUTE_PENALTY
    r['T16_age_penalty_threshold_1'] = (
        'PASS' if attribute_penalty_for_age(generational_shift=GEN_SHIFT_THRESHOLD_FIRST_PENALTY,
                                              character_thread_sensitivity=0) == expected_first_penalty
        else 'FAIL'
    )

    # T17 — attribute_penalty_for_age: GS 4 (Year 20) → -2
    # [canonical: §7.1 — "Threshold 4 (Year 20): ... -2 to highest attribute"]
    r['T17_age_penalty_threshold_2'] = (
        'PASS' if attribute_penalty_for_age(generational_shift=GEN_SHIFT_THRESHOLD_SECOND_PENALTY,
                                              character_thread_sensitivity=0) == GEN_SHIFT_SECOND_ATTRIBUTE_PENALTY
        else 'FAIL'
    )

    # T18 — attribute_penalty_for_age: GS 6 (Year 30) → -3
    # [canonical: §7.1 — "Threshold 6 (Year 30): ... -3 to highest attribute"]
    r['T18_age_penalty_threshold_3'] = (
        'PASS' if attribute_penalty_for_age(generational_shift=GEN_SHIFT_THRESHOLD_THIRD_PENALTY,
                                              character_thread_sensitivity=0) == GEN_SHIFT_THIRD_ATTRIBUTE_PENALTY
        else 'FAIL'
    )

    # T19 — TS >= 50 exempts character from age penalty
    # [canonical: §7.1 — "Characters (NPC or PC) with Thread Sensitivity ≥ 50 are exempt"]
    high_ts = TS_EXEMPTION_FROM_AGE_PENALTY_THRESHOLD
    r['T19_ts_50_exempts'] = (
        'PASS' if attribute_penalty_for_age(generational_shift=GEN_SHIFT_THRESHOLD_THIRD_PENALTY,
                                              character_thread_sensitivity=high_ts) == 0
        else 'FAIL'
    )

    # T20 — Unmanaged settlement Order -1/season
    from module_01_primitives import SettlementStats as SS, STAT_MIN
    stats_unman = SS(prosperity=2, defense=2, order=3)
    unmanaged_settlement_tick(stats_unman)
    # [canonical: §7.2 — "Order −1 per season until a governor is assigned"]
    expected_order_post = 2
    r['T20_unmanaged_order_decrement'] = (
        'PASS' if stats_unman.order == expected_order_post else f'FAIL ({stats_unman.order})'
    )

    # T21 — Unmanaged settlement clamps at STAT_MIN
    stats_floor = SS(prosperity=2, defense=2, order=STAT_MIN)
    unmanaged_settlement_tick(stats_floor)
    r['T21_unmanaged_clamps_at_min'] = (
        'PASS' if stats_floor.order == STAT_MIN else 'FAIL'
    )

    # T22 — Protégé eligibility (Disposition +4, Standing 4+)
    r['T22_protege_eligible'] = (
        'PASS' if is_eligible_protege(disposition=4, standing=4) else 'FAIL'
    )

    # T23 — Protégé blocked on low Disposition
    r['T23_protege_blocked_low_disposition'] = (
        'PASS' if not is_eligible_protege(disposition=3, standing=4) else 'FAIL'
    )

    # T24 — Protégé blocked on low Standing
    r['T24_protege_blocked_low_standing'] = (
        'PASS' if not is_eligible_protege(disposition=4, standing=3) else 'FAIL'
    )

    # T25 — Cross-generational Renown inheritance: Renown 8 → successor 4
    # [canonical: §7.2 — "inheriting Renown ÷ 2 (round down)"]
    expected_inheritance = 4
    r['T25_cross_gen_inheritance'] = (
        'PASS' if cross_generational_inheritance(predecessor_renown=8) == expected_inheritance
        else 'FAIL'
    )

    # T26 — Cross-generational Renown 9 → 4 (round down)
    r['T26_cross_gen_round_down'] = (
        'PASS' if cross_generational_inheritance(predecessor_renown=9) == 4
        else 'FAIL'
    )

    # T27 — Battle Consequences canonical constants
    # [canonical: params/bg/clocks.md battle consequences —
    #  "Each season with inter-faction battle: IP +2"]
    r['T27_battle_ip_delta_2'] = (
        'PASS' if INTER_FACTION_BATTLE_IP_DELTA == 2 else 'FAIL'
    )

    # T28 — Per-season accounting hook: clock ticks fire
    cs_acct = ClockState(ms=72, ci=28, ip=20, turmoil=0)
    ctx = SeasonContext(
        season_number=4,   # year boundary (season 4 of year 1)
        clock_state=cs_acct,
        settlement_stats_by_id={},
        church_infra_by_id={},
        governor_state_by_id={},
        facility_state_by_id={},
        governance_transitions={},
        active_sieges={},
        church_mandate=3,
        inter_faction_battle_this_season=False,
    )
    report = per_season_accounting(ctx)
    ok = (report.is_year_boundary
          # [canonical: §7.1 MS row — 72 start - 1 year decay = 71]
          and cs_acct.ms == 71      # decay applied
          # [canonical: §7.1 CI row — 28 start + 1/season = 29]
          and cs_acct.ci == 29       # accumulation applied
          and cs_acct.ip == 20       # not yet — accumulator at 1
          and cs_acct.turmoil == 0)  # no battle
    r['T28_accounting_year_boundary_ticks'] = (
        'PASS' if ok else f'FAIL (ms={cs_acct.ms}, ci={cs_acct.ci}, ip={cs_acct.ip})'
    )

    # T29 — Per-season accounting: 5-year boundary triggers Generational Shift
    # season 20 = year 5 (20 / 4 = 5 years; 5 % 5 == 0); five-year boundary
    cs_5y = ClockState()
    ctx_5y = SeasonContext(
        season_number=20,
        clock_state=cs_5y,
        settlement_stats_by_id={},
        church_infra_by_id={},
        governor_state_by_id={},
        facility_state_by_id={},
        governance_transitions={},
        active_sieges={},
        church_mandate=3,
        inter_faction_battle_this_season=False,
    )
    report = per_season_accounting(ctx_5y)
    ok = (report.is_five_year_boundary
          and cs_5y.generational_shift == 1)
    r['T29_accounting_5yr_boundary_gen_shift'] = (
        'PASS' if ok else f'FAIL (5y_flag={report.is_five_year_boundary}, gs={cs_5y.generational_shift})'
    )

    # T30 — Per-season accounting: sieges surrender at Order 0
    from module_07_military import SiegeState as SiegeStateImport
    stats_siege = SS(prosperity=3, defense=3, order=1)
    siege = SiegeStateImport(settlement_id='S-001', attacker_faction='Hafenmark',
                              season_started=0)
    ctx_siege = SeasonContext(
        season_number=1,
        clock_state=ClockState(),
        settlement_stats_by_id={'S-001': stats_siege},
        church_infra_by_id={},
        governor_state_by_id={},
        facility_state_by_id={},
        governance_transitions={},
        active_sieges={'S-001': siege},
        church_mandate=3,
        inter_faction_battle_this_season=False,
    )
    report = per_season_accounting(ctx_siege)
    # season 1: siege ticks Order 1->0; surrender flag fires
    r['T30_accounting_siege_surrender'] = (
        'PASS' if 'S-001' in report.sieges_surrendered else f'FAIL ({report.sieges_surrendered})'
    )

    # T31 — Per-season accounting: unmanaged settlements decrement Order
    from module_05_governance import GovernorState as GS
    stats_unmgr = SS(prosperity=2, defense=2, order=3)
    gov_unmgr = GS(settlement_id='S-001', has_governor=False, current_order=3)
    ctx_unmgr = SeasonContext(
        season_number=1,
        clock_state=ClockState(),
        settlement_stats_by_id={'S-001': stats_unmgr},
        church_infra_by_id={},
        governor_state_by_id={'S-001': gov_unmgr},
        facility_state_by_id={},
        governance_transitions={},
        active_sieges={},
        church_mandate=3,
        inter_faction_battle_this_season=False,
    )
    report = per_season_accounting(ctx_unmgr)
    ok = (stats_unmgr.order == 2 and 'S-001' in report.unmanaged_settlements)
    r['T31_accounting_unmanaged_order_decrement'] = (
        'PASS' if ok else f'FAIL (order={stats_unmgr.order}, unmanaged={report.unmanaged_settlements})'
    )

    # T32 — Per-season accounting: emergent event firing composes
    # (Famine fires because settlement is at Prosperity 0)
    stats_famine = SS(prosperity=0, defense=2, order=3)
    ctx_fam = SeasonContext(
        season_number=1,
        clock_state=ClockState(),
        settlement_stats_by_id={'S-001': stats_famine},
        church_infra_by_id={},
        governor_state_by_id={},
        facility_state_by_id={},
        governance_transitions={},
        active_sieges={},
        church_mandate=3,
        inter_faction_battle_this_season=False,
    )
    report = per_season_accounting(ctx_fam)
    from module_06_events import SettlementEvent as SE
    famine_fired = any(fe.event == SE.FAMINE_ECONOMIC_COLLAPSE
                       for fe in report.fired_events)
    r['T32_accounting_emergent_events_compose'] = (
        'PASS' if famine_fired else f'FAIL ({report.fired_events})'
    )

    # T33 — Throughline coverage queryable
    ok = ('T-04' in THROUGHLINE_COVERAGE_BY_THIS_MODULE
          and 'PRIMARY' in THROUGHLINE_COVERAGE_BY_THIS_MODULE['T-04'])
    r['T33_throughline_coverage_T04_primary'] = 'PASS' if ok else 'FAIL'

    # T34 — Meta-throughline М-1 PRIMARY (closes M8 retroactive-audit gap)
    ok = ('М-1' in META_THROUGHLINE_COVERAGE_BY_THIS_MODULE
          and 'PRIMARY' in META_THROUGHLINE_COVERAGE_BY_THIS_MODULE['М-1'])
    r['T34_meta_m1_primary_closes_gap'] = 'PASS' if ok else 'FAIL'

    # T35 — Long-horizon emergent chain: full 30-year game simulation
    # of pressure-clock progression. Confirms § 7.1 30-year game canonical
    # numbers: MS ~42, IP ~80, generational shift reaches 6.
    cs_30y = ClockState()
    for season in range(1, 121):   # 120 seasons = 30 years
        ctx30 = SeasonContext(
            season_number=season,
            clock_state=cs_30y,
            settlement_stats_by_id={},
            church_infra_by_id={},
            governor_state_by_id={},
            facility_state_by_id={},
            governance_transitions={},
            active_sieges={},
            church_mandate=3,
            inter_faction_battle_this_season=False,
        )
        per_season_accounting(ctx30)
    # [canonical: §7.1 MS row — "30-year game = MS ~42 at game end (Fragile band)"]
    # MS starts 72, decays 1/year for 30 years → 72-30 = 42
    expected_ms_30y = 42
    # [canonical: §7.1 IP row — "30-year game: IP ~80 (Altonian preparation)"]
    # IP starts 20, +1/2 seasons over 120 seasons → 60 ticks → 20+60 = 80
    expected_ip_30y = 80
    # Generational Shift: 30 years / 5 = 6 ticks
    expected_gs_30y = 6
    ok = (cs_30y.ms == expected_ms_30y
          and cs_30y.ip == expected_ip_30y
          and cs_30y.generational_shift == expected_gs_30y)
    r['T35_30_year_canonical_simulation'] = (
        'PASS' if ok else f'FAIL (ms={cs_30y.ms}, ip={cs_30y.ip}, gs={cs_30y.generational_shift})'
    )

    # T36 — Emergent chain test crosses M3-M9: facility expansion → decade reset.
    # Run 40 seasons (10 years) and verify facility expansion cap resets.
    from module_03_facilities import FACILITY_TIERS as FT, _CAPACITY_BY_TYPE, FacilityState as FS
    facility = FS(
        settlement_id='S-001',
        capacity=dict(zip(FT, _CAPACITY_BY_TYPE['Seat'])),
        expansions_this_decade=1,   # already capped
    )
    cs_dec = ClockState()
    for season in range(1, 41):   # 40 seasons = 10 years (decade boundary at season 40)
        ctx_dec = SeasonContext(
            season_number=season,
            clock_state=cs_dec,
            settlement_stats_by_id={},
            church_infra_by_id={},
            governor_state_by_id={},
            facility_state_by_id={'S-001': facility},
            governance_transitions={},
            active_sieges={},
            church_mandate=3,
            inter_faction_battle_this_season=False,
        )
        per_season_accounting(ctx_dec)
    # After 40 seasons (10 years), decade boundary reset should fire
    r['T36_emergent_decade_reset'] = (
        'PASS' if facility.expansions_this_decade == 0
        else f'FAIL (expansions={facility.expansions_this_decade})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 09 — extended timeline + clocks — isolation tests"
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
    print(f"Clock substrate: MS {MS_START}->0 over time, CI {CI_START}->{CI_MAX}, IP {IP_START}->{IP_MAX}, Turmoil 0-{TURMOIL_MAX}")
    print(f"Generational Shift: +1 per {GENERATIONAL_SHIFT_YEARS_PER_TICK} years; thresholds at 2/4/6")
    print(f"Throughline coverage: {sorted(THROUGHLINE_COVERAGE_BY_THIS_MODULE.keys())}")
    print(f"Meta-throughline coverage: {sorted(META_THROUGHLINE_COVERAGE_BY_THIS_MODULE.keys())}")
    sys.exit(1 if fail else 0)
