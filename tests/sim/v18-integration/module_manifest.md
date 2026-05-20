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
| T0-3 | `sim/cross_scale/handoff_rules.py` | `designs/architecture/scale_transitions_v30.md §3` | **verified** — 8 handoff rules §3.1-§3.8 + §3.9 fieldwork dispatcher; TS-banded coherence cost; HandoffResult procedure descriptor |
| T0-4 | `sim/__init__.py` | (declarations) | **verified** — module docstring updated to reflect Tier 0 progress |
| T0-5 | `sim/peninsular/ms_track.py` | `params/core.md §MS Baseline Decay PP-255` | **verified** — apply_ms_baseline_decay + apply_ms_delta; floor/ceiling clamps; drift noted vs accounting._ms_decay |
| T0-6 | `sim/peninsular/season.py` | `designs/architecture/campaign_architecture_v30.md` | **verified** — composes advance_season + caller-actions + run_accounting; drift noted vs mc_v18 inline |
| T0-7 | `sim/provincial/treaty.py` | `faction_balance_convergence_v12c §4.5 + §4.7` | **partial** — process_treaty_expirations against §4.5 (lapse_rate=0.90); register_treaty/get_active_treaties helpers; propose_treaty CANON-GATED on Pass 2h (treaty_expiration_v30.md pending) |
| T0-8 | `sim/provincial/charter_liberties.py` | (canon ref incorrect — §6 is Public Temperament not Charter Liberties) | **CANON-GATED** — no implementable spec exists. Pass 2e Hafenmark canon authoring required. |
| T0-9 | `sim/provincial/varfell_mandate_action.py` | (current canon flagged broken by Jordan 2026-05-17) | **CANON-GATED** — Pass 2d Varfell contamination audit pending; both name and mechanism redesign needed |
| T0-10 | `sim/world/insurgency_pipeline.py` | `canon/02_canon_constraints.md §B GD-3` | **verified** — check_insurgency_triggers detects 2+ contiguous Uncontrolled, 2-season streak; check_insurgency_promotion gates on L/territories/Accord; RM-vs-parliamentary on PT threshold |
| T0-11 | `sim/world/npe.py` | `designs/scene/investigation_systems_v30.md` SYSTEM 1 | **verified** — Territory Social Ecology weights, NPC Genome 5-axis, Two-Tier Generation (archetype seed + d6 deviation), simulate_npc_actions for season-end stance drift |
| T0-12 | `sim/cross_scale/zoom_in_out.py` | `scale_transitions_v30.md §4` | **verified** — Zoom In legal entry points (PP-103) + board-degree scene Ob modifier; Zoom Out domain-echo queue + PC incap + Contested Figure wound; 8 mandatory triggers (§4.3.2) enumerated |
| T0-13 | `sim/cross_scale/domain_echo.py` | `scale_transitions_v30.md §5` | **verified** — §5.2 amount-by-degree, §5.5 Accord Echo with 4 scene-outcome rules, §5.6 Thread Echo with 6 event-type rules; PP-329 cap acknowledged |
| T0-14 | `sim/autoload/npc_ai.py` | (priority-stack contamination flagged by Jordan 2026-05-17) | **CANON-GATED** — audit pending before content authoring |


## Schema migration 2026-05-19 — World registries

Per stub_infill_plan amendment (f40bb51a): game_state.World gains 6 registry
fields collapsing the Tier 0 module-level stores. Backwards-compatible —
modules check `hasattr(world, '<registry>')` and fall back to module-level
when absent. Status: **landed**.

| Field | Owning module | Purpose |
|---|---|---|
| `practitioners` | sim/thread/coherence | actor_id → CoherenceState (10-0 track) |
| `insurgencies` | sim/world/insurgency_pipeline | insurgency_id → InsurgencyRecord (GD-3 state machine) |
| `uncontrolled_streaks` | sim/world/insurgency_pipeline | frozenset[tid] → consecutive Uncontrolled seasons |
| `npcs` | sim/world/npe | territory_id → list[NPC] |
| `npc_counter` | sim/world/npe | incrementing NPC id source |
| `treaties` | sim/provincial/treaty | frozenset[parties] → TreatyRecord |

