# Valoria Ecosystem Workplan v2 — 2026-04-30

STATUS: WORKPLAN
VERSION: 2 — supersedes ecosystem_workplan_2026-04-30.md
DRAFT: 2026-04-30
AUTHORITY: Pending Jordan ratification.

CHANGES FROM v1:
- Phase 1 split into two-layer design (JSON Schema structural + custom referential); estimate 2 directives.
- Phase 2 corrected: "finalizes" taxonomy changed to "proposes"; V4 resolution required before Phase 5 can be scoped.
- Phase 2.5 added: data migration (existing records → schema-compliant). Missing in v1.
- Phase 4: shadow-mode adapter added as deliverable; transactional-commit pattern specified; acquire_id mechanism specified.
- Phase 5: exit criterion corrected (differ-from-reference-by-disclosed-Δ, not match); per-commit structural check vs full audit cadenced.
- Phase 6 split into 6a (enforcement), 6b (tests), 6c (CI + observability).
- Phase 7: time-based criterion added (30 real-world days); N defined (≥ 10 commits clean).
- Connectivity matrix corrected: Ph3→Ph5 and Ph2→Ph6 edges added.
- Effort revised from 8–13 to 17–20 directives.
- Self-audit added as §II (best practices + long-term project health).

---

# PART I — IMPROVED WORKPLAN

---

## §0 Executive summary

Three P0 defects from this session's commits require immediate repair (Phase 0). Beyond those, the path forward is an 8-phase infrastructure rebuild — not because the current system is broken, but because it has accumulated enough structural debt (8 registers with hand-maintained referential integrity; no schema validation; no idempotency guarantees; no reproducible audit pipeline) that the cost of that debt now compounds faster than the cost of addressing it.

Total revised effort: **17–20 directives** (~4–5 weeks dedicated dev, or proportionally more part-time). Phase 7 (full cutover) is conditional — the system delivers most of its value at Phase 6 and cutover should only happen when real-world use validates the new primitives.

Critical path: Ph0 → Ph1 → Ph2 → Ph2.5 → Ph3 → Ph4 → Ph6a → Ph6b → Ph6c → Ph7. Ph5 runs in parallel with Ph4 after Ph3 completes.

---

## §1 Current state (unchanged from v1)

### §1.1 This-session commits

| SHA | What | Status |
|---|---|---|
| `eae4eb0b6` | `designs/audit/2026-04-30-terminology-vector-audit/` | applied |
| `157523f2d` | PP-691 / ED-772 — terminology P0 propagation pass | applied |
| `7cf88ce6a` | `designs/audit/ecosystem_workplan_2026-04-30.md` (v1 workplan, draft) | applied |

### §1.2 P0 cleanup queue

| ID | Description | Cost |
|---|---|---|
| T1 | `npc_behavior_v30.md` priority-tree branches gate on CI ≥ 75, which ci_political_v30 §2.1 removed. | 30 min |
| D1 | Glossary renumbering (old Parts 11/12 → 12/13) may have broken external cross-refs. | 10 min grep + fix |
| B1 | Mode G context filter case-insensitivity bug. `mode_g_2026-04-30.json` incorrect. | 15 min re-run + patch |

### §1.3 Live register health

- `patch_register_active.yaml`: 33 PP entries; PP-689 gap (reserved SHA followup).
- `editorial_ledger.yaml`: `next_id: 773`; hit 90.9% of 2,000-token health threshold.
- `propagation_map.md`: ~52k chars; near 80% of 15k-token threshold.
- `canonical_sources.yaml`: 263 lines of "Last touched" comments; accumulation without pruning.

---

## §2 Findings inventory

### §2.1 Inherited from v1 (unchanged — see v1 §2.1 / §2.2 for full tables)

Content findings: 17 across directions (T/B/V/D/L/H prefixes).
Code findings: 30 across categories (A/B/C/D/E/F/G/H prefixes).
After dedup: ~38 distinct underlying defects.

### §2.2 Findings from code review of v1 workplan (new)

