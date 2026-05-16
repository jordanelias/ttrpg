# m1_church_infrastructure — Module One of the v17 strategic-sim integration plan.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical primitives for the Church's four-axis settlement infrastructure model,  # [canonical: N/A — doc]
# SW-weighted Piety Yield, the canonical Mass-Seizure Ob formula, Parish Social  # [canonical: N/A — doc]
# Services, and the Pastoral Assumption Domain Action.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# This module is intentionally PURE PRIMITIVES — it exposes data + computational  # [canonical: N/A — doc]
# functions only. It does not own the World/Faction/Territory classes (those live  # [canonical: N/A — doc]
# in mc_v15) and does not run a simulation by itself. The integration module  # [canonical: N/A — doc]
# wires these primitives into the next-version sim.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources (force_full reads required to validate this module):  # [canonical: N/A — doc]
#   - settlement_layer_v30 Axis specification, Parish Social Services, Pastoral  # [canonical: N/A — doc]
#     Assumption, and the canonical Settlement Registry.  # [canonical: N/A — doc]
#   - ci_political_v30 Spiritual Weight table and CI milestone table.  # [canonical: N/A — doc]
#   - victory_v30 Church-of-Solmund strategy section (Mass Seizure mechanics).  # [canonical: N/A — doc]
#   - settlement_layer cross-references campaign_architecture for the canonical  # [canonical: N/A — doc]
#     four-axis specification.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Mode G compliance: every mechanical constant carries an inline canonical tag  # [canonical: N/A — doc]
# alongside its declaration. Verification ledger at sim_verification_ledger.json.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional decisions (held provisionally per Jordan directive — mark with  # [canonical: N/A — doc]
# ASSUMPTION_N tags in code and ratify in editorial ledger before integration runs).  # [canonical: N/A — doc]
# Full prose justifications live in sim_verification_ledger.json's  # [canonical: N/A — doc]
# provisional_assumptions section. Tags ASSUMPTION_ONE through ASSUMPTION_SIX  # [canonical: N/A — doc]
# correspond to GAP-A through GAP-F in the M1 design audit.  # [canonical: N/A — doc]
import sys
import os
import math
from dataclasses import dataclass, field
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════

# Religious Building enum (Axis 1 — mutually exclusive)
# [canonical: settlement_layer_v30 §1.5 Axis 1]
RB_NONE = 'None'
RB_CHAPEL = 'Chapel'
RB_CHURCH = 'Church'
RB_CATHEDRAL = 'Cathedral'
RELIGIOUS_BUILDINGS = (RB_NONE, RB_CHAPEL, RB_CHURCH, RB_CATHEDRAL)

# PT generation per season per Religious Building (in territory)
# [canonical: settlement_layer_v30 §1.5 Axis 1]
PT_YIELD_PER_RB = {
    RB_NONE: 0.0,
    RB_CHAPEL: 0.5,
    RB_CHURCH: 1.0,
    RB_CATHEDRAL: 2.0,
}

# Cathedral additional PT bonus to each direct-adjacent territory
# [canonical: settlement_layer_v30 §1.5 Axis 1]
# [ASSUMPTION-4: stacks per Cathedral, direct-adjacent only, no cap, no decay]
PT_CATHEDRAL_ADJACENCY_BONUS = 0.5

# Per-axis Seizure Ob modifiers (stacking per settlement)
# [canonical: settlement_layer_v30 §1.5 + victory_v30 §3.2]
SEIZURE_OB_MODIFIER = {
    'chapel':       0,   # Chapel  −0
    'church':      -1,   # Church  −1
    'cathedral':   -2,   # Cathedral −2
    'templar':     -1,   # Templar Station −1
    'inquisitor':  -1,   # Inquisitor Base −1
    'governor':    -2,   # Church Governor −2
}

# Cap on stacked modifiers PER SETTLEMENT
# [canonical: settlement_layer_v30 §1.5 — "Cap: −4 per settlement"]
SEIZURE_OB_PER_SETTLEMENT_CAP = -4

