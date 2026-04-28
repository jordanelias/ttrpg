# Valoria Workplan v2 — Throughline-Organized
**Generated:** 2026-04-27 · session token `8ca3fffeaca3bb9c`
**Supersedes:** `valoria_workplan_throughline_organized.md` (v1, 2026-04-26)
**Framework:** PP-672/674 — N→Ω→Μ→М→Τ→Q→Μ̄
**Authority:** Jordan owns N, Ω, Μ. Co-owned М, Τ. Claude applies Q + protocol (§10).
**Grandfathering:** Pre-PP-672 items use `pre-framework: true`; structural alignment still tracked.

---

## §0 Data Cohesiveness — Single Source of Truth

**Problem.** Three documents give three different answers to "what implementation phase are we in":

| Document | Claims | Last updated |
|---|---|---|
| `valoria-game/docs/conversion_ledger.md` | Phase 0 IN PROGRESS; Phase 1 NOT STARTED | 2026-04-14 (stale) |
| `valoria-game/docs/design_sync.md` | Phases 0–5 complete; Phase 1 extraction all ✓ | 2026-04-18 |
| `canon/editorial_ledger_summary.yaml` | 12 active entries; total_active 12 | 2026-04-23 (auto-gen; stale — actual count is 6) |

**Root cause.** conversion_ledger was created Phase 0 and partially updated but never reconciled against design_sync's bulk-completion pass. editorial_ledger_summary was auto-generated before the 2026-04-26 sweep that resolved ED-660–705.

**Resolution.** This workplan is the sole authority for outstanding work. conversion_ledger and design_sync are reference sources for *what was done*, not for *what remains*. The workplan subsumes both. A reconciliation commit (item F0.1 below) will align all three to agree.

**Data cohesiveness rules applied throughout:**

1. **Every item traces to a source document.** No item exists from memory alone.
2. **Every PROVISIONAL is tracked with its promotion gate.** No provisional floats without a defined path to canonical or archive.
3. **Cross-repo items name both repos and the sync mechanism.** ttrpg design → Python sim → Godot implementation. Authority flows one direction only.
4. **Register regen follows every batch of changes.** No summary is trusted unless regenerated after the last substantive commit.

---

## §1 Bucket Taxonomy

| Bucket | Role | Protocol | Exit gate |
|---|---|---|---|
| **F · Foundation** | Broken or unverified — Μ modes impaired or data sources contradictory | Fix before downstream work is meaningful | All Μ modes operational; all sources-of-truth reconciled |
| **A · Authority** | N/Ω-tier decisions only Jordan can make | Block → escalate; never resolve autonomously | Written decisions landed as editorial/canon entries |
| **V · Validation** | PROVISIONAL specs + mechanical verification | Sim is oracle; outcome = promotion or redesign | All PROVISIONAL promoted or redesigned; sim serves as Godot parity oracle |
| **P · Playability** | First human-testable experience | Engine loop exercised end-to-end | One season playable; Q-robust dramatic legibility tested by a human |
| **C · Construction** | Class D content + Μ̄ implementation | Execute on stable canon | Resource instances populated; UI authored; persistence hardened |
| **M · Maintenance** | Class E cleanup | Run in parallel; never blocks | Registers at near-zero open; tooling automated |

**Change from v1:** Added **P · Playability** between V and C. Rationale: mechanical verification (sim) does not test experiential correctness. Q-robust's "dramatic legibility" criterion — "designer can read game-state and answer: whose position is at risk, what each actor wants, what happens if no one acts" — requires a human reading the actual game UI, not a Python console.

---

## §2 F · FOUNDATION

### F0 · Data reconciliation (prerequisite to all other F items)

| ID | Item | Action | Repo |
|---|---|---|---|
| **F0.1** | Status reconciliation | Update conversion_ledger.md: Phase 0 → COMPLETE, Phase 1 → COMPLETE (per design_sync evidence). Update design_sync `last_sync_date`. Regen editorial_ledger_summary.yaml to reconcile to actual 6 active entries. | valoria-game + ttrpg |
| **F0.2** | `videogame_mode_spec.md` as extraction authority | Verify all Phase 2+ extraction decisions in conversion_ledger reference this doc (`designs/architecture/videogame_mode_spec.md`). Currently absent from conversion_ledger entirely. Add as required-read header. | valoria-game |
| **F0.3** | `ms_budget.md` as centralized MS source | Verify `Meta.gd run_accounting()` implements all drain sources from ms_budget.md §2 and recovery sources from §3. Currently, conversion_ledger makes no reference to this doc despite it being canonical (ED-668) for all MS calculations. | valoria-game |

