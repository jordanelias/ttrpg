# Digest designs_rest

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: archived design documents under `.designs/` that earlier lanes did not finish (18 files: factions index stubs, the NPC behaviour/analyses/roster set, the overview clock registry, MS budget and flow skeleton). All sources are ARCHIVED-NOT-CANON; read for intent, vocabulary, referents.

### .designs/systems/factions/reference/faction_succession_split_v30_index.md
- **What it is:** auto-generated heading/size index (doc_index_gen.py, generated 2026-04-19) of `faction_succession_split_v30.md`; no design content of its own.
- **Status:** no Status line; ARCHIVED-NOT-CANON banner (:2-5). Reading: historical (index of a sibling that is itself archived).
- **Bears on:** FA, WR.
- **Content that matters:**
  - Outline of the parent doc: §2.1 Trigger Matrix, §2.2 Contest Mechanics "Generalized from Baralta Spec", §2.3 Outcomes, §2.4 Faction Split Mechanics, §2.5 Split Persistence (:21-34).
  - §3 Worked Example is "Vaynard Falls"; §4 is "RM Emergence Trajectory (Formalization of Existing Stage 2→5 Pathway)"; §5 Implementation (Videogame); §6 Open Items (:31-34).
  - Parent is 2,701 tokens; §2 (universal succession contest framework) is the bulk at 1,210 tokens (:12, :41).
  - Canonical pointer is the dissolved path `designs/provincial/faction_succession_split_v30.md` (:10), i.e. a pre-`.designs/` location.
- **Conflicts / stale:** usage line names `g.read_sections(...)`, a retired reader (:17) `[UNVERIFIED]`; canonical path `designs/provincial/` is dissolved (CLAUDE.md §3 "Dissolved").
- **Open items:** none in the index; the parent has a §6 Open Items (not read here; sibling file `faction_succession_split_v30.md` exists in the same directory).

### .designs/systems/factions/reference/factions_personal_v30_index.md
- **What it is:** auto-generated heading/size index (generated 2026-04-20) of `factions_personal_v30.md`, "PART EIGHT: FACTIONS".
- **Status:** no Status line; `canonical_sha: unknown` (:11). Reading: historical.
- **Bears on:** FA, WR, CHAR.
- **Content that matters:**
  - Roster of factions at v30: Crown (Monarchy), Church of Solmund, Hafenmark (Duchy), Varfell (Duchy), Guilds, "Faction 6: [DISSOLVED — Niflhel struck]", People's Revolution (Restoration Movement), Löwenritter (Military Order), plus 8.9b Ministry of the Peninsula "Institutional Actor — Throughline T4", and 8.10 Schoenland "Spoiler Actor" (:31-41).
  - Faction mechanics subsections: "Faction Stats (6-stat, 1–7 scale)", Starting Values, Domain Actions, Ethical Framework Modifiers, "Leader vs Institution" (7 tokens, effectively empty), "Nine Political Axes" (:25-30).
  - 8.11 Parliamentary Vote and 8.12 "Seasonal Accounting — Faction Phase" close the part (:41-42).
  - Largest faction sections: Löwenritter 835 tokens, Revolution 820, Hafenmark 801 (:57-62).
- **Conflicts / stale:** faction count and the 6-stat / 1-7 scale are v30 claims; check against `engine/season/` faction state before use `[UNVERIFIED]`. Niflhel strike is documented elsewhere (CR-STRIKE-2026-04-19, per edeyja_npc.md:69).
- **Open items:** none in the index.

### .designs/systems/factions/reference/fractional_province_ownership_v30_index.md
- **What it is:** auto-generated heading/size index (generated 2026-04-19) of `fractional_province_ownership_v30.md`, the "Split-Province Mechanic".
- **Status:** no Status line. Reading: historical.
- **Bears on:** SE, FA.
- **Content that matters:**
  - Mechanic outline: §2.1 Trigger, §2.2 Province Value (PV) Re-derivation, §2.3 Greater / Lesser Naming, §2.4 "Consolidation Threshold (CK3 Precedent)", §2.5 Effects of Fractional State, §2.6 Resistance and Collapse of Fractional States (:26-31).
  - §3 Worked Example; §4 Implementation (Videogame); §5 Open Items (:32-34).
  - Parent is 2,245 tokens; §2 is 1,380 of those (:40-42).
