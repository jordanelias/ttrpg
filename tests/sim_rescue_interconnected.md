# SIM-RES-01/02/03/04 — Rescue Interconnected Test Suite
## Date: 2026-04-04 | Mode: C+D | Focus: Rescue mechanic full stress test
## 7-Dimension Tag:
## Mechanics: Rescue, Fibonacci, Double Exposure, Ob floor | Mode: TTRPG | Temporal: PRES
## Tracks: Health, Wounds, Stamina, Momentum | Factions: None
## NPCs: Generic 3v2 actors | Archetypes: SATISFY, MARTYR, RISK-AVERSE

---
## SIM-RES-01 — Eligibility

F01 [P1→PP-290]: Eligibility timing undefined. Fix: assessed at Phase 1 declaration only.
  - 2v1: eligible. 1v1: ineligible (fails silently). 2v2 where ally falls at P1: ineligible (assessed at declaration).
F02 [P2→PP-290 note]: Fibonacci recalculation after Rescue redirect — locked at declaration. No mid-round recalc.

---
## SIM-RES-02 — Double Exposure

Setup: B rescues A from X (3v2). Z still attacks B from B's original pairing.
B: 11D pool, End 3, Health 9, wound threshold 9, no Defence either engagement.
Z (8D TN7) vs Ob 1 floor: E[net]=2.4, P(≥1)≈97% — Z almost certainly hits B.
X (8D TN5) vs Ob 1 floor: E[net]=4.4, P(≥1)≈99% — X almost certainly hits B.
P(both hit B) ≈ 96%. Expected: B takes 2 Wounds in one round.

F01 [P1→PP-290]: Ob 0 below system minimum. Own-engagement attack resolves at Ob 1 floor (PP-232).
F02 [OK]: 2-wound expected cost is correct risk profile for sacrifice mechanic. Design-valid.
F03 [OK]: Payoff asymmetric correctly — rescuer pays, rescued actor benefits. No change needed.

A's state: Y's attack (only remaining) resolves against A's declared Defence. Fibonacci drops to +0 (1 attacker). A effectively safe this round.

---
## SIM-RES-03 — Payoff Calibration

Rescuer pays ~2 wounds for: 1 Momentum + A's exemptions.
Feint comparator: 1 exposure, 0 Defence, gains: opponent -2D Defence ceiling next round.
Rescue: 2 exposures, 0 Defence, gains: 1 Momentum (rescuer) + full ally protection (rescued).
Conclusion: payoff structure correct. Rescuer Momentum may be undervalued at +1 given double exposure.
→ ED-290 open: consider +2 Momentum.

---
## SIM-RES-04 — Edge Cases

F01 [P1→PP-290]: Rescue chain — B rescues A, C declares Rescue on B. Block: voluntary double exposure ≠ outnumbered. Chain block rule added.
F02 [OK]: Rescuer Out of Breath — no active roll in Rescue. OoB penalty irrelevant. No special case.
F03 [OK]: Feint + Rescue same round — coherent. A's Defence 0 irrelevant (untargetable). No conflict.
F04 [P1→PP-290]: Rescuer incapacitated at P1 before Rescue trigger — Rescue fails, attack reverts. Momentum not reclaimed.

---
## Findings Summary
P1 (→PP-290): F01-RES-01, F01-RES-02, F01-RES-04, F04-RES-04 (4 findings, single patch)
P2 (→ED-290): RES-03 Momentum calibration (open)
Design-valid: RES-02-F02, RES-02-F03, RES-04-F02, RES-04-F03
