"""
sim/territory/registry.py — Settlement registry (closes audit gap G1)

Canon source: designs/territory/goldenfurt_slice/sim_build_spec.md §1;
              designs/territory/settlement_layer_v30.md §1.1-1.3, §2.1

The Settlement is the base civic/political unit (settlement_layer §1.1; the
siege-target). Before this module, sim/territory/settlement.py mapped 1:1
territory->settlement because game_state.World had no Settlement registry
(audit 2026-06-22 gap G1). This adds a registry so a province can hold its
canonical 1-3 settlements and the §1.3 floor-average province aggregation can
finally fire over real members instead of a synthetic single one.

Follows the established sim store-router idiom (cf. infrastructure.py
_infra_store / temperaments.py _drift_store): world.settlements if a World is
supplied, else a module-level fallback for legacy callers + tests.

Entry points:
  - Settlement(...)                              # the dataclass (fields per sim_build_spec §1)
  - register_settlement(s, world=None) / get_settlement(sid, world=None)
  - province_members(province_id, world=None)
  - province_accord(province_id, world=None)     # §1.3 floor(mean order)
  - province_effective_prosperity(province_id, world=None)
  - succeed_governor(sid, new_governor, world=None, season=0)  # durable ledger survives
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from sim.territory.ledger import (
    LedgerTag, ledger_add, ledger_get, ledger_has, ledger_sweep,
)

# §1.2 legal settlement types (+ Village, per the PP-726 §2.1 registry; see audit H3)
LEGAL_TYPES = {
    "Seat", "City", "Town", "Fortress", "Port", "Cathedral", "Mine", "Outpost",
    "Village", "Fortress-City", "Cathedral-City",
}

STAT_MIN, STAT_MAX = 0, 5      # §1.3 settlement stats
L_PS_MIN, L_PS_MAX = 0, 7      # §1.8 Legitimacy / Popular Support


@dataclass
class Settlement:
    sid: str
    name: str
    stype: str
    province_id: str
    owner_faction: str | None = None
    governor_id: str | None = None
    # §1.3 stats (0-5)
    prosperity: int = 0
    defense: int = 0
    order: int = 0
    fort_level: int = 0
    garrison: bool = False
    # §1.8 per-settlement political acceptance (0-7)
    legitimacy: int = 0
    popular_support: int = 0
    # §1.4 / governance economy
    facility_tier: int = 0
    suspicion: int = 0
    pressure: float = 4.0
    # deck/dossier-referenced state (verify sim-F1/F2/F3/F5/F9)
    active_directive: str | None = None
    religious_building: str = "None"   # None|Chapel|Church|Cathedral
    church_attention: int = 0
    governor_emergence: int = 0
    # presences + relational + memory
    subnational: dict = field(default_factory=dict)   # foothold -> level
    npc_ids: list = field(default_factory=list)
    ledger: list = field(default_factory=list)        # list[LedgerTag]
    open_needs: list = field(default_factory=list)    # [(card_id, pressure_if_ignored)]
    deck_state: dict = field(default_factory=dict)

    @property
    def ap(self) -> int:
        """Administration Points/season = 2 + FacilityTier, +1 at a Seat/Cathedral
        (governance_play_redesign §1.1)."""
        bonus = 1 if self.stype in ("Seat", "Cathedral", "Cathedral-City") else 0
        return 2 + self.facility_tier + bonus

    # ── Ledger convenience (delegates to ledger.py) ──
    def add_tag(self, kind: str, key: str, value: float = 1.0,
                created_season: int = 0, ttl: int | None = None) -> None:
        ledger_add(self.ledger, LedgerTag(kind, key, value, created_season, ttl))

    def has_tag(self, kind: str, key: str | None = None) -> bool:
        return ledger_has(self.ledger, kind, key)

    def tags(self, kind: str) -> list:
        return ledger_get(self.ledger, kind)


# ── store router (cf. infrastructure._infra_store) ──
_settlement_store: dict = {}


def settlement_store(world=None) -> dict:
    if world is not None and hasattr(world, "settlements"):
        return world.settlements
    return _settlement_store


def register_settlement(s: Settlement, world=None) -> Settlement:
    settlement_store(world)[s.sid] = s
    return s


def get_settlement(sid: str, world=None):
    return settlement_store(world).get(sid)


def province_members(province_id: str, world=None) -> list:
    return [s for s in settlement_store(world).values() if s.province_id == province_id]


def province_accord(province_id: str, world=None) -> int:
    """§1.3: province Accord = floor(mean settlement Order) over real members.
    With the registry this finally aggregates >1 settlement (was synthetic-1)."""
    members = province_members(province_id, world)
    if not members:
        return 0
    return math.floor(sum(m.order for m in members) / len(members))


def province_effective_prosperity(province_id: str, world=None) -> int:
    """§1.3: each point of settlement Prosperity adds to the province pool."""
    return sum(m.prosperity for m in province_members(province_id, world))


def succeed_governor(sid: str, new_governor: str | None, world=None, season: int = 0):
    """Replace the governor; durable Ledger (ttl=None) and settlement stats
    survive — the player->world persistence guarantee (sim_build_spec §2).
    Transient tags (ttl set) are swept on the season boundary."""
    s = get_settlement(sid, world)
    if s is None:
        raise KeyError(f"settlement not in registry: {sid}")
    s.governor_id = new_governor
    ledger_sweep(s.ledger, season)
    return s


def reset_registry(world=None):
    """Test helper."""
    settlement_store(world).clear()
