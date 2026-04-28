# Valoria Comprehensive Workplan v3 — Reconciled
**Generated:** 2026-04-27 · session token `8ca3fffeaca3bb9c`
**Status:** Reconciliation. Supersedes the three competing workplans named in §0.
**Target:** Godot 4.6 videogame.
**Scope:** Complete project completion plan from current state to first playable.

---

## §0 What This Document Supersedes

This workplan reconciles three previously-independent plans plus three rounds of audit findings:

| Source | Date | Status |
|---|---|---|
| `designs/audit/valoria_workplan_final.md` (92 KB) | 2026-04-18 | **Backbone.** Phase structure adopted verbatim. Pre-existing ~55-item content retained. |
| `designs/workplans/wave1_workplans.md` (25 KB) | undated, uncommitted | **Folded into Phase 5.** Five proposals (P1, P3, P9, P10, P21) become Phase 5 player-UX subsections. |
| `valoria_workplan_v2.md` (mine, /mnt/user-data/outputs) | 2026-04-26 | **Findings absorbed.** Engine bugs, missing CI, throughlines integration, governance gaps absorbed into Phase 0/1/5. |
| Round 1 review + Round 2 audit + Round 3 audit | 2026-04-26/27 | **All open items absorbed.** Items resolved against existing workplan_final coverage. |

**Authority:** Jordan owns N, Ω, Μ, M-tier vision decisions per `references/throughlines_meta.md` §10. Claude applies Q + protocol.

**Vetting framework:** PP-672/674 throughlines hierarchy is canonical. Class A/B PP entries from PP-674 forward require full `vetting:` blocks. Pre-PP-674 items use `pre-framework: true`.

**Canon compliance gate:** Before any Phase 1–3 design decision, read `canon/00_philosophical_foundations_rules.md`. Every mechanical change verified against P-01 through P-15+ principles. State principle and compliance rationale in commit message. **Principles do not bend** — if a resolution would violate, redesign the resolution.

---

## §1 Reading Guide

### Phase structure

| Phase | Purpose | Sessions | Gate |
|---|---|---|---|
| **0 Foundation** | Register truthfulness + governance + housekeeping | 1–2 | All registers reconcile; LICENSE+READMEs in; CI/freshness gates running |
| **1 P1 Blockers** | Design gaps that block implementation | 2–3 | All P1 items in editorial ledger resolved |
| **2 Calibration Inputs** | Simulation debt + parameter calibration | 3–5 | All P2 items resolved; ms_budget integrated |
| **3 Polish + Authority** | P3 cleanup + atoms_pending + STRUCK followups | 2–3 | All Authority decisions landed |
| **4 Full-Campaign Sim** | The verification oracle | 8–12 | **Calibration report passes 7-criterion gate** |
| **5 Godot Prep** | Engine fixes + parity tests + UX scaffolding | 4–6 | Sim parity confirmed; engine layers operational |
| **6 First Playable** | One season, end-to-end, human-tested | 2–3 | Q-robust dramatic legibility test passes |
| **7 Ongoing** | Maintenance protocol | permanent | — |

**Total: 22–34 sessions, plus content authoring (declared-deferred per §10).**

### 5-Lens Inconsistency Protocol (run at session start, every session)

Adopted verbatim from `valoria_workplan_final.md`:

| Lens | Catches | Tool |
|---|---|---|
| **Propagation Map** | Files changed without downstream propagation | `tools/broken_dependency_checker.py` |
| **Session Log** | `open_items` acknowledged but uncommitted | manual cross-check vs editorial_ledger |
| **Editorial Summary** | `p1_blocker_count` mismatch with active ledger | manual count check |
| **Coverage Matrix** | Items "Open — ED-NNN" not in active ledger | grep-and-cross-ref |
| **File Index** | `propagation-pending` count drift | `references/file_index_summary.md` |

**Sweep procedure:**
1. Bootstrap (registers loaded)
2. Compare editorial ledger open items ↔ coverage matrix open findings; flag mismatches
3. Compare session log `open_items` ↔ editorial ledger; flag items in one but not the other
4. Run `python3 tools/broken_dependency_checker.py`
5. Check file_index_summary.md `propagation-pending`; each is uncommitted downstream work
6. Check editorial_ledger_summary.yaml: if `p1_blocker_count` doesn't match active ledger, summary stale
7. **NEW:** Run `python3 tools/freshness_gate.py` — if stale canonical SHAs, halt before any sim/audit/patch work

### Standard Commit Protocol (every commit modifying a design doc)

1. Update `references/propagation_map.md` per Step A–D auto-update protocol
2. Update `references/canonical_sources.yaml` SHA for every modified file
3. Update `canon/editorial_ledger.yaml` for any resolved or newly raised ED items
4. Include `references/canonical_sources.yaml` for co-file compliance (enforced by `safe_commit`)
5. Run `h.safe_commit()` — the only valid commit path
6. **NEW:** After commit, run `python3 tools/freshness_gate.py --update`

---

## §2 Phase 0 — Foundation

**Estimated effort: 1–2 sessions. No design decisions required.**

### 2.1 Register truthfulness (NEW — supersedes workplan_final 0.1)

| ID | Item | Action |
|---|---|---|
| **0.1.1** | **Patch register applied_commit recovery** | 11 of 14 active patches show `applied_commit: pending`. Round 3 git-history verification confirms commits exist (PP-672 = 03da0601; PP-673 = f2f3efe8; PP-674 = 3fab28a6; PP-666 = c3de2eff; PP-665 = d7c5f200; etc.). For each pending entry: read commit log, populate actual SHA. **Register currently lies about commit state; this is the load-bearing data-integrity fix.** |
| **0.1.2** | Rebuild editorial_ledger_summary.yaml | Stale (auto-gen 2026-04-23). Claims 12 active; actual is 6. References resolved EDs (660-705). Regenerate with correct counts, IDs, next_id. Verify `p1_blocker_count` matches actual count. |
| **0.1.3** | Deduplicate ED-663 in active ledger | Two ED-663 entries exist — one open (gap-logged), one resolved. Archive the old. Scan for other duplicate IDs. |
| **0.1.4** | Update file_index_summary.md propagation-pending count | Currently 13 items listed. Some resolved without count update. |
| **0.1.5** | Run broken_dependency_checker against propagation_map | 3 known broken deps (deprecated compilations). Log new breaks. |
| **0.1.6** | Verify session_log open_items against editorial_ledger | ED-666/667/663 resolved this session per workplan_final notes; verify reflected. |

### 2.2 P0 triage and threadwork audit reconciliation

