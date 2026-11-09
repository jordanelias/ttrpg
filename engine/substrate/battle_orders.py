"""engine.substrate.battle_orders -- the standing order of battle's closed sets, read from the cooked artifact.

The mass-battle module owns the vocabulary (`modules/mass_battle/massbattle.py::ORDER_ROLES`, `config.ROLE_SPEC`'s names,
and `ORDER_RETREAT_AT`); `tools/export_battle_orders.py` cooks it into `engine/engine_params/battle_orders.json` behind a
blocking `--check`; this is its single runtime reader. The season (`marshal`'s `role` and `retreat_at`, the
`order_of_battle` Record, the chooser's fan) reads these two tuples and spells no role. A LEAF: stdlib only, importable
from `engine/` and from the module's tests without either naming the other (`names.py`' shape).
"""
from __future__ import annotations

import json
import os

_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'engine_params',
                                      'battle_orders.json'))

with open(_PATH, encoding='utf-8') as _fh:
    _DATA = json.load(_fh)

#: The roles a standing order may name, in `ROLE_SPEC`'s order.
ROLES = tuple(_DATA['roles'])

#: The values of an order's `retreat_at` (`none`, or the share of starting strength at which the side falls back).
RETREAT_AT = tuple(_DATA['retreat_at'])
