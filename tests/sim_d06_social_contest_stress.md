# Valoria Social Contest — Stress Test Results
## SIM-D-06
## Date: 2026-04-08
## Model: Sonnet 4.6
## Source: designs/debate/debate_system_redesign_v1.md (Part 6, v1.6) + references/params_debate.md
## Modes: A (Isolation) + D (Edge Cases)
## Status: COMPLETE — findings below

---

## FETCH LOG
designs/debate/debate_system_redesign_v1.md: ✓ fetched (787 lines)
references/params_debate.md: ✓ fetched (366 lines)
canon/02_canon_constraints.md: ✓ fetched (25 lines)
references/canonical_sources.yaml: ✓ fetched (156 lines)

**Governing values source:** params_debate.md (PP-232 pool correction applied; PP-278 resistance formula applied)
**Simulations:** 50,000–100,000 trials per scenario, random seed varied per section.

---

## SCOPE NOTES

**Operative system:** Part 6 only (Parts 1–4 are deprecated design reference).
**Pool formula used:** (Cognition × 2) + History (PP-232 governs; Presence pool from Part 6 is superseded).
**Initiative stat used:** Attunement (PP-232 governs).
**Orientation handling:** All simulations assume Revealing orientation. Obscuring is UNDEFINED (CONFLICT-1 below).
**Composure formula:** Provisional (ED-127 unresolved). Strain results are indicative.

---

## MODE A — POOL ISOLATION

### A-1: Dice Pool Distribution (TN 7, 100k trials)

| Pool | E[net] | P(≥1) | P(≥2) | P(≥3) | P(≥5) | P(≤0) |
|------|--------|-------|-------|-------|-------|-------|
| 4D   | 1.32   | 71.9% | 44.5% | 19.9% |  1.1% | 28.1% |
| 6D   | 1.98   | 80.6% | 60.8% | 37.8% |  7.2% | 19.4% |
| 8D   | 2.63   | 86.0% | 71.5% | 52.3% | 17.2% | 14.0% |
| 10D  | 3.29   | 89.5% | 79.0% | 63.8% | 29.1% | 10.5% |
| 12D  | 3.96   | 92.4% | 84.3% | 72.4% | 40.9% |  7.6% |
| 15D  | 4.95   | 94.9% | 89.8% | 81.5% | 56.3% |  5.1% |
| 18D  | 5.93   | 96.6% | 93.0% | 87.4% | 68.2% |  3.4% |
| 20D  | 6.60   | 97.4% | 94.8% | 90.3% | 74.6% |  2.6% |

### A-2: Representative Character Pools

| Profile | Cognition | History | Base Pool | w/Memory +2D | E[net] |
|---------|-----------|---------|-----------|--------------|--------|
| Scholar   | 4 | 3 | 11D | 13D | 3.6 |
| Diplomat  | 3 | 3 |  9D | 11D | 3.0 |
| Advocate  | 3 | 2 |  8D | 10D | 2.6 |
| Courtier  | 2 | 2 |  6D |  8D | 2.0 |
| Merchant  | 2 | 3 |  7D |  9D | 2.3 |
| Novice    | 1 | 1 |  3D |  5D | 1.0 |

### A-3: CT Movement — Minimum Margin Required (Revealing orientation)

Formula: effective_margin = floor(margin × genre_weight); Δ = effective_margin − resistance (if > resistance).

**Resistance 1 (Stability 1–4, typical low-stability audience):**

| Genre Weight | Min margin to move | Margin for +1 CT | Margin for +2 CT | Margin for +3 CT |
|---|---|---|---|---|
| ×0.5 (off-genre)  | 3 | 5 | 7 | 9 |
| ×1.0 (primary)    | 2 | 3 | 4 | 5 |
| ×1.5 (boosted)    | 1 | 2 | 3 | 3 |

**Resistance 2 (Stability 5–7):**

| Genre Weight | Min margin to move | Margin for +1 CT | Margin for +2 CT | Margin for +3 CT |
|---|---|---|---|---|
| ×0.5 (off-genre)  | 6 | 7 | 9 | 11 |
| ×1.0 (primary)    | 3 | 4 | 5 | 6  |
| ×1.5 (boosted)    | 2 | 3 | 3 | 4  |

**Finding A-3a:** Off-genre (×0.5) + resistance 2 requires margin ≥ 6 for ANY CT movement. P(|margin| ≥ 6 between 9D pools) ≈ 6.5%. Off-genre play against a high-stability audience is mechanically near-dead.

---

## MODE A — CLASH SIMULATION

