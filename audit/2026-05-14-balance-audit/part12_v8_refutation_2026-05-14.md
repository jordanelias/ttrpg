# Part 12 — v8 Iteration Results: Symmetric Analogs Don't Close Balance
## Date: 2026-05-14 · Session: bottom-up-canonical-verified · Part 12/12
## Trigger: Part 11 §6.1–§6.4 — implement all 4 analog cards, verify 4-way balance closure
## Methodology: Bottom-up iteration with PP-674 framework lens

---

## §1 Hypothesis Going In

Part 11 §6 hypothesized that closing the stalled trajectories (Varfell + Hafenmark analog cards) would close the 4-way balance gap to ≤ 15pp. The reasoning:

- Each faction would have one flagship L-recovery card
- Recovery rates would converge
- Spread should drop from canon's 42pp to ≤ 15pp

Implementation: v8 simulator added Crown Initiative + Vaynard's Hall + Charter of Liberties + Council of Solmund (4 analog cards, one per faction). 500 campaigns per config.

---

## §2 Result: Hypothesis Refuted

### §2.1 v8 (all 4 analog cards added)

| Configuration | Cr | Ch | Ha | Va | Spread |
|---------------|-----|-----|-----|-----|--------|
| canon (no cards) | 33.4 | 47.6 | 13.8 | 5.2 | 42.4pp |
| canon + 4 analogs | 27.4 | **62.4** | **2.6** | 7.6 | **59.8pp** ← WORSE |
| consent=0.75 + 4 analogs | 33.0 | 57.2 | 1.8 | 8.0 | 55.4pp |
| consent=0.5 + 4 analogs + 50s | 12.6 | 76.8 | 4.2 | 6.4 | 72.6pp |
| consent=0.5 + 4 analogs + 24s | 52.6 | 21.2 | 14.6 | 11.6 | 41.0pp |

**Adding all 4 cards made balance WORSE** in 3 of 5 configs. Spread expanded from canon's 42.4pp to 59.8pp in canon-with-cards.

### §2.2 v8b (3 analog cards, Council of Solmund removed)

Reasoning: Church already has Ecclesiastical Appointment for L-gain; adding Council of Solmund double-stacks. Test: remove Council.

| Configuration | Cr | Ch | Ha | Va | Spread |
|---------------|-----|-----|-----|-----|--------|
| canon, 3 analogs (no Council) | 25.8 | **62.8** | 2.8 | 8.6 | 60.0pp |
| consent=0.75, 3 analogs | 35.4 | 55.2 | 1.8 | 7.6 | 53.4pp |
| consent=0.5, 3 analogs + 24s | 52.4 | 18.8 | 16.2 | 12.6 | 39.8pp |
| consent=1.0, 3 analogs | 43.4 | 48.0 | 1.0 | 7.6 | 47.0pp |

**Still doesn't close.** Stripping Church's analog card barely moves Church's win rate (62.4 → 62.8). The double-stack hypothesis was insufficient.

### §2.3 Failure of the symmetric-cards hypothesis

Closure rate across all 9 tested v8/v8b configs:
- **9/9 configs OPEN** (spread > 25pp)
- **0/9 configs CLOSED** (spread ≤ 15pp)
- Best spread: 39.8pp (consent=0.5 + 3 analogs + 24s) — still 25pp over target

The Part 11 hypothesis ("symmetric L-recovery cards close balance") is refuted by the data.

---

## §3 Why Did the Hypothesis Fail?

### §3.1 The compounding-rate finding

Final Mandate (L) means across configs:

| Faction | canon | canon+4 | consent=0.75+4 |
|---------|-------|---------|----------------|
| Crown | 3.47 | 3.34 | 3.76 |
| Church | 6.15 | 6.45 | 6.43 |
| Hafenmark | 3.57 | 3.48 | 3.43 |
| Varfell | 2.37 | 2.50 | 2.52 |

**Church's mean final L = 6.45** (near the canonical max of 7). Other factions cluster around 3–4. The gap is **3+ L points**, equivalent to a 1.5x advantage in faction Mandate at campaign end.

