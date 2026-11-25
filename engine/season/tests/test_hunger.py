"""REM-50 -- `world_q.hunger(w, S)`: a settlement's hunger as a derived Query, and its line in `census`.

WHAT IS ASKED: it reads and writes nothing and `census` reports it, on `harness/scarce.build` (h); and on the
built realm every populated settlement starves before the first yield (i).

`hunger` has no caller in the loop (REM-51 is cut): only `census` reads it.
"""

from __future__ import annotations

from dataclasses import replace

import pytest

from ..harness import populated as POP
from ..boot.realm import build_realm, place_person
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..gaps import Unspecified, expect_refusal
from ..harness import scarce as S
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..queries.inputs import Eater, LarderInput, SubsistInput
from ..state.carriers import Rung, Tenure
from ..state.world import World
from engine.substrate import composition


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


def test_a_severity_of_two_doubles_the_fall_and_zero_spares_it():
    """B12a.60 (`16_PESSIMIST_GAME_the_world_draws` edit 4): `settlements.subsist`, on a hand-built input with one eater short 3 units
    (wants 5 `grain`, the home holds 2), multiplies the fall by the eater's severity: none given is 1, 2 doubles it, 0 spares it."""
    def fall(severity):
        larder = LarderInput((("grain", 5),), (Eater("p1", "h", 1, True),), (("h", ("h",)),), (("h", (("grain", 2),)),))
        out = composition.require("settlements.subsist")(SubsistInput(larder, (("h", ("h",)),), 4, (("p1", 100),), severity))
        assert out.short_by_person == (("p1", (("grain", 3),)),), "the eater is not short 3: the arm cannot observe the multiplier"
        return {f.pid: f.body_after for f in out.falls}
    assert fall(()) == {"p1": 100 - 4 * 3}
    assert fall((("p1", 1),)) == {"p1": 100 - 4 * 3}
    assert fall((("p1", 2),)) == {"p1": 100 - 4 * 3 * 2}
    assert fall((("p1", 0),)) == {}


# B12a.61 (`16_PESSIMIST_GAME_the_world_draws` edit 3): THE HOST DRAWS THE SEVERITY PER HUNGRY EATER. The world is planted, not read off the realm
# (B12a.55's `granary_seasons` 4 leaves no cohort short at season 0): COHORTS settlements, each holding one cohort at weight 2 (want 6: grain 4,
# salt 2) and an empty larder, so every cohort is short its whole want (depth share 1, obstacle `hunger_depth_obstacle`). THE PLANT'S DEPTH
# [ASSUMPTION; basis: body_step 10 x 6 units short = 60 a season at the control; Failure's multiple 2 makes 120, Partial's 1 makes 60, Success's 0.5
# makes 30, Overwhelming's 0]: bodies at 100, so a Failure (120) kills in season 1, the control's fixed 60 kills every cohort together in season 2, and
# the drawn arm's first deaths fall in season 1 for some cohorts and in season 2 or never for others.
COHORTS, PLANTED_BODY, BASE_FALL = 36, 100, 10 * 6


def _planted(fixtures, seed: int = 0) -> World:
    w = World(world_seed=seed, fixtures=fixtures)
    w.rungs["R"], w.rungs["T"] = Rung("R", "realm"), Rung("T", "territory")
    w.add_tenure(Tenure("t_T", "T", "R", "contain", since=0))
    for i in range(COHORTS):
        sid = f"set{i:02d}"
        w.rungs[sid] = Rung(sid, "settlement")
        w.add_tenure(Tenure(f"t_{sid}", sid, "T", "contain", since=0))
        place_person(w, f"c{i:02d}", f"cohort {i}", sid, weight=2, body=PLANTED_BODY)
    w.manifest = {"contest": "seam.contest_resolver", "order": "core.canonical_order"}
    return w


def _seasons(w: World, seasons: int) -> dict:
    """Run MATTER `seasons` times; `{pid: (season it was first gone, or None; body at the end)}` over the cohorts planted (a dead cohort's body reads 0)."""
    pids = sorted(p for p, x in w.persons.items() if x.is_cohort)
    d, first = SeasonDriver(w), {}
    for season in range(1, seasons + 1):
        w.tick += 1
        d.matter(mint_token(w, WriteClass.MATTER), [])
        for pid in pids:
            if pid not in w.persons:
                first.setdefault(pid, season)
    return {pid: (first.get(pid), w.persons[pid].body if pid in w.persons else 0) for pid in pids}


