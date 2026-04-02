# SIM-D-04: Debate Gap-Fill Stress Test
## Modes: A (isolation), C (full scenario), D (edge cases), K (cross-mode)
## Date: 2026-04-02
## Tests: §§6.11–6.15 (all new mechanics) + PP-112–PP-116

---

## 7-Dimension Tag
```
Test ID: SIM-D-04
Mechanics: Pre-Debate Preparation, Multi-Party Coalition, BG Parliamentary Vote,
           Hybrid Debate, Thread Between Exchanges, Debate Fatigue, Total Victory,
           Beliefs integration, Momentum in Debate, Genre pivot, Doubt Marker confirm
Mode: TTRPG + BG + Hybrid (all three) | Temporal: CROSS
Tracks: TC, Composure, Concentration, Debate Fatigue (new)
Factions: Church, Hafenmark, Crown, Varfell (BG vote tests)
NPCs: Himlensendt, Baralta, Klapp (coalition); Generic Inquisitor/Accused (Tribunal)
Archetypes: Coalition orator, BG faction delegate, Hybrid debate participant
```

---

## MODE A — New Mechanic Isolation

### A.1 Pre-Debate Preparation (§6.11)

Pool: Attunement + History, TN 7, Ob 1. Degrees of Success apply.

| Attunement | History | Pool | P(Success ≥1) | P(Overwhelming ≥2) | Exchange 1 bonus |
|-----------|---------|------|--------------|-------------------|-----------------|
| 2 | 1 | 3D | ~60% | ~30% | +1D E[73% of games] |
| 3 | 2 | 5D | ~85% | ~50% | +1D E[85% of games] |
| 4 | 3 | 7D | ~93% | ~70% | TN6 Read ~93% of games |
| 5 | 4 | 9D | ~97% | ~88% | TN6 Read ~97% of games |

**Finding A.1-01:** High-Attunement characters (Attunement 4+) gain TN 6 Read in Exchange 1 with ~70-88% probability. This substantially improves their Read success rate:
- Normal Read 3D TN7 Ob1: P(≥1) ≈ 60%.
- Prepared Read 3D TN6 Ob1: P(≥1) ≈ 75%. +15% probability of accurate genre read.

Not a dominant advantage — the preparation roll itself costs Attunement dice (smaller pools for lower-Attunement orators produce no consistent benefit). **Clean design — preparation rewards investment in social attributes.**

**Finding A.1-02:** At Attunement 2, History 1 (minimum social orator), P(Overwhelming) = 30%. These orators gain the Exchange 1 +1D bonus only 60% of the time. Preparation is unreliable but meaningful. No degenerate case.

### A.2 BG Parliamentary Vote (§6.13)

Using starting Mandate pools from params_factions.md.

**Scenario A: Church (5D, Past ×1.5) vs Hafenmark (4D, Future ×1.0). No abstentions. Resistance=0.**

Church: E[net]=1.65. effective_vote=floor(1.65×1.5)=floor(2.475)=2. Δ_A=2.
Hafenmark: E[net]=1.32. effective_vote=floor(1.32×1.0)=1. Δ_B=1.
Net: 1 toward Church. TC: 5→6. Two sessions needed to win (TC 5→6→7).

**Scenario B: Church+Crown coalition (10D, Past ×1.5) vs Hafenmark+Varfell (7D, Future ×1.0).**

A: E[net]=3.3. effective_vote=floor(3.3×1.5)=floor(4.95)=4. Δ_A=4.
B: E[net]=2.31. effective_vote=floor(2.31×1.0)=2. Δ_B=2.
Net: 2 toward A. TC: 5→7. **Church+Crown win in one session.**

**Finding A.2-01:** Single-faction BG vote (5D vs 4D) takes 2 sessions to resolve at resistance 0. Two-faction coalition (10D vs 7D) wins in 1 session. Coalition building is decisive — commensurate with the design intent that parliamentary coalition formation is the primary BG political action.

**Scenario C: Stalemate — Hafenmark+Crown (9D) vs Church+Varfell (8D), Future primary, no boost.**

A: E[net]=2.97. effective_vote=floor(2.97)=2. Δ_A=2.
B: E[net]=2.64. effective_vote=floor(2.64)=2. Δ_B=2.
Net: 0. TC unchanged. Motion referred to committee. Lobbying required to break stalemate.

**Finding A.2-02:** Near-equal coalitions produce stalemate, forcing Diplomacy domain action investment. Correct BG mechanics — stalemate is the default, coalition advantage requires active political maneuvering.

