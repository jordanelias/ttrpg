# Session Log — 2026-04-18 (engine v3 iteration 2)
last_stage: Engine v3 AI tuning — throttled military, Crown dominance identified
next_action:
  skill: simulation — AI balance iteration
  description: >
    Engine v3 core mechanics canonical (dice, CI, RS, seizure CI≥75 one-time, victory=peninsula).
    AI balance issues found: Crown Royal Decree overpowered (+1 stat/season free),
    other factions lose territory via Accord decay and don't reclaim.
    Next: constrain Royal Decree to card-slot cost, add Uncontrolled territory
    reclaim logic, balance faction expansion rates for equal win probability.
  blockers: []
commits:
  - 250715f8: "[fix] seizure threshold CI≥75"
  - fcb1ea76: "[simulation] engine v3 initial"
  - pending: "[simulation] engine v3 AI tuning v2"
P1-BLOCKER count: 0
