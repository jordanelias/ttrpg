"""
sim/peninsular/season.py — Season loop orchestrator

Canon source: designs/architecture/campaign_architecture_v30.md (campaign
flow); season_manager.SEASONS_PER_ARC; accounting.run_accounting.

Composes the canonical per-season step:
  1. season_manager.advance_season → season counter, arc boundary detection,
     seasonal/arc faction-flag reset
  2. (faction actions — caller-side; this orchestrator does not dispatch)
  3. accounting.run_accounting → CI generation, MS decay

Returns a SeasonResult summarising the step. Faction-action dispatch is
caller-side because the dispatch policy (random, AI, scripted) varies by
calling context (mc_v18 batch sim vs. interactive Godot session vs.
deterministic test).

[DRIFT: sim/mc_v18.py L73-87 currently inlines the same composition rather
 than calling this module's run_season. This module is the canonical
 surface per Pass 2l decomposition; mc_v18 migration is out of Tier 0
 scope (touches implemented module). The two paths produce identical
 ordering: advance_season → (caller-provided actions) → run_accounting.]

Dependencies:
  - sim/autoload/season_manager
  - sim/peninsular/accounting

Entry points:
  - run_season(world: GameState, action_callback=None) -> SeasonResult
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Callable

from sim.autoload.season_manager import advance_season, SEASONS_PER_ARC
from sim.peninsular.accounting import run_accounting


@dataclass
class SeasonResult:
    """Per-season summary for caller (mc_v18, Godot scene controller, tests)."""
    season: int
    arc: int
    new_arc: bool
    accounting_run: bool


def run_season(world, action_callback: Optional[Callable] = None) -> SeasonResult:
    """Run one complete season step per the canonical ordering.

    action_callback: optional callable(world) invoked between advance_season
                     and run_accounting. Used by mc_v18 to dispatch
                     faction_take_action across all factions; by Godot to
                     drive UI scene flow; by tests to inject deterministic
                     actions or skip the step entirely.

    The composition is canonical:
      Step 1: season_manager.advance_season — advances season counter,
              detects arc boundary, fires per-arc and per-season faction
              flag resets (Faction.reset_arc / reset_seasonal).
      Step 2: action_callback(world) — faction actions, scene resolution,
              whatever the caller wants to inject this season.
      Step 3: accounting.run_accounting — CI generation (+2 per Church
              territory), MS baseline decay (per PP-255, when season % 4 == 0).
    """
    sr = advance_season(world)
    if action_callback is not None:
        action_callback(world)
    run_accounting(world)
    return SeasonResult(
        season=sr.season,
        arc=sr.arc,
        new_arc=sr.new_arc,
        accounting_run=True,
    )
