"""`IS-B3-GO-07` (V12 B34.10; A-104) -- A MANAGEMENT ORDER COSTS NO SCENE. `rosters.yaml: management_orders` ships EMPTY (CL-MGMT's list is held),
so every test here PLANTS a one-member list (`dispatch`, a verb row) by rebinding the name the reader holds: `decision.choose.MANAGEMENT_ORDERS`
for the packer and `loop.deliberate.MANAGEMENT_ORDERS` for the release. The control each time is the shipped empty list, where nothing changes.

The refusal of a member that is no verb row (`data/verbs.py::_check_resolution_classes`) and the realm hash at the empty list were each RUN ONCE
at B34.10's build and are not kept (receipt)."""

from __future__ import annotations

import importlib

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import MANAGEMENT_ORDERS
from ..decision import choose as CH
from ..loop.driver import SeasonDriver
from ..queries import world_q
from ..state.carriers import Act, Candidate, Person, Scene
from . import test_dispatch_sends as DS
from .test_in53_vacancy_need import _formed

DL = importlib.import_module("engine.season.loop.deliberate")
ORDER = "dispatch"
ORDERS = frozenset({ORDER})
EXT = DEFAULT_FIXTURES.get("extended_scene_cost")


def _mint(*a):
    return "|".join(a)


def _scene(verbs, effort=0, who="p"):
    return Scene("s", who, [Act(f"a{i}", who, v, payload={"effort": effort} if effort else None) for i, v in enumerate(verbs)])


def _pack(ranked, budget):
    fx = DEFAULT_FIXTURES.sweep("interactions_per_scene", 3)
    return CH.pack_scenes(Person(id="p_pack", name="p_pack"), ranked, budget, fx, _mint)


def test_an_order_scene_costs_nothing_and_a_priced_scene_is_unchanged():
    assert _scene([ORDER]).cost(EXT, ORDERS) == 0
    assert _scene([ORDER, ORDER]).cost(EXT, ORDERS) == 0, "every act an order: free, however many"
    assert _scene(["utter"]).cost(EXT, ORDERS) == 1, "a plain scene: one"
    assert _scene(["utter"], effort=1).cost(EXT, ORDERS) == EXT > 1, "an extended one: `extended_scene_cost`"
    assert _scene([ORDER, "utter"]).cost(EXT, ORDERS) == EXT, "a hand-built mixed scene is priced as two slots, never half free"
    assert Scene("e", "p").cost(EXT, ORDERS) == 1, "an empty scene is no order scene"


def test_an_order_never_shares_a_scene_with_a_priced_act(monkeypatch):
    ranked = [Candidate("utter", "x"), Candidate(ORDER, "m"), Candidate("utter", "y"), Candidate("convene", "z")]
    kept = [[a.verb for a in s.acts] for s in _pack(ranked, 5)]
    assert kept == [["utter", ORDER, "utter"], ["convene"]], "CONTROL: with no list the order rides in a priced scene"
    monkeypatch.setattr(CH, "MANAGEMENT_ORDERS", ORDERS)
    scenes = _pack(ranked, 5)
    assert [[a.verb for a in s.acts] for s in scenes] == [["utter"], [ORDER], ["utter", "convene"]]
    assert [s.cost(EXT, ORDERS) for s in scenes] == [1, 0, EXT]


def test_a_person_with_a_full_budget_may_still_order(monkeypatch):
    monkeypatch.setattr(CH, "MANAGEMENT_ORDERS", ORDERS)
    ranked = [Candidate("utter", "x"), Candidate(ORDER, "m"), Candidate("convene", "z")]
    assert [[a.verb for a in s.acts] for s in _pack(ranked, 0)] == [[ORDER]], "a remainder of 0 still packs the order"
    assert [[a.verb for a in s.acts] for s in _pack(ranked, 1)] == [["utter"], [ORDER]], "one priced scene, the order beside it"

    # and DELIBERATE releases it: every person's season budget spent, the chooser asked and the order let through
    def released(orders):
        monkeypatch.setattr(DL, "MANAGEMENT_ORDERS", orders)
        w = DS.P.tiny_world()
        w.frozen = True
        d = SeasonDriver(w)
        d._spent = {pid: 10_000 for pid in w.persons}
        out = d.deliberate(lambda p, v, s, ask: [_scene([ORDER], who=p.id)] if p.id == DS.DUKE else [], None, d._questions_at_barrier())
        return [(sc.actor, [a.verb for a in sc.acts]) for sc in out.values()]
    assert released(frozenset()) == [], "CONTROL: spent, and no order is a management order: nothing is asked or released"
    assert released(ORDERS) == [(DS.DUKE, [ORDER])]


def test_an_order_opens_a_scene_next_lap(monkeypatch):
    """The Duke's `dispatch` costs 0; the fold and WITNESS leave the clerk holding the order, and the scene he forms on it, `comply`, is priced 1."""
    monkeypatch.setattr(CH, "MANAGEMENT_ORDERS", ORDERS)
    w, d = DS._world()
    DS._dispatch(w, d, dest=DS.TO)
    rid = "rec:d1"
    comply = [c for q in world_q.questions_for(w, w.persons[DS.MAN]) for c in _formed(w, DS.MAN, q) if c.verb == "comply" and c.subject == rid]
    assert comply, "the order opened a scene for its recipient"
    scenes = CH.pack_scenes(w.persons[DS.MAN], comply[:1], 5, w.fixtures, _mint)
    assert [[a.verb for a in s.acts] for s in scenes] == [["comply"]]
    assert scenes[0].cost(EXT, ORDERS) == 1
    assert _scene([ORDER]).cost(EXT, ORDERS) == 0
