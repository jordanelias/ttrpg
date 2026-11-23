"""B11.08 (`08_FI_01` edits 1-6, `08_FI_02` edit 5, `16_PESSIMIST_FI_C` edit 4) -- REFERENTS ABOUT OTHER PEOPLE COME FROM THE ASKER'S OWN LEDGER.

`queries/world_q.py::questions_for` stopped handing a person referents read from another person's or seat's current state: a seat's holder
(`_goal_referents`), a vacancy (`vacancies`), a met aim (`aim_state`), a docketed matter (`matters_awaiting`), and whether a claim's person
subject still exists or where he is (the claim loop). Each pair below is two realms (`build_realm(0)`) that differ ONLY by an edit made
on the World with no Event and no WITNESS, so the subject's ledger and own edges are identical in both; his candidates (`opening_set` over
every question `questions_for` gives him) must be too. The positive arms are the same change made by the real fold and the real WITNESS.

⚠ THE BOUND OF `test_a_silent_death_removes_no_candidate`, STATED: the rows that declare a `referent_class` (`capture`, `tend`, `open_case`,
`petition`, `dispatch` on the dead man) form on a referent only when `World.class_of` stamps it (`_of_stamped_class`, REM-21), and a person the
world no longer holds has no class. That stamp is another world read and is not this item's; the test compares the questions and the
candidates of the rows with no class.
"""
from __future__ import annotations

import pytest

from ..boot.realm import build_realm
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set
from ..epistemic import SEEN_PREDICATE, Seen
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..queries.person_q import holders_named, known_persons, vacant_named
from ..state.carriers import Act, Claim

KING = "p_npc_020"
SEAT = "off_archbishops_rep"        # the King may fill it (`may_fill` through `off_king`)


def hears_of(person, obj, holder, kind="tenure.opened", when=0, lap=0) -> None:
    """`person` HAS HEARD that `holder` came to hold (or, `kind="tenure.closed"`, ceased to hold) `obj`: the two claims a witness of it
    deposits, about the holder and about the seat (`epistemic.claim_subjects`, `per_change`), at one `(when, lap)`. For a hand-built
    world whose person is to be told what the real WITNESS would have told him (v12 B11.08: his referents and vacancies are his ledger's)."""
    for n, subject in enumerate((holder, obj)):
        person.ledger.append(Claim(f"c_heard_{person.id}_{obj}_{kind}_{when}_{lap}_{n}", person.id, subject, kind, True, when,
                                   "told_by", 100, "own", lap))


def _candidates(w, pid, classless=False) -> frozenset:
    """EVERY CANDIDATE `pid` FORMS ON EVERY QUESTION `questions_for` GIVES HIM, `(verb, subject, operands)`; `classless` keeps the rows
    that declare no `referent_class` (their formation reads no `World.class_of` stamp)."""
    p = w.persons[pid]
    out = set()
    for q in world_q.questions_for(w, p):
        for c in opening_set(p, assemble(p, q, 12), q, w.fixtures):
            if not classless or VERB_TABLE[c.verb].referent_class is None:
                out.add((c.verb, c.subject, tuple(sorted((c.operands or {}).items()))))
    return frozenset(out)


def _question_ids(w, pid) -> frozenset:
    return frozenset(q.id for q in world_q.questions_for(w, w.persons[pid]))


def _knowers(w, x) -> list:
    return sorted(pid for pid, p in w.persons.items() if pid != x and x in known_persons(p.ledger, pid))


def _silently_gone(w, x) -> None:
    """`x` stops existing on the World with no Event: his edges close, he and his person-kind rung leave the stores."""
    for t in list(w.tenures):
        if t.object == x and t.live:
            t.until = w.tick
    w.persons.pop(x)
    w.rungs.pop(x, None)


def _silently_moved(w, x, to) -> None:
    for t in w.tenures:
        if t.subject == x and t.kind == "contain" and t.live:
            t.object = to


def _silently_vacated(w, seat) -> None:
    for t in w.tenures:
        if t.kind == "hold" and t.live and t.object == seat:
            t.until = w.tick


def _holder(w, seat) -> str:
    return next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == seat)


def _released_through_the_fold(w, seat) -> set:
    """The seat's holder releases it through the real fold and the real WITNESS; returns the kinds the fold emitted."""
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id="rel_seat", actor=_holder(w, seat), verb="release", payload={"subject": seat})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return {e.kind for e in out}


def test_a_silent_death_removes_no_candidate():
    """`p1_belief.py` `dead-silent`: the King deleted on the World with no Event; every person who knows him holds the same ledger, so
    the same questions and the same candidates (the class-stamped rows aside, the module docstring)."""
    control, dead = build_realm(0), build_realm(0)
    _silently_gone(dead, KING)
    assert KING not in dead.persons and KING in control.persons
    knowers = _knowers(control, KING)
    checked = 0
    for s in knowers:
        assert _question_ids(dead, s) == _question_ids(control, s), s
        assert _candidates(dead, s, classless=True) == _candidates(control, s, classless=True), s
        checked += any(KING in q.referents for q in world_q.questions_for(control, control.persons[s]))
    assert len(knowers) >= 10 and checked >= 10, (len(knowers), checked)        # the pair is not vacuous: he is asked about the King


