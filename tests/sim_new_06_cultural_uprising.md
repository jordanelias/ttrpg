# SIM-NEW-06 — BG: Cultural Uprising Full Run (RM New Win Condition)
## Mode: C (Full Scenario) + A (Isolation) + D (Edge Cases)
## Date: 2026-04-08

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1431 lines)
victory_architecture_v1.md: ✓ (412 lines) — PP-460 RM redesign

---

## System Under Test

RM's new two-phase win condition (PP-460):
- Phase 1: CV ≤ 1 in ≥ 8 of 15 playable territories.
- Phase 2: Cultural Uprising of T9 Himmelenger. Weaver Thread pool vs Ob = TC ÷ 10 (round up, min 1, max 5). Prerequisite: RS ≥ 25.
- Win: T9 under RM administration + Phase 1 held × 2 Accounting steps.

Never tested — first run of the new mechanic.

---

## Mode A: Cultural Uprising Ob Calibration

**Ob formula: TC ÷ 10 (round up, min 1, max 5).**

| TC | Ob |
|----|-----|
| 1–10 | 1 |
| 11–20 | 2 |
| 21–30 | 3 |
| 31–40 | 4 |
| 41–50 | 5 (capped) |
| 51+ | 5 (capped) |

**Starting TC: 28 → Ob 3.** By S10 (TC ~38 assuming passive +1/season with Hafenmark suppression cancelling some): Ob 4. By S15 (TC ~43, post-AER 3 bypass): Ob 5 (capped).

**Weaver Thread pool:** RM's Weaver NPC. TS 18 (from params). Leap pool: Spirit + Attunement + History + TPS. TS 18 → TPS ≤ 1 (TS 18 < 30 threshold for standard Leap). Wait — Weaver at TS 18 cannot Leap at all (Leap requires TS ≥ 30).

