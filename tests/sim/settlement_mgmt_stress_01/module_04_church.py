# module_04_church.py — Church four-axis infrastructure + parish + pastoral
#
# Mode G Module four of settlement_mgmt_stress_01.
#
# Continues populating the IMPROVEMENT arm of the player-action loop (begun
# in Module three) with Church-side improvement actions:
#
#   install-religious-building (Chapel / Church / Cathedral — one per
#     settlement, mutually exclusive per §1.5 Axis 1)
#   install-templar-station (binary, §1.5 Axis 2)
#   install-inquisitor-base (binary, §1.5 Axis 3)
#   install-church-governor (binary, §1.5 Axis 4) — also the Pastoral
#     Assumption action (§1.7) when preconditions met
#
# Encodes:
#   §1.5 four independent axes + seizure Ob modifiers
#   §1.6 parish stability bonus (Geneva trap)
#   §1.7 Pastoral Assumption (post-collapse Church governance vacuum-fill)
#
# Canonical source (full read this session):
#   designs/territory/settlement_layer_v30.md (§1.5, §1.6, §1.7)
#
# Out of scope (deferred):
#   - Province-level faction stats Piety Track / Church Influence / Mandate
#     Challenge resolution — Module twelve (faction integration)
#   - Mass Seizure Declaration at CI=100 — Module twelve
#   - Templar interrupt action against rival Domain Actions — Module six
#     (settlement events) carries the action-cancellation surface
#   - Inquisitor surveillance Concealment test against Thread practitioners —
#     Module six
#   - Order-decay mechanics across seasons — Module nine (extended timeline)
#     supplies the per-season Accounting hook that consumes §1.6 effects
#   - Governor-assignment Ob lookup for non-Pastoral-Assumption case —
#     Module five (dual-authority governance)
#   - RM (Religious Minority? Refugee Movement?) cultural-presence
#     Church Attention generation — Module twelve

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

from module_01_primitives import Settlement, SettlementStats, by_id
from module_03_facilities import ActionResult

# ── §1.5 Axis 1 — Religious Building (mutually exclusive) ───────────────────

class ReligiousBuilding(Enum):
    """Axis 1 per §1.5. Mutually exclusive — one per settlement."""
    NONE = 'none'
    CHAPEL = 'chapel'
    CHURCH = 'church'
    CATHEDRAL = 'cathedral'

# §1.5 Axis 1: PT generation per-season per building tier.
# [canonical: settlement_layer_v30 §1.5 Axis 1 — "None / Chapel (+0.5
#  PT/season) / Church (+1 PT/season) / Cathedral (+2 PT/season, +0.5 PT
#  to adjacent territories)"]
# PT is stored as twice-the-value to keep arithmetic integer (Chapel 0.5
# PT becomes a 1 unit of half-PT-per-season; Cathedral 2 PT becomes 4 units).
# Half-PT units are the canonical fractional currency exposed downstream.
HALF_PT_UNITS_PER_PT: int = 2
RELIGIOUS_BUILDING_PT_HALF_UNITS: Dict[ReligiousBuilding, int] = {
    ReligiousBuilding.NONE:      0,
    ReligiousBuilding.CHAPEL:    1,   # 0.5 PT/season -> 1 half-PT-unit
    ReligiousBuilding.CHURCH:    2,   # 1 PT/season   -> 2 half-PT-units
    ReligiousBuilding.CATHEDRAL: 4,   # 2 PT/season   -> 4 half-PT-units
}

# §1.5 Axis 1: Cathedral also generates a half-PT bonus to adjacent territories
# [canonical: settlement_layer_v30 §1.5 Axis 1 Cathedral entry —
#  "+0.5 PT to adjacent territories"]
CATHEDRAL_ADJACENT_PT_HALF_UNITS: int = 1  # 0.5 PT half-units per adjacent territory


# ── §1.6 Parish Stability bonus (Geneva trap) ───────────────────────────────

