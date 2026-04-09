# WORLDBUILDING INTEGRATION v3 — Lore-to-Mechanics (Final Trimmed)
## Source: Pre-project lore documents (Church, Löwenritter, Crown, Guilds, Economy, Governance)
## Date: 2026-04-03
## Authority: DESIGN (working document).
## Supersedes: worldbuilding_integration_v2.md
## Changes v2→v3: Levy system cut entirely. Cardinal BG modifiers replaced with Named Character Event cards. Cut proposals evaluated for event card potential.

---

# 1. SOLMUND RENAME

All references to "Solmund" → "Solmund." Calendar: "Before Solmund (BG)" → "Before Solmund (BS)." "After Solmund (AG)" → "After Solmund (AS)." Haiku-tier cleanup. Run last.

[EDITORIAL: ED-NEW-01 — Confirm "Solmund" as final canonical name.]

---

# 2. NAME DISCREPANCIES

| Character | Lore | Design | Editorial |
|-----------|------|--------|-----------|
| Duke of Varfell | Dienton Vaynard ("The White Wolf") | Magnus Vaynard | ED-NEW-02: which name? Lore gives epithet + military prowess + progressive policies. |
| Duchess of Hafenmark | Inga | Inge | ED-NEW-03: confirm spelling. |
| Church leader title | "The Holy See" | "Confessor" | ED-NEW-04: recommend both canonical — "Holy See" = formal title, "Confessor" = address. |
| T4 territory | Oastad | Grauwald (PP-199) | ED-NEW-05: confirm name. |
| Lowenskyst duchy | Valorsmark (lore) | Hafenmark (PP-199 map) | No conflict — historical Valorsmark, current Hafenmark. Playable tension. |

---

# 3. CHURCH OF SOLMUND — FOUR-CARDINAL STRUCTURE

## 3.1 Structure (Reference — All Modes)

| Cardinal | Arm | Portfolio | Named NPC |
|----------|-----|-----------|-----------|
| Fortitude | Military | Knights Templar, enforcement, monstrous incursion suppression | Osten Jarnstal |
| Justice | Judicial | Inquisitors, Grand Adjudication, heresy investigation, text suppression | Arnlod Olafsson |
| Prudence | Economic | Tithes, charities, Church land management | [UNNAMED — ED-NEW-06] |
| Temperance | Knowledge | Universities, observatories, monasteries, archives | Magnus Klapp |

## 3.2 Cardinal Mechanics (TTRPG)

Cardinals act as officers. Each rolls the Church faction stat relevant to their portfolio. No new pools.

**Cardinal Independence Check:** Cardinal acts against explicit Holy See instruction: relevant pool vs Ob 3. Success: action proceeds, Church Stability −1. Failure: blocked.

**Jarnstal Drift (0–3, Game Master-tracked, private):** Increments each season Jarnstal deploys Templars without Holy See authorisation. At 3: Church Military controlled by Jarnstal, not the Confessor. Church Stability −2, Theocracy Counter (TC) +2.

**Klapp Awakening:** Already in stage13. On Thread Sensitivity (TS) growth success: protects Thread-significant texts. Church Intel detects pattern → internal Heresy Investigation. If investigated before player intervention: Church Stability −1, TC +1. If players extract Klapp: −1D on Church scholarly Influence rolls.

**Olafsson-Niflhel Exposure:** Already in stage13 (Baralta evidence mechanic). No new mechanics.

## 3.3 Cardinal Events (Board Game — Named Character Event Cards)

Cardinals are NOT passive modifiers. They exist in the Named Character Events deck as targetable/triggerable event cards. Each Cardinal matters when something happens TO them — when they break, defect, or are exposed. This creates player decisions (do I target Olafsson? Do I let Jarnstal drift?) without inflating Church stats.

**Card: Jarnstal Independence**
- Trigger: Jarnstal Independence Counter reaches 3 (Game Master-tracked; increments when Church Military is deployed without explicit Confessor authorisation — operationally, when Church plays a Military card in a territory where Confessor token is absent).
- Effect: Church Military stat now controlled by Jarnstal, not the Church player. Jarnstal acts as a semi-independent NPC: deploys only against perceived threats to the Church (monstrous incursions, territorial attacks on Church territories). Will NOT deploy for political operations. Church Stability −2. TC +2.
- Counter-play: Church player may spend 1 Influence + 1 Stability to recall Jarnstal and reset the counter. Can only be done once per game.

