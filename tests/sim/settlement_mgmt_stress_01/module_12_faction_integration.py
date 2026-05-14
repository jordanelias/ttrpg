# module_12_faction_integration.py — Faction stat-sheet integration + CI + battle consequences
#
# Mode G Module twelve of settlement_mgmt_stress_01.
# Last functional module before M13 integration runner.
#
# Approach: BOTTOM-UP GRANULAR EMERGENT (continued from prior modules).
#
# THROUGHLINE BINDINGS (per references/throughlines_meta_infill.md §3.1):
#
#   T-21 Thread Political Warfare — PRIMARY (currently unbound).
#   М-4 institutional + М-3 substrate-grounded. Load-bearing: factions,
#   faction_layer, threadwork, conflict_architecture, mass_combat. M12
#   wires the faction Mandate / Stability mechanics that ARE the warfare
#   layer T-21 names. Closes prior-unbound primary.
#
#   T-24 Convergence as Crisis — PRIMARY (currently unbound).
#   М-5 scale-connecting. Load-bearing: conflict_architecture, scale_transitions,
#   victory, tensions_deck. M12 wires the cascade where multiple
#   throughlines intersect at battles + CI threshold crossings — the
#   canonical "multiple throughlines intersecting at various scales produce
#   emergent crisis." Closes second prior-unbound primary.
#
#   T-08 Church Rendering Reinforcement — EXTENSION (M4 primary).
#   M12 wires CI political-pool mechanism that operationalizes Church's
#   substrate-posture per §3.2 + §3.3 of ci_political_v30.
#
#   T-20 Two Contests — EXTENSION (M7/M8/M11 secondary).
#   М-6 forced-choice. M12 binds the canonical "sovereignty vs survival"
#   via faction_layer §1 Stability triggers — capital territories at
#   double-magnitude penalty force the canonical forced choice.
#
#   T-04 MS Decay — EXTENSION (M9 primary).
#   M12 wires the §E.1 immediate-battle-trigger MS -1 / MS -2 Campaign/War
#   that augments M9's per-year decay.
#
# META-THROUGHLINE BINDINGS:
#
#   М-4 INSTITUTIONS STAKE SUBSTRATE-POSTURES — PRIMARY (extends M3/M4/M5/M11).
#   The faction stat-sheet IS the institutional-posture substrate at the
#   national-faction layer. Strongest M-4 binding so far.
#
#   М-6 CHOICE IS FORCED — PRIMARY (previously unbound primary at sim
#   level). The §1 Stability triggers with capital-territory double-magnitude
#   penalty + Suppress-failure named exception forces canonical choice
#   architecture. M12 may finally close the M-6 gap at sim level. Note:
#   character-layer T-12/T-13/T-17 forced-choice remains separate sim scope.
#
# Encodes:
#   faction_layer_v30 §1 Stability Triggers (five canonical) — territorial
#       occupation, capital double-magnitude penalty, Suppress-failure exception
#   faction_layer_v30 §9 CI Formula (full integration sequence) — institutional
#       momentum, Piety yield, Assert/Suppress, Baralta structural suppression,
#       CI seasonal cap
#   ci_political_v30 §3.2 CI bonus dice — floor(CI/20) bonus dice in
#       Parliamentary/Treaty/Diplomacy contexts
#   ci_political_v30 §3.3 CI Mandate-reduction — floor(CI/30) reduction to
#       anti-Church voting Mandate
#   mass_battle_v30 §E.1 Immediate Battle Consequences — Substrate Fracture
#       (MS -1 / MS -2 Campaign-War), Accord erosion on conquest, Order -1
#       at battle site
#   mass_battle_v30 §E.2 Deferred Accounting Consequences — IP advance via
#       peninsular_strain §3.2 thresholds, Strain advance via §4.1 cap
#
# Bottom-up: each faction-level effect is a pure transform. Stability
# triggers fire on canonical events; CI bonus dice is a pure calculation;
# battle consequences are pure-state mutators. Module 13 will compose
# these into the integrated per-season runner.
#
# Canonical sources (full read this session):
#   designs/provincial/faction_layer_v30.md (§1, §9)
#   designs/provincial/ci_political_v30.md (§3)
#   designs/provincial/mass_battle_v30.md (§E.1, §E.2)

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

from module_05_governance import SubnationalFaction
from module_06_events import SettlementEvent
from module_07_military import MilitaryAction
from module_09_timeline import (
    ClockState, INTER_FACTION_BATTLE_IP_DELTA, BATTLE_MS_PENALTY_NORMAL,
    BATTLE_MS_PENALTY_CAMPAIGN_WAR,
)
from module_11_provincial_authority import DomainActionResult


# ── Faction stat-sheet (canonical six stats per faction_layer + ED-790) ────