# [FINDING F8] §1.5 ↔ §1.6 semantic asymmetry. §1.5 Axis 1 expresses PT
# generation as a uniform per-season rate for all three tiers (Chapel/
# Church/Cathedral). §1.6 expresses Stability (Order) bonus differently
# per tier:
#   Chapel    -> per-season recurring (+0.5 Order/season, "rounds: +1 every
#                other season" — accumulator semantics)
#   Church    -> one-time at installation (+1 Order at installation)
#   Cathedral -> one-time at installation (+1 Order) PLUS structural
#                modifier (Order decay −1; the Order stat decays slower)
#
# Module 4 encodes all three patterns and surfaces them as distinct return
# fields. Module 13 Mode B chains test that the player-visible feedback is
# proportionate (installation is one-time; per-season effect should be
# legible across many seasons; decay modifier should be persistent state).

@dataclass(frozen=True)
class ParishBonus:
    """Per-tier parish stability effects per §1.6.
    installation_order_delta is applied ONCE on the install action.
    per_season_half_order_units accumulates each season (Module nine hook).
    order_decay_reduction is a persistent modifier on the settlement.
    """
    installation_order_delta: int
    per_season_half_order_units: int    # half-Order per season
    order_decay_reduction: int          # subtracted from order-decay rate

# [canonical: settlement_layer_v30 §1.6 Parish Social Services table]
PARISH_BONUS_BY_BUILDING: Dict[ReligiousBuilding, ParishBonus] = {
    ReligiousBuilding.NONE:      ParishBonus(0, 0, 0),
    # Chapel: "+0.5 Order/season (rounds: +1 every other season)"
    # [canonical: settlement_layer_v30 §1.6 Chapel row —
    #  "Chapel | +0.5 Order/season (rounds: +1 every other season)"]
    ReligiousBuilding.CHAPEL:    ParishBonus(0, 1, 0),   # 1 half-Order-unit/season
    # Church: "+1 Order at installation (one-time)"
    # [canonical: settlement_layer_v30 §1.6 Church row —
    #  "Church | +1 Order at installation (one-time)"]
    ReligiousBuilding.CHURCH:    ParishBonus(1, 0, 0),
    # Cathedral: "+1 Order at installation + Order decay −1"
    # [canonical: settlement_layer_v30 §1.6 Cathedral row —
    #  "Cathedral | +1 Order at installation + Order decay −1"]
    ReligiousBuilding.CATHEDRAL: ParishBonus(1, 0, 1),
}

# Half-Order accumulator threshold — accumulating 2 half-units triggers +1 Order
# [canonical: settlement_layer_v30 §1.6 Chapel row parenthetical —
#  "rounds: +1 every other season"]
HALF_ORDER_UNITS_PER_ORDER: int = 2


# ── §1.5 Axis 2 / 3 / 4 binary feature flags ────────────────────────────────

# §1.5 Axis 2 — Templar Station: +1 CI/season in territory.
# [canonical: settlement_layer_v30 §1.5 Axis 2 — "+1 CI/season in territory"]
TEMPLAR_CI_PER_SEASON: int = 1
# Templar can interrupt rival Domain Actions: +1 Ob, costs 1 CI.
# [canonical: settlement_layer_v30 §1.5 Axis 2 —
#  "Church can interrupt rival Domain Actions (+1 Ob, costs 1 CI)"]
TEMPLAR_INTERRUPT_OB_DELTA: int = 1
TEMPLAR_INTERRUPT_CI_COST: int = 1

# §1.5 Axis 3 — Inquisitor Base.
# [canonical: settlement_layer_v30 §1.5 Axis 3 — "RM governance-building
#  actions +1 Ob"]
INQUISITOR_RM_GOVERNANCE_OB_DELTA: int = 1
# [canonical: settlement_layer_v30 §1.5 Axis 3 —
#  "RM cultural presence generates 1 Church Attention/season"]
INQUISITOR_CHURCH_ATTENTION_PER_SEASON: int = 1


