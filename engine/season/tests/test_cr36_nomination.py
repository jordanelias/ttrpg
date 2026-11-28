"""v11 CR-36 -- B21c.04: A SEAT FILLED BY ONE BODY'S NOMINATION AND A SECOND SEAT'S CONFIRMATION (the `nominated` half of §1b-3).

A `nominated` seat is filled by `confer` (`state/gate.py::FILLED_BY["nominated"]` is the conferral basis), and `confer` on it is admitted only
when the CONFIRMING actor HOLDS a live `resolution` naming the seat (`terms`) and the conferee (`to`) whose creating Act exercised a seat
OTHER than the conferring `via` (`loop/predicates.py::confirming_resolutions`, the creating Act read as `_eff_arrest` reads a warrant's,
`world_q.issuing_seat`). The `resolution` is minted by a determination under a `disposes: Record` row (`parliamentary_debate`) at
Overwhelming or Success, held by the determining actor (`_eff_determine`'s Record disposal site; ED-IN-0292 (1) bars minting it into any
other hand). REACH 0 in the realm: no computed docket item names an arrangement (H-80) and no computed `give` delivers a resolution (H-229).

THE WORLD is `test_u7_remit.py`'s (`probes.tiny_world`: R > D > S > Hh) with the Duke's hold ended and:
  * the vacant clerk's seat `off_parliamentary_clerk` (`conferral: nominated`, rung `D`, no faction, as the realm row);
  * the King's seat `off_king` (Crown, scope `R`, remit `determine` and `confer`, held by p_king) and the Widow Regent's `off_regent` (Crown,
    scope `R`, remit `determine`, held by p_high): the nominating bench `judging_set` lists for `parliamentary_debate` (the interim two-seat
    bench, CR-38); the Regent's seat is HAND-BUILT with `determine` -- the shipped Widow Regent's hold carries none (B21.16);
  * the nominee p_mid holding the petition `pet_clerk` (terms the clerk's seat), docketed under `parliamentary_debate`.
The hand-built `give` (H-229's residue) moves the resolution's `hold` from the Regent to the King by hand: the delivery is not under test.
"""
from __future__ import annotations

import pytest

from ..loop.effects_information import _docket_item
from ..queries import world_q
from ..queries.person_q import vacant_named
from ..state.carriers import Act, Claim, Office, Record, Tenure
from .test_u7_remit import JUDGE, OPENS, _fold, _kinds, _open, _world

CROWN = "Valorsmark"
CLERK, PETITION, NOMINEE, OTHER = "off_parliamentary_clerk", "pet_clerk", "p_mid", "p_other"
KING_SEAT, REGENT_SEAT = "off_king", "off_regent"
ROW = "parliamentary_debate"
SEEDS = range(40)


def _seat(w, sid, post, rung, remit, faction, holder, conferral=None, body=None):
    off = Office(sid, post, rung, list(remit), faction=faction, conferral=conferral, body=body)
    off.scope_rung = rung
    w.offices[sid] = off
    if holder is not None:
        w.add_tenure(Tenure(f"t_seat_{sid}", holder, sid, "hold", since=0))


def _court(**fx):
    w, d = _world(**fx)
    for t in list(w.tenures):
        if t.kind == "hold" and t.object == "off_duke":
            t.until = 0
    _seat(w, CLERK, "Chief Parliamentary Clerk", "D", ["issue"], None, None, conferral="nominated", body="Ministries")
    _seat(w, KING_SEAT, "King", "R", ["issue", "determine", "confer", "revoke", "convene"], CROWN, "p_king")
    _seat(w, REGENT_SEAT, "Dicastery", "R", ["issue", "determine"], CROWN, "p_high")
    w.records[PETITION] = Record(PETITION, "Hh", "petition", subject_matter={"terms": CLERK, "to": None, "from": "Hh"})
    w.add_tenure(Tenure("t_pet", NOMINEE, PETITION, "hold", since=0))
    w.docket.append(_docket_item(NOMINEE, ROW, PETITION))
    return w, d