- **Conflicts / stale:** canonical pointer dissolved path `designs/provincial/` (:10). Whether `engine/season/` has any fractional ownership at all is `[UNVERIFIED]` here.
- **Open items:** parent's §5 Open Items not read here.

### .designs/systems/npcs/reference/baralta_v30.md
- **What it is:** NPC theology profile of Duchess Inge Baralta, extracted 2026-04-25 from `miraculous_event_v30.md` §21 (Stage 4 routing fix, conflict-eval finding MEDIUM-01), Jordan-extension content.
- **Status:** "PROVISIONAL — pending Jordan editorial review" (:14). Reading: historical / unclear (never shown ratified).
- **Bears on:** CHAR, FA, WR, ARCS.
- **Content that matters:**
  - Historical anchors Isabella I of Castile / Henry VIII; "She does not question the Church's theology. She questions its jurisdiction." (:23).
  - Jordan's extension: Baralta believes in direct communion with Solmund without Church mediation; deeds are evidence of divine favour (:27). Accepts Church *content*, rejects its *monopoly on mediation* (:31).
  - Editorial item: NPC analysis §6 should be updated from "jurisdictional challenge" to "theological innovation" (:33).
  - Perceptual prophylaxis: her deed-theology introduces contingency and weakens prophylaxis over generational timescales; explicitly NOT a mechanical variable in play (~5-year game span) (:37-39).
  - She is the Restoration Movement's "pure adversary"; framework has two legitimate sources (sovereign, Solmund), so Einhir pre-Solmund tradition threatens it (:43).
- **Conflicts / stale:** the editorial item at :33 may or may not have been applied to `npc_character_analyses_v30.md` (see that entry). Orphan atom comment at :45 ("22-faction-response-pathways") has no content under it.
- **Open items:** the editorial update of NPC analysis §6 (:33); Jordan's review of the entity canon (:9).

### .designs/systems/npcs/reference/edeyja_npc.md
- **What it is:** full NPC sheet for Edeyja, Southernmost Warden-Chief, dated 2026-03-30; written for a Game Master reader (pre-"no GM" framing).
- **Status:** "Canonical Non-Player Character (working name — pending final name pass with territory naming audit)" (:10). Reading: historical; GM-facing prose, partly superseded by the no-GM engine.
- **Bears on:** CHAR, WR, FI, ARCS, MB.
- **Content that matters:**
  - Stats: Thread Sensitivity 75-80 ("highest of any living practitioner"), Coherence 9, Cognition 5, Focus 5, Endurance 4, social attributes 3-4 (:29-33). Uses a Thread Sensitivity 0-80ish scale, not a dice-pool attribute scale.
  - Conviction "Warden"; Resonant Style "Evidence" (:38-39): abstract appeals do not register, Thread-state data does.
  - Access gating table by expedition progress: Askeheim border = no contact; Season 2 entry: TS ≤20 dismissed, 21-39 limited guidance, 40+ useful; Season 3 primary site: substantive; Season 4+ after successful Extraordinary Weaving: collaboration; multiple Weaving seasons: reveals the Calamity's mechanism and Locked Zones (:77-83). She never leaves the Southernmost (:85).
  - Conflict-as-disturbance: each inter-faction battle registers (mass_battle §E.1: MS -1/battle, MS -2 at Campaign/War scale; calamity_radiation THREAD-tagged Domain Actions, PP-531); slow-burn arc as Turmoil rises and MS decays (:69). Replaces the struck Niflhel supply-chain framing.
  - Warden count "single digits to low teens", a dying institution; she has accepted "a handful" of outsiders (:46-48). Military non-answer: coordinated Weaving makes conquest irrational; Varfell/Vaynard suspects, Church does not want to know (:53-55).
  - Varfell link: if Vaynard reaches TK 5 and comes to her, she will talk to him (:68); Dahl Erikssen (TS 18, Restoration) she would dismiss (:62).
- **Conflicts / stale:** MS -1/-2 per battle is a design number quoted from mass_battle §E.1; check against the code before use `[UNVERIFIED]`. "Game Master's discretion" (:48) and GM Notes (:89-93) contradict the no-GM engine; "exact values for Game Master reference" (:28). Pronouns flagged [EDITORIAL: confirm] (:12).
- **Open items:** name pass with territory audit (:10); pronouns (:12); whether an engine registry has Edeyja with a TS value or gating table at all `[UNVERIFIED]`.

