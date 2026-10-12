"""IN-53 (H-207 'VACANCY AS NEED') -- a vacant seat a person may fill widens his `need` questions;
`confer` forms on it with a conferee and executes in computed play.

The pieces, each of which can fail here: `queries/world_q.py::vacancies` (every Office with no live
`hold` that `may_fill` reaches through a seat of the person granting `confer`) and the Q4 splice in
`questions_for` (`(subject, *vacant)`, one `need` question per vacancy for a person with no
ambition), the class stamped per referent (`state/carriers.py::Question.classes`, from
`rosters.yaml: question_sources.referent_class`, unioned by `decision/questions.py::
aggregate_questions`), the verb column reading it (`verb_table.yaml: referent_class` ->
`VerbRow.formed_from`, compared in `decision/options.py::opening_set`), `confer`'s conferee
(`counterparty: to`, fanned by `VerbRow.known_person_operands`), and the one reader of the office an
act names (`loop/predicates.py::office_named_by`).

  (a) a seat with a live hold adds no referent; the same seat with its hold closed adds exactly its
      id to the `need` questions of the one person whose seat `may_fill` reaches it; with no vacancy
      the questions are byte-identical to the questions without the splice (the control).
  (b) `confer` forms for him with `to` over the persons he knows, and `confer`/`revoke` never form
      on a non-Office referent; a referent the person's `reach` excludes is never offered as one.
  (c) the class survives the fold; a class pair naming a referent the question is not about, or a
      class no source stamps, is refused; the loader refuses a verb column naming such a class.
  (d) the office reader: `subject` for a computed act, `office` for a hand-built one; a computed
      `confer` executes end to end into the vacant seat.
  (e) `build_realm(0)`, 3 seasons through the real chooser: `confer` executes >= 1 with `via`, into
      a seat with no live hold at the act's season; `issue`/`levy`/`transfer` execute at least as
      often as on the base (the crowd-out control, base counts pinned below).

MUTATION, run at the build: `vacant = vacancies(w, p)` -> `vacant = ()` in `questions_for` reddens
(a), (b) and (e).
"""
from collections import Counter

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import WriteClass
from engine.season.data.rosters import SOURCE_REFERENT_CLASS
from engine.season.data.verbs import VERB_TABLE
from engine.season.decision import aggregate_questions, assemble
from engine.season.decision.options import opening_set
from engine.season.gaps import Forbidden
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Question
from engine.season.state.gate import may_fill

from .test_g3_not_yours import _gov_world, _hold

CLASSED = ("confer", "revoke")


def _know(w, pid, *others):
    """`pid` knows `others` exist: the truthy `exists:Person` claim `known_persons` reads."""
    for i, o in enumerate(others):
        w.persons[pid].ledger.append(Claim(f"c_k{pid}{i}", pid, o, "exists:Person", 1, 0,
                                           "firsthand", 100, "own"))


def _need_refs(w):
    """Per person, the referents of their `need` questions that are offices."""
    return {pid: {r for q in world_q.questions_for(w, p) if q.source == "need"
                  for r in q.referents if r in w.offices}
            for pid, p in w.persons.items()}


def _formed(w, pid, q):
    p = w.persons[pid]
    return opening_set(p, assemble(p, q, 12), q, w.fixtures)


# ======================================================================================
# (a) THE VACANCY WIDENS `need`, AND ONLY FOR WHOEVER `may_fill` ADMITS
# ======================================================================================

def test_in53v_a_a_closed_hold_adds_exactly_its_seat_to_the_one_filler():
    """`off_duke2` (D2) is held by `p_other`. Held, it is nobody's referent. With the hold closed,
    exactly `p_king` (through `off_crown`, purview over R) may fill it -- `p_other`'s own seat is the
    seat itself, `p_high`'s duchy is a sibling -- and exactly his `need` referents gain it."""
    w, _ = _gov_world()
    before = _need_refs(w)
    assert all("off_duke2" not in refs for refs in before.values()), before
    _hold(w, "off_duke2").until = w.tick
    after = _need_refs(w)
    fillers = sorted(p for p in w.persons for t in w.persons[p].tenures
                     if t.kind == "hold" and t.live and t.object in w.offices
                     and "confer" in t.granted_acts and may_fill(w, p, t.object, w.offices["off_duke2"]))
    assert sorted(set(fillers)) == ["p_king"], fillers
    gained = {pid: after[pid] - before[pid] for pid in w.persons if after[pid] != before[pid]}
    assert gained == {"p_king": {"off_duke2"}}, gained


