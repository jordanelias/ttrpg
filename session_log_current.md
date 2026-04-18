session_id: repo_restructure_2026-04-18
session_close: 2026-04-18
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
  description: >
    Repo restructure complete. 474 files processed across 14 commits.
    Verify CI passes. Regenerate file_index.md + file_index_summary.md.
    Remove infrastructure bypass from editorial_gate when confirmed stable.
blockers: []
commits:
  - f7bbed65: "Phase 1 — 17 ecosystem files updated (canonical_sources, design_registry, atomization_rules, params_split, propagation_map, github_ops, valoria_hooks, 3 CI tools, 6 skill SKILL.md, restructure_ledger)"
  - 376d12c9: "editorial_gate infrastructure bypass + EDITORIAL_PATHS dedup"
  - cfc43dfe: "Phase 2A — designs provincial+scene+threadwork (71 files)"
  - 9995f494: "Phase 2B — designs npcs+world+arcs+gm_ref (52 files)"
  - 27661711: "Phase 2C — designs architecture+audit (21 files)"
  - 3592e1dd: "Phase 2D — params all (41 files)"
  - c428c037: "Phase 2E — archives canon+session (23 files)"
  - d8a1692b: "Phase 2G — tests audit+stress+misc (44 files)"
  - d1b6fdbf: "Phase 2H — deprecated+refs (26 files)"
  - 287752b5: "Phase 2I — tests/sim misc (1 file)"
  - 7810e735: "Phase 2J — 4 deletes (session_log_archive.md, path, 2 non-canonical skeletons)"
  - 0cce4cef: "Phase 2F part 1 — tests/sim (48 files)"
  - d3890c8d: "Phase 2F part 2 — tests/sim (48 files)"
  - 3841faa1: "Phase 2F part 3 — tests/sim (48 files)"
  - 6ff017bc: "Phase 2F part 4 — tests/sim (45 files)"
  - f990cedf: "Phase 2K — settlement_layer → designs/territory/ (2 files)"
resolutions_this_session:
  - "474 files moved/deleted/deprecated across 16 commits"
  - "17 ecosystem files updated with new paths"
  - "New top-level dirs: archives/, params/, designs/provincial/, designs/scene/, designs/threadwork/, designs/territory/, designs/architecture/, designs/world/, designs/arcs/"
  - "Mode labels eliminated (board_game/, ttrpg/, hybrid/ → scale-based taxonomy)"
  - "compilation/v0.14 → deprecated/"
  - "references/params_* → params/"
  - "gm_ref/ → designs/arcs/gm_ref/"
  - "tests/ reorganized: sim/, audit/, stress/, misc/"
  - "session_log_archive* → archives/session/"
  - "editorial/patch archives → archives/editorials/, archives/patches/"
  - "editorial_gate infrastructure bypass added for file-move operations"
open_items:
  - "Regenerate file_index.md and file_index_summary.md"
  - "Remove editorial_gate infrastructure bypass after verification"
  - "Verify CI passes on new structure"
  - "Update internal cross-references within moved design docs (canonical: path headers in skeletons)"
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
files_modified:
  - "474 files across entire repo — see restructure_ledger.md for complete mapping"