# Seizure Ob base formula floor (cannot go below 1)
# [canonical: victory_v30 §3.2]
SEIZURE_OB_FLOOR = 1

# Spiritual Weight per territory (fixed attribute, set at game start)
# [canonical: ci_political_v30 §1 — Spiritual Weight table]
SPIRITUAL_WEIGHT = {
    'T1':  2,   # Valorsplatz — seat of secular power
    'T2':  2,   # Kronmark
    'T3':  2,   # Lowenskyst
    'T4':  1,   # Grauwald
    'T5':  2,   # Feldmark
    'T6':  1,   # Stillhelm
    'T7':  2,   # Rendstad
    'T8':  3,   # Gransol — trading city, Church commercial presence
    'T9':  5,   # Himmelenger — Church's primary anchor
    'T10': 2,   # Spartfell
    'T11': 1,   # Halvardshelm
    'T12': 2,   # Sigurdshelm
    'T13': 1,   # Oastad
    'T14': 3,   # Ehrenfeld — military stronghold w/ Church benediction tradition
    'T15': 0,   # Askeheim — Calamity ground, Church presence impossible
    'T16': 1,   # Schoenland (foreign, inert in sim)
    'T17': 2,   # Halvarshelm
}
SW_TOTAL_CANONICAL = 32  # ci_political_v30 §1 table foot

# Parish Social Services — Order/Stability effects per Religious Building
# [canonical: settlement_layer_v30 §1.6]
# Returns a structured dict so M5 (Settlement-Territory Aggregation) can apply.
PARISH_ORDER_RULES = {
    RB_NONE: {'order_per_season': 0.0, 'order_install_bonus': 0, 'order_decay_modifier': 0},
    RB_CHAPEL: {'order_per_season': 0.5, 'order_install_bonus': 0, 'order_decay_modifier': 0},
    RB_CHURCH: {'order_per_season': 0.0, 'order_install_bonus': 1, 'order_decay_modifier': 0},
    RB_CATHEDRAL: {'order_per_season': 0.0, 'order_install_bonus': 1, 'order_decay_modifier': -1},
}

# CI milestones — effects gated by current world.clocks['CI']
# [canonical: ci_political_v30 §2.1 milestone table + victory_v30 §3.2 §CI=100]
CI_MILESTONE_ASCENDANT = 80      # Seizure Ob −1 global, PT drift +1 at YE
CI_MILESTONE_UNIFICATION = 100   # Theocracy Unification Attempt
CI_MASS_SEIZURE_AVAILABLE = 60   # Mass Seizure threshold (one-shot bid)

# Mass Seizure declaration probability formula
# [canonical: victory_v30 §3.2 — P(declare) = ((CI−60)/40)^3.3, clamped [0,1]]
MASS_SEIZURE_DECLARE_EXPONENT = 3.3
MASS_SEIZURE_DECLARE_RANGE = 40.0  # [canonical: victory_v30 Mass Seizure formula — (CI-60)/40]

# Mass Seizure Pool bonus from CI: floor(CI/15)
# [canonical: victory_v30 §3.2 — Pool = Influence + floor(CI/15)]
MASS_SEIZURE_POOL_DIVISOR = 15

# CI bonus dice to Church in political forums: floor(CI/20)
# [canonical: ci_political_v30 §3.2] — M2 territory, declared here for completeness
CI_POLITICAL_BONUS_DIVISOR = 20

# Playable territories (M1 sim scope)
# [ASSUMPTION-3: matches mc_v15 ALL_PLAYABLE_15 = T1..T14, T17]
PLAYABLE_TERRITORIES = frozenset({
    'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9',
    'T10', 'T11', 'T12', 'T13', 'T14', 'T17',
})

# Inert territories (registered but do not participate in mechanics)
INERT_TERRITORIES = frozenset({
    'T15',   # Askeheim — Calamity wilderness, no settlements
    'T16',   # Schoenland — foreign-exempt (awaiting ED-055 naval scope)
})