**Card: Olafsson Exposure**
- Trigger: Any faction successfully executes an Intel action (Spy/Investigate) targeting Church in a territory where Niflhel has presence, AND rolls Overwhelming.
- Effect: Olafsson-Niflhel connection revealed. Church Stability −2, TC −3. Olafsson removed (Inquisitor operations suspended for 2 seasons). Church Heresy Investigation actions +1 Ob until replacement Cardinal appointed.
- Counter-play: Church may pre-emptively remove Olafsson (spend 1 Stability at Accounting) to prevent the exposure — but loses Inquisitor effectiveness permanently.

**Card: Klapp Awakening**
- Trigger: Already defined in BG v05 Scenario A — Thread operation within 1 territory of T3 (Himmelstift/Himmelenger), TC ≥ 30, no Heresy Investigation opened this season.
- Effect: Three trajectories (Suppress/Fracture/Convert) as per BG v05 Scenario A. Already designed. No changes needed.

**Card: Prudence Crisis**
- Trigger: Church Wealth drops to 2 or below (tithe income insufficient — economic pressure from Guilds or Crown taxation).
- Effect: Church charities collapse in low-Prosperity territories. Church Mandate −1 in each territory where Prosperity ≤ 3. Restoration Movement gains +1 Influence in those territories (they fill the gap).
- Counter-play: Crown or Guilds may spend 1 Wealth to prop up Church charities in one territory (prevents Mandate loss there but creates a debt relationship).

## 3.4 Church Taxation (Simple Rule — All Modes)

Church-controlled territories at Prosperity 4+: Crown gains +1 Wealth/season (taxation on Church lands). This is a simple accounting rule, not a new mechanic. Already implicit in the Crown-Church economic relationship.

## 3.5 Excommunication Reversal Paths

Add to existing mechanic:
- **Penance** (voluntary): target regains standing after 1 season public service. Church Mandate +1.
- **Grand Debate** (existing): 5 exchanges.
- **Banishment** (Church Mandate vs Ob 4): permanent expulsion from public office in Church-aligned territories.

## 3.6 Almaic Kyriakos

[FLAG: Needs Institutional Pressure (IP) ladder overcrowding check.]

Single decision point at IP 50: Almaic Kyriakos envoy. Church chooses cooperate (IP −3, TC +2) or refuse (no effect). Consequences branch at higher IP if cooperated.

[EDITORIAL: ED-NEW-07 — Almaic Kyriakos IP interaction. Needs IP ladder review.]

---

# 4. LÖWENRITTER INTERNAL STRUCTURE

## 4.1 Structure (Reference — All Modes)

| Arm | Function |
|-----|----------|
| Lions' Table | Military coordination, levy operations, Royal Guard |
| Lions' Helm | Naval affairs [NO MECHANICS — ED-NEW-10: future naval design question] |
| Knights of the Peace | Road patrol, civilian protection, law enforcement |
| Royal Investigators | Investigation, counter-espionage, court prosecution |
| Riskbreakers | Extralegal infiltration. Loyal to Valoria the concept, not institutions. |

## 4.2 Riskbreaker Identity (Resolves ED-006 — TTRPG/Hybrid)

Riskbreakers have hidden Conviction: Valoria (nation as idea). When ordered to act against this conviction: Game Master rolls Riskbreaker Intel vs Ob 2. Success: comply. Failure: refuse or sabotage.

Deniability Debt: already in stage13. No changes.

## 4.3 Löwenritter Event Cards (Board Game — Named Character Events)

**Card: Ehrenwall Coup**
- Already defined (stage6 §8.9, Coup Counter 0–3). No new design needed. Confirm it belongs in Named Character Events deck.

**Card: Riskbreaker Exposure**
- Trigger: Deniability Debt reaches 3 (tracked per stage13).
- Effect: Crown Domain Actions against non-Crown factions +1 Ob. At Debt 5: Parliamentary inquiry opens — Grand Debate (Crown Influence + Mandate at stake).
- This is already in stage13 but should be formalised as a Named Character Event card for BG consistency.

**Card: Lions' Table Mutiny**
- Trigger: Löwenritter Military drops to 2 or below AND Ehrenwall has been removed or neutralised.
- Effect: Löwenritter fragments. Military stat halved (round down). Crown loses deniable covert arm. Remaining Löwenritter units become NPC-controlled (defend fortress territory only).
- This is a late-game catastrophic event. Low probability but high consequence.

