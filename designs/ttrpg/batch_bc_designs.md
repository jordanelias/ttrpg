# Phase 1 — Batch B: TTRPG Military Gaps + Batch C: TTRPG Political Gaps
## Date: 2026-03-25 (Session 4)
## Status: Design briefs for editorial review

---

# BATCH B — MILITARY (6 gaps)

---

## G-033: Army Levy / Mustering from Territories

### Problem
No procedure for raising military units from controlled territories. Units appear from nowhere.

### Design

**Mustering procedure (Domain Action, 1 season):**

1. Faction leader or governor declares Muster in a controlled territory.
2. Roll: faction Military vs Ob set by territory conditions.

| Territory Condition | Ob |
|-------|-----|
| Prosperous (Prosperity 7+), no recent combat | 1 |
| Standard (Prosperity 4–6) | 2 |
| Poor (Prosperity 1–3) or recently contested | 3 |
| Under siege or recently conquered | 4 |

3. Results:

| Degree | Outcome |
|--------|---------|
| Overwhelming | Unit raised at full stats + Cohesion bonus (+1) |
| Success | Unit raised at standard stats |
| Partial | Unit raised at −1 Martial and −1 Cohesion (green troops) |
| Failure | Muster fails; territory Prosperity −1 (resentment, draft evasion) |

**Unit stats by type (baseline on successful muster):**

| Type | Martial | Endurance | Cohesion | Notes |
|------|---------|-----------|----------|-------|
| Light Infantry | 3 | 3 | 3 | Default muster result |
| Heavy Infantry | 4 | 4 | 4 | Requires Prosperity 5+, Wealth Ob 2 |
| Cavalry | 4 | 3 | 5 | Requires Prosperity 6+ or relevant History, Wealth Ob 3 |
| Ranged | 3 | 2 | 3 | Requires relevant History or officer with Ranged proficiency |
| Artillery | 2 | 2 | 2 | Requires Wealth Ob 4 + 1 season construction |

**Caps:**
- Maximum units from a single territory = Prosperity ÷ 2 (round up).
- Mustering reduces territory Prosperity by 1 for the season (labor and resources diverted).
- Prosperity recovers +1 per season of peace if territory is controlled and not at cap.

**Narrative constraint:** Troops are people. Mustering from a low-Prosperity territory is pressing peasants into service. This may trigger Revolution Influence +1 in that territory if Prosperity drops below 3 from mustering.

### Canon compliance
- P-07 (Calamity = rendered-side): Military mobilization is a material disruption with economic consequences.
- P-01 (inseparability): Mustering affects Prosperity, which affects TT contribution calculations at high TT.

---

## G-035: Officer Recruitment, Caps, and Maintenance

### Problem
Officers exist in simulations and the VG doc but have no TTRPG recruitment procedure, capacity limits, or upkeep costs.

### Design

**Recruitment:**
- Roll Circles within the appropriate faction/social sphere. Ob by officer quality:

| Officer Quality | Ob | Typical Profile |
|----------------|-----|-----------------|
| Green (all stats 2–3) | 1 | Minor noble's son, retired sergeant |
| Competent (one stat 4+) | 2 | Experienced soldier, ambitious courtier |
| Elite (two stats 4+) | 3 | War veteran, famous knight, renowned scholar |
| Legendary (stat at 5+) | 4 | Campaign-defining figure; GM introduces via narrative |
| Practitioner officer | 3 + TS ≥ 30 requirement | Extremely rare; may not exist at low TT |

- Recruited officers arrive with 1–2 Histories, 1 Belief, 0–1 Inspiration, and a Loyalty score starting at 5.
- Faction Reputation modifies the roll per G-054 (Circles redesign).

**Caps:**
- Maximum named officers per faction = faction Influence ÷ 2 (round up). Minimum 1.
- Rationale: Influence represents organizational depth. A faction with Influence 2 can manage 1 named officer. Influence 8 allows 4.

**Maintenance (seasonal):**
- Each named officer costs 1 Wealth-equivalent per season. This is abstract — it represents pay, equipment, retinue.
- Roll: faction Wealth, Ob = number of officers maintained. Success: all maintained. Partial: choose one officer to go unpaid (Loyalty −1). Failure: all officers Loyalty −1.
- Officers unpaid for 2 consecutive seasons automatically trigger a Loyalty confrontation (see existing Loyalty rules).