### F1 · Engine integrity (Godot — active Μ violations)

| ID | Item | Class | Framework failure | Fix | Blocks |
|---|---|---|---|---|---|
| **F1.1** | NPCTrajectoryEvaluator stub (A-02) | **B** (system extension — incomplete subsystem) | **Μ-β violation.** `SituationGenerator._evaluate_npc_trajectories` never calls evaluator. NPC arcs disconnected from season loop. T-23, T-25, T-15 silently fail. Failure lexicon: **Authored emergence** — world doesn't generate events without player. | Wire evaluator; verify per-faction priority trees fire. | V3 (GAP-T-04) |
| **F1.2** | Deferred consequence pipeline (B-07) | **B** | **Μ-δ violation.** `EngineResult.deferred_consequences` from VersusResolution never forwarded through `_on_versus_resolved` to ConflictContainer. Domain Echoes, Belief evaluations, NPC triggers vanish. T-23, T-21, T-22 cannot fire cross-scale. Failure lexicon: **Scale break.** | Forward deferred consequences through pipeline. | V3 |
| **F1.3** | GameMode enum still present | **E** (cleanup; no mechanic touches) | `Enums.gd` L44: `enum GameMode { TTRPG, HYBRID, BOARD }` — contradicts 2026-04-17 videogame-only collapse. `Constants.gd` has 5 mode-branched constants (RS_START_TTRPG, TC_START_TTRPG, IP_START_TTRPG, PI_START_TTRPG, SPARK_HYBRID_MINIMUM_OB). Dead code / latent bug source. | Strip enum. Collapse mode-branched constants to single videogame values per `videogame_mode_spec.md`. | — |
| **F1.4** | Church faction stats wrong | **C** (parameter) | `ValoriaDataLibrary.gd` Man=5 Wea=5; canonical Man=4 Wea=3. Μ-γ drift: wrong attractor. T-08 (Church institutional posture) encoded incorrectly. | Correct values. | V3 (Godot parity) |
| **F1.5** | Four Open Provisional Values | **C** (parameter) | `Constants.gd RS_BASELINE_DECAY=1`, `Meta.gd RS_initial=100`, `CombatLogic health=4`, `CombatLogic damage=placeholder`. Phase 0 provisionals never confirmed against params. | Verify each against canonical source (params/core.md, params/combat.md). Confirm or correct. | V3 |
| **F1.6** | Run test_dice_engine.gd + test_tracker_registry.gd | **E** | Conversion_ledger: "never been run." Coverage_matrix Phase 12 implies pass. Contradiction. | Run in Godot. Fix failures. Record results. | F0.1 (status reconciliation depends on knowing actual test state) |
| **F1.7** | README.md videogame-only | **E** | Still describes "hybrid TTRPG/board game." | Update. | — |

**Note on F1.1/F1.2 class correction from v1:** v1 classified these as Class E. They are Class B — incomplete subsystems whose absence constitutes active Μ-mode failure. A `vetting:` block is required for the fix PP entry. However, these are *restoration* fixes (wiring existing code that was always intended to be wired), not new proposals — they restore design intent, not add capability. The vetting block should note `restoration: true`.

**Sim independence:** F1.1, F1.2, F1.4, F1.5 are Godot-only bugs. The Python sim (`valoria_full_campaign_sim.py`) has its own data and consequence routing. F1 items block V3 (Godot parity), NOT V1/V2 (sim sessions). This corrects a dependency error in v1.

### F2 · Canon hardening

