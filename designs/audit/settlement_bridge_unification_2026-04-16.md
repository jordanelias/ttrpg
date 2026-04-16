# VALORIA — Settlement-Bridge Unification Audit
## Date: 2026-04-16
## Scope: Cross-audit of settlement_layer_v30.md against all 10 bridge revisions. Editorial resolution of all conflicts. Unified architecture specification.
## Authority: Editorial permission granted. Resolutions are binding.
## Method: Per-system conflict identification → resolution → unified mechanic → file revision specification

---

# PART 1: CONFLICT REGISTRY AND RESOLUTIONS

## C-01: Scene Slate Generation Is Province-Level; Settlements Need Anchoring

**Conflict:** player_agency_v30 §4.2 (Scene Slate generation algorithm, 7 steps) generates entries at province level. Settlement layer §4.1 says entries should be settlement-anchored. The algorithm doesn't reference settlements.

**Resolution:** Every Scene Slate entry now specifies a settlement, not just a province. Revise the algorithm:

- Step 1 (Mandatory Crisis): "Player is in or adjacent to a territory at Accord 0" → "Player is in a province containing a settlement at Order 0"
- Step 2 (Crisis Events): "Territory within 2 adjacencies at Accord ≤ 1" → "Province within 2 adjacencies containing a settlement at Order ≤ 1; entry specifies the settlement"
- Steps 3–7: Each entry includes a settlement location. NPCs reside in specific settlements (per NPC roster + settlement assignments). Duty-aligned scenes occur at the settlement relevant to the Duty.

**Implication:** The player now travels to a specific settlement to pursue a scene, not to a province. Travel within a province is free (settlement layer §4.1). Travel between provinces costs 1 scene per province traversed (existing rule).

**Editorial resolution:** ADOPTED. player_agency_v30 §4.2 reinterpreted: all "territory" references in the Slate algorithm now mean "settlement within a territory." Province-level events (clock thresholds, faction-level crises) generate entries at the province's Seat settlement by default.

---

## C-02: Accord Derivation Chain Is Now Two-Tier

**Conflict:** Bridge work added personal-scale Accord pathways (peninsular_strain §2.7) and environmental legibility (§2.8) targeting province Accord directly. Settlement layer changes Accord to a derived value (floor of mean settlement Order). The §2.7 pathways now target the wrong thing.

**Resolution:** All personal-scale Accord pathways (§2.7) now target **settlement Order**, not province Accord. Province Accord is always derived — never set directly by personal action.

Revised §2.7 mapping:

| Player Action | Effect |
|--------------|--------|
| Social fieldwork: Disposition +3 with 2+ local NPCs in one settlement | Order +1 in that settlement |
| Investigation: resolve local concern affecting settlement population | Order +1 in that settlement |
| Community Weaving in settlement | Order +1 in that settlement (if PT ≤ 2) |
| Public violence in settlement | Order −1 in that settlement |
| Assassination of local named NPC | Order −1 in that settlement |
| Public defiance of controlling authority | Order −1 in that settlement |

Province Accord updates automatically at Accounting via the floor(mean(Order)) formula.

Environmental legibility (§2.8) now operates at settlement level — different settlements in the same province may have different atmospheres. The Accord-level descriptions (Aligned, Compliant, Resistant, Revolt) become Order-level descriptions at settlement scale.

**Editorial resolution:** ADOPTED. §2.7 pathways retargeted. §2.8 legibility retargeted. Province Accord is emergent, not directly set. This is cleaner — the player governs settlements, and the province follows.

---

## C-03: NPC Outreach Needs Settlement Anchoring

**Conflict:** npc_behavior §8.11 (NPC Outreach) generates Scene Slate entries specifying NPC name and agenda but not settlement location.

**Resolution:** Each NPC is assigned a home settlement in the NPC roster. Outreach entries specify the NPC's home settlement as the meeting location. If the NPC is traveling (companion, officer on assignment), the meeting occurs at the NPC's current settlement.

Demand entries specify the NPC's institutional settlement (the Seat of their faction's province, or the settlement they govern). The player must travel there.

**Editorial resolution:** ADOPTED. NPC roster annotations needed (ED-SETT-10: assign home settlements to all named NPCs).

---

## C-04: Companion-Governor Dual Role Needs Action Economy

