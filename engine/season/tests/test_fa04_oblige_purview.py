"""v9 FA-04 (batch B-X, B-X2) -- THE LÖWENRITTER IS A SUBFACTION OF THE CROWN BY ITS GRAND MASTER'S OATH.

`offices.yaml`'s `off_king` row gains `obligees: ["NPC-070"]` (Lisbeth Ehrenwall, the Grand Master); the
world-gen pass over `obligees:` (`harness/populated.py`) turns it into one `oblige` Tenure, with no term,
from her to the King's seat. "Under" is that edge and nothing else (`IN-40`, `H-101`): no parent is stored.
Each fact below is asked of the real build, the real `faction_q` queries and the real fold.

⚠ THE SEAT'S ID IS `off_npc_020`, NOT `off_king`. `off_king` is the ROW's id; NPC-020's seat is
LOOP-BUILT, and a loop-built seat keeps its `off_<holder>` id (`offices.yaml`'s header), so the edge's
object is `w._office_census["authored"]["off_king"]`, which this file resolves rather than assumes.

THE EXIT AND THE FALSIFIER, each with the mutation that turns it red:
  1. `faction_q.superiors(w, "p_npc_070") == [the King's seat]` and `subordinates(w, <it>)` holds her.
     Mutation: empty `off_king`'s `obligees:` (red at both).
  2. HER OWN `release` OF THE OATH, through the real fold, ends `superiors` -> `[]` (the Split as an act;
     CONTROL: before the act it reads the King's seat, in the same world). Mutation: drop the `live` test
     in `faction_q.superiors` (red at the `[]`).
  3. LISTING HER AMONG HER OWN SEAT'S OBLIGEES REFUSES (`populated.py`: the occupant is not his own seat's
     obligee). CONTROL: the real roster builds. Mutation: delete the `opid == holder_pid` raise.
"""

from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..gaps import Forbidden
from ..harness import populated as POP
from ..loop.driver import SeasonDriver, mint_token
from ..queries import faction_q
from ..state.carriers import Act

GRAND_MASTER = "p_npc_070"


def _kings_seat(w) -> str:
    seat = w._office_census["authored"]["off_king"]
    assert w.offices[seat].post == "King" and seat == "off_npc_020", seat
    return seat


def test_fa04_the_grand_master_is_under_the_kings_seat_at_build():
    w = POP.build_realm(0)
    seat = _kings_seat(w)
    assert faction_q.superiors(w, GRAND_MASTER) == [seat]
    assert GRAND_MASTER in faction_q.subordinates(w, seat)
    [t] = [t for t in w.tenures if t.kind == "oblige" and t.subject == GRAND_MASTER and t.live]
    assert t.object == seat and t.term is None, "a seeded oath has no opening act to declare a term"


def test_fa04_her_own_release_of_the_oath_ends_it_through_the_fold():
    w = POP.build_realm(0)
    seat = _kings_seat(w)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    assert faction_q.superiors(w, GRAND_MASTER) == [seat], "control: the oath stands before she acts"
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS),
                    [Act(id="fa04_split", actor=GRAND_MASTER, verb="release", payload={"subject": seat})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    assert [e.kind for e in out] == ["tenure.closed"], [e.kind for e in out]
    assert faction_q.superiors(w, GRAND_MASTER) == []
    assert GRAND_MASTER not in faction_q.subordinates(w, seat)


def test_fa04_a_seat_may_not_list_its_own_holder_among_its_obligees_the_grand_masters_seat():
    real = POP.OFFICES_SEATS
    grand = next(r for r in real if r["id"] == "off_grand_master")
    assert grand["holder"] == "NPC-070" and "NPC-070" not in (grand.get("obligees") or ()), (
        "control: the real row does not list her")
    POP.build_realm(0)                                  # the real roster builds
    rows = [dict(r, obligees=["NPC-070"]) if r is grand else r for r in real]
    mp = pytest.MonkeyPatch()
    try:
        mp.setattr(POP, "OFFICES_SEATS", rows)
        with pytest.raises(Forbidden) as red:
            POP.build_realm(0)
    finally:
        mp.undo()
    assert "off_grand_master" in str(red.value) and "own holder" in str(red.value), str(red.value)
