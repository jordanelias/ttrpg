# R2 — Skill Input Layer in Architecture C (Dueling)
## Module 2 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** A (single-mechanic isolation) + D (exhaustive edge cases)
**Source question:** `tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §4 R2`
**Question text:** *"Canonical math is dice-driven. Pirates! / Sekiro / For Honor reference systems involve real-time player skill (timing windows, deflect windows, animation reads). Chunk 6 Q4 adopted E5 as 'C-only inspiration' without specifying mechanic. Decision needed: does C add a skill-timing layer that modifies dice (cap +1 net hit), or does C remain pure dice with stance-UI as visualization only?"*

**Decision shape:** pure dice / cap +1 / cap +2 / no cap

---

## 1. Verification ledger entries (PP-716 canon)

All quoted_text strings verbatim-verified.

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R2-L01 | combat_pool_formula | (Agility × 2) + Relevant History + 3 (minimum 5) | designs/scene/combat_v30.md | §1 | "Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)" |
| R2-L02 | tabletop_baseline_constraint | All mechanics scale from TTRPG baseline | designs/scene/combat_v30.md | header | "Mode applicability: ALL (TTRPG baseline; scales to Hybrid and Board Game via params)" |
| R2-L03 | feint_player_skill_precedent | Cognitive player-skill canonical precedent (commit allocation) | designs/scene/combat_v30.md | §4 line 95 | "Feint \| Player chooses commit: allocate N dice (minimum 3) to Offence for the feint" |
| R2-L04 | stunt_skill_modifier | Existing Game-Master-judged skill modifier with cap +5 | designs/scene/combat_v30.md | §4 line 105 | "Stunt \| Declared with Strike. +N dice to Offence from environmental/positional narrative (Game Master sets N, max 5)." |
| R2-L05 | tn7_baseline | Standard TN baseline | designs/scene/combat_v30.md | §5 | "Base TN = 7" |
| R2-L06 | pool_floor | Combat Pool minimum 5D | params/combat.md | §Pool minimum | "Combat Pool minimum 5 is a clean floor. No −1D penalty at the floor." |

(R2-L01, R2-L05, R2-L06 re-cited from PP-716 baseline; R2-L03 / R2-L04 establish that canon already has cognitive player-skill surfaces.)

---

## 2. Architecture C scope reminder

Per `tests/stress/combat_videogame_arch_2026-05-01/05_q4_q5_q6.md §Q5`:

C is the duel architecture. EXPLORATORY composite stack already adopted:
- **E5 stance flow** (Pirates!-style): "C-only inspiration." Cognitive pre-commit choice — player picks stance/direction; opponent counters.
- **E7 posture-as-yield** (Sekiro): Stamina depletion in C ends the duel rather than penalizing actions.

R2 asks: do we ALSO add a real-time motor-skill layer (Sekiro deflect window, For Honor animation read, button-timing) on top of the cognitive pre-commit + posture endgame?

The synthesis flagged this unspecified. R2 specifies it.

---

## 3. Existing player-skill surfaces in canon

| Surface | Mechanism | Type |
|---|---|---|
| Feint commit (R2-L03) | Player allocates 3+ dice; risk/reward calculation | Cognitive (pre-commit) |
| Stunt declaration (R2-L04) | Player describes environmental/positional creativity; Game Master assigns +N up to +5 | Cognitive (narrative) |
| Phase-1 declaration | Player chooses action priority before resolution | Cognitive |
| Pool allocation | Offence ↔ Defence split per round | Cognitive |
| Architecture C stance commit (proposed E5) | Pre-commit attack direction; opponent counters | Cognitive |

**Player skill in canon is universally cognitive — pre-commit decisions, narrative creativity, resource allocation.** No motor-skill (timing/reflex) channel exists. R2 asks whether to add one for C.

---

## 4. Candidates

