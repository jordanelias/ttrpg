<!-- v30 path update applied 2026-04-13 -->
# VALORIA PROPAGATION MAP
## Last updated: 2026-04-14
## Version: 2.0 — self-maintaining
## Format: machine-readable YAML blocks + human-readable tables

---

## AUTO-UPDATE PROTOCOL (runs on EVERY commit — not optional)

Before any commit closes, the orchestrator executes this protocol:

### Step A — New file detection
For every file being added in this commit:
1. Determine its system(s): which of TTRPG/Hybrid/BG/ALL does it cover?
2. Determine its type: DESIGN / TEST / COMPILED / SKILL / REF / TOOL / LOG
3. Determine its dependencies: which existing files does it draw mechanical values from?
4. Determine who depends on it: which existing files reference or will need to reference it?
5. Add a row to the appropriate section of this map.
6. Add a row to `references/file_index.md` CURRENT FILES section.
7. If the file is a design doc: add it to `references/propagation_map.md` under its system heading.

If you cannot determine dependencies at commit time, add the file with `depends_on: [UNKNOWN — audit required]` and flag it in the commit message as `[PROP-UNKNOWN: filename]`.

### Step B — New cross-reference detection
A new cross-reference exists whenever a simulation finding, patch, or editorial item links:
- a finding in file X to a rule in file Y (that was not previously linked)
- a patch applied to file X that affects values extracted in params file Y
- an editorial decision in file X that changes rules referenced in file Y

For each new cross-reference:
1. Add the relationship to the propagation map under the relevant system heading.
2. If the relationship is bidirectional, add it in both directions.
3. Update `references/file_index.md` `referenced_by` column for both files.

### Step C — Stale detection (executable)
Run `tools/broken_dependency_checker.py` before closing any commit.

```bash
export GITHUB_PAT=<pat>
python3 tools/broken_dependency_checker.py
```

The script:
1. Fetches the full repository file tree from GitHub
2. Scans propagation_map.md, canonical_sources.yaml, skill_registry.md, and editorial_ledger.yaml
3. Reports every file reference that does not exist in the repo
4. Exits 1 if any broken dependency found; 0 if clean

If broken dependencies are found:
- Do NOT close the commit until resolved
- Either fix the reference (update the path) or add `[BROKEN-DEP: path — reason]` to the commit message with an explanation

## PP-653 Opposing Operations Propagation (2026-04-18)
| Source | Target | Type |
|---|---|---|
| designs/threadwork/threadwork_v30.md 2.6 | params/threadwork.md | design to params propagation |


## 2026-04-19 — PP-663 VTM-STRIKE / CR-STRIKE mechanical cleanup

**Commit:** (this commit)
**Scope:** completing propagation of VTM-STRIKE-2026-04-19 and CR-STRIKE-2026-04-19 canonical supersessions by cleaning residual mechanical references in:
- designs/provincial/clock_registry_v30.md (VTM row removed from Faction-Specific Tracks table)
- params/bg/tracks.md (VTM and VTM 5 track definitions tombstoned)
- params/bg/core.md (Cultural Reformation action row tombstoned)
- params/bg/npcs_special.md (Patience Protocol flattened to flat PC 0–4; Intel note corrected)
- designs/provincial/victory_v30.md (Varfell Path A → Intelligence gate; Path B → WR ≥ 3; Path C dissolved; 2 co-victory pairings re-gated; win probability table cleaned; non-military acquisition table CR row tombstoned; RM cultural displacement PT sources cleaned)
- designs/provincial/strategic_layer_v30.md (G-03 and G-07 sections tombstoned; G-06/P-26 Forgetting Check corrected to Intelligence stat; Cascade Test 3 re-framed character-scale; Scenario B header cleaned; private tracks list adjusted)
- designs/provincial/faction_politics_v30.md (Edeyja Inner Circle gate, Council of Warden context, ED-658 note)
- designs/npcs/npc_behavior_v30.md (§8.5 rows 2b/4b/5; §7.4 rows 2/4/7; §7.9 Institutional Mandate unique-clock changed VTM→WR)
- designs/provincial/varfell_path_b_v30.md (all three Options cleaned; Path B canonical = Option A + raised WR)
- designs/provincial/peninsular_strain_v30.md (§5.4 Cultural Reformation section tombstoned; 5 other CR mentions across §2, §7 cleaned)

