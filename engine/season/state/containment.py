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
