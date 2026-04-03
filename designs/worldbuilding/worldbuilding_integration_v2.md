# WORLDBUILDING INTEGRATION v2 — Lore-to-Mechanics (Audit-Trimmed)
## Source: Pre-project lore documents (Church, Löwenritter, Crown, Guilds, Economy, Governance)
## Date: 2026-04-03
## Authority: DESIGN (working document).
## Supersedes: worldbuilding_integration_v1.md
## Audit applied: canon compliance (P-01–P-15), cognitive load assessment, three-mode necessity check. Flavour-only proposals cut. Redundant mechanics cut. Balance flags raised.

---

# 1. SOLMUND RENAME

All references to "Galbados" → "Solmund." Calendar: "Before Galbados (BG)" → "Before Solmund (BS)." "After Galbados (AG)" → "After Solmund (AS)." Haiku-tier cleanup. Run last.

[EDITORIAL: ED-NEW-01 — Confirm "Solmund" as final canonical name.]

---

# 2. NAME DISCREPANCIES

| Character | Lore | Design | Editorial |
|-----------|------|--------|-----------|
| Duke of Varfell | Dienton Vaynard ("The White Wolf") | Magnus Vaynard | ED-NEW-02: which name? Lore also gives epithet + military prowess + progressive policies. |
| Duchess of Hafenmark | Inga | Inge | ED-NEW-03: confirm spelling. |
| Church leader title | "The Holy See" | "Confessor" | ED-NEW-04: recommend both canonical — "Holy See" = formal title, "Confessor" = address. |
| T4 territory | Oastad | Vargstad (PP-199) | ED-NEW-05: confirm name. |
| Lowenskyst duchy | Valorsmark (lore) | Hafenmark (PP-199 map) | No conflict — historical Valorsmark, current Hafenmark. Playable tension. |

---

# 3. CHURCH OF SOLMUND — FOUR-CARDINAL SUB-ARM STRUCTURE

## 3.1 Structure

| Cardinal | Arm | Portfolio | Named NPC |
|----------|-----|-----------|-----------|
| Fortitude | Military | Knights Templar, enforcement, monstrous incursion suppression | Osten Jarnstal |
| Justice | Judicial | Inquisitors, Grand Adjudication, heresy investigation, text suppression | Arnlod Olafsson |
| Prudence | Economic | Tithes, charities, Church land management | [UNNAMED — ED-NEW-06] |
| Temperance | Knowledge | Universities, observatories, monasteries, archives | Magnus Klapp |

## 3.2 Cardinal Mechanics (TTRPG)

Cardinals act as officers. Each rolls the Church faction stat relevant to their portfolio. No new pools — this is a clarification of who rolls what when a Cardinal acts.

**Cardinal Independence Check:** Cardinal acts against explicit Holy See instruction: Cardinal's relevant pool vs Ob 3. Success: action proceeds, Church Stability −1. Failure: blocked. TTRPG only.

**Jarnstal Drift (0–3, Game Master-tracked, private):** Increments each season Jarnstal deploys Templars without Holy See authorisation. At 3: Church Military controlled by Jarnstal, not the Confessor. Church Stability −2, Theocracy Counter (TC) +2.

**Klapp Awakening:** Already in stage13. On Thread Sensitivity (TS) growth success: Klapp protects Thread-significant texts instead of suppressing them. Church Intel eventually detects pattern → internal Heresy Investigation. If investigated before player intervention: Church Stability −1, TC +1. If players extract Klapp: Church loses −1D on scholarly Influence rolls.

**Olafsson-Niflhel Exposure:** Already in stage13 (Baralta evidence mechanic). No new mechanics needed.

## 3.3 Cardinal Mechanics (Board Game)

[FLAG: BALANCE-FLAG-01 — Church cumulative passive bonuses. Church starts with highest stats (Mandate 5, Influence 6, Wealth 5, Military 4, Stability 5). Adding 4 Cardinal modifiers is 4 passive bonuses with no new costs. Needs stress testing before approval. Presenting the proposal; do not integrate until simulated.]

| Cardinal | BG Modifier |
|----------|------------|
| Fortitude | Church Military actions: −1 Ob |
| Justice | Heresy Investigation: +1D |
| Prudence | +1 Wealth/season from tithe territories |
| Temperance | Church Influence in university territories: −1 Ob |

**Cardinal Loss:** Modifier removed when Cardinal is removed. Replacement: 1 Influence + 1 Stability at accounting.

## 3.4 Church Levy and Taxation

