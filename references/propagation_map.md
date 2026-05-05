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


## Pre-2026-05-01 entries archived to archives/propagation/propagation_map_archive_2026_05_01_c.md

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


---

## PP-684/685/686/687/688 — 2026-05-01 — Architecture session ratification (5 PPs)

**Trigger:** 2026-04-30 architecture session ratification per integration plan `designs/audit/2026-04-30-architecture-session/16_open_items_NERS_integration_plan.md` (commit 9230603, 800 lines).

**Six commits executed (per integration plan §3.2):**

1. **PP-687 substrate (commit d2a75fc):** designs/architecture/key_substrate_v30.md + designs/architecture/key_type_registry_v30.md created. canonical_sources.yaml updated; PP-665..674 trace comments archived to free space.
2. **PP-684 + PP-685 taxonomy + roster (commit 8d31419):** designs/personal/conviction_taxonomy_v30.md + designs/personal/conviction_migration_roster_v30.md created. 13-Conviction taxonomy with Honor as 13th per integration plan D1; 9 named character migrations + 4 placeholders + 4 edge cases.
3. **PP-686 v2 faction architecture (commit dede72f):** designs/provincial/faction_behavior_v30.md created. C1-C10 calibration set applied; D3 multi-root cascade; D4 4-trigger Mission shift; D12 drift_coef=0.6.
4. **PP-688 articulation layer (commit b633778):** designs/articulation/articulation_layer_v30.md created. 8-trigger ruleset per D10; pacing deferred per D11; 3 Class B Key types added (meta.knot_formed retained, meta.knot_ruptured + state.belief_revised new).
5. **Conviction → axis matrix (commit 98f492a):** designs/personal/conviction_axis_matrix_v30.md created. 13 × 4 = 52-cell matrix with per-row Renaissance-grounded calibration rationale.
6. **Register entries (this commit):** PP-684/685/686/687/688 added to patch_register_active.yaml with full vetting blocks; SUPERSESSION-PP687-001/002/003 + SUPERSESSION-PP686-001 to supersession_register.yaml; substrate_aliases section added to alias_registry.yaml.

**12 Jordan-decisions resolved** (per integration plan §3.4, signed off by delegation):
D1=Honor 13th YES · D2=4-axis accepted, 5th Class B if needed · D3=multi-root cascade · D4=4 Mission-shift triggers · D5=PP-687 schema approved · D6=7×30 type registry · D7=visibility default-from-scene · D8=phased rollout · D9="Key" retained · D10=8 initial triggers · D11=pacing deferred · D12=drift_coef=0.6.

**Files modified:**
- designs/architecture/key_substrate_v30.md (NEW)
- designs/architecture/key_type_registry_v30.md (NEW)
- designs/personal/conviction_taxonomy_v30.md (NEW)
- designs/personal/conviction_migration_roster_v30.md (NEW)
- designs/personal/conviction_axis_matrix_v30.md (NEW)
- designs/provincial/faction_behavior_v30.md (NEW)
- designs/articulation/articulation_layer_v30.md (NEW)
- canon/patch_register_active.yaml (5 PP entries)
- canon/supersession_register.yaml (4 supersession entries)
- references/alias_registry.yaml (substrate_aliases section)
- references/canonical_sources.yaml (7 source entries; PP-665..674 trace archived)
- references/propagation_map.md (this entry)

**Status:** All 7 docs PROVISIONAL. Stage 10 verification battery (per integration plan §3.5) required before promotion to canonical: lateral cross-system simulation (faction × mass_battle × social_contest at scene scale + Strain interaction), articulation-layer simulation (significance scoring, 8-trigger firing rate, chronicle prose generation, K/B/I integration, determinism), production-engine determinism verification during Phase 5a Godot.

**Phase 5a Godot scope updated:** original 5 sessions → 7.5-8.5 sessions per integration plan §3.5 — adds diagnostic UI (2 sessions: faction dashboard, Memory viewer, CAUSAL_GRAPH walker, arc-resolution notifications) + cut scene rendering (1-2 sessions: Tier 2 5-15s + Tier 3 30-90s annual chronicle paragraphs).

**NERS verdict at session close:** 17 STRONG / 5 STRONG-conditional / 4 MODERATE / 0 WEAK. 4 lateral+diagonal directions transitioned WEAK→STRONG. Story-vs-happenings probability raised from substrate-alone ~15% to PP-688-complete ~75-85%.

**Out of scope (carried forward):**
- PP-666 trio (settlement adjacency ED-710, fractional province ED-711, succession split) — Phase 1 P2 carryover.
- Workplan v3 ↔ commit ID linkage (week-audit R5).
- PROVISIONAL→canonical sweep for ED-750/751/752/753/754/762/764, PP-297/351/653 (week-audit R6).
- Mass-battle decision queue (16 items, MB-01..08 + INTER-10d/12b/14a/14d/14e/12e/17b/09d).
- Pacing system (future PP per artifact 10 §10.5).

## 2026-05-01 — Geography canon audit + Phase 1 (PP-706, ED-779/780/781)

Pre-spec-rewrite audit conducted on geography canon. Findings: canon is more
substantial than prior session synthesis suggested — narrative regions
(geography_v30.md), 17-territory adjacency (jsx + table), 36-settlement registry
(settlement_layer §2.1), and visual map (SVG) are largely authored. The
disconnect is mechanical: settlement_adjacency_v30 uses abstract edge-typing
(Road/River/Mountain Pass/Coastal labels on graph-edges) and doesn't reference
the (x,y) coordinate data or geographic terrain features that already exist.

**Findings summary:**
- 9 gaps (G1-G9) blocking v2 mechanical spec authoring: settlement-level coords,
  province polygons, typed terrain layer, terrain-cost matrix, vision-range,
  weather/season-modulated mechanics, march-bubble layer, geographic
  battle-terrain derivation, naval mechanics
- 5 bugs (C1-C5): coordinate-system disconnect (abstract jsx vs visual SVG);
  SVG pass-label errors (in-SVG); Lake Eidursjø geometry conflict with T4 jsx
  position; SVG is structurally pre-canon (different territory numbering schema —
  e.g., SVG T2=Sigurdshelm, canon T2=Kronmark; SVG T8=Lowenskyst, canon T8=Gransol;
  no surgical fix possible); Schoenland sea route flagged but not modeled.

**Phase 1 strike (this commit):**
- Audit report committed at designs/audit/2026-04-30-geography-audit/00_audit_report.md
- valoria_map_v2.svg deprecated via banner-comment (retained as historical
  reference — visual peninsula shape, mountain geometry, lake position,
  calamity rings remain correct; territory labels/numbering do not)
- Standing items minted ED-779 (Phase 2 data authoring), ED-780 (Phase 3 spec
  rewrite), ED-781 (Phase 4 stress tests — three queued scenarios)

**Sequencing established for v2 geography work:**
- Phase 1 (this commit): bug fixes + audit + standing items minted
- Phase 2 (ED-779, P2): data authoring — coordinate system, settlement coords,
  province polygons, terrain layer, terrain-cost matrix, vision-range tables,
  weather/season modifier tables. Output: valoria_geography_v30.yaml + redrawn map.
