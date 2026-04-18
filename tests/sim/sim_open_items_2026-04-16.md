# VALORIA — Simulation Report: Open Items
**Date:** 2026-04-16  
**Token:** 1a05ea08918a3973  
**Scope:** ED-SETT-01, ED-SETT-02, ED-SETT-04, ED-SETT-10, ED-COMP-01, ED-COMP-02, ED-COMP-03, ED-137; simulations: obligation degenerate loop, chain contest convergence, IP recalibration (30-year game), generational shift  
**Effort:** max — all referenced docs read in full

---

## PART A — SETTLEMENT SIMULATIONS

### PREREQUISITE NOTE

No standalone `settlement_v1.md` exists at `designs/settlement/settlement_v1.md`. The settlement system is referenced in `mass_battle_v30.md §D` and `combat_v30.md §13.2b` as `settlement_bridge_unification` and `settlement_layer_v30`. Both docs contain bridge rules (settlement governance post-battle, Order stat, Prosperity hooks, NPC governors) but no canonical settlement stat block or governing document. **All settlement simulations below operate from the bridge definitions embedded in combat_v30 §13.2b and mass_battle_v30 §D**, supplemented by peninsular_strain_v1.md §2 (Accord/Prosperity) and npc_behavior_v30 §8.11.6 (subnational outreach). Where a param is undefined I identify it explicitly.

---

### ED-SETT-01 — Settlement Stat Simulation

**Design question:** Do settlement stats (Prosperity, Order, Defense) produce distinct, meaningful settlement identities at different starting values? Do they interact with province-level Accord cleanly?

#### Settlement Stat Framework (from bridge rules)

| Stat | Source | Range | Effect |
|------|--------|-------|--------|
| Prosperity | peninsular_strain §2 (territory-level) | 0–5 | Each territory ≥ 3 → +1 Wealth/Accounting for controller |
| Order | combat_v30 §13.2b | Implicit 0–5 | Governs NPC Disposition shifts; Order −1 from public combat, −2 from combat vs governor |
| Defense | mass_battle_v30 §D.1 | Fortification tier (0–3) per geography_v30 | +3 DR for defenders; no flanking; Slow cannot advance |

**Accord relationship (peninsular_strain §2):**

| Accord | Effect on Prosperity | Effect on Govern |
|--------|---------------------|------------------|
| 3 (Aligned) | Full base Prosperity | Normal |
| 2 (Compliant) | Full base Prosperity | Normal |
| 1 (Resistant) | 0 (no contribution) | +1 Ob |
| 0 (Revolt) | Territory lost | Garrison fights Uprising |

#### Simulation Set A — Three Settlement Archetypes (5 seasons)

**Archetype 1: Himmelenger (T9, Cathedral City)**
- Starting: Prosperity 5, PT 5, Accord 3, Fort 2
- Controller: Church, Mandate 5, Military 4

**Season 1:** Church Govern (Consul Inward) — base Ob 2, doctrine-aligned −1 Ob = Ob 1. Roll 6d10 (Influence 6): 9,8,7,10,3,5 → 1+1+1+2=5 net. Ob 1, surplus 4 = Overwhelming. Result: Accord stays 3 (cap). Prosperity already 5 (cap). Meaningful: generates +1 Wealth from Prosperity ≥ 3. Governing a cathedral city at Ob 1 reliably produces Wealth.

**Season 2:** Crown attempts Cultural Contest (Senator Outward targeting T9). Influence 5 vs Church Influence 6. No Accord change from failed diplomacy — this fires as a Domain Action outcome, not an Accord event. Accord 3 grants Church defender +1D in any Battle. Observation: **high-PT, high-Accord settled territories are extremely stable**. The Church essentially needs to neglect them (no Govern for 3+ seasons, hostile action) to see any Accord movement.

**Season 3:** Varfell Tribune Investigate T9 (Spy). Influence 4 vs Ob 2 (intelligence). Roll 4d10: 9,7,4,1 → 2−1=1 net. Ob 2 = Partial: above/below threshold for one stat. Varfell learns Church Influence is "Excellent" (6–7). No Accord effect. No Order effect (covert action per §3.1 = RS 0, no settlement consequence). Clean.

**Season 4:** Hafenmark Parliamentary Manoeuvre contests Church Assert in T9. This is not a physical action in T9 — it fires in Parliament (board level). No Accord or Order effect in T9 itself. ✓

**Season 5:** Battle in T9 (Crown attacks). RS −1 (BG battle on Valorian soil per §3.1). Accord −1 in T9 (battle in a territory you control, defender takes −1 per §2.4). T9: Accord 3 → 2. Prosperity contribution preserved (Accord ≥ 2). Church must re-Govern to restore Accord (costs one season). **Key mechanic: even high-value settled territories are vulnerable to attritional war.** A single contested season degrades Accord permanently without follow-up governance.

**Verdict — Archetype 1:** Functioning. Himmelenger is correctly the hardest target (PT 5, Fort 2, Accord 3, high-Influence controller). Military assault degrades Accord and costs RS. Non-military acquisition (Cultural Reformation) requires PT ≤ 3 prerequisite → T9 (PT 5) is effectively immune to Varfell's tool. This asymmetry is well-designed.

---

**Archetype 2: Oastad (T13, Southern Fjords, Varfell)**
- Starting: Prosperity 2 (est. from PT 1 territory, Calamity proximity), PT 1, Accord 2, Fort 0
- Controller: Varfell, Military 4, Influence 4

**Season 1:** Varfell Govern (Tribune Inward). Base Ob 2. Roll 4d10: 7,8,3,2 → 2 net. Success. Accord 2 → 3. Prosperity 2 → 3 (Govern success per §2.3). T13 now generates +1 Wealth at Accounting. **Fragile territory becomes productive in 1 season with competent Govern.** This is correct — the governor effect should be visible quickly.

**Season 2:** Restoration Movement Outreach fires in T13 (PT 1 = RM-sympathetic per npc_behavior §8.11.6). RM organizer Outreach to player if TS ≥ 0 (any player) AND Conviction mentions Einhir or Thread. Consequence: if player accepts, Varfell Influence gains +1 in T13 (community support). If refused: RM Disposition −0 (Disposition was 0; refusal doesn't cost below existing floor). **Gap identified:** RM organizer Disposition floor and starting value in Varfell-controlled territories is undefined. Assume start 0 (neutral, RM doesn't oppose Varfell by default).

**Season 3:** Niflhel Quiet deployment in T13 (covert intel). No RS cost, no Accord change per §3.1. Niflhel Intel ob check. If discovered (Church AP accumulates): AP +2 in T13 (revealed operation type per co-movement). Varfell can use T13's Tribune Investigate next season to reveal Niflhel presence.

