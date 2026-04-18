# Simulation Report — Mending 0-Coherence Impact on Metaphysical Stability
## Date: 2026-04-17
## Status: CANONICAL SIM OUTPUT
## Scope: Skeleton simulations assessing impact of Mending Coherence cost removal (campaign_architecture_v1 §3.2) on RS trajectories, practitioner Coherence, arc integrity, and RS budget assumptions.
## Canonical parameters: params_threadwork.md (canonical), campaign_architecture_v1.md §3.2, rs_budget.md, wc_survival_spine.md, arc_register.md §II
## Sims: SIM 1 (seasonal fatigue throttle) · SIM 2 (Coherence trajectories old vs new) · SIM 3–4 (RS budget impact) · SIM 5 (phase-transition stochastic) · SIM 6 (ARC-S34 viability)

---

## Ruling Required Before Propagation

**⚠ CONTRADICTION — OW Coherence cost (P1 — blocks propagation):**

| Document | OW Mending Coherence cost |
|---|---|
| `campaign_architecture_v1 §3.2` | −1 |
| `params_threadwork` degree table (cites §3.2 as authority) | 0 |

`params_threadwork` is the more recently edited document and explicitly cross-references `§3.2` as the source of the asymmetry. Its degree table (0 for all degrees including OW) is treated as authoritative for all sims below. The architectural doc requires correction.

**Jordan must confirm:** Is OW Mending cost 0 or −1? The architectural doc implies −1 as a philosophical hedge ("even aligned work under extreme strain"); the params table stripped it entirely.

---

## SIM 1 — Seasonal Fatigue as Primary Throttle

**Question:** Does the +1 cumulative Ob fatigue (resets each season) adequately replace Coherence cost as a Mending limiter?

**Target:** Field-established Gap (Ob 5 base) — primary active Gap type in a mid-campaign year.

| Practitioner | Pool | Optimal Mendings/season | E[RS]/season | Stop condition |
|---|---|---|---|---|
| Edeyja (Spirit 6, TS 90) | 24D | 5 | +6.35 | Mend #6 E[RS] turns negative |
| Expert (Spirit 5, TS 70) | 20D | 3 | +3.09 | Mend #4 E[RS] turns negative |
| Skilled (Spirit 4, TS 60) | 17D | 2 | +1.40 | Mend #3 E[RS] turns negative |
| Journeyman (Spirit 2, TS 50) | 12D | **0** | **−0.44** | Mend #1 already E[RS] < 0 |

**Finding:** Seasonal fatigue is an effective throttle for Skilled+ practitioners. It self-corrects: once expected RS recovery turns negative, rational play stops Mending. The system is smooth without Coherence cost.

**Finding — Journeyman targeting:** Journeyman-tier practitioners (Spirit 2, TS 50, 12D) have **negative expected RS recovery at Field Ob 5**. They should only Mend Relational-scale Gaps (Ob 2–3) where E[RS] is positive. This is a player-facing design note, not a rules change.

---

## SIM 2 — Coherence Trajectories: Old vs New

**Question:** How does removing Coherence cost change practitioner long-term Coherence? Does Rendering Crisis remain possible?

**Practitioner:** Expert (20D), 2 Mendings/season, +1 Coherence recovery/season.

| Mode | Rendering Crisis rate (30 years) | Year 5 Coh | Year 10 Coh | Year 30 Coh |
|---|---|---|---|---|
| OLD (−1/S or OW) | 0% | ~1.1 | ~1.0 | ~1.0 |
| NEW-A (0 always, params reading) | 0% | 10.0 | 10.0 | 10.0 |
| NEW-B (−1/OW only, arch reading) | 0% | ~3.4 | ~1.5 | ~1.3 |

**Critical finding — old system hidden cost:** Under OLD, Expert practitioners equilibrated at **Coherence ~1 (Severed band)** for the entire campaign. Severed = +2 Ob to all Thread operations permanently. This was a significant unreported penalty: practitioners who Mended regularly were permanently operating at maximum impairment without hitting Rendering Crisis. The new rule eliminates this.

**Finding:** No Rendering Crisis from Mending alone under any interpretation. The fatigue Ob is the limiting mechanic, not Coherence.

---

## SIM 3–4 — RS Budget Impact

**Question:** How does the 10x increase in Mending capacity change the RS budget scenarios?

**Old budget assumption:** ~4 Mendings/year = +1 RS/season recovery. This was calibrated to the old system where Coherence pressure throttled Mending frequency.

### Community Mending Recovery Capacity (New)

| Configuration | E[RS/season] |
|---|---|
| Old baseline (4 Mendings/year total) | +1.0 |
| Edeyja alone (5 Mendings/season) | +6.35 |
| Edeyja + Expert | +9.44 |
| Edeyja + Expert + Skilled | +10.84 |
| Seasonal cap (±10/season) | +10.0 max |

Recovery capacity is **~10x the old assumption**. The seasonal cap (±10 net RS change per season) limits gains but is still a substantial buffer.

### Scenario Comparison (Net RS/season)

| Scenario | Old Net | New Net (Edeyja only) | New Net (E+Ex) | New Net (E+Ex+Sk) |
|---|---|---|---|---|
| A: Moderate, WC0 (−12.75 drain) | −11.75 | −6.40 | −3.31 | −1.91 |
| B: Peak Military, WC0 (−22 drain) | −21.00 | −15.65 | −12.56 | −11.16 |
| C: WC3, Peak (−16.5 after WC savings) | −13.50 | −8.15 | −5.06 | −3.66 |