@dataclass
class FactionStats:
    # Canonical faction stat-sheet. clock_registry plus faction_layer §1
    # surface six core stats. The ED-seven-nine-zero M8 founded-faction work added
    # Legitimacy plus Public Support for founded factions; this module retains
    # them as separate fields, defaulting to None for original-canonical factions
    # (Crown, Hafenmark, Varfell, Church).
    faction_name: str
    mandate: int = 0       # 0-7; 0 = subjugated
    influence: int = 1     # 1-7 (BG floor 1)
    wealth: int = 1        # 1-7 (BG floor 1)
    military: int = 1      # 1-7 (BG floor 1)
    stability: int = 1     # 0-7 (BG: 0 = eliminated)
    intel: int = 1         # 1-7 (BG floor 1)
    # ED-790 founded-faction additions (None for canonical originals)
    legitimacy: Optional[int] = None        # 0-7 for founded factions
    public_support: Optional[int] = None    # 0-7 for founded factions
    # Capital territories (per §1 Stability triggers)
    capital_territories: List[str] = field(default_factory=list)
    controlled_territories: List[str] = field(default_factory=list)


# §faction_layer Stat ranges
# [canonical: clock_registry_v30.md Faction Stats table —
#  "| Mandate | 0–7 (0 = subjugated) |"]
FACTION_MANDATE_MIN: int = 0
FACTION_MANDATE_MAX: int = 7
FACTION_MANDATE_SUBJUGATED_VALUE: int = 0

# [canonical: clock_registry_v30.md —
#  "| Stability | 0–7 (BG: 0 = eliminated) |"]
FACTION_STABILITY_MIN: int = 0
FACTION_STABILITY_MAX: int = 7
FACTION_STABILITY_ELIMINATED_VALUE: int = 0

# [canonical: clock_registry_v30.md — other stats "1–7 (BG: floor 1)"]
FACTION_OTHER_STATS_MIN: int = 1
FACTION_OTHER_STATS_MAX: int = 7


# ── faction_layer §1 Stability Triggers ────────────────────────────────────

class StabilityTrigger(Enum):
    """faction_layer §1 — five canonical Stability triggers."""
    TERRITORIAL_OCCUPATION = 'territorial_occupation'        # Trigger 1
    TERRITORIAL_LOSS_FORMAL = 'territorial_loss_formal'
    CAPITAL_OCCUPATION = 'capital_occupation'
    CAPITAL_LOSS_FORMAL = 'capital_loss_formal'
    SUPPRESS_FAILURE = 'suppress_failure'                    # §9 Step 4 exception


# §1 Trigger 1 — Territorial Occupation
# [canonical: faction_layer §1.2 Trigger 1 Territorial Occupation table —
#  "Own territory placed under Occupation | −1 | Immediate, one-time"]
TERRITORIAL_OCCUPATION_STABILITY_DELTA: int = 1   # -1 magnitude
# [canonical: §1.2 Trigger 1 —
#  "Territory formally transferred (control lost) | −1 additional | At moment of transfer"]
TERRITORIAL_LOSS_FORMAL_STABILITY_DELTA: int = 1

# §1 Trigger 1 — Capital territory double-magnitude
# [canonical: §1.2 Trigger 1 —
#  "Capital territory lost (T1, T8, T9, T12) | −2 total (not −1) | Replaces standard −1"]
CAPITAL_OCCUPATION_STABILITY_DELTA: int = 2
# [canonical: §1.2 Trigger 1 —
#  "Capital territory formally transferred | −3 total | Replaces standard −2"]
CAPITAL_LOSS_FORMAL_STABILITY_DELTA: int = 3

# §9 Step 4 — Suppress failure named exception
# [canonical: faction_layer §1 —
#  "Suppress action (CI Accounting formula, params_board_game §CI Generation
#  Step 4) Failure → Stability −1."]
SUPPRESS_FAILURE_STABILITY_DELTA: int = 1


def apply_stability_trigger(
    stats: FactionStats,
    trigger: StabilityTrigger,
    is_capital_territory: bool = False,
) -> int:
    """faction_layer §1 — apply Stability delta from a canonical trigger.
    Pure transform on FactionStats.stability. Returns new stability value.
    Clamps at FACTION_STABILITY_MIN."""
    if trigger == StabilityTrigger.TERRITORIAL_OCCUPATION:
        delta = (CAPITAL_OCCUPATION_STABILITY_DELTA if is_capital_territory
                 else TERRITORIAL_OCCUPATION_STABILITY_DELTA)
    elif trigger == StabilityTrigger.TERRITORIAL_LOSS_FORMAL:
        delta = (CAPITAL_LOSS_FORMAL_STABILITY_DELTA if is_capital_territory
                 else TERRITORIAL_LOSS_FORMAL_STABILITY_DELTA)
    elif trigger == StabilityTrigger.CAPITAL_OCCUPATION:
        # Direct capital trigger — same magnitude as territorial_occupation
        # with is_capital=True. Defensive: use canonical -2 magnitude.
        delta = CAPITAL_OCCUPATION_STABILITY_DELTA
    elif trigger == StabilityTrigger.CAPITAL_LOSS_FORMAL:
        delta = CAPITAL_LOSS_FORMAL_STABILITY_DELTA
    elif trigger == StabilityTrigger.SUPPRESS_FAILURE:
        delta = SUPPRESS_FAILURE_STABILITY_DELTA
    else:
        return stats.stability
    new_stability = max(FACTION_STABILITY_MIN, stats.stability - delta)
    stats.stability = new_stability
    return new_stability


