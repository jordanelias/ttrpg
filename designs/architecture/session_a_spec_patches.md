# Session A — Spec Patches (Ready for Propagation)

**Date:** 2026-04-19  
**Status:** ALL PATCHES PROPAGATED  
**Commit scope:** 6 patches + 1 new action + 1 backstory strike

---

## Patch 1: Three-Scale Resolution Model

**Target:** `params/bg/phases.md` — insert before Phase 4 Resolution Priority Order

**Add:**

```
## Three-Scale Resolution Model (PP-TBD)

Each season resolves in three layers, bottom-up:

1. **Settlement layer** (resolves first). Infrastructure actions: Church building construction,
   Guild trade operations, Crown ministerial placement, RM community organizing, governor
   appointments (including bishop appointments per PP-TBD). Settlement Order and Prosperity
   update. Black markets emerge (Order ≤ 1, no governor) or resolve (Order ≥ 3). Governor
   authority checks fire.

2. **Province layer** (resolves second). Fragmentation checks using updated settlement data.
   Accord recalculates from settlement Order floor-average. Province PV recalculates from
   settlement Prosperity weighted by controller alignment. Military movement along settlement
   adjacency graph. Mass battles resolve at settlement nodes. Territorial transfer.

3. **Peninsula layer** (resolves third). RS/CI/IP/PI/Strain clocks update from province-level
   events. Altonian pressure evaluated. Victory condition check against updated PV totals.
   Warden emergence. Season advances.

Control flows upward: settlement infrastructure → province Accord/PV → peninsula victory.
Pressure flows downward: peninsula events → province consequences → settlement disruption.
```

---

## Patch 2: Bishop Appointment (Church Domain Action)

**Target:** `params/bg/faction_actions.md` — add after Church — Cardinal Focus (PP-430)

**Add:**

```
### Church — Ecclesiastical Appointment (PP-TBD)
**Type:** Consul Outward (Church only).
**Prerequisite:** Target settlement has Church building ≥ tier 2 (Church or Cathedral).
Target settlement has no governor OR existing governor Disposition toward Church ≥ +2.
**Roll:** Influence vs Ob 1.

| Degree | Effect |
|--------|--------|
| Overwhelming | Church bishop-governor installed. Settlement governance transfers to Church.
                 Accord +1 in settlement (population accepts — bishop was already the de facto
                 authority). PT +1 in territory. |
| Success | Church bishop-governor installed. Settlement governance transfers to Church.
            Accord unchanged. |
| Partial | Appointment contested. Governor remains. Church Stability −1 (institutional
            embarrassment). PT unchanged. |
| Failure | Appointment rejected. Controlling faction gains awareness of Church governance
            ambition. No Casus Belli generated (appointment is non-military). |

**Notes:**
- Does NOT generate Casus Belli (non-military institutional action).
- Province fractionalizes if settlement controller now differs from Seat holder.
- Fragmentation checks fire at next Accounting for affected province.
- This action is the pre-Seizure accumulation path. Mass Seizure at CI 60+ remains
  the formal political formalization of settlement-level Church governance.
```

**Propagation:**
- `settlement_layer_v30 §3.2` (Governor Assignment): add bishop-governor as a governor type
- `ci_seizure.md`: add note that bishop appointment is the pre-Seizure path; Mass Seizure formalizes accumulated settlement control
- `npc_behavior_v30 §8.2` Church Priority Tree: add to P4 default — "if Church building ≥ tier 2 in ungoverned settlement: Ecclesiastical Appointment"

---

## Patch 3: Secession Candidate Restriction

**Target:** `designs/provincial/fractional_province_ownership_v30.md §2.6`

**Add to Fragmentation Check Failure outcome:**

```
Secession candidates are limited to settlements controlled by a national faction
(Crown, Hafenmark, Varfell, Church, Löwenritter, Guilds, Schoenland). Settlements
already held by a subnational faction (RM, Wardens) or marked Uncontrolled are NOT
valid Secession candidates. If all non-Seat alien settlements are subnational, the
Failure outcome produces no Secession — treat as Partial instead (Order drop).
```

**Rationale:** B2-1 found RM→RM secession noise. Settlements already under subnational governance cannot secede further.

---

## Patch 4: RM Emergence Threshold Clarification

**Target:** `designs/provincial/faction_succession_split_v30.md §4`

**Change:**