**Registers:**
- canon/patch_register_active.yaml: PP-663 entry added
- canon/editorial_ledger.yaml: ED-708 entry (Path C dissolution + rebalance flag)
- references/canonical_sources.yaml: PP-663 commit reference appended to VTM and CR struck entries

**Consequences requiring further editorial work:**
- Varfell win probability rebalance (ED-708) — removal of Path C and change of A/B gates may affect win rates
- Varfell non-military acquisition toolkit: no replacement for Cultural Reformation. Varfell expansion now military-only. Consider whether this leaves Varfell underpowered vs non-military-expanding rivals (Crown Treaty, Church Seizure, Hafenmark Dynastic Proclamation).

## 2026-04-19 — PP-664 VTM-STRIKE residual cleanup

**Commit:** (this commit)
**Scope:** completes PP-663 propagation. Three files had tombstone banners added in PP-663 commits but their body mechanics were never edited.

- params/bg/faction_actions.md — VTM Discretion (PP-438) tombstoned in both duplicate sites; Cultural Reformation (PP-650) section tombstoned; Tribune Intel actions "VTM-building" reference corrected in both sites.
- params/bg/npc_priority_trees.md — Varfell priority tree P5 rows (both duplicates) replaced: "VTM/WR advancement ... VTM ≥ 2" → "WR advancement ... no Varfell unit in T15".
- designs/provincial/strategic_layer_v30.md — Cascade Test 3 body + Scenario B body wrapped in [HISTORICAL EXAMPLE — PP-664] banners; Scenario A "Varfell VTM 3/4" state descriptors re-framed to character-scale Vaynard presence; Cognitive Load private-tracks list corrected.

**Registers:**
- canon/editorial_ledger.yaml: ED-706/707 indentation normalized (dedent 2 spaces); ED-708 description compacted; ED-709 added.
- canon/patch_register_active.yaml: PP-664 entry added.
- references/canonical_sources.yaml: struck VTM and CR entries updated with committed SHAs (613ebf9, dc13a75) + pending-PP-664 marker.

**Consequences:** none new. Closes PP-663 propagation.

## 2026-04-19 — PP-665 Yrsa Vossen → Yrsa Vossen forename rename

**Commit:** (this commit)
**Scope:** resolves forename collision between Maret Uln (Varfell) and Yrsa Vossen (RM). Vossen renamed to Yrsa Vossen; Uln retains forename.

**Renames:**
- 43 instances of "Yrsa Vossen" → "Yrsa Vossen" across 25 canonical active files.
- 2 standalone "Maret" → "Yrsa" in Aldric Hann's belief quote (npc_behavior_v30 and npc_behavior_system_v1) — context is RM leader reference.
- Registry key `maret_vossen` → `yrsa_vossen` in references/proper_noun_registry.yaml.
- proper_noun_triage_decisions.yaml `maret` token: action `flag` → `split_resolved`, comment updated to note PP-665 resolution.

**Intentionally NOT renamed:**
- Archives (`archives/session/`, `archives/editorials/`, `archives/patches/`).
- Deprecated files (`deprecated/`, `*_deprecated.md`).
- Historical simulation outputs (`tests/sim/`, `tests/stress/`, `tests/audit/`, `tests/emergent_arc_skeleton_test_*`).
- Standalone "Maret" references in active files where context is Maret Uln (Varfell succession) — no rename required.

**Registers:**
- canon/patch_register_active.yaml: PP-665 entry added.
- references/canonical_sources.yaml: PP-665 cross-reference note appended.

