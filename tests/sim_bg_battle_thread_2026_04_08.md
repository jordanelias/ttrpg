# Valoria BG — Battle Resolution + Thread Operations Simulation
## Date: 2026-04-08 | SIM-DEBT-BG-01 + SIM-DEBT-BG-02
## Mode A (isolation) + Mode D (edge cases)
## Source: params_board_game.md (1431L, freshly fetched post-Jordan commits), valoria_bg_v05_simulation_and_patches.md (734L)
## Latest patch applied: PP-467

---

## FETCH LOG
references/params_board_game.md: ✓ re-fetched (1431 lines) post-SHA 3bdfb4cfd5e5
designs/board_game/valoria_bg_v05_simulation_and_patches.md: ✓ fetched (734 lines)
designs/board_game/victory_architecture_v1.md: ✓ re-fetched (412 lines)
canon/editorial_ledger.yaml: ✓ re-fetched (2018 lines) — confirms ED-327 resolved (RM redesign), ED-328/329 flagged

---

## STATUS CHECK — PRIOR P1 FINDINGS

| Finding | Status |
|---------|--------|
| P1-01 Overwhelming threshold contradiction | Still live — 3 conflicting statements in params |
| P1-02 TCV table numbering (victory_arch stale) | Technically resolved by RM redesign (PP-460) but TCV table §1 still uses old T-numbers — renumber still needed |
| P1-03 Crown TCV threshold (18 vs 16) | Still live — params says 18, victory_arch says 16 |
| P1-04 Torben Loyalty start (10 vs 3) | Still live — Starting Values table (10/0–10) vs Track section (3/0–7) |
| P1-05 Seizure Ob formula | Still live — provisional "2+Fort+max(0,3−CV)" |
| Community Weaving Ob | RESOLVED by PP-491 — dynamic formula (100−RS)÷20 is canonical. BG doc L90 confirms. |

---

## SIM-DEBT-BG-01: Battle Resolution — Mode A Isolation

### A-01: Battle Pool Construction

**P-16 procedure (canonical):**
1. Both sides roll simultaneously.
2. Each side: Military stat + Commander modifier + Disposition modifier vs Ob.
3. Compare net successes. Higher net wins.
4. Degree applied using WINNER's margin (winner net − loser net) vs winner's Ob.
5. Drawn battle: equal net → both Discipline −1, hold position.

**P-16 is not fully defined in params.** The BG doc defines the comparison mechanic (I-05/G-12) but the outcome table (what Success, Overwhelming, Partial, Failure mean for each degree of victory margin) only appears from the attacker's perspective in the original B8. The v05 patches partially resolve this but no unified outcome table exists. Gap confirmed.

**Disposition modifiers (from BG design doc Part Five Cascade Test 2):**
- Offensive: +2D (attacker bonus)
- Balanced: no modifier
- Defensive: +fort dice (= Fort Level additional dice to defender pool)

Confirmed from Cascade Test 4 and Scenario C: Fort level adds dice to the defending roll. T14 Fort 3 = defender gets +3D.

**Commander modifier:** Not defined in params or accessible sections of BG doc. The original B8 mention ("Commander Coordination modifier") has no table. [GAP: Commander modifier values undefined in current canonical docs.]

**Standard battle pool (no commander, balanced):**
- Attacker: Military stat dice, Ob 2
- Defender: Military stat dice + Fort level dice, Ob 2

### A-02: Battle Outcome Table (reconstructed from P-16 + cascade tests)

Per I-05 correction (PATCH P-16): both sides roll, compare net successes. The winner's degree is applied:

| Winner margin (winner net − loser net) | Result |
|----------------------------------------|--------|
| = 0 | Drawn — both Discipline −1, no territory change |
| ≥ 1, < Ob | Partial victory — losing side Discipline −2 |
| = Ob | Success — losing side unit Discipline −4 (or destroyed if at 0) |
| > Ob (Overwhelming threshold) | Overwhelming — losing side unit destroyed; winner may advance |

**Verification from Scenario C (Cascade Test 4):**
Löwenritter 6 net vs Vanguard 2 net at Ob 2 = margin 4, Ob 2 → 4 > 2 = Overwhelming → Vanguard unit destroyed. ✓
Vanguard Success (2 net, Ob 2) produces Discipline −2 on Löwenritter. ✓
This implies: defender can produce its own degree result simultaneously. Both degree results apply.