| ID | Item | Class | Severity | Touches | Action |
|---|---|---|---|---|---|
| **F2.1** | ED-543 clock registry refresh | E | **P1** (only active P1) | T-04, T-05, T-06, T-07 (М-1) | Determine if refresh landed under another ED. Close or execute. |
| **F2.2** | ED-745 IP=20 start | E | P3 | T-06 (М-1) | Cross-check `peninsular_strain §4` vs `params/bg/core` starting values. |
| **F2.3** | ED-746 Intel Advancement Counter | E | P3 | T-09, T-30 (М-8) | Confirm fieldwork VTM system fully replaces. **DIAGONAL: if Intelligence-as-stat is STRUCK (F2.5), then A3's Varfell Path A re-gate to "Intelligence ≥ 4" uses a struck stat. Flag to Jordan.** |
| **F2.4** | ED-747 Popular Will (PW) | E | P3 | T-15c (М-4) | Verify against RM founding mechanics. |
| **F2.5** | ED-748 Intelligence stat | E | P3 | T-09 (М-4) | Audit active specs for Intelligence-as-faction-stat references. **Result feeds A3.** |
| **F2.6** | ED-768 orphaned PROVISIONAL markers (13) | E | P3 | Cross-cutting | Jordan-review: classify still-open vs resolved-but-unarchived. |
| **F2.7** | Threadwork audit P0 triage | E | P0-equivalent | T-01, T-03, T-12, T-28 | `tests/stress/thread/threadwork_audit_register.md` contains 28 P0 blockers (2026-04-16). At least 5 partially resolved by subsequent work (P0-06/07/09 by ms_budget; P0-16 by Niflhel dissolution). **Remaining ~23 directly block V3 threadwork implementation and V2 Sim S3 threadwork module.** Triage: classify each as resolved/open/Jordan-decision. |
| **F2.8** | PP-652 starting PT values | C | P2 | T-07 (М-1) | PROVISIONAL starting PT per territory. Sim S2 needs these values. Verify or flag for promotion as V1 input. |
| **F2.9** | Patch register sweep policy | E | Infra | — | 164 active patches: 65 provisional, 61 proposed, 30 unknown. Define: promotion path for pre-PP-672 provisionals (bulk `pre-framework: true` + canonical-source-verification); archive path for proposed items superseded by subsequent work. |
| **F2.10** | Register regeneration | E | Infra | — | Regen: `editorial_ledger_summary.yaml`, `patch_register_index.md`, stale `*_index.md` files post-rename. Run `doc_index_gen.py`. |
| **F2.11** | hybrid_gaps_v30 propagation debt | E | — | М-5 (Μ-δ) | design_registry: "PROPAGATION-PENDING — 17 hybrid gaps not yet in bg_v05 / stage11." Post-videogame-only collapse, verify which gaps still apply and propagate or mark N/A. |
| **F2.12** | arc_register open editorials ED-401–405 | E | — | T-23, T-24 (М-5) | canonical_sources_notes: "Open editorials ED-401-405." Locate (likely pre-ledger); classify or archive. |

---

## §3 A · AUTHORITY UNLOCKS

### A1 · Vision-tier decisions (Jordan-blocking)

| ID | Item | Tier | Touches | Decision needed | Blocks |
|---|---|---|---|---|---|
| **A1.1** | D-5 Einhir site-network (ED-726) | **N** + Μ-δ + М-2 | T-15c (М-4), T-04 (М-3) | New mechanical layer or reskin of Mending sites? **N question:** what Renaissance political-leadership dynamic does "sacred-site network" model? (Candidate: pilgrimage-route economics / shrine-patronage politics — Medici chapel system, Habsburg Marian shrines.) | V1 (Sim S2 territory model), RM full spec |
| **A1.2** | D-4 Altonian invasion ~18 AG (ED-725) | Ω-c | T-06 (М-1), T-04 | Lock canonical timeline for campaign starting state. | V2 (deterministic test corpus) |
| **A1.3** | Ministry NPC design doc | Ω-c | T-08 (М-4), T-14 (М-6) | Locate or commission. Open since 2026-04-20. | Church full spec, npc_behavior_v30 §2 |

### A2 · Blocked v30 design docs

Each: accept compilation/stage source as canon, or commission design-layer doc?

| ID | Item | Mode | Touches | Unverified source | Impact if unresolved |
|---|---|---|---|---|---|
| **A2.1** | factions_ttrpg | TTRPG | T-08, T-09, T-11, T-15a/b/c (М-4) | stage6 | Personal-scale faction mechanics unverified |
| **A2.2** | campaign_modes | ALL | Cross-cutting | stage12 | Campaign parameters inherited from unverified source. Note: `videogame_mode_spec.md` exists and covers *mode collapse* but does NOT cover campaign-mode-specific parameters (campaign length, starting conditions, endgame triggers). The actual gap is narrower than v1 stated. |
| **A2.3** | southernmost (ED-048) | TTRPG | T-19 (М-2), T-04 | stage4 | Survival contest geography spec unverified. Open since 2026-04-04. Longest-standing blocker. |

**Blocking nuance (v1 correction):** A2 items *weaken* V1/V2 (sim uses data from canonical params, which may inherit unverified compilation values), but do NOT *block* them. Sim S1 already committed and passed without these docs. Mark as: **constrains confidence, does not gate execution.**

### A3 · STRUCK-system follow-up

