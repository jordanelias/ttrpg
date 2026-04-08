# SIM-VAR-05 — Hybrid: Crown Zoom In During BG Campaign Arc
## Mode: C (Full Scenario) + K2 (State Transfer) + G-HY + B (Interaction Chain)
## Date: 2026-04-08 | Multi-season BG arc with Zoom In, personal combat, Domain Echo chain

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1375 lines)
params_core.md: ✓ (161 lines)
params_mass_combat.md: ✓ (500 lines)
state_transfer_spec.md: ✓ (230 lines)

---

## Scenario

**4-player BG, Season 6.** Crown has TCV 14, pressing toward Regency (needs 16). Hafenmark at TCV 9. Church at TCV 4 (TC 36). Varfell at TCV 6.

Crown's player controls Marshal Edren (PC General): Coordination 4, Endurance 4, Health 10, Spirit 3, Attunement 2, TS 28.

Crown wants to take T9 (Himmelenger, Church capital, TCV 3). If successful: TCV 14+3 = 17, exceeds Regency threshold. T9 has Fort 2, Church Military 4 + Fort 2 = 6D defending. Crown Military 4D attacking + Fort bonus doesn't apply to attacker. Battle at T9.

**Zoom In trigger:** Crown player has Marshal Edren personally leading the assault. Player declares Zoom In.

**BG phase suspends at Phase 4 (Battle resolution phase).**

---

## State Transfer: BG → TTRPG

Per state_transfer_spec.md §1:

| BG Variable | TTRPG Equivalent | Value |
|---|---|---|
| T9 CV (4) | Scene context: strong Piety, NPC crowds hostile | Read-only |
| Crown unit Strength (Military 4) | TTRPG unit Str = ⌈4 ÷ 1.5⌉ = 3 | 3 units of Str 1 each |
| Church defender Cohesion 6 | TTRPG Cohesion 6 direct | Cohesion 6 |
| Church Fort 2 | Defender +2D | Applied to Church pool |
| BG phase suspended at Phase 4 Battle | TTRPG scene opens: Assault on Himmelenger | Phase held |
| Church Inquisitor in T9 (AP 3 from S5) | Inquisitor NPC: Willpower 4, Mandate-equivalent 4 | Present in scene |

**Variables suspended:** All other faction BG turns. RS, TC clocks don't advance during Zoom In scene.

---

## TTRPG Scene: Assault on Himmelenger

**Scene framing:** Marshal Edren leads Crown's assault force. Church defenders hold the Cathedral gates. Cardinal Klapp (Intelligence 4, Willpower 5) is coordinating the defence from inside. Inquisitor Vald (Intelligence 3, Willpower 4) is at the gates interrogating a suspected Crown sympathiser.

**TTRPG units:**
- Crown: 3 units (Str 1 each), Command = Edren Coordination 4, Power = Military÷size converted via B.2 (Crown Military 4 → Power 2).
- Church defenders: 2 units (Cohesion 6, +2D Fort). Power (Church Military 4 → P 2).

**Mass Combat Turn 1:**

**Phase 1 — Strategy:** Crown plays Advance (engage, Aggressive). Church plays Hold (Defend, Defensive).

**Phase 2 — Volley:** No ranged units declared. Skip.

**Phase 3 — Manoeuvre:** Crown advances to engagement range.

**Phase 4 — Thread (Edren TS 28):** TS 28 < 30 minimum for Leap. Edren cannot Thread. Church has no practitioner in the scene (Klapp TS unspecified, assume non-practitioner — Cardinal). Skip Phase 4.

