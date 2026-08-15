"""
sim/peninsular/accounting.py — End-of-season Accounting

Canon source: designs/scene/conviction_track_v30.md §3 PP-412 (CI generation);
              params/core.md §MS Baseline Decay PP-255 (MS year-end decay);
              systems/factions/ci_political_v30.md (CI political role);
              canon/02_canon_constraints.md §B GD-3 (insurgency pipeline);
              systems/fieldwork/investigation_systems_v30.md SYSTEM 1 (NPE).
Status: [CANONICAL — Phase 2 2026-05-17; Deferred Migration Batch 2026-05-20;
                    insurgency + NPE wire-up 2026-05-20]
[PRE-LPS-1 (schema gap, NOT a port block) — ED-FA-0004, 2026-07-07: run_accounting() has NO Mandate-aggregation
 or Treasury-accrual step; the LPS-1 per-settlement L/PS → Mandate pipeline is UNIMPLEMENTED
 (C-FA-1). The self-imposed port block is DELETED (Jordan, 2026-08-15 — ED-IN-0193); the gap
itself is unchanged and ED-FA-0004 is still open.]

Composes per-season world-track updates and end-of-season state propagation.
Track arithmetic lives in dedicated modules (ci_track, ms_track); insurgency
and NPC ecology run through their pipeline modules.

[2026-05-20 wire-up — closes two "module verified but not invoked" gaps from
 the post-Deferred-Migration roadmap (#2 + #3):
   - systems.world.sim.insurgency_pipeline.check_insurgency_triggers — GD-3 emergence
     fires at accounting time after Accord aggregates.
   - systems.world.sim.npe.simulate_npc_actions — territory-level NPC stance drift
     runs at season end before victory check.
 Both modules were verified individually at T0-10 / T0-11 but never invoked
 from the season loop.]

[2026-07-29 — W3 Handoff item 2, ED-IN-0091 plan §3 Wave 3: run_accounting gained a REPORT-ONLY
 province-Accord DRIFT PROBE (see `_probe_province_accord_drift` below). Two write paths for
 "provincial Accord" coexist uncoordinated in the live tree: `registry.province_accord` (§1.3
 floor(mean settlement Order), READ-ONLY aggregate) and `Territory.accord` (game_state.py's own
 continuous field, written DIRECTLY by parliamentary_transfer.py:210 and mass_seizure.py:295,
 bypassing settlement Order entirely). The W2 re-critic finding flagged this as a genuine
 divergence risk; reconciling the two write models into one is the SE lane's own L/PS workstream
 (OI-37, "single highest-priority open item" per HANDOFF_SE.md) — NOT this program's to resolve.
 The probe therefore only MEASURES and RECORDS the divergence as additive campaign telemetry
 (mirrors `engine.substrate.stubwire`'s `stub_hits` pattern); it never writes either value.]
"""
from __future__ import annotations

from engine.autoload.game_state import canonical_accord
from systems.overview.sim.ci_track import apply_seasonal_ci
from systems.overview.sim.ms_track import apply_ms_baseline_decay, SEASONS_PER_YEAR
from systems.settlements.sim import registry as settlement_registry
from systems.world.sim.insurgency_pipeline import (
    check_insurgency_triggers,
    check_insurgency_promotion,
    get_insurgencies,
)
from systems.world.sim.npe import simulate_npc_actions


def _probe_province_accord_drift(world) -> None:
    """W3 Handoff item 2 (ED-IN-0091 plan §3 Wave 3, 2026-07-29) — REPORT-ONLY.

    Compares, per province, `registry.province_accord` (the §1.3 floor(mean settlement Order)
    aggregate, canonical-index 0-4 [`math.floor` of an average over 0-5 members clamps the same
    range `canonical_accord` below produces]) against the live `Territory.accord` field
    (game_state.py's own continuous 0.5-7.0 representation), converted to ITS OWN canonical-index
    0-4 via `game_state.canonical_accord` for a like-for-like comparison — never mixing the two
    raw scales directly (the same "MULTS-scaled continuous value vs. canonical-index" defect class
    `echo_transport._apply_accord_echo`'s Unit note warns about).

    NEVER WRITES either value. `Territory.accord` is written directly by
    `parliamentary_transfer.py:210` and `mass_seizure.py:295` (province-scale actions, bypassing
    settlement Order entirely); `Settlement.order` is written by settlement-scale mechanics
    including this wave's own queued `scene.accord_echo` Key
    (`echo_transport._apply_accord_echo`). Two uncoordinated write models for "provincial Accord"
    is exactly the divergence risk the W2 re-critic finding flagged; reconciling them into one
    model is the SE lane's own L/PS workstream (OI-37, `HANDOFF_SE.md`'s "single highest-priority
    open item in this entire thread") — this probe only measures and records, per module docstring.

    Additive telemetry ONLY, mirroring `engine.substrate.stubwire`'s `stub_hits` pattern:
    `world.accord_drift_probe_hits` is a per-campaign counter (not a World dataclass field — set
    dynamically, same as `stubwire.invocations`'s campaign-delta convention, so this stage does
    not need to touch `engine/autoload/game_state.py`'s dataclass, a different lane's file this
    wave), left absent/zero when no province has both a settlement AND a Territory to compare, or
    when nothing diverges."""
    settlements = getattr(world, "settlements", None)
    territories = getattr(world, "territories", None)
    if not settlements or not territories:
        return
    hits = getattr(world, "accord_drift_probe_hits", 0)
    for tid, territory in territories.items():
        if not settlement_registry.province_members(tid, world):
            continue  # no settlements in this province — nothing to diverge from
        live_settlement_accord = settlement_registry.province_accord(tid, world)
        live_territory_accord = canonical_accord(territory.accord)
        if live_settlement_accord != live_territory_accord:
            hits += 1
    if hits:
        world.accord_drift_probe_hits = hits


def run_accounting(world):
    """End-of-season accounting pass.

    Order:
      1. CI seasonal calculation (PP-412 5-step) — every season
      2. MS baseline decay (PP-255) — Year-End only (every SEASONS_PER_YEAR seasons)
      3. Insurgency triggers (GD-3 a-b: emergence) — every season
      4. Insurgency promotions (GD-3 c-e: insurgency→faction) — every season
      5. NPC ecology (territory-level stance drift) — every season
      6. Province-Accord drift PROBE (report-only, W3 Handoff item 2) — every season

    Track arithmetic routes through dedicated modules; no inline duplication.
    Seasonal resets (faction flags, arc boundaries) handled by
    engine.autoload.season_manager.advance_season upstream.
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
    # [canonical: systems/fieldwork/investigation_systems_v30.md SYSTEM 1 §Persistence]
    simulate_npc_actions(world)

    # W3 Handoff item 2 (ED-IN-0091 plan §3 Wave 3) — report-only; see the function's own
    # docstring above. Runs last: purely observational, never gates or reorders the steps above.
    _probe_province_accord_drift(world)
