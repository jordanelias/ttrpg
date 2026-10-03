"""`seam/wrappers/` -- `04_CODE_ARCHITECTURE.md` §A.2: *"one wrapper per deferred subsystem"*, and
the §A.2 table's row for them is the shortest in the document: they own **"nothing, ever"**, they
read the projection, and they emit a `Margin`.

Three wrappers: `combat.py`, the IN-side of the personal-combat call `seam/contest.py` dispatches
to; `sigma.py`, the interim social provider `ED-SC-0037` rules (`engine/dice_engine/sigma_leverage.py`);
and `mass_battle.py`, wired M3 of the `mc_v18`-retirement plan (`ED-IN-0279`) -- `rosters.yaml`'s
"a field" row now has a `provider:`, closing the gap this docstring used to describe.
⚠⚠ **THIS PACKAGE IMPORTS ITS OWN WRAPPERS, AND THAT IS WHAT REGISTERS THEM.
`manifest/registry.py` USED TO, AND IT WAS AN IMPORT CYCLE.** `U1` had
`registry._load_providers()` import `seam/wrappers/*` so `@provider` would run; the wrappers import
the decorator back, and `combat.py` reaches `...decision`, which reaches `state/world.py`, whose
`boot()` imports `..manifest`. The loop closed:

    manifest.registry -> seam.wrappers.combat -> decision -> ... -> state.world
                      -> manifest -> manifest.registry

`registry.py` made that import LAZY and its own docstring called the cycle *"genuine"*. Laziness
hides a cycle from the interpreter, not from the instrument:
`tests/valoria/test_import_cycle_game_state_npe.py` counted 3 cycles before `U1` and 4 after, and
that test says why in its own words -- *"A deferred or bare-named import hides a cycle from an
instrument; it does not remove it."*

**THE LAYERING WAS INVERTED AND THE CUT RESTORES IT: the manifest owns ROWS (data), the seam owns
PROVIDERS (code).** A manifest importing seam code is the inversion; a seam importing its own
wrappers is a package importing its own modules. Nothing in the `decision -> queries -> state`
chain imports `seam/` -- checked by grep, not assumed -- so this edge closes no loop. Both
`loop/driver.py` and `loop/resolve.py` import `..seam`, so by the time `resolvable_verbs()` asks
`manifest.has(...)` or `contest()` dispatches, both providers are registered.


⚠ **A WRAPPER'S IMPORTS STAY RELATIVE.** `tests/valoria/test_engine_does_not_import_systems.py`'s
`_relative_module_files` follows relative imports only, so an absolute import here makes the
declared `sys.path` seam invisible to the scan that bounds it.
"""

# Importing them IS the registration: each module carries `@provider(role, module)` on its
# `resolve`. Order is irrelevant -- the decorator only writes one dict entry.
from . import combat as _combat            # noqa: F401,E402
from . import sigma as _sigma              # noqa: F401,E402
from . import mass_battle as _mass_battle  # noqa: F401,E402
