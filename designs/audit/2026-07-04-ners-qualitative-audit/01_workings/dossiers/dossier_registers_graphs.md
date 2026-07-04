# Dossier — registers_graphs lane (SHAPE)

## Files read
canon/mechanics_index.yaml (full), canon/supersession_register.yaml (full),
canon/03_canonical_timeline.md (skim), canon/patch_register_active.yaml (skim ~150 lines),
references/canonical_sources.yaml (first 120 lines + mass_battle grep), tools/observability/DECISIONS.md
(head + counts), tests/coverage_matrix.md (full, 2026-06-15 through 2026-07-04), propagation_map.md /
throughline_registry.md (heads), grounding docs 00/02/03.

## Key raw evidence

- mechanics_index.yaml header: `last_authored: "2026-05-17"`, `drift_report.last_generation: "2026-05-17"`,
  `mechanics_total: 70`, `not_implemented: 60` (86%). Generator "v1... auto-population from canon-doc
  scanning deferred to v2" (never built, per file's own note).
- `mass_battle` entry (L468-491): `test_status: not_implemented`, note "v17 M3 has <5% of v22 feature
  surface", 11-item `v22_features_pending` (rally_check_hook, reform_check_hook, threadwork_check_hook,
  multi_unit_orchestrator, etc.) — all dated to the 2026-05-17 Pass 2n authoring.
- tests/coverage_matrix.md (2026-06-15→2026-07-04, ~440 lines) is **entirely mass_battle engine work**:
  Stage 1-2 rearchitecture, gauge_mb.py live port, TOI refactor, Stage D/E role wiring + deploy UI,
  ED-1089/1090/1091 (field-default flip, subunit cap 11, frontal recoil gate), ED-1095 T1-T4 charge-recoil
  ruling, ED-1096 movement/pathing audit steps 1-7 + adversarial review (6 confirmed fixes), ED-MB-0001,
  ED-MB-0002 (Cannae gauge DG-3/DG-4 pool-math + morale-pull rulings, PR #73/#75 merge-ratified). This
  directly falsifies the mechanics_index mass_battle entry — rally/rout/morale-sibling-pull/multi-unit
  orchestrator/envelopment-refused-flank compositions are now built, byte-exact tested, and Jordan-ratified.
  File's own title: "Coverage Matrix — Weapon System v2 (Active)" — no longer describes its content.
- mechanics_index `combat` entry (L205-218) WAS hand-patched post-generation: cites "Repointed 2026-06-23"
  and ED-1041 (bilateral-Ob wounds) — dates after the file's own `last_authored`/`drift_report` timestamps,
  which were never bumped. So the registry mixes at least one live-patched entry with ~59 frozen-at-Pass-2j
  entries and gives no in-file signal which is which.
- `social_contest` entry (L220-231): "v17 missing entirely (degenerate single-roll only)" — contradicts
  charter §Calibration "social-contest rebuild Stages 0-3 done" and interdependency map "(rebuild in
  flight, sim/personal/contest/)".
- canonical_sources.yaml `mass_battle` system entry (L156-161) pins only prose doc SHAs
  (`mass_battle_v30.md`/`_index`/`_infill`, `mass_battle_integration_v30.md`) — no reference to any of the
  ED-1089..1096/ED-MB-0001/0002 sim-level ratifications above.
- supersession_register.yaml: grep for `mass_battle|FIELD_MOVEMENT|PER_CELL|ED-108|ED-109|ED-MB` = **zero
  hits**. The FIELD_MOVEMENT/PER_CELL default-path flips (ED-1089, gate 4) are supersession-shaped events
  (which resolution path is "the" canonical default) and aren't filed here or in canonical_sources.
- tools/observability/DECISIONS.md: 957 open items / 892 files; **507 P1 (53%)**, 311 P2, 139 P3. Top
  category "Naming & collisions" (343). Hotspot files: `references/npc_registry.yaml` (161),
  `references/module_contracts.yaml` (75). Sampled P1 "Naming & collisions" entries are almost all cosmetic
  rename flags (e.g. arc-doc collision tables), not load-bearing mechanical blockers.
- mechanics_index.yaml has no orphan/gap_notes/doc:null-style staleness field at all (unlike sibling
  module_contracts.yaml, which the interdependency map documents as tracking doc:null/[ASSUMPTION]/orphan
  status for 27 modules). The two registries overlap in scope (mechanic ↔ module) but don't cross-reference.

## Trunk vs branch read
Actual engine-verification bandwidth for the last ~3 weeks (per the only executable-test-adjacent log,
coverage_matrix.md) has gone almost 100% into mass_battle. None of the three "shape of record" artifacts
this lane covers (mechanics_index, canonical_sources, supersession_register) reflect that this is where
the corpus's real current center of gravity is — the reverse of the expected staleness direction (usually
a neglected branch goes stale; here the registries are blind to the *most active* branch).

## Findings retained for structured output
See StructuredOutput `findings[]`. All tagged NEW (verified against calibration list — none match the
listed KNOWN items verbatim; closest is the general "module_contracts gaps" calibration item, which is a
different registry than the ones flagged here).