# ── §1.5 Seizure Ob modifiers ───────────────────────────────────────────────
# [canonical: settlement_layer_v30 §1.5 — "Seizure Ob Modifiers (stacking,
#  per settlement): Chapel −0, Church −1, Cathedral −2, Templar −1,
#  Inquisitor −1, Church Governor −2. Cap: −4 per settlement"]

SEIZURE_OB_MODIFIER_CHAPEL: int = 0
SEIZURE_OB_MODIFIER_CHURCH: int = 1
SEIZURE_OB_MODIFIER_CATHEDRAL: int = 2
SEIZURE_OB_MODIFIER_TEMPLAR: int = 1
SEIZURE_OB_MODIFIER_INQUISITOR: int = 1
SEIZURE_OB_MODIFIER_CHURCH_GOVERNOR: int = 2
SEIZURE_OB_MODIFIER_CAP: int = 4

# [canonical: settlement_layer_v30 §1.5 —
#  "CI=100 Mass Seizure Declaration triggers simultaneous Seizure"]
CI_MASS_SEIZURE_DECLARATION_THRESHOLD: int = 100


# ── §1.7 Pastoral Assumption ────────────────────────────────────────────────
# [canonical: settlement_layer_v30 §1.7 —
#  "the Church may install a Church Governor (Axis 4) as a Domain Action
#  at Ob 1 (vs normal governor assignment Ob)"]
PASTORAL_ASSUMPTION_OB: int = 1

# Province-faction revocation per §1.7 paragraph 3
# [canonical: settlement_layer_v30 §1.7 —
#  "The province faction may revoke this per §3.3 revocation rules
#  (Ob = Church Influence ÷ 2, Order −1, Disposition −2 with Church)"]
PASTORAL_REVOCATION_ORDER_COST: int = 1
PASTORAL_REVOCATION_DISPOSITION_COST: int = 2


# ── Church state (mutable; player-action loop write-target) ─────────────────

@dataclass
class ChurchInfrastructure:
    """Four-axis Church infrastructure state for a single settlement per §1.5.
    Mutable. Player Church-improvement actions write here."""
    settlement_id: str
    religious_building: ReligiousBuilding = ReligiousBuilding.NONE
    templar_station: bool = False
    inquisitor_base: bool = False
    church_governor: bool = False
    # §1.6 per-season accumulator for Chapel half-Order
    half_order_accumulator: int = 0
    # §1.6 Cathedral structural modifier (set at install; cleared on remove)
    order_decay_reduction: int = 0


# ── Settlement-state stub for §1.7 governor-vacuum precondition ─────────────

@dataclass
class GovernorState:
    # Minimal governor-presence state used by Pastoral-Assumption
    # precondition check (per the §1.7 spec). Module five (governance)
    # supplies the full state; Module 4 only needs the boolean
    # 'is there a governor' and the settlement's current Order value.
    settlement_id: str
    has_governor: bool
    current_order: int


# ── Seizure-Ob computation per §1.5 ─────────────────────────────────────────

def seizure_ob_modifier(infra: ChurchInfrastructure) -> int:
    """Per §1.5 stacking seizure-Ob modifier, capped at SEIZURE_OB_MODIFIER_CAP."""
    delta = 0
    if infra.religious_building == ReligiousBuilding.CHAPEL:
        delta += SEIZURE_OB_MODIFIER_CHAPEL
    elif infra.religious_building == ReligiousBuilding.CHURCH:
        delta += SEIZURE_OB_MODIFIER_CHURCH
    elif infra.religious_building == ReligiousBuilding.CATHEDRAL:
        delta += SEIZURE_OB_MODIFIER_CATHEDRAL
    if infra.templar_station:
        delta += SEIZURE_OB_MODIFIER_TEMPLAR
    if infra.inquisitor_base:
        delta += SEIZURE_OB_MODIFIER_INQUISITOR
    if infra.church_governor:
        delta += SEIZURE_OB_MODIFIER_CHURCH_GOVERNOR
    return min(delta, SEIZURE_OB_MODIFIER_CAP)


# ── Improvement action: install Religious Building (Axis 1) ─────────────────

