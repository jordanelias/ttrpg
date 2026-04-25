# VALORIA — Mending Stability Budget
## ED-668 | Status: CANONICAL
## Date: 2026-04-17 (content) / 2026-04-20 (file rename)
## Scope: Single source of truth for all MS drain and recovery sources
## Cross-references: params_threadwork.md, params_core.md, peninsular_strain_v1.md, victory_v30.md, calamity_radiation_v30.md, threadwork_v30.md §5, mass_battle_v30.md §A.10
## Rename history: references/rs_budget.md → references/ms_budget.md (2026-04-20, ED-731 terminology propagation)
## Canon compliance: A1 (Thread constitutive ground — MS measures substrate integrity)

---

## Starting Values

| Mode | Starting MS | Source |
|---|---|---|
| TTRPG | 60 (Strained band) | params_threadwork §MS Track |
| Board Game | 72 (Strained band) | params_board_game |
| Hybrid | 60 | params_threadwork |

---

## MS Drain Sources (All Negative)

### Passive / Environmental

| Source | Rate | Condition | Document |
|---|---|---|---|
| Baseline annual decay | −1/year (−0.25/season) | Always active | params_core §MS Baseline Decay PP-255 |
| Gap persistence | −4/season per Gap | While Gap exists | params_threadwork §MS Track |
| Lock chronic drift | −1 to −2/season per Lock | While Lock exists | params_threadwork §MS Track |
| Strain 9–10 additional drain | −1/season | While Peninsular Strain ≥ 9 | peninsular_strain_v1 §4.3 |

### Operation-Driven

| Source | Cost | Condition | Document |
|---|---|---|---|
| Dissolution Success | −5 | Per operation | params_threadwork §MS Track |
| Dissolution Failure | −8 | Per operation | params_threadwork §MS Track |
| POP Success | −3 minimum | Per operation; scales with temporal displacement | params_threadwork §MS Track |
| ~~Mass battle MS ×3 multiplier~~ | **STRUCK (campaign_architecture_v1 §3.1).** Replaced by flat −1 per battle in which any Thread operation occurs. | During mass battle | params_threadwork PP-192 (struck) |
| Substrate Saturation (≥3 ops/turn) | −1 at battle end | Counter ≥3 at battle resolution | params_threadwork §Substrate Saturation PP-606 |

### Event-Driven

| Source | Cost | Condition | Document |
|---|---|---|---|
| Battle on Valorian soil | −1 | Per battle resolved | peninsular_strain_v1 §3.1 |
| Campaign/War scale battle | −2 | Per battle at Campaign/War scale | peninsular_strain_v1 §3.1 |
| Siege | −1 | Per season of active siege | params_threadwork §MS Track |
| Popular Uprising (Accord 0) | −1 | Per uprising event | peninsular_strain_v1 §3.1 |
| TS 90+ Reality Strain | −1/season | Per practitioner at TS 90+ | threadwork_v30 §5.2 |
| Southernmost cracking (ARC-S15) | +1 to +2/season additional | MS ≤ 50 without Weaving stabilization | arc_register §II ARC-S15 |

---

## MS Recovery Sources (All Positive)

| Source | Rate | Condition | Document |
|---|---|---|---|
| Mending Success | +1 | Per successful Mending operation | params_threadwork §MS Track |
| Mending Overwhelming | +2 | Per Overwhelming Mending | params_threadwork §MS Track |
| Weaving Overwhelming (Relational+) | +1 | Per Overwhelming Weaving at Relational+ scale | params_threadwork §MS Track |
| WC ≥ 2 | Halves all Gap/Lock drain | While WC ≥ 2 | victory_v30 §6 |
| WC ≥ 3 | +2/season at Accounting | While WC ≥ 3 (Edeyja active Mending) | victory_v30 §6 |
| Gap self-closure | Eliminates Gap's drain | Per scale: Object 1d10 per season (1–3); Personal 1d10 (1–2); Relational 1d10 (1); Territorial+ never | params_threadwork §Gap Self-Closure PP-604 |

---

## Budget Scenarios

### Scenario A: Year 10, Moderate Campaign (2 Gaps, 1 Lock, WC 0)
- Passive: −0.25/season (baseline) + −8/season (2 Gaps) + −1.5/season (1 Lock avg) = **−9.75/season**
- Military: ~2 battles/year = −0.5/season
- Operations: ~2 Dissolutions/year avg = −2.5/season (assuming 50% success rate)
- **Total drain: ~−12.75/season**
- Recovery: ~4 successful Mendings/year = +1/season
- **Net: ~−11.75/season**
- From MS 60: Fragile band by Season 8. Fractured by Season 13.