| ID | Item | Action |
|---|---|---|
| **0.2.1** | Triage P0 blockers ED-668–672 from editorial_summary | Read `tests/stress/thread/threadwork_audit_register.md`. For each ED-668–672: resolved (archive), still open (add to Phase 1 P0), reclassify (severity change with rationale). |
| **0.2.2** | Triage threadwork audit register (28 P0 + AUD-TW-001 P1s) | Per Round 3: ~5 P0s resolved by ms_budget/Niflhel-dissolution/etc. Remaining ~23 P0s + AUD-TW-001 P1s (POP paradox window, Rendering Crisis procedure) classified: resolved/open/Jordan-decision. |
| **0.2.3** | Cross-reference 27 unknown canonical IDs from atoms_pending audit | 8 EDs (ED-129/131/200/295/297/618/670/694), 18 PPs (PP-233/238/239/246/251/285/294/402/508/512+8), 1 TC (TC-01) referenced in atoms but not in canon. Cross-check archives/editorials/ and archives/patches/. Classify: stale / anticipatory / fabricated. |

### 2.3 Params staleness audit

| ID | Item | Action |
|---|---|---|
| **0.3.1** | Params freshness sweep | Compare each `params/*.md` against canonical source design doc per `canonical_sources.yaml`. Mark stale entries. Refresh values. Clear `KNOWN STALE SYNC GAPS` in file_index. |
| **0.3.2** | rs_budget → ms_budget rename propagation | ED-731 renamed file. Grep `rs_budget` references across docs. Update all. |
| **0.3.3** | Numeric bounds report regen | `references/numeric_bounds_report.yaml` flagged for regen "after next collator run." Run `tools/valoria_collator.py`. |
| **0.3.4** | Values master regen | Run `tools/extract_values.py` to refresh `references/values_master.yaml` against current design docs. |

### 2.4 Engine integrity (FROM v2 — post-2026-04-18 discoveries)

| ID | Item | Class | Failure | Action |
|---|---|---|---|---|
| **0.4.1** | Wire NPCTrajectoryEvaluator | B | Μ-β violation (Authored emergence) | `SituationGenerator._evaluate_npc_trajectories` is stub. Wire `NPCTrajectoryEvaluator.evaluate_all()`. **Restoration fix; vetting block carries `restoration: true`.** |
| **0.4.2** | Forward deferred consequences | B | Μ-δ violation (Scale break) | `EngineResult.deferred_consequences` from VersusResolution never forwarded through `_on_versus_resolved`. Forward to ConflictContainer. |
| **0.4.3** | Strip GameMode enum + runtime grep | E (cleanup; no mechanic touches) | Dead code post-videogame-only collapse | (a) `Enums.gd` L44 — remove `enum GameMode { TTRPG, HYBRID, BOARD }`. (b) `Constants.gd` — collapse 5 mode-branched constants to single videogame values. (c) **`Meta.gd` L9 — `var game_mode: int = Enums.GameMode.TTRPG` removed.** (d) Grep all `Meta.game_mode` references across 60 systems + 32 scenes; eliminate branches. |
| **0.4.4** | Disambiguate "A-02" tags | E | Naming collision: `Meta.gd` autoload-ordering "A-02" vs NPCTrajectoryEvaluator "A-02" (0.4.1) | Rename one. Suggest: AUTOLOAD-A-02 vs NPC-A-02. |
| **0.4.5** | Fix Church faction stats | C (parameter) | Μ-γ drift | `ValoriaDataLibrary.gd`: Man=5→4, Wea=5→3 per design_sync canonical. |
| **0.4.6** | Resolve 4 Open Provisional Values | C | Phase 0 placeholders | Verify `Constants.gd RS_BASELINE_DECAY=1`, `Meta.gd RS_initial=100`, `CombatLogic health=4`, `CombatLogic damage=placeholder` against canonical sources. Confirm or correct. |
| **0.4.7** | Run never-run Godot tests | E | `test_dice_engine.gd`, `test_tracker_registry.gd` — conversion_ledger says never run; coverage_matrix Phase 12 implies pass. Resolve contradiction. | Run in Godot. Fix failures. Record. |

### 2.5 CI / orchestration infrastructure (NEW)

| ID | Item | Action |
|---|---|---|
| **0.5.1** | Wire compliance_check at bootstrap | Tool exists at `tools/compliance_check.py` (21 KB, fully functional). Bootstrap reports "not found." `atomization_rules.yaml` says `compliance_check_on_bootstrap: true`. Investigate orchestrator path lookup. Fix integration so bootstrap runs `check_all()`. |
| **0.5.2** | Wire freshness_gate at bootstrap | `tools/freshness_gate.py` exists (10.8 KB) with spec at `docs/freshness_gate_spec.md` (4.4 KB). Spec status: "IMPLEMENTED — pending SHA population pass" since 2026-04-02. Run `python3 tools/freshness_gate.py --update` to populate SHAs. Add to bootstrap protocol per spec §3. |
| **0.5.3** | Author valoria-game CI workflow | `valoria-game/.github/workflows/godot-ci.yml`. Minimum: Godot headless test runner on push/PR. Eventually: GUT framework integration, scene-load smoke tests. ttrpg has 7-job CI; valoria-game has none. |
| **0.5.4** | Resolve coverage_matrix.md atomization violation | `tests/coverage_matrix.md` (19.7 KB) violates `atomization_rules.yaml max_tokens: 5000`. Either chunk or update rule. |

### 2.6 Status reconciliation (NEW)

| ID | Item | Action |
|---|---|---|
| **0.6.1** | Update `valoria-game/docs/conversion_ledger.md` | Phase 0 IN PROGRESS → COMPLETE. Phase 1 NOT STARTED → COMPLETE (per design_sync evidence). Phase 4/5/6 status to current truth. |
| **0.6.2** | Update `valoria-game/docs/design_sync.md` | `last_sync_date` to current. Reflect Phase 6 partial. |
| **0.6.3** | Conversion_ledger path renames | Apply post-restructure paths from design_sync.md §Conversion Ledger Path Updates. |

### 2.7 Governance (NEW)

| ID | Item | Action |
|---|---|---|
| **0.7.1** | Add LICENSE to both repos | Decide: proprietary all-rights-reserved / MIT / Apache 2.0 / CC BY-NC 4.0 (design + separate code license) / custom. Single 5-min decision; significant downstream consequence. |
| **0.7.2** | Author top-level `ttrpg/README.md` | What Valoria is; two-repo structure; project state pointer (link to this workplan); bootstrap process; key directories overview; license reference. |
| **0.7.3** | Rewrite `valoria-game/README.md` | Currently 5 lines, says "hybrid TTRPG/board game" (videogame-only since 2026-04-17). Add: Godot version (4.6), dependencies, build instructions when available, pointer to ttrpg design canon. |
| **0.7.4** | Declare-deferred governance items | CONTRIBUTING.md, CODE_OF_CONDUCT.md, .github/templates, branch protection rules, PAT rotation policy, playtest protocol. Each declared as known-deferred until First Playable (Phase 6). |

