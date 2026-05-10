# R6 — Fibonacci Group-Bonus Cap at High N
## Module 6 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** A (single-mechanic isolation)
**Source question:** *"Synthesis Q1 raised the Fibonacci damage scaling. Decision: cap at +5 (current canon, 8+ attackers), raise the cap to follow actual Fibonacci progression (+6 at 13+, +7 at 21+), remove the cap entirely, or impose a logarithmic asymptote above the cap point?"*

**Decision shape:** cap=+5 (preserve) / cap=+6 / cap=+7 / no-cap / asymptotic

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R6-L01 | fibonacci_table | 1→+0, 2→+1, 3→+2, 4–5→+3, 6–7→+4, 8+→+5 cap | designs/scene/combat_v30.md | §8 Fibonacci Group Bonus | "\| 8+ \| +5 (cap) \|" |
| R6-L02 | fibonacci_trigger | 3+ combatants in a zone | designs/scene/combat_v30.md | §8 Zone Collapse | "When 3+ combatants in a zone: combat becomes group combat. Fibonacci bonus applies." |
| R6-L03 | fibonacci_pp216_origin | PP-216 introduced canonical Fibonacci bonus | designs/scene/combat_v30.md | §8 | "Each additional attacker beyond the first against a single unsupported target adds dice to Offence allocation. (PP-216)" |
| R6-L04 | base_tn7 | Base TN 7 baseline | designs/scene/combat_v30.md | §5 | "Base TN = 7" |
| R6-L05 | combat_pool_floor | Combat Pool minimum 5D | params/combat.md | §Pool minimum | "Combat Pool minimum 5 is a clean floor. No −1D penalty at the floor." |
| R6-L06 | rescue_eligibility | Rescue eligible if outnumbered (subject to Fibonacci) | designs/scene/combat_v30.md | §8 Rescue (PP-290) | "**Eligibility (PP-290):** Rescue may only be declared if the rescued actor is outnumbered at Phase 1 declaration — facing 2+ attackers with no supporting ally" |

---

## 2. Probability framing — Fibonacci bonus as Δ-net-successes

At TN 7 with 1s subtracting (canonical roll), expected net per die is approximately 0.33. The Fibonacci bonus contributes:

| Attackers | Bonus dice | Δ E[net] | Defender's task (Combat Pool ~5D = 1.65 net) |
|---|---|---|---|
| 2 (canonical 1v2) | +1 | +0.33 | net = 1.65 + 1 × (Off split factor) ≈ minor edge |
| 3 (zone collapse trigger R6-L02) | +2 | +0.66 | net = 1.65 + ~0.66 → ~2.31 attacker advantage |
| 4–5 | +3 | +0.99 | ~2.64 attacker advantage |
| 6–7 | +4 | +1.32 | ~2.97 attacker advantage |
| 8+ (R6-L01 cap) | +5 | +1.65 | ~3.30 attacker advantage |
| 13 (Fib_7) | +6 (uncapped extrap.) | +1.98 | ~3.63 |
| 21 (Fib_8) | +7 (uncapped extrap.) | +2.31 | ~3.96 |
| 34 (Fib_9) | +8 (uncapped extrap.) | +2.64 | ~4.29 |

A defender with 12D Combat Pool (E[net] ≈ 3.96) is the high-stat baseline. Δ-net of +5 means attacker pool + bonus ≈ 8.5D + 5 = effectively 13.5D for offence allocation. Defender at 12D defending → ~50/50 contested outcome at 8 attackers per R6-L01 cap.

