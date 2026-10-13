"""IN-53 (H-207 'VACANCY AS NEED', DECISION 2026-10-13 D1/D2) -- a vacant seat a person may fill
rides, as a CLASSED referent, on the question he answers; `confer` forms on it with a conferee who
may be himself, and executes in computed play.

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
  (e) `build_realm(0)`, 3 seasons through the real chooser: `confer` executes >= 1 with `via`, into
      a seat with no live hold when it resolved; the crowd-out control on executions.

MUTATIONS, run at the build: `vacant = vacancies(w, p)` -> `vacant = ()` in `questions_for`, and the
self term in `operand_bags` deleted -- each reddens this file (counts in H-207's OUTCOME).
"""
import dataclasses
from collections import Counter

import pytest

from engine.season.harness import populated as POP
from engine.season.harness.corpus_run import attribute
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.decision import make_chooser
from engine.season.state.ids import H, draw_factory

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import WriteClass
from engine.season.data.rosters import REFERENT_CLASSES
from engine.season.data.verbs import VERB_TABLE
from engine.season.decision import aggregate_questions, assemble
from engine.season.decision.options import opening_set
from engine.season.gaps import Forbidden
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Proposition, Question, Tenure
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
    what `questions_for` returns with the vacancy reader stubbed to `()`."""
    w, _ = _gov_world()
    held = {t.object for t in w.tenures if t.kind == "hold" and t.live}
    for i, o in enumerate(sorted(set(w.offices) - held)):
        w.add_tenure(Tenure(f"t_fill{i}", "p_mid", o, "hold", since=0))
    assert all(world_q.vacancies(w, p) == () for p in w.persons.values())
    real = {pid: world_q.questions_for(w, p) for pid, p in w.persons.items()}
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
    and stripped, `confer` forms nothing."""
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
            assert _sig(c for c in got if c.verb != "confer") == _sig(bare), (pid, q.id)
            assert not [c for c in bare if c.verb == "confer"], (pid, q.id)
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
    forms on an id it carries ONLY classed."""
    w, _ = _gov_world()
    for pid in w.persons:
        _know(w, pid, *[o for o in w.persons if o != pid])
    checked = 0
    for pid, p in w.persons.items():
        for q in world_q.questions_for(w, p):
            only_classed = {r for r, _ in q.classes} - set(q.referents)
            for c in _formed(w, pid, q):
                if c.verb == "confer":
                    assert (c.subject, "Office") in q.classes, (pid, q.id, c)
                    checked += 1
                else:
                    assert c.subject not in only_classed, (pid, q.id, c)
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
# (c) THE CLASSES RIDE THE QUESTION AND ARE CLOSED; THE TWO COLUMNS ARE VALIDATED
# ======================================================================================

def test_in53v_c_the_classes_survive_the_fold_and_are_closed():
    assert REFERENT_CLASSES == {"Office"}
    a = Question("q:claim:x", "claim_landed", ("S",), "x")
    b = Question("q:need:off_reeve", "need", (), "off_reeve", (("off_reeve", "Office"),))
    for rule in ("all", "one_per_source"):
        f = aggregate_questions([a, b], rule)
        assert f.source == "claim_landed" and f.referents_for("Office") == ("off_reeve",), f
        assert f.referents_for(None) == ("S",), f
    assert aggregate_questions([a, b], "first") is a
    with pytest.raises(Forbidden, match="no declared class"):
        Question("q:bad", "need", ("off_duke",), "", (("off_duke", "Rung"),))
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
    assert {v for v, r in VERB_TABLE.items() if r.referent_class} == {"confer"}
    assert VERB_TABLE["confer"].referent_class == "Office"
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


def _fold_confer(w, d, payload, via):
    return [e.kind for e in d.resolve(
        mint_token(w, WriteClass.ACTS),
        [Act(id="cf", actor="p_king", verb="confer", payload=payload, via=via)],
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


def test_in53v_d_a_confer_naming_nobody_is_refused():
    w, d = _gov_world()
    kinds = _fold_confer(w, d, {"subject": "off_reeve"}, "off_crown")
    assert kinds == ["confer.refused"] and _hold(w, "off_reeve") is None, kinds


# ======================================================================================
# (e) THE EXIT, ON `build_realm(0)`: 4 SEASONS THROUGH THE REAL CHOOSER, NOTHING FORCED (the plan's
# instrument is `aperture 4 0`; at 3 seasons seed 0 `confer` executes 0 times, at 4 it executes once)
# ======================================================================================

#: Executed `issue`+`levy`+`transfer` on the base commit (e716f10b), `build_realm(0)`, 4 seasons,
#: seed 0, `corpus_run.attribute`'s `made` -- the crowd-out control's floor, less one per `confer`
#: executed (each may displace at most one act).
_BASE_EXECUTED_ILT = 7      # issue 2 + levy 0 + transfer 5, `aperture 4 0` realm row at the base
SEASONS = 4


@pytest.fixture(scope="module")
def realm3():
    """`populated.run`'s construction, line for line, over `SEASONS` seasons."""
    w = POP.build_realm(0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(SEASONS):
        d.season(ch, question=None, subsistence=POP.P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d, attribute(w, d, SEASONS)


def test_in53v_e_confer_executes_into_a_seat_nobody_held(realm3):
    """At least one computed `confer` executes, through a seat (`via`), opening a hold and closing
    none -- the seat had no live hold when the act resolved (`_eff_confer` names a closure for every
    live hold it displaces, G4)."""
    w, _, rows = realm3
    into_vacant = [a for a, made, _ in rows
                   if a.verb == "confer" and made and a.via in w.offices
                   and "tenure.opened" in made and "tenure.closed" not in made]
    assert into_vacant, sorted(Counter(a.verb for a, made, _ in rows if made).items())


def test_in53v_e_the_crowd_out_control(realm3):
    w, _, rows = realm3
    ex = Counter(a.verb for a, made, _ in rows if made)
    ilt = ex["issue"] + ex["levy"] + ex["transfer"]
    assert ilt >= _BASE_EXECUTED_ILT - ex["confer"], (dict(ex), _BASE_EXECUTED_ILT)
    assert all(_preds.office_named_by(a) in w.offices for a, _, _ in rows if a.verb == "confer")
