<!-- [PROVISIONAL: 2026-05-01 — Phase 2 workplan reconciliation, post-collision] -->
<!-- AUTHORITY: PP-709 (proposed) / ED-779 -->

# Geography Canon Phase 2 — Workplan Reconciliation

**Date:** 2026-05-01
**Status:** PROVISIONAL — reconciliation memo, post-parallel-session collision
**Authority:** ED-779 (extends standing item)
**Context:** Two parallel sessions independently authored Phase 2 workplans. Both committed at PP-707 (commit `0e75ccd0`, file `01_phase2_workplan.md`) and PP-708 (commit `70c77288`, file `00_phase2_workplan.md`). Both claim AUTHORITY: PP-707 internally. They agree on most of the Phase 2 plan and disagree on three specific decisions.

A third draft was prepared by another parallel session (this one). Rather than committing as a third competing workplan, this memo:
1. Acknowledges the duplicate-workplan situation
2. Identifies the three substantive disagreements between the two committed workplans
3. Recommends resolutions for Jordan to confirm or override
4. Adds six decisions that neither committed workplan covers, sourced from the third-draft analysis
5. Designates one workplan as canonical, the other as superseded reference

---

## §1 Workplan disagreements (Jordan-decision required)

### §1.1 Canvas dimensions — 1920×2880 vs 2400×2880

| Workplan | Decision | Rationale given |
|---|---|---|
| PP-707 (`01_phase2_workplan.md`) | **1920×2880** | Godot screen-friendly multiples of 32, 16:9 viewport with peninsula-tall extension, hex-grid overlay alignment for UI v4 §7.4 tactical hex |
| PP-708 (`00_phase2_workplan.md`) | **2400×2880** | 5:6 aspect matches existing jsx settlement bounding box (553×528), accommodates eastward Schoenland and ocean-west margin |
| Third-draft (uncommitted) | 1920×2880 | Same as PP-707, peninsula 2:3 elongation |

**Recommended resolution: 1920×2880 (PP-707 + third-draft).**

PP-708's 2400 width argument is reasonable but PP-707's hex-grid alignment with UI v4 §7.4 (16×10 tactical hex) is mechanically load-bearing for Godot impl — the strategic-map zoomed-in view should grid-align with tactical hex without floating-point recalculation. 1920 width gives clean 32-px hex cells (1920 ÷ 32 = 60 hexes wide at full zoom) where 2400 doesn't divide as cleanly into the canonical hex set.

The Schoenland margin concern PP-708 raises is real but resolvable in 1920-wide canvas: Schoenland is currently authored in jsx at canonical x=1777 (per transform script output), leaves 143px east of island for ocean. Adequate.

### §1.2 Terrain taxonomy — annotations-vs-terrain split

| Workplan | Type count | Treatment of river/road/lake | Notable distinctions |
|---|---|---|---|
| PP-707 | 8 terrain | river/road/bridge/forgetting_zone/radiation_band = annotations | `fjord` distinct from `coast` |
| PP-708 | 8 terrain | river deferred to §1.4 (pending decision) | `fjord_coast` distinct from `coast` |
| Third-draft | 9 terrain | river + lake_sea = terrain types | river included as terrain |

**Recommended resolution: PP-707's annotation model + PP-708's `fjord_coast` naming.**

PP-707's annotation-vs-terrain split is architecturally cleaner. River, road, bridge, forgetting_zone, radiation_band aren't movement-area types — they're feature lines or polygon-overlays that modify movement on whatever terrain underlies them. Making them terrain types creates polygon-overlap ambiguity (does `forest+river` = forest or river for cost lookup?). Annotations resolve cleanly: terrain underneath gives base cost, annotations apply modifier.

PP-708's `fjord_coast` (over PP-707's `fjord`) is more descriptive — `fjord_coast` makes clear it's a *coast type*, not a sea type. Mechanically distinguishes fjord-coast (limited ports, broken terrain) from `coast` (smooth lowland coast, developed ports).

