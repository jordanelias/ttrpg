# Simulation Report: Church Graduated Seizure (PP-494)
## Test ID: SIM-GS-01
## Date: 2026-04-09
## Modes: A + D + J + L
## Sources: params_board_game.md, params_factions.md, valoria_bg_v05, canon/02_canon_constraints.md

---

## FETCH LOG
canonical_sources.yaml:            ✓ (154 lines)
designs/board_game/valoria_bg_v05: ✓ (734 lines)
references/params_factions.md:     ✓ (565 lines)
references/params_board_game.md:   ✓ (1541 lines)
canon/02_canon_constraints.md:     ✓ (25 lines)

---

## MECHANIC SPEC (PP-494)
- **Pool:** Influence + floor(TC / 15)
- **Ob:** 7 − CV (floor 1)
- **Prerequisites:** Church Mandate ≥ 4. Prominence (Church Mandate > controlling faction Mandate).
- **Overwhelming:** CV +1 in target territory
- **Failure:** Stability −1
- **Political cost:** Casus Belli granted to defending faction on every attempt
- **Limit:** One seizure attempt per season. Cannot target T15 or T16.
- **Gate:** Post-TC 75 only (inherited from TC 75 seizure section)
- **At TC=75 (frozen):** Pool = Influence + 5 (constant)

---

## MODE A — ISOLATION TABLES

### A1. Pool vs TC (Influence=6, CV=3, Ob=4)
| TC | Pool | P(OW) | P(Suc) | P(Part) | P(Fail) | E[CV+] |
|-----|------|-------|--------|---------|---------|--------|
| 28 | 7 | 0.096 | 0.194 | 0.290 | 0.420 | 0.096 |
| 30 | 8 | 0.174 | 0.232 | 0.279 | 0.315 | 0.174 |
| 40 | 8 | 0.174 | 0.232 | 0.279 | 0.315 | 0.174 |
| 50 | 9 | 0.267 | 0.251 | 0.251 | 0.232 | 0.267 |
| 60 | 10 | 0.367 | 0.251 | 0.215 | 0.167 | 0.367 |
| 70 | 10 | 0.367 | 0.251 | 0.215 | 0.167 | 0.367 |
| 75 | 11 | 0.467 | 0.236 | 0.177 | 0.119 | 0.467 |
| 85 | 11 | 0.467 | 0.236 | 0.177 | 0.119 | 0.467 |
| 90 | 12 | 0.562 | 0.213 | 0.142 | 0.083 | 0.562 |
| 99 | 12 | 0.562 | 0.213 | 0.142 | 0.083 | 0.562 |

### A2. Pool vs CV (TC=75, Influence=6)
| CV | Ob | Pool | P(OW) | P(Suc) | P(Part) | P(Fail) |
|-----|-----|------|-------|--------|---------|---------|
| 0 | 7 | 11 | 0.029 | 0.070 | 0.147 | 0.753 |
| 1 | 6 | 11 | 0.099 | 0.147 | 0.221 | 0.533 |
| 2 | 5 | 11 | 0.247 | 0.221 | 0.236 | 0.296 |
| 3 | 4 | 11 | 0.467 | 0.236 | 0.177 | 0.119 |
| 4 | 3 | 11 | 0.704 | 0.177 | 0.089 | 0.030 |
| 5 | 2 | 11 | 0.881 | 0.089 | 0.027 | 0.004 |

### A3. P(Failure) full matrix [Influence=6] — Stability drain per attempt
| CV | Ob | TC=75 | TC=80 | TC=85 | TC=90 | TC=99 |
|----|-----|-------|-------|-------|-------|-------|
| 0 | 7 | 0.753 | 0.753 | 0.753 | 0.665 | 0.665 |
| 1 | 6 | 0.533 | 0.533 | 0.533 | 0.438 | 0.438 |
| 2 | 5 | 0.296 | 0.296 | 0.296 | 0.225 | 0.225 |
| 3 | 4 | 0.119 | 0.119 | 0.119 | 0.083 | 0.083 |
| 4 | 3 | 0.030 | 0.030 | 0.030 | 0.020 | 0.020 |
| 5 | 2 | 0.004 | 0.004 | 0.004 | 0.002 | 0.002 |

