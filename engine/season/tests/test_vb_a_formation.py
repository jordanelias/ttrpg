"""B21.07 -- VB-A commit A1: `release` forms only on a tie the actor holds, and a bench's sentence is not released by its party.

GAME STATE, lane `season_loop` (`engine/season/tests/`). Two claims, each asked of the real `opening_set`, the real fold and the real witness:

  1. `test_a1_release_forms_only_on_a_held_tie` -- the formation decline reads the row's own `domain:` (`rosters.yaml:
     own_edge_declines`): a person forms `release` on the object of a releasable edge he holds and on no other referent (not a
     seat he holds nothing toward, not a place he only `contain`s and `reside`s in, not a person). The realm arm (`aperture 2 0`
     refuses no `release`) is the batch gate's reading, not a test: two seasons of a realm cost 100 s.
  2. `test_a1_a_bench_imposed_edge_is_not_released_by_its_party` -- VRES §4 edit 1 (A-37). A determination opens the party's
     `oblige` on the seat; a `release` of it is refused by the FOLD (`_req_release`, the clause is the only thing between the party
     and the sentence) and the party's formation declines it once he HOLDS the finding in his own ledger (the generic Event claim,
     `subject` the edge's id). Controls, in the same world: before he hears of it the candidate forms and the fold still refuses
     (the person-side decline is a courtesy to the scene budget, not the rule); an edge he opened himself is released as ever.
     FALSIFIER (3a): a disposal edge closed by an Event whose actor is its subject -- no logged Event naming the edge has the party
     for its actor.
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..decision.options import opening_set
from ..loop.driver import mint_token
from ..queries import world_q
from ..state.attribution import causing_act
from ..state.carriers import Act, Proposition, Question, Tenure, View
from .test_u7_remit import DUKE, JUDGE, OPENS, PARTY, SEAT, _determine, _fold, _kinds, _obliges, _open, _world


def _formed(w, pid, referents):
    """The referents `pid` forms `release` on, for a question that carries `referents`."""
    q = Question("q:vba", "need", tuple(referents))
    p = w.persons[pid]
    got = [c.subject for c in opening_set(p, View(pid, [], w.fixtures.get("view_k")), q, w.fixtures) if c.verb == "release"]
    return got


def _release(key, actor, subject):
    return Act(id=key, actor=actor, verb="release", via=None, payload={"subject": subject})


def test_a1_release_forms_only_on_a_held_tie():
    w, _ = _world()
    w.propositions["prop_vba"] = Proposition("prop_vba", "IS", "p_low", "kind", True, 0)
    w.add_tenure(Tenure("t_vba_commit", "p_low", "prop_vba", "commit", since=0))
    p = w.persons["p_low"]
    held = {t.object for t in p.tenures if t.live}
    # the tied referents: `commit`'s object forms; his hearth (`contain` and `reside`, outside `release`'s `domain:`), the King
    # and a seat he holds nothing toward do not
    assert {"Hh", "p_king", SEAT} - held == {"p_king", SEAT} and "Hh" in held, held
    got = _formed(w, "p_low", ["prop_vba", "Hh", "p_king", SEAT])
    assert got == ["prop_vba"], got


def test_a1_a_bench_imposed_edge_is_not_released_by_its_party():
    w, d = _world(**JUDGE)
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    out = _fold(w, d, _determine("dt"))
    assert _kinds(out) == ["matter.determined"] and out[0].degree in OPENS, (_kinds(out), out[0].degree)
    edge, = _obliges(w)
    assert (edge.subject, edge.object, edge.live) == (PARTY, SEAT, True)

    # CONTROL: before the finding reaches his ledger the person-side decline has nothing to read, so the candidate FORMS -- and the
    # fold still refuses the planted release, naming the edge it would have closed: the fold's clause is the rule
    assert _formed(w, PARTY, [SEAT]) == [SEAT]
    out = _fold(w, d, _release("rel1", PARTY, SEAT))
    assert _kinds(out) == ["release.refused"], _kinds(out)
    assert edge.live and edge.until is None, "a party released the edge a bench imposed"

    # THE FORMATION HALF: the finding is deposited into his own ledger (the generic Event claim, `subject` the disposal edge)
    d.witness(mint_token(w, WriteClass.INTERIOR), [e for e in w.log if e.kind == "matter.determined"])
    heard = [c for c in w.persons[PARTY].ledger if c.predicate == "matter.determined" and c.subject == edge.id]
    assert heard and heard[0].value is True, "the party's ledger holds no claim of his own determination"
    assert _formed(w, PARTY, [SEAT]) == [], "a party forms a release of the edge a bench imposed on him"

    # CONTROL: an edge he opened himself is released through the same predicate, in the same world
    w.propositions["prop_vba"] = Proposition("prop_vba", "IS", DUKE, "kind", True, 0)
    own = Tenure("t_vba_own", PARTY, "prop_vba", "commit", since=0)
    w.add_tenure(own)
    assert _formed(w, PARTY, ["prop_vba"]) == ["prop_vba"]
    out = _fold(w, d, _release("rel2", PARTY, "prop_vba"))
    assert "release.refused" not in _kinds(out) and own.until is not None, _kinds(out)
    assert edge.live, "the release of his own commit closed the sentence beside it"

    # FALSIFIER (3a): a disposal edge closed by an Event whose actor is its subject
    closers = [e for e in w.log if any(c.subject == edge.id for c in e.changes)
               and (causing_act(w, e) is not None and causing_act(w, e).actor == edge.subject
                    and causing_act(w, e).verb != "determine")]
    assert closers == [], [e.kind for e in closers]
    assert world_q.establishment_of(w, SEAT).count(PARTY) == 1
