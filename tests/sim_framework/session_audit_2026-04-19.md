# Valoria — Session Audit: Simulation Batches + Ignition Analysis

**Date:** 2026-04-19  
**Scope:** Quality and legibility audit of all work committed this session  
**Documents audited:** 4 sim batch results, 4 sim scripts, 1 design analysis  
**Commits:** 6ea1f3e, acfe32d, 8088bc3, d195dbc, c5be6fc

---

## Audit Summary

**Overall quality: GOOD with corrections needed.** Findings are substantive and design-relevant. Methodology is appropriate for pre-engine-v4 targeted testing. However: three results docs contain known errors that aren't marked as superseded, gap flags aren't consolidated, and the ignition analysis needs revision per Jordan's feedback on assassination timing.

**Legibility: ADEQUATE for Jordan, POOR for a cold reader.** The docs assume familiarity with prior sessions and canonical sources. A new reader would not know which findings are current, which are superseded, or where to find the master gap list. Fixing this requires a summary index, not rewrites of individual docs.

---

## Issue 1: Superseded Findings Not Marked

**Three committed results docs contain findings that later batches invalidated.**

| Doc | Finding | Superseded by | Status in repo |
|-----|---------|--------------|----------------|
| arc_test_results.md (B1) | "Secession cooldown needed (2-season post-Consolidation)" | B2-1: cooldown has zero effect; root cause is RM→RM secession, not churn | **No correction marker** |
| arc_test_results.md (B1) | RM Inf=55, PV totals fully deterministic across seeds | B2 bug fix: RM Inf was inflating on RM→RM no-ops; same-season race masked cooldown | **No correction marker** |
| arc_test_batch3_results.md (B3) | B3-1 Church builds PT from low starting values; Assert drives CI | B4-1: T9 PT=5 at game start (canonical core.md); Piety Yield hits cap from S1; Assert irrelevant | **Flagged in B4 gap list but B3 doc unchanged** |
| arc_test_batch3_results.md (B3) | B3-5 suppression race: Challenge supplements structural | B4-1: PP-431-COR — Challenge replaces structural, not supplements | **Flagged as re-run needed; B4-1 provides corrected results** |

**Fix needed:** Add `<!-- [PARTIALLY SUPERSEDED — see Batch 2/4] -->` markers to the top of B1 and B3 results docs, with specific references to which findings are invalidated and which remain valid.

**What remains valid from B1:** Settlement adjacency path-constraint model, fractional PV re-derivation, succession contest variance, RM ascent arc shape. These were not affected by the sim bugs.

**What remains valid from B3:** RS decay timeline (fully deterministic, no dice involved), Fort constraint analysis (T14 impassable at Mil 4, Route A too easy), IP/Vanguard deployment timing, campaign arc shape (three-act structure). These don't depend on the bugged CI/suppression model.

---

## Issue 2: Dice System Inconsistency

**B1–B2 use simplified d10 (TN 7: 7+ = 1 hit). B3–B4 use full canonical d10 (1=−1, 7–9=+1, 10=+2).**

The simplified model has P(hit per die) = 0.4. The full model has E(net per die) = 0.4 (same expected value) but different variance: the 10=+2 and 1=−1 rules create fatter tails. This means B1–B2 results have slightly narrower outcome distributions than B3–B4.

**Impact:** Low. The arc-level findings (which factions win, when arcs resolve, which mechanics matter) are driven by pool/Ob ratios, not by tail probabilities. The dice difference affects individual roll outcomes but not the statistical conclusions across 5 seeds.

**Fix needed:** None for existing docs. Engine_v4 should use the full canonical dice system. Note in any master index that B1–B2 use the simplified system.

---

## Issue 3: Gap Flag Consolidation

**25 gap flags across 5 docs. No master list. Some gaps are duplicated; some are resolved by later batches.**

**Consolidated master gap list (current status):**

### Resolved by later batches:
| Gap | Raised | Resolved |
|-----|--------|----------|
| PP-431-COR not modeled | B3 | B4-1 (corrected sim) |
| Secession cooldown needed | B1 | B2-1 (wrong mechanism — need Secession candidate restriction instead) |

### Open — spec fixes required before PP-666 canonization:
| # | Gap | Source |
|---|-----|--------|
| 1 | Secession candidates must exclude subnational factions (RM→RM noise) | B2 |
| 2 | RM emergence threshold: clarify Order=0 (not ≤1) | B2 |
| 3 | Splinter Influence split needed if durable rivals intended | B2 |
| 4 | settlement_adjacency_map.yaml not authored | B1 |
| 5 | Fractional stake disposition on faction succession split | B1 |