Where does Church's L come from? Pre-card sources:
- **Ecclesiastical Appointment**: per-season L+1 on Success (~67% success at canon L=5/Ob=2). Fires ~24 times/36 seasons → ~16 successful → +16 L attempts (capped at L=7 — effectively maxes out around season 10).
- **Cardinal Focus** + **Piety Spread** chain: fuels Active Inquisition → territory acquisition → more I + W. Indirect L support via increased resource base.

Compare to Hafenmark's per-arc Parliamentary Session (~4 per campaign × ~50% pass rate ≈ +2 L) or Crown's Crown Treaty (~1.4 successes per campaign per Part 7 data ≈ +1.4 L).

**Church's L-compounding rate is structurally 5–8× faster than other factions.** Adding analog cards at 1×/season or 1×/arc adds at most +1–2 L per campaign for the others — Church already has +5+ baked into the per-season Ecclesiastical Appointment cycle.

### §3.2 The Hafenmark Token cannibalization finding

Hafenmark CRASHED to 1.0–2.8% with Charter of Liberties enabled. Why?

Charter of Liberties (per Part 10 §5.2 spec) requires **1 Token spent + W −1**. Hafenmark holds 1–2 Tokens at a time. Spending one on Charter starves the Token-leverage economy that Dynastic Proclamation depends on (Token on target → DP Ob −1).

**The faction with the strongest existing economy is the most vulnerable to a card that consumes that economy.** Adding Charter without re-thinking Token flow broke Hafenmark.

### §3.3 The Crown opportunity cost finding (re-confirmed)

Crown win-rate: 33.4 → 27.4% with Crown Initiative added. Confirms Part 10 finding — Crown Initiative is a defensive/recovery mechanic, not a power amplifier. Adds character-scale survival without faction-scale dominance.

### §3.4 The Varfell modest-improvement finding

Varfell: 5.2 → 7.6% with Vaynard's Hall. Modest but present. Vaynard's Hall is delivering Mandate recovery; Varfell just remains structurally locked out of Peninsular Sovereignty by the post-CR-STRIKE acquisition vacuum.

---

## §4 Revised Diagnosis

**The 4-way balance problem is not "missing L-recovery for some factions."** It is:

1. **Church's L-compounding rate is too high** (Ecclesiastical Appointment fires too frequently with too-low Ob)
2. **Hafenmark's territorial acquisition vector is bottlenecked** by Token economy (DP requires Tokens for Ob reduction; competing card consumption breaks it)
3. **Varfell has no acquisition path** (CR-STRIKE)
4. **Crown's hegemony path is consent-gated** (Q-1)
5. **All 4 factions face Turmoil ≥ 30** ceiling on victory (Part 8 already showed this)

Adding L-recovery cards addresses #3 partially. Does not address #1, #2, #4, #5.

### §4.1 Per-faction structural analysis

| Faction | Structural issue | Wrong fix | Right fix |
|---------|------------------|-----------|-----------|
| Crown | consent gate (Q-1) | Add L-gain card | Resolve Q-1 canonically; Crown Initiative supplements but doesn't fix |
| Church | L-compounding rate too high | Add Council of Solmund (worsens) | **Throttle Ecclesiastical Appointment** (e.g., 1×/arc instead of per-season, OR L≤5 prereq) |
| Hafenmark | Token cannibalization + DP slot cap | Add Charter of Liberties | **Decouple Charter from Token cost** OR raise Token cap (Hafenmark holds 3+ Tokens before strategic effect) |
| Varfell | No acquisition path | Vaynard's Hall (L-gain) | **Restore an acquisition mechanic** (replacement for CR-STRIKE-struck Cultural Reformation); Vaynard's Hall is L-gain but doesn't enable territorial control |

---

## §5 Bottom-Up Iteration — What Methodology Reveals

This is the value of bottom-up granular emergent: **a naive symmetric-buff hypothesis was refuted by the data**. A top-down design pass would have said "give each faction an L-recovery card, balance closes." Bottom-up simulation said "doesn't work, here's why."

