# Valoria Roadmap
**Generated:** 2026-04-26 · session token `8ca3fffeaca3bb9c`
**Sources:** design_sync.md (2026-04-18), conversion_ledger.md, coverage_matrix.md (2026-04-13), audit_2026-04-12.md, session_checkpoint.md (2026-04-20), session_log_current.md (2026-04-26), editorial_ledger.yaml, file tree of both repos.

---

## 0 · Reading the State

**Two repos. Two phase systems. Don't conflate.**

| System | Status |
|---|---|
| `jordanelias/ttrpg` orchestrator compliance phases | Pre-Phase 0 (`compliance_check.py` not deployed; manual hooks via `valoria_hooks.py`) |
| `jordanelias/valoria-game` implementation phases | Phases 0–5 complete · Phase 6 partial · Phase 12 most-recent test pass |
| `tests/sim/valoria_full_campaign_sim.py` verification harness | Session 1 of 3 committed (129f2f2b) |

The Godot codebase is mid-build, not a green field. ~250 KB of GDScript across 60 system files, 32 scene files, 71 resources, 6 test files.

---

## 1 · What's Actually Done

### 1.1 valoria-game (Godot)

**Engine layer — DONE.**
CoreResolver, CoreEngine, ConsequenceRouter, RollContext, all 6 ResolutionModes, TrackerRegistry/Tracker/Threshold, all 24 data type Resources, 5 registries (Character/Faction/Setting/Narrative/Unit). All Phase-0 critical bugs (B-01–B-07) resolved.

**Domain systems — DONE or near-done.**
DomainActionSystem, ThreadworkSystem (3-axis mechanics; card content deferred), InvestigationSystem, SkillSparkingSystem, SkillEffectResolver, KnotFormationSystem, RMPresenceSystem, ValoriaFactionAI, FactionTurnSystem, CombatLogic (32 KB), BattleLogic (PP-233), CombatInitiativeSystem, CascadeEngine, SituationGenerator, TriggerRuleRegistry.

**Containers — DONE (logic) / GAP (.tscn files).**
Battle, Board, Combat, Conflict, Debate, Narrative — all have `.gd` logic files. `.tscn` scene files exist as stubs (75–341 b each); proper scene authoring requires Godot editor.

**Character data — DONE.**
24 character `.tres` instances (9 extended, 15 primary). 15 trigger `.tres` instances.

**Tests — PARTIAL.**
6 GDScript test files cover dice engine, tracker registry, season loop, integration, canonical examples. `test_dice_engine.gd` and `test_tracker_registry.gd` flagged as never-run in conversion_ledger but coverage_matrix says Phase 12 passed — **needs verification**.

### 1.2 ttrpg (design canon)

- 697 files. 6 active editorial entries (next_id 750). 16 entries archived 2026-04-23.
- Latest sweep: TC→CI, RS→MS, Maret→Yrsa propagation across ~1,800 instances. Closed 2026-04-26. P1-BLOCKER count = 0.
- `tests/sim/valoria_full_campaign_sim.py` Session 1 (foundation): 623 lines, 103-entry verification ledger, smoke tests pass.

---

## 2 · What's Live Right Now

| ID | Stream | Status |
|---|---|---|
| **VG-A** | valoria-game Phase 6 (Threadwork/Victory) | Code partial; tests gap (Phase 9 victory, Phase 10 Domain Echo, Phase 11 ArcEvaluator all ⬜) |
| **SIM-S2** | Campaign sim Session 2 | Pending start — Territory T1-T15, DA framework, Piety Yield, Strain propagation, mass combat, contests, faction AI stub, 40-season smoke |
| **ED-Q** | Editorial open queue | ED-543 P1 (clock registry verification) · ED-710/711 P2 (settlement adjacency, fractional province) · ED-745–748 P3 (PROVISIONAL marker verifications) |
| **WB-D** | Worldbuilding decisions | D-4 Altonian invasion ~18 AG (per ED-725) · D-5 Einhir site-network (per ED-726) — block spec finalization |

---

## 3 · The Roadmap

### Phase A — Stabilize & Verify (1–3 sessions)
*Close the loop on what's already shipped before adding more.*

| Item | Repo | Why now |
|---|---|---|
| Run `test_dice_engine.gd` + `test_tracker_registry.gd` end-to-end; confirm passes | valoria-game | Conversion ledger says never run; coverage matrix implies passed. Resolve the contradiction. |
| Refresh `conversion_ledger.md` with current state (Phases 0–5 complete + Phase 6 partial); update post-restructure paths from `design_sync.md §Conversion Ledger Path Updates` | valoria-game | Single source of truth for ported state |
| Fix Church faction stats in `ValoriaDataLibrary.gd` (Man 5→4, Wea 5→3) | valoria-game | Flagged in design_sync.md, not addressed |
| Resolve **ED-543 (P1)** clock registry refresh | ttrpg | Highest open severity; one P1 in active ledger |
| Verify ED-745–748 PROVISIONAL markers against `canonical_definitive_r2`; close or escalate | ttrpg | P3 cleanup, but blocks ledger health |
| Update `valoria-game/README.md` from "hybrid TTRPG/board game" to videogame-only | valoria-game | Stale since 2026-04-17 mode collapse |

