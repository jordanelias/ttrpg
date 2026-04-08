# SIM-PP-431-COR — Parliamentary Challenge Corrected Retest
## Date: 2026-04-07 | Mode: A (Isolation) + B (Interaction Chain)
## Source: PP-431-COR — Challenge REPLACES structural suppression in seasons used

---

## FETCH LOG
canonical_sources.yaml: ✓ fetched (156 lines)
references/params_board_game.md: ✓ fetched (1068 lines)
references/params_factions.md: ✓ fetched (480 lines)
designs/board_game/victory_architecture_v1.md: ✓ fetched (368 lines)

---

## System Under Test

**PP-431 (corrected by PP-431-COR):**
Parliamentary Challenge (Senator Inward, Hafenmark, once/season).
Roll: Mandate vs Ob 2 (−1 Ob if PI ≥ 5 → Ob 1 at high PI).
- Overwhelming: TC −2 + Church Uphold/Appease
- Success: TC −1
- Partial: Stability −1
- Failure: Stability −1 + Church Mandate +1

**PP-431-COR rule:** In any season Hafenmark plays Parliamentary Challenge, the structural TC suppression (TC −1/season automatic from Baralta's Mandate ≥ 4 threshold) does NOT fire. Challenge replaces structural in that season.

---

## Mode A: TC Suppression Mechanics — Full Input Range

### TC Effect Sources (combined view)

| Season State | TC sources | Net TC change |
|---|---|---|
| No actions | Passive +1 | +1 |
| Church plays Assert | Assert replaces passive: +2 | +2 |
| Baralta Mandate ≥ 4 (structural) | Passive +1, structural −1 | 0 |
| Challenge played (Success), Baralta M ≥ 4 | Challenge replaces structural: net TC −1 | −1 |
| Challenge played (Overwhelming), Baralta M ≥ 4 | Challenge replaces structural: net TC −2 | −2 |
| Challenge played (Failure), Baralta M ≥ 4 | Challenge played but failed — structural still replaced? |

**Ruling clarification (PP-431-COR):** "When Hafenmark plays Parliamentary Challenge" — the replacement fires on declaration, not on outcome. If Hafenmark declares Challenge (card played), structural suppression is foregone that season regardless of roll result. This means:

| Challenge outcome | TC effect | Net vs baseline (structural active) |
|---|---|---|
| Overwhelming | −2 | −2 vs 0 baseline = TC −2 net delta |
| Success | −1 | −1 vs 0 baseline = TC −1 net delta |
| Partial | 0 (Challenge fired, no TC effect, structural forfeited) | 0 vs 0 baseline = no change |
| Failure | +1 (passive only, structural forfeited) + Church Mandate +1 | +1 vs 0 baseline = TC +1 net delta |

**Finding:** Partial and Failure outcomes are now costly — Hafenmark has given up structural suppression for no TC gain (Partial) or a net loss (Failure). This is correct design tension: Challenge is not a free supplement, it is a gamble on replacing reliable structural suppression with variable roll-based suppression.

### Probability Analysis

Hafenmark Mandate 4 (starting), Ob 2:
| Pool | Ob | P(Overwhelming) | P(Success) | P(Partial) | P(Failure) |
|------|----|-----------------|------------|------------|------------|
| 4D | 2 | ~27% | ~29% | ~31% | ~13% |
| 4D | 1 (PI≥5) | ~85% | ~12% | ~3% | ~0% |

At Ob 2 (standard): Expected TC change from Challenge = (0.27 × −2) + (0.29 × −1) + (0.31 × 0) + (0.13 × +1)
= −0.54 + (−0.29) + 0 + 0.13 = **−0.70 TC expected per season** (vs −0 structural baseline, −1 if structural fires)

At Ob 1 (PI ≥ 5): Expected TC change = (0.85 × −2) + (0.12 × −1) + (0.03 × 0) + 0
= −1.70 + (−0.12) = **−1.82 TC expected per season**

**Structural baseline (Baralta Mandate ≥ 4, no Challenge):** −1.0 TC/season (deterministic).

**Comparison:**
- Structural alone: −1.0/season (reliable)
- Challenge alone (Ob 2): −0.70/season (lower expected value, higher variance, Failure risk)
- Challenge alone (Ob 1, high PI): −1.82/season (better than structural, but Mandate-dependent)

**Finding:** Challenge at Ob 2 is slightly worse expected value than structural, compensating for Overwhelming upside (−2 possible). At Ob 1 (PI ≥ 5), Challenge strongly outperforms structural. The correct strategic call: use Challenge when PI ≥ 5; rely on structural when PI < 5 and Mandate < 5. This is appropriate design — Hafenmark is rewarded for developing PI.

---

## Mode B: Interaction Chain — Challenge + PP-441-COR Counter-Narrative

**Chain:** Season where both Challenge (Hafenmark) and Counter-Narrative (Varfell) fire.

### PP-441-COR Counter-Narrative revised effects:
- Overwhelming: TC −0.5 + AP +2
- Success: AP +2 only (no TC effect)
- Partial: AP +1
- Failure: network exposed

**Combined TC suppression (Hafenmark Challenge Success + Varfell Counter-Narrative Overwhelming):**

TC passive: +1
Hafenmark structural: FORFEITED (Challenge played)
Hafenmark Challenge Success: −1
Varfell Counter-Narrative Overwhelming: −0.5

Net TC: +1 − 1 − 0.5 = **−0.5** (TC decreases by 0.5)

**Is this problematic?** TC 0.5 fractional rounding: floor at Accounting = TC drops by 1 if ≥ 0.5 net decrease. But TC also has passive +1 applied. Net: TC −0.5 rounds to TC decreases by 0 at Accounting (0.5 below starting point = round down to no change since positive TC drift is integer and negative is fractional). 

**Ruling:** Fractional TC values accumulate across seasons. Keep a running decimal on the TC track clock (track full value, round to integer only for display/threshold checks). At Accounting: apply the accumulated fractional change. This prevents fraction-stripping.

**Worst credible case (both at maximum):** Hafenmark Challenge Overwhelming (−2) + Varfell Counter-Narrative Overwhelming (−0.5) + structural forfeited:
Net: +1 (passive) − 2 − 0.5 = **−1.5 TC in one season**.

**Is −1.5 TC in one season pathological?** TC starts at 28. To freeze Church at 75 requires TC to cross 75. With −1.5 TC/season maximum combined, and passive +1, net drift without both Overwhelming: +1/season. Maximum combined suppression is a niche outcome requiring both factions to roll Overwhelming in the same season. Church still advances 46 TC points at +1/season baseline — that's 46 seasons (multiple arcs). Even sustained Hafenmark+Varfell coordination at average yields (−0.70 + ~−0.15 Varfell) = ~−0.85 combined suppression, meaning TC advances at approximately +0.15/season. 

**No longer pathological. PP-431-COR + PP-441-COR together produce a TC that Church can still credibly advance.**

**Finding:** PASS. Corrected versions interact correctly. Church is suppressed but not locked.

---

## Mode A: Edge Cases

**Edge 1: Hafenmark Mandate drops below 4 mid-game**
Structural suppression (Baralta) requires Mandate ≥ 4. If Mandate drops to 3: structural no longer fires. Challenge is Hafenmark's only TC tool. At Mandate 3, pool 3D:
- Ob 2: P(Success+OW) = ~42%. Expected TC = ~−0.55/season. Worse than structural was — Hafenmark must maintain Mandate.

**Edge 2: Challenge + Church Assert in same season**
Challenge replaces structural. Assert fires as Church action (Church plays Assert; TC +2 replaces passive +1 → net +2). Hafenmark Challenge Success: −1. Net: +2 − 1 = **+1 TC**. Hafenmark cannot stop Assert via Challenge — they can only mitigate it. Correct.

**Edge 3: Challenge + Hafenmark Sovereign Authority Doctrine (arc-use)**
Both target TC. Sovereign Authority (once per arc, Ob 4): Overwhelming = TC −3. These are distinct actions on distinct timing. Sovereign Authority fires as Special/Unique Power (Phase 4 Priority 6). Challenge fires as Senator Inward (Phase 4 Priority 4). Both may fire in same season — they do not interact. Structural suppression: forfeited only if Challenge played. Sovereign Authority is not Challenge. Both can fire in the same season. Net possible: TC passive +1 − 3 (SAD Overwhelming) − 1 (Challenge Success) = −3. Strong season but arc-limited.

**Edge 4: PI ≥ 5 + Challenge + Ministry Facilitation**
At PI ≥ 5, Challenge Ob drops to 1. Ministry AP-token in T1 provides Parliamentary Manoeuvre −1 Ob. But Challenge is Senator Inward (not Parliamentary Manoeuvre by card type). Ministry facilitation applies to Parliamentary Manoeuvre (Hafenmark's Inward Senator action). If Parliamentary Challenge IS a Parliamentary Manoeuvre subtype: Ob would be 0 — but Ob minimum is 1 (floor). So: Ob 1 floor. This is the cap.

**Conclusion:** PP-431-COR resolves the P1 finding from SIM-PP-03. No new pathological interactions found. Retest: **PASS.**

---

## Findings
- PASS: Challenge replaces structural; combined suppression is credible but non-pathological
- PASS: Failure/Partial risk creates correct design tension (forfeit structural for gamble)
- PASS: PI ≥ 5 makes Challenge highly efficient — rewards Hafenmark PI investment
- FINDING: Fractional TC accumulation requires running decimal tracking on TC clock (not a new rule — existing; just needed clarification)
- FINDING: Ob floor at 1 caps all modifier stacking (confirmed)

