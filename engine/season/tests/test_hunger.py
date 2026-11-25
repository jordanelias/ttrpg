"""REM-50 -- `world_q.hunger(w, S)`: a settlement's hunger as a derived Query, and its line in `census`.

WHAT IS ASKED: it reads and writes nothing and `census` reports it, on `harness/scarce.build` (h); and on the
built realm every populated settlement starves before the first yield (i).

`hunger` has no caller in the loop (REM-51 is cut): only `census` reads it.
"""

from __future__ import annotations

from ..harness import populated as POP
from ..boot.realm import build_realm
from ..data.fixtures import DEFAULT_FIXTURES
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


UNIFORM = DEFAULT_FIXTURES.sweep("endowment_mode", "uniform")


def test_i_on_the_built_realm_every_populated_settlement_starves_before_the_first_yield():
    """KEPT AS WRITTEN UNDER `uniform` (B12a.54): one Site of every kind at every settlement, so every larder is empty at build and the whole
    realm starves at once. The arm is pinned here because the shipped realm is `ground` since the flip; the uniform realm is its control."""
    realm = build_realm(0, fixtures=UNIFORM)
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


def test_i_under_ground_the_shipped_realm_does_not_starve_all_at_once_before_the_first_yield():
    """B12a.54, `test_i` re-recorded under `ground` to assert the opposite on the SHIPPED realm: not every populated settlement starves at build.
    Under `ground` the places differ, so the realm's settlements span more than one band and some cohort is fed. (Not "no cohort short at
    season 0", which `granary_seasons` 0 made false; B12a.55's flip to 4 makes it true, below.) PINNED TO `granary_seasons` 0 (B12a.55): its
    `0 < fed < checked` is that arm's world-gen artefact (some cohort short at build); under the shipped 4 every populated settlement is fed."""
    realm = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("granary_seasons", 0))
    draw = world_q.subsistence_draw(realm)
    hist = POP.census(realm)["hunger_by_settlement"]
    settlements = [r for r in sorted(realm.rungs) if realm.rungs[r].kind == world_q.HUNGER_KIND]
    assert sum(hist.values()) == len(settlements) >= 30, hist
    assert len(hist) >= 2, hist
    checked = fed = 0
    for rid in settlements:
        if sum(world_q.demanded(realm, rid, draw).values()) > 0:
            fed += world_q.hunger(realm, rid, draw)[0] != "starving"
            checked += 1
    assert checked >= 30, "the loop asserted nothing: no settlement carried a cohort"
    assert 0 < fed < checked, (fed, checked)
    assert hist.get("starving", 0) == checked - fed


def test_i_under_ground_no_cohort_is_short_at_season_0():
    """B12a.55 (`07_SE_ground_and_granaries` §5, "no cohort short at season 0"), on the SHIPPED realm (`ground`, `granary_seasons` 4), seed 0: the
    draw the build's stores give leaves no populated settlement unmet, so no cohort under any is short. Control `granary_seasons` 0 under
    `ground`: the same read finds settlements short (22 of the 37 populated at B12a.54's reading)."""
    def short(realm):
        draw = world_q.subsistence_draw(realm)
        rids = [r for r in sorted(realm.rungs) if realm.rungs[r].kind == world_q.HUNGER_KIND
                and sum(world_q.demanded(realm, r, draw).values()) > 0]
        return [r for r in rids if world_q.hunger(realm, r, draw)[2] > 0], len(rids)
    gone, populated = short(build_realm(0))
    assert populated >= 30, "the loop asserted nothing: no settlement carried a cohort"
    assert gone == [], gone
    assert short(build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("granary_seasons", 0)))[0], "the control is not short: the assertion cannot see the failure"
