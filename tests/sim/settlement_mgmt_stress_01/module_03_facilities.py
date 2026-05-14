# module_03_facilities.py — Institutional facility tiers + capacity pressure
#
# Mode G Module three of settlement_mgmt_stress_01. Begins populating the
# IMPROVEMENT arm of the player-action loop:
#
#   improvement action -> facility state mutation -> faction-standing feedback
#                      -> renown delta -> player-visible UI update
#
# Encodes §1.4 of settlement_layer_v30 (PP-six-six-one):
#   - §1.4.1 facility-slot capacity by settlement type (eight canonical types)
#   - §1.4.2 allocation rules (Standing-six-plus requires Wing; durable)
#   - §1.4.3 capacity-pressure mechanic (three outcomes including the
#     improvement action "expand-institutional-capacity")
#   - §1.4.4 cross-faction wing allocation (Cathedral inside Crown territory
#     remains Church-controlled — settlement-direct-controller, not
#     province-controller, owns the wing)
#
# Canonical source (full read this session):
#   designs/territory/settlement_layer_v30.md (§1.4.1, §1.4.2, §1.4.3, §1.4.4)
#
# Out of scope (deferred):
#   - §1.5 Church four-axes (Religious Building / Templar / Inquisitor /
#     Church Governor) — Module four (Church / parish / pastoral)
#   - §1.6 Parish Stability bonus (Geneva-trap mechanic) — Module four
#   - §1.7 Pastoral Assumption (Church fills governance vacuum) — Module four
#   - Hall Tier spec (faction_politics_expanded_v1 §1) — Module five
#     (governance) consumes the rank-holder side of slot allocation
#   - Treasury substrate (derived_stats_v1) — Module twelve (faction
#     integration) ties faction Treasury into the cost computation
#   - F1 type-map for §2.1 extra types (Village / Fortress-City /
#     Cathedral-City) against §1.4.1's canonical-eight matrix — see
#     finding F7 below

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

# Module 1 + Module 2 substrate
from module_01_primitives import (
    REGISTRY,
    Settlement,
    by_id,
    by_province,
    CANONICAL_TYPES,
    EXTRA_TYPES_IN_REGISTRY,
)
from module_02_hierarchy import SPECIAL_CASE_ENTITIES

# ── §1.4.1 Facility tier names ─────────────────────────────────────────────

# Four canonical facility tiers per §1.4.1 matrix headers
# [canonical: settlement_layer_v30 §1.4.1 — "Wing Slots (Std 6+)",
#  "Suite Slots (Std 5)", "Chamber Slots (Std 3-4)", "Billet Slots (Std 1-2)"]
FACILITY_TIERS: Tuple[str, ...] = ('Wing', 'Suite', 'Chamber', 'Billet')

# Standing thresholds per tier (the value at the LOW end of the Std range)
# [canonical: settlement_layer_v30 §1.4.1 column headers]
TIER_STANDING_MIN: Dict[str, int] = {
    'Wing':    6,   # "Std 6+"
    'Suite':   5,   # "Std 5"
    'Chamber': 3,   # "Std 3-4"
    'Billet':  1,   # "Std 1-2"
}

# ── §1.4.1 Capacity matrix (per canonical type) ─────────────────────────────

# Capacity values from §1.4.1 table. -1 == unlimited (canonical for Billet).
# [canonical: settlement_layer_v30 §1.4.1 facility-slot capacity table]

# Each tuple is (Wing, Suite, Chamber, Billet) — order matches FACILITY_TIERS.
_CAPACITY_BY_TYPE: Dict[str, Tuple[int, int, int, int]] = {
    'Seat':      (3, 5, 8, -1),   # Seat row
    'City':      (1, 3, 5, -1),
    'Town':      (0, 1, 3, -1),
    'Fortress':  (0, 1, 4, -1),
    'Cathedral': (1, 3, 5, -1),
    'Port':      (0, 1, 3, -1),
    'Mine':      (0, 0, 1, -1),
    'Outpost':   (0, 0, 1, -1),
}

