"""modules.mass_battle.troop_types.table -- the troop file's reader: every troop type and arm, from one data file.

The authored head is `references/troops.yaml`; `tools/export_troops.py` writes it, behind one blocking `--check`, as
`engine/engine_params/troops.json` (the artifact the port reads) and as `troops_data.py` beside this module (the same
document as a Python literal). This module reads the second, once, on first use, and imports no `engine` code and no
other module of this package (so `config.py`, `registry.py`, `recruitment.py` and `equipment/` may all import it
without a cycle). WHY A LITERAL AND NOT THE JSON: a registered module opens no file (A-25;
`engine/season/tests/test_mass_battle_module.py` watches `open` while a field is fought), and the exporter's `--check`
pins the two artifacts equal, so there is no second owner.

THE TABLES IT REPLACED, each now a function of this loader (or a view of it) under its present name and signature:
`stats_for` (the §B.2 stat line), `is_mounted`, `roles_for`, `training_site_for`, `loadout_for_names` (what
`equipment.loadout_for` turns into records) and `cell_cap_of` (what `config.cell_cap_for` wraps with its density flag).
B17.11 adds the four columns code used to read by a troop type's spelling -- `charge_of`, `wheels_fast`,
`default_role_of` and (with `is_mounted`) `mounted` -- and derives reach and support depth from the arm in hand:
`reach_of` and `support_ranks_of` read the `classes` row of the primary arm's class, so no per-type reach table is kept.
The views (`stats_table`, `mounted_types`, `role_menus`, `role_spec_table`, `training_sites`) are built from the file
for a reader that iterates a table; none is a second copy.

IT REFUSES, by name (`TroopFileError`): an unknown or missing column; a troop row naming an arm, armour tier, role or
site kind that is not a member of its closed set; an arm whose mass is stated both here (`mass_kg`) and in personal
combat's export; a `secondary` equal to the `primary`; a column (or section) name that is also a field of `config.EngineConfig`
(B17.12: a value is the troop file's or the config's, never both). The mass check reads
`engine/engine_params/combat_engine_v1.json` (its `weapons` section) as DATA, never an import of `modules/combat/`.
`check` is the one validator. It opens that export, so it runs where a file may be opened -- the exporter, on what it
derives from the YAML, before either artifact is written -- and never inside a field.
"""
from __future__ import annotations

import functools
import json
import os
from typing import Optional

__all__ = ['TroopFileError', 'check', 'engine_config_names', 'combat_weapon_keys', 'COMBAT_EXPORT_PATH', 'troop_types', 'row_of',
           'stats_for', 'is_mounted', 'roles_for', 'training_site_for', 'loadout_for_names', 'cell_cap_of',
           'charge_of', 'wheels_fast', 'default_role_of', 'reach_of', 'support_ranks_of', 'stats_table', 'mounted_types', 'role_menus', 'role_spec_table', 'training_sites']

_REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
COMBAT_EXPORT_PATH = os.path.join(_REPO, 'engine', 'engine_params', 'combat_engine_v1.json')

#: The keys the exporter adds to the file's own; the loader accepts and ignores them.
META_KEYS = ('_generated', 'schema_version', 'source')
HEADER_KEYS = ('site_kinds', 'armour_tiers', 'default_roles', 'role_specs', 'arms', 'classes', 'troops')
ROLE_COLUMNS = ('shape', 'instructions')
ARM_COLUMNS = ('class', 'mass_kg')
CLASS_COLUMNS = ('reach', 'support_ranks')
TROOP_COLUMNS = ('power', 'discipline', 'morale', 'strength', 'mounted', 'charge', 'wheel', 'default_role', 'cell_cap',
                 'ranks', 'primary', 'secondary', 'armour', 'roles', 'training_site', 'min_site_condition', 'upkeep')
STAT_COLUMNS = ('power', 'discipline', 'morale')


class TroopFileError(ValueError):
    """The troop file names something it may not. The message names the section, the row and the offending key."""


def _columns(where, got, allowed, required=()):
    for k in got:
        if k not in allowed:
            raise TroopFileError(f"{where}: unknown column {k!r} (allowed: {', '.join(allowed)})")
    for k in required:
        if k not in got:
            raise TroopFileError(f"{where}: missing column {k!r}")


def _member(where, value, closed, what, nullable=True):
    if value is None and nullable:
        return
    if value not in closed:
        raise TroopFileError(f"{where}: {what} {value!r} is not a member of {sorted(closed)}")


def combat_weapon_keys(path: str = COMBAT_EXPORT_PATH) -> frozenset:
    """The keys of personal combat's weapon roster, from its typed export (`sections.weapons`)."""
    with open(path, encoding='utf-8') as fh:
        return frozenset(json.load(fh)['sections']['weapons'])


