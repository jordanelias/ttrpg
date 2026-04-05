# SIM-FM-01/02, SIM-RES-05/06/07 — Feint Partial Commit + Rescue Contested Roll
## Date: 2026-04-04 | Mode: C+D | Focus: Feint and Rescue pool split mechanics
## 7-Dimension Tag:
## Mechanics: Feint, Rescue, pool split, contested roll, Fibonacci | Mode: TTRPG | Temporal: PRES
## Tracks: Health, Wounds, Defence allocation, Momentum | Factions: None
## NPCs: Generic actors | Archetypes: GREEDY, RISK-AVERSE, SATISFY

---
## SIM-FM-01 — Feint Partial Commit

A (12D) vs B (10D). Feint commit N, remainder to Defence. Payoff fixed: opponent -2D ceiling.

P(feint success Ob2) by N: N=2→10%, N=4→25%, N=6→50%, N=8→68%, N=12→88%
F01 [OK]: All-in dominated by partial commit (pays 6 extra dice for +38% success, zero defensive gain). Available but no longer optimal. Design-valid.
F02 [P2→PP-291]: N=1 gives 2% success at near-zero cost — speculative Feint viable without minimum. Minimum commit 3D added.
F03 [OK]: Old "Defence=0" was consequence of all-in, not independent rule. Removed cleanly.

---
## SIM-FM-02 — Feint + Initiative Information

F01 [OK]: Higher initiative sees A's declared commit N — calibrates Offence accordingly. Asymmetry preserved.
F02 [OK]: Partial commit creates genuine information game vs old binary "Defence=0" signal. Design improvement.

---
## SIM-RES-05 — Rescue Contest Probability Landscape

B (11D) commits N vs X (8D TN5). Contest: B N dice TN7 vs X Offence roll.
E[X net TN5] = 4.4 (high). P(B wins) by N: N=4→18%, N=6→30%, N=8→42%, N=11→58%.
F01 [P1→PP-292 note]: TN5 attacker heavily disadvantages intercept at partial commits. Correct texture — light weapons hard to intercept. Stated explicitly in rule.
F02 [OK]: TN7 attacker: N=6→52% intercept. Viable at moderate cost. Design-valid.

---
## SIM-RES-06 — Rescue Double Exposure: Corrected Model

B commits N=6, keeps 5D Defence. B faces: Z (own engagement, 5D Defence applies) + X (redirected, DR only).
F01 [P1→PP-292]: "No Defence" framing wrong. Contest dice expended — redirected attack hits DR only. Own engagement defended by (pool−N). Rule corrected.
F02 [—]: Revised model: N dice contest, pool−N defend own attacker, redirected hits DR only if intercept won.
F03 [OK]: Failed intercept: B wastes N dice, A still hit, B defends own engagement normally. Correct tension — no patch.

---
## SIM-RES-07 — Momentum Calibration

Old rule: Momentum on declaration. Failed intercept → B gains Momentum for helping no one.
F01 [P2→PP-292+ED-291]: Moved to successful intercept only. Failed Rescue = no payoff, no Momentum. Correct.

---
## Findings Summary
PP-291: Feint minimum commit 3D, partial commit model.
PP-292: Rescue contested roll, partial commit, corrected exposure, payoff on successful intercept only.
ED-291 resolved: Momentum on successful intercept.
Design-valid: FM-01-F01, FM-02-F01/F02, RES-05-F02, RES-06-F03.