| ID | Item | Class | Touches | Status | Notes |
|---|---|---|---|---|---|
| **A3.1** | Varfell victory paths editorial rewrite | **B** (post-PP-672; requires vetting block) | T-09 (М-4), T-20 (М-6) | Open since 2026-04-19; no PP | **DIAGONAL DEPENDENCY on F2.5:** If Intelligence-as-faction-stat is STRUCK, Path A re-gate to "Intelligence ≥ 4" is invalid. F2.5 resolution determines whether A3.1 is a parameter tweak (Class C) or a full path redesign (Class B). Do F2.5 before A3.1. |

### A4 · Solmund throughlines integration

| ID | Item | Tier | V2 impact |
|---|---|---|---|
| **A4.1** | T-A (Perceptual Prophylaxis as Literary Engine) | Τ → needs parent М + T-NN | **BLOCKS V2** — connects to Certainty track, which is in Sim S3 NPC priority trees |
| **A4.2** | T-B (Seam Texts as Mechanical Objects) | Τ | Does not block V2 — fieldwork Survey not in Sim S3 scope |
| **A4.3** | T-C (Double Consciousness Spiral) | Τ | **BLOCKS V2** — connects to faction AI + Conviction Track, both in Sim S3 |
| **A4.4** | T-D (Baralta as Accidental Prophylaxis Cracker) | Τ | Does not block V2 — explicitly "generational, not in-game mechanical" |
| **A4.5** | T-E (Solmund Repetition) | Τ | Weakly blocks V2 — arc emergence (T-23) |
| **A4.6** | Solmund Appendix B — 9 editorial items | Mixed class | Individually classified below: |

Appendix B item classification:

| Appendix B item | Class | Authority tier | Blocks |
|---|---|---|---|
| Baralta direct communion | A (new NPC mechanic) | Jordan (N+Ω) | NPC analysis §6, Baralta AI |
| Two witness traditions | D (content/lore) | Jordan | worldbuilding_v30 §3.7 |
| Ficinian Cardinal emanation | D (content/lore) | Jordan | §3.2 Church self-understanding |
| Miraculous Event trigger | B (system extension) | Jordan (N) | Southernmost engagement |
| Miracle Investigation action | B (system extension) | Jordan (N) | Church Southernmost response |
| SA-gated faction actions | C (parameter thresholds) | Jordan | All faction engagement |
| Miraculous Event → Accord +1 | C (parameter) | Jordan | Settlement-scale effects |
| Miraculous Event → Proximity −1 | C (parameter) | Jordan | Territory-scale MS interaction |
| Conviction mechanic for Miraculous Event | B (system extension) | Jordan (N) | Personal-scale effects |

**Three Class B items need N-tier decisions.** These are substantial — Miraculous Event trigger, Miracle Investigation, and Conviction mechanic for Miraculous Event all introduce new mechanical systems. They cannot be quietly absorbed; they need full N→Ω→Μ→М→Τ→Q vetting if accepted.

---

## §4 V · VALIDATION

### V1 · PP-666 trio via Sim Session 2

| PROVISIONAL spec | Class | Framework alignment | Sim verifies |
|---|---|---|---|
| `settlement_adjacency_v30.md` (ED-710 P2) | A | Μ-α + Μ-δ · М-2 primary · T-04, T-07, T-15 | Invasion routing through adjacency edges; Strain propagation |
| `fractional_province_ownership_v30.md` (ED-711 P2) | A | Μ-γ · М-4 + М-6 · T-15, T-07 | Seat/non-Seat split; three viable approaches (Q-robust); PV fractionalization preserves Μ-δ |
| `faction_succession_split_v30.md` (ED-712) | A | Μ-β + Μ-α · М-4 + М-6 · T-08, T-09, T-11, T-23 | Leader-loss contest; narrow-margin split; Baralta Crown Claim subsumption |

**V1 build scope** (per `session_checkpoint.md`):

1. Territory T1-T15 (locks М-2; **requires PP-652 PT values from F2.8**)
2. Domain Action framework (Μ-δ apparatus; **source: `stats_1_7_scale.md §DA Table` + `faction_politics_v30.md §2`**)
3. Piety Yield + CI political bonus (T-05, T-08; **source: `ci_political_v30.md §1`**)
4. Peninsular Strain propagation (T-07)
5. Mass combat + Contest system (Μ-α)
6. Faction AI stub (Μ-β minimal)
7. 40-season smoke test (full Μ-α/β/γ/δ)
8. **MS budget integration** — all drain/recovery sources from `references/ms_budget.md` (canonical ED-668) must be in the sim's accounting phase. v1 omitted this.

**V1 exit criteria:** Three specs promoted to CANONICAL *or* fail-flagged with redesign path classified:
- Class C redesign (parameter adjustment) → handled inline, stays in V1.
- Class B redesign (extension) → new PP entry with `vetting:` block, re-enters A· pipeline.
- Class A redesign (new system) → full vetting, Jordan-authority.