def _arm(draw: bool, **rows):
    f = DEFAULT_FIXTURES.sweep("hunger_severity_draw", draw)
    for name, value in rows.items():
        f = f.sweep(name, value)
    return f


def test_hunger_draw_on_bodies_diverge_and_first_deaths_differ():
    """A planted shortfall on every cohort, two seasons (eight in the source; A-114): with `hunger_severity_draw` on the cohorts' bodies are not all
    equal at the end and the season of first death differs between at least two cohorts. The control (the same plant at `False`) is the synchronized
    death the draw exists to break, one body and one first-death season for every cohort, so the assertions can see it."""
    off = _seasons(_planted(_arm(False)), 2)
    assert set(off.values()) == {(2, 0)}, "the control is not the synchronized death: the plant cannot see the draw"
    on = _seasons(_planted(_arm(True)), 2)
    checked = len(on)
    assert checked >= 30, "the loop asserted nothing: too few cohorts read"
    assert len({body for _, body in on.values()}) > 1, "every cohort ended at one body: the draw is a threshold"
    assert len({first for first, _ in on.values()}) >= 2, f"one first-death season for every cohort: {set(on.values())}"
    assert any(first == 1 for first, _ in on.values()), "no cohort died in season 1: the plant is too shallow to see a Failure"


def test_hunger_draw_off_is_the_base_hash():
    """The control: at `False` (the shipped arm) no `hunger_severity` draw is taken, every cohort falls by exactly `body_step x units short` and so all
    bodies are equal, and the world's hash is the one the same season gives with the projection's severity stripped (`()`, what the base `subsist`
    reads); the drawn arm's hash differs from it, so the equality can fail."""
    drawn, real = [], world_q.draw_factory

    def spy(seed, tick_of):
        keyed = real(seed, tick_of)

        def draw(subject_id, purpose):
            drawn.append(purpose)
            return keyed(subject_id, purpose)
        return draw

    def hash_after(fixtures, strip: bool = False) -> str:
        w, real_input = _planted(fixtures), world_q.subsist_input
        if strip:
            world_q.subsist_input = lambda x: replace(real_input(x), severity=())
        try:
            _seasons(w, 1)
        finally:
            world_q.subsist_input = real_input
        return w.content_hash()

    world_q.draw_factory = spy
    try:
        w = _planted(_arm(False))
        ended = _seasons(w, 1)
    finally:
        world_q.draw_factory = real
    assert "hunger_severity" not in drawn, "the control took a hunger draw"
    assert len(ended) >= 30 and {body for _, body in ended.values()} == {PLANTED_BODY - BASE_FALL}, ended
    base = hash_after(_arm(False), strip=True)
    assert w.content_hash() == base
    assert hash_after(_arm(True)) != base, "the drawn arm moved nothing: the control cannot fail"


@pytest.mark.parametrize("row, bad", [("hunger_band_steps", {"Overwhelming": 0.0, "Success": 0.5, "Partial": 1.0}),
                                     ("hunger_band_steps", {"Overwhelming": 0.0, "Success": 0.5, "Partial": 1.0, "Failure": 2.0, "Fatal": 3.0}),
                                     ("hunger_body_pool", None), ("hunger_depth_obstacle", None)])
def test_the_arm_refuses_a_row_that_is_not_the_ladders(row, bad):
    """The arm on a `hunger_band_steps` whose keys are not exactly the ladder's four bands, or on a body or depth row left unset, refuses naming the row
    (`Unspecified`) and writes no body; the control (`False`) reads none of them and the season runs."""
    w = _planted(_arm(True, **{row: bad}))
    with expect_refusal(), pytest.raises(Unspecified, match=row):
        _seasons(w, 1)
    assert all(p.body == PLANTED_BODY for p in w.persons.values()), "the refused arm wrote a body"
    assert len(_seasons(_planted(_arm(False, **{row: bad})), 1)) == COHORTS
