"""modules.mass_battle.troop_types.registry — troop-type stat presets + gated role menus.
The "stat home" for the taxonomy (ED-1018): a subunit OF a type draws these per-subunit combat stats. [B17.10] The
rows are authored once, in the troop file (`references/troops.yaml`, read by `troop_types/table.py`); `TROOP_TYPE_STATS`
and `MOUNTED_TYPES` are that file read as tables, and `stats_for`, `is_mounted` and `roles_for` are its loader's
functions under their old names. Reach and support depth are derived from the arm in hand (B17.11) and the four columns
code once read by a type's name (`charge`, `wheel`, `default_role`, `mounted`) are read through the loader.
Depends on config and the loader only — no up-DAG import, no cycle.
[canonical: mass_battle_v30.md §B.2 troop table; config TROOP_TYPE_ROLES/ROLE_SPEC]"""
from modules.mass_battle.config import *
import modules.mass_battle.config as _cfg
import functools as _functools
from modules.mass_battle.equipment import loadout_for
from modules.mass_battle.troop_types import table as _table

__all__ = ['MOUNTED_TYPES', 'is_mounted', 'roles_for', 'role_allowed', 'TROOP_TYPE_STATS', 'stats_for',
           'REACH_SHORT', 'REACH_MELEE_DEFAULT', 'reach_for', 'charge_for', 'wheels_fast', 'default_role_for',
           'support_ranks_for', 'support_weight',
           'unit_type_for']


def is_mounted(troop_type):
    """True iff `troop_type` fights mounted (the troop file's `mounted` column). Case-sensitive."""
    return _table.is_mounted(troop_type)


def roles_for(troop_type):
    """Roles a troop type may be assigned (its gated menu); falls back to the 'any' menu."""
    return _table.roles_for(troop_type)

def role_allowed(troop_type, role):
    """True iff `role` is in `troop_type`'s gated menu."""
    return role in roles_for(troop_type)


# ─── CANONICAL TROOP-TYPE STAT PRESETS ──────────────────────────────────────
# The "stat home" for the troop taxonomy: a subunit OF a given type carries these per-subunit combat stats, the
# TTRPG Power / Discipline / Morale columns of the canonical BG unit table (mass_battle_v30.md §B.2), authored in the
# troop file's rows (each row's provenance is its entry there; the pike, spearmen, skirmishers, mounted_archers and
# light_cavalry lines are PROVISIONAL-BY-ANALOGY to the nearest canonical type, ED-MB-0014 and ED-IN-0306).
# Keyed to match the troop-type snake_case taxonomy. Accessor: stats_for; constructor: Unit.of_type. dr (armour) and
# stamina (endurance) are intentionally left to inherit: §B.2's Armour column maps to a vs-Piercing DR scale
# (None=0/Light=1/Medium=2/Heavy=3) whose identity with the Unit.dr field is unconfirmed, and Endur (1-6) has no clean
# bridge to the 0-100 stamina pool. [ED-1018]
TROOP_TYPE_STATS = _table.stats_table()
# Types that fight mounted: the one owner of "is this a horse" is the troop file's `mounted` column. knights_templar is
# deliberately NOT here.
MOUNTED_TYPES = _table.mounted_types()


def stats_for(troop_type):
    """Canonical per-subunit combat stats for a troop type (mass_battle_v30 §B.2), as a
    fresh dict {power, discipline, morale}, or None if the type has no preset. None lets
    the caller fall back to Army inheritance. Lookup is case-insensitive."""
    return _table.stats_for(troop_type)


# ─── REACH (Stage A — true-adjacency stand-off primitive) ───────────────────
# [canonical: params/core.md §Reach Terminology (PP-290) — "Short Reach: melee contact (<=1 metre).
#  Applies to most melee weapons." / "Long Reach: extended melee (polearms, spears; <=3 metres)."]
# The 3x ratio is applied to the movement lattice's own pitch (COL_WIDTH=1.0, hierarchy/units.py)
# rather than injecting an unratified meters-per-lattice-unit conversion.
REACH_SHORT = 0.5  # [canonical: params/core.md §Reach Terminology (PP-290) — "Short Reach... <=1 metre"]

