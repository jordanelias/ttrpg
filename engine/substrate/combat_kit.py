"""engine.substrate.combat_kit -- what the personal-combat engine can be armed with, read from its export.

Status: [live, CP-T03-03; `FORMS` B14.12]. The single runtime reader of the `kit` section and of `attributes.end.default` of
`engine/engine_params/combat_engine_v1.json` (written by `tools/export_engine_params.py` from
`modules/combat/weapons.py`, `vocabulary.py` and `combatant.py`, behind its blocking `--check`). Same shape as
`names.py`, `descriptors.py` and `composition.py`. It also owns the carry rule (`carry_demand_of`, `carry_demand`, B18.06),
which reads `D_MASS` and `ARMOR_DEMAND` from the export's `cfg` and a weapon's `mass` from its `weapons` section.

IT IS A LEAF: stdlib only (`json`, `os`). The season's `rosters.yaml: arms_kinds` is validated against these sets
AT LOAD (`engine/season/data/rosters.py`), and `queries/world_q.py::kit_of` answers a person who holds no arms with
`DEFAULTS`, so neither the key lists nor the default kit are copied anywhere in the season.
"""
from __future__ import annotations

import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.normpath(os.path.join(_HERE, '..', 'engine_params', 'combat_engine_v1.json'))

with open(_PATH, encoding='utf-8') as _fh:
    _SECTIONS = json.load(_fh)['sections']

_KIT = _SECTIONS['kit']

#: The combat module's default for the `end` attribute (`attributes.end.default`): what a fight reads for a person who
#: authors no Endurance (`seam/wrappers/combat.py::party_end`). Not the sheet scale's floor in `descriptor_registry.yaml`.
END_DEFAULT = _SECTIONS['attributes']['end']['default']

#: Every key of `modules/combat/weapons.py::WEAPONS` WITHOUT a `base` (`UNARMED` included): a Combatant's `weapon` is one of these.
#: A half-sword form is a grip the engine switches into, never a person's kit, so it is not here (B14.12).
WEAPONS = frozenset(_KIT['weapons'])

#: The weapon a person holds when he holds none (`modules/combat/weapons.py::UNARMED`, B18.03): one of `WEAPONS`, a
#: physical record like the rest. `queries/world_q.py::kit_of` returns it for the weapon field once an arms roster exists.
UNARMED = _KIT['unarmed']

#: `{form: its base weapon}` for each record carrying a `base` (the half-sword grips), for a reader that needs the
#: mapping. Disjoint from `WEAPONS`.
FORMS = dict(_KIT['forms'])

#: Every member of `modules/combat/vocabulary.py::ARMOUR_TIERS`: a Combatant's `armor` is one of these.
ARMOUR_TIERS = frozenset(_KIT['armour_tiers'])

#: `{Combatant field: the key a Combatant built with no kit carries}`, the fields being `weapon` and `armor`.
DEFAULTS = dict(_KIT['defaults'])

#: `{Combatant field: the closed set of keys it takes}`; the fields an `arms_kinds` row may name.
FIELDS = {'weapon': WEAPONS, 'armor': ARMOUR_TIERS}

# The carry rule's two coefficients, read from the export's `cfg` (`modules/combat/config.py`: D_MASS and ARMOR_DEMAND).
_D_MASS = _SECTIONS['cfg']['D_MASS']
_ARMOR_DEMAND = _SECTIONS['cfg']['ARMOR_DEMAND']
_WEAPON_RECORDS = _SECTIONS['weapons']


def carry_demand_of(masses: tuple, armour: str) -> float:
    """Strength points demanded by what is CARRIED: D_MASS per kilogram of every carried mass that is not in hand,
    plus the harness's ARMOR_DEMAND. Reads the export's `cfg`.

    `masses` is the kilograms of what is carried and NOT held (the weapon in hand is already charged by
    `combat_systems.str_demand`'s own `D_MASS * mass`); empty, it is the harness term alone, which is what
    `combat_systems.act_cost` charges today. An unknown `armour` tier raises KeyError (a closed set: `ARMOUR_TIERS`)."""
    return _D_MASS * sum(masses) + _ARMOR_DEMAND[armour]


def carry_demand(weapons: tuple, armour: str) -> float:
    """The keyed spelling: looks each weapon's mass up in the export's `weapons` section and calls `carry_demand_of`.
    A person's kit uses this; a troop row, whose arm may have no key here, uses the mass form. One rule, two
    spellings of its argument. `weapons` are the record keys carried and not in hand."""
    return carry_demand_of(tuple(_WEAPON_RECORDS[w]['mass'] for w in weapons), armour)