**Phase 5 — Engagement:**
Crown pool: min(Size 3, Command 4) + Command 4 = 3+4 = **7D**. TN 7, Ob = Church Cohesion ÷ 2 = 3. Roll: 7D vs Ob 3.
E(net) = 7 × 0.572 = 4.0. P(Success ≥ 3): ~80%.
Result: **Success** (net 4). Damage = net successes × (1+Power) = 4 × 3 = 12 damage.
H per Size = min(Discipline=6, Command=Edren's Command for defender? No — Church defender Command is their own). Church defender Command: assume Command 4 (standard trained unit). H = min(6,4)+DR. DR (Damage Reduction) for fortified defenders: Fort 2 → DR 2. H = 4+2 = 6. Total Health = 2 × 6 = 12.
Church takes 12 damage → Health 12−12 = 0. Church Size = ⌊0÷6⌋ = 0. **Church gate unit destroyed.**

Church counter-attack: pool = min(Church Size 2, Command 4) + Command 4 + Fort 2 = 2+4+2 = **8D**. Ob = Crown Cohesion ÷ 2 = ... Crown Cohesion: not transferred from BG directly. Cohesion for Crown units starts at TTRPG default: set to BG Cohesion equivalent = Crown Military 4 → B.2: TTRPG Cohesion 4 (BG 1–5 → TTRPG 1–5 direct). Ob = 4÷2 = 2.
8D vs Ob 2. E(net) ≈ 4.6. P(Success): ~95%.
Damage = 4.6 × 3 = 13.8 → call it 14. Crown H = min(4,4)+0DR = 4. Total Health = 3 × 4 = 12.
Crown takes 14 damage → Health 12−14 = −2. Size = 0. **Crown assault force destroyed.**

**Both sides wiped in Turn 1.** Mutual annihilation.

**Phase 6 Cascade — Edren personal action (Step 4):**
Edren is the General. Both units are gone. Edren is alone in the breach.

**Personal combat phase (Edren in the gates):**
Edren faces Inquisitor Vald (Willpower 4, Coordination 3, Health = Endurance+6 = ?). Assume Vald Endurance 3 → Health 9.

Edren: Coordination 4, Health 10, Spirit 3.
Edren attacks: Combat Pool = Agi + hist_pts + 3 (PP-247). Assume Agi 3, History combat bonus 1: CP = 3+1+3 = **7D**. TN 7, Ob = Vald's Endurance ÷ 2 = 1.5 → Ob 2.
Result: **Overwhelming** (net 8, ≥ 4 and ≥ 3). Damage: net 8, Vald Health −8 → Health 1. Vald Rattled (Health ≤ Endurance/2? No — Rattled in personal combat = wound threshold. Check: at Health ≤ 3, Vald takes a Wound (−1D). Vald Health 1, Endurance 3: ≤ 3 → **Vald takes Wound**. −1D to Vald's pool.

Vald counter-attack: CP = (Coordination 3)+(hist 1)+(3) = 7D, −1D Wound = **6D** vs Edren Ob 2. Net ~3.4 expected. Result: **Success** (net 3). Edren Health −3 → Health 7. No Wound (7 > Endurance 4).

**End of Turn 1 personal combat.** Vald Health 1, Wounded. Edren Health 7, unwounded.

**Turn 2 mass combat — reinforcements?** Church's second unit (inside Cathedral, not yet engaged). Klapp sends the reserve unit through the gates. Church unit 2: same stats as unit 1 (Cohesion 6, Command 4, Fort 2D in T9).

Edren alone vs Church unit 2: Edren cannot fight a mass combat unit in personal scale (different resolution tiers). **Ruling:** Edren retreats to avoid death by formation. Zoom Out triggered by Edren's retreat.

---

## State Transfer: TTRPG → BG (Zoom Out)

Per state_transfer_spec.md Zoom Out:

| TTRPG Outcome | BG Update |
|---|---|
| Crown assault force destroyed (Size 0) | BG Crown Military −2 (unit lost; Crown Military 4 → 2). |
| Church gate unit destroyed | BG Church unit Strength −1 (converts back). Church Military 4 → 3 effective in T9 this season. |
| Vald Wounded | BG: commander bonus unaffected (wounds personal). Church Inquisitor in T9 flagged as "Wounded Inquisitor" — next season AP generation in T9: −1D on Active Inquisition (Vald impaired). |
| Edren retreats (Health 7) | Edren Health 7, no wound. BG: Commander bonus intact. Crown assault fails — T9 not taken. |
| No Thread ops | No RS change. |
| No Domain Actions during scene | No Domain Echoes queued. |

**BG resumes at Phase 4 Battle resolution:** Crown assault on T9 failed. T9 remains Church-controlled.

---

## Post-Zoom BG Resolution (Season 6 continued)

**Crown's situation:** TCV 14 (unchanged). Military 2 (reduced from 4 — major blow). Royal Decree: Crown plays Decree targeting Hafenmark (Mandate 5D vs Ob 2, targets Hafenmark Stability). Church still holds T9.

**Domain Echo chain:** No Domain Echo fired from Zoom In (no Domain Actions taken during scene). But Edren's personal combat with Vald creates a narrative echo: Church will remember the assault, affecting future Diplomacy.

**[RULING: Personal combat outcomes in Zoom In are NOT Domain Echoes unless they explicitly involve a Thread operation or stated Domain Action. Edren fighting Vald is a tactical personal event — no BG faction-stat consequence queues automatically. GM may apply narrative consequence (Church Mandate +1 "righteous resistance to invasion") but this is not a mechanical Domain Echo.]**

**TC Accounting (S6):** Church played Assert earlier (TC +2). Hafenmark structural (−1). Net TC: 36 + 2 − 1 = **TC 37**.

**Critical finding — Crown Military post-Zoom:** Crown's Military 2 means:
- Future March rolls: 2D vs Ob 2. P(Success): ~22%. Crown can barely sustain military operations.
- Crown TCV 14 is now harder to extend — they need Diplomacy, not Military, to reach Regency.
- Formal Crown Treaty offers become the dominant Crown strategy. TCV 14 + Church Treaty (Church Mandate ≤ 2 OR Treaty) + Hafenmark Treaty... but Treaties require both parties to agree.

---

## Mode B: Domain Echo Interaction Chain

**Chain: Zoom In outcome → BG Military stat reduction → Crown strategy pivot**

Step 1: Zoom In assault fails. Crown Military 4 → 2 (BG state update on Zoom Out).
Step 2: With Military 2, Crown cannot pursue Military Consolidation path. Crown pivots to Diplomacy-heavy play.
Step 3: Crown plays Formal Crown Treaty with Hafenmark (both factions agree — Hafenmark Mandate −1 for Treaty, but Hafenmark is satisfied: they want Crown weak). Treaty: Hafenmark Mandate 4 → 3 (−1 for Treaty), Hafenmark Stability +1 → 5.
Step 4: With Treaty in place, Crown's Regency condition for Hafenmark is met (Treaty counts as "suppressed" for the rival Mandate condition).
Step 5: Crown still needs Church Mandate ≤ 2 OR Church Treaty OR Church eliminated. Crown plays Decree chain targeting Church. Church Mandate 5 → 4 → 3 → 2 over 3 seasons at Ob 3 (consecutive penalty).
Step 6: By S9, Crown meets Regency conditions: TCV 14 (insufficient — needs 16), Hafenmark Treaty ✓, Church M 2 ✓, IP 24 < 60 ✓, PI ~4 (if Hafenmark has been running Parliamentary Manoeuvre) ✓.

**TCV still insufficient at 14.** Crown must gain TCV 2 more without military capacity. Only path: Varfell-targeted Treaty (TCV += Varfell territories if Treaty counts?). No — Treaty grants the Mandate condition, not TCV transfer. Crown must hold territories.

**Crown can play Royal Charter:** Crown Charter Territory in T5 (Feldmark, Crown TCV 1 — already held). Charter gives −2 Ob to Crown own actions in T5. Doesn't help TCV.

**Finding P1 — Crown Military loss from Zoom In creates a victory-blocking cascade.** Military 2 prevents further territorial expansion. Crown TCV 14 is 2 short of Regency. Without military, Crown cannot take the 2 TCV needed. Crown is forced into a Diplomacy win that requires Church Mandate ≤ 2 — achievable via Decree chain but slow (3 seasons) and uncertain (Ob 3 at 5D = 68% per roll, ~3 attempts needed). Expected S9 resolution assumes no Church counter-play.

---

## Findings Summary

| ID | Severity | Finding |
|----|----------|---------|
| F-HY-01 | P1 | Mutual unit annihilation in Turn 1 is reachable at matched pools. When both sides eliminate each other, the General is exposed to personal combat with no unit support — dramatic and correct, but creates extreme pressure on the PC. |
| F-HY-02 | P2 | Crown Military loss from failed Zoom In (4→2) creates a strategy-forcing cascade: no military expansion possible, pivot to Diplomacy mandatory. Hybrid mode has asymmetric downside risk that BG-only play doesn't reveal. |
| F-HY-03 | P2 | Wounded Inquisitor BG trace (−1D on next Active Inquisition) is a clean Zoom Out consequence. No rule existed for this; gap-filled as "Wounded commander reduces that action's pool next season." |
| F-HY-04 | P3 | Personal combat NPC outcomes during Zoom In do not automatically queue as Domain Echoes (no Domain Action taken). GM discretion only. Confirm this is intentional design. |

