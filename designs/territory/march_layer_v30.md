<!-- [PROVISIONAL: 2026-05-01 — march layer skeleton, full body Phase 3] -->
<!-- AUTHORITY: ED-780 (Phase 3) / depends-on: ED-779 (Phase 2 geography canon) -->

# VALORIA — March Layer (Strategic Movement)

**Status:** PROVISIONAL — Phase 3 mechanical body authored 2026-05-10 (ED-780 closure). Phase 4 (ED-781) stress tests pending. Naval (§6) deferred to ED-055.
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
A cavalry-majority army (≥ 50% cavalry by Size composition) gains 1.5× march budget. Mid-tier and Elite cavalry both qualify; partial-cavalry compositions below 50% threshold receive no modifier. Dismounted cavalry (status flag, e.g., siege-bound or terrain-forced) lose the modifier for that march. The 1.5× compounds with skirmish-modifier (§1.2) when both apply, capped at 1.7× total to prevent cumulative explosion in light cavalry skirmish forces.

### §1.2 Skirmish / chevauchée
A skirmish-only force (low-tier units only — Levy, Militia, Light Cavalry — with no siege equipment, no Elite, no heavy infantry) gains 1.3× march budget. Tactical purpose: chevauchée operations, scouting columns, raid forces. The skirmish force CANNOT initiate Settlement Siege (per `settlement_layer §6 Siege Declaration`) — siege requires at least one Heavy Infantry or Siege unit in composition. Cavalry-skirmish stack: 1.5 × 1.3 = 1.95, capped at 1.7× (§1.1).

### §1.3 Supply line attrition (Phase 4 calibration)
Armies operating beyond a finite supply radius (default 8 settlements from a friendly Mine, Cathedral, or Port supply node) accumulate Attrition strain at +1 per season per 4 settlements over budget. Attrition strain converts to Size loss at season Accounting at 1:1 ratio (rounded down). Friendly territory traversal does NOT contribute to attrition; hostile/contested territory does. Phase 4 stress tests (ED-781) calibrate the supply radius and conversion rates against historical Renaissance-period Italian-state campaigns.

### §1.4 Multi-army coordination across the budget
A faction with multiple armies executes march budgets independently per army; budgets do NOT pool. An army with 0 remaining budget cannot participate in a battle scheduled by another friendly army that turn (per `mass_battle §A.4 ENGAGEMENT`). Coordinated arrival at a battle site requires the slower army to commit budget early-season; the faster army may arrive ahead and engage (or wait, declining to engage). Combined-army engagement requires both armies arriving in the same Manoeuvre Phase tick.

---

## §2 Pathfinding

Routes computed as A* shortest-path over the terrain-cost field per PP-709 §2.4.

### §2.1 Cached canonical routes
Roads are NOT a separate authored canonical layer. They are A*-cached between settlement pairs and rendered as stable strategic-map roads.

### §2.2 Cache invalidation
Cached A* paths invalidate when: (a) a settlement on the path is sieged or hostile-occupied (§2.4 route blocking); (b) a calamity radiation band changes magnitude (terrain-cost matrix updates); (c) a bridge collapses or is destroyed (river crossing penalty changes); (d) weather closure activates a winter-impassable mountain pass. Engine recomputes only paths that pass through the invalidated cell; non-affected paths retain cache.

### §2.3 Player-visible pathfinding UI
On Strategic Map (Godot 4.6 implementation per §8.1), clicking a destination settlement renders the proposed march route as a highlighted polyline overlay with per-segment cost annotations and total budget consumption. Alternate routes (within +20% cost) are offered as toggleable variants. Hover-tooltip shows: distance_px, terrain factors applied, cavalry/skirmish modifiers active, expected season-arrival.

### §2.4 Route blocking (siege, hostile occupation, weather closure)
A route is blocked if any of: (a) hostile army occupies a settlement on the path with Size ≥ 1 (engagement is forced — march halts at the blocking settlement; battle resolves per `mass_battle §A.5`); (b) sieged settlement on path is hostile-controlled (army must besiege or detour; siege bypass per `settlement_layer §5.1`); (c) winter weather closure on a mountain_pass edge between season Q4 and Q1 (path detours via lowland edges); (d) calamity radiation band ≥ 4 (army takes Forgetting/attrition risk per `calamity_radiation_v30`; player must opt-in to traverse).

---

## §3 Vision & Reconnaissance

