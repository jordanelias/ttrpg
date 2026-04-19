# Valoria — Provisional Mechanics Arc Test Results

**Date:** 2026-04-19  
**Systems under test:** `settlement_adjacency_v30`, `fractional_province_ownership_v30`, `faction_succession_split_v30` (all PROVISIONAL, PP-666)  
**Simulation:** `arc_test_provisional.py` — 4 scenarios × 3 seeds × 16 seasons  
**Status:** Not a full engine rebuild. Targeted interaction test only.

---

## Summary

The three provisional mechanics interact. The dominant emergent arc across all scenarios is **RM ascent from political fracture** — not as a designed win condition, but as a structural consequence of how fractionalization, fragmentation checks, and secession chain together.

Two mechanics behave well. One has a critical design flaw.

---

## Arc 1: Partial Capture → Fractionalization (no succession)

**Setup:** Varfell takes S017 Gransol Market Quarter via settlement-granular movement (T12→T11→T8 road edges). T8 fractionalizes. No succession event.

**Arc (16 seasons, seed 42):**
- S01: Fragmentation check fires. S017 immediately seceeds to RM (Failure roll). Consolidation restores order elsewhere (Ehrenfeld Barracks, Cathedral submit).
- S02–S16: S017 oscillates between RM and null-control. Grauwald Lodge (S029, already RM) similarly cycles. Neither Varfell nor Hafenmark ever consolidates T8.

**Outcome (3 seeds):** Fully deterministic — PV totals identical across all seeds. RM holds 2 settlements and 2.21 PV at end.

**Findings:**
1. **Settlement adjacency works as designed.** Path-constrained invasion creates genuine partial-capture situations that binary province rules would have missed. The fractionalization trigger fires correctly.
2. **Fragmentation check is too punishing at low Influence pools.** Varfell's Influence (4) vs Ob 3 should produce mostly Success outcomes, but the S01 Failure + Secession happening immediately (season 1) indicates the spec's mechanic doesn't account for the *newly fractured* state being inherently harder to hold. Design intent unclear — is immediate secession after first-season capture intended?
3. **Consolidation submit/resist logic works but produces a churn loop.** S017 seceedes to RM → Varfell consolidates → seceedes again. The 4-season cooldown on RM Settlement Emergence prevents explosive growth but doesn't prevent this oscillation. **The fractional_province_ownership spec has no cooldown on Secession itself** — gap.
4. **RM's 2-settlement, 2.21-PV endstate is seed-invariant.** The arc is fully deterministic under this scenario because no high-variance event (succession) fires. This is actually correct behavior — the fractionalization/fragmentation/consolidation loop is stable but not explosive without an external shock.

---

## Arc 2: Succession During Fractional Hold

**Setup:** Same as Arc 1 (T8 fractional from start). Vaynard dies S08.

**Arc (seed 42):** Succession resolves as **Clear winner — Maret Uln** (margin 2 over Tribune Captain). Faction stays unified. Stability −1, Mandate −1. No split occurs.

**Arc (seed 137):** Succession resolves as **SPLIT — Eastern Varfell** emerges with T4 (Grauwald province). Varfell retains T12 + T11 + T13.

**Findings:**
1. **Succession clear-win produces no notable emergent arc beyond a Mandate dip.** The faction continues on the same trajectory. The fractional T8 stake is unaffected. This is correct behavior — clear succession shouldn't cascade.
2. **Succession split in seed 137 reveals a gap:** Eastern Varfell receives T4 (Grauwald), but the fractional stake in T8 (Gransol Market Quarter, S017) is NOT transferred to the splinter — it stays with "Varfell" because T8 is a Hafenmark province. The spec's asset split rule (§2.4: "winner holds capital province + adjacent; splinter takes remaining") doesn't address what happens to *contested settlements in enemy-held provinces*. This is a real gap: does the T8 fractional stake follow the asset split, or does it revert to RM/null because Varfell loses the army that took it?
3. **Post-succession fragmentation checks still fire on the now-split T4.** Eastern Varfell has only 1 mandate and low influence — its Fragmentation Ob defense collapses quickly. This produces a plausible arc: Varfell civil war → Eastern Varfell fragment loses Grauwald Lodge to RM immediately.

---

## Arc 3: RM Cascade from Eastern Varfell Collapse

