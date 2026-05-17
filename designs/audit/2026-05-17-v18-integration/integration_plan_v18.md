# VALORIA — v18 Integration Plan

## Status: CANONICAL — Pass 2m synthesis 2026-05-17

## Scope: Executable build roadmap synthesizing the Pass 2 canonization work (armature + mechanics index + 5 new canon docs) into a sequenced implementation plan for `sim/` v18. Maps each sim module to its canon source, dependency chain, implementation phase, test status progression target, and blocking conditions. Identifies which modules are blocked on Pass 2k editorial-ledger decisions and which are blocked on the contamination audit. Defines v17 → v18 migration discipline.

## GD constraints: All three GDs bound through implementation. GD-1 enforced at `sim/autoload/victory.py` boundary. GD-2 enforced at `sim/provincial/faction_action.py` mandatory-actions pass. GD-3 enforced across `sim/world/insurgency_pipeline.py`, `sim/personal/parliamentary_vote.py`, `sim/provincial/parliamentary_transfer.py`.

## Source authority:

| Source | Commit | Role |
|---|---|---|
| `canon/02_canon_constraints.md` §B GD-1/2/3 | `fe367105` (Pass 2b) | Constraint enforcement |
| Strike-propagation across conviction_track / varfell_path_b / victory_v30 / complete_systems_reference / canonical_sources | `eaabf455` (Pass 2c) | HR-1 enforced; faction-specific victories struck |
| `sim/` armature (72 modules) | `80b4eb7e` (Pass 2l) | Build target |
| `canon/mechanics_index.yaml` + `tools/mechanics_index_gen.py` | `d493944f` (Pass 2j) | Registry + validator |
| `designs/provincial/mass_battle_integration_v30.md` | `2420a193` (Pass 2n) | Mass battle 10-step migration plan |
| `designs/personal/knots_v30.md` | `98417ac9` (Pass 2g) | Knot synthesis + 3 canon drifts |
| `designs/provincial/parliamentary_transfer_v30.md` | `3985cea0` (Pass 2h) | Universal mechanic |
| `designs/provincial/treaty_expiration_v30.md` | `3985cea0` (Pass 2h) | Universal mechanic |
| Royal Progress iter + ED-840 close | `3985cea0` (Pass 2h) | Crown action fix |
| `designs/world/insurgency_pipeline_v30.md` | `6d6373c9` (Pass 2i) | GD-3 implementation surface |

## Sim target: `sim/` (72-module armature scaffolded at Pass 2l)

---

## §1. What Pass 2 Has Produced (canon → sim mapping)

The Pass 2 canonization work produced **5 new canonical docs**, **3 amended canonical docs**, **the sim armature scaffold**, **the mechanics index**, and **the index generator**. The canon-to-sim mapping is now explicit for every module.

### §1.1 Foundations layer (canonized, ready to implement)

| Sim module | Canon authority | Pass | Implementation readiness |
|---|---|---|---|
| `sim/autoload/dice_engine.py` | `params/core.md` (Die Rule, TN Values, Degrees, Continuous Engine, Pool Min, Net Successes Floor, Momentum) | pre-existing canon | **READY** — all primitives canonized; M5 quasibinomial confirmed by params §Continuous Engine Decision E |
| `sim/autoload/game_state.py` | `designs/architecture/complete_systems_reference.md` | pre-existing canon | **READY** — infrastructure |
| `sim/autoload/season_manager.py` | `designs/architecture/campaign_architecture_v30.md` | pre-existing canon | **READY** — infrastructure |
| `sim/autoload/victory.py` | GD-1 (`canon/02_canon_constraints.md §B`) + `victory_v30 §0` | Pass 2b + 2c | **READY** — GD-1 enforced; sole victory path is peninsular_sovereignty |
| `sim/autoload/registry.py` | `canon/mechanics_index.yaml` | Pass 2j | **READY** — consumes index canonized this Pass |

### §1.2 Personal layer (mixed readiness)