**Consequences:** none — cosmetic rename with no mechanical impact. All NPC stance triangles, priority trees, arc profiles, and mechanical references preserved.

## 2026-04-19 — PP-666 Three new mechanical systems (settlement adjacency, fractional ownership, succession split)

**Commit:** (this commit)
**Scope:** per user direction, add three new mechanical systems as PROVISIONAL design specs + pointer ED entries in editorial ledger.

**New specs:**
- designs/territory/settlement_adjacency_v30.md — inter-settlement adjacency graph, edge types (road/river/mountain/coastal), army movement at settlement scale, mass battle at settlement scale, siege sequencing.
- designs/provincial/fractional_province_ownership_v30.md — CK-style province fractionalization when Seat and non-Seat have different controllers; PV share by settlement Prosperity; Greater/Lesser naming; Consolidation at 75%; Fragmentation Check each Accounting; Secession.
- designs/provincial/faction_succession_split_v30.md — universal Succession Contest framework; contenders by claim type; narrow-winner faction split; asset split (provinces, Mandate 60/40, Wealth 70/30, units by Loyalty); RM Settlement Emergence pathway formalized.

**Registers:**
- canon/editorial_ledger.yaml: ED-710, ED-711, ED-712 added as pointer entries. ED-706-709 archived to free headroom.
- archives/editorials/editorial_ledger_archive_601_800.yaml: ED-706-709 appended with VTM/CR strike audit trail note.
- canon/patch_register_active.yaml: PP-666 entry.
- references/canonical_sources.yaml: PP-666 cross-reference note.

**Supersedes (partially):**
- baralta_crown_claim_v30 Succession Contest (§2) — now special case of generalized Succession Contest in faction_succession_split_v30.
- settlement_layer_v30 §5.1 'internal road network' reference — formalized as adjacency graph in settlement_adjacency_v30.
- settlement_layer_v30 §5.1 'When the Seat is captured, provincial control transfers' — superseded by fractional ownership (Seat-only transfer now produces fractional state if non-Seat also contested).

**Consequences requiring further work:**
- settlement_adjacency_map.yaml needs authoring (derivable from geography_v30 + settlement_layer §2.1).
- PV-recompute logic needed across victory_v30 win probability table (current figures assume whole-province control).
- NPC behavior priority trees (npc_behavior_v30 §7) need succession-contest decision branches.
- Smoke-test required for all three systems before moving from PROVISIONAL to CANONICAL.

## 2026-04-19 — PP-667 Gap sweep + editorial ledger archival batch

**Commit:** (this commit)
**Scope:**
- Resolve 3 real audit gaps from canon_audit §4.
- Sweep OPEN ITEMS across 6 surveyed design docs — 26 resolutions logged.
- Archive ED-540..ED-659 batch (31 entries) to archives/editorials/editorial_ledger_archive_601_800.yaml.

**Gap resolutions (canon_audit §4):**
- Mine income rate: Mine-type settlement yields floor(Prosperity/2) Wealth/year; Guild +1; Trade Network +1; cap 4.
- Hafenmark food vulnerability: confirmed as worldbuilding-only; existing mechanics (Trade Network, Occupation Effects) cover the design space.
- Crown Einhir suppression: confirmed as ambient worldbuilding; existing Heresy Investigation / Church AP / Parliament Motion suffice.

**OPEN ITEMS sweep:**
- settlement_layer §9: 9 items (2 deferred to smoke-test, 4 resolved, 1 superseded by PP-666, 2 out-of-scope/confirmed).
- military_layer §5: 9 items (3 deferred, 6 resolved).
- peninsular_strain §8: 7 items (1 superseded by PP-663, 6 confirmed/resolved).
- faction_layer §10: 9 items (7 resolved, 2 deferred).
- victory_v30 §11: ED-311 closed (resolved in-file by PP-663).
- threadwork_v30: 10+ PROVISIONALs deferred as scene-layer / out-of-scope for videogame rebuild.