**Setup:** Varfell succession split fires S05 (Tribune Captain wins, Maret Uln's faction = Eastern Varfell with T4). Halvardshelm (S030) and Oastad (S031) start at Order 1 to simulate wartime degradation.

**Arc (all seeds — fully deterministic):**
- S02: RM Settlement Emergence fires in *both* S030 and S031 simultaneously (both Order 1, Varfell-controlled, emergence check passes). RM jumps from 2 to 4 Influence, gains 2 settlements in a single check.
- S05: Varfell splits. Tribune Captain's Varfell retains T12+T11+T13. Eastern Varfell gets T4. RM gets political momentum bonus (+1 Influence → 5).
- S05 onward: Eastern Varfell (T4, Grauwald + Lodge) fails fragmentation checks repeatedly. Grauwald Lodge cycles through RM secession. Eastern Varfell effectively non-functional by S08.

**Final state (all seeds):** RM holds 5 settlements (2.21 PV from T8 stake + 2 Varfell settlements + Lodge + Shrine), Influence 5. Eastern Varfell at 1.33 PV (Grauwald Town only).

**Findings:**
1. **RM cascade arc is compelling and emergent.** It's not scripted — it emerges from: (a) low-Order settlements enabling Emergence, (b) succession split giving RM political momentum, (c) Eastern Varfell too weak to run Fragmentation checks. This is exactly the kind of arc the design intent ("RM emerges from populist fracture") describes.
2. **Full seed-determinism is a problem.** All 3 seeds produce identical outcomes. The RM emergence check and fragmentation check resolve identically because the Influence pools are fixed and the Ob values produce consistent outcomes. The dice randomness is insufficient to create variance at these pool sizes. **Design gap: the spec needs stochastic elements with more spread, or the simulation needs to model Influence as a dynamic stat that changes season-to-season.**
3. **RM 4-season cooldown per-province is too coarse.** When two adjacent provinces (T11, T13) both have low-Order settlements, RM emerges in both in the same check. The cooldown applies per-province, so T11 cooldown doesn't block T13 emergence. RM gains 2 settlements simultaneously in S02. This may be the intended behavior, but the resulting +2 Influence jump feels high.
4. **Eastern Varfell at Mandate 1 is non-functional.** It cannot run meaningful Domain Actions or mount defense. It collapses in ~4 seasons. This is realistic (a splinter in crisis) but means the splinter is not a political actor — it's just a timer until collapse. The succession split mechanic produces a "dead faction" not a rival. Whether this is intended depends on design goals for splinters.

---

## Arc 4: Full Interaction — Settlement Adjacency + Fractionalization + Succession

**Setup:** Varfell takes S017 S00 (adjacency mechanic). Halvardshelm + Oastad at Order 1. Vaynard dies S10.

**Arc (seed 42):**
- S00: T8 fractionalizes. RM footholds exist in T4, T13.
- S02: RM emerges in Halvardshelm + Oastad (Order 1 → Emergence). RM Influence 4.
- S10: Vaynard dies. **SPLIT** — Maret Uln vs Tribune Captain, margin 0. Maret Uln takes Eastern Varfell with T4. RM +1 Influence (momentum) → 5.
- S10–S16: Eastern Varfell in T4 collapses. Grauwald Lodge repeatedly seceedes. RM holds T4 Lodge, T13 Shrine, T11 Halvardshelm, T13 Oastad, T8 Market Quarter. 5 settlements, 5.21 PV.

**Arc (seed 137 — diverges):** Succession resolves as **Clear** (no split). Varfell stays unified. RM reaches 5 settlements but without the momentum bonus. Final RM PV: 5.21, Varfell: 4.33 (keeps T4 + T11 + T12 + T13 unified).

**Findings:**
1. **The full interaction produces a meaningful divergence between seeds.** Seed 42/99 = Varfell civil war + RM ascent. Seed 137 = Varfell survives, RM grows but doesn't get momentum boost. This is the correct behavior — succession outcome should matter.
2. **RM reaching Stage 3 (5 settlements, 5.21 PV) by S16 is plausible but fast.** Per `faction_succession_split §4`, Stage 3 requires 2+ settlements across 2+ provinces. RM hits this by S02 in degraded-Order scenarios. The 4-season cooldown per province is the only brake, and it's insufficient when 3–4 provinces are simultaneously low-Order. **Design risk: if the player creates the conditions (multiple wars degrading Varfell Order), RM ascent is very fast.**
3. **Crown is completely uninvolved in all four arcs.** Crown holds ~20 PV in every run across all scenarios. It has no mechanism that interacts with fractionalization, succession, or RM emergence in the current simulation scope. This isn't a bug in the provisional mechanics — it correctly reflects that Crown's lever is political/diplomatic, not geographic. But it confirms the engine_v4 must model Crown's active suppression AI (political pressure, Einhir suppression action) for Crown to be a real actor in these arcs.
4. **Church is similarly passive.** 4.0 PV throughout. The Valorsplatz Cathedral (S003) seceeds to RM and then submits back to Crown in S01 across every run — the Church is too weak to hold non-Himmelenger settlements under fragmentation pressure. This may be accurate to the design (Church wins via Mass Seizure, not territorial defense) but it means Church fractional losses are systematically unrecoverable without the Mass Seizure mechanic being modeled.

---

## Mechanical Assessment by System

### Settlement Adjacency (`settlement_adjacency_v30`) — **Works, one gap**

The path-constraint model fires correctly. Settlement-granular invasion creates genuine partial-capture situations. The edge-type modifiers (mountain pass, river) are not exercised in these arcs (all Varfell movement used road edges) — they need targeted tests.

**Gap:** `settlement_adjacency_map.yaml` does not exist. The adjacency graph is inferred from province adjacency + Seat-to-Seat rule. Non-Seat inter-settlement edges within provinces are fully connected (all same-province settlements adjacent to each other), which may not reflect actual geography — a fortress town that controls a mountain pass shouldn't be adjacency-equivalent to a port in the same province.

### Fractional Province Ownership (`fractional_province_ownership_v30`) — **Design flaw in Secession loop**

The fractionalization trigger, PV re-derivation, and Consolidation threshold work correctly.

**Critical issue:** There is no cooldown on Secession. A settlement can secede, be consolidated back, and secede again in consecutive seasons. The oscillation produces noise in the event log but no real PV consequence. The spec needs a Secession cooldown (suggest: 2 seasons after Consolidation submit before next Fragmentation check fires in that settlement).

**Gap:** The spec does not address what happens to a fractional stake (enemy-held non-Seat settlement) when the faction that holds it undergoes a succession split. Does the stake transfer to the geographically-nearer splinter? Revert to RM? This was not resolvable from the spec text.

### Faction Succession Split (`faction_succession_split_v30`) — **Works, splinter viability gap**

The contest mechanics, asset split, and splinter establishment all fire correctly. Seed-to-seed variance in succession outcome (clear vs narrow) produces meaningfully different arcs.

**Design gap:** Splinters at Mandate 1 are non-functional actors. They exist for ~4 seasons and then collapse. This may be intentional (succession crises produce temporary chaos, not durable rivals) but the spec doesn't clarify whether splinters are intended as permanent rivals or temporary instability. If the intent is durable rival factions (the CK3 precedent implies this), the Mandate floor for splinters needs raising or the emergence path needs more support.

**Gap:** Contender pools for all non-Varfell factions are not in canonical sources. Only the Vaynard example (workplan §3) provides values. Crown succession (Baralta Claim vs Regency Council) uses estimated pools.

---

## Emergent Arcs — Summary for Design Review

| Arc | Trigger | Result | Design Intent Alignment |
|-----|---------|--------|------------------------|
| Fractional oscillation | Partial capture of low-Prosperity settlement | Endless secede/consolidate cycle, no stable partial state | Probably not intended — needs Secession cooldown |
| RM ascent from Varfell collapse | Multiple low-Order Varfell settlements + succession split | RM reaches Stage 3 by S02–S10 | Intended, but may be too fast |
| Succession civil war → RM momentum | Narrow succession + RM contender backing | RM gets +1 Influence + political window | Well-designed, correct behavior |
| Crown/Church passivity | No active suppression AI in scope | Both factions hold static PV while Varfell/RM dynamics resolve around them | Expected for this simulation scope; confirms engine_v4 needs political AI |

---

## Gap Flags

```
[GAP: settlement_adjacency — settlement_adjacency_map.yaml not authored; graph approximated from province adjacency + Seat-to-Seat rule; intra-province full-connectivity assumption may not reflect geography]
[GAP: fractional_province_ownership — no cooldown on Secession in spec; produces oscillation loop; suggest 2-season post-Consolidation cooldown]
[GAP: fractional_province_ownership — fractional stake disposition on faction split not specified in §2.4; does stake follow geographically-nearer splinter or revert?]
[GAP: fractional_province_ownership — province base PV not in canonical source; approximated from settlement count; needs geography_v30 explicit PV table]
[GAP: faction_succession_split — splinter viability at Mandate 1 unclear; spec doesn't distinguish temporary-chaos splinter from durable-rival splinter]
[GAP: faction_succession_split — contender pools canonical only for Varfell (workplan example); Crown/Hafenmark/Church succession pools not specified in npc_character_analyses_v30]
[GAP: RM settlement emergence — Disposition toward Yrsa Vossen not tracked at settlement level; simulation proxied by Order ≤ 1; actual tracking requires NPC disposition system]
[GAP: consolidation — Influence pool source per faction not specified in fractional_province_ownership_v30 §2.4]
```

---

## Recommendations

**Before canonizing these three mechanics:**

1. **Add Secession cooldown to `fractional_province_ownership_v30`.** 2 seasons post-Consolidation submit before next Fragmentation check in that settlement. Prevents oscillation loop.

2. **Specify fractional stake disposition on succession split.** One line in `faction_succession_split_v30 §2.4`: "Contested settlements in enemy-held provinces follow the faction whose province of origin the enemy settlement borders in the adjacency graph." Or: "Contested settlements revert to RM/null on succession split."

3. **Clarify splinter intent.** Is a Mandate-1 splinter a "4-season chaos token" or a "viable new faction"? If the latter, consider: splinters start at Mandate 2 minimum, or splinter assets can include the contested Influence of Inner Circle NPCs who backed the runner-up (already in the spec at §2.4 but not implemented as pool injection).

4. **Author `settlement_adjacency_map.yaml`.** The graph cannot be formally tested without it. This is the prerequisite for the adjacency mechanic to be canonical rather than provisional.

5. **RM emergence speed.** Consider whether a per-settlement minimum Order threshold of 0 (rather than ≤ 1) would slow the cascade to a more manageable rate. Current ≤ 1 triggers on first Order-drop, which happens early under normal warfare pressure.
