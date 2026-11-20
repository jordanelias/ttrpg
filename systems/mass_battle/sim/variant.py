"""systems.mass_battle.sim.variant -- an engine built from an explicit `EngineConfig` (B17.12).

THE ONE PLACE A PROCESS VARIABLE REACHES THE MASS-BATTLE ENGINE. `modules/mass_battle/` reads no process variable: its
switches and coefficients are the fields of `config.EngineConfig`, and the shipped values are `config.DEFAULT`. A
workbench run that wants another set (the byte-exact batteries' pins, a probe that turns friction off, a stress arm)
states it as `dataclasses.replace(DEFAULT, PER_CELL=False)` or reads it off its own variables with `cfg_from_environ`,
and builds the engine from it. That is done here and only under `systems/mass_battle/sim/`.

WHY A BUILT ENGINE AND NOT A PARAMETER THREADED THROUGH EVERY CALL. The engine's modules read their constants as
module names (`from modules.mass_battle.config import *`), several hundred read sites in functions that have no
`cfg` argument to receive one. A variant is therefore a second copy of the module tree whose `config` was built from
the variant's config, so every read in it is a read of that config. `install` and `built` DO swap the process's
`modules.mass_battle` tree (and `restore` puts the shipped one back): a caller that installs must restore, as
`test_body_no_interpenetration`'s fixture does. A declared departure from 04 C.12's "no ambient selector". There is no
`config.active()` and no `using()`: `resolve_field(inp, rng, cfg=variant)` on the shipped tree refuses a config
that is not its own and names this module, and the variant tree's own `resolve_field` accepts it.

TWO WAYS TO USE IT.
    `install(cfg)`        a script (`bat.py`, a probe) builds the tree for the whole process, before it imports the engine;
                          a test file calls it per case and `restore()` once, in its teardown.
    `with built(cfg):`    a test builds it for the block and gets the shipped tree back, restored name by name, after.
Both evict `modules.mass_battle.*` and `systems.mass_battle.sim.*` (this module stays) so the next import executes them
afresh against the variant's `config`.
"""
from __future__ import annotations

import contextlib
import dataclasses
import importlib
import sys

from modules.mass_battle import config as _shipped

EngineConfig = _shipped.EngineConfig
DEFAULT = _shipped.DEFAULT

#: The one field whose process-variable name is not its own (kept from before the config object).
ENV_NAME = {'SIGMA_HEAD_ENABLED': 'SIGMA_HEAD'}

_MISSING = object()


def _parse(kind, text):
    """One variable's text as its field's type: a switch is `'1'` or not, a number is the number."""
    if kind is bool:
        return text == '1'
    return kind(text)


def cfg_from_environ(environ, base=None):
    """`base` (default `DEFAULT`) with every field a variable in `environ` names replaced. The names are the fields' own,
    but `SIGMA_HEAD` for `SIGMA_HEAD_ENABLED`; a variable that names no field is not read."""
    base = DEFAULT if base is None else base
    changes = {}
    for f in dataclasses.fields(EngineConfig):
        name = ENV_NAME.get(f.name, f.name)
        if name in environ:
            changes[f.name] = _parse(f.type, environ[name])
    return dataclasses.replace(base, **changes)


def _owned(name):
    return (name == 'modules.mass_battle' or name.startswith('modules.mass_battle.')
            or (name.startswith('systems.mass_battle.sim.') and name != __name__))


def _evict():
    """Take every owned module out of `sys.modules`. Returns what to put back: the modules, and each parent's attribute
    for them (`import a.b as m` reads the parent's attribute first, so a stale one would hand back the wrong tree)."""
    saved = {n: sys.modules.pop(n) for n in [n for n in sys.modules if _owned(n)]}
    attrs = {}
    for n in saved:
        parent_name, _, child = n.rpartition('.')
        parent = sys.modules.get(parent_name) or saved.get(parent_name)
        if parent is not None:
            attrs[(parent, child)] = getattr(parent, child, _MISSING)
    return saved, attrs


def _build(cfg):
    config = importlib.import_module('modules.mass_battle.config')
    config.rebind(cfg)
    return config


_held = None        # (modules, parent attributes) of the SHIPPED tree, while a variant is installed


def install(cfg):
    """Build the engine from `cfg` and keep it: for a script, for the rest of the process; for a test, until `restore()`.
    Call it again to build another variant (the shipped tree is held from the first call). Call before the engine is
    imported."""
    global _held
    held = _evict()
    if _held is None:
        _held = held                       # the first eviction is the shipped tree; a later one is a previous variant's
    return _build(cfg)


def restore():
    """Put the shipped modules back, with the parents' attributes, and drop the variant's. A no-op when none is installed."""
    global _held
    if _held is None:
        return
    saved, attrs = _held
    _held = None
    created = []
    for n in [n for n in sys.modules if _owned(n)]:
        parent_name, _, child = n.rpartition('.')
        created.append((sys.modules.get(parent_name), parent_name, child))
        del sys.modules[n]
    sys.modules.update(saved)
    for parent, parent_name, child in created:
        if parent is not None and parent_name in sys.modules and sys.modules[parent_name] is parent \
                and (parent, child) not in attrs and hasattr(parent, child):
            delattr(parent, child)           # a module the variant imported that the shipped tree never had
    for (parent, child), old in attrs.items():
        if old is _MISSING:
            if hasattr(parent, child):
                delattr(parent, child)
        else:
            setattr(parent, child, old)


@contextlib.contextmanager
def built(cfg):
    """`install(cfg)` for the block, yielding the variant's `config` module (import the rest by name inside the block);
    `restore()` after. Not nestable."""
    install(cfg)
    try:
        yield sys.modules['modules.mass_battle.config']
    finally:
        restore()
