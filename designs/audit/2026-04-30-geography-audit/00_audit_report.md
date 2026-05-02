<!-- [PROVISIONAL: 2026-04-30 — geography canon audit, pre-Phase-2 spec rewrite] -->
<!-- AUTHORITY: PP-705 / ED-778 -->

# Geography Canon Audit — 2026-04-30

**Date:** 2026-04-30
**Scope:** Audit of geography canon for completeness, internal consistency, and readiness to support v2 mechanical spec (geographic-route model superseding edge-typed graph).
**Trigger:** Jordan flagged that current `settlement_adjacency_v30` uses abstract edge-typing (Road/River/Mountain Pass/Coastal labels on graph-edges) which doesn't reference existing (x,y) coordinate data or geographic terrain features. Audit precedes any spec rewrite.
**Outcome:** Canon is more substantial than prior session synthesis suggested, but contains four bug categories and seven gap categories that must be resolved before v2 mechanical spec can be authored.

---

## §1 What exists (POSITIVE)

The geography canon is largely authored across multiple coherent sources:

| Source | Status | Content |
|---|---|---|
| `designs/world/geography_v30.md` (skeleton, CANONICAL 2026-04-05) | Solid | Five terrain regions (Northern Mountains, NW Highlands, Western Fjords, Eastern Lowlands, Central Peninsula); Continental Context; Geographic Unity; Church Geography; Restoration Movement Geography; Maritime Forgetting Zone; Calamity Bleed Gradient; 17-territory adjacency table; faction control summary; POI catalog; Altonian Invasion Routes |
| `designs/world/geography_v30_infill.md` | Solid | Region prose: Hafenmark Swiss-coded, Varfell Norwegian-coded, Crown Italian-coded; Lake Eidursjø as east-west barrier; Maritime Forgetting east/west theatre split; Adjacency Notes |
| `designs/world/adjacency_map.jsx` | Solid | All 17 territory (x, y) coordinates on 700×600 abstract canvas; 26 directed edges; faction control by territory |
| `designs/territory/settlement_layer_v30.md §2.1` | Solid | Full 36-settlement registry (S-001 through S-036) with: territory mapping (T1–T17), settlement type (Seat/Port/Cathedral/Town/Fortress/Mine/Outpost/City), controller, stats, narrative description |
| `designs/provincial/valoria_map_v2.svg` | **STALE — pre-canon** | Visual peninsula map. **Territory numbering is from a superseded schema** (see §3.C4 below). Visually informative for shape and feature placement; mechanically and label-wise unusable. |
| `params/bg/geography.md` | Solid | Spiritual Weight per territory, faction starting stats, full territory table consistent with geography_v30 |

**Cross-reference verification:** geography_v30.md adjacency table and adjacency_map.jsx edges are in **perfect agreement** — 26/26 edges match symmetrically. Faction control assignments match across all canonical sources. Calamity proximity table is consistent. The narrative canon and registry data are coherent with each other.

The prior session synthesis ("settlement_adjacency_map.yaml not authored") understated what exists. The 36-settlement registry IS authored — it just lacks (x, y) coordinates per individual settlement (only territory-level anchors exist).

---

## §2 What's incomplete (GAPS)

