# module_07_military.py — Settlement-scoped military granularity
#
# Mode G Module seven of settlement_mgmt_stress_01.
#
# Approach: BOTTOM-UP GRANULAR EMERGENT (per Jordan's directive,
# continued from M6).
#
# Each military function is a pure predicate or pure transform on
# settlement state. There is no military "controller" or "battle
# manager" object. The full military surface is:
#
#   1. effective_defense(stats, garrison) — settlement Defense + garrison
#      Discipline (pure)
#   2. action_eligibility(attacker_military, effective_defense) — Assault
#      / Siege / Bypass requirement predicates (pure)
#   3. terrain_modifier(edge_type) — adjacency §2.2 Manoeuvre Phase modifier
#      lookup (pure)
#   4. settlement_type_modifier(settlement) — adjacency §2.2 defender bonus
#      lookup (pure)
#   5. resolve_assault(...) — single roll; mutates state per §5.1 +
#      adjacency §2.3 consequences
#   6. resolve_siege_tick(...) — per-season Order -1; mutates state
#   7. resolve_bypass_supply_strike(...) — bypassed garrison's per-season
#      attack on invader's supply (§5.1 — Discipline -1 on success)
#
# Composition with M6:
#   - M6.predicate_raid_or_siege fires when Defense=0 + adjacent_hostile.
#     M7's resolve_assault provides the resolution mechanism.
#   - M6.predicate_fortress_mobilize fires for Fortress + hostile_in_province.
#     M7 provides the Defense pool vs Ob 2 check (§4.3 referenced; §5.1
#     supplies the mechanic).
#   - M6.resolve_local_revolt receives `garrison_present` as parameter. M7
#     supplies the canonical garrison-presence state.
#
# Encodes:
#   §5.1 Invasion and Defense (Assault, Siege, Bypass; capture sequence;
#        Seat-capture-grants-provincial-control; Fortress chokepoint)
#   §5.2 Garrison and Defense (one military unit per settlement; effective
#        Defense; auto-capture of ungarrisoned Defense-0 settlements)
#   settlement_adjacency_v30 §2 Mass Battle at Settlement Scale (terrain
#        modifiers from edge type; settlement-type defender modifiers;
#        battle consequences scoped to settlement)
#   settlement_adjacency_v30 §3 Invasion Sequencing (path-constrained
#        movement)
#
# Canonical sources (full read this session):
#   designs/territory/settlement_layer_v30.md (§5.1, §5.2)
#   designs/territory/settlement_adjacency_v30.md (§2, §3)
#
# Out of scope (deferred):
#   - mass_battle_v30 Part B BG Battle Resolution mechanics — Module 7
#     surfaces the call-site; actual battle resolution happens in the
#     mass-combat sim (parallel work, sim_mb_06_v19 currently)
#   - mass_battle_v30 Part E consequences (MS/Strain/IP peninsula-wide
#     effects) — Module 12 (faction integration)
#   - Fort Level mechanics (Fortress-only defender bonus) — Module 12
#     binds Fort Level to military_layer_v30
#   - military_layer_v30 garrison Discipline derivation — Module 12
#   - march_layer_v30 strategic-scale movement — distinct layer

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

from module_01_primitives import (
    Settlement, SettlementStats, by_id, STAT_MAX, STAT_MIN, REGISTRY,
)
from module_02_hierarchy import EDGES, neighbors
from module_03_facilities import ActionResult


# ── §5.1 Military action enumeration ────────────────────────────────────────

class MilitaryAction(Enum):
    """§5.1 three canonical military actions an attacker may declare."""
    ASSAULT = 'assault'
    SIEGE   = 'siege'
    BYPASS  = 'bypass'


# §5.1 / §5.2 action requirements (margin thresholds)
# [canonical: settlement_layer_v30 §5.1 Assault row —
#  "Military vs Defense + garrison"]
# Assault: no minimum margin — Military vs effective-Defense roll resolves it
ASSAULT_MIN_MILITARY_MARGIN: int = 0

# [canonical: settlement_layer_v30 §5.1 Siege row — "Military ≥ Defense"]
SIEGE_MIN_MILITARY_MARGIN: int = 0

# [canonical: settlement_layer_v30 §5.1 Bypass row —
#  "Military > Defense by 2+"]
BYPASS_MIN_MILITARY_MARGIN: int = 2

# [canonical: settlement_layer_v30 §5.1 — "A Fortress settlement in the
#  invader's path forces engagement — it cannot be bypassed unless the
#  invader's Military exceeds the Fortress Defense by 3+"]
FORTRESS_BYPASS_MIN_MARGIN: int = 3


# §5.1 Siege tick effects
# [canonical: settlement_layer_v30 §5.1 Siege row —
#  "Each season: defender Order −1 (starvation/pressure). When Order = 0,
#  settlement surrenders."]
SIEGE_ORDER_DECREMENT_PER_SEASON: int = 1
SIEGE_SURRENDER_ORDER_THRESHOLD: int = 0


# §5.1 Bypass — bypassed garrison's supply-line attack
# [canonical: settlement_layer_v30 §5.1 Bypass row —
#  "Bypassed settlement remains hostile — its garrison can attack the
#  invader's supply line (Military vs Ob 1 each season: success = invader
#  takes −1 Discipline on all units in the province)"]
BYPASS_SUPPLY_STRIKE_OB: int = 1
BYPASS_SUPPLY_STRIKE_DISCIPLINE_PENALTY: int = 1


# §5.1 Resistance threshold for non-Seat settlements after Seat capture
# [canonical: settlement_layer_v30 §5.1 —
#  "Non-Seat settlements with Order ≥ 3 may resist (maintaining their
#  current governor)"]
POST_SEAT_CAPTURE_RESIST_ORDER_THRESHOLD: int = 3


# ── §5.2 Garrison state ─────────────────────────────────────────────────────

