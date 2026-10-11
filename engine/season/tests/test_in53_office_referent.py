"""IN-53 (H-203, form B) -- offices as a standing referent; `confer` and `revoke` from computed play.

The `seat` question source (`rosters.yaml: question_sources`), the referent class it stamps on the
Question's REFERENTS (`state/carriers.py::Question.classes`, filled by `queries/world_q.py::
questions_for`, unioned by `decision/questions.py::aggregate_questions`), the verb column that
reads it (`verb_table.yaml: referent_class` -> `VerbRow.formed_from`, compared per referent in
`decision/options.py::opening_set`), the one reader of the office an act names
(`loop/predicates.py::office_named_by`), and the conferee a computed `confer` carries
(`VerbRow.known_person_operands`). Each block can fail:

  (a) a person whose `reach` covers an office's rung is offered a `seat` Question for it; one whose
      reach excludes it is not -- a sibling duchy, and a PLANTED far rung nobody's reach covers.
  (b) `confer`/`revoke` form Candidates only on a referent the question carries as `Office`: from a
      `claim_landed`/`need` question over the same referents -- an office id included -- none; every
      other verb's Candidates are the same whichever source the question came from.
  (c) the loader refuses a verb row naming a referent class no source yields.
  (d) `_req_revoke`/`_eff_revoke` (and `_req_confer`/`_eff_confer`) read the office from `subject`;
      a hand-built act's `office` still works.
  (e) THE CLASS SURVIVES THE FOLD (H-207 cause 2): a person whose FIRST question is a plain `need`
      and who also holds a `seat` question forms the office-class Candidate under `all` and
      `one_per_source`, where a class kept on the SOURCE is overwritten by the fold. Under `first`
      the person answers `qs[0]` alone, and that is H-54's rule: a non-office first question forms
      none -- asserted as such, not hidden.
  (f) THE CONFEREE (H-207 cause 4): a computed `confer` carries `to`, one Candidate per person the
      conferrer knows, none when he knows nobody and none on a non-office referent; a hand-built
      `confer` naming nobody, or the conferrer, is a `confer.refused`, not an `InstrumentDefect`.

NOT HELD HERE: the position's EXIT (`revoke` executing on `build_realm(0)`) -- `aperture`'s
reading, in the commit. The plan's stopping rule bars holding it as an xfail.
"""
from dataclasses import replace
from pathlib import Path

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import WriteClass
from engine.season.data.rosters import QUESTION_AGGREGATION, QUESTION_SOURCES, SOURCE_REFERENT_CLASS
from engine.season.data.verbs import VERB_TABLE, act_key
from engine.season.decision import aggregate_questions, assemble
from engine.season.decision.options import opening_set
from engine.season.gaps import Forbidden
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Office, Question, Rung

from .test_g3_not_yours import _RUNG_ABOVE, _gov_world, _hold

CLASSED = ("confer", "revoke")


def _with_far_office(w):
    """PLANTED: a rung in no containment tree and an office on it that nobody holds -- no limb of
    `reach` (me, mine, the ladder above home, a held seat's purview) can cover it."""
    w.rungs["F"] = Rung("F", "duchy")
    w.offices["off_far"] = Office("off_far", "Duke", "F", ["issue"], faction="Crown",
                                  conferral="appointed", revocation=_RUNG_ABOVE)
    return w


def _know(w, pid, *others):
    """`pid` knows `others` exist: the truthy `exists:Person` claim `known_persons` reads."""
    for i, o in enumerate(others):
        w.persons[pid].ledger.append(Claim(f"c_k{pid}{i}", pid, o, "exists:Person", 1, 0,
                                           "firsthand", 100, "own"))


def _formed(w, pid, q):
    p = w.persons[pid]
    return opening_set(p, assemble(p, q, 12), q, w.fixtures)