def engine_config_names() -> frozenset:
    """The field names of the engine's `EngineConfig` (`config.py`), the other owner of a named value. Imported where it is
    called, never at the top: `config.py` imports this module."""
    from dataclasses import fields
    from modules.mass_battle import config
    return frozenset(f.name for f in fields(config.EngineConfig))


def check(data: dict, combat_weapons=None, config_names=None) -> None:
    """Refuse a troop file that breaks a rule above. `combat_weapons` is the roster's key set (read from the export by
    default), `config_names` the `EngineConfig` field names (likewise). Raises `TroopFileError`."""
    if combat_weapons is None:
        combat_weapons = combat_weapon_keys()
    if config_names is None:
        config_names = engine_config_names()
    for column in HEADER_KEYS + ROLE_COLUMNS + ARM_COLUMNS + CLASS_COLUMNS + TROOP_COLUMNS:
        if column.upper() in config_names:
            raise TroopFileError(f"troop file: the name {column!r} is a column here and a field of `EngineConfig` "
                                 f"(`config.py`); a value has one owner, never both")
    for k in data:
        if k not in HEADER_KEYS and k not in META_KEYS:
            raise TroopFileError(f"troop file: unknown section {k!r} (allowed: {', '.join(HEADER_KEYS)})")
    for k in HEADER_KEYS:
        if k not in data:
            raise TroopFileError(f"troop file: missing section {k!r}")
    sites, tiers = set(data['site_kinds']), set(data['armour_tiers'])
    roles, arms, classes = data['role_specs'], data['arms'], data['classes']
    for role, spec in roles.items():
        _columns(f"role_specs.{role}", spec, ROLE_COLUMNS, ROLE_COLUMNS)
    for r in data['default_roles']:
        _member('default_roles', r, roles, 'role', nullable=False)
    for name, c in classes.items():
        _columns(f"classes.{name}", c, CLASS_COLUMNS, CLASS_COLUMNS)
    for name, arm in arms.items():
        where = f"arms.{name}"
        _columns(where, arm, ARM_COLUMNS, ('class',))
        _member(where, arm['class'], classes, 'class', nullable=False)
        if 'mass_kg' in arm and name in combat_weapons:
            raise TroopFileError(f"{where}: mass stated twice -- `mass_kg` here and the key {name!r} in personal "
                                 f"combat's export; keep it in one place")
    for name, row in data['troops'].items():
        where = f"troops.{name}"
        _columns(where, row, TROOP_COLUMNS, TROOP_COLUMNS)
        _member(where, row['primary'], arms, 'arm (primary)')
        _member(where, row['secondary'], arms, 'arm (secondary)')
        if row['secondary'] is not None and row['secondary'] == row['primary']:
            raise TroopFileError(f"{where}: secondary {row['secondary']!r} equals the primary")
        _member(where, row['armour'], tiers, 'armour tier')
        _member(where, row['training_site'], sites, 'site kind')
        _member(where, row['default_role'], roles, 'role (default_role)')
        for r in (row['roles'] or ()):
            _member(where, r, roles, 'role', nullable=False)


@functools.lru_cache(maxsize=None)
def _data() -> dict:
    """The exported document, imported once, on first use (so the exporter can import `check` before the literal exists).
    The exporter checked it before writing it; `--check` pins it equal to the JSON."""
    from modules.mass_battle.troop_types.troops_data import DATA
    return DATA


def _rows() -> dict:
    return _data()['troops']


def troop_types() -> tuple:
    """Every troop row's name, in the file's order (the unmustered `infantry` body included)."""
    return tuple(_rows())


def row_of(troop_type) -> Optional[dict]:
    """A copy of the troop's row, or None; the name matched exactly."""
    row = _rows().get(troop_type) if isinstance(troop_type, str) else None
    return dict(row) if row is not None else None


def _lower(troop_type) -> str:
    return str(troop_type).strip().lower()


@functools.lru_cache(maxsize=None)
def _stats() -> dict:
    return stats_table()


@functools.lru_cache(maxsize=None)
def _mounted() -> frozenset:
    return mounted_types()


@functools.lru_cache(maxsize=None)
def _menus() -> dict:
    return role_menus()


@functools.lru_cache(maxsize=None)
def _sites() -> dict:
    return training_sites()


def stats_table() -> dict:
    """`{troop type: {power, discipline, morale}}` for each row with a full stat line (today's `TROOP_TYPE_STATS`)."""
    return {t: {k: r[k] for k in STAT_COLUMNS} for t, r in _rows().items() if all(r[k] is not None for k in STAT_COLUMNS)}


