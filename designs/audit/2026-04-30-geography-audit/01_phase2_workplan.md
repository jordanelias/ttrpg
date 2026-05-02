<!-- [PROVISIONAL: 2026-05-01 — Phase 2 workplan, pre-authoring] -->
<!-- AUTHORITY: PP-707 / ED-779 -->

# Geography Canon Phase 2 — Workplan & Schema

**Date:** 2026-05-01
**Authority:** ED-779
**Status:** PROVISIONAL — workplan + decision lock-in for Phase 2 data authoring. Pre-authoring artifact. Hand-authoring of 36 settlement coordinates, province polygons, full terrain layer, terrain-cost matrix, and vision-range tables happens in a dedicated next session using this workplan as decision basis.

**Purpose:** Lock decisions needed before Phase 2 authoring begins so the authoring session is execution, not relitigation. Provides schema, sample populated entries, and a coordinate transform script.

---

## §1 Decisions locked

These decisions are now canonical for Phase 2 authoring. Subsequent sessions execute against this spec rather than redebating.

### §1.1 Canonical coordinate system

**Decision:** New unified canvas, **1920×2880** (2:3 aspect, peninsula proportions, Godot screen-friendly multiples).

- Origin: top-left (0, 0). +x = east. +y = south. (Matches SVG and Godot conventions.)
- Peninsula occupies the central column ~480 to ~1440 (x), ~80 to ~2800 (y) — leaves margin for sea, Schoenland island, Altonian land mass, and UI overlay.
- All coordinates in Phase 2 data file are in this system.
- adjacency_map.jsx (700×600) is **migrated**, not deleted — it becomes a presentation-layer schematic with its own non-canonical coordinates. The canonical source is `valoria_geography_v30.yaml`.
- Lake Eidursjø, Calamity rings, Schoenland island all repositioned in canonical system to be self-consistent (resolves C1 from audit).

**Rationale:** Godot's default viewport is 1920×1080 16:9, but a peninsula map wants tall aspect. 1920 width preserves horizontal Godot screen-fit; 2880 height fits a peninsula extending north-south. Multiples of 32 enable hex-grid overlays cleanly at 16×10 (UI v4 §7.4 tactical hex) when zoomed in.

### §1.2 Coordinate migration rule (jsx → canonical)

The 17 territory anchor coordinates in `adjacency_map.jsx` are abstract on a 700×600 canvas. They have correct *relative* topology but wrong absolute positions for Phase 2 needs. Migration formula:

```
new_x = old_x_jsx * (1920 / 700)   # scale × 2.7428…
new_y = old_y_jsx * (2880 / 600)   # scale × 4.8

# Then apply per-territory geographic correction offsets per §1.3.
```

The pure scaling alone won't be right — the jsx layout is schematic, not geographic. Per-territory corrections needed for:
- T4 Grauwald (out of lake — see §1.3)
- Schoenland (jsx places it north; canon places it east-coast)
- Askeheim (jsx is south-central; canon is south, possibly south-west)
- Lake Eidursjø position (geometry to resolve)

The transform script (§3) does the scaling. Hand-authoring in next session does the geographic correction offsets.

### §1.3 Lake Eidursjø + T4 Grauwald

**Decision:** Lake Eidursjø is canonically positioned in the **central-south interior** as a real geographic barrier between western (Varfell) and eastern (Crown) southern corridors per `geography_v30_infill.md`. T4 Grauwald is on the **NE shore of the lake** (highland, timber, Einhir-heritage), with edges T4↔T7 (Rendstad, north — clears lake), T4↔T12 (Sigurdshelm, west — *historically* a long route around lake), T4↔T14 (Ehrenfeld, east — clears lake).

Concretely, in canonical 1920×2880 system:
- **Lake Eidursjø:** center ~(960, 1700), rx ~180, ry ~280 (oriented north-south, narrow)
- **T4 Grauwald:** ~(1090, 1430) — NE shore, above lake's north tip
- **T12 Sigurdshelm:** ~(540, 1850) — west shore, requires routing around lake's south for T4↔T12
- **T11 Halvardshelm:** ~(440, 1280) — west of lake, north
- **T14 Ehrenfeld:** ~(1290, 1320) — east of lake, north

T4↔T12 edge is canonically a "long route around lake" — distance modifier in spec. Either via T11 north-of-lake corridor or via T13 south-of-lake corridor. (Spec resolution in Phase 3.)

**Visual aid (schematic, not authoritative — coordinates illustrative):**
```
                 (north)
                    |
       T17  T3      T9
        \  /        |
        T8          |
       /  \         |
      T7   T10      |
      |    |        |
      T11  T4 -- T14
       \   |\  /
        \  | \/
        T12-+--T1   T16
            |  |
       T13-T6 T5
            |
           T15
                 (south)
```

### §1.4 Terrain type taxonomy

