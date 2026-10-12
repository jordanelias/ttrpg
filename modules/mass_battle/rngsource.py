"""The single owner of randomness for the mass-battle engine.

WHY THIS EXISTS. This engine was developed under `tests/sim/mass_battle/` and drew from the GLOBAL
`random` module at seven call sites. The engine it replaced at `systems/mass_battle/sim/` threaded an
explicit `rng` parameter end to end (49 references), because of a documented 2026-05-20 defect:

    "non-determinism 03ce9c79: thread world.rng through run_battle so batch reproducibility no
     longer requires a global random.seed() pin … Pre-fix run_batch results varied between runs at
     the same seed; post-fix, byte-identical at the same seed."

Porting the canon engine over the top WITHOUT restoring that property would not merely move the
seeded campaign goldens — it would make them UNPINNABLE, which is strictly worse: a moved golden is
a measurement, an unreproducible one is the end of measurement. the campaign-driver regression,
`test_f7_smoke_oracle` and `test_parliamentary_bridge` (all since deleted) all depended on same-seed byte-exactness.

WHY A SCOPED SOURCE RATHER THAN A THREADED PARAMETER. The old engine's approach — an `rng=None`
argument on every roll, passed down every call chain — is the more explicit design and it is what the
canon engine would have if it had grown up here. Retrofitting it means touching every caller of
`roll_pool`/`roll_pool_fractional` and every function between them and `run_battle`, in an 11,400-line
tree. This source restores the PROPERTY (same seed -> same bytes) without that, and leaves the
parameter-threading available as a later, separately-verifiable refactor.

PER-CALL STATE, NOT A MODULE GLOBAL (plan position `31c`, AX-4). The source is a CONTEXT VARIABLE: the
module holds the variable, never a value; `using()` sets it for the extent of one block and resets it by
its own token on exit, so a source cannot outlive the call that scoped it, and there is no setter to call
outside a block. The source a block scopes is the CALLER's parameter (`massbattle.resolve_field`'s `rng`).

USE. Callers that own a seed scope it:

    with rngsource.using(rng):
        result = run_battle(unit_a, unit_b)

Outside every block the engine draws from the global `random` module exactly as it did under
`tests/sim/` -- the fallback the unscoped callers (the workbench, `bat.py`'s golden batteries, the
engine tests that `random.seed`) rely on, so every existing test keeps its behaviour.
"""
from __future__ import annotations

import contextlib
import contextvars
import random as _stdlib_random

#: The scoped source. Never read this directly from engine code — call `get()`. Its default, outside
#: every `using()` block, is the stdlib `random` module.
_SCOPED = contextvars.ContextVar('mass_battle_rng', default=_stdlib_random)


def get():
    """The RNG the engine should draw from right now: the innermost `using()` block's, else stdlib `random`."""
    return _SCOPED.get()


@contextlib.contextmanager
def using(rng):
    """Scope an RNG to a block; on exit, even on exception, the source is the one before the block.

    The reset matters: a battle that raised while holding the source would otherwise hand every later
    draw in the process a different stream than its own seed implies. `None` scopes the stdlib module.
    """
    token = _SCOPED.set(rng if rng is not None else _stdlib_random)
    try:
        yield
    finally:
        _SCOPED.reset(token)
