## Franchise — Per-Territory Parliamentary Weight
## Date: 2026-05-04
## Status: DRAFT — awaiting Jordan review
## Scope: New territory stat; per-territory faction influence derivation; national influence aggregation; caste-system territorial expression
## Affects: geography_v30 (territory stats), faction_behavior_v30 (Influence stat), peninsular_strain_v30 (PI interaction), settlement_layer_v30 (settlement stats), faction_politics_v30 (caste integration), ValoriaDataLibrary.gd, ValoriaSettlementLibrary.gd, Constants.gd
## Cross-references: faction_politics_v30 §3 (caste integration layer), settlement_layer_v30 §1.3 (settlement stats), parliament.md (PI), ministry.md (AP-tokens), stats_1_7_scale.md (Influence), canonical_timeline §94–100 (caste system), geography_v30 (territory table)

---

## §1 Problem

Influence is a single faction-level scalar (1–7). A faction holding six backwater provinces has the same Influence as one holding the capital. The caste system — deeply specified at the player/NPC level (faction_politics_v30 §3) — has zero territorial expression at the strategic layer. A faction controlling stigmatized southern territories and one controlling prestigious northern ones get identical parliamentary leverage.

Parliament (parliament.md) tracks PI as a pressure meter and provides Crown Policy, Hafenmark Parliamentary Manoeuvres, and Ministry stabilization. But nothing in the parliamentary model accounts for *which territories* a faction holds. The relationship between territory → political weight → national power does not exist mechanically.

---

## §2 Franchise (0–5)

**Definition:** Franchise is a per-territory stat representing the political weight that territory's delegation carries in Parliament. It is not Prosperity (economic output), not Order (local stability), not Spiritual Weight (Church institutional presence). It is the structural position of that territory within the post-war settlement's power hierarchy.

