"""`seam/wrappers/_estimate.py` -- THE SAMPLER A PROVIDER'S ODDS ESTIMATE SHARES (CP-T03-05, CP-T04-08).

Two providers estimate the odds of the act they deal by SAMPLING their own module entry on a private rng: personal
combat (`combat.py::fight_estimate`) and mass battle (`mass_battle.py::field_estimate`). What is the same between them,
and so lives once here, is HOW MANY samples (the `estimate_samples` fixture, `H-251`) and WHICH STREAM (the key
`(world_seed, tick, actor, "estimate")`). What is sampled and how a sample is read is each provider's, and neither
copies the other's.

⚠ THE RNG IS PRIVATE AND IS NOT A SEASON DRAW. It is built from `H(...)` and never from `w.new_draw()` or the driver's
generator, so an estimate reads `World` and writes nothing, and asking twice in a tick shows one figure.

A LEAF, as `_entry.py` is: `gaps` and `state.ids` only, so no import here closes a loop into the seam."""
from __future__ import annotations

import random
from typing import Any

from ...gaps import Forbidden
from ...state.ids import draw_factory


def samples_of(w: Any) -> int:
    """`estimate_samples`, the number of scenes an estimate runs: a whole number of at least 1 or a refusal naming the
    fixture (a sampler of no scenes has no shares, and shares of a fraction of one are not shares)."""
    n = w.fixtures.get("estimate_samples")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise Forbidden(f"`estimate_samples` must be a whole number of at least 1; got {n!r}",
                        "H-251", law="a sampler of no fights has no shares, and shares of a fraction of one are not shares")
    return n


def rng_of(w: Any, actor: str) -> random.Random:
    """The estimate's private stream, keyed `(world_seed, tick, actor, "estimate")`: `state.ids.draw_factory`'s one
    seeding rule, read at the call's tick."""
    return draw_factory(w.world_seed, lambda: w.tick)(actor, "estimate")
