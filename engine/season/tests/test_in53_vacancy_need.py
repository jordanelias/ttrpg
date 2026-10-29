"""IN-53 (H-207 'VACANCY AS NEED', DECISION 2026-10-13 D1/D2) -- a vacant seat a person may fill
rides, as a CLASSED referent, on the question he answers; `confer` forms on it with a conferee who
may be himself, and executes end to end through the fold ((d)).

The pieces, each of which can fail here: `queries/world_q.py::vacancies` (every Office with no live
`hold` that `may_fill` reaches through a seat of the person granting `confer`) and the post-sort
splice in `questions_for` (`out[0]` carries them through `_stamped`; a person with no question gets
one `need` question carrying them), the classed referents (`state/carriers.py::Question.classes`,
a PARTITION beside `referents`, `Question.referents_for`, unioned by `decision/questions.py::
aggregate_questions`), the verb column reading it (`verb_table.yaml: referent_class` ->
`VerbRow.referents_of`, iterated by `decision/options.py::opening_set`), `confer`'s conferee
(`counterparty: to` fanned over known persons, plus the conferrer under `counterparty_may_be_self`,
`decision/options.py::operand_bags`; both counterparty sites ask `VerbRow.self_counterparty_refused`),
and the one reader of the office a `confer` names (`loop/predicates.py::office_named_by`).

  (a) a seat with a live hold adds nothing; the same seat with its hold closed is carried, classed,
      by exactly the one person whose seat `may_fill` reaches it, on his FIRST question only, which
      keeps its id, source and plain referents; with no vacancy the questions are byte-identical
      (the control); THE PARTITION: every row but `confer` forms exactly the Candidates it forms
      from the same question with its classed referents stripped.
  (b) `confer` forms on the vacancies and nothing else, `to` over the persons he knows AND himself;
      knowing nobody, himself alone; no Office outside his `reach` is offered.
  (c) the classes survive the fold and are closed; the loader refuses an undeclared class and a
      `counterparty_may_be_self` that is no boolean or sits on a row the fan does not reach.
  (d) the office reader; a computed `confer` executes end to end, onto another and onto himself;
      one naming nobody is refused.
  (e) RETIRED 2026-10-13 (the session user's "Relax exit rules"; plan §0.5): the realm-execution
      exit on `build_realm(0)` at 4 seasons is a recorded reading, not a test.
  (f) the U2 fingerprint moves when a classed referent opens or is told of under an unchanged
      question id (`loop/deliberate.py::_inputs_fingerprint`).

MUTATIONS, run at the build: `vacant = vacancies(w, p)` -> `vacant = ()` in `questions_for`, and the
self term in `operand_bags` deleted -- each reddens this file (counts in H-207's OUTCOME).
"""
import dataclasses

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import REFERENT_CLASSES
from engine.season.data.verbs import VERB_TABLE
from engine.season.decision import aggregate_questions, assemble
from engine.season.decision.options import opening_set
from engine.season.gaps import Forbidden
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Proposition, Question, Tenure
from engine.season.state.ids import ROOT
from engine.season.state.gate import may_fill

from .test_g3_not_yours import _gov_world, _hold


def _know(w, pid, *others):
    """`pid` knows `others` exist: the truthy `exists:Person` claim `known_persons` reads."""
    for i, o in enumerate(others):
        w.persons[pid].ledger.append(Claim(f"c_k{pid}{i}", pid, o, "exists:Person", 1, 0,
                                           "firsthand", 100, "own"))


def _classed(w):
    """Per person, the ids their questions carry as classed referents."""
    return {pid: {r for q in world_q.questions_for(w, p) for r, _ in q.classes}
            for pid, p in w.persons.items()}


def _formed(w, pid, q):
    p = w.persons[pid]
    return opening_set(p, assemble(p, q, 12), q, w.fixtures)


def _ambition(w, pid, prop, subject):
    w.propositions[prop] = Proposition(prop, "OUGHT", subject, f"{prop} thrives", True, 0)
    w.add_tenure(Tenure(f"tc_{prop}", pid, prop, "commit", since=0))


# ======================================================================================
# (a) THE VACANCY RIDES ON THE QUESTION ANSWERED, AND ONLY FOR WHOEVER `may_fill` ADMITS
# ======================================================================================