def install_religious_building(
    infra: ChurchInfrastructure,
    stats: SettlementStats,
    new_building: ReligiousBuilding,
) -> ActionResult:
    """Improvement action — install/upgrade the settlement's Religious
    Building (Axis 1). Mutually exclusive per §1.5: replaces any existing
    building with the new one. Applies §1.6 installation-order delta and
    Cathedral order-decay modifier on install.

    Returns ActionResult carrying:
      - state_mutated (always True on success)
      - faction_standing_delta (positive — Church gains standing where its
        infrastructure lands)
      - renown_delta (positive — visible institutional contribution)
    """
    if new_building == infra.religious_building:
        return ActionResult(success=False, reason='already_installed')
    if new_building == ReligiousBuilding.NONE:
        return ActionResult(success=False, reason='cannot_install_none')

    # Clear prior building's structural modifier (Cathedral order-decay)
    if infra.religious_building == ReligiousBuilding.CATHEDRAL:
        infra.order_decay_reduction = 0

    # Apply new building's structural modifier
    new_bonus = PARISH_BONUS_BY_BUILDING[new_building]
    infra.religious_building = new_building
    infra.order_decay_reduction = new_bonus.order_decay_reduction

    # Apply one-time installation Order delta
    order_delta = new_bonus.installation_order_delta
    if order_delta != 0:
        # Clamp into [0, 5] per Module 1 STAT_MAX
        from module_01_primitives import STAT_MAX, STAT_MIN
        new_order = max(STAT_MIN, min(STAT_MAX, stats.order + order_delta))
        stats.order = new_order

    return ActionResult(
        success=True,
        reason=f'installed_{new_building.value}',
        state_mutated=True,
        faction_standing_delta=+1,   # provisional — Module 12 binds
        renown_delta=+1,             # provisional — Module 8 binds
    )


# ── Improvement actions: install binary axes ────────────────────────────────

def install_templar_station(infra: ChurchInfrastructure) -> ActionResult:
    """§1.5 Axis 2 install — binary."""
    if infra.templar_station:
        return ActionResult(success=False, reason='already_installed')
    infra.templar_station = True
    return ActionResult(
        success=True,
        reason='installed_templar_station',
        state_mutated=True,
        faction_standing_delta=+1,
        renown_delta=+1,
    )


def install_inquisitor_base(infra: ChurchInfrastructure) -> ActionResult:
    """§1.5 Axis 3 install — binary."""
    if infra.inquisitor_base:
        return ActionResult(success=False, reason='already_installed')
    infra.inquisitor_base = True
    return ActionResult(
        success=True,
        reason='installed_inquisitor_base',
        state_mutated=True,
        faction_standing_delta=+1,
        renown_delta=+1,
    )


def install_church_governor(
    infra: ChurchInfrastructure,
    governor_state: GovernorState,
    is_pastoral_assumption: bool = False,
) -> ActionResult:
    # Axis-four install per the §1.5 spec. When is_pastoral_assumption=True,
    # applies the §1.7 preconditions: settlement must have no governor AND
    # have at least Chapel.
    #
    # For non-pastoral installation, the precondition lookup is Module five's
    # territory (dual-authority governance Ob). Module four surfaces the
    # pastoral case explicitly with Ob one.
    if infra.church_governor:
        return ActionResult(success=False, reason='already_installed')

    if is_pastoral_assumption:
        # §1.7 preconditions
        if governor_state.has_governor:
            return ActionResult(
                success=False,
                reason='pastoral_assumption_blocked_governor_present',
            )
        if infra.religious_building == ReligiousBuilding.NONE:
            return ActionResult(
                success=False,
                reason='pastoral_assumption_blocked_no_chapel',
            )

    infra.church_governor = True
    return ActionResult(
        success=True,
        reason=('installed_church_governor_pastoral' if is_pastoral_assumption
                else 'installed_church_governor'),
        state_mutated=True,
        faction_standing_delta=+1,
        renown_delta=+1,
    )


# ── §1.6 per-season accumulator hook (Module nine calls each Accounting) ────