**Final terrain types (8):** `plains`, `forest`, `highland`, `mountain`, `mountain_pass`, `fjord_coast`, `coast`, `marsh`.
**Annotations (5):** `river`, `road`, `bridge`, `forgetting_zone`, `radiation_band`.
**Implicit (impassable):** mountain interior (no terrain ID — represented by mountain polygon without overlapping pass annotation), open ocean (no terrain ID — represented by absence of any land polygon).

This combines both committed workplans' best decisions and is consistent with the third-draft's Forgetting-as-overlay decision (§1.5 in that draft).

### §1.3 Lake Eidursjø geometry concrete coordinates

| Workplan | Lake center | Lake size | T4 Grauwald position |
|---|---|---|---|
| PP-707 | (~960, ~1700) | rx ~180, ry ~280 (oriented N-S) | NE shore ~(1090, 1430) |
| PP-708 | "central-south interior" (no specific coords) | TBD execution session | "above lake's north tip" (no coords) |
| Third-draft | center central-south interior | TBD execution session | NE shore (no specific coords) |

**Recommended resolution: PP-707's specific coordinates as starting values.**

PP-707 commits to concrete numbers. PP-708 and third-draft defer to execution. PP-707's positioning (T4 at 1090, 1430; lake at 960, 1700, 180×280 ellipse) is internally consistent and matches the geographic narrative (lake separating western Varfell territories from eastern Crown farmland; T4 Grauwald above north tip; T11 Halvardshelm west; T14 Ehrenfeld east). Execution session can adjust if the resulting Voronoi province boundaries are wrong, but starting from concrete values is faster than starting from prose.

---

## §2 Decisions absent from both committed workplans

These are present in the uncommitted third-draft analysis but not in either committed workplan. Adding to canonical decision set:

### §2.1 Settlement-coordinate placement rule (per-settlement nudge)

Per-territory anchor positioning is in both workplans. Per-settlement positioning within a multi-settlement territory is not explicitly ruled.

**Decision:** For territories with multiple settlements:
- Primary Seat at territory anchor.
- Secondary settlements within ~50–150 px radius of anchor.
- Bias toward narratively-appropriate features per `settlement_layer_v30 §2.1` description text:
  - Ports nudge toward coastline polygon edge
  - Mines nudge toward mountain polygon
  - Cathedrals are interior-of-region (not coastal)
  - Watchtowers / Outposts at directional periphery (e.g., "guards northern approach" → north of anchor)
  - Garrison-attached settlements adjacent to their fortress

This pattern-template is demonstrated in PP-708's `02_sample_data.yaml` for T1 Valorsplatz but not stated as a rule.

### §2.2 Forgetting zone as overlay-not-terrain (canon preservation)

Both committed workplans treat the Calamity zone as either annotation (PP-707) or polygon-overlay (PP-708 implicitly). Neither states the canon-preservation rationale.

**Decision:** `forgetting_zone` is a separate polygon overlay, NOT a terrain type. Terrain underneath the polygon is classified normally. Entry to the zone triggers Forgetting per `calamity_radiation_v30 §Forgetting` (personal TS ≥ 30 required for individuals; **faction-property exemptions impossible per PP-703**).

This is critical: making Forgetting a terrain type would imply faction-property exemptions are mechanically possible (a faction could have a "this faction ignores forgetting_zone terrain cost" property). The canonical hierarchy is that the Forgetting is universal at the personnel layer, not modulatable by faction or terrain. This decision must be on the record before Phase 2 execution.

### §2.3 March-budget formula

Neither committed workplan specifies the army-movement budget formula. ED-780 will need it.

**Decision:** Per-army per-season march budget = `Military × 100 px` baseline.
- Cavalry-heavy armies (≥ 50% Cav units): 1.5× modifier
- Skirmish/Raid armies (low-tier units only, no siege equipment): 1.3× modifier

Crown Military 5 → 500 px budget per season, ~2-3 settlements traversable per season at 1.0 terrain cost. Matches "1-3 settlements per season" precedent intuition (Ogre Battle, Total War strategic). Cavalry advantage emerges from positional speed. Skirmish enables chevauchée/attrition raids per Jordan flag.

