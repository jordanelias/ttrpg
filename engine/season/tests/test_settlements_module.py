"""v9 IN-07: THE `settlements` MODULE IMPORTS ONLY THE RECORD TYPES (A-25), observed in a fresh interpreter.

`modules/**` is the port's input set (`tests/valoria/test_modules_reachable_closure.py`), and that scan
records a file under `engine/` as reached without walking it, so a settlements entry that later imported
`world_q` or `World` would stay green there. The four sibling modules each carry this probe
(`test_social_contest_module.py`, `test_combat_module.py`, `test_mass_battle_module.py`,
`test_fi03_trail.py`); this is settlements', one interpreter for all its entries.
"""
from __future__ import annotations

from engine.substrate import composition

from ._fresh_process import probe

_IMPORT_PROBE = """
import importlib, os, sys
before = set(sys.modules)
for t in {target!r}.split(","):
    mod_name, attr = t.split(":", 1)
    getattr(importlib.import_module(mod_name), attr)
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
print(repr(loaded))
"""


def test_the_settlements_entries_import_only_the_record_types_in_a_fresh_process():
    """Every composition row whose target is under `modules.settlements.` is imported as the registrar
    reaches it. The repository files that loaded are the package `__init__`s on the way, the record leaf
    `engine/season/queries/inputs.py` and the module's own directory: nothing of the host."""
    targets = sorted(row["target"] for row in composition.ROLES.values()
                     if row["target"].startswith("modules.settlements."))
    assert len(targets) >= 8, f"the settlements module's entry rows are gone from the composition: {targets}"
    loaded = probe(_IMPORT_PROBE, ",".join(targets), 300)
    allowed = {"engine/__init__.py", "engine/season/__init__.py", "engine/season/queries/__init__.py",
               "engine/season/queries/inputs.py", "modules/__init__.py"}
    stray = [f for f in loaded if f not in allowed and not f.startswith("modules/settlements/")]
    assert not stray, f"a settlements entry loaded host code: {stray}"
    assert "engine/season/queries/inputs.py" in loaded and any(
        f.startswith("modules/settlements/") for f in loaded), loaded