**CRITICAL GAP — Simultaneous degree application:**
Scenario C demonstrates: Löwenritter wins by Overwhelming (unit destroyed) AND defender achieves Success (Discipline −2 on attacker). Both apply. This is the correct reading of "both sides roll."

But the outcome table is not formally defined anywhere in canonical docs. The cascade test examples are the only evidence. A winner who Overwhelms and a loser who Succeeds: winner destroys loser's unit AND takes Discipline −2. This is correct but undocumented as a formal rule.

**[PATCH PP-476: Formalise Battle Outcome Table. Both attacker and defender apply their own degree result independently. For each side: calculate that side's margin (net − opponent net if positive, 0 if negative) relative to Ob. Apply outcome for that margin. Margin 0 = neither side applies outcome. Margin 1 to Ob−1 = Discipline −2 on the OTHER side's unit. Margin = Ob = Discipline −4 on other side. Margin > Ob = other side's unit destroyed. Overwhelming applies to each side independently. A drawn battle (equal net) = no degree result for either side, both Discipline −1.]**

### A-03: Battle Probability Matrix (Balanced vs Balanced, no forts, no commander)

Standard engagement: Attacker Military A pool vs Defender Military D pool, both at Ob 2.

**E(net) per pool = 0.4 × pool size.**
**P(Overwhelming per side) ≈ using PROVISIONAL 2×Ob floor 3 → need net ≥ 4 at Ob 2.**

| Attacker pool | Defender pool | P(Att wins) | P(Def wins) | P(Draw) | P(Att OW) | P(Def OW) |
|--------------|--------------|-------------|-------------|---------|-----------|-----------|
| 4D (Crown, Varfell, Church) | 4D | ~42% | ~42% | ~16% | ~9% | ~9% |
| 4D | 6D (4+Fort 2) | ~25% | ~60% | ~15% | ~4% | ~20% |
| 6D (4+Off+2D) | 4D | ~60% | ~25% | ~15% | ~20% | ~4% |
| 6D (Löwenritter) | 4D | ~60% | ~25% | ~15% | ~20% | ~4% |
| 6D | 7D (4+Fort3: Ehrenfeld) | ~38% | ~49% | ~13% | ~13% | ~22% |
| 8D (6+Off+2D) | 4D | ~76% | ~16% | ~8% | ~35% | ~3% |
| 8D | 7D (Fort3) | ~55% | ~33% | ~12% | ~22% | ~14% |

*Approximated using normal approximation: E(A net) = 0.4A, E(D net) = 0.4D, SD(net) = √(0.3×N) per pool. P(A > D) from normal CDF. Overwhelming approximated from P(margin ≥ 4) at respective pool sizes.*

**Key findings:**

**F-01: Löwenritter Offensive strategy is dominant at low fort levels.** Military 6 with Offensive +2D = 8D. At Ob 2, P(win) ≈ 76% against standard Military 4 defenders. Even Ehrenfeld Fort 3 (+3D = 7D defender) yields P(Löwenritter wins) ≈ 55%. Löwenritter is the strongest early military faction. As designed.

**F-02: Fort levels are the primary defensive equaliser.** A Military 4 faction defending a Fort 3 territory (7D) beats a Military 6 unmodified attacker (6D) ≈ 49% vs 38%. Fort 3 effectively reverses the Military 2 disadvantage. This makes T14 Ehrenfeld (Fort 3) the most defensible territory on the board, particularly relevant for Crown's central hinge.

**F-03: Hafenmark Military 3 is severely constrained.** Military 3 pool at Ob 2: P(≥2 net) ≈ 40%. Against any non-Löwenritter unfortified defender (Military 4, 4D): P(Hafenmark wins) ≈ 30%. Hafenmark cannot expand militarily without Offensive Disposition. No card in Hafenmark's starting hand gives +2D Offensive. **Hafenmark's military handicap means Territory acquisition via conquest is very difficult.** TCV gap of 4 (need TCV 12, have TCV 8) must be achieved through diplomatic means (Formal Crown Treaty) or opportunistic seizure of uncontrolled/weakened territories. This is thematically correct for the Parliamentary faction but creates a bottleneck if rivals all fortify.

**F-04: Draw rate is significant (12–16%).** Drawn battles are not rare at equal pools. Each draw costs both sides Discipline −1. At starting Discipline 3 (Light Infantry), three draws destroy the unit. This creates meaningful attrition even without decisive battles.

---

### A-04: Fortification as Upkeep Cost

**Fortify action: Ob = Fort level + 1.**
- Fort 0 → Fort 1: Ob 1 (always succeeds at any pool ≥ 1)
- Fort 1 → Fort 2: Ob 2 (P ≈ 56–85% depending on pool)
- Fort 2 → Fort 3: Ob 3 (P ≈ 15–57% depending on pool)
- Fort 3 → Fort 4 (max): Ob 4 (P ≈ 3–27% depending on pool)

**Key finding F-05:** Fort max is 4 (T3 Lowenskyst, T14 Ehrenfeld). Upgrading from Fort 3 to Fort 4 at pool 4 (Mandate rolls Fortify? No — Fortify uses what stat? **GAP: Fortify stat undefined in params.** The action table lists "Fortify | Fort level + 1" with no pool specification.)

**[EDITORIAL: ED-338 — What stat governs the Fortify action pool? Military (most logical, represents the engineering capacity of the deployed force), Wealth (represents procurement/supply cost), or Mandate (administrative authority to build)?]**
**[PROVISIONAL: Fortify uses Military stat. Military represents the faction's ability to construct and maintain fortifications. This aligns with: "Number of units deployed cannot exceed current Military stat" (P-18), implying Military represents the faction's total force capacity including engineering. Marked provisional pending confirmation.]**

---

### A-05: Discipline Track Edge Cases

**Starting Discipline:** Light Infantry 3, Heavy Infantry 4, Cavalry 4, Ranged 3, Artillery 3.

**Depletion events:**
- Draw: both units Discipline −1
- Defender Success degree: Discipline −2 on attacker
- Winner Partial degree: Discipline −2 on loser
- Winner Success degree: Discipline −4 on loser

**Edge D-01: Discipline goes negative — undefined.**
Unit at Discipline 1 takes Discipline −2 (from defender Success). Discipline 1 − 2 = −1. Is the unit destroyed (Discipline ≤ 0 = destroyed) or is Discipline floored at 0?
Drawn battle rule: "Both at Discipline 0: both units destroyed simultaneously." This implies Discipline 0 is a destruction state, not floor. But does taking Discipline −2 at Discipline 1 produce Discipline −1 (floor at 0 = destroyed) or just Discipline 0?
**[PROVISIONAL: Discipline floor is 0. Any result that would push Discipline to ≤ 0 destroys the unit. Negative Discipline does not accumulate.]**

**Edge D-02: Multiple units per territory — undefined.**
A faction with Military 4 can deploy up to 4 units (P-18 cap = Military stat). If 2 units are in one territory during a battle, do they each roll separately or pool? The BG doc's cascade tests treat each territory as one battle pool per faction — the faction's entire Military stat is the pool. But if a faction has units at Discipline 3 and Discipline 1 in the same territory, which Discipline value applies to the pool?
**[PROVISIONAL: Per territory, one roll per faction using that faction's Military stat pool (not individual unit pools). Discipline tracked per individual unit card for purposes of destruction; but the battle roll uses the faction's Military stat. Discipline loss from the battle result is applied to the specific unit involved (player choice which unit absorbs it).]**

**Edge D-03: Unit Muster cap at Military stat (P-18) — interaction with stat changes.**
If Crown's Military drops from 4 to 3 mid-season (from Royal Decree or attribute loss), units above the cap (4th unit) are "immediately removed." What happens to that unit's Discipline? Is the unit destroyed (removed from play) or returned to the Muster pool?
**[PROVISIONAL: Removed units are returned to the faction's reserve (not destroyed). Their Discipline is reset if mustered again. The cap enforces a current-Military ceiling on deployed forces.]**

---

## SIM-DEBT-BG-02: Thread Operations — Mode A + D

### A-06: Thread Operation Pool Construction (BG Mode)

**Canonical procedure (ED-086 / PP-299):**
1. Declare operation type (Weaving, Dissolution, Mending, Past-Pull).
2. Roll faction stat pool (Influence for Varfell, Mandate×½ for other factions? — see gap below).
3. Apply degree result.
4. Draw Co-Movement card.
5. Apply Actualized dimension, then Temporal dimension.

**GAP: Thread operation pool stat for non-Varfell factions.**
- Varfell: Influence confirmed (BG doc Cascade Test 3: "Thread operations use Influence").
- Church: Pontifex card — stat undefined. Is it Mandate (institutional will), Influence (reach), or a fixed pool?
- Restoration: Community Weaving pool now = "1D base + 1D per adjacent territory with RM Presence marker" (PP-460). Confirmed canonical. Range 1–4D based on Presence spread.

**From Cascade Test 1 (Church Overwhelming Decree):** Church's Senator Inward uses Mandate 5 pool. Church Pontifex (Thread operation) — pool not specified in params.
**[PROVISIONAL: Church Thread operations (Pontifex) use Mandate pool. Mandate represents the institutional authority that makes the Church's Thread operations legitimate within the Theocratic framework. Confirmation needed.]**
**[EDITORIAL: ED-339 — Thread operation pool for Church Pontifex and any non-Varfell/non-Restoration faction attempting Thread operations. What stat governs?]**

### A-07: Community Weaving Ob (PP-491 confirmed canonical)

**Formula (confirmed): Ob = ceil((100−RS)/20), min 1, −1 per Presence marker in territory (floor 1).**

| RS | Base Ob | 0 markers | 1 marker | 2 markers | 3+ markers |
|----|---------|-----------|----------|-----------|------------|
| 72–60 | 2 | 2 | 1 | 1 | 1 |
| 59–40 | 3 | 3 | 2 | 1 | 1 |
| 39–20 | 4 | 4 | 3 | 2 | 1 |
| 19–1 | 5 | 5 | 4 | 3 | 2 |

**RM pool = 1D base + 1D per adjacent territory with RM Presence (PP-460). Range 1–4D.**

**Key dynamics:**
- At RS 72 (start) with 1 adjacent marker: Ob 1, pool 2D. P(≥1 net) ≈ 58%. Reasonable early-game tension.
- At RS 40 with 2 adjacent markers: Ob 2, pool 3D. P(≥2 net) ≈ 40%. Difficult but meaningful.
- At RS 20 with 3 adjacent markers: Ob 2, pool 4D. P(≥2 net) ≈ 56%. Manageable if RM has spread.

**Finding F-06:** RM's Community Weaving gets HARDER as RS drops, using MORE dice due to spread. These two forces partially cancel: lower RS raises Ob but RM is incentivised to spread Presence (which adds dice). The system creates a treadmill — RM must expand to keep pace with rising Ob. This is elegant design. RS 40 with 3 markers: Ob 1 (−3 markers from base Ob 4). Pool 4D. P(success) ≈ 85%. The spread requirement is the real gate.

### A-08: Co-Movement Deck Distribution Analysis

**20-card deck (PP-187):**
| Category | Count | Actualized effect |
|----------|-------|-------------------|
| TC effect | 4 | TC +1 |
| RS stabilisation | 3 | RS +1 at next Accounting |
| Faction intel leak | 3 | Operation location revealed to one faction |
| Thread Debt adjacent | 3 | Thread Debt token in adjacent territory |
| History Resonance adjacent | 3 | History Resonance marker in adjacent territory |
| Benign | 4 | No mechanical effect |

**Expected per draw:**
- E(TC per draw) = 4/20 × 1 = 0.20 TC
- E(RS per draw) = 3/20 × 1 = 0.15 RS (at next Accounting)
- P(exposed) = 3/20 = 15%
- P(Thread Debt adjacent) = 3/20 = 15%
- P(benign) = 4/20 = 20%

**At Thread Witness Node (2 draws per operation):**
- E(TC per operation) = 2 × 0.20 = 0.40 TC
- P(at least one intel leak) = 1 − (17/20)² ≈ 27.75%
- P(at least one Thread Debt adjacent) ≈ 27.75%

**Finding F-07: TC generation from Thread operations is significant.**
If Church is the faction performing Thread operations (Pontifex), each operation generates E(TC) = 0.20 per draw. Church with Cardinal Prudence Focus (Wealth +1) never uses Pontifex anyway — but Varfell Thread operations inadvertently generate TC for Church. At VTM 4–5, Varfell may perform 1–2 Thread operations per season, generating 0.20–0.40 expected TC per season from Co-Movement alone. This is unintended TC acceleration that favors Church.

**[EDITORIAL: ED-340 — TC cards in the Co-Movement deck: does the TC +1 benefit Church regardless of who draws it? If yes, Varfell's Thread operations (which serve Varfell's VTM path) simultaneously accelerate Church's primary clock. Is this intentional systemic pressure, or should the TC card be neutral (no clock effect) or faction-conditional?]**

**Finding F-08: P-01 compliance — three-dimensional auto-effects.**
Every Thread operation must produce automatic co-movement across all three dimensions (P-01/P-14). The Co-Movement card covers Actualized + Temporal dimensions. The Epistemic dimension fires automatically (Attention Pool +2 for "unexplained structural change"). This is confirmed in Cascade Test 1.

**P-01 check:** All three dimensions fire on every BG Thread operation via: (1) Co-Movement card draw (Actualized + Temporal), (2) Attention Pool increment (Epistemic). ✓ P-01 compliant in BG mode.

### D-Thread-01: Thread Debt Cascade at High Thread Tension

**Thread Tension (TT) = sum of all History Resonance markers across board.**
- TT ≥ 10: all Thread operation Obs +1 globally.
- TT ≥ 15: Thread Wound formation triggers automatically in any territory with ≥ 2 markers.

**Cascade scenario: Season 8, TT = 12 (above threshold).**
Varfell plays Pontifex T13 (Community Weaving, Ob = ceil(28/20) = 2, RS = 44). Thread Witness Node in T13: draw 2 cards. Draw CM (History Resonance adjacent) and CM (Benign).

- History Resonance adjacent: marker placed in T12 or T6 (adjacent to T13). Assume T12.
- TT was 12. New marker: TT = 13. Still ≥ 10, still ≤ 14.
- T12 check: does T12 have ≥ 2 markers? If yes: Thread Wound. If TT 13 with marker distribution including 2 in T12: Thread Wound forms automatically.

**Thread Wound formation at TT ≥ 15:** This is an automatic cascade — no roll, no faction action required. At TT 15, any territory with ≥ 2 History Resonance markers automatically forms a Thread Wound at Accounting step 6. Thread Wounds are not defined mechanically in the BG params (Thread Wound effects = from TTRPG scale, not yet BG-adapted).

**[GAP: Thread Wound mechanics in BG mode are undefined. The TT ≥ 15 trigger exists in params but the effect (Thread Wound formation) has no BG-specific mechanical consequence. In TTRPG mode, Thread Wounds affect practitioners. In BG mode, there are no individual practitioners. What does Thread Wound formation produce in BG mode? Recommended: RS −1 per Wound formed at Accounting + that territory's Thread operations +1 Ob until Wound is Mended.]**

**[EDITORIAL: ED-341 — BG Thread Wound consequences. When TT ≥ 15 triggers automatic Thread Wound formation in a territory, what are the BG mechanical effects? Suggest: RS −1 per Wound at Accounting + Thread operations in that territory +1 Ob (stacks). Mending (Pontifex action, Ob = existing Wound count) removes one Wound on Success.]**

### D-Thread-02: VTM 5 "Once per game" interaction with session continuity

**VTM 5 ability: "Once per game: choose the Actualized dimension outcome of one Co-Movement card draw."**

If the game spans multiple sessions, the "once per game" tracking requires a physical marker. No tracking mechanism is specified. **[PATCH PP-477: Varfell faction mat includes a "VTM 5 Power Used" marker (flip token). Set to Used when the ability fires. Not reset between sessions. Cleared only if VTM drops below 5 (which is not normally possible — VTM can only increase or hold).]**

### D-Thread-03: Partial Community Weaving and Co-Movement draw

**BG params §Co-Movement Reference (PP-187):** "Draw on: Partial Community Weaving, Niflhel Harvest, VTM preview."
Partial Community Weaving draws a Co-Movement card. But: P-14 requires ALL Thread operations produce three-dimensional co-movement. Does a Partial count as a Thread operation completing?

**Finding:** Partial is a valid degree result from a Thread operation roll. The Thread operation was performed — it just succeeded imperfectly. P-14 applies: the co-movement fires regardless of degree. The existing "Partial Community Weaving → draw Co-Movement card" rule is P-14 compliant. ✓

But the Partial result still places History Resonance marker (Partial Mend per PP-184 cross-reference — Partial or Failed Mend still places History Resonance marker). Does this apply to Community Weaving too? The Partial Mend rule (PP-184) explicitly covers Mend; Community Weaving is not Mend. **[PROVISIONAL: History Resonance marker on Partial applies to Mend only (per PP-184). Community Weaving Partial produces CV −1 (reduced from Success CV −2? Or CV −0.5?) AND Co-Movement draw. No History Resonance marker from Weaving Partial unless the Co-Movement card places one.]**

**[EDITORIAL: ED-342 — Community Weaving degree table: what are the Partial and Failure outcomes for BG Community Weaving? The CV −1 result is stated for Success; the Partial/Failure effects are not defined. Suggest: Overwhelming = CV −2; Success = CV −1; Partial = Co-Movement draw only (no CV change); Failure = no effect, no Co-Movement draw.]**

---

## P1/P2 FINDINGS FROM THIS SIMULATION

### P1 (breaks play)

**P1-06 — Battle Outcome Table Undefined**
No formal table mapping battle degree margins to unit consequences. The cascade test examples imply a table but it is not stated. A GM running the first BG battle has no authoritative reference.
Severity: P1. Frequency: every battle.
Proposed fix: PP-476 (see above).

**P1-07 — Thread Wound BG consequences undefined**
TT ≥ 15 trigger exists but produces no stated BG effect. The mechanic fires into a void.
Severity: P1. Frequency: high-Thread late-game (Season 10+).
Proposed fix: ED-341.

### P2 (bad play experience)

**P2-01 — Fortify stat undefined**
Fortify Ob table exists; pool stat doesn't. Every Fortify action requires GM ruling.
Severity: P2. [PROVISIONAL: Military.]

**P2-02 — Church Pontifex pool undefined**
Thread operation pool for non-Varfell factions not specified. Confirmed gap.
Severity: P2. [EDITORIAL: ED-339.]

**P2-03 — TC cards in Co-Movement benefit Church regardless of drawer**
Varfell Thread operations generate E(0.20) TC per draw — inadvertently accelerating Church primary clock.
Severity: P2. [EDITORIAL: ED-340.]

**P2-04 — Community Weaving degree table incomplete**
Partial and Failure outcomes not defined. Only Success is stated.
Severity: P2. [EDITORIAL: ED-342.]

**P2-05 — Discipline negative interaction**
Discipline can theoretically be driven to negative by high-margin outcomes. Floor rule not stated.
Severity: P2. [PROVISIONAL: floor 0, destruction.]

**P2-06 — Multi-unit territory battle pooling undefined**
If faction has 2 units in one territory, battle pool ambiguous.
Severity: P2. [PROVISIONAL: Military stat pool, player choice for Discipline application.]

### P3 (minor)

**P3-01 — VTM 5 "once per game" needs physical marker**
No tracking mechanism specified. [PATCH PP-477.]

**P3-02 — Partial Community Weaving History Resonance unclear**
Partial Mend rule (PP-184) doesn't clearly extend to Weaving Partial.
Severity: P3. [PROVISIONAL: no History Resonance on Weaving Partial.]

---

## NEW PATCHES

| PP | Scope | Description |
|----|-------|-------------|
| PP-476 | Battle | Formalise Battle Outcome Table — both sides apply degree independently |
| PP-477 | Varfell | VTM 5 "once per game" physical marker (flip token on faction mat) |

## NEW EDITORIALS

| ED | Priority | Description |
|----|---------|-------------|
| ED-338 | P2 | Fortify action pool stat (provisional: Military) |
| ED-339 | P2 | Thread operation pool for Church Pontifex and non-Varfell factions |
| ED-340 | P2 | Co-Movement TC cards — benefit Church regardless of drawer? Intentional? |
| ED-341 | P2 | BG Thread Wound consequences when TT ≥ 15 triggers |
| ED-342 | P2 | Community Weaving degree table — Partial and Failure outcomes |

---

## COVERAGE MATRIX UPDATE

| Mechanic | Mode A | Mode D | Status | Issues |
|----------|--------|--------|--------|--------|
| Battle resolution | ✓ | ✓ | Issues found | P1-06 outcome table undefined |
| Fortification | ✓ | ✓ | Issues found | P2-01 pool stat undefined |
| Thread operations (BG) | ✓ | ✓ | Issues found | P1-07 Thread Wound, P2-02 Pontifex pool, P2-03 TC acceleration |
| Community Weaving | ✓ | ✓ | Issues found | P2-04 degree table incomplete |
| Co-Movement deck | ✓ | ✓ | Issues found | P2-03 TC Church acceleration |
| Discipline track | ✓ | ✓ | Issues found | P2-05 negative floor, P2-06 multi-unit |
| VTM abilities (BG) | — | ✓ | Issues found | P3-01 tracking marker |
| Co-victory pairings | — | — | Not started | SIM-DEBT-BG-03 |
| Faction Unique Actions balance | — | — | Not started | SIM-DEBT-BG-04 |
| Ministry AI | — | — | Not started | SIM-DEBT-BG-05 |
| RS decay 20-season | — | — | Not started | SIM-DEBT-BG-06 |

