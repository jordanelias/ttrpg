# VALORIA — Rendering Stability Budget
## ED-668 | Status: CANONICAL
## Date: 2026-04-17
## Scope: Single source of truth for all RS drain and recovery sources
## Cross-references: params_threadwork.md, params_core.md, peninsular_strain_v1.md, victory_v30.md, calamity_radiation_v30.md, threadwork_v30.md §5, mass_battle_v30.md §A.10
## Canon compliance: A1 (Thread constitutive ground — RS measures substrate integrity)

---

## Starting Values

| Mode | Starting RS | Source |
|---|---|---|
| TTRPG | 60 (Strained band) | params_threadwork §RS Track |
| Board Game | 72 (Strained band) | params_board_game |
| Hybrid | 60 | params_threadwork |

---

## RS Drain Sources (All Negative)

### Passive / Environmental

| Source | Rate | Condition | Document |
|---|---|---|---|
| Baseline annual decay | −1/year (−0.25/season) | Always active | params_core §RS Baseline Decay PP-255 |
| Gap persistence | −4/season per Gap | While Gap exists | params_threadwork §RS Track |
| Lock chronic drift | −1 to −2/season per Lock | While Lock exists | params_threadwork §RS Track |
| Strain 9–10 additional drain | −1/season | While Peninsular Strain ≥ 9 | peninsular_strain_v1 §4.3 |

### Operation-Driven

| Source | Cost | Condition | Document |
|---|---|---|---|
| Dissolution Success | −5 | Per operation | params_threadwork §RS Track |
| Dissolution Failure | −8 | Per operation | params_threadwork §RS Track |
| POP Success | −3 minimum | Per operation; scales with temporal displacement | params_threadwork §RS Track |
| Mass battle RS ×3 multiplier | ×3 on all Thread RS costs | During mass battle | params_threadwork §Mass Battle Thread RS PP-601 |
| Substrate Saturation (≥3 ops/turn) | −1 at battle end | Counter ≥3 at battle resolution | params_threadwork §Substrate Saturation PP-606 |

### Event-Driven

| Source | Cost | Condition | Document |
|---|---|---|---|
| Battle on Valorian soil | −1 | Per battle resolved | peninsular_strain_v1 §3.1 |
| Campaign/War scale battle | −2 | Per battle at Campaign/War scale | peninsular_strain_v1 §3.1 |
| Siege | −1 | Per season of active siege | params_threadwork §RS Track |
| Popular Uprising (Accord 0) | −1 | Per uprising event | peninsular_strain_v1 §3.1 |
| TS 90+ Reality Strain | −1/season | Per practitioner at TS 90+ | threadwork_v30 §5.2 |
| Southernmost cracking (ARC-S15) | +1 to +2/season additional | RS ≤ 50 without Weaving stabilization | arc_register §II ARC-S15 |

---

## RS Recovery Sources (All Positive)

| Source | Rate | Condition | Document |
|---|---|---|---|
| Mending Success | +1 | Per successful Mending operation | params_threadwork §RS Track |
| Mending Overwhelming | +2 | Per Overwhelming Mending | params_threadwork §RS Track |
| Weaving Overwhelming (Relational+) | +1 | Per Overwhelming Weaving at Relational+ scale | params_threadwork §RS Track |
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
- From RS 60: Fragile band by Season 8. Fractured by Season 13.

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
- From RS 45 (Fragile): Rupture in under 2 seasons.

### Scenario C: Year 20–25, WC 3
- Same drain as Scenario B: ~−21 to −23/season
- WC 2 halves Gap/Lock drain: −8 → −4, −3 → −1.5 = saves ~5.5/season
- WC 3 adds +2/season
- Recovery: Edeyja Mending + player Mending = +3/season
- **Net: ~−10 to −12/season**
- From RS 45: Fractured band by Year 24. Critical by Year 27. Survival to Year 30 viable with active Mending rotation.

### Conclusion: WC 3 is the singular endgame survival path.

At WC 0, peak drain exceeds recovery capacity by ~20 RS/season. No combination of individual Mending operations can offset this — ARC-S32 (Mending Trap) confirms one practitioner's full Coherence budget covers ~2–3 seasons of passive decline.

At WC 3, drain is reduced to ~10–12/season and offset by +5/season recovery (WC bonus + Mending), producing a net decline of ~5–7/season — survivable to Year 30 with concentrated effort.

---

## Seasonal Cap

±10 net RS change per season. Applied at Accounting. Prevents single-season catastrophic swings from compounding operations. Does NOT prevent Rupture from sustained multi-season decline.

---

## Cross-References Requiring This Document

| Document | Section | What References RS |
|---|---|---|
| calamity_radiation_v30 | Full matrix | RS band → per-territory effects |
| victory_v30 | §5, §6 | Shared loss at RS 0; WC effects |
| peninsular_strain_v1 | §3.1, §4.3 | Battle RS costs; Strain additional drain |
| threadwork_v30 | §5 | RS thresholds; operation costs |
| clock_registry_v30 | Shared Clocks | RS range and starting values |
| npc_behavior_v30 | §4.3 | Warden RS override at RS ≤ 20 |
| arc_register | §II Thread Vectors | ARC-S32, S15, S34 |
| params_board_game | §RS Effects | BG RS threshold lookup table |
| settlement_layer_v30 | §7.1 | Extended timeline clock recalibration |

---

*Budget assembled from all canonical sources as of 2026-04-17. Corrected peak drain validates throughlines_2026-04-17 finding: WC 3 is the singular endgame survival path.*
