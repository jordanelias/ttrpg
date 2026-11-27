"""B34.12 (`16_PESSIMIST_GO` §4, gate 4): what a creation row marks. The seat-holder-from-ledger items of B34 (B34.23, B34.24) land their tests here."""
from __future__ import annotations

import pytest

from ..boot.realm import build_realm
from ..decision.sheet import creation_sheet
from ..harness.play_surface import holdings_of
from ..queries import person_q, world_q

#: the goal and asker of the B34.23 pair: `goal_restoration_evade_capture` is a `seat_holders` goal over two seats, `p_npc_088` holds it
_GOAL, _ASKER = "goal_restoration_evade_capture", "p_npc_088"


@pytest.fixture(scope="module")
def realm():
    return build_realm(0)


def _need_questions(w, p):
    return [q for q in world_q.questions_for(w, p) if q.source == "need" and q.about == _GOAL]


def test_creation_sheet_marks_cohorts_and_holdings():
    """`creation_sheet` at seed 0: a row's `cohort` is its person's `Person.is_cohort`, so as many rows are marked as the world seats cohorts, and
    the cohorts are neither all of the rows nor none. The holdings half of the gate (the Inquisitor's `("hold", "off_senior_inquisitor")`, a person
    with no seat showing no `hold`) is `test_season_shape.py::test_creation_sheet_shows_holdings_for_a_seat_holder`; here it is read again only
    to say the marked column and the held column are one row's, not two sheets."""
    w = build_realm(0)
    rows = creation_sheet(w.persons.values(), holdings_of(w))
    marked = sum(r.cohort for r in rows)
    assert marked == sum(p.is_cohort for p in w.persons.values())
    assert 0 < marked < len(rows), f"setup: {marked} of {len(rows)} rows are cohorts, so the column cannot show a difference"
    checked = 0
    for r in rows:
        assert r.cohort is w.persons[r.id].is_cohort, f"{r.id}: the row says cohort={r.cohort}, the person says {w.persons[r.id].is_cohort}"
        checked += 1
    assert checked == len(rows) == len(w.persons)
    # a cohort holds no seat (`state/gate.py`: a population is no officeholder), so a marked row shows no `hold`; the Inquisitor's row is no cohort
    assert not any(kind == "hold" for r in rows if r.cohort for kind, _ in r.holdings)
    inquisitor = next(r for r in rows if r.id == "p_npc_004")
    assert not inquisitor.cohort and ("hold", "off_senior_inquisitor") in inquisitor.holdings


def test_goal_referent_reads_own_ledger(realm):
    """B34.23 (`16_PESSIMIST_GO` §1, gate 1): a `seat_holders` goal's referents are the persons the ASKER'S OWN ledger names as holding a listed seat, not the
    live `hold`s. At build the two agree (`seed_seat_news` tells every person every seat); then the world moves one holder out of his seat and the referents
    do not follow it, and the ledger loses a seat and they do."""
    w, p, prop = realm, realm.persons[_ASKER], realm.propositions[_GOAL]
    seats = tuple(prop.scope)
    from_ledger = tuple(dict.fromkeys(h for s in seats for h in person_q.holders_named(p.ledger, s)))
    world_holders = tuple(t.subject for s in seats for t in w.tenures if t.kind == "hold" and t.live and t.object == s)
    refs = world_q.goal_referents(w, p, prop)
    assert len(seats) == 2 and refs == from_ledger == world_holders and len(refs) == 2, f"setup: {refs} / {from_ledger} / {world_holders}"
    gone = next(t for t in w.tenures if t.kind == "hold" and t.live and t.object == seats[0])
    try:
        gone.until = w.tick                          # the world says the first seat has changed hands; he has not been told
        assert world_q.goal_referents(w, p, prop) == refs
    finally:
        gone.until = None
    kept = p.ledger
    try:
        p.ledger = [c for c in kept if c.subject != seats[0]]   # he holds no claim on the first seat: it contributes nobody
        assert world_q.goal_referents(w, p, prop) == refs[1:]
    finally:
        p.ledger = kept
    assert world_q.goal_referents(w, p, prop) == refs


def test_unheard_holder_forms_no_question_until_a_deposit_names_him(realm):
    """B34.23 (gate 2): with no claim of any seat changing hands in his ledger the goal names nobody and forms no `need` question; the claims a witness of
    the seat's opening deposits (the seat's and the holder's, one `(when, lap)`) name him, and the question forms about him."""
    w, p, prop = realm, realm.persons[_ASKER], realm.propositions[_GOAL]
    seat = prop.scope[0]
    kept = p.ledger
    opening = {(c.when, c.lap) for c in kept if c.subject == seat and c.predicate in person_q.HOLD_OPEN_KINDS}
    deposit = [c for c in kept if c.predicate in person_q.HOLD_OPEN_KINDS and (c.when, c.lap) in opening]
    assert len(deposit) == 2 and _need_questions(w, p), "setup: the seat's opening is two claims and the goal forms a question on the built ledger"
    try:
        p.ledger = [c for c in kept if c.predicate not in person_q.HOLD_OPEN_KINDS]
        assert world_q.goal_referents(w, p, prop) == () and _need_questions(w, p) == []
        p.ledger = p.ledger + deposit
        (q,) = _need_questions(w, p)
        holder = next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == seat)
        assert tuple(q.referents) == (holder,)
    finally:
        p.ledger = kept
