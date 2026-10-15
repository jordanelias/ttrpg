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

THE OBJECT-SIDE TENURE INDEX (`tenure_index`, IN-54) AND ITS INVALIDATION RULE -- written before the
code, because the rule is what makes the index safe and the code only follows it.

WHAT IT ANSWERS. Two of `epistemic`'s channel predicates asked, per (event, person), a question over
every Tenure in `w.tenures`: `_ch_document_key` *does `pid` hold, live, the thing this change wrote?*
and `_ch_witness_key` *is `pid` knotted, live, to this Event's anchor?* The index files the same
LIVE edges by the end the predicate asks from: `holds[subject] -> {objects}` for `hold`, and
`knots` as the set of `(subject, object)` pairs for `knot`. It holds ids (strings), never a
`Tenure`, so it cannot alias a mutable edge. Only LIVE edges are filed, so a closed Tenure is
absent from the index exactly as `t.live` makes it absent from the scan.

THE RULE. An index answer is valid exactly while `w.tenure_version()` equals the version the index
was built at. The version is a pair -- (`Tenure.writes`, `World._tenure_structure`):

  1. `Tenure.writes` counts every ASSIGNMENT to a field of any Tenure (`state/carriers.py`,
     `Tenure.__setattr__`) -- construction, a close (`t.until = ...`), a renewal, a restore. It is
     the one place a field write can be seen, so no effect needs to remember to bump anything and a
     bare `t.until = ...` in a test or a probe is counted the same.
  2. `World._tenure_structure` counts what `__setattr__` cannot see, a Tenure entering or leaving
     the store without a field changing: `add_tenure`, `_restore_tenures` and `remove_person`.
     (`_rehome` moves a Tenure between two lists inside the store and changes membership of
     `w.tenures` not at all, so it does not count.)

The index is filed in the barrier cache UNDER A KEY THAT CARRIES THE VERSION, so the lookup is the
check: a version that moved is a key the cache has never seen, and the answer is rebuilt from a
fresh scan of `w.tenures` -- the worst case is today's scan, once per version, not once per
(event, person). `World.discard_caches()` still empties it at every step's entry like any other
barrier index; the version is what makes it safe BETWEEN discards. That is the one place it is
needed: `loop/resolve.py` calls `observers_for` mid-RESOLVE, right after its own
`discard_caches()`, and RESOLVE's fold writes Tenures between acts.

WHAT IT DOES NOT COVER, said plainly. A Tenure inserted into or removed from a `Person.tenures`
list by hand (`p.tenures.append(t)`, `p.tenures = [...]`) bypasses `add_tenure`, the store's one
adder, and the index will not see it until a field write or a counted structure change; the
`_unowned` list is the same. Outside `state/world.py` (the store itself, counted) production code has
one such site, a harness probe (`probes.py`, `p42`); the rest are tests that build a world and then
ask. `engine/season/tests/test_in54_tenure_index.py` fails on a new one. A mutation of a Tenure's
`payload` IN PLACE (`payload["x"] = ...`) is not a field assignment and is not counted -- the index
reads no payload. Nor is a person removed by hand outside `remove_person` (`w.persons.pop(...)` at
`harness/probes.py:903`, `del w.persons[...]` at `:1114`), whose Tenures leave `w.tenures` with no
count, nor any slice or `del` surgery on a Tenure list, which the sweep's mutator set does not name.

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
    """The version-keyed `TenureIndex`; the module docstring states the invalidation rule.

    ⚠ NOT FOR `_ch_post_remit` -- `establishment_of` stays a live re-scan (r2 `05` §A.1.5 RULED (d))."""
    return w.cache_at_barrier("tenures@%d.%d" % w.tenure_version(), lambda: _build_tenure_index(w))


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
