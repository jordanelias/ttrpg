# Valoria Ecosystem Workplan — 2026-04-30

STATUS: SUPERSEDED — see ecosystem_workplan_v2_2026-04-30.md (ratified 2026-05-01)
DRAFT: 2026-04-30
SCOPE: Consolidates conversation 2026-04-30 — vector audit, P0 propagation, repo / ecosystem / atom-taxonomy / vector-integration proposals, content audit, code-developer audit. Forward path through 7 phases.
AUTHORITY: Superseded by v2; retained as historical record.

---

## §0 Executive summary

Two commits landed this session: `eae4eb0b6` (terminology vector-audit folder) and `157523f2d` (P0 propagation pass — PP-691 / ED-772). The propagation pass shipped 5 atomic terminology actions across 10 files, with three P0 defects detected in self-audit (mechanical-threshold regression in `npc_behavior_v30.md`; glossary-renumbering cross-reference risk; Mode G case-sensitivity bug).

Beyond commits, the conversation produced four conceptual proposals — repository audit, ecosystem update, atom-first commit taxonomy, vector/LLM data-architecture integration — which a code-developer audit then revealed are unifiable into a single multi-phase pipeline rebuild. Total findings consolidated: **17 content-audit + 30 code-audit = 47 distinct issues** (after dedup, ~38 unique).