Crown may requisition 2/3 of Church Military (round down) for one military action per season. Church refusal is a Leadership Deviation — use existing deviation mechanics.

Church-controlled territories at Prosperity 4+: Crown gains +1 Wealth/season (taxation on Church lands).

## 3.5 Excommunication (Enriched)

Add reversal paths to existing mechanic:
- **Penance** (voluntary): target regains standing after 1 season public service. Church Mandate +1.
- **Grand Debate** (existing): 5 exchanges.
- **Banishment** (Church Mandate vs Ob 4): target permanently expelled from public office in Church-aligned territories.

## 3.6 Almaic Kyriakos (Altonian Religious Institution)

[FLAG: Needs Institutional Pressure (IP) ladder overcrowding check before integration.]

At IP 50: Almaic Kyriakos envoy arrives. Church chooses: cooperate (IP −3, TC +2) or refuse (no effect). Consequences of cooperation branch at higher IP thresholds. Single decision point — do not add multiple threshold events.

[EDITORIAL: ED-NEW-07 — Almaic Kyriakos interaction. Needs IP ladder review and simulation.]

---

# 4. LÖWENRITTER INTERNAL STRUCTURE

## 4.1 Structure

| Arm | Function |
|-----|----------|
| Lions' Table | Military coordination, levy operations, appoints Royal Guard |
| Lions' Helm | Naval affairs | [CUT from mechanics — no naval system exists. ED-NEW-10: naval design question for future.] |
| Knights of the Peace | Road patrol, civilian protection, law enforcement, border security |
| Royal Investigators | Investigation, counter-espionage, court prosecution |
| Riskbreakers | Extralegal infiltration. Loyal to Valoria the concept, not Crown or institutions. |

## 4.2 Mechanical Additions (TTRPG)

**Royal Guard:** Narrative effect — assassination of Imperial Court members is nearly impossible while Royal Guard is active. No new roll.

**Knights of the Peace and Royal Investigators:** Worldbuilding reference for Game Master scene framing. No new mechanics — Löwenritter's existing Intel and Influence stats already cover their capability. The arms tell the GM what these stats represent in fiction.

**Riskbreaker Identity (resolves ED-006):**

Riskbreakers have hidden Conviction: Valoria (nation as idea, not institution). When ordered to act against this conviction (e.g. coup enforcement that would destabilise the nation): Game Master rolls Riskbreaker Intel vs Ob 2. Success: comply. Failure: refuse or sabotage. TTRPG/Hybrid only.

Riskbreaker Deniability Debt: already in stage13. No changes.

## 4.3 Board Game

No new BG mechanics from Löwenritter structure. Existing stats cover capability. The arms are TTRPG narrative scaffolding.

## 4.4 Levy Rules

Crown may requisition 2/3 of vassal Military (round down) per season. Vassal refusal = Leadership Deviation (existing mechanics).

---

# 5. GUILD INTERNAL STRUCTURE

## 5.1 Reference (TTRPG Worldbuilding — Not Mechanics)

Guild hierarchy: Guild Masters (own businesses, sit on Council) → Free Masters (contractors) → Journeymen (qualified, mobile) → Apprentices (trainees).

Each guild elects a Council of five Guild Masters: set guild policy, liaise with government, resolve internal disputes, attend city Guild Forum.

Ministry of Guilds: Crown instrument that monitors guilds, arranges contracts, sets taxation, enforces non-competition. Crown-Guild interactions use existing Domain Action rules — no new mechanics needed.

Burgher status: Guild Masters and Free Masters qualify. Burghers may petition Parliament through the Ministry of Guilds.

## 5.2 Journeymen Years (Campaign Hook)

Player Character travels 3+ territories working in different guilds over 2+ seasons. Qualifies for Free Master. Broadens Circles (+1D guild contacts).

## 5.3 Guild Arbitration (ED-009 — Route to Debate System)

Proposal: 3-exchange proceeding. Pool: Wealth + relevant History. Audience biased toward guild autonomy. Not resolved here — route to debate system design doc for integration alongside Royal Audience and Church Tribunal.

ED-009 status: proposal pending debate system integration.

---

# 6. COURT PARLIAMENT AND GOVERNANCE

## 6.1 Reference (TTRPG Worldbuilding — Not Mechanics)