def _determine(key, actor="p_high", via=REGENT_SEAT):
    return Act(id=key, actor=actor, verb="determine", via=via, payload={"subject": NOMINEE})


def _confer(key, to=NOMINEE, actor="p_king", via=KING_SEAT):
    return Act(id=key, actor=actor, verb="confer", via=via, payload={"subject": CLERK, "to": to})


def _resolutions(w):
    return {rid: r for rid, r in w.records.items() if r.kind == "resolution"}


def _holder(w, rid):
    return [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == rid]


def _give_by_hand(w, rid, to):
    """H-229's residue: the resolution's one live `hold` closes and the receiver's opens -- `give`'s two edges, written by hand."""
    held, = [t for t in w.tenures if t.kind == "hold" and t.live and t.object == rid]
    held.until = w.tick
    w.add_tenure(Tenure(f"t_given_{rid}", to, rid, "hold", since=w.tick))


def _clerk_holders(w):
    return [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == CLERK]


def _nominated(key, **fx):
    """A court whose Regent's determination carried: the resolution she holds, or `None` where the draw did not open."""
    w, d = _court(**fx)
    out = _fold(w, d, _determine(key))
    return w, d, out


# --- THE ROUTE EXECUTES ----------------------------------------------------------------------------------------------------------------

def test_nominee_is_confirmed_on_a_held_resolution():
    """EXIT: the clerk's seat vacant; the Widow Regent `determine`s the nominee under `parliamentary_debate` -> at Overwhelming or Success a
    `resolution` whose `terms` is the seat and whose `to` is [the nominee], held by HER, its creating Act's seat her own; after the hand-built
    `give` the King, holding it, `confer`s the seat on the nominee -> he holds the seat. Read where both draws carry, over forty act ids
    (shipped fixtures). The bench is the King and the Regent."""
    checked = nominated = seated = 0
    for s in SEEDS:
        w, d = _court()
        assert sorted(world_q.judging_set(w, "Hh", NOMINEE)) == ["p_high", "p_king"]
        out = _fold(w, d, _determine(f"nm{s}"))
        assert "determine.refused" not in _kinds(out) or out[0].degree == "Partial", _kinds(out)
        checked += 1
        made = _resolutions(w)
        if out[0].degree not in OPENS:
            assert made == {}, (s, out[0].degree)
            continue
        (rid, rec), = made.items()
        assert rec.subject_matter == {"terms": CLERK, "to": [NOMINEE]}, rec.subject_matter
        assert _holder(w, rid) == ["p_high"]
        assert world_q.issuing_seat(w, rid) == REGENT_SEAT
        assert not world_q.docketed(w, NOMINEE), "the matter stayed on the docket"
        nominated += 1
        _give_by_hand(w, rid, "p_king")
        got = _fold(w, d, _confer(f"cf{s}"))
        assert "confer.refused" not in _kinds(got), _kinds(got)
        if got[0].degree in OPENS or got[0].degree == "Partial":
            assert _clerk_holders(w) == [NOMINEE], (s, got[0].degree)
            seated += 1
    assert checked >= 40
    assert nominated >= 1 and seated >= 1, (nominated, seated)


# --- THE REFUSALS: AT THE PRECONDITION, NEVER A DRAW ------------------------------------------------------------------------------------

def _arm(arm):
    """A carried nomination (a strong judge), delivered to the King, then one change per arm. Returns the world, its driver and the act."""
    w, d = _court(**JUDGE)
    actor, via = "p_high", REGENT_SEAT
    if arm == "iv_one_seat":
        actor, via = "p_king", KING_SEAT
    out = _fold(w, d, _determine(f"n_{arm}", actor=actor, via=via))
    assert out[0].degree in OPENS, (arm, _kinds(out))
    (rid, _), = _resolutions(w).items()
    if actor != "p_king":
        _give_by_hand(w, rid, "p_king")
    to = NOMINEE
    if arm == "ii_another_person":
        to = OTHER
    elif arm == "iii_none_held":
        _give_by_hand(w, rid, "p_low")
    return w, d, _confer(f"c_{arm}", to=to)


