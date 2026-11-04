# Content parameters docket, chapter 05: Clocks, timers, thresholds, conditional arcs, threadwork

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Collation only. Counts measured 2026-11-04 by loading the YAML / grep. Paths relative to /home/user/ttrpg.

## 0. What the code does and does not carry (read first)

- **There is NO authored clock/track registry.** `grep clock_registry` over engine/modules/references/proposals/workplans: 0 hits. The loop's header says "NO CLOCK GENERATES ANYTHING" (`engine/season/loop/census.py:39`) and "no container gets a clock" (`loop/driver.py:253`). The only clocks are three LICENSED self-motions in `loop/matter.py` (wear, Tenure `term`, claim decay) plus the bodies clock (`body_step`/`age_step`/`illness_rate`), all driven by fixtures not by authored rows.
- **No `due_at`-bearing authored data.** Dates are minted at runtime by `_eff_convene` (`loop/effects_governance.py:409-456`); `World.dates` starts `{}` (`state/world.py:368`).
- **No threshold registry.** Thresholds are (a) fixture/roster band floors, (b) module constants, (c) verb-table `requires:` gates.
- **No conditional-arc carrier.** M20 (ED-IN-0301) = "ordered stage conditions on the person's own ledger"; `goal_stages` schema is built, content 0. Arcs are "never runtime data" (ED-IN-0225).
- **Threadwork has a Python sim (`systems/threadwork/sim/`, 7 files) but the season loop reaches none of it** (`references/module_contracts.yaml:300-323`: `wiring.build: unwired`; verb_table `thread_read` note: "P-01 co-movement and the coherence cost ... are threadwork effects with no carrier in this loop", `engine/season/verb_table.yaml:1640`). The only season-loop threadwork carrier is `Person.thread_sensitivity` (a gate value).

---

## 1. CLOCK / TRACK  — carrier/loader: none authored (licensed clocks live in code + fixtures)
Population now: 0 authored clock/track rows. 4 licensed clocks in code (below).   Status: EMPTY (as a registry); the clocks exist as fixture-driven code.

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | clock id / name / owner / scale / trigger source | no carrier | PLAN | NONE | `proposals/2026-10-28-content-architecture-suite/07c_ADJ3_events_arcs_clocks.md:29-34` ("None runs in the loop"); `loop/matter.py:161` ("a world track that moved by itself would be a fourth clock") |
| 2 | licensed clock A: matter wear | `wear_per_season.rates` per site kind (9 kinds: harbour, seam, body, dwelling, garrison, barracks, archery_range, stable, siege_workshop) | int/season per site kind; closed key set = `site_kinds` | REQ | HAS (harbour 10, seam 10, body 10, others 0) | `engine/season/rosters.yaml:1558`, read by `data/fixtures.py:107,245` (H-07) |
| 3 | licensed clock A | `condition_scale` | int | REQ | HAS (1000, per hole_register H-125 cite) | `engine/season/hole_register.yaml:~918` |
| 4 | licensed clock B: tenure term | `oblige_term` (seasons a declared `oblige` Tenure runs) | int or None | REQ | HAS (4; swept None/1/4) | `data/fixtures.py:958` (H-159); `Term.matures_at` `state/carriers.py:42-68`; matured at `loop/matter.py:387-420` |
| 5 | licensed clock C: claim decay | `claim_decay_per_season` | int | REQ (Fixtures refuses if absent, `fixtures.py:66-87`) | HAS (5) | `data/fixtures.py:293` |
| 6 | licensed clock D: bodies | `body_step` | int/season starvation loss | REQ | HAS (10; swept 0/10/67) | `data/fixtures.py:643` (H-125) |
| 7 | licensed clock D | `age_step` | float | REQ | HAS (0.0, control) | `data/fixtures.py:655` (IN-34) |
| 8 | licensed clock D | `illness_rate` | float | REQ | HAS (0.0, control) | `data/fixtures.py:656` |
| 9 | licensed clock D | `age_at_build` (seasons old at tick 0) | int | REQ | HAS (0) | `data/fixtures.py:657`; `Person.born` `state/carriers.py:~726` |
| 10 | licensed clock E: weather | `season_factor` (constant) / `season_factor_draw` (per-season outcome table; its LENGTH defines the year) | float / tuple of tuples of floats | REQ | HAS (1.0 / `()` = off) | `data/fixtures.py:494,500`; `queries/world_q.py:1053-1090` (H-26) |
| 11 | record stage clock | `record_stages_default`, `record_stage_term` | int | REQ | HAS (3, 1) | `data/fixtures.py:555-556` (H-80) |
| 12 | long-horizon windows | `entrenchment_seasons` 60 (in-chain), `practice_window` 4 (seasons), `estimate_window_seasons` 20 | int | REQ | HAS | `data/fixtures.py:395,440,788` |
| 13 | retired tracks | CI, IP, RS, MS, Turmoil, Accord, WC, Prosperity, PV, Torben loyalty, Coup Counter | retired / no carrier | — | RETIRED (`ms_track.py` MS_START 60 on disk, no importer) | 07c:29-34, :64, :86-94 |
| 14 | threadwork "clock" | Thread Fatigue (module_contracts bucket `clock`, "advances to Spirit*5 contact-break threshold") | contract row only | RETIRED-KEY | NONE in season loop | `references/module_contracts.yaml:300-307` (row carries `registry_system: Key Type Registry vocabulary`, `parity: key-log`; only source is the Key-era contract row). Live equivalent: none; the licensed clocks above (matter wear, Term.matures_at, claim decay, bodies) are the only clocks. |