# ═══════════════════════════════════════════════════════════════════════════
# SETTLEMENT DATA MODEL
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Settlement:
    """Per-settlement state — the four canonical Church infrastructure axes
    plus identification.

    [canonical: settlement_layer_v30 §1.5 — four independent axes]
    """
    sid: str
    name: str
    territory_id: str
    settlement_type: str    # 'Seat', 'Town', 'Village', 'Fortress', 'City', 'Cathedral-City', 'Fortress-City'
    role: str               # 'province primary' or 'spoke' or special-case
    # Axis 1 — mutually exclusive
    religious_building: str = RB_NONE
    # Axes 2, 3, 4 — binary
    templar_station: bool = False
    inquisitor_base: bool = False
    church_governor: bool = False

    # [canonical: settlement_layer Axis specification + victory_v30 Mass Seizure]
    # Sum of Ob modifiers for this settlement, capped per-settlement (see cap constant).
    def per_settlement_seizure_modifier(self) -> int:
        rb = self.religious_building
        m = 0
        if rb == RB_CHAPEL:
            m += SEIZURE_OB_MODIFIER['chapel']      # [canonical: see SEIZURE_OB_MODIFIER]
        elif rb == RB_CHURCH:
            m += SEIZURE_OB_MODIFIER['church']      # [canonical: see SEIZURE_OB_MODIFIER]
        elif rb == RB_CATHEDRAL:
            m += SEIZURE_OB_MODIFIER['cathedral']   # [canonical: see SEIZURE_OB_MODIFIER]
        if self.templar_station:
            m += SEIZURE_OB_MODIFIER['templar']     # [canonical: see SEIZURE_OB_MODIFIER]
        if self.inquisitor_base:
            m += SEIZURE_OB_MODIFIER['inquisitor']  # [canonical: see SEIZURE_OB_MODIFIER]
        if self.church_governor:
            m += SEIZURE_OB_MODIFIER['governor']    # [canonical: see SEIZURE_OB_MODIFIER]
        # Cap per settlement: not more negative than the per-settlement floor constant.
        return max(m, SEIZURE_OB_PER_SETTLEMENT_CAP)

    # [canonical: victory_v30 Mass Seizure targeting — all territories with Church building (Chapel+)]
    # True if Religious Building is at least Chapel (gates Mass Seizure targeting).
    def has_any_church_building(self) -> bool:
        return self.religious_building != RB_NONE


# ═══════════════════════════════════════════════════════════════════════════
# CANONICAL SETTLEMENT REGISTRY
# ═══════════════════════════════════════════════════════════════════════════
# 37 settlements per settlement_layer_v30 §2.1 (PP-726 rebuild).
# Format: (sid, name, territory_id, type, role, starting_RB, T, I, G)
# [ASSUMPTION-2: only S-036 Himmelenger starts with Cathedral+Templar+Governor;
#  all others start with no Church infrastructure. Ratify in editorial ledger.]

