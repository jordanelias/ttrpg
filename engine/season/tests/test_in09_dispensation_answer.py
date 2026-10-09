"""Plan position IN-09 (`19b`, U7-disp) -- `comply`, `evade / defy` and `construe`, the three acts that
answer a dispensation, typed on THE HELD WRIT (J-2 arm A, one `evade / defy` row).

What each block proves, and the control that stops it passing vacuously:

  1. THE ROWS. Each of the three is in `resolvable_verbs()`: a typed cell the fold evaluates and no
     write, so no effect is owed (`VerbRow.effect_carried`) -- the rows are EMISSION-ONLY (#453
     `:502`), and none carries an `EFFECTS` entry the fold would never call.
  2. THE CARRIED FALSIFIER, THROUGH THE REAL FOLD: `comply` evaluable for a person whose ledger holds
     no claim of the terms -> FAIL. The actor HOLDS the writ (so only the ledger conjunct can refuse),
     and with no claim on it the act is refused `compliance.impossible`; control: the same act after
     his own `content:dispensation` claim lands emits `compliance.given`. `evade / defy` is the same
     cell (*as `comply`*) and is asserted the same way.
  3. THE WRIT CONJUNCT. A claim on something that is NOT a dispensation -- a person -- admits none of
     the three, so compliance is never published about a person or a rung.
  4. `construe` IS THE HOLDER'S OWN READING. A person who holds a claim on the writ but not the writ
     is refused `construal.impossible`; the holder construes (`terms.distorted`).
  5. PERSON-SIDE FORMATION. A question about the writ forms all three Candidates for its holder, with
     `subject` the writ -- the computed-play route the aperture reads (the EXIT).

The EXIT's other half -- each of the three EXECUTING >= 1 in `python -m engine.season.harness.aperture
4 0` -- is a 10-minute realm run and is read at the position's close, not in this file.
"""
import pytest

from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import RECORD_CONTENT
from engine.season.data.verbs import VERB_TABLE
from engine.season.decision.options import opening_set
from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.loop.effects import EFFECTS
from engine.season.loop.witness import content_value
from engine.season.queries.world_q import hold_force
from engine.season.state.carriers import Act, Claim, Question, View

THREE = ("comply", "evade / defy", "construe")
HOLDER, OTHER = "p_low", "p_mid"                  # `tiny_world`: both in Hh
WRIT = "rec_writ"
_CONTENT = RECORD_CONTENT["predicate"]
TERMS = {"terms": OTHER, "to": [HOLDER], "at": None}


def _with_writ():
    """`tiny_world` at a RESOLVE barrier, with `HOLDER` holding a `dispensation` Record minted
    through the real fold (`create_record` declaring the kind: the one mint `issue` shares). No
    claim on it is in anyone's ledger yet -- WITNESS has not run."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    w.step = Step.RESOLVE
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id="mk", actor=HOLDER, verb="create_record",
                      payload={"record": WRIT, "kind": "dispensation", "subject_matter": TERMS}))
    assert [e.kind for e in out] == ["record.created"], [e.kind for e in out]
    assert w.records[WRIT].kind == "dispensation", "fixture: the writ is not a dispensation"
    assert hold_force(w, WRIT).subject == HOLDER, "fixture: the maker does not hold the writ"
    return w, d


def _claim(w, pid, subject, predicate, value, cid):
    w.persons[pid].ledger.append(
        Claim(cid, pid, subject, predicate, value, w.tick, "firsthand", 100, "own"))


def _read_terms(w, pid):
    """The holder's own `content:dispensation` claim -- the deposit WITNESS makes for a new holder."""
    _claim(w, pid, WRIT, f"{_CONTENT}:dispensation", content_value(w.records[WRIT].subject_matter),
           f"c_terms_{pid}")


def _fold(w, d, actor, verb, subject, key):
    return [e.kind for e in d._fold(w, mint_token(w, WriteClass.ACTS),
                                    Act(id=f"{key}", actor=actor, verb=verb,
                                        payload={"subject": subject}))]


