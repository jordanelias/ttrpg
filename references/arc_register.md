# Arc Register

> **Version:** 2 (audit-corrected)
> **Status:** WORKING DRAFT
> **[EDITORIAL: ED-NEW — Tier assignments are provisional pending user review]**
> **Sources fetched this session:** `designs/gm_ref_cp14/arcs/*` (11 files), `gm_ref/arcs_*` (3 files), `designs/npcs/npc_roster.md`, `references/params_factions.md`, `references/params_threadwork.md`, `references/params_board_game.md`, `designs/board_game/victory_architecture_v1.md`, `designs/board_game/valoria_bg_v05_simulation_and_patches.md`, `designs/ttrpg/valoria_narrative_scenario_chains.md`, `compilation/v0.14/stage6_factions.md`, `canon/02_canon_constraints.md`

---

## Classification Criteria

| Tier | Definition |
|------|-----------|
| Principal | Near-inevitable from running mechanical engines (clocks, seasonal accounting, Non-Player Character faction tendency). Emerges unless players actively prevent it. Campaign-defining. |
| Secondary | Emerges from specific Non-Player Character tracks, subsystem engagement, or player interaction with particular world elements. High probability given typical play patterns but not automatic. |
| Tertiary | Narrow prerequisites, single-roll pivots, or specific player choices. Possible but not guaranteed in any given campaign. |

---

## Named Non-Player Character Index

### Legacy Non-Player Characters (pre-roster, referenced across arc files and design docs)

