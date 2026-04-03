# WORLDBUILDING INTEGRATION v1 — Lore-to-Mechanics
## Source: Pre-project lore documents (Church, Löwenritter, Crown, Guilds, Economy, Governance)
## Date: 2026-04-02
## Authority: DESIGN (working document). Proposals require integration into canonical stage6, stage7, stage13, params files.
## Skeleton format: tables, formulas, procedures, edge cases. No explanatory prose.

---

# 1. GALBADOS → SOLMUND RENAME

**Scope:** All references to "Galbados" become "Solmund" across the repo. "The Church of Galbados" → "The Church of Solmund." Calendar epoch "BG (Before Galbados)" → "BS (Before Solmund)." "AG (After Galbados)" → "AS (After Solmund)."

**Name:** Solmund, The First Founder.

**Exception:** The Almaic Kyriakos (Altonian religious institution) retains its own name — no rename needed.

**Affected files:** Every file containing "Galbados." Haiku-tier cleanup task. Run after all other changes in this document are committed.

[EDITORIAL: ED-NEW-01 — Confirm "Solmund" as final canonical name for The First Founder. User stated "Galbados is now Solmund" but formal confirmation needed before repo-wide rename.]

---

# 2. NAME DISCREPANCIES

| Character | Lore Name | Current Design Name | Resolution |
|-----------|-----------|-------------------|------------|
| Duke of Varfell | Dienton Vaynard ("The White Wolf") | Magnus Vaynard | [EDITORIAL: ED-NEW-02 — Which name is canonical? Lore says Dienton. Design says Magnus. Lore also gives epithet "The White Wolf" and notes military prowess + progressive policies.] |
| Duchess of Hafenmark | Inga Baralta | Inge Baralta | Minor spelling variant. Lore uses "Inga"; design uses "Inge." [EDITORIAL: ED-NEW-03 — Confirm spelling.] |
| King | Almqvist (no first name in lore body) / "King Almqvist" | Almud Almqvist | No conflict. Lore confirms surname. |
| Confessor | "The Holy See" (title) | Confessor Arne Himlensendt | No conflict. "Holy See" = lore title for role; "Confessor" = design title. [EDITORIAL: ED-NEW-04 — Should the title be "Holy See" or "Confessor"? Lore uses "Holy See" consistently. Design uses "Confessor." These are different registers. Recommend: "The Holy See" as formal title, "Confessor" as mode-of-address — both canonical.] |
| Varfell territory "Oastad" | Oastad | Vargstad (PP-199 territory map) | Lore says Varfell contains "Oastad." PP-199 definitive map uses "Vargstad" for T4. [EDITORIAL: ED-NEW-05 — Confirm T4 name: Oastad (lore) or Vargstad (PP-199)?] |
| Valorsmark composition | Valorsplatz, Lowenskyst, Himmelenger, Arcansheld, Stillhelm | T8 Lowenskyst = Hafenmark per PP-199 | Lore assigns Lowenskyst to Valorsmark. PP-199 map assigns it to Hafenmark. Map is authoritative for BG territory control. Lore may reflect historical claim vs current control. No conflict if framed as: Lowenskyst was historically Valorsmark, transferred to Hafenmark in post-Secession settlement. |

---

# 3. CHURCH OF SOLMUND — FOUR-CARDINAL SUB-ARM STRUCTURE

## 3.1 Structure

The Church operates through four arms, each governed by a Cardinal appointed by the Holy See (Confessor). This mirrors Niflhel's four-arm decentralised structure but is hierarchical rather than horizontal.

| Cardinal | Title | Arm | Portfolio |
|----------|-------|-----|-----------|
| Cardinal of Fortitude | Commands the Knights Templar | Military Arm | Church military operations, enforcement of Solmund's justice, monstrous incursion suppression |
| Cardinal of Justice | Oversees the Grand Adjudication and the Inquisitors | Judicial Arm | Heresy investigation, religious courts, excommunication recommendations, text suppression |
| Cardinal of Prudence | Oversees tithes and charities | Economic Arm | Tithe collection, charitable foundations, poor relief, Church land management |
| Cardinal of Temperance | Oversees scholarly institutions | Knowledge Arm | Universities, observatories, monasteries, archive management |

### Named Cardinals (from stage13)

| Cardinal | Name | Arm | Key Trait |
|----------|------|-----|-----------|
| Justice | Arnlod Olafsson | Judicial | Active Niflhel connection. Uses Niflhel to suppress texts. |
| Temperance (Scholarship) | Magnus Klapp | Knowledge | Thread Sensitivity (TS) 31. Approaching Stirring. Contact with originary locks. |
| Fortitude (Military) | Osten Jarnstal | Military | Believes Templars should be independent of political authority. Drifting toward unilateral action. |
| Prudence | [UNNAMED] | Economic | [EDITORIAL: ED-NEW-06 — Name and profile for Cardinal of Prudence. This is the fourth Cardinal referenced in ED-007. Controls tithes, charities, Church economic operations. Mechanical profile needed.] |

## 3.2 Cardinal Mechanics (TTRPG)

Each Cardinal controls an institutional sub-pool drawn from Church faction stats. Cardinals act as officers — they cannot override the Holy See but can act independently within their portfolio.

**Cardinal Authority Pool:** Each Cardinal rolls their arm's relevant Church stat when acting within portfolio:

| Cardinal | Pool Source | Typical Domain Actions |
|----------|-----------|----------------------|
| Fortitude | Church Military | Deploy Templars, suppress monstrous incursion, garrison territory |
| Justice | Church Intel (proxy — Inquisitors operate as intelligence) | Heresy Investigation, text suppression, evidence gathering |
| Prudence | Church Wealth | Tithe collection, charity deployment, economic pressure |
| Temperance | Church Influence | University policy, scholarly appointments, archive access control |

**Cardinal Independence Check:** When a Cardinal acts against the Holy See's explicit instruction, roll Cardinal's relevant pool vs Ob 3. Success: action proceeds, Church Stability −1. Failure: action blocked, no Stability cost.

**Jarnstal Drift Mechanic:** Each season Jarnstal acts without explicit Holy See authorisation (deploying Templars unilaterally, refusing to stand down from a territory): increment a private Jarnstal Independence Counter (0–3, Game Master-tracked). At 3: Jarnstal issues a public declaration of Templar operational independence from civil authority. Effects:
- Church Stability −2 (institutional fracture)
- Church Military remains at current value but is now controlled by Jarnstal, not the Holy See
- Theocracy Counter +2 (Templars acting as autonomous religious military = theocratic acceleration)
- Crown must respond: Royal Decree or Parliamentary Vote to address Templar independence, or Löwenritter confrontation