### .designs/systems/npcs/reference/npc_behavior_system_v1.md
- **What it is:** the v1 NPC Ethical Stance and Resonance Behaviour System, dated 2026-04-13: Stance Triangles for ~13 named NPCs, Belief/Scar machinery, arc state machines, Resonant Style contest targeting, framework drift, and board-game priority trees (836 lines; the first full TTRPG/BG/Hybrid NPC model).
- **Status:** "SUPERSEDED — canonical doc is designs/systems/npc_behavior_v30.md (editorial batch acceptance 2026-04-17). Retained as historical reference." (:11). Reading: superseded by `npc_behavior_v30.md` (sibling in the same directory); the NPC vocabulary here (Conviction, Resonant Style, Scar) is the ancestor of what the v30 doc and `engine/season` person queries use.
- **Bears on:** CHAR, SC, FA, WR, FI, ARCS.
- **Content that matters:**
  - Stance Triangle = Conviction (what they want), Ethical Framework (inherited from faction; what the institution rewards), Resonant Style (the argument form that bypasses their defences) (:21-31). Convictions closed set of 7: Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity (:35-43); Resonant Styles closed set of 4: Evidence, Consequence, Authority, Solidarity, each mapped to a social-contest genre pair (:49-54). Primary plus secondary of each; the secondary "activates under pressure" (:45, :56).
  - Named-NPC roster with Conviction pair / Ethical Framework / Resonant Styles / Thread Sensitivity / Truth / Leadership Deviation Ob: Almud (Order/Reason, TS 28, Truth 3, LDO 2), Himlensendt (Faith/Order, TS 0, Truth 5, LDO 3), Baralta (Precedent/Faith, TS 0, Truth 4, LDO 1; ED-531 resolved Precedent over stage6 "Order"), Vaynard (Reason/Autonomy, TS 14, Truth 3), Ehrenwall (Order/Autonomy), Vossen, Hann, Torben (blank Conviction, set by first faction to reach Loyalty ≥ 5, else Autonomy by end of Year 2), Edeyja (Continuity/Reason, TS 75-80, Truth 0, no framework), Maret Uln (Equity/Reason, activates only if Vaynard eliminated, PP-486), Guild Council, Niflhel, four Cardinals (:62-316).
  - Decision procedure (:364-381): Step 1 institutional filter (Ethical Framework Ob modifiers; for non-named NPCs this IS the decision, :383-387); Step 2 conviction filter; Step 3 Decision Fork keyed on Scar count (0: Conviction over Framework at a Leadership Deviation Stability check; 1: the Conviction the last Scar did not address; ≥2: conviction-crisis d6 table; Stability ≤ 1: Autonomy regardless); Step 4 a PC Contest suspends the Fork.
  - Belief lifecycle: 2-3 Beliefs per named NPC; revised only when a decisive contest (Piety Track ≥ 7 or ≤ 3) win used the NPC's Resonant Style AND engaged that Belief; old Belief becomes a permanent Scar (:334-341); Scar table 0/1/2/3+ and a d6 crisis table (1-2 original, 3-4 secondary, 5 Autonomy, 6 last-PC-aligned) (:343-358). Revealing a Belief: Appraise Overwhelming, Niflhel Intelligence, Knot Close/Intimate, or observation (:328-332).
  - Targeting rules: a declared Resonant Style hit gives +1D, and each style adds its own rider (Evidence +1 Piety bypass; Consequence +2 strain; Authority Doubt Marker; Solidarity needs a Knot and lowers next revision Ob by 1) (:561-568); positional cap +5D (genre 1, audience 1, style 1, Recall 2) (:578). Evidence against TS 0 NPCs is limited to "ontical" evidence; Thread-level data works only once TS ≥ 30 (AUD-NPC-01 fix, :546-550). Church wrong-style in public: Church Stability +1 (PP-259 Martyrdom) (:572-574).
  - Arc maps: Almud A Reformer / B Fortress / C Overthrown (Coup Counter 3); Himlensendt A Zealot (default) / B Crisis of Faith / C Confrontation (needs a threadcut being or Locked Zone); Baralta A Constitutional Triumph / B Pragmatist / C Excommunication; Vaynard A Scholar (TK 5, TS < 30) / B Awakened (TS ≥ 30, TK ≥ 3) / C Consumed; Edeyja A Holdout / B Collaboration / C Crisis (warden count 0 or MS ≤ 20; she may leave the Southernmost, :523-536). Branch conditions are concrete game-state predicates (:428, :436, :443, :452, :458, :465).
  - Seven-level board-game priority tree template: 1 Survival (Stability ≤ 2), 2 Conviction-critical, 3 Framework-aligned opportunity, 4 Institutional tendency, 5 Secondary conviction, 6 Reactive, 7 Pass (:618-628), instantiated for Church, Crown, Hafenmark, Varfell, Guilds, Löwenritter, Niflhel, Restoration, Wardens (:630-740). Framework Drift table, one passive drift per framework (:590-600). Transformation knot strain propagation by TS band (:393-405).
