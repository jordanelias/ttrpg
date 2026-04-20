session_id: 2026-04-19-sim-all-sessions
session_close: 2026-04-19
phase: 0
status: complete
last_stage: Full campaign simulation harness complete (Sessions 1+2+3); 8-seed deterministic corpus PASS
next_action:
  skill: Tier A conquest loop (mass combat + territory seizure + Peninsular Sovereignty reachable)
  description: >
    The sim runs end-to-end but no faction can conquer another's territory
    yet, so Peninsular Sovereignty is unreachable in simulation. Tier A
    adds mass_battle_v30 resolution, Church CI=60+ TC Seizure DA, Crown
    military occupation, territory control changes with Accord damage.
    After Tier A: factions can win via Peninsular Sovereignty and we can
    measure win-rate distributions across seeds. See
    tests/sim/campaign_simulation_readiness_2026-04-19.md §5 for full
    Tier A/B/C scope.
  blockers: []
blockers: []
commits:
  - 129f2f2b: Sim Session 1 — foundation (core engine, clocks, factions, seasonal loop)
  - 99b469cf: Sim Session 2 — territory model + DA framework + Piety Yield + faction AI
  - 6264e685: Sim Session 3 — victory + Tensions Deck + Royal Assassination + Threadwork + 8-seed corpus
P1-BLOCKER count: 0
design_complete: true
sim_harness_complete: true
