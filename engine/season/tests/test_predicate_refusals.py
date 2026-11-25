"""06_FA_hygiene item 2 -- A REFUSAL OF `confer` OR `establish` NAMES ITS CLAUSE.

`_req_release` and `_req_revoke` route each refusal through `loop/predicates.py::_refuse`, which leaves
`"<clause> -> <ids>"` in the trace (a DECISION row, `chose="refuse"`). `_req_confer` and `_req_establish`
returned a bare `False` at each clause, so the fold's own row said THAT a precondition failed and
nothing said WHICH.

THE OBSERVATION: the two predicates are wrapped as the fold looks them up (`REQUIRES_PREDICATES`), over a
populated realm for one season; every call that answers `False` must have written, during that call, a
DECISION row whose clause is non-empty. `checked` counts the refusals seen, and the test asserts that it
saw some -- a loop that asserts conditionally must assert that it asserted (`CLAUDE.md` §0.1 pt 2).
"""

from __future__ import annotations

import pytest
from collections import Counter

from ..boot.realm import build_realm
from ..harness.populated import run
from ..loop.predicates import REQUIRES_PREDICATES
from ..state.carriers import Act
from ..trace_log import TRACE

@pytest.fixture(autouse=True)
def _recording():
    """`TRACE` keeps rows only inside a window an instrument opens; these tests read them."""
    with TRACE.recording():
        yield


VERBS = ("confer", "establish")


def test_every_confer_and_establish_refusal_names_a_clause(monkeypatch):
    checked: Counter = Counter()
    unnamed: list = []
    for verb in VERBS:
        inner = REQUIRES_PREDICATES[verb]

        def wrapped(w, a, _inner=inner, _verb=verb):
            start = len(TRACE.rows)
            answer = _inner(w, a)
            if not answer:                   # B09.19: `Answer(False, clause)` for these two, a bare `False` before it
                checked[_verb] += 1
                clauses = [r.what.split(" -> ")[0].strip() for r in TRACE.rows[start:]
                           if r.channel == "DECISION" and r.detail.get("chose") == "refuse"]
                if not any(clauses):
                    unnamed.append((_verb, a.actor))
            return answer

        wrapped.clauses = inner.clauses      # B21.80: `confer`'s row is keyed, admitted only while the predicate declares its keys
        monkeypatch.setitem(REQUIRES_PREDICATES, verb, wrapped)

    w = build_realm(0)
    run(1, 0, w=w)

    # A season of the realm refuses `establish` and not `confer`, so `confer` is asked directly, once, by
    # the same wrapped predicate: an act naming an office the world does not hold.
    REQUIRES_PREDICATES["confer"](w, Act("a_probe", next(iter(w.persons)), "confer",
                                         payload={"office": "no_such_office"}))
    assert checked["confer"] >= 1, "the confer probe was not refused: the confer arm observed nothing"
    assert sum(checked.values()) >= 1, "no confer or establish refusal occurred: the loop observed nothing"
    assert not unnamed, f"{len(unnamed)} refusal(s) wrote no clause row: {unnamed[:5]} (checked {dict(checked)})"