Verification ledger grows to ~200+ entries.

### V2 · Sim Session 3 — full-stack throughline coverage

| Module | T's verified | Μ served | Prerequisites |
|---|---|---|---|
| Threadwork (Tension/Coherence/Leap/Weaving) | T-01, T-03, T-12, T-28, T-31, T-33 | Μ-γ + Μ-β | **F2.7 threadwork P0 triage** — ~23 open P0 blockers directly affect threadwork sim implementation. Must triage before V2. |
| Victory (8 factions + Peninsular Sovereignty) | T-09, T-08, T-20 | Μ-α + Μ-δ | **A3.1** Varfell paths rewritten + **F2.5** Intelligence stat resolution |
| Scale transitions | T-15, T-23, T-25, T-26 | Μ-δ | — |
| NPC priority trees (7 NPCs) | T-23, T-25, T-17 | Μ-β | **A4.1** T-A + **A4.3** T-C (Certainty/Conviction connected to NPC trees) |
| Royal Assassination fuse | T-11, T-23, T-24 | Μ-α + Μ-β | — |
| Tensions Deck | T-22, T-24 | Μ-α + Μ-β | — |
| Deterministic regression (sim_var_01–06) | All | All | **A1.2** D-4 timeline locked |

**V2 exit criteria:** Every T (1–41 + 15a/b/c, minus T-10 STRUCK) has at least one mechanically-verified instantiation. Sim becomes Godot parity oracle.

### V3 · Godot Phase 6 parity

| Gap | Touches | Prerequisites |
|---|---|---|
| GAP-T-01 ThreadworkSystem co-movement | T-03 (Μ-γ + Μ-δ) | F2.7 P0 triage; Meta mock |
| GAP-T-02 `check_victory` unit tests | T-20 (М-6) | Full faction/territory state mock |
| GAP-T-03 ValoriaFactionAI decision tree coverage | T-08–T-15a/b/c (М-4), T-23 (М-5) | Branch coverage tests |
| GAP-T-04 NarrativeContainer routing | T-02 (Μ-γ) | **F1.1** (A-02 wired) — V3 cannot complete without F1.1 |

**V3 exit criteria:** All P0–P11 phase tests green. Sim parity on identical seeds.

---

## §5 P · PLAYABILITY — First Playable Season Loop

**New section (absent from v1).**

**Purpose:** Verify experiential correctness. Mechanical correctness (V1-V3) confirms the numbers are right. Playability confirms the experience works: can a designer read the game-state and answer "whose position is at risk, what each actor wants, what happens if no one acts"? This is Q-robust's dramatic legibility test, which requires a human and a screen.

**Scope — one season, minimal viable path:**

1. SeasonSlate displays 2–3 scene options (Layer 2 — SituationGenerator)
2. Player enters one Combat scene (Layer 3 — CombatContainer with real data)
3. CascadeDisplay shows consequences (Layer 4 — reads Meta visual queue)
4. RS + CI + PI clocks advance visibly (Layer 1 — PersistentUI HUD)
5. One NPC arc condition evaluated (Μ-β fires visibly)
6. One Domain Echo propagated (Μ-δ fires visibly)

**Requires (minimum):**
- F1.1 + F1.2 (Μ-β and Μ-δ operational)
- V3 GAP-T-04 closed (NarrativeContainer wired)
- `scenes/ui/persistent/` — RS+WC HUD (one scene file)
- `scenes/containers/combat/CombatContainer.tscn` — minimal scene (one scene file)
- `scenes/director/GameDirector.tscn` — orchestration scene
- One character `.tres` + one weapon `.tres` (from C1 weapon extraction)

**Does NOT require:**
- Full UI (C2)
- Full resource content (C1)
- Save system (C3)
- Board/Battle/Debate containers

**Exit criteria:** A designer plays one season and answers the three dramatic-legibility questions correctly from the screen.

---

## §6 C · CONSTRUCTION

### C1 · Resource content — classified by V-dependency

**V-independent (safe to start during Sprint 2 stall or parallel with V1):**

| Directory | Source | Class |
|---|---|---|
| `weapons/` | `params/combat.md` (canonical, stable) | D |
| `armour/` | `params/combat.md` | D |
| `factions/` (extraction from ValoriaDataLibrary.gd) | Already-shipped data → `.tres` Resources | D (after F1.4 Church stats fix) |
| `characters/templates/` | OfficerGenerator templates | D |