**Registers:**
- canon/editorial_ledger.yaml: archived ED-542..ED-658 batch (31 entries). Added ED-713, ED-714, ED-715 as resolution pointers.
- archives/editorials/editorial_ledger_archive_601_800.yaml: appended archival batch with note.
- canon/patch_register_active.yaml: PP-667 entry.
- references/canonical_sources.yaml: co-file note.

**Remaining work:**
- Propagation to source-doc OPEN ITEMS tables (setting settlement_layer §9 ED-SETT-01 to RESOLVED etc.) deferred. This is a mechanical update across 6 files; best handled as an infrastructure commit after engine_v4 smoke-test confirms the resolutions stand.

## 2026-04-19 — PP-668 OPEN ITEMS propagation (completes PP-667)

**Commit:** (this commit)
**Scope:** propagate PP-667 gap-sweep resolutions into the source-doc OPEN ITEMS tables. Closes the deferred propagation work flagged in PP-667.

**Files:**
- designs/territory/settlement_layer_v30.md §9 — 9 items with final status (4 RESOLVED, 1 CONFIRMED, 1 SUPERSEDED by PP-666, 2 DEFERRED, 1 N/A).
- designs/provincial/military_layer_v30.md §5 — 9 items (6 RESOLVED, 3 DEFERRED).
- designs/provincial/peninsular_strain_v30.md §8 — 7 items (4 CONFIRMED, 1 RESOLVED, 1 SUPERSEDED by PP-663, 1 N/A).
- designs/provincial/faction_layer_v30.md §10 — 9 items (7 RESOLVED, 2 DEFERRED).
- designs/provincial/victory_v30.md §11 — ED-311 CLOSED.

All new statuses reference PP-667 and the resolution document `designs/audit/gap_resolution_2026-04-19.md`.

**Registers:**
- canon/patch_register_active.yaml: PP-668 entry.
- references/canonical_sources.yaml: co-file touch.

**Consequences:** none new. Completes PP-667 propagation. No new editorial ledger entries needed (resolutions already logged under ED-713/714/715 in PP-667).

## 2026-04-19 — PP-670 Label accuracy audit

**Commit:** (this commit)
**Scope:** audit of all files with deprecation-suffix names (`_deprecated`, `_legacy`, `_historical`, `_superseded`). 71 files reviewed.

**Findings:**
- `designs/npcs/npc_roster_caste_annotations_deprecated.md`: correctly labeled. Merge into `npc_roster_v30.md §14` verified.
- `designs/threadwork/threadwork_v25_historical.md`: mislabel — filename said historical but no internal banner. **Fixed** — banner added pointing to canonical `threadwork_v30.md`.
- `tests/sim/sim_ttrpg_batch_legacy_02/03/04.md`: filename-only labels, no internal banners. Deferred as low-priority test-layer work.
- All 57 files in `deprecated/` directory correctly placed per `deprecated/README.md` policy.
- `params/threadwork_superseded.md`: correctly labeled internally, location intentional.

**Registers:**
- canon/patch_register_active.yaml: PP-670 entry.
- canon/editorial_ledger.yaml: ED-716 resolution entry.
- references/canonical_sources.yaml: co-file touch.

**Deferred:** sim_ttrpg_batch_legacy banner pass — not a blocker. Low reader-hazard; names are self-describing.

## 2026-04-19 — PP-671 Meta-throughline synthesis

**Commit:** (this commit)
**Scope:** synthesize 5 meta-throughlines from the 25 game throughlines; provide evaluative criteria for design proposals.

**New file:** references/throughlines_meta.md (15k chars)

