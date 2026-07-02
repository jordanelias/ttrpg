"""mass_battle.troop_types.registry — troop-type stat presets + gated role menus.
Stage-1 behaviour-frozen extract from orchestration.py (TROOP_TYPE_STATS, stats_for, roles_for,
role_allowed). The "stat home" for the taxonomy (ED-1018): a subunit OF a type draws these
per-subunit combat stats. Depends on config (TROOP_TYPE_ROLES) only — no up-DAG import, no cycle.
Re-imported by orchestration via star-import (Subunit.of_type and the stress-test imports unchanged).
[canonical: mass_battle_v30.md §B.2 troop table; config TROOP_TYPE_ROLES/ROLE_SPEC]"""
from mass_battle.config import *
from mass_battle.equipment import loadout_for

__all__ = ['roles_for', 'role_allowed', 'TROOP_TYPE_STATS', 'stats_for',
           'REACH_SHORT', 'REACH_LONG', 'TROOP_TYPE_REACH', 'reach_for',
           'unit_type_for']


def roles_for(troop_type):
    """Roles a troop type may be assigned (its gated menu); falls back to the 'any' menu."""
    return TROOP_TYPE_ROLES.get(troop_type, TROOP_TYPE_ROLES.get("any", []))

def role_allowed(troop_type, role):
    """True iff `role` is in `troop_type`'s gated menu."""
    return role in roles_for(troop_type)


# ─── CANONICAL TROOP-TYPE STAT PRESETS ──────────────────────────────────────
# The "stat home" for the troop taxonomy: a subunit OF a given type carries these
# per-subunit combat stats. Values are transcribed directly from the canonical BG
# unit table (mass_battle_v30.md §B.2) — the TTRPG Power / Discipline / Morale columns.
# Keyed to match the config TROOP_TYPE_ROLES snake_case taxonomy. Co-located here with
# its accessor (stats_for) and constructor (Subunit.of_type) — the role accessors
# (roles_for / role_allowed) already live in this module. Constructions that do not call
# stats_for / of_type are untouched (byte-exact). dr (armour) and stamina (endurance) are
# intentionally left to inherit: §B.2's Armour column maps to a vs-Piercing DR scale
# (orch L413-417, None=0/Light=1/Medium=2/Heavy=3) whose identity with the Subunit.dr
# field is unconfirmed, and Endur (1-6) has no clean bridge to the 0-100 stamina pool.
# Both are deferred to an explicit follow-up rather than guessed. [ED-1018]
TROOP_TYPE_STATS = {
    # troop_type        : power, discipline, morale   (morale_start defaults to morale)
    "levy":             {"power": 1, "discipline": 1, "morale": 2},
    "light_infantry":   {"power": 3, "discipline": 3, "morale": 4},  # [canonical: mass_battle_v30.md §B.2 — troop-type stat table]
    "heavy_infantry":   {"power": 4, "discipline": 4, "morale": 5},  # [canonical: mass_battle_v30.md §B.2 — troop-type stat table]
    "cavalry":          {"power": 5, "discipline": 5, "morale": 5},
    "archers":          {"power": 3, "discipline": 3, "morale": 3},
    "crossbow":         {"power": 3, "discipline": 3, "morale": 3},
    "sling":            {"power": 2, "discipline": 2, "morale": 3},
    "artillery":        {"power": 2, "discipline": 2, "morale": 3},
    "knights_templar":  {"power": 5, "discipline": 6, "morale": 6},  # [canonical: mass_battle_v30.md §B.2 — troop-type stat table]
}


def stats_for(troop_type):
    """Canonical per-subunit combat stats for a troop type (mass_battle_v30 §B.2), as a
    fresh dict {power, discipline, morale}, or None if the type has no preset. None lets
    the caller fall back to Unit inheritance (byte-exact). Lookup is case-insensitive."""
    if troop_type is None:
        return None
    preset = TROOP_TYPE_STATS.get(str(troop_type).strip().lower())
    return dict(preset) if preset is not None else None


# ─── REACH (Stage A — true-adjacency stand-off primitive) ───────────────────
# [canonical: params/core.md §Reach Terminology (PP-290) — "Short Reach: melee contact (<=1 metre).
#  Applies to most melee weapons." / "Long Reach: extended melee (polearms, spears; <=3 metres)."]
# The 3x ratio is applied to the movement lattice's own pitch (COL_WIDTH=1.0, hierarchy/units.py)
# rather than injecting an unratified meters-per-lattice-unit conversion.
REACH_SHORT = 0.5  # [canonical: params/core.md §Reach Terminology (PP-290) — "Short Reach... <=1 metre"]
REACH_LONG = 1.5   # [canonical: params/core.md §Reach Terminology (PP-290) — "Long Reach... <=3 metres", 3x ratio]

# No TROOP_TYPE_STATS key today is textually a polearm/spear unit (PP-290's literal Long-Reach
# examples). cavalry/knights_templar plausibly carry lances, but PP-290's cited text does not
# actually say "lances" -- that would be an inference beyond the citation, not licensed by it. Left
# empty (every type falls through to Short) rather than fabricating an assignment; extend this table
# when a troop type explicitly wielding a polearm/spear is added, or Jordan rules on cavalry/lances.
TROOP_TYPE_REACH = {}


def reach_for(troop_type):
    """PP-290 reach class for a troop type, in lattice units (COL_WIDTH=1.0 pitch). Unmapped types,
    including bare 'infantry' (a real call-site default, not a TROOP_TYPE_STATS key), fall through
    to Short Reach -- stated here as intended, not an implicit side effect. Lookup is
    case-insensitive, matching stats_for."""
    cls = TROOP_TYPE_REACH.get(str(troop_type).strip().lower()) if troop_type else None
    return REACH_LONG if cls == 'long' else REACH_SHORT


# ─── unit_type (movement audit gate 2, ED-1097) ──────────────────────────────
# [canonical: Jordan-ruled 2026-07-02, verbatim: "Ranged is troop type as per the weapon assigned
#  to troop."] unit_type ('ranged'/'melee') must derive from the troop's ASSIGNED WEAPON, not from
# its role -- ED-1095/T4's mistake was defaulting a mounted_archers spec to role='Kite' without
# this half, so the unit never actually got unit_type='ranged' (role='Kite' carries no unit_type
# of its own; ROLE_SPEC never has). The primitive already existed and was already "NOT YET WIRED
# into resolution" per its own docstring: mass_battle.equipment.loadout_for(troop_type) returns
# (weapon_record, armour_record) from the provisional TROOP_LOADOUT table (mass_battle_v30 §B.2 +
# the mounted_archers extension added alongside this fix); a weapon record's `reach` field is
# already exactly 'melee'/'ranged' (equipment/weapons.py ARSENAL). This wires that existing,
# previously-inert mapping -- no new primitive invented.
def unit_type_for(troop_type):
    """'ranged'/'melee' derived from troop_type's assigned weapon (TROOP_LOADOUT/loadout_for). An
    unmapped troop type (no loadout entry -- e.g. bare 'infantry', a real call-site default that is
    not a TROOP_TYPE_STATS/TROOP_LOADOUT key) falls through to 'melee', preserving every existing
    call site's byte-exact default. Lookup is case-insensitive, matching stats_for/reach_for."""
    weapon, _armour = loadout_for(troop_type)
    if weapon is None:
        return 'melee'
    return weapon.get('reach', 'melee')