| Sim module | Canon authority | Pass | Readiness |
|---|---|---|---|
| `sim/personal/combat.py` | `combat_v30.md` + `params/combat.md` | pre-existing | **READY** |
| `sim/personal/contest.py` | `social_contest_v30.md §§1-9` + `params/contest.md` | pre-existing | **READY** |
| `sim/personal/tribunal.py` | `social_contest_v30.md §7.1` (ED-625) | pre-existing | **READY** |
| `sim/personal/parliamentary_vote.py` | `social_contest_v30.md §10` | pre-existing | **READY** (GD-3 status-flag gate added Pass 2h) |
| `sim/personal/parliamentary_stay.py` | `social_contest_v30.md §10.1` (ED-631) | pre-existing | **READY** |
| `sim/personal/fieldwork.py` | `fieldwork_v30.md` + `params/fieldwork.md` | pre-existing | **READY** |
| `sim/personal/investigation.py` | `investigation_systems_v30.md` | pre-existing | **READY** |
| `sim/personal/conviction.py` | `conviction_track_v30.md` §§1-3 + §5 (post-HR-1 strike) | Pass 2c marker | **READY** |
| `sim/personal/beliefs.py` | cross-doc (fieldwork §5.5 + social_contest §9.5 + articulation §3.5) | pre-existing | **READY** (synthesis pending future Pass) |
| `sim/personal/knots.py` | `designs/personal/knots_v30.md` Pass 2g | Pass 2g | **BLOCKED** on TIER-DRIFT-001 (Pass 2k) |
| `sim/personal/companion.py` | `scene_tree_architecture.md` (CompanionScene) | pre-existing | **READY** |

### §1.3 Thread layer (all canonized)

| Sim module | Canon authority | Readiness |
|---|---|---|
| `sim/thread/operations.py` | `threadwork_v30 Part 2` (Leap / Weaving / Pulling / Past-Pulling / Locking / Dissolution / Mending) | **READY** |
| `sim/thread/collective.py` | `threadwork_v30 §2.5` | **READY** |
| `sim/thread/opposing.py` | `threadwork_v30 §2.6` | **BLOCKED** on TIER-DRIFT-001 (Knot Strain interactions) |
| `sim/thread/coherence.py` | `threadwork_v30 Part 3` + foundations P-10, P-15 | **READY** |
| `sim/thread/co_movement.py` | `threadwork_v30 Part 4` (15 cards) | **READY** |
| `sim/thread/rendering.py` | `threadwork_v30 Part 5` | **READY** |
| `sim/thread/threadcut.py` | `threadwork_v30 Part 6` | **READY** |

### §1.4 Provincial layer (mixed readiness)

| Sim module | Canon | Readiness |
|---|---|---|
| `sim/provincial/massbattle.py` | `mass_battle_integration_v30.md` Pass 2n (10-step plan) | **READY** (per Pass 2n migration §4 steps 1-10) |
| `sim/provincial/units.py` | `combat_v30 §11` + `mass_battle_v30` | **READY** |
| `sim/provincial/tactic_cards.py` | `mass_battle_v30` + `m6_faction_actions` | **BLOCKED** on contamination audit (card pool contents) |
| `sim/provincial/crown_initiative.py` | `part10_crown_initiative_design` post-ED-840 close (Pass 2h) | **READY** |
| `sim/provincial/excommunication.py` | `faction_canon §8.2` + `social_contest §7.1` | **READY** (calls personal/tribunal.py) |
| `sim/provincial/absolution.py` | `faction_canon §8` | **READY** |
| `sim/provincial/council_solmund.py` | `faction_canon` | **READY** |
| `sim/provincial/charter_liberties.py` | `faction_canon §6` (Hafenmark) | **READY** (mechanic-canon; flavor frame is faction-identity-territory) |
| `sim/provincial/varfell_mandate_action.py` | placeholder (renamed from vaynards_hall 2026-05-17 per VARFELL-MANDATE-ACTION-001) | **READY** (placeholder-name; mechanism authoring proceeds Pass 2d) |
| `sim/provincial/varfell_territorial_acquisition.py` | v12c §4.1 (validated_n1000) + canon doc Pass 2d pending | **READY** (placeholder-name; mechanism v12c-canonized; identity wrapping pending audit) |
| `sim/provincial/altonian_reinforcements.py` | v12c §4.3 (validated_n1000) + `altonian_reinforcements_v30.md` (Pass 2e pending) | **BLOCKED** on Pass 2e + contamination audit |
| `sim/provincial/infrastructure_reclamation.py` | `infrastructure_reclamation_v30.md` (Pass 2f pending) | **BLOCKED** on Pass 2f + contamination audit |
| `sim/provincial/home_sanctuary.py` | `home_sanctuary_t9_v30.md` (Pass 2f pending) | **BLOCKED** on Pass 2f + contamination audit |
| `sim/provincial/parliamentary_transfer.py` | `parliamentary_transfer_v30.md` Pass 2h | **READY** (PARL-* flags resolved at Pass 2k for full canonization) |
| `sim/provincial/mass_seizure.py` | `conviction_track §2 PP-411` + `ci_political §7.6` + `victory_v30 §3.2` | **READY** (3-source drift reconciliation pending Pass 2f) |
| `sim/provincial/treaty.py` | `treaty_expiration_v30.md` Pass 2h | **READY** |
| `sim/provincial/faction_action.py` | GD-2 + `faction_canon` + `params/factions.md` | **READY** (GD-2 boundary) |

### §1.5 Territory + Peninsular + World + Cross-scale (mostly ready)

