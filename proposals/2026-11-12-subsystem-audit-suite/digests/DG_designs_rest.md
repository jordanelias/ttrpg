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
