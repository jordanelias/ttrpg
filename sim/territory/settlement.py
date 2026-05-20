"""
sim/territory/settlement.py — Settlement-level state — Order, Prosperity, Population

Canon source: designs/territory/settlement_layer_v30.md §1.2-1.3

Implements §1.3 derived values + province-aggregation formula. Settlement
registry does not yet exist in game_state.World (territories carry the
prosperity/accord fields directly); this module derives settlement-shape
output from Territory state until a settlement registry lands. The
SettlementState shape is canonical and matches §1.3; consumers can begin
calling against this surface.

[ASSUMPTION: 1:1 territory->settlement mapping for Tier 0 — basis: game_state
 schema has no Settlement model; building one requires changing world
 creation + persistence + all faction_action callers; out of scope for stub
 infill. When a settlement registry is added, this module's body changes;
 the entry-point signature stays.]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - compute_settlement_state(settlement_id: str, world: GameState) -> SettlementState
  - aggregate_to_province(province_id: str, world: GameState) -> ProvinceState
"""
from __future__ import annotations

from dataclasses import dataclass
import math


# Section 1.3 derived-value multipliers (settlement stat -> videogame derived value)
# [canonical: designs/territory/settlement_layer_v30.md §1.3 Settlement Stats table]
PROSPERITY_TO_LOCAL_ECONOMY = 50   # Prosperity x 50 = Gold contribution
DEFENSE_BASE_TO_GARRISON = 20      # Defense x 20 + Fort x 30 = Garrison Strength
FORT_LEVEL_TO_GARRISON = 30        # Per-fort-level contribution to Garrison Strength
ORDER_TO_PUBLIC_ORDER = 20         # Order x 20 = Public Order meter

# Stat scale bounds per §1.3 ("0-5 scale")
SETTLEMENT_STAT_MIN = 0
SETTLEMENT_STAT_MAX = 5


@dataclass
class SettlementState:
    """Derived-value view of a settlement per §1.3.

    Fields mirror the §1.3 derived-values table. settlement_id is the
    identity key (currently 1:1 with territory tid; will become a sub-tid
    when settlement registry lands).
    """
    settlement_id: str
    settlement_type: str       # §1.2 type — "Seat" / "City" / "Town" / etc.
    owner: str | None          # Province-controlling faction (§1.2 Natural Manager)
    prosperity: int            # §1.3 stat 0-5
    defense: int               # §1.3 stat 0-5
    order: int                 # §1.3 stat 0-5
    fort_level: int            # Fort scaling input
    local_economy: int         # §1.3 derived: prosperity x 50
    garrison_strength: int     # §1.3 derived: defense x 20 + fort_level x 30
    public_order: int          # §1.3 derived: order x 20


@dataclass
class ProvinceState:
    """Aggregated province-level state per §1.3 'Province Accord derivation'.

    Province Accord is the floor of average settlement Order. Effective
    Prosperity is the sum of settlement Prosperity values.
    """
    province_id: str
    accord: int                # §1.3 floor(avg(settlement.order))
    effective_prosperity: int  # §1.3 sum of settlement Prosperity
    settlement_count: int
    member_settlements: list[str]


def compute_settlement_state(settlement_id: str, world) -> SettlementState:
    """Derive §1.3 settlement-state view for one settlement.

    Currently maps 1:1 from Territory; see module docstring ASSUMPTION.
    Order is derived from Territory.accord (continuous 0.5-7.0) as the
    canon §1.3 mapping requires an integer 0-5 stat; we map by linear
    clamp + floor. Defense is derived from fort_level + garrison
    presence per §1.2 Fortress / §1.3 Defense.
    """
    # [canonical: §1.3 — accord is the floor-aggregate of settlement Order;
    #  inverse mapping for derivation: settlement Order = Territory Accord
    #  clamped/floored into the 0-5 stat scale]
    if settlement_id not in world.territories:
        raise KeyError(f"settlement_id not found in world.territories: {settlement_id}")
    t = world.territories[settlement_id]

    # Order derivation: accord is 0.5-7.0 (granular); §1.3 Order is 0-5 int
    order_int = max(SETTLEMENT_STAT_MIN, min(SETTLEMENT_STAT_MAX, math.floor(t.accord)))

    # Defense derivation: fort_level (0+) + +1 for garrison presence, clamped
    defense_int = max(SETTLEMENT_STAT_MIN,
                      min(SETTLEMENT_STAT_MAX, t.fort_level + (1 if t.garrison else 0)))

    # Prosperity: Territory.prosperity is already 0-5 int per game_state schema
    prosperity_int = max(SETTLEMENT_STAT_MIN, min(SETTLEMENT_STAT_MAX, t.prosperity))

    # Settlement type derivation: minimum-viable from fort_level + templar marker
    # [canonical: §1.2 — Fortress = military installation; Cathedral = Church institution]
    # Until settlement registry lands, infer type from territory metadata.
    if t.templar:
        s_type = "Cathedral"
    elif t.fort_level >= 2:
        s_type = "Fortress"
    elif t.prosperity >= 2:
        s_type = "Seat"
    else:
        s_type = "Town"

    # Derived values per §1.3
    local_economy = prosperity_int * PROSPERITY_TO_LOCAL_ECONOMY
    garrison_strength = defense_int * DEFENSE_BASE_TO_GARRISON + t.fort_level * FORT_LEVEL_TO_GARRISON
    public_order = order_int * ORDER_TO_PUBLIC_ORDER

    return SettlementState(
        settlement_id=settlement_id,
        settlement_type=s_type,
        owner=t.owner,
        prosperity=prosperity_int,
        defense=defense_int,
        order=order_int,
        fort_level=t.fort_level,
        local_economy=local_economy,
        garrison_strength=garrison_strength,
        public_order=public_order,
    )


def aggregate_to_province(province_id: str, world) -> ProvinceState:
    """Aggregate child settlements into province-level state per §1.3.

    Currently a single-settlement aggregation (settlement_id == province_id ==
    territory tid) until settlement registry lands. Formula preserved per
    canon so consumers see the right shape:
      - accord = floor(avg(settlement.order))
      - effective_prosperity = sum(settlement.prosperity)
    """
    # [canonical: §1.3 — "Province Accord = floor of the average Order across
    #  all settlements in the province" + "Each point of settlement Prosperity
    #  adds to the province's Prosperity pool"]
    if province_id not in world.territories:
        raise KeyError(f"province_id not found in world.territories: {province_id}")

    # Until registry: one settlement per province (the territory itself)
    member_settlements = [province_id]
    states = [compute_settlement_state(sid, world) for sid in member_settlements]

    orders = [s.order for s in states]
    avg_order = sum(orders) / len(orders) if orders else 0
    accord_int = math.floor(avg_order)

    effective_prosperity = sum(s.prosperity for s in states)

    return ProvinceState(
        province_id=province_id,
        accord=accord_int,
        effective_prosperity=effective_prosperity,
        settlement_count=len(member_settlements),
        member_settlements=member_settlements,
    )
