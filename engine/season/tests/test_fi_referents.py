"""B11.08 (`08_FI_01` edits 1-6, `08_FI_02` edit 5, `16_PESSIMIST_FI_C` edit 4) -- REFERENTS ABOUT OTHER PEOPLE COME FROM THE ASKER'S OWN LEDGER.

`queries/world_q.py::questions_for` stopped handing a person referents read from another person's or seat's current state: a seat's holder
(`_goal_referents`), a vacancy (`vacancies`), a met aim (`aim_state`), a docketed matter (`matters_awaiting`), and whether a claim's person
subject still exists or where he is (the claim loop). Each pair below is two realms (`build_realm(0)`) that differ ONLY by an edit made
on the World with no Event and no WITNESS, so the subject's ledger and own edges are identical in both; his candidates (`opening_set` over
every question `questions_for` gives him) must be too. The positive arms are the same change made by the real fold and the real WITNESS.

⚠ A MEASURED RESIDUAL OF THE ITEM'S OWN FALSIFIER (`16_PESSIMIST_FI_C`: "any pair of worlds that differ only by an un-evented edit to another
person's existence or place, in which the subject's candidate set differs"), NOT A BOUND OF THE TEST: on the silent death the pair still differs
in five rows -- `capture`, `tend`, `open_case`, `petition`, `dispatch` on the dead man (measured, seed 0, the King: 2 to 5 lost for each of the 10 of the
12 persons who know him that differ). Those rows declare a `referent_class`, so they form on a referent only where `World.class_of` stamps it
(`world_q._of_stamped_class`, called by `own_referents_of_class`, REM-21), and a person the world no longer holds has no class. The claim loop
this item edits admits the same questions in both worlds; the class stamp is another world read on the same man, outside the item's edits
(`hole_register.yaml`, the B11.08 rows). `test_a_silent_death_removes_no_candidate` compares the questions and the rows with no class, and says so.
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
                out.add((c.verb, c.subject, tuple(sorted((k, v if getattr(v, '__hash__', None) else repr(v)) for k, v in (c.operands or {}).items()))))
    return frozenset(out)


def _question_ids(w, pid) -> frozenset:
    return frozenset(q.id for q in world_q.questions_for(w, w.persons[pid]))


def _knowers(w, x) -> list:
    return sorted(pid for pid, p in w.persons.items() if pid != x and x in known_persons(p.ledger, pid))


def _silently_gone(w, x) -> None:
    """`x` stops existing on the World with no Event, as `World.remove_person`'s cascade leaves it (`state/world.py`: every live edge naming him,
    his own and the ones that hold him as their object, closes) -- so the aim rule's `governing_hold`, `members` and `faction_holding` (which
    `opinion_referents` reads) see no edge of his -- then he and his person-kind rung leave the stores. No Event, no WITNESS."""
    for t in list(w.tenures):
        if (t.subject == x or t.object == x) and t.live:
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
    the same questions and the same candidates (the class-stamped rows aside, the module docstring).

    ⚠ IT ITERATES ONLY THE PERSONS WHO KNOW HIM (`_knowers`: `known_persons` names him, from an acquaintance, a sighting or a teller). A person who
    holds a claim about a man he has no acquaintance, sighting or teller for reads him as a thing once the world no longer holds him
    (`world_q._is_person_subject`), so a deletion nobody has heard of is outside this pair: it is the old clauses' reading for him, and the
    pair would differ there (`_is_person_subject`'s stated bound)."""
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
    """`p1d_where.py`: a man moved to a hearth nobody lives at, outside his own territory, on the World alone; nobody who knows him has his
    candidates move. Two movers: the King, and the heir (`p_npc_031`), who is not the King and whose seat is not the throne.

    ⚠ BOUNDED, NOT CLOSED: `matters_awaiting` still reads `place_of` of a matter (a person on a docket) to place its tier -- `08_FI_01` edit 5
    keeps "the seat and tier logic" and only gates the matter on his own ledger holding a claim of its docketing. The realm holds no docketed matter
    at build, so that read is dormant in this pair; a docketed person who moves still moves the tier a convener is offered
    (`test_cr56_matter_stamped.py` observes the tier logic with the matter's place planted)."""
    HEIR = "p_npc_031"
    arms = 0
    for mover in (KING, HEIR):
        control, moved = build_realm(0), build_realm(0)
        homes = world_q.home_of(control)
        territory = next(r for r in world_q.ancestry(control, homes[mover]) if control.rungs[r].kind == "territory")
        to = next(r.id for r in sorted(control.rungs.values(), key=lambda r: r.id)
                  if r.kind == "hearth" and r.id not in set(homes.values()) and territory not in world_q.ancestry(control, r.id))
        _silently_moved(moved, mover, to)
        assert world_q.home_of(moved)[mover] == to != world_q.home_of(control)[mover]
        knowers = _knowers(control, mover)
        for s in knowers:
            assert _candidates(moved, s) == _candidates(control, s), (mover, s)
        arms += sum(len(_candidates(control, s)) for s in knowers) > 0
    assert arms == 2


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


