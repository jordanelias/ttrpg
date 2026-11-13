# Holistic audit — the game as a suite of engines

## Status: REFERENCE (stage 3 of `STAGES.md`; an audit; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: `4dc8a7b` (working tree, 2026-11-12; `ff2f508` landed during the run and touches the suite directory only: `git diff --name-only 4dc8a7b ff2f508 -- engine modules tools references architecture` prints nothing). Producer: Fable, the holistic lane. Companions: `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` (the edits, items `CI-01` to `CI-11`), `master/HOLISTIC_FOR_JORDAN.md` (what survives the ladder).

**Words.** The glossary's plain words are used in prose (`unified/U1_GLOSSARY.md` §H): a *setting* is a
`Fixtures` field; the *act-count instrument* is `harness/aperture.py`; a *dataclass* is one of the typed
input or outcome classes of `queries/inputs.py`; a *hot file* is one of the files `U3` §1.1 lists as edited by
twenty or more proposals. "The season core" is this audit's short name for `engine/season/loop` and `state`
(the write gate, the fold, the stores); "reach" is the share of function lines a named run entered. `04`
is `architecture/meta/04_CODE_ARCHITECTURE.md`, read at `4dc8a7b`; Jordan's amendments of 2026-11-12 (A-97)
were being applied to it during this run and move no line number cited here.

Parts: this file (§0 verdict, §1 method and limits, §2 the engines, §3 what the loop calls), `_part2`
(§4 findings ranked, §5 the six directions, §6 attacks that failed), `_part3` (§7 the nine requirements,
§8 port cost, §9 evidence log). Finding ids are `H-01` to `H-13`.

## 0. Verdict

**The season loop's core is a sound base for a suite of engines and the suite is not yet organised as one.** What
holds, on execution evidence: one write gate, one fold and one loader; the season package imports no
module by name (0 import edges from `engine/season` to `modules/`, `W2`); every registered module is
reached through a composition row (16 rows, `W3`); the typed input dataclasses sit in one
standard-library-only file a module can import without loading the host (measured, §6); and two seeded realm runs enter 84 to
97 % of the function lines of `loop/`, `state/`, `decision/`, `data/`, `seam/` and `manifest/` (`W4`).
Same seed, same content hash, three times over (§9).

What does not hold, worst first:

1. **The engines are reached unevenly and by seed (H-01).** At seed 0 the personal-combat engine
   (`modules/combat`, 195 functions) is entered by no function in three seasons; the field resolver is not
   entered until the third; six of the sixteen composition rows are entered in none of three realm runs; the army
   verbs' effects (`loop/effects_army.py`, ten functions) never run. This is R-05's shadow at the scale
   of engines and it is the largest obstacle to the standing requirement that each subsystem plays.
2. **The game has no entry point of its own (H-02).** The realm builder (982 lines), the chooser's
   composition and the run loop live in the instrument package `harness/`, which Layer 1's nine modules do
   not name; six harness files build worlds by assigning stores directly (71 sites); two tools import
   `harness` to obtain "the game".
3. **More than half of the source is prose, and the two largest runtime registries are about 70 %
   annotation (H-03).** Of 81,908 non-blank lines of non-test Python, 39,502 are code; `rosters.yaml` and
   `verb_table.yaml` (713 KB together) carry about 500 KB of notes, sources and comments. Every later batch
   pays for it in reading: `rosters.yaml` is edited by 130 proposals.
4. **The season's 101 tuning values have no typed export (H-04)**: they are keyword arguments of one
   Python call, which the constant exporter does not see; the port's parity file maps five constants.
5. **One host site reaches a module attribute no composition row names (H-05).**
   `seam/wrappers/sigma.py:246` imports the social-contest module by reflection and calls `obstacle`, 102
   times in one season. (A second observation there, two lookups for one row, was attacked and needs no
   edit.)

