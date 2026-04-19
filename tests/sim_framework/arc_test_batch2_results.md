# Valoria — Provisional Mechanics Arc Test — Batch 2 Results

**Date:** 2026-04-19  
**Builds on:** `tests/sim_framework/arc_test_results.md` (Batch 1)  
**Simulation:** `arc_test_batch2.py` — 5 variants × 5 seeds × 24 seasons  
**Bug fixes vs Batch 1:** RM Inf now only increments on genuine ctrl change; same-season Consolidation race fixed; secession_blocks tick correctly.

---

## B2-1: Secession Cooldown — 0 vs 2-season fix

**Finding: the cooldown fix has zero effect.**

Event counts are identical across all 5 seeds (no cooldown: 76.4 avg; cooldown: 76.4 avg; 0% reduction). The logs are character-for-character identical. The reason: the oscillation in Batch 1 was the RM→Varfell→RM loop driven by Consolidation grabbing settlements back from RM and Fragmentation re-seceeding them. The Batch 1 sim bugs (RM Inf inflation, same-season race) were masking that the cooldown fix addressed the wrong mechanism.

After fixing those bugs, what the corrected sim reveals is different: the oscillation is NOT a Consolidation churn. It's persistent RM secession events on settlements that are **already RM-controlled** (`was RM` in the log). The secession is firing on a province that is fractional because RM holds a settlement — but RM-held settlements are themselves triggering the Ob calculation as "alien non-seat," so the Fragmentation check keeps firing and keeps logging `→ RM (was RM)`. This is a **spec ambiguity**: should a Fragmentation check be able to produce a Secession event when the alien settlement is already controlled by RM? The spec says Secession is "the settlement becomes a de facto independent subnational holding" — but if it's already RM's, there's nothing to secede.

**Required spec fix (revised from Batch 1):** Secession should only be a valid outcome when the candidate settlement is controlled by a faction *other than RM*. A settlement already under RM governance cannot secede further. Add to `fractional_province_ownership_v30 §2.6`: "Secession candidates are limited to settlements not already held by a subnational faction."

The 2-season cooldown is still a reasonable friction mechanic but does not address the core issue.

---

## B2-2: RM Emergence Threshold — Order≤1 vs Order=0

**Finding: Order=0 is the correct threshold. Order≤1 fires too early and produces the wrong arc shape.**

| Metric | Order≤1 | Order=0 |
|--------|---------|---------|
| Avg RM settlements | 7.0 | 4.2 |
| Avg RM Influence | 8.6 | 9.6 |
| Seed variance | Low | Higher |

Order≤1 produces 7 RM settlements consistently across seeds — effectively deterministic. Order=0 produces 4–5 settlements with genuine variance (seeds 42 and 201 end with Varfell intact at 7.33 PV; seeds 77, 99, 137 produce Eastern Varfell splinter at 4.33 PV). The strict threshold forces RM to wait for genuine collapse conditions rather than emerging on first Order degradation from warfare.

Notably, RM Influence is *higher* under Order=0 despite fewer settlement emergences. This is because the succession split fires more often with Order=0 (Varfell stays stronger longer, succession becomes a real contest with political stakes), and the RM-candidate partial success gives +1 Influence on split. RM grows through political leverage rather than settlement accumulation — which is the correct design intent.

**Recommendation:** Change RM Settlement Emergence threshold in `faction_succession_split_v30 §4` from Order≤1 to Order=0.

---

## B2-3: Splinter Mandate Floor — 1 vs 2

**Finding: mandate floor has no effect on arc outcomes. The design problem is structural, not parametric.**

Eastern Varfell PV at end of 24 seasons:
- Floor 1: [1.33, 0, 0, 1.33, 1.33] across 5 seeds
- Floor 2: [1.33, 0, 0, 1.33, 1.33] — identical

