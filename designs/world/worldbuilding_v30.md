<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: worldbuilding_v30_infill.md -->

<!-- v30 baseline — renamed from designs/worldbuilding/worldbuilding_integration_v3.md on 2026-04-13 -->
# WORLDBUILDING INTEGRATION v3 — Lore-to-Mechanics (Final Trimmed)
## Source: Pre-project lore documents (Church, Löwenritter, Crown, Guilds, Economy, Governance)
## Date: 2026-04-03
## Authority: DESIGN (working document).
## Supersedes: worldbuilding_integration_v2.md
## Changes v2→v3: Levy system cut entirely. Cardinal BG modifiers replaced with Named Character Event cards. Cut proposals evaluated for event card potential.

---

# 1. SOLMUND RENAME


[EDITORIAL: ED-NEW-01 — Confirm "Solmund" as final canonical name.]

---

# 2. NAME DISCREPANCIES

| Character | Lore | Design | Editorial |
|-----------|------|--------|-----------|
| Duke of Varfell | Magnus Vaynard ("The White Wolf") | Magnus Vaynard | RESOLVED 2026-04-30 (ED-775 / PP-699): Magnus is canonical first name; "The White Wolf" epithet retained. Lore-form "Dienton Vaynard" superseded. |
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
| Prudence | Economic | Tithes, charities, Church land management | Aldric Tormann |
| Temperance | Knowledge | Universities, observatories, monasteries, archives | Magnus Klapp |

## 3.2 Cardinal Mechanics (TTRPG)


**Cardinal Independence Check:** Cardinal acts against explicit Holy See instruction: relevant pool vs Ob 3. Success: action proceeds, Church Stability −1. Failure: blocked.

**Jarnstal Drift (0–3, Game Master-tracked, private):** Increments each season Jarnstal deploys Templars without Holy See authorisation. At 3: Church Military controlled by Jarnstal, not the Confessor. Church Stability −2, Church Influence (CI) +2.

**Klapp Awakening:** Already in stage13. On Thread Sensitivity (TS) growth success: protects Thread-significant texts. Church Intel detects pattern → internal Heresy Investigation. If investigated before player intervention: Church Stability −1, CI +1. If players extract Klapp: −1D on Church scholarly Influence rolls.

**Olafsson-Broker Exposure (formerly Olafsson-Niflhel):** Already in stage13 (Baralta evidence mechanic). No new mechanics. Trigger reframed post-Session-B: Olafsson's exposure via settlement-layer intelligence broker connection (previously Niflhel connection). Mechanical effect unchanged.

## 3.3 Cardinal Events (Board Game — Named Character Event Cards)


**Card: Jarnstal Independence**
- Effect: Church Military stat now controlled by Jarnstal, not the Church player. Jarnstal acts as a semi-independent NPC: deploys only against perceived threats to the Church (monstrous incursions, territorial attacks on Church territories). Will NOT deploy for political operations. Church Stability −2. CI +2.
- Counter-play: Church player may spend 1 Influence + 1 Stability to recall Jarnstal and reset the counter. Can only be done once per game.

**Card: Olafsson Exposure**
- Effect: Olafsson's connection to settlement-layer intelligence brokers revealed (post-Niflhel-dissolution reframing). Church Stability −2, CI −3. Olafsson removed (Inquisitor operations suspended for 2 seasons). Church Heresy Investigation actions +1 Ob until replacement Cardinal appointed.
- Counter-play: Church may pre-emptively remove Olafsson (spend 1 Stability at Accounting) to prevent the exposure — but loses Inquisitor effectiveness permanently.

**Card: Klapp Awakening**
- Trigger: Already defined in BG v05 Scenario A — Thread operation within 1 territory of T3 (Himmelstift/Himmelenger), CI ≥ 30, no Heresy Investigation opened this season.

**Card: Prudence Crisis**
- Effect: Church charities collapse in low-Prosperity territories. Church Mandate −1 in each territory where Prosperity ≤ 3. Restoration Movement gains +1 Influence in those territories (they fill the gap).
- Counter-play: Crown or Guilds may spend 1 Wealth to prop up Church charities in one territory (prevents Mandate loss there but creates a debt relationship).

## 3.4 Church Taxation (Simple Rule — All Modes)


## 3.5 Excommunication Reversal Paths

Add to existing mechanic:
- **Penance** (voluntary): target regains standing after 1 season public service. Church Mandate +1.
- **Grand Debate** (existing): 5 exchanges.
- **Banishment** (Church Mandate vs Ob 4): permanent expulsion from public office in Church-aligned territories.

## 3.6 Almaic Kyriakos

