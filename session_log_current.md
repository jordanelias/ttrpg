---
session_id: 2026-04-29-vocab-sweep
session_close: 2026-04-29
phase: "vocabulary debt sweep — Game Master + active Cultural Reformation"
status: complete
last_stage: >
  PP-678 / ED-765 — 17 Game Master references replaced with 'engine'
  equivalents in threadwork_v30, npc_behavior_v30, mass_battle_v30. 2 active
  Cultural Reformation references in complete_systems_reference cleaned with
  STRUCK editorial markers. 14 CR STRUCK markers retained as historical record.
  Coup Counter sweep DEFERRED — substitution to Graduated Autonomy needs design
  judgment, not mechanical replacement. Bonus: ED-762 collision resolved
  (renumbered doc 12 v1.2 entry to ED-763) + 4 ledger entries compressed.
next_action:
  skill: editorial
  description: >
    Coup Counter sweep is the next vocabulary debt item. 10 active references
    across 7 files require Coup Counter (binary 0-4 counter) → Graduated Autonomy
    (4-state track: Loyal/Restless/Autonomous/Split per ED-781) substitution.
    NOT 1:1 — Coup Counter ≥ 3 was the trigger threshold; Graduated Autonomy uses
    state transitions instead. Each site needs review of what mechanical role
    Coup Counter played there and which Graduated Autonomy state(s) map.
    Active sites needing replacement:
      - npc_behavior_v30 L601 ("Coup Counter advances from Crown instability triggers...")
      - complete_systems_reference L46 ("Coup ≤ 1", "Coup Counter ≥ 3, exile")
      - victory_v30 L464 ("premature Coup Counter cascade")
      - victory_v30 L494 ("When Coup Counter reaches 4 and Löwenritter activates")
      - victory_v30 L501 ("Coup Counter resets to 0")
      - conflict_architecture_proposal L157 ("integrates with the existing Coup Counter")
    Sites describing the strike (LEAVE):
      - canon/03_canonical_timeline L92 (worldbuilding context — historical)
      - campaign_architecture_v30 L179 ("replacing the binary Coup Counter")
      - conflict_architecture_proposal L37, L78 (argument FOR Graduated Autonomy)
    PRIOR ITEMS still pending Jordan decision:
    - PP-676 v3 weakness register §V3-10 priority items (NPC Behavior audit pass,
      isolate promotion to first-class docs, Peninsular Strain + IP change-control)
    - PP-677 throughline→system mappings (43 throughlines, 27/32 systems mapped)
    - PP-678 vocabulary cleanup (this commit)
    - CI-01 Church Prominent definition (HIGH-PRIORITY)
    - PT-01, ACCT-01, mass battle MB-01..08, INTER batches
    - Intelligence stat, LICENSE/GOV-08, §1.1 Knot Formation, §1.2 Accord Propagation
blockers:
  - "Coup Counter sweep — design judgment per site for Graduated Autonomy substitution"
  - "Jordan review of PP-678 (vocabulary cleanup)"
  - "Jordan review of PP-677 (throughline mappings)"
  - "Jordan review of PP-676 v3 weakness register findings"
  - "Prior session blockers"
notes:
  - "Same-session continuation per Jordan directive 'commit continue all best'"
  - "All 17 GM replacements unique-match verified before apply"
  - "2 active CR cleanups in csr; 14 CR STRUCK markers retained as audit trail"
  - "Coup Counter deferred because Graduated Autonomy substitution is not 1:1"
  - "ED-762 collision (flagged in PP-677/ED-764) resolved by renumbering doc 12 v1.2 entry to ED-763"
  - "4 ledger entries compressed (ED-751/752/755/762) for size compliance — content references retained"
  - "canonical_sources.yaml included with no changes per co-file rule for design doc edits"