The splinter holds T4 (Grauwald). T4 has two settlements: Grauwald Town (Varfell seat of T4, P=2) and Grauwald Lodge (RM, P=1). Eastern Varfell controls only Grauwald Town, giving it 2/3 of T4's PV = 1.33. This is stable — the Lodge is already RM, so T4 is always fractional, but Eastern Varfell's Fragmentation check for T4 is vs Ob 3 (2 + 1 alien settlement). With Mandate 1 or 2, the Influence pool for Eastern Varfell is the same (inherited from parent Varfell at split), and the rolls produce the same distribution.

The real problem: raising Mandate floor from 1→2 doesn't change Influence, which is what drives Fragmentation checks and Domain Action pools. **Mandate and Influence are separate stats.** The spec's splinter initialization (§2.4) only specifies Mandate and Wealth splits — Influence is explicitly NOT split ("Each contender keeps pre-contest Influence"). So both splinters start with identical Influence (4), making Mandate floor irrelevant to survival.

**Design implication:** If the intent is durable splinter rivals, the lever is Influence (give the splinter a share), not Mandate. Or: give the splinter a dedicated starting Stability that affects action availability, not just Fragmentation Ob.

---

## B2-4: Crown Suppression — Off vs On

**Finding: Crown suppression backfires. The suppression action accelerates RM growth.**

| Metric | Off | On |
|--------|-----|-----|
| Avg RM settlements | 7.0 | 8.0 |
| Avg fractional provinces at end | 3.0 | 4.0 |
| Crown PV (seed 42) | 20.0 | 18.2 |

When Crown suppression fires, it targets T1 (Valorsplatz) or T8 — the highest-PV fractional province. Adding Ob+1 to T1's Fragmentation check means the Crown Seat province's fragmentation check becomes harder to pass. This is backwards: the suppression action costs Crown 1 Influence per season AND makes T1 more likely to fail its fragmentation check. By S05 Crown Influence is at 0 (exhausted); after that Crown has no suppression capability for the remaining 19 seasons.

The Crown suppression model is wrong. The design intent (Crown redirecting pressure onto rivals) cannot be modeled as Ob+1 on fragmentation checks — that mechanic affects the *seat-holder's* defense of their own province, not an attack on rivals. Crown's actual suppression lever in canon is political/diplomatic: rumorcraft, Heresy referral, Parliamentary manoeuvring. These are not representable as a fragmentation Ob modifier.

**This is a simulation modeling limitation, not a spec flaw.** The canonical Crown suppression action (`npc_priority_trees Crown P2`) needs to be implemented as a dedicated action affecting rivals' Mandate or Influence, not as a province-fragmentation modifier. Flag for engine_v4 Phase 4 (political AI).

The notable artifact: Crown losing 5 Influence in 5 seasons to a useless suppression action while RM grows reveals that **Influence drain without political payoff is dangerous**. If engine_v4 implements any Influence-spending actions, it needs a validity check — spending Influence on an action that produces net-negative outcomes for the spender should either be blocked by the AI or flagged as a warning.

---

## B2-5: Mutual Fractionalization — T8 and T11 Simultaneously

**Finding: mutual fractionalization is mechanically stable. The two provinces don't compound each other.**

Hafenmark holds T11 Halvardshelm (captured S030) while Varfell holds S017 in T8. Both provinces fractional from S00.

Outcomes across all seeds:
- Hafenmark ends with 8.46 PV (vs 7.46 in single-fractionalization scenarios) — it *gains* PV from holding S030 in T11
- Varfell ends with 6.33 PV vs 3.0–4.33 in fracture scenarios — also gains from still holding more of its own territory
- RM reaches only 4–5 settlements (vs 7 in fracture scenarios) — mutual fractionalization creates *less* RM growth, not more

Why: when both aggressors are engaged in their own fractional provinces, neither has the Influence surplus to be running fragmentation failures on as many provinces simultaneously. The two fractional provinces (T8 and T11) each generate fragmentation events, but T11's fragmentation check has Hafenmark as the seat-holder (Influence 5, Ob 3) — Hafenmark is more stable than Varfell as a Fragmentation defender, so T11 rarely seceeds.