All territory/peninsular/world modules canon-grounded. Cross-scale layer ready except as noted.

- **Territory** (settlement / infrastructure / adjacency / temperaments): all **READY**
- **Peninsular** (season / accounting / ci_track / rs_track / ms_track / ip_track): all **READY**
- **World** (restoration_movement / miraculous_event / insurgency_pipeline / npe): `insurgency_pipeline.py` **READY** post-Pass 2i; others **READY** for core implementation; `restoration_movement.py` core canonized (v12c §4.2) but full canon doc Pass 2d pending
- **Cross-scale** (domain_echo / zoom_in_out / handoff_rules / articulation): all **READY**

---

## §2. Dependency Graph

Implementation must respect dependency direction (provincial → personal → primitive, peninsular → provincial → personal, etc., per `sim/CONVENTIONS.md`). Phases sequenced so each phase only depends on prior phases' completion.

```
Phase 1 (Foundations) — no upstream dependencies
├── sim/autoload/dice_engine.py
├── sim/autoload/game_state.py
├── sim/autoload/season_manager.py
├── sim/autoload/scene_slate.py
├── sim/autoload/registry.py
└── sim/autoload/victory.py [GD-1 boundary]

Phase 2 (Personal primitives) — depends on Phase 1
├── sim/personal/combat.py
├── sim/personal/contest.py
├── sim/personal/conviction.py [post-HR-1 strike]
├── sim/personal/beliefs.py
├── sim/personal/companion.py
└── sim/territory/* (settlement, infrastructure, adjacency, temperaments)

Phase 3 (Thread layer) — depends on Phase 1-2
├── sim/thread/coherence.py [foundations P-10, P-15]
├── sim/thread/operations.py
├── sim/thread/co_movement.py
├── sim/thread/rendering.py
└── sim/thread/threadcut.py

Phase 4 (Cross-scale) — depends on Phase 1-3
├── sim/cross_scale/handoff_rules.py
├── sim/cross_scale/zoom_in_out.py
├── sim/cross_scale/domain_echo.py
└── sim/cross_scale/articulation.py [PP-688]

Phase 5 (Fieldwork + Investigation + Tribunal/Parliamentary) — depends on Phase 1-3
├── sim/personal/fieldwork.py
├── sim/personal/investigation.py
├── sim/personal/tribunal.py [calls contest]
├── sim/personal/parliamentary_vote.py [GD-3 status-flag gate]
└── sim/personal/parliamentary_stay.py

Phase 6 (Knots + Thread integration) — depends on Phase 2-5
├── sim/personal/knots.py [BLOCKED on TIER-DRIFT-001]
└── sim/thread/opposing.py [BLOCKED on TIER-DRIFT-001 — Knot Strain integration]
└── sim/thread/collective.py

Phase 7 (Mass battle) — depends on Phase 1-2, follows mass_battle_integration_v30 10-step plan
├── sim/provincial/units.py
├── sim/provincial/tactic_cards.py [BLOCKED on contamination audit]
└── sim/provincial/massbattle.py [10-step migration per Pass 2n]

Phase 8 (Universal faction actions) — depends on Phase 1-7
├── sim/provincial/crown_initiative.py [post-ED-840]
├── sim/provincial/excommunication.py [calls Phase 5 tribunal]
├── sim/provincial/absolution.py
├── sim/provincial/council_solmund.py
├── sim/provincial/charter_liberties.py
├── sim/provincial/parliamentary_transfer.py [calls Phase 5 parliamentary_vote + parliamentary_stay]
├── sim/provincial/mass_seizure.py
├── sim/provincial/treaty.py
└── sim/provincial/faction_action.py [GD-2 boundary]

Phase 9 (Faction-specific) — BLOCKED on contamination audit + Pass 2d/2e/2f
├── sim/provincial/vaynards_hall.py [BLOCKED — name + mechanic redesign + audit]
├── sim/provincial/einhir_revival.py [BLOCKED — Pass 2d + audit]
├── sim/provincial/altonian_reinforcements.py [BLOCKED — Pass 2e + audit]
├── sim/provincial/infrastructure_reclamation.py [BLOCKED — Pass 2f + audit]
└── sim/provincial/home_sanctuary.py [BLOCKED — Pass 2f + audit]

Phase 10 (World layer) — depends on Phase 1-9
├── sim/world/restoration_movement.py [v12c §4.2 core; Pass 2d for full canon]
├── sim/world/miraculous_event.py
├── sim/world/insurgency_pipeline.py [GD-3 boundary, Pass 2i]
└── sim/world/npe.py

Phase 11 (Peninsular orchestration) — depends on all prior phases
├── sim/peninsular/ci_track.py
├── sim/peninsular/rs_track.py
├── sim/peninsular/ms_track.py
├── sim/peninsular/ip_track.py
├── sim/peninsular/season.py
└── sim/peninsular/accounting.py [13-step cascade]

Phase 12 (Strategic orchestrator) — depends on all phases
└── sim/mc_v18.py [replaces tests/sim/v17-integration/mc_v17.py monolith]
```

