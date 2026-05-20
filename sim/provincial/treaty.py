"""
sim/provincial/treaty.py — Crown Treaties + Treaty Expiration (90-95%/arc lapse per v12c)

Canon source: designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md §4.5 + §4.7

PARTIAL IMPLEMENTATION:
  - process_treaty_expirations: implemented against §4.5 (Treaty Expiration
    at arc boundary, TREATY_LAPSE_RATE).
  - propose_treaty: canon-gated. The proposal protocol references
    designs/provincial/treaty_expiration_v30.md (canon authoring pending
    Pass 2h). Stub form retained — raises NotImplementedError with explicit
    canon-gate note.

[ASSUMPTION: treaty registry on Faction — basis: treaties are bilateral
 (Crown<->target) and naturally faction-scoped. game_state.Faction does
 not currently expose a treaties field. process_treaty_expirations reads
 from world-level dict if available, falls back to module state.]

Dependencies:
  - sim/autoload/dice_engine
  - sim/autoload/season_manager

Entry points:
  - propose_treaty(parties: list, terms: dict, world: GameState) -> TreatyResult
    [CANON-GATED — Pass 2h authoring pending]
  - process_treaty_expirations(world: GameState) -> list[ExpirationResult]
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


# Module-level treaty registry (until Faction.treaties lands)
# Key: (party_a, party_b) tuple sorted; Value: TreatyRecord
_treaty_registry: dict[tuple, "TreatyRecord"] = {}


@dataclass
class TreatyRecord:
    parties: tuple
    terms: dict
    bound_arc: int
    bound_season: int
    active: bool = True


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
    """[CANON-GATED] Propose a treaty between parties.

    Canon authoring for the proposal protocol (Pass 2h) is pending per the
    stub's original canon-source declaration. The decision tree (who can
    initiate, what terms are bindable, how consent is rolled, what
    constitutes a Casus Belli per §4.4.1, the Senator Outward action's role
    per §4.5) is not yet specified in implementable detail. Raises until
    canon lands.
    """
    raise NotImplementedError(
        "sim/provincial/treaty.py:propose_treaty — Pass 2h canon authoring pending. "
        "§4.5 references Senator Outward action; §4.7 CONSENT_RATE specified but "
        "the consent decision protocol is not. Awaiting designs/provincial/"
        "treaty_expiration_v30.md."
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
    results = []
    for key, treaty in list(_treaty_registry.items()):
        if not treaty.active:
            continue
        roll = rng.random() if rng else 0.95  # default to high-lapse if no rng
        lapsed = roll < lapse_rate
        if lapsed:
            treaty.active = False
        results.append(ExpirationResult(treaty=treaty, lapsed=lapsed, roll_value=roll))
    return results


def register_treaty(parties: list, terms: dict, bound_arc: int, bound_season: int) -> TreatyRecord:
    """Test/scaffolding helper: directly insert a treaty without going
    through propose_treaty (which is canon-gated). Used until Pass 2h lands
    and the proposal protocol becomes the supported insertion path."""
    key = tuple(sorted(parties))
    record = TreatyRecord(parties=key, terms=terms,
                          bound_arc=bound_arc, bound_season=bound_season)
    _treaty_registry[key] = record
    return record


def get_active_treaties() -> list[TreatyRecord]:
    """Inspection helper — active treaties only."""
    return [t for t in _treaty_registry.values() if t.active]


def reset_registry():
    """Test helper."""
    _treaty_registry.clear()