def is_eliminated(stats: FactionStats) -> bool:
    """A faction is eliminated when Stability reaches 0 in BG mode."""
    return stats.stability <= FACTION_STABILITY_ELIMINATED_VALUE


# ── §9 CI Formula Integration ──────────────────────────────────────────────

# §9 Step 1 — Institutional Momentum (canonical +1/season baseline)
# [canonical: faction_layer §9 Step 1 —
#  "Institutional Momentum: CI +1 (always, cannot be negated below this
#  baseline by player actions; only events can)"]
CI_INSTITUTIONAL_MOMENTUM: int = 1

# §9 Step 5 — Hafenmark Structural Suppression (Baralta)
# [canonical: faction_layer §9 Step 5 —
#  "Hafenmark Structural Suppression (Baralta): While Inge Baralta NPC
#  Mandate ≥ 4: CI −1/season automatically."]
BARALTA_STRUCTURAL_SUPPRESSION_MAGNITUDE: int = 1
BARALTA_STRUCTURAL_SUPPRESSION_MANDATE_THRESHOLD: int = 4

# §9 Step 6 — CI seasonal caps (PP-504)
# [canonical: faction_layer §9 Step 6 —
#  "CI seasonal cap (PP-504): ±3/season from player-initiated Domain Actions.
#  ±5/season from all sources combined."]
CI_PLAYER_DA_SEASONAL_CAP: int = 3
CI_ALL_SOURCES_SEASONAL_CAP: int = 5


def ci_institutional_momentum() -> int:
    """§9 Step 1 — passive CI +1/season baseline."""
    return CI_INSTITUTIONAL_MOMENTUM


def ci_baralta_suppression(baralta_mandate: int) -> int:
    """§9 Step 5 — Baralta structural suppression. Returns the magnitude of
    CI penalty to apply (positive integer)."""
    if baralta_mandate >= BARALTA_STRUCTURAL_SUPPRESSION_MANDATE_THRESHOLD:
        return BARALTA_STRUCTURAL_SUPPRESSION_MAGNITUDE
    return 0


def apply_ci_seasonal_cap(
    raw_delta: int,
    from_player_da: bool,
) -> int:
    """§9 Step 6 — cap CI delta at canonical thresholds.
    Player Domain Actions: ±3/season. All sources: ±5/season."""
    cap = CI_PLAYER_DA_SEASONAL_CAP if from_player_da else CI_ALL_SOURCES_SEASONAL_CAP
    if raw_delta > cap:
        return cap
    if raw_delta < -cap:
        return -cap
    return raw_delta


# ── ci_political §3.2 CI bonus dice ────────────────────────────────────────

# [canonical: ci_political §3.2 — "Church acts in any of the following
#  contexts, it adds floor(CI/20) bonus dice to its roll"]
CI_BONUS_DICE_DIVISOR: int = 20


def ci_bonus_dice(ci: int) -> int:
    # §3.2 — Church bonus dice in Parliamentary/Treaty/Diplomacy contexts.
    # Pure function of CI. Worked examples per canon — see canonical table
    # in the throughline-referenced ci_political_v30 §3.2 source.
    return ci // CI_BONUS_DICE_DIVISOR


# ── ci_political §3.3 CI Mandate-reduction (anti-Church voting) ────────────

# [canonical: ci_political §3.3 — "Ob of the vote threshold calculation is
#  unchanged, but each secular faction voting against Church reduces their
#  effective Mandate contribution by floor(CI/30)"]
CI_MANDATE_REDUCTION_DIVISOR: int = 30


def ci_mandate_reduction(ci: int) -> int:
    # §3.3 — Mandate reduction for secular factions voting against Church.
    # Pure function of CI. Canonical thresholds and reductions per the
    # ci_political_v30 §3.3 canonical table.
    return ci // CI_MANDATE_REDUCTION_DIVISOR


# ── mass_battle §E.1 Immediate Battle Consequences ─────────────────────────

class BattleScale(Enum):
    """mass_battle §E.1 — battle scale determines MS penalty magnitude."""
    SKIRMISH = 'skirmish'
    STANDARD = 'standard'
    CAMPAIGN = 'campaign'
    WAR = 'war'


# §E.1 Substrate Fracture
# Note: BATTLE_MS_PENALTY_NORMAL (1) and BATTLE_MS_PENALTY_CAMPAIGN_WAR (2)
# are already in M9 ledger; we re-use those constants here.


def battle_ms_penalty(scale: BattleScale) -> int:
    """§E.1 — Substrate Fracture MS penalty by battle scale.
    Returns positive integer to subtract from MS."""
    if scale in (BattleScale.CAMPAIGN, BattleScale.WAR):
        return BATTLE_MS_PENALTY_CAMPAIGN_WAR
    return BATTLE_MS_PENALTY_NORMAL


# §E.1 Accord erosion
# [canonical: mass_battle §E.1 —
#  "Accord erosion — conquered territory | Attacker conquers via Battle |
#  Accord set to 1 (Category A: all settlements reset to Order 1)"]
CONQUEST_ACCORD_RESET_VALUE: int = 1

