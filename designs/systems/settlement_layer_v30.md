# VALORIA — Settlement Layer Specification
## Date: 2026-04-16
## Status: PROPOSAL — requires approval before integration
## Scope: Sub-territory settlement nodes, dual-authority governance, subnational factions, invasion granularity, player progression from settlement to national, faction emergence/collapse, extended timeline, succession
## Precedent: KOEI ROTK (officer-city assignment, development, provincial control), Crusader Kings III (barony-county-duchy-kingdom hierarchy, vassal governance, realm fragmentation)
## Affects: S03 Geography, S04 Clocks, S06 Faction Layer, S07 Victory, S08 TC, S09 Military, S10 NPC Behavior, S14 Fieldwork, S15 Mass Combat, S17 Scale Transitions, Player Agency, Companion Specification
## Canon compliance: P-01 (settlement-level Thread phenomena), P-03 (settlement as rendered environment), P-15 (settlement identity as cultural-layer persistence)

---

# PART 1: ARCHITECTURE

## §1.1 The Two-Tier Map

The existing 17 territories become **provinces** — the strategic layer. Each province contains 1–3 **settlements** — the personal layer. Provinces are where factions operate. Settlements are where people live and where the player acts.

| Layer | Unit | Count | Control | Mechanical Function |
|-------|------|-------|---------|-------------------|
| Province | T1–T17 | 17 | National-level faction | Domain Actions, faction stats, Accord, military movement |
| Settlement | S-001 to S-036 | 36 | Governor (NPC, player, or subnational faction) | Scene actions, fieldwork, social engagement, local governance, economic output |

**Provinces are not changed.** All existing province-level mechanics (Accord, Piety Track, TCV, Fort Level, Calamity radiation, adjacency) continue to operate at the province level. Settlements add granularity beneath provinces — they do not replace them.

**The ROTK principle:** A national-level faction controls a province. It assigns officers to manage settlements within that province. An officer who governs well builds standing. An officer who governs badly or rebels can be replaced. A player who accumulates enough settlements can challenge for provincial control. A faction that loses all its provinces may retain a single settlement as a city-state.

**The CK3 principle:** Settlements have types (Seat, City, Town, Fortress, Cathedral, Port). Type determines what the settlement produces and which subnational factions have a natural claim to manage it. A Market settlement naturally aligns with Guild management. A Cathedral settlement naturally aligns with Church management. The controlling province faction can override these natural alignments, but doing so costs Accord.

## §1.2 Settlement Types

| Type | Function | Natural Manager | Stats |
|------|----------|-----------------|-------|
| **Seat** | Provincial capital. Administrative center. Court location. | Province-controlling faction | Prosperity, Defense, Population |
| **City** | Major urban center. Trade, population, culture. | Province-controlling faction or Guilds | Prosperity, Population, Trade |
| **Town** | Smaller settlement. Local governance. Agricultural or resource base. | Province-controlling faction | Prosperity, Population |
| **Fortress** | Military installation. Chokepoint defense. Garrison base. | Province-controlling faction or Löwenritter | Defense, Garrison Capacity |
| **Port** | Coastal or river settlement. Naval access. Trade hub. | Province-controlling faction or Guilds | Prosperity, Trade, Naval |
| **Cathedral** | Church institution. Theological center. Piety generator. | Church (regardless of province controller) | Piety Influence, Population |
| **Mine** | Resource extraction. Economic output. | Province-controlling faction or Guilds | Prosperity (raw), Population (low) |
| **Outpost** | Frontier settlement. Observation, defense, or Thread monitoring. | Province-controlling faction or Wardens | Defense (low), Special (varies) |

## §1.3 Settlement Stats

Each settlement has 3 stats tracked on a 0–5 scale:

| Stat | What it represents | Effect |
|------|-------------------|--------|
| **Prosperity** | Economic output and quality of life | Contributes to province Effective Prosperity. Each point of settlement Prosperity adds to the province's Prosperity pool. |
| **Defense** | Fortification and garrison readiness | Determines Ob for attackers. Defense 0 = undefended (auto-capture). Defense 5 = major fortress. |
| **Order** | Local institutional stability and compliance | Analogous to province Accord but at settlement scale. Order 0 = local revolt. Order 3+ = stable governance. Feeds upward into province Accord. |

**Province Accord derivation (REVISED):** Province Accord is now the floor of the average Order across all settlements in the province, rounded down. If a province has 3 settlements with Order 4, 2, and 1, the province Accord = floor((4+2+1)/3) = floor(2.33) = 2. This means province Accord emerges from settlement governance rather than being set directly. Existing Accord change rules (peninsular_strain §2.3–2.4) now operate by modifying settlement Order values, which cascade upward.

---

# PART 2: THE 36 SETTLEMENTS

## §2.1 Settlement Registry