@dataclass
class Garrison:
    # One military unit per settlement per the §5.2 spec. Discipline adds to
    # effective Defense for Assault checks.
    # unit_id is opaque (military_layer_v30 owns the unit registry).
    # discipline is the unit's Discipline stat (military_layer derivation
    # deferred to the Module-twelve faction-integration layer).
    settlement_id: str
    unit_id: Optional[str] = None
    discipline: int = 0


def has_garrison(garrison: Optional[Garrison]) -> bool:
    """A settlement has a garrison if `garrison` is non-None AND its
    unit_id is set. A Garrison object with unit_id=None represents a
    'garrison slot available but unfilled' state."""
    return garrison is not None and garrison.unit_id is not None


def effective_defense(stats: SettlementStats, garrison: Optional[Garrison]) -> int:
    """§5.2 effective Defense = settlement Defense + garrison Discipline.
    Ungarrisoned: effective Defense == settlement Defense.
    [canonical: settlement_layer_v30 §5.2 —
     'effective Defense = settlement Defense + garrison Discipline']
    """
    if not has_garrison(garrison):
        return stats.defense
    return stats.defense + garrison.discipline


def is_auto_capture(stats: SettlementStats, garrison: Optional[Garrison]) -> bool:
    """§5.2 auto-capture: ungarrisoned settlement with Defense 0.
    [canonical: settlement_layer_v30 §5.2 —
     'Ungarrisoned settlements with Defense 0 are auto-captured on any
     hostile military entry — no roll needed.']
    """
    return stats.defense == 0 and not has_garrison(garrison)


# ── §5.1 action eligibility predicates (pure) ───────────────────────────────

def can_assault(attacker_military: int, eff_def: int) -> bool:
    """§5.1 Assault: Military vs Defense+garrison. No minimum margin —
    the roll resolves it. Module 7 surfaces eligibility as "able to attempt"
    (always True if attacker has any Military); resolve_assault performs
    the actual roll."""
    return attacker_military > 0


def can_siege(attacker_military: int, eff_def: int) -> bool:
    """§5.1 Siege: Military ≥ Defense."""
    return attacker_military >= eff_def + SIEGE_MIN_MILITARY_MARGIN


def can_bypass(
    attacker_military: int,
    eff_def: int,
    settlement_type: str,
) -> bool:
    """§5.1 Bypass: Military > Defense by 2+ (3+ for Fortress).
    Canonical wording 'by 2+' means margin ≥ 2 (Military ≥ Defense + 2).
    Canonical worked example: Lowenskyst Defense 4 requires Military 7+
    (= Defense + 3) — confirms Fortress margin is 3.
    [canonical: settlement_layer_v30 §5.1 — Fortress chokepoint rule]
    """
    margin = (FORTRESS_BYPASS_MIN_MARGIN
              if settlement_type == 'Fortress'
              else BYPASS_MIN_MILITARY_MARGIN)
    return attacker_military >= eff_def + margin


# ── adjacency §2.2 terrain modifiers from edge type ─────────────────────────

# [canonical: settlement_adjacency_v30 §2.2 Terrain-from-Edge-Type table]
# Returns (attacker_dice_modifier, defender_modifier_description)
# Dice modifiers are signed integers; description strings are surfaced for
# the player-facing layer (Module 12).
@dataclass(frozen=True)
class TerrainModifier:
    """§2.2 Manoeuvre Phase modifier from edge type."""
    attacker_dice_delta: int                     # signed; -1 = attacker -1D
    description: str
    attacker_loses_fort_level_bonus: bool = False


TERRAIN_MODIFIER_BY_EDGE_TYPE: Dict[str, TerrainModifier] = {
    # [canonical: §2.2 — "Road | none"]
    'road':            TerrainModifier(attacker_dice_delta=0, description='no_modifier'),
    # [canonical: §2.2 — "River | Attacker −1D (defender benefits from crossing)"]
    'river':           TerrainModifier(attacker_dice_delta=-1,
                                        description='attacker_dice_minus_1_river_crossing'),
    # [canonical: §2.2 — "Mountain Pass | Attacker −1D (fatigue)"]
    'mountain_pass':   TerrainModifier(attacker_dice_delta=-1,
                                        description='attacker_dice_minus_1_pass_fatigue'),
    # [canonical: §2.2 — "Coastal (naval) | Attacker loses Fort-level bonus"]
    'coastal':         TerrainModifier(attacker_dice_delta=0,
                                        description='attacker_no_fort_bonus_coastal',
                                        attacker_loses_fort_level_bonus=True),
    # Sea and thread_witnessed edges (from M2 EDGES) — not in §2.2 table.
    # Module 7 surfaces these as 'no modifier' provisionally; canonical
    # ruling pending.
    'sea':             TerrainModifier(attacker_dice_delta=0,
                                        description='sea_edge_provisional'),
    'thread_witnessed':TerrainModifier(attacker_dice_delta=0,
                                        description='thread_witnessed_provisional'),
}


def terrain_modifier(edge_type: str) -> TerrainModifier:
    """§2.2 terrain modifier from edge type. Provisional for non-canonical
    edge types (sea, thread_witnessed) — those return zero-modifier."""
    return TERRAIN_MODIFIER_BY_EDGE_TYPE.get(
        edge_type,
        TerrainModifier(attacker_dice_delta=0, description=f'unknown_{edge_type}'),
    )


# ── adjacency §2.2 settlement-type defender modifiers ───────────────────────

@dataclass(frozen=True)
class SettlementTypeModifier:
    """§2.2 defender modifier by settlement type."""
    defender_ob_delta: int            # +Fort Level for Fortress (Module 12 binds Fort Level)
    defender_discipline_delta: int    # +1 for Seat
    defender_dice_bonus_conditional: int  # +1D for Port if naval reinforcements
    attacker_casus_belli: bool         # Cathedral imposes political cost
    attacker_captures_prosperity_on_victory: bool   # Mine
    fort_level_applies: bool           # Fortress only


