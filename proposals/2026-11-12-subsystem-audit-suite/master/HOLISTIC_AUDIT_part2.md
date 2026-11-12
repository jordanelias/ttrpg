# Holistic audit — part 2: findings, the six directions, attacks that failed

## Status: REFERENCE (part 2 of `master/HOLISTIC_AUDIT.md`; resolves nothing at runtime)

Extract files are `master/work/W1` to `W6`. `CI-nn` is an item of `master/CODEBASE_IMPROVEMENT_PROPOSAL.md`.
Severity words are the suite's: *blocks a requirement*, *degrades*, *hygiene*.

## 4. Findings, worst first

### H-01 · The engines are reached unevenly, and which ones run depends on the seed — blocks a requirement (R-05, R-04)

**Claim.** The suite has five resolver engines and the shipped realm exercises two of them reliably.
Personal combat and the army record are reachable by declaration and are not reached by computed play at
a seed the instruments use as their default.

**Evidence** (`W3`, `W4`; §3). Seed 0, three seasons: 0 functions of `modules/combat` entered; mass battle
fought only from the third season. Seed 2: combat entered in the first season (155 functions). Six of
sixteen composition rows entered in none of three runs, four of them game paths (`mass_battle.army`,
`mass_battle.army_order`, `settlements.drawn_under`, `settlements.fabric`). `loop/effects_army.py` 0 of 10
functions, `loop/effects_founding.py` 1 of 9. The census lane's count at the verb level is the same
picture: 34 of 67 verbs execute in neither the corpus nor a three-season realm
(`audits/17_CENSUS_REST.md` §0); one season at seed 0 executes 26 verbs (`audits/25_GROUNDING_ENGINE.md` L-14).

**Falsifier, and its outcome.** A run in which every composition row is entered. The three runs made here
are that test and it failed for six rows. Control that the probe can see an entry: the ten rows it does
report are the ones whose callers `W3`'s profiler table shows by name and count.

**Consequence for the game.** A player at seed 0 sees no duel in the first year; a faction never raises or
organises an army by its own choice; a place is never founded. The standing requirement (*each subsystem is
a playable game, in conformance, integrated*) fails at "integrated" for combat's entry by the season and
for the whole army record.

**Minimal fix at the owner.** The fixes are the verbs' own and are carried: the task draw (B07), the
military verbs (B22), custody and force (B15, B29), founding and works (B12). What this audit adds is the
reading that lets a batch show it moved an engine and not only a verb: **CI-11**, an `ENGINES` block on
the existing instrument `harness/aperture.py` (rows entered, per role, per season), read at each batch
close beside `--requirements`.

### H-02 · The game has no entry point of its own — degrades (delivery of R-04 and R-05; the port)

**Claim.** What a player would call "start a new game and play a season" is three functions in the
instrument package, and what "a world" is has six builders.

**Evidence.**
- The realm: `engine/season/harness/populated.py::build_realm` (`:1014` to `:1995`, 982 lines), nine
  parameters, seven of them boolean arms (`from_roster`, `goals`, `goals_complete`, `foreign`, `guards`,
  `acquaintances`, `cast_attributes`; `:1014-1016`).
- The chooser's composition: `harness/probes.py::chooser` (`:278-292`), whose docstring says *"`soak`,
  `interactions` and `storybar` still compose it by hand"*.
- The run loop: `harness/populated.py::run` (`:2048-2077`).
- `04` §A.2 lists nine modules (`04:129-156`): `state`, `data`, `queries`, `decision`, `loop`, `seam`,
  `manifest`, `game`, `tests`. `harness/` is none of them; `grep -n harness architecture/meta/04_CODE_ARCHITECTURE.md`
  prints nothing. `04` F.31 (`:1231`) calls world generation *"a registry row read once at boot"*; the code's
  `World.boot()` checks roles and rows only (`state/world.py:1730-1744`) and `loop/driver.py:265` records
  that *"NOTHING ON A RUN PATH CALLS"* it.
