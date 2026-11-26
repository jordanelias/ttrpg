"""v9 IN-21 -- FORCE-WEATHER: a keyed seasonal draw on MATTER's yield term (`H-26`).

The draw is `world_q.season_factor_of`, read at the yield step in `loop/matter.py`; B12b.03 made it ONE keyed draw on the four-band ladder (pool
the place's endurance, obstacle the season's `hardship` plus the year's spell, the band choosing a factor of `rosters.yaml: season_band_factors`),
and a non-empty `season_factor_draw` (one entry per season of the year, `()` = off) is its switch. Each test asks the real MATTER barrier, never a
re-derivation of the arithmetic; the band factors and hardship are PLANTED here (the shipped factors are all 1.0, the control).

THE FALSIFIERS, each with the failure it would show:
  * CONTROL: on the one-town world, a declared all-1.0 table (the draw ON but degenerate) reads the same as
    no table over two seasons -- a draw that perturbed the arithmetic when it multiplies by 1.0 would move it
    (the realm's own hashes are `_realm_goldens.py`'s);
  * DROUGHT: every band at 0.5 leaves the larder below the control arm's after the same barriers,
    and the control arm emits no `shortfall:` observation where the drought arm does;
  * KEYED: the same seed twice gives one hash; a different seed reads a different factor sequence; the season's hardship at a tick is the
    year's entry at `tick % len(year)` (the season of the year, read off the clock and stored nowhere).
"""

from __future__ import annotations

import hashlib

import pytest

from ..data.matrix import Step, WriteClass
from ..data.requires import SHORTFALL_PREDICATE
from ..data.rosters import SEASONS_OF_YEAR
from ..gaps import Unspecified
from ..harness import populated as POP
from ..boot.realm import build_realm
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Person, Rung, Site, Tenure
from ..state.world import World

DEFAULT = POP.P.DEFAULT_FIXTURES


def _digest(w) -> tuple:
    seq = [f"{e.kind}|{e.id}" for e in w.log]
    return len(seq), hashlib.sha256("\n".join(seq).encode()).hexdigest()

# H-26's switch, as tables: a year of four seasons each time. The entries are read by nothing; the draw's size is `season_band_factors`.
YEAR = 4
UNIT = ((1.0,),) * YEAR                        # the draw on (the shipped band factors are all 1.0: degenerate at the control value)
#: Planted band factors (the shipped ones are 1.0): a drought is every band at 0.5; the spread reads three values over the four bands.
DROUGHT_BANDS = {"Overwhelming": 0.5, "Success": 0.5, "Partial": 0.5, "Failure": 0.5}
SPREAD_BANDS = {"Overwhelming": 2.0, "Success": 1.0, "Partial": 0.5, "Failure": 0.5}
#: Planted hardship by season, so every band has support (pool 6 at the shipped `pool_add`, hardship 0 clears the obstacle in most draws).
HARDSHIP = (0, 2, 4, 6)


def _plant(monkeypatch, bands, hardship=None):
    """Plant the band factors (and, where given, the season's hardship) the shipped control sets to 1.0 and 0."""
    monkeypatch.setattr(world_q, "SEASON_BAND_FACTORS", bands)
    if hardship is not None:
        monkeypatch.setattr(world_q, "SEASON_TERMS", {s: {**t, "hardship": h} for (s, t), h in zip(world_q.SEASON_TERMS.items(), hardship)})


def _matter(w):
    """MATTER alone, through the real barrier and a real MATTER token (the `24f` tests' helper)."""
    d = SeasonDriver(w)
    w.step = Step.MATTER
    return d.matter(mint_token(w, WriteClass.MATTER), [])


# --- a world where the control feeds everyone and a drought does not -----------------------------
# Test data, not a claim about Valoria's economy: one harbour at full condition (40 grain, 30 salt a
# season at factor 1) under a cohort that eats 30 grain and 15 salt a season at the shipped
# `subsistence_weight`, opening with exactly one season's want. Control: surplus every season.
# Drought (x0.5): the yield falls to 20 grain, so the second draw runs the larder dry.
TOWN, COHORT = "set_town", "p_town_folk"
# [JUSTIFIED: a test-fixture size, not a game value -- 15 mouths want 30 grain and 15 salt a season at the shipped weights, sized so a 0.5 yield cannot cover them and a 1.0 yield can]
COHORT_WEIGHT = 15
# [JUSTIFIED: a test-fixture stock, not a game value -- exactly one season's want, so the first draw empties nothing early]
OPENING = {"grain": 30, "salt": 15}