- Phase 3 (ED-780, P2): spec rewrite — settlement_adjacency v2 (geography-querying),
  new march_layer_v30, mass_battle terrain-derivation update, naval mechanics
  (resolves ED-055 standing since 2026-04-05).
- Phase 4 (ED-781, P3): three stress tests — Mountain Pass battle, Open-field
  cavalry encounter, Coastal landing.

**Also flagged:** Pre-existing PP-684..688 collision in patch_register_active.
My applied mass-battle-MB-batch entries (date 2026-04-30, status: applied,
commit cd09b98) collide with another session's provisional architecture-work
entries (date 2026-05-01, status: provisional, commits dede72f4 / 0f29cf87).
Duplicate IDs in active register. Architecture-session author should renumber
their provisional entries before marking applied. Not corrected in this commit
because would override a parallel session's pending work.

**Files modified:**
- designs/audit/2026-04-30-geography-audit/00_audit_report.md (new)
- designs/provincial/valoria_map_v2.svg (deprecation banner)
- canon/patch_register_active.yaml (PP-706)
- canon/editorial_ledger.yaml (ED-779, 780, 781)
- canon/editorial_ledger_summary.yaml (refreshed)
- references/propagation_map.md (this entry)

**Cross-references:** PP-706, ED-779/780/781, ED-055 (naval mechanics),
ED-710 (settlement adjacency graph PP-666), ED-711 (fractional province ownership),
designs/world/geography_v30.md (canonical 2026-04-05), designs/world/adjacency_map.jsx,
designs/territory/settlement_adjacency_v30.md (PROVISIONAL PP-666),
designs/territory/settlement_layer_v30.md §2.1 (36-settlement registry),
params/board_game_misc.md (territory rename history).

## 2026-05-01 — Geography Phase 1.5 prep work (PP-707)

Workplan + schema + sample entries + coordinate transform script committed.
Pre-Phase-2-authoring artifact: locks decisions so the next session is execution,
not relitigation.

**Decisions locked:**
- Canonical coordinate system: 1920×2880 (Godot screen-friendly, peninsula proportions)
- Lake Eidursjø central-south interior; T4 Grauwald NE shore; T12 Sigurdshelm west shore — resolves audit C3
- Terrain taxonomy: 8 types (plains, coast, forest, marsh, highland, fjord, mountain, pass) + annotations (river, bridge, road, forgetting_zone, radiation_band)
- Terrain cost matrix seed values (Phase 4 calibrates)
- Vision-range table seed values (Phase 4 calibrates)
- Schema for valoria_geography_v30.yaml — flat, queryable, no nested deep hierarchy

**Sample populated entries** (proof-of-concept; next session pattern-matches):
S-001 Valorsplatz Palace, S-006 Lowenskyst Fortress, S-015 Gransol Parliament, S-026 Sigurdshelm Keep, S-033 Askeheim Ruins; T1 Valorsplatz province polygon; northern_range + lake_eidursjo terrain polygons; r_valoris river feature.

**Coordinate transform script** (tools/geography/jsx_to_canonical.py):
Mechanical, deterministic. Reads adjacency_map.jsx, emits Phase 2 stub with scaled anchors + per-territory correction notes for hand-authoring. Tested: produces valid YAML, 17 territories + 26 edges extracted.

**Phase 2 task list** (~160k tokens, single fresh session):
1. Read workplan
2. Run transform script
3. Hand-author 17 canonical territory anchors + province polygons
4. Hand-author 36 settlement coordinates
5. Hand-author terrain layer (~30-60 polygons, 8 types)
6. Author features layer (rivers, bridges, roads, forgetting zone, radiation bands)
7. Verify schema validity
8. Commit

**Files:**
- designs/audit/2026-04-30-geography-audit/01_phase2_workplan.md (new)
- tools/geography/jsx_to_canonical.py (new)
- canon/patch_register_active.yaml (PP-707)
- references/propagation_map.md (this entry)

**Cross-references:** PP-706 (audit), PP-707 (this), ED-779 (Phase 2 authority), audit doc 00_audit_report.md.

## 2026-05-01 — Geography Canon Phase 1.5 — Phase 2 prep (PP-708)

Phase 2 prep documents committed to designs/audit/2026-04-30-geography-audit/ to
leverage existing context for next-session execution efficiency. Phase 2 proper
(ED-779: data authoring, ~3 commits) needs ~150-200k working space and was
deferred to a fresh session; this Phase 1.5 commit produces the prep artifacts
that turn execution-session work from "design + author + decide" into
"author + verify + extend."

**Three documents:**

1. **00_phase2_workplan.md** — locks all decisions gating execution. Canonical
   coordinate system 2400×2880 (5:6 aspect, matches jsx peninsula proportions,
   Godot strategic-map sized). Lake Eidursjø repositioned to canonical (1135, 2263)
   center, rx=200, ry=150 — per geography_v30_infill east-west barrier function
   (midpoint between T6 Stillhelm canonical and T13 Oastad canonical). 8-terrain-type
   taxonomy: plains/forest/highland/mountain/mountain_pass/fjord_coast/coast/marsh.
   Province polygons implicit-from-Voronoi (no hand-authoring). Vision-range model:
   multiplicative composition radius × terrain × weather × season. Full schema
   for valoria_geography_v30.yaml. §2.2 validation checklist (16 items) for
   pre-commit verification. 3-commit execution plan.

2. **01_coord_transform.py** — Python projection script. Reads adjacency_map.jsx
   (700×600 abstract canvas), applies linear scale to canonical (2400×2880),
   validates settlements inside canvas + outside Lake Eidursjø, outputs
   territory_anchors_canonical.json. Tested: all 17 territories project cleanly;
   no settlement inside lake. Mechanical/deterministic — execution session runs
   it once and feeds output directly into territories: section.

3. **02_sample_data.yaml** — proof-of-concept for valoria_geography_v30.yaml schema.
   Demonstrates: T1 Valorsplatz with 3 settlements (S-001 Palace, S-002 Riverside,
   S-003 Cathedral) at offset coordinates around territory anchor; 4 terrain
   polygons (mountain spine, two mountain passes, eastern lowlands plains);
   river-valoris polyline with crossings; one road polyline; lake-eidursjo
   ellipse; all top-level keys present; TBD values use YAML null (not literal
   strings) so queries fail-fast on unauthored values. YAML validates.

**Resolves audit findings:** C1 (coordinate-system disconnect — canonical
system locked) and C3 (Lake Eidursjø geometry conflict — T4 canonical (789, 1512)
is 28× squared-normalized-distance away from lake center).

**Files committed:**
- designs/audit/2026-04-30-geography-audit/00_phase2_workplan.md (new, 21678 chars)
- designs/audit/2026-04-30-geography-audit/01_coord_transform.py (new, 5kB)
- designs/audit/2026-04-30-geography-audit/02_sample_data.yaml (new, 8439 chars)
- canon/patch_register_active.yaml (PP-708)
- references/propagation_map.md (this entry)

**Phase 2 execution session opens with:**
1. Bootstrap → read 00_phase2_workplan.md (full)
2. Run `python3 01_coord_transform.py designs/world/adjacency_map.jsx`
3. Begin populating designs/territory/valoria_geography_v30.yaml using
   02_sample_data.yaml as pattern; territories filled from transform script
   output; settlement-level offsets per territory's narrative description in
   settlement_layer §2.1
