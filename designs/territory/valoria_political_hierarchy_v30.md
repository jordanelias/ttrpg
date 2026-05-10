<!-- [PROVISIONAL: 2026-05-10 — PP-726 (substrate canon: Valn → Kingdom → Duchy → Province → Settlement hierarchy)] -->
<!-- STATUS: PROVISIONAL — Class A canonical foundational document. -->
<!-- AUTHORITY: PP-726 (this doc; resolves the granularity error in PP-666/ED-710/PP-723 settlement modeling). -->
<!-- COMPANIONS: designs/territory/settlement_layer_v30.md (per-settlement registry, governance, types — refactored at PP-726 §2.1 to reference settlements proper rather than mixed districts/sub-features); designs/territory/valoria_geography_v30.yaml :: settlement_adjacency: (the 56-edge canonical march-route graph at correct granularity, also rebuilt at PP-726). -->
<!-- SUPERSEDES: implicit substrate-modeling assumption that "settlement = entry in §2.1" — that schema mixed siege-target settlements with subservient districts/sub-features at one level. PP-726 introduces explicit hierarchy and corrects the modeling. -->

# Valoria — Political Hierarchy Canon (PP-726)

**Class:** A — substrate-defining canon.
**Status:** PROVISIONAL.
**Purpose.** Establish the canonical political hierarchy from peninsula geography down to march-route settlement: who owns what, at what scale, under what rules. Closes the substrate-modeling error that ran through PP-666/ED-710/PP-723 — those iterations conflated siege-target settlements with their subservient districts and outposts, producing a 36-entry registry that mixed two granularities and a 49-edge adjacency graph at the wrong level. PP-726 re-cuts the schema at the correct level and establishes the political-administrative scaffolding (duchies, provinces, fracturing rule, political-value computation, governor assignment).

---

## §1 The hierarchy

```
Valn (peninsula — geographic extent)
└── Kingdom of Valoria (sovereign realm)
    ├── Duchy (3 within Kingdom)
    │   └── Province (multiple per duchy)
    │       └── Territory = Settlement (1–3 per province)
    └── Special-case entities (within Kingdom geography but outside the duchy structure)
        ├── Himmelenger (Church city-state — sovereign ecclesiastical entity)
        ├── Askeheim (Calamity-zone wilderness — no settlements until healing)
        └── Schoenland (foreign Altonian island — political tributary, sea-connected only)
```

### §1.1 Levels

**Valn** is the peninsula — pure geographic extent, encompassing the Kingdom of Valoria, the foreign Altonian holdings to the north, and the Calamity-zone of Askeheim within Valorian boundaries. Valn is not a political entity; the term names the land mass.

**Kingdom of Valoria** is the sovereign realm covering most of Valn. The Crown holds it. The current monarch is **Almund** (Almud), who is also Duke of Valorsmark (one of the three constituent duchies). As monarch, Almud holds direct lordship over his own duchy and exercises overlordship over the other two duchies; the Dukes of Varfell and Hafenmark owe him fealty and operate within his royal authority while administering their own duchies day-to-day.

**Duchies** (3 — each owned by a Duke):
- **Valorsmark** — held by **Almud** (also monarch). Crown duchy. Six provinces. Cultural template: Solmundic-Latinate.
- **Hafenmark** — held by **Baralta**. Commercial duchy. Four provinces. Cultural template: Hanseatic-commercial.
- **Varfell** — held by **Vaynard**. Northern duchy. Four provinces. Cultural template: Old-Einhir / Norse.

**Provinces** are the administrative regions within each duchy. Each duchy has multiple provinces; each province is comprised of 1–3 territories (settlements). Provinces aggregate political value to the duchy. The province-level was previously called "territory" in early canon (T1, T2, …, T17) — that nomenclature is deprecated by PP-726; the level is canonically "province" and the labels remain (Valorsplatz province, Kronmark province, …).

**Territory = Settlement** is the smallest political unit. A territory is the geographic extent of a single settlement plus its agricultural hinterland and subservient sub-features (districts, garrison towns, mines, watchtowers, lodges, shrines, outposts, harbors, watches, storehouses). A settlement is the **siege target** — the city, fortress, village, or town that armies march to and lay siege upon. Districts and other sub-features are not separately siegeable; they are taken when the parent settlement is taken.

### §1.2 Special-case entities

Three entities sit within Valn geographically but outside the standard duchy/province hierarchy:

**Himmelenger** is a Church city-state — sovereign ecclesiastical entity analogous to the historical Vatican. The Confessor (Cardinal of Faith) holds it as Church territory, not as a province of any duchy. It is a single settlement (the cathedral-city itself) with internal districts (Cathedral, Seminary, City) but no surrounding province-territory in the Kingdom's political hierarchy. Himmelenger sits geographically between Valorsmark and Hafenmark provinces but answers politically to the Church alone. Its march-route connections (5 edges per `valoria_geography :: settlement_adjacency`) are inter-province in the graph topology even though Himmelenger itself is not a province.

