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
    live `hold`s. At build the two agree at seed 0 (the asker drew both seats: `seed_seat_news` gates a goal-named seat by a draw, B34.24); then the world moves one holder out of his seat and the referents
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


# -- B34.24 (`16_PESSIMIST_GO` §2, gates 2 and 3): who knows a goal-named seat's holder at build is a keyed draw ----------------------------

#: the three classes of `Fixtures holder_known_chance`, each at 1.0: the revert arm, which must reproduce the ungated seed
_ALL_ONE = {"same_settlement": 1.0, "same_faction_or_goal": 1.0, "elsewhere": 1.0}


def _need_rows(w) -> set:
    """Every `need` question `questions_for` returns for every person, as `(person, about, referents)`."""
    return {(pid, q.about, tuple(q.referents)) for pid, p in sorted(w.persons.items())
            for q in world_q.questions_for(w, p) if q.source == "need"}


def _seat_claims(w) -> set:
    return {(c.holder, c.id, c.subject, c.when, c.lap) for p in w.persons.values() for c in p.ledger if c.id.startswith("c_seat_")}


def test_all_chances_one_reproduces_todays_referents(monkeypatch):
    """Gate 2, the control: with every `holder_known_chance` at 1.0 the seat news deposited at build, and so the `need` questions and their
    referents every person forms at tick 0, equal today's -- `seed_seat_news` with no seat gated (`goal_named_seats` answering none, which is
    the code path every seat no goal names keeps). The shipped chances must differ from it, or the equality could not have seen a draw."""
    from ..boot import realm as realm_mod
    from ..data.fixtures import DEFAULT_FIXTURES
    ones = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("holder_known_chance", dict(_ALL_ONE)))
    shipped = build_realm(0)
    with monkeypatch.context() as m:
        m.setattr(realm_mod, "goal_named_seats", lambda w: {})
        today = build_realm(0)
    assert realm_mod.goal_named_seats(shipped), "setup: some loaded goal names a seat, so the gate has seats to draw on"
    assert _seat_claims(ones) == _seat_claims(today)
    rows = _need_rows(ones)
    assert rows == _need_rows(today) and len({pid for pid, _, _ in rows}) >= 30, f"setup: {len(rows)} need rows"
    assert _seat_claims(shipped) < _seat_claims(today), "the shipped chances deposited every claim the ungated seed does: the draw is decoration"
    assert _need_rows(shipped) != rows


def _seat_goals(w) -> dict:
    """`{goal id: its seats}` for every loaded goal of object kind `seat_holders` the world minted."""
    from ..data import goals as goals_data
    return {g.id: tuple(w.propositions[g.id].scope) for g in goals_data.goals()
            if g.object["kind"] == "seat_holders" and g.id in w.propositions}


def _unheard(w) -> tuple:
    """`(askers, unheard)`: the persons committed to a `seat_holders` goal, and those of them holding no claim naming a holder of any of one
    such goal's seats (`person_q.holders_named`, the reader the goal's referents are), each as `(person, goal)`."""
    goals = _seat_goals(w)
    commits = [(t.subject, t.object) for t in w.tenures if t.kind == "commit" and t.live and t.object in goals and t.subject in w.persons]
    askers = {pid for pid, _ in commits}
    unheard = sorted({(pid, g) for pid, g in commits
                      if not any(person_q.holders_named(w.persons[pid].ledger, s) for s in goals[g])})
    return askers, unheard


def test_shipped_chances_leave_some_unheard():
    """Gate 3, its build half: at the shipped chances, over seeds 0-9, the share of persons with a `seat_holders` goal who hold no claim on any of
    one such goal's seats is neither 0 nor more than a quarter (the draw is a draw, and ambition does not die), and every such person forms no
    `need` question on that goal at tick 0 (an unheard seat names nobody). The run half (one of them forms it within two seasons, after a deposit
    names the holder) is not met on this tree and is not asserted here: `hole_register.yaml` H-758's `cite:` holds the reading."""
    asked = checked = 0
    unheard_persons = set()
    for seed in range(10):
        w = build_realm(seed)
        askers, unheard = _unheard(w)
        asked += len(askers)
        unheard_persons |= {(seed, pid) for pid, _ in unheard}
        for pid, g in unheard:
            assert not [q for q in world_q.questions_for(w, w.persons[pid]) if q.source == "need" and q.about == g], f"seed {seed}: {pid} on {g}"
            checked += 1
    assert asked >= 200, f"setup: {asked} askers over ten seeds"
    assert checked >= len(unheard_persons), "the loop asserted on every unheard person"
    assert 0 < len(unheard_persons) <= asked / 4, (
        f"{len(unheard_persons)} of {asked} persons with a seat_holders goal heard of none of one goal's seats at build")
