# Codebase improvement proposal — organization, centralization, efficiency, modularity

## Status: PROPOSED (stage 3 of `STAGES.md`; a plan of ordered edits for workplan v12; nothing here is applied; not canon)

## Read at: `4dc8a7b` (working tree, 2026-11-12; the code tree is unchanged through `ff2f508`). Producer: Fable, the holistic lane. Findings: `master/HOLISTIC_AUDIT.md` and its parts 2 and 3 (`H-01` to `H-13`). For Jordan: `master/HOLISTIC_FOR_JORDAN.md`.

**Words** (`unified/U1_GLOSSARY.md` §H): a *setting* is a `Fixtures` field; the *act-count instrument* is
`harness/aperture.py`; a *dataclass* is a typed input or outcome class of `queries/inputs.py`; a *hot file*
is one of the files `U3` §1.1 lists. Code identifiers stay as the tree has them.

Parts: this file (§0 what changes at runtime, §1 the standard and the cut test, §2 the batches and where
they slot, §3 the tables v12 takes, items `CI-01` to `CI-05`), `_part2` (items `CI-06` to `CI-11`, §4 the
deletion list, §5 notes for v12's author, §6 what this proposal does not carry).

## 0. What it changes in `engine/season/` at runtime

**Nothing a seeded world can show.** Every item is hash-EQUAL for `World.content_hash()` on every pinned
world, and says how that is observed. Three items regenerate a tracked artifact through its own exporter
(`composition.json`, `sim_params.json`); one adds lines to an instrument's printout (the act-count
instrument, `harness/aperture.py`); one
deletes three files nothing reads. No draw, outcome, band, odds or order of resolution changes, so nothing
here bears on the standing rule (*we do not do deterministic*): the rule concerns outcomes, and these items
touch none.

These are **apparatus** items in `valoria-simplify`'s sense (*"if removing the artifact changes only how
the code arranges what the game does, it is APPARATUS"*), so the cut test is that skill's and no NERS
reading is given: a moved content hash on a control shown to see the edit would make an item a mechanic,
and the instruction in that case is to revert it, not to re-pin.

## 1. The standard, and the cut test each item carries

Jordan's standard (`skills/efficient-coding-review/SKILL.md`, JORDAN'S DEFINITION): *"as little code as
possible in an extremely clear organized manner that is centralized and modularity"*; *"the exact same
behavior and outcomes with less code … without hard-coding values"*.

Each item states, in this order:

1. **What dies and what is preserved** (the cut test): the lines, files or edges removed, and the
   behaviour that must read the same after.
2. **Earning** (`valoria-simplify` EARN): why what is kept is kept, with its citation.
3. **Exact edits**, ordered, at the single owner: files and symbols, the schema of any data row, the call
   sites.
4. **Tests**, named: added, changed, or the covering file to run (CLAUDE.md §0.4 cl. 2).
5. **Gate**: an execution artifact and its expected reading.
6. **Falsifier and control**: the plant that must be seen *before* the real edit is trusted
   (`valoria-simplify` C2: reach, plant, observe, then edit; in a scratch worktree, bytecode off). This lane
   ran no plant; each is a step of the item.
7. **Declared hash movers; dependencies; what lands it; cost class and tier** (CLAUDE.md §10).

**Baselines.** Where a gate says "the opening reading", it is the reading the batch takes once, at its
first commit, on the tree it starts from (`reading @<sha>`): B01 re-records every realm pin, so today's
hashes are examples, not targets. At `4dc8a7b` they are: `headless --case NPC-088 --seasons 2 --seed 0` →
`5405522c36b0399247f83fd9f6d29494`; `build_realm(0)`, one season, the shipped chooser →
`5ab73af282d0779646c38839fbab85d8`; seed 2, four seasons → `b4bae063f33476988db678b5aae62a28`
(`master/HOLISTIC_AUDIT_part3.md` §9). **Use seed 2 as well as seed 0 for any item that touches personal
combat or the field**: at seed 0 no function of `modules/combat` is entered in three seasons (H-01), so a
seed-0 hash cannot see an edit there.

