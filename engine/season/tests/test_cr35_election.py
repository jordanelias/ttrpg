"""v11 CR-35 (1)-(7), (9) -- B21c.02: AN ELECTED SEAT IS FILLED BY ITS FACTION'S BENCH; THE CONTESTED SUCCESSION (H-217, SC-04).

A docketed petition whose `terms` name a vacant seat S, heard under an arrangement row that `disposes: hold` (`election`, `succession`), is
determined by a judging seat of S's faction: at a band that opens, the party holds S. Built: the gate's election arm (`state/gate.py::
may_elect`, asked by `tenure_write_basis`'s determination clause and by the precondition's `bench` stem), `_disposal`'s `hold` literal,
`judging_set`'s `matter` wired for a hold-disposing row (the electorate: the live judging seats of S's faction, S excluded, no containment
walk), the elector's commit read only where its OUGHT names the candidate and the seat (`declared_votes_by_member`), and the two seeded rows.
REACH 0 in the realm: no computed docket item names an arrangement, so nothing here moves `build_realm`.

THE WORLD is `test_u7_remit.py`'s (`probes.tiny_world`: R > D > S > Hh) with the Duke's hold ended and:
  * the vacant Church seat `off_confessor` (`conferral: elected`, rung and scope `D`), its last holder's hold ended (vacated);
  * two Church judging seats at `D` -- `off_cardinal_justice` (p_high) and `off_senior_inquisitor` (p_low) -- the electorate;
  * a Crown judging seat `off_crown_bench` (p_king, scope `R`): a bench of another faction, never an elector of a Church seat;
  * the candidate p_mid, committed to the Church, holding the petition `pet_confessor` (terms `off_confessor`), docketed under `election`.
The contested succession re-uses the world with a Crown throne (`off_king`, `inheritance`) vacated, the Widow Regent's Crown judging seat
`off_regent` (p_high), the heir's title `off_heir` (p_other; `rosters.yaml: successions` names it for `off_king`), and the rival p_mid.
"""
from __future__ import annotations

import pytest

from ..data.rosters import faction_prop_id
from ..loop.effects_information import _docket_item
from ..queries import world_q
from ..state import gate as G
from ..state.carriers import Act, Office, Proposition, Record, Tenure
from ..state.ids import H
from .test_u7_remit import JUDGE, OPENS, _fold, _kinds, _world

CHURCH, CROWN = "Church of Solmund", "Valorsmark"
SEAT, PETITION, CANDIDATE = "off_confessor", "pet_confessor", "p_mid"
ELECTORS = {"off_cardinal_justice": "p_high", "off_senior_inquisitor": "p_low"}
JUDGE_SEAT, KING_SEAT = "off_cardinal_justice", "off_crown_bench"
THRONE, TITLE, REGENT_SEAT = "off_king", "off_heir", "off_regent"
SEEDS = range(40)


def _commit(w, who, obj, key=None):
    w.add_tenure(Tenure(key or f"cm_{who}_{obj}", who, obj, "commit", since=0))


def _ought(w, who, pid, subject=CANDIDATE, predicate=SEAT):
    """`who` commits to the OUGHT `pid` (minted if absent) about `subject` naming `predicate`."""
    if pid not in w.propositions:
        w.propositions[pid] = Proposition(pid, "OUGHT", subject, predicate, True, 0)
    _commit(w, who, pid)


def _petition(w, party, seat, row):
    w.records[PETITION] = Record(PETITION, "Hh", "petition", subject_matter={"terms": seat, "to": None, "from": "Hh"})
    w.add_tenure(Tenure("t_pet", party, PETITION, "hold", since=0))
    w.docket.append(_docket_item(party, row, PETITION))


def _seat(w, sid, post, rung, remit, faction, holder, n, conferral=None):
    off = Office(sid, post, rung, list(remit), faction=faction, conferral=conferral)
    off.scope_rung = rung
    w.offices[sid] = off
    if holder is not None:
        w.add_tenure(Tenure(f"t_seat_{n}", holder, sid, "hold", since=0))


def _church_world(**fx):
    w, d = _world(**fx)
    for t in list(w.tenures):
        if t.kind == "hold" and t.object == "off_duke":
            t.until = 0
    _seat(w, SEAT, "Confessor", "D", ["issue", "determine", "confer", "revoke", "convene"], CHURCH, None, 0, conferral="elected")
    w.add_tenure(Tenure("t_old_confessor", "p_other", SEAT, "hold", since=0, until=0))        # vacated
    for n, (sid, who) in enumerate(ELECTORS.items(), start=1):
        _seat(w, sid, "Dicastery", "D", ["issue", "determine"], CHURCH, who, n)
    _seat(w, KING_SEAT, "Dicastery", "R", ["issue", "determine"], CROWN, "p_king", 9)
    _commit(w, CANDIDATE, faction_prop_id(CHURCH))
    _petition(w, CANDIDATE, SEAT, "election")
    return w, d


