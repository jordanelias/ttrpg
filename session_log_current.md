session_id: 2026-05-15-integration-plan
session_close: 2026-05-15T23:59:00Z
phase: infrastructure
status: complete
last_stage: integration_plan_v3_committed
next_action:
  skill: valoria-simulator
  task: Phase 1a dice calibration — match v15 quasibinomial to v12c VFIVE (p_hit=0.4 phi=2.67)
  files:
    - designs/audit/2026-05-14-balance-audit/sim/mc_v12c.py
    - designs/audit/2026-05-14-balance-audit/sim/mc_v15.py
    - designs/audit/2026-05-14-balance-audit/integration_plan_v3_2026-05-15.md
blockers:
  - Jordan decision: balance target symmetric vs asymmetric (plan §9 Q1)
  - Jordan decision: Workstream C ratification (plan §9 Q2)
  - Jordan decision: PROP-05 treaty expiration (plan §9 Q3)
  - Jordan decision: dice fallback approval (plan §9 Q4)
  - Jordan decision: unit movement model a/b/c (plan §9 Q5)
commits:
  - 08f667c: "[infrastructure] integration plan v3"