def test_in53v_a_a_closed_hold_adds_exactly_its_seat_to_the_one_filler():
    """`off_duke2` (D2) is held by `p_other`. Held, it is nobody's referent. With the hold closed,
    exactly `p_king` (through `off_crown`, purview over R) may fill it -- `p_other`'s own seat is the
    seat itself, `p_high`'s duchy is a sibling -- and exactly his classed referents gain it."""
    w, _ = _gov_world()
    before = _classed(w)
    assert all("off_duke2" not in refs for refs in before.values()), before
    _hold(w, "off_duke2").until = w.tick
    after = _classed(w)
    fillers = sorted(p for p in w.persons for t in w.persons[p].tenures
                     if t.kind == "hold" and t.live and t.object in w.offices
                     and "confer" in t.granted_acts and may_fill(w, p, t.object, w.offices["off_duke2"]))
    assert sorted(set(fillers)) == ["p_king"], fillers
    gained = {pid: after[pid] - before[pid] for pid in w.persons if after[pid] != before[pid]}
    assert gained == {"p_king": {"off_duke2"}}, gained


def test_in53v_a_the_first_question_carries_them_and_keeps_its_id_source_and_referents():
    """With NO question, one `need` question carrying the vacancies (no plain referent). With two
    ambitions, the FIRST question after the sort carries them, its id/source/plain referents as they
    were without the splice; the second carries none."""
    w, _ = _gov_world()
    p = w.persons["p_king"]
    vac = world_q.vacancies(w, p)
    assert vac and "off_reeve" in vac, vac
    (only,) = world_q.questions_for(w, p)
    assert (only.source, only.referents) == ("need", ()), only
    assert only.classes == tuple((o, "Office") for o in vac), only
    _ambition(w, "p_king", "prop_b", "R")
    _ambition(w, "p_king", "prop_a", "S")
    qs = world_q.questions_for(w, p)
    assert [(q.id, q.source, q.referents) for q in qs] == [
        ("q:need:prop_a", "need", ("S",)), ("q:need:prop_b", "need", ("R",))], qs
    assert qs[0].classes == tuple((o, "Office") for o in vac) and qs[1].classes == (), qs


def test_in53v_a_control_with_no_vacancy_the_questions_are_byte_identical(monkeypatch):
    """Seat every vacant office, so nobody has a vacancy: the questions then equal, field for field,
    what `questions_for` returns with the vacancy reader stubbed to `()`. Every person holds an
    ambition, so there ARE questions to compare (batch B-I close, L6: with none, both sides were
    empty and the comparison could not fail)."""
    w, _ = _gov_world()
    held = {t.object for t in w.tenures if t.kind == "hold" and t.live}
    for i, o in enumerate(sorted(set(w.offices) - held)):
        w.add_tenure(Tenure(f"t_fill{i}", "p_mid", o, "hold", since=0))
    for pid in w.persons:
        _ambition(w, pid, f"prop_{pid}", "R")
    assert all(world_q.vacancies(w, p) == () for p in w.persons.values())
    real = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    assert all(real.values()), real
    monkeypatch.setattr(world_q, "vacancies", lambda w, p: ())
    stub = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
    assert real == stub and repr(real) == repr(stub)
    assert all(q.classes == () for qs in real.values() for q in qs)


def _sig(cands):
    return sorted(repr((c.verb, c.subject, sorted(c.operands.items()))) for c in cands)


def test_in53v_a_the_partition_moves_no_other_rows_formations():
    """THE CROWD-OUT CONTROL AT FORMATION, BY CONSTRUCTION: over every person and question (as
    built, and folded under `all`/`one_per_source`), with the vacancies on them, every Candidate of
    every row but `confer` equals what the same question forms with its classed referents stripped;
    and stripped, `confer` forms nothing. RE-RECORDED AT v9 IN-10 (a): "every row but `confer`" is
    now every row declaring no `referent_class:` -- `oblige` declares `Office` too (a seat the person
    was told of), so both are the classed side of the partition and neither forms when stripped."""
    classed_rows = {v for v, r in VERB_TABLE.items() if r.referent_class}
    w, _ = _gov_world()
    _hold(w, "off_duke2").until = w.tick
    for pid in w.persons:
        _know(w, pid, *[o for o in w.persons if o != pid])
        _ambition(w, pid, f"prop_{pid}", "off_reeve")     # an office id ALSO as a plain referent
    checked = 0
    for pid, p in w.persons.items():
        qs = world_q.questions_for(w, p)
        folded = [aggregate_questions(qs, rule) for rule in ("all", "one_per_source")]
        for q in qs + [f for f in folded if f is not None]:
            got = _formed(w, pid, q)
            bare = _formed(w, pid, dataclasses.replace(q, classes=()))
            assert _sig(c for c in got if c.verb not in classed_rows) == _sig(bare), (pid, q.id)
            assert not [c for c in bare if c.verb in classed_rows], (pid, q.id)
            checked += bool(q.classes)
    assert checked >= 3, checked