**Phase 0 exit criteria:**
- Patch register `applied_commit` truthful for all entries
- Editorial summary reconciles to actual ledger counts
- All 5 lenses produce zero contradictions
- All 4 engine integrity issues resolved (NPC eval wired, deferred consequences forwarded, GameMode stripped, Church stats fixed)
- compliance_check + freshness_gate running at bootstrap
- valoria-game has CI workflow
- LICENSE + READMEs in both repos
- conversion_ledger / design_sync / current state all agree

---

## §3 Phase 1 — P1 Blockers

**Estimated effort: 2–3 sessions. Requires design decisions.**

**Reference:** `designs/audit/valoria_workplan_final.md` §Phase 1 contains full body for 1.1–1.5. Items below mirror or extend.

### 3.1 P1 items from workplan_final (carried forward)

| ID | Item | Audit flag | Canon ref | Status |
|---|---|---|---|---|
| **1.1** | Knot Formation During Play | AUD-NPC-01 | P-12, P-15 | Solidarity Resonant Style requires Knot; videogame mode lacks formation procedure post-character-creation. Proposed: Disposition +5 + TS≥30 → Spirit/TN7/Ob2 scene. Affected: `npc_behavior_v30 §6.3`, `fieldwork_v30 §5.6`, `companion_specification_v30 §2.1`. |
| **1.2** | Accord Propagation to Settlement Order | AUD-SET-02 | P-03 | Settlement layer §1.3 changed Accord derivation: `Province Accord = floor(mean settlement Order)`. 15–25 individual rules across 7 docs need settlement targeting. |
| **1.3** | Derived Stats Numerical Calibration | AUD-DS-01 | — | All multipliers PROVISIONAL: Treasury×100, Legitimacy×20, Reputation×15, Discipline×10. Per-faction economic models needed. **Depends on 1.2.** |
| **1.4** | Faction Politics Simulation | AUD-FP-01 | — | Faction interaction scenarios need sim verification. **Depends on 1.3.** |
| **1.5** | Resolve Coverage Matrix P1 EDs | ED-588, ED-589, ED-612 | — | Three open P1 EDs from coverage matrix. |

### 3.2 P1 items added since workplan_final (post-2026-04-18)

| ID | Item | Source | Action |
|---|---|---|---|
| **1.6** | ED-543 Clock registry refresh verification | session_log_current | Determine if registry refresh landed under another ED. Close or execute. **Only active P1 in summary.** |
| **1.7** | PP-666 trio formal vetting | post-PP-672 | settlement_adjacency_v30, fractional_province_ownership_v30, faction_succession_split_v30 — all PROVISIONAL since 2026-04-19, all Class A. Each needs full N→Ω→Μ→М→Τ→Q vetting block. Currently committed to canon without vetting block. |
| **1.8** | Varfell victory paths editorial rewrite | canonical_sources note | Post-VTM-strike (PP-663). "Pending editorial rewrite" since 2026-04-19. **Diagonal dependency on 1.9 below.** |
| **1.9** | F2.5 Intelligence stat STRUCK verification | ED-748 | Audit active specs for Intelligence-as-faction-stat references. Result determines whether 1.8's Path A re-gate to "Intelligence ≥ 4" is valid. |
| **1.10** | F2 verification batch (ED-745–748) | Round 1 | IP=20 start (745), Intel Advancement Counter STRUCK (746), Popular Will STRUCK (747), Intelligence stat STRUCK (748). Single read pass against `references/valoria_canonical_definitive_r2.md` (14 KB) closes all four. |
| **1.11** | ED-768 orphaned PROVISIONAL markers triage | post-2026-04-25 | 13 orphaned markers in design docs reference pre-ledger EDs. Jordan-review classification. |

**Phase 1 exit criteria:**
- All P1 items in `editorial_ledger.yaml` resolved or escalated
- PP-666 trio carries valid vetting blocks
- Varfell victory paths rewrite committed
- All F2 verification batch closed

---

## §4 Phase 2 — Calibration Inputs

**Estimated effort: 3–5 sessions. Reference workplan_final §Phase 2 for full bodies.**

### 4.1 P2 items from workplan_final (12 items)

| ID | Item | Flag | Notes |
|---|---|---|---|
| **2.1** | Social Contest Re-simulation | AUD-SC-02, AUD-SC-03 | |
| **2.2** | Co-Movement Card Calibration | ED-577-01/02/03/04 | **⚠ HARD DEPENDENCY FOR PHASE 4** |
| **2.3** | NPC Stat Gaps | AUD-NPC-02 | |
| **2.4** | NPC Priority Tree Cross-Faction Simulation | AUD-NPC-03 | |
| **2.5** | Settlement Economy Simulation | AUD-SET-01, AUD-SET-03 | Depends on 1.2 + 1.3 |
| **2.6** | RM Victory Probability | AUD-VIC-02 | Depends on 2.4 |
| **2.7** | Mass Battle Editorial Items | AUD-MB-02 | |
| **2.8** | Combat Ranged TN Integration | AUD-COM-04, ED-129 | |
| **2.9** | Threadwork Foundation Text | AUD-TW-01 | |
| **2.10** | UI/UX Integration: Derived Stats + Settlement Map | AUD-UI-01, AUD-UI-02 | |
| **2.11** | Generational Transition Throughline | — | |
| **2.12** | params_threadwork Ob Alignment | AUD-TW-02 | |

### 4.2 Items added post-workplan_final