def _office_q(w, office="off_duke"):
    """A `seat` Question for `office`, built the way `questions_for` builds it."""
    return world_q._stamped(Question(f"q:seat:{office}", "seat", (office,)))


# ======================================================================================
# (a) THE SOURCE: ONE `seat` QUESTION PER OFFICE IN REACH, AND NONE OUTSIDE IT
# ======================================================================================

def test_in53_a_a_seat_question_is_offered_exactly_for_the_offices_in_reach():
    w, _ = _gov_world()
    _with_far_office(w)
    checked = offered = 0
    for p in w.persons.values():
        R = world_q.reach(w, p)
        got = {q.referents[0] for q in world_q.questions_for(w, p) if q.source == "seat"}
        for o in w.offices.values():
            want = o.rung is not None and o.rung in R
            assert (o.id in got) == want, (p.id, o.id, o.rung, sorted(R))
            checked += 1
            offered += want
        assert "off_far" not in got, f"{p.id} was offered the planted far office"
    assert checked >= len(w.persons) * len(w.offices) and offered > 0, (checked, offered)
    # The sibling duchy: `p_low` lives under D, so off_duke (D) is in reach and off_duke2 (D2) not.
    low = {q.referents[0] for q in world_q.questions_for(w, w.persons["p_low"]) if q.source == "seat"}
    assert "off_duke" in low and "off_duke2" not in low, sorted(low)


def test_in53_a_the_seat_question_is_claim_free_occasioned_by_nothing_and_classed():
    assert QUESTION_SOURCES[:2] == ("claim_landed", "need") and "seat" in QUESTION_SOURCES
    assert SOURCE_REFERENT_CLASS["seat"] == "Office"
    assert SOURCE_REFERENT_CLASS["need"] is None and SOURCE_REFERENT_CLASS["claim_landed"] is None
    w, _ = _gov_world()
    seats = [q for q in world_q.questions_for(w, w.persons["p_king"]) if q.source == "seat"]
    assert seats and all(q.about == "" and q.id == f"q:seat:{q.referents[0]}" for q in seats)
    assert all(q.class_of(q.referents[0]) == "Office" for q in seats)
    assert all(world_q.occasioned_by(w, q) == [] for q in seats)


def test_in53_a_only_the_seat_source_stamps_a_class():
    """`need` and `claim_landed` declare no class, so their referents (an office id included) are
    `None` -- the resolver stamps nothing the source did not declare."""
    w, _ = _gov_world()
    p = w.persons["p_king"]
    assert world_q._stamped(Question("q:need:x", "need", ("off_duke",))).classes == ()
    assert world_q._stamped(Question("q:claim:x", "claim_landed", ("off_duke",))).class_of("off_duke") is None
    stamped = [q for q in world_q.questions_for(w, p)]
    assert stamped and {q.source for q in stamped if q.classes} == {"seat"}


def test_in53_a_a_class_for_a_referent_the_question_is_not_about_is_refused():
    with pytest.raises(Forbidden, match="not about"):
        Question("q:bad", "seat", ("off_duke",), "", (("off_other", "Office"),))


# ======================================================================================
# (b) THE CLASS CHECK: `confer`/`revoke` ONLY ON A REFERENT CARRIED AS `Office`
# ======================================================================================