# ======================================================================================
# (b) `confer` FORMS ON THE VACANCIES ALONE, ONTO A KNOWN PERSON OR HIMSELF
# ======================================================================================

def test_in53v_b_confer_forms_on_the_vacancy_with_to_over_known_persons_and_himself():
    w, _ = _gov_world()
    _know(w, "p_king", "p_mid", "p_low")
    p = w.persons["p_king"]
    vac = set(world_q.vacancies(w, p))
    confer = [c for q in world_q.questions_for(w, p) for c in _formed(w, "p_king", q)
              if c.verb == "confer"]
    assert {c.subject for c in confer} == vac, (sorted({c.subject for c in confer}), vac)
    assert {c.operands.get("to") for c in confer} == {"p_mid", "p_low", "p_king"}, confer
    # Knowing nobody, he may still assume the seat himself (D2) -- and only that.
    w2, _ = _gov_world()
    q2 = world_q.questions_for(w2, w2.persons["p_king"])
    tos = {c.operands.get("to") for q in q2 for c in _formed(w2, "p_king", q) if c.verb == "confer"}
    assert tos == {"p_king"}, tos


def test_in53v_b_only_confer_forms_on_a_classed_referent_and_only_on_one():
    """Every `confer` Candidate names a referent its question carries as `Office`; no other row
    forms on an id it carries ONLY classed. RE-RECORDED AT v9 IN-10 (a): `oblige`, which declares the
    class too, is held to `confer`'s rule (no `oblige` forms here: nobody was told of a seat)."""
    classed_rows = {v for v, r in VERB_TABLE.items() if r.referent_class}
    w, _ = _gov_world()
    for pid in w.persons:
        _know(w, pid, *[o for o in w.persons if o != pid])
        _ambition(w, pid, f"prop_{pid}", "R")          # plain referents, so other rows form too
    checked = other = 0
    for pid, p in w.persons.items():
        for q in world_q.questions_for(w, p):
            only_classed = {r for r, _ in q.classes} - set(q.referents)
            for c in _formed(w, pid, q):
                if c.verb in classed_rows:
                    assert (c.subject, "Office") in q.classes, (pid, q.id, c)
                    checked += c.verb == "confer"
                else:
                    assert c.subject not in only_classed, (pid, q.id, c)
                    other += bool(only_classed)
    # Batch B-I close (L6): the second branch compared something -- Candidates of unclassed rows
    # formed from a question that carried an Office-only referent.
    assert checked >= 4 and other >= 1, (checked, other)


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
# (c) THE CLASSES RIDE THE QUESTION AND ARE CLOSED; THE TWO COLUMNS ARE VALIDATED
# ======================================================================================

def test_in53v_c_the_classes_survive_the_fold_and_are_closed():
    # RE-RECORDED AT v9 IN-09: `Record` joins (was `{"Office"}`), the held writs `writs_held` stamps.
    # RE-RECORDED AT v9 IN-45 `migrate`: `Rung` joins, the places `places_named` stamps (H-168).
    # Spelled as a size and two memberships: `test_jordan_no_definition_is_hardcoded_in_a_body` flags a
    # three-string literal here as a roster duplicated from rosters.yaml.
    # RE-RECORDED AT v10 REM-21: `Site`, `Proposition` and `Person` join (was 3), the classes the
    # own-referent term stamps once a row declares one (`test_referent_class_stamps.py`).
    assert len(REFERENT_CLASSES) == 6 and {"Office", "Record"} <= REFERENT_CLASSES and "Rung" in REFERENT_CLASSES
    a = Question("q:claim:x", "claim_landed", ("S",), "x")
    b = Question("q:need:off_reeve", "need", (), "off_reeve", (("off_reeve", "Office"),))
    for rule in ("all", "one_per_source"):
        f = aggregate_questions([a, b], rule)
        assert f.source == "claim_landed" and f.referents_for("Office") == ("off_reeve",), f
        assert f.referents_for(None) == ("S",), f
    assert aggregate_questions([a, b], "first") is a
    with pytest.raises(Forbidden, match="no declared class"):
        # `Rung` is declared since IN-45, `Site` since v10 REM-21; a misspelt class still refuses
        Question("q:bad", "need", ("off_duke",), "", (("off_duke", "Ofice"),))
    with pytest.raises(Forbidden, match="twice"):
        Question("q:bad", "need", (), "", (("off_duke", "Office"), ("off_duke", "Office")))


