"""mass_battle.troop_types.registry — troop-type stat presets + gated role menus.
Stage-1 behaviour-frozen extract from orchestration.py (TROOP_TYPE_STATS, stats_for, roles_for,
role_allowed). The "stat home" for the taxonomy (ED-1018): a subunit OF a type draws these
per-subunit combat stats. Depends on config (TROOP_TYPE_ROLES) only — no up-DAG import, no cycle.
Re-imported by orchestration via star-import (Subunit.of_type and the stress-test imports unchanged).
[canonical: mass_battle_v30.md §B.2 troop table; config TROOP_TYPE_ROLES/ROLE_SPEC]"""
from mass_battle.config import *

__all__ = ['roles_for', 'role_allowed', 'TROOP_TYPE_STATS', 'stats_for']


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
