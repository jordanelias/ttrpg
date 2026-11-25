"""v9 IN-35 FORCE-HAZARD -- the Calamity re-expressed as a coupling rule (#457 `:123-143`, `:174`).

The rule is `loop/matter.py::_lattice_strain`: inside the existing wear loop, a Site loses
`lattice_coupling / condition_scale` of its condition when a BROKEN Site (condition 0) stands in its own or
a bordering territory (`data/geography.py::adjacent_territories`), read from the barrier's opening
conditions (B12a.63: only a broken Site pulls; uneven wear alone couples nothing).
Mending is persons' `restore` acts, unchanged. The effect per territory is `world_q.closed_uses`.

THE ENTRY'S FALSIFIER, ONE TEST PER ARM, each able to see the failure it excludes:
  (a) UNMANAGED: lattice condition falls, and the band crossings reach territories IN ORDER OF
      DISTANCE. Distance is read off the geography file's `radiation_bands:` (*"band number = node
      distance"* from Askeheim) -- data the rule does NOT read, so the order is checked against an
      oracle independent of the edges the rule couples across.
  (b) MANAGED: persons standing at the fabric execute `restore` each season through the real RESOLVE
      fold, IN THE DRIVER'S ORDER (MATTER opens the season, RESOLVE follows). Holding the first ring
      stops the front at that ring: ring 1 crosses in EVERY season's MATTER (the source is never mended,
      so each MATTER pulls ring 1 from the full scale back under its floor and RESOLVE mends it: a
      limit cycle, not a fixed point), and nothing beyond it ever crosses. A mend at the source does NOT recall a ring MATTER has
      already pulled: the front reaches every territory in the season the unmanaged arm does. Each
      beside the unmanaged arm on the same world, which does cross.
  (c) WEIGHT 0 REPRODUCES TODAY: every Site ends where its kind's wear alone puts it, and the same
      world at a non-zero weight DIFFERS (the control that can fail). The realm-level half: at
      `23b33e9e` (IN-35) the 1- and 2-season content-hash pins in `test_season_weather.py` read the
      same as before it; K-3 later moved those pins (`Person.thread_sensitivity` is in every `repr`),
      so AT HEAD the live control is `test_the_thread_read_withheld_arm_is_pinned_and_differs_from_the_shipped_season`, a change detector
      since IN-59 (a) moved that arm (it no longer equals the pre-IN-35 sequence); the hash-level identity
      is historical (`@23b33e9e`).

THE WORLD is hand-built: a realm, every territory the geography names (by its rung id, so the real
borders apply), one harbour per territory at full condition, inserted nearest-the-source first, and
Askeheim's (`terr_T15`) planted at 0. ⚠ THE PLANT IS THE SOURCE THE TREE DOES NOT YET HAVE (`H-236`):
no act strains the lattice AT ASKEHEIM and the built realm holds no Site there. Harbour wear (10 a
season) alone needs 21 seasons to cross the first floor (800), so every crossing inside these runs is
the coupling's.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.geography import adjacent_territories, geography
from ..data.matrix import WriteClass
from ..data.rosters import territory_rung_id
from ..loop.driver import SeasonDriver, mint_token
from ..loop.matter import _lattice_strain
from ..queries import world_q
from ..state.attribution import event_by_id
from ..state.carriers import Act, Claim, Person, Rung, Site, Tenure
from ..state.world import World
from ..trace_log import TRACE

pytestmark = pytest.mark.flat_fold

@pytest.fixture(autouse=True)
def _recording():
    """`TRACE` keeps rows only inside a window an instrument opens; these tests read them."""
    with TRACE.recording():
        yield


SOURCE = territory_rung_id("T15")            # Askeheim, the epicentre
RING_1 = (territory_rung_id("T6"), territory_rung_id("T13"))
SEASONS = 8
ON = 500                                     # a test arm (H-235's sweep), not a chosen value
# B12a.63: only a BROKEN Site (condition 0) pulls, so a front moves out a ring only once the ring before it
# has been worn to 0. A share of the whole condition (the weight at its ceiling, `condition_scale`) breaks a
# pulled ring in one MATTER, so the front advances one ring a season: the arm the front tests run at.
BREAKS = 1000
# B12a.65: `restore` is declined at a broken Site while the coupling runs, so a ring can be held only BEFORE it breaks: a managed ring is pulled
# part-way (this weight, a quarter of the scale: under the first floor, above the second) and mended before the next MATTER opens.
HOLDS = 250
FLOOR = "bulk_shipping"                      # the harbour's first floor, `band_floors.harbour`


def _bands() -> dict:
    """`{territory rung id: radiation band}` -- the INDEPENDENT distance oracle (see the header)."""
    return {territory_rung_id(t): b["band"] for b in geography()["radiation_bands"]
            for t in b["territories"]}


def _sid(t: str) -> str:
    """A territory's harbour, NAMED SO ITS ID SORTS BY DISTANCE FROM THE SOURCE (`site_b0_...` first).
    `_lattice_strain` keys its map on `sorted(w.sites)`; the wear loop that WRITES walks
    `w.sites.values()` in insertion order, and `_world` inserts in the same band order (`_band_order`),
    so a rule that read a neighbour's write of the same barrier would carry the front outward in ONE
    season on this world whichever of the two walks it rode; the one-ring test sees it."""
    return f"site_b{_bands().get(t, 9)}_{t}"


def _band_order(territories) -> list:
    """The territories nearest the source first (band, then id): the order `_world` inserts Sites."""
    bands = _bands()
    return sorted(territories, key=lambda t: (bands.get(t, 9), t))


def _world(weight: int, menders_at: tuple = (), seed: int = 1) -> World:
    # B07.99: the coupling is asked of the managed holder's `restore` EXECUTING every season; under `task_draw_arm` on a drawn restore fails
    # about two seasons in three (a failed draw mends nothing), so the world runs the flat fold, as the arm-off control does.
    fixtures = DEFAULT_FIXTURES.sweep("lattice_coupling", weight)
    w = World(world_seed=seed, fixtures=fixtures)
    scale = fixtures.get("condition_scale")
    w.rungs["R"] = Rung("R", "realm")
    n = [0]

    def edge(sub, obj, kind):
        n[0] += 1
        w.add_tenure(Tenure(f"t{n[0]}", sub, obj, kind, since=0))

    for t in _band_order(set(adjacent_territories()) | set(_bands())):
        w.rungs[t] = Rung(t, "territory")
        edge(t, "R", "contain")
        w.sites[_sid(t)] = Site(_sid(t), t, "harbour", condition=0 if t == SOURCE else scale)
    for t in menders_at:
        pid = f"p_mender_{t}"
        w.persons[pid] = Person(pid, "a mender")
        w.rungs[pid] = Rung(pid, "person")
        edge(pid, t, "contain")
        edge(pid, t, world_q.RESIDE_KIND)
    w.manifest = {"contest": "seam.contest_resolver", "order": "core.canonical_order"}
    return w


def _run(w: World, menders_at: tuple = ()) -> dict:
    """`SEASONS` seasons IN THE DRIVER'S ORDER (`loop/driver.py::SeasonDriver.season`: MATTER, then the
    rounds' DELIBERATE/RESOLVE): at each, the real MATTER barrier, then the menders' `restore` through
    the real RESOLVE fold. So the first MATTER pulls before anybody has mended, as in computed play.
    Returns `{territory: the season its harbour first crossed FLOOR}`, `{territory: how many seasons it
    crossed}`, the seasons' summed lattice
    condition, the restores that executed, and `{site: its condition at each MATTER open}`; the
    crossings are read off the Events MATTER emitted (each anchored, through its cause, on the wear
    write that crossed)."""
    d = SeasonDriver(w)
    first, totals, restored = {}, [sum(s.condition for s in w.sites.values())], 0
    crossings: dict = {}
    at_open: dict = {sid: [] for sid in w.sites}
    for season in range(1, SEASONS + 1):
        w.tick += 1
        for sid, s in w.sites.items():
            at_open[sid].append(s.condition)
        for ev in d.matter(mint_token(w, WriteClass.MATTER), []):
            if ev.kind != "condition.band_crossed":
                continue
            worn = event_by_id(w, ev.causes[0])
            site = w.sites[worn.changes[0].subject]
            if site.condition < w.fixtures.get("band_floors")["harbour"][FLOOR]:
                first.setdefault(site.rung, season)
                crossings[site.rung] = crossings.get(site.rung, 0) + 1
        acts = [Act(id=f"mend_{season}_{t}", actor=f"p_mender_{t}", verb="restore",
                    payload={"site": _sid(t)}) for t in menders_at]
        if acts:
            out = d.resolve(mint_token(w, WriteClass.ACTS), acts,
                            contest_max_depth=w.fixtures.get("contest_max_depth"))
            w.log.extend(out)
            restored += sum(e.kind == "site.restored" for e in out)
        totals.append(sum(s.condition for s in w.sites.values()))
    return {"first": first, "totals": totals, "restored": restored, "at_open": at_open,
            "crossings": crossings}


# ======================================================================================
# (a) UNMANAGED: CONDITION FALLS, AND THE CROSSINGS REACH TERRITORIES IN ORDER OF DISTANCE
# ======================================================================================

def test_in35_unmanaged_the_lattice_falls_and_crossings_reach_territories_in_order_of_distance():
    w = _world(BREAKS)
    got = _run(w)
    bands = _bands()
    # falling while there is a fabric left to break, and whole-fabric-broken by the end (nothing below 0)
    assert all(b <= a for a, b in zip(got["totals"], got["totals"][1:])), got["totals"]
    assert got["totals"][0] > got["totals"][1] > got["totals"][-1], got["totals"]
    # Every territory the oracle places at a distance is reached within the run -- asserted, so the
    # ordering check below cannot pass vacuously on a front that never left the source.
    reached = {t: s for t, s in got["first"].items() if bands.get(t, 0) >= 1}
    assert set(reached) == {t for t, b in bands.items() if b >= 1}, sorted(set(bands) - set(reached))
    by_band: dict = {}
    for t, s in reached.items():
        by_band.setdefault(bands[t], []).append(s)
    order = sorted(by_band)
    assert order == [1, 2, 3, 4, 5], order
    for near, far in zip(order, order[1:]):
        assert max(by_band[near]) < min(by_band[far]), by_band
    # The effect per territory, as the Query reads it at the end: every territory has a closed use, the
    # source's own included (below its floor before the run, so it never CROSSED, but shut all the same).
    shut = {t for t in bands if world_q.closed_uses(w, t)}
    assert shut == set(bands), sorted(set(bands) - shut)


def test_in35_the_front_advances_one_ring_a_season_at_most():
    """The parallel-map read (`_lattice_strain` reads the barrier's OPENING conditions): after ONE season
    only the first ring has crossed. A rule that read its neighbours' writes of the same barrier would
    let the front run outward through `w.sites`' order in a single pass."""
    w = _world(BREAKS)                       # the whole condition in one season: the fastest arm
    d = SeasonDriver(w)
    w.tick += 1
    d.matter(mint_token(w, WriteClass.MATTER), [])
    shut = {t for t in _bands() if world_q.closed_uses(w, t)}
    assert shut == {SOURCE, *RING_1}, sorted(shut)


# ======================================================================================
# (b) MANAGED: MENDING (`restore`, PERSONS' ACTS) STABILIZES
# ======================================================================================

def test_in35_managed_holding_the_first_ring_stops_the_front_there_and_the_unmanaged_arm_does_not():
    """Menders at both ring-1 harbours `restore` at every RESOLVE, at `HOLDS` (a ring pulled part-way, never to 0: `restore` is declined at a
    broken Site, B12a.65, so a ring is held before it breaks). Season 1's MATTER pulls ring 1 before
    anybody has mended (the driver's order), so ring 1 crosses in every season's MATTER (the source stays
    at 0, so the pull is the same each time), and nothing beyond it ever does:
    each restore puts ring 1 back at the full scale before the next MATTER opens, so ring 2 opens every
    season at exactly its kind's wear (no pull: ring 1 is whole at the open, so nothing there is broken),
    while the same world unmended (at `BREAKS`) crosses ring after ring."""
    managed = _run(_world(HOLDS, RING_1), RING_1)
    unmanaged = _run(_world(BREAKS))
    scale, wear = DEFAULT_FIXTURES.get("condition_scale"), DEFAULT_FIXTURES.wear("harbour")
    assert managed["restored"] >= len(RING_1) * SEASONS, managed["restored"]   # EXECUTED, every season
    assert managed["first"] == {t: 1 for t in RING_1}, managed["first"]
    # the limit cycle: pulled from the full scale to a quarter short of it, ring 1 crosses the floors above that each MATTER
    pulled = scale - wear - HOLDS
    floors = len([f for f in DEFAULT_FIXTURES.get("band_floors")["harbour"].values() if pulled < f])
    assert floors >= 1
    assert managed["crossings"] == {t: SEASONS * floors for t in RING_1}, managed["crossings"]
    ring_2 = [t for t, b in _bands().items() if b == 2]
    checked = 0
    for t in ring_2:
        assert managed["at_open"][_sid(t)] == [scale - k * wear for k in range(SEASONS)], t
        checked += 1
    for t in RING_1:
        assert managed["at_open"][_sid(t)] == [scale] * SEASONS, t
        checked += 1
    assert checked == len(ring_2) + len(RING_1) and ring_2, checked
    beyond = {t for t in unmanaged["first"] if t not in RING_1 and t != SOURCE}
    assert len(beyond) >= 10, sorted(beyond)                     # the same world, unmended, does cross
    assert managed["totals"][-1] > unmanaged["totals"][-1] + 5000, (managed["totals"], unmanaged["totals"])


def test_in35_a_mended_source_does_not_recall_a_ring_matter_has_already_pulled():
    """THE OTHER HALF, INVERTED FROM WHAT THE RULE CANNOT DO: a mender at the source tries to restore it at every
    RESOLVE, but the source is broken (B12a.65: `restore` is declined there while the coupling runs, so nothing is mended) and season 1's MATTER
    has already pulled ring 1 to 0, and a ring at 0 is itself broken and pulls the next. So the front reaches every banded territory in
    the season the unmanaged arm does: the mender at the source changes nothing. Holding a ring does (the test above)."""
    managed = _run(_world(BREAKS, (SOURCE,)), (SOURCE,))
    unmanaged = _run(_world(BREAKS))
    assert managed["restored"] == 0, managed["restored"]   # every attempt DECLINED at the broken source
    banded = {t for t, b in _bands().items() if b >= 1}
    assert all(unmanaged["first"].get(t) for t in banded), unmanaged["first"]   # not vacuous
    assert {t: managed["first"].get(t) for t in banded} == {t: unmanaged["first"].get(t) for t in banded}, (
        managed["first"], unmanaged["first"])
    assert all(managed["first"].get(t) == 1 for t in RING_1), managed["first"]


# ======================================================================================
# (c) WEIGHT 0 REPRODUCES TODAY, AND THE CONTROL CAN FAIL
# ======================================================================================

@pytest.mark.parametrize("weight", [250, ON])           # H-235's two non-zero sweep points
def test_in35_weight_zero_is_wear_alone_and_a_nonzero_weight_differs(weight):
    zero, on = _world(0), _world(weight)
    start = {sid: s.condition for sid, s in zero.sites.items()}
    _run(zero), _run(on)
    wear = zero.fixtures.wear("harbour")
    assert {sid: s.condition for sid, s in zero.sites.items()} == {
        sid: max(0, c - SEASONS * wear) for sid, c in start.items()}
    assert not [e for e in zero.log if e.kind == "condition.band_crossed"]
    assert zero.content_hash() != on.content_hash()
    assert [e for e in on.log if e.kind == "condition.band_crossed"]


def test_in35_the_control_reads_no_site_and_the_weight_is_refused_outside_its_share():
    w = _world(0)
    scale = w.fixtures.get("condition_scale")
    # A SECOND harbour at the source, at full condition: its only broken neighbour is the source's own
    # harbour, IN ITS OWN TERRITORY, so it is pulled only if the rule reads a Site's own territory and
    # not just the bordering ones.
    extra = "site_b0_extra_at_source"
    w.sites[extra] = Site(extra, SOURCE, "harbour", condition=scale)
    traced = len(TRACE.rows)
    assert _lattice_strain(w, scale) == {}
    assert len(TRACE.rows) == traced, "the control traced a line"
    for bad in (-1, scale + 1, float("nan")):
        w.fixtures = DEFAULT_FIXTURES.sweep("lattice_coupling", bad)
        with pytest.raises(ValueError):
            _lattice_strain(w, scale)
    w.fixtures = DEFAULT_FIXTURES.sweep("lattice_coupling", ON)
    pulled = _lattice_strain(w, scale)
    assert set(pulled) == {extra, *(_sid(t) for t in RING_1)}, sorted(pulled)
    gap = scale                                  # each pulled Site is at the scale, its weakest at 0
    assert all(v == ON * gap // scale for v in pulled.values()), pulled


def _far_from_the_source() -> str:
    """A banded territory that is neither the source nor one it borders (the oracle's farthest band)."""
    near = {SOURCE, *adjacent_territories().get(SOURCE, ())}
    bands = _bands()
    far = max((t for t in bands if t not in near), key=lambda t: (bands[t], t))
    assert far not in near and bands[far] > 1
    return far


def test_a_realm_with_nothing_broken_couples_nothing():
    """B12a.63: strain flows from what is broken. Uneven wear (one Site worn to 400, every Site above 0)
    propagates nothing at weight 250: a realm with nothing broken couples nothing."""
    w = _world(250)
    scale = w.fixtures.get("condition_scale")
    for s in w.sites.values():
        s.condition = scale
    w.sites[_sid(_far_from_the_source())].condition = 400
    assert min(s.condition for s in w.sites.values()) > 0
    assert _lattice_strain(w, scale) == {}


def test_the_pull_is_toward_a_broken_neighbour_only():
    """B12a.63: one Site planted at 0 pulls only the Sites of its own and bordering territories, each by
    `weight * condition // scale`; a worn, unbroken Site far away pulls none (today's rule pulls its
    neighbours down to 400 as well, which this asserts out)."""
    w = _world(250)
    scale = w.fixtures.get("condition_scale")
    far = _far_from_the_source()
    w.sites[_sid(far)].condition = 400
    assert [s.id for s in w.sites.values() if s.condition <= 0] == [_sid(SOURCE)]
    near = {SOURCE, *adjacent_territories().get(SOURCE, ())}
    expect = {_sid(t) for t in near if t != SOURCE and _sid(t) in w.sites}
    pulled = _lattice_strain(w, scale)
    assert expect and set(pulled) == expect, (sorted(pulled), sorted(expect))
    assert all(v == 250 * scale // scale for v in pulled.values()), pulled


def test_in35_the_shipped_weight_is_the_control():
    assert DEFAULT_FIXTURES.get("lattice_coupling") == 0


def test_the_wound_switch_mints_one_site_on_t15_and_off_is_byte_identical():
    """B12a.07: `build_realm(wound=True)` mints the one Site T15's `wound:` row in the geography file names (its kind, at its
    `condition`) on `terr_T15`; off, the default, the realm is byte-identical to the build without the parameter."""
    from ..boot.realm import build_realm
    row = geography()["provinces"]["T15"]["wound"]
    off, plain, on = build_realm(0, cap=5, wound=False), build_realm(0, cap=5), build_realm(0, cap=5, wound=True)
    assert row["kind"] in on.fixtures.get("band_floors") and row["condition"] == 0
    assert off.content_hash() == plain.content_hash()
    assert not [s for s in off.sites.values() if s.rung == SOURCE]
    here = [s for s in on.sites.values() if s.rung == SOURCE]
    assert [(s.kind, s.condition) for s in here] == [(row["kind"], row["condition"])]
    assert set(on.sites) - set(off.sites) == {here[0].id} and set(off.sites) <= set(on.sites)
    assert on.content_hash() != off.content_hash()


# ======================================================================================
# B12a.64: A STRAINED SITE BREAKS, HOLDS OR KNITS BY A DRAW (`16_PESSIMIST_WR_B` edit 2)
# ======================================================================================
# Every test plants its strain at season 0 (UNDECIDED 5: the sources read fourteen seasons, A-114 reads two), so the draw is taken in the
# FIRST MATTER: a Site below the rupture floor beside a broken Site. The pool is the count of broken Sites near it (capped at
# `rupture_pool_cap`), and one die cannot break a Site (Success needs the net to clear an obstacle of 2 by one), so the arms that must SEE a
# break plant several broken Sites beside the ring, the way the wound's own territory would hold them once the front had gone through.
STRAINED = 50                                  # below every kind's lowest floor (harbour 100; an empty cell's `rupture_band`, 100)
WOUND_PLANT = 5                                # broken harbours planted at the source beside the wound, so the ring's pool reaches the cap


def _strained_world(weight: int, seed: int, broken: int = WOUND_PLANT) -> World:
    """`_world`, then at season 0: the wound's two bordering harbours below the floor, and `broken` more harbours at 0 in the source's territory."""
    w = _world(weight, seed=seed)
    for t in RING_1:
        w.sites[_sid(t)].condition = STRAINED
    for i in range(broken):
        sid = f"site_b0_planted_{i}"
        w.sites[sid] = Site(sid, SOURCE, "harbour", condition=0)
    return w


def _first_matter(w: World) -> list:
    """The first MATTER barrier's emissions, at the driver's own call."""
    d = SeasonDriver(w)
    w.tick += 1
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def test_a_rupture_is_emitted_and_its_season_differs():
    """Weight 250, the wound planted and the ring below its floor at season 0, seeds 0 to 9: a `site.ruptured` is emitted at some seed and
    the SET of ruptured Sites differs between at least two seeds (the front moves by a draw, not by the same hand every time)."""
    ruptured, checked = {}, 0
    for seed in range(10):
        w = _strained_world(250, seed)
        out = _first_matter(w)
        ruptured[seed] = frozenset(e.changes[0].subject for e in out if e.kind == "site.ruptured")
        checked += 1
        assert all(w.sites[sid].condition == 0 for sid in ruptured[seed]), (seed, ruptured[seed])
    assert checked >= 10, checked
    assert any(ruptured.values()), ruptured
    assert len(set(ruptured.values())) >= 2, ruptured


def _realm_yield(w: World) -> int:
    return sum(sum((r.__dict__.get("yield") or {}).values()) for r in w.rungs.values())


def _strained_realm(seed: int, weight: int) -> World:
    """`build_realm` with the wound planted (B12a.07) and, at season 0, every Site of the wound's bordering territories below its kind's lowest
    floor (an empty cell's, `rupture_band`), the first four of each territory broken."""
    from ..boot.realm import build_realm
    w = build_realm(seed, cap=5, wound=True, fixtures=DEFAULT_FIXTURES.sweep("lattice_coupling", weight))
    floors = w.fixtures.get("band_floors")
    for t in sorted(adjacent_territories()[SOURCE]):
        mine = sorted((s for s in w.sites.values() if world_q.enclosing_territory(w, s.rung) == t), key=lambda s: s.id)
        for k, s in enumerate(mine):
            low = min(floors[s.kind].values()) if floors[s.kind] else w.fixtures.get("rupture_band")
            s.condition = 0 if k < 4 else low // 2
    return w


def test_yield_differs_between_seeds_after_two_seasons():
    """The source's falsifier, at two seasons and planted (UNDECIDED 5): the realm's summed yield after season 1 differs between seeds 0 and 1
    at weight 250 (the front advances by drawn breaks)."""
    from ..harness.populated import run
    got = {}
    for seed in (0, 1):
        w = _strained_realm(seed, 250)
        run(2, seed, w=w)
        got[seed] = _realm_yield(w)
    assert got[0] != got[1], got


def test_weight_zero_is_the_base_hash():
    """At weight 0 the season is the base hash (the control): the same strained world with the three rupture rows swept to other values reads
    the same content hash and emits no `site.ruptured`, while at weight 250 it emits one."""
    base = _strained_world(0, 3)
    swept = _strained_world(0, 3)
    for name, value in (("rupture_band", 400), ("rupture_base", 0), ("rupture_pool_cap", 1)):
        swept.fixtures = swept.fixtures.sweep(name, value)
    out_base, out_swept = _first_matter(base), _first_matter(swept)
    assert not [e for e in out_base + out_swept if e.kind == "site.ruptured"]
    assert base.content_hash() == swept.content_hash()
    assert any(e.kind == "site.ruptured" for s in range(10) for e in _first_matter(_strained_world(250, s)))


def test_front_stops_where_the_source_is_mended():
    """The source's gate at two seasons: the wound planted at 0 at season 0 and raised to `condition_scale` before season 1; after season 1
    no Site is pulled and no `site.ruptured` is emitted (the ring was pulled once, to a standing condition, and nothing near it is broken)."""
    w = _world(250)
    scale = w.fixtures.get("condition_scale")
    d = SeasonDriver(w)
    log = []
    for season in range(2):
        if season == 1:
            w.sites[_sid(SOURCE)].condition = scale
        w.tick += 1
        log += d.matter(mint_token(w, WriteClass.MATTER), [])
    assert _lattice_strain(w, scale) == {}
    assert not [e for e in log if e.kind == "site.ruptured"]
    assert all(w.sites[_sid(t)].condition > 0 for t in RING_1)


def test_a_strained_site_takes_no_draw_above_its_floor_or_beside_nothing_broken():
    """The draw's two gates, each against the arm that would take it: a Site below its floor with NOTHING broken near it (uneven wear alone) and
    a Site beside a broken Site but STANDING above its floor take no draw, so neither breaks and neither knits (its wear is its kind's alone
    plus the pull, written once)."""
    for seed in range(10):
        w = _strained_world(250, seed)
        w.sites[_sid(RING_1[0])].condition = 600                       # beside the broken Sites, above the floor
        far = _sid(_far_from_the_source())
        w.sites[far].condition = STRAINED                              # below the floor, nothing broken near it
        wear = w.fixtures.wear("harbour")
        pull = _lattice_strain(w, w.fixtures.get("condition_scale"))
        out = _first_matter(w)
        assert not [e for e in out if e.kind == "site.ruptured" and e.changes[0].subject in (_sid(RING_1[0]), far)], seed
        assert w.sites[far].condition == STRAINED - wear, seed
        assert w.sites[_sid(RING_1[0])].condition == 600 - wear - pull[_sid(RING_1[0])], seed


def test_restore_is_refused_at_a_broken_site_while_the_coupling_runs():
    """A hand-built `restore` at a Site at 0 through the real RESOLVE fold: refused at weight 250 (`restore.refused`, the Site stays at 0, the
    decline's TRACE line is written) and admitted at weight 0 (`site.restored`, the Site rises). The same act at a standing Site at weight 250 is
    admitted, so the refusal is the broken Site's and not the weight's."""
    got = {}
    for weight in (250, 0):
        w = _world(weight, (SOURCE,))
        site = w.sites[_sid(SOURCE)]
        assert site.condition == 0
        seen = len(TRACE.rows)
        out = SeasonDriver(w).resolve(mint_token(w, WriteClass.ACTS),
                                      [Act(id="mend", actor=f"p_mender_{SOURCE}", verb="restore", payload={"site": site.id})],
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))
        got[weight] = ([e.kind for e in out], site.condition,
                       [r for r in TRACE.rows[seen:] if r.channel == "DECISION" and "broken Site" in r.what])
    assert "restore.refused" in got[250][0] and "site.restored" not in got[250][0] and got[250][1] == 0, got
    assert len(got[250][2]) == 1 and not got[0][2], got
    assert "site.restored" in got[0][0] and got[0][1] > 0, got
    w = _world(250, (RING_1[0],))                       # a standing Site at the same weight: admitted
    w.sites[_sid(RING_1[0])].condition = 400
    out = SeasonDriver(w).resolve(mint_token(w, WriteClass.ACTS),
                                  [Act(id="mend", actor=f"p_mender_{RING_1[0]}", verb="restore", payload={"site": _sid(RING_1[0])})],
                                  contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert "site.restored" in [e.kind for e in out] and w.sites[_sid(RING_1[0])].condition > 400


def test_a_site_the_strain_fails_to_break_knits_by_the_pull_it_took():
    """One broken Site is a pool of one, which the obstacle of 2 beats (Failure: the fabric held): the ring harbour recovers the pull it took
    this season and ends at its kind's wear alone, with a second `condition.worn` written. Over seeds 0 to 9 at least one knits."""
    knit, checked = 0, 0
    for seed in range(10):
        w = _strained_world(250, seed, broken=0)
        site = w.sites[_sid(RING_1[0])]
        wear, pull = w.fixtures.wear("harbour"), 250 * STRAINED // 1000
        out = _first_matter(w)
        worn = [e for e in out if e.kind == "condition.worn" and e.changes[0].subject == site.id]
        checked += 1
        assert site.condition in (STRAINED - wear, STRAINED - wear - pull), (seed, site.condition)
        if site.condition == STRAINED - wear:
            knit += 1
            assert len(worn) == 2, (seed, len(worn))
        assert not [e for e in out if e.kind == "site.ruptured" and e.changes[0].subject == site.id]
    assert checked >= 10 and knit >= 1, (checked, knit)


# ======================================================================================
# B12a.66: A CROSSING A PERSON STANDS BESIDE RAISES A QUESTION ABOUT THE PLACE (`16_PESSIMIST_WR_B` edit 4)
# ======================================================================================
def _crossing_claim(site: str, holder: str, kind: str = "condition.band_crossed") -> Claim:
    """The claim WITNESS deposits for a crossing: predicate the Event's kind, subject its anchor (the Site), landed at tick 0."""
    return Claim(f"c_{kind}_{site}", holder, site, kind, True, 0, "firsthand", 5, "own")


def _stands_beside(kind: str, far: bool) -> tuple:
    """One person living at a territory, holding a claim of `kind` on a Site (at his own rung, or `far`: a bordering territory's) AND, ahead of it in
    the question order, a claim about himself: the crossing's own question is NOT the one he answers first, so the Site reaches him only by the stamp."""
    w = _world(250, (RING_1[0],))
    p = w.persons[f"p_mender_{RING_1[0]}"]
    site = _sid(RING_1[1] if far else RING_1[0])
    p.ledger.append(Claim("c_0_self", p.id, p.id, "body", 5, 0, "firsthand", 5, "own"))
    p.ledger.append(_crossing_claim(site, p.id, kind))
    w.tick = 1                                   # the claims landed last season: new to his next deliberation
    return w, p, site


def test_a_witnessed_crossing_at_his_rung_stamps_the_site():
    """One person, one claim of a crossing (`condition.band_crossed`, then `site.ruptured`) on a Site at his rung, a claim about himself sorting
    ahead of it: the question he answers carries the Site as a `Site`-classed referent, so `restore` forms for him. The falsifier arm: the same claim
    on a Site at a rung he does not stand on stamps nothing."""
    for kind in ("condition.band_crossed", "site.ruptured"):
        w, p, site = _stands_beside(kind, far=False)
        assert world_q.place_of(w, site) == world_q.place_of(w, p.id)
        got = world_q.questions_for(w, p)
        assert got and got[0].about == "c_0_self" and got[0].referents_for("Site") == (site,), (kind, got)
        w, p, site = _stands_beside(kind, far=True)
        assert world_q.place_of(w, site) != world_q.place_of(w, p.id)
        got = world_q.questions_for(w, p)
        assert got and got[0].about == "c_0_self" and not got[0].referents_for("Site"), (kind, got)


def test_restore_or_mend_attempted_at_a_crossed_site():
    """Played, two seasons, the wound planted and the ring strained at season 0 (the B12a.64 plant, weight 250), seeds 0 and 1 POOLED: `restore`
    is ATTEMPTED at least once by a person standing at a crossed Site (an Event of `condition.band_crossed` or `site.ruptured` anchored on it). ATTEMPTED,
    not executed: B12a.65 declines `restore` at a broken Site while the coupling runs, and a decline is an attempt the fold refuses. The Mend does not
    exist yet (B35), so `restore` is the only verb read."""
    from ..harness.populated import run
    from ..state.attribution import anchor_of
    attempts, checked = [], 0
    for seed in (0, 1):
        w = _strained_realm(seed, 250)
        run(2, seed, w=w)
        crossed = {anchor_of(w, e) for e in w.log if e.kind in ("condition.band_crossed", "site.ruptured")}
        crossed = {s for s in crossed if s in w.sites}
        checked += len(crossed)
        attempts += [(seed, a.id) for a in w.acts
                     if a.verb == "restore" and isinstance(a.payload, dict) and a.payload.get("site") in crossed
                     and world_q.place_of(w, a.actor) == w.sites[a.payload["site"]].rung]
    assert checked >= 2, checked
    assert attempts, "no `restore` was attempted at a crossed Site by a person standing there"
