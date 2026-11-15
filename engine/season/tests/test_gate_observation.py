"""H-137 -- the gate sees an effect body that moves an ENTITY FIELD by itself.

`loop/resolve.py::_apply_write` runs the effect function BEFORE `World.write`, so a field the body
set before it returned its `Change` was baked into the gate's `before` and judged by nothing.
`World.effect_body_observed` snapshots every entity of `World._STATE_COLLECTIONS` around the call
(as it does the tenure store, `test_tenure_gate_effect_body.py`) and, for one that moved, was added
or was removed, puts it back and raises `NotYours`, which the fold emits as the row's refusal.

What each block proves, and the control that stops it passing vacuously:

  1. A FIELD SET IN THE BODY is refused, the field reads its old value after, and the act is a
     refusal Event, not a raise. Control (same host, actor, field, value): the same assignment
     deferred into `Change.apply`, which the gate admits and judges, is a success and stands.
  2. AN ENTITY ADDED OR REMOVED IN THE BODY is refused and the collection put back.
"""
import dataclasses

from engine.season.data.matrix import WriteClass
from engine.season.harness import probes as P
from engine.season.loop.driver import mint_token
from engine.season.state.carriers import Act, Tenure
from engine.season.state.containment import edges_of
from engine.season.state.gate import Change, Subject

from .test_g4_no_op_receipt import _driver, _plant
from .test_tenure_gate_effect_body import _grain, _run


def test_an_effect_that_eagerly_mutates_an_unrelated_entity_field_is_refused(monkeypatch):
    def eager(w, a, res=None):
        w.persons["p_high"].body = 7                          # the eager mutation of an unrelated field
        return _grain(w)
    _plant(monkeypatch, "utter", eager)
    w = P.tiny_world()
    assert w.persons["p_high"].body == 1000, "the fixture's field is not what the test reads"
    evs = _run(w, "h137_eager")         # B03.76: the gate's `NotYours` is the fold's refusal, not a raise
    assert [e.kind for e in evs] == ["act.refused"], [e.kind for e in evs]
    assert w.persons["p_high"].body == 1000, "the eager field write stood"
    assert w.rungs["Hh"].stores == {"grain": 8}, "the refused effect's write still ran"

    # CONTROL: the same assignment DEFERRED into `apply`, naming its subject, is admitted by the
    # gate and stands, so the refusal above came from the body's own write and from nothing else.
    def deferred(w, a, res=None):
        return Change((Subject.entity("persons", "p_high"),),
                      lambda: setattr(w.persons["p_high"], "body", 7))
    _plant(monkeypatch, "utter", deferred)
    w = P.tiny_world()
    evs = _run(w, "h137_deferred")
    assert [e.kind for e in evs] == ["proposition.uttered"], [e.kind for e in evs]
    assert w.persons["p_high"].body == 7


def test_an_effect_that_adds_or_removes_an_entity_in_its_body_is_refused_and_put_back(monkeypatch):
    def adds(w, a, res=None):
        w.sites["h137_side_site"] = dataclasses.replace(w.sites["site_harbour"], id="h137_side_site")
        return _grain(w)
    _plant(monkeypatch, "utter", adds)
    w = P.tiny_world()
    evs = _run(w, "h137_add")
    assert [e.kind for e in evs] == ["act.refused"], [e.kind for e in evs]
    assert "h137_side_site" not in w.sites, "the eagerly added entity stood"

    def removes(w, a, res=None):
        del w.sites["site_seam"]
        return _grain(w)
    _plant(monkeypatch, "utter", removes)
    w = P.tiny_world()
    seam = w.sites["site_seam"]
    evs = _run(w, "h137_remove")
    assert [e.kind for e in evs] == ["act.refused"], [e.kind for e in evs]
    assert w.sites.get("site_seam") is seam, "the eagerly removed entity stayed gone"


def test_an_equal_valued_replacement_is_put_back_as_the_original_object(monkeypatch):
    """Detection is by identity (`coll.get(k) is not item`); the restore compared members with `==`, so a
    body that replaced an entity with an EQUAL copy was detected, refused, and left the copy standing."""
    def replaces(w, a, res=None):
        w.sites["site_seam"] = dataclasses.replace(w.sites["site_seam"])
        return _grain(w)
    _plant(monkeypatch, "utter", replaces)
    w = P.tiny_world()
    seam = w.sites["site_seam"]
    evs = _run(w, "h137_equal_copy")
    assert [e.kind for e in evs] == ["act.refused"], [e.kind for e in evs]
    assert w.sites["site_seam"] is seam, "the equal-valued copy stood in place of the original"


def test_the_live_edge_view_follows_a_membership_change_that_keeps_the_counts():
    """`edges_of` caches a view of `(kind, subject)` Tenures at the barrier and rebuilds when the store's
    stamp moves. A stamp made of COUNTS (persons, unowned, owned) cannot see one Tenure leave and another
    arrive: every count is as it was and the view answers with the Tenure that is gone."""
    w = P.tiny_world()
    scan = lambda: [t for t in w.tenures if t.kind == "contain" and t.subject == "Hh"]
    old = edges_of(w, "contain", "Hh")
    assert [t.object for t in old] == ["S"] and old == scan(), "the fixture's edge is not what the test reads"
    counts = (len(w.persons), len(w._unowned), sum(len(p.tenures) for p in w.persons.values()))
    w._restore_tenures([(old[0], None)])                          # the store's own removal of an edge
    w.add_tenure(Tenure("t_swap", "Hh", "D", "contain", since=0))
    assert counts == (len(w.persons), len(w._unowned), sum(len(p.tenures) for p in w.persons.values()))
    got = edges_of(w, "contain", "Hh")
    assert [t.object for t in scan()] == ["D"]
    assert got == scan(), [t.id for t in got]

    # THE REFUSAL'S RESTORE: an edge opened and then put back is not in the view that read it open.
    w.add_tenure(Tenure("t_open", "Hh", "R", "contain", since=0))
    assert [t.id for t in edges_of(w, "contain", "Hh")] == ["t_swap", "t_open"]
    w._restore_tenures([(next(t for t in w.tenures if t.id == "t_open"), None)])
    assert [t.id for t in edges_of(w, "contain", "Hh")] == ["t_swap"]
