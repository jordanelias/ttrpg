"""engine.substrate.troops -- the troop file's `deployment` facts the host hands the module, read from the cooked artifact.

The mass-battle module owns the troop file (`references/troops.yaml`, read by `modules/mass_battle/troop_types/table.py`);
`tools/export_troops.py` cooks it into `engine/engine_params/troops.json` behind a blocking `--check`; this is the host's reader
of the one fact it carries onto the field's input record. A LEAF: stdlib only, importable from `engine/` without naming the module
(`battle_orders.py`'s shape).
"""
from __future__ import annotations

import json
import os

_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine_params', 'troops.json'))

with open(_PATH, encoding='utf-8') as _fh:
    _DEPLOYMENT = json.load(_fh)['deployment']

#: `deployment.max_bouts` (B19.20): the most bouts a field is fought in. `field_input` writes it to `MassBattleInput.max_bouts`.
MAX_BOUTS = _DEPLOYMENT['max_bouts']