### A-4: CLASH — Scholar(11D) vs Diplomat(9D), resistance 1

| Genre Weight | A wins | B wins | Ties | A avg CT move | A zero-move rate | B avg CT move |
|---|---|---|---|---|---|---|
| ×0.5 | 52.1% | 35.5% | 12.5% | 0.51 | 64.5% | 0.34 |
| ×1.0 | 52.1% | 35.6% | 12.3% | 2.10 | 23.9% | 1.66 |
| ×1.5 | 51.9% | 35.7% | 12.5% | 3.36 | 24.0% | 2.70 |

**Finding A-4a:** Pool advantage of 2D (52% vs 35% win rate per exchange) is real but moderate. The larger effect of genre weight is on CT movement magnitude, not on who wins each exchange.

**Finding A-4b:** At ×0.5, 64.5% of Scholar's winning exchanges produce ZERO CT movement (resistance absorbs). This confirms off-genre play as extremely CT-inefficient even with a pool advantage.

### A-5: 3-Exchange Formal Debate — Final Outcome Distribution

| Matchup | Genre Weight | Resistance | A wins | B wins | Compromise | Avg CT |
|---|---|---|---|---|---|---|
| Scholar(11D) vs Diplomat(9D)  | ×1.0 | 1 | 52.9% | 20.0% | 27.1% | 6.39 |
| Scholar(11D) vs Diplomat(9D)  | ×1.5 | 1 | 55.9% | 25.4% | 18.6% | 6.40 |
| Scholar(11D) vs Diplomat(9D)  | ×1.0 | 2 | 45.4% | 15.3% | 39.3% | 6.20 |
| Scholar(11D) vs Diplomat(9D)  | ×1.5 | 2 | 53.7% | 21.5% | 24.7% | 6.41 |
| Scholar(11D) vs Novice(3D)    | ×1.0 | 1 | 90.8% |  1.1% |  8.2% | 9.05 |
| Scholar(11D) vs Novice(3D)    | ×1.5 | 1 | 92.6% |  1.9% |  5.5% | 9.29 |
| Diplomat(9D) vs Diplomat(9D)  | ×1.0 | 1 | 38.9% | 30.1% | 31.1% | 5.35 |
| Diplomat(9D) vs Diplomat(9D)  | ×1.5 | 1 | 42.1% | 36.5% | 21.4% | 5.27 |
| Diplomat(9D) vs Diplomat(9D)  | ×1.0 | 2 | 31.9% | 22.3% | 45.8% | 5.38 |
| Scholar(11D) vs Scholar(11D)  | ×1.0 | 1 | 39.5% | 32.5% | 28.0% | 5.29 |
| Scholar(11D) vs Scholar(11D)  | ×1.5 | 1 | 42.6% | 38.0% | 19.4% | 5.24 |

**Finding A-5a:** In even matchups (Diplomat vs Diplomat), initiative holder wins 38–42% vs 30–36% for non-holder, with 20–46% compromise. Initiative advantage is structurally significant in contested debates.

**Finding A-5b:** High resistance (2) dramatically increases compromise rates in close matchups (31% → 46% in 9D vs 9D). High-Stability audiences actively suppress decisive outcomes.

**Finding A-5c:** Single-exchange P(CT reaching 7 from 5) = 28% at ×1.0, 39% at ×1.5. First-exchange decisive wins are common for pool-advantaged orators at boosted genre.

---

## MODE D — EDGE CASES

### EC-01: Off-genre against boosted-genre opponent (severity: P3)
**Setup:** Scholar(11D, ×0.5) vs Diplomat(9D, ×1.5). Resistance 1.
**Outcome:** A wins 19.7% | B wins 44.2% | Compromise 36.1%.
**Mechanism:** Scholar's pool advantage cannot overcome the 3× weight differential (×0.5 vs ×1.5).
**Severity:** P3 — expected behavior. Off-genre should lose. No fix needed.
**Note:** Genre choice is the dominant strategic variable, not pool size, in mismatched weight scenarios.

### EC-02: Off-genre + resistance 2 deadlock (severity: P2)
**Setup:** Any orator playing ×0.5 genre against resistance 2 audience.
**Mechanism:** Minimum margin for CT movement = 6. P(|margin| ≥ 6 from 9D pools) ≈ 6.5%.
**Result:** Expected CT movement per exchange ≈ 0.07. Effectively zero.
**Severity:** P2 — produces a bad play experience for any orator who mischooses or is forced off-genre against a high-stability audience. The ×0.5 weight at resistance 2 is functionally a dead play.
**Proposed fix:** Consider whether resistance 2 should be reduced to resistance 1 for certain faction types (Guilds, Revolution) or whether off-genre play needs a floor effect. Alternatively, confirm by design intent.