| S# | Name | Province | Type | Starting Controller | Starting Stats (P/D/O) | Notes |
|----|------|----------|------|--------------------|-----------------------|-------|
| **Crown Provinces** | | | | | | |
| S-001 | Valorsplatz Palace | T1 Valorsplatz | Seat | Crown | 4/3/4 | Royal court. Lion's Table HQ. Torben resides here. |
| S-002 | Valorsplatz Riverside | T1 Valorsplatz | Port | Crown (Guild-managed) | 4/1/3 | River trade hub. Guild quarter. Largest market in Valoria. |
| S-003 | Valorsplatz Cathedral | T1 Valorsplatz | Cathedral | Church | 2/1/4 | Old Solmundic church. Not as grand as Himmelenger but politically significant — Church presence in the capital. |
| S-004 | Kronmark | T2 Kronmark | Town | Crown | 3/1/3 | Agricultural heartland center. Crown's breadbasket administration. |
| S-005 | Kronmark Watchtower | T2 Kronmark | Fortress | Crown | 1/3/3 | Guards northern approach to Valorsplatz. |
| S-006 | Lowenskyst Fortress | T3 Lowenskyst | Fortress | Crown | 1/4/4 | The NE pass fortress. Primary Altonian chokepoint. Fort Level 3 (max 4). |
| S-007 | Lowenskyst Garrison Town | T3 Lowenskyst | Town | Crown | 2/1/3 | Military support settlement. Soldiers' families, supply depot. |
| S-008 | Feldmark | T5 Feldmark | Town | Crown | 4/0/3 | Breadbasket territory. Granary complex. Hafenmark food dependency anchor. |
| S-009 | Feldmark Storehouse | T5 Feldmark | Mine | Crown | 3/0/2 | Strategic food storage and processing. Controls food supply to northern provinces. |
| S-010 | Stillhelm | T6 Stillhelm | Town | Crown | 2/0/2 | Southern farming settlement. Calamity-adjacent. Population uneasy. |
| S-011 | Stillhelm Watch | T6 Stillhelm | Outpost | Crown (Warden-aligned) | 0/2/2 | Observation post facing Askeheim. Calamity monitoring. Warden contact point. |
| S-012 | Ehrenfeld Citadel | T14 Ehrenfeld | Fortress | Crown (Löwenritter-garrisoned) | 1/4/4 | Military headquarters. Löwenritter base. 5-way connection hub. Fort Level 3. |
| S-013 | Ehrenfeld Market | T14 Ehrenfeld | City | Crown | 3/1/3 | Trade junction at the crossroads. Merchants from all factions. |
| S-014 | Ehrenfeld Barracks | T14 Ehrenfeld | Fortress | Löwenritter | 1/3/4 | Riskbreaker operations. Separate from Citadel command. |
| **Hafenmark Provinces** | | | | | | |
| S-015 | Gransol Parliament | T8 Gransol | Seat | Hafenmark | 4/2/4 | Parliament building. Baralta's court. Constitutional center. |
| S-016 | Gransol Harbor | T8 Gransol | Port | Hafenmark (Guild-managed) | 4/1/3 | Western sea trade. Schoenland route. |
| S-017 | Gransol Market Quarter | T8 Gransol | City | Guilds | 5/0/3 | Guild headquarters. Largest trade settlement in Hafenmark. |
| S-018 | Rendstad | T7 Rendstad | Town | Hafenmark | 2/0/2 | Timber processing. Remote valley settlement. |
| S-019 | Spartfell Fortress | T10 Spartfell | Fortress | Hafenmark | 1/3/3 | NW pass fortress. Secondary Altonian chokepoint. Fort Level 2. |
| S-020 | Spartfell Village | T10 Spartfell | Town | Hafenmark | 2/1/2 | Border garrison town. |
| S-021 | Halvarshelm Mines | T17 Halvarshelm | Mine | Hafenmark (Guild-managed) | 3/0/2 | Primary mining operation. Iron and copper. |
| S-022 | Halvarshelm Town | T17 Halvarshelm | Town | Hafenmark | 2/0/3 | Miner settlement. Guild labor presence. |
| **Church Province** | | | | | | |
| S-023 | Himmelenger Cathedral | T9 Himmelenger | Cathedral | Church | 3/2/5 | Solmundic spiritual center. Confessor's seat. Highest Piety. |
| S-024 | Himmelenger City | T9 Himmelenger | City | Church | 3/1/4 | Urban population. Scholars. Cardinal of Temperance. |
| S-025 | Himmelenger Seminary | T9 Himmelenger | Cathedral | Church | 1/1/5 | Church training. Theological center. Inquisitor recruitment. |
| **Varfell Provinces** | | | | | | |
| S-026 | Sigurdshelm Keep | T12 Sigurdshelm | Seat | Varfell | 3/2/3 | Vaynard's court. Private Collection housed here. |
| S-027 | Sigurdshelm Cove | T12 Sigurdshelm | Port | Varfell | 2/1/2 | Fjord access. Varfell's limited naval capability. |
| S-028 | Grauwald | T4 Grauwald | Town | Varfell | 2/0/2 | Highland settlement. Einhir heritage site. RM presence. |
| S-029 | Grauwald Lodge | T4 Grauwald | Outpost | RM (covert) | 1/0/2 | Einhir cultural preservation. RM meeting site. Hidden. |
| S-030 | Halvardshelm | T11 Halvardshelm | Town | Varfell | 2/0/2 | Central fjord settlement. |
| S-031 | Oastad | T13 Oastad | Town | Varfell | 2/0/2 | Southern fishing settlement. Calamity-adjacent. |
| S-032 | Oastad Shrine | T13 Oastad | Outpost | RM (overt) | 0/0/1 | Old Einhir ceremonial site. RM stronghold. Lowest CV territory. Community Weaving site. |
| **Uncontrolled** | | | | | | |
| S-033 | Askeheim Ruins | T15 Askeheim | Outpost | Wardens | 0/1/1 | Einhir Catastrophe epicenter. Active Warden operations. Forgetting barrier. |
| S-034 | Askeheim Gate | T15 Askeheim | Outpost | Uncontrolled | 0/0/0 | Southern access point. Observation camp. No permanent population. |
| **Schoenland** | | | | | | |
| S-035 | Schoenland City | T16 Schoenland | City | Schoenland | 4/2/4 | Island capital. Altonian trade. Independent governance. |
| S-036 | Schoenland Harbor | T16 Schoenland | Port | Schoenland | 3/3/4 | Naval base. Passage control. Altonian supply chain. |

