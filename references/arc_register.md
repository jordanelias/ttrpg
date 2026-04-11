# Arc Register

> **Status:** WORKING DRAFT
> **[EDITORIAL: ED-NEW — Tier assignments and NPC arc classifications are provisional pending user review]**
> **Sources fetched:** `designs/gm_ref_cp14/arcs/*`, `gm_ref/arcs_*`, `designs/npcs/npc_roster.md`, `references/params_factions.md`, `designs/ttrpg/valoria_narrative_scenario_chains.md`

---

## Classification Criteria

| Tier | Definition |
|------|-----------|
| Principal | Near-inevitable from running mechanical engines (clocks, seasonal accounting, Non-Player Character faction tendency). Emerges unless players actively prevent it. Campaign-defining. |
| Secondary | Emerges from specific Non-Player Character tracks, subsystem engagement, or player interaction with particular world elements. High probability given typical play patterns but not automatic. |
| Tertiary | Narrow prerequisites, single-roll pivots, or specific player choices. Possible but not guaranteed in any given campaign. |

---

## Named Non-Player Character Index

### Legacy Non-Player Characters (pre-roster, referenced across arc files)

| Non-Player Character | Faction | Key Tracks | Source |
|------|---------|------------|--------|
| King Almud | Crown | Beliefs (3), TS (potential 28→30), Discovery Event | `stage6_factions`, `narrative_scenario_chains` |
| Duchess Inge Baralta | Crown (independent) | Mandate (7), Reach (5), Theocracy Counter (TC) suppression (−1/season while Mandate ≥ 5), Solmund claim | `params_factions`, `arcs_09_11` |
| Grandmaster Sigrid Ehrenwall | Löwenritter | Coup Counter (3-threshold), Health/Wound track, Lions' Table | `params_factions`, `arcs_20_23` |
| Cardinal Arnlod Olafsson | Church (Justice) | Niflhel connection (hidden), Church Intel operations | `narrative_scenario_chains`, `arcs_09_11` |
| Duke Magnus Vaynard | Varfell | Thread Investigation Track (TK, 0–5), Thread Sensitivity (TS, starts 14 Dormant), Private Collection, Belief 3 (succession leverage) | `params_factions`, `arcs_01_04`, `arcs_24_27` |
| Confessor Arne Himlensendt | Church (head) | Resonant Style (Evidence), Stability checks under institutional crisis | `arcs_09_11`, `narrative_scenario_chains` |
| Cardinal Magnus Klapp | Church (Education) | Combat Endurance (CE) 4, TS 31, archive access to originary Locks | `arcs_09_11`, `arcs_31_35` |
| Cardinal Osten Jarnstal | Church | [minimal mechanical data — editorial gap] | `arcs_09_11` |
| Princess Elske Almqvist | Crown/Altonia | Loyalty track (starts high, degrades under Altonian influence), succession candidate, potential TS development [EDITORIAL — not canonised] | `arcs_09_11`, `narrative_scenario_chains` |
| Prince Torben Almqvist | Crown/Altonia | Loyalty track (starts high, −1/season under Altonian influence), Tutoring Demand trigger at Institutional Pressure (IP) 30 | `arcs_09_11`, `arcs_20_23` |
| Lenneth Almqvist | Crown | Combat Endurance (CE) accumulation, TS growth (self-directed), archive holdings, concealment | `arcs_28_30` |
| Solvind Brak | Niflhel (former?) | Testimony value for Olafsson-Niflhel exposure | `arcs_09_11` |
| Revolution elder | Restoration Movement (RM) | Fragmentary inner-tradition knowledge, TS uncertain, Forgetting-impaired | `narrative_scenario_chains` [EDITORIAL — not canonised as named character] |

### Roster Non-Player Characters (designs/npcs/npc_roster.md — ED-358)