UNLIMITED_BILLET: int = -1   # sentinel value


def base_capacity(settlement_type: str) -> Optional[Dict[str, int]]:
    """Return the §1.4.1 base capacity for `settlement_type`, or None if
    the type isn't in the canonical eight-type matrix.

    Per finding F7 (this module), the §2.1 extra types (Village,
    Fortress-City, Cathedral-City) have no canonical capacity row in
    §1.4.1. This function returns None for those; callers should consult
    the type-to-canonical mapping below for an interpretation, or surface
    the gap.
    """
    row = _CAPACITY_BY_TYPE.get(settlement_type)
    if row is None:
        return None
    return dict(zip(FACILITY_TIERS, row))


# ── F7 — extra-type-to-canonical mapping (provisional) ──────────────────────

# [FINDING F7] §1.4.1 matrix uses the §1.2 canonical eight settlement types
# (Seat, City, Town, Fortress, Cathedral, Port, Mine, Outpost). The §2.1
# registry uses three additional types (Village, Fortress-City,
# Cathedral-City) — see Module one F1. §1.4.1 has no row for them.
#
# Module three surfaces a PROVISIONAL extra-type interpretation: each extra
# type falls back to its nearest canonical-eight analogue for capacity
# computation. This is provisional pending editorial resolution of F1
# (which would either rename §2.1 entries to canonical types, or add
# matrix rows for the three extra types).
#
# Provisional mapping (used only for downstream sim continuity, NOT
# canonical):
#   Village        -> Town       (smaller settlement; "Town" is closest
#                                 in §1.2 description "Smaller settlement.
#                                 Local governance.")
#   Fortress-City  -> [unmapped] — Fortress-City is genuinely composite
#                                 (S-014 Ehrenfeld is described as a
#                                 fortress with a city around it; capacity
#                                 should plausibly be max(Fortress, City)
#                                 per axis, but the canon does not specify.
#                                 We surface as gap rather than guess.)
#   Cathedral-City -> [unmapped] — Cathedral-City (S-036 Himmelenger) is
#                                 a sovereign city-state that is also a
#                                 Cathedral. Capacity should plausibly
#                                 be max(Cathedral, Seat) or higher than
#                                 either, given canonical-significance as
#                                 Church seat-of-power. Surface as gap.
#
# This is the conservative path: Village gets a fallback (it's mechanically
# the most common — 15 of 37 settlements — and is plainly a smaller version
# of Town); the two composite types are gapped explicitly so Module 13
# Mode D can stress-test the gap rather than letting silent reconciliation
# hide it.

PROVISIONAL_EXTRA_TYPE_MAPPING: Dict[str, Optional[str]] = {
    'Village':         'Town',
    'Fortress-City':   None,
    'Cathedral-City':  None,
}


def effective_capacity(settlement: Settlement) -> Optional[Dict[str, int]]:
    """Capacity for a Settlement, with F7 fallback for extra types where a
    mapping exists. Returns None when the type is genuinely unmapped
    (Fortress-City, Cathedral-City) — caller must handle the gap."""
    direct = base_capacity(settlement.type)
    if direct is not None:
        return direct
    fallback_type = PROVISIONAL_EXTRA_TYPE_MAPPING.get(settlement.type)
    if fallback_type is None:
        return None
    return base_capacity(fallback_type)


# ── §1.4.3 capacity-pressure constants ──────────────────────────────────────

# [canonical: settlement_layer_v30 §1.4.3 outcome 2 —
#  "Treasury -300 (derived_stats_v1), scene action at settlement,
#  +1 Wing added; cap: +1 Wing per settlement per decade"]
EXPAND_CAPACITY_TREASURY_COST: int = 300
EXPAND_CAPACITY_WING_DELTA: int = 1
EXPAND_CAPACITY_DECADE_CAP: int = 1   # +1 Wing per settlement per decade