| ID | Name | Description | Tabletop-compatible? |
|---|---|---|---|
| **C2.1** | Pure dice (cognitive only) | E5 + E7 already adopted. No additional skill layer. Stance UI is visualization only. | ✓ — all-cognitive |
| **C2.2** | Cap +1 net hit | Real-time deflect window or animation-read mini-game. Skill check (timing/pattern). On success, +1 net hit. | ⚠ — needs tabletop fallback |
| **C2.3** | Cap +2 net hits | Same as +1 but doubled cap. | ⚠ — same fallback constraint |
| **C2.4** | No cap (skill-resolves) | Full Sekiro: perfect deflect = engagement won, dice bypassed. | ✗ — tabletop-incompatible |

---

## 5. Probability impact (Mode A isolation)

Skill-check success probability assumed at 0.70 (calibrated from Sekiro-class deflect-window pass rates). At TN 7 with 1s subtracting, expected net per die ≈ 0.33.

### Skill contribution as % of total expected net successes

| Pool | Base E[net] | Cap +1 (% leverage) | Cap +2 (% leverage) | Uncapped (% leverage) |
|---|---|---|---|---|
| 4D | 1.32 | 2.02 (35%) | 2.72 (51%) | 4.12 (68%) |
| 6D | 1.98 | 2.68 (26%) | 3.38 (41%) | 6.18 (68%) |
| 8D | 2.64 | 3.34 (21%) | 4.04 (35%) | 8.24 (68%) |
| 10D | 3.30 | 4.00 (18%) | 4.70 (30%) | 10.30 (68%) |
| 12D | 3.96 | 4.66 (15%) | 5.36 (26%) | 12.36 (68%) |
| 15D | 4.95 | 5.65 (12%) | 6.35 (22%) | 15.45 (68%) |

**Capped skill input scales inversely with pool size** — strong compensator at low pool, marginal at high pool. Uncapped is uniform 68% leverage regardless of stat — degenerate skill-trumps-stat.

### Stat ↔ skill priority table

Reference: low-stat character (5D Pool floor R2-L06) with skill vs high-stat (12D, no skill).

| Mechanic | Low-stat + skill | High-stat − skill | Winner | Comment |
|---|---|---|---|---|
| C2.1 Pure dice | 1.65 | 3.96 | HIGH (stat) | Stat dominates as canon intends |
| C2.2 Cap +1 | 2.35 | 3.96 | HIGH (stat) | Skill compensates 41% of gap, doesn't close it |
| C2.3 Cap +2 | 3.05 | 3.96 | HIGH (stat) | Skill compensates 70% of gap; stat still wins |
| C2.4 Uncapped | 5.15 | 3.96 | **LOW (skill)** | Stat hierarchy inverted — degenerate |

**Cap +1 and Cap +2 both preserve canonical stat hierarchy.** Uncapped breaks it.

---

## 6. NERS at full grain — 24 cells per candidate

Criteria locked at module start (consistent with R1 v2):
- N: ✓ if mechanic present and complete; ⚠ specified with gaps; ✗ missing/undefined.
- E: ✓ depth without overhead; ⚠ depth with non-trivial bookkeeping; ✗ overhead exceeds depth.
- R: ✓ produces emergent variation; ⚠ uneven; ✗ homogenizing or dominant strategy.
- S: ✓ integrates without contradicting another rule; ⚠ adds new edge cases; ✗ contradicts canonical rule.

### C2.1 — Pure dice (cognitive only)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Stance UI is pure visualization; no new mechanic; Pirates!-style commit already adopted (E5). |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Combat Pool math (R2-L01) unchanged; Feint (R2-L03) provides cognitive player-skill precedent. |
| Vertical | ✓ | ✓ | ✓ | ✓ | C-only architecture preserved; no impact on A scene combat or mass scale. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Cross-system effects unchanged — no new skill-trigger surface for thread / social. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Pool/Stamina/Composure unchanged. |
| Horizontal | ⚠ | ✓ | ⚠ | ✓ | ⚠ on cinematic-genre expectation: videogame audience may expect Sekiro-class motor-skill engagement. Pure-dice may feel "underactive" mid-duel. |

