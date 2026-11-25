"""B07.04 (`U5c_VERBS_residue` §2, edits 1-4): ONE PRIZE ROSTER FOR THE GOVERNANCE ROWS AND ONE AUDIENCE FUNCTION.

A prize row's `heard_by:` names the room that hears the act (`manifest/registry.py::HEARD_BY_ROOMS`: `bench`, `seat_body`,
`residents`); `seam/wrappers/sigma.py::audience_of` is the one table that says whom a room means, keyed by room and nothing else; `world_q.reception`
and `world_q.proofs` take its tuple. No verb row names `a seat` or `a holding` yet (each lands with its verb: B21, B23), so none of this moves a season.

  * gate (1): the loader refuses a planted `heard_by: nobody` and a verb naming a prize no row claims (invariant 9);
  * gate (2): one act, the prize row's `heard_by` swapped between `bench` and `seat_body`, two audiences: the audience follows the row;
  * the direction (edit 4): `toward: to` asks the room about the receiver; an unknown side is refused naming the row;
  * the falsifier: no row of the audience table, and no branch of `audience_of`, names a verb.
"""

from __future__ import annotations

import ast
import dataclasses
from pathlib import Path

import pytest
from engine.dice_engine import draw

from ..boot.realm import build_realm
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import ABSENT_PREDICATE, roster_map
from ..data.verbs import VERB_TABLE
from ..gaps import Unspecified
from ..decision.options import _hears_by_presence
from ..epistemic import SEEN_PREDICATE, Seen
from ..harness import probes as P
from ..harness.play_surface import dispatching_chooser
from ..loop.driver import SeasonDriver
from ..manifest import registry
from ..queries import world_q
from ..queries.person_q import known_persons, present_persons, said_of
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim, Office, Scene, Tenure
from ..state.ids import H
from .test_fi_referents import _candidates
from .test_u7_remit import _world

SPEAKER, PARTY, DUKE, REEVE = "p_low", "p_mid", "p_high", "p_other"
SEAT, OTHER_SEAT = "off_duke", "off_reeve"
PRIZES = roster_map("contest_subsystems", "prizes")


def _council_world():
    """`tiny_world` plus a second seat at the Duke's rung, held by a man who sits on no bench (no `determine` in his grant): the bench over `Hh` is
    the Duke alone, the seated persons at the Duke's rung are the two, and the residents of `Hh` are the three who live there."""
    w, _d = _world()
    w.offices[OTHER_SEAT] = Office(OTHER_SEAT, "Reeve", "D", ["issue"], faction="Valorsmark")
    w.add_tenure(Tenure("t_reeve", REEVE, OTHER_SEAT, "hold", since=0))
    return w


def _the_two_audiences(w, *rooms):
    return [sigma.audience_of(w, sigma.HeardAct(SPEAKER, SEAT, "Hh"), room) for room in rooms]


def test_each_room_means_the_persons_its_row_of_the_table_names():
    w = _council_world()
    bench, council, residents = _the_two_audiences(w, "bench", "seat_body", "residents")
    assert bench == (DUKE,), bench
    assert council == (DUKE, REEVE), council
    assert sorted(residents) == sorted((SPEAKER, PARTY, REEVE)), residents
    assert sigma.audience_of(w, sigma.HeardAct(SPEAKER, None, "Hh"), "seat_body") == (), "an act through no seat has no body to hear it"
    assert sigma.audience_of(w, sigma.HeardAct(SPEAKER, SEAT, None), "residents") == (), "a placeless act has no residents"
    assert sigma.audience_of(w, sigma.HeardAct(SPEAKER, SEAT, None), "bench") == (), "a placeless act has no bench"
    assert set(sigma._AUDIENCES) == registry.HEARD_BY_ROOMS