**V1-dependent (wait for Sim S2 value lock):**

| Directory | Source | Class |
|---|---|---|
| `territories/` | 17 instances — SW/PV/Proximity/Accord/POI from `settlement_layer_v30` + `geography_v30` | D |
| `action_cards/` | DA Table from `stats_1_7_scale.md` + `faction_politics_v30.md` | D |
| `tables/` | TC milestones, MS thresholds, Strain modifiers | D |

**V2-dependent (wait for Sim S3):**

| Directory | Source | Class |
|---|---|---|
| `co_movement_cards/` | `threadwork_v30.md §6` — deferred per design_sync | D |
| `triggers/` | Full Phase 8 catalogue (trigger_catalogue.md currently empty — content must be authored, not extracted) | D |
| `characters/named/` | Additional NPCs beyond 24 primary/extended | D |

### C2 · UI scenes (Godot-editor, out-of-band)

Prioritized by P (Playability) milestone dependency:

| Priority | Scene | Throughline |
|---|---|---|
| **P-required** | `ui/persistent/` RS+WC HUD | T-04, T-20 — equal UI real estate per `wc_survival_spine.md` |
| **P-required** | `director/GameDirector.tscn` | Layer 2/3/4 orchestration |
| **P-required** | `containers/combat/CombatContainer.tscn` | Layer 3 minimal |
| Post-P | `ui/season_overview/` SeasonSlate | Layer 2 |
| Post-P | `ui/cascade/` CascadeDisplay | Layer 4 |
| Post-P | `ui/board_ui/`, `combat_ui/`, `debate_ui/`, `thread_ui/`, `victory/`, `menus/` | Per-container |
| Post-P | `transitions/` ZoomManager | Μ-δ scale-transition animation |

### C3 · Save system hardening

| ID | Item | Framework tier | Notes |
|---|---|---|---|
| **C3.1** DA-01 save/load order | **Evaluate severity** — if current code corrupts state on load, this is F1-level, not C3. Test first: does save→load→continue produce different game state than continuous play? If yes → promote to F1. | All persistence |
| **C3.2** DA-02 `card_hand` → `CardHandState` | Μ-α apparatus | Card state lost on save; Domain Action card economy breaks across sessions |
| **C3.3** DA-03 `NarrativeState.deserialize()` | **Μ-β violation across save boundaries.** NPC trajectories reset on load. Autonomous-agent state non-persistent. Same class of violation as F1.1 but scoped to save/load rather than runtime. | NPC arc persistence |

### C4 · Q-elegance audit (new, absent from v1)

**After V2, before full C2 commitment.** Audit the verified mechanical stack against Q-elegant criteria:

- Core rule restatable after one reading?
- Second-order consequence predictable without additional rule-reading?
- External dependencies enumerated; "except when X" flagged and justified?

This prevents committing UI effort to mechanics that fail elegance. Redesign cost pre-UI is ~1 session; post-UI is ~3+ sessions.

---

## §7 M · MAINTENANCE

Run parallel to all streams. Never blocks vision-tier work.

| ID | Item | Volume | Notes |
|---|---|---|---|
| M.1 | RS-in-tests disambiguation (~1,340 instances) | High | Needs classifier: RS = Mending Stability vs Rhetorical Style. **Pre-V2 check:** verify sim files are RS-clean before V2 starts. |
| M.2 | TD disambiguation | Low | Mostly Mermaid syntax false positives |
| M.3 | `campaign_sim_npc_pcs_2026-04-18.py` Maret rename | Single file | Fabrication-check blocked |
| M.4 | TC in `deprecated/` | Low | Defer indefinitely |
| M.5 | `compliance_check.py` deployment | Infra | Move from pre-Phase 0 → Phase 0 orchestrator compliance |
| M.6 | `doc_index_gen.py` regen | Mechanical | Stale post-renames; sequence with F2.10 |
| M.7 | Add `RS = Rhetorical Style` to alias_registry if canonical | Pending term confirmation | |
| M.8 | Patch register provisional/unknown sweep | 156 entries | Sequence with F2.9 (policy must exist first) |

---

## §8 Dependency Graph