# [canonical: settlement_adjacency_v30 §2.2 Settlement-Type defender-modifier table]
SETTLEMENT_TYPE_MODIFIER_BY_TYPE: Dict[str, SettlementTypeModifier] = {
    # [canonical: §2.2 Fortress row — "+Fort Level to Defender Ob"]
    'Fortress': SettlementTypeModifier(
        defender_ob_delta=0,        # Module 12 binds Fort Level
        defender_discipline_delta=0,
        defender_dice_bonus_conditional=0,
        attacker_casus_belli=False,
        attacker_captures_prosperity_on_victory=False,
        fort_level_applies=True,
    ),
    # [canonical: §2.2 Seat row — "+1 Defender Discipline (capital defense is rallying)"]
    'Seat': SettlementTypeModifier(
        defender_ob_delta=0,
        defender_discipline_delta=1,
        defender_dice_bonus_conditional=0,
        attacker_casus_belli=False,
        attacker_captures_prosperity_on_victory=False,
        fort_level_applies=False,
    ),
    # [canonical: §2.2 Port row — "Defender gains +1D if naval reinforcements available"]
    'Port': SettlementTypeModifier(
        defender_ob_delta=0,
        defender_discipline_delta=0,
        defender_dice_bonus_conditional=1,
        attacker_casus_belli=False,
        attacker_captures_prosperity_on_victory=False,
        fort_level_applies=False,
    ),
    # [canonical: §2.2 Cathedral row — "Attacker takes Church Casus Belli"]
    'Cathedral': SettlementTypeModifier(
        defender_ob_delta=0,
        defender_discipline_delta=0,
        defender_dice_bonus_conditional=0,
        attacker_casus_belli=True,
        attacker_captures_prosperity_on_victory=False,
        fort_level_applies=False,
    ),
    # [canonical: §2.2 Mine row — "Attacker gains captured Prosperity on victory"]
    'Mine': SettlementTypeModifier(
        defender_ob_delta=0,
        defender_discipline_delta=0,
        defender_dice_bonus_conditional=0,
        attacker_casus_belli=False,
        attacker_captures_prosperity_on_victory=True,
        fort_level_applies=False,
    ),
    # [canonical: §2.2 Town/Outpost row — "No modifier"]
    'Town':    SettlementTypeModifier(0, 0, 0, False, False, False),
    'Outpost': SettlementTypeModifier(0, 0, 0, False, False, False),
    # §1.2 'City' is in canonical-eight types but §2.2 table doesn't list
    # it explicitly. Module 7 treats it as zero-modifier (same as Town/Outpost).
    # See finding F15 below.
    'City':    SettlementTypeModifier(0, 0, 0, False, False, False),
}


# [FINDING F15] adjacency §2.2 settlement-type modifier table lists six
# of §1.2's eight canonical types (Fortress / Seat / Port / Cathedral /
# Mine / Town / Outpost) but omits **City**. The §1.2 canonical type
# 'City' has no entry in §2.2's defender-modifier table.
#
# Module 7 provisionally treats City the same as Town/Outpost (zero modifier).
# This may be intentional (Cities are simply "no modifier" along with
# Town/Outpost, just not listed) but the omission is structurally suspicious
# given City is a §1.2 canonical type and gets specific treatment elsewhere
# (§1.4.1 facility matrix has a distinct City row; §3.2 governor table has
# distinct Lieutenant-tier City eligibility).
#
# Editorial decision needed: confirm City is intentionally "no modifier"
# in §2.2, or add a City row with the canonically-intended modifier.


# [FINDING F14] §5.1 example references and §3 example reference are stale
# pre-PP-726 settlement IDs and types:
#
# §5.1: "Lowenskyst Fortress (S-006, Defense 4) requires Military 7+ to bypass"
#   - S-006 in canonical post-PP-726 registry is Goldenfurt (Town, Kronmark),
#     NOT a Fortress named Lowenskyst.
#
# adjacency §3: "Hafenmark army at S-015 Gransol Parliament wishes to invade
#   T2 Kronmark. Gransol is adjacent (via road edge) to S-012 Kronburg Seat.
#   ... It cannot leap to S-014 Kronmark Cathedral..."
#   - S-015 is Nordhain (Village, Ehrenfeld), NOT Gransol Parliament.
#     Gransol is S-018 (City, Gransol province).
#   - S-012 is Stillhelm (Town), NOT Kronburg Seat. The Valorsmark Seat is
#     S-002 (Valorsplatz, per M1 registry).
#   - S-014 is Ehrenfeld (Fortress-City), NOT Kronmark Cathedral. Kronmark
#     itself is S-004 (Town, no Cathedral district per current settlement
#     name).
#
# These are pre-PP-726 example IDs left in design docs after the §2.1
# rebuild. The mechanical content (Bypass margin = 2; Fortress bypass margin
# = 3; Lowenskyst Defense 4 → required Military 7) is canonically valid;
# only the S-IDs and settlement-name examples are stale.
#
# Sixth distinct surfacing of the canonical type-taxonomy / S-ID drift
# family (F1, F7, F10, F11, F12, F14).


# ── Resolution: Assault ─────────────────────────────────────────────────────

@dataclass(frozen=True)
class AssaultResult:
    """§5.1 + adjacency §2.3 Assault outcome."""
    outcome: str                          # 'captured' | 'repelled'
    settlement_captured: bool
    casus_belli_imposed: bool             # §2.2 Cathedral
    prosperity_captured: int              # §2.2 Mine
    casualties_attacker: int              # provisional placeholder
    casualties_defender: int              # provisional placeholder
    settlement_order_delta: int           # §2.3 "Accord drop ... Order -1"
    settlement_prosperity_delta: int      # §2.3 "Prosperity -1 on Partial+"
    faction_standing_delta: int
    renown_delta: int


