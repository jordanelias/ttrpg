"""v9 IN-21 -- FORCE-WEATHER: a keyed seasonal draw on MATTER's yield term (`H-26`).

The draw is `world_q.season_factor_of`, read at the yield step in `loop/matter.py`; its distribution is
the `season_factor_draw` fixture (one tuple of equally likely multipliers per season of the year,
`()` = off). Each test asks the real MATTER barrier, never a re-derivation of the arithmetic.

THE FALSIFIERS, each with the failure it would show:
  * CONTROL: on the one-town world, a declared all-1.0 table (the draw ON but degenerate) reads the same as
    no table over two seasons -- a draw that perturbed the arithmetic when it multiplies by 1.0 would move it
    (the realm's own hashes are `_realm_goldens.py`'s);
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
from ..boot.realm import build_realm
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Person, Rung, Site, Tenure
from ..state.world import World

DEFAULT = POP.P.DEFAULT_FIXTURES


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


#: The one-season event count and digest of the season with `thread_read` added to `withheld_verbs`, a change
#: detector: it must differ from the shipped season (`_realm_goldens.SHIPPED`), which is what the test below reads.
#: Its re-record history is in `git log`; the constants it was once recorded against (`BASE_HASHES`, `BASE_EVENTS`) are gone.
THREAD_READ_WITHHELD_EVENTS_1 = (12584, "6670c94255c1c18cf43e91f617600dbb992a99050b1cf1deb48b0f1134d7b219")   # B06/B14 merge re-pin (B14's combat record read against the keyed stream): was (12604, 6b918b8c...)   # B06.99 re-pin (the uniform's source changes from CPython's generator to the keyed mix, B06.04; a stream change, not a balance change): was (14150, d120e7df...)   # B05.99 re-pin (the B05 movers, `_realm_goldens.py`'s list): was (14276, 23047403...)   # B01 re-pin (B11 lane A, both commits rebased): was (13366, b7632953...); B10-13 pin commit: was 13441 / 9f23e5f1...   # CP-T03-08: was 13387 / 1cdf25c4...   # CP-T03-04: was 13386 / 2cea2d08...   # CR-87: was 11767 / c35ef751...   # PC-10b: was 11586 / 860b0d23...   # CP-T03-09: was 11582 / e23a1f6e...   # REM-30 rows: was 11852 / e6f3edeb...   # REM-31: was 11799 / 07b7a36b...   # CR-86: was 11781 / 43774342...   # CR-17: was 10316 / af2eb292...; CR-25: was 10847 / 83f4c9a2...; CR-81: was 9741 / 1e77a5a4...


def test_the_thread_read_withheld_arm_is_pinned_and_differs_from_the_shipped_season():
    """THE THREAD-READ-WITHHELD ARM, A CHANGE DETECTOR: `thread_read` added to the shipped `Fixtures
    withheld_verbs` reads `THREAD_READ_WITHHELD_EVENTS_1` -- the arm's own event count and digest on the IN-59 tree, no
    longer the PRE-K-3 sequence it was recorded as at K-3 (IN-59 (a) moved that arm too; see the
    constant's comment) -- and that differs from the shipped season's own event sequence, read in process, so
    `thread_read`'s formation still moves what a season does. The K-3-time control (the arm equalling the
    pre-K-3 sequence) can no longer be read on one tree."""
    w = build_realm(0)
    shipped = tuple(w.fixtures.get("withheld_verbs"))
    assert "thread_read" not in shipped, "fixture: `thread_read` is already withheld at the shipped arm"
    w.fixtures = w.fixtures.sweep("withheld_verbs", shipped + ("thread_read",))
    POP.run(seasons=1, seed=0, w=w)
    assert _digest(w) == THREAD_READ_WITHHELD_EVENTS_1, _digest(w)
    s = build_realm(0)
    POP.run(seasons=1, seed=0, w=s)
    assert THREAD_READ_WITHHELD_EVENTS_1 != _digest(s), "the arm equals the shipped season -- withholding `thread_read` moved nothing"


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
