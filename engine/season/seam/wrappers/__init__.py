"""`seam/wrappers/` -- `04_CODE_ARCHITECTURE.md` §A.2 (the line *"one wrapper per deferred subsystem"* was amended there), and
the §A.2 table's row for them is the shortest in the document: they own **"nothing, ever"**, they
read the projection, and they emit a `Margin`.

Three wrappers: `combat.py`, the IN-side of the personal-combat call `seam/contest.py` dispatches
to; `sigma.py`, the social contest scene's provider (`social_contest`, `ED-SC-0037`);
and `mass_battle.py` (`ED-IN-0279`). A fourth, under a
second role: `fieldwork.py`, `@provider("inquiry", "fieldwork")` (v9 FI-02 + FI-03, `SM-3`) -- not a
contest provider; its own docstring adjudicates the §A.2 row it deviates from.
⚠⚠ **THIS PACKAGE IMPORTS ITS OWN WRAPPERS, AND THAT IS WHAT REGISTERS THEM.** The manifest
importing `seam/wrappers/*` would be an import cycle: the wrappers import the `@provider` decorator
back, and `combat.py` reaches `...decision`, which reaches `state/world.py`, whose
`boot()` imports `..manifest`:

    manifest.registry -> seam.wrappers.combat -> decision -> ... -> state.world
                      -> manifest -> manifest.registry

A lazy import hides a cycle from the interpreter, not from the instrument:
`tests/valoria/test_import_cycle_game_state_npe.py` says why -- *"A deferred or bare-named import hides
a cycle from an instrument; it does not remove it."*

**THE MANIFEST OWNS ROWS (data), THE SEAM OWNS PROVIDERS (code).** A manifest importing seam code is the
inversion; a seam importing its own wrappers is a package importing its own modules. Nothing in the
`decision -> queries -> state` chain imports `seam/`, so this edge closes no loop. Both
`loop/driver.py` and `loop/resolve.py` import `..seam`, so by the time `SeasonDriver` construction
asks `manifest.has(...)` (`check_contest_prizes`) or `contest()` dispatches, every
provider is registered.


⚠ **A WRAPPER'S IMPORTS STAY RELATIVE.** `tests/valoria/test_engine_does_not_import_systems.py`'s
`_relative_module_files` follows relative imports only, so an absolute import here makes the
declared `sys.path` seam invisible to the scan that bounds it.
"""

# Importing them IS the registration: each module carries `@provider(role, module)` on its
# `resolve`. Order is irrelevant -- the decorator only writes one dict entry.
from . import combat as _combat            # noqa: F401,E402
from . import sigma as _sigma              # noqa: F401,E402
from . import mass_battle as _mass_battle  # noqa: F401,E402
# The `inquiry` role's provider, the fieldwork scene's adapter (v9 FI-02 + FI-03, `SM-3`).
from . import fieldwork as _fieldwork      # noqa: F401,E402
