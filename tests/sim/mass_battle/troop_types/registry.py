"""mass_battle.troop_types.registry — troop-type stat presets + gated role menus.
Stage-1 behaviour-frozen extract from orchestration.py (TROOP_TYPE_STATS, stats_for, roles_for,
role_allowed). The "stat home" for the taxonomy (ED-1018): a subunit OF a type draws these
per-subunit combat stats. Depends on config (TROOP_TYPE_ROLES) only — no up-DAG import, no cycle.
Re-imported by orchestration via star-import (Subunit.of_type and the stress-test imports unchanged).
[canonical: mass_battle_v30.md §B.2 troop table; config TROOP_TYPE_ROLES/ROLE_SPEC]"""
from mass_battle.config import *
from mass_battle.equipment import loadout_for

__all__ = ['roles_for', 'role_allowed', 'TROOP_TYPE_STATS', 'stats_for',
           'REACH_SHORT', 'REACH_LONG', 'REACH_MELEE_DEFAULT', 'TROOP_TYPE_REACH', 'reach_for',
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
    # [v2 Stage E, ED-MB-0014, Jordan P-DEC-1 2026-07-22 "add a pike troop type carrying reach 0.3"]
    # A pike block is disciplined heavy formation infantry whose edge is the pike's REACH (0.3, the
    # longest melee in TROOP_TYPE_REACH below), not raw per-soldier power. Stats mirror heavy_infantry
    # EXACTLY so reach is the sole, isolated differentiator (no fabricated stat line): §B.2 carries no
    # pike row, so mirroring the closest canonical type is the non-inventing choice, pending an explicit
    # §B.2 pike grounding. [provisional-by-analogy: heavy_infantry base + P-DEC-1 reach 0.3]
    "pike":             {"power": 4, "discipline": 4, "morale": 5},
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

# [v2 Stage E, ED-MB-0014, Jordan P-DEC-1 2026-07-22] Per-troop-type FRONT-FACE weapon reach, in
# lattice units (COL_WIDTH=1.0 pitch), feeding the OBB front-reach envelope (hierarchy/units.cell_boxes_for
# -> geometry.obb_front_reach_overlap). Jordan-ruled weapon-class map: non-pole melee 0.1, pole/spear
# 0.2, PIKE 0.3, cavalry/knights lance 0.2, ranged = projectile band (VOLLEY_MAX_RANGE, handled
# separately) + a 0.1 melee sidearm. This SUPERSEDES the flat REACH_SHORT=0.5 placeholder that Stages
# B/C carried while the shape swap (circle->OBB) was validated at unchanged reach. NOTE (flagged for
# Stage F / Jordan): the 0.1/0.2/0.3 scale is a FINER differentiation than PP-290's Short≤1m (0.5) /
# Long≤3m (1.5) meter-grounding above -- P-DEC-1 is the newer, explicit ruling and governs the field OBB
# model; the PP-290 meter→lattice reconciliation (do the two scales coexist, or does one re-ground the
# other?) is deferred to Stage F's historical-revalidation pass, NOT silently overwritten here (REACH_
# SHORT/REACH_LONG stay defined + exported for any PP-290 consumer).
# [canonical: audit/2026-07-22-mass-battle-stress-test/spatial_model_v2_plan.md §9 P-DEC-1 — weapon-class reach map (ED-MB-0014)]
REACH_MELEE_DEFAULT = 0.1   # non-pole melee (P-DEC-1); the fallthrough for unmapped/bare 'infantry'
TROOP_TYPE_REACH = {
    "levy":             0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — non-pole melee (ED-MB-0014)]
    "light_infantry":   0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — non-pole melee (ED-MB-0014)]
    "infantry":         0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — bare-default non-pole melee (ED-MB-0014)]
    "heavy_infantry":   0.2,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — pole/spear (ED-MB-0014)]
    "pike":             0.3,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — PIKE, longest melee reach (ED-MB-0014)]
    "cavalry":          0.2,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — lance (ED-MB-0014)]
    "knights_templar":  0.2,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — lance (ED-MB-0014)]
    "archers":          0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — ranged, melee sidearm (ED-MB-0014)]
    "crossbow":         0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — ranged, melee sidearm (ED-MB-0014)]
    "sling":            0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — ranged, melee sidearm (ED-MB-0014)]
    "artillery":        0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — ranged, melee sidearm (ED-MB-0014)]
    "mounted_archers":  0.1,   # [canonical: spatial_model_v2_plan.md §9 P-DEC-1 — ranged, melee sidearm (ED-MB-0014)]
}


def reach_for(troop_type):
    """[v2 Stage E, ED-MB-0014] Per-troop-type front-face weapon reach in lattice units (COL_WIDTH=1.0
    pitch), from the Jordan-ruled P-DEC-1 weapon-class map (TROOP_TYPE_REACH). Unmapped types, including
    bare 'infantry' (a real call-site default, not a TROOP_TYPE_STATS key), fall through to
    REACH_MELEE_DEFAULT=0.1 (non-pole melee) -- stated as intended, not an implicit side effect. Lookup
    is case-insensitive, matching stats_for."""
    if troop_type is None:
        return REACH_MELEE_DEFAULT
    return TROOP_TYPE_REACH.get(str(troop_type).strip().lower(), REACH_MELEE_DEFAULT)


# ─── unit_type (movement audit gate 2, ED-MB-0001) ──────────────────────────────
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