| ID | Severity | Phase affected | Finding |
|---|---|---|---|
| W1 | P1 | Ph1 | JSON Schema cannot enforce "path-must-exist" / "foreign-key-must-resolve" — requires two-layer validator |
| W2 | P1 | Ph1 | Validator without enforcement path until Ph6 is advisory-only; not acknowledged in v1 |
| W3 | P1 | Ph2 | Taxonomy "finalized" before empirical test (Ph3); sequencing inverted |
| W4 | P1 | Ph2 | V4 conflict (live-state contradicts methodology lock-in) described but not resolved |
| W5 | P1 | Ph3 | Atom ID naming convention unspecified |
| W6 | P1 | Ph3 | Verification semantics for `atom_verifications.jsonl` underspecified |
| W7 | P1 | Ph3 | 80% mapping exit criterion has undefined denominator |
| W8 | P1 | Ph4 | `transactional_commit()` pattern unspecified (in-memory / branch / best-effort) |
| W9 | P1 | Ph4 | Shadow-mode adapter not in Ph4 deliverables |
| W10 | P1 | Ph4 | `acquire_id()` conflict detection mechanism unspecified |
| W11 | P1 | Ph5 | Exit criterion requires output to match 2026-04-29 reference — wrong (corpus has changed) |
| W12 | P2 | Ph5 | "Full audit per commit" will hit GitHub API rate limits |
| W13 | P2 | Ph6 | `mypy --strict` from dynamically typed codebase is 20–30% of Ph6 effort; not acknowledged |
| W14 | P2 | Ph6 | "Implement or remove" dead references is an unresolved design decision, not a bullet |
| W15 | P1 | Ph7 | N for "≥ N commits clean" is undefined; time-based criterion from risk register not in exit criteria |
| W16 | P1 | All | Missing Phase 2.5 — data migration |
| W17 | P2 | All | Missing rollback plan if Ph4 shadow mode reveals unresolvable divergence |
| W18 | P2 | matrix | Ph3 → Ph5 dependency missing from connectivity matrix |
| W19 | P2 | matrix | Ph2 → Ph6 dependency missing from connectivity matrix |

---

## §3 Logic for approach — updated

### Six engineering principles (unchanged from v1)

P-1: Repair before extend. P-2: Diagnose before treat. P-3: Backfill before evolve.
P-4: Shadow before cutover. P-5: Reproducibility before scale. P-6: Bottom-up sufficiency.

### Four additional principles from code and best-practices review

**P-7: Contract before implementation.** Interface specifications (typed function signatures, pre/post conditions) are written in Phase 2 ecosystem audit before Phases 3/4 implement them. "Design on paper first" is not process overhead — it's the mechanism that makes shadow-mode diffs meaningful.

**P-8: Test before enforce.** Tests cover every enforcement rule (positive and negative) before the enforcement hook goes live. Line coverage is the wrong metric; rule coverage is the right one. Phase 6a (enforcement) requires 6b (tests) to complete before enforcement is considered stable.

**P-9: Observe before tune.** The system should run in a read-and-report mode (Phase 1) long enough to produce baseline metrics before any enforcement gate is added. Enforcement before baseline = blind thresholds.

**P-10: Proportionality.** Every layer of governance must justify its existence against the project's scale (current: 1 primary author, 47 design docs, 1 Godot repo). If a layer's complexity exceeds its marginal benefit relative to "just use git," remove it. Apply this test explicitly at each Phase decision point.

---

## §4 Phases (revised)

### Phase 0 — Outstanding P0 cleanup (1 directive)

**Scope:** Fix T1 (NPC behavior threshold stale), D1 (glossary cross-refs), B1 (Mode G bug).

**Deliverables:**
- `npc_behavior_v30.md`: add `[STALE-THRESHOLD: see ci_political_v30 §2.1]` markers on `CI < 75` / `CI ≥ 75` branches. Design-judgment update to canonical probabilistic thresholds deferred (non-trivial branch logic change; must be authored, not mechanic-swept).
- Corpus grep: `grep -rn "Part Twelve\|Part Eleven\|glossary §12\|glossary §11\|UNRESOLVED" designs/ canon/ references/ params/`; fix broken cross-refs.
- Mode G re-run with `re.IGNORECASE` on context patterns; update `mode_g_2026-04-30.json`; append disclosure note to audit folder `01_methodology.md` §3 and `02_weakness_register.md` §1.1.
- Single commit: PP-692 / ED-773.

**Exit criteria:** All 3 P0s resolved. Audit folder updated with methodology note.

**Effort:** 1 directive.

---

### Phase 1 — Schemas + advisory two-layer validator (2 directives)

**Scope:** JSON Schema for all 8 registers (structural). Custom referential validator (cross-file). Advisory-only — no enforcement gate.

**Two-layer design:**
- Layer A (JSON Schema): types, required fields, format constraints (`PP-\d+`, ISO dates, enum values). Runs offline via standard jsonschema library. Fast.
- Layer B (custom validator): cross-file referential integrity — `affects:` paths exist, `source:` PP-ids resolve, `next_id:` values are consistent. Runs as `valoria validate`. Slower; network-dependent.

**Deliverables:**
- `schemas/` directory: 8 schema files (one per register; each schema includes both Layer A definition and Layer B rule declarations in `x-referential-checks:` extension field).
- `skills/valoria-validate/scripts/validate.py`: CLI running both layers; outputs structured violation report (JSON + human-readable).
- Violation baseline committed: `designs/audit/{date}-schema-validation-baseline/02_findings.md` — actual violation counts by severity and register.
- **Explicit advisory notice** in baseline report: "Validation is advisory until Phase 6a. Violations above this baseline must be tracked but do not block commits."