The refutation surfaced THREE structural issues invisible to symmetric-design thinking:

1. **Per-faction action densities matter as much as per-card effects** (Church compounds via Ecclesiastical Appointment per-season; others can't keep up)
2. **Currency dependencies create cannibalization risk** (Hafenmark Token economy)
3. **Acquisition mechanics are different from L-gain mechanics** (Varfell needs the former, not the latter)

These are **emergent structural findings**, not designer intuitions. The framework's failure lexicon term applicable here is **"abstractable"** — symmetric L-recovery cards abstracted the asymmetric faction surfaces; the abstraction failed.

---

## §6 Revised Editorial Slate

Per Part 11 §6.5, bundle Q-1 through Q-15 + new findings into an editorial slate.

### §6.1 Highest-priority decisions (data-ordered)

1. **THROTTLE Ecclesiastical Appointment** — propose: 1×/arc (matching Council of Solmund) instead of per-season. Test impact in v9.
2. **Q-1 Treaty consent rule** — define explicitly (Part 8 ranking)
3. **DECOUPLE Charter of Liberties from Token cost** — propose: pure W −1 cost, higher Ob (test ran in v8c but crashed; needs clean retest)
4. **Restore Varfell acquisition mechanic** — fundamentally needed; Vaynard's Hall L-gain alone insufficient
5. **Resolve territorial completeness threshold** (Part 8 finding)

### §6.2 Mid-priority

6. **Crown Initiative** — adopt per Part 10/11 vetting; positive for character-scale, neutral for faction-scale
7. **Mode II Open Pledge** mechanics — playtest needed
8. **Campaign length** — pick explicitly; 24s favors Crown, 50+ favors Church

### §6.3 Deferred

9. Q-12 through Q-15 (character-scale recovery questions)
10. Cross-faction copy-cat Initiatives (Q-20)

---

## §7 Methodology Audit Update (Part 11 §4 extension)

### §7.1 What Part 12 contributed to the methodology grade

- **Μ-β AUTONOMOUS AGENT COMPOSITION**: continued to embody — emergent results refuted designer hypothesis, demonstrating that the simulator is generating outcomes no agent (or designer) predicted
- **М-6 CHOICE IS FORCED**: deepened — design choices that look symmetric (give everyone a card) produce non-symmetric outcomes; the choice is forced *despite* the apparent symmetry
- **М-4 INSTITUTIONS STAKE SUBSTRATE-POSTURES**: surfaced — Church's institutional density is itself a substrate-posture choice (Ecclesiastical Appointment is canonically about Church's institutional hierarchy); rate-limiting it requires rethinking Church's posture, not just card surface

### §7.2 Failure-lexicon check (Part 12 specifically)

| Failure | Part 12 status |
|---------|----------------|
| Authored emergence | NO — refutation was emergent from sim, not predetermined |
| Abstractable | The proposal in Part 11 §6 was abstractable (symmetric buff); Part 12 caught this |
| Cost-hidden | Hafenmark's Token cannibalization was Cost-hidden in the Part 10 §5.2 sketch; surfaced here |

### §7.3 Momentum audit update (Part 11 §5 extension)

| Trajectory | Status now |
|------------|------------|
| Crown character-scale (Parts 6→10) | landed at design proposal; vetting passed |
| Methodology refinement (v3→v8) | continues compounding — v8 added 4-card test that refuted v8 hypothesis |
| Varfell structural redesign | **STILL stalled** — Vaynard's Hall delivers L-gain not acquisition |
| Hafenmark scaling | **STILL stalled** — Charter of Liberties damaged Hafenmark via Token cost |
| Editorial questions Q-1..Q-20 | unchanged — still need Jordan's editorial pass |
| **NEW: Church L-compounding throttle** | **surfaced as new high-leverage canonical question (Q-21)** |

**The momentum audit now shows MORE stalled trajectories, not fewer.** Bottom-up iteration revealed that the naive closure path doesn't work. This is good methodologically (negative results are informative) but requires next-iteration restructure.

---