**[GAP: RM's Weaver at TS 18 cannot Leap, yet the Cultural Uprising requires a Weaver Thread pool roll. Is the Uprising not a Thread operation in the traditional sense? Is the roll using a different pool?]**

**Ruling (gap-fill):** The Cultural Uprising is not a standard Thread Leap. It's a Community action driven by collective cultural force, not an individual practitioner's Thread skill. The pool for the Uprising roll is: **Presence markers in all territories at CV ≤ 1 (count) + 1D base.** This makes the Uprising's strength proportional to RM's accumulated cultural work — the more territories shifted, the stronger the Uprising roll. RS thresholds still apply (Co-Movement auto-effects fire as if it were a Thread-adjacent action).

Revised formula: **Pool = (count of territories at CV ≤ 1) × 1D + 1D base vs Ob = TC ÷ 10.**

**[EDITORIAL: ED-345 — Cultural Uprising pool undefined. Weaver TS 18 cannot Leap normally. Uprising pool should be defined as either: (a) collective Presence pool (1D per territory with RM Presence at CV ≤ 1, max 15D), or (b) Weaver pool only (if Weaver TS is raised by Warden interaction to TS 30+ by Phase 1 unlock). Option (a) is more narratively coherent — the Uprising is the people, not one practitioner. P1 — blocks Cultural Uprising adjudication.]**

---

## Mode C: Full Scenario — Cultural Uprising at Season 18

**Setup:** 5-player game, S18. Phase 1 condition just met (CV ≤ 1 in 8 territories at Accounting S17 — confirmed, just crossed threshold).

CV ≤ 1 territories (8): T3, T4, T6, T7, T10, T12, T13, T17. RM has Presence markers in all 8.
T9 (Himmelenger) CV: was 5 at start, now 2 (Church partially spread, Varfell Counter-Narrative fired twice against it). Not yet ≤ 1.

**TC at S18:** 28 + 17 passive (assuming Hafenmark suppressed 5 seasons, Church Asserted 8 seasons) ≈ 28 + 17 − 5 + 8 = **TC 48.** Ob = ceil(48÷10) = ceil(4.8) = **5 (capped).**

**RS at S18:** 72 − 17 (Weaving costs ~1/season) − 1 (baseline year-end decay × 4 years) ≈ **RS 51.** Above RS 25 prerequisite ✓.

**Uprising modifiers:**
- T9 CV = 2 (not ≤ 1): Ob −1 modifier does NOT apply.
- WC: 0 (Warden Emergence not fired): no +1D.
- TC 48 ≥ 50? No: 48 < 50 → TC modifier does NOT apply.
- Church Mandate 5 ≥ 5: **Ob +1** (Church actively suppresses).

**Final Ob: 5 (capped) + 1 (Church M5) = 6.** But Ob max from formula: cap is 5. Does the Church Mandate modifier push beyond the cap?

**Ruling:** The formula cap (max 5) applies to the TC ÷ 10 calculation. The Church Mandate modifier is a separate additive bonus. Final Ob = 6 is valid (Ob can go above the formula cap via modifiers; Ob cap of 20 from core rules applies universally). **Final Ob: 6.**

**Pool (using gap-fill: 1D per CV≤1 territory with Presence + 1D base):** 8 territories + 1 base = **9D vs Ob 6.**

9D vs Ob 6, TN 7. E(net) = 9 × 0.572 = 5.15. 
P(Overwhelming: net ≥ 12 AND ≥ 3): ~5%.
P(Success: net ≥ 6): ~35%.
P(Partial: 0 < net < 6): ~40%.
P(Failure: net ≤ 0): ~10%.
P(Failure or Partial combined): ~50%.

**Result (simulated): Partial.** Net 4, Ob 6 → 0 < 4 < 6 → Partial.
**Effect:** T9 does not transfer. CV in T9 −1 (4→... wait, T9 was at CV 2 entering Uprising, Partial drops it to 1). Uprising attempt used up for this arc.

**Post-Partial state:** T9 CV now 1. Uprising attempt exhausted until next arc. RM must hold Phase 1 for another arc before attempting again.

**Finding P1 — Partial Uprising is actually positive.** T9 CV dropped from 2 to 1. Next Uprising attempt: T9 CV = 1 → Ob −1 modifier NOW applies. Combined with one arc of additional territory Weaving (potentially 9–10 territories at CV ≤ 1 → pool 10–11D), next attempt is significantly stronger.

### Second Uprising Attempt (Season 22, next arc)

**Changes:**
- T9 CV 1: Ob −1 modifier applies.
- RM has 10 territories at CV ≤ 1 (one more territory Weaved during arc gap): pool **11D**.
- TC at S22: 48 + 4 seasons ≈ **TC 52.** Ob = ceil(52÷10) = ceil(5.2) = **6 (above cap, but cap is 5).** Wait — cap applies to TC component: TC ÷ 10 capped at 5. So TC contribution = 5 regardless of TC ≥ 51. Church Mandate modifier: Church M 5 → +1. T9 CV ≤ 1 modifier: −1. Net Ob: 5 + 1 − 1 = **5.**
- WC: still 0.

**Pool: 11D vs Ob 5.** E(net) = 11 × 0.572 = 6.3.
P(Overwhelming: net ≥ 10 AND ≥ 3): ~22%.
P(Success: net ≥ 5): ~62%.
P(Partial): ~20%.
P(Failure): ~8%.

**Result (simulated): Success.** Net 6, Ob 5 → 6 ≥ 5 → **Success.**
Effect: T9 transfers to RM administration. Church Mandate −1 → M 4.

**Win condition check at S22 Accounting:**
- T9 under RM administration ✓
- CV ≤ 1 in ≥ 8 territories: 10 territories ✓
- Must hold for 2 consecutive Accounting steps.

**S23: can Church disrupt?**
Church (M 4 post-Uprising) wants T9 back. Church Territorial Seizure on T9 (RM-held): Ob +3 (RM resistance mechanic). Church Seizure base Ob = 2 + Fort 2 + max(0, 3 − CV) = 2 + 2 + max(0, 3−1) = 6. Plus RM resistance +3 = **Ob 9.** Church M 4D vs Ob 9: P(Success): ~0.2%. **Essentially impossible.** Church cannot recapture T9 in one season.

**S23 Accounting: Phase 1 held (10 territories ≥ 8), T9 still RM. 2 consecutive steps met. RM wins.**

**Total game duration: S23 — RM wins in 23 seasons.**

---

## Mode D: Edge Cases

**Edge 1: RS drops below 25 before Uprising.**
If RS falls below 25 during Phase 1 hold, Uprising cannot be declared. RM is locked out of Phase 2. This creates a race: RM must Weave enough territories to trigger Phase 1 AND maintain RS ≥ 25. Weaving costs RS (~1/season per op). At 8+ Weavings/season near Phase 1: RS drain could be 8 RS/season. From RS 72: ~6 seasons to RS 25 if RM Weaves aggressively. RM must pace Weaving to preserve RS.

**Finding P2 — Aggressive Weaving to hit Phase 1 fast risks dropping RS below Uprising prerequisite.** RM faces a pacing constraint: Weave too fast → RS collapse → Uprising blocked. Weave slowly → other factions win first. Optimal pace: 2–3 Weavings/season (RS drain ~2–3/season), reaching Phase 1 around S15–18.

**Edge 2: Church takes T9 BEFORE RM declares Uprising.**
If Church reaches TC 75 and seizes T9 via Territorial Seizure, T9 is Church-controlled with high CV (Church keeps CV up in own territory). RM cannot easily Weave T9 down to CV ≤ 1 (Church will Piety Spread to counter), and the Uprising targets T9 regardless of who controls it. Uprising would need to unseat Church from T9 — the Ob formula still applies.

**Can RM do Cultural Uprising on a Church-seized T9?** Nothing in the mechanic restricts it to uncontrolled T9. The Uprising is a popular movement against institutional authority — it makes MORE sense if Church controls T9 (the Uprising is against Church occupation). RM can attempt Uprising on Church-held T9 with the same formula.

**Edge 3: Multiple Uprising attempts via arc cycling.**
The Uprising is once per arc (not once per game). If the game spans multiple arcs (~4–6 seasons each), RM could attempt 3–4 Uprisings. Each failed Partial attempt drops T9 CV by 1 — three Partial attempts convert T9 from CV 5 to CV 2, then Success becomes much easier (Ob −1 modifier from CV ≤ 1). The Partial failure outcome is actually a progress mechanism disguised as a setback.

---

## Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-CU-01 | P1 | Cultural Uprising pool undefined — Weaver TS 18 cannot Leap. Pool must be defined (recommended: 1D per CV≤1 Presence territory + 1D base). |
| F-CU-02 | P2 | Partial Uprising is effectively progress — drops T9 CV by 1, improving next attempt's Ob. The "failure" outcome has positive downstream effect. |
| F-CU-03 | P2 | Church seizure of RM-held T9 is near-impossible (Ob 9 via resistance clause). RM hold is effectively permanent once Uprising succeeds. |
| F-CU-04 | P2 | Aggressive Weaving to hit Phase 1 risks RS < 25 (Uprising blocked). RM must pace at 2–3 Weavings/season to preserve RS. |
| F-CU-05 | P3 | Multiple arc Uprising attempts (Partial → Partial → Success) is a valid and narratively coherent path. Each Partial converts T9 CV −1 for free. |

