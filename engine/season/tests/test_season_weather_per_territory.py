"""v10 CL-EVENTS (1) -- FORCE-WEATHER IS PER TERRITORY: `world_q.season_factor_of` is keyed on
`(world_seed, tick, territory rung id)` and `ProduceInput.factor` carries the factor per rung (M16 (b)).

This file holds the KEY and the INTERFACE; the arm stays `season_factor_draw = ()` (commit (2), B10-18, is the
live arm), so every test that needs a draw sweeps it on a world of its own, the way `test_season_weather.py`
does. The control is that file's `BASE_HASHES` / `BASE_EVENTS` (the realm, arm off, reads the pre-change hash),
which this change leaves unedited.

THE FALSIFIERS, each with the failure it would show:
  * KEY: with the arm swept on, two territories at one tick draw different factors at some seed. A key that
    drops the territory (`("world", "season_factor")` for everyone) gives every territory one factor and reddens;
  * INTERFACE: the real MATTER barrier hands `settlements.produce` a factor PER RUNG, rungs of one territory read
    one factor, a rung in no territory reads the territory-less key, and the yield each rung is credited with is
    its own territory's draw -- a module that read one factor for every rung would credit one yield everywhere;
  * CONTROL: with the arm at its shipped `()` every rung reads the bare constant and NO DRAW IS MADE (the mint
    is replaced by one that raises), and the yield is the constant's.
"""

from __future__ import annotations

from ..data.matrix import Step, WriteClass
from ..harness import populated as POP
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Rung, Site, Tenure
from ..state.world import World

DEFAULT = POP.P.DEFAULT_FIXTURES

# [JUSTIFIED: a test-fixture size, not a game value -- `test_season_weather.py`'s year: four seasons, each holding the swept points `H-26` declares (0.5 / 1 / 2), equally likely]
SPREAD = ((0.5, 1.0, 2.0),) * 4

# Test data, not a claim about Valoria's economy: one harbour at full condition yields 40 grain and 30 salt a season
# at factor 1 (`test_season_weather.py`'s own reading), so a factor of 0.5 / 1 / 2 yields half / the same / double.
CONTROL_YIELD = {"grain": 40, "salt": 30}

#: territory -> the settlements under it; `None` is the settlement under the realm itself (no territory above it).
LAYOUT = {"terr_a": ("set_a1", "set_a2"), "terr_b": ("set_b",), None: ("set_free",)}


def _world(seed: int, table) -> World:
    """Two territories (the first holding two settlements), one settlement under the realm, and a harbour in each
    settlement. No persons: this reads the yield step, not the larder."""
    w = World(seed, DEFAULT.sweep("season_factor_draw", table))
    scale = w.fixtures.get("condition_scale")
    w.rungs["r_realm"] = Rung("r_realm", "realm", stores=None)
    n = 0
    for terr, settlements in LAYOUT.items():
        if terr is not None:
            w.rungs[terr] = Rung(terr, "territory", stores=None)
            w.add_tenure(Tenure(f"t_in_{n}", terr, "r_realm", "contain", 0))
            n += 1
        for sid in settlements:
            w.rungs[sid] = Rung(sid, "settlement", stores={})
            w.add_tenure(Tenure(f"t_in_{n}", sid, terr or "r_realm", "contain", 0))
            w.sites[f"s_{sid}_harbour"] = Site(f"s_{sid}_harbour", sid, "harbour", condition=scale)
            n += 1
    return w


def _matter(w):
    """MATTER alone, through the real barrier and a real MATTER token (`test_season_weather.py`'s helper)."""
    d = SeasonDriver(w)
    w.step = Step.MATTER
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _yield_of(w, rid: str) -> dict:
    return dict(getattr(w.rungs[rid], "yield"))


def test_cl_events_1_two_territories_at_one_tick_draw_different_factors_at_some_seed():
    """THE KEY'S FALSIFIER. PLANTED FAILURE (run, then reverted): `draw_factory(...)("world", "season_factor")`
    for every territory -- `differing` reads 0 and the last assertion reddens."""
    checked = differing = 0
    for seed in range(8):
        w = _world(seed, SPREAD)
        for t in range(8):
            w.tick = t
            a, b = world_q.season_factor_of(w, "terr_a"), world_q.season_factor_of(w, "terr_b")
            assert {a, b} <= {0.5, 1.0, 2.0}
            assert (a, b) == (world_q.season_factor_of(w, "terr_a"), world_q.season_factor_of(w, "terr_b")), (
                "the same (seed, tick, territory) drew twice and read two factors; the key is not a key")
            checked += 1
            differing += a != b
    assert checked == 64
    assert 0 < differing < checked, f"two territories drew apart at {differing} of {checked} (seed, tick) pairs"