def test_a_heard_by_outside_the_rooms_and_an_unclaimed_prize_are_refused(monkeypatch):
    """Gate (1). CONTROL first: the shipped roster, with `a seat` and `a holding` claimed by no verb, boots and passes the prize check
    (`check_contest_prizes` binds a prize row to no verb, only a verb to a prize row); then each plant is refused naming itself."""
    assert {"a seat", "a holding"} <= set(PRIZES)
    # B21.09/B21.14 re-read: `establish`, `confer`, `revoke` and `succeed` now draw on `a seat` (the prize is claimed); `a holding` is still claimed by none
    assert {v for v, r in VERB_TABLE.items() if "a seat" in set(registry._as_list(r.contests or []))} == {"confer", "establish", "revoke", "succeed"}
    assert not [v for v, r in VERB_TABLE.items() if "a holding" in set(registry._as_list(r.contests or []))], "a verb names the new prize"
    assert registry.check_rows()
    assert registry.check_contest_prizes(VERB_TABLE)
    monkeypatch.setitem(PRIZES["a seat"], "heard_by", "nobody")
    with pytest.raises(Unspecified, match=r"contest:'a seat' declares `heard_by: 'nobody'`"):
        registry.check_rows()
    monkeypatch.setitem(PRIZES["a seat"], "heard_by", "seat_body")
    assert registry.check_rows()
    planted = {**VERB_TABLE, "speak": dataclasses.replace(VERB_TABLE["speak"], contests="a seatt")}
    assert registry.unclaimed_contest_prizes(planted) == [("speak", "a seatt")]
    with pytest.raises(Unspecified, match=r"verb 'speak' declares `contests: 'a seatt'`"):
        registry.check_contest_prizes(planted)


def test_the_audience_follows_the_prize_row(monkeypatch):
    """Gate (2): the same act through `resolve`, the prize row's `heard_by` swapped between `bench` and `seat_body`, reads two different audiences
    from `audience_of`, and a room no row swaps in is not read."""
    w = _council_world()
    read = []
    real = sigma.audience_of
    monkeypatch.setattr(sigma, "audience_of", lambda w_, act, room: read.append((room, real(w_, act, room))) or read[-1][1])
    for room in ("bench", "seat_body"):
        monkeypatch.setitem(PRIZES["a matter"], "heard_by", room)
        out = sigma.resolve(w, [SPEAKER, PARTY], ["root"], "a matter", verb="determine", subject=PARTY, via=SEAT,
                            rng=draw.seeded(draw.H2("test_vres_task_and_prize", 0)), rung="Hh")
        assert out["status"] == "RESOLVED", out
    assert [room for room, _ in read] == ["bench", "seat_body"]
    assert read[0][1] == (DUKE,) and read[1][1] == (DUKE, REEVE) and read[0][1] != read[1][1], read


def test_toward_to_asks_the_room_about_the_receiver_and_an_unknown_side_is_refused(monkeypatch):
    """Edit 4: `a holding` declares `toward: to`; its room is asked about the receiver (the roll's person counterparty), not the actor. Unset, the
    actor. A side no reader knows is refused at boot naming the row."""
    assert PRIZES["a holding"]["toward"] == "to" and PRIZES["a holding"]["heard_by"] == "residents"
    asked = []
    monkeypatch.setattr(sigma, "reception", lambda w_, who, audience, actor: asked.append((who, audience, actor)) or 0.0)
    w = _council_world()
    for toward in (None, "to"):
        sigma.contest_input(w, [SPEAKER, PARTY], verb="determine", subject=PARTY, room="Hh", heard_by="residents", toward=toward)
    assert [who for who, _, _ in asked] == [SPEAKER, PARTY], asked
    assert all(sorted(a) == sorted((SPEAKER, PARTY, REEVE)) for _, a, _ in asked), asked
    assert [actor for _, _, actor in asked] == [SPEAKER, SPEAKER], asked          # B24.02: the actor is `claimants[0]` whichever side the room is asked about
    monkeypatch.setitem(PRIZES["a holding"], "toward", "from")
    with pytest.raises(Unspecified, match=r"contest:'a holding' declares `toward: 'from'`"):
        registry.check_rows()


