session_id: f41be7d36c28f087
session_close: 2026-05-12
phase: SIM-MB-06 v8
status: clean — tension F resolved, commit 1daf87b
last_stage: SIM-MB-06 v8 committed — tension F (cell support + puncture) resolved
next_action:
  description: Horseshoe vs Line investigation (29.5% → target 40-60%) + lethality fix (9.5t → target 3-6)
  skill: valoria-simulator
blockers: []

p1_blocker_count: 0

commits_this_session:
  - sha: 1daf87b
    message: "[simulation] SIM-MB-06 v8 — tension F: cell support stack + puncture bonus"

open_tensions:
  - Horseshoe vs Line T3: 29.5% (target 40-60%) — separate investigation needed
  - Lethality: 9.5 turns T3 (target 3-6) — under-damage at scale
  - GappedLine vs Line: 72.7% — possibly over-tuned, not blocking
  - F-iii cascading sub-phases: not needed for T3; available as v9 enhancement

ratification_checklist:
  - Horseshoe vs Line in 40-60% range
  - Lethality in 3-6 turns
  - All matchups in 30-70% range (min)
  - ED-826 written superseding ED-814