**What stays out of Phase 1:** Enforcement. `mypy`. CI. Those are Phase 6.

**Phase 1 decision gate:** After baseline report, Jordan decides whether the violation count / pattern distribution supports atom-first design or suggests a simpler path (P-10 proportionality check).

**Effort:** 2 directives. Directive 1: 8 schemas + Layer A. Directive 2: Layer B referential validator + CLI + baseline report.

---

### Phase 2 — Ecosystem audit (E1-expanded) (2 directives)

**Scope:** Comprehensive inventory of hooks, skills, registers, conventions, naming, identifier-numbering, document-category taxonomy, commit primitives, integration concept. Produces *proposed* (not final) atom taxonomy and a V4 design-decision.

**Deliverables:** dated audit folder `designs/audit/{date}-ecosystem-audit/`:
- `00_workplan.md`, `01_methodology.md`, `03_validation_report.md` (standard structure).
- `02_weakness_register.md` — 10 sections (see v1 §4 Phase 2 for section list). Critical additions:
  - §9 must include: explicit mapping of proposed atom categories to existing register fields (V3 resolution).
  - §10 must include: **a design decision on V4** — which of the following: (a) live vector_state directory, continuously updated per atom-category rules; (b) snapshot-only (dated audit folders), no live state; (c) hybrid (lightweight live token-list only, full graphs on cadence). Pick one, document rationale, this decision unblocks Phase 5.
  - §11 (new): **Contract specifications** — typed function signatures, pre/post conditions for `propagate()`, `acquire_id()`, `AtomStore.record()`, `PatchRegister.append()`. These are the Phase 4 implementation contracts.

**Taxonomy status:** PROPOSED. Explicitly labeled "pending Phase 3 empirical validation." Phase 2 exit does NOT finalize taxonomy.

**Effort:** 2 directives. Directive 1: §§1-5 (hooks, skills, registers, conventions, identifiers). Directive 2: §§6-11 (taxonomy, primitives, integration, contracts).

---

### Phase 2.5 — Data migration (1 directive)

**Scope:** Migrate existing non-compliant register records to schema-compliant format. This is the gap v1 had between "surface violations" (Phase 1) and "enforce compliance" (Phase 6).

**Why this is its own phase:** Schema adoption without migration produces a two-tier system (old records invalid, new records valid) that the validator can never be clean about. Every new commit will show N baseline violations from legacy records. This undermines the baseline's signal value and produces false noise in the Phase 1 violation report.

**Deliverables:**
- Script: `skills/valoria-validate/scripts/migrate.py` — reads each register, applies schema-compliant transformations, writes back. Idempotent (run twice = same output as run once). Dry-run mode.
- Migration run on all 8 registers; commit resulting changes.
- Post-migration validation run; violation count should drop to structural-debt-only (path-not-found type, not format-error type).
- `canonical_sources.yaml` "Last touched" comments pruned: move to a separate `canonical_sources_history.yaml` (solves H1 finding).

**Effort:** 1 directive.

---

### Phase 3 — Atom store + retroactive decomposition (2 directives)

**Scope:** Implement typed atom store with specified ID convention. Retroactively decompose 3 historical PPs. Taxonomy finalization.

**Atom ID convention (specified):** `A-{PP_ID}-{SEQUENCE_TWO_DIGIT}` where SEQUENCE is zero-padded two-digit integer within the commit, e.g. `A-PP691-01`, `A-PP691-02`. Generated at decomposition time. Idempotent: if `A-PP678-01` exists in the store, re-decomposing PP-678 replaces it (keyed by atom ID, not appended). This allows taxonomy refinement to produce updated backfill without duplication.

**Verification semantics (specified):** `atom_verifications.jsonl` is populated by the Phase 5 audit pipeline (not Phase 3). Phase 3 writes predictions; Phase 5 writes verifications. Phase 3 exit criterion does NOT require verifications to exist — only predictions.

**Exit criterion (corrected):** Each of the 3 historical PPs (PP-678, PP-690, PP-691) must decompose with ≥ 75% of atoms mapping cleanly to taxonomy **per PP** (not aggregate). A clean mapping means: the atom's category has defined co-touch rules that were either satisfied or explicitly documented as deferred.

**Deliverables:**
- `references/atom_store/atoms.jsonl`, `atom_predictions.jsonl`, `atom_verifications.jsonl` — with schemas.
- `valoria atom` CLI: `add`, `list`, `verify`, `decompose {PP_ID}`.
- Backfill: PP-678, PP-690, PP-691 decomposed.
- **Taxonomy finalization report** — output of the backfill empirical test. Where taxonomy held, where it failed, what changed. This is the Phase 2 taxonomy's empirical verdict.

