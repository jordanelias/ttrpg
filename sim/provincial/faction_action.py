"""
sim/provincial/faction_action.py — Faction action selection + resolution

Canon source: mc_v17.py faction_take_action; GD-2 (mandatory before stochastic)
Game Design constraints applicable: GD-1, GD-2
Status: [CANONICAL — Phase 2 implementation 2026-05-17; Phase 5/9 faction-unique
         dispatch wired 2026-05-17]

v17 port: probabilistic action mix (M7_ASSUMPTION_SIX).
30% faction-unique | 35% Conquest | 20% Muster | 15% Govern.

Dependencies:
  - sim/autoload/game_state
  - sim/territory/adjacency
  - sim/provincial/crown_initiative (Phase 5/9)
  - sim/provincial/excommunication (Phase 5/9)
  - sim/provincial/absolution (Phase 5/9)
  - sim/provincial/council_solmund (Phase 5/9)
"""
from __future__ import annotations

import math
from sim.autoload.game_state import MULTS, ALL_PLAYABLE_15
from sim.territory.adjacency import ADJACENCY
from sim.provincial import crown_initiative
from sim.provincial import excommunication
from sim.provincial import absolution
from sim.provincial import council_solmund


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
    Phase 5/9: 30% slot routes to faction-unique actions per faction.name.
    """
    roll = rng.random()

    # 30% faction-unique (Phase 5/9 dispatch)
    if roll < 0.30:
        unique_result = _try_faction_unique(faction, world, rng)
        if unique_result != 'invalid':
            return unique_result
        # fall through to Conquest if faction-unique unavailable

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


def _try_faction_unique(faction, world, rng) -> str:
    """Phase 5/9 dispatch — faction-unique action routing by faction.name.

    Crown: Crown Initiative (3 modes via select_initiative_mode heuristic).
    Church: Excommunication / Absolution / Council, picked by situational priority:
        1. Council if not used this arc (rare, high value)
        2. Excommunication if a viable target exists (highest-L rival not already excomm)
        3. Absolution otherwise (recovery + Stability support — Church always has L cost)
    Varfell/Hafenmark: deferred (Pass 2d/2e + contamination audit BLOCKED).
    """
    if faction.name == 'Crown':
        mode = crown_initiative.select_initiative_mode(faction, world, rng)
        if mode is None:
            return 'invalid'
        if mode == 'royal_progress':
            r = crown_initiative.attempt_royal_progress(faction, world, rng)
        elif mode == 'great_work':
            r = crown_initiative.attempt_great_work(faction, world, rng)
        elif mode == 'coronation_renewal':
            r = crown_initiative.attempt_coronation_renewal(faction, world, rng)
        else:
            return 'invalid'
        if r.status != 'resolved':
            return 'invalid'
        return f'CrownInitiative_{mode}:{r.degree.value}'

    if faction.name == 'Church':
        # Priority 1: Excommunication (primary offensive, high strategic impact)
        if faction.L >= excommunication.EXCOMM_PREREQ_L_LIGHT:
            target = excommunication.select_excommunication_target(faction, world, rng)
            if target is not None:
                r = excommunication.attempt_excommunication(faction, target, world, rng)
                if r.status == 'resolved':
                    return f'Excommunication:{r.degree.value}'
        # Priority 2: Council (1/arc, rare but high-value Mandate boost)
        if not getattr(faction, 'council_used_this_arc', False):
            r = council_solmund.attempt_council(faction, world, rng)
            if r.status == 'resolved':
                return f'Council:{r.degree.value}'
        # Priority 3: Absolution — only when Church.L >= 4 (cost is L-1; protect Excomm prereq)
        if faction.L >= 4.0:
            target = absolution.select_absolution_target(faction, world, rng)
            if target is not None:
                r = absolution.attempt_absolution(faction, target, world, rng)
                if r.status == 'resolved':
                    return f'Absolution:{r.degree.value}'
        return 'invalid'

    # Varfell + Hafenmark — BLOCKED on Pass 2d/2e + contamination audit
    return 'invalid'


def _try_conquest(faction, world, rng) -> str:
    """Attempt military conquest of adjacent territory.

    Phase 7 (§4.10 sub-step 3): single-roll path replaced with
    `resolve_mass_battle` engine invocation per
    designs/provincial/mass_battle_integration_v30.md §4.10.
    GD-1 binding: produces faction stat / territorial-control deltas only —
    no victory triggers from the battle outcome itself.

    Citations:
      - designs/provincial/mass_battle_integration_v30.md §4.10 step 3
      - canon/02_canon_constraints.md §B GD-1
    """
    adj = set()
    for tid in faction.territories:
        adj |= ADJACENCY.get(tid, set())
    # [hash-seed fix 2026-05-20] sort before rng.choice — adj is built from
    # ADJACENCY set-literals whose iteration order depends on PYTHONHASHSEED.
    # Sorting collapses that into a deterministic candidate list; rng.choice
    # then makes a world.rng-deterministic selection from it.
    targets = sorted(tid for tid in adj
                     if tid in world.territories
                     and world.territories[tid].owner not in (faction.name, None))

    if not targets or faction.Mil < 3.0:
        return 'invalid'

    target = rng.choice(targets)
    t = world.territories[target]

    # Phase 7 §4.10.3 — mass-battle engine invocation (replaces v17 single-roll path).
    # Defender is the territory owner faction, or None (uncontrolled garrison stub).
    from sim.provincial.massbattle import resolve_mass_battle
    defender_faction = world.factions.get(t.owner) if t.owner else None
    battle = resolve_mass_battle(
        faction_a=faction,
        faction_b=defender_faction,
        terrain=None,  # [GAP: terrain modifiers deferred to Phase 7 follow-on Steps 2-9]
        world=world,
    )
    deg = battle['degree']

    if battle['attacker_wins']:
        old = t.owner
        if old and old in world.factions:
            # [hash-seed fix 2026-05-20] .discard() → list guard-remove
            if target in world.factions[old].territories:
                world.factions[old].territories.remove(target)
            world.factions[old].adjust('L', -10)
        t.owner = faction.name
        # [hash-seed fix 2026-05-20] .add() → guarded append (preserves set-like idempotence)
        if target not in faction.territories:
            faction.territories.append(target)
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
