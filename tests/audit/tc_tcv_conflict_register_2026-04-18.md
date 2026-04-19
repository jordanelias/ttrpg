# TC / CI / TCV / Seizure — Cross-Document Conflict Register
# Date: 2026-04-18
# Purpose: Identify all conflicts across canonical sources; requires editorial resolution

---

## CONFLICT 1: TC freeze at 75 vs TC runs to 100

| Document | Date | Status | Says |
|----------|------|--------|------|
| victory_v30.md L218,L543 | 2026-04-06 | DESIGN | "TC freezes at 75" |
| military_layer_v30 §3.10 | 2026-04-14 | CANONICAL | "At TC 75: TC freezes" |
| params/bg/core.md | — | — | "0–75 (freeze ceiling)" |
| params/bg/clocks.md | — | — | "75+ TC frozen" |
| tc_political_v30 §2 | 2026-04-14 | CANONICAL | "TC no longer freezes at 75. TC runs to 100." |
| params/bg/tc_seizure.md | — | — | "TC runs to 100 (no freeze)" |
| campaign_architecture_v30 §1.3 | 2026-04-17 | CANONICAL | "CI=100 Mass Seizure Declaration" (implies 100 ceiling) |

**tc_political and campaign_architecture (newer, CANONICAL) say no freeze. victory_v30 and military_layer (older or same-day) say freeze. victory_v30 itself is internally contradictory — L543 says "freeze at 75" while L545 describes CI=100.**

---

## CONFLICT 2: TC vs CI naming

| Document | Term used |
|----------|-----------|
| victory_v30 §7 L541–554 | "TC" throughout, except L545 uses "CI" in the CI=100 section |
| tc_political_v30 | "TC" throughout |
| campaign_architecture_v30 | "CI" in §1.3 |
| params/bg/* | "TC" throughout |
| military_layer_v30 | "TC" throughout |

**CI appears only in campaign_architecture_v30 (newest doc) and one line in victory_v30. Not formally defined or renamed anywhere. Jordan states TC = CI = Church Influence.**

---

## CONFLICT 3: Seizure availability threshold

| Document | Seizure available from |
|----------|----------------------|
| params/bg/tc_seizure.md | TC ≥ 15 (PP-507) |
| tc_political_v30 §2.1 | TC 40 ("Church Assertive" milestone — seizure +1D) |
| victory_v30 §3.2 | "any TC value" (Graduated Seizure PP-494) |

**Three different thresholds in three docs. victory_v30 says "any TC value". tc_political gates it at TC 40 milestone. params says TC 15.**

---

## CONFLICT 4: Seizure Ob formula

| Document | Seizure Ob formula |
|----------|--------------------|
| victory_v30 §3.2 | 7 − PT |
| params/bg/tc_seizure.md | 2 + Fort Level + max(0, 3 − PT) |
| campaign_architecture_v30 §1.3 | 7 − PT − (infrastructure modifiers) |
| tc_political_v30 §2.1 | "Ob = 2 + Fort Level + max(0, 3 − PT)" (the "prior protocol") |

**Two different base formulas. victory_v30 and campaign_architecture use 7 − PT. params and tc_political use 2 + Fort + max(0, 3 − PT). These produce different results:**

| PT | 7 − PT | 2 + Fort0 + max(0, 3−PT) |
|----|--------|--------------------------|
| 5  | 2      | 2                        |
| 4  | 3      | 2                        |
| 3  | 4      | 2                        |
| 2  | 5      | 3                        |
| 1  | 6      | 4                        |
| 0  | 7      | 5                        |

**At PT 4 and 3, the formulas diverge significantly (Ob 3/4 vs Ob 2). At Fort > 0, the params formula adds Fort Level. victory_v30 formula does not include Fort in base Ob (but §3.2 states "Fort Level does NOT modify Seizure Ob").**

---

## CONFLICT 5: TCV values

| Territory | victory_v30 §1 | tc_political §1 | params/bg/victory |
|-----------|----------------|-----------------|-------------------|
| T8 (Gransol) | 3 | 4 | 4 |
| T9 (Himmelenger) | 5 | 3 | 3 |
| Starting Church TCV | 5 | 3 | 3 |
| Starting Hafenmark TCV | 6 | 8 | 8 |
| Total | 31 | 30 | 30 |

**victory_v30 has T9=5 (boosting Church). tc_political and params have T9=3. Which is canonical?**

---

## CONFLICT 6: TC 100 event naming and mechanics

| Document | Name | Mechanic |
|----------|------|----------|
| tc_political_v30 §2.2 | "Theocracy Unification Attempt" | Church may declare Unification Seizure on ANY territory (not just prominent), Ob = 2 + Fort. Fails if Church loses 3 territories, Mandate ≤ 3, or Crown Treaty against Church. Wins at ≥ 10 territories for 2 Year-Ends. |
| campaign_architecture_v30 §1.3 | "CI=100 Mass Seizure Declaration" | Every territory with Church building targeted simultaneously. Individual Ob per territory = 7 − PT − infrastructure. Mandatory Zoom In. 1 Emergency Session for opponents. |

**These describe two different mechanics for the same event. tc_political has per-season seizure on any territory. campaign_architecture has simultaneous mass seizure. The Ob formulas also differ (2 + Fort vs 7 − PT − infra).**

---

## CONFLICT 7: Church victory condition

| Document | Church victory requires |
|----------|----------------------|
| victory_v30 §3.2 | TCV ≥ 8 + PT ≥ 3 all held territories + Accord ≥ 3 in ≥ 3 non-capitals |
| tc_political_v30 flag ED-NEW-TC-10 | "Confirm whether Church victory at TC 65 + TCV ≥ 8 remains as-is or is replaced by TC 100 Unification only" |
| params/bg/victory.md | TCV ≥ 8 + PT ≥ 3 all held |

**tc_political flags an open editorial question about whether Church victory changes to TC 100 Unification only. This was never resolved.**

---

## SUMMARY: EDITORIAL DECISIONS REQUIRED

1. **TC/CI: freeze or no freeze?** tc_political (newer) says no. victory_v30 (older) says yes. Which is canon?
2. **TC or CI?** Is the track renamed from Theocracy Counter to Church Influence?
3. **Seizure availability: TC 15, TC 40, or any TC?**
4. **Seizure Ob: 7 − PT, or 2 + Fort + max(0, 3 − PT)?**
5. **TCV for T8 and T9?** T9=5 (victory_v30) or T9=3 (tc_political/params)?
6. **TC 100 event: Unification Attempt (per-season seizure) or Mass Seizure Declaration (simultaneous bid)?**
7. **Church victory: existing conditions or TC 100 Unification only?**

These 7 decisions must resolve before the engine can be built.

