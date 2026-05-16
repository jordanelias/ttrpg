# m4_unit_state — Module Four of the v17 strategic-sim integration plan.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Per-faction unit roster, mutation operations (Muster, commit to battle,  # [canonical: N/A — doc]
# apply battle losses), and JSONL-safe serialization.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# This module is FOUNDATIONAL — no dependencies on other v17 modules. Module 3  # [canonical: N/A — doc]
# (Mass Battle Resolution) consumes this module. The integration module wires  # [canonical: N/A — doc]
# UnitRoster instances onto Faction objects.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Canonical sources:  # [canonical: N/A — doc]
#   - mass_battle_v30 Section B.2 (BG Unit Stats) — unit class roster + stats.  # [canonical: N/A — doc]
#   - integration_plan_v3 Section 5 Phase 2c (Unit-token state in Workstream A) —  # [canonical: N/A — doc]
#     defaultdict schema, schema-complete + semantics-partial split.  # [canonical: N/A — doc]
#   - params/mass_combat.md — unit cost and recruitment doctrine reference.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Schema-complete (9 classes): Levy, LightInf, HeavyInf, Cavalry, Archer,  # [canonical: N/A — doc]
# Crossbow, Sling, Artillery, KnightsTemplar.  # [canonical: N/A — doc]
# Semantics-partial (3 active): Levy, LightInf, HeavyInf.  # [canonical: N/A — doc]
#  # [canonical: N/A — doc]
# Provisional assumptions: see sim_verification_ledger provisional_assumptions  # [canonical: N/A — doc]
# block. Tags M4_ASSUMPTION_ONE through M4_ASSUMPTION_FIVE.  # [canonical: N/A — doc]

import json
from collections import defaultdict
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════
# UNIT CLASS REGISTRY
# ═══════════════════════════════════════════════════════════════════════════

# Schema-complete unit class roster
# [canonical: mass_battle_v30 §B.2 — 9 BG unit classes]
UNIT_CLASSES = (
    'Levy',
    'LightInf',
    'HeavyInf',
    'Cavalry',
    'Archer',
    'Crossbow',
    'Sling',
    'Artillery',
    'KnightsTemplar',
)

# Active classes per integration_plan §5 Phase 2c (semantics-partial)
# [canonical: integration_plan_v3 §5 Phase 2c — Active classes: Levy, LightInf, HeavyInf]
ACTIVE_UNIT_CLASSES = frozenset({'Levy', 'LightInf', 'HeavyInf'})

# Reserved classes — schema present, semantics deferred to later modules
# [canonical: integration_plan_v3 §5 Phase 2c — Reserved classes]
RESERVED_UNIT_CLASSES = frozenset({
    'Cavalry', 'Archer', 'Crossbow', 'Sling', 'Artillery', 'KnightsTemplar',
})

# Canonical per-class stat block per mass_battle_v30 §B.2 table
# Fields: martial, endurance, discipline, health, bg_dmg_mod, ttrpg_dmg_mod,
#         armour, anti_armour, volley
# [canonical: mass_battle_v30 §B.2 — BG Unit Stats table]
UNIT_STATS = {
    'Levy': {
        'martial': 1, 'endurance': 1, 'discipline': 1, 'health': 7,                # [canonical: mass_battle_v30 §B.2 Levy row]
        'bg_dmg_mod': 1, 'ttrpg_dmg_mod': 1,                                       # [canonical: mass_battle_v30 §B.2 + PP-245 TTRPG Dmg Mod table]
        'armour': 'None', 'anti_armour': False, 'volley': False,
    },
    'LightInf': {
        'martial': 3, 'endurance': 3, 'discipline': 3, 'health': 9,                # [canonical: mass_battle_v30 §B.2 Light Infantry row]
        'bg_dmg_mod': 2, 'ttrpg_dmg_mod': 1,                                       # [canonical: mass_battle_v30 §B.2 + PP-245]
        'armour': 'Light', 'anti_armour': False, 'volley': False,
    },
    'HeavyInf': {
        'martial': 4, 'endurance': 4, 'discipline': 4, 'health': 10,               # [canonical: mass_battle_v30 §B.2 Heavy Infantry row]
        'bg_dmg_mod': 4, 'ttrpg_dmg_mod': 2,                                       # [canonical: mass_battle_v30 §B.2 + PP-245]
        'armour': 'Medium', 'anti_armour': False, 'volley': False,
    },
    'Cavalry': {
        'martial': 4, 'endurance': 3, 'discipline': 5, 'health': 9,                # [canonical: mass_battle_v30 §B.2 Cavalry row]
        'bg_dmg_mod': 5, 'ttrpg_dmg_mod': 3,                                       # [canonical: mass_battle_v30 §B.2 + PP-245]
        'armour': 'Heavy', 'anti_armour': False, 'volley': False,
    },
    'Archer': {
        'martial': 3, 'endurance': 2, 'discipline': 3, 'health': 8,                # [canonical: mass_battle_v30 §B.2 Archer row]
        'bg_dmg_mod': 0, 'ttrpg_dmg_mod': 0,                                       # [canonical: mass_battle_v30 §B.2 + PP-245]
        'armour': 'Light', 'anti_armour': False, 'volley': True,
    },
    'Crossbow': {
        'martial': 3, 'endurance': 2, 'discipline': 3, 'health': 8,                # [canonical: mass_battle_v30 §B.2 Crossbow row]
        'bg_dmg_mod': 0, 'ttrpg_dmg_mod': 0,                                       # [canonical: mass_battle_v30 §B.2 + PP-245 (Crossbow note +1 vs med/heavy post-DR)]
        'armour': 'Light', 'anti_armour': False, 'volley': True,
    },
    'Sling': {
        'martial': 2, 'endurance': 2, 'discipline': 2, 'health': 8,                # [canonical: mass_battle_v30 §B.2 Sling row]
        'bg_dmg_mod': 0, 'ttrpg_dmg_mod': 0,                                       # [canonical: mass_battle_v30 §B.2 — "by ammo (−2D)" — base 0]
        'armour': 'Light', 'anti_armour': False, 'volley': True,
    },
    'Artillery': {
        'martial': 2, 'endurance': 2, 'discipline': 2, 'health': 8,                # [canonical: mass_battle_v30 §B.2 Artillery row]
        'bg_dmg_mod': 3, 'ttrpg_dmg_mod': 2,                                       # [canonical: mass_battle_v30 §B.2 + PP-245]
        'armour': 'None', 'anti_armour': True, 'volley': True,
    },
    'KnightsTemplar': {
        'martial': 5, 'endurance': 5, 'discipline': 6, 'health': 11,               # [canonical: mass_battle_v30 §B.2 Knights Templar row]
        'bg_dmg_mod': 5, 'ttrpg_dmg_mod': 3,                                       # [canonical: mass_battle_v30 §B.2 + PP-245]
        'armour': 'Heavy', 'anti_armour': True, 'volley': False,
    },
}


