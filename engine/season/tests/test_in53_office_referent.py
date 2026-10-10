"""IN-53 (H-203, form B) -- offices as a standing referent; `confer` and `revoke` from computed play.

Steps (1)-(3) together: the `seat` question source (`rosters.yaml: question_sources`, last), the
referent-class declaration (`question_sources.referent_class` -> `verb_table.yaml: referent_class`
-> `VerbRow.formed_from`, compared in `decision/options.py::opening_set`), and the one reader of the
office an act names (`loop/predicates.py::office_named_by`). Each block can fail:

  (a) a person whose `reach` covers an office's rung is offered a `seat` Question for it; one whose
      reach excludes it is not -- a sibling duchy, and a PLANTED far rung nobody's reach covers.
  (b) `confer`/`revoke` form Candidates only from a question whose source declares `Office`: from a
      `claim_landed`/`need` question over the same referents -- an office id included -- none; every
      other verb's Candidates are the same whichever source the question came from.
  (c) the loader refuses a verb row naming a referent class no source yields.
  (d) `_req_revoke`/`_eff_revoke` (and `_req_confer`/`_eff_confer`) read the office from `subject`;
      a hand-built act's `office` still works.

NOT HELD HERE: the position's EXIT (`revoke` executing on `build_realm(0)`). Measured at piece B,
it does not execute under `first`, under H-54's swept arms, or with the question named -- the
plan's stopping rule bars holding it as an xfail.
"""
from pathlib import Path

import pytest

from engine.season.data import verbs as _verbs
from engine.season.data.matrix import WriteClass
from engine.season.data.rosters import QUESTION_SOURCES, SOURCE_REFERENT_CLASS
from engine.season.data.verbs import VERB_TABLE
from engine.season.decision import assemble
from engine.season.decision.options import opening_set
from engine.season.loop import predicates as _preds
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Office, Question, Rung

from .test_g3_not_yours import _RUNG_ABOVE, _gov_world, _hold

CLASSED = ("confer", "revoke")


def _with_far_office(w):
    """PLANTED: a rung in no containment tree and an office on it that nobody holds -- no limb of
    `reach` (me, mine, the ladder above home, a held seat's purview) can cover it."""
    w.rungs["F"] = Rung("F", "duchy")
    w.offices["off_far"] = Office("off_far", "Duke", "F", ["issue"], faction="Crown",
                                  conferral="appointed", revocation=_RUNG_ABOVE)
    return w


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


def test_in53_a_the_seat_question_is_last_claim_free_and_occasioned_by_nothing():
    assert QUESTION_SOURCES[-1] == "seat" and QUESTION_SOURCES[:2] == ("claim_landed", "need")
    assert SOURCE_REFERENT_CLASS["seat"] == "Office"
    w, _ = _gov_world()
    qs = world_q.questions_for(w, w.persons["p_king"])
    seats = [q for q in qs if q.source == "seat"]
    assert seats and all(q.about == "" and q.id == f"q:seat:{q.referents[0]}" for q in seats)
    order = [QUESTION_SOURCES.index(q.source) for q in qs]
    assert order == sorted(order), "seat questions do not come after every other source"
    assert all(world_q.occasioned_by(w, q) == [] for q in seats)


# ======================================================================================
# (b) THE CLASS CHECK: `confer`/`revoke` ONLY FROM AN `Office`-CLASS SOURCE
# ======================================================================================

def _formed(w, pid, q):
    p = w.persons[pid]
    return opening_set(p, assemble(p, q, 12), q, w.fixtures)


def test_in53_b_confer_and_revoke_form_only_from_an_office_class_question():
    """`p_king` holds `remit:confer`+`remit:revoke` through `off_crown`. Over the SAME referents --
    an office, a rung, a person and himself -- a `claim_landed` or `need` question forms neither
    verb, and a `seat` question over the office forms both. Every other verb forms the same
    Candidates from all three sources (the check reads the row's column, not the question)."""
    w, _ = _gov_world()
    refs = ("off_duke",)
    by_source = {s: _formed(w, "p_king", Question(f"q:{s}:x", s, refs)) for s in QUESTION_SOURCES}
    classed = {s: sorted(c.verb for c in cs if c.verb in CLASSED) for s, cs in by_source.items()}
    assert classed["seat"] == ["confer", "revoke"], classed
    assert classed["claim_landed"] == [] and classed["need"] == [], classed
    other = {s: sorted((c.verb, c.subject) for c in cs if c.verb not in CLASSED)
             for s, cs in by_source.items()}
    assert other["seat"] == other["claim_landed"] == other["need"] and other["seat"], other
    # The non-office referent classes: a rung, a person, the actor. From the mixed sources none
    # forms either verb.
    for s in ("claim_landed", "need"):
        q = Question(f"q:{s}:mix", s, ("D", "S", "p_mid", "p_king", "off_duke"))
        assert not [c for c in _formed(w, "p_king", q) if c.verb in CLASSED], s


def test_in53_b_every_unclassed_row_is_formed_from_every_source():
    """`formed_from` is True for every row that declares no class, whatever the source; the two
    classed rows are formed only from `seat`."""
    rows = 0
    for verb, row in VERB_TABLE.items():
        for s in QUESTION_SOURCES:
            want = verb not in CLASSED or s == "seat"
            assert row.formed_from(s) == want, (verb, s)
            rows += 1
    assert rows == len(VERB_TABLE) * len(QUESTION_SOURCES) and rows > 0
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
