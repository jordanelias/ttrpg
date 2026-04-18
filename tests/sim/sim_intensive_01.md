# SIM Intensive Batch 01 — 6 Suites
## Date: 2026-04-04 | Suites: Rescue in Play, Feint Chains, BG Mandate, Social Contest, PI Cascade, Dissonant Thread
## 7-Dimension Tag:
## Mechanics: Rescue, Feint, BG Mandate suppression, Social Contest, PI, Dissonant Thread
## Mode: TTRPG/BG/Hybrid | Temporal: PRES
## Tracks: Health, Wounds, Momentum, Fibonacci, Mandate, TC, Composure, PI, RS
## Factions: Crown, Church, Hafenmark, Varfell, Restoration Movement
## NPCs: Aldric, Maret, Scholar/Diplomat/Demagogue (generic)
## Archetypes: MARTYR, SURVIVAL-FLOOR, GREEDY, RISK-AVERSE, FACTION-LOYAL, RITUAL, FACTION-OPPORTUNIST

---
## SUITE 1 — Rescue in Play (3v2 Full Scenario)

Setup: Aldric 14D vs Z (9D TN6). Maret 11D vs X (8D TN5) + Y (10D TN7, Fibonacci +1D). Aldric [MARTYR].

Round 1: Aldric targets X (TN5). Commits N=8, keeps 6D vs Z.
Contest: E[Aldric 8D TN7]=2.4 vs E[X 8D TN5]=4.4. P(intercept)≈18%. Expected: FAIL.
Z vs Aldric (6D Def): P(hit)≈72%. Expected: Aldric 1 Wound.
X vs Maret (7D Def): P(hit)≈76%. Expected: Maret 1 Wound.
Y vs Maret (11D+Fib, 7D Def): P(hit)≈80%. Expected: Maret 2nd Wound.

Round 2: Aldric retargets Y (TN7). N=7, keeps 7D vs Z.
Contest: E[Aldric 7D]=2.1 vs E[Y 10D TN7]=3.0. P(intercept)≈34%. Expected: FAIL.
Z hits Aldric (P≈62%). Maret: SURVIVAL-FLOOR, 0O/9D. X hits Maret P≈68%. Y hits P≈53%.
End R2: Aldric 2 Wounds, Maret 3-4 Wounds (incapacitation imminent).

F01 [P2]: TN5 attackers structurally near-uninterceptable. No viable N gives P≥50% and meaningful own Defence simultaneously.
F02 [P2]: MARTYR no fallback after 2 failed Rescues. Protocol refinement: add "Rescue failed N times" pivot.
F03 [OK]: Fibonacci correctly stays active on failed intercept.
F04 [P2→ED-292]: MARTYR accumulates wounds, gains 0 Momentum from failed intercepts. Consider: wound-from-own-engagement on same round as failed Rescue = 1 Momentum.

---
## SUITE 2 — Feint Chains

A: Feint→Strike: +8% hit probability at median pools. Situationally useful, not dominant. OK.
B: Feint vs Feint: fully resolvable. Both commit to Offence, defend remainder. OK.
C: Minimum N=3: 16% P(success). Non-trivial, not dominant. Threshold correctly set. OK.
D: Feint ceiling with incapacitation: ceiling expires if Feinting actor cannot act. PP-293 applied.
   Stacking: successive Feints do not stack (always pool−2). PP-293 applied.

F01 OK | F02 OK | F03 P1→PP-293 (stacking) | F04 OK | F05 P1→PP-293 (incap expiry)

---
## SUITE 3 — BG Mandate Ceiling

P(suppression success) by pool vs Ob:
3D: M3=16%, M4=5%, M5=1%, M6<1%
5D: M3=34%, M4=16%, M5=6%, M6=2%
7D: M3=50%, M4=30%, M5=14%, M6=6%

F01 [P1]: Direct suppression non-viable vs M5-6 at any starting faction pool. ED-173→ED-293 (4 options).
F02 [P1]: 2-faction coalition (7D) vs M6: 6%. 3-faction (11D): 25%. Coalition barely viable.
F03 [P1→ED-293]: Unchecked Church reaches M7 in 2-3 seasons. At M7: near-impossible for any coalition.
F04 [P1]: M7+TC≥50 simultaneous = win-lock condition. No current BG rule prevents.

ED-293 options: A=cap Ob4, B=coalition +2D, C=Stability path, D=Mandate decay above M5.

---
## SUITE 4 — Social Contest Baselines (SIM-DEBT-03/04)

New attribute mapping: Cognition×2+History=Argue pool. Attunement=initiative. Charisma+6=Composure.
Scholar 13D Composure 9. Diplomat 10D Composure 11. Demagogue 6D Composure 12.

Scholar vs Diplomat CLASH: P(Scholar wins)≈62%. Strategic texture correct.
F01 OK: Pool-driven advantage. Composure asymmetry creates Diplomat attrition strategy.
F02 P2: Contest too long at median — Conviction Track length not defined. GAP SC-DEBT-02.
F03 P1: Demagogue non-viable in CLASH vs Scholar (P≈12%). AMPLIFY path not yet tested. GAP SC-DEBT-03.

SIM-DEBT-03/04 PARTIAL — baselines established for CLASH. AMPLIFY and multi-genre not yet re-run.

---
## SUITE 5 — PI Revolt Cascade
BLOCKED: PI threshold values not in params_factions. SIM-DEBT-08 opened.
GAP PI-CASCADE-01: escalation trigger values missing.
GAP PI-CASCADE-02: PI revolt threshold missing.

---
## SUITE 6 — Dissonant Thread Effects (War-Scale)
BLOCKED: War-scale Dissonant rates not in params_threadwork. SIM-DEBT-06 carried.
GAP DISSONANT-01: war-scale Dissonant effect rates and RS impact per operation not parameterised.

---
## SIM-DEBT Register Updates
SIM-DEBT-08 OPENED: PI cascade — threshold values needed before simulation.
SIM-DEBT-06 CARRIED: Dissonant war-scale — params needed.
SIM-DEBT-03/04 PARTIAL: CLASH baselines established. AMPLIFY, multi-genre, multi-party pending.
