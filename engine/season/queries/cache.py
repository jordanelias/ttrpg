"""`queries/cache.py` -- `04_CODE_ARCHITECTURE.md` §A.2's `queries/cache` row.

> `queries/cache` | barrier indexes: **presence, object-side Tenures, subtree aggregates** | any
> store, **at a barrier only** | -- | --

⚠ **THE PRESENCE INDEX HAS ONE OWNER.** `epistemic.py` and `loop/driver.py` both ask it for

    w.cache_at_barrier("presence", lambda: {r: world_q.presence(w, r) for r in w.rungs})

`CLAUDE.md` §8 is explicit -- *every rule lives once* -- and this is one rule: WHICH key the index is
filed under, WHAT it maps, and the fact that it is legitimate only at a barrier. Two copies is one
edit away from two answers.

⚠ **"AT A BARRIER ONLY" IS THE WHOLE OF THE DISCIPLINE, AND IT IS NOT ENFORCED BY THIS MODULE.**
`World.cache_at_barrier` fills on first ask and `World.discard_caches()` empties it at each loop
step's entry -- `calendar.py`, `matter.py`, `resolve.py` and `witness.py` all call it, not only
CALENDAR's and MATTER's -- so a cache built mid-step would survive to the
next reader with a stale answer. What makes the existing calls safe is stated at their sites --
`epistemic.py`'s fan is built BEFORE `witness` enters its own loop -- and this module adds no
check: it is a single owner, not a guard.

**ONE OF THE THREE INDEXES §A.2 NAMES DOES NOT EXIST**: there is no subtree-aggregate index in the tree.
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

THE LIVE-EDGE VIEW (`parent_of`, `seat_hold`, `_eligible`'s `hold:` branch) is NOT FILED HERE, and the reason
is the layering: those readers are in `state/` and `loop/`, and `state/` may not import `queries/`. Its one
owner is `state/containment.py::edges_of`, which files it under `"live_edges"` in the same
`World.cache_at_barrier` this module uses, with the same lifetime (dropped by `discard_caches()`); unlike
`tenure_index` it holds Tenure OBJECTS (`seat_hold` returns one) and re-checks `t.live` at read, and it is
rebuilt whenever `World.tenure_extent()` changes, because those readers run INSIDE a step, after writes.

NOT `establishment_of`. `_ch_post_remit` keeps a live re-scan (r2 `05` §A.1.5 RULED (d)); the index files `hold` and `knot` and answers nothing about
`oblige`.
"""

from __future__ import annotations

from typing import NamedTuple

from engine.dice_engine.sigma_leverage import levels_to_net_sigma, pool_of

