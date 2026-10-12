"""v9 IN-21 -- FORCE-WEATHER: a keyed seasonal draw on MATTER's yield term (`H-26`).

The draw is `world_q.season_factor_of`, read at the yield step in `loop/matter.py`; its distribution is
the `season_factor_draw` fixture (one tuple of equally likely multipliers per season of the year,
`()` = off). Each test asks the real MATTER barrier, never a re-derivation of the arithmetic.

THE FALSIFIERS, each with the failure it would show:
  * CONTROL: with the draw off, `build_realm(0)`'s content hash is the pre-change reading at build, after
    one season and after two; and, on the one-town world, a declared all-1.0 table (the draw ON but
    degenerate) reads the same as no table over two seasons -- a draw that perturbed the arithmetic
    when it multiplies by 1.0 would move it;
  * DROUGHT: a drought-only table leaves the larder below the control arm's after the same barriers,
    and the control arm emits no `shortfall:` observation where the drought arm does;
  * KEYED: the same seed twice gives one hash; a different seed reads a different factor sequence; the
    factor at a tick is the table's entry at `tick % len(table)` (the season of the year, read off the
    clock and stored nowhere).
"""

from __future__ import annotations

import hashlib

from ..data.matrix import Step, WriteClass
from ..data.requires import SHORTFALL_PREDICATE
from ..harness import populated as POP
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Person, Rung, Site, Tenure
from ..state.world import World

DEFAULT = POP.P.DEFAULT_FIXTURES

# `build_realm(0)`'s content hash, originally on the base commit (068ec322, re-pinned below), taken before this position changed
# anything: at build, after one season, after two. With `season_factor_draw` at its shipped `()` all
# three must still read these.
# RE-PINNED 2026-10-11 (Jordan's ruling "null" on seven `offices.yaml` seats): `Office.revocation` is in
# the content hash, and seven seats moved from `rung_above_same_faction` to `null`. Restoring those seven
# values on the built world reproduces the old three hashes (2d0d1200..., a53cceff..., 286fd568...)
# exactly, so the move is that data change alone.
# RE-PINNED at v9 IN-34, A SCHEMA MOVE DECLARED: `Person.born` adds a field to every person's `repr`,
# which `content_hash` folds, so all three move with the bodies clock at its control (both rates 0).
# Was 5812a959... / 0d4f7ae4... / 6bc6123e.... The ordered (kind, id) event sequence over one and two
# seasons is identical to the pre-IN-34 base's (`BASE_EVENTS`, below), so the move is the field alone.
# RE-PINNED 2026-10-12 (`rung_above_in_holdings`, Jordan's holdings ruling): `off_duchess_hafenmark` and
# `off_duke_varfell` moved from `rung_above_same_faction` to the new basis, a data change alone
# (`Office.revocation` is hashed). Was 0a7e27c4... / d188461a... / 33b1ae3b.... `BASE_EVENTS` below is
# unchanged, which is the proof that no event moved.
BASE_HASHES = {0: "11989dcf5e1c25afab556bf3f234a200",
               1: "c2230a36c97b14ce64dbd0e6cb8fa131",
               2: "88f6f2436eff40f8b52db1b18d5d49c8"}

# The pre-IN-34 base (d47077d5), `build_realm(0)` driven by `POP.run`, seed 0: the whole log's event
# count and the sha256 of its ordered `kind|id` lines after one season and after two. A ONE-TIME PROOF
# that the schema re-pin of `BASE_HASHES` moved nothing at the event level (the hash folds
# `repr(Person)`, which gained a field; the events did not move); re-recorded together with
# `BASE_HASHES`, never alone. A hazard that fired at the control would change the sequence.
BASE_EVENTS = {1: (7526, "e56f8652be7f7cd52352bdf07ef17dcc555daf83e267a37b0eecafc096ec82e7"),
               2: (21508, "dc3c440ad533b0548d69bfdc8b092e3ccc03ff622baa9a5167a92c839c2b42f4")}


def _digest(w) -> tuple:
    seq = [f"{e.kind}|{e.id}" for e in w.log]
    return len(seq), hashlib.sha256("\n".join(seq).encode()).hexdigest()

