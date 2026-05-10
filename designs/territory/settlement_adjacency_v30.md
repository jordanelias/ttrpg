<!-- [PROVISIONAL: ED-710 — PP-666 2026-04-19; SUPERSESSION-PENDING per ED-779/ED-780 2026-05-01] -->
<!-- BANNER (ED-779 Phase 2 commit 2026-05-01): -->
<!-- This document remains PROVISIONAL but is on a supersession track. -->
<!-- Successor: designs/territory/march_layer_v30.md (SKELETON; full body Phase 3 ED-780). -->
<!-- Phase 2 geographic canon at: designs/territory/valoria_geography_v30.yaml. -->
<!-- Adjacency graph (26 edges) is now sourced from valoria_geography_v30.yaml :: adjacency. -->
<!-- The mechanical body below remains operative for mass-battle resolution until march_layer_v30 is CANONICAL. -->
<!-- Reconciliation memo: designs/audit/2026-04-30-geography-audit/04_workplan_reconciliation.md (PP-709 §5 O5). -->

<!-- [PROVISIONAL: ED-710 — PP-666 2026-04-19 new mechanical system, pending smoke-test before CANONICAL] -->
# Settlement Adjacency & Mass Battle at Settlement Scale

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

The full graph lives in `designs/world/settlement_adjacency_map.yaml` (generated from this spec + existing `settlement_layer_v30 §2.1` registry + `geography_v30` province adjacency).

Rule for generation:
1. Every Seat is adjacent to every other settlement in the same province.
2. Every province-adjacent pair has exactly one inter-settlement edge connecting their most-connected settlements (typically Seat-to-Seat, but `geography_v30` may specify otherwise).
3. Special routes (Askeheim T15 expedition, T17 mine routes, coastal Ports) are hand-specified per `southernmost_v30` and `geography_v30 Altonian Invasion Routes`.

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

- **Adjacency map file:** `designs/world/settlement_adjacency_map.yaml` needs authoring. Can be derived from `geography_v30` adjacency + settlement Seat positions, but hand-review required for mountain/river/coastal edge classification.
- **Edge capacity:** should edges have capacity limits (only N armies can traverse per season)? Current spec: unlimited. Flag for rebalance after smoke-test.
- **Thread-Witnessed edges:** flagged — not yet tested whether practitioner Leap between settlements is a character-scale convenience or a mass-battle transport mechanism. Current spec: character-scale only.
