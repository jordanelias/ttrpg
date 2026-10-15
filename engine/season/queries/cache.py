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

**ONE OF THE THREE INDEXES §A.2 NAMES DOES NOT EXIST YET**, and that is the honest state rather than
something this unit invented a stub for: there is no subtree-aggregate index in the tree.
`world_q.r1_aggregate` and `world_q.single_holder_counter` compute their answers per call,
uncached. When either is cached it belongs here, and the `04` row is why.

THE OBJECT-SIDE TENURE INDEX (`tenure_index`, IN-54) AND WHY IT IS VALID.

WHAT IT ANSWERS. Two of `epistemic`'s channel predicates asked, per (event, person), a question over
every Tenure in `w.tenures`: `_ch_document_key` *does `pid` hold, live, the thing this change wrote?*
and `_ch_witness_key` *is `pid` knotted, live, to this Event's anchor?* The index files the same
LIVE edges by the end the predicate asks from: `holds[subject] -> {objects}` for `hold`, and
`knots` as the set of `(subject, object)` pairs for `knot`. It holds ids (strings), never a
`Tenure`, so it cannot alias a mutable edge. Only LIVE edges are filed, so a closed Tenure is
absent from the index exactly as `t.live` makes it absent from the scan.

THE RULE. It is a PER-BARRIER CACHE, keyed exactly as `presence_index` is (`"tenures"` in
`World.cache_at_barrier`), built from one scan of `w.tenures` on the first ask after a barrier and
dropped by `World.discard_caches()`. It is valid because EVERY BARRIER CALLS `discard_caches()`
FIRST -- CALENDAR, ENCOUNTER, MATTER, RESOLVE and WITNESS each do at entry -- so no answer
survives into a step that may have written Tenures since it was built (`04` AX-4: an object-side
index is a barrier cache owned by Nobody; D-34: dropped at the next barrier). The one mid-step
reader in production is `loop/resolve.py`'s scar fan, which calls `observers_for` immediately
after its own `discard_caches()` with no Tenure write between; WITNESS discards at entry and writes
no Tenure. The worst case is the scan this replaced, once per barrier, not once per (event, person).

WHAT IT DOES NOT COVER, said plainly -- THE SAME AS `presence_index`. A direct caller (a test, a
probe) that mutates Tenures between two asks WITHOUT a `w.discard_caches()` between them gets the
answer built before the mutation: stale, exactly as `presence_index` would be after a hand-moved
`contain`. Such a caller must discard. Carriers hold no counter and no behaviour for this (`04`
T-i, D-21): the barrier is the invalidation, and nothing else is.

NOT `establishment_of`. `_ch_post_remit` keeps a live re-scan: caching that Query was tried and
reverted (r2 `05` §A.1.5 RULED (d)); the index files `hold` and `knot` and answers nothing about
`oblige`.
"""

from __future__ import annotations

from typing import NamedTuple

from . import world_q


class TenureIndex(NamedTuple):
    """`holds`: `{subject: frozenset(objects)}` over live `hold` Tenures. `knots`: `frozenset` of
    `(subject, object)` over live `knot` Tenures. Ids only -- see the module docstring."""
    holds: dict
    knots: frozenset


def tenure_index(w: "World") -> TenureIndex:
    """The barrier-scoped `TenureIndex`, built once per barrier; the module docstring states why
    that is valid and what a direct caller must do (discard between a Tenure write and the next ask).

    ⚠ NOT FOR `_ch_post_remit` -- `establishment_of` stays a live re-scan (r2 `05` §A.1.5 RULED (d))."""
    return w.cache_at_barrier("tenures", lambda: _build_tenure_index(w))


def _build_tenure_index(w: "World") -> TenureIndex:
    holds: dict = {}
    knots = set()
    for t in w.tenures:
        if not t.live:
            continue
        if t.kind == "hold":
            holds.setdefault(t.subject, set()).add(t.object)
        elif t.kind == "knot":
            knots.add((t.subject, t.object))
    return TenureIndex({s: frozenset(o) for s, o in holds.items()}, frozenset(knots))


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
