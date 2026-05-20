"""
sim/territory/infrastructure.py — Church infrastructure — Religious Buildings, Templar Stations, Inquisitor Bases, Church Governors

Canon source: designs/territory/settlement_layer_v30.md §1.5-§1.7

Implements the §1.5 four-independent-axis model:
  Axis 1 (Religious Building, mutually exclusive): None / Chapel / Church / Cathedral
  Axis 2 (Templar Station, binary): adds +1 CI/season, interrupt capability
  Axis 3 (Inquisitor Base, binary): surveillance zone, +1 Ob to RM
  Axis 4 (Church Governor, binary): de facto Church territory

Plus §1.6 Parish Social Services (Order/Stability bonuses) + §1.7
Pastoral Assumption (vacuum-fill installation).

[ASSUMPTION: infrastructure stored per-territory on world rather than
 per-settlement — basis: World has territories but no settlement registry.
 §1.5 specifies "per settlement"; the 1-to-1 territory:settlement mapping
 from settlement.py applies here too. When settlement registry lands,
 the registry shifts but the entry-point signatures stay.]

Dependencies:
  - sim/autoload/game_state
  - sim/territory/settlement

Entry points:
  - build_infrastructure(territory_id, infra_type, world) -> BuildResult
  - count_infrastructure(territory_id, infra_type, world) -> int
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# §1.5 Axis 1 — Religious Building types (mutually exclusive)
# [canonical: settlement_layer_v30 §1.5 Axis 1]
BUILDING_NONE = "None"
BUILDING_CHAPEL = "Chapel"
BUILDING_CHURCH = "Church"
BUILDING_CATHEDRAL = "Cathedral"
RELIGIOUS_BUILDINGS = {BUILDING_NONE, BUILDING_CHAPEL, BUILDING_CHURCH, BUILDING_CATHEDRAL}

# §1.5 Axis 1 PT generation per season
# [canonical: §1.5 Axis 1 — "Chapel (+0.5 PT/season) / Church (+1 PT/season) /
#  Cathedral (+2 PT/season, +0.5 PT to adjacent territories)"]
PT_GAIN_CHAPEL = 0.5
PT_GAIN_CHURCH = 1.0
PT_GAIN_CATHEDRAL = 2.0
PT_GAIN_CATHEDRAL_ADJACENT = 0.5

# §1.5 Axis 2 Templar Station CI per season
# [canonical: §1.5 Axis 2 — "+1 CI/season in territory"]
CI_GAIN_TEMPLAR = 1

# §1.5 Seizure Ob Modifiers (stacking, per settlement; cap -4)
# [canonical: §1.5 Seizure Ob Modifiers]
SEIZURE_OB_BY_BUILDING = {
    BUILDING_NONE: 0,
    BUILDING_CHAPEL: 0,         # "Chapel −0"
    BUILDING_CHURCH: -1,        # "Church −1"
    BUILDING_CATHEDRAL: -2,     # "Cathedral −2"
}
SEIZURE_OB_TEMPLAR = -1         # "Templar −1"
SEIZURE_OB_INQUISITOR = -1      # "Inquisitor −1"
SEIZURE_OB_CHURCH_GOVERNOR = -2 # "Church Governor −2"
SEIZURE_OB_CAP = -4             # "Cap: −4 per settlement"

# §1.6 Parish Social Services Order bonuses
# [canonical: §1.6 table — Chapel +0.5 Order/season; Church +1 at installation;
#  Cathedral +1 at installation + Order decay -1]
ORDER_GAIN_CHAPEL_PER_SEASON = 0.5
ORDER_GAIN_CHURCH_INSTALL = 1
ORDER_GAIN_CATHEDRAL_INSTALL = 1
ORDER_DECAY_CATHEDRAL_BONUS = -1  # Order is more stable


@dataclass
class InfrastructureState:
    """Per-territory Church infrastructure state per §1.5 four-axis model."""
    territory_id: str
    religious_building: str = BUILDING_NONE      # Axis 1
    templar_station: bool = False                 # Axis 2
    inquisitor_base: bool = False                 # Axis 3
    church_governor: bool = False                 # Axis 4

    def to_dict(self) -> dict:
        return {'territory_id': self.territory_id,
                'religious_building': self.religious_building,
                'templar_station': self.templar_station,
                'inquisitor_base': self.inquisitor_base,
                'church_governor': self.church_governor}

    @classmethod
    def from_dict(cls, d: dict) -> "InfrastructureState":
        return cls(territory_id=d['territory_id'],
                   religious_building=d.get('religious_building', BUILDING_NONE),
                   templar_station=d.get('templar_station', False),
                   inquisitor_base=d.get('inquisitor_base', False),
                   church_governor=d.get('church_governor', False))


@dataclass
class BuildResult:
    success: bool
    territory_id: str
    infra_type: str
    reason: str


# Module-level fallback registry — keyed by territory_id
# Migrates to World.territory_infrastructure when added (future schema migration)
_infra_state: dict[str, InfrastructureState] = {}


def _infra_store(world):
    """Return the infrastructure store: world.territory_infrastructure
    if world supplied, else module-level fallback."""
    if world is not None and hasattr(world, 'territory_infrastructure'):
        return world.territory_infrastructure
    return _infra_state


def _get_or_create(territory_id: str, world=None) -> InfrastructureState:
    """Initialise per-territory infrastructure state with the canonical
    starting value (None/False/False/False)."""
    store = _infra_store(world)
    if territory_id not in store:
        # Honor existing templar flag from game_state.Territory for backward compat
        templar_seed = False
        if world is not None and territory_id in getattr(world, 'territories', {}):
            templar_seed = getattr(world.territories[territory_id], 'templar', False)
        store[territory_id] = InfrastructureState(
            territory_id=territory_id,
            templar_station=templar_seed,
        )
    return store[territory_id]


def build_infrastructure(territory_id: str, infra_type: str, world=None) -> BuildResult:
    """Construct a §1.5 infrastructure axis at a territory.

    infra_type valid values:
      'Chapel' / 'Church' / 'Cathedral'  -> Axis 1 (mutually exclusive replace)
      'Templar Station'                    -> Axis 2 (binary set True)
      'Inquisitor Base'                    -> Axis 3 (binary set True)
      'Church Governor'                    -> Axis 4 (binary set True)

    Axis 1 mutually-exclusive: setting a different religious building replaces
    the prior one (canonical "one per settlement").
    """
    if territory_id not in getattr(world, 'territories', {}):
        return BuildResult(success=False, territory_id=territory_id,
                           infra_type=infra_type,
                           reason=f"territory_id '{territory_id}' not in world.territories")

    state = _get_or_create(territory_id, world)

    if infra_type in (BUILDING_CHAPEL, BUILDING_CHURCH, BUILDING_CATHEDRAL):
        # Axis 1 mutually exclusive
        state.religious_building = infra_type
        return BuildResult(success=True, territory_id=territory_id,
                           infra_type=infra_type,
                           reason=f"Axis 1 set to {infra_type}")

    if infra_type == 'Templar Station':
        state.templar_station = True
        return BuildResult(success=True, territory_id=territory_id,
                           infra_type=infra_type, reason="Axis 2 set True")

    if infra_type == 'Inquisitor Base':
        state.inquisitor_base = True
        return BuildResult(success=True, territory_id=territory_id,
                           infra_type=infra_type, reason="Axis 3 set True")

    if infra_type == 'Church Governor':
        state.church_governor = True
        return BuildResult(success=True, territory_id=territory_id,
                           infra_type=infra_type, reason="Axis 4 set True")

    return BuildResult(success=False, territory_id=territory_id,
                       infra_type=infra_type,
                       reason=f"unknown infra_type '{infra_type}'")


def count_infrastructure(territory_id: str, infra_type: Optional[str], world=None) -> int:
    """Count infrastructure at a territory.

    infra_type=None: returns count of all axes present (0-4).
    infra_type='Religious Building': 1 if any of Chapel/Church/Cathedral, else 0.
    infra_type='Chapel'/'Church'/'Cathedral': 1 if exactly that, else 0.
    infra_type='Templar Station'/'Inquisitor Base'/'Church Governor': 1 if set, else 0.
    """
    if territory_id not in _infra_store(world):
        # Not yet initialised — read from Territory.templar for seed
        if world is not None and territory_id in getattr(world, 'territories', {}):
            templar = getattr(world.territories[territory_id], 'templar', False)
            if infra_type is None:
                return 1 if templar else 0
            if infra_type == 'Templar Station':
                return 1 if templar else 0
            return 0
        return 0

    state = _infra_store(world)[territory_id]

    if infra_type is None:
        count = 0
        if state.religious_building != BUILDING_NONE:
            count += 1
        if state.templar_station:
            count += 1
        if state.inquisitor_base:
            count += 1
        if state.church_governor:
            count += 1
        return count

    if infra_type == 'Religious Building':
        return 1 if state.religious_building != BUILDING_NONE else 0

    if infra_type in (BUILDING_CHAPEL, BUILDING_CHURCH, BUILDING_CATHEDRAL):
        return 1 if state.religious_building == infra_type else 0

    if infra_type == 'Templar Station':
        return 1 if state.templar_station else 0

    if infra_type == 'Inquisitor Base':
        return 1 if state.inquisitor_base else 0

    if infra_type == 'Church Governor':
        return 1 if state.church_governor else 0

    return 0


def seizure_ob_modifier(territory_id: str, world=None) -> int:
    """Per §1.5 Seizure Ob Modifiers — stacking, capped at -4.

    Returns the Ob modifier (negative = easier to seize) for a territory's
    Church infrastructure stack.
    """
    if territory_id not in _infra_store(world):
        return 0

    state = _infra_store(world)[territory_id]
    mod = SEIZURE_OB_BY_BUILDING.get(state.religious_building, 0)
    if state.templar_station:
        mod += SEIZURE_OB_TEMPLAR
    if state.inquisitor_base:
        mod += SEIZURE_OB_INQUISITOR
    if state.church_governor:
        mod += SEIZURE_OB_CHURCH_GOVERNOR
    # Cap per §1.5: -4 floor
    return max(SEIZURE_OB_CAP, mod)


def reset_infrastructure(world=None):
    """Test helper."""
    _infra_store(world).clear()
