"""CP-T02-02 -- A BUILT SEAT KEEPS ITS AUTHORED ID (H-230 limit 2).

`harness/populated.py::_seat_id` is the one choice of a loop-built seat's Office id: the `offices.yaml`
row's id where a row stands for the seat (the throne is `off_king`, the heir's seat `off_heir`), else the
registry slug (NPC-084's `guild leader` has no row). The "old" side below is the SAME builder with
`_seat_id` replaced by the pre-change slug rule, never a stored copy of the old world.

  (a) FALSIFIER: in `build_realm(0)` every `offices.yaml` seat is an Office under its own row id, and the
      census map `authored` is the identity map; the unauthored seat keeps its slug id.
"""
from __future__ import annotations

from ..data.rosters import OFFICES_SEATS
from ..boot.realm import build_realm


def _row_ids_missing(w):
    return [r["id"] for r in OFFICES_SEATS if r["id"] not in w.offices]


def test_cp_t02_02_every_authored_seat_stands_under_its_row_id():
    w = build_realm(0)
    assert OFFICES_SEATS and not _row_ids_missing(w), "every offices.yaml seat is an Office under its row id"
    assert "off_king" in w.offices and "off_heir" in w.offices
    census = w._office_census
    assert all(k == v for k, v in census["authored"].items()), "the census map is the identity map"
    assert census["authored"] and len(census["authored"]) >= len(OFFICES_SEATS)
    # a seat with no row keeps its slug id (the guild leader)
    assert census["unauthored"] and all(oid.startswith("off_npc_") for oid in census["unauthored"])
    assert all(oid in w.offices for oid in census["unauthored"])
    # no loop-built seat is left under a slug where a row stands for it
    slugged = [oid for oid in w.offices if oid.startswith("off_npc_") and oid not in census["unauthored"]]
    assert not slugged, slugged
