# SIM-X-28R — BG Multi-Faction Re-simulation with Decision Protocols
## Date: 2026-04-04 | Mode: G5 (BG) | Protocols: FACTION-LOYAL, RITUAL, FACTION-OPPORTUNIST, RISK-AVERSE, MARTYR
## 7-Dimension Tag:
## Mechanics: BG Turn Sequence, Domain Actions, TC, Coalition | Mode: BG | Temporal: PRES
## Tracks: TC, Mandate, Wealth, Stability, Public Instability | Factions: Crown, Church, Hafenmark, Varfell, Restoration Movement
## NPCs: None (faction actors) | Archetypes: FACTION-LOYAL, RITUAL, FACTION-OPPORTUNIST, RISK-AVERSE, MARTYR

## Protocol Assignments
- Crown: FACTION-LOYAL (Mandate expansion goal)
- Church: RITUAL (Phase 1: Mandate, Phase 2: Intel suppress, Phase 3: TC trigger)
- Hafenmark: FACTION-OPPORTUNIST
- Varfell: RISK-AVERSE
- Restoration Movement: MARTYR (protecting Public Instability from rising)

## Starting BG State: Crown M5 I5 W4 Mil4 Sta4 | Church M5 I6 W5 TC28 | Hafenmark M4 I4 W5 | Varfell M3 I4 W3 Mil4 | Restoration M2 I3 W2 Sta3 | PI=5

---
## Turn 1
Crown [FACTION-LOYAL]: Royal Proclamation (M+1, Ob2). 5D TN7. E[net]=1.5. P(≥2)≈64%. Success. M 5→6.
Church [RITUAL Phase1]: Mandate expansion. 5D TN7. P(≥2)≈64%. Success. M 5→6.
Hafenmark [FACTION-OPPORTUNIST]: No trigger. Trade income +1W auto. W 5→6.
Varfell [RISK-AVERSE]: Mandate Ob2, 3D, P(≥2)=30% — exactly at rejection threshold. Reject. Intel maintain (Ob1, 4D, P(≥1)≈87%). Intel held.
Restoration [MARTYR]: Community Weaving (PI-1, Ob2). 3D TN7. E[net]=0.9. P(≥2)≈30%. FAIL. PI=5.

Coalition attempt: Crown proposes pact with Church (defer TC). Church [RITUAL] cannot accept — Phase 3 is in sequence. COALITION FAILS.

## Turn 2
Crown [FACTION-LOYAL]: Mandate M6, attack Hafenmark M. Ob=Hafenmark M=4. Pool 6D. P(≥4)≈20%. FAIL.
[FACTION-LOYAL viability gate absent in v1.0 — PP-257 adds gate, would have blocked this action]
Hafenmark [FACTION-OPPORTUNIST]: Crown failed — opportunity fires. Suppress Crown M6. Ob6. Pool 4D. P(≥6)<1%. UNVIABLE (PP-258). Pass.
Varfell [RISK-AVERSE]: Still Ob2, 3D, P=30%. Reject again. 2 consecutive passive turns.
Restoration [MARTYR]: Community Weaving. 3D. P≈30%. FAIL. PI=5.

## Turn 3
Church [RITUAL]: Phase 2 (Intel suppress, Ob5, 6D, P≈3%) — gate fires (PP-257). Skip. Phase 3: TC trigger action.
TC: 28→28+increment [GAP-SIM-X-28R-G02]
Hafenmark [FACTION-OPPORTUNIST]: Church committed to TC — M6 exposed. Suppress Ob6. Pool 4D. P<1%. UNVIABLE. Pass. Third consecutive non-action.
Varfell [RISK-AVERSE]: Rivals at M-cap. Varfell opportunity. Still Ob2, 3D, P=30%. Reject. [SIM-X-28 "timing error" = protocol artefact under RISK-AVERSE — no error, correct protocol behaviour]
Restoration [MARTYR]: CW attempt. 3D. P≈30%. Expected: FAIL. PI=5.

---
## Findings

F01 [OK]: MARTYR Restoration viable over multi-turn horizon (P(≥1 success in 3 turns)≈66%). Correct design.
F02 [OK]: RITUAL prevents coalition — mechanically correct, not a system flaw. Church NPC should not be offered coalitions requiring sequence deviation.
F03 [P1→PP-257]: FACTION-LOYAL executes 20% action (SIM-X-28 "self-inflicted crisis"). Feasibility gate required.
F04 [P2]: RISK-AVERSE Varfell (M3 BG) cannot take Ob2 actions — permanently passive. → GAP-SIM-X-28R-G01
F05 [OK/methodology]: "Varfell timing error" from SIM-X-28 is protocol-relative artefact. RISK-AVERSE never acts at 30% failure. Label protocols before assessing errors.
F06 [P1→ED-172]: BG Mandate suppression Ob=target Mandate creates ceiling. Hafenmark (4D) cannot challenge Church/Crown (M6). No viable counter-play for M<5 factions. Dominant faction self-reinforces.

## Gaps
- GAP-SIM-X-28R-G01: No escalation trigger to pull RISK-AVERSE actors out of permanent passivity
- GAP-SIM-X-28R-G02: TC per-action increment not in params_board_game (carried)