- Six harness files build worlds by assigning the stores directly, 71 sites
  (`grep -rnE "\b(w|world|self)\.(persons|rungs|sites|offices|records|propositions)\[[^]]+\] *=[^=]" engine/season modules`,
  tests excluded): `probes.py` 24, `populated.py` 22, `scarce.py` 9, `governance_spine.py` 6, `headless.py`
  5, `corpus_run.py` 5. The four-line act of seating a person (a `Person`, a person `Rung`, a `contain`
  Tenure, a `reside` Tenure) is written out at `populated.py:515-518` and again at `:693-696`.
- `tools/m1_acceptance.py` and `tools/export_npc_roster.py` import `engine.season.harness` (`W2`); 29
  proposals edit `populated.py` (`unified/U3_DEPENDENCY_ORDER.md` §5.1).

**Falsifier, and its outcome.** A non-harness file that builds the realm or composes the chooser:
`grep -rn "build_realm\|def chooser" engine/season --include=*.py` outside `harness/` and `tests/` prints
only `decision/choose.py::make_chooser` (the primitive, not the composition). Attack on the other side:
does the kernel depend on the harness? No: `W2` shows no import edge from any non-harness season file into
`harness/`. The harness is a leaf above the kernel; the defect is what lives in it, not a cycle.

**Consequence.** The port has no file to port for "new game": it would transcribe an instrument. Every
world-shaped proposal (worldgen, cast, prologue, the playable scenarios) edits a 2,163-line harness file.
A builder that drifts from the others produces worlds that differ in ways no gate compares.

**Minimal fix at the owner.** Two parts. **CI-06** (hash-EQUAL, no ruling needed): one owner for the
chooser's composition and for the run loop, with `soak`, `interactions` and `storybar` routed through it,
and one owner for seating a person, used by the six builders. **Where the realm builder itself lives** is
a Layer 1 question (a tenth module, or a row of an existing one) and is listed for Jordan as `J-H-01`
with two options; **CI-07** is written for both.

### H-03 · More than half the source is prose, and the largest registries are mostly annotation — degrades (cost of every later batch; clarity; the port)

**Claim.** The code carries its own history, in comments, docstrings and `note:` fields, at a volume that
exceeds the code. CLAUDE.md puts dated narrative in commits and `_history` files (§1), and makes the
checkout the record (§2).

**Evidence** (`W1`, `W5`).
- Non-test Python under `engine/`, `modules/`, `tools/`: 39,502 code lines, 18,030 whole-line comments,
  24,376 docstring lines: **52 %** of non-blank lines are prose. By area: `loop` 65 %, `state` 65 %,
  `decision` 64 %, `queries` 60 %, `seam` 61 %, `data` 52 %, `modules/combat` 55 %, `modules/mass_battle` 51 %.
- Single files: `queries/world_q.py` 1,989 code of 5,557; `state/gate.py` 503 of 1,933;
  `data/fixtures.py` 219 code against 861 comment lines; `loop/driver.py` 170 of 621.
- Registries: `rosters.yaml` 359,435 bytes, of which `note:` 183,132, `source:` 27,617 and comments
  48,638; `verb_table.yaml` 353,681 bytes, of which the seven largest `*_note` and `source` columns are
  208,818 and comments 31,431; `requirements.yaml` 165,722 bytes, of which `measured:` is 135,348.
- The text is history by its own words: `loop/driver.py:11` *"THIS DOCSTRING WAS STALE THE MOMENT L5 LANDED
  AND SAID SO FOR A DAY"*; `harness/populated.py:8-19` describes the instrument it replaced on 2026-09-13.
- The tests lane measured the same in the tests: 60 % of `test_season_shape.py` (10,664 of 17,880 lines)
  is comment or docstring (`audits/01_CORE_audit_addendum_C_tests.md:48`).

