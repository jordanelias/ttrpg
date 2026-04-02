# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_DEBATE_STRESS_TEST
phase: Phase 9 — Debate stress test (SIM-DEBT-01)
status: IN PROGRESS

completed:
  - SIM-D-01: Debate stress test Modes A+D+J+L. Calibration baselines recalibrated.
  - PP-097 PROVISIONAL: DIVERGE+TIE → Tie rule fires (any interaction type). Applied in-place to debate_system_redesign_v1.md §6.4 DIVERGE block.
  - PP-098 PROVISIONAL: Regroup at Concentration=0 → consumes Spent without penalty. Applied in-place §6.4 Step 5.
  - PP-099 PROVISIONAL: Obscuring in Divergence → Doubt Marker; orientation_weight=1.0. Applied in-place §6.4 DIVERGE block.
  - debate_system_redesign_v1.md bumped to v1.1.
  - propagation_map.md updated with DEBATE section.
  - SIM-DEBT-01 PARTIALLY RESOLVED: Mode C scenario run still needed.

key_findings:
  - P(Overwhelming) doubled: ~25% old → ~60% new (symmetric 8D pools)
  - Exchanges to Rattled halved: 7-9 old → 3-5 new (Composure 9)
  - Track movement now consistent 1 step/exchange vs 0 often under old pool
  - F-D-01 P1 (PP-097): DIVERGE+TIE ambiguity — Tie rule takes priority
  - F-D-06 P2: Grand Debate + Corroboration ~90 resolution steps, no GM reference card

next_action:
  task: "Mode C debate scenario — Baralta vs Himlensendt, 3-exchange Formal Debate. Completes SIM-DEBT-01."
  note: "Read stage13_npcs.md for Baralta and Himlensendt stats before running. New pool: (Presence×2)+History."

commits_this_session:
  - 22a1f24: SIM-D-01 test file + patch_register PP-097/098/099 + params_debate recalibration + coverage_matrix
  - [this commit]: debate_system_redesign_v1.md v1.1 in-place patches + propagation_map + session_log
```