def _ledger_on(w, pid, subject):
    return [c for c in w.persons[pid].ledger if c.subject == subject]


# ======================================================================================
# 1. THE ROWS
# ======================================================================================

@pytest.mark.parametrize("verb", THREE)
def test_in09_each_row_is_typed_resolvable_and_emission_only(verb):
    row = VERB_TABLE[verb]
    assert row.requires_typed is not None, f"{verb}: the cell is still untyped"
    assert not row.requires_decline_note, f"{verb}: a stale `requires_decline_note:`"
    assert verb in resolvable_verbs(), f"{verb}: the fold still cannot carry it"
    assert row.writes == (), f"{verb}: declares writes {row.writes} -- not emission-only"
    assert verb not in EFFECTS, f"{verb}: an effect the fold never calls (`ID-13`)"


# ======================================================================================
# 2. THE CARRIED FALSIFIER
# ======================================================================================

@pytest.mark.parametrize("verb,given", [("comply", "compliance.given"),
                                        ("evade / defy", "compliance.withheld")])
def test_in09_falsifier_no_claim_of_the_terms_refuses_and_holding_one_admits(verb, given):
    """THE CARRIED FALSIFIER: *`comply` evaluable for a person whose ledger holds no claim of the
    terms -> fail*. The actor holds the writ and it IS a dispensation, so the one conjunct left to
    refuse is the ledger's -- and it does."""
    w, d = _with_writ()
    assert _ledger_on(w, HOLDER, WRIT) == [], "fixture: the holder already holds a claim on the writ"
    refused = _fold(w, d, HOLDER, verb, WRIT, "a1")
    assert refused == ["compliance.impossible"], (
        f"{verb} admitted for a person whose ledger holds no claim of the terms: {refused}")
    _read_terms(w, HOLDER)
    admitted = _fold(w, d, HOLDER, verb, WRIT, "a2")
    assert admitted == [given], f"control: {verb} with the terms in hand emitted {admitted}"


# ======================================================================================
# 3. THE WRIT CONJUNCT
# ======================================================================================

@pytest.mark.parametrize("verb,refusal", [("comply", "compliance.impossible"),
                                          ("evade / defy", "compliance.impossible"),
                                          ("construe", "construal.impossible")])
def test_in09_a_claim_on_a_person_answers_no_writ(verb, refusal):
    w, d = _with_writ()
    _claim(w, HOLDER, OTHER, "exists:Person", 1, "c_person")
    assert _ledger_on(w, HOLDER, OTHER), "fixture: no claim on the person"
    assert _fold(w, d, HOLDER, verb, OTHER, "p1") == [refusal]


# ======================================================================================
# 4. CONSTRUE IS THE HOLDER'S OWN READING
# ======================================================================================

def test_in09_construe_is_refused_to_a_non_holder_and_admitted_to_the_holder():
    w, d = _with_writ()
    _read_terms(w, OTHER)                         # OTHER knows the terms and does not hold the writ
    _read_terms(w, HOLDER)
    assert _fold(w, d, OTHER, "construe", WRIT, "c1") == ["construal.impossible"]
    assert _fold(w, d, HOLDER, "construe", WRIT, "c2") == ["terms.distorted"]
    # and `comply` does not ask for the writ in hand: knowing its terms is the whole requirement
    assert _fold(w, d, OTHER, "comply", WRIT, "c3") == ["compliance.given"]


# ======================================================================================
# 5. PERSON-SIDE FORMATION
# ======================================================================================

def test_in09_a_question_about_the_writ_forms_all_three_for_its_holder():
    w, _d = _with_writ()
    _read_terms(w, HOLDER)
    p = w.persons[HOLDER]
    c = _ledger_on(w, HOLDER, WRIT)[0]
    q = Question(f"q:claim:{c.id}", "claim_landed", (WRIT,), c.id)
    view = View(HOLDER, [], w.fixtures.get("view_k"))
    got = {(x.verb, x.subject) for x in opening_set(p, view, q, w.fixtures)}
    for verb in THREE:
        assert (verb, WRIT) in got, f"{verb} formed no Candidate on the held writ: {sorted(got)}"
