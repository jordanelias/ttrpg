"""
sim/mc_v18.py — Top-level strategic simulator runner — orchestrator only

Canon source: canon/02_canon_constraints.md §B (GD-1, GD-2, GD-3);
              designs/architecture/campaign_architecture_v30.md (campaign flow).
Game Design constraints applicable: GD-1, GD-2, GD-3
Status: [CANONICAL — Phase 2 implementation 2026-05-17;
                    Deferred Migration Batch 2026-05-20]

Replaces tests/sim/v17-integration/mc_v17.py (39k monolith).
Phase 2: faction actions (conquest/muster/govern) + accounting wired in.

[2026-05-20 — Deferred Migration Batch: inline season block deleted.
 Composition (advance_season → faction actions → accounting) now routes
 through sim.peninsular.season.run_season with action_callback.
 Pure refactor — ordering identical to v17/Phase-2 inline path.]

Dependencies:
  - sim/autoload/* (all autoload services)
  - sim/peninsular/season (season composition)
  - sim/provincial/faction_action

Entry points:
  - run_campaign(seed, max_seasons, params) -> CampaignResult
  - run_batch(n, base_seed, params) -> BatchResult
"""
from __future__ import annotations

import time
from collections import Counter
from dataclasses import dataclass, field

from sim.autoload import game_state, victory, scene_slate
from sim.provincial.faction_action import faction_take_action
from sim.peninsular.season import run_season
from sim.cross_scale import scene_dispatch


DEFAULT_PARAMS = {
    'CAMPAIGN_SEASONS': 50,
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
    battles_mean: float = 0.0


def _faction_actions_callback(world):
    """Per-season faction action dispatch — passed to season.run_season.

    GD-2 mandatory-actions precedence is enforced inside faction_take_action
    (mandatory pass before stochastic candidates per HR-9). Parliamentary +
    territory-holding gate matches the pre-migration inline block at
    mc_v18 L75-87 prior to 2026-05-20.
    """
    for fn, faction in world.factions.items():
        if not faction.parliamentary:
            continue
        if not faction.territories:
            continue
        try:
            faction_take_action(faction, world, world.rng)
        except Exception:
            pass  # action error — skip
    # Scale seam (§4 zoom protocol): dispatch personal-scale scenes triggered by
    # this season's world-state. Caller-side per season.py design. Side-effect-free
    # on strategic stats until the context-derivation bridge lands — see
    # sim/cross_scale/scene_dispatch.py GAP notes.
    scene_dispatch.run_scene_phase(world, world.rng)


def run_campaign(seed: int | None = None, max_seasons: int = 50,
                 params: dict | None = None) -> CampaignResult:
    """Run a single campaign to completion."""
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

        # season.run_season composes: advance_season → action_callback → run_accounting
        # [canonical: designs/architecture/campaign_architecture_v30.md;
        #  Deferred Migration Batch 2026-05-20 — replaces inline composition]
        run_season(world, action_callback=_faction_actions_callback)

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
    wins = Counter()
    total_battles = 0
    for i in range(n):
        r = run_campaign(seed=base_seed + i, params=params)
        if r.winner:
            wins[r.winner] += 1
        total_battles += r.battle_count

    total = sum(wins.values()) or 1
    factions = ['Crown', 'Church', 'Hafenmark', 'Varfell']
    return BatchResult(
        n=n,
        win_share={fn: round(wins.get(fn, 0) / total * 100, 1) for fn in factions},
        all_winners=dict(wins),
        battles_mean=round(total_battles / n, 1),
    )


if __name__ == '__main__':
    print("=== mc_v18 Phase 2 smoke test — 100 campaigns ===")
    r = run_batch(100, base_seed=42)
    print(f"  win_share: {r.win_share}")
    print(f"  all_winners: {r.all_winners}")
    print(f"  battles_mean: {r.battles_mean}")