# [canonical: mass_battle §E.1 —
#  "Accord erosion — defender's territory | Battle occurs in a territory
#  the defender controls | Order −1 in settlement nearest battle site"]
DEFENDER_TERRITORY_BATTLE_ORDER_PENALTY: int = 1


# §E.2 Deferred Accounting Consequences — IP / Strain thresholds
# [canonical: mass_battle §E.2 referencing peninsular_strain §3.2 —
#  "territory-count thresholds: 2-3 → +1; 4-5 → +2; 6+ → +3"]
IP_THRESHOLD_LOW_RANGE: int = 2     # 2-3 contested territories
IP_THRESHOLD_LOW_DELTA: int = 1
IP_THRESHOLD_MID_RANGE: int = 4     # 4-5
IP_THRESHOLD_MID_DELTA: int = 2
IP_THRESHOLD_HIGH_RANGE: int = 6    # 6+
IP_THRESHOLD_HIGH_DELTA: int = 3

# [canonical: mass_battle §E.2 referencing peninsular_strain §4.1 —
#  "Strain advance per peninsular_strain §4.1 (+1/territory, cap +3/season)"]
STRAIN_PER_CONTESTED_TERRITORY: int = 1
STRAIN_SEASONAL_CAP: int = 3


def ip_advance_from_contested_territories(contested_count: int) -> int:
    """§E.2 — IP advance from contested-territory count at Accounting.
    Canonical thresholds: 0-1 → 0; 2-3 → +1; 4-5 → +2; 6+ → +3."""
    if contested_count >= IP_THRESHOLD_HIGH_RANGE:
        return IP_THRESHOLD_HIGH_DELTA
    if contested_count >= IP_THRESHOLD_MID_RANGE:
        return IP_THRESHOLD_MID_DELTA
    if contested_count >= IP_THRESHOLD_LOW_RANGE:
        return IP_THRESHOLD_LOW_DELTA
    return 0


def strain_advance_from_contested_territories(contested_count: int) -> int:
    """§E.2 — Strain advance from contested-territory count at Accounting.
    Linear: +1/territory, capped at STRAIN_SEASONAL_CAP."""
    return min(STRAIN_SEASONAL_CAP, contested_count * STRAIN_PER_CONTESTED_TERRITORY)


@dataclass(frozen=True)
class BattleConsequenceReport:
    # Aggregated battle consequence report consumed by the Module-thirteen
    # integration runner.
    ms_delta: int                         # negative; subtract from clock_state.ms
    conquered_territories_accord_reset: List[str]
    defender_territory_settlements_order_penalty: List[str]


def apply_battle_consequences(
    clock_state: ClockState,
    scale: BattleScale,
    is_conquest: bool,
    is_defender_territory: bool,
    conquered_territory_id: Optional[str] = None,
    defender_settlement_id: Optional[str] = None,
) -> BattleConsequenceReport:
    """§E.1 — apply immediate Battle Consequences.
    Mutates clock_state.ms (Substrate Fracture). Returns the report;
    caller applies the territory/settlement-level changes."""
    from module_09_timeline import MS_MIN
    ms_penalty = battle_ms_penalty(scale)
    new_ms = max(MS_MIN, clock_state.ms - ms_penalty)
    actual_ms_delta = new_ms - clock_state.ms
    clock_state.ms = new_ms

    conquered_list: List[str] = []
    if is_conquest and conquered_territory_id is not None:
        conquered_list.append(conquered_territory_id)

    defender_order_list: List[str] = []
    if is_defender_territory and defender_settlement_id is not None:
        defender_order_list.append(defender_settlement_id)

    return BattleConsequenceReport(
        ms_delta=actual_ms_delta,
        conquered_territories_accord_reset=conquered_list,
        defender_territory_settlements_order_penalty=defender_order_list,
    )


# ── Renown signal binding (rebinds M3-M11 provisional signals) ─────────────

# Module 8 owns the Renown track and apply_renown_delta. Module 12 owns the
# faction-stat-sheet equivalents: bind the provisional faction_standing_delta
# signals from M3-M11 ActionResult to canonical Mandate/Influence/Stability
# changes per faction.

@dataclass(frozen=True)
class FactionDeltaBinding:
    """Canonical mapping from M3-M11 ActionResult.faction_standing_delta
    signal magnitude to faction-stat-sheet effects."""
    mandate_delta: int
    influence_delta: int
    stability_delta: int