def stats_for(troop_type) -> Optional[dict]:
    """The row's stat line as a fresh dict, or None for a type with no full stat line (and for None). Case-insensitive."""
    if troop_type is None:
        return None
    preset = _stats().get(_lower(troop_type))
    return dict(preset) if preset is not None else None


def mounted_types() -> frozenset:
    """The rows that fight mounted (today's `MOUNTED_TYPES`)."""
    return frozenset(t for t, r in _rows().items() if r['mounted'])


def is_mounted(troop_type) -> bool:
    """True iff the row says `mounted`. Case-sensitive, as `MOUNTED_TYPES` was."""
    return troop_type in _mounted()


def role_menus() -> dict:
    """`{troop type: its menu}` for each row with a menu of its own, then `'any': default_roles` (today's
    `TROOP_TYPE_ROLES`)."""
    menus = {t: list(r['roles']) for t, r in _rows().items() if r['roles'] is not None}
    menus['any'] = list(_data()['default_roles'])
    return menus


def roles_for(troop_type) -> list:
    """The roles a troop type may take: its own menu, else `default_roles`. Case-sensitive, as the table was."""
    menus = _menus()
    return list(menus.get(troop_type, menus['any']))


def role_spec_table() -> dict:
    """`{role: {'shape', 'instructions'}}` (today's `config.ROLE_SPEC`), the instructions a tuple."""
    return {r: {'shape': s['shape'], 'instructions': tuple(s['instructions'])} for r, s in _data()['role_specs'].items()}


def training_sites() -> dict:
    """`{troop type: (site kind, least condition fraction)}` for each row trained at a site (today's `TRAINING_SITE`)."""
    return {t: (r['training_site'], r['min_site_condition']) for t, r in _rows().items() if r['training_site'] is not None}


def training_site_for(troop_type) -> Optional[tuple]:
    """`(site_kind, min_condition_fraction)`, or None for a type that needs no site. Case-insensitive."""
    return _sites().get(_lower(troop_type))


def loadout_for_names(troop_type) -> tuple:
    """`(arm key, armour tier)` the row carries, or `(None, None)` for an unknown type, a falsy one, or a row with
    neither (the unmustered `infantry`). Case-insensitive. `equipment.loadout_for` turns the names into records."""
    row = _rows().get(_lower(troop_type)) if troop_type else None
    if row is None or (row['primary'] is None and row['armour'] is None):
        return (None, None)
    return (row['primary'], row['armour'])


def cell_cap_of(troop_type) -> Optional[int]:
    """The most troops a cell of the type holds, or None when the file has no row of that name (exact match). The
    density flag and the fallthrough to `CELL_CAP` are `config.cell_cap_for`'s."""
    row = _rows().get(troop_type) if isinstance(troop_type, str) else None
    return row['cell_cap'] if row is not None else None


def charge_of(troop_type) -> int:
    """The row's charge penetration (ranks punched through on impact); 0 for a type with no row. Exact match, as the
    `== 'cavalry'` it replaced. A recoil that needs "a charger" asks for `charge_of(t) > 0`."""
    row = _rows().get(troop_type) if isinstance(troop_type, str) else None
    return row['charge'] if row is not None else 0


def wheels_fast(troop_type) -> bool:
    """True iff the row makes the fast enveloping wheel (today's `cavalry` and `light_cavalry`). Exact match."""
    row = _rows().get(troop_type) if isinstance(troop_type, str) else None
    return bool(row['wheel']) if row is not None else False


def default_role_of(troop_type) -> Optional[str]:
    """The role a body of this type takes when no role, shape or instructions are named (`Kite` for mounted archers),
    or None. Exact match."""
    row = _rows().get(troop_type) if isinstance(troop_type, str) else None
    return row['default_role'] if row is not None else None


def _class_row(troop_type) -> Optional[dict]:
    """The `classes` row of the class of the troop's primary arm, or None for an unknown type (case-insensitive, as
    `reach_for` was) or one that carries no arm (the unmustered `infantry`)."""
    row = _rows().get(_lower(troop_type)) if troop_type is not None else None
    if row is None or row['primary'] is None:
        return None
    data = _data()
    return data['classes'][data['arms'][row['primary']]['class']]


def reach_of(troop_type) -> Optional[float]:
    """The front-face reach of the arm in hand (its class's `reach`), or None when there is no arm to read; the
    fallthrough to the melee default is `registry.reach_for`'s."""
    cls = _class_row(troop_type)
    return cls['reach'] if cls is not None else None


def support_ranks_of(troop_type) -> Optional[int]:
    """The ranks behind contact the arm in hand reaches (its class's `support_ranks`), or None when there is no arm to
    read; the floor of one is `registry.support_ranks_for`'s."""
    cls = _class_row(troop_type)
    return cls['support_ranks'] if cls is not None else None
