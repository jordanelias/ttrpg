# Workplan v2 — Extended Audit (Round 2)
**Generated:** 2026-04-27 · session token `8ca3fffeaca3bb9c`
**Companion to:** `valoria_workplan_v2.md` + `workplan_v2_gap_addendum.md`
**Method:** Comprehensive directory survey + targeted reads of previously-unaudited infrastructure layers.

---

## §0 Headline

The previous audits (review + gap addendum) examined what the workplan covered and identified missing items at the *editorial* and *implementation* layers. This audit extends one tier deeper: into the **content management infrastructure**, **canon foundations**, and **pre-existing workplan artifacts** that have been running in parallel without integration.

**Headline finding: a workplan already exists.** `designs/workplans/wave1_workplans.md` (25 KB) is a pre-existing five-proposal workplan (P1, P3, P9, P10, P21) referenced as "G-core N-direct proposals identified in `gameplay_assessment.md` §2 Wave 1 schedule." This workplan was never surfaced in the v2 build. The v2 workplan and wave1_workplans address different scopes — v2 is infrastructure-and-validation, wave1 is gameplay-proposal — but their existence in parallel without cross-reference is a coordination failure.

---

## §1 Pre-existing Workplans + Gameplay Assessment Layer

### G17 · `designs/workplans/wave1_workplans.md` exists and is uncommitted

**Content (head):** Atomization-oriented workplans for five "G-core N-direct proposals" — P1 (Leap UX), and four others (P3, P9, P10, P21 — exact identities require full read). Each workplan enumerates: canonical anchors, pre-implementation decisions, implementation-unit breakdown, cross-proposal dependencies, verification criteria.

**Status:** "Proposal. No commits. Each workplan requires editorial approval before individual PP entries are drafted for atomization register."

