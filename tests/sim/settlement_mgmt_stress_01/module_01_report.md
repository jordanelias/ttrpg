# Module 01 Report — Settlement Primitives

**Date:** 2026-05-13
**Session:** Mode G Module 1 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_01_primitives.py`
**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §1.1, §1.2, §1.3, §2.1

## Summary

Substrate module. Encodes settlement identity (37-entry §2.1 registry),
canonical type list (§1.2), stat schema (§1.3 three-stat block, 0–5 scale),
derived value formulas (§1.3 table), and the REVISED province-Accord rule
(province Accord = floor(mean(settlement Order)) per §1.3).

## Isolation tests — 15/15 PASS

| # | Test | Result |
|---|------|--------|
| T1 | Total registry count == 37 | PASS |
| T2 | Settlement IDs unique | PASS |
| T3 | Every ID matches `S-NNN` format | PASS |
| T4 | Kingdom settlement count == 35 | PASS |
| T5 | Valorsmark: 6 provinces / 15 settlements | PASS |
| T6 | Hafenmark: 4 provinces / 10 settlements | PASS |
| T7 | Varfell: 4 provinces / 10 settlements | PASS |
| T8 | Every type in registry is in canonical or extra-types set | PASS |
| T9 | Halvarshelm (Hafenmark) ≠ Halvardshelm (Varfell) | PASS |
| T10 | Stat range boundaries 0 and 5 accepted | PASS |
| T11 | Stat range −1 and 6 rejected | PASS |
| T12 | Derived value formulas match §1.3 (Pros×50, Def×20+Fort×30, Ord×20) | PASS |
| T13 | Province Accord worked example (Order 4,2,1 → 2) | PASS |
| T14 | Lookup by_id resolves correctly | PASS |
| T15 | Special-entity flag correct for Himmelenger / Schoenland | PASS |

## Findings — canonical inconsistencies surfaced (NOT silently reconciled)

### F1 — type-list divergence between §1.2 and §2.1
§1.2 enumerates 8 settlement types in its table:
Seat, City, Town, Fortress, Port, Cathedral, Mine, Outpost.
§2.1 registry uses 3 additional types not in §1.2:
**Village** (used heavily — 15 settlements), **Fortress-City** (S-014
Ehrenfeld), **Cathedral-City** (S-036 Himmelenger).
Conservative interpretation in Module 1: `ALL_REGISTRY_TYPES =
CANONICAL_TYPES + EXTRA_TYPES_IN_REGISTRY`. Module 1 does not collapse
these together.
**Editorial decision needed:** add Village/Fortress-City/Cathedral-City to
§1.2 type table, OR reclassify the §2.1 entries to existing §1.2 types.

### F2 — stat-column inconsistency in §1.2 vs §1.3
§1.2's per-type table has a "Stats" column listing varied stats:
Prosperity, Defense, Population, Trade, Naval, Garrison Capacity, Piety
Influence. §1.3 declares the canonical mechanical schema as three stats
on a 0–5 scale: Prosperity, Defense, Order.
**Conservative interpretation:** §1.3 governs mechanically. §1.2 stat
column is flavor.
**Editorial decision needed:** rename §1.2's "Stats" column to
"Contributions" (flavor) or harmonize the language.

### F3 — province count discrepancy between §1.1 and §2.1
§1.1 table: "Province | T1–T17 | 17". §2.1 enumerates 14 Kingdom provinces
+ Himmelenger + Schoenland = 16 entities (not 17).
**Module 2 territory:** PP-726 / political_hierarchy_v30 reconciles this.

### F4 — per-settlement starting stat values absent at §1.3 / §2.1 layer
§1.3 declares schema (3 stats × 0–5). §2.1 declares registry. Neither
specifies per-settlement starting values.
**Module 1 stance:** `Settlement` is identity-only; `SettlementStats` are
separately constructible with no canonical default.
**Downstream:** Modules 3 (facility tiers — may seed stats), 4 (Church
axes), 5 (governance), 12 (faction integration) need this before campaign
sim (Module 13, Mode C). Plausible homes: `params/` or
`designs/territory/valoria_geography_v30.yaml`. May be a gap; surface
for editorial generation.

## Module 1 data model — what Module 2+ inherits

```python
Settlement(id, name, type, province, duchy, role)        # immutable identity
SettlementStats(prosperity, defense, order)              # mutable state
local_economy(prosperity) -> int                         # §1.3 derived
garrison_strength(defense, fort_level=0) -> int          # §1.3 derived
public_order(order) -> int                               # §1.3 derived
province_accord_from_settlements(province, stats_dict) -> int  # §1.3 REVISED
REGISTRY: Tuple[Settlement, ...]                         # 37 entries
KINGDOM_DUCHIES, SPECIAL_ENTITIES                        # duchy classification
CANONICAL_TYPES, EXTRA_TYPES_IN_REGISTRY                 # F1 split preserved
```

## Player-action loop substrate (Jordan, 2026-05-13 scope addendum)

Module 1 surfaces the state that improvement/maintenance/problem-resolution
handlers will mutate:
- `Settlement` — identity (read-only)
- `SettlementStats` — mutable Prosperity/Defense/Order
- `province_accord_from_settlements` — feedback into province layer

Loop closes downstream (Modules 3/4/6/7 = action surfaces; Modules 5/8/12
= faction-standing recompute; Module 11 = Domain Echo to faction scale).

## Ledger entries committed this session

17 entries: 6 derived-value coefficients + 2 stat-range bounds + 8
expected-count constants + 3 worked-example values.

## Next session — Module 2

Political hierarchy + adjacency graph. Force-full read:
- `designs/territory/valoria_political_hierarchy_v30.md`
- `designs/territory/settlement_adjacency_v30.md`
- `designs/territory/valoria_geography_v30.yaml`
- `designs/territory/march_layer_v30.md`

Will resolve F3 (the 17 vs 14+2 count) directly.