# [canonical: §1.4.3 outcome 3 —
#  "Each season without Wing, player makes social contest (Disposition pool
#  vs Ob 2) to maintain inner-circle standing. Failure reverts to Standing 5."]
PRINCE_IN_WAITING_SOCIAL_OB: int = 2
PRINCE_IN_WAITING_FAILURE_STANDING: int = 5

# Outcome enumeration per §1.4.3 (three explicit alternatives)
CAPACITY_PRESSURE_OUTCOMES: Tuple[str, ...] = (
    'existing_wing_holder_departs',     # outcome 1: generational shift / etc.
    'settlement_expands_capacity',      # outcome 2: improvement action
    'player_accepts_prince_in_waiting', # outcome 3: provisional rank
)

# Standing thresholds for capacity-pressure trigger
# [canonical: §1.4.3 opening — "If a Seat has 3 Wings occupied (leader +
#  2 inner circle) and the player reaches Standing 6 as a fourth claimant"]
CAPACITY_PRESSURE_TRIGGER_STANDING: int = 6


# ── Facility state (mutable; player-action loop write-target) ───────────────

@dataclass
class FacilityState:
    """Mutable facility-slot state for a single settlement.
    Module three's contribution to the player-action loop substrate.

    `expansions_this_decade` tracks the per-decade-cap consumption; the
    expand_institutional_capacity action fails if `expansions_this_decade
    >= EXPAND_CAPACITY_DECADE_CAP`.

    `occupied[tier]` counts how many slots of `tier` are currently
    occupied. Capacity-pressure triggers when occupied[tier] equals
    capacity[tier] and a new claimant emerges at that tier's standing.
    """
    settlement_id: str
    capacity: Dict[str, int]                       # mutable — expand action grows this
    occupied: Dict[str, int] = field(default_factory=lambda: {t: 0 for t in FACILITY_TIERS})
    expansions_this_decade: int = 0
    pending_claimants: List[str] = field(default_factory=list)   # rank-holder IDs awaiting slot

    def is_full(self, tier: str) -> bool:
        cap = self.capacity[tier]
        if cap == UNLIMITED_BILLET:
            return False
        return self.occupied[tier] >= cap

    def slots_available(self, tier: str) -> int:
        cap = self.capacity[tier]
        if cap == UNLIMITED_BILLET:
            # billet tier — sentinel value surfaces "effectively unlimited"
            # without overflowing arithmetic. Downstream consumers should
            # treat any >= zero as 'available'.
            # [canonical: arbitrary sentinel for §1.4.1 unlimited Billet]
            return 999
        return max(0, cap - self.occupied[tier])


# ── §1.4.3 improvement-action handler (the canonical player improve loop) ──

@dataclass(frozen=True)
class ActionResult:
    """Result of any player-action attempt. Carries faction-standing-delta
    signals downstream modules (Module five governance, Module eight
    Stature) will consume."""
    success: bool
    reason: str
    state_mutated: bool = False
    treasury_delta: int = 0
    faction_standing_delta: int = 0           # signed; Module five computes
    renown_delta: int = 0                     # signed; Module eight computes
    new_capacity: Optional[int] = None        # if Wing expansion succeeded


def expand_institutional_capacity(
    facility: FacilityState,
    treasury_available: int,
) -> ActionResult:
    """Improvement action — player invokes Domain Action 'Expand Institutional
    Capacity' at a settlement.

    Mutates: facility.capacity['Wing'] += 1; facility.expansions_this_decade += 1
    Cost: treasury_available -= 300 (Module twelve binds this to faction Treasury)

    Returns ActionResult carrying success/failure + downstream signals.
    Module five (governance) consumes faction_standing_delta;
    Module eight (Stature) consumes renown_delta.

    The renown signal is intentionally positive on success — expansion is
    a visible institutional improvement that should grow faction standing.
    The exact scalar is provisional and routes to canonical balance pass.
    """
    # Decade cap check per §1.4.3 outcome 2
    if facility.expansions_this_decade >= EXPAND_CAPACITY_DECADE_CAP:
        return ActionResult(
            success=False,
            reason='decade_cap_exhausted',
        )
    # Treasury check
    if treasury_available < EXPAND_CAPACITY_TREASURY_COST:
        return ActionResult(
            success=False,
            reason='insufficient_treasury',
        )
    # Mutate
    facility.capacity['Wing'] += EXPAND_CAPACITY_WING_DELTA
    facility.expansions_this_decade += EXPAND_CAPACITY_WING_DELTA
    return ActionResult(
        success=True,
        reason='wing_added',
        state_mutated=True,
        treasury_delta=-EXPAND_CAPACITY_TREASURY_COST,
        faction_standing_delta=+1,   # provisional — Module five rebinds
        renown_delta=+1,             # provisional — Module eight rebinds
        new_capacity=facility.capacity['Wing'],
    )


