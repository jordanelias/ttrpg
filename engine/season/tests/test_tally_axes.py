"""B12b.13 -- a private tally raises a mandatory question (`09_WR_provided_arcs` edit 1; A-47, L3 clause 1, L5).

THE BUILD: `rosters.yaml: tally_axes` (shipped EMPTY) is the closed registry; `world_q.tally_reached(w, p)` names the referents
about which `p`'s OWN ledger holds at least `at` claims of an axis's kinds, and `questions_for` stamps each onto the question he answers
as a classed referent and marks that question `mandatory`. Nothing fires at the count: which act he takes is the chooser's draw.

The planted axis is `tally_axes`' one seam (`monkeypatch.setattr(world_q, "TALLY_AXES", ...)`), as the content is authored per arc.
  (a) THREE claims of an axis's kinds about one seat-holder reach him, TWO do not; the question is `mandatory`.
  (b) A person holding none is offered nothing, though another holds three about the same man (no world read leaks into a person-side tally).
  (c) The referent rides as a classed referent of the class the World gives it, and only on the holder's slate.
"""
from __future__ import annotations

from ..harness.probes import tiny_world
from ..queries import world_q
from ..state.carriers import Claim

AXIS = {"grievance": {"counts": ("body.changed",), "about": "Person", "at": 3}}


def _claims(holder: str, subject: str, n: int, kind: str = "body.changed") -> list:
    """`n` claims of `kind` about `subject`, long enough ago (`when=-5`) that none lands as news: the tally is the only occasion."""
    return [Claim(f"c_{holder}_{subject}_{i}", holder, subject, kind, True, -5, "firsthand", 100, "own") for i in range(n)]


def _world(monkeypatch, held: int, *, other: int = 0):
    """`p_high` holds `held` claims about `p_king`; `p_other` holds `other` about him; `p_low` holds none."""
    monkeypatch.setattr(world_q, "TALLY_AXES", AXIS)
    w = tiny_world()
    w.persons["p_high"].ledger = _claims("p_high", "p_king", held)
    w.persons["p_other"].ledger = _claims("p_other", "p_king", other)
    return w


def _slate(w, pid: str):
    return world_q.questions_for(w, w.persons[pid])


def test_three_claims_reach_the_tally_two_do_not(monkeypatch):
    reached = _world(monkeypatch, 3)
    assert world_q.tally_reached(reached, reached.persons["p_high"]) == ("p_king",)
    assert ("p_king", "Person") in _slate(reached, "p_high")[0].classes
    short = _world(monkeypatch, 2)
    assert world_q.tally_reached(short, short.persons["p_high"]) == ()
    assert _slate(short, "p_high") == [], "two claims are no occasion: he is offered no question at all"


def test_a_person_holding_none_is_offered_nothing(monkeypatch):
    w = _world(monkeypatch, 0, other=3)
    assert world_q.tally_reached(w, w.persons["p_other"]) == ("p_king",), "control: the same count in another's ledger does reach him"
    assert world_q.tally_reached(w, w.persons["p_high"]) == () and _slate(w, "p_high") == []
    assert world_q.tally_reached(w, w.persons["p_low"]) == () and _slate(w, "p_low") == []


def test_tally_referent_is_mandatory(monkeypatch):
    w = _world(monkeypatch, 3)
    q = _slate(w, "p_high")[0]
    assert q.mandatory and q.referents_for("Person") == (("p_king",)), "the question is marked and carries the referent for the rows that declare its class"
    assert not _slate(w, "p_low"), "and no other slate carries it"
