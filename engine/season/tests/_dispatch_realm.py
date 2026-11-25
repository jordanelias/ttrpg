"""THE SHIPPED REALM, WITH THE TWO MARCH SEATS SEATED AS THE ROWS THAT NAME `dispatch` DO (B21.03 fallout; one owner).

A seat holds a remit act iff its row names it (B21.03), and `off_spymaster` and `off_cardinal_prudence` name `[issue]` alone, so the
shipped Spymaster (`p_npc_033`) and Cardinal (`p_npc_013`) no longer hold the `dispatch` that `march` reads, while the fixtures of
the files that import this march them through those seats. Those files observe the march mechanics (the field, the feed, the cohorts),
never who may march, so the one realm they build seats the two grants: the seat's remit gains `dispatch` and the sitting `hold` is
re-stamped through `World._grant_remit(force=True)`, the writer `establish` uses, not a hand-written payload. `offices.yaml` is
untouched (which rows name `dispatch` is ruled); `off_parliamentary_clerk` is left without it (`test_march.py`'s refusal test)."""
from __future__ import annotations

from ..boot.realm import build_realm as _shipped_realm

MARCH_SEATS = (("p_npc_033", "off_spymaster"), ("p_npc_013", "off_cardinal_prudence"))


def realm_seating_dispatch(seed):
    w = _shipped_realm(seed)
    for pid, seat_id in MARCH_SEATS:
        seat = w.offices[seat_id]
        seat.remit_acts = list(seat.remit_acts) + ["dispatch"]
        held = [t for t in w.persons[pid].tenures if t.kind == "hold" and t.object == seat_id and t.live]
        assert len(held) == 1, f"fixture moved: {pid} no longer sits in {seat_id}; re-read it"
        w._grant_remit(held[0], force=True)
        assert "dispatch" in held[0].granted_acts
    return w
