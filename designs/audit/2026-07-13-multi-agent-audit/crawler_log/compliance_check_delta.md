# Crawler-log delta — compliance_check (2026-07-13 multi-agent audit)

**Instrument just completed:** compliance_check — PASS, exit 0, zero violations of any severity
(`designs/audit/2026-07-13-multi-agent-audit/compliance_check/raw_output.txt`).

**What existed at cross-reference time** (`find designs/audit/2026-07-13-multi-agent-audit -type f`):
- `compliance_check/raw_output.txt` — this instrument's own output. Read in full (3 lines: banner,
  `[COMPLIANCE ✓] All files within thresholds`, done — no per-file token counts printed by the tool
  itself; the specific numbers below come from the compliance_check agent's own summary text and from
  `references/atomization_rules.yaml`, cross-checked directly).
- `crawler_log/vector_audit_delta.md` — the crawler-logger pass for the previous instrument
  (vector_audit, BLOCKED/stub). Read in full; it already logged "no compliance_check cross-reference
  available" against a zero-file inventory. That pass ran before mechanic_audit/module_adjudicator had
  written anything — this pass now has both, so the picture is fuller.
- `mechanic_audit/` — 6 subsystem folders, each with 5 files. Complete. Read all 6
  `gap_register_update.md` in full; grepped `formula_audit.md`/`core_principles_audit.md`/
  `number_systems_audit.md` across all 6 subsystems for hits on the compliance-relevant filenames
  (`module_contracts.yaml`, `values_master.yaml`, `mechanical_terms_index.md`, `coverage_matrix.md`).
- `module_adjudicator/` — 4 files, complete (`module_flowchart.mermaid`, `state_graph.mermaid`,
  `module_map_flat.md`, `verdict_full_graph.md`). Read `module_map_flat.md` and `verdict_full_graph.md`
  in full.
- `vector_audit/00_status.md` — BLOCKED/stub, no analytic content (confirmed by reading it and by the
  prior crawler-log pass); nothing to cross-reference from vector_audit's own output.

---

## 1. Convergent evidence (three instruments, one file): `references/module_contracts.yaml`

This is the highest-value finding this round — the same file is independently implicated by all three
other instruments that have produced content, from three genuinely different angles, and the angles
compound into a real forward risk rather than three unrelated observations:

- **compliance_check (this instrument)** spot-checked `module_contracts.yaml` at **14.4k / 18k tokens**
  (80% of cap) — comfortably passing today, but flagged its own **severity-classification bug**: CI
  mode's inline logic only treats `on_exceed` values in `{flag_unknown_pattern, flag_for_split,
  flag_for_next_session}` as warn-tier; `module_contracts.yaml`'s actual policy in
  `references/atomization_rules.yaml:251-254` is **`on_exceed: "warn_only"`**, which is NOT in that
  treated-as-warn set — meaning if this file ever crosses 18k tokens, CI mode's inline logic falls
  through to **error severity** (exit 1, blocking merge to `main` per CLAUDE.md §8), contradicting the
  file's own explicitly-authored "raise the cap, don't block on it, this file is expected to grow" intent
  recorded right next to the policy (`atomization_rules.yaml:254`: "expected to grow, not shrink, as
  those gaps get filled").
- **module_adjudicator** (`module_adjudicator/module_map_flat.md:3`) names this exact file as its
  **source of truth** ("REGENERATE, never hand-edit") for the entire 27-module graph this run just
  produced, and its own remediation queue in `verdict_full_graph.md` (P1-A, P2-A, P3-A, P3-B — lines
  149-153) queues **four separate edits into this same file**: removing a spurious
  `scene_outcome.battle_concluded` emit, propagating ED-1038 §12 transitions, wiring a consumer for
  `env.crisis`, and reconciling an npc_behavior↔social_contest loop annotation. Every one of these is
  additive or structural content landing in the file compliance_check just measured at 80% of cap.
- **mechanic_audit** (`mechanic_audit/social_contest/gap_register_update.md:27`, GAP-13/G-13)
  independently found, from the content-correctness side rather than the structural or size side, that
  `module_contracts.yaml` L425-447 (the `social_contest` entry) is **stale** — it predates the Stage
  1b-3 δσ-substrate rebuild and still reads `resolver: dice_pool`. Filed P2, already tracked
  (`ED-SC-0008`), status "No action — already tracked" — but a live fix for that gap is itself another
  future edit destined for the same file, on top of module_adjudicator's four.
- **Cross-reference:** three independent axes (a documented severity-classification bug in
  compliance_check's own CI-mode logic; a structural remediation queue module_adjudicator authored
  against the file this very run; and a content-staleness gap mechanic_audit found in the file
  independently) all converge on one file that is (a) explicitly designed to keep growing per its own
  atomization-rules note, (b) sitting at 80% of its cap today, and (c) has at minimum 5 known pending
  edits queued against it from this run's own two other instruments. None of this is a violation
  today — compliance_check correctly reported PASS — but it is a specific, named, near-term collision:
  the next time someone lands module_adjudicator's P1-A/P2-A/P3-A/P3-B fixes plus mechanic_audit's
  ED-SC-0008 fix into this file, growth toward 18k is plausible, and if it crosses that threshold the
  misclassification bug this instrument itself flagged would turn a designed-to-be-tolerated warn into
  an unexpected CI-blocking error. **Recommended action for the synthesis pass:** either (i) file an ED
  to fix compliance_check's `on_exceed` severity-set to include `warn_only`/`flag_for_manual_archive`
  (compliance_check's own finding #3, IN lane), or (ii) flag `module_contracts.yaml` specifically for a
  cap increase ahead of the queued edits landing, before relying on CI to stay green through this
  file's next growth cycle.

## 2. No other compliance-relevant convergence found

- Grepped all 6 `mechanic_audit` subsystem folders for `values_master.yaml`, `mechanical_terms_index.md`,
  and `coverage_matrix.md` (the other three largest warn/flag-tier files compliance_check spot-checked:
  34.6k/50k, 33.3k/40k, 8.9k/10k respectively) — **zero matches**. No subsystem audit this run reads or
  flags those files as hard to reason about, needing decomposition, or otherwise notable. Stating this
  plainly rather than manufacturing a connection: as of this pass, `module_contracts.yaml` is the only
  file compliance_check's spot-check set overlaps with content the other two finished instruments
  actually touched.
- `module_adjudicator` output was also grepped for `values_master`/`mechanical_terms_index`/
  `coverage_matrix` — zero matches.
- `vector_audit/00_status.md` is a pure BLOCKED status report (confirmed by direct read and the prior
  crawler-log pass) — it contains no file-size, vocabulary, or citation-graph content to cross-reference
  against compliance_check's size-policy findings at all.

## 3. Note on compliance_check's own scope gap (finding #1) vs. what's visible so far

compliance_check's finding #1 — that CI mode never runs `_check_index` (missing/stale doc-index) or
`_check_archive_pressure` — is a real scope gap in this instrument, but nothing in mechanic_audit's or
module_adjudicator's finished output this round exercises doc-index staleness or archive pressure in a
way that lands a concrete missed-catch example (that class of defect is closer to vector_audit's job,
and vector_audit is blocked/stub this run — already logged in the prior crawler-log pass under "blind
spot," not duplicated here).

---

**Governance-file discipline:** this delta note is analysis-only, written solely to
`designs/audit/2026-07-13-multi-agent-audit/crawler_log/compliance_check_delta.md`. No writes were made
to `audit_registry.jsonl`, `editorial_ledger*.jsonl`, or `id_reservations.yaml` — those remain reserved
for this run's dedicated sequential registry step.