def _town(table, seed: int = 0) -> World:
    w = World(seed, DEFAULT.sweep("season_factor_draw", table))
    scale = w.fixtures.get("condition_scale")
    for rid, kind, stores in (("r_realm", "realm", None), ("terr_town", "territory", None),
                              (TOWN, "settlement", dict(OPENING))):
        w.rungs[rid] = Rung(rid, kind, stores=stores)
    w.add_tenure(Tenure("t_in_0", "terr_town", "r_realm", "contain", 0))
    w.add_tenure(Tenure("t_in_1", TOWN, "terr_town", "contain", 0))
    w.sites["s_town_harbour"] = Site("s_town_harbour", TOWN, "harbour", condition=scale)
    w.persons[COHORT] = Person(COHORT, "the town folk", weight=COHORT_WEIGHT)
    w.rungs[COHORT] = Rung(COHORT, "person")
    w.add_tenure(Tenure("t_folk_in", COHORT, TOWN, "contain", 0))
    w.add_tenure(Tenure("t_folk_home", COHORT, TOWN, world_q.RESIDE_KIND, 0))
    return w


def _seasons(w, n: int):
    """`n` MATTER barriers with the clock advanced between; returns (stores after each, the shortfall
    observations each emitted)."""
    stores, shorts = [], []
    for _ in range(n):
        evs = _matter(w)
        w.tick += 1
        stores.append(dict(w.rungs[TOWN].stores))
        shorts.append([(o.subject, o.predicate, o.value) for e in evs for o in e.observed
                       if str(o.predicate).partition(":")[0] == SHORTFALL_PREDICATE])
    return stores, shorts


#: The one-season event count and digest of the season with `thread_read` added to `withheld_verbs`. A change detector:
#: since B08.03 (scenes fold in their own order) it EQUALS the shipped season (`_realm_goldens.SHIPPED`, seed 0, one season),
#: which is what the test below reads. Its re-record history is in `git log`.
THREAD_READ_WITHHELD_EVENTS_1 = (9447, "57ef8c00332691b3c8ba983ed8493d7e43a1a643eddec4d3efe64cd6d0fe9b4d")   # B21b partial re-record on the merge with B08 and B12a: (8660, 3e0eb0c8..) -> (9447, 57ef8c00..), equal to the shipped season the guards-on realm reads; B12a.99: (9319, e5b3ab7c..) -> (8660, 3e0eb0c8..)




def test_in21_a_table_of_ones_reads_the_same_as_no_table():
    """The draw ON but degenerate at 1.0: base * 1.0 is the bare constant. Compared on the one-town
    world (`content_hash` folds state and the log, not fixtures), over two seasons, exactly."""
    off, unit = _town(()), _town(UNIT)
    assert _seasons(off, 2) == _seasons(unit, 2)
    assert off.content_hash() == unit.content_hash(), "a table of 1.0 moved the hash"


def test_in21_drought_leaves_stores_below_control_and_a_drained_larder_reports_shortfall(monkeypatch):
    control, c_short = _seasons(_town(()), 2)
    _plant(monkeypatch, DROUGHT_BANDS)
    drought, d_short = _seasons(_town(UNIT), 2)
    # Non-vacuity: the control world actually produced and fed (stores moved, nothing short), so a
    # "below control" reading is a difference and not two empty larders.
    assert control[0] == {"grain": 40, "salt": 30}, f"control world is not the one sized: {control[0]}"
    assert drought[0] == {"grain": 20, "salt": 15}, f"drought did not halve the yield: {drought[0]}"
    checked = 0
    for kind in ("grain", "salt"):
        for season in (0, 1):
            assert drought[season][kind] < control[season][kind], (
                f"season {season}: drought {kind} {drought[season][kind]} is not below control "
                f"{control[season][kind]}")
            checked += 1
    assert checked == 4
    assert c_short == [[], []], f"the control arm reported a shortfall: {c_short}"
    # The second draw wants 30 grain of the 20 the drought left: the larder drains, one unit kind short.
    assert d_short[0] == []
    assert d_short[1] == [(TOWN, f"{SHORTFALL_PREDICATE}:grain", 10)], d_short[1]