| Body | Composition | Function |
|------|-------------|----------|
| Imperial Court | Aristocrats, courtiers, advisors | Advisory. Informal power arena. |
| Court Parliament | Landed aristocrats + distinguished service aristocrats | Recommends policies, nominates Ministers/Rectorates/Magistrates. |
| Ministries | Headed by Ministers, nominated by Parliament, confirmed by Monarch | Execute government services. |
| Rectorates | Judicial. Nominated by Parliament, evaluated by Ministry of Law | Execute law. |
| Praefectures | Local governance by Civil Magistrates | Administer regions. |

Parliament recommends. Monarch decides. Existing Parliamentary Vote (stage6 §8.11) already handles contested votes. No new mechanics for routine Parliamentary business.

**Ducal Presence:** Dukes spend half their time or more at Imperial Court. If absent for a full season: halved Parliamentary Influence. Game Master note — TTRPG only.

## 6.2 Motion of No Confidence (New Mechanic — All Modes)

**Deposal procedure:** Constitutional right of Court Parliament to depose the Monarch if deemed unfit by BOTH the Holy See AND the Imperial Court.

| Step | Mechanic |
|------|----------|
| 1. Parliamentary Vote | Influence vs Crown Mandate (existing §8.11 procedure) |
| 2. Holy See concurrence | If Holy See concurs: deposal succeeds. If refuses: constitutional crisis. |

**Deposal consequences:**
- Crown Mandate → 1. Crown Stability −3.
- Succession: Torben inherits if available and loyal. If not: IP +10 (Altonian leverage). If no heir: interregnum (Parliament governs, all Crown Domain Actions +2 Ob).

**Holy See refusal consequences:**
- TC +3 (Church protects Monarch = Church gains leverage).
- Thread Tension (TT) +2 (institutional paralysis).

**BG expression:** Motion of No Confidence is a named variant of Parliamentary Vote with deposal as the stakes. Uses existing vote mechanics.

**Church leverage:** The deposal clause gives the Church structural veto over regime change. This is why Church political position is disproportionate to its military strength.

---

# 7. HISTORICAL CONTEXT (Setting Reference)

## 7.1 Three Indigenous Nations → Three Duchies

| Province (Altonian) | Duchy (Valorian) |
|--------------------|------------------|
| Valoria | Valorsmark |
| Baiamont | Hafenmark |
| Lupicco | Varfell |

Each duchy retains a pre-Altonian indigenous identity. Valorsmark adopted Church/Altonian culture most thoroughly. Hafenmark maintained strongest legal tradition. Varfell maintained strongest Einhir material culture connection.

## 7.2 Altonian Cultural Imperialism

Altonia systematically destroyed Valnese historical records, monuments, and temples. This is a political and cultural fact — NOT the source of the Forgetting. The Forgetting is epistemological (P-08): Thread knowledge is experiential and cannot be transmitted through text or institutional memory. The barrier is metaphysical and would exist even if every Einhir record survived. The Altonian destruction matters politically (grievance the Restoration Movement organises around) but has zero mechanical bearing on the epistemological barrier.

## 7.3 Cognatic Senior Succession

All three duchies follow cognatic senior succession — eldest child inherits regardless of gender. Elske is a legitimate Crown succession candidate. If Almud dies without Torben ratified: Elske's claim is legally strong but she is in Altonia — creating an IP crisis.

---

# 8. RESTORATION MOVEMENT LEADER (ED-005)

**Proposed Non-Player Character: Elder Solvei Kaldring**

| Attribute | Value |
|-----------|-------|
| Role | Southern Einhir elder. Informal authority in Korntal (T14) and Sudwald (T12). |
| Age | Late 60s |
| Thread Sensitivity (TS) | 22 (Dormant — elevated by proximity and lifelong cultural practice, but not a practitioner. Cannot bridge epistemological barrier per P-08.) |
| Conviction | Community |
| Resonant Style | Evidence |
| Composure | 9 (Presence 4 + 5) |
| Histories | Einhir Oral Tradition (3), Herbalism (2), Community Organising (2) |

**Belief:** *"The old ways are not dead. They are sleeping in the land and in us. I will not let them be forgotten while I am alive."*

**Mechanical role:** Contact point for Restoration affiliation (Circles Ob 2 southern territories, Ob 4 elsewhere). Provides cultural context for Community Weaving but cannot anchor it (TS 22 < 30 threshold). Needs a Player Character practitioner.

ED-005 status: proposal pending user approval (worldbuilding content).

---

# 9. TERRITORY MAPPING

## 9.1 Lore-to-Map Alignment

