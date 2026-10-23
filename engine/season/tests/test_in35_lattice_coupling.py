"""v9 IN-35 FORCE-HAZARD -- the Calamity re-expressed as a coupling rule (#457 `:123-143`, `:174`).

The rule is `loop/matter.py::_lattice_strain`: inside the existing wear loop, a Site loses
`lattice_coupling / condition_scale` of its gap down to the weakest Site of its own or a bordering
territory (`data/geography.py::adjacent_territories`), read from the barrier's opening conditions.
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
      so AT HEAD the live control is `test_the_thread_read_withheld_arm_reproduces_the_pre_k3_event_
      sequence`, which equals the pre-IN-35 one-season event sequence -- the identity is checked over
      one season, at event kind/id level only; the hash-level identity is historical (`@23b33e9e`).

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
from ..state.carriers import Act, Person, Rung, Site, Tenure
from ..state.world import World
from ..trace_log import TRACE

SOURCE = territory_rung_id("T15")            # Askeheim, the epicentre
RING_1 = (territory_rung_id("T6"), territory_rung_id("T13"))
SEASONS = 8
ON = 500                                     # a test arm (H-235's sweep), not a chosen value
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


def _world(weight: int, menders_at: tuple = ()) -> World:
    fixtures = DEFAULT_FIXTURES.sweep("lattice_coupling", weight)
    w = World(world_seed=1, fixtures=fixtures)
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
    w = _world(ON)
    got = _run(w)
    bands = _bands()
    assert all(b < a for a, b in zip(got["totals"], got["totals"][1:])), got["totals"]
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
    w = _world(1000)                         # the whole gap in one season: the fastest arm
    d = SeasonDriver(w)
    w.tick += 1
    d.matter(mint_token(w, WriteClass.MATTER), [])
    shut = {t for t in _bands() if world_q.closed_uses(w, t)}
    assert shut == {SOURCE, *RING_1}, sorted(shut)


# ======================================================================================
# (b) MANAGED: MENDING (`restore`, PERSONS' ACTS) STABILIZES
# ======================================================================================

def test_in35_managed_holding_the_first_ring_stops_the_front_there_and_the_unmanaged_arm_does_not():
    """Menders at both ring-1 harbours `restore` at every RESOLVE. Season 1's MATTER pulls ring 1 before
    anybody has mended (the driver's order), so ring 1 crosses in every season's MATTER (the source stays
    at 0, so the pull is the same each time), and nothing beyond it ever does:
    each restore puts ring 1 back at the full scale before the next MATTER opens, so ring 2 opens every
    season at exactly its kind's wear (no pull), while the same world unmended crosses ring after ring."""
    managed = _run(_world(ON, RING_1), RING_1)
    unmanaged = _run(_world(ON))
    scale, wear = DEFAULT_FIXTURES.get("condition_scale"), DEFAULT_FIXTURES.wear("harbour")
    assert managed["restored"] >= len(RING_1) * SEASONS, managed["restored"]   # EXECUTED, every season
    assert managed["first"] == {t: 1 for t in RING_1}, managed["first"]
    assert managed["crossings"] == {t: SEASONS for t in RING_1}, managed["crossings"]   # the limit cycle
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
    """THE OTHER HALF, INVERTED FROM WHAT THE RULE CANNOT DO: a mender at the source restores it at every
    RESOLVE, but season 1's MATTER has already pulled ring 1 below its floor, and a pulled ring pulls
    the next. So the front reaches every banded territory in the season the unmanaged arm does: mending
    the source does not stop it. Holding a ring does (the test above)."""
    managed = _run(_world(ON, (SOURCE,)), (SOURCE,))
    unmanaged = _run(_world(ON))
    assert managed["restored"] >= SEASONS, managed["restored"]   # the arm EXECUTED, every season
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
    # A SECOND harbour at the source, at full condition: its only weaker neighbour is the source's own
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


def test_in35_the_shipped_weight_is_the_control():
    assert DEFAULT_FIXTURES.get("lattice_coupling") == 0
