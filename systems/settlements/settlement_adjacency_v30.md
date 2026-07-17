<!-- [PROVISIONAL: ED-710 — PP-666 2026-04-19; PARTIALLY SUPERSEDED post PP-723 2026-05-10] -->
<!-- BANNER updates (latest 2026-05-10): -->
<!-- Strategic movement (march budget, A* pathfinding, vision/recon, route blocking) migrated to march_layer_v30 (Phase 3 closure ED-780, commit 65b918a2). -->
<!-- Settlement-level adjacency graph (PP-723, this commit) authored at valoria_geography_v30.yaml :: settlement_adjacency: (49 edges across 36 settlements). -->
<!-- Battle-resolution-at-settlement (this doc §2) consumes the new settlement_adjacency block; mechanic is now reachable. -->
<!-- The 26 territory-level edges remain canonical at valoria_geography_v30.yaml :: adjacency for strategic-layer routing per march_layer §4.1. -->
<!-- Reconciliation memo: designs/audit/2026-04-30-geography-audit/04_workplan_reconciliation.md (PP-709 §5 O5). -->

<!-- [PROVISIONAL: ED-710 — PP-666 2026-04-19 new mechanical system, pending smoke-test before CANONICAL] -->
# Settlement Adjacency & Mass Battle at Settlement Scale
## Status: CANONICAL

**Status:** PROVISIONAL — approved mechanical design 2026-04-19 (PP-666)
**Supersedes:** Implicit "internal road network" reference in `settlement_layer_v30 §5.1`
**Affects:** `settlement_layer_v30`, `mass_battle_v30`, `military_layer_v30`, `faction_layer_v30 §2` (occupation), `geography_v30`
**Canon compliance:** P-03 (settlement as rendered environment), ROTK precedent (officer-city assignment), CK3 precedent (barony-county hierarchy)

---

## §1 Settlement Adjacency Graph

Every settlement has a defined adjacency list of other settlements it is directly connected to. Adjacency is not derived from province membership — two settlements in the same province may be non-adjacent (if separated by terrain); two settlements in different provinces may be adjacent (if historically connected by road or river).

### §1.1 Edge Types

| Edge Type | Traversal Cost | Battle Modifier | Notes |
|-|-|-|-|
| Road | 1 (standard) | none | Paved or maintained route. Most common. |
| River | 1 | Attacker −1D (river crossing penalty if defender holds far bank) | Fjord/waterway. Applies Valoria's coastal geography. |
| Mountain Pass | 2 | Attacker −1D (altitude/exhaustion) | Highland → lowland or cross-highland connections. |
| Coastal | 1 (requires naval) | Attacker only via Port-type settlement | Port-to-Port edges. Uses naval mechanics. |
| Thread-Witnessed | 0 (instantaneous, character-scale only) | n/a | Practitioner Leap connection between Thread-sensitive settlements. Does not transfer armies. |

### §1.2 Canonical Adjacency Set (36 settlements)

**Status (PP-723, 2026-05-10):** The full graph is canonical at `designs/territory/valoria_geography_v30.yaml :: settlement_adjacency:` block (49 edges: 19 intra-province, 26 inter-province, 4 thread-witnessed). The earlier ED-710 placeholder pointing to `designs/world/settlement_adjacency_map.yaml` is **superseded** — the data lives in the canonical geography YAML alongside territory adjacency for clean two-tier composition.

Rule for generation (applied at PP-723):
1. **Hub settlement adjacent to every other settlement in the same province** (intra-province road edges). Hub is the Seat if one exists; otherwise the highest-priority type per `Seat > Cathedral > Fortress > City > Port > Town > Mine > Outpost`, breaking ties by lowest S-ID for stability. Per-territory hubs:
   - T1 Valorsplatz → S-001 (Seat); T8 Gransol → S-015 (Seat); T12 Sigurdshelm → S-026 (Seat) — three canonical Seats.
   - T9 Himmelenger → S-023 (Cathedral); T2/T3/T10/T14 → Fortresses; T16 → City; remainder → Towns or Outpost.
2. **For each territory-adjacency, hub-to-hub edge** with the territory edge type (road / river / mountain_pass / coastal / gate). 26 territory-adjacency edges produce 26 inter-province settlement edges.
3. **Hand-specified overrides** for canonical port/gate/mine routes:
   - T1↔T16 coastal: T1's Port (S-002 Riverside), not the Palace, is the canonical sea-trade connection.
   - T6↔T15 gate: Stillhelm Watch (S-011, Warden contact post) ↔ Askeheim Gate (S-034). Two land sides of the gate.
   - T13↔T15 gate: Oastad (S-031) ↔ Askeheim Gate (S-034). The other land side.
   - T8↔T17 mining route: Gransol Harbor (S-016) ↔ Halvarshelm Mines (S-021) — ore transport.
   - T3↔T17 mining route: Lowenskyst Garrison Town (S-007) ↔ Halvarshelm Mines (S-021) — military/mine.
   - T2↔T9: Kronmark (S-004) ↔ Himmelenger City (S-024) — Crown→Church border via secular City, not Cathedral.
   - T8↔T9: Gransol Market Quarter (S-017) ↔ Himmelenger City (S-024) — civic-trade route.
   - T1↔T5: Riverside (S-002, Port) ↔ Feldmark (S-008) — grain trade by river preferable to overland from Palace.
4. **Thread-Witnessed special edges** (4 total; character-scale only, no army transport):
   - Cathedral network: Valorsplatz Cathedral (S-003) ↔ Himmelenger Cathedral (S-023) — Solmundic chain of Light.
   - Warden network: Stillhelm Watch (S-011) ↔ Askeheim Ruins (S-033) — Calamity monitoring.
   - Scholarly Thread tie: Sigurdshelm Keep (S-026, housing the Private Collection) ↔ Himmelenger Seminary (S-025).
   - RM covert network: Grauwald Lodge (S-029) ↔ Oastad Shrine (S-032) — Einhir cultural preservation.