**This workplan sequences forward work in 7 phases over an estimated 8–13 directives** (≈ 2–3 weeks dedicated dev, or proportionally more part-time), with explicit decision points and exit criteria at each phase boundary. Phase 0 (cleanup of today's P0s) is non-negotiable and recommended same-session-or-next-directive. Phase 1 (read-only schema validation) is the cheapest information-gathering step and is recommended next.

---

## §1 Current state — snapshot 2026-04-30

### §1.1 This-session commits

| SHA | Date | What | Status |
|---|---|---|---|
| `eae4eb0b6` | 2026-04-30 | `designs/audit/2026-04-30-terminology-vector-audit/` (4 deliverables + 11 data artefacts; 676 lines) | applied |
| `157523f2d` | 2026-04-30 | PP-691 / ED-772 — terminology P0 propagation pass (10 files; ~341k chars) | applied |

### §1.2 Live register state

- `patch_register_active.yaml`: 33 PP entries, latest PP-691, max ID PP-691, gap at PP-689 (reserved for SHA followup).
- `editorial_ledger.yaml`: 8 active entries, latest ED-772, `next_id: 773`.
- `propagation_map.md`: ~52k chars (≈ 12k tokens; near 80% of 15k threshold).
- `censured_vocabulary.yaml`: 11 entries (populated this commit; was empty stub).
- `canonical_sources.yaml`: 19,634 chars; 263 lines of "Last touched" comments accumulating.
- `glossary.md`: 13 parts (renumbered this commit).
- `alias_registry.yaml`: ~19k chars; collision_table updated.
- `supersession_register.yaml`: untouched.

### §1.3 Outstanding defects from this-session work (P0 cleanup queue)

| ID | Description | Source | Cost-to-fix |
|---|---|---|---|
| **T1** | `npc_behavior_v30.md` priority-tree branches now read `IF CI < 75` / `IF CI ≥ 75` after TC→CI rename, but ci_political_v30 §2.1 removed the 75-threshold (Mass Seizure now probabilistic from CI ≥ 60). Mechanical regression: NPC AI fires off a non-canonical threshold. | content audit T1 | 5–10 min surgical edit |
| **D1** | Glossary parts renumbered (old 11 → 12, old 12 → 13, new 11 inserted). Corpus cross-references to "Part Twelve UNRESOLVED" or "glossary §12" silently broken. Not yet grepped. | content audit D1 | 5 min grep + fix |
| **B1** | Mode G context filter case-sensitivity bug (`re.compile(r'...seizure...threshold...Holy)')` without `re.IGNORECASE`). True actionable count higher than reported 21. `mode_g_2026-04-30.json` is technically incorrect. | content audit B1 | 5 min re-run + JSON patch + audit-folder note |

### §1.4 Outstanding from prior sessions (carried forward, not in scope of this workplan unless Phase 0 is expanded)

- PP-689 SHA followup (covers PP-690 + PP-691 file edits — single SHA-update commit pending).
- NPC Behavior audit (107k chars even after Conviction Track extraction — needs dedicated session).
- Promote remaining isolates: Wager, Thread Revelation (each ~PP-681-scope).
- Convictions framework registration (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity).
- Pressure Points framework registration (Evidence, Consequence, Authority, Loyalty).
- Three-doc Cohesion → Discipline sweep (5 paragraphs total).
- Bare `GM` corpus sweep (29 paragraphs, 14 docs).
- VTM / Cultural Reformation / Niflhel-as-faction / Coup Counter design-judgment cleanups.
- Jordan review of accumulated PP chain 676..691.
- PT-01, ACCT-01, INTER batches.
- Intelligence stat, LICENSE/GOV-08, §1.1 Knot Formation, §1.2 Accord Propagation.

---

## §2 Consolidated findings inventory

### §2.1 Content findings (17, by direction)

| ID | Severity | Direction | Finding |
|---|---|---|---|
| T1 | P0 | top-down | npc_behavior_v30 mechanical regression (incomplete atom) |
| T2 | P2 | top-down | Scope creep across abstraction layers in this conversation |
| T3 | P3 | top-down | Project-intent (positive feedback loop) not visible in recent infrastructural work |
| B1 | P1 | bottom-up | Mode G context filter case-sensitivity bug |
| B2 | P1 | bottom-up | Glossary cites `_proposal` doc as canonical (Conflict Architecture) |
| B3 | P2 | bottom-up | Church Prominent disambiguation incomplete |
| B4 | P3 | bottom-up | PP-689 reservation not documented in patch_register |
| B5 | P2 | bottom-up | `next_id:` field is non-binding YAML comment |
| V1 | P1 | vertical | Inherited graphs (2026-04-29) trusted without sample re-verification |
| V2 | P2 | vertical | P2 conviction-symmetry FAIL flagged but not investigated this run |
| V3 | P0 | vertical | Atom proposal partially reinvents existing structure |
| D1 | P0 | diagonal | Glossary renumbering may break external cross-refs (unverified) |
| D2 | P2 | diagonal | Audit-evidence-citation atoms compounded with term:definition atoms |
| D3 | P2 | diagonal | propagation_map evidence pointers prose-level, not atom-level |
| L1 | P3 | lateral | Audit folder name composition deeper than precedent |
| L2 | P2 | lateral | Class B vetting may not be granular enough for term-governance commits |
| L3 | P3 | lateral | Severity tag scales differ between audit and patch register |
| H1 | P1 | horizontal | canonical_sources.yaml comment accumulation |
| H2 | P2 | horizontal | Bootstrap fetched stale registers — caching/freshness opaque |
| H3 | P3 | horizontal | Order of operations bottom-up not top-down this session |

### §2.2 Code findings (30, by category)

| ID | Severity | Category | Finding |
|---|---|---|---|
| A1 | P0 | concurrency/atomicity | No atomicity guarantees on multi-file commits beyond git itself |
| A2 | P0 | concurrency/atomicity | Concurrent-session ID-collision unsolved |
| A3 | P1 | concurrency/atomicity | Bootstrap-time staleness is unhandled cache invalidation |
| B1c | P0 | state | Cross-register referential integrity hand-maintained |
| B2c | P1 | state | No schema validation on registers |
| B3c | P2 | state | Generated artefacts (_index.md) coexist with sources without separation |
| C1 | P1 | data flow | Vector audit pipeline is documented scaffold, not runnable |
| C2 | P2 | data flow | Append operations not idempotent |
| C3 | P2 | data flow | Bootstrap caches scripts to runtime without version pin |
| D1c | P0 | testability | Zero unit tests on hook logic |
| D2c | P0 | testability | No regression suite for atom application |
| D3c | P1 | testability | No simulation harness for register edits |
| E1 | P1 | observability | Hook failures unlogged structurally |
| E2 | P2 | observability | No metrics on register growth, drift, audit cadence |
| E3 | P2 | observability | No runtime monitoring of audit folder publication |
| F1 | P0 | reproducibility | vector_audit.py cannot reproduce its own published output |
| F2 | P1 | reproducibility | mode_g_2026-04-30.json generated by transcript-only Python |
| G1 | P1 | type discipline | Free-form string identifiers for PP/ED/T-NN |
| G2 | P2 | type discipline | Path strings duplicated across registers |
| H1c | P1 | docs | No internals architecture doc |
| H2c | P2 | docs | Skill scripts have no API contracts |

(Note: code findings reuse letters A–H; suffix `c` to distinguish from content findings where there's a collision.)

### §2.3 Dedup pass — content ↔ code overlaps

| Content finding | Code finding | Combined description |
|---|---|---|
| B5 (`next_id:` non-binding) | A2 (concurrent ID collision) | Same defect: ID acquisition is not transactional. |
| H2 (bootstrap stale registers) | A3 (cache invalidation) | Same defect: bootstrap reads can lag live state. |
| V3 (atom reinvents structure) | G1, G2 (type discipline) | Adjacent: atoms are typed objects today's free-form strings should become. |
| H1 (canonical_sources comments) | E2 (no growth metrics) | Adjacent: register-growth visibility absent. |
| V1 (inherited graphs unverified) | F1, F2 (reproducibility) | Same defect: pipeline outputs not regenerable. |

After dedup: **~38 distinct underlying defects.** P0 count: 8 distinct (T1, V3, D1, A1, A2, B1c, D1c, D2c, F1).

---

## §3 Logic for approach — six principles

The phase ordering below is not arbitrary. Six principles drive it:

**P-1: Repair before extend.** Today's commits introduced 3 P0 defects. Any forward work that touches the same files (npc_behavior_v30, glossary, audit folder) needs those defects resolved first or it builds on a broken floor. Phase 0 is non-negotiable.

**P-2: Diagnose before treat.** Schemas + validators are *read-only* — they observe the registers and report violations without changing anything. Running them on the current state reveals the actual scope of referential bugs (likely far more than the audits surfaced). Phase 1 is cheap, high-information, and zero-risk. It also produces empirical data for whether atoms-first is the right framing (V3 finding).

**P-3: Backfill before evolve.** Before designing how atoms-going-forward should work (Phase 4), retroactively decompose recent PPs (PP-678, PP-690, PP-691) into atoms (Phase 3). Validates the taxonomy against real commits. Reveals where the proposed taxonomy is wrong, where it collapses, where new categories are needed. Stops us shipping a typed system based on a speculative model.

**P-4: Shadow before cutover.** New primitives (`propagate()`) must run *alongside* current `safe_commit` before replacing it. Both produce file edits; differ them. Expose discrepancies. Expose cases the new primitive doesn't yet handle. Cutover happens only after shadow mode passes ≥ N commits without divergence. Same discipline the vector audit's v2 → v3 migration followed (locked thresholds, validated properties before publishing).

**P-5: Reproducibility before scale.** Adding new diagnostics (embedding-augmented modes I/J, RAG consumer surface) before existing diagnostics (vector audit Modes A-H) are reproducibly executable would be malpractice. Phase 5 closes that gap before any scaling work.

**P-6: Bottom-up sufficiency.** Each phase produces *standalone value*. If Jordan stops the workplan after Phase 1, the deliverable (typed schema map + violation report) is still useful. If after Phase 3, retroactive atom decomposition is itself a documentation artefact. Each phase compounds the next, but no phase is purely setup-for-later.

---

## §4 Phases

Each phase below: **scope · deliverables · dependencies · exit criteria · effort estimate · key risks**.

### Phase 0 — Outstanding cleanup (immediate)

**Scope:** Resolve the 3 P0 defects from this-session work (T1, D1, B1).

**Deliverables:**
- Surgical edit to `designs/npcs/npc_behavior_v30.md` priority-tree CI-threshold lines (either update to canonical thresholds from `ci_political_v30.md` §2.1, or add `[STALE-THRESHOLD]` markers with cross-ref).
- Corpus grep for `glossary.*\b(11|12|XI|XII|Part Eleven|Part Twelve|UNRESOLVED)\b`; fix any external cross-references caught by glossary renumbering.
- Re-run Mode G with `re.IGNORECASE`; patch `mode_g_2026-04-30.json` data file; append note to `02_weakness_register.md` §1.1 and `01_methodology.md` §3 disclosing the patch.
- Single PP / ED entry for the fix commit (PP-692 / ED-773 if no other commits land first).

**Dependencies:** None. Can run immediately.

**Exit criteria:**
- All 3 P0 defects resolved; commit lands.
- Audit folder annotated with post-publication patch.
- Updated mode_g count reported.

**Effort:** 1 directive. ~30–60 min focused work.

**Risk:** Low. Surgical edits, no architecture changes.

### Phase 1 — Schema canonicalization + read-only validation

**Scope:** Author JSON Schemas for all 8 active registers. Build a `valoria validate` CLI that runs them over live state and produces a violation report. No write-path changes.

**Deliverables:**
- `schemas/` directory with: `patch_register_entry.schema.json`, `editorial_ledger_entry.schema.json`, `canonical_source_entry.schema.json`, `censured_vocabulary_entry.schema.json`, `propagation_map_entry.schema.json`, `supersession_register_entry.schema.json`, `alias_registry_entry.schema.json`, `audit_finding.schema.json`.
- Each schema declares: required fields, types, format constraints (`PP-\d+`, ISO-8601 dates), referential constraints (path-must-exist, foreign-key-must-resolve).
- `valoria validate` CLI as `skills/valoria-validate/scripts/validate.py`.
- Violation report committed as `designs/audit/{date}-schema-validation-baseline/02_findings.md`.

**Dependencies:** Phase 0 (must repair before measure — broken state would inflate the violation count with already-known defects).

**Exit criteria:**
- All 8 schemas published.
- CLI runs against live state; produces violation report.
- Report categorizes violations as: schema-only, referential-only, both. Counts published.
- Jordan reviews report; decides whether atom-first design is supported by empirical defect distribution (informs Phase 2 scope).

**Effort:** 1 directive. Schemas are mechanical; CLI is light Python.

**Risk:** Low — read-only. Highest *information* value of any phase.

**Output decision points:**
- If violation count is large + structurally similar (e.g. mostly `affects:` path-not-found) → Phase 2 scope can shrink (the diagnostic is sufficient).
- If violation count reveals novel defect classes → Phase 2 scope expands.

### Phase 2 — Ecosystem audit (E1-expanded)

**Scope:** Comprehensive read-only inventory of hooks, skills, registers, conventions, identifier-numbering, document-category taxonomy, commit primitives, integration concept, and vector-layer integration. The audit deliverable scopes Phases 3+.

**Deliverables:** dated audit folder `designs/audit/{date}-ecosystem-audit/`:
- `00_workplan.md` — config, scope, bound on each dimension.
- `01_methodology.md` — execution provenance.
- `02_weakness_register.md` — primary deliverable. Sections:
  - §1 Hooks inventory (existing hooks, dead references, threshold provenance)
  - §2 Skills inventory (scaffolds vs implementations, missing skills)
  - §3 Registers inventory (purpose, overlap, schema readiness)
  - §4 Conventions inventory (implicit rules, naming, dating, file organization)
  - §5 Identifier-numbering audit (gaps, collisions, allocation mechanism)
  - §6 Document category taxonomy proposal (refined from this conversation's draft)
  - §7 Commit primitive proposal (refined `propagate()`)
  - §8 Integration concept (when, what, how)
  - §9 Atom taxonomy proposal (refined; explicit mapping to existing fields per V3 finding)
  - §10 Vector-layer integration (live-state vs snapshot; predictions; embeddings)
  - §11 Action queue (P0/P1/P2 with cross-references to subsequent phases)
- `03_validation_report.md` — does the ecosystem itself satisfy the structural properties it asks of design docs? (Self-audit of self-auditing system.)

**Dependencies:** Phase 1 (schema-validation baseline informs §3 register inventory).

**Exit criteria:**
- Audit committed.
- Atom-taxonomy proposal mapped against existing fields (resolves V3).
- Phase 3+ scopes determined empirically rather than speculatively.

**Effort:** 1 directive. Substantial deliverable but methodology mirrors today's vector-audit run (which fits in 1 directive).

**Risk:** Medium. Risk is scope creep within the audit (what we did this conversation). Mitigated by hard-locking deliverable structure before drafting.

### Phase 3 — Atom store + retroactive decomposition

**Scope:** Implement append-only atom store. Retroactively decompose recent PPs into atoms; commit atom records as backfill. Validates atom taxonomy.

**Deliverables:**
- `references/atom_store/atoms.jsonl` — append-only JSONL store, schema-validated.
- `references/atom_store/atom_predictions.jsonl` — predictions awaiting verification.
- `references/atom_store/atom_verifications.jsonl` — post-audit verification outcomes.
- Schema in `schemas/atom.schema.json`.
- CLI: `valoria atom add`, `valoria atom verify`, `valoria atom list`.
- Backfill: PP-678, PP-690, PP-691 retroactively decomposed; atom records committed.
- Backfill report: `designs/audit/{date}-atom-backfill/02_decomposition_findings.md` — records where the taxonomy was wrong, where atoms collapsed, where new categories were needed.

**Dependencies:** Phase 2 (taxonomy is finalized in audit deliverable).

**Exit criteria:**
- Atom store is operational + schema-validated.
- 3 historical PPs decomposed; ≥ 80% of decomposition produces atoms cleanly mapped to taxonomy.
- Decomposition findings published; taxonomy refined accordingly.
- Jordan ratifies refined taxonomy.

**Effort:** 2 directives. Directive 1: implementation + schema + 1 PP decomposition. Directive 2: 2 more decompositions + findings.

**Risk:** Medium. Taxonomy may need substantial revision after backfill. Mitigated by Phase 2 doing the speculative work first.

### Phase 4 — `propagate()` primitive in shadow mode

**Scope:** Implement typed commit primitive. Run in shadow mode alongside `safe_commit` for next ≥ 3 real commits. Diff outputs.

**Deliverables:**
- `propagate()` primitive in `skills/valoria-orchestrator/scripts/`.
- `Directive` / `Atom` / `CommitResult` dataclasses with type discipline.
- Co-touch enforcement derived from atom categories (not hand-written hook rules).
- Identifier acquisition primitive (`acquire_pp_id()` / `acquire_ed_id()`) — atomic, retry-on-conflict.
- Shadow-mode runner: takes the same directive, produces both `safe_commit`-style and `propagate()`-style file edits, diffs them, reports.
- Shadow-mode report after ≥ 3 commits: `designs/audit/{date}-propagate-shadow-mode/02_divergences.md`.

**Dependencies:** Phase 3 (atom store must exist).

**Exit criteria:**
- Shadow mode validates against ≥ 3 commits with zero unexplained divergence.
- Atomic ID acquisition replaces `next_id:` non-binding comment.
- Phase 6 cutover criteria defined (e.g. N commits clean before cutover).

**Effort:** 2–3 directives.

**Risk:** Medium-high. The new primitive must handle all current commit shapes. Risk of "novel primitive doesn't yet handle case X." Shadow mode is the mitigation — divergences are caught, not committed.

### Phase 5 — Vector audit reproducibility

**Scope:** Port ad-hoc pipeline code from conversation transcripts into `skills/valoria-vector-audit/scripts/vector_audit.py` proper. Make `valoria audit run` reproducibly regenerate canonical artefacts.

**Deliverables:**
- `vector_audit.py` `main()` actually runs all 8 stages end-to-end.
- Stages 1–7 implemented from methodology + reference run code.
- `valoria audit run --output-dir DIR` regenerates `tokens.json`, `g_cite.json`, `g_metadata.json`, `degrees.json`, `multigraph_diagnostics.json`, `validation.json`.
- Verifies regenerated outputs match published 2026-04-29 reference artefacts (modulo intentional Mode G expansions).
- CI step that re-runs the audit on every commit and archives drift report.

**Dependencies:** None hard, but Phase 1 schemas help validate audit output schema. Recommended after Phase 4 because shadow-mode diffs reveal what the audit needs to track.

**Exit criteria:**
- `valoria audit run` produces canonical artefacts.
- 2026-04-29 reference run regenerable from script (sanity check: re-run produces equivalent or improved-with-disclosed-Δ output).
- B1 (Mode G case bug) resolved at code level — hardcoded into the canonical implementation.

**Effort:** 1 directive. Methodology is fully specified; code is the gap.

**Risk:** Low-medium. Gnarly code (multi-graph construction, citation extraction) but well-specified inputs/outputs.

### Phase 6 — Ring 1 hooks rewrite + Ring 2 CI + test harness

**Scope:** Replace current `valoria_hooks.py` with schema-driven version. Add CI workflow. Build pytest harness with golden-file fixtures.

**Deliverables:**
- `valoria_hooks_v2.py` — schema-driven; no hand-written co-file rules; consults atom-taxonomy for validation.
- Test harness: `tests/` directory with fixture register files, atom-application golden files, schema-violation injection tests.
- CI workflow (GitHub Actions): runs `valoria validate`, runs schema validation, runs test suite, runs vector-audit drift report.
- Migration: existing hook calls updated to v2 API.
- Dead references resolved: `doc_index_gen` and `freshness_gate` either implemented or removed (today's session surfaced both as silent skips).

**Dependencies:** Phases 1, 3, 4 (schemas, atom store, propagate primitive all exist).

**Exit criteria:**
- All current hook checks have v2 equivalents (no regressions).
- Test coverage ≥ 80% on hook logic.
- CI green on the live repo state.
- Dead references resolved.

**Effort:** 2–3 directives.

**Risk:** Medium. Hook rewrite must preserve all current enforcement; regressions silently break commits. Mitigated by test harness + shadow mode where possible.

### Phase 7 — Full cutover (conditional)

**Scope:** Deprecate `safe_commit` direct path. `propagate()` is sole commit entry. Free-form YAML edits forbidden by hook unless they go through typed registry primitives.

**Deliverables:**
- `safe_commit` removed or aliased to `propagate()` with shim.
- All commits flow through atom decomposition.
- Convention doc `references/conventions.md` published — internals architecture, primitives reference, atom taxonomy reference.

**Dependencies:** Phase 6 (CI must be green; tests must cover regressions).

**Exit criteria:**
- ≥ N commits land via propagate-only without rollback.
- No outstanding P0/P1 against the new pipeline.

**Effort:** 1–2 directives.

**Risk:** Highest. Cutover removes the safety net of the old primitive. Recommended deferral until ≥ 3 real-world months of shadow mode validate the new path.

**Recommendation:** Make Phase 7 explicitly conditional. Phases 1–6 produce most of the value; Phase 7 is the discipline-tightening step that should only run when everyone is comfortable.

---

## §5 Connectivity matrix

How phases interlock. Read row-as-phase, column-as-other-phase: cell value indicates dependency type (`enables` / `validated by` / `informs scope of`).

| ↓ depends on / right enables → | Ph0 | Ph1 | Ph2 | Ph3 | Ph4 | Ph5 | Ph6 | Ph7 |
|---|---|---|---|---|---|---|---|---|
| **Ph0 cleanup** | — | enables clean baseline | — | — | — | resolves B1 in code | — | — |
| **Ph1 schemas** | requires Ph0 | — | informs §3 inventory | provides atom schema model | provides typed primitives | provides audit schema | provides hook validation rules | enables typed-only primitive |
| **Ph2 ecosystem audit** | — | requires Ph1 baseline | — | scopes taxonomy | scopes propagate() spec | scopes audit reproducibility | scopes hook rewrite | scopes cutover |
| **Ph3 atom store** | — | uses schemas | finalizes taxonomy | — | provides atoms for propagate | — | provides atom validation | enables atom-only commits |
| **Ph4 propagate** | — | uses schemas | uses primitive spec | uses atom store | — | uses audit reproducibility for verification | provides hook v2 inputs | becomes sole primitive |
| **Ph5 audit reproducibility** | — | uses schemas | uses methodology | provides atom verification harness | enables propagate prediction-validation | — | enables CI audit step | maintained under cutover |
| **Ph6 hooks v2 + CI** | — | uses schemas | uses convention proposals | uses atom validation | uses propagate primitive | uses audit CI | — | required for cutover |
| **Ph7 cutover** | — | — | — | — | requires shadow validated | — | requires CI green | — |

**Critical path:** Ph0 → Ph1 → Ph2 → Ph3 → Ph4 → Ph6 → Ph7. Ph5 is parallelizable with Ph4 (same dependencies).

**Earliest-stop value:** Each prefix of the critical path produces standalone value:
- `Ph0` alone → repaired baseline.
- `Ph0+Ph1` → typed schemas + violation report.
- `Ph0+Ph1+Ph2` → comprehensive ecosystem map.
- `Ph0+Ph1+Ph2+Ph3` → typed atom-aware governance.
- (each subsequent prefix adds primitives, then enforcement, then cutover.)

---

## §6 Decision points

Explicit human-in-the-loop checkpoints. Workplan does not auto-advance.

| After | Decide |
|---|---|
| Ph0 | Proceed to Ph1, defer (other priorities), or rescope. |
| Ph1 | Whether atom-first design is supported empirically (informs Ph2 scope). Whether to expand Ph2 to fold in any patterns Ph1 surfaced. |
| Ph2 | Final atom taxonomy. Final commit-primitive spec. Whether to fold integration concept + register consolidation into Phase 3, separate phase, or defer. |
| Ph3 | Whether retroactive decomposition validates the taxonomy or surfaces breaking changes. Whether to refine and re-decompose, or proceed. |
| Ph4 | Cutover criteria for Ph7 (e.g. "N consecutive shadow-mode runs without divergence"). Whether to extend shadow mode or proceed to Ph6. |
| Ph5 | Whether to add embedding-augmented Mode I/J diagnostics now or defer (re-checks against methodology lock-in concern V4). |
| Ph6 | Whether CI is sufficient stable for Ph7. Whether to extend hook test coverage. |
| Ph7 | Final cutover gate. |

---

## §7 Risk register

| Risk | Severity | Phase | Mitigation |
|---|---|---|---|
| Concurrency hazards remain in Phases 0–3 | High | 0–3 | Single-session commits only until Phase 4 introduces atomic ID acquisition. Document the limitation. |
| Scope creep within phase deliverables | High | All | Hard-lock deliverable structure + exit criteria before drafting phase audits. Reference today's "scope climbed 6 layers" pattern. |
| Continuity across N directives | Medium | 1–7 | Each phase completes independently. Workplan is committable + referencable. Re-bootstrap reads the workplan as anchor. |
| Sunk cost / institutional knowledge loss | Medium | 6–7 | Don't rip-and-replace. Shadow modes everywhere. Keep current primitives until new ones are ≥ 3-months proven. |
| Atom taxonomy wrong | Medium | 2–3 | Phase 3 backfill is empirical validation. Decomposition failures route back into taxonomy refinement, not silent acceptance. |
| Vector audit methodology drift | Medium | 5 | Phase 5 enforces methodology §3.7 thresholds locked in code. Embeddings (Mode I/J) deferred per V4 concern. |
| New defect classes surface mid-rollout | Low-medium | All | Each phase produces audit deliverable; defects route to next phase or backlog. |
| Project-intent drift (T3) | Low | All | Workplan is infrastructure; gameplay validation is separate. Schedule a gameplay-validation directive after Phase 2 to re-anchor. |
| Persistence-layer turn loss during long deliverables | Low | 1–7 | Per `<persistence_mitigation>`: inline checkpoints during multi-stage work. Pre-flight on > 200-line deliverables. |

---

## §8 Out-of-scope (explicit)

The following items are tracked but not in this workplan's execution scope. They will continue to be handled via current `safe_commit` until Phase 4+.

- **Wager + Thread Revelation isolate promotion** — gameplay-design work; ~PP-681-scope each. Either folded into a "Phase 1.5 — backlog burndown" sub-track, or deferred entirely.
- **Convictions / Pressure Points framework registration** — design + registry work. Same handling.
- **Three-doc Cohesion → Discipline sweep** — terminology cleanup; runs as PP-693-scope when scheduled.
- **Bare GM corpus sweep** — terminology cleanup; runs as PP-694-scope when scheduled.
- **VTM / Cultural Reformation / Niflhel-as-faction / Coup Counter design-judgment cleanups** — require Jordan design input per site.
- **NPC Behavior audit** — separate dedicated session; out of ecosystem scope.
- **PT-01, ACCT-01, INTER batches; Intelligence stat; LICENSE/GOV-08; Knot Formation; Accord Propagation** — design-content backlog from prior sessions.
- **Repository audit Tier A (audit folder consolidation)** — folded into Phase 2 ecosystem audit §3 (registers + folders inventory).
- **Repository audit Tier B (cross-reference integrity)** — folded into Phase 1 schema validation.
- **Repository audit Tier C (naming consistency, skill folder hygiene)** — folded into Phase 6 hook rewrite + Phase 2 conventions.

The repository-audit framing from earlier in the conversation is fully absorbed by Phases 1, 2, 6.

---

## §9 First-action recommendation

**Phase 0 — same session if budget permits, else immediately next directive.**

Three surgical commits, ≤ 1 hour total:

1. T1 fix — `npc_behavior_v30.md` priority-tree threshold lines: either update to canonical `ci_political_v30.md` §2.1 thresholds, or add `[STALE-THRESHOLD: see ci_political_v30 §2.1]` markers pending Jordan design judgment per affected branch. Recommend the marker approach since the design-judgment is non-trivial (probabilistic Mass Seizure changes branch logic, not just numbers).
2. D1 fix — `grep -rn "Part Twelve\|glossary §12\|UNRESOLVED" designs/ canon/ references/` and fix any external cross-references to the renumbered glossary parts.
3. B1 fix — re-run Mode G with `re.IGNORECASE`; patch `mode_g_2026-04-30.json`; append disclosure note to audit folder's `01_methodology.md` §3 + `02_weakness_register.md` §1.1 with corrected numbers if they shift.

Single PP / ED entry covers all three. Class B (parameter correction). Demonstrates the audit-of-audit discipline produces actionable cleanup, not just findings. Builds the pattern that will repeat per phase: produce, audit, repair before extending.

After Phase 0 closes: pause for Jordan ratification of this workplan. Adjust scope, sequencing, or deliverables before Phase 1 begins.

---

## §10 Workplan governance

**This file is itself an artefact governed by the system it describes.**

- **Status:** WORKPLAN (draft pending ratification)
- **Located at:** `designs/audit/2026-04-30-ecosystem-workplan/00_workplan.md` (proposed; subject to placement decision)
- **Version policy:** rewrites land as new dated workplan files; this file is not edited in place after ratification.
- **Cross-references:** `designs/audit/2026-04-30-terminology-vector-audit/02_weakness_register.md` (this session's audit deliverable, referenced by §1.3); `canon/patch_register_active.yaml` (PP-691 entry, the trigger); conversation log 2026-04-30 (full context).
- **Ratification:** Jordan reviews workplan, modifies, approves. Approval = commit message stating ratification. Phase 0 may begin same-session or deferred.

---

*Drafted by Claude (claude-opus-4-7) at user direction 2026-04-30. Pending ratification before execution.*
