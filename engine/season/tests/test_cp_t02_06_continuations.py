"""v10 CP-T02-06 (B10-10; M7 taken (b), `continuation_ties: [heir_title, sworn]`): THE SEATED PERSON'S LINE
CONTINUES, OR ENDS. Player half only (R-WORLD is IN-61's).

  * `rosters.yaml: continuation_ties` is a closed ORDERED roster, read by `world_q.continuations` (the Query on
    the living) and by nothing in the client; `harness/play_surface.py::carry_on` is the client's re-bind on the
    existing `overrides` seam: when the seated person dies it OFFERS the living members of his last reading, in
    roster order, and binds the callback to the one the PLAYER chose (scripted here, as the play surface's other
    choices are). None alive: the line is extinct, exactly as for an empty reading.

FALSIFIER (the entry's): a seated person dies in the same season as his one sworn retainer, a second tie alive:
the client offers the second; none alive, the run ends. Also: the offer is in `continuation_ties` order
(`heir_title` before `sworn`); an unrostered tie kind is REFUSED. PLANTED FAILURE (run at build, reverted): the
Query iterating `_TIE_READERS` (declared sworn-first) instead of the roster reddens
`test_the_reading_is_in_continuation_ties_order` and the three tests that read heir_title before sworn, and
`test_the_roster_not_the_reader_table_fixes_the_order` (its table is declared heir-first, the roster sworn-first).
CONTROL: no seated person dies in a run -> `carry_on` touches nothing and `build_realm(s)` after 1 season equals
the pre-build hash (`test_rem30_character_sheet.py::PRE_BUILD`, the same three pins).
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..decision import make_chooser
from ..gaps import Forbidden, Unspecified
from ..harness.heir_hears import HEIR_SEAT, THRONE
from ..harness.heir_hears import holder as _holder
from ..harness.play_surface import carry_on, dispatching_chooser
from ..harness.populated import build_realm
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.matter import _die
from ..queries import world_q
from ..state.carriers import Tenure
from ..state.ids import H, draw_factory

# Re-recorded by CR-33 (it lands after this item, in one batch): carin's `capability` now holds {inquiry: 2},
# so every Person repr moved. Old (this item's own commit) -> new:
#   f2e5e265012d1d96333a43ff514d2b13 -> 69783660ea3ca2163bd346ee7e29e711
#   0d25717b85d52c4f156136fa724ae46e -> d81d7a7377008ddbe4000624e259f4b2
#   05f065f4c917faf3d970f2c50cfd792f -> 43d2c5249670a51c24c1a102517e9567
# the same three pins as `test_rem30_character_sheet.py::PRE_BUILD`.
PRE_BUILD = {0: "69783660ea3ca2163bd346ee7e29e711",
             1: "d81d7a7377008ddbe4000624e259f4b2",
             2: "9ab1a7492246bf0ae324f4c0cfb65bdf"}  # CR-33 verify pass (NPC-004's `lifepath: 3-CH5` holds `inquiry`, a Person repr): was 43d2c524... (seeds 0 and 1: NPC-004 has left the world by season 1)


def _realm(retainers=2):
    """The realm at seed 0: the throne's holder, the heir-title's holder, and `retainers` other persons sworn
    (a live `oblige`) to the throne. Returns `(w, king, heir, [retainer ids])`."""
    w = build_realm(0)
    king, heir = _holder(w, THRONE), _holder(w, HEIR_SEAT)
    assert king and heir and king != heir, "fixture: no distinct throne-holder and heir"
    for t in w.tenures:                  # the realm ships three sworn retainers: end them, so each arm sets its own
        if t.kind == "oblige" and t.live and any(t.object == h.object for h in w.seat_holds(king)):
            t.until = w.tick
    others = [pid for pid in sorted(w.persons) if pid not in (king, heir)][:retainers]
    assert len(others) == retainers
    for i, pid in enumerate(others):
        w.add_tenure(Tenure(f"t_cp0206_sworn_{i}", pid, THRONE, "oblige", w.tick))
    return w, king, heir, others


def _kill(w, *ids):
    w.step = Step.MATTER
    w._emitted_by_write = []
    for pid in ids:
        _die(w, mint_token(w, WriteClass.MATTER), pid)
        assert pid not in w.persons


def _cb(p, v, s, ask_budget, auto):
    return auto(p, v, s, ask_budget)


def _ties(reading):
    return [c.tie for c in reading]


def _in_roster_order(**counts):
    """The tie kinds a reading of `counts` (kind -> how many) must show: each ROSTER member that many times,
    in `world_q.CONTINUATION_TIES` order as bound NOW (a test may patch it). No second list of kinds here."""
    assert set(counts) <= set(world_q.CONTINUATION_TIES)
    return [t for t in world_q.CONTINUATION_TIES for _ in range(counts.get(t, 0))]


# --- THE QUERY -----------------------------------------------------------------------------------

def test_the_reading_is_in_continuation_ties_order():
    """The heir (`heir_title`) is read BEFORE both retainers (`sworn`), though `_TIE_READERS` is declared
    sworn-first and the retainers' edges were added before anything else: the roster fixes the order."""
    w, king, heir, sworn = _realm()
    reading = world_q.continuations(w, w.persons[king])
    assert _ties(reading) == _in_roster_order(heir_title=1, sworn=2), reading
    assert _ties(reading)[0] == "heir_title", "the roster puts heir_title first"
    assert reading[0].person == heir and {c.person for c in reading[1:]} == set(sworn)


