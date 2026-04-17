# VALORIA — Rendering Stability Budget
## Status: CANONICAL (ED-668)
## Date: 2026-04-17
## Single source of truth for all RS inputs and outputs across all systems.
## Cross-references: params_threadwork.md §RS Track, §Gap Self-Closure, §WC; params_core.md §RS Baseline Decay; peninsular_strain_v1.md §3.1, §4.3; threadwork_v30.md §5.2; victory_v30.md §6; calamity_radiation_v30.md; arc_register.md §II ARC-S32.
## Starting RS: TTRPG default 60; BG default 72. RS = 0 → Rupture (shared loss).

---

## RS DRAIN SOURCES (per season unless noted)

### Passive Drains (fire automatically at Accounting)

| Source | Rate | Condition | Authority |
|---|---|---|---|
| Winter annual drift | −1/year (−0.25/season average) | Unconditional | params_core §RS Baseline Decay PP-255 |
| Gap persistence (per open Gap) | Object: 0; Relational: −1; Field: −2; Structural: −3; Foundational: −5 | Per Gap per season until self-closure or Mending | params_threadwork §Gap Self-Closure PP-604 |
| Lock chronic drift (per Lock) | Object: 0; Personal: −1; Relational: −1 (→−2 at season 4+); Field: −2 (→−3); Structural: −3 (→−5) | Per Lock per season, escalating | params_threadwork §Gap Self-Closure PP-604 |
| Peninsular Strain 9–10 | −1/season additional | While Strain counter ≥ 9 | peninsular_strain_v1 §4.3 |

### Event-Driven Drains (fire on occurrence)

| Source | Cost | Condition | Authority |
|---|---|---|---|
| Battle on Valorian soil | −1 per battle | Per battle resolved | peninsular_strain_v1 §3.1 |
| Campaign/War scale battle | −2 per battle | Mass battle at Campaign or War scale | peninsular_strain_v1 §3.1 |
| Siege (sustained) | −1/season | Per besieged territory per season | threadwork_v30 §5.2 |
| Einhir site under siege | −1 additional | Siege on territory containing Einhir site | threadwork_v30 §5.2 |
| Thread operation — Partial/Failure | −1 to −2 per degree table | Per failed/partial Thread operation | threadwork_v30 §5.2 |
| FR Lock (immediate) | −1 to −3 | Per Lock placed | threadwork_v30 §5.2 |
| FR Dissolution | −3 to −8 | Per Dissolution | threadwork_v30 §5.2 |
| Past-Oriented Pulling | −3 minimum | Per POP | threadwork_v30 §5.2 |
| Substrate Saturation (mass battle) | −1 at battle end | If Saturation Counter ≥ 3 at battle end | params_threadwork §Substrate Saturation PP-606 |
| Micro-Gap persisting to Accounting | −1 | If micro-Gap not closed same scene | threadwork_v30 §5.2 |
| Popular Uprising | −1 | Per uprising (violence) | peninsular_strain_v1 §3.1 |

### TS 90+ Reality Strain
Practitioners at TS 90+ exert passive RS strain. Rate: per threadwork_v30 §5.2 degree table (operation-dependent, not passive). [GAP: No standalone passive drain rate specified for TS 90+ existence alone. The strain is operation-mediated, not ambient.]

---

## RS RECOVERY SOURCES

| Source | Rate | Condition | Authority |
|---|---|---|---|
| Mending (success) | +1 | Per successful Mending | threadwork_v30 §5.2 |
| Mending (overwhelming) | +2 | Per overwhelming Mending | threadwork_v30 §5.2 |
| Community Weaving (success) | +1 to +2 | Per successful Community Weaving | threadwork_v30 §5.2 |
| Southernmost expedition Mending | +2/season | Per successful expedition season | threadwork_v30 §5.2 |
| WC ≥ 3 (Edeyja active Mending) | +2/season | While WC ≥ 3 | params_threadwork §WC PP-605 |
| BG Weave order (success) | +1 | Per successful BG Weave | threadwork_v30 §7.1 |
| BG Mend order (success) | +1 | Per successful BG Mend | threadwork_v30 §7.1 |
| Overwhelming Weaving at Relational+ | +1 | Per overwhelming Weaving at scale | threadwork_v30 §5.2 |

### WC Drain Modification

| WC Level | Effect on Drains |
|---|---|
| WC 0 | No modification |
| WC 1 | +1D all Thread ops (indirect: higher success rate reduces failure-driven drain) |
| WC 2 | All RS drain from Gaps and Locks halved |
| WC 3 | RS +2/season at Accounting (Edeyja active Mending) |

---

## PEAK DRAIN SCENARIOS

### Year 20–25 Campaign Peak (WC 0)

Assumptions: 2 Structural Locks (−6/season), 1 Structural Gap (−3/season), 2 battles/year on Valorian soil (−2/year = −0.5/season average), winter drift (−0.25/season), 4 practitioner operations/season with 25% failure rate (−1/season average from failures), 1 siege/season (−1/season).

| Source | Per Season |
|---|---|
| 2 Structural Locks | −6.0 |
| 1 Structural Gap | −3.0 |
| Winter drift | −0.25 |
| Battles (2/year) | −0.5 |
| Operation failures | −1.0 |
| Siege | −1.0 |
| **Subtotal passive + event** | **−11.75** |

With military escalation (4 battles/year, Peninsular Strain ≥ 9, mass battle Thread operations):

| Source | Per Season |
|---|---|
| 2 Structural Locks | −6.0 |
| 1 Structural Gap | −3.0 |
| Winter drift | −0.25 |
| Battles (4/year at Campaign scale) | −2.0 |
| Operation failures (8 ops/season) | −2.0 |
| Siege × 2 | −2.0 |
| Strain 9–10 additional | −1.0 |
| Substrate Saturation (2 battles) | −2.0 |
| Battle drain from victory_v30 §0.4 | −4.0 |
| **Peak drain** | **−22.25 to −23.25** |

**At RS 60 (TTRPG start), peak drain → Rupture in under 3 seasons.**
**At RS 72 (BG start), peak drain → Rupture in ~3 seasons.**

### Year 20–25 Campaign Peak (WC 3)

Same scenario with WC 3:

| Source | Modification |
|---|---|
| Structural Lock drain | Halved (−3.0 instead of −6.0) |
| Structural Gap drain | Halved (−1.5 instead of −3.0) |
| Edeyja Mending | +2.0/season |
| Net drain | **−14.75 to −15.75** |

WC 3 buys approximately 1–2 additional seasons before Rupture. Still terminal without Gap/Lock resolution.

---

## SURVIVAL ARITHMETIC

The RS budget demonstrates that RS preservation requires:
1. **WC ≥ 2** to halve Gap/Lock drain (saves ~4.5 RS/season at peak).
2. **WC 3** for Edeyja Mending (+2/season).
3. **Gap resolution** (Mending or self-closure) to eliminate the largest drain source.
4. **Lock resolution** where possible to eliminate chronic drift.
5. **Military restraint** to limit battle RS costs and Peninsular Strain.

No single action is sufficient. WC 3 + concentrated mass battle Mending is the singular viable endgame path (throughline #3). See arc_register §II ARC-S32 (Mending Trap) for the practitioner Coherence budget analysis.

---

*Budget maintained by valoria-orchestrator. Update in same commit as any RS source creation or modification.*
