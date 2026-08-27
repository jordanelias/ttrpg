"""
sim/peninsular/season.py — Season loop orchestrator

Canon source: designs/architecture/campaign_architecture_v30.md (campaign
flow); season_manager.SEASONS_PER_ARC; accounting.run_accounting.

⚠ THIS MODULE NO LONGER OWNS THE COMPOSITION (2026-08-27, ED-IN-0199). It is an ADAPTER
over engine/autoload/engine_clock.py:run_tick, which owns SEASON_TICK -> ACTION ->
ACCOUNTING_BOUNDARY per propagation_spec_v1 §O.1 — "engine_clock owns this composition and
is the only module that may advance the season counter". What survives here is `SeasonResult`,
a systems-lane return shape with its own callers, and the `action_callback` contract below.
Everything above this line used to describe a three-step composition this function performed
itself; it does not perform it any more, and the ordering is not this module's to change.

Faction-action dispatch stays caller-side, and that reason is unchanged: the dispatch policy
(random, AI, scripted) varies by calling context — mc_v18 batch sim vs. interactive Godot
session vs. a test injecting deterministic actions.

[2026-05-20 — Deferred Migration Batch closed the mc_v18 inline DRIFT: mc_v18.run_campaign
 invokes run_season(world, action_callback=...) instead of duplicating the composition inline.
 That fixed a real duplication, but it sited the single owner in `systems/` — which is the
 half ED-IN-0199 corrected. The claim "this module is the single canonical season
 orchestrator" that stood here is RETRACTED, not softened.]

Dependencies:
  - engine/autoload/engine_clock  (the composition)
  - engine/autoload/season_manager (SEASONS_PER_ARC only)

Entry points:
  - run_season(world: GameState, action_callback=None) -> SeasonResult
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Callable

from engine.autoload import engine_clock
from engine.autoload.season_manager import SEASONS_PER_ARC


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
    The composition below is engine_clock's, restated for a reader of this file — it is NOT
    performed here and editing this docstring changes nothing:
      SEASON_TICK: season_manager.advance_season — advances season counter,
              detects arc boundary, fires per-arc and per-season faction
              flag resets (Faction.reset_arc / reset_seasonal).
      ACTION: action_callback(world) — faction actions, scene resolution,
              whatever the caller wants to inject this season.
      ACCOUNTING_BOUNDARY: the scheduler's OF-7 deferred applies drain first,
              then accounting.run_accounting: CI seasonal calc (PP-412 5-step:
              Institutional Momentum + Conviction Yield + caller-driven
              Assert/Suppress + Hafenmark Structural Suppression) and
              MS baseline decay (PP-255, Year-End cadence — every
              SEASONS_PER_YEAR seasons).
    """
    # ED-IN-0199: the ordering is engine_clock's, not this module's. `run_season` used to
    # inline `advance_season -> action_callback -> run_accounting`, which made a systems-lane
    # file the owner of the tick composition that propagation_spec_v1 §O.1 assigns to
    # engine_clock — and left the scheduler's two phase calls with nowhere correct to live, so
    # they sat at the tail of mc_v18's action callback instead. This function is now the
    # adapter that keeps `SeasonResult` (a systems-lane shape with its own callers) available;
    # it defines no ordering.
    sr = engine_clock.run_tick(world, action_callback=action_callback)
    return SeasonResult(
        season=sr.season,
        arc=sr.arc,
        new_arc=sr.new_arc,
        accounting_run=True,
    )
