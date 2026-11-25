"""B12a.10 (`09_WR_B_draws_not_thresholds` edit 1): WEAR IS DRAWN, behind the fixture `wear_draw` (`loop/matter.py`'s Site loop).

THE ARM. Per Site per season one keyed draw `draw_factory(world_seed, tick)(site.id, "wear")`, rolled by the one roller and graded on the
one ladder; the band picks the wear from the kind's rate (+ the lattice pull): Overwhelming 0, Success half, Partial the rate, Failure
twice. ELIGIBILITY is the control's own (`wear == 0` or condition 0 is not written, so draws nothing). `wear_draw: False` is today's rate.

THE WORLD is hand-built: a realm, one territory, harbours at full condition. The two `[CALIBRATE]` rows (`wear_draw_pool`,
`wear_draw_ob_step`) ship `None`, so each arm plants them with `Fixtures.sweep` -- test arms (H-523's sweep), not chosen values.

THE FALSIFIERS, each able to see what it excludes: the draw collapsed into a threshold (two harbours of one condition and kind never
differ, or every seed gives the same wear); the eligibility leaked (a wear-0 kind, or a Site at condition 0, takes a draw); an arm that
runs on an unset calibration row instead of refusing.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..gaps import Unspecified, expect_refusal
from ..loop import matter
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Rung, Site, Tenure
from ..state.world import World

SEEDS = range(20)
POOL, OB_STEP = 4.0, 0.12                     # a test arm (H-523's sweep), not a chosen value
RATE = DEFAULT_FIXTURES.wear("harbour")


def _fixtures(draw: bool = True, pool=POOL, ob_step=OB_STEP):
    f = DEFAULT_FIXTURES.sweep("wear_draw", draw)
    return f.sweep("wear_draw_pool", pool).sweep("wear_draw_ob_step", ob_step)


def _world(seed: int, fixtures, sites: dict) -> World:
    """A realm holding one territory, and `{id: (kind, condition)}` Sites under it."""
    w = World(world_seed=seed, fixtures=fixtures)
    w.rungs["R"] = Rung("R", "realm")
    w.rungs["T"] = Rung("T", "territory")
    w.add_tenure(Tenure("t1", "T", "R", "contain", since=0))
    for sid, (kind, condition) in sites.items():
        w.sites[sid] = Site(sid, "T", kind, condition=condition)
    w.manifest = {"contest": "seam.contest_resolver", "order": "core.canonical_order"}
    return w


def _matter(w: World, seasons: int) -> None:
    d = SeasonDriver(w)
    for _ in range(seasons):
        w.tick += 1
        d.matter(mint_token(w, WriteClass.MATTER), [])


def test_two_harbours_of_equal_condition_and_kind_diverge_under_the_draw_at_some_seed():
    scale = DEFAULT_FIXTURES.get("condition_scale")
    checked, diverged, wears = 0, 0, set()
    for seed in SEEDS:
        w = _world(seed, _fixtures(), {"h_a": ("harbour", scale), "h_b": ("harbour", scale)})
        _matter(w, 2)
        a, b = (scale - w.sites[s].condition for s in ("h_a", "h_b"))
        wears |= {a, b}
        diverged += a != b
        checked += 1
    assert checked >= 20, checked
    assert diverged >= 1, "two harbours of one condition and kind wore alike at every seed: the draw collapsed into a threshold"
    # every drawn two-season total is a sum of the four bands' wears (0, half, the rate, twice), and the draw reaches more than one of them
    assert len(wears) >= 3 and wears <= {x + y for x in (0, RATE // 2, RATE, 2 * RATE) for y in (0, RATE // 2, RATE, 2 * RATE)}, wears


def test_a_wear_zero_kind_draws_nothing():
    """ELIGIBILITY: a dwelling wears 0 and a harbour already at condition 0 is not written; neither takes a keyed draw (a spy on the
    factory), while the worn harbour beside them does -- so the arm ran."""
    scale = DEFAULT_FIXTURES.get("condition_scale")
    assert DEFAULT_FIXTURES.wear("dwelling") == 0
    drawn = []
    real = matter.draw_factory

    def spy(seed, tick_of):
        keyed = real(seed, tick_of)

        def draw(subject_id, purpose):
            drawn.append((subject_id, purpose))
            return keyed(subject_id, purpose)
        return draw

    matter.draw_factory = spy
    try:
        checked = 0
        for seed in SEEDS:
            w = _world(seed, _fixtures(), {"d": ("dwelling", scale), "dead": ("harbour", 0), "h": ("harbour", scale)})
            _matter(w, 2)
            assert (w.sites["d"].condition, w.sites["dead"].condition) == (scale, 0), seed
            worn = {e.changes[0].subject for e in w.log if e.kind == "condition.worn"}
            assert worn <= {"h"}, (seed, worn)       # an Overwhelming draw wears 0 and writes nothing, so a subset
            checked += 1
    finally:
        matter.draw_factory = real
    assert checked >= 20, checked
    assert {s for s, p in drawn if p == "wear"} == {"h"}, sorted(set(drawn))
    assert len([1 for s, p in drawn if (s, p) == ("h", "wear")]) == 2 * checked, "one draw per Site per season"


@pytest.mark.parametrize("draw", [False, True])
def test_a_wear_of_zero_is_not_a_write_on_either_arm(draw):
    """B12a.14 (`07_SE_kernel_repairs` B): a Site whose wear this season is 0 -- its kind's, or a drawn Overwhelming -- writes nothing and emits
    no `condition.worn`, so no `condition.worn` reports a condition that did not move. A world of one dwelling and one harbour: the control
    arm emits exactly one per season (the harbour's); the drawn arm emits one exactly in the seasons the harbour's condition moved, and at
    some seed a season draws 0 (observed, so the zero clause is not an unobserved vacuity)."""
    scale = DEFAULT_FIXTURES.get("condition_scale")
    seasons, checked, drawn_zero = 3, 0, 0
    for seed in SEEDS:
        w = _world(seed, _fixtures(draw), {"d": ("dwelling", scale), "h": ("harbour", scale)})
        d = SeasonDriver(w)
        for _ in range(seasons):
            before, logged = w.sites["h"].condition, len(w.log)
            w.tick += 1
            d.matter(mint_token(w, WriteClass.MATTER), [])
            worn = [e for e in w.log[logged:] if e.kind == "condition.worn"]
            moved = w.sites["h"].condition != before
            assert [e.changes[0].subject for e in worn] == (["h"] if moved else []), (draw, seed, worn)   # no worn event without a move
            assert w.sites["d"].condition == scale, "a dwelling at wear 0 moved"
            if not draw:
                assert len(worn) == 1, (seed, worn)                  # the control: one a season, the harbour's, never the dwelling's
            drawn_zero += not moved
            checked += 1
    assert checked >= 20 * seasons, checked
    assert (drawn_zero >= 1) == draw, f"a drawn zero must be reached on the drawn arm only: {drawn_zero}"


@pytest.mark.parametrize("pool, ob_step, row", [(None, OB_STEP, "wear_draw_pool"), (POOL, None, "wear_draw_ob_step"),
                                                (None, None, "wear_draw_pool")])
def test_the_arm_refuses_an_unset_calibrate_row(pool, ob_step, row):
    scale = DEFAULT_FIXTURES.get("condition_scale")
    w = _world(0, _fixtures(True, pool, ob_step), {"h": ("harbour", scale)})
    with expect_refusal(), pytest.raises(Unspecified, match=row):
        _matter(w, 1)
    assert w.sites["h"].condition == scale, "the refused arm wrote a wear"
    # the control reads neither row: unset is the shipped state, and the season is today's
    f = _fixtures(False, pool, ob_step)
    c = _world(0, f, {"h": ("harbour", scale)})
    _matter(c, 1)
    assert c.sites["h"].condition == scale - RATE
