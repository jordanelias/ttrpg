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