- **Conflicts / stale:** wholly superseded by `npc_behavior_v30.md` (not read here). Quotes v30-era faction machinery (TC, Piety Track, Coup Counter, Mandate, Domain Action caps, Niflhel) that the Niflhel strike (CR-STRIKE-2026-04-19 per edeyja_npc.md:69) partly removed, while this doc still carries a Niflhel arm (:287-301, :706-716). The "GM" is the arbiter throughout (:339, :350, :387, :468), contradicting the no-GM engine. Edeyja Arc C "explicitly overrides" `edeyja_npc.md`'s "never leaves" (:533), a contradiction between the two. engine/ and rosters grep count shows `conviction`/`resonant_style` are live words in 73 engine files (e.g. `engine/season/rosters.yaml`, `state/carriers.py`, `harness/decision_spread.py`) so the vocabulary survives into code; whether the Scar machinery does is `[UNVERIFIED]`. The index file's line numbers (e.g. §3.2 at :326) are ~8 lines behind this file's (:334), so the index is stale against the body.
- **Open items:** ED-515..ED-530 editorial items (:776-791; P1 blockers: ED-517 arc shapes, ED-518 "BG priority trees, P1-BLOCKER for BG sim"); SIM-NPC-01..05 simulation debt, none shown executed (:799-803); Hann has only two Beliefs and no arc (:200-204).

### .designs/systems/npcs/reference/npc_behavior_system_v1_index.md
- **What it is:** auto-generated heading/size index of `npc_behavior_system_v1.md` (generated 2026-04-19, PP-673 rename from `_skeleton`), 166 lines.
- **Status:** inherits the superseded line: heading 1 quotes "SUPERSEDED — canonical doc is designs/systems/npc_behavior_v30.md" (:25). Reading: historical.
- **Bears on:** CHAR, FA.
- **Content that matters:**
  - Parent size 16,360 tokens; §2 named stance triangles 5,139; §5 arc state machine 3,323 (of which §5.2 arc profiles 2,763); §8 priority trees 2,583 (:98, :108, :129, :148).
  - Section map = same structure as the body (§1 core, §2 triangles, §3 beliefs/scars, §4 decisions, §5 arcs, §6 resonance in contest, §7 drift, §8 priority trees, §9 hybrid, §10 editorial, §11 sim debt, §12 compliance, §13 propagation) (:30-92).
  - Carries `canonical_sha: 7c980a42e643` (:12) - a pin that no tool should now verify (the file is under the quarantine).
- **Conflicts / stale:** the Line column is stale against the body: index says §3 at :312, body has it at :320 (offset ~8); `g.read_sections` usage line (:18) refers to a retired reader `[UNVERIFIED]`.
- **Open items:** none.