### EC-03: Initiative advantage quantification (severity: P3)
**Setup:** Equal pool matchup (9D vs 9D), 3 exchanges.
**Mechanism:** TIE rate = 13.2%. Each tie moves CT +1 toward initiative holder. Expected free CT gain from ties = 0.4 in 3 exchanges.
**Outcome:** Initiative holder wins 38.9% vs 30.1% for non-holder in equal matchup. 8.8 percentage point structural advantage.
**Severity:** P3 — meaningful but not dominant. Initiative tie-breaking (PP-318/ED-138) is warranted.
**Note:** In Grand Debates (5 exchanges), this advantage compounds: ~0.65 free CT from ties.

### EC-04: Single-exchange decisive win probability (severity: P3)
**Setup:** Scholar(11D) vs Diplomat(9D), boosted genre ×1.5, resistance 1.
**Result:** P(CT reaches 7+ from 5 in 1 exchange) = 39%.
**Severity:** P3 — aggressive but not degenerate. A strong first exchange can pre-decide the debate before most decisions matter.
**Note:** Prepstep (§6.11) grants +1D on Exchange 1. Scholar with prep = 12D. P(decisive first exchange) increases further. Not a problem; confirms prep is high-value.

### EC-05: Concentration depletion — Grand Debate guarantee (severity: P2)
**Setup:** Any character with Focus + Presence ≤ 7 in a 5-exchange Grand Debate.
**Mechanism:** Depletion = −1/exchange + −1/loss. Expected depletions in 5 exchanges ≈ 7.5 (assuming 50% loss rate). Spent fires when Concentration = 0; resets to max.
**Result:** ALL standard characters will be Spent at least once in a Grand Debate. Spent penalty: −2D; opponent +1D.
**Severity:** P2 — Spent is not a rare dramatic moment; it's a guaranteed tax in Grand Debates. The intended arc (Spent as dramatic exhaustion) is diluted when every character hits it every Grand Debate.
**Proposed fix:** Reduce Concentration depletion rate in Grand Debates (e.g., −1/2 exchanges instead of −1/exchange), OR increase Focus contribution to Concentration. Alternatively, confirm by design intent that Spent is expected every Grand Debate.

### EC-06: AMPLIFY pool cap bite point (severity: P3)
**Setup:** AMPLIFY exchange with 3+ orators.
**Mechanism:** Cap = highest individual pool × 2. With lead 11D, cap = 22D. Cap bites when total coalition pool > 22D (i.e., when a third orator of 9D+ joins).
**Result:** 2-orator coalitions: cap doesn't bite. 3-orator coalitions with typical pools: cap bites, reducing effective pool by 3–9D.
**Severity:** P3 — cap functions as intended. Prevents degenerate 4-orator blowouts.

### EC-07: Doubt Marker effectiveness (severity: P2)
**Setup:** Obscuring win → Doubt Marker placed. Marker reduces next winning exchange's effective_margin by 2.
**Result:** Against Scholar(11D), Doubt Marker fully negates 46.3% of wins at ×1.0 genre weight, 24.3% at ×1.5.
**Severity:** P2 — Doubt Marker is highly effective against moderate-margin wins at primary genre weight. Against boosted genre, it's less decisive. This is functionally a powerful defensive tool.
**Note:** Conditional on CONFLICT-1 (Obscuring is undefined). See below.

### EC-08: Genre pivot depletion stack (severity: P2)
**Setup:** Orator pivots genre + loses the same exchange.
**Mechanism:** Pivot exchange: −1 (standard) + −1 (pivot cost) + −1 (loss) = −3 Concentration in one exchange.
**Result:** Focus 2, Presence 2 character (Concentration=4): one pivot+loss in exchange 1 leaves Concentration=1. Any subsequent exchange loss triggers Spent immediately.
**Severity:** P2 — pivot is a high-risk action for any character with Concentration ≤ 5. Strategically sound but carries significant endurance cost.
**[P1-CONFLICT]:** Params says "pivot once per debate" (params_debate ED-045). Design says "unrestricted between exchanges" (PP-112). These are contradictory. Pivot frequency is unresolved.

### EC-09: Corroboration value by exchange type (severity: P3)
**Result:** In CLASH: +1D adds +0.33 expected margin — meaningful. In CROSS at ×0.5: +0.33 net → +0.17 effective → often zero increase in effective_margin after floor + halving.
**Severity:** P3 — design note in PP-317 already calls this out. No new finding.