def test_no_row_of_the_audience_table_names_a_verb():
    """The falsifier: a function in the seam that names a verb to pick an audience. The table's functions read no `.verb` and spell no verb name."""
    tree = ast.parse(Path(sigma.__file__).read_text())
    owned = {"audience_of", "_bench", "_seat_body", "_residents", "HeardAct"}
    checked = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in owned:
            checked += 1
            for sub in ast.walk(node):
                assert not (isinstance(sub, ast.Attribute) and sub.attr == "verb"), (node.name, sub.lineno)
                assert not (isinstance(sub, ast.Constant) and isinstance(sub.value, str) and sub.value in VERB_TABLE), (node.name, sub.value)
    assert checked == len(owned)


# --- B11.83 (`U5c_VERBS_residue` §3 steps 1 and 3): A REFUSAL ON THE `with` CONJUNCT TEACHES THE ACTOR, AND ONLY HIM, THAT THE PERSON WAS NOT THERE ---

_TELLER, _AT = "p_low", "Hh"          # `p_low` stands in `Hh`; `p_king` stands in `R`, `p_mid` in `Hh`


def _tell_season(subject, hearer, **fx):
    """One season in which `_TELLER` (holding one claim, about `Hh`) is handed a `tell` of `subject` to `hearer` every time he is asked, and nobody
    else chooses anything. Returns the world and the refusal Events in log order."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    d = SeasonDriver(w)
    w.persons[_TELLER].ledger.append(Claim("c_held", _TELLER, _AT, "stores:grain", 8, 0, "firsthand", 80, "own"))
    said = said_of(w.persons[_TELLER].ledger, subject, w.fixtures)

    def tell(p, v, s, ask_budget, auto):
        aid = H(w.world_seed, w.tick, p.id, f"act:tell:{subject}:{hearer}")
        return [Scene(H(w.world_seed, w.tick, p.id, f"scene:b11_83"), p.id,
                      [Act(aid, p.id, "tell", payload={"subject": subject, "to": hearer, "said": said})])]

    d.season(dispatching_chooser(P.NOCHOOSE, {_TELLER: tell}), question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, [e for e in w.log if e.kind == "tell.refused"]


def _absent_claims(w):
    return [c for p in w.persons.values() for c in p.ledger if c.predicate == ABSENT_PREDICATE]


@pytest.mark.parametrize("mode", ["actor", "total"])
def test_a_with_refusal_deposits_absent_to_the_actor_only(mode):
    """The source's falsifier, "a second person holding the `absent` claim": a `tell` to a hearer who stands elsewhere is refused on `hearer` (the `with`
    conjunct); the teller alone holds a firsthand `(hearer, absent, <the place he stood>)`, and no other ledger holds the predicate.
    CONTROL: a `tell` refused on `holds` (the teller holds nothing of the subject) deposits no `absent` claim -- the refusal is the same kind, the
    deciding read is not a `with` read."""
    w, refused = _tell_season(_AT, "p_king", observation_deposit_mode=mode)
    assert refused, "no refusal reached the log: the falsifier cannot see a deposit"
    got = _absent_claims(w)
    assert got, "the refused `with` conjunct deposited nothing"
    assert {c.holder for c in got} == {_TELLER}, [(c.holder, c.subject) for c in got]
    assert {(c.subject, c.value, c.source, c.chain) for c in got} == {("p_king", _AT, "firsthand", ())}, got
    assert all(c.confidence > 0 and c.visibility == "own" for c in got)
    # the control: the same refusal kind, decided by another conjunct (the hearer stands with him, so no `with` read is ever False)
    w2, refused2 = _tell_season("R", "p_mid")
    assert refused2 and not _absent_claims(w2), [(c.holder, c.subject) for c in _absent_claims(w2)]
    assert {e.kind for e in refused2} == {"tell.refused"} and all(o.predicate == "claim.held" for e in refused2 for o in e.observed[-1:])
    # and a hearer who IS there is told: nothing is absent
    w3, refused3 = _tell_season(_AT, "p_mid")
    assert not refused3 and not _absent_claims(w3)


def test_a_with_refusal_deposits_no_absent_claim_at_none():
    """`none` is the control arm of `observation_deposit_mode`: the deposit block it gates is the `absent` claim's too, so the same refusal that leaves
    one at `actor` and `total` leaves none. The refusal itself is asserted, so the empty reading is an observation and not an absent run."""
    w, refused = _tell_season(_AT, "p_king", observation_deposit_mode="none")
    assert refused, "no refusal reached the log: the control cannot see a deposit"
    assert not _absent_claims(w), [(c.holder, c.subject) for c in _absent_claims(w)]


def test_an_absent_claim_is_never_passed_on_by_the_man_who_holds_it():
    """Step 3 against a retelling: `said_of` offers the newest non-`seen` claim a teller holds about a subject; his own `absent` claim about the man is
    not among them, so a telling cannot make a second holder. With another claim about him held, that one is said; with nothing else, nothing."""
    absent = Claim("c_abs", _TELLER, "p_king", ABSENT_PREDICATE, _AT, 3, "firsthand", 100, "own")
    other = Claim("c_oth", _TELLER, "p_king", "exists:Person", 1, 0, "firsthand", 80, "own")
    fx = DEFAULT_FIXTURES
    assert said_of([absent], "p_king", fx) is None
    assert said_of([other, absent], "p_king", fx).predicate == "exists:Person"


# --- B11.84 (`U5c_VERBS_residue` §3 step 2): `present_persons` LEAVES OUT A PERSON THE HOLDER'S NEWEST CLAIM SAYS IS ABSENT ---

def test_absent_claim_removes_the_person_until_a_newer_sighting():
    """The source's gate (`p1b_belief.py`'s shape): under `telling_hearers: seen_since_move` a teller who holds a sighting of a man forms acts on him;
    the `absent` claim a refused `with` leaves removes every one of them; a sighting newer than it restores them, and an `absent` claim about somebody
    else removes nothing (the control: no `absent` claim about him, the same reading as before). FALSIFIER: a candidate formed on a man the holder's
    newest claim says is absent."""
    w = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("telling_hearers", "seen_since_move"))
    control = build_realm(0)
    teller = hearer = None
    for pid in sorted(control.persons):
        for c in _candidates(control, pid):
            if c[0] == "tell" and dict(c[2]).get("to") in known_persons(control.persons[pid].ledger, pid):
                teller, hearer = pid, dict(c[2])["to"]
                break
        if teller:
            break
    assert teller, "no person forms a tell at build"
    led = w.persons[teller].ledger
    on_him = lambda: [c for c in _candidates(w, teller) if _hears_by_presence(VERB_TABLE[c[0]]) and dict(c[2]).get("to") == hearer]
    assert not on_him()                                                                          # no sighting: nobody to offer it to
    led.append(Claim("c_saw1", teller, hearer, SEEN_PREDICATE, Seen(stratum="speech", who=hearer), 0, "firsthand", 100, "own", 0))
    before = len(on_him())
    assert before > 0, "the sighting forms no act on him: the falsifier cannot see a removal"
    led.append(Claim("c_abs_other", teller, "p_nobody", ABSENT_PREDICATE, "Hh", 1, "firsthand", 100, "own", 0))
    assert len(on_him()) == before                                                                # absent of somebody else: nothing moves
    led.append(Claim("c_abs", teller, hearer, ABSENT_PREDICATE, "Hh", 1, "firsthand", 100, "own", 0))
    assert hearer not in present_persons(led, teller) and not on_him(), on_him()                  # 0 after the refusal
    led.append(Claim("c_saw2", teller, hearer, SEEN_PREDICATE, Seen(stratum="speech", who=hearer), 2, "firsthand", 100, "own", 0))
    assert hearer in present_persons(led, teller) and len(on_him()) == before                     # a newer sighting places him there again
