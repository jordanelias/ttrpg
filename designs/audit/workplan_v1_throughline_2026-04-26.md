# Valoria Workplan — Throughline-Organized
**Generated:** 2026-04-26 · session token `8ca3fffeaca3bb9c`
**Framework:** PP-672 / PP-674 hierarchy — N (Necessity) → Ω (Intent) → Μ (Modes) → М (Meta-throughlines, 11) → Τ (Throughlines, 41+) → Q (Quality) → Μ̄ (Mechanics).
**Authority per §10:** Jordan owns N, Ω, Μ. Co-owned М, Τ. Claude applies Q + protocol.
**Grandfathering:** All items pre-PP-672 are grandfathered for vetting (`pre-framework: true`); structural alignment is still tracked for ordering work.

---

## How This Is Organized

Items are grouped by **what role they play in the framework's vision-stack**, not by severity.

| Bucket | Role | Protocol |
|---|---|---|
| **F · Foundation** | Currently broken or unverified — the framework's ability to serve Μ is impaired | Fix before downstream vetting is meaningful |
| **A · Authority unlocks** | N/Ω-tier decisions only Jordan can make; downstream specs cannot finalize without them | Block → escalate; do not autonomously proceed |
| **V · Validation** | PROVISIONAL specs awaiting smoke-test promotion to canonical | Sim is the oracle; outcome determines promotion-or-redesign |
| **C · Construction** | Class D content + Μ̄ implementation | Execute once preceding canon stable |
| **M · Maintenance** | Class E cleanup; cross-cutting hygiene | Run in parallel; never blocking |

Cross-stream dependencies are explicit at the end.

---

## F · FOUNDATION — Engine & Canon Integrity

### F1 · Engine substrate integrity (Godot — currently violating Μ)

Three shipped bugs in `valoria-game` constitute *active framework violations*. They are not "audit findings" but Μ-mode failures: the engine cannot serve the Μ mode it claims to serve.

| Item | Class | Failure | Tier | Fix |
|---|---|---|---|---|
| **A-02 NPCTrajectoryEvaluator wired** | E (architectural) | **Μ-β VIOLATION (Authored emergence — failure lexicon).** `SituationGenerator._evaluate_npc_trajectories` is a stub that never calls `NPCTrajectoryEvaluator.evaluate_all()`. NPC arcs are completely disconnected from the season loop. The autonomous-agent layer that **М-β** depends on is dark. T-23 (NPC Arc Emergence), T-25 (Generational Arc), T-15 (Player Progression) all silently fail. | Highest engine priority | Wire evaluator. Verify per-faction priority trees fire. |
| **B-07 deferred consequence pipeline** | E | **Μ-δ VIOLATION (Scale break).** Deferred consequences from VersusResolution `TrackerBindings` are never emitted. Domain Echoes, Belief evaluations, and NPC trigger consequences silently vanish on every roll. T-23 (NPC Arc Emergence), T-21 (Thread Political Warfare), T-22 (Belief Lattice) cannot mechanically fire cross-scale. | Highest engine priority | Forward `EngineResult.deferred_consequences` through `_on_versus_resolved` to `ConflictContainer` |
| **Church faction stats wrong in `ValoriaDataLibrary.gd`** | C (parameter) | **Μ-γ drift (Reskinned attractor risk).** Man=5 Wea=5 shipped; canonical is Man=4 Wea=3. T-08 (Church Rendering Reinforcement) — Church's substrate-posture is encoded in stats. Wrong numbers = wrong attractor behavior in any sim/run-through using the library. | Sequence with F2 | Correct values. Audit any sim runs since 2026-04-18 for inheritance. |

**Stream exit criteria:** Engine serves Μ-β and Μ-δ as designed. Faction stat library matches canonical source-of-truth.

### F2 · Editorial canon hardening

Eight items — close the open P1, verify the four active PROVISIONALs, regen stale infrastructure.

