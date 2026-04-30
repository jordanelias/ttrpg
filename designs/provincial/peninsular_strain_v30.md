# VALORIA BG — Peninsular Strain System v1
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance). Integrated into victory_v30.md.
## Date: 2026-04-14
## Supersedes: victory_v30.md §1 TCV table (partial — TCV revaluation), victory_v30.md §3 (faction-specific victory conditions replaced by universal condition), victory_v30.md §4 (co-victory restructured), victory_v30.md §5 (shared loss retained with modifications)
## Dependencies: geography_v30.md (territory numbering), params_board_game.md (card-hand PP-177, faction stats, Prosperity per territory, Diplomatic Token PP-517/521, Standing PP-515, Institutional Mandate PP-189), victory_v30.md §2 (PT track retained), victory_v30.md §6 (Askeheim/MS retained), victory_v30.md §7 (CI generation retained), victory_v30.md §9 (Hybrid integration retained)
## Propagation required: victory_v30.md, params_board_game.md, geography_v30.md (TCV only)

---

## Design Principle

Every faction shares the same victory condition: sovereign control of the peninsula. Asymmetry is in the tools each faction uses to get there, not in the destination. Military conquest is always available but structurally expensive — four interlocking pressures ensure that governance, institutional authority, and cultural legitimacy are faster paths than violence.

The peninsula is 35 years post-secession. The population has living memory of the independence war. Military conquest across the peninsula recreates the Altonian pattern of domination; the population resists it.

---

## §1 Territory Consolidation Values (TCV) — Revised

