"""`season.state.containment` -- THE CONTAINMENT TREE, READ: one edge up, and the subtree down.

⚠ THE WALK LIVES IN `state/` AND NOT IN `queries/`, BY THE LAYERING. `04 §C.2`'s F3 clause puts
*"via is a Seat whose `revocation` basis reaches it"* INSIDE THE GATE, and ruling (3)'s rule
(`rung_above_same_faction`) asks for the seat's PARENT rung, while ruling (4)'s purview asks for a
seat's SUBTREE. The gate is in `state/`; `queries/` imports `state/` and never the reverse
(`state/__init__.py`, `world.py`'s own header). So a gate that calls `world_q.parent_of` is an
upward import, and a gate that re-derives the walk is `CLAUDE.md` §8's second copy. `world_q`
re-exports these two names, so `world_q.parent_of is containment.parent_of` and every caller
(`loop/predicates`, the probes, the tests) reaches the same function object.

⚠ PRECEDENT, NOT INVENTION: `World.contain_ascends` lives in `state/` for the same reason --
*"ONE OWNER, TWO POLARITIES"*, the store's writer needs the ladder rule, so the rule lives where the
writer can reach it and the loop calls it from there.

Both read `w.tenures` and nothing else, so this module imports no carrier and no store -- it takes
the `World` it is handed and asks it. `descendants` traces `TRACE.query`: a consolidated walk must
not change what the walk traces.
"""

from __future__ import annotations

from typing import Optional

from ..trace_log import TRACE

# NO `World` IMPORT, even under `TYPE_CHECKING`: `world` imports `gate`, which imports this module,
# and the import-cycle instrument counts a guarded import as an edge. The type is named as a string.


class _LiveEdges:
    """The barrier's view of the Tenures a hot reader asks by `(kind, subject)`: Tenure OBJECTS, in
    `w.tenures` order, for the kinds in `_VIEWED`. Objects, not ids, because `seat_hold` returns the
    Tenure; so a reader re-asks `t.live` / `t.until` of the object it is handed, and a Tenure closed
    since the view was built reads as closed. What the view cannot see is a Tenure ADDED or REMOVED, which
    `stamp` (`World.tenure_extent`) catches: `edges_of` rebuilds on a changed stamp."""
    __slots__ = ("stamp", "by")

    def __init__(self) -> None:
        self.stamp = None
        self.by: dict = {}


_VIEWED = ("hold", "contain")


def edges_of(w: "World", kind: str, subject: str) -> list:
    """Every `kind` Tenure of `subject` (live or closed), in `w.tenures` order; the caller filters.

    From the barrier's cache (`World.cache_at_barrier`, key `"live_edges"`, dropped by `discard_caches`
    like every barrier index) where one may be built: `parent_of`, `seat_hold` and `_eligible` read this
    inside loops, and each asked `w.tenures`, which sorts and concatenates the whole store per call. Where
    none may be -- inside a parallel map, which refuses the cache even to read -- or for a kind the view
    does not carry, the answer is the same scan of `w.tenures` those readers made, so the two routes agree.

    This lives in `state/` and not in `queries/cache.py` because `state/` may not import `queries/`
    (`gate.py` is a reader); the key and the shape have this one owner."""
    if kind in _VIEWED and not w.in_parallel_map:
        view = w.cache_at_barrier("live_edges", _LiveEdges)
        stamp = w.tenure_extent()
        if view.stamp != stamp:
            by: dict = {}
            for t in w.tenures:
                if t.kind in _VIEWED:
                    by.setdefault((t.kind, t.subject), []).append(t)
            view.by, view.stamp = by, stamp
        return view.by.get((kind, subject), [])
    return [t for t in w.tenures if t.kind == kind and t.subject == subject]


def parent_of(w: "World", rung_id: str) -> Optional[str]:
    for t in edges_of(w, "contain", rung_id):
        if t.live:
            return t.object
    return None


