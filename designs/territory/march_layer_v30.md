<!-- [PROVISIONAL: 2026-05-01 — march layer skeleton, full body Phase 3] -->
<!-- AUTHORITY: ED-780 (Phase 3) / depends-on: ED-779 (Phase 2 geography canon) -->

# VALORIA — March Layer (Strategic Movement)

**Status:** SKELETON — Phase 2 lock-in for structural decisions; full mechanical body authored in Phase 3 under ED-780.
**Authority:** ED-780 (Phase 3 standing). Depends on Phase 2 canon at `designs/territory/valoria_geography_v30.yaml`.
**Supersedes (planned):** `designs/territory/settlement_adjacency_v30.md` (PP-666 PROVISIONAL movement abstraction). Banner posted at predecessor pointing here.
**Affects:** `mass_battle_v30 §A.4–A.11`, `military_layer_v30`, `faction_layer_v30 §2`, `clocks_v30` (Accounting cadence), `geography_v30`.
**Canon compliance:** P-03 (settlement as rendered environment), P-15 (settlement identity persistence), PP-703 (Forgetting universality, no faction exemption).

---

## §1 March Budget

Locked-in formula per PP-709 §2.3 (this Phase 2 commit):

```
march_budget_pixels = Military × 100
  × cavalry_modifier (1.5 if Cav ≥ 50% of army composition)
  × skirmish_modifier (1.3 if low-tier-only, no siege equipment)
```

Cost per traversed segment: `distance_px × terrain_cost_multiplier` per `valoria_geography_v30.yaml :: terrain_cost_matrix`.

### §1.1 Cavalry advantage
### §1.2 Skirmish / chevauchée
### §1.3 Supply line attrition (Phase 4 calibration)
### §1.4 Multi-army coordination across the budget

---

## §2 Pathfinding

Routes computed as A* shortest-path over the terrain-cost field per PP-709 §2.4.

### §2.1 Cached canonical routes
Roads are NOT a separate authored canonical layer. They are A*-cached between settlement pairs and rendered as stable strategic-map roads.

### §2.2 Cache invalidation
### §2.3 Player-visible pathfinding UI
### §2.4 Route blocking (siege, hostile occupation, weather closure)

---

## §3 Vision & Reconnaissance

Multiplicative factor stack per PP-709 §2.6:

```
effective_vision = base_vision × terrain_factor × weather_factor × season_factor
```

Base 240 px; factor tables in `valoria_geography_v30.yaml :: vision_range`.

### §3.1 Fog of war
### §3.2 Scouting actions
### §3.3 Counter-reconnaissance
### §3.4 Thread-Witnessed scouting (TS-gated; not army transport)

---

## §4 Adjacency Edges

Graph defined in `valoria_geography_v30.yaml :: adjacency` (26 edges across 17 provinces).

### §4.1 Edge types
| Type | Source |
|------|--------|
| road | Standard inter-settlement road |
| coastal | Port-to-Port; requires naval (Phase 3 ED-055) |
| mountain_pass | Highland → lowland; attacker −1D |
| gate | Askeheim Gate edges (T6↔T15, T13↔T15); marsh-entry, attacker −1D |
| river | Per `bridges` table; crossing penalty without bridge |

### §4.2 Edge traversal modifiers in mass battle
Per `settlement_adjacency_v30 §2.2` (preserved). Manoeuvre Phase modifiers carry forward.

### §4.3 Bypass rule
Per `settlement_layer §5.1`. An army may skip a settlement; bypassed settlement remains hostile.

---

## §5 Movement Sequencing

### §5.1 Per-season march
Single march budget per army per season. Consumed across multiple edges until exhausted.

### §5.2 Multi-edge moves
### §5.3 Engagement-on-arrival vs siege declaration
### §5.4 Inter-faction edge crossing → Casus Belli check

---

## §6 Naval (Phase 3 ED-055)

Phase 2 publishes the geographic data that *can support* naval (Port settlements have port metadata; sea polygons exist). Phase 3 specifies fleet types, port loading, sea zones, naval combat, weather-on-sea, Schoenland mediation, Maritime Forgetting interaction.

