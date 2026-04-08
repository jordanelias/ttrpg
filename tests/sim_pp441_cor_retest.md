# SIM-PP-441-COR — Counter-Narrative Corrected Retest
## Date: 2026-04-07 | Mode: A (Isolation) + B (Interaction Chain)
## Source: PP-441-COR — Overwhelming = TC −0.5 + AP +2; Success = AP +2 only

---

## FETCH LOG
canonical_sources.yaml: ✓ fetched (156 lines)
references/params_board_game.md: ✓ fetched (1068 lines)
references/params_factions.md: ✓ fetched (480 lines)

---

## System Under Test

**PP-441 (corrected by PP-441-COR):**
Counter-Narrative (Tribune Outward, Varfell only). Target = Church-held or Church-prominent territory.
Roll: Intel vs Ob = Church Mandate ÷ 2 round up, min 1. Consequentialism −1 Ob.

| Degree | Effect |
|--------|--------|
| Overwhelming | TC −0.5 + AP +2 in territory |
| Success | AP +2 in territory (no TC effect) |
| Partial | AP +1 |
| Failure | Network exposed (Church notified, AP +1 tagged as Varfell) |

---

## Mode A: Counter-Narrative Isolation

### Input Space
- Varfell Intel: 4 (starting), max 7
- Church Mandate: 5 (starting), max 7
- Ob = Church Mandate ÷ 2 round up = 3 (standard), 4 (max Church Mandate)
- Consequentialism −1 Ob → Ob 2 (standard), Ob 3 (max Church Mandate)

### Probability Table (Varfell Intel 4D, Tribune = Intel-class action)

| Pool | Ob | P(OW) | P(Succ) | P(Partial) | P(Fail) |
|------|----|-------|---------|------------|---------|
| 4D | 2 | ~27% | ~29% | ~31% | ~13% |
| 4D | 3 | ~8% | ~34% | ~38% | ~20% |
| 5D | 2 | ~42% | ~28% | ~22% | ~8% |
| 5D | 3 | ~15% | ~35% | ~33% | ~17% |

### TC Effect Analysis

At Ob 2 (Intel 4, Church M 4, Consequentialism modifier applied):
- Expected TC per use: (0.27 × −0.5) + (0.29 × 0) + (0.31 × 0) + (0.13 × 0) = **−0.135 TC expected per use**

At Ob 3 (Intel 4, Church M 5–6):
- Expected TC: (0.08 × −0.5) = **−0.04 TC expected per use**

**Comparison with prior PP-441 (before correction):**
Old: Overwhelming = TC −1; Success = TC −0.5
Old expected TC at Ob 2: (0.27 × −1) + (0.29 × −0.5) = −0.27 − 0.145 = **−0.415 TC/use**
New: **−0.135 TC/use** — reduced by 67%.

**Finding:** Counter-Narrative is now predominantly an Attention Pool (AP) tool, not a TC suppressor. TC reduction is a meaningful but rare bonus (Overwhelming only). This correctly repositions the mechanic: Varfell weakens the Church's territorial infrastructure, with occasional strategic TC dents on excellent rolls.

### AP Effect Analysis

AP = Church Attention Pool. High AP triggers Inquisitor deployments (thresholds: first at AP ≥ 3 per ED-322, second at AP ≥ 6).

At Ob 2, pool 4D:
- Expected AP gain per use: (0.27 × 2) + (0.29 × 2) + (0.31 × 1) + (0.13 × 1 tagged) = 0.54 + 0.58 + 0.31 = **1.43 effective AP per use** (note: Failure-tagged AP is attributed to Varfell, creating a risk distinct from standard AP)

**Is this too strong?** AP at 1.43/use means ~2 Counter-Narrative uses hit first Inquisitor threshold. But:
1. AP resets at Accounting Step 5 (Church Attention Pool resolves threshold responses, pool resets to 0)
2. Counter-Narrative fires in Phase 4 Priority 1 (Intel tier)
3. Uses limited by card hand — Tribune Outward card is shared (4 shared cards; Tribune Outward is Phase 4 Priority 1 slot)