```
BEFORE: "if settlement Order drops to 0 AND PT ≤ 1 AND local Disposition toward
         Yrsa Vossen is ≥ +3, RM may declare Settlement Emergence"

AFTER:  "if settlement Order = 0 (not merely ≤ 1) AND PT ≤ 1 AND local Disposition
         toward Yrsa Vossen is ≥ +3, RM may declare Settlement Emergence.
         Order = 0 is a hard threshold — Order 1 settlements are degraded but still
         governed; Order 0 represents complete governance collapse, which is the
         prerequisite for RM's alternative governance to fill the vacuum."
```

**Rationale:** B2-2 showed Order ≤ 1 fires too early, produces deterministic RM growth. Order = 0 creates genuine variance and makes RM grow through political leverage rather than settlement accumulation.

---

## Patch 5: Splinter Influence Split

**Target:** `designs/provincial/faction_succession_split_v30.md §2.4`

**Change the Influence row in the Asset Split table:**

```
BEFORE: | Influence | Each contender keeps pre-contest Influence. No split. |

AFTER:  | Influence | Winner: 60% (round down). Splinter: 40% (round down).
          Remainder lost (institutional capacity fragmented in succession crisis).
          Follows same split ratio as Mandate. |
```

**Rationale:** B2-3 showed Mandate floor has zero effect on splinter viability because Influence (which drives Fragmentation defense and Domain Action pools) was unsplit. With 60/40 Influence split, splinters have proportionally reduced capacity at both political (Mandate) and institutional (Influence) levels, making the Mandate floor meaningful.

---

## Patch 6: T2 Kronmark Small Garrison

**Target:** `params/bg/npc_priority_trees.md` — Crown Priority Tree

**Add to P4 Default:**

```
BEFORE: | 4 | Default | Maintain treaties. Defend territory. Govern. Consul/Senator. |

AFTER:  | 4 | Default | Maintain treaties. Defend territory. Govern. Consul/Senator.
          If T2 Kronmark is ungarrisoned AND any Varfell unit is active in T4:
          deploy minimum garrison to T2 (1 unit, Legionary Inward). Crown's breadbasket
          must not be left exposed when Varfell has forward-deployed forces. |
```

**Rationale:** B3-3 showed Varfell Route A (T4→T2→T1) bypasses T14's Fort 3 entirely. T2 has no fort and no canonical garrison requirement. Without this priority tree entry, Crown's food supply (T5 Feldmark depends on T2 as administrative hub) is structurally undefended.

**Propagation:** `npc_behavior_v30 §8.3` Crown NPC Priority Tree — same addition.

---

## Patch 7: Strike Almud's Father Assassination Backstory

**Target:** Any doc referencing the prior king's assassination as settled backstory.

**Change:** The prior king's assassination is no longer pre-game canon. It is replaced by the Royal Crisis Tension Card (to be specified in Session C Tensions Deck), where one of the current Royal family members (Almud, Lenneth, or Torben) faces an assassination fuse that fires at S8+.

**Search for references:** `character_histories_v30.md` (Stage 4 catalysts may reference the prior assassination), `npc_character_analyses_v30.md` (Almud's backstory), `worldbuilding_v30.md` (historical timeline).

**Note:** Full propagation requires reading these docs in a fresh session to identify and modify specific passages. This patch is flagged for propagation — do not commit modifications to these files without reading them first.

---

## Propagation Checklist (for next session)

| Patch | Target files | Status |
|-------|-------------|--------|
| 1 (Three-scale) | `phases.md` | **DONE** — e89d196 |
| 2 (Bishop appointment) | `faction_actions.md`, `settlement_layer_v30 §3.2`, `ci_seizure.md`, `npc_behavior_v30 §8.2` | **DONE** — e89d196 |
| 3 (Secession restriction) | `fractional_province_ownership_v30 §2.6` | **DONE** — e89d196 |
| 4 (RM threshold) | `faction_succession_split_v30 §4` | **DONE** — e89d196 |
| 5 (Splinter Influence) | `faction_succession_split_v30 §2.4` | **DONE** — e89d196 |
| 6 (T2 garrison) | `npc_priority_trees.md`, `npc_behavior_v30 §8.3` | **DONE** — e89d196 |
| 7 (Backstory strike) | `npc_character_analyses_v30_infill`, `narrative_scenario_chains`, `arcs_10_18` | **DONE** — 7da338a. character_histories_v30 and worldbuilding_v30 had no assassination refs. |