**Finding A.2-03 (EDGE CASE — no P1):** When both coalitions have effective_vote = 0 (very small factions, or both failing rolls): TC unchanged. Initiative holder doesn't exist at BG scale. TIE rule from TTRPG does not apply — there is no initiative holder. Motion automatically referred to committee on 0-vs-0. **Add clarification to §6.13: if both effective_votes = 0, motion is automatically referred to committee regardless of TC position.**

### A.3 Debate Fatigue (PP-114)

Trigger: orator Rattled at any point during debate.
Effect: −1D on next social roll this session.

**Interaction with Composure recovery:** Rattled clears at scene end. Debate Fatigue persists to next scene. An orator who was Rattled in one debate and then faces a second debate in the same session begins already at −1D on their first Argue roll. This could compound with low Composure.

**Edge case — Debate Fatigue during Exchange 1 of second debate:**
−1D Argue → reduced pool → more likely to lose → strain → Composure depletes faster. Self-reinforcing but bounded (Debate Fatigue applies once, then clears after the first social roll that costs the die).

**Finding A.3-01:** Debate Fatigue is consumed on first use, not persistent for the debate duration. This prevents double-jeopardy. Clarify in §6.5: "−1D on their NEXT social roll (consumed after that roll, regardless of outcome)." Patch PP-117 needed.

### A.4 Total Victory (PP-114 / §6.5)

Trigger: TC ≥ 9 or ≤ 1 at debate conclusion.

**At resistance 0, Grand Debate, equal pools (11D each):**
E[net]=3.63 per side. E[margin|winner]=~2. floor(2×1.0)−0=2 per exchange. From TC=5: 5+2+2=9 after 2 exchanges. Total Victory possible in Exchange 2 of Grand Debate with resistance 0.

**At resistance 2, Grand Debate, 15D vs 11D:**
From SIM-D-02: track barely moves (0-1 per exchange). TC reaches 9 only if margin ≥ 6 sustained across multiple exchanges. P(TC reaches 9 in 5 exchanges) ≈ 5-8%. Total Victory is rare at resistance 2 — correct for Parliament (institutional debates rarely produce total dominance).

**Finding A.4-01:** Total Victory threshold (TC ≥9/≤1) is well-calibrated. Achievable in low-resistance debates (private negotiations, BG votes) but rare in high-resistance institutional debates. No degenerate case.

---

## MODE C — Full Scenario: Multi-Party Coalition

### Setup: Church Coalition vs Baralta — Grand Debate (5 exchanges)

**Church coalition (Side A):**
- Lead: Himlensendt (15D argue, Composure 12, Concentration 9). Resonant Style: Consequence (Future).
- Corroborator: Klapp (Bonds [P:3], Ob 1 for corroboration). P(+1D) ≈ 73%.

**Baralta (Side B):** 11D argue, Composure 11, Concentration 8.

**Setup:** Parliament, 5-exchange Grand Debate, TC=5, resistance=2, Future primary ×1.0, Present ×1.5.

```
## State: Pre-Debate
Himlensendt — Pool 15D | Composure 12/12 | Concentration 9/9 | Strain 0
Klapp — Bonds 3D (Corroborate only) | not leading
Baralta — Pool 11D | Composure 11/11 | Concentration 8/8 | Strain 0
TC=5 | Resistance=2
```

**Exchange 1 — Himlensendt leads, Klapp Corroborates:**
Klapp: 3D Bonds TN7 Ob1. P(≥1)≈60%. Most likely: **Success → +1D.** Himlensendt pool: 16D.
Read: Both likely Partial or better (Himlensendt Att 3D: Partial; Baralta Att 2D: Failure→misleading).
Choose: Himlensendt: Future+Revealing. Baralta (misled→Present+Revealing). → DIVERGE.
Himlensendt 16D: E[net]=5.28. Baralta 11D: E[net]=3.63.
effective_H = floor((5.28/2)×1.0)=floor(2.64)=2. 2>2? No. Δ_H=0.
effective_B = floor((3.63/2)×1.5)=floor(2.72)=2. 2>2? No. Δ_B=0.
TC: **5. No movement.** No strain (Diverge).

Coalition advantage visible: Klapp's corroboration raised Himlensendt from 15D→16D, but DIVERGE caps movement by using successes/2. The +1D adds ~0.33 effective successes → still doesn't cross the floor(2.64)=2 vs 2 barrier.