| Item | Class | Severity | Touches | Action |
|---|---|---|---|---|
| **ED-543** Clock registry refresh verification | E | **P1** (only active P1) | T-04, T-05, T-06, T-07 (all clock throughlines = М-1 Pressure-is-continuous) | Determine if registry refresh actually landed under another ED. If yes → close. If no → execute. |
| **ED-745** IP=20 start verification | E | P3 | T-06 (IP/Altonian, М-1) | Cross-check `peninsular_strain §4` against `params/bg/core` starting values |
| **ED-746** Intel Advancement Counter STRUCK verification | E | P3 | T-09 (Varfell), T-30 (Information asymmetry, М-8) | Confirm fieldwork VTM system fully replaces. Audit active specs. |
| **ED-747** Popular Will (PW) STRUCK verification | E | P3 | T-15c (RM substrate-heritage, М-4) | Verify against RM founding mechanics in current specs |
| **ED-748** Intelligence stat STRUCK verification | E | P3 | T-09 (Varfell, М-4) | Audit if any active spec still references Intelligence as a faction stat |
| **ED-768** 13 orphaned PROVISIONAL markers triage | E | P3 | Cross-cutting | Jordan-review classification: still-open vs resolved-but-unarchived. Pre-PP-672, grandfathered for vetting; resolution still required for register hygiene. |
| **`editorial_ledger_summary.yaml` regen** | E | Infra | — | Summary (auto-gen 2026-04-23) claims 12 active; actual is 6. Stale references to ED-660/661/662/664/665/669/704/705 (resolved per "Last touched 2026-04-25" trail). Regen via doc_index_gen.py. |
| **`patch_register_index.md` regen + provisional sweep policy** | E | Infra | — | Define promotion-or-archive policy for the 65 provisional + 30 unknown + 61 proposed. Most are grandfathered (`pre-framework: true`); promotion policy is the missing decision. |

**Stream exit criteria:** P1-BLOCKER count = 0 *and* zero unverified PROVISIONALs in active ledger *and* register summaries reconcile to actual state.

---

## A · AUTHORITY UNLOCKS — Jordan-decision blockers

These all flag as **N or Ω failure-flagged** until you decide. Do not autonomously resolve. Each is sequenced by what downstream stream it unblocks.

### A1 · Tier N + Ω specifications (load-bearing for vision)

| Item | Tier | Touches | What's needed | Blocks |
|---|---|---|---|---|
| **D-5 Einhir site-network model** (ED-726) | **N + Ω-b** | T-15c (RM substrate-heritage, М-4 institutional), T-04 (Mending sites, М-3 substrate), М-2 (Geography holds pressure) | New mechanical layer? Or reskin of existing Mending site? **N-question:** what Renaissance/historical analogue does "site network" model? **Ω-b:** how does engagement transform the player? | Sim S2 (V1), RM faction full spec, threadwork substrate finalization |
| **D-4 Altonian invasion ~18 AG timeline** (ED-725) | Ω-c | T-06 (IP/Altonian, М-1), T-04 (RS decay history) | Timeline lock: pre/post-invasion campaign starting state | All sims; deterministic test corpus (Sim S3) |
| **Ministry NPC design doc** | Ω-c | T-08 (Church rendering reinforcement, М-4), T-14 (Conviction Architecture, М-6) | Locate or commission. Open since 2026-04-20. | Church faction full spec; npc_behavior_v30 §2 completeness |

### A2 · Three blocked v30 design-doc renames

Each blocker raises the same Ω-question: accept the unverified compilation/stage source as canon, or commission a design-layer doc?

| Item | Mode | Touches | What unverified source claims | What's at risk |
|---|---|---|---|---|
| **factions_ttrpg blocker** (ED-048-adjacent) | TTRPG | T-08, T-09, T-11 (institutional throughlines, М-4), T-15a/b/c (Hafenmark/Löwenritter/RM postures) | `compilation/v0.14/stage6_factions` — TTRPG-faction mechanics | All institutional throughlines for personal-scale play |
| **campaign_modes blocker** | ALL | Ω-d (non-dominance) lives here; cross-cuts all M's | `compilation/v0.14/stage12_campaign_modes` | Defines the unified videogame mode (post-2026-04-17 collapse). Currently inheriting from unverified source. |
| **southernmost blocker** (ED-048 since 2026-04-04) | TTRPG | T-19 (Southernmost Hidden Front, М-2), T-04 (RS decay) | `compilation/v0.14/stage4_southernmost` | Survival contest's load-bearing geography spec |