**Reference baselines cited:**
- `rigorous_audit_synthesis_s1_s7_v3_1.md` — synthesis-level proposal layer (NOT FOUND in this audit's directory survey — possibly in atoms_pending or designs/audit)
- `mechanical_implementation_revised.md` §1, §4, §5, §6, §8 — mechanical specification (location TBD)
- `mechanical_implications_revised.md` — decision architecture + feedback loops
- `gameplay_assessment.md` — G-tier + contribution analysis

**Workplan integration impact:** The v2 workplan has no analog to "Wave 1." It does not classify mechanics by G-tier (gameplay tier) or N-directness. The wave1 proposals (P1=Leap UX in particular) describe **player-facing UX work that v2's C2 bucket should subsume.** P1 alone — Leap UX — is a multi-unit player-experience design (entry-commit UX, contact-phase execution, sentinel action, retention roll resolution) that v2 treats as a single cell ("threadwork player UX" under C5).

**Required action:**
- F2.17 — locate and read `gameplay_assessment.md`, `mechanical_implementation_revised.md`, `mechanical_implications_revised.md`, `rigorous_audit_synthesis_s1_s7_v3_1.md`. Determine whether they exist as canonical docs, atoms_pending content, or cross-referenced artifacts that have been lost.
- A5 — `wave1_workplans.md` editorial approval. Each of the five proposals is currently uncommitted-with-decisions-required (e.g., P1 has DECISION P1-1, P1-2, P1-3 listed). These are Authority-tier items.
- C5 expansion — Player Character Domain must subsume Wave 1 player UX work, not invent a parallel classification.

### G18 · The "G-tier" classification system

`wave1_workplans.md` references "G-core N-direct proposals" without defining G-tier or N-directness in v2's framework vocabulary. This implies a *separate* classification system (G-tier, gameplay-tier?) running alongside N→Ω→Μ→М→Τ→Q→Μ̄.

**Required action:** F2.18 — reconcile classification systems. If G-tier/N-direct is a sub-taxonomy of N (Necessity), it should be integrated into the throughlines_meta framework. If it is parallel, the project has two competing vetting hierarchies.

---

## §2 Three Throughline Documents — Unreconciled

The repo contains **three throughline artifacts** of different scope, never cross-referenced in v2:

| Document | Size | Purpose | Indexing |
|---|---|---|---|
| `references/throughlines_meta.md` (skeleton) | 13 KB | PP-672/674 vetting framework | Tier-based: N/Ω/Μ/М/Τ/Q/Μ̄ |
| `references/throughlines_meta_infill.md` | 51 KB | Vetting framework rationale + worked examples | Same |
| `references/throughlines_complete.md` | 51 KB | Technical chains across mechanical systems | T-01 through T-41+ |
| `references/throughline_registry.md` | 14 KB | **Narrative + system throughlines** | N1-N6 (narrative) + T1+ (system) |
| `references/throughlines_meta_solmund_appendix.md` | 7 KB | PROVISIONAL Solmund T-A..T-E | Provisional T-letter |

**Numbering collision risk:** `throughline_registry.md` has "T1" entries (system throughlines numbered as plain T1, T2, ...) while `throughlines_complete.md` has "T-01" through "T-41+" (hyphen-prefixed). The Solmund appendix has "T-A through T-E" (letter-prefixed PROVISIONAL). All three use "T" prefix. This is a glossary collision waiting to mislead.

**Required action:**
- F2.19 — Throughline taxonomy reconciliation. Define which document is canonical for which axis (narrative? mechanical chain? vetting tag?). Establish a consistent numbering scheme. Regenerate cross-references.
- A4 (Solmund) integration must specify which throughline registry the T-A..T-E numbers fold into, AND ensure no collision with existing T-1 (registry), T-01 (complete), or T-A..T-E in any other appendix.

### G19 · `throughline_registry.md` introduces N1-N6 NARRATIVE throughlines

These are absent from the v2 workplan entirely:

- **N1 — Thread Revelation Is the Master Clock** (drives every NPC arc + faction response + Certainty track)
- **N2 — Sovereignty Is Governance, Not Conquest** (Accord ≥ 2 to win; Cultural Reformation/Show of Force/Military pathways)
- **N3 — The Peninsula Is One World Through Different Lenses** (replayability via faction perspective)
- **N4 — Every Ending Is Earned** (Portrait Retirement after ≥ 2 Convictions resolved)
- **N5 — The Forgetting Makes Knowledge Contested** (RM substrate-heritage gap; hidden Thread-site bonus)
- **N6 — Institutions Are Characters** (faction priority trees; Pastoral Assumption; subnational factions)

**v2 workplan engages with mechanical T's (T-01 through T-41+) but NOT narrative N's.** This is an oversight: the narrative throughlines describe what the *game is about* whereas mechanical T's describe how the engine wires it together. A workplan that ignores N1-N6 risks delivering correct mechanics that fail to convey the intended experience.

**Required action:** Each major item in v2 should declare which N's it serves *and* which T's. Currently only T's are tagged. Particularly: V2 (Sim S3) should verify N1 (Thread Revelation curve actually drives NPC arcs in sim), N4 (Conviction resolutions produce ending portraits), N6 (institutional priority trees produce coherent autonomous behavior).

---

## §3 Canon Foundations Layer — Never Touched

### G20 · `canon/00_philosophical_foundations.md` (62 KB)

This is the constitutive document. The canon-guard skill validates every proposal against it. The workplan never references it, never reads it, never plans interaction with it.

**Why this matters:** Foundations = ontology. Every mechanic must comply with Foundations. The Foundations doc is the layer above N (Necessity Test). When the workplan tags an item with N (e.g., D-5 Einhir site-network), the implicit appeal is to Foundations. Without reading Foundations, that N tagging is ungrounded.

**Required action:** F2.20 — Foundations read. At minimum, skeleton-level read of canon/00 to align the workplan's N-tier vocabulary with the actual constitutive constraints. The canon-guard skill exists precisely to apply Foundations; the workplan should reference it.

### G21 · `canon/02_canon_constraints.md` introduces P-### test infrastructure

Sample of P-### constraints (read in this audit):

| ID | Constraint | Mechanical implication |
|---|---|---|
| **P-01** Inseparability | Every Thread op MUST produce co-movement effects across all three dimensions. No GM discretion. |
| **P-02** Monstrosity grounded in Lacanian Real | No moral-register language for monstrous origin. |
| **P-03** Rendering = consciousness-performed | Information asymmetry is the core mechanic, not overlay. |
| **P-04** Monstrosity = ontological, not moral | No alignment system. |
| **P-05** Three emergence modes mechanically distinct | Mode 1/2/3 must be procedurally distinguishable. |
| **P-06** Threadcut beings have no layer 2 | Past-Pull auto-Gap; Coherence inapplicable. |
| **P-07** Calamity = rendered-side mechanism | Ein Sof has no agency. |
| **P-08** Epistemological barrier = inaccessibility | Inert Knowledge mechanic. |
| **P-09** Memory pulling messy/costly/detectable | Co-movement applies; produces CD. |
| **P-10** Coherence indexes commensurability | Lower Coherence = less commensurate with human-mode being. |
| **...** P-11 through P-15 (PP-15 added from Amendment 01) | Three-layer being-persistence, Leap mechanics, Coherence 0 |

**Each constraint has a "Violation Test" — a mechanical predicate that any new mechanic must satisfy.** This is the canon-guard skill's literal validation rubric.

**Workplan implications:**
- Every PP-666 PROVISIONAL spec (settlement_adjacency, fractional_province, faction_succession_split) needs to pass all applicable P-### tests. The v2 workplan does not check this.
- F1.1 (NPCTrajectoryEvaluator wiring) and F1.2 (deferred consequences) are restoration fixes — but they restore P-01-relevant machinery (co-movement). The fix should explicitly cite P-01.
- Every Sim S3 module (V2) should map to applicable P-### tests. Threadwork → P-01, P-06, P-07. Fieldwork → P-03, P-08. Settlement layer → P-03 (rendering). Etc.

**Required action:** F2.21 — P-### test integration. Each Class A/B item in the workplan adds a "P-tests applicable" field. Vetting protocol §8.5 should include P-### check alongside N/Ω/Μ/М/Τ/Q.

### G22 · `canon/03_canonical_timeline.md` (19.6 KB)

The canonical project timeline. References to "Solmund dissolution" (D-3, ED-724) propagated to this doc. The workplan's **A1.2 D-4 Altonian invasion timeline** decision must integrate with the existing canonical timeline. v2 treats D-4 as a single date decision; the timeline doc may already commit to surrounding events that constrain D-4's plausible values.

**Required action:** F2.22 — Read canonical_timeline.md before A1.2 decision. Surface existing constraints to Jordan.

### G23 · Foundations Amendments 1 + 2

`canon/01_foundations_amendment_self_rendering.md` (14.5 KB) and `canon/02_foundations_amendment_leap_mechanism.md` (14.5 KB) are referenced throughout throughlines_meta and the M-7 borrowings spec. The workplan never touches them.

**Why this matters:** PP-672 incorporated Amendment 1 (Am 1) and Amendment 2 (Am 5) into the throughlines framework explicitly. Wave 1 P1 (Leap UX) workplan §1.1 lists "canon/02 Am 1, Am 2, Am 3, Am 6" as canonical anchors. Anything touching Leap mechanics, knot formation, or operation-type taxonomy must comply with Am 2.

**Required action:** F2.23 — Skeleton read of both Amendments. Tag any v2 item that touches Leap, knot formation, or operation-type as Am-1/Am-2-relevant.

---

## §4 Content Management Pipeline — `references/atoms_pending/` (381 files)

**The largest single discovery.** 381 files in one batch (`2026-04-25/`) totaling ~2 MB. Every file is "pending" canonization. The Solmund cultural guide that produced T-A..T-E PROVISIONAL throughlines came from this batch.

**Implications:**

1. **A4 covers ONE batch.** The v2 workplan's A4 (Solmund T-A..T-E + 9 Appendix B items) addresses ONLY the Solmund subset of the 2026-04-25 batch. The other ~370 files are uncategorized and unaddressed.

2. **No declared canonization process.** What moves an atom from `atoms_pending/` to canonical? Who decides? On what cadence? The workflow is invisible.

3. **381 files of pending content is risk.** Each could contain editorial decisions, mechanical proposals, lore additions, or PROVISIONAL specs that should be in the editorial ledger or patch register. Until triaged, this is unaccounted-for design surface.

4. **Likely ED/PP/T sources.** Given that Solmund alone produced T-A..T-E + 9 Appendix B editorial items, extrapolation suggests the full 381-file batch could contain hundreds of pending editorial items.

**Required action:**
- F2.24 — atoms_pending triage. Per-file classification: (a) canonical-promotion candidate; (b) atoms_pending archive (kept for record but not canonized); (c) editorial-ledger entry needed; (d) patch register entry needed; (e) duplicate/superseded.
- F2.25 — atoms_pending workflow declaration. Define: who creates atoms_pending content, who reviews, what triggers canonization, what cadence.
- This is conservatively a multi-week effort if done thoroughly.

---

## §5 Test Corpus Reality

Previous audits noted ~34 sim files. Actual count by directory:

| Directory | Files | Total KB |
|---|---|---|
| `tests/sim/` | **207** | 5,298 |
| `tests/sim_framework/` | 23 | 377 |
| `tests/audit/` | 29 | 427 |
| `tests/stress/` | 17 | 862 |
| `tests/emergent_arc_skeleton_test_*.md` (root) | 7 | 478 |
| `tests/audit_three_day_2026-04-18.md` (root) | 1 | 38 |
| `tests/coverage_matrix.md` (ttrpg) | 1 | 19.7 (violates atomization rule max 5K) |
| `tests/coverage_matrix_archive.md` | 1 | 105 |
| `tests/valoria_throughline_synthesis_holistic_audit.md` | 1 | 51 |
| `tests/misc/` | 2 | 0 |

**Total tests/: 290 files, ~7.7 MB.**

The v2 workplan's V2 (Sim S3) deterministic regression treats `sim_var_01` through `sim_var_06` (6 files) as the regression target. This is **3% of `tests/sim/`.**

### G24 · `tests/sim_framework/` — distinct sim framework

23 files specific to sim framework infrastructure (not the sim runs themselves). Likely contains the canonical sim build patterns, ledger schema, and harness code. The v2 workplan references the Python sim but doesn't address the framework.

### G25 · `tests/audit/` — 29 audit files

`tests/audit/aud_tw_001_threadwork_audit.md` was identified earlier. 28 more audit files exist. Likely contains the historical audit findings that produced editorial entries 401–700+. The workplan doesn't engage with this audit body.

### G26 · `tests/stress/` — 17 files including the 28 P0 threadwork blockers

Already partly addressed (F2.7). The directory contains `thread/threadwork_audit_register.md` (32 KB) but presumably also stress tests for combat, debate, mass battle, etc. that the workplan hasn't surfaced.

### G27 · Emergent arc skeleton tests (7 batches)

`tests/emergent_arc_skeleton_test_2026-04-17_batch2.md` through `batch8_counterfactual.md`. Total ~478 KB. Tests for emergent arc generation. The workplan's V2 NPC priority tree module (T-23, T-25) should presumably reference these as regression targets but does not.

### G28 · `tests/coverage_matrix.md` (ttrpg, 19.7 KB) violates atomization rule

`atomization_rules.yaml` says: `match: "tests/coverage_matrix.md"` `max_tokens: 5000`. Actual file is ~5000+ tokens. **The compliance check should flag this.** Bootstrap reports "compliance_check.py not found — skipping" so the violation is currently uncaught.

This is a smoking gun for G3 (compliance_check not running): a known size-policy violation that exists undetected.

**Required action:**
- F2.26 — sim corpus triage (similar to atoms_pending triage). Classify all 207 sim files as regression target / historical / extract-findings.
- F2.27 — sim_framework integration into V1/V2 build process.
- F2.28 — audit history triage. 29 + 1 holistic + 7 emergent arc = 37 audit artifacts. Surface findings into editorial ledger.
- F2.29 — coverage_matrix.md (ttrpg) atomization fix or rule exemption.

---

## §6 Designs Layer Reality

Previously surveyed: `designs/` has 13 subdirectories totaling ~190 files.

| Subdir | Files | Workplan engagement |
|---|---|---|
| `architecture/` | 25 | Partial (videogame_mode_spec read) |
| `arcs/` | 39 | None — arc designs not in workplan |
| `audit/` | 48 | None — audit history not surfaced |
| `godot/` | 4 | None — Godot-specific design docs |
| `npcs/` | 17 | Partial (npc_behavior_v30 referenced) |
| `provincial/` | 35 | Partial (a few key docs referenced) |
| `scene/` | 33 | Partial (combat_v30, social_contest_v30 referenced) |
| `territory/` | 4 | Engaged (settlement_adjacency_v30, settlement_layer_v30) |
| `threadwork/` | 9 | Partial (threadwork_v30 referenced) |
| `ui/` | 9 | **Designed but never implemented (valoria-game scenes/ui/ all .gitkeep)** |
| `videogame/` | 1 | None — godot_architecture_specification.md (51 KB) never read |
| `workplans/` | 1 | None — wave1_workplans.md never integrated (G17) |
| `world/` | 21 | Partial |

### G29 · `designs/ui/` (9 files, 412 KB) — UI designs exist; UI implementation does not

The workplan's C2 (UI scenes) treats UI as undeclared content. **In fact UI was designed.** 412 KB of UI design across 9 files. valoria-game/scenes/ui/* are all `.gitkeep` only.

The gap is not "we need UI design" but "we have UI design and have not implemented any of it." This is an enormous unstated debt.

**Required action:** F2.30 — UI design inventory. List the 9 design docs. Map each to a target valoria-game scene. Estimate implementation effort per scene. P (Playability) milestone needs at minimum 3 of these (persistent HUD, season overview, combat UI) before First Playable Season Loop is achievable.

### G30 · `designs/videogame/godot_architecture_specification.md` (51 KB)

Single-file Godot architecture spec. **valoria-game/docs/architecture.md is 5.8 KB.** The 51 KB ttrpg-side spec is presumably the authoritative source; the 5.8 KB valoria-game-side is a summary or excerpt. Relationship undeclared.

**Required action:** F2.31 — Architecture document reconciliation. Determine which is authoritative. If ttrpg-side: valoria-game/docs/architecture.md should reference it. If valoria-game-side: ttrpg-side should be archived or updated.

### G31 · `designs/godot/` (4 files)

Godot-specific designs distinct from `designs/videogame/godot_architecture_specification.md`. Purpose unclear. Possibly Godot integration patterns, autoload configurations, or build setup.

**Required action:** F2.32 — Read and classify `designs/godot/*.md`.

### G32 · `designs/audit/` (48 files, 1 MB)

`designs/audit/gap_resolution_2026-04-19.md` was referenced (PP-667). 47 other audit docs. Likely contains:
- Historical mechanical audits (per-system)
- Cross-cutting integration audits
- Holistic audits
- Editorial decisions audits

**Required action:** F2.33 — Audit content inventory. Surface still-relevant findings into editorial ledger or patch register. Archive resolved.

### G33 · `designs/arcs/` (39 files, 811 KB)

39 arc design files. arc_register.md and arc_register_infill.md are in references/. designs/arcs/ has the arc *content* — likely per-NPC, per-faction, per-territory arc trees.

The workplan's V2 (Sim S3) covers "NPC priority trees + Arc transitions per `npc_behavior_v30 §5.2 + arc_expansion_v30`" but the actual arc content lives in 39 files in designs/arcs/. The workplan's scope is understated.

**Required action:** F2.34 — Arc content inventory. Determine which arc files are needed for Sim S3 vs which are content-layer (post-V).

---

## §7 References Layer — Major Unaudited Documents

Beyond the docs already discussed, several large reference docs were never engaged:

| Document | Size | Likely purpose | Workplan impact |
|---|---|---|---|
| `references/values_master.yaml` | 136 KB | Aggregated canonical values | F0.3 (ms_budget centralization) is a subset of this larger problem |
| `references/numeric_bounds_report.yaml` | 63 KB | Numeric bounds tracking; staleness flagged | Session log mentioned "flagged for regen after next collator run" — this should be M-tier or F2 |
| `references/proper_noun_triage_round2.yaml` | 50 KB | Proper noun triage round 2 | Maret/Yrsa propagation (PP-665) was round 1; round 2 is undisclosed |
| `references/restructure_ledger.md` | 47 KB | v30 baseline restructure log | The 2026-04-13 restructure history; should be project record |
| `references/propagation_log.md` | 44 KB | Propagation tracking | Active log of cross-doc propagation |
| `references/propagation_map.md` | 24 KB | Propagation map | Architecture for cross-doc propagation |
| `references/valoria_canonical_definitive_r2.md` | 14 KB | The doc ED-745–748 verify against | F2.2–F2.5 must read this — currently underspecified |
| `references/valoria_complete_systems_r2.md` | 14 KB | Companion to canonical_definitive_r2 | Cross-system overview |
| `references/valoria_interdoc_audit.md` | 33 KB | Inter-document audit | Cross-cutting audit findings |
| `references/valoria_simulation_review.md` | 9 KB | Simulation review | Sim findings |
| `references/valoria_cross_conversation_review.md` | 11 KB | Cross-session review | Multi-session synthesis |
| `references/collation_report_summary.yaml` | 53 KB | Collation report | Output of valoria_collator.py |
| `references/glossary.md` | 17 KB | Project glossary | Term definitions |
| `references/D10_INTEGRATION_GUIDE.md` | 5 KB | d10 dice integration guide | Dice system integration patterns |
| `references/d10_success_probabilities.json` | 3 KB | Pre-computed dice probs | Dice probability tables |
| `references/wc_survival_spine.md` | 10 KB | WC survival contest spec | Referenced in workplan (P bucket UI) but never read |
| `references/historical/` | 89 KB / 2 files | Historical references | Preserved for record |

**Aggregate: ~700 KB of reference material the v2 workplan never engaged with.**

### G34 · `references/proper_noun_triage_round2.yaml`

PP-665 (Maret Vossen → Yrsa Vossen) was proper noun work. There's a "round 2" that isn't surfaced in the workplan. What proper nouns are pending triage? What's the cadence?

### G35 · `references/numeric_bounds_report.yaml` regeneration debt

Session log explicitly says "flagged for regen after next collator run." 63 KB report stale. Workplan should surface this.

### G36 · `references/valoria_canonical_definitive_r2.md` is the verification target for F2.2–F2.5

ED-745–748 verifications are described as "Verify against valoria_canonical_definitive_r2." The doc is 14 KB — small enough to fully read in one pass. F2.2–F2.5 are mechanical lookups that should be trivially executable.

**Required action:** F2.2–F2.5 should be elevated from "verification work" to "single read pass against r2 doc." If the relevant info is there, ED-745–748 close immediately.

### G37 · `references/propagation_map.md` + `references/propagation_log.md`

Propagation infrastructure (24 KB + 44 KB). Tracks how design changes propagate across documents. The valoria-collator.py and patch_propagation_checker.py operate on these.

**Required action:** F2.36 — Read propagation_map and propagation_log. Determine what propagation debt is open (similar to hybrid_gaps propagation in design_registry.yaml).

---

## §8 Tools + Skills Infrastructure — Underspecified

### G38 · Skills with multi-file structure

Most skills are single SKILL.md. Three are multi-file:

| Skill | Files | Total KB | Significance |
|---|---|---|---|
| valoria-orchestrator | 10 | 224 | SKILL.md (24 KB) + scripts/ (github_ops, valoria_hooks, etc.) + references/ |
| valoria-combat-simulator | 5 | 31 | Why is combat-simulator multi-file when other simulators are single-file? |
| valoria-dice-model | 2 | 11 | Companion file |

**Required action:** F2.37 — Audit multi-file skills. Document why combat-simulator and dice-model are special. Verify all script dependencies in orchestrator are current post-PP-673 (skeleton→index rename).

### G39 · `tools/coverage_matrix.py` (4.3 KB) — unused automation

A tool that auto-generates `tests/coverage_matrix.md`. The workplan says coverage_matrix is stale and contradictory. The tool to regenerate it exists but isn't run.

**Required action:** F2.38 — Run coverage_matrix.py against current state. Compare output to stored coverage_matrix.md. Reconcile.

### G40 · `tools/freshness_gate.py` + `docs/freshness_gate_spec.md` (10.8 KB + 4.4 KB)

**Major infrastructure absent from the workplan.** Freshness gate is SHA-tracked staleness for canonical docs vs `canonical_sources.yaml`. Code-enforced. Spec mandates session-start invocation.

**Status:** "IMPLEMENTED — pending SHA population pass" (per spec dated 2026-04-02).

**Workplan implications:**
- Bootstrap output never mentions freshness_gate. Either it's not being run at session start (process gap) or the SHA population pass was never completed (spec gap).
- Every sim session, every audit, every patch could have used stale params/canonical docs without freshness_gate enforcement. v2's V1/V2 sim sessions are vulnerable.

**Required action:** F2.39 — Freshness gate operational status check. Run `python3 tools/freshness_gate.py` (check mode). If exit 2 (canonical_sha fields missing), run `--update`. Then add freshness_gate to bootstrap protocol.

This is potentially **the same severity as G3 (compliance_check not running):** another piece of CI/orchestration infrastructure that exists but isn't running.

### G41 · `tools/extract_values.py` + `references/values_master.yaml`

`extract_values.py` (15.8 KB) extracts canonical values from design docs into `values_master.yaml` (136 KB). The aggregation is the canonical-values reference for sim verification.

**Required action:** F2.40 — Verify values_master.yaml is current vs design docs. Re-run extract_values.py if stale.

### G42 · `tools/extract_proper_nouns.py` + `references/proper_noun_triage_round2.yaml`

Proper-noun extraction tool feeds round-2 triage. PP-665 was round 1.

**Required action:** Reconcile with G34. Triage round 2 may be in-progress and should be tracked in workplan.

### G43 · `tools/valoria_collator.py` + `references/collation_report_summary.yaml`

Collator (22 KB) produces collation report (53 KB). Session log mentions "flagged for regen after next collator run." Report is stale.

**Required action:** F2.41 — Run valoria_collator.py. Surface findings into editorial ledger / numeric_bounds_report regen.

### G44 · `tools/editorial_review/valoria-editorial-review.jsx` (15 KB)

Browser-based editorial review tool (JSX). Purpose undocumented. Possibly an HTML-rendered editorial decision UI.

**Required action:** F2.42 — Document valoria-editorial-review.jsx purpose. Determine in-use status.

### G45 · `tools/model_router.html` (11 KB)

AI model routing tool (HTML). Possibly relates to the model_router.html user preference passthrough patterns. Purpose undocumented.

**Required action:** F2.43 — Document model_router.html purpose.

### G46 · `tools/compliance_dryrun.py` (3 KB)

Compliance dryrun tool. Companion to compliance_check.py. Suggests compliance has a dryrun mode that could be used during workplan execution to flag violations before commits.

**Required action:** F2.44 — Use compliance_dryrun.py during F0/F1 work to verify changes don't introduce violations.

### G47 · `tools/verify_cuts.py` (2.5 KB)

Verifies content "cuts" — likely the atomizer's split outputs. Small tool, specific purpose.

---

## §9 Archives Layer

`archives/` contains:
- `editorials/`: 6 files, 220 KB
- `patches/`: 13 files, 410 KB
- `session/`: 8 files, 297 KB
- `session_handoff_2026_04_20.md`: 15 KB

`canon/editorial_ledger_archive.yaml`: 54 KB (separate from archives/editorials/).

### G48 · Archive vs canon-archive distinction

`archives/editorials/` and `canon/editorial_ledger_archive.yaml` both exist. Different scopes? Different lifecycles? The atomization rules say `canon/editorial_ledger_archive*.yaml` is `read_restriction: "index_first"`. The directory archives/editorials/ has 6 files at 220 KB.

**Required action:** F2.45 — Document archive layering. Determine: when does an editorial entry move from `editorial_ledger.yaml` to `editorial_ledger_archive.yaml`, and when (if ever) further to `archives/editorials/`?

### G49 · `archives/session_handoff_2026_04_20.md` (15 KB)

A specific handoff document from 2026-04-20. The workplan should account for what handoffs have occurred and what they covered.

---

## §10 valoria-game Code-Level Reality

Surveyed beyond what previous audits covered:

### G50 · `autoload/Meta.gd` is 41.7 KB

The single autoload is enormous. Likely contains:
- TrackerRegistry / FactionRegistry / CharacterRegistry / SettingState / NarrativeState management
- Faction AI dictionary
- Domain echo queue
- Trigger rules array
- Visual queue
- Threshold queue
- Many signals
- Likely the core consequence-routing logic

**41 KB is substantial code in one autoload.** This violates the architecture's "Resources are data; Nodes are lifecycle; RefCounted is logic; ONE autoload" principle in spirit if not letter — Meta.gd is *the* logic concentration point.

**Required action:** F2.46 — Meta.gd code review. Check for:
- Functions that should be in Tracker / Registry / NarrativeState rather than Meta
- The `var game_mode: int = Enums.GameMode.TTRPG` line (G1, already known)
- Comments referencing "A-02" — disambiguate from F1.1's NPC-A-02
- Whether all 41 KB is genuinely autoload-required or refactorable

### G51 · `autoload/EventBus.gd` (5.7 KB) + `autoload/GameStateMachine.gd` (5.3 KB)

Three autoloads (Meta + EventBus + GameStateMachine) with documented load order: `EventBus → Meta → GameStateMachine`. The architecture spec says "ONE autoload." This violates the spec.

**Required action:** F2.47 — Reconcile architecture spec ("ONE autoload") with implementation (three autoloads). Either spec is wrong or implementation is. Likely the spec is older; update.

### G52 · `valoria-game/systems/` 13 subdirectories

Beyond the directories I'd previously surveyed:

| Subdir | Files | Likely contents |
|---|---|---|
| `engine/` | 16 | CoreResolver, CoreEngine, ConsequenceRouter, RollContext, etc. |
| `npc/` | 8 | NPC behavior, trajectory evaluator, priority trees |
| `resolution_modes/` | 6 | Solo/OpposedSimultaneous/OpposedSequential/Versus/PhaseLockedSimultaneous |
| `registries/` | 5 | Character/Faction/Setting/Narrative/Unit registries |
| `data/` | 4 | DataLibrary, SaveData, etc. |
| `context/` | 4 | Roll context types |
| `situation/` | 4 | SituationGenerator, etc. |
| `trackers/` | 3 | TrackerRegistry / Tracker / Threshold |
| `faction/` | 3 | ValoriaFactionAI, FactionTurnSystem, etc. |
| `util/` | 4 | Enums, Constants, utilities |
| `threadwork/` | 1 | **Single file?** Just one threadwork system file |
| `transition/` | 1 | ZoomManager? |
| `ai/` | 1 | **Single file?** General AI |

**`systems/threadwork/` and `systems/ai/` having only 1 file each is suspect.** Threadwork is one of the largest design areas (9 design docs in ttrpg/designs/threadwork). One implementation file likely means: (a) it's a stub, (b) most functionality is elsewhere, or (c) the threadwork implementation is genuinely thin and a major implementation gap exists.

**Required action:** F2.48 — Verify threadwork implementation depth. If 1 file is genuinely the entire threadwork system, that's a massive C5 (Player Character Domain) gap.

### G53 · `versions/.gitkeep` — empty versions directory

`ttrpg/versions/` is empty (`.gitkeep` only). Suggests planned version snapshots that have not been used.

**Required action:** F2.49 — Versions strategy declaration. Either populate (snapshot v30 baseline as `versions/v30/...`) or remove the directory.

---

## §11 Compliance Check Gap — Confirmed Violations Currently Uncaught

`atomization_rules.yaml` declares:
- `compliance_check_on_bootstrap: true`
- `compliance_check_on_commit: true`
- `compliance_check_on_close: true`
- `auto_fix_on_violation: true`

But bootstrap reports compliance_check.py "not found." Therefore zero compliance checks have been running.

**Confirmed violations the rule would catch:**

| Rule | File | Status |
|---|---|---|
| `tests/coverage_matrix.md max_tokens: 5000` | `tests/coverage_matrix.md` (~5300 tokens) | Likely violation |
| `canon/editorial_ledger.yaml max_tokens: 2000` | 1.9 KB / ~470 tokens | OK |
| `canon/patch_register_active.yaml max_tokens: 15000` | 18.6 KB / ~4700 tokens | OK |
| `canon/editorial_ledger_summary.yaml summary_max_tokens: 1000` | 1.1 KB / ~270 tokens | OK |
| `params/threadwork.md max_tokens: 5000` | 14.3 KB / ~3600 tokens | OK |
| `params/board_game.md max_tokens: 5000` | 11.2 KB / ~2800 tokens | OK |
| `params/threadwork_superseded.md max_tokens: 15000` | 44.1 KB / ~11000 tokens | OK |

So the explicit-rule violations are smaller than feared (just coverage_matrix.md). But:

**The bigger issue is the rule for `params/*.md` (max 10000, exceed → flag_for_split):**
- `params/threadwork_superseded.md` is 44 KB / ~11000 tokens — over the params/*.md generic threshold (10000) BUT has its own specific rule (15000). OK by specific rule.

And **`require_rule_above_threshold: true`** is set under `params/*.md` — meaning any params file over 10000 tokens MUST have a specific rule. Verify all params files comply.

**Required action:** F2.50 — Run compliance_check.py once it's wired. Document current violations. The single known violation (coverage_matrix.md) is a concrete fix.

---

## §12 Consolidated Round-2 Additions

### Severity-ordered

**Critical (must promote to F0/F1):**

| ID | Item | Action |
|---|---|---|
| **G17** | wave1_workplans.md exists, uncommitted | A5 — editorial approval of P1, P3, P9, P10, P21 proposals |
| **G19** | N1-N6 narrative throughlines absent from v2 | Tag every major v2 item with applicable N's |
| **G21** | P-### test infrastructure unused | F2.21 — integrate P-tests into vetting protocol |
| **G24-G27** | tests/sim/ has 207 files; v2 covers 6 | F2.26 — sim corpus triage |
| **G29** | 9 UI design docs exist; UI implementation is `.gitkeep` | F2.30 — UI design inventory + P-milestone gating |
| **G40** | freshness_gate.py exists, not running at session start | F2.39 — wire freshness_gate to bootstrap |
| **G50-G52** | systems/threadwork has 1 file (potential implementation gap) | F2.48 — verify threadwork implementation depth |

**High (extend F2):**

| ID | Item |
|---|---|
| G18 | G-tier classification reconciliation with N-framework |
| G20 | canon/00_philosophical_foundations.md never read |
| G22 | canon/03_canonical_timeline.md never read (constrains A1.2) |
| G23 | Foundations Amendments 1+2 never read |
| G28 | tests/coverage_matrix.md atomization-rule violation |
| G30 | designs/videogame/godot_architecture_specification.md (51 KB) never read |
| G33 | designs/audit/ 48-file audit history not surfaced |
| G36 | valoria_canonical_definitive_r2.md is small enough to fully read; F2.2–F2.5 should close in one pass |
| G37 | propagation_map.md + propagation_log.md never engaged |
| G47-G49 | tools/extract_values.py, valoria_collator.py, editorial_review.jsx undocumented |
| G50 | Meta.gd 41 KB code review |
| G51 | Three autoloads vs "ONE autoload" architecture spec |

**Moderate (M-tier additions):**

| ID | Item |
|---|---|
| G34 | proper_noun_triage_round2 status |
| G35 | numeric_bounds_report regen debt |
| G38 | Multi-file skills audit (orchestrator, combat-simulator, dice-model) |
| G41-G43 | values_master, collator, proper_noun extraction freshness |
| G45 | tools/model_router.html purpose |
| G46 | compliance_dryrun.py integration into workflow |
| G49 | archives/session_handoff_2026_04_20.md surfacing |

**Architectural declarations (declared, deferred):**

| ID | Item |
|---|---|
| G31 | designs/godot/ purpose (4 files) |
| G44 | editorial_review.jsx in-use? archive? |
| G53 | versions/ strategy: populate or remove |

---

## §13 Aggregate Workplan Surface — Reality Check

After Round 1 review, the gap addendum, and this Round 2 audit:

**Identified items (across all artifacts):**

| Tier | Count |
|---|---|
| F0 (data reconciliation) | 3 |
| F1 (engine integrity) | 8 (3 original + G1, G2, G3 + revised) |
| F2 (canon hardening) | ~50 (12 v2 + 4 addendum + ~34 round-2) |
| A (authority unlocks) | 12 (3 v2 vision + 3 doc blockers + 1 Varfell + 6 Solmund Appendix B classified + Wave 1 ×5) |
| V (validation) | 6 (V1 + V2 + V3 each with sub-prerequisites) |
| P (playability) | 1 milestone |
| C1-C7 (construction, expanded) | ~30 across content/UI/save/player-domain/localization/campaigns |
| M (maintenance) | 12 |
| B (build/release) | declared bucket |
| **Triage workstreams** | atoms_pending (381 files), sim corpus (207 files), audit history (48+29+7=84 docs) |

**This is ~120+ active items, plus three triage streams, plus declared-deferred buckets.**

The workplan as currently formed cannot execute end-to-end in any reasonable timeline by one developer without:
1. **Severe scope reduction** — drop all "declared deferred" items; defer player-character UI and campaign authoring; ship a minimal substrate-validation prototype.
2. **Triage automation** — atoms_pending and sim corpus triage should be partially automatable (heuristic classification + spot-check) rather than file-by-file review.
3. **Clear MVP target** — define what "shippable" means. Without an MVP definition, the workplan is open-ended.

---

## §14 Recommended Reframe

The v2 workplan is a *project completion plan*. After Round 2, it is clear the project is not at a *completion* phase — it is at a **scope-decision** phase. The repo contains far more design surface than can be implemented end-to-end. The decision Jordan needs to make is not "how do we sequence this work" but "what is the minimum coherent slice we ship?"

**Three possible scope frames:**

**Frame 1 — Mechanical Verification Project.**
Goal: complete the sim oracle. V1 + V2 land. Sim S3 verifies all T's mechanically. No Godot UI work. No playable artifact. The output is a verified design specification.

- Effort: ~6–10 sessions
- Player-facing output: none
- Defers: all of C, B, P milestone, atoms_pending triage, audit history surfacing
- Justification: the design canon is already nearly complete; verifying it formally is achievable

**Frame 2 — First Playable Substrate.**
Goal: Godot project plays one season end-to-end. Demonstrates Μ-α/β/γ/δ in working engine. UI minimal but functional.

- Effort: ~15–25 sessions
- Player-facing output: a single-season prototype
- Defers: most C content, B build infrastructure, atoms_pending triage, full UI, save system hardening, campaign authoring
- Requires: F0+F1 complete; V1 done; minimal C1 (weapons, factions, ~3 territories); minimal C2 (3 UI scenes); P milestone; one Q-elegance pass

**Frame 3 — Full Project Completion.**
Goal: shippable game with all currently-designed mechanics, full UI, full content, full save system, build pipeline.

- Effort: estimated 50+ sessions, likely much more
- Player-facing output: complete game
- Requires: everything in this audit + likely more discovered along the way
- Reality check: solo developer + content authoring at scale + UI + audio + testing is multi-year effort

**My recommendation: Frame 2.** Frame 1 produces a paper artifact. Frame 3 is open-ended. Frame 2 produces a tangible thing that can be tested, iterated on, and grown — and forces decisions that infrastructure-only work can defer indefinitely.

Frame 2 reframes the workplan: every item is asked "is this required for one playable season, or can it be deferred?" The answer ruthlessly cuts the surface. atoms_pending triage → defer. designs/audit surfacing → defer except blockers. UI → only the 3 essential scenes. C5 player domain → only character creation + threadwork player UX (P1 from Wave 1). Build infrastructure → defer until first playable exists. Asset content → minimum (no audio, placeholder portraits, simple iconography).

The workplan produced from Frame 2 would be ~30 items deep, executable in ~15–25 sessions. The current workplan (~120+ items) is closer to Frame 3 in scope while presenting as an execution plan, which is the gap Round 2 has clarified.

**The single most useful next decision: which Frame.** Without it, every subsequent workplan revision will continue accreting surface rather than narrowing toward a shippable artifact.
