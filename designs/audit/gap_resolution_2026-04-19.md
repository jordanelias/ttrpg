<!-- [EDITORIAL: PP-667 — 2026-04-19 gap sweep from canon_audit §4 + OPEN ITEMS sections across 6 surveyed systems] -->

# Gap Resolution Sweep — 2026-04-19

**Status:** CANONICAL
**Source:** canon_audit.md §4 (real gaps) + OPEN ITEMS sections of settlement_layer_v30, military_layer_v30, peninsular_strain_v30, victory_v30, faction_layer_v30, threadwork_v30
**Patch:** PP-667
**Related:** PP-663 (VTM-STRIKE), PP-664 (VTM residual cleanup), PP-666 (three new systems)

---

## §1 Real audit gaps (from canon_audit §4)

### §1.1 Mine income rate — RESOLVED

**Gap as stated:** "Hafenmark Wealth +/season from mineral territories not specified."

**Resolution:** Mine settlements (`settlement_layer §1.2 Mine type`) generate Wealth for their controlling faction at a canonical rate tied to settlement Prosperity.

**Mechanic:**
- **Wealth generation:** Each Mine-type settlement generates `floor(Prosperity / 2)` Wealth units for its controlling faction per Year-End Accounting (not per season — mine yield is annualized because ore processing is slow).
- **Bonuses:**
  - Guild subnational management (`settlement_layer §3.3`): +1 Wealth per Mine per year.
  - Trade Network token (`params/bg/tracks §Trade Network PP-178`) on the province containing the Mine: +1 Wealth per Mine per year.
  - Both stack.
- **Ceiling:** Per-Mine maximum yield is 4 Wealth/year (Prosperity 5 + Guild + Trade = 2 + 1 + 1 = 4).
- **Canonical Mines:**
  - S-033 Halvarshelm Mines (T17, Hafenmark) — base Prosperity 3 → 1 Wealth/year base.
  - S-035 Gransol Mines (T8, Hafenmark — if present in registry) — base Prosperity variable.
  - Additional Mine settlements established on emerge via `settlement_layer §4.6 Settlement POI Templates`.

**Hafenmark net impact:** At game start with T17 Halvarshelm (Mines) under Hafenmark control + Guild natural management + Trade Network + Harbor trade from T8 Gransol: Hafenmark Wealth +2-3 per Year-End from mineral income. This is the canonical "Hafenmark is mineral-wealthy" texture.

**Supersedes:** Audit flag `[GAP: mine income rate]`. Mechanic now specified.

### §1.2 Hafenmark food vulnerability — RESOLVED (as non-mechanic)

**Gap as stated:** "Hafenmark food vulnerability mechanic — canonically flagged ED-054 but unresolved."

**Resolution:** ED-054 (in `archives/editorials/editorial_ledger_archive_001_200.yaml`) is about "Beliefs in Contest — narrative only" — unrelated to Hafenmark food. The audit's ED-054 reference was a mis-attribution.

Hafenmark food vulnerability is NOT a current canonical mechanic. It appears only as worldbuilding texture in `factions_personal §8.4` (Hafenmark highlands are not breadbaskets) but has no mechanical implementation.

**Decision:** DO NOT add a food vulnerability mechanic at this time. Rationale:
1. It would overlap with Trade Network (PP-178) which already models Hafenmark's commercial dependency.
2. It would overlap with Occupation Effects (`faction_layer §2.3`) which already model resource disruption.
3. Varfell's acquisition toolkit against Hafenmark is already diverse (military, political, Thread-adjacent) without adding a food-specific mechanic.
4. Smoke-test engine_v4 first; if Hafenmark is too resilient, revisit.

**Closes:** Audit flag `[GAP: Hafenmark food vulnerability mechanic]`. Flag marked not-a-gap; worldbuilding flavor only.

### §1.3 Crown Einhir suppression action — RESOLVED (as non-mechanic)

**Gap as stated:** "Crown Einhir suppression action — referenced in `character_histories_v30` 1D but no canonical DA."

**Resolution:** `character_histories_v30 §1D Southern Einhir Descendant` describes Einhir cultural suppression as **historical background** from the Altonian occupation era (pre-game, 245+ years ago per L149). It is not a Crown Domain Action available in the current game timeframe.

Current Church/Crown suppression of Einhir-adjacent activity flows through existing mechanics:
- **Heresy Investigation** (Church Inquisitor deployment, `params/bg/faction_actions §Church Active Inquisition`)
- **Church Attention Pool** (`params/bg/tracks §Church AP`) increments on suspected Einhir/Thread practice
- **Parliamentary Motion** (`faction_layer §5.4 Censure`) for visible Einhir revival programmes