def test_in53_b_confer_and_revoke_form_only_on_an_office_class_referent():
    """`p_king` holds `remit:confer`+`remit:revoke` through `off_crown`, and knows `p_mid`. Over the
    SAME referent -- an office id -- a `claim_landed` or `need` question forms neither verb, and a
    `seat` question over it forms both. Every other verb forms the same Candidates from all three
    sources (the check reads the row's column and the referent's class, not the verb)."""
    w, _ = _gov_world()
    _know(w, "p_king", "p_mid")
    refs = ("off_duke",)
    by_source = {s: _formed(w, "p_king", world_q._stamped(Question(f"q:{s}:x", s, refs)))
                 for s in QUESTION_SOURCES}
    classed = {s: sorted({c.verb for c in cs if c.verb in CLASSED}) for s, cs in by_source.items()}
    assert classed["seat"] == ["confer", "revoke"], classed
    assert classed["claim_landed"] == [] and classed["need"] == [], classed
    other = {s: sorted({(c.verb, c.subject) for c in cs if c.verb not in CLASSED})
             for s, cs in by_source.items()}
    assert other["seat"] == other["claim_landed"] == other["need"] and other["seat"], other
    # Non-office referents: a rung, a person, the actor -- even from a `seat` question's company
    # (a mixed folded question) neither classed verb forms on them.
    mixed = Question("q:mix", "need", ("D", "S", "p_mid", "p_king", "off_duke"),
                     "", (("off_duke", "Office"),))
    got = {(c.verb, c.subject) for c in _formed(w, "p_king", mixed) if c.verb in CLASSED}
    assert got == {("confer", "off_duke"), ("revoke", "off_duke")}, got


def test_in53_b_every_unclassed_row_is_formed_on_every_referent():
    """`formed_from` is True for every row that declares no class, whatever the referent's class;
    the classed rows are formed only on an `Office`. Counted, so the loop cannot pass empty."""
    rows = 0
    for verb, row in VERB_TABLE.items():
        for cls in (None, "Office"):
            assert row.formed_from(cls) == (verb not in CLASSED or cls == "Office"), (verb, cls)
            rows += 1
    assert rows == len(VERB_TABLE) * 2 and rows > 0
    assert {v for v, r in VERB_TABLE.items() if r.referent_class} == set(CLASSED)


# ======================================================================================
# (c) THE LOADER REFUSES AN UNDECLARED REFERENT CLASS
# ======================================================================================

def test_in53_c_the_loader_refuses_a_referent_class_no_source_yields(monkeypatch, tmp_path):
    text = Path(_verbs.VERB_TABLE_YAML).read_text()
    assert text.count("referent_class: Office\n") == 2
    good = tmp_path / "good.yaml"
    good.write_text(text)
    monkeypatch.setattr(_verbs, "VERB_TABLE_YAML", good)
    assert _verbs._load_verb_table()["revoke"].referent_class == "Office"     # control
    bad = tmp_path / "bad.yaml"
    bad.write_text(text.replace("referent_class: Office\n", "referent_class: Ofice\n", 1))
    monkeypatch.setattr(_verbs, "VERB_TABLE_YAML", bad)
    with pytest.raises(SystemExit, match="referent_class 'Ofice'"):
        _verbs._load_verb_table()


# ======================================================================================
# (d) ONE READER: THE OFFICE IS `subject` ON A COMPUTED ACT, `office` ON A HAND-BUILT ONE
# ======================================================================================

def _resolve(w, d, act):
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act],
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))]


@pytest.mark.parametrize("key", ["subject", "office"])
def test_in53_d_revoke_reads_the_office_from_subject_or_office(key):
    w, d = _gov_world()
    act = Act(id=f"rv_{key}", actor="p_king", verb="revoke", payload={key: "off_duke"},
              via="off_crown")
    assert _preds.office_named_by(act) == "off_duke"
    assert _preds._req_revoke(w, act)
    kinds = _resolve(w, d, act)
    assert "tenure.closed" in kinds, kinds
    assert _hold(w, "off_duke") is None, "the hold is still live"


@pytest.mark.parametrize("key", ["subject", "office"])
def test_in53_d_confer_reads_the_office_from_subject_or_office(key):
    w, d = _gov_world()
    act = Act(id=f"cf_{key}", actor="p_high", verb="confer",
              payload={key: "off_reeve", "to": "p_mid"}, via="off_duke")
    assert _preds._req_confer(w, act)
    assert "tenure.opened" in _resolve(w, d, act)
    assert _hold(w, "off_reeve").subject == "p_mid"