**Meta-throughlines identified:**
- M-1 Decay-as-default — entropic baseline, instantiated by 8 throughlines
- M-2 Substrate-as-universal-medium — rendering/thread ontology across all systems, instantiated by 8 throughlines
- M-3 Institutional identity = mechanical attractor — each faction's distinct substrate-relationship, instantiated by 5 throughlines
- M-4 Scale-preserving chains — same throughlines fire at multiple scales, instantiated by 9 throughlines
- M-5 Forced-choice architecture — irreducible tradeoffs at every significant choice point, instantiated by 6 throughlines

**Findings:**
- Hafenmark, Löwenritter, and RM all lack their own institutional-attractor throughlines (M-3 gap). ED-717 logs this.
- PP-666's three new systems (settlement adjacency, fractional ownership, succession split) each strongly satisfy multiple meta-throughlines — validates PP-666 as vision-aligned design.
- Throughline-interaction matrix is sparse (7 throughlines covered of 25); recommended for future expansion.

**Registers:**
- canon/patch_register_active.yaml: PP-671 entry.
- canon/editorial_ledger.yaml: ED-717 entry (M-3 faction under-spec).
- references/canonical_sources.yaml: cross-reference note.

**No mechanical changes.** Pure synthesis / meta-analysis document.

## 2026-04-19 — PP-672 Throughlines hierarchical framework (canonical vetting guide)

**Commit:** (this commit)
**Scope:** adopt five-tier hierarchical framework as canonical vetting authority for all Valoria work. Supersedes PP-671 meta-throughlines document.

**Structure:**
- Ω (1) — Intent: belonging criterion with four clauses (cross-scale consequence, personal transformation, autonomous world, non-dominance); Thread-substrate ontology committed.
- Μ (4) — Modes: Pressure, Autonomous Composition, Substrate Ontology, Cross-Scale Consequence.
- М (6) — Meta-throughlines: Pressure is continuous, Geography holds pressure, Substrate grounds all, Institutions stake substrate-postures, Scales connect, Choice is forced.
- Τ (25) — existing throughlines, now tagged with primary/secondary М.
- Q — quality tier (robust, smooth, elegant) applied after belonging established.
- Μ̄ — Godot translation requirements.

**Protocol:**
- Scope classification (Class A new system → E cleanup), each with vetting depth.
- Failure lexicon (11 named failure modes).
- Authority: Jordan owns Ω/Μ; Claude applies full protocol; Ω failures flagged, never unilaterally rejected.

**Files:**
- references/throughlines_meta.md: full rewrite as skeleton (9k chars; loaded during routine vetting).
- references/throughlines_meta_infill.md: new; rationale, worked examples, full per-T tag table, Godot translation rationale, failure lexicon with examples (28k chars; loaded only when deeper context needed).
- canon/editorial_ledger.yaml: ED-718 adoption entry.
- canon/patch_register_active.yaml: PP-672 entry (supersedes PP-671).
- references/canonical_sources.yaml: framework named as vetting authority.

**Audit integration:** addresses 21 findings against PP-671 including Ω-substrate gap, personal-layer omission, Μ-triad agent-composition omission, М-tier misclassifications, missing vetting protocol, undefined audience, no connection to robust/smooth/elegant. Full change list in skeleton adoption notes.

**Consequences:**
- All future Class A proposals run through framework before approval.
- Existing canon grandfathered; retroactive audit deferred.
- Existing ED-717 gaps (Hafenmark/Löwenritter/RM substrate-postures) persist as open items against М-4.

## 2026-04-19 — PP-673 Terminology cleanup (skeleton → index for auto-gen files)

**Commit:** (this commit)
**Scope:** resolve three-way collision in the term "skeleton":
1. Canonical ruleset in mechanical-spec-only authorial style (banner SKELETON) — PRESERVED
2. Auto-generated heading/line/token navigation companion — RENAMED to "index"
3. depth string indicator for read-depth tracking — RENAMED from 'skeleton' to 'index'

Meaning #1 retains "skeleton" (correct usage). Meanings #2 and #3 migrate to "index".