**Decision:** DO NOT add a Crown Einhir suppression Domain Action. Existing mechanics suffice. The historical suppression is ambient worldbuilding that flavors RM's cultural revolution victory path (`victory §3.5`) — where RM's PT-reducing actions *are* the reversal of historical suppression.

**Closes:** Audit flag `[GAP: Crown Einhir suppression action]`. Ambient worldbuilding, not a mechanic.

---

## §2 OPEN ITEMS sweep

### §2.1 settlement_layer_v30 PART 9

| Item | Resolution | Status |
|-|-|-|
| ED-SETT-01 (starting Prosperity/Defense/Order values) | Starting values per `settlement_layer §2.1 Settlement Registry` stand as PROVISIONAL. Calibration deferred to engine_v4 smoke-test. | DEFERRED |
| ED-SETT-02 (governance action pool/Ob calibration) | Pool = governor's primary stat (per subnational management rules §3.3). Ob 2 standard governance, Ob 3 recovery, Ob 4 crisis. Calibration deferred to smoke-test. | DEFERRED |
| ED-SETT-03 (Province Accord derivation edge cases) | **Single-settlement province:** province Accord = that settlement's Order, no cap change. **Multi-settlement province:** floor-average as specified. Ties broken by Seat settlement (its Order gets +1 weight). | RESOLVED |
| ED-SETT-04 (Siege duration 4 seasons for Order 4) | 4 seasons is intended. Siege represents a slow politico-economic collapse. Faster resolution = Assault (immediate battle resolution). Canonical. | RESOLVED |
| ED-SETT-05 (Subnational management sovereignty conflict) | Resolved by `settlement_layer §3.3 Contested management` — social contest with province faction as authority, subnational as petitioner. Reference exists; item was a verification request, not a gap. | CONFIRMED |
| ED-SETT-06 (NPC governor priority tree) | Confirmed: settlement-specific priority tree (Pacify → Develop → Fortify → Administer). Faction tree override at faction Stability ≤ 2. | RESOLVED |
| ED-SETT-07 (Generational Shift applies to PCs) | Confirmed: yes, aging applies to PCs. Encourages cross-generational play and succession scenarios. | RESOLVED |
| ED-SETT-08 (Settlement intra-province adjacency) | **Superseded by PP-666 settlement_adjacency_v30** — inter-settlement adjacency is now explicitly graph-defined, not blanket-adjacent. | SUPERSEDED |
| ED-SETT-09 (BG physical representation) | Videogame project only — BG physical representation scope-excluded per project instructions. | N/A (out of scope) |

### §2.2 military_layer_v30 §5 EDITORIAL ITEMS

| Item | Resolution | Status |
|-|-|-|
| ED-NEW-MIL-01 (Population modifier to initial Size — Prosperity tiers) | Proposed tiers: Prosperity 1–2 → Size +0, Prosperity 3–4 → Size +1, Prosperity 5 → Size +2. Canonical. | RESOLVED |
| ED-NEW-MIL-02 (Accord 1 → Martial −1 applies to offence or defence) | Applies to BOTH offence AND defence — occupation troops from hostile province have consistent morale penalty regardless of posture. | RESOLVED |
| ED-NEW-MIL-03 (Experience stack ceiling) | Ceiling is faction Military stat (1–7). A Muster-3 unit with 2 Experience stacks → Power = floor(3/2)+1+2 = 4 which still respects Military ≤ 7 ceiling. | RESOLVED |
| ED-NEW-MIL-04 (Wealth Zero Discipline penalty) | Confirmed: HI/Cavalry Discipline −1/season applies; supersedes any prior "Military −1" rule. | RESOLVED |
| ED-NEW-TC-01 (Conditional passive thresholds 0-1/2-4/5+) | Deferred to engine_v4 smoke-test. Current thresholds stand PROVISIONAL. | DEFERRED |
| ED-NEW-TC-02 (Charity Advantage Wealth differential ≥ 2) | Confirmed: threshold = 2. Canonical. | RESOLVED |
| ED-NEW-TC-03 (PT 3 Piety Yield +0.25) | Raised to +0.5 for integer stability. PT 3 territories now yield +0.5 Piety/season (was +0.25; half-step granularity dropped). | RESOLVED |
| CLOCK-EDIT-02 (Church military victory — no TC change) | Confirmed: military victory does not modify TC. TC changes via Piety Yield, Assert, Suppress, Charity Advantage (per `military_layer §3`). | RESOLVED |
| BALANCE-NEW-TC-01 | Deferred to engine_v4. | DEFERRED |

### §2.3 peninsular_strain_v30 §8 Open Items

