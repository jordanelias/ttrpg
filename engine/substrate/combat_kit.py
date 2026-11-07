"""engine.substrate.combat_kit -- what the personal-combat engine can be armed with, read from its export.

Status: [live, CP-T03-03]. The single runtime reader of the `kit` section of
`engine/engine_params/combat_engine_v1.json` (written by `tools/export_engine_params.py` from
`modules/combat/weapons.py`, `vocabulary.py` and `combatant.py`, behind its blocking `--check`). Same shape as
`names.py`, `descriptors.py` and `composition.py`.

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
    _KIT = json.load(_fh)['sections']['kit']

#: Every key of `modules/combat/weapons.py::WEAPONS`: a Combatant's `weapon` is one of these.
WEAPONS = frozenset(_KIT['weapons'])

#: Every member of `modules/combat/vocabulary.py::ARMOUR_TIERS`: a Combatant's `armor` is one of these.
ARMOUR_TIERS = frozenset(_KIT['armour_tiers'])

#: `{Combatant field: the key a Combatant built with no kit carries}`, the fields being `weapon` and `armor`.
DEFAULTS = dict(_KIT['defaults'])

#: `{Combatant field: the closed set of keys it takes}`; the fields an `arms_kinds` row may name.
FIELDS = {'weapon': WEAPONS, 'armor': ARMOUR_TIERS}