**Critical path:** Phase 1 → Phase 2 → Phase 5 → Phase 8 (parliamentary_transfer + treaty) → Phase 11 → Phase 12 → first v18 N=1000 sweep.

**Parallel paths:** Phase 3 (Thread) and Phase 7 (Mass battle) can proceed alongside Phase 5 once Phase 1-2 complete. Phase 4 (Cross-scale) can proceed alongside Phase 7.

---

## §3. Implementation Phases — Sequenced Build

Each phase produces a working sim subset. Phase exit criteria are gate-checked at commit.

### Phase 1 — Foundations (target: Pass 2 follow-up week 1)

**Deliverables:**
- All 6 autoload modules implemented (non-`NotImplementedError`)
- Tests under `sim/tests/autoload/` covering each module's entry points
- Round-trip test: `sim.autoload.registry.load_index('canon/mechanics_index.yaml')` produces validated MechanicsIndex object
- GD-1 boundary test: `sim.autoload.victory.peninsular_sovereignty()` is the ONLY victory function exported; assertion fails if any other victory function is registered

**Exit criterion:** all autoload modules pass smoke tests; mechanics_index loads; victory boundary asserted.

### Phase 2 — Personal Primitives (target: week 2)

**Deliverables:**
- combat.py, contest.py, conviction.py, beliefs.py, companion.py implemented
- territory/ modules (settlement, infrastructure, adjacency, temperaments) implemented
- Personal-scale single-action tests (1 round of combat; 1 exchange of contest; 1 conviction shift; 1 belief revision)

**Exit criterion:** PersonalPhaseScene-equivalent flows produce expected outcomes for canonical examples.

### Phase 3 — Thread Layer (target: week 3, parallel with Phase 5)

**Deliverables:**
- coherence.py, operations.py (7 Thread ops), co_movement.py, rendering.py, threadcut.py implemented
- opposing.py and collective.py stubs (FULL implementation blocked on TIER-DRIFT-001 — see §7 below)
- Cross-scale tests: Leap → Coherence track update; Mending → opposing-ops Knot Strain (when knots ready)

**Exit criterion:** all 7 Thread operations resolve correctly per canon. Coherence track responds to mechanics.

### Phase 4 — Cross-scale (target: week 3, parallel with Phase 3)

**Deliverables:**
- handoff_rules.py (8 handoff rules), zoom_in_out.py, domain_echo.py, articulation.py (Tier 1/2/3) implemented
- Cross-scale test: scene result → faction state via domain_echo

**Exit criterion:** 8 scale_transitions handoff rules pass smoke tests. Articulation Tier 2 trigger ruleset fires correctly on canonical cases.

### Phase 5 — Fieldwork / Tribunal / Parliamentary contests (target: week 4)

**Deliverables:**
- fieldwork.py, investigation.py, tribunal.py, parliamentary_vote.py, parliamentary_stay.py implemented
- GD-3 status-flag enforcement at parliamentary_vote.py
- Tests: full fieldwork scene → evidence track advancement; Excommunication Tribunal flows; Parliamentary Vote with extra-parliamentary block

**Exit criterion:** all five personal-scale contest types resolve correctly. GD-3 boundary enforced.

### Phase 6 — Knots + Thread Integration

**Status:** **BLOCKED on TIER-DRIFT-001 resolution (Pass 2k).**

When unblocked:
- knots.py implemented per `knots_v30.md` (with tier system resolved per Jordan)
- opposing.py (Knot Strain integration) and collective.py implemented
- Tests: Knot formation Spirit Ob 2; Knot strain accumulation; rupture consequences (Composure damage TBD per COMPOSURE-DRIFT-001 resolution); Anchoring Scene Coherence +1

**Exit criterion:** Knots functional end-to-end. PP-632 invariants verified.

### Phase 7 — Mass Battle (target: week 4-7, follows Pass 2n 10-step plan)

**Deliverables:** per `mass_battle_integration_v30.md` §4 step sequence:
1. Bare port (byte-equivalent to sim_mb_06_v22)
2. LETHALITY_SCALE restoration (15% per-turn casualty target)
3. Flanking detection
4. Penetration morale shock
5. Cell displacement ripple
6. Equal-speed tiebreakers
7. Phase-boundary hooks (rally / reform / threadwork)
8. Internal collision wiring
9. Cleanup (halt_before_enemy deletion; STAMINA_DRAIN doc; POOL_VARIANT 0.5)
10. Strategic-layer integration

