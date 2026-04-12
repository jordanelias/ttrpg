# Arc Register

> **Version:** 7 (delay vs preclusion evaluation — roll failures reclassified)
> **Status:** WORKING DRAFT
> **[EDITORIAL: ED-NEW — Tier assignments are provisional pending user review]**
> **Sources fetched this session:** `designs/gm_ref_cp14/arcs/*` (11 files), `gm_ref/arcs_*` (3 files), `designs/npcs/npc_roster.md`, `designs/npcs/npc_comprehensive_audit.md`, `designs/npcs/npc_character_analyses_existing.md`, `designs/npcs/npc_roster_caste_annotations.md`, `references/params_factions.md`, `references/params_threadwork.md`, `references/params_board_game.md`, `designs/board_game/victory_architecture_v1.md`, `designs/board_game/valoria_bg_v05_simulation_and_patches.md`, `designs/ttrpg/valoria_narrative_scenario_chains.md`, `compilation/v0.14/stage6_factions.md`, `canon/02_canon_constraints.md`

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
| King Almud | Crown | Beliefs (3: Altonian trade, unresolved ethical doubt about caste, RM as governance input), TS 0 (northern, Church-culturally integrated; Discovery Event = rupture not confirmation), Resonant Style: Consequence. Historical anchor: Manuel I Komnenos. | `stage6_factions`, `narrative_scenario_chains` ARC 2, `npc_character_analyses_existing` (ED-364 rewrite) |
| Duchess Inge Baralta | Hafenmark | Mandate (personal: 7 per cp14 arcs; faction: 4 per starting stats), Reach (5 per cp14 arcs), TC suppression (−1/season while her Mandate ≥ 4), Sovereign Authority Doctrine (once per campaign arc), Solmund claim [EDITORIAL]. **Active Crown ambition** — decades-long institutional campaign for throne (deed-claim strongest on peninsula). Pure RM adversary (Einhir revival threatens sovereign divine right). Historical anchor: Isabella I of Castile. Leadership Deviation Ob 1 — she IS Hafenmark. | `params_factions`, `stage6_factions`, `narrative_scenario_chains` ARC 3, `npc_character_analyses_existing` (deed-monarchy reframing) |
| Grandmaster Sigrid Ehrenwall | Löwenritter | Coup Counter (0–3, fires at 3; never decrements) = deed-logic enforcement mechanism (each increment: data point toward "deed-presumption failing"). Would transfer loyalty to Baralta without experiencing it as betrayal. Health/Wound track (incapacitation at ceiling(Health ÷ 2)), Lions' Table. | `params_factions`, `arcs_20_23`, `npc_character_analyses_existing` (deed-monarchy reframing) |
| Cardinal Arnlod Olafsson | Church (Justice) | Niflhel connection (hidden — used Niflhel to suppress texts/individuals), Church Intel operations, Heresy Investigation authority | `narrative_scenario_chains` ARC 4, `arcs_09_11` |
| Duke Magnus Vaynard | Varfell | Thread Investigation Track (TK 0–5; TC effects: TK 3 = +1, TK 4 = +2, TK 5 = +3), Thread Sensitivity (TS starts 14 Dormant — from southern Einhir environmental exposure, not artefact contact), Private Collection (Intel vs Ob 2, each use: hidden TS +1; at TS 14+ triggers Spirit TN 7 Ob 1 Discovery Event), Belief 3 (succession leverage). "The Revolutionary" — wants Church and Altonian cultural residue expelled from peninsula. Historical anchor: Reinhard von Lohengramm. The Forgetting is his political prison (cannot build coalition because non-practitioners cannot retain the argument). | `params_factions`, `narrative_scenario_chains` ARC 9, `npc_character_analyses_existing` |
| Confessor Arne Himlensendt | Church (head) | Resonant Style: Evidence (responds to documentation — ironic vulnerability: cannot perceive the evidence that matters). "Most dangerous person on the peninsula and does not know it" — sincere faith is load-bearing wall of post-war settlement. TC accumulation is pastoring, not strategy. Consecration crisis if Baralta claims Crown. Southernmost Awareness 0. | `arcs_09_11`, `narrative_scenario_chains`, `npc_character_analyses_existing` |
| Cardinal Magnus Klapp | Church (Temperance) | Combat Endurance (CE) 4, TS 31, archive access to originary Locks, essentialist formation (TS growth check Ob raised from 1 to 2) | `arcs_09_11`, `arcs_31_35` |
| Cardinal Osten Jarnstal | Church (Fortitude) | Independence Drift counter (0–3, never decrements). At Drift 3: Church Military deploys only against perceived threats, not political operations. Praetorian parallel. Paired foil with Brandt (two soldiers, different chains of command). | `arcs_09_11`, `npc_comprehensive_audit` |
| Princess Elske Almqvist | Crown/Altonia | Conviction: Family vs Self-Determination, Resonant Style: Evidence, Loyalty (to Valoria — distinct from Torben's Loyalty), independence arc preconditions | `narrative_scenario_chains` ARC 6, `arcs_09_11` |
| Prince Torben Almqvist | Crown/Altonia | Loyalty track (starts high; −1/season under Altonian influence if Covert Contact fails; floor at 6 if Contact maintained 3 consecutive seasons), Tutoring Demand trigger at Institutional Pressure (IP) 30 | `narrative_scenario_chains` ARC 5, `arcs_09_11` |
| Lenneth Almqvist | Crown | CE accumulation, TS growth (self-directed, can gain through research), sea-republic archive, concealment, People's Revolution endowment. "The Institutional Revivalist" — wants Crown-led Einhir revival (Catherine the Great anchor). Programme: cultural recognition → institutional reform → Thread work. **Zero mechanical expression** (audit finding #1: no Modifier, no Event Card). Lenneth↔Baralta collision = "the campaign's defining political confrontation." | `arcs_28_30`, `narrative_scenario_chains`, `npc_character_analyses_existing`, `npc_comprehensive_audit` |
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
**Roll failure category:** Costly Delay — fires eventually through repeated archive exposure. Ob 2 (essentialist formation, raised from 1) creates 34% failure chance per check, buying Church ~1–2 seasons of structural integrity per failed check. Over 3 exposures: P(at least one success) ≈ 96%.
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
**Roll failure category:** Pure Delay — fires eventually through repeated Private Collection use (each use: Spirit TN 7 Ob 1; over 5 uses, P(at least one success) ≈ 99.97%). Failure delays arc 1–3 seasons.
**Engine:** Vaynard TS 14 (Dormant) + Discovery Event
**Emergence:** Discovery Event trigger: Thread activity of sufficient intensity in proximity (practitioner at Relational scale nearby OR originary Lock deployed — per narrative_scenario_chains). Spirit TN 7 Ob 1. Success → TS jumps to 30 (Stirring), Certainty −1. Vaynard begins practice driven by TK urgency. TK +2 immediately.
**Non-Player Characters:** Vaynard (primary), Maret Uln (may facilitate or obstruct), Edeyja (if Vaynard seeks training)

### ARC-S14: Almud's Constraint — The Unresolved Question
**Engine:** Almud's ethical doubt about caste + erosion paths
**Emergence:** Almud has genuine ethical doubt about whether a Valnese kingdom should have a caste system. The doubt is intellectual, not experiential (TS 0, northern, Church-culturally integrated). He does not act because he is genuinely uncertain, not because political costs prevent him. If he were certain, he would find a way — he has managed six pressure vectors for 27 years. The constraint erodes when one or more costs is removed AND/OR the Discovery Event ruptures his governance framework: (a) Church discredited (TC −3 or more in one event) → Almud can act without Church opposition carrying weight; (b) northern Einhir nobility shifts (Revolution Influence 5+ in northern territories) → Mandate cost removed; (c) Baralta absorbs institutional cost via Hafenmark Influence in northern territories. If 218 AG truth revealed (accidental death) → Belief 2 revealed as 27 years of constraint in response to nothing → forced Belief revision.
**Non-Player Characters:** Almud (primary — Resonant Style: Consequence; show him what this costs Valoria. Historical anchor: Manuel I Komnenos — strategic patience that looks like inaction from any single vantage. TS 0; Discovery Event = rupture, not confirmation — his entire governance framework invalidated by personal perception), Baralta (can provide political cover BUT is pure RM adversary — her cover serves her Crown ambition, not RM goals), Vossen (RM Influence growth enables path (b); RM sees Almud as complicit and cowardly — from their perspective, the uncertain/cowardly distinction is irrelevant), Ehrenwall (no coup trigger from TS alone — evaluates deed-logic, not theology)

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
**Engine:** Lenneth CE accumulation → TS growth (can gain through scholarly research)
**Emergence:** CE from concealed practice via sea-republic archive and People's Revolution endowment. TS grows through self-directed work. Lenneth's programme (cultural recognition → institutional reform → Thread work) provides strategic context for her Thread development.
**Non-Player Characters:** Lenneth (primary — "The Institutional Revivalist"; Catherine the Great anchor; wants Crown-led Einhir revival, not passive scholarship; **zero mechanical expression per audit**), Torsvald (archive connection — TS 35 developed from same exposure; natural escort for Lenneth's arc; Haelgrund↔Torsvald parallel = most valuable unwritten interaction), Ehrenwall (if Lenneth exposed → dynastic implications), Baralta (Lenneth↔Baralta collision = "the campaign's defining political confrontation" — mutually exclusive programmes)

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

### ARC-S26: The Lenneth-Baralta Collision
**Engine:** Competing Crown succession programmes (irreconcilable)
**Emergence:** Lenneth wants Crown authority to revive Einhir heritage (build up — Crown as patron of cultural revival). Baralta wants Crown authority for herself under sovereign divine right (suppress — Einhir revival threatens her theological framework). Their programmes are mutually exclusive. Lenneth's revival delegitimises Baralta's claim. Baralta's reign would terminate Lenneth's programme immediately. Described in npc_character_analyses_existing as "the campaign's defining political confrontation."
**Non-Player Characters:** Lenneth (primary — Catherine the Great: strengthen institution through incorporation; zero mechanical expression), Baralta (primary — Isabella I: institutional campaign for throne; Mandate 7, Ob 1 deviation), Almud (current holder — Manuel I: manages six threats; his uncertainty means he enables both programmes), Ehrenwall (deed-logic: evaluates both candidates on competence), Vaynard (would regard Lenneth as inadequate and Baralta as the enemy — his revolutionary programme is incompatible with both), Himmensendt (consecration crisis if Baralta wins → ARC-T14)

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
**Roll failure category:** Costly Delay — retryable with 2-season delay (1 season recovery + 1 season preparation) + RS −8 cost. Endgame spiral fires only if failure compounds with no Mending during 2-season delay AND simultaneous Lock/Gap decay.
**Failure cascade (Collision C):** RS +8 + IP +2 + TC +2. If RS near 50 → Southernmost cracking clock resets. Coup Counter may reach 3 from single-season cascade.

### ARC-T05: The General Falls
**Roll failure category:** TRUE PRECLUSION — one-turn window, no retry. The only permanent roll outcome in the arc register. Conditional on player choice to commit Ehrenwall to Mass Battle.
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

### ARC-T14: The Consecration Crisis
**Engine:** Baralta claims Crown → Himmensendt consecration dilemma (ED-407, abe1b1e)
**Emergence:** If Baralta's deed-claim becomes actionable (Almqvist deed-presumption fails or weakens sufficiently), Himmensendt must decide: consecrate or refuse. The deed-monarchy's legitimation requires Church consecration. Baralta's sovereign supremacy doctrine (Henry VIII parallel) holds that the monarch rules by divine right superseding Church jurisdiction.
**Non-Player Characters:** Himmensendt (primary — sincere faith as load-bearing wall; theology compels refusal), Baralta (Crown claimant — Isabella I; deed-claim strongest on peninsula), Almud (current holder — his own consecration implicitly questioned if the question is asked), Klapp (if converted → theological crisis compounded), Ehrenwall (deed-logic: would accept Baralta; a Baralta Crown requires Löwenritter support → Ehrenwall gains leverage she doesn't currently have — ED-406)
**Provisional mechanics (ED-407 — open design question, both paths campaign-defining):**
- **Himmensendt refuses:** TC +3 (Church overreach visible). Crown Mandate −2 in territories expecting orderly succession. Baralta may claim without consecration — testing whether deed-logic alone is sufficient. Successful unconsecrated reign → Church legitimation role permanently diminished.
- **Himmensendt consecrates (under duress or calculation):** TC −5 (sovereign supremacy enacted). Church Stability −3. Church becomes subordinate institution within one reign.
**Classification:** Tertiary (requires Baralta to reach Crown-claim stage). But if fires, campaign-defining.
**[Note: arcs_09_11 line 21 says Baralta TC suppression "while Mandate stays above 5" — this conflicts with params_factions (≥ 4) and victory_architecture §7 (≥ 4). The arc file contains a consistency error; ≥ 4 is canonical per params.]**

### NPC-ARC-JAR: The Jarnstal Drift
**Engine:** Jarnstal Independence Drift counter (0–3, never decrements)
**Emergence:** Progressive independence from Confessor control. Each increment: Church Military acts more autonomously. Drift 3: Church Military deploys only against perceived threats, not political operations.
**Non-Player Characters:** Jarnstal (primary — Fortitude Cardinal, Praetorian parallel), Himmensendt (chain of command), Brandt (paired foil — two soldiers), Ehrenwall (if Löwenritter and Church Military both acting independently → military coordination collapse)
**Consequence:** Church loses political control of military arm. Heresy Investigations lose enforcement capacity. TC unaffected mechanically but Church force-projection constrained.
**Classification:** Secondary (drift accumulates passively). One-directional: no reversal condition, no branching.

---

## Cross-Non-Player Character Interaction Gaps (from npc_comprehensive_audit)

These are not separate arcs but emergence conditions that should inform existing arcs:

| Interaction | Register Arcs | Audit Priority |
|-------------|--------------|----------------|
| Haelgrund↔Torsvald: hidden TS in rejecting institutions | NPC-ARC-HAE + NPC-ARC-TOR | Highest — "most valuable unwritten NPC interaction" |
| Haelgrund↔Klapp: Thread-adjacent crises in Church | NPC-ARC-HAE + ARC-S21 | High — if both exposed, Church loses education + investigation |
| Vaynard↔Laskaris: intelligence monitoring | ARC-S01 + NPC-ARC-LAK | Medium — Varfell should monitor Altonian representative; no interaction exists |
| Prudence↔Olafsson: Cardinal portfolio friction | NPC-ARC-PRU + ARC-S06 | Medium — Economics vs Justice = Church-internal friction |
| Solberg↔Strand: outsider parallel | NPC-ARC-SOL + NPC-ARC-STR | Low — potential cross-faction scene but no mechanical interaction |

---

## Mechanical Expression Gaps (from npc_comprehensive_audit)

| Non-Player Character | Gap | Audit Priority | Register Arcs Affected |
|------|-----|----------------|----------------------|
| Lenneth | Zero mechanical expression (no Modifier, no Event Card, no measurable effects) | #1 | ARC-S18, ARC-S26 |
| Almud | No BG expression (no Event Card, no Modifier) | #2 | ARC-S14, ARC-S17 |
| Baralta | No BG Event Card | #3 | ARC-S06, ARC-T03, ARC-S24 |
| Vossen | Zero Hybrid Modifier | #4 | NPC-ARC-VOS, ARC-S22 |
| Torsvald | Abort mechanic not precisely specified (trigger/Ob/consequence) | #8 | NPC-ARC-TOR |
**Engine:** Crown elimination → Torben Loyalty transfer (PP-494)
**Emergence:** If Crown eliminated: Torben Loyalty transfers to Löwenritter as dynastic successor. Track meaning shifts (0 = aligns with anti-Löwenritter faction; 7 = full Löwenritter loyalty). Löwenritter inherits current Loyalty value.
**Non-Player Characters:** Torben, Brandt/Ehrenwall (Löwenritter inheritor), Laskaris (Altonian response)

---

## New Emergent Arcs (PP-428–442, foil analysis, mechanical interactions)

### ARC-S27: The Revelation Token Cascade
**Engine:** Varfell Revelation Tokens (PP-439) — intelligence supremacy becomes public
**Emergence:** When Varfell fully reveals a rival faction (Overwhelming Investigate or 4 Patience Counter Spy), a permanent Revelation Token is placed on the target's mat, visible to all players. The target faction knows they've been penetrated. Cascade: revealed factions may ally against Varfell, Church may open Heresy Investigation against Varfell intelligence operations, Crown invokes Royal Guard (PP-442). Two tokens on two different factions = Varfell Path A "fully revealed" condition met.
**Non-Player Characters:** Vaynard (intelligence architect), Maret Uln (if Varfell leader → different intelligence style), Strand (Crown target — flattery vulnerability makes Crown the easiest revelation), Feldhaus (Guilds target — supply chain exposure compounds), all faction leaders (publicly aware of penetration)
**Interaction:** Each token makes Varfell more politically exposed while making its information advantage more decisive. The tension between intelligence supremacy and political isolation is the arc's core.

### ARC-S28: The Thread Liaison
**Engine:** Crown Thread Liaison designation (PP-436) — Crown↔practitioner alliance made public
**Emergence:** Crown designates allied faction's Thread operations to count toward Crown co-victory RS threshold tracking. Designation is public and declarative. The act is Crown formally acknowledging Thread operations as legitimate — creating a visible Crown-practitioner alliance. Church response: TC pressure (Crown endorsing Thread work contradicts Church ontology), possible Heresy Investigation against the Liaison faction.
**Non-Player Characters:** Almud (designating a Liaison is acting on the Einhir question — a governance decision that reveals his position without requiring full Belief resolution), Himmensendt (theological objection — Crown legitimising Thread work), Vaynard (natural Liaison candidate if Crown Treaty exists), Maret Uln (if Varfell leader → RM-aligned Liaison creates Crown-RM axis)
**Interaction with ARC-S14:** Designating a Thread Liaison may be the first concrete action Almud takes on the Einhir question.

### ARC-S29: The Cardinal Schism
**Engine:** Church Stability 2 + hostile Senator action in same season (PP-430 note)
**Emergence:** Cardinal schism fires. The schisming Cardinal acts independently regardless of Cardinal Focus designation. Focus suppressed on schisming Cardinal. Which Cardinal schisms depends on game state — the Cardinal whose portfolio creates the most institutional friction with the Confessor's current direction.
**Non-Player Characters:** Jarnstal (Fortitude — if already at Drift 2–3, schism accelerates to functional autonomy; Church Military deploys without Confessor approval), Klapp (Temperance — schism + hidden TS = double crisis; AER maintenance disrupted), Prudence (Economics — schism over tithe policy = Parish Revolt accelerant; NPC-ARC-PRU fires), Olafsson (Justice — schism exposes Niflhel connection if he acts independently), Himmensendt (must manage schism while managing all other crises)
**Interaction with Collision A:** Cardinal schism at Stability 2 compounds Church Double Fracture. If Klapp + Olafsson crises + Cardinal schism fire simultaneously → Church institutional collapse.

### ARC-S30: The Counter-Narrative War
**Engine:** Three-faction TC contest — Varfell Counter-Narrative (PP-441) + Hafenmark Parliamentary Challenge (PP-431) + Church Piety Spread (PP-428) / Assert
**Emergence:** TC is no longer a two-faction contest (Church advance vs Hafenmark suppression). Varfell Counter-Narrative (Intel vs Ob = Church Mandate ÷ 2; consequentialism −1 Ob) gives Varfell TC reduction that also feeds AP — Varfell operatives documenting Church overreach can trigger Heresy Investigations against the Church itself. Hafenmark Parliamentary Challenge (Mandate vs Ob 2; PI ≥ 5: Ob −1) gives seasonal TC reduction independent of Baralta suppression. Church counters with Piety Spread (CV raising pre-seizure) and Cardinal Focus. The three-way dynamic produces TC trajectories more volatile than ARC-P01 captures.
**Non-Player Characters:** Vaynard (Counter-Narrative — consequentialist Intel vs Church), Baralta (Parliamentary Challenge — constitutional TC tool; used via Senator card, opportunity cost with other Senator actions), Himmensendt (defending on two flanks: Varfell ontological + Hafenmark jurisdictional), Prudence Cardinal (Piety Spread / Church Wealth efficiency), Almstedt (PI level affects Challenge Ob)
**Key interaction:** VTM Discretion (PP-438) lets Varfell suppress its own TK-derived TC contribution for 1 season (cooldown: 1/2 seasons). Vaynard can simultaneously reduce Church TC via Counter-Narrative while hiding his own TC contribution. The net effect: Varfell manages both sides of the TC equation.

### ARC-T15: The Forgetting Barrier
**Engine:** The Forgetting prevents non-practitioners (TS < 29) from retaining Thread knowledge
**Emergence:** Vaynard's political programme requires building coalition around the Southernmost argument. The most important argument for Einhir restoration dissolves in the minds of anyone who cannot perceive Thread reality. Vaynard must find workarounds: documentary evidence (Lenneth's archive — written accounts survive because they are documentary, not experiential), institutional memory (Klapp's archive — first-person accounts the Church suppressed), cultural memory (Revolution elder — fragmentary, partially Forgetting-impaired), or creating new practitioners (Discovery Events via originary Locks offered at TK 4).
**Non-Player Characters:** Vaynard (primary — "the Forgetting is his political prison"), Lenneth (sea-republic archive — pre-Altonian accounts ~180 AG), Klapp (Church archive — Cardinal reassignment records, Solmund accounts), Vossen (TS 25 — below gate of 29; her knowledge partially self-erasing near T13/T15), Revolution elder [EDITORIAL]
**Classification:** Tertiary — requires player identification of the Forgetting as strategic barrier and active circumvention work.

### ARC-T16: The Perceptual Prophylaxis
**Engine:** Himmensendt's pastoral responses simultaneously suppress and address Einhir concerns
**Emergence:** Himmensendt's pastoral tools (education, charity, missionaries) genuinely help southern Einhir communities while deepening the essentialist framework's penetration into exactly the communities where Thread Sensitivity survives. Every school and mission is simultaneously care and cultural overwrite. His compassion and his suppression are the same act. If someone can make Himmensendt see this through Evidence (his Resonant Style) — it is a Belief crisis. But the Forgetting prevents the evidence from persisting in his mind without TS. The only Church figures who could eventually perceive what Himmensendt cannot are Haelgrund (TS 12) and Klapp (TS 31).
**Non-Player Characters:** Himmensendt (primary — "simply, completely, sincerely wrong"; Southernmost Awareness 0), Vossen (RM communities targeted by pastoral outreach), Haelgrund (hidden TS 12 — if exposed and defects, he becomes the potential Evidence-bearer), Klapp (archive evidence + developing TS)
**Classification:** Tertiary — requires practitioner Player Character to identify the contradiction and find Evidence that survives in Himmensendt's perception.
**Interaction with ARC-S08 (Faith that Destroys):** This is the structural mechanism ARC-S08 fires against. Klapp's TS development is the crack in the prophylaxis. Haelgrund's defection (NPC-ARC-HAE) is the second crack.

### ARC-T17: The Diplomatic Outreach Arc
**Engine:** Crown Diplomatic Outreach to Schoenland (PP-437) + Solberg STABILITY-SEEKING flaw + AER track
**Emergence:** Crown has a direct IP management tool (Influence vs Ob = AER level; Virtue Ethics −1 Ob; floor 1). Combined with Solberg's unconscious stability bias. Success path: sustained engagement → AER 4+ → IP 75 threshold rises to 80; AER 5 → IP held at 50 (Altonia satisfied). Failure path: AER drops → IP baseline returns; Solberg recalled → Schoenland more dangerous. Complication: if Valoria is fragmented (3+ factions Stability ≤ 2), Ob +2 (Schoenland hedges toward Altonia).
**Non-Player Characters:** Almud (Crown diplomatic capacity), Strand (administrative execution — but Senator card shared with Treaty, cannot do both in same season), Solberg (STABILITY-SEEKING — active asset if offered credible treaty), Laskaris (IP reduction serves his protective instinct)
**Classification:** Tertiary — requires sustained Crown investment over multiple seasons. Counter-play: any faction can destabilise Valoria to make Schoenland hedge.

### ARC-S31: The Lock Distribution
**Engine:** Vaynard TK 4 → offers originary Locks (Private Collection) → simultaneous Discovery Events in multiple TS 10+ characters
**Emergence:** At TK 4, Vaynard offers the entire Private Collection including originary Locks. Each Lock triggers Spirit TN 7 Ob 1 Discovery Event in any TS 10+ character who handles it. If Locks are distributed to multiple recipients: Haelgrund (TS 12), Klapp (TS 31), Torsvald (TS 35), and Player Characters all roll simultaneously. Expected ~60% success rate per character. 3–5 Discovery Events possible in one season. Cascade: Church triple fracture if Klapp + Haelgrund + Olafsson crises coincide.
**Non-Player Characters:** Vaynard (TK 4 — distributor), Haelgrund (TS 12 — worldview shatters), Klapp (TS 31 — compounds existing CE development), Torsvald (TS 35 — Riskbreaker crisis compounds), Himmensendt (loses personnel simultaneously), Edeyja (recognises Lock nature immediately)
**Key decision:** Who receives Locks? Player choice determines which NPC arcs accelerate. The highest-impact single decision in the campaign's threadwork system.
**Interaction:** ARC-S01 (TK 4), Collision A (Church Double Fracture), NPC-ARC-HAE, ARC-S21, NPC-ARC-TOR

### ARC-S32: The Mending Trap
**Engine:** Mending = sole practitioner RS recovery (+1/+2 per success) but Coherence −1 per attempt regardless of outcome. Coherence 10→0.
**Emergence:** RS passive decline (−6 to −9/season with 2 Locks + 1 Gap). One practitioner's entire Coherence budget (~10 Mendings ≈ +10 to +20 RS) covers ~2–3 seasons of passive decline. After ~10 Mendings: Coherence 0 → Rendering Crisis → Non-Player Character if unresolved by season end. Recovery costs TS −1 permanent. The world needs Mending to survive; Mending burns out the practitioners who perform it. The campaign cannot be saved by individual heroism. It requires: multiple practitioners in rotation, Warden Cooperation (WC ≥ 2: decay halved; WC ≥ 3: RS +2/season), Community Weaving (RM Mandate ≥ 1), AND Lock/Gap resolution.
**Non-Player Characters:** Edeyja (TS 75–80, Coherence 9 — most capable but not inexhaustible), Maret Uln (TS ~50), any practitioner Player Character, Vossen (Community Weaving gated by RM Mandate)
**Structural significance:** This is the campaign's central mechanical tragedy — a resource-exhaustion arc, not a single-roll event. Individual Mending successes/failures matter tactically (success = RS +1, failure = RS −2) but the trap is structural: even perfect rolls cannot sustain RS indefinitely because Coherence is finite. The Einhir practitioners reached this same position 245 years ago.
**Interaction:** ARC-P02 (RS budget), ARC-S16/S17/S18 (Coherence Zero — burnout destination), ARC-S25 (Warden Cooperation — necessary), ARC-S10 (Community Weaving access), ARC-S15 (Ceiral Ritual — only bulk RS source)

### ARC-S33: The Lattice of Enemies
**Engine:** Cross-faction collective Thread operations gated by Belief compatibility (threadwork v2.5 §2.5)
**Emergence:** Endgame RS recovery at RS Critical (19–1) requires practitioner cooperation across faction lines. Collective operations require Belief checks: directly opposing Beliefs → Spirit TN 7 Ob 1 pre-Leap (failure = helper drops, ~40% failure rate); tangential conflicts → helper dice don't chain on 10. The practitioners who must cooperate to save the world may be mechanically unable to cooperate because their factions' Beliefs conflict.
**Key Belief interactions:** Vaynard (consequentialist) vs Edeyja (deontological) = tangential conflict → non-chaining. Crown vs Varfell practitioners = directly opposing → Spirit check. Maret Uln (RM sympathy) vs Church-aligned = directly opposing. Player Character practitioners with harmonised Beliefs = full dice — the campaign rewards Player Character cooperation and penalises Player Character–Non-Player Character cross-faction cooperation.
**Non-Player Characters:** Edeyja (best collective partner — substrate-aligned Beliefs compatible with pure Mending intent), Vaynard (diminished partner despite high TS — non-chaining dice), Maret Uln (RM friction), Almud (governance Beliefs tangentially conflict with substrate Beliefs)
**Structural consequence:** Endgame is not "can practitioners cooperate?" but "which practitioners can cooperate?" Belief compatibility determines viable alliances for RS recovery.
**Interaction:** ARC-S16/S17/S18, ARC-P02, Collision B (Almud's Beliefs affect viability), ARC-S32 (Mending Trap — collective Mending is more efficient but Belief-gated)

### ARC-T18: The Overweaving Cascade
**Engine:** Multiple practitioners Weaving same configuration → stacked over-actualisation (PP-209) → catastrophic brittleness
**Emergence:** Two practitioners independently Weave same configuration in separate contact windows: +2 Ob total (stacked over-actualisation). Shattering consequence escalates one severity tier (Shifting Object forms as if 1 season old → accelerated Gap deterioration). In mass battle (RS ×3 multiplier, PP-192): stacked over-actualisation shattering produces RS −6 to −12 from a single collapsed configuration.
**Non-Player Characters:** Any two practitioners operating in same theatre without Collective Diagnosis coordination
**Key mechanic:** During contact, practitioners CANNOT communicate (communication requires rendering). Collective Diagnosis pre-Leap is the only coordination mechanism. Separate Leaps = no knowledge of what the other has Woven → stacking risk.
**Classification:** Tertiary — requires two practitioners independently targeting same configuration. But when it fires, RS consequences compound rapidly.
**Interaction:** ARC-S02 (Brittle Peace — over-actualisation), ARC-S04 (Rendering Debt — ×3 in mass battle)

### ARC-T19: The Governance Pause
**Engine:** Almud Discovery Event attempt (success OR failure) → 1-season Crown Non-Player Character AI pause
**Emergence:** Whether the Discovery Event succeeds or fails, Almud enters 1-season self-examination. Crown Non-Player Character AI takes no offensive Domain Actions. The ATTEMPT changes him. During this season: TC advances unopposed (no Crown Suppress), IP advances (no Crown diplomatic action), Coup Counter may increment (Crown inaction at TC ≥ 40). All factions have a 1-season window to act without Crown opposition.
**Non-Player Characters:** Almud (paused), Ehrenwall/Brandt (Coup Counter — Crown inaction counts), Baralta (Parliamentary Challenge without resistance), Vaynard (Counter-Narrative without interference), Himmensendt (Assert without Suppress)
**Classification:** Tertiary — requires Almud Discovery Event attempt (itself requiring player action to expose him). But fires on BOTH success and failure.

### ARC-S34: The Edeyja Burnout
**Engine:** Edeyja Coherence 9 → repeated Mending at Critical RS → Coherence crisis
**Emergence:** If Ceiral Ritual fails (ARC-T04 failure branch) or RS enters Critical, Edeyja becomes sole high-level Mender (TS 75–80). ~8 Mendings before Coherence 2 (Fractured). ~10 before Coherence 0 (Rendering Crisis → Non-Player Character if unresolved). If she reaches Coherence 0: Wardens lose principal practitioner. Warden Cooperation (WC) track may degrade. No living practitioner can perform Locked Zone border Mending (requires TS 70+ AND Einhir framework). Southernmost becomes mechanically unsalvageable.
**Non-Player Characters:** Edeyja (primary — finite Coherence despite being the moral anchor), any practitioner Player Characters (Mending rotation extends her timeline), Maret Uln (TS ~50 — can Mend standard Gaps but not Locked Zone borders)
**Structural significance:** Hidden fail state — cumulative resource exhaustion, not a single roll. Each Mending is a Costly Delay decision (spend Coherence now for RS recovery, or preserve for future Mendings). The fail state is invisible until Edeyja reaches Coherence 4–5 and the budget becomes visibly finite.
**Interaction:** ARC-S32 (Mending Trap), ARC-S25 (WC degrades if Edeyja incapacitated), ARC-S15 (Ceiral Ritual becomes only option if Mending unavailable)

### COLLISION F: The Succession Triangle
**Trigger:** Almqvist deed-presumption weakens (Coup Counter ≥ 2, or Almud Discovery Event, or Torben loss) while both Lenneth and Baralta programmes are active
**Effect:** Three-way succession contest fires. Lenneth's counter-claim: "the family that earned the throne should keep it — and I will make the Crown worthy of keeping." Baralta's claim: deed-logic's obvious choice (strongest governance record, Mandate 7, Ob 1 deviation). Ehrenwall's calculus: competence within the system (Baralta) vs competence to strengthen the system (Lenneth) vs competence to replace the system (Vaynard — excluded by deed-logic's limit). Consecration crisis (ARC-T14) fires if Baralta wins. Lenneth's zero mechanical expression means her claim has narrative weight but no measurable game-state effects — audit gap #1.
**Non-Player Characters:** Almud (current holder — his uncertainty enables both programmes), Lenneth (cognatic succession candidate — zero mechanical expression), Baralta (institutional campaign — Isabella I), Ehrenwall (deed-logic enforcement — evaluates both), Vaynard (excluded by deed-logic but competence is real), Himmensendt (consecration authority)
**Source:** ruler_diamond_extended_foils §Almud-Lenneth-Baralta Succession Triangle

### COLLISION G: The Einhir Triangle
**Trigger:** Lenneth's revival programme, Baralta's suppression, and Vaynard's revolutionary restoration are all active simultaneously
**Effect:** Three positions on the Einhir question — no two can ally without excluding the third. Lenneth + Vaynard agree on diagnosis but not treatment (build up vs tear down). Lenneth + Baralta share institutional orientation but oppose on Einhir entirely. Vaynard + Baralta agree on nothing. The triangle has no stable resolution — whichever position wins, the other two lose. Player characters positioned within this triangle must choose which axis to support, and the choice excludes one ally permanently.
**Non-Player Characters:** Lenneth (institutional revival — Catherine the Great), Baralta (sovereign suppression — Henry VIII), Vaynard (revolutionary restoration — Reinhard von Lohengramm), Almud (uncertainty enables all three), Himmensendt (pastoral prophylaxis — his compassion IS the suppression Vaynard fights and Lenneth wants to replace)
**Source:** ruler_diamond_extended_foils §Lenneth-Baralta-Vaynard Einhir Triangle

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
  ├→ ARC-S30 (Counter-Narrative War — 3-faction TC contest)
  │    └→ PP-438 VTM Discretion (Varfell hides own TC contribution)
  ├→ ARC-T01 (Tied Vote — TC +1 spike)
  ├→ ARC-T10 (TC 75+ Phase Transition — seizure mode)
  ├→ ARC-S21 (Klapp Threshold → TC pause)
  │    └→ COLLISION A (Church Double Fracture)
  │         └→ ARC-S29 (Cardinal Schism — compounds at Stability 2)
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
  NPC-ARC-JAR (Jarnstal Drift — passive accumulation)
  ARC-S11 (Headless Network)
  ARC-S12 (Favour Gate)
  ARC-S23 (Elske Independence)
  ARC-S26 (Lenneth-Baralta Collision — competing succession)
    └→ ARC-T14 (Consecration Crisis — ED-407)
    └→ COLLISION F (Succession Triangle)
  ARC-S27 (Revelation Token Cascade — Varfell intelligence goes public)
  ARC-S28 (Thread Liaison — Crown↔practitioner alliance)
  ARC-S29 (Cardinal Schism — Church Stability 2)
  ARC-S30 (Counter-Narrative War — 3-faction TC)
  ARC-T07 (Dissolution)
  ARC-T09 (Forgetting Road)
  ARC-T11 (IP 75+ Vanguard)
  ARC-T12 (BG Convictions)
  ARC-T13 (Torben After Crown Elimination)
  ARC-T15 (Forgetting Barrier — Vaynard's political prison)
  ARC-T16 (Perceptual Prophylaxis — Himmensendt's compassion = suppression)
  ARC-T17 (Diplomatic Outreach — Crown IP management via Schoenland)

COLLISION SCENARIOS
  A: Church Double Fracture (S21 + S06)
  B: Practitioner King (S17 + S23 + S07)
  C: Tutoring + Southernmost (S07 + T04 failure)
  D: Niflhel Weaponises (S11 + S06 + assassination)
  E: Einhir Elder + Baralta Claim (S19 + elder + Klapp)
  F: Succession Triangle (S26 + P03 + Ehrenwall calculus)
  G: Einhir Triangle (Lenneth revival vs Baralta suppression vs Vaynard revolution)
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
| ARC-S23–S30 | Not simulated | Elske Independence, Baralta Succession, Warden Cooperation, Lenneth-Baralta Collision, Revelation Token Cascade, Thread Liaison, Cardinal Schism, Counter-Narrative War |
| NPC-ARC-* | **Not simulated** | All NPC-derived arcs from roster (including NPC-ARC-JAR Jarnstal Drift) |
| ARC-T01–T17 | Mixed | T01–T09 partially via CP14; T10–T17 not simulated |
| Collisions A–G | **Not simulated** | All collision scenarios |

---

## Open Items

| ID | Item | Status |
|----|------|--------|
| GAP-ARC-01 | Arc S11 — Niflhel Quiet deployment RS/Thread Tension cause | Pending editorial clarification |
| GAP-ARC-02 | IP generation formula — no canonical base advancement rate | bg_v05 gap; narrative_scenario_chains uses +2/season working assumption |
| GAP-ARC-03 | Jarnstal — Independence Drift counter characterized (Fortitude Cardinal, 0–3) but arc structure one-directional with no branching; no reversal condition | Audit score 27/40, lowest arc interest (2/5) |
| GAP-ARC-04 | Baralta NPC personal stats — conflicting values between cp14 arcs and narrative_scenario_chains | May represent different evidence levels |
| ED-NEW-01 | Tier assignments (principal/secondary/tertiary) | Provisional — user review required |
| ED-NEW-02 | Revolution elder — not canonised as named character | Required for Collision E |
| ED-NEW-03 | Elske TS development — not established | Affects Collision B branching |
| ED-NEW-04 | 218 AG resolution — narrative_scenario_chains presents accidental death as design intent; E-01 flagged as unresolved elsewhere | Reconciliation needed |
| ED-358 | Full roster identities, motivations, stat blocks | Provisional — user review pending |
| E-01 | Perpetrator of 218 AG assassination | Unresolved (but see ED-NEW-04) |
| GAP-ARC-05 | ARC-T03 Excommunication — Church Mandate pool (5d10) cannot reach Ob 7 (Baralta personal Mandate). Non-functional at game-start stats. Fires only after political erosion reduces Baralta Mandate. Likely intentional: excommunicating the peninsula's most legitimate secular ruler SHOULD be mechanically near-impossible at baseline. At Mandate 4: P(success) ≈ 32%. At Mandate 3: P ≈ 66%. Retryable each season (no unique resource consumed). | Gated mechanic — intentional design per delay evaluation |
| SIM-BRANCH-05 | Edeyja burnout = hidden fail state. Southernmost endgame condition permanently unachievable if Edeyja Coherence 0. | → ARC-S34 |

### Caste Gradient Note (701eacf)

Olafsson's Heresy Investigations disproportionately target southern Einhir communities (higher TS, more Thread-adjacent activity). The enforcement pattern is ethnic even if the doctrine is theological. Affects ARC-S03 (Tribunal), NPC-ARC-VOS (Vossen Exposure), ARC-S06 (Duchess Holds the Line). Vaynard's TS is environmental (southern baseline), not artefact-derived — his Thread awareness is what southern Einhir people are when the Church has not completely suppressed their capacity.

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

### v2 → v3 (review against recent commits)

| Error | v2 Text | v3 Correction | Source |
|-------|---------|---------------|--------|
| Klapp cardinal title | "Church (Education)" | "Church (Temperance)" | npc_comprehensive_audit, params_board_game §Cardinal Focus |
| Almud characterization | "TS potential (28→30), RM sympathy" | TS 0, governance pragmatism + ethical doubt, Manuel I Komnenos, Discovery Event = rupture | ED-364 (5200ab8), npc_character_analyses_existing |
| Baralta characterization | Faction correct but missing Crown ambition | Active Crown ambition, pure RM adversary, Isabella I, deed-claim strongest | npc_character_analyses_existing (701eacf) |
| Lenneth characterization | "passive researcher" framing | "Institutional Revivalist", Catherine the Great, zero mechanical expression, Lenneth↔Baralta = defining confrontation | npc_character_analyses_existing (701eacf), npc_comprehensive_audit |
| Vaynard TS origin | Not specified | Southern Einhir environmental exposure, Reinhard von Lohengramm, Forgetting as political prison | npc_character_analyses_existing (701eacf) |
| Ehrenwall framing | Coup Counter correct but no deed-logic context | Deed-logic enforcement mechanism, would accept Baralta | npc_character_analyses_existing (5200ab8) |
| Jarnstal | "GAP: minimal mechanical data" | Fortitude Cardinal, Drift counter 0–3, Independence at 3, Praetorian parallel | npc_comprehensive_audit (bbf9849) |
| Himmensendt | Basic characterization | "Most dangerous person — doesn't know it", consecration crisis, Southernmost Awareness 0 | npc_character_analyses_existing (701eacf) |
| Missing: ARC-S26 | Not present | Lenneth-Baralta Collision — competing Crown succession programmes | npc_character_analyses_existing |
| Missing: ARC-T14 | Not present | Consecration Crisis — Baralta claims Crown → Himmensendt dilemma | npc_character_analyses_existing |
| Missing: NPC-ARC-JAR | Not present | Jarnstal Independence Drift — Fortitude Cardinal, counter 0–3 | npc_comprehensive_audit |
| Missing: cross-NPC gaps | Not present | 5 unwritten NPC interactions from audit | npc_comprehensive_audit |
| Missing: mechanical gaps | Not present | 5 NPC mechanical expression gaps from audit | npc_comprehensive_audit |
| Missing: caste gradient | Not present | Heresy Investigations disproportionately target southern Einhir (higher TS) — ethnic enforcement pattern | npc_roster_caste_annotations (701eacf) |

### v3 → v4 (abe1b1e review + new emergent arcs)

| Change | Detail | Source |
|--------|--------|--------|
| ARC-T14 updated | ED-407 provisional mechanics added: refuse (TC +3, Mandate −2) vs consecrate (TC −5, Stability −3). Ehrenwall-Baralta leverage (ED-406). | abe1b1e |
| Baralta TC suppression discrepancy | arcs_09_11 line 21 says ">5" — flagged as consistency error vs params ≥4 | abe1b1e vs params_factions |
| ARC-S27 added | Revelation Token Cascade — Varfell intelligence goes public (PP-439) | faction_resolutions |
| ARC-S28 added | Thread Liaison — Crown designates practitioner ally publicly (PP-436) | faction_resolutions |
| ARC-S29 added | Cardinal Schism — Church Stability 2 + hostile Senator (PP-430) | faction_resolutions |
| ARC-S30 added | Counter-Narrative War — 3-faction TC contest (PP-441/431/428) | faction_resolutions |
| ARC-T15 added | Forgetting Barrier — Vaynard's political prison | npc_character_analyses |
| ARC-T16 added | Perceptual Prophylaxis — Himmensendt's compassion = suppression | npc_character_analyses + foils |
| ARC-T17 added | Diplomatic Outreach — Crown IP management via Schoenland (PP-437) | faction_resolutions |
| COLLISION F added | Succession Triangle — Almud/Lenneth/Baralta | ruler_diamond_extended_foils |
| COLLISION G added | Einhir Triangle — Lenneth/Baralta/Vaynard (no stable resolution) | ruler_diamond_extended_foils |