The arc this produces: Hafenmark-Varfell standoff where both hold partial stakes in each other's territories, creating a persistent cold-war fractionalization state rather than RM cascade. This is the most interesting arc produced by any Batch 2 scenario — it's genuinely emergent from the mutual mechanic interaction and has no analogue in Batch 1.

**Notable: T13 fractionalizes in seeds 42 and 201.** Oastad Shrine (S032, RM) in T13 creates a fractional province because the Oastad Seat (S031, Varfell) passes fragmentation checks inconsistently when Varfell Influence is strained by the T8 action. The RM pressure on T13 grows as a secondary effect of Varfell's distraction. This is the correct Einhir-territory dynamic: RM presence in T13 is canonical (Oastad Shrine is established RM), and distracted Varfell cannot suppress it.

---

## Cross-Variant Summary

| Variant | RM s | RM inf | Events | Key finding |
|---------|------|--------|--------|-------------|
| B2-1 no cooldown | 7 | 9 | 82 | Oscillation is RM→RM secessions, not churn |
| B2-1 2s cooldown | 7 | 9 | 82 | Cooldown has zero effect; wrong mechanism |
| B2-2 Order≤1 | 7 | 9 | 82 | RM growth deterministic, too fast |
| B2-2 Order=0 | 4 | 9 | 86 | RM growth correct speed, genuine variance |
| B2-3 Mandate floor 1 | 7 | 9 | 82 | Splinter survives in 3/5 seeds at PV 1.33 |
| B2-3 Mandate floor 2 | 7 | 9 | 82 | Identical — Mandate floor is not the lever |
| B2-4 suppression off | 7 | 9 | 82 | Baseline |
| B2-4 suppression on | 9 | 10 | 120 | Crown suppression backfires; drains Influence |
| B2-5 mutual frac | 5 | 9 | 80 | Stable standoff arc; less RM than expected |

---

## Revised Gap Flags and Recommendations

**Spec fixes required before PP-666 canonization:**

1. **`fractional_province_ownership_v30 §2.6` — Secession candidates:** Add: "Settlements already under subnational faction governance (e.g., RM) are not valid Secession candidates. The Fragmentation Check Failure outcome only fires if at least one alien settlement is held by a national faction." This eliminates the RM→RM secession noise.

2. **`faction_succession_split_v30 §4` — RM Emergence threshold:** Change Order≤1 to Order=0 as the trigger. Current spec says "Order drops to 0" which is Order=0 — but the example thresholds suggest ≤1. Clarify and standardize to Order=0.

3. **`faction_succession_split_v30 §2.4` — Splinter Influence:** The spec explicitly keeps Influence unsplit ("Each contender keeps pre-contest Influence"). This makes Mandate floor irrelevant. If durable rival splinters are the intent, either: (a) split Influence 60/40 same as Mandate, or (b) give the splinter a reduced Influence equal to its Mandate floor × faction's per-Mandate Influence rate. Flag as design decision required.

**Simulation gap (not a spec flaw):**

4. **Crown suppression** cannot be modeled as province Ob+1. Engine_v4 Phase 4 must implement Crown's political AI as Mandate/Influence drain on targets, not as fragmentation modifiers.

**New arc finding for design:**

5. **Mutual fractionalization produces stable cold-war arcs.** This is the correct Hafenmark-Varfell dynamic for a mid-game standoff scenario. The two factions holding stakes in each other's territory — neither able to consolidate, both defending Fragmentation checks — generates persistent tension without RM cascade. This arc should be a target state for the mid-game balance. Consider whether the engine_v4 should have a diplomatic mechanic that resolves mutual fractionalization via treaty (exchange of held settlements) as an alternative to the consolidation/siege path.