_REGISTRY_RAW = [
    # ── Valorsmark duchy (Crown) ──
    ('S-001', 'Valorsplatz',         'T1',  'Seat',          'province primary', RB_NONE,      False, False, False),
    ('S-002', 'Auerheim',            'T1',  'Town',          'spoke',            RB_NONE,      False, False, False),
    ('S-003', 'Königsbrück',         'T1',  'Town',          'spoke',            RB_NONE,      False, False, False),
    ('S-004', 'Kronmark',            'T2',  'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-005', 'Saatfeld',            'T2',  'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-006', 'Goldenfurt',          'T2',  'Town',          'spoke',            RB_NONE,      False, False, False),
    ('S-007', 'Lowenskyst Fortress', 'T3',  'Fortress',      'province primary', RB_NONE,      False, False, False),
    ('S-008', 'Tiefental',           'T3',  'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-009', 'Feldmark',            'T5',  'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-010', 'Erntehof',            'T5',  'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-011', 'Spelzdorf',           'T5',  'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-012', 'Stillhelm',           'T6',  'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-013', 'Aschenbach',          'T6',  'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-014', 'Ehrenfeld',           'T14', 'Fortress-City', 'province primary', RB_NONE,      False, False, False),
    ('S-015', 'Nordhain',            'T14', 'Village',       'spoke',            RB_NONE,      False, False, False),
    # ── Hafenmark duchy (Baralta) ──
    ('S-016', 'Rendstad',            'T7',  'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-017', 'Holzbrück',           'T7',  'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-018', 'Gransol',             'T8',  'City',          'province primary', RB_NONE,      False, False, False),
    ('S-019', 'Niedersol',           'T8',  'Town',          'spoke',            RB_NONE,      False, False, False),
    ('S-020', 'Saltbrück',           'T8',  'Town',          'spoke',            RB_NONE,      False, False, False),
    ('S-021', 'Spartfell Fortress',  'T10', 'Fortress',      'province primary', RB_NONE,      False, False, False),
    ('S-022', 'Gelbgrund',           'T10', 'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-023', 'Halvarshelm Town',    'T17', 'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-024', 'Erzbach',             'T17', 'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-025', 'Schmiedhof',          'T17', 'Village',       'spoke',            RB_NONE,      False, False, False),
    # ── Varfell duchy (Vaynard) ──
    ('S-026', 'Grauwald',            'T4',  'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-027', 'Skogheim',            'T4',  'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-028', 'Halvardshelm',        'T11', 'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-029', 'Geirsvik',            'T11', 'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-030', 'Yrnastead',           'T11', 'Village',       'spoke',            RB_NONE,      False, False, False),
    ('S-031', 'Sigurdshelm',         'T12', 'Seat',          'province primary', RB_NONE,      False, False, False),
    ('S-032', 'Brynjard',            'T12', 'Town',          'spoke',            RB_NONE,      False, False, False),
    ('S-033', 'Sundfjord',           'T12', 'Town',          'spoke',            RB_NONE,      False, False, False),
    ('S-034', 'Oastad',              'T13', 'Town',          'province primary', RB_NONE,      False, False, False),
    ('S-035', 'Salgrund',            'T13', 'Village',       'spoke',            RB_NONE,      False, False, False),
    # ── Special-case territories ──
    # S-036: Church's primary anchor — Cathedral + Templar + Governor at start [ASSUMPTION-2]
    # [canonical: settlement_layer §2.1 — Himmelenger as sovereign ecclesiastical city-state]
    ('S-036', 'Himmelenger',         'T9',  'Cathedral-City', 'sovereign',       RB_CATHEDRAL, True,  False, True),
    # S-037: foreign-exempt — registered but inert per ASSUMPTION-3
    ('S-037', 'Schoenland',          'T16', 'City',          'foreign',          RB_NONE,      False, False, False),
]


def build_settlement_registry() -> dict:
    """Construct the canonical 37-settlement registry as {sid: Settlement}."""
    reg = {}
    for sid, name, tid, stype, role, rb, t, i, g in _REGISTRY_RAW:
        reg[sid] = Settlement(
            sid=sid, name=name, territory_id=tid,
            settlement_type=stype, role=role,
            religious_building=rb,
            templar_station=t, inquisitor_base=i, church_governor=g,
        )
    return reg


SETTLEMENT_REGISTRY = build_settlement_registry()

# Territory → list of S-IDs (derived once)
TERRITORY_SETTLEMENTS: dict[str, list[str]] = {}
for _sid, _s in SETTLEMENT_REGISTRY.items():
    TERRITORY_SETTLEMENTS.setdefault(_s.territory_id, []).append(_sid)
# Sort each list lexically for determinism
for _tid in TERRITORY_SETTLEMENTS:
    TERRITORY_SETTLEMENTS[_tid].sort()