**Officer death consequences (retained from existing rules):**
- Bonded officers with Loyalty 7+ to dead officer: −1 Inspiration point.
- Player character may perform Tribute scene: convert dead officer's highest Inspiration into permanent +1D to a relevant History.

---

## G-036: Defection / Cross-Faction Recruitment

### Problem
Officers can defect at Loyalty 0 (existing rule), but there's no procedure for actively recruiting enemy officers.

### Design

**Active recruitment (Domain Action or personal scene):**

1. Identify target officer. Requires: knowing their identity (Intelligence Domain Action or narrative discovery) and their Belief (Intelligence Ob 2 or social scene).
2. Make contact: Circles Ob 2 within the target's social sphere, or personal scene if accessible.
3. Persuade: Social roll (Appeal or Debate).
   - **Appeal** (emotional): Presence + History vs target's Loyalty score as Ob.
   - **Debate** (logical): Cognition + History vs target's Loyalty score as Ob. Rhetoric style matching target's conviction axis gives +1D.

| Degree | Outcome |
|--------|---------|
| Overwhelming | Target defects immediately. Loyalty to new faction starts at 4. Old faction Intelligence: target reveals one hidden attribute. |
| Success | Target's Loyalty to current faction −3. If this brings Loyalty to 0, Confrontation scene fires immediately. |
| Partial | Target's Loyalty −1. They become aware of the offer. May report it (50% chance based on remaining Loyalty). |
| Failure | Target reports recruitment attempt. Current faction Intelligence gains +1 vs recruiting faction for 1 season. Target's Loyalty +1 (rallying effect). |

**Defection consequences:**
- Defecting officer takes knowledge of former faction's strategy: new faction gains +2 Intelligence vs old faction for 1 season.
- Old faction Stability −1 (betrayal shakes cohesion).
- If defecting officer commanded a unit: unit makes Cohesion check Ob 2. Failure: unit disbands. Success: unit remains under new generic commander at −1 Cohesion.

**Counter-intelligence:** A faction with Intelligence ≥ 6 can assign an officer to counter-recruitment watch. Any recruitment attempt against their officers is detected automatically (no surprise). The target officer's Loyalty cannot drop below 2 from external recruitment while watch is active.

---

## G-046: Unit Composition / Formation Mechanics

### Problem
Units are stat blocks with no internal structure. Formations are named (Balanced/Defensive/Offensive/Brutal) but have no composition requirements.

### Design

**Unit composition (optional layer — GM may use simplified stat blocks for minor engagements):**

A unit consists of a base type + optional attachments:

| Attachment | Effect | Requirement |
|-----------|--------|------------|
| Shield wall trained | +1D Cohesion checks when Defensive | Heavy Infantry only; 1 season training |
| Mounted scouts | May reveal enemy disposition before declaration | Cavalry only |
| Sappers | May attempt Fortification damage (see G-047) | Wealth Ob 2; 1 season training |
| Practitioner attached | +1D to Cohesion near Thread events; can perform Thread ops during battle | TS 30+ officer assigned |
| Banner bearer | +1D Rally attempts | Any unit; costs 1 officer slot |

**Formation constraints:**
- Defensive disposition: requires Cohesion 3+ (green troops panic when told to hold).
- Offensive disposition: requires Martial 3+ (poorly armed troops cannot charge effectively).
- Brutal disposition: requires Cohesion 4+ (troops must be disciplined enough to commit atrocities on command without breaking). Brutal against a civilian population: automatic +1 TC if Church observes.
- Flank manoeuvre: requires 2+ friendly units in the same engagement (one pins, one flanks).

**Formation break (refined):**
- On Formation Break: unit's attachments are lost for the remainder of the battle.
- Rallied unit: regains base type stats but not attachments.

### Design rationale
- Attachments add tactical depth without adding stat complexity. Each attachment is a single modifier, not a sub-system.
- Formation constraints prevent absurd combinations (green conscripts attempting Brutal).
- Attachment loss on break creates meaningful risk — elite attachments are valuable and fragile.