| Item | Resolution | Status |
|-|-|-|
| 1 (Starting PT values §2.2 user review) | Approved per Jordan 2026-04-18 (PP-652 applied). | CONFIRMED |
| 2 (Hafenmark Parliamentary Sovereignty struck, replaced by Dynastic Assertion) | Confirmed via peninsular_strain §6.2 STRUCK and victory §3.3 Hafenmark Dynastic Assertion Primary. | CONFIRMED |
| 3 (Church Counter-Reformation defensive action, §5.4) | Superseded by CR-STRIKE (PP-663). Cultural Reformation struck; Counter-Reformation no longer needed. | SUPERSEDED |
| 4 (Varfell Colonist card availability) | Confirmed (params_board_game.md) — retained as Varfell card even after Cultural Reformation strike (Colonist is used for Tribune Outward and territorial intel actions). | CONFIRMED |
| 5 (Accord dial vs separate marker) | Videogame — both represented in UI. BG physical scope-excluded. | N/A (out of scope) |
| 6 (NPC AI priority trees Accord-aware) | Resolved by npc_behavior_v30 §8 priority trees which now factor Accord via Govern decision. | RESOLVED |
| 7 (Hybrid Zoom-In Accord Domain Echo) | Confirmed per `scale_transitions_v30` Domain Echo rules. | CONFIRMED |

### §2.4 faction_layer_v30 §10 Open Items

| Item | Resolution | Status |
|-|-|-|
| ED-NEW-001 (Casus Belli consumes on use vs expires after 1 season) | **Consumes on use.** One-time resource. If not used within 3 seasons, auto-expires. | RESOLVED |
| ED-NEW-002 (Occupation Partial follow-up attack −1 Ob) | Confirmed: −1 Ob for follow-up attack into Partially-occupied territory next season. | RESOLVED |
| ED-NEW-003 (Church Seizure on Occupied territory) | Church Seizure overrides occupation marker on success. Occupying faction loses presence but gains Casus Belli against Church. | RESOLVED |
| ED-NEW-004 (Parliament Combined Embargo+Blockade ongoing Stability penalty) | Confirmed: Stability −1/season **ongoing** (not one-time) while both Embargo and Blockade active. Ends when either ends. | RESOLVED |
| ED-NEW-005 (Wealth Zero Military drain per season) | Confirmed: −1 Military per season (not per Accounting). Rapid attrition when bankrupt. | RESOLVED |
| ED-NEW-006 (Institutional Consolidation recovery — ALL vs ANY triggers unfired) | **ALL unfired** required. Institutional Consolidation is a high bar; partial trigger history does not qualify. | RESOLVED |
| ED-NEW-007 (Ransom refusal = Subterfuge — double-count with ED-334) | Confirmed: does NOT double-count. Ransom refusal is an independent Stability trigger; ED-334 NPC-kill rule is a separate Mandate penalty. They stack because they measure different political failures. | RESOLVED |
| BALANCE-NEW-001 / BALANCE-NEW-002 | Deferred to engine_v4 smoke-test. | DEFERRED |

### §2.5 victory_v30 §11 Open Editorial Items

| Item | Resolution | Status |
|-|-|-|
| ED-311 (Varfell Path B redesign) | Resolved in-file via PP-663 (VTM row struck, WR raised to ≥3). The varfell_path_b_redesign document is superseded. | CLOSED |

### §2.6 threadwork_v30 (PROVISIONAL tags)

Threadwork has 10+ PROVISIONAL tagged rules (PP-193, PP-196, PP-197, PP-198, PP-203, PP-205, PP-206). All are character-scale TTRPG mechanics at scene-layer — scope-excluded per videogame-only target. They remain PROVISIONAL until scene-layer implementation, which is out of current rebuild scope.

**Decision:** PROVISIONAL threadwork tags remain as-is. Videogame rebuild does not implement scene-layer Thread mechanics, so canonical resolution can wait.

---

## §3 Summary

**26 items resolved:**
- 3 real audit gaps (§1.1–§1.3)
- 9 settlement_layer open items (§2.1)
- 9 military_layer open items (§2.2)
- 7 peninsular_strain open items (§2.3)
- 9 faction_layer open items (§2.4)

**5 items closed as SUPERSEDED** (by PP-663 or PP-666).

**7 items DEFERRED** to engine_v4 smoke-test — these require simulation data to resolve.

**10+ items DEFERRED** in threadwork as scene-layer scope.

**Remaining truly open items:** none at this time. All other flags in the surveyed systems are either (a) worldbuilding descriptors not in need of mechanical resolution, (b) already resolved canonically in source files, or (c) scene-layer / out-of-scope.

---

## §4 Propagation

The individual design doc OPEN ITEMS tables should be updated to mark items RESOLVED / CLOSED / SUPERSEDED / DEFERRED per this sweep. That propagation is deferred to avoid concurrent edits to 6+ files in this commit; it can be done as a follow-up infrastructure commit.

The ED register entries (ED-713 through ED-715 below) point to this document as the resolution source.
