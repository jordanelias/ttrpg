"""engine.substrate.pc_engine — THE ONE PATH SEAM into modules/combat/ (the personal-combat engine).

Status: [live, 2026-09-25]. Declared in
tests/valoria/test_engine_does_not_import_systems.py::PATH_SEAM_ALLOWED (shrink-only); this file is
its single entry. Plan position `31b` moved the engine's reachable set (the import closure of `wrapper`
and `combatant`) from systems/combat/combat_engine_v1/ to modules/combat/, flat names kept
(references/restructure_ledger.md); workbench/ and the unreached files stayed. It is a FLAT module
set whose modules bare-import each other (wrapper.py:4), so it cannot be imported as
`modules.combat.wrapper` without giving `wrapper`/`combatant`
a second identity in any process that also loads them flat (the balance workbench does). Its two
former loaders — engine/cross_scale/combat_bridge.py::_load_engine and
engine/season/seam/wrappers/combat.py::engine — each spelled this path and this insert, and returned
the two modules in OPPOSITE tuple orders. One spelling, one insert, named fields.

FAILURE MODE: RAISES, on first use. A loader that swallows an import error is the silent-green
failure engine/season/data/files.py names; composition.require raises on a missing role for the same
reason. A caller whose own contract is a typed refusal (04 §A.2 seam/contest: "returns Events +
degree, or a typed refusal") translates the raise at the seam — see seam/wrappers/combat.py::engine.
The path is hand-transcribed from references/module_contracts.yaml combat.sim_module (the contract
was named personal_combat until plan position 30)
(CLAUDE.md §5's live drift risk, now in one place instead of two). IT IS A LEAF: stdlib only;
`import engine.substrate.pc_engine` mutates nothing (no sys.path change until load()).
"""
from __future__ import annotations

import importlib
import os
import sys
from types import ModuleType
from typing import NamedTuple, Optional

_HERE = os.path.dirname(os.path.abspath(__file__))
PC_ENGINE_DIR = os.path.normpath(os.path.join(_HERE, '..', '..', 'modules', 'combat'))


class PCEngine(NamedTuple):
    wrapper: ModuleType
    combatant: ModuleType


_LOADED: Optional[PCEngine] = None


def load() -> PCEngine:
    """The flat module set, by name. Raises FileNotFoundError (dir absent) or ModuleNotFoundError."""
    global _LOADED
    if _LOADED is None:
        if not os.path.isdir(PC_ENGINE_DIR):
            raise FileNotFoundError(f"the personal-combat engine not found at {PC_ENGINE_DIR}")
        if PC_ENGINE_DIR not in sys.path:
            sys.path.insert(0, PC_ENGINE_DIR)
        _LOADED = PCEngine(importlib.import_module('wrapper'), importlib.import_module('combatant'))
    return _LOADED