def resolve_assault(
    settlement: Settlement,
    stats: SettlementStats,
    garrison: Optional[Garrison],
    attacker_military: int,
    edge_traversed: str,
    attacker_roll: int,
) -> AssaultResult:
    """§5.1 Assault resolution.
    Combines: terrain modifier (edge_type), settlement-type modifier
    (defender), garrison contribution to effective Defense, and the
    attacker roll.

    Returns AssaultResult. Mutates `stats` per adjacency §2.3 consequences:
    Order -1 on any assault outcome; Prosperity -1 on Partial+ (provisional:
    Module 7 treats all 'repelled' outcomes as Partial+ for Prosperity loss
    since the canon doesn't separate Partial from Failure at settlement scope).
    """
    # Pre-flight: auto-capture path
    if is_auto_capture(stats, garrison):
        return _apply_assault_outcome(
            settlement, stats, captured=True,
            partial_or_worse=True, mods=SETTLEMENT_TYPE_MODIFIER_BY_TYPE.get(
                settlement.type, SettlementTypeModifier(0, 0, 0, False, False, False)),
            attacker_casualties=0, defender_casualties=0,
        )

    # Get modifiers
    terrain = terrain_modifier(edge_traversed)
    type_mod = SETTLEMENT_TYPE_MODIFIER_BY_TYPE.get(
        settlement.type,
        SettlementTypeModifier(0, 0, 0, False, False, False),
    )

    eff_def = effective_defense(stats, garrison)
    # Apply defender Discipline bonus from settlement type (Seat +1)
    eff_def += type_mod.defender_discipline_delta

    # Apply terrain modifier to attacker effective military
    eff_attacker = attacker_military + terrain.attacker_dice_delta + attacker_roll

    captured = eff_attacker > eff_def
    # Provisional casualty placeholder values — sim_mb_06 owns these
    # mechanically; Module 7 just surfaces.
    # [canonical: derived attacker-vs-defender from §5.1 — "attacker takes casualties"]
    attacker_casualties = max(0, eff_def - attacker_military) if not captured else 0
    defender_casualties = max(0, attacker_military - eff_def) if captured else 0

    return _apply_assault_outcome(
        settlement, stats, captured=captured,
        partial_or_worse=True,   # any assault outcome triggers §2.3 cost
        mods=type_mod,
        attacker_casualties=attacker_casualties,
        defender_casualties=defender_casualties,
    )


def _apply_assault_outcome(
    settlement: Settlement,
    stats: SettlementStats,
    captured: bool,
    partial_or_worse: bool,
    mods: SettlementTypeModifier,
    attacker_casualties: int,
    defender_casualties: int,
) -> AssaultResult:
    """Internal: apply adjacency §2.3 consequences to `stats`.
    Returns AssaultResult."""
    # §2.3 Accord drop → settlement Order -1
    order_delta = -1
    new_order = max(STAT_MIN, stats.order + order_delta)
    stats.order = new_order

    # §2.3 Prosperity -1 on Partial or worse
    prosperity_delta = -1 if partial_or_worse else 0
    if prosperity_delta != 0:
        new_pros = max(STAT_MIN, stats.prosperity + prosperity_delta)
        stats.prosperity = new_pros

    # §2.2 Mine — attacker captures Prosperity on victory
    captured_prosperity = (stats.prosperity
                           if captured and mods.attacker_captures_prosperity_on_victory
                           else 0)

    return AssaultResult(
        outcome='captured' if captured else 'repelled',
        settlement_captured=captured,
        casus_belli_imposed=mods.attacker_casus_belli,
        prosperity_captured=captured_prosperity,
        casualties_attacker=attacker_casualties,
        casualties_defender=defender_casualties,
        settlement_order_delta=order_delta,
        settlement_prosperity_delta=prosperity_delta,
        # signal direction: captured = defender loses standing (faction_standing
        # _delta < 0 from defender's perspective); attacker gains. Module 7
        # surfaces from defender's perspective (the settlement's controller's).
        faction_standing_delta=(-2 if captured else -1),
        renown_delta=(-2 if captured else -1),
    )


# ── Resolution: Siege ───────────────────────────────────────────────────────

@dataclass
class SiegeState:
    """§5.1 + §2.4 Siege state. Persists across seasons until surrender."""
    settlement_id: str
    attacker_faction: str
    season_started: int   # absolute season count; Module 9 binds calendar
    seasons_elapsed: int = 0


def resolve_siege_tick(
    siege: SiegeState,
    stats: SettlementStats,
) -> Tuple[ActionResult, bool]:
    """§5.1 + §2.4 Siege per-season tick.
    Each season: defender Order -1. Returns (ActionResult, surrender_flag).
    `surrender_flag` is True when Order has dropped to SIEGE_SURRENDER_ORDER_THRESHOLD.
    """
    new_order = max(STAT_MIN, stats.order - SIEGE_ORDER_DECREMENT_PER_SEASON)
    order_delta = new_order - stats.order
    stats.order = new_order
    siege.seasons_elapsed += 1
    surrender = stats.order <= SIEGE_SURRENDER_ORDER_THRESHOLD
    return (
        ActionResult(
            success=True,
            reason=('siege_surrender' if surrender else 'siege_tick'),
            state_mutated=(order_delta != 0 or surrender),
            faction_standing_delta=(-2 if surrender else -1),
            renown_delta=(-2 if surrender else -1),
        ),
        surrender,
    )


# ── Resolution: Bypass + supply-strike ──────────────────────────────────────

@dataclass
class BypassState:
    """§5.1 Bypass state: bypassed settlement remains hostile and its garrison
    can attack the invader's supply line each season."""
    settlement_id: str
    invader_faction: str
    seasons_elapsed: int = 0


