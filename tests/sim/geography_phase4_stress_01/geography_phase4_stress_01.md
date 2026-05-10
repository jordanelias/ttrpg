# Phase 4 Geography Stress Tests
## geography_phase4_stress_01

**Date:** 2026-05-10
**Mode:** Mode A (single-system isolation; geographic mechanics under battle conditions) + Mode D (edge cases)
**Scope:** Three scenarios queued by ED-781 (Phase 4 — depends on ED-780 Phase 3 closure):
1. Mountain Pass battle (T10/T11 Halvardshelm-area pass — geometry-constrained engagement, narrow-pass clamp emergence)
2. Open-field cavalry encounter (T2 Kronmark plains — flanking-as-position vs declaratory)
3. Coastal landing (Schoenland → T13 Oastad — amphibious sequencing, no naval mechanics per ED-780 scope deferred to ED-055)

**Source authority:** `designs/territory/valoria_geography_v30.yaml` (PP-710 ED-779 canon); `designs/territory/march_layer_v30.md` (ED-780 Phase 3 closure, commit 65b918a2); `designs/provincial/mass_battle_v30.md` (with §A.9 Phase 3 extension); `designs/territory/settlement_adjacency_v30.md`.

**Related to:** completed F-bundle and stress sweep, validating that the geography substrate produces sensible mass-battle behavior under three distinct geometric conditions.

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| GP4-L01 | t10_t11_mountain_pass_edge | T10↔T11 is the canonical mountain_pass edge | designs/territory/valoria_geography_v30.yaml | adjacency | "{from: T10, to: T11, type: mountain_pass}" |
| GP4-L02 | t11_halvardshelm_anchor | T11 Halvardshelm anchor [440, 1280]; Central Fjords | designs/territory/valoria_geography_v30.yaml | T11 | "T11:\n    name: Halvardshelm\n    faction: Varfell\n    region: Central Fjords" |
| GP4-L03 | t2_kronmark_plains | T2 Kronmark anchor [1280, 880]; Eastern Lowlands; "Italian-coded farmland" | designs/territory/valoria_geography_v30.yaml | T2 | "Crown heartland between capital and northern pass. Italian-coded farmland." |
| GP4-L04 | t13_oastad_coastal | T13 Oastad anchor [580, 2380]; Southern Fjords; gate to Askeheim | designs/territory/valoria_geography_v30.yaml | T13 | "Varfell southern gate to Askeheim (Gate 1). Calamity-adjacent." |
| GP4-L05 | t1_t16_coastal_edge | T1↔T16 is the canonical coastal edge (Crown capital ↔ Schoenland) | designs/territory/valoria_geography_v30.yaml | adjacency | "{from: T1, to: T16, type: coastal}" |
| GP4-L06 | terrain_cost_matrix | mountain_pass 2.0; plains 1.0; coast 1.0; fjord_coast 2.5; mountain 999.0 (impassable) | designs/territory/valoria_geography_v30.yaml | terrain_cost_matrix | "mountain_pass: 2.0    # embedded pass strips; gated by fortress" |
| GP4-L07 | mass_battle_a9_geographic_extension | Phase 3 (ED-780) geographic battle-terrain derivation at engagement coordinates | designs/provincial/mass_battle_v30.md | §A.9 | "**Phase 3 (ED-780) extension — Geographic battle-terrain derivation:**" |
| GP4-L08 | march_layer_t10_t11_pass_modifier | Mountain pass: attacker −1D Manoeuvre; per march_layer §4.1 edge-types table | designs/territory/march_layer_v30.md | §4.1 | "\| mountain_pass \| Highland → lowland; attacker −1D \|" |
| GP4-L09 | march_layer_winter_pass_closure | Winter (Q4-Q1) closes mountain_pass edges; path detours to lowland | designs/territory/march_layer_v30.md | §2.4 | "(c) winter weather closure on a mountain_pass edge between season Q4 and Q1 (path detours via lowland edges)" |
| GP4-L10 | naval_deferred_ed055 | Naval mechanics deferred to ED-055; coastal scenario uses geographic data only | designs/territory/march_layer_v30.md | §6 | "Phase 2 publishes the geographic data that *can support* naval (Port settlements have port metadata; sea polygons exist). Phase 3 specifies fleet types, port loading, sea zones, naval combat, weather-on-sea, Schoenland mediation, Maritime Forgetting interaction." |

---

## 2. Scenario 1 — Mountain Pass battle (T10↔T11 Halvardshelm-area pass)

### 2.1 Setup