---

## G-056: Supply Lines / Logistics

### Problem
VG doc mentions supply attrition (−1 Endurance per season if >2 territories from friendly supply). No TTRPG procedure.

### Design

**Supply check (seasonal, during accounting):**

Each unit checks supply status:
- **Supplied:** Within 2 territories of a friendly-controlled territory with Prosperity 3+. No penalty.
- **Strained:** 3 territories from supply, or supply territory has Prosperity 1–2. Unit: −1D to all rolls next season.
- **Cut off:** No connected friendly territory with Prosperity 1+, or route physically blocked by enemy. Unit: −1 Endurance per season (cumulative). Cohesion check Ob 1 each season or Loyalty −1 (for officer-led units) / Cohesion −1 (for generic).

**Supply route interdiction (Domain Action):**
- Attacker rolls Intelligence vs defender's Military ÷ 2.
- Success: one enemy supply route is blocked for 1 season.
- Overwhelming: blocked + defender's unit in that territory is unaware (no Cohesion check warning).
- Failure: interdiction detected; defender may reinforce the route.

**Foraging (officer Domain Action):**
- Roll relevant History (Survival, Campaign Veteran, etc.) Ob = 2 in fertile territory, Ob 3 in poor territory, Ob 4 in winter/mountain.
- Success: supply status improves one step for 1 season.
- Failure: local population hostile — territory Prosperity −1, potential Revolution Influence +1.

**Strategic implication:** Long campaigns across the peninsula require supply management. A faction that conquers distant territories without securing supply routes will lose units to attrition, not combat. This incentivizes alliance, trade agreements with Schoenland, and strategic territory selection.

---

## G-045: Knights Templar Organizational Mechanics

### Problem
The Templars are described narratively (Church military arm, deployed by Cardinal of Fortitude) but have no organizational rules.

### Design

**Templar structure:**
- The Knights Templar are a Church military asset, not an independent faction.
- Total Templar strength = Church Military score × 2 (in unit-equivalents). At Church Military 6: 12 unit-equivalents, organizeable into 3–4 named units.
- Commanded by the Cardinal of Fortitude (NPC) or a PC Templar knight if one exists.

**Deployment authorization:**
- Templars deploy only on Church orders (Cardinal of Fortitude Domain Action).
- Deployment without ducal/Crown authorization: TC +2 per deployment.
- Deployment WITH authorization: TC +0, but Crown Mandate −1 (appearing to submit to Church military direction).

**Templar unit stats:**

| Stat | Value | Notes |
|------|-------|-------|
| Martial | 5 | Elite heavy infantry |
| Endurance | 5 | Fanatical endurance |
| Cohesion | 6 | Religious discipline; +1D vs Thread-related Cohesion checks |
| Special | Immune to Brutal disposition morale effects | Faith-based resilience |

**Templar limitations:**
- Cannot be mustered from territories (they are a standing order, not levied).
- Cannot be recruited by non-Church factions (Loyalty is to the institution, not a person).
- Losses are permanent within a campaign arc — the order does not replenish quickly. Destroyed Templar units can only be rebuilt at rate of 1 per 3 seasons, requiring Church Wealth Ob 3.
- Templar officers have the Devout Constraint (cannot develop TS). If a Templar officer somehow loses the Devout Constraint, they are expelled from the order (automatic defection to whichever faction the GM determines is appropriate).

**Templar interactions with Thread events:**
- Templars near a Gap or monstrous entity: +1D Cohesion checks (their theology gives them a framework, even if wrong).
- Templars ordered to destroy an Einhir site: automatic success (they are trained for this). TT +3. TC +1 (zealotry visible to population).

**Heresy enforcement:**
- Templars may be deployed to enforce a Heresy conviction: arrest a target. Roll Templar unit Martial vs target's faction Military ÷ 2. Success: target arrested. Failure: target escapes; TC +1 (public spectacle of Church failure).

### Canon compliance
- P-03 (rendering = consciousness): Templars' theological framework is a rendering that functions defensively but prevents Thread development.
- P-04 (monstrosity ≠ moral): Templars treat all Thread phenomena as monstrous — this is canonically incorrect but mechanically coherent within their worldview.