| ID | Item | Source | Action |
|---|---|---|---|
| **2.13** | PP-652 starting PT values verification | patch_register | T9=5, T6/T13=1, T4/T11/T12=2, rest=3. PROVISIONAL. Sim S2 needs these. Verify or promote. |
| **2.14** | hybrid_gaps_v30 propagation debt | design_registry | "PROPAGATION-PENDING — 17 hybrid gaps not yet in bg_v05 / stage11." Post-videogame-only collapse, verify which gaps still apply. |
| **2.15** | arc_register open editorials ED-401–405 | canonical_sources_notes | Five open editorials in arc register. Locate (likely pre-ledger). Classify or archive. |
| **2.16** | Solmund T-A..T-E throughline integration | A4 / atoms_pending | Five PROVISIONAL throughlines (Perceptual Prophylaxis, Seam Texts, Double Consciousness, Baralta Cracker, Solmund Repetition). T-A and T-C block V2 (Certainty/Conviction in NPC trees); T-B/T-D do not; T-E weakly. Assign canonical T-NN + parent М-NN. **Awaits Solmund Appendix B 9-item authority decisions.** |
| **2.17** | Solmund Appendix B 9 editorial items | atoms_pending | 3 Class B (Miraculous Event trigger, Miracle Investigation, Conviction-for-Miraculous) + 4 Class C (SA-gated thresholds, Accord +1, Proximity −1, others) + 2 Class D (Baralta direct communion lore, two witness traditions). Each needs N-tier Jordan decision. |
| **2.18** | Sim corpus triage (207 sim files in tests/sim/) | Round 2 | v2 references 6 (sim_var_01–06). Triage all 207: regression target / historical / extract findings. |
| **2.19** | Audit history triage (37 files) | Round 2 | designs/audit (48), tests/audit (29), tests/emergent_arc_skeleton_test (7). Surface still-relevant findings to editorial ledger. |
| **2.20** | proper_noun_triage_round2 status | Round 2 | references/proper_noun_triage_round2.yaml (50 KB). PP-665 was round 1. What's pending in round 2? |

**Phase 2 exit criteria:**
- All 20 P2 items resolved or scheduled-for-Phase-4
- 2.2 (Co-Movement) confirmed implementation-ready
- All Solmund decisions committed
- Sim corpus + audit history triaged

---

## §5 Phase 3 — Polish + Authority

**Estimated effort: 2–3 sessions. Reference workplan_final §Phase 3 for full bodies (18 items).**

### 5.1 P3 cleanup from workplan_final (18 items, 3.1–3.18)

Carried forward verbatim. Sim-relevant items (3.1, 3.2, 3.9, 3.11) sequence before Phase 4.

### 5.2 atoms_pending pipeline approval (NEW)

| ID | Item | Action |
|---|---|---|
| **3.A.1** | Stage 1 topic decomposition approval | `references/atoms_pending/2026-04-25/_consolidation_workplan.yaml` Stage 1 awaits Jordan. 316 atoms across 10 topics. **15–30 min review.** Unblocks document assembly (Stage 2) of remaining 9 master documents (Solmund is one of 10). |
| **3.A.2** | Stage 2 document assembly | Post-3.A.1. 9 consolidated docs (Solmund already done). `[infrastructure]` per doc. |
| **3.A.3** | Stage 3 audit pass per consolidated doc | Per-topic audit reports at `_audit_reports/<topic>_audit.md`. |
| **3.A.4** | Stage 4 post-audit canon decisions | Per topic: ingest into canon / archive without ingestion / reject. **Each consolidated doc may produce multiple downstream commits.** |

### 5.3 Authority decisions (Jordan-blocking)

| ID | Item | Tier | Touches |
|---|---|---|---|
| **3.B.1** | D-5 Einhir site-network model | **N** + Μ-δ + М-2 | T-15c, T-04. New mechanical layer or reskin? Renaissance analog: pilgrimage-route economics / shrine patronage. |
| **3.B.2** | D-4 Altonian invasion ~18 AG timeline | Ω-c | T-06, T-04. Lock for campaign starting state and deterministic seeds. **Read `canon/03_canonical_timeline.md` first to surface existing constraints.** |
| **3.B.3** | Ministry NPC design doc | Ω-c | T-08, T-14. Locate or commission. Open since 2026-04-20. |
| **3.B.4** | factions_ttrpg blocker | Mode authority | T-08, T-09, T-11, T-15a/b/c. Accept compilation/stage6 as canon or commission design-layer doc? |
| **3.B.5** | campaign_modes blocker | Mode authority | Accept compilation/stage12 or commission. Note: `videogame_mode_spec.md` covers mode collapse but not campaign-mode-specific parameters. |
| **3.B.6** | southernmost blocker (ED-048) | Mode authority | T-19, T-04. Open since 2026-04-04. Longest-standing. |
| **3.B.7** | Wave 1 proposal approvals | wave1_workplans | P1 (Leap UX), P3, P9, P10, P21. Each has DECISION items requiring editorial confirmation. **Folded into Phase 5.** |

### 5.4 Round 1-3 audit cleanup (additional Phase 3 items)

| ID | Item |
|---|---|
| **3.C.1** | Skills audit (11 skills) — PP-672/673/674 propagation to canon-guard, mechanic-audit, editorial-register |
| **3.C.2** | Tools inventory (23 tools) — current vs archive-candidate |
| **3.C.3** | Multi-file skills audit (orchestrator, combat-simulator, dice-model) |
| **3.C.4** | Three throughline registries reconciliation — `throughlines_meta.md` + `throughlines_complete.md` + `throughline_registry.md` numbering scheme + cross-reference |
| **3.C.5** | RS-in-tests disambiguation (~1,340 instances) |
| **3.C.6** | TD disambiguation (Mermaid TD vs PP-166 Thread Depth) |
| **3.C.7** | Patch register provisional/unknown sweep (156 entries: 65 provisional, 61 proposed, 30 unknown) |
| **3.C.8** | designs/godot/ purpose audit (4 files; relationship to designs/videogame/godot_architecture_specification.md) |

**Phase 3 exit criteria:**
- All 18 workplan_final P3 items resolved
- atoms_pending Stage 1 approved (unblocks Stage 2/3/4)
- All 7 authority items decided
- Three workplan/audit reconciliation items closed

---

## §6 Phase 4 — Full-Campaign Simulation Framework

**Estimated effort: 8–12 sessions. THIS IS THE GATE.**

**Reference workplan_final §Phase 4 verbatim for all sub-items.** Adopted unchanged.

### 6.1 Sub-items

| ID | Sub-item | Sessions |
|---|---|---|
| 4.0 | Framework Architecture | 1 |
| 4.1 | State Initialization | 1 |
| 4.2 | Season Resolution Engine (18 systems × resolution procedures) | 3–4 |
| 4.3 | Feature Coverage Checklist (~130 features across 13 categories) | 1 |
| 4.4 | Simulation Output & Analysis (50 baseline runs) | 1–2 |
| 4.5 | Stress Tests (8 scenarios) | 1–2 |
| 4.6 | Calibration Report | 1 |
| 4.7 | Regression Testing | 1 |
| 4.8 | Simulation Infrastructure | (parallel) |

### 6.2 Feature Coverage Checklist (~130 features)

