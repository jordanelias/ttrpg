"""v11 CR-28 (G-04 (a), B10-09 close two; CP-T02-05's re-take folded in): THE PROPOSITIONS A PERSON HAS
HEARD OF FROM ANOTHER STAMP AS CLASS `Proposition` -- `queries/world_q.py::propositions_heard`, one more
term appended to `questions_for`'s `added` splice, on `seats_named`' precedent (his own ledger, the World
asked only which ids are Propositions).

What each test can see fail:
  (a) the term: a claim another's act left (an `utter` he witnessed) names the Proposition and the term
      returns it; a claim recording HIS OWN act (`Claim.doer == p.id`, the own-act screen's test) does
      not feed it; a person who heard of none gets `()`; a non-Proposition id the same claim names is
      not returned.
  (b) the stamp: the question he answers carries the heard Proposition as class `Proposition`, and
      `commit` forms on it. PLANTED FAILURE, executed: the term stubbed to `()` and `commit` forms on
      nothing -- the reading REM-23's tree gives (H-156: no `commit` on a heard-of Proposition).
  (c) the decline the failed term lacked: with a live `commit` on the Proposition, `commit` is not
      formed on it (`rosters.yaml: held_edge_declines`, B10-09 close one D3) and `argue` still is.
  (d) DONE: the Candidate, minted as the chooser mints it and folded by the real driver, emits
      `commitment.made` and opens his live `commit` edge on a Proposition another person uttered.
The realm readings (HR-9 controls (2) and (4), `aperture 3 0`) are commit-body readings, never
assertions here.
"""
from engine.season.decision.choose import _payload_of
from engine.season.decision.options import seat_of
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Claim, Proposition

from .test_in53_vacancy_need import _formed, _know
from .test_works_founding import ABSENT, PRESENT, _fold, _kinds, _world

HEARD = "prop_heard"


def _utter_witnessed(w, pid, prop=HEARD, utterer=ABSENT, doer=None, cid="c_heard"):
    """`utterer` uttered `prop` (an OUGHT about himself) and `pid` holds the claim of it -- the deposit a
    witness of the `utter` holds. `doer=pid` makes it the claim of HIS OWN act instead."""
    w.propositions[prop] = Proposition(prop, "OUGHT", utterer, "the strait stays open", True, 0)
    w.persons[pid].ledger.append(Claim(cid, pid, prop, "proposition.uttered", True, w.tick, "firsthand",
                                       100, "own", doer=doer))


def _question(w, pid):
    qs = world_q.questions_for(w, w.persons[pid])
    assert qs, "no question at all: the stamp has nothing to ride"
    return qs[0]


def _commits(w, pid, q):
    return [c for c in _formed(w, pid, q) if c.verb == "commit"]


# --- (a) THE TERM ---------------------------------------------------------------------------------

def test_cr28_a_a_proposition_another_uttered_is_heard_and_nothing_else_is():
    w, _ = _world()
    p = w.persons[PRESENT]
    assert world_q.propositions_heard(w, p) == (), "CONTROL: heard of none at build"
    _utter_witnessed(w, PRESENT)
    # the same ledger also names a person (`ABSENT`) through another claim: not a Proposition, not returned
    p.ledger.append(Claim("c_person", PRESENT, ABSENT, "exists:Person", 1, w.tick, "firsthand", 100, "own"))
    assert world_q.propositions_heard(w, p) == (HEARD,)


def test_cr28_a_the_claim_of_his_own_act_does_not_feed_the_term():
    """The own-act screen's test (`attention_key`, CR-10): the echo of his own deed is not news."""
    w, _ = _world()
    _utter_witnessed(w, PRESENT, utterer=PRESENT, doer=PRESENT)
    assert world_q.propositions_heard(w, w.persons[PRESENT]) == ()
    _utter_witnessed(w, PRESENT, prop="prop_other", cid="c_other")
    assert world_q.propositions_heard(w, w.persons[PRESENT]) == ("prop_other",)


# --- (b) THE STAMP, AND ITS PLANTED FAILURE --------------------------------------------------------

def test_cr28_b_the_heard_proposition_rides_the_answered_question_and_commit_forms_on_it():
    w, _ = _world()
    _utter_witnessed(w, PRESENT)
    q = _question(w, PRESENT)
    assert (HEARD, "Proposition") in q.classes, q
    assert [c.subject for c in _commits(w, PRESENT, q)] == [HEARD]


def test_cr28_b_planted_failure_the_term_returning_nothing_forms_no_commit(monkeypatch):
    """The stamper stubbed to `()`: no question carries the heard Proposition and `commit` forms on
    nothing -- the REM-23 tree's reading, which the test above must not reproduce."""
    w, _ = _world()
    _utter_witnessed(w, PRESENT)
    monkeypatch.setattr(world_q, "propositions_heard", lambda w_, p_: ())
    qs = world_q.questions_for(w, w.persons[PRESENT])
    assert all((HEARD, "Proposition") not in q.classes for q in qs), qs
    assert all(c.subject != HEARD for q in qs for c in _commits(w, PRESENT, q))


# --- (c) THE DECLINE THE FAILED TERM LACKED --------------------------------------------------------

def test_cr28_c_a_cause_he_already_holds_forms_no_commit_and_argue_still_forms():
    w, d = _world()
    _utter_witnessed(w, PRESENT)
    _know(w, PRESENT, ABSENT)                   # `argue` fans its `to` over the persons he knows
    p = w.persons[PRESENT]
    q = _question(w, PRESENT)
    (c,) = _commits(w, PRESENT, q)
    assert _kinds(_fold(w, d, Act("a_commit_heard", p.id, c.verb, payload=_payload_of(c),
                                  via=seat_of(p, c)))) == ["commitment.made"]
    q = _question(w, PRESENT)
    assert (HEARD, "Proposition") in q.classes, "the stamp is not withdrawn: argue still reads it"
    formed = _formed(w, PRESENT, q)
    assert [x for x in formed if x.verb == "commit" and x.subject == HEARD] == []
    assert any(x.verb == "argue" and x.subject == HEARD for x in formed), formed


# --- (d) DONE: THROUGH THE REAL FOLD --------------------------------------------------------------

def test_cr28_d_a_person_commits_to_a_cause_another_uttered_through_the_fold():
    w, d = _world()
    _utter_witnessed(w, PRESENT)
    p = w.persons[PRESENT]

    def live():
        return sorted(t.object for t in p.tenures if t.kind == "commit" and t.live)

    assert HEARD not in live()
    (c,) = _commits(w, PRESENT, _question(w, PRESENT))
    out = _fold(w, d, Act("a_commit_heard", p.id, c.verb, payload=_payload_of(c), via=seat_of(p, c)))
    assert _kinds(out) == ["commitment.made"]
    assert HEARD in live() and w.propositions[HEARD].subject == ABSENT