### A3 · STRUCK-system follow-up

| Item | Class | Touches | Action | Status |
|---|---|---|---|---|
| **Varfell victory paths editorial rewrite** (post VTM-strike) | B (extension) | T-09 (Varfell Thread Progressive, М-4), T-20 (Two Contests, М-6) | Path A re-gated to Intelligence ≥4. Path B WR ≥3 raised. Path C dissolved. PP-664 closed residual cleanup but **the Varfell victory-path rewrite itself is "Pending editorial rewrite" per `canonical_sources.yaml`** — no PP yet. | Open since 2026-04-19 |

### A4 · Solmund throughlines appendix integration (canonical T-NN assignment)

| Item | Class | Tier | Action |
|---|---|---|---|
| **T-A through T-E PROVISIONAL throughlines** (Solmund appendix) | A or B | Τ-tier | Five throughlines (Perceptual Prophylaxis as Literary Engine; Seam Texts as Mechanical Objects; Double Consciousness Spiral; Baralta as Accidental Prophylaxis Cracker; Solmund Repetition) need canonical T-NN numbers + parent-Μ̄ assignment. Co-owned per §10. **Plus 9 open editorial items in Appendix B** (Baralta direct communion, two witness traditions, Ficinian Cardinal emanation, Miraculous Event trigger, Miracle Investigation action, SA-gated faction actions, Miraculous Event Accord/Proximity effects, Conviction mechanic for Miraculous Event). |

---

## V · VALIDATION — PROVISIONAL specs via simulation oracle

### V1 · PP-666 trio smoke-test (Sim Session 2)

The Sim S2 build IS the validation that promotes ED-710/711/712 from PROVISIONAL to CANONICAL.

| PROVISIONAL spec | Class | Tier alignment | What the sim verifies |
|---|---|---|---|
| **`settlement_adjacency_v30.md`** (ED-710 P2) | A (new system) | Μ-α (pressure routing) + Μ-δ (settlement→province cross-scale) · М-2 primary, М-5 secondary · T-04, T-07, T-15 | Inter-settlement edges (road/river/mountain/coastal) actually route invasion as designed. Strain propagates through adjacency graph. |
| **`fractional_province_ownership_v30.md`** (ED-711 P2) | A | Μ-γ (substrate-grounded ownership state) · М-4 + М-6 · T-15, T-07 | Seat/non-Seat split with 75% Consolidation threshold produces three viable approaches (Q-robust). PV fractionalization preserves Μ-δ scale-coupling. |
| **`faction_succession_split_v30.md`** (ED-712) | A | Μ-β (autonomous succession events) + Μ-α (forced contest pressure) · М-4 + М-6 · T-08, T-09, T-11, T-23 | Generalized leader-loss contest fires across all factions. Narrow-margin split actually fractures faction. Baralta Crown Claim subsumes correctly as Crown-special. |

**Sim S2 build scope** (per `canon/session_checkpoint.md` next_bootstrap_actions):

1. Territory T1-T15 model (verifies ED-710 + locks Μ-2 geography)
2. Domain Action framework (Μ-δ cross-scale apparatus)
3. Piety Yield + CI political bonus (T-05, T-08 verification)
4. Turmoil propagation (T-07)
5. Mass combat + Contest system (Μ-α resolution machinery)
6. Faction AI stub (Μ-β minimal — promote via priority trees in Sim S3)
7. 40-season smoke test (full Μ-α/β/γ/δ stack)

**V1 exit criteria:** All three specs land CANONICAL or fail-flagged with redesign requirements. Verification ledger grows ~200+ entries.

