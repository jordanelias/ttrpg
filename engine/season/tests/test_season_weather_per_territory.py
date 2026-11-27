"""v10 CL-EVENTS (1) -- FORCE-WEATHER IS PER TERRITORY: `world_q.season_factor_of` is keyed on
`(world_seed, tick, territory rung id)` and `ProduceInput.factor` carries the factor per rung (M16 (b)).

This file holds the KEY and the INTERFACE; the arm stays `season_factor_draw = ()` (commit (2), B12b.43, is the
live arm), so every test that needs a draw sweeps it on a world of its own, the way `test_season_weather.py`
does, with the band factors planted (the shipped ones are all 1.0). B12b.03 adds the SPELL's key: the year and the
parent rung. The control is that file's `BASE_HASHES` / `BASE_EVENTS` (the realm, arm off, reads the pre-change hash),
which this change leaves unedited.

THE FALSIFIERS, each with the failure it would show:
  * KEY: with the arm swept on, two territories at one tick draw different factors at some seed. A key that
    drops the territory (`("world", "season_factor")` for everyone) gives every territory one factor and reddens;
  * INTERFACE: the real MATTER barrier hands `settlements.produce` a factor PER RUNG, rungs of one territory read
    one factor, a rung in no territory reads the territory-less key, and the yield each rung is credited with is
    its own territory's draw -- a module that read one factor for every rung would credit one yield everywhere;
  * CONTROL: with the arm at its shipped `()` every rung reads the bare constant and NO DRAW IS MADE (the mint
    is replaced by one that raises), and the yield is the constant's;
  * SPELL: the obstacle term of one region for one year is a function of `(seed, year, region)`: two territories under one
    parent read one term in every season of a year, the next year may differ, two parents may differ in one season; a spell with
    no season table, and a table that is not one entry a season, are refused.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import check_season_weather
from ..gaps import Unspecified
from ..queries import world_q
from ..state.carriers import Rung, Site, Tenure
from ..state.world import World
from .test_season_weather import DEFAULT, HARDSHIP, SPREAD_BANDS, UNIT as SPREAD, _matter, _plant


@pytest.fixture(autouse=True)
def _bands(monkeypatch):
    _plant(monkeypatch, SPREAD_BANDS, HARDSHIP)


# Test data, not a claim about Valoria's economy: one harbour at full condition yields 40 grain and 30 salt a season
# at factor 1 (`test_season_weather.py`'s own reading), so a factor of 0.5 / 1 / 2 yields half / the same / double.
CONTROL_YIELD = {"grain": 40, "salt": 30}

#: territory -> the settlements under it; `None` is the settlement under the realm itself (no territory above it).
LAYOUT = {"terr_a": ("set_a1", "set_a2"), "terr_b": ("set_b",), None: ("set_free",)}
RUNGS = tuple(r for rs in LAYOUT.values() for r in rs)          # sorted, as `_site_rungs` returns them


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
    rungs = RUNGS
    assert [r for r, _ in inp.factor] == sorted(rungs), f"the factor does not cover the rungs a Site stands on: {inp.factor}"
    assert [r for r, _ in inp.stores] == [r for r, _ in inp.factor], "`factor` and `stores` cover different rungs"
    fa, fb, ff = (world_q.season_factor_of(w, t) for t in ("terr_a", "terr_b", None))
    assert fa != fb
    assert factors == {"set_a1": fa, "set_a2": fa, "set_b": fb, "set_free": ff}, factors
    checked = 0
    for rid, f in factors.items():
        want = {k: int(v * (f if k in world_q.GROWN_KINDS else 1)) for k, v in CONTROL_YIELD.items()}   # B12b.22: the factor bears on grown kinds only
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
    # B12a.99: `hunger_severity_draw` (shipped True since B12a.62) builds its own `draw_factory` in every MATTER (`world_q._hunger_severity`), which the patch below would read as a
    # weather draw; it is another arm's draw, so it is set at its control here and this test sees only the weather's.
    w.fixtures = w.fixtures.sweep("hunger_severity_draw", False)

    def no_draw(*args, **kwargs):
        raise AssertionError("a draw was made with `season_factor_draw` at `()`")

    monkeypatch.setattr(world_q, "draw_factory", no_draw)
    base = DEFAULT.get("season_factor")
    assert world_q.season_factors_by_rung(w) == tuple((r, base) for r in RUNGS)
    assert world_q.season_factor_of(w, "terr_a") == world_q.season_factor_of(w, "terr_b") == world_q.season_factor_of(w) == base
    _matter(w)
    for rid in RUNGS:
        assert _yield_of(w, rid) == {k: int(v * base) for k, v in CONTROL_YIELD.items()}


# --- the spell (B12b.03, R-27) ---------------------------------------------------------------------------------------------------------
SPELLS = (-1, 0, 1)
#: parent rung -> its territories: `terr_a` and `terr_a2` share `duchy_x`; `terr_b` stands under `duchy_y`.
PARENTS = {"duchy_x": ("terr_a", "terr_a2"), "duchy_y": ("terr_b",)}


def _spell_world(seed: int) -> World:
    w = World(seed, DEFAULT.sweep("season_factor_draw", SPREAD).sweep("season_spell_draw", SPELLS))
    w.rungs["r_realm"] = Rung("r_realm", "realm", stores=None)
    n = 0
    for parent, territories in PARENTS.items():
        w.rungs[parent] = Rung(parent, "duchy", stores=None)
        w.add_tenure(Tenure(f"t_in_{n}", parent, "r_realm", "contain", 0)); n += 1
        for terr in territories:
            w.rungs[terr] = Rung(terr, "territory", stores=None)
            w.add_tenure(Tenure(f"t_in_{n}", terr, parent, "contain", 0)); n += 1
    return w


def _spells_over(w, ticks, territories=("terr_a", "terr_a2", "terr_b")) -> dict:
    out = {}
    for t in ticks:
        w.tick = t
        out[t] = tuple(world_q.season_spell(w, terr) for terr in territories)
    return out


def test_spell_shared_under_one_parent_for_a_year():
    """Two territories under one parent rung read one spell in every season of a year, at every seed (the parent, not the territory, is the key)."""
    checked = 0
    for seed in range(6):
        read = _spells_over(_spell_world(seed), range(8))
        for t, (a, a2, _b) in read.items():
            assert a == a2, f"seed {seed} tick {t}: two territories under one parent read {a} and {a2}"
            checked += 1
        assert read[0] == read[1] == read[2] == read[3] and read[4] == read[5] == read[6] == read[7], f"seed {seed}: the spell moved inside a year"
    assert checked == 48


def test_spell_differs_across_parents_or_years_at_some_seed():
    """Non-vacuity of the key: the spell is not one value everywhere. Two parents differ in one season at some seed, and the next year differs from this one at some seed."""
    across_parents = across_years = 0
    for seed in range(12):
        read = _spells_over(_spell_world(seed), (0, 4))
        across_parents += read[0][0] != read[0][2]
        across_years += read[0][0] != read[4][0]
    assert across_parents > 0, "no seed of 12 read two parents apart in one season: the key dropped the region"
    assert across_years > 0, "no seed of 12 read a year apart from the next: the year is not in the key"


def test_spell_is_a_function_of_seed_year_region():
    """The same inputs read the same spell from a world built afresh, at a tick other than the first of the year, with the draw's other inputs (a different territory under the same parent) changed."""
    w1, w2 = _spell_world(5), _spell_world(5)
    w1.tick, w2.tick = 5, 6                       # the year's second and third seasons
    assert world_q.season_spell(w1, "terr_a") == world_q.season_spell(w2, "terr_a2")
    assert world_q.season_spell(_spell_world(5), "terr_a") in SPELLS