Validated cross-world isolation (w1.practitioners ≠ w2.practitioners) + mc_v18
backward-compat (battles_mean=31.8 at seed=42 N=5; no regression vs prior baseline).
Serialize/restore does NOT yet snapshot new registries — lands separately when
production save format is needed.


## Tier 1 Stub Infill (2026-05-19) — first batch landed

Per stub_infill_plan: Tier 1 stubs have all dependencies on implemented
modules. First batch: territory/infrastructure + territory/temperaments
(both depend on settlement, landed at fbc08811).

| # | Module | Canon | Status |
|---|---|---|---|
| T1-1 | `sim/territory/infrastructure.py` | `settlement_layer_v30 §1.5-§1.7` | **verified** — 4-axis Church infrastructure (Religious Building / Templar / Inquisitor / Church Governor); build_infrastructure + count + seizure_ob_modifier with -4 cap; Templar seed from Territory.templar |
| T1-2 | `sim/territory/temperaments.py` | `territory_temperaments_v30` | **verified** — 5-typology authored for 17 territories (T1-T17); temperament_of + temperament_modifiers (α/β + drift); apply_strain_shock per §4 drift formula; faction aggregates per §3 |
| T1-3a | `sim/personal/conviction.py` | `designs/personal/conviction_track_v1.md §2-§3` (PP-718 per-Conviction Scar) | **verified** — Scar accumulation per-Conviction (not aggregate); 0/1/2/3+ thresholds; crisis at 3+; Certainty scaling; season cap for Thread witnessing; cycle pair with beliefs |
| T1-3b | `sim/personal/beliefs.py` | `designs/scene/fieldwork_v30.md §5.5; designs/scene/social_contest_v30.md §9.5` | **verified** — add_belief/revise_belief/social_success; +1 Momentum on aligned win (cap 4); challenging win marks revision pending; late-import resolves cycle |
| T1-4 | `sim/thread/operations.py` | `threadwork_v30.md Part 2 + params/threadwork.md` | **verified** — 7 entry points (Leap + Weaving + Pulling + POP + Locking + Dissolution + Mending); Three-Axis Ob; FR surcharge; integrates with coherence.apply_coherence_delta |
| T1-5 | `sim/personal/combat.py` | `combat_v30.md §1-§7` | **verified (partial)** — Strike + Full Guard + Take a Breath + Dodge + Establish Distance implemented; Feint/Rescue/Disarm/Tie Up explicitly deferred to Tier 2+. §1 Combat Pool, §5 Weapon TN matrix, §5 PP-232 damage formula with armor tiers, §4 resolution-order ordering |

UNBLOCKS Tier 2: peninsular/ci_track (needs infrastructure ✓);
provincial/mass_seizure (needs ci_track + infrastructure ✓);
provincial/infrastructure_reclamation (canon-gated but dep ✓);
provincial/varfell_territorial_acquisition (needs temperaments ✓ + restoration_movement canon-gated).


## Tier 2 Stub Infill (2026-05-19+)