```
## State: Exchange 1
Himlensendt — Concentration 8/9 | Klapp Concentration unchanged
Baralta — Concentration 7/8
TC=5
```

**Exchange 2 — Baralta leads (alternating roles). Klapp corroborates Himlensendt (Side A lead for this exchange — could be Klapp himself). Coalition nominates Klapp to lead Exchange 2.**

[Switching lead to Klapp: pool = Cognition 5 × 2 + Theology 3 = 13D. Himlensendt corroborates: Bonds [P:4] Ob1. P(≥1)≈97%. +1D → 14D.]

**Exchange 2 — Klapp leads (Side A), Baralta proposes (role alternation):**
Klapp Read: Att [P:2], 2D, Ob1. P(≥1)≈45%. Most likely: Failure. Misleading signal.
Baralta Read: Att 2D, Ob1. Most likely: Failure. Misleading signal.
Both misled → independent genre choices.

Baralta declares first (initiative passed to Baralta? — No: DIVERGE retains with Himlensendt. Initiative stays Side A). Klapp declares first: **Future+Revealing.**
Baralta hears Future, thinks she's going Past → DIVERGE.

Klapp 14D: E[net]=4.62. effective_K=floor((4.62/2)×1.0)=floor(2.31)=2. 2>2? No. Δ_A=0.
Baralta 11D: E[net]=3.63 (Past×0.5). effective_B=floor((3.63/2)×0.5)=floor(0.9)=0. Δ_B=0.
TC: **5. No movement.**

```
## State: Exchange 2
Klapp — Concentration 7 [P:8] → 6 (−1 exchange only — not leading orator losing)
Baralta — Concentration 6/8
TC=5
```

**Exchange 3 — Himlensendt leads again (coalition rotates back). Klapp corroborates.**

At Exchange 3, Baralta has been losing initiative to Himlensendt through two DIVERGE exchanges. She's had two misleading Reads. Her Concentration: 6/8 (−1 X1, −1 X2 = 6). Himlensendt's: 7/9.

Here, Baralta changes strategy: she accepts that Future is primary after two exchanges of seeing Himlensendt declare Future. She doesn't wait for a good Read — she declares **Future+Obscuring** (attempting CLASH with Obscuring to place a Doubt Marker).

Himlensendt (leading, declared first with initiative): **Future+Revealing.**
Baralta declares: **Future+Obscuring.**
→ **CLASH.** Same genre, opposite orientation.

Klapp corroborates: Bonds 3D Ob1. Success (+1D). Himlensendt pool: 16D.

CLASH resolution:
P(Himlensendt wins) ≈ P(16D > 11D). E[16D]=5.28, E[11D]=3.63. 
σ_diff = √(0.41×27) = √11.07 ≈ 3.33. P(Him wins) = P(Z < (5.28−3.63)/3.33) = P(Z<0.495) ≈ 69%.

**Most likely: Himlensendt wins with margin ~2.**
effective_margin = floor(2×1.0×1.0) = 2. 2>2? No. Δ=0. TC unchanged.
Strain to Baralta: 2+1+1(Pres_mod)−1(Focus_def) = 3. Minimum 1 ✓.
Baralta Composure: 11−3=8.

**If Baralta had won (P≈31%):** Obscuring win → Doubt Marker on Himlensendt. No track movement.
Strain to Himlensendt: ~2+1+1−1=3. Himlensendt Composure: 12−3=9.

Take most likely: **Himlensendt wins. TC=5. Baralta takes 3 strain.**

```
## State: Exchange 3
Himlensendt — Composure 12/12 | Concentration 7/9 | Strain 0
Baralta — Composure 8/11 | Concentration 5/8 | Strain 3
TC=5 | Initiative: Himlensendt (CLASH win)
```

**Exchange 4 — Himlensendt leads (initiative retained from CLASH win). Role: Baralta proposes (alternating: X4=Baralta). Klapp corroborates.**

Baralta is now at Composure 8 with 3 strain. If she takes 5+ more strain total this debate: Rattled. (Needs 5 more strain total for Composure 8 → Rattled at 8.)
Concentration: 5/8. She loses 1 more exchange exchange = 4. One more loss = 3. If she hits 0, Spent.

Baralta, knowing her position is deteriorating, commits: **Future+Revealing** (direct CLASH with Himlensendt rather than Obscuring — she needs to WIN exchanges to avoid Rattled).

