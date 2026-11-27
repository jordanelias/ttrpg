"""`data/geography.py` -- THE GEOGRAPHY FILE, READ ONCE PER PROCESS, FOR THE BATTLE FIELD (and, since
v9 IN-35, its territory borders for the lattice coupling: `adjacent_territories`, below).

`files.GEOGRAPHY_YAML` (canon's world map) is a DATA INPUT of the `mass_battle` module: its terrain
lookup and river test (`modules/mass_battle/terrain.py`) read `provinces:`, `terrain:` and `water:`.
The module may not read it itself -- AX-4 leaves it no state between calls, so it re-parsed 37 KB on
every fought field, and a file it opens by path is an input outside `modules/**` that the module's
port input set cannot see. So the HOST reads it, here, and hands it on: `seam/wrappers/mass_battle.py::
field_input` puts it on the record (`queries/inputs.py::MassBattleInput.geography`).

ONE READ PER PROCESS, `data/cast.py`'s idiom: the file is repository content that cannot change under a
running season (`manifest/registry.py`'s `_CONTRACTS_CACHE` states the same licence). AX-4 binds the
module, not the host. ⚠ THE MAPPING IS SHARED by every record built in the process: nothing may write
into it (the module only reads it). A test that needs the file re-read sets `_CACHE` back to `None`.
"""
from __future__ import annotations

import heapq
import math
from typing import Optional

from .files import GEOGRAPHY_YAML
from .rosters import load_yaml, settlement_rung_id, territory_rung_id

_CACHE: Optional[dict] = None


def geography() -> dict:
    """The parsed geography file, read on first use and kept (`data/rosters.load_yaml`, the package's
    one YAML reader, so a duplicated key raises rather than silently keeping the last)."""
    global _CACHE
    if _CACHE is None:
        _CACHE = load_yaml(GEOGRAPHY_YAML.read_text(encoding="utf-8")) or {}
    return _CACHE


def load() -> dict:
    """`data.load_all`'s handle on this loader: read the file now. The same cache `geography()` fills."""
    return geography()


def settlement_neighbours(geo: Optional[dict] = None) -> dict:
    """B12b.02 (CP-T10-01): `{settlement geography id: tuple of the ids it borders, sorted}`, read off the file's `settlement_adjacency:`
    edges (`from`/`to`) and made UNDIRECTED, as `adjacent_territories` does for the territories. The edge `type:` is not read: what an
    edge costs is the ground of the settlement it enters (`route_over`). Read each call, so a test that swaps `geography()`'s
    cache sees its own graph; 55 edges. `geo` is the loaded geography (B12b.04: `leg_price` is handed it); `None` reads `geography()`."""
    out: dict = {}
    for e in (geography() if geo is None else geo).get("settlement_adjacency") or ():
        out.setdefault(e["from"], set()).add(e["to"])
        out.setdefault(e["to"], set()).add(e["from"])
    return {s: tuple(sorted(n)) for s, n in sorted(out.items())}


def shortest_path(a: str, b: str, price, geo: Optional[dict] = None) -> Optional[tuple]:
    """B12b.02: THE CHEAPEST PATH from settlement `a` to settlement `b` over `settlement_neighbours()`, as `(path, cost)` -- `path` the
    ids from `a` to `b` inclusive, `cost` the sum of `price(s)` over every settlement ENTERED (`a` itself is not entered). `price(s)` is
    a number, or `None` for a settlement that may not be entered; `None` is returned where `b` cannot be reached without one. A path
    from `a` to itself is `((a,), 0.0)`. DETERMINISTIC: among equal costs the path that sorts first by its ids wins (Dijkstra over
    `(cost, path)` pairs), so no tie breaks on dict order or on a hash. Pure: it reads the graph and `price`, nothing else.
    An id the graph does not hold is no node, and `None` comes back for it."""
    graph = settlement_neighbours(geo)
    if a not in graph or b not in graph:
        return None
    heap, done = [(0.0, (a,))], set()
    while heap:
        cost, path = heapq.heappop(heap)
        here = path[-1]
        if here in done:
            continue
        if here == b:
            return path, cost
        done.add(here)
        for n in graph[here]:
            if n in done:
                continue
            p = price(n)
            if p is not None:
                heapq.heappush(heap, (cost + p, path + (n,)))
    return None


#: The composition role of the one owner of terrain at a point (`modules/mass_battle/terrain.py::terrain_type_at`, B12b.02); `world_q.QUERY_ENTRIES` registers it.
TERRAIN_TYPE_AT = "mass_battle.terrain_type_at"


def settlement_by_rung(geo: dict) -> dict:
    """B12b.04: `{settlement Rung id: settlement geography id}` over `geo`'s `settlements:`, the inverse `rosters.settlement_rung_id` documents
    (read off the file, never off the spelling). The one table `world_q.route` (through `ancestry`) and `leg_price` (a rung it is handed) both resolve a rung by."""
    return {settlement_rung_id(s): s for s in geo.get("settlements") or ()}


