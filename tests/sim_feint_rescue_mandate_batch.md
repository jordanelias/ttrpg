# SIM Batch 02 — Feint Versus Roll, Rescue Momentum, BG Mandate
## Date: 2026-04-04 | Suites: SIM-FM-03, SIM-RES-08, SIM-BG-02
## 7-Dimension Tag:
## Mechanics: Feint (versus roll), Rescue (Momentum wound trigger), BG Mandate suppression
## Mode: TTRPG/BG | Temporal: PRES
## Tracks: Health, Wounds, Momentum, Defence pool, Mandate
## Factions: Crown, Church, Hafenmark, Varfell | NPCs: Aldric, Maret
## Archetypes: GREEDY, RISK-AVERSE, MARTYR, FACTION-LOYAL, FACTION-OPPORTUNIST, RITUAL

---
## SIM-FM-03 — Feint Versus Roll

A (12D, lower init) commits N=6 vs B (10D, higher init). B allocates D_B to Defence.
B neutralises expected Feint value at D_B≥6 (E[B 6D]=1.8 ≥ E[A 6D]=1.8).
Cost to B: 4D remaining Offence, Strike P(hit)≈38% only.

F01 OK: Initiative premium real but costly — correct design.
F02 OK: Information game improved over old binary "Defence=0" signal.
F03 P1→PP-294: Pool reduction needs floor (min 1D). Without floor, extreme margin could zero-out opponent.
F04 OK: All-in (N=12) now viable as high-risk choice — imposes large pool reduction; A takes max exposure. Coherent.

Pool reduction expected values:
N=6 vs D_B=4: E[margin]=1.8−1.2=0.6. Expected B loses 1D next round.
N=12 vs D_B=2: E[margin]=3.6−0.6=3.0. Expected B loses 3D next round.

---
## SIM-RES-08 — Rescue Momentum Wound Trigger

Scenarios tested:
A: Intercept success + own-engagement wound → 1 Momentum. ✓
B: Intercept failure + own-engagement wound → 1 Momentum (wound fires regardless). ✓
C: Intercept success + redirect wound → 1 Momentum. ✓
D: Intercept success + both wounds same round → 1 Momentum (capped, not 2). PP-295 cap required.

F01 P1→PP-295: Without cap, double-exposure farms 2 Momentum/round. Cap at 1/round applied.
F02 OK: No wound = no Momentum. Correct.
F03 OK: MARTYR over 3 rounds failed intercept + wound each round = 3 Momentum. Meaningful recovery. Design-valid.

---
## SIM-BG-02 — BG Mandate Suppression Combined Options A+B

P(suppression success, Ob capped at 4, combined pools with coalition +2D/faction):
1 faction 5D: P(≥4, 5D TN7)≈16%
2 factions 5D+4D+2D bonus=11D: P(≥4, 11D TN7)≈68%
3 factions 5+4+3+4D bonus=16D: P(≥4, 16D TN7)≈90%

F01 OK: Gradient rewards coordination without trivialising solo suppression.
F02 OK: Consistent with Excommunication Ob cap (PP-180).
F03 P2→PP-296: Coalition auto-trigger (same-phase suppression actions) — no pact declaration needed.
F04 OK: Excommunication (PP-180) unaffected — separate action targeting character, not faction stat.

PP-296 applied: Ob cap 4 + coalition +2D/faction (auto, max +6D at 4+).
ED-172/ED-293 resolved.