**What is not proposed, by rule.** No guard whose subject is another guard or a process artifact (CLAUDE.md
§0.1 pt 5); no new tool, scorer, register or standing check; no edit to `architecture/`; no `raise`-to-result
sweep and no shaping of Python toward a Godot idiom (`valoria-simplify` port rules (c), (d)); nothing that
overwrites a `(RULED)` item (the one Layer 1 question is in `HOLISTIC_FOR_JORDAN.md`).

## 2. The batches, and where they slot into `unified/U3_DEPENDENCY_ORDER.md`

| item | what | finding | joins | why there |
|---|---|---|---|---|
| **CI-11** | an `ENGINES` reading on the act-count instrument (`harness/aperture.py`) | H-01 | **B02-tests** (IN, W2, hash EQUAL), after `16_PESSIMIST_GAME_consequence_reading` | B02 holds the instrument readings later gates name; it edits no file another B02 member edits (`harness/aperture.py`, `engine/season/tests/test_aperture.py`) |
| **CI-10** | three deletions with their `FORK:` rows | H-10 | **B03-hygiene** (IN, W3, hash EQUAL), first, with `17_CENSUS_C1A_01` D1 | deletions of what nothing reads go first (STAGES practice 4) |
| **CI-08** | the driver's 79 never-referenced imports | H-09 | **B03**, after the census deletions | same batch owns dead-name removal; `loop/driver.py` is edited by no other B03 member |
| **CI-03** | the `social_contest.obstacle` composition row | H-05 | **B03**, after `17_CENSUS_REST_1` D4 (it edits `references/module_contracts.yaml` first) | one regeneration of `composition.json` for the batch; B03's gate already runs `export_composition.py --check` |
| **CI-04**, **CI-05** | the season's settings (`Fixtures`) and the realm's arms in the typed export | H-04 | **B03**, after `17_CENSUS_C1B_01` D3 (it rebuilds `sim_params.json` first) | one rebuild of the artifact for the batch |
| **CI-06** | one owner of the chooser's composition | H-02 | **B03**, after `U5a_CORE_owed_edits` (it edits `harness/probes.py`) | lands before B06, which changes what `draw_factory` returns: B06 then edits one composition, not four |
| **CI-01**, **CI-02** | annotations out of the two registries; history out of the source | H-03, H-07 | **new batch `B03a-prose`** (IN, hash EQUAL), after B03, before B04 | below |
| **CI-09** | personal combat as a package | H-08 | **new batch `B13-pc-package`** (PC, hash EQUAL; the handle U3 left unused), after B03a, before B05 and B14 | below |
| **CI-07** | the realm builder's home; one way to place a person | H-02 | **held** on `J-H-01`; when ruled, **new batch `B03c-boot`** (IN, hash EQUAL) at the next IN-lane boundary | a pure move; lands at any boundary once its home is ruled |

**`B03a-prose`** (IN; after B00, B01, B02, B03; before B04, B05, B08). Members: CI-01, CI-02. One close.
*Why its own batch and not part of B03:* its diff touches almost every non-test file of the season package's game code and the
modules and is comment-only by construction; its gate (an AST-equality reading over every edited file,
CI-02) would be broken by any code edit in the same batch, and B03 is all code edits. Merged, the batch
would save one close and lose the only gate that makes a 30,000-line diff reviewable. *Why before B04:*
B04 is the first batch whose members edit `rosters.yaml`, `fixtures.py`, `verb_table.yaml`, `person_q.py`
and `options.py` in number (`U3` §5.1); every later batch then reads the shorter files. *What it costs
later batches:* every `path:line` citation in the suite into an edited file goes stale at this batch (as
it does at the first batch that edits the file in any case); proposals name symbols and keys beside their
lines, and `layer-conformance` B0 already says a stale line is re-located by its symbol.

