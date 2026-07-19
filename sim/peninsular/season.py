"""
sim/peninsular/season.py — Season loop orchestrator

Canon source: designs/architecture/campaign_architecture_v30.md (campaign
flow); season_manager.SEASONS_PER_ARC; accounting.run_accounting.

Composes the canonical per-season step:
  1. season_manager.advance_season → season counter, arc boundary detection,
     seasonal/arc faction-flag reset
  2. (faction actions — caller-side; this orchestrator does not dispatch)
  3. accounting.run_accounting → CI seasonal calc (PP-412), MS year-end decay (PP-255)

Returns a SeasonResult summarising the step. Faction-action dispatch is
caller-side because the dispatch policy (random, AI, scripted) varies by
calling context (mc_v18 batch sim vs. interactive Godot session vs.
deterministic test).

[2026-05-20 — Deferred Migration Batch closes the mc_v18 inline DRIFT:
 mc_v18.run_campaign now invokes run_season(world, action_callback=...)
 instead of duplicating the advance_season → actions → run_accounting
 composition inline. This module is the single canonical season orchestrator.]

Dependencies:
  - sim/autoload/season_manager
  - sim/peninsular/accounting

Entry points:
  - run_season(world: GameState, action_callback=None) -> SeasonResult
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Callable

from engine.autoload.season_manager import advance_season, SEASONS_PER_ARC
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
      Step 3: accounting.run_accounting — CI seasonal calc (PP-412 5-step:
              Institutional Momentum + Conviction Yield + caller-driven
              Assert/Suppress + Hafenmark Structural Suppression) and
              MS baseline decay (PP-255, Year-End cadence — every
              SEASONS_PER_YEAR seasons).
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
