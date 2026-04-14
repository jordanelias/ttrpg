# Valoria Simulation — SIM-DEBT-SOC-01, SOC-02, SOC-03 + ED-519
**Date:** 2026-04-13
**Modes:** A (isolation) + D (edge cases)
**System:** Fieldwork Socializing §5 (PP-632): Disposition, Knot Formation, Knot Breaking
**ED-519:** Resonant Style +1D stacking (Social Contest)
**Runs:** 50,000 per probability cell

---

## FETCH LOG
- references/params_core.md: ✓ 213 lines
- references/params_threadwork.md: ✓ 900 lines
- references/params_contest.md: ✓ 267 lines
- designs/fieldwork/fieldwork_socializing.md: ✓ 190 lines
- canon/02_canon_constraints.md: ✓ 25 lines (fetched earlier session)

---

## SIM-DEBT-SOC-01: Disposition Ob Calibration

### Mechanic under test
`Effective Ob = max(1, base_Ob − Disposition)` applied to social fieldwork actions.
Connect: base Ob 3, pool = (Bonds×2)+3.
Converse: base Ob 2, pool = (Cha×2)+3.

### Connect results (base Ob 3)

| Bonds | Pool | Disp | Eff Ob | P(OW) | P(Su) | P(Pa) | P(Fa) |
|-------|------|------|--------|-------|-------|-------|-------|
| 2 | 7D | −2 | 5 | 0.1% | 21.0% | 65.2% | 13.7% |
| 2 | 7D | −1 | 4 | 1.5% | 34.8% | 50.2% | 13.5% |
| 2 | 7D | 0 | 3 | 10.4% | 44.3% | 31.7% | 13.6% |
| 2 | 7D | +1 | 2 | 35.9% | 36.8% | 13.4% | 13.9% |
| 2 | 7D | +2 | 1 | 54.5% | 31.6% | 0.0% | 13.9% |
| 3 | 9D | 0 | 3 | 21.4% | 45.6% | 23.7% | 9.4% |
| 3 | 9D | +1 | 2 | 50.9% | 30.2% | 9.5% | 9.4% |
| 3 | 9D | +2 | 1 | 67.0% | 23.3% | 0.0% | 9.7% |
| 5 | 13D | 0 | 3 | 44.9% | 37.6% | 12.8% | 4.7% |
| 5 | 13D | +1 | 2 | 71.7% | 18.5% | 4.9% | 4.8% |
| 7 | 17D | 0 | 3 | 65.2% | 25.6% | 6.7% | 2.5% |
| 7 | 17D | −2 | 5 | 20.5% | 55.1% | 21.9% | 2.5% |

### Converse results (base Ob 2)

| Cha | Pool | Disp | Eff Ob | P(OW) | P(Su) | P(Pa) | P(Fa) |
|-----|------|------|--------|-------|-------|-------|-------|
| 3 | 9D | −1 | 3 | 21.4% | 45.5% | 23.4% | 9.6% |
| 3 | 9D | 0 | 2 | 50.7% | 30.1% | 9.7% | 9.5% |
| 3 | 9D | +1 | 1 | 67.4% | 23.1% | 0.0% | 9.5% |
| 4 | 11D | 0 | 2 | 62.5% | 23.9% | 6.9% | 6.7% |
| 5 | 13D | 0 | 2 | 72.1% | 18.2% | 4.8% | 4.9% |

### Findings

**SOC-01-F01 [CLEAN]:** Disposition direct-subtraction Ob rule is well-calibrated. At the design midpoint (Bonds 3, Disposition 0, Connect Ob 3): 21% OW / 46% Su / 24% Pa / 9% Fa — this is a meaningful roll with all four outcomes reachable. No auto-success or auto-fail pathology.

**SOC-01-F02 [CLEAN]:** The Disposition +2 → Ob 1 floor produces a probability plateau: Disposition +2 and +3 are statistically identical (67.0% vs 66.7% OW at Bonds 3). This is expected and appropriate — Ob 1 is the floor by design (PP-232). The plateau is not a flaw; it correctly represents that above-Friendly relationships don't make rolls trivial, they just remove Partial as an outcome.