def _planted(monkeypatch, verb, key, value):
    real = _verbs.load_yaml

    def planted(text):
        doc = real(text)
        if isinstance(doc, dict) and "verbs" in doc:
            for r in doc["verbs"]:
                if r.get("verb") == verb:
                    r[key] = value
        return doc
    monkeypatch.setattr(_verbs, "load_yaml", planted)


def test_in53v_c_the_declarations_as_built():
    # RE-RECORDED AT v9 IN-10 (a): `oblige` declares the class (was `{"confer"}`); AT v9 IN-09 the
    # `comply` declares `Record` (was `{"confer", "oblige"}`); AT v9 IN-45 `migrate` declares `Rung`;
    # AT v9 IN-49 `requisition` declares `Rung` beside it; AT v10 REM-22 `restore`, `work` and `examine`
    # declare `Site` (B10-05); AT v10 REM-23 `commit` declares `Proposition` (B10-05).
    assert {v for v, r in VERB_TABLE.items() if r.referent_class} == {"confer", "oblige", "comply",
                                                                      "migrate", "requisition",
                                                                      "restore", "work", "examine",
                                                                      "commit"}
    assert VERB_TABLE["migrate"].referent_class == "Rung" and not VERB_TABLE["migrate"].referent_named
    assert VERB_TABLE["requisition"].referent_class == "Rung" and not VERB_TABLE["requisition"].referent_named
    assert VERB_TABLE["confer"].referent_class == VERB_TABLE["oblige"].referent_class == "Office"
    assert {v for v, r in VERB_TABLE.items() if r.counterparty_may_be_self} == {"confer"}
    assert VERB_TABLE["confer"].known_person_operands() == ("to",)
    assert VERB_TABLE["oblige"].known_person_operands() == ()       # untyped `subject`: no fan
    for verb in ("tell", "give"):                                    # the fan's other rows: unchanged
        assert VERB_TABLE[verb].known_person_operands() and not VERB_TABLE[verb].counterparty_may_be_self


@pytest.mark.parametrize("verb,key,value,match", [
    ("confer", "referent_class", "Ofice", "not a declared class"),
    ("confer", "counterparty_may_be_self", "true", "is `true` or `false`"),
    ("oblige", "counterparty_may_be_self", True, "not an operand a known person fills"),
])
def test_in53v_c_the_loader_refuses(monkeypatch, verb, key, value, match):
    _planted(monkeypatch, verb, key, value)
    with pytest.raises(SystemExit, match=match):
        _verbs._load_verb_table()


# ======================================================================================
# (d) THE OFFICE READER, AND A COMPUTED `confer` END TO END
# ======================================================================================

def test_in53v_d_one_office_reader_subject_or_office():
    assert _preds.office_named_by(Act("a", "p", "confer", payload={"subject": "off_x"})) == "off_x"
    assert _preds.office_named_by(Act("a", "p", "confer",
                                      payload={"subject": "s", "office": "off_y"})) == "off_y"
    assert _preds.office_named_by(Act("a", "p", "confer", payload={})) is None


def _fold_confer(w, d, payload, via, aid="cf"):
    return [e.kind for e in d.resolve(
        mint_token(w, WriteClass.ACTS),
        [Act(id=aid, actor="p_king", verb="confer", payload=payload, via=via)],
        contest_max_depth=w.fixtures.get("contest_max_depth"))]


