"""
systems/settlements/sim/registry.py — Settlement registry (closes audit gap G1)

Canon source: systems/settlements/goldenfurt_slice/sim_build_spec.md §1;
              systems/settlements/settlement_layer_v30.md §1.1-1.3, §2.1

The Settlement is the base civic/political unit (settlement_layer §1.1; the
siege-target). Before this module, systems/settlements/sim/settlement.py mapped 1:1
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
import os
from dataclasses import dataclass, field

import yaml

from systems.settlements.sim.ledger import (
    LedgerTag, ledger_add, ledger_get, ledger_has, ledger_sweep,
)

# OI-07 (ED-IN-0091 plan §3 Wave 2 item 4) — the canonical geography source. "PP-726-rebuilt
# geography YAML" per references/id_reservations.yaml's ED-SE-0048 note ("PP-726-rebuilt
# geography YAML (37/55)" — 37 settlements, 55 provinces+settlements combined); authority line
# in the file itself: "AUTHORITY: ED-779 / PP-707 (canonical workplan) / PP-709 (reconciliation)".
_GEOGRAPHY_YAML = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'valoria_geography_v30.yaml')

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
    # [PRE-LPS-1 (schema gap, NOT a port block) — ED-FA-0004, 2026-07-07: legitimacy/popular_support are declared
    #  but NEVER READ OR WRITTEN anywhere in sim/ (zero non-definition references) — an INERT LPS-1
    #  schema stub, not a working per-settlement L/PS pipeline (R2's qualification to U-1). Wiring
    #  them into a Mandate aggregate is ED-FA-0004 Stratum-B work. The self-imposed port block is
    #  DELETED (Jordan, 2026-08-15 — ED-IN-0193); the gap is unchanged and ED-FA-0004 is still open.]
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

    # ── serialization (OI-07, mirrors NPC.to_dict/from_dict in systems/world/sim/npe.py —
    #    engine.autoload.game_state.serialize_world/restore_world dispatch through these
    #    per the established `hasattr(v, 'to_dict')` registry pattern) ──
    def to_dict(self) -> dict:
        return {
            'sid': self.sid, 'name': self.name, 'stype': self.stype,
            'province_id': self.province_id, 'owner_faction': self.owner_faction,
            'governor_id': self.governor_id,
            'prosperity': self.prosperity, 'defense': self.defense, 'order': self.order,
            'fort_level': self.fort_level, 'garrison': self.garrison,
            'legitimacy': self.legitimacy, 'popular_support': self.popular_support,
            'facility_tier': self.facility_tier, 'suspicion': self.suspicion,
            'pressure': self.pressure,
            'active_directive': self.active_directive,
            'religious_building': self.religious_building,
            'church_attention': self.church_attention,
            'governor_emergence': self.governor_emergence,
            'subnational': dict(self.subnational),
            'npc_ids': list(self.npc_ids),
            'ledger': [{'kind': t.kind, 'key': t.key, 'value': t.value,
                        'created_season': t.created_season, 'ttl': t.ttl}
                       for t in self.ledger],
            'open_needs': [list(n) for n in self.open_needs],
            'deck_state': dict(self.deck_state),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Settlement":
        return cls(
            sid=d['sid'], name=d['name'], stype=d['stype'],
            province_id=d['province_id'], owner_faction=d.get('owner_faction'),
            governor_id=d.get('governor_id'),
            prosperity=d.get('prosperity', 0), defense=d.get('defense', 0),
            order=d.get('order', 0),
            fort_level=d.get('fort_level', 0), garrison=d.get('garrison', False),
            legitimacy=d.get('legitimacy', 0), popular_support=d.get('popular_support', 0),
            facility_tier=d.get('facility_tier', 0), suspicion=d.get('suspicion', 0),
            pressure=d.get('pressure', 4.0),
            active_directive=d.get('active_directive'),
            religious_building=d.get('religious_building', 'None'),
            church_attention=d.get('church_attention', 0),
            governor_emergence=d.get('governor_emergence', 0),
            subnational=dict(d.get('subnational', {})),
            npc_ids=list(d.get('npc_ids', [])),
            ledger=[LedgerTag(kind=t['kind'], key=t['key'], value=t.get('value', 1.0),
                               created_season=t.get('created_season', 0), ttl=t.get('ttl'))
                    for t in d.get('ledger', [])],
            open_needs=[list(n) for n in d.get('open_needs', [])],
            deck_state=dict(d.get('deck_state', {})),
        )


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


def populate_from_geography(world, path: str | None = None) -> int:
    """OI-07 (ED-IN-0091 plan §3 Wave 2 item 4) — register every settlement from the canonical
    geography source at world-gen. Deterministic: no RNG draw, so this cannot move any
    RNG-derived campaign golden (win_share / battles_mean / scenes_resolved all read
    `world.rng`, never touched here) — only `serialize_world`'s output dict gains a new key.

    Source: `systems/settlements/valoria_geography_v30.yaml` — the PP-726-rebuilt geography
    file (see `_GEOGRAPHY_YAML`'s module-level citation above; 37 settlements at the time of
    this wave). Field mapping, cited per field:
      - `type` -> Settlement.stype, validated against LEGAL_TYPES (a stray geography-file type
        raises rather than silently registering an illegal settlement type — no fabrication).
      - `stats: [a, b, c]` -> (prosperity, defense, order), in that order, per
        settlement_layer_v30.md §1.3's derived-value table (`| Prosperity | ... |`,
        `| Defense | ... |`, `| Order | ... |`, listed in exactly that row order — the only
        place the doc names a Settlement stat *order*).
      - `territory` -> Settlement.province_id (the geography file's own key name for the same
        referent Settlement.province_id names).
      - `controller` -> Settlement.owner_faction (one entry, S-037/Schoenland, controller
        "Schoenland" — an independent city-state per the geography file's own description, not
        one of the four parliamentary factions in game_state.STARTING_STATS; registered as-is,
        not coerced to a parliamentary faction — no fabrication).
    Every other Settlement field (governor_id, legitimacy, popular_support, facility_tier, ...)
    is left at its dataclass default: the geography file carries no per-settlement value for
    any of them, and PP-726 does not specify starting values for governance-economy fields
    that a later system (charter assignment, governor appointment) is what populates.

    Returns the settlement count registered — the falsifier compares this against the source
    file's own entry count (not a hardcoded literal), so it self-updates if the geography file
    ever grows.
    """
    if path is None:
        path = _GEOGRAPHY_YAML
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    entries = data.get('settlements', {})
    count = 0
    for sid in sorted(entries.keys()):
        e = entries[sid]
        stype = e['type']
        if stype not in LEGAL_TYPES:
            raise ValueError(
                f"geography settlement {sid!r} has illegal type {stype!r} "
                f"(not in registry.LEGAL_TYPES) — refusing to register a non-canonical type")
        prosperity, defense, order = e['stats']  # §1.3 order — raises if not exactly 3
        s = Settlement(
            sid=sid, name=e['name'], stype=stype,
            province_id=e['territory'], owner_faction=e.get('controller'),
            prosperity=prosperity, defense=defense, order=order,
        )
        register_settlement(s, world=world)
        count += 1
    return count