13 categories per workplan_final §4.3:

| Category | Features |
|---|---|
| Personal Scale | 11 |
| Fieldwork | 13 |
| Social Contest | 14 |
| Threadwork | 16 |
| Mass Battle | 14 |
| Scale Transitions | 8 |
| Player Agency | 10 |
| NPC Behavior | 9 |
| Settlement & Governance | 10 |
| Victory & Endgame | 12 |
| Derived Stats Economy | 8 |
| Companion & Knot | 8 |
| Character Lifecycle | 5 |
| **Total** | **138** |

### 6.3 Stress Tests (8 scenarios)

Per workplan_final §4.5:

| ID | Scenario |
|---|---|
| 4.5.1 | Church Theocracy Rush |
| 4.5.2 | Military Conquest Death Spiral |
| 4.5.3 | Thread Practitioner Coherence Arc |
| 4.5.4 | Five-Faction Simultaneous Race |
| 4.5.5 | Altonian Invasion |
| 4.5.6 | NPC Cascade |
| 4.5.7 | Settlement Economic Engine |
| 4.5.8 | Long Campaign NPC Turnover |

### 6.4 The Calibration Gate

**No Godot implementation begins until calibration report confirms:**

| Criterion | Threshold |
|---|---|
| **No death spirals** | No faction enters unrecoverable decline before Season 30 |
| **No stasis** | No 10-season window where nothing changes |
| **Victory timing** | Within Season 60–100 (Year 15–25) |
| **Feature coverage** | All ~138 features fire ≥1 time across 50 runs (100%) |
| **MS crisis** | Reaches Fractured band (39–20) between Season 40–80 |
| **NPC arc transitions** | ≥4 of 14 named NPCs transition by Season 60 |
| **Player impact** | Player's faction outperforms AI-only by ≥2 stat points |

**Issue triage protocol** (sim-discovered issues):
- **P1 (balance-critical):** Resolve before Phase 5; loop back to Phase 1/2 → fix → regression
- **P2 (system-specific):** Resolve during Phase 5 or early Godot
- **P3 (cosmetic):** Track; don't block

### 6.5 v3 additions to Phase 4

| ID | Item | Action |
|---|---|---|
| **4.A.1** | ms_budget integration | All MS drain/recovery sources from `references/ms_budget.md` (canonical ED-668) wired into accounting phase |
| **4.A.2** | tests/sim_framework/ integration | 23 sim_framework files specify build patterns. Use existing patterns; don't reinvent. |
| **4.A.3** | atoms_pending Monte Carlo simulator | `09__sim-balance-py-36kb-monte-carlo-simulator.md` is preserved Python source for an existing balance simulator. Read; integrate or supersede. |
| **4.A.4** | Reconcile NPC count (7 v2 vs 14 workplan_final vs 24 valoria-game .tres) | Likely: 7 = major faction leaders subset; 14 = "named" full set; 24 = roster including extended. Sim S3 NPC priority trees: 14 named per workplan_final canonical. |
| **4.A.5** | PP-666 trio CANONICAL promotion | Sim S2 smoke-test outcomes determine promotion. settlement_adjacency, fractional_province, faction_succession_split. Currently PROVISIONAL. |

**Phase 4 exit criteria:** Calibration report meets all 7 criteria. Sim becomes Godot parity oracle.

---

## §7 Phase 5 — Godot Implementation Prep

**Estimated effort: 4–6 sessions. Reference workplan_final §Phase 5 for full body.**

### 7.1 workplan_final Phase 5 items (5)

| ID | Sub-item |
|---|---|
| 5.1 | GM-to-Engine Rule Conversion |
| 5.2 | Godot Implementation Sequence |
| 5.3 | Data Serialization Specification |
| 5.4 | Godot Scene Tree Architecture |
| 5.5 | Cross-Repo Propagation Protocol |

### 7.2 Engine bug fixes (post-2026-04-18 — already executed in Phase 0)

Phase 0.4 absorbed these. Reference for Phase 5 verification:
- 0.4.1 NPCTrajectoryEvaluator wired
- 0.4.2 Deferred consequences forwarded
- 0.4.3 GameMode stripped
- 0.4.5 Church stats fixed
- 0.4.6 Provisional values verified

### 7.3 GAP closure (from coverage_matrix.md)

| ID | Gap | T's | Prereq |
|---|---|---|---|
| **5.G.1** | GAP-T-01 ThreadworkSystem co-movement | T-03 (Μ-γ + Μ-δ) | Phase 4.A.1 (ms_budget) + threadwork P0 triage from 0.2.2 |
| **5.G.2** | GAP-T-02 `check_victory` unit tests | T-20 (М-6) | Full faction/territory state mock |
| **5.G.3** | GAP-T-03 ValoriaFactionAI per-framework decision tree coverage | T-08–T-15a/b/c (М-4), T-23 (М-5) | Branch coverage tests |
| **5.G.4** | GAP-T-04 NarrativeContainer routing | T-02 (Μ-γ) | Phase 0.4.1 (NPC eval wired) |

### 7.4 Wave 1 proposals as Phase 5 player-UX (NEW)

From `designs/workplans/wave1_workplans.md`:

| ID | Proposal | Decision items pending |
|---|---|---|
| **5.W.1** | P1 Leap UX (Two-Decision Player Surface) | DECISION P1-1 (surprise/prone Ob), P1-2 (multi-sentinel cap), P1-3 (conditional exit complexity). Implementation units: Entry-commit UX, Contact-phase execution, Sentinel action, Retention Roll resolution. |
| **5.W.2** | P3 (identity TBD via full read) | TBD |
| **5.W.3** | P9 (identity TBD) | TBD |
| **5.W.4** | P10 (identity TBD) | TBD |
| **5.W.5** | P21 (identity TBD) | TBD |

**Required action 5.W.0:** Read full `wave1_workplans.md` to identify P3/P9/P10/P21 proposals.

### 7.5 Architecture spec reconciliation (NEW)

| ID | Item |
|---|---|
| **5.A.1** | Reconcile architecture: "ONE autoload" spec vs implementation has three (EventBus, Meta, GameStateMachine). Update spec or refactor implementation. |
| **5.A.2** | Read `designs/videogame/godot_architecture_specification.md` (51 KB) to compare against `valoria-game/docs/architecture.md` (5.8 KB). Reconcile. |
| **5.A.3** | Meta.gd code review (41 KB autoload). Functions that should be in Tracker/Registry/NarrativeState. |
| **5.A.4** | systems/threadwork/ has 1 file. Verify implementation depth vs design (9 design docs). |

