# Propagation Map Archive — Batch 2026-05-01 (b)
# Archived from references/propagation_map.md to maintain size limits.

## 2026-04-19 — PP-674 Framework enforcement + Necessity tier (N)

**Commit:** (this commit)
**Scope:** make the vetting framework a mandatory validation tool; add tier N (Necessity) above Ω.

**Framework changes (references/throughlines_meta.md, references/throughlines_meta_infill.md):**
- New tier N (Necessity Test) above Ω. Tests whether a proposal models a load-bearing Renaissance-era political-leadership dynamic.
- N-level questions (5) added to skeleton §0.
- 4 new Failure Lexicon terms: fantasy imposition, duplicate coverage, edge case mechanic, abstractable.
- Vetting protocol (§8.1) updated: Class A/B begin with N-check.
- §8.5 added: enforcement specification — required vetting: block schema for Class A/B patches.
- Authority table: N owned by Jordan (subject-matter authority).
- Infill §10 added: tier N rationale, worked examples, what counts as subject grounding.
- Infill §11 added: enforcement mechanism, vetting: block schema, self-validation of PP-674.

**Ecosystem enforcement (skills/valoria-orchestrator/scripts/valoria_hooks.py):**
- New function: vetting_gate(additions) — validates Class A/B patch register entries from PP-674 forward have vetting: blocks with required keys (class, necessity, omega, mu, m_ratings, q).
- vetting_gate wired into pre_commit_gate — fires on every commit that touches canon/patch_register_active.yaml.
- New task type: design_proposal — requires references/throughlines_meta.md in context before proposing mechanics.
- Grandfathering: entries with pre-framework: true exempt. PP-001..PP-673 implicit-grandfathered (no new entries before PP-674 need retroactive markers; only new entries are checked).

**Registers:**
- canon/patch_register_active.yaml: PP-674 entry (self-validating — includes own vetting: block, class A, infrastructure note).
- canon/editorial_ledger.yaml: ED-720.
- references/canonical_sources.yaml: enforcement note.

**Consequences:**
- All future Class A/B gameplay proposals will carry permanent vetting records in the patch register.
- Pattern-detection across vetting records becomes possible (are certain М's consistently violated? are N failures flagged but merged anyway?).
- Framework is no longer advisory — it is procedurally enforced.
- Substantive framework compliance (correct M ratings, accurate N judgments) still requires Jordan's review; the gate catches only procedural violations.

## Stage 4 Provisional Promotions (2026-04-25)

33 PROVISIONAL patches added to `archives/patches/patch_register_archive_stage4_promotions_2026_04_25.yaml`. Propagation status: **pending review**.

These entries were promoted from MENTIONED-in-canon-corpus state (atom references in `references/atoms_pending/2026-04-25/`) to formal register entries. Each requires manual review of:
- `finding_id` field (auto-extraction couldn't infer)
- `affects` list (derived from canon_mentions; may need refinement)
- `description` wording (auto-extracted from atom contexts, may be approximate)
- Reconciliation against actual implementation status (some patches may already be applied)

Until reviewed, these PROVISIONAL patches should not drive propagation cascades. They are visible in the register for discoverability only.

## PP-675 Terminology Conversion Workplan (2026-04-29)

PROVISIONAL workplan: retire framing terms (TTRPG/BG/Hybrid) and Hybrid-as-third-mode. Preserve mechanical vocabulary (dice pool, TN, Ob, exchange, degree of success, pool formulas).

**Source doc:** `designs/audit/2026-04-29-terminology-conversion/00_workplan.md`
**Status:** PROVISIONAL — pending Jordan signoff on 5 decisions in workplan §4.

**Propagation status:** **NOT STARTED.** No source-doc edits begin until Jordan resolves §4 decisions and PP-675 promotes from PROVISIONAL → APPLIED. Phase 1 of the workplan creates `references/terminology_canon.md` as authority; Phase 2 builds `references/terminology_sweep_inventory.md` enumerating every legacy-term occurrence by file; Phase 3 propagates by directory cluster (architecture first, archives skipped); Phase 4 adds `terminology_gate` to `safe_commit` to make conversion permanent; Phase 5 updates project-level files (project knowledge instructions block, hook docstrings, SKILL.md files).

**Single load-bearing structural change (workplan §3):** `scale_transitions_v30 §1, §6` rewritten from three-mode (TTRPG/BG/Hybrid) to two-mode (Strategic/Scene) plus Zoom-In as transition verb. Engine already runs on a binary Strategic/Scene state machine; three-mode framing was textual, not implementation. No gameplay behavior change.

**Cross-references:** ED-759.

## PP-676 Topographic Analysis Workplan (2026-04-29)

PROVISIONAL workplan: vectorized corpus investigation as analytic instrument for surfacing weaknesses unreachable by hand-curation.

**Source doc:** `designs/audit/2026-04-29-topographic-analysis/00_workplan.md`
**Status:** PROVISIONAL — pending Jordan signoff.

**Propagation status:** **NOT STARTED.** No execution begins until PP-676 promotes to APPLIED and §8 pre-execution checklist is satisfied (dedicated session, v2 connections audit landed, canonical_sources pruned, index-routing bypass tested).

**Distinct from connections artifact:** the connections artifact draws topology from a designer's hand. Topographic analysis derives topology from the corpus via TF-IDF + cosine similarity. Diagnostic value highest in the gap between the two views.

**Cross-references:** ED-760. Companion to v2 connections audit (separate session).

## PP-676 Topographic Analysis — Stage 1-4 Executed (2026-04-29)

Stages 1-4 of the topographic analysis workplan executed in same chat session per Jordan directive.

**Outputs:**
- `designs/audit/2026-04-29-topographic-analysis/02_weakness_register.md` — narrative findings (12 TOPO entries)
- `designs/audit/2026-04-29-topographic-analysis/data/tokens.json` — 126 curated tokens with surface forms, doc counts
- `designs/audit/2026-04-29-topographic-analysis/data/layout.json` — t-SNE 2D coordinates
- `designs/audit/2026-04-29-topographic-analysis/data/neighbors.json` — top-8 cosine neighbors per token
- `designs/audit/2026-04-29-topographic-analysis/data/diagnostics.json` — D1-D6 raw diagnostic outputs
- `designs/audit/2026-04-29-topographic-analysis/data/cross_doc.json` — doc-level Jaccard graph + v1 edge recheck

**Findings status:** PROVISIONAL pending Jordan review. Each TOPO finding may convert to an ED entry on signoff.

**Three convergent observations:**
1. Knot system more central than v1 portrayed — high jaccard with Social Contest, Leap, Combat, Domain Echo. **v2 should re-elevate.**
2. Political-dynamics layer (Armature, Domain Action, Concern, etc.) entirely degree-0 — confirms PROVISIONAL status of 12_development_specification.md numerically.
3. Several v1 hand-curated edges are genuinely-thin (cosine<0.05 AND jaccard<0.10): Threadwork↔MS Trajectory, Royal Assassination↔NPC Behavior, Fractional Province↔Faction Layer. These are real propagation gaps, not measurement artifacts.

**Methodology limits explicit:** TF-IDF cosine measures co-mention; doc-level Jaccard measures shared territory; hand-curated edges encode causal/functional logic. The diagnostic value is in the disagreement between the three lenses. Future iterations should refine surface-form coverage (Stealth, contest styles undermatched) and consider section-level granularity.

**Cross-references:** ED-760, PP-676.