**Total: 36 settlements across 17 provinces.**

| Province | # Settlements | Distribution |
|----------|--------------|-------------|
| T1 Valorsplatz | 3 | Seat + Port + Cathedral |
| T2 Kronmark | 2 | Town + Fortress |
| T3 Lowenskyst | 2 | Fortress + Town |
| T4 Grauwald | 2 | Town + Outpost (RM) |
| T5 Feldmark | 2 | Town + Mine |
| T6 Stillhelm | 2 | Town + Outpost (Warden) |
| T7 Rendstad | 1 | Town |
| T8 Gransol | 3 | Seat + Port + City (Guilds) |
| T9 Himmelenger | 3 | Cathedral + City + Cathedral |
| T10 Spartfell | 2 | Fortress + Town |
| T11 Halvardshelm | 1 | Town |
| T12 Sigurdshelm | 2 | Seat + Port |
| T13 Oastad | 2 | Town + Outpost (RM) |
| T14 Ehrenfeld | 3 | Fortress + City + Fortress (Löwenritter) |
| T15 Askeheim | 2 | Outpost (Warden) + Outpost |
| T16 Schoenland | 2 | City + Port |
| T17 Halvarshelm | 2 | Mine + Town |

---

# PART 3: DUAL-AUTHORITY GOVERNANCE

## §3.1 The Two-Tier Authority Model

Every settlement has two authority slots:

| Slot | Who | What they control |
|------|-----|------------------|
| **Provincial Authority** | The national-level faction controlling the province | Military deployment, taxation, legal framework, Domain Actions targeting the province |
| **Settlement Governor** | An officer (NPC or player) or subnational faction assigned to manage the settlement | Local governance (Order), economic development (Prosperity), local NPC relationships, settlement-level scene generation |

The Provincial Authority sets the rules. The Settlement Governor executes them. When they agree, governance is efficient. When they disagree, tension generates gameplay.

## §3.2 Governor Assignment

The faction controlling a province assigns governors to its settlements. Assignment follows the existing Duty system (player_agency_v30 §3) but at a higher stature level.

| Standing | Governor Eligibility |
|----------|---------------------|
| 0–2 (Operative/Agent) | Cannot be assigned as Governor. Receives standard Duties. |
| 3 (Counselor) | Eligible for Governor of one Town or Outpost. |
| 4 (Lieutenant) | Eligible for Governor of one City, Fortress, or Mine. |
| 5 (Successor) | Eligible for Governor of a Seat or Cathedral (requires faction leader approval). |

**Player as Governor:** When a player is assigned as Settlement Governor, their seasonal Duty IS governance. Each season, the player receives one mandatory governance action (no scene action cost) plus their normal scene actions for personal pursuits. **Companion-governor (per settlement_bridge_unification C-04):** A companion serving as governor gets 1 free action per season — social OR governance, player chooses. Not both. The governance action targets the settlement's stats:

