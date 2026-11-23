"""H-143 (B03.76) -- a refusal by the write gate EMITS in the fold, never raises out of it.

`04 §C`'s row "a refusal emits, never raises | no raise path after eligibility" is MECHANICAL.
`_fold` already converted F9's `NoOpReceipt` into the row's `emits_on_refusal`; F3's `NotYours`
escaped it, so a precondition the gate disagreed with ended the season. The fold now catches
`NotYours` beside `NoOpReceipt` (the act's own write, and the site-sum write that refuses every
staged act through `_refuse_after_the_fact`).

What each test proves, and the control that stops it passing vacuously:

  1. THE MISMATCH EMITS. A `confer` whose `_req_confer` admits (the precondition is the one thing
     replaced) and whose write the gate refuses as not the actor's (a seat with no purview over
     the office) comes out of `resolve` as ONE `confer.refused` Event, the store put back, and the
     next act in the same batch still folds. Control: the shipped `_req_confer` refuses the same
     act first, so the gate's clause is what was read, not the predicate's.
  2. THE GATE IS UNCHANGED. A direct `World.write` of the same refused edge still raises
     `NotYours` and puts the store back -- only the FOLD converts it.
  3. THE SITE-SUM WRITE. A `NotYours` raised by the summed `(Site, condition)` write refuses every
     act staged on the site, as a `NoOpReceipt` there does."""
import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.loop import predicates as PR
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.state.carriers import Act, StateChange
from engine.season.state.gate import NotYours
from engine.season.state.world import World
from engine.season.trace_log import TRACE

from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)
from .test_g3_not_yours import _gov_world, _hold


def _confer(w, d, aid, actor, via, to="p_mid"):
    return d.resolve(mint_token(w, WriteClass.ACTS),
                     [Act(id=aid, actor=actor, verb="confer",
                          payload={"office": "off_reeve", "to": to}, via=via)],
                     contest_max_depth=w.fixtures.get("contest_max_depth"))


@pytest.mark.usefixtures("seat_at_success")       # B21.14: the gate's refusal is read here at Success; the draw is C3's test
def test_a_precondition_and_gate_mismatch_emits_the_refusal(monkeypatch):
    # CONTROL: the shipped precondition refuses `p_other` through `off_duke2` (no purview over the
    # reeve's rung) before the gate is asked.
    w, d = _gov_world()
    assert [e.kind for e in _confer(w, d, "c_ctl", "p_other", "off_duke2")] == ["confer.refused"]

    # THE MISMATCH: the precondition admits what the gate refuses.
    monkeypatch.setitem(PR.REQUIRES_PREDICATES, "confer", lambda w, a: True)
    w, d = _gov_world()
    with TRACE.recording():
        first = len(TRACE.rows)
        # one batch: the refused act, then a lawful one -- the season must carry on past the refusal
        out = d.resolve(
            mint_token(w, WriteClass.ACTS),
            [Act(id="c_bad", actor="p_other", verb="confer",
                 payload={"office": "off_reeve", "to": "p_mid"}, via="off_duke2"),
             Act(id="c_ok", actor="p_high", verb="confer",
                 payload={"office": "off_reeve", "to": "p_mid"}, via="off_duke")],
            contest_max_depth=w.fixtures.get("contest_max_depth"))
        decided = [r for r in TRACE.rows[first:]
                   if r.channel == "DECISION" and "gate refused" in r.what]
    mine = [e for e in out if e.causes and e.causes[0] == "c_bad"]
    assert [e.kind for e in mine] == ["confer.refused"], [e.kind for e in out]
    assert not [t for t in w.tenures if t.object == "off_reeve" and t.subject == "p_mid"
                and t.id.startswith("c_bad")], "the refused opener left a hold"
    assert len(decided) == 1 and decided[0].where == "C.4", [r.what for r in decided]
    carried_on = [e.kind for e in out if e.causes and e.causes[0] == "c_ok"]
    assert "tenure.opened" in carried_on, carried_on
    assert _hold(w, "off_reeve").subject == "p_mid"


def test_a_direct_gate_write_still_raises():
    w, _ = _gov_world()
    t = _hold(w, "off_duke")
    with pytest.raises(NotYours) as refused:
        w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda: setattr(t, "until", w.tick),
                record_kind="Tenure", fieldname="until", driver="Act", actor="p_king", via=None)
    assert refused.value.where == "F3"
    assert t.live, "the refused closure was not put back"


def test_the_site_sum_write_refuses_its_staged_acts_on_a_gate_refusal(monkeypatch):
    """`work` stages a delta on a Site; the summed `(Site, condition)` write is the fold's own, with
    no actor. The shipped gate cannot refuse an entity write, so the refusal is PLANTED at the
    `World.write` seam for that one write (no actor, `Site`/`condition`); the staged act must come
    out refused and the site unmoved. Control: unplanted, the same act succeeds."""
    def run(plant):
        w = P.tiny_world()
        site = w.sites["site_seam"]
        d = SeasonDriver(w)
        w.step = Step.RESOLVE
        if plant:
            real = World.write

            def refusing(self, *a, **kw):
                if (kw.get("actor") is None and kw.get("record_kind") == "Site"
                        and kw.get("fieldname") == "condition"):
                    raise NotYours("planted: the summed site write is refused", "F3")
                return real(self, *a, **kw)
            monkeypatch.setattr(World, "write", refusing)
        before = site.condition
        out = d.resolve(mint_token(w, WriteClass.ACTS),
                        [Act(id="wk_ny", actor="p_low", verb="work", payload={"site": site.id},
                             changes=[StateChange(site.id, "alter", "Act", "condition", 5)])])
        return [e.kind for e in out], before, site.condition

    kinds, before, after = run(plant=False)
    assert kinds == ["site.worked"] and after == before + 5, (kinds, before, after)
    with TRACE.recording():
        first = len(TRACE.rows)
        kinds, before, after = run(plant=True)
        decided = [r for r in TRACE.rows[first:]
                   if r.channel == "DECISION" and "summed write" in r.what and "refused by the gate" in r.what]
    assert kinds == ["work.unavailable"], kinds
    assert len(decided) == 1, [r.what for r in TRACE.rows[first:] if r.channel == "DECISION"]