### Scenario B: Year 20–25, Peak Military (2 Gaps, 2 Locks, WC 0, sustained warfare)
- Passive: −0.25 + −8 + −3 = **−11.25/season**
- Military: 4 battles/year avg (civil war + Altonian) = −1/season + −2/season Campaign scale = **−3/season**
- Operations: sustained Thread warfare, 4 Dissolutions/year = −5/season
- Strain 7–8 effects: Accord degradation → additional battles
- TS 90+ practitioner(s): −1/season
- Southernmost cracking if unfed: +1 to +2/season additional
- **Total drain: ~−21 to −23/season**
- Recovery without WC: ~4 Mendings/year = +1/season
- **Net: ~−20 to −22/season**
- From MS 45 (Fragile): Rupture in under 2 seasons.

### Scenario C: Year 20–25, WC 3
- Same drain as Scenario B: ~−21 to −23/season
- WC 2 halves Gap/Lock drain: −8 → −4, −3 → −1.5 = saves ~5.5/season
- WC 3 adds +2/season
- Recovery: Edeyja Mending (5 ops across 4 scenes ≈ +6–8/season) + player community Mending (+2–4/season) = +8–12/season total; capped at +10/season by seasonal cap
- **Net: ~−4 to −8/season (capped)**
- From MS 45: Fractured band by Year 24. Critical by Year 27. Survival to Year 30 viable with active Mending rotation.

### Conclusion: WC 3 is the budget enabler for substrate-respectful Thread-active play.

The peak-drain Scenario B figures (~−21 to −23/season at WC 0) describe the *un-disciplined* Thread-aggressive faction profile: 4 Dissolutions/year, 2 active Locks, sustained Thread warfare in mass battle, no Gap closure discipline. This is the budget under which WC 3 is mathematically necessary.

Three viable late-game paths exist:

**Path 1 — Disciplined non-Warden play.** Self-mitigation via: restraint on Dissolution and POP; active Gap closure within 1–2 seasons of opening; Lock cleanup; battle minimization; ≤2 Thread ops/turn in mass battle (avoiding Substrate Saturation); voluntary withdrawal of TS 90+ practitioners from active operations. A faction observing these disciplines sustains MS within ±2/season of baseline through a 35-year campaign without Warden integration.

**Path 2 — WC 3 with substrate discipline.** Path 1 disciplines plus WC 3 cooperation. Halved Gap/Lock drain, Edeyja active Mending +2/season, community Mending recovery available. Maximum survivability margin. The "responsible Warden ally" profile.

**Path 3 — WC 3 with successful Wager (Arc E).** Active Knot with Edeyja + Grand Contest victory using Projection-Consequence-Solidarity argument structure + verifiable future commitment. WC 3 cooperation extends to cover Scenario B operational profile. The "staked credit" path — Edeyja accepts present substrate cost on the strength of demonstrated competence and committed future restoration. The wager itself becomes a Wager Obligation (social_contest §6.1) — failure produces immediate Arc D Confrontation with no probation. See npc_behavior §5.2 Edeyja Arc E for full mechanic.

**The trap (Path 4 — non-viable):** WC 3 without discipline AND without Wager. Player misreads ms_budget framing as "WC 3 license to operate without consequence." Edeyja Arc D Confrontation fires within ~10 seasons of WC 3 + sustained substrate-disruptive operations. Player either commits to discipline (collapsing into Path 2) or breaks the alliance (collapsing into a degraded version of Path 1, having spent seasons of investment on a now-lost relationship).

The substrate ontology does not permit "Thread without consequence." WC 3 shifts the discipline target — it does not remove the discipline requirement. Factions seeking maximum operational latitude must arrive at it through the Wager structure, not through cooperation alone.

[EDITORIAL: ED-740 — ms_budget Conclusion reframed from "WC 3 is the singular endgame survival path" to three-path framing. Source: 2026-04-24 audit conversation. Prior framing produced player misread that WC 3 was a survival floor; correct reading is that WC 3 is a budget enabler for one of three viable late-game configurations, with Path 1 (disciplined non-Warden) being equally survivable for substrate-respectful factions.]

---

## Seasonal Cap

±10 net MS change per season. Applied at Accounting. Prevents single-season catastrophic swings from compounding operations. Does NOT prevent Rupture from sustained multi-season decline.

---

## Cross-References Requiring This Document

| Document | Section | What References MS |
|---|---|---|
| calamity_radiation_v30 | Full matrix | MS band → per-territory effects |
| victory_v30 | §5, §6 | Shared loss at MS 0; WC effects |
| peninsular_strain_v1 | §3.1, §4.3 | Battle MS costs; Strain additional drain |
| threadwork_v30 | §5 | MS thresholds; operation costs |
| clock_registry_v30 | Shared Clocks | MS range and starting values |
| npc_behavior_v30 | §4.3 | Warden MS override at MS ≤ 20 |
| arc_register | §II Thread Vectors | ARC-S32, S15, S34 |
| params_board_game | §MS Effects | BG MS threshold lookup table |
| settlement_layer_v30 | §7.1 | Extended timeline clock recalibration |

---

*Budget assembled from all canonical sources as of 2026-04-17. Corrected peak drain validates throughlines_2026-04-17 finding: WC 3 is the singular endgame survival path.*