## §8 Next Iteration (Part 13 if continued)

### §8.1 Implementation targets

1. **v9 simulator: throttle Ecclesiastical Appointment** to 1×/arc; verify Church L-compounding caps; retest 4-way spread
2. **Charter of Liberties variant**: pure W cost, no Token consume, higher Ob (clean reimplementation of v8c that crashed)
3. **Varfell acquisition mechanic**: NEW design needed — Vaynard's Hall L-gain alone insufficient. Sketch options:
   - **Vaynard's Conquest** (military-led acquisition with Mandate gain at completion)
   - **Tribune Settlement** (Tribune Network → settlement-level Order erosion → eventual ownership)
   - **Strategic Insight** (Revelation Tokens → forced Treaty acceptance; bypasses Q-1)

### §8.2 Open canonical question added

| # | Question | Source |
|---|----------|--------|
| Q-21 | Should Ecclesiastical Appointment be throttled (1×/arc instead of per-season)? Sim data: Church mean L = 6.45 vs others 3.4. | Part 12 emergent finding |
| Q-22 | Should Charter of Liberties consume Tokens (current spec) or just W (canonicalize as legislative-only)? | Part 12 |
| Q-23 | What is Varfell's canonical acquisition mechanism post-CR-STRIKE? | Part 7 EM-10; Part 10 §5.3 sketched L-gain only |

---

## §9 Cross-Part Synthesis (Final, post-Part 12)

| Part | Status |
|------|--------|
| 1 — Errata (4-faction canonical) | Preserved |
| 2 — Log Schema | Preserved |
| 3 — Top-Down Re-Sim | Directionally correct |
| 4 — NERS Audit | Methodologically valid |
| 5 — Throughline Audit (top-down) | Methodologically valid |
| 6 — Bottom-Up MC v3 | Self-corrected by Part 7 |
| 7 — Canonical Bottom-Up v5 | Self-corrected by Part 8 |
| 8 — Sensitivity Analysis | Editorial leverage ranking |
| 9 — Character Decoupling | Surfaced scale layer |
| 10 — Crown Initiative Design | PP-674 vetting candidate |
| 11 — Throughline Audit + Momentum | Framework grade applied |
| **12 — v8 Iteration Refutation** | **NEW** — symmetric analogs hypothesis refuted; Church L-compounding identified as actual structural lever |

**The 12-part chain demonstrates the methodology's core value: refutability.** Part 11 hypothesized; Part 12 tested; the hypothesis failed; the failure surfaced three new structural findings (Church compounding, Hafenmark cannibalization, Varfell acquisition-vs-L distinction) that were invisible to symmetric-design thinking.

Bottom-up granular emergent doesn't deliver final answers. It delivers refined questions. Each iteration's refutation surfaces the next iteration's structural target.

---

## §10 Recommendation to Jordan

The 12-part audit is complete. Next move requires **editorial decision** rather than further simulation. Specifically:

**Single highest-leverage decision: Q-21 (Throttle Ecclesiastical Appointment).** Sim data says Church mean L = 6.45 vs others 3.4; throttling Ecclesiastical Appointment to 1×/arc is the most likely lever to close the 4-way balance. Pre-implementation editorial decision needed: is this canonically appropriate? (Ecclesiastical Appointment is a real Church power historically; throttling it should fit Church's canonical institutional rhythm.)

**Second-highest: Q-1 (Treaty consent rule)** per Part 8. Still highest editorial leverage on Crown's win-rate.

**Third: Varfell acquisition redesign** per Q-23. Vaynard's Hall is necessary but insufficient.

**Fourth: Defer Crown Initiative ratification** until Q-21 + Q-1 + Q-23 resolved — the Crown Initiative's effect depends on the broader balance state.

---

*Session: bottom-up-canonical-verified · 2026-05-14 · Part 12/12*
*Bottom-up methodology delivered a refutation of Part 11's symmetric-buff hypothesis.
The refutation surfaced three new structural findings, requiring next-iteration design
work rather than further simulation. The methodology continues compounding by producing
refined targets.*