# Default class minted by Muster action
# [canonical: integration_plan_v3 §5 Phase 2c — "Muster action: mints Levy tokens in territory"]
MUSTER_DEFAULT_CLASS = 'Levy'


# Movement model for commit-to-battle
# [canonical: integration_plan_v3 §5 Phase 2c — option (b) recommended for canon fidelity]
# [M4_ASSUMPTION_ONE: option (b) adopted as default; can be overridden by integration]
COMMITMENT_ADJACENCY_MODEL = 'adjacent_to_target'


# ═══════════════════════════════════════════════════════════════════════════
# VALIDATION HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def validate_unit_class(name):
    # [canonical: mass_battle_v30 §B.2 — 9-class enum]
    return name in UNIT_CLASSES


def is_active_class(name):
    # [canonical: integration_plan_v3 §5 Phase 2c — active vs reserved split]
    return name in ACTIVE_UNIT_CLASSES


def is_adjacent(attacker_tid, target_tid, adjacency):
    # [canonical: M1 ADJACENCY graph — direct-neighbour relation]
    # Thin wrapper around the adjacency dict for clarity.
    return target_tid in adjacency.get(attacker_tid, set())


# ═══════════════════════════════════════════════════════════════════════════
# POOL CONTRIBUTION (used by Module 3's resolve_battle)
# ═══════════════════════════════════════════════════════════════════════════

def pool_contribution(committed_units):
    # [canonical: mass_battle_v30 §B.3 Step 3 — "Pool = sum of all engaged unit Martial values"]
    # committed_units: {unit_class: count}
    total = 0
    for unit_class, count in committed_units.items():
        if unit_class not in UNIT_STATS:
            raise ValueError(f"Unknown unit class: {unit_class}")
        total += count * UNIT_STATS[unit_class]['martial']
    return total


# ═══════════════════════════════════════════════════════════════════════════
# UNIT ROSTER — per-faction state container
# ═══════════════════════════════════════════════════════════════════════════

