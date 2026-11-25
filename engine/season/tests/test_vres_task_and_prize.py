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

from ..data.rosters import roster_map
from ..data.verbs import VERB_TABLE
from ..gaps import Unspecified
from ..manifest import registry
from ..queries import world_q
from ..seam.wrappers import sigma
from ..state.carriers import Office, Tenure
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
    monkeypatch.setattr(sigma, "reception", lambda w_, who, audience: asked.append((who, audience)) or 0.0)
    w = _council_world()
    for toward in (None, "to"):
        sigma.contest_input(w, [SPEAKER, PARTY], verb="determine", subject=PARTY, room="Hh", heard_by="residents", toward=toward)
    assert [who for who, _ in asked] == [SPEAKER, PARTY], asked
    assert all(sorted(a) == sorted((SPEAKER, PARTY, REEVE)) for _, a in asked), asked
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