@pytest.mark.parametrize("to", ["p_mid", "p_king"])
def test_in53v_d_a_computed_confer_fills_the_vacant_seat(to):
    """The Candidate `opening_set` forms (subject the vacancy, `to` a known person or the conferrer
    himself, the seat it is exercised through) folds to `tenure.opened` and seats the conferee."""
    w, d = _gov_world()
    _know(w, "p_king", "p_mid")
    (q,) = world_q.questions_for(w, w.persons["p_king"])
    c = next(c for c in _formed(w, "p_king", q)
             if c.verb == "confer" and c.subject == "off_reeve" and c.operands.get("to") == to)
    via = c.operands.get("via") or "off_crown"
    payload = {"subject": c.subject, **{k: v for k, v in c.operands.items() if k != "via"}}
    kinds = _fold_confer(w, d, payload, via)
    assert "tenure.opened" in kinds and _hold(w, "off_reeve").subject == to, kinds


@pytest.mark.parametrize("to", ["p_mid", "p_king"])
def test_in53v_g_conferring_a_seat_on_its_own_holder_is_refused(to):
    """B-I close, Phase 3 F1: a seat conferred on the person who already holds it changes nothing but
    would close and reopen his edge, and (his ledger then naming the seat) feed itself every season.
    Red before `_req_confer`'s `holder == conferee` refusal; the first conferral and a conferral on
    somebody ELSE are the controls (both admitted)."""
    w, d = _gov_world()
    assert "tenure.opened" in _fold_confer(w, d, {"subject": "off_reeve", "to": to}, "off_crown")
    first = _hold(w, "off_reeve")
    assert first.subject == to
    again = _fold_confer(w, d, {"subject": "off_reeve", "to": to}, "off_crown", aid="cf2")
    assert again == ["confer.refused"], again
    assert _hold(w, "off_reeve") is first and first.live        # untouched: no close, no reopen


def test_in53v_g_a_list_valued_subject_is_refused_never_raised():
    """Sibling of the unhashable `to`: a hand-built `confer` whose subject is a list refuses."""
    w, d = _gov_world()
    assert _fold_confer(w, d, {"subject": ["off_reeve"], "to": "p_mid"}, "off_crown") == ["confer.refused"]


def test_in53v_d_a_confer_naming_nobody_is_refused():
    w, d = _gov_world()
    kinds = _fold_confer(w, d, {"subject": "off_reeve"}, "off_crown")
    assert kinds == ["confer.refused"] and _hold(w, "off_reeve") is None, kinds


