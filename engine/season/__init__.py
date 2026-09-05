"""THE SEASON LOOP — the adopted game code (ED-IN-0202, Jordan 2026-09-05, "adopt in full").

⚠ WHY THIS FILE INSERTS ITS OWN DIRECTORY ON `sys.path`, WHICH IS NOT ORDINARY PACKAGE STYLE.

The modules here import each other by BARE NAME (`import shape`, `import probes`) — a flat
module-set convention carried in from the instrument this package was adopted from, and the same
convention `systems/combat/combat_engine_v1/` uses. Without this insert the package is importable
ONLY by a caller that has already arranged the path, which is how it worked while it lived under
`proposals/` and every entry point did the insert itself.

That stopped being adequate at adoption. `tests/valoria/test_engine_does_not_import_systems.py`
walks EVERY `engine/**/*.py` and imports it by dotted path in a subprocess, to hold the
engine→systems import count at zero. Under that walk `engine.season.corpus_run` raised
`ModuleNotFoundError: shape` and reddened a BLOCKING CI gate — found by an adversarial pass on the
conversion, not by the move itself, which is the §0.1 pt 1 read/write-asymmetry signature: the
importers were fine, the IMPORT CONTEXT changed underneath them.

⚠ THE COST, NAMED RATHER THAN GLOSSED: a module here can now be reached as `shape` AND as
`engine.season.shape`, and those are TWO module objects with two sets of module-level state if a
process loads both. That is the same second-identity hazard `CLAUDE.md` §3 records for
`combat_engine_v1`, and it is accepted here for the same reason — converting 11 modules to dotted
imports would shift every line number, and `hole_register.yaml` cites those files by `:NNN`.
Prefer `engine.season.X` in new callers; the bare form exists for the modules' own siblings.
"""
import sys
from pathlib import Path

_PKG = Path(__file__).resolve().parent
if str(_PKG) not in sys.path:
    sys.path.insert(0, str(_PKG))
