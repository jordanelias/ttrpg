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

H-135 (B09.21) -- `loop/matter.py`'s wear loop does not write a Site whose wear this season is 0, so
no `condition.worn` reports a condition that did not move (`test_a_zero_wear_write_emits_no_condition_worn`,
whose control is a Site that wears and still writes).
"""
import dataclasses

from engine.season.boot.realm import build_realm
from engine.season.data.matrix import Step, WriteClass
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.state.attribution import anchor_of
from engine.season.state.carriers import Act, Site, Tenure
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
    assert [e.kind for e in evs] == ["utter.refused"], [e.kind for e in evs]
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
    assert [e.kind for e in evs] == ["utter.refused"], [e.kind for e in evs]
    assert "h137_side_site" not in w.sites, "the eagerly added entity stood"

    def removes(w, a, res=None):
        del w.sites["site_seam"]
        return _grain(w)
    _plant(monkeypatch, "utter", removes)
    w = P.tiny_world()
    seam = w.sites["site_seam"]
    evs = _run(w, "h137_remove")
    assert [e.kind for e in evs] == ["utter.refused"], [e.kind for e in evs]
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
    assert [e.kind for e in evs] == ["utter.refused"], [e.kind for e in evs]
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


def _matter(w):
    """MATTER alone, through the real barrier and a real MATTER token; returns what it emitted."""
    w.step = Step.MATTER
    return SeasonDriver(w).matter(mint_token(w, WriteClass.MATTER), [])


def _worn(w, evs) -> dict:
    """`{site id: [condition.worn Events]}` among the Events MATTER returned."""
    out: dict = {}
    for e in evs:
        if e.kind == "condition.worn":
            out.setdefault(anchor_of(w, e), []).append(e)
    return out


def test_a_zero_wear_write_emits_no_condition_worn():
    """H-135: a Site whose wear this season is 0 is not written and emits nothing. The falsifier is a
    `condition.worn` whose Site's condition did not move; the CONTROL, in the same MATTER pass, is a Site
    that wears (harbour, seam), which still writes, emits one and moves."""
    w = P.tiny_world()
    scale = w.fixtures.get("condition_scale")
    w.sites["s_h135_dwelling"] = Site("s_h135_dwelling", "Hh", "dwelling", condition=scale)
    assert w.fixtures.wear("dwelling") == 0 and w.fixtures.wear("harbour") > 0, "the fixture's rates are not what the test reads"
    before = {sid: s.condition for sid, s in w.sites.items()}
    worn = _worn(w, _matter(w))
    # THE ARM: the zero-wear Site emits nothing and its condition stays put
    assert "s_h135_dwelling" not in worn, "a zero-wear Site still emitted `condition.worn`"
    assert w.sites["s_h135_dwelling"].condition == scale
    # THE CONTROL: the wearing Sites each wrote once, emitted once, and moved
    checked = 0
    for sid in ("site_harbour", "site_seam"):
        assert len(worn.get(sid, [])) == 1, (sid, sorted(worn))
        assert w.sites[sid].condition == max(0, before[sid] - w.fixtures.wear(w.sites[sid].kind)) != before[sid]
        checked += 1
    assert checked == 2
    # every `condition.worn` the pass logged is for a Site that wears
    logged = [e for e in w.log if e.kind == "condition.worn"]
    assert len(logged) == 2 and {anchor_of(w, e) for e in logged} == {"site_harbour", "site_seam"}


def test_a_site_already_at_condition_zero_is_not_written_and_emits_no_condition_worn():
    """H-135 (B09.21), the second half: a Site that wears but whose condition is already 0 would write
    `max(0, 0 - wear)` = 0, move nothing and still emit `condition.worn`. It is not written. CONTROL, in
    the same MATTER pass: a Site of the same kind with condition above 0, which still writes once."""
    w = P.tiny_world()
    scale = w.fixtures.get("condition_scale")
    w.sites["s_b0921_ruin"] = Site("s_b0921_ruin", "Hh", "harbour", condition=0)
    w.sites["s_b0921_sound"] = Site("s_b0921_sound", "Hh", "harbour", condition=scale)
    assert w.fixtures.wear("harbour") > 0 and scale > 0, "the fixture's rates are not what the test reads"
    worn = _worn(w, _matter(w))
    assert "s_b0921_ruin" not in worn, "a Site already at condition 0 still emitted `condition.worn`"
    assert w.sites["s_b0921_ruin"].condition == 0
    checked = 0
    for sid in ("s_b0921_sound", "site_harbour", "site_seam"):       # the control and the fixture's own wearers
        assert len(worn.get(sid, [])) == 1, (sid, sorted(worn))
        assert w.sites[sid].condition < (scale if sid == "s_b0921_sound" else w.sites[sid].condition + 1)
        checked += 1
    assert checked == 3
    logged = [e for e in w.log if e.kind == "condition.worn"]
    assert len(logged) == 3 and "s_b0921_ruin" not in {anchor_of(w, e) for e in logged}


def test_a_realm_season_emits_no_condition_worn_for_a_site_whose_wear_is_zero():
    """The same arm on the shipped realm, where `dwelling` and `garrison` wear 0: one MATTER pass writes
    one `condition.worn` per Site that wears and none for the rest."""
    w = build_realm(0)
    wearing = sorted(sid for sid, s in w.sites.items() if w.fixtures.wear(s.kind) > 0)
    still = sorted(sid for sid, s in w.sites.items() if w.fixtures.wear(s.kind) == 0)
    assert wearing and still, "the realm holds no wearing or no zero-wear Site, so this proves nothing"
    before = {sid: w.sites[sid].condition for sid in w.sites}
    worn = _worn(w, _matter(w))
    assert not (set(worn) & set(still)), sorted(set(worn) & set(still))[:3]
    checked = 0
    for sid in wearing:
        assert len(worn.get(sid, [])) == 1, sid
        checked += 1
    assert checked == len(wearing) > 0
    assert all(w.sites[sid].condition == before[sid] for sid in still)