**Askeheim** is a Calamity-zone wilderness — the Einhir Catastrophe epicenter. Currently zero settlements (the Ruins and the Gate are unmanned outposts/observation features, not siege targets). Askeheim is not a province in the duchy hierarchy; it is unincorporated wilderness pending Warden-led healing. Should the Calamity zone heal sufficiently, settlements may emerge there and the territory may be assigned to a duchy — but that is a future-state contingent on canonical healing events, not a current condition.

**Schoenland** is a foreign Altonian island — politically independent of the Kingdom of Valoria. It engages the Kingdom only through the sea route to Valorsplatz (the Crown capital's port handles Schoenland trade and diplomatic contact). Schoenland has its own internal districts (City, Harbor) but appears in the Kingdom's adjacency graph as a single foreign-tributary node connected by one sea-edge. It is exempt from the Kingdom's ≥2 march-route rule (its singular sea-connection is the canonical condition pending ED-055 naval-scope expansion, which would canonically add additional sea routes).

---

## §2 The rules

### §2.1 Settlement count per province

Each province has **1–3 settlements**. Provinces with denser geography or economy (capitals, breadbaskets, commerce hubs, multi-fjord coastlines, industrial mining regions) carry 3 settlements; sparser provinces (chokepoints, remote valleys, Calamity-edge depopulation zones, highland forests) carry 2. **The minimum is 2 — every province in the Kingdom must have at least two settlements** (so that no province is reducible to a single siege-target with brittle strategic surface). The current canonical distribution is 7 provinces at 3 settlements and 7 at 2 settlements (14 provinces total in the duchy hierarchy = 35 settlements), per `settlement_layer_v30 §2.1`.

### §2.2 Settlement march-route connections

**Each settlement is connected by road to at least two other settlements.** Connections are settlement-to-settlement march routes — the canonical strategic-layer movement substrate. A settlement's connections may be intra-province (to other settlements within the same province) or inter-province (to settlements in adjacent provinces). The ≥2 rule ensures resilience: no settlement can be cut off by losing a single connection, and no settlement is reachable by only one approach. Sea routes count (Valorsplatz↔Schoenland is canonically one sea-edge).

Per the canonical adjacency graph in `valoria_geography_v30.yaml :: settlement_adjacency:`, all 35 Kingdom settlements satisfy ≥2 connections, plus Himmelenger at 5 connections (city-state crossroads). Schoenland at 1 connection is the canonical foreign-exempt case.

### §2.3 Province fracturing rule

**A province whose constituent territories are aligned to different factions is canonically fractured into smaller sub-provinces** named *northern*/*southern* or *western*/*eastern* (per geographic split). Each sub-province retains the 1–3 territories rule and is treated as a full province for political-value purposes. Fracturing is a state-transition produced by faction-control changes during play (e.g., a settlement defects to a different faction; the province governing that settlement may fracture if the new alignment is incompatible with the duchy's faction). Reunification is symmetric: when all sub-provinces of a fractured province return to common faction-alignment, they merge back into the original province.

This rule introduces dynamic political geography: provinces are not static administrative units but state-machines that respond to faction-control shifts. Fracturing makes faction-territorial conflict more legible and produces secondary political-value consequences (per §2.4).

### §2.4 Political value computation

**Each faction holds a total political value used for parliamentary influence and Mandate-track inputs**, computed from its province-and-territory holdings. The basic principle: a unified province is worth more than the sum of its constituent territories considered individually, incentivizing consolidation.

Provisional formula (subject to balance calibration):

```
political_value(faction) = Σ over owned-territories(territory_value)
                         + Σ over fully-owned provinces(province_unification_bonus)
```

Where `territory_value` is a per-settlement scalar derived from settlement type (Seat/Cathedral/Fortress/City/Port/Town/Mine/Outpost) plus current Prosperity/Defense/Order, and `province_unification_bonus` is a positive scalar awarded only when the faction owns *all* territories within a province. Specific scalar values are TBD pending balance pass; the structure is canonical here, the numbers are not.

Implication: a faction holding two of three territories in a province gets only the territory_value sum; capturing the third territory triggers the unification bonus. This creates a sharp strategic-layer incentive to fully resolve provincial territory-control rather than leave unsettled splits.

### §2.5 Governor assignment

**Each settlement is assigned a Governor by the faction that controls that territory.** Governor mechanics live in `settlement_layer_v30 §3.2` (existing canon, refined here only at the granularity layer): Standing 3+ NPCs (Counselor, Lieutenant, Successor) and PCs are eligible for Governor postings; the eligible settlement type depends on Standing. Governor assignment is per-settlement, not per-province — a faction can have different Governors for different territories within the same province, each accountable to their faction-leader (the Duke for duchy-aligned settlements; Almud for Crown-aligned; the Confessor for Church-aligned at Himmelenger).

Governance actions per season are specified in `settlement_layer §3.2`. The governance substrate is unchanged by PP-726; what changes is the granularity at which governance operates (per-settlement, with sub-features inheriting their parent's Governor).

---

## §3 Sub-features (subservient to settlements)

Each settlement may host **sub-features** — districts, garrison towns, mines, watchtowers, lodges, shrines, watches, storehouses, harbors, gates, ruins. Sub-features are *not* settlements: they are not separately siegeable, not separately governed, and not separate march-targets in the adjacency graph. They are properties of their parent settlement that confer mechanical effects:

- **Cathedral / Seminary district** within a settlement → Church-faction presence; ecclesiastical scenes available; Confession's Cardinal-relevant access.
- **Mine / Storehouse / industrial district** → Wealth/Resource production per settlement_layer income mechanics.
- **Harbor / Port district** → trade-route enablement (sea routes attach to settlements with Harbor districts).
- **Garrison town / Barracks district** → military-unit production capacity; standing-army support.
- **Watchtower / Watch outpost** → vision/recon range extension into adjacent territory.
- **Lodge / Shrine** → specific cultural/religious affordances (RM meeting access; Einhir ceremonial presence).
- **Gate / Ruins** within Calamity zones → observation/Warden-operations features without settlement-level mechanics.

The full sub-features registry is canonical at `settlement_layer_v30 §2.2` (post-PP-726 refactor — a new section listing the 30+ sub-features as properties of their parent settlements, replacing the deprecated practice of listing them as standalone settlements in old §2.1).

---

## §4 Migration from old canon

Per PP-726, the following deprecations apply:

- **Old "territory" = New "province"**: T1..T17 nomenclature deprecated; canonical labels are the province names (Valorsplatz, Kronmark, Lowenskyst, Feldmark, Stillhelm, Ehrenfeld, Rendstad, Gransol, Spartfell, Halvarshelm, Grauwald, Halvardshelm, Sigurdshelm, Oastad, Himmelenger, Askeheim, Schoenland — last three special).
- **Old S-001..S-036 IDs**: deprecated. New canonical IDs per `settlement_layer_v30 §2.1` are S-001..S-037 covering the 35 Kingdom settlements + Himmelenger + Schoenland. Old S-IDs in non-substrate documents (character_canon Part B per-NPC sheets, migration_roster, npc_roster, editorial_ledger historical entries, propagation_map historical entries) are migrated lazily as those documents are next touched; PP-726 only updates the substrate-canonical files (settlement_layer §2.1, valoria_geography settlement_adjacency, npc_relational_graph §6 settlement coupling).
- **Sub-features collapse**: the 36 old §2.1 entries that were a mix of settlements and districts/outposts collapse to 35 Kingdom settlements + sub-features registry. The mapping is canonical at `settlement_layer_v30 §2.2` migration table.

---

## §5 Open items

- **Province-fracturing canonicalization (§2.3)**: rule stated; specific event triggers and reunification thresholds not yet specified. Likely Class B follow-up PP.
- **Political-value scalars (§2.4)**: structure stated; specific scalar values (territory_value per type, province_unification_bonus magnitude) deferred to balance pass. Class B follow-up.
- **ED-055 naval-scope expansion**: would add Schoenland additional sea routes, lifting it from foreign-exempt degree-1 status to in-graph degree-2+. P1 in `improvement_avenues_2026-05-10`. Class A follow-up.
- **Askeheim healing path**: if/when Warden-led healing succeeds, settlements may emerge in T15 Askeheim; the duchy assignment for a healed Askeheim is undecided (canonically it sits between Valorsmark and Varfell geographically; political alignment of any new settlements would depend on the healing-faction). Future Class A.

---

## §6 Vetting block

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: ["Μ-α", "Μ-δ"]
  mu_secondary_preserved: ["Μ-β", "Μ-γ"]
  m_ratings:
    M-1: "○"   # PP-726 is substrate clarification, not a new pressure mechanic. Pressure remains where it was; the granularity at which it's modeled is corrected.
    M-2: "+"   # extends — geography-holds-pressure now operates at correct granularity. Per-settlement strain (PP-725) lands on actual settlements rather than mixed-granularity entries; per-province political pressure (Mandate, Cascade) aggregates from canonically-correct subunits.
    M-3: "+"   # extends — substrate vectorization corrected at the political layer. Provinces are not just labeled regions but state-machines (per §2.3 fracturing rule); settlements are not just nodes but typed siege-targets with sub-feature affordances; the duchy/province/settlement hierarchy IS substrate state at the political-administrative axis.
    M-4: "+"   # extends — institutional substrate-postures sharpen. Duchies-as-political-entities now have explicit ownership relations to provinces and territories; faction-aggregate political value (§2.4) is canonically derived from holdings rather than abstractly authored. Crown-Hafenmark-Varfell-Church-foreign distinction now load-bearing at the geography layer.
    M-5: "+"   # extends — cross-scale composition: personal-scale Knot/relational edges (PP-724) ↔ settlement-scale (PP-725) ↔ province-scale (faction Cascade) ↔ duchy-scale (Almud's overlordship + Dukes' direct control) ↔ kingdom-scale (Almund as monarch). The full cross-scale chain is now canonical at every level rather than collapsed at the duchy/province join.
    M-6: "✓"   # forced-choice mechanics preserved. The fracturing rule (§2.3) introduces a sharp consequence-of-action choice (do you push for unification at cost, or accept fracture and lose unification bonus?), but operates within existing choice architecture.
    M-7: "✓"   # KOEI ROTK / Crusader Kings precedents named in settlement_layer §Precedent and PP-724 §0 — PP-726 makes those borrowings operational at the political-hierarchy layer (CK-style duchy/county/barony) without altering their deployment in PP-723/724/725.
    M-8: "○"   # access-vertical-position-gating is upstream; PP-726 doesn't engage access mechanics at the governance layer.
    M-9: "○"   # ontological-inversion-of-clinical-phenomenology unrelated to political-hierarchy canon.
    M-10: "✓"  # environment-as-constitutive-medium preserved at correct granularity. Geography (settlements + adjacency at correct level) constitutes what's strategically actionable; the substrate gains precision, no inversion.
    M-11: "○"  # voluntary/involuntary capacity duality unrelated to political-hierarchy canon.
  m_summary: "5 + · 3 ✓ · 3 ○ · 0 − — pass per throughlines_meta §8.2 (zero violations; the three ○ ratings are appropriate scope-mismatch on patterns that don't engage with political-hierarchy canon clarification, not failures). Genuine extensions: M-2 (substrate strain at correct granularity), M-3 (political-administrative substrate vectorization), M-4 (institutional posture sharpened with explicit duchy-province-territory ownership), M-5 (full cross-scale chain canonical at every level)."
  t_touches:
    extends: ["T-23", "T-22", "T-18", "T-19", "T-25"]
    preserves: ["T-08", "T-09", "T-11", "T-14", "T-15a", "T-15b", "T-15c", "T-17", "T-20"]
    breaks: []
  q: pass
  q_robust: "Three viable player approaches per province-control conflict: (a) full conquest for unification bonus (high investment, high payoff); (b) partial control accepting fracture (lower investment, ongoing parliamentary disadvantage); (c) diplomatic/political resolution (no invasion, faction-realignment via Cascade or other mechanisms). Visible world-state change: province fracturing per §2.3 produces named sub-provinces visible in strategic UI; political value per §2.4 aggregates and modulates parliamentary action availability. Mechanic fires without player action: NPC-faction Domain Actions can produce fracturing (vassal defections), reunifications (diplomatic settlements), Governor-assignment shifts."
  q_smooth: "Methodology composes with PP-686 faction Cascade math (province-level aggregation), PP-723 territory adjacency (now correctly settlement-level via PP-726 rebuild), settlement_layer §3 governance (per-settlement Governor at correct granularity), PP-724/725 NPC-relational system (residence canon now references settlements not districts). Scale chain: kingdom→duchy→province→settlement at every level."
  q_elegant: "Core rule restatable: 'The Kingdom is three duchies of provinces of 1-3 settlements; settlements are siege-targets connected ≥2 ways; sub-features attach to their parent; provinces fracture under faction-split and unify under common alignment; political value aggregates with a unification bonus.' Second-order consequences predictable: ROTK-style officer-network defections (PP-724 B1.2 defection cascade) compose cleanly with §2.3 fracturing — a defecting Lieutenant who controls a province's only Crown territory triggers fracture into northern/southern sub-provinces."
  note: "Class A substrate canon. Resolves the granularity error that ran through PP-666/ED-710/PP-723/PP-725. Updates to substrate-canonical files only; downstream document migration (S-ID references in character_canon, migration_roster, npc_roster, etc.) deferred to lazy update as those documents are next touched. ED-710 closure properly resolved: the placeholder requested settlement_adjacency_map.yaml at correct granularity; PP-723 attempted at wrong granularity (49-edge mixed); PP-726 supersedes with correct 56-edge graph at proper settlement granularity."
```