def _determine(key, via=JUDGE_SEAT, actor="p_high", subject=CANDIDATE):
    return Act(id=key, actor=actor, verb="determine", via=via, payload={"subject": subject})


def _holds(w, who, seat):
    return any(t.kind == "hold" and t.live and t.subject == who and t.object == seat for t in w.tenures)


def _seat_holders(w, seat):
    return [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == seat]


def _bare_opening(w, actor, via, party, seat):
    """The gate's own verdict on the opening an election writes, below the precondition."""
    nt = Tenure(H(w.world_seed, w.tick, party, f"hold:{seat}:bare"), party, seat, "hold", since=w.tick)
    return G.tenure_write_basis(w, nt, None, actor, via, frozenset())


# --- THE ELECTION EXECUTES ---------------------------------------------------------------------------------------------------------

def test_a_bench_elects_into_a_vacated_church_seat():
    """EXIT: the Confessor's seat vacated; the candidate's petition naming it docketed under `election`; the Cardinal of Justice, committed
    to an OUGHT whose subject is the candidate and whose predicate names the seat, `determine`s -> at a band that opens, the candidate holds
    `off_confessor` (shipped fixtures, forty act ids). The electorate is the two Church seats (the Crown bench is not one), the elector's
    commit is read, and every seat-hold the determination opens is the candidate's, admitted as `determination`, and carries the seat's grant."""
    carried = checked = 0
    for s in SEEDS:
        w, d = _church_world()
        _ought(w, "p_high", "prop_elect")
        assert sorted(world_q.judging_set(w, "Hh", CANDIDATE)) == sorted(ELECTORS.values())
        assert world_q.declared_votes_by_member(w, CANDIDATE, _row("election")) == {"p_high": 1}
        out = _fold(w, d, _determine(f"el{s}"))
        kinds = _kinds(out)
        assert "determine.refused" not in kinds, kinds
        checked += 1
        if out[0].degree in OPENS or out[0].degree == "Partial":
            assert _seat_holders(w, SEAT) == [CANDIDATE], (s, out[0].degree)
            new = next(t for t in w.tenures if t.kind == "hold" and t.live and t.object == SEAT)
            assert set(w.offices[SEAT].remit_acts) <= set(new.granted_acts), new.granted_acts
            assert not world_q.docketed(w, CANDIDATE), "the matter stayed on the docket"
            carried += 1
        else:
            assert _seat_holders(w, SEAT) == [], (s, out[0].degree)
    assert checked >= 40
    assert carried >= 1, "no seed seated the candidate"


# --- THE REFUSALS: AT THE FOLD AND AT THE GATE, NEVER A DRAW -----------------------------------------------------------------------

def _arm(arm):
    w, d = _church_world(**JUDGE)
    _ought(w, "p_high", "prop_elect")
    actor, via = "p_high", JUDGE_SEAT
    if arm == "ii_king_judges":
        actor, via = "p_king", KING_SEAT
    elif arm == "iii_not_church":
        for t in w.tenures:
            if t.kind == "commit" and t.subject == CANDIDATE and t.object == faction_prop_id(CHURCH):
                t.until = 0
        _commit(w, CANDIDATE, faction_prop_id(CROWN))
    elif arm == "iv_held_seat":
        w.add_tenure(Tenure("t_sitting_confessor", "p_other", SEAT, "hold", since=0))
    elif arm == "v_second_faction":
        _commit(w, CANDIDATE, faction_prop_id(CROWN))
    return w, d, actor, via


@pytest.mark.parametrize("arm", ["ii_king_judges", "iii_not_church", "iv_held_seat", "v_second_faction"])
def test_election_refusals(arm):
    """(ii) the King as judge (a bench of another faction); (iii) a candidate committed to no Church; (iv) a seat with a live hold (one per
    object); (v) a candidate committed to a second faction too. Each is `determine.refused` at the fold -- the `bench` stem asks the gate's
    own `may_elect` -- and the election arm refuses it at the gate. CONTROL (`control`, one clause away): the same world with no arm applied
    is admitted at both, the bare opening as `determination`. (The bare gate still admits an `elected` seat by `conferral` to any seated
    holder whose purview reaches it: `elected` keeps `conferral` until CR-35 (8), B21c.03.)"""
    w, d, actor, via = _arm("control")
    assert _bare_opening(w, actor, via, CANDIDATE, SEAT) == G.DETERMINATION
    assert "determine.refused" not in _kinds(_fold(w, d, _determine("ctl", via=via, actor=actor)))
    w, d, actor, via = _arm(arm)
    holders = _seat_holders(w, SEAT)
    assert not G.may_elect(w, actor, via, CANDIDATE, w.offices[SEAT]), arm
    assert _bare_opening(w, actor, via, CANDIDATE, SEAT) != G.DETERMINATION, arm
    assert _kinds(_fold(w, d, _determine(f"r_{arm}", via=via, actor=actor))) == ["determine.refused"], arm
    assert _seat_holders(w, SEAT) == holders, arm