**Falsifier, and its outcome.** *"If the prose were deleted, would the game behave differently?"*
(CLAUDE.md §0.05). Searched for readers of it: (a) `argparse` descriptions built from `__doc__` in eleven
harness files and seven tools; (b) `inspect.getsource` in nine test files and source parsing in twenty-four;
(c) the anti-fabrication gate's tags, 114 `[JUSTIFIED` lines in non-test code, which
`tools/ci_sim_fabrication_check.py` reads per line; (d) three `*_note` columns whose presence the verb
loader checks (`data/verbs.py:662-667`, `:759-762`). Nothing else. So the prose is reference except those
four classes, and a cut must keep them.

**Consequence.** Reading is the cost (CLAUDE.md §10). A lane that edits one roster opens a 359 KB file of
which about a quarter is values; 130 proposals do so. A newcomer's lookup *"what does this module do, and
where do its inputs come from?"* (`efficient-coding-review` L4) fails at `loop/driver.py`, whose first 28
lines are an account of a stale docstring and a load-bearing unused import list.

**Minimal fix.** **CI-01** (the registries: annotations cut to the definition, the three checked columns
kept), **CI-02** (source: each docstring states what the unit does, its inputs and its governing row;
dated narrative leaves; the four reader classes are preserved). Both hash-EQUAL; both early.

### H-04 · The season's tuning values have no typed export — degrades (CLAUDE.md §5; the port)

**Claim.** The rule is that a value the engine or the port uses lives in a typed artifact behind an
exporter, or in a single Python owner. The season's values have the Python owner and no artifact, so the
port can only transcribe them by hand.

**Evidence** (`W5` §2, §3). `engine/season/data/fixtures.py:213` `DEFAULT_FIXTURES = Fixtures(...)` passes
101 keyword arguments. `tools/export_sim_params.py` reads module-scope literals (`:1-20`), so
`sim_params.json`'s `engine.season` block holds 21 constants and none of the 101.
`engine/engine_params/game_constants.json`, the file the port's parity checker reads (its `_generated`
line), holds 5 constants, 2 collisions and 3 divergences. Arms that select behaviour are spread over three
places: 20 string selectors and 7 booleans in `Fixtures`, 7 boolean parameters of `build_realm`, and 91
`os.environ` reads in `modules/mass_battle` (66 in `config.py`); the last is already carried
(`proposals/11_GO_port_gate_order_and_coverage.md` §5 and gate 1).

**Falsifier, and its outcome.** `python tools/export_sim_params.py --search pool_default` would list the
constant if it were exported. Not run as a search; settled instead from the artifact: no key under
`by_module["engine.season"]` can be a fixture, because the exporter's reader takes `ast.Assign` at module
scope and the fixtures are `ast.keyword` nodes of one call (read at `tools/export_sim_params.py:1-60`).
`[UNVERIFIED: the 21 names were not listed one by one.]`

**Minimal fix.** **CI-04**: extend the existing exporter (the neighbour, `valoria-simplify` ladder rung
4) to read the keyword literals of `DEFAULT_FIXTURES` into the same artifact under their own module key;
no new tool. **CI-05**: the builder's seven arms are read into the same export, so "what ships"
has one list a port can read.

### H-05 · One host site reaches a module attribute no composition row names; one row is looked up through two tables — degrades (modularity; holonic §43)

**Claim.** A registered module is attached by a registry row, never an import (`layer-conformance` B0,
citing `architecture/holonic_ARCHITECTURE.md` §43). One site obtains a row's callable and then uses it to
import the callable's module and call a different function.

**Evidence.** `engine/season/seam/wrappers/sigma.py:239-247`:
`module = importlib.import_module(composition.require(_ROLL_ROLE).__module__)` then
`module.obstacle(inp)`. The row `social_contest.roll` names `modules.social_contest.roll:roll`
(`references/module_contracts.yaml:52-55`); `obstacle` (`modules/social_contest/roll.py:89`) is named by no
row. Executed 102 times in one season (`W3`). Second: the four adapters look their entry up in
`manifest.MODULE_ENTRIES` (`seam/wrappers/_entry.py:19-33`), and nine other sites look the same rows up
through `composition.require` (`W3`, second table), because the table fills only at driver construction
(`queries/world_q.py:1353-1358` says so).

