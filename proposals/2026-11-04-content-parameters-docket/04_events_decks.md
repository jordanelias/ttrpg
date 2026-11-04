# Content parameters docket, chapter 04: Events, decks, weather, storylines, endings, narration

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Scope narrowed by orchestrator mid-task: clocks/timers/thresholds/thrust ladders/threadwork/calendar are another agent's (see Belongs elsewhere).
Measured 2026-11-04 in the tree: `engine/season/tensions.yaml`, `data/tensions.py`, `scenarios.yaml` do NOT exist; no `tension_effects` roster, no `TENSIONS_YAML`, no `territory_yield_scale` fixture (grep over engine/season: 0 hits). No event-deck/event-card carrier exists anywhere in code.

## EVENT DECK / EVENT CARD (general) — carrier/loader: NONE
Population now: 0 authored in code.   Status: EMPTY
Proposed shapes only (all PROPOSED-ONLY):
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | id | string, unique (prefixed `tension_<card>_` / `scn_<id>_` in proposals) | PROPOSED-ONLY | NONE | 08_decks...md:19-30; appendix_A5 §2 |
| 2 | identity | family | tag only | PROPOSED-ONLY | NONE | appendix_A5 §1 "Goldenfurt fields" |
| 3 | identity | source | quoted origin string + `[ASSUMPTION; medium; Jordan to correct; revert: ...]` | PROPOSED-ONLY | NONE | v10 part4 CL-EVENTS (4) |
| 4 | eligibility | eligible / triggers | build-time query over world | PROPOSED-ONLY | NONE | appendix_A5 §2 |
| 5 | draw | weight (base) | number | PROPOSED-ONLY | NONE | appendix_A5 §1 |
| 6 | draw | cooldown/excludes | draw-without-replacement at build | PROPOSED-ONLY | NONE | appendix_A5 §1 |
| 7 | binding | npc_refs → role slots | seats/body roles, never names | PROPOSED-ONLY | NONE | 08 §3 |
| 8 | content | the_ask | question to named person | PROPOSED-ONLY | NONE | appendix_A5 §1 |
| 9 | content | responses | existing verbs from `verb_table.yaml` | PROPOSED-ONLY | NONE | appendix_A5 §1 |
Owed: the user's supply order "name, type, effect" matches NO loader field; code has no card schema. Grounded deck (`proposals/grounded_event_card_deck_v1.md`) card fields (Grounding, Trigger, Scale, Branches, Three-vector burden, Ripples, Follow-on, New lever) are PROPOSED-ONLY and gated on retired Key types (v10 part4 CL-EVENTS: "not adopted as written").
Conflicts: A5 says 58 cards in grounded deck; file contains 10 distinct `EVT-` ids (measured).

## TENSIONS CARDS — carrier/loader: planned `engine/season/tensions.yaml` + `data/tensions.py` (CL-EVENTS commit 3, B10-18) — NOT BUILT
Population now: 0 in code. 6 cards drafted PROPOSED-ONLY in `proposals/2026-10-28-content-architecture-suite/08_decks_and_template_in_engine_form.md` §1 (Royal Crisis, Feldmark Famine, Cardinal Independence, Guild Fracture, Einhir Incident, Ministry Crisis); draw 1 at build.   Status: EMPTY
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | card id | string | PLAN | NONE | workplans v10_part4.md:413 |
| 2 | identity | source | quoted line + [ASSUMPTION] tag | PLAN | NONE | part4:414 |
| 3 | effect | effect kind | closed roster `tension_effects: [goal, yield_scale]` (unbuilt) | PLAN | NONE | part4:413 |
| 4 | effect (goal) | goal row (org, object, pursuits, stance, id) | same schema as `goals.yaml` rows (`data/goals.py::parse`) | PLAN | HAS in proposal: 18 goal rows over 5 of the 6 cards (royal 9, cardinal 4, guild 1, einhir 2, ministry 2); card 2 Famine is a yield_scale, no goal row | part4:413; goals.yaml header |
| 5 | effect (goal) | choose_one lists | keyed draw per card id + list index | PLAN | HAS in proposal (card 1: 3 factions x 3 royal seats) | part4:414 |
| 6 | effect (yield_scale) | territory id, scale | territory id (`data/geography.py`), number; card 2 = 0.75 on terr_T5 | PLAN | proposal only | part4:413-414 |
| 7 | build | switch `build_realm(tensions=False)` | bool, shipped off | PLAN | NONE | part4:413 |
Owed: all six cards as loaded data; schema file. Refused keys (plan): date, deadline, firing condition, outcome, write to standing/seat/tenure/stance, `closing`, `successor`, `deal`.
Conflicts: A5 says archive cut table = 6 cards draw 1, superseding 8-10 draw 2; 08 and part4 agree on 6/draw 1. 08 uses Feldmark = terr_T5; part4 says "Feldmark territory rung" (id not stated there).

