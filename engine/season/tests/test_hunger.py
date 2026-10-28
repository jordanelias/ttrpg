"""REM-50 -- `world_q.hunger(w, S)`: a settlement's hunger as a derived Query, and its line in `census`.

WHAT IS ASKED, each on `harness/scarce.build` (a town whose cohort is the only eater) through the real
`demanded`/`delivered`, with the expectation recomputed from the fixtures' own `subsistence_weight`:
  * the population term: raising the cohort's weight raises D, lowers `cover`, and moves the band
    toward `starving` (a). CONTROL: the same world at the weights below it;
  * the supply term: removing stores lowers `cover`, restoring them raises it back EXACTLY (b);
  * individuals do not eat: a weight-1 person housed at S changes nothing, while `population` DOES count
    him -- so the reading would move if D were taken from `population` (c). THE MUTATION: D computed
    from `population(w, S)` instead of `demanded` turns (c) red; it was run once at the REM-50 build;
  * the Query is defined for the settlement rung only (d);
  * `()` is the control: no floor band, so only `starving` or `fed`; the register's own sweep is run (e);
  * the floors are strict whole-season comparisons (f), the three STATED LIMITS read as they are (g),
    and it reads and writes nothing (h).

`hunger` has no caller in the loop (REM-51 is cut): only `census` reads it, so a wrong band moves nothing
in play and these tests are what would show it.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import RUNG_KINDS
from ..gaps import Forbidden, InstrumentDefect
from ..harness import populated as POP
from ..harness import register as REG
from ..harness import scarce as S
from ..queries import world_q
from ..state.carriers import Person, Rung, Tenure

#: per-head ration by kind, read off the fixtures the Query reads, never copied
RATION = dict(DEFAULT_FIXTURES.get("subsistence_weight"))
PER_HEAD = sum(RATION.values())
#: severity, mildest first: `fed`, then the floor bands in reverse floor order, then `starving`
SEVERITY = ("fed", *reversed(world_q.HUNGER_FLOOR_BANDS), "starving")


def _stock(seasons: int, weight: int = S.COHORT_WEIGHT) -> dict:
    """Stores holding exactly `seasons` seasons of the ration for a cohort of `weight`, kind by kind."""
    return {k: seasons * weight * v for k, v in RATION.items()}


def _town(weight: int = S.COHORT_WEIGHT, stores: dict | None = None, fixtures=DEFAULT_FIXTURES):
    """`scarce.build`'s hungry settlement, with its cohort re-weighted and its larder re-stocked."""
    w = S.build(fixtures=fixtures)
    w.persons[S.POPULACE].weight = weight
    w.rungs[S.HUNGRY].stores = dict(stores if stores is not None else _stock(5))
    return w


def test_a_raising_the_cohorts_weight_raises_D_lowers_cover_and_moves_the_band_toward_starving():
    base_weight, held = S.COHORT_WEIGHT, 5 * S.COHORT_WEIGHT * PER_HEAD
    rows, checked = [], 0
    for weight in (10, 30, 50, 60, 100):
        w = _town(weight)
        band, cover, unmet = world_q.hunger(w, S.HUNGRY)
        d = sum(world_q.demanded(w, S.HUNGRY).values())
        assert d == weight * PER_HEAD, "D is the cohort's weight times the per-head ration"
        # the oracle for `unmet`, not the Query's own arithmetic: what each kind is short of its held stock
        short = sum(max(0, weight * v - 5 * base_weight * v) for v in RATION.values())
        assert unmet == short and type(unmet) is int
        assert cover == Fraction(held, d), "cover is the exact ratio stores / need, no float"
        rows.append((weight, d, cover, band, unmet))
        checked += 1
    assert checked == 5
    ds, covers = [r[1] for r in rows], [r[2] for r in rows]
    assert ds == sorted(set(ds)), "D rises with every added head"
    assert covers == sorted(set(covers), reverse=True), "cover falls with every added head"
    bands = [SEVERITY.index(r[3]) for r in rows]
    assert bands == sorted(bands), f"the band never eases while the cohort grows: {rows}"
    assert rows[0][3] == "fed" and rows[-1][3] == "starving" and "lean" in {r[3] for r in rows}, rows
    assert rows[-1][4] > 0 and all(r[4] == 0 for r in rows if r[3] != "starving"), (
        "`starving` is exactly `unmet > 0`")


