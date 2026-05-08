# VALORIA — Historical Precedent Analysis: Warfare, Mustering, Territory Seizure
## Date: 2026-04-17
## Status: ANALYSIS — feeds design refinements
## Scope: Historical grounding for mass battle, army composition, feudal mustering, siege warfare, territory acquisition, governance legitimacy
## Companion to: references/historical_precedents_analysis.md (Church/RM/invasion/cultural revival)

---

## §1 — Medieval Warfare and the "Generalship Dominates" Axiom

### 1.1 Historical Precedents

**Crécy (1346).** Edward III's 12,000 defeated Philip VI's 30,000+. Why: terrain selection (hill, muddy field funneling cavalry), disciplined archer deployment, and command coordination. The French had more men, better-armed knights, and more cavalry. They lost because Philip couldn't coordinate sequential cavalry charges — each wave charged independently into arrow fire. Key pattern: command quality determines whether numerical superiority translates into combat effectiveness.

**Agincourt (1415).** Henry V's ~6,000 defeated a French force of 12,000–36,000 (estimates vary). Nearly identical to Crécy: terrain channeling (flanking woods), archer deployment, disciplined defense. The French command failed to coordinate a coherent plan — nobles charged independently seeking personal glory. Key pattern: feudal armies composed of independently-acting lords are structurally inferior to armies under unified command, regardless of individual unit quality.

**Cannae (216 BC).** Hannibal's 50,000 encircled and destroyed a Roman force of 86,000. Double envelopment — the defining tactical achievement of pre-modern warfare. Key pattern: a commander who can coordinate simultaneous multi-axis movement (center retreat + cavalry envelopment) defeats a larger force that can only advance in one direction. Command enables tactical complexity; lack of command reduces an army to frontal assault regardless of size.

**Hastings (1066).** Harold's Saxon army was exhausted (forced march from Stamford Bridge) and fighting without cavalry against William's combined-arms force (infantry + cavalry + archers). The decisive moment was the feigned retreat — Norman cavalry faked flight, the Saxon shield wall broke discipline to pursue, and the cavalry turned and cut down the disorganized pursuers. Key pattern: discipline (holding formation vs pursuing a retreating enemy) determines battle outcome more than equipment or numbers.

**Austerlitz (1805).** Napoleon's 68,000 defeated 85,000 Austro-Russian forces through deliberate operational deception — weakening his right to invite attack, then counterattacking through the center with the corps he'd hidden. Key pattern: the commander who controls the tempo of battle and can execute a multi-phase plan defeats the one who can only react.

### 1.2 What Valoria Already Has Right

The **"generalship dominates" axiom** (Command asymmetry, ECP = min(Size, Command) + Command) is historically correct. The formula means:
- A high-Command general with a small army outperforms a low-Command general with a large one (Agincourt, Crécy)
- As Size drops, the army degrades but Command sustains minimum effectiveness (Hannibal maintaining operational coherence while outnumbered)
- The general's death is catastrophic (two-stage death, Command drops to 0, all units uncommanded) — historically accurate for pre-modern armies that relied on the commander's personal authority

The **formation counter system** (Wedge > Line, Shield Wall > Wedge, Skirmish immune to flanking) is a reasonable abstraction of combined-arms dynamics. The **feigned retreat mechanic** directly models Hastings.

### 1.3 What's Missing or Underweight

**1.3a Supply and campaign logistics.** The single largest omission. Historical armies could not simply exist in the field indefinitely. Medieval campaigns were constrained by:
- **Foraging range:** An army could feed itself for ~3 days from carried supplies, then needed to forage. Foraging range was ~10 miles from the army's position. After the foraging radius was exhausted, the army had to move.
- **Seasonal constraints:** Campaigns were fought May–October. Winter campaigns were rare and logistically devastating (Napoleon's retreat from Moscow, Swedish campaigns in the Thirty Years' War).
- **Supply lines:** A besieging army needed continuous supply from friendly territory. Cut the supply line and the siege lifts automatically.