def test_the_shipped_realm_reads_the_heir_then_its_sworn():
    """Unmodified `build_realm(0)`: the King's heir first, then the retainers already sworn to his seats."""
    w = build_realm(0)
    king = _holder(w, THRONE)
    reading = world_q.continuations(w, w.persons[king])
    assert _ties(reading)[0] == "heir_title" and set(_ties(reading)[1:]) == {"sworn"} and len(reading) >= 2, reading


def test_the_roster_not_the_reader_table_fixes_the_order(monkeypatch):
    """The reader table declared heir-first and the roster sworn-first: the read is sworn first, so
    `continuation_ties` is the order's owner and the table's own order is not."""
    w, king, heir, sworn = _realm()
    monkeypatch.setattr(world_q, "_TIE_READERS", {"heir_title": world_q._heir_title_holders,
                                                  "sworn": world_q._sworn_retainers})
    monkeypatch.setattr(world_q, "CONTINUATION_TIES", ("sworn", "heir_title"))
    assert _ties(world_q.continuations(w, w.persons[king])) == _in_roster_order(heir_title=1, sworn=2)
    assert world_q.CONTINUATION_TIES[0] == "sworn"


def test_a_person_who_is_both_heir_and_sworn_is_read_once_at_the_earlier_tie():
    w, king, heir, sworn = _realm(retainers=1)
    w.add_tenure(Tenure("t_cp0206_heir_sworn", heir, THRONE, "oblige", w.tick))
    reading = world_q.continuations(w, w.persons[king])
    assert [(c.tie, c.person) for c in reading] == [("heir_title", heir), ("sworn", sworn[0])], reading


def test_the_query_reads_the_living_only_and_writes_nothing():
    w, king, heir, sworn = _realm()
    before = w.content_hash()
    p = w.persons[king]
    assert world_q.continuations(w, p)
    assert w.content_hash() == before, "the Query wrote"
    _kill(w, heir)
    assert [c.person for c in world_q.continuations(w, p)] == sworn or \
        {c.person for c in world_q.continuations(w, p)} == set(sworn)
    assert heir not in {c.person for c in world_q.continuations(w, p)}
    _kill(w, king)
    assert world_q.continuations(w, p) == (), "a dead person's own edges leave the view: the client keeps its last reading"


def test_a_person_with_no_ties_reads_nothing():
    w, king, heir, sworn = _realm(retainers=0)
    _kill(w, heir)
    assert world_q.continuations(w, w.persons[king]) == ()


# --- THE ROSTER IS CLOSED ------------------------------------------------------------------------

def test_an_unrostered_tie_kind_is_refused():
    with pytest.raises(Unspecified):
        world_q._continuation("follower", "p_x")
    assert world_q._continuation("sworn", "p_x").tie == "sworn"


def test_a_roster_member_with_no_reader_and_a_reader_with_no_member_are_refused(monkeypatch):
    world_q.check_continuation_ties()
    monkeypatch.setattr(world_q, "CONTINUATION_TIES", ("heir_title", "sworn", "follower"))
    with pytest.raises(Unspecified):
        world_q.check_continuation_ties()
    monkeypatch.setattr(world_q, "CONTINUATION_TIES", ("heir_title",))
    with pytest.raises(Unspecified):
        world_q.check_continuation_ties()


# --- THE RE-BIND (the entry's falsifier) ---------------------------------------------------------