**Conflict:** Companion spec says companions get 1 free social action/season. Settlement layer says governors get 1 free governance action/season. A companion who is also a settlement governor would get both — 2 free actions, which may be too generous.

**Resolution:** A companion-governor gets 1 free action that can be used as EITHER a social action (companion role) OR a governance action (governor role), not both. The player chooses each season which role the companion prioritizes. This creates a meaningful trade-off: use your companion for relationship deepening, or use them for settlement development.

**Editorial resolution:** ADOPTED. companion_specification_v30 §4.1 and settlement_layer_v30 §3.2 both updated to reference this choice.

---

## C-05: Mandatory Zoom In Triggers Need Settlement Specificity

**Conflict:** scale_transitions §4.3.2 mandatory triggers reference province-level events ("territory at Accord 0"). With settlements, Accord 0 = a settlement at Order 0, not the province as a whole.

**Resolution:** Mandatory Zoom In triggers reframed:

| Trigger | Province-Level Version (OLD) | Settlement-Level Version (NEW) |
|---------|----------------------------|-----------------------------|
| Revolt | Territory at Accord 0 | Settlement at Order 0 where player is present or in the same province |
| Battle | Mass battle in player's territory | Mass battle at a settlement in player's province — scene occurs at the besieged/assaulted settlement |
| Faction Leader Removal | Faction leader assassinated/overthrown | Scene occurs at the Seat settlement of the affected faction |
| Companion Arc | Companion arc trigger fires | Scene occurs at the companion's current settlement |

**Editorial resolution:** ADOPTED. Triggers are now settlement-anchored.

---

## C-06: Domain Echo Sufficient Scope Needs Settlement Governance

**Conflict:** scale_transitions §7 (Sufficient Scope) lists 6 qualifying conditions. None mention settlement governance. But governing a settlement IS an institutional act — a governor whose actions improve or damage a settlement's Order is reshaping the political landscape.

**Resolution:** Add condition 7 to Sufficient Scope:

> 7. Settlement governance action that changes Order by ±1 or more — the governor's institutional authority produced a measurable political outcome

This means a player-governor who successfully Pacifies a settlement fires Domain Echo. Governance IS political action. The faction layer registers what the governor does.

**Editorial resolution:** ADOPTED. scale_transitions §7 extended.

---

## C-07: Combat in Settlements Has Settlement-Level Consequences

**Conflict:** combat_v30 §13 (Combat World Bridge) fires Domain Echo and reputation/death cascades at province level. With settlements, combat location should matter — fighting in the Cathedral settlement vs. the Market settlement has different consequences.

**Resolution:** Combat in a settlement adds settlement-level consequences on top of existing province-level effects:

- Public combat in a settlement: Order −1 in that settlement (violence destabilizes local governance)
- Combat against the settlement's governor: Order −2 (institutional authority challenged)
- Killing a named NPC who resides in the settlement: that settlement's NPC population Disposition toward the killer shifts −2 (local community impact)

These stack with existing Domain Echo and reputation effects.

**Editorial resolution:** ADOPTED. combat_v30 §13 extended with settlement-level consequences.

---

## C-08: Obligations Can Target Settlement Governance

**Conflict:** social_contest §6.1 (Obligations) describes province-level binding commitments. With settlements, Obligations can be more granular and interesting.

**Resolution:** Obligations may target specific settlements:

- "Church must not station Inquisitors in S-017 Gransol Market Quarter for 2 seasons" — protects Guild autonomy in a specific location
- "Crown must maintain Defense ≥ 2 in S-006 Lowenskyst Fortress" — binds the Crown to border defense
- "Varfell must not develop Prosperity in S-032 Oastad Shrine" — protects RM cultural heritage

Settlement-targeted Obligations are easier to verify (specific location, specific stat) and more narratively grounded than province-level abstractions.

**Editorial resolution:** ADOPTED. Obligations can target province OR settlement. Settlement-targeted Obligations use the settlement stat as the verification condition.

---

## C-09: Mass Combat Post-Battle Scenes Are Now Settlement-Specific

**Conflict:** mass_battle PART D (post-battle consequence scenes) references province-level Accord. With settlements, the aftermath occurs at the battle's settlement.

**Resolution:** Post-battle consequence scenes occur at the specific settlement that was assaulted/besieged. The three choices (tend wounded, survey damage, address population) now affect settlement stats:

