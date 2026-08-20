"""engine.substrate.composition — resolve a ROLE to a subsystem callable, without naming it.

Status: [live, 2026-08-20]

WHY. `systems/` stems from `engine/` and `references/`. The campaign driver contradicted that:
`engine/mc_v18.py` imported `systems.factions.sim.faction_action` and `systems.overview.sim.season`
at module level, so the root named its own dependents and the package graph carried a cycle
(`faction_action.py` -> `engine.autoload.game_state` -> `systems.factions.sim.treaty`).

`engine/` now states WHAT it needs — a role name — and `references/module_contracts.yaml`'s
`composition_roles:` block states WHICH module provides it. This module is the resolver, reading the
cooked artifact `engine/engine_params/composition.json` (written by `tools/export_composition.py`,
blocking `--check`). Adding a subsystem to the campaign loop is a row in the registry, not an import
in the engine.

WHY LATE FAILURE IS NOT A RISK HERE, which is the obvious objection to import-by-string: the
exporter imports and resolves every declared target AT EXPORT TIME, behind a blocking CI gate. A
typo or a moved module reds CI, not a campaign run. `require()` additionally caches, so resolution
happens once per role per process and cannot change mid-run.

IT IS A LEAF. stdlib only, no `engine.*` or `systems.*` imports at module level — the `importlib`
call is by string, at first use, which is precisely what keeps `systems` out of `engine`'s import
graph.
"""
from __future__ import annotations

import importlib
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.normpath(os.path.join(_HERE, '..', 'engine_params', 'composition.json'))

with open(_PATH) as _fh:
    _DATA = json.load(_fh)

#: {role -> {target, needed_by}} exactly as references/ declares it.
ROLES = _DATA['roles']

_CACHE = {}


def require(role):
    """Return the callable `references/` binds to `role`. Raises if the role is undeclared.

    Deliberately NOT `get(role, default)`: a missing role is a registry defect, and a silent default
    would let a campaign run with a subsystem quietly absent — the failure mode this indirection
    exists to avoid, not to introduce.
    """
    if role in _CACHE:
        return _CACHE[role]
    row = ROLES.get(role)
    if row is None:
        raise KeyError(
            f'no composition role {role!r}. Declare it under composition_roles: in '
            f'references/module_contracts.yaml and re-run tools/export_composition.py — do not '
            f'import the subsystem directly to work around this.'
        )
    mod_name, attr = row['target'].split(':', 1)
    fn = getattr(importlib.import_module(mod_name), attr)
    _CACHE[role] = fn
    return fn