| ID | Gap | Authoring scope estimate |
|---|---|---|
| G1 | Settlement-level (x, y) coordinates within territory anchor regions | 36 entries (~1 day's work) |
| G2 | Province polygons (territory boundary geometry) | 17 polygons, or implicit-from-Voronoi rule |
| G3 | Typed terrain layer (queryable polygons or raster: forest/plains/mountain/marsh/coast/river) | ~30–60 polygons depending on resolution |
| G4 | Terrain-cost matrix (terrain type × movement cost multiplier) | ~5–10 terrain types × cost values |
| G5 | Vision-range mechanic (base radius + terrain × weather × season modifiers) | Not authored anywhere in canon |
| G6 | Weather/season → spatial mechanic modifiers | Season-state exists for Accounting cadence but doesn't modulate any spatial mechanic |
| G7 | March-bubble / real-time march layer | Doesn't exist. Current §1.3 movement is "Military ÷ 2 edges per season" — abstract, no real-time playback |
| G8 | Battle-terrain derivation from geography | Currently derived from edge-type label (4 categories), not actual geography at engagement coordinates |
| G9 | Naval mechanics (resolves ED-055 standing item from 2026-04-05) | Schoenland↔T1 sea route is flagged but not mechanically modeled |

---

## §3 What's inconsistent (BUGS)

### C1. Coordinate system disconnect

Two coordinate systems exist and don't agree:

- `adjacency_map.jsx`: 700×600 canvas (abstract, schematic). Schoenland T16 at (648, 168), Askeheim T15 at (340, 588).
- `valoria_map_v2.svg`: 700×900 canvas (visual, geographic). Schoenland island rendered at (658, 504), Calamity rings rendered at (189, 792).

Schoenland is positioned in the *north* in the abstract map and the *middle-east* in the visual map. Askeheim/Calamity is south-central in abstract and far-south-west in visual. These are two different mental maps not yet unified.

**Impact:** Any v2 spec must pick one canonical coordinate system. Mixing creates ambiguity in spec authoring and downstream bugs in Godot impl.

### C2. SVG pass-label errors (within-SVG, pre-canon)

```svg
<!-- NW pass from Sigurdshelm -->   ← WRONG per any naming schema
<!-- NE pass from Spartfell -->     ← WRONG per any naming schema
```

Per geography_v30.md and params/bg/geography.md (current canon): NE pass enters at T3 Lowenskyst (primary), NW pass enters at T10 Spartfell (secondary). Sigurdshelm (T12) is the Varfell Seat, not a pass. The SVG comments are reversed/wrong on both directions.

This is a SVG-internal bug, not a canon-vs-SVG bug. Already-superseded by C4 — the SVG is being deprecated wholesale.

### C3. Lake Eidursjø geometry conflict

SVG places Lake Eidursjø at (cx=275, cy=298, rx=52, ry=82). T4 Grauwald jsx position (230, 315) is **inside the lake ellipse** (normalized distance 0.79 < 1). Edge T4↔T14 (T14 at 373, 285) crosses the lake — sample-line analysis: 14 of 21 line-samples are inside the lake. Edge T7↔T4 also crosses (12/21 inside).

This is a coordinate-system disconnect (C1) artifact: T4's jsx coordinates were placed without reference to the SVG's lake position. Resolution requires either (a) repositioning T4 to NE shore of lake (~290, 325 — clears lake), (b) reshaping lake to be smaller, or (c) accepting T4-T14 as a "long route around lake" abstraction that isn't a straight line.

Recommended resolution (folded into Phase 2 data authoring): unified canonical coordinate system established first, then T4 placed at NE-shore of canonical lake. Avoid surgical-fix attempt at C3 in Phase 1 because the underlying coordinate-system pick (C1) gates the right answer.

### C4. valoria_map_v2.svg is structurally pre-canon

The SVG is from a superseded territory-numbering schema that predates the current canon. Concrete evidence:

| SVG label | SVG T# | Current canon T# |
|---|---|---|
| Sigurdshelm | T2 | T12 |
| Halvardshelm | T3 | T11 |
| Vargstad (superseded name) | T4 | — (renamed to Grauwald, now T4 by coincidence) |
| Gransol | T5 | T8 |
| Eidursjo (superseded name) | T6 | — (renamed to Rendstad, now T7) |
| Spartfell | T7 | T10 |
| Lowenskyst | T8 | T3 |
| Arcansheld (superseded name) | T9 | — (renamed to Ehrenfeld, now T14) |
| Nordhelm (superseded name) | T10 | — (renamed to Kronmark, now T2) |
| Mittelmark (superseded name) | T11 | — (renamed to Feldmark, now T5) |
| Valorsplatz | T12 | T1 |
| Stillhelm | T13 | T6 |
| Himmelenger | T14 | T9 |
| Askeheim | T15 | T15 (matches) |
| Schoenland | T16 | T16 (matches) |

SVG legend reads "Varfell (T1–T4) / Hafenmark (T5–T8) / Crown (T9–T13)" — completely different faction-territory assignment from current canon (Crown holds T1, T2, T3, T5, T6, T14).

The SVG is not just stale-on-labels — it is a fundamentally different territory schema. Surgical edits cannot bring it into canon-alignment. **Recommended action:** deprecate the SVG (move to `deprecated/` or mark with banner). Phase 2 redraws from canon.

**No active mechanical spec depends on the SVG.** GitHub code-search for `valoria_map_v2` returns 5 references: `references/file_index.md`, `references/restructure_ledger.md`, `designs/audit/valoria_systems_workplan.md` — all index/ledger entries, none mechanical.

### C5. Schoenland sea route is flagged but not modeled

`geography_v30.md §Adjacency Notes` lists Schoenland's only connection as `T1 (sea)`. `settlement_adjacency_v30 §1.1` has only 4 edge types (Road, River, Mountain Pass, Coastal). The "sea connection" T16↔T1 fits "Coastal (requires naval)" semantically but isn't explicitly tagged that way. ED-055 (Maritime Forgetting Zone — naval movement spec) has been open since 2026-04-05. Folded into G9 above.

---

## §4 Naming hygiene (post-2026-04-30)

Already-applied via recent commits: Niflhel residue strike (PP-698), Vaynard canonicalization (PP-699), faction-doctrine framework (PP-700–702). Other terrain-rename history is recorded in `params/board_game_misc.md`:

> Old territory names (Vargstad, Eidursjo, Arcansheld, Nordhelm, Mittelmark) replaced with canonical names (Grauwald, Rendstad, Ehrenfeld, Kronmark, Feldmark).

These superseded names still surface as text in the SVG — addressed by SVG deprecation in Phase 1.

---

## §5 Recommended sequencing for v2

| Phase | Scope | Commits | Outputs |
|---|---|---|---|
| **Phase 1 — Bug fixes** (this commit) | Deprecate stale SVG; record audit findings; commit standing items | 1 | Audit doc; SVG deprecation banner; PP-705/ED-778 +ED-779–781 standing |
| **Phase 2 — Data authoring** | (a) Decide canonical coordinate system; (b) author 36 settlement (x, y); (c) author province polygons or Voronoi rule; (d) author typed terrain layer; (e) author terrain-cost matrix + vision-range tables + weather/season modifier tables | ~3 | `designs/territory/valoria_geography_v30.yaml` (or .json); redrawn map |
| **Phase 3 — Spec rewrite** | (a) Rewrite `settlement_adjacency_v30` to query geography rather than edge-types; (b) author march-bubble + encounter-trigger spec (new doc `designs/territory/march_layer_v30.md`); (c) update `mass_battle_v30 §A.9 / §B.5` for geographic battle-terrain derivation; (d) author naval mechanics (resolves ED-055) | ~2 | Updated specs |
| **Phase 4 — Validation** | Run three queued stress tests (Mountain Pass, Open-field cavalry, Coastal landing) against new spec | per-scenario | Stress test reports |

Phase 1 is small and discrete (this commit). Phase 2 is where most actual authoring effort lives. Phase 3 leans on the new data. Phase 4 validates against scenarios.

---

## §6 Decisions taken in Phase 1 (this commit)

1. **C1 coordinate system:** Decision deferred to Phase 2. Recommended approach: new unified canonical sized to Godot screen needs (~1920×2880 or similar), proportions matching peninsula geography. Migration of jsx → new canonical happens during Phase 2 data authoring.
2. **C3 Lake Eidursjø + T4 Grauwald repositioning:** Decision deferred to Phase 2 (coordinate-system pick gates the right answer).
3. **C4 SVG handling:** Deprecate via banner-comment + retain file as historical reference. Do NOT delete (preserves history). Phase 2 produces replacement map.
4. **Audit committed:** This document, as `designs/audit/2026-04-30-geography-audit/00_audit_report.md`.
5. **Standing items minted:**
   - **ED-778** (P2): Phase 2 data authoring — 36 settlement coordinates, terrain layer, cost matrix, vision-range tables.
   - **ED-779** (P2): Phase 3 spec rewrite — settlement_adjacency v2 + march_layer + mass_battle terrain derivation + naval mechanics.
   - **ED-780** (P3): Phase 4 stress tests — three scenarios queued (Mountain Pass / Open-field / Coastal Landing).

---

## §7 Cross-references

- Recent commits: ca921b7 (faction-doctrine batch ED-775/PP-698-704), a6da757 (Stratagem rename ED-771/PP-690), cd09b98 (mass battle MB-01..08 ED-770/PP-683-688)
- Standing items: ED-055 (naval mechanics, 2026-04-05), ED-710 (settlement adjacency graph, PP-666), ED-711 (fractional province ownership), ED-776 (Hafenmark equipment-quality mechanism via simulation)
- Affected files: `designs/world/geography_v30.md`, `designs/world/geography_v30_infill.md`, `designs/world/adjacency_map.jsx`, `designs/provincial/valoria_map_v2.svg`, `designs/territory/settlement_adjacency_v30.md`, `designs/territory/settlement_layer_v30.md`, `params/bg/geography.md`, `designs/provincial/mass_battle_v30.md` §A.9 / §B.5
