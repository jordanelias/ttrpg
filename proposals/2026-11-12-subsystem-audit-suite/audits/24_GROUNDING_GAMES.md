# 24 · Grounding: the suite's claims about how other games work, each traced to a repository source

## Status: REFERENCE (a grounding pass over documents that already exist; resolves nothing at runtime, CLAUDE.md §0.05; queues nothing)

## Read at: `c68d697` (working tree, 2026-11-12). Sibling lanes were inserting `Grounded:` lines at file heads while this was written, so a suite line number below may sit one or two lines off.

Jordan, 2026-11-12: *"All ungrounded information should have info available on repository."* *"Do not
guess."* (`AUDIT_BRIEF.md:61-71`.) This file takes every place the suite (`audits/`, `proposals/`, `unified/`,
`digests/`) leans on a statement about how a game works and settles each one of three ways: it already cites
a repository research note (cited, sampled); the repository held a note the suite missed (pointed to); or the
repository held nothing, in which case the claim was sourced on the web and a note was filed under
`research/game_precedent_suite/grounding/` so that the claim now has a repository path, or it was not
found and is listed in §5 as unsourced. Research is tier 3 (`research/00_INDEX.md` §1): it informs design and
settles nothing. A figure is quoted only where a source read in body states it.

Tiers used here (the precedent suite's, `research/game_precedent_suite/README.md`): **V3** page body read
(by this lane: raw wikitext or page text fetched and read; not a model's summary of a page); **S3** search
snippet only; **M** memory; **?** not established. External requests carried game search terms only.

---

## 0. Result

| | count |
|---|---|
| claim groups inventoried (one group = one statement about a game, with every suite site that makes it) | **63** |
| already grounded in the repository by the suite's own citation (§2; about forty line citations opened across §2 and §3, all resolve and say what the suite says) | **33** |
| grounded from the repository where the suite had not cited it or had marked it memory-grade (§3, status REPO) | **6** |
| newly sourced on the web and filed as repository notes (§3, status FILED) | **11** |
| partly sourced: the shape is filed, a named part is still open (§3, status PART) | **7** |
| still unsourced: to be marked or dropped (§3 status OPEN; §5 lists them by topic) | **5** |
| no claim made (Heavy Rain) | **1** |
| corrections: a suite statement a source contradicts, or a wrong sourcing grade (§4), applied in place | **8**, in 12 files; 3 more files gained a pointer line only |

Eleven research notes were filed (§6). No suite finding, resolution or proposal changes: the corrections alter
what a precedent may be cited for, and in two cases remove a precedent from the support of a claim that
stands on its other sources.

**The three that matter for design decisions.**

1. **Ogre Battle is now sourced** (`grounding/ogre_battle.md`). The mass-battle addendum's three memory-grade
   statements are confirmed: squads of at most five; the player picks one tactic per unit and does not control
   the fighters; a member's row decides which action he takes. The squad-grid proposal declined the row rule
   "because nothing in the tree sources it"; that reason no longer holds (the decision is the MB lane's).
2. **"Football Manager is one engine at three fidelities" is still not established**, after a second attempt
   (`grounding/football_manager_instant_result.md`). Three suite files stated it as fact; they now carry the
   qualifier. The one-resolver rule does not need it: it stands on Jordan's ruling 1 of 2026-11-12.
3. **Two detective claims were wrong as written.** Sherlock Holmes: Crimes & Punishments is not "never
   corrected": the game offers an optional reveal and a replay. Spelunky does not "reject or repair" a level
   with no path: it lays a guaranteed path first and fills in around it.

---

## 1. Method

1. `grep -rnE` over `audits/ proposals/ unified/` for about 130 game titles gave 425 lines in 64 files;
   `digests/` gave more, and every digest line is a summary of a repository file, so a digest's game claim is
   grounded by construction in the file it digests and is not listed again.
2. `grep -rnE` for the tier marks (`[M]`, `[S2]`, `[S3]`, `[UNVERIFIED]`, "from memory", "memory-grade",
   "snippet", "not sourced", "unsourced", "not established") gave 401 lines, almost all about the engine
   (lane 25's subject). The ones about games are §3.
3. Each game claim was read in its paragraph and sorted: cites a repository research path (§2); marked
   memory, snippet or unverified, or stated with no source (§3).
4. For §3, the repository was searched first: `research/game_precedent_suite/` (tables, tutorials,
   dispositions), `research/by_lane/`, the companion, `research/emergent_narrative_literature/`.
5. Where the repository held nothing or a self-graded row, the claim was sourced on the web and filed.
6. Corrections were applied in place, each edited file given a `Grounded:` head line. No text of another lane
   was deleted: a corrected clause keeps its original words and gains a bracketed correction.

**What "grounded in the repository" means for the game tables.** `research/game_precedent_suite/` is itself
tagged per cell; many cells are `[M]`. A suite claim citing a table is grounded only as far as the cell it
rests on is `V2`/`V3`. Where the suite carried a table's `[M]` forward honestly, that claim is in §3, not §2.

---

## 2. Claims the suite already grounds in the repository (33 groups)

Each row: where the suite says it, and the repository source it cites. **(v)** marks a citation this lane
opened at the line and found to say what the suite says.

| # | suite site | claim, in short | repository source the suite cites |
|---|---|---|---|
| GA-01 | `audits/01_CORE_audit.md:438` | Dwarf Fortress simulation principles; RimWorld's storyteller | `research/emergent_narrative_literature/04_*` (G13, G14) |
| GA-02 | `audits/02_CHAR_audit.md:572-588` | RimWorld memory read at a decision; Old World ambitions; CK council-seat grudge; Jagged Alliance bands | `research/by_lane/NPC_npc_cast.md` rows as cited |
| GA-03 | `audits/02_CHAR_audit_addendum_B.md:133-135`, `:588-640` | Disco Elysium passive checks (skill + 6, no dice; about ten thousand of them); Thought Cabinet; Pentiment's remembered choices and thresholds | `tables/R4` (v: `R4:34`), `tables/R5` (v: `R5:52`, `:74-75`) |
| GA-04 | `audits/03_PC_audit.md:446-462`; `proposals/03_PC_exits_withdrawal_recovery.md:98-99` | Griftlands surrender and spare-or-kill; Kenshi and Jagged Alliance 2 capture; Wildermyth's mortal choice; Kingdom Come's improvement by doing; shown odds in XCOM, Battle Brothers, Baldur's Gate 3 | `dispositions/D_T03.md` rows 5, 8, 17, 22, 25, 27, 29, 33, 36, 39 |
| GA-05 | `audits/03_PC_audit.md:454-455`; `audits/03_PC_audit_addendum_B.md:52`, `:218-222` | a character layer the campaign does not read becomes decoration; Total War's auto-resolve; a plan set before the engine resolves (nine games); Unicorn Overlord's Tactics | `research/by_lane/PC_personal_combat.md` T-PC-7, T-PC-8; `THROUGHLINES.md` P36; `tutorials/T19` (v: `T19:104`, `:146`) |
| GA-06 | `audits/04_MB_audit.md:813-829`, `:840`, `:851-857` | the pre-battle panel; a priced exit; levy against professional; occupation then title; strategy selection in one-clock games; Total War's wipe-out thresholds and Ultimate General's routers (both marked leads there) | `dispositions/D_T04.md` rows 3-11, 23, 34, 40, 46, 55, 58; `research/by_lane/MB_mass_battle.md` T-MB-4, -5, -12, -14; `tutorials/T07`; `tables/R6` |
| GA-07 | `audits/04_MB_audit.md:1345-1363` | Unicorn Overlord squads, Tactics, stage preview; Football Manager's loop and menu; Total War's campaign; Bannerlord recruitment, upgrade, simulated battles | `tutorials/T19:79-155`; `tutorials/T16:5-40`; `tutorials/T07`; `tables/R6`; `tables/R2:6-90` |
| GA-08 | `audits/04_MB_audit_addendum_B.md:75-79`, `:499-505` (the cells marked "sourced") | Unicorn Overlord: leader, priority list with two conditions, prediction, swap/rest/Valor; Football Manager: two shapes, shouts, review; Bannerlord: recruits, wages, desertion, speed against load, result screen; Total War: muster, upkeep, auto-resolve by comparing statistics | (v) `T19:90`, `:94`, `:104-105`, `:146`; (v) `T16:22-25`; (v) `T02:16-20`; `tables/R6`; `D_T04` row 27 |
| GA-09 | `proposals/04_MB_campaign_party_economy.md:24-28`, `:60`, `:90`; `proposals/04_MB_manager_battle_one_resolver.md:73`; `proposals/04_MB_playable_field_scenario.md:27-29` | the same Bannerlord, Field of Glory, Unicorn Overlord, Football Manager and Total War shapes | (v) `T02:16-20`; `tables/R2`, `R6`; (v) `T19:146`; `T16`; `T07` |
| GA-10 | `audits/05_SC_audit.md:528-573`, `:585`, `:935-947` | Dogs in the Vineyard's priced concession; Guild 2's verdict scale and docket; the detective set's cite-a-held-item rule; Ace Attorney's one correct statement; Triangle Strategy's Scales vote; Victoria 3's enactment clock; Disco Elysium's shown odds | `research/by_lane/SC_social_contest.md` §2.2; `dispositions/D_T05.md` rows 12, 17-22, 40, 66-68; `dispositions/D_T06.md`; `tables/R1:119`, `:150` |
| GA-11 | `audits/05_SC_audit_addendum_B.md:46-47`, `:351-355` | Griftlands' board and hand; Disco Elysium passive check; Ace Attorney and Danganronpa testimony; L.A. Noire's held item; Pentiment's accusation | `tables/R4`, `R5`; `tutorials/T05`, `T06` (that addendum states its own partial reading) |
| GA-12 | `audits/06_FA_audit.md:510-540`; `audits/06_FA_audit_addendum_B.md:371-372`, `:593`, `:638` | Old World ruler goals; EU4 estates; Victoria 3 laws; CK3 vassal contracts; CK2's priced truce breach; Rome II upkeep and replenishment | `research/by_lane/FA_faction_actions.md` T-FA-*; `tables/R1` §1; `tables/R6` §1 |
| GA-13 | `audits/07_SE_audit.md:534-544`, `:563` | Banished labour loss; Manor Lords plot capacity; Kingmaker problem cards; Victoria 3 pops; Songs of Syx and Tropico citizens; Total War's governor | `research/by_lane/SE_settlements_territory_economy.md` §2.2, §2.3; `dispositions/D_T08.md` rows 3, 5, 10, 14, 40 |
| GA-14 | `audits/07_SE_audit_addendum_B.md:154-179`, `:244-247` | labour, population, mood, trade and upkeep shapes in thirteen settlement games, each with its own `[V2]` or `[S2]` tag | `tables/R3a`, `R3b`, `R6`, `R8`, `R9` (tags carried from the tables) |
| GA-15 | `audits/08_FI_audit.md:624-628`, `:642-660` | Dwarf Fortress rumours; Lacuna and Pentiment submission without a verifier; Obra Dinn's lock leak; L.A. Noire's removed option; Shadows of Doubt signatures and witnessed inquiry; how each game spreads news | `dispositions/D_T06.md` rows 3-5, 8-9, 15, 17, 21, 24, 30-31, 37-39, 47; `research/by_lane/FI_fieldwork_investigation.md` |
| GA-16 | `audits/08_FI_audit_addendum_B.md:215-231` (the "nearest precedent" column), `:241-246` | Shadows of Doubt's board, bribe, trespass, blown cover, cover-up job; Obra Dinn's book and opening decks; L.A. Noire's notebook and Accuse; Pentiment's hours and opinion; Disco Elysium's passive reads; Guild 2's evidence strength | (v) `tutorials/T06:18`, `:101`, `:111`, `:119`, `:122`, `:248`, `:259`; (v) `tutorials/T14:261`; `tables/R5`; `D_T06` rows 9, 41. The column gives no line; the lines are added here |
| GA-17 | `audits/09_WR_audit.md:643-655` | generate on demand (CK3, Qud); a single switch gets switched off (Guild 3, Bannerlord); memory gates eligibility (Dwarf Fortress, CK, Nemesis); RimWorld's director; King of Dragon Pass advisers | `research/by_lane/WR_world.md` T-WR-2, -5, -8 |
| GA-18 | `audits/09_WR_audit_addendum_B.md:184-202`, `:288`, `:413`, `:461`, `:484`, `:590-591`; `proposals/09_WR_B_threadwork_session_and_practitioner.md:47`, `:220`; `proposals/09_WR_B_chronicle_that_tells.md:46` | the sanity and terror meters; Sunless Sea's shared cargo; Pathologic 2's daily draw; Wildermyth's repeat suppression; Façade's beat; Prom Week's random arm | `tables/R7`, `tutorials/T08`, `T09`; (v) `tables/R8:136`; `research/emergent_narrative_literature/`; `dispositions/D_T07.md` |
| GA-19 | `audits/10_DICE_audit.md:565-568`, `:593` | shown odds (Baldur's Gate 3, Disco Elysium); the complication band (Blades, PbtA); XCOM's hidden assist | `dispositions/D_T01.md` rows 6, 10, 12, 24, 29 |
| GA-20 | `audits/11_GO_audit.md:505`, `:633-637`, `:656` | CK3's opinion modifiers; Total War played or resolved per contact; Football Manager's viewing ladder | `THROUGHLINES.md` "One resolver or two?"; `D_T04` row 57 |
| GA-21 | `audits/12_ARCS_adjudication.md:473-476`; `audits/13_SC_contest_interrogation.md:354`; `proposals/14_VERBS_SOCIAL2_C_case_question_confession.md:172-173` | L.A. Noire's cited-item accusation; Obra Dinn's joint lock; Ace Attorney's contradiction; Pentiment's moving opinion | named without a line; the repository holds each: `tables/R5` §4 and `D_T06` rows 30-31; `tutorials/T06:62`; `tutorials/T19:160-226`; (v) `R5:52` |
| GA-22 | `audits/15_INSTITUTIONS_VENICE.md:1020`; `audits/22_HAPPENINGS.md:154` | CK3's hook; CK3 murder schemes | `tables/R1` §1 (H3) |
| GA-23 | `audits/16_PESSIMIST_FI.md:324`, `:833-837` | the detective set against five runs | cites `08_FI_audit`, its addendum and `19_LACUNA`; the game side is GA-15, GA-16 |
| GA-24 | `audits/19_LACUNA_investigation_to_proceedings.md:60-134` (rows tagged `[T19 ...]`), `:171-176`, `:250` | Lacuna's player, log, lost clues, tone counter, endings; Ace Attorney's court; Pentiment's accusation | (v) `tutorials/T19:228-298` (`:229`, `:276`, `:298`), `T19:171-216`; (v) `R5:52` |
| GA-25 | `audits/21_PROCEDURAL_GENERATION.md:101-102`, `:104-107`, `:109` | Dwarf Fortress worldgen; Caves of Qud's sultans; RimWorld's threat points; Left 4 Dead's director; Wildermyth's casting and suppression; storylets and Sunless Sea's gate; Façade's beat counts | (v) `tables/R3a:64`, `:125-126`; (v) `tables/R8:126`, `:133`, `:136`; (v) `tutorials/T08:110`; `research/emergent_narrative_literature/` (E15, E17, G07, G10, G11, G13, G14, `02_interactive_drama`) |
| GA-26 | `audits/21_PROCEDURAL_GENERATION.md:76-77`, `:82-83` (the `[T ...]` cells) | Shadows of Doubt population, profile fields, six archetypes, the Resolution Form, the tutorial case | `tables/R5` §2; `tutorials/T06` |
| GA-27 | `proposals/21_PROCEDURAL_B_cast_and_seats.md:237`; `proposals/21_PROCEDURAL_D_world_cards_and_churn.md:163`; `proposals/21_PROCEDURAL_E_names_and_texts.md:29`, `:127` | RimWorld's small cast; the Wildermyth rule; Qud's replacement grammar | as GA-25 |
| GA-28 | `proposals/02_CHAR_voices_and_the_room.md:21-23`, `:122`, `:158` | Disco Elysium's voiced skills; Pentiment's "this will be remembered" | the archived design documents it quotes; `tables/R5` §3 |
| GA-29 | `proposals/08_FI_05_evidence-interface.md:42`; `proposals/08_FI_05_evidence-interface_B.md:136`; `proposals/05_SC_hearing_capabilities.md:80` | L.A. Noire's rule (what is not held cannot be cited); Triangle Strategy's information gate; Disco Elysium's passive check | `D_T06` rows 30-31; the companion (K5) by way of `research/by_lane/FI_fieldwork_investigation.md:246`; (v) `R4:34` |
| GA-30 | `proposals/05_SC_negotiation_scene.md:10`, `:49` | Griftlands' board, hand and concession | `tables/R4` §2; `tutorials/T05` |
| GA-31 | `audits/08_FI_audit_addendum_B.md:101`, `:410` | which games the tree names (Danganronpa in the companion; Immortality in `T08`) | a tree search, repeated here: confirmed |
| GA-32 | `audits/04_MB_audit_addendum_B.md:507-509`, `:514`, `:716` | Dominions as the closest verified precedent; Total War's two calculations | `D_T04` row 27; `tables/R6` F5 |
| GA-33 | `audits/16_PESSIMIST_MB.md:11`, `:330`; `proposals/03_PC_duel_round_and_approach.md:152-163`; `proposals/11_GO_port_gate_order_and_coverage.md:93-94`; `audits/11_GO_audit_addendum_B.md:323-324` | the five mass-battle referents, as Jordan named them | `AUDIT_BRIEF.md` (a quotation of the direction, not a claim about the games); the games' content is GA-07, GA-08, GM-01 to GM-07 |

---

## 3. Claims marked memory, snippet or unverified, or stated with no source (30 groups)

Status: **REPO** the repository already held a sourced note; **FILED** newly sourced, note filed; **PART** the
shape is filed and a named part is still open; **OPEN** still unsourced (§5); **NONE** the suite makes no
claim. Notes are under `research/game_precedent_suite/grounding/`.

| # | suite site(s) | the claim as the suite has it | grade in the suite | source now backing it | status |
|---|---|---|---|---|---|
| GM-01 | `audits/04_MB_audit_addendum_B.md:82`, `:148`, `:499`; `audits/04_MB_audit.md:1350-1353`, `:1357`; `proposals/04_MB_squad_grid_of_named_characters.md:31-32` | Ogre Battle: a unit is a few named characters in front and rear rows | memory, "unsourced in the tree" | `ogre_battle.md` rows 1, 5, 11 (V3: Wikipedia; RPGFan review) | FILED |
| GM-02 | `audits/04_MB_audit_addendum_B.md:499`; `proposals/04_MB_squad_grid_of_named_characters.md:100` | Ogre Battle: a member's row decides what it does | memory; "not adopted, because nothing in the tree sources it" | `ogre_battle.md` row 5 (V3 RPGFan, quoted) | FILED |
| GM-03 | `audits/04_MB_audit_addendum_B.md:500`, `:502`, `:503` | Ogre Battle: one tactic a unit (whom to strike); resolves by itself; the player may change the tactic, play a card, retreat | memory | `ogre_battle.md` rows 3, 4, 6, 7 | FILED |
| GM-04 | `audits/04_MB_audit_addendum_B.md:505` | Ogre Battle keeps a campaign economy | memory | `ogre_battle.md` row 10 (deployment cost, daily maintenance, town income), at stage scale only | FILED |
| GM-05 | `audits/04_MB_audit.md:1357`; `audits/04_MB_audit_addendum_B.md:75`, `:499` | Unicorn Overlord's grid is 2 x 3 | memory (`T19:153` `[M]`) | `unicorn_overlord.md` row 5: two agreeing snippets (S3); rows 2 and 4 give "a grid" and front and back rows at V3 | PART |
| GM-06 | `audits/04_MB_audit.md:824-826`, `:846-847`, `:1347`; `audits/04_MB_audit_addendum_B.md:76`, `:502`, `:514` | that Football Manager's instant result is the same simulation is not established | "not established" (correct) | `football_manager_instant_result.md`: second attempt, same verdict | REPO (confirmed open) |
| GM-07 | `audits/10_DICE_audit.md:587`; `audits/11_GO_audit_addendum_B.md:286`; `audits/07_SE_audit.md:537` | "Football Manager's three fidelities of one match engine", stated as fact | no mark | contradicted in the tree: `D_T04` row 58 (CONTRADICTS), `T16:79` | corrected, §4 GC-3 |
| GM-08 | `audits/04_MB_audit.md:1349-1350`, `:1363`; `audits/04_MB_audit_addendum_B.md:77`; `proposals/04_MB_playable_field_scenario.md:29-30` | Bannerlord: fight, send troops or auto-resolve at contact | memory (`T02:18` `[M]`) | `bannerlord_encounter_menu.md` rows 1-2: Attack or Send Troops, where Send Troops is the simulation (V3, players' forum posts); a third option not found | PART |
| GM-09 | `audits/04_MB_audit.md:1349`; `audits/07_SE_audit_addendum_B.md:237`; `proposals/07_SE_campaign_supply_and_muster.md:48` | Bannerlord's wages are memory-grade and not relied on | memory (from `R2` E6) | the tree holds it at page-read grade: `tutorials/T02_warband.md:17` `[V3 B2]` | REPO; corrected, §4 GC-4 |
| GM-10 | `audits/04_MB_audit.md:1350` | Bannerlord in-battle rout | memory (`R2` F8) | none found | OPEN |
| GM-11 | `audits/04_MB_audit_addendum_B.md:503` | Total War: "pause is memory" | memory | the tree holds it: `tutorials/T07_mass_battle.md:25` `[V3]` ("fight with pause and time controls") | REPO; corrected, §4 GC-6 |
| GM-12 | `audits/08_FI_audit_addendum_B.md:249`; `audits/08_FI_audit.md:957` | Paradise Killer: the trial can be called at any time; the verdict follows the case made, not the truth | `[M: from memory]` | `paradise_killer.md` rows 1, 2, 4 (V3: Wikipedia; the studio's own words; a critic) | FILED; the court's decision rule is `?` |
| GM-13 | `audits/08_FI_audit_addendum_B.md:251`, `:218`; `audits/08_FI_audit.md:958`, `:971` | Frogwares' Sherlock Holmes: a deduction board; a chosen conclusion and a moral choice, never corrected | `[M; the first audit's reading]` | `sherlock_holmes_crimes_and_punishments.md` rows 1-6 (V3: Wikipedia; PC Gamer; GamingBolt) | FILED; corrected, §4 GC-1 |
| GM-14 | `audits/08_FI_audit.md:955-957`, `:969-971`; `audits/08_FI_audit_addendum_B.md:215`, `:218`, `:247`; `audits/16_PESSIMIST_FI.md:838`; `audits/05_SC_audit.md:555`, `:947` | The Case of the Golden Idol: a typed sentence filled from collected words, graded by the machine | no mark; the tree had a self-graded survey row only (`by_lane/FI:93`) | `detective_set.md` §1 rows 1-3 (V3 Wikipedia) | FILED |
| GM-15 | `audits/08_FI_audit.md:970`, `:977`; `audits/08_FI_audit_addendum_B.md:227`, `:248` | Outer Wilds: knowledge is the only persistent state; a ship log; knowledge gates traversal | no mark | `detective_set.md` §2 rows 2-3 (V3 Wikipedia) for what persists and the log; "knowledge gates traversal" is supported in shape, not stated | PART |
| GM-16 | `audits/08_FI_audit.md:977`; `audits/08_FI_audit_addendum_B.md:248` | Her Story: knowledge is the only persistent state and gates where one can go | no mark; the tree had nothing | `detective_set.md` §3 rows 1-2 (V3 Wikipedia): access is by the words the player thinks to search | FILED |
| GM-17 | `audits/08_FI_audit.md:973`; `audits/08_FI_audit_addendum_B.md:246`; `audits/05_SC_audit.md:551`, `:942`; `audits/05_SC_audit_addendum_B.md:353` | Danganronpa: testimony against a presented item; one correct pair | "T2" | the tree: `tutorials/T19:226`, `D_T05` row 40; plus `detective_set.md` §4 rows 1-4 (V3 Wikipedia) | REPO and FILED |
| GM-18 | `audits/08_FI_audit_addendum_B.md:250`; `audits/08_FI_audit.md:976`; `audits/21_PROCEDURAL_GENERATION.md:111`, `:145`, `:155` | Blade Runner (1997): the culprit set is randomised per run; clues are objects; evidence must be generative | `[M]`; `[T FWP §2.3, self-graded HIGH]` | `detective_set.md` §5 rows 1-4 (V3 Wikipedia): which characters are replicants is randomised; "evidence must be generative" not found | PART; made precise, §4 GC-7 |
| GM-19 | `audits/08_FI_audit.md:957`; `audits/08_FI_audit_addendum_B.md:101`, `:252`, `:384` | Heavy Rain | "no claim" (correct) | `detective_set.md` §6, so the name resolves; it establishes nothing about investigation | NONE |
| GM-20 | `audits/19_LACUNA_investigation_to_proceedings.md:44-58`, `:60-134` (rows `[P GD]`, `[P GWO]`); `proposals/19_LACUNA_verdict_ladder_and_reversal.md:9`; `proposals/19_LACUNA_questioning_has_an_approach_and_a_cost.md:8`; `audits/21_PROCEDURAL_GENERATION.md:110` | Lacuna's design, from the developer's devlog: many channels out and few back in; the Case Sheet; no takebacks; a wrong answer is redirected and cascades | page read by that lane; no repository note | `lacuna.md` rows 1-17: both devlogs re-read in body, every quotation found | FILED |
| GM-21 | `audits/21_PROCEDURAL_GENERATION.md:80-81`, `:83` | Shadows of Doubt: every item is saved; goal-based routines, cheap unless near; a dialogue editor with procedural fields | page read by that lane; no repository note | `shadows_of_doubt_generation.md` rows 5-8 (V3: DevBlogs #15, #28, #30, quoted) | FILED |
| GM-22 | `audits/21_PROCEDURAL_GENERATION.md:28-32`, `:76`, `:78-79`, `:141-145`, `:397`, `:418`; `proposals/21_PROCEDURAL_C_prologue_and_case_seeds.md:36` | Shadows of Doubt: the order of generation; a simulated stretch before play; the killer picks an acquaintance; the location hierarchy | snippet (`[S ...]`), stated as such | not reached (`colepowered.com` 403). `shadows_of_doubt_generation.md` rows 1-4 give only: generated per save from a seed; the game selects a citizen as the next killer | OPEN for order and method; PART for the rest |
| GM-23 | `audits/21_PROCEDURAL_GENERATION.md:96`, `:112`, `:149` | Hades and Spelunky: authored chunks under hard constraints; reject or repair a level with no path; Hades selects dialogue by priority | `[M]`, not in the tree | `hades_spelunky.md` rows 1-7 (V3: Kazemi; Wikipedia; Game Developer) | FILED; corrected, §4 GC-2; "priority" is `?` |
| GM-24 | `audits/21_PROCEDURAL_GENERATION.md:103` | CK3's event generator: weighted pools keyed to character state, eligibility triggers plus weights | "generator detail `[M]`" | none (the game's wiki returned a block page) | OPEN |
| GM-25 | `audits/21_PROCEDURAL_GENERATION.md:108` | Kenshi's hand-keyed world states; Mount & Blade's lords are thin characters | "detail `[M]`" | Kenshi's world states are `tables/R2:205` `[V2]`; "thin characters" has no source | PART (Kenshi REPO; the Mount & Blade judgment OPEN) |
| GM-26 | `audits/05_SC_audit.md:528-529`; `audits/05_SC_audit_addendum_B.md:349`; `proposals/05_SC_negotiation_scene.md:11` | Duel of Wits: stakes declared first; a compromise scaled to what the winner lost; three volleys to an exchange; the Point-and-Dismiss collapse | "rules T0"; collapse `[UNVERIFIED]` | `burning_wheel_and_griftlands.md` §1 rows 1-3 (V3, the publisher's forum) for the scaled compromise; the tree's "T0 (printed)" has no fetch record | PART: stakes-first and three volleys are snippet grade; the collapse stays `[UNVERIFIED]` |
| GM-27 | `audits/05_SC_audit.md:533-534`; `audits/05_SC_audit_addendum_B.md:351` | Griftlands: spend-and-roll persuasion was "less fun than fighting" | "T2 ... unverified in v3" | `burning_wheel_and_griftlands.md` §2 row 1 (V3 PC Gamer): dice-rolled speech checks were replaced by cards; the quoted judgment not found | PART |
| GM-28 | `audits/05_SC_audit_addendum_B.md:350`; `audits/05_SC_audit_addendum_B.md:121` | Victoria 3: opposition organises between sittings | `[UNVERIFIED against current patch]` | enactment is `tables/R1:119`, `:150` `[V2]`; counter-mobilisation not re-checked | OPEN (kept marked) |
| GM-29 | `audits/02_CHAR_audit.md:582` | Triangle Strategy's hidden conviction axes: "named once in the companion, unsourced" | "unsourced" | the tree holds it: `tutorials/T19_tactics_narrative.md:13`, `:17`, `:20`, `:23` `[V3]` | REPO; corrected, §4 GC-5 |
| GM-30 | `audits/03_PC_audit.md:468-471`; `audits/03_PC_audit_addendum_B.md:71`, `:173`, `:224`; `audits/04_MB_audit.md:1201`; `audits/11_GO_audit.md:656`; `audits/16_PESSIMIST_GO.md:234-235`, `:335`, `:470` | Final Fantasy Tactics, Tactics Ogre, Fire Emblem, SaGa as referents; what a Crusader Kings, Dwarf Fortress, Disco Elysium or Pentiment player "expects" | named, never surveyed (the suite says so); the genre expectations carry no mark | none filed | OPEN; no proposal rests on them |

---

## 4. Corrections applied (a source contradicts the suite, or the suite gave a wrong grade)

Each is applied in place as a bracketed correction after the original words; each edited file has a
`Grounded:` line at its head naming this file.

| # | what was wrong | what the source says | files edited |
|---|---|---|---|
| GC-1 | Sherlock Holmes: Crimes & Punishments: "a chosen conclusion and a moral choice, **never corrected**" | The game accepts a wrong conclusion and goes on, **and offers an optional reveal of whether it was right, with a replay of the case's last part** (PC Gamer 2014-11-06; GamingBolt 2014-10-22; `sherlock_holmes_crimes_and_punishments.md` rows 4-6). The games that never tell the player are Paradise Killer and, with "right away", Lacuna | `audits/08_FI_audit_addendum_B.md` |
| GC-2 | Spelunky: "reject or repair a level with no path"; convergence 4 lists it under "constraints plus rejection" | Spelunky lays a guaranteed solution path first (rooms with guaranteed exits) and fills the rest in; nothing is tested and rejected (Kazemi; `hades_spelunky.md` rows 1-3). Hades: selection by situation and weight is sourced; "by priority" is not | `audits/21_PROCEDURAL_GENERATION.md` |
| GC-3 | "Football Manager's three fidelities of one match engine" stated as fact | The tree's own check marks it CONTRADICTS, not established (`D_T04` row 58; `T16:79`); a second attempt did not establish it. Sourced: a ladder of ways to watch one match (`D_T04` row 57) | `audits/10_DICE_audit.md`, `audits/11_GO_audit_addendum_B.md`, `audits/07_SE_audit.md` |
| GC-4 | "Bannerlord's wages are memory-grade ... not relied on" | Page-read in the tree: `T02:17` `[V3 B2]` (daily wages; the unpaid lose morale, then desert). `R2` E6 is the `[M]` cell | `audits/04_MB_audit.md`, `audits/07_SE_audit_addendum_B.md`, `proposals/07_SE_campaign_supply_and_muster.md` |
| GC-5 | Triangle Strategy's hidden conviction axes: "unsourced" | Sourced in the tree: `T19:13`, `:17`, `:20`, `:23` `[V3]` (three hidden convictions, shown on New Game Plus). The entry's conclusion (did not transfer) is untouched | `audits/02_CHAR_audit.md` |
| GC-6 | Total War: "pause is memory" | Page-read in the tree: `T07:25` `[V3]` | `audits/04_MB_audit_addendum_B.md` |
| GC-7 | Blade Runner (1997): "the culprit set is randomised"; "evidence must therefore be generative" | What is randomised is **which characters are replicants**, over an authored cast; how clues follow is not stated in the source read (`detective_set.md` §5) | `audits/08_FI_audit_addendum_B.md`, `audits/21_PROCEDURAL_GENERATION.md` |
| GC-8 | Ogre Battle "not sourced as a battle referent anywhere in the tree"; its cells "memory"; the row rule "not adopted, because nothing in the tree sources it"; Paradise Killer `[M]`; Unicorn Overlord's grid "memory"; Bannerlord's menu "memory-grade" | Now sourced or regraded: GM-01 to GM-05, GM-08, GM-12 | `audits/04_MB_audit.md`, `audits/04_MB_audit_addendum_B.md`, `proposals/04_MB_squad_grid_of_named_characters.md`, `proposals/04_MB_playable_field_scenario.md`, `audits/08_FI_audit_addendum_B.md` |

Pointer lines only (no claim changed; the head line names the repository note that now backs the web reading):
`audits/19_LACUNA_investigation_to_proceedings.md`, `audits/08_FI_audit.md`, `audits/05_SC_audit_addendum_B.md`.

**Not edited, recorded instead.** `research/game_precedent_suite/tutorials/T16:79` and `dispositions/D_T04.md`
row 58 summarise the Operation Sports report as saying Instant Result "bypasses the match engine". The page,
read here, says the button would "instantly simulate the remainder of a match without watching highlights or
sitting through the 3D match engine". That describes skipping the viewing and is consistent with either
reading. This lane does not alter existing sourced text in `research/`; the observation is in
`grounding/football_manager_instant_result.md`. The verdict (not established) is unchanged.

---

## 5. Still unsourced (mark where it stands, or drop; none carries a proposal)

| # | claim | where | what was tried | disposition |
|---|---|---|---|---|
| GU-1 | That Football Manager's instant result runs the same simulation as a watched match | GM-06, GM-07 | two passes; Operation Sports read; no Sports Interactive statement found; the studio's bug tracker blocked | keep "not established"; cite for nothing |
| GU-2 | The order of Shadows of Doubt's generation, the simulated stretch before play, how the killer chooses and stalks a victim, the location hierarchy; witnesses who lie | GM-22 | `colepowered.com` 403; itch.io DevBlogs #16, #18, #23 read and carry no method | keep at snippet grade as leads, as `21_PROCEDURAL` already says at `:69-70`; the kit's order in that audit is its own design and needs no precedent |
| GU-3 | CK3's event generator (weighted pools, triggers) | GM-24 | the game's wiki returned a block page | keep `[M]`; the row's sourced half (`R1`) carries the comparison |
| GU-4 | Bannerlord's in-battle rout; a third "join" option at contact; that Mount & Blade's lords are thin characters | GM-08, GM-10, GM-25 | Steam forum threads read; no first-party page reached | keep marked; the suite relies on none |
| GU-5 | Duel of Wits: the Point-and-Dismiss collapse and its "21-vs-11"; stakes-first and three volleys at page-read grade; the Klei "less fun than fighting" quotation; Victoria 3's counter-mobilisation | GM-26, GM-27, GM-28 | the printed rulebook not reached; forum threads read; one PC Gamer feature read | keep `[UNVERIFIED]` exactly as the suite has them |
| GU-6 | Final Fantasy Tactics, Tactics Ogre, Fire Emblem and SaGa as referents; statements of what a given game's players "expect" | GM-30 | Final Fantasy Tactics' encyclopedia article was read and nothing filed, because the suite makes no mechanic claim about it | the referents stay nulls ("neither may be cited as support", `03_PC_audit_addendum_B.md:224`); the genre expectations are the pessimist lanes' judgments and are not precedent |

Also open inside filed notes (each note's "does NOT establish" section): Unicorn Overlord's 2 x 3 shape at
page-read grade; how Paradise Killer's court decides; whether Hades orders dialogue by priority; whether Outer
Wilds states "knowledge gates traversal" as a rule; how Blade Runner's clues follow its randomisation.

---

## 6. Research notes filed (all `## Status: FILED — reference, tier 3`, dated 2026-11-12)

Under `research/game_precedent_suite/grounding/` (a new directory; the suite's `README.md`, tables and
tutorials were not edited). Each states its sources, the date read, the tier of every row, and what it does
not establish.

| note | covers | sources read in body |
|---|---|---|
| `ogre_battle.md` | squads, rows, tactics, one-round exchange, leader, deployment cost | Wikipedia (two articles); RPGFan review 2000-08-24; a fan strategy page |
| `unicorn_overlord.md` | the unit grid | Wikipedia; one player's blog; two snippets for the 2 x 3 shape |
| `football_manager_instant_result.md` | whether instant and played are one simulation | Operation Sports 2025-10-21; Wikipedia. Verdict: not established |
| `bannerlord_encounter_menu.md` | Attack or Send Troops; wages | two Steam forum threads; Wikipedia; the tree's `T02:17` |
| `lacuna.md` | the developer's design principles and the worked example | Colbus, Game World Observer 2020-11-08 and Game Developer 2020-09-28 |
| `shadows_of_doubt_generation.md` | what is generated, routines, save-everything, the authoring tool | ColePowered DevBlogs #15, #28, #30 (itch.io); Wikipedia |
| `paradise_killer.md` | the trial at any time; never told you were wrong | Wikipedia; the studio's interview 2021-04-02; a critic 2021-03-09 |
| `sherlock_holmes_crimes_and_punishments.md` | the deduction board; the optional reveal | Wikipedia; PC Gamer 2014-11-06; GamingBolt 2014-10-22 |
| `detective_set.md` | Golden Idol, Outer Wilds, Her Story, Danganronpa, Blade Runner (1997), Heavy Rain | one encyclopedia article each |
| `hades_spelunky.md` | Spelunky's path by construction; Hades' rooms and event selection | Kazemi; Wikipedia (two); Game Developer 2020-02-13 |
| `burning_wheel_and_griftlands.md` | the scaled compromise; dice replaced by cards | two publisher-forum threads; Wikipedia; PC Gamer 2019-07-12 |

---

## 7. Limits of this pass

- **The 33 groups of §2 were sampled, not re-derived.** Twenty-two line citations were opened; the rest are
  taken as the citing lane wrote them. A table cell's own tag (`V2`, `S2`, `M`) was not re-checked against
  its web source: that is the precedent suite's own record.
- **Encyclopedia articles carry several notes.** A gameplay section is a secondary summary, often uncited
  itself. It is good for the shape of a mechanic and wrong to trust for a constant. No figure from one is
  relied on anywhere.
- **Forum-grade rows** (Bannerlord's menu, the Duel of Wits compromise) are folk models read in body. They
  are marked as such in their notes.
- **Blocked this pass:** `colepowered.com`, `unicornoverlord.atlus.com/system.html`,
  `community.sports-interactive.com`, `wireframe.raspberrypi.com`, `strategywiki.org`, `ck3.paradoxwikis.com`,
  several guide sites. Each note lists what it could not reach.
- **Digests were not edited.** A digest restates a repository file; correcting the file it digests is the
  correction.
- **Not done:** no pytest (a prose and research change; `CLAUDE.md` §0.4); no commit; no edit outside
  `research/game_precedent_suite/grounding/` and this suite directory.