**Tactic_cards module BLOCKED on contamination audit.**

**Exit criterion:** D-8 battery `tests/sim/battery_v22.py` produces 12/13 in-band per v9 historical spec. Multi-turn calibration at 14-16% per-turn casualties.

### Phase 8 — Universal Faction Actions (target: week 5-8)

**Deliverables:**
- crown_initiative.py (Royal Progress iter, Great Work, Coronation Renewal) per Pass 2h amendment
- excommunication.py (calls tribunal), absolution.py, council_solmund.py, charter_liberties.py
- parliamentary_transfer.py (calls parliamentary_vote + parliamentary_stay)
- mass_seizure.py (3-source drift reconciliation pending Pass 2f formalization)
- treaty.py (lapse + violation per Pass 2h)
- faction_action.py (GD-2 boundary)

**Exit criterion:** universal mechanics dispatchable. GD-2 boundary enforced (mandatory before stochastic). All universal mechanics reproduce v12c balance at N=100 baseline.

### Phase 9 — Faction-specific Mechanics

**Status:** **BLOCKED on contamination audit + Pass 2d/2e/2f canon authoring.**

Per Pass 2 master plan, Pass 2d / 2e / 2f are deferred pending Jordan's contamination audit (per Jordan diagnosis 2026-05-17 that faction-identity claims in canon have been re-inserted by prior Claude sessions). The faction-specific modules cannot proceed against contaminated traits.

When unblocked (audit complete + Pass 2d/2e/2f authoring):
- vaynards_hall.py (name + mechanic redesign per Jordan)
- einhir_revival.py (Varfell)
- altonian_reinforcements.py (Hafenmark with choice-lock)
- infrastructure_reclamation.py (Church)
- home_sanctuary.py (Church T9)
- hafenmark_equipment.py (Wagenburg + Bombards tactic cards)

**Exit criterion:** v12c balance reproduced at N=1000 with all faction-specific mechanics enabled. Win-rate distribution within 20-30% per faction (per v12c §5.2 target).

### Phase 10 — World Layer (target: week 6-8)

**Deliverables:**
- restoration_movement.py (v12c §4.2 PT decay; full canon Pass 2d pending)
- miraculous_event.py
- insurgency_pipeline.py (4-stage model per Pass 2i)
- npe.py

**Stage 3 Insurgency stat baseline BLOCKED on INSURGENCY-STATS-001 resolution.**

**Exit criterion:** RM PT decay reproduces v12c per-arc rate. Insurgency formation triggers correctly per GD-3 (a). Promoted Faction emergence branches correctly (PT < 3 → extra-parliamentary, PT ≥ 3 → parliamentary).

### Phase 11 — Peninsular Orchestration (target: week 8)

**Deliverables:**
- ci_track.py, rs_track.py, ms_track.py, ip_track.py implemented
- season.py (season loop)
- accounting.py (13-step end-of-season cascade including: RM PT decay, Treaty expiration check, Insurgency formation/promotion check, all world-tracks update, faction stat reconciliation)

**Exit criterion:** Full season runs cleanly. Accounting cascade order matches campaign_architecture_v30 spec.

### Phase 12 — Strategic Orchestrator (target: week 8-9)

**Deliverables:**
- mc_v18.py (~150 lines, orchestrator only)
- `run_campaign(seed, max_seasons=100)` produces complete campaign trace
- `run_balance_sweep(n_campaigns=1000)` produces faction win-rate distribution

**Exit criterion:** v18 produces v12c-equivalent balance (Crown 24.7% / Church 28.6% / Hafenmark 24.2% / Varfell 22.5% within ±3pp) when all Pass 2d/2e/2f mechanics ratified and contamination audit complete.

---

## §4. Test Status Progression Targets

Per `canon/mechanics_index.yaml` schema:

| Status | Trigger | Modules expected at each tier post-Phase-N |
|---|---|---|
| `not_implemented` | Stub state | Phase 0 (current); pre-Phase-N for that module |
| `provisional` | Implementation present, smoke tests pass | Phase 1-N exit |
| `validated_n100` | N=100 sweep produces expected output range | Phase 7 (mass battle), Phase 8 (universal mechanics) |
| `validated_n500` | N=500 sweep statistically stable | Phase 12 mid |
| `validated_n1000` | N=1000 sweep matches v12c balance | Phase 12 final exit |
| `canonical` | validated_n1000 + GD-compliant + matches canon expectation | Triple-pass review verdict (Pass 3) |
| `contested` | Audit-blocked | Phase 9 modules (blocked); tactic_cards |
| `superseded` | GD-1 strike applied | Faction-specific victory paths (Pass 2c outcome) |

Updates flow into `canon/mechanics_index.yaml` via co-commit per CONVENTIONS.md (Pass 2j enforcement, pending v2 generator integration).