def test_in53v_d_an_act_on_a_classed_referent_cites_no_unrelated_occasion():
    """A vacancy rides on whatever question the person answers (D1), so a `confer` can be packed in
    a scene whose occasion is a `claim_landed` question about something else. Its occasion is the
    STANDING one, `[ROOT]` as a Q4 `need` has (plan IN-53 step 3; batch B-I close, F1), never the
    unrelated claim's originating Event. Control: an act on the same scene's PLAIN referent still
    cites it, and so does one whose subject is both plain and classed."""
    from engine.season.state.carriers import Event, Scene, StateChange
    w, d = _gov_world()
    origin = Event("ev_v_origin", "speech.made", [], [ROOT], w.tick)
    w.log.append(origin)
    w.log.append(Event("ev_v_deposit", "claim.deposited",
                       [StateChange("claim_v", "set", "Act")], [origin.id], w.tick))
    q = Question("q:claim:claim_v", "claim_landed", ("S",), "claim_v", (("off_reeve", "Office"),))
    d.scenes["sc_v"] = Scene("sc_v", "p_king", [], occasion=q)
    assert world_q.occasioned_by(w, q) == [origin.id]          # the scene HAS an occasion
    a = Act(id="cf_v", actor="p_king", verb="confer", via="off_crown", scene="sc_v",
            payload={"subject": "off_reeve", "to": "p_king"})
    out = d.resolve(mint_token(w, WriteClass.ACTS), [a],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert "tenure.opened" in [e.kind for e in out], [e.kind for e in out]
    assert not [e for e in out if origin.id in e.causes], [(e.kind, e.causes) for e in out]
    plain = Act(id="pl_v", actor="p_king", verb="work", scene="sc_v", payload={"subject": "S"})
    assert d._occasion_ids(w, plain) == [origin.id]
    both = Question("q:claim:claim_v", "claim_landed", ("off_reeve",), "claim_v",
                    (("off_reeve", "Office"),))
    d.scenes["sc_v2"] = Scene("sc_v2", "p_king", [], occasion=both)
    assert d._occasion_ids(w, dataclasses.replace(a, id="cf_v2", scene="sc_v2")) == [origin.id]


def test_in53v_d_a_confer_onto_no_living_person_is_refused():
    """The conferee must be a living person (batch B-I close, C1): `to` comes from the conferrer's
    own claims (`known_persons`), which can name somebody since dead; an id `w.persons` does not hold
    is refused at the precondition (`_req_confer`), never filed as a seat held by nobody."""
    w, d = _gov_world()
    kinds = _fold_confer(w, d, {"subject": "off_reeve", "to": "p_ghost"}, "off_crown")
    assert kinds == ["confer.refused"] and _hold(w, "off_reeve") is None, kinds
    w, d = _gov_world()
    w.step = Step.MATTER                    # a death, in `loop/matter.py`'s own write shape
    w.write("Tenure", mint_token(w, WriteClass.MATTER), lambda: w.remove_person("p_mid"),
            record_kind="Tenure", fieldname="until", driver="Event",
            caused_person_exists="p_mid", emits="tenure.closed", subject="p_mid", causes=[ROOT])
    w.step = Step.RESOLVE
    assert "p_mid" not in w.persons
    kinds = _fold_confer(w, d, {"subject": "off_reeve", "to": "p_mid"}, "off_crown")
    assert kinds == ["confer.refused"] and _hold(w, "off_reeve") is None, kinds


# ======================================================================================
# (f) THE U2 FINGERPRINT SEES THE CLASSED REFERENTS (batch B-I close, L1): `loop/deliberate.py::
# _inputs_fingerprint` must move whenever `opening_set` would form a different set, or the driver
# serves a stale queue. Both arms keep every question id fixed, which is the case the id alone missed.
# ======================================================================================

def _fp_and_formed(w, pid, since=None):
    from engine.season.loop.deliberate import _inputs_fingerprint
    from engine.season.state.carriers import Sensation
    p = w.persons[pid]
    qs = world_q.questions_for(w, p, since)
    return ([q.id for q in qs], _inputs_fingerprint(p, qs, Sensation(0)),
            _sig(c for q in qs for c in _formed(w, pid, q)))


def test_in53v_f_a_vacancy_opening_under_a_standing_question_moves_the_fingerprint():
    """`p_king` answers an ambition question. `off_reeve` is seated (no vacancy), then its hold
    closes: the question keeps its id and gains the seat as `Office`, `confer` forms on it -- and the
    fingerprint must move, though nothing of `p_king`'s own (tenures, ledger) did."""
    w, _ = _gov_world()
    _ambition(w, "p_king", "prop_k", "R")
    w.add_tenure(Tenure("t_seat_reeve", "p_mid", "off_reeve", "hold", since=0))
    ids0, fp0, sig0 = _fp_and_formed(w, "p_king")
    _hold(w, "off_reeve").until = w.tick
    ids1, fp1, sig1 = _fp_and_formed(w, "p_king")
    assert ids1 == ids0 == ["q:need:prop_k"], (ids0, ids1)
    assert sig1 != sig0 and any("'confer', 'off_reeve'" in s for s in sig1), sig1
    assert fp1 != fp0, "the vacancy moved the candidate set and left the fingerprint unmoved"


def test_in53v_f_being_told_of_a_seat_already_carried_moves_the_fingerprint():
    """`off_reeve` is already `p_king`'s vacancy, so being TOLD of it moves no class and no id -- but
    `oblige` (`referent_named`) starts forming on it. `since` is past the told claim, so Q2 does not
    admit it as a question of its own (it would move the ids by itself, and the arm would observe
    nothing): what is left is the seventh term."""
    from .test_in10a_oblige_formable import _told
    w, _ = _gov_world()
    _ambition(w, "p_king", "prop_k", "R")
    since = (w.tick, 1)
    ids0, fp0, sig0 = _fp_and_formed(w, "p_king", since)
    _told(w, "p_king", "off_reeve")
    ids1, fp1, sig1 = _fp_and_formed(w, "p_king", since)
    assert ids1 == ids0 == ["q:need:prop_k"], (ids0, ids1)
    assert fp1[0] == fp0[0], "the classes moved: this arm no longer isolates the told term"
    assert sig1 != sig0 and any("'oblige', 'off_reeve'" in s for s in sig1), sig1
    assert fp1 != fp0, "being told of the seat moved the candidate set, not the fingerprint"