def test_in21_same_seed_twice_one_hash_and_the_draw_moves_it_off_control(monkeypatch):
    _plant(monkeypatch, SPREAD_BANDS, HARDSHIP)
    a, b = _town(UNIT, seed=7), _town(UNIT, seed=7)
    _seasons(a, 6)
    _seasons(b, 6)
    assert a.content_hash() == b.content_hash(), "the same seed twice gave two hashes"
    off = _town((), seed=7)
    _seasons(off, 6)
    assert a.content_hash() != off.content_hash(), "the draw on moved nothing; it is not wired"


def test_in21_the_factor_is_keyed_on_the_seed_and_the_season_of_the_year_is_read_off_tick(monkeypatch):
    _plant(monkeypatch, SPREAD_BANDS, HARDSHIP)

    def factors(seed):
        w = _town(UNIT, seed=seed)
        out = []
        for t in range(24):
            w.tick = t
            out.append(world_q.season_factor_of(w))
        return out

    seq = {s: factors(s) for s in range(4)}
    assert all(set(f) <= {0.5, 1.0, 2.0} for f in seq.values())
    # FULL SUPPORT, not only a subset: a band the ladder can reach but the draw never does would pass the line above.
    assert set().union(*(set(f) for f in seq.values())) == {0.5, 1.0, 2.0}
    assert len({tuple(f) for f in seq.values()}) > 1, "four seeds drew one sequence; the key ignores the seed"
    assert len(set(seq[0])) > 1, "one seed drew one value for 24 seasons; the key ignores the tick"
    assert factors(0) == seq[0], "the same seed read a different sequence the second time"
    # The season of the year IS tick % len(year): the hardship the draw reads at a tick is the planted year's entry at that index, and the year wraps.
    w = _town(UNIT)
    seen = 0
    for t in range(2 * YEAR + 1):
        w.tick = t
        assert world_q.season_of_year(w) == t % YEAR
        assert world_q.season_term(w, "hardship") == HARDSHIP[t % YEAR]
        seen += 1
    assert seen == 9
    # And no table: the control returns the bare constant, and the year is the roster's, not the table's.
    w = _town(())
    assert world_q.season_of_year(w) == w.tick % len(SEASONS_OF_YEAR)
    assert world_q.season_factor_of(w) == DEFAULT.get("season_factor")


def test_season_of_year_reads_zero_to_three_at_shipped_fixtures():
    """The year is `rosters.yaml: seasons_of_year`, read by `season_of_year` at the shipped fixtures (no
    `season_factor_draw` declared): five ticks read 0, 1, 2, 3, 0 and the answer is never `None`."""
    w = build_realm(0)
    assert not w.fixtures.get("season_factor_draw"), "fixture: the shipped realm declares a weather table"
    read = []
    for t in range(5):
        w.tick = t
        read.append(world_q.season_of_year(w))
    assert read == [0, 1, 2, 3, 0], read


def test_nonempty_season_factor_draw_of_wrong_length_is_refused():
    """A table that is not one entry per season of the declared year is refused where it is first read,
    naming `season_factor_draw`'s length and the year's."""
    wrong = ((1.0,),) * (len(SEASONS_OF_YEAR) - 1)
    w = _town(wrong)
    with pytest.raises(Unspecified) as e:
        world_q.season_factor_of(w)
    assert "season_factor_draw" in str(e.value) and str(len(wrong)) in str(e.value) \
        and str(len(SEASONS_OF_YEAR)) in str(e.value), str(e.value)
    # The right length is not refused (non-vacuity: the refusal is the length, not the table).
    assert world_q.season_factor_of(_town(UNIT)) == DEFAULT.get("season_factor")