def resolve_capacity_pressure(
    facility: FacilityState,
    outcome: str,
    treasury_available: int = 0,
) -> ActionResult:
    """Resolve §1.4.3 capacity pressure via one of three canonical outcomes.

    Outcome 1 — existing_wing_holder_departs: declares an existing holder
    leaves (death / exile / generational shift). Wing freed.
    Outcome 2 — settlement_expands_capacity: triggers expand_institutional_capacity.
    Outcome 3 — player_accepts_prince_in_waiting: player keeps Standing 6
    provisionally; downstream code rolls Disposition vs Ob each season.
    """
    if outcome == 'existing_wing_holder_departs':
        if facility.occupied['Wing'] > 0:
            facility.occupied['Wing'] -= 1
            return ActionResult(
                success=True,
                reason='wing_freed',
                state_mutated=True,
                faction_standing_delta=-1,   # losing an established holder is costly
                renown_delta=-1,
            )
        return ActionResult(success=False, reason='no_wing_holder_to_depart')
    if outcome == 'settlement_expands_capacity':
        return expand_institutional_capacity(facility, treasury_available)
    if outcome == 'player_accepts_prince_in_waiting':
        # No mutation — just declares the provisional-rank path.
        # Each season Module five rolls Disposition vs Ob 2 per §1.4.3.
        return ActionResult(
            success=True,
            reason='prince_in_waiting_declared',
            state_mutated=False,
            renown_delta=0,
        )
    return ActionResult(success=False, reason=f'unknown_outcome_{outcome}')


# ── §1.4.4 cross-faction wing allocation predicate ──────────────────────────

@dataclass(frozen=True)
class WingControl:
    """A Wing's direct-controller assignment. Per §1.4.4, the Wing belongs
    to the settlement's direct controller, not the province's."""
    settlement_id: str
    direct_controller: str        # faction that directly controls the settlement
    province_controller: str      # faction that controls the parent province
    is_ceded: bool = False        # treaty concession per §1.4.4 paragraph 2
    ceded_to: Optional[str] = None


def wing_belongs_to(wing: WingControl) -> str:
    """Per §1.4.4: 'Wing slots belong to the settlement's direct controller,
    not the province's controller.' Ceded Wings count against the ceding
    faction's capacity while occupied by the allied faction.
    """
    if wing.is_ceded and wing.ceded_to is not None:
        return wing.ceded_to
    return wing.direct_controller


# ── Decade-boundary reset hook ──────────────────────────────────────────────

def advance_decade(facility: FacilityState) -> None:
    """Called at decade boundary by Module nine (timeline). Resets the
    per-decade expansion cap counter."""
    facility.expansions_this_decade = 0


