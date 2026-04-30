---
session_id: 2026-04-29-conviction-track-promotion
session_close: 2026-04-29
phase: "Conviction Track promotion to first-class doc"
status: complete
last_stage: >
  PP-681 / ED-768 — Conviction Track promoted to first-class doc.
  designs/personal/conviction_track_v1.md created (4,834 chars consolidating
  §1.2 + §3.3 + §3.4 from npc_behavior_v30). Original sections replaced with
  redirect stubs. scale_transitions L219 cross-ref updated. canonical_sources
  repointed (SHA placeholder PENDING_FIRST_COMMIT). Bonus: 3 bare 'GM' refs
  in §3.3 table cells fixed (missed by PP-678).
next_action:
  skill: editorial
  description: >
    Immediate next: SHA follow-up commit for designs/personal/conviction_track_v1.md.
    Procedure: fetch new file's blob SHA after current commit lands, update
    canonical_sources.yaml canonical_sha__designs__personal__conviction_track_v1_md
    from "PENDING_FIRST_COMMIT" to actual SHA, ship as small editorial PP.
    Remaining v3 §V3-10 priority items:
    1. NPC Behavior audit pass — corpus integration spine (cite-deg 56);
       needs dedicated session at full focus, NOT same-session continuation
    2. Other isolate promotions (Convictions Taxonomy already done as part
       of Conviction Track; Pressure Points Taxonomy, Wager, Thread Revelation
       remain — each requires similar scope decision + SHA follow-up workflow)
    3. Peninsular Strain + IP change-control review (highest propagation
       risk per multi-graph hubs ≥3/4)
    4. Wager system clarity audit (sparse footprint canonical)
    5. Bare 'GM' sweep (PP-678 used 'Game Master' full phrase; bare 'GM'
       in table cells like §3.3 needs separate pass; 3 fixed in this PP,
       full corpus sweep TBD)
    PRIOR ITEMS still pending Jordan decision:
    - Review of accumulated PPs: 676 (v3 audit), 677 (throughlines col),
      678 (GM+CR), 679 (vector-audit skill), 680 (CC sweep), 681 (Conviction
      Track promotion)
    - CI-01 Church Prominent definition (HIGH-PRIORITY)
    - PT-01, ACCT-01, mass battle MB-01..08, INTER batches
    - Intelligence stat, LICENSE/GOV-08, §1.1 Knot Formation, §1.2 Accord Propagation
blockers:
  - "Canonical SHA follow-up for conviction_track_v1.md (next commit)"
  - "NPC Behavior audit needs dedicated session"
  - "Other isolate promotions (Pressure Points, Wager, Thread Revelation)"
  - "Bare 'GM' corpus sweep (separate from 'Game Master' phrase sweep)"
  - "Jordan review of accumulated PPs (676, 677, 678, 679, 680, 681)"
  - "Prior session blockers"
notes:
  - "Same-session continuation per Jordan directive 'perform all'"
  - "Stub-redirect strategy preserves existing file-level citations"
  - "Only 1 explicit cross-section reference found and updated (scale_transitions §3.4)"
  - "Conviction Track was multi-graph isolate per v3 §V3-5 despite canonical centrality; isolate status now resolved"
  - "Convictions Taxonomy is part of Conviction Track doc (no separate file); Pressure Points Taxonomy still pending separate PP"
  - "NPC Behavior audit declined for this turn — too large for same-session continuation; honest deferral per task_pressure quality > completion"
