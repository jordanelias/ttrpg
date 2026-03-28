session_id: 2026-03-27T18
phase: Thread Operations Redesign — Simulation Batch 2
status: Batch 2 complete. 3 P1, 6 P2, 2 P3. Editorial decisions needed on F-03 and F-04.

completed_this_session:
  - Stress test batch 2: Collective Operations, Past-Oriented Pulling, Involuntary Leap, Opposing Ops
  - 11 new findings (SIM2-F-01 through SIM2-F-11)
  - Gap register updated: +11 items
  - Output: tests/sim_threadweaving_v25_batch2.md

critical_findings:
  - SIM2-F-03 (P1): Past-Oriented Pulling recency Ob table absent from v2.5 — blocks play
  - SIM2-F-04 (P1): Past-Oriented Pulling pool (Spirit+History only) makes TS irrelevant to execution
  - SIM2-F-09 (P1): Involuntary-to-voluntary-extension bypasses concealment — exploit

editorial_decisions_needed:
  - SIM2-F-04: Add TPS (or TPS/2) to Past-Oriented Pulling pool? Or add rationale note?
  - SIM2-F-03: Reproduce recency Ob table in §2.4 (from prior ruleset — needs source)

deferred_tasks:
  - Resolve editorial decisions on SIM2-F-03 and SIM2-F-04
  - Mechanic-audit patches for SIM2-F-03, F-04, F-09 (P1s)
  - P2 patches: SIM2-F-01, F-02, F-05, F-08, F-10, F-11
  - Haiku batch: Solmund rename, AG→AS, Church rename
  - Stage 3 compilation (pending all patches)

blockers:
  - SIM2-F-03: recency Ob table source unknown — need prior ruleset or user input
  - SIM2-F-04: design decision required before patching

next_action:
  task: Editorial decisions on SIM2-F-03 and SIM2-F-04
  model: Current (user decision)