---

## §5. Test Plan — Per-Module Gates

### §5.1 Smoke tests (Phase exit minimum)

Every implemented module must have:
1. `test_<module>_imports_clean` — module imports without exception
2. `test_<module>_entry_points_match_docstring` — public entry-points listed in docstring exist as callable functions
3. `test_<module>_gd_boundary` (where applicable) — GD-1/2/3 constraint not violated by any entry point
4. `test_<module>_canon_reference_resolves` — canon_source paths resolve to existing files

### §5.2 Behavioral tests (Provisional status)

Per-module behavioral tests targeting canonical examples:
- Combat: 1 round resolution matches expected outcome for canonical attacker/defender pair
- Contest: 1 Exchange resolution per `social_contest_v30 §4` Step 1-7 sequence
- Fieldwork: 1 scene → Evidence Track advance
- Thread operations: each of 7 operations executes a canonical case
- Mass battle: 1 round of 1 engagement pair resolves with simultaneous damage application
- Parliamentary Vote: 4-faction vote with bloc majority produces correct outcome
- Treaty Expiration: arc-boundary check produces 90% lapse rate at N=100

### §5.3 Balance tests (Validated_n1000 status)

Per `tests/sim/v17-integration/m7_balance_sweep.py` pattern, but against v18:
- Run N=1000 campaigns with canonical seed
- Faction win-rate distribution within 20-30% per faction
- All v12c parameters honored (RM_PT_DECAY_CHANCE=0.35, TREATY_LAPSE_RATE=0.90, etc.)
- Mass battle D-8 historical battery 12/13 in-band

### §5.4 GD-compliance gates (Canonical status)

Final tier requires:
- GD-1 invariant: no faction-specific victory triggers in code (grep + AST-walk)
- GD-2 invariant: mandatory action precedence in faction_action.py
- GD-3 invariant: status-flag enforcement at parliamentary_vote.py + parliamentary_transfer.py + treaty.py + insurgency_pipeline state machine valid
- All forward-flags from Pass 2g/h/i/n/m resolved at Pass 2k editorial-ledger

---

## §6. Validation Sequence (week-by-week target)

| Week | Phase | Module count implemented | Cumulative test_status |
|---|---|---|---|
| 1 | Phase 1 | 6 autoload | 6 `provisional` |
| 2 | Phase 2 | + 5 personal + 4 territory | 15 `provisional` |
| 3 | Phase 3 + 4 | + 7 thread + 4 cross_scale | 26 `provisional` |
| 4 | Phase 5 | + 5 personal contests | 31 `provisional` |
| 5-6 | Phase 7 (mass battle, 10 steps) | + 3 provincial (units, tactic_cards stubbed, massbattle) | 34, D-8 battery 12/13 |
| 5-8 | Phase 8 (universal faction actions) | + 9 provincial | 43 |
| 6-8 | Phase 10 (world) | + 4 world | 47 |
| 8 | Phase 11 (peninsular) | + 6 peninsular | 53 |
| 8-9 | Phase 12 (strategic) | + mc_v18 | 54 |
| Post-2k | Phase 6 (knots) | + 3 personal/thread (knots, opposing, collective) | 57 |
| Post-audit | Phase 9 (faction-specific) | + 6 provincial | 63 |
| Pass 3 | Final review | All `validated_n1000` → `canonical` where eligible | 86 mechanics finalized |

**Note:** 86 mechanics-index entries vs 72 sim modules — primitives are mechanics but don't have unique modules (multiple primitives in `dice_engine.py`); services are infrastructure (not all are independent "mechanics"); some mechanics span multiple modules.

---

## §7. Blocked Modules — Resolution Routes

### §7.1 Blocked on Pass 2k editorial-ledger (20 forward-flags accumulated)

Resolution = Jordan ratification at Pass 2k batch:

| Flag | Module(s) affected | Phase blocked |
|---|---|---|
| TIER-DRIFT-001 (knots) | knots.py, opposing.py, collective.py | Phase 6 |
| COMPOSURE-DRIFT-001 (knots) | knots.py | Phase 6 (subset) |
| TRUNC-DRIFT-001 (knots) | coherence.py band-Severed row | Phase 3 (subset) |
| PARL-MODE-DRIFT-001 | parliamentary_transfer.py | Phase 8 (mode-specific effects) |
| PARL-VOTE-MODIFIER-001 | parliamentary_transfer.py | Phase 8 (vote-bloc Pool modifier) |
| PARL-PROTECTION-001 | parliamentary_transfer.py | Phase 8 (self-transfer block confirm) |
| TREATY-VIOLATION-001 | treaty.py | Phase 8 (violation magnitudes) |
| TREATY-NARRATIVE-001 | treaty.py | Phase 8 (active-maintenance alt consideration) |
| TREATY-MEMORYLESS-001 | treaty.py | Phase 8 (memoryless confirmation) |
| INSURGENCY-STATS-001 | insurgency_pipeline.py | Phase 10 (Stage 3 stats) |
| INSURGENCY-STATUS-MUTABILITY-001 | insurgency_pipeline.py | Phase 10 (post-promotion mutability) |
| INSURGENCY-CONVICTION-DERIVATION-001 | insurgency_pipeline.py | Phase 10 (Stage 4 Convictions algorithm) |
| INSURGENCY-DISSOLUTION-001 | insurgency_pipeline.py | Phase 10 (Stage 3 dissolution Option A/B) |
| INSURGENCY-PROMOTED-DISSOLUTION-001 | insurgency_pipeline.py | Phase 10 (Stage 4 dissolution) |
| INSURGENCY-DEMOTE-DIRECTION-001 | insurgency_pipeline.py | Phase 10 (non-symmetric model confirm) |
| LATENT-RM-vs-INSURGENCY-RM-001 | restoration_movement.py + insurgency_pipeline.py | Phase 10 (layered interpretation confirm) |
| SPEED-1 (mass battle) | massbattle.py | Phase 7 (speed tier table) |
| POOL-0.5 (mass battle) | massbattle.py | Phase 7 (POOL_VARIANT 0.5 canonization) |
| D-2 (mass battle) | massbattle.py | Phase 7 (shared vs per-unit grid) |
| D-8-interim (mass battle) | tests/sim/battery_v22.py | Phase 7 (interim-band canonization decision; doc resolves "no" already) |

### §7.2 Blocked on Contamination Audit (Jordan diagnosis 2026-05-17) — RESOLVED via Placeholder Registry (Option A, 2026-05-17)

**Status update 2026-05-17 (Pass 2 follow-up Option A):** Faction-specific module implementation UNBLOCKED via the generic-name placeholder mechanism. Two modules renamed (`vaynards_hall` → `varfell_mandate_action`; `einhir_revival` → `varfell_territorial_acquisition`); four functional-named modules + 2 audit-pending modules (`tactic_cards`, `npc_ai`) registered in `canon/placeholder_names.yaml` with `deadline_status: pending`. Hook `valoria_hooks.placeholder_names_gate` enforces rename precondition once Jordan flips status to `expired` post-audit.

Mechanic shape implementation can proceed against:
- Renamed modules (`varfell_mandate_action`, `varfell_territorial_acquisition`) using generic placeholder names + mechanism-only specs
- Functional-named modules (`altonian_reinforcements`, `infrastructure_reclamation`, `home_sanctuary`, `hafenmark_equipment`, `tactic_cards`, `npc_ai`) using mechanism-only specs without identity content

Pass 2d/e/f authoring can now proceed against placeholder identity. Contamination audit becomes a follow-on rename-and-content-audit pass (target: post-Pass-3, before any Phase-9 implementation work).

Registry: `canon/placeholder_names.yaml` (8 entries; canonical_name_pending fields track replacement decisions).

### §7.3 Blocked on Pass 2d (Varfell canon)

`einhir_revival.py` and `restoration_movement.py` (full doc) both depend on Pass 2d authoring. Pass 2d depends on contamination audit completion.

### §7.4 Blocked on Pass 2e (Hafenmark canon)

`altonian_reinforcements.py` and `hafenmark_equipment.py` depend on Pass 2e authoring + tactic_cards audit.

### §7.5 Blocked on Pass 2f (Church canon)

`infrastructure_reclamation.py`, `home_sanctuary.py`, plus mass_seizure 3-source drift reconciliation, depend on Pass 2f.

---

## §8. v17 → v18 Migration Discipline

### §8.1 v17 remains canonical-functional until Phase 12 exit

`tests/sim/v17-integration/mc_v17.py` is the **current balance simulator**. v18 line under `sim/` is the **build target**. v17 is NOT modified during Pass 2 work. v17 deprecation occurs only after v18 reaches Phase 12 exit (`validated_n1000` matching v12c balance).

### §8.2 No premature v17 deletion

Per Pass 2l commit message: "v17 line at tests/sim/v17-integration/ is untouched and remains the current balance simulator." This stands through Phase 1-11. Phase 12 exit gates v17 archival.

### §8.3 Test parity check at Phase 12

Before v17 deprecation, run both v17 (existing) and v18 (new) at N=1000 with identical seeds. Faction win-rate distributions must match within ±2pp per faction. Mismatch larger than ±2pp triggers root-cause investigation, not v17 deletion.

### §8.4 v17 archival (post-Phase 12 only)

When v18 passes parity check, move v17 to `tests/sim/v17-archived/` and update `canon/supersession_register.yaml` with the v17-supersession entry. v17 code remains queryable as supersession-trail evidence but is not part of active build.