# [v2 Stage E, ED-MB-0014, Jordan P-DEC-1 2026-07-22] FRONT-FACE weapon reach, in lattice units (COL_WIDTH=1.0
# pitch), feeding the front-reach body (hierarchy/units.cell_bodies_for -> geometry.reach_reaches). The Jordan-ruled
# weapon-class map is the troop file's `classes` (non-pole melee 0.1, pole/spear 0.2, PIKE 0.3, a missile arm used hand
# to hand 0.1; a missile troop's projectile band is VOLLEY_MAX_RANGE, handled separately); [B17.11] a troop
# type's reach is that of the class of the arm in hand, read through the loader, not kept per type. NOTE (flagged for
# Jordan): the 0.1/0.2/0.3 scale is a FINER differentiation than PP-290's Short<=1m (0.5) / Long<=3m (1.5)
# meter-grounding above -- P-DEC-1 is the newer, explicit ruling and governs the field OBB model; whether the two scales
# coexist or one re-grounds the other is open (REACH_SHORT/REACH_LONG stay defined + exported for any PP-290 consumer).
# [canonical: audit/2026-07-22-mass-battle-stress-test/spatial_model_v2_plan.md §9 P-DEC-1 — weapon-class reach map (ED-MB-0014)]
REACH_MELEE_DEFAULT = 0.1   # non-pole melee (P-DEC-1); the fallthrough for unmapped/bare 'infantry'


@_functools.lru_cache(maxsize=None)   # pure in troop_type and the static troop file; read per atom per tick
def reach_for(troop_type):
    """[v2 Stage E, ED-MB-0014] Front-face weapon reach in lattice units (COL_WIDTH=1.0 pitch) of the arm the troop
    type carries (the troop file's class row, P-DEC-1). A type with no arm, including bare 'infantry' (a real call-site
    default), and an unmapped one fall through to REACH_MELEE_DEFAULT=0.1 (non-pole melee). Lookup is
    case-insensitive, matching stats_for."""
    reach = _table.reach_of(troop_type)
    return REACH_MELEE_DEFAULT if reach is None else reach


def charge_for(troop_type):
    """The charge penetration (ranks punched through on impact) of the troop file's row; 0 for any other type."""
    return _table.charge_of(troop_type)


def wheels_fast(troop_type):
    """True iff the troop file's row makes the fast enveloping wheel."""
    return _table.wheels_fast(troop_type)


def default_role_for(troop_type):
    """The role a body of this type takes when none is named (the troop file's `default_role`), or None."""
    return _table.default_role_of(troop_type)


# ─── support depth (MB-07, J-18 (A), ED-MB-0041) ─────────────────────────────────
# Ranks behind contact a troop type's weapon reaches: the `support_ranks` of the class of the arm in hand (troop file),
# so it is read, not kept per type (sword/axe: only the rank directly behind presses its blade into the fight; a spear is
# levelled from the second rank behind; a pike's points project from the third; a missile arm used hand to hand is
# non-pole). Lives here, not in config, because config sits below the loader's callers. [ASSUMPTION; medium; Jordan to correct]
@_functools.lru_cache(maxsize=None)   # pure in troop_type and the static troop file; read per supporter cell
def support_ranks_for(troop_type):
    ranks = _table.support_ranks_of(troop_type)
    return 1 if ranks is None else ranks


def support_weight(depth, troop_type):
    """Pool weight of a cell `depth` ranks behind its contact rank, for one troop type. The single owner of
    the support stack: core.exchange._pair_engaged_troops and geometry.support_engage_frac both read it.
    The cap flag and the weight table are read from config at CALL time, so a test can set the control
    without reloading anything."""
    if _cfg.MB_SUPPORT_RANK_CAP and depth > support_ranks_for(troop_type):
        return 0.0
    return _cfg.SUPPORT_WEIGHTS.get(depth, _cfg.SUPPORT_WEIGHT_FLOOR)


# ─── unit_type (movement audit gate 2, ED-MB-0001) ──────────────────────────────
# [canonical: Jordan-ruled 2026-07-02, verbatim: "Ranged is troop type as per the weapon assigned
#  to troop."] unit_type ('ranged'/'melee') derives from the troop's ASSIGNED WEAPON, not from its
# role (role='Kite' carries no unit_type of its own; ROLE_SPEC never has).
# modules.mass_battle.equipment.loadout_for(troop_type) returns (weapon_record, armour_record) from
# the provisional TROOP_LOADOUT table (mass_battle_v30 §B.2); a weapon record's `reach` field is
# exactly 'melee'/'ranged' (equipment/weapons.py ARSENAL).
def unit_type_for(troop_type):
    """'ranged'/'melee' derived from troop_type's assigned weapon (TROOP_LOADOUT/loadout_for). An
    unmapped troop type (no loadout entry -- e.g. bare 'infantry', a real call-site default that is
    not a TROOP_TYPE_STATS/TROOP_LOADOUT key) falls through to 'melee'. Lookup is case-insensitive, matching stats_for/reach_for."""
    weapon, _armour = loadout_for(troop_type)
    if weapon is None:
        return 'melee'
    return weapon.get('reach', 'melee')