def test_in53_d_office_wins_over_subject_and_neither_names_nothing():
    a = Act(id="x", actor="p_king", verb="revoke", payload={"office": "off_duke", "subject": "D"})
    assert _preds.office_named_by(a) == "off_duke"
    assert _preds.office_named_by(Act(id="y", actor="p_king", verb="revoke", payload={})) is None


# ======================================================================================
# (e) THE CLASS SURVIVES THE FOLD (H-207 CAUSE 2)
# ======================================================================================

def _planted(w, first_source="need"):
    """A person whose FIRST question is a plain non-office one and who also holds a `seat` question
    for `off_duke`, as `questions_for` orders them (`need` before `seat`)."""
    first = world_q._stamped(Question("q:need:first", first_source, ("p_mid",), "prop_x"))
    return [first, _office_q(w, "off_duke")]


def _classed_candidates(w, pid, q):
    return sorted({(c.verb, c.subject) for c in _formed(w, pid, q) if c.verb in CLASSED})


@pytest.mark.parametrize("rule", ["all", "one_per_source"])
def test_in53_e_the_class_survives_a_folding_rule(rule):
    w, _ = _gov_world()
    _know(w, "p_king", "p_mid")
    qs = _planted(w)
    q = aggregate_questions(qs, rule)
    assert q.source == "need", "the fold stamps qs[0]'s source -- the premise of the test"
    assert q.class_of("off_duke") == "Office" and q.class_of("p_mid") is None
    assert _classed_candidates(w, "p_king", q) == [("confer", "off_duke"), ("revoke", "off_duke")]


def test_in53_e_under_first_the_answered_question_is_the_first_and_h54_is_untouched():
    """`first` returns `qs[0]` itself. With a non-office first question the person answers it alone
    and forms no office-class Candidate (H-54's rule, recorded, not changed); with the office
    question first it forms both -- the class is on the question's referent either way."""
    w, _ = _gov_world()
    _know(w, "p_king", "p_mid")
    qs = _planted(w)
    q = aggregate_questions(qs, "first")
    assert q is qs[0] and _classed_candidates(w, "p_king", q) == []
    swapped = aggregate_questions(list(reversed(qs)), "first")
    assert _classed_candidates(w, "p_king", swapped) == [("confer", "off_duke"), ("revoke", "off_duke")]


def test_in53_e_every_rostered_rule_is_exercised():
    """The parametrised rules above are the roster minus `first`; a rule added to the roster must be
    added to one test or the other."""
    assert set(QUESTION_AGGREGATION) == {"first", "all", "one_per_source"}


def test_in53_e_a_class_kept_on_the_source_would_not_survive_the_fold():
    """THE CONTROL FOR (e): the same fold, with the class read off the source (the first attempt's
    shape), loses it -- which is what the per-referent class exists to prevent."""
    w, _ = _gov_world()
    q = aggregate_questions(_planted(w), "all")
    on_source = SOURCE_REFERENT_CLASS[q.source]            # the folded question's source is `need`
    assert on_source is None and q.class_of("off_duke") == "Office"


# ======================================================================================
# (f) THE CONFEREE (H-207 CAUSE 4)
# ======================================================================================

def test_in53_f_a_computed_confer_carries_a_known_person_as_to():
    w, _ = _gov_world()
    _know(w, "p_king", "p_mid", "p_low")
    got = [c for c in _formed(w, "p_king", _office_q(w, "off_duke")) if c.verb == "confer"]
    # `p_king` holds two seats that grant `confer` (H-134): one Candidate per (conferee, seat).
    assert {c.operands.get("to") for c in got} == {"p_low", "p_mid"}, got
    assert {c.operands.get("via") for c in got} == {"off_crown", "off_mayor"}, got
    assert all(c.subject == "off_duke" for c in got)
    # distinct conferees (and seats) are distinct acts
    ids = {act_key(c.verb, c.subject, c.operands) for c in got}
    assert len(ids) == len(got) == 4, ids
    # `revoke` takes nobody: its operands stay what they were.
    assert all("to" not in c.operands for c in _formed(w, "p_king", _office_q(w, "off_duke"))
               if c.verb == "revoke")