# --- A-14: THE VOTE IS A DRAW, READ AS SHARES ----------------------------------------------------------------------------------------

def _row(rid):
    from ..data.arrangements import ARRANGEMENTS
    return ARRANGEMENTS[rid]


def _share(arm):
    carried = 0
    for s in SEEDS:
        w, d = _church_world()
        if arm == "committed":
            _ought(w, "p_high", "prop_elect")
            _ought(w, "p_low", "prop_elect")
        elif arm == "plot":
            _ought(w, "p_high", "prop_plot", predicate=G.PLOT_PREDICATE)
            _ought(w, "p_low", "prop_plot", predicate=G.PLOT_PREDICATE)
        _fold(w, d, _determine(f"sh{s}"))
        carried += _holds(w, CANDIDATE, SEAT)
    return carried / len(SEEDS)


def test_uncommitted_bench_carries_less_often():
    """(i-b) no elector committed; (i-c) the electors committed only to a plot OUGHT against the candidate. A-14: the vote is a draw on each
    voter, so neither is refused; each carries LESS OFTEN than the arm whose electors are committed to an OUGHT naming the candidate and the
    seat. The predicate test is read first: a plot OUGHT, or an OUGHT naming another seat, is no vote."""
    w, _ = _church_world()
    _ought(w, "p_high", "prop_plot", predicate=G.PLOT_PREDICATE)
    _ought(w, "p_low", "prop_other_seat", predicate=KING_SEAT)
    assert world_q.declared_votes_by_member(w, CANDIDATE, _row("election")) == {}
    committed, none, plot = _share("committed"), _share("none"), _share("plot")
    assert committed > none and committed > plot, (committed, none, plot)


# --- THE CONTESTED SUCCESSION ----------------------------------------------------------------------------------------------------------

def _succession_world(held=False, **fx):
    w, d = _world(**{**JUDGE, **fx})
    for t in list(w.tenures):
        if t.kind == "hold" and t.object == "off_duke":
            t.until = 0
    _seat(w, THRONE, "King", "R", ["issue", "determine", "confer", "revoke", "convene"], CROWN, "p_king" if held else None, 1,
          conferral="inheritance")
    _seat(w, REGENT_SEAT, "Dicastery", "R", ["issue", "determine"], CROWN, "p_high", 2)
    _seat(w, TITLE, "Heir", "R", ["issue"], CROWN, "p_other", 3, conferral="appointed")
    _commit(w, CANDIDATE, faction_prop_id(CHURCH))          # the rival is of ANY faction: the party's faction clause is dropped
    _petition(w, CANDIDATE, THRONE, "succession")
    return w, d


def test_contested_succession_arms():
    """A rival's petition naming the vacant throne, docketed under `succession`, determined by the Widow Regent (a strong judge) -> the
    rival, a Church man, holds the throne. With a live throne-hold -> refused at the fold and the gate. With the heir's claim executed
    first in the same fold -> the determination declines (one per object): the heir holds the throne, the rival nothing."""
    w, d = _succession_world()
    out = _fold(w, d, _determine("su", via=REGENT_SEAT))
    assert out[0].degree in OPENS, _kinds(out)
    assert _seat_holders(w, THRONE) == [CANDIDATE]

    w, d = _succession_world(held=True)
    assert _bare_opening(w, "p_high", REGENT_SEAT, CANDIDATE, THRONE) is None
    assert _kinds(_fold(w, d, _determine("su_held", via=REGENT_SEAT))) == ["determine.refused"]
    assert _seat_holders(w, THRONE) == ["p_king"]

    w, d = _succession_world()
    claim = Act(id="su_claim", actor="p_other", verb="succeed", payload={"subject": THRONE})
    out = _fold(w, d, claim, _determine("su_race", via=REGENT_SEAT))
    assert _seat_holders(w, THRONE) == ["p_other"], _kinds(out)
    assert "succession.claimed" in _kinds(out) and "determine.refused" in _kinds(out), _kinds(out)
    assert "matter.determined" not in _kinds(out), _kinds(out)
