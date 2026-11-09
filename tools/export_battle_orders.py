#!/usr/bin/env python3
"""Cook the mass-battle module's standing-order vocabulary so the season reads it from an artifact, not a second list.

WHY THIS EXISTS (CP-T04-02, `marshal`). A standing order of battle (`order_of_battle`, `engine/season/rosters.yaml:
record_kinds`) names a `role` and a `retreat_at`. The role names are the MODULE's: `modules/mass_battle/config.py::
ROLE_SPEC` is their one owner and `massbattle.ORDER_ROLES` / `ORDER_RETREAT_AT` are the order's two closed sets. The
season (`engine/season/`) names no module by import, so it reads them from `engine/engine_params/battle_orders.json`
through `engine/substrate/battle_orders.py`, a leaf. This is the same shape as `export_names.py` and
`export_composition.py`: one owner, one exporter with a blocking `--check`, one artifact, one leaf reader. A role added to
`ROLE_SPEC` reaches the season's choosers by re-running this exporter; a hand edit of the JSON fails `--check`.

Usage:
    python3 tools/export_battle_orders.py           # write engine/engine_params/battle_orders.json
    python3 tools/export_battle_orders.py --check   # re-derive and diff vs committed (exit 1 on drift)
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
OUT = os.path.join(REPO, 'engine', 'engine_params', 'battle_orders.json')


def build() -> dict:
    """The artifact, derived from the module's own constants; refuses an empty or repeating closed set."""
    if REPO not in sys.path:
        sys.path.insert(0, REPO)
    from modules.mass_battle import massbattle
    from modules.mass_battle.config import ROLE_SPEC
    roles, retreat_at = list(massbattle.ORDER_ROLES), list(massbattle.ORDER_RETREAT_AT)
    for name, values in (('roles', roles), ('retreat_at', retreat_at)):
        if not values or len(set(values)) != len(values):
            raise SystemExit(f'[battle_orders] {name} is empty or repeats: {values!r}')
    if set(roles) != set(ROLE_SPEC):
        raise SystemExit('[battle_orders] ORDER_ROLES is not config.ROLE_SPEC\'s names')
    return {
        '_generated': 'tools/export_battle_orders.py -- do not hand-edit; edit modules/mass_battle/massbattle.py '
                      '(ORDER_ROLES from config.ROLE_SPEC, ORDER_RETREAT_AT)',
        'schema_version': 1,
        'source': 'modules/mass_battle/massbattle.py',
        'roles': roles,
        'retreat_at': retreat_at,
    }


def main(argv):
    text = json.dumps(build(), indent=2, ensure_ascii=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[battle_orders] MISSING {os.path.relpath(OUT, REPO)} -- run without --check.')
            return 1
        if open(OUT, encoding='utf-8').read() != text:
            print(f'[battle_orders] DRIFT -- {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_battle_orders.py')
            return 1
        d = json.loads(text)
        print(f'[battle_orders] OK -- {len(d["roles"])} roles, {len(d["retreat_at"])} retreat_at values.')
        return 0
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print(f'[battle_orders] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