# Adjacency graph (mirrors mc_v15.ADJACENCY) used for Cathedral PT bonus
# [canonical: valoria_geography_v30.yaml + mc_v15.py]
ADJACENCY = {
    'T1':  {'T2', 'T5', 'T14', 'T16'},
    'T2':  {'T1', 'T3', 'T9', 'T14'},
    'T3':  {'T2', 'T9', 'T17'},
    'T4':  {'T7', 'T12', 'T14'},
    'T5':  {'T1', 'T6', 'T14'},
    'T6':  {'T5', 'T13', 'T15'},
    'T7':  {'T4', 'T8'},
    'T8':  {'T7', 'T9', 'T10', 'T17'},
    'T9':  {'T2', 'T3', 'T8', 'T14', 'T17'},
    'T10': {'T8', 'T11'},
    'T11': {'T10', 'T12'},
    'T12': {'T4', 'T11', 'T13'},
    'T13': {'T6', 'T12', 'T15'},
    'T14': {'T1', 'T2', 'T4', 'T5', 'T9'},
    'T15': {'T6', 'T13'},
    'T17': {'T3', 'T8', 'T9'},
}


# ═══════════════════════════════════════════════════════════════════════════
# PT MAP — bidirectional canon-tier ↔ v15 float
# ═══════════════════════════════════════════════════════════════════════════
# [canonical: mc_v15.py PT_MAP — 0→1.0, 1→2.5, 2→4.0, 3→5.5, 4→6.5, 5→7.0]

PT_TIER_TO_FLOAT = {0: 1.0, 1: 2.5, 2: 4.0, 3: 5.5, 4: 6.5, 5: 7.0}  # [canonical: mc_v15.py PT_MAP]
PT_FLOAT_TO_TIER_THRESHOLDS = [
    # [canonical: derived from mc_v15.py PT_MAP — boundary midpoints between adjacent tiers]
    # (upper_bound_inclusive, tier_returned)
    (1.75, 0),    # [canonical: midpoint of PT_MAP[0]=1.0 and PT_MAP[1]=2.5]
    (3.25, 1),    # [canonical: midpoint of PT_MAP[1]=2.5 and PT_MAP[2]=4.0]
    (4.75, 2),    # [canonical: midpoint of PT_MAP[2]=4.0 and PT_MAP[3]=5.5]
    (6.0,  3),    # [canonical: midpoint of PT_MAP[3]=5.5 and PT_MAP[4]=6.5]
    (6.75, 4),    # [canonical: midpoint of PT_MAP[4]=6.5 and PT_MAP[5]=7.0]
    # else → tier 5
]

# [canonical: mc_v15.py PT_MAP inverse — float to canon tier]
# Map v15's float PT space back to canon tier integers.
def pt_float_to_tier(pt_float: float) -> int:
    for bound, tier in PT_FLOAT_TO_TIER_THRESHOLDS:
        if pt_float < bound:
            return tier
    return 5  # [canonical: PT_MAP[5]=7.0 is the upper tier]


# ═══════════════════════════════════════════════════════════════════════════
# ACCESSORS
# ═══════════════════════════════════════════════════════════════════════════

def territory_settlements(tid: str, registry: dict = None) -> list:
    """Return list[Settlement] for the given territory T#."""
    reg = registry if registry is not None else SETTLEMENT_REGISTRY
    return [reg[sid] for sid in TERRITORY_SETTLEMENTS.get(tid, [])]


def is_playable(tid: str) -> bool:
    """True iff this T# participates in CI/PT/Seizure mechanics."""
    return tid in PLAYABLE_TERRITORIES


# ═══════════════════════════════════════════════════════════════════════════
# MECHANICAL PRIMITIVES — Seizure
# ═══════════════════════════════════════════════════════════════════════════

def territory_seizure_modifier(tid: str, registry: dict = None) -> int:
    # [canonical: settlement_layer Axis specification + victory_v30 Mass Seizure]
    # Sum of per-settlement Seizure Ob modifiers across the territory.
    # Each settlement's modifier is independently capped per-settlement.
    # The territory total is the unbounded sum (no canonical territory-level cap).
    return sum(s.per_settlement_seizure_modifier()
               for s in territory_settlements(tid, registry))