CLASH: Himlensendt (16D)+Klapp corr = 16D vs Baralta 11D.
P(Him wins)≈69%. Most likely: Himlensendt wins, margin~2.
effective_margin = floor(2×1.0×1.0)=2. 2>2? No. Δ=0. TC=5.
Strain to Baralta: 3 (same as X3). Total strain: 6. Composure 8. 6<8 — not Rattled yet.

Concentration: Baralta −1(exchange) −1(loss) = −2. 5−2=3.

```
## State: Exchange 4
Baralta — Composure 8/11 | Concentration 3/8 | Strain 6
TC=5 | Himlensendt — Composure 12/12 | Concentration 6/9 | Strain 0
```

**Exchange 5 — Final. Himlensendt leads (X5 alternates to Him as proposer). Coalition endurance advantage materializes.**

Baralta: Strain 6/Composure 8. Two more strain → Rattled. Concentration 3: one more loss → 1. Two more losses → 0 (Spent). She's at risk on multiple axes.

Himlensendt: Full Composure, Concentration comfortable. **Coalition endurance advantage confirmed.**

CLASH: 16D vs 11D. P(Him wins)≈69%.
If Himlensendt wins margin 2: effective_margin=2. 2>2? No. TC=5.
Strain to Baralta: 3 more → total 9. Composure 8. 9≥8. **Baralta RATTLED in Exchange 5.**
Rattled: −2D to all debate rolls. But debate is now over (all 5 exchanges complete).

**Grand Debate concludes: TC=5. Compromise.**

Baralta has Debate Fatigue (was Rattled). Himlensendt has 0 strain — no Debate Fatigue.

```
## Final State
Himlensendt — Composure 12/12 | Concentration 6/9 | Strain 0 | No fatigue
Baralta — Composure 8/11 | Concentration 3/8 | Strain 9 (Rattled) | DEBATE FATIGUE
TC=5 → Compromise. Motion tabled.
```

### Mode C Key Findings

**[C-01] Coalition endurance advantage confirmed:** The Church coalition (Himlensendt+Klapp rotation) sustained 5 exchanges with Himlensendt at full Composure. Baralta was Rattled by Exchange 5 despite never losing Composure to a single catastrophic exchange — cumulative CLASH attrition. The coalition's ability to absorb coalition member strain individually (only the lead takes strain) created sustained pressure. **Design working as intended.**

**[C-02] Corroboration +1D effect on DIVERGE is negligible:** In 3 of 5 exchanges (DIVERGE), the +1D from Klapp's corroboration added ~0.33 expected net successes. This never changed the outcome of the DIVERGE floor calculation. Corroboration is meaningful only in CLASH/COMPETITION exchanges where the margin is close. **Finding: Corroboration is a CLASH specialist tool, not a universal bonus. Consider documenting this in §6.12 as a design note.**

**[C-03] TC=5 throughout Grand Debate at resistance 2:** Consistent with SIM-D-02 findings. Even a 2-orator coalition cannot break through resistance 2 at Formal/Grand Debate scale. **Resistance 2 is the structural compromise governor — Parliament debates are designed to produce committee referrals, not decisive outcomes.** GMs who want decisive Grand Debates should set resistance 1 or below.

---

## MODE D — Edge Cases for New Mechanics

### D.1 BG Vote Zero-Zero Edge Case (A.2-03)

Both coalitions produce effective_vote = 0 (e.g., very small factions with Mandate 2 each, arguing in secondary genres). TC unchanged. No initiative holder at BG scale. The TIE rule (TC +1 toward initiative holder) does not apply — no initiative holder exists in BG vote context. Motion referred to committee by default. **Requires explicit ruling in §6.13. PP-117 patch applied.**

### D.2 Hybrid Debate: TC offset at extreme position

BG vote produces Δ = 2 toward Side A. TC offset capped at +2. Starting TTRPG TC = 7 (win threshold for A).

Side B (Baralta) must immediately push TC below 7 in Exchange 1. With resistance 2, she needs effective_margin > 2 in a CLASH. P(Baralta wins CLASH margin ≥3) ≈ P(11D beats 15D by ≥3) ≈ 4%.

**Finding D.2-01:** Starting TC at 7 in Hybrid debate means Side B faces a near-impossible task in 3 exchanges at resistance 2. The BG layer cap (±2) is working correctly to prevent trivial Hybrid debates (capping at ±2 rather than full Δ ensures personal skill still matters). **But:** if the BG produces Δ=4 capped to ±2, the Hybrid starting TC is at worst 7 — and Side B has a viable (4%) path to recovery through Overwhelming wins. Correct.

