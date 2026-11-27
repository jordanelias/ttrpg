"""B21b.21 (CR-09 with `H-101`) -- A SWORN HOLDER'S GROUND IS IN HIS LIEGE'S PURVIEW, IN THE SET FORM TOO.

`state/gate.py::purview_reaches` (the predicate) has read the oblige clause since v9 IN-40: a seat also reaches the ground of every seat a
holder of a live, non-imposed `oblige` to it holds. `queries/world_q.py::own_purview` (`reach`'s limb 4, `attention_key`'s tier 1) re-derived
the own-ground walk and missed it, so a liege was never asked about his vassal's ground. B21b.21 routes `own_purview` through
`gate.purview_of`, the predicate's set form over the one clause walk (`gate.sworn_seats`).

Every test drives the governance world (`test_g3_not_yours._gov_world`: R > D > S > Hh; `p_high` on `off_duke` at D; `p_king` on
`off_crown` at R and `off_mayor` at S; `p_other` on `off_duke2` at D2, a sibling duchy OUTSIDE D, living at Hh inside D), plus the
hand-built rungs each test names. No test reads a realm count: in `build_realm(0)` neither canon detachment is expressible (`H-101`).
"""
from __future__ import annotations

from ..data.matrix import WriteClass
from ..loop.driver import mint_token
from ..queries import faction_q, world_q
from ..state.carriers import DETERMINED_BY, Act, Person, Rung, Tenure
from ..state.gate import purview_reaches, seat_faction
from .test_g3_not_yours import _gov_world, _seat_on

DUKE, VIA_D = "p_high", "off_duke"
KING, VIA_K = "p_king", "off_crown"
VASSAL, VASSAL_SEAT = "p_other", "off_duke2"     # his seat's ground, D2, lies OUTSIDE D


def _swear(w, pid, seat, **kw):
    w.add_tenure(Tenure(f"t_oath_{pid}_{seat}", pid, seat, "oblige", 0, **kw))


def _rung(w, rid, kind, parent=None):
    w.rungs[rid] = Rung(rid, kind)
    if parent is not None:
        w.add_tenure(Tenure(f"t_{rid}_in_{parent}", rid, parent, "contain", 0))


def _person(w, pid):
    w.persons[pid] = Person(pid, pid)
    w.rungs[pid] = Rung(pid, "person")


def _release(w, d, pid, seat):
    """THE DETACHMENT, DRIVEN: the swearer's own `release` of his oath through the shipped fold (`_eff_release`, T-m)."""
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id=f"rel_{pid}", actor=pid, verb="release", payload={"subject": seat})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert "tenure.closed" in {e.kind for e in out}, [e.kind for e in out]


def test_a_sworn_holders_ground_outside_the_liege_seat_is_in_own_purview():
    """THE FALSIFIER. `p_other` holds `off_duke2` at D2 (with a settlement S2 under it), outside the Duke's own ground. Sworn to the
    Duke's seat, D2 and S2 enter `own_purview` and `reach` for the Duke, as `purview_reaches` already said. The swearer gains nothing over
    the Duke's ground (not upward). CONTROL: the same world before the oath, where neither is reached."""
    w, _ = _gov_world()
    _rung(w, "S2", "settlement", parent="D2")
    duke, high = w.offices[VIA_D], w.persons[DUKE]
    assert not purview_reaches(w, duke, "D2"), "fixture: D2 is outside the Duke's own ground"
    assert {"D2", "S2"}.isdisjoint(world_q.own_purview(w, high))
    assert {"D2", "S2"}.isdisjoint(world_q.reach(w, high))
    _swear(w, VASSAL, VIA_D)
    assert purview_reaches(w, duke, "D2") and purview_reaches(w, duke, "S2"), "fixture: the oblige clause fires"
    assert {"D2", "S2"} <= world_q.own_purview(w, high)
    assert {"D2", "S2"} <= world_q.reach(w, high), "a claim about the sworn ground is admitted by reach"
    assert "D" not in world_q.own_purview(w, w.persons[VASSAL]), "the swearer's seat gains nothing over the seat he swore to"