**Effort:** 2 directives.

---

### Phase 4 — `propagate()` primitive in shadow mode (3–4 directives)

**Scope:** Typed commit primitive, shadow mode with adapter, atomic ID acquisition.

**Transactional commit pattern (specified — option A: in-memory staging):** All file mutations computed in memory before any disk write. Single git push at end. No mid-commit dirty state. Failure before push = clean abort. Failure after push = git revert on the next session. This is the safest pattern for a single-author context; it doesn't require branch management or lock files.

**`acquire_id()` conflict detection (specified):** Read-modify-write via git optimistic concurrency. Sequence: (1) read live `next_id`, (2) increment, (3) attempt push with pre-condition that the file SHA matches what was read. GitHub API's `PUT /contents` with `sha` parameter provides this. If SHA mismatch (someone else pushed between read and write), retry from step 1. For single-author context, collision probability is near-zero; but the mechanism is correct regardless.

**Shadow-mode adapter (added to deliverables):** Converts `Directive(atoms=[...])` to `(additions, deletions, message)` format for `safe_commit`. Enables apples-to-apples comparison. Adapter is a first-class deliverable; it's the bridge between old and new primitives and must be correct before the diff is meaningful.

**Deliverables:**
- `propagate()` primitive with typed `Directive`, `Atom`, `CommitResult` dataclasses.
- `safe_commit_adapter(directive: Directive) -> (additions, deletions, message)`.
- `acquire_id()` with optimistic-concurrency retry.
- Shadow-mode runner; report after ≥ 3 commits.
- Phase 4 rollback policy: if shadow-mode finds an unresolvable divergence after 5 commits, document the divergence class as a known limitation and defer cutover indefinitely. `safe_commit` remains supported. This is the explicit rollback path v1 was missing.

**Effort:** 3–4 directives.

---

### Phase 5 — Vector audit reproducibility (2 directives)

**Scope:** Port ad-hoc pipeline into `valoria_audit.py` proper. Cadenced CI.

**Exit criterion (corrected):** Re-run of the full pipeline against today's corpus should produce:
- Token list: same as v3 (corpus stable except PP-691 / PP-690 changes).
- G_cite: P3 property still passes (≥ 100 edges). Specific edge counts may differ due to corpus changes.
- Mode G: corrected counts per Phase 0 B1 fix.
- Validation: P1 corrected pass, P2 fail (still expected — Convictions throughline anchoring not fixed), P3 pass.
- Crucially: the output is **documented to differ** from 2026-04-29 reference in specific ways attributable to intermediate commits. Not "matches reference" — "differs by the documented Δ."

**V4 design decision implementation:** Whatever Phase 2 decided (live-state, snapshot-only, or hybrid), Phase 5 implements it. If hybrid: `references/vector_state/tokens.json` maintained as lightweight live list; full graphs on cadence.

**CI cadence:** Full audit runs once per day (scheduled GitHub Action) OR on manual trigger. Per-commit: structural check only (token count, P3 edge count, Mode G top-term count). Not full audit per commit.

**B1 fix in code:** Mode G context patterns compiled with `re.IGNORECASE` in the canonical script.

**Effort:** 2 directives.

---

### Phase 6a — Enforcement on existing rules (1 directive)

**Scope:** Deploy schema-based hook enforcement using Phase 1 schemas. No new rules — existing rules only, now schema-driven. This is the narrowest possible enforcement step.

**Deliverables:**
- `valoria_hooks_v2.py` — schema-driven, replaces hand-written co-file rules with Layer A/B validator calls.
- All existing enforcement rules verified against Phase 6b tests before going live.
- Advisory-to-enforcement migration note: violation baseline from Phase 1 defines the starting state; any violation that existed in the baseline is grandfathered (not blocking) until Phase 2.5 migration cleaned it.

**Effort:** 1 directive.

---

### Phase 6b — Test harness (1–2 directives)

**Scope:** Every enforcement rule has a positive test (valid input passes) and a negative test (invalid input fails). `mypy` applied to new code only (not legacy codebase). Coverage metric is rule coverage, not line coverage.

**Deliverables:**
- `tests/` directory with fixture register files.
- Per-rule test: every rule in `valoria_hooks_v2.py` has at least 1 positive and 1 negative test.
- `mypy`: applied to `valoria_hooks_v2.py`, `validate.py`, `migrate.py`, `propagate.py`, `atom_store.py`. Not retroactively applied to old code.
- Dead references resolved: `doc_index_gen` and `freshness_gate` — this is the Phase 2 design decision's implementation. If implement: separate micro-tasks defined. If remove: call-site cleanup only.

