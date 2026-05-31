# LPS-2e + Size-Weighted Mandate — Comprehensive NERS Audit (All Directions)

**Scope:** the faction-resolution surface this session changed — per-settlement L/PS (LPS-2e grain),
Settlement Weight, the size-weighted saturating Mandate aggregation, the Mandate↔settlement feedback,
per-settlement Church L-strip effects, and the F-RESID Unique-Action migration.
**Instrument:** `valoria-resolution-diagnostic` Stage 1–4 + NERS + all six directions
(top-down / bottom-up / vertical / diagonal / lateral / horizontal).
**Date:** 2026-05-30 · **HEAD:** b339335c · **Method:** bottom-up from fetched canon, sim-confirmed.

`[SELF-AUTHORED — bias risk]` Every item here was built by me this session. Counter-measures applied:
the size property is instrumented numerically and reported where it does **not** robustly hold; the prior
session's "size test passes (6 vs 5)" claim is re-examined and found **value-dependent**; my own Settlement
Weight is flagged as possibly over-built. The 2026-05-30 faction-sigma audit covered the *pre*-LPS-2e faction
layer; this audit is scoped to the new grain + size mechanic + migration (the surface that audit predates).

---

## VERDICT (worst-first, no false balance)

**NERS-COMPLIANT AS BUILT — no hard mechanical defect.** The diagnostic found no unbounded loop, no
foreclosure wall, no accidental cliff, and no broken formula: the conquest snowball is bounded (saturation +
the 0–7 cap), the collapse spiral is floored (resolver 0.05), the Mandate↔settlement feedback is mean-reverting
and convergent, the per-settlement Church L-strip is bounded (−1 settlement = −1 aggregate L), and faction
actions resolve with uniform +10pp/pt impact, a 0.05 floor, and a 0.90 cap. **Three items need a Jordan call —
none blocking:**

- **[INTENT — confirm, P2] The "few huge > many small" property is value-dependent.** The size-weighted
  Mandate is a *pure total-population-mass* model. 12 moderate villages (ΣW≈36) **out-mass** 3 large settlements
  (ΣW≈26) and tie/edge them at Mandate 6; equal mass ties exactly (5=5). The prior session's reported "6 vs 5"
  used favorable values. This is **correct** if Mandate should track total population (more people wins, however
  distributed); it is a **defect** if a huge capital should carry a *super-linear* premium beyond its mass.
  The current Weight range (1–11) makes "few huge > many small" hold only when W_huge > ~4·W_small.
- **[N / Lesson-1, P2] Settlement Weight may double-count development.** `W = base(Type) + Prosperity +
  FacilityTier`. Prosperity (0–5) and FacilityTier (0–3) both rise with investment → likely positively correlated
  → partial double-counting of "development." Unmeasurable without the 37-settlement registry values; if the
  correlation is high, Weight could collapse to fewer terms (improves N and E).
- **[E — reservation, P3] The size mechanic is the elegance cost.** Weight (3 terms) + the saturating formula +
  the K=6 constant: a player can intuit the *direction* (more/bigger/richer → higher Mandate) but not the
  *magnitude* (saturation, K). As simple as the intent allows, but the least-elegant link in an otherwise-linear
  chain. K=6 is sim-calibrated, not principle-derived (a tunable).

---

## THREE-CATEGORY CLASSIFICATION (load-bearing)

| Quantity | Category | Lessons that apply |
|---|---|---|
| L, PS (per-settlement, 0–7) | **Base parameter** | 2, 3 (feed Mandate; not rolled bare) |
| Settlement Weight W (base+Prosperity+FacilityTier) | **Derived base-parameter composite** | 1 (role overlap), 2 |
| Mandate (faction headline, 0–7, derived-by-aggregation) | **Base parameter** (functions as resolver margin) | 2, 3 |
| Mandate aggregation `clamp(round(7·T/(T+K)))` | **Deterministic accounting** | 6 (cliffs); exempt from 2 (deliberate absolute) |
| Legitimacy meter (Mandate×20 buffer) | **Continuous resource** | 2, 6 |
| Mandate↔settlement feedback | **Feedback loop** | 5 |
| Church L-strip (−1 L/settlement) | **Deterministic modifier on a base param** | 5, 6 |
| Faction actions (Domain + migrated Unique) | **Dice → d+σ resolver** | 2, 3, 4 |

