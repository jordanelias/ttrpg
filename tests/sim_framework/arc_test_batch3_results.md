# Valoria — Arc Test Batch 3 Results

**Date:** 2026-04-19  
**Builds on:** Batches 1 and 2 (PP-666 provisional mechanics)  
**Simulation:** `arc_test_batch3.py` — 5 systems × 5 seeds  
**Systems under test:** CI buildup/Mass Seizure, RS decay, Fort constraint, IP/Altonian Vanguard, Hafenmark suppression race  
**Canonical sources used:** `params/bg/ci_seizure.md`, `params/bg/clocks.md`, `params/bg/core.md`, `params/bg/faction_actions.md`, `designs/world/geography_v30.md`

---

## B3-1: CI Buildup → Mass Seizure Timing

**Setup:** Church performs Assert each season, Piety Spread in target territory, infrastructure buildup at 1 tier/season. Hafenmark structural suppression on/off.

**Results:**

| Config | Seeds | Seizure season range | Outcome distribution |
|--------|-------|---------------------|---------------------|
| No suppression, T9 | 5 seeds | S11–S15 | 3× Overwhelming, 1× Success, 1× Partial |
| Suppression on, T9 | 5 seeds | S12–S14 | 4× Overwhelming, 1× Success |
| Suppression on, T1 | 5 seeds | S10–S15 | 4× Overwhelming, 1× Success |

**Key findings:**