### V2 · Sim Session 3 — full-stack throughline coverage

The throughlines whose mechanics the videogame must implement get verified here. This is where T-coverage becomes systematic rather than spot-checked.

| Sim S3 module | T's verified | Μ served |
|---|---|---|
| Threadwork (Tension/Coherence/Leap/Weaving) | T-01, T-03, T-12, T-28, T-31, T-33 | Μ-γ + Μ-β |
| Victory conditions (8 factions + Peninsular Sovereignty) | T-09, T-08, T-20 | Μ-α + Μ-δ |
| Scale transitions (personal → faction → strategic) | T-15, T-23, T-25, T-26 | Μ-δ primary |
| NPC priority trees (7 named: Almud, Himlensendt, Baralta, Vaynard, Ehrenwall, Torben, Edeyja) | T-23, T-25, T-17 | Μ-β primary |
| Royal Assassination fuse | T-11, T-23, T-24 | Μ-α + Μ-β |
| Tensions Deck activations | T-22 (Belief Lattice), T-24 | Μ-α + Μ-β |
| Deterministic regression (sim_var_01–06) | All above | All Μ |

**V2 exit criteria:** Every Τ (1–41 + 15a/b/c) has at least one mechanically-verified instantiation. Sim becomes the parity oracle for Godot tests.

### V3 · Godot Phase 6 — sim parity gates

`tests/coverage_matrix.md` gaps map directly to Μ failures awaiting verification.

