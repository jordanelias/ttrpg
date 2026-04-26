# VALORIA — Simulation & Test Inventory (5-Day Review)
## What the audit documents are missing from tests/simulations
## Date: 2026-04-15

---

## SIMULATION SESSIONS CONDUCTED (April 10–15)

### 1. valoria_sim.py v4 — Full Campaign Simulation (April 14)

**20/20 tests passing.** Key results:

| Metric | Board Game | Hybrid |
|---|---|---|
| Church Theocracy victory | 53% | 45% |
| Crown Treaty victory | 14% | 16% |
| Timeout (no victory) | 32% | 39% |
| Average game length | 13.3 years | 14.5 years |
| Crown collapse rate | 3.4% | — |
| Hafenmark collapse rate | 27.8% | — |

**Critical finding:** Church dominates the pure AI faction layer. The only counter-CI mechanic is Hafenmark's diplomatic token, which is fragile (Hafenmark collapses 27.8% of the time before it can be used effectively). This is the finding that motivated tc_political_redesign_v30.

**My audit documents never referenced these numbers.** They directly inform every balance discussion.

### 2. SIM-NPC-01 — NPC Behavior Simulation (April 14)

Ran NPC behavior system against faction AI. 7 findings, 4 patches applied:

| Patch | Fix | Why It Matters |
|---|---|---|
| PP-NPC-01 | Crown Decree gated on Mandate ≥ 3 | Prevents death spiral where Almud keeps issuing Decrees at low Mandate, failing, losing more Mandate |
| PP-NPC-02 | Deterministic coup requires active Church Assert, not just passive CI | Prevents coup from firing based on a clock no player actively controls |
| PP-NPC-03 | Church Influence drift conditioned on Stability + CI + yearly cycle | Prevents runaway Church Influence accumulation |
| PP-NPC-04 | Varfell Private Collection cooldown enforced | Prevents unbounded VTM advancement |

**My documents mentioned none of these.** They're critical for videogame AI.

### 3. SIM-STRESS-04/05/06 — Social Contest & Combat Calibration (April 4-5)

All prior SIM-DEBTs cleared in this session:

| SIM-DEBT | Finding |
|---|---|
| SIM-DEBT-01 | Charisma×2 pool: ±1 Cha gap = ~25-30% Grand Contest win rate (correctly non-dominant). ±4 gap = Total Victory in 2 exchanges. |
| SIM-DEBT-03 | Two-genre integer-dice system calibration confirmed. Primary genre +2D → ~1pt/exchange net at resistance 1. |
| SIM-DEBT-04 | Expert Judge vs Crowd: same pair reverses advantage (Cognition-heavy vs Charisma-heavy). Confirmed adjudicator type matters. |
| SIM-DEBT-06 | War-scale Coherence: practitioner operating every turn of 7-turn battle loses 7 Coherence (10 → 3, Dissonant). Severance requires 9+ consecutive ops. |
| SIM-DEBT-07 | High-resistance contest: resolved via ED-164 Option A. |

**Key calibration finding:** PP-285 confirmed — Rescue provides no Defence roll on redirect (armour DR only). This makes Rescue a genuine sacrifice that earns +2 Momentum.

**Coalition Grand Contest:** Shared pool (14) handles 5 exchanges without hitting Spent. Coalition Concentration mechanic works.

### 4. SIM-DEBT-FW-01 through FW-10 — Fieldwork Simulations (April 13)

All 10 items resolved:

| Finding | Result |
|---|---|
| Ob calibration | 5D pool handles Depth 1. 9D handles D1-2. 13D handles D1-3. 17D handles D1-4. 24D challenges D5. |
| Evidence pacing | 5-threshold investigation completes in 3-5 scenes (high-pool 15-19D). Low-pool (9D): 4-6 scenes at D1-2. |
| Disposition economy | Neutral→Bonded = 6-8 actions across 3-4 seasons. Sincerity Gate adds ~37% failure on instrumental Connect. |
| Attention Pool feedback | Fieldwork contributes ~11% of max CI acceleration over 4 seasons. Cap sufficient. |
| Survey vs Govern | Different niches. Govern dominates mid-proximity. Survey dominates high-proximity. Neither universally optimal. |
| Cover calibration | Cover 3 = detected in 3 scenes. Cover 9 = full season before detection. Cover 12+ = near-immune to casual detection. |
| Transition simulation | All 6 fieldwork ↔ other-system transitions functional (F-TRANS-01 through F-TRANS-12). |
| Thread × fieldwork | All Thread ops may advance Evidence Track contextually. |
| NPC arc cascades | 7 Domain Echo cascades tested. NPC Disposition −2 if investigated; +1 if NPC wanted truth found. |
| Extended threadwork | Knot-mediated remote Thread-Read: +1 Knot strain/use. Detection → Disposition −3. |