---

## STAGE 1 — DIAGNOSTIC (Phase 0–6)

**Phase 0 (decompose).** Composite: (A) deterministic accounting — Weight, Mandate aggregation, Legitimacy
buffer; (B) resolver-resolved — faction actions; (C) feedback — Mandate↔settlement.

**Phase 1 (stress points).** N=0 settlements (Restoration start) → Mandate 0; N=1 (embedded Löwenritter) →
low graded Mandate; weak actor (Mandate 1) acting; Weight extremes (undeveloped Outpost W=1 → developed Seat
W=11, a 5–11× spread). The aggregation is deterministic → **no small-pool dice variance in the aggregation
itself** (the historical small-pool defect lived in the bare-stat ROLL, now the resolver).

**Phase 2 (what the stress decides).** A small holding produces a low-but-**graded** Mandate (0–7), which feeds
the resolver as a margin — **not a fragile binary**. The size-weighted Mandate + d+σ resolver + 0.05 floor
together are the architectural fix: a weak/small faction is hard-but-not-impossible, never a coin-flip on a
near-irreversible outcome.

**Phase 3 (effect curves).**
- *3a impact uniformity.* The resolver delivers a constant +10pp/stat-point across the whole 1–7 range
  (the σ-leverage fix; confirmed M=−4..+4 → uniform +10pp). PASS.
- *3b cliffs.* Mandate's `round()` quantizes a continuous aggregate to an integer 0–7 — inherent to a bounded
  integer stat, not an accidental cliff. A marginal settlement change can flip Mandate ±1 (→ ±10pp on all
  actions via the resolver); bounded (±1) and inherent to integer stats. The Legitimacy buffer degrades
  continuously (no cliff). PASS (note: the quantization is the one sensitivity point).
- *3c role conflation.* L and PS are split at the **settlement** level (two variables, two roles — correctly
  placed); Mandate is the single faction aggregate (one headline). No harmful conflation — the §5.2
  "one number, two roles" concern is resolved by placing the split at settlement scale.

**Phase 4 (loops — all directions, highest severity).**
- *Mandate↔settlement feedback* (negative/mean-reverting, ±1/season): **damped + convergent** (sim: q=2 under
  Mandate 5 → converges to ~5 in 2 seasons, no oscillation). Damper present, gain<1. BOUNDED. ✓
- *Conquest snowball* (diagonal, cross-system: faction action → settlement gain → higher T → higher Mandate →
  more wins): **bounded** by (i) the 0–7 Mandate cap, (ii) the saturating aggregation `T/(T+K)` (sim:
  Mandate 4→5→6→6→6→6 across n=1→12 strong settlements — marginal settlements stop raising it), and (iii) the
  resolver 0.90 cap (a dominant faction still fails 10%). **The saturation is itself a damper on the snowball** —
  a strength of the size-weighted form (Lesson 5; bounds the `intent_of_game` positive loop). ✓