**Edge-type-to-Manoeuvre mapping** (consumed by `march_layer §4.1` and `mass_battle §A.9` Phase 3 extension): see §1.1 above. The geographic battle-terrain derivation introduced by ED-780 now has settlement-edge data to consume.

### §1.3 Army Movement

An army occupies one settlement at a time. Movement:
- **Intra-province:** traverse 1 edge per season (free within province, no Accord cost).
- **Inter-province:** traverse 1 edge per season. Crosses a provincial border — triggers Casus Belli check if edge connects two factions.
- **Bypass:** army may skip a settlement it does not wish to assault (per `settlement_layer §5.1` Bypass rule). Bypassed settlement remains hostile.

Per season, an army may move up to **Military ÷ 2 edges** (round down, minimum 1). This replaces the current "one province per season" movement abstraction with settlement-granular movement.

---

## §2 Mass Battle at Settlement Scale

All mass battles now occur at specific settlements. `mass_battle_v30` Part B (BG Battle Resolution) continues to govern the mechanical resolution, but the battle's *location* is a settlement node, not a province.

### §2.1 Battle Declaration

An attacker targeting a settlement:
1. Moves an army adjacent to the target settlement.
2. Declares Assault, Siege, or Bypass (per `settlement_layer §5.1`).
3. Assault or Siege triggers `mass_battle_v30` Part B resolution at the settlement location.

### §2.2 Terrain from Edge Type

The edge the attacker traversed into the settlement provides a Manoeuvre Phase modifier:

| Edge Traversed | Manoeuvre Modifier |
|-|-|
| Road | none |
| River | Attacker −1D (defender benefits from crossing) |
| Mountain Pass | Attacker −1D (fatigue) |
| Coastal (naval) | Attacker loses Fort-level bonus (arrived by sea, no pre-battle positioning) |

Plus settlement type modifier:

| Settlement Type | Defender Modifier |
|-|-|
| Fortress | +Fort Level to Defender Ob (existing `mass_battle A.4`) |
| Seat | +1 Defender Discipline (capital defense is rallying) |
| Port | Defender gains +1D if naval reinforcements available |
| Cathedral | Attacker takes Church Casus Belli (political cost, not battle cost) |
| Mine | Attacker gains captured Prosperity on victory |
| Town / Outpost | No modifier |

### §2.3 Battle Consequences at Settlement Scale

`mass_battle_v30 Part E` consequences continue to apply, but scoped to the settlement:
- MS −1 to −2: applied peninsula-wide (unchanged).
- Strain +1: applied peninsula-wide (unchanged).
- IP +2: applied peninsula-wide (unchanged).
- **Accord drop:** now applies to the **settlement's Order** (Order −1), not the province's Accord. Province Accord recalculates via floor-average derivation per `settlement_layer §1.3`.
- **Settlement Prosperity −1** on Assault outcome Partial or worse (battle damage to local economy).

### §2.4 Siege at Settlement Scale

Siege (`settlement_layer §5.1`) runs per-settlement. Attacker holds adjacent position, cannot move, defender Order −1/season until Order = 0 → surrender. Unchanged from existing spec; this ED formalizes it against the adjacency graph.

---

## §3 Invasion Sequencing

An invader entering a province now has a defined sequence: they enter via the edge their army traversed. They must first engage or bypass the settlement they enter. They cannot jump to arbitrary settlements in the province.

This replaces the current abstraction where an invader "enters a territory" and picks any settlement. Movement is path-constrained.

**Example:** Hafenmark army at S-015 Gransol Parliament wishes to invade T2 Kronmark. Gransol is adjacent (via road edge) to S-012 Kronburg Seat. The army moves to Kronburg and must engage or bypass. It cannot leap to S-014 Kronmark Cathedral without first passing through Kronburg or taking a different edge.

---

## §4 Implementation (Videogame)

- The 36-settlement network renders as a graph overlay on the strategic map.
- Army movement = clicking edges between settlements.
- Mass battles fire at the destination settlement node, presented as a battle scene.
- Siege = persistent attacker-token at settlement edge, ticking Order down each Accounting.

---

## §6 Cross-reference: March Layer (Phase 3, ED-780)

Strategic movement (march budget, A* pathfinding, vision/recon, route blocking, multi-edge moves, Casus Belli on edge crossing) is canonical at `designs/territory/march_layer_v30.md` (Phase 3 mechanical body authored 2026-05-10 under ED-780). This document (`settlement_adjacency_v30.md`) preserves the authored Edge Type → Manoeuvre Modifier mapping (§2.2) which is consumed by march_layer §4.2 by reference. Future strategic-movement extensions should be authored in march_layer; settlement-scale battle resolution remains here.

## §5 Open Items

- **Adjacency map file:** ~~`designs/world/settlement_adjacency_map.yaml` needs authoring.~~ **CLOSED 2026-05-10 PP-723** — graph authored as `valoria_geography_v30.yaml :: settlement_adjacency:` block (49 edges); `designs/world/settlement_adjacency_map.yaml` is not used (data lives in geography YAML for clean two-tier composition).
- **Edge capacity:** should edges have capacity limits (only N armies can traverse per season)? Current spec: unlimited. Flag for rebalance after smoke-test.
- **Thread-Witnessed edges:** flagged — not yet tested whether practitioner Leap between settlements is a character-scale convenience or a mass-battle transport mechanism. Current spec: character-scale only.