def test_spell_table_without_season_table_refused():
    with pytest.raises(Unspecified) as e:
        check_season_weather((), SPELLS)
    assert "season_spell_draw" in str(e.value)
    w = World(0, DEFAULT.sweep("season_spell_draw", SPELLS))      # a swept arm is refused where it is read
    with pytest.raises(Unspecified):
        world_q.season_factor_of(w)
    check_season_weather(SPREAD, SPELLS)           # non-vacuity: the table beside it is not refused


def test_season_table_length_must_equal_the_year():
    with pytest.raises(Unspecified) as e:
        check_season_weather(SPREAD[:-1], ())
    assert "season_factor_draw" in str(e.value)


def test_ore_and_timber_ignore_the_weather():
    """B12b.22 (`16_PESSIMIST_SE_B` edit 1): the season's factor multiplies the GROWN kinds only. The realm at seed 0, MATTER's yield
    step alone for two seasons, the weather arm on (bands planted, the shipped ones are 1.0) against the arm off: ore and timber
    yield equal the arm-off yield rung for rung and season for season; grain differs. FALSIFIER: ore following the weather
    (`f = factor[rung]` for every kind) reads a differing ore and reddens the second assertion."""
    import copy
    from ..boot.realm import build_realm

    base = build_realm(0)
    on = copy.deepcopy(base)
    on.fixtures = on.fixtures.sweep("season_factor_draw", SPREAD)
    seen = {k: 0 for k in ("ore", "timber", "grain")}
    differs = {k: 0 for k in seen}
    for _ in range(2):
        for w in (base, on):
            _matter(w)
        for rid, rung in base.rungs.items():
            a, b = dict(getattr(rung, "yield", None) or ()), dict(getattr(on.rungs[rid], "yield", None) or ())
            for k in seen:
                if a.get(k) or b.get(k):
                    seen[k] += 1
                    differs[k] += a.get(k, 0) != b.get(k, 0)
        base.tick += 1
        on.tick += 1
    assert all(seen.values()), f"a kind yielded nowhere, so the comparison observed nothing: {seen}"
    assert differs["ore"] == 0 and differs["timber"] == 0, f"a non-grown kind followed the weather: {differs}"
    assert differs["grain"] > 0, "the weather moved no grain; the arm is not on"


def test_yield_receipt_carries_the_produced_map():
    """B12b.25 (A-54, C3-R7): a season's `yield.taken` receipt at a rung carries what the rung produced (sorted pairs) and the band its territory's draw
    landed in; at the control arm the produced map rides with no band. FALSIFIER: a receipt with `spec` empty at a rung that produced. No reader branches on it."""
    w = _world(0, SPREAD)
    _matter(w)
    got = {e.changes[0].subject: e.changes[0] for e in w.log if e.kind == "yield.taken"}
    checked = 0
    for rid in RUNGS:
        pairs, band = got[rid].spec
        assert pairs and pairs == tuple(sorted(_yield_of(w, rid).items())), f"{rid}: spec holds {pairs}, the rung yielded {_yield_of(w, rid)}"
        assert band is not None and band == world_q.season_band_of(w, world_q.enclosing_territory(w, rid)), f"{rid}: band {band}"
        checked += 1
    assert checked == len(RUNGS) == 4
    c = _world(0, ())
    _matter(c)
    ctl = {e.changes[0].subject: e.changes[0].spec for e in c.log if e.kind == "yield.taken"}
    assert len(ctl) == len(RUNGS) and all(pairs and band is None for pairs, band in ctl.values()), ctl