**Effort:** 1–2 directives.

---

### Phase 6c — CI + observability (1 directive)

**Scope:** GitHub Actions CI running validator + tests. Structured hook logging. Register-growth metrics.

**Deliverables:**
- CI workflow: `valoria validate` (Layer A + B) + test suite. Runs on push. Advisory-only on main; blocking on PRs if team grows.
- Structured logging: hook failures write to `references/hook_log.jsonl` (append-only; schema-validated). Replaces stderr-and-forget.
- Metrics: `references/register_metrics.yaml` updated on each CI run with: PP count, ED count, token count, G_cite edge count, validation violation count. Time-series via git history.
- Register archival trigger: when `patch_register_active.yaml` exceeds 14k tokens, CI emits a warning. Archival is a separate directed operation, not automatic.

**Effort:** 1 directive.

---

### Phase 7 — Full cutover (conditional)

**Scope:** `safe_commit` deprecated. `propagate()` is sole path.

**Exit criteria (strengthened):**
- ≥ 10 commits via `propagate()` in production (not shadow mode) without rollback.
- ≥ 30 real-world days of using `propagate()` on actual session commits.
- CI green across all Phase 6c checks.
- No outstanding P0 or P1 against the new pipeline.
- Jordan explicitly ratifies cutover via a commit whose message contains `[CUTOVER] ratify propagate() as sole commit primitive`.

**Effort:** 1–2 directives.

---

## §5 Connectivity matrix (corrected)

| ↓ / right → | Ph0 | Ph1 | Ph2 | Ph2.5 | Ph3 | Ph4 | Ph5 | Ph6a | Ph6b | Ph6c | Ph7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ph0** | — | enables clean baseline | — | — | — | resolves B1 | — | — | — | — | — |
| **Ph1** | requires Ph0 | — | informs §3 | triggers migration scope | provides atom schema | provides typed API | provides audit schema | provides hook rules | provides test targets | provides metrics schema | — |
| **Ph2** | — | requires Ph1 | — | scopes migration | scopes taxonomy + finalizes contracts | provides propagate() spec | provides V4 decision | **provides taxonomy for co-touch rules** | provides test scope | scopes CI | scopes cutover |
| **Ph2.5** | — | requires Ph1 | — | — | clean baseline for atoms | — | clean baseline for audit | required for clean enforcement | required for clean tests | — | — |
| **Ph3** | — | uses schemas | finalizes taxonomy | — | — | provides atoms for propagate | **provides atom predictions for verification** | provides atom validation rules | — | — | enables atom-only |
| **Ph4** | — | uses schemas | uses contracts | — | uses atom store | — | uses reproducibility for verification | provides propagate() for enforcement test | provides shadow report | — | becomes sole primitive |
| **Ph5** | — | uses schemas | uses V4 decision | uses clean baseline | uses atom predictions | enables verification | — | enables CI audit step | — | provides metrics baseline | maintained |
| **Ph6a** | — | requires Ph1 schemas | requires Ph2 taxonomy | requires Ph2.5 clean | requires Ph3 atom validation | — | — | — | requires Ph6b tests | — | — |
| **Ph6b** | — | uses schemas | uses Ph2 contracts | — | — | uses propagate() spec | — | tests Ph6a rules | — | — | — |
| **Ph6c** | — | uses schemas | — | — | — | — | uses Ph5 metrics baseline | requires Ph6a live | requires Ph6b tests | — | required |
| **Ph7** | — | — | — | — | — | requires shadow validated | — | — | — | requires CI green | — |

**Critical path:** Ph0 → Ph1 → Ph2 → Ph2.5 → Ph3 → Ph4 → Ph6a → Ph6b → Ph6c → Ph7.
**Parallel track:** Ph5 runs after Ph3; parallelizable with Ph4 from Ph3 onward.

---

## §6 Decision points (updated)

| After | Decide |
|---|---|
| Ph0 | Proceed to Ph1, or defer infrastructure for N directives to address gameplay backlog (T3 concern). |
| Ph1 | P-10 proportionality check: does violation count/pattern support the full Ph2-Ph7 stack, or suggest a simpler path (fix ID acquisition + schema 2 registers + stop)? |
| Ph2 | Ratify atom taxonomy (proposed). Ratify V4 design decision. Ratify contract specifications. These three decisions unblock Ph3/Ph4/Ph5 respectively. |
| Ph2.5 | Verify migration cleaned the baseline to structural-debt-only. If not, identify which legacy records are non-migratable and explicit-grandfather them. |
| Ph3 | Taxonomy finalization verdict: did ≥ 75% per-PP decompose cleanly? If not, revise taxonomy and re-decompose before Ph4. |
| Ph4 | Define cutover criteria for Ph7 (ratify N=10, 30-days). Assess shadow-mode adapter effort; consider whether adapter itself reveals the need for a simpler primitive design. |
| Ph5 | V4 implementation verdict: was the live-vs-snapshot decision correct? If hybrid live-state causes unexpected complexity, revert to snapshot-only. |
| Ph6b | "Implement or remove" dead references decision: `doc_index_gen` and `freshness_gate`. Either scope the implementation or scope the cleanup. |
| Ph6c | Assess whether CI is blocking or advisory. If the project scales to collaborators, blocking CI becomes critical; solo-author context, advisory is acceptable. |
| Ph7 | Final cutover gate. Jordan's explicit ratification commit required. |