from ..data.rosters import capability_rows, require_use_site, when_holds
from ..state import containment
from ..trace_log import TRACE
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
    and `loop/driver`'s witness fan -- ask it, so the key is written once (`CLAUDE.md` §8).
    """
    def build() -> dict:
        for _ in w.rungs:
            TRACE.query("presence", "resolver")      # the row `world_q.presence` wrote per rung, so the trace is unchanged
        return world_q.presence_map(w)
    return w.cache_at_barrier("presence", build)


def deposit_index(w: "World") -> dict:
    """The barrier-scoped `{Event id: (claim ids deposited from it, in log order)}` map (B09.17), built once per barrier from one
    scan of the log: each `claim.deposited` Event's `causes[0]` is the witnessed Event (`loop/witness.py::_deposit`) and its one
    receipt's subject is the claim. It exists for `epistemic._antecedent_claim`, which asks it per (witness, Event) and so would
    otherwise scan the log each time; it is the look-up through the record the tree already writes, not a second copy of how WITNESS
    mints a claim's id. Holder-blind on purpose (ids only): the caller tests each against the witness's OWN ledger.

    VALID FOR THE SAME REASON AND ONLY WHERE `presence_index` IS: WITNESS asks it BEFORE its own deposits of the barrier (the fan's
    `seen` terms are read ahead of the parallel map), so the log it scanned is the log the question is about; a direct caller that
    deposits between two asks must `w.discard_caches()`. Built only when asked, and `connection_chance` 0.0 never asks."""
    def build() -> dict:
        out: dict = {}
        for ev in w.log:
            if ev.kind == "claim.deposited" and ev.causes and ev.changes:
                out.setdefault(ev.causes[0], []).append(ev.changes[0].subject)
        return {k: tuple(v) for k, v in out.items()}
    return w.cache_at_barrier("deposits", build)


def home_index(w: "World") -> dict:
    """The barrier-scoped `{person id: containing rung id}` map, built once per barrier: `containment.home_of`'s
    map, filed the way `presence_index` is. It exists for WITNESS, whose co-location channel asks
    `place_of` -> `home_of(w)` once per (event, person) pair, each of which would rebuild the whole map from
    every Tenure.

    VALID FOR THE SAME REASON AND ONLY WHERE `presence_index` IS: the barrier is the invalidation
    (`World.discard_caches()` at each step's entry), WITNESS writes no Tenure, and a direct caller that moves a
    person between two asks must `w.discard_caches()` between them. It is NOT a replacement for `home_of(w)`
    at a mid-step reader, which must keep the live scan."""
    return w.cache_at_barrier("homes", lambda: containment.home_map(w))


#: `rosters.yaml: capability_use_sites`' site whose rows name what a bystander brings to seeing a deed (B11.66): its `dice` row the skill his pool is read from, its `edge` row
#: the attribute whose levels shift his roll. Bound through `require_use_site`, so a renamed site refuses at import rather than reading no capability.
NOTICE_SITE = require_use_site("notice")


def notice_pools(w: "World") -> dict:
    """The barrier-scoped `{person id: his pool for noticing a deed}` map (B11.66; `18_DETERMINISM_notice_is_a_draw` edit 2, D-74 B), built once per barrier, for every
    person, from the `notice` site's `dice` row: the one pool rule (`sigma_leverage.pool_of`) on his held rank in the row's skill, `pool_default` where he holds none (an
    untrained witness reads the untrained score, as `pool.score` does) -- the row's own `add:` and `floor:` fixtures through `pool.pool_pair`, `(0, 0)` where it names none.
    It exists so `epistemic.notice`, which runs inside WITNESS, reads a map and computes no pool there (04 §A.2); WITNESS builds it at its entry, beside `presence_index`, and
    only at `notice_arm: on`, so at the control nothing is read.

    VALID FOR THE SAME REASON AND ONLY WHERE `presence_index` IS: the barrier is the invalidation, and nothing WITNESS writes moves a held skill. A direct caller that
    changes a person's skill between two asks must `w.discard_caches()` between them.
    ⚠ `seam.wrappers.pool` is imported at the call, not at module level: `seam/` imports `epistemic`, which imports this module."""
    def build() -> dict:
        from ..seam.wrappers.pool import pool_pair, untrained
        fx = w.fixtures
        row = next(r for r in capability_rows(NOTICE_SITE) if r.role == "dice")
        add, floor = pool_pair(fx, NOTICE_SITE)
        default = untrained(fx)
        return {pid: pool_of(max(default, int(have)) if (have := (p.capability or {}).get(row.key)) is not None else default, 0, add, floor)
                for pid, p in w.persons.items()}
    return w.cache_at_barrier("notice_pools", build)


def notice_edges(w: "World") -> dict:
    """The barrier-scoped `{person id: his net sigma for noticing a deed}` map (B11.66), `notice_pools`' sibling and built beside it for the same reason: the `notice` site's
    `edge` rows (the shipped one keys his Perception, `per: mid`) are selected as the social roll's are (`when_holds`), each read at the value he holds, summed by the ONE `edge`
    reader (`sigma.ADVANTAGE_SOURCES["capability"]`) into named levels and turned into a sigma by `levels_to_net_sigma` -- the reader `loop/resolve.py::_crisis_net_sigma`
    uses for its own site. A person who holds no value reads the scale's mid-point: no step. `0.0` where the site has no `edge` row. Same lifetime and lazy import as `notice_pools`."""
    def build() -> dict:
        from ..seam.wrappers.sigma import ADVANTAGE_SOURCES, CAPABILITY, EDGE
        rows = tuple(r for r in capability_rows(NOTICE_SITE) if r.role == "edge")
        return {pid: levels_to_net_sigma(*ADVANTAGE_SOURCES[CAPABILITY](
                    w.fixtures, {EDGE: tuple((r, r.key, (p.attributes or {}).get(r.key)) for r in rows if when_holds(r, p))}))
                for pid, p in w.persons.items()}
    return w.cache_at_barrier("notice_edges", build)
