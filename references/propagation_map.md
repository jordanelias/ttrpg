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

## 2026-04-29 — Throughlines load-bearing systems column (PP-677)

Augments `references/throughlines_meta_infill.md` with a 6th column "Load-bearing
systems" mapping each of 43 active throughlines to canonical system slugs (from
`references/canonical_sources.yaml` `systems:` block). Conservative rule: only
systems whose absence prevents the throughline from operating are listed.

**Files modified:**
- references/throughlines_meta_infill.md (added Load-bearing systems column to T-NN table; editorial marker added at file head)
- canon/patch_register_active.yaml (PP-677 entry)
- canon/editorial_ledger.yaml (ED-764 entry)
- session_log_current.md (replaced with this session status)
- references/propagation_map.md (this entry)

**Propagation status:** complete in this commit. Pre-table and post-table content
byte-identical to prior version (modulo new editorial marker). Verified row-by-row:
44 rows preserved (T-01..T-09, T-10 STRUCK, T-11..T-41, T-15a/b/c). All original
column content (Title, Primary М, Secondary М, Justification) byte-identical.

**Cross-references:** PP-676 v3 §V3-2, ED-764.

**INTEGRITY FLAG — Jordan attention requested:**
ED-762 collision detected in `canon/editorial_ledger.yaml` active section. Two
entries share ID ED-762:
1. Topographic analysis v2+v3 entry (PP-676, this session-track)
2. doc 12 v1.2 production entry (separate session-track)