**SOC-01-F03 [CLEAN]:** Negative Disposition creates meaningful difficulty without hard blocking. At Bonds 3, Disposition −2 (Ob 5): 0.8% OW / 34% Su / 56% Pa / 9% Fa. The character can succeed but it takes time. Failure rate stays constant (~9-14%) because it's driven by 1s in pool, not Ob level — this is correct die mechanic behaviour.

**SOC-01-F04 [CLEAN]:** Converse (Ob 2) is easier than Connect (Ob 3) as designed — Converse at Disposition 0 hits 50-72% OW depending on Cha, making it a reliable Disposition-building tool across 1-2 scenes. Connect is the riskier investment, correctly reserved for deeper relationship formation.

**SOC-01-F05 [GAP — non-blocking]:** Disposition ≤ −3 recovery condition ("requires a significant narrative event before social actions can be attempted") has no mechanical definition of what constitutes a qualifying event. This is an editorial gate, not a calibration gap. Log as ED-new.

**VERDICT: SOC-01 CLEAN. Ob calibration sound.**

---

## SIM-DEBT-SOC-02: Knot Formation Pacing

### Mechanic under test
Connect roll to form Knot of target tier. Pool = (Bonds×2)+3. Ob = tier cost − Disposition (floor 1). 2 Connect actions per season assumed.

### Results

| Bonds | Tier | Disp Start | Median Seasons | P(≤2 seasons) | P(≤4 seasons) |
|-------|------|-----------|---------------|--------------|--------------|
| 3 | Loose | 0 | 1.0 | 99.8% | 99.9% |
| 3 | Medium | 0 | 1.0 | 99.4% | 100.0% |
| 3 | Close | 0 | 1.0 | 78.5% | 91.9% |
| 3 | Close | +1 | 1.0 | 91.1% | 98.1% |
| 3 | Close | +2 | 1.0 | 97.5% | 99.6% |
| 5 | Close | 0 | 1.0 | 96.6% | 99.7% |
| 7 | Close | 0 | 1.0 | 99.4% | 100.0% |

### Findings

**SOC-02-F01 [P1 — DESIGN GAP]:** Loose and Medium Knots form trivially fast — near-certain within one season at any Disposition ≥ 0. At Bonds 3, Disposition 0: Loose/Medium form in 1 season with 99%+ probability. This removes any mechanical cost or pacing from forming non-Close Knots. If the design intent is that Loose and Medium Knots represent casual/friendly bonds formed quickly, this is fine. If they are meant to represent investment, the Ob is too low.

**SOC-02-F02 [CLEAN]:** Close Knot formation (Ob 5) provides genuine pacing tension at low Disposition. At Bonds 3, Disposition 0 (Ob 5): 78.5% within 2 seasons, 91.9% within 4. A player must invest 2-3 Connect actions over 1-2 seasons to reliably form a Close Knot without Disposition preparation — this is meaningful investment.

**SOC-02-F03 [CLEAN]:** Disposition preparation before attempting Close Knot formation significantly improves speed. Disposition +2 before Connect attempt (Ob 3): 97.5% within 2 seasons vs 78.5% at Disposition 0. This correctly incentivises the Converse→Connect pathway.

**SOC-02-F04 [DESIGN NOTE — editorial]:** The max Knot count cap (floor(Bonds/2)+1) is the meaningful constraint on Knot accumulation, not formation pacing. A Bonds 3 character can hold max 2 Knots. The difficulty in Knot economy is opportunity cost and the Close tier's formation difficulty, not Loose/Medium. [EDITORIAL: ED-new — clarify whether Loose/Medium Knot trivial formation is intended design (casual bonds) or a calibration gap requiring Ob adjustment.]

**VERDICT: SOC-02 PARTIALLY CLEAN. Close Knot pacing correct. Loose/Medium formation rate requires editorial intent confirmation.**

---

## SIM-DEBT-SOC-03: Knot Breaking Composure Damage

### Mechanic under test
Rupture: Disposition →−4 + Composure damage = tier cost.
Loss: Coherence −1 + Composure damage = tier cost.
Composure = Charisma + 6 (range 7–13).

### Single Knot break results