---

# BATCH C — POLITICAL (8 gaps)

---

## G-041: Non-Leader Faction Membership Mechanics

### Problem
PCs who aren't faction leaders have no mechanical relationship with their faction beyond narrative affiliation.

### Design

**Faction membership (for non-leader PCs):**

Each PC may declare faction affiliation (or none) at character creation. Membership provides:

| Benefit | Mechanic |
|---------|----------|
| Circles bonus within faction | +1D to Circles rolls targeting faction contacts |
| Resources access | May attempt faction Resources (faction Wealth pool) at +1 Ob for personal-scale faction-appropriate purchases |
| Information | Automatically learns public faction attribute changes at seasonal accounting |
| Protection | Faction provides legal/social cover — Heresy investigation Ob +1 if faction has Influence 5+ |

| Cost | Mechanic |
|------|----------|
| Obligation | GM may call one faction-obligation scene per season (deliver a message, attend a meeting, vote a certain way). Refusing: Reputation −1 with faction. |
| Exposure | Actions against affiliated faction's interests: Reputation −2 (betrayal is worse than disinterest). |
| Visibility | Affiliated PCs are known associates. Enemy factions may target them as leverage. |

**Leaving a faction:** Declare departure. Reputation with former faction −3 immediately. If faction has Intelligence 5+: departure is tracked and former faction gains +1D to Intelligence actions against the character for 2 seasons.

**Unaffiliated PCs:** No Circles bonus, no faction Resources access, no obligation. May join a faction mid-campaign through Circles Ob 2 + one scene of genuine service.

---

## G-042: Faction Creation by Players

### Problem
No procedure for PCs to found a new faction.

### Design