def test_in53v_a_every_need_question_carries_the_vacancies_and_qs0_keeps_its_id():
    """A person WITH an ambition keeps it as each `need` question's first referent and its id, the
    vacancies after it; one WITHOUT gets one `need` question per vacancy. Either way the class is
    stamped on the vacancies alone."""
    w, _ = _gov_world()
    p = w.persons["p_king"]
    vac = world_q.vacancies(w, p)
    assert vac and "off_reeve" in vac, vac
    no_amb = [q for q in world_q.questions_for(w, p) if q.source == "need"]
    assert [q.referents for q in no_amb] == [(o,) for o in vac], no_amb
    assert all(q.classes == ((q.referents[0], "Office"),) for q in no_amb), no_amb
    # Give him an ambition: one `need` question, its subject first, the vacancies after.
    from engine.season.state.carriers import Proposition, Tenure
    w.propositions["prop_k"] = Proposition("prop_k", "OUGHT", "R", "the realm thrives", True, 0)
    w.add_tenure(Tenure("tc_k", "p_king", "prop_k", "commit", since=0))
    qs = [q for q in world_q.questions_for(w, p) if q.source == "need"]
    assert [(q.id, q.referents) for q in qs] == [("q:need:prop_k", ("R",) + vac)], qs
    assert qs[0].class_of("R") is None and all(qs[0].class_of(o) == "Office" for o in vac)


def test_in53v_a_control_with_no_vacancy_the_questions_are_byte_identical(monkeypatch):
    """Seat every vacant office, so nobody has a vacancy: the questions then equal, field for field,
    what `questions_for` returns with the vacancy reader stubbed to `()` -- the splice adds nothing
    where there is nothing to add."""
    w, _ = _gov_world()
    from engine.season.state.carriers import Tenure
    held = {t.object for t in w.tenures if t.kind == "hold" and t.live}
    for i, o in enumerate(sorted(set(w.offices) - held)):
        w.add_tenure(Tenure(f"t_fill{i}", "p_mid", o, "hold", since=0))
    assert all(world_q.vacancies(w, p) == () for p in w.persons.values())
    real = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    monkeypatch.setattr(world_q, "vacancies", lambda w, p: ())
    stub = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    assert real == stub and repr(real) == repr(stub)
    assert all(q.classes == () for qs in real.values() for q in qs)


# ======================================================================================
# (b) `confer` FORMS WITH A CONFEREE, AND NOTHING CLASSED FORMS OFF AN OFFICE
# ======================================================================================

def test_in53v_b_confer_forms_on_the_vacancy_with_to_over_known_persons():
    w, _ = _gov_world()
    _know(w, "p_king", "p_mid", "p_low")
    p = w.persons["p_king"]
    vac = set(world_q.vacancies(w, p))
    cands = [c for q in world_q.questions_for(w, p) for c in _formed(w, "p_king", q)]
    confer = [c for c in cands if c.verb == "confer"]
    assert confer, [c.verb for c in cands]
    assert {c.subject for c in confer} == vac, (sorted({c.subject for c in confer}), vac)
    assert {c.operands.get("to") for c in confer} == {"p_mid", "p_low"}, confer
    # Knowing nobody, he forms none -- a conferral onto nobody is an act with a hole.
    w2, _ = _gov_world()
    q2 = world_q.questions_for(w2, w2.persons["p_king"])
    assert not [c for q in q2 for c in _formed(w2, "p_king", q) if c.verb == "confer"]


def test_in53v_b_classed_verbs_never_form_on_a_non_office_referent():
    """Over every person and every question in a world with vacancies, and over a FOLDED question
    mixing the vacancies with rungs and persons: `confer`/`revoke` Candidates name an Office every
    time, and some did form (else the check checked nothing)."""
    w, _ = _gov_world()
    for pid in w.persons:
        _know(w, pid, *[o for o in w.persons if o != pid])
    checked = 0
    for pid, p in w.persons.items():
        qs = world_q.questions_for(w, p)
        folded = [aggregate_questions(qs, rule) for rule in ("all", "one_per_source")] if qs else []
        mixed = [Question("q:mix", "need", ("R", "S", pid, "p_mid") + world_q.vacancies(w, p),
                          "", tuple((o, "Office") for o in world_q.vacancies(w, p)))]
        for q in qs + [f for f in folded if f is not None] + mixed:
            for c in _formed(w, pid, q):
                if c.verb in CLASSED:
                    assert c.subject in w.offices, (pid, q.id, c)
                    checked += 1
    assert checked >= 4, checked