**Exit criteria:** Tests run and pass. Conversion ledger reflects truth. P1-BLOCKER count remains 0. Editorial ledger reduced to ED-710/711 + worldbuilding holds.

---

### Phase B — Worldbuilding Authority (Jordan-blocking)
*Cannot proceed past these without your decisions.*

| ID | Decision needed | Impact |
|---|---|---|
| **D-4** | Altonian invasion timeline (~18 AG canonical date per ED-725) | Locks campaign-start clock state; gates all sims that begin pre/post invasion |
| **D-5** | Einhir site-network model (new spec per ED-726) | Threadwork substrate spec; gates Threadwork Phase 4 finalization in Godot |
| **Open** | Ministry NPC design doc location | Flagged in `params/bg/core.md` NPC-Only Factions; unresolved since session_checkpoint 2026-04-20 |

**Exit criteria:** Three written decisions. Each lands as an editorial entry that resolves D-4/D-5 and locates or creates the Ministry doc.

---

### Phase C — Sim Session 2: Middle Layer (1–2 sessions)
*Verify the strategic stack before Godot finalization.*

Per `canon/session_checkpoint.md` next_bootstrap_actions:

1. Re-fetch `params/factions/stats_1_7_scale.md §Domain Action Table` + `faction_politics_v30.md §2` for DA catalog
2. Read `designs/territory/settlement_layer_v30.md` for T1-T15 canonical data
3. Read `designs/provincial/ci_political_v30.md §1` for Piety Yield formula
4. Extend `valoria_full_campaign_sim.py` with §6 Territory, §7 Domain Actions, §8 Contests, §9 Faction AI stub, §10 40-season smoke test
5. Append ledger entries for each new constant

**Exit criteria:** 40-season smoke test runs to plausible endgame. Verification ledger grows to ~200+ entries. Single commit, single file (architecture preference per Session 1).

---

### Phase D — Sim Session 3: Top Layer & Test Corpus (1 session)

- Threadwork mechanics (Thread Tension, Coherence, Leap, Weaving)
- Victory conditions (8 factions, Peninsular Sovereignty)
- Scale transitions (personal → faction → strategic)
- NPC priority trees for 7 named NPCs (Almud, Himlensendt, Baralta, Vaynard, Ehrenwall, Torben, Edeyja)
- Arc transitions per `npc_behavior_v30 §5.2` + `arc_expansion_v30`
- Royal Assassination fuse activation
- Tensions Deck card activations
- Deterministic-seed regression tests reproducing `sim_var_01` through `sim_var_06`

**Exit criteria:** Sim runs all canonical scenarios deterministically. Sim becomes the ground-truth oracle for Godot test parity.

---

### Phase E — Godot Phase 6 Completion (2–3 sessions)
*Close the gaps in coverage_matrix.md.*

| Coverage gap | Action |
|---|---|
| GAP-T-01 ThreadworkSystem co-movement integration | Build Meta mock; write Phase 12-2 test |
| GAP-T-02 `check_victory` unit tests | Build full faction/territory state mock |
| GAP-T-03 ValoriaFactionAI per-framework decision tree coverage | Branch coverage tests |
| GAP-T-04 NarrativeContainer investigation/evidence routing | Wire SituationGenerator → NPCTrajectoryEvaluator (currently A-02 stub) |
| Co-Movement card content | Defer to Phase F (asset content) |

**Exit criteria:** All P-numbered phases (P0–P11) green in coverage matrix. Sim parity tests pass against same inputs.

---

### Phase F — Resource Content Build (large, parallelizable)
*Fill the empty `.gitkeep` directories.*

Currently empty in `valoria-game/resources/instances/`:
- `weapons/` — needs canonical weapon stats (data already in `params_combat`)
- `armour/` — same
- `action_cards/` — Domain Action card definitions
- `co_movement_cards/` — Threadwork Co-Movement deck
- `factions/` — full FactionData instances (currently in `ValoriaDataLibrary.gd`, should be extracted)
- `territories/` — 17 TerritoryData instances with SW/PV/Proximity/Accord/POI
- `tables/` — lookup tables (TC milestones, RS thresholds, etc.)
- `characters/named/` — additional named NPCs beyond the 24 already in primary/extended
- `characters/templates/` — generated officer/local templates
- `triggers/` — currently 15 of TBD count; full Phase 8 catalogue per `trigger_catalogue.md`

**Exit criteria:** Trigger catalogue moves from "(None yet)" to full per-source extraction. Faction/territory data extracted from libraries into instance Resources. Item/weapon/armour data populated from params.

---

### Phase G — UI / Scenes / Audio / Visual (largest single effort)
*Currently 100% empty `.gitkeep` in every UI directory.*