### EC-10: Memory bonus — pool gap closure (severity: P3)
**Result:** +2D Memory bonus closes a 2–3D pool gap: Weak(8D+2D) beats Strong(11D) 39.7% of exchanges. Weak(6D+2D) beats Strong(9D) 38.6%.
**Severity:** P3 — Memory bonus is significant but not dominant. Correct incentive for players to prepare specific citations.
**Note:** Memory bonus is binary and GM-adjudicated ("specific, named, verifiable claim"). GM call consistency is a play quality concern, not a mechanical one.

### EC-11: Appraise failure rate by Attunement (severity: P2)
**Result:** Attunement 1: 61% mislead rate. Attunement 2: 44%. Attunement 3: 35%. Attunement 4: 28%.
**Mechanism:** Failure on Appraise Ob 1 causes GM to identify a weak genre as strong → orator plays ×0.5 thinking it's ×1.0+.
**Severity:** P2 — at Attunement 1–2 (common attribute range), nearly half of all Appraise rolls produce false information. Combined with the severity of off-genre play (EC-01, EC-02), low-Attunement characters face a systematic disadvantage that stacks: they can't read the room AND pay full price for misreads. This may or may not be intended differentiation.
**Proposed fix:** Consider whether Attunement 1 characters should have access to a safer fallback: e.g., Failure produces "no information" rather than "false information." Or confirm by design intent.

---

## CHURCH TRIBUNAL ANALYSIS

### CT-01: Asymmetric proceeding — Inquisitor(11D, Past×1.5) vs Accused(9D)

**Key finding:** Halved resistance for Accused is **mechanically null at resistance 1** (ceil(1/2)=1). The accused benefit only manifests when base resistance ≥ 2.

| Exchanges | Accused genre | Inquisitor wins | Accused wins | Compromise |
|---|---|---|---|---|
| 1 | ×0.5 off-genre | 52.0% | 0.4% | 47.5% |
| 3 | ×0.5 off-genre | 84.4% | 0.8% | 14.8% |
| 5 | ×0.5 off-genre | 93.5% | 0.6% |  5.9% |
| 1 | ×1.0 present   | 52.0% | 9.4% | 38.6% |
| 3 | ×1.0 present   | 69.6% | 11.9% | 18.4% |
| 5 | ×1.0 present   | 73.5% | 11.2% | 15.3% |

With resistance 2 (Stability 5–7 audience, halved to 1 for accused):

| Exchanges | Accused genre | Inquisitor wins | Accused wins |
|---|---|---|---|
| 3 | ×0.5 off-genre | 81.9% | 0.9% |
| 3 | ×1.0 present   | 64.4% | 13.5% |
| 3 | ×1.5 boosted   | 56.9% | 23.1% |

**Finding CT-01a:** Design note (PP-109) warns that 1-exchange Tribunal with boosted genre + biased CT start achieves ~88% P(Inquisitor win). Simulations confirm: at 3 exchanges off-genre, 84% win rate. Design's recommendation (≥3 exchanges for dramatic play) is correct.

**Finding CT-01b [P1]:** Accused playing the boosted genre (Past ×1.5 against Church) at resistance 2 reduces Inquisitor win rate to 56.9%. This requires the accused to argue on Church's strongest terrain — citing scripture/doctrine against the Inquisitor's charge. Mechanically possible but narratively constrained. The system correctly represents "best defense is the Church's own texts."

---

## STRAIN ACCUMULATION

### SA-01: Rattled rates, 3-exchange debate

| Matchup | Composure | Rattled rate |
|---|---|---|
| Diplomat(9D) vs Scholar(11D) | 8 | 7.3% |
| Novice(6D, Composure 6) vs Scholar(11D) | 6 | 56.1% |

**Finding SA-01a:** Mismatched debates produce very high Rattled rates for the weaker party. Novice-level characters in competitive formal debates will be Rattled majority of the time. This is appropriate — formal debates should be punishing for underprepared participants.

**Finding SA-01b:** Composure formula is provisional (ED-127 unresolved). These rates will change once ED-127 is resolved.

---

## CRITICAL UNRESOLVED CONFLICTS