| # | Module | Canon | Status |
|---|---|---|---|
| T2-1 | `sim/peninsular/ci_track.py` | `conviction_track_v30 §3 PP-412` | **verified** — PP-412 5-step seasonal CI calc (Momentum +1; Conviction Yield by PT; Assert; Suppress; Hafenmark suppression -1 at L≥4); apply_ci_delta for non-seasonal (Excommunication +4); drift noted vs accounting._ci_generation |
| T2-2 | `sim/provincial/mass_seizure.py` | `victory_v30 §3.2 + supersession 250715f` | **verified** (landed with bug fix at ec3727fc) — probabilistic declaration; one-shot lifetime; PP-534 self-control |
| T2-3 | `sim/personal/contest.py` | `social_contest_v30 §1-§9` | **verified** — Argue Pool (PA×2)+History; resolve_exchange; Persuasion Track 1-9; Belief alignment integration via late-import |
| T2-4 | `sim/personal/knots.py` | `knots_v30 (Pass 2g)` | **verified (Option A)** — 2-tier Distant/Close per ED-773 supersession; formation prerequisites + roll; strain accumulation + break; rupture triggers + -1 Coherence per PP-632 |
| T2-5 | `sim/thread/co_movement.py` | `threadwork_v30 Part 4 + §4.3 ED-577` | **verified** — 15-card canonical deck; Object/Personal → unactualized, Relational+ → actualized; deck reshuffle on exhaustion (16-draw verified) |
| T2-6 | `sim/thread/collective.py` | `threadwork_v30 §2.5` | **verified** — Anchor (highest TS) + Helpers; floor(Cognition/2) bonus dice; lattice fracture +1 Ob if pool drops below half expected; per-practitioner Coherence cost |
| T2-7 | `sim/thread/threadcut.py` | `threadwork_v30 Part 6` | **verified** — registry-based threadcut flag; §6.2 5-band perception table; §6.3 +1 Rendering Strain per external op; §6.4 De-Actualisation Round 1/2/3 trigger at strain ≥ Health |
| T2-8 | `sim/thread/opposing.py` | `threadwork_v30 §2.6` | **verified** — Opposing Ob modifier floor(opponent_TPS/2), min +1; 7-cell resolution matrix (Meets/Partial/Failure × 2); Knot strain via late-import; FR-vs-standard penalty distinction |


## Bug fix 2026-05-19 — canonical PT/Accord bucketing

T2-1 ci_track (f145e4b6) committed with a latent unit-conversion bug:
canon PT is categorical 0-5 but Territory.pt is continuous 0.5-7.0 via
PT_MAP. Original code used `int(t.pt)` which drifts (pt=7.0 → int=7 has
no CI_YIELD_BY_PT entry → 0 yield). Same bug in nascent mass_seizure
(uncommitted) and npe (committed at 94dac72e schema migration).

Fix lands canonical_pt(continuous_pt) and canonical_accord(continuous_accord)
helpers in game_state.py (round-trip verified for all PT_MAP / ACCORD_MAP
entries). ci_track and npe updated to use them. PP-534 Self-Control Rule
also fixed in ci_track._church_is_prominent (Church auto-prominent in
own territories, was failing 5.0 > 5.0 False).

Also lands T2-2 mass_seizure.py (verified post-fix) and the same bug
fixes in its post-fix version before commit.

| Action | Module | Status |
|---|---|---|
| Add canonical_pt + canonical_accord helpers | sim/autoload/game_state.py | **landed** |
| Fix ci_track Step 2 yield bucketing | sim/peninsular/ci_track.py | **fixed** |
| Fix ci_track PP-534 Self-Control Rule | sim/peninsular/ci_track.py | **fixed** |
| Fix npe ecology accord bucketing | sim/world/npe.py | **fixed** |
| Land T2-2 mass_seizure (post-fix) | sim/provincial/mass_seizure.py | **landed** |

Validation: ci_track default state now produces +1/season (matching
canon §3 Pacing "Early game S1-S5 ≈ +1/season"). Was +0 pre-PP-534 fix;
was wildly inflated +10 pre-bucketing fix. NPE T13 (low accord canon=1)
NPCs avg volatility 4.0 vs T2 (high canon=3) avg 3.0 — canon-correct
direction (low accord +1 volatility). mc_v18 backwards compat verified
(no regression; observed RNG variance is mc_v18's pre-existing non-
determinism, not from this fix).


## Schema migration #2 — 2026-05-19 — Tier 1/2 World registries