Empty zones:
- `scenes/ui/persistent/` — RS+WC HUD (per `wc_survival_spine.md` UI requirement)
- `scenes/ui/season_overview/` — Layer 2 SeasonSlate display
- `scenes/ui/board_ui/`, `combat_ui/`, `debate_ui/`, `thread_ui/`, `cascade/`, `menus/`, `victory/`
- `scenes/transitions/` — ZoomManager animations
- `assets/audio/`, `sprites/`, `portraits/`, `backgrounds/`, `map/`, `ui/`
- `dialogue/` — branching dialogue tree assets
- `shaders/`
- `systems/ai/` — empty (high-level ai distinct from `ValoriaFactionAI`?)

**Recommendation:** UI work requires Godot editor sessions, not GitHub-only CLI. Plan distinct Godot-editor work blocks. The `.tscn` files will not author themselves through API commits.

**Exit criteria:** Each Layer 2/3/4 UI element has a working scene. RS+WC primary HUD live. ZoomManager animates between Board/Battle/Combat. Cascade Display reads Meta visual queue.

---

### Phase H — Save System Hardening
*Audit DA-01 / DA-02 / DA-03 carry-forward.*

- DA-01: enforce save/load order (registration before deserialize)
- DA-02: extract `card_hand` from `FactionData` to `CardHandState` resource (otherwise hands lost on save)
- DA-03: implement `NarrativeState.deserialize()` (currently stub — NPC trajectories reset on load)

**Exit criteria:** Full save/load round-trip preserves NPC arcs, faction card state, narrative log.

---

### Phase I — Long-Tail Editorial / Tooling

| Item | Severity |
|---|---|
| RS test disambiguation (~1,340 instances; needs Mending Stability vs Rhetorical Style classifier) | High volume, low severity |
| ED-768 (P3) PROVISIONAL marker audit (13 orphaned) | P3 |
| `doc_index_gen.py` regen (index files stale post-rename) | Mechanical |
| Python sim file Maret rename in `campaign_sim_npc_pcs_2026-04-18.py` (currently fabrication-check blocked) | Low |
| TC in `deprecated/` files | Low |
| TD disambiguation (Mermaid TD vs removed Thread Depth PP-166) | Low |
| Add `RS = Rhetorical Style` to `alias_registry` if canonical | Pending term confirmation |
| Build `compliance_check.py` for ttrpg orchestrator (move from pre-Phase 0 → Phase 0) | Infrastructure |

**Exit criteria:** Editorial register at near-zero open items. Compliance hooks automated rather than asserted.

---

## 4 · Cross-Stream Dependencies

```
WB-D (D-4 Altonian, D-5 Einhir)
   ↓ blocks
Sim Session 2 (Phase C) — needs locked timeline + threadwork substrate spec
   ↓ feeds
Sim Session 3 (Phase D) — Threadwork + Victory verification
   ↓ feeds
Godot Phase 6 finalization (Phase E) — sim is oracle for parity tests
   ↓ enables
Resource content (Phase F) — final values locked, instances safe to author
   ↓ enables
UI build (Phase G) — final mechanic surface known
```

**Phase A and Phase I run in parallel to all of the above.**
**Phase H can run any time after Phase E.**

---

## 5 · Risk Register

| Risk | Mitigation |
|---|---|
| `conversion_ledger.md` and `coverage_matrix.md` disagree on Phase 0 test status | Phase A item 1: actually run the tests |
| Sim Session 2/3 reveals mechanics that break already-shipped Godot code | Sim is the oracle — fixes go to Godot. Treat as design correction, not regression. |
| `D-4`/`D-5` decisions delay → Sim Session 2 cannot start with locked inputs | Run Phase A and Phase I in the meantime; do not start Sim S2 with provisional values |
| UI work (Phase G) requires sustained Godot editor sessions, not API-driven | Plan editor blocks separately from GitHub work. Mark Phase G as out-of-band for orchestrator. |
| Faction stat Church values (Man=5/Wea=5) currently shipped wrong; any sim using ValoriaDataLibrary inherits the error | Phase A fix item; flag any sim that has run since 2026-04-18 |
| ttrpg has 30 commits since last valoria-game commit (per conversion_ledger §Design Repo Changes); some may not yet be ported (e.g. POI catalog, TC milestone rewrite, Standing 0–7 expansion) | Phase E port pass before Phase F resource authoring |

---

## 6 · Recommended Next Action

**Phase A item 1 + 2** in a single session:

1. Run `test_dice_engine.gd` and `test_tracker_registry.gd` in Godot. Verify pass.
2. Update `conversion_ledger.md` to reflect actual state (mark Phases 0–5 complete; Phase 6 partial; correct path renames).
3. Commit single `[infrastructure]` to valoria-game.

This unblocks every downstream phase and resolves the most damaging single source of confusion (a ledger that still says "Phase 0 IN PROGRESS").

After that, the choice is yours: **WB-D decisions** (unblocks Sim S2) or **ED-543 + ED-745–748** (clears ttrpg ledger to near-zero open). Either path is productive; both must happen before Sim Session 2.
