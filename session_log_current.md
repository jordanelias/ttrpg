session_id: 2026-03-27T15
phase: Thread Operations Redesign — Simulation
status: v2.5 simulation complete. 4 P1 findings, 5 P2, 6 P3. Mechanic-audit patches needed.

completed_this_session:
  - Full Sonnet-tier stress test of threadweaving v2.5
  - Simulation 1: Coherence degradation curves (3 archetypes — all hit crisis by late campaign, confirmed by design)
  - Simulation 2: FR Lock chronic RS drift — 3 unremoved Locks fatal within 7-8 seasons (P1)
  - Simulation 3: Mending pool probability curves — Standard Gap needs 14D+; Catastrophic Gap borderline impossible
  - Simulation 4: Over-actualisation impact — Brittleness (P-18) can make Weaving produce worse outcome than not Weaving
  - Simulation 5: Diagnosis-Leap combat timing — 5 edge cases found including priority ambiguity (P1)
  - Simulation 6: Threadcut De-actualisation — TS 100 beings immune to Dissolution/Pulling via §9.7 formula (P1)
  - Simulation 7: Involuntary Leap edge cases — 2 P3 findings
  - Gap register updated: 149 → 164 items (+15 sim findings)
  - Output file: tests/sim_threadweaving_v25.md

findings_summary:
  P1: [SIM-F-01 (Coherence cliff), SIM-F-02 (Lock RS drift), SIM-F-03 (Catastrophic Gap documented), SIM-F-04 (threadcut immunity cap), SIM-F-05 (priority convention)]
  P2: [SIM-F-06 (Brittleness sidebar), SIM-F-07 (Wound+Leap timing), SIM-F-08 (mid-sequence config change), SIM-F-09 (P-19 integration check), SIM-F-10 (Mending pool guidance)]
  P3: [SIM-F-11, SIM-F-12, SIM-F-13, SIM-F-14, SIM-F-15]

editorial_needed:
  - §9.7 interference cap proposal (cap at +3): requires user confirmation before patching
  - Catastrophic Gap design intent (near-impossible floor): confirm or lower Ob

deferred_tasks:
  - Mechanic-audit: specify patches for SIM-F-01 through SIM-F-08 (P1+P2 findings)
  - Haiku batch: Solmund rename, AG→AS calendar, Church rename
  - Confirm P-19 integration into §2.4 main text
  - Compilation: Stage 3 Thread Operations chapter (pending patch completion)
  - Board game RS track integration
  - Hybrid mode branching catalogue update

blockers: []

next_action:
  task: Mechanic-audit for patch specification on SIM-F-01 through SIM-F-08
  model: Sonnet
  input: tests/sim_threadweaving_v25.md + designs/threadweaving_redesign_v25.md