## GOLDENFURT DECK (28 cards) / SETTLEMENT OPENINGS — carrier: none (PROPOSED-ONLY, 08 §2-§4; plan row CL-OPEN, B10-19, build HELD on M26)
Population now: 0 in code; 9 `gf_*` goal rows drafted in 08 §2 (parse-tested per 08 §0, not shipped).   Status: EMPTY
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | pool row id `<kind>_<settlement>_<slot>` | string, unique | PROPOSED-ONLY | NONE | 08 §3 rule 3 |
| 2 | identity | opening kind | 5 kinds: market dispute, levy grievance, church draws near, old rite, law sides | PROPOSED-ONLY | NONE | 08 §3 |
| 3 | binding | slots | seat/body roles (trade body, commons, law, church, Restoration) | PROPOSED-ONLY | NONE | 08 §3 |
| 4 | eligibility | building map of settlement type | `venues.yaml` | PROPOSED-ONLY | HAS (venues.yaml exists) | 08 §3 rule 2 |
| 5 | content | goal rows | goals schema | PROPOSED-ONLY | 9 drafted | 08 §2 |
| 6 | content | seed Record | Record held from build (carrier owed) | PROPOSED-ONLY | NONE | 08 §2 G505 |
| 7 | content | opens_with | existing verb name, loader-verified | PLAN | NONE | part4 CL-OPEN |
| 8 | draw | deal | `build | convene` | PROPOSED-ONLY | NONE | 08 §4 |
Owed: 12 of 28 cards have no engine form (G205, G301, G302, G401, G403, G404, G501, G504, G601, G604, G701, G702); loader `settlement_openings`; pool size P>=36 (first slice 8) per A5 §2.
Conflicts: A5 "each world draws 6 (2 Tensions + 4 openable)" vs plan CL-OPEN "a few bundles" (unspecified).

## SCENARIO / STORYLINE / SET PIECE ROWS — carrier: planned `engine/season/scenarios.yaml` — NOT BUILT, PROPOSED-ONLY (appendix_A5 §2)
Population now: 0; seed corpus ~60 per A5 (unmeasured by me).   Status: EMPTY
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | id, family, source | string | PROPOSED-ONLY | NONE | A5 §2 |
| 2 | eligibility | eligible | build-time query | PROPOSED-ONLY | NONE | A5 §2 |
| 3 | binding | places | persons / goal rows / one seeded claim | PROPOSED-ONLY | NONE | A5 §2 |
| 4 | binding | opener | a seat | PROPOSED-ONLY | NONE | A5 §2 |
| 5 | binding | opens_on | band on opener's own ledger | PROPOSED-ONLY | NONE | A5 §2 |
| 6 | binding | opening_act | existing verb + Record kind with stages | PROPOSED-ONLY | NONE | A5 §2 |
| 7 | content | roles, beats | questions per role | PROPOSED-ONLY | NONE | A5 §2 |
Refused (A5): fires_at, outcome, deadline, standing/stance/tenure writes. Outcomes not authored.

## WEATHER / SEASON-FACTOR DRAW — carrier/loader: `engine/season/data/fixtures.py:494-500`, read by `queries/world_q.py:1055-1120` (`season_factor_of`)
Population now: `season_factor=1.0` (HAS, default); `season_factor_draw=()` (STUB, control, shipped off).   Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | base | season_factor | number; swept 0.5/1/2 | REQ | HAS 1.0 | fixtures.py:494 (H-26) |
| 2 | year | season_factor_draw | tuple per season of year of tuples of equally likely multipliers; length = year length; `()` = no draw; raises Unspecified if a season has no outcomes (world_q.py:1084) | OPT | HAS `()` | fixtures.py:500 |
| 3 | live arm | values Jordan sets | plan default `((0.5,1.0,2.0),)*4` [ASSUMPTION] | PLAN | NONE | part4 CL-EVENTS (2) |
| 4 | per-territory | territory_yield_scale | per territory number | PLAN | NONE | part4:413 (commit 3) |
| 5 | calendar | season_terms.want per season_of_year; year_length | year_length 0 = off, flip to 4 | PLAN | NONE (no `year_length` in engine/season py/yaml, grep 0) | CP-T10-03 (part12:98, part14:218) |
Owed: the multipliers per season and the year length; climatic family of grounded deck as candidate source (part4 CL-EVENTS).
Conflicts: A5 says weather factor "constant 1.0 at world_q.py:945"; actual owner at world_q.py:1062.