### §6.1 Fleet composition
### §6.2 Naval combat resolution
### §6.3 Schoenland passage rules (IP ≥ 75 → Altonian sea route opens)
### §6.4 Maritime Forgetting Zone interaction
### §6.5 Coastal-edge traversal at Port settlements

---

## §7 Forgetting & Calamity Interactions

### §7.1 Forgetting zone polygon entry (personal scale)
Per PP-709 §2.2: zone is overlay, NOT terrain. Entry triggers personnel-layer Forgetting per `calamity_radiation_v30 §Forgetting`. TS ≥ 30 individual gating; **no faction-property exemption** (PP-703 universality, load-bearing).

### §7.2 Radiation band traversal cost (RS-band modulated)
Per `calamity_radiation_v30` band table referenced from `valoria_geography_v30.yaml :: radiation_bands`.

### §7.3 Askeheim Gate mechanics (Gate 1 T13, Gate 2 T6)

---

## §8 Implementation (Godot 4.6)

### §8.1 Strategic map graph rendering
17 province polygons + 36 settlement nodes + 26 adjacency edges as a graph overlay. Settlement nodes are clickable; edges are clickable for path preview.

### §8.2 Hex-grid alignment for tactical zoom
1920×2880 ÷ 32 = 60×90 hex grid at full zoom (per UI v4 §7.4 tactical hex). Strategic-to-tactical zoom = 4× (`scale_anchors :: strategic_to_tactical_zoom`).

### §8.3 A* over terrain-cost field
Unity-style: precompute terrain-cost grid at strategic resolution (~60×90 cells); cache shortest paths for 36×36 settlement pairs (≤ 630 unordered pairs); invalidate on terrain or occupation change.

### §8.4 March budget UI lens
Per PP-688 articulation Tier 1 (UI lens). Player sees their army's remaining budget as a movement radius preview from current settlement.

### §8.5 Vision overlay rendering
Fog-of-war shader applied per army's effective_vision radius; multiplicative stack updates each Accounting (clocks_v30).

---

## §9 Open Items (carried into Phase 3)

| ID | Description | Source |
|---|---|---|
| ED-055 | Maritime Forgetting + naval mechanics — Phase 3 specification. | geography_v30 §Open Items |
| ED-710 | settlement_adjacency_v30 PP-666 PROVISIONAL — superseded by this doc once full body lands. | adjacency v30 |
| ED-781 | Phase 4 stress tests — calibrate terrain cost, vision, march budget seed values. | PP-709 |
| MARCH-01 | Edge capacity (max armies per edge per season) — current spec unlimited; flag for stress test. | adjacency v30 §5 |
| MARCH-02 | Thread-Witnessed Leap as character-only (no army transport) — confirm at smoke test. | adjacency v30 §5 |
| MARCH-03 | Road quality annotation (settlement-improvement mechanic) — defer until Phase 4 reveals need. | PP-709 §2.4 |
| MARCH-04 | Naval Casus Belli — does coastal-edge traversal at Port settlement carry the same CB cost as land border crossing? | this skeleton |

---

## §10 Cross-References

- Phase 2 canon data: `designs/territory/valoria_geography_v30.yaml`
- Audit trail: `designs/audit/2026-04-30-geography-audit/` (00 audit, 01 workplan PP-707, 04 reconciliation PP-709)
- Settlement registry: `designs/territory/settlement_layer_v30.md §2.1`
- Predecessor (PP-666): `designs/territory/settlement_adjacency_v30.md`
- Geography narrative: `designs/world/geography_v30.md` + infill
- Calamity mechanics: `designs/setting/calamity_radiation_v30.md`
- Mass battle resolution: `designs/mass-battle/mass_battle_v30.md` (Part B preserved)
- UI lens for march budget: PP-688 Tier 1 articulation layer

---

## §11 PROVISIONAL → CANONICAL gate

This skeleton becomes the canonical March Layer when:
1. Phase 3 (ED-780) authors §1–§7 full body.
2. Phase 4 (ED-781) stress-tests calibration values for terrain cost / vision / march budget.
3. `settlement_adjacency_v30.md` PP-666 PROVISIONAL is formally superseded.
4. ED-055 naval mechanics specified in §6.

Until then: structural metadata + load-bearing locked decisions only. Mechanical mass-battle integration continues to use `settlement_adjacency_v30 §2.2` modifiers as authoritative.