## 4.4 Levy System

**CUT.** The lore fact (Crown can raise 2/3 of vassal/Church levies) is already reflected in starting Military stats. Crown Military 4 already incorporates levy access. Löwenritter Military 5 is the professional core. No standalone levy mechanic needed. If a TTRPG scenario requires requisitioning Church troops specifically, the Game Master resolves it as a standard Domain Action.

---

# 5. GUILD STRUCTURE

## 5.1 Reference (TTRPG Worldbuilding — Not Mechanics)

Guild hierarchy: Guild Masters (own businesses, Council seat) → Free Masters (contractors) → Journeymen (qualified, mobile) → Apprentices (trainees). Each guild elects a Council of five Guild Masters. Ministry of Guilds provides Crown oversight.

Burgher status: Guild Masters and Free Masters qualify for political participation.

## 5.2 Journeymen Years (TTRPG Campaign Hook)

Player Character travels 3+ territories working in different guilds over 2+ seasons. Qualifies for Free Master. Broadens Circles (+1D guild contacts).

## 5.3 Guild Event Cards (Board Game — Named Character Events)

**Card: Guild Schism**
- Trigger: Guilds Stability drops to 2 or below (internal disputes between guild factions).
- Effect: Guilds Wealth −1, Influence −1 for 1 season. One territory where Guilds have presence: Guild Favour drops to 0 (local guild chapter collapses).
- Counter-play: any faction may spend 1 Influence to mediate (Guilds Stability +1, mediating faction gains +1 Influence with Guilds for 1 season).

**Card: Guild Forum Revolt**
- Trigger: Crown raises Guild taxation (Crown plays Economic Leverage or Policy Instrument targeting Guilds) AND Guilds Stability ≤ 3.
- Effect: Guilds withdraw from Ministry oversight. Crown loses Ministry of Guilds benefits (no Guild taxation income, no non-competition enforcement). Guilds Wealth +1 (no taxes). Restoration Movement gains +1D Influence in Guild-heavy territories (workers radicalise).
- Counter-play: Crown restores normal relations by reducing taxation (spend 1 Wealth) or Parliamentary Vote to reinstate Ministry authority.

## 5.4 Guild Arbitration (ED-009 — Route to Debate System)

Proposal only — route to debate system design doc for integration.

---

# 6. COURT PARLIAMENT AND GOVERNANCE

## 6.1 Reference (TTRPG Worldbuilding — Not Mechanics)

| Body | Composition | Function |
|------|-------------|----------|
| Imperial Court | Aristocrats, courtiers, advisors | Advisory. Informal power arena. |
| Court Parliament | Landed + distinguished service aristocrats | Recommends policies, nominates Ministers/Rectorates/Magistrates. |
| Ministries | Headed by Ministers | Execute government services. |
| Rectorates | Judicial | Execute law. |
| Praefectures | Local governance | Administer regions. |

Parliament recommends. Monarch decides. Existing Parliamentary Vote (stage6 §8.11) handles contested votes.

**Ducal Presence (Game Master note):** Dukes absent from Imperial Court for a full season: halved Parliamentary Influence. TTRPG only.

## 6.2 Motion of No Confidence (New Mechanic — All Modes)

Constitutional right to depose the Monarch. Requires BOTH Parliamentary Vote AND Holy See concurrence.

| Step | Mechanic |
|------|----------|
| 1. Parliamentary Vote | Influence vs Crown Mandate (existing §8.11) |
| 2. Holy See concurrence | Confessor chooses: concur or refuse |

**Deposal:** Crown Mandate → 1, Stability −3. Succession: Torben if available and loyal; if not, IP +10; if no heir, interregnum (Crown actions +2 Ob).

**Holy See refusal:** TC +3, Thread Tension (TT) +2.

**Church leverage:** The deposal clause gives the Church structural veto over regime change.

## 6.3 Governance Event Cards (Board Game — Named Character Events)

**Card: Constitutional Crisis**
- Trigger: Crown Mandate drops to 1 OR Crown loses 3+ territories in a single season.
- Effect: Motion of No Confidence automatically raised in Parliament. Parliamentary Vote fires at next Accounting. If Crown loses the vote AND Confessor concurs: deposal (§6.2 consequences). If Crown loses but Confessor refuses: TC +3, TT +2.
- This makes deposal a live threat in BG without requiring players to initiate it — it fires from game state.