**Falsifier, and its outcome.** A composition row whose target is `roll:obstacle`: `engine/engine_params/composition.json`
has 16 roles and none (`W3`). Steelman: the docstring at `sigma.py:243-245` calls this *"the host's own
way of naming a module"*, and the exporter resolves the row at export time, so a moved module still reds
CI. It does: for `roll`. A renamed `obstacle` passes the exporter's check and fails at the first contest.

**Consequence.** The port maps a composition row to one callable; this edge is not in the map. An
obstacle composer is exactly the function several proposals rewrite (`proposals/U5c_SC_one_obstacle_form.md`),
so the undeclared edge sits on a hot path of the plan.

**Minimal fix.** **CI-03**: a row `social_contest.obstacle` (`entry: query`), called by role. The second
observation needs no edit, and the attack on it failed: both routes return the one object
`composition.require` caches (`engine/substrate/composition.py:60-69`; `manifest/registrar.py:115` stores
that same result), so they cannot disagree, and routing the nine sites through the table would add an
import edge from `queries/` to `manifest/` that `04` §A.2 does not give. `MODULE_ENTRIES` itself is earned
by ruling (A-25, ED-IN-0284, quoted in `manifest/registrar.py:15-22`) and stays.

### H-06 · The contest seam returns an untyped mapping for two engines — degrades (carried)

`04` §C.5 says the subsystem returns a `Margin`. `queries/inputs.py:17-24` records that the social roll
returns one and that *"the SEAM keeps one return shape"*, a `dict`, because combat returns a scene and
mass battle a field. `audits/25_GROUNDING_ENGINE.md` V-01 and V-02 opened both. Carried by
`proposals/03_PC_typed_outcome_one_door.md` (B14) and `proposals/04_MB_typed_outcome_and_one_path.md`
(B17), as narrowed by A-3 (the field returns an end state). Nothing added here; listed because it is the
widest untyped seam in §2.1.

### H-07 · Sixteen files carry the plan, and the first five are the largest files in the tree — degrades (delivery)

**Claim.** The plan's parallel waves rest on hand merges of the same few files.

**Evidence.** `unified/U3_DEPENDENCY_ORDER.md` §5.1: `rosters.yaml` 130 proposals over 32 batches,
`fixtures.py` 91 over 26, `world_q.py` 81 over 23, `verb_table.yaml` 66 over 26, `person_q.py` 53 over 19.
§1.1 of the same file: *"Two open batches may edit one of them only in different top-level keys or
functions; the merge keeps both edits by hand in handle order and never regenerates the file."* §2.2: in
waves W9 to W13 every concurrent batch is in `rosters.yaml`'s batch list (W9: B11, B15, B21; W10: B12,
B16, B19, B24). Sizes: 4,548 lines, 1,170, 5,557, and (`W5`) 354 KB.

**Falsifier.** A wave from W9 on in which some batch does not edit `rosters.yaml`: by §5.1's list W9, W10
and W13 have none; W11 has three (B20, B29, B34) and W12 one (B41).