def test_a_witnessed_release_of_another_commitment_does_not_end_the_seat_hold():
    """Close fix F-B1: a claim that K ceased some OTHER tenure (`tenure.closed` about K, no closing claim about the seat in its `(when, lap)`) is no news
    of the seat, so `holders_named` still names K. CONTROL: a closing claim about the seat at the same `(when, lap)` as K's ends his hold; a death ends it
    whatever the key. FALSIFIER: the pre-fix reading drops K at the first ledger."""
    mk = lambda cid, subj, pred, when: Claim(cid, "p_w", subj, pred, True, when, "firsthand", 100, "own", 0)
    base = [mk("a", "T", "tenure.opened", 2), mk("b", "K", "tenure.opened", 2)]
    assert holders_named(base + [mk("c", "K", "tenure.closed", 9)], "T") == ("K",), "an unrelated closing claim ended the seat hold"
    assert holders_named(base + [mk("d", "K", "tenure.closed", 9), mk("e", "T", "tenure.closed", 9)], "T") == ()
    assert holders_named(base + [mk("f", "K", "person.died", 9)], "T") == ()
    assert set(holders_named(base, "T")) == {"K"}


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


def test_the_realms_rung_aim_is_met_for_its_holder_and_open_for_those_who_have_not_heard():
    """`aim_state` on the realm's one met aim (`goal_varfell_oastad_gate`, rung `terr_T13`, governed by a Varfell man -- `test_governance_build.py`'s
    589 reads it): the holder reads `met` from his own live hold (R-03: a man knows his own lands, an own-edge read) and is asked no `need`; every
    other man committed to it reads `open`, since the realm seeds no news of a RUNG's holder (`seed_seat_news` seeds Office holds, and a rung hold
    is the build's own edge), until his claims name the GOVERNING hold's holder -- told, `met` again."""
    w = build_realm(0)
    gid = "goal_varfell_oastad_gate"
    prop = w.propositions[gid]
    committed = sorted(t.subject for t in w.tenures if t.kind == "commit" and t.live and t.object == gid)
    governing = world_q.governing_hold(w, "terr_T13")
    assert governing is not None and governing.subject in committed and len(committed) >= 3, (governing, committed)
    state = {pid: world_q.aim_state(w, w.persons[pid], prop) for pid in committed}
    assert state[governing.subject] == "met" and {s for pid, s in state.items() if pid != governing.subject} == {"open"}, state
    need = lambda pid: [q for q in world_q.questions_for(w, w.persons[pid]) if q.id == f"q:need:{gid}"]
    other = next(pid for pid in committed if pid != governing.subject)
    assert not need(governing.subject) and need(other)
    hears_of(w.persons[other], governing.object, governing.subject)
    assert world_q.aim_state(w, w.persons[other], prop) == "met" and not need(other)