**Card: Ministry Collapse**
- Trigger: Crown Stability drops to 2 or below.
- Effect: One Ministry (Game Master choice or random) ceases to function for 1 season. Effects by Ministry:
  - Law: no legal proceedings. Disputes escalate.
  - Taxation: Crown Wealth −1.
  - Guilds: Guilds Wealth +1 (no oversight), Crown loses Guild tax income.
  - Water/Granaries: one Crown territory −1 Prosperity.
- Counter-play: Crown spends 1 Influence to restore Ministry at next Accounting.

---

# 7. HISTORICAL CONTEXT (Setting Reference)

## 7.1 Three Indigenous Nations → Three Duchies

| Province (Altonian) | Duchy (Valorian) |
|--------------------|------------------|
| Valoria | Valorsmark |
| Baiamont | Hafenmark |
| Lupicco | Varfell |

## 7.2 Altonian Cultural Imperialism

Altonia systematically destroyed Valnese records, monuments, and temples. This is a political fact — NOT the source of the Forgetting. The Forgetting is epistemological (P-08): Thread knowledge is experiential, cannot be transmitted through text or study. The barrier is metaphysical and would exist even if every record survived. The destruction matters politically (Restoration Movement grievance) but has zero bearing on the epistemological barrier.

## 7.3 Cognatic Senior Succession

All duchies follow cognatic senior succession — eldest child inherits regardless of gender. Elske is a legitimate Crown succession candidate.

---

# 8. RESTORATION MOVEMENT LEADER (ED-005)

**Proposed: Elder Solvei Kaldring**

| Attribute | Value |
|-----------|-------|
| Role | Southern Einhir elder. Informal authority in Korntal (T14) and Sudwald (T12). |
| Age | Late 60s |
| Thread Sensitivity (TS) | 22 (Dormant. Not a practitioner. Cannot bridge epistemological barrier — P-08.) |
| Conviction | Community |
| Resonant Style | Evidence |
| Composure | 9 (Presence 4 + 5) |
| Histories | Einhir Oral Tradition (3), Herbalism (2), Community Organising (2) |

**Belief:** *"The old ways are not dead. They are sleeping in the land and in us. I will not let them be forgotten while I am alive."*

Contact point for Restoration affiliation (Circles Ob 2 south, Ob 4 elsewhere). Cannot anchor Community Weaving (TS 22 < 30 threshold). Needs Player Character practitioner.

---

# 9. TERRITORY MAPPING

## 9.1 Lore-to-Map Alignment

| Lore Territory | PP-199 Territory | Duchy (Lore) | Duchy (Map) | Notes |
|----------------|-----------------|-------------|-------------|-------|
| Valorsplatz | T12 | Valorsmark | Crown | Match |
| Lowenskyst | T8 | Valorsmark | Hafenmark | Historical vs current control |
| Himmelenger | T14 | Valorsmark | Church | Church controls cathedral city |
| Ehrenfeld | T9 | Valorsmark | Crown (shared) | Match |
| Stillhelm | T13 | Valorsmark | Crown | Match |
| Gransol | T5 | Hafenmark | Hafenmark | Match |
| Rendstad | T6 | Hafenmark | Hafenmark | Match |
| Spartfell | T7 | Hafenmark | Hafenmark | Match |
| Varfell city | T1 | Varfell | Varfell | Match |
| Sigurdshelm | T2 | Varfell | Varfell | Match |
| Halvardshelm | T3 | Varfell | Varfell | Match |
| Oastad | T4 Grauwald | Varfell | Varfell | ED-NEW-05 |

[EDITORIAL: ED-NEW-09 — Stage7-to-PP-199 territory name reconciliation needed.]

---

# 10. NAMED CHARACTER EVENT CARDS — COMPLETE CATALOGUE

All new cards from this document, plus existing events confirmed for the deck:

## Existing (already designed, confirm for Named Character Events deck)

| Card | Faction | Trigger | Source |
|------|---------|---------|--------|
| Klapp Awakening | Church | Thread op within 1 territory of Himmelenger, TC ≥ 30, no Heresy Investigation this season | BG v05 Scenario A |
| Ehrenwall Coup | Löwenritter | Coup Counter reaches 3 | stage6 §8.9 |
| Riskbreaker Exposure | Crown | Deniability Debt reaches 3/5 | stage13 §13.6 |