### A4. Influence degradation impact (TC=75)
| Influence | Pool | P(Fail) CV=3 Ob=4 | P(Fail) CV=5 Ob=2 |
|-----------|------|-------------------|-------------------|
| 2 | 7 | 0.420 | 0.028 |
| 3 | 8 | 0.315 | 0.017 |
| 4 | 9 | 0.232 | 0.010 |
| 5 | 10 | 0.167 | 0.006 |
| 6 | 11 | 0.119 | 0.004 |

---

## MODE D — EDGE CASES

**D1. Ob floor (P-28):** CV=5 → Ob=2. CV maximum is 5, so Ob minimum is 2. No Ob floor violation possible. Clean.

**D2. CV=0 territory:** Ob=7, Pool=11 (TC=75). P(Fail)=0.753. Effectively unsieizable — 75% Stability drain rate. CV=0 territories function as a natural structural firewall. Good design.

**D3. Mandate=4 split gate:** Mandate ≥ 4 prerequisite is satisfied at M=4, but prominence (Church M > controlling M) requires M ≥ 5 against a M=4 defender. The two conditions are independent but create a confusing dual gate. Low severity — correct as written, could be clearer.

**D4. [FINDING D4-P2]:** At Influence=0, TC=75: Pool = floor(75/15) = 5D. Church cannot be mechanically locked out of seizure by Influence damage alone. TC/15 component provides a non-trivial floor. Casus Belli cost still applies per attempt.

**D5. [FINDING D5-P1 — P1]:** Graduated Seizure pre-TC 75 availability is AMBIGUOUS. PP-494 is filed under the TC 75 section, implying post-75 gate. But the formula (Influence + floor(TC/15)) is defined at TC=28 in params_board_game, suggesting it may be a general formula applicable earlier. If available pre-75, it interacts with standard Assert/Suppress and TC generation — major precedent implications.

**D6. TC frozen pool cap:** Post-freeze, floor(TC/15) = 5 (constant). Church pool caps at Influence + 5 = 11D forever. Seizure success removes territories from Conviction Yield pool (PP-473 dead zone), reducing future Conviction Yield. TC stays frozen regardless. Structurally self-consistent.

**D7. [FINDING D7-P1 — P1]:** RULE CONFLICT. PP-421 states OW CV+1 'counts against ±1 CV seasonal cap.' PP-494 states OW CV+1 is 'not cap-governed.' These are directly contradictory. PP-494 is more recent and specific. Provisional ruling: PP-494 governs. Requires confirmation.

---

## MODE J — COGNITIVE LOAD

**J1. [FINDING J1-P2]:** No 7−CV Ob quick-reference table exists in spec. Players must compute Ob from CV on the fly. Recommend adding a seizure Ob reference row to territory cards or seizure section of params.

**J2. [FINDING J2-P2]:** Seizure resolution requires 10 simultaneous state checks. No resolution checklist exists. This is table-critical: missed PI reduction, unresolved Casus Belli, or forgotten Conviction Yield dead zone are likely in play. A dedicated resolution checklist card is warranted.

**J3. [FINDING J3-P1 — P1]:** RULE CONFLICT. Standard TC 75 seizure Ob = 2 + Fort Level + max(0, 3−CV). Graduated Seizure Ob = 7−CV only — Fort Level absent. If Graduated Seizure supersedes Standard Seizure post-75, Fort Levels become irrelevant to Church seizure Ob. ED-355 flagged this but the design consequence (Fort Levels as a defence mechanic) is not captured in that flag.

**J4. [FINDING J4-P2]:** Prominence check timing unspecified. Prominence can shift mid-season via Excommunication or Mandate damage. Whether it is checked at seizure declaration vs resolution determines exploitability. Ambiguous.

---

## MODE L — PRECEDENT / CROSS-SYSTEM

**L1. [FINDING L1-P2]:** Composite pool (stat + clock/15) has no precedent in any other faction action. Risk of players forgetting the TC/15 bonus (+5D at freeze). Faction mat reminder needed.

