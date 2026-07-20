# Pointer register — G_pointer registry-resolution layer (WS1 progress meter)

Deterministic, working-tree only. **Measures; does not gate** — the gate is `tools/ci_quantity_vocabulary_check.py` (A17), report-only today per its own docstring; this is the graph/meter VIEW over that same check's facts, reusing its scanners (`scan_module_contracts`, `scan_sim_literals`) and `tools/quantity_registry.py`'s `resolve()` verbatim — no resolution logic is reimplemented here.

**Scorecard (progress meter):** 29/55 unique identifiers resolved (52.7%) · 42/71 raw occurrences resolved (59.2%) · known registry vocabulary = 196 resolvable name strings (aliases included) → 99 distinct registry keys.

**Refined meter (formula-local intermediates excluded, ED-IN-0061):** 29/54 unique (53.7%) · 42/70 occurrences (60.0%) — after removing 1 per-derivation formula-local(s), each a variable the formula itself defines (not an external quantity reference) and each listed below. This is a scope refinement, NOT a silent cap: the raw meter above is unchanged and every exclusion is enumerated.

## By surface

| surface | total | resolved | unresolved | % resolved |
|---|---:|---:|---:|---:|
| `module_contracts.state` | 48 | 25 | 23 | 52.1% |
| `module_contracts.derivations.output` | 9 | 6 | 3 | 66.7% |
| `module_contracts.derivations.inputs` | 14 | 11 | 3 | 78.6% |
| `sim_literals` | 0 | 0 | 0 | — |

## Resolved buckets — load-bearing registry keys (most-referenced pointers)

- `set.legitimacy` — 3 occurrence(s), 2 unique identifier(s): `Legitimacy`, `Legitimacy (L)`
- `set.order` — 3 occurrence(s), 1 unique identifier(s): `Order`
- `set.popular_support` — 3 occurrence(s), 2 unique identifier(s): `Popular Support`, `Popular Support (PS)`
- `set.prosperity` — 3 occurrence(s), 1 unique identifier(s): `Prosperity`
- `set.defense` — 2 occurrence(s), 1 unique identifier(s): `Defense`
- `attr.body.endurance` — 1 occurrence(s), 1 unique identifier(s): `Endurance`
- `attr.body.strength` — 1 occurrence(s), 1 unique identifier(s): `Strength`
- `attr.mind.will` — 1 occurrence(s), 1 unique identifier(s): `Spirit`
- `attr.social.bonds` — 1 occurrence(s), 1 unique identifier(s): `Bonds`
- `terr.fort_level` — 1 occurrence(s), 1 unique identifier(s): `Fort Level`

## Formula-local intermediates excluded from the refined meter (logged, not silently dropped)

1 identifier(s), each a variable its derivation's `formula` defines (the LHS of an `=`), so it is not an external quantity reference:
- `settlement_layer` · `W_s` — defined in formula: `q_s = 0.5L+0.5PS; W_s = base(Type)+Prosperity+FacilityTier; T = Σ W_s·(q_s/7); Mandate = c…`

## Unresolved identifiers — candidate pointer-debt (surface / location / identifier)

**Triage before acting — not every row is fixable debt.** Formula-local intermediates (a derivation input its own formula defines) are already excluded above. What remains still mixes kinds the resolver cannot tell apart: (a) genuinely-missing registrations — a stat name that *should* resolve but is hardcoded (real pointer-debt: register or rename to canonical); (b) computed/internal quantities with no registry-eligible identity, which A17's own docstring calls "a real, expected backlog item, not a bug" (e.g. `cumulative_damage`); and (c) candidate NON-SCALAR structured state (e.g. npc_behavior's `beliefs`/`opinions`/`arc state`), left in this list ON PURPOSE — whether it is a registry quantity at all is a DESIGN ruling (see references/registry/pointer_debt_worklist.md, Category B/C), not something to silently exclude. `derivations.inputs` rows skew toward (b); `state`/`derivations.output` toward (a).

28 unique unresolved (surface, location, identifier) row(s), 28 occurrence(s), 25 unique identifier(s) — counts computed from THIS (refined) list, so they always match it. (Raw, formula-locals included: 29 occ / 26 unique — the 1 excluded formula-local(s) are enumerated above.)

- [`module_contracts.derivations.inputs`] `personal_combat`: `cumulative_damage`
- [`module_contracts.derivations.inputs`] `settlement_layer`: `faction Mandate`
- [`module_contracts.derivations.output`] `settlement_layer`: `faction Mandate (cross-module → faction_state)`
- [`module_contracts.derivations.output`] `settlement_layer`: `faction Treasury income (cross-module → faction_state)`
- [`module_contracts.derivations.output`] `settlement_layer`: `province Accord`
- [`module_contracts.state`] `ci_political`: `card hands`
- [`module_contracts.state`] `ci_political`: `cooldown`
- [`module_contracts.state`] `ci_political`: `faction political pool`
- [`module_contracts.state`] `engine_clock`: `season counter`
- [`module_contracts.state`] `faction_state`: `faction stats 1-7`
- [`module_contracts.state`] `fieldwork_knots`: `knot strain`
- [`module_contracts.state`] `npc_behavior`: `arc state`
- [`module_contracts.state`] `npc_behavior`: `beliefs`
- [`module_contracts.state`] `npc_behavior`: `concerns`
- [`module_contracts.state`] `npc_behavior`: `opinions`
- [`module_contracts.state`] `npc_behavior`: `projects`
- [`module_contracts.state`] `peninsular_strain`: `Turmoil`
- [`module_contracts.state`] `personal_combat`: `Initiative`
- [`module_contracts.state`] `personal_combat`: `Poise`
- [`module_contracts.state`] `personal_combat`: `Wounds`
- [`module_contracts.state`] `personal_combat`: `cumulative_damage`
- [`module_contracts.state`] `piety_track`: `conviction scars`
- [`module_contracts.state`] `settlement_layer`: `province Accord`
- [`module_contracts.state`] `territorial_piety`: `CV (per-territory Piety)`
- [`module_contracts.state`] `victory`: `Accord`
- [`module_contracts.state`] `victory`: `PT reads`
- [`module_contracts.state`] `victory`: `PV`
- [`module_contracts.state`] `victory`: `Turmoil`