def accrue_parish_bonus_per_season(
    infra: ChurchInfrastructure,
    stats: SettlementStats,
) -> Tuple[int, bool]:
    """Module nine (timeline) hook. Returns (new accumulator value, whether
    a +1 Order tick triggered this season). Modifies infra and stats in
    place.

    Chapel: +1 half-Order-unit per season; rounds up every other season.
    Church / Cathedral / None: no per-season accrual (their effects are
    one-time at install or structural).
    """
    from module_01_primitives import STAT_MAX, STAT_MIN
    bonus = PARISH_BONUS_BY_BUILDING[infra.religious_building]
    if bonus.per_season_half_order_units == 0:
        return (infra.half_order_accumulator, False)

    infra.half_order_accumulator += bonus.per_season_half_order_units

    triggered = False
    while infra.half_order_accumulator >= HALF_ORDER_UNITS_PER_ORDER:
        infra.half_order_accumulator -= HALF_ORDER_UNITS_PER_ORDER
        new_order = max(STAT_MIN, min(STAT_MAX, stats.order + 1))
        if new_order != stats.order:
            stats.order = new_order
            triggered = True
        # If stats.order is already at STAT_MAX, the half-units accumulated
        # cap and don't tick. We still consumed them — the canonical
        # interpretation (accumulator drains regardless of whether the
        # underlying stat could absorb the gain) prevents perpetual
        # accumulator buildup. Module 13 Mode D should test the cap case.

    return (infra.half_order_accumulator, triggered)