Multiplicative factor stack per PP-709 §2.6:

```
effective_vision = base_vision × terrain_factor × weather_factor × season_factor
```

Base 240 px; factor tables in `valoria_geography_v30.yaml :: vision_range`.

### §3.1 Fog of war
Settlements outside any friendly army's effective_vision (per §3 multiplicative stack) render as fog-of-war; their last-known state (faction control, garrison strength, Prosperity tier) persists until a friendly army or scout re-enters vision range. Hostile army positions in fog-of-war are HIDDEN; faction Intelligence (Investigate Strategic vs Ob 3) can reveal partial state.

### §3.2 Scouting actions
Scouting is an army-level action consuming half the march budget for the season. Scout output: full vision of all settlements within 2 hops on the adjacency graph from the scout's starting position; reveals army composition (size, tier mix) but NOT faction priorities or arc-state.

### §3.3 Counter-reconnaissance
A faction with active counter-reconnaissance (Intel investment ≥ 3 in territory) imposes +1 Ob on enemy scouting actions and reduces scouted vision range by 1 hop. Counter-recon does not reveal scouting attempts to the defender automatically — only on contested-roll success.

### §3.4 Thread-Witnessed scouting (TS-gated; not army transport)
A practitioner with Thread Sensitivity ≥ 50 may observe a settlement's rendered state at distance via Thread-Read operation (per `threadwork_v30 §2.6 Knot-mediated remote Thread-Read`). This reveals settlement state per §3.2 scouting output but does NOT reveal hostile army positions — Threads bind to settlements, not to mobile units in transit. Cost: +1 Knot strain per observation (per F2 `fieldwork_lifecycle_stress_01 F-L06`). Crucially: Thread-Witnessed scouting is observation only; armies cannot be transported via Threads (P-12 relational contagion does not propagate physical mass).

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
Per `settlement_layer §5.1`. An army may skip a settlement on its march path; bypassed settlements remain hostile and may be re-engaged on subsequent seasons. Bypass risk: hostile garrison may sortie against the bypassing army's supply line (per §1.3 attrition), forcing engagement at +1 attrition per bypassed hostile settlement at season Accounting. The Crown's classical strategic pattern (Italian condottieri, Renaissance period reference) is a sequence of forced bypass-and-return campaigns.

---

## §5 Movement Sequencing

### §5.1 Per-season march
Single march budget per army per season. Consumed across multiple edges until exhausted.

### §5.2 Multi-edge moves
A march budget may consume multiple edges in sequence. The army moves to each settlement in order; each edge consumes its `distance_px × terrain_cost` from the budget. The army stops at the first settlement where: (a) budget is fully consumed, (b) engagement is forced (§2.4), or (c) player declines further movement. Stopping mid-edge is not permitted; the army arrives at a settlement node or remains at start.

### §5.3 Engagement-on-arrival vs siege declaration
On arriving at a hostile-controlled settlement, the player declares either ENGAGEMENT (immediate Manoeuvre Phase per `mass_battle §A.4`, terrain modifiers from §4.2 carry forward) or SIEGE (per `settlement_layer §6`, longer multi-season process with attrition exchange). ENGAGEMENT requires a defending army on-site; if the settlement has only garrison forces (no field army), the choice is SIEGE only — garrison cannot Manoeuvre. The choice is locked at arrival; cannot be changed mid-engagement.

### §5.4 Inter-faction edge crossing → Casus Belli check
Crossing an edge into another faction's controlled territory triggers a Casus Belli check per `faction_layer_v30 §3 War Doctrine`. Permitted crossings (treaty, alliance, vassalage) consume budget normally with no political cost. Unauthorised crossings produce: (a) immediate Casus Belli +1 to the territorial faction, (b) IP −2 to the trespassing faction, (c) territorial faction may treat the army as hostile from next Manoeuvre tick (engagement-on-arrival forced if the trespasser does not retreat by next-season Accounting).

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
The two Askeheim Gates (Gate 1 in T13, Gate 2 in T6) are marsh-edge passage points per `valoria_geography_v30.yaml :: gates` (PP-709 §2.4). Each gate edge imposes attacker −1D in mass-battle Manoeuvre Phase (terrain familiarity favors the side that has held the gate longer). Gate edges are also the only land-route into T15 (Askeheim itself); naval bypass requires Phase 3 ED-055 naval mechanics. Holding a gate confers +1 IP per season (strategic chokepoint value).

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