4. Three-commit Phase 2 structure per workplan §5

**Cross-references:** PP-706 (audit + Phase 1, commit e0d6a07), PP-708 (this prep),
ED-779 (Phase 2 standing), ED-780 (Phase 3 standing, blocked on ED-779),
ED-781 (Phase 4 stress tests).

## 2026-05-01 — Phase 2 workplan reconciliation (PP-709 / ED-779 progressed)

Two parallel sessions independently authored Phase 2 workplans within 13 minutes of each other on 2026-05-01:

- **PP-707** (commit `0e75ccd0`, file `01_phase2_workplan.md`)
- **PP-708** (commit `70c77288`, file `00_phase2_workplan.md`)

Both claim AUTHORITY: PP-707 internally. Reconciliation memo committed at `designs/audit/2026-04-30-geography-audit/04_workplan_reconciliation.md` resolves the duplication.

**Three substantive disagreements identified and resolved:**
1. **Canvas dimensions** (1920×2880 vs 2400×2880) → CANONICAL: 1920×2880 (PP-707). Rationale: hex-grid alignment with UI v4 §7.4 tactical hex (32px cells, 60×90 hexes at full canvas) is mechanically load-bearing for Godot impl.
2. **Terrain taxonomy** (annotations-vs-type split vs flat type list) → CANONICAL: 8 terrain types + 5 annotations (PP-707 architecture + PP-708 `fjord_coast` naming adopted). Rivers/roads/bridges/forgetting_zone/radiation_band are annotations, not terrain types — resolves polygon-overlap ambiguity.
3. **Lake Eidursjø geometry** (concrete coords vs deferred) → CANONICAL: PP-707's concrete starting values (lake center 960, 1700; T4 Grauwald NE shore 1090, 1430). Execution session can adjust if Voronoi gives wrong boundaries; starting from concrete values is faster than starting from prose.

**Six decisions absent from both committed workplans, added by reconciliation memo:**
- §2.1 Settlement-coordinate placement rule (per-settlement nudge from territory anchor by type-bias: Ports toward coast, Mines toward mountain, Cathedrals interior, etc.)
- §2.2 Forgetting zone as overlay-not-terrain (canon-preservation: making Forgetting a terrain type would imply faction-property exemptions are mechanically possible, contradicting PP-703 universality)
- §2.3 March-budget formula (Military × 100 px baseline; cavalry 1.5×; skirmish 1.3×)
- §2.4 Roads as A*-cached, not authored (eliminates duplicate authoring; the terrain layer IS the road network)
- §2.5 Naval mechanics scope (explicit Phase 3 deferral; Phase 2 authors data layer that *can support* naval but does NOT spec fleets/ports/sea zones/naval combat)
- §2.6 Vision multiplicative factor structure with concrete starting values (base 240 px × terrain × weather × season; weather: clear 1.0, fog 0.4, storm 0.3, blizzard 0.2; season: spring 1.0, summer 1.05, autumn 0.9, winter 0.6)

**Workplan-of-record designation:**
- `01_phase2_workplan.md` (PP-707) → CANONICAL
- `00_phase2_workplan.md` (PP-708) → SUPERSEDED with banner pointing to canonical and to reconciliation memo

**Phase 2 execution canonical decision set:** PP-707's workplan + reconciliation memo. Execution session uses both as authoritative decision basis. PP-708 retained as historical reference.

**Parallel-session collision pattern flagged.** This is the third register-collision incident in 36 hours:
1. PP-684..688 (mass-battle MB batch vs architecture-session work — applied vs provisional)
2. PP-705/ED-778 (geography audit vs ecosystem-cleanup workplan)
3. PP-707/PP-708 (Phase 2 workplan duplicates)

The valoria-orchestrator hooks catch content-level collisions but don't prevent scope-level duplication. Suggested follow-up at orchestrator-skill maintenance level: `pending_workstream.yaml` check at task_gate, or session-scope-reservation protocol. Out-of-scope for this memo.

**Files modified:**
- designs/audit/2026-04-30-geography-audit/04_workplan_reconciliation.md (new, ~16k chars)
- designs/audit/2026-04-30-geography-audit/00_phase2_workplan.md (banner added)
- canon/patch_register_active.yaml (PP-709)
- canon/editorial_ledger_summary.yaml (refreshed; ED-779 reflects reconciliation)
- references/propagation_map.md (this entry)

**Cross-references:** PP-706 (Phase 1 audit), PP-707 (workplan A), PP-708 (workplan B), PP-709 (reconciliation), ED-779 (Phase 2 standing), PP-703 (Forgetting universality — load-bearing for §2.2), PP-666 (settlement adjacency v1, becomes superseded by Phase 3), ED-055 (naval mechanics — Phase 3 standing).

## 2026-05-01 — Phase 2 geography canon executed (PP-710 / ED-779 closed)

ED-779 Phase 2 data-authoring executed per PP-707 canonical workplan and PP-709 locked decisions. Single atomic commit produces the geography data canon at canonical 1920×2880 and skeletons the Phase 3 successor.

**Authored (new):**
- `designs/territory/valoria_geography_v30.yaml` — data canon: 17 territory anchors (jsx-derived via 01_coord_transform pattern + per-territory geographic correction), 17 hand-authored Voronoi-style province polygons (settlement-containment validated), 36 settlement coordinates with type-bias placement, 26 adjacency edges (incl. T15 gates T6+T13, T1↔T16 coastal, T10↔T11 mountain_pass), 20 terrain polygons covering all 8 canonical types from PP-709 §2.1, Lake Eidursjø ellipse, river Valoris polyline + 2 bridges, forgetting_zone overlay polygon, 6 calamity radiation bands, march_budget formula, vision_range table.
- `designs/territory/valoria_map_v30.svg` — replacement map: terrain colorization, faction-tinted province outlines, settlement glyphs by type, edge classification.
- `designs/territory/march_layer_v30.md` — SKELETON for Phase 3 ED-780 successor (full body deferred to ED-780). Locks march budget formula and pathfinding contract; defers calibration, naval, weather × season tables.

**Banners added:**
- `designs/territory/settlement_adjacency_v30.md` — SUPERSESSION-PENDING marker pointing to march_layer_v30.md (PP-666 mechanical body operative until march_layer is CANONICAL).
- `designs/audit/2026-04-30-geography-audit/00_phase2_workplan.md` — SUPERSEDED per PP-709 §3 (canonical = 01_phase2_workplan.md / PP-707).

**Deleted:**
- `designs/provincial/valoria_map_v2.svg` — deprecated map at non-canonical dimensions, replaced by valoria_map_v30.svg in territory/.

**Register updates:**
- `canon/patch_register_active.yaml` — PP-710 entry (Class A vetting; all M-ratings ○).
- `canon/editorial_ledger.yaml` — ED-779 transitioned `open` → `closed`; description updated to EXECUTED.
- `canon/editorial_ledger_summary.yaml` — open_count 9 → 8; ED-779 removed from p2_open; recent-activity comment updated.
- `references/canonical_sources.yaml` — territories block extended with `geographic_data`, `geographic_map`, `march_layer_skeleton` sub-keys (SHAs PENDING_PP_710).
- `references/file_index_summary.md` — total 697 → 699; territory/ 2 → 5; provincial/ 31 → 30; designs/ 189 → 191.
- `session_log_current.md` — last_stage updated.