Counter-Narrative cannot chain — one use per season. AP effect per season: ~1.43 AP. This is meaningful but not dominant.

**Failure case — network exposed:** Church is notified of Varfell's presence in territory + AP +1 tagged as Varfell. Two-season consequences: Church knows Varfell has an Intel network there (Counter-Narrative Ob +1 in that territory next season as Church alerts Inquisitors — local counter-intelligence). This asymmetric failure condition creates genuine risk. Failure at Ob 3 (20% chance) is not negligible.

### Interaction with Hafenmark Challenge (combined)

Confirmed via SIM-PP-431-COR: worst case = −0.5 TC in one season (Hafenmark OW + Varfell CN OW). Not pathological. PASS.

### Edge Cases

**Edge 1: Counter-Narrative in Hafenmark-controlled territory with Church Prominence**
Church Prominence = Church global Mandate exceeds controlling faction Mandate. Hafenmark M 4, Church M 5 → Church prominent in Hafenmark territory. Varfell can target. Effect: AP +2 in Hafenmark's territory. Does Hafenmark care? Yes — if Church seizes a Hafenmark territory, PI drops. So Varfell's AP pressure in Hafenmark territories can indirectly threaten PI. Interesting emergent interaction: Varfell + Hafenmark co-operate against Church even without coordination.

**Edge 2: Counter-Narrative + Active Inquisitor in territory (PP-429 Inquisitor)**
Investigate/Intel in Church territory with Inquisitor: +2 Ob. Counter-Narrative is Tribune Outward (not Investigate). Is it a Tribune Intel action? Yes — Tribune tier actions. Does +2 Ob (Inquisitor penalty) apply? Rule states "+2 Ob in Church territory with Inquisitor" for Investigate/Intel. Counter-Narrative is Intel-class. Ruling: +2 Ob applies. Ob 2 → Ob 4 with Inquisitor present. At Ob 4, pool 4D: P(OW) ≈ 1%, P(Succ) ≈ 15%, P(Partial) ≈ 40%, P(Fail) ≈ 44%. Counter-Narrative becomes near-unworkable with an Inquisitor in territory — Varfell must remove the Inquisitor first. Correct design: Inquisitors counter intelligence operations.

**Edge 3: Counter-Narrative in TC 75 Church seizure territory**
Post-TC 75, Church is in seizure mode. Counter-Narrative firing in a territory about to be seized: Church notified (on Failure) = seized territory has Varfell network flagged. Seizure Ob formula unchanged. No interaction with seizure mechanics. Safe.

**Edge 4: VTM 3+ + Counter-Narrative**
VTM 3+: Tribune Intel actions are Consequentialism-aligned → −1 Ob already applied. No double-dip: VTM provides the ethical framework modifier, not an additional separate modifier. Single −1 Ob, confirmed.

### Summary
- Counter-Narrative is repositioned as AP-pressure tool with occasional TC dent
- Expected TC impact: −0.04 to −0.135 per use (far below original −0.415)
- Expected AP impact: 1.43/use — meaningful; drives Church toward Inquisitor deployment
- Failure risk creates credible downside (network exposed, +2 Ob next season)
- Inquisitor interaction creates natural counter-play (Church deploys Inquisitor → Counter-Narrative neutered)

**Retest: PASS. PP-441-COR resolves the P1 finding from SIM-PP-06.**

---

## Findings
- PASS: TC effect no longer dominant — correctly repositioned as AP mechanic
- PASS: No stacking path to negative TC drift
- PASS: Inquisitor counter-play exists and functions correctly
- FINDING: Counter-Narrative in Hafenmark-prominent territories creates emergent Varfell/Hafenmark indirect coordination (noted; no fix required — interesting design)
- FINDING: Failure-tagged AP creates asymmetric exposure (Varfell's Intel identified in territory for one season)