### Open — design review required:
| # | Gap | Source |
|---|-----|--------|
| 6 | ~~CI seasonal cap vs Piety Yield (T9 SW5 PT5 = +5/season, cap saturated from S1)~~ — **RESOLVED ED-721 (2026-04-20)**: formula ambiguity. PT_tier is non-linear (PT 5 → 1.0; PT 4 → 0.5; PT 3 → 0.25; PT 2 → 0.10; PT ≤ 1 → 0). T9 yields 1 CI/season floored. Cap not saturated. B3/B4 results based on literal-PT formula are invalidated — flagged for re-run on corrected engine_v3. | B3, revised B4 |
| 7 | ~~Assert irrelevant once Piety Yield saturates cap~~ — **RESOLVED ED-721**: Assert remains mechanically relevant under canonical PT_tier table. | B3, revised B4 |
| 8 | T2 Kronmark garrison not in Crown priority tree (Route A too easy) | B3 |
| 9 | AER generation mechanic not found in any read doc | B3 |
| 10 | Warden emergence mechanics post-RS40 unspecified | B3 |
| 11 | Campaign-scale vs standard battle distinction undefined | B3 |
| 12 | PI upper-bound effects trivially met by Crown M=5 | B4 |
| 13 | Coup Counter advancement sources not canonical | B4 |
| 14 | Coup effect on Crown Mandate unspecified | B4 |
| 15 | Seizure Failure consequences not tracked in any sim | B4 |
| 16 | Treaty mechanic interaction with Strain not modeled | B4 |

### Open — data gaps:
| # | Gap | Source |
|---|-----|--------|
| 17 | Province base PV approximated in B1; canonical values found in B4 (victory.md) | B1/B4 |
| 18 | Contender pools for non-Varfell factions not canonical | B1 |
| 19 | RM Disposition toward Yrsa Vossen not tracked at settlement level | B1 |
| 20 | Consolidation Influence pool source not specified | B1 |

---

## Issue 4: Ignition Analysis — Assassination Timing

**The committed ignition analysis (c5be6fc) proposes assassinations as game-start events.** Jordan's feedback revises this:

1. Assassinations should **succeed** (not be attempts with variable outcomes)
2. Should fire at **S8+ minimum** (~2 game years), not at game start
3. Consequences are specific per target:
   - **Lenneth dead** → Almud rage-driven revenge arc (not just "hardening" — active pursuit, Crown resources diverted to investigation)
   - **Torben dead** → Crown immediately attempts Elske retrieval from Altonia → direct Altonian provocation (IP spike, possible war)

**This changes the Tensions Deck concept fundamentally.** The deck as designed draws at S0 with immediate effects. Jordan's model is: the deck establishes *conditions* at S0 (who is being targeted, what crisis is building), but the *event* fires later (S8+). This makes the Tensions Deck a fuse, not a detonator — the player sees the fuse burning but can't necessarily stop it.

**Revised Tensions Deck model:**

| Phase | Timing | Function |
|-------|--------|----------|
| **Seed** | S0 (game start) | 2 Tension Cards drawn. Cards specify: which systems are under pressure, which NPCs are activated, what conditions are building. Visible to player as "brewing tensions" — narrative signals, NPC dialogue, atmospheric events. |
| **Escalation** | S1–S7 | Tension conditions intensify each season. Player can attempt to intervene (divert resources, make diplomatic moves, investigate). Intervention is possible but costly — it competes with normal faction-building for action slots. |
| **Ignition** | S8+ | Tension resolves into a specific event. If the player didn't intervene successfully: the event fires (assassination succeeds, famine hits, coup threshold crosses). If the player did intervene: the event is averted or modified. |

This is a better model. It creates the early-game engagement the design needs (player is aware of building tensions from S1, must decide how to allocate attention) without eliminating the passive-build phase entirely. The first 7 seasons have both buildup AND tension management. The ignition event at S8 disrupts whatever equilibrium has been established.

**The graduated Löwenritter autonomy system (Counter 0→1→2→3→4) already follows this pattern.** It's a fuse. The Tensions Deck should work the same way: a publicly visible countdown toward a crisis point.

---

## Issue 5: Legibility for Cold Readers

**The 5 docs have no reading order, no master summary, and no cross-reference index.** A reader encountering these for the first time would need to read all 5 docs to understand the findings, then mentally reconcile the B1 findings that B2 superseded, the B3 findings that B4 corrected, and the ignition analysis that Jordan's feedback revised.

**Fix: a one-page index document.** Should contain:

1. Reading order: Ignition analysis → B3 (high-level systems) → B4 (political systems) → B1/B2 (PP-666 provisional mechanics)
2. Known supersessions (which findings in which docs are no longer current)
3. The consolidated gap list (§Issue 3 above)
4. The revised Tensions Deck timing model (§Issue 4 above)
5. The campaign arc shape summary from B3 (the three-act structure: expansion S1–10, seizure crisis S10–14, external pressure S19–30) as the reference timeline

