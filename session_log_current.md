session_id: 2026-04-19-batch4-arc-test
session_close: 2026-04-19
phase: 0
status: complete
last_stage: arc test batch 4 — PI/RDT/TD/Accord/Coup — committed d195dbc
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0. Workplan at tests/sim_framework/workplan_rebuild_2026-04-19.md.
    Phase 0 canon audit, produce tests/sim_framework/canon_audit.md.
    Batch 4 added 6 new gap flags. Notable: T9 PT=5 at game start changes B3-1
    findings (CI hits cap from S1). Coup triggers PI collapse to 0 permanently.
  blockers:
    - T9 PT=5 at game start (canonical) — B3-1 seizure timing results need revision
    - Coup Counter advancement sources not in any read doc
commits:
  - d195dbc: arc test batch 4 — PI track, RDT/TD, Accord revolt, Löwenritter Coup
session_highlights:
  - B4-1 (PP-431-COR fix): Corrected model produces S12-S18 variance vs S12-S14 structural-only.
    Challenge is a situational tool (play near CI thresholds), not a blanket every-season strategy.
    T9 PT=5 at game start discovered — B3-1 used wrong PT values; Piety Yield hits cap from S1.
  - B4-2 (PI track): PI is structurally net-positive under Hafenmark pressure. PI never reaches
    NonFunctional (≤2) without the Coup. PI drifts to 15+ over 30 seasons. Upper-band effects
    (Crown Policy M≥4) trivially met by Crown M=5. PI track needs either higher-frequency loss
    sources or more meaningful ceiling effects.
  - B4-3 (RDT/TD): CI60 fires at S8 in every seed (T9 PT=5 canonical). TD4 (Ob+2 at HF territories)
    not reached until S20 — after first Seizure attempt. TD5 (T8 permanently unseizable) fires S24.
    RDT/TD is a viable long-game defensive path for Hafenmark, but the first 12 seasons are exposed.
    Seizure Failure consequences (Stab-1 + Casus Belli) not tracked — gap for engine_v4.
  - B4-4 (Accord revolt): Strain hits Collapse (10) by S4-5 under 2 battles/season. Cascade driven
    by garrison coverage, not battle intensity. Recovery path absent under sustained conflict.
    Treaty mechanic (-1 Strain from diplomatic resolution) not modeled — key missing piece.
  - B4-5 (Löwenritter Coup): PI collapses to 0 immediately post-coup and stays there permanently.
    PI=0 gives Church CI+2/season but this is largely redundant past CI80. Real consequence is
    permanent loss of Parliament as Hafenmark tool. Paradox: Coup accelerates Church victory —
    Crown must prevent the Coup to avoid enabling Church. Post-coup board (Löwenritter at T14 Fort3
    Mil6, PI=0, CI accelerating) is the richest player decision space in the design.
    Coup Counter advancement sources and Coup effect on Crown Mandate are unspecified gaps.
open_items:
  - B3-1 results need revision — T9 PT=5 canonical, not PT=1 as assumed; CI hits cap S1
  - ED-706, ED-707 (P2 rewrites)
  - PP-666 spec fixes (3 from Batch 2)
  - B3-5 suppression race already rerun as B4-1 (PP-431-COR corrected)
  - GAP: T9 PT=5 at start — Piety Yield hits cap from S1; Assert irrelevant immediately
  - GAP: Coup Counter advancement sources not in read docs
  - GAP: Coup effect on Crown Mandate not canonical
  - GAP: Seizure Failure consequences (Stab-1 + Casus Belli) not modeled in any sim
  - GAP: Treaty mechanic interaction with Strain not modeled
  - GAP: PI track upper-bound effects need design review
  - All prior open items carried forward