def resolve_bypass_supply_strike(
    bypass: BypassState,
    bypassed_garrison_military: int,
    roll: int,
) -> ActionResult:
    """§5.1 Bypass — bypassed garrison's per-season supply attack.
    Military vs Ob 1 each season. Success: invader takes -1 Discipline
    on all units in the province.
    """
    if bypassed_garrison_military < 1:
        # No garrison can't strike supply lines
        return ActionResult(
            success=False, reason='no_bypass_garrison',
            state_mutated=False,
        )
    success = roll >= BYPASS_SUPPLY_STRIKE_OB
    bypass.seasons_elapsed += 1
    return ActionResult(
        success=success,
        reason=('supply_strike_success' if success else 'supply_strike_failed'),
        state_mutated=success,
        # Discipline delta is downstream — Module 12 applies the
        # province-wide -1 Discipline to invader units; M7 surfaces the
        # signal via faction_standing_delta.
        faction_standing_delta=(-1 if success else 0),
        renown_delta=0,
    )


# ── §5.1 post-Seat-capture resistance check ─────────────────────────────────

def settlement_resists_post_seat_capture(stats: SettlementStats) -> bool:
    """§5.1 — When the Seat is captured, non-Seat settlements with Order ≥ 3
    may resist (maintaining their current governor).
    """
    return stats.order >= POST_SEAT_CAPTURE_RESIST_ORDER_THRESHOLD


# ── §4.3 Fortress mobilization check (referenced by M6 predicate) ───────────

# [canonical: settlement_layer_v30 §4.3 Fortress Garrison Mobilization —
#  "Defense check: Defense pool vs Ob 2. Success: settlement holds.
#  Failure: attacker bypasses or captures."]
FORTRESS_MOBILIZE_HOLD_OB: int = 2


def fortress_mobilize_check(
    stats: SettlementStats,
    garrison: Optional[Garrison],
    defense_pool_roll: int,
) -> bool:
    """§4.3 Fortress garrison mobilization Defense check.
    Returns True if settlement holds; False if attacker bypasses/captures.
    """
    eff_def = effective_defense(stats, garrison)
    return defense_pool_roll + eff_def >= FORTRESS_MOBILIZE_HOLD_OB


# ── §3 Invasion Sequencing — path-constrained movement ──────────────────────

def can_jump_to_settlement(
    invader_position: str,
    target_settlement_id: str,
) -> bool:
    """adjacency §3: an invader may only move to settlements they are
    adjacent to. They cannot jump to arbitrary settlements in the province.
    [canonical: settlement_adjacency_v30 §3 — 'They cannot jump to
     arbitrary settlements in the province.']
    """
    return target_settlement_id in neighbors(invader_position)


# ── Garrison reinforcement action (maintenance arm) ─────────────────────────

# §5.2 "Each settlement can host a garrison (one military unit)"
# [canonical: settlement_layer_v30 §5.2 —
#  "Each settlement can host a garrison (one military unit)"]
MAX_GARRISONS_PER_SETTLEMENT: int = 1


def reinforce_garrison(
    garrison: Optional[Garrison],
    settlement: Settlement,
    new_unit_id: str,
    new_discipline: int,
) -> ActionResult:
    """Maintenance action: install a garrison at a settlement.
    Pure-state mutation; no Ob roll (administrative — equivalent to
    domain-action level decision)."""
    if garrison is None:
        return ActionResult(
            success=False,
            reason='garrison_object_required',
            state_mutated=False,
        )
    if has_garrison(garrison):
        # Replace? §5.2 says one unit at a time. Module 7 treats reinforce
        # of an already-garrisoned settlement as a replacement decision.
        return ActionResult(
            success=False,
            reason='garrison_already_present',
            state_mutated=False,
        )
    garrison.unit_id = new_unit_id
    garrison.discipline = new_discipline
    return ActionResult(
        success=True,
        reason='garrison_installed',
        state_mutated=True,
        faction_standing_delta=+1,
        renown_delta=0,   # garrisoning is invisible maintenance work
    )


# ── Isolation tests ─────────────────────────────────────────────────────────