def seizure_ob(tid: str, pt_canon_tier: int, world_ci: float = 0.0,
               registry: dict = None) -> int:
    # [canonical: victory_v30 — Church Seizure Ob = 10 − PT − infrastructure modifiers, floor 1]
    # [canonical: ci_political_v30 Ascendant milestone — Seizure Ob reduced by 1 globally]
    # Mass Seizure Ob against a single territory.
    base = 10 - pt_canon_tier                                                # [canonical: see SEIZURE_OB base formula above]
    infra = territory_seizure_modifier(tid, registry)  # negative or zero
    ascendant_modifier = -1 if world_ci >= CI_MILESTONE_ASCENDANT else 0     # [canonical: ci_political_v30 Ascendant milestone]
    raw = base + infra + ascendant_modifier
    return max(SEIZURE_OB_FLOOR, raw)


def seizure_pool(church_influence: float, world_ci: float) -> float:
    # [canonical: victory_v30 — Church Seizure Pool = Influence + floor(CI / divisor)]
    # Mass Seizure attacker pool.
    return church_influence + math.floor(world_ci / MASS_SEIZURE_POOL_DIVISOR)


def mass_seizure_declaration_probability(world_ci: float) -> float:
    # [canonical: victory_v30 — P(declare) = ((CI − threshold) / range) ^ exponent, clamped to unit interval]
    # Returns the per-season probability the Church declares Mass Seizure.
    if world_ci < CI_MASS_SEIZURE_AVAILABLE:
        return 0.0
    normalised = (world_ci - CI_MASS_SEIZURE_AVAILABLE) / MASS_SEIZURE_DECLARE_RANGE
    p = normalised ** MASS_SEIZURE_DECLARE_EXPONENT
    return max(0.0, min(1.0, p))


# ═══════════════════════════════════════════════════════════════════════════
# MECHANICAL PRIMITIVES — PT generation (Religious Buildings)
# ═══════════════════════════════════════════════════════════════════════════

def pt_yield_per_territory(registry: dict = None) -> dict:
    """Returns {tid: float} of in-territory PT yield from Religious Buildings.

    Sums Chapel/Church/Cathedral PT yield across all settlements in each
    territory. Does NOT include Cathedral adjacency bonus (see
    pt_yield_adjacency).

    [canonical: settlement_layer_v30 §1.5 Axis 1]
    """
    reg = registry if registry is not None else SETTLEMENT_REGISTRY
    yields = {tid: 0.0 for tid in PLAYABLE_TERRITORIES | INERT_TERRITORIES}
    for s in reg.values():
        yields[s.territory_id] = yields.get(s.territory_id, 0.0) + PT_YIELD_PER_RB[s.religious_building]
    return yields


def pt_yield_adjacency(registry: dict = None) -> dict:
    # [canonical: settlement_layer Axis One — Cathedral yields PT to adjacent territories]
    # [ASSUMPTION_FOUR: stacks per Cathedral, direct-adjacent only via ADJACENCY, no cap, no decay]
    # Returns {tid: float} of PT bonus received from adjacent Cathedrals.
    reg = registry if registry is not None else SETTLEMENT_REGISTRY
    bonus = {tid: 0.0 for tid in PLAYABLE_TERRITORIES | INERT_TERRITORIES}
    for s in reg.values():
        if s.religious_building != RB_CATHEDRAL:
            continue
        for adj in ADJACENCY.get(s.territory_id, set()):
            bonus[adj] = bonus.get(adj, 0.0) + PT_CATHEDRAL_ADJACENCY_BONUS
    return bonus


def pt_yield_total(registry: dict = None) -> dict:
    """Returns {tid: float} of combined PT yield = in-territory + adjacency."""
    interior = pt_yield_per_territory(registry)
    adjacency = pt_yield_adjacency(registry)
    return {tid: interior.get(tid, 0.0) + adjacency.get(tid, 0.0)
            for tid in set(interior) | set(adjacency)}