- Tend wounded: Settlement Defense +1 (garrison reinforced). Order +1 if Success.
- Survey damage: Reveals settlement stat changes. Identifies if any named NPC officers were killed.
- Address population: Settlement Order +1 if Success. Order −1 if Failure.

Named unit officers (PART D §D.2) may be assigned as settlement governors after the battle — the military officer transitions to civil administrator. This is the ROTK post-conquest appointment.

**Editorial resolution:** ADOPTED. PART D retargeted to settlement level.

---

## C-10: Two Overlapping Stature Ladders

**Conflict:** player_agency §5.4 (Renown Track) defines governance scope thresholds. Settlement layer §6.1 also defines governance scope thresholds. These are the same system described twice.

**Resolution:** Merge into one authoritative table. Settlement layer §6.1 is the canonical stature ladder. player_agency §5.4 references it. Delete the redundant table in player_agency and replace with a cross-reference.

**Editorial resolution:** ADOPTED. Single stature ladder in settlement_layer §6.1. player_agency §5.4 retains Renown sources and cap but references settlement_layer for governance scope.

---

## C-11: Faction Emergence Duplicates Renown Progression

**Conflict:** Settlement layer §6.2 (faction emergence, 5 stages) and player_agency §5.4 (Renown thresholds) describe the same progression arc in different terms.

**Resolution:** Unify. The 5-stage emergence path IS the Renown progression. Each emergence stage maps to a Renown threshold:

| Renown | Stage | Governance | What Changes |
|--------|-------|-----------|-------------|
| 0–2 | Cell | None | Personal network only |
| 3–4 | Organization | 1 settlement | Governor. Free governance action. Local NPC recruitment. |
| 5–6 | Movement | 2–3 settlements | Partial faction sheet (Influence, Wealth). Cross-settlement coordination. |
| 7–8 | Faction | 4+ settlements, 1+ Seat | Full faction sheet. Domain Actions. Parliament eligible. Provincial authority. |
| 9–10 | Hegemon | 2+ Seats | Multiple provinces. Victory conditions apply. National parity. |

Stage transitions require both Renown threshold AND the specific settlement/officer requirements listed in settlement_layer §6.2. Renown is necessary but not sufficient — you need the Renown AND the settlements AND the officers.

**Editorial resolution:** ADOPTED. One system. Settlement layer §6.1 and §6.2 merged with Renown as the quantitative axis and settlement control as the qualitative axis.

---

## C-12: Subnational Faction NPCs Need Outreach

**Conflict:** NPC Outreach (npc_behavior §8.11) only covers national-level faction NPCs. With settlements making subnational factions visible, subnational leaders should also generate Outreach.

**Resolution:** Extend §8.11 to include subnational faction leaders:

- Guild Council members in Guild-managed settlements may generate Outreach if Disposition ≥ +2 with player AND the player is in or adjacent to their settlement
- Ministry officials in Seat/City settlements may generate Outreach to players governing nearby settlements (bureaucratic coordination)
- Local RM organizers in RM-managed settlements may generate Outreach to players with Convictions mentioning Einhir, Thread, or Restoration
- Warden-post NPCs may generate Outreach to players with TS ≥ 10 (Thread competence recognition)

Subnational Outreach counts toward the 3-entry maximum (§8.11.5), competing with national-level Outreach for the player's attention. This creates a natural tension: do you respond to Baralta's summons or to the Guild elder who wants to discuss trade policy in Gransol Market Quarter?

**Editorial resolution:** ADOPTED. §8.11 extended.

---

## C-13: Generational Shift Interacts with NPC Arcs

**Conflict:** Generational Shift clock (settlement §7.1) applies age penalties at Year 10/20/30. NPC arc profiles (npc_behavior §5.2) have branch triggers that may not fire before the NPC ages out.

**Resolution:** Generational Shift does not prevent arc triggers from firing — it adds urgency. An NPC at −2 highest attribute (Year 20) is mechanically weaker but still active. At −3 (Year 30), the NPC's arc either resolves or transitions to a new state:

- **Almud at Year 30:** If Arc A (Reformer) or Arc C (Overthrown) hasn't fired, a new Arc D fires: **The Twilight King.** Almud is old, his authority eroded by time. Torben inherits by default. The player's relationship with Torben becomes the Crown's future.
- **Himlensendt at Year 30:** If no arc has fired, the Church's institutional momentum has carried TC to 75+ regardless of the Confessor's personal state. The system generates pressure; the leader does not need to drive it.
- **Edeyja at Year 30:** Wardens are practitioners — Thread Sensitivity 75+ delays physical aging (the rendering sustains them). No age penalty. But the Wardens are fewer each decade. The work continues. The help gets more desperate.