```
F0 (Data reconciliation)
  ↓ enables
F1 (Engine integrity) ─────────────────→ V3 (Godot Phase 6 parity)
F2 (Canon hardening) ─┐                    ↑
  F2.5 (Intelligence) ─→ A3.1 (Varfell)    │
  F2.7 (TW P0 triage) ─→ V2 (Sim S3 TW) ──┘
  F2.8 (PP-652 PT) ────→ V1 (Sim S2)
                           │
A1.1 D-5 ─────────────────→ V1
A1.2 D-4 ──────────────────→ V2 (deterministic seeds)
A3.1 (Varfell) ─────────────→ V2 (8-faction victory)
A4.1 T-A + A4.3 T-C ────────→ V2 (NPC priority trees)

V1 ──→ V2 ──→ V3 ──→ P (First Playable) ──→ C4 (Q-elegance) ──→ C2 (full UI)

C1.V-independent ── runs parallel from Sprint 1 onward (after F1.4)
C1.V1-dependent ─── runs after V1
C1.V2-dependent ─── runs after V2

F2, M· ── run parallel throughout
```

**Key v1 corrections:**
- F1 does NOT block V1/V2 (sim-independent). F1 blocks V3 only.
- A2 does NOT block V1/V2 (sim works without design-layer docs). A2 constrains confidence.
- F2.5 feeds A3.1 (diagonal dependency surfaced).
- F2.7 feeds V2 threadwork module (28 P0 blockers).
- P milestone inserted between V3 and C2.
- C1 items split by V-dependency for parallel execution.

---

## §9 Sprint Sequencing

### Sprint 1 — Foundation (1–2 sessions, Claude-executable)

| Order | Items | Repo |
|---|---|---|
| 1 | **F0.1** Status reconciliation | both |
| 2 | **F1.6** Run Godot tests; record results | valoria-game |
| 3 | **F1.3** Strip GameMode enum + collapse mode-branched constants | valoria-game |
| 4 | **F1.4** Fix Church stats | valoria-game |
| 5 | **F1.5** Verify 4 provisional values | valoria-game |
| 6 | **F2.1** ED-543 P1 verification | ttrpg |
| 7 | **F2.2–F2.5** ED-745–748 verification (F2.5 result feeds Sprint 2) | ttrpg |
| 8 | **F2.10** Register regen | ttrpg |
| 9 | **C1.V-independent start:** extract weapons/armour from params/combat.md | valoria-game |
| 10 | Commit: `[infrastructure]` to valoria-game; `[editorial]` to ttrpg | both |

### Sprint 2 — Authority unlocks (Jordan-blocking)

| Order | Items |
|---|---|
| 1 | **A1.1** D-5 Einhir site-network decision |
| 2 | **A1.2** D-4 Altonian timeline |
| 3 | **A1.3** Ministry NPC doc |
| 4 | **A2.1–A2.3** Three design-doc blocker resolutions |
| 5 | **A3.1** Varfell victory paths (gated on F2.5 from Sprint 1) |
| 6 | **A4.1–A4.6** Solmund throughlines: T-NN assignment + Appendix B triage |
| 7 | **F2.6** ED-768 orphaned PROVISIONAL triage (Jordan-review) |

**Sprint 2 stall path (new, absent from v1):**

If authority decisions are delayed, Claude executes:

| Item | Why safe |
|---|---|
| **F1.1** Wire NPCTrajectoryEvaluator | Godot-only; no design decision required |
| **F1.2** Forward deferred consequences | Godot-only |
| **F2.7** Threadwork P0 triage (classify resolved vs open) | Triage is classification, not decision |
| **F2.8** PP-652 PT values — locate canonical source, present to Jordan | Preparation, not resolution |
| **F2.9** Draft patch sweep policy | Draft, not adoption |
| **F2.11** hybrid_gaps propagation assessment | Triage |
| **F2.12** arc_register ED-401–405 classification | Triage |
| **C1.V-independent:** faction Resource extraction (post-F1.4) | Mechanical reshaping of shipped data |
| **M.1–M.8** Maintenance items | Always parallel |

### Sprint 3 — Sim S2 (1–2 sessions)

| Order | Items |
|---|---|
| 1 | **V1** full build per §4 scope |
| 2 | **F2.9** Adopt provisional patch sweep policy |
| 3 | **C1.V1-dependent:** territory instances, action_cards, tables | 

### Sprint 4 — Sim S3 (1 session)

| Prerequisite | Check |
|---|---|
| F2.7 P0 triage done? | Unresolved threadwork P0s block threadwork module |
| A3.1 done? | Victory module needs rewritten Varfell paths |
| A4.1 + A4.3 done? | NPC module needs T-A/T-C |
| A1.2 done? | Deterministic seeds need locked timeline |

**V2** full build per §4 scope.

### Sprint 5 — Godot Phase 6 (2–3 sessions)

| Prerequisite | Check |
|---|---|
| F1.1 + F1.2 done? | Must be — V3 GAP-T-04 depends on A-02 wired |

**V3** all gaps closed. Sim parity verified.