### .designs/systems/npcs/reference/npc_behavior_v30_index.md
- **What it is:** auto-generated heading/size index (generated 2026-04-20) of `npc_behavior_v30.md` (22,532 tokens), the canonical successor of the v1 system; 245 lines. Its heading list is the only compact map of what v30 added to v1.
- **Status:** records the parent's status as "CANONICAL — approved 2026-04-17 (editorial batch acceptance)" (:24); `canonical_sha: unknown` (:11). Reading: historical map of an archived design; the parent is not canon any more (CLAUDE.md §0.05).
- **Bears on:** CHAR, SC, FA, WR, SE, CORE.
- **Content that matters:**
  - v30 additions over v1 (new headings): §2.13a Extra-Territorial Heresy Jurisdiction (ED-670); §2.14 Registrar Lennart Haelgrund (Ministry, Throughline T4, 1,578 tokens, the largest single NPC block); §2.15 Crown Inner Circle (PROVISIONAL, ED-634, names pending Jordan); §2.16 Hafenmark Inner Council (ED-635/636); §2.17 Varfell Jarl Council (ED-637/638) (:47-51).
  - §3.4 "Thread Operation → Conviction Scar Triggers (ED-663, ED-664)" and §4.3 "NPC Practitioner Coherence Decision Thresholds (ED-665)": NPC decision gates driven by Coherence and Thread operations (:56, :60).
  - §8.11 "NPC Personal Outreach Generation (NEW — feeds player_agency_v30 §4.2 Step 5)" with sub-sections Outreach Conditions, Demand Conditions, Outreach by Faction, Scene Structure, Volume Control, and §8.11.6 "Subnational Faction Outreach (per settlement_bridge_unification C-12)" - the NPC-initiates-contact mechanism, 1,437 tokens (:92-98).
  - §9.5 "NPC Recruitment Procedure (PP-642)": Identify, Approach, Offer, Resolution by Degree, Hooks, Defection (:103-109); §11 "Named NPC Roster Tracking Capacity (PP-661)": tiers, capacity, demotion triggers in priority order, background tier, inner-circle NPCs, companion app display (:125-131).
  - Second §7 "BG Faction Priority Trees" (Crown, Church, Hafenmark, Varfell, Löwenritter "activates on Crown elimination or Split", Ministry "procedural", Schoenland "observer", Altonian Vanguard "activates at IP ≥ 75") plus §7.9 override conditions and §7.10 "NPC Stat Values (Thread Sensitivity and Truth)" (:113-123): the faction-level NPC decision layer, 1,550 tokens, in addition to the §8 trees.
  - Niflhel shrank from 329 tokens (v1 §2.12) to 51 and its tree from 296 to 26 tokens (:159, :203 vs v1 index :120, :157): the strike's footprint.
- **Conflicts / stale:** the index shows structural defects of the parent: duplicate §5.2 heading (idx 41 and 42, :64-65), two §7 sections (drift at :78, BG trees at :113), two §11 sections (Simulation Debt :112, Roster Tracking :125), and §9.5 with no §9.4 (:103). These duplicated numbers mean a section citation like "§7" or "§11" in other docs is ambiguous `[UNVERIFIED which one is meant]`. Refers to dissolved `designs/npcs/` paths and a retired reader (:10, :17).
- **Open items:** none in the index itself; ED-634 crown inner-circle naming pending Jordan (:49).