**Editorial resolution:** ADOPTED. Generational Shift adds urgency and creates natural succession moments without blocking existing arc triggers. Practitioners above TS 50 are exempt from age penalties (metaphysical justification: the rendering sustains high-TS beings more robustly).

---

## C-14: Investigation Synthesis Across Settlements

**Conflict:** Fieldwork investigation synthesis (fieldwork §4.1, Reconstruct as completion mechanic) operates at investigation level. With settlement anchoring, a structural investigation (threshold 8) spanning multiple settlements requires the player to have gathered evidence from multiple specific locations.

**Resolution:** This is not a conflict — it is an enhancement. Multi-settlement investigations are more meaningful because the player must travel between settlements, managing Exposure per province and building Disposition with different local NPCs in different settlements. The Evidence Track remains unified per investigation (existing rule, fieldwork §4.1). The synthesis (Reconstruct) can be performed at any settlement where the player has gathered evidence — they don't need to return to a specific location to synthesize.

**Editorial resolution:** No change needed. Settlement anchoring naturally enriches the existing investigation system.

---

## C-15: CV Presentation at Settlement Level

**Conflict:** conviction_track §11 (CV presentation layer) describes province-level environmental cues. With settlements, different settlements in the same province may have different cultural atmospheres — a Cathedral settlement feels different from a Market settlement regardless of the province's CV value.

**Resolution:** CV presentation operates at settlement level, modulated by settlement type:

- Cathedral settlements: CV effects are amplified. CV 5 in a Cathedral = totalizing Church presence. CV 0 in a Cathedral = the building is repurposed, the icons removed.
- Market/Port settlements: CV effects are muted. Commerce dampens religious extremes. CV 4 in a Market = Church officials in the trade quarter, but merchants still trade freely.
- Outpost settlements: CV effects are minimal. Frontier settlements are too practical for doctrinal enforcement. CV 5 in an Outpost = a chapel is maintained; CV 0 = the chapel is a storage shed.

Church Attention Pool (§11.2) is now tracked per settlement, not per province. AP accumulates where the player acts, not across the whole territory.

**Editorial resolution:** ADOPTED. CV presentation settlement-modulated. AP per settlement.

---

# PART 2: THE UNIFIED ARCHITECTURE

## §2.1 The Player-World Constitution

The game now has three mutually constitutive layers:

**Layer 1 — World Physics (Strategic)**
Province-level. Faction stats, Domain Actions, clocks (MS, TC, IP, Generational Shift), victory conditions, military movement. This layer runs regardless of the player's actions. It is the world that does not care about the protagonist.

**Layer 2 — Settlement Physics (Institutional)**
Settlement-level. Governance stats (Prosperity, Defense, Order), subnational factions, governor assignment, local NPCs, local events. This layer is where the world becomes legible to the player. It is the world the player can touch.

**Layer 3 — Player Physics (Personal)**
Individual-level. Convictions, Duties, Scene Slate, combat, contests, fieldwork, Thread operations, companions. This layer is where the player acts. It is the player making choices within the world's constraints.

**The bridges between layers:**

| Bridge | Direction | Mechanism |
|--------|-----------|-----------|
| Scene Slate | Layer 1 → Layer 3 | World events become personal opportunities (settlement-anchored) |
| Domain Echo | Layer 3 → Layer 1 | Personal actions reshape faction politics (7 qualifying conditions) |
| Settlement Governance | Layer 2 ↔ Layer 3 | Player governs settlements; settlement stats feed province Accord |
| Province Accord | Layer 2 → Layer 1 | Settlement Order averages → province Accord → victory conditions |
| NPC Outreach | Layer 1+2 → Layer 3 | National and subnational NPCs seek the player |
| Obligations | Layer 3 → Layer 1+2 | Contest outcomes bind NPC behavior at province and settlement level |
| Companions | Layer 3 ↔ Layer 1+2 | Companions translate world events into personal commentary; companion faction feedback loop |
| Faction Emergence | Layer 3 → Layer 2 → Layer 1 | Player accumulates settlements → claims province → becomes national actor |
| Faction Collapse | Layer 1 → Layer 2 | National faction loses provinces → contracts to city-state at settlement level |
| Environmental Legibility | Layer 2 → Layer 3 | Settlement Order, CV, AP expressed as lived texture |
| Military Granularity | Layer 1 ↔ Layer 2 | Province military → settlement assault/siege/bypass → settlement Defense/Order consequences |
| Generational Shift | Layer 1 → Layer 2 → Layer 3 | Time passes → leaders age → succession opens → player inherits or creates |