---

## §7 Risk register (updated)

| Risk | Severity | Phase | Mitigation |
|---|---|---|---|
| P0 defects compound before Phase 0 | Critical | 0 | Fix same-session or immediately. |
| Phase 1 advisory-only enables violation drift | High | 1–6 | Publish baseline; track delta from baseline on every commit; flag regressions in Phase 6c metrics. |
| Taxonomy wrong after Phase 2 (empirical test fails) | High | 2–3 | Phase 3 backfill is the test; if ≥ 1 PP fails, taxonomy revision required before Phase 4. Rollback = revise Phase 2 taxonomy section, re-scope Phase 3. |
| Shadow-mode unresolvable divergence | High | 4 | After 5 commits with divergence, document the divergence class as known limitation; maintain `safe_commit` indefinitely. `propagate()` becomes optional, not mandatory. |
| `mypy --strict` scope explosion | Medium | 6b | Apply `mypy` only to new files. Legacy code is `# type: ignore` at module level. Strict typing is a forward-looking constraint, not a retrofit obligation. |
| GitHub Actions rate limits on per-commit audit | Medium | 5–6c | Full audit on schedule/trigger only; per-commit structural check only. Documented in Phase 5 spec. |
| Infrastructure vs. gameplay velocity imbalance | Medium | All | See §II self-audit. Explicit: schedule a gameplay-design directive after every 3 infrastructure directives. |
| Concurrent-session ID collision (until Phase 4) | Medium | 0–3 | Single-session commits only; document limitation. |
| Bootstrap stale-register reads | Medium | All | Always direct-fetch critical registers (patch_register, editorial_ledger) at bootstrap using Contents API with SHA verification, not GraphQL (which may hit cache). |
| Governance system self-referentially corrupted | Low-medium | All | Recovery path: git revert to last known-good state; restart bootstrap from that commit. Document the revert procedure in §10 governance. |
| Phase 7 cutover premature | Low | 7 | Time-based (30 days) + count-based (10 commits) + explicit ratification make premature cutover structurally hard. |

---

## §8 Effort summary (revised)

| Phase | v1 estimate | v2 estimate | Reason for change |
|---|---|---|---|
| Ph0 | 1 | 1 | Unchanged |
| Ph1 | 1 | 2 | Two-layer design; baseline report |
| Ph2 | 1 | 2 | 10 sections + V4 decision + contracts |
| Ph2.5 | — | 1 | New phase |
| Ph3 | 2 | 2 | Unchanged |
| Ph4 | 2–3 | 3–4 | Adapter added; transactional pattern implementation |
| Ph5 | 1 | 2 | CI cadence design; V4 implementation |
| Ph6 (now 6a+6b+6c) | 2–3 | 3–4 | Split into 3 sub-phases; mypy scoped to new code only |
| Ph7 | 1–2 | 1–2 | Unchanged |
| **Total** | **8–13** | **17–20** | ~1.6× increase |

---

---

# PART II — SELF-AUDIT

Best practices and long-term project health perspective. Covers this session's work, the original workplan, and the direction being proposed.

---

## §A Code / engineering best practices

**A1 [P1] — I designed before specifying contracts.** I proposed `propagate()`, `acquire_id()`, `AtomStore.record()` in narrative before writing any interface spec. TDD and contract-first design both say the interface comes before the implementation. I authored implementation details (dataclass fields, retry-on-conflict) without a single function signature. Phase 2 ecosystem audit now includes contract specifications as a required deliverable — but the error was mine in the original design, not just a workplan omission.

**A2 [P1] — I built layer on layer without proportionality checks.** The progression: content audit → terminology checks → vector audit → propagation → repository audit → ecosystem audit → atom taxonomy → vector integration → code architecture → this workplan. Each layer was a reasonable response to what I found, but I never paused to ask: "does the complexity of what I'm proposing match the scale of what we're building?" A P-10 proportionality check earlier would have surfaced that the atom/schema/CI stack may be overbuilt for a solo project.

