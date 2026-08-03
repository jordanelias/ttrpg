"""Single owner of the structure_audit loader (ED-IN-0123).

`skills/valoria-vector-audit/scripts/structure_audit.py` is a SCRIPT, not a package module, so
every test that wants it has to load it by explicit path with importlib. Three files had each
written that loader out: `test_structure_audit.py` as `_load`, `test_import_cycle_game_state_npe.py`
and `test_oi12_orphan_census.py` as `_load_structure_audit`. The third copy's own docstring claimed
it was "reused rather than re-implemented, per CLAUDE.md §8" — it was re-implemented, and the claim
went unchallenged because the copies sat in different files and nothing compared them. The
duplicated-helper ratchet in `tools/build_test_register.py` surfaced it the moment the third landed
in the same tree.

Cached, because exec_module is not free and three suites call it.
"""
from __future__ import annotations

import importlib.util
import os

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'structure_audit.py')

_cached = None


def load():
    """Return the structure_audit module, loaded by explicit path."""
    global _cached
    if _cached is None:
        spec = importlib.util.spec_from_file_location('structure_audit', SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _cached = mod
    return _cached
