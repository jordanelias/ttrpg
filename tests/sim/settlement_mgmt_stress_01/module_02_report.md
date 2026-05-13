# Module 02 Report — Political hierarchy + adjacency

**Date:** 2026-05-13
**Session:** Mode G Module 2 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_02_hierarchy.py`

**Canonical sources read at full depth:**
- `designs/territory/valoria_political_hierarchy_v30.md` (rebuild doc, ~5.1k tok)
- `designs/territory/settlement_adjacency_v30.md` (predecessor — partially superseded at granularity layer)
- `designs/territory/valoria_geography_v30.yaml` (settlement_adjacency block + settlements block)
- `designs/territory/march_layer_v30.md` (§1 march-budget signature only)
- `designs/territory/settlement_layer_v30.md` (re-fetched for sim_gate system 'settlement_layer')

## Summary

Wires the canonical political-administrative scaffolding atop Module 1: rebuild hierarchy (Valn to Kingdom to Duchy to Province to Settlement); three Kingdom duchies + three special-case entities (Himmelenger, Askeheim, Schoenland); 55-edge canonical adjacency graph from geography YAML; greater-than-or-equal-to-two-march-route validator; province-fracturing predicate (§2.3); political-value computation structure (§2.4 — scalars deferred).

## Isolation tests — 22/22 PASS

| # | Test | Result |
|---|------|--------|
| T1 | Total edge count == 55 (YAML actual content) | PASS |
| T2 | Intra-province edge count == 28 | PASS |
| T3 | Inter-province edge count == 27 | PASS |
| T4 | Every settlement in degree map | PASS |
| T5 | Every Kingdom settlement satisfies greater-than-or-equal-to-two-connection rule | PASS |
| T6 | Himmelenger has degree 5 | PASS |
| T7 | Schoenland has degree 1 (foreign-exempt) | PASS |
| T8 | Schoenland's single edge is sea-route to S-001 (Valorsplatz) | PASS |
| T9 | Every edge endpoint is a known settlement | PASS |
| T10 | No self-loops | PASS |
| T11 | No duplicate edges | PASS |
| T12 | Every Kingdom duchy has provinces | PASS |
| T13 | Kingdom province count == 14 | PASS |
| T14 | Every Kingdom province has 2-3 settlements | PASS |
| T15 | Fracturing predicate fires on mixed-faction province | PASS |
| T16 | Fracturing predicate quiet on unified province | PASS |
| T17 | Unification bonus awarded only on full-ownership | PASS |
| T18 | Monarch / monarch-duchy consistency (Almund / Valorsmark) | PASS |
| T19 | Kingdom settlement total via hierarchy == 35 | PASS |
| T20 | Askeheim has zero settlements | PASS |
| T21 | Graph one connected component across all 37 settlements | PASS |
| T22 | Every edge type in canonical taxonomy | PASS |

## Findings NEW this session

### F5 — settlement_adjacency edge count internal inconsistency

geography_v30 settlement_adjacency block header asserts: "56 edges total: 28 intra-province ... + 28 inter-province". The block actually contains 55 edges: 28 intra-province + 24 primary inter-province (including 1 sea-edge S-001 to S-037) + 3 second-routes. Header "24 primary + 1 sea" section breakdown double-counts the sea.

**Module 2 stance:** trust actual content (55) over header assertion (56).

**Editorial decision needed:** either add a 56th edge for consistency with the header, or fix the header to say "55 edges (28 intra + 24 primary inter [1 of which is sea] + 3 second-routes)".

### F6 — intra-YAML S-ID granularity drift in valoria_geography_v30.yaml

The `settlement_adjacency:` block was rebuilt at the new post-rebuild granularity (35 + 1 + 1 = 37 settlements, S-001 through S-037, siege-target level). The `settlements:` block in the same YAML file remains at the old pre-rebuild granularity (36 entries, S-001 through S-036, district level). Same S-ID strings denote different settlements between the two blocks:

- `settlements: S-001` = "Valorsplatz Palace" (a district — old granularity)
- `settlement_adjacency: S-001` = Valorsplatz (the whole siege-target — new granularity)

Rebuild §4 migration note acknowledges this lazy-update pattern: "Old S-IDs in non-substrate documents ... are migrated lazily as those documents are next touched."

The `settlements:` block IS a substrate document by usage (it carries canonical per-settlement starting stats), even if the rebuild didn't explicitly list it for immediate migration. The pre-rebuild `settlements:` block has 36 entries with `stats: [Prosperity, Defense, Order]` arrays — mechanically valid data at the wrong granularity for post-rebuild work.

**Resolves F4 partially.** The data exists; the granularity mismatch is what needs reconciling.

**Editorial decision needed:** migrate the `settlements:` block to the post-rebuild granularity (37 entries S-001 through S-037 matching `settlement_adjacency:` + `settlement_layer §2.1`). The migration is not mechanical-trivial — the old districts (Valorsplatz Palace / Riverside / Cathedral) are sub-features of the new Valorsplatz siege-target, so their stats may need to be aggregated rather than mapped 1:1.

**Module 13 Mode C campaign sim cannot use the current `settlements:` block directly.** Either (a) wait for canonical migration, (b) implement an aggregation rule (faction-integration module territory), or (c) author seed-stats directly in sim params at post-rebuild granularity. This is a stop-the-presses finding for Module 13.

## Findings from prior session revisited

### F1 — type list (Module 1)
Status unchanged; not addressable from political_hierarchy doc.

### F2 — §1.2 stats column (Module 1)
Status unchanged; not addressable from political_hierarchy doc.

### F3 — province count (Module 1) — RESOLVED

Rebuild §2.1: "14 provinces total in the duchy hierarchy = 35 settlements" plus three special-case entities (Himmelenger / Askeheim / Schoenland) = 17 entities total. The §1.1 "T1 through T17" label was the deprecated territory-level nomenclature; T1 through T17 mapped to 14 provinces + 3 special entities in the new schema. Module 2 confirms via T13_kingdom_province_count_14 + T20_askeheim_zero_settlements PASS.

### F4 — per-settlement starting stats (Module 1) — PARTIALLY RESOLVED

Data lives in `valoria_geography_v30.yaml :: settlements:` block. BUT the block is at pre-rebuild granularity (36 districts, not 37 siege-targets). See F6 for the granularity-mismatch resolution path.

## Module 2 data model — what downstream modules inherit

```
EDGE_TYPES = ('road', 'sea', 'river', 'mountain_pass', 'coastal', 'thread_witnessed')
EDGES: Tuple[Edge, ...]                       # 55 entries
neighbors(sid), degree(sid)
is_intra_province(edge), is_inter_province(edge)
validate_min_connections() -> Dict[str, int]
province_is_fractured(province, settlement_factions) -> bool
PoliticalValueComputation                      # structure; scalars TBD
provinces_in_duchy, kingdom_provinces, all_provinces
DUCHY_DUKE, MONARCH_NAME, MONARCH_DUCHY
SPECIAL_CASE_ENTITIES = ('Himmelenger', 'Askeheim', 'Schoenland')
MIN_SETTLEMENTS_PER_PROVINCE = 2
MAX_SETTLEMENTS_PER_PROVINCE = 3
MIN_CONNECTIONS_PER_SETTLEMENT = 2
EXPECTED_KINGDOM_PROVINCES = 14
```

Module 3 (facility tiers) uses the graph to model capacity pressure propagation and cross-faction wing allocation. Module 5 (governance) consumes `province_is_fractured` for the governor-assignment cascade. Module 7 (military) consumes EDGES + EDGE_TYPES for invasion movement + battle modifiers. Module 12 (faction integration) consumes `PoliticalValueComputation` once §2.4 scalars are canonical.

## Player-action loop contribution

Module 2 carries no player-action handlers itself. It supplies the **graph topology** that improvement/maintenance/problem-solve actions operate against:

- Invasion / siege movement uses EDGES (downstream military module maps action to movement).
- Settlement-isolation pressure (degenerate-loop Mode D case) checks against `degree(sid)` — a single-connection settlement under siege cannot be relieved, surfaces as an "unreadable feedback" loop case.
- Province-control consolidation (improvement loop closing on unification bonus) checks against `province_is_fractured` predicate.

## Ledger entries this session

11 new entries (28 total across M1 + M2):
- 3 rebuild rules (1-3 settlements per province, greater-than-or-equal-to-two connections)
- 2 expected-count constants (14 provinces, 35 settlements)
- 3 edge-count constants (55 total, 28 intra, 27 inter)
- 1 header-asserted-mismatch constant (56) for F5 surfacing
- 2 special-case-degree constants (Himmelenger 5, Schoenland 1)

## Next session — Module 3

Facility tiers + slot allocation + capacity pressure. Force-full read: `settlement_layer_v30` §1.4.1, §1.4.2, §1.4.3, §1.4.4. Surfaces:
- Per-type slot-capacity tables (improvement-action substrate)
- §1.4.3 capacity pressure threshold (problem-solve trigger)
- §1.4.4 cross-faction wing allocation (subnational faction visibility)

Module 3 begins to populate the *improvement* arm of the player-action loop (Modules 6 and 7 cover *problem-solve* and *maintenance* respectively).