# H-26's declared sweep, as tables: a year of four seasons each time.
YEAR = 4
DROUGHT = ((0.5,),) * YEAR                    # every season draws the 0.5 point
UNIT = ((1.0,),) * YEAR                        # the draw on, degenerate at the control value
SPREAD = ((0.5, 1.0, 2.0),) * YEAR            # the swept points, equally likely


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


def test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes():
    h, events = {}, {}
    w = POP.build_realm(0)
    h[0] = w.content_hash()
    assert w.fixtures.get("age_step") == 0 and w.fixtures.get("illness_rate") == 0
    for n in (1, 2):
        POP.run(seasons=1, seed=0, w=w)   # continuing one world reads the fresh two-season hash
        h[n] = w.content_hash()
        events[n] = _digest(w)
    assert w.fixtures.get("season_factor_draw") == (), "the shipped default is not the control arm"
    assert h == BASE_HASHES, f"draw off moved a hash: {h}"
    assert events[1][0] >= 5000 and events[2][0] >= 15000, f"the seasons emitted too little: {events}"
    assert events == BASE_EVENTS, f"the bodies clock at its control moved the event sequence: {events}"


def test_in21_a_table_of_ones_reads_the_same_as_no_table():
    """The draw ON but degenerate at 1.0: base * 1.0 is the bare constant. Compared on the one-town
    world (`content_hash` folds state and the log, not fixtures), over two seasons, exactly."""
    off, unit = _town(()), _town(UNIT)
    assert _seasons(off, 2) == _seasons(unit, 2)
    assert off.content_hash() == unit.content_hash(), "a table of 1.0 moved the hash"


def test_in21_drought_leaves_stores_below_control_and_a_drained_larder_reports_shortfall():
    control, c_short = _seasons(_town(()), 2)
    drought, d_short = _seasons(_town(DROUGHT), 2)
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


def test_in21_same_seed_twice_one_hash_and_the_draw_moves_it_off_control():
    a, b = _town(SPREAD, seed=7), _town(SPREAD, seed=7)
    _seasons(a, 6)
    _seasons(b, 6)
    assert a.content_hash() == b.content_hash(), "the same seed twice gave two hashes"
    off = _town((), seed=7)
    _seasons(off, 6)
    assert a.content_hash() != off.content_hash(), "the draw on moved nothing; it is not wired"


def test_in21_the_factor_is_keyed_on_the_seed_and_the_season_of_the_year_is_read_off_tick():
    def factors(seed):
        w = _town(SPREAD, seed=seed)
        out = []
        for t in range(24):
            w.tick = t
            out.append(world_q.season_factor_of(w))
        return out

    seq = {s: factors(s) for s in range(4)}
    assert all(set(f) <= {0.5, 1.0, 2.0} for f in seq.values())
    # FULL SUPPORT, not only a subset: a modulus that never reaches the last outcome (`% (n - 1)`)
    # draws only members of the set and would pass the line above.
    assert set().union(*(set(f) for f in seq.values())) == {0.5, 1.0, 2.0}
    assert len({tuple(f) for f in seq.values()}) > 1, "four seeds drew one sequence; the key ignores the seed"
    assert len(set(seq[0])) > 1, "one seed drew one value for 24 seasons; the key ignores the tick"
    assert factors(0) == seq[0], "the same seed read a different sequence the second time"
    # The season of the year IS tick % len(table): with a distinct single outcome per season the
    # factor is the table's entry at that index, for every tick, and the year wraps.
    year = ((0.5,), (1.0,), (2.0,), (1.5,))
    w = _town(year)
    seen = 0
    for t in range(2 * len(year) + 1):
        w.tick = t
        assert world_q.season_of_year(w) == t % len(year)
        assert world_q.season_factor_of(w) == year[t % len(year)][0]
        seen += 1
    assert seen == 9
    # And no table, no year: the control returns the bare constant and no season.
    w = _town(())
    assert world_q.season_of_year(w) is None
    assert world_q.season_factor_of(w) == DEFAULT.get("season_factor")
