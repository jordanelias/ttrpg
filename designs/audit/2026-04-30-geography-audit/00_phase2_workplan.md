<!-- [SUPERSEDED: 2026-05-01 — PP-708 superseded by PP-707 per PP-709 §3 reconciliation] -->
<!-- BANNER (ED-779 Phase 2 commit 2026-05-01): -->
<!-- This is workplan B (PP-708). The canonical Phase 2 workplan is PP-707 at: -->
<!--   designs/audit/2026-04-30-geography-audit/01_phase2_workplan.md -->
<!-- Reconciliation: designs/audit/2026-04-30-geography-audit/04_workplan_reconciliation.md -->
<!-- Of the three substantive disagreements, PP-707 won on (1) canvas 1920×2880, -->
<!-- (3) explicit Lake/T4 coordinates. PP-708's contribution preserved: terrain naming -->
<!-- 'fjord_coast' (over PP-707's 'fjord') was adopted into the canonical taxonomy. -->
<!-- See PP-709 §1.1, §1.2, §1.3 for resolution detail. -->
<!-- This document is preserved as historical reference only. -->

<!-- [PROVISIONAL: 2026-05-01 — Phase 2 workplan, prep for ED-779 execution] -->
<!-- AUTHORITY: PP-707 -->

<!-- =====================================================================
[SUPERSEDED — see reconciliation memo 2026-05-01]

This file (00_phase2_workplan.md, PP-708) is one of two parallel-authored
Phase 2 workplans committed within minutes of each other on 2026-05-01.
Per reconciliation memo (designs/audit/2026-04-30-geography-audit/04_workplan_reconciliation.md):

- CANONICAL workplan = 01_phase2_workplan.md (PP-707)
- This workplan (PP-708) = SUPERSEDED reference

Specific dispositions:
- §1.1 canvas decision (2400×2880) → SUPERSEDED in favor of 01_phase2_workplan §1.1 (1920×2880, hex-grid alignment with UI v4 §7.4)
- §1.3 terrain naming `fjord_coast` → ADOPTED into canonical taxonomy
- §1.4 river deferral → SUPERSEDED in favor of 01_phase2_workplan §1.4 (river as annotation, not terrain)
- Other sections → DUPLICATIVE with 01_phase2_workplan; canonical content lives there

Phase 2 execution session uses 01_phase2_workplan.md + 04_workplan_reconciliation.md
as authoritative decision basis. This file is preserved for historical reference
and to record the parallel-session collision pattern (memo §9).

Authority: PP-709 (reconciliation memo)
===================================================================== -->


# Geography Canon Phase 2 — Workplan

**Date:** 2026-05-01
**Phase:** 2 of 4 (geography canon work; per audit at `designs/audit/2026-04-30-geography-audit/00_audit_report.md`)
**Status:** PROVISIONAL — workplan locked; execution opens next session
**Trigger:** Audit identified 9 gaps and 5 bugs blocking v2 mechanical spec authoring. Phase 2 produces the canonical geography data file that Phase 3 spec rewrite will query.
**Predecessors:** PP-706 (audit + Phase 1), commit `e0d6a07`
**Successors:** ED-780 (Phase 3 spec rewrite, blocked on this), ED-781 (Phase 4 stress tests)

---

## §0 What this workplan does and doesn't do

**Does:** Lock all decisions that gate authoring. Define schema. Demonstrate format with sample data. Project existing 17-territory coordinates to canonical system mechanically. Establish naming conventions and YAML structure.

**Doesn't:** Author the full 36 settlement coordinates, terrain polygons, terrain-cost matrix values, vision-range tables, or weather/season modifier tables. Those are next-session execution work — they require fresh attention and shouldn't be done in a partial-context session.

This workplan is leverage: it reduces next session's scope from "design + author + decide" to "author + verify + extend."

---

## §1 Locked decisions

These decisions are made and not subject to relitigation in the execution session unless a hard blocker emerges. If a blocker emerges, surface it explicitly — don't quietly revise.

### §1.1 Canonical coordinate system

**Decision:** New unified canonical coordinate system, **2400×2880**, north-up.

**Rationale:**
- 5:6 aspect ratio matches the existing jsx canvas peninsula proportions (settlement bounding box is 553w × 528h on 700×600 canvas — close to square; canonical 5:6 leaves headroom east for Schoenland and ocean-west margin)
- 2400 width fits standard 1080p+ Godot screen with UI side-panels at typical strategic-map zoom
- 2880 height accommodates north-south peninsula elongation including Altonian passes (top) and Calamity rings (bottom) without crowding
- Pixel-grade resolution allows sub-settlement precision for vision-range and proximity calculations without floating-point drift

**Migration:** Existing jsx coordinates linearly project. See §3 transform script.

**Resolves:** Audit finding C1 (coordinate system disconnect).

### §1.2 Lake Eidursjø position

**Decision:** Center (1135, 2263), rx=200, ry=150, shape=ellipse.

**Rationale:**
- Midpoint between T6 Stillhelm canonical (1406, 2280) and T13 Oastad canonical (864, 2246), serving its canonical function as east-west barrier in the central-south interior per `geography_v30_infill` ("creating a natural barrier between the western and eastern southern corridors")
- Wide enough to block direct T6-T13 line (lake is ~37% of inter-settlement distance)
- T4 Grauwald canonical (789, 1512) is in NW highland region per canon ("Highland Timber" Varfell territory) — far from lake; C3 conflict resolved

**Resolves:** Audit finding C3 (T4 inside lake artifact).

### §1.3 Terrain type taxonomy

**Decision:** 8 terrain types.

| Type | Description | Movement cost (placeholder; values authored in execution) |
|---|---|---|
| `plains` | Open farmland, lowlands. Default for Eastern Lowlands and central peninsula. | 1.0 (baseline) |
| `forest` | Wooded terrain. Slows movement; reduces vision. | TBD |
| `highland` | Hills, rolling elevation, sparse forest. NW Hafenmark character. | TBD |
| `mountain` | Mountainous terrain — high elevation, rocky. Northern range, NW/NE clusters, southern ridge. | TBD |
| `mountain_pass` | Specific narrow corridors through mountain terrain. Lowenskyst NE, Spartfell NW, Altonian routes. | TBD |
| `fjord_coast` | Western Norwegian-coded coastal terrain — fjord inlets, deep water, narrow shelves. Varfell west coast. | TBD |
| `coast` | Eastern smooth coastline — beaches, ports, shallow shelves. Eastern Lowlands, Schoenland. | TBD |
| `marsh` | Calamity-adjacent disturbed terrain. Around Askeheim, Stillhelm, Oastad. | TBD |

**Rationale:**
- 8 types covers the regional character distinctions in `geography_v30` (Norwegian-coded Varfell vs Italian-coded Crown vs Swiss-coded Hafenmark) without over-engineering
- `mountain` vs `mountain_pass` distinction is mechanically important — passes are traversable, mountain interior isn't
- `fjord_coast` vs `coast` distinction supports differentiated naval mechanics (fjord ports limited, eastern ports developed) and Maritime Forgetting boundary
- `marsh` captures the Calamity-disturbance gradient near Askeheim without conflating with mountain/forest

**Open for execution session:** Whether to add `glacier` (T17 Halvarshelm Northern Mines area, mountain peaks), `river` (currently as feature-line, not terrain polygon — see §1.4). Defer until polygon authoring forces the decision.

### §1.4 Rivers and feature lines

**Decision:** Rivers and roads are **feature lines** (polylines with attributes), not terrain polygons. Stored separately from the terrain layer.

**Rationale:**
- A river is a 1D curve, not a 2D area — modeling as polygon distorts geometry and pathing
- Crossings (bridges, fords) are points on the river line with attributes
- Roads are similar — polylines with surface-quality attribute, not polygons
- Settlement adjacency is implied by feature-line endpoints + proximity, not by polygon containment

**Schema:** See §2.4. Each river/road has start/end coordinates, intermediate vertices, type, and crossing-point list.

### §1.5 Province polygons

**Decision:** Implicit-from-Voronoi rule. No hand-authored province polygons.

**Rationale:**
- Hand-authoring 17 province polygons is fragile (boundaries shift if settlement coords shift; redrawing in canonical coordinate system is wasted effort if Voronoi works)
- Voronoi tessellation with one seed per territory anchor (territory's representative settlement) produces well-defined boundaries automatically
- Province boundaries don't carry mechanical weight at the strategic layer (boundaries are political, not movement-blocking — that's terrain's job)
- For UI render, Voronoi cells can be smoothed or hand-edited at draw time without affecting mechanical data

**Implementation note for Phase 3 spec:** When a coordinate query needs to know "which province is this point in?", the answer is "the territory whose anchor is closest" — Voronoi by definition. Phase 3 spec writes the lookup as a closest-anchor function, not a polygon-containment test.

**Territory anchor for Voronoi:** Territory anchor coordinate is the centroid of all settlements in that territory. For territories with one settlement (T7 Rendstad has only S-018), anchor = settlement coordinate. For territories with multiple settlements (T1 Valorsplatz has S-001, S-002, S-003), anchor = centroid of (S-001, S-002, S-003) coordinates.

**Resolves:** Audit gap G2 (province polygons).

### §1.6 Vision range model

**Decision:** Geometric circle around army position; radius modulated multiplicatively by terrain × weather × season.

**Schema:**
```yaml
vision_range:
  base_radius: <pixel value>           # to be authored in execution
  modifiers:
    terrain:                            # multiplier applied based on terrain at vision origin
      plains: 1.0
      forest: <multiplier; expect <1>
      highland: <expect >1, hills give vantage>
      mountain: <expect >1.2, vantage>
      mountain_pass: <expect <1, narrow>
      fjord_coast: <terrain-of-army; expect 1.0>
      coast: 1.0
      marsh: <expect <1>
    weather:                            # multiplier per weather state
      clear: 1.0
      overcast: <expect ~0.85>
      fog: <expect ~0.5>
      storm: <expect ~0.4>
      blizzard: <expect ~0.3>
    season:                             # multiplier per season
      spring: 1.0
      summer: <expect ~1.1>             # clearer atmosphere, longer days
      autumn: <expect ~0.9>             # diminishing daylight
      winter: <expect ~0.7>             # short days + frequent weather
```

**Calculation:** `effective_radius = base_radius × terrain_at_origin × weather × season`

**Rationale:**
- Multiplicative composition is intuitive (each axis modulates independently); clamps are simpler than additive offsets
- Terrain at *vision origin* (the army's location) is what matters — observer's position determines vantage
- Detection ≠ engagement (detection enables informed strategic-commit decisions next season; doesn't auto-trigger encounter — see Phase 3 spec for encounter-trigger rules)

**Open for execution session:** All concrete multiplier values. The brackets above are expected ranges, not authored values.

**Resolves:** Audit gap G5 (vision-range mechanic).

### §1.7 Naming conventions

- Coordinate system origin: top-left (0, 0); x increases east, y increases south. **Standard SVG/screen convention. Not standard math (y-up) convention.** Document this clearly in the geography YAML header.
- Settlements: `S-001` through `S-036` per existing settlement_layer §2.1 registry. Do not renumber.
- Territories: `T1` through `T17` per existing geography_v30 registry. Do not renumber.
- Terrain polygon IDs: `terrain-NNN` numbered sequentially as authored (no semantic ID).
- Feature lines: `river-<name>` for rivers (e.g., `river-valoris`), `road-NNN` for roads.

### §1.8 Decisions explicitly deferred to execution session

| Item | Reason for deferral |
|---|---|
| 36 settlement (x, y) within territory anchor regions | Detail-intensive; needs fresh attention; uses §1.7 schema |
| Terrain polygon vertices | Hand-authoring task; ~30-60 polygons; needs visual map work |
| Terrain-cost matrix values | Stress-test sensitive; better to iterate during Phase 3 simulation |
| Vision-range concrete values | Same as terrain-cost — calibrate against stress tests |
| Weather/season state machine | Currently season-state exists for Accounting; needs lookup-table only, not new state machine — but author tables in execution |

These all use the schema in §2 and the transform-script output in §3 as inputs.

---

## §2 Canonical data file schema

**File:** `designs/territory/valoria_geography_v30.yaml` (new — to be created in execution session)

```yaml
# VALORIA GEOGRAPHY — CANONICAL DATA
# Status: <PROVISIONAL until Jordan-approval>
# Coordinate system: 2400×2880, top-left origin, x→east, y→south
# Authority: PP-707 schema; ED-779 data authoring

meta:
  canonical_canvas: [2400, 2880]
  origin: top_left
  axis: { x: east, y: south }
  unit: pixel

territories:
  T1:
    name: Valorsplatz
    anchor: [<centroid of T1 settlements>, <centroid>]
    starting_control: Crown
    settlements: [S-001, S-002, S-003]
  # ... T2 through T17

settlements:
  S-001:
    name: Valorsplatz Palace
    territory: T1
    type: Seat
    controller: Crown
    coords: [<x>, <y>]
    stats: [4, 3, 4]   # Pros / Mil / Order per settlement_layer §2.1
    description: "Royal court. Lion's Table HQ. Torben resides here."
  # ... S-002 through S-036

terrain:
  - id: terrain-001
    type: mountain
    polygon: [[x1, y1], [x2, y2], ...]   # closed polygon vertices, north-up
    description: "Northern mountain spine — east-west range above passes"
  - id: terrain-002
    type: mountain_pass
    polygon: [...]
    description: "Lowenskyst NE pass — primary Altonian crossing"
  # ... ~30-60 polygons

water:
  lakes:
    - id: lake-eidursjo
      shape: ellipse
      center: [1135, 2263]
      rx: 200
      ry: 150
      description: "Lake Eidursjø — east-west barrier in central-south interior"
  rivers:
    - id: river-valoris
      vertices: [[x1, y1], [x2, y2], ...]   # ordered polyline source-to-mouth
      type: navigable
      crossings: [[x, y, "ford"], [x, y, "bridge"]]
      description: "Major river through Valorsplatz to eastern sea"
  coast: <implied by terrain polygons of type 'coast'/'fjord_coast' bordering ocean — no explicit data>

roads:
  - id: road-001
    vertices: [[x1, y1], [x2, y2], ...]
    surface: paved   # paved | unpaved | trail
    connects: [S-XXX, S-YYY]   # endpoint settlements
    description: "Crown highway from Valorsplatz to Lowenskyst"

terrain_costs:
  plains: 1.0
  forest: <TBD>
  highland: <TBD>
  mountain: <impassable_or_huge_cost>
  mountain_pass: <TBD>
  fjord_coast: <TBD>
  coast: 1.0
  marsh: <TBD>

vision_range:
  base_radius: <TBD>
  modifiers:
    terrain: { plains: 1.0, forest: <TBD>, highland: <TBD>, mountain: <TBD>, mountain_pass: <TBD>, fjord_coast: 1.0, coast: 1.0, marsh: <TBD> }
    weather: { clear: 1.0, overcast: <TBD>, fog: <TBD>, storm: <TBD>, blizzard: <TBD> }
    season:  { spring: 1.0, summer: <TBD>, autumn: <TBD>, winter: <TBD> }

altonian_passes:
  primary:   { name: Lowenskyst, settlement: S-006, terrain_id: terrain-002 }
  secondary: { name: Spartfell,  settlement: S-019, terrain_id: <id> }

calamity:
  epicenter: [<canonical Askeheim center>, <ditto>]
  rings:
    - { proximity: 0, radius: <px> }
    - { proximity: 1, radius: <px> }
    # ... per geography_v30 calamity proximity table

forgetting_zone:
  description: "Maritime Forgetting boundary — coastal waters around southern peninsula. East and west are separate maritime theatres."
  zone_polygon: [[x1, y1], ...]   # waters where naval routes blocked
```

### §2.1 Schema notes

- All coordinates are `[x, y]` arrays of integers in canonical canvas units
- Polygons are closed implicitly (last vertex connects back to first; do not duplicate first vertex at end)
- Polylines are open (rivers, roads — start to end, no closure)
- Stats triples are `[Prosperity, Military, Order]` per settlement_layer §2.1 column order
- TBD values: must be authored in execution session; not committed with literal "TBD" strings — use sentinel comments instead and fail fast if a query encounters one
- Naming: kebab-case for IDs (`lake-eidursjo`, `river-valoris`), PascalCase for proper nouns (`Valorsplatz`), snake_case for keys (`canonical_canvas`)

### §2.2 Validation checklist (for execution session)

Before committing the data file:

- [ ] All 17 territories present in `territories` map
- [ ] All 36 settlements present in `settlements` map; each has territory, type, controller matching settlement_layer §2.1
- [ ] All settlement coordinates inside canonical canvas bounds (0 ≤ x ≤ 2400, 0 ≤ y ≤ 2880)
- [ ] No two settlements share identical coordinates
- [ ] Each territory's anchor is the centroid of its settlements (or single-settlement coordinate)
- [ ] No settlement is inside a `mountain` polygon (settlements are habitable)
- [ ] No settlement is inside Lake Eidursjø
- [ ] All terrain polygons are simple (non-self-intersecting); polygon vertices in counter-clockwise order
- [ ] Terrain polygons collectively cover all peninsula land (no gaps in habitable territory)
- [ ] All `mountain_pass` polygons are inside `mountain` polygons (passes traverse mountains)
- [ ] All `terrain_costs` keys present; no literal "TBD" remains
- [ ] All `vision_range.modifiers` keys present; no literal "TBD" remains
- [ ] River polylines have at least 2 vertices; rivers connecting to ocean have endpoint at coast
- [ ] Roads connect existing settlements (`connects` references valid S-IDs)
- [ ] Altonian passes reference valid settlement and terrain IDs
- [ ] Calamity epicenter inside Askeheim territory polygon (Voronoi cell of T15)
- [ ] Forgetting zone polygon includes coastal waters around southern peninsula

---

## §3 Coordinate transformation script

A Python script projecting jsx (700×600) coordinates to canonical (2400×2880). Already built and tested — see §4 for output. The script is in this directory for execution session use.

**File:** `designs/audit/2026-04-30-geography-audit/01_coord_transform.py` (committed alongside this workplan)

**Usage:**
```bash
python3 01_coord_transform.py
# Outputs: 17 territory anchors at canonical coords + Lake Eidursjø position
```

**What it does:** Reads `designs/world/adjacency_map.jsx`, extracts T# coordinates, applies linear projection (×TARGET_W/SRC_W and ×TARGET_H/SRC_H), prints projected coordinates + Lake Eidursjø position from §1.2.

**What it doesn't do:** Author 36 settlement coordinates (only 17 territory anchors exist as input). Settlement placement within each territory is manual authoring task. Recommended approach in execution session: each multi-settlement territory places settlements at offsets around its territory anchor (e.g., T1 has 3 settlements; place S-001 Palace at anchor center, S-002 Riverside slightly south-east toward river/coast, S-003 Cathedral slightly west). Use existing settlement_layer §2.1 narrative descriptions to guide placement.

---

## §4 Sample data — proof-of-concept

The following sample data demonstrates the full schema for one territory (T1 Valorsplatz, 3 settlements) and one terrain polygon. Execution session uses this as pattern.

```yaml
territories:
  T1:
    name: Valorsplatz
    anchor: [1920, 1176]   # = (560,245) jsx projected to canonical
    starting_control: Crown
    settlements: [S-001, S-002, S-003]

settlements:
  S-001:
    name: Valorsplatz Palace
    territory: T1
    type: Seat
    controller: Crown
    coords: [1920, 1176]   # at territory anchor; royal court
    stats: [4, 3, 4]
    description: "Royal court. Lion's Table HQ. Torben resides here."
  S-002:
    name: Valorsplatz Riverside
    territory: T1
    type: Port
    controller: Crown   # Guild-managed per settlement_layer §2.1
    coords: [1990, 1230]   # ~70px southeast of Palace; toward river-Valoris mouth
    stats: [4, 1, 3]
    description: "River trade hub. Guild quarter. Largest market in Valoria."
  S-003:
    name: Valorsplatz Cathedral
    territory: T1
    type: Cathedral
    controller: Church
    coords: [1850, 1150]   # ~85px northwest of Palace; older quarter
    stats: [2, 1, 4]
    description: "Old Solmundic church. Politically significant — Church presence in capital."

terrain:
  - id: terrain-001
    type: mountain
    polygon: [[0, 0], [2400, 0], [2400, 400], [1800, 350], [1200, 280], [600, 320], [0, 380]]
    description: "Northern mountain spine — east-west range; Altonia border"
  # ... more polygons in execution session
```

This sample demonstrates: canonical coord usage, multi-settlement territory layout (S-001 at anchor, S-002/S-003 at offsets), stat preservation from settlement_layer §2.1, terrain polygon notation. Execution session extends pattern across 17 territories + 36 settlements + ~30-60 terrain polygons.

---

## §5 Phase 2 execution plan (for next session)

Estimated commits: 3.

### Commit 1 — Data structure
- Create `designs/territory/valoria_geography_v30.yaml`
- Populate `meta`, `territories` (17), `water.lakes` (lake-eidursjo from §1.2)
- Populate `settlements` (36) — use transform script output for territory anchors; manual offset for multi-settlement territories
- Validation: §2.2 first 5 items
- Status: PROVISIONAL

### Commit 2 — Terrain layer
- Author `terrain` polygons (~30-60 entries covering peninsula land)
- Author `water.rivers` (Valoris mouth-to-Valorsplatz, plus 1-2 Varfell rivers per geography_v30)
- Author `roads` (~10-15 connecting major settlements per geography_v30 adjacency)
- Validation: §2.2 next 5 items (terrain coverage, polygon hygiene, pass-inside-mountain, no settlement in mountain/lake)
- Status: PROVISIONAL

### Commit 3 — Modifier tables + edge data
- Author `terrain_costs` values (8 types; values to be calibrated against acclaimed-precedent like Total War movement penalties)
- Author `vision_range.base_radius` and all modifier values (~15 values total)
- Author `altonian_passes`, `calamity`, `forgetting_zone`
- Validation: §2.2 final items
- Status: PROVISIONAL → CANONICAL after Jordan review

### Phase 2 close
- Refresh propagation_map with Phase 2 entries
- Mark ED-779 as RESOLVED (Phase 2 complete)
- Phase 3 (ED-780) becomes unblocked

---

## §6 Open items

| ID | Item | Phase |
|---|---|---|
| **OPEN** | Concrete vision_range base radius (depends on canonical canvas size) | Commit 3 |
| **OPEN** | Concrete terrain_cost values | Commit 3 (initial) → Phase 4 calibration |
| **OPEN** | Whether to add `glacier` or `river` as terrain types | Commit 2 |
| **OPEN** | Naval coordinate system (Schoenland sea routes; Forgetting zone) — same canvas, ocean polygon | Commit 2 |
| **OPEN** | Weather state machine — does season pre-determine weather distribution, or are weather states sampled per turn? | Commit 3 (lookup table) → Phase 3 spec (mechanism) |
| **DEFERRED** | Adjacency_map.jsx update or deprecation — its abstract canvas is technically supersededed once Phase 2 lands. Decision deferred to Phase 3 (when settlement_adjacency v2 spec is rewritten and jsx becomes either unused or repurposed) | Phase 3 |

---

## §7 Cross-references

- Audit doc: `designs/audit/2026-04-30-geography-audit/00_audit_report.md` (PP-706, commit `e0d6a07`)
- Standing items: ED-779 (this Phase), ED-780 (Phase 3 spec rewrite, blocked on this), ED-781 (Phase 4 stress tests), ED-055 (naval mechanics, open since 2026-04-05 — resolved by Phase 3)
- Source data: `designs/world/geography_v30.md`, `designs/world/geography_v30_infill.md`, `designs/world/adjacency_map.jsx`, `designs/territory/settlement_layer_v30.md §2.1`, `params/bg/geography.md`
- Deprecated reference: `designs/provincial/valoria_map_v2.svg` (visual peninsula geometry preserved, territory labels superseded — see audit §3.C4)