**`B13-pc-package`** (PC; after B00, B01, B02, B03, B03a; before B05 and B14). Member: CI-09. One close.
*Why after B03a:* both edit every file of `modules/combat` (CI-02 the comments, CI-09 the import lines);
serial, prose first, so CI-02's AST gate is not disturbed. *Why before B05:* B05 carries PC edits
(`U5b_PC_rulings_in_the_fight` §2–§3) inside `modules/combat`; an import-form change under an open mover
batch would have to be merged by hand. *Parallel:* B13 is in the PC lane and may run beside B04 (IN) if
B04's members edit no file under `modules/combat`, `systems/combat`, `engine/substrate/pc_engine.py` or the
27 test files CI-09 names; `[UNVERIFIED: U3 §5.1 lists files edited by two or more proposals only; v12's
author checks B04's single-proposal files.]`

**Edges added to U3's graph** (all point forward): B03 → B03a → B04; B03a → B13 → B05; B13 → B14;
CI-06 (B03) → B06; CI-11 (B02) → every later batch's close (a reading it may quote). No edge points back.
The critical path gains one batch (B03a); B13 runs beside the IN spine.

**Requirement map** (STAGES step 6, rule 1). None of these batches moves a requirement row: they are
ground for the batches that do, and STAGES rule 5 asks that such a batch be named with its reason. B03a's
reason is reading cost on every later batch (H-03, H-07); B13's is the port's first slice and the PC lane's
own batches (H-08); the B03 items serve R-05's delivery indirectly (H-01's reading is CI-11, in B02).

## 3. The tables v12 takes

### 3.1 Declared hash movers

| item | moves a world's content hash? | regenerates a tracked artifact (through its exporter, never by hand) | re-pin? |
|---|---|---|---|
| CI-01 | no | none (the two registries are the edit) | no |
| CI-02 | no | none | no |
| CI-03 | no | `engine/engine_params/composition.json` (`tools/export_composition.py`): 16 → 17 roles | no |
| CI-04 | no | `engine/engine_params/sim_params.json` (`tools/export_sim_params.py --build`): gains the setting rows | no |
| CI-05 | no | the same file, same rebuild: gains the realm-arm rows | no |
| CI-06 | no | none | no |
| CI-07 | no | none | no |
| CI-08 | no | none | no |
| CI-09 | no | `engine/engine_params/combat_engine_v1.json` must come out **byte-identical** (`tools/export_engine_params.py --check`) | no |
| CI-10 | no | deletes `engine/engine_params/value_pointer_links.json` | no |
| CI-11 | no | none | no |

**No item is a declared mover.** A moved hash at any gate below is a defect in the edit: revert the item.

### 3.2 File census (which items edit which file; serial order is item order within a batch)

| file | items | batch |
|---|---|---|
| `engine/season/rosters.yaml`, `engine/season/verb_table.yaml` | CI-01 | B03a |
| every non-test `*.py` under `engine/season/{loop,state,decision,queries,data,seam,manifest}`, `engine/season/epistemic.py`, `engine/substrate/`, `engine/dice_engine/`, `modules/` | CI-02 | B03a |
| `references/module_contracts.yaml`, `engine/engine_params/composition.json` | CI-03 | B03 |
| `engine/season/seam/wrappers/sigma.py` | CI-03 (B03), CI-02 (B03a) | B03 → B03a |
| `engine/season/loop/driver.py` | CI-03 (one line), CI-08 (B03), CI-02 (B03a) | B03 → B03a |
| `tools/export_sim_params.py`, `engine/engine_params/sim_params.json`, `tests/valoria/test_export_sim_params.py` | CI-04, CI-05 | B03 |
| `engine/season/harness/probes.py`, `soak.py`, `storybar.py`, `interactions.py` | CI-06 | B03 |
| `engine/season/harness/populated.py` and its importers | CI-07 | B03c (held) |
| `modules/combat/*.py`, `engine/substrate/pc_engine.py`, `systems/combat/combat_engine_v1/workbench/*.py`, `tools/export_engine_params.py`, the 27 test files of CI-09 step 6 | CI-09 | B13 |
| `tools/join_audit_workings.py`, `tools/verify_handoff_split.py`, `tools/link_values_pointers.py`, `tests/valoria/test_link_values_pointers.py`, `engine/engine_params/value_pointer_links.json`, `references/restructure_ledger.md` | CI-10 | B03 |
| `engine/season/harness/aperture.py`, `engine/season/tests/test_aperture.py` | CI-11 | B02 |