Dead and inert code is the census lanes' subject and is cited, not repeated (§4, H-10): the code is not
littered with dead records, it is starved at the verbs (`audits/17_CENSUS_REST.md` §0).

The improvement proposal's answer is eleven items, every one of them hash-EQUAL for the game's worlds,
placed in two existing batches and two new ones before the calibrated landings so that every later batch
reads less, plus one question for Jordan (where the game's entry lives). None is a guard.

## 1. Method, partition and limits

**Subject.** `engine/season/`, `modules/`, `engine/substrate/`, `engine/dice_engine/`,
`engine/engine_params/`, `tools/` and the registries they read. Measured by `git ls-files` and `ast`
(`master/work/W1_AREAS_AND_LINES.md`): 293 Python files under `engine/` (131,180 lines, of which
`engine/season/tests/` is 166 files and 71,169 lines), 57 under `modules/` (18,213 lines), 54 under
`tools/` (15,016 lines). The line count overstates the code: see H-03.

**Instruments used** (the methods of three ratified skills, as planning instruments only; no edit was
made to the tree): `layer-conformance` Lens A (placement), `valoria-simplify` SURVEY (the map M1 to M6, the
six directions) and its DISTIL rules as a *plan* (EARN, the control C1 to C6, the ladder), then
`layer-conformance` Lens B (rows of `architecture/meta/04_CODE_ARCHITECTURE.md`, called `04` below, read
at the line). The plants of `valoria-simplify` C2 were **not** run by this lane (they need a worktree and
edits); every item in the improvement proposal therefore names its plant as a step of its own gate.

**The partition, and why.** By the areas `valoria-simplify` M1 defines, grouped by what one engine is:

| # | partition | areas | why it is one reading |
|---|---|---|---|
| P1 | the season core | `engine/season/loop`, `state`, `gaps.py`, `trace_log.py` | one write gate, one fold, seven steps |
| P2 | the chooser and the readers | `engine/season/decision`, `queries`, `epistemic.py` | what a person reads and how he picks |
| P3 | the data channel | `engine/season/data`, `manifest`, the YAML registries, `engine/engine_params`, `engine/substrate` | every fact code reads and its loader |
| P4 | the resolvers and their seams | `engine/season/seam`, `modules/*`, `engine/dice_engine` | the draw, the ladder, the registered modules |
| P5 | the instruments | `engine/season/harness`, `engine/reference` | what observes the game |
| P6 | the apparatus | `tools/` | exporters (load-bearing on the game) apart from process gates |

**Shared reading, forked judgment.** The reading was shared in two ways. (1) The dossiers, digests,
census lists and the grounding audit (`dossiers/`, `digests/`, `census/`, `audits/17_CENSUS_*`,
`audits/25_GROUNDING_ENGINE.md`) already hold the per-file reading; they are cited, not redone. (2) The
mechanical extraction was done once by throwaway `ast` probes and seeded runs, and written as
fixed-format extract files under `master/work/` (`W1` to `W6`). **No reader agents were spawned: this
lane's toolset held no agent-dispatch tool** (stated in the receipt), so the per-partition extraction
the brief assigned to `valoria-measure` and `valoria-author` readers was done by script instead, which
for counting and edge extraction is the cheaper tier in any case. The judgment in §4 onward is this
lane's alone. One round; no second wave.

**What this lane did not do** (carried forward, not hidden):

- It did not read the 39,502 code lines of non-test Python in full. It read heads, the seam files,
  the loaders' interfaces and every site a finding cites; everything else rests on the extracts and on
  the cited audits. A finding that rests on an extract says which.
- Of the suite's own documents it read in full the briefs, `unified/DECISIONS_ANSWERED.md` (A-1 to A-93;
  A-94 to A-97 at their rows when they landed mid-run), `audits/25_GROUNDING_ENGINE.md`,
  `dossiers/00_NINE.md` and the three skills; it read `unified/U3_DEPENDENCY_ORDER.md` at §0 to §2 and
  §5.1, the census audits and proposals at their heads and tables, and the glossary at §H and §I. **It did
  not read the per-subsystem dossiers, the digests, `U1_OWNERS_AND_VOCABULARY.md` beyond its headings or
  `U2_LAYER1_CONFORMANCE.md` beyond its head.** Overlap with the 300 proposals was checked by searching
  them for the symbols each item touches (§9 of part 3, row 12), not by reading them.