def run_isolation_tests() -> Dict[str, str]:
    r: Dict[str, str] = {}

    # T1 — MilitaryAction enum has exactly three values per §5.1
    # [canonical: §5.1 — three actions Assault, Siege, Bypass]
    expected_action_count = 3
    r['T1_three_military_actions'] = (
        'PASS' if len(MilitaryAction) == expected_action_count else 'FAIL'
    )

    # T2 — effective_defense without garrison == settlement Defense
    stats_a = SettlementStats(prosperity=2, defense=3, order=3)
    r['T2_eff_def_no_garrison'] = (
        'PASS' if effective_defense(stats_a, None) == 3 else 'FAIL'
    )

    # T3 — effective_defense with garrison adds Discipline
    g_a = Garrison(settlement_id='S-001', unit_id='U-1', discipline=2)
    # [canonical: §5.2 — settlement Defense + garrison Discipline]
    expected_eff_def_garrisoned = 5  # 3 + 2
    r['T3_eff_def_with_garrison'] = (
        'PASS' if effective_defense(stats_a, g_a) == expected_eff_def_garrisoned
        else f'FAIL ({effective_defense(stats_a, g_a)})'
    )

    # T4 — effective_defense ignores garrison with no unit_id
    g_empty = Garrison(settlement_id='S-001', unit_id=None, discipline=2)
    r['T4_eff_def_empty_garrison_slot'] = (
        'PASS' if effective_defense(stats_a, g_empty) == 3 else 'FAIL'
    )

    # T5 — is_auto_capture: Defense 0 + no garrison
    stats_d0 = SettlementStats(prosperity=2, defense=0, order=2)
    r['T5_auto_capture_defense_0_no_garrison'] = (
        'PASS' if is_auto_capture(stats_d0, None) else 'FAIL'
    )

    # T6 — is_auto_capture: Defense 0 with garrison: NOT auto-capture
    g_d0 = Garrison(settlement_id='S-001', unit_id='U-1', discipline=1)
    r['T6_auto_capture_defense_0_garrisoned_no'] = (
        'PASS' if not is_auto_capture(stats_d0, g_d0) else 'FAIL'
    )

    # T7 — is_auto_capture: Defense 1, no garrison: NOT auto-capture
    stats_d1 = SettlementStats(prosperity=2, defense=1, order=2)
    r['T7_auto_capture_defense_1_no_garrison_no'] = (
        'PASS' if not is_auto_capture(stats_d1, None) else 'FAIL'
    )

    # T8 — can_bypass: Town with Defense 2 vs Military 4 (margin 2): success
    stats_town = SettlementStats(prosperity=2, defense=2, order=3)
    r['T8_bypass_town_margin_2'] = (
        'PASS' if can_bypass(4, 2, 'Town') else 'FAIL'
    )

    # T9 — can_bypass: Town with Defense 2 vs Military 3 (margin 1): fail
    r['T9_bypass_town_margin_1_fails'] = (
        'PASS' if not can_bypass(3, 2, 'Town') else 'FAIL'
    )

    # T10 — Fortress bypass requires margin 3 — F14 canonical worked example
    # [canonical: §5.1 "Lowenskyst Fortress ... Defense 4 ... requires
    #  Military 7+ to bypass"]
    # (NB: F14 — S-006 in actual registry is Goldenfurt Town, not Lowenskyst
    # Fortress. But the mechanical claim Military > Defense + 3 is canonical.)
    expected_lowenskyst_military_to_bypass = 7
    r['T10_fortress_bypass_margin_3'] = (
        'PASS' if (can_bypass(expected_lowenskyst_military_to_bypass, 4, 'Fortress')
                   and not can_bypass(6, 4, 'Fortress'))
        else 'FAIL'
    )

    # T11 — can_siege: Military >= Defense
    r['T11_siege_military_geq_defense'] = (
        'PASS' if (can_siege(3, 3) and not can_siege(2, 3)) else 'FAIL'
    )

    # T12 — terrain modifier: road == zero
    # [canonical: §2.2 — "Road | none"]
    r['T12_terrain_road_zero'] = (
        'PASS' if terrain_modifier('road').attacker_dice_delta == 0 else 'FAIL'
    )

    # T13 — terrain modifier: river == attacker -1D
    # [canonical: §2.2 — "River | Attacker −1D"]
    expected_river_delta = -1
    r['T13_terrain_river_minus_1'] = (
        'PASS' if terrain_modifier('river').attacker_dice_delta == expected_river_delta
        else 'FAIL'
    )

    # T14 — terrain modifier: mountain_pass == attacker -1D
    # [canonical: §2.2 — "Mountain Pass | Attacker −1D (fatigue)"]
    r['T14_terrain_pass_minus_1'] = (
        'PASS' if terrain_modifier('mountain_pass').attacker_dice_delta == -1
        else 'FAIL'
    )

    # T15 — terrain modifier: coastal sets fort-level-bonus loss flag
    # [canonical: §2.2 — "Coastal (naval) | Attacker loses Fort-level bonus"]
    r['T15_terrain_coastal_loses_fort_bonus'] = (
        'PASS' if terrain_modifier('coastal').attacker_loses_fort_level_bonus
        else 'FAIL'
    )

    # T16 — Seat defender +1 Discipline modifier
    # [canonical: §2.2 — "Seat | +1 Defender Discipline"]
    expected_seat_discipline_delta = 1
    r['T16_seat_discipline_bonus'] = (
        'PASS' if SETTLEMENT_TYPE_MODIFIER_BY_TYPE['Seat'].defender_discipline_delta == expected_seat_discipline_delta
        else 'FAIL'
    )

    # T17 — Cathedral imposes attacker Casus Belli flag
    # [canonical: §2.2 — "Cathedral | Attacker takes Church Casus Belli"]
    r['T17_cathedral_casus_belli'] = (
        'PASS' if SETTLEMENT_TYPE_MODIFIER_BY_TYPE['Cathedral'].attacker_casus_belli
        else 'FAIL'
    )

    # T18 — Mine attacker captures Prosperity on victory flag
    # [canonical: §2.2 — "Mine | Attacker gains captured Prosperity on victory"]
    r['T18_mine_attacker_prosperity'] = (
        'PASS' if SETTLEMENT_TYPE_MODIFIER_BY_TYPE['Mine'].attacker_captures_prosperity_on_victory
        else 'FAIL'
    )

    # T19 — Fortress fort_level_applies flag
    # [canonical: §2.2 — "Fortress | +Fort Level to Defender Ob"]
    r['T19_fortress_fort_level_flag'] = (
        'PASS' if SETTLEMENT_TYPE_MODIFIER_BY_TYPE['Fortress'].fort_level_applies
        else 'FAIL'
    )

    # T20 — F15: City has zero modifiers (provisional)
    city_mod = SETTLEMENT_TYPE_MODIFIER_BY_TYPE['City']
    ok = (city_mod.defender_discipline_delta == 0
          and not city_mod.attacker_casus_belli
          and not city_mod.fort_level_applies)
    r['T20_F15_city_zero_modifier'] = 'PASS' if ok else 'FAIL'

    # T21 — Assault outcome: captured (high attacker military)
    settlement_seat = by_id('S-001')   # Almund's Seat (Seat)
    stats_seat = SettlementStats(prosperity=4, defense=3, order=4)
    g_seat = Garrison(settlement_id='S-001', unit_id='U-1', discipline=2)
    result = resolve_assault(
        settlement_seat, stats_seat, g_seat,
        attacker_military=20, edge_traversed='road', attacker_roll=5,
    )
    r['T21_assault_captured_high_military'] = (
        'PASS' if result.settlement_captured else f'FAIL ({result})'
    )

    # T22 — Assault outcome: repelled (low attacker military)
    settlement_town = Settlement(id='S-XXX', name='TestTown', type='Town',
                                  province='X', duchy='X', role='x')
    stats_town2 = SettlementStats(prosperity=2, defense=3, order=3)
    result = resolve_assault(
        settlement_town, stats_town2, None,
        attacker_military=1, edge_traversed='road', attacker_roll=1,
    )
    r['T22_assault_repelled_low_military'] = (
        'PASS' if not result.settlement_captured else f'FAIL ({result})'
    )

    # T23 — Assault on auto-capture (Defense 0 + no garrison)
    stats_d0b = SettlementStats(prosperity=2, defense=0, order=2)
    result = resolve_assault(
        settlement_town, stats_d0b, None,
        attacker_military=1, edge_traversed='road', attacker_roll=1,
    )
    r['T23_assault_auto_capture'] = (
        'PASS' if result.settlement_captured else f'FAIL ({result})'
    )

    # T24 — Assault applies §2.3 Order -1
    stats_t24 = SettlementStats(prosperity=4, defense=3, order=4)
    g_t24 = Garrison(settlement_id='S-001', unit_id='U-1', discipline=1)
    result = resolve_assault(
        settlement_seat, stats_t24, g_t24,
        attacker_military=10, edge_traversed='road', attacker_roll=3,
    )
    # [canonical: §2.3 — "Accord drop ... settlement's Order (Order -1)"]
    expected_order_after = 3   # 4 -1
    r['T24_assault_order_decrement'] = (
        'PASS' if stats_t24.order == expected_order_after else f'FAIL ({stats_t24.order})'
    )

    # T25 — Assault applies §2.3 Prosperity -1
    # [canonical: §2.3 — "Settlement Prosperity −1 on Assault outcome Partial or worse"]
    expected_prosperity_after = 3   # 4 -1
    r['T25_assault_prosperity_decrement'] = (
        'PASS' if stats_t24.prosperity == expected_prosperity_after
        else f'FAIL ({stats_t24.prosperity})'
    )

    # T26 — Cathedral assault imposes Casus Belli on attacker
    settlement_cath = Settlement(id='S-XXX', name='TestCath', type='Cathedral',
                                  province='X', duchy='X', role='x')
    stats_cath = SettlementStats(prosperity=3, defense=2, order=3)
    result = resolve_assault(
        settlement_cath, stats_cath, None,
        attacker_military=10, edge_traversed='road', attacker_roll=3,
    )
    r['T26_cathedral_assault_casus_belli'] = (
        'PASS' if result.casus_belli_imposed else f'FAIL ({result})'
    )

    # T27 — Mine assault captures Prosperity on victory
    settlement_mine = Settlement(id='S-XXX', name='TestMine', type='Mine',
                                  province='X', duchy='X', role='x')
    stats_mine = SettlementStats(prosperity=4, defense=1, order=3)
    result = resolve_assault(
        settlement_mine, stats_mine, None,
        attacker_military=10, edge_traversed='road', attacker_roll=3,
    )
    # captured + Mine -> captured Prosperity (post-decrement value: was 4 → 3 post-§2.3)
    ok = (result.settlement_captured
          and result.prosperity_captured > 0)
    r['T27_mine_assault_captures_prosperity'] = (
        'PASS' if ok else f'FAIL ({result})'
    )

    # T28 — Siege tick decrements Order
    siege_state = SiegeState(settlement_id='S-001',
                              attacker_faction='Hafenmark', season_started=0)
    stats_siege = SettlementStats(prosperity=3, defense=3, order=3)
    result, surrender = resolve_siege_tick(siege_state, stats_siege)
    # [canonical: §5.1 Siege — "Each season: defender Order -1"]
    expected_order_after_tick = 2
    ok = (stats_siege.order == expected_order_after_tick
          and not surrender
          and siege_state.seasons_elapsed == 1)
    r['T28_siege_tick_decrements_order'] = (
        'PASS' if ok else f'FAIL (order={stats_siege.order}, elapsed={siege_state.seasons_elapsed})'
    )

    # T29 — Siege surrender when Order reaches 0
    # Order is at 2 after T28; need two more ticks to reach 0
    resolve_siege_tick(siege_state, stats_siege)   # 1
    result, surrender = resolve_siege_tick(siege_state, stats_siege)  # 0
    r['T29_siege_surrender_at_order_0'] = (
        'PASS' if surrender and stats_siege.order == SIEGE_SURRENDER_ORDER_THRESHOLD
        else f'FAIL (order={stats_siege.order}, surrender={surrender})'
    )

    # T30 — Bypass supply-strike success (roll >= Ob 1)
    bypass_state = BypassState(settlement_id='S-001',
                                invader_faction='Hafenmark')
    result = resolve_bypass_supply_strike(bypass_state,
                                           bypassed_garrison_military=2, roll=2)
    # [canonical: §5.1 Bypass — "Military vs Ob 1 each season: success =
    #  invader takes -1 Discipline"]
    r['T30_bypass_supply_strike_success'] = (
        'PASS' if result.success else f'FAIL ({result})'
    )

    # T31 — Bypass supply-strike failure (roll < Ob)
    bypass_state2 = BypassState(settlement_id='S-001',
                                 invader_faction='Hafenmark')
    result = resolve_bypass_supply_strike(bypass_state2,
                                           bypassed_garrison_military=2, roll=0)
    r['T31_bypass_supply_strike_failure'] = (
        'PASS' if not result.success else 'FAIL'
    )

    # T32 — Bypass supply-strike no-garrison case
    bypass_state3 = BypassState(settlement_id='S-001',
                                 invader_faction='Hafenmark')
    result = resolve_bypass_supply_strike(bypass_state3,
                                           bypassed_garrison_military=0, roll=5)
    r['T32_bypass_no_garrison_no_strike'] = (
        'PASS' if not result.success and result.reason == 'no_bypass_garrison'
        else 'FAIL'
    )

    # T33 — settlement_resists_post_seat_capture at Order 3
    stats_r3 = SettlementStats(prosperity=2, defense=1, order=3)
    stats_r2 = SettlementStats(prosperity=2, defense=1, order=2)
    ok = (settlement_resists_post_seat_capture(stats_r3)
          and not settlement_resists_post_seat_capture(stats_r2))
    r['T33_post_seat_resist_at_order_3'] = 'PASS' if ok else 'FAIL'

    # T34 — Fortress mobilize check
    stats_fort = SettlementStats(prosperity=2, defense=2, order=3)
    g_fort = Garrison(settlement_id='S-001', unit_id='U-1', discipline=1)
    # eff_def = 2+1 = 3; Ob = 2; roll 0 + 3 = 3 >= 2 → holds
    ok = fortress_mobilize_check(stats_fort, g_fort, defense_pool_roll=0)
    r['T34_fortress_mobilize_holds'] = 'PASS' if ok else 'FAIL'

    # T35 — Fortress mobilize check failure (no garrison + Defense 1 + roll 0)
    stats_weak = SettlementStats(prosperity=2, defense=1, order=2)
    # eff_def = 1; Ob = 2; roll 0 + 1 = 1 < 2 → fails
    ok = not fortress_mobilize_check(stats_weak, None, defense_pool_roll=0)
    r['T35_fortress_mobilize_fails'] = 'PASS' if ok else 'FAIL'

    # T36 — can_jump_to_settlement: adjacent passes
    s001_neighbors = set(neighbors('S-001'))
    if s001_neighbors:
        any_neighbor = next(iter(s001_neighbors))
        r['T36_can_jump_adjacent_passes'] = (
            'PASS' if can_jump_to_settlement('S-001', any_neighbor) else 'FAIL'
        )
    else:
        r['T36_can_jump_adjacent_passes'] = 'SKIP (no neighbors)'

    # T37 — can_jump_to_settlement: non-adjacent fails
    # Pick a settlement NOT in S-001's neighbors
    non_neighbor = None
    for s in REGISTRY:
        if s.id != 'S-001' and s.id not in s001_neighbors:
            non_neighbor = s.id
            break
    if non_neighbor:
        r['T37_cannot_jump_non_adjacent'] = (
            'PASS' if not can_jump_to_settlement('S-001', non_neighbor) else 'FAIL'
        )
    else:
        r['T37_cannot_jump_non_adjacent'] = 'SKIP'

    # T38 — Garrison reinforce installs unit
    g_slot = Garrison(settlement_id='S-001', unit_id=None, discipline=0)
    settle_x = by_id('S-001')
    result = reinforce_garrison(g_slot, settle_x,
                                 new_unit_id='U-NEW', new_discipline=3)
    r['T38_garrison_reinforce_installs'] = (
        'PASS' if result.success and g_slot.unit_id == 'U-NEW' and g_slot.discipline == 3
        else f'FAIL ({result})'
    )

    # T39 — Garrison reinforce rejects already-garrisoned slot
    result = reinforce_garrison(g_slot, settle_x,
                                 new_unit_id='U-OTHER', new_discipline=5)
    r['T39_garrison_reinforce_rejects_full'] = (
        'PASS' if not result.success and result.reason == 'garrison_already_present'
        else 'FAIL'
    )

    # T40 — Emergent composition with M6: an undefended Defense-0 town
    # auto-captures and the M6 raid-predicate would have fired the previous
    # season. Validate that M7's auto-capture + M6's predicate compose:
    from module_06_events import predicate_raid_or_siege
    stats_emergent = SettlementStats(prosperity=2, defense=0, order=2)
    # M6 predicate fires when Defense=0 + adjacent hostile
    m6_fires = predicate_raid_or_siege(stats_emergent, adjacent_hostile=True)
    # M7 auto-capture predicate fires when Defense=0 + no garrison
    m7_auto = is_auto_capture(stats_emergent, None)
    ok = m6_fires and m7_auto
    r['T40_emergent_m6_m7_composition'] = 'PASS' if ok else 'FAIL'

    # T41 — Siege from M6 raid-event triggers M7 resolve_siege_tick over seasons
    # Bottom-up emergent: M6 predicate fires once, M7 ticks for multiple seasons,
    # cumulative state mutation eventually triggers M6's local-revolt predicate
    # (Order 0 → revolt fires) — no authored link between siege and revolt.
    stats_chain = SettlementStats(prosperity=3, defense=3, order=3)
    siege_chain = SiegeState(settlement_id='S-001',
                              attacker_faction='Hafenmark', season_started=0)
    from module_06_events import predicate_local_revolt
    revolt_fired_at_season = None
    for season in range(1, 6):
        resolve_siege_tick(siege_chain, stats_chain)
        if predicate_local_revolt(stats_chain):
            revolt_fired_at_season = season
            break
    # Order: 3 → 2 → 1 → 0 → 0 ... revolt fires at season 3 (Order reaches 0)
    expected_revolt_season = 3
    r['T41_emergent_siege_to_revolt_chain'] = (
        'PASS' if revolt_fired_at_season == expected_revolt_season
        else f'FAIL (revolt at season {revolt_fired_at_season})'
    )

    return r


if __name__ == '__main__':
    import sys
    results = run_isolation_tests()
    width = max(len(k) for k in results)
    header = "Module 07 — military granularity — isolation tests"
    bar_width = max(width, len(header))
    print("=" * bar_width)
    print(header)
    print("=" * bar_width)
    fail = False
    for k, v in results.items():
        marker = '✓' if v == 'PASS' else ('⊘' if v.startswith('SKIP') else '✗')
        print(f"  {marker} {k:<{width}} {v}")
        if v != 'PASS' and not v.startswith('SKIP'):
            fail = True
    print("=" * bar_width)
    print(f"Military actions: {[a.value for a in MilitaryAction]}")
    print(f"Bypass margin: standard {BYPASS_MIN_MILITARY_MARGIN} / fortress {FORTRESS_BYPASS_MIN_MARGIN}")
    print(f"Terrain edge types covered: {sorted(TERRAIN_MODIFIER_BY_EDGE_TYPE.keys())}")
    print(f"Settlement-type modifiers: {sorted(SETTLEMENT_TYPE_MODIFIER_BY_TYPE.keys())}")
    sys.exit(1 if fail else 0)