**A3 [P2] — I didn't distinguish advisory from enforced in Phase 1.** Read-only validators without enforcement are documentation. The v1 workplan implied Phase 1 produced governance; it produced observation. Correctly scoped in v2, but worth naming as an error pattern: "I built reports when I should have built gates (later, once reports are stable)."

**A4 [P2] — I inherited graphs without sampling.** The code review flagged this (V1). More deeply: I made a methodological choice (inherit 2026-04-29 artefacts) and disclosed it in `01_methodology.md`, but did not verify any inherited finding by independent spot-check. The discipline I advocated for (audit, verify, then commit) I didn't apply to my own foundational data. The mode_g_2026-04-30.json case-sensitivity error was a direct consequence.

**A5 [P2] — No incident response procedure documented.** If a commit corrupts a register (ED-762 collision is historical evidence this happens), the recovery path is "grep, revert, re-apply." That's not a procedure; that's improvisation. A brief `references/incident_response.md` (revert to last known-good SHA → verify registers → re-apply intent → document the incident) would cost 30 minutes and prevent a lot of future confusion.

---

## §B Long-term project health

**B1 [P0] — Infrastructure-to-gameplay ratio is out of balance.**

This is the most important finding. The last several sessions have been: vector audit, mass-battle patches, vocabulary-debt propagation, register governance, ecosystem design, this workplan. None of it produces a second of playable Valoria. The Godot repo (`jordanelias/valoria-game`) has minimal activity.

The risk isn't that infrastructure is wrong — it's that the game never ships because infrastructure is always incomplete. Every governance system ever built has one more feature it needs before it's "ready." The disciplines embedded in the PP/ED/atom system serve a game that needs to exist first.

**Recommendation:** After Phase 0, schedule a gameplay-design directive before Phase 1. Not as a deferral of infrastructure, but as a rebalancing signal. If the gameplay directive produces nothing useful without better governance, that's evidence to continue the infrastructure track. If it produces something useful, that's evidence to ship gameplay now and do infrastructure when it hurts.

**B2 [P1] — The register system is growing past proportionality for the project's scale.**

Current state: 8 registers, 33 PPs, 8 EDs, ~52k chars propagation map, 19k alias registry. This is more governance infrastructure than many production SaaS projects. For context: if Valoria were a 5-person game studio with a 200-file Godot codebase, this scale would be appropriate. For 1 primary author + Claude sessions + 47 design docs, it's heavy.

P-10 (proportionality) test applied explicitly: does the atom/schema/CI stack justify its existence? Answer is conditional — **yes if** the project grows to a team or if design corpus grows to 150+ docs. **No if** it remains solo + Claude for the next 6 months. The v2 workplan builds toward a more capable system; the question is whether to build it now or wait for the pain to justify it.

**Honest recommendation:** Phase 1 (schemas + validator) and Phase 2.5 (data migration) are justified at current scale. Phase 3+ (atom store, propagate(), full CI) should be gated on a meaningful project event — either first external collaborator, first playtest session, or first Godot feature shipment. Build those phases when they solve a felt pain, not speculatively.

**B3 [P1] — The `jordanelias/valoria-game` repo has received almost no attention.**

All infrastructure work targets `jordanelias/ttrpg` (design source-of-truth). The Godot implementation repo is essentially empty relative to the design doc volume. The asymmetry matters because the actual product is the game, not the design docs. An ecosystem that governs design docs but has no CI, no structure, and no governance for the implementation repo is an ecosystem that governs the wrong thing.

**Recommendation:** Phase 2 ecosystem audit should explicitly scope `valoria-game` repo health. What's in it? What should be? What governance does Godot code need (GDScript linting, scene graph validation, export checks)? The answer may be "not much yet" — but the audit should make that explicit.

**B4 [P2] — Claude session continuity is a systemic risk that the workplan doesn't address.**

The entire system depends on Claude being able to bootstrap and recover full context. Today's session showed: bootstrap fetched stale registers (H2); skills fetched at runtime without SHA verification (C3); session_log was the primary context-recovery document, and it reflected a session that closed before this conversation's work began.

The workplan proposes better governance of the registers themselves but doesn't address the Claude-session recovery path. If a session crashes mid-commit (which the persistence mitigation rules attempt to prevent), recovery requires: knowing what commit was in progress, what state the registers were in before, and what the intent was. Today, that's in session_log_current.md (which I update at session close, not mid-session) and in the conversation history (which may be lost).

**Recommendation:** Add a `references/session_state.yaml` — a mid-session checkpoint file that records: current directive, atoms in progress, files being edited, last clean commit SHA. Updated every 10 tool calls (alongside `context_gate()`). Costs one tool call per 10; prevents total loss on session crash. Lower-risk and lower-effort than the full Phase 4 primitive.