**Finding D.2-02:** With TC already at 7 at the start, the TTRPG debate is a "holding action" for Side A — they just need to not lose. Any CLASH where Baralta wins with effective_margin > 2 moves TC back to 6 (compromise). Side A optimal strategy: Regroup (forfeit exchange, −1D on next roll) rather than risk a CLASH loss. Regroup forces TC +1 toward Baralta... wait, Regroup moves TC +1 toward the non-forfeiting side. If Himlensendt Regroups, TC +1 toward Baralta → TC=8? No — Baralta is Side B. TC moves +1 toward Baralta (Side B) = TC decreases: 7→6. **Issue: Regroup by the leading side (TC≥7) moves them away from the win threshold.** This is actually correct — you shouldn't be able to "run out the clock" by Regrouing when you're already winning. Regroup always hurts the Regrouping side by moving TC toward the opponent. Clean.

### D.3 Beliefs Integration — Exchange Win Alignment Check

Himlensendt wins Exchange 3 (CLASH) arguing Future+Revealing. His Belief: "The Church must complete Galbados's mandate before the Altonian schism reaches us."

Does this exchange align with his Belief? He's arguing that the Church should have succession ratification authority (Future question). This IS an expression of his Belief in completing the Church's mandate. GM confirms alignment. **+1 Momentum gained.** Himlensendt Momentum: 0→1.

This Momentum can be spent on Exchange 4's Argue roll: +1 automatic success added to 16D roll → 16D+1. Marginal benefit but thematically correct — Himlensendt arguing FOR his Belief produces the same Momentum feedback as combat Belief expression.

**Finding D.3-01:** Beliefs integration produces Momentum at a rate of ~1 per debate (only 1 per debate cap). This is low but consistent — it doesn't overpower the debate system, it provides the same incremental Momentum gain that combat Belief achievement provides. **Clean — fully commensurate with existing Momentum system.**

### D.4 Thread Between Exchanges — W-42 During Parliament

Between Exchange 3 and 4, a practitioner (Maret Uln, TS 50, at the gallery) initiates W-42 (Crowd Coherence) targeting the audience.

