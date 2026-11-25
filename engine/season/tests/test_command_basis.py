"""`16_PESSIMIST_FA_C` edit 1 (V12 B21.19) -- THE COMMAND BASIS: whom a seat may order (A-22), one Query,
`queries/world_q.py::commands(w, actor, via, person_id)`, composed on the three owners that already exist
(`establishment_of` for the sworn, `may_revoke` for the holder of a seat this seat may dismiss,
`purview_reaches` + `place_of` for an unseated person in the seat's land).

Every test drives the Query on the governance world (`test_g3_not_yours._gov_world`: R > D > S > Hh; `p_king`
on `off_crown` at R and `off_mayor` at S; `p_high` on `off_duke` at D, revocable by the seat on the rung above;
`p_other` on `off_duke2` at D2 yet living at Hh, INSIDE D; `p_low`, `p_mid` unseated at Hh). No test reads a
realm count.

`test_dispatch_to_a_stranger_refused` reads `_req_dispatch`, which asks nothing of the order's reach until
B21.21 (`16_PESSIMIST_FA_C` edit 3): EXPECTED RED UNTIL B21.21 (`[skip ci]`).
"""
from __future__ import annotations

from ..loop import predicates as _preds
from ..queries import world_q
from ..state.carriers import Act, Tenure
from ..state.gate import may_revoke, purview_reaches
from .test_g3_not_yours import _gov_world

DUKE, VIA_D = "p_high", "off_duke"
KING, VIA_K = "p_king", "off_crown"
STRANGER = "p_other"             # seated at D2 (another chain of seats), living at Hh inside D


def _move(w, pid, to):
    """Re-home `pid` to the rung `to`: the `contain` and `reside` edges `tiny_world` gave him."""
    for t in w.persons[pid].tenures:
        if t.live and t.kind in ("contain", "reside"):
            t.object = to


def _swear(w, pid, seat):
    w.add_tenure(Tenure(f"t_oath_{pid}", pid, seat, "oblige", 0))


def test_sworn_man_is_commanded_wherever_he_lives():
    """An unseated man living in D2, outside the Duke's land, is not his until he swears to the Duke's seat;
    sworn, he is, though the Duke's purview still does not reach his home. CONTROL: the same man before the oath."""
    w, _ = _gov_world()
    _move(w, "p_low", "D2")
    duke = w.offices[VIA_D]
    assert not purview_reaches(w, duke, world_q.place_of(w, "p_low")), "fixture: his home is not the Duke's land"
    assert world_q.commands(w, DUKE, VIA_D, "p_low") is False
    _swear(w, "p_low", VIA_D)
    assert "p_low" in world_q.establishment_of(w, VIA_D), "fixture: the oath is live"
    assert world_q.commands(w, DUKE, VIA_D, "p_low") is True
    assert not purview_reaches(w, duke, world_q.place_of(w, "p_low")), "he is commanded by the oath, not by the land"


def test_seated_resident_not_sworn_not_revocable_is_not_commanded():
    """THE FALSIFIER. `p_other` holds a seat in another chain (D2, under the same R) and lives at Hh, inside the
    Duke's purview. The old basis (purview of his home) reads him ordered; the command basis does not. CONTROL:
    sworn to the Duke's seat, the same man is commanded."""
    w, _ = _gov_world()
    duke = w.offices[VIA_D]
    assert purview_reaches(w, duke, world_q.place_of(w, STRANGER)), "fixture: the old basis would admit him"
    assert w.seat_holds(STRANGER) and not may_revoke(w, DUKE, VIA_D, w.offices["off_duke2"]), "fixture"
    assert world_q.commands(w, DUKE, VIA_D, STRANGER) is False
    _swear(w, STRANGER, VIA_D)
    assert world_q.commands(w, DUKE, VIA_D, STRANGER) is True


def test_unseated_resident_is_commanded_by_the_land_lord():
    """`p_mid` is unseated and lives at Hh, in D: the Duke's and the King's. The seat at D2 reaches no part of D.
    CONTROL: seating him on a seat that is neither sworn nor revocable by the Duke takes him out of the Duke's command."""
    w, _ = _gov_world()
    assert world_q.commands(w, DUKE, VIA_D, "p_mid") is True
    assert world_q.commands(w, KING, VIA_K, "p_mid") is True
    assert world_q.commands(w, STRANGER, "off_duke2", "p_mid") is False
    w.add_tenure(Tenure("t_seat_mid", "p_mid", "off_duke2", "hold", 0))
    assert world_q.commands(w, DUKE, VIA_D, "p_mid") is False


def test_holder_of_a_revocable_seat_is_commanded():
    """The King holds `off_mayor` (at S), which the Duke's seat (the rung above S, same faction) may revoke; the King
    lives at R, which the Duke's purview does not reach, so the seat he holds is the only route. The Duke is commanded
    by the King the same way (`off_duke`, revocable from `off_crown`). CONTROL: the King does not command the Duke's
    seat-mate across chains, and the Duke does not command the holder of `off_duke2`."""
    w, _ = _gov_world()
    assert not purview_reaches(w, w.offices[VIA_D], world_q.place_of(w, KING)), "fixture"
    assert may_revoke(w, DUKE, VIA_D, w.offices["off_mayor"]), "fixture"
    assert world_q.commands(w, DUKE, VIA_D, KING) is True
    assert world_q.commands(w, KING, VIA_K, DUKE) is True
    assert world_q.commands(w, DUKE, VIA_D, STRANGER) is False


def test_dispatch_to_a_stranger_refused():
    """EXPECTED RED UNTIL B21.21: the Duke's `dispatch` to the seated stranger of another chain is refused by
    `_req_dispatch`; to a man sworn to the Duke's seat it is admitted."""
    w, _ = _gov_world()
    send = lambda to: Act(id=f"d_{to}", actor=DUKE, verb="dispatch", via=VIA_D, payload={"subject": to})
    assert _preds._req_dispatch(w, send(STRANGER)) is False
    _swear(w, STRANGER, VIA_D)
    assert _preds._req_dispatch(w, send(STRANGER)) is True