**Decisions executed:** all PP-707 + PP-709 §2 locked decisions (canvas 1920×2880, 8-terrain taxonomy with `fjord_coast` adopted, Lake Eidursjø central-south, T4 Grauwald NE shore, type-bias settlement placement, forgetting-zone-as-overlay per PP-703 universality, march-budget Military×100px, roads-as-A*-cached, naval deferred to Phase 3, vision multiplicative with concrete starting values). See PP-710 patch_register description for full enumeration.

**PROVISIONAL flags retained:**
- terrain_cost_matrix off-road multipliers, vision per-terrain coefficients, weather/season multipliers — calibration TBD via Phase 4 stress tests (ED-781).
- march_layer_v30.md is SKELETON only; full mechanical body authored under ED-780.

**Successor handoff (ED-780, Phase 3):** settlement_adjacency_v30.md mechanical body migrates to march_layer_v30.md; mass_battle_v30 §A.4–A.11 terrain-derivation refactor uses geographic_data terrain layer; naval mechanics first authoring (resolves long-standing ED-055).

**Cross-references:** PP-666 (settlement adjacency v1, supersession-pending), PP-703 (Forgetting universality, load-bearing for forgetting-zone-as-overlay), PP-706 (Phase 1 audit), PP-707 (canonical workplan), PP-708 (superseded workplan), PP-709 (reconciliation memo), ED-779 (Phase 2, CLOSED), ED-780 (Phase 3 spec rewrite, depends-on), ED-781 (Phase 4 stress tests, depends-on), ED-055 (naval mechanics, deferred).


## 2026-05-01 Stage 10 promotion — PP-684/685/686/687/688

PROVISIONAL → canonical promotion of architecture-session entries after Stage 10 sims PASS (12/14 battery).

**Source:** designs/audit/2026-05-01-stage-10-validation/01_lateral_evaluation.md (9/9 PASS) + 02_articulation_evaluation.md (6/6 PASS).
**Promoted:** PP-684 (Conviction taxonomy + axis matrix), PP-685 (migration roster), PP-686 v2 (faction behavior), PP-687 (Key substrate + type registry), PP-688 (articulation layer).
**Files updated:** 7 design docs (PROVISIONAL → CANONICAL marker); patch_register_active.yaml (5 entries provisional → applied); canonical_sources.yaml (7 entries provisional → canonical).
**P2 carry-forward (non-blocking):** (a) PP-687 substrate dispatch by type only, not visibility-aware (lateral sim §4.1); (b) PP-688 state.belief_revised omitted from 8-trigger ruleset (articulation sim §4.1).
**Decision-supported:** A6 cross-faction clustering correlation +0.937 in 30-season fixture supports ADD as 9th trigger with corr ≥0.40 threshold (Phase B).
**Deferred to Phase 5a:** PP-687 §9 V7/V8 (memory query + walk perf) require production engine measurement.
**Cross-references:** session 2026-04-30-architecture-session (origin); session 2026-05-01-stage-10-validation (validation + promotion); ED-755 unblocked.


## 2026-05-01 Phase 5a session 1 — KeyStore substrate landed (valoria-game)

PP-687 §8.8 Godot binding implemented in `jordanelias/valoria-game` (commit 737106a).

**Files added:**
- `autoload/KeyStore.gd` — emit/dispatch/store/walks/log_hash autoload
- `systems/keys/Key.gd` — Key Resource with content-hashed id
- `systems/keys/KeyValidator.gd` — §2.3 invariants + §4.6 cycle detection
- `systems/keys/KeyTypeRegistry.gd` — 30-type registry per `key_type_registry_v30.md`
- `tests/test_keystore.gd` — GdUnit suite (14 tests)
- `docs/key_substrate.md` — implementation doc cross-referencing canonical spec
- `project.godot` — KeyStore registered as autoload (load order: Meta → EventBus → KeyStore → GameStateMachine → GameDirector)

**Invariants verified at engine layer:**
- V1 cycle-freeness (test_emit_blocks_cycle)
- V3 visibility correctness (auto-augmentation)
- V4 replay determinism (log_hash matches across runs; differs with payload)
- V5 exact-once dispatch (3 tests: exact pattern, wildcard family, exact+wildcard+universal interleaved)
- 4-hop diagonal walk back+forward
- Type registry: 30 types verified, family extraction, wildcard matching

**Deferred to later Phase 5a sessions:**
- V2 salience monotonicity, V7 memory query perf, V8 walk perf at 10 hops
- Memory Query API (§4.4), save format Resource serialization (§6)
- Bridge with EventBus legacy signals; integration with Meta.gd (session 2)

**Phase 5a roadmap:** 1 ✓ | 2 faction L+PS state | 3 cut scene | 4 walk diagnostic UI | 5 chronicle paragraph

**Cross-references:** PP-687 (canonical 2026-05-01); session 2026-05-01-stage-10-validation; jordanelias/valoria-game commit 737106a.


## 2026-05-01 Phase 5a session 2 — FactionStateV30 with PP-686 v2 §3.4/§3.5 (valoria-game)

PP-686 v2 §3.4/§3.5/§3.6 + PP-684 13-Conviction axis matrix Godot binding implemented in `jordanelias/valoria-game` (commit 36514e8).

**Files added (parallel namespace `systems/faction_v30/`):**
- `systems/faction_v30/ConvictionAxisMatrixV30.gd` — canonical 13×4 matrix verbatim from `conviction_axis_matrix_v30.md` §2; project + cosine + rescaled-cosine
- `systems/faction_v30/NPCStateV30.gd` — minimal NPC state (Convictions Dictionary, standing, Self-Other, supervisor, scars)
- `systems/faction_v30/CascadeFidelityV30.gd` — β-fidelity (mean rescaled cosine) + standing-weighted aggregate (C9)
- `systems/faction_v30/FactionStateV30.gd` — L+PS state, mission alignment (-1/0/+1), ΔPS/ΔL formulae, strictness, 5-temperament weights, Self-Other modulation, β-fidelity gating, single-Key dampening (0.25)
- `systems/faction_v30/FactionLayerV30.gd` — coordinator subscribing to KeyStore for `da.*` + `state.scar_acquired`
- `tests/test_faction_v30.gd` — 21 GdUnit tests
- `docs/faction_v30.md` — implementation doc

**Invariants verified at engine layer:**
- V6 §3.4/§3.5 formula match within 1e-3 (aligned + neutral + contradicted alignments)
- C5 β-fidelity gating (negative attributed → gate halves contribution)
- C7 Self-Other modulation (positive reduces; zero/negative no effect)
- C9 standing-weighted aggregate (Authority 0.875, Liberty 0.125 in 7+1 cascade)
- §3.4.1 5-temperament weights produce distinct ΔPS (0.76 / 0.84 / 0.68 / 0.80 / 0.72)
- §3.6 strictness corners (L=4 PS=4 → 0.514; L=7 PS=0 → 0.9; L=0 PS=7 → 0.1; L=7 PS=7 → 0.6)
- 13-Conviction axis matrix size + projection correctness
- Mission alignment routing (3 cases)
- L+PS clamp at [0, 7] boundaries
- KeyStore subscription integration (da.* and state.scar_acquired both route correctly)