**B5 [P2] — The SKILL.md orchestration pattern doesn't scale past ~5 skills.**

Currently: `valoria-orchestrator`, `valoria-vector-audit`, and potentially `valoria-validate`, `valoria-audit`, `valoria-atom` (from this workplan). Each skill has a SKILL.md, scripts/, references/. Bootstrap downloads 2 scripts at startup; every new skill adds to bootstrap complexity and to the potential for version skew between what's in the repo and what's cached in `/home/claude/`.

The right answer is a single `valoria` CLI entry point — which Phase 6 proposes. But Phase 6 is 12–16 directives away. In the interim, cap the skill count at 3. `valoria-validate` and `valoria-atom` should be subcommands of `valoria-orchestrator/scripts/valoria.py`, not new skills.

**B6 [P3] — The governance system is designed for Claude-as-operator, not for Jordan-as-operator.**

Every PP entry, ED entry, atom decomposition, and propagation_map entry is written by Claude. Jordan reviews and ratifies. This is a reasonable division of labor given Claude's context-window advantage. But it creates a dependency: if Claude is unavailable or makes a mistake, Jordan cannot easily reconstruct the governance state.

**Recommendation:** At some point, the governance system needs a Jordan-readable summary that isn't 50k chars of YAML. A `references/project_status.md` — updated monthly, human-authored by Jordan with Claude's assistance, ~200 lines — capturing: where the project is, what the last 5 commits did, what's next. A document Jordan could write without Claude's help. Not a substitute for the registers; a complement that reduces bus-factor.

---

## §C Honest assessment of the v1 workplan

**What it got right:**
- Phase structure (0 → 7) with clear earlier-stop-value at every prefix.
- Connectivity matrix — the idea, even if the edges were incomplete.
- Decision points at every phase boundary.
- Risk register.
- "Shadow before cutover" discipline.
- Explicit out-of-scope section.

**What it got wrong:**
- Effort estimates: 1.6× off. This is the most practically consequential error — wrong estimates produce wrong scheduling decisions.
- Taxonomy finalization before empirical test: classic design-then-validate inversion. Should have been validate-then-finalize.
- Phase 2.5 missing: a schema-adoption without migration produces a permanently dirty validator.
- API contracts absent: three complex new primitives designed in prose without a single typed function signature.
- Proportionality check absent: built toward the most capable system regardless of whether it's warranted at current scale.

**The meta-error:** The v1 workplan was produced at the end of a long session in which I'd spent significant context on the work itself. Long sessions produce optimistic estimates and incomplete specs. The right process — which the v2 workplan now follows — is: self-audit first, then produce the spec. I did it in the wrong order. The session as a whole exhibited the same pattern: build, then audit, then rebuild. Correct but inefficient. Top-down (intent → spec → contract → implement → audit) is faster when the spec is correct.

---

## §D What "best practices" actually implies for this project's scale

Best practices are scale-dependent. Some things that are best practices for teams of 5+ are anti-patterns for solo projects:

| Practice | Right at team scale | Right at solo scale |
|---|---|---|
| Full CI with blocking gates | Yes | Advisory-only CI; blocking only for obvious regressions |
| Typed schemas on all data stores | Yes | Typed schemas on high-churn stores only (patch_register, editorial_ledger) |
| 80%+ test coverage | Yes | Test every enforcement rule; no coverage target |
| Formal API contracts before impl | Yes | Typed signatures + docstring; not full OpenAPI-style contracts |
| Atom-first commit taxonomy | Necessary at 3+ concurrent committers | Valuable but not necessary solo; useful as audit tool |
| Atomic ID acquisition with CAS | Necessary at concurrent writers | Useful for preventing drift; not critical solo |
| Full vector audit on every commit | Only with fast pipeline | Never; cadenced (daily/weekly) is correct |

The v2 workplan applies best practices at the right scale. Phase 6c CI is advisory-only. `mypy` applies only to new code. Test coverage is rule-based, not percentage-based. This is the "proportionality" principle (P-10) expressed as a decision table.

---

## §10 Workplan governance

- **Status:** v2 DRAFT — supersedes `ecosystem_workplan_2026-04-30.md`.
- **Located at:** `designs/audit/ecosystem_workplan_v2_2026-04-30.md`.
- **Version policy:** further revisions land as v3, v4, etc. No in-place editing after ratification.
- **Ratification:** Jordan reviews; ratification = a commit message containing `[ratify] ecosystem workplan v2`.
- **Phase 0 may begin before ratification.** T1/D1/B1 fixes do not depend on workplan ratification.

---

*Drafted by Claude 2026-04-30. Incorporates code-developer review of v1 workplan plus best-practices and long-term project health self-audit.*