@pytest.mark.parametrize("arm", ["ii_another_person", "iii_none_held", "iv_one_seat"])
def test_confirmation_refusals(arm):
    """(ii) the seat conferred on another person than the resolution names; (iii) the confirmer holds no resolution (it went elsewhere);
    (iv) the King nominating through `off_king` and confirming through `off_king` (the two-seat clause). Each is `confer.refused` at the
    precondition and the seat stays vacant. CONTROL (one clause away): the `control` arm -- the Regent's resolution in the King's hand,
    conferred on its nominee -- passes the precondition (no `confer.refused`)."""
    w, d, act = _arm("control")
    assert "confer.refused" not in _kinds(_fold(w, d, act))
    w, d, act = _arm(arm)
    assert _kinds(_fold(w, d, act)) == ["confer.refused"], arm
    assert _clerk_holders(w) == [], arm


def test_a_nominated_vacancy_is_offered_only_to_a_resolution_holder():
    """`world_q.vacancies` OFFERS A `nominated` SEAT ONLY TO A CONFERRER WHO HOLDS A `resolution` NAMING IT: the King, told the clerk's seat
    is empty and granted `confer` over it, is offered nothing while he holds no resolution; once the Regent's carried nomination is in his
    hand (the hand-built `give`), he is offered the seat (CONTROL, one edge away)."""
    w, d = _court(**JUDGE)
    king = w.persons["p_king"]
    king.ledger.append(Claim("c_clerk_empty", "p_king", CLERK, "tenure.closed", True, w.tick, "firsthand", 1.0, "own"))
    assert vacant_named(king.ledger, CLERK)
    assert CLERK not in world_q.vacancies(w, king)
    out = _fold(w, d, _determine("n_vac"))
    assert out[0].degree in OPENS, _kinds(out)
    (rid, _), = _resolutions(w).items()
    _give_by_hand(w, rid, "p_king")
    assert CLERK in world_q.vacancies(w, king)


def test_a_petition_naming_no_seat_is_not_docked_for_a_seat_row():
    """`open_case` DOCKS NO MATTER `_eff_determine` WOULD DECLINE FOREVER: under a row that mints a resolution (`parliamentary_debate`) or
    fills a seat (`election`), a petition whose `terms` name no Office is not docked; CONTROL (one value away): `terms` the clerk's seat is.
    `test_u7_remit.py`'s world, whose Duke's seat opens cases."""
    checked = 0
    for row in (ROW, "election"):
        for terms, docks in ((CLERK, True), ("off_nowhere", False)):
            w, d = _world(**JUDGE)
            _seat(w, CLERK, "Chief Parliamentary Clerk", "D", ["issue"], None, None, conferral="nominated", body="Ministries")
            w.records["pet_x"] = Record("pet_x", "Hh", "petition", subject_matter={"terms": terms, "to": None, "from": "Hh"})
            w.add_tenure(Tenure("t_pet_x", NOMINEE, "pet_x", "hold", since=0))
            out = _fold(w, d, _open(f"oc_{row}_{docks}", subject=NOMINEE, arrangement=row, petition="pet_x"))
            assert bool(world_q.docketed(w, NOMINEE)) is docks, (row, terms, _kinds(out))
            checked += 1
    assert checked == 4


def test_a_failed_nomination_mints_nothing():
    """(v) a `determine` at Failure mints no resolution and leaves the matter docketed; the King then holds nothing to confirm on, so his
    `confer` is refused. Read over forty act ids at a weak judge (the pool floor at 0): at least one Failure is read, each mints nothing."""
    failed = 0
    for s in SEEDS:
        w, d = _court(pool_floor=0)
        out = _fold(w, d, _determine(f"f{s}"))
        if out[0].degree != "Failure":
            continue
        failed += 1
        assert _kinds(out) == ["matter.undetermined"], _kinds(out)
        assert _resolutions(w) == {} and world_q.docketed(w, NOMINEE)
        assert _kinds(_fold(w, d, _confer(f"fc{s}"))) == ["confer.refused"]
    assert failed >= 1, "no seed read a Failure"