**Coexistence with legacy FactionData:** the `systems/faction_v30/` namespace is the canonical-spec impl. The pre-Mandate-migration `FactionData` in `systems/registries/FactionRegistry.gd` is unchanged; bridge between namespaces deferred until Jordan answers Mandate-audit 5 OQs and per-faction Mandate → L+PS classifications are ratified.

**Calibration items flagged:**
- `FactionLayerV30.SINGLE_KEY_DAMPENING = 0.25` — calibration-eligible at Phase B per `sim_verification_ledger.json`
- 5th axis allowance — Class B, conditional on Stage 10 calibration finding Community/Identity collapse load-bearing (not yet observed)

**Phase 5a roadmap:** 1 ✓ KeyStore | 2 ✓ FactionStateV30 | 3 cut scene | 4 walk diagnostic UI | 5 chronicle paragraph

**Cross-references:** PP-686 v2 (canonical 2026-05-01); session 2026-05-01-stage-10-validation; jordanelias/valoria-game commit 36514e8.

---

## 2026-05-02 — PP register collision resolution (ED-782)

**Trigger:** Pre-flight integrity audit before Stage 10 promotion sign-off discovered duplicate PP IDs in `canon/patch_register_active.yaml` (PP-684..688 each had two entries: 2026-04-30 mass-battle batch + 2026-05-01 architecture-session backfill).

**Resolution:** Mass-battle set renumbered PP-684..688 → PP-711..715. Architecture set retains PP-684..688 (primary semantic owner: 50+ downstream files in audits/sims/designs).

**Renumber map:**
- PP-684 (MB-03 morale reset) → PP-711
- PP-685 (MB-04 discipline persists) → PP-712
- PP-686 (MB-06 shadow intel peek) → PP-713
- PP-687 (MB-02 unit type TARGET relabel) → PP-714
- PP-688 (MB-07 siege pool fix) → PP-715

**Files updated this commit:**
- canon/patch_register_active.yaml (5 id renumbers + header note)
- designs/provincial/mass_battle_v30.md (3 inline citations)
- designs/provincial/military_layer_v30.md (3 inline citations)
- references/canonical_sources.yaml (2 PENDING_PP_705 comments)

**Out of scope:** archives/patches/patch_register_archive_stage4_promotions_2026_04_25.yaml carries a third PP-684 entry (Disposition ceiling = Bonds) in an auto-extracted PROVISIONAL archive. Referenced once in propagation_log.md. Pending Jordan review; not modified here.

**Pattern flagged:** Third register-collision incident in 36 hours. The earlier PP-684..688 collision was already noted in this propagation_map under "Pre-existing PP-684..688 collision" — that note can now be considered resolved.

---

## 2026-05-02 — Register archival sweep (ED-783)

**Trigger:** Three register files at >97% of size cap after ED-782 collision-repair commit. Continuing further work would have started bouncing on `pre_commit_gate` size limits.

**Action — patch_register_active.yaml:** 17 applied PPs (date ≤ 2026-04-30) moved to `archives/patches/patch_register_archive_2026_05_02_a.yaml`.
- PP-681, PP-682 (mass-battle architecture)
- PP-683, PP-690, PP-691 (mass-battle, stratagem, march layer)
- PP-698..704 (geography canon work, settlement adjacency, etc.)
- PP-711..715 (mass-battle ratification set, renumbered from PP-684..688 per ED-782 — archived in same batch as their original-number siblings)

Active register reduced 14,947 → ~8,500 tokens (cap 15,000). Retained: 3 provisional (PP-652, PP-675, PP-676) + 11 applied 2026-05-01 entries (architecture set PP-684..688 + workplan v3 series PP-705..710).

**Action — editorial_ledger.yaml:** 3 closed entries (ED-775, ED-778, ED-779) moved to `archives/editorial/editorial_ledger_archive_2026_05_02_a.yaml`. Active reduced 1,959 → ~1,300 tokens (cap 2,000). Retained: 7 open + ED-782 (most recent closure).

**Action — canonical_sources.yaml:** 35 stale `# Last touched: 2026-04-25 ...` breadcrumb comments stripped. Pruned 4,988 → ~4,300 tokens (cap 5,000). PENDING_PP_705 SHA-follow-up status entries preserved (mass-battle SHA references already updated post-ED-782 renumber).

**Cross-references:** ED-782 (collision repair, immediate predecessor), ED-770 (PENDING_PP_705 SHA follow-up), session log 2026-05-01..02.

**Pattern note:** ED-782 + ED-783 combined are downstream consequences of insufficient pre-emptive archival discipline. Archival should precede cap pressure, not respond to it. Future workplan should include a recurring archival cadence (e.g., when any register passes 80% of cap).

---

## 2026-05-02 — Mandate audit resolution + Phase B trigger ruleset finalized (ED-784, ED-785)

**ED-784 (P1, closed) — Mandate audit Q1-Q5 resolved.** Jordan signoff 2026-05-02.

| Q | Resolution |
|---|---|
| Q1 Submission threshold | PS = 0 |
| Q2 PP-189 Institutional Mandate | L only |
| Q3 Failure-clause Church gain | L only |
| Q4 personal_mandate_view | `round((L+PS)/2)` (already in factions_personal.md per PP-686 v2) |
| Q5 Mandate≥4 gates | per-mechanic (Crown Policy L≥4, populist DAs PS≥4, deviation-cost gates strictness) |

Resolution log: `designs/audit/2026-05-01-stage-10-validation/03_mandate_consumer_audit.md` §5b.

**Phase 2 mechanical sweep queued (separate commit):** 9 consumer files + 8 reference files. Includes Ethical Framework Modifiers strike in `params/factions/stats_1_7_scale.md` (bg/core.md strike already applied).

**ED-785 (P2, closed) — Phase B trigger ruleset finalized.**

- Trigger #9 (cross-faction clustering): threshold |sim| > 0.7 → > 0.40 per Stage 10 §3.6 / A6 evidence.
- Trigger #10 (state.belief_revised) ADDED: tracked NPC fires Tier 2 cut scene directly. Closes Stage 10 §4.1 finding.

Total triggers in articulation §3.1: 10. Stage 8c calibration sweep (Phase 5a) refines further.

**Files touched this commit:**
- `designs/audit/2026-05-01-stage-10-validation/03_mandate_consumer_audit.md` (§5b RESOLVED, §6/§7 updated)
- `designs/articulation/articulation_layer_v30.md` (§3.1 — header, table, threshold, trigger 10 spec)
- `canon/editorial_ledger.yaml` (ED-784, ED-785 added; next_id 784 → 786)
- `references/propagation_map.md` (this section)

**Cross-references:** PP-688 (articulation layer canonical), Stage 10 articulation sim, Stage 8b/c sims, Mandate-consumer audit 2026-05-01.

---

## 2026-05-02 — Register cap revision + chunking sweep (ED-786)