| # | Non-Player Character | Faction | Compromise | Behavioral Artificial Intelligence Flaw | Key Tracks |
|---|------|---------|------------|------|------------|
| 1 | Edeyja | Wardens | None | None | TS 75–80, Coherence 9 |
| 2 | Maret Uln | Varfell | Dual loyalty (RM sympathy) | CONFLICTED (hesitates vs RM) | TS ~50, Belief checks (Spirit Target Number (TN) 7 Obstacle (Ob) 1) |
| 3 | Maret Vossen | RM | Visibility = Church target | IDEALIST (spreads Presence thin) | TS 25, Attention Pool (AP) accumulation, Popular Will |
| 4 | Sæmund Haelgrund | Church (Inquisitor) | Evidence contradicts doctrine | PROCEDURALIST (+1 season investigations) | TS 12 (hidden), Heresy Investigation |
| 5 | Sigrid Torsvald | Löwenritter (Riskbreaker) | TS 35 in anti-Thread org | RISK-AVERSE on Thread collateral | TS 35, Deniability Debt, Lenneth connection |
| 6 | Halvar Brandt | Löwenritter | Border war trauma | EXTERNAL THREAT FIXATED | Ehrenwall succession candidate, Coup Counter threshold 2 |
| 7 | Annika Feldhaus | Guilds | Thread-touched supply chain | PROFIT-MAXIMISING | Guilds Wealth/Mandate, Virke connection |
| 8 | Peder Almstedt | Ministry | Preserves system over justice | CONSERVATIVE (blocks reform) | IP recovery +1, reform Ob +1 |
| 9 | Gerik Strand | Crown (Lord Steward) | Conditional position | OVERPERFORMER (can't delegate) | Treasury +1D, flattery vulnerability (−1 Ob) |
| 10 | Dalla Virke | Niflhel (Virke syndicate) | Thread-touched supply chain | NETWORK PROTECTOR | Trust network, family recall risk |
| 11 | Doux Alexios Laskaris | Altonia | Genuine attachment to Elske | PROTECTIVE | IP modifier (−1/season), flip trigger (Elske Loyalty ≤ 2 → IP +3) |
| 12 | Rikard Solberg | Schoenland | Wants to go home | STABILITY-SEEKING | Arms supply modifier, intelligence downplay |
| 13 | [Name Pending] | Church (Prudence) | Tithe maximiser | OPTIMISER | Church Wealth +1/season, Mandate erosion in squeezed territories |

---

## Principal Arcs

These emerge from core mechanical engines running. Near-inevitable unless players actively intervene.

### ARC-01: The Coup That Wasn't Supposed to Happen
**Engine:** IP clock → Löwenritter Coup Counter
**Emergence:** Players focus on Church opposition and TC reduction. Crown management neglected. IP accumulates. Ehrenwall's Coup Counter increments from IP threshold + unaddressed Crown threats. Counter reaches 3 → Martial Law.
**Non-Player Characters:** Ehrenwall (trigger), Almud (target), Brandt (succession), Torsvald (Riskbreaker exposure), Strand (administrative collapse if coup succeeds), Almstedt (Ministry disruption)
**Clock interaction:** IP ≥ 30 fires Tutoring Demand (Arc 20) and Ehrenwall's Count (Arc 34) simultaneously. Rendering Stability (RS) ≤ 10 adds +1 to coup trigger check pools.

### ARC-03: The Accumulating Substrate Damage
**Engine:** RS clock — seasonal decay from unresolved Thread activity
**Emergence:** Lock drift, persistent Gaps, and seasonal RS decay accumulate without coordinated response. RS degradation is constant. No player action required for this to worsen — only inaction.
**Non-Player Characters:** Edeyja (the only person who fully understands the problem), Maret Uln (Thread operations contribute to decay), any practitioner Player Character
**Clock interaction:** RS ≤ 60 → Arc 08 (Temporal Window). RS ≤ 55 → cross-clock fires: TC +1/season, IP +1/season. RS ≤ 50 → Southernmost cracking clock resets. RS ≤ 10 → coup trigger pool bonus.

### ARC-04: The Axis 9 Resolution
**Engine:** Axis 9 (Thread ontology: suppress vs accept) — forced to resolution by practitioner visibility + Vaynard TK + RM cultural pressure
**Emergence:** Practitioners operate visibly. Vaynard TK climbing. Revolution sheltering sensitives. The question of whether Thread reality is acknowledged publicly becomes unavoidable.
**Non-Player Characters:** Vaynard (TK track), Almud (potential Discovery Event → practitioner king), Himlensendt (doctrinal authority), Klapp (hidden TS), Haelgrund (hidden TS), Vossen (RM public face), Edeyja (substrate authority)
**Endgame significance:** If Almud develops TS 30+ and publicly acknowledges Thread practice → TC +3 but RS improves. This is the scenario where the campaign's central dramatic question answers itself.

### ARC-13: The Dominance Event
**Engine:** TC clock — Church Mandate ≥ 5 → TC +1/season automatic
**Emergence:** TC accumulates. Baralta's suppression (−1/season while her Mandate ≥ 5) is the only brake. If Baralta's Mandate drops below 5, net TC = +1/season. TC 60 → territorial seizure procedure.
**Non-Player Characters:** Baralta (suppression), Himlensendt (Church head), Olafsson (covert acceleration via Niflhel), Klapp (TC generation pauses if he converts), Prudence Cardinal (tithe friction erodes Church grassroots → CV erosion complicates TC)
**Clock interaction:** TC 42 → Arc 31 (Quaestio). TC 60 → seizure. TC +2 if Almud's TS exposed. TC −1 if Himlensendt deviates from doctrine.

### ARC-16: The World Without Direction
**Engine:** Non-Player Character faction tendency (artificial intelligence) — runs automatically at seasonal accounting when players focus elsewhere
**Emergence:** Players focused elsewhere ≥ 2 seasons. Game Master runs Non-Player Character faction rolls (faction stat as d10s, TN 7, Ob = opposing stat ÷ 2 round up). Factions drift toward institutional tendencies: Church expands Piety and accumulates civil authority; Varfell maximises information advantage; Crown consolidates.
**Non-Player Characters:** All Non-Player Character faction heads act via institutional tendency. Laskaris (IP sandbagging − 1/season), Solberg (Schoenland arms supply conservative), Almstedt (IP recovery +1/season), Prudence Cardinal (Church Wealth +1/season but Mandate erosion)
**Clock interaction:** All clocks drift per tendency. The world does not stand still.

### ARC-19: The Accounting Sequence
**Engine:** Seasonal accounting strict order — Domain Echo outcomes → Stability checks → clock drift → floors/ceilings → Character Point (CP) award
**Emergence:** Two+ factions under Stability pressure in the same season. Order-of-operations effects create interaction patterns. Anti-death-spiral floor activates at Stability 2 (Ob 4 regardless of actual pressure). 1–2 season intervention window.
**Non-Player Characters:** All faction Non-Player Characters — accounting is universal. Almstedt (PI recovery +1), Strand (Crown admin +1D), Prudence Cardinal (Church Wealth +1 but Mandate −0.5 fractional)
**Clock interaction:** Cross-cuts all clocks. This is the engine that makes the other engines interact.

### ARC-24: The Faction That Breaks
**Engine:** Stability checks — any faction under sustained pressure
**Emergence:** Multiple concurrent threats across 2–3 seasons. Stability checks escalating: Ob 3 → 4 → 5. Any faction reaching Stability 0 collapses. Anti-spiral floor at Stability 2 (Ob 4 regardless of pressure) gives 1–2 season intervention window.
**Non-Player Characters:** The leader of whichever faction breaks. Potential candidates: Church (if Klapp + Olafsson crises coincide → Stability −3), Crown (if IP + TC + Coup Counter cascade), Revolution (if Rawlsian framework contradictions accumulate), Varfell (if Vaynard eliminated → Maret Uln succession, VTM reset)
**Clock interaction:** Any clock crossing a threshold adds Stability pressure. Multiple clock crossings in the same season = cascade risk.

---

## Secondary Arcs

These emerge from specific Non-Player Character tracks or subsystem engagement. High probability given typical play but require interaction with particular world elements.

### ARC-02: The Vaynard Revelation Cascade
**Engine:** Vaynard TK track (0–5)
**Emergence:** Practitioner Player Character forms sustained relationship with Vaynard. Private Collection deployed. TK advances toward Discovery Event.
**Non-Player Characters:** Vaynard (TK), Maret Uln (intelligence operative, dual loyalty), Olafsson (if Vaynard exposed → Church investigation)
**Thresholds:** TK 3+ → TC secondary effect. TK 4 → Arc 32 (Confession). TK 5 → full Discovery Event cascade.

### ARC-05: The Brittle Peace
**Engine:** Threadweaving over-actualisation brittleness (threadwork v2.5 §2.3, §9.8)
**Emergence:** Practitioner Weaves a diplomatic agreement at Relational scale. Over-actualisation makes the agreement mechanically fragile. Consequence genre fires on fracture.
**Non-Player Characters:** Any practitioner Player Character, affected faction leaders, Edeyja (if consulted on Relational work)

### ARC-06: The Tribunal and the Temporal Shimmer
**Engine:** Church Inquisitorial proceedings + Debate redesign v1
**Emergence:** Church opens proceeding against practitioner Player Character or Varfell for Thread-related heresy. Evidence genre produces temporal co-movement or Pulling as courtroom consequence.
**Non-Player Characters:** Haelgrund (PROCEDURALIST — investigation +1 season but Overwhelming), Himlensendt (presides), Olafsson (Justice portfolio), Klapp (if his TS is exposed during proceedings → internal crisis)

### ARC-07: The Rendering Debt
**Engine:** Mass Battle per-turn Threadweaving + Coherence drain curve
**Emergence:** War begins. Practitioner Player Character operates as faction battlefield Thread asset every turn. Coherence drain accelerates. Rendering Crisis at Coherence 0.
**Non-Player Characters:** Ehrenwall (if war involves Löwenritter), Brandt (if Ehrenwall falls → border redirection), any practitioner Player Character, Edeyja (if Coherence crisis threatens Askeheim)

### ARC-08: The Temporal Window
**Engine:** RS ≤ 60 threshold
**Emergence:** RS deteriorates below 60. Past-Oriented Pulling becomes mechanically accessible. Multiple factions learn this. Einhir Ritual Framework (§9.15) relevant.
**Non-Player Characters:** Any practitioner, Edeyja (Einhir knowledge), Klapp (archive records of past Pulling), Vossen (RM cultural memory)

### ARC-09: The Duchess Holds the Line
**Engine:** Baralta Non-Player Character track — TC suppression + Olafsson evidence
**Emergence:** Baralta Mandate ≥ 5 (suppression active). Players supply corroborating evidence of Olafsson-Niflhel connection. Baralta launches Domain Action vs Church Stability Ob 3 (pool: Mandate 7 + Reach 5 + evidence bonus).
**Non-Player Characters:** Baralta (suppression), Olafsson (target), Solvind Brak (testimony), Himlensendt (if Olafsson exposed → Himlensendt must act)

### ARC-10: The Princess in Altonian Territory
**Engine:** IP 30 threshold → Altonian education demand
**Emergence:** IP reaches 30. Altonia issues formal demand for Torben. Almud faces Belief 1 vs Belief 3 collision. Torben Loyalty degrades −1/season under Altonian influence.
**Non-Player Characters:** Torben (Loyalty track), Almud (Beliefs), Elske (dynastic link), Laskaris (PROTECTIVE — delays demands, but flips if Elske Loyalty ≤ 2), Ehrenwall (Coup Counter +1 if Torben alignment changes)

### ARC-11: The Faith that Destroys What It Defends
**Engine:** Klapp CE/TS tracks
**Emergence:** Cardinal Klapp (CE 4, TS 31) encounters Thread-significant object. TS growth check: Spirit TN 7 Ob 2 (essentialist formation raises Ob). Success → crisis of faith. Head of Church education perceives what the Church suppresses.
**Non-Player Characters:** Klapp (primary), Himlensendt (must respond), Olafsson (if simultaneous exposure → Collision A: Church Double Fracture), Haelgrund (parallel hidden TS — if both exposed simultaneously, Church loses its inquisitorial AND educational leadership)

### ARC-12: The Framework Trap
**Engine:** Ethical framework Ob modifiers (Crown Virtue Ethics +1 Ob for covert; Church uses Niflhel covert channels)
**Emergence:** Church advances TC through covert Domain Actions via Niflhel channels. Crown ethical framework penalises covert response (+1 Ob). Crown succeeds openly but fails to address covert accumulation.
**Non-Player Characters:** Olafsson (Niflhel connection), Almud (Crown Virtue Ethics), Strand (administrative response), Virke (if Niflhel channel exposed → supply chain cascade)

### ARC-14: The Revolution Eats Itself
**Engine:** Revolution ethical framework (Rawlsian Social Contract) + structural contradiction (no Mandate)
**Emergence:** Revolution has Influence, Stability, Intel but no Mandate. Community Weaving requires Mandate ≥ 1. RS declining — Weaving needed. Rawlsian framework penalises power concentration (+1 Ob). Players must build to Mandate 1 while navigating framework constraints.
**Non-Player Characters:** Vossen (IDEALIST — spreads thin), Maret Uln (if Vaynard eliminated → Varfell aligns with RM, relieving structural pressure), Revolution elder [EDITORIAL — not canonised]

### ARC-15: The Headless Network
**Engine:** Niflhel four-arm structure — decentralised control
**Emergence:** Players identify Niflhel as necessary (intelligence, covert capacity, port access). Four arms (Quiet, Reckoners, Burned, Port) each require separate influence operation (Intel vs Ob 3 per arm). Uncontrolled arms act independently.
**Non-Player Characters:** Virke (Virke syndicate — trust network), Olafsson (Niflhel-Church connection), Solvind Brak (potential evidence source)
**[GAP-ARC-01]:** Quiet deployment RS/Thread Tension accumulation cause pending editorial clarification.

### ARC-17: The Favour Gate
**Engine:** Guild Favour threshold (≥ 5) for Economic Leverage
**Emergence:** Guild Favour ≥ 5 required for Economic Leverage unique action. Default Favour 3. Seasonal cap ±2. Minimum 1 season to reach threshold.
**Non-Player Characters:** Feldhaus (PROFIT-MAXIMISING — Guilds Wealth over Mandate), Virke (supply chain connection)

### ARC-26: The Duke Awakens
**Engine:** Vaynard TS track + Discovery Event
**Emergence:** Vaynard TS 14 (Dormant). Discovery Event trigger: Thread activity of sufficient intensity in proximity. Spirit TN 7 Ob 1. Success → TS jumps, Vaynard begins practice driven by TK urgency.
**Non-Player Characters:** Vaynard (primary), Maret Uln (intelligence operative, may facilitate or obstruct), Edeyja (if Vaynard seeks training)

### ARC-28: Vaynard — The Reckoner Who Saw the Sum
**Engine:** Vaynard TS 30 + Coherence 0 endgame
**Emergence:** Discovery Event success → TS 30 → practice at scale driven by TK urgency. Coherence 0 scenario.
**Non-Player Characters:** Vaynard, Edeyja (substrate authority), Maret Uln

### ARC-29: Almud — The King at the Limit of Order
**Engine:** Almud TS 28→30 + First Leap + Coherence 0
**Emergence:** Discovery Event (TS 28 → 30) → First Leap → practice under crisis pressure. Coherence 0 endgame arc.
**Non-Player Characters:** Almud, Ehrenwall (no coup trigger from TS alone — she cares about sovereignty, not theology), Himlensendt (Church response if known), Elske (if installed as independent heir → Almud retires to practitioner path?)

### ARC-30: Lenneth — What She Finally Understood
**Engine:** Lenneth CE accumulation → TS growth → self-directed practice
**Emergence:** CE accumulation from concealed practice. TS grows through self-directed work. Lenneth practices in concealment using archive holdings.
**Non-Player Characters:** Lenneth (primary), Torsvald (Lenneth archive connection — Riskbreaker assigned to catalogue archive; her TS 35 developed from this exposure), Ehrenwall (if Lenneth exposed → dynastic implications)

### ARC-31: The Quaestio of Baralta
**Engine:** TC 42 threshold → Grand Debate + multi-system convergence
**Emergence:** TC reaches 42 (Church Mandate ≥ 5 → +1/season × seasons). Grand Debate fires. Löwenritter Coup Counter, Niflhel Quiet Network, and Mass Battle all converge.
**Non-Player Characters:** Baralta (Solmund claim), Himlensendt (Debate opponent — Evidence Resonant Style), Ehrenwall (Coup Counter), Vaynard (intelligence), Maret Uln (dual loyalty), Olafsson (Niflhel connection), Klapp (archive testimony), Revolution elder (inner-tradition testimony) [EDITORIAL]

### ARC-34: Ehrenwall's Count
**Engine:** IP 30 → Löwenritter Coup Counter + Martial Law
**Emergence:** IP reaches 30 (same trigger as Arc 10). Coup Counter fires. Martial Law declared. Mass Battle and Grand Debate (to remove Martial Law) become available.
**Non-Player Characters:** Ehrenwall (Coup Counter), Brandt (succession if Ehrenwall falls — Counter threshold 2 not 3, redirects military to borders), Almud (target), Torsvald (Riskbreaker exposure risk), Almstedt (Ministry disruption)

### ARC-35: The Klapp Threshold
**Engine:** Klapp CE 4 + sustained archive contact with originary Locks
**Emergence:** Klapp's CE from archive work. TS development via threadwork v2.5 §2.3 Discovery. If Klapp converts: TC generation pauses (Church internal fracture), Church Stability implications.
**Non-Player Characters:** Klapp (primary), Himlensendt (must choose: suppress Klapp or deviate from doctrine), Haelgrund (parallel TS — if both Klapp and Haelgrund exposed → Church loses education + investigation leadership simultaneously)

### NPC-ARC-HAE: The Haelgrund Defection
**Engine:** Haelgrund hidden TS 12 + practitioner proximity
**Emergence:** Any Player Character with TS ≥ 30 who interacts with Haelgrund during an investigation can attempt Diagnosis (Cognition vs Ob 2). Success reveals Haelgrund's TS. What the Player Character does with this information defines the arc.
**Non-Player Characters:** Haelgrund (primary), Himlensendt (institutional response), Klapp (parallel crisis if simultaneous)
**Consequence:** Haelgrund removed from Church service → Church Heresy Investigation Ob +1 permanently (best investigator lost). Haelgrund available as neutral Non-Player Character practitioner (TS 12 — low but symbolically devastating).
**BG Event Card:** *Haelgrund Defection* — trigger: Thread operation Overwhelming within 1 territory of Haelgrund's investigation AND no active Inquisitor suppression.

### NPC-ARC-TOR: The Torsvald Exposure
**Engine:** Torsvald TS 35 + Riskbreaker operations in Thread-active zones
**Emergence:** Riskbreaker operations in Thread-active territories: ~30% abort rate when Torsvald leads. Aborted operations leave evidence → Deniability Debt +1. Pattern becomes detectable. If Ehrenwall (or successor) identifies the cause → Torsvald exposed as Thread-sensitive within anti-Thread institution.
**Non-Player Characters:** Torsvald (primary), Ehrenwall/Brandt (superior officer), Lenneth (archive connection — Torsvald is natural escort for Lenneth's arc)
**Consequence:** Crown covert capability −1D for 1 season per abort. Torsvald becomes potential bridge between Lenneth's intellectual curiosity and practitioner world.

### NPC-ARC-BRA: The Brandt Succession
**Engine:** Ehrenwall removal → succession
**Emergence:** Ehrenwall removed (death, player action, or Lions' Table Mutiny). Brandt takes command. Military assets redirect from internal political control to border defence (T3 Lowenskyst, T10 Spartfell). Coup Counter threshold drops from 3 to 2 (Brandt acts sooner).
**Non-Player Characters:** Brandt (primary), Ehrenwall (predecessor), Almud (if coup target changes), Laskaris (if Brandt's border focus validates Altonian threat → IP dynamics shift)
**Consequence:** Crown-held territories lose Martial Law garrison coverage. Military actions T3/T10 at −1 Ob (border focus), all other territories +1 Ob (internal neglect).

### NPC-ARC-FEL: The Supply Chain Exposure
**Engine:** Thread-touched goods in Guilds supply chain (via Niflhel/Virke)
**Emergence:** Investigation reveals Thread connection in guild merchandise. Intel + Thread Diagnosis on guild goods (Ob 3). Cascades to Virke (shared supply chain).
**Non-Player Characters:** Feldhaus (Guilds — primary), Virke (Niflhel syndicate — supply source), Haelgrund (if Church opens Heresy Investigation), Olafsson (if Niflhel connection exposed simultaneously → multi-faction cascade)
**Consequence:** Guilds Wealth −1, Stability −2. Church opens free Heresy Investigation vs Guilds. Virke family network disrupted (Niflhel trade +1 Ob for 2 seasons). OR: quiet audit (spend 1 Wealth + 1 Stability) removes Thread goods, no scandal, but Wealth recovery bonus permanently lost.

### NPC-ARC-STR: Strand Turned
**Engine:** Strand flattery vulnerability (−1 Ob) + non-Crown faction Intel
**Emergence:** Any non-Crown faction succeeds on Intel action targeting Crown Court with Overwhelming. Strand's insecurity makes him the easiest approach vector. Intelligence leak: non-Crown faction learns Crown's full stat line + planned actions for next season.
**Non-Player Characters:** Strand (primary), Almud (Crown head — consequences fall on him), whoever targets Strand (Church, Varfell, Hafenmark, Niflhel)
**Consequence:** Strand removed. Crown admin +1 Ob for 2 seasons (he IS the administrative capacity). Counter-play: Crown counter-intelligence (Intel vs Ob 2) each season.

### NPC-ARC-VIR: The Virke Recall
**Engine:** Virke trust network vs family discipline
**Emergence:** Virke shields Valorian trade partners from family intelligence operations. Three instances of protecting partners over family revenue triggers family intervention. Virke replaced by operator with no local relationships.
**Non-Player Characters:** Virke (primary), Feldhaus (shared supply chain — if Virke recalled, Guilds lose Thread-touched luxury goods access), all factions inside trust network
**Consequence:** Trust network collapses overnight. All Niflhel trade actions +1 Ob for remainder of campaign. Replacement has no loyalty to anyone on the peninsula.

### NPC-ARC-LAK: The Laskaris Flip
**Engine:** Laskaris PROTECTIVE flaw + Elske Loyalty track
**Emergence:** Elske Loyalty ≤ 2 at Accounting OR Elske Return attempt fails. Laskaris stops shielding Valoria and prioritises Elske extraction.
**Non-Player Characters:** Laskaris (primary), Elske (trigger condition), Almud (Crown consequences), Torben (if simultaneously under Altonian control → both royals compromised)
**Consequence:** IP +3 immediately. Laskaris replaced by imperial-loyal governor. IP generation returns to baseline. Elske's off-board card locked (no Contact attempts until new diplomatic channel — Crown Influence vs Ob 4).

### NPC-ARC-SOL: The Solberg Recall
**Engine:** Schoenland central discovers Solberg's stability bias
**Emergence:** Schoenland central reassesses or discovers Solberg is downplaying instability and understating demand. Solberg recalled. Neutral replacement installs.
**Non-Player Characters:** Solberg (primary), all faction leaders (arms supply and intelligence dynamics change)
**Consequence:** Arms supply to all factions +1 unit/season. Intelligence to Schoenland sharpens. Schoenland becomes a more dangerous neutral actor. Counter-play: players offer Solberg a plausible stability treaty → he becomes a genuine Crown/Hafenmark asset.

### NPC-ARC-PRU: The Parish Revolt
**Engine:** Prudence Cardinal tithe pressure + Church Mandate erosion
**Emergence:** ≥ 3 territories where Prudence Cardinal has increased tithes AND Church Mandate ≤ 3 in any. Parish leaders refuse collection.
**Non-Player Characters:** Prudence Cardinal (primary), Himlensendt (institutional response), Vossen (RM recruitment in over-tithed territories — CV erosion accelerates +1/Year-End)
**Consequence:** Church Wealth −2 for 1 season. Conviction Yield (CV) −1 in affected territories. TC −1 (institutional fracture). Counter-play: Church spends 1 Stability to discipline Parish leaders (tithes restored but Mandate −1 permanently).

### NPC-ARC-ULN: The Maret Uln Succession
**Engine:** Vaynard elimination → Varfell succession (PP-486)
**Emergence:** Vaynard eliminated (Loyalty 0 + Mandate 0). Maret Uln takes Varfell leadership. Aligns with RM goals. Varfell Thread Mastery (VTM) resets to 0.
**Non-Player Characters:** Maret Uln (primary), Vaynard (predecessor), Vossen (RM alignment partner), Edeyja (Maret's TS ~50 — potential Warden cooperation)
**Consequence:** Varfell cannot target RM. Varfell Stability −1 (reorientation). Varfell intelligence apparatus weakened but RM gains a practitioner-led faction ally. Structural pressure on Revolution relieved (Arc 14 may not fire).

### NPC-ARC-VOS: The Vossen Exposure
**Engine:** Church AP accumulation against Vossen
**Emergence:** Every season Vossen operates publicly, Church gains +1 AP toward her location. Vossen cannot lead from hiding (movement requires visible leadership for Popular Will). Church Heresy Investigation resolves against her.
**Non-Player Characters:** Vossen (primary), Haelgrund (if assigned — investigation +1 season but Overwhelming), Maret Uln (if Varfell aligned with RM → protection), Revolution elder (if Vossen removed → leadership vacuum)
**Consequence:** RM loses named leader. Popular Will mechanism disrupted. CV erosion rate changes. If Haelgrund leads investigation and it resolves Overwhelming → Vossen is suppressed unless Player Characters intervene.

---

## Tertiary Arcs

These require narrow prerequisites, single-roll pivots, or specific player choices.

### ARC-18: The Tied Vote
**Engine:** Parliamentary Vote tie condition
**Emergence:** Parliamentary Vote called. Best of 3 exchanges; tie = motion fails by abstention → TC +1 AND RS −1 simultaneously. Pre-vote whipping via Influence Domain Actions (Ob 2–3).
**Non-Player Characters:** Almstedt (Parliamentary Clerk — facilitates procedure), Baralta (if motion concerns sovereignty), Himlensendt (if motion concerns Church authority), Almud (Crown position)

### ARC-20: The Tutoring Demand
**Engine:** IP 30 → Almud Belief collision
**Emergence:** IP reaches 30. Altonian Tutoring Demand issued. Almud faces Belief 1 vs Belief 3 direct collision. Crown Influence vs Ob 3 (negotiate delay) or refuse.
**Non-Player Characters:** Almud (Beliefs), Torben (subject), Laskaris (PROTECTIVE — may delay demand 1 season), Ehrenwall (Coup Counter +1 if Torben taken)

### ARC-21: The Excommunication
**Engine:** Olafsson Church Mandate roll vs Baralta Mandate
**Emergence:** Olafsson files complete (2 seasons building). Excommunication declared vs Baralta. Church Mandate 5d10 TN 7 vs Ob 7 (Baralta Mandate). Players may intervene with counterevidence (−1 Ob).
**Non-Player Characters:** Olafsson (initiator), Baralta (target), Himlensendt (if forced to arbitrate), Haelgrund (if assigned investigation role)

### ARC-22: The Ceiral Ritual
**Engine:** Multiple narrow prerequisites
**Emergence:** Ceiral Text held, Awareness 5+, Maret Uln TS 60+, 2× TS 20+ participants, preparation season completed, all personnel in Askeheim (T13). Lead practitioner Weaving pool vs Ob 5.
**Non-Player Characters:** Maret Uln (if lead), Edeyja (Askeheim access), practitioner Player Characters
**Failure cascade (Collision C):** Ritual failure → RS +8, Mode 3 entity, lead practitioner incapacitated. If RS near 50 → Southernmost cracking clock resets. IP +2, TC +2. Ehrenwall Coup Counter may reach 3 from single-season cascade.

### ARC-23: The General Falls
**Engine:** Combat wound threshold + single Medicine roll
**Emergence:** Mass battle: Ehrenwall engaged. Wound in Phase 4 or from Thread operation. Wounds reach ceiling(Health ÷ 2) → Incapacitation. Medicine Ob 2 (stabilise) — one-turn window in Phase 5.
**Non-Player Characters:** Ehrenwall (primary), Brandt (immediate succession → NPC-ARC-BRA fires), Almud (if Ehrenwall falls during coup → legitimacy crisis), Torsvald (if present → Thread-collateral abort risk)

### ARC-25: The Schoenland Pivot
**Engine:** Solberg Non-Player Character observation + Domain Action
**Emergence:** Schoenland reads political situation each season (inputs: Mandate levels, Prosperity in T7/T4, IP trajectory, trade disruption, Altonian intelligence from T15). Crown Influence vs Ob 3 Diplomatic Domain Action.
**Non-Player Characters:** Solberg (STABILITY-SEEKING — biases reading), Laskaris (Altonian intelligence source), Strand (Crown diplomatic capacity)

### ARC-27: The Dissolution
**Engine:** Player choice + high TS prerequisite
**Emergence:** Practitioner declares Dissolution. TS 50+ required. Diagnosis mandatory. Target: personal Non-Player Character configuration, institutional record, Locked Zone border, or political thread. Spirit + relevant pool vs Ob (minimum Ob 4).
**Non-Player Characters:** Edeyja (Dissolution authority — will she approve?), Maret Uln (TS ~50 — meets threshold), any practitioner Player Character

### ARC-32: Vaynard's Confession
**Engine:** Vaynard TK 4 + Hybrid multi-system convergence
**Emergence:** TK reaches 4 (practitioner relationship × 2 seasons). Vaynard TK track, Discovery Event, Thread operations, Inquisitor CE track, Parliamentary Vote, faction play converge.
**Non-Player Characters:** Vaynard (primary), Maret Uln (dual loyalty), Olafsson (Church response), Baralta (if simultaneous with Solmund claim), Klapp (if archive evidence relevant), Haelgrund (if Inquisitor CE track involved)

### ARC-33: The Forgetting Road
**Engine:** Player choice + TS 30 prerequisite
**Emergence:** Expedition to the Southernmost. TS ≥ 30 required (below 30 → dissolve without awareness). Forgetting mechanic (§6.1) applies. Faction consequence on return via Domain Echo. TC spike.
**Non-Player Characters:** Edeyja (Southernmost authority), Maret Uln (if expedition member — TS ~50), Vossen (TS 25 — below threshold, cannot participate safely)

---

## Collision Scenarios (Multi-Arc Convergence)

These are not independent arcs but configurations where multiple arcs fire simultaneously, producing compound effects.

### COLLISION A: Church Double Fracture
**Trigger:** Klapp conversion (Arc 35: TS 30+, CE 4) coincides with Olafsson exposure (Arc 09)
**Effect:** Church Stability −3 (two simultaneous crises). TC generation pauses (Stability ≤ 4, Cardinals competing). Window opens for player action without TC escalation. Klapp becomes practitioner ally with archive access and originary Locks.
**Non-Player Characters:** Klapp, Olafsson, Himlensendt (must choose: suppress Klapp or deviate), Haelgrund (if also exposed → triple fracture)

### COLLISION B: The Einhir Practitioner King
**Trigger:** Almud Discovery Event (Arc 29) + Elske installed independently + Torben in Altonia
**Effect:** Almud publicly acknowledges Thread practice → TC +3 but RS improves. Axis 9 resolves publicly. Campaign central question answers itself.
**Non-Player Characters:** Almud, Elske, Ehrenwall (no coup trigger from TS alone), Himlensendt (doctrinal crisis), Laskaris (if Elske installed → protective instinct satisfied)

### COLLISION C: Tutoring Demand + Southernmost Failure
**Trigger:** Torben at Loyalty 3 (Arc 10) coincides with Ceiral Ritual failure (Arc 22)
**Effect:** RS +8, IP +2, TC +2. RS crosses 50 → Southernmost cracking clock resets. Ehrenwall Coup Counter may reach 3 from single-season cascade.
**Non-Player Characters:** Torben, Almud, Ehrenwall, lead practitioner (incapacitated), Laskaris (IP surge)

### COLLISION D: Niflhel Weaponises Everything
**Trigger:** Full Church-Niflhel exposure + assassination perpetrator = Niflhel + Varfell Private Collection in Niflhel's hands
**Effect:** Niflhel has leverage over every faction simultaneously. Sells to highest bidder. Cascade varies by buyer.
**Non-Player Characters:** Virke (syndicate broker), Olafsson (Church connection), Vaynard (if Varfell involvement), Strand (if Crown pays → Riskbreaker Deniability Debt +3)

### COLLISION E: The Einhir Elder and Baralta's Claim
**Trigger:** Revolution elder testimony + Baralta Solmund claim + Klapp archive access (Arc 31)
**Effect:** Grand Debate (5 exchanges). If Himlensendt's reinterpretation fails → Church Stability −3. Axis 9 resolves publicly. Originary Locks enter public discourse → practitioner attempts → RS consequences.
**Non-Player Characters:** Baralta, Himlensendt (Evidence Resonant Style turned against him), Klapp (archive testimony), Revolution elder [EDITORIAL], Edeyja (if originary Lock attempts → substrate consequences)

---

## Endgame Configuration

The campaign's central dramatic question resolves when ≥ 3 of these conditions are simultaneously true:

| Condition | Effect | Arcs Contributing |
|-----------|--------|-------------------|
| Almud TS 30+ | Monarchy acknowledges Thread reality | 29, Collision B |
| Axis 9 resolves publicly | Church foundational claim contested | 04, Collision B/E |
| Elske installed independently | Succession stable without Altonia | 10, NPC-ARC-LAK |
| Torben retrieved at Loyalty 6+ | Dynasty intact | 10, 20 |
| RS above 40 (Wakening → Stirring) | Practitioners functional; world stabilising | 03, 07, 08 |
| TC below 40 | Church institutional conquest stalled | 13, 31, 35, NPC-ARC-PRU |
| IP below 45 | Altonian invasion deterred | 01, 10, 34, NPC-ARC-LAK |
| Ehrenwall Coup Counter ≤ 1 | Löwenritter maintain loyalty | 01, 34, 23, NPC-ARC-BRA |
| Southernmost stabilised (Ceiral success) | RS −6 to −10; world healing | 22 |

**All nine simultaneously:** STABLE — the peninsula survives intact, changed.
**None simultaneously:** The Einhir Catastrophe repeats — political and metaphysical conditions that produced the original collapse are recreated.

---

## Arc Dependency Map

```
PRINCIPAL ENGINES
─────────────────
ARC-13 (TC clock)
  ├→ ARC-09 (Baralta suppression — counterweight)
  ├→ ARC-12 (Framework Trap — accelerant)
  ├→ ARC-31 (Quaestio — TC 42)
  │    ├→ ARC-21 (Excommunication — branching)
  │    └→ COLLISION E (Einhir Elder + Baralta claim)
  ├→ ARC-18 (Tied Vote — TC +1 spike)
  ├→ ARC-35 (Klapp → TC generation pause)
  │    └→ COLLISION A (Church Double Fracture)
  └→ NPC-ARC-PRU (Parish Revolt — TC −1, CV erosion)

ARC-01 (IP clock)
  ├→ ARC-10 (Princess — IP 30)
  │    └→ NPC-ARC-LAK (Laskaris Flip — Elske Loyalty ≤ 2 → IP +3)
  ├→ ARC-34 (Ehrenwall's Count — IP 30 / Coup Counter)
  │    └→ ARC-23 (General Falls → NPC-ARC-BRA Brandt Succession)
  └→ ARC-20 (Tutoring Demand — IP 30)
       └→ COLLISION C (+ Ceiral failure)

ARC-03 (RS clock)
  ├→ ARC-07 (Rendering Debt — war accelerant)
  ├→ ARC-08 (Temporal Window — RS ≤ 60)
  ├→ ARC-05 (Brittle Peace — localised RS stress)
  ├→ ARC-22 (Ceiral Ritual — RS recovery attempt)
  └→ ARC-28/29/30 (Coherence Zero — endgame)

ARC-04 (Axis 9)
  ├→ ARC-02 (Vaynard Cascade — TK track)
  │    ├→ ARC-26 (Duke Awakens — TS 14)
  │    ├→ ARC-32 (Confession — TK 4)
  │    └→ NPC-ARC-ULN (Maret Uln Succession — Vaynard eliminated)
  ├→ ARC-06 (Tribunal — Church response)
  │    └→ NPC-ARC-HAE (Haelgrund Defection — TS exposed)
  ├→ ARC-11 (Klapp TS)
  │    └→ ARC-35 (Klapp Threshold)
  └→ COLLISION B (Practitioner King — Almud TS 30+)

ARC-16 (NPC AI — runs when players absent)
  ├→ ARC-25 (Schoenland Pivot — NPC reads)
  └→ NPC-ARC-SOL (Solberg Recall — Schoenland reassessment)

ARC-24 (Faction That Breaks — Stability)
  ├→ ARC-14 (Revolution structural contradiction)
  └→ Any faction-specific collapse arc

ARC-19 (Accounting Sequence)
  └→ [cross-cuts all arcs via seasonal order]

INDEPENDENT ENTRY (player-initiated)
  NPC-ARC-FEL (Supply Chain Exposure — investigation)
  NPC-ARC-STR (Strand Turned — Intel action)
  NPC-ARC-VIR (Virke Recall — family discipline)
  NPC-ARC-TOR (Torsvald Exposure — Deniability Debt pattern)
  NPC-ARC-VOS (Vossen Exposure — Church AP accumulation)
  ARC-15 (Headless Network — Niflhel engagement)
  ARC-17 (Favour Gate — Guild engagement)
  ARC-27 (Dissolution — player choice)
  ARC-33 (Forgetting Road — expedition choice)

COLLISION SCENARIOS (multi-arc convergence)
  COLLISION A: Church Double Fracture (35 + 09)
  COLLISION B: Practitioner King (29 + Elske + Torben)
  COLLISION C: Tutoring + Southernmost (10 + 22 failure)
  COLLISION D: Niflhel Weaponises (15 + 09 + assassination)
  COLLISION E: Einhir Elder + Baralta Claim (31 + elder + Klapp)
```

---

## Simulation Coverage

| Arc | Simulated | Source |
|-----|-----------|--------|
| ARC-01 through ARC-30 | Yes (CP14 batch) | `designs/gm_ref_cp14/arcs/` |
| ARC-31, ARC-33 | Yes — clean | `arcs_31_35_hybrid_systems.md` |
| ARC-32, ARC-34, ARC-35 | **NOT YET SIMULATED** | `arcs_31_35_hybrid_systems.md` note |
| NPC-ARC-HAE through NPC-ARC-VOS | **NOT YET SIMULATED** | Derived from `npc_roster.md` |
| COLLISION A through E | **NOT YET SIMULATED** | `narrative_scenario_chains.md` |

---

## Open Items

| ID | Item | Status |
|----|------|--------|
| GAP-ARC-01 | Arc 15 — Niflhel Quiet deployment RS/Thread Tension accumulation cause | Pending editorial clarification |
| ED-NEW | Tier assignments (principal/secondary/tertiary) | Provisional — user review required |
| ED-NEW | Revolution elder — not canonised as named character | Required for Collision E |
| ED-NEW | Elske TS development — not established | Affects Collision B branching |
| ED-NEW | Jarnstal — minimal mechanical data | Editorial gap in NPC tracks |
| ED-358 | Full roster identities, motivations, stat blocks | Provisional — user review pending |
| E-01 | Perpetrator of 218 AG assassination | Unresolved — affects Collision D branching |