**Judgment.** Attacked as a case for splitting the files; the split does not earn itself yet (§6, attack 5).
What does: most of each hub's bulk is prose, so H-03's fix cuts the reading and the merge surface of
`rosters.yaml`, `verb_table.yaml` and `fixtures.py` by more than half without moving a key.
**CI-01** and **CI-02** therefore land before B04, and §5 of the proposal asks v12's file census to
carry one ordering rule for additions to the two registries (a new key or row goes at the end of its
family's block), so two batches' additions do not meet in one hunk. That rule binds a reader and gets no
mechanism.

### H-08 · Personal combat is a flat set of top-level modules behind a path insert — hygiene (modularity; the port)

**Evidence.** `modules/combat/` has no `__init__.py`; its fifteen files import each other by bare name
(`wrapper.py:8` `import core, combat_systems as S, tradition as TR, contact as CT`; `combatant.py:9`
`from config import CFG`). Five files insert a path: `engine/substrate/pc_engine.py:47-49` and
`modules/combat/{wrapper.py:7, contact.py:13, core.py:14-17, combat_systems.py:4}`. By that
import form a process that has fought once holds `core`, `config`, `geometry`, `weapons`, `vocabulary` and
`attributes` as top-level module names (read from the imports; not executed). `tests/valoria/test_engine_does_not_import_systems.py:250` holds `PATH_SEAM_ALLOWED =
{'substrate/pc_engine.py'}`, shrink-only, with the reason at `:248-249`: the balance workbench loads the
set flat. Loaders of the flat set: 15 files under `systems/combat/`, 23 under `tests/valoria`, 4 under
`engine/season/tests`, `tools/export_engine_params.py:127-132`.

**Falsifier.** `python -c "import modules.combat.wrapper"` succeeding without a path insert; not run
(it would import `core` by bare name and fail or pick up another `core`). `[UNVERIFIED: not executed.]`

**Minimal fix.** **CI-09**: make it a package; delete the path seam and its allow-list entry. Lowers the
port's cost for this engine (§8): one construct fewer with no GDScript counterpart to read.

### H-09 · The kernel's import surface is held open by a frozen instrument — hygiene (minimality; clarity)

**Evidence.** `loop/driver.py` imports 112 names and references 33 (an `ast` count of imported names never
used as a `Name` in the module; `__future__` excluded). Its docstring (`:18-28`) says the list is *"WIDER
THAN THIS MODULE USES ... load-bearing"* so that `engine/reference/degree-sweep/sweep_core.py` keeps
resolving `S.<name>`: that file builds `S` by `dir()` over sixteen modules ending with the driver
(`sweep_core.py:58-66`). The same count reads 13 of 14 for `loop/effects.py` and
11 of 11 for `modules/combat/tradition.py`; both are registration and re-export files (`effects.py:85-102`
imports the `effects_*` modules so their `@effect_for` bodies register), so their imports are what they are
for and are no part of this finding. `engine/reference/` (33 functions) is entered by no run (`W4`); its arms are imported
by two tests (`engine/season/tests/test_season_shape.py:14247`) and by the R-02 instrument under
`proposals/2026-09-04-degree-sweep/` (`dossiers/00_NINE.md`, R-02 `measure:`).

**Falsifier, and its outcome.** A name among the 79 that something obtains through the driver. Measured two
ways (§9, probe 13). (a) The sweep tree and the season tests read 26 distinct `S.<name>`; the only two that
resolve through the driver's namespace alone are `SeasonDriver` and `resolvable_verbs`, which the driver
defines; the 14 of the 79 that some file reads as `S.<name>` all resolve from their owner module among the
other fifteen. (b) Across `engine/`, `modules/`, `tests/`, `tools/` and `proposals/2026-09-04-degree-sweep/`,
no file imports one of the 79 `from ...loop.driver` or reads it as `driver.<name>` or `DRV.<name>`
(`ast` over imports and attribute reads on an alias of the module). So the docstring's claim that the wide
list is load-bearing is **not borne out**: by these two searches all 79 are unused. Blind spot: a dynamic
`getattr(driver, name)` or a star import would be missed; the item's gate runs the two tests that import
the sweep arms.

**Minimal fix.** **CI-08**: the driver's unused imports go (the aggregate needs no change); the docstring
states what the driver does.

### H-10 · Duplicated facts and dead code: mostly already carried — hygiene

Cited, not redone. Each has a carrier in the unified order:

| the duplicate or the dead thing | evidence | carrier (batch) |
|---|---|---|
| two degree ladders that disagree at 6 or 18 of 10,000 cells | `audits/25` V-16 | `proposals/U5a_DICE_owed_edits.md`, `10_DICE_exported_face_rule_and_band_edges.md` (B05) |
| three samplers (the bell curve, the social whole-dice roll, the battle's sampler) | A-5; `audits/10_DICE_audit.md` | `10_DICE_one_roller_one_fraction_rule.md` (B05) |
| 14 `random.Random(` constructions in 7 non-test files | this audit's grep (§9) | `11_GO_one_draw_owner.md` (B06) |
| 91 `os.environ` reads in `modules/mass_battle` | this audit's grep; the proposal's §5 | `11_GO_port_gate_order_and_coverage.md` (B41) |
| the social-contest kernel under `systems/social_contest` (75 census rows) | `audits/17_CENSUS_C1B.md` §0 | `05_SC_sc05_kernel_retirement.md` (B24) |
| unreferenced symbols, dead fields, phantom contract rows | `census/C1` to `C6`; `audits/17_CENSUS_*` | `17_CENSUS_C1A_01`, `C1B_01`, `REST_1` (B03) |
| `requirements.yaml` `measured:` as a 135 KB narrative | `W5` §1 | `01_CORE_requirements_reading_record.md` (B02) |

**New here** (no proposal names them; `grep -rl` over `proposals/` and `audits/` of the suite, §9):
`tools/join_audit_workings.py` (253 lines) and `tools/verify_handoff_split.py` (662 lines) have no caller
and their tests were dropped as process tests on 2026-11-04 (`references/restructure_ledger.md:3100`,
`:3118`, ED-IN-0312); `engine/engine_params/value_pointer_links.json` (23 KB) is read by nothing but its
generator `tools/link_values_pointers.py` and that tool's test (`W5` §2, `W6`). **CI-10** deletes them.

### H-11 · The authored data has three roots — hygiene

`engine/season/data/files.py` reads the season registries from `engine/season/` (`:98-130`), the cast from
`references/npc_registry.yaml` (`:158`) and the realm's geography from
`systems/settlements/valoria_geography_v30.yaml` (`:147`). The last is canon the engine reads from the
tree CLAUDE.md §3 describes as holding design. One owner of each path exists (`data/files.py`), so this is
a placement note and not a second owner; it becomes a port question (which directory a `Resource` loader
walks). No item: the unified owner ledger (`unified/U1_OWNERS_AND_VOCABULARY.md` §4.6) is where a move
would be decided, and nothing in this audit shows the present place costing a behaviour.

### H-12 · A ruled requirement's instrument lives in the unratified-proposal tree — hygiene (placement)

R-02's `measure:` is `python proposals/2026-09-04-degree-sweep/wd_collect.py` after 36 chunk cells
(`dossiers/00_NINE.md`). Lens A, A1: the reader of that script is the requirements register, so it is
mechanism for the acceptance surface, in a directory whose contents are *"surfaced BY LOCATION"* as
unratified (CLAUDE.md §3). The CORE audit already reads the row as resting on one committed log
(`audits/01_CORE_audit.md:174-175`), and `proposals/16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md`
(B02) replaces the `measure:` of R-01 and R-02. Carried; when that lands, **CI-08** can retire the sweep's
aggregate with it.

### H-13 · `tools/` is half apparatus about the repository — hygiene (no item beyond CI-10)

`W6`: of 54 tools, 8 write an artifact the engine or the port opens (the exporters); `m1_acceptance.py` and
`export_npc_roster.py` import and run the season package (`W2`); the rest, by their rows in
`references/ci_checks_registry.yaml`, check documents, ledgers, names and links (not opened one by one). By CLAUDE.md §0.1 pt 5 the second kind earns nothing from
this audit: no standard is pointed at it, no guard is proposed for it, and the two files with no caller
are deleted (H-10).

## 5. The six directions

Per `valoria-simplify` SURVEY. A direction ends in SURVEYED, PARTLY or NOT SURVEYED.

| direction | what was run | reading | verdict |
|---|---|---|---|
| **top-down** (is each stated goal realised) | M6: `register --requirements`; `m1_acceptance --summary`; the 16 composition rows against three runs | nine rows each name a measure; three read `met`, one `not_met`; six rows of sixteen unentered (H-01); R-02's instrument sits in `proposals/` (H-12) | **PARTLY**: the `measure:` commands were not re-run (limits, §1); goals nobody wrote down are INCONCLUSIVE |
| **bottom-up** (what justifies each artifact) | M1, M4 over every non-test function; M2 over 119 rosters by name | kernel reach 84 to 97 % of function lines; 2 of 119 roster keys named by no non-test file, one of them confirmed unread by another lane (`knowledge_kinds`, `audits/25` V-17); `sim_params.json` and `value_pointer_links.json` have no runtime reader | **SURVEYED** for code reach on two seeds; **PARTLY** for data (name matching; its blind spot sampled on one key only) |
| **vertical** (do levels keep their order) | M1 by area | 0 import edges from `engine/` to `modules/`; modules import one host file, the leaf `queries/inputs.py`; `seam/` imports `loop/sides.py` twice and `loop/` imports `seam/` four times (a declared pair); four area pairs import each other, all through the three top-level files `epistemic.py`, `gaps.py`, `trace_log.py` | **SURVEYED** for declared edges; string seams read apart in `W3` |
| **lateral** (do peers share what no contract names) | M2; the role constants | the composition role names (`ARMY`, `PROVISION`, `HOUSING`…) are constants of `queries/world_q.py:1335-1350` imported by `seam/`, `loop/` and `harness/`: a reader module owns the seam's vocabulary; `Fixtures` is read at 218 sites over 99 names; `sigma.py` reaches `roll.obstacle` (H-05) | **PARTLY** |
| **over time** (order, replay, carried cost) | I1 as replay: same seed, same hash, three readings (§9) | replay holds; build plus the first season costs about 8 s, the fourth season 65 s at seed 2 (`W4` marks: 7.4, 23.4, 55.5, 120.0 s cumulative), so cost per season grows with the log | **PARTLY**: one machine, two seeds; history NOT SURVEYED (shallow clone) |
| **diagonal** (coupling no structure declares) | I3, I4 without I5 | the driver's imports and a frozen sweep (H-09); behaviour arms in three places (H-04); the realm in the harness (H-02) | **PARTLY**: without history only the structural instruments ran |

## 6. Attacks that failed (steelmen that held)

1. **"A module imports the host, so it cannot stand alone."** Measured: `import modules.social_contest.roll`
   loads three `engine.season` modules (`engine.season`, `.queries`, `.queries.inputs`), no YAML, in 0.03 s;
   the same for `modules.settlements.housing`, `modules.fieldwork.find`, `modules.combat.fight`.
   `queries/inputs.py:11-15` states the leaf rule and names the test that observes it. Holds. (It does
   differ from `holonic` §45, which puts the records inside the module; the file says so at `:7-10`.)
2. **"The engine imports a module somewhere."** `W2`: no edge. Holds.
3. **"`MODULE_ENTRIES` is a second table and unearned."** Earned by ruling (E1): A-25 and ED-IN-0284, as
   `manifest/registrar.py:15-22` quotes them. The second route is the nine direct sites (H-05), not the table.
4. **"The harness leaks into the kernel."** `W2`: no non-harness season file imports it. Holds.
5. **"`world_q.py`, `rosters.yaml` and `verb_table.yaml` should be split into families."** Attacked as hubs
   (H-07). A split is relocation (`valoria-simplify` DISPOSE: the number of places a reader opens does not
   fall); `04` §A.2 names `world_q` as a member of `queries/`; 81 proposals cite `world_q.py` by function and
   130 cite `rosters.yaml` by key, and every one would need re-pointing mid-plan. The reading cost that made
   the split attractive is mostly prose, which CI-01 and CI-02 remove without moving anything. Not proposed.
   If, after those land, a lane still cannot hold one of these files, that is the time to ask again.
6. **"`sim_params.json` is dead because nothing at runtime reads it."** It feeds `game_constants.json`,
   which the port's parity checker reads. Earned (E4: the one place the cross-repository constants are
   derived). Holds; CI-04 extends it.