---

## §9. Pass 2 → Pass 3 Hand-off

Triple-pass review (Pass 3) consumes the Pass 2 work. Per `<triple_pass_review>` discipline:

- **Pass 1** (catalog): Pass 2a / 2a-extended / 2a-3 surveyed; Pass 2 plan formed
- **Pass 2** (granular build): Pass 2b through 2m (this doc) — execute against plan
- **Pass 3** (re-review verdict): pending. Will verify:
  1. Every Pass 1 catalog item is addressed OR deferred-with-reason
  2. No edit introduced a new contradiction in canon
  3. Edits compose — Pass 2c strike-propagation didn't break Pass 2g knots; Pass 2h Royal Progress fix didn't undermine Pass 2b GD-1; etc.
  4. The deliverable still serves the original ask (integrate all systems into modular simulation; produce mechanics index; surface contamination)
  5. All 20+ forward-flags from Pass 2g/2h/2i/2n collected for Pass 2k batch

---

## §10. Cross-references

### Canon authority chain

`canon/02_canon_constraints.md` §B GD-1/2/3 → `canon/mechanics_index.yaml` → individual canon docs → sim modules.

### Sim modules (all 72)

See `sim/__init__.py` subpackage summary; `sim/README.md` for orientation; `sim/CONVENTIONS.md` for module-stub anatomy.

### Pass 2 commit log

- `fe367105` Pass 2b — GD-1/2/3 canonized
- `eaabf455` Pass 2c — HR-1 strike propagation
- `80b4eb7e` Pass 2l — sim/ armature 72-file scaffold
- `d493944f` Pass 2j — mechanics_index v1 + generator
- `2420a193` Pass 2n — mass battle integration spec
- `98417ac9` Pass 2g — knots unification + 3 canon drifts
- `3985cea0` Pass 2h — Royal Progress iter (ED-840 closed) + Parliamentary Transfer + Treaty Expiration
- `6d6373c9` Pass 2i — insurgency pipeline (GD-3)
- `[pending]` Pass 2m — this doc
- `[pending]` Pass 2k — ED batch
- `[pending]` Pass 3 — final review verdict

---

## §11. Forward-flags surfaced by Pass 2m

| ID | Description | Resolution required |
|---|---|---|
| **INTEGRATION-WEEK-CADENCE-001** | §6 week-by-week cadence is Pass 2m derivation. Actual rate depends on implementation speed and Pass 2k resolution rate. | Confirm or adjust target cadence at first weekly check-in. |
| **V17-V18-PARITY-TOLERANCE-001** | §8.3 ±2pp per-faction win-rate parity tolerance is Pass 2m proposed. Tighter (e.g., ±1pp) or looser (e.g., ±3pp) tolerance may be appropriate. | Jordan ratify tolerance. |
| **PHASE-9-SEQUENCING-001** | §3 Phase 9 (faction-specific) is blocked on contamination audit. If audit splits per-faction (1 turn per faction), Phase 9 can also split into Phase 9a (Crown — non-blocked) / 9b (Hafenmark) / 9c (Church) / 9d (Varfell). | Confirm split sequencing if audit splits per-faction. |

These 3 new forward-flags add to Pass 2k batch (23 total accumulated).

---

## §12. Status Declaration

[STATUS: CANONICAL — Pass 2m 2026-05-17. Executable build roadmap for v18 modular sim. Phase sequencing, dependency graph, test plan, validation gates, and blocking conditions are all canon-grounded. 3 new derivation flags forward-flagged for Pass 2k. Phase exit criteria defined per phase. v17 → v18 migration discipline established.]

Pass 2 is now content-complete for the planned scope. Remaining work:
- **Pass 2k** — Editorial-ledger batch resolving the 23 forward-flags
- **Pass 3** — Triple-pass review verdict over all Pass 2 work
- (Deferred) **Pass 2d/2e/2f** — Faction-specific canon, gated by Jordan contamination audit
- (Implementation) **Phase 1-12** — execute v18 build per this plan

---

## §13. Changelog

- **v30 init (2026-05-17, Pass 2m):** Initial authoring. Synthesizes Pass 2b/2c/2g/2h/2i/2j/2l/2n into 12-phase build roadmap for sim/ v18 modular armature. Maps 72 modules to canon source + dependency chain + test status target. Identifies 20 forward-flag blocks from prior Passes plus 3 new ones (INTEGRATION-WEEK-CADENCE-001, V17-V18-PARITY-TOLERANCE-001, PHASE-9-SEQUENCING-001) for Pass 2k batch. Establishes v17 archival discipline gated on v18 Phase 12 parity check. Pass 2 declared content-complete pending Pass 2k + Pass 3.
