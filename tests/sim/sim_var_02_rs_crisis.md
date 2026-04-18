# SIM-VAR-02 — TTRPG: Threadwork at RS 22 Crisis Conditions
## Mode: A (Mechanic Isolation) + C (Full Scenario) + D (Edge Cases)
## Date: 2026-04-08 | Finding F-58 stress test

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_threadwork.md: ✓ (613 lines)
params_core.md: ✓ (161 lines)
params_board_game.md: ✓ RS threshold table confirmed

---

## Context

F-58 (SIM-X-14): RS 22 is 2 points from the RS 20 Dormant threshold — any failed Weaving at this RS crosses into Dormant globally. This simulation stress-tests what RS 22 conditions mean for practitioners, specifically:
- Whether any Thread operation remains viable
- Whether Mending is net-positive (does RS gain from Mending outpace the operation cost?)
- Cascade risk from Dissolution attempt at RS 22

**Starting conditions:** RS 22. Active practitioner: Maret Uln (Varfell agent, TS 50, Attunement 4, Spirit 3, Focus 4, Cognition 3). Single practitioner, no collective.

---

## Mode A: RS 22 — All Operation Costs

**RS threshold at 22:** Band 19–1 ("Critical").
Per RS threshold table:
- Proximity 0 (Askeheim T15): +2 Ob Mending; beings present; Gaps (1d3 per season)
- Proximity 1 (T6 Stillhelm, T13 Oastad): +1 Ob all; Gaps (1d10: 1–4 = Gap fires)
- Proximity 2 (T5, T12): +1 Ob Thread; Gaps (1d10: 1–2)
- Proximity 3–5: Shifting Objects or lesser

**Global effects at Critical RS:** All Thread operations +1 Ob worldwide. Seasonal Stability checks Ob 1 (failure: faction Mandate −1).

Maret is operating in T13 (Oastad, Proximity 1). Her Ob modifiers:
- +1 Ob all actions (Proximity 1 at Critical RS)
- +1 Ob Thread operations (global Critical effect)
- Total Thread op Ob bonus: +2 Ob on all operations in T13 at RS 22

**Leap Ob for Maret (TS 50, Ob 1):** +2 Ob from RS = **Ob 3**.
Leap pool: Spirit (3) + Attunement (4) + History bonus (assume 1) + Thread Pool Score (TS 50 → TPS = TS÷10 = 5) = **13D**.
13D vs Ob 3, TN 7. E(net successes at 13D) ≈ 13 × 0.40 × 1.43 ≈ 7.4 net. P(≥3 net) ≈ 99.9%. 

**Finding: Maret's Leap at RS 22 remains essentially guaranteed.** High TS practitioners are insulated from RS-caused Ob increases on Leap because their pool is so large. A low-TS practitioner (TS 30, pool ~5D) at RS 22 in Proximity 1: Leap Ob 3, pool 5D. P(≥3 net at 5D Ob 3) ≈ 15%. Near-unworkable. RS 22 blocks low-TS practitioners entirely. High-TS practitioners are barely inconvenienced on Leap.

---

## Mode A: Mending at RS 22 — Net RS Gain Assessment

**Goal:** Determine whether Mending is net-positive at RS 22, or whether the operation cost erodes RS faster than Mending restores it.

**Mending operation costs (from params_threadwork.md):**
- Mending Success: RS +1
- Mending Overwhelming: RS +2
- Mending Failure: RS cost (typically −2 to −4 for personal scale, depending on Dissolution table row)

Actually: Mending is not a Dissolution — Mending is its own operation type. Mending RS cost = Mending failure consequence. Let me use what's in params: "Mending Success: +1. Mending Overwhelming: +2." The cost is the operation's auto-effect on Leap + Co-Movement, not a separate Mending failure cost.

**Mending Ob:** At RS 22, Proximity 1 = +1 Ob all, +1 Ob Thread global = base Mending Ob + 2.
Mending base Ob: Ob 2 (standard) + 2 = **Ob 4**. At Proximity 0 (T15): +2 Ob Mending specifically (Critical band rule) + 2 global = **Ob 6** in Askeheim.

**Maret Mending in T13 (Proximity 1):** 13D vs Ob 4. E(net) ≈ 7.4. P(OW: net ≥ 8 AND ≥ 3) ≈ 85%. P(Succ): ~12%. P(Partial/Fail): ~3%.