| Lore Territory | PP-199 Territory | Duchy (Lore) | Duchy (Map) | Notes |
|----------------|-----------------|-------------|-------------|-------|
| Valorsplatz | T12 | Valorsmark | Crown | Match |
| Lowenskyst | T8 | Valorsmark | Hafenmark | Historical vs current control |
| Himmelenger | T14 | Valorsmark | Church | Church controls cathedral city |
| Arcansheld | T9 | Valorsmark | Crown (shared) | Match |
| Stillhelm | T13 | Valorsmark | Crown | Match |
| Gransol | T5 | Hafenmark | Hafenmark | Match |
| Eidursjo | T6 | Hafenmark | Hafenmark | Match |
| Spartfell | T7 | Hafenmark | Hafenmark | Match |
| Varfell city | T1 | Varfell | Varfell | Match |
| Sigurdshelm | T2 | Varfell | Varfell | Match |
| Halvardshelm | T3 | Varfell | Varfell | Match |
| Oastad | T4 Vargstad | Varfell | Varfell | Name discrepancy (ED-NEW-05) |

## 9.2 Stage7-to-PP-199 Name Reconciliation

[EDITORIAL: ED-NEW-09 — Stage7 uses design-generated names (Hafenstadt, Kronmark, Sternhaven, etc.). PP-199 uses lore-derived names. Lore names govern where they exist. Design names retained where no lore equivalent exists. Definitive name table needed.]

---

# 10. EDITORIAL ITEMS

## New Items

| ID | Description | Priority |
|----|-------------|----------|
| ED-NEW-01 | Confirm Solmund as canonical First Founder name | P1 |
| ED-NEW-02 | Vaynard first name: Dienton (lore) vs Magnus (design) | P2 |
| ED-NEW-03 | Baralta spelling: Inga vs Inge | P3 |
| ED-NEW-04 | Church leader title: Holy See (formal) + Confessor (address) — both canonical? | P3 |
| ED-NEW-05 | T4 name: Oastad vs Vargstad | P3 |
| ED-NEW-06 | Cardinal of Prudence — name and profile | P2 |
| ED-NEW-07 | Almaic Kyriakos IP threshold interaction | P2 |
| ED-NEW-08 | Timeline reconciliation (canonical timeline governs) | P3 |
| ED-NEW-09 | Stage7-to-PP-199 territory name reconciliation | P2 |
| ED-NEW-10 | Naval mechanics as future design question (Lions' Helm) | P3 |

## Existing Items Addressed

| ID | Status |
|----|--------|
| ED-005 | Proposal: Elder Solvei Kaldring. Pending user approval. |
| ED-006 | Resolved: Riskbreakers loyal to Valoria concept, not institutions. Intel vs Ob 2 on divergence. |
| ED-009 | Routed to debate system design doc. Not resolved here. |

## Balance Flags

| ID | Concern |
|----|---------|
| BALANCE-FLAG-01 | Church cumulative passive bonuses from Cardinals (4 modifiers) + tithe Wealth + university Influence. Church already strongest by starting stats. Stress test required before any BG integration. |

---

# 11. WHAT WAS CUT AND WHY

| Proposal | Reason |
|----------|--------|
| Ministry of Guilds mechanics (§5.3 in v1) | Existing Domain Actions with flavour labels. No new strategic choice. |
| Guild PC advancement table (§5.4 in v1) | Character creation appendix, not faction design. |
| Prestige Economics (§6.2 in v1) | GM intuition, not a mechanic. |
| Ministry disruption mechanics (§6.3 in v1) | 4 parallel tracking systems for worldbuilding effects. Cognitive bloat. |
| Charity Network (§10.2 in v1) | Flavour rename of existing Wealth→Mandate Domain Action. |
| University Influence mechanic (§10.3 in v1) | Folded into BALANCE-FLAG-01. Not approved until Church balance verified. |
| Lions' Helm naval mechanics (§4.2 in v1) | No naval system exists. Scope creep. Flagged as future design question (ED-NEW-10). |
| Knights of Peace territory modifier (§4.2 in v1) | Redundant with Löwenritter Intel stat. |
| 4 named Parliamentary action sub-types (§6.2 in v1) | Existing Domain Actions with Parliament framing. Only Motion of No Confidence adds genuinely new mechanic. |
| Church levy contested roll (§3.4 in v1) | Redundant with Leadership Deviation mechanics. |

---

*End of Worldbuilding Integration v2. Proposals marked FLAG require simulation before BG integration. All worldbuilding content requires user editorial approval.*