| Tier | Cost | Cha | Composure | Rupture % | Status |
|------|------|-----|-----------|-----------|--------|
| Loose | 1 | 2–6 | 8–12 | 8–13% | OK |
| Medium | 2 | 2–6 | 8–12 | 17–25% | OK |
| Close | 5 | 2 | 8 | 62.5% | **HIGH** |
| Close | 5 | 3 | 9 | 55.6% | **HIGH** |
| Close | 5 | 5 | 11 | 45.5% | Manageable |

### Simultaneous Knot break results (all Close Knots rupture)

| Bonds | Cha | Max Close Knots | Total Damage | Composure | Verdict |
|-------|-----|----------------|-------------|-----------|---------|
| 3 | 3 | 2 | 10 | 9 | **CATASTROPHIC** |
| 3 | 5 | 2 | 10 | 11 | Survivable |
| 5 | 3 | 3 | 15 | 9 | **CATASTROPHIC** |
| 5 | 5 | 3 | 15 | 11 | **CATASTROPHIC** |
| 7 | 3 | 4 | 20 | 9 | **CATASTROPHIC** |
| 7 | 5 | 4 | 20 | 11 | **CATASTROPHIC** |
| 7 | 7 | 4 | 20 | 13 | **CATASTROPHIC** |

### Findings

**SOC-03-F01 [CLEAN — single break]:** Single Close Knot Rupture (5 damage) is calibrated to be severe but survivable for most characters. Cha 3 (Composure 9): 56% of Composure — rattled but functional. Cha 5 (Composure 11): 45% — significant but recoverable. This matches intended weight of Close Knot loss as a campaign-altering event.

**SOC-03-F02 [P1 — EDGE CASE]:** Simultaneous Rupture of all Close Knots is catastrophic for nearly all character builds. A Bonds 7 character with 4 Close Knots suffers 20 Composure damage. Even Cha 7 (Composure 13) cannot survive this. This state is reachable: any scene that collapses multiple relationships simultaneously (betrayal revelation, mass casualty event, social catastrophe) can trigger all Knots rupturing at once. **No rule caps simultaneous Knot break damage.** A character optimised for Bonds can be rendered permanently incapacitated by a single narrative event.

**SOC-03-F03 [P2 — edge case]:** The simultaneous break scenario requires editorial ruling: is stacked Knot Rupture intended to be potentially catastrophic (representing the mechanics of relational devastation), or should there be a per-scene Composure damage cap? At Bonds 5, Cha 3, all Close Knots rupturing: 15 damage vs 9 Composure. Incapacitated and then some. [EDITORIAL: ED-new — simultaneous Knot Rupture cap or confirmation that catastrophic stacking is intended.]

**SOC-03-F04 [CLEAN]:** Loss (not Rupture) adds Coherence −1 as a separate track penalty. For non-practitioners this is meaningless (Coherence is a practitioner stat). For practitioners: losing a Close Knot to Loss costs 5 Composure damage AND 1 Coherence. At Coherence 5 or lower this is significant pressure. The interaction is intentional and not degenerate.

**VERDICT: SOC-03 has one P1 edge case (simultaneous Rupture stack) and one P2. Single break calibration is sound.**

---

## ED-519: Resonant Style +1D Stacking Validation