A Crown army marching from Eastern Lowlands attempts to project force into Varfell territory via the T10↔T11 mountain_pass edge (the canonical Phase 2 edge per GP4-L01). Halvardshelm (T11, anchor [440, 1280]) is the destination.

**Forces:**
- **Attacker (Crown):** mid-tier infantry (Size 4) + Light Cavalry (Size 2). Total Size 6.
- **Defender (Varfell):** mid-tier infantry (Size 3) + Highland militia (Size 2) on home terrain. Total Size 5.

**Geographic conditions:**
- Attacker traverses mountain_pass: terrain_cost 2.0 (per GP4-L06)
- Engagement coordinates anchor at the T11-side pass exit
- Per GP4-L08: attacker takes −1D Manoeuvre Phase from pass traversal (highland → lowland descent disadvantage)

### 2.2 Phase 3 mechanics under test

**Geographic battle-terrain derivation (GP4-L07):** the engagement coordinates intersect mountain_pass terrain at the exit. Per §A.9 Phase 3 extension, the Terrain row queries `valoria_geography_v30.yaml :: terrain_polygons` at the battle hex. Mountain_pass terrain produces:
- Narrow pass: 1 engagement per side (per existing §A.9 row)
- Fibonacci impossible (per existing §A.9 row)

**Result:** attacker is forced into single-engagement file; cannot leverage Size advantage; cavalry component degrades to standard infantry per the "Forest / broken" row analog.

### 2.3 Mode A — single-mechanic isolation

Strip everything but pass-geometry effects. Assume both armies at full pool and discipline.

- Attacker effective Pool: standard − 1D (pass traversal) − 1D (single-engagement file = no Size leverage). Net −2D.
- Defender effective Pool: standard + 1D (defensive position familiarity per highland tradition).
- Net Manoeuvre Phase: attacker -2D vs defender +1D → defender +3D differential.

**Verdict:** mountain pass produces strong defensive advantage. The 3D differential is significant; the attacker's structural choice is to either commit to Manoeuvre Phase loss OR detour via T11→T12→T10 (3-edge route at terrain_cost 1+1+1.5 = 3.5 vs 2.0 direct, but no traversal penalty).

The narrow-pass-clamp emergence is canonically clean: geometry (edge type) drives the engagement constraint; this is exactly the Phase 3 design intent.

### 2.4 Mode D — edge cases

**EC-Pass-01 [P2]:** Winter (Q4-Q1) per GP4-L09: pass closure forces detour. Cavalry-majority Crown army (1.5× march budget) may fall below required budget for the lowland detour (T10→T9→T8→T11 four-edge route at ~5.0 cost). Cavalry advantage compensates partially.

**EC-Pass-02 [P3]:** Defender holds pass with Heavy Infantry "fortified at the pass exit." Per existing §A.9 walls/fortifications row: defender +3 DR, no flanking, Slow cannot advance. Combined with pass single-engagement: attacker's structural option is Pierre-de-Médicis-style multi-season siege, not direct assault.

**EC-Pass-03 [P3]:** Attacker brings Thread-Sensitive officer for Thread-Witnessed scouting (per march_layer §3.4). Reveals defender composition before commit, allowing tactical declination. PP-703 universality (Forgetting) does not apply at T10-T11 (calamity_proximity 3, no zone overlay). Recon advantage preserves attacker option to retreat.

### 2.5 Decision-shape finding

**Verdict: Phase 3 mechanics produce coherent Mountain Pass battle resolution.** Geometry (mountain_pass edge type) drives the narrow-pass-clamp emergence at the engagement hex; tactical options (detour via lowland or commit to file battle) are structural choices for the player; defensive advantage is mechanically significant but not absolute. **No spec gaps surfaced.**

**Calibration recommendation:** the 3D defender differential at the pass is substantial but consistent with historical Renaissance pass-defense outcomes (e.g., Habsburg-Swiss confrontations). If playtest reveals systematic attacker-deterrence (Crown never attempts T10→T11), reduce pass −1D to −0.5D OR add a Guts-pool conversion: attackers who pre-commit Guts (cultural courage) reduce the −1D to 0 for the first engagement only.

---

## 3. Scenario 2 — Open-field cavalry encounter (T2 Kronmark plains)

### 3.1 Setup

A Crown cavalry wing (mostly Light Cavalry, minor Mid-tier) encounters a Varfell raid force (Mid-tier infantry, no cavalry) inside T2 Kronmark.

