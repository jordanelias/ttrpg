"""The single owner of randomness for the mass-battle engine.

Every roll draws from `get()`. The property it provides is same key -> same bytes, so the seeded campaign pins stay
reproducible without an `rng` parameter threaded through every roll site between `roll_pool` and `run_battle`.

PER-CALL STATE, NOT A MODULE GLOBAL (plan position `31c`, AX-4). The source is a CONTEXT VARIABLE: the
module holds the variable, never a value; `using()` sets it for the extent of one block and resets it by
its own token on exit, so a source cannot outlive the call that scoped it, and there is no setter to call
outside a block. The source a block scopes is the CALLER's parameter (`massbattle.resolve_field`'s `rng`).

USE. Callers that own a seed scope it:

    with rngsource.using(rng):
        result = run_battle(unit_a, unit_b)

THE SOURCE IS REQUIRED. There is no default: `get()` outside every block raises `LookupError` naming this module, and
`using(None)` raises the same, so a draw never falls back to the global `random` module or to a fresh unseeded stream.
A caller that owns no `Draw` builds one (`draw.seeded(draw.H2("<module>", seed))`) and scopes it. The source a block
scopes is a `Draw` (`engine/dice_engine/draw.py`): the method names the engine calls on it are that class's.
"""
from __future__ import annotations

import contextlib
import contextvars

#: The scoped source. Never read this directly from engine code — call `get()`. It has no default: outside
#: every `using()` block there is no source.
_SCOPED = contextvars.ContextVar('mass_battle_rng')


def get():
    """The `Draw` the engine should draw from right now: the innermost `using()` block's. Outside every block there
    is none, and this raises `LookupError` rather than drawing from anywhere else."""
    try:
        return _SCOPED.get()
    except LookupError:
        raise LookupError("modules.mass_battle.rngsource: no draw source is scoped; a mass-battle draw outside a "
                          "`using(draw.seeded(...))` block is refused, never a global or fresh stream") from None


@contextlib.contextmanager
def using(rng):
    """Scope an RNG to a block; on exit, even on exception, the source is the one before the block.

    The reset matters: a battle that raised while holding the source would otherwise hand every later
    draw in the process a different stream than its own seed implies. `None` raises the same `LookupError` as an
    unscoped `get()`: a block with no source is no block.
    """
    if rng is None:
        raise LookupError("modules.mass_battle.rngsource.using(None): a block needs a draw source, and there is "
                          "no default to fall back to")
    token = _SCOPED.set(rng)
    try:
        yield
    finally:
        _SCOPED.reset(token)
