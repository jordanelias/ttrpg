"""`queries/cache.py` -- `04_CODE_ARCHITECTURE.md` §A.2's `queries/cache` row.

> `queries/cache` | barrier indexes: **presence, object-side Tenures, subtree aggregates** | any
> store, **at a barrier only** | -- | --

⚠ **THIS MODULE EXISTS BECAUSE THE PRESENCE INDEX WAS BUILT IDENTICALLY IN TWO PLACES.** Before unit
L3, `epistemic.py` and `loop/driver.py` each carried

    w.cache_at_barrier("presence", lambda: {r: world_q.presence(w, r) for r in w.rungs})

character for character. `CLAUDE.md` §8 is explicit -- *every rule lives once* -- and this is one
rule: WHICH key the index is filed under, WHAT it maps, and the fact that it is legitimate only at a
barrier. Two copies is one edit away from two answers. So the build has a single owner and both
callers ask it.

⚠ **"AT A BARRIER ONLY" IS THE WHOLE OF THE DISCIPLINE, AND IT IS NOT ENFORCED BY THIS MODULE.**
`World.cache_at_barrier` fills on first ask and `World.discard_caches()` empties it at each of
CALENDAR's and MATTER's entries, so a cache built mid-step would survive to the next reader with a
stale answer. What makes the existing calls safe is stated at their sites -- `epistemic.py`'s fan is
built BEFORE `witness` enters its own loop -- and moving the build here does not add a check that
was not there. Said plainly rather than implied: this is a single-owner refactor, not a new guard.

**TWO OF THE THREE INDEXES §A.2 NAMES DO NOT EXIST YET**, and that is the honest state rather than
something this unit invented a stub for: there is no object-side Tenure index and no subtree-aggregate
index in the tree. `world_q.r1_aggregate` and `world_q.single_holder_counter` compute their answers
per call, uncached. When either is cached it belongs here, and the `04` row is why.
"""

from __future__ import annotations

from . import world_q


def presence_index(w) -> dict:
    """The barrier-scoped `rung -> [person ids present]` index, built once per barrier.

    THE SINGLE OWNER of the key, the shape and the build. Both callers -- `epistemic.observers_for`
    and `loop/driver`'s witness fan -- asked `World.cache_at_barrier` with a hand-written lambda
    before L3; the lambdas were identical, which is the duplication `CLAUDE.md` §8 forbids rather
    than a coincidence worth keeping.

    ⚠ NO `World` ANNOTATION, DELIBERATELY. `w` is a `World` and typing it would be honest, but this
    module is imported by `epistemic.py`, which `decision/` imports -- and the AX-2 by-path scan
    resolves every name `decision/` reaches and refuses any that TAKES a `World`, by token, quoted
    forward references included. That check is `04:171` row 2's smuggling route closed by
    derivation, and it is worth more than the annotation. The parameter's identity is stated here
    instead, where a reader meets it.
    """
    return w.cache_at_barrier("presence", lambda: {r: world_q.presence(w, r) for r in w.rungs})
