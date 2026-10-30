# Valoria: content, characters, factions, settlements, playability, events, arcs

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Part 01 of the suite, first of two files (this file holds the title block to the end of section 9; `01_MAIN_REPORT_part2.md` holds sections 10 to 15), split at a section boundary because the whole was about 58 KB (CLAUDE.md §4). Base: `main_clean.md`, the pre-review text, which is identical line for line to the session's reads of 07:11 (`read_071122_01_MAIN_REPORT.md`, line numbers stripped) and of 07:22 (`read_072240` lines 1 to 250 joined to `read_072245` lines 251 to 357); the session's earlier section 11 rewrite (`heredoc_070736`) is already in that base and was not replayed. Patch scripts replayed in time order against a copy, each with its asserts, all applied: `heredoc_072531` (glossary paragraph and related edits), `heredoc_072607` (what a seat can order depends on its remit; the 754-conflict sentence), `heredoc_072811` (the `04:793`/`:802` to `04:801`/`:810` sweep). None failed. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This directory is a reconstruction from the session transcript's surviving reads and patch scripts, not the original files. Recovered in a second pass (2026-10-30), each with its own provenance: parts 05 and 07a to 07d, and the lens-3 (directive-compliance) critic report (`critic_lens3.md`). Parts 06 and appendices A1 to A5 are recovered in the third pass (see `00_INDEX.md`). Edits the session made by tools other than Bash heredocs (Edit-tool calls) were not captured, so the text may differ from the session's final file in ways not recorded here. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

*Part 01 of the review suite (see `00_INDEX.md`). Revised after the conflict adjudication (parts 07a–07d): where the first draft and the adjudication differ, this text follows the adjudication.*

Repo state: `ttrpg` at be24c71 (B10-02 closed, 2026-10-28); `valoria-game` at 6b0df3d (2026-08-19). Method: 43 cited digests of about 3 MB of source (cheap readers, no judgment), then five analysts who re-opened sources for every claim they relied on. Where the old design corpus and the code disagree, the code and the newest ruling decide. Tags: BUILT executes; PLANNED in adopted v10, unbuilt; PROPOSED held design; NEW from this review; [RETIRED] a mechanism the current architecture refuses.

**Words used throughout, once.** A **person** is any character, named or a cohort of many. A **seat** is an office a person holds (King, Confessor, Lord Steward). A **rung** is a place in the realm's nesting (realm, territory, settlement); "rung 1 or 2" means a seat near the top of that nesting, such as a cardinal or a steward; which orders a seat offers depends on the seat's own list of acts (its remit), not its rung. A **verb** is an act the game resolves (`tell`, `research`, `confer`); a **verb row** is its line in `verb_table.yaml`, saying who may do it and what it writes. A **claim** is one thing a person believes, and a **ledger** is the list of claims a person holds. A **Record** is a document in the world (a petition, a finding). A **Proposition** is a statement people can commit to (a creed). A **Tenure** is a held relationship (holding a seat, living somewhere, being sworn to someone). A **field** is a value stored on a sheet; a **query** is a question the game asks fresh each time (§6 explains). `content_hash` is a fingerprint of the whole world state, used to prove two runs are identical.

---

## 0. The picture in one page

**The engine is a lawful society simulator, not yet a game.** A seeded realm of 83 persons (46 named), 37 settlements, 32 offices and 38 goals runs seasons in which persons choose acts and the engine resolves them. It has no human seat, no authored events, no attribute values, no storylines and no words. The plan (workplan v10) reaches a clean, ported simulator and says so: "Content is not the plan's to author" (`workplans/valoria_master_workplan_v10.md:129`).