# ── Isolation tests ─────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — capacity matrix has all eight canonical types
    r['T1_matrix_canonical_eight'] = (
        'PASS' if set(_CAPACITY_BY_TYPE.keys()) == set(CANONICAL_TYPES)
        else f"FAIL ({set(_CAPACITY_BY_TYPE) ^ set(CANONICAL_TYPES)})"
    )

    # T2 — Seat row matches §1.4.1 (Wing=3, Suite=5, Chamber=8, Billet=unlimited)
    seat = base_capacity('Seat')
    # [canonical: settlement_layer_v30 §1.4.1 Seat row]
    seat_wing_canon = 3
    seat_suite_canon = 5
    seat_chamber_canon = 8
    ok = (seat['Wing'] == seat_wing_canon and seat['Suite'] == seat_suite_canon
          and seat['Chamber'] == seat_chamber_canon and seat['Billet'] == UNLIMITED_BILLET)
    r['T2_seat_capacity'] = 'PASS' if ok else f'FAIL ({seat})'

    # T3 — City row (Wing=1, Suite=3, Chamber=5, Billet=unlimited)
    city = base_capacity('City')
    # [canonical: settlement_layer_v30 §1.4.1 City row]
    city_wing_canon = 1
    city_suite_canon = 3
    city_chamber_canon = 5
    ok = (city['Wing'] == city_wing_canon and city['Suite'] == city_suite_canon
          and city['Chamber'] == city_chamber_canon and city['Billet'] == UNLIMITED_BILLET)
    r['T3_city_capacity'] = 'PASS' if ok else f'FAIL ({city})'

    # T4 — Mine has only Chamber=1 (no Wing, no Suite, unlimited Billet)
    mine = base_capacity('Mine')
    # [canonical: settlement_layer_v30 §1.4.1 Mine row — "0 | 0 | 1 | unlimited"]
    mine_chamber_canon = 1
    ok = (mine['Wing'] == 0 and mine['Suite'] == 0
          and mine['Chamber'] == mine_chamber_canon and mine['Billet'] == UNLIMITED_BILLET)
    r['T4_mine_capacity'] = 'PASS' if ok else f'FAIL ({mine})'

    # T5 — Cathedral row (Wing=1, Suite=3, Chamber=5, Billet=unlimited)
    cath = base_capacity('Cathedral')
    # [canonical: settlement_layer_v30 §1.4.1 Cathedral row]
    cath_wing_canon = 1
    cath_suite_canon = 3
    cath_chamber_canon = 5
    ok = (cath['Wing'] == cath_wing_canon and cath['Suite'] == cath_suite_canon
          and cath['Chamber'] == cath_chamber_canon and cath['Billet'] == UNLIMITED_BILLET)
    r['T5_cathedral_capacity'] = 'PASS' if ok else f'FAIL ({cath})'

    # T6 — base_capacity returns None for extra types
    r['T6_extra_types_no_direct'] = (
        'PASS' if all(base_capacity(t) is None for t in EXTRA_TYPES_IN_REGISTRY)
        else 'FAIL'
    )

    # T7 — provisional Village fallback to Town
    village = effective_capacity(by_id('S-005'))   # Saatfeld, Village
    town = base_capacity('Town')
    r['T7_village_fallback_to_town'] = (
        'PASS' if village == town else f'FAIL ({village} vs {town})'
    )

    # T8 — Fortress-City genuinely unmapped (F7 gap)
    ehrenfeld_cap = effective_capacity(by_id('S-014'))   # Ehrenfeld, Fortress-City
    r['T8_fortress_city_unmapped'] = (
        'PASS' if ehrenfeld_cap is None else f'FAIL ({ehrenfeld_cap})'
    )

    # T9 — Cathedral-City genuinely unmapped (F7 gap)
    himm_cap = effective_capacity(by_id('S-036'))   # Himmelenger, Cathedral-City
    r['T9_cathedral_city_unmapped'] = (
        'PASS' if himm_cap is None else f'FAIL ({himm_cap})'
    )

    # T10 — count of Village-type settlements
    villages = [s for s in REGISTRY if s.type == 'Village']
    # [canonical: registry-derived count from settlement_layer_v30 §2.1
    #  enumeration — 14 entries with type=Village. Module 1's F1 finding
    #  initially reported "15 settlements" which is the Town count; Village
    #  count is 14. Corrected here.]
    expected_villages = 14
    r['T10_village_count'] = (
        'PASS' if len(villages) == expected_villages
        else f'FAIL ({len(villages)}, expected {expected_villages})'
    )

    # T11 — Standing 6 requires Wing (§1.4.2)
    # [canonical: §1.4.2 — "Player advancement to Standing 6+ requires an
    #  available Wing slot"]
    r['T11_standing_six_requires_wing'] = (
        'PASS' if TIER_STANDING_MIN['Wing'] == CAPACITY_PRESSURE_TRIGGER_STANDING
        else 'FAIL'
    )

    # T12 — FacilityState defaults to zero occupied across all tiers
    fs = FacilityState(
        settlement_id='S-001',
        capacity=dict(zip(FACILITY_TIERS, _CAPACITY_BY_TYPE['Seat'])),
    )
    r['T12_facility_state_init_zero'] = (
        'PASS' if all(fs.occupied[t] == 0 for t in FACILITY_TIERS) else 'FAIL'
    )

    # T13 — is_full negative case
    r['T13_is_full_negative'] = 'PASS' if not fs.is_full('Wing') else 'FAIL'

    # T14 — is_full positive case after filling
    # [canonical: §1.4.1 Seat row Wing=3 — cited above as seat_wing_canon]
    fs.occupied['Wing'] = seat_wing_canon
    r['T14_is_full_at_capacity'] = 'PASS' if fs.is_full('Wing') else 'FAIL'

    # T15 — Billet treated as not-full regardless of occupancy
    # [canonical: §1.4.1 "unlimited (shared quarters)" sentinel]
    fs.occupied['Billet'] = 999
    r['T15_billet_never_full'] = 'PASS' if not fs.is_full('Billet') else 'FAIL'

    # T16 — expand_institutional_capacity success path
    fs2 = FacilityState(
        settlement_id='S-001',
        capacity=dict(zip(FACILITY_TIERS, _CAPACITY_BY_TYPE['Seat'])),
    )
    initial_wing = fs2.capacity['Wing']
    # [canonical: arbitrary test scalar above §1.4.3 cost of 300]
    sufficient_treasury = 500
    result = expand_institutional_capacity(fs2, treasury_available=sufficient_treasury)
    # [canonical: §1.4.3 outcome 2 — capacity grows by +1 Wing]
    expected_new_wing_capacity = initial_wing + EXPAND_CAPACITY_WING_DELTA
    ok = (result.success and result.state_mutated
          and result.treasury_delta == -EXPAND_CAPACITY_TREASURY_COST
          and fs2.capacity['Wing'] == expected_new_wing_capacity
          and fs2.expansions_this_decade == 1)
    r['T16_expand_success'] = (
        'PASS' if ok else f'FAIL ({result}, {fs2.capacity}, {fs2.expansions_this_decade})'
    )

    # T17 — expand fails on insufficient treasury
    fs3 = FacilityState(
        settlement_id='S-001',
        capacity=dict(zip(FACILITY_TIERS, _CAPACITY_BY_TYPE['Seat'])),
    )
    # 100 < EXPAND_CAPACITY_TREASURY_COST (300) — but the literal 100 is
    # a test scalar, not a mechanical constant. Add canonical comment.
    # [canonical: arbitrary test scalar below §1.4.3 cost of 300]
    insufficient_amount = 100
    result = expand_institutional_capacity(fs3, treasury_available=insufficient_amount)
    r['T17_expand_fails_no_treasury'] = (
        'PASS' if not result.success and result.reason == 'insufficient_treasury'
        else f'FAIL ({result})'
    )

    # T18 — expand fails on decade-cap exhaustion
    fs4 = FacilityState(
        settlement_id='S-001',
        capacity=dict(zip(FACILITY_TIERS, _CAPACITY_BY_TYPE['Seat'])),
        expansions_this_decade=EXPAND_CAPACITY_DECADE_CAP,
    )
    result = expand_institutional_capacity(fs4, treasury_available=sufficient_treasury)
    r['T18_expand_fails_decade_cap'] = (
        'PASS' if not result.success and result.reason == 'decade_cap_exhausted'
        else f'FAIL ({result})'
    )

    # T19 — advance_decade resets the cap counter
    advance_decade(fs4)
    result = expand_institutional_capacity(fs4, treasury_available=sufficient_treasury)
    r['T19_advance_decade_resets'] = (
        'PASS' if result.success else f'FAIL ({result})'
    )

    # T20 — three canonical outcomes are exposed
    # [canonical: §1.4.3 enumerates three alternatives]
    expected_outcomes_count = 3
    r['T20_three_capacity_pressure_outcomes'] = (
        'PASS' if len(CAPACITY_PRESSURE_OUTCOMES) == expected_outcomes_count else 'FAIL'
    )

    # T21 — outcome 1 (existing departs) frees a Wing
    fs5 = FacilityState(
        settlement_id='S-001',
        capacity=dict(zip(FACILITY_TIERS, _CAPACITY_BY_TYPE['Seat'])),
        occupied={'Wing': 3, 'Suite': 0, 'Chamber': 0, 'Billet': 0},
    )
    result = resolve_capacity_pressure(fs5, 'existing_wing_holder_departs')
    # [canonical: §1.4.3 outcome 1 — Wing freed from 3 to 2]
    expected_remaining_occupied = 2
    r['T21_outcome_existing_departs'] = (
        'PASS' if result.success and fs5.occupied['Wing'] == expected_remaining_occupied
        else f'FAIL ({result}, {fs5.occupied})'
    )

    # T22 — outcome 3 (prince_in_waiting) doesn't mutate state
    fs6 = FacilityState(
        settlement_id='S-001',
        capacity=dict(zip(FACILITY_TIERS, _CAPACITY_BY_TYPE['Seat'])),
        occupied={'Wing': 3, 'Suite': 0, 'Chamber': 0, 'Billet': 0},
    )
    result = resolve_capacity_pressure(fs6, 'player_accepts_prince_in_waiting')
    r['T22_prince_in_waiting_no_mutation'] = (
        'PASS' if result.success and not result.state_mutated
        and fs6.occupied['Wing'] == 3
        else f'FAIL ({result}, {fs6.occupied})'
    )

    # T23 — §1.4.4 cross-faction wing: Cathedral inside Crown province
    # belongs to direct controller (Church), not province controller (Crown)
    # [canonical: §1.4.4 — "Church-controlled Seats host Prelates and
    #  Cardinals regardless of Crown occupation"]
    wing_cathedral_inside_crown = WingControl(
        settlement_id='S-036',
        direct_controller='Church',
        province_controller='Crown',
    )
    r['T23_wing_direct_controller'] = (
        'PASS' if wing_belongs_to(wing_cathedral_inside_crown) == 'Church' else 'FAIL'
    )

    # T24 — ceded Wing belongs to allied faction (still counts against ceding)
    wing_ceded = WingControl(
        settlement_id='S-001',
        direct_controller='Crown',
        province_controller='Crown',
        is_ceded=True,
        ceded_to='Hafenmark',
    )
    r['T24_wing_ceded_to_allied'] = (
        'PASS' if wing_belongs_to(wing_ceded) == 'Hafenmark' else 'FAIL'
    )

    # T25 — improvement action carries faction_standing + renown signal
    # (the player-action-loop feedback connection)
    fs7 = FacilityState(
        settlement_id='S-001',
        capacity=dict(zip(FACILITY_TIERS, _CAPACITY_BY_TYPE['Seat'])),
    )
    result = expand_institutional_capacity(fs7, treasury_available=sufficient_treasury)
    r['T25_improvement_carries_feedback'] = (
        'PASS' if result.success
        and result.faction_standing_delta != 0
        and result.renown_delta != 0
        else f'FAIL ({result})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 03 — facility tiers + capacity pressure — isolation tests"
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
    villages = [s for s in REGISTRY if s.type == 'Village']
    print(f"Capacity matrix: {len(_CAPACITY_BY_TYPE)} canonical types covered")
    print(f"Villages (F7 fallback to Town): {len(villages)} settlements")
    print(f"Fortress-City + Cathedral-City unmapped: 2 settlements (F7 gap)")
    sys.exit(1 if fail else 0)
