# VALORIA — Throughline Specifications
## Eight Structural Gaps: Thread↔Settlements, Player Economy, Settlement POIs, Ministry, Löwenritter Governance, Altonian Campaign, Local Populace, Conviction Legacy
## Date: 2026-04-17
## Status: DESIGN — editorial authority exercised per Jordan's grant
## Scope: All 8 throughlines specified to mechanical depth, audited against existing systems, RSE-evaluated
## Affects: S01, S03, S04, S05, S06, S08, S09, S10, S13, S14, S15, S17, S18, Settlement Layer, Player Agency, Companion Spec

---

# THROUGHLINE 1: THREAD OPERATIONS ↔ SETTLEMENTS

## Problem

Thread operations affect province-level Metaphysical Stability (MS) but skip settlements entirely. The game's most distinctive system has no settlement-level consequence. A Dissolution that tears the substrate in S-028 Grauwald produces no visible change to the settlement. A Mending at S-033 Askeheim Ruins produces no settlement-level improvement. The settlement layer and the Thread layer do not talk to each other.

## Design

Thread operations performed within a settlement produce **settlement-level Thread consequences** alongside the existing province-level MS effects. The consequence depends on operation type and scale.

### §T1.1 Thread Consequence Table (Settlement-Level)

| Operation | Settlement Effect on Success | Settlement Effect on Failure |
|-----------|-----------------------------|-----------------------------|
| Thread-Read | No settlement effect (perception only — the settlement is observed, not changed) | No settlement effect |
| Weaving (Object/Personal) | No settlement effect (scale too small) | No settlement effect |
| Weaving (Relational+) | Order +1 if the Weaving stabilizes local social configurations. The population feels the change as a lifting of ambient tension — relationships ease, agreements hold, suspicion recedes. | No settlement effect (Weaving failure produces personal Coherence cost, not environmental) |
| Pulling (any) | No positive settlement effect | Failure: Order −1 if the Pulling's co-movement disrupts local configurations. Ambient disturbance — objects misremembered, names forgotten briefly, déjà vu across the population. |
| Past-Oriented Pulling | No positive settlement effect | Failure: Settlement Prosperity −1 (paradox window disrupts local commerce and routine). The population experiences temporal disjunction without understanding its source. |
| Dissolution (any) | No positive settlement effect | Failure: Defense −1 AND Order −1. The substrate is torn. Physical structures weaken. The population is terrified without knowing why. Visible: cracks in stone that weren't there before. A wall that no longer quite fits its foundation. |
| Mending (Object/Personal) | No settlement effect | No settlement effect |
| Mending (Relational+) | Prosperity +1 if the Mending restores substrate coherence at a scale the settlement's infrastructure depends on. Structures strengthen. Crops improve. The ambient discomfort that proximity to Thread damage produces — and that the population attributed to weather, bad luck, or divine punishment — lifts. | No settlement effect (Mending failure is personal, not environmental) |
| Community Weaving | Order +1 AND Prosperity +1 if the settlement has PT ≤ 2 AND the Weaving Succeeds. Community Weaving IS governance — it is the population participating in their own metaphysical maintenance. The settlement feels the difference. | No settlement effect |
| Lock | Defense +1 if the Lock stabilizes a structurally significant configuration (foundation, wall, natural feature). The locked configuration becomes architecturally permanent — it cannot be degraded by time, weather, or ordinary force. Only Thread operations or Calamity radiation can degrade it. | No settlement effect |

**Scale gate:** Settlement effects fire only for operations at Relational scale or above (per scale_transitions §2). Object/Personal operations are too small to affect a settlement's aggregate state. This prevents trivial Thread actions from producing governance consequences.

**Cap:** ±1 per settlement stat per season from Thread operations. Thread effects do not stack with governance actions for cap purposes — they are separate sources.

### §T1.2 Calamity Radiation at Settlement Level

Calamity radiation (calamity_radiation_v30) operates at province level per node distance from T15. With settlements, the effects are now visible at settlement level. Settlements closer to Askeheim within a province experience effects first.

| Settlement Type | Radiation Modifier |
|----------------|-------------------|
| Outpost (near Askeheim: S-011 Stillhelm Watch, S-033 Askeheim Ruins, S-034 Askeheim Gate) | Effects manifest one MS band earlier than province level. If the province is in the Strained band, these settlements experience Fragile-band effects. |
| Town (in distance-1 or distance-2 provinces) | Effects manifest at province level (no modifier). |
| Fortress, City, Seat (in any province) | Effects manifest one MS band later (institutional infrastructure provides buffer). If the province is in Fragile, these settlements experience Strained-band effects. |
| Cathedral | Church doctrine provides psychological buffer: population Certainty preserved at 1 band later. But Thread effects are not psychological — physical substrate damage fires at province level regardless. |

This means within a single province, the player sees Calamity effects hit the frontier outpost before the capital city — the radiation creeps inward from the periphery. The Seat is the last to fall. This is geographically correct and narratively powerful.

### §T1.3 Thread Perception at Settlement Level

High-TS characters (30+) perceive Thread configurations differently in different settlement types:

- **Cathedral settlements:** Thread perception is muted by institutional Certainty. The population's collective rendering is thick with doctrinal conditioning — the orthodox narrative smooths over substrate irregularities. +1 Ob to Thread-Read in Cathedral settlements (the rendering resists being perceived as substrate).
- **Outpost settlements near Askeheim:** Thread perception is amplified. The rendering is thin. −1 Ob to Thread-Read (the substrate is closer to the surface).
- **Einhir heritage settlements (S-028 Grauwald, S-029 Lodge, S-032 Oastad Shrine):** Thread perception includes cultural memory. Thread-Read Success reveals not just current configuration but one historical layer — the Einhir community's relationship to the substrate as it existed before the Catastrophe.

### §T1.4 RSE Evaluation

**Robust:** Thread operations now produce settlement consequences that create strategic decisions. Do you Mend the Gap near the town (improving Prosperity) or the fortress (improving Defense)? Do you Lock the bridge (permanent Defense) or Weave the market district (improving Order)?

**Smooth:** Uses existing Thread operation types, existing degree table, existing scale gates. Settlement effects are additive — they do not change how Thread operations resolve, only what happens afterward.

**Elegant:** One rule: Relational+ Thread operations produce settlement effects. Players intuit this — big Thread work affects the environment. Small Thread work is personal.

---

# THROUGHLINE 2: PLAYER ECONOMY AND GUILD MECHANICS

## Problem

The player has no personal economic system. Factions have Wealth. Settlements have Prosperity. The player has neither. They cannot buy, sell, invest, trade, or profit. The Guilds are visible in settlements but have no mechanical interface with the player.

## Design

### §T2.1 Personal Resources

Each player character has a **Resources** value (0–5) representing their personal economic capacity — money, trade goods, favors owed, material assets.

| Resources | What It Represents |
|-----------|-------------------|
| 0 | Destitute. Cannot pay for lodging, equipment, or services. |
| 1 | Subsistence. Basic needs met. No surplus. |
| 2 | Comfortable. Can afford equipment, travel, modest bribes. |
| 3 | Prosperous. Can fund a small operation, hire agents, maintain a household. |
| 4 | Wealthy. Can fund military equipment, sponsor events, invest in settlement development. |
| 5 | Magnate. Can influence faction-level economics. Personal wealth rivals minor faction Wealth stats. |

**Starting Resources:** Determined by faction alignment and character background. Crown officer: 2. Hafenmark merchant family: 3. Varfell scholar: 2. RM organizer: 1. Independent: 1. Church functionary: 2.

### §T2.2 Resource Sources

| Source | Resources Gained | Condition |
|--------|-----------------|-----------|
| Faction salary | +1/season | Faction-aligned character. Standing 2+ required. Standing 4+: +2/season. |
| Settlement governance | +1/season per settlement governed with Prosperity ≥ 3 | Governor takes a share of settlement economic output. This is the CK3 domain income. |
| Trade action (NEW) | +1 on Success | Pool: Cognition + Trade History. Ob: floor(5 − settlement Trade stat) + 1, min 1. Must be in a Port or City settlement. |
| Guild contract (NEW) | +1 to +3, one-time | Accept a Guild task. Reward depends on task difficulty. Tasks are Scene Slate entries from Guild Outreach (npc_behavior §8.11.6). |
| Loot | +1 per valuable recovered | Post-combat, post-investigation. GM determines when loot is available. |
| Bribery/gifts received | +1 per significant gift | NPC or faction attempting to influence the player. Accepting may shift Disposition or create Obligation. |

### §T2.3 Resource Uses

| Use | Cost | Effect |
|-----|------|--------|
| Equipment purchase | 1 | Acquire one piece of equipment (weapon, armor, tool). Follows existing equipment lists. |
| Bribe/gift | 1 | +1 Disposition with target NPC before social fieldwork. Per fieldwork §5.2 Gift/Bribe action. |
| Hire agent | 2 | Recruit one non-named NPC agent for one season. Agent performs one fieldwork action in a settlement the player is not present in. |
| Fund settlement development | 2 | Contribute to settlement Prosperity as a governance action. +1D to the governor's Develop roll (whether the governor is the player or someone else). |
| Fund military equipment | 3 | Equip one unit with upgraded weapons or armor. +1 to unit's effective Power for one battle. |
| Sponsor event | 1 | Host a public event in a settlement. Order +1 in that settlement (celebration as governance). One per season per settlement. |
| Economic Leverage (player-initiated) | 3 | Player initiates Guild-style Economic Leverage (factions_ttrpg §8.6) using personal Resources instead of faction Wealth. Only in settlements where the player has Resources ≥ 3 and governance authority. |

**Resources do not accumulate indefinitely.** Cap: 5. Excess is narratively explained as reinvestment, charity, or operational cost.

### §T2.4 Guild Mechanical Interface

The Guilds are Valoria's economic engine. With settlements and player Resources, the Guilds now have a direct player interface:

**Guild Favor (per settlement):** Already exists as a 1–7 track in Guild-managed settlements. Players can build Guild Favor through:
- Successful Trade actions in Guild settlements: +1 Favor
- Completing Guild contracts: +1 Favor
- Sponsoring events in Guild settlements: +1 Favor
- Actions that damage trade (combat in markets, blocking trade routes): −1 Favor

**Guild Favor effects (player-facing):**