**Forces:**
- **Crown wing:** Light Cavalry (Size 4) + Mid-tier infantry (Size 1). Total Size 5. Cavalry-majority (4/5 = 80%) → 1.5× march budget.
- **Varfell raid force:** Mid-tier infantry (Size 4). Total Size 4.

**Geographic conditions:**
- T2 polygon: [[1130, 720], [1500, 720], [1500, 1000], [1130, 1000]] — 370×280 px rectangle of plains
- Per GP4-L03: "Italian-coded farmland" — descriptively plains
- terrain_cost: 1.0 (plains baseline per GP4-L06)
- No fortifications, no rivers within polygon, no calamity zone (proximity 4 acceptable)

### 3.2 Phase 3 mechanics under test

**Geographic battle-terrain derivation (GP4-L07):** engagement coordinates anywhere within T2 polygon → plains terrain. §A.9 row "Open flat: No modifiers." Battle is unmodified; full structural use of cavalry mechanics.

**Cavalry advantage in Manoeuvre Phase:** cavalry-majority composition opens flanking opportunities. The structural test: under §A.9 plains, flanking is permitted; cavalry's Size 4 positions (engagement points) can encircle Varfell infantry's Size 4.

### 3.3 Mode A — flanking-as-position vs declaratory

**Question:** under Phase 3 geometric resolution, does flanking emerge from position (cavalry's mobility around the enemy line) or remain declaratory (announced as a Stunt / Tactic)?

**Phase 3 finding:** Phase 3 does NOT change canonical declaratory flanking (per `mass_battle §A.4` engagement-declared-by-faction). Geographic data informs **terrain modifiers and route options**, not declaration semantics. Cavalry-majority armies still announce flanking declaratively at engagement; geography does not substitute the declaration.

However: terrain restricts flanking declaration in some cases. §A.9 "Forest / broken" row blocks flanking. Phase 3's geographic-derivation extension (GP4-L07) means: if engagement coordinates fall in forest polygon (within T2 there's none, but in adjacent T9 there is), flanking is geometrically blocked. **This is the Phase 3 contribution: terrain restrictions on declaratory flanking are now data-driven.**

### 3.4 Mode A — full plains battle resolution

- Crown effective Pool: standard + 1D (cavalry flanking on plains, declared)
- Varfell effective Pool: standard (defensive line, plains)
- Net Manoeuvre: Crown +1D advantage

Cavalry mobility allows withdraw-redeploy if first engagement goes poorly. Varfell infantry, slower, cannot match.

### 3.5 Mode D — edge cases

**EC-Plains-01 [P2]:** Crown cavalry engages, takes minor losses (Size 4 → 3), retreats to redeploy. Cavalry mobility advantage: full march budget remaining (low engagement consumption + 1.5× cavalry modifier). Crown can return to engage on subsequent tick. Varfell pinned in T2; cannot easily withdraw across T9 (road, but slow infantry).

**EC-Plains-02 [P3]:** Both sides near a bridge (river crossing entry into T2 from T1 direction). Per GP4-L06 + bridge mechanics: bridge-crossing is terrain_cost 1.0 (with bridge), 1.5 (without bridge crossing penalty). If Varfell forces lack bridge access, retreat path constrained. Cavalry can intercept at the bridge bottleneck — geographic-derivation (GP4-L07) enforces the bottleneck.

**EC-Plains-03 [P3]:** Counter-recon (per march_layer §3.3): Varfell with Intel ≥ 3 in T2 (faction territory) imposes +1 Ob on Crown scouting. Crown commits with imperfect information; surprises possible. Mid-engagement intelligence reveals Varfell composition; Crown may commit or decline.

### 3.6 Decision-shape finding

**Verdict: Phase 3 mechanics produce coherent open-field cavalry resolution.** Cavalry flanking remains declaratory but geography determines whether terrain permits it. T2 plains are unrestricted; flanking is permissive. Cavalry mobility advantage (1.5× march budget) is mechanically distinct from per-engagement Pool benefits — both apply but at different scales.

**No spec gaps surfaced.** The flanking-as-position-vs-declaratory question resolves as: declaratory at engagement, geometry-restricted by terrain polygon. Phase 3 does NOT add positional-flanking; that would be a Phase 5 scope (tactical hex movement).

---

## 4. Scenario 3 — Coastal landing (Schoenland → T13 Oastad)

### 4.1 Setup

A Schoenland-based force attempts amphibious assault on T13 Oastad. Naval mechanics are deferred to ED-055 (per GP4-L10), so this scenario tests **only the geographic substrate that supports amphibious sequencing** — not naval combat resolution itself.