**Why it is built this way.** The axioms (`architecture/meta/01_AXIOMS.md`) make one commitment that explains most of what you found hard: *only a person acts* (AX-1), *every value has one owner and only its owner writes it* (AX-4), so an aggregate cannot be a field, only a computation (T-a). A faction is therefore not an actor (T-h); the design makes it a creed plus the people committed to it (a design claim in §D.5, not a derivation); and a settlement is a place whose "stats" are queries. The purpose is authorship: every change in the world has a named author, so stories have causes. It is not a flexibility device, and it has a stated price: the old arcs, "authored against a model with faction meters, world tracks and a GM", are "unrunnable, deliberately" (AX-1).

**Five structural gaps, in the order they block play:**
1. **No seat for a human.** One test-only callback (`dispatching_chooser`). Nothing in v10 schedules a client before the port gate.
2. **No capability.** `Person.capability` is empty on 83 of 83; everyone rolls 2 dice. 1 of 46 cast rows carries any attribute value.
3. **No authoring layer.** Persons are records; factions and settlements are scattered across 8 to 12 files keyed by name. You cannot author or catalogue them.
4. **No situations.** There is no event or storyline carrier. Two seeds differ only in random draws.
5. **No words.** The only rendering is a one-line chronicle. A full voice specification and a seven-scene scenario exist in the prose-writer skill and connect to nothing; its five tiers are keyed to the old Coherence scale (10 coherent, 0 crisis), which ED-WR-0010 retired, so they need re-indexing before they can drive text.

**What the design corpus is worth.** About 3 MB of design describes an older model. The mechanisms are mostly [RETIRED]; the stories, cast, places and precedents are reusable. Your note that some of it is superseded is right and large: see §10.

**Three decisions you gave this session** (recorded as yours): agents may draft `[ASSUMPTION]`-tagged content for you to edit (each with a revert); a text-first playable slice (**B10-S**) goes into the plan before the port gate; the first playable person is seated at rung 1 or 2.

---

## 1. Q1: How much content does the game have, and what is missing?

| Layer | Verdict | Evidence |
|---|---|---|
| Carriers (structures that can hold content) | **partial** | strong for persons, offices, tenures, information; none for events, kit, troops, text, arcs; bonds have a carrier (`tie` and `knot` Tenures) but the verb is declined for want of a partner operand (H-182) |
| Content (data present) | **thin** | 46 named persons, 17 provinces, 37 settlements, 38 goals, 2 endings, 74 place descriptions; nothing varies by seed beyond dice |
| Player surface | **none** | `valoria-game` is 8 bare scenes, no art, audio or dialogue, on the retired Key substrate, reading nothing from the engine; it also holds 22 character and 15 trigger resources on the retired model |
| Narrative text | **none in the game** | `harness/chronicle.py` prints one instrument line per act, wired to no gate; the prose-writer skill's tiers use a retired Coherence scale |

Measured: `build_realm(0)` gives 83 persons, 32 offices, 322 sites, 67 Propositions; 56 verb rows, 51 resolvable; requirements met 3, partial 5, not met 1.

**Does v10 contain a path to a playable game? No.** The words "vertical slice", "playable slice" and "first playable" occur nowhere in the plan. No client, no un-held text layer, no content authoring and no halting ending are scheduled; Godot (B10-20) comes after eighteen serial batches, in a repo that reads none of the engine.

**Missing, split by who must act**
- (a) *Scheduled engine work:* the refusal rate (in the one stored two-season run at seed 0, 327 of 1,132 attempted acts produced an event other than a refusal, `proposals/2026-10-22-system-description/ctl/realm_seed0_2seasons.txt:1-40`; the largest scheduled block), attributes (B10-10), odds (B10-08), the Tensions receiver, bonds (B10-15).
- (b) *Content the plan assigns to you:* the 46 attribute sets, weather values, thrust ladders, heritage, lifepath key map, Tensions cards.
- (c) *Nobody provides:* a client, a text layer, freestanding storylines, a loss state, a companion mechanic, save/load and onboarding, POI names.

