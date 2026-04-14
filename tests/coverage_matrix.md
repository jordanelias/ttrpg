# Coverage Matrix — Active
# Full archive: tests/coverage_matrix_archive.md
# Last updated: 2026-04-14
# Total sim runs completed: 25 (see archive for full history)

## Open SIM-DEBT

## SIM-DEBT Register

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-DEBT-02 | SIM-D-04 | **STRUCK** — superseded by PP-234 (Social Contest System v2 redesign). Corroboration mechanics rebuilt. Subsumed by SIM-DEBT-03. |

*(old SIM-DEBT register entries above)*


| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-DEBT-01 | Debate system | RESOLVED. Mode C (SIM-D-02) confirmed: resistance dominates track movement; genre weight > pool size adjustments; 3-exchange Formal Debate → Compromise ~95%. CLASH strain calibration (2-3/exchange) analytically confirmed, scenario validation pending forced-CLASH run. | RESOLVED |
| AUD-TTRPG-01 | Modes A–G: Formula, Number Systems, Interaction Chains, Gap Detection, Core Principles, Playtest Burden, Cross-Mode | TTRPG | — | All tracks | All factions | All named NPCs | Full TTRPG mode | Complete | 11 P1s, 14 P2s, 4 P3s — see tests/aud_ttrpg_01.md |


## Open P1 Findings

## P1 Findings — Editorial Decisions Required

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-11 | X-03 | W-33 broken for Size≤2 units: Cohesion=2 insufficient when Size is binding constraint | RESOLVED — ST-TW-02 applied to threadwork_redesign_v25.md |
| F-27 | X-07 | Mass battle deadlock (HeavyCut vs HeavyArmour): no stalemate resolution rule | PATCHED — Add to mass_battle_v3: at 3+ consecutive turns with 0 damage dealt, units with no tactical option may withdraw one zone (costs movement, does not trigger pursuit). |
| F-30/F-33 | X-07/08 | Coup Counter: no successor rule on Grandmaster death | PROVISIONAL — On Grandmaster death with Coup Counter ≥ 1: Löwenritter selects highest-CR surviving named officer as acting Grandmaster. Coup Counter resets to 0. Provisional pending user approval. |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season; no seasonal cap on TC | PROVISIONAL — TC change cap: ±3 per season from Domain Actions (±5 from all sources combined). Provisional pending user approval. |
| F-45 | X-10 | Church Stability brake scope — suppresses Mandate-based TC only or all TC sources? | EDITORIAL — ED-049 added to ledger |
| F-52 | X-12 | No Stability recovery mechanic for externally damaged faction Stability | PROVISIONAL — Stability recovery: +1 Stability per season of no hostile Domain Actions targeting that faction + Stability ≤ 3 (slow natural recovery). Provisional pending user approval. |
## New P1 Findings (SIM-X-13 through X-16)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-58 | X-14 | RS 22 is 2 points from Dormant (Leap-disabled) threshold — any failed Weaving crosses the line globally | Open — campaign awareness item |


## Provisional Decisions Pending Application

## Provisional Decisions (from coverage matrix findings)

| Finding | Provisional Rule | Status |
|---------|-----------------|--------|
| F-27 | Mass battle stalemate: 3+ turns 0 damage → may withdraw one zone | Provisional — apply to mass_battle_v3 |
| F-30/F-33 | Coup Counter successor: highest-CR officer, Counter resets | Provisional — apply to designs/combat |
| F-43 | TC change cap: ±3/season Domain Actions, ±5 all sources | Provisional — apply to stage5_clocks or designs |
| F-52 | Stability recovery: +1/season with no hostile actions when Stability ≤ 3 | Provisional — apply to faction rules |