Expected RS per Mending in T13: (0.85 × +2) + (0.12 × +1) + (0.03 × some_cost) ≈ +1.70 + 0.12 − small = **~+1.80 RS per Mending at T13**.

Auto-effect from Leap + Co-Movement: each Thread op triggers Co-Movement card draw (Version C: temporal + epistemic + d6). Expected RS cost from Leap auto-effect ≈ −0.5 to −1 per scene (probabilistic).

**Net RS per Mending session in T13: approximately +0.8 to +1.3 RS.** Mending is net-positive at RS 22 for a TS 50 practitioner in Proximity 1. 

**But:** RS 22 is 2 from Rupture-adjacent Dormant threshold. Each Mending moves RS only ~+1. To get RS from 22 back to 40 (minimum viable): 18 Mendigs needed. At one operation per scene, one scene per session: 18 sessions. This is months of in-game time.

**Finding P1 — Recovery from RS 22 is technically possible but represents a multi-arc commitment.** No emergency recovery exists. The game can continue but the RS clock is effectively a slow death unless:
1. Multiple practitioners Mend simultaneously (Collective Weave, Anchor + Helper: Helper adds ⌊Cog÷2⌋ bonus dice, Mending Ob 4 becomes manageable for lower-TS helpers)
2. Warden Cooperation (WC) bonus is active (+1D to all Thread ops, including Mending)

---

## Mode C: Full Scenario — Maret Operates at RS 22

**Scene:** Maret is in T13 (Oastad). She needs to Mend a deteriorating Gap that has been open for 3 seasons (RS −4 pending from sustained gap). If she doesn't close it this season, RS drops to 18 — crossing the threshold fully into Critical and approaching Dormant.

**Step 1: Maret Leaps.** Ob 3 (base 1 + 2 RS modifiers). Pool 13D.
Roll simulation (expected outcome): 7 net successes. Overwhelming (≥ 6 and ≥ 3). Clean suspension, next op Ob −1. +1 TS (Maret TS 50 → 51).

**Step 2: Contact established.** Focus 4 → 3 op rounds available (Round 1 = Leap, Rounds 2–4 = operations).

**Round 2 — Mend the Gap.**
Gap Mending: the Gap in T13 is a Micro-Gap (persistent small rupture, RS cost −4/season if untreated). Mending Ob for Micro-Gap: base 2, +2 RS modifiers, −1 from Overwhelming Leap = **Ob 3**.
Pool: Attunement 4 + relevant history 1 + TPS 5 = **10D vs Ob 3**.
E(net) ≈ 10 × 0.572 = 5.7. P(OW: ≥6 AND ≥3): ~55%. P(Succ): ~35%. P(Partial): ~8%. P(Fail): ~2%.

**Result: Overwhelming.** Gap Mending Overwhelming: RS +2. Gap closed (no further seasonal −4 drain). Paradox Window: does a successfully closed Gap create a paradox window? No — PP-193 paradox windows apply to Past-Oriented Pulling (POP), not Mending. Gap is cleanly closed.

**RS update:** RS 22 + 2 = RS 24. Still Critical but retreating from the edge.

**Co-Movement (Version C — three dimensions):**
Temporal auto-effect: d6 roll (expected ~3.5). At d6 = 3: minor physical object shifts nearby. Narrative only.
Epistemic auto-effect: nearest person with TS 0 (TS 10–29) feels brief disorientation. If Church Inquisitor in T13: triggers "Inquisitor detects Thread operation" — Investigation stage opens.

**Is there an Inquisitor in T13?** Church deployed Inquisitors in T2 and T14 per prior simulation. T13 is Proximity 1 — Church may prioritise Proximity-0 and 1 territories for Investigation. Let's say no Inquisitor in T13 currently. Epistemic effect: local Guilds merchant feels dread, shakes it off. No mechanical consequence.

**Round 3 — Second operation: Maret attempts Weaving (CV reduction in T13).**
Weaving Ob: base 2, +1 Ob global Critical, +1 Ob Proximity 1 Critical = **Ob 4**. Minus Overwhelming Leap modifier (−1) = **Ob 3**.
Pool: Attunement 4 + History 1 + TPS 5 = **10D vs Ob 3**.
**Result: Success.** T13 CV: 1 → 0 (floor? CV range is 0–5, so CV 0 is achievable). This takes T13 to CV 0 — maximum Restoration pole alignment.