def test_b_removing_stores_lowers_cover_and_restoring_them_raises_it_exactly():
    w = _town()
    before = world_q.hunger(w, S.HUNGRY)
    saved = dict(w.rungs[S.HUNGRY].stores)
    seen = [before[1]]
    # empty one kind, then the other: cover falls at each step and the band ends at `starving`
    for kind in sorted(RATION):
        w.rungs[S.HUNGRY].stores[kind] = 0
        seen.append(world_q.hunger(w, S.HUNGRY)[1])
    emptied = world_q.hunger(w, S.HUNGRY)
    assert seen == sorted(set(seen), reverse=True) and len(seen) == 1 + len(RATION), seen
    assert emptied[0] == "starving" and emptied[1] == 0 and emptied[2] == S.COHORT_WEIGHT * PER_HEAD
    w.rungs[S.HUNGRY].stores = saved
    assert world_q.hunger(w, S.HUNGRY) == before, "restoring the stores restores the reading exactly"
    assert before[0] == "fed" and before[1] == 5 and before[2] == 0


def test_c_an_individual_at_the_settlement_does_not_eat_so_nothing_changes():
    w = _town()
    before = world_q.hunger(w, S.HUNGRY)
    demanded_before = world_q.demanded(w, S.HUNGRY)
    population_before = world_q.population(w, S.HUNGRY)
    w.persons["p_lord"] = Person("p_lord", "a lord", weight=1)
    w.rungs["p_lord"] = Rung("p_lord", "person")
    w.add_tenure(Tenure("t_lord_in", "p_lord", S.HUNGRY, "contain", 0))
    w.add_tenure(Tenure("t_lord_home", "p_lord", S.HUNGRY, world_q.RESIDE_KIND, 0))
    # THE CONTROL THAT MAKES THE MUTATION VISIBLE: the roof counts him, the larder does not. If `hunger`
    # took D from `population`, D (and the band's cover) would move by his one head and this goes red.
    assert world_q.population(w, S.HUNGRY) == population_before + 1
    assert world_q.demanded(w, S.HUNGRY) == demanded_before
    assert world_q.hunger(w, S.HUNGRY) == before
    # and the same at the town's own scarce reading, where the band is `starving`
    scarce = S.build()
    scarce_before = world_q.hunger(scarce, S.HUNGRY)
    scarce.persons["p_lord"] = Person("p_lord", "a lord", weight=1)
    scarce.rungs["p_lord"] = Rung("p_lord", "person")
    scarce.add_tenure(Tenure("t_lord_in", "p_lord", S.HUNGRY, "contain", 0))
    scarce.add_tenure(Tenure("t_lord_home", "p_lord", S.HUNGRY, world_q.RESIDE_KIND, 0))
    assert world_q.hunger(scarce, S.HUNGRY) == scarce_before and scarce_before[0] == "starving"


def test_d_a_rung_that_is_not_a_settlement_raises():
    w = _town()
    checked = 0
    for kind in RUNG_KINDS:
        w.rungs[f"x_{kind}"] = Rung(f"x_{kind}", kind)
        if kind == world_q.HUNGER_KIND:
            world_q.hunger(w, f"x_{kind}")      # a settlement answers (D = 0 here: nobody lives in it)
            continue
        with pytest.raises(InstrumentDefect):
            world_q.hunger(w, f"x_{kind}")
        checked += 1
    assert checked == len(RUNG_KINDS) - 1 and checked >= 7
    with pytest.raises(InstrumentDefect):
        world_q.hunger(w, "no_such_rung")
    with pytest.raises(InstrumentDefect):
        world_q.hunger(w, S.STEWARD)            # the steward's own person rung, from the scarce build
    # a settlement with nobody under it: nothing is demanded, nothing is unmet, the band is `fed`
    assert world_q.hunger(w, f"x_{world_q.HUNGER_KIND}") == ("fed", 0, 0)
    assert world_q.hunger(w, S.GRANARY)[0] == "fed", "the granary's only resident is exempt (weight 1)"