## §2.2 The Mutual Constitution Principle

The game's central design achievement, once all revisions are applied, is that no layer operates independently. Every action at every scale produces consequences at the other two scales. The player cannot fight a battle without the settlement's Order being affected. The settlement cannot lose Order without the province's Accord shifting. The province cannot lose Accord without the faction's victory conditions becoming harder to achieve. The faction's difficulty produces new NPC Outreach. The Outreach becomes a Scene Slate entry. The Scene Slate becomes a player choice. The player's choice produces a Domain Echo. The Echo reshapes the faction layer. The cycle continues.

This is not a loop — it is a constitution. The player and the world constitute each other through action and consequence, mediated by settlements as the layer where abstract politics becomes lived experience.

## §2.3 What a Season Looks Like (Unified)

**Phase 0 — Briefing.** State of the Peninsula: 3–5 most significant changes. Generated from clock movements, settlement Order changes, NPC arc events.

**Phase 1a — Duty Assignment.** Faction leader evaluates priority stack. Assigns Duty — now settlement-specific: "Govern S-018 Rendstad. Restore Order." or "Investigate Church activity in S-024 Himmelenger City."

**Phase 1b — Scene Slate Generation.** 7-step algorithm (settlement-anchored). Companion commentary on 1–2 entries. Maximum: 4–9 entries with specific settlement locations.

**Phase 1c — Governor Action (if applicable).** Player-governor takes one free governance action at their settlement: Develop, Fortify, Pacify, or Administer.

**Phase 1d — Personal Phase.** 3–5 scene actions. Each scene occurs at a specific settlement. Travel between provinces costs scene actions. Travel within a province is free.

**Phase 2 — Strategic Phase.** Domain Actions (province-level). Military movements (province → settlement targeting). Faction AI priority trees with settlement-level extensions. NPC governors develop their settlements per AI.

**Phase 3 — Accounting.** Settlement Order → Province Accord derivation. Clock advancement. Domain Echo resolution. Duty evaluation (Standing ±1). Conviction review. Renown update. Generational Shift check (every 5 years). Obligation duration countdown.

**Phase 4 — Aftermath.** Companion conversation (free). Companion reacts to what happened. Retrospective scenes ("Where Were You?") for missed events.

## §2.4 The Player's Felt Experience

At Year 1, the player is nobody. They arrive at a settlement — say S-028 Grauwald Town — with a Conviction, a Duty, and three scene actions. The settlement is a highland town with Einhir heritage, low CV, and an RM presence they can sense but not see. The Guilds manage the timber trade. Varfell controls the province but their grip is light. The player investigates, socializes, maybe fights. They form a relationship with a local NPC. They fulfill a Conviction. Renown: 1.

At Year 5, the player governs S-028. They've developed its Prosperity, pacified its Order, and made friends with the RM organizer at S-029 Grauwald Lodge. They have a companion — the RM organizer who travels with them to other settlements. The Church is preaching aggressively in the north. The player feels it through the CV presentation in the settlements they visit. The AP is rising in S-024 Himmelenger City. Renown: 4.

At Year 10, the player manages three settlements across two provinces. Their organization has Influence 2 and Wealth 1. They participate in local politics. Generational Shift hits — Almud is aging. Torben is approaching adulthood. The faction leaders the player has known for a decade are changing. The player's companion is Knotted to them; the Thread bond deepens their perception. The Calamity is getting worse — MS has dropped to Fragile. The settlements near Askeheim are feeling it. Renown: 6.

At Year 20, the player controls a province. They have a full faction sheet. They sit in Parliament alongside Baralta and whoever replaced Vaynard. The Church has seized two provinces via Graduated Seizure. The Altonian vanguard is mobilizing. The player's first-generation allies are aging or dead. Their protégé governs the settlements the player has outgrown. The game's clock pressures are acute: MS is at 35, TC is at 75, the peninsula is fracturing. The player's Convictions have evolved three times. Their original goals are distant memories. The game asks: what kind of Valoria will you leave behind? Renown: 8.