| Non-Player Character | Faction | Key Tracks | Source |
|------|---------|------------|--------|
| King Almud | Crown | Beliefs (3: Altonian trade, the path dilemma, RM sympathy), TS potential (28→30 via Discovery Event), Resonant Style: Consequence | `stage6_factions`, `narrative_scenario_chains` ARC 2 |
| Duchess Inge Baralta | Hafenmark | Mandate (personal: 7 per cp14 arcs; faction: 4 per starting stats), Reach (5 per cp14 arcs), TC suppression (−1/season while her Mandate ≥ 4), Sovereign Authority Doctrine (once per campaign arc), Solmund claim [EDITORIAL] | `params_factions`, `stage6_factions`, `narrative_scenario_chains` ARC 3 |
| Grandmaster Sigrid Ehrenwall | Löwenritter | Coup Counter (0–3, fires at 3; never decrements), Health/Wound track (incapacitation at ceiling(Health ÷ 2)), Lions' Table | `params_factions`, `arcs_20_23` |
| Cardinal Arnlod Olafsson | Church (Justice) | Niflhel connection (hidden — used Niflhel to suppress texts/individuals), Church Intel operations, Heresy Investigation authority | `narrative_scenario_chains` ARC 4, `arcs_09_11` |
| Duke Magnus Vaynard | Varfell | Thread Investigation Track (TK 0–5; TC effects: TK 3 = +1, TK 4 = +2, TK 5 = +3), Thread Sensitivity (TS starts 14 Dormant), Private Collection (Intel vs Ob 2, each use: hidden TS +1; at TS 14+ triggers Spirit TN 7 Ob 1 Discovery Event), Belief 3 (succession leverage) | `params_factions`, `narrative_scenario_chains` ARC 9 |
| Confessor Arne Himlensendt | Church (head) | Resonant Style: Evidence, Stability checks under institutional crisis, doctrinal authority over TC/Heresy policy | `arcs_09_11`, `narrative_scenario_chains` |
| Cardinal Magnus Klapp | Church (Education) | Combat Endurance (CE) 4, TS 31, archive access to originary Locks, essentialist formation (TS growth check Ob raised from 1 to 2) | `arcs_09_11`, `arcs_31_35` |
| Cardinal Osten Jarnstal | Church | [GAP: minimal mechanical data — no tracks, no AI flaw defined] | `arcs_09_11` |
| Princess Elske Almqvist | Crown/Altonia | Conviction: Family vs Self-Determination, Resonant Style: Evidence, Loyalty (to Valoria — distinct from Torben's Loyalty), independence arc preconditions | `narrative_scenario_chains` ARC 6, `arcs_09_11` |
| Prince Torben Almqvist | Crown/Altonia | Loyalty track (starts high; −1/season under Altonian influence if Covert Contact fails; floor at 6 if Contact maintained 3 consecutive seasons), Tutoring Demand trigger at Institutional Pressure (IP) 30 | `narrative_scenario_chains` ARC 5, `arcs_09_11` |
| Lenneth Almqvist | Crown | CE accumulation, TS growth (self-directed), sea-republic archive (pre-Altonian coastal survey, first-person Thread-perception accounts ~180 AG), concealment | `arcs_28_30`, `narrative_scenario_chains` |
| Solvind Brak | Niflhel (operative) | Testimony value for Olafsson-Niflhel exposure (Intelligence Domain Action vs Ob 3 to find and extract; Social scene to break Niflhel loyalty) | `narrative_scenario_chains` ARC 4, `arcs_09_11` |
| Revolution elder | Restoration Movement (RM) | Fragmentary inner-tradition knowledge, TS uncertain, Forgetting-impaired. Testimony for Collision E (Grand Debate on Solmund's nature). | `narrative_scenario_chains` **[EDITORIAL — not canonised as named character]** |

### Roster Non-Player Characters (designs/npcs/npc_roster.md — ED-358)

| # | Non-Player Character | Faction | Compromise | Behavioral Artificial Intelligence Flaw | Key Tracks |
|---|------|---------|------------|------|------------|
| 1 | Edeyja | Wardens | None | None | TS 75–80, Coherence 9, moral anchor |
| 2 | Maret Uln | Varfell | Dual loyalty (RM sympathy) | CONFLICTED (hesitates vs RM — delays 1 season) | TS ~50, Belief checks (Spirit TN 7 Ob 1 per Tribune Inward in RM-presence territory) |
| 3 | Maret Vossen | RM | Visibility = Church target (AP +1/season when operating publicly) | IDEALIST (spreads Presence thin — 5 territories at 1 each rather than 3 at 2) | TS 25 (below Forgetting resistance gate of 29), Popular Will |
| 4 | Sæmund Haelgrund | Church (Inquisitor) | Evidence contradicts doctrine (TS 12 hidden) | PROCEDURALIST (+1 season investigations but Overwhelming if they resolve) | TS 12 (hidden — does not know he is Thread Sensitive), Heresy Investigation |
| 5 | Sigrid Torsvald | Löwenritter (Riskbreaker) | TS 35 in anti-Thread institution | RISK-AVERSE on Thread collateral (~30% abort rate in Thread zones) | TS 35, Deniability Debt (+1 per aborted op), Lenneth archive connection (3 seasons securing it) |
| 6 | Halvar Brandt | Löwenritter | Border war trauma (Lowenskyst pass, 12 years ago) | EXTERNAL THREAT FIXATED (evaluates all actions against Altonian threat metric) | Ehrenwall succession candidate, Coup Counter threshold 2 (not 3), military redirect to T3/T10 |
| 7 | Annika Feldhaus | Guilds | Thread-touched supply chain (~15% luxury revenue via Niflhel/Virke) | PROFIT-MAXIMISING (Wealth over Mandate — Mandate trends toward 2) | Guilds Wealth recovery +1/season, Virke connection |
| 8 | Peder Almstedt | Ministry | Preserves system over justice | CONSERVATIVE (blocks reform — +1 Ob to Parliamentary reform actions) | PI recovery +1/season, AP-token placement, Parliamentary Manoeuvre facilitation |
| 9 | Gerik Strand | Crown (Lord Steward) | Conditional position in unconditional world | OVERPERFORMER (cannot delegate — Crown admin brittle) | Treasury +1D, flattery vulnerability (−1 Ob to social actions acknowledging competence), +1 Ob for 2 seasons if removed |
| 10 | Dalla Virke | Niflhel (Virke syndicate) | Thread-touched supply chain (personally built, Thread-woven antiquities from Einhir ruins) | NETWORK PROTECTOR (shields partners; withholds intel from own family) | Trust network (factions inside: trade Ob −1; outside: no modifier), family recall risk (3 protection incidents → recall) |
| 11 | Doux Alexios Laskaris | Altonia | Genuine attachment to Elske (assigned asset) | PROTECTIVE (IP −1/season while active; flips if Elske Loyalty ≤ 2) | IP modifier, flip trigger (Elske Loyalty ≤ 2 → IP +3 immediately + replaced by imperial-loyal governor) |
| 12 | Rikard Solberg | Schoenland | Wants to go home (7 years on posting) | STABILITY-SEEKING (unconsciously steers toward stabilisation) | Arms supply −1 unit/season vs optimal, intelligence downplayed (Schoenland response 1 season delayed) |
| 13 | [Name Pending] | Church (Prudence) | Tithe maximiser (alienates parishes while funding charities) | OPTIMISER (Church Wealth throughput over grassroots loyalty) | Church Wealth +1/season, Church Mandate −0.5 per over-tithed territory (fractional, at Year-End), CV erosion +1 in over-tithed territories at Year-End |

---

## Clock Starting Values and Key Thresholds

| Clock | TTRPG Start | Board Game Start | Key Thresholds |
|-------|-------------|-----------------|----------------|
| Theocracy Counter (TC) | 0 | 28 | 40 = Coup Counter increment if Crown inactive; 50–69 = mandatory Assert/Suppress; 60 = Territorial Seizure; 75+ = TC frozen, seizure mode |
| Rendering Stability (RS) | 60 | 72 | 59–40 = Fragile (Shifting Objects, +1 Ob in affected territories); 39–20 = Fractured (Gaps, Incursion risk); 19–1 = Critical (+1 Ob worldwide, Stability Ob 1 all factions); 0 = Rupture (all lose) |
| Institutional Pressure (IP) | 20 | 20 | 30 = Tutoring Demand fires, Schoenland trade +1 Ob; 60–74 = trade +2 Ob, proxy; 75+ = Vanguard; 100 + Altonian External Relationship (AER) ≤ 1 = Altonian Conquest (all lose) |
| Public Instability (PI) | — | 5 | PI ≥ 6 = Baralta BG Conviction fires (if also TCV ≥ 12); PI < 4 = Baralta succession → fracture |
| Coup Counter | 0 (hidden) | 0 (hidden) | Increments (+1 each): TC ≥ 40 + Crown inaction, Torben loyalty ≤ 3, Crown loses 2+ territories without military response. Never decrements. 3 = fires. |

**TC Generation (PP-402, victory_architecture §7):**
1. Institutional Momentum: TC +1/season (passive, always)
2. Conviction Yield: per Church-Prominent territory, add by CV (CV 5 = +1, CV 4 = +0.5, others = 0; total = floor(sum))
3. Assert (optional Church action): Influence vs Ob 2. Success: TC +1. Failure: Stability −1.
4. Suppress (optional opponent action): Mandate vs Ob = Church Mandate. Success: negates Step 1 passive for that season only. TC does not decrease. Failure: Stability −1.
5. Hafenmark Structural Suppression: while Baralta Mandate ≥ 4, TC −1/season.

**Baralta excommunication:** if excommunicated, TC +4 immediately and suppression ends permanently.

**RS threshold effects:** geographically graduated by Proximity Rating (node distance from Askeheim T15), not applied globally. No cross-clock coupling to TC or IP. See params_board_game §RS Effects for full proximity table.

**IP generation:** [GAP: no canonical base IP advancement rate stated. bg_v05 notes this gap. narrative_scenario_chains uses +2/season as working assumption but this is not in params.]

---

## Principal Arcs

### ARC-P01: TC Accumulation → Dominance Event
**Engine:** TC clock — +1/season passive (institutional momentum) + Conviction Yield
**Emergence:** TC accumulates passively. Baralta Mandate ≥ 4 is the only passive brake (−1/season). If Baralta's Mandate drops below 4 (via failed actions, excommunication, or elimination), net TC ≥ +1/season. TC 40 → Coup Counter increment if Crown inactive. TC 60 → Church Territorial Seizure protocol. TC 75+ → TC frozen, seizure mode.
**Non-Player Characters:** Baralta (suppression — Hafenmark), Himlensendt (Church head — TC policy), Olafsson (covert TC acceleration via Niflhel channels), Klapp (TC generation pauses if he converts — Church Stability ≤ 4, Cardinals competing), Prudence Cardinal (tithe friction → CV erosion in over-tithed territories → reduces Conviction Yield), Almstedt (PI recovery — interacts via Parliamentary procedures)
**Key values:** TC suppression threshold = Baralta Mandate ≥ 4. Excommunication = TC +4 immediately. TC 60 = Territorial Seizure (Church Mandate ≥ 4 required; pool = Influence + floor(TC/15), Ob = 7 − CV). TC 75+ = frozen.

### ARC-P02: RS Decay → Substrate Collapse
**Engine:** RS clock — seasonal decay from Lock drift (−1 to −2/season), Gap persistence (−4/season per Gap), Winter annual drift (−1), siege (−1/season), failed Thread operations
**Emergence:** RS degrades constantly from multiple sources. No player action required for decline — only inaction. RS threshold effects activate at Accounting by proximity rating (geographic graduation, not global). Seasonal cap: ±10 net RS change per season.
**Non-Player Characters:** Edeyja (TS 75–80 — the only person who fully understands the problem; WC track is her engagement threshold), Maret Uln (Thread operations contribute to decay), any practitioner Player Character
**Key values:** RS starts 60 (TTRPG) / 72 (BG). 59–40 = Fragile. 39–20 = Fractured (Gaps, Incursion). 19–1 = Critical (+1 Ob worldwide; all factions Stability check Ob 1; Mandate 0 → Faction Fracture). 0 = Rupture (campaign ends, all lose). No cross-clock coupling to TC or IP from RS thresholds.
**[CORRECTION: v1 register stated "RS ≤ 55 → cross-clock fires: TC +1/season, IP +1/season." This is NOT a canonical mechanic. Source was narrative_scenario_chains (scenario document, not mechanical specification). Actual RS effects are proximity-graduated. See params_board_game §RS Effects.]**

### ARC-P03: The Coup That Wasn't Supposed to Happen
**Engine:** Coup Counter (0–3, hidden, never decrements)
**Emergence:** Counter increments from three specific triggers: (a) TC reaches 40 while Crown took no action to reduce it that season, (b) Torben Loyalty reaches 3 or lower, (c) Crown loses 2+ territories in one season without a military response Domain Action. Counter = 3 → Ehrenwall issues formal demand at next Accounting. RS ≤ 10 adds +1 to coup/succession trigger check pools.
**Non-Player Characters:** Ehrenwall (trigger — Coup Counter threshold 3), Almud (target — must yield command or face coup), Brandt (succession candidate — threshold 2 not 3; redirects to borders), Torsvald (Riskbreaker exposure risk during Martial Law), Strand (administrative collapse if coup succeeds — Crown admin +1 Ob for 2 seasons), Almstedt (Ministry disruption — PI recovery mechanics change)
**[CORRECTION: v1 register conflated IP 30 with direct Coup Counter increment. IP drives Tutoring Demand → Torben Loyalty degradation → possible Counter increment. This is a chain, not a direct link.]**

### ARC-P04: The Axis 9 Resolution
**Engine:** Axis 9 (Thread ontology: suppress vs accept) — forced by practitioner visibility, Vaynard TK advancement, RM cultural pressure
**Emergence:** Practitioners operate visibly. Vaynard TK climbing (TC effects at each level: TK 3 = +1, TK 4 = +2, TK 5 = +3). Revolution sheltering sensitives. The question of whether Thread reality is acknowledged publicly becomes unavoidable. Multiple resolution paths exist (see Collisions B and E).
**Non-Player Characters:** Vaynard (TK track — most informed secular actor at TK 5), Almud (potential Discovery Event → practitioner king; if TS 30+ and public → TC +3 but RS improves), Himlensendt (doctrinal authority — Resonant Style: Evidence makes him vulnerable to proof), Klapp (hidden TS 31 — Church education head perceives what Church suppresses), Haelgrund (hidden TS 12 — Church investigator), Vossen (RM public face — TS 25), Edeyja (substrate authority — TS 75–80)

### ARC-P05: The World Without Direction
**Engine:** Non-Player Character faction tendency (artificial intelligence) — runs automatically at seasonal Accounting when players focus elsewhere ≥ 2 seasons
**Emergence:** Game Master runs Non-Player Character faction rolls (faction stat as d10s, TN 7, Ob = opposing stat ÷ 2 round up). Each faction drifts toward institutional tendencies: Church expands Piety and accumulates civil authority; Varfell maximises information advantage and deploys Private Collection (hidden TS +1 per use); Crown consolidates.
**Non-Player Characters:** All Non-Player Character faction heads via tendency. Laskaris (IP −1/season sandbagging), Solberg (arms supply conservative), Almstedt (PI recovery +1/season), Prudence Cardinal (Church Wealth +1/season but Mandate erosion), Feldhaus (Guilds Wealth over Mandate)

### ARC-P06: The Accounting Sequence
**Engine:** Seasonal accounting strict order — Domain Echo outcomes → Stability checks → clock drift → floors/ceilings → Character Point (CP) award
**Emergence:** Two+ factions under Stability pressure in the same season. Order-of-operations effects create interaction patterns. Anti-death-spiral floor at Stability 2 (Ob 4 regardless of actual pressure). State-based RS/TC/IP/PI environmental effects do not count against seasonal caps.
**Non-Player Characters:** All faction Non-Player Characters. Almstedt (PI recovery +1), Strand (Crown admin +1D), Prudence Cardinal (Church Wealth +1 but Mandate fractional loss)

### ARC-P07: The Faction That Breaks
**Engine:** Stability checks — any faction under sustained multi-season pressure
**Emergence:** Multiple concurrent threats across 2–3 seasons. Stability checks escalating: Ob 3 → 4 → 5. Any faction reaching Stability 0 collapses. Anti-spiral floor at Stability 2 gives 1–2 season window. At RS Critical (19–1): all factions face Stability check Ob 1 each season; Mandate 0 → Faction Fracture.
**Non-Player Characters:** The leader of whichever faction breaks. High-risk candidates: Church (Klapp conversion + Olafsson exposure → Stability −3 per Collision A), Crown (IP + TC + Coup Counter cascade), Revolution (Rawlsian framework contradictions), Varfell (Vaynard eliminated → Maret Uln succession, Varfell Thread Mastery (VTM) reset)

### ARC-P08: The 218 AG Investigation
**Engine:** Evidence trail access across 4 sources (Crown archives, Niflhel records, Varfell documents, Lenneth archive)
**Emergence:** Players investigate the 218 AG death. Each single trail points to a different faction (each faction built a theory implicating rivals). Only cross-referencing ≥ 3 of 4 trails reveals the truth: the death was accidental. Partial investigation produces confident wrong answers. False accusation produces real political consequences even against innocent factions.
**Non-Player Characters:** Almud (Belief crisis — 27 years of constraint in response to nothing; 1-season self-examination; Crown Non-Player Character AI suspends offensive Domain Actions), Ehrenwall (threat model reassessment — Löwenritter readiness partly based on assassination assumption), Vaynard (intelligence apparatus exposed as pretext for Thread research; Varfell Mandate −1 if publicised), Lenneth (sea-republic archive provides independent physical evidence), Solvind Brak (Niflhel evidence trail), Olafsson (Church defensive posture recalculation)
**Key mechanic:** If publicised: PI −2. If suppressed: PI +0. If selectively revealed: leverage — "Accidental Truth" condition (each faction told knows the secret and owes a debt of silence). This is described as the most valuable political currency in the game.
**[Note: narrative_scenario_chains presents the accidental death as the canonical resolution. E-01 (assassination perpetrator) flagged as unresolved elsewhere — these two positions may need reconciliation.]**

---

## Secondary Arcs

### ARC-S01: The Vaynard Revelation Cascade
**Engine:** Vaynard TK track (0–5) + Discovery Event (Spirit TN 7 Ob 1 at TS 14+)
**Emergence:** Practitioner Player Character forms sustained relationship with Vaynard. Private Collection deployed (Intel vs Ob 2, each use: hidden TS +1). TK advances through relationship, Lenneth archive access, or Church archives via Niflhel.
**Non-Player Characters:** Vaynard (TK — TC effects: TK 3 = +1, TK 4 = +2, TK 5 = +3; at TK 4 offers entire Private Collection including originary Locks for Thread education + Southernmost partnership; at TK 5 shifts from knowledge to capability — "controls" not "understands"), Maret Uln (intelligence operative; dual loyalty delays anti-RM actions 1 season), Olafsson (if Vaynard exposed → Church investigation), Lenneth (archive channel if players broker access)
**Thresholds:** TK 3 = TC +1 + succession leverage formalised. TK 4 = TC +2 + Collection offered → potential multi-character Discovery Events from originary Locks. TK 5 = TC +3 + Vaynard is most dangerous secular actor. Discovery Event at any TK: TS jumps to 30 (Stirring), Certainty −1 permanent, TK +2 immediately.

### ARC-S02: The Brittle Peace
**Engine:** Threadweaving over-actualisation brittleness (threadwork v2.5 §2.3, §9.8)
**Emergence:** Practitioner Weaves a diplomatic agreement at Relational scale. Over-actualisation makes the agreement mechanically fragile. Consequence genre fires on fracture.
**Non-Player Characters:** Any practitioner Player Character, affected faction leaders, Edeyja (if consulted on Relational work)

### ARC-S03: The Tribunal and the Temporal Shimmer
**Engine:** Church Inquisitorial proceedings + Debate redesign v1
**Emergence:** Church opens proceeding against practitioner Player Character or Varfell for Thread-related heresy. Evidence genre produces temporal co-movement or Pulling as courtroom consequence.
**Non-Player Characters:** Haelgrund (PROCEDURALIST — investigation +1 season but Overwhelming), Himlensendt (presides), Olafsson (Justice portfolio), Klapp (if his TS exposed during proceedings → internal crisis)

### ARC-S04: The Rendering Debt
**Engine:** Mass Battle per-turn Threadweaving + Coherence drain (×3 multiplier per PP-192)
**Emergence:** War begins. Practitioner Player Character operates as faction battlefield Thread asset every turn. Coherence drain accelerates. All RS costs from Thread operations in Mass Battle ×3 (PP-192). Rendering Crisis at Coherence 0.
**Non-Player Characters:** Ehrenwall (if war involves Löwenritter), Brandt (if Ehrenwall falls → border redirection), any practitioner Player Character, Edeyja (if Coherence crisis threatens Askeheim)

### ARC-S05: The Temporal Window
**Engine:** RS ≤ 60 threshold (threadwork v2.5 §Past-Oriented Pulling: requires TS 70+, RS ≤ 60)
**Emergence:** RS deteriorates below 60. Past-Oriented Pulling becomes mechanically accessible. Multiple factions learn this. Einhir Ritual Framework (§9.15) relevant.
**Non-Player Characters:** Any TS 70+ practitioner (Edeyja qualifies; player practitioners at late campaign), Klapp (archive records of past Pulling), Vossen (RM cultural memory)

### ARC-S06: The Duchess Holds the Line
**Engine:** Baralta TC suppression + Olafsson-Niflhel evidence
**Emergence:** Baralta Mandate ≥ 4 (suppression active, −1 TC/season). Players supply corroborating evidence of Olafsson-Niflhel connection. Baralta launches Domain Action vs Church Stability.
**Non-Player Characters:** Baralta (Hafenmark — suppression; NPC personal pool: Mandate 7 + Reach 5 per cp14 arcs), Olafsson (target), Solvind Brak (testimony — Intel vs Ob 3 to extract; Social scene to break Niflhel loyalty), Himlensendt (must act if Olafsson exposed), Klapp (if CE 4+ can provide archive access to restricted Church documents)
**[Note: Conflicting pool values between sources. cp14 arcs: Mandate 7 + Reach 5 vs Ob 3. narrative_scenario_chains: Mandate 4 + Reach 4 vs Ob 5 (partial evidence scenario). These may represent different evidence levels. NPC personal stats vs faction stats distinction applies.]**

### ARC-S07: The Princess in Altonian Territory / Torben Loyalty Clock
**Engine:** IP 30 threshold → Tutoring Demand → Torben Loyalty degradation
**Emergence:** IP reaches 30. Altonia issues formal Tutoring Demand for Torben. Crown options: refuse (IP +1 acceleration), negotiate delay (Influence 5 vs Ob 3; success defers 1 season), or surrender Torben (Loyalty clock begins at 8). Torben Loyalty degrades −1/season if Covert Contact (Crown Intel vs Ob 3/season) fails. Loyalty ≤ 3 → Coup Counter +1. Loyalty ≤ 2 → Crown Mandate −2 cumulative. Contact maintained 3 consecutive seasons → Loyalty floor 6 (retrieval straightforward).
**Non-Player Characters:** Torben (Loyalty track), Almud (Belief 1 vs Belief 3 collision), Elske (dynastic link — Resonant Style: Evidence), Laskaris (PROTECTIVE — delays demands; may leak imperial intentions to Elske; but flips if Elske Loyalty ≤ 2 → IP +3), Ehrenwall (Coup Counter +1 if Torben alignment changes)

### ARC-S08: The Faith that Destroys What It Defends
**Engine:** Klapp CE/TS tracks
**Emergence:** Cardinal Klapp (CE 4, TS 31) encounters Thread-significant object. TS growth check: Spirit TN 7 Ob 2 (essentialist formation raises Ob from 1 to 2). Success → crisis of faith. Head of Church education perceives what Church suppresses.
**Non-Player Characters:** Klapp (primary), Himlensendt (must choose: suppress Klapp via Inquisitor protocol, or deviate from doctrine — Spirit Ob 3 Stability check; failure = complies, success = deviates; deviation: Church Stability −1, TC −1), Haelgrund (parallel hidden TS 12 — if both exposed simultaneously: Church loses education AND investigation leadership), Olafsson (if Klapp crisis coincides with Niflhel exposure → Collision A)

### ARC-S09: The Framework Trap
**Engine:** Ethical framework Ob modifiers
**Emergence:** Church advances TC through covert Domain Actions via Niflhel channels. Crown Virtue Ethics: covert actions +1 Ob. Crown succeeds in open theatre but cannot address covert TC accumulation. Church categorical imperative: no direct effect on Ob. Hafenmark ad hoc: +1 Ob. Revolution Rawlsian: actions benefiting common population −1 Ob, concentrating power +1 Ob.
**Non-Player Characters:** Olafsson (Niflhel-Church connection), Almud (Crown Virtue Ethics), Strand (administrative response), Virke (if Niflhel channel exposed → supply chain cascade to Feldhaus)

### ARC-S10: The Revolution Eats Itself
**Engine:** Revolution ethical framework (Rawlsian Social Contract) + structural contradiction
**Emergence:** Revolution has Influence, Stability, Intel but no Mandate (rejects legitimacy). Community Weaving requires Mandate ≥ 1 (PP-195). RS declining — Weaving needed. Rawlsian framework: power-concentrating actions +1 Ob. Players must build to Mandate 1 while navigating framework constraints.
**Non-Player Characters:** Vossen (IDEALIST — spreads Presence thin), Maret Uln (if Vaynard eliminated → Varfell aligns with RM, relieving structural pressure), Revolution elder [EDITORIAL — not canonised]

### ARC-S11: The Headless Network
**Engine:** Niflhel four-arm structure (Quiet, Reckoners, Burned, Port) — decentralised control
**Emergence:** Players identify Niflhel as necessary (intelligence, covert, port). Each arm requires separate influence operation (Intel vs Ob 3). Uncontrolled arms act independently. Quiet is most operationally valuable but most visible to other arms — approaching Quiet first alerts Reckoners and Burned.
**Non-Player Characters:** Virke (Virke syndicate — trust network; NETWORK PROTECTOR), Olafsson (Niflhel-Church connection), Solvind Brak (evidence source)
**[GAP-ARC-01]:** Quiet deployment RS/Thread Tension accumulation cause pending editorial clarification.

### ARC-S12: The Favour Gate
**Engine:** Guild Favour threshold (≥ 5) for Economic Leverage unique action
**Emergence:** Guild Favour ≥ 5 required. Default 3. Seasonal cap ±2: minimum 1 season. Trade protection Domain Action (player pool vs Ob 2; success: +1 Favour; Overwhelming: +2). Economic Leverage roll: Wealth vs target Wealth.
**Non-Player Characters:** Feldhaus (PROFIT-MAXIMISING — Guilds Wealth over Mandate; Wealth recovery +1/season when she's active), Virke (supply chain connection)

### ARC-S13: The Duke Awakens
**Engine:** Vaynard TS 14 (Dormant) + Discovery Event
**Emergence:** Discovery Event trigger: Thread activity of sufficient intensity in proximity (practitioner at Relational scale nearby OR originary Lock deployed — per narrative_scenario_chains). Spirit TN 7 Ob 1. Success → TS jumps to 30 (Stirring), Certainty −1. Vaynard begins practice driven by TK urgency. TK +2 immediately.
**Non-Player Characters:** Vaynard (primary), Maret Uln (may facilitate or obstruct), Edeyja (if Vaynard seeks training)

### ARC-S14: Almud's Sympathies — The Sovereign Constraint
**Engine:** Almud's Belief 2 (structural lock) + erosion paths
**Emergence:** Almud privately sympathises with Einhir Restoration but acts within post-war settlement that suppressed it. Belief 2: "I cannot act until I find a path that doesn't require choosing between justice and the monarchy." The constraint erodes when one or more costs is removed: (a) Church discredited (TC −3 or more in one event) → Almud can act without Church opposition carrying weight; (b) northern Einhir nobility shifts (Revolution Influence 5+ in northern territories) → Mandate cost removed; (c) Baralta absorbs institutional cost via Hafenmark Influence in northern territories. If 218 AG truth revealed (accidental death) → Belief 2 revealed as 27 years of constraint in response to nothing → forced Belief revision.
**Non-Player Characters:** Almud (primary — Resonant Style: Consequence; show him what this costs Valoria), Baralta (can provide political cover), Vossen (RM Influence growth enables path (b)), Ehrenwall (no coup trigger from TS alone — cares about sovereignty, not theology)

### ARC-S15: The Southernmost Spiral
**Engine:** RS-driven cracking timeline
**Emergence:** RS reaches 50 (Stirring/Wakening boundary): outer Einhir winding shows strain. Stabilising Weaving (Ob 3, TS 40+) pauses cracking counter for 1 season (delay only). No Weaving for 3 consecutive seasons: outer winding begins to crack (RS +1/season from Southernmost). 3 more seasons without Ceiral Ritual: outer winding fails (RS +2/season — automatic, unremovable until Ritual). Expedition requires RS ≥ 40 and practitioner TS 30+.
**Non-Player Characters:** Edeyja (Southernmost authority; WC track = her engagement threshold: WC ≥ 1: +1D Thread ops; WC ≥ 2: RS decay halved; WC ≥ 3: RS +2/season), Maret Uln (TS ~50 — expedition candidate), Vossen (TS 25 — below Forgetting resistance gate of 29, cannot participate safely)

### ARC-S16: Coherence Zero — Vaynard
**Engine:** Vaynard TS 30 + endgame Coherence dynamics
**Emergence:** Discovery Event success → TS 30 → practice at scale. Consequentialist framework meets ontological experience. Belief revision required.
**Non-Player Characters:** Vaynard, Edeyja, Maret Uln

### ARC-S17: Coherence Zero — Almud
**Engine:** Almud TS 28→30 + First Leap
**Emergence:** Discovery Event → TS 30 → practice under crisis pressure. Most radical resolution: practitioner-king.
**Non-Player Characters:** Almud, Ehrenwall, Himlensendt, Elske (if installed independently → Almud retires to practitioner path?)

### ARC-S18: Coherence Zero — Lenneth
**Engine:** Lenneth CE accumulation → TS growth
**Emergence:** CE from concealed practice. TS grows through self-directed work using archive holdings.
**Non-Player Characters:** Lenneth (primary), Torsvald (archive connection — TS 35 developed from same exposure; natural escort for Lenneth's arc), Ehrenwall (if Lenneth exposed → dynastic implications)

### ARC-S19: The Quaestio of Baralta
**Engine:** TC 42 threshold → Grand Debate + multi-system convergence
**Emergence:** TC reaches 42. Grand Debate fires (5 exchanges, theological contest). Coup Counter, Niflhel Quiet Network, and Mass Battle all potentially converge.
**Non-Player Characters:** Baralta (Solmund claim — Evidence Style + documented precedent), Himlensendt (Debate opponent — Faith + Evidence Resonant Style), Ehrenwall (Coup Counter implications), Vaynard (intelligence), Maret Uln (dual loyalty), Olafsson (Niflhel connection), Klapp (archive testimony — first-person accounts of Solmund's works), Revolution elder (inner-tradition testimony) [EDITORIAL]

### ARC-S20: Ehrenwall's Count
**Engine:** IP 30 → Tutoring Demand → Torben Loyalty → Coup Counter chain
**Emergence:** IP reaches 30 (same trigger as ARC-S07). Tutoring Demand fires. If Torben surrendered and Contact fails: Loyalty degrades. Loyalty ≤ 3 → Coup Counter +1. If Counter reaches 3 → Martial Law. Simultaneously: TC ≥ 40 + Crown inaction → Counter +1. Crown territory loss → Counter +1. Multiple paths to Counter 3 in same season possible.
**Non-Player Characters:** Ehrenwall (Coup Counter threshold 3), Brandt (succession: threshold 2, redirects military to borders — Military actions T3/T10 at −1 Ob, all other territories +1 Ob), Almud (target), Torsvald (Riskbreaker exposure), Almstedt (Ministry disruption)

### ARC-S21: The Klapp Threshold
**Engine:** Klapp CE 4 + sustained archive contact with originary Locks
**Emergence:** Klapp's CE from archive work. TS development via threadwork v2.5 §2.3 Discovery. If Klapp converts: TC generation pauses (Church Stability ≤ 4), Church internal fracture.
**Non-Player Characters:** Klapp (primary), Himlensendt (must choose: Inquisitor suppression protocol or refuse — Spirit Ob 3 check), Haelgrund (parallel TS — if both exposed: Church loses education + investigation), Olafsson (if simultaneous → Collision A)

### NPC-ARC-HAE: The Haelgrund Defection
**Engine:** Haelgrund hidden TS 12 + practitioner proximity
**Emergence:** Any Player Character TS ≥ 30 interacting with Haelgrund during investigation can attempt Diagnosis (Cognition vs Ob 2). Success reveals TS. What Player Character does with information defines the arc.
**Non-Player Characters:** Haelgrund (primary — TS 12, attributes "hunches" to investigative instinct), Himlensendt (institutional response), Klapp (parallel crisis if simultaneous)
**Consequence:** Defection → Church Heresy Investigation Ob +1 permanently. Haelgrund available as neutral practitioner (TS 12 — symbolically devastating). BG Event Card trigger: Thread operation Overwhelming within 1 territory of investigation AND no active Inquisitor suppression.

### NPC-ARC-TOR: The Torsvald Exposure
**Engine:** Torsvald TS 35 + abort pattern in Thread-active zones
**Emergence:** ~30% abort rate when Torsvald leads Riskbreaker operations in Thread-active territories. Aborted operations leave evidence → Deniability Debt +1. Pattern detectable over multiple seasons.
**Non-Player Characters:** Torsvald (primary), Ehrenwall/Brandt (superior officer detects pattern), Lenneth (archive connection — Torsvald is natural escort; her TS developed from same archive exposure)
**Consequence:** Crown covert capability −1D per abort. Torsvald becomes potential bridge between Lenneth and practitioner world.

### NPC-ARC-BRA: The Brandt Succession
**Engine:** Ehrenwall removal → succession
**Emergence:** Ehrenwall removed (death, player action, Lions' Table Mutiny). Brandt takes command. Military redirects from internal control to border defence (T3, T10). Coup Counter threshold drops from 3 to 2.
**Non-Player Characters:** Brandt (primary — EXTERNAL THREAT FIXATED), Ehrenwall (predecessor), Almud (coup target dynamics change), Laskaris (if border focus validates Altonian threat → IP dynamics shift)
**Consequence:** Crown territories lose Martial Law garrison coverage. Military T3/T10 at −1 Ob, all others +1 Ob.

### NPC-ARC-FEL: The Supply Chain Exposure
**Engine:** Thread-touched goods in Guilds supply chain via Niflhel/Virke
**Emergence:** Investigation: Intel + Thread Diagnosis on guild goods (Ob 3). Cascades to Virke (shared supply chain).
**Non-Player Characters:** Feldhaus (Guilds), Virke (Niflhel syndicate), Haelgrund (if Church opens Heresy Investigation), Olafsson (if Niflhel connection exposed simultaneously)
**Consequence:** Guilds Wealth −1, Stability −2. Church free Heresy Investigation vs Guilds. Virke network disrupted (Niflhel trade +1 Ob, 2 seasons). OR: quiet audit (1 Wealth + 1 Stability) removes Thread goods, no scandal, permanent Wealth recovery bonus lost.

### NPC-ARC-STR: Strand Turned
**Engine:** Strand flattery vulnerability (−1 Ob) + Intel action
**Emergence:** Non-Crown faction Intel Overwhelming targeting Crown Court. Strand's insecurity = lowest-Ob approach vector.
**Non-Player Characters:** Strand (primary), Almud (consequences), targeting faction
**Consequence:** Intelligence leak (full Crown stat line + planned actions). Strand removed. Crown admin +1 Ob, 2 seasons. Counter-play: Crown Intel vs Ob 2 each season.

### NPC-ARC-VIR: The Virke Recall
**Engine:** Virke trust network vs family discipline
**Emergence:** Virke shields partners from family operations. Third instance → family intervention. Replacement has no local relationships.
**Non-Player Characters:** Virke (primary), Feldhaus (loses Thread-touched luxury goods access), all factions in trust network
**Consequence:** Trust network collapses. All Niflhel trade +1 Ob for remainder of campaign.

### NPC-ARC-LAK: The Laskaris Flip
**Engine:** Laskaris PROTECTIVE flaw + Elske Loyalty track
**Emergence:** Elske Loyalty ≤ 2 at Accounting OR Elske Return attempt fails. Laskaris stops shielding Valoria.
**Non-Player Characters:** Laskaris (primary), Elske (trigger condition), Almud (Crown consequences), Torben (if simultaneously under Altonian control → both royals compromised)
**Consequence:** IP +3 immediately. Imperial-loyal governor replaces Laskaris. IP generation returns to baseline. Elske off-board card locked (Crown Influence vs Ob 4 to reopen).

### NPC-ARC-SOL: The Solberg Recall
**Engine:** Schoenland central discovers stability bias
**Emergence:** Schoenland reassessment or discovery of downplayed intelligence. Solberg recalled.
**Non-Player Characters:** Solberg (primary), all faction leaders
**Consequence:** Arms supply +1 unit/season to all factions. Intelligence sharpens. Schoenland more dangerous. Counter-play: offer credible stability treaty → Solberg becomes genuine Crown/Hafenmark asset.

### NPC-ARC-PRU: The Parish Revolt
**Engine:** Prudence Cardinal tithe pressure + Church Mandate erosion
**Emergence:** ≥ 3 over-tithed territories AND Church Mandate ≤ 3 in any. Parish leaders refuse collection.
**Non-Player Characters:** Prudence Cardinal (primary), Himlensendt, Vossen (RM recruitment in over-tithed territories — CV erosion +1/Year-End)
**Consequence:** Church Wealth −2, 1 season. CV −1 in affected territories. TC −1 (institutional fracture). Counter-play: 1 Stability to discipline (tithes restored, Mandate −1 permanently).

### NPC-ARC-ULN: The Maret Uln Succession
**Engine:** Vaynard elimination → Varfell succession (PP-486)
**Emergence:** Vaynard eliminated (Loyalty 0 + Mandate 0). Maret Uln takes leadership. VTM resets to 0. Varfell aligns with RM: cannot target RM, cannot seize RM territory. This is factional realignment, NOT RM Emergence.
**Non-Player Characters:** Maret Uln (primary), Vaynard (predecessor), Vossen (RM alignment), Edeyja (Maret TS ~50 → potential Warden cooperation)

### NPC-ARC-VOS: The Vossen Exposure
**Engine:** Church AP accumulation against Vossen (+1/season when she operates publicly)
**Emergence:** Vossen cannot lead from hiding (movement requires visible leadership for Popular Will). Heresy Investigation accumulates toward resolution.
**Non-Player Characters:** Vossen (primary), Haelgrund (if assigned — +1 season but Overwhelming), Maret Uln (if Varfell aligned with RM → protection), Revolution elder (leadership vacuum if Vossen removed)

### ARC-S22: RM Emergence
**Engine:** Warden's Accord (WA) track + CV decay + RS threshold (BG) / Founding Mechanic (Hybrid)
**Emergence (BG):** Triple-condition: WA ≤ −2 AND ≥ 3 territories CV ≤ 1 AND RS ≤ 50. One-shot. Suppression: WA ≥ 0 OR all territories CV ≥ 2 OR RM Stability 0.
**Emergence (Hybrid):** PP-478 replaces WA-based emergence with Founding Mechanic. RM solo victory and co-victories available only after Founding.
**Non-Player Characters:** Vossen (primary — Founding Agent candidate; if Founding Agent, her Influence roll determines RM starting stats), Maret Uln (if Varfell realigned → RM gains practitioner-led ally), Revolution elder [EDITORIAL]

### ARC-S23: Elske Independence
**Engine:** Elske Conviction (Family vs Self-Determination) + evidence-driven decision tree
**Emergence:** Contact established (any faction; Circles Ob 3 — she's in Altonian territory). Three approach vectors: Protect Torben (most receptive — requires evidence of harm at Loyalty 3 or lower), Take the Throne (requires evidence Torben beyond saving + evidence she can rule independently), Serve Valoria (least receptive alone — must combine with another). Resonant Style: Evidence — abstract appeals fail.
**Non-Player Characters:** Elske (primary), Laskaris (PROTECTIVE — has leaked imperial intentions twice; genuine regard for her autonomy), Torben (family trigger), Almud (if Elske installed → succession implications)

### ARC-S24: Baralta Succession
**Engine:** Baralta elimination (Loyalty 0 + Mandate 0) + PI gate (PP-487)
**Emergence:** If Baralta eliminated: PI ≥ 4 → institutional succession (Hafenmark Mandate −1, Stability −1, mechanics intact). PI < 4 → fracture (Mandate halved, TCV requirement +2, Parliamentary Sovereignty unavailable until PI ≥ 4). No named successor — Hafenmark's identity is institutional.
**Non-Player Characters:** Baralta (eliminated), Almstedt (PI recovery determines which path fires), Himlensendt (if excommunication was cause → TC +4 already applied)

### ARC-S25: Warden Cooperation Progression
**Engine:** Warden Cooperation (WC) track (0–3) / Warden Recognition (WR) track (0–4)
**Emergence:** WC advances through any faction's Askeheim (T15) Expedition engagement. WR advances only through Varfell's Expedition actions. If no faction engages with Askeheim, RS trends toward 0 and second Calamity occurs.
**Non-Player Characters:** Edeyja (engagement threshold — WC is her decision that practitioners have demonstrated competence and integrity), Vaynard (WR track for Varfell Path B), Maret Uln (if Varfell leader → WR progression style changes)
**Key values:** WC ≥ 1: +1D all Thread ops. WC ≥ 2: RS decay halved. WC ≥ 3: RS +2/season. WR 4: Edeyja makes substantive contact.

---

## Tertiary Arcs

### ARC-T01: The Tied Vote
**Engine:** Parliamentary Vote tie condition
**Emergence:** Vote called. Best of 3 exchanges; tie = motion fails by abstention → TC +1 AND RS −1 simultaneously. Pre-vote whipping via Influence Domain Actions (Ob 2–3).
**Non-Player Characters:** Almstedt (facilitates procedure), Baralta (sovereignty motions), Himlensendt (Church authority motions), Almud (Crown position)

### ARC-T02: The Tutoring Demand (branching)
**Engine:** IP 30 → Almud Belief collision (branching detail of ARC-S07)
**Emergence:** IP reaches 30. Almud faces Belief 1 (Altonian trade) vs Belief 3 direct collision. Crown Influence vs Ob 3 (negotiate delay) or refuse (IP +1 acceleration). Distinct from ARC-S07 in that this tracks Almud's personal Belief crisis rather than the Torben Loyalty mechanics.
**Non-Player Characters:** Almud (Belief crisis), Torben, Laskaris (delays demand), Ehrenwall (Counter +1 if Torben taken)

### ARC-T03: The Excommunication
**Engine:** Olafsson Church Mandate roll vs Baralta Mandate
**Emergence:** Olafsson files complete (2 seasons building). Excommunication declared vs Baralta. Church Mandate pool (5d10) TN 7 vs Ob 7 (Baralta personal Mandate). Players may intervene with counterevidence (−1 Ob).
**Non-Player Characters:** Olafsson (initiator), Baralta (target — if excommunicated: TC +4 immediately, suppression ends permanently), Himlensendt (arbiter)
**Consequence if successful:** Baralta TC suppression permanently removed. TC +4 one-time. Hafenmark loses its most critical TC-management tool. ARC-P01 accelerates drastically.

### ARC-T04: The Ceiral Ritual
**Engine:** Multiple narrow prerequisites
**Emergence:** Ceiral Text held, Awareness 5+, Maret Uln TS 60+, 2× TS 20+ participants, preparation season, all personnel in Askeheim (T13). Lead Weaving pool vs Ob 5. Success: RS −6 to −10 (world healing). Failure: RS +8, Mode 3 entity, lead practitioner incapacitated.
**Non-Player Characters:** Maret Uln (if lead — TS ~50, may need further growth), Edeyja (Askeheim access), practitioner Player Characters
**Failure cascade (Collision C):** RS +8 + IP +2 + TC +2. If RS near 50 → Southernmost cracking clock resets. Coup Counter may reach 3 from single-season cascade.

### ARC-T05: The General Falls
**Engine:** Combat wound threshold + single Medicine roll
**Emergence:** Ehrenwall in Mass Battle. Wound in Phase 4 or from Thread operation. Wounds reach ceiling(Health ÷ 2). Medicine Ob 2 in Phase 5 — one-turn window.
**Non-Player Characters:** Ehrenwall (primary), Brandt (immediate succession → NPC-ARC-BRA fires), Torsvald (if present → abort risk)

### ARC-T06: The Schoenland Pivot
**Engine:** Solberg observation + Domain Action
**Emergence:** Schoenland reads political situation each season (Mandate levels, Prosperity, IP, trade disruption, Altonian intelligence from T15). Crown Influence vs Ob 3.
**Non-Player Characters:** Solberg (STABILITY-SEEKING bias), Laskaris (Altonian intelligence source), Strand (Crown diplomatic capacity)

### ARC-T07: The Dissolution
**Engine:** Player choice + TS 50+ prerequisite
**Emergence:** Practitioner declares Dissolution. TS 50+ required. Diagnosis mandatory. Target: NPC configuration, institutional record, Locked Zone border, political thread. Spirit + relevant pool vs Ob (min 4). RS consequences: Success −5, Failure −8.
**Non-Player Characters:** Edeyja (Dissolution authority), Maret Uln (TS ~50 — meets threshold), practitioner Player Characters

### ARC-T08: Vaynard's Confession (Hybrid)
**Engine:** Vaynard TK 4 + Hybrid multi-system convergence
**Emergence:** TK reaches 4 (practitioner relationship × 2 seasons). Multiple systems converge: TK track, Discovery Event, Thread operations, Inquisitor CE track, Parliamentary Vote, faction play.
**Non-Player Characters:** Vaynard, Maret Uln, Olafsson, Baralta (if simultaneous with Solmund claim), Klapp (archive evidence), Haelgrund (Inquisitor CE track)

### ARC-T09: The Forgetting Road
**Engine:** Player choice + TS 30 prerequisite
**Emergence:** Expedition to Southernmost. TS ≥ 30 required (below 30 → dissolve without awareness per §6.1). Domain Echo consequences on return. TC spike.
**Non-Player Characters:** Edeyja, Maret Uln (if expedition member), Vossen (TS 25 — below threshold)

### ARC-T10: TC 75+ Phase Transition
**Engine:** TC clock reaching 75
**Emergence:** TC freezes. Church shifts entirely to Territorial Seizure mode. AER no longer modifies TC gains. Church prioritises seizure actions.
**Non-Player Characters:** Himlensendt (Church head — seizure policy), Baralta (Sovereign Authority Doctrine as response), all territorial controllers

### ARC-T11: IP 75+ Altonian Vanguard
**Engine:** IP clock reaching 75
**Emergence:** Altonian Vanguard deployed at T10 (Spartfell) and T16 (Schoenland). AER ≥ 4 raises threshold to 80. AER 5: IP held at 50 (Altonia satisfied with relationship).
**Non-Player Characters:** Laskaris (if still active — may have already flipped), Brandt (if Ehrenwall successor — border focus validated), Solberg (if still active — Schoenland response), Almud (Crown must respond)

### ARC-T12: Baralta BG Conviction / Vaynard BG Conviction
**Engine:** One-time mechanical events at specific thresholds
**Emergence:** Baralta: fires at Accounting where PI ≥ 6 OR Hafenmark TCV ≥ 12. Effect: Hafenmark Mandate +1 (one-time). Vaynard: fires at Accounting where VTM ≥ 4 AND Varfell controls T9 or T13. Effect: Varfell Mandate +1 AND VTM +1 (one-time).
**Non-Player Characters:** Baralta (Hafenmark), Vaynard (Varfell), Almstedt (PI level determines Baralta trigger)

### ARC-T13: Torben After Crown Elimination
**Engine:** Crown elimination → Torben Loyalty transfer (PP-494)
**Emergence:** If Crown eliminated: Torben Loyalty transfers to Löwenritter as dynastic successor. Track meaning shifts (0 = aligns with anti-Löwenritter faction; 7 = full Löwenritter loyalty). Löwenritter inherits current Loyalty value.
**Non-Player Characters:** Torben, Brandt/Ehrenwall (Löwenritter inheritor), Laskaris (Altonian response)

---

## Collision Scenarios (Multi-Arc Convergence)

### COLLISION A: Church Double Fracture
**Trigger:** Klapp conversion (ARC-S21: TS 30+, CE 4) coincides with Olafsson exposure (ARC-S06)
**Effect:** Church Stability −3. TC generation pauses (Stability ≤ 4, Cardinals competing). Window opens for player action without TC escalation. Klapp becomes practitioner ally with archive access and originary Locks. If Himlensendt refuses Inquisitor protocol against Klapp: Spirit Ob 3 check; success = deviates (Church Stability −1, TC −1); failure = complies (Klapp suppressed, window closes).
**Non-Player Characters:** Klapp, Olafsson, Himlensendt, Haelgrund (if also exposed → triple fracture: Church loses education, justice, and investigation)

### COLLISION B: The Einhir Practitioner King
**Trigger:** Almud Discovery Event (ARC-S17: TS 28→30) + Elske installed independently (ARC-S23) + Torben in Altonia (ARC-S07)
**Effect:** Almud publicly acknowledges Thread practice → TC +3 but RS improves (new practitioner with high TS capital supports Mending). Axis 9 resolves publicly. Elske as Queen in practice; Almud retires to practitioner path or governs as practitioner-king (most radical narrative resolution).
**Non-Player Characters:** Almud, Elske, Ehrenwall (no coup trigger from TS alone), Himlensendt (doctrinal crisis), Laskaris (protective instinct may be satisfied if Elske installed)

### COLLISION C: Tutoring Demand + Southernmost Failure
**Trigger:** Torben at Loyalty 3 (ARC-S07) coincides with Ceiral Ritual failure (ARC-T04)
**Effect:** RS +8, IP +2, TC +2 in single season. If RS near 50: Southernmost cracking clock resets + RS +2/season. Ehrenwall Coup Counter may reach 3 from single-season cascade (Torben Loyalty ≤ 3 = +1; TC possibly ≥ 40 from +2 = +1; territory loss from RS surge possible = +1). Players face: retrieve Torben OR contain RS OR prevent TC crossing 40 — all simultaneously, with lead practitioner incapacitated.
**Non-Player Characters:** Torben, Almud, Ehrenwall, lead practitioner (incapacitated), Laskaris (IP surge)

### COLLISION D: Niflhel Weaponises Everything
**Trigger:** Full Church-Niflhel exposure + assassination perpetrator = Niflhel + Varfell Private Collection in Niflhel's hands
**Effect:** Niflhel has leverage over every faction simultaneously (Church: Olafsson; Crown: assassination secret; Varfell: if they hired Niflhel). Sells to highest bidder. If Varfell pays: TK 4+ + Niflhel Intel = most dangerous information actor, TC +3. If Church pays: Olafsson suppressed, assassination buried, TC acceleration resumes. If Crown pays: Riskbreaker Deniability Debt +3, Parliamentary inquiry, Grand Debate threatens Crown Mandate. If nobody pays: Niflhel arms Schoenland → IP +2/season.
**Non-Player Characters:** Virke (broker), Olafsson, Vaynard, Strand (if Crown pays → Deniability Debt)

### COLLISION E: The Einhir Elder and Baralta's Claim
**Trigger:** Revolution elder testimony + Baralta Solmund claim (ARC-S19) + Klapp archive access
**Effect:** Grand Debate (5 exchanges). If both elder and Klapp testify: Himlensendt's Evidence Resonant Style turned against his institution. If reinterpretation fails (net ≤ 0): Inspiration loss, Destabilisation Trigger fires fully (Church relics ARE originary Locks), Church Stability −3 in one season. Axis 9 resolves publicly. Originary Locks enter public discourse → practitioner attempts → RS consequences severe.
**Non-Player Characters:** Baralta (Evidence Style + documented precedent), Himlensendt (Evidence Resonant Style — vulnerable to proof), Klapp (archive testimony — Cardinal reassignment records, first-person accounts), Revolution elder [EDITORIAL — not canonised], Edeyja (if originary Lock attempts → substrate authority)

---

## Endgame Configuration

The campaign's central dramatic question resolves when ≥ 3 are simultaneously true:

| Condition | Effect | Primary Arcs |
|-----------|--------|--------------|
| Almud TS 30+ | Monarchy acknowledges Thread reality | S17, Collision B |
| Axis 9 resolves publicly | Church foundational claim contested | P04, Collisions B/E |
| Elske installed independently | Succession stable without Altonia | S23, S07 |
| Torben retrieved, Loyalty 6+ | Dynasty intact | S07, T02 |
| RS above 40 | Practitioners functional; world stabilising | P02, S04, S05, S15 |
| TC below 40 | Church institutional conquest stalled | P01, S19, S21, NPC-PRU |
| IP below 45 | Altonian invasion deterred | P03, S07, S20, NPC-LAK |
| Coup Counter ≤ 1 | Löwenritter loyal | P03, S20, T05, NPC-BRA |
| Southernmost stabilised (Ceiral success) | RS −6 to −10; world healing | T04, S15 |

**All nine:** STABLE — the peninsula survives intact, changed.
**None:** The Einhir Catastrophe repeats — political and metaphysical collapse conditions recreated.

**Shared Loss Conditions (campaign ends, all factions lose):**
- RS = 0 at Accounting → Rupture (Second Calamity)
- IP ≥ 100 AND AER ≤ 1 → Altonian Conquest
- All playable factions at Stability 0 simultaneously → Total Institutional Collapse

---

## Arc Dependency Map

```
PRINCIPAL ENGINES
─────────────────
ARC-P01 (TC clock — passive +1/season)
  ├→ ARC-S06 (Baralta suppression — counterweight, Mandate ≥ 4)
  │    └→ ARC-T03 (Excommunication — removes suppression + TC +4)
  │         └→ ARC-S24 (Baralta Succession — PI-gated)
  ├→ ARC-S09 (Framework Trap — covert TC acceleration)
  ├→ ARC-S19 (Quaestio — TC 42)
  │    └→ COLLISION E (Einhir Elder + Baralta claim)
  ├→ ARC-T01 (Tied Vote — TC +1 spike)
  ├→ ARC-T10 (TC 75+ Phase Transition — seizure mode)
  ├→ ARC-S21 (Klapp Threshold → TC pause)
  │    └→ COLLISION A (Church Double Fracture)
  └→ NPC-ARC-PRU (Parish Revolt — TC −1, CV erosion)

ARC-P03 (Coup Counter — 3 increments)
  ├→ via TC ≥ 40: links to ARC-P01
  ├→ via Torben Loyalty ≤ 3: links to ARC-S07
  │    └→ NPC-ARC-LAK (Laskaris Flip — IP +3)
  ├→ via territory loss: links to any war/seizure arc
  ├→ ARC-S20 (Ehrenwall's Count — Counter fires)
  │    └→ ARC-T05 (General Falls → NPC-ARC-BRA)
  └→ ARC-T02 (Tutoring Demand — Almud Belief crisis)
       └→ COLLISION C (+ Ceiral failure)

ARC-P02 (RS clock — decay)
  ├→ ARC-S04 (Rendering Debt — war ×3 multiplier)
  ├→ ARC-S05 (Temporal Window — RS ≤ 60)
  ├→ ARC-S02 (Brittle Peace — localised RS stress)
  ├→ ARC-S15 (Southernmost Spiral — cracking timeline)
  │    └→ ARC-T04 (Ceiral Ritual — RS recovery or failure)
  ├→ ARC-S25 (Warden Cooperation — RS recovery tool)
  └→ ARC-S16/S17/S18 (Coherence Zero — endgame)

ARC-P04 (Axis 9)
  ├→ ARC-S01 (Vaynard Cascade — TK track)
  │    ├→ ARC-S13 (Duke Awakens — TS 14 Discovery)
  │    ├→ ARC-T08 (Confession — TK 4 Hybrid)
  │    └→ NPC-ARC-ULN (Maret Uln Succession)
  ├→ ARC-S03 (Tribunal — Church response)
  │    └→ NPC-ARC-HAE (Haelgrund Defection — TS exposed)
  ├→ ARC-S08 (Klapp TS → Faith that Destroys)
  │    └→ ARC-S21 (Klapp Threshold)
  ├→ ARC-S14 (Almud's Sympathies — erosion paths)
  └→ COLLISION B (Practitioner King — Almud TS 30+)

ARC-P08 (218 AG Investigation)
  ├→ ARC-S14 (Almud Sympathies — Belief 2 collapses if truth revealed)
  └→ COLLISION D (Niflhel Weaponises — if assassination = Niflhel)

ARC-P05 (NPC AI — runs when players absent)
  ├→ ARC-T06 (Schoenland Pivot — NPC reads)
  ├→ NPC-ARC-SOL (Solberg Recall)
  └→ ARC-S22 (RM Emergence — WA/CV/RS triple condition)

ARC-P06 (Accounting Sequence) → [cross-cuts all arcs via seasonal order]
ARC-P07 (Faction That Breaks) → [any faction under sustained pressure]

INDEPENDENT ENTRY (player-initiated / NPC-driven)
  NPC-ARC-FEL (Supply Chain Exposure)
  NPC-ARC-STR (Strand Turned)
  NPC-ARC-VIR (Virke Recall)
  NPC-ARC-TOR (Torsvald Exposure)
  NPC-ARC-VOS (Vossen Exposure)
  ARC-S11 (Headless Network)
  ARC-S12 (Favour Gate)
  ARC-S23 (Elske Independence)
  ARC-T07 (Dissolution)
  ARC-T09 (Forgetting Road)
  ARC-T11 (IP 75+ Vanguard)
  ARC-T12 (BG Convictions)
  ARC-T13 (Torben After Crown Elimination)

COLLISION SCENARIOS
  A: Church Double Fracture (S21 + S06)
  B: Practitioner King (S17 + S23 + S07)
  C: Tutoring + Southernmost (S07 + T04 failure)
  D: Niflhel Weaponises (S11 + S06 + assassination)
  E: Einhir Elder + Baralta Claim (S19 + elder + Klapp)
```

---

## Simulation Coverage

| Arc ID | Simulated | Notes |
|--------|-----------|-------|
| ARC-P01 through P07 | Partial (via CP14 arcs 1–30 batch) | Clock interactions covered; NPC AI behaviour not independently simulated |
| ARC-P08 | Not simulated | 218 AG Investigation is narrative design, no mechanical simulation run |
| ARC-S01–S12 | Yes (CP14 batch, arcs 1–19) | |
| ARC-S13 | Yes (CP14 arc 26) | |
| ARC-S14 | Not simulated | Almud Sympathies — narrative_scenario_chains ARC 2 |
| ARC-S15 | Not simulated | Southernmost Spiral — narrative_scenario_chains ARC 7 |
| ARC-S16–S18 | Yes (CP14 arcs 28–30) | |
| ARC-S19 | Yes (CP14 arc 31) | Clean |
| ARC-S20 | **Not yet simulated** | Ehrenwall's Count (CP14 arc 34) |
| ARC-S21 | **Not yet simulated** | Klapp Threshold (CP14 arc 35) |
| ARC-S22 | Not simulated | RM Emergence |
| ARC-S23–S25 | Not simulated | Elske Independence, Baralta Succession, Warden Cooperation |
| NPC-ARC-* | **Not simulated** | All NPC-derived arcs from roster |
| ARC-T01–T13 | Mixed | T01–T09 partially via CP14; T10–T13 not simulated |
| Collisions A–E | **Not simulated** | narrative_scenario_chains scenarios |

---

## Open Items

| ID | Item | Status |
|----|------|--------|
| GAP-ARC-01 | Arc S11 — Niflhel Quiet deployment RS/Thread Tension cause | Pending editorial clarification |
| GAP-ARC-02 | IP generation formula — no canonical base advancement rate | bg_v05 gap; narrative_scenario_chains uses +2/season working assumption |
| GAP-ARC-03 | Jarnstal — no mechanical tracks, no AI flaw | NPC design gap |
| GAP-ARC-04 | Baralta NPC personal stats — conflicting values between cp14 arcs and narrative_scenario_chains | May represent different evidence levels |
| ED-NEW-01 | Tier assignments (principal/secondary/tertiary) | Provisional — user review required |
| ED-NEW-02 | Revolution elder — not canonised as named character | Required for Collision E |
| ED-NEW-03 | Elske TS development — not established | Affects Collision B branching |
| ED-NEW-04 | 218 AG resolution — narrative_scenario_chains presents accidental death as design intent; E-01 flagged as unresolved elsewhere | Reconciliation needed |
| ED-358 | Full roster identities, motivations, stat blocks | Provisional — user review pending |
| E-01 | Perpetrator of 218 AG assassination | Unresolved (but see ED-NEW-04) |

---

## Corrections Log (v1 → v2)

| Error | v1 Text | v2 Correction | Source |
|-------|---------|---------------|--------|
| Baralta faction | "Crown (independent)" | Hafenmark | stage6_factions line 241, victory_architecture §7 Step 5 |
| Baralta TC suppression | "Mandate ≥ 5" (throughout) | Mandate ≥ 4 | params_factions line 144, victory_architecture §7 |
| TC generation | "Church Mandate ≥ 5 → TC +1/season automatic" | TC +1/season passive (institutional momentum, PP-402); Conviction Yield adds more; Suppress negates passive only | params_factions §TC Passive Advance, victory_architecture §7 |
| RS cross-clock | "RS ≤ 55 → cross-clock fires: TC +1/season, IP +1/season" | NOT CANONICAL. RS effects are proximity-graduated. No TC/IP coupling. | params_board_game §RS Effects; narrative_scenario_chains was scenario doc |
| Coup Counter | Conflated IP 30 with direct Counter increment | IP → Tutoring Demand → Torben Loyalty → Counter. Three specific increments only. | params_factions §Löwenritter |
| Vaynard TK TC effects | Not specified per level | TK 3 = TC +1, TK 4 = TC +2, TK 5 = TC +3 | narrative_scenario_chains ARC 9 |
| Baralta excommunication | Not mentioned | TC +4 immediately, suppression ends permanently | params_factions line 144 |
| Missing arcs (11) | Not present in v1 | Added: P08, S14, S15, S22–S25, T10–T13 | Various sources |
| ARC-09 pool | "Mandate 7 + Reach 5 vs Ob 3" only | Flagged conflicting values between sources | cp14 arcs vs narrative_scenario_chains |