**File renames:**
- 75 `*_skeleton.md` → `*_index.md` (auto-generated heading navigation companions)
- `tools/doc_index_gen.py` → `tools/doc_index_gen.py`

**Code migrations (skills/valoria-orchestrator/scripts/):**
- `github_ops.py`: `_route_to_skeletons` → `_route_to_indexes`, `read_skeleton` → `read_index`, `was_skeletonized` → `was_indexed`, `_skeleton_route_cache` → `_index_route_cache`, `_skeleton_reads` → `_index_reads`, `skeleton_path` → `index_path` (var), `[SKELETON ROUTE]` / `[SKELETON]` print tags → `[INDEX ROUTE]` / `[INDEX]`
- `valoria_hooks.py`: `assert_skeleton_before_full_read` → `assert_index_before_full_read`, `skeleton_only_paths` → `index_only_paths`, `already_fetched_without_skeleton` → `already_fetched_without_index`, all `depth='skeleton'` → `depth='index'`
- `tools/compliance_check.py`: `_check_skeleton` → `_check_index`, `find_skeleton_for` → `find_index_for`, rule fields `require_skeleton_above` → `require_index_above`, violation kinds `missing_skeleton`/`stale_skeleton` → `missing_index`/`stale_index`

**Skill doc updates:**
- `skills/valoria-orchestrator/SKILL.md`: terminology migrated throughout
- `skills/valoria-orchestrator/references/skill_registry.md`: terminology migrated
- `skills/valoria-atomizer/SKILL.md`: terminology migrated
- `skills/valoria-simulator/SKILL.md`: terminology migrated (including anti-pattern description)
- `references/file_index.md`: regenerated references

**Banner updates in 75 renamed files:**
- `<!-- SKELETON — auto-generated by skeleton_gen.py -->` → `<!-- INDEX — auto-generated by doc_index_gen.py -->`
- Title line `# foo — Skeleton` → `# foo — Index`

**NOT changed:**
- `<!-- SKELETON — mechanical spec only -->` banner on canonical rulesets (e.g., faction_layer_v30.md, throughlines_meta.md) — meaning #1, correctly named.
- Canonical rulesets themselves — only their auto-gen navigation companions.

**Session impact:** Next bootstrap session (re-loading github_ops.py and valoria_hooks.py from the skills directory) will pick up the new API. This session's in-memory copies use the old names but the skeleton-routing still works because the CACHE is empty each session and the routing code in the new copies will look for `*_index.md` files, which now exist.

**Registers:**
- canon/editorial_ledger.yaml: ED-719 entry.
- canon/patch_register_active.yaml: PP-673 entry.
- references/canonical_sources.yaml: cleanup note.

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

## 2026-04-29 — Topographic analysis v2 + v3 (PP-676)

Same-session execution: v2 TF-IDF methodology (validation FAILED) → v3 multi-graph
triangulation pivot (validation VALIDATED 2/3 structural properties).

**Files added/modified:**
- designs/audit/2026-04-29-topographic-analysis/00_workplan.md (REPLACED v1 with v3)
- designs/audit/2026-04-29-topographic-analysis/01_methodology.md (NEW; v2+v3 sections)
- designs/audit/2026-04-29-topographic-analysis/02_weakness_register.md (REPLACED v1 with combined v2+v3)
- designs/audit/2026-04-29-topographic-analysis/03_validation_report.md (NEW; v3 P1/P2/P3)
- designs/audit/2026-04-29-topographic-analysis/data/* (REPLACED v1 with v2+v3 outputs; .npz binaries dropped, JSON only — see methodology for reproducibility)
- canon/patch_register_active.yaml (PP-676 description + applied_commit updated)
- canon/editorial_ledger.yaml (ED-762 added)
- session_log_current.md (replaced with this session status)
- references/propagation_map.md (this entry)

**Propagation status:** complete in this commit. All findings are in the weakness
register pending Jordan review. v2 register sections retained as audit trail per
v3 §V3-13 v2→v3 diff.