| Governance Action | Pool | Ob | Effect on Success |
|------------------|------|-----|-------------------|
| Develop | Cognition + Wealth-relevant History | floor(Prosperity/2) + 1 | Prosperity +1 (cap: settlement type max) |
| Fortify | Military-relevant stat + History | floor(Defense/2) + 1 | Defense +1 (cap: settlement type max) |
| Pacify | Charisma + local History | floor((3 − Order) + 1), min 1 | Order +1 (cap: 5) |
| Administer | Attunement + Governance History | 2 | Maintain Order (no decay this season). Reveals one local NPC's active Conviction. |

**NPC Governor:** NPC governors use the faction AI priority tree with settlement-level adaptation. NPC governors always prioritize Order ≥ 2 (institutional stability), then Prosperity development, then Defense only if threatened.

## §3.3 Subnational Faction Governance

Certain settlement types naturally align with subnational factions. The provincial authority may grant management rights to a subnational faction, or the subnational faction may already hold traditional rights.

| Subnational Faction | Natural Settlement Types | Management Effect |
|--------------------|------------------------|-------------------|
| Church | Cathedral | +1 Piety Influence per season. Church governor uses Church stats, not province faction stats. Province faction retains taxation rights. |
| Guilds | City, Port, Market, Mine | +1 Trade per season. Guild governor uses Wealth as primary stat. Province faction retains military and legal authority. |
| Ministry | Seat, City | Administrative efficiency: Order decay −1 (Order is more stable). Governor uses Influence as primary stat. |
| Löwenritter | Fortress | Military efficiency: Defense +1 passive. Löwenritter governor uses Military as primary stat. Province faction retains legal authority but military operations defer to Löwenritter. |
| RM | Outpost, Town (in low-CV territories) | Community presence: CV −1 potential per season (Einhir heritage restoration). Only available in territories with PT ≤ 2. Province faction may not know RM is managing the settlement (covert management). |
| Wardens | Outpost (Askeheim, Stillhelm Watch) | Thread monitoring: RS effects detected 1 band earlier. Warden governor operates independently. |
| Niflhel | Any (covert) | Niflhel does not govern openly. Niflhel infiltrates a settlement by placing an operative as a secondary influence. Effect: Intel-gathering at +1D in that settlement. Detection: province faction may discover Niflhel presence via Investigation (Evidence Track threshold 3). |

**Granting management:** The province faction may grant management of a settlement to a subnational faction as a Domain Action (Influence, Ob 1 — it is an administrative act, not a contested one). The subnational faction's governor replaces the faction governor for that settlement. The province faction retains Provincial Authority (taxation, military, legal framework).