**Valoria's gap:** Units exist in territories without supply cost (except during siege, where Wealth −1/season models supply expenditure). A faction can maintain indefinite military presence in hostile territory with no logistical consequence. This means military conquest is "too cheap" — the cost is in battle outcomes, not in maintaining the army.

**Implication:** Add a **Campaign Supply** mechanic: units stationed in hostile territory (territory not controlled by the unit's faction) cost Wealth −0.5/season (rounded: −1 every other season). Units in friendly territory cost nothing (the population supports them). This creates economic pressure to either conquer quickly (reducing hostile time) or consolidate supply routes. The mechanic already exists for siege (Wealth −1/season) — extending it to general occupation is consistent.

Additionally: units in territories with Prosperity 0 cannot be supplied at all — they lose Size −1/season from attrition regardless of whose territory it is. A faction that devastates a territory's economy to conquer it then cannot garrison it effectively. This models the historical dynamic where scorched-earth policies made territories ungovernable.

**1.3b Feudal levy vs professional army distinction.** The unit type table (Levy, Light Infantry, Heavy Infantry, etc.) captures quality tiers but doesn't model the fundamental structural difference between feudal levies and professional armies:

- **Feudal levies** serve for a fixed term (historically 40 days in England). They cannot be kept in the field indefinitely. They have personal obligations (harvest, family) that compete with military service.
- **Professional soldiers** serve as long as they're paid. They can be kept in the field indefinitely. But they're expensive and if pay stops, they become bandits or defect.
- **Mercenaries** are professionals who fight for whoever pays. They're available quickly but have no loyalty.

**Valoria's gap:** All units persist indefinitely once mustered. There's no term-of-service limit for levies, no pay requirement for professionals, no mercenary availability.

**Implication:** Add a **Service Duration** property to unit types:

| Type | Service Duration | Overstay Consequence |
|------|-----------------|---------------------|
| Levy | 4 seasons | Discipline −1/season after duration expires. At Discipline 0: unit disbands. |
| Light Infantry | Unlimited (professional) | Requires Wealth expenditure: −0.5/season (−1 every other season). On Wealth 0: Discipline −1/season. |
| Heavy Infantry | Unlimited (professional) | Requires −1 Wealth/season (expensive equipment maintenance). |
| Cavalry | Unlimited (professional) | Requires −1 Wealth/season. |
| Ranged | Unlimited (professional) | Requires −0.5 Wealth/season. |
| Artillery | Unlimited (professional) | Requires −1.5 Wealth/season (most expensive). |

This makes army composition a genuine strategic decision. Levies are free but temporary — good for defensive campaigns (raise, fight, disband). Professionals are permanent but drain Wealth — sustainable only for wealthy factions. A faction at low Wealth cannot maintain a professional army, which is historically accurate (bankrupted states lose wars because they can't pay soldiers).

**1.3c Morale as social phenomenon.** The current Morale system is a unit stat (floor = 1 while general present). Historical morale was social — armies broke when they saw allied units running, when rumors spread, when supply failed, when leadership was visibly incompetent. Morale cascaded.

**Valoria's gap:** Morale is tracked per-unit in isolation. There's no cascade — one unit routing doesn't affect adjacent units' morale.

**Implication:** Add a **Morale Cascade** rule: when a unit routs (Morale 0), all friendly units in the same engagement make an immediate Discipline check (Ob 1). Failure: Morale −1. This is Ob 1 — most units pass — but it means multiple simultaneous routs create a cascading collapse. This models the historical reality where battles were won or lost when one section of the line broke and panic spread.

---

## §2 — Siege Warfare

### 2.1 Historical Precedents

**The Siege of Constantinople (1453).** 53 days. The Ottomans used massive artillery (Orban's bombard) to breach walls that had resisted every previous siege for a thousand years. Key pattern: technology changes siege dynamics fundamentally. But even with the bombard, the siege succeeded because of logistics — Mehmed could supply his army from Ottoman territory while the defenders were cut off from resupply.

**The Hundred Years' War sieges.** Most territory changed hands through siege, not field battle. English strategy (chevauchée — devastating raids) aimed to undermine the economic base that sustained French garrisons. Key pattern: sieges are won by economics, not by assault. The attacker who can sustain supply longer than the defender wins.

**The Siege of Osaka (1614–1615).** Tokugawa's siege of the Toyotomi stronghold. The castle was essentially impregnable to assault. Tokugawa won through negotiation — filling the moats as a "peace" condition, then attacking the weakened defenses. Key pattern: sieges can be resolved diplomatically, and diplomatic resolution can be as devastating as military assault.

### 2.2 What Valoria Already Has Right

The siege mechanic (§1.9) correctly models:
- Fort Level as defensive strength (Ob = 2 + Fort Level)
- Duration cap (5 seasons maximum)
- Supply cost (Wealth −1/season for attacker)
- Garrison supply runs from adjacent friendly territory
- The "Fort 3 is impregnable to Military 4" calibration (historically accurate — well-fortified positions could not be taken by forces of similar quality)
- The "political or sabotage" counter to impregnable forts (historically accurate — most castles fell through negotiation, treachery, or starvation, not assault)

### 2.3 What's Missing

**Civilian population during siege.** Sieges historically devastated civilian populations — starvation, disease, massacre after breach. The current siege mechanic affects Fort Level and Wealth but not settlement population.

**Implication:** Add settlement consequences: each season of siege, the besieged settlement's Prosperity −1 (starvation, economic collapse). If Prosperity reaches 0 during siege: the population demands surrender — the defending faction must make a Mandate check (Ob 2) to continue. Failure: garrison surrenders. This models the historical dynamic where garrisons were forced to surrender not by military defeat but by civilian pressure.

**Negotiated surrender.** The current siege has two outcomes: reduce Fort Level through Siege action, or Assault. No negotiation option.

**Implication:** Add a **Parley** action during siege: Social Contest between attacker commander and defender commander. If attacker wins: defender surrenders on terms (Accord set to 2 instead of 1 — the population accepted the transition rather than being conquered). If defender wins: siege continues but attacker Stability −1 (the offer of terms was rejected publicly). This is historically common — most sieges ended in negotiated surrender, not storm. The Accord distinction (2 vs 1) makes parley mechanically attractive — a conquered territory at Accord 2 is much easier to govern than one at Accord 1.

---

## §3 — Mustering and Army Composition

### 3.1 Historical Precedents

**The English feudal levy (13th–15th century).** The king summoned vassals who brought their own retinues. Each lord equipped and supplied his own men. The result was a composite army with variable quality and limited central control. The shift to paid soldiers (Indenture system under Edward III) produced more reliable armies but required taxation infrastructure.

**The Swiss pike militia (14th–16th century).** Citizen-soldiers who trained regularly and fought in disciplined formations. They defeated Burgundian heavy cavalry at Grandson and Morat (1476) through training and unit cohesion, not equipment superiority. Key pattern: disciplined militia from a cohesive community can defeat professional armies if their training and morale are high.

**The Ottoman Janissary corps.** Professional soldiers raised from childhood, loyal to the Sultan personally, equipped and paid by the state. They were the most effective infantry in the Mediterranean for 200 years. Key pattern: state-funded professional soldiers outperform feudal levies in sustained campaigns but create political dependency (the Janissaries eventually became kingmakers).

### 3.2 Mapping to Valoria

The existing Muster system captures the basic economics (Prosperity gates unit quality, Wealth gates professional equipment). The Accord → Muster effect table (§4.1 of military_layer) correctly models the political dimension — you can't muster effectively from a hostile population.

**What's missing:** The connection between **settlement type and unit availability.** Historically, different settlements produced different types of soldiers. Castle towns produced garrisoned professionals. Trading cities produced militia. Rural villages produced levies. The existing Muster Prerequisites (§1.5) gate on Prosperity and Wealth but not on settlement type.

**Implication:** Add settlement-type Muster bonuses:

| Settlement Type | Muster Bonus |
|----------------|-------------|
| Fortress | +1 to Muster Size for Heavy Infantry and Cavalry (military infrastructure supports equipping) |
| City / Port | Militia available (a new unit type: Power 2, Discipline 3, Service 4 seasons — better than Levy, cheaper than Light Infantry). Represents armed citizenry. |
| Town | Levy only (standard) |
| Mine | Sapper available (a new unit type: Power 1, Discipline 2, but +2 to Siege actions — mining specialists). Historical precedent: siege mining was done by actual miners. |
| Cathedral | Knights Templar only (existing rule) |
| Outpost | Cannot Muster (too small) |

This creates geographic strategy for military campaigns — where you muster matters, not just whether you can afford to. The faction that controls Fortress settlements has a military infrastructure advantage (better units). The faction that controls Cities has militia (moderate quality, moderate duration — good for defensive campaigns).

---

## §4 — Territory Seizure and Acquisition

### 4.1 Historical Precedents for Non-Military Seizure

**Dynastic marriage and inheritance.** The most common mechanism for territorial transfer in medieval Europe. The Habsburgs built their empire through marriage, not war ("Let others wage war; you, happy Austria, marry"). Key pattern: territorial control transfers through personal relationships and legal frameworks, not military conquest.

**Papal grant and arbitration.** The Pope divided the New World between Spain and Portugal (Treaty of Tordesillas, 1494). Ecclesiastical authority could legitimize territorial claims. Key pattern: a universally-recognized moral authority can arbitrate territorial disputes and make the arbitration stick because all parties recognize the authority.

**Cultural assimilation.** The Roman approach: conquered territories became Roman through roads, law, language, citizenship. Within a generation, the conquered population identified as Roman. Key pattern: governance quality and cultural integration change territorial identity more effectively than military occupation. The territory doesn't just change rulers — it changes identity.

**Economic dependency.** The Hanseatic League controlled Baltic trade without conquering territory. Cities that wanted access to Hanseatic trade networks accepted Hanseatic commercial law and governance. Key pattern: economic power creates governance authority without military action. You don't conquer the territory — you make the territory's economy dependent on your network, and governance follows.

**Treaty of cession after military demonstration.** Most territorial transfers in the 18th–19th century followed military demonstration (not conquest): one side showed it could win, the other ceded territory to avoid the cost of actual defeat. Key pattern: military capability creates bargaining power that translates into territorial transfer without actual battle.

### 4.2 What Valoria Already Has

The faction acquisition toolkits (peninsular_strain §5) already model four patterns:
- **Crown — Formal Crown Treaty** (diplomatic acquisition): maps to treaty of cession
- **Church — Graduated Seizure** (institutional accumulation + PT thresholds): maps to ecclesiastical authority
- **Hafenmark — Dynastic Proclamation** (legal/constitutional claim): maps to dynastic inheritance
- **Varfell — Cultural Reformation** (cultural identity shift): maps to cultural assimilation

### 4.3 What's Missing

**Economic acquisition (Hanseatic pattern).** No faction currently acquires territory through economic dependency. This should be the Guilds' toolkit — or a Hafenmark variant. A territory whose economy depends on trade through Hafenmark-controlled ports should be acquirable through economic leverage, not military or diplomatic means.

**Implication:** Add to peninsular_strain §5 or settlement_layer: **Economic Integration** — when a territory's primary economic output flows through a faction-controlled Port or City (mechanically: ≥ 2 of the territory's settlements have Guild management or the territory is adjacent to a faction-controlled Port), the controlling faction can attempt **Trade Mandate**: Social Contest vs territory governor (Ob = 3 − number of economically-dependent settlements). Success: territory accepts Trade Agreement (Accord +1, faction gains economic coordination rights — not full control, but influence over governance). This is the Hanseatic model: you don't conquer, you make yourself economically indispensable.

**Military demonstration without battle.** Currently, military pressure only matters through actual Battle. But historically, most territorial changes happened through the *threat* of battle, not battle itself. A faction with Military 6 massed on a border should be able to compel concessions without fighting.

**Implication:** Add a **Show of Force** Domain Action: the faction moves units to a territory border but does not declare Battle. If the faction's total military Size in adjacent territories exceeds the defender's garrison Size by ≥ 3: the defender must make a Mandate check (Ob = attacker Military − defender Military, min 1). Failure: defender cedes territory voluntarily (Accord set to 2 — negotiated transfer, not conquest). Success: defender holds, but attacker may then declare Battle normally. This is the gun-boat diplomacy pattern: showing up with overwhelming force and letting the defender calculate the odds.

**Show of Force does NOT trigger IP +2 or Turmoil +1** because no battle occurs. It does trigger RS −0 (no substrate damage). This makes military coercion strategically distinct from actual battle — cheaper in world-state terms, but requires overwhelming local superiority.

---

## §5 — Accord and Governance Legitimacy

### 5.1 Historical Precedents (Weber's Three Types)

Max Weber identified three bases of legitimate authority:

**Traditional authority.** "We've always been governed this way." The Crown's legitimacy in Valoria is traditional — the Almqvist dynasty has ruled since independence. Traditional authority is stable but brittle: once broken (coup, succession crisis), it cannot be reconstructed.

**Rational-legal authority.** "The law says this is how governance works." Hafenmark's parliamentary system is rational-legal. It derives legitimacy from procedure, not personality. Rational-legal authority is resilient (it survives leadership changes) but slow (everything requires procedural justification).

**Charismatic authority.** "This person's extraordinary qualities earn them the right to lead." Vaynard's authority is partly charismatic (his private Thread knowledge makes him seem visionary). RM's Vossen is charismatic (her personal commitment inspires the movement). Charismatic authority is powerful but non-transferable — when the charismatic leader dies, the authority dies with them.

### 5.2 What Valoria Already Has

The Accord system (0–5 in the comprehensive analysis, 0–3 in peninsular_strain) already models governance acceptance. Accord rises through good governance and falls through military conquest. The Turmoil system models the cost of military acquisition (Battle → Strain +1, Accord set to 1 for conquered territory).

### 5.3 What's Missing

**Accord should vary by acquisition method and legitimacy type.** Currently, all non-military acquisition methods set Accord generically. But historically, the *type* of legitimacy the new ruler brings determines how quickly the population accepts governance.

**Implication:** Revise Accord starting values based on acquisition method AND the acquiring faction's legitimacy type:

| Method | Starting Accord | Rationale |
|--------|----------------|-----------|
| Military conquest | 1 (Resistant) | Existing rule. Population resents conquest. |
| Show of Force | 2 (Compliant) | Population accepted transfer to avoid destruction. Grudging but rational. |
| Crown Treaty | 2 (Compliant) | Diplomatic transfer. Population accepts because their existing ruler agreed. |
| Church Seizure (PT ≥ 3) | 2 (Compliant) | Population already religiously aligned. Seizure formalizes existing cultural reality. |
| Church Seizure (PT < 3) | 1 (Resistant) | Population was NOT religiously aligned. Seizure imposed against cultural grain. |
| Hafenmark Dynastic Proclamation | 2 (Compliant) | Legal claim recognized. But population outside Hafenmark may not respect parliamentary authority. |
| Varfell Cultural Reformation | 3 (Aligned) | Population underwent genuine cultural transformation. Slowest method, best Accord. |
| RM Community Organizing | 3 (Aligned) | Population self-organized into RM governance. By definition the highest buy-in. |
| Trade Mandate (proposed) | 2 (Compliant) | Economic dependency. Population accepts because prosperity depends on trade relationship. |
| Parley (proposed siege negotiation) | 2 (Compliant) | Negotiated surrender. Better than conquest. |
| Pastoral Assumption (proposed) | 2 (Compliant) | Vacuum filling. Population accepted because no alternative. |

This makes the acquisition method strategically meaningful beyond the Ob to acquire. A faction that conquers militarily has to spend seasons governing a Resistant population up to Compliant and then Aligned. A faction that acquires through cultural work or economic integration starts with a population that already accepts governance. The victory condition (Accord ≥ 2 in all territories) means military conquest is mechanically possible but requires post-conquest governance investment that other methods avoid.

---

## §6 — Cross-Cutting Audit

### 6.1 Robustness

**Campaign Supply** creates a genuine strategic decision: how long can you sustain offensive operations? Wealthy factions can project power farther; poor factions must fight defensively or conquer quickly.

**Service Duration** for levies creates a time pressure on military campaigns — you have 4 seasons before your levies start degrading. This mirrors the historical constraint that shaped campaign strategy for centuries.

**Morale Cascade** makes battle outcomes less predictable and more dramatic — a single unit breaking can cascade into army-wide collapse, which is historically accurate and creates memorable gameplay moments.

**Settlement-type Muster** makes geography militarily meaningful — controlling a Fortress settlement gives military infrastructure advantages. This integrates the settlement layer with the military layer.

### 6.2 Smoothness

**Campaign Supply** operates at the same scale as existing Wealth mechanics (per-season at Accounting). Integrates cleanly.

**Service Duration** operates per-unit per-season. New tracking overhead, but simple (each Levy unit has a 4-season counter). For BG mode, this could be simplified to: Levy units automatically disband after 4 seasons unless the faction pays Wealth −1 to extend (representing transition from conscript to paid service).

**Morale Cascade** operates within the existing battle turn structure (Phase 6). One additional Discipline check per routing unit. Minimal complexity addition.

**Settlement-type Muster** extends the existing Muster Prerequisites table. No new mechanics — just new entries in an existing table.

**Show of Force** uses existing mechanics (unit Size comparison, Mandate check). No new system.

**Trade Mandate** uses existing Social Contest mechanics. No new system.

**Siege Parley** uses existing Social Contest mechanics with Accord consequence. No new system.

### 6.3 Elegance

| Addition | Elegance Assessment |
|----------|-------------------|
| Campaign Supply | One modifier (Wealth −0.5/season in hostile territory). Simple. **Elegant.** |
| Service Duration | Per-unit counter with type-specific values. Moderate complexity. **Acceptable** — could be simplified for BG mode. |
| Morale Cascade | One check (Discipline Ob 1) triggered by rout. Simple, high-impact. **Elegant.** |
| Settlement Muster | Table extension. No new mechanics. **Elegant.** |
| Show of Force | Size comparison + Mandate check. Two existing mechanics combined. **Elegant.** |
| Trade Mandate | Social Contest with specific trigger conditions. Slightly complex trigger (≥ 2 economically-dependent settlements). **Acceptable.** |
| Siege Parley | Social Contest with Accord consequence. Simple. **Elegant.** |
| Accord by acquisition method | Table lookup, no new mechanics. **Elegant.** |
| Siege civilian consequences | Prosperity −1/season + Mandate check at Prosperity 0. Simple. **Elegant.** |

### 6.4 Priority

**Priority A (simple, high-impact, historically critical):**
1. Campaign Supply — hostile territory costs Wealth
2. Morale Cascade — rout spreads
3. Siege civilian consequences — Prosperity −1/season, surrender pressure
4. Siege Parley — negotiated surrender option
5. Show of Force — military demonstration without battle
6. Accord by acquisition method — differentiated starting Accord

**Priority B (moderate complexity, historically important):**
7. Service Duration — levy term limits, professional pay requirements
8. Settlement Muster bonuses — geography matters for military composition

**Priority C (needs more design work):**
9. Trade Mandate — economic acquisition (needs Guild system integration)
10. Militia and Sapper unit types — new units need balancing

---

## §7 — Interaction with PP-675 (Previous Commit)

The additions here interact with PP-675 additions:

**Campaign Supply + Occupation Era:** During Occupation, Altonian forces are in hostile territory (from Valorian perspective). But Altonia controls its supply lines through the invasion corridor. Altonian units should NOT pay Campaign Supply cost in territories they occupy (they control the supply chain). This means Campaign Supply only applies to Valorian factions operating offensively in Altonian-occupied territory — which creates the correct asymmetry (it's expensive for the resistance to mount conventional military operations in occupied zones).

**Show of Force + IP milestones (PP-675):** Show of Force near the Altonian border could trigger IP visibility effects — the militarization of the border is itself a signal to Altonia. Show of Force against another faction in territories adjacent to the Altonian border should contribute +1 IP (military posturing near the invasion route signals instability).

**Morale Cascade + RM Consensus Delay (PP-675):** If RM governs a territory where a battle occurs, the Consensus Delay mechanic means RM's response to a rout cascade is slower — the community assembly must deliberate before authorizing retreat or reinforcement. This is the structural military weakness of anti-hierarchical governance: when the line breaks, you need instant command decisions, not consensus.

**Siege Parley + Pastoral Assumption (PP-675):** If a siege ends through Parley and the settlement's governor departs, the Church's Pastoral Assumption could immediately install a Church Governor. This creates a dynamic where the Church benefits from military conflicts it doesn't participate in — historically accurate (the medieval Church expanded most effectively during and after wars between secular powers).

---

*This analysis identifies 10 historically-grounded additions to the warfare, mustering, and territory seizure systems. Each is traced to specific historical precedents, mapped to existing Valoria mechanics, audited for robustness/smoothness/elegance, and cross-checked for interactions with PP-675. The "generalship dominates" axiom and formation counter system are validated as historically correct. The primary gaps are logistics/supply, feudal levy service terms, morale cascade, siege negotiation, economic acquisition, and differentiated Accord by acquisition method.*

---

## §8 — Post-Commit Audit: Complexity vs. Narrative Value (2026-04-17)

All additions audited against the core design criterion: does this mechanic contribute to the character↔world feedback loop that generates emergent narrative?

### Committed (simplified where noted):

| Addition | Narrative Value | Simplification |
|----------|----------------|----------------|
| Campaign Supply | Player feels treasury drain from hostile occupation — genuine strategic pressure | Simplified: flat Wealth −1/season for any units in hostile territory (was per-unit-type table) |
| Levy Restriction | Army composition becomes a genuine choice — levies defend, professionals conquer | Simplified: "Levy cannot attack outside home territory" (was 4-season countdown timer) |
| Morale Cascade | Dramatic battle moments — one unit breaks, panic spreads | None needed — already elegant (Discipline Ob 1 check) |
| Siege Civilian Consequences | Moral dimension to siege — civilians suffer, garrison faces surrender pressure | None needed |
| Siege Parley | Most historical sieges ended in negotiation — Accord 2 vs 1 makes the choice meaningful | None needed |
| Show of Force | Military capability as diplomatic leverage — avoids RS/Strain costs of battle | None needed |
| Settlement Muster (Fortress only) | Controlling Fortress settlements is militarily meaningful | Simplified: kept only Fortress +1 Size bonus |
| Accord by Acquisition Method | How you take territory determines how well you govern it — direct feedback loop | None needed |

### Cut (insufficient narrative return for complexity cost):

| Addition | Why Cut |
|----------|---------|
| Militia unit type | Mechanically "slightly better Levy" — no narrative situation it creates that Levy doesn't |
| Sapper unit type | Niche unit for a mechanic (siege mining) that doesn't exist. Zero character↔world feedback |
| Per-unit Campaign Supply costs | Granular tracking without proportional narrative return. One flat rule communicates the same strategic truth |
| Service Duration countdown | Per-unit timer is bookkeeping, not narrative. Levy restriction captures the same truth in one sentence |
| RM Accord ceiling | Invisible cap → player frustration. Hidden Thread-site bonus (kept) communicates the same idea through positive signal |
| Mutual Aid bonus | Small modifier, zero narrative moments |
| Trade Mandate | Premature — needs Guild system that doesn't exist yet |

### Deprioritized (systems already functional, precedent grounding is polish):
- Turmoil cascade precedent
- Social Contest precedent
- Caste system precedent
- Faction collapse/emergence precedent