### Key findings:

**Scenario A (Moderate):** Old: Rupture at ~Season 5 from RS 60. New (Edeyja + Expert): net −3.31/season — from RS 60, survives ~18 seasons (4.5 years). Campaign survives to Year 5+ without WC. This significantly loosens the survival pressure in early game.

**Scenario B (Peak Military):** Still a death sentence at WC0. Time-to-rupture from RS 45 extends from 2.1 seasons to 3.6–4.0 seasons — marginally longer but not viable. WC3 still required for endgame.

**Scenario C (WC3):** Old: net ~−10/season. New (all 3 + WC3): net −3.66/season (−3.66 with seasonal cap considerations). Campaign survivable to Year 30 with active Mending. **WC3-is-singular-endgame conclusion holds** — without WC3, community Mending cannot offset peak drain. With WC3, it makes the difference viable.

**Finding — RS budget text is stale:** The budget's recovery assumption (+1/season) is wrong under the new rule. Scenarios A/B/C net calculations need updating. The narrative conclusion ("WC3 is singular endgame path") remains correct but for different reasons.

**Calibration note:** Scenarios in rs_budget.md are peak-pressure stress tests, not Year 1 baselines (confirmed by wc_survival_spine.md framing). SIM 5's 100% rupture rate was a modelling error (peak drain applied from Season 1); this is not a design problem.

---

## SIM 6 — ARC-S34 (Edeyja Burnout) Viability

**Question:** Does ARC-S34 (Edeyja Burnout from Mending) remain viable under the new rule?

**ARC-S34 text states:** "Edeyja's Coherence (9) depletes from repeated Mending at RS Critical. ~8 Mendings before Coherence 2; ~10 before Rendering Crisis."

Under 0-Coherence Mending: **this primary burnout path is eliminated.** Mending cannot drain Coherence.

### Edeyja Coherence Under Non-Mending Sources (30 years)

| Year | Avg Coherence | Band |
|---|---|---|
| 5 | 7.46 | Dissonant |
| 10 | 7.09 | Dissonant |
| 15 | 6.96 | Dissonant |
| 20 | 6.88 | Dissonant |
| 25 | 6.92 | Dissonant |
| 30 | 6.97 | Dissonant |

- **Rendering Crisis rate: 0%** from non-Mending sources alone (mass battle saturation, Knot loss, Shifting Object proximity, History Resonance)
- Equilibrium Coherence ~7 — comfortably Dissonant, never near the Coh ≤ 5 threshold that gates TE-15
- TE-15 secondary path (Structural Dissolution → crisis at Coh ≤ 5) **never activates** under normal conditions

**ARC-S34 as written is mechanically broken.** The arc requires Coherence to drain from Mending to reach ≤5, which is now impossible.

---

## Findings Summary

| # | Finding | Priority | Action |
|---|---|---|---|
| F1 | OW Mending Coherence cost: contradiction between campaign_architecture_v1 §3.2 (−1) and params_threadwork (0) | **P1 — blocks propagation** | Jordan confirms which is correct |
| F2 | Seasonal fatigue correctly throttles Mending; replaces Coherence cost as limiter without hidden ongoing impairment | Design valid | No action |
| F3 | Old system caused practitioners to operate permanently at Severed (Coh ~1, +2 Ob all ops) — silent long-term penalty, now gone | Design improvement | Acknowledge in propagation notes |
| F4 | Journeyman practitioners (Spirit 2, TS 50) have negative expected RS from Field Gaps; Relational-only targeting | Design note | Add player-facing guidance to arc_register or params |
| F5 | RS budget recovery assumption (+1/season) is 10x understated under new rule; scenarios need updated net figures | P2 | Update rs_budget.md scenarios |
| F6 | **ARC-S32 text** explicitly states "costs −1 Coherence regardless of outcome" — now wrong | **P1** | Update ARC-S32 in arc_register |
| F7 | **ARC-S34 (Edeyja Burnout)** primary path eliminated; arc text states Mending drains Coherence (false under new rule); TE-15 path needs a new activation condition | **P1** | Redesign ARC-S34 primary burnout path |
| F8 | WC3-is-singular-endgame conclusion holds; new rule makes WC3 outcomes more decisive (better) | Design valid | No action on conclusion; update rs_budget narrative |
| F9 | wc_survival_spine note "Practitioner Coherence" as IP/expedition resource now partially wrong | P2 | Update wc_survival_spine resource tension table |

---

## Required Propagation (pending F1 ruling)

Once Jordan rules on OW cost:

1. **arc_register.md:** ARC-S32 text — remove "costs −1 Coherence regardless of outcome"; replace with seasonal fatigue framing.
2. **arc_register.md:** ARC-S34 — strike primary Mending-burnout path; redesign activation condition (suggest: Dissolution residue overuse + TE-15, or introduce external Coherence drain event).
3. **references/rs_budget.md:** Update scenario net figures (A, B, C) with community Mending recovery values.
4. **references/wc_survival_spine.md:** Update resource tension table (Practitioner Coherence row — Mending no longer competes with other ops for Coherence budget).
5. **designs/systems/campaign_architecture_v1.md §3.2:** Correct OW cost to match ruling.