def route_over(a: str, b: str, geo: Optional[dict] = None) -> Optional[tuple]:
    """B12b.02/.04 (CP-T10-01): THE ONE OWNER OF A JOURNEY'S PATH AND PRICE between two SETTLEMENT GEOGRAPHY IDS, `(path of ids, cost)` or `None`
    where it is blocked. Each step over a `settlement_adjacency` edge costs `terrain_cost_matrix[t]`, `t` the terrain at the coords of the settlement
    ENTERED (`mass_battle.terrain_type_at`, reached by its `query` role; `plains` where no polygon holds the point), summed by `shortest_path`. A
    settlement whose ground costs the matrix's `mountain` entry may not be entered. A function of the two ids and `geo`, nothing else: `world_q.route`
    (which finds each id by `ancestry`) and `leg_price` (which is handed none and finds it in `geo`) both call it. `geo` `None` reads `geography()`."""
    from engine.substrate import composition        # lazy, as `fixtures.py` does: the loader of the file does not need the module until a journey is priced
    geo = geography() if geo is None else geo
    matrix, locate = geo["terrain_cost_matrix"], composition.require(TERRAIN_TYPE_AT)
    impassable = matrix["mountain"]

    def price(sid: str) -> Optional[float]:
        cost = matrix[locate(geo["settlements"][sid]["coords"], geography=geo) or "plains"]
        return None if cost >= impassable else cost

    return shortest_path(a, b, price, geo)


def leg_points_of(cost: float, leg_unit: float) -> int:
    """B12b.02/.04: THE SCENE POINTS a route of `cost` costs, `max(1, ceil(cost / leg_unit))`: the floor is one point. The one formula `world_q.leg_points`
    and `leg_price` share."""
    return max(1, math.ceil(cost / leg_unit))


def leg_price(a: str, b: str, geo: dict, *, leg_unit: float) -> int:
    """B12b.04 (CP-T10-01; `09_WR_B_weather` edit 3): THE SCENE POINTS A JOURNEY FROM RUNG `a` TO RUNG `b` COSTS, a pure function of the two rung ids,
    the loaded geography `geo` and `leg_unit` (the fixture, handed as a keyword): `leg_points_of` over `route_over`'s cost, so it equals
    `world_q.leg_points` wherever both are asked of settlement rungs. No `World` crosses: this is what `decision/` prices a journey with.

    A rung that is no settlement rung of `geo` (a hearth, a territory, `None`), a journey inside one settlement and a journey `route_over` finds
    blocked all read the FLOOR, 1: `decision/` cannot walk `ancestry` to the settlement a hearth sits in (AX-2), and whether the road is open
    stays the fold's read -- a priced journey refused there is `travel.blocked`, how a person learns the road is shut. ⚠ So a person standing
    in a hearth prices every journey at the floor; `world_q.leg_points` resolves his hearth and does not."""
    nodes = settlement_by_rung(geo)
    na, nb = nodes.get(a), nodes.get(b)
    if na is None or nb is None or na == nb:
        return 1
    found = route_over(na, nb, geo)
    return 1 if found is None else leg_points_of(found[1], leg_unit)


_ADJACENT: Optional[dict] = None


def adjacent_territories() -> dict:
    """v9 IN-35: `{territory rung id: frozenset of the territory rung ids it borders}`, read off the
    file's `adjacency:` edges (`from`/`to`, geography codes) and made UNDIRECTED -- the file writes each
    border once. Rung ids, through `rosters.territory_rung_id`, the one owner of that spelling, so a
    caller holding a `Site`'s territory rung asks with what it holds. A territory with no edge is absent
    (the caller reads `.get(t, frozenset())`). The edge `type:` (road, gate, ...) is not read: the
    lattice coupling (`loop/matter.py`) couples across a border, whatever crosses it.

    One read per process, `geography()`'s licence; nothing may write into the mapping it returns.
    ⚠ THE FILE'S `radiation_bands:` IS NOT READ HERE, AND THAT IS THE POINT: a band there is *"node
    distance"* from Askeheim, i.e. a breadth-first reading of these same edges, so reading both would be
    two owners of one distance. The tests use it as the independent control (`test_in35_*.py`)."""
    global _ADJACENT
    if _ADJACENT is None:
        out: dict = {}
        for e in geography().get("adjacency") or ():
            a, b = territory_rung_id(e["from"]), territory_rung_id(e["to"])
            out.setdefault(a, set()).add(b)
            out.setdefault(b, set()).add(a)
        _ADJACENT = {t: frozenset(n) for t, n in sorted(out.items())}
    return _ADJACENT