**Verdict C2.1:** 22/24 ✓, 2 ⚠ on Horizontal (genre-expectation gap). Mechanically sound; cinematically conservative.

### C2.2 — Cap +1 net hit

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | Skill-check trigger spec needed (timing window vs pattern-read vs commit-anticipate). ⚠ Engineering surface added. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | +1 net hit is bounded; integrates cleanly with dice resolution math. Pool floor (R2-L06) unaffected. |
| Vertical | ✓ | ✓ | ✓ | ✓ | C-only; no propagation to A or mass. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Wound, Threadwork, Stamina interactions unchanged — skill check happens at resolution, doesn't propagate. |
| Lateral | ✓ | ✓ | ✓ | ⚠ | ⚠ Stamina-banking E6 already pre-commits the Heavy attack; layering a real-time check on top is double-pre-commit. |
| Horizontal | ✓ | ⚠ | ✓ | ⚠ | ⚠ E on tabletop fallback bookkeeping (Game Master must judge skill-check equivalent for table play). ⚠ S on cross-medium consistency. |

**Verdict C2.2:** 17/24 ✓, 7 ⚠. No ✗. Workable with tabletop-fallback specification.

### C2.3 — Cap +2 net hits

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ⚠ | ⚠ | Same spec needs as C2.2; ⚠ R because cap +2 is enough to flip outcome at low pool sizes — skill becomes strategically dominant for low-stat builds. |
| Bottom-up | ✓ | ✓ | ⚠ | ✓ | Cap +2 = ~6D equivalent; at 4D pool, skill contributes 51% (Section 5). Pool relevance halved at low end. |
| Vertical | ✓ | ✓ | ⚠ | ✓ | Cap +2 widens the C-vs-A gap; A non-skill encounters feel "less impactful" than C duels mechanically. |
| Diagonal | ✓ | ✓ | ⚠ | ⚠ | ⚠ on Threadwork interaction: a Practitioner duelist with skill +2 effectively bypasses some −1-D-per-Wound cost (Pool penalty offset by skill bonus). Cross-system asymmetry. |
| Lateral | ✓ | ✓ | ⚠ | ⚠ | Wager-stake range (R5) and skill-cap interact: at +2, low-stake duels resolve too decisively; mechanic crowds out canonical wager tension. |
| Horizontal | ✓ | ⚠ | ⚠ | ⚠ | Player skill compounds across campaign — practiced players keep advantage; tabletop fallback wider gap to manage. |

**Verdict C2.3:** 11/24 ✓, 13 ⚠. No ✗. Trends ⚠ across multiple axes — adopt at risk; specifically ⚠ R for stat-relevance at low pool.

### C2.4 — No cap (skill-resolves)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✗ | ✗ | ✗ | **E ✗:** real-time deflect window must be implementable in tabletop play — no obvious fallback. **R ✗:** skill-trumps-stat (Section 5: low-stat with skill beats high-stat without). **S ✗:** contradicts canon "TTRPG baseline; scales to Hybrid and Board Game" (R2-L02). |
| Bottom-up | ⚠ | ✗ | ✗ | ✗ | Bypasses Combat Pool math entirely on perfect deflect — Combat Pool formula (R2-L01) becomes irrelevant in C duels. |
| Vertical | ✗ | ✗ | ✗ | ✗ | C-only mechanic that bypasses canonical resolution; cannot scale to mass or even A. |
| Diagonal | ✗ | ⚠ | ✗ | ✗ | Threadwork −1D Pool per Wound becomes irrelevant in C duels because dice no longer determine outcome. Cross-system rules dormant. |
| Lateral | ⚠ | ⚠ | ✗ | ✗ | Wager-stake mechanic (R5), Stamina-banking (E6), and posture-as-yield (E7) all become moot — perfect deflect resolves the duel. |
| Horizontal | ✓ | ✗ | ✗ | ⚠ | "Cinematic feel" achieved at the cost of all canonical-math relevance. Combat Pool growth across campaign loses meaning in C. |