def test_cl_events_1_a_territory_still_draws_every_point_over_the_ticks_and_the_territory_less_key_is_one_more():
    """The territory joins the key; the tick and the seed stay in it. Each territory alone walks more than one value
    over 24 ticks, and `None` (a place in no territory) is a third stream, not the first territory's."""
    w = _world(3, SPREAD)
    streams = {}
    for terr in ("terr_a", "terr_b", None):
        out = []
        for t in range(24):
            w.tick = t
            out.append(world_q.season_factor_of(w, terr))
        assert len(set(out)) > 1, f"{terr} drew one value for 24 seasons; the key ignores the tick"
        streams[terr] = tuple(out)
    assert len(set(streams.values())) == 3, "two of terr_a, terr_b and the territory-less key drew one stream"
    w.tick = 5
    assert world_q.season_factor_of(w) == world_q.season_factor_of(w, None), "the bare call is not the territory-less key"


def test_cl_events_1_matter_hands_produce_a_factor_per_rung_and_each_rung_is_credited_its_territorys_draw(monkeypatch):
    """THE INTERFACE'S FALSIFIER, through the real MATTER barrier. A seed is chosen (non-vacuity) at which the two
    territories draw apart at tick 0; the `ProduceInput` MATTER built is captured as it is handed over."""
    seed = next((s for s in range(16)
                 if world_q.season_factor_of(_world(s, SPREAD), "terr_a") != world_q.season_factor_of(_world(s, SPREAD), "terr_b")),
                None)
    assert seed is not None, "no seed in 0..15 draws the two territories apart at tick 0"
    w = _world(seed, SPREAD)
    seen = []
    real = world_q.produce_input

    def spy(*args, **kwargs):
        seen.append(real(*args, **kwargs))
        return seen[-1]

    monkeypatch.setattr(world_q, "produce_input", spy)
    _matter(w)
    assert len(seen) == 1, "MATTER built the produce record other than once a season"
    inp = seen[0]
    factors = dict(inp.factor)
    rungs = ("set_a1", "set_a2", "set_b", "set_free")
    assert [r for r, _ in inp.factor] == sorted(rungs), f"the factor does not cover the rungs a Site stands on: {inp.factor}"
    assert [r for r, _ in inp.stores] == [r for r, _ in inp.factor], "`factor` and `stores` cover different rungs"
    fa, fb, ff = (world_q.season_factor_of(w, t) for t in ("terr_a", "terr_b", None))
    assert fa != fb
    assert factors == {"set_a1": fa, "set_a2": fa, "set_b": fb, "set_free": ff}, factors
    checked = 0
    for rid, f in factors.items():
        want = {k: int(v * f) for k, v in CONTROL_YIELD.items()}
        assert _yield_of(w, rid) == want, f"{rid}: yielded {_yield_of(w, rid)}, its territory's factor {f} gives {want}"
        assert dict(w.rungs[rid].stores) == want, f"{rid}: credited {dict(w.rungs[rid].stores)}, not its yield {want}"
        checked += 1
    assert checked == 4
    assert _yield_of(w, "set_a1") != _yield_of(w, "set_b"), "two territories drew apart and yielded the same"


def test_cl_events_1_the_control_arm_reads_the_bare_constant_at_every_rung_and_draws_nothing(monkeypatch):
    """THE CONTROL (`season_factor_draw` = `()`, the shipped arm): no mint is touched, every rung reads
    `season_factor`, and every harbour yields the control's 40 and 30."""
    w = _world(0, ())
    assert w.fixtures.get("season_factor_draw") == (), "fixture: the shipped arm is not `()`"

    def no_draw(*args, **kwargs):
        raise AssertionError("a draw was made with `season_factor_draw` at `()`")

    monkeypatch.setattr(world_q, "draw_factory", no_draw)
    base = DEFAULT.get("season_factor")
    assert world_q.season_factors_by_rung(w) == tuple((r, base) for r in sorted(("set_a1", "set_a2", "set_b", "set_free")))
    assert world_q.season_factor_of(w, "terr_a") == world_q.season_factor_of(w, "terr_b") == world_q.season_factor_of(w) == base
    _matter(w)
    for rid in ("set_a1", "set_a2", "set_b", "set_free"):
        assert _yield_of(w, rid) == {k: int(v * base) for k, v in CONTROL_YIELD.items()}