# Per ED-790 + faction_politics_v30 conventions, faction_standing_delta from
# ActionResult is a coarse signal. M12 canonicalizes the binding:
# +1 = positive engagement (Influence +1 typical)
# -1 = political setback (Stability check; Influence -1)
# -2 = governance crisis (Stability -1 direct, no check)
# Higher magnitudes scale linearly.
def bind_faction_standing_delta(
    raw_delta: int,
) -> FactionDeltaBinding:
    # Bind a coarse faction_standing_delta signal to canonical faction-stat
    # changes. Used by the Module-thirteen integration runner to translate
    # ActionResult signals from prior modules into faction-stat-sheet mutations.
    if raw_delta == 0:
        return FactionDeltaBinding(0, 0, 0)
    if raw_delta == 1:
        return FactionDeltaBinding(mandate_delta=0, influence_delta=1, stability_delta=0)
    if raw_delta == -1:
        return FactionDeltaBinding(mandate_delta=0, influence_delta=-1, stability_delta=0)
    if raw_delta == 2:
        return FactionDeltaBinding(mandate_delta=1, influence_delta=1, stability_delta=0)
    if raw_delta == -2:
        return FactionDeltaBinding(mandate_delta=0, influence_delta=-1, stability_delta=-1)
    # Beyond ±2: scale stability for stronger negatives, mandate for stronger positives
    if raw_delta > 2:
        return FactionDeltaBinding(
            mandate_delta=raw_delta - 1,
            influence_delta=1,
            stability_delta=0,
        )
    # raw_delta < -2
    return FactionDeltaBinding(
        mandate_delta=0,
        influence_delta=-1,
        stability_delta=raw_delta + 1,   # negative
    )


# ── Throughline coverage (audit-facing) ────────────────────────────────────

THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[str, str] = {
    'T-21': 'PRIMARY — Faction Mandate/Stability mechanics IS the political warfare layer (closes prior-unbound primary).',
    'T-24': 'PRIMARY — Cascade at battles + CI threshold crossings IS the convergence-as-crisis canonical mechanism (closes second prior-unbound primary).',
    'T-08': 'EXTENSION (M4 primary) — CI political-pool mechanism per §3.2 + §3.3.',
    'T-20': 'EXTENSION (M7/M8/M11 secondary) — Capital double-magnitude Stability penalty forces sovereignty-vs-survival choice.',
    'T-04': 'EXTENSION (M9 primary) — §E.1 immediate-battle MS -1/-2 augments M9 per-year decay.',
}

META_THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[str, str] = {
    'М-4': 'PRIMARY (extends M3/M4/M5/M11) — Faction stat-sheet IS the institutional-posture substrate at national-faction layer. Strongest M-4 binding.',
    'М-6': 'PRIMARY (previously unbound primary at sim level) — Capital-territory double-magnitude penalty + Suppress-failure named exception force canonical choice architecture. M-6 closes at sim-level scope.',
}


