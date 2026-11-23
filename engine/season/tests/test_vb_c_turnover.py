"""B21.13 (`14_VERBS_BINDING_C` commit C2 with `06_FA_decree_binds` edit 5): `revoke` READS ITS SEAT FROM `subject`.

A COMPUTED `revoke` names its seat on `subject` (the classed Office referent of the question it was formed from) and
carries no `office` key; `confer` already read the seat that way (`loop/predicates.py::office_named_by`), `revoke` did not,
so every computed `revoke` was refused at its first clause. One function per gate of BIND_C's C2..C4 lives here; B21.14
adds C3's. The hand-built world is `test_g3_not_yours._gov_world` (`p_king` on `off_crown`, above `off_duke`, held by `p_high`).
"""
from __future__ import annotations

from engine.season.data.matrix import Step, WriteClass
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.state.carriers import Act

from .test_g3_not_yours import _gov_world, _hold

KING, VIA, TARGET = "p_king", "off_crown", "off_duke"


def _fold(w, d, act: Act) -> list:
    """Fold ONE act through the shipped `SeasonDriver.resolve`; the event kinds."""
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out]


def test_c2_a_computed_revoke_reaches_the_roll():
    """A `revoke` whose `subject` names the seat and whose payload carries no `office` is admitted and its effect closes
    the holder's `hold`. CONTROL: a hand-built act carrying `payload['office']` reads the same seat (`office` wins), and
    one naming no seat on either key is still refused."""
    w, d = _gov_world()
    assert _hold(w, TARGET) is not None, "fixture: the duke holds his seat"
    computed = Act(id="rv_computed", actor=KING, verb="revoke", payload={"subject": TARGET}, via=VIA)
    assert "office" not in computed.payload
    assert _preds._req_revoke(w, computed), "a computed revoke is refused at its precondition"
    assert _fold(w, d, computed) == ["tenure.closed"]
    assert _hold(w, TARGET) is None, "the effect did not close the holder's hold"

    w2, d2 = _gov_world()
    handbuilt = Act(id="rv_hand", actor=KING, verb="revoke", payload={"office": TARGET}, via=VIA)
    assert _preds._req_revoke(w2, handbuilt)
    assert _fold(w2, d2, handbuilt) == ["tenure.closed"] and _hold(w2, TARGET) is None

    w3, d3 = _gov_world()                       # `office` wins where both are present
    both = Act(id="rv_both", actor=KING, verb="revoke", payload={"office": TARGET, "subject": "off_nowhere"}, via=VIA)
    assert _preds.office_named_by(both) == TARGET
    assert _fold(w3, d3, both) == ["tenure.closed"] and _hold(w3, TARGET) is None

    w4, _ = _gov_world()
    assert not _preds._req_revoke(w4, Act(id="rv_none", actor=KING, verb="revoke", payload={}, via=VIA))