**Verdict C2.4:** N=✗ on 2, E=✗ on 4, R=✗ on 5, S=✗ on 5. **Categorical multi-axis fail. Reject.**

### Cross-candidate summary

| Candidate | N pass | E pass | R pass | S pass | Verdict |
|---|---|---|---|---|---|
| C2.1 Pure dice | 6/6 (1⚠) | 6/6 | 5/6 (1⚠) | 6/6 | **PASS — minor genre-expectation gap** |
| C2.2 Cap +1 | 5/6 (1⚠) | 4/6 (2⚠) | 6/6 | 4/6 (2⚠) | **PASS with tabletop-fallback spec** |
| C2.3 Cap +2 | 5/6 (1⚠) | 4/6 (2⚠) | 2/6 (4⚠) | 3/6 (3⚠) | **MARGINAL — risk of skill dominating at low pool** |
| C2.4 Uncapped | 1/6 (3✗) | 0/6 (4✗) | 0/6 (5✗) | 0/6 (5✗) | **REJECT — categorical multi-axis fail** |

---

## 7. Mode D — Edge case discovery

### Boundary
**EC-D2.B-01 [P2] (C2.2/C2.3):** At 4D pool (low-stat duelist), cap +2 increases expected net by 106% (Section 5). Skill-check pass rate becomes the *primary* outcome predictor. Stat differentiation collapses at low end.

**EC-D2.B-02 [P2] (C2.4):** Pool floor 5D (R2-L06) does not bind in C duels under uncapped — the Pool floor's protection is irrelevant when skill bypasses dice.

### Cascade
**EC-D2.C-01 [P3] (C2.2/C2.3):** Tabletop fallback ("Game Master judges narrative description") creates per-Game-Master variance. One Game Master grants +1 generously, another stingily; cross-table consistency degrades.

**EC-D2.C-02 [P2] (C2.4):** Once a player learns the deflect window, *every* C engagement skews toward auto-win. No counter-pressure mechanism unless Stamina-banking E6 + posture-as-yield E7 specifically interact with skill resolution — currently unspecified.

### Regression
**EC-D2.R-01 [P3] (any non-C2.1):** Player skill improving → players bait Architecture-C triggers (per Q5: T-Wager / T-Cultural / T-Boss / T-Thread / T-Hero-Officer / T-Honor-call) deliberately. C-trigger frequency increases mechanically, contrary to "default A, C as exception" framing.

### Deadlock
**EC-D2.D-01 [P3] (C2.2/C2.3):** Two skilled players in mutual C duel — both pass skill checks routinely; expected net advantage cancels. Returns to dice-driven baseline. Wasted complexity.

### Crunch cascade
**EC-D2.CR-01 [P2] (C2.2/C2.3):** Per-round real-time check + canonical Combat Pool resolution + Stamina tracking + posture-as-yield gauge + stance commit. Mid-duel cognitive load near or above sustainable for tabletop. Tabletop fallback simplifies but introduces medium asymmetry.

### Ambiguity
**EC-D2.A-01 [P1] (C2.2/C2.3/C2.4):** Skill-check trigger underspecified. Synthesis identifies three families (timing window / pattern-read / commit-anticipate); they are not interchangeable. Without choosing one, mechanic is undefined.

**EC-D2.A-02 [P2] (C2.2/C2.3):** When does skill check fire? Every round? Every Strike? Per-action? Per-zone? Spec gap.

### Incoherence
**EC-D2.I-01 [P1] (C2.4):** Direct contradiction with R2-L02 (TTRPG baseline). Cannot scale.

**EC-D2.I-02 [P3] (C2.2/C2.3):** Stamina-banking E6 is "pre-commit choice"; layering real-time check on top is "pre-commit + reactive" — operational meaning of "pre-commit" weakened.

