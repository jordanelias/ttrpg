"""
sim/provincial/treaty.py — Crown Treaties + Treaty Expiration (90-95%/arc lapse per v12c)

Canon source: designs/provincial/treaty_expiration_v30.md (CANONICAL, Pass 2h
2026-05-17); designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md §4.5 + §4.7

IMPLEMENTATION STATUS (2026-05-26 review):
  - process_treaty_expirations: implemented against treaty_expiration_v30 §1
    (Treaty Expiration at arc boundary, TREATY_LAPSE_RATE).
  - propose_treaty: still raises. Canon for the *proposal* protocol is the
    Senator Outward re-binding action (treaty_expiration_v30 §2), which lives
    in crown_initiative, not here. propose_treaty is retained as a direct
    insertion entry point for non-Senator-Outward paths; until a non-Crown
    treaty-formation path is canonized it raises. register_treaty is the
    supported scaffolding insertion.

Treaty storage: World.treaties (game_state L164) is the canonical store and
exists with serialize/deserialize support. The module-level _treaty_registry
is a fallback only for world=None callers (legacy tests).

Dependencies:
  - sim/autoload/dice_engine
  - sim/autoload/season_manager

Entry points:
  - propose_treaty(parties: list, terms: dict, world: GameState) -> TreatyResult
    [raises — no canonized non-Senator-Outward formation path yet]
  - process_treaty_expirations(world: GameState) -> list[ExpirationResult]
  - register_treaty(...) — scaffolding insertion (supported)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# §4.5 Treaty Expiration parameters
# [canonical: faction_balance_convergence_v12c §4.5 — "At each arc boundary,
#  each Crown Treaty has TREATY_LAPSE_RATE chance of lapsing."]
TREATY_LAPSE_RATE_DEFAULT = 0.90  # balanced value per §5.1 (table 0.90-0.95 range)

# §4.7 Treaty Consent Rate
# [canonical: §4.7 + §5.1 balanced config CONSENT_RATE = 0.28]
TREATY_CONSENT_RATE_DEFAULT = 0.28


# Module-level treaty registry — fallback when world is None
# Post-2026-05-19 schema migration: when world is supplied, treaties live
# on world.treaties.
_treaty_registry: dict[tuple, "TreatyRecord"] = {}


def _treaty_store(world):
    if world is not None and hasattr(world, 'treaties'):
        return world.treaties
    return _treaty_registry


@dataclass
class TreatyRecord:
    parties: tuple
    terms: dict
    bound_arc: int
    bound_season: int
    active: bool = True

    def to_dict(self) -> dict:
        return {'parties': list(self.parties),
                'terms': dict(self.terms),
                'bound_arc': self.bound_arc,
                'bound_season': self.bound_season,
                'active': self.active}

    @classmethod
    def from_dict(cls, d: dict) -> "TreatyRecord":
        return cls(parties=tuple(d['parties']),
                   terms=dict(d.get('terms', {})),
                   bound_arc=d['bound_arc'],
                   bound_season=d['bound_season'],
                   active=d.get('active', True))


@dataclass
class TreatyResult:
    accepted: bool
    treaty: Optional[TreatyRecord]
    reason: str


@dataclass
class ExpirationResult:
    treaty: TreatyRecord
    lapsed: bool
    roll_value: float


def propose_treaty(parties: list, terms: dict, world=None) -> TreatyResult:
    """Propose a treaty between parties.

    Canon (treaty_expiration_v30.md, 2026-05-17) specifies the Crown re-binding
    path as the Senator Outward action (§2), which is resolved in
    crown_initiative — not through a generic propose_treaty. No canonized
    non-Senator-Outward treaty-formation protocol exists yet, so this entry
    point raises. Use register_treaty for scaffolding/test insertion and
    Senator Outward (crown_initiative) for the canonical Crown path.
    """
    raise NotImplementedError(
        "sim/provincial/treaty.py:propose_treaty — no canonized generic "
        "formation path. Canon formation is Senator Outward (treaty_expiration_v30 "
        "§2, resolved in crown_initiative). Use register_treaty for test insertion."
    )


def process_treaty_expirations(world, lapse_rate: float = TREATY_LAPSE_RATE_DEFAULT) -> list[ExpirationResult]:
    """Apply §4.5 Treaty Expiration at arc boundary.

    For each active treaty, roll against TREATY_LAPSE_RATE. Lapsed treaties
    are marked inactive (cleared from registers per §4.5). Caller is
    responsible for invoking this only at arc boundaries (season_manager
    detects via check_arc_boundary).
    """
    # [canonical: §4.5 — "Lapsed Treaty: cleared from both factions' treaty
    #  registers. Crown may re-bind via Senator Outward action."]
    rng = world.rng if world is not None and hasattr(world, 'rng') else None
    store = _treaty_store(world)
    results = []
    for key, treaty in list(store.items()):
        if not treaty.active:
            continue
        roll = rng.random() if rng else 0.95  # default to high-lapse if no rng
        lapsed = roll < lapse_rate
        if lapsed:
            treaty.active = False
        results.append(ExpirationResult(treaty=treaty, lapsed=lapsed, roll_value=roll))
    return results


def register_treaty(parties: list, terms: dict, bound_arc: int, bound_season: int,
                    world=None) -> TreatyRecord:
    """Test/scaffolding helper: directly insert a treaty without going
    through propose_treaty (which is canon-gated). Used until Pass 2h lands
    and the proposal protocol becomes the supported insertion path."""
    key = tuple(sorted(parties))
    record = TreatyRecord(parties=key, terms=terms,
                          bound_arc=bound_arc, bound_season=bound_season)
    _treaty_store(world)[key] = record
    return record


def get_active_treaties(world=None) -> list[TreatyRecord]:
    """Inspection helper — active treaties only."""
    return [t for t in _treaty_store(world).values() if t.active]


def reset_registry(world=None):
    """Test helper."""
    _treaty_store(world).clear()
