"""
sim/peninsular/accounting.py — End-of-season Accounting

Canon source: mc_v17.py L677-685; ci_political_v30
Status: [CANONICAL — Phase 2 implementation 2026-05-17]

Simplified from v17 (no M1/M5 settlement integration yet — Phase 7+).
CI generation: +2 per Church-held territory.
MS decay: -1 per 4 seasons (annual).
"""
from __future__ import annotations

from sim.autoload.game_state import ALL_PLAYABLE_15


def run_accounting(world):
    """End-of-season accounting pass."""
    _ci_generation(world)
    _ms_decay(world)
    # Seasonal resets already handled by season_manager.advance_season


def _ci_generation(world):
    """Church Infrastructure generation per mc_v17 L620-633 (simplified)."""
    delta = 0
    for tid in ALL_PLAYABLE_15:
        if tid not in world.territories:
            continue
        t = world.territories[tid]
        if t.owner == 'Church':
            delta += 2
    world.clocks['CI'] = min(100.0, world.clocks.get('CI', 30.0) + delta)


def _ms_decay(world):
    """MS baseline decay: -1 per year (every 4 seasons). Canon: params/core.md §MS Baseline Decay."""
    if world.season > 0 and world.season % 4 == 0:
        world.clocks['MS'] = max(0.0, world.clocks.get('MS', 80.0) - 1.0)