**Phase 5 exit criteria:** All P0–P11 phase tests green. Sim parity tests pass on identical seeds. Engine ready for first playable scene.

---

## §8 Phase 6 — First Playable

**Estimated effort: 2–3 sessions (mostly Godot-editor, out-of-band for orchestrator).**

**NEW phase. Absent from workplan_final.** Verifies experiential correctness — what mechanical correctness alone cannot test.

### 8.1 First Playable Season Loop

One season, end-to-end, human-tested:

1. SeasonSlate displays 2–3 scene options (Layer 2 — SituationGenerator)
2. Player enters one Combat scene (Layer 3 — CombatContainer with real data)
3. CascadeDisplay shows consequences (Layer 4 — reads Meta visual queue)
4. RS + CI + PI clocks advance visibly (Layer 1 — PersistentUI HUD)
5. One NPC arc condition evaluates (Μ-β fires visibly)
6. One Domain Echo propagates (Μ-δ fires visibly)

### 8.2 Required scenes (minimum viable)

From `designs/ui/` (9 design docs exist, none implemented):

| Scene | Throughline |
|---|---|
| `ui/persistent/` RS+WC HUD | T-04, T-20 — equal UI real estate per `wc_survival_spine.md` |
| `director/GameDirector.tscn` | Layer 2/3/4 orchestration |
| `containers/combat/CombatContainer.tscn` | Layer 3 minimal scene authoring |
| `ui/season_overview/` SeasonSlate | Layer 2 |
| `ui/cascade/` CascadeDisplay | Layer 4 |

### 8.3 Required content (minimum viable)

- Player character `.tres` (extracted from char-creation flow)
- 1 weapon `.tres`, 1 armour `.tres` (from C1 weapons/armour authoring against `params/combat.md`)
- 3 territories (subset of 17, enough for Domain Action exercise)
- 1 NPC `.tres` with arc condition (already authored — pick from 24 existing)

### 8.4 Q-elegance audit (NEW)

After P milestone reached, before full UI build:

- Core rule restatable after one reading?
- Second-order consequence predictable without additional rule-reading?
- External dependencies enumerated; "except when X" flagged?
- **Dramatic legibility test:** can a designer unfamiliar with the proposal read game-state and answer in one sentence each — *whose position is at risk, what each named actor wants, what happens if no one acts next season*?

Redesign cost pre-UI: ~1 session. Post-UI: ~3+ sessions. **Audit before commitment to full UI build.**

**Phase 6 exit criteria:**
- One season playable end-to-end
- Q-robust dramatic legibility test passes
- All 7 calibration-gate criteria still hold in shipped engine (sim-vs-game parity)

---

## §9 Phase 7 — Ongoing Maintenance

**Reference workplan_final §Phase 6.** Adopted with v3 additions.

### 9.1 Session Start (every session)

5-Lens sweep + freshness_gate check (per §1).

### 9.2 After Design Doc Changes

Update propagation_map; SHA refresh; ledger updates; co-file compliance.

### 9.3 Per Commit

Run `h.safe_commit()` (only valid path); freshness_gate `--update`.

### 9.4 New Issues

Add to active editorial ledger; flag severity; cross-reference.

### 9.5 Quarterly Review

- Patch register sweep
- Editorial archive triage
- Coverage matrix refresh
- Skills audit (per 3.C.1)
- Tools inventory (per 3.C.2)
- atoms_pending workflow status

### 9.6 Maintenance items (M-tier, parallel throughout)

| ID | Item |
|---|---|
| M.1 | RS-in-tests disambiguation (~1,340 instances) |
| M.2 | TD disambiguation |
| M.3 | `campaign_sim_npc_pcs_2026-04-18.py` Maret rename |
| M.4 | TC in `deprecated/` — defer indefinitely |
| M.5 | Branch protection rules (after First Playable) |
| M.6 | PAT rotation reminder |
| M.7 | Versions/ strategy (populate or remove) |
| M.8 | model_router.html, editorial-review.jsx purpose documentation |

---

## §10 Declared-Deferred (Out-of-Scope Until First Playable)

These are *known gaps*, not oversights. Each is declared so its absence is intentional.

| Domain | What's deferred | Trigger to start |
|---|---|---|
| **C5 Player Character UX** | Standing 0–7, Rank ladders, full character creation flow, tutorial path. (`designs/audit/player_world_bridge_2026-04-16.md` likely contains source content.) | Phase 6 + post-P stabilization |
| **C6 Localization / accessibility** | i18n via `tr()`, colorblind mode, audio sliders, key remapping, reduced motion, font scaling, settings menu | Post-P |
| **C7 Campaign authoring** | Default campaign scenarios, tutorial campaign, historical scenarios, what-if scenarios | Post-P |
| **B Build/Release** | export_presets.cfg, platform targets, release versioning, beta/playtest distribution | Post-P |
| **Asset content domain** | Background music, ambient, UI SFX, combat SFX; portraits, faction crests; map backgrounds; UI iconography; thread visualization shaders | Post-P |
| **Performance budgets** | Frame rate target (60 FPS min), save file size limit, memory ceiling, season-tick latency target | First profiling reveals issue |
| **Save format versioning** | `SaveData.version: int`; migration handler. (DA-01/02/03 must land first per workplan_final §5.3.) | Post-Phase 5 |
| **CONTRIBUTING / CODE_OF_CONDUCT / templates** | Multi-developer infrastructure | When team expands |
| **Multiplayer** | Likely NEVER. Decision: explicitly declare "single-player only" in README. | — |

---

## §11 Effort Estimates

| Phase | Items | Sessions | Dependencies |
|---|---|---|---|
| 0 Foundation | 25+ | 1–2 | None |
| 1 P1 Blockers | 11 | 2–3 | 1.2→1.3→1.4 chain; 1.9→1.8 |
| 2 Calibration Inputs | 20 | 3–5 | 2.2 hard dep for Phase 4; 2.5 dep on 1.2+1.3; 2.6 dep on 2.4 |
| 3 Polish + Authority | ~30 | 2–3 | atoms_pending Stage 1 unblocks Stages 2-4 |
| 4 Full-Campaign Sim | 9 sub-items + 8 stress tests | 8–12 | Phase 1 + 2.2 + 0.7 |
| 5 Godot Prep | 14 (5+4+5) | 4–6 | Phase 4 calibration accepted |
| 6 First Playable | 1 milestone + Q-elegance audit | 2–3 | Phase 5 GAP closure |
| 7 Ongoing | Permanent | — | — |
| **Total** | **~110 items** | **22–34 sessions** | |

**Phase 4 breakdown:**