def test_own_purview_equals_purview_reaches_over_every_rung():
    """THE SET FORM AND THE PREDICATE READ ONE RULE, over every rung of a world carrying all three cases at once: the Duke's own ground,
    a sworn seat's ground outside it (D2), and an IMPOSED oblige from the holder of the realm seat (a sentence, no oath, so R is reached
    by neither). The Duke holds one seat and his other edges name rungs inside it, so membership equals the predicate exactly."""
    w, _ = _gov_world()
    _rung(w, "S2", "settlement", parent="D2")
    _swear(w, VASSAL, VIA_D)
    _swear(w, KING, VIA_D, payload={DETERMINED_BY: VIA_D})
    duke, high = w.offices[VIA_D], w.persons[DUKE]
    assert [t.object for t in high.tenures if t.live and t.kind == "hold"] == [VIA_D], "fixture: one seat"
    mine, checked = world_q.own_purview(w, high), 0
    for r in w.rungs:
        assert (r in mine) == purview_reaches(w, duke, r), r
        checked += 1
    assert checked >= len(w.rungs)
    assert "D2" in mine and "R" not in mine, "fixture: both the sworn and the imposed arms are exercised"


def test_a_detachment_drops_the_ground_at_both_scales():
    """THE TWO CANON DETACHMENTS, HAND-BUILT [ASSUMPTION: names], each a sworn holder's `release` driven through the fold.
      * EHRENWALL SPLIT (the faction scale): the Löwenritter Grand Master, seated at a commandery L outside the realm's ground, swears
        to the Crown's seat; the Löwenritter is under the Crown -- `faction_q.subordinates(off_crown)` names the holder of a
        Löwenritter seat -- and the King is asked about L. He releases: both drop.
      * JARNSTAL DRIFT (the office scale): Cardinal Jarnstal, seated at T5, swears to the Confessor's seat at T9 (a sibling, outside
        it); the Confessor reaches T5. He releases: both drop.
    No stored parent anywhere: each "under" is the swearer's own `oblige`, and each detachment writes nothing but its close."""
    w, d = _gov_world()
    king = w.persons[KING]
    _rung(w, "L", "duchy")                                          # a root: outside the realm's ground
    _person(w, "p_grand_master")
    _seat_on(w, "p_grand_master", "off_grand_master", "Grand Master", "L", faction="Löwenritter")
    _rung(w, "T9", "duchy", parent="R")
    _rung(w, "T5", "duchy", parent="R")
    _person(w, "p_confessor")
    _person(w, "p_jarnstal")
    _seat_on(w, "p_confessor", "off_confessor", "Confessor", "T9", faction="Church of Solmund")
    _seat_on(w, "p_jarnstal", "off_cardinal_jarnstal", "Cardinal", "T5", faction="Church of Solmund")
    confessor = w.persons["p_confessor"]
    assert "L" not in world_q.own_purview(w, king) and "T5" not in world_q.own_purview(w, confessor), "fixture: neither is under"

    _swear(w, "p_grand_master", VIA_K)
    _swear(w, "p_jarnstal", "off_confessor")
    assert "p_grand_master" in faction_q.subordinates(w, VIA_K) and seat_faction(w, "off_grand_master") != seat_faction(w, VIA_K)
    assert "L" in world_q.own_purview(w, king) and purview_reaches(w, w.offices[VIA_K], "L")
    assert "p_jarnstal" in faction_q.subordinates(w, "off_confessor")
    assert "T5" in world_q.own_purview(w, confessor) and purview_reaches(w, w.offices["off_confessor"], "T5")

    _release(w, d, "p_grand_master", VIA_K)
    assert "p_grand_master" not in faction_q.subordinates(w, VIA_K)
    assert "L" not in world_q.own_purview(w, king) and not purview_reaches(w, w.offices[VIA_K], "L")
    assert "T5" in world_q.own_purview(w, confessor), "the Split detaches the Löwenritter alone"
    _release(w, d, "p_jarnstal", "off_confessor")
    assert "p_jarnstal" not in faction_q.subordinates(w, "off_confessor")
    assert "T5" not in world_q.own_purview(w, confessor) and not purview_reaches(w, w.offices["off_confessor"], "T5")
    assert w.offices["off_grand_master"].rung == "L" and w.offices["off_cardinal_jarnstal"].rung == "T5", "each keeps his own seat"