def descendants(w: "World", rung_id: str) -> list[str]:
    """S6.1 -- the CONTAINMENT TREE and only it. S38.1: ITERATIVE, with a visited set --
    the reference graph is cyclic ON PURPOSE and a tree walk hangs on the NORMAL case."""
    TRACE.query("descendants", "resolver")
    # One read of the store: each object's live `contain` subjects, in Tenure order -- the order a
    # per-node scan of `w.tenures` visits them in, so the walk's output is unchanged.
    children: dict = {}
    for t in w.tenures:
        if t.kind == "contain" and t.live:
            children.setdefault(t.object, []).append(t.subject)
    out, seen, stack = [], {rung_id}, [rung_id]
    while stack:
        cur = stack.pop()
        for sub in children.get(cur, ()):
            if sub not in seen:
                seen.add(sub); out.append(sub); stack.append(sub)
    return out


# =================================================================================================
# ⚠ `ancestry` AND `home_of` ARE HERE FOR THE REASON `parent_of`/`descendants` ARE, AND BY THE SAME
# ROUTE. The write gate's `determination` basis (`state/gate.py::may_determine`) asks whether a
# judging seat's ground contains the PARTY's home -- the bench's containment test (`judging_set`'s,
# `H-32`), asked of the person a determination binds. The gate is in `state/`, which may not import
# `queries/`; a gate re-deriving either walk would be `CLAUDE.md` §8's second copy. `world_q`
# re-exports them: `world_q.ancestry is containment.ancestry`, `world_q.home_of is
# containment.home_of`. `home_of` traces `TRACE.query` and `ancestry` traces nothing -- a shared walk
# must not change what it traces (`ancestry`'s own docstring says why).
# =================================================================================================


def home_of(w: "World") -> dict:
    """`{person id: containing rung id}` for every person with a live `contain` edge.

    ⚠ **THE INVERSE OF `presence`.** `presence(w, rung)` answers *who is here*; this answers *where
    is everyone*, the question `harness/populated.py::census`, `tools/export_npc_roster.py` and
    `engine/season/tests/test_season_shape.py` each ask. That is load-bearing rather than cosmetic:
    `export_npc_roster.py --check` detects drift by comparing ITS notion of home against the
    builder's, and `census`'s `largest_building` is asserted in the suite. A change to what counts as
    home — a dead tenure, a person with two contain edges — lands in one place (§8, and the §0.1 pt 5
    pattern-defect signature).

    ⚠ LAST WRITE WINS on a person with more than one live `contain`, which `World.add_tenure`
    does not forbid. That is the behaviour every reader of this map relies on; it is deliberately
    not tightened here."""
    TRACE.query("home_of", "resolver")
    return home_map(w)


def home_map(w: "World") -> dict:
    """`home_of`'s map WITHOUT its trace row: the one place the rule lives, read by `home_of` (which traces) and
    by `queries/cache.py::home_index` (the barrier-scoped copy, whose readers trace per read instead, so the
    row stream is the one `home_of` per call wrote). Same last-write-wins as `home_of`."""
    return {t.subject: t.object for t in w.tenures
            if t.kind == "contain" and t.live and t.subject in w.persons}


def ancestry(w: "World", rung_id: str) -> list[str]:
    """`[rung_id, its parent, ..., the root]` — the containment walk up from a rung.

    ⚠ **ONE OWNER OF THE CHAIN.** `parent_of` owns ONE EDGE; every caller that wants the CHAIN asks this
    loop -- step, guard with a visited set, stop at the root or on a revisit. §8: the walk is a rule,
    and a rule lives once.

    ⚠ **THE VISITED SET IS LOAD-BEARING, NOT DEFENSIVE.** `World.add_tenure` enforces strict
    ascent on a `contain` edge, so a well-formed world presents no cycle — but `contain_ascends`
    passes any edge whose endpoints are not both resolvable rungs, so a half-built world can.

    The start rung is INCLUDED, so `len(ancestry(w, r)) - 1` is its depth and a root returns
    `[root]`. An unknown id returns `[id]` — this reports the containment edges that exist and
    does not assert the rung does.

    ⚠ **IT DOES NOT `TRACE`.** A shared helper must be INVISIBLE to its callers: the moment it emits,
    consolidating copies becomes a behaviour change (`TRACE.txt` and `results.json` would move), and
    the callers own their query names."""
    out: list[str] = []
    seen: set[str] = set()
    cur: str | None = rung_id
    while cur is not None and cur not in seen:
        out.append(cur); seen.add(cur)
        cur = parent_of(w, cur)
    return out
