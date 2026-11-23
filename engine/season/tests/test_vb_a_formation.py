"""B21.07/B21.08 -- VB-A commits A1 and A2: `release` forms only on a tie the actor holds, and a bench's sentence is not released by its party.

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

B21.08 -- commit A2: `establish` forms only on an unfounded holding.

  3. `test_a2_establish_forms_only_on_an_unfounded_holding` -- the row declares the class `Holding`, which only
     `world_q.holdings_to_found` stamps, and that stamp leaves out a holding whose office is already founded. Asked of the real
     `questions_for` and the real `opening_set`: a king who holds one territory (`T`) and holds nothing of another (`T2`) forms
     `establish` on `T` alone; a `Rung`-classed place that is no holding forms none; once the founding executes the same king forms
     none. CONTROL, same world: the holding is still stamped as a `Rung` (so `migrate`, `requisition`, `march` and `convene` keep
     their formation), and `migrate` still forms on a `Rung`-classed place. FALSIFIER: edit 6's `founded_office_id` filter dropped,
     the founded holding is offered again (read once, not kept).

B21.09 -- commit A3: `establish` is drawn.

  4. `test_a3_establish_bands_on_a_hand_built_holding` -- the founding contests the prize `a seat` (the social roll, no person
     opposite) and its band decides what it writes. On the king's world with one foundable holding (`T`), seeded across 40 world
     seeds, each seed's founding is folded by the real driver: all four bands occur; Overwhelming and Success found the office the
     derivation describes (`office_founded_by`), Partial founds it with the first half of that remit in authored order, and Failure
     writes nothing, emits `office.unrecognised` (deposited to the actor's own ledger at WITNESS, the durable write of the band,
     A-81) and leaves the holding stamped, so `establish` forms on it again. FALSIFIER: the roll pinned to Success, the band count
     collapses to one (read once, not kept). CONTROL: `rank_step` 0 lists no `rank_gap` term on any roll (read once, not kept).
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..data.verbs import VERB_TABLE
from ..decision.options import opening_set
from ..loop.driver import mint_token
from ..loop.predicates import office_founded_by
from ..queries import world_q
from ..state.attribution import causing_act
from ..state.carriers import Act, Proposition, Question, Tenure, View
from .test_cr25_computed_establish import _act as _found_act, _world as _king_world
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


def _forms(w, pid, verb, q):
    p = w.persons[pid]
    return sorted(c.subject for c in opening_set(p, View(pid, [], w.fixtures.get("view_k")), q, w.fixtures) if c.verb == verb)


def test_a2_establish_forms_only_on_an_unfounded_holding():
    w, d = _king_world()
    holding_cls = VERB_TABLE["establish"].referent_class
    assert holding_cls != "Rung", "establish still declares the class its sibling rows share"
    p = w.persons["p_king"]

    q = world_q.questions_for(w, p)[0]
    assert world_q.holdings_to_found(w, p) == ("T",), world_q.holdings_to_found(w, p)
    assert q.referents_for(holding_cls) == ("T",), q.classes
    assert _forms(w, "p_king", "establish", q) == ["T"]

    # a place that is no holding, carried as a `Rung`: no `establish`, while `migrate` (which declares `Rung`) is untouched
    stray = Question("q:vba2", "need", (), "T2", classes=(("T2", "Rung"),))
    assert _forms(w, "p_king", "establish", stray) == [], "establish formed on a Rung that is no holding"
    assert _forms(w, "p_king", "migrate", stray) == ["T2"]
    # CONTROL: the holding is still stamped as a Rung, so the sibling Rung rows form on it as before
    assert ("T", "Rung") in q.classes and _forms(w, "p_king", "migrate", q) == ["T"]

    # the founding executes; the holding is then founded, so it is no longer stamped as one and no `establish` forms on it
    assert [e.kind for e in _found_act(w, d, "e_vba2", "p_king", "off_king", {"subject": "T"})] == ["office.established"]
    assert world_q.founded_office_id("T", world_q.founded_post(w, "T")) in w.offices
    assert world_q.holdings_to_found(w, p) == ()
    q2 = world_q.questions_for(w, p)
    assert q2 and all(q_.referents_for(holding_cls) == () and _forms(w, "p_king", "establish", q_) == [] for q_ in q2)


def test_a3_establish_bands_on_a_hand_built_holding():
    bands: dict = {}
    checked = 0
    for seed in range(40):
        w, d = _king_world()
        w.world_seed = seed
        p = w.persons["p_king"]
        # the king holds Presence 5 (the row's one governing attribute), so each band carries several of the 40 draws; untrained he
        # reads one Overwhelming in 40 and the four-band check would rest on a single draw
        p.attributes = {**(p.attributes or {}), VERB_TABLE["establish"].governing[0]: 5}
        derived = office_founded_by(w, Act(id="probe", actor="p_king", verb="establish", via="off_king",
                                           payload={"subject": "T"}))
        assert derived is not None and derived.id not in w.offices and len(derived.remit_acts) >= 2, derived
        before = {k: list(o.remit_acts) for k, o in w.offices.items()}
        out = d.resolve(mint_token(w, WriteClass.ACTS),      # the real RESOLVE: the seam's draw decides the band
                        [Act(id=f"e_vba3_{seed}", actor="p_king", verb="establish", via="off_king", payload={"subject": "T"})],
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
        band = out[0].degree
        bands[band] = bands.get(band, 0) + 1
        if band == "Failure":
            assert _kinds(out) == ["office.unrecognised"], _kinds(out)
            assert {k: list(o.remit_acts) for k, o in w.offices.items()} == before, "a Failed founding wrote an office"
            w.log.extend(out)                                   # logged as `SeasonDriver.season` logs a RESOLVE pass
            d.witness(mint_token(w, WriteClass.INTERIOR), list(out))
            assert any(c.predicate == "office.unrecognised" for c in p.ledger), "the refused founding is no remembered deed"
            q = world_q.questions_for(w, p)[0]
            assert _forms(w, "p_king", "establish", q) == ["T"], "the Failed founding does not re-form"
        else:
            assert _kinds(out) == ["office.established"], (band, _kinds(out))
            got = w.offices[derived.id].remit_acts
            want = derived.remit_acts[: (len(derived.remit_acts) + 1) // 2] if band == "Partial" else derived.remit_acts
            assert got == want, (band, got, derived.remit_acts)
        checked += 1
    assert checked >= 40, checked
    assert set(bands) == {"Overwhelming", "Success", "Partial", "Failure"}, bands