- It ran no `pytest`, no long run of the act-count instrument (`harness/aperture.py`), no `corpus_run` (eight minutes, already recorded by the CORE
  lane) and no C2 plant.
- It did not open `jordanelias/valoria-game` (not in this clone) and did not read the Godot reference
  for the ruled series (`ED-GO-0002`): no outbound read was made. **Every port-cost line in §8 is
  therefore a statement about the Python construct only, and the GDScript half is marked
  `[NOT READ]`** (`valoria-simplify` THE PORT NOTE requires the page; it was not read).
- `efficient-coding-review` excludes `tools/`, `tests/` and `systems/` from its subject (*"a standard
  pointed at the repository's own apparatus is the recursion CLAUDE.md §0.1 pt 5 exists to stop"*). The
  brief names `tools/`. This audit therefore reads `tools/` under one question only: which tools are
  load-bearing on the game (an exporter whose output the engine opens), and which are process apparatus.
  For the second kind the only dispositions offered are delete or leave; no guard, no grader.
- History: the clone is shallow (`.git/shallow` present; `audits/25_GROUNDING_ENGINE.md` §0), so the
  history instrument (I5: co-change, carried cost) did not run. The *over time* and *diagonal*
  directions are PARTLY at best and say so (§5).

## 2. The engines

Eleven engines, by what each owns. "Code" is code lines (`W1`: not blank, not a whole-line comment, not
a docstring). "Reach" is the share of function lines entered by the union of two realm runs (seed 0 for
three seasons, seed 2 for four; `W4`, method B). An engine is named by its plain function; the tree's
directory is given once in backticks.

| # | engine | what it is | code | owns (writes) | entry | reach |
|---|---|---|---|---|---|---|
| E1 | **the season core** (`engine/season/loop`, `state`) | the driver and seven steps; the stores, the write gate, the log, the id mint | 4,871 | every store, through `state/gate.py`; the log; the content hash | `SeasonDriver(w).season(chooser, ...)` (`loop/driver.py`) | loop 84 %, state 90 % |
| E2 | **the chooser** (`engine/season/decision`) | questions, options, budget, sheet, choice; no `World` in scope | 1,015 | nothing; returns scenes | `decision.make_chooser(fx, mint, verbs, draw)` (`decision/choose.py:488`) | 93 % |
| E3 | **the readers** (`engine/season/queries`, `epistemic.py`) | world-first and asker-first queries, barrier caches, the faction view, the typed input dataclasses | 2,801 + 241 | nothing | functions; `world_q` holds 191 of them | 76 % |
| E4 | **the data channel** (`engine/season/data`, `manifest`, `engine/substrate`, `engine/engine_params`) | the loaders of every roster, table, verb row, matrix row and setting (`Fixtures`); role-to-provider rows; the cooked exports and their leaf readers | 3,687 + 432 + 160 | the in-memory forms | import of `engine.season.data` (loads at import) | data 91 %, manifest 97 %, substrate 64 % |
| E5 | **the contest seam** (`engine/season/seam`) | `contest()`, the ladder, the four provider adapters and the pool reader | 835 | nothing | `seam.contest(...)`; `@provider(role, module)` | 90 % |
| E6 | **the dice engine** (`engine/dice_engine`) | the degree ladder (`degree_from_net`), the bell-curve roll and its leverage arithmetic | 216 | nothing | `sigma_leverage.roll_net`, `dice_engine.degree_from_net` | 72 % |
| E7 | **personal combat** (`modules/combat`) | the duel: range, tempo, weapons, wounds | 2,560 | nothing (returns a dict, `audits/25` V-02) | `modules.combat.fight:fight`, role `combat.fight` | 83 % (seed 2 only; 0 % at seed 0) |
| E8 | **mass battle** (`modules/mass_battle`) | the cell battlefield, units, orders, the army record | 5,194 | nothing (returns `attacker_wins`, `winner=`, `audits/25` V-01) | `massbattle:resolve_field` (role `mass_battle.resolve_field`); `armyrecord:apply` and three more query rows | 60 % |
| E9 | **the small modules** (`modules/social_contest`, `fieldwork`, `settlements`) | the social roll and its obstacle; the inquiry's finding; larder, produce, subsist, housing, fabric, fortification, provision | 36 + 8 + 152 | nothing | eleven composition rows | 100 %, 100 %, 86 % |
| E10 | **the instruments** (`engine/season/harness`, `engine/reference`) | probes, the corpus grader, the realm builder, the act-count instrument (`aperture.py`), registers, reports | 8,795 + 824 | `runs/results.json` (`report`), **and the realm itself** (H-02) | `python -m engine.season.harness.<name>` | not a game path |
| E11 | **the apparatus** (`tools/`) | eight exporters; CI gates; validators | 7,575 | the files under `engine/engine_params/` | CLI | not a game path |

Beside these sits `systems/*/sim` (15,779 lines, 539 functions): the retained per-subsystem oracle
scripts. No realm run enters one function of them (`W4`); they are reached by `engine/tests`
(`sim-regression`) and `tests/valoria`. Their retention is ruled (ED-IN-0283, CLAUDE.md §3) and their
per-subsystem retirement is already carried (H-10).

### 2.1 The seams between engines

| seam | from → to | how it is crossed | typed? | evidence |
|---|---|---|---|---|
| S1 | driver → steps | methods bound on `SeasonDriver` at the foot of `loop/driver.py` | tokens typed (`state/gate.py::Token`) | `04` §C.1 |
| S2 | steps → stores | `World.write(thing, token, apply, ...)` | receipt | `04` §C.2; `state/world.py:1138` |
| S3 | DELIBERATE → chooser | `choose(person, view, sensation, budget)`; no `World` | by module path: `decision/` imports `state/carriers.py` only (`W2`: five edges, all to `carriers.py`) | `04` §C.3 |
| S4 | RESOLVE → verb table | the one fold over `VERB_TABLE` rows; `@effect_for` bodies | row dataclass (`data/verbs.py::VerbRow`) | `04` §C.4 |
| S5 | RESOLVE/ENCOUNTER → contest | `seam.contest(...)` → `manifest` prize row → `@provider` adapter | **the adapters return a `dict`** (`queries/inputs.py:20-24`: *"the SEAM keeps one return shape"*) | `04` §C.5 says a `Margin` (for the field an end state, as amended 2026-11-12 under A-3 and A-97) |
| S6 | adapter → registered module | typed input dataclass → `MODULE_ENTRIES[role].fn(input)` | input typed (`queries/inputs.py`, 32 dataclasses); output typed for social contest (`Margin`), fieldwork (`Findings`) and settlements; **untyped for combat and mass battle** | `W3`; `audits/25` V-01, V-02 |
| S7 | readers → settlements module | `world_q._entry(role)` → `composition.require` | typed both ways | `queries/world_q.py:1353-1358` |
| S8 | effects → army record | `composition.require(ARMY)(ArmyCommand(...))` | typed input | `loop/effects_army.py:57`, `effects_information.py:119` |
| S9 | every roller → the draw | `random.Random(...)` built at seven files (14 sites, §4 H-10) | not one owner yet | `grep -rn "random\.Random(" engine/season modules engine/dice_engine`, tests excluded |
| S10 | data channel → code | `data/files.py` owns each path; `data/rosters.py::load_yaml` is the one YAML reader | refuses a duplicate key, an unknown column, an unread row | `04` §B.13 |
| S11 | exporters → engine | `tools/export_*.py --check` writes `engine/engine_params/*.json`; a leaf reader each | round-trip check | `W5` §2 |

## 3. What the loop actually calls (execution evidence)

All from `master/work/W3_SEAMS_AND_ROLES.md` and `W4_REACH.md`. Three realm runs, the shipped builder
and chooser (`harness/populated.py::build_realm`, `harness/probes.py::chooser`), `PYTHONHASHSEED=0`:

| run | seasons | content hash | control that the run happened |
|---|---|---|---|
| seed 0 | 1 | `5ab73af282d0779646c38839fbab85d8` | equal to `audits/25_GROUNDING_ENGINE.md` L-18; 13,379 Events; reproduced by two runs of this lane, and the three-season run's first season logs the same 13,379 |
| seed 0 | 3 | `52ff67bc45c5b956cd99215f6ba3097f` | log 13,379 → 37,646 → 74,510 Events |
| seed 2 | 4 | `b4bae063f33476988db678b5aae62a28` | equal to `audits/25` L-18 (the King's-death run) |

**One season at seed 0, calls crossing into a resolver** (`W3`, last table):

- the social roll: `seam/wrappers/sigma.py::resolve` → `modules/social_contest/roll.py::roll` **48**
  times; `sigma._composed_obstacle` → `roll.obstacle` **102** times; `dice_engine.degree_from_net` 48;
- the inquiry: `seam/wrappers/fieldwork.py::find` → `modules/fieldwork/find.py::find` **62**;
- settlements: `world_q.capacity` and `world_q.population` → `housing` **79**; MATTER → `produce` **1**,
  `subsist` **1**; `larder_draw` 1;
- mass battle: the adapter `seam/wrappers/mass_battle.py::resolve` is entered 3 times and
  `massbattle.resolve_field` **0** times;
- personal combat: **0** calls; `modules/combat/fight.py` is imported and not entered.

So in the first season of the shipped realm at seed 0, 13,379 Events come from 48 rolls of one roller,
62 graded findings and the settlement arithmetic. That agrees with the determinism lane's figure,
verified by the grounding lane, that 92.7 % of success Events at seed 0 carry no degree
(`audits/25_GROUNDING_ENGINE.md` L-15).

**Over more seasons and a second seed** (`W4`, method B):

| | seed 0, after season 1 | after 2 | after 3 | seed 2, after season 1 | after 4 |
|---|---|---|---|---|---|
| functions of `modules/combat` entered | 0 | 0 | **0** | 155 | 161 |
| functions of `modules/mass_battle` entered | 18 | 18 | 152 | 149 | 153 |

**The sixteen composition rows** (`W3`, first table): ten are entered in at least one of the three runs.
Six are entered in none: `mass_battle.army`, `mass_battle.army_order`, `mass_battle.army_options`,
`mass_battle.army_preset`, `settlements.drawn_under`, `settlements.fabric`. Two of the six
(`army_options`, `army_preset`) are called only from harness menus and would not be entered by a realm
run by construction; the other four are game paths no computed act reached.

**Files of the loop no run entered or barely entered** (`W4`, per-file table): `loop/effects_army.py`
0 of 10 functions; `loop/effects_founding.py` 1 of 9; `modules/mass_battle/armyrecord.py` 0 of 23;
`armies.py` 0 of 4; `orderofbattle.py` 0 of 6; `core/state.py` 0 of 5; `perimeter.py` 0 of 9;
`troop_types/presets.py` and `recruitment.py` 0 of 3 each. A function no run entered is **unobserved**,
not dead (`valoria-simplify` C5): the census lanes' verdicts on these files are the authority
(`audits/17_CENSUS_C1B.md`), and `audits/17_CENSUS_C1A.md` §0 already names the army, march, found, build
and establish effects as *"live as symbols and inert as game"*.