| Gap | Touches | Μ tier | Required |
|---|---|---|---|
| GAP-T-01 ThreadworkSystem co-movement | T-03 (Inseparability) | Μ-γ + Μ-δ | Meta mock; Phase 12-2 test |
| GAP-T-02 `check_victory` unit tests | T-20 (Two Contests, М-6) | Μ-α + Μ-δ | Full faction/territory state mock |
| GAP-T-03 ValoriaFactionAI per-framework decision tree coverage | T-08–T-15a/b/c (institutional, М-4), T-23 (М-5) | Μ-β | Branch coverage tests |
| GAP-T-04 NarrativeContainer investigation/evidence routing | T-02 (Rendering consciousness-performed) | Μ-γ | Wire `SituationGenerator → NPCTrajectoryEvaluator` (this is F1's A-02 — V3 cannot complete without F1) |

**V3 exit criteria:** All P0–P11 phase tests green. Sim parity tests pass on identical seeds against same inputs.

---

## C · CONSTRUCTION — Class D content + Μ̄ implementation

### C1 · Resource content (`valoria-game/resources/instances/`)

Currently `.gitkeep`-only directories. Each cluster maps to a throughline-set whose data must populate.

| Directory | Touches | Source | Class |
|---|---|---|---|
| `weapons/`, `armour/` | T-01 (substrate state at personal scale) | `params/combat.md` | D |
| `action_cards/` | Μ-δ apparatus | Domain Action Table from `stats_1_7_scale.md` + `faction_politics_v30.md` | D |
| `co_movement_cards/` | T-03 (Inseparability) | `params/threadwork.md` + `threadwork_v30.md §6` Co-Movement | D (deferred per design_sync) |
| `factions/` | T-08, T-09, T-11, T-15a/b/c (М-4) | Currently in `ValoriaDataLibrary.gd` — extract | D |
| `territories/` | T-04, T-07, T-19 (М-2) | 17 instances with SW/PV/Proximity/Accord/POI from `geography_v30 §POI catalog` + `settlement_layer_v30` | D |
| `tables/` | Cross-cutting | TC milestones, RS thresholds, Strain accord modifiers | D |
| `characters/named/`, `characters/templates/` | T-23 (NPC Arc Emergence) | `npc_roster_v30` named + `OfficerGenerator` templates | D |
| `triggers/` | Μ-β autonomous fire conditions | Currently 15 `.tres`; full Phase 8 catalogue per `trigger_catalogue.md` (currently empty) | D |

### C2 · UI scenes (Μ̄ tier — implementation work)

100% empty `.gitkeep` in every UI directory. Out-of-band for GitHub-only orchestration; requires Godot editor sessions.

| Scene | Throughline | Notes |
|---|---|---|
| `ui/persistent/RS+WC HUD` | T-04 + Two Contests T-20 | **Required:** equal UI real estate for RS and WC per `wc_survival_spine.md`. The survival-contest's two axes must be visible on the main screen. |
| `ui/season_overview/` | Μ-β SeasonSlate display | Layer 2 visualization |
| `ui/cascade/` | Progression layer | Reads Meta visual queue |
| `ui/board_ui/`, `combat_ui/`, `debate_ui/`, `thread_ui/`, `victory/`, `menus/` | Per-container UI | All Μ̄-tier |
| `transitions/` | Μ-δ apparatus | ZoomManager animations between Board/Battle/Combat |

### C3 · Save system hardening

| Item | Touches | Action |
|---|---|---|
| **DA-01** save/load order enforcement | All persistence | Assert/document order in `save_game/load_game` |
| **DA-02** `card_hand` extraction to `CardHandState` | Μ-α apparatus | Currently lost on save — moves to separate Resource saved in `SaveData` |
| **DA-03** `NarrativeState.deserialize()` implementation | Μ-β autonomous-agent persistence | Currently stub — NPC trajectories reset on load. **М-β VIOLATION across save boundaries.** |

---

## M · MAINTENANCE — Class E cross-cutting cleanup

Run in parallel with everything else. Never blocks vision-tier work.

| Item | Volume | Touches |
|---|---|---|
| RS-in-tests disambiguation (~1,340 instances) | High volume, low severity | Needs classifier: RS = Mending Stability vs RS = Rhetorical Style. Add `RS = Rhetorical Style` to `alias_registry` if confirmed canonical. |
| TD disambiguation (Mermaid TD vs PP-166 Thread Depth) | Low | Mostly false-positive (Mermaid syntax) |
| `campaign_sim_npc_pcs_2026-04-18.py` Maret rename | Single file | Currently fabrication-check blocked |
| TC in `deprecated/` files | Low | Historical; defer indefinitely |
| `compliance_check.py` deployment (move ttrpg from pre-Phase 0 → Phase 0) | Infrastructure | Replace `valoria_hooks` manual assertions with auto-enforcement |
| `doc_index_gen.py` regen across stale indexes | Mechanical, large scope | Index files stale post-bulk-renames |
| Patch register provisional/unknown sweep | 156 of 164 entries | Promotion-or-archive policy from F2 |

---

## Cross-Stream Dependency Graph

```
F1 (Engine integrity)
   ↓ blocks
V3 (Godot Phase 6) — GAP-T-04 cannot complete without A-02 wired
   ↓ blocks (parity)
V2 (Sim S3 used as oracle) — sim and Godot must agree

A1.D5 (Einhir site-network)
   ↓ blocks
V1 (Sim S2) — substrate spec needed before threadwork-territory binding finalizes
   ↓ promotes
V1 PROVISIONAL trio → CANONICAL
   ↓ enables
V2 (Sim S3 full-stack)

A1.D4 (Altonian timeline)
   ↓ blocks
V2 (deterministic test corpus needs locked starting state)

A2 (3 design-doc blockers)
   ↓ blocks
V1 + V2 — TTRPG-faction layer mechanically present in sim only via unverified compilation source

A3 (Varfell editorial rewrite)
   ↓ blocks
V2 (8-faction victory verification)

A4 (Solmund T-A..T-E integration)
   ↓ blocks
V2 if any T-A..T-E touches Sim S3 modules

C1, C2, C3
   ↓ require
V1 + V2 complete (final mechanical values locked)

F2, M· run parallel to F1 + V1 + V2
```

---

## Recommended Sequencing

**Sprint 1 — Foundation parallel** (1–2 sessions)
1. **F1.A-02** wire NPCTrajectoryEvaluator (Μ-β restoration)
2. **F1.B-07** forward deferred consequences (Μ-δ restoration)
3. **F1.Church stats** correct in `ValoriaDataLibrary.gd`
4. **F2.ED-543** verify clock registry refresh status (close P1)
5. **F2.ED-745–748** verify the four PROVISIONALs against `canonical_definitive_r2`
6. Single-commit `[infrastructure]` to valoria-game; ledger reconciliation commit to ttrpg

**Sprint 2 — Authority unlocks** (Jordan-blocking)
7. **A1.D-5** Einhir site-network decision
8. **A1.D-4** Altonian invasion timeline decision
9. **A1.Ministry** NPC doc location/commissioning
10. **A2** ×3 — accept compilation/stage as canon OR commission design-layer docs
11. **A3** Varfell victory paths editorial rewrite
12. **A4** Solmund T-A..T-E throughlines: assign T-NN numbers + Μ-NN parents

**Sprint 3 — Validation via Sim S2** (1–2 sessions)
13. **V1** Sim Session 2 — promote PP-666 trio through smoke test
14. **F2.summary regen** + provisional patch sweep policy adoption

**Sprint 4 — Validation via Sim S3** (1 session)
15. **V2** Sim Session 3 — full-stack throughline coverage

**Sprint 5 — Godot Phase 6 parity** (2–3 sessions)
16. **V3** GAP-T-01 through GAP-T-04 closure

**Sprint 6+ — Construction parallel**
17. **C1** Resource content authoring (parallelizable)
18. **C2** UI scenes (Godot-editor sessions, out-of-band for orchestrator)
19. **C3** Save system hardening
20. **M·** runs throughout, never blocking

---

## Vetting Posture for New Work in This Workplan

For any new Class A/B item generated *during* execution of this workplan (e.g. a new mechanic discovered during Sim S2 to fill a gap), the PP entry must include the `vetting:` block per §8.5:

```yaml
vetting:
  class: A | B
  necessity: pass | fail | flagged
  omega: pass | fail | flagged
  mu: [Μ-α | Μ-β | Μ-γ | Μ-δ]
  m_ratings: { M-1..M-11: + | ✓ | − | ○ }
  q: pass | iterate | skip
```

Pre-existing items above are grandfathered (`pre-framework: true`).

Class C/D/E items use minimal `{ class: C }` (or D/E).

`valoria_hooks.vetting_gate` will block commits on Class A/B PP entries lacking the block from PP-674 forward.

---

## Failure Lexicon — Watchwords During Execution

These are the framework-level smell tests. Flag any item that triggers one and re-vet before proceeding:

| Flag | Means | Tier |
|---|---|---|
| Fantasy imposition | From game-design convention, not subject grounding | N |
| Duplicate coverage | Existing mechanic already models this | N |
| Edge case mechanic | Dynamic was rare historically | N |
| Abstractable | Existing abstract mechanics cover it | N |
| Rest state | Player can idle without consequence | Ω-c, Μ-α |
| Dominant strategy | Single approach beats others | Ω-d, М-6 |
| Flavor-only | Reads like Valoria but doesn't mechanically engage substrate | Ω, Μ-γ, М-3 |
| Scale break | Action at one scale produces no other-scale consequence | Μ-δ, М-5 |
| Reskinned attractor | Faction's substrate-posture indistinct from another | М-4 |
| Event without stakes | Mechanic fires; nothing changes | Q-robust |
| Special-cased | "Except when X" without justification | Q-smooth, Q-elegant |
| Cost-hidden | Tooltip shows gain, not cost | М-6 |
| Strategic-only | No personal-scale registration | Ω-b |
| Personal-only | No strategic-scale registration | Ω-a |
| Authored emergence | Player authors world-fact; not autonomous | Μ-β |

**B-07 was a "Scale break" hidden in pipeline. A-02 was an "Authored emergence" violation in pipeline. F1 fixes restore framework-fidelity; without them, every Sim S2/S3 result is suspect for the same reasons.**