### Optimal play
**EC-D2.O-01 [P1] (C2.4):** Player optimal: bait C-architecture triggers (Wager / Honor-call), then skill-check to victory regardless of stat. Combat Pool growth ceases to matter for duel-focused builds.

**EC-D2.O-02 [P3] (C2.2/C2.3):** Player optimal: build low-stat duelist + practice skill check; rely on cap +1/+2 to compensate. Caps prevent dominance per Section 5; effect is reasonable build-diversity, not degeneracy.

### Degenerate
**EC-D2.DG-01 [P3] (C2.1):** No skill layer → C duels are mechanically identical to A, just visually different. Pirates! commit-and-tell (E5) + posture-as-yield (E7) carry the differentiation. Acceptable per synthesis intent.

**EC-D2.DG-02 [P1] (C2.4):** Skill-check pass rate becomes only-relevant input. Stat-pool growth across campaign mechanically inert in C.

---

## 8. Decision-shape findings

**Recommendation: C2.1 (pure dice, cognitive layer only) — with explicit acknowledgment of the Horizontal genre-expectation gap.**

**Secondary fallback: C2.2 (cap +1) — if Jordan determines genre-expectation gap is unacceptable for the videogame medium.**

**Rationale:**

1. **C2.1 (pure dice) passes 22/24 NERS.** Only ⚠ on Horizontal (videogame-genre cinematic expectation). The Pirates!-style stance commit (E5, already adopted) and Sekiro posture-as-yield (E7, also adopted) carry C-distinctiveness without requiring real-time motor-skill. Stance UI as visualization is consistent with canon's pattern (UI presents canonical math; player choices are cognitive, like Feint per R2-L03).

2. **C2.2 (cap +1) passes NERS at full grain (no ✗) but adds spec surface.** Cap +1 leverage at typical pool sizes is 12–35% — impactful without degeneracy. Tabletop fallback requires Game-Master adjudication (parallels Stunt declaration R2-L04 with binary cap rather than +N up to 5).

3. **C2.3 (cap +2) is marginal.** Mechanically functional but trends ⚠ on R (stat relevance at 4D pool drops to 49%) and S (cross-system asymmetry with Threadwork penalty, Wager-stake range R5). Adopt only if Jordan deems C2.2 too subtle.

4. **C2.4 (uncapped) fails categorically.** Tabletop-incompatible (R2-L02), inverts canonical stat hierarchy (Section 5), nullifies Combat Pool math, makes Stamina-banking and posture-as-yield mechanically silent. Reject.

**Implementation under C2.1 (no new code, design-doc clarification):**

- Affirm Pirates!-style stance commit (E5) as cognitive-only mechanic — pre-commit choice + opponent counter-choice + canonical-dice resolution.
- Stance UI is visualization of the commit choices — not a separate skill-check surface.
- Posture-as-yield (E7) remains the duel-ender via canonical Stamina depletion.
- No new skill-input layer added.

**Decision-shape statement for Jordan ratification:**

> Architecture C duel resolves on canonical dice with Pirates!-style cognitive stance commit (E5) and Sekiro posture-as-yield (E7) endgame, both already adopted. No real-time motor-skill layer is added. Stance UI is visualization only. The genre-expectation gap (videogame audience may expect Sekiro-class motor-skill) is acknowledged as a Horizontal direction ⚠ but does not justify the categorical failures of C2.4 or the bookkeeping cost of C2.2/C2.3.

---

## 9. Module status

| Item | Status |
|---|---|
| Canonical sources fetched at full depth (PP-716) | ✓ |
| Verification ledger entries (6) | ✓ |
| sim_gate('custom', systems=['combat']) | (called at commit) |
| NERS full-grain analysis (96 cells) | ✓ |
| Mode A probability tables across pool sizes | ✓ |
| Mode D edge cases (12 across 9 categories) | ✓ |
| Decision-shape finding (C2.1 primary; C2.2 fallback) | ✓ |

**Module 2 status: verified.**
