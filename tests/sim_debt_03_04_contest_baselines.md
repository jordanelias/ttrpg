# SIM-DEBT-03/04 — Contest System Re-Simulation
## Date: 2026-04-04 | Closes: SIM-DEBT-03 (partial), SIM-DEBT-04 (partial)
## 7-Dimension Tag:
## Mechanics: CLASH, REINFORCE, CROSS, AMPLIFY, adjudicator pools | Mode: TTRPG | Temporal: PRES
## Tracks: Composure, Concentration, Conviction Track | Factions: Crown, Hafenmark
## NPCs: Scholar, Diplomat, Demagogue | Archetypes: GREEDY, SATISFY

## Actors
Scholar: 13D Argue (Expert), 9D (Crowd/NoAdj), Composure 9, Concentration 5, FocDef 1, ChaMod 0
Diplomat: 10D Argue (Expert), 14D (Crowd/NoAdj), Composure 11, Concentration 5, FocDef 1, ChaMod 1
Demagogue: 6D Argue (all types), Composure 12, Concentration 2, FocDef 0, ChaMod 1
Audience: Crown+Hafenmark. Resistance=1. Crown boosts Revealing, Hafenmark boosts Memory.

## SIM-DEBT-03 Results

### A — CLASH Scholar(15D) vs Diplomat(11D) after bonuses
E[margin]=1.2. Movement=floor(1.2×1.0×1.0−1)=floor(0.2)=0.
P(margin≥2, track moves)≈45%. Grand Contest (5 exchanges) insufficient for decisive outcome.
F01 P1→ED-295: CLASH stalls at median. Formula + resistance blocks movement.
F02 P1→ED-295: 5 exchanges insufficient for track to move decisively.
F03 OK: Doubt Marker compounds stall but is correct conditional mechanic.

### B — REINFORCE Scholar(15D) vs Diplomat(11D)
Movement=floor((1.2−1)×1.0×1.0−1)=floor(−0.8)=−1. NEGATIVE for winner.
F01 P1→ED-296: REINFORCE formula error — stronger orator penalised. Fix: max(0,...).

### C — CROSS Scholar(15D) vs Demagogue(6D)
Scholar movement=floor(4.5−1)=3. Demagogue movement=floor(1.8−1)=0. Net: Scholar +3/exchange.
F01 OK: CROSS favours Scholar correctly. Demagogue needs AMPLIFY path.

### D — AMPLIFY Scholar(15D) + Ally(8D) combined
Pool=23D (under cap 30D). Movement=floor(6.9−1)=5/exchange.
F01 OK: AMPLIFY high-yield path. Correct.
F02 P2→ED-297: AMPLIFY (5/exchange) vs CLASH (0/exchange) — AMPLIFY dominant when ally available.

## SIM-DEBT-04 Results

Adjudicator inversion: Expert→Scholar favoured 13D vs 10D (P≈62%). Crowd/NoAdj→Diplomat favoured 14D vs 9D (P≈64%).
F01 OK: Inversion design-valid. Strategic proceeding-type choice meaningful.
F02 P2→ED-297: Crowd vs NoAdj pools identical for Scholar/Diplomat. Distinction only meaningful at high Cha/Att divergence.

## Pending (not yet run)
- AMPLIFY multi-party (3+ orators)
- DIVERGE sequences (ED-133 governs)
- Multi-genre sequence chains
- Demagogue AMPLIFY viable path
