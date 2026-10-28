"""CR-06 / H-137 -- the gate sees an effect body that changes a tenure by itself.

`loop/resolve.py::_apply_write` runs the effect function BEFORE `World.write`, and the tenure
snapshot F3 judges from is taken inside `write()`. A tenure the effect's own body moved before it
returned its `Change` was therefore baked into that snapshot and judged by nothing.
`World.effect_body_observed`, which `_apply_write` calls, now observes the tenure store around the
effect call and refuses a change there the same way the gate refuses an unauthored one: the store
put back first, then `NotYours`.

What each block proves, and the control that stops it passing vacuously:

  1. THE HOLE ROW'S WORKED EXAMPLE. An effect that sets `seat.until` on an unrelated live
     seat-hold in its own body and returns an unrelated `Change` raises `NotYours`, and the seat is
     live afterwards. Control (same host, same actor): an effect that builds the same `Change`
     with no eager closure is a success, so the refusal is the eager body's and not the host's.
  2. THE OPENED-EDGE ARM. An eager body that OPENS a tenure (one the actor would be lawfully
     allowed to write from inside `apply`) is refused too and the edge is removed: the fold does not
     ask whether it is lawful, because an effect body is not a write. Control: the same edge opened
     inside `apply` stands.
  3. A LEGITIMATE `Change` IS NOT REFUSED. An effect that mutates nothing in its body and returns
     a `Change` whose `apply` writes a tenure the gate admits is observed by `World.write` as before.

Tenures only: an eager write to an entity field is still convention-bound (`_apply_write` says so).
"""
import pytest

from engine.season.data.matrix import WriteClass
from engine.season.harness import probes as P
from engine.season.loop.driver import mint_token
from engine.season.state.carriers import Act, Tenure
from engine.season.state.gate import Change, NotYours, Subject

from .test_g4_no_op_receipt import _driver, _plant


def _run(w, aid):
    return _driver(w).resolve(mint_token(w, WriteClass.ACTS),
                              [Act(id=aid, actor="p_low", verb="utter")])


def _grain(w):
    """An unrelated `Change` that does move its subject (rung `Hh`'s grain 8 -> 9)."""
    return Change((Subject.entity("rungs", "Hh"),),
                  lambda: w.rungs["Hh"].stores.__setitem__("grain", 9))


def _live(w, tid):
    return [t.live for t in w.tenures if t.id == tid]


def test_cr06_an_effect_body_that_closes_a_seat_by_itself_is_refused_and_put_back(monkeypatch):
    """H-137's worked example: close an unrelated live seat-hold in the effect's own body, return
    an unrelated `Change` that does move its subject. `p_low` has no basis to close `p_high`'s seat
    (no `via`), so the gate would say `NotYours` if it had seen the write; it had not."""
    def eager(w, a, res=None):
        seat = next(t for t in w.tenures if t.id == "t9")
        seat.until = w.tick                                   # the eager mutation
        return _grain(w)
    _plant(monkeypatch, "utter", eager)
    w = P.tiny_world()
    assert _live(w, "t9") == [True], "the fixture seat is not live"
    with pytest.raises(NotYours):
        _run(w, "cr06_eager")
    assert _live(w, "t9") == [True], "the eager closure stood"
    assert w.rungs["Hh"].stores == {"grain": 8}, "the refused effect's write still ran"

    # CONTROL: the same host, actor and `Change` with no eager closure is a success and leaves the
    # seat live, so the `NotYours` above came from the effect body's closure and from nothing else.
    def clean(w, a, res=None):
        return _grain(w)
    _plant(monkeypatch, "utter", clean)
    w = P.tiny_world()
    evs = _run(w, "cr06_clean")
    assert [e.kind for e in evs] == ["proposition.uttered"], [e.kind for e in evs]
    assert w.rungs["Hh"].stores == {"grain": 9}
    assert _live(w, "t9") == [True]


def test_cr06_an_effect_body_that_opens_an_edge_by_itself_is_refused_and_removed(monkeypatch):
    def eager(w, a, res=None):
        w.add_tenure(Tenure("cr06_side_hold", "p_low", "Hh", "hold", w.tick))
        return _grain(w)
    _plant(monkeypatch, "utter", eager)
    w = P.tiny_world()
    with pytest.raises(NotYours):
        _run(w, "cr06_open")
    assert not [t for t in w.tenures if t.id == "cr06_side_hold"], "the eagerly opened edge stood"

    # CONTROL: the same edge opened INSIDE `apply` (T-m: the actor owns it) is admitted and stands.
    def deferred(w, a, res=None):
        t = Tenure("cr06_side_hold", "p_low", "Hh", "hold", w.tick)
        return Change((Subject.edge(t),), lambda: w.add_tenure(t))
    _plant(monkeypatch, "utter", deferred)
    w = P.tiny_world()
    evs = _run(w, "cr06_open2")
    assert [e.kind for e in evs] == ["proposition.uttered"], [e.kind for e in evs]
    assert _live(w, "cr06_side_hold") == [True]


def test_cr06_a_legitimate_change_is_observed_by_the_write_as_before(monkeypatch):
    """No eager mutation: the body only reads. The `Change` it returns closes `p_low`'s own `tie`
    edge (T-m, the owner writing his edge) inside `apply`; the gate admits it and the fold's
    observation around the effect call adds no refusal."""
    def lawful(w, a, res=None):
        tie = next(t for t in w.tenures if t.kind == "tie" and t.subject == "p_low")
        return Change((Subject.edge(tie),), lambda: setattr(tie, "until", w.tick))
    _plant(monkeypatch, "utter", lawful)
    w = P.tiny_world()
    evs = _run(w, "cr06_lawful")
    assert [e.kind for e in evs] == ["proposition.uttered"], [e.kind for e in evs]
    assert [t.live for t in w.tenures if t.kind == "tie" and t.subject == "p_low"] == [False]
