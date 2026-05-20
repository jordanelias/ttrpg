"""
sim/peninsular/accounting.py — End-of-season Accounting

Canon source: designs/scene/conviction_track_v30.md §3 PP-412 (CI generation);
              params/core.md §MS Baseline Decay PP-255 (MS year-end decay);
              designs/provincial/ci_political_v30.md (CI political role).
Status: [CANONICAL — Phase 2 2026-05-17; Deferred Migration Batch 2026-05-20]

Composes per-season world-track updates. Both CI and MS arithmetic live in
their dedicated modules (sim/peninsular/ci_track.py, sim/peninsular/ms_track.py).
This module is the orchestrator; it does not implement track formulas.

[2026-05-20 — Deferred Migration Batch: legacy _ci_generation (+2 per
 Church-held territory) and _ms_decay (inline MS clamp) deleted.
 _ci_generation was canon-violating per PP-412 §3 (which specifies a
 5-step seasonal calculation: passive Institutional Momentum +1,
 PT-bucketed Conviction Yield via SW weighting, caller-driven
 Assert/Suppress, Hafenmark Structural Suppression at Baralta Mandate ≥ 4).
 _ms_decay duplicated ms_track.apply_ms_baseline_decay without behavioral
 difference but with split source-of-truth. Both now route through their
 dedicated modules.]
"""
from __future__ import annotations

from sim.peninsular.ci_track import apply_seasonal_ci
from sim.peninsular.ms_track import apply_ms_baseline_decay, SEASONS_PER_YEAR


def run_accounting(world):
    """End-of-season accounting pass.

    Order:
      1. CI seasonal calculation (PP-412 5-step) — every season
      2. MS baseline decay (PP-255) — Year-End only (every SEASONS_PER_YEAR seasons)

    Both routed through dedicated track modules; no inline duplication.
    Seasonal resets (faction flags, arc boundaries) handled by
    sim.autoload.season_manager.advance_season upstream.
    """
    # PP-412 — runs every season; no caller-driven Assert/Suppress at accounting
    # (those are faction Domain Actions resolved by faction_action, not by the
    # accounting orchestrator)
    apply_seasonal_ci(world)

    # PP-255 — Year-End cadence. Caller (this orchestrator) gates on the
    # season-modulo; apply_ms_baseline_decay itself does not check cadence.
    if world.season > 0 and world.season % SEASONS_PER_YEAR == 0:
        apply_ms_baseline_decay(world)
