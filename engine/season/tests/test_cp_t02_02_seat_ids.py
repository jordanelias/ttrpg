"""CP-T02-02 -- A BUILT SEAT KEEPS ITS AUTHORED ID (H-230 limit 2).

`harness/populated.py::_seat_id` is the one choice of a loop-built seat's Office id: the `offices.yaml`
row's id where a row stands for the seat (the throne is `off_king`, the heir's seat `off_heir`), else the
registry slug (NPC-084's `guild leader` has no row). The "old" side below is the SAME builder with
`_seat_id` replaced by the pre-change slug rule, never a stored copy of the old world.

  (a) FALSIFIER: in `build_realm(0)` every `offices.yaml` seat is an Office under its own row id, and the
      census map `authored` is the identity map; the unauthored seat keeps its slug id.
  (b) `goal_referents` for `goal_crown_peninsular_sovereignty` names the same holder under old and new
      ids (else the seeding map was load-bearing somewhere else).
  (c) CONTROL: old and new worlds hold the same multiset of (post, rung, holder); only ids differ.
  (d) MUTATION (run below): reverting the choice to the slug turns (a) red.
"""
from __future__ import annotations

from collections import Counter

from ..data.rosters import OFFICES_SEATS
from ..harness import populated
from ..queries import world_q

GOAL = "goal_crown_peninsular_sovereignty"


def _slug_id(row, cid):
    """The pre-CP-T02-02 rule: every loop-built seat is `off_<case slug>`."""
    return f"off_{populated._slug(cid)}"


def _old_world(monkeypatch):
    monkeypatch.setattr(populated, "_seat_id", _slug_id)
    return populated.build_realm(0)


def _holders(w):
    """seat id -> the persons with a live `hold` on it (`w.tenures` order)."""
    out: dict = {}
    for t in w.tenures:
        if t.kind == "hold" and t.live and t.object in w.offices:
            out.setdefault(t.object, []).append(t.subject)
    return out


def _referents(w):
    prop = w.propositions[GOAL]
    onlooker = next(iter(w.persons.values()))
    return tuple(sorted(world_q.goal_referents(w, onlooker, prop)))


def _row_ids_missing(w):
    return [r["id"] for r in OFFICES_SEATS if r["id"] not in w.offices]


def test_cp_t02_02_every_authored_seat_stands_under_its_row_id():
    w = populated.build_realm(0)
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


def test_cp_t02_02_the_crown_goal_names_the_same_holder_under_old_and_new_ids(monkeypatch):
    new = populated.build_realm(0)
    got_new = _referents(new)
    assert got_new, "control: the goal names a holder (an empty read would equal itself)"
    old = _old_world(monkeypatch)
    assert "off_king" not in old.offices, "control: the old side really is the slug-id world"
    assert _referents(old) == got_new
    assert world_q.goal_referents(new, next(iter(new.persons.values())), new.propositions[GOAL]) == \
        world_q.goal_referents(old, next(iter(old.persons.values())), old.propositions[GOAL])


def test_cp_t02_02_control_only_ids_differ_between_old_and_new(monkeypatch):
    new = populated.build_realm(0)
    old = _old_world(monkeypatch)

    def shape(w):
        h = _holders(w)
        return Counter((o.post, o.rung, tuple(h.get(oid, ()))) for oid, o in w.offices.items())

    assert sum(shape(new).values()) == len(new.offices) > 0
    assert shape(new) == shape(old)
    assert set(new.offices) != set(old.offices), "control: the ids really differ"
    assert len(new.offices) == len(old.offices) and len(new.persons) == len(old.persons)


def test_cp_t02_02_mutation_reverting_the_choice_turns_the_falsifier_red(monkeypatch):
    monkeypatch.setattr(populated, "_seat_id", _slug_id)
    w = populated.build_realm(0)
    assert _row_ids_missing(w), "the slug rule leaves authored row ids unbuilt, so (a) would be red"