**Trigger:** Three register files at >97% of cap during 2026-05-02 session forced ED-783 emergency archival mid-work. Caps were under-budgeted relative to actual work pace (2-3 commits/session, 800-1200 char ED entries, linear growth in canonical_sources with each new design doc).

**Cap raises** (`skills/valoria-orchestrator/scripts/github_ops.py` `TOKEN_THRESHOLDS`):

| File | Old | New | % raise |
|---|---:|---:|---:|
| `canon/editorial_ledger.yaml` | 2,000 | 4,000 | +100% |
| `canon/editorial_ledger_summary.yaml` | 1,000 | 2,000 | +100% |
| `references/file_index_summary.md` | 1,000 | 2,000 | +100% |
| `references/canonical_sources.yaml` | 5,000 | 8,000 | +60% |
| `tests/coverage_matrix.md` | 5,000 | 8,000 | +60% |
| `canon/patch_register_active.yaml` | 15,000 | 18,000 | +20% |

Unchanged: `session_log_current.md` (2k — session-bounded, rotates), `propagation_map.md` (15k — fine), `arc_register.md` (20k — huge headroom), `design_registry.yaml` (8k — 41% used), `valoria-orchestrator/SKILL.md` (8k).

**Chunking actions** (this commit):

- `canon/editorial_ledger.yaml`: 4 closed entries (ED-782, ED-783, ED-784, ED-785) → `archives/editorial/editorial_ledger_archive_2026_05_02_b.yaml`. Active 1,968 → 1,107 tokens (now 28% of new 4k cap).
- `tests/coverage_matrix.md`: All historical sim batches 2026-04-17 to 2026-04-19 → `tests/coverage_matrix_archive_2026_04_19.md`. Open Findings table pruned to unresolved-only (resolved rows still traceable via ED refs in archive). Active 4,983 → 358 tokens (now 4% of new 8k cap).
- `references/canonical_sources.yaml`: All 7 remaining `# Last touched: ...` breadcrumb comments stripped (continuing 2026-05-02-a sweep). Editorial history now exclusively traced via ED entries + propagation_log. Active 4,333 → 4,130 tokens (now 52% of new 8k cap).

**Not chunked** (deliberate):

- `canonical_sources.yaml`: structural split by domain (personal/provincial/meta) considered but rejected — every consumer (sim_gate, audit hooks) reads this file; refactor blast radius too large for marginal benefit once cap raised to 8k. Revisit if growth trajectory pushes back into >80% in <8 weeks.
- `patch_register_active.yaml`: already chunked aggressively in ED-783 (now 8,533/18,000 = 47% of new cap). No further action.

**Discipline note** (going forward): When any register passes 80% of cap, archive proactively in the same commit as the next routine work. Treat 80% as the operational ceiling, not 100%.

**Cross-references:** ED-782 (collision repair), ED-783 (initial archival sweep), ED-786 (this entry).

**Files in this commit:**
- `skills/valoria-orchestrator/scripts/github_ops.py` (TOKEN_THRESHOLDS revised + comment block)
- `canon/editorial_ledger.yaml` (ED-786 added; ED-782/783/784/785 archived)
- `archives/editorial/editorial_ledger_archive_2026_05_02_b.yaml` (NEW)
- `tests/coverage_matrix.md` (historical sections moved to archive; Open Findings pruned)
- `tests/coverage_matrix_archive_2026_04_19.md` (NEW)
- `references/canonical_sources.yaml` (Last-touched breadcrumbs stripped)
- `references/propagation_map.md` (this section)

---

## 2026-05-02 — ED-784 Phase 2 sweep: stats_1_7_scale.md (commit A)

First commit of the L+PS mechanical migration sweep mandated by ED-784. `params/factions/stats_1_7_scale.md` is the canonical 1-7 stat block file — most foundational of the 9 consumer files.

**Header migration:** Stat block header `Mandate / Influence / Wealth / Military / Intel / Stability` → `Legitimacy / Popular_Support / Influence / Wealth / Military / Intel / Stability`. Starting Stats table header columns expanded `M (TTRPG) | M (BG)` → `L (TTRPG) | PS (TTRPG) | L (BG) | PS (BG)`. All faction rows seeded with equal L=PS values per PP-686 v2 §3.4-3.5 (Crown 5/5/5/5, Church 5/5/5/5, Hafenmark 4/4/4/4, Varfell 4/4/4/4, Guilds 3/3/3/3, Löwenritter —/—/3/3).

**Mechanic migrations (per audit §2.1 classifications):**

| Mechanic | Roll/Effect | Classification |
|---|---|---|
| Crown Royal Decree | Mandate vs Ob 2 | **L** (procedural) |
| Church Excommunication | Mandate vs target Mandate | **L** vs target **L** (procedural authority both sides) |
| Excommunication outcome | target Mandate −1 | target **L** −1 (institutional) |
| CI 60 Territorial Seizure | Mandate vs floor(owner's Mandate / 2) + 1 | **L** vs floor(owner's **L** / 2) + 1 |
| CI Seizure failure | Mandate −1 | Church **L** −1 |
| RM Community Weaving | Mending Mandate prerequisite ≥ 1 | Mending **PS** ≥ 1 (populist) |
| Baralta Suppression | Church Mandate −1/season while Mandate ≥ 4 | Church **L** −1/season while Baralta **L** ≥ 4 |
| Baralta Heresy outcomes | Church Mandate −1, Baralta's Mandate −1 | Church **L** −1, Baralta's **L** −1 |
| Baralta CI Suppression gate | while Baralta Mandate ≥ 4 | while Baralta **L** ≥ 4 |
| RM Mending prerequisite | Mandate ≥ 1 | **PS** ≥ 1 |
| Mandate Recovery (ED-066b) | factions with Mandate < starting recover +1 | **L** AND **PS** independently (cap at each starting value) |
| Institutional Mandate Trigger (ED-003) | Faction Mandate ≥ 4 | Faction **L** ≥ 4 (per audit Q2 — institutional) |
| Institutional Mandate Uphold/Appease (PP-189) | Mandate ≥ 4, Mandate −1 | **L** ≥ 4, **L** −1 (per audit Q2) |
| RM Revolution DA pool | Mandate (as dice) + History | **PS** (as dice) + History (populist) |
| RM Revolution outcome | Mandate −1 on failure | **PS** −1 on failure |
| PI track accrual | any faction Mandate < 3 at accounting | any faction **PS** < 3 (populace dissatisfaction trigger) |
| PI revolt check failure | Mandate −1 | **PS** −1 (outcome-driven populist loss) |

**Ethical Framework Modifiers strikes (PP-686 v2 / SUPERSESSION-PP686-002 + 003):**
- §General "Ethical Framework Ob Modifiers" table: SUPERSEDED, struck through, replaced by triadic decomposition in `faction_behavior_v30.md §3.7` (mission_alignment_modifier + cascade_alignment_modifier + expectation_alignment_modifier, ±2 cap).
- §Löwenritter "Ethical Framework Modifiers (PP-246)" table: SUPERSEDED, struck through. Löwenritter's Mission/cascade/expectation tags now authored in faction state per `faction_behavior_v30 §3.7`.