def _band_under(floors, stores, weight=S.COHORT_WEIGHT):
    w = _town(weight, stores, DEFAULT_FIXTURES.sweep("hunger_band_floors", floors))
    return world_q.hunger(w, S.HUNGRY)


def test_e_the_empty_floor_list_is_the_control_and_the_registers_own_sweep_runs():
    # cover 3/2 with every kind held at or above its want: not starving, between one and two seasons
    half = {k: 3 * S.COHORT_WEIGHT * v // 2 for k, v in RATION.items()}
    assert all(held >= S.COHORT_WEIGHT * v for held, v in zip((half[k] for k in RATION), RATION.values()))
    assert _band_under((), half)[0] == "fed" and _band_under((1, 2), half)[0] == "lean"
    # `()` leaves `starving` alone: it is not a floor
    assert _band_under((), {})[0] == "starving" and _band_under((1, 2), {})[0] == "starving"
    assert DEFAULT_FIXTURES.get("hunger_band_floors") == (1, 2), "the shipped arm is the register's default"
    arms = [tuple(a) for a in _sweep_of_the_row()]
    assert () in arms and DEFAULT_FIXTURES.get("hunger_band_floors") in arms and len(arms) == 3
    read = {arm: _band_under(arm, half)[0] for arm in arms}
    assert len(set(read.values())) == len(arms), f"two sweep arms read the same band, so one is not an arm: {read}"
    assert read[()] == "fed" and read[(1, 2)] == "lean" and read[(2, 4)] == "hungry"
    # a floor list that would label the wrong band is refused, not answered
    refused = 0
    # `(1, "2")` is mixed: the type test must refuse it before an ordering of unlike types can raise
    for bad in ((2, 1), (1, 2, 3), (-1,), (1.5,), (True,), ("1",), (1, "2")):
        with pytest.raises(Forbidden):
            _band_under(bad, half)
        refused += 1
    assert refused == 7


def _sweep_of_the_row() -> list:
    """The `sweep:` of the register row whose `site:` names `Fixtures hunger_band_floors`."""
    rows = [r for r in REG.load()["rows"] if "Fixtures hunger_band_floors" in str(r.get("site") or "")]
    assert len(rows) == 1, f"exactly one register row owns the thresholds, found {[r['id'] for r in rows]}"
    assert rows[0]["kind"] == "NUMBER" and rows[0]["grade"] == "assumption"
    return list(rows[0]["sweep"])


def test_f_the_floors_are_strict_whole_season_comparisons():
    # a draw taken from full stores, then the stores read AFTER it (the way MATTER's own record is read):
    # unmet is that draw's 0, and cover is what is left over one season's need
    w = _town(stores=_stock(1))
    draw = world_q.subsistence_draw(w)
    d = S.COHORT_WEIGHT * PER_HEAD
    got, checked = {}, 0
    for left, band in ((d - 1, "hungry"), (d, "lean"), (2 * d - 1, "lean"), (2 * d, "fed")):
        # distribute `left` units over the kinds, whole numbers: all in the first kind, the rest at zero
        first = sorted(RATION)[0]
        w.rungs[S.HUNGRY].stores = {k: (left if k == first else 0) for k in RATION}
        got[left] = world_q.hunger(w, S.HUNGRY, draw)
        assert got[left][0] == band and got[left][1] == Fraction(left, d) and got[left][2] == 0, got[left]
        checked += 1
    assert checked == 4
    # the same stores read with NO draw are the next draw's: the zeroed kind is short, so `starving`
    assert world_q.hunger(w, S.HUNGRY)[0] == "starving"


def test_g_the_stated_limits_read_as_they_are():
    # (1) stores ABOVE the settlement feed the cohort (the walk goes up) but are not counted in A:
    w = _town(stores={})
    w.rungs["terr_march"].stores = _stock(9)
    above = world_q.hunger(w, S.HUNGRY)
    assert above == ("hungry", 0, 0), above
    # (2) stores BENEATH the settlement on a rung no cohort's ladder passes through are counted though
    # never drawn:
    w = _town()
    base = world_q.hunger(w, S.HUNGRY)
    w.rungs["hh_pantry"] = Rung("hh_pantry", "hearth", stores=_stock(4))
    w.add_tenure(Tenure("t_pantry_in", "hh_pantry", S.HUNGRY, "contain", 0))
    beneath = world_q.hunger(w, S.HUNGRY)
    assert beneath[1] == base[1] + 4 and beneath[2] == base[2] == 0
    assert world_q.delivered(w, S.HUNGRY) == world_q.demanded(w, S.HUNGRY), "and the draw is unchanged"
    # (3) only the kinds the cohort EATS are food on hand: ore on the shelf is not cover
    w = _town()
    w.rungs[S.HUNGRY].stores["ore"] = 10_000
    assert world_q.hunger(w, S.HUNGRY) == base
    # (4) A and D sum UNLIKE kinds while the draw substitutes none, so a surplus of one eaten kind lifts
    # `cover` over a floor that another kind sits under: the thin kind at exactly one season reads `lean`
    # beside the other kinds at one season, and `fed` once the others are in surplus
    thin = sorted(RATION)[0]
    one_season = _town(stores=_stock(1))
    assert world_q.hunger(one_season, S.HUNGRY)[0] == "lean"
    glut = {k: (1 if k == thin else 100) * S.COHORT_WEIGHT * v for k, v in RATION.items()}
    masked = world_q.hunger(_town(stores=glut), S.HUNGRY)
    assert masked[0] == "fed" and masked[2] == 0, masked
    assert masked[1] == Fraction(sum(glut.values()), S.COHORT_WEIGHT * PER_HEAD)
    assert glut[thin] == S.COHORT_WEIGHT * RATION[thin], "and the thin kind itself is still one season"


def test_h_it_reads_and_writes_nothing_and_the_census_reports_it():
    w = S.build()
    h0, stores0, log0 = w.content_hash(), {r: dict(x.stores or {}) for r, x in w.rungs.items()}, len(w.log)
    for rid in (S.HUNGRY, S.GRANARY):
        world_q.hunger(w, rid)
    assert w.content_hash() == h0 and len(w.log) == log0
    assert {r: dict(x.stores or {}) for r, x in w.rungs.items()} == stores0
    assert POP.census(w)["hunger_by_settlement"] == {"fed": 1, "starving": 1}
    assert w.content_hash() == h0


@pytest.fixture(scope="module")
def realm():
    return POP.build_realm(0)


def test_i_on_the_built_realm_every_populated_settlement_starves_before_the_first_yield(realm):
    hist = POP.census(realm)["hunger_by_settlement"]
    settlements = [r for r in sorted(realm.rungs) if realm.rungs[r].kind == world_q.HUNGER_KIND]
    assert list(hist) == sorted(hist) and sum(hist.values()) == len(settlements) >= 30, hist
    checked = 0
    for rid in settlements:
        if sum(world_q.demanded(realm, rid).values()) > 0:
            assert world_q.hunger(realm, rid)[0] == "starving", rid
            checked += 1
    assert checked >= 30, "the loop asserted nothing: no settlement carried a cohort"
    assert hist.get("starving", 0) == checked
