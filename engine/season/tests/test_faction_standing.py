"""`queries/faction_q.py::standing` -- one composed, resolver-side reading of where a faction stands
(B03.65; `U5a_CORE_owed_edits` §I). It is the first reader of `world_q.footprint`, `density`,
`sovereign_fraction` and `provinces_of`, which no caller outside tests reached before.

  (a) `standing(...).footprint` IS `world_q.footprint(w, f)` for every faction that holds, and is
      non-empty: the record composes the Query, it does not re-derive a second footprint.
  (b) at the realm rung, `present` never exceeds `persons`, summed over every faction as well as
      for each one: a faction's members present cannot outnumber the persons present.

Both run on `build_realm(0)` played one season, and each asserts that it checked something
(CLAUDE.md §0.1 pt 2).
"""
from __future__ import annotations

import pytest

from engine.season.data.rosters import FACTION_BY_PROP
from engine.season.harness import populated as POP
from engine.season.queries import faction_q as FQ
from engine.season.queries import world_q as Q

REALM = "r_valoria"


@pytest.fixture(scope="module")
def realm():
    w = POP.build_realm(0)
    POP.run(1, 0, w=w)
    return w


def _holds(w, prop: str) -> bool:
    """A faction with a live hold: some live `hold` Tenure whose subject is a member of it (or the
    faction itself) and whose object is a rung. Read off `w.tenures`, not off the Query under test."""
    inside = set(Q.members(w, prop)) | {prop}
    return any(t.kind == "hold" and t.live and t.subject in inside and t.object in w.rungs
               for t in w.tenures)


def test_standing_footprint_equals_footprint_for_every_holding_faction(realm):
    w = realm
    checked = 0
    for prop in FACTION_BY_PROP:
        if not _holds(w, prop):
            continue
        got = FQ.standing(w, prop, REALM)
        assert got.footprint, f"{prop} holds a rung and its standing has an empty footprint"
        assert list(got.footprint) == Q.footprint(w, prop), prop
        checked += 1
    assert checked >= 1, "no faction with a live hold was checked"


def test_present_never_exceeds_persons_at_the_realm(realm):
    w = realm
    checked = 0
    total_present = 0
    persons = None
    for prop in FACTION_BY_PROP:
        got = FQ.standing(w, prop, REALM)
        assert 0 <= got.present <= got.persons, prop
        persons = got.persons if persons is None else persons
        assert got.persons == persons, "persons present is the rung's, the same for every faction"
        total_present += got.present
        checked += 1
    assert checked >= 1, "no faction was checked"
    assert persons is not None and persons >= 1, "the realm rung holds no persons: nothing to bound"
    assert total_present <= persons
