"""`loop/encounter.py` -- ENCOUNTER, the SEVENTH season-loop step (M4, `ED-IN-0279` clause (a),
`04 §A.2:134` as amended 2026-09-28). Sits between RESOLVE and WITNESS, sharing barrier 3.

Fights the contests RESOLVE deferred. A verb whose prize row declares `step: ENCOUNTER` is
admitted and DECLARED at RESOLVE -- `loop/resolve.py::_contest` folds it at the row's own
`declares:` band (`Declared`, `field_degree_bands`), writing nothing, because nothing has been
fought yet. This step selects the acts that declaration produced and calls `_contest` again --
now that `w.step` is ENCOUNTER, the SAME deferral check inside `_contest` takes the other branch:
dispatch to the seam, fold at the degree the subsystem's own result decides.

⚠ HOLDS NO STATE BETWEEN STEPS. The declaration is an Event in the round's own list (this step's
one input, alongside what `self.act_of` already maps it to); the act is already in `w.acts`
(RESOLVE appended it before folding). No new carrier, no field, no Tenure kind, no clock -- the
seven ratified Tenure kinds are closed and none of them needed touching to build this.

⚠ SELECTS BY THE DECLARATION EVENT, NEVER BY RE-RUNNING `_admits`. A contest refused at RESOLVE
(ineligible, or its `requires` unmet) has no declaration Event, so it is invisible here BY
CONSTRUCTION -- `_contest`'s own docstring: ENCOUNTER's admission is the ONE RESOLVE already
gave, never re-checked against a world the whole round has since moved. This is load-bearing, not
incidental: `state/log.py::EventLog.append` does not refuse a duplicate Event id, so re-running
admission and re-emitting a refusal here on a contest RESOLVE already refused would risk a SILENT
DOUBLE EMISSION rather than a raise -- the declaration filter is what prevents it ever being
asked, not a second admission gate that would have to agree with the first.

⚠ MINTS NO NEW TOKEN CLASS. `Step.ENCOUNTER` shares RESOLVE's `WriteClass.ACTS` (`data/matrix.py`)
-- two steps sharing a class has precedent twice over already (DELIBERATE/RESOLVE,
CENSUS/MATTER); the STEP, not the class, is what the write matrix's `steps:` column gates on, so
`(Person, body)`/`(Person, stance)` needed their own `ENC` cell regardless (`write_matrix.yaml`).
"""

from __future__ import annotations

from typing import Optional

from .resolve import _canonical_order, _contests_of
from ..data.matrix import Step
from ..data.rosters import DECLARED
from ..data.verbs import VERB_TABLE
from ..state.gate import Token
from ..trace_log import TRACE


def encounter(self, token: Token, events: list,
              contest_max_depth: Optional[int]) -> list:
    """M4's seventh step. `events` is the SAME round's own -- the driver passes what RESOLVE
    just produced, before it is appended to `w.log` (`loop/driver.py::season`), so this step's
    own events join the same fan-out WITNESS sees for the round."""
    w = self.w
    w.step = Step.ENCOUNTER
    TRACE.step("ENCOUNTER", "enter")
    w.discard_caches()
    # THE SELECTION. `self.act_of` is cumulative across the whole season (never reset,
    # `loop/resolve.py`'s own note on why), so this reads only the ACTS THIS ROUND'S EVENTS
    # NAME -- never an earlier round's declaration, which would already have been fought.
    declared: dict = {}
    for e in events:
        if e.degree == DECLARED:
            a = self.act_of.get(e.id)
            if a is not None:
                declared[a.id] = a
    if not declared:
        TRACE.step("ENCOUNTER", "leave")
        return []
    out: list = []
    for a in _canonical_order(w, list(declared.values())):
        gone = self._survives(w, a)
        if gone:
            out.extend(gone)
            continue
        row = VERB_TABLE.get(a.verb)
        contests = _contests_of(a, row)
        produced = self._contest(w, token, a, contests, contest_max_depth)
        for e in produced:
            self.act_of[e.id] = a
        out.extend(produced)
    TRACE.step("ENCOUNTER", "leave")
    return out