**Klapp Awakening Mechanic:** Already in stage13. Thread Sensitivity (TS) 31, one more sustained encounter triggers growth check. If successful:
- Church Knowledge Arm becomes internally compromised — Klapp begins selectively protecting Thread-significant texts instead of suppressing them
- Church Intel (via Olafsson's Inquisitors) eventually detects the protection pattern: triggers internal Heresy Investigation against Klapp
- If Klapp is investigated before players intervene: Church Stability −1, Theocracy Counter +1 (internal purge)
- If players extract or protect Klapp: Church loses Knowledge Arm effectiveness (−1D on all Church Influence rolls related to scholarly institutions)

**Olafsson-Niflhel Exposure:** Already in stage13 (Baralta evidence mechanic). Lore confirms: Olafsson uses Niflhel resources for text suppression. The Inquisitors were designed to perform exactly this function.

## 3.3 Cardinal Mechanics (Board Game)

Cardinals are abstracted to modifiers on Church Domain Actions:

| Cardinal | BG Effect |
|----------|-----------|
| Fortitude | Church Military actions: −1 Ob when deploying Templars |
| Justice | Heresy Investigation: Church gains +1D |
| Prudence | Church Wealth generation: +1 Wealth/season from tithe territories |
| Temperance | Church Influence in university territories: −1 Ob |

**BG Cardinal Loss:** If a Cardinal is removed (investigation, assassination, defection), the corresponding modifier is lost until a replacement is appointed. Replacement: Church spends 1 Influence + 1 Stability at seasonal accounting.

## 3.4 Church Levy Rules

From lore: The Church maintains levies in cathedrals across every major city. Two-thirds of those levies can be raised by the King at any given moment. The Church is taxed on its owned lands.

**Mechanical translation:**

| Rule | TTRPG | Board Game |
|------|-------|------------|
| Church levy raising | Crown may requisition Church Military as bonus dice (+Church Military × 2/3, round down) for one military Domain Action per season. Requires Royal Decree or Parliamentary Vote. | Crown Muster in a territory with Church presence: +1D (represents levy requisition). |
| Church refusal | If Church refuses levy call: Crown Mandate vs Church Mandate contested roll. Crown success: levies raised, Church Stability −1. Crown failure: levies not raised, Crown Mandate −1. | Church player may spend 1 Stability to block Crown levy bonus in one territory. |
| Church land taxation | Church-controlled territories generate Wealth for Church AND pay tax to Crown (Crown gains +1 Wealth/season per Church-controlled territory with Prosperity ≥ 4). | Same — flat +1 Wealth to Crown from Church territories at Prosperity 4+. |

## 3.5 Excommunication Procedure (Enriched)

Lore adds: Excommunication is recommended by the Cardinal of Justice. Excommunicated people must pay penance and perform public service. Some cases warrant banishment.

**Revision to stage6 §8.3 Excommunication:**

Add pre-roll step: Cardinal of Justice must recommend excommunication (automatic if Heresy Investigation conviction reached; otherwise requires Church Intel vs Ob 2 to build a case).

Add post-excommunication resolution paths:

| Path | Ob | Effect |
|------|-----|--------|
| Penance (voluntary submission) | None — target accepts | Target regains Church standing after 1 season of public service. Mandate restored. Church Mandate +1 (demonstration of authority). |
| Grand Debate (challenge) | 5 exchanges | As currently specified. |
| Banishment (Game Master determination) | Church Mandate vs Ob 4 | Target permanently expelled. Cannot hold public office in Church-aligned territories. If target is a faction leader: faction Stability −2, Mandate −1. |

## 3.6 Almaic Kyriakos (New — Altonian Religious Institution)

From lore: The Church of Solmund "exists in opposition to the major religious institution of Altonia, the Almaic Kyriakos," and "exhibits growing influence within Altonia's borders."

**Mechanical relevance:**
- Church influence within Altonia reduces Institutional Pressure (IP) at certain thresholds (Altonian internal religious division weakens imperial cohesion)
- At IP 50+, the Almaic Kyriakos may request Church cooperation against shared threats — creating an unlikely Church-Altonia alignment that destabilises all other factions

| IP Threshold | Almaic Kyriakos Effect |
|-------------|----------------------|
| IP 30 | Church Altonian missionaries quietly benefit from normalised movement (already in timeline). No mechanical effect. |
| IP 50 | Almaic Kyriakos envoy arrives. Church may choose: cooperate (IP −3, Theocracy Counter +2 — Church gains cross-border legitimacy) or refuse (no effect). |
| IP 65 | If Church cooperated at 50: Almaic Kyriakos formally recognises Church authority over Valn Peninsula spiritual matters. Theocracy Counter +5. IP −5 (Altonia internally divided). |
| IP 75+ | If Church refused: Almaic Kyriakos supports Altonian invasion as religious mandate. IP escalation proceeds normally. |

[EDITORIAL: ED-NEW-07 — Almaic Kyriakos interaction at IP thresholds. Enriches the IP escalation ladder with a Church-specific diplomatic path. Needs simulation to confirm balance.]

---

# 4. LÖWENRITTER INTERNAL STRUCTURE

## 4.1 Structure

From lore: The Löwenritter is overseen by The Lions' Council and divided into:

| Arm | Name | Function |
|-----|------|----------|
| Military | The Lions' Table | Coordination and operation of military levies. Appoints the Royal Guard. |
| Naval | The Lions' Helm | Naval affairs. |
| Civic — Law Enforcement | Knights of the Peace | Patrol the kingdom, aide civilians, resolve disputes, protect roads/borders, enforce law. |
| Civic — Investigation | Royal Investigators | Investigate wrongdoings, counter-espionage, bring people before courts. |
| Extralegal | The Riskbreakers | Operate outside the law to infiltrate and root out cults and criminal organisations. Loyal to Valoria the concept, not the institutions or the Crown. |

**Lions' Council:** Oversees all arms. Chaired by the Grandmaster (Ehrenwall). The Council is the command structure — Ehrenwall commands through it, not around it.

## 4.2 Arm Mechanics (TTRPG)

Each arm draws from the Löwenritter's faction stats but operates in a distinct domain:

| Arm | Primary Stat | Domain Actions Available |
|-----|-------------|------------------------|
| Lions' Table | Military | Muster, Deploy, Garrison, Battle coordination, Royal Guard assignment |
| Lions' Helm | Military (naval subset) | Naval patrol, sea route security, blockade, Schoenland trade escort |
| Knights of the Peace | Influence | Road patrol, civilian protection, dispute resolution, border enforcement, law enforcement |
| Royal Investigators | Intel | Investigation, counter-espionage, evidence gathering, court prosecution |
| Riskbreakers | Intel | Infiltration, cult disruption, criminal organisation takedown, deniable operations |

**Royal Guard:** Appointed by Lions' Table. Protects Imperial Court members. Mechanical effect: any assassination attempt targeting a Court member while Royal Guard is active requires +2 Ob.

**Knights of the Peace — Territory Presence:** Each territory with an active Knight of the Peace patrol gains:
- +1 Ob to all Covert Domain Actions by hostile factions in that territory
- Dispute resolution: if two factions contest a non-military matter in that territory, Knights of the Peace may mediate (Löwenritter Influence vs Ob 2; success: both sides accept ruling, no faction stat changes)

**Lions' Helm — Naval Mechanics:**

| Action | Pool | Ob | Effect |
|--------|------|-----|--------|
| Secure Sea Route | Military | 2 | Schoenland trade route protected. Trade +1D for Crown and allies using the route. |
| Naval Blockade | Military | Target's Military | Target faction cannot use sea routes this season. Schoenland trade suspended for that faction. |
| Coastal Defence | Military | IP ÷ 20 (round up) | At IP 75+: Lions' Helm opposes Altonian naval approach. Success: IP escalation delayed 1 season. Failure: coastal territory vulnerable. |

**Riskbreaker Identity (resolves ED-006):**

From lore: "Riskbreakers are technically under Löwenritter, but they are loyal to Valoria the concept, not the institutions or the crown itself."

This creates a structural fault line. The Riskbreakers serve the Löwenritter's command structure but their loyalty is ideological, not institutional. They will disobey orders that they believe harm Valoria — including orders from Ehrenwall if the coup would damage the nation.

**Riskbreaker Loyalty Divergence:** Riskbreakers have a hidden Conviction: Valoria (the nation as idea, not as institution). When ordered to act against this Conviction (e.g., coup enforcement that would destabilise the nation, suppression of a popular movement that serves Valorian interests), the Game Master rolls Riskbreaker Intel vs Ob 2. Success: Riskbreakers comply reluctantly. Failure: Riskbreakers refuse or sabotage the operation.

**Riskbreaker Recruitment Pool:** Riskbreakers draw from across Valorian society — they are not exclusively military. Their operatives include former criminals, guild dropouts, southern Einhir who want to protect the nation on their own terms, and disgraced nobles. This diversity gives them Intel capability but makes them culturally distinct from the rest of the Löwenritter.

**Deniability Debt:** Already in stage13. Preserved. Riskbreaker operations exposed → Debt +1. At Debt 3: Crown Domain Actions +1 Ob. At Debt 5: Parliamentary inquiry.

## 4.3 Arm Mechanics (Board Game)

| Arm | BG Abstraction |
|-----|---------------|
| Lions' Table | Löwenritter Military actions as currently defined |
| Lions' Helm | Naval modifier: +1D on Trade orders in coastal territories (T8 Lowenskyst, T12 Valorsplatz, T16 Schoenland) while Löwenritter is Crown-aligned |
| Knights of the Peace | Law Enforcement modifier: hostile Covert actions in Crown territories +1 Ob |
| Royal Investigators | Intel modifier: +1D on Crown Intel actions when targeting factions with presence in Valorsplatz |
| Riskbreakers | As currently defined — deniable operations |

## 4.4 Löwenritter Levy Rules

From lore: Löwenritter serves the King and Queen. The military arm coordinates and operates military levies throughout the kingdoms.

**Mechanical translation:** The Löwenritter's Military stat represents the professional core. Levies are drawn from territory populations. When Crown musters:
- Löwenritter Military pool provides the command structure
- Territory Prosperity provides the recruits (Muster Ob reduced by Prosperity ÷ 2, round down)
- Two-thirds of ducal levies can be raised by the Monarch (same mechanic as Church levy: Crown Mandate vs Ducal Mandate contested roll if the Duke objects)

---

# 5. GUILD INTERNAL STRUCTURE AND ECONOMY

## 5.1 Guild Hierarchy

From lore:

| Rank | Role | Mechanical Relevance |
|------|------|---------------------|
| Guild Master | Master craftsmen who control means of production, run businesses | Officers of the Guilds faction. Sit on Guild Council. |
| Free Master | Master craftsmen without production control — contractors or employees of Guild Masters | Skilled Non-Player Characters available for hire. Source of Player Character backgrounds. |
| Journeyman | Qualified practitioners free to work for any registered guild | Mobile workforce. Journeymen Years = travel across kingdom + abroad. Source of information networks. |
| Apprentice | Trainees under a Master | Non-combatant. Cannot operate independently. |

## 5.2 Guild Council

From lore: Each guild elects a Council of five Guild Masters who act as liaisons to the government, set guild policies, and resolve judgments in conflicts among membership. These five also attend the city's Guild Forum.

**Mechanical translation:**

**Guild Council (per guild):** 5 Guild Masters. Acts as the decision-making body for that guild's territory-level interests.

**Guild Forum (per city/territory):** All Guild Council members in a territory meet. The Forum is where inter-guild coordination happens. The Forum's collective decision becomes the Guilds faction's Domain Action in that territory.

**Redirecting Guild Policy:** Already defined as Influence vs Ob 3. The lore confirms why: you must convince the Council, which is a collective of independent business owners with competing interests.

## 5.3 Ministry of Guilds

From lore: The Ministry of Guilds monitors the guild system, defines guilds, requires membership lists, arranges contracts between guilds and Imperial Court, sets taxation levels, and enforces non-competition against unregistered businesses.

**Mechanical translation — Crown-Guild Interaction:**

| Crown Action via Ministry of Guilds | Pool | Ob | Effect |
|-------------------------------------|------|-----|--------|
| Set Guild Taxation | Crown Wealth vs Guilds Wealth | Contested | Crown success: Crown Wealth +1 this season (higher taxes). Guild Wealth −1. Crown failure: no change, Guild Stability +1 (guilds resist). |
| Enforce Non-Competition | Crown Influence vs Ob 2 | — | Unregistered businesses in a territory are shut down. Guilds Wealth +1 in that territory (monopoly reinforced). Niflhel Wealth −1 in that territory (black market squeezed). |
| Arrange Imperial Contract | Crown Influence vs Guilds Influence | Contested | Success: one guild produces goods at cost for Crown military/infrastructure. Crown Military or Fortification +1. Guild Wealth +1 (guaranteed income). Failure: guilds refuse terms, no effect. |

## 5.4 Guild Entry and Advancement (TTRPG — Player Character Mechanics)

From lore: Entering a guild requires (1) being the child of a guild member or being vouched by three members, (2) proof of competence, (3) an entrance tax.

**Player Character Guild Entry:**

| Requirement | Mechanical Test |
|-------------|----------------|
| Sponsorship | Circles Ob 2 (guild member parent) or Circles Ob 3 (three vouching members) |
| Competence | Relevant craft History ≥ 2 |
| Entrance Tax | 1 Resource Point (or equivalent in-fiction cost) |

**Player Character Advancement:**

| Stage | Requirement | Benefit |
|-------|-------------|---------|
| Apprentice → Journeyman | Craft History 2 + 1 season of active guild work | Free to work for any registered guild. +1D on Circles tests with guild contacts in any territory. |
| Journeyman → Free Master | Craft History 4 + Journeymen Years (travel to 3+ territories working in different guilds — 2 seasons minimum) + Guild Council approval (Presence vs Ob 3) | May contract services independently. +1 Reputation with Guilds faction. |
| Free Master → Guild Master | Craft History 5 + establish a business (Resources Ob 4) + Guild Council election (Influence vs Ob 3 within guild) | Controls means of production. Sits on Guild Council. Guilds faction officer. |

## 5.5 Burgher Status

From lore: The Ministry evaluates membership lists to determine whether a guild member qualifies as a burgher.

**Mechanical translation:** Burgher status = political participation rights outside the aristocracy. A burgher may:
- Attend Guild Forum and vote on guild policy
- Petition Court Parliament through the Ministry of Guilds (Influence vs Ob 4 — guild-level concerns reach Parliament)
- Hold municipal office (Civil Magistrate appointment — see §6)

Non-burgher guild members (most Journeymen and Apprentices) cannot participate politically. This creates a class divide within the guilds that the Restoration Movement exploits.

## 5.6 Guild Proceeding Type (resolves ED-009 — Guild Arbitration)

**Guild Arbitration:** When a dispute involves guild interests (trade disputes, contract violations, quality complaints, territorial monopoly challenges):

| Element | Specification |
|---------|--------------|
| Convener | Guild Council (5 Guild Masters from the relevant guild) |
| Procedure | 3 exchanges. Both sides roll. |
| Pool | Wealth + relevant craft History |
| Audience | Guild Council (biased toward guild interests: +1D to the side whose position protects guild autonomy) |
| Win condition | First to 2 exchange wins. |
| Binding? | Within guild jurisdiction: yes. Cross-faction: recommendation only (enforced if both sides agreed to arbitration). |

---

# 6. COURT PARLIAMENT AND GOVERNANCE

## 6.1 Court Parliament Structure

From lore:

| Body | Composition | Function |
|------|-------------|----------|
| Imperial Court | Aristocrats, courtiers, advisors | Advisory. The political arena where power is exercised informally. |
| Court Parliament | Aristocrats with landed titles + distinguished service aristocrats | Votes to recommend policies, nominate Ministers, Rectorates, Civil Magistrates. |
| Ministries | Headed by Ministers nominated by Parliament, confirmed by Monarch | Execute government services: Law, Taxation, Water, Granaries, Logothetes, Guilds, etc. |
| Rectorates | Judicial. Nominated by Parliament, evaluated by Ministry of Law | Execute law. Administer legal institutions. |
| Praefectures | Administrative regions. Governed by Civil Magistrates nominated by Parliament | Local governance. Council-chaired by Magistrate. |

**Key constitutional rule:** Parliament recommends. The Monarch decides. Parliamentary decisions are strong recommendations, not rulings. The Monarch can veto any decision.

**Deposal clause:** Court Parliament has constitutional right to depose the Monarch for the good of the nation if deemed unfit by both the Holy See AND the Imperial Court.

## 6.2 Parliamentary Mechanics (Enrichment of stage6 §8.11)

Current §8.11 defines a 3-exchange contested roll. Lore adds the governance layer around it.

**Parliamentary Actions:**

| Action | Initiator | Ob | Effect |
|--------|-----------|-----|--------|
| Recommend Policy | Any Parliament member | Influence vs Ob 2 | Policy adopted unless Monarch vetoes. Veto: Crown Mandate −1 (if policy had popular support) or no cost (if policy was unpopular). |
| Nominate Minister | Parliament collective | Influence vs Ob 3 | Minister installed. Ministry operates under nominee's direction. Monarch can block: Crown Mandate vs Parliament's Influence contested. |
| Nominate Rectorate | Parliament collective | Influence vs Ob 2 | Rectorate installed. Legal institution operates under nominee. Evaluated by Ministry of Law scholars (Cognition + History vs Ob 3 yearly — failure: Rectorate challenged). |
| Nominate Civil Magistrate | Parliament collective | Influence vs Ob 2 | Magistrate installed in a Praefecture. Chairs local council. |
| Motion of No Confidence | Parliament collective (requires Hafenmark or Varfell sponsorship) | Influence vs Crown Mandate | If passed AND the Holy See concurs: Monarch deposed. If passed but Holy See refuses: constitutional crisis — Thread Tension (TT) +2, Theocracy Counter (TC) +3. |

**Ducal Presence Requirement:** From lore: Dukes and Counts spend half their time or more in Valorsplatz's Imperial Court. Mechanically: if a Duke is not present in Valorsplatz for a full season, their Influence in Parliament is halved (round down) for Parliamentary actions that season.

**Prestige Economics:** From lore: serving in the Imperial Court is more prestigious than ducal/municipal administration. Mechanically: Non-Player Character nobles assigned to Imperial Court duty gain +1 Influence for their sponsoring faction in Parliament. Non-Player Character nobles kept at home provide +1 to their duchy's local Domain Actions instead. Dukes must choose where to deploy their people.

## 6.3 Ministry Mechanics

Ministries are Crown instruments. Each Ministry provides a specific mechanical benefit while it is operational:

| Ministry | Benefit | Disruption Effect |
|----------|---------|-------------------|
| Ministry of Law | Rectorates function. Legal proceedings resolved. | If disrupted: no legal proceedings this season. Disputes escalate to military or factional resolution. |
| Ministry of Taxation | Crown collects tax from territories and Church. | If disrupted: Crown Wealth −1/season until restored. |
| Ministry of Guilds | Guild oversight, contracts, non-competition enforcement. | If disrupted: Guilds operate without oversight. Guild Wealth +1 (no taxes), but Crown loses Guild taxation income. |
| Ministry of Water / Granaries | Territory Prosperity maintenance. | If disrupted: one territory loses −1 Prosperity per season (infrastructure decay). |

**Disrupting a Ministry:** Targeted Domain Action (any faction). Intel or Influence vs Ob 3 (Ministries are bureaucratic — hard to disrupt but possible through corruption, sabotage, or political paralysis).

## 6.4 Deposal Procedure

From lore: Court Parliament can depose the Monarch if deemed unfit by the Holy See AND the Imperial Court.

**Mechanical procedure:**

1. Motion of No Confidence passes Parliament (Influence vs Crown Mandate).
2. Holy See must concur. If Holy See concurs: Monarch deposed. Succession triggers.
3. If Holy See refuses: constitutional crisis. The refusal means the Church is protecting the Monarch — or extracting concessions.

**Church leverage:** The deposal clause gives the Church a structural veto over regime change. This is why the Church's political position is so powerful despite not being a military hegemon. The Holy See can protect or destroy any Monarch.

**Mechanical consequence of deposal:**
- Crown Mandate drops to 1 (institutional collapse).
- Crown Stability −3.
- Succession crisis: if Torben is available and loyal, he inherits. If Torben is in Altonia or Altonia-aligned: IP +10 (Altonia leverages the crisis). If no heir available: interregnum — Parliament governs temporarily, all Crown Domain Actions at +2 Ob.

---

# 7. DUCAL ADMINISTRATION

## 7.1 Ducal Structure

From lore: Dukes and Counts are vassals of the Monarch. Pay taxes on titled lands. Two-thirds of personal levies raiseable by Monarch. Taxes contribute to centralised administration.

| Duchy | Title Holder | Territories | Counties |
|-------|-------------|-------------|----------|
| Valorsmark | King Almud Almqvist (cognatic senior succession) | Valorsplatz, Himmelenger, Arcansheld, Stillhelm + historically Lowenskyst | 3 counties |
| Hafenmark | Duchess Inge/Inga Baralta (cognatic senior succession) | Gransol (capital), Eidursjo, Spartfell + Lowenskyst (current control) | 2 counties |
| Varfell | Duke Vaynard (cognatic senior succession) | Varfell city (capital), Sigurdshelm, Halvardshelm, Oastad/Vargstad | 3 counties |

**Privy Councils:** Each Duke/Count has a privy council composed of constituents (noble or otherwise). Mechanically: the privy council provides +1D on Domain Actions within the duchy's territory. If the council is divided or subverted, the bonus is lost.

## 7.2 Levy Mechanics

| Rule | Mechanic |
|------|----------|
| Ducal levy raising by Crown | Crown may requisition 2/3 of ducal Military (round down) for one military action per season. If Duke consents: automatic. If Duke refuses: Crown Mandate vs Duke's Mandate contested roll. |
| Church levy raising by Crown | Same — 2/3 of Church Military (round down). Contested roll if Church refuses. |
| Tax contribution | Each territory controlled by a vassal generates +1 Wealth for the Crown per season (at Prosperity ≥ 3). This is the centralised administration benefit. |
| Ducal tax burden | Vassals pay taxes, but benefit from centralised infrastructure (Ministries, roads, Löwenritter protection). If Crown taxation increases beyond baseline: vassal Stability check Ob 2 at next accounting. |

---

# 8. HISTORICAL CONTEXT INTEGRATION

## 8.1 Three Indigenous Nations → Three Duchies

From lore: The Valn Peninsula was home to three indigenous nations (worshipping the Einhir) before Altonian conquest in 122 Before Solmund (BS). Altonia established the Diocese of Valoria, organising three nations as Provinces of Valoria, Baiamont, and Lupicco. After Secession Wars (50–67 After Solmund (AS)), these became Duchies of Valorsmark, Hafenmark, and Varfell.

**Province-to-Duchy mapping:**

| Province (Altonian) | Duchy (Valorian) |
|--------------------|------------------|
| Valoria | Valorsmark |
| Baiamont | Hafenmark |
| Lupicco | Varfell |

**Mechanical relevance:** Each duchy has a pre-Altonian indigenous identity that the Restoration Movement seeks to recover. The three-nation structure explains why the duchies have distinct political cultures:
- Valorsmark: adopted Altonian/Church cultural identity most thoroughly (capital, administrative center)
- Hafenmark: maintained strongest legal tradition from pre-Altonian governance (hence Baralta's constitutional framework)
- Varfell: maintained strongest connection to Einhir material culture (hence Vaynard's Private Collection)

**Secession Wars (50–67 AS):** 17-year war. The lore says this is when Valoria achieved independence. The canonical timeline places this at 195–200 AG (After Solmund/Galbados). These dates need reconciliation.

[EDITORIAL: ED-NEW-08 — Timeline reconciliation: lore says Secession Wars at "50–67" (unclear epoch). Canonical timeline says ~195–200 AG. The lore's "50–67" may be an internal Altonian dating system or draft-era numbers. Canonical timeline (200 AG) governs.]

## 8.2 Altonian Cultural Imperialism

From lore: Altonia "enforced its cultural imperialism by systematically destroying Valnese historical records, monuments and temples."

**Mechanical relevance:** This is a political and cultural fact, NOT the source of the Forgetting. The Forgetting is epistemological (P-08): Thread knowledge is experiential and cannot be transmitted through text, study, or institutional memory. The barrier is metaphysical — it would exist even if every Einhir record survived intact. Publishing all documents would not end it.

The Altonian destruction matters politically (it is a grievance the Restoration Movement organises around, and it eliminated cultural context that had coexisted with Thread practice), but it has zero mechanical bearing on the epistemological barrier. The Church reinforces the barrier institutionally, but did not create it. Nothing created it — it is a structural feature of how Thread knowledge works (P-08: "religious poetry" — non-sensitives can recite but not act with Thread-level precision).

**Restoration Movement connection:** The Revolution's mission to recover Einhir cultural knowledge is politically significant (identity, dignity, resistance to colonial erasure) but does not and cannot restore Thread capability. Community Weaving works because it is performed by Thread-sensitive practitioners using cultural forms as a practice interface — not because the cultural knowledge itself contains Thread information. A non-sensitive elder who knows every recovered Einhir text still cannot perform Thread operations (P-08 Inert Knowledge mechanic).

---

# 9. RESTORATION MOVEMENT LEADER (ED-005 Resolution Proposal)

From lore context: the Revolution needs a named Non-Player Character contact point. The lore doesn't name one, but the cultural context suggests the profile.

**Proposed Non-Player Character: Elder Solvei Kaldring**

| Attribute | Value |
|-----------|-------|
| Role | Southern Einhir elder. Informal authority in Korntal (T14) and Sudwald (T12). |
| Age | Late 60s. Remembers the last generation that practiced openly before the post-war settlement formalised suppression. |
| Thread Sensitivity (TS) | 22 (Dormant — elevated by proximity to Thread Wound in Sudwald and lifelong cultural practice, but never crossed into active perception). |
| Conviction | Community — the survival and dignity of southern Einhir people |
| Resonant Style | Evidence — show her concrete proof, not abstract arguments |
| Composure | 9 (Presence 4 + 5) |
| Histories | Einhir Oral Tradition (3), Herbalism (2), Community Organizing (2) |

**Belief:** *"The old ways are not dead. They are sleeping in the land and in us. I will not let them be forgotten while I am alive."*

**Mechanical role:**
- Contact point for Player Character affiliation with the Restoration Movement (Circles Ob 2 in southern territories, Ob 4 elsewhere)
- Provides access to Community Weaving ritual knowledge (prerequisite for the faction Unique Action)
- Her Thread Sensitivity (TS) 22 is not sufficient to meet the TS 30+ requirement for Community Weaving — she needs a Player Character practitioner or must develop further
- If she reaches TS 30+: she becomes the first non-Player Character Restoration Movement member who can anchor Community Weaving, making the faction self-sufficient

[EDITORIAL: ED-005 — This proposal resolves the editorial. Name, profile, and mechanical role provided. Requires user approval (worldbuilding content).]

---

# 10. NEW MECHANICS DERIVED FROM LORE

## 10.1 Tithe Economy (Church Wealth Generation)

The Cardinal of Prudence collects tithes across the kingdom. This is the Church's primary Wealth engine.

**Tithe Mechanic:** At seasonal accounting, the Church generates Wealth from tithe-eligible territories:

| Territory Condition | Tithe Value |
|--------------------|-------------|
| Church-controlled territory | +1 Wealth |
| Territory with cathedral/Church presence (not Church-controlled) | +0.5 Wealth (round down across all territories) |
| Territory with Prosperity ≤ 2 | No tithe (too poor to extract from — Cardinal of Prudence runs charities here instead) |

**Counter-play:** Guilds Economic Leverage targeting Church Wealth in a tithe territory: if successful, tithe suspended in that territory for 1 season.

## 10.2 Charity Network (Church Mandate Generation)

The Cardinal of Prudence operates charities serving the poor. This is the Church's Mandate engine in low-Prosperity territories — where other factions have no economic incentive to operate.

**Charity Mechanic:** In territories with Prosperity ≤ 3, Church may deploy charity (Wealth −1, Church Mandate +1 in that territory on the territory-level track). This competes directly with the Restoration Movement's community organising.

**Tension:** Church charities and Restoration Movement community work target the same population. If both operate in the same territory: contested roll (Church Wealth vs Restoration Influence). Winner gains +1 territory-level support. Loser: no penalty but the population gravitates toward one institution.

## 10.3 University Influence (Church Knowledge Control)

The Cardinal of Temperance controls universities, observatories, and monasteries. This is the Church's mechanism for controlling what counts as knowledge.

**University Territory Bonus:** Territories with Church-controlled universities (Himmelenger/Himmelstift, Valorsplatz):
- Church Influence +1D for Domain Actions related to knowledge, education, or cultural policy
- Any faction attempting to spread Thread truth or Einhir knowledge in these territories: +1 Ob (institutional resistance)

**Klapp's Awakening interacts:** If Klapp develops Thread Sensitivity and begins protecting texts, the university bonus flips — Klapp's institution becomes a conduit for Thread knowledge rather than a barrier. This is the highest-consequence NPC event in the Church faction.

## 10.4 Journeymen Years (Player Character Travel Mechanic)

From lore: Journeymen must travel across the kingdom and abroad, working in different guilds, to qualify for Master status.

**TTRPG Mechanic:** A Player Character undertaking Journeymen Years gains:
- After 1 territory: +1D Circles in guild networks (broadened contacts)
- After 3 territories: qualifies for Free Master (craft History 4 required)
- If traveled abroad (Altonia or Schoenland): +1D Circles with foreign contacts, but Crown Intel may notice (Royal Investigators: Intel vs Ob 2 to flag the PC as a potential foreign agent)

**Campaign hook:** Journeymen Years naturally move Player Characters across territories, exposing them to faction conflicts, Thread phenomena, and guild politics in different regions.

## 10.5 Cognatic Senior Succession

From lore: all three duchies follow cognatic senior succession — the eldest child inherits regardless of gender.

**Mechanical relevance:** Succession crises can involve daughters and sons equally. Elske is a legitimate succession candidate for the Crown. If Almud dies without Torben being ratified: Elske's claim is legally strong but she is in Altonia — creating an IP crisis.

---

# 11. TERRITORY MAPPING CORRECTIONS

## 11.1 Lore-to-Map Territory Alignment

| Lore Territory | PP-199 Map Territory | Duchy (Lore) | Duchy (Map) | Notes |
|----------------|---------------------|-------------|-------------|-------|
| Valorsplatz | T12 Valorsplatz | Valorsmark | Crown | Aligned |
| Lowenskyst | T8 Lowenskyst | Valorsmark (lore) | Hafenmark (map) | Discrepancy — map governs. Historical claim: Valorsmark. Current control: Hafenmark. |
| Himmelenger | T14 Himmelenger | Valorsmark (lore) | Church (map) | Discrepancy — map governs. Church controls the cathedral city. |
| Arcansheld | T9 Arcansheld | Valorsmark | Crown (shared) | Aligned |
| Stillhelm | T13 Stillhelm | Valorsmark | Crown | Aligned |
| Gransol | T5 Gransol | Hafenmark | Hafenmark | Aligned |
| Eidursjo | T6 Eidursjo | Hafenmark | Hafenmark | Aligned |
| Spartfell | T7 Spartfell | Hafenmark | Hafenmark | Aligned |
| Varfell city | T1 Varfell | Varfell | Varfell | Aligned |
| Sigurdshelm | T2 Sigurdshelm | Varfell | Varfell | Aligned |
| Halvardshelm | T3 Halvardshelm | Varfell | Varfell | Aligned |
| Oastad | T4 Vargstad | Varfell | Varfell | Name discrepancy — see ED-NEW-05 |

**Resolution:** The lore represents historical/constitutional claims. The PP-199 map represents game-start control. Lowenskyst was historically part of Valorsmark but transferred to Hafenmark. Himmelenger was part of Valorsmark but the Church established control over the cathedral city. These historical grievances are playable tensions.

## 11.2 Stage7 Territory Name Alignment

The stage7 compilation uses different territory names than PP-199 map. Stage7 uses fictional names (Hafenstadt, Kronmark, Sternhaven, etc.) while PP-199 uses lore-derived names. These need reconciliation.

| Stage7 Name | PP-199 Name | Proposed Resolution |
|-------------|-------------|-------------------|
| Valorsplatz | T12 Valorsplatz | Match |
| Kronmark | T10 Nordhelm (provisional) | [ED-108 still open] |
| Himmelstift | T14 Himmelenger | Lore name is Himmelenger. Stage7 uses Himmelstift. Use Himmelenger (lore authority). |
| Border Pass | No exact match | May map to Altonian passes |
| Ehrenfeld | T10 Nordhelm? | Unclear mapping |
| Hafenstadt | T5 Gransol | Lore name is Gransol. Use Gransol. |
| Sternhaven | T8 Lowenskyst | Lore name is Lowenskyst. Use Lowenskyst. |
| Grauwald | No lore equivalent | Retain — no conflict |
| Schwarzmarkt | No lore equivalent | Retain — no conflict |
| Feldmark | No lore equivalent | Retain — no conflict |
| Sudwald | No lore equivalent | Retain — no conflict |
| Askeheim | T15 Askeheim | Match |
| Korntal | No lore equivalent | Retain — no conflict |

[EDITORIAL: ED-NEW-09 — Full stage7-to-PP-199 territory name reconciliation needed. Some stage7 names have no lore basis (Grauwald, Schwarzmarkt, Feldmark, Korntal) and were generated during design. Others conflict with lore names. Recommend: lore names govern where they exist; design-generated names retained where no lore equivalent exists. Requires a definitive territory name table.]

---

# 12. EDITORIAL ITEMS GENERATED

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| ED-NEW-01 | Confirm "Solmund" as canonical name for The First Founder | P1 | Pending user confirmation |
| ED-NEW-02 | Duke of Varfell first name: Dienton (lore) vs Magnus (design) | P2 | Pending user confirmation |
| ED-NEW-03 | Duchess of Hafenmark spelling: Inga (lore) vs Inge (design) | P3 | Pending user confirmation |
| ED-NEW-04 | Church leader title: "Holy See" (lore) vs "Confessor" (design) — both canonical? | P3 | Pending user confirmation |
| ED-NEW-05 | T4 territory name: Oastad (lore) vs Vargstad (PP-199) | P3 | Pending user confirmation |
| ED-NEW-06 | Cardinal of Prudence — name and profile | P2 | Design proposal in §3.2 |
| ED-NEW-07 | Almaic Kyriakos interaction at Institutional Pressure (IP) thresholds | P2 | Design proposal in §3.6 |
| ED-NEW-08 | Timeline reconciliation: Secession Wars dating | P3 | Canonical timeline governs |
| ED-NEW-09 | Stage7-to-PP-199 territory name reconciliation | P2 | Requires definitive name table |
| ED-005 | Restoration Movement leader | P2 | Proposal: Elder Solvei Kaldring (§9) |
| ED-006 | Riskbreakers identity | P2 | Resolved in §4.2 |
| ED-009 | Guild Arbitration proceeding type | P2 | Resolved in §5.6 |

---

# 13. CROSS-MODE SUMMARY

| New Mechanic | TTRPG | Board Game | Hybrid |
|-------------|-------|------------|--------|
| Church four-Cardinal structure | Full sub-arm mechanics, Cardinal Independence Checks, named Non-Player Characters | Cardinal modifiers on Church actions | Cardinals as officers in Zoom In scenes |
| Löwenritter five-arm structure | Full arm mechanics, Lions' Helm naval, Knights of the Peace patrol | Arm modifiers on Löwenritter actions | Arms as institutional tools during Zoom In |
| Guild hierarchy | Player Character advancement path, Guild Council, Guild Forum | Abstracted — Guilds Wealth/Influence as before | Guild scenes during Zoom In; Journeymen Years as Player Character arc |
| Court Parliament governance | Full ministry/rectorate/praefecture system, Parliamentary actions | Parliament abstracted to vote mechanic (existing) | Parliamentary scenes during Zoom In |
| Levy mechanics | Contested rolls for levy requisition | +1D modifier for levy territories | Levy as Domain Action with personal scene |
| Tithe economy | Church Wealth generation per territory | +1 Wealth from tithe territories | Same as Board Game |
| Charity network | Church Mandate generation in low-Prosperity territories | Not tracked (abstracted into Church Mandate) | Charity scenes during Zoom In |
| University influence | +1D Church Influence in university territories | Same | Same |
| Almaic Kyriakos | IP threshold events | Same | Same |

---

*End of Worldbuilding Integration v1. All proposals require user editorial approval before propagation to canonical documents.*