**Eight terrain types**, ordered roughly by movement cost ascending:

| ID | Type | Description |
|---|---|---|
| `plains` | Plains | Open farmland, grassland. Fastest, best vision. |
| `coast` | Coastal lowland | Beach, seaside flatland. Plains-equivalent. |
| `forest` | Forest | Mixed woodland. Slower, reduced own-vision but cover. |
| `marsh` | Marsh / wetland | Lake-edge, river-delta swamp. Slow, malarial penalties optional. |
| `highland` | Highland / hills | Rolling elevated terrain. Slower than plains, extends vision from peaks. |
| `fjord` | Fjord | Deep coastal inlet, broken terrain, sea-cut. Varfell west coast. Land movement very slow; sea movement enabled. |
| `mountain` | Mountain | Steep, rocky. Slow, blocks vision, blocks armies without specific pass routes. |
| `pass` | Mountain pass | Designated traversable strip through mountain terrain. Slow but possible. |

**Special features (annotations, not terrain types):**
- `river` — line feature, crosses other terrain. Crossing penalty unless `bridge` annotated.
- `bridge` — point feature, removes river crossing penalty.
- `road` — line feature, follows or cuts through terrain. Reduces movement cost by ~25-50% on the path it follows.
- `forgetting_zone` — annotated region around Askeheim. Polygon-bounded. TS ≥ 30 gating per `mass_battle §A.11`.
- `radiation_band` — Calamity radiation rings per `calamity_radiation_v30`. Polygon-bounded.

**Rationale for taxonomy:** Avoids confusion between "highland" (Hafenmark NW Highlands — Swiss-coded) and "mountain" (the impassable Northern Mountains barrier). Avoids confusion between "coast" (Eastern Lowlands shoreline — gentle) and "fjord" (Varfell west coast — broken). Eight types is enough granularity for meaningful mechanical differentiation without authoring becoming impossible.

### §1.5 Terrain cost matrix (initial values, simulation-tunable)

Movement cost = base distance × terrain multiplier. Initial values for Phase 2 author seed:

| Terrain | Multiplier | Rationale |
|---|---|---|
| `plains` | 1.0 | baseline |
| `coast` | 1.0 | equivalent to plains for army movement |
| `road` (overlay) | 0.7 | when path follows a road, multiplier reduces by ~30% |
| `forest` | 1.5 | slowed by undergrowth, broken sightlines |
| `highland` | 1.5 | uphill, terrain-broken |
| `marsh` | 2.0 | slow, dangerous, supply-degrading |
| `fjord` | 2.5 | broken inlet terrain (land); naval movement enabled, separate rules |
| `pass` | 2.0 | slow but viable |
| `mountain` | ∞ | impassable without `pass` overlay |

Bridge: river crossing penalty 0 with bridge, +50% terrain cost without (must ford).

**These are seed values.** Phase 4 stress tests calibrate them. Lock in only the structure; the numbers are tunable.

### §1.6 Vision-range tables (initial values, simulation-tunable)

Base army vision range: **8 units** (where 1 unit = 16 canonical pixels = ~1 league in lore). At 1920×2880, peninsula is ~180 vertical units, so 8-unit base means an army sees ~4-5% of peninsula's length.

Modifiers:

| Modifier | Δ | Notes |
|---|---|---|
| Hill/highland (army on) | +50% | extends sight |
| Mountain (army on) | n/a (army can't be there without pass) |
| Forest (army in) | -30% | own vision reduced |
| Marsh (army in) | -30% | mist, broken sightlines |
| Fog of war (weather) | -50% | spring fog, autumn mist |
| Storm (weather) | -70% | severe winter or coastal storm |
| Clear summer | +20% | best season |
| Winter | -30% | shorter days, snow obscure |
| Night | -60% | implementation depending on day-cycle granularity |

These are seed values. Phase 4 stress tests calibrate.

### §1.7 Schema for `valoria_geography_v30.yaml`

Single canonical data file. Top-level structure:

```yaml
# Valoria Geographic Canon — Phase 2 data
# AUTHORITY: ED-779 / PP-706 / Phase 2 workplan PP-707
# Coordinate system: 1920×2880, origin top-left, +x east, +y south.

canvas:
  width: 1920
  height: 2880
  origin: top-left
  units_to_pixels: 16   # 1 unit = 16 px = ~1 league

provinces:
  T1:
    name: Valorsplatz
    faction: Crown
    polygon: [[1340, 720], [1500, 760], [1490, 1080], [1320, 1060]]
    region: Eastern Lowlands
    spiritual_weight: 2
    proximity_calamity: 3
    starting_pros: 6
  # ... all 17 provinces

settlements:
  S-001:
    name: Valorsplatz Palace
    province: T1
    type: Seat
    controller: Crown
    coords: [1380, 880]
    stats: {prosperity: 4, fortification: 3, prominence: 4}
    notes: "Royal court. Lion's Table HQ. Torben resides here."
  # ... all 36 settlements

terrain:
  - id: northern_range
    type: mountain
    polygon: [[300, 80], [1600, 80], [1620, 280], [310, 290]]
    notes: "Northern Mountains — east-west barrier vs Altonia"
  - id: lake_eidursjo
    type: marsh   # treated as obstacle for movement
    polygon: [[920, 1480], [1000, 1480], [1010, 1900], [930, 1900]]
    notes: "Lake Eidursjø — central-south interior, east-west barrier"
  # ... all terrain polygons

features:
  rivers:
    - id: r_valoris
      path: [[1500, 200], [1480, 600], [1460, 900], [1500, 1100]]
      notes: "Major river through Valorsplatz to eastern sea"
  bridges:
    - id: b_valorsplatz
      coords: [1500, 1000]
      crosses: r_valoris
  roads:
    - id: rd_lowenskyst_valorsplatz
      path: [[1500, 200], [1490, 600], [1480, 900]]
      notes: "Primary trade artery"
  forgetting_zone:
    polygon: [[700, 2400], [1100, 2400], [1100, 2800], [700, 2800]]
    notes: "Maritime Forgetting + Askeheim TS-gating zone"
  radiation_bands:
    - band: 0
      center: [900, 2700]
      radius: 80
    - band: 1
      center: [900, 2700]
      radius: 200
    # ... per calamity_radiation_v30

terrain_cost_matrix:
  plains: 1.0
  coast: 1.0
  forest: 1.5
  marsh: 2.0
  highland: 1.5
  fjord: 2.5
  pass: 2.0
  mountain: 999.0    # treated as impassable
  road_overlay: 0.7  # multiplier on whatever underlying terrain
  river_crossing_no_bridge: 1.5
  river_crossing_with_bridge: 1.0

vision_range:
  base_units: 8
  modifiers:
    on_highland: 1.5
    in_forest: 0.7
    in_marsh: 0.7
    weather_fog: 0.5
    weather_storm: 0.3
    weather_clear: 1.2
    season_winter: 0.7
    night: 0.4
```

Schema is intentionally **flat and queryable** for Godot impl — settlements list, terrain list, features list. Polygons are arrays of [x, y] vertex pairs. No nested deep hierarchy.

---

## §2 Sample populated entries

The following 5 settlements are populated end-to-end in canonical schema as **proof-of-concept**. They represent the variety of settlement types and territories. Next session uses these as pattern-match reference and fills in remaining 31.

```yaml
settlements:

  S-001:
    name: Valorsplatz Palace
    province: T1
    type: Seat
    controller: Crown
    coords: [1380, 880]
    stats: {prosperity: 4, fortification: 3, prominence: 4}
    notes: "Royal court. Lion's Table HQ. Torben resides here. Capital seat."

  S-006:
    name: Lowenskyst Fortress
    province: T3
    type: Fortress
    controller: Crown
    coords: [1500, 230]
    stats: {prosperity: 1, fortification: 4, prominence: 4}
    notes: "NE Altonian pass fortress. Primary chokepoint. Fort Level 3 (max 4)."

  S-015:
    name: Gransol Parliament
    province: T8
    type: Seat
    controller: Hafenmark
    coords: [690, 480]
    stats: {prosperity: 4, fortification: 2, prominence: 4}
    notes: "Parliament building. Baralta's court. Constitutional center."

  S-026:
    name: Sigurdshelm Keep
    province: T12
    type: Seat
    controller: Varfell
    coords: [380, 1900]
    stats: {prosperity: 3, fortification: 2, prominence: 3}
    notes: "Vaynard's court. Private Collection housed here."

  S-033:
    name: Askeheim Ruins
    province: T15
    type: Outpost
    controller: Wardens
    coords: [890, 2680]
    stats: {prosperity: 0, fortification: 1, prominence: 1}
    notes: "Einhir Catastrophe epicenter. Active Warden operations. Forgetting barrier."

provinces:

  T1:
    name: Valorsplatz
    faction: Crown
    polygon: [[1340, 720], [1500, 760], [1490, 1080], [1320, 1060]]
    region: Eastern Lowlands
    spiritual_weight: 2
    proximity_calamity: 3
    starting_pros: 6
    description: "Capital. River-sea nexus. Italian-coded. Major river through to eastern sea."

terrain:

  - id: northern_range
    type: mountain
    polygon: [[300, 80], [1600, 80], [1620, 280], [310, 290]]
    notes: "Northern Mountains — east-west barrier vs Altonia. Two passes: NE Lowenskyst (T3), NW Spartfell (T10)."

  - id: lake_eidursjo
    type: marsh
    polygon: [[920, 1480], [1000, 1480], [1010, 1900], [930, 1900]]
    notes: "Lake Eidursjø — central-south interior. East-west barrier between Varfell west and Crown east southern corridors."

features:

  rivers:
    - id: r_valoris
      path: [[1500, 200], [1480, 600], [1460, 900], [1500, 1100]]
      notes: "Major river through Valorsplatz to eastern sea. Crown trade artery."
```

These five populated entries demonstrate every schema field and cover all settlement types except Cathedral (S-003 Valorsplatz Cathedral fits) and Mine (S-009 Feldmark Storehouse fits) — next session uses them as pattern-match seed.

---

## §3 Coordinate transform script (deterministic, low-risk)

Path: `tools/geography/jsx_to_canonical.py`

Reads `designs/world/adjacency_map.jsx`, extracts 17 territory (x, y) coordinates from the abstract 700×600 canvas, projects them onto the canonical 1920×2880 system. Outputs YAML stub for Phase 2 authoring session to amend.

The script is **mechanical**: it does the pure scaling, then writes per-territory correction-offset hooks that the next session fills in by hand (knowing the geographic correction needs to apply for T4, T16 Schoenland, T15 Askeheim, etc.).

Output stub looks like (for one territory):

```yaml
T1:
  name: Valorsplatz
  faction: Crown
  jsx_anchor: [560, 245]   # original
  scaled_anchor: [1536, 1176]   # (1920/700)*560, (2880/600)*245
  canonical_anchor: [TBD, TBD]   # to be hand-authored: scaled + geographic correction
  correction_note: "Eastern Lowlands. River-sea nexus. Place south of northern mountains, on east coast adjacent to major river outflow."
```

Next session's job is to fill `canonical_anchor` for each territory using `scaled_anchor` as a starting reference plus geographic-correction-note as guidance.

---

## §4 Phase 2 authoring task list (next session)

The Phase 2 authoring session, opening fresh, executes this work in this order:

1. **Bootstrap, read this workplan.** Confirm decisions §1 still hold or surface objections. ~20k tokens.
2. **Run jsx_to_canonical.py.** Output is YAML stub with 17 scaled territory anchors and correction-note placeholders. ~5k tokens.
3. **Hand-author 17 canonical territory anchors.** Apply geographic correction per workplan §1.3 and the §3 correction notes. Plus province polygons (4-8 vertices each, ~17 polygons). ~30k tokens.
4. **Hand-author 36 settlement coordinates.** Each settlement positioned within its province polygon, type-appropriate (Ports near coast, Mines near mountains, Cathedrals on hills, etc.). Use the 5 sample populated entries as pattern-match. ~25k tokens.
5. **Hand-author terrain layer.** ~30-60 polygon entries covering all 8 terrain types. Use existing SVG geometry as visual reference (it has correct peninsula shape, mountain spine, lake position — only territory labels are wrong). ~40k tokens.
6. **Author features layer.** Rivers, bridges, roads, forgetting zone, radiation bands. ~20k tokens.
7. **Verify schema validity** (YAML parse, all referenced IDs exist, all coordinates within canvas, terrain polygons cover peninsula reasonably). ~10k tokens.
8. **Commit.** Single editorial commit with PP and ED. ~10k tokens.

Total estimate: ~160k tokens. Comfortable within 1M context. Single focused session.

---

## §5 What this workplan does NOT include

- Hand-authoring 36 settlement coordinates (deferred to Phase 2 authoring session).
- Hand-authoring province polygons (deferred).
- Hand-authoring full terrain layer (deferred).
- Hand-authoring full feature layer (rivers, roads, etc.) (deferred).
- Final calibration of terrain-cost values (Phase 4 stress test).
- Final calibration of vision-range values (Phase 4 stress test).
- Spec rewrite for settlement_adjacency_v30 (Phase 3, ED-780).
- New march_layer_v30 doc (Phase 3, ED-780).
- Naval mechanics doc (Phase 3, ED-780, resolves ED-055).
- Stress tests (Phase 4, ED-781).

---

## §6 Cross-references

- ED-779 (this workplan's authority)
- PP-706 (geography canon audit)
- PP-707 (this workplan; minted in same commit as workplan)
- audit doc: `designs/audit/2026-04-30-geography-audit/00_audit_report.md`
- existing canon: `designs/world/geography_v30.md` (CANONICAL 2026-04-05)
- existing data: `designs/world/adjacency_map.jsx` (17 territory coords, abstract 700×600)
- existing visual: `designs/provincial/valoria_map_v2.svg` (DEPRECATED — pre-canon T-numbers)
- existing registry: `designs/territory/settlement_layer_v30.md §2.1` (36 settlements, no coords yet)
- ED-055 (naval mechanics, standing since 2026-04-05; resolved via Phase 3)
- ED-710 (settlement adjacency PROVISIONAL PP-666, will be superseded by Phase 3)