**RS cost from Weaving Co-Movement:** Weaving Overwhelming/Relational auto-effect not triggered (this was Success, not OW). Standard d6 auto-effect at Success: minor consequence. RS unchanged from Weaving itself (Weaving RS cost is embedded in the Co-Movement auto-effect, which at Success is minor).

**Round 4 — Maret maintains contact but chooses not to operate.** Contact closes naturally. TPS −1D penalty: Leap roll failed? No — successful Leap, contact ends cleanly. TPS unchanged.

**End of scene:** RS 24. T13 CV 0. Gap closed. Gap was threatening −4 this season; instead RS gains +2. Net vs threat: +6 RS saved relative to doing nothing.

---

## Mode D: Edge Cases at RS 22

**Edge 1: Dissolution attempt at RS 22**
From PP-201 (mass combat context, applicable generally): "E[RS per Dissolution attempt at TS70] = −18.4." At personal scale, Dissolution Success: −5. Dissolution Failure: −8.
At RS 22: a single Dissolution Failure drops RS to 22 − 8 = **RS 14** (band 19–1 remains but approaching 10: Southernmost Surge one-time event fires at RS ≤ 10). A Failure is 8 RS from Surge trigger.

**Conclusion:** Dissolution at RS 22 is existentially reckless. Even Success (−5) brings RS to 17. No practitioner with any situational awareness should attempt Dissolution below RS 30. No rule prevents it — GM responsibility.

**[EDITORIAL: ED-328 — Consider adding a "Dissolution Recklessness" rule: if a practitioner attempts Dissolution when RS ≤ 25, all practitioners peninsula-wide make a Spirit check (Ob 2, TN 7) or suffer Coherence −1 from sympathetic substrate stress. Does not block the attempt — just raises the stakes. P3 — design option, not a gap.]**

**Edge 2: Leap Failure at RS 22 (low-TS practitioner)**
Low-TS practitioner (TS 30, pool 5D) at Ob 3 in Proximity 1 at RS 22:
P(Leap Failure) ≈ ~35%. On Leap Failure: "Thread contact fails. −1D to Thread Pool Score for remainder of scene."
If Thread Pool Score was already 3D and loses 1D = 2D. Next Leap attempt with TPS 2D: effectively capped at 2D bonus in pool. Multiple failed Leaps progressively debilitate the practitioner.

**But:** If Leap Failure at RS 22 triggers a Co-Movement auto-effect even on failure? No — Leap Failure = contact not established, no operation occurs, no Co-Movement draw. Coherence and Focus intact. Just TPS penalty.

**Edge 3: Two practitioners operating simultaneously at RS 22 (Collective Weave)**
Maret (Anchor) + secondary practitioner (Helper, TS 30, Cog 3 → contributes ⌊3÷2⌋ = 1D).
Combined pool: 13D (Maret) + 1D (Helper) = 14D. Ob modifier from Collective: if pool < half Maret's solo pool (13D), +1 Ob. 14D > half of 13D = 6.5 → no penalty. Good: even 1 helper avoids the penalty.

But: both practitioners performing operations means two Co-Movement draws per round. Two sets of auto-effects. At RS 22, auto-effects are more consequential (Proximity 1 auto-effect includes Gaps on 1d10: 1–4 result). Two draws double the gap-triggering probability.

**Collective Weave at RS 22 is net-positive for the Mending result but doubles auto-effect exposure.** 

---

## Findings Summary

| ID | Severity | Finding |
|----|----------|---------|
| F-RS-01 | P1 | RS 22 recovery requires ~18 Mending sessions (months of play). No emergency recovery mechanism exists. Multi-arc commitment to stabilise. |
| F-RS-02 | P2 | RS 22 Ob modifiers (+2 total in Proximity 1) block low-TS practitioners (TS 30 pool ~5D) from reliable Leap (P(Fail) ~35%). High-TS practitioners unaffected. RS crisis creates practitioner tier divide. |
| F-RS-03 | P2 | Dissolution at RS 22 risks RS 14 on Failure — 4 points from Southernmost Surge. No mechanical gate exists. Design relies on player/GM awareness. |
| F-RS-04 | P3 | Collective Weave at RS 22 doubles Co-Movement auto-effect exposure, increasing Gap-trigger probability. Net still positive for Mending but risk profile elevated. |