### Mechanic under test
Contest bonus dice sources that may apply to a single exchange:
- Genre match: +1D (primary genre matches GM-set primary genre)
- Audience boost: +1D (orator's genre or orientation matches faction boost axis)
- Resonant Style: +1D (argument style matches NPC's Resonant Style)
- Corroborate: +1D (Bonds ≥ 3 symmetric, on success)

Question: can all four sources stack? If so, is the result degenerate?

### Pool impact at Ob 3 (contested)

| Base Pool | +0D | +1D | +2D | +3D |
|-----------|-----|-----|-----|-----|
| 11D (Cha 4) | OW 33% | OW 39% | OW 45% | OW 50% |
| 13D (Cha 5) | OW 45% | OW 51% | OW 56% | OW 61% |
| 15D (Cha 6) | OW 56% | OW 61% | OW 65% | OW 69% |

### Findings

**ED-519-F01 [CLEAN — stacking not degenerate]:** Each +1D bonus contributes approximately 5–6 percentage points to P(OW) at Ob 3. Full stack of +3D raises P(OW) from 33% to 50% at pool 11D — meaningful but not automatic. Even at pool 15D with +3D (68.7% OW), the opponent can still succeed and track movement is contested. No degenerate outcome.

**ED-519-F02 [DESIGN CLARIFICATION NEEDED]:** The four bonus sources are mechanically distinct but their simultaneous applicability to a single exchange needs explicit ruling:
- **Genre match** (+1D) and **Audience boost** (+1D): these can both apply in the same exchange (matching both genre and orientation). This is already canonical (params_contest.md: "Maximum combined: +2D").
- **Resonant Style** (+1D): applies when argument style matches NPC's Resonant Style. This is a third source on top of genre+audience. The design doc does not cap this stack explicitly.
- **Corroborate** (+1D): conditional on Bonds ≥ 3 and success — this is a post-roll bonus, applying only when the Argue roll succeeds. Mechanically this is a separate resolution step.

**ED-519-F03 [RULING REQUIRED]:** The question is whether Genre+Audience (+2D max per params_contest.md) also caps Resonant Style. If Resonant Style is a fourth independent source, maximum stack is +3D. If it counts toward the +2D cap, max is +2D (either Genre+RS or Audience+RS but not all three simultaneously). Corroborate is post-roll and clearly independent.

**Current params_contest.md cap text:** "Maximum combined: +2D" — this refers to Genre+Audience only. Resonant Style is defined in npc_behavior_v30.md, not params_contest.md, and has no stated cap interaction. **The sources are currently uncapped in combination.**

**ED-519-F04 [PROVISIONAL RULING — for Jordan confirmation]:** +3D total (Genre+RS+Audience, or any combination to max +3D, plus Corroborate post-roll) is not degenerate at any tested pool size. P(OW) peaks at ~69% for elite characters in ideal conditions — this is strong but not automatic, and the opponent is also rolling. **[PROVISIONAL: Allow full stack as-is. Resonant Style +1D does not count toward the Genre+Audience +2D cap — it is a third independent source. Document explicitly in params_contest.md.]**

**VERDICT: ED-519 — stacking not degenerate. Provisional ruling: allow full stack. Requires explicit documentation in params_contest.md and Jordan confirmation on intent.**

---

## Summary of Findings

| ID | Priority | Status | Finding |
|----|----------|--------|---------|
| SOC-01-F01 | — | CLEAN | Disposition Ob calibration sound |
| SOC-01-F02 | — | CLEAN | Ob floor plateau expected and correct |
| SOC-01-F03 | — | CLEAN | Negative Disposition creates difficulty without hard block |
| SOC-01-F04 | — | CLEAN | Converse vs Connect Ob differential correct |
| SOC-01-F05 | P3 | GAP | Disposition ≤ −3 recovery has no mechanical definition → ED-new |
| SOC-02-F01 | P2 | DESIGN GAP | Loose/Medium Knot formation trivially fast — editorial confirmation needed → ED-new |
| SOC-02-F02 | — | CLEAN | Close Knot pacing correct |
| SOC-02-F03 | — | CLEAN | Disposition preparation incentivised correctly |
| SOC-02-F04 | P3 | EDITORIAL | Loose/Medium trivial formation may be intended design — confirm → ED-new |
| SOC-03-F01 | — | CLEAN | Single Close Knot break calibrated correctly |
| SOC-03-F02 | **P1** | EDGE CASE | Simultaneous Rupture of all Close Knots → catastrophic at nearly all builds. No cap rule. |
| SOC-03-F03 | P2 | EDITORIAL | Simultaneous Rupture cap needed or intent confirmation → ED-new |
| SOC-03-F04 | — | CLEAN | Loss + Coherence −1 interaction not degenerate |
| ED-519-F01 | — | CLEAN | RS +1D stacking not degenerate |
| ED-519-F02 | P2 | DESIGN | Four bonus sources can stack; cap rule not explicit |
| ED-519-F03 | P2 | RULING | Genre+Audience cap (params_contest.md) does not cover RS — uncapped combination |
| ED-519-F04 | — | PROVISIONAL | Full +3D stack allowed. RS is third independent source. Document in params_contest.md. |

**P1 count: 1 (SOC-03-F02 — simultaneous Rupture stack)**
**P2 count: 3**
**P3 count: 2**
**Provisional rulings: 1 (ED-519-F04 — Jordan confirmation required)**
