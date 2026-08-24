"""The single owner of randomness for the mass-battle engine.

WHY THIS EXISTS. This engine was developed under `tests/sim/mass_battle/` and drew from the GLOBAL
`random` module at seven call sites. The engine it replaced at `systems/mass_battle/sim/` threaded an
explicit `rng` parameter end to end (49 references), because of a documented 2026-05-20 defect:

    "non-determinism 03ce9c79: thread world.rng through run_battle so batch reproducibility no
     longer requires a global random.seed() pin … Pre-fix run_batch results varied between runs at
     the same seed; post-fix, byte-identical at the same seed."

Porting the canon engine over the top WITHOUT restoring that property would not merely move the
seeded campaign goldens — it would make them UNPINNABLE, which is strictly worse: a moved golden is
a measurement, an unreproducible one is the end of measurement. `engine/tests/test_mc_v18_regression`,
`test_f7_smoke_oracle` and `test_parliamentary_bridge` all depend on same-seed byte-exactness.

WHY A MODULE-LEVEL HOLDER RATHER THAN A THREADED PARAMETER. The old engine's approach — an `rng=None`
argument on every roll, passed down every call chain — is the more explicit design and it is what the
canon engine would have if it had grown up here. Retrofitting it means touching every caller of
`roll_pool`/`roll_pool_fractional` and every function between them and `run_battle`, in an 11,400-line
tree, in the same commit that moves that tree. That is two risky changes wearing one commit message.
This holder restores the PROPERTY (same seed -> same bytes) with a seven-line diff, and leaves the
parameter-threading available as a later, separately-verifiable refactor.

USE. Callers that own a seed set it and restore it:

    with rngsource.using(world.rng):
        result = run_battle(unit_a, unit_b)

Nothing inside the engine calls `set()`. If nobody sets one, the engine draws from the global
`random` module exactly as it did under `tests/sim/`, so every existing test keeps its behaviour.
"""
from __future__ import annotations

import contextlib
import random as _stdlib_random

#: The active source. Never read this directly from engine code — call `get()`, so a caller's
#: `using()` block is always honoured.
_active = _stdlib_random


def get():
    """The RNG the engine should draw from right now."""
    return _active


def set(rng):  # noqa: A001 - deliberate: this module IS the setter
    """Point the engine at `rng`. `None` restores the global `random` module."""
    global _active
    _active = rng if rng is not None else _stdlib_random
    return _active


@contextlib.contextmanager
def using(rng):
    """Scope an RNG to a block and restore the previous one, even on exception.

    The restore matters: `resolve_mass_battle` runs inside a campaign that owns `world.rng`, and a
    battle that raised while holding the source would silently hand the rest of the campaign a
    different stream than the seed implies.
    """
    previous = _active
    try:
        yield set(rng)
    finally:
        set(previous)