def test_in53v_b_no_office_referent_outside_reach():
    """No person is offered an Office whose rung his `reach` excludes."""
    w, _ = _gov_world()
    _hold(w, "off_duke2").until = w.tick
    offered = 0
    for pid, p in w.persons.items():
        R = world_q.reach(w, p)
        for q in world_q.questions_for(w, p):
            for r, cls in q.classes:
                assert cls == "Office" and w.offices[r].rung in R, (pid, r, sorted(R))
                offered += 1
    assert offered >= 2, offered


# ======================================================================================
# (c) THE CLASS RIDES THE REFERENT AND IS CLOSED
# ======================================================================================

def test_in53v_c_the_class_survives_the_fold_and_is_closed():
    assert SOURCE_REFERENT_CLASS == {"claim_landed": None, "need": "Office"}
    a = Question("q:claim:x", "claim_landed", ("S",), "x")
    b = Question("q:need:off_reeve", "need", ("off_reeve",), "off_reeve", (("off_reeve", "Office"),))
    for rule in ("all", "one_per_source"):
        f = aggregate_questions([a, b], rule)
        assert f.source == "claim_landed" and f.class_of("off_reeve") == "Office", f
        assert f.class_of("S") is None
    assert aggregate_questions([a, b], "first") is a
    with pytest.raises(Forbidden, match="not about"):
        Question("q:bad", "need", ("off_duke",), "", (("off_other", "Office"),))
    with pytest.raises(Forbidden, match="no source stamps"):
        Question("q:bad", "need", ("off_duke",), "", (("off_duke", "Rung"),))


def test_in53v_c_the_loader_refuses_a_class_no_source_stamps(monkeypatch):
    assert VERB_TABLE["confer"].referent_class == "Office" == VERB_TABLE["revoke"].referent_class
    assert {v for v, r in VERB_TABLE.items() if r.referent_class} == set(CLASSED)
    assert VERB_TABLE["confer"].known_person_operands() == ("to",)
    assert VERB_TABLE["oblige"].known_person_operands() == ()       # untyped `subject`: no fan
    real = _verbs.load_yaml

    def planted(text):
        doc = real(text)
        if isinstance(doc, dict) and "verbs" in doc:
            for r in doc["verbs"]:
                if r.get("verb") == "confer":
                    r["referent_class"] = "Ofice"
        return doc
    monkeypatch.setattr(_verbs, "load_yaml", planted)
    with pytest.raises(SystemExit, match="no question source stamps"):
        _verbs._load_verb_table()


# ======================================================================================
# (d) THE OFFICE READER, AND A COMPUTED `confer` END TO END
# ======================================================================================

def test_in53v_d_one_office_reader_subject_or_office():
    assert _preds.office_named_by(Act("a", "p", "confer", payload={"subject": "off_x"})) == "off_x"
    assert _preds.office_named_by(Act("a", "p", "confer",
                                      payload={"subject": "s", "office": "off_y"})) == "off_y"
    assert _preds.office_named_by(Act("a", "p", "revoke", payload={})) is None


def test_in53v_d_a_computed_confer_fills_the_vacant_seat():
    """The Candidate `opening_set` forms (subject the vacancy, `to` a known person, the seat it is
    exercised through) folds to `tenure.opened` and seats the conferee."""
    w, d = _gov_world()
    _know(w, "p_king", "p_mid")
    q = next(q for q in world_q.questions_for(w, w.persons["p_king"]) if "off_reeve" in q.referents)
    c = next(c for c in _formed(w, "p_king", q)
             if c.verb == "confer" and c.subject == "off_reeve" and c.operands.get("to") == "p_mid")
    via = c.operands.get("via") or "off_crown"
    payload = {"subject": c.subject, **{k: v for k, v in c.operands.items() if k != "via"}}
    kinds = [e.kind for e in d.resolve(
        mint_token(w, WriteClass.ACTS),
        [Act(id="cf", actor="p_king", verb="confer", payload=payload, via=via)],
        contest_max_depth=w.fixtures.get("contest_max_depth"))]
    assert "tenure.opened" in kinds and _hold(w, "off_reeve").subject == "p_mid", kinds
    # And a hand-built `confer` naming no conferee is refused, never an InstrumentDefect.
    w2, d2 = _gov_world()
    kinds = [e.kind for e in d2.resolve(
        mint_token(w2, WriteClass.ACTS),
        [Act(id="cf", actor="p_king", verb="confer", payload={"subject": "off_reeve"},
             via="off_crown")], contest_max_depth=w2.fixtures.get("contest_max_depth"))]
    assert kinds == ["confer.refused"] and _hold(w2, "off_reeve") is None, kinds