def test_the_seated_person_dies_with_his_one_sworn_retainer_and_the_client_offers_the_second_tie():
    """The king dies in the same season as his one sworn retainer; the heir is alive: the offer is the heir,
    the retainer is not in it, and the callback moves to the heir."""
    w, king, heir, sworn = _realm(retainers=1)
    overrides = {king: _cb}
    now, last = carry_on(w, overrides, king, (), None)
    assert now == king and len(last) == 2
    _kill(w, king, sworn[0])
    offered = []
    now, reading = carry_on(w, overrides, king, last, lambda offer: offered.append(offer) or offer[0])
    assert [(c.tie, c.person) for c in offered[0]] == [("heir_title", heir)], offered
    assert now == heir and overrides == {heir: _cb}, overrides
    assert reading == world_q.continuations(w, w.persons[heir])


def test_the_choice_is_the_players_not_the_first_tie():
    """Two ties alive: the pick scripted to take the LAST binds to it, and the offer was whole and ordered."""
    w, king, heir, sworn = _realm(retainers=2)
    overrides = {king: _cb}
    _, last = carry_on(w, overrides, king, (), None)
    _kill(w, king)
    seen = []
    now, _ = carry_on(w, overrides, king, last, lambda offer: seen.append(_ties(offer)) or offer[-1])
    assert seen == [_in_roster_order(heir_title=1, sworn=2)]
    assert now == last[-1].person and list(overrides) == [now]


def test_with_no_tie_alive_the_line_is_extinct_and_the_callback_is_dropped():
    w, king, heir, sworn = _realm(retainers=1)
    overrides = {king: _cb}
    _, last = carry_on(w, overrides, king, (), None)
    assert last
    _kill(w, king, heir, sworn[0])
    now, reading = carry_on(w, overrides, king, last, lambda offer: pytest.fail("offered a dead tie"))
    assert (now, reading) == (None, ()) and overrides == {}


def test_an_empty_last_reading_is_extinct_exactly_the_same():
    w, king, heir, sworn = _realm(retainers=0)
    _kill(w, heir)
    overrides = {king: _cb}
    _, last = carry_on(w, overrides, king, (), None)
    assert last == ()
    _kill(w, king)
    assert carry_on(w, overrides, king, last, lambda offer: pytest.fail("offered")) == (None, ())
    assert overrides == {}


def test_a_choice_outside_the_offer_is_refused():
    w, king, heir, sworn = _realm(retainers=1)
    overrides = {king: _cb}
    _, last = carry_on(w, overrides, king, (), None)
    _kill(w, king)
    with pytest.raises(Forbidden):
        carry_on(w, overrides, king, last, lambda offer: world_q.Continuation("sworn", "p_nobody"))


def test_the_rebound_callback_plays_the_successor_through_a_real_season():
    """The seam end to end: after the re-bind the NEXT season's DELIBERATE calls the callback for the heir."""
    w, king, heir, sworn = _realm(retainers=0)
    called = []

    def cb(p, v, s, ask_budget, auto):
        called.append(p.id)
        return auto(p, v, s, ask_budget)

    overrides = {king: cb}
    _, last = carry_on(w, overrides, king, (), None)
    _kill(w, king)
    now, _ = carry_on(w, overrides, king, last, lambda offer: offer[0])
    assert now == heir
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    SeasonDriver(w).season(dispatching_chooser(auto, overrides), None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert heir in called and king not in called, called


# --- THE CONTROL ---------------------------------------------------------------------------------

@pytest.mark.parametrize("seed", sorted(PRE_BUILD))
def test_no_death_means_no_behaviour_change_and_the_realm_hash_is_the_pre_build_hash(seed):
    w = build_realm(seed)
    king = _holder(w, THRONE)
    calls = []

    def cb(p, v, s, ask_budget, auto):
        calls.append(p.id)
        return auto(p, v, s, ask_budget)

    overrides = {king: cb}
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    choose = dispatching_chooser(auto, overrides)
    last = ()
    now, last = carry_on(w, overrides, king, last, None)
    SeasonDriver(w).season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert king in w.persons, "the control needs the seated person to live"
    now, last = carry_on(w, overrides, king, last, lambda offer: pytest.fail("rebound with no death"))
    assert now == king and overrides == {king: cb} and calls, "carry_on touched a run with no death"
    assert w.content_hash() == PRE_BUILD[seed]