Owed:
- Whether any authored clock/track registry is wanted: no code or plan position calls for one (07c:29 "None runs in the loop"; M16 fourth motion = "CONFIRMED AT THE DEFAULT" off, `workplans/valoria_master_workplan_v10_part6.md:199`).
- Per-territory weather values (the `season_factor_draw` table is `()`): "Content, not questions", `v10_part6.md:206` (CL-EVENTS; other agent's scope, listed once).
- `age_step`, `illness_rate` magnitudes ship at control 0: unruled (`fixtures.py:655-656`).

Conflicts:
- `SEASONS_PER_YEAR` (`systems/overview/sim/ms_track.py` -> `game_constants.json`) vs `season_factor_draw` length as the year: two owners; `engine/season` reads no engine_params (`engine/season/hole_register.yaml:284`).
- `references/module_contracts.yaml:542` and `registers/mechanics_index.yaml:140` call `ms_track` the "live tick"; it has no importer (07c:98).
- `matter.py` header (loop) says licensed clocks are "three" (`loop/matter.py:425`, "THIRD LICENSED CLOCK") while the bodies clock (`:678`) is a fourth; AX-5 names "three self-motions and bodies is the one with no writer" (`matter.py:635`) — counted as written in code.

Belongs elsewhere: weather / Tensions / event decks (CL-EVENTS) — other agent.

---

## 2. TIMER / DATED ITEM (Date, DocketItem, Term)  — carrier: `World.dates` dict `state/world.py:368`; Date is a dict, no class
Population now: 0 authored (dates minted at runtime by `convene`).   Status: EMPTY (by design; runtime-minted)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `id` | `H(world_seed, tick, actor, "convene:<venue>")` | DERIVED | — | `loop/effects_governance.py:448` |
| 2 | location | `venue` (rung id) | id in `w.rungs` | REQ (`_req_convene`) | runtime | `effects_governance.py:447,453`; `loop/predicates.py:581` |
| 3 | schedule | `due_at` (tick) | int; default `w.tick + 1` from payload `when` | REQ (act payload) | runtime | `effects_governance.py:446,454`; `loop/calendar.py:40` (fires when `due_at == w.tick`) |
| 4 | holder | `holder` (SEAT id exercised via `Act.via`) | seat id or None; None = date fires and lapses | DERIVED | [ASSUMPTION; medium] | `effects_governance.py:433-444`; `calendar.py:42,59` |
| 5 | state | `fired`, `convening_attached` | bool | DERIVED | — | `calendar.py:55`; `effects_governance.py:455` |
| 6 | docket | DocketItem `{date, matter}` | matter None until `open_case` fills | DERIVED | — | `calendar.py:64-68`; `queries/world_q.py:239-263` |
| 7 | tenure term | `Term.matures_at`, `Term.declared_by` | int tick / act id | DERIVED from `oblige_term` | — | `state/carriers.py:42-68`; `loop/matter.py:387-420` |
| 8 | calendar | season-of-year | `w.tick % len(season_factor_draw)`; None when table `()` | DERIVED | none (table off) | `queries/world_q.py:1053-1059` |

Owed:
- No authored dated item. A card or arc may not carry a date (T-c; 07c:36, :58 "Dates are also barred from cards"); "a scripted invasion or other dated pin" is cut (`proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md:257`).
- Convener-seat-as-holder is an [ASSUMPTION; Jordan to correct] (`effects_governance.py:436`).

Conflicts: none beyond §1.

Belongs elsewhere: arrangements / bench (`determine`, `open_case`) — governance agent.

---

## 3. THRESHOLD (band floors, crossing triggers, gates)  — carriers: `rosters.yaml tables`/rosters, `data/fixtures.py`, module constants
Population now: authored as fixtures/rosters (listed). No authored "what fires at which value -> effect" table: crossings emit an Event and "MAY NEVER PRODUCE AN OUTCOME" (L5, `loop/matter.py:79`).   Status: PARTIAL

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | site condition bands | `band_floors` per site kind (verb-keyed floors) | int per (site kind, use verb); `dwelling: {}`, `garrison: {}` empty on purpose; body = `{full_operations 800, limited 500, withdrawal_only 100}` | REQ | HAS ("INVENTED", H-08) | `rosters.yaml:3003` (H-08); `data/fixtures.py:108,484` |
| 2 | capacity | `capacity_floor.floors` per site kind | int (dwelling 1, rest 0) | REQ | HAS | `rosters.yaml` capacity_floor (H-167); `fixtures.py:170,487` |
| 3 | standing gap | `standing_band_floors` | tuple int | REQ | HAS ((500,); swept (), (250,500,750)) | `fixtures.py:471` (H-223); `loop/matter.py:187-240` |
| 4 | hunger | `hunger_band_floors` + roster `hunger_bands` [starving, hungry, lean, fed] | tuple int; roster ordered, >=2 | REQ | HAS ((1,2)) | `fixtures.py:477`; `rosters.yaml:1705-1715` (REM-50) |
| 5 | scar | `SCAR_WEIGHT_SHIFT_AT` 2, `SCAR_CRISIS_AT` 3 | int, "ruled, not swept" (ED-IN-0261); scar threshold 1 (destabilise) has no reader | REQ | HAS | `queries/person_q.py:711-716` |
| 6 | scar | `scar_weight_shift` (fraction) | float, swept | REQ | HAS (fixture) | `queries/person_q.py:771-796` |
| 7 | thread gate | `thread_sensitivity_gate` | int; swept 0/30/50 (50 declared not run) | REQ | HAS (30) [ASSUMPTION, H-239] | `data/fixtures.py:1000`; `verb_table.yaml:1623-1634` (`thread_read`) |
| 8 | told drift | `told_drift_band` | float | REQ | HAS (0.5) | `fixtures.py:834` |
| 9 | docket crossing (B4.1) | floors on a seated person's own-ledger deed claims that raise a bench question | tuple, `()` = control | PLAN (held) | NONE | `00_THRUST_LAYER_DESIGN.md:254,456`; `v10_part12.md:19` ("B4.x stay held"); 07c A5 family B "B4.1 HELD, no owner" |
| 10 | arc-driven summons | summons hook for 19 arcs flagged `forced_by_threshold: yes` | no carrier | PLAN | NONE | `appendix_A5_events_and_arcs.md:108` |
| 11 | classification | ENDINGS_CLASSIFIED: 50 rows (18 unforced DECIDER/ROLL, 11 forced, 8 THRESHOLD, 9 NEVER, 2 UNCLEAR per 07c:24; unmeasured by me) | per-arc class | — | HAS | `engine/season/ENDINGS_CLASSIFIED.yaml` (endings agent's scope) |

Owed:
- Band edges for B4.1 docket crossing: "fixture floors; `()` = control" — none authored (`00_THRUST_LAYER_DESIGN.md:254`).
- Values for the "INVENTED" floors in `band_floors` are Jordan's to confirm (`rosters.yaml:3011`, H-08).

Conflicts:
- `thread_sensitivity_gate` 30 (fixture, `fixtures.py:1000`) vs `DEPTH_TS_MINIMUM` Object/Personal 30 (`systems/threadwork/sim/operations.py:95-102`) — same number held in two owners (the sim reads no fixture).
- `systems/overview` / design prose cites Church Attention Pool etc. as threshold-driven; no code in engine/season (grep: 0 hits for church_attention, thread_debt, mending_stability in `engine/season`).

Belongs elsewhere: `scale_of_rung` map -> geography/rung agent (listed in §8).

---

## 4. CONDITIONAL / TRIGGERED ARC (arc deck, goal stages)  — carrier/loader: `engine/season/data/goals.py` (`goal_stages:` key in `engine/season/goals.yaml`)
Population now: `goal_stages:` = absent (reads `[]`); 38 goal rows, 0 carry `axis:`. Arc ladders content = 0.   Status: EMPTY (schema BUILT)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | stage-row `id` | unique string | REQ | NONE | `goals.yaml:38-50`; `data/goals.py:414-463` |
| 2 | precondition target | `for:` goal ids | non-empty list of goal ids; never an `orientation` goal; a goal in at most one row | REQ | NONE | `data/goals.py:441-461` |
| 3 | stages | `stages:` list | ordered, >= 2, keys `{id, term, predicate, pursuits}` and no other | REQ | NONE | `data/goals.py:379-412` |
| 4 | stage | stage `id` | unique within row | REQ | NONE | `data/goals.py:381` |
| 5 | stage | `term` | enum {short, medium, long} (`rosters.yaml:2055-2067`), never decreasing along row | REQ | NONE | `data/goals.py:385` |
| 6 | stage (condition) | `predicate` | a `requires_typed` cell with `of: subject`; may not ask `WORLD_ONLY_STEMS` or `LEDGER_DERIVED_STEMS`; read person-side off the ledger | REQ | NONE | `goals.yaml:46-48`; closed stem set `data/requires.py:794-797` |
| 7 | stage | `pursuits` | `{<pursuit of canonical 15>: weight > 0}`, >= 1 | REQ | NONE | `goals.yaml:49-50` |
| 8 | struck keys | `deadline`, `closing`, `successor`, `deal` | NOT in schema (M20; excluded) | — | STRUCK | `goals.yaml:40-41`; `v10_part6.md:167-173,200` |
| 9 | exits / branch | arc exits, branches | no carrier: succession via `commit`/`release` by the person's own acts; branch = none | PLAN (excluded) | NONE | `00_THRUST_LAYER_DESIGN.md:238-241` (struck) |
| 10 | content | ladder content per axis (B6.n), ordered by buildability A,B,C,D,E,F,G,H,I | one axis per position | PLAN (held) | NONE | `00_THRUST_LAYER_DESIGN.md:332-418,460`; `v10_part12.md:19`; `v10_part6.md:206` ("Content, not questions") |
| 11 | arc rule | B6.n draws only from the first two ENDINGS_CLASSIFIED classes | rule | PLAN | NONE | `v10_part12.md:19`; `v10_part6.md:218` |
| 12 | arc corpus | 55 arc numbers (58 titles), ENDINGS 50 rows, 97 ARC cases + 46 NPC = 143 cases; arcs 46-55 unclassified | corpus | reference | HAS (corpus, never runtime) | `07c:22-28`; `appendix_A5:97-129`; ED-IN-0225 |
| 13 | NPC arc maps | Himlensendt C, Vaynard A/B (bodies lost in v30; "triggers RETIRED") | content to transcribe as goal rows + ladders | PROPOSED-ONLY | NONE | `07c:68` |

Owed:
- Every ladder (0 of the up-to-10 axes have one). Stage predicates, pursuits and terms per axis: `00_THRUST_LAYER_DESIGN.md:340-418` (PROPOSED-ONLY text; stems named there are gaps where not in `REQUIRES_STEMS`).
- Referent-bearing goal rows for axes whose only row is `orientation` (`goals.yaml:24`): axes 2 (hide), 4 (caste), 5 (purge Altonia, needs `off_katepano`/`off_kommerkiarios` seat_holders -1), 8 (community benevolence, needs a `rung` row), 10 (revive Einhir) — `00_THRUST_LAYER_DESIGN.md:336-338,350-352,385-387,401,406`.
- Org kind `org: {rung: <populated rung>}` for cohort identity thrust (PROPOSED-ONLY, `00_THRUST_LAYER_DESIGN.md:150-157`).
- B3.2 (R2 + R3') released but R3' pulse and deadline excluded (T-c), `v10_part6.md:200`.

Conflicts:
- Thrust design speaks of `ladders:` / `deadline` / `closing` / `successor` / `deal`; code is `goal_stages:` with none of those keys (`data/goals.py:61`, `goals.yaml:38-41`). Code wins.
- Design §6 labels "axis 9 heal the Calamity" and "axis 2 hide thread truth"; 07c/A5 count the ENDINGS denominators differently ("50 of 55" is wrong; 48 ARC rows + EMG-10/11, `appendix_A5:128`).

Belongs elsewhere: goal rows themselves (38; org goals) -> goals/organizations agent. Event/Tension cards -> other agent.

---

## 5. THRUST AXES (CL-THRUST axes roster)  — carrier/loader: `engine/season/rosters.yaml:2028` read by `engine/season/data/goals.py:236-248`
Population now: 14 members (10 user axes + 4 opposite poles), 6 `opposes:` pairs (measured). 0 goal rows tagged `axis:` of 38.   Status: AUTHORED (roster) / EMPTY (tagging)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | roster | `values` (closed, editable) | suppress_einhir_revival, hide_thread_truth, overthrow_church, overthrow_caste, purge_altonia, political_authority, faction_standing, community_benevolence, heal_calamity, revive_einhir, reveal_thread_truth, uphold_church, uphold_caste, altonian_ascendancy | REQ | HAS [ASSUMPTION; medium] | `rosters.yaml:2043-2046` |
| 2 | roster | `opposes:` pairs (6 keys; the loader refuses a pole not in `values`) | suppress_einhir_revival<->revive_einhir, hide_thread_truth->reveal_thread_truth, overthrow_church->uphold_church, overthrow_caste->uphold_caste, purge_altonia->altonian_ascendancy | REQ | HAS | `rosters.yaml:2047-2053`; `data/goals.py:236-248` |
| 3 | tagging | goal row `axis:` | a `thrust_axes` member; refused on `orientation` rows | OPT | NONE (0 of 38) | `goals.yaml:33-35`; `data/goals.py:272-281` |
| 4 | stage terms | roster `goal_stage_terms` | [short, medium, long] ordered, no durations | REQ | HAS [ASSUMPTION] | `rosters.yaml:2055-2067` |
| 5 | ARC predicate | `arc_effect_fields` rosters ARC_SELF / ARC_WORLD | `(kind, field)` pairs keyed on write class | PROPOSED-ONLY | NONE as roster; reader `harness/arc.py` built (B10-02) | `00_THRUST_LAYER_DESIGN.md:65-75` (design says this roster is "not enough" per review 2026-10-28) |
| 6 | pole counts | axes with a referent-bearing goal row | e.g. 1 political_authority (rows exist), 7 faction_standing (2 foreign seat rows only) | — | PARTIAL | `00_THRUST_LAYER_DESIGN.md:340-418` |

Owed: the user's list is "not exhaustive" (`rosters.yaml:2035`); no further axes supplied. The axis-to-affiliation/pursuit mapping is not a carrier.
Conflicts: design `arc_effect_fields` roster is NOT in `rosters.yaml` (grep: only the thrust design names it); B2.1 landed with `thrust_axes` only (`goals.py:20`).

---

## 6. CONVICTION / TRUTH TRACKS (ED-IN-0251)  — carrier: `Person.conviction` `state/carriers.py:746`; roster `affiliation_roster` `engine/engine_params/descriptors.json` via `rosters.yaml:574`
Population now: 5 affiliations; 5 of 10 incompatibility pairs filled.   Status: PARTIAL

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | roster | affiliation names | solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics (count 5) | REQ | HAS | `descriptors.json` `affiliation_roster`; `rosters.yaml:574-582` |
| 2 | roster | `scale` | int floor 0, ceiling 5 | REQ | HAS | `descriptors.json`; `state/carriers.py:738-745` |
| 3 | roster | `concerns` grouping | church:[solmund_orthodoxy, inner_tradition], einhir:[einhir_restoration], altonia:[altonian_civics] | REQ | HAS | `descriptors.json` |
| 4 | per person | `conviction: {affiliation: int 0-5}` (absence = not held; stored 0 = held rejection) | cast row key `affiliations:` | OPT per person | per-cast (not counted here) | `data/cast.py::conviction_of`; `data/affiliations.py::conviction_map` |
| 5 | strain | `incompatible` half-matrix (10 pairs): true / false / null | bool or null; unkeyed pair, self-pair, double key refused | REQ | HAS: 5 filled (solmund_orthodoxy x inner_tradition true, x thread_truth true, x einhir_restoration true, inner_tradition x thread_truth false, thread_truth x einhir_restoration false), 5 null (inner_tradition x einhir_restoration; 4 altonian_civics pairs) | `rosters.yaml:3055-3092`; `data/affiliations.py::_load_incompatible` |
| 6 | act effect | `affiliation_engagement` verb x affiliation cells (signed; only sign read) | signed int / null | REQ | HAS (table; e.g. `thread_read` -1 / +1 / +1 on three affiliations) | `rosters.yaml:3098-3170`; `data/affiliations.py::engagement` |
| 7 | crisis | scar thresholds 2, 3 | see §3 row 5 | REQ | HAS | `queries/person_q.py:711-716`; `loop/resolve.py:677-702` |
| 8 | tracks | Truth / PT tracks (the "absorbed" tracks) | no track store; confliction DERIVED | DERIVED | — | `rosters.yaml:3062` comment; `queries/person_q.py::confliction` |
| 9 | caste | "caste" as a Query over convictions on einhir_restoration/thread_truth/inner_tradition poles | no store | PROPOSED-ONLY | NONE (no caste code in engine/season) | `00_THRUST_LAYER_DESIGN.md:408-410,501` |

Owed: pair 6 (inner_tradition x einhir_restoration) "knife-edge is Jordan's to promote" (`rosters.yaml:3078`); four altonian_civics pairs null "no source" (`rosters.yaml:3085-3089`).
Conflicts: `affiliations` roster note says "count 4" in its `source:` (`rosters.yaml:575-576`) while descriptors.json holds count 5 and the roster has 5 names. Code (`descriptors.json`) wins.
Belongs elsewhere: per-person `affiliations:` values on the 46 cast rows -> NPC/cast agent.

---

## 7. THREAD SENSITIVITY / THREADWORK  — carriers: `Person.thread_sensitivity` (`state/carriers.py:756`), `systems/threadwork/sim/*.py` (unwired)
Population now: `ts:` present on 32 of 46 `references/npc_registry.yaml` rows, non-null on 10 (NPC-001 "75–80", NPC-002 "~50", 003 25, 004 15, 005 35, 020 28, 030 0, 070 0, 075 60, 080 0); the rest `null # [GAP]` or key absent.   Status: PARTIAL (TS gate carrier) / PLAN (everything else)

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | per person | `ts:` | whole int >= 0, or `NN–MM` (lower bound), or `~N`, or null (null = UNKNOWN, cannot attempt); other shapes REFUSE | OPT | 10 of 46 non-null | `data/cast.py:272-310`; descriptor `prac.thread_sensitivity` floor 0, ceiling open (reference 100) `engine_params/descriptors.json:123` |
| 2 | gate | `thread_sensitivity_gate` | int | REQ | HAS 30 [ASSUMPTION] | `fixtures.py:1000` |
| 3 | verb | `thread_read` requires `Thread Sensitivity >= 30`; writes nothing | — | REQ | HAS | `verb_table.yaml:1623-1634` |
| 4 | `thread_substrate` knowledge kind | roster `[mundane, thread_substrate]`; "gates nothing yet" | closed pair | — | HAS, read by nothing | `rosters.yaml:1490-1499` |
| 5 | thread operations (sim, unwired) | operation entry points: leap, weaving, pulling, past-pulling, locking, dissolution, mending | 7 | PLAN (no loop carrier) | sim HAS | `systems/threadwork/sim/operations.py:1-30`; `module_contracts.yaml:300-323` |
| 6 | thread inputs | `TN_STANDARD` 7; `DEPTH_OB` (Object 1, Personal 2, Relational 3, Field 5, Structural 8, Foundational 13); `MENDING_OB` (2/4/7/12); `DEPTH_TS_MINIMUM` (30,30,50,50,70,90); `BREADTH_OB` (Single 0, Small group 1, Formation 2, Battlefield 3, Regional 4); `DISTANCE_OB` (Contact/Close 0, Near 1, Distant 2, Far 3); Leap Ob by TS (30-49: 2; 50+: 1) | ints, `[canonical: params/threadwork.md]` | PLAN | HAS (sim module) | `operations.py:73-124` |
| 7 | thread outputs | `COHERENCE_COST_BY_SCALE` (Object 0, Personal 0, Relational -1, Field -1, Territorial -1, Structural -2, Foundational -2); `FR_SURCHARGE` -1; `MENDING_COHERENCE_COST` 0 (ED-871); `RESILIENCE_GAIN` 0 (sweep 0/1/3; slot name unruled); `RESTING_POINT_MEND_BY_DEGREE`; mending stability delta REPORTED, written nowhere | ints | PLAN | HAS (sim) | `operations.py:128-168,451` |
| 8 | Coherence track | `RESTING_POINT_START` 0, `ELASTIC_RANGE` 6, `HUMAN_BAND_LIMIT` 5, `DISPLACEMENT_DISSONANT_LOW` 2, `..._FRAGMENTED_LOW` 4, `..._FRACTURED_LOW` 6, `ELASTIC_RETURN_PER_SEASON` 6; bands Stable/Dissonant/Fragmented/Fractured/Coherence failure | all `[JUSTIFIED ... edge invented, ED-WR-0010]` | PLAN | HAS (sim); no `Person` coherence field in season loop | `systems/threadwork/sim/coherence.py:113-139`; A5/07c:69 ("no Person coherence field") |
| 9 | co-movement | 15 `CO_MOVEMENT_CARDS` (CM-01..CM-15; each: ms_delta actualized/unactualized + effect text) | tuple rows | PLAN | HAS (sim) | `systems/threadwork/sim/co_movement.py:42-60` |
| 10 | opposing / knot | `OPPOSING_OB_MODIFIER_MIN` 1; `KNOT_STRAIN_*_LOSER` 1/2; `KNOT_COMPOSURE_*` 2/4 loser, 1/2 winner; `KNOT_DISSOLUTION_WOUND` 1 | ints | PLAN | HAS (sim) | `systems/threadwork/sim/opposing.py:48-60` |
| 11 | collective | `LATTICE_FRACTURE_OB_PENALTY` 1 | int | PLAN | HAS (sim) | `systems/threadwork/sim/collective.py:43` |
| 12 | rendering | `PERCEPTION_BANDS`; `RENDERING_STRAIN_PER_BEYOND_SCENE` 1, `..._PER_EXTERNAL_OP` 1 | table + ints | PLAN | HAS (sim) | `systems/threadwork/sim/threadcut.py:37-51` |
| 13 | thread type / thread sensitivity "type" | no carrier: no thread-type roster in code (grep: 0 hits for thread_type in engine) | — | PLAN | NONE | grep (none) |
| 14 | tenth attribute / TS as attribute | TS as person attribute; "nine keys, pending slot refuses a value" | HELD on J-T2 | PLAN | NONE | `appendix_A5:105` citing `v10_part12.md:272`; CL-ATTR `v10_part12.md:12` |
| 15 | TS gain | "TS gains on anomalous claims" (arcs family G) | no reader | PLAN | NONE | `appendix_A5:105`; `Person.thread_sensitivity` "NEVER WRITTEN IN PLAY" `state/carriers.py:749` |
| 16 | world Thread substrate | a MATTER condition on Thread sites (Escalation 1) | not built | PROPOSED-ONLY | NONE | `appendix_A5:107,142` |
| 17 | heal-Calamity act | thread-operation act (IN-35/IN-06); axis 9 unbuildable | no verb | PLAN | NONE | `00_THRUST_LAYER_DESIGN.md:416-418` |
| 18 | thread-witnessed adjacency | 4 Thread-Witnessed edges, BFS bypass at TS >= 30 | geography YAML | reference | HAS (`systems/settlements/valoria_geography_v30.yaml`, settlement_adjacency) | `references/propagation_map.md:116-146` (patch log; not verified against YAML by me) |

Owed: the 36 cast rows with no `ts` value (46 − 10); the unruled `resilience` slot name; mending stability destination (reported, written nowhere); every threadwork→season-loop carrier (no verb opens thread operations: `tie / knot` has no opener `rosters.yaml:141-143`, per thrust design `:383`).
Conflicts:
- `module_contracts.yaml:302` doc pointer `.designs/systems/threadwork/reference/threadwork_v30.md` (quarantined; not read) and its header note "design proposal, requires editorial approval" vs CANONICAL POOL NOTICE: `[OPEN — Jordan]` (`module_contracts.yaml:315`).
- `rosters.yaml:2779` lists threadwork as `kind: loop_resident` while contract row says `build: unwired` and the verb note says no loop carrier.
- Coherence/band edges in the sim are tagged `[JUSTIFIED ... invented]`, ruled mechanism, unruled magnitude.

Belongs elsewhere: Church Attention Pool (CM-11/CM-13 effects), Thread Debt — church/faction agent, no code carrier found.

---

## 8. SCALE TRANSITIONS / CALENDAR-SEASON STRUCTURE / HORIZONTAL INTEGRATION / PROPAGATION
Population now: scale map total on 8 rungs; propagation_map.md is a patch log.   Status: PARTIAL

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | scale | `scale_of_rung` map | rung kind -> {Personal, Relational, Territorial, Structural}; person Personal, hearth Relational, community Relational, settlement/territory/province/duchy Territorial, realm Structural; `Object` reachable by nothing | REQ (total on `rung_kinds`) | HAS | `rosters.yaml:272-330` |
| 2 | scale transitions | Personal->Thread, Thread->Faction, Thread->Mass transition rules | contract rows only | RETIRED-KEY | NONE (code) | `references/module_contracts.yaml:309-312` (Key-era `transitions: via scale_transitions §3.x`; `scale_transitions_v30.md` is quarantined). Live equivalent: `scale_of_rung` (row 1) and the `rung` containment walk `ancestry(w, venue)`; no scale-transition thresholds exist in the loop. |
| 3 | season structure | six steps, four barriers; `w.tick` the only season count; year = `len(season_factor_draw)` (off) | — | DERIVED | — | `loop/driver.py:239-253`; 07c:83 |
| 4 | horizontal integration / propagation inputs | no carrier; `references/propagation_map.md` records patches (MS/IP/CI propagation), not a schema | — | reference | n/a | `references/propagation_map.md:12,73,83,116` |
| 5 | thread->scale | scales `[personal, thread]` for threadwork; Thread->Mass handoff via `sim/cross_scale/handoff_rules` | — | RETIRED-KEY | `sim/` dissolved (CLAUDE.md §3); referenced in `operations.py` docstring | `module_contracts.yaml:300-306` (Key-era row, `parity: key-log`). Live equivalent: none for Thread->Mass; `systems/threadwork/sim/*` constants (§7 rows 6-12) are code but unwired. |

Owed: scale-transition thresholds in code form (none authored); calendar structure beyond tick ordering (year length, season names): none supplied, off.
Conflicts: `operations.py` docstring depends on `sim/autoload/dice_engine` and `sim/cross_scale/handoff_rules`; `sim/` is a dissolved tree (CLAUDE.md §3). Unverified whether these imports resolve (I did not run them).

---

## Key-retirement re-check (orchestrator correction, ED-IN-0232)
Rows re-marked `RETIRED-KEY`: §1 row 14, §8 rows 2 and 5. Not marked: §7 rows 5-12 (constants in `systems/threadwork/sim/*.py`, cited to code and `params/threadwork.md`, not to a Key source; I did not open `.designs/` or `threadwork_v30.md`, so whether those sim modules import Key machinery is unverified) and §8 row 4 (`propagation_map.md` is a patch log, reference only). No `clock_registry`, `propagation_spec_v1` or `thread_horizontal_integration` source exists outside `.designs`/archives (grep 0 hits in engine/references), so no row rests on them.

## 9. Follow-up (orchestrator, same file)

**(1) Key grep over threadwork sim.** `grep -nEi "keystore|keys\b|\bkey\b|echo|emit|consume|import keys" systems/threadwork/sim/*.py systems/threadwork/__init__.py` returned 6 lines, none a Key-substrate use: `co_movement.py:46` ("Echo Cascade", a card name), `coherence.py:142` ("Key: actor id", a dict-key comment), `:268` (snapshot dict key), `:415` (prose "consumer"), `collective.py:102` (`sorted(key=...)`). No import of keys/KeyStore/echo/emit. Result: §7 rows 5-12 stay NOT RETIRED-KEY (code is Key-free). The only Key-dependent threadwork rows remain the contract-row ones already marked (§1 row 14, §8 rows 2, 5).

**(3) Which loader reads `ts`.** The cast loader `engine/season/data/cast.py::thread_sensitivity_of` (`cast.py:283-310`) reads the `ts:` key of a row from `references/npc_registry.yaml` (`NPC_REGISTRY_YAML`, `engine/season/data/files.py:159`; loaded by `cast.load()` `cast.py:112`, per-row `cast.row()` `cast.py:117`). One path, not two: the cast loader IS the reader of npc_registry. Called once per person at world build (`harness/populated.py::build_realm`, per `cast.py:292`). The "32 present / 10 non-null" count in §7 row 1 is from loading `references/npc_registry.yaml` directly, which is the same file `cast.load()` reads (this resolves the earlier open question).

**(2) Workplan v10 hits (all parts; hit cards only).** Generic word "clock"/"threshold" hits are mostly retire/IRRELEVANT ledger rows (e.g. `v10_part10.md:29`: Mending Stability clock "struck", `matter.py:175`; `:130` world MS clock has no season analogue). Cards that call for threadwork/threshold/TS content:

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | threadwork build | CR-13: Partial/Failure Leap each nets 0 Coherence; Weaving keeps blanket penalty (fixes `operations.py::_resolve_operation` extra charge) | oracle edit | PLAN | NONE (code still charges extra, per card) | `v10_part4.md:107`; exit `v10_part3.md:207` |
| 2 | threadwork build | REM-45 pool(h=3) − pool(h=0) is exactly 3 | falsifier | PLAN | NONE | `v10_part3.md:207` |
| 3 | threadwork host | CP-T07-02: Leap stage, one working host, actor adapter, `Person.coherence` carrier; stored `spirit` reads `attr.mind.will` via a `faculty` addend | carrier + adapter | PLAN | NONE (`Person.coherence` absent from `state/carriers.py`) | `v10_part3.md:216`; shared files `:209` (`seam/wrappers/threadwork.py`, `Site.locked`, `rosters.yaml: thread_scales`, `verb_table.yaml` `weave`, `lock`) |
| 4 | threadwork roster | `rosters.yaml: thread_scales` (+ cells) | roster | PLAN | NONE (grep `thread_scales` not found in rosters) | `v10_part3.md:209` |
| 5 | verbs | `weave`, `lock` on Sites (CP-T07-03); `mend` (locked Site / other person / self, with a price on self-repair) (CP-T07-04); `ward` (CP-T07-11); `thread_read` finds (CP-T07-10) | verb rows | PLAN | NONE for weave/lock/mend/ward; `thread_read` exists (writes nothing) | `v10_part3.md:217,220,223,225` |
| 6 | threshold | `coherence_band_floors` Fixtures tuple, shipped `()`, counted by `bands_below` (permanent set narrows the season) | tuple of ints, `()` = control | PLAN | NONE | `v10_part3.md:222` (CP-T07-07) |
| 7 | equilibrium | equilibrium decided by place (locked-Site gate) | gate | PLAN | NONE | `v10_part3.md:218` (CP-T07-05) |
| 8 | recovery | recovery as a projection written at next seam write | rule | PLAN | NONE | `v10_part3.md:221` (CP-T07-06) |
| 9 | threadwork cells | every thread row a witnessable, celled deed: affiliation cells now; pursuit cells wait on JQ-3 | data cells | PLAN | NONE | `v10_part3.md:219` (CP-T07-09) |
| 10 | breach | crossing as a witnessed breach (Event only, no outcome slot) | Event | PLAN | NONE | `v10_part3.md:224` (CP-T07-08) |
| 11 | strain source | strain row waits on H-236's source (Calamity source in realm) | — | PLAN (blocked) | NONE | `v10_part3.md:217`; `v10_part11.md:42` (G-21: Calamity has no source; 0 threadwork modules loaded in a season) |
| 12 | threshold (held) | B4.1 threshold-raised docket crossing, HELD on `determine` executing (H-163, IN-12, CP-T09) | see §3 row 9 | PLAN (held) | NONE | `v10_part11.md:106`, `:35` (G-14) |
| 13 | tenth attribute | J-T2: TS or Recall as the tenth attribute; nine-key default, pending slot refuses a value | name | PLAN (held, Jordan) | NONE | `v10_part4.md:154`; CL-ATTR `v10_part3.md:402` |
| 14 | axis H content | G-24 "hide the threadwork truth": no goal row and no record kind for the truth; holder = Church per D2 [ASSUMPTION] | goal row + record kind | PLAN (held with B6.n) | NONE | `v10_part11.md:45,74` |

Further conflict: `v10_part4.md:111` says the season loop does not reach threadwork ("`matter.py:135`: threadwork module stays unplugged"; nothing under `engine/` imports it but one test), consistent with `module_contracts` `build: unwired`; `rosters.yaml:2779` still lists it `loop_resident`.

Updated row count: 84 + 14 = **98**.

## Row counts (before follow-up)
§1: 14 · §2: 8 · §3: 11 · §4: 13 · §5: 6 · §6: 9 · §7: 18 · §8: 5 = **84 parameter rows**.

## Unresolved
- Whether the `ts` shape count "32 present / 10 non-null" in `references/npc_registry.yaml` is the same row set `data/cast.py` loads (the cast loader file path was not opened beyond `thread_sensitivity_of`).
- Which of workplan v10 parts 4/9–11/13 carry additional CL-/threadwork cards: not read (only parts 6, 12 and `10_part6` greps).