This appears to be a cross-session race condition: both sessions read the same
"next ED" before either committed. ED-763 has been deliberately skipped in this
commit; PP-677 uses ED-764. Jordan should renumber one of the duplicate ED-762
entries (suggest renumbering doc 12 v1.2 to ED-763 since it was the second
addition, but Jordan's choice).

## 2026-04-29 — Vocabulary debt sweep + ED-762 collision resolution (PP-678)

GM-to-engine replacement (17 sites) + 2 active CR cleanups (1 site) + ED-762
collision resolution (ledger renumbering).

**Files modified:**
- designs/threadwork/threadwork_v30.md (-67 chars; 12 Game Master → engine)
- designs/npcs/npc_behavior_v30.md (-24 chars; 3 Game Master → engine)
- designs/provincial/mass_battle_v30.md (-2 chars; 2 Game Master → engine)
- designs/architecture/complete_systems_reference.md (+74 chars; 2 active Cultural Reformation cleaned with STRUCK markers)
- canon/editorial_ledger.yaml (ED-762 collision resolved: doc 12 v1.2 entry renumbered to ED-763; 4 entries compressed for size; ED-765 added; 7,277 → 6,821 chars / ~1819 → ~1705 tokens)
- canon/patch_register_active.yaml (PP-678 entry)
- references/canonical_sources.yaml (no content change; included per co-file rule for design doc edits)
- session_log_current.md (replaced)
- references/propagation_map.md (this entry)

**Propagation status:** complete in this commit for GM + active CR + collision
resolution. Coup Counter sweep DEFERRED — substitution to Graduated Autonomy is
design-judgment work, not mechanical replacement.

**Cross-references:** PP-676 v3 §V3-9, PP-650 (CR strike), ED-781 (CC strike),
PP-677 (throughlines column), ED-765.

**Collision resolution detail:** Prior commit (f5da82b9, PP-677) flagged a
collision in active ledger where ED-762 was assigned to two distinct entries
(topographic v2+v3 / doc 12 v1.2). Resolution: doc 12 v1.2 entry renumbered to
ED-763 (which had been deliberately skipped in PP-677 commit precisely to allow
this resolution without renumbering interference). Topographic v2+v3 retains
ED-762 (was the first-arrived). Flag in PP-677 / ED-764 entries closed.

**Standing flags:**
- Coup Counter cleanup pending design-judgment review (10 sites across 7 files;
  suggested mappings in session log notes)

## 2026-04-29 — valoria-vector-audit skill enshrinement (PP-679)

Packages v3 multi-graph triangulation audit methodology (PP-676) as a reusable
directory-based skill. Reference run remains designs/audit/2026-04-29-topographic-
analysis/ as canonical executed implementation.

**Files added:**
- skills/valoria-vector-audit/SKILL.md (skill entry point with triggers, modes, common failure modes)
- skills/valoria-vector-audit/references/methodology.md (canonical v3 spec with locked thresholds)
- skills/valoria-vector-audit/references/diagnostic_modes.md (all 8 modes documented)
- skills/valoria-vector-audit/references/v1_v2_v3_history.md (institutional memory: 14 v2 problems, v3 corrections)
- skills/valoria-vector-audit/scripts/vector_audit.py (pipeline scaffold; full implementation references the v3 reference run)

**Files modified:**
- skills/valoria-orchestrator/references/skill_registry.md (new skill entry + 5 routing-table rows)
- canon/patch_register_active.yaml (PP-679)
- canon/editorial_ledger.yaml (ED-766)
- session_log_current.md (replaced)
- references/propagation_map.md (this entry)

**Propagation status:** complete. Skill is invocable from this commit forward
via skill call or trigger phrase from skill_registry.

**Cross-references:** PP-676 v3 (source methodology), PP-677 (Load-bearing systems
column — restored Mode F), PP-678 (vocabulary debt sweep — demonstrated Mode G
workflow), ED-766.

**Locked thresholds in methodology.md §3.7:** No post-hoc tuning. Threshold
deviation invalidates findings — this is the v2 lesson that v3 was designed
to prevent. Future operators must understand WHY each procedural choice was
tightened (see v1_v2_v3_history.md) before relaxing.

## 2026-04-29 — Coup Counter → Graduated Autonomy substitution (PP-680)

Completes PP-678 (which deferred CC due to non-1:1 substitution requiring
design judgment). Per ED-781 spec, applied substitution map across 6 active
sites in 4 files; preserved 4 leaves as historical/descriptive references.

**Substitution table (per ED-781):**

| CC value | GA stage |
|---|---|
| 0 | Loyal |
| 2 | Restless |
| 3 | Autonomous |
| 4 | Split |

**Files modified:**
- designs/npcs/npc_behavior_v30.md (1 active rewrite)
- designs/architecture/complete_systems_reference.md (1 active rewrite — Arcs A/C)
- designs/provincial/victory_v30.md (3 active rewrites — Season gate, §3.6a header, §3.6a item 4)
- designs/architecture/conflict_architecture_proposal.md (1 active rewrite — §Recommendation L157)
- canon/patch_register_active.yaml (PP-680 entry)
- canon/editorial_ledger.yaml (ED-767 entry)
- references/canonical_sources.yaml (no content change; included per co-file rule)
- session_log_current.md (replaced)
- references/propagation_map.md (this entry)

**Leaves (intentionally preserved):**
- canon/03_canonical_timeline.md L92 (worldbuilding — Coup Counter as enforcement
  mechanism is conceptual political-historical reference, not the mechanic)
- designs/architecture/campaign_architecture_v30.md §5.3 L179 (describes strike:
  "Loyal → Restless → Autonomous → Split, replacing the binary Coup Counter")
- designs/architecture/conflict_architecture_proposal.md L37, L78 (argument FOR
  Graduated Autonomy referencing what it replaces)

**Cross-references:** PP-676 v3 §V3-9, PP-678 (GM + active CR sweep, CC deferred),
ED-781 (Graduated Autonomy spec), ED-767.

**Standing:** vocabulary debt sweep complete for the 3 terms identified in v3
audit (Game Master, Cultural Reformation, Coup Counter).

## 2026-04-29 — Conviction Track promotion (PP-681)

Addresses PP-676 v3 §V3-5 multi-graph isolate finding. Conviction Track was
canonical and central but lived inline in npc_behavior_v30 with no own file.
Now has first-class doc status.

**Files added:**
- designs/personal/conviction_track_v1.md (4,834 chars; canonical extraction
  + banner + cross-references)

**Files modified:**
- designs/npcs/npc_behavior_v30.md (-3,835 chars; §1.2 + §3.3 + §3.4 replaced
  with redirect stubs)
- designs/architecture/scale_transitions_v30.md (+50 chars; L219 cross-ref
  updated 'npc_behavior_v30 §3.4' → 'conviction_track_v1.md §3, formerly
  npc_behavior_v30 §3.4')
- references/canonical_sources.yaml (~+200 chars; conviction_track.design_doc
  repointed at new file; SHA placeholder PENDING_FIRST_COMMIT to be filled in
  follow-up commit; original npc_behavior listed as 'related' for traceability)
- canon/patch_register_active.yaml (PP-681)
- canon/editorial_ledger.yaml (ED-768)
- session_log_current.md (replaced)
- references/propagation_map.md (this entry)

**SHA follow-up required:** canonical_sources.yaml has
canonical_sha__designs__personal__conviction_track_v1_md = "PENDING_FIRST_COMMIT".
After this commit lands, fetch the new file's blob SHA and update with a
follow-up no-op-content PP. This is standard procedure for new canonical
files — the SHA can't be set until the file exists.

**Stub-redirect strategy:** Original §1.2 / §3.3 / §3.4 sections in
npc_behavior_v30 retain their headers + a 1-2 sentence redirect to the new
canonical file. Existing references that cite npc_behavior_v30 file-level
still resolve correctly. Only one explicit cross-section reference was found
(scale_transitions §3.4) and was updated; broader cross-reference audit
recommended in future session.

**Bonus cleanup:** 3 'GM' references inside §3.3 table cells (missed by
PP-678 because 'GM' bare differs from 'Game Master' full phrase) replaced
with 'engine' equivalents in the extracted version. PP-678 used "Game Master"
exact-match; bare "GM" is a separate sweep candidate for future PP.

**Cross-references:** PP-676 v3 §V3-5 (source finding), PP-678 (parent
vocabulary debt sweep, missed bare 'GM'), PP-680 (CC sweep, also a v3 §V3-9
follow-up), ED-663/ED-664/ED-672 (source authority for Conviction mechanics),
ED-768.

**Standing flags:**
- Bare 'GM' references may exist elsewhere in design corpus (3 found and
  fixed in §3.3 extraction; full corpus sweep not done in this PP)
- canonical SHA follow-up commit needed for the new file

## 2026-04-29 — Conviction Track SHA follow-up (PP-682)

PP-681 set canonical_sources.yaml SHA placeholder PENDING_FIRST_COMMIT
(file didn't exist yet). After PP-681 commit (4802e83b) landed, fetched
new file blob SHA 32d8e3412d17157fc0fd27fed91a0e11262743ef and updated.

**Files modified:**
- references/canonical_sources.yaml (SHA placeholder filled, note removed)
- canon/patch_register_active.yaml (PP-682)
- canon/editorial_ledger.yaml (ED-769)
- session_log_current.md (replaced)
- references/propagation_map.md (this entry)

**Cross-references:** PP-681 (Conviction Track promotion), ED-769.

## 2026-04-30 — Mass Battle MB-01..08 editorial-decision batch (PP-683..688, ED-770)

Jordan editorial approval applied 2026-04-30 to the 8 Jordan-decision items
from designs/audit/mass_battle_patch_proposals_2026-04-29.md, plus PROVISIONAL
marker strip on PP-500/501/502/503/504. The 8 auto-approvable patches
(PP-PROP-MB-01..08) had already been applied in prior sessions and were
verified in-place via inspection.

**Decisions applied:**
- MB-01 (Stalemate Break): Option A — design doc Tactical Withdrawal wins;
  params/mass_combat.md §PP-297 rewritten to match. No Rout possible from
  stalemate; battle ends inconclusive; IP +1 at Accounting.
- MB-02 (Muster initial Size): Option C — §1.2 column relabeled TARGET Size;
  §1.4 governs base muster output (PP-687).
- MB-03 (Morale reset): Option A — Morale resets to starting formula at each
  new battle (PP-684).
- MB-04 (Discipline recovery): Option B — Discipline persists across battles;
  recovery via Muster only (PP-685). §1.7 cross-reference added.
- MB-05 (Rout contagion brake): already applied prior session — verified at
  mass_battle_v30 §A.4.
- MB-06 (Shadow Intel resolution): Option A — Peek mechanism specified
  (PP-686). UI: Varfell sees opponent's committed card, may swap from hand,
  both reveal simultaneously.
- MB-07 (Siege pool formula): Option A — Pool = Mil + 3 (PP-688). Resolves
  MATH-FAIL-01: Fort 3 + Mil 4 now Ob 5 from pool 7 ≈ 2% match (prior
  formula was 0%).
- MB-08 (Encirclement no-cap): Applied (PP-683). Morale −3 cap removed when
  unit has no valid retreat path (3-direction flank OR all retreat zones
  occupied). Stage 2 general kill remains additive.

**PROVISIONAL strip:** PP-500 (Shield Wall +2D simul), PP-501 (Coherence
depletion), PP-502 (Discipline check deterministic), PP-503 (Volley Power-only),
PP-504 (Command per sub-unit) — all confirmed by editorial approval; PROVISIONAL
markers replaced with stripping note.

**Files modified:**
- designs/provincial/mass_battle_v30.md (~+2400 chars; §A.4 cap exception, §A.13
  reset/persists, §B.4 Shadow Intel resolution, 5 PROVISIONAL strips)
- designs/provincial/military_layer_v30.md (~+1250 chars; §1.2 TARGET relabel,
  §1.7 between-battle cross-ref, §1.9 Siege pool fix)
- params/mass_combat.md (~+460 chars; §PP-297 Stalemate rewritten)
- canon/patch_register_active.yaml (PP-683..688 entries + vetting blocks)
- canon/editorial_ledger.yaml (ED-770)
- canon/editorial_ledger_summary.yaml (next_id 770→771; ED-770 noted)
- references/canonical_sources.yaml (mass_battle, mass_combat, military_layer
  SHAs set to PENDING_PP_689 — follow-up SHA commit required)
- references/propagation_map.md (this entry)

**SHA follow-up required (PP-689):** canonical_sources.yaml has 3 SHAs set to
PENDING_PP_689. After this commit lands, fetch new blob SHAs for the 3 modified
canonical files and update via PP-689 follow-up commit. Standard procedure.

**Downstream propagation candidates (audit-flagged, not blocking):**
- compilation/v0.14/stage8_combat.md — already marked OUTDATED in file_index;
  any future re-compile must pull from updated canonical files.
- designs/audit/mass_battle_stress_test_2026-04-29.md, mass_battle_patch_proposals_2026-04-29.md —
  source documents of this batch; remain as historical record.
- designs/architecture/scale_transitions_v30.md — no direct mass-battle
  cross-reference identified, but Discipline/Morale persistence semantics
  may impact zoom-in/zoom-out edge cases. Future audit candidate.

**Cross-references:** PP-PROP-MB-01..08 (auto-approvable, prior session,
verified in-place), MB-01..08 editorial decisions, ED-770, MATH-FAIL-01,
S-FAIL-05/06/13/19, designs/audit/mass_battle_patch_proposals_2026-04-29.md.

**Standing flags:**
- PP-689 SHA follow-up commit needed (next session priority).
- Geography × hex/square map × distance/orientation stress test follows this
  commit (next-action item).

## 2026-04-30 — Stratagem rename + information-model correction (PP-690, ED-771)

Tactic card "Shadow Intel" (Varfell faction-specific card 1, mass_battle_v30 §B.4)
renamed to **Stratagem**. Mechanic preserved — Varfell reads opponent's tactic
card before locking own; may revise once; both reveal simultaneously thereafter.
PP-690 supersedes PP-686 naming.

**Reframe rationale:** Varfell faction profile per Vaynard is *cunning + immensely
proud*. Vaynard refuses anything publicly seen as cowardly; he embraces what is
commonly recognized as classical battle stratagem. "Shadow Intel" coded the card
sneaky/secretive — wrong register. "Stratagem" is the prestige-doctrine framing:
Hannibal at Trasimene, Belisarius reading Persian commitments, Mongol envelopment
reads. Same mechanic, correct framing.

**Information-model correction also applied:** PP-686 resolution paragraph used
"simultaneous-secret commit" framing for tactical-layer mechanics. This was
incorrect. Tactical-layer (mass battle, personal combat) uses initiative-determined
reveal with simultaneous resolution — initiative-holder sees lower-init's
declaration before locking own (UI v4 §7.4.2). NO hidden commits at tactical scale.
Stratagem is mechanically an initiative inversion at the tactic-card resolution
layer (Varfell becomes higher-init for that one card, regardless of Speed/Command),
not a hidden-commit override.

**Strategic-layer (faction-season) is the only scale that retains hide-until-reveal**
because no initiative exists at faction-scale to determine declaration order —
simultaneous-reveal is the fairness-consequence of that absence, not commit-asymmetry-
as-feature. Strategic encounters that resolve into mass battle transition from
no-initiative (strategic) to initiative-exists (tactical) at the engagement
handoff. Strategic-layer fog-of-war on enemy positions persists across reveal —
order reveal lifts fog on enemy *orders*, not enemy *positions*.

**Files modified:**
- designs/provincial/mass_battle_v30.md §B.4 (table row + resolution paragraph)
- canon/patch_register_active.yaml (PP-690 entry + vetting)
- canon/editorial_ledger.yaml (ED-771)
- canon/editorial_ledger_summary.yaml (next_id 771→772; ED-771 noted)
- references/canonical_sources.yaml (mass_battle SHA still PENDING — extends
  the placeholder window from PP-689 to cover both ED-770 and ED-771 changes;
  single SHA followup commit will resolve both)
- references/propagation_map.md (this entry)

**Cross-references:** PP-686 (Shadow Intel original, superseded by PP-690),
ED-770 (MB-06 batch), ED-771 (this rename), Vaynard faction profile (npc/faction
docs — discovery sweep pending for low-Military/sneaky/raider language).

**Standing flags:**
- Niflhel strike scope discovery pass queued (next operation).
- Varfell descriptor reframe discovery pass queued (after Niflhel).
- Hafenmark equipment-quality / Crown-Löwenritter / Crown-fragility design
  notes queued for the comprehensive faction-doctrine commit that follows the
  two discovery passes.
- PP-689 SHA followup still pending (now covers two content commits' worth
  of changes to mass_battle_v30 etc).




---

## 2026-04-30 — PP-698 / ED-775 — Terminology P0 propagation pass

**Trigger:** 2026-04-30 vector-audit (designs/audit/2026-04-30-terminology-vector-audit/) §11.1 P0 actions. Audit committed at SHA eae4eb0b61a718a9.

**Five actions executed:**

1. **TC → CI sweep in designs/npcs/npc_behavior_v30.md.** All 26 mechanical TC mentions (across 17 paragraphs) renamed to CI. Context-verified Church-Influence (not Conviction Track). Resolves the alias_registry collision_table.tc.status='resolved' contradiction surfaced by Mode G — pre-PP-698: 21 actionable TC residuals in design corpus, 16 of them in this single doc.

2. **RS → MS + TC → CI sweep in references/throughlines_meta_infill.md.** T-04 row "RS Decay" → "MS Decay"; T-05 row "TC Accumulation" → "CI Accumulation"; plus 5 body residuals (M-3 historical reference, T-18 description, T-21 description, Τ check section, Failure Lexicon Reskinned-attractor + Cost-hidden examples).

3. **references/glossary.md rewrite.** Added Disposition + Domain Action under Part Seven (Mode D cascade sinks 391 + 346 chains; both lacked first-class docs and glossary entries). Added new Part Eleven for top-level systems missing from glossary (Peninsular Strain, Conflict Architecture, Campaign Architecture, Victory, CI Political — Mode A multi-graph hubs). Reconciled Part Two CI threshold row to ci_political_v30 §2.1 canonical (40 / 55 / 60 probabilistic Mass Seizure / 65 / 80 / 100 — old 75 = territorial seizure threshold REMOVED per supersession_register entry 250715f; glossary now reflects). Replaced stale Part 12 (TERMS FLAGGED AS UNRESOLVED) with new Part 13 (DEPRECATED / RESOLVED ABBREVIATIONS) reflecting alias_registry deprecated_abbreviations block. Old Part 11 collision table renumbered to Part 12; added RS legacy entry. Added VG-target preamble per project instructions. Added Game Master engine-resolution note per "There is no GM" directive. Disambiguations added: Coherence/Intelligibility, TT/MS opposite-direction, CE/Stamina, Belief/Inspiration/History.

4. **references/alias_registry.yaml updates.** church_influence: structured milestones map (40/55/60/65/80/100) + accurate threshold note. collision_table.tc.resolution corrected from "Disambiguation sweep completed 2026-04-26" (false per Mode G) to "resolved at term level; corpus residuals 16 in npc_behavior_v30 swept this commit; ~2 paragraphs queued". status: resolved_term_partial_corpus. Disposition + Domain Action added under world_narrative.

5. **references/censured_vocabulary.yaml stub populated.** 11 entries from supersession_register + alias_registry legacy_renames + collision_table + audit Mode G corpus counts: VTM, Vaynard Thread Mastery, Cultural Reformation, Combat Power, Cohesion, Thread Depth, Rendering Stability, Theocracy Counter, TC (as Church Influence), Coup Counter, Niflhel-as-faction, GM (bare). Each entry includes residual_count and residual_concentration from 2026-04-30 audit Mode G.

**Files modified:**
- references/glossary.md
- references/alias_registry.yaml
- references/censured_vocabulary.yaml
- references/throughlines_meta_infill.md
- designs/npcs/npc_behavior_v30.md
- references/canonical_sources.yaml (Last touched comment)
- canon/patch_register_active.yaml (PP-698 entry + vetting)
- canon/editorial_ledger.yaml (ED-775; next_id 772 → 773)
- references/propagation_map.md (this entry)
- session_log_current.md

**Cross-references:** PP-679 skill (vector-audit), PP-678 (prior Game Master sweep — full-phrase only, complementary scope), ED-731 (RS→MS rename original), ED-782 (TC→CI rename original), ED-781 (Coup Counter → Graduated Autonomy), ED-764 (Niflhel-as-faction strike), ED-706/ED-707 (VTM/CR strikes), supersession_register entry 250715f (CI 75-threshold removal).

**Mode G post-sweep state:** TC=Church-Influence reduced from 21 → 2 actionable (16 npc_behavior_v30 cleared + 3 throughlines_meta_infill cleared this commit; remaining residuals: npc_character_analyses_v30.md (1) + mass_battle_v30.md (1)).

**Standing flags:**
- P1 actions deferred to next directive: Wager + Thread Revelation isolate promotion; Convictions framework registration (Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity); Pressure Points framework registration (Evidence/Consequence/Authority/Loyalty); three-doc Cohesion → Discipline sweep; bare GM corpus sweep (29 paragraphs, 14 docs).
- P2 actions deferred: VTM full sweep + Varfell victory-path editorial rewrite; Cultural Reformation cleanup in peninsular_strain_v30; Niflhel faction-context audit; Coup Counter → Graduated Autonomy per-site substitution; Armature System + Event Impact Matrix status clarification.
- Methodology follow-up: P2 conviction-symmetry audit (investigate whether Conviction-bearing throughlines list Conviction tokens in Load-bearing systems column); re-run vector-audit after P0+P1 land.
- PP-689 SHA followup still pending (covers two content commits' worth of changes; queued from PP-690 propagation note).

## 2026-04-30 — Comprehensive faction-doctrine batch (PP-698..697, ED-775, +ED-776/774 standing)

Major editorial pass completing several long-running threads:

**1. Niflhel residue strike (PP-698).** Most of Niflhel was already struck per
CR-STRIKE-2026-04-19 / PP-DISSOLVE / conflict_architecture_proposal §Niflhel
Dissolution / ED-752 / ED-764. This patch removes residual references that
survived prior strikes — registry entries, STRUCK-marker debris in params,
Niflhel-pair byproducts in compound clauses, faction_layer treaty/trigger/NPC-list
rows. Niflhel as a faction-level entity is now fully retired from active canon.
Functions distributed to settlement-broker mechanic (settlement_layer §4.7-4.9).

**Files modified by Niflhel strike:**
- references/alias_registry.yaml (DD entry decoupled from Niflhel)
- references/proper_noun_registry.yaml (niflhel: block deleted; Dalla Virke
  reassigned to settlement-broker)
- references/proper_noun_triage_decisions.yaml (niflhel: block deleted)
- params/contest.md (table row + §Niflhel Social Toolkit deleted)
- params/factions_personal.md (table row + STRUCK explanatory block deleted)
- params/bg/npc_priority_trees.md (§Niflhel Priority Tree deleted x2)
- params/factions/stats_1_7_scale.md (§Niflhel — The Quiet Network deleted)
- params/bg/institutions.md ("Niflhel or Varfell" → "Varfell" x2)
- params/bg/ministry.md (§Niflhel Network Starting Depth deleted)
- params/factions/npc_stance_triangles.md (Amoral Consequentialism row deleted)
- params/fieldwork.md (Niflhel social action modifier row deleted)
- params/board_game.md (TOC entry deleted)
- params/bg/military.md (Niflhel Harvest strikethrough → Settlement-Broker Harvest)
- params/bg/core.md (STRUCK comments cleaned x2)
- designs/provincial/faction_layer_v30.md (Trigger 4 row, §4.1 Niflhel row,
  §6 BG NPC list — all Niflhel refs removed)

**Deferred (ED-777 standing):** arc_register_factions.md has 5 Niflhel-coded
arcs (ARC-S11 Headless Network, ARC-S54 Quiet Overreach, ARC-S55 Arms Out of Sync,
NPC-ARC-VIR Virke Recall, ARC-T25 Virke Family Ultimatum) that require plot-level
reframe to settlement-broker mechanic. Dedicated arc-reframe session needed —
each arc's four-arm structure or Virke trust-network plot needs design-level
reconception, not just term swap.

**2. Vaynard first name canonicalized (PP-699, resolves ED-NEW-02).** Magnus
Vaynard, "The White Wolf." Lore-form "Dienton Vaynard" superseded.

**3. Hafenmark equipment-quality doctrine note (PP-700).** Doctrine canon fixed:
Hafenmark Military 4 expressed as superior equipment quality from mining
(T17 Halvarshelm) and smithing (T8 Gransol). Mechanical expression TBD via
simulation testing — flagged as ED-776 standing item. Note inserted at
faction_layer §1.5 + military_layer §1.3.

**4. Crown standing army doctrine note (PP-701).** Crown's pre-coup standing
military force is the Löwenritter Order. Crown Military 5 expressed through
Löwenritter Power 5 / Discipline 6 elite units. Löwenritter row in mass_battle
§B.4 represents post-coup independent-faction scenario. Note inserted at
faction_layer §1.5 + military_layer §1.3.

**5. Crown structural-fragility doctrine note (PP-702).** Almud's "least bad
option" framing canonized. Crown holds highest perceived strength + is most
structurally fragile (assailed from Altonia/Schoenland/Restoration/Church/
Hafenmark/Varfell/Löwenritter simultaneously). Fragility is structural, not
stat-based. Note inserted at faction_layer §1.5.

**6. mass_battle §A.11 PP-MB-06 correction (PP-703).** Previous draft incorrectly
gated Varfell Southernmost units on "VTM ≥ 2" (VTM struck per params/bg/core L6)
and implied a faction-property exemption from the Forgetting (the Forgetting is
universal — every individual entering Askeheim must have personal TS ≥ 30 or
dissolves). Corrected: no faction can field a conventional military force in the
Southernmost; only Restoration communities and ad-hoc TS ≥ 30 expeditions can.
Faction-property exemptions impossible by mechanism.

**7. Edeyja L61 conflict-as-disturbance redirect (PP-704).** Replaced
Niflhel-supply-chain plot driver with canonical principle: mass battles,
destructive Thread operations, and faction conflicts ALL generate trace Thread
disturbance Edeyja senses (mass_battle §E.1 MS −1/battle; calamity_radiation
§[THREAD]-tagged Domain Actions, PP-531). No replacement plot driver invented —
redirected to existing mechanic.

**Files modified (consolidated, all 7 patches):**
- references/alias_registry.yaml
- references/proper_noun_registry.yaml
- references/proper_noun_triage_decisions.yaml
- references/glossary.md (no edit — already correct from prior pass)
- params/contest.md
- params/factions_personal.md
- params/bg/npc_priority_trees.md
- params/factions/stats_1_7_scale.md
- params/bg/institutions.md
- params/bg/ministry.md
- params/factions/npc_stance_triangles.md
- params/fieldwork.md
- params/board_game.md
- params/bg/military.md
- params/bg/core.md
- designs/provincial/faction_layer_v30.md (Niflhel strikes + §1.5 doctrine notes)
- designs/provincial/mass_battle_v30.md (§A.11 PP-MB-06 correction)
- designs/provincial/military_layer_v30.md (§1.3 doctrine notes)
- designs/npcs/edeyja_npc.md
- designs/world/worldbuilding_v30.md
- canon/patch_register_active.yaml (PP-698..697 + vetting)
- canon/editorial_ledger.yaml (ED-775, 773, 774)
- canon/editorial_ledger_summary.yaml
- references/canonical_sources.yaml (SHA placeholders → PENDING_PP_705)
- references/propagation_map.md (this entry)

**Standing follow-ups:**
- ED-776 (P3 standing): Hafenmark mechanism TBD via simulation
- ED-777 (P2 standing): arc_register_factions Niflhel reframe — 5 arcs need
  plot-level reframe in dedicated session
- PP-698 SHA followup pending — canonical_sources.yaml has placeholders for
  4 modified files (mass_battle_v30, military_layer_v30, faction_layer_v30,
  params/mass_combat). Fetch new blob SHAs after this commit lands and update.

**Cross-references:** CR-STRIKE-2026-04-19, PP-DISSOLVE, conflict_architecture_proposal
§Niflhel Dissolution, ED-752, ED-764, ED-770, ED-771, PP-686/PP-690 (Stratagem
rename context), PP-MB-06, ED-NEW-02, params/bg/core L4-L9 (Vaynard military-conqueror
canon).




---

## 2026-05-01 — PP-705 / ED-778 — Phase 0 cleanup (workplan v2 §0)

**Trigger:** Three P0 defects from ecosystem workplan v2 §0 (T1, D1, B1).

**Three actions executed:**

1. **T1 — npc_behavior_v30.md stale-threshold markers.** 5 lines containing CI threshold gates flagged: L791 `CI < 75 AND Mandate ≥ 4` (Church Assert priority); L1115 `CI ≥ 50` (non-canonical milestone, nearest is 55 = Institutional Reach); L1122 `CI ≥ 75` (Graduated Seizure — territorial-seizure threshold removed per ED-782 / ci_political §2.1); L1123 `CI < 75` (paired with L1122). L1135 `CI ≥ 40` left unmarked (40 = Church Assertive is canonical). Markers reference ci_political_v30 §2.1 canonical milestone set: 40 / 55 / 60 (probabilistic Mass Seizure with P = ((CI-60)/40)^3.3) / 65 / 80 / 100. Design-judgment update to canonical probabilistic logic deferred — branch logic change non-trivial.

2. **D1 — Glossary cross-reference grep.** 423 files scanned across canon/, designs/, references/, params/. Patterns: `glossary §11`, `glossary §12`, `Part Eleven`, `Part Twelve`, `UNRESOLVED`. 111 matches. All matches are self-referential documentation: audit folder describing the rename (PP-691), workplan describing the rename, propagation_map describing the rename, patch_register entry describing the rename, alias_registry section header (empty section). **No external broken cross-references found.** D1 closed without code change.

3. **B1 — Mode G case-sensitivity corrigendum.** Audit folder `designs/audit/2026-04-30-terminology-vector-audit/01_methodology.md` §8 appended with corrigendum disclosing the defect: context-filter regex was case-sensitive; pattern `(?:Theocracy|Church|Influence|Mass Seizure|seizure|threshold|Holy)` would not match capitalized variants on alternative branches. Re-run with `re.IGNORECASE` and post-PP-691 corpus state shows minor numerical Δ — most of TC's -19 paragraph reduction is attributable to PP-691's npc_behavior_v30 + throughlines_meta_infill cleanup, not the case fix. New file `data/mode_g_2026-04-30_corrigendum.json` with corrected counts; audit-time `mode_g_2026-04-30.json` preserved (frozen-on-creation convention). 02_weakness_register.md §1 prefaced with corrigendum note pointing to methodology §8. Audit-time §1.1 numbers preserved as historical record. **Methodology fix in canonical code scheduled for Phase 5 of ecosystem workplan v2.**

**Files modified:**
- designs/npcs/npc_behavior_v30.md (T1 markers)
- designs/audit/2026-04-30-terminology-vector-audit/01_methodology.md (B1 §8 corrigendum)
- designs/audit/2026-04-30-terminology-vector-audit/02_weakness_register.md (B1 corrigendum pointer)
- designs/audit/2026-04-30-terminology-vector-audit/data/mode_g_2026-04-30_corrigendum.json (NEW)
- canon/patch_register_active.yaml (PP-705)
- canon/editorial_ledger.yaml (ED-778; next_id 778 → 779)
- references/canonical_sources.yaml (Last-touched comment)
- references/propagation_map.md (this entry)
- session_log_current.md (full session arc + Phase 0 close)

**Cross-references:** PP-679 vector-audit skill (B1 fix-target for Phase 5), PP-691 (TC sweep that PP-705 follows up), ED-782 (TC→CI rename original; ci_political §2.1 thresholds), workplan v1 (7cf88ce6a, superseded), workplan v2 (6b0d0f424, draft pending ratification).

**Register health flag:** This commit pushes 4 of 5 registers past 90% of WARN thresholds. Archival pass urgent — workplan v2 Phase 2.5 candidate.

**Standing flags (unchanged from PP-691):**
- PP-689 SHA followup still pending (now covers PP-690 + PP-691 + PP-705 file edits — single SHA-update commit pending).
- Workplan v2 ratification gates Phase 1+.
- Concurrent-session ID hazard partially mitigated (assert_unique_ids hook 24ea3b9b0); stale-snapshot reasoning hazard remains until Phase 4.