**Question:** under Phase 3 (ED-780) geographic data, what is the structural state of Schoenland → T13 amphibious landing **without** naval mechanics canonically defined?

**Forces:**
- **Schoenland landing force:** Mid-tier infantry (Size 3) + Marines (Size 1). Total Size 4. (Marines are placeholder pending ED-055 fleet types.)
- **Varfell defender:** Light Infantry (Size 2) + Coastal levies (Size 1). Total Size 3 in T13.

**Geographic conditions:**
- T13 Oastad polygon: [[340, 2200], [870, 2200], [870, 2500], [340, 2500]] — Southern Fjords, calamity-adjacent
- T13 description: "Varfell southern gate to Askeheim (Gate 1). Calamity-adjacent."
- T13's only canonical adjacency edges: T6↔T13 (road), T12↔T13 (road), T13↔T15 (gate to Askeheim). **No coastal edge to T13 in Phase 2 canon.**
- Schoenland (T16) has only one canonical edge: T1↔T16 (coastal, GP4-L05).

### 4.2 Critical structural finding

**No direct canonical coastal edge between T16 (Schoenland) and T13 (Oastad).** Phase 2 canon does not specify a Schoenland → T13 sea route. The amphibious landing requires either:

1. **Naval transit via undefined sea-zone routing.** Schoenland landing force boards (mechanism deferred to ED-055), traverses sea zones (no canonical sea-zone graph in Phase 2 — only port metadata and `fjord_coast` terrain), lands at T13. Phase 4 cannot stress-test what does not exist as data canon.

2. **Land transit via T1 → T6 → T13.** Schoenland force lands at T1 (Crown capital) via existing coastal edge (GP4-L05), then marches T1→T5→T6→T13 (4-edge land route, requires Crown permission per inter-faction Casus Belli check, march_layer §5.4). This is not "amphibious landing" in the sense ED-781 intended.

3. **Phase 4 stress test reveals Phase 2/3 gap.** The Phase 2 geography canon does not include sea-zone polygons, sea-zone adjacency graph, port-to-port direct routes, or amphibious-landing-coordinate specification. ED-055 (naval) must populate these; until then, Schoenland → T13 amphibious sequencing cannot be canonically resolved.

### 4.3 Mode A — what CAN be tested

Despite the substrate gap, several Phase 3 mechanics ARE testable in this scenario:

- **Geographic-derivation at landing coordinates (GP4-L07):** if a landing site is hypothesized at T13 polygon edge near (870, 2350), the terrain query returns either coast (if polygon classified as coast) or fjord_coast (if classified as broken inlet). Per terrain_cost_matrix (GP4-L06), fjord_coast = 2.5× — heavy penalty for landing forces traversing.
- **Forgetting zone interaction:** T13 calamity_proximity 1 (close to Askeheim), but no zone overlay at T13 polygon (zone is centered on T15 Askeheim per Phase 2). Landing force does NOT trigger personnel-Forgetting per PP-703 universality unless they enter T15. Calamity-adjacent designation is narrative atmosphere, not mechanical effect at T13 itself.
- **Defender position:** Varfell defender holds T13 with home-terrain familiarity; landing attacker takes the canonical "Coastal (naval) — Attacker loses Fort-level bonus (arrived by sea, no pre-battle positioning)" modifier per `settlement_adjacency §2.2`.

### 4.4 Mode D — edge cases

**EC-Coast-01 [P1]:** **No canonical sea-zone adjacency.** This is a Phase 2 spec gap exposed by Phase 4 stress testing. Defining Schoenland → T13 (or any non-T1 coastal landing) requires Phase 2 amendment OR ED-055 naval scope expansion. Recommend escalating to Jordan as a Phase 5 design item.

**EC-Coast-02 [P3]:** Land-route circumvention (option 2) is mechanically resolvable via existing Phase 3 mechanics. T16→T1 (coastal, requires permission) + T1→T5→T6→T13 (3-edge land, total terrain_cost ~3-4 + Casus Belli with Crown). This is a long campaign path, not an amphibious operation.

**EC-Coast-03 [P3]:** Schoenland's IP-75 Altonian sea route (mentioned in march_layer §6.3 stub but not body-authored) is a separate naval-mediated mechanic deferred to ED-055.

### 4.5 Decision-shape finding

**Verdict: Phase 3 mechanics are NOT sufficient to resolve Schoenland → T13 amphibious landing. The Phase 2 canon does not include sea-zone adjacency.** This is the key finding from this scenario — Phase 4 stress testing surfaces the structural gap that ED-055 is supposed to address.