---

## Issue 6: Simulation Methodology — What's Tested, What's Not

**Coverage map after 4 batches:**

| System | Tested | Confidence |
|--------|--------|------------|
| Settlement adjacency (path constraint) | B1 | Medium — road edges only, no mountain/river/coastal |
| Fractional province ownership (PV, fragmentation, consolidation) | B1, B2 | High — multiple variants, bugs found and fixed |
| Faction succession split (contest, asset split, splinter) | B1, B2 | High — multiple seeds, mandate/influence levers tested |
| RM emergence (threshold, cascade, political momentum) | B1, B2 | High — Order=0 vs ≤1 tested, speed concerns identified |
| CI buildup / Mass Seizure timing | B3, B4 | High — multiple configs, PT values corrected in B4 |
| RS decay (proximity gradient, band crossings) | B3 | High — fully deterministic, verified |
| Fort constraint (Varfell breakout routes) | B3 | High — 3 routes × 5 seeds, stall points identified |
| IP escalation / Altonian Vanguard | B3, B4 | Medium — Vanguard advance modeled, AER not |
| Hafenmark CI suppression (structural + Parliamentary Challenge) | B3, B4 | High — PP-431-COR corrected in B4 |
| PI track dynamics | B4 | High — multiple configs, stability confirmed |
| RDT/TD track (Reformed Doctrine as Seizure defense) | B4 | Medium — simplified CI growth model |
| Accord revolt cascade | B4 | Medium — garrison model simplified, treaty recovery absent |
| Löwenritter Coup timing and aftermath | B4 | Medium — Counter advancement stochastic (canonical sources unknown) |

| System | NOT tested | Reason |
|--------|-----------|--------|
| Mass battle (Part B full resolution) | No sim | Engine_v4 Phase 3 scope |
| Church infrastructure buildup at settlement scale | No sim | Needs settlement-level Church 4-axis model |
| AER generation | No sim | Mechanic not found in any read doc |
| Treaty / submission mechanics | No sim | Engine_v4 Phase 4 scope |
| Food vulnerability (Hafenmark T5/T2 dependency) | No sim | Canonical rate not specified |
| Thread operations in battle | No sim | Canonical pool/Ob not read |
| Multi-faction CI suppression (Crown + Hafenmark) | No sim | Needs Crown suppression as Mandate drain, not fragmentation Ob |
| NPC priority tree execution (full AI) | No sim | Engine_v4 Phase 4 scope |
| Event card system | No sim | Content unwritten |
| Tensions Deck / ignition mechanics | No sim | Proposed this session, not yet simulated |

---

## Issue 7: Quality of Design Recommendations

**Each batch produced specific, actionable recommendations. Assessment:**

| Recommendation | Quality | Action needed |
|----------------|---------|---------------|
| B2: Restrict Secession candidates to national factions | Good — addresses root cause | Write spec patch |
| B2: RM emergence Order=0 threshold | Good — produces correct arc shape | Write spec patch |
| B2: Splinter Influence split decision | Good — identifies the real lever | Jordan design decision |
| B3: Review CI cap vs Piety Yield at T9 | Critical — Assert is mechanically irrelevant | Jordan design decision (SW values or cap) |
| B3: T2 garrison in Crown priority tree | Good — specific, actionable | Write priority tree entry |
| B4: PP-431-COR confirmed correct | Good — rerun validated | No further action |
| B4: PI track upper-bound review | Valid concern, low priority | Defer to engine_v4 |
| B4: Graduated Löwenritter autonomy | Excellent — replaces binary coup with richer state | Write spec (per Jordan's conversation feedback) |
| Ignition: Tensions Deck | Excellent concept, timing needs revision per Jordan | Revise timing model (S0 seed → S8+ fire) |
| Ignition: Niflhel Provocation | Good — extends existing intelligence system | Write priority tree entry |
| Ignition: No new faction needed | Correct — analysis is thorough | No action |

---

## Recommended Immediate Actions

**1. Add supersession markers to B1 and B3 results docs.** One-line banners noting which findings are corrected by later batches. Prevents misreading.

**2. Create a master index document** (`tests/sim_framework/sim_coverage_index.md`) containing: reading order, supersession list, consolidated gap list, campaign arc shape summary.

**3. Revise ignition analysis** for assassination timing (S8+ fire, succeed-on-fire, Tensions Deck as fuse-not-detonator model). Incorporate Lenneth→Almud-revenge and Torben→Elske-retrieval consequences.

**4. Write the three spec patches that are clearly ready:**
- Secession candidate restriction (fractional_province_ownership_v30 §2.6)
- RM emergence threshold clarification (faction_succession_split_v30 §4)
- Graduated Löwenritter autonomy (replace binary coup in core.md)
