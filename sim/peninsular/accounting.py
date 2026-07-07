"""
sim/peninsular/accounting.py — End-of-season Accounting

Canon source: designs/scene/conviction_track_v30.md §3 PP-412 (CI generation);
              params/core.md §MS Baseline Decay PP-255 (MS year-end decay);
              designs/provincial/ci_political_v30.md (CI political role);
              canon/02_canon_constraints.md §B GD-3 (insurgency pipeline);
              designs/scene/investigation_systems_v30.md SYSTEM 1 (NPE).
Status: [CANONICAL — Phase 2 2026-05-17; Deferred Migration Batch 2026-05-20;
                    insurgency + NPE wire-up 2026-05-20]
[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004, 2026-07-07: run_accounting() has NO Mandate-aggregation
 or Treasury-accrual step; the LPS-1 per-settlement L/PS → Mandate pipeline is UNIMPLEMENTED
 (C-FA-1). Do NOT treat this season-end pass as canon-conformant until ED-FA-0004 (Stratum B).]

Composes per-season world-track updates and end-of-season state propagation.
Track arithmetic lives in dedicated modules (ci_track, ms_track); insurgency
and NPC ecology run through their pipeline modules.

[2026-05-20 wire-up — closes two "module verified but not invoked" gaps from
 the post-Deferred-Migration roadmap (#2 + #3):
   - sim.world.insurgency_pipeline.check_insurgency_triggers — GD-3 emergence
     fires at accounting time after Accord aggregates.
   - sim.world.npe.simulate_npc_actions — territory-level NPC stance drift
     runs at season end before victory check.
 Both modules were verified individually at T0-10 / T0-11 but never invoked
 from the season loop.]
"""
from __future__ import annotations

from sim.peninsular.ci_track import apply_seasonal_ci
from sim.peninsular.ms_track import apply_ms_baseline_decay, SEASONS_PER_YEAR
from sim.world.insurgency_pipeline import (
    check_insurgency_triggers,
    check_insurgency_promotion,
    get_insurgencies,
)
from sim.world.npe import simulate_npc_actions


def run_accounting(world):
    """End-of-season accounting pass.

    Order:
      1. CI seasonal calculation (PP-412 5-step) — every season
      2. MS baseline decay (PP-255) — Year-End only (every SEASONS_PER_YEAR seasons)
      3. Insurgency triggers (GD-3 a-b: emergence) — every season
      4. Insurgency promotions (GD-3 c-e: insurgency→faction) — every season
      5. NPC ecology (territory-level stance drift) — every season

    Track arithmetic routes through dedicated modules; no inline duplication.
    Seasonal resets (faction flags, arc boundaries) handled by
    sim.autoload.season_manager.advance_season upstream.
    """
    # PP-412 — every season; no caller-driven Assert/Suppress at accounting
    # (those are faction Domain Actions resolved by faction_action, not here)
    apply_seasonal_ci(world)

    # PP-255 — Year-End cadence. apply_ms_baseline_decay does not check cadence;
    # caller (this orchestrator) gates on season-modulo.
    if world.season > 0 and world.season % SEASONS_PER_YEAR == 0:
        apply_ms_baseline_decay(world)

    # GD-3 (a)-(b) — Insurgency emergence. Detects 2+ contiguous Uncontrolled
    # territories sustained 2+ seasons. Side-effect: world.insurgencies state
    # machine populated. Events list discarded here; callers needing it should
    # invoke check_insurgency_triggers directly.
    # [canonical: canon/02_canon_constraints.md §B GD-3 a-b]
    check_insurgency_triggers(world)

    # GD-3 (c)-(e) — Insurgency promotion. Checks each existing insurgency for
    # L≥3 / 2+ territories / Accord≥4 / 2-season streak; promotes to either
    # parliamentary candidate (PT≥3 avg) or RM extra-parliamentary (PT<3 avg).
    # Iterate over a snapshot since promotion may mutate the insurgencies dict.
    # [canonical: canon/02_canon_constraints.md §B GD-3 c-e]
    for ins_id in list(get_insurgencies(world).keys()):
        check_insurgency_promotion(ins_id, world)

    # NPE — territory-level NPC stance drift. Pairs with shared worldview and
    # adjacent stance positions roll Volatility to drift toward each other.
    # Side-effect: world.npcs state mutated. Actions list discarded here.
    # [canonical: designs/scene/investigation_systems_v30.md SYSTEM 1 §Persistence]
    simulate_npc_actions(world)
