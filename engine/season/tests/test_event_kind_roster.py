"""B03.57 -- THE LOG ACCEPTS ONLY DECLARED EVENT KINDS (`04` §B.13 loader invariant 7: *"the Event-kind
roster is derived from every emission column, and the log accepts no other kind"*).

`EventLog.append` takes the roster (`data/verbs.py::EVENT_KINDS`, handed in by `World`) and refuses a kind
outside it. Before this, the roster was enforced only where the fold builds an Event
(`loop/resolve.py::_act_events`), so `loop/matter.py`'s direct appends and every probe's were unchecked.
"""
from __future__ import annotations

import pytest

from ..data.verbs import EVENT_KINDS
from ..gaps import Forbidden
from ..boot.realm import build_realm
from ..harness.populated import run
from ..state.carriers import Event
from ..state.ids import ROOT
from ..state.world import World


def _ev(kind: str, eid: str = "ev.test") -> Event:
    return Event(id=eid, kind=kind, changes=[], causes=[ROOT], emitted_at=0)


def test_planted_undeclared_kind_is_refused_at_append():
    w = World(0)
    assert "zz.undeclared" not in EVENT_KINDS, "the planted kind must really be outside the roster"
    with pytest.raises(Forbidden, match=r"zz\.undeclared"):
        w.log.append(_ev("zz.undeclared"))
    assert len(w.log) == 0, "a refused Event is not logged"
    # control: a declared kind is accepted, and a test kind declared through the roster parameter is too
    w.log.append(_ev(sorted(EVENT_KINDS)[0], "ev.declared"))
    w2 = World(0, event_kinds=EVENT_KINDS | {"zz.undeclared"})
    w2.log.append(_ev("zz.undeclared"))
    assert [e.kind for e in w2.log] == ["zz.undeclared"]


def test_every_shipped_matter_kind_is_accepted():
    """One season at seed 0 runs with no refusal, and every kind it logged is in the roster. The second
    clause is what lets this test observe the failure it excludes: it counts the kinds (`checked`) that
    `append` had to accept, `loop/matter.py`'s two crossing kinds among them."""
    w = build_realm(0)
    run(1, 0, w=w)                                     # raises `Forbidden` at the first refused kind
    kinds = {e.kind for e in w.log}
    assert kinds <= EVENT_KINDS, sorted(kinds - EVENT_KINDS)
    checked = len(w.log)
    assert checked >= 1000 and len(kinds) >= 20, (checked, len(kinds))