**Prerequisites:**
1. At least 1 controlled territory (or control of a significant non-territorial power base — e.g., a guild network, a religious movement).
2. At least 3 named NPCs with Loyalty 5+ to the founding PC (the nucleus of institutional capacity).
3. A declared Mandate (public statement of purpose — this becomes the faction's starting Belief-equivalent).
4. [EDITORIAL: Should founding a faction require spending CP, or is it purely narrative + mechanical prerequisites?]

**Founding procedure:**
1. PC declares faction publicly (or covertly — covert factions have Influence but no Mandate until revealed).
2. Set starting attributes:

| Attribute | Starting Value |
|-----------|---------------|
| Mandate | 1 (or 0 if covert) |
| Influence | = founding PC's Circles ÷ 2 (round up; min 1) |
| Wealth | = founding PC's Resources ÷ 2 (round up; min 1) |
| Military | 0 (must be mustered) |
| Intelligence | = founding PC's highest relevant History ÷ 2 (round up; min 1) |
| Stability | 3 (new organizations are fragile) |

3. Faction enters play at next seasonal accounting.

**Growth constraints:**
- New factions cannot exceed attribute 5 in any score for their first 2 seasons (institutional immaturity).
- Mandate grows only through public action — Domain Echoes, successful Appeals, or narrative events.
- Other factions react: founding a new faction automatically triggers a Stability check for each existing faction in the same territory (political disruption).

---

## G-043: NPC Faction Elevation to PC Status

### Problem
When a significant NPC or NPC-led group becomes important enough to warrant PC-level control, there's no procedure.

### Design

**Triggers for elevation:**
- An NPC faction reaches Influence 3+ and Stability 3+ (institutional viability).
- A player's character dies and the player wants to take over an existing NPC faction leader.
- The GM determines an NPC faction has become a significant campaign actor.

**Procedure:**
1. GM and player agree on elevation.
2. NPC faction's attributes transfer unchanged.
3. The NPC faction leader becomes a full PC with: existing stats (if established), or stats generated using standard character creation if only narrative stats existed.
4. The NPC faction leader's Beliefs are rewritten by the new controlling player (reflecting the shift from GM-driven to player-driven motivation).
5. Existing Loyalty scores of officers toward the NPC-leader transfer.
6. The faction's ethical framework tendency remains (institutional inertia) but the new PC leader may deviate from it (leader ≠ institution, per editorial decision).

**Constraint:** Elevation is a one-way door. Once a faction has a PC leader, it cannot revert to NPC status without the PC dying, retiring, or being deposed.

---

## G-038: Alliance / Treaty / Betrayal Mechanics

### Problem
Factions interact but there's no mechanical framework for formal agreements between them.

### Design

**Alliance formation:**
1. Both faction leaders (PC or NPC) agree to terms in a scene (social roll not required for voluntary agreement; required if one party is reluctant).
2. Terms are recorded as a **Treaty Card** with:
   - Parties
   - Obligations (e.g., "military support if attacked," "trade rights in territory X," "non-aggression for 4 seasons")
   - Duration (fixed seasons, or until broken)
   - Penalty clause (what happens on violation)

**Treaty types:**

| Type | Typical Obligations | Typical Duration |
|------|-------------------|-----------------|
| Non-aggression pact | No military action against each other | 4 seasons |
| Military alliance | Mutual defense; contribute units if partner attacked | Until broken |
| Trade agreement | +1 Wealth to both factions per season; shared supply lines | 2 seasons, renewable |
| Intelligence sharing | Reveal one hidden attribute per season | 2 seasons |
| Vassalage | Subordinate faction contributes Military/Wealth; superior provides protection | Permanent until revolt |

**Treaty enforcement:**
- Treaties are enforced by Reputation. Breaking a treaty: Reputation −3 with the betrayed faction AND Reputation −1 with all other factions that witnessed the treaty (word spreads).
- NPC factions: GM rolls Loyalty-equivalent check each season to determine if they honor the treaty. Ob = number of seasons remaining. At Ob 4+: NPC factions become unreliable.

**Betrayal:**
- A faction may break a treaty at any time by declaration.
- The betraying faction gains the initiative advantage (first strike in any resulting military engagement).
- The betrayed faction gains: Mandate +1 (sympathy), and may immediately declare war without casus belli (see G-039).
- [EDITORIAL: Should treaty-breaking have a mechanical Stability cost for the betrayer beyond Reputation? Suggested: Stability −1 for the betraying faction (internal dissent from those who valued the agreement).]

---

## G-039: Casus Belli / War Justification

### Problem
Factions can attack each other freely. There's no political cost for unjustified aggression and no benefit for justified war.

### Design

**Casus belli categories:**

| Category | Example | Mandate Effect |
|----------|---------|---------------|
| Treaty violation | Ally breaks agreement | Attacker: Mandate +1. Defender: no penalty. |
| Territorial claim | Historical claim to contested territory | Attacker: no Mandate change. Defender: no change. |
| Religious mandate | Church authorizes action against heretics | Attacker: Mandate +1 if Church Mandate > 5. TC +1. |
| Defensive war | Responding to attack | Defender: Mandate +2. Attacker: Mandate −1. |
| Unprovoked aggression | No justification | Attacker: Mandate −2. All non-allied factions: Reputation toward attacker −1. |
| Retribution | Response to assassination, sabotage, or espionage | Attacker: Mandate +0 (public understands). If evidence is fabricated: Mandate −3 when exposed. |

**Declaration procedure:**
1. Faction leader declares war publicly (or initiates military action — undeclared war is treated as unprovoked aggression).
2. GM assesses casus belli category.
3. Mandate adjustments applied immediately.
4. Other factions react: each non-involved faction makes a Stability check (Ob 1). Failure: they are drawn toward a side based on ethical framework alignment.

**War termination:**
- Negotiated peace: both sides agree in a scene. Treaty Card created.
- Unconditional surrender: losing faction's Mandate drops to 0. Victor determines terms.
- Exhaustion: both factions' Military at 2 or below. Automatic ceasefire for 2 seasons (neither can sustain operations).

---

## G-037: Territory Governance After Conquest

### Problem
When a faction conquers a territory, there's no procedure for what happens to its governance, population, or economy.

### Design

**Immediate effects of conquest:**
- Territory control transfers to conquering faction.
- Prosperity −1 (war damage).
- Fortification −1 level (siege damage, if siege occurred).
- Church Presence: unchanged (the Church transcends political control — this is a key setting element).
- Previous controller's Circles contacts in territory: burned (Network Damage per G-054 for any PC with contacts there).

**Governance establishment (Domain Action, required within 1 season of conquest):**

Roll: faction Influence vs Ob set by population resistance.

| Condition | Ob |
|-----------|----|
| Population was hostile to previous controller | 1 |
| Population was neutral | 2 |
| Population was loyal to previous controller | 3 |
| Conquest was Brutal (Brutal disposition used in final battle) | +1 |
| Conqueror shares ethical framework with population | −1 |

| Degree | Outcome |
|--------|---------|
| Overwhelming | Governance established; Prosperity recovers +1 immediately; population accepts |
| Success | Governance established; standard recovery |
| Partial | Governance established but unstable: Stability check Ob 2 each season for 2 seasons |
| Failure | Resistance movement forms: Revolution Influence +2 in territory; guerrilla actions possible |

**Ongoing governance:**
- Governed territory contributes to faction Wealth and Military mustering as normal.
- Ungoverned territory (no establishment roll or failed): contributes nothing; costs 1 Military unit to garrison or it reverts to neutral.

---

## G-044: Altonian Presence Pre-Invasion

### Problem
Altonia is described as an external threat with a clock, but there's no mechanical presence before the invasion fires. Players can't interact with it.

### Design

**Altonian presence by IP range:**

| IP Range | Presence | Mechanical Expression |
|----------|----------|----------------------|
| 0–29 (Dormant) | Trade delegations, cultural exchange | Schoenland trade active (+1 Wealth to coastal territories). Altonian spies present but inactive (GM layer only). |
| 30–44 (Aggressive) | Economic pressure, diplomatic demands | Schoenland trade conditional (requires Influence Ob 2 to maintain). Altonian ambassador makes demands: 1 per season, escalating. Refusal: IP +1. Compliance: Crown Mandate −1 (appearing weak). |
| 45–59 (Hostile) | Border skirmishes, proxy operations | Altonian-funded proxy units appear in Border Pass territory (Martial 3, Endurance 3, Cohesion 4). 1 unit per 2 seasons. They attack whoever controls Border Pass. Niflhel receives Altonian Intelligence support: +1D to Niflhel Intelligence Domain Actions. |
| 60–74 (Warlike) | Invasion preparation visible | Altonian army assembles at Border Pass (visible to any faction with Intelligence 4+). Diplomatic Resolution becomes possible if conditions met. All Valorian factions receive IP notification at seasonal accounting. |
| 75–99 (Imminent) | Active military presence | Altonian vanguard (1 elite unit: Martial 6, Endurance 5, Cohesion 7) enters Border Pass. Engages any faction present. Schoenland trade suspended. |
| 100 (Invasion) | Full invasion force | See existing rules. |

**Player interaction with Altonia (pre-invasion):**
- **Diplomacy:** At IP 30+, any faction may attempt to negotiate with Altonia. Circles Ob 3 to contact Altonian representative. Social scene resolves as Appeal or Debate vs Altonian representative's conviction (Order-leaning; Forensic arguments +1D).
- **Espionage:** Intelligence Domain Action vs Altonia: Ob 4 (they are a major power). Success reveals: current IP acceleration sources, which internal faction is dominant, and whether diplomatic resolution conditions are met.
- **Sabotage:** At IP 60+, a faction may attempt to delay invasion by sabotaging Altonian supply lines. Intelligence Ob 5. Success: IP −2. Failure: IP +1 (provocation).
- **Alliance offer:** A faction may offer vassalage to Altonia to redirect invasion elsewhere. Influence Ob 3 + Crown Mandate must be below 3 (Altonia only accepts broken states). Success: faction becomes Altonian client state — IP frozen but faction loses sovereignty (cannot make treaties, must contribute Military to Altonian interests). [EDITORIAL: Is this option too politically extreme to include, or is it a valid dark-path choice?]

---

## G-055: Southernmost Expedition Procedures

### Problem
The Southernmost is described as a late-game region with Thread significance. No procedure for organizing and executing an expedition there.

### Design

**Prerequisites:**
- TT ≥ 40 (the Southernmost is dormant below this — nothing to find).
- At least one PC or officer with TS 30+ (can perceive Thread structures).
- At least one PC or officer with relevant History (Einhir Scholar, Natural Philosophy, Expedition Leader). Ob 3 to plan the expedition.
- Resources Ob 3 (expedition supplies for hostile terrain).
- Military escort recommended (1+ units; the Southernmost has hostile configurations).

**Expedition structure (multi-season extended action):**

| Season | Phase | Procedure |
|--------|-------|-----------|
| 1 | Approach | Travel to Southernmost border territory. Cohesion check Ob 1 for military escort (Thread proximity unsettles troops). TS 30+ character: automatic Discovery Event. |
| 2 | Exploration | Enter Southernmost. Zone-based exploration (3 zones to traverse). Each zone: one encounter (Thread phenomenon, hostile entity, or environmental hazard). Resolution: per combat or Thread operation rules. |
| 3 | Discovery | Reach the primary site (the locus of the original Einhir catastrophe). Practitioner with TS 50+: Diagnosis automatically reveals the nature of the damage. Below TS 50: Diagnosis Ob 3 to gain partial understanding. |
| 4+ | Repair (optional) | Extraordinary Weaving per existing rules. Each season of successful Weaving: TT −2 permanent from Southernmost contribution. |

**Hazards per zone:**

| Zone | Primary Hazard | Mechanic |
|------|---------------|----------|
| Border zone | Shifting Objects | Object-scale Thread operation or Agility Ob 2 to avoid |
| Inner zone | Gap incursion | Monstrous entity (Mode 1 or 2). Mass combat or personal combat depending on scale. |
| Core zone | Configuration instability | All non-practitioners: Spirit check Ob 2 or Certainty −1 per round of exposure. Practitioners: Contact duration halved (Thread density interferes). |

**Expedition failure:**
- If military escort routes or all practitioners are incapacitated: expedition retreats. All participants: Certainty −1. TT +1 (disturbing the Southernmost without completing the work).
- Retreat can be attempted at any zone. Retreating from Core zone: Agility Ob 2 or additional encounter.

**Expedition success indicators:**
- Diagnosis complete: Southernmost's Thread signature is understood. This is required for Extraordinary Weaving.
- Each successful Extraordinary Weaving season: TT permanent reduction. After 4–5 successful seasons: Southernmost fully stabilized (see VG doc's repair arc).

### Canon compliance
- P-02 (Ein Sof = fullness): The Southernmost's damage is a failure of rendering, not an absence. The expedition discovers this directly.
- P-06 (Threadcut = is without becoming): The Southernmost's locked configurations are Threadcut zones — visible to practitioners as static rather than dynamic.
- P-13 (Forgetting = rendering failure): The expedition confronts the Forgetting directly — the reason the peninsula doesn't remember the catastrophe becomes mechanically relevant.

---

# BATCH B+C SUMMARY

| Gap | Batch | Status | Editorial Flags |
|-----|-------|--------|----------------|
| G-033 | B | Designed | None |
| G-035 | B | Designed | None |
| G-036 | B | Designed | Treaty-break Stability cost? |
| G-046 | B | Designed | None |
| G-056 | B | Designed | None |
| G-045 | B | Designed | None |
| G-041 | C | Designed | None |
| G-042 | C | Designed | Should founding a faction cost CP? |
| G-043 | C | Designed | None |
| G-038 | C | Designed | Treaty-break Stability −1 for betrayer? |
| G-039 | C | Designed | None |
| G-037 | C | Designed | None |
| G-044 | C | Designed | Altonian vassalage option — include or cut? |
| G-055 | C | Designed | None |

**Editorial decisions needed: 4**
1. **G-042:** Should founding a new faction cost CP (e.g., 10 CP), or is it purely narrative + mechanical prerequisites?
2. **G-038:** Should treaty-breaking cost the betrayer Stability −1 (internal dissent)?
3. **G-044:** Should the Altonian vassalage option (a faction can submit to Altonia to redirect invasion) be included as a valid dark-path choice?
4. **G-036 + G-038 share a question:** The Reputation penalty for treaty-breaking (−3 with betrayed, −1 with witnesses) is the primary enforcement. Is additional Stability cost redundant, or does it add meaningful weight?

**Gaps designed this batch: 14 (6 military + 8 political)**
**Total Phase 1 gaps designed (A+B+C): 21 of 51**