**Open item flagged:** Pre-existing inconsistency between Starting Stats table (Varfell BG Mandate 4) and L18 footnote (Varfell BG Mandate 3). Footnote updated to match table; flagged for Jordan confirmation as part of ED-784 Phase 2 (not blocking).

**Files in this commit:**
- `params/factions/stats_1_7_scale.md` (38 Mandate refs migrated; 2 Ethical Framework sections struck; Starting Stats table header + 6 rows updated; L18 footnote inconsistency flagged)
- `references/canonical_sources.yaml` (canonical_sha bumped)
- `references/propagation_map.md` (this section)

**Cross-references:** ED-784 (umbrella), PP-686 v2 (faction behavior v2), audit §2.1 (per-site classifications), `params/factions_personal.md` (L+PS canonical authority for seed-equal rule), `params/bg/core.md` (Ethical Framework strike applied 2026-05-01 SUPERSESSION-PP686-001).

**Remaining Phase 2 work:** 8 consumer files (faction_actions, factions_personal additional refs, ministry, institutions, parliament, ci_seizure, tracks, stress_patches, phases) + 8 reference files. Subsequent commits B, C, D.

---

## 2026-05-02 — ED-784 Phase 2 sweep: Commit B (faction_actions + ministry + factions_personal)

Second commit of the L+PS migration sweep. Three consumer files migrated.

**`params/bg/faction_actions.md` (38 refs):** All Mandate references in territory/parliamentary/charter/conquest mechanics → L (procedural authority across the board). Bulk patterns:

- `Roll: Mandate vs Ob ...` → `Roll: L vs Ob ...` (Assert, Charter, Influence, Tribune Investigate, Conquest)
- `controlling faction Mandate`, `controlling faction global Mandate`, `target Mandate`, `target controller Mandate` → L equivalents (institutional/procedural opposition)
- `Baralta's Mandate ≥ 4` (PP-431-COR CI suppression) → `Baralta's L ≥ 4`
- `Church Mandate +1` (failure-clause gain per audit Q3) → `Church L +1`
- `Hafenmark Mandate +1` (Manoeuvre/Conquest gain) → `Hafenmark L +1`
- `Hafenmark Mandate ≥ 4` (Conquest prerequisite) → `Hafenmark L ≥ 4`
- `Hafenmark Mandate >` (Manoeuvre gate) → `Hafenmark L >`
- `Church global Mandate >` (Church-prominent gate) → `Church global L >`
- `floor(Mandate / 2) + 1` (Charter limit, Assert/Seize Ob) → `floor(L / 2) + 1`
- `Mandate 0 from submission` (Diplomatic Token suspension) → `PS 0 from submission` (per audit Q1)
- Defensive Institutional Mandate (PP-189) gate `Mandate ≥ 4` → `L ≥ 4` (per audit Q2)
- Legacy mechanic name "Institutional Mandate" preserved in textual reference (Q2).

**`params/bg/ministry.md` (32 refs):** Ministry is a structurally institutional (administrative apparatus) entity. Per audit Q2, Ministry's "Mandate" → Ministry **L** only. Bulk: `Ministry Mandate` → `Ministry L`; `Crown Mandate ≥ 4` (Crown decree-support gate) → `Crown L ≥ 4`; bare `Mandate 3D vs Ob 1` (Ministry rolls) → `L 3D vs Ob 1`; `Ministry Collapse (Mandate 0)` → `Ministry Collapse (L 0)`; `AP-token in T13, Mandate ≥ 2` → `... Ministry L ≥ 2`. Stat-block row updated to indicate `PS not tracked for Ministry — administrative apparatus has no separate populist axis`.

**`params/factions_personal.md` (18 refs):** Mostly canonical-authoring file (PP-686 v2 source); bulk of "Mandate" mentions are intentional historical/derived references. Migrations applied:

- Starting Values table header expanded: `Mandate | Influence | ...` → `Legitimacy | Popular_Support | Influence | ...`
- All 7 faction rows seeded with equal L=PS values per PP-686 v2 (Crown 5/5, Church 5/5, Hafenmark 4/4, Varfell 4/4, Guilds 3/3, Revolution —/—, Löwenritter —/—)
- L36 "Löwenritter (no Mandate, no Wealth)" → "no L, no PS, no Wealth"
- Crown Royal Decree pool, Church Excommunication pool/gate, Hafenmark Sovereign Authority Doctrine pool → L (procedural authority)
- "Active attack on Mandate/Wealth" Stability check → "Active attack on L, PS, or Wealth"
- "Pool: relevant faction stat (typically Mandate or Influence)" → "(typically L, PS, or Influence depending on action's procedural-vs-populist nature)"
- Church Mandate ≥ 5 / Piety DA pool → Church L ≥ 5 / L pool (institutional)
- L38 init note phrasing updated to remove the now-stale "Mandate value above" reference (table no longer has a Mandate column); replaced with the canonical seed-equal rule with explicit per-faction values.

**Preserved intentionally** (L, PS, derived Mandate retained for backward compat):
- L8 PP-686 v2 NOTE comment block
- L14 derived Mandate row (`~~Mandate~~ (derived) | Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support)`)
- L38 init note (now updated phrasing, but keeps "Mandate" only in narrative explanation)

**Cumulative ED-784 Phase 2 progress:**

| File | Mandate refs | Status |
|---|---:|---|
| stats_1_7_scale.md | 38 | ✓ Commit A (f8ac629) |
| factions_personal.md | 18 | ✓ Commit B |
| faction_actions.md | 38 | ✓ Commit B |
| ministry.md | 32 | ✓ Commit B |
| institutions.md | ~21 | pending |
| parliament.md | ~16 | pending |
| ci_seizure.md | ~12 | pending |
| tracks.md | ~11 | pending |
| stress_patches.md | ~9 | pending |
| phases.md | ~2 | pending |
| 8 reference files | ~56 | pending |

**Files in Commit B:**
- `params/bg/faction_actions.md`
- `params/bg/ministry.md`
- `params/factions_personal.md`
- `references/canonical_sources.yaml` (3 SHAs bumped)
- `references/propagation_map.md` (this section)

---

## 2026-05-02 — ED-784 Phase 2 sweep: Commit C (institutions + parliament + ci_seizure + tracks + stress_patches + phases)

Third commit of the L+PS migration sweep. Six consumer files migrated, ~99 Mandate refs total.

**`params/bg/institutions.md` (27 refs):** Bulk migration — Ministry Mandate / Crown Mandate / Church Mandate / Crown's Mandate → L equivalents. Specific edits: Cardinal of Temperance Altonian diplomacy advancement roll (Mandate vs Ob = floor(Altonian diplomacy/2)+1) → L; bare Crown confirmation roll (Mandate vs Ob 2) → L; Ministry stat-row narrative ("Its Mandate (3) represents institutional legitimacy") → L (3) with audit Q2 footnote. All institutional throughout — Ministry is administrative apparatus per audit Q2 (no separate populist axis).