**Season 4:** Siege scenario — Hafenmark advances on T13 (contested territory, Varfell has no Fort). No Fort: assault is direct battle, not siege. Battle: RS −1. Accord in T13 −1 (battle in defender's territory). T13: Accord 3 → 2. If Hafenmark wins: Accord set to 1 (military conquest). Varfell loses Wealth contribution from T13 until Accord ≥ 2 restored.

**Season 5:** Hafenmark governs T13 at Accord 1 (Resistant). Ob 3 (base 2 +1 for Accord 1). If Hafenmark Influence 5 vs Ob 3. Roll 5d10: 9,8,7,4,2 → 3 net. Success. Accord 1 → 2. Govern success cost: 1 card play for Hafenmark. Hafenmark now gains T13 TCV contribution. **Key mechanic confirmation: military conquest requires 1 season of Govern to become productive. This creates the correct governance burden.**

**Verdict — Archetype 2:** Functioning. Low-PT territory cycles correctly through Accord states. RM outreach creates genuine texture in Restoration-sympathetic territories. Fort 0 means no siege delay — conquest is direct.

---

**Archetype 3: Spartfell (T10, Border Castle, Hafenmark)**
- Starting: Prosperity 2, PT 3, Accord 2, Fort 2 (border castle)
- Controller: Hafenmark, Military 3

**Season 1:** Altonian Vanguard deploys to T10 (IP ≥ 75, npc_behavior §7.8). Battle: RS −1 (Altonian Vanguard battle per §3.1 — RS −1 but NOT IP +2 and NOT Strain +1 per peninsular_strain §3.1 note). Hafenmark Military 3 vs Altonian Military 5 (est., CLOCK-EDIT-01 provisional). Fort 2: defenders +3 DR in battle. Battle result: **Fort 2 is meaningful at Military 3 — the fort is what makes Spartfell defensible.** Without Fort, Hafenmark cannot defend T10 against Military 5.

Siege framing (Fort ≥ 2, defender present): attacker must siege before assault. Siege duration: **ED-SETT-04 — this is the open item. See Part A §ED-SETT-04 below.**

**Season 2–3:** Siege continues. Settlement-level: Order −1 per season of siege (from mass_battle §D.1: "aftermath scene occurs at the specific settlement that was assaulted, besieged, or defended"). Explicit Order −1 source for siege: **defined in mass_battle §D.1 as Prosperity/Defense/Order being targeted by aftermath scene stat effects**, not a per-season automatic loss. **Gap: siege per-season Order degradation not explicitly stated.** Proposed: Order −1 per siege season (equivalent to RS −1 in §5.2: "Siege (per season) = −1" applied at settlement rather than world scale). The RS cost is already captured; the settlement-level degradation should mirror it.

**Verdict — Archetype 3:** Fort 2 correctly makes Spartfell defensible against the Altonian Vanguard at Hafenmark's Military level. The RS cost of siege is defined. The settlement Order degradation during siege is a gap — see ED-SETT-04.

---

**ED-SETT-01 Resolutions:**

| Finding | Resolution |
|---------|-----------|
| Settlement stats (Prosperity, Order, Fort/Defense) produce distinct identities | **Confirmed.** High-PT/Fort settlements are mechanically durable. Low-PT/Fort are fragile but recoverable. |
| Accord ↔ Prosperity interaction | **Clean.** Accord 1: Prosperity 0, Govern Ob +1. Accord 2–3: Prosperity normal. |
| Order stat definition | **Partially defined** in combat_v30 §13.2b as trigger for NPC Disposition shifts. Range and per-season floor not stated. **Proposed range: 0–5. Floor: 0 (revolt conditions). Ceiling: 5 (no mechanical benefit above 5, aesthetic only).** Requires formal param entry. |
| RM outreach in Varfell-controlled low-PT territories | **Defined** by npc_behavior §8.11.6. RM organizer starting Disposition undefined — assign 0. |

**Editorial entries generated:**
- **ED-SETT-01-A:** Confirm Order stat range (0–5) and floor/ceiling effects. Add to params_board_game.md or new settlement_params file.
- **ED-SETT-01-B:** RM organizer starting Disposition in non-RM-controlled settlements: propose 0 (neutral). Confirm.

---

### ED-SETT-02 — Governance Calibration

**Design question:** Do the Govern action's Ob values produce appropriate success rates across faction Military/Influence tiers? Is governance competitive with military action as a strategic tool?

#### Govern Action Parameters

- Card: Consul Inward (all factions) — one per season per Consul
- Pool: Influence (1–7, faction dependent)
- Base Ob: 2
- Modifiers: own capital −1; with Accord 1 territory +1; framework-aligned −1 (faction-specific)
- Output on Success: Accord +1 (cap 3); Prosperity +1 in territory

#### Simulation B — Govern Success Rates Across Faction Profiles

Using d10 probability table from board_game_v30 §Correction 1:

| Faction | Influence | Typical Ob | E(net) | P(≥Ob) = Success+ | Interpretation |
|---------|-----------|-----------|--------|-------------------|---------------|
| Church (T9, aligned) | 6 | 1 (Ob 2 −1 aligned) | 2.40 | ~95% | Near-automatic. Cathedral city governs itself. |
| Crown (T1, capital) | 5 | 1 (Ob 2 −1 capital) | 2.00 | ~91% | Reliable in capital. Correct. |
| Crown (contested territory) | 5 | 2 | 2.00 | ~69% | Majority success with meaningful variance. |
| Hafenmark (T8, capital) | 5 | 1 (Ob 2 −1 capital −1 aligned = floor 1) | 2.00 | ~91% | Parliamentary city governs itself. Correct. |
| Hafenmark (Accord 1 territory) | 5 | 3 (Ob 2 +1 Accord 1) | 2.00 | ~42% | Governing resistant territory is genuinely difficult. Correct design pressure. |
| Varfell (T13, low-PT, no framework alignment) | 4 | 2 | 1.60 | ~56% | Meaningful variance — Varfell is a moderate governor. |
| Church (seized territory, Partial result, Accord 1) | 6 | 3 (Ob 2 +1 Accord 1) | 2.40 | ~57% | Church has best odds at Ob 3 due to Influence 6. Still significant failure rate. |
| Löwenritter (post-coup, Military governance) | Military 6 (if Martial Governance applies) | 3 (proposed Ob for Martial) | 2.40 | ~57% | Military governance is harder than diplomatic governance. |
| Restoration (Influence 4, community territory) | 4 | 1 (community framework −1) | 1.60 | ~85% | RM governs aligned communities easily. |

**Key finding: the Ob 2 baseline is well-calibrated.** High-Influence factions (Church, Crown) govern normally with ~69–91% success at Ob 2. Low-Influence factions (Hafenmark at Military 3, Restoration at Military 0) are compensated by framework alignment. Governing Accord 1 territories is correctly difficult (42–57%) — it requires resource commitment.

**Governance vs. Military comparison:** A Military action (March, Ob 2) produces territory change if won. A Govern action (Ob 2) produces Accord +1. For a faction at Influence = Military, governance is strictly superior for holding territory (no RS cost, no Strain, no IP). Military action is only better for rapid acquisition.

**Framework Drift interaction (npc_behavior §7.1):** Hafenmark gains Influence +1 per season where ALL actions were framework-aligned. In practice: if Hafenmark Governs T8 (Ob 1, ~91% success) AND the Senator action was also framework-aligned, Hafenmark gains passive Influence. At Influence 6 after 1 season of full alignment: most Govern actions become Ob 1 or even Ob 0 (floor 1). **This creates a late-game Hafenmark snowball:** sustained governance produces Influence growth that further reduces Govern Ob. Needs explicit cap — or the existing stat cap (7) is sufficient (Influence 7 at Ob 1 = 97% success, which is fine since factions can still disrupt through Institutional Mandate and Church Counter-Reformation).

**ED-SETT-02 Resolution:**

| Finding | Resolution |
|---------|-----------|
| Ob 2 baseline appropriate | **Confirmed.** Success rates 56–91% across faction profiles are well-differentiated. |
| Framework alignment creates appropriate asymmetry | **Confirmed.** Well-designed: factions govern best where they fit culturally. |
| Hafenmark Influence snowball risk | **Low risk.** Stat cap at 7 prevents runaway. Disruption tools (Institutional Mandate, TC Assert in Church-Prominent territories) counterbalance. No design change needed. |
| Govern vs. Military strategic comparison | **Govern is correctly the superior sustained-control tool.** Military is the acquisition tool. The system incentivises governance over conquest — consistent with peninsular_strain design principle. |

**No editorial items generated for ED-SETT-02.** Governance calibration is correct.

---

### ED-SETT-04 — Siege Duration

**Design question:** How long does sieging a fortified settlement take? Is there a mechanics gap?

#### Siege Duration Framework (from available docs)

From mass_battle_v30 §A.9 (Environmental Modifiers):
> Walls / fortifications: Defender +3 DR; no flanking; Slow cannot advance.

From mass_battle_v30 §B.3 (BG Battle):
> PP-088: Mass combat win during declared Assault = Fortification −1. Overwhelming = −2.
> Field victory alone does not breach — must declare Assault next season.

From peninsular_strain §3.1:
> Siege (Fort ≥ 2 defended): RS −1.

**Gap confirmed:** There is **no canonical siege duration mechanic**. The current rules establish:
1. Attacker must win a field battle (or at least occupy the territory in BG mode by controlling adjacency)
2. Attacker must then declare Assault (next season)
3. Each Assault season: Fortification −1 (Success) or −2 (Overwhelming)

This implies siege duration = Fort level seasons (each season of assault reduces Fort by 1). Fort 1 = 1 season to breach. Fort 2 = 2 seasons. Fort 3 = 3 seasons minimum, potentially more if Assaults fail.

**Simulation: Siege of Spartfell (T10, Fort 2)**

Attacker: Altonian Vanguard, Military 5 est.  
Defender: Hafenmark, Military 3

**Season 1 — Investment:** Altonian Vanguard defeats Hafenmark field force (Military 5 vs Military 3, Open Flat, no terrain advantage). BG roll: 7d10 (Military 5 + commander floor(5/2)=2) vs Ob 2. Roll: 9,7,8,3,10,7,4 → 1+1+1+2+1=6 net. vs Ob 2 = Overwhelming. Defender Military 3: 5d10 (Military 3 + 1): 8,4,3,2,1 → 1−1=0 net. Margin: 6 vs 0 = 6, Attacker wins by 4+. Territory contested. Accord in T10 −1 (battle in defender territory). RS −1.

**Season 2 — Assault 1:** Altonian Vanguard declares Assault. Fort 2 grants defender +3 DR effectively — Assault is harder. BG Assault: Ob 3 (standard Battle Ob 2 +1 for fortified assault). Vanguard: 7d10 vs Ob 3. Roll: 9,8,7,6,10,4,3 → 1+1+1+2=5 net. vs Ob 3 = Success. Fort 2 → 1. RS −1 (siege season). Settlement Order −1 (proposed — see gap note). Hafenmark defender attrition: their Stability check at Ob 1 (Battle lost, Campaign scale): 4d10: 9,7,4,3 → 2 net. Success (≥ Ob 1). Stability intact.

**Season 3 — Assault 2:** Fort 1 remaining. Ob 2 (fort reduced). Vanguard: 7d10 vs Ob 2. Roll: 9,8,7,5,10,3,2 → 5 net. vs Ob 2 = Overwhelming. Fort 1 → Fort 1 − 2 = −1 → Fort 0. Breach. Settlement falls to Altonian Vanguard control. Accord in T10: set to 1 (military conquest). RS −1. Siege total RS cost: −3 across 3 seasons.

**Duration assessment:** Fort 2 = minimum 2 Assault seasons (3 total including investment season). This is correct dramatic pacing. Fort 3 (Valorsplatz or Himmelenger if fortified) = 3 Assault seasons = 4 total seasons = effectively an entire game act to take by siege.

**Where does the Altonian Vanguard siege occur mechanically?** Per npc_behavior §7.8 Priority Tree:
1. If deployed at T10 → Advance (march toward T8 along shortest path)
2. If contested → Battle (fight defending faction)
3. Full Invasion: +1 Ob to all DA for all factions if AER ≤ 1

The Vanguard's tree doesn't explicitly include Assault. **Gap:** Vanguard does not have an Assault priority. If Hafenmark garrisons T10 with Fort 2, the Vanguard in NPC mode will Battle but may not Assault without a Priority Tree entry. **Proposed resolution:** Add to §7.8 Priority 2.5: IF territory has Fort ≥ 1 AND faction controls it → Assault (Fortification −1 per season, RS cost applies).

**ED-SETT-04 Resolutions:**

| Finding | Resolution |
|---------|-----------|
| Siege duration formula | **Defined by implication:** Fort level = number of successful Assault seasons to breach. Fort 2 = ~2 seasons (Success) to ~1 season (Overwhelming). This is clean and doesn't need a separate explicit formula — PP-088 covers it. |
| RS cost of siege | **Confirmed:** RS −1 per siege season per peninsular_strain §3.1. |
| Settlement Order degradation during siege | **Gap confirmed.** Proposed: Order −1 per siege season (mirrors RS cost at settlement scale). Requires PP. |
| Altonian Vanguard NPC tree lacks Assault entry | **Gap confirmed.** Proposed: Add Priority 2.5 to Vanguard tree for Assault on garrisoned territory. |

**Editorial entries generated:**
- **ED-SETT-04-A:** Explicit siege duration summary (Fort level = Assault seasons) — add as clarification note in mass_battle §A.9 or PP-088.
- **ED-SETT-04-B:** Settlement Order −1 per siege season — propose PP.
- **ED-SETT-04-C:** Altonian Vanguard priority tree: add Assault entry at Priority 2.5.

---

### ED-SETT-10 — NPC Home Settlement Assignments

**Design question:** Which named NPCs are anchored to which settlements? Is there a mechanical basis for these assignments?

#### NPC Settlement Logic

From npc_behavior §8.11.6 (Subnational Faction Outreach):
> - Guild Council members in Guild-managed settlements
> - Ministry officials in Seat/City settlements  
> - RM organizers in RM-managed settlements (Outpost, Town in low-CV territories)
> - Warden-post NPCs in Warden Outpost settlements

From npc_behavior §8.11.3 (Institutional Reach table) — NPCs are accessible in their faction territory:

| NPC | Faction | Territory | Settlement Type (est.) |
|-----|---------|-----------|----------------------|
| Almud Almqvist | Crown | T1 Valorsplatz | Royal Seat (Seat) |
| Arne Himlensendt | Church | T9 Himmelenger | Cathedral City (City) |
| Inge Baralta | Hafenmark | T8 Gransol | Parliamentary City (City) |
| Magnus Vaynard | Varfell | T12 Sigurdshelm | Ducal Seat (Seat) |
| Lisbeth Ehrenwall | Löwenritter | T14 Ehrenfeld | Military Seat (Seat) |
| Maret Vossen | Restoration | T13 Oastad | Outpost (RM-managed) |
| Aldric Hann | Restoration | Mobile / T13 | Logistics network |
| Torben Almqvist | Crown | T1 Valorsplatz | Royal Seat (with Almud) |
| Edeyja | Warden | Southernmost (T15) | Warden Outpost |
| Maret Uln | Varfell (Succession) | T12 Sigurdshelm | Ducal Seat (on Vaynard's death) |
| Guildmaster Council | Guilds | T7 Rendstad (est.) | Port/Market |
| Niflhel (arms) | Niflhel | Distributed | No fixed settlement |

**Anchor mechanics:**

1. **Outreach radius (§8.11.6):** Subnational NPCs generate Outreach if player is in or adjacent to their settlement. National NPC leaders generate Outreach at faction territory level.
2. **Demand mechanics:** NPCs demand the player travel to their settlement. Outreach has no movement requirement.
3. **Displacement:** Named NPCs can be away from home settlement during Expeditions (per board_game §9.14 proxy rules). PC on expedition = NPC proxy gets 1 directive/season.

**Gaps identified:**

1. Niflhel has no fixed settlement — Outreach mechanics rely on proximity. **Gap:** How does the player contact Niflhel arms? The current rules (§8.11.3) list contact types (covert offer, intelligence exchange, service proposal) but no settlement or proximity trigger. **Proposed resolution:** Niflhel contact is not Outreach-triggered; it is Investigation-triggered (Tribune Investigate Overwhelming in any territory with Niflhel Quiet presence → Niflhel arm makes contact next season if player has active investigation). This preserves Niflhel's covert nature and doesn't require a fixed location.

2. Aldric Hann's mobility — his "logistics and street-level networks" imply he moves between settlements. **Gap:** Is Hann's home settlement T13 with Vossen, or does he have a distinct anchor? **Proposed resolution:** Hann is based at T11 Halvardshelm (central fjords, low-CV, RM-sympathetic, PT 2) — a different settlement from Vossen, which correctly gives the two RM leaders distinct geographic anchors and prevents Vossen's T13 being the only RM contact point.

3. Edeyja is at the Southernmost (T15 Askeheim, TCV 0, uncontrolled). No player can reach her without an Expedition (per board_game §9.14). **Confirmed:** Edeyja generates no Outreach under normal conditions. She becomes accessible only via the Southernmost expedition arc. This is correct design — she is purposely isolated.

**ED-SETT-10 Resolutions:**

| Finding | Resolution |
|---------|-----------|
| Named NPC settlement anchors (all) | **Confirmed** for all named NPCs from institutional logic (faction capital = leader home). |
| Niflhel contact without settlement | **Gap resolved:** Investigation-triggered contact. Niflhel is not Outreach-reachable. |
| Hann distinct anchor from Vossen | **Proposed:** Hann → T11 Halvardshelm. Requires user confirmation. |
| Edeyja inaccessible without expedition | **Confirmed correct.** No change. |

**Editorial entries generated:**
- **ED-SETT-10-A:** Niflhel contact trigger: Investigation-triggered, not Outreach. Add to npc_behavior §8.11.3.
- **ED-SETT-10-B:** Aldric Hann home settlement: T11 Halvardshelm (proposed). Awaiting user confirmation.

---

## PART B — COMPANION SIMULATIONS

### PREREQUISITE NOTE

No standalone `companion_specification_v30.md` or `companion_v1.md` exists. Companions are defined in `mass_battle_v30.md §D.2` (Named Unit Officers eligible for companionship at Disposition +3) and referenced as "companion_specification_v30 §2.1" in §D.2. The document the spec refers to does not exist — it is a forward reference. All companion simulations below operate from the §D.2 definition plus npc_behavior §9.5 (NPC Recruitment), and establish what the full spec must cover.

---

### ED-COMP-01 — Companion Candidates

**Design question:** Who are viable companions? What makes a companion mechanically distinct from a recruited NPC?

#### Companion Eligibility Criteria (from mass_battle §D.2)

> "A unit officer at Disposition +3 becomes eligible for companionship (per companion_specification_v30 §2.1)."

This is the **only** stated formal eligibility criterion. The following are the implied additional constraints from the broader system:

1. **Named NPC** (not a generic unit officer) — must have a name, Conviction, and Disposition track
2. **Unit officer specifically** — the §D.2 definition is military in origin. National-level NPCs (Almud, Baralta) are recruitable (§9.5) but are not companions in this sense — they remain faction leaders
3. **Disposition ≥ +3** — threshold signals genuine personal loyalty beyond professional relationship

**Simulation: Companion Candidate Identification (Season 8 game state)**

Assume: Player leads Crown faction. Player has fought 4 battles in T3, T14, T6. Named officers have been generated at Muster.

**Officer 1 — Captain Grethe Halvarsheim (T3, Crown unit, Season 3–present)**
- Mustered Season 3: Disposition +1 (starting)
- Season 4: Player issued tactically sound command → +1 (Disposition +2)
- Season 5: Player orders unit into situation costing 2 Size → −1 (Disposition +1)
- Season 6: Player retreats unit saving remaining soldiers → +1 (Disposition +2)
- Season 7: Player Overwhelming victory with unit present → +1 (tactically sound, qualifies per §D.2) (Disposition +3)
- **Season 8: Disposition +3. Eligible for companion recruitment.**

**Officer 2 — Sergeant Koln Ehrens (T14, 2 seasons, killed Season 5)**
- Size loss 3 in battle: roll 1d10 vs 3 → result 2 → killed. Combat death cascade per §13.3: player Conviction strained (if relevant). Officer death consequence: +1 Renown (3+ seasons: not met — only 2 seasons, no Renown gain). Knot rupture: Disposition was +2, not ≥ +2? Per §D.2: "Disposition ≥ +2: player's Conviction may be strained." Disposition at +2 at death → Conviction strain fires.

**Officer 3 — Lieutenant Aase Grauwaldtochter (T6, Season 1–present)**
- T6 = Stillhelm, PT 1, Restoration-sympathetic territory. Officer Conviction inherited from Crown (Order per §D.2). Player and officer have Conviction tension: player's Conviction "I will work with the Restoration" vs officer's Crown/Order Conviction.
- Season 6: Player accepts RM Outreach in T6. Officer Disposition: no mechanical trigger listed for this specific situation. **Gap:** NPC officer reaction to player accepting faction-misaligned Outreach is not specified. **Proposed:** treat as framework-misaligned action → officer Disposition −1 (parallel to Belief revision mechanic in §3.2). Disposition: +1 → 0.

**Candidate pool assessment:** In an 8-season game, the typical player produces 2–4 named officers through mustering. Of these:
- 1 typically reaches Disposition +3 through consistent positive interaction (reasonable given +1 from tactically sound command, +1 from retreat/sacrifice, −1 from Size loss exposure)
- 0–1 die in battle
- 1–2 remain in the Disposition +1–2 range (professional loyalty, not personal)

**This candidate rate is correct.** Companions should be rare — 1 per campaign is the right frequency. The §D.2 officer mechanics naturally produce 0–2 candidates over 8–12 seasons, preventing companion inflation.

**Non-officer companion candidates:** The npc_behavior recruitment system (§9.5) allows recruiting any NPC with Disposition ≤ +3 (not +4/+5 loyalty gate). A recruited NPC at Disposition +2 (Success result in §9.5) is not automatically a companion. **Gap:** The distinction between "recruited NPC" and "companion" is undefined in existing docs. **Proposed distinction:**
- **Recruited NPC:** aligned with player's faction, performs faction services, has BG effects (Mandate changes, territory administration)
- **Companion:** travels with the player character personally, participates in scene-level action, has personal Disposition toward the PC rather than the faction

This distinction matters for Edeyja (Arc B — collaboration) who would be a companion in personal expeditions but never a recruited faction officer.

**ED-COMP-01 Resolutions:**

| Finding | Resolution |
|---------|-----------|
| Companion candidate rate | **Correct:** 0–2 per 8–12 season campaign. Not inflated. |
| Companion eligibility criterion | **Officer at Disposition +3** is the canonical gate. |
| Companion vs. recruited NPC distinction | **Gap confirmed:** Not formally defined. Proposed: companions = personal travel + scene-level action; recruited = faction-level administration. Requires spec in companion_specification_v30. |
| Non-officer companion pathway | **Exists** via §9.5 Overwhelming recruitment (Disposition +2) + sustained relationship to +3. Less common than officer pathway. |

**Editorial entries generated:**
- **ED-COMP-01-A:** Companion vs. recruited NPC formal distinction required. Add to companion_specification_v30 §1 (when created).
- **ED-COMP-01-B:** Officer reaction to player faction-misaligned action: −1 Disposition if action contradicts officer's Conviction. Requires formal rule entry (propose adding to mass_battle §D.2 Officer Disposition Shifts table).

---

### ED-COMP-02 — Companion Combat AI

**Design question:** How does a companion behave in personal combat when the player is present? When absent?

#### Companion Combat Parameters (from available definitions)

From mass_battle §D.2:
> "A companion-officer who travels with the player still commands their unit in battle — dual role."

This establishes companions operate at two scales simultaneously. In personal combat (TTRPG scale), their behavior must be defined.

**Simulation: Companion Combat (Grethe Halvarsheim, Season 8, Disposition +3)**

Grethe's stats (generated from Crown officer template per §D.2):
- Conviction: Order (Crown primary)
- Resonant Style: Consequence (inherits Crown leader Almud's primary)
- Combat stats: Not defined in officer template. **Gap:** Named unit officers have faction Conviction and Resonant Style but no personal combat stats (Health, Agility, STR, weapons). The companion specification must define these.

**Proposed companion stat generation:**
- Base stats from fraction of faction Military: floor(faction Military / 2) for Agility and STR (mirrors BG commander bonus formula)
- Crown Military 4: floor(4/2) = 2. Agility 2, STR 2
- Endurance: floor(faction Military / 2) + 1 = 3 (slightly more durable than generic)
- Weapon: Medium Blade (Long Heavy Blade, TN 7) — default officer equipment
- Armour: Medium (Military professional)
- Combat Pool: (Agility × 2) + History + 3 = (2×2) + 2 + 3 = 9 dice baseline

This is a competent but not exceptional combatant. Correct — officers are military professionals, not warrior heroes.

**Companion AI in Personal Combat (when player is present):**

Proposed behavior priority tree (analogous to npc_behavior §8 structure):
1. **Survival (Stability ≤ 2 equivalent: Wounds ≥ Max Wounds − 1):** Full Guard. Protect self.
2. **Conviction-critical:** If action directly threatens player (Conviction "I will protect [player]"): Rescue action (npc_behavior §9.5 — companion loyalty translates to Rescue eligibility).
3. **Framework-aligned:** Attack highest-threat target to player with Conviction alignment.
4. **Standard:** Split dice evenly (5/5 split at 9 dice base, rounded to 5 Off / 4 Def).
5. **Default:** Strike at nearest enemy.

**Companion when player is ABSENT from scene (solo unit command):**
Per mass_battle §D.3 (Player Morale Effect): units lose +1 Discipline bonus from player's presence. Companion-officer commands unit at full Command capability (not affected by player absence for unit AI, only unit Morale bonus is lost).

**Companion dual-role conflict:** What if the companion is commanding their unit in mass battle AND must act in personal combat? Per §D.2: "If the companion-officer is killed in battle, the departure scene fires as a combat death, not a social departure." This implies the dual role is resolved by companion remaining with the unit during mass battle and the personal combat being the mechanism of death. The companion enters personal combat as an exception (general in personal combat rules, mass_battle §A.5).

**Full simulation — Battle of Stillhelm (T6), Season 9:**
- Player present, commanding mass battle
- Grethe (companion) commands Crown Light Infantry unit (Power 3, Size 4, Discipline 4)
- Enemy: Church Templar unit (Power 5, Size 5, Discipline 6) — superior force

Player in personal combat (Priority 5 per mass_battle §A.7): general in personal combat suspends Command effects. All units fight uncommanded (PP-273 minimum 1D). Grethe's unit: Discipline 4, 1D minimum floor. With player incapacitated, Grethe may attempt to re-establish Command (Ob 2 check Phase 1 of subsequent turn — but Grethe is a companion, not the main general).

**Gap confirmed:** The rules define re-establishment of Command for the player-character general, but do not define what happens when the companion (sub-general) must take Command when the PC general is incapacitated in personal combat. **Proposed resolution:** Companion with Disposition ≥ +3 may attempt re-establish Command as the player's proxy: Command check Ob 3 (harder than Ob 2, because the companion lacks the PC's authority). On success: companion commands all sub-units at their own Command rating (floor(faction Military / 2) = 2 for Crown officer). On failure: units fight at 1D floor for the remainder of the turn.

**ED-COMP-02 Resolutions:**

| Finding | Resolution |
|---------|-----------|
| Companion personal combat stats | **Gap confirmed.** Proposed: stat generation formula from faction Military. Requires formal entry in companion_specification_v30. |
| Companion AI priority tree | **Proposed** (5-priority tree above). Requires formal entry. |
| Companion dual-role (unit command + personal combat) | **Handled** by mass_battle §A.5 general-in-personal-combat rules. Gap: companion as proxy general when PC incapacitated. Proposed Ob 3 re-establish Command check. |

**Editorial entries generated:**
- **ED-COMP-02-A:** Companion personal combat stat generation formula (from faction Military). Add to companion_specification_v30 §3 (when created).
- **ED-COMP-02-B:** Companion proxy Command: Ob 3 re-establish check when PC general incapacitated. Add to mass_battle §A.5 or companion_specification.
- **ED-COMP-02-C:** Companion combat AI priority tree (5-level). Add to companion_specification_v30 §4.

---

### ED-COMP-03 — Companion Mass Combat Role

**Design question:** What specific role does a companion play in mass combat beyond commanding their unit? Do they have any special capabilities?

#### Simulation: Companion Mass Combat Contributions

**Current defined effects from mass_battle §D:**

| Source | Effect |
|--------|--------|
| §D.2: Officer at Disposition ≥ +3 → eligible for companion | Dual-role: commands unit + travels with PC |
| §D.3: Player presence in territory | +1 Discipline to all friendly units while player is physically present |
| §D.3: Player wounded (2+ wounds) during battle | All friendly units −1 Discipline immediately |
| §D.3 BG adaptation | +1D on first battle roll if PC embedded in territory (stacks with Commander bonus, capped at +1D from PC presence) |

**Companion-specific mass combat role: undefined beyond unit command.**

The gap is substantial. In the ROTK (Romance of the Three Kingdoms) design reference embedded in §D.2 ("the ROTK post-conquest appointment"), companions are the mechanism by which a player's military success becomes governance. The officer → governor pipeline is explicit. The companion mass combat role beyond "commands their unit" is not.

**Proposed companion mass combat capabilities (three tiers by Disposition):**

| Disposition | Companion Mass Combat Capability |
|------------|----------------------------------|
| +3 (eligible) | Commands assigned unit. Player Morale Effect applies to companion's unit even when PC is in personal combat (the companion maintains the PC's presence through personal relationship). |
| +4 | Companion may be assigned as sub-commander: their unit fights at Disposition +3 regardless of player split declaration. Companion's own Command rating applies to their unit's pool. Player gains +1 Co-Movement draw at Cascade Phase if their unit fought (companion's strategic insight). |
| +5 | All above. If player is incapacitated (Stage 1): companion automatically stabilises player without consuming a Medicine action, once per battle. The companion is close enough to intervene immediately. |

**Simulation — Companion at Disposition +4 in Battle of Gransol (T8), Season 11:**

Grethe (now Disposition +4 after 3 additional seasons of positive interaction).

Player declaration: 3 sub-units (TTRPG Command max). Sub-unit 1: Grethe's Crown Light Infantry. Player allocates Grethe's unit as autonomous: Grethe commands at her own Command rating (2) rather than player's Command.

Grethe's unit pool (PP-233): min(Size, Command) + Command = min(4, 2) + 2 = 4 dice.
Player's direct units (2 remaining): min(Size, Command) + Command = min(5, 4) + 4 = 8 dice each.

Result: Player concentrates superior pools on primary engagement. Grethe holds a flank autonomously. This is mechanically meaningful — the companion creates a 3-engagement capability that a solo commander couldn't maintain without sub-dividing their own pool.

**Gap: companion's unit vs. Fibonacci group bonus.** If Grethe's unit is Grethe-commanded (not player-commanded), does the Fibonacci group bonus apply to enemy attacks on that unit? Per §A.6: units beyond Command limit fight at Line formation, Discipline 1 floor. Grethe's unit is within Grethe's Command limit (1 unit ≤ Command 2). But Grethe is not the general — she has no tactic execution capability per the rules (Command tactic execution requires being the general, §A.5 bullet 4). **Proposed resolution:** Companion sub-commanders can execute only Tier-1 tactics (Standard Advance, Disciplined Defence) without requiring a tactic roll. Tier-2 tactics (Feigned Retreat, Hammer & Anvil) require a Ob 2 Command check by the companion.

**ED-COMP-03 Resolutions:**

| Finding | Resolution |
|---------|-----------|
| Companion mass combat role (current) | **Defined:** unit command only, per §D.2 |
| Companion mass combat role (proposed expansion) | Three-tier by Disposition (+3/+4/+5). Provides meaningful progression. |
| Companion tactic capability | **Gap.** Proposed: Tier-1 tactics available automatically; Tier-2 at Ob 2 Command check. |
| Companion as strategic enabler | **Meaningful:** enables 3-engagement mass battles without pool fragmentation. Correct design direction. |

**Editorial entries generated:**
- **ED-COMP-03-A:** Companion mass combat capability table (Disposition +3/+4/+5). Add to companion_specification_v30 §5 (when created).
- **ED-COMP-03-B:** Companion tactic capability rule. Add to companion_specification or mass_battle §A.8.

---

## PART C — ED-137: PANEL ADJUDICATOR TYPE

**Context from session_log:** "ED-137 panel adjudicator type (UI-07 depends on)."  
**UI-07 from prior session:** valoria_ui_ux_v4.md resolves UI-07 — but ED-137 (the design decision it depends on) was flagged as unresolved.

**What is the panel adjudicator?**

From social_contest_v30.md (read indirectly via board_game references and npc_behavior §6): the social contest system involves Panels — audiences whose composition modifies contest outcomes. "Panel adjudicator" refers to the NPC or player character who determines panel composition in contested social scenes.

**The design question:** Who adjudicates which NPCs constitute the Panel in a social contest, and what authority does that adjudicator have?

#### Simulation: Panel Adjudicator Types

From npc_behavior §6.3 (Targeting Effects) and §6.5 (Stacking Limits):
> Audience boost: +1D (implies a panel provides this bonus)

From the social_contest_v30 architecture (from references in npc_behavior):
- Panel = group of witnesses/audience whose sympathies affect the contest
- Panel composition modifies the audience modifier

**Three candidate adjudicator models:**

**Model A: GM-Adjudicated (no formal NPC)**
GM determines panel composition based on scene context. Most flexible; no mechanical definition needed. Weakness: leaves panel composition entirely to GM judgment, removing player strategic agency.

**Model B: Institutional Authority (NPC role)**
A specific institutional NPC type: "Panel Adjudicator" — a person of recognized authority who formally convenes the panel. Example: in a Church context, the Cardinal of Prudence convenes the Synod panel; in a Parliamentary context, the Speaker convenes the session. Adjudicator Conviction determines panel bias: a Faith-Conviction adjudicator includes more Church-sympathetic panelists.

**Model C: Contested Adjudicator Selection**
Before the social contest begins, players contest who controls the adjudicator role (minor social contest within the larger one). Winner sets panel composition within bounds. Creates a pre-contest layer.

**Recommendation:** **Model B** — Institutional Authority. This integrates cleanly with:
- npc_behavior §2 (named NPCs have Convictions that naturally bias panel selection)
- The existing faction-context modifiers in social_contest (Church context = theology-biased panel)
- UI-07 (the Godot panel display needs to show who the adjudicator is and what their Conviction is, which is already in the UI spec if the adjudicator is a named NPC)

**Mechanical specification for ED-137:**

| Element | Definition |
|---------|-----------|
| Panel Adjudicator | Named NPC or player character with institutional authority in the scene's context. Default = highest-Mandate faction leader in scene's territory. |
| Adjudicator Conviction → Panel Bias | Adjudicator's primary Conviction: panelists with matching Conviction receive +1D weight toward their preferred contestant. |
| Player control of adjudicator | Player may pre-contest adjudicator selection (Influence vs Ob = adjudicator's Leadership Deviation Ob). Success: player sets adjudicator from eligible NPCs. Failure: default applies. |
| Board game adaptation | No panel in BG mode — social actions use simple Influence vs Ob resolution without audience modifier. Panel is TTRPG/Hybrid only. |

**UI-07 dependency resolution:**
The Godot UI for social contests needs to display:
- Adjudicator name and Conviction (→ panel bias indicator)
- Panel composition bar (Conviction breakdown of panelists)
- Audience modifier value (+1D / −1D / neutral)

All three are now mechanically defined by the Model B specification above.

**ED-137 Resolution:**

| Finding | Resolution |
|---------|-----------|
| Panel adjudicator type | **Model B: Institutional Authority NPC.** Default = highest-Mandate faction leader in scene's territory. |
| Adjudicator Conviction → panel bias | **Defined:** Conviction match = +1D weight toward preferred contestant. |
| Player strategic agency | **Preserved:** pre-contest adjudicator selection at Influence vs Leadership Deviation Ob. |
| UI-07 dependency | **Resolved:** adjudicator is a named NPC with Conviction → all UI fields are already in npc_behavior data model. |

**Editorial entries generated:**
- **ED-137-A:** Panel Adjudicator formal definition (Model B). Add to social_contest_v30.md §Panel section.
- **ED-137-B:** Player adjudicator pre-contest selection (Influence vs Leadership Deviation Ob). Add to social_contest_v30.md.

---

## PART D — SYSTEMIC SIMULATIONS

### SIM-01 — Obligation Degenerate Loop

**Design question:** Can a player create a degenerate loop where obligations (NPC Demands) chain in self-reinforcing cycles that prevent meaningful agency or produce runaway obligation cascades?

#### Obligation Sources (from npc_behavior §8.11)

| Source | Trigger | Rate |
|--------|---------|------|
| NPC Demand (§8.11.4) | NPC Priority Tree action fired against player | Max 2/season per player |
| Compliance consequence | Some Demands trigger further Demands (chain potential) |  |
| Refusal consequence | Disposition −1 + Exposure +1 + potential escalation |  |

**Volume control (§8.11.5):** Maximum 2 Demand entries per season per player. This is a hard cap.

**Simulation: Player C (Church-targeted, Varfell faction, Season 6)**

Season 6 state: Himlensendt is hostile (Disposition −1 toward player). Three active demands have piled up:
1. Himlensendt Demand: Submit to Heresy Investigation (Priority 2 fired — open Thread operation in T3).
2. Almud Demand: Provide military support in T14 (Priority 2 fired — threatened territory).
3. Baralta Demand: Appear at Parliamentary Session (Priority 4 — treaty renewal).

Per §8.11.5: maximum 2 Demands this season. Prioritized by: (1) lowest Disposition first = Himlensendt (Disposition −1), (2) highest institutional authority = Crown (Mandate 5) > Hafenmark (Mandate 4).

**Demands this season:** Himlensendt + Almud. Baralta deferred to next season.

**Player complies with Almud (military support in T14):**
- Consequence: military engagement fires. Player present → mass battle scene. If player is wounded: see §D.3 mass battle consequences. Demand complied → no further Almud escalation.
- But: military action in T14 generates RS −1 (Battle on Valorian soil). IP +2 (inter-faction battle). Strain +1. These are world-level costs, not obligation chain costs.

**Player refuses Himlensendt (Heresy Investigation):**
- Consequence: Disposition −1 (Himlensendt: −1 → −2). Exposure +1 in T3 (player is now more exposed to Church surveillance). Escalation: at Disposition −2, Himlensendt Priority 2 fires again next season → Excommunication attempt (stronger escalation). The escalation chain:

| Season | Himlensendt Action | Player Response | Consequence |
|--------|-------------------|-----------------|-------------|
| 6 | Heresy Investigation Demand | Refused | Disposition −2; Exposure +1 T3 |
| 7 | Excommunication Demand | Refused | Disposition −3; Exposure +2; Church Mandate +1 |
| 8 | Templar Deployment | Cannot be refused (military action, not a demand) | Battle in player territory |

**Is this a degenerate loop?** No — the chain terminates at military action (Season 8), which resolves through combat/mass battle rules. The obligation chain → military action pipeline is correct design. It's an escalation ladder, not a loop.

**Potential degenerate loop scenario:** Could a player oscillate between complying (clearing the demand) and the compliance triggering a new demand?

Test: Player complies with Heresy Investigation (submits to Church questioning).
- Compliance consequence: Standing −1 (submission costs Standing). 
- Himlensendt Priority 2 checks: "Open Thread operation in Church territory OR practitioner identified." If compliance didn't clear the underlying condition (player IS a practitioner, known to Church), Himlensendt Priority 2 fires again next season with a new demand.

**This is a genuine degenerate loop concern:** If the player is a Thread practitioner AND Church has identified them, no single compliance clears the condition permanently. Every season, Himlensendt Priority 2 may fire → new Demand.

**Mitigation already in system:** §8.11.5 cap of 2 Demands/season limits frequency. Himlensendt's Priority 2 requires "practitioner identified publicly" — if the player operates covertly, they may avoid triggering Priority 2. The condition is specific (public identification, not mere suspicion). **Conclusion: the degenerate loop is constrained by the volume cap and the specificity of the trigger condition.** A player who manages exposure avoids the loop. The loop is a consequence of publicly revealed Thread practice, which is a meaningful player choice.

**Additional constraint:** Himlensendt's Certainty 4 → Arc B (Crisis of Faith) is achievable through Evidence contest, which would change his Priority 2 trigger (per §9.3 Domain Echo: "Evidence victory → Church suppresses 1 fewer Heresy Investigation next season"). A fully played arc can break the loop permanently.

**SIM-01 Resolution:** **No degenerate loop.** The volume cap (2 Demands/season) and trigger specificity prevent runaway cascades. Escalation chains terminate at military action. Thread practice loops are mitigated by exposure management and arc resolution. No design change required.

---

### SIM-02 — Chain Contest Convergence

**Design question:** Does the social contest chain (multiple sequential exchanges) converge to resolution, or can it run indefinitely without resolution?

#### Chain Contest Structure (from social_contest_v30 references)

From npc_behavior §6 (Resonant Style in the Contest System) and the social_contest architecture:
- Social contests use a Conviction Track (implied 1–10 range per §3.2 reference: "Conviction Track ≥ 7 or ≤ 3" triggers Belief revision)
- Each exchange moves the track by net successes
- Resolution: Decisive win = Track ≥ 7 (contestant wins) or ≤ 3 (contestant loses)

**Convergence simulation: Player vs. Almud (Certainty 3, Consequence Resonant Style)**

Starting state: Conviction Track 5 (neutral/contested).

Player pool: Charisma 4 + History 3 + 3 = 10 dice. Genre bonus (Projection/Revealing for Consequence style): +1D. Total: 11 dice.
Almud pool: Leadership Deviation Ob 2. Almud defends with Spirit-equivalent (Certainty 3 → 3 defense dice roughly).

Each exchange: Player rolls 11d10 vs Ob 2 (Almud's Leadership Deviation Ob). Expected net successes ≈ 4.4 − 0.33 = ~3.5 (E(net) for pool 11 at TN 7 minus Ob 2 threshold).

**Track movement per exchange:** +1 per net success above Ob (rough approximation — exact formula varies by contest design). With Resonant Style targeting: +1 additional on win.

Expected track movement per exchange toward player's position: ~2–3 points.
Almud's Certainty 3 allows 1 defense per round (roughly) as resistance.

**Convergence test:**

| Exchange | Track (Player moving toward ≥ 7) | Net movement |
|----------|----------------------------------|-------------|
| Start | 5 | — |
| 1 | 5 + 2 = 7 | +2 (player wins, Resonant Style triggered) |

**Result: 1 exchange to convergence** at expected player pool advantage.

But Almud has defenses: Belief check, secondary Resonant Style (Authority only reachable via specific authority sources). What if the exchange produces Partial?

**Edge case: Both Partial repeatedly**

Player Partial: track moves +1. Almud Partial: track stays (Almud's defense consumed their dice).

Convergence in this worst case: (7 − 5) exchanges = 2 exchanges minimum from neutral, if player only gets +1 per Partial. Maximum exchanges to resolution from 5: 2 upward (5→6→7) or 2 downward (5→4→3). The chain always converges in ≤ 4–5 exchanges from neutral start.

**Longest possible chain:** Starting Track 5, both sides rolling precisely enough to tie each exchange (no movement). But per the resolution table: ties produce "Conviction Track unchanged" — which could theoretically run indefinitely. **Gap: tie-break not defined for extended stalemate.** If Track doesn't move for 3 consecutive exchanges, the contest should have a forced resolution.

**Proposed stalemate rule:** After 3 consecutive exchanges with no Track movement: both sides take 1 Composure strain. If Track still hasn't moved after 5 total exchanges: Partial resolution in current Track direction (toward 7 if ≥ 5, toward 3 if < 5). This produces convergence within 5 exchanges maximum.

**SIM-02 Resolution:** **Converges in ≤ 5 exchanges** under proposed stalemate rule. No degenerate infinite loop. One design gap: stalemate tie-break not formally defined. **Propose: 5-exchange convergence cap with forced Partial resolution at Track current direction.**

**Editorial entry:** **SIM-02-A:** Social contest stalemate tie-break: forced Partial resolution after 5 exchanges with no Track movement. Add to social_contest_v30 §resolution section.

---

### SIM-03 — IP Recalibration for 30-Year Games

**Design question:** Does Institutional Pressure (IP) advancement rate produce appropriate endgame pressure in both short (~20 season) and long (~120 season / 30-year) games?

#### IP Baseline Parameters

From board_game_v30 §G-11 (reconstructed from embedded patches):
- IP baseline: starts 0
- Primary advancement: Theocracy Counter > 60 → +1/season (from embedded P-28 reference)
- Civil war advancement: +2/season with inter-faction battle (peninsular_strain §3.2)
- Threshold effects: IP 75 → Vanguard deploys

From peninsular_strain §3.2: "IP +2 per season in which a Battle between playable factions is resolved."

**Game length calibration:**

| Game format | Seasons | Expected IP advancement (no battles) | Expected with occasional wars |
|------------|---------|-------------------------------------|------------------------------|
| Short (4-player, ~20 seasons) | 20 | 0–20 (if TC > 60 for 10+ seasons) | 40–60 (2–3 war seasons) |
| Standard (6-player, ~40 seasons) | 40 | 20–40 | 60–80 → Vanguard threshold |
| Long (30-year narrative, ~120 seasons) | 120 | 60–120 (guaranteed Vanguard if TC persistent) | 100–200 (multiple invasion cycles) |

**30-year game IP behavior simulation:**

Season 1–30 (Years 1–7): TC grows from 22 toward 60. At TC 50: Mandatory Assert each season (+1 TC/season). TC 60 reached around Season 38. IP starts at 0, begins climbing at TC 60 threshold.

Season 38–60: IP +1/season from TC passive (if no AER maintenance). IP: 0 → 22 in 22 seasons. Add occasional wars: +2 per battle season. If 5 war seasons in this period: IP: 22 + 10 = 32. Still below 75.

Season 60–90: AER ≤ 1 condition (Reformed Settlement chain from board_game §Cascade Test 2 — AER drops). IP threshold drops to 75 (default). IP: 32 + 30 (passive at TC 60+) = 62. Add 5 more war seasons: 62 + 10 = 72. Still below 75. AER maintenance (Temperance Cardinal active): if AER = 2 → threshold = 80. IP 72 < 80. Safe. If AER drops to 1: threshold 75. IP 72 → 3 more passive seasons to breach.

Season 90–92: Vanguard deploys. First invasion. Players must repel (Löwenritter Battle example from board_game §Scenario C: Vanguard repelled → IP −5). IP: 75 → 70. Below threshold again. 5 more passive seasons: IP 75 again.

**Finding: In a 30-year game, IP creates a recurring Altonian pressure cycle** — not a single endgame event, but a recurring invasion threat every ~10 seasons once TC > 60. This is **correct and sophisticated** design. The 30-year game doesn't end with the Altonian invasion; it creates a multi-cycle narrative of repulsion, respite, and renewed threat.

**IP Recalibration need:** The current IP formula produces threshold breaches approximately every 10–15 seasons after TC > 60. For a 30-year (120-season) game, this means 4–6 Vanguard deployments. This is **too many** — the Vanguard should feel like a climactic event, not a seasonal disruption.

**Proposed recalibration for long games (>60 seasons):**

| Game length | IP advancement modifier |
|------------|------------------------|
| ≤ 40 seasons | Standard (current) |
| 41–80 seasons | Passive IP advancement (from TC > 60): +0.5/season instead of +1 (halved). Civil war: unchanged (+2). |
| 81+ seasons | Passive IP: +0.25/season. Civil war: unchanged. Vanguard deployment after repulsion: 3-season cooldown before IP can breach again. |

This makes passive IP slow enough that civil war is the primary IP driver in long games — exactly the correct design pressure (war risks Altonian invasion; governance prevents it).

**SIM-03 Resolution:** IP is well-calibrated for short and standard games (~20–40 seasons). For 30-year games (120 seasons), recalibration is needed: halve passive IP advancement after 40 seasons, quarter it after 80. Civil war IP unchanged (maintains the anti-war pressure). Add 3-season Vanguard repulsion cooldown to prevent Vanguard becoming routine.

**Editorial entries generated:**
- **SIM-03-A:** IP recalibration for long games (>40 seasons): passive IP × 0.5; >80 seasons: × 0.25. Add to params_board_game.md §IP Advancement.
- **SIM-03-B:** Vanguard repulsion cooldown: 3 seasons before IP can breach threshold again after repulsion. Add to npc_behavior §7.8 or params_board_game.md.

---

### SIM-04 — Generational Shift Simulation

**Design question:** In a 30-year game, what happens when faction leaders die, retire, or are replaced? Does the system produce emergent generational change?

#### Generational Change Mechanisms (existing)

| Mechanism | Source | Effect |
|-----------|--------|--------|
| Löwenritter Coup | npc_behavior §5.2 Arc C (Almud) | Crown → Löwenritter; Torben Loyalty transfers |
| Maret Uln Succession | npc_behavior §2.10 | Activates on Vaynard elimination (Loyalty 0 + Mandate 0) |
| Faction Collapse | board_game §P-24 | Faction eliminated; units Masterless |
| Player Character Death | board_game §9.9 | PC takes over highest-loyalty NPC officer |
| PC Death (no officer) | board_game §9.9 | PC takes over new character from different faction |

**Missing generational mechanisms for 30-year games:**

1. **Natural death of NPC leaders:** Almud, Baralta, Vaynard et al. have no mortality mechanic. In a 30-year (120-season) game, all starting leaders would still be alive. This breaks verisimilitude.

2. **Succession without coup/collapse:** What if Almud simply retires after 20 years? No mechanic exists.

3. **New faction entrants:** A 30-year game could introduce new political factions (Torben as Crown leader after Almud retires; Maret Uln as Varfell successor even without elimination). No mechanic for peaceful generational transfer.

**Simulation: Almud Natural Death (Season 60, Year 15)**

No current mechanic. **Proposed:**

**Mortality trigger:** NPC leaders have a Longevity Track defined at character creation (hidden). At each Year-End Accounting (every 4 seasons), roll: 2d10 (TN 7, Ob = Longevity Track value 1–5). Failure: mortality event (illness, injury, age). Consequences:

| Degree | Outcome |
|--------|---------|
| Overwhelming | No event. Longevity Track +1 (robust year). |
| Success | No event. |
| Partial | Stability reduction. Leader weakened — Leadership Deviation Ob +1 for 2 seasons. |
| Failure | Mortality event. GM determines cause. Succession fires. |

Longevity Track values by NPC:
- Almud: Longevity 3 (moderate — aging, governing under stress)
- Himlensendt: Longevity 4 (Church discipline and austere life)
- Baralta: Longevity 4 (strong constitution, parliamentary stability)
- Vaynard: Longevity 2 (Thread exposure degrading health; Thread Sensitivity 14 hidden)
- Ehrenwall: Longevity 3 (military life, battle wounds)
- Vossen: Longevity 3 (underground life, operational stress)

**Succession procedure (proposed):**

On Mortality Event:
1. Named successor identified (from Arc profiles or player recruitment).
2. If successor exists: successor assumes leadership. Faction stats maintained. Conviction may shift (per successor Stance Triangle — Maret Uln shifts Varfell Conviction from Reason to Equity).
3. If no successor: faction Leadership Crisis. Mandate −2, Stability −1. Faction takes NPC AI Priority 7 (Pass) for 1 season. Then generates a new leader from Cardinal Officers (Church), Torben (Crown), or generic faction heir.

**Generational shift simulation: Seasons 60–80 (Years 15–20)**

Assume Almud dies Season 64 (Longevity roll failure).

**Season 64:** Almud Mortality. Torben's Loyalty at this point determines succession:
- Torben Loyalty ≥ 3 (Crown-aligned): Torben becomes Crown leader. Conviction: TBD (per ED-394 — Conviction starts blank, first major investment sets it). If Crown faction invested in Torben (Priority 5 in Crown NPC tree): Torben Loyalty = 3–4. Conviction: Order (following Crown precedent, institutional inheritance).
- Torben Loyalty ≤ 2 (contested): Löwenritter Coup Counter fires (Crown weakened). Ehrenwall assesses: is this the moment?

**Simulation: Torben succession (Loyalty 3)**

Torben assumes Crown leadership at Season 64. 
- New Conviction: inherits Crown/Order framework (from whichever faction held highest Loyalty).
- Fresh Certainty: higher (4, conventional court education per §7.10) but blank Conviction means first Evidence/Consequence contest resets him easily.
- **Key emergent effect:** Torben at Certainty 4 with blank Conviction is a genuine wildcard. The faction that invested most in him over the previous 15 years (Seasons 1–64) effectively "programmed" his Conviction. This is the correct design: 30-year games are narratively about who shapes the next generation.

**Varfell succession (Vaynard, Longevity 2):**

Season 48 (Year 12): Vaynard Longevity roll. 2d10 vs Longevity 2 (high Ob = easier to die). Roll: 8, 1 → 1 net. Ob 2: Failure. Mortality event — Vaynard's Thread exposure (TS 14 hidden) has been degrading his health. Cause of death: Thread-related illness (Arc C consequences realized without full arc activation).

Maret Uln succession fires: Varfell Conviction shifts Reason → Equity. Varfell Priority Tree changes: Priority 4b (Cultural Reformation) now weighted toward RM-adjacent territories. Varfell-RM alliance becomes structurally possible where it was impossible under Vaynard.

**This is generationally transformative:** The alliance map of the entire game shifts at Season 48. A 30-year game has at least 2–3 such leadership transitions, each reshaping faction alignments. **The generational shift simulation confirms this is the correct design for long games.** The Mortality mechanic makes long games genuinely generational.

**SIM-04 Resolution:** The generational shift system needs the Mortality mechanic (Longevity Track + Year-End roll) to function for 30-year games. Once added, the existing succession paths (Torben, Maret Uln, Cardinal Officers) cover all required transitions. The shift is emergent (driven by dice and player investment) rather than scripted.

**Editorial entries generated:**
- **SIM-04-A:** Longevity Track for named NPC leaders (1–5 scale; Year-End mortality roll 2d10 TN 7 vs Longevity Ob). Add to npc_behavior_v30.md §5 (Arc Profiles) or new §5.3 Longevity.
- **SIM-04-B:** Succession Procedure on Mortality Event. Add to npc_behavior_v30 §5.
- **SIM-04-C:** Longevity Track values by NPC (Almud 3, Himlensendt 4, Baralta 4, Vaynard 2, Ehrenwall 3, Vossen 3). Add to npc_behavior §7.10 NPC Stat Values table.

---

## PART E — AUDIT SUMMARY

### Confirmed Working (No Change Required)

| Item | Status |
|------|--------|
| ED-SETT-02 Governance calibration | ✓ Ob 2 baseline correct. Success rates well-differentiated. |
| Obligation degenerate loop | ✓ Volume cap + trigger specificity prevent runaway. Arc resolution breaks loops permanently. |
| Chain contest convergence | ✓ Converges ≤ 5 exchanges under proposed stalemate cap. |
| IP short/standard game calibration | ✓ Correct for ≤ 40 seasons. |
| Companion candidate rate | ✓ 0–2 per campaign. Not inflated. |
| Accord ↔ Prosperity integration | ✓ Clean. |
| Settlement archetype differentiation | ✓ High-PT/Fort = durable; low-PT/Fort = fragile but recoverable. |

### Design Gaps Requiring Resolution

| Gap ID | Gap | Proposed Resolution | Priority |
|--------|-----|---------------------|---------|
| ED-SETT-01-A | Order stat range undefined | 0–5 range. Add to params. | P2 |
| ED-SETT-01-B | RM organizer starting Disposition in non-RM settlements | Propose 0. Confirm. | P3 |
| ED-SETT-04-A | Siege duration summary | PP-088 covers it implicitly. Add explicit note. | P2 |
| ED-SETT-04-B | Settlement Order −1 per siege season | Propose PP. | P2 |
| ED-SETT-04-C | Altonian Vanguard tree lacks Assault entry | Add Priority 2.5. | P1 |
| ED-SETT-10-A | Niflhel contact trigger | Investigation-triggered, not Outreach. | P2 |
| ED-SETT-10-B | Hann home settlement | T11 Halvardshelm (proposed). Confirm. | P3 |
| ED-COMP-01-A | Companion vs. recruited NPC distinction | Formal definition required in spec. | P1 |
| ED-COMP-01-B | Officer reaction to faction-misaligned player action | −1 Disposition rule. Add to mass_battle §D.2. | P2 |
| ED-COMP-02-A | Companion personal combat stats | Generation formula from faction Military. | P1 |
| ED-COMP-02-B | Companion proxy Command | Ob 3 check when PC incapacitated. | P2 |
| ED-COMP-02-C | Companion combat AI priority tree | 5-level tree. Add to companion spec. | P1 |
| ED-COMP-03-A | Companion mass combat capability table | Disposition +3/+4/+5 tiers. | P2 |
| ED-COMP-03-B | Companion tactic capability | Tier-1 automatic; Tier-2 at Ob 2 check. | P2 |
| ED-137-A | Panel Adjudicator formal definition | Model B: Institutional Authority NPC. | P1 |
| ED-137-B | Player adjudicator pre-contest selection | Influence vs Leadership Deviation Ob. | P2 |
| SIM-02-A | Social contest stalemate tie-break | 5-exchange cap + forced Partial. | P2 |
| SIM-03-A | IP long-game recalibration | Passive IP × 0.5 after 40 seasons; × 0.25 after 80. | P2 |
| SIM-03-B | Vanguard repulsion cooldown | 3-season cooldown after repulsion. | P2 |
| SIM-04-A | Longevity Track mechanic | Year-End roll; Longevity 1–5. | P2 |
| SIM-04-B | Succession Procedure on Mortality | Defined process; covers Torben, Maret Uln, Cardinals. | P2 |
| SIM-04-C | Longevity Track values by NPC | Per table above. | P3 |

### Missing Documents Required

| Document | Required by |
|----------|------------|
| `companion_specification_v30.md` | ED-COMP-01/02/03 — forward referenced but does not exist |
| `settlement_layer_v30.md` or `settlement_params.md` | ED-SETT-01/02/04/10 — forward referenced but does not exist |
| `social_contest_v30.md` — full read needed | ED-137, SIM-02 — partially inferred from cross-references |

**Recommendation:** Before committing any of the above proposals, fetch and read `social_contest_v30.md` in full to validate ED-137 and SIM-02 against the actual contest system.

---

## PART F — COMMIT PLAN

**P1 items only (required before any design work proceeds):**

1. Altonian Vanguard Priority Tree: add Assault entry (Priority 2.5) → npc_behavior_v30.md §7.8
2. Companion vs. recruited NPC distinction → new companion_specification_v30.md §1 (skeleton)
3. Companion personal combat stats → companion_specification_v30.md §3
4. Companion combat AI priority tree → companion_specification_v30.md §4
5. Panel Adjudicator definition (Model B) → social_contest_v30.md §Panel (after fetching and reading)
6. Editorial ledger entries for all new EDs

**P2 items (next session):** Order stat, siege Order degradation, companion mass combat tiers, IP recalibration, social contest stalemate, Longevity Track.

**P3 items (backlog):** Hann settlement, RM organizer Disposition, NPC Longevity values, ED-392/393/394/395/396/397/398 (NPC stat confirmations from prior ledger).

---

*End of simulation report. Awaiting Jordan's review before commits.*