### 3.3 Order of work (cheap hash-EQUAL first)

1. **B02:** CI-11 (the reading every later close can quote).
2. **B03:** CI-10 (delete) → CI-08 (unused imports) → CI-03 (the row) → CI-04 → CI-05 (the export) → CI-06
   (the chooser's one composition). Each is one commit, `[skip ci]` until the batch's last (STAGES
   practice 3b).
3. **B03a:** CI-01 (two files, two lanes at once) → CI-02 (one lane per package, at once, disjoint files).
4. **B13:** CI-09, beside B04.
5. **B03c:** CI-07, when `J-H-01` is answered.

---

## CI-01 · The two largest registries carry values and definitions, not their history

**Finding.** H-03, H-07. `engine/season/rosters.yaml` is 359,435 bytes of which `note:` strings are
183,132 and whole-line comments 48,638; `engine/season/verb_table.yaml` is 353,681 bytes of which seven
annotation columns are 208,818 and comments 31,431 (`master/work/W5_DATA_CHANNELS.md` §1). 130 and 66
proposals edit them.

**What dies.** Dated narrative inside `note:` and `*_note:` strings and inside comment blocks: who found
what, what a cell used to say, measurement logs, the story of a correction. **What is preserved, byte for
byte:** every key, value, row and column a loader reads; every `source:`; every `[ASSUMPTION; …]` tag and
`revert:` clause; one or two sentences per annotation saying what the roster or cell *is* (the call-site
definition CLAUDE.md §4 asks for).

**Earning of what stays.** `source:` is read (`engine/season/data/rosters.py:1481`; `data/verbs.py:441`
lists it among the row keys). `requires_typed_note`, `effect_decline_note` and `requires_decline_note` are
checked for presence (`data/verbs.py:662-667`, `:759-762`; `manifest/registry.py:650-698`), and
`formation_decline_note` is read by `tests/valoria/test_module_registrar.py:403`: E2. The other annotations
are skipped by rule (`data/rosters.py:1402`, `:1462`; `data/verbs.py:616-627`): reference.

**Exact edits** (one lane per file; the two files are disjoint).

1. Open the two tests that read annotation text and note what they assert:
   `engine/season/tests/test_season_shape.py:7572-7576` (reads `writes_note`) and
   `engine/season/tests/test_governance_build.py:799` (reads the verb table's raw text). Whatever string
   they match is kept verbatim.
2. For each `note:` / `*_note:` value and each comment block, apply the rule above. An annotation that is
   only history is cut to its one-line definition; it is never deleted if it is one of the four
   presence-checked columns on a row that carries it.
3. Leave `source:`, `cite:`, `ground:`, `row:` and every other key untouched. Leave the other season YAML
   files alone: their prose is small (`W5` §1) and they are not hot files.
4. The commit body names the parent SHA as where the annotations as they stood can be read. No `FORK:` row:
   no file is deleted.
5. `unified/U1_GLOSSARY.md`: no row changes (no term is introduced, renamed or retired).

**Tests.** None added. Covering files, run once each after the edit:
`python -m pytest engine/season/tests/test_season_shape.py engine/season/tests/test_governance_build.py tests/valoria/test_module_registrar.py -q -n auto`.

**Gate.**

1. *Parsed-object equality.* A scratch probe (not committed): `yaml.safe_load` each file at the batch's
   base and at the edit; delete every mapping key equal to `note` or ending in `_note`, and compare.
   Expected: equal for both files. Then compare the **set of rows that carry** each of
   `requires_typed_note`, `effect_decline_note`, `requires_decline_note`, `formation_decline_note`:
   expected equal.
2. `python -c "import engine.season.data"` exits 0 (the loaders' own refusals run at import).
3. The headless hash and the realm hashes at seeds 0 and 2 equal the batch's opening reading.
4. A reading for the close, not a threshold: `wc -c` of the two files before and after.

**Falsifier and control.** In a scratch worktree: (a) blank one `requires_typed_note` on a row whose
`requires_typed` is null → the import must fail (`data/verbs.py:759-762`); (b) change one roster value →
gate 1 must report the file unequal. Both seen, then reverted, before the real edit is read as green.

**Declared hash movers.** None. **Depends on:** B03 (the census edits to these files land first).
**Lands in:** B03a. **Lands it:** two `valoria-author` lanes, `sonnet`, effort `high`, one per file (N−1
would leave one 350 KB file to a lane already holding the other). **Cost class:** edit, large by volume;
[estimate] one to two hours of agent time per file.

---

## CI-02 · The source says what it does; its history lives in the commits

**Finding.** H-03. 52 % of the non-blank lines of non-test Python are comment or docstring; 60 to 65 % in
`loop/`, `state/`, `decision/`, `queries/`, `seam/` (`W1`).

**Scope.** Non-test `*.py` under `engine/season/{loop,state,decision,queries,data,seam,manifest}`,
`engine/season/epistemic.py`, `gaps.py`, `trace_log.py`, `engine/substrate/`, `engine/dice_engine/`,
`modules/`. **Not** `engine/season/harness/` (eleven of its files build their `--help` from `__doc__`,
and it is an instrument package), not tests (the tests lane's proposals own them), not `tools/`.

**What dies.** In docstrings and comments: accounts of what the code used to do, who caught which defect,
measurement logs, revision histories (`REV 4, TWICE`), the names of deleted files, a second telling of a
rule that a cited row already states.

**What is preserved.**

1. A module docstring's statement of what the module does, what it owns, where its inputs come from and
   the Layer 1 row or ED id that governs it.
2. A function docstring's contract: inputs, return, what it raises and why.
3. A comment that explains a line a reader would otherwise misread.
4. Every `# [JUSTIFIED: …]`, `# [DECLARED-DIVERGENCE: …]`, `[ASSUMPTION; …]` tag and `# noqa`, byte-identical
   and on the same code line or the line directly above it (`tools/ci_sim_fabrication_check.py` reads a tag
   per line; `layer-conformance` THE CONTROL).
5. Jordan's words where a comment quotes them, with their date.
6. Every string that is code: the `law=` and `needs=` arguments of a refusal are arguments of a call and
   are not touched.

**Earning.** By the deletion test of CLAUDE.md §0.05 the prose is reference, except four classes of
reader found by search (`master/HOLISTIC_AUDIT_part2.md` H-03, falsifier): `argparse` descriptions (out of
scope here), tests that read source (nine files use `inspect.getsource`, twenty-four parse source), the
fabrication gate's tags, and the checked `*_note` columns (CI-01's subject). Rules 1 to 6 keep each.

**Exact edits.** One lane per package (`loop`, `state`, `decision` + `epistemic.py`, `queries`, `data` +
`manifest` + `engine/substrate` + `engine/dice_engine`, `seam`, `modules/combat`, `modules/mass_battle` +
the small modules): eight lanes, disjoint files, `isolation: worktree`.

1. Before editing a file, list the tests that read it as text:
   `grep -rlE "getsource|ast\.parse|read_text\(\)" engine/season/tests tests/valoria` and, in those, the
   names of this file's functions. A docstring or comment a test matches on is kept verbatim.
2. Edit comments and docstrings only, by the rules above. Do not reorder, rename, re-indent or reflow
   code; do not delete a docstring outright where the function has one (its first sentence stays), so no
   `__doc__` becomes `None`.
3. Order within a lane: largest prose first (`W1`'s last table: `queries/world_q.py`,
   `modules/mass_battle/hierarchy/units.py`, `state/gate.py`, `modules/mass_battle/orchestration.py`,
   `decision/options.py`, `data/verbs.py`, `state/world.py`, `data/fixtures.py`).
4. `loop/driver.py`'s docstring after CI-08: what the driver is, the seven steps bound at the foot of the
   file, the tokens it mints; nothing about the docstring's own past.

**Tests.** None added. The suites run once at the batch close (CLAUDE.md §0.4); mid-batch, each lane runs
the test files step 1 listed for its package.

**Gate.**

1. *AST equality modulo docstrings*, per edited file (a scratch probe, not committed):

   ```python
   import ast, subprocess, sys
   def strip(tree):
       for n in ast.walk(tree):
           b = getattr(n, "body", None)
           if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and b \
              and isinstance(b[0], ast.Expr) and isinstance(b[0].value, ast.Constant) \
              and isinstance(b[0].value.value, str):
               n.body = b[1:] or [ast.Pass()]
       return ast.dump(tree)
   bad = [f for f in sys.argv[2:]
          if strip(ast.parse(subprocess.check_output(["git", "show", f"{sys.argv[1]}:{f}"], text=True)))
          != strip(ast.parse(open(f).read()))]
   print("AST-EQUAL" if not bad else bad); assert len(sys.argv) > 2
   ```

   run as `python probe.py <base-sha> $(git diff --name-only <base-sha> -- '*.py')`. Expected: `AST-EQUAL`.
   Comments are not in the tree and docstrings are stripped, so equality means no code token moved.
2. `GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python tools/ci_sim_fabrication_check.py` green.
3. The headless hash and the realm hashes at seeds 0 and 2 equal the opening reading.
4. `python tools/export_engine_params.py --check`, `python tools/export_sim_params.py --check`,
   `python tools/export_composition.py --check` all current (the exporters read these files).
5. At the close, the suites once.
6. A reading for the close: `W1`'s table re-run (the probe is `census.py` in this lane's scratchpad; it is
   thirty lines of `ast` and `tokenize` and may be rewritten from the method line of `W1`).

**Falsifier and control.** In a scratch worktree: (a) change one comparison operator in an edited file →
gate 1 must name the file; (b) move one `[JUSTIFIED: …]` tag off its line → gate 2 must go red. Both seen
and reverted before the gate's green is read.

**Declared hash movers.** None. **Depends on:** B03 (CI-08 trims `driver.py`'s imports first; the census
deletions remove files this item would otherwise edit). **Lands in:** B03a, after CI-01. **Lands it:** eight
`valoria-author` lanes, `sonnet`, effort `high`; no critic fan (the AST probe is the control, and a
comment-only diff has no behaviour to attack). **Cost class:** edit, the largest in this proposal by
volume (about 31,000 prose lines in scope, `W1`); [estimate] the batch is a day of agent time, most of it
in parallel.

---

## CI-03 · The obstacle composer is reached by its own composition row

**Finding.** H-05. `engine/season/seam/wrappers/sigma.py:246` imports the social-contest module by
reflection from another row's callable and calls `obstacle`; no row names it.

**What dies.** The reflective reach: `import importlib` (`sigma.py:80`), `_ROLL_ROLE` (`:239`) and the
`importlib.import_module(...)` line (`:246`). **Preserved:** the obstacle every contest and every believed
odds reads, call for call (102 calls in the first season at seed 0, `W3`).

**Earning.** The row is E1: a registered module is attached by a registry row, never an import
(`architecture/holonic_ARCHITECTURE.md` §43, as `layer-conformance` B0 cites it).

**Exact edits, in order.**

1. `references/module_contracts.yaml`, under `composition_roles:`, directly after the `social_contest.roll`
   row (`:52-56`):

   ```yaml
     social_contest.obstacle:
       target: "modules.social_contest.roll:obstacle"
       entry: query
       needed_by: "engine/season/seam/wrappers/sigma.py — `_composed_obstacle` (the obstacle a contest is rolled against and the one believed odds read), called by role."
   ```

   No `verb:` (a `query` entry names none; `tools/export_composition.py:82` `_ENTRIES`).
2. `python tools/export_composition.py` (rewrites `engine/engine_params/composition.json`; never by hand).
3. `engine/season/seam/wrappers/sigma.py`: replace `:239` with
   `OBSTACLE_ROLE = "social_contest.obstacle"` and
   `QUERY_ENTRIES = ((OBSTACLE_ROLE, "query"),)`; replace the body of `_composed_obstacle` (`:242-247`)
   with `return composition.require(OBSTACLE_ROLE)(inp)` and a one-line docstring; delete `import
   importlib` (`:80`; it has no other use in the file).
4. `engine/season/loop/driver.py:294`: `require_entries(world_q.QUERY_ENTRIES + MATTER_STEP_CALLS)` gains
   `+ sigma.QUERY_ENTRIES`, importing the name from `..seam.wrappers.sigma` beside the existing `..seam`
   import (`loop/` already imports that file: `loop/deliberate.py`), so a missing row is refused at driver
   construction as the other host needs are (`manifest/registrar.py::require_entries`).

**Tests.** Add to `engine/season/tests/test_social_contest_module.py`:
`test_the_obstacle_is_reached_by_its_own_composition_row`: with
`composition._CACHE["social_contest.obstacle"]` replaced (and restored) by a stub returning `7.0`,
`sigma._composed_obstacle(inp)` returns `7.0` for any `SocialContestInput`. It executes the route. Change:
whichever assertion in `tests/valoria/test_module_registrar.py` counts or lists the production entry rows
gains the new role.

**Gate.** `python tools/export_composition.py --check` current, 17 roles;
`grep -n "import_module" engine/season/seam/wrappers/sigma.py` prints nothing; the new test green; the
headless and realm hashes equal the opening reading.

**Falsifier and control.** In a scratch worktree, before the edit: make `modules/social_contest/roll.py::obstacle`
return its value plus `1.0` → the seed-0 realm hash must move (the control sees the path). Revert. After
the edit: misspell the new row's target (`roll:obstacel`) → `export_composition.py --check` must exit
non-zero; that is the failure the reflective call could not give. Revert.

**Declared hash movers.** None. **Depends on:** `17_CENSUS_REST_1_deletions` D4 (same file, earlier in
B03). **Lands in:** B03. **Lands it:** one `valoria-author` lane, `sonnet`, `medium`. **Cost class:** edit.

---

## CI-04 · The season's 101 settings are in the typed export

**Finding.** H-04. The settings are the 101 keyword arguments of `DEFAULT_FIXTURES = Fixtures(...)`
(`engine/season/data/fixtures.py:213`); `tools/export_sim_params.py` reads module-scope assignments only, so none is exported.

**What dies.** Nothing. **What is added** is the smallest thing that closes the chain: one more reader in
the existing exporter (`valoria-simplify` ladder rung 4, *extend the neighbour*; a new exporter would be a
second owner of "the season's constants as data").

**Earning.** CLAUDE.md §5: a value the port uses lives in a typed artifact behind an exporter with a
blocking round-trip. The artifact exists and is checked by `tests/valoria/test_export_sim_params.py::test_sim_params_current`.

**Exact edits, in order.**

1. `tools/export_sim_params.py`: a function `_setting_rows() -> list` that parses
   `engine/season/data/fixtures.py`, finds the module-scope assignment whose target is `DEFAULT_FIXTURES`
   and whose value is a call to `Fixtures`, and for each `keyword` whose value `_literal()` accepts (the
   file's own anti-fabrication reader, `:54-60`) emits a row of the exporter's own shape
   `{key, name, value, kind, module, file, note}` with `module: "engine.season.settings"`,
   `key: "engine.season.settings.<name>"`, `file: "engine/season/data/fixtures.py"` and `note` the
   trailing comment of that line where one exists. A keyword whose value is not a literal (the five table
   names) is skipped and counted. The build appends these rows; `by_module` gains the key.
2. The count the build prints states how many settings it read and how many it skipped, and the
   build **raises** if it read none (an assertion that it asserted, CLAUDE.md §0.1 pt 2: a renamed
   `DEFAULT_FIXTURES` must not produce a smaller artifact that still checks green).
3. `python tools/export_sim_params.py --build`; commit the artifact with the tool.
4. `python tools/export_game_constants.py --check` (it composes from `sim_params.json`): expected current,
   because no mapped constant's key changes. If it is not, the new keys collided with a mapped name: give
   the setting rows the distinct module key above and rebuild.

**Tests.** Add to `tests/valoria/test_export_sim_params.py`:
`test_the_season_settings_are_exported_and_a_rename_cannot_empty_them`: the artifact holds a row
`engine.season.settings.pool_default` whose value equals `DEFAULT_FIXTURES.get("pool_default")`; the count
of setting rows is at least 90; and pointing `_setting_rows` at a source with no `DEFAULT_FIXTURES`
raises.

**Gate.** `python tools/export_sim_params.py --check` → `[SIM-PARAMS] current`;
`python tools/export_sim_params.py --search pool_default` prints the row; the new test green; hashes
equal (nothing at runtime reads the artifact, `W5` §2).

**Falsifier and control.** In a scratch worktree: change `pool_default=2` to `3` in `fixtures.py` without
rebuilding → `--check` must exit 1. Revert → `current`.

**Declared hash movers.** None; `sim_params.json` is regenerated. **Depends on:** `17_CENSUS_C1B_01` D3
(rebuilds the same artifact, earlier in B03); CI-10 first (it deletes `value_pointer_links.json`, which
would otherwise need rebuilding against the new rows). **Lands in:** B03. **Lands it:** one lane,
`sonnet`, `medium`. **Cost class:** edit.

---

## CI-05 · The realm's seven arms are in the same export

**Finding.** H-04. `build_realm`'s boolean parameters (`from_roster`, `goals`, `goals_complete`, `foreign`,
`guards`, `acquaintances`, `cast_attributes`; `engine/season/harness/populated.py:1014-1016`) decide what
world ships, and their defaults are in no artifact.

**What dies.** Nothing. **Preserved:** the defaults and every call that overrides one.

**Why not make them settings.** Considered and rejected: every setting must be named by a
hole-register row's `site:` (`engine/season/data/fixtures.py`, the comment in `claim_decay`: *"unless the
fixture is named in a register row's `site:`"*), so seven new settings are seven new register rows and a
changed `runs/results.json` (`harness/report.py:292` iterates them), for a list the port only
needs to *read*. Reading the defaults into the export costs one function.

**Exact edits, in order.**

1. `tools/export_sim_params.py`: `_realm_arm_records()` parses `engine/season/harness/populated.py`, finds
   `def build_realm`, and for each parameter with a literal default emits a row with
   `module: "engine.season.realm"`, `key: "engine.season.realm.<param>"`. It raises if `build_realm` is not
   found. (If CI-07 has moved the builder, the path constant is the one line that changes; it is read from
   `engine/season/data/files.py` if CI-07 added one there.)
2. Rebuild in the same commit as CI-04's rebuild if both are in flight; otherwise `--build` again.

**Tests.** Extend CI-04's test: the artifact holds `engine.season.realm.cast_attributes` with value
`False` and `engine.season.realm.foreign` with value `True` (the shipped defaults,
`audits/25_GROUNDING_ENGINE.md` L-08).

**Gate.** `--check` current; `--search engine.season.realm` prints the seven arms and `seed`.
`[ASSUMPTION: `cap`, whose default is `None`, is skipped, because the exporter's literal reader returns
`None` both for a `None` literal and for a non-literal (`tools/export_sim_params.py:54-60`); the lane opens
the caller of `_literal` and says which.]` **Falsifier:** flip `cast_attributes` to `True` in a scratch
worktree → `--check` exits 1.

**Declared hash movers.** None. **Depends on:** CI-04. **Lands in:** B03. **Lands it:** the same lane as
CI-04. **Cost class:** edit.