**Recommendation:** ED-055 (naval) scope must include:
1. Sea-zone polygon definition (or implicit derivation from coast/fjord_coast terrain)
2. Sea-zone adjacency graph (port-to-port routes; weather-conditional closures)
3. Amphibious landing coordinate spec (which terrain types accept landing; which fortifications block)
4. Schoenland's Altonian sea route (IP-75 unlock per march_layer §6.3)

**Until ED-055 closes, Schoenland → T13 amphibious operations cannot be authored. Affected arcs include any Schoenland-pivot scenarios that assume sea projection.**

---

## 5. Cross-scenario synthesis

| Scenario | Phase 3 mechanics tested | Result | Spec gap surfaced? |
|---|---|---|---|
| 1 Mountain Pass (T10↔T11) | Geographic-derivation, terrain modifier, narrow-pass clamp, march budget consumption, winter closure | Coherent — narrow-pass clamp emerges from geometry; defender +3D differential | None (calibration recommendation only) |
| 2 Open-field cavalry (T2) | Geographic-derivation, plains terrain, declaratory flanking, cavalry mobility advantage | Coherent — flanking remains declaratory but geometry-restricted; cavalry advantage at 1.5× march budget; bridge bottleneck enforceable | None |
| 3 Coastal landing (T16→T13) | Geographic-derivation at coastal polygon, fjord_coast terrain cost, defender Fort-level loss | **Structural gap: no canonical sea-zone adjacency** (T16↔T13). ED-055 (naval) must populate sea-zone graph before amphibious operations are authorable. | **Yes — Phase 2 spec gap.** |

---

## 6. Decision-shape findings (cross-scenario)

**Recommendation: Phase 3 (ED-780) is verified for land-based mass battle resolution; Phase 4 stress testing surfaces a Phase 2 sea-zone adjacency gap that must be closed before amphibious operations can be canonically resolved.**

**Three component recommendations:**

1. **Mountain Pass battle (Scenario 1):** Phase 3 mechanics produce coherent narrow-pass-clamp emergence. The 3D defender differential is significant; calibration playtest may justify reducing pass −1D to −0.5D OR adding Guts-pool conversion.

2. **Open-field cavalry (Scenario 2):** Phase 3 mechanics produce coherent flanking-as-declaratory + geometry-restricted resolution. Cavalry-majority advantage applies at march-budget scale (1.5×) and per-engagement Pool scale (+1D plains-flanking). Both scales clean.

3. **Coastal landing (Scenario 3):** Phase 4 stress testing reveals Phase 2 substrate gap — no canonical sea-zone adjacency between non-T1 coastal territories. ED-055 (naval) must populate this. Recommend escalating as Phase 5 priority blocker for coastal scenarios.

**ED-781 closure:** Phase 4 stress test produces (a) two scenario verifications confirming Phase 3 sufficiency for land battles, and (b) one P1 spec-gap surface for naval/sea-zone canon to be addressed in ED-055.

---

## 7. Module status

| Item | Status |
|---|---|
| Canonical sources (geography YAML; march_layer ED-780 closure; mass_battle §A.9) fetched at full depth | ✓ |
| Verification ledger (10 entries) | ✓ |
| Scenario 1 (Mountain Pass T10↔T11) — Phase 3 verified | ✓ |
| Scenario 2 (Open-field cavalry T2) — Phase 3 verified | ✓ |
| Scenario 3 (Coastal landing T16→T13) — Phase 2 gap surfaced (spec deficiency) | ✓ |
| Cross-scenario synthesis | ✓ |
| Decision-shape findings (per scenario + cross-scenario) | ✓ |

**geography_phase4_stress_01 status: verified.**

**Open follow-ups (carryover):**

- `[GAP: Phase 2 sea-zone adjacency canon — basis: Scenario 3 EC-Coast-01. T16↔T13 (and any non-T1 coastal landing) cannot be canonically resolved without sea-zone polygon+adjacency definition. Escalate to ED-055 naval scope OR Phase 5 substrate amendment.]`
- `[ASSUMPTION: pass −1D Manoeuvre is a calibration choice — basis: Scenario 1 Mountain Pass test. Playtest may reveal systematic attacker-deterrence; consider half-magnitude or Guts-pool conversion.]`
- `[ASSUMPTION: T13 Oastad polygon classification (coast vs fjord_coast) — basis: Phase 2 canon does not specify the polygon's terrain assignment for amphibious-landing purposes. ED-055 should clarify.]`