# ═══════════════════════════════════════════════════════════════════════════
# MECHANICAL PRIMITIVES — CI generation (Templar Stations, Piety Yield)
# ═══════════════════════════════════════════════════════════════════════════

def ci_from_templars(registry: dict = None, playable_only: bool = True) -> float:
    """+1 CI/season per territory containing ≥1 Templar Station.

    [canonical: settlement_layer_v30 §1.5 Axis 2 — '+1 CI/season in territory']
    Per territory (not per settlement) — multiple Templar Stations in one
    territory still yield +1.
    """
    reg = registry if registry is not None else SETTLEMENT_REGISTRY
    territories_with_templar = set()
    for s in reg.values():
        if playable_only and s.territory_id not in PLAYABLE_TERRITORIES:
            continue
        if s.templar_station:
            territories_with_templar.add(s.territory_id)
    return float(len(territories_with_templar))


def piety_yield_sw_weighted(prominent_territories, pt_floats: dict) -> float:
    """SW-weighted Piety Yield = Σ(PT_tier × SW/5) per prominent territory.

    Replaces mc_v15's tier-binary piety_yield. Per ci_political §1 use case 1.

    Arguments:
      prominent_territories: iterable of T#s where Church is Prominent
        (Church-controlled OR Church Mandate > controlling faction Mandate).
        Caller is responsible for the Prominence check.
      pt_floats: {tid: float} — current PT float values from world.territories.

    [canonical: ci_political_v30 §1 — SW use case 1 — 'CI from Piety Yield
     = Σ(PT tier × SW factor)', SW factor = SW/5]
    """
    total = 0.0
    for tid in prominent_territories:
        if tid not in PLAYABLE_TERRITORIES:
            continue
        sw = SPIRITUAL_WEIGHT.get(tid, 0)
        pt_float = pt_floats.get(tid, 0.0)
        pt_tier = pt_float_to_tier(pt_float)
        total += pt_tier * (sw / 5.0)
    return total


# ═══════════════════════════════════════════════════════════════════════════
# MECHANICAL PRIMITIVES — Other axis effects
# ═══════════════════════════════════════════════════════════════════════════

def rm_ob_modifier_from_inquisitors(tid: str, registry: dict = None) -> int:
    """Inquisitor Base: RM governance-building actions +1 Ob per Inquisitor
    Base territory.

    Returns +1 if territory contains ≥1 Inquisitor Base, else 0.

    [canonical: settlement_layer_v30 §1.5 Axis 3]
    """
    for s in territory_settlements(tid, registry):
        if s.inquisitor_base:
            return 1
    return 0


def parish_order_yields(registry: dict = None) -> dict:
    # [canonical: settlement_layer Parish Social Services section]
    # Returns {sid: {order_per_season, order_install_bonus, order_decay_modifier}}.
    # Aggregator module will apply these to settlement Order tracking.
    reg = registry if registry is not None else SETTLEMENT_REGISTRY
    out = {}
    for sid, s in reg.items():
        out[sid] = dict(PARISH_ORDER_RULES[s.religious_building])
    return out


def pastoral_assumption_eligible(sid: str, governor_present: bool,
                                  registry: dict = None) -> bool:
    # [canonical: settlement_layer Pastoral Assumption section]
    # Pastoral Assumption: install a Church Governor at low Ob when
    #   (a) settlement has no governor (governor_present is False), AND
    #   (b) settlement has at least Chapel (Religious Building is not None).
    # Restriction: does not change Provincial Authority. This module only exposes
    # the eligibility check; the action-expansion module wires the Domain Action.
    reg = registry if registry is not None else SETTLEMENT_REGISTRY
    if sid not in reg:
        return False
    s = reg[sid]
    if governor_present:
        return False
    return s.has_any_church_building()


# ═══════════════════════════════════════════════════════════════════════════
# MILESTONE HOOKS — Ascendant and Unification
# ═══════════════════════════════════════════════════════════════════════════