Himmelenger revalued to 5 (Cathedral City, 5 adjacencies, site of Cultural Uprising, focal point of CI/PT mechanics). Gransol revalued to 3 (Hafenmark's power is parliamentary/institutional, not territorial primacy).

| T# | Territory | TCV | Controller |
|----|-----------|-----|------------|
| T1 | Valorsplatz | 5 | Crown★ |
| T9 | Himmelenger | 5 | Church★ |
| T8 | Gransol | 3 | Hafenmark★ |
| T12 | Sigurdshelm | 3 | Varfell★ |
| T3 | Lowenskyst | 2 | Crown |
| T14 | Ehrenfeld | 2 | Crown |
| T10 | Spartfell | 1 | Hafenmark |
| T7 | Rendstad | 1 | Hafenmark |
| T17 | Halvarshelm | 1 | Hafenmark |
| T2 | Kronmark | 1 | Crown |
| T5 | Feldmark | 1 | Crown |
| T6 | Stillhelm | 1 | Crown |
| T13 | Oastad | 1 | Varfell |
| T11 | Halvardshelm | 1 | Varfell |
| T4 | Grauwald | 1 | Varfell |
| T15 | Askeheim | 0 | Uncontrolled |
| T16 | Schoenland | — | Not in territorial play |
| | **Total** | **31** | |

**Starting TCV:** Crown 12, Hafenmark 6, Church 5, Varfell 6.

---

## §2 Accord (Per-Territory Attribute) — NEW

Accord represents the population's acceptance of the current controller's governance. It modifies the territory's effective Prosperity.

**Range:** 0–3 (dial or marker on territory card, alongside Fort and PT).

**Effective Prosperity:** A territory's base Prosperity (from params_board_game.md territory table) is modified by Accord.

| Accord | Name | Effective Prosperity | Other Effects |
|--------|------|---------------------|---------------|
| 3 | Aligned | Base Prosperity (full) | Defender +1D in Battle. |
| 2 | Compliant | Base Prosperity (full) | Normal operations. |
| 1 | Resistant | 0 (no Prosperity contribution) | Govern Ob +1. Garrison required (≥ 1 military unit) or Accord → 0 at Accounting. |
| 0 | Revolt | Territory becomes Uncontrolled at Accounting | Garrison (if present) fights Popular Uprising: Military vs Ob 2. Win: territory held, Accord → 1. Loss: garrison retreats to adjacent friendly territory. |

**Note on Govern/Trade Ob interaction:** Govern Ob and Trade Ob use base Prosperity (unchanged by Accord). Accord 1 adds +1 Ob to Govern in that territory. This means governing resistant territory is harder (higher Ob) AND less rewarding (no Prosperity contribution).

**Accord and TCV:** A territory's TCV counts toward your total only if Accord ≥ 2. Territories at Accord 1 are nominally yours but do not contribute to sovereignty. At Accord 0 the territory is lost entirely.

### §2.1 Starting Accord

**Derivation (authoritative, per settlement_layer_v30 §1.3 REVISED):** Province Accord = floor(mean Order across all settlements in the province). Values below are derived from settlement_layer §2.1 starting Order values and are the authoritative starting state. Accord is dynamic thereafter — it recomputes whenever any settlement's Order changes. Prior direct-assignment rules (§2.3–2.4) now operate by modifying settlement Order values, which cascade upward. T15 Askeheim and T16 Schoenland retain explicit overrides (see footnotes).

| Territory | Controller | Accord | Source Settlement Orders | Rationale |
|-----------|-----------|--------|--------------------------|-----------|
| T1 Valorsplatz | Crown★ | 3 | Palace 4, Riverside 3, Cathedral 4 → floor(3.67) | Royal capital |
| T2 Kronmark | Crown | 3 | Kronmark 3, Watchtower 3 → floor(3.0) | Heartland |
| T3 Lowenskyst | Crown | 3 | Fortress 4, Garrison Town 3 → floor(3.5) | Border fortress |
| T5 Feldmark | Crown | 2 | Feldmark 3, Storehouse 2 → floor(2.5) | Breadbasket |
| T6 Stillhelm | Crown | 2 | Stillhelm 2, Watch 2 → floor(2.0) | Southern farmland |
| T14 Ehrenfeld | Crown | 3 | Citadel 4, Market 3, Barracks 4 → floor(3.67) | Military hinge |
| T8 Gransol | Hafenmark★ | 3 | Parliament 4, Harbor 3, Market 3 → floor(3.33) | Hafenmark capital |
| T7 Rendstad | Hafenmark | 2 | Rendstad 2 → floor(2.0) | Timber valley |
| T10 Spartfell | Hafenmark | 2 | Fortress 3, Village 2 → floor(2.5) | Border castle |
| T17 Halvarshelm | Hafenmark | 2 | Mines 2, Town 3 → floor(2.5) | Northern mines |
| T9 Himmelenger | Church★ | 4 | Cathedral 5, City 4, Seminary 5 → floor(4.67) | Cathedral city — highest institutional alignment |
| T12 Sigurdshelm | Varfell★ | 2 | Keep 3, Cove 2 → floor(2.5) | Varfell seat |
| T13 Oastad | Varfell | 1 | Oastad 2, Shrine 1 → floor(1.5) | Southern fjords — RM-influenced Shrine drags Order |
| T11 Halvardshelm | Varfell | 2 | Halvardshelm 2 → floor(2.0) | Central fjords |
| T4 Grauwald | Varfell | 2 | Grauwald 2, Lodge 2 → floor(2.0) | Highland territory |
| T15 Askeheim | Uncontrolled | 0 | (override) | No Accord (Uncontrolled — Ruins 1, Gate 0 would derive 0; explicit override ensures Uncontrolled status holds regardless of future Order changes) |
| T16 Schoenland | Schoenland | 0 | (override) | Not in territorial play (derived Order values exist but territory does not participate in peninsular Accord/TCV economy) |

**Cross-reference:** This table's values match `systems/data/ValoriaDataLibrary.gd` territory seed Accord values exactly (verified 17/17). Any future canonical change to settlement_layer §2.1 starting Orders must propagate to this table and to ValoriaDataLibrary in the same commit.

### §2.2 Starting Piety Track (PT) Values — NEW

| T# | Territory | Starting PT | Rationale |
|----|-----------|-------------|-----------|
| T1 | Valorsplatz | 3 | Capital, moderate piety, diverse population |
| T2 | Kronmark | 3 | Crown heartland, orthodox but not zealous |
| T3 | Lowenskyst | 3 | Border fortress, practical piety |
| T4 | Grauwald | 2 | Highland, old Einhir traditions persist |
| T5 | Feldmark | 3 | Agricultural, conventional faith |
| T6 | Stillhelm | 1 | Southern, Calamity proximity erodes orthodox faith |
| T7 | Rendstad | 3 | Timber valley, conventional |
| T8 | Gransol | 3 | Hafenmark capital, Baralta is devout but parliamentary culture moderates |
| T9 | Himmelenger | 5 | Cathedral city, spiritual centre (existing canonical value) |
| T10 | Spartfell | 3 | Border castle, practical |
| T11 | Halvardshelm | 2 | Central fjords, old Einhir ways |
| T12 | Sigurdshelm | 2 | Varfell seat, Restoration-sympathetic |
| T13 | Oastad | 1 | Southern fjords, Calamity proximity, Restoration stronghold |
| T14 | Ehrenfeld | 3 | Military hinge, institutional piety |
| T15 | Askeheim | 0 | Hard-fixed (existing canonical value) |
| T16 | Schoenland | — | Not in territorial play |
| T17 | Halvarshelm | 3 | Northern mines, conventional |

### §2.3 Accord Changes — Gaining

| Method | Accord Change | Notes |
|--------|--------------|-------|
| Govern (Consul Inward), Success | +1 | Cap: Accord 3. |
| Govern (Consul Inward), Overwhelming | +1, removes garrison requirement for 1 season if territory was Accord 1 | Decisive governance calms resistance. |
| 2 consecutive seasons: no hostile action in territory, garrison present | +1 | Passive normalisation. Cap: Accord 2 (Accord 3 requires active Govern). |
| Church Seizure, Success | Accord set to max(floor(PT/2) + 1, 2) | Guarantees ≥ 2. Political act backed by institutional authority. |
| Church Seizure, Overwhelming | Accord set to floor(PT/2) + 2, max 3 | Strong institutional mandate. |
| Dynastic Proclamation (Hafenmark), Success or Overwhelming | Accord set to 2 | Diplomatic transfer with dynastic legitimacy. |
| ~~Cultural Reformation (Varfell)~~ | STRUCK CR-STRIKE-2026-04-19 | Action dissolved. |
| Crown Treaty — diplomatic transfer | Accord set to 2 | Legitimacy inherited from prior ruler. |
| Territory transfer via Co-Victory partition | Accord set to 2 | Negotiated handover. |

### §2.4 Accord Changes — Losing

| Trigger | Accord Change | Notes |
|---------|--------------|-------|
| Military conquest (March + win Battle) | Accord set to 1 | Regardless of prior value. |
| Battle in a territory you control (you are defender) | −1 | War came to their home. |
| Church Seizure, Partial | Accord set to 1 | Contested seizure, politically messy. |
| Controller's Stability drops to ≤ 2 | −1 in all territories controlled by that faction | Destabilised faction loses trust. One-time per Stability-drop event. |
| Faction that conquered by force loses Battle elsewhere | −1 in all force-conquered territories held by that faction | Military weakness emboldens resistance. |
| Peninsular Strain threshold effects | See §4 | Global war-weariness erosion. |

### §2.4b Accord vs Order — Scale Distinction (ED-626)

**Accord** (0–3) is a *province-level* attribute governing territorial TCV contribution and population acceptance of the controlling faction's governance. It is tracked per territory.

**Order** (0–5) is a *settlement-level* attribute governing local stability within a specific settlement inside a territory. It is tracked per settlement, not per territory.

They are independent: a province at Accord 2 (Compliant governance) may contain a settlement at Order 1 (simmering unrest). Peninsular Strain threshold effects (§4.3) affect province-level Accord. Settlement Order is governed by: garrison presence (+1/season), Govern success (+1 from Success, +2 from Overwhelming in that settlement), battle at settlement (−2 immediately), sustained hostile occupation (−1/season), Church Heresy Investigation at settlement level (Order −1 for non-Church-aligned population in that settlement only).

**Both can reach 0 simultaneously.** When Province Accord 0 and Settlement Order 0 both trigger in the same territory at the same Accounting, resolve in this sequence: **(1) Settlement Order 0 first** — garrison fights Popular Uprising (Military vs Ob 2). Win: territory held, Accord → 1. **(2) Province Accord 0 consequence second** — if garrison won the Uprising: territory is contested but held (Accord at 1 from the garrison win). If garrison lost the Uprising: the garrison has retreated; the territory becomes Uncontrolled per the Accord 0 rule. This ordering means a garrison victory in a Popular Uprising can prevent the Accord 0 Uncontrolled consequence in the same Accounting. (ED-632)

### §2.5 Accord — Restoration Movement Exception

RM does not use Accord. RM controls T9 (if taken via Cultural Uprising) through cultural presence, not governance. RM-held T9 control is maintained while RM has ≥ 3 Presence markers in T9 AND PT ≤ 1 (existing rule from victory_v30.md §3.5). RM has no Stability, Mandate, or Military — Accord triggers do not apply.

### §2.6 Accord — Löwenritter Adaptation

Löwenritter uses Accord but gains access to **Martial Governance**: a Govern variant using Military as pool instead of Influence. Accord +1 on Success, same as standard Govern. Ob = floor(Prosperity/2) + 2 (harder than civil governance). Löwenritter cannot exceed Accord 2 via Martial Governance (cap); reaching Accord 3 requires standard Govern with Influence pool.

### §2.6b Martial Law at Settlement Level (Throughline T5)

When the Löwenritter Coup fires, all Crown-controlled settlements enter Martial Law:

| Settlement Type | Under Martial Law |
|----------------|-------------------|
| Fortress | No change. Löwenritter governance is natural. |
| Seat | Military governor. Govern pool: Military. Govern Ob +1. Order −1 at onset. |
| City | Military governor. Prosperity −1 at onset. Guild management revoked unless explicitly re-granted (Influence, Ob 2). |
| Cathedral | Church management NOT revoked (Martial Honour respects Church authority). |
| Town | Military patrol. Govern Ob +2. |
| Port | Trade continues under supervision. Prosperity maintained if Guilds retained. |

**Governance cap under Martial Law:** Prosperity cannot exceed Coup-onset value. Order cannot exceed 2. Löwenritter NEEDS civilian partners (Ministry, Guilds, player-governors) to govern effectively. Ehrenwall's Outreach to capable players intensifies during Martial Law.

### §2.7 Personal-Scale Accord Pathways (NEW — Hybrid/TTRPG)

The faction-level Accord changes in §2.3–2.4 operate at BG scale. In Hybrid and TTRPG modes, the player's personal actions can also affect Accord via Domain Echo (scale_transitions_v30 §5.5). This section expands the available pathways.

| Player Action | Accord Effect | Condition | Domain Echo Route |
|--------------|--------------|-----------|------------------|
| Social fieldwork: reach Disposition +3 with 2+ local NPCs in one settlement in one season | Settlement Order +1 (queued to Accounting) | Player spent ≥ 2 scene actions on social fieldwork in the settlement | §5.5: PC publicly governs/administers |
| Investigation: resolve a local concern affecting a settlement's population (Evidence Track threshold reached) | Settlement Order +1 (queued to Accounting) | Finding is publicly shared in or about the settlement | §5.5: PC publicly governs — the investigation's resolution IS governance |
| Community Organizing in a settlement | Settlement Order +1 (queued to Accounting) | Settlement in territory with PT ≤ 2 AND Community Organizing Success | §5.5: PC publicly administers — the practice IS cultural governance |
| Public violence: player initiates combat in settlement (public, 3+ witnesses) | Settlement Order −1 (immediate) | Combat Exposure ≥ 3 (public) | §5.5: PC destabilises settlement governance |
| Assassination or killing of named NPC residing in settlement | Settlement Order −1 (immediate) | Dead NPC had Disposition ≥ +1 with local settlement NPCs | §5.5: PC destabilises — violence against a known figure |
| Player publicly defies controlling authority in a settlement | Settlement Order −1 (immediate) | Player's action is witnessed (Exposure ≥ Noticed) and contradicts the controlling faction's or governor's institutional position | §5.5: PC destabilises |

**Cap:** ±1 Order per settlement per season from personal-scale actions. Province Accord is derived at Accounting: floor(mean(settlement Order values)), capped at 3. Personal-scale Order changes and governor governance actions stack normally — they target different settlements or stack within the same settlement (cap ±1 per source per settlement per season).

### §2.8 Accord Environmental Legibility (NEW — presentation layer)

Accord is the game's victory condition foundation. It should be experienceable, not just trackable.

**TTRPG/Hybrid:** When the player enters or remains in a settlement, the GM describes the environment using the following cues. Different settlements within the same province may have different atmospheres — a Cathedral at Order 4 feels different from a Town at Order 1.

| Accord | Environmental Description |
|--------|--------------------------|
| 3 (Aligned) | Markets are busy and well-stocked. People greet the patrol warmly. Public buildings are maintained. Children play in the square. The faction's banners fly without graffiti. |
| 2 (Compliant) | Life proceeds normally. People are civil but reserved with officials. Trade functions. No visible unrest, but no visible enthusiasm. The status quo is tolerated. |
| 1 (Resistant) | Shops close early. People avoid the patrol's gaze. Graffiti appears on faction buildings overnight and is scrubbed by morning. A garrison is visible and the population keeps its distance. Whispered conversations stop when strangers approach. |
| 0 (Revolt) | A barricade blocks the main road. Someone has painted slogans on the faction hall. The garrison is confined to the fortress. Armed civilians watch from rooftops. The market has moved to an unofficial location the patrol cannot reach. |

**Videogame:** Environmental art, NPC ambient dialogue, and crowd behavior shift based on Accord value. At Accord 3: warm lighting, populated streets, friendly greetings. At Accord 0: dark palette, empty streets, hostile stares, barricades as navigation obstacles.

**Accord change visibility:** When Accord changes in a territory where the player is present, the GM or game narrates the transition: "Over the past weeks, you've noticed the market closing earlier. The baker who used to greet you by name now serves you in silence." This is not a stat notification — it is world texture.


### §2.5 Settlement Targeting Specification (AUD-SET-02 resolution)

Province Accord = floor(mean(settlement Order)) per settlement_layer_v30 §1.3. Existing Accord change rules operate as follows:

**Category A — Province-Level Set (Accord set to N):** Macro-political events that reset the entire province's relationship with its population. Implementation: set ALL settlement Order values in the province to N. Applies to: military conquest (§2.4), Church Seizure (§3.4), Dynastic Proclamation (§3.5), Crown Treaty, Co-Victory partition, diplomatic transfers (faction_layer §2.1), Occupation transfers (faction_layer §5). (CR-STRIKE-2026-04-19: Cultural Reformation removed from list.)

**Category B — Targeted ±N (Accord ±N → Order ±N in specific settlement):**

| Rule | Target Settlement | Rationale |
|------|------------------|-----------|
| Govern Success/OW (§2.3) | Seat settlement of province | Governance operates from seat of power |
| Passive normalisation (§2.3) | All settlements in province equally | Stability affects entire province |
| Strain Fracture (§2.6 roll 5-6) | Lowest-Order settlement in province | Instability breaks at weakest point |
| Strain Crisis (§2.6 roll 7-8) | All non-capital settlements −1 Order | Capital settlements insulated by institutional presence |
| Strain Collapse (§2.6 roll 9-10) | All settlements Order capped at 2 | Province-wide crisis ceiling |
| Dynastic Proc Partial (§3.5) | Seat settlement | Political rejection radiates from seat |
| Institutional consolidation (faction_layer §4) | Lowest-Order settlement | Investment flows to weakest link |
| Parliamentary action (faction_layer §9) | All settlements −1 Order | Economic sanctions affect entire province |
| Battle in territory (mass_battle Part E) | Settlement nearest battle site; if no identifiable settlement, Seat | Military action damages local governance |
| PC public governance (scale_transitions §5.5) | Settlement where scene occurred | Personal-scale actions are location-specific |
| PC destabilisation (scale_transitions §5.5) | Settlement where scene occurred | Personal-scale actions are location-specific |
| PC territorial violence (scale_transitions §5.5) | Settlement where violence occurred | Violence damages local Order |
| Löwenritter Martial Governance (§2.8) | Seat settlement | Military governance operates from seat |

**Province Accord recalculation:** After any settlement Order change, Province Accord recalculates at next Accounting: floor(mean(all settlement Order values in province)).

**Cap:** ±1 Order per settlement per season from personal-scale actions (per §2.4b Accord vs Order Scale Distinction). Province-level Domain Actions (Category A and B Govern/Strain) are not subject to this cap.


---

## §3 Battle Consequences — NEW

Automatic consequences firing when Battle is resolved on Valorian soil. Not optional. Not faction-specific.

### §3.1 Substrate Fracture (Pressure 1)

Each Battle resolved on Valorian soil: **MS −1.**

| Battle type | MS cost | Rationale |
|------------|---------|-----------|
| Standard Battle (Legionary contested entry) | −1 | Mass violence degrades the Rendering. |
| Mass Battle (Campaign/War scale per mass_battle_v30.md §A.3) | −2 | Larger scale violence, greater substrate damage. |
| Siege (Fort ≥ 2 defended) | −1 | Concentrated but geographically contained. |
| Church Seizure requiring Battle (garrisoned territory) | −1 | The Battle component triggers MS cost; Seizure itself does not. |
| Popular Uprising (Accord 0 → Revolt) | −1 | Violence is violence; the substrate does not distinguish. |
| Altonian Vanguard Battle | −1 | Foreign invasion also damages the substrate. |
| Covert action (Tribune Investigate, Spy) | 0 | Not mass-violence events. |
| Church Seizure, ungarrisoned territory | 0 | Political act, no violence. |

### §3.2 Vulnerability Signal (Pressure 2)

**Held-instability trigger (ED-743 — supersedes ED-623 battle-occurrence trigger).** Altonia gains intelligence from *visible administrative failure*, not from inter-faction battles per se. The signal is the inability to govern conquered or contested ground. Pax Romana stabilized after conquest; the prior battle-occurrence trigger inverted that logic, taxing the act of conquest rather than the failure to consolidate.

| Trigger | IP Change |
|---------|-----------|
| At each Accounting, count territories at Accord ≤ 1 controlled by playable factions. 0–1 territories → IP +0; 2–3 → IP +1; 4–5 → IP +2; 6+ → IP +3. | Up to +3/season |
| CI ≥ 60 sustained (Church dominance signal) | +2/season while sustained |
| Faction eliminated (Stability 0) | +2 (one-time at moment of collapse) |

The Accord-based trigger means battle-occurrence does not directly advance IP. What advances IP is the *sustained inability* to bring conquered or contested territory to Compliant governance (Accord ≥ 2). A faction that fights short, decisive wars and rapidly stabilizes generates *less* IP than one that fights inconclusively or holds territory at Resistant Accord for extended periods. Battles still produce Accord-1 conquered territories at the moment of conquest (mass_battle §E.1) — the IP advance fires the season *after*, when those territories remain at Accord ≤ 1 across Accountings.

Battles involving NPC factions (Altonian Vanguard, Popular Uprising, Löwenritter coup) do NOT trigger IP advancement directly — Altonia does not gain intelligence from its own operations, and internal unrest is a different signal from inter-faction civil war. However, NPC-faction battles that produce Accord ≤ 1 territories DO contribute to the count above — the inability to stabilize is the same signal regardless of who caused the destabilization.

**IP and Strain may advance from the same world-state** (e.g., a conquered Accord-1 territory contributes to both counts) but through separate aggregation rules — see §4.4.

[EDITORIAL: ED-743 — Vulnerability Signal mechanism revised from battle-occurrence to held-instability. ED-623 superseded. Source: 2026-04-24 audit conversation P1-1 — prior mechanism inverted historical Pax Romana logic (Pax stabilizes after conquest; the prior spec taxed the act of conquest rather than the failure to consolidate). Combination of fix-options (1)+(3) per audit conversation: held-instability advance + Treaty-pair decay.]

---

## §4 Peninsular Strain Counter — NEW

Global track, range 0–10. Starts at 0. Public (visible counter on board).

### §4.1 Advancing Strain

**Held-instability trigger (ED-743).** Strain advances from instability of held ground, not from battle-occurrence. Conquest itself does not advance Strain; *failure to consolidate conquered or contested territory* does.

| Trigger | Strain Change |
|---------|--------------|
| At each Accounting, per territory at Accord ≤ 1 controlled by any playable faction | +1 per territory, capped at +3/season from this source |
| Playable faction eliminated (Stability 0) | +2 (one-time at moment of collapse) |
| Territory Revolt (Accord 0 → Uncontrolled at Accounting) | +1 per Revolt event |

The +3/season cap from territory-instability prevents runaway escalation — a peninsula with 6+ Accord ≤ 1 territories advances Strain at the cap, not unbounded. Faction elimination and Revolt remain uncapped (discrete events, not ongoing conditions).

### §4.2 Reducing Strain

Strain decay is per-Accounting and decoupled from peninsula-wide peace (the prior coupling produced the multi-faction lock where one faction's war prevented Strain decay for everyone).

| Trigger | Strain Change |
|---------|--------------|
| At each Accounting, if no Strain advanced from §4.1 territory-instability this season (all controlled territories at Accord ≥ 2) | −1 (min 0) |
| Per active Treaty pair (Truce, Peace, Alliance, Capitulation, Tributary per faction_layer §3.1) at Accounting | −1 per Treaty pair, capped at −2/season from this source |
| Public diplomatic resolution (Crown Treaty newly formed, Open Pledge honoured, Co-Victory declared) | −1 (max one from this source per season) |

**Treaty-binding is a Strain-budgeting tool.** Two factions in active Treaty produce Strain decay even while a third faction is at war — the Roman Pax expressed mechanically. Example: peninsula with 3 Treaty pairs (Crown-Hafenmark, Crown-Varfell, Hafenmark-Varfell) and active Crown-Church war. Crown territories at Accord ≤ 1 advance Strain per §4.1, but Treaty pairs deliver −2/season (cap) — net Strain hold or decay despite active warfare. Compare to a peninsula with no Treaty structure, where the same Crown-Church war + Crown territory destabilization produces unmitigated Strain advance.

### §4.3 Strain Threshold Effects

| Strain | Name | Effect |
|--------|------|--------|
| 0–2 | Peace | No effect. |
| 3–4 | Tension | All factions: Legitimacy −25 at Accounting (derived_stats_v1). |
| 5–6 | Fracture | All factions: Accord −1 in one territory (lowest-Accord first, controller's choice among ties). |
| 7–8 | Crisis | All factions: Accord −1 in ALL non-capital territories. Mandate check Ob 2 at Accounting. |
| 9–10 | Collapse | Non-capital territories: Accord cap at 2. Mandate check Ob 3. MS −1/season additional. |

**Löwenritter Strain exemption:** Löwenritter emergence (coup) adds Strain +1 (not +2 — the coup is a succession event, not faction elimination). Battles in the first 2 seasons after Löwenritter activation do not advance Strain (the population expects military governance during succession crisis). After 2 seasons: normal Strain rules apply.

### §4.4 Strain and IP — Shared Signal, Independent Aggregation

Both tracks now advance from the same world-state signal (Accord ≤ 1 territories at Accounting) but through different aggregation rules:
- **Strain** (§4.1): +1 per territory, cap +3/season from this source. Faction elim +2, Revolt +1 add separately.
- **IP** (§3.2): stepwise threshold (0-1 → +0; 2-3 → +1; 4-5 → +2; 6+ → +3) — single contribution per Accounting from this source. CI ≥ 60 adds +2/season independently. Faction elim +2 once.
- **No direct feed.** Strain effects at Fracture/Crisis/Collapse do NOT add IP. IP does not feed back into Strain.

Both may rise together in a campaign with sustained governance failure. They share the underlying world-state but aggregate it differently (Strain accumulates linearly across territories up to cap; IP uses threshold steps).

[EDITORIAL: ED-743 — §4.4 updated to reflect shared trigger with independent aggregation. Prior framing ("no cross-feeding") preserved as principle but mechanism-level explanation added.]

---

## §5 Faction Toolkits — Non-Military Territory Acquisition

Each faction has a non-military domain action for acquiring territory that produces Accord ≥ 2. These are categorically better than military conquest (Accord 1) for legitimacy purposes and do not trigger MS/IP costs (unless Battle is required for garrisoned territories).

### §5.1 Crown — Formal Crown Treaty (Existing)

See victory_v30.md §3.1 for full Treaty mechanics (PP-512/513/514/523).

**Card type:** Senator Outward (Crown only).
**Ob:** floor(target Mandate / 2) + 1, min 1.
**Pool:** Influence.

Crown Treaty subordinates rival factions diplomatically. Treaty-bound factions count toward Crown's effective hegemony for the universal victory condition. Territories held by Treaty-bound factions are counted as Crown-controlled for sovereignty purposes.

**Accord on diplomatic transfer:** If a Treaty-bound faction cedes a territory to Crown as part of Treaty terms (negotiated between players or via NPC consent rules), that territory starts at Accord 2.

**Defensive interaction with Institutional Mandate (PP-189):** Target faction may Appease (Mandate −1, Treaty cancelled) if Mandate ≥ 4. This is the existing defensive mechanic.

### §5.2 Church — Graduated Seizure (Existing, Accord Formula Revised)

See victory_v30.md §3.2 for full Seizure mechanics (PP-494).

**Card type:** Special/Unique Power (Priority 6).
**Pool:** Influence + floor(CI / 15).
**Ob:** 7 − PT.
**Prerequisites:** Church Mandate ≥ 4. Prominence (Church Mandate > controlling faction Mandate). **Uncontrolled exclusion (ED-704):** Seizure cannot target Uncontrolled territories (no controlling faction = no Mandate to exceed). Uncontrolled territories must first be brought under Mandate-bearing control via Pastoral Assumption (settlement_layer §1.7) for Church-routed restoration, or Conquest by another faction, or RM Founding (victory_v30 §8). Only then can subsequent Seizure target the territory.

**Revised Accord on Seizure:**

| Degree | Accord | Formula |
|--------|--------|---------|
| Overwhelming | floor(PT/2) + 2, max 3 | High institutional authority. PT 5 → Accord 3. PT 3 → Accord 3. PT 1 → Accord 2. |
| Success | max(floor(PT/2) + 1, 2) | Guaranteed ≥ 2. PT 5 → Accord 3. PT 3 → Accord 2. PT 1 → Accord 2. |
| Partial | 1 | Politically messy. Contested seizure fails to establish authority. |
| Failure | N/A | Seizure fails. Discipline −20 (derived_stats_v1). |

**Defensive interaction:** Controlling faction gains Casus Belli on every seizure attempt (PP-510, existing rule). Institutional Mandate (PP-189) applies — controlling faction may Appease to cancel Seizure before roll.

**Fort interaction:** Unchanged (PP-506). Fort does NOT modify Seizure Ob. If garrisoned: Battle required first (existing rule). The Battle triggers MS −1 per §3.1.

### §5.3 Hafenmark — Dynastic Proclamation — NEW

Baralta's divine-right claim. "Faith is not mediated — it is lived. Anyone who is truly faithful can hear Solmund. Anyone who cannot should not rule."

**Card type:** Diplomat (Hafenmark faction card). Once per season.
**Pool:** Influence.
**Ob:** floor(target faction Stability / 2) + 1. Modifiers: if target territory PT ≤ 1: +1 Ob (Restoration-leaning population resists divine-right authority). If Hafenmark has active Diplomatic Token on target faction mat: −1 Ob (existing diplomatic leverage).
**Prerequisites:** Hafenmark Mandate ≥ 4 AND Hafenmark Mandate > target territory controlling faction's Mandate. Target territory must be adjacent to Hafenmark-controlled territory.

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory control transfers. Accord set to 2. Target faction Mandate −1. Hafenmark Mandate +1 (momentum of divine right). No Casus Belli (legitimate succession claim). +1 Standing (PP-515: the claim was publicly made and upheld). |
| Success | Territory control transfers. Accord set to 2. Target faction Mandate −1. |
| Partial | Territory does not transfer. Hafenmark gains Casus Belli vs target (rejected claim = justification for force). Target territory Accord −1 (population destabilised by competing claims). |
| Failure | Hafenmark Discipline −20 (overreach, derived_stats_v1). No Casus Belli. |

**Diplomatic Token interaction (PP-517/521):** If Hafenmark has Diplomatic Token on target faction AND uses Proclamation: Token provides −1 Ob (above). On Overwhelming Proclamation: Token is NOT consumed (unlike military conflict, which removes Tokens). On Partial/Failure: Token remains. Token is consumed only if Hafenmark subsequently uses military force against that faction (existing PP-517 rule).

**Standing interaction (PP-515):** Proclamation may be declared as an Open Pledge in Phase 1 ("I will assert my divine right over [territory] this season"). Honour: +1 Standing. Breach (failing to play Diplomat card for Proclamation): Cohesion −20 + Reputation −15 (derived_stats_v1) + Casus Belli per PP-515 rules.

**Defensive interaction:** Target faction may invoke Institutional Mandate (PP-189) if Mandate ≥ 4 (Appease: Mandate −1, Proclamation cancelled). Target faction may also contest via Parliamentary Session (Hafenmark's Proclamation is a constitutional claim — Parliament has standing to adjudicate). If Parliamentary Session vote opposes Proclamation: +1 Ob to Proclamation this season.

**Why Diplomat card, not Senator:** Hafenmark has 1× Senator and 1× Diplomat. Diplomat is Hafenmark's unique card. Proclamation is Hafenmark's unique acquisition tool. Using Diplomat preserves Senator for Diplomacy and Parliamentary Manoeuvre. The Diplomat card's existing function (place Diplomatic Tokens) creates a natural two-phase strategy: first deploy Diplomatic Tokens (build leverage), then Proclaim (use leverage for territorial acquisition).

### §5.4 Varfell — Cultural Reformation — STRUCK CR-STRIKE-2026-04-19

Cultural Reformation dissolved. Incompatible with Vaynard's identity as military conqueror (Reinhardt von Lohengramm parallel). Vaynard does not convert populations ideologically; Varfell expansion is purely military. Tribune intel operations remain (reveals enemy stats for target selection). Thread operations remain character-scale only (threadwork_v30), not BG-layer bonuses.

See canon/supersession_register.yaml entry CR-STRIKE-2026-04-19. PP-650 superseded.

---

## §6 Universal Victory Condition — Peninsular Sovereignty

All factions share the same victory condition. Available in all modes (BG, Hybrid).

### §6.1 Peninsular Sovereignty (Primary)

All conditions simultaneous at Accounting, held for 2 consecutive Accountings:

| Condition | Threshold |
|-----------|-----------|
| Territory control | All 15 playable territories (T1–T14, T17) — directly or via effective hegemony |
| Accord | ≥ 2 in all directly-controlled territories |
| Peninsular Strain | ≤ 6 (peninsula not in Crisis) |

**Effective hegemony** counts rival-held territories toward sovereignty if the rival faction is:
- Treaty-bound (Crown Treaty or equivalent bilateral agreement), OR
- Submitted (Stability 0, formal submission per ED-318), OR
- Institutionally dominated (rival Mandate ≤ 1 AND hegemon Mandate ≥ 5)

Territories held by Treaty-bound or Submitted factions do not need to meet Accord ≥ 2 for the hegemon — the legitimacy question belongs to the subordinate.

### §6.2 Faction-Specific Victory Conditions — STRUCK

**There are no faction-specific victory conditions.** The only faction victory is Peninsular Sovereignty (§6.1). All existing faction-specific condition sets are reframed as descriptions of each faction's asymmetric approach to territorial acquisition in victory_v30.md §3. They describe HOW each faction pursues peninsular sovereignty, not WHEN a faction has won.

### §6.3 Co-Victory: Peninsular Partition

Available when playing with 2+ human players. Two factions agree to divide the peninsula.

All conditions simultaneous at Accounting, held for 2 consecutive Accountings:

| Condition | Threshold |
|-----------|-----------|
| Collective territory control | Both factions collectively control all 15 playable territories — directly or via effective hegemony over remaining factions |
| Individual minimum | Each faction controls territories with TCV ≥ 10 |
| Accord | ≥ 2 in all territories controlled by each faction |
| Non-aggression | No Battle between the two factions in preceding 4 seasons |
| Peninsular Strain | ≤ 6 |
| Institutional standing | Both factions Mandate ≥ 3 |

**Partition declaration:** Both players formally declare Partition at the same Accounting.

**Incompatible pairings:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM (structurally contradictory programs).

Existing co-victory pairings from victory_v30.md §4 are retained as alternate co-victories with their existing (lower) thresholds, alongside the new Partition option.

### §6.4 World-State Transitions

**No shared loss. No fade to black.**

| Condition | Trigger | Transition |
|-----------|---------|------------|
| Post-Calamity Era | MS = 0 at Accounting | Substrate tears. Faction acquisition suspended 3 seasons. Mending doubled. Recovery: MS to 20 within 10 seasons. |
| Occupation Era | IP ≥ 100 AND AER ≤ 1 at Accounting | Altonian Governorate activates. Faction actions +2 Ob in occupied territories. Recovery: IP below 60. |
| Anarchy Era | All factions Stability 0 | Direct governance via personal action. Founded Organization faction formation available. Recovery: Parliament quorum restored. |

The only campaign terminal: Second Calamity after 10 seasons sustained at MS ≤ 5.

---

## §7 Accounting Integration

New steps to add to Phase 5 Seasonal Accounting (params_board_game.md):

Insert after existing Step 4 (Clock advances):

**Step 4c — Accord checks:**
1. Each territory at Accord 1: if no garrison present (no military unit from controlling faction), Accord → 0.
2. Each territory at Accord 0: Revolt fires. Garrison fights Popular Uprising (Military vs Ob 2) or retreats. Territory becomes Uncontrolled. Peninsular Strain +1.
3. Passive normalisation: each territory with garrison present AND no hostile action this season for 2 consecutive seasons: Accord +1 (cap Accord 2).

**Step 4d — Peninsular Strain update:**
1. Per §4.2: if no Strain advanced from territory-instability this season (all controlled territories at Accord ≥ 2): Strain −1 (min 0). *(Updated to align with §4.2; prior "no battles AND no Revolts" condition was superseded by territory-count mechanism.)*
2. If diplomatic resolution occurred (Treaty, Pledge honoured): Strain −1 (max one from this source).
3. Apply Strain threshold effects per §4.3.

**Step 4e — Battle consequence accounting (ED-743):**
1. ~~If Battle between playable factions occurred this season: IP +2~~ STRUCK by ED-743 (2026-04-29). Battle-occurrence no longer directly advances IP. IP advances from Accord-based territory-count thresholds at Accounting (§3.2). See mass_battle_v30 §E.2.
2. MS adjustments from battles already applied during Phase 4 resolution (immediate, not deferred to Accounting).

Modify existing Step 12 (Victory condition check): Check universal Peninsular Sovereignty condition (§6.1) alongside existing faction-specific conditions (§6.2). Either type of victory is valid. Co-Victory (§6.3) checked simultaneously.

---

## §7b Occupation / Accord Harmonization (faction_layer_v30.md integration)

Occupation (faction_layer_v30.md §2) and Accord (this document §2) address different moments in the territorial lifecycle.

**During Occupation (territory controlled by Faction B, occupied by Faction A):**
- Accord tracks Faction B's (the displaced controller's) relationship with the population. Accord may drop due to inability to defend (Stability drop from faction_layer §1.2 Trigger 1).
- The occupying faction has no Accord in this territory — they don't control it yet. They bear garrison costs per faction_layer §2.3.
- TCV counts as 0 for both parties during Occupation (faction_layer §0 OCCUPATION_TCV_UNSPECIFIED).

**At Control Transfer (3-season occupation conversion, Overwhelming military victory, or Treaty cession):**
- Accord resets based on method of transfer:

| Transfer method | Accord at transfer | Source |
|-----------------|-------------------|--------|
| Military occupation (3-season conversion) | 1 (Resistant) | §2.4 this document |
| Military Overwhelming (immediate transfer) | 1 (Resistant) | §2.4 this document |
| Show of Force (military demonstration) | 2 (Compliant) | military_layer_v30 §1.10 |
| Siege Parley (negotiated surrender) | 2 (Compliant) | military_layer_v30 §1.9c |
| Treaty cession (negotiated) | 2 (Compliant) | §2.3 this document |
| Pastoral Assumption (Church vacuum fill) | 2 (Compliant) | settlement_layer_v30 §1.7 |
| Church Seizure, PT < 3 (imposed against cultural grain) | 1 (Resistant) | §5.2, revised |
| Church Seizure, PT ≥ 3 (Success) | max(floor(PT/2)+1, 2) | §5.2 this document |
| Church Seizure, PT ≥ 3 (Overwhelming) | floor(PT/2)+2, max 3 | §5.2 this document |
| Dynastic Proclamation (Success/OW) | 2 (Compliant) | §5.3 this document |
| ~~Cultural Reformation~~ | STRUCK CR-STRIKE-2026-04-19 | Action dissolved. |
| RM Community Organizing (post-Founding) | 3 (Aligned) | victory_v30 §8 — population self-organized into RM governance |

**Historical grounding (historical_precedents_warfare §5.3):** Accord varies by acquisition method because the *type* of legitimacy determines population acceptance. Military conquest imposes through force (Weber: no legitimacy basis → Resistant). Show of Force / Parley / Treaty involve negotiation (rational acceptance → Compliant). RM represents genuine population transformation (identity shift → Aligned). Church Seizure depends on whether the population was already religiously aligned (PT ≥ 3) or not (PT < 3). (CR-STRIKE-2026-04-19: Cultural Reformation removed from list.)

**Note:** ~~Cultural Reformation Accord tier~~ STRUCK CR-STRIKE-2026-04-19.

[EDITORIAL: ED-692 — Accord by acquisition method revision. Source: historical_precedents_warfare.md §5.3.]

**Recapture:** The displaced faction may attempt military_advance at -1 Ob (home territory advantage per faction_layer §2.2). If successful, territory returns to their control. Accord resets to 2 (population welcomes return of familiar governance), not the original pre-occupation value.

**Key principle:** Occupation is the transition phase. Accord only matters for the controlling faction. During Occupation, the territory is contested. Accord kicks in when the question of "who governs" is settled.

---

## §7c CI 0-100 Integration (tc_political_redesign_v30.md)

This document's Church Seizure pool formula (Influence + floor(CI/15)) is compatible with CI running to 100 (no freeze at 75). At CI 100: pool bonus = floor(100/15) = 6 (vs 5 at old CI 75 ceiling). The Seizure Ob formula (7 - PT) is unchanged.

CI milestone effects (tc_political_redesign_v30.md §2.1) interact with Seizure availability:
- CI >= 40: Church Seizure available (replaces old CI >= 75 gate)
- CI 80: Seizure Ob -1 globally (stacks with 7 - PT formula)
- CI 100: Theocracy Unification Attempt (Seizure on any territory, not just Prominent)

Accord on Seizure follows this document §5.2 regardless of CI milestone. Seizure is always a political act; Accord reflects institutional legitimacy, not CI level.

---

## §8 Open Items

<!-- Updated 2026-04-19 PP-668 — PP-667 resolutions propagated. See designs/audit/gap_resolution_2026-04-19.md §2.3 -->

| # | Item | Status (PP-667) |
|---|------|------------------|
| 1 | Starting PT values (§2.2): requires user review. | **CONFIRMED** — approved per Jordan 2026-04-18 (PP-652 applied). |
| 2 | Hafenmark Parliamentary Sovereignty struck, Dynastic Assertion primary. | **CONFIRMED** — peninsular_strain §6.2 STRUCK; victory_v30 §3.3 Dynastic Assertion primary. |
| 3 | Church Counter-Reformation defensive action (§5.4). | **SUPERSEDED** by CR-STRIKE (PP-663). Cultural Reformation struck; Counter-Reformation no longer needed. |
| 4 | Varfell Colonist card availability. | **CONFIRMED** (params_board_game.md). Retained post-CR-STRIKE for Tribune Outward / territorial intel use. |
| 5 | Accord physical component. | **N/A** — videogame-only project scope. BG physical excluded. |
| 6 | NPC AI priority trees Accord-aware updates. | **RESOLVED** — npc_behavior_v30 §8 priority trees factor Accord via Govern decision. |
| 7 | Hybrid mode Zoom-In Accord Domain Echo. | **CONFIRMED** — per scale_transitions_v30 Domain Echo rules. |

---

## §9 Propagation Checklist

| Target File | Change Required | Priority |
|-------------|----------------|----------|
| victory_v30.md §1 | TCV revaluation (Himmelenger 5, Gransol 3, total 31) | P1 |
| victory_v30.md §3 | Add universal victory condition (§6.1) as primary. Retain faction-specific as alternates. Strike Hafenmark Parliamentary Sovereignty. | P1 |
| victory_v30.md §4 | Add Partition co-victory (§6.3). Retain existing pairings as alternates. | P1 |
| victory_v30.md §10 | Update win probability assessment for revised TCV and universal condition. | P2 |
| params_board_game.md §Starting Values | Add: Accord per territory (§2.1), Starting PT (§2.2), Peninsular Strain (start 0, range 0–10). | P1 |
| params_board_game.md §Clock Environmental Effects | Add: Peninsular Strain threshold table (§4.3). | P1 |
| params_board_game.md §Accounting | Add steps 4c/4d/4e per §7. | P1 |
| params_board_game.md §Faction Actions | Add: Dynastic Proclamation (§5.3). Cultural Reformation (§5.4) STRUCK CR-STRIKE-2026-04-19. | P1 |
| params_board_game.md §Starting TCV | Update Crown 12, Hafenmark 6, Church 5, Varfell 6. | P1 |
| geography_v30.md | No change needed (TCV is in victory_v30.md, not geography). | — |
| npc_behavior_v30.md | Update NPC priority trees for Accord-aware governance. | P2 |
| designs/hybrid/scale_transitions_v30.md §9 | Add Accord Domain Echo rules for Zoom In/Out. | P2 |

---

## §10 Patch Register Entries

| PP | Scope | Description |
|----|-------|-------------|
| PP-NEW-01 | TCV | Himmelenger TCV 3 → 5. Gransol TCV 4 → 3. Total TCV 30 → 31. Starting: Crown 12, Hafenmark 6, Church 5, Varfell 6. |
| PP-NEW-02 | Victory | Universal Peninsular Sovereignty condition added. Faction-specific conditions retained as alternates. |
| PP-NEW-03 | Victory | Peninsular Partition co-victory added. Existing co-victory pairings retained. |
| PP-NEW-04 | System | Accord per-territory attribute (0–3). Modifies effective Prosperity. Accord ≥ 2 required for TCV contribution. |
| PP-NEW-05 | System | Peninsular Strain counter (0–10). Advances from inter-faction battles, faction eliminations, revolts. |
| PP-NEW-06 | System | Battle consequences: MS −1 per battle on Valorian soil. IP +2 per season with inter-faction battle. |
| PP-NEW-07 | Hafenmark | Dynastic Proclamation domain action (Diplomat card). Replaces Parliamentary Sovereignty as primary path. |
| ~~PP-NEW-08~~ | Varfell | ~~Cultural Reformation domain action~~ STRUCK CR-STRIKE-2026-04-19. |
| PP-NEW-09 | Church | Seizure Accord formula revised: Success → max(floor(PT/2)+1, 2). Guaranteed ≥ 2. |
| PP-NEW-10 | PT | Starting PT values per territory proposed (§2.2). |
| PP-NEW-11 | Löwenritter | Accord adaptation: Martial Governance (Military pool Govern, Ob +1, cap Accord 2). Strain exemption for first 2 seasons post-coup. |
| PP-NEW-12 | Hafenmark | Parliamentary Sovereignty (victory_v30.md §3.3 primary) struck. Dynastic Assertion promoted to primary. |