## New (proposed in this document)

| Card | Faction | Trigger | Effect Summary |
|------|---------|---------|---------------|
| Jarnstal Independence | Church | Jarnstal Counter reaches 3 | Church Military splits. Church Stability −2, TC +2. |
| Olafsson Exposure | Church | Overwhelming Intel action vs Church in Niflhel-present territory | Church Stability −2, TC −3. Inquisitor operations suspended 2 seasons. |
| Prudence Crisis | Church | Church Wealth ≤ 2 | Church Mandate −1 in low-Prosperity territories. Restoration +1 Influence there. |
| Lions' Table Mutiny | Löwenritter | Military ≤ 2 AND Ehrenwall removed | Löwenritter fragments. Military halved. |
| Guild Schism | Guilds | Stability ≤ 2 | Wealth −1, Influence −1 for 1 season. One territory Guild Favour → 0. |
| Guild Forum Revolt | Guilds | Crown taxation action AND Guilds Stability ≤ 3 | Guilds withdraw from Ministry. Crown loses Guild tax. Restoration gains Influence. |
| Constitutional Crisis | Crown | Mandate ≤ 1 OR loses 3+ territories in one season | Motion of No Confidence fires automatically. Deposal possible. |
| Ministry Collapse | Crown | Stability ≤ 2 | One Ministry ceases function for 1 season. |

**Design principle:** These cards fire from game state, not player initiative. They reward strategic targeting (weaken Church Wealth to trigger Prudence Crisis; destabilise Crown to trigger Constitutional Crisis) and create cascading consequences without adding passive stat inflation. Players interact with Cardinals and institutions by attacking the conditions that keep them stable, not by receiving free bonuses for having them.

---

# 11. EDITORIAL ITEMS

## New Items

| ID | Description | Priority |
|----|-------------|----------|
| ED-NEW-01 | Confirm Solmund as canonical First Founder name | P1 |
| ED-NEW-02 | Vaynard first name: Dienton (lore) vs Magnus (design) | P2 |
| ED-NEW-03 | Baralta spelling: Inga vs Inge | P3 |
| ED-NEW-04 | Church leader title: Holy See + Confessor both canonical? | P3 |
| ED-NEW-05 | T4 name: Oastad vs Grauwald | P3 |
| ED-NEW-06 | Cardinal of Prudence — name and profile | P2 |
| ED-NEW-07 | Almaic Kyriakos IP threshold interaction | P2 |
| ED-NEW-08 | Timeline reconciliation (canonical timeline governs) | P3 |
| ED-NEW-09 | Stage7-to-PP-199 territory name reconciliation | P2 |
| ED-NEW-10 | Naval mechanics as future design question (Lions' Helm) | P3 |

## Existing Items Addressed

| ID | Status |
|----|--------|
| ED-005 | Proposal: Elder Solvei Kaldring. Pending user approval. |
| ED-006 | Resolved: Riskbreakers loyal to Valoria concept. Intel vs Ob 2 on divergence. |
| ED-009 | Routed to debate system design doc. |

---

# 12. WHAT CHANGED v2→v3

| Change | Reason |
|--------|--------|
| Levy system cut entirely | Already reflected in starting Military stats. No scenario requires it as a standalone mechanic. |
| Cardinal BG modifiers → Named Character Event cards | Passive bonuses inflated Church stats. Event cards create player decisions (target the conditions) without stat bloat. |
| Guild Schism and Forum Revolt added as event cards | v2 cut Ministry of Guilds mechanics and Guild advancement. The interesting parts (Guild institutional fragility, Crown-Guild tension) survive as event triggers instead of standing mechanics. |
| Constitutional Crisis and Ministry Collapse added as event cards | v2 cut Ministry mechanics and Parliamentary sub-actions. The deposal procedure and Ministry disruption survive as events that fire from game state. |
| Lions' Table Mutiny added as event card | v2 had no late-game Löwenritter catastrophe. This fills the gap. |
| BALANCE-FLAG-01 resolved | Church no longer gets passive bonuses in BG. Cardinals are event triggers only. Flag closed. |

---

*End of Worldbuilding Integration v3. 8 new Named Character Event cards proposed. All worldbuilding content requires user editorial approval.*