[FLAG: Needs Institutional Pressure (IP) ladder overcrowding check.]

Single decision point at IP 50: Almaic Kyriakos envoy. Church chooses cooperate (IP −3, CI +2) or refuse (no effect). Consequences branch at higher IP if cooperated.

[EDITORIAL: ED-NEW-07 — Almaic Kyriakos IP interaction. Needs IP ladder review.]

## 3.7 Practitioner Witness Tradition (suppressed)

A parallel literary tradition exists alongside the canonical miracle-witness scripture: accounts by thread-sensitive people who encountered Solmund and perceived his operations at a scale the non-practitioner witness could not access. These accounts describe Solmund's acts accurately — which, within the Church's interpretive commitment to the miracle framework, reads as heresy. The Church's interpretive community was built by non-practitioners; by the time it encountered practitioner accounts, it had already committed to the miracle framework, and practitioner accounts were categorised as heretical from their first circulation.

The tradition survives in fragments: Seam Texts (passages of orthodox scripture in which the underlying practitioner testimony breaks through the theological overlay, readable only at TS 30+; see `designs/world/solmund_cultural_guide_consolidated.md` §12); a small number of suppressed manuscripts held privately by Einhir-sympathetic lineages; and oral practitioner transmission within Warden orders. The tradition is the most theologically dangerous material in the setting because accuracy, within the Church's framework, is worse than denial — accurate description reveals the mechanism, and the mechanism reveals that the Church's cosmology is a rendering applied to something the rendering cannot contain.

**Mechanical implications.** Seam Texts function as discoverable POIs (Remnant type) in Church territories, gated by TS via the visibility tables in `designs/threadwork/threadwork_v30.md` §2.3. Same text, two readings: TS 0–29 reads devotional language; TS 30+ reads the suppressed witness account. Discovery develops character arcs (Conviction pressure, SA increments, Certainty track). Placement in new territories can also occur via Miracle Investigation (§22.1 consolidated guide) once Miraculous Event events fire.

[EDITORIAL: PR-14 Finding 7 — resolved 2026-04-20 (ED-735). Section added as canonical worldbuilding placement for the practitioner witness tradition.]

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

**Card: Ehrenwall Split** *(formerly Card: Ehrenwall Coup — renamed post-Session-B to reflect Löwenritter graduated autonomy replacing the binary Coup Counter; fires when Autonomy track reaches Split stage, not on a single count-threshold trigger. See designs/architecture/conflict_architecture_proposal.md.)*

**Card: Riskbreaker Exposure**
- Trigger: Deniability Debt reaches 3 (tracked per stage13).
- Effect: Crown Domain Actions against non-Crown factions +1 Ob. At Debt 5: Parliamentary inquiry opens — Grand Debate (Crown Influence + Mandate at stake).

**Card: Lions' Table Mutiny**
- Trigger: Löwenritter Military drops to 2 or below AND Ehrenwall has been removed or neutralised.
- This is a late-game catastrophic event. Low probability but high consequence.

## 4.4 Levy System


---

# 5. GUILD STRUCTURE

## 5.1 Reference (TTRPG Worldbuilding — Not Mechanics)


Burgher status: Guild Masters and Free Masters qualify for political participation.

## 5.2 Journeymen Years (TTRPG Campaign Hook)

Player Character travels 3+ territories working in different guilds over 2+ seasons. Qualifies for Free Master. Broadens Circles (+1D guild contacts).

## 5.3 Guild Event Cards (Board Game — Named Character Events)

**Card: Guild Schism**
- Trigger: Guilds Stability drops to 2 or below (internal disputes between guild factions).
- Counter-play: any faction may spend 1 Influence to mediate (Guilds Stability +1, mediating faction gains +1 Influence with Guilds for 1 season).

**Card: Guild Forum Revolt**
- Trigger: Crown raises Guild taxation (Crown plays Economic Leverage or Policy Instrument targeting Guilds) AND Guilds Stability ≤ 3.
- Effect: Guilds withdraw from Ministry oversight. Crown loses Ministry of Guilds benefits (no Guild taxation income, no non-competition enforcement). Guilds Wealth +1 (no taxes). Restoration Movement gains +1D Influence in Guild-heavy territories (workers radicalise).

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



## 6.2 Motion of No Confidence (New Mechanic — All Modes)


| Step | Mechanic |
|------|----------|
| 1. Parliamentary Vote | Influence vs Crown Mandate (existing §8.11) |
| 2. Holy See concurrence | Confessor chooses: concur or refuse |

**Deposal:** Crown Mandate → 1, Stability −3. Succession: Torben if available and loyal; if not, IP +10; if no heir, interregnum (Crown actions +2 Ob).