def test_who_is_where_is_read_from_the_askers_ledger():
    """`p1d_where.py`: the King moved to a hearth nobody lives at, outside his own territory, on the World alone; nobody who knows him has his candidates move."""
    control, moved = build_realm(0), build_realm(0)
    homes = world_q.home_of(control)
    territory = next(r for r in world_q.ancestry(control, homes[KING]) if control.rungs[r].kind == "territory")
    to = next(r.id for r in sorted(control.rungs.values(), key=lambda r: r.id)
              if r.kind == "hearth" and r.id not in set(homes.values()) and territory not in world_q.ancestry(control, r.id))
    _silently_moved(moved, KING, to)
    assert world_q.home_of(moved)[KING] == to != world_q.home_of(control)[KING]
    knowers = _knowers(control, KING)
    for s in knowers:
        assert _candidates(moved, s) == _candidates(control, s), s
    assert sum(len(_candidates(control, s)) for s in knowers) > 0


def test_a_witnessed_change_does_move_the_candidates():
    """The positive arms, green before and after: the same seat vacated by the real fold moves the King's candidates and names the seat
    vacant to him; a man told that somebody is gone is no longer offered acts on him."""
    base = build_realm(0)
    assert SEAT in world_q.seats_named(base, base.persons[KING]) and SEAT not in world_q.vacancies(base, base.persons[KING])
    heard = build_realm(0)
    assert _released_through_the_fold(heard, SEAT) == {"tenure.closed"}
    k = heard.persons[KING]
    assert vacant_named(k.ledger, SEAT) and not vacant_named(base.persons[KING].ledger, SEAT)
    assert world_q.vacancies(heard, k) == (SEAT,)
    assert _candidates(heard, KING) != _candidates(base, KING)
    # refused the King: a falsy `exists:Person` claim newer than the acquaintance he holds of him (`when` 1 beats the build's 0, as a refusal
    # deposited in play beats it), and the acts whose cell asks that the subject exist (`interview`) decline on him
    s = "p_npc_036"
    told = build_realm(0)
    told.persons[s].ledger.append(Claim("c_told_gone", s, KING, "exists:Person", False, 1, "firsthand", 100, "own"))
    before, after = _candidates(base, s), _candidates(told, s)
    on_king = lambda cs: {c[0] for c in cs if c[1] == KING}
    assert "interview" in on_king(before) and "interview" not in on_king(after) and after != before


def test_the_realm_starts_with_seat_news():
    """`seed_seat_news`: every person the realm reaches holds who sits each seat that has a rung, as the seat's own claims name him, and
    holds nobody for a seat in another realm; `seat_news: local` (A-32's arm B) seeds the same seats of his own realm."""
    local = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("seat_news", "local"))
    shipped = build_realm(0)
    homes = world_q.home_of(shipped)
    checked = 0
    for w in (shipped, local):
        assert len(w._seat_news) == len(shipped._seat_news) > 0
        for t in w.tenures:
            if t.kind != "hold" or not t.live or t.object not in w.offices:
                continue
            rung = w.offices[t.object].rung
            for pid, p in w.persons.items():
                top = world_q.ancestry(w, homes[pid])[-1] if pid in homes else None
                same = rung is not None and top is not None and world_q.ancestry(w, rung)[-1] == top
                assert (t.subject in holders_named(p.ledger, t.object)) == same, (pid, t.object)
                checked += 1
    assert checked > 5000, checked


@pytest.fixture(scope="module")
def known_hearers():
    """The shipped realm and a person who forms a `tell` on somebody he knows, with that somebody."""
    w = build_realm(0)
    for pid, p in sorted(w.persons.items()):
        for c in _candidates(w, pid):
            if c[0] == "tell" and dict(c[2]).get("to") in known_persons(p.ledger, pid):
                return pid, dict(c[2])["to"]
    raise AssertionError("no person forms a tell at build")


def test_telling_hearers_seen_since_move(known_hearers):
    """`08_FI_02` edit 5: under `seen_since_move` a teller offers the telling only to those he holds a firsthand sighting of since his own
    newest movement; the shipped `known` offers it to everyone he knows (control)."""
    teller, hearer = known_hearers
    w = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("telling_hearers", "seen_since_move"))
    tells = lambda: {dict(c[2]).get("to") for c in _candidates(w, teller) if c[0] == "tell"}
    assert hearer in {dict(c[2]).get("to") for c in _candidates(build_realm(0), teller) if c[0] == "tell"}      # the control forms it
    assert hearer not in tells()                                                                                   # no sighting
    led = w.persons[teller].ledger
    led.append(Claim("c_saw", teller, hearer, SEEN_PREDICATE, Seen(stratum="speech", who=hearer), 0, "firsthand", 100, "own", 0))
    assert hearer in tells()                                                                                       # seen
    led.append(Claim("c_moved", teller, teller, "travel.moved", True, 0, "firsthand", 100, "own", 1))
    assert hearer not in tells()                                                                                   # he moved since
