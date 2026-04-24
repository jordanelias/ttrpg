session_id: 2026-04-24-consolidation-followups
session_close: 2026-04-24
phase: infrastructure
status: complete
last_stage: >
  Continued follow-ups from 2026-04-23 consolidation-system close.
  Five commits:
    2071752 — alias_registry v2 (Certainty added, unresolved gaps closed via deprecated section),
              + references/numeric_bounds_report.yaml (targeted scan of 207 files for ceiling/cap/
              floor/threshold/max/min; 254 hits, 97 stats, 14 flagged as potentially drifted).
    02ba388 — bulk-fix applied: 104 substitutions across 22 files
              (Rendering Stability→Mending Stability: 74, Cohesion→Discipline: 29, Combat Power→Power: 1).
              User-authority paths skipped (designs/world, designs/npcs, designs/arcs, designs/territory).
              Historical/deprecated/superseded files skipped. Lines with rename-context markers skipped.
    08e0cf1 — tools/valoria_bulk_fix.py + glossary additions (Arc, Zoom In, Zoom Out, Cardinal).
    Glossary last_updated advanced to 2026-04-24.
  Collator re-run post-fix: 9101→8969 findings (−132). LEGACY_TERM_USED 903→799 (−104 matches substitutions).
  COLLISION_USED_ALONE 1092 unchanged — TC/TD/CP require per-context judgment, not auto-fixable.
next_action:
  skill: editorial
  description: >
    Only manual-judgment items remain from the consolidation system:
    (1) TC disambiguation sweep — 943 occurrences across design docs. Each TC instance must be
        manually classified as Theocracy Counter (faction clock) or Conviction Track (debate
        system). Top files: designs/audit/npc_faction_arc_interdependency_2026-04-18.md (61×),
        designs/arcs/narrative_scenario_chains.md (57×), designs/scene/conviction_track_v30.md (52×),
        designs/arcs/gm_ref/arcs_46_55_resolved.md (50×), designs/provincial/faction_politics_v30.md (48×).
    (2) CP and TD disambiguation — smaller footprint (~149 combined) but also per-context.
    (3) User-authority-path RS/Rendering Stability residuals — bulk-fix skipped designs/world,
        designs/npcs, designs/arcs, designs/territory. These need editorial-flagged commits if swept.
    (4) Numeric bounds report review — 14 stats flagged for potential drift; most are likely
        legitimate (multiple thresholds per stat) but a handful may be stale references.
    (5) Maret disambiguation pass — flagged since round-1 proper noun triage (Uln vs Vossen).
    (6) Five carried-over items from 2026-04-22: D-4, D-5, ED-735 (RWCE/Miracle/SA-gating),
        PROVISIONAL marker audit, doc_index_gen.py regen.
  priority: "TC disambiguation is the highest impact on mechanical correctness — ~30 min focused work on top 5 files clears 268 of 943"
blockers: []
notes:
  - "Collator per-instance report (962KB) not committed; regenerate via tools/valoria_collator.py"
  - "Numeric bounds report highlights Mending Stability threshold (20/40/60) inconsistencies in arcs — likely intentional multiple thresholds, not bugs"
  - "Certainty now registered in alias_registry — any remaining 'CERT' usages in active docs are now properly named (not unresolved)"