class UnitRoster:
    # [canonical: integration_plan_v3 §5 Phase 2c — defaultdict(lambda: defaultdict(int)) schema]
    # [M4_ASSUMPTION_FOUR: per-faction state, not per-world]

    def __init__(self):
        self._units = defaultdict(lambda: defaultdict(int))

    # ─── Mutation ───────────────────────────────────────────────────────

    def muster(self, territory_id, count=1, unit_class=None):
        # [canonical: integration_plan_v3 §5 Phase 2c — "Muster action: mints Levy tokens in territory"]
        # [M4_ASSUMPTION_TWO: only active classes can be mustered; reserved classes raise]
        # [M4_ASSUMPTION_THREE: single-territory muster; multi-territory or doctrine variation out of scope]
        if unit_class is None:
            unit_class = MUSTER_DEFAULT_CLASS
        if not validate_unit_class(unit_class):
            raise ValueError(f"Unknown unit class: {unit_class}")
        if not is_active_class(unit_class):
            raise ValueError(
                f"Cannot muster reserved class '{unit_class}' — "
                f"semantics-partial deferred per integration_plan §5 Phase 2c"
            )
        if count <= 0:
            raise ValueError(f"Muster count must be positive; got {count}")
        self._units[territory_id][unit_class] += count

    def commit_to_battle(self, attacker_territory, target_territory,
                         units, adjacency):
        # [canonical: mass_battle_v30 §B.3 + integration_plan_v3 §5 Phase 2c]
        # [M4_ASSUMPTION_ONE: adjacent-to-target adjacency required (option b)]
        # [M4_ASSUMPTION_TWO: only active classes commitable]
        # units: {unit_class: count} — what to commit
        if not is_adjacent(attacker_territory, target_territory, adjacency):
            raise ValueError(
                f"Cannot commit from {attacker_territory} to {target_territory}: "
                f"not adjacent. Required by COMMITMENT_ADJACENCY_MODEL='{COMMITMENT_ADJACENCY_MODEL}'."
            )
        # Validate request before mutating
        for unit_class, count in units.items():
            if not validate_unit_class(unit_class):
                raise ValueError(f"Unknown unit class: {unit_class}")
            if not is_active_class(unit_class):
                raise ValueError(
                    f"Cannot commit reserved class '{unit_class}' — "
                    f"semantics-partial deferred"
                )
            if count <= 0:
                raise ValueError(f"Commit count must be positive; got {count}")
            available = self._units[attacker_territory][unit_class]
            if count > available:
                raise ValueError(
                    f"Insufficient {unit_class} in {attacker_territory}: "
                    f"requested {count}, available {available}"
                )
        # Apply commit
        committed = {}
        for unit_class, count in units.items():
            self._units[attacker_territory][unit_class] -= count
            committed[unit_class] = count
        self._prune_zeros(attacker_territory)
        return committed

    def apply_battle_losses(self, territory_id, losses):
        # [canonical: mass_battle_v30 §B.3 Step 5 — damage reduces unit Health → Formation Break]
        # [M4_ASSUMPTION_FIVE: aggregate-count semantics; no per-token identity]
        # losses: {unit_class: count_to_remove}
        for unit_class, count in losses.items():
            if not validate_unit_class(unit_class):
                raise ValueError(f"Unknown unit class: {unit_class}")
            current = self._units[territory_id][unit_class]
            self._units[territory_id][unit_class] = max(0, current - count)
        self._prune_zeros(territory_id)

    def _prune_zeros(self, territory_id):
        # Remove unit classes with 0 count from the territory's inner dict.
        inner = self._units.get(territory_id)
        if inner is None:
            return
        zero_keys = [k for k, v in inner.items() if v == 0]
        for k in zero_keys:
            del inner[k]
        # Don't prune the outer territory key — preserves the empty-territory state.

    # ─── Accessors ──────────────────────────────────────────────────────

    def unit_count(self, territory_id, unit_class):
        # [canonical: derived accessor — sums per integration_plan §5 Phase 2c schema]
        if not validate_unit_class(unit_class):
            raise ValueError(f"Unknown unit class: {unit_class}")
        return self._units.get(territory_id, {}).get(unit_class, 0)

    def total_units(self, territory_id=None):
        # [canonical: derived accessor]
        if territory_id is not None:
            return sum(self._units.get(territory_id, {}).values())
        return sum(
            sum(inner.values()) for inner in self._units.values()
        )

    def territories_with_units(self):
        # [canonical: derived accessor — returns set of territory IDs with at least one unit]
        return {tid for tid, inner in self._units.items() if sum(inner.values()) > 0}

    def units_in_territory(self, territory_id):
        # [canonical: derived accessor — returns dict copy of {unit_class: count} for the territory]
        return dict(self._units.get(territory_id, {}))

    # ─── Serialization ─────────────────────────────────────────────────

    def to_dict(self):
        # [canonical: integration_plan_v3 §5 Phase 2c — defaultdict doesn't serialize; convert to plain dict]
        return {tid: dict(inner) for tid, inner in self._units.items() if sum(inner.values()) > 0}

    @classmethod
    def from_dict(cls, d):
        # [canonical: integration_plan_v3 §5 Phase 2c — JSONL round-trip]
        roster = cls()
        for tid, inner in d.items():
            for unit_class, count in inner.items():
                if not validate_unit_class(unit_class):
                    raise ValueError(f"Unknown unit class in serialized data: {unit_class}")
                if count < 0:
                    raise ValueError(f"Negative count in serialized data: {unit_class}={count}")
                if count > 0:
                    roster._units[tid][unit_class] = count
        return roster

    def to_json(self):
        # [canonical: integration_plan_v3 §5 Phase 2c — JSONL output]
        return json.dumps(self.to_dict(), sort_keys=True)

    @classmethod
    def from_json(cls, s):
        return cls.from_dict(json.loads(s))

    # ─── Equality + repr ───────────────────────────────────────────────

    def __eq__(self, other):
        if not isinstance(other, UnitRoster):
            return NotImplemented
        return self.to_dict() == other.to_dict()

    def __hash__(self):
        return hash(self.to_json())

    def __repr__(self):
        return f"UnitRoster({self.to_dict()})"