Franchise reflects:
- The territory's role in the Secession Wars coalition (higher for war-coalition leadership territories)
- Church institutional penetration (the settlement consecrated the deed-monarchy; Church-dense territories have structural legitimacy)
- Caste gradient (southern Einhir populations carry stigma; their territories' delegations are taken less seriously)
- Institutional presence (capital, Parliament, Cathedral — territories housing national institutions carry weight)

**Scale:** 0–5, integer. 0 = no parliamentary representation (foreign or uncontrolled). 5 = maximum parliamentary weight.

### §2.1 Starting Values

| T# | Territory | Controller | Franchise | Rationale |
|---|---|---|---|---|
| T1 | Valorsplatz | Crown | 5 | Capital. Parliament seat (ministry.md). War hero's base. Northern Einhir prestige apex. Houses Crown court, Ministry AP-token. |
| T2 | Kronmark | Crown | 5 | Crown heartland. Administrative core of the deed-monarchy. Secondary Ministry AP-token. |
| T9 | Himmelenger | Church | 5 | Cathedral city. Church institutional center. University. Maximum institutional prestige — the institution that consecrated the Crown sits here. |
| T8 | Gransol | Hafenmark | 4 | Hafenmark capital. Commercial center. Guild Forum. Parliamentary Committee infrastructure. Second-most-important institutional city after Valorsplatz. |
| T14 | Ehrenfeld | Crown | 4 | Military hinge. Löwenritter citadel. Crown's military prestige — the settlement that defends the peninsula's interior. Ministry AP-token. |
| T3 | Lowenskyst | Crown | 4 | Border fortress. Defends the primary Altonian invasion route (NE pass). The Secession Wars' defining front — military founding myth. |
| T5 | Feldmark | Crown | 3 | Breadbasket. Feeds the capital. Economically valued, but peripheral to political decision-making. Ministry AP-token but no institutional seat. |
| T10 | Spartfell | Hafenmark | 3 | Border castle. Defends the secondary Altonian invasion route (NW pass). Military function gives it weight above its size. |
| T17 | Halvarshelm | Hafenmark | 3 | Northern mines. Economically productive, proximity to Church infrastructure (adjacent T9, T3, T8). Northern — no caste stigma. |
| T7 | Rendstad | Hafenmark | 3 | Timber valley. Commercially productive, northern, no stigma. But no institutional presence — a working territory, not a political one. |
| T4 | Grauwald | Varfell | 2 | Highland timber. Varfell-controlled. Geographically central but ethnically southern Einhir. RM outpost (S-029) further damages institutional credibility. Calamity distance 3. |
| T12 | Sigurdshelm | Varfell | 2 | Varfell seat. Ducal capital gives it some institutional weight. But southern Einhir population + Niflhel presence (arc_register_territory) actively undermine parliamentary credibility. |
| T6 | Stillhelm | Crown | 2 | Crown-controlled but Calamity-proximate (distance 1). "Southern Crown" — viewed as instrumental frontier. Warden outpost (S-011) reinforces perception of danger zone. Not where serious political figures come from. |
| T11 | Halvardshelm | Varfell | 1 | Central fjords. Southern Einhir. Old Einhir settlement. Minimal institutional presence. The demographic the post-war settlement was built to marginalize. |
| T13 | Oastad | Varfell | 1 | Southern fjords. Calamity-proximate (distance 1). RM outpost (S-032). Maximum stigma — delegates from Oastad are barely listened to. |
| T15 | Askeheim | Uncontrolled | 0 | Calamity epicenter. No population. No parliamentary seat. Ruins and Warden outposts. |
| T16 | Schoenland | Schoenland | 0 | Foreign — Island Republic. No parliamentary representation in the Valorian Parliament. |

**Sum check:** Franchise total across represented territories (T15/T16 excluded) = 47. Crown territories sum = 23 (49%). Hafenmark = 13 (28%). Varfell = 6 (13%). Church = 5 (11%). This distribution reflects the post-war settlement's structural inequality: Crown dominates Parliament through territorial prestige, Varfell is structurally marginalized.

---

## §3 Territory Influence

**Definition:** Territory Influence is a per-faction, per-territory derived stat representing how much practical reach and leverage a faction has in that territory. It replaces the single-scalar Influence (I) stat from stats_1_7_scale.md.

### §3.1 Derivation

```
territory_influence(faction, territory) =
    controller_bonus                    [+2 if faction controls the territory]
  + infrastructure_count                [count of faction-owned settlements in the territory, 0–3]
  + npc_presence                        [+1 if faction has ≥1 active NPC stationed in the territory]
  + governor_bonus                      [+1 if faction holds Settlement Governor slot in any settlement]
```

Scale: 0–7 (matches faction stat scale). Values above 7 clamp to 7.

**Church infrastructure exception:** Church settlements (Cathedrals, parishes per settlement_layer §1.5–§1.7) count as infrastructure in *any* territory where they exist, regardless of controller. The Church's parish network is the canonical reason Church Influence was 6 — it reaches everywhere. This derivation preserves that property: Church has infrastructure_count ≥ 1 in every territory with a Cathedral or parish, even territories controlled by other factions.

### §3.2 Examples (Game Start)

| Territory | Crown TI | Church TI | Hafenmark TI | Varfell TI |
|---|---|---|---|---|
| T1 Valorsplatz | 2(ctrl)+2(palace,riverside)+1(NPC) = **5** | 0+1(cathedral)+1(NPC) = **2** | 0+0+0 = **0** | 0 |
| T9 Himmelenger | 0+0+0 = **0** | 2(ctrl)+3(cath,city,seminary) = **5** | 0+0+0 = **0** | 0 |
| T8 Gransol | 0+0+0 = **0** | 0+0+0 = **0** | 2(ctrl)+2(parliament,harbor)+1(NPC) = **5** | 0 |
| T12 Sigurdshelm | 0 | 0 | 0 | 2(ctrl)+2(keep,cove) = **4** |
| T14 Ehrenfeld | 2(ctrl)+2(citadel,market)+1(NPC) = **5** | 0 | 0 | 0 |

(Full starting table requires NPC location data from npc_roster_v30; deferred to implementation.)

---

## §4 National Influence

**Definition:** National Influence replaces the single-scalar Influence stat. It is the Franchise-weighted average of a faction's Territory Influence across the peninsula.

### §4.1 Formula

```
national_influence(faction) = clamp(
    round( Σ(territory_influence(faction, t) × t.franchise)
           / Σ(t.franchise) ),
    1, 7)
```

Summation over all territories with Franchise > 0 (excludes T15, T16).

National Influence is used wherever the old Influence stat appeared as a roll pool: Heresy Investigation, Excommunication, Diplomatic Outreach, and all other Domain Actions specifying "Influence vs Ob."

### §4.2 Recalculation Timing

National Influence recalculates at Accounting (after territory control changes, settlement changes, and NPC movement resolve). It is stable within a season. This means capturing a territory mid-season doesn't immediately boost your roll pool — the parliamentary weight adjusts at Accounting when the political reality is formalized.

### §4.3 Design Consequences

**Crown:** starts with Franchise-weighted TI advantage. Six territories, three at Franchise 5/4/4. Crown's National Influence will be high (~5) because they hold the most prestigious territories. Losing Valorsplatz (F=5) or Ehrenfeld (F=4) would crater their parliamentary position.

**Church:** holds only T9 (F=5) but has parish infrastructure everywhere. Church TI in non-controlled territories is low (1–2 from infrastructure alone) but spread across many high-Franchise territories. National Influence ~3–4 — lower than the old scalar I=6. This is intentional: the Church's reach (infrastructure) and its political weight (Franchise-weighted TI) are now separate things. Church has reach without proportional political power — historically accurate for a religious institution operating within a secular parliamentary system.

**Hafenmark:** four territories at F=4/3/3/3. Concentrated in the commercial north. National Influence ~4 — slightly above the old I=4.

**Varfell:** four territories at F=2/2/1/1. Southern, stigmatized. National Influence ~3–4 from high TI in low-Franchise territories. Structural disadvantage: even with total control of their territories, the caste system means their parliamentary voice is muted. This is the design point — the player *feels* the structural inequality. Vaynard's motivation to break the caste system becomes a concrete strategic objective: if Franchise shifts upward in Varfell territories, Varfell's National Influence rises without conquering anything.

---

## §5 Franchise Dynamics

Franchise is mostly static — structural inequality doesn't change quickly. But specific events can shift it.

### §5.1 Shift Triggers (each ±1 Franchise, clamped 0–5)

| Trigger | Direction | Territories Affected | Rationale |
|---|---|---|---|
| Faction controls territory for 4+ consecutive seasons without Accord dropping below 2 | +1 (once) | The controlled territory | Sustained stable governance legitimizes the territory's political position. A Varfell territory governed well for a year earns grudging respect. |
| Territory Accord drops to 0 (revolt) | −1 | The revolting territory | A territory in revolt loses parliamentary credibility. |
| Church Territorial Seizure (CI 60+) of a territory | −1 to seized territory | The seized territory | Theocratic takeover delegitimizes the territory's secular parliamentary position. |
| Löwenritter Coup | −1 to T14 | T14 Ehrenfeld | Military coup damages the territory's institutional credibility even though military prestige remains. |
| PI drops to ≤ 2 (Parliament non-functional) | All Franchise values frozen | All | If Parliament isn't functioning, Franchise is moot — Crown governs by decree. Values resume when PI recovers above 2. |
| Caste reform event (TBD — hooks system) | +1 to specific southern territory | Southern territories (T4, T6, T11, T13) | Breaking the caste system's structural marginalization — the concrete mechanical reward for anti-caste action. |

### §5.2 Franchise Floor

No territory with Franchise ≥ 1 can drop below 1 via shift triggers. A territory with parliamentary representation cannot lose it entirely through governance failure — only through complete depopulation or foreign conquest (which are narrative events, not shift triggers).

---

## §6 Caste Expression

This spec provides the caste system's missing territorial layer (faction_politics_v30 §3 gap noted in survey):

**Before:** Caste operates at player/NPC level only (rank advancement gates, Renown modifiers, Disposition floors, Conviction Scar risk). Strategic-layer impact = zero.

**After:** Caste operates at territorial level through Franchise. Southern Einhir territories (T4, T11, T12, T13) have low Franchise because the post-war settlement structurally devalues their populations. This devaluation cascades upward through the National Influence formula: factions holding southern territories have lower National Influence, meaning weaker roll pools for Domain Actions, meaning less ability to project power through institutional channels.

The caste system is now load-bearing at both scales:
- **Personal:** rank advancement, Renown, Disposition, Conviction (faction_politics_v30 §3 — unchanged)
- **Strategic:** Franchise → National Influence → Domain Action pools (this spec)

A player pursuing caste reform isn't just navigating personal-scale obstacles. They're fighting to change the Franchise values that determine their faction's strategic position. The personal and strategic scales reinforce each other.

---

## §7 Implementation Notes (Godot)

### §7.1 Data Model Changes

**TerritoryData.gd** — add field:
```gdscript
@export var franchise: int = 0  ## Parliamentary weight (0-5). See franchise_v30.md §2.1.
```

**ValoriaDataLibrary.gd** — seed Franchise values per §2.1 table in territory init.

**Constants.gd** — add:
```gdscript
const FRANCHISE_MAX := 5
const FRANCHISE_MIN := 0
```

### §7.2 National Influence Computation

**New function** in Meta.gd or FactionLayerV30.gd:
```gdscript
func compute_national_influence(faction_id: StringName) -> int:
    var weighted_sum := 0.0
    var franchise_sum := 0.0
    for t in setting.all_territories():
        if t.franchise <= 0: continue
        var ti := compute_territory_influence(faction_id, t)
        weighted_sum += ti * t.franchise
        franchise_sum += t.franchise
    if franchise_sum == 0.0: return 1
    return clampi(roundi(weighted_sum / franchise_sum), 1, 7)
```

### §7.3 Migration from Old Influence Stat

The old Influence scalar in FactionData becomes `base_influence` — a legacy field used only as a fallback if Territory Influence data is unavailable. All Domain Action roll pools that currently read `faction.influence` should read `compute_national_influence(faction_id)` instead. This is a mechanical change to DomainActionSystem.gd.

---

## §8 Open Items

| Item | Status | Notes |
|---|---|---|
| NPC location data for starting TI table | Deferred | Requires npc_roster_v30 location assignments |
| Church parish infrastructure per territory | Deferred | settlement_layer §1.5–§1.7 specifies framework but per-territory parish data not authored |
| Caste reform hook specification | Deferred | §5.1 references "caste reform event (TBD)" — requires Altonian hooks system design |
| Guilds/Löwenritter/RM/Niflhel TI derivation | Deferred | §3 covers 4 playable factions; non-playable factions need separate treatment |
| Church stat discrepancy | **BLOCKING** | stats_1_7_scale.md: Church L=5/PS=5/W=5 (both TTRPG and BG). VDL has L=4/PS=4/W=3. Three values wrong. Needs Jordan decision before Godot implementation. |