**Revoking management:** The province faction may revoke subnational management as a Domain Action (Influence, Ob = subnational faction's Influence ÷ 2, round up). Revocation costs Order −1 in the settlement (the population perceives institutional disruption) and Disposition −2 with the subnational faction's leadership.

**Contested management:** If the subnational faction's interests conflict with the province faction's orders (e.g., Church governor refuses to allow RM Community Weaving in a Cathedral settlement), the conflict resolves through social contest (per social_contest_v30 §7 — asymmetric, with the province faction as institutional authority and the subnational faction as petitioner).

---

# PART 4: SETTLEMENT AS GAMESPACE

## §4.1 Scene Slate Settlement Anchoring

Every Scene Slate entry (player_agency_v30 §4.2) is now anchored to a specific settlement, not just a province. When the Slate says "Baralta's aide wants to discuss the treasury crisis," the scene location is S-015 Gransol Parliament, not "T8 Gransol." The player travels to the settlement, not the province.

**Travel within a province:** Moving between settlements in the same province costs no scene action (local travel). Moving between provinces costs 1 scene per province traversed (existing rule, fieldwork_v30 §3.3).

**Settlement-level fieldwork:** All fieldwork actions (investigation, socializing, exploration) operate at settlement level. The Depth Axis applies per settlement — a character who has explored S-015 Gransol Parliament to Depth 3 has not necessarily explored S-017 Gransol Market Quarter at all. Exposure, however, is tracked per province (existing rule — faction surveillance covers the whole territory).

## §4.2 Subnational Faction Visibility

Settlements make subnational factions visible to the player:

| Subnational Faction | Where Visible | How Visible |
|--------------------|--------------|-------------|
| Ministry | Seat and City settlements | Officials in administrative buildings. Bureaucratic delays. Paperwork. The Ministry is the slow grind of institutional governance — the player sees it in settlement administration. |
| Guilds | City, Port, Market, Mine settlements | Merchants, craftsmen, guild halls, trade disputes, labor actions. The Guilds are the economic texture of urban life. |
| Niflhel | Any settlement (covert) | NOT visible unless discovered. The player may notice: unexplained supply chain activity, strangers who arrive and leave without transaction, a locked warehouse in the dock quarter. Investigation can reveal Niflhel presence. |
| RM | Town and Outpost settlements in low-CV territories | Community gatherings, Einhir cultural practices, whispered songs, the old stone circles maintained despite Church disapproval. RM presence is visible in the cultural texture of daily life. |
| Löwenritter | Fortress settlements | Military patrols, knight chapters, weapons training, the tension between martial discipline and political loyalty. The player sees the Löwenritter as a professional military organization operating semi-independently. |
| Wardens | Outpost settlements near Askeheim | Thread practitioners in practical dress. Equipment for Mending. The work — the constant, unglamorous work of holding the Southernmost together. |
| Local Actors | Any settlement | Mayors, magistrates, elders, community leaders who are not affiliated with any national faction. These NPCs have Convictions and Disposition tracks. They represent the population's autonomous political will. |

## §4.3 Settlement Events

Each settlement generates 0–1 local events per season based on its stats and type. These feed into the Scene Slate at Priority 4 (Territorial).

| Condition | Event |
|-----------|-------|
| Prosperity 0 | Famine or economic collapse. Population leaving. Order −1 automatic. |
| Defense 0 + adjacent hostile military | Raid or siege. Mandatory scene if player is present. |
| Order 0 | Local revolt (analogous to province Accord 0 but at settlement scale). Governor expelled unless garrison present. |
| Order 5 + Prosperity 4+ | Flourishing. Local festival, trade fair, or cultural event. +1 Disposition with all local NPCs. Scene opportunity for the player. |
| Cathedral type + CV change in province | Religious event: sermon, ceremony, procession, or protest depending on CV direction. |
| Mine type + Prosperity 3+ | Resource surplus. Province Wealth +1 at Accounting (economic contribution). |
| Fortress type + hostile military in province | Garrison mobilization. Defense check: Defense pool vs Ob 2. Success: settlement holds. Failure: attacker bypasses or captures. |

---

# PART 5: MILITARY GRANULARITY

## §5.1 Invasion and Defense

Invading a province now requires capturing (or bypassing) its settlements. The Seat is the strategic objective — capturing the Seat grants provincial control. Other settlements may be captured, bypassed, or besieged independently.

**Capture sequence:** An invading army entering a province must choose which settlement to attack first. Adjacent settlements within the province are connected by the internal road network. The invader moves through settlements in sequence unless they bypass.

| Action | Requirement | Effect |
|--------|------------|--------|
| Assault | Military vs Defense + garrison | Success: settlement captured. Failure: attacker repelled, takes casualties. |
| Siege | Military ≥ Defense | No immediate roll. Each season: defender Order −1 (starvation/pressure). When Order = 0, settlement surrenders. Attacker cannot move to other settlements while besieging. |
| Bypass | Military > Defense by 2+ | Attacker moves past the settlement to the next one. Bypassed settlement remains hostile — its garrison can attack the invader's supply line (Military vs Ob 1 each season: success = invader takes −1 Discipline on all units in the province). |

**Province capture:** When the Seat is captured, provincial control transfers to the invader. Non-Seat settlements with Order ≥ 3 may resist (maintaining their current governor). The invader must reduce each resistant settlement individually or grant them autonomy (subnational management) to avoid further conflict.

**Fortress as chokepoint:** A Fortress settlement in the invader's path forces engagement — it cannot be bypassed unless the invader's Military exceeds the Fortress Defense by 3+. Lowenskyst Fortress (S-006, Defense 4) requires Military 7+ to bypass — effectively impossible for most armies. This is the design's intended function.

## §5.2 Garrison and Defense

Each settlement can host a garrison (one military unit). The garrison's stats (from military_layer_v30) add to the settlement's Defense for the purpose of Assault checks: effective Defense = settlement Defense + garrison Discipline.

Ungarrisoned settlements with Defense 0 are auto-captured on any hostile military entry — no roll needed. This makes Towns and Outposts vulnerable unless garrisoned, while Fortresses can hold independently.

---

# PART 6: PLAYER PROGRESSION — SETTLEMENT TO NATIONAL

## §6.1 The Stature Ladder (Canonical — referenced by player_agency_v30 §5.4)

The existing Standing track (0–5 per faction) and Renown track (0–10 cross-faction) from player_agency_v30 now map to a concrete progression of governance scope:

| Renown | Standing | Governance Scope | ROTK Parallel | CK3 Parallel |
|--------|----------|-----------------|---------------|-------------|
| 0–2 | 0–2 | None. Operative/Agent. Personal actions only. | Officer without assignment | Unlanded courtier |
| 3–4 | 3 | **Settlement Governor.** Manage one Town/Outpost. Free governance action per season. | City governor | Baron |
| 5–6 | 4 | **Multi-Settlement.** Manage up to 3 settlements. May hold settlements across provinces (with faction permission). Province-level influence. | Provincial governor | Count |
| 7–8 | 4–5 | **Provincial Authority.** De facto province controller. Independent Domain Actions via Renown pool. May challenge for formal leadership. | Viceroy | Duke |
| 9–10 | 5 | **National Actor.** Found a new faction or take over existing one. Control provinces directly. Issue Domain Actions. Participate in Parliament. Full parity with Crown, Hafenmark, Varfell, Church. | Independent warlord / Emperor | King |

## §6.2 Faction Emergence — Local to National

A player (or NPC actor like RM) can build a faction from the ground up:

**Stage 1 — Cell (Renown 0–2):** Personal network. Companions and Knots. No institutional structure. No settlements. The player exists at the mercy of existing factions.

**Stage 2 — Organization (Renown 3–4):** Assigned to or seize a settlement. Begin developing it. Recruit local NPCs. The player is visible as a local authority figure. The subnational faction begins to exist — it has one settlement, one governor (the player), and an implicit claim to local autonomy.

**Stage 3 — Movement (Renown 5–6):** Multiple settlements. Cross-settlement coordination. The player's organization has Influence and maybe Wealth as faction stats (partial sheet — like RM or early Löwenritter). The organization can participate in local politics but cannot issue national-level Domain Actions.

**Stage 4 — Faction (Renown 7–8):** Provincial authority. The organization controls enough settlements to claim a province. It now has a full faction stat sheet (Mandate, Influence, Wealth, Military, Stability). It can issue Domain Actions, participate in Parliament, enter treaties. It is a national-level faction — one of the powers on the peninsula.

**Stage 5 — Hegemon (Renown 9–10):** Multiple provinces. The player's faction competes with Crown, Hafenmark, Varfell, Church for peninsular sovereignty. Victory conditions apply. The player has risen from nobody to contender through accumulated deeds, not scripted events.

**Emergence requirements per stage:**

| Stage | Requirements |
|-------|-------------|
| 2 → 3 | Control 2+ settlements. Renown 5+. At least 2 NPC officers with Disposition +3. |
| 3 → 4 | Control 4+ settlements across 2+ provinces. Renown 7+. Declare faction formally (Domain Action: Influence pool = Renown ÷ 2, Ob 3). At least 1 province Seat controlled. |
| 4 → 5 | Control 2+ province Seats. Renown 9+. Full faction stat sheet. Participate in Parliament or equivalent political body. |

## §6.3 Faction Collapse — National to Local

When a national-level faction loses all its provinces, it does not vanish. It contracts.

**Collapse sequence:**

1. **Province lost:** Faction loses control of a province. Settlements in that province with governors loyal to the collapsing faction may resist the new controller (Order ≥ 3 + governor Disposition ≥ +3 toward the faction). These become holdout settlements.

2. **Last province lost:** The faction has no provinces. But if the faction leader (NPC or player) is alive and located in a settlement they personally control (typically their capital Seat), the faction survives as a **city-state** — a subnational faction controlling one or more settlements without provincial authority.

3. **City-state mechanics:** A city-state faction has a partial stat sheet (Influence, Wealth, Stability — no Mandate, no Military unless garrisoned). It cannot issue national-level Domain Actions but can: defend its settlements, trade, form alliances, participate in subnational politics, and work toward re-emergence via the Stage 2→4 pathway above.

4. **Full collapse:** If the faction leader is killed or captured and no successor exists with Standing 4+, the faction dissolves. Its remaining settlements become unmanaged (NPC governors revert to local actors with no faction affiliation). Its officers become free agents eligible for recruitment by other factions.

**Examples:**

- **Hafenmark falls:** Baralta loses T7, T10, T17 to military conquest. She retreats to S-015 Gransol Parliament with loyal officers. Hafenmark becomes a city-state: Baralta controls Gransol's 3 settlements, retains Parliament as a political institution (even if diminished), and can negotiate from a position of reduced but not eliminated power. She retains Influence 4, Wealth 3 (trade revenue from Gransol Harbor), Stability 3. She is the Duchess of Gransol, not the Duchess of Hafenmark. She can rebuild.

- **Crown collapses via Coup:** Löwenritter Coup fires. Almud is exiled. Crown provinces transfer to Löwenritter control. But Almud escapes to S-010 Stillhelm with Torben and loyal Crown officers. Crown becomes a city-state: Almud controls Stillhelm and possibly Feldmark settlements. The Crown's legitimacy claim persists — Almud is still the King, just a king without a kingdom. He can attempt restoration.

- **Church loses Himmelenger:** Varfell or RM conquers T9. But Church retains S-003 Valorsplatz Cathedral (Church management in Crown territory) and S-023 through S-025 may resist if Order is high enough. The Church's institutional authority transcends territory — it has cathedrals in other provinces. The Church contracts but does not collapse.

---

# PART 7: EXTENDED TIMELINE

## §7.1 Clock Recalibration for 10–30 Year Games

The existing clocks assume a 13–15 year game. With settlements adding governance granularity and the faction emergence pathway adding a bottom-up progression, games may last 20–30 years. Clocks must be recalibrated.

| Clock | Current Rate | Recalibrated Rate | Rationale |
|-------|-------------|-------------------|-----------|
| MS decay | −1/year baseline | −1/year baseline (unchanged) | MS is an existential pressure. 72 → 0 in 72 years without intervention. 30-year game = MS ~42 at game end (Fragile band). This is correct — long games should reach deep Calamity effects. |
| TC (Church Influence) | Passive +1/season | Passive +1/season if Church Mandate ≥ 3 (existing conditional). 28 start. | 30-year game = 120 seasons. TC caps at 75 (phase transition), so the real question is: when does 75 fire? At +1/season: ~47 seasons (~12 years). This is correct — Church pressure should peak in mid-game. |
| IP (Invasion Pressure) | +1/season baseline | +1/2 seasons baseline (halved) | Current rate: 20 start, 100 in 80 seasons (20 years). This is too fast for a 30-year game — invasion would fire before the player completes the settlement→national progression. Halved rate: 100 in 160 seasons (40 years). 30-year game: IP ~80 (Altonian preparation, not yet invasion). Invasion fires only if events accelerate IP. |
| Political Stability | 0 start, +1 per violence event | Unchanged | Cumulative. Self-regulating via victory gate (≤ 6). |

**New clock: Generational Shift (0–10).**

A 30-year game spans a generation. The first leaders (Almud, Baralta, Vaynard, Himlensendt) will age, weaken, and potentially die of natural causes. Generational Shift tracks this.

- Rate: +1 per 5 years of game time.
- Threshold 2 (Year 10): First generation leaders begin showing age. All original faction leaders: −1 to their highest attribute (age penalty). Succession planning becomes relevant. **Exception:** Characters (NPC or PC) with Thread Sensitivity ≥ 50 are exempt — the rendering sustains high-TS beings more robustly (metaphysical justification per P-15).
- Threshold 4 (Year 20): Second generation leaders emerge. Original leaders who have not been replaced are at −2 to highest attribute. NPC arc branches for retirement, abdication, or natural death activate.
- Threshold 6 (Year 30): Original leaders who survive are elderly. −3 to highest attribute. The game's political landscape has fundamentally shifted — the players' generation IS the leadership class, whether they sought it or not.

## §7.2 Succession System (Extended)

**Settlement succession:** When a settlement governor dies, is removed, or departs, the province faction must assign a new governor. If no eligible NPC or player is available, the settlement becomes unmanaged (Order −1 per season until a governor is assigned).

**Province succession:** Existing rules (npc_behavior_v30 §5.2 arc profiles) cover faction leader succession. Extended: if the heir is a player character, the player receives the province with all settlements and their current states. If the heir is an NPC, the NPC becomes the faction leader and the player's Standing is preserved.

**Cross-generational play:** In a 30-year game, the player character may age and retire. If the player has a protégé (a named NPC companion or officer with Disposition +4 and Standing 4+), the player may transfer their governance to the protégé and create a new character — starting at Standing 0 but inheriting Renown ÷ 2 (round down) from their predecessor's reputation. The predecessor becomes an NPC. This is CK3's heir system applied to TTRPG.

---

# PART 8: SYSTEM IMPACT ASSESSMENT

## §8.1 Changes to Existing Systems

| System | Impact | Severity |
|--------|--------|----------|
| S03 Geography | Province map unchanged. Settlement layer added beneath. Adjacency within provinces defined per §2.1. | Moderate — additive, not disruptive |
| S04 Clocks | IP recalibrated (halved baseline). Generational Shift clock added. All other clocks unchanged. | Low — one rate change, one new clock |
| S06 Faction Layer | Provincial Authority slot formalized. Subnational management rights added. Domain Actions unchanged — they still operate at province level. | Moderate — new governance mechanics |
| S07 Victory | Province Accord now derived from settlement Order averages. TCV unchanged. Universal victory still requires Accord ≥ 2 in all provinces. The pathway to Accord ≥ 2 is now through settlement governance. | Moderate — Accord derivation changed |
| S09 Military | Garrison at settlement level. Invasion sequence through settlements. Fortress chokepoints. Unit deployment now specifies settlement, not just province. | Significant — military granularity increased |
| S10 NPC | Settlement governors are NPCs with Stance Triangles. Local actors added as new NPC category. NPC Outreach now settlement-anchored. | Moderate — more NPCs, same system |
| S14 Fieldwork | Fieldwork anchored to settlements. Depth Axis per settlement. Exposure per province (unchanged). | Low — reframing, not redesign |
| S15 Mass Combat | Settlement Defense as pre-battle condition. Siege mechanics added. Fortress bypass rules. | Moderate — new assault/siege layer |
| S17 Scale Transitions | Settlement governance action as new Zoom In entry point. Governor → Province → National as Domain Echo chain. | Moderate — new scale level |
| Player Agency | Governor as Duty. Settlement governance as scene action. Stature ladder revised with governance scope. | Moderate — Renown thresholds now map to settlement control |
| Companions | Companions can serve as settlement governors (dual role). Companion officer from mass combat can govern the settlement their unit is garrisoned in. | Low — extension of existing |

## §8.2 What Does NOT Change

- Province-level mechanics (Domain Actions, faction stats, Parliamentary votes) operate at province level. Settlements add granularity beneath but do not replace the province layer.
- Personal-scale mechanics (combat, contests, Thread operations, fieldwork actions) operate at individual level. Settlements provide the location where these actions occur but do not modify their mechanics.
- The dice engine, pool construction, Ob system, and degree table are unchanged.
- NPC Stance Triangles, Resonant Styles, Conviction Scars — unchanged.
- Clock pressures (MS, TC, IP) — unchanged in function, only IP rate adjusted.
- Calamity radiation — operates at province level per node distance. Settlements within a province share the same radiation band.

---

# PART 9: OPEN ITEMS

| ID | Description | Priority |
|----|-------------|----------|
| ED-SETT-01 | Settlement starting Prosperity/Defense/Order values need simulation. Current values are estimated from province context, not calibrated. | P1 |
| ED-SETT-02 | Settlement governance action pool/Ob calibration. Does a 4-Cognition governor reliably develop Prosperity? Simulation needed. | P1 |
| ED-SETT-03 | Province Accord derivation from settlement Order average: does this produce Accord values consistent with existing peninsular_strain Accord tables? Edge cases: province with 1 settlement (Accord = that settlement's Order, capped at 3) vs province with 3 settlements (average may produce non-integer floors). | P1 |
| ED-SETT-04 | Siege duration calibration. At Order −1/season, a Fortress with Order 4 takes 4 seasons to fall by siege alone. Is this too long? Too short? | P2 |
| ED-SETT-05 | Subnational faction management rights: does Church management of cathedrals in non-Church provinces create a sovereignty conflict? The province faction controls the province; the Church controls the cathedral. What happens when they disagree about territorial policy? | P2 |
| ED-SETT-06 | NPC governor AI: do NPC governors follow the faction priority tree or a settlement-specific priority tree? Proposed: settlement-specific (Pacify → Develop → Fortify → Administer) with faction tree override at faction Stability ≤ 2. | P2 |
| ED-SETT-07 | Generational Shift clock: does the −1/−2/−3 attribute penalty apply to player characters? If yes, it creates a natural incentive for cross-generational play. If no, the player is mechanically immortal while NPCs age around them. Proposed: yes, it applies to PCs. | P2 |
| ED-SETT-08 | Settlement adjacency within provinces: are all settlements in a province adjacent to each other, or do some have internal road connections that matter for invasion sequence? Current proposal: all adjacent (province is small enough for local travel). | P3 |
| ED-SETT-09 | Board game physical representation: 36 settlement tokens on the map creates cognitive load. Options: (a) settlements represented on province cards, not the map; (b) settlement tokens placed only when contested; (c) settlements abstracted in BG mode (only surface in Hybrid/TTRPG). | P2 |

---

# PART 10: PROPAGATION MAP

| File | Change Required |
|------|----------------|
| designs/setting/geography_v30.md | Add settlement registry. Province map unchanged. |
| designs/board_game/peninsular_strain_v1.md | §2 Accord derivation changed to settlement Order average. §2.3/2.4 Accord change rules now target settlement Order. |
| designs/board_game/faction_layer_v30.md | Add Provincial Authority and Settlement Governor authority slots. Add subnational management grants. |
| designs/board_game/military_layer_v30.md | Add garrison at settlement level. Add Assault/Siege/Bypass mechanics. |
| designs/board_game/victory_v30.md | Verify Accord ≥ 2 still functional with settlement-derived Accord. |
| designs/systems/player_agency_v30.md | §5 Stature ladder revised with governance scope. Governor Duty type added. |
| designs/systems/npc_behavior_v30.md | Settlement governor NPCs. Local actor NPCs. NPC Outreach anchored to settlements. |
| designs/systems/clock_registry_v30.md | IP rate change. Generational Shift clock added. Settlement Order tracked. |
| designs/mass_combat/mass_battle_v30.md | Settlement Defense as pre-battle condition. Siege mechanics. Fortress rules. |
| designs/hybrid/scale_transitions_v30.md | Settlement governance as new scale level. Governor→Province→National Domain Echo chain. |
| designs/systems/companion_specification_v30.md | Companion as settlement governor (dual role). |
| designs/fieldwork/fieldwork_v30.md | Scene location anchored to settlement. Depth Axis per settlement. |
| references/canonical_sources.yaml | New entry: settlement_layer |
| designs/setting/calamity_radiation_v30.md | Confirm province-level operation (no change needed). |

---

*End of document.*
