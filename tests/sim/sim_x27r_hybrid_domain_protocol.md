# SIM-X-27R — Hybrid Domain Season Re-simulation with Decision Protocols
## Date: 2026-04-04 | Mode: G4 (Hybrid) | Protocols: RITUAL, FACTION-LOYAL, FACTION-OPPORTUNIST, BELIEF-FIXED
## 7-Dimension Tag:
## Mechanics: Domain Actions, Faction Stats, TC | Mode: Hybrid | Temporal: PRES
## Tracks: TC, Mandate, Intel, Public Instability | Factions: Crown, Church, Hafenmark
## NPCs: PC (generic) | Archetypes: RITUAL, FACTION-LOYAL, FACTION-OPPORTUNIST, BELIEF-FIXED

## Protocol Assignments
- Church: RITUAL (Phase 1: Mandate, Phase 2: Suppress Crown Intel, Phase 3: TC trigger)
- Crown: FACTION-OPPORTUNIST
- PC: BELIEF-FIXED ("will not act to increase Church power")

## Starting State: TC=0, Church M5 I6 W5 Mil4 Sta5, Crown M5 I5 W4 Mil4 Sta4

---
## Season 1
Church [RITUAL Phase 1]: Mandate expansion. Pool 5D TN7 Ob2. E[net]=1.5. P(≥2)≈64%. Success. M 5→6.
Crown [FACTION-OPPORTUNIST]: No trigger (Season 1, no exposed stats). Passive. Intel maintain (auto). 
PC [BELIEF-FIXED]: Church action (belief violation). Hafenmark trade (belief-neutral). P(≥1 Ob1)≈80%. Success.
TC: 0 (unchanged)

## Season 2
Church [RITUAL Phase 2]: Suppress Crown Intel. Ob=Crown Intel=5. Pool 6D TN7. E[net]=1.8. P(≥5)≈3%. FAIL.
[RITUAL feasibility gate not present in v1.0 — this is the failing case. PP-257 adds gate.]
Crown [FACTION-OPPORTUNIST]: No viable trigger. Passive.
PC: Hafenmark trade again. Success.
TC: 0

## Season 3
Church [RITUAL]: Phase 2 impossible (Ob 5, pool 6D, P<10%). Skip (PP-257 gate). Phase 3: TC trigger.
TC: 0 → 0+increment [GAP-SIM-X-27R-G02: TC per-action increment not in params]
Crown [FACTION-OPPORTUNIST]: Church committed to TC action — Mandate exposed. Opportunity: suppress Church M6. Ob6. Pool5D. P(≥6)<1%. UNVIABLE (PP-258 gate). Crown passes.
PC: Hafenmark trade. Success.

---
## Findings

F01 [OK]: RITUAL correctly models Church institutional delay of TC. Design confirmed.
F02 [P2]: Crown 6% action from SIM-X-27 was protocol mismatch (GREEDY-implicit). FACTION-OPPORTUNIST does not take it. Root cause identified.
F03 [P2]: BELIEF-FIXED PC mechanically isolated in Hybrid — no mandatory PC-engagement path exists for constrained actors. → GAP-SIM-X-27R-G01
F04 [P1→PP-257]: RITUAL executes Ob5 action with 6D pool (P≈3%). Feasibility gate required.
F05 [P2→PP-258]: FACTION-OPPORTUNIST fires on unviable opportunities (Ob6, P<1%). Viability check required.

## Gaps
- GAP-SIM-X-27R-G01: No mandatory PC engagement path in Hybrid seasonal structure for BELIEF-FIXED actors
- GAP-SIM-X-27R-G02: TC per-action increment value missing from params_factions (carried from SIM-X-27)