- *Collapse spiral* (lose settlements → lower Mandate → weaker → lose more): **floored** by the resolver 0.05
  (a Mandate-1 faction's pivotal action is 5%, not 0%) + the §1.4/§1.3 Stability recovery + one-time collapse
  immunity. BOUNDED. ✓
- *Church L-strip*: −1 L per controlled settlement = −1 to the W-weighted aggregate L = ~−0.5 Mandate;
  bounded, not a runaway (per-settlement ruling is mechanically clean). ✓

**Phase 5 (intent gate).** Size-weighted Mandate (deliberate, Jordan ruling; safeguard = saturation + clamp →
pass); per-settlement L-strip (deliberate; safeguard = −1 aggregate bound → pass); resolver floor/cap
(deliberate ED-865/874; the floor IS the foreclosure safeguard → pass). **One item `[INTENT UNDETERMINED]`:**
whether Mandate should be *pure population-mass* or carry a *super-linear hugeness premium* — Jordan stated
"huge-population province > many-few-people provinces," which the mass model satisfies only for sufficient
weight contrast. Carried as a true finding (the V-1 finding above).

**Phase 6 (score).** No P1. P2: the hugeness-premium intent + the Weight redundancy. P3: the elegance cost.

---

## STAGE 2 — SIX-LESSON TEST

| Lesson | Result |
|---|---|
| **1 — one variable, one role** | L/PS split at settlement = correct. **Watch:** Weight's Prosperity+FacilityTier may overlap (the only Lesson-1 flag). |
| **2 — uniform-impact steps** | Resolver = constant +10pp/pt ✓. Mandate aggregation is a *deliberate, bounded absolute* effect (size-mass) — exempt; legibility-flagged under E. |
| **3 — dice only on healthy pools** | The pivotal faction roll is the d+σ resolver (graded, floored), **not** a bare small pool ✓. |
| **4 — route small rolls through a deep clock** | N/A — the resolver replaced the small roll; Mandate is a deterministic aggregate, not a roll. |
| **5 — no undamped+unbounded loop** | Feedback mean-reverting+capped ✓; conquest snowball saturation+cap-damped ✓; collapse spiral floored ✓. |
| **6 — continuous degrade, no stacked cliffs** | Legitimacy buffer continuous ✓; Mandate quantization is inherent integer-stat granularity, not a stacked accidental cliff ✓. |

---

## STAGE 3 — NERS VERDICT

```
SYSTEM: LPS-2e per-settlement L/PS + size-weighted Mandate + per-settlement Church effects + F-RESID resolver migration
COMPONENTS: deterministic accounting (aggregation, buffer) + d+σ resolver (actions) + mean-reverting feedback
VERDICT: NERS-COMPLIANT AS BUILT — no hard mechanical defect; 2 intent/calibration confirmations + 1 elegance reservation for Jordan.

N: pass (flag) — nothing redundant in the grain/resolver; the size mechanic is necessary (Jordan intent).
   FLAG: verify Settlement Weight's Prosperity+FacilityTier are not double-counting development (Lesson-1).
R: pass — holds at extremes (N=0→0, N=1→low graded, large→bounded 7); no fragile small-pool binary
   (resolver graded+floored); loops bounded (conquest saturation-damped, collapse floored, feedback convergent);
   modifiers uniform-impact; Church L-strip bounded. The "few huge > many small" property is robust *as a
   mass model* — see the intent confirmation (it is value-dependent vs Jordan's wording, not a mechanic failure).
S: pass — settlement→faction rollup consistent with Treasury=Σ(Prosperity)×10; resolver consistent with the
   deterministic spine and across all faction actions; clean across scales (settlement→faction→peninsula);
   Legitimacy meter consistent with sibling meters. Note: the saturating aggregation is the one non-linear link.
E: pass (reservation) — L/PS split + single Mandate headline + the 50%+10·M resolver are highly legible.
   RESERVATION: the size-weighted Mandate (Weight composite + saturation + K=6) is the elegance cost of the
   size mechanic — direction intuitable, magnitude not. As simple as the intent allows; K=6 is a tunable.

REMEDIATION (worst-first):
  P2 [INTENT]  "few huge > many small" value-dependent → CONFIRM with Jordan: pure population-mass (current,
               correct) vs super-linear hugeness premium (widen Weight range / add a per-settlement size term).
  P2 [N/L-1]   Weight Prosperity+FacilityTier overlap → measure correlation against the 37-settlement registry;
               if high, collapse Weight to fewer terms.
  P3 [E]       Saturation/Weight opacity + K=6 magic constant → optional: simpler Weight, or surface Mandate
               drivers in-UI; tune/justify K. Not required (the overhead serves the necessary size intent).
```

---

## STAGE 4 — RE-TEST OF (POTENTIAL) FIXES

No fix is applied here (no hard defect), but the two candidate remediations are pre-tested against the pipeline:

- **Collapse Weight to fewer terms** (if Prosperity+FacilityTier are redundant). Re-test: must NOT lose the
  infrastructure-investment signal Jordan named as a driver. If FacilityTier is dropped, Prosperity must still
  capture "developed → heavier." Risk: under-weights a fortress/cathedral that is low-Prosperity but
  high-infrastructure → keep a type/infrastructure term. `[OPEN — needs registry data]`.
- **Add a super-linear hugeness premium** (if Jordan wants "few huge >> many small"). Re-test: a convex weight
  (e.g., W² or a capital multiplier) re-introduces a snowball risk — the saturation must still bound it.
  Likely fine (saturation + 0–7 cap hold), but re-sim before adopting. `[OPEN — Jordan intent]`.

Both are **Jordan-gated** (one needs data, one needs an intent ruling); neither is a defect requiring action now.

---

## ALL-DIRECTIONS COVERAGE

- **Top-down** (serves the whole?): the size-weighted Mandate makes settlement/territory growth feed political
  power, **bounded** so it doesn't runaway — directly serves `intent_of_game` (emergent narrative: build a
  populous heartland → political dominance, with diminishing returns). STRENGTH. The hugeness-premium question
  is the open top-down item.