**`params/bg/parliament.md` (19 refs):** All procedural-authority parliamentary mechanics. Notable migrations:
- Crown Policy gates (`Mandate ≥ 4`) → `L ≥ 4` per audit Q5 procedural-authority interpretation
- §Mandate Recovery (PP-174): renamed to track L+PS independently, like ED-066b in stats_1_7_scale
- §Mandate Suppression (PP-296): renamed §L Suppression. Coalition cap targets institutional L stat (procedural-authority suppression). PS-targeting suppression (e.g., populist undermining via Information ops) noted as not bound by this cap.
- Institutional Mandate Uphold/Appease (PP-189): legacy name preserved, mechanic operates on L per audit Q2 (header + body footnoted)
- Trigger scope: Domain Action targeting "Mandate stat" → "L stat" (institutional context)
- Crown end-of-Phase-4 Mandate −1 → L −1

**`params/bg/ci_seizure.md` (20 refs):** Pure procedural Church religious-authority mechanics. All Mandate refs → L: Conditional Passive prominence gate, Suppress §3.7 opponent action, Hafenmark Structural Suppression (PP-431-COR Baralta L ≥ 4), Church/non-Church Political pool formulas (Mandate ± floor(CI/N)), seizure prerequisites (Church L ≥ 4, Prominence Church L > controlling faction L).

**`params/bg/tracks.md` (16 refs):** Mostly Peninsular Strain track + Hafenmark Awareness track effects. PP-686 v2 NOTE comment block (L1) preserved as historical record. Migrations:
- Cardinal Altonian diplomacy advancement roll → L (matches institutions.md)
- Strain "Mandate check" at Tension/Crisis/Collapse states → "L check" (institutional pressure on faction procedural authority)
- Hafenmark Awareness 3+ effects: Church Mandate −1 → Church L −1 (institutional strain); Hafenmark Mandate ≥ 3 → Hafenmark L ≥ 3 (CI suppression ratchet)
- Excommunication "+2 Mandate" cost annotation → "+2 L" (Church loses procedural authority equivalent to Hafenmark's PE-driven institutional resilience)

**`params/bg/stress_patches.md` (14 refs):** Mostly Restoration Movement Founding outcomes + PP-475 Submission ruling + Church Prominence formula. Migrations:
- Church Prominence formula → Church L > controlling faction L
- Baralta Mandate ≥ 4 (CI suppression context) → Baralta L ≥ 4
- §Submission + Mandate 0 Ruling (PP-475) → §Submission + PS 0 Ruling per audit Q1 explicitly (header + body)
- "halved Mandate = 0" → "halved PS = 0" (audit Q1 ratification)
- "Mandate 0" / "Mandate-0 effects" → "PS 0" / "PS-0 effects"
- RM Founding outcome stats: Mandate 2/Mandate 1 → L 2 + PS 2 / L 1 + PS 1 (seed equal per PP-686 v2). Inline TODO flagged: PP-460 says RM is statless; may be obsolete content — flagged for Jordan review.

**`params/bg/phases.md` (3 refs):** Brief migrations:
- Church Prominence update (ED-326): "Church global Mandate exceeds territory's controlling faction's global Mandate" → "Church global L exceeds ... controlling faction's global L"
- Torben Loyalty modifier "Crown upheld Mandate 2+ consecutive seasons" → "Crown upheld L 2+ consecutive seasons" (procedural Crown discipline reward)

**Cumulative ED-784 Phase 2 progress:**

| File | Mandate refs | Status |
|---|---:|---|
| stats_1_7_scale.md | 38 | ✓ Commit A (f8ac629) |
| factions_personal.md | 18 | ✓ Commit B (0a32a29) |
| faction_actions.md | 38 | ✓ Commit B (0a32a29) |
| ministry.md | 32 | ✓ Commit B (0a32a29) |
| institutions.md | 27 | ✓ Commit C |
| parliament.md | 19 | ✓ Commit C |
| ci_seizure.md | 20 | ✓ Commit C |
| tracks.md | 16 | ✓ Commit C |
| stress_patches.md | 14 | ✓ Commit C |
| phases.md | 3 | ✓ Commit C |
| 8 reference files | ~56 | pending Commit D |

**Subtotal so far:** 225 Mandate refs migrated across 10 consumer files. ED-784 Phase 2 (consumer-file sweep) complete pending Commit D (reference files).

**Note on canonical_sources.yaml:** The 6 files in this commit (`params/bg/{institutions,parliament,ci_seizure,tracks,stress_patches,phases}.md`) are not SHA-tracked in `references/canonical_sources.yaml`. Only some `params/bg/*.md` files have SHA records (core, clocks, victory, royal_assassination, tensions_deck, faction_actions, ministry); the rest are downstream reference files without independent canonical authority. No canonical_sources update is required for this commit.

**Files in Commit C:**
- `params/bg/institutions.md`
- `params/bg/parliament.md`
- `params/bg/ci_seizure.md`
- `params/bg/tracks.md`
- `params/bg/stress_patches.md`
- `params/bg/phases.md`
- `references/propagation_map.md` (this section)

---

## 2026-05-02 — ED-784 Phase 2 sweep: Commit D — closure

Final commit. ED-784 Phase 2 work complete.

**7 reference files migrated** (74 refs total): `params/factions/riskbreakers_identity.md` (17), `params/bg/ed_resolutions.md` (9), `params/bg/victory.md` (12), `params/bg/core.md` (17), `params/bg/npc_priority_trees.md` (9), `params/bg/npcs_special.md` (5), `params/scale_transitions.md` (5). Migration patterns followed audit §2/§3 classifications + commits A/B/C established conventions: procedural rolls → L; populist outcomes (morale, defection, talent drain) → PS; institutional gates → L; Crown Policy/Hafenmark Sovereignty/Crown Treaty/Senator Outward → L; named victory conditions (Ecclesiastical Mandate) preserved as proper nouns with L footnote; Mandate-order resolution (PP-112) → derived-Mandate = round((L+PS)/2) per audit Q4.

**Notable:** core.md Starting Stats table split (Mandate column → Legitimacy + Popular_Support; all 7 faction rows seeded equal); core.md PP-686 v2 init block phrasing updated; victory.md Hafenmark Parliamentary Sovereignty Mandate≥4 → L≥4; Peninsular Partition "Both Mandate ≥ 3" → "Both L ≥ 3 AND PS ≥ 3" (institutional + populist viability per audit Q5 strict reading); npcs_special.md general capture/execution PS−1/−2 (morale-blow populist component); scale_transitions.md debate-outcome Domain Echo expanded to contested-axis (L procedural / PS populist).

**ED-784 Phase 2 — COMPLETE.** 17 files, **299 Mandate refs** migrated.

| Commit | SHA | Files | Refs |
|---|---|---:|---:|
| A | f8ac629 | stats_1_7_scale.md | 38 |
| B | 0a32a29 | factions_personal + faction_actions + ministry | 88 |
| C | 9a07316 | institutions + parliament + ci_seizure + tracks + stress_patches + phases | 99 |
| D | (this) | riskbreakers_identity + ed_resolutions + victory + core + npc_priority_trees + npcs_special + scale_transitions | 74 |

**Files in Commit D:** the 7 above + `references/canonical_sources.yaml` (3 SHAs bumped: victory, core, scale_transitions; other 4 not tracked) + `references/propagation_map.md` (this section).

**Watch-out:** propagation_map now ~99% of cap. Next session priority: archive ED-782..786 + Phase 2 commit-A/B/C/D sections from propagation_map (same chunking discipline as ED-786 editorial_ledger archival).