def test_in53_f_a_conferrer_who_knows_nobody_forms_no_confer():
    w, _ = _gov_world()
    names = {c.verb for c in _formed(w, "p_king", _office_q(w, "off_duke"))}
    assert "revoke" in names and "confer" not in names, names


def test_in53_f_confer_is_not_fanned_on_a_non_office_referent():
    """`to` over every referent a question names is how `30d38a12` failed: no `confer` on a rung,
    a person or a Record, however many persons are known."""
    w, _ = _gov_world()
    _know(w, "p_king", "p_mid", "p_low")
    q = Question("q:need:r", "need", ("D", "S", "p_mid", "p_king"))
    assert not [c for c in _formed(w, "p_king", q) if c.verb in CLASSED]


def test_in53_f_a_hand_built_confer_naming_nobody_is_refused_not_raised():
    w, d = _gov_world()
    for i, payload in enumerate(({"office": "off_reeve"}, {"office": "off_reeve", "to": "p_high"})):
        act = Act(id=f"cf_x{i}", actor="p_high", verb="confer", payload=payload, via="off_duke")
        kinds = _resolve(w, d, act)
        assert kinds == ["confer.refused"], (payload, kinds)
        assert _hold(w, "off_reeve") is None


def test_in53_f_the_untyped_counterparty_is_still_no_candidate_where_it_is_not_a_known_person():
    """`oblige` is untyped and names `counterparty: subject`: still the declared hole, formed by
    nobody (IN-10 (a) is the position that closes it)."""
    assert VERB_TABLE["oblige"].known_person_operands() == ()
    assert VERB_TABLE["confer"].known_person_operands() == ("to",)
    assert VERB_TABLE["tell"].known_person_operands() == ("to",)
    assert VERB_TABLE["revoke"].known_person_operands() == ()


# ======================================================================================
# (g) END TO END: A COMPUTED `revoke`, THEN A COMPUTED `confer` INTO THE SEAT IT VACATED
# ======================================================================================

def test_in53_g_a_computed_revoke_then_a_computed_confer_execute():
    """The whole computed path with nothing hand-built but the pick: `opening_set` forms the
    Candidate from a `seat` question, `pack_scenes` mints the act (`Act.via` the seat it was formed
    for), the fold admits it from `subject` alone and the effect writes. Then the SAME path confers
    the seat it vacated on a person the conferrer knows -- `to` carried, not defaulted, not raised.
    (What this does not claim: that a person CHOOSES either; `aperture`'s reading is that.)"""
    from engine.season.decision.choose import pack_scenes
    from engine.season.state.ids import H
    w, d = _gov_world()
    _know(w, "p_king", "p_mid")
    p, q = w.persons["p_king"], _office_q(w, "off_duke")
    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")

    def act_for(verb):
        cands = [c for c in _formed(w, "p_king", q) if c.verb == verb and c.operands["via"] == "off_crown"]
        assert len(cands) == 1, (verb, cands)
        scenes = pack_scenes(p, cands, 99, w.fixtures, mint, occasion=q)
        (a,) = [a for s in scenes for a in s.acts]
        return a

    rv = act_for("revoke")
    assert rv.via == "off_crown" and "office" not in rv.payload and rv.payload["subject"] == "off_duke"
    assert _hold(w, "off_duke") is not None
    assert "tenure.closed" in _resolve(w, d, rv), "the computed revoke did not execute"
    assert _hold(w, "off_duke") is None

    cf = act_for("confer")
    assert cf.payload["to"] == "p_mid" and cf.payload["subject"] == "off_duke"
    assert "tenure.opened" in _resolve(w, d, cf), "the computed confer did not execute"
    assert _hold(w, "off_duke").subject == "p_mid"