- **Bottom-up** (primitives assemble?): per-settlement L/PS + Weight terms aggregate into Mandate correctly
  (sim-validated). STRENGTH. The Weight-redundancy flag is the open bottom-up item.
- **Vertical** (across scales): settlement (L/PS) → faction (Mandate) → peninsula (victory clocks) — clean
  handoffs, no friction at the category boundaries. PASS.
- **Diagonal** (cross-system): faction Mandate ↔ Church L-strip ↔ combat (muster) ↔ territory (settlement
  acquisition) — the conquest loop is bounded, the collapse spiral floored. PASS (the highest-value check).
- **Lateral / horizontal** (sibling systems): Mandate aggregation consistent with Treasury = Σ(Prosperity)×10;
  the d+σ resolver consistent across every faction action (Domain + migrated Unique); the Legitimacy meter
  consistent with the sibling faction meters (Reputation ×15, Discipline ×10, Treasury ×100). PASS.

---

## PROVENANCE (`[READ:]` trail)

- `[READ: designs/territory/settlement_layer_v30.md §1.1–1.4.1, §1.8 (LPS-2e) — Weight, aggregation, feedback]`
- `[READ: designs/provincial/faction_behavior_v30.md §2/§3.4/§3.5/§3.6/§4; faction_canon_v30.md §3.4/§5/Excommunication]`
- `[READ: params/factions/stats_1_7_scale.md §Domain Action Resolution (d+σ resolver) + §Unique Actions]`
- `[READ: designs/scene/derived_stats_v30.md §3 (per-system multipliers) + §8 (Mandate/Legitimacy)]`
- `[READ: engine/sigma_leverage_engine_armature.md; designs/audit/2026-05-30-faction-sigma-engine-audit/* (prior faction NERS)]`
- `[VERIFIED: sim this session — Weight range, conquest saturation curve, Jordan size test (value-dependence found),
   equal-mass tie, resolver floor/cap, mean-reverting feedback convergence, Prosperity/FacilityTier redundancy probe]`
- `[CONFIDENCE: high on the mechanical verdict (loops/floors/cliffs traced + sim-confirmed); the two P2 items are
   INTENT/DATA confirmations for Jordan, not mechanical failures — flagged as such, not resolved.]`
- `[SELF-AUTHORED — bias risk: corrected the prior session's "size test passes 6 vs 5" to value-dependent;
   flagged my own Weight composite as possibly over-built.]`
