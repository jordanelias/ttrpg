"""`manifest/providers.py` -- the provider TABLE and its decorator, and nothing else.

⚠⚠ **THIS MODULE EXISTS TO BREAK AN IMPORT CYCLE BY CONSTRUCTION, AND THE CYCLE WAS REAL.**
`U1` put `PROVIDERS` and `@provider` in `registry.py`, which also holds `_load_providers()` --
the import of `seam/wrappers/*`. The wrappers import the decorator back, so the edges were

    manifest.registry -> seam.wrappers.sigma -> manifest -> manifest.registry

`registry.py` made its wrapper import LAZY (inside a function) and its own docstring called the
cycle *"genuine"* while relying on laziness to hide it. It did not hide it:
`tests/valoria/test_import_cycle_game_state_npe.py` went from 3 cycles to 4 on the `U1` tree, and
that test's own docstring says why in as many words -- ***"A deferred or bare-named import hides a
cycle from an instrument; it does not remove it."*** Deferring was the wrong repair for a defect
whose statement is structural.

**THE SPLIT IS THE REPAIR: the TABLE is a primitive, the REGISTRY is a policy over it.**
`providers.py` is a LEAF -- it imports nothing from this package and nothing from `seam/` -- so a
wrapper may import the decorator without reaching `registry.py`, and `registry.py` may import the
wrappers without closing a loop. The cycle is gone by construction rather than by an import that
executes late, which is the same distinction `04` draws between an acyclic package and one that
merely defers its edges.

⚠ **`has()` AND `call()` STAY IN `registry.py`, NOT HERE, AND THAT IS DELIBERATE.** Both must first
`_load_providers()`, which is the policy half; a leaf that triggered the wrapper import would be the
cycle again wearing a new filename. This module answers only *what is registered*, never *make sure
everything is registered*.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# THE TABLE. `(role, module) -> callable`. `04 §A.2:136`'s other half: the seam names a ROLE, the
# manifest row names the MODULE, and this is what actually runs it.
# ---------------------------------------------------------------------------
PROVIDERS: dict = {}


def provider(role: str, module: str):
    """Register a callable as the provider for `(role, module)`. `04 §A.2:136`'s other half."""
    def deco(fn):
        PROVIDERS[(str(role), str(module))] = fn
        return fn
    return deco