def ci_ascendant_pt_drift(pt_floats: dict, warden_cooperation: int = 0) -> dict:
    # [canonical: ci_political_v30 Ascendant milestone + victory_v30 Mass Seizure section]
    # [ASSUMPTION_FIVE: drift is +1 in canon-tier units, snap to next tier boundary]
    # [ASSUMPTION_SIX: warden_cooperation defaults to 0 until aggregator module wires Warden state]
    # Apply Ascendant-milestone PT drift toward piety pole at Year-End.
    # Capped at the highest canon tier (mapped to PT_MAP top). Suppressed when
    # Warden Cooperation is at or above its canonical suppression threshold.
    # Returns {tid: new_pt_float}. Caller applies to world.territories.
    if warden_cooperation >= 2:  # [canonical: ci_political_v30 — suppression threshold of 2]
        return dict(pt_floats)  # no-op
    new = {}
    for tid in PLAYABLE_TERRITORIES:
        if tid not in pt_floats:
            new[tid] = pt_floats.get(tid, 0.0)
            continue
        current_float = pt_floats[tid]
        current_tier = pt_float_to_tier(current_float)
        new_tier = min(5, current_tier + 1)                              # [canonical: mc_v15.py PT_MAP top tier = 5]
        new[tid] = PT_TIER_TO_FLOAT[new_tier]
    # preserve inert/non-playable values untouched
    for tid, v in pt_floats.items():
        if tid not in new:
            new[tid] = v
    return new


def ci_unification_active(world_ci: float, theocracy_seasons: int,
                          church_controlled_count: int) -> dict:
    """CI=100 Theocracy Unification Attempt — returns active state dict.

    [canonical: ci_political_v30 §2.2 + victory_v30 §3.2 §CI=100]

    Returns:
      {
        'active': bool — Unification phase currently engaged,
        'free_secular_motion': bool — each secular faction has free Parliamentary motion,
        'victory_pending': bool — Church holds ≥10 territories,
        'victory_achieved': bool — pending for ≥2 consecutive Year-Ends,
      }

    Caller (M2 or M7) tracks `theocracy_seasons` (consecutive Year-Ends Church
    has held ≥10 territories while Unification active) and supplies the count.
    """
    active = world_ci >= CI_MILESTONE_UNIFICATION
    victory_pending = active and church_controlled_count >= 10
    victory_achieved = victory_pending and theocracy_seasons >= 2
    return {
        'active': active,
        'free_secular_motion': active,
        'victory_pending': victory_pending,
        'victory_achieved': victory_achieved,
    }


# ═══════════════════════════════════════════════════════════════════════════
# SELF-CHECK (loaded at import time as a sanity guard)
# ═══════════════════════════════════════════════════════════════════════════

def _validate_registry():
    # [canonical: settlement_layer Settlement Registry — total march-target count]
    # Cheap structural validation — fails import if registry is malformed.
    # [canonical: settlement_layer Settlement Registry — 37 march-target settlements]
    assert len(SETTLEMENT_REGISTRY) == 37, \
        f"Settlement registry must have the canonical entry count; has {len(SETTLEMENT_REGISTRY)}"
    assert sum(SPIRITUAL_WEIGHT.values()) == SW_TOTAL_CANONICAL, \
        f"SPIRITUAL_WEIGHT sum must be {SW_TOTAL_CANONICAL}; got {sum(SPIRITUAL_WEIGHT.values())}"
    # Every settlement's territory must be in our T-set
    valid_tids = PLAYABLE_TERRITORIES | INERT_TERRITORIES
    for sid, s in SETTLEMENT_REGISTRY.items():
        assert s.territory_id in valid_tids, \
            f"{sid} has unknown territory {s.territory_id}"
    # Religious Building enum check
    for sid, s in SETTLEMENT_REGISTRY.items():
        assert s.religious_building in RELIGIOUS_BUILDINGS, \
            f"{sid} has invalid religious_building '{s.religious_building}'"


_validate_registry()