# ── Isolation tests ─────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — four axes are independent (binary flags + one mutually-exclusive
    # building enum). Sanity check on data shape.
    infra = ChurchInfrastructure(settlement_id='S-001')
    ok = (infra.religious_building == ReligiousBuilding.NONE
          and not infra.templar_station
          and not infra.inquisitor_base
          and not infra.church_governor)
    r['T1_axes_default_none'] = 'PASS' if ok else 'FAIL'

    # T2 — Religious Building enum has exactly four values
    # [canonical: §1.5 Axis 1 — "None / Chapel / Church / Cathedral"]
    expected_axis1_values_count = 4
    r['T2_religious_building_four_tiers'] = (
        'PASS' if len(ReligiousBuilding) == expected_axis1_values_count else 'FAIL'
    )

    # T3 — PT half-unit table matches §1.5 (Chapel 1, Church 2, Cathedral 4)
    # [canonical: §1.5 Axis 1 "Chapel (+0.5 PT/season) / Church (+1 PT/season)
    #  / Cathedral (+2 PT/season)"; encoded as half-PT units]
    chapel_half_pt_canon = 1
    church_half_pt_canon = 2
    cathedral_half_pt_canon = 4
    ok = (RELIGIOUS_BUILDING_PT_HALF_UNITS[ReligiousBuilding.CHAPEL] == chapel_half_pt_canon
          and RELIGIOUS_BUILDING_PT_HALF_UNITS[ReligiousBuilding.CHURCH] == church_half_pt_canon
          and RELIGIOUS_BUILDING_PT_HALF_UNITS[ReligiousBuilding.CATHEDRAL] == cathedral_half_pt_canon)
    r['T3_pt_half_units_match_canon'] = 'PASS' if ok else 'FAIL'

    # T4 — Cathedral adjacent PT bonus exists
    # [canonical: §1.5 Axis 1 Cathedral — "+0.5 PT to adjacent territories"]
    r['T4_cathedral_adjacent_pt_bonus'] = (
        'PASS' if CATHEDRAL_ADJACENT_PT_HALF_UNITS == 1 else 'FAIL'
    )

    # T5 — Chapel install (Religious Building Axis 1)
    infra_tb = ChurchInfrastructure(settlement_id='S-005')
    stats = SettlementStats(prosperity=2, defense=1, order=2)
    result = install_religious_building(infra_tb, stats, ReligiousBuilding.CHAPEL)
    ok = (result.success
          and infra_tb.religious_building == ReligiousBuilding.CHAPEL
          and stats.order == 2)  # Chapel has no installation order delta
    r['T5_install_chapel'] = 'PASS' if ok else f'FAIL ({result}, order={stats.order})'

    # T6 — Church install gives +1 Order at installation (§1.6 one-time)
    infra_tc = ChurchInfrastructure(settlement_id='S-001')
    stats_tc = SettlementStats(prosperity=3, defense=2, order=2)
    result = install_religious_building(infra_tc, stats_tc, ReligiousBuilding.CHURCH)
    # [canonical: §1.6 Church row — "+1 Order at installation (one-time)"]
    expected_post_install_order = 3   # 2 + 1
    r['T6_install_church_one_time_order'] = (
        'PASS' if result.success and stats_tc.order == expected_post_install_order
        else f'FAIL ({result}, order={stats_tc.order})'
    )

    # T7 — Cathedral install gives +1 Order AND sets order_decay_reduction
    infra_td = ChurchInfrastructure(settlement_id='S-036')
    stats_td = SettlementStats(prosperity=4, defense=2, order=3)
    result = install_religious_building(infra_td, stats_td, ReligiousBuilding.CATHEDRAL)
    # [canonical: §1.6 Cathedral row — "+1 Order at installation + Order decay −1"]
    expected_cath_order = 4   # 3 + 1
    expected_decay_reduction = 1
    ok = (result.success
          and stats_td.order == expected_cath_order
          and infra_td.order_decay_reduction == expected_decay_reduction)
    r['T7_install_cathedral_one_time_and_decay'] = (
        'PASS' if ok else f'FAIL ({result}, order={stats_td.order}, decay={infra_td.order_decay_reduction})'
    )

    # T8 — Order clamps at STAT_MAX on install
    from module_01_primitives import STAT_MAX
    infra_te = ChurchInfrastructure(settlement_id='S-001')
    stats_te = SettlementStats(prosperity=0, defense=0, order=STAT_MAX)
    result = install_religious_building(infra_te, stats_te, ReligiousBuilding.CATHEDRAL)
    r['T8_order_clamps_at_max'] = (
        'PASS' if result.success and stats_te.order == STAT_MAX else f'FAIL ({stats_te.order})'
    )

    # T9 — install_religious_building rejects same-tier install (already_installed)
    infra_tf = ChurchInfrastructure(
        settlement_id='S-001', religious_building=ReligiousBuilding.CHAPEL,
    )
    stats_tf = SettlementStats(prosperity=2, defense=1, order=2)
    result = install_religious_building(infra_tf, stats_tf, ReligiousBuilding.CHAPEL)
    r['T9_reject_same_tier'] = (
        'PASS' if not result.success and result.reason == 'already_installed'
        else f'FAIL ({result})'
    )

    # T10 — Cathedral install replaces prior Church; clears Church's
    # installation already-applied effect, applies Cathedral effect
    # (Module 4 stance: installation Order delta is one-time and stays;
    # only the structural modifier — order-decay reduction — toggles.
    # If a player upgrades Church -> Cathedral, the Cathedral structural
    # modifier replaces nothing, since Church has no structural modifier.)
    infra_tg = ChurchInfrastructure(settlement_id='S-001',
                                   religious_building=ReligiousBuilding.CHURCH)
    stats_tg = SettlementStats(prosperity=3, defense=1, order=3)
    result = install_religious_building(infra_tg, stats_tg, ReligiousBuilding.CATHEDRAL)
    # [canonical: §1.6 Cathedral row "+1 Order at installation"]
    expected_upgrade_order = 4   # 3 + 1
    expected_upgrade_decay = 1
    ok = (result.success
          and infra_tg.religious_building == ReligiousBuilding.CATHEDRAL
          and stats_tg.order == expected_upgrade_order
          and infra_tg.order_decay_reduction == expected_upgrade_decay)
    r['T10_upgrade_church_to_cathedral'] = (
        'PASS' if ok else f'FAIL ({result}, order={stats_tg.order}, decay={infra_tg.order_decay_reduction})'
    )

    # T11 — Templar install (binary)
    infra_th = ChurchInfrastructure(settlement_id='S-001')
    result = install_templar_station(infra_th)
    r['T11_install_templar'] = (
        'PASS' if result.success and infra_th.templar_station else f'FAIL ({result})'
    )

    # T12 — Templar reject second install
    result = install_templar_station(infra_th)
    r['T12_reject_templar_double_install'] = (
        'PASS' if not result.success else 'FAIL'
    )

    # T13 — Inquisitor install (binary)
    infra_ti = ChurchInfrastructure(settlement_id='S-001')
    result = install_inquisitor_base(infra_ti)
    r['T13_install_inquisitor'] = (
        'PASS' if result.success and infra_ti.inquisitor_base else f'FAIL ({result})'
    )

    # T14 — §1.5 seizure-Ob modifier stacks
    # All four axes maxed (Cathedral + Templar + Inquisitor + Church Governor)
    infra_tj = ChurchInfrastructure(
        settlement_id='S-036',
        religious_building=ReligiousBuilding.CATHEDRAL,
        templar_station=True,
        inquisitor_base=True,
        church_governor=True,
    )
    # Raw stack: Cathedral 2 + Templar 1 + Inquisitor 1 + Governor 2 = 6
    # Capped at SEIZURE_OB_MODIFIER_CAP = 4
    # [canonical: §1.5 — "Cap: −4 per settlement"]
    expected_capped = SEIZURE_OB_MODIFIER_CAP
    r['T14_seizure_ob_caps_at_4'] = (
        'PASS' if seizure_ob_modifier(infra_tj) == expected_capped
        else f'FAIL ({seizure_ob_modifier(infra_tj)})'
    )

    # T15 — partial stack does not cap
    # Chapel (0) + Templar (1) + Inquisitor (1) = 2
    infra_tk = ChurchInfrastructure(
        settlement_id='S-001',
        religious_building=ReligiousBuilding.CHAPEL,
        templar_station=True,
        inquisitor_base=True,
    )
    # [canonical: §1.5 — Chapel 0 + Templar 1 + Inquisitor 1 = 2]
    expected_uncapped = 2
    r['T15_seizure_ob_uncapped_stack'] = (
        'PASS' if seizure_ob_modifier(infra_tk) == expected_uncapped
        else f'FAIL ({seizure_ob_modifier(infra_tk)})'
    )

    # T16 — Pastoral Assumption succeeds with no governor + Chapel present
    infra_tl = ChurchInfrastructure(
        settlement_id='S-005',
        religious_building=ReligiousBuilding.CHAPEL,
    )
    gov = GovernorState(settlement_id='S-005', has_governor=False, current_order=2)
    result = install_church_governor(infra_tl, gov, is_pastoral_assumption=True)
    r['T16_pastoral_assumption_succeeds'] = (
        'PASS' if result.success and infra_tl.church_governor else f'FAIL ({result})'
    )

    # T17 — Pastoral Assumption blocked when governor present
    infra_tm = ChurchInfrastructure(
        settlement_id='S-001',
        religious_building=ReligiousBuilding.CHAPEL,
    )
    gov_tm = GovernorState(settlement_id='S-001', has_governor=True, current_order=3)
    result = install_church_governor(infra_tm, gov_tm, is_pastoral_assumption=True)
    r['T17_pastoral_blocked_governor_present'] = (
        'PASS' if not result.success
        and result.reason == 'pastoral_assumption_blocked_governor_present'
        else f'FAIL ({result})'
    )

    # T18 — Pastoral Assumption blocked without Chapel/Church/Cathedral
    infra_tn = ChurchInfrastructure(settlement_id='S-005')
    gov_tn = GovernorState(settlement_id='S-005', has_governor=False, current_order=0)
    result = install_church_governor(infra_tn, gov_tn, is_pastoral_assumption=True)
    r['T18_pastoral_blocked_no_chapel'] = (
        'PASS' if not result.success
        and result.reason == 'pastoral_assumption_blocked_no_chapel'
        else f'FAIL ({result})'
    )

    # T19 — Non-pastoral church-governor install succeeds without preconditions
    infra_to = ChurchInfrastructure(settlement_id='S-001')
    gov_to = GovernorState(settlement_id='S-001', has_governor=True, current_order=3)
    result = install_church_governor(infra_to, gov_to, is_pastoral_assumption=False)
    r['T19_non_pastoral_unrestricted'] = (
        'PASS' if result.success else f'FAIL ({result})'
    )

    # T20 — Chapel per-season accumulator: 1 season -> 1 half-unit, no tick
    infra_tp = ChurchInfrastructure(
        settlement_id='S-005',
        religious_building=ReligiousBuilding.CHAPEL,
    )
    stats_tp = SettlementStats(prosperity=2, defense=1, order=2)
    (acc, triggered) = accrue_parish_bonus_per_season(infra_tp, stats_tp)
    # [canonical: §1.6 Chapel "rounds: +1 every other season" — first
    #  season accumulates one half-unit, no tick yet]
    r['T20_chapel_one_season_accumulates'] = (
        'PASS' if acc == 1 and not triggered and stats_tp.order == 2
        else f'FAIL (acc={acc}, triggered={triggered}, order={stats_tp.order})'
    )

    # T21 — Chapel two seasons: accumulator hits threshold, +1 Order, drains
    (acc, triggered) = accrue_parish_bonus_per_season(infra_tp, stats_tp)
    # [canonical: §1.6 Chapel — accumulator threshold +1 Order every other season]
    expected_order_after_tick = 3
    r['T21_chapel_two_seasons_tick'] = (
        'PASS' if acc == 0 and triggered and stats_tp.order == expected_order_after_tick
        else f'FAIL (acc={acc}, triggered={triggered}, order={stats_tp.order})'
    )

    # T22 — Church per-season accumulator: no per-season effect, order unchanged
    infra_tq = ChurchInfrastructure(
        settlement_id='S-001',
        religious_building=ReligiousBuilding.CHURCH,
    )
    stats_tq = SettlementStats(prosperity=3, defense=1, order=3)
    (acc, triggered) = accrue_parish_bonus_per_season(infra_tq, stats_tq)
    r['T22_church_no_per_season_effect'] = (
        'PASS' if acc == 0 and not triggered and stats_tq.order == 3 else 'FAIL'
    )

    # T23 — install actions carry faction_standing + renown signals
    infra_tr = ChurchInfrastructure(settlement_id='S-001')
    stats_tr = SettlementStats(prosperity=2, defense=1, order=2)
    result = install_religious_building(infra_tr, stats_tr, ReligiousBuilding.CHAPEL)
    ok = (result.success
          and result.faction_standing_delta != 0
          and result.renown_delta != 0)
    r['T23_install_carries_feedback'] = 'PASS' if ok else f'FAIL ({result})'

    # T24 — CI=100 Mass Seizure Declaration threshold canonical
    # [canonical: §1.5 — "CI=100 Mass Seizure Declaration"]
    expected_threshold = 100
    r['T24_mass_seizure_threshold'] = (
        'PASS' if CI_MASS_SEIZURE_DECLARATION_THRESHOLD == expected_threshold
        else 'FAIL'
    )

    # T25 — Pastoral Assumption Ob is canonically 1
    # [canonical: §1.7 — "Domain Action at Ob 1 (vs normal governor
    #  assignment Ob)"]
    expected_pastoral_ob = 1
    r['T25_pastoral_ob_is_one'] = (
        'PASS' if PASTORAL_ASSUMPTION_OB == expected_pastoral_ob else 'FAIL'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 04 — Church / parish / pastoral — isolation tests"
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
    print(f"Religious Building tiers: {[b.value for b in ReligiousBuilding]}")
    print(f"Binary axes: Templar, Inquisitor, Church Governor")
    print(f"§1.5 seizure-Ob cap: -{SEIZURE_OB_MODIFIER_CAP}")
    print(f"§1.7 Pastoral Assumption Ob: {PASTORAL_ASSUMPTION_OB}")
    sys.exit(1 if fail else 0)