1. **Hafenmark structural suppression delays Seizure by ~2 seasons on average but does not prevent it.** No-suppression: S11–15. With-suppression: S12–14. The Piety Yield (CI+6/season from T9's SW=5) overwhelms the structural suppression (CI−1/season). The net CI gain even with suppression is ~+4–5/season, reaching CI 60 by ~S8–9 and CI 80–100 by S12–14.

2. **Seizure probability at CI 98 (84%) means the window is narrow but almost always fires before CI 100.** The exponential curve `P=((CI-60)/40)^3.3` produces: 1% at CI 70, 10% at CI 80, 39% at CI 90, 84% at CI 98, 100% at CI 100. In practice, Seizure fires between CI 80–100 across all seeds. Very few seeds reach CI 100 (deterministic fire) — most fire probabilistically in the 88–98 range.

3. **At T9 (PT=5, infra=3), Seizure Ob=2. Pool at CI 98 = 12d.** 12d vs Ob 2 is almost guaranteed Overwhelming. This is the Church's best-case scenario: Seizure against a high-PT, fully-infrastructured territory. **This is correctly calibrated** — Church must invest heavily in T9 to make Seizure powerful, and T9 is already the canonical Church heartland.

4. **Critical gap:** Piety Yield at T9 (SW=5, PT 1→5) generates CI+6/season at full PT. This is far above the CI seasonal cap of ±5/season from all sources combined (PP-504). The simulation is violating the cap. The CI formula must enforce the ±5/season ceiling — Piety Yield alone at T9 maxes this out, leaving no room for Assert, Conditional Passive, or Charity Advantage to contribute. **The cap effectively makes Assert a wasted action once Piety Yield is maximized at T9.** This is a design interaction that needs flagging: the season cap may be too restrictive given T9's SW value, or T9's SW needs tuning.

5. **Church Stability collapses under the sim conditions.** Assert failures cost Stability −1, and with the cap already saturated by Piety Yield, Assert fires unnecessarily at full CI gain and fails often. Church Stability reaches 0 by S7–10 in most seeds. This is a modeling artifact (the sim runs Assert regardless of whether it's needed), but it reveals a real design tension: an aggressive Assert strategy at high CI will damage Church Stability, which eventually threatens the Seizure attempt itself (Mandate checks require Stability > 0).

---

## B3-2: RS Decay Under Warfare

**Key season markers (deterministic across seeds — no variance):**

| Intensity | RS Band 79 | RS Band 59 | RS Band 39 | RS Band 19 | Vanguard deploys | RS 0 |
|-----------|-----------|-----------|-----------|-----------|-----------------|------|
| 1 battle/s | S21 | never | never | never | never | never |
| 2 battles/s | S11 | S21 | S31 | never | S19 | never |
| 3 battles/s | S7 | S14 | S21 | S27 | S13 | never |
| 2 battles/s (campaign) | S6 | S11 | S16 | S21 | S6 | S25 |

**Full seed-determinism.** RS and IP are fixed arithmetic — no dice involved — so all three seeds produce identical results. This confirms the RS/IP system is purely deterministic at BG scale. The randomness in the game comes from what actions factions take, not from RS/IP itself.

**Key findings:**

1. **Moderate warfare (1 battle/season) never triggers meaningful RS effects.** Over 30 seasons: RS=70, IP=60. IP never reaches 75 (Vanguard threshold). Only the RS 79→60 band is entered at S21. Ob penalties: Proximity 0 territories (T15) get +1 Ob to all non-Thread actions. All other territories unaffected. This is the game's "cold war" state — conflict exists but never escalates to existential.

2. **Active warfare (2 battles/season) triggers Vanguard by S19 and reaches RS 59 (Ob+2 at T15, Ob+1 at T6/T13) by S21.** The Vanguard then advances from T10 to T1 in 5 seasons (S19→S24). This means active faction warfare automatically produces an Altonian crisis by mid-game (~S20–25). **This is structurally correct** — the Altonian pressure is supposed to be the forcing function that ends faction conflict. The question is whether S20–25 is the right timing for the Vanguard arrival.

3. **Campaign-scale warfare (RS −2/battle) produces Rupture at S25.** 2 campaign-scale battles/season = RS −4/season. RS 0 in 25 seasons. Rupture is canonically "all factions lose" — this is the shared-loss outcome. The sim confirms that campaign-scale warfare can trigger Rupture without Vanguard even reaching T1 (Vanguard deploys at S6, reaches T1 by ~S14, but Rupture fires at S25 regardless). **Design implication: campaign-scale battles should be rare events, not routine actions.** If factions fight campaign-scale battles every season, the game ends in mutual loss.

4. **Proximity gradient is working correctly.** At RS 56 (active war by S22): T15=+2 Ob, T6/T13=+1 Ob, all other territories=0. The gradient correctly concentrates Calamity pressure in the south without globally penalizing all factions. Varfell (T12, node 2) starts feeling Thread Ob penalties at RS≤59. Church in T9 (node 4) feels nothing until RS≤39.

5. **Warden emergence at RS≤40 fires at S30 in active-war scenario.** This is 30 seasons in, well past the Vanguard deployment (S19) and Vanguard's arrival at T1 (S24). The Wardens emerge into a peninsula already in crisis — which is the correct narrative sequence. **Gap:** the canonical Warden emergence mechanics beyond "they appear" are not in `params/bg/clocks.md`. They need spec in `npc_behavior_v30` or equivalent.

---

## B3-3: Fort Constraint — Varfell Breakout

**Setup:** Varfell Military=4 (canonical start). Three routes tested: A (T4→T2→T1, no major forts), B (T11→T9→T14→T1, hits Fort3 at T14), C (T13→T15→T6→T5→T1, Askeheim bypass).

**Results (static Mil=4):**

| Route | Seeds succeeding | Seasons | Stall point |
|-------|-----------------|---------|-------------|
| A — via T4/T2 | 4/5 | S1 (immediate) | T1 Fort2 in 1 seed |
| B — via T9/T14 | 0/5 | — | T14 Fort3 in 4/5; T9 in 1/5 |
| C — via T15 | 4/5 | S1 (immediate) | T1 Fort2 in 1 seed |

**With Mil growth +1/4 seasons:**
- Route A: 5/5 break through (T1 Fort2 now beatable at Mil 5+)
- Route B: 1/5 breaks through (T14 Fort3 still holds in 4/5 seeds at Mil 5–6)

**Key findings:**

1. **T14 Ehrenfeld (Fort3) is an absolute wall for Varfell at Mil 4.** Route B stalls at T14 in 4/5 seeds, stalls at T9 (Fort2, Church Mil 4) in 1/5 seeds. Battle Ob at T14 = `floor(4/2)+1+3 = 6`. Varfell 4d vs Ob 6: expected net = −2 (Failure). With Mil growth to 5: 5d vs Ob 6, expected net ≈ −1 (still Failure/Partial). T14 is essentially impassable for Varfell without Military 7+. **This is canonical** — T14 is the primary Crown chokepoint and Löwenritter base.

2. **Route A (via T2) is the weakest link.** T2 Kronmark has no fort. Crown Mil 4, Battle Ob = `floor(4/2)+1 = 3`. Varfell 4d vs Ob 3: expected net ≈ 0 (Success/Partial range). Varfell takes T2 in S1–5 in most seeds. T1 Fort2 then stalls Varfell: Ob = `3+2=5`. 4d vs Ob 5 ≈ expected net −1 (Failure). Route A breaks through T2 but stalls at T1 in most seeds with static Mil. **Design issue: T2 (Crown's breadbasket) is not adequately defended. Varfell can reach it too easily, threatening Crown's food supply before hitting the real fortification chokepoints.** Whether this is intentional — Crown must garrison T2 or lose it — needs clarification.

3. **Route C (Askeheim) is mechanically equivalent to Route A.** T15 has no military defender, T6 Stillhelm has minimal garrison (modeled at Crown Mil/2). Varfell transits T15 at RS cost (−1 per season of transit) and reaches T5/T1 on the same timeline as Route A. The RS cost per transit is negligible at RS=100 start. **The Askeheim route only becomes costly if RS is already degraded from warfare.** If Varfell chooses the southern route in a high-RS game, it's functionally free. At RS=60 (active war mid-game), Askeheim adds Ob+1 to all actions at Proximity 0 for the transiting army — still manageable.

4. **The Fort system works as a meaningful constraint on Route B but not Routes A/C.** The game's geographic containment of Varfell relies on Crown actively garrisoning T2 and the Askeheim route being costly due to RS degradation. Neither is automatic — Crown must make the choice to defend T2, and RS degradation requires faction conflict that may not have happened yet when Varfell moves. **Design recommendation:** either T2 needs a Fort (making Route A harder) or the canonical assumption is that Crown always garrisons T2 (which needs to be explicit in Crown's priority tree).

---

## B3-4: IP Escalation → Altonian Vanguard

**Results:**

| Config | Vanguard deploys | Final position | Coalition | RS final |
|--------|-----------------|---------------|-----------|---------|
| 1 battle/s, 30s | never | — | no | 70 |
| 2 battles/s, 30s | S19–22 | T1 (all seeds) | yes | 53–57 |
| 3 battles/s, 30s | S13–14 | T1 (all seeds) | yes | 50–52 |
| 2 battles/s + AER4 | S22 | T1 (all seeds) | yes | 50–53 |

**Key findings:**

1. **AER4 (Schoenland mediates) does not prevent Vanguard deployment in active-war scenarios.** The spec says AER≥4 raises IP threshold to 80. But with 2 battles/season, IP reaches 80 by S20 regardless — the 5-IP threshold difference buys ~1 season. **AER4 is not a meaningful brake on Vanguard.** AER5 (IP held at 50) is the only effective counter, and it requires sustained high-performance diplomacy.

2. **The coalition mechanic fires correctly but the coalition cannot stop the Vanguard.** When Vanguard reaches T2/T1, factions pause conflict and form a coalition. Coalition Military 4 vs Vanguard Ob 3 rolls Partial/Failure repeatedly. The Vanguard reaches T1 anyway. This means **the Altonian Vanguard is a crisis the faction coalition cannot reliably resolve through military means** — which is correct per the spec (Vanguard requires Schoenland mediation, not military defeat, to halt). But the coalition military rolls produce consistent failures, suggesting the coalition needs non-military resolution paths (Schoenland, AER5) to be viable.

3. **Vanguard reaches T1 in 5–6 seasons from deployment in active-war scenarios.** Deployed at S19, reaches T1 at S24. This is a 5-season crisis window after Vanguard appears. Given that Mass Seizure fires at ~S11–14 (B3-1) and Varfell breakout begins around S3–5 (B3-3), the Vanguard arrives after both the Church Seizure crisis and Varfell's initial expansion. The sequence: Varfell expands (S1–10) → Church seizes (S11–14) → Vanguard crisis (S19–24). This is a plausible campaign arc shape.

4. **Critical gap: AER is not tracked in any simulation.** AER (Altonian Engagement Rating) is referenced in the spec as the counter to Vanguard pressure but has no canonical generation mechanic in the documents read so far. It's the most significant unmodeled external lever in the game. `[GAP: AER generation mechanic — not found in params/bg/* read so far; needed for Vanguard resolution path]`

---

## B3-5: Hafenmark Suppression Race

**Results:**

| Config | Seizure range (5 seeds) | Effective delay |
|--------|------------------------|----------------|
| Structural only | S10–S13 | baseline |
| + Parliamentary Challenge | S10–S18 | +0 to +7 seasons |

**CI comparison (seed 42, no challenge vs. challenge):**

| Season | No Challenge | With Challenge |
|--------|-------------|---------------|
| S1 | 33 | 33 |
| S5 | 53 | 49 |
| S9 | 73 | 67 |

**Key findings:**

1. **Structural suppression alone cannot prevent Mass Seizure.** CI reaches 60 by ~S7–9 in every seed regardless of suppression. The Piety Yield from T9 (+6/season at full PT) drives CI growth that exceeds the combined suppression capacity of −1/season structural + occasional successful Suppress action.

2. **Parliamentary Challenge adds meaningful variance but is unreliable.** Seeds range from S10 (same as no challenge) to S18 (7-season delay). The CI−2 on Overwhelming Challenge success is powerful, but Challenge roll is Mandate 4 vs Ob 2 — roughly 50/50 Overwhelming/Success/Partial. Partial/Failure results cost Hafenmark Stability −1 without slowing CI. In seed 201, Challenge delays Seizure to S18 — the longest delay in any scenario. In seeds 42 and 77, Challenge provides no additional delay over structural suppression alone.

3. **Critical issue: PP-431-COR invalidates the sim's model.** The spec states that when Hafenmark plays Parliamentary Challenge, structural suppression does NOT fire that season — Challenge replaces it. The simulation applies both structural suppression and Challenge effects in seasons where Challenge is played, which is incorrect. Correcting this means Challenge is a trade-off: aggressive Challenge play gives CI−2 on success but sacrifices the reliable CI−1 from structural suppression. This makes Challenge more strategically interesting — and reduces the guaranteed suppression in high-aggression seasons. **Re-run needed with PP-431-COR correctly modeled.**

4. **Piety Yield at T9 is the dominant CI driver, not Church actions.** Removing Assert and Conditional Passive from the calculation and running Piety Yield alone: +6/season at full PT from T9 (SW=5, PT=5). With the ±5/season cap, Piety Yield hits the cap every season. All other CI sources (Assert, Conditional Passive) are noise — they add at most +1 when the season cap allows. **This means the CI system's balance depends entirely on how quickly Church can build PT in high-SW territories, not on the Assert/Suppress minigame.** The Assert/Suppress mechanic is structurally irrelevant to Seizure timing once T9 reaches PT 3+.

---

## Cross-System Interaction: Campaign Arc Shape

The five systems produce a consistent campaign arc shape:

| Season band | Events |
|-------------|--------|
| S1–5 | Varfell expands via Route A (T2) or Route C (T15). Church builds PT/infra at T9. |
| S5–10 | CI reaches 50→60. Varfell stalls at T1/T14. RS still >80 (no Calamity effects). |
| S10–14 | Mass Seizure fires (CI 80–98). Church takes T9 formally or high-PT territory. |
| S14–20 | RS enters 79→60 band (Ob+1 at T15). IP approaches 70–75. |
| S19–22 | Vanguard deploys. All factions face external pressure. Faction conflict pauses. |
| S24–30 | Vanguard at T1 or RS enters 59→40 band. Warden emergence. Late-game pressure. |

This is a structurally sound campaign arc. The three act structure — expansion (S1–10), crisis (S10–20), endgame pressure (S20–30) — emerges naturally from the mechanical interactions without scripted triggers.

---

## Gap Flags

```
[GAP: CI seasonal cap vs Piety Yield — Piety Yield at T9 (SW5, PT5) = +6/season, exceeds ±5 cap; cap makes Assert irrelevant once T9 PT is maximized; needs design review of SW values or cap recalibration]
[GAP: Church Stability collapse — Assert failure drains Stability unnecessarily at high CI when Piety Yield already saturates cap; Church AI should suppress Assert once CI gain is capped by Piety Yield]
[GAP: PP-431-COR not modeled — Challenge replaces structural suppression when played; sim incorrectly applies both; re-run required for accurate suppression race timing]
[GAP: AER generation mechanic — not in any params/bg/* doc read; needed for Vanguard resolution; AER4/5 effects are canonical but generation route is not]
[GAP: T2 Kronmark garrison — no canonical rule requiring Crown to garrison T2; Varfell can reach T2 freely and Crown's breadbasket is exposed without explicit garrison mechanic in Crown priority tree]
[GAP: Warden emergence mechanics — RS≤40 triggers emergence per clocks.md but canonical Warden faction behavior (actions, priorities, effects) not in any read doc]
[GAP: Campaign-scale battle threshold — RS-2/battle for campaign scale vs RS-1/battle for standard; no canonical definition of what distinguishes campaign-scale from standard-scale battle]
```

---

## Recommendations for Design

1. **Review Piety Yield vs seasonal CI cap.** Either reduce T9 SW from 5 to 3 (making Piety Yield +3/season at full PT, leaving room for Assert/Suppress to matter), or raise the CI seasonal cap from ±5 to ±7. Current interaction makes Assert irrelevant.

2. **Specify T2 garrison as Crown default behavior.** Add to Crown priority tree: "If T2 is ungarrisoned and Varfell has Military active at T4, deploy garrison to T2 (Defend action)." Without this, Varfell's Route A breakout is too easy and Crown's food supply is unprotected.

3. **Clarify Parliamentary Challenge replacement per PP-431-COR.** The correction is canon but its strategic implication (Challenge is a trade-off, not a supplement) changes the suppression race dynamics significantly. The re-run with correct modeling is needed.

4. **Define AER generation.** Schoenland trade, Altonian diplomacy, Elske marriage (IP event), Torben decisions — these are referenced as AER sources but no mechanical generation table exists. Without it, AER5 (the only true Vanguard counter) is aspirational rather than achievable.