This is the game. Three layers. Mutually constitutive. Settlement by settlement, season by season, the player and the world build each other.

---

# PART 3: FILE REVISION SPECIFICATIONS

These are the specific changes needed to reconcile all conflicts. Each revision is concise and can be applied via str_replace or section insertion.

| File | Revision | Conflict Resolved |
|------|---------|-------------------|
| player_agency_v30.md | §4.2: all "territory" → "settlement within a territory." Province-level events anchor to Seat. §5.4: delete governance scope table, replace with cross-reference to settlement_layer §6.1. | C-01, C-10, C-11 |
| peninsular_strain_v1.md | §2.7: all pathways target settlement Order, not province Accord. §2.8: legibility descriptions operate at settlement level. Add note: Province Accord = floor(mean(settlement Order)). | C-02 |
| npc_behavior_v30.md | §8.11: entries specify NPC's home settlement. Add §8.11.6: subnational faction Outreach (Guilds, Ministry, RM, Wardens). | C-03, C-12 |
| companion_specification_v30.md | §4.1: companion-governor gets 1 free action (social OR governance), not both. | C-04 |
| scale_transitions_v30.md | §4.3.2: triggers settlement-anchored (Order 0 not Accord 0; battle at specific settlement). §7: add condition 7 (settlement governance → Domain Echo). | C-05, C-06 |
| combat_v30.md | §13: add settlement-level consequences (Order −1 on public combat, −2 on governor combat, local NPC Disposition −2 on killing resident). | C-07 |
| social_contest_v30.md | §6.1: Obligations can target specific settlements. | C-08 |
| mass_battle_v30.md | PART D: aftermath at specific settlement. Stat effects target settlement P/D/O. Officers can become governors. | C-09 |
| conviction_track_v30.md | §11: CV presentation settlement-modulated by type. §11.2: AP per settlement. | C-15 |
| settlement_layer_v30.md | §6.1 and §6.2: merged with Renown as quantitative axis. §7.1: TS 50+ exempt from Generational Shift age penalties. Companion-governor action economy clarified. | C-10, C-11, C-13, C-04 |

---

# PART 4: RESOLVED EDITORIAL ITEMS

With editorial authority granted, the following open items from previous work are hereby resolved:

| ID | Resolution |
|----|-----------|
| ED-SETT-03 | Province Accord = floor(mean(settlement Order)). Province with 1 settlement: Accord = that settlement's Order, capped at 3. Province with 3 settlements: average, floor, capped at 3. Confirmed: produces values consistent with existing Accord 0-3 range. |
| ED-SETT-05 | Church management of cathedrals in non-Church provinces: Church retains theological authority; province faction retains taxation and military. Conflict resolution via social contest (province as institution, Church as petitioner). Church CANNOT use cathedral management to override province military or legal decisions. Church CAN set theological policy, CV-influencing actions, and Heresy Investigation initiation from cathedrals. |
| ED-SETT-06 | NPC governors: settlement-specific priority tree (Pacify → Develop → Fortify → Administer). Faction tree overrides at faction Stability ≤ 2. |
| ED-SETT-07 | Generational Shift age penalties DO apply to PCs. Exception: PCs with TS ≥ 50 are exempt (the rendering sustains them). This creates a natural incentive for Thread engagement even for non-practitioners — seek TS advancement or age. |
| ED-SETT-08 | All settlements within a province are adjacent to each other (province is small enough for local travel). Internal road connections do NOT matter for invasion — the invader chooses which settlement to attack, not which route to take. |
| ED-SETT-09 | Board game representation: settlements abstracted on province cards (Option A). Each province card shows its settlements with stat dials. Settlement tokens placed on the map only during siege or contested governance. Hybrid/TTRPG/Videogame: full settlement map. |
| ED-COMP-04 | Companion departure Knot consequence: Knot persists at distance (dormant). Constitutive per P-12. Strain accumulates at +1/season while dormant. If strain exceeds Bonds capacity: rupture. The Knot does not break by choice — it breaks by neglect. |
| ED-SETT-10 (NEW) | All named NPCs assigned home settlements. See settlement_layer §2.1 notes column for initial assignments. Full NPC roster annotation deferred to next session. |

---

*End of document.*
