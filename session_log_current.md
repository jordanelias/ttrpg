session_id: 2026-04-18-phase1-restructure-plan
session_close: 2026-04-18
phase: infrastructure
status: complete
last_stage: done
next_action:
  skill: repo restructure
  description: >
    Full directory + file rename proposal. Read canonical_sources.yaml to
    resolve duplicates and authority. Drop mode labels (bg, ttrpg, hybrid).
    Taxonomy: provincial/ territory/ scene/ npcs/ world/ architecture/ ui/ audit/.
    Params to params/ with bg/ factions/ history/ subdirs.
    Archives to archives/session/ patches/ editorials/.
    Tests to tests/sim/ audit/ stress/.
    Produce complete old→new mapping for Jordan review before executing.
    Must atomically update: canonical_sources.yaml, design_registry.yaml,
    atomization_rules.yaml, split map, TOKEN_THRESHOLDS, file_index,
    propagation_map, skeleton routing, CI checks, co-file rules,
    and all internal cross-references.
blockers: []
resolutions_this_session:
  - "Phase 0 built and committed (11 build units)"
  - "Phase 1 executed: 103 violations → 0 errors"
  - "  53 skeletons generated"
  - "  params_board_game atomized (16 domains)"
  - "  params_factions, params_threadwork, arc_register, propagation_map atomized"
  - "  91 consumed patches archived from active register"
  - "  3 monolithic archives chunked (patch 9, editorial 6, session 7)"
  - "  Fix: warn-severity violations non-blocking"
  - "  patch_register_active threshold raised to 15k"
  - "Repo structure audit completed"
  - "  Identified: root clutter, references/ junk drawer, mode-based design dirs"
  - "  Proposed taxonomy: provincial/territory/scene + npcs/world/architecture"
  - "  File rename needed: drop mode labels, resolve duplicates, clean slugs"
  - "  Next session executes full restructure with Jordan review"
files_modified:
  - "(see prior session log for Phase 0/1 file list)"
open_items:
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
  - "Repo restructure: full directory + rename migration (next session)"
