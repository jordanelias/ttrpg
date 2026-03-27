session_close: 2026-03-27
checkpoint: 14-p1-repairs
model: claude-sonnet-4-6
completed_stages:
  - Identified 4 open P1 items from prior sessions via recent-chat audit
  - Fixed stage16_reference.md: Thread pool formulas (Stage17-P3 propagation), CD->ThS label, Past-Oriented Pulling entry added
  - Fixed CP14 §16.2: same Thread pool formula propagation
  - Fixed CP14 §14.1 and §12 GM checklist: attribute pool 18->31 (2 instances)
  - Added §5.6 Past-Oriented Pulling degree table (Overwhelming/Success/Partial/Failure with TT/ThS costs)

commits:
  stage16: 7e476716c28c
  cp14: df195c585530

p1_items_resolved:
  - stage16 §16.2 Thread pool formulas wrong (Cognition+Focus/Memory/Attunement -> Attunement+History+TPS / Spirit+History+TPS)
  - CP14 §16.2 same formula mismatch
  - Attribute pool contradiction (§2.2=31, §14.1/§12=18) — now all say 31
  - §5.6 Past-Oriented Pulling missing degree table — now added

editorial_still_pending:
  - S-08 Einhir site name (deferred)
  - Co-movement d10 table in BG (uses card system; d10 is TTRPG only)
  - E-01 assassination perpetrator (intentionally unresolved)
  - Vaynard Private Collection transfer procedure (design pending)
  - Niflhel Supremacy seasonal resolution full procedure (design pending)
  - Coherence 0 saving attempt procedure (design pending)
  - GAP-UC-03-A: Thread op performed ON a Devout character (ruling pending)
  - F-32 Ehrenwall coup counter: undefined value and decrement triggers
  - F-33 Martial Law procedure: undefined
  - F-34 TC80 territorial seizure procedure: missing

next_action:
  task: Continue Phase 3 simulation — Batch 5 (core combat engine M-01-M-09) + BUG-004 verification on stage13
  skill: valoria-simulator
  note: stage13_npcs.md scanned clean for Heart/Poise — BUG-004 may be complete; verify before batch 5
  also_check: stage16 old CD track label in gap register — may need gap register update
  model: Sonnet 4.6
