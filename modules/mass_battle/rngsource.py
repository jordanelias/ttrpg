"""The single owner of randomness for the mass-battle engine.

Every roll draws from `get()`. The property it provides is same seed -> same bytes, so the seeded campaign pins stay
reproducible without an `rng` parameter threaded through every roll site between `roll_pool` and `run_battle`.

PER-CALL STATE, NOT A MODULE GLOBAL (plan position `31c`, AX-4). The source is a CONTEXT VARIABLE: the
module holds the variable, never a value; `using()` sets it for the extent of one block and resets it by
its own token on exit, so a source cannot outlive the call that scoped it, and there is no setter to call
outside a block. The source a block scopes is the CALLER's parameter (`massbattle.resolve_field`'s `rng`).

USE. Callers that own a seed scope it:

    with rngsource.using(rng):
        result = run_battle(unit_a, unit_b)

Outside every block the engine draws from the global `random` module -- the fallback the unscoped callers
(the workbench, `bat.py`'s golden batteries, the engine tests that `random.seed`) rely on.
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