| Sub-item | Sessions |
|---|---|
| 4.0–4.1 Architecture + initialization | 2 |
| 4.2 Season resolution engine | 3–4 |
| 4.3 Feature coverage validation | 1 |
| 4.4 Baseline analysis (50 runs) | 1–2 |
| 4.5 Stress tests | 1–2 |
| 4.6 Calibration report | 1 |
| 4.7 Regression | 1 |

---

## §12 Critical Path

```
Phase 0 (Foundation)
  ├── 0.1 Register truthfulness ──────→ unblocks all subsequent register-trust assumptions
  ├── 0.2 P0 + threadwork triage ─────→ unblocks Phase 1 P0/P1 ledger reconciliation
  ├── 0.3 Params staleness ───────────→ unblocks Phase 4 (sim reads params)
  ├── 0.4 Engine integrity ──────────→ unblocks Phase 5 + Phase 6 (engine layers operational)
  ├── 0.5 CI/orchestration wired ────→ unblocks all subsequent commit verification
  ├── 0.6 Status reconciliation ─────→ documentation truthful
  └── 0.7 Governance ────────────────→ legal + onboarding clarity

Phase 1 (P1 Blockers)
  Phase 1.1 Knot Formation ──────────────────────────────────────┐
  Phase 1.2 Accord Propagation ──→ Phase 1.3 Derived Stats ──→ 1.4 Faction Politics
  Phase 1.5 Coverage matrix P1s                                  │
  Phase 1.6–1.11 (post-2026-04-18 P1s) ──────────────────────────┤
                                                                  │
  ▼                                                               ▼
Phase 2 (Calibration Inputs)                                     │
  Phase 2.2 Co-Movement ⚠ HARD DEP for Phase 4                  Phase 2.5 Settlement economy
  Phase 2.1, 2.3, 2.4, 2.7–2.12 (parallel)                      Phase 2.10 UI integration
  Phase 2.6 RM victory ← depends on 2.4                          │
  Phase 2.13–2.20 (post-2026-04-18 P2s)                         │
  │                                                              │
  ▼                                                              │
Phase 3 (Polish + Authority)                                    │
  3.A atoms_pending Stage 1 ◄ Authority decision                │
  3.B authority decisions (Jordan-blocking)                     │
  3.C audit cleanup (parallel)                                  │
  ▼                                                              │
Phase 4 (Sim Framework) ← depends on Phase 1 + 2.2 + 0.7       │
  ├── 4.0–4.1 Build  ◄──────────────────────────────────────────┘
  ├── 4.2 Engine
  ├── 4.3 Coverage validation (~138 features)
  ├── 4.4 50-run baseline
  ├── 4.5 8-stress-test battery
  ├── 4.6 CALIBRATION GATE ⚠
  └── 4.7 Regression (loops back if issues)
  │
  ▼
Phase 5 (Godot Prep) ← gated on calibration acceptance
  ├── 5.1–5.5 workplan_final items
  ├── 5.G.1–5.G.4 GAP closure
  ├── 5.W.1–5.W.5 Wave 1 proposals
  └── 5.A.1–5.A.4 Architecture reconciliation
  │
  ▼
Phase 6 (First Playable) ← gated on Phase 5 GAP closure
  ├── 6.1 Season loop end-to-end
  └── 6.4 Q-elegance audit
  │
  ▼
Phase 7 (Ongoing) ← permanent
```

**Critical path:** 0.1 → 0.4 → 1.2 → 1.3 → 1.4 → 2.2 → 2.5 → 4.0 → 4.2 → 4.4 → 4.6 → 4.7 → 5.1 → 5.G → 6.1 → 6.4

**Minimum critical-path sessions: ~22.**

---

## §13 Vetting Posture for New Class A/B Work

Per PP-674 §8.5. Required for any Class A/B PP entry from PP-674 forward:

```yaml
vetting:
  class: A | B
  necessity: pass | fail | flagged   # N — Renaissance political dynamic
  omega: pass | fail | flagged       # Ω — central-experience contribution
  mu: [Μ-α | Μ-β | Μ-γ | Μ-δ]        # Modes served
  m_ratings:                         # 11-pattern rubric
    M-1: "+" | "✓" | "−" | "○"
    M-2: ...
    [...]
    M-11: ...
  q: pass | iterate | skip           # Quality
```

**Restoration fixes** (e.g., F1.1, F1.2):

```yaml
vetting:
  class: B
  restoration: true
  necessity: pass
  omega: pass
  mu: [Μ-β, Μ-δ]
  m_ratings: { M-1: ○, M-2: ○, M-3: ○, M-4: ✓, M-5: +, M-6: ○, M-7: ○, M-8: ○, M-9: ○, M-10: ○, M-11: ○ }
  q: pass
```

**Pre-PP-674 items:** `pre-framework: true`. Class C/D/E: `{ class: C }`.

`valoria_hooks.vetting_gate` blocks commits missing the block. CI runs same check.

---

## §14 Scope Frames

The workplan supports three scope decisions Jordan can make. Each is internally coherent.

| Frame | Stop after | Sessions | Output |
|---|---|---|---|
| **Frame A — Verified Spec** | Phase 4 calibration passes | ~14 | Verified design specification (paper) |
| **Frame B — First Playable** | Phase 6 milestone | ~22 | One-season Godot prototype (recommended) |
| **Frame C — Full Project** | All declared-deferred items + content | 50+ | Shippable game |

**Recommendation: Frame B.** Frame A produces a paper artifact. Frame C is open-ended. Frame B produces a tangible thing testable, iteratable, growable — and forces decisions infrastructure-only work can defer indefinitely.

The single most useful decision Jordan can make: **declare which Frame.** Without it, every subsequent revision continues accreting surface rather than narrowing toward a shippable artifact.

---

## §15 Risk Register

| Risk | Severity | Mitigation |
|---|---|---|
| Patch register lies confirmed (Phase 0.1.1 reveals uncommitted work) | **Critical** | Round 3 git verification confirmed commits exist; register staleness only. SHA recovery is mechanical. |
| Phase 0 takes longer than 2 sessions due to scope discovery | High | Hard time-box. Items not closable in 2 sessions promote to dedicated phase. |
| Authority decisions (3.B) stall for weeks | High | Stall path: Claude executes Phase 2 P2 + Phase 3 P3 cleanup + atoms_pending Stage 2 (auto-executable post-Stage-1) in parallel. |
| Calibration gate (Phase 4.6) fails | Medium | Expected. Triage protocol classifies P1/P2/P3; loops back to Phase 1/2. |
| atoms_pending Stage 1 introduces 27+ new editorial items | Medium | Triage budget reserved (Phase 3.A.1 includes ID-presence check). Items absorbed into editorial ledger before canonization. |
| 5-Lens sweep takes ~30 min/session and feels heavy | Low | Tooling exists; freshness_gate + broken_dependency_checker automate most lenses. Session log lens is manual but quick. |
| Q-elegance audit reveals redesign needs post-Phase 4 | Medium | Audit scheduled BEFORE Phase 6 commitment to UI; redesign cost ~1 session pre-UI vs 3+ post-UI. |
| Solo developer + scope = multi-year | Accepted | Frame B caps scope to ~22 sessions; rest declared-deferred per §10. |