### Sprint 6 — First Playable (1 session, Godot-editor)

**P** milestone per §5.

### Sprint 7 — Q-Elegance Audit (1 session)

**C4** audit per §6. Results may trigger Class C/B redesign → re-enters pipeline.

### Sprint 8+ — Full Construction

**C1.V2-dependent** + **C2 post-P** + **C3** + remaining **M·**.

---

## §10 Vetting Posture

For new Class A/B items generated during execution:

```yaml
vetting:
  class: A | B
  necessity: pass | fail | flagged
  omega: pass | fail | flagged
  mu: [Μ-α | Μ-β | Μ-γ | Μ-δ]
  m_ratings: { M-1..M-11: + | ✓ | − | ○ }
  q: pass | iterate | skip
```

For F1.1/F1.2 restoration fixes:

```yaml
vetting:
  class: B
  restoration: true  # wiring existing intended functionality
  necessity: pass  # autonomous agents + cross-scale consequences model real political dynamics
  omega: pass  # restores Ω-b (transformation), Ω-c (autonomous world), Ω-a (cross-scale)
  mu: [Μ-β, Μ-δ]
  m_ratings: { M-1: ○, M-2: ○, M-3: ○, M-4: ✓, M-5: +, M-6: ○, M-7: ○, M-8: ○, M-9: ○, M-10: ○, M-11: ○ }
  q: pass
```

Pre-existing items: `pre-framework: true`. Class C/D/E: minimal `{ class: C }`.

---

## §11 Risk Register

| Risk | Severity | Mitigation |
|---|---|---|
| Sprint 2 stalls for weeks | High | Stall path defined (§9). F1.1/F1.2, F2.7, C1.V-independent, M· all executable. |
| V1 spec fails smoke-test (PP-666 trio) | Medium | Fail-path protocol: Class C stays in V1; Class B/A re-enters A· with PP + vetting. |
| 23 threadwork P0 blockers remain open at V2 start | High | F2.7 triage mandatory before V2. Jordan-decisions queued with A· items in Sprint 2. |
| F2.5 confirms Intelligence STRUCK → A3.1 Path A gate invalid | Medium | Expected outcome. Path A re-gate becomes authority decision (A3.1). |
| conversion_ledger / design_sync never reconciled | High | F0.1 is Sprint 1 item #1. |
| DA-01 corrupts save state (not just cosmetic) | Medium | C3.1 includes severity test. If corrupting → promote to F1. |
| Q-elegance audit reveals redesign needs post-V2 | Medium | Scheduled before C2 (Sprint 7). Redesign cost pre-UI is ~1 session; post-UI is ~3+. |
| No playable moment until Sprint 6 | Accepted | P milestone scoped minimal (one season, one combat). Infrastructure-first is correct for project maturity. |

---

## §12 What Full Execution Achieves

### Elegance

The sim-as-oracle architecture produces a single verified mechanical specification. One source (Python sim), one target (Godot), one authority direction. A designer reads the sim's output and intuits what the game will feel like. The C4 Q-elegance audit (Sprint 7) tests whether the *game mechanics themselves* are elegant — "core rule restatable after one reading" — not just the infrastructure.

### Smoothness

Cross-repo pipeline: ttrpg design → Python sim → Godot implementation. Authority flows one direction. Discrepancies caught at defined gates. No mechanic requires reading both repos simultaneously. The P milestone verifies experiential smoothness: does the season loop transition cleanly between Layer 2 (SituationGenerator) → Layer 3 (Container) → Layer 4 (CascadeDisplay) → Layer 1 (clock advancement)?

The dependency graph eliminates the v1 false-dependencies that would have created artificial serialization (F1 doesn't block V1; A2 doesn't block V1; C1 items split by actual V-dependency). Work parallelizes where the framework permits.

### Robustness

The vetting framework filters every new Class A/B proposal through N→Ω→Μ→М→Τ→Q. The Sprint 2 stall path prevents dead time. The V1 fail-path protocol handles discovery risk. The 28 threadwork P0 blockers are triaged before they can silently corrupt V2.

The F1.1 and F1.2 fixes restore the two Μ modes the game's identity depends on: autonomous agents (Μ-β — "the world doesn't wait") and cross-scale consequence (Μ-δ — "my choice here changed something there"). Without these, the engine actively undermines the player's sense of impact and the world's sense of life.

After full execution: every T (1–41 + 15a/b/c) has a mechanically-verified instantiation, every PROVISIONAL is promoted or archived, every source-of-truth document agrees with every other, and one human has played one season and confirmed that the framework's promises are legible on screen.