## ENDINGS — carrier/loader: `engine/season/rosters.yaml: endings` (read by `world_q.endings_reached`, world_q.py:2366)
Population now: 2 members: peninsular_sovereignty (victory: true), theocracy.   Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | ending id | string | REQ | HAS x2 | rosters.yaml:2883 |
| 2 | victory | victory | bool; loader refuses a second `true` | REQ | HAS | rosters.yaml:2883-2929 |
| 3 | condition | holds | exactly one of `{post: <offices seat post>}` or `{rung_kind: <rung_kinds member>}` | REQ | HAS | same |
| 4 | condition | under | a `factions` member or `one_faction` | REQ | HAS | same |
| 5 | provenance | source, assumption_note | string | OPT | HAS | same |
Owed: loss states (none in code); GD-1 clauses not carried (Accord, Stability, sustain 2 seasons, treaties) have no carrier (rosters.yaml note). Nothing halts on a reached ending.

## ENDINGS_CLASSIFIED (arc closure classes) — `engine/season/ENDINGS_CLASSIFIED.yaml`
Population now: 50 rows (measured). Labels: DECIDER 20, NEVER 10, ROLL 9, THRESHOLD 8, UNCLEAR 3; forced_by_threshold yes = 19.   Status: AUTHORED (agent classification of prose, labelled non-execution)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | id | ARC-NN (A5: rows cover ARC 1-18, 20-45, R16-R19 + EMG-10/11; arcs 46-55 unclassified) | OPT | HAS x50 | ENDINGS_CLASSIFIED.yaml |
| 2 | class | label | enum {DECIDER, ROLL, THRESHOLD, NEVER, UNCLEAR} | OPT | HAS | header :9-14 |
| 3 | class | forced_by_threshold | yes/no | OPT | HAS | header :16 |
| 4 | evidence | phrase | quoted string | OPT | HAS | rows |
Owed: classes for arcs 46-55 (A5 §3); plan B6.n rule draws ladder positions only from first two classes (part12:19).

