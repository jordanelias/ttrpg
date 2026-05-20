# Sim Module Manifest — v18 Integration / Phase 7 (Mass Battle)

Status: Step 4.2 LETHALITY landed 2026-05-18 (PP-233 formula correction + LETHALITY_SCALE=1.25 calibrated)
Scope: C2 narrow — canon §4.1 Step 1 (bare port v22 → sim/) + §4.10 Step 3 (faction_action wiring). Steps 2–9 deferred.
Source canon: `designs/provincial/mass_battle_integration_v30.md` §4.1, §4.10
Source engine: `tests/sim/sim_mb_06_v22.py` (2143 lines; per canon §4.1 — NOT m3_mass_battle.py)

## Modules — Phase 7 C2

| # | Module | Depends On | Canonical Sources | Status |
|---|---|---|---|---|
| P7-1 | `sim/provincial/units.py` | massbattle (late-bind for constants/utils) | `designs/provincial/mass_battle_v30.md §A.3–A.4`; `designs/scene/derived_stats_v30.md` (TroopCount / block_size); v22 dataclass surface | **verified** — `@dataclass(eq=False)` on Subunit + Unit (canon §4.1 PROVISIONAL flex; identity __eq__ resolves target_atom cycle) |
| P7-2 | `sim/provincial/tactic_cards.py` | — | `designs/provincial/mass_battle_v30.md §A.7`; `integration_plan_v18 §1.4` (BLOCKED on contamination audit) | stub-only — empty dict + marker per Jordan 2026-05-17 |
| P7-3 | `sim/provincial/massbattle.py` | `units`, `tactic_cards`; `params/mass_combat.md`; `params/core.md` | `designs/provincial/mass_battle_v30.md` (full); `designs/provincial/military_layer_v30.md`; `designs/provincial/mass_battle_integration_v30.md`; v22 source | **verified + Step 4.2 landed** — PP-233 continuous formula at engagement / pursuit / freed-attacker damage sites; LETHALITY_SCALE=1.25 calibrated; mc_v18 smoke battles_mean=40.1 |
| P7-4 | `sim/provincial/faction_action.py` | `massbattle.resolve_mass_battle`; `sim/territory/adjacency`; `sim/autoload/game_state` | `mass_battle_integration_v30.md §4.10 step 3` (faction_action invokes resolve_mass_battle for Military Conquest, HR-8 / §B GD-1) | **verified** — `mc_v18.run_batch(10, seed=42)` yields `battles_mean=30.0` (was 0 pre-fix); spread across factions (Crown 40 / Varfell 50 / Church 10) |
| P7-5 | `sim/mc_v18.py` | `faction_action` | `canon/02_canon_constraints.md §B (GD-1/2/3)` | no-op for C2 (battle_count already incremented in faction_action) |

## Deferred — Steps 2–9 (not in C2 scope)

| Step | Canon ref | Status |
|---|---|---|
| 4.2 — LETHALITY_SCALE restoration | §3.1 | deferred to Phase 7 follow-on |
| 4.3 — flanking detection | §3.2 P1 | deferred |
| 4.4 — penetration morale shock | §3.2 P2 | deferred |
| 4.5 — cell displacement ripple | §3.3 | deferred |
| 4.6 — equal-speed tiebreakers | §3.4 | deferred |
| 4.7 — phase-boundary hooks | §3.5 | deferred |
| 4.8 — internal collision wiring | §3.6 | deferred |
| 4.9 — cleanup (§3.7/§3.8/§3.9) | §3.7–3.9 | deferred |

## Step 10 sub-steps deferred (only sub-step 3 in C2)

| Sub-step | Module | Status |
|---|---|---|
| 10.1 | `sim/cross_scale/domain_echo.py` consumes battle result | deferred to Phase 7+ |
| 10.2 | `sim/peninsular/accounting.py` integrates §E.1/§E.2 | deferred to Phase 7+ |
| 10.3 | `sim/provincial/faction_action.py` invokes resolve_mass_battle | **in C2 (this manifest)** |

## Verification ledger (M-of-N coverage)

Bare port from validated v22 (already verified through battery_v22; v22 itself is the canonical engine per `mass_battle_integration_v30.md §4.1`). Per-constant ledger entries pending; deferred under same logic as Steps 2–9.

