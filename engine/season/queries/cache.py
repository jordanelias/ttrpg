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
`World.cache_at_barrier` fills on first ask and `World.discard_caches()` empties it at each loop
step's entry -- `calendar.py`, `matter.py`, `resolve.py` and `witness.py` all call it, not only
CALENDAR's and MATTER's (an earlier wording of this line named two sites and undercounted; four
call sites is the safer state, not a riskier one) -- so a cache built mid-step would survive to the
next reader with a stale answer. What makes the existing calls safe is stated at their sites --
`epistemic.py`'s fan is built BEFORE `witness` enters its own loop -- and moving the build here does
not add a check that was not there. Said plainly rather than implied: this is a single-owner
refactor, not a new guard.

**TWO OF THE THREE INDEXES §A.2 NAMES DO NOT EXIST YET**, and that is the honest state rather than
something this unit invented a stub for: there is no object-side Tenure index and no subtree-aggregate
index in the tree. `world_q.r1_aggregate` and `world_q.single_holder_counter` compute their answers
per call, uncached. When either is cached it belongs here, and the `04` row is why.
"""

from __future__ import annotations

from . import world_q


def presence_index(w: "World") -> dict:
    """The barrier-scoped `rung -> [person ids present]` index, built once per barrier.

    THE SINGLE OWNER of the key, the shape and the build. Both callers -- `epistemic.observers_for`
    and `loop/driver`'s witness fan -- asked `World.cache_at_barrier` with a hand-written lambda
    before L3; the lambdas were identical, which is the duplication `CLAUDE.md` §8 forbids rather
    than a coincidence worth keeping.

    ⚠ AN EARLIER WORDING OF THIS DOCSTRING LEFT `w` UNANNOTATED, on the claim that the AX-2 by-path
    scan over `decision/` would refuse any name it reaches that takes a `World`. That claim was
    false: the scan resolves only the names `decision/` imports directly, and no `decision/` module
    imports `presence_index` (`decision/options.py` imports `epistemic.belief_contradicts`, a
    `Person`-side function, and nothing here). Annotating this parameter trips nothing.
    """
    return w.cache_at_barrier("presence", lambda: {r: world_q.presence(w, r) for r in w.rungs})
