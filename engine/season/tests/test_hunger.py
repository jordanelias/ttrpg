"""REM-50 -- `world_q.hunger(w, S)`: a settlement's hunger as a derived Query, and its line in `census`.

WHAT IS ASKED: it reads and writes nothing and `census` reports it, on `harness/scarce.build` (h); and on the
built realm every populated settlement starves before the first yield (i).

`hunger` has no caller in the loop (REM-51 is cut): only `census` reads it.
"""

from __future__ import annotations

from ..harness import populated as POP
from ..boot.realm import build_realm
from ..harness import scarce as S
from ..queries import world_q


def test_h_it_reads_and_writes_nothing_and_the_census_reports_it():
    w = S.build()
    h0, stores0, log0 = w.content_hash(), {r: dict(x.stores or {}) for r, x in w.rungs.items()}, len(w.log)
    for rid in (S.HUNGRY, S.GRANARY):
        world_q.hunger(w, rid)
    assert w.content_hash() == h0 and len(w.log) == log0
    assert {r: dict(x.stores or {}) for r, x in w.rungs.items()} == stores0
    assert POP.census(w)["hunger_by_settlement"] == {"fed": 1, "starving": 1}
    assert w.content_hash() == h0


def test_i_on_the_built_realm_every_populated_settlement_starves_before_the_first_yield():
    realm = build_realm(0)
    draw = world_q.subsistence_draw(realm)
    hist = POP.census(realm)["hunger_by_settlement"]
    settlements = [r for r in sorted(realm.rungs) if realm.rungs[r].kind == world_q.HUNGER_KIND]
    assert list(hist) == sorted(hist) and sum(hist.values()) == len(settlements) >= 30, hist
    checked = 0
    for rid in settlements:
        if sum(world_q.demanded(realm, rid, draw).values()) > 0:
            assert world_q.hunger(realm, rid, draw)[0] == "starving", rid
            checked += 1
    assert checked >= 30, "the loop asserted nothing: no settlement carried a cohort"
    assert hist.get("starving", 0) == checked