### .designs/systems/npcs/reference/npc_character_analyses_v30.md
- **What it is:** the skeleton half of "Valoria - NPC Character Analyses", consolidated 2026-04-11, atomized 2026-04-13 (prose moved to `_infill`; the skeleton retains headings, a few mechanical paragraphs and many blank gaps). Part One 13 roster NPCs, Part Two the ruler diamond and existing named NPCs.
- **Status:** "Status: DESIGN" and "[EDITORIAL: All analyses flagged for user review.]" (:14-16). Reading: historical character reference; unclear which analyses were reviewed.
- **Bears on:** CHAR, FA, WR, FI, ARCS.
- **Content that matters:**
  - Roster with TS and mechanical flaw tags: Edeyja (TS 75-80, Coherence 9, "fixed point", does not arc, :24), Maret Uln (P-10 test; seduction toward empathy), Yrsa Vossen (TS 25, below the Forgetting resistance threshold 29, so she loses Einhir knowledge near T13/T15, :46), Sæmund Haelgrund (Inquisitor, hidden TS 12; Diagnosing him is "the single highest-impact personal scene in the roster", :57), Sigrid Torsvald (RISK-AVERSE, ~30% abort rate in Thread-active territory, TS developing; concealment threshold "TS 40? 45?" GM discretion, :66-69), Halvar Brandt (EXTERNAL THREAT FIXATED; Martial Law threshold 2 vs Ehrenwall's 3, :79), Annika Feldhaus (PROFIT-MAXIMISING; drives Guilds Mandate toward 2, :87), Peder Almstedt, Gerik Strand (flattery gives -1 Ob on social actions against him, :108), Dalla Virke, Doux Alexios Laskaris (PROTECTIVE: sandbags IP -1/season while Elske Loyalty ≥ 3, flips to IP +3 when ≤ 2, :126), Rikard Solberg, a Prudence Cardinal (name pending, :139).
  - Ruler diamond on the Einhir/caste axis: Almud (TS 0, pragmatism plus doubt), Lenneth (TS 0, SA-gated slow scholarly loosening, ceiling 10-20, D-6 / ED-727), Baralta (TS 0, pure adversary), Vaynard (environmental southern baseline) (:152-157). Almud is TS 0 here, versus TS 28 in v1 (`npc_behavior_system_v1.md:71`).
  - Royal Assassination Fuse: a Royal Crisis Tension Card, sub-rolled target (Lenneth 1-2, Torben 3-4, Almud 5-6, "params/bg/royal_assassination.md"), fires S8-S12; Almud target means Lenneth becomes Widow Regent (Crown inverts pro-Einhir, Church opens Heresy Investigation, Crown Mandate -2 to -3), Lenneth target means Almud Arc D "The Avenger", Torben target means Almud Arc E "The Bereaved Father" and a T4 military extraction of Elske (:188-197, :210, :220). Replaces the struck pre-game father-assassination backstory (infill :84).
  - Crown Mandate 5 is the highest starting faction stat and is the in-fiction answer to "was Almud competent" (:164); Baralta: Leadership Deviation Ob 1, PP-487 PI-gated succession fork, institution fractures at PI < 4 (:241-249).
  - Baralta theology supplement (PR-11 BA-1, ED-732, resolved 2026-04-20): accepts Church content, rejects its monopoly on mediation; this is the point where the editorial item in `baralta_v30.md:33` was applied, as a supplement not a supersession (:247).
  - Elske: in Altonia on a tutoring arrangement, not a default playable heir; relevant when the fuse hits Torben or as a standing Altonian chip (Tutoring Demand at IP 30) (:218-221, :212).
- **Conflicts / stale:** the skeleton has ~60 consecutive blank lines where per-NPC mechanical blocks used to be (e.g. :26-37, :44-46, :104-118, :226-234); for Dalla Virke, Vaynard, Klapp, Olafsson, Ehrenwall the skeleton has nothing at all and the infill only prose. Elske's status disagrees inside the set: skeleton says she is in Altonia on a tutoring arrangement (:218), the infill says she is married to Doux Laskaris (infill :98) and was "given" to him as a political instrument (infill :63). Almud TS 0 / no secret interiority contradicts v1 (TS 28, privately sympathetic to Restoration) and v1 Arc A "Reformer". Whether the engine's person data (`engine/season/rosters.yaml`) carries these flaw tags/TS values is `[UNVERIFIED]`.
- **Open items:** Prudence Cardinal's name (:139); Torsvald TS threshold "40? 45?" (:69); Jarnstal "Unchanged" with no earlier text to be unchanged from (:277); Almud's Arc D/E are referenced to `npc_behavior_v30.md` §5.2 but the v30 index (npc_behavior_v30_index.md :64-70) lists only five arc maps without lettered D/E `[UNVERIFIED]`.

### .designs/systems/npcs/reference/npc_character_analyses_v30_index.md
- **What it is:** auto-generated heading/size index (2026-04-20) of the skeleton above; 89 lines (read from :9).
- **Status:** none of its own (parent: "Status: DESIGN", :24). Reading: historical.
- **Bears on:** CHAR.
- **Content that matters:**
  - Parent total 4,797 tokens (:12); Part One 2,379 and Part Two 2,296 tokens (:63, :77).
  - Section token sizes expose which analyses survive in the skeleton: Lenneth 587, Almud 420, Baralta 412 are the largest; Dalla Virke 12, Prudence Cardinal 18, Vaynard 14, Klapp 14, Olafsson 16, Ehrenwall 15 are effectively empty (:73, :76, :83, :86-89).
  - Line numbers are ~8 behind the body (Edeyja at :14 versus body :22).
- **Conflicts / stale:** retired reader usage line (:17), dissolved canonical path (:10).
- **Open items:** none.

### .designs/systems/npcs/reference/npc_character_analyses_v30_infill.md
- **What it is:** the prose/rationale half of the same document (127 lines): the historical-parallel and flaw-rationale paragraphs per NPC.
- **Status:** "Status: DESIGN" (:13); "Skeleton: npc_character_analyses_v30.md" (:10). Reading: historical; the character-design rationale for the roster.
- **Bears on:** CHAR, FA, WR, FI, SC, ARCS.
- **Content that matters:**
  - Design method visible in every entry: a real historical parallel, one mechanical flaw tag, and an arc fork. Parallels: Sorge (Maret), Luxemburg (Vossen), Bellarmine (Haelgrund), Granville (Torsvald), Aetius (Brandt), Jacques Coeur (Feldhaus), Byzantine logothetes (Almstedt), William Marshal (Strand), Medici branch manager (Virke), Palaiologos (Laskaris), Xenophon (Solberg), Suger (Prudence Cardinal), Manuel I Komnenos (Almud), Catherine the Great (Lenneth), Reinhard von Lohengramm (Vaynard), Isabella I of Castile (Baralta) (:24-112).
  - Linked exposure chain: Feldhaus and Virke share a Thread-touched supply chain neither knows; exposing it either way cascades to both - "the most mechanically consequential NPC relationship in the roster" because it links Niflhel syndicates (criminal) to Guilds (legitimate) (:47). Whether the strike of Niflhel (edeyja_npc.md:69) broke this link is `[UNVERIFIED]`.
  - Prudence Cardinal's OPTIMISER feedback loop: Church Wealth +1/season, but Church Mandate -0.5 at Year-End per over-tithed territory and CV erosion +1 there; Parish Revolt card at ≥ 3 squeezed territories with Mandate ≤ 3 (Church Wealth -2 for a season, CV -1, CI -1); reform gives Wealth bonus +0.5/season and stops the erosion (:73-75).
  - Strand OVERPERFORMER: Crown admin +1D, but removing him collapses Crown admin for 2 seasons (:55); Haelgrund PROCEDURALIST: investigations +1 season (:35); Maret CONFLICTED: 1-season hesitation against RM targets, VTM resets to 0 if she inherits Varfell (:25-26).
  - Edeyja treated as an environmental-hazard monitor: every faction action is a "frequency" of Thread stress; "functionally omnipotent inside her domain and powerless outside" (:18-19).
  - Lenneth versus Baralta is "the campaign's defining political confrontation" (:94); Lenneth programme in stages: cultural recognition, institutional reform, Thread work last (:90); Himlensendt consecration crisis if Baralta claims the Crown (:116); Ehrenwall's Coup Counter as the deed-logic's enforcement mechanism (:127).
- **Conflicts / stale:** Elske described as married to Laskaris (:98) versus the skeleton (see above). Maret is "TS ~50" here (:23), whereas v1 assigns Maret Uln TS 0 (`npc_behavior_system_v1.md:260`) - a direct numeric conflict between v1 and v30 analyses (v1 superseded). Vossen in this set is TS 25; v1 gives TS 0. Jarnstal heading has no text (:124). The faction stat words used (Mandate, CI, CV, IP, PW, VTM, Coup Counter) are v30 board-game state; map to `engine/season` state is `[UNVERIFIED]`.
- **Open items:** Torben's text is a single paragraph (:96) and carries none of the ED-618 Conviction-window rule the skeleton cites (:210); "Southernmost Awareness 0" for Himlensendt (:119) is a stat with no definition in this set.

### .designs/systems/npcs/reference/npc_roster_v30_index.md
- **What it is:** auto-generated heading/size index (2026-04-19) of `npc_roster_v30.md` ("Valoria - Named NPC Roster", consolidated 2026-04-11; 8,680 tokens); 109 lines (read from :9).
- **Status:** records parent's "Status: CANONICAL" (:24); `canonical_sha: 30bc852ac34c` (:11). Reading: historical; no longer canon.
- **Bears on:** CHAR, FA, WR, CORE.
- **Content that matters:**
  - The roster is 13 NPCs: Edeyja, Maret Uln, Yrsa Vossen, Saemund Haelgrund (Church Inquisitor, "Cardinal Justice"), Sigrid Torsvald, Halvar Brandt, Annika Feldhaus, Peder Almstedt, Gerik Strand (Lord Steward), Dalla Virke (Niflhel broker), Doux Alexios Laskaris ("Altonian Prince (married to Elske)"), Rikard Solberg, **Aldric Tormann** (Fourth Cardinal, Prudence) (:28-40). This is the only place in my set that names the Prudence Cardinal, which the analyses doc leaves "[Name Pending]".
  - A "Mode Interface Matrix" (4,543 of 8,634 tokens, i.e. over half the parent) gives each NPC a per-mode (TTRPG / Board Game / Hybrid) section, then a "Mode Coverage Summary", "Summary Table", "Cross-Reference: Faction Axis Positions" and "Stat Blocks" (:41-59).
  - §14 "Caste System Impact on Roster NPCs": direct implications, "strengthened without textual changes", and a "Key structural finding" (:60-63).
  - Stat Blocks is 49 tokens - a placeholder (:105).
- **Conflicts / stale:** line numbers ~8 behind body; retired reader usage line (:17); dissolved path (:10). Whether `engine/season/rosters.yaml` carries these 13 NPCs by these names is `[UNVERIFIED]`.
- **Open items:** Stat Blocks never written (see infill).

### .designs/systems/npcs/reference/npc_roster_v30_infill.md
- **What it is:** prose/rationale half of the NPC roster (130 lines): per-NPC compromise, historical echo, ethics, behavioural AI flaw, mode bridges, caste-system annotations.
- **Status:** "Status: CANONICAL" in the header copy (:13) while §Stat Blocks says "Names, motivations, compromises, and behavioral profiles are provisional. User may modify any element. Stat blocks will be generated after identities are confirmed." (:112). Reading: historical, self-contradictory about status, never completed.
- **Bears on:** CHAR, FA, WR, FI, SC, SE, ARCS.
- **Content that matters:**
  - Design principle: every named NPC except Edeyja carries a structural compromise (personal ethics versus faction loyalty, uncontrolled Thread exposure, a decision flaw, or spoiler position); these are "emergent arc triggers"; each has a Behavioral AI Profile with a named flaw (:17-18). This is the clearest statement of the NPC chooser's intent: a flaw tag produces suboptimal, exploitable play.
  - Named flaw tags and consequences: Maret CONFLICTED (delays harming RM by 1 season, :27); Vossen IDEALIST (RM Presence spread thin, 5 territories at 1 versus 3 at 2, so Heresy Investigations succeed more, :30); Haelgrund PROCEDURALIST (+1 season, but Overwhelming results, :36); Virke NETWORK PROTECTOR (never burns a source; the family replaces her if it finds out, trust network collapses, :64); Solberg STABILITY-SEEKING (arms recommendations conservative, reports downplay instability, better deals to the losing faction, ~1 season behind optimal aggression, :76); Prudence Cardinal tithe maximiser (:80).
  - Feldhaus: ~15% of Guilds' luxury-goods revenue depends on the Niflhel contraband chain; she thinks it is "just contraband antiquities" (:50). Torsvald: TS 35, spent 3 seasons securing Lenneth's archive, Riskbreakers "officially do not exist" (:38-41). Brandt: held Lowenskyst pass 3 days 12 years ago; succession candidate if Ehrenwall falls, "provisional rule F-30" (:43-45).
  - Mode bridge text defines how one NPC should behave across scales: e.g. Torsvald is invisible in BG, but Deniability Debt rising "for no apparent reason" is her aborts (:95); Laskaris is "the IP clock's human face" and flips IP from slow-burn to crisis in one Accounting step (:106); Vossen exists only where RM can be player-facing (RM is mid-game emergence, not a starting faction, :91). The same NPC must have presence in at least 2 of 3 modes (:85).
  - "Niflhel is not a coordinated faction: a colloquial name for the constellation of criminal families, smuggling networks and black-market syndicates"; Virke family competes with "at least three other major syndicates (unnamed — GM discretion)" (:61).
  - Caste annotations: Strand is "more loyal to the founding logic than the founding family" (a potential ally of Baralta, Lenneth or Vaynard, :120); the NPC ecosystem reproduces the caste "through structural incentives, not individual malice" (:130); Prudence extraction "accidentally radicalising the south" and Parish Revolt has a caste dimension (:123); Vossen/Lenneth positioning is a "design gap requiring resolution" (ED-NEW-24, :116).
- **Conflicts / stale:** Niflhel here is a loose constellation of syndicates; `npc_behavior_system_v1.md:287` has a "Four-Arm Structure" faction with a priority tree, and the struck-Niflhel record is in `edeyja_npc.md:69` - three incompatible Niflhel models in the NPC set. Laskaris "whose province borders T4 (Grauwald)", married to Elske by imperial arrangement (:66) agrees with the analyses infill but not with the analyses skeleton ("Elske is in Altonia (tutoring arrangement)", skeleton :218). Maret and Vossen TS values are not stated in this doc; v1 and analyses disagree (see above). "GM guidance for TTRPG" (:18) and "GM discretion" (:61) are no-GM-engine residue.
- **Open items:** all stat blocks (:112); ED-NEW-24 Vossen/RM split on Crown patronage (:116); the Summary Table and Faction Axis Positions headings have no content in the infill (:82-83) - they are in the skeleton `npc_roster_v30.md` (not in this assignment); Maret's "Succession Fallback" activation rules.