**Holy See refusal:** CI +3, Thread Tension (TT) +2.

**Church leverage:** The deposal clause gives the Church structural veto over regime change.

## 6.3 Governance Event Cards (Board Game — Named Character Events)

**Card: Constitutional Crisis**
- Trigger: Crown Mandate drops to 1 OR Crown loses 3+ territories in a single season.
- Effect: Motion of No Confidence automatically raised in Parliament. Parliamentary Vote fires at next Accounting. If Crown loses the vote AND Confessor concurs: deposal (§6.2 consequences). If Crown loses but Confessor refuses: CI +3, TT +2.

**Card: Ministry Collapse**
- Trigger: Crown Stability drops to 2 or below.
  - Law: no legal proceedings. Disputes escalate.
  - Taxation: Crown Wealth −1.
  - Guilds: Guilds Wealth +1 (no oversight), Crown loses Guild tax income.
  - Water/Granaries: one Crown territory −1 Prosperity.
- Counter-play: Crown spends 1 Influence to restore Ministry at next Accounting.

---

# 7. HISTORICAL CONTEXT (Setting Reference)

## 7.1 Three Altonian Provinces → Three Duchies

The Einhir civilisation's internal organisation is unknowable from post-Calamity sources (see `canon/03_canonical_timeline.md` L16, D-2 resolved 2026-04-20). The three provinces below are Altonian colonial administrative overlays, not indigenous nations; their boundaries do not correspond to any recoverable pre-Calamity political geography. Post-colonial Valorian duchies inherited province boundaries but renamed.

| Province (Altonian colonial) | Duchy (current Valorian) |
|-----------------------------|--------------------------|
| Valoria | Valorsmark |
| Baiamont | Hafenmark |
| Lupicco | Varfell |

[EDITORIAL: D-2 — resolved 2026-04-20; heading and framing corrected to reflect Altonian-overlay status, not indigenous.]

## 7.2 Altonian Cultural Imperialism


## 7.3 Cognatic Senior Succession


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
| Klapp Awakening | Church | Thread op within 1 territory of Himmelenger, CI ≥ 30, no Heresy Investigation this season | BG v05 Scenario A |
| Ehrenwall Split (was Ehrenwall Coup) | Löwenritter | Löwenritter Autonomy track reaches Split (graduated autonomy, replaces Coup Counter 3-trigger) | conflict_architecture_proposal.md, clock_registry_v30.md |
| Riskbreaker Exposure | Crown | Deniability Debt reaches 3/5 | stage13 §13.6 |

## New (proposed in this document)

| Card | Faction | Trigger | Effect Summary |
|------|---------|---------|---------------|
| Jarnstal Independence | Church | Jarnstal Counter reaches 3 | Church Military splits. Church Stability −2, CI +2. |
| Olafsson Exposure | Church | Overwhelming Intel action vs Church in a settlement with intelligence-broker presence (reframed post-Niflhel-dissolution; settlement_layer_v30 §4.8) | Church Stability −2, CI −3. Inquisitor operations suspended 2 seasons. |
| Prudence Crisis | Church | Church Wealth ≤ 2 | Church Mandate −1 in low-Prosperity territories. Restoration +1 Influence there. |
| Lions' Table Mutiny | Löwenritter | Military ≤ 2 AND Ehrenwall removed | Löwenritter fragments. Military halved. |
| Guild Schism | Guilds | Stability ≤ 2 | Wealth −1, Influence −1 for 1 season. One territory Guild Favour → 0. |
| Guild Forum Revolt | Guilds | Crown taxation action AND Guilds Stability ≤ 3 | Guilds withdraw from Ministry. Crown loses Guild tax. Restoration gains Influence. |
| Constitutional Crisis | Crown | Mandate ≤ 1 OR loses 3+ territories in one season | Motion of No Confidence fires automatically. Deposal possible. |
| Ministry Collapse | Crown | Stability ≤ 2 | One Ministry ceases function for 1 season. |


---

# 11. EDITORIAL ITEMS

## New Items

| ID | Description | Priority |
|----|-------------|----------|
| ED-NEW-01 | Confirm Solmund as canonical First Founder name | P1 |
<!-- ED-NEW-02 RESOLVED 2026-04-30 (PP-699): Magnus Vaynard canonical, "The White Wolf" epithet retained. -->
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

[EDITORIAL: ED-741 — TC→CI + RS→MS abbreviation disambiguation per ED-782/ED-731. Mechanical abbreviation rename only; no semantic changes to worldbuilding/NPC content.]