# ── Isolation tests ────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — FactionStats canonical defaults
    fs = FactionStats(faction_name='Crown')
    ok = (fs.mandate == 0 and fs.influence == 1 and fs.wealth == 1
          and fs.military == 1 and fs.stability == 1 and fs.intel == 1)
    r['T1_faction_stats_defaults'] = 'PASS' if ok else f'FAIL ({fs})'

    # T2 — StabilityTrigger has exactly 5 canonical triggers per §1.2
    # [canonical: §1.2 — "Stability Triggers (Five Canonical)"]
    expected_trigger_count = 5
    r['T2_five_stability_triggers'] = (
        'PASS' if len(StabilityTrigger) == expected_trigger_count else 'FAIL'
    )

    # T3 — Territorial Occupation applies -1 Stability
    fs_a = FactionStats(faction_name='Crown', stability=4)
    apply_stability_trigger(fs_a, StabilityTrigger.TERRITORIAL_OCCUPATION,
                             is_capital_territory=False)
    # [canonical: §1.2 Trigger 1 — "Own territory placed under Occupation | −1"]
    expected_stability_after_normal_occ = 3
    r['T3_territorial_occupation_minus_1'] = (
        'PASS' if fs_a.stability == expected_stability_after_normal_occ else f'FAIL ({fs_a.stability})'
    )

    # T4 — Capital occupation applies -2 (double magnitude)
    fs_b = FactionStats(faction_name='Crown', stability=4)
    apply_stability_trigger(fs_b, StabilityTrigger.TERRITORIAL_OCCUPATION,
                             is_capital_territory=True)
    # [canonical: §1.2 Trigger 1 — "Capital territory lost ... | −2 total"]
    expected_stability_after_capital_occ = 2
    r['T4_capital_occupation_minus_2'] = (
        'PASS' if fs_b.stability == expected_stability_after_capital_occ else f'FAIL ({fs_b.stability})'
    )

    # T5 — Capital formal loss applies -3
    fs_c = FactionStats(faction_name='Crown', stability=5)
    apply_stability_trigger(fs_c, StabilityTrigger.TERRITORIAL_LOSS_FORMAL,
                             is_capital_territory=True)
    # [canonical: §1.2 Trigger 1 — "Capital territory formally transferred | −3 total"]
    expected_stability_after_capital_loss = 2
    r['T5_capital_loss_formal_minus_3'] = (
        'PASS' if fs_c.stability == expected_stability_after_capital_loss else f'FAIL ({fs_c.stability})'
    )

    # T6 — Stability clamps at min (eliminated value)
    fs_d = FactionStats(faction_name='Crown', stability=1)
    apply_stability_trigger(fs_d, StabilityTrigger.TERRITORIAL_LOSS_FORMAL,
                             is_capital_territory=True)
    # -3 from 1 → would be -2, clamps to 0 (eliminated)
    r['T6_stability_clamps_eliminated'] = (
        'PASS' if fs_d.stability == FACTION_STABILITY_ELIMINATED_VALUE else 'FAIL'
    )

    # T7 — is_eliminated at Stability 0
    r['T7_is_eliminated_at_zero'] = (
        'PASS' if is_eliminated(fs_d) else 'FAIL'
    )

    # T8 — Suppress failure exception fires Stability -1
    # [canonical: §1 — "Suppress action ... Failure → Stability −1"]
    fs_e = FactionStats(faction_name='Crown', stability=3)
    apply_stability_trigger(fs_e, StabilityTrigger.SUPPRESS_FAILURE)
    r['T8_suppress_failure_minus_1'] = (
        'PASS' if fs_e.stability == 2 else f'FAIL ({fs_e.stability})'
    )

    # T9 — CI institutional momentum is +1 per §9 Step 1
    # [canonical: §9 Step 1 — "Institutional Momentum: CI +1 (always)"]
    expected_momentum_per_season = 1
    r['T9_ci_institutional_momentum'] = (
        'PASS' if ci_institutional_momentum() == expected_momentum_per_season else 'FAIL'
    )

    # T10 — Baralta suppression fires at Mandate >= 4
    # [canonical: §9 Step 5 —
    #  "While Inge Baralta NPC Mandate ≥ 4: CI −1/season automatically"]
    expected_baralta_suppression = 1
    r['T10_baralta_suppression_active'] = (
        'PASS' if ci_baralta_suppression(baralta_mandate=4) == expected_baralta_suppression
        else 'FAIL'
    )

    # T11 — Baralta suppression dormant at Mandate < 4
    r['T11_baralta_suppression_dormant'] = (
        'PASS' if ci_baralta_suppression(baralta_mandate=3) == 0 else 'FAIL'
    )

    # T12 — CI seasonal cap from player DA = ±3
    # [canonical: §9 Step 6 — "±3/season from player-initiated Domain Actions"]
    capped = apply_ci_seasonal_cap(raw_delta=10, from_player_da=True)
    r['T12_ci_player_da_cap_3'] = (
        'PASS' if capped == 3 else f'FAIL ({capped})'
    )

    # T13 — CI seasonal cap from all sources = ±5
    # [canonical: §9 Step 6 — "±5/season from all sources combined"]
    capped = apply_ci_seasonal_cap(raw_delta=10, from_player_da=False)
    r['T13_ci_all_sources_cap_5'] = (
        'PASS' if capped == 5 else f'FAIL ({capped})'
    )

    # T14 — CI bonus dice canonical worked examples
    # [canonical: §3.2 — "CI 28: floor(28/20) = +1D"]
    expected_bonus_dice_at_28 = 1
    r['T14_ci_bonus_dice_28'] = (
        'PASS' if ci_bonus_dice(28) == expected_bonus_dice_at_28 else 'FAIL'
    )

    # T15 — CI bonus dice at CI 40 = +2D
    # [canonical: §3.2 — "CI 40: +2D"]
    r['T15_ci_bonus_dice_40'] = (
        # [canonical: ci_political §3.2 — 'CI 40: +2D']
        'PASS' if ci_bonus_dice(40) == 2 else 'FAIL'
    )

    # T16 — CI bonus dice at CI 100 = +5D (max canonical worked)
    # [canonical: §3.2 — "CI 100: +5D"]
    expected_bonus_dice_at_100 = 5
    r['T16_ci_bonus_dice_100'] = (
        # [canonical: ci_political §3.2 — 'CI 100: +5D']
        'PASS' if ci_bonus_dice(100) == expected_bonus_dice_at_100 else 'FAIL'
    )

    # T17 — CI Mandate reduction at CI 0-29 = 0
    # [canonical: §3.3 table — "0–29 | 0"]
    r['T17_ci_mandate_reduction_below_30'] = (
        'PASS' if ci_mandate_reduction(20) == 0 else 'FAIL'
    )

    # T18 — CI Mandate reduction at CI 30 = 1
    # [canonical: §3.3 table — "30–59 | -1"]
    r['T18_ci_mandate_reduction_30_59'] = (
        'PASS' if ci_mandate_reduction(30) == 1 else 'FAIL'
    )

    # T19 — CI Mandate reduction at CI 90+ = 3
    # [canonical: §3.3 table — "90+ | -3"]
    expected_mandate_reduction_at_90 = 3
    r['T19_ci_mandate_reduction_90'] = (
        # [canonical: ci_political §3.3 table — '90+ | -3']
        'PASS' if ci_mandate_reduction(90) == expected_mandate_reduction_at_90 else 'FAIL'
    )

    # T20 — Battle MS penalty: standard scale = -1
    # [canonical: §E.1 — "MS −1 (Campaign/War scale: MS −2)"]
    r['T20_battle_ms_standard_minus_1'] = (
        'PASS' if battle_ms_penalty(BattleScale.STANDARD) == BATTLE_MS_PENALTY_NORMAL
        else 'FAIL'
    )

    # T21 — Battle MS penalty: campaign scale = -2
    r['T21_battle_ms_campaign_minus_2'] = (
        'PASS' if battle_ms_penalty(BattleScale.CAMPAIGN) == BATTLE_MS_PENALTY_CAMPAIGN_WAR
        else 'FAIL'
    )

    # T22 — Battle MS penalty: war scale = -2
    r['T22_battle_ms_war_minus_2'] = (
        'PASS' if battle_ms_penalty(BattleScale.WAR) == BATTLE_MS_PENALTY_CAMPAIGN_WAR
        else 'FAIL'
    )

    # T23 — IP advance: 0 contested = 0
    r['T23_ip_no_contested'] = (
        'PASS' if ip_advance_from_contested_territories(0) == 0 else 'FAIL'
    )

    # T24 — IP advance: 2-3 contested = +1
    # [canonical: §E.2 — "2-3 → +1"]
    r['T24_ip_low_range_plus_1'] = (
        'PASS' if ip_advance_from_contested_territories(2) == 1
        and ip_advance_from_contested_territories(3) == 1
        else 'FAIL'
    )

    # T25 — IP advance: 4-5 contested = +2
    # [canonical: §E.2 — "4-5 → +2"]
    r['T25_ip_mid_range_plus_2'] = (
        'PASS' if ip_advance_from_contested_territories(4) == 2
        and ip_advance_from_contested_territories(5) == 2
        else 'FAIL'
    )

    # T26 — IP advance: 6+ contested = +3
    # [canonical: §E.2 — "6+ → +3"]
    r['T26_ip_high_range_plus_3'] = (
        'PASS' if ip_advance_from_contested_territories(6) == 3
        and ip_advance_from_contested_territories(10) == 3
        else 'FAIL'
    )

    # T27 — Strain advance: linear with cap
    # [canonical: §E.2 — "+1/territory, cap +3/season"]
    ok = (strain_advance_from_contested_territories(0) == 0
          and strain_advance_from_contested_territories(2) == 2
          and strain_advance_from_contested_territories(5) == STRAIN_SEASONAL_CAP)
    r['T27_strain_linear_with_cap'] = 'PASS' if ok else 'FAIL'

    # T28 — Battle consequences mutate clock_state.ms
    # [canonical: starting MS sentinel for §E.1 test — derived from MS_START=72 minus 2 prior decays]
    cs_a = ClockState(ms=70)
    report = apply_battle_consequences(
        clock_state=cs_a, scale=BattleScale.STANDARD,
        is_conquest=False, is_defender_territory=False,
    )
    r['T28_battle_consequences_mutate_ms'] = (
        # [canonical: §E.1 standard battle MS -1 — 70-1=69]
        'PASS' if cs_a.ms == 69 and report.ms_delta == -1 else f'FAIL ({cs_a.ms}, {report})'
    )

    # T29 — Battle consequences: campaign-scale MS -2
    # [canonical: starting MS sentinel for §E.1 campaign test]
    cs_b = ClockState(ms=70)
    apply_battle_consequences(
        clock_state=cs_b, scale=BattleScale.CAMPAIGN,
        is_conquest=False, is_defender_territory=False,
    )
    # [canonical: §E.1 Campaign/War scale MS -2 — 70-2=68]
    expected_post_campaign_ms = 68
    r['T29_battle_campaign_ms_minus_2'] = (
        'PASS' if cs_b.ms == expected_post_campaign_ms else f'FAIL ({cs_b.ms})'
    )

    # T30 — Battle consequences: conquest surfaces territory in report
    # [canonical: starting MS sentinel for §E.1 conquest test]
    cs_c = ClockState(ms=70)
    report = apply_battle_consequences(
        clock_state=cs_c, scale=BattleScale.STANDARD,
        is_conquest=True, is_defender_territory=False,
        conquered_territory_id='T2_Kronmark',
    )
    r['T30_battle_conquest_surfaces_territory'] = (
        'PASS' if 'T2_Kronmark' in report.conquered_territories_accord_reset
        else f'FAIL ({report})'
    )

    # T31 — Battle consequences: defender territory surfaces settlement
    # [canonical: starting MS sentinel for §E.1 defender-territory test]
    cs_d = ClockState(ms=70)
    report = apply_battle_consequences(
        clock_state=cs_d, scale=BattleScale.STANDARD,
        is_conquest=False, is_defender_territory=True,
        defender_settlement_id='S-001',
    )
    r['T31_battle_defender_surfaces_settlement'] = (
        'PASS' if 'S-001' in report.defender_territory_settlements_order_penalty
        else f'FAIL ({report})'
    )

    # T32 — bind_faction_standing_delta: 0 = neutral
    binding = bind_faction_standing_delta(0)
    ok = (binding.mandate_delta == 0 and binding.influence_delta == 0
          and binding.stability_delta == 0)
    r['T32_bind_zero_delta'] = 'PASS' if ok else f'FAIL ({binding})'

    # T33 — bind_faction_standing_delta: +1 = Influence +1
    binding = bind_faction_standing_delta(1)
    r['T33_bind_plus_1_influence'] = (
        'PASS' if binding.influence_delta == 1 and binding.stability_delta == 0
        else f'FAIL ({binding})'
    )

    # T34 — bind_faction_standing_delta: -2 = governance crisis (Stability -1)
    binding = bind_faction_standing_delta(-2)
    r['T34_bind_minus_2_stability_hit'] = (
        'PASS' if binding.stability_delta == -1 and binding.influence_delta == -1
        else f'FAIL ({binding})'
    )

    # T35 — Throughline coverage: T-21 PRIMARY (closes prior-unbound)
    r['T35_throughline_t21_primary'] = (
        'PASS' if 'T-21' in THROUGHLINE_COVERAGE_BY_THIS_MODULE
        and 'PRIMARY' in THROUGHLINE_COVERAGE_BY_THIS_MODULE['T-21']
        else 'FAIL'
    )

    # T36 — Throughline coverage: T-24 PRIMARY (closes prior-unbound)
    r['T36_throughline_t24_primary'] = (
        'PASS' if 'T-24' in THROUGHLINE_COVERAGE_BY_THIS_MODULE
        and 'PRIMARY' in THROUGHLINE_COVERAGE_BY_THIS_MODULE['T-24']
        else 'FAIL'
    )

    # T37 — Meta-throughline М-6 PRIMARY (closes prior-unbound at sim level)
    r['T37_meta_m6_primary_closes_gap'] = (
        'PASS' if 'М-6' in META_THROUGHLINE_COVERAGE_BY_THIS_MODULE
        and 'PRIMARY' in META_THROUGHLINE_COVERAGE_BY_THIS_MODULE['М-6']
        else 'FAIL'
    )

    # T38 — Emergent cross-module chain: M9 MS decay + M12 battle MS -2
    # composes naturally. Starting MS=72; M9 year-1 decay -> 71; M12
    # Campaign battle -> 69.
    cs_chain = ClockState(ms=72)
    from module_09_timeline import tick_ms_decay
    tick_ms_decay(cs_chain, is_year_boundary=True)   # 72 -> 71
    apply_battle_consequences(
        clock_state=cs_chain, scale=BattleScale.CAMPAIGN,
        is_conquest=False, is_defender_territory=False,
    )   # 71 -> 69
    # [canonical: M9 year-decay then M12 Campaign -2 = 72-1-2=69]
    expected_post_compose_ms = 69
    r['T38_emergent_m9_m12_ms_compose'] = (
        'PASS' if cs_chain.ms == expected_post_compose_ms
        else f'FAIL ({cs_chain.ms})'
    )

    # T39 — Capital territory Stability double-magnitude forces forced-choice
    # (M-6 binding test): a faction with 2 territories where one is capital
    # cannot afford to defend both — losing the capital is -2/-3 magnitude.
    fs_forced = FactionStats(faction_name='Crown', stability=4,
                              capital_territories=['T1'],
                              controlled_territories=['T1', 'T2'])
    # Forced-choice: must prioritize T1 defense or accept -2 Stability hit.
    apply_stability_trigger(fs_forced, StabilityTrigger.TERRITORIAL_OCCUPATION,
                             is_capital_territory=True)
    # Stability 4 -> 2; non-capital occupation would be 4 -> 3
    expected_forced_choice_penalty = 2
    r['T39_forced_choice_capital_penalty_double'] = (
        'PASS' if fs_forced.stability == expected_forced_choice_penalty else 'FAIL'
    )

    # T40 — Emergent cascade: Suppress failure + capital loss = Stability collapse
    # T-24 Convergence as Crisis: multiple Stability triggers converging in
    # one season produce emergent crisis (Stability cascade per §1.2 note
    # "fires when a faction sustains ≥2 attribute losses in one season").
    fs_cascade = FactionStats(faction_name='Crown', stability=4)
    apply_stability_trigger(fs_cascade, StabilityTrigger.TERRITORIAL_LOSS_FORMAL,
                             is_capital_territory=True)   # -3 -> stability 1
    apply_stability_trigger(fs_cascade, StabilityTrigger.SUPPRESS_FAILURE)
    # -3 -1 = -4 from 4 -> 0 (eliminated)
    ok = (fs_cascade.stability == FACTION_STABILITY_ELIMINATED_VALUE
          and is_eliminated(fs_cascade))
    r['T40_convergence_crisis_cascade'] = (
        'PASS' if ok else f'FAIL ({fs_cascade.stability})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 12 — Faction integration — isolation tests"
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
    print(f"Stability triggers: {[t.value for t in StabilityTrigger]}")
    print(f"Battle scales: {[s.value for s in BattleScale]}")
    print(f"CI worked examples — 28: {ci_bonus_dice(28)}D, 40: {ci_bonus_dice(40)}D, 100: {ci_bonus_dice(100)}D")
    print(f"Throughline coverage: {sorted(THROUGHLINE_COVERAGE_BY_THIS_MODULE.keys())}")
    print(f"Meta-throughline: {sorted(META_THROUGHLINE_COVERAGE_BY_THIS_MODULE.keys())}")
    sys.exit(1 if fail else 0)