**L2. [FINDING L2-P1 — P1]:** Casus Belli is referenced in PP-494 but has no definition anywhere in params_board_game.md. The mechanic's effects are entirely undefined. Cannot simulate correctly. Blocks accurate play.

**L3. Stability sustainability:** At CV=3 targets (Influence=6, TC=75): expected drain 0.12 Stability/season — sustainable across a long game. At CV=0 targets: 0.75 Stability/season — unsustainable, eliminates Church in 6–7 seasons. Seizure strategy should rationally avoid CV=0 territories. Good natural deterrent.

**L4. [FINDING L4-P2]:** CV overflow on OW not addressed. If target is already CV=5, OW bonus (CV+1) is wasted. Church should target CV 3–4 for optimal OW value. Design implication: Church seizure strategy has a natural mid-CV sweet spot.

**L5. [FINDING L5-P1 — P1]:** Battle trigger on Graduated Seizure success in contested territory is unspecified. Cascade Test 4 in bg_v05 establishes a precedent that TC-threshold seizure success triggers Battle when military units are present. PP-494 is silent on whether this applies to Graduated Seizure.

**L6. [FINDING L6-P2]:** Post-TC 75, mandatory Assert (PP-480, mandatory at TC 50–74) has no TC effect (TC frozen). Church must still spend the action but gains nothing. It is not specified whether mandatory Assert is suspended in the seizure phase. Significant action economy impact.

---

## FINDINGS REGISTER

| ID | Severity | Description | Action |
|----|----------|-------------|--------|
| D5 | P1 | Graduated Seizure pre-TC 75 availability ambiguous — no TC gate stated in PP-494 | ED required |
| D7 | P1 | PP-421 vs PP-494 OW CV cap conflict — contradictory rules | ED required |
| J3 | P1 | Fort Level absent from PP-494 Ob formula vs present in PP-421 standard seizure | ED-355 (open) |
| L2 | P1 | Casus Belli undefined — mechanic referenced but no ruleset definition | GAP — patch required |
| L5 | P1 | Battle trigger on Graduated Seizure success unspecified | ED required |
| D4 | P2 | Influence=0 does not lock out seizure — TC floor component still provides dice | Note |
| J1 | P2 | No 7−CV Ob quick-reference in spec | Infrastructure |
| J2 | P2 | No seizure resolution checklist — 10 simultaneous state checks | Infrastructure |
| J4 | P2 | Prominence check timing unspecified | ED required |
| L1 | P2 | Composite pool formula has no precedent — risk of forgotten +5D bonus | Infrastructure |
| L4 | P2 | CV=5 OW overflow unaddressed — wasted Overwhelming consequence | Note |
| L6 | P2 | Mandatory Assert post-TC 75 has no TC effect — action economy waste | ED required |

**P1 total: 5 | P2 total: 7**

---

## EDITORIALS RAISED

| ED | Description | Blocks |
|----|-------------|--------|
| ED-NEW-A | Graduated Seizure availability: pre-TC 75 vs post-TC 75 only | Simulation correctness |
| ED-NEW-B | PP-421 vs PP-494 Overwhelming CV cap conflict | Seizure resolution |
| ED-NEW-C | Prominence check timing: declaration vs resolution | Action sequencing |
| ED-NEW-D | Battle trigger on Graduated Seizure success in contested territory | Cascade resolution |
| ED-NEW-E | Mandatory Assert (PP-480) suspension post-TC 75 | Action economy |
| GAP | Casus Belli mechanic undefined | Playability |

---

## WHAT IS WORKING
- Ob formula (7−CV) creates a natural CV gradient: high-CV territories are easy, low-CV are risky.
- CV=0 territory P(Fail)=0.75 acts as a structural firewall — mechanically elegant.
- Pool growth (Influence + floor(TC/15)) rewards early investment in Influence.
- Stability drain on failure is appropriately calibrated for median-CV targets (0.12/season).
- Post-freeze pool cap (11D) is clean: no runaway scaling after TC=75.