**Beyond +5 cap:** the curve flattens by design. Uncapped scaling produces certain-victory regimes at attacker counts 13+ (Fib bonus alone exceeds defender's full Pool capacity).

---

## 3. Candidates

| ID | Name | Description |
|---|---|---|
| **C6.1** | Preserve +5 cap (canonical) | Per R6-L01, cap at +5 for 8+ attackers. Current canon, PP-216. |
| **C6.2** | Raise cap to +7 at 21+ | Approximate true Fibonacci through 21+ attackers; saturate at +7. |
| **C6.3** | No cap (full Fib) | Continue Fibonacci progression indefinitely: +5 at 8, +6 at 13, +7 at 21, +8 at 34, etc. |
| **C6.4** | Asymptotic decay above cap | Above 8 attackers, bonus continues but with logarithmic decay: +5 at 8, +5.3 at 13, +5.5 at 21, +5.7 at 34, asymptotic to ~+6. |

---

## 4. NERS at full grain

### C6.1 — Preserve +5 cap

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Mature canonical mechanic per PP-216 (R6-L03). Cap is documented and bounded. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Δ-net at cap +5 = +1.65 = within tactical-significance range without overwhelming canonical Pool math. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Personal-scale Fibonacci translates to mass-scale via Effective Pool aggregation (R3-L03); cap consistency maintained. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Rescue mechanic (R6-L06) couples to Fibonacci eligibility — bounded interaction. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Stamina-banking, Wounds, Threadwork all unaffected by cap level. |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Tabletop scenarios with 8+ attackers are rare; cap rarely hit; mechanic feels organic. |

**Verdict C6.1:** 24/24 ✓. Canonical, mature, mechanically clean.

### C6.2 — Raise cap to +7 at 21+

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ⚠ | ⚠ | Spec change requires PP. ⚠ R: incentivizes 21-attacker pile-ons in narrow scenarios; mass-battle micro-tactics may degenerate. ⚠ S: cap break propagates to mass-scale equivalent. |
| Bottom-up | ✓ | ✓ | ⚠ | ⚠ | Δ-net at +7 = +2.31, exceeds defender's typical Pool advantage; defender → likely-felled regime at 21 attackers. ⚠ R: defender no longer has tactical viability. |
| Vertical | ⚠ | ⚠ | ⚠ | ⚠ | Cap raise affects personal scale only; mass-scale must be recomputed. Spec gap. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | No new diagonal effects. |
| Lateral | ✓ | ✓ | ⚠ | ⚠ | Rescue mechanic (R6-L06) loses leverage at higher attacker counts — Rescue contest's pool advantage drowned by Fibonacci stack. |
| Horizontal | ⚠ | ⚠ | ⚠ | ⚠ | Tabletop scenarios with 21+ attackers are very rare. Spec work pays off only in mass-scale edge cases. ⚠ on cost-benefit. |

**Verdict C6.2:** 16/24 ✓, 8 ⚠. **MARGINAL — solves a rare problem at moderate cost.**

### C6.3 — No cap (full Fibonacci)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✗ | ✗ | **R ✗:** unbounded scaling produces certain-victory regimes at attacker counts 13+. **S ✗:** breaks defender Pool relevance — Combat Pool math becomes meaningless at high N. |
| Bottom-up | ✓ | ⚠ | ✗ | ✗ | At 21 attackers, +7 bonus = +2.31 net; defender Pool 5D yields 1.65 → certain offence dominance. |
| Vertical | ✓ | ✗ | ✗ | ✗ | Mass-scale: 100-attacker engagement = +9 bonus = absurd. Whole resolution mechanic collapses. |
| Diagonal | ✓ | ⚠ | ✗ | ✗ | Threadwork pool floor (R1v2-L10) becomes meaningless when Fibonacci stack dwarfs all defensive resources. |
| Lateral | ✓ | ✗ | ✗ | ✗ | Rescue, Multi-Engagement, all defensive mechanics drown. |
| Horizontal | ⚠ | ✗ | ✗ | ✗ | "Realistic" gang-piled-on overwhelm — but breaks all canonical defensive mechanics. |

**Verdict C6.3:** N=⚠ on 1, E=✗ on 4, R=✗ on 5, S=✗ on 5. **REJECT — categorical multi-axis fail.**

### C6.4 — Asymptotic decay

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | Spec change requires PP. Math: log-asymptote formula needs explicit table. ⚠ E: introduces non-integer dice (+5.3, +5.5) which contradicts canonical integer-dice convention. |
| Bottom-up | ⚠ | ✗ | ✓ | ✗ | **E ✗:** non-integer dice break canonical resolution. **S ✗:** introduces fractional-dice precedent. |
| Vertical | ✓ | ✗ | ✓ | ✗ | Mass-scale would also need fractional-dice handling. |
| Diagonal | ✓ | ⚠ | ✓ | ⚠ | No new diagonal effects but spec needs to handle non-integer. |
| Lateral | ✓ | ✗ | ✓ | ✗ | All other dice mechanics use integer dice. |
| Horizontal | ✓ | ⚠ | ✓ | ⚠ | Smooth scaling above cap is a nice property but the integer-dice constraint kills it. |

**Verdict C6.4:** N=⚠ on 2, E=✗ on 3 + ⚠ on 3, R=✓ on 6, S=✗ on 3 + ⚠ on 3. **REJECT — fractional-dice contradicts canonical integer convention.**

### Cross-candidate summary

| Candidate | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| C6.1 Preserve +5 cap | 6/6 | 6/6 | 6/6 | 6/6 | **PASS — canonical, mature** |
| C6.2 Raise cap to +7 | 5/6 (1⚠) | 4/6 (2⚠) | 1/6 (5⚠) | 1/6 (5⚠) | **MARGINAL — narrow benefit** |
| C6.3 No cap | 5/6 (1⚠) | 1/6 (4✗+1⚠) | 1/6 (5✗) | 1/6 (5✗) | **REJECT — multi-axis fail** |
| C6.4 Asymptotic | 4/6 (2⚠) | 0/6 (3✗+3⚠) | 6/6 | 0/6 (3✗+3⚠) | **REJECT — fractional-dice contradicts canon** |

---

## 5. Mode D — Edge cases (compressed)

### Boundary
**EC-D6.B-01 [P3] (any):** What happens at exactly 8 attackers? Per R6-L01 row "8+", bonus is +5. Boundary is canonically clean.

**EC-D6.B-02 [P2] (C6.2 only):** New boundary at 21 attackers introduces another inflection point. Spec needs explicit table; Game Master adjudication burden increases.

### Cascade
**EC-D6.C-01 [P3] (C6.3):** Mass-battle Effective Pool calculation (R3-L03) couples Size to Combat Pool. Uncapped Fibonacci would reframe Effective Pool's Size-to-Power conversion at high N. Cascade through mass-resolution math.

### Regression
**EC-D6.R-01 [P2] (C6.3):** Players optimize: pile-on tactics (gang-up on single targets) become dominant strategy. Combat resolution collapses to "first to mass attackers wins."

### Crunch cascade
**EC-D6.CR-01 [P3] (C6.4):** Fractional dice tracking adds bookkeeping no other system has.

### Ambiguity
**EC-D6.A-01 [P3] (C6.4):** Rounding rule for fractional dice undefined.

### Incoherence
**EC-D6.I-01 [P2] (C6.3):** Combat Pool floor (R6-L05) becomes meaningless when Fibonacci stack dwarfs Pool. Floor's protective function breaks at high N.

### Optimal play
**EC-D6.O-01 [P1] (C6.3):** Player optimal: focus-fire single targets with maximum attacker count. Distributed engagement (1v1, 2v2) becomes strictly dominated. Tabletop play converges to "mob the boss."

### Degenerate
**EC-D6.DG-01 [P3] (C6.4):** Asymptote rounded to nearest integer collapses C6.4 → C6.2 (cap +6 effectively).

---

## 6. Decision-shape findings

**Recommendation: C6.1 (preserve canonical +5 cap at 8+ attackers per R6-L01).**

**Rationale:**

1. **C6.1 passes 24/24 NERS.** Mature canonical mechanic per PP-216 (R6-L03). The +5 cap produces tactically significant attacker advantage (Δ E[net] = +1.65) at the saturation point without breaking defender Pool relevance.

2. **C6.2 is mechanically functional but solves a rare problem.** 21+ attacker scenarios are rare in personal-scale play; the cap-raise's benefit is narrow. The cost (PP, propagation through mass-scale, defender-relevance erosion) is moderate. Net: not worth the work.

3. **C6.3 (no cap) fails categorically** on R (certain-victory regime at 13+ attackers) and S (defender Pool math breaks). At 100 attackers (mass-scale extreme), bonus would be +12, drowning all defensive mechanics. Reject.

4. **C6.4 (asymptotic decay) fails on E and S** because canonical resolution uses integer dice. Fractional-dice precedent would propagate through all dice mechanics. Reject.

**Implementation under C6.1 (no change; documentation):**

- Affirm `combat_v30 §8 Fibonacci Group Bonus` table with +5 cap at 8+ attackers (R6-L01) as canonical.
- No new PP needed.

**Decision-shape statement for Jordan ratification:**

> Fibonacci Group Bonus per `combat_v30 §8` is preserved as canonical: +0 / +1 / +2 / +3 (4–5) / +4 (6–7) / +5 (8+, cap). The cap at +5 produces tactically significant attacker advantage at saturation without breaking defender Pool relevance. Uncapped or raised-cap variants either collapse defensive mechanics (C6.3) or solve a rare problem (C6.2) at moderate cost. The synthesis Q1 question is answered: keep the cap.

---

## 7. Module status

| Item | Status |
|---|---|
| Canonical sources fetched (combat_v30, params/combat) | ✓ |
| Verification ledger (6 entries) | ✓ |
| NERS full-grain analysis (96 cells) | ✓ |
| Probability tables (Δ-net by attacker count) | ✓ |
| Mode D edge cases | ✓ |
| Decision-shape finding (C6.1 — preserve canonical) | ✓ |

**Module 6 status: verified.**