| Favor | Effect |
|-------|--------|
| 1–2 | Guilds are neutral. Standard Trade Ob. |
| 3–4 | Guilds are cooperative. −1 Ob on Trade actions. Access to Guild intelligence (one rival faction's Wealth stat revealed per season). |
| 5–6 | Guilds are allied. +1D on all economic actions in this settlement. Guild agents available for hire at cost 1 instead of 2. |
| 7 | Guild partnership. The Guilds treat the player as an institutional ally. Economic Leverage can be coordinated: player and Guilds combine Resources + Wealth for joint actions. |

### §T2.5 RSE Evaluation

**Robust:** Resources create meaningful economic decisions at every stature level. A starting character (Resources 1) chooses between buying equipment and bribing a guard. A governor (Resources 3) chooses between funding settlement development and equipping their garrison. The trade-offs scale with the player's position.

**Smooth:** Resources use the existing pool/Ob/degree system. Trade is a fieldwork-style action. Guild Favor integrates with existing Guild mechanics. No new dice mechanics introduced.

**Elegant:** One number (0–5). Earnable, spendable, capped. Players intuit it immediately.

---

# THROUGHLINE 3: SETTLEMENT POIs

## Problem

Fieldwork POIs (fieldwork §3.1) were designed for provinces. With settlement anchoring, each settlement needs specific POIs to make it a distinct investigation/exploration gamespace.

## Design

### §T3.1 POI Assignment Principle

Each settlement has 2–4 POIs across Depth levels. POIs are authored per settlement type — a Fortress has different discovery content than a Cathedral. POI availability may be conditional (RS band, CV value, faction control, prior discovery).

### §T3.2 POI Templates by Settlement Type

| Type | Depth 0 (Surface) | Depth 1 (Settled) | Depth 2 (Hidden) | Depth 3+ (Buried/Liminal) |
|------|-------------------|-------------------|-------------------|--------------------------|
| **Seat** | Royal/ducal court. Public architecture. Government buildings. | Administrative archives. Court records. Official correspondence. | Private chambers. Secret passages. Diplomatic back-channels. Intelligence archives. | (If applicable) Thread-locked vault. Hidden foundation configurations. |
| **City** | Market square. Public houses. Artisan quarters. | Guild halls. Private workshops. Merchant ledgers. | Smuggling routes. Hidden meeting rooms. Underground economy. | (Rare) Einhir-era foundations beneath the city. Thread scars from pre-Catastrophe settlement. |
| **Town** | Village square. Inn. Common fields. | Local elder's records. Church chapel records. Family histories. | Concealed caches. Hidden paths. Factional safe houses. | (If Einhir territory) Remnant sites. Stone circles. Oral histories that preserve Thread memory. |
| **Fortress** | Battlements. Armory. Garrison hall. | Command archives. Prisoner records. Supply inventories. | Secret sally ports. Hidden armories. Covert communication systems. | (If ancient) Pre-Catastrophe fortification. Locked configurations in the walls. |
| **Port** | Docks. Warehouses. Customs house. | Shipping manifests. Trade contracts. Harbor master records. | Smuggling networks. Hidden cargo. Niflhel supply chain nodes. | (If old port) Submerged Einhir harbor. Maritime Thread signatures. Forgetting Zone boundary observations. |
| **Cathedral** | Nave. Public chapel. Clergy quarters. | Church archives. Theological records. Confession records (locked). | Hidden reliquaries. Pre-Solmundic architecture beneath the cathedral. Internal Inquisition files. | Thread-locked theological artifacts. The cathedral's foundation as Thread anchor — the building itself is a stabilized configuration. |
| **Mine** | Mine entrance. Processing area. Worker housing. | Geological surveys. Production records. Ore samples. | Hidden veins. Collapsed tunnels with pre-Catastrophe artifacts. | (If deep) Einhir excavation sites. Thread-dense mineral formations. Substrate exposure at depth. |
| **Outpost** | Observation post. Basic shelter. | Warden patrol logs. Environmental readings. | Hidden Thread monitoring equipment. Warden knowledge caches. | Active Thread phenomena. Gap proximity. Substrate boundary observation points. |

### §T3.3 Named POIs for Key Settlements

Rather than authoring all 80+ POIs, here are the narratively critical ones:

| Settlement | POI | Depth | Content |
|-----------|-----|-------|---------|
| S-001 Valorsplatz Palace | The Lion's Archive | 2 (Hidden) | Löwenritter intelligence records. Contains evidence of Crown-Löwenritter tensions, Coup Counter documentation, Riskbreaker operations. Gated by Löwenritter Standing or successful infiltration. |
| S-003 Valorsplatz Cathedral | The Foundation Stones | 3 (Buried) | Pre-Solmundic architecture beneath the cathedral. Thread-Read reveals the building was constructed on an Einhir ceremonial site. The Church built literally on top of what it suppresses. TS ≥ 10 required. |
| S-015 Gransol Parliament | The Constitutional Archive | 2 (Hidden) | Original Hafenmark founding documents. Contains evidence relevant to Baralta Crown Claim and Sovereign Authority Doctrine. Gated by Hafenmark Standing 3+ or successful investigation. |
| S-023 Himmelenger Cathedral | The Sealed Codex | 3 (Buried) | Pre-Schism Solmundic texts that acknowledge Thread reality in theological terms. The Church's deepest secret: the early Church knew. TS ≥ 10 OR Church Standing 5 (Cardinal access). Evidence tag: Documentary. Finding this is a campaign-defining moment. |
| S-026 Sigurdshelm Keep | Vaynard's Private Collection | 2 (Hidden) | Already specified in factions_ttrpg §8.5. Thread-locked objects, research notes, TS-advancement opportunity. Gated by Varfell Standing 3+ or Vaynard Disposition +3. |
| S-029 Grauwald Lodge | The Einhir Memory Circle | 3 (Buried) | Oral history preservation site. Thread-Read reveals the Einhir community's understanding of the Catastrophe — different from both Church doctrine and Warden knowledge. Provides +2 Evidence Track progress for any Structural investigation about the Calamity. |
| S-033 Askeheim Ruins | The Wound Core | 5 (Unintelligible) | The epicenter. Where the Catastrophe began. TS ≥ 50 required. Thread-Read here reveals the Catastrophe's mechanism — not what happened, but what the rendering encountered that it could not process. Coherence check Ob 3 on entry. Campaign endgame content. |

### §T3.4 RSE Evaluation

**Robust:** Settlement POIs make each settlement a distinct gamespace. Grauwald Lodge is not interchangeable with Gransol Parliament — they have different content at different depths requiring different character capabilities.

**Smooth:** Uses existing Depth Axis, existing POI categories (Landmark/Resource/Secret/Remnant/Anomaly/Breach), existing discovery procedure. No new mechanics.

**Elegant:** POI templates by settlement type allow GMs (and videogame content authoring) to generate POIs systematically. The templates are generative, not exhaustive.

---

# THROUGHLINE 4: THE MINISTRY AS MECHANICAL ACTOR

## Problem

The Ministry is listed as a subnational faction but has no mechanical identity — no leader, no priority tree, no NPC Stance Triangle, no Outreach. It is a passive modifier (Order decay −1) in a game where every other institution has active mechanical agency.

## Design

### §T4.1 The Ministry — Institutional Profile

The Ministry of the Peninsula is the bureaucratic apparatus that predates the current faction structure. It administers roads, courts, tax collection, land records, census, and inter-territorial communication. It is not a faction — it has no political agenda. It is infrastructure. Its continued function is what prevents Valoria from collapsing into feudal anarchy even as the factions compete.

**Partial stat sheet:** Influence 4, Stability 5. No Mandate, no Military, no Wealth, no Intel. The Ministry has institutional reach (Influence) and institutional resilience (Stability) but no capacity for political ambition, military action, economic leverage, or intelligence gathering.

### §T4.2 The Ministerialdirektor — NPC Leader

| Attribute | Value |
|-----------|-------|
| Name | Registrar Lennart Haelgrund |
| Primary Conviction | Continuity | "The work continues regardless of who sits on the throne." |
| Secondary Conviction | Precedent | When Continuity is challenged (the system is breaking down), Haelgrund falls back on procedural correctness — the records say what the records say. |
| Ethical Framework | Administrative Proceduralism | Aligned: −1 Ob on actions maintaining institutional function. Contradictory: +1 Ob on actions disrupting institutional procedure. |
| Primary Resonant Style | Consequence | Show him that the Ministry's neutrality is enabling harm — that by maintaining the roads for all factions, he is maintaining the infrastructure that allows the Church to move Inquisitors and the Crown to move armies. His Continuity conviction claims the work is apolitical. Demonstrated political consequences challenge this. |
| Secondary Resonant Style | Evidence | If Consequence fails, present documentary evidence that the Ministry has already been politicized — that specific Ministry officials have been providing faction intelligence, that census records have been altered, that road maintenance priorities favor certain factions. His system IS compromised. |
| Thread Sensitivity | 12 (Hidden) | Haelgrund has encountered Thread-adjacent phenomena in the deep archives — documents that remember differently than they should, records that describe places as they were before the Catastrophe. He does not understand what he has seen. His hidden TS makes Evidence attacks partially effective. |
| Certainty | 3 (Questioning) | His institutional certainty is intact. His metaphysical certainty is not. |
| Disposition | +1 toward all factions (neutral bureaucrat). −1 toward Niflhel (institutional threat). |
| Home Settlement | S-013 Ehrenfeld Market (the administrative crossroads) |

**Beliefs:**
1. "The Ministry serves whoever governs. We do not choose sides."
2. "The archives are the peninsula's memory. Without them, we are nothing."
3. "Something is wrong in the deep records. I do not know what, and I am afraid to find out."

### §T4.3 Ministry Priority Tree (Settlement-Level)

| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | Any Seat or City settlement under Ministry management has Order ≤ 1 | Administrative Intervention: Order +1 in that settlement (the Ministry sends officials to restore basic services). |
| 2 | Controlling faction of a Ministry-managed settlement changed this season | Administrative Transition: maintain records continuity. No stat effect, but the new controller inherits clean administrative records (Govern Ob −1 for their first governance action in this settlement). |
| 3 | Census due (every 4 seasons) | Census: reveals actual population and economic conditions. May expose discrepancies between official records and reality (e.g., Niflhel population movements, RM community size, hidden Thread practitioners). Census data is available to the controlling faction AND any player with Ministry Standing 2+. |
| 4 | Road/communication maintenance | Passive: inter-province travel Ob remains at baseline. If Ministry management is revoked from all settlements in a province, travel Ob +1 for that province (infrastructure degrades). |
| 5 | Archive request from any faction or player | Provide Documentary evidence (reliability tag) from Ministry records. Ob: 1 (Surface/Settled), 2 (Hidden), 3+ (Buried — deep archives, Haelgrund's personal territory). |

### §T4.4 Ministry Outreach (Player Interface)

Haelgrund generates Outreach when:
- Player is governing a settlement with Ministry management rights
- Player has completed an investigation using Ministry archives
- Player has Disposition ≥ +2 with Haelgrund
- A Census is due and the player's territory has anomalies

**Typical Outreach:** "Registrar Haelgrund requests a meeting at S-013 Ehrenfeld Market. The quarterly census has produced... irregularities... in your territory." (The irregularities may be: Niflhel operative movements, RM community growth, Thread-sensitive population changes, or evidence decay in the deep archives.)

### §T4.5 Ministry and Player-Governor

A player governing a settlement with Ministry management rights receives:
- −1 Ob on Administer governance action (Ministry officials assist)
- One free Research action per season at the settlement's Ministry archive (no scene action cost)
- Access to Census data for their province

This makes the Ministry the governor's institutional partner. The player who cultivates Ministry relations governs more efficiently. The player who ignores or antagonizes the Ministry governs blind.

### §T4.6 Ministry Arc: The Deep Archives

Haelgrund's third Belief ("Something is wrong in the deep records") is the Ministry's arc hook. If a player investigates the deep archives (Depth 3+ in Ministry settlements), they discover that the pre-Catastrophe records contain inconsistencies that cannot be explained by clerical error:

- Place names that don't match any known geography
- Census counts for settlements that no longer exist
- References to a "Rendering Commission" that predates both Church and Einhir institutions
- Documents that change subtly between readings (a configuration that has not been fully Locked)

This is the Ministry's Thread connection. The archives ARE a Thread artifact — not deliberately, but because records are rendered objects, and the Catastrophe's effects on rendering extend to institutional memory. Haelgrund knows something is wrong. The player can help him understand it, or can exploit the archives for investigation purposes, or can alert the Church (which would trigger a Heresy Investigation of the Ministry itself — a campaign-destabilizing event).

### §T4.7 RSE Evaluation

**Robust:** The Ministry creates governance decisions (cultivate or ignore), investigation opportunities (deep archives), and political stakes (Ministry neutrality as contested asset). It makes settlement governance richer without adding combat or military complexity.

**Smooth:** Uses existing fieldwork actions (Research), existing Outreach system, existing Stance Triangle, existing arc structure. Integrates with Census as a new information source that feeds into multiple systems (NPC behavior, faction intelligence, investigation).

**Elegant:** The Ministry is one NPC (Haelgrund) + one institutional function (bureaucracy) + one secret (the archives). Three elements that generate a full throughline.

---

# THROUGHLINE 5: LÖWENRITTER POST-COUP GOVERNANCE

## Problem

The Löwenritter Coup (npc_behavior §5.2, Almud Arc C) transfers Crown provinces to Löwenritter control. But Löwenritter has no Mandate, no Wealth — only Military, Intel, Influence, Stability. Military governance (peninsular_strain §2.6) caps at Accord 2. How do Löwenritter-controlled Seat and City settlements function?

## Design

### §T5.1 Martial Law at Settlement Level

When the Coup fires, all Crown-controlled settlements enter **Martial Law**. This is already specified at province level (factions_ttrpg §8.9). At settlement level:

| Settlement Type | Under Martial Law |
|----------------|-------------------|
| Fortress | No change. Löwenritter governance is natural here. Defense maintained. Order stable. |
| Seat | Military governor installed. Governance pool: Military (not Influence). Govern Ob +1 (military governors struggle with civil administration). Order −1 at Coup onset (population anxiety). |
| City | Military governor installed. Prosperity −1 at Coup onset (trade disruption — merchants are nervous). Guild management revoked unless Löwenritter explicitly grants it back (Influence, Ob 2). |
| Cathedral | Church management is NOT revoked. The Löwenritter respects Church institutional authority (Martial Honour framework). But Church Outreach to the player may increase — the Church sees an opportunity in Crown's fall. |
| Town | Military patrol installed. Order maintained through presence rather than governance. Govern Ob +2 (Löwenritter soldiers are not administrators). |
| Port | Trade continues under military supervision. Prosperity maintained if Guilds retained. Prosperity −1 if Guilds revoked. |

### §T5.2 The Governance Gap

Löwenritter's structural weakness: they can defend settlements but not develop them. Prosperity cannot exceed its Coup-onset value under pure Martial Governance (cap). Order cannot exceed 2 under Martial Governance (existing peninsular_strain §2.6 rule, now applied at settlement level).

**The implication:** Löwenritter NEEDS civilian partners. They must either:
1. Retain Ministry management in Seat/City settlements (maintaining administrative function)
2. Grant Guild management in commercial settlements (maintaining economic function)
3. Accept Church management in Cathedral settlements (maintaining social stability)
4. Recruit a player-governor to manage civil settlements while Löwenritter handles defense

Option 4 is the throughline to the player. Ehrenwall's Outreach to a capable player: "I can hold the walls. I cannot hold the markets. Govern this city for me." This is the CK3 moment where the martial lord needs a capable administrator — and the player is it.

### §T5.3 Post-Coup Player Opportunity

The Coup is the game's most dramatic governance opportunity for a player. Crown has fallen. Löwenritter controls the provinces but cannot govern the settlements. The player who has built Standing with Crown (now collapsed to city-state) or Renown independently is suddenly the most valuable person on the peninsula — someone who can govern.

**If the player accepts Löwenritter governance assignment:**
- They receive 1–3 Crown settlements as governor
- Their Duty becomes settlement governance
- Their Renown accelerates (+1 for each settlement maintained at Order ≥ 2 during Martial Law)
- But: they serve Löwenritter, not Crown. Standing with Crown freezes. Almud (if alive) views them with suspicion (Disposition −1). Torben may view them as a collaborator or a pragmatist, depending on the player's prior relationship.

**If the player refuses:** The settlements deteriorate. Löwenritter's Martial Governance produces Order 2 cap. Prosperity stagnates. The population resents military rule. This creates the conditions for the player to CHALLENGE Löwenritter later — liberating settlements from incompetent military governance.

### §T5.4 RSE Evaluation

**Robust:** The Coup becomes a settlement-level governance crisis, not just a faction-level event. The player has meaningful choices with lasting consequences.

**Smooth:** Uses existing Martial Governance rules, existing settlement governance actions, existing Outreach. No new mechanics.

**Elegant:** One event (Coup) creates a cascade of settlement-level consequences that naturally generate player engagement.

---

# THROUGHLINE 6: ALTONIAN INVASION CAMPAIGN

## Problem

IP triggers invasion, but the invasion has no settlement-by-settlement campaign plan. The Altonian Vanguard needs target priorities.

## Design

### §T6.1 Altonian Campaign AI

The Altonian Vanguard enters through Lowenskyst (T3, primary NE pass) or Spartfell (T10, secondary NW pass, at IP 75+). Once inside, the Vanguard operates as a military AI with a settlement-by-settlement target sequence.

**Primary Route (Lowenskyst Entry):**

| Stage | Target Settlement | Objective | Bypass Condition |
|-------|------------------|-----------|-----------------|
| 1 | S-006 Lowenskyst Fortress | Must capture or siege. Cannot bypass (Defense 4). | Only if Defense reduced to ≤ 1 by prior action (sabotage, siege attrition). |
| 2 | S-005 Kronmark Watchtower | Capture or bypass. | Military > Defense + 2 |
| 3 | S-004 Kronmark Town | Capture. Supply base for advance on Valorsplatz. | Cannot bypass (supply requirement). |
| 4 | S-001 Valorsplatz Palace | Strategic objective. Capture = Crown province falls. | — |

**Secondary Route (Spartfell Entry):**

| Stage | Target Settlement | Objective | Bypass Condition |
|-------|------------------|-----------|-----------------|
| 1 | S-019 Spartfell Fortress | Must capture or siege. | Only if Defense reduced to ≤ 1. |
| 2 | S-020 Spartfell Village | Capture for supply. | Military > Defense + 2 |
| 3 | S-022 Halvarshelm Town → S-021 Mines | Economic target. Capture mines to fund continued campaign. | Can bypass if supply from Spartfell is sufficient. |
| 4 | S-008 Gransol Parliament | Strategic objective. Capture = Hafenmark province falls. | — |

**Naval Route (Schoenland permission at IP 75+):**

| Stage | Target Settlement | Objective |
|-------|------------------|-----------|
| 1 | S-002 Valorsplatz Riverside | Port capture. Landing site. |
| 2 | S-001 Valorsplatz Palace | Direct strike on Crown capital. |

### §T6.2 Altonian Vanguard Settlement Behavior

When the Vanguard occupies a settlement:
- Defense set to Vanguard Military (typically 5–6)
- Order set to 0 (occupied population revolts)
- Prosperity −2 (military requisition, economic disruption)
- CV set to 0 (Altonian empire is not Solmundic — Church authority is irrelevant to occupiers)

**Player opportunity during invasion:** The invasion creates Priority 0 mandatory scenes for any player in invaded provinces. The player can: defend a settlement (mass combat), evacuate civilians (Endurance, Ob 2 — saves population, Order −1 prevented), sabotage Altonian supply (Intel action, Ob 3 — reduces Vanguard effective Military by 1 for next assault), or negotiate (Attunement, Ob 4 — Altonian commander may spare a settlement if offered strategic value).

### §T6.3 RSE Evaluation

**Robust:** The invasion is a settlement-by-settlement campaign with player agency at each stage.

**Smooth:** Uses existing assault/siege/bypass mechanics from settlement_layer §5.1. Vanguard priority tree follows existing NPC AI template.

**Elegant:** Two invasion routes with clear chokepoints. Players can see what's coming and prepare.

---

# THROUGHLINE 7: LOCAL POPULACE

## Problem

Settlements have Order as a stat but no named population. No bakers, magistrates, elders, or laborers to talk to.

## Design

### §T7.1 Local Actors

Each settlement generates 1–2 **Local Actors** — non-faction NPCs who represent the settlement's population. Local Actors are not full Stance Triangle NPCs (that would overwhelm the roster). They are lightweight:

| Attribute | Value |
|-----------|-------|
| Name | Generated from settlement culture (Germanic for Crown/Church, Norse for Varfell, Maritime for Hafenmark). |
| Role | One of: Elder, Magistrate, Merchant, Priest, Artisan, Farmer, Fisher, Miner, Scholar, Healer. |
| Conviction | One conviction (drawn from settlement's cultural context). |
| Disposition | Starting +1 toward the settlement's governor. 0 toward all others. |

**Local Actor count by settlement type:**

| Settlement Type | Local Actors | Rationale |
|----------------|-------------|-----------|
| Seat | 2 | Capital has diverse population representation. |
| City | 2 | Urban centers have multiple community voices. |
| Town | 1 | Small settlement, one community leader. |
| Fortress | 1 | Garrison chaplain or quartermaster. |
| Port | 2 | Dock workers and merchants are distinct communities. |
| Cathedral | 1 | Church layperson (not clergy — clergy are Church faction NPCs). |
| Mine | 1 | Mine foreman or labor representative. |
| Outpost | 0 | Too small/remote for settled population. |

**Total Local Actors: ~45–50** across 36 settlements. These are lightweight NPCs — one Conviction, one Disposition track, one role. They do not have full arc profiles, Resonant Styles, or Certainty tracks. They are the settlement's human face.

### §T7.2 Local Actor Functions

- **Scene generation:** Local Actors generate Priority 5 (ambient) Scene Slate entries. "The elder of Grauwald wants to discuss the harvest" or "The dock foreman in Gransol Harbor has a complaint about Guild fees."
- **Information source:** Local Actors provide Settled-depth (Depth 1) information about their settlement for free (no roll — they volunteer it). Hidden-depth (Depth 2) requires Disposition +2.
- **Governance feedback:** When the player governs a settlement, Local Actors are the player's feedback channel. Their Disposition reflects the population's satisfaction. Order stat changes are felt through Local Actor conversations before they appear as numbers.
- **Recruitment pool:** Local Actors at Disposition +3 become eligible for organization recruitment (settlement_layer §6.2, Stage 2→3). The player builds their movement from the bottom up — one elder, one merchant, one healer at a time.

### §T7.3 Local Actor Disposition Drivers

| Event | Disposition Change |
|-------|-------------------|
| Player governs settlement, Order improves | +1 |
| Player governs settlement, Order declines | −1 |
| Player sponsors event in settlement | +1 |
| Player initiates public combat in settlement | −2 |
| Player defends settlement from invasion/siege | +2 |
| Settlement changes controller (any cause) | Reset to 0 (new regime, wait and see) |
| Player fulfills a Conviction relevant to the settlement's concerns | +1 |

### §T7.4 RSE Evaluation

**Robust:** Local Actors give the population a voice. Governance has a human face. The player's relationship with their settlement is not Order-as-number — it is the elder's gratitude or the merchant's complaint.

**Smooth:** Lightweight NPCs (one Conviction, one Disposition) — minimal tracking overhead. Use existing fieldwork social actions.

**Elegant:** ~45 lightweight NPCs across the game. One role, one Conviction, one Disposition. Generated, not hand-authored. The system scales.

---

# THROUGHLINE 8: CROSS-GENERATIONAL CONVICTION LEGACY

## Problem

When a player character retires or dies in a 30-year game, their Convictions die with them. A cause pursued for 20 years vanishes. The new character starts with blank Convictions, disconnected from their predecessor's life work.

## Design

### §T8.1 Conviction Legacy

When a player character retires, dies, or passes governance to a protégé (settlement_layer §7.2), the player may designate one active Conviction as a **Legacy Conviction**. The new character inherits this Conviction in transformed form.

**Transformation rules:**

| Original Conviction | Transformation |
|--------------------|---------------|
| "I will [achieve X]" (unfulfilled goal) | "I will complete what [predecessor] began — [X]" OR "I will understand why [predecessor] failed at [X]" |
| "I will [achieve X]" (fulfilled goal) | "I will protect [predecessor]'s achievement — [X must endure]" OR "I will surpass what [predecessor] built" |
| "I will [relationship with NPC]" | "I will honor [predecessor]'s bond with [NPC]" OR "I will learn what [NPC] meant to [predecessor]" (if NPC survives) / "I will carry [predecessor]'s grief for [NPC]" (if NPC dead) |

The Legacy Conviction occupies one of the new character's three Conviction slots at creation. The other two are authored fresh. The Legacy Conviction can be revised normally (per player_agency §2.3) — the new character is not bound forever by their predecessor's cause. But it starts there. The past shapes the present.

### §T8.2 Renown Inheritance

Already specified: new character inherits floor(predecessor Renown ÷ 2). This means a Renown 8 predecessor produces a Renown 4 heir — Noted stature, not starting from zero. The predecessor's reputation opens doors that a nobody could not walk through.

### §T8.3 Relationship Inheritance

The new character inherits modified Disposition tracks:
- NPCs who had Disposition ≥ +3 with the predecessor: start at +1 with the new character ("I respected your mentor/parent/predecessor")
- NPCs who had Disposition ≤ −2 with the predecessor: start at −1 with the new character ("I remember what your predecessor did")
- All other NPCs: start at 0

**Knotted NPCs:** Knots do not transfer. The new character must build their own Thread relationships. But NPCs who were Knotted to the predecessor have a Knot scar — a relational echo that provides +1D on the new character's first Connect action with that NPC (the residual Thread connection facilitates initial contact).

### §T8.4 Settlement Inheritance

If the predecessor governed settlements, the new character may inherit governance:
- If the new character is the predecessor's designated protégé: governance transfers automatically. Settlements retain their stats. Local Actors' Disposition resets to +1 (benefit of the doubt for the chosen successor).
- If the new character is not the designated protégé: the faction assigns a new governor. The new character starts as an Operative and must earn governance through Standing (existing pathway).

### §T8.5 The Felt Experience of Legacy

The Legacy Conviction creates a unique narrative moment at the start of the new character's story. The player is not starting over — they are continuing. The world remembers their predecessor. NPCs reference the predecessor's actions. The settlements the predecessor governed bear the marks of their governance (Prosperity levels, Defense investments, Order maintenance). The clocks the predecessor influenced (MS Mended, TC resisted, IP delayed) reflect their contributions.

The new character walks into a world shaped by the player's prior choices. This is Crusader Kings' dynasty system applied to a single-player narrative. The player's investment across generations compounds.

### §T8.6 RSE Evaluation

**Robust:** Legacy Convictions, Renown inheritance, Disposition inheritance, and settlement inheritance create meaningful continuity. The player's 20-year investment is not lost.

**Smooth:** Uses existing Conviction mechanics, existing Disposition system, existing settlement governance. One new concept (Legacy Conviction) with simple transformation rules.

**Elegant:** One inherited Conviction, halved Renown, modified Dispositions. Three numbers that carry 20 years of accumulated meaning.

---

# PART 2: CROSS-THROUGHLINE AUDIT

## Interdependency Verification

| Throughline | Interacts With | Interaction |
|-------------|---------------|-------------|
| T1 Thread↔Settlements | T3 POIs | Thread-dense POIs (Depth 3+) in settlements produce Thread consequences when explored |
| T1 Thread↔Settlements | T4 Ministry | Deep archives are a Thread artifact — Thread-Read in Ministry settlements may trigger archive instability |
| T2 Player Economy | T4 Ministry | Ministry governance reduces administration cost; Guild contracts provide Resources; Trade requires Port/City settlements |
| T2 Player Economy | T7 Local Populace | Sponsoring events builds Local Actor Disposition; Guild Favor built through Trade interactions in settlements |
| T3 POIs | T4 Ministry | Ministry archives are POIs at Depth 2–3 in Seat/City settlements |
| T4 Ministry | T5 Löwenritter | Post-Coup, Löwenritter needs Ministry management to maintain civil governance. Ministry Outreach to player increases during Martial Law. |
| T5 Löwenritter | T6 Altonian | Löwenritter Coup weakens Crown border defense, accelerating Altonian invasion timeline (IP +5 on Coup). Player must choose: stabilize post-Coup settlements or defend the border. |
| T6 Altonian | T7 Local Populace | Invasion resets all Local Actor Dispositions in occupied settlements to −2 (occupier resentment). Liberation resets to +2 (gratitude). |
| T7 Local Populace | T8 Legacy | Local Actors who had Disposition +3 with predecessor start at +2 with inheritor (the community remembers who governed well). |

## No Conflicts Detected

All 8 throughlines use existing mechanical vocabulary (pool/Ob/degree, Disposition, Order, Depth Axis, Stance Triangles, Outreach, Scene Slate). No new dice mechanics. No new resolution systems. Every throughline extends what exists rather than inventing from scratch.

---

# PART 3: PROPAGATION MAP

| File | Changes |
|------|---------|
| designs/systems/settlement_layer_v30.md | §T1.1 Thread consequence table, §T1.2 Calamity settlement modulation, §T7.1 Local Actors, §T3.2 POI templates |
| designs/ttrpg/threadwork_v30.md | Cross-reference: settlement-level Thread consequences per settlement_layer |
| designs/setting/calamity_radiation_v30.md | Settlement-type radiation modifier table |
| designs/fieldwork/fieldwork_v30.md | POI templates by settlement type. Named POIs for key settlements. |
| designs/systems/npc_behavior_v30.md | §T4.2 Haelgrund Stance Triangle. §T4.3 Ministry priority tree. §T4.4 Ministry Outreach. |
| designs/ttrpg/factions_ttrpg_v30.md | Ministry faction profile (partial sheet: Influence 4, Stability 5). |
| designs/board_game/peninsular_strain_v1.md | §T5.1 Martial Law at settlement level. |
| designs/systems/player_agency_v30.md | §T2.1 Resources (0–5). §T8.1 Legacy Conviction. §T8.3 Relationship inheritance. |
| designs/board_game/military_layer_v30.md | §T6.1 Altonian campaign AI with settlement targets. |
| designs/systems/companion_specification_v30.md | Legacy: Knotted companion Knot scar for inheritor. |
| designs/combat/combat_v30.md | Cross-reference: Trade action Ob for Guild-settlement interactions. |
| designs/systems/clock_registry_v30.md | Resources track (0–5 per PC). Local Actor Disposition tracks. |
| references/canonical_sources.yaml | Throughline entries. |

---

*End of document.*