### §2.4 Roads as A*-cached, not authored

Both workplans mention roads but don't specify whether to author 26 settlement-pair road polylines or compute from terrain.

**Decision:** Roads are NOT a separate authored canonical layer. They are computed as A* shortest-path between settlement pairs over the terrain-cost field, then cached as canonical routes.

Eliminates duplicate authoring (don't draw 26 road polylines AND 9 terrain features AND 17 province polygons). The terrain layer IS the road network. Caching the canonical route per settlement-pair gives stable visual roads on the strategic map without per-frame pathfinding cost.

Open follow-up (Phase 4): whether to add a `road_quality` annotation that improves cost on cached routes (settlement-improvement mechanic). Defer until stress tests reveal need.

### §2.5 Naval mechanics scope (explicit Phase 3 deferral)

Both workplans imply naval is for Phase 3 but don't make the scope-line explicit. ED-055 (naval mechanics, open since 2026-04-05) is a real standing item that depends on this decision.

**Decision:** Phase 2 authors the geographic data layer that *can support* naval (settlements have port-type metadata, sea polygons exist as `lake_sea` or absence-of-land). Phase 2 does NOT spec fleet types, port loading/unloading, sea zones, naval combat, weather-on-sea (storms), Schoenland mediation, or Maritime Forgetting Zone. Those are Phase 3 (ED-780).

This explicit scope-line keeps Phase 2 from accidentally swelling into naval design.

### §2.6 Vision range, weather, season — multiplicative factor structure

PP-708 mentions vision range model in §1.6 but punts on specific values. PP-707 has §1.6 vision-range tables. Third-draft has the multiplicative formula explicit.

**Decision:** Three multiplicative factor tables, vision computed at march-time as:

```
effective_vision = base_vision × terrain_factor × weather_factor × season_factor
```

- **Base vision:** 240 px (12.5% of canvas width; one settlement-spacing distance)
- **Terrain factors:** per terrain table
- **Weather factors:** clear 1.0, cloudy 0.85, fog 0.4, storm 0.3, blizzard 0.2
- **Season factors:** spring 1.0, summer 1.05, autumn 0.9, winter 0.6

Numbers are starting values for Phase 4 calibration. The structure (multiplicative factor stack) is canonical; values are tunable.

---

## §3 Workplan-of-record designation

Two workplans cannot both be canonical. **Recommendation:**

- **`designs/audit/2026-04-30-geography-audit/01_phase2_workplan.md` (PP-707) → CANONICAL** for Phase 2.
- **`designs/audit/2026-04-30-geography-audit/00_phase2_workplan.md` (PP-708) → SUPERSEDED reference.** Mark with banner pointing to canonical and to this reconciliation memo.

**Rationale for picking PP-707 as canonical:**
1. Filename matches the existing audit directory pattern (`00_audit_report.md` is the audit; `01_phase2_workplan.md` is workplan-following-audit).
2. PP-707's hex-grid-alignment rationale for 1920×2880 is mechanically stronger than PP-708's settlement-bounding-box rationale for 2400×2880.
3. PP-707's terrain annotation-vs-type split is architecturally cleaner.
4. PP-707 commits to concrete Lake/T4 coordinates rather than deferring.

**Important: PP-708's `fjord_coast` naming is adopted into PP-707's terrain taxonomy** per §1.2 above. PP-708's contribution is preserved.

---

## §4 Phase 2 execution: canonical decision set

For execution session, the canonical Phase 2 decision set is **PP-707's workplan + this memo's resolutions**. Specifically:

| § | Decision | Source |
|---|---|---|
| Canvas | 1920×2880, top-left origin, +x east, +y south | PP-707 + §1.1 confirm |
| Coordinate migration | Linear scale × per-territory geographic correction | PP-707 §1.2 |
| Lake Eidursjø | Center (960, 1700), 180×280 N-S ellipse | PP-707 §1.3 |
| T4 Grauwald | NE shore ~(1090, 1430) | PP-707 §1.3 |
| Terrain types (8) | plains, forest, highland, mountain, mountain_pass, **fjord_coast**, coast, marsh | PP-707 + §1.2 (PP-708 naming) |
| Annotations (5) | river, road, bridge, forgetting_zone, radiation_band | PP-707 §1.4 + §2.2 confirmation |
| Settlement placement | Primary Seat at anchor; ±50-150 px nudge for type-bias | §2.1 (new) |
| Forgetting overlay | Polygon overlay, not terrain. Personnel-layer trigger. | §2.2 (new, canon-preservation) |
| Province polygons | Voronoi from anchors + manual override (T15, T16, lake-crossings) | PP-707 + third-draft §1.6 |
| YAML naming | snake_case, s_NNN, t_NN | PP-707 + third-draft §1.7 |
| Vision multiplicative | base × terrain × weather × season; base 240 px | §2.6 (new, formula explicit) |
| Weather distribution | per-territory roll at season start (Accounting cadence) | PP-707 + third-draft |
| March budget | Military × 100 px; cavalry 1.5×; skirmish 1.3× | §2.3 (new) |
| Roads | A*-cached, not authored | §2.4 (new) |
| Naval scope | Phase 2 data layer only; Phase 3 mechanics | §2.5 (new, explicit) |

---

## §5 Phase 2 execution outputs (consolidated)

| # | Output | Authoring effort |
|---|---|---|
| O1 | `designs/territory/valoria_geography_v30.yaml` | ~15-20k tokens |
| O2 | New canonical map (replaces deprecated `valoria_map_v2.svg`) | ~5k tokens |
| O3 | Banner on PP-708 workplan marking it superseded | ~500 chars |
| O4 | Skeleton `designs/territory/march_layer_v30.md` | ~3-5k tokens (full body Phase 3) |
| O5 | Banner on `settlement_adjacency_v30.md` pointing to v2 successors | ~500 chars |
| O6 | Register entries (PP-XXX, propagation_map note) | standard |

Total Phase 2 commit: ~25-35k tokens authoring, single execution session at ~20% starting context.

---

## §6 Standing items resolved by this memo

- ED-779 progresses from "workplan + sample + script" (unresolved-disagreements) to "workplan + decision-set canonical" (ready-for-execution).

## §7 Standing items still open

- ED-055, ED-710, ED-711, ED-755, ED-763, ED-764, ED-776, ED-777, ED-780, ED-781 — unchanged
- Unresolved: pre-existing PP-684..688 collision in patch_register_active (architecture-session vs mass-battle-MB-batch). Memo flags this as visible-but-not-actioned.

---

## §8 Cross-references

- PP-706 (Phase 1 audit, commit `e0d6a07`)
- PP-707 (workplan A, commit `0e75ccd0`)
- PP-708 (workplan B, commit `70c77288`)
- PP-703 (Forgetting universality, no faction-property exemption — load-bearing for §2.2)
- ED-779 (Phase 2 standing — this memo extends)
- ED-780, ED-781 (Phase 3, 4 standing)
- `designs/world/geography_v30.md` (canonical narrative, 2026-04-05)
- `designs/world/adjacency_map.jsx` (700×600 abstract anchors)
- `designs/territory/settlement_layer_v30.md §2.1` (36-settlement registry)
- `calamity_radiation_v30.md §Forgetting` (canonical Forgetting mechanic — unmodulatable)

---

## §9 Note on parallel-session collision pattern

This is the third register-collision incident in 36 hours (PP-684..688 mass-battle vs architecture; PP-705/ED-778 audit vs ecosystem-cleanup; PP-707/PP-708 Phase 2 workplan duplicates). The pattern: parallel sessions claim adjacent ID space without coordinated reservation. The valoria-orchestrator hooks catch *content-level* collisions but don't prevent *scope-level* duplication.

Out-of-scope for this memo to fix, but worth flagging for orchestrator-skill maintenance: a session-scope-reservation mechanism would prevent two parallel sessions from independently authoring overlapping work. Suggested follow-up: `designs/skills/valoria-orchestrator/...` reservation protocol, or simpler — a `pending_workstream.yaml` checked at task_gate.
