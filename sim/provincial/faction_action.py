"""
sim/provincial/faction_action.py — Faction action selection + resolution

Canon source: mc_v17.py faction_take_action; GD-2 (mandatory before stochastic)
Game Design constraints applicable: GD-1, GD-2
Status: [CANONICAL — Phase 2 implementation 2026-05-17]

v17 port: probabilistic action mix (M7_ASSUMPTION_SIX).
30% faction-unique | 35% Conquest | 20% Muster | 15% Govern.

Dependencies:
  - sim/autoload/game_state
  - sim/territory/adjacency
"""
from __future__ import annotations

import math
from sim.autoload.game_state import MULTS, ALL_PLAYABLE_15
from sim.territory.adjacency import ADJACENCY


def _successes(pool: float, rng) -> int:
    """Strategic-scale roll: d6 >= 4 per die (v17 convention, M3 compatible)."""
    if pool <= 0:
        return 0
    return sum(1 for _ in range(int(pool)) if rng.randint(1, 6) >= 4)


def _degree(net: int) -> str:
    if net >= 3:
        return 'Overwhelming'
    elif net >= 1:
        return 'Success'
    elif net == 0:
        return 'Partial'
    return 'Failure'


def faction_take_action(faction, world, rng) -> str:
    """Select and execute one action for a faction this season.

    GD-2: mandatory threat-response before stochastic selection.
    Currently simplified: probabilistic mix per v17.
    """
    roll = rng.random()

    # 30% faction-unique
    if roll < 0.30:
        pass  # Faction-unique actions deferred to Phase 5+

    # 35% Conquest (cumulative 65%)
    if roll < 0.65:
        result = _try_conquest(faction, world, rng)
        if result != 'invalid':
            return result

    # 20% Muster (cumulative 85%)
    if roll < 0.85:
        result = _try_muster(faction, world, rng)
        if result != 'invalid':
            return result

    # 15% Govern (fallback)
    return _try_govern(faction, world, rng)


def _try_conquest(faction, world, rng) -> str:
    """Attempt military conquest of adjacent territory."""
    adj = set()
    for tid in faction.territories:
        adj |= ADJACENCY.get(tid, set())
    targets = [tid for tid in adj
               if tid in world.territories
               and world.territories[tid].owner not in (faction.name, None)]

    if not targets or faction.Mil < 3.0:
        return 'invalid'

    target = rng.choice(targets)
    t = world.territories[target]

    # Legacy single-roll path (v17 L350-368)
    pool = faction.Mil
    ob = 2 if t.is_uncontrolled() else 4
    net = _successes(pool, rng) - ob
    deg = _degree(net)

    if deg in ('Overwhelming', 'Success'):
        old = t.owner
        if old and old in world.factions:
            world.factions[old].territories.discard(target)
            world.factions[old].adjust('L', -10)
        t.owner = faction.name
        faction.territories.add(target)
        t.garrison = True
        t.adjust_accord(-25)
        world.battle_count += 1

    return f'Conquest:{deg}'


def _try_muster(faction, world, rng) -> str:
    """Muster military strength in owned territory."""
    if not faction.territories:
        return 'invalid'
    pool = faction.Mil
    ob = 1
    net = _successes(pool, rng) - ob
    deg = _degree(net)

    if deg in ('Overwhelming', 'Success'):
        faction.adjust('Mil', 5 if deg == 'Overwhelming' else 3)
    elif deg == 'Failure':
        faction.adjust('W', -3)

    return f'Muster:{deg}'


def _try_govern(faction, world, rng) -> str:
    """Govern an owned territory to improve Accord."""
    if not faction.territories:
        return 'invalid'
    target = rng.choice(list(faction.territories))
    t = world.territories.get(target)
    if not t or t.owner != faction.name:
        return 'invalid'

    pool = faction.I
    ob = 2
    net = _successes(pool, rng) - ob
    deg = _degree(net)

    if deg in ('Overwhelming', 'Success'):
        t.adjust_accord(15 if deg == 'Overwhelming' else 10)
    elif deg == 'Failure':
        faction.adjust('Sta', -5)

    return f'Govern:{deg}'
