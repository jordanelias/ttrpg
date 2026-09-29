"""`season.state.containment` -- THE CONTAINMENT TREE, READ: one edge up, and the subtree down.

⚠ MOVED HERE FROM `queries/world_q.py` BY G3 (plan position 6), BODIES UNCHANGED, AND THE MOVE IS
FORCED BY THE LAYERING RATHER THAN CHOSEN. `04 §C.2`'s F3 clause puts *"via is a Seat whose
`revocation` basis reaches it"* INSIDE THE GATE, and ruling (3)'s rule (`rung_above_same_faction`)
asks for the seat's PARENT rung, while ruling (4)'s purview asks for a seat's SUBTREE. The gate is in
`state/`; `queries/` imports `state/` and never the reverse (`state/__init__.py`, `world.py`'s own
header). So a gate that calls `world_q.parent_of` is an upward import, and a gate that re-derives the
walk is `CLAUDE.md` §8's second copy. The walk moved DOWN instead: `world_q` re-exports these two
names, so `world_q.parent_of is containment.parent_of` and every existing caller (`loop/predicates`,
the probes, the tests) reaches the same function object it always did.

⚠ PRECEDENT, NOT INVENTION: `World.contain_ascends` already lives in `state/` for the same reason --
*"ONE OWNER, TWO POLARITIES"*, the store's writer needs the ladder rule, so the rule lives where the
writer can reach it and the loop calls it from there.

Both read `w.tenures` and nothing else, so this module imports no carrier and no store -- it takes
the `World` it is handed and asks it. `descendants` keeps its `TRACE.query` line verbatim: a caller
that consolidates a walk must not change what the walk traces (`world_q.ancestry`'s docstring
records the red that taught this).
"""

from __future__ import annotations

from typing import Optional

from ..trace_log import TRACE

# NO `World` IMPORT, even under `TYPE_CHECKING`: `world` imports `gate`, which imports this module,
# and the import-cycle instrument counts a guarded import as an edge. The type is named as a string.


def parent_of(w: "World", rung_id: str) -> Optional[str]:
    for t in w.tenures:
        if t.kind == "contain" and t.subject == rung_id and t.live:
            return t.object
    return None


def descendants(w: "World", rung_id: str) -> list[str]:
    """S6.1 -- the CONTAINMENT TREE and only it. S38.1: ITERATIVE, with a visited set --
    the reference graph is cyclic ON PURPOSE and a tree walk hangs on the NORMAL case."""
    TRACE.query("descendants", "resolver")
    out, seen, stack = [], {rung_id}, [rung_id]
    while stack:
        cur = stack.pop()
        for t in w.tenures:
            if t.kind == "contain" and t.object == cur and t.live and t.subject not in seen:
                seen.add(t.subject); out.append(t.subject); stack.append(t.subject)
    return out


# =================================================================================================
# ⚠ `ancestry` AND `home_of` MOVED HERE FROM `queries/world_q.py` AT PLAN POSITION `19` (U7-remit),
# BODIES UNCHANGED, FOR THE REASON `parent_of`/`descendants` MOVED AT G3 AND BY THE SAME ROUTE. The
# write gate's `determination` basis (`state/gate.py::may_determine`) asks whether a judging seat's
# ground contains the PARTY's home -- the bench's containment test (`judging_set`'s, `H-32`), asked of
# the person a determination binds. The gate is in `state/`, which may not import `queries/`; a
# gate re-deriving either walk would be `CLAUDE.md` §8's second copy. So both moved DOWN, and
# `world_q` re-exports them: `world_q.ancestry is containment.ancestry`, `world_q.home_of is
# containment.home_of`, and every existing caller reaches the same function object. `home_of`
# keeps its `TRACE.query` line verbatim and `ancestry` keeps tracing nothing -- a moved walk must
# not change what it traces (`ancestry`'s own docstring records the red that taught this).
# =================================================================================================


def home_of(w: "World") -> dict:
    """`{person id: containing rung id}` for every person with a live `contain` edge.

    ⚠ **THE INVERSE OF `presence`, AND IT EXISTS BECAUSE FOUR SITES HAD ROLLED IT BY HAND.**
    `presence(w, rung)` answers *who is here*; this answers *where is everyone*, which is the
    question `harness/populated.py` (twice — the `by_home`/`home_of` index and `census`),
    `tools/export_npc_roster.py` and `engine/season/tests/test_season_shape.py` were each
    computing with their own copy of `t.kind == "contain" and t.live and t.subject in w.persons`.
    That is load-bearing rather than cosmetic: `export_npc_roster.py --check` detects drift by
    comparing ITS notion of home against the builder's, so the two agreeing by coincidence is the
    whole point of the check, and `census`'s `largest_building` is asserted in the suite. A change
    to what counts as home — a dead tenure, a person with two contain edges — had to land in four
    places with nothing to catch a miss (§8, and the §0.1 pt 5 pattern-defect signature).

    ⚠ LAST WRITE WINS on a person with more than one live `contain`, which `World.add_tenure`
    does not forbid. That is the incumbent behaviour of every site this replaces, preserved
    deliberately rather than quietly tightened here."""
    TRACE.query("home_of", "resolver")
    return {t.subject: t.object for t in w.tenures
            if t.kind == "contain" and t.live and t.subject in w.persons}


def ancestry(w: "World", rung_id: str) -> list[str]:
    """`[rung_id, its parent, ..., the root]` — the containment walk up from a rung.

    ⚠ **IT EXISTS BECAUSE THREE SITES HAD ROLLED IT BY HAND**, which is the same reason and the
    same remedy as `home_of` above. `parent_of` owns ONE EDGE; every caller that wants the CHAIN
    was repeating the identical loop — step, guard with a visited set, stop at the root or on a
    revisit — in `WorldReader._ancestry`, in `conferral_path` (deleted at `18a`), and most
    recently in `harness/governance_spine.census`. §8: the walk is a rule, and a rule lives once.

    ⚠ **THE VISITED SET IS LOAD-BEARING, NOT DEFENSIVE.** `World.add_tenure` enforces strict
    ascent on a `contain` edge, so a well-formed world presents no cycle — but `contain_ascends`
    passes any edge whose endpoints are not both resolvable rungs, so a half-built world can. The
    three hand copies each carried their own guard and agreed; consolidating keeps that agreement
    a property of one function rather than a coincidence of three.

    The start rung is INCLUDED, so `len(ancestry(w, r)) - 1` is its depth and a root returns
    `[root]`. An unknown id returns `[id]` — this reports the containment edges that exist and
    does not assert the rung does.

    ⚠ **IT DOES NOT `TRACE`, AND THAT IS THE EXTRACTION BEING CORRECT RATHER THAN AN OMISSION.**
    The first writing called `TRACE.query("ancestry", "resolver")` like its neighbours, and
    `test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` went red on `TRACE.txt`
    and `results.json`: `conferral_path` traces its own name and would now have traced twice, and
    `WorldReader._ancestry` traced nothing and would have started. A helper extracted to remove
    duplication must be INVISIBLE to its callers -- the moment it emits, consolidating three copies
    becomes a behaviour change, and the callers own their query names."""
    out: list[str] = []
    seen: set[str] = set()
    cur: str | None = rung_id
    while cur is not None and cur not in seen:
        out.append(cur); seen.add(cur)
        cur = parent_of(w, cur)
    return out