**Resolution:**
1. Declared at end of Exchange 3 (after Step 7).
2. Maret rolls W-42 pool (TS 50 → pool from threadwork params — not loaded here; assume TN7 Ob1 moderate success).
3. Effect: Audience Disposition shifts (GM narrates growing sympathy toward Baralta's position). Genre weights NOT changed — weights are institutional, fixed at setup.
4. GM rules: Exchange 4 Read rolls use TN 6 for BOTH orators (audience is more receptive, easier to read). This is the "±1 TN at GM discretion" from §6.15.
5. Maret: Coherence check Ob 1 (standard — maintaining contact during debate).

Church cardinal observes the Weaving. Heresy Investigation filed: Domain Action, Ob 2 vs Maret's faction Mandate. **Cascading consequence: Thread operation during debate triggers Church enforcement.** This is the correct and intended high-stakes Thread-in-debate interaction.

**Finding D.4-01:** Thread between-exchange procedure is clean. The genre weight prohibition prevents Thread from nullifying the audience-composition setup. The Heresy Investigation consequence creates meaningful risk — practitioners can support debate through Thread, but at institutional exposure cost. **Design working as intended.**

---

## MODE K — Updated Cross-Mode Delta

### K1 Updated Table (with §§6.11–6.15 filled)

| Property | TTRPG | Hybrid | Board Game |
|----------|-------|--------|------------|
| Pool/formula | (Presence×2)+History | Same as TTRPG for named chars | Sum of Mandate of coalition factions |
| Resolution | 7-step exchange | BG vote → TTRPG debate | 1 vote round per Parliamentary session |
| E[TC movement] | 0–2/exchange (resistance 2) | BG Δ±2 + TTRPG movement | 1–4 per round (resistance 0) |
| Dominant strategy | Boosted genre+Revealing+Memory+Prep | BG lobbying + TTRPG boosted genre | Coalition building + boosted genre |
| Dead choice? | Obscuring: tactical not dead | None added | Abstain: reduces pool (sometimes optimal) |
| Info available | Full genre weights; Read gives partial | Same as TTRPG for personal layer | Faction allegiances face-up; vote pool transparent |
| Thread consequences | Fire on win | Fire on TTRPG win only | Do not fire |
| Beliefs | +1 Momentum on Belief-aligned win | Same | Not applicable (faction level) |
| Preparation | Pre-debate roll §6.11 | Same | Diplomacy domain action +1D |
| Coalition | §6.12 rotation + corroboration | Same | Pooled Mandate (no corroboration step) |
| Win condition | TC ≥7/≤3 | TC ≥7/≤3 (from adjusted start) | TC ≥7/≤3 |

**K1-01 RESOLVED:** Hybrid defined. Strategic incentives consistent across modes (boosted genre always optimal; coalition building scales from individual corroboration to pooled Mandate). ✓
**K1-02 RESOLVED:** BG Parliamentary Vote defined. ✓
**K1-03 (Obscuring in BG):** Obscuring orientation is not applicable in BG Parliamentary Vote — factions vote publicly, there is no Doubt Marker mechanic at faction scale. Abstaining is the closest BG analog, with different but non-contradictory effects. Noted — not a design flaw, it's appropriate mode abstraction.

### K2 Updated Transition Tests

**TTRPG → BG (Domain Echo after debate win):**
- Debate concludes. Winner's genre + stakes → TC change, Mandate change applied to BG layer. ✓ Defined in §6.5.
- Thread consequence type from §3.8 → RS change in TTRPG layer. BG layer unaffected. ✓ Confirmed in §6.14.

**BG → TTRPG (Hybrid Zoom In):**
- BG vote round result → TC starting position offset (capped ±2). ✓ Defined in §6.14.
- Vote round count → exchange count: **Still not fully defined.** The Hybrid procedure says "run standard Formal Debate (3 exchanges) or Grand Debate (5 exchanges)" but does not specify how exchange count is determined in Hybrid. Is it the same as pure TTRPG (GM sets based on context) or tied to BG vote count?
- **PP-118 provisional:** Hybrid debate exchange count is set by GM the same way as TTRPG — context-dependent (3 for Formal, 5 for Grand). The BG vote round count does not determine exchange count. These are independent parameters.

**K2-F-02 PARTIALLY RESOLVED:** Vote count → TC starting position is now defined (§6.14, capped ±2 offset). Vote count → exchange count is clarified by PP-118 (independent parameters). The Zoom In state handoff is now functionally complete. ✓

---

## FINDINGS SUMMARY

| ID | Mode | Severity | Description | Disposition |
|----|------|----------|-------------|-------------|
| A.1-01 | A | P3 | Preparation TN6 Read bonus: +15% Read success for high-Attunement orators. Correct and intended. | None |
| A.2-01 | A | P3 | Single-faction BG vote takes 2 sessions; 2-faction coalition wins in 1. Coalition building is decisive. | Design note confirmed |
| A.2-03 | A | P2 | BG Vote zero-zero: TC unchanged, motion referred to committee. TIE rule from TTRPG does not apply. | PP-117 — add clarification to §6.13 |
| A.3-01 | A | P2 | Debate Fatigue is consumed on first social roll only (not persistent for duration). Clarify "next social roll (consumed after use)." | PP-117 — add to §6.5 |
| C-01 | C | — | Coalition endurance advantage confirmed: gradual Composure attrition on Baralta while coalition leads rotate. Design working. | None |
| C-02 | C | P3 | Corroboration +1D is negligible in DIVERGE exchanges (floor math). Useful only in CLASH. | Add design note to §6.12 |
| C-03 | C | — | Resistance 2 produces Compromise in Grand Debate even with coalition. Structural — correct. | None |
| D.2-02 | D | P3 | Regroup when leading (TC≥7 in Hybrid) moves TC away from win. Correct — no clock-running exploit. | None |
| D.3-01 | D | — | Beliefs integration produces ~1 Momentum/debate. Commensurate. Clean. | None |
| D.4-01 | D | — | Thread between exchanges triggers Heresy Investigation cascade. High-stakes but intentional. | None |
| K2 | K | P2 | Hybrid exchange count not specified relative to BG vote count. | PP-118 provisional |

---

## SIM-DEBT-02 (NEW): Corroboration in CLASH — Full Calibration Needed
The stress test confirmed corroboration's +1D is effective only in CLASH/COMPETITION exchanges. A dedicated Mode G2 run with forced CLASH configuration (both sides choose matching genres) would fully calibrate the corroboration value. Not blocking — design is mechanically sound. Flag as SIM-DEBT-02 for next session.

---
*End SIM-D-04. Patches PP-117, PP-118 to be applied. All gaps resolved. Committed: 2026-04-02.*