### CONFLICT-1 [P1]: Obscuring orientation — incompatible definitions
**Design (Part 6, §6.4):** Obscuring win → Doubt Marker placed; zero CT movement.
**Params (params_debate):** Orientation weights Revealing=×1.0, Obscuring=×0.75. Obscuring still moves CT (at reduced rate).
**Mechanical impact:**
- Design version: Obscuring + boosted genre = powerful defensive tool (Doubt Marker) with no offensive CT gain.
- Params version: Obscuring + boosted genre (×1.5×0.75=×1.125) still beats Revealing primary (×1.0) for CT movement.
- These produce fundamentally different strategic incentives.
**Status:** Cannot simulate Obscuring play. All simulations assume Revealing.
**Action required:** Editorial decision on which definition governs before Obscuring mechanics can be validated.

### CONFLICT-2 [P2]: Genre pivot frequency
**Design (PP-112):** Unrestricted genre pivot between exchanges.
**Params (ED-045):** Pivot once per debate, costs −1 Concentration.
**Mechanical impact:** Unrestricted pivot enables genre-reads-counter-pivot loop each exchange. Once-per-debate makes pivot a one-time trump card.
**Action required:** Confirm which rule governs.

### CONFLICT-3 [P2]: Composure formula
**Design (§6.2):** Composure = Poise + Bonds + 3.
**Params:** Formula pending ED-127. Poise deprecated.
**Action required:** ED-127 must be resolved before Composure/Rattled/strain mechanics can be validated.

### CONFLICT-4 [RESOLVED]: Corroboration Knot requirement
Params PP-260 governs: any witness may corroborate. Design's Knot requirement is superseded.

### CONFLICT-5 [RESOLVED]: Pool formula
Params PP-232 governs: (Cognition × 2) + History. All simulations use this.

---

## OPEN ITEMS FROM DESIGN (still unresolved)

These items from the design doc's §6.9 remain flagged but were not the focus of this stress test:

- GAP-DS-12: Corroboration procedure not fully ported to Part 6 (§3.5 used as provisional)
- [EDITORIAL: Concentration attribute — Focus vs Poise] (stress test used Focus; confirm)
- [EDITORIAL: Audience Disposition win-condition — all Formal vs Grand only] (untested)
- [EDITORIAL: Grand Debate role alternation — which side proposes 3 times in 5 exchanges?]
- [EDITORIAL: Niflhel formal Debate access]
- Multi-party debates (§6.12): not stress-tested. ED-179 (simultaneous audience capture) open.

---

## SIM-DEBT REGISTER UPDATE

| Item | Status | Notes |
|------|--------|-------|
| SIM-DEBT-01 | RESOLVED (SIM-D-05) | Baselines already in params |
| SIM-DEBT-02 | OPEN | Corroboration in CLASH calibration pending |
| SIM-DEBT-03 (new) | OPEN | Obscuring mechanics untestable until CONFLICT-1 resolved |
| SIM-DEBT-04 (new) | OPEN | Composure/strain calibration pending ED-127 resolution |
| SIM-DEBT-05 (new) | OPEN | Grand Debate 5-exchange full simulation pending Concentration fix (EC-05) |

---

## FINDINGS SUMMARY BY SEVERITY

**P1:**
- CONFLICT-1: Obscuring orientation incompatibly defined in design vs params. Blocks all Obscuring simulation.

**P2:**
- EC-02: Off-genre (×0.5) + resistance 2 = mechanically dead play (P(CT movement) ≈ 6.5%).
- EC-05: Spent is guaranteed every Grand Debate for all standard characters. Undermines intended dramatic arc.
- EC-07: Doubt Marker very effective (negates 24–46% of winning exchanges) — conditional on CONFLICT-1.
- EC-08: Genre pivot + loss = −3 Concentration triple-stack. Dangerous for low-Concentration builds. Pivot frequency unresolved (CONFLICT-2).
- EC-11: Attunement 1–2: 44–61% Appraise mislead rate. Systematic disadvantage stacking with off-genre penalty.
- CT-01b: Tribunal halved resistance is null at resistance 1. Only matters at resistance 2+. Low-stability Church audiences provide no actual accused benefit.
- CONFLICT-2: Genre pivot frequency unresolved.
- CONFLICT-3: Composure formula unresolved (ED-127).

**P3:**
- EC-01: Off-genre against boosted-genre opponent loses as expected. No fix needed.
- EC-03: Initiative advantage = 8.8 pp in even matchups. Confirmed significant; tie-break rule (PP-318) is warranted.
- EC-04: 39% P(decisive first exchange) at boosted genre. Aggressive but not degenerate.
- EC-06: AMPLIFY cap functions correctly. No issue.
- EC-09: Corroboration weaker in CROSS than CLASH. Confirmed by design note. No fix needed.
- EC-10: Memory bonus closes 2–3D gap. Correct incentive.

---
*End SIM-D-06*