Extends migration #1 (94dac72e) with 8 additional fields for Tier 1/2
modules. Same Any-typing rationale + _store(world) router pattern.
Modules retain module-level fallback for world=None (legacy callers
and tests).

| Field | Owning module | Purpose |
|---|---|---|
| `convictions` | sim/personal/conviction | actor_id → ConvictionState (per-Conviction Scar counts) |
| `beliefs` | sim/personal/beliefs | actor_id → list[Belief] |
| `knots` | sim/personal/knots | knot_id → Knot (Distant/Close tiers) |
| `knot_id_counter` | sim/personal/knots | incrementing Knot id source |
| `territory_infrastructure` | sim/territory/infrastructure | territory_id → InfrastructureState (4-axis Church) |
| `npc_drift_state` | sim/territory/temperaments | territory_id → drift float (strain shock cumulative) |
| `threadcut_beings` | sim/thread/threadcut | being_id → ThreadcutState (rendering strain, de-actualisation round) |
| `comovement_deck` | sim/thread/co_movement | global deck state (remaining + discard) |

Validated cross-world isolation: 7-test smoke confirms each registry
isolates w1 ≠ w2; module-level fallback survives for world=None callers;
mc_v18 backwards-compat verified (battles_mean=37.4 with random.seed(0)
pin per ndet finding 2026-05-19c). serialize_world unchanged — new
registries still not in snapshot format, same limitation as migration #1.


## Per-record serializers — 2026-05-20 — Production save format

serialize_world / restore_world now snapshot all 14 World registries
from schema migrations #1 (94dac72e) and #2 (d2941cde). Each owning
dataclass exposes .to_dict() and .from_dict(); serialize_world calls
.to_dict() with hasattr-fallback (defensive against legacy module-level
state); restore_world reconstructs via late-imports on owning modules
(no module-load-time import cycles).

| Dataclass | Module | Round-trip verified |
|---|---|---|
| `CoherenceLogEntry` | sim/thread/coherence | ✓ (nested under CoherenceState.log) |
| `CoherenceState` | sim/thread/coherence | ✓ (Alice 4 deltas, log roundtrip exact) |
| `InsurgencyRecord` | sim/world/insurgency_pipeline | ✓ (L, territory_ids, formed_season) |
| `NPC` | sim/world/npe | ✓ (5-axis: stance, worldview, affiliation, compromise, volatility) |
| `TreatyRecord` | sim/provincial/treaty | ✓ (parties tuple, terms dict) |
| `ScarRecord` | sim/personal/conviction | ✓ (nested under ConvictionState.log) |
| `ConvictionState` | sim/personal/conviction | ✓ (scars, resonant_active, in_crisis, log) |
| `Belief` | sim/personal/beliefs | ✓ (statement, underlying_convictions, revision history with non-serializable evidence handling) |
| `Knot` | sim/personal/knots | ✓ (strain, tier, active, formed_season, log) |
| `InfrastructureState` | sim/territory/infrastructure | ✓ (4-axis: religious_building, templar_station, inquisitor_base, church_governor) |
| `ThreadcutState` | sim/thread/threadcut | ✓ (rendering_strain, deactualisation_round) |

Non-dataclass registries handled inline in serialize_world:
- `uncontrolled_streaks` (frozenset keys → list-of-dicts via sorted tids)
- `treaties` (frozenset keys → list-of-dicts with parties_key)
- `npc_drift_state` (dict[str, float] — straight roundtrip)
- `comovement_deck` (tuples in remaining/discard → lists for JSON, tuples on restore)
- `npc_counter`, `knot_id_counter` (int — straight roundtrip)

VALIDATION.

26/26 round-trip checks pass through `json.dumps()`/`json.loads()` cycle.
14/14 old-schema tolerance checks pass — snapshots produced by code
predating migrations #1 / #2 load cleanly with registries defaulting
to empty containers (via .get(key, default) pattern).

mc_v18 backwards-compat verified.
