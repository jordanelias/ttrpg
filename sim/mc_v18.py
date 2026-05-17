"""
sim/mc_v18.py — Top-level strategic simulator runner — orchestrator only

Canon source: canon/02_canon_constraints.md §B (GD-1, GD-2, GD-3)
Game Design constraints applicable: GD-1, GD-2, GD-3
Status: [CANONICAL — Phase 1 implementation 2026-05-17]

Replaces tests/sim/v17-integration/mc_v17.py (39k monolith).
v18 is the modular line: this file orchestrates; subpackage modules do the work.

Dependencies:
  - sim/autoload/* (all autoload services)

Entry points:
  - run_campaign(seed, max_seasons, params) -> CampaignResult
  - run_batch(n, base_seed, params) -> BatchResult
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field

from sim.autoload import game_state, season_manager, victory, scene_slate


DEFAULT_PARAMS = {
    'CAMPAIGN_SEASONS': 100,
    'VICTORY_THRESHOLD': 11,
}


@dataclass
class CampaignResult:
    winner: str | None
    season: int
    surviving: int
    battle_count: int
    final_state: dict = field(default_factory=dict)


@dataclass
class BatchResult:
    n: int
    win_share: dict[str, float] = field(default_factory=dict)
    all_winners: dict[str, int] = field(default_factory=dict)


def run_campaign(seed: int | None = None, max_seasons: int = 100,
                 params: dict | None = None) -> CampaignResult:
    """Run a single campaign to completion.

    Phase 1: autoload modules only. Faction actions are stub — each faction
    does nothing per season. Victory check runs. Campaign ends by timeout
    with fallback winner by territory count.

    Subsequent phases wire in personal/provincial/territory/world modules.
    """
    if seed is None:
        seed = int(time.time()) & 0xFFFFFFFF

    world = game_state.create_world(seed=seed)
    victory.reset()
    scene_slate.clear()

    effective_params = dict(DEFAULT_PARAMS)
    if params:
        effective_params.update(params)
    max_s = effective_params.get('CAMPAIGN_SEASONS', max_seasons)

    for _ in range(max_s):
        if world.winner:
            break

        sr = season_manager.advance_season(world)

        # === FACTION ACTIONS (Phase 2+ wiring point) ===
        # GD-2: mandatory actions precede stochastic selection.
        # Currently stub: no faction actions implemented.
        # Phase 2+ will wire faction_action.py here.

        # === ACCOUNTING (Phase 2+ wiring point) ===
        # End-of-season accounting stub.
        # Phase 2+ will wire peninsular/accounting.py here.

        # === VICTORY CHECK (GD-1) ===
        results = victory.check_all_factions(world)
        for vr in results:
            if vr.won:
                world.winner = vr.faction_id
                break

    # Fallback winner by territory count (v17 L753-761)
    if not world.winner:
        scores = {}
        for fn, f in world.factions.items():
            if not f.parliamentary:
                continue
            held = sum(1 for tid in game_state.ALL_PLAYABLE_15
                       if tid in world.territories and world.territories[tid].owner == fn)
            scores[fn] = held * 10 + f.L + len(f.territories)
        if scores:
            world.winner = max(scores, key=scores.get)

    surviving = sum(1 for f in world.factions.values() if len(f.territories) > 0)

    return CampaignResult(
        winner=world.winner,
        season=world.season,
        surviving=surviving,
        battle_count=world.battle_count,
        final_state=game_state.serialize_world(world),
    )


def run_batch(n: int = 100, base_seed: int = 0,
              params: dict | None = None) -> BatchResult:
    """Run n campaigns and aggregate results."""
    from collections import Counter
    wins = Counter()
    for i in range(n):
        r = run_campaign(seed=base_seed + i, params=params)
        if r.winner:
            wins[r.winner] += 1

    total = sum(wins.values()) or 1
    factions = ['Crown', 'Church', 'Hafenmark', 'Varfell']
    return BatchResult(
        n=n,
        win_share={fn: round(wins.get(fn, 0) / total * 100, 1) for fn in factions},
        all_winners=dict(wins),
    )


if __name__ == '__main__':
    print("=== mc_v18 Phase 1 smoke test — 20 campaigns ===")
    r = run_batch(20, base_seed=42)
    print(f"  win_share: {r.win_share}")
    print(f"  all_winners: {r.all_winners}")
    print(f"  (Phase 1: no faction actions; winner = fallback by starting territory count)")