## NAMED-NPC / ARC CASE FILES (authored-content inventory) — `engine/season/cases/`
Population now: 54 distinct ARC ids and 46 NPC ids across cases/ARC*.yaml, NPC*.yaml, chain/*, exercises/ (measured by grep of `- id:`; exercises/ARC-* are scale re-authoring records per A5). chain/ARC3 has 2 rows only.   Status: AUTHORED (calibration corpus, "never runtime data", part B10-19)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | id, name, one_line, scale | scale enum {person, settlement, faction, realm, world} | OPT | HAS | cases/chain/CASE_BRIEF.md |
| 2 | needs | season_requires[need, why, hardness] | hardness {core, important, flavour}; 4-12 rows | OPT | HAS | CASE_BRIEF.md |
| 3 | time | temporal{span_seasons, needs_memory_of, needs_deadline} | | OPT | HAS | CASE_BRIEF.md |
| 4 | actors | who_acts, knowledge | list | OPT | HAS | CASE_BRIEF.md |
| 5 | close | ends_when | prose; code evaluates none (G-25, part11:46) | OPT | HAS | CASE_BRIEF.md |
Conflicts: cases/ARC*.yaml and chain/NPC3.yaml are not all valid YAML (chain/NPC3.yaml fails safe_load at line 1: backtick); counts above are by grep.

## NARRATION FRAGMENTS (NM-W rows) — no carrier; plan rows in workplans v10_part4.md:393-408
Population now: 0 authored fragments.   Status: EMPTY
| # | group | row | state | called for by |
|---|---|---|---|---|
| 1 | render | NM-W1 chronicle (ranking tiers, name fallback) | PARTLY LANDED (`harness/chronicle.py`) | part4:395 |
| 2 | content | NM-W4 content-bearing record kind | UNBUILT, HELD | part4:398 |
| 3 | render | NM-W5 focalized journal | UNBUILT, behind NM-W1 | part4:399 |
| 4 | content | NM-W6 fragment bake | UNBUILT | part4:400 |
| 5 | content | NM-W7 scale lines | UNBUILT | part4:401 |
| 6 | content | NM-W8 occasion ladder | UNBUILT; decision 2 in -05 | part4:402 |
| 7 | conformance | NM-W9 | UNBUILT | part4:403 |
Fragment text fields (name, scale, text) are not specified by code or plan rows read; narration proposal `proposals/2026-10-13-narration-mechanisms.md` §4 not read in detail (PROPOSED-ONLY).

## World travel / survival inputs (as found; CP-T10 items, B10-18)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | hazard | body_step | 0/10/67 swept | REQ | HAS 10 | fixtures.py:643 |
| 2 | hazard | age_step, illness_rate, age_at_build | numbers; "ALL ARE JORDAN'S TO SET" | REQ | HAS 0.0/0.0/0 (dark) | fixtures.py:655-657; CP-T10-05 |
| 3 | travel | route price by terrain (`terrain_type_at`) | geography terrain rows (`valoria_geography_v30.yaml:760-771`) | PLAN | NONE | CP-T10-01 (part14:203) |
| 4 | calamity | exposure_body keyed by BFS band from epicentre terr_T15 | numbers per band | PLAN | NONE | CP-T10-02 (part14:211) |

## NARRATION FRAGMENT FIELDS (PROPOSED-ONLY; `proposals/2026-10-13-narration-mechanisms.md` §3.2, §4 W4/W6/W7/W8; plan rows v10_part4.md:393-408)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | W6 key | kind family | Event kind family (read before degree; degree spans three ladders) | PROPOSED-ONLY | NONE | narration-mechanisms.md W6 "Template selection" (:294-296) |
| 2 | W6 key | degree band | from `emits_at(degree)` (`resolve.py:480`) | PROPOSED-ONLY | NONE | W6 "Cells" |
| 3 | W6 key | refusal stem or explicit no-stem cell | `REFUSAL_KINDS` members | PROPOSED-ONLY | NONE | W6 |
| 4 | W6 key | via? | bool (act via a seat) | PROPOSED-ONLY | NONE | W6 |
| 5 | W6 key | weight > 1 | bool (cohort) | PROPOSED-ONLY | NONE | W6 |
| 6 | W6 text | N variants per enumerated cell (observed cells first) | prose strings; names bind at render, never in fragments; most specific wins, ties by seeded pick (seeded on `e.id`, the proposal's choice) | PROPOSED-ONLY | NONE | W6 "Bake protocol" |
| 7 | W6 text | lexicon swap for Certainty; optional chronicler voice lexicon | strings | PROPOSED-ONLY | NONE | W6; §2.3 (a) |
| 8 | W4 content | new record kind with one key `says` (a `Said`) | registered on `_mint_document`; no `about` key | PROPOSED-ONLY | NONE | W4 Statement |
| 9 | W7 text | settlement line (actorless MATTER Events per settlement per season) | text per aggregate | PROPOSED-ONLY | NONE | W7 (a) |
| 10 | W7 text | faction line; cohort line; march declaration + field-band line | text | PROPOSED-ONLY | NONE | W7 (b),(c), March |
| 11 | W8 | authored occasion rows, boot-time, read once by `build_realm` | roster + loader in `data/rosters.py`; rows may not key on seat age | PROPOSED-ONLY | NONE | W8 Rung 2 |
Fragment file location: "beside its reader"; loader refuses unknown key (W6). The proposal gives no named per-fragment fields beyond key + variant text. `anti-patterns-skeleton.md` I.14 is the audit reference.

## Belongs elsewhere
- CLOCKS/THRESHOLDS/CONDITIONAL ARCS/THREADWORK (skipped per scope change): thrust ladders `goal_stages` (goals.yaml:38-52; 0 authored), `axis:` on goals (0 of 38 carry one), `rosters.yaml:2028 thrust_axes` (14 members) and `:2055 goal_stage_terms` (short, medium, long); CL-THRUST B4.x/B5.2/B6.n (part12:19; part11:98-110); `fixtures.py:1000 thread_sensitivity_gate=30`; `loop/calendar.py` (Date due_at/venue/holder/fired; no authored dates found); CL-THRUST content gaps G-09/G-10/G-26 (part11:30-47).
- Goal-row schema for Tensions/Goldenfurt rows (org, object kinds, pursuits, stance, derives): goals owner (character/faction docket).
- Foreign-actor switch `foreign=False` (A5 family D): faction/world build.