[GAP: sim_verification_ledger.json — not produced. Bare port replicates v22 constants verbatim with inline `# [canonical: …]` comments preserved from v22. Full ledger production deferred to Phase 7 Step 4.2+ when LETHALITY recalibration introduces new constants needing fresh attestation.]

## Phase 7 follow-on plan (separate handoffs)

After C2 verified end-to-end, the deferred work splits into independent handoffs to keep blast radius small:

| Handoff | Scope | Files | Prereq |
|---|---|---|---|
| Phase 7 — Step 4.2 LETHALITY recalibration | restore lethality scaling factors per §3.1 | `sim/provincial/massbattle.py`; `params/mass_combat.md` | **landed** — PP-233 formula correction (continuous net_successes) + LETHALITY_SCALE=1.25 calibrated to 14.48% mean / 16.45% median per-turn at T3 mirror N=60 |
| Phase 7 — Steps 4.3–4.6 (flanking + ripple + tiebreakers) | §3.2–§3.4 | `sim/provincial/massbattle.py` | 4.2 landed |
| Phase 7 — Steps 4.7–4.9 (phase hooks + collision + cleanup) | §3.5–§3.9 | `sim/provincial/massbattle.py` | 4.6 landed |
| Phase 7 — Step 10.1 domain_echo | cross-scale battle-result echo | `sim/cross_scale/domain_echo.py` (new) | C2 verified ✓ |
| Phase 7 — Step 10.2 accounting + faction→unit richening | unit-roster mapping richer than `_faction_to_unit` MV-defaults; §E.1/§E.2 in `peninsular/accounting` | `sim/peninsular/accounting.py`; `sim/provincial/faction_action.py` | C2 verified ✓; resolves GAP-1 |

## Phase 8 successor (recorded per handoff)

Phase 8 Strategic AI is the natural follow-on. Phase 7 alone retains stochastic dispatch (30 % faction-unique slot in `faction_take_action`); Phase 8 replaces that with goal-driven action selection. Not in C2 scope.

## Tier 0 Stub Infill — separate workstream (2026-05-19+)

Per `designs/proposals/stub_infill_plan.md` (commit 6669592f). Tier 0 = 14 stubs whose deps are already implemented modules. Each lands as a separate commit per Mode G "one module per session".

| # | Module | Canon | Status |
|---|---|---|---|
| T0-1 | `sim/territory/settlement.py` | `designs/territory/settlement_layer_v30.md §1.2-1.3` | **verified** — derives SettlementState + ProvinceState per §1.3 multipliers (50/20/30/20); 1:1 territory→settlement mapping pending registry |
| T0-2 | `sim/thread/coherence.py` | `designs/threadwork/threadwork_v30.md Part 3` | **verified** — Coherence 10-0 track with §3.3 bands (Stable/Dissonant/Fragmented/Fractured/Severed/Rendering Crisis); apply_coherence_delta + check_coherence_zero_transition; module-level practitioner registry pending World schema |
| T0-3 | `sim/cross_scale/handoff_rules.py` | `designs/architecture/scale_transitions_v30.md §3` | pending |
| T0-4 | `sim/__init__.py` | (declarations) | pending |
| T0-5 | `sim/peninsular/ms_track.py` | `params/core.md §MS Baseline Decay PP-255` | pending |
| T0-6 | `sim/peninsular/season.py` | `designs/architecture/campaign_architecture_v30.md` | pending |
| T0-7 | `sim/provincial/treaty.py` | balance audit memo | pending |
| T0-8 | `sim/provincial/charter_liberties.py` | `faction_canon_v30.md §6` | pending |
| T0-9 | `sim/provincial/varfell_mandate_action.py` | balance audit §part10 | pending |
| T0-10 | `sim/world/insurgency_pipeline.py` | `canon/02_canon_constraints.md §B GD-3` | pending |
| T0-11 | `sim/world/npe.py` | `designs/scene/investigation_systems_v30.md` (NPE) | pending |
| T0-12 | `sim/cross_scale/zoom_in_out.py` | `scale_transitions_v30.md §4` | pending |
| T0-13 | `sim/cross_scale/domain_echo.py` | `scale_transitions_v30.md §5` | pending |
| T0-14 | `sim/autoload/npc_ai.py` | `complete_systems_reference.md Part 1` | pending |