### 5. Mass Combat Stress Test (April 10)

Validated post-patch mechanics:

| Mechanic | Result |
|---|---|
| PP-502 (deterministic Discipline) | ✓ Working — degrades when Size lost > Discipline AND asymmetric loss |
| PP-504 (Command per sub-unit) | ✓ Full Command to each sub-unit independently |
| PP-505 (Thread-destroyed units) | ✓ Participate in Phase 5 with pre-Thread Size; removed at Phase 6 Step 1 |
| PP-506 (bilateral general combat) | ✓ Both armies fight uncommanded; 1D minimum per unit |
| PP-507 (mutual destruction) | ✓ Draw; no territory change; both Stability check Ob 1 |
| PP-508 (splitting doctrine) | ✓ Split dominates concentration +9% to +45%. Counter: Narrow Pass terrain or Feigned Retreat. |

### 6. Opposing Threadwork Stress Test (April 14)

13 scenarios tested across 3 candidate approaches. Key validated mechanics:

| Mechanic | Finding |
|---|---|
| Mending immunity | Mending categorically immune to direct opposition (different target category — substrate absence vs thread presence). Philosophical derivation, not arbitrary rule. |
| Opposing engagement modifier | +floor(opponent TPS / 2), min +1. Opponent's configuration IS part of thread's resistance. |
| N-way opposing (3+) | Automatic lattice collapse. All ops fail. Gap at target's scale. MS −(2 × number of practitioners). |
| Co-movement in opposition | Coherence per-practitioner. Epistemic + actual effects once per compound event. |
| FR vs FR Both-Fail | Scaling table by scale: Object MS −1 to Structural MS −5, with increasing Shifting Object risk. |
| Sustained opposition | +1 Ob sequential failure penalty. Shifting Object receiving second SO advances one deterioration tier. |

### 7. SIM-BG-01/02 — Board Game Simulations (March-April)

| Finding | Result |
|---|---|
| Church CI race | CI ≥ 60 unreachable in 12-round standard game with Hafenmark suppression active (+1/season net = needs 32 seasons from start) |
| Thread Wound formation | Appropriate pace (requires sustained neglect or repeated failure) |
| Church viable paths | CI-accelerating plays, Excommunicate Baralta, alt victory via Deed 4 (Crown Mandate ≤ 2) |

---

## WHAT MY AUDIT DOCUMENTS MISSED

### Not Referenced At All

1. **valoria_sim.py v4 results** — Church 53% win rate, Hafenmark 27.8% collapse, 13.3-year average. These are the numbers that motivated the tc_political_redesign.
2. **PP-NPC-01 through NPC-04** — Crown Decree Mandate gate, coup determinism fix, Church drift conditioning, Varfell cooldown. All critical for videogame AI.
3. **SIM-STRESS-04/05/06 calibration** — Social contest Cha±1 gap = 25-30%, Cha±4 = Total Victory. Reserve timing confirmed. Coalition mechanic validated.
4. **PP-285 (Rescue no Defence)** — Confirmed via simulation. My combat action table should note this.
5. **Mass combat splitting doctrine** — Split dominates concentration by 9-45%. Only counters: Narrow Pass terrain, Feigned Retreat. My mass combat section doesn't mention this critical tactical finding.
6. **Mending immunity to opposition** — Philosophical derivation validated by simulation. My Thread operations section has it but buries it.
7. **All SIM-DEBT-FW results** — Cover calibration, disposition economy, evidence pacing. These are the calibration data that make the fieldwork system playable.

### Referenced But Incomplete

8. **Hafenmark collapse rate (27.8%)** — I mentioned the sim results in the cross-conversation review but didn't note this as a game balance problem requiring design response.
9. **Church dominance in pure AI** — I noted it but didn't connect it to tc_political_redesign_v30 as the design response.
10. **SIM-BG-02 (CI race)** — The finding that CI ≥ 60 is unreachable with suppression was from March. The tc_political_redesign changes the CI ceiling to 100 and adds milestones at 40/55/65/80 — directly addressing this. I should have connected the finding to the redesign.

---

## UNVALIDATED INTERACTIONS (Flagged by Conversations)

These were explicitly called out in conversations as needing simulation but not yet run:

1. **Accord + Strain + battle consequences compound effect** — peninsular_strain system hasn't been simulated with the full valoria_sim (ED-538, P1).
2. **CI reform + TCV revaluation + Seizure Accord ≥ 2 compound effect on Church** — three simultaneous Church buffs/reforms without combined validation (ED-539, P1).
3. **NPC AI with Accord-aware governance** — priority trees were updated but sim hasn't re-run to check if Hafenmark collapse rate improves.
4. **Dynastic Proclamation and Cultural Reformation** — two new acquisition tools never simulated.
5. **Unit health = Type Health × Size** — Jordan's directive; not yet validated by simulation against existing mass combat balance.