**Repair, one position: B10-S** (after B10-10, so attributes exist when the seated person rolls; before B10-11): text-first Python over `dispatching_chooser`, one seated person; screens for what the person knows, a menu with odds, and the result with refusals in plain words; stops on the person's line ending or season 12; control is a scripted-callback-equals-chooser hash test (the REM-31 pattern). Approved by you this session. [GAP: whether a boot-time date can be written without an act's token is unchecked; only `convene` writes dates today. Read the build path before B10-S.]

---

## 2. Q2: Attributes, prowess, verbs, precedent

**Verdict.** The plan's shape, nine attributes on a 1–7 scale plus Thread Sensitivity (TS) as a practitioner stat, with capability one function of them, is a workable default but not a finding: the built evidence cannot separate it from the alternatives. It is v10's shape (M2, CR-20, ED-IN-0301); none of it is built (the plan's "LANDED ALREADY: faculty" is wrong at HEAD: `faculty` appears nowhere in `engine/season`). Three coherent attribute proposals, plus a ten-score variant (split Attention into Perception and Insight, fold Focus into Will, keep Bonds, count TS), are in part 03 (P2). You rule on them (§11, item 2). Reopening the ten-score question is cheaper than it looks, because the variant passes the demand tests without overriding ED-IN-0185.

| key | definition |
|---|---|
| STR, END, AGI | force; what the body bears; speed and balance |
| FOC, ACU | holding attention; reasoning and reckoning |
| WIL | resolve; holding a course |
| ATT, CHA | noticing and reading people; bearing and voice |
| BON | capacity to hold ties |
| TS (0–100+) | perception of the threads; BUILT as `Person.thread_sensitivity` (set at build, written by nothing in play), gate 30; counted as the tenth by letting the roster point at this existing field (ED-IN-0301 confirmed the default that the tenth slot refuses a value, so this reopens it) |

(Definitions are the analyst's; names, scale and groups come from `references/descriptor_registry.yaml:33-48`.)

**Prowess** := `faculty(p, verb)`, the dice a person brings to a contested verb. It supplies dice and gates nothing (J-13); the opponent's score halved sets the Ob.

**How verbs relate.** A verb never names an attribute (`verb_table.yaml` has no such column). It names a capability key (`verb_capability`); a table (`vocation_attribute`, PLANNED) names the attribute that key rests on, with an optional `resist` column (NEW) so a hearer resists a tell by reading people, not by presence. An attribute reaches a verb only if its row declares `contests:`; uncontested verbs differ by remit, holdings and information. Examples: fight (STR/AGI/END/ACU/FOC through the combat module); tell (CHA vs ATT); argue (ACU vs WIL); thread_read (WIL + ⌊TS/10⌋); march (Command is derived from Charisma and Cognition, clamped 1–7, `exchange.py:55-64`, and does not enter the dice pool); confer, issue and revoke carry no attribute.

**Precedent.** "Attribute base plus learned skill, capped" fits d10 pools (Disco Elysium, Bannerlord: from the repo's research digests). Lifepaths work only as creation templates. Class and level systems, and full attribute-plus-skill sums, do not fit a closed cast and risk pushing pools into saturation. Burning Wheel and Traveller as lifepath models are from memory.

**Decision needed (amends ratified CR-20).** CR-20's `max(key, attribute)` hides training for anyone talented. Recommended: `faculty = attribute + min(cap, max(0, key − pool_default)) + practice`. Revert: `max`.

"Aptitude" is retired as a word (three senses; `proposals/2026-10-16-attribute-derivation_aptitudes.md:8-14`).

---

## 3. Q3: What is a character?

**Template.** One `Person` in four layers on identity and position records. About 20 fields, 13 BUILT.

| Group | Fields | Status |
|---|---|---|
| Identity | id, name, weight (a cohort is a Person at weight > 1), born, heritage | built; heritage PLANNED (CR-30) |
| Position | tenures: office = hold, faction = commit, home = reside, oath = oblige, ties | built; faction and office are derived |
| 1 Capability | attributes (nine); capability keys + train; TS; body; kit | attributes PLANNED (CR-20); capability built but empty; kit a GAP (take: a hold Tenure on an item) |
| 2 Ambition | commits to OUGHTs seeded by `goals.yaml`; thrust ladder | goals built; ladders PROPOSED |
| 3 Values | pursuits (15), stance, conviction (5 affiliations), scar | built and scored; conviction and scar inert at weight 0 |
| 4 Personality | offsets on rigid/flexible, grandiose/humble, deontological/instrumental | PROPOSED |
| Knowledge | ledger (the View, at most 12 claim ids) | built |

**Histories** grant starting state and are never stored on the person. CR-33 expands 34 vocation rows into capability keys; NEW: all four stages (origin, formation, vocation, catalyst). The **catalyst** stage seeds one authored OUGHT with a ladder, a want not derived from office or faction. That is the storyline hook (see §7).

**Progression.** Practice (built `train`, PLANNED windowed practice), values erode (scars, pursuit shifts), body wears. Proposed: attributes change only with age and permanent wounds, never by use.

**How a character chooses (from the code).** Question (the head of `questions_for`) → View (≤ 12 claims) → budget (5, plus 1 per live `hold` Tenure including Records, minus body bands, minus travel legs, at least 1; at most 5 scenes can be released in a season, `loop/deliberate.py:85-113`) → options (the verb table filtered by own, remit, hold, presence, TS) → score Σ axis weight × verb alignment + 2 × stance toward the subject → softmax draw at τ = 0.1. In plain words: **values pick the verb, stance picks the target, the question picks the matter**, and the draw is weighted, not forced. The score ignores capability, odds, goal text, scars and conviction. The engine chooses every act; a player can only replace the whole chooser. The code departs from `npc_behavior_v30` (a deterministic priority tree, GM crisis table, Self-Other), which is [RETIRED].

**Decision (recommended): build personality behind a spread-0 control.** It is the only layer that separates two persons sharing a faction and an office, which answers your sameness concern. Falsifier: spread 0 leaves `content_hash` equal.

---

## 4. Q4: What is a faction?

**Verdict.** Not a record with stats. In plain words, a faction is a creed (a statement) plus the people who have committed to it; everything else about it is asked fresh. In the code's words, a creed `Proposition` plus the live `commit` Tenures to it. In code it is a frozen five-field view (`proposition, members, holdings, seats, head`; `queries/faction_q.py:84-96`); `head` is `None` for all because nothing writes `Tenure.degree`. Measured members/held rungs/seats: Crown 11/6/11, Church 7/1/7, Hafenmark 4/4/4, Varfell 5/4/4. The old four hold land; the cast is eight canon factions plus Altonia (off) and the test faction `faction x`.

**Template (all stats are queries):**

| Tier | Fields |
|---|---|
| Identity | name (naming index), creed, role template (6 of 9 present), founding leader, foreign flag |
| State | members, leaders; standing per viewer (`person_q.legitimacy`, never one number); strength (`mustered`); cohesion and wealth (NEW queries) |
| Relations | war (`at_war`, no producer in play), treaty (`covenant`, tests only), service chain |
| Holdings | land, seats, sub-organisations (`office_bodies`) |
| Behaviour | goals members commit to; decisions are each member's own chooser |
| Colour | mission text, culture, foils (design) |

**A faction has no action menu.** The holder of its seat acts: `issue`, `covenant`, `requisition`, `seize`, `transfer`, `confer`, `establish`, `revoke`, `determine`, `open_case`, `pardon`, `dispatch`, `march`, `arrest`, `convene`. Missing: `declare`, `recruit`, `conspire`, and the effect of `succeed`. There is no `levy` verb, but the troop levy feed is built and shipped off (`requisition` into a treasury, then `settlements.provision` into the field; `field_provisioning=False`, H-241). Canon "unique actions" become seat verbs (Royal Decree = the King's `issue`; Excommunication = Church `determine` plus ban).

**Retired:** the 6-stat block (`fac.*`, 29b), faction AI, and `stats_1_7_scale.md` (gone from the tree). `registers/supersession_register.yaml:22-28` still calls `fac.legitimacy` live, which the code contradicts: plan position 29b (`references/restructure_ledger.md:2687`) supersedes it, so the row should be closed.

---

## 5. Q5: What is a settlement?

**Verdict.** A `Rung` of kind `settlement` under a territory, typed by its geography row, with quarters and buildings from `venues.yaml`; no `class Settlement`, and none should be added. 37 settlements across 16 territories (T15 Askeheim has none): Town 15, Village 14, Seat 2, Fortress 2, City 2, Fortress-City 1, Cathedral-City 1.

**Four gaps found in the build:** the settlement's cohort has empty `pursuits`, `stance` and `conviction` and holds no `commit`, so the people have no politics; no seat sits at any settlement (the Mayor title is ruled but unseated, so 4–14 territory, duchy or realm seat-holders govern each town); the geography file's Prosperity/Defense/Order are never read; the `set.*` descriptors are loaded and read by nothing.

**Template:** identity (id, parent, geography row, type); state (population, capacity, larder, defence built; prosperity and holder-standing NEW queries; unrest designed, CP-T08-06); relations (holder faction, adjacency data unread); holdings (governors, local seat, Sites, treasury as `stores`); behaviour (eat, produce, wear built; standing edicts designed); colour (Goldenfurt's 6 + 3 dossiers and 28-card deck: archived design).

**Minimum viable settlement:** seed each cohort's motives from existing fields; use the geography triplet as build-time seeds only; add `prosperity`, `standing` and build `unrest`.

**Generated or authored.** `build_realm` already is the generator (geography row + `venues` template). Extend it; do not build the VSG paradigm-stack generator. Of the VSG stack, the built layers are location, starting faction, type and infrastructure; piety, economy and temperament become seeds on existing fields; the Altonian and caste scalars, governance type and allegiance die or become queries.

**How other games let a player run a settlement (what is decided each turn, what comes back).** Romance of the Three Kingdoms XIV assigns an overseer and a priority to each area; the overseer's stats set the yield (repo digest T13:47, :78). Knights of Honor II yields 100% under a governor and about a tenth without one (T13:251). Crusader Kings 3 gives each councillor one standing task and the player sets policy (R1:81-84). Manor Lords, Frostpunk and King of Dragon Pass [FROM MEMORY] run a town by allocating labour and stores and answering events. The common shape: **a few standing choices per place, a person who carries them out, and a visible result next turn.** For Valoria that is the management console of part 04 (P3-B): the holder's orders on stores and appointments, the delegate's own chooser doing the work, and the next season's account showing what changed.

**Action menu.** Develop/fortify = `work`, `build`, `restore` (inert on dwellings and garrisons: no floors); Hold Court = `convene` → `open_case` → `determine`; Sponsor = `transfer`; Levy = `requisition` (goods built, men missing); Investigate = `examine`, `interview`, `surveil`. Missing: Tax, Ration, Proclaim, Craft; `patrol` parked until `unrest`.

---

## 6. Structural answer to "I can't directly associate data to a faction"

**Fields and queries, in plain terms.** A *field* is a line written on a character sheet ("Military: 5"): stored, easy to open and edit, but someone must keep it correct. A *query* is a question the game asks fresh each time ("how many people committed to the Crown hold arms right now?"): always right, nothing to update, but no card to open. A person is mostly a card. A faction's strength, wealth and standing are questions with no card, by rule.

You are right, and the cause is a mis-scaling of a correct rule. AX-4 (through T-a) forbids aggregates as *fields*; it does not forbid authored *facts*. Today "Crown" appears in twelve files keyed by one string, and no file answers "everything about Crown".

**Recommendation (NEW; needs `layer-conformance` before building):** keep the runtime model. Add an **authoring layer**: one dossier file per faction, settlement and named character (identity, role template, creed, starting offices and holdings, goals, relations, descriptive text), read at world build and compiled into the same Propositions, Tenures and Rungs the engine uses. Add a read-only **dossier report** that prints the authored file beside the live queried view (members, holdings, strength). This follows CLAUDE.md §0.05/§5 (a fact the engine uses lives in a typed artifact code reads). Unchecked against Layer 1 rules S10.1 and 04 row 27a (proper nouns in the content layer).

---

## 7. Q7: Event decks

**Verdict.** No event deck or card carrier exists in code (zero hits), and none should be built as a per-season deck. The Tensions deck is 6 cards, draw 1 (the plan: `workplans/valoria_master_workplan_v10_part4.md:526-527`, `_part6:217`; early_game's 8–10 draw 2 loses); its six cards (Royal Crisis, Feldmark Famine, Cardinal Independence, Guild Fracture, Einhir Incident, Ministry Crisis) are unbuilt commits in B10-18, and `tensions.yaml` does not exist. Jordan's "45" cards is 6 Tensions + 28 Goldenfurt + 11 named; the grounded deck's "58" is its own claim (50 ids named, 8 written in full) and is not part of the 45. The plan's CL-EVENTS ships off.

"Event" means three things: world forcing (matter, bodies, fading memory; actorless, writes no outcome; weather is currently a constant 1.0); person-driven acts (the bulk, built); authored situations (goals built; Tensions planned; scenarios proposed).

**Best existing template: Goldenfurt (28 cards, 7 families, archived).** It survives with cuts: keep `id/family`, the base weight (drawn at build), cooldown/excludes (as draw-without-replacement), role slots on seats, `the_ask` as the question to a named person, the existing verbs as responses. Cut the Π pressure meter, authored effects, Ledger tags, the Directive generator, and `pressure_if_ignored`; split `triggers` into a build-time eligibility query plus a band on the opener's own ledger.

**What events attach to:** a person (goal row, body), a seat (whoever holds it), a place, and the world only at build. Never a faction (via its seats) and never a season.

**The rule on cards** is the "May not be data" list for a Tensions card (`proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-18.md:183`, M20's line applied to a card): a card may not carry a date, a deadline, a firing condition, an outcome, a write to standing, a seat, a tenure or a stance, or a `closing`, `successor` or `deal` key. The only effect kinds are `goal` and `yield_scale`, and the world draws **one** card, equally likely (B10-18:183, :199). `workplans/valoria_master_workplan_v10_part12.md:275` applies the rule: the eleven named cards fail because their effects write aggregates or outcomes by fiat.

---

## 8. Freestanding storylines (your directive)

**In plain words:** a storyline here is a bundle of starting wants and one starting piece of knowledge attached to a seat or a place, drawn when the world is built, so that worlds differ; nothing in it is a date or an ending, and only a person's own choice ever starts it. The rest of this section says why that form, and not a fuller script, is the one the standing rules allow.

You said 100% emergence from characterization, office and faction will produce too many similar stories. The repo has no measurement of story variety, so the concern is untested; the plan's own words are that emergent range is "unmeasurable, not zero".

**Verdict, corrected after the critic pass and the adjudication.** A scenario can be made to fit, but my first draft broke standing texts and named only one. The first draft's row carried a firing condition and a fuse that writes dates. Two of the three collisions need an amendment; the third (ED-IN-0225) is already answered.
1. **B10-19's "must NOT" list:** no arc carrier or stage store; "deal arcs per season (the deck is world-gen only)".
2. **The "May not be data" list for a card** (`B10-18.md:183`, M20's line applied to a card): no date, deadline, firing condition, outcome, write to standing, seat, tenure or stance. The first draft's `opens_on` is a firing condition, and its T-c basis ("nothing a card authors falls due after build") fails for a row that opens mid-game.
3. **ED-IN-0225** (Jordan, 2026-09-13: "Maybe we just ignore the arcs now.") and `part12:276`. **Answered, not a question for you:** ED-IN-0225 refuses only an arc *carrier* (archive `:3209-3237`), M20(b) already narrowed it, and the plan already quotes arcs as provenance (B6.n ladders name their source arc, `part12:276`; Tensions rows quote archived lines in `source:`, `part4:527`). The fix is a plan-text amendment: change `part12:276`'s "no arc is a carrier, a card field or a loaded row" to "…a carrier or a loaded row; a row may quote one in `source:`". A provenance string changes no behaviour.

**The reduced form that fits what exists.** A scenario is a *bundle of goal rows*, the one effect kind a card may already carry (`goal`, parsed with `goals.yaml` by `data/goals.py::parse`), bound to roles by query, plus one claim seeded at build in one ledger. Nothing on the row is a date, deadline, firing condition or outcome. The opening is person-side: the opener's existing question machinery decides whether the person acts. The opening act is an existing verb (`open_case`) that mints a staged Record, and the act declares the term, so T-c is satisfied by the act and not by the card.

| On the row (world-gen data) | Person-side (not on the row) |
|---|---|
| `eligible`: a build-time query; a failing row is not drawn | whether the opener acts: the opener's ordinary question machinery on the goal row; a band on his own ledger that raises the question is B4.1, which the plan holds with no owner, and is not on the row |
| `roles`: queries to existing persons (a seat, so it rebinds through tenure); unbound means not drawn | the opening act: the opener's own choice among existing verbs; the verb, not the row, declares the stages (`open_case`, `verb_table.yaml:963`) |
| `goals`: role-bound goal rows (the question each role receives) | `beats`: each role's choice; the menu is the whole verb table, with no whitelist |
| `seed_claim`: one claim in one ledger (check against AX-7: a build-time deposit) | `outcomes`: none authored; only degrees of existing verbs |
| non-repetition: at most one row per family per world; the gate refuses a second live Record of the same kind and subject | |

**Worked instance:** Rendstad. A Church assessor arrives in a Hafenmark settlement over a folk practitioner. The foreman's claim sits in the Doctrinal Compliance seat's ledger and the seat's goal row makes acting on it a question. If the seat-holder chooses, `open_case` mints a Record (today it mints kind `text`, `effects_information.py:286-287`; a Record kind `assessment` is NEW, and its stages are declared by the act's payload, not listed on any card). The sub-prefect may comply, defy or petition the Duchess; the Duchess may counter-writ or do nothing; the hearing is decided by a judge or argued. Endings are chosen only by persons. Scenes 4 to 7 (the protagonist's Thread Sensitivity) are render-only and wait on the text layer.

**What this needs beyond today.** (a) Widen the Tensions card schema from one `goal` effect to role-bound goal rows plus one seeded claim, keeping the "May not be data" list intact. (b) Amend B10-19's clause so the world-generation draw may include scenario bundles: *"deal arcs or scenarios per season by any emitter: no loop step mints one; a scenario is world-generation data read once by `build_realm`, opened mid-game only by a bound person's own act."* (c) Amend `part12:276` as in collision 3 (a plan-text change).

**How many.** If a world draws k scenario bundles from a pool of P, the expected overlap between two worlds is about k²/P, so P of at least k² keeps it under one (k = 4: 16 rows; k = 6: 36). The plan draws one Tensions card per world, so a world with four scenario bundles draws five and the pool needs 25 or more. First slice: 8 rows. Seeds that exist: SCN-01..15 (`cases/ARC6.yaml`), NSC 2/6/8/9, the six Tensions, Goldenfurt, Rendstad. Arc-derived seeds (the nine NEVER arcs, 05/16/24/25/26/28/36/38/39, all among the numbered 55; and arcs 10/14/18) may be quoted as `source:`; some were struck by canon (PP-675; Niflhel dissolved), so each needs a canon re-check. Runtime-generated: zero (variety comes from binding). King of Dragon Pass ships 544 authored events (repo digest T16).

**Layer note.** AX-5's "a world-generation roster is not a clock and is lawful" is about individuating persons, and B10-18:183 itself cites it "by analogy only". That a scenario bundle is lawful rests on T-c and on the reduced form above; I treat it as an inference to confirm.

---

## 9. Q8: The 55-arc register

Corrected scope: the 55 are the numbered register of 2026-06-28 (source recovered from tag `v30-snapshot-2026-06-28`; copied to the scratchpad, repo tree untouched).

**Verdict.** The stories survive; the mechanisms do not. The August exercise scored each arc on MECHANISM and STORY separately. Recounted from the lane headings (the synthesis's own totals, 40/2/22/10/9, cover a larger scored set): 31 reproduced-better, 2 reproduced, 16 transformed (49 survive as stories); 4 lost (5, 22, 27, 48); 2 never worked (19, 52). In code, 1 of 50 traced arcs plays (ARC-06); the `cases/ARC-*` files are test scaffolds, not arcs. Every ambient track, CI/MS faction scalar, auto-firing threshold and GM call in the register is [RETIRED].

**What reaching them takes, by family** (arc counts from the family table; low confidence, not traced):

| Capability (family) | Arcs needing it (register numbers) | Plan provides? |
|---|---|---|
| A summons hook: a person's private estimate crossing summons someone (CL-THRUST B4.1; family B) | 3 4 17 34 47 55 as primary need; 19 arcs in all (those whose ending is forced by a threshold) | no: held with no owner |
| TS gain and Coherence on persons (G) | 2 9 26 28 29 30 32 35 39 41 51 54 (12) | no: TS is on persons (10 cast rows authored, 4 pass the gate) but nothing writes it in play, and Coherence has no carrier in the season loop |
| A standing venue that decides (A) | 6 10 13 18 19 21 31 49 52 (9) | partial (`determine` executes in 3 of 43 cases) |
| A world Thread substrate (H) | 5 22 27 33 42 43 48 (7, including all four lost) | no |
| Mass opinion moved by witnessed acts (I) | 1 14 36 44 46 50 (6) | partial |
| Covert action and revelation (E) | 8 12 15 16 37 (5) | partial |
| Foreign polity as persons (D; `foreign` switch, off by your 2026-10-26 confirmation) | 20 25 38 45 (4) | built, held |
| Battle and wounds carrying over (F) | 7 23 53 (3) | partial |
| Succession (C) | 11 24 40 (3) | yes (IN-61, CR-35) |

Arc titles are in the register copy (`scratchpad/arcs_src/designs/arcs/`). The earlier gap register of PR #506 (G-01..G-29, `proposals/2026-10-24-master-workplan-v10/ctl/coverage_check.py`) is the plan's own list of what these capabilities lack; G-09/G-10/G-26 (goal rows and ladders for domestic seats) and G-21 (the Thread substrate) are the ones above.

**Reachable:** about 17 as the plan stands; about 36 with the summons hook owned, TS on persons, and scenario rows plus authored ladders (`foreign` stays off); about 40 if `foreign` is turned on; about 47 with the world substrate. All are family-level estimates. Arc 19 never worked (a pure phase ordering; its dilemma survives as the one-act rule); 5, 22, 27, 48 die unless the substrate is built; 52 needs a councillor venue.

**Where the arcs go (subject to ED-IN-0225: arcs are never runtime data):** the nine NEVER arcs (05, 16, 24, 25, 26, 28, 36, 38, 39) and arcs 10/14/18 are candidates for scenario bundles, quoted as `source:` (ED-IN-0225 permits this once `part12:276` is amended); arcs that resolve by a decider or a roll become person-side ladders (`goal_stages`); the NPC arc maps (A/B/C; Vaynard A and B lost their bodies in the v30 copy and are recoverable from `.designs/systems/npcs/reference/npc_behavior_system_v1.md:496-506`) transcribe as goal rows and ladders; the register stays a calibration corpus. The thrust ladder content is yours to author and has no builder. CL-THRUST's first piece (the ARC reader, `harness/arc.py`) is already built, although the plan still says "Built so far: nothing".

---