---

## §16 What This Plan Achieves at Each Phase Boundary

| After phase | What can be claimed |
|---|---|
| 0 | All registers truthful; CI/freshness running; LICENSE+READMEs in; engine bugs fixed; data-truth foundation solid |
| 1 | All P1 design gaps resolved; framework canon verified |
| 2 | All calibration inputs ready; Solmund integration done; sim corpus triaged |
| 3 | All authority decisions landed; atoms pipeline approved; audit history surfaced |
| **4 (Frame A complete)** | **Verified mechanical specification: 138 features fire, 8 stress tests pass, 7-criterion gate met. Game works on paper.** |
| 5 | Engine layers operational; sim parity confirmed; Wave 1 proposals scaffolded |
| **6 (Frame B complete)** | **First playable season; Q-robust dramatic legibility tested by human; experiential correctness verified.** |
| 7 | Maintenance protocol; quarterly cadence; gradual content expansion until Frame C closes |

---

## §17 Bootstrap Update Required

Current bootstrap (`/mnt/project/VALORIA_PROJECT_INSTRUCTIONS.md`) does not run:
- compliance_check.py
- freshness_gate.py
- 5-Lens inconsistency sweep

**Add to bootstrap after Status Block, before STOP:**

```python
# Phase 0.5 enforcement: compliance + freshness gates
import subprocess
print("\n=== ENFORCEMENT GATES ===")

# Compliance
try:
    r = subprocess.run(['python3', 'tools/compliance_check.py', '--check-all'],
                       capture_output=True, timeout=60)
    print(f"compliance_check: {'PASS' if r.returncode==0 else 'VIOLATIONS'}")
    if r.returncode != 0: print(r.stdout.decode()[:1000])
except Exception as e:
    print(f"compliance_check: ERROR {e}")

# Freshness
try:
    r = subprocess.run(['python3', 'tools/freshness_gate.py'],
                       capture_output=True, timeout=60)
    if r.returncode == 0: print("freshness_gate: ALL FRESH")
    elif r.returncode == 1: print("freshness_gate: STALE — block sim/audit/patch on stale systems"); print(r.stdout.decode()[:500])
    elif r.returncode == 2: print("freshness_gate: SHA fields missing — run --update first")
except Exception as e:
    print(f"freshness_gate: ERROR {e}")
```

Phase 0.5 items 0.5.1 + 0.5.2 land this update.

---

## §18 What Was Reconciled

### From workplan_final.md

- All 7 Phase 0 housekeeping items (carried to §2.1 + 2.2)
- All 5 Phase 1 P1 blockers (carried to §3.1)
- All 12 Phase 2 P2 items (carried to §4.1)
- All 18 Phase 3 P3 items (referenced in §5.1)
- All 9 Phase 4 sub-items + ~138-feature checklist + 8 stress tests + calibration gate (carried verbatim to §6)
- All 5 Phase 5 items (carried to §7.1)
- Phase 6 ongoing protocol → §9
- 5-Lens inconsistency protocol → §1
- Standard commit protocol → §1
- Effort estimates → §11
- Critical path → §12

### From wave1_workplans.md

- P1 Leap UX → §7.4 5.W.1
- P3, P9, P10, P21 → §7.4 5.W.2-5.W.5 (placeholder pending full read 5.W.0)
- DECISION items → 3.B.7 authority decisions

### From valoria_workplan_v2.md (mine, 2026-04-26)

- F1.1 NPCTrajectoryEvaluator wiring → 0.4.1
- F1.2 Deferred consequences → 0.4.2
- F1.3 GameMode strip → 0.4.3
- F1.4 Church stats → 0.4.5
- F1.5 Provisional values → 0.4.6
- F1.7 README → 0.7.3
- F2.1 ED-543 → 1.6
- F2.2-F2.5 ED-745–748 → 1.10
- F2.7 threadwork P0 triage → 0.2.2
- F2.8 PP-652 → 2.13
- A1 D-5/D-4/Ministry → 3.B.1-3.B.3
- A2 v30-blockers → 3.B.4-3.B.6
- A3 Varfell rewrite → 1.8
- A4 Solmund → 2.16-2.17
- V1 PP-666 trio → 4.A.5
- V2 sim corpus → 2.18
- V3 GAP closure → 5.G.1-5.G.4
- P milestone → §8 Phase 6
- C4 Q-elegance → §8.4
- M· items → §9.6

### From Round 1-3 audits

- Round 1 player-engagement gap → §8 Phase 6 introduced
- Round 1 elegance/smoothness/robustness analysis → §16
- Gap addendum G1 (Meta.gd game_mode) → 0.4.3 expanded
- Gap addendum G2 (no CI in valoria-game) → 0.5.3
- Gap addendum G3 (compliance_check not running) → 0.5.1
- Gap addendum C5 Player Domain → §10 declared-deferred
- Gap addendum B Build/Release → §10 declared-deferred
- Round 2 wave1_workplans existence → §0 supersession + §7.4
- Round 2 N1-N6 narrative throughlines → 3.C.4 throughline reconciliation
- Round 2 P-### test infrastructure → §3.2 canon compliance gate
- Round 2 atoms_pending pipeline → 3.A.1-3.A.4
- Round 2 freshness_gate missing → 0.5.2
- Round 2 architecture spec violations → 5.A.1-5.A.4
- Round 3 patch register truthfulness → 0.1.1 (verified: register stale, commits exist)
- Round 3 governance gaps → §2.7
- Round 3 5-Lens protocol → §1
- Round 3 Phase 4 calibration gate → §6.4
- Round 3 ~130-feature catalog → §6.2 (~138 actual)
- Round 3 NPC count reconciliation → 4.A.4
- Round 3 audit history → 2.19
- Round 3 atoms_pending 27 unknown IDs → 0.2.3

---

*End of Workplan v3. This document supersedes all prior workplan artifacts. Next action per §15 risk register: Sprint 1 = Phase 0.*
