# Workplan v12 — part 6, continued: batches B03a-prose, B13-pc-package, B16M-mb-engine-words

## Status: PROPOSED (the continuation of `workplan_v12_part6.md`, `V12_STRUCTURE_part2.md` §4.1's `_cont` rule; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The head of the part before this one (its Status, Written-against, Words, Paths and the two readings, **the realm hash at seed s, k seasons** and **the headless hash**) governs this file; nothing there is restated. Every batch here is hash EQUAL and ends with a `.99` position that records the EQUAL readings (E-1).

---

## Batch B03a-prose · lane IN · wave W5 · step S5 · HASH EQUAL
INVOCATION: /methodology-execute Batch B03a-prose
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B03-hygiene
GATE: Batch B03c-boot
GATE: Batch B16L-mb-words
REQUIREMENT: none — reading cost of every later batch (H-03, H-07; CIP §2: "B03a's reason is reading cost on every later batch"); no row moves
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; CIP CI-01 "Gate" and CI-02 "Gate", copied where they are commands):
  CI-01 gate 1, *parsed-object equality*: the scratch probe of B03a.01 → equal for `engine/season/rosters.yaml` and `engine/season/verb_table.yaml`, and the set of rows carrying each of `requires_typed_note`, `effect_decline_note`, `requires_decline_note`, `formation_decline_note` equal;
  CI-01 gate 2: `python -c "import engine.season.data"` → exit 0;
  CI-02 gate 1, *AST equality modulo docstrings*: `python probe.py <batch-start-sha> $(git diff --name-only <batch-start-sha> -- '*.py')` → `AST-EQUAL`;
  CI-02 gate 2: `GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python tools/ci_sim_fabrication_check.py` → green;
  CI-02 gate 4: `python tools/export_engine_params.py --check`, `python tools/export_sim_params.py --check`, `python tools/export_composition.py --check` → all current, **with no rebuild** (B03a.02's preserved rule 7); `python tools/export_season_registries.py --check` → current (rebuilt once, in B03a.01, for the note strings it copies);
  CI-01 gate 3 and CI-02 gate 3: the headless hash and the realm hash at seeds 0 and 2, one season → equal to B03c's close (`reading @<sha>`), and the realm hash at seed 1 → equal;
  `python -m pytest engine/season/tests/test_season_shape.py engine/season/tests/test_governance_build.py tests/valoria/test_module_registrar.py -q -n auto` → pass (CI-01's covering files);
  `python -m engine.season.harness.register --check` → exit 0; `python -m engine.season.harness.register --requirements` → nine lines, unchanged; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names, once (CI-02: "At the close, the suites once");
  readings for the close, not thresholds: CI-01 gate 4, `wc -c engine/season/rosters.yaml engine/season/verb_table.yaml` before and after; CI-02 gate 6, `W1`'s table re-run (the comment-and-docstring share per package, before and after);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; no conjunct is named, so no `reading:` record is written and `status:` is not edited (`IS-A-12`).
RE-PIN: none (B03a.99 records the EQUAL readings). CIP §3.1: "**No item is a declared mover.** A moved hash at any gate below is a defect in the edit: revert the item."
IDS: ED-IN 0; H 0
DIALS AT CONTROL: none
UNDECIDED: (1) CI-02's earning lists four classes of reader of source prose; a fifth exists at `aa31fd2`: `tools/export_sim_params.py` copies the trailing comment of every module-scope assignment it exports into `sim_params.json` as that row's `note` and `citation` (`_comment`, `_citation`), over `ci_common.sim_reference_roots()`, which covers CI-02's scope; CI-02's own gate 4 requires that export current. So B03a.02 keeps those trailing comments byte-identical (its preserved rule 7) and the gate reads current with no rebuild; the other reading trims them and rebuilds the artifact in the same commit. (2) CI-02 names eight producer lanes and a scope that also holds `engine/season/gaps.py`, `trace_log.py` (no lane named) and `boot/` (added by A-102, no lane named): `gaps.py` and `trace_log.py` join the `decision` + `epistemic.py` lane (the package's top-level files), `boot/` joins the `data` lane (the builder reads `data/`); the other reading opens a ninth producer. (3) CI-01 and CI-02 are one item each, each fanned to the producers its source names (the skill §0.3: the instruction names file-disjoint sub-parts), integrated and committed once; the other reading writes one item per file or per package (E-13), which serialises the producers and loses CIP's "most of it in parallel".
C(B03a-prose): this batch's entries; the plan's head parts; `engine/season/rosters.yaml`, `engine/season/verb_table.yaml`; `engine/season/data/rosters.py`, `engine/season/data/verbs.py`, `engine/season/manifest/registry.py` (the presence checks of the four `*_note` columns, read only); `engine/season/tests/test_season_shape.py` (its `writes_note` read), `engine/season/tests/test_governance_build.py` (its raw-text read), `tests/valoria/test_module_registrar.py` (`formation_decline_note`);
  every non-test `*.py` under `engine/season/{loop,state,decision,queries,data,seam,manifest,boot}`, `engine/season/epistemic.py`, `gaps.py`, `trace_log.py`, `engine/substrate/`, `engine/dice_engine/`, `modules/` (CIP §3.2's row, `boot` added by A-102); the test files that read source as text (`grep -rlE "getsource|ast\.parse|read_text\(\)" engine/season/tests tests/valoria`);
  `tools/ci_sim_fabrication_check.py`; `tools/export_engine_params.py`, `tools/export_sim_params.py` (`_comment`, `_citation`), `tools/export_composition.py`, `tools/export_season_registries.py` (B03g) and their artifacts; `master/work/W1_AREAS_AND_LINES.md` and `W5_DATA_CHANNELS.md` §1 (the census method, read for the close's readings only);
  instruments: `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `harness/headless.py`; the closing SHAs of B03, B03c, B16L; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_IN.md`, the skill and `methodology-close`).
SERIAL EDGES: within the batch: B03a.01 → B03a.02 (CIP §3.3: "CI-01 (two files, two lanes at once) → CI-02 (one lane per package, at once, disjoint files)"; CI-02 lands "after CI-01") → B03a.99. CI-02's AST gate is per file and would be broken by any code edit in the batch (CIP §2: "Why its own batch").
  With other batches, by file: every file of CI-02's scope B03 (CI-08 trims `loop/driver.py` first; the census deletions) → B03c (`boot/` exists) → B16L (its renames, comments included) → B03a → B04, B13 (CI-09 edits the import lines of `modules/combat`: "serial, prose first, so CI-02's AST gate is not disturbed") and B16M (L2's renames in `modules/mass_battle`) and every later batch; `rosters.yaml`, `verb_table.yaml` B16L → B03a → B04 (CIP part 2 §5 note 1: after B03a a batch adds a roster or row at the end of its family's block); `engine/engine_params/season_registries.json` B16L.99 → B03a.01.
FILE CENSUS: B03a.01: `engine/season/rosters.yaml`, `engine/season/verb_table.yaml`, `engine/engine_params/season_registries.json` (re-derived). B03a.02: every non-test `*.py` of CI-02's scope (comments and docstrings only).
PARALLEL: S5, alone in the whole plan (`V12_STRUCTURE.md` §2.3: "it edits the comments of every game-code file").
COST: edit, the largest by volume (CIP CI-02: "about 31,000 prose lines in scope"); `sonnet`, `high` producers, two for CI-01 and eight for CI-02, `isolation: worktree`, disjoint files; "no critic fan (the AST probe is the control, and a comment-only diff has no behaviour to attack)" (CIP CI-02, read with BATCH-CLOSE: the close's phases still run once, over the batch's range).
EST: 3.7 h [estimate: §2.4's formula over three positions (0.4 h × 3 + 2.5 h), E-15. CIP's own estimates are larger and are the better guide here: CI-01 "one to two hours of agent time per file", CI-02 "the batch is a day of agent time, most of it in parallel"]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B03a.01 | the two largest registries carry values and definitions, not their history | CI-01 (H-03, H-07) | BUILD | EQUAL | Batch B03, Batch B16L |
| B03a.02 | the source says what it does; its history lives in the commits | CI-02 (H-03) | BUILD | EQUAL | B03a.01; Batch B03c, Batch B16L |
| B03a.99 | re-pin and close readings: the EQUAL readings recorded | E-1 | BUILD | EQUAL (records) | B03a.01, B03a.02 |

### B03a.01 — the two largest registries carry values and definitions, not their history · CI-01 · BUILD · HASH EQUAL
- SOURCE: `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` CI-01 ("What dies", "Exact edits" 1–5, "Tests", "Gate", "Falsifier and control"); closes H-03 (its registry half), H-07.
- ADVANCES: none of the nine; reading cost for every batch that edits the two hot files (130 and 66 proposals edit them, CI-01's finding).
- INSTRUCTION (CI-01, copied): "**What dies.** Dated narrative inside `note:` and `*_note:` strings and inside comment blocks: who found what, what a cell used to say, measurement logs, the story of a correction. **What is preserved, byte for byte:** every key, value, row and column a loader reads; every `source:`; every `[ASSUMPTION; …]` tag and `revert:` clause; one or two sentences per annotation saying what the roster or cell *is* (the call-site definition CLAUDE.md §4 asks for)." "**Exact edits** (one lane per file; the two files are disjoint).
  1. Open the two tests that read annotation text and note what they assert: `engine/season/tests/test_season_shape.py` (reads `writes_note`) and `engine/season/tests/test_governance_build.py` (reads the verb table's raw text). Whatever string they match is kept verbatim.
  2. For each `note:` / `*_note:` value and each comment block, apply the rule above. An annotation that is only history is cut to its one-line definition; it is never deleted if it is one of the four presence-checked columns on a row that carries it.
  3. Leave `source:`, `cite:`, `ground:`, `row:` and every other key untouched. Leave the other season YAML files alone: their prose is small … and they are not hot files.
  4. The commit body names the parent SHA as where the annotations as they stood can be read. No `FORK:` row: no file is deleted.
  5. `unified/U1_GLOSSARY.md`: no row changes (no term is introduced, renamed or retired)."
  Added by this plan: 6. `python tools/export_season_registries.py --build`, in the same commit (B03g.01's artifact copies both files whole, notes included; GO-09's rule: a registry edited without a re-export reds `--check`).
- WHERE: `engine/season/rosters.yaml` (`note:`, `*_note:` values, comment blocks); `engine/season/verb_table.yaml` (the same); `engine/engine_params/season_registries.json` (re-derived).
- TESTS: "None added. Covering files, run once each after the edit: `python -m pytest engine/season/tests/test_season_shape.py engine/season/tests/test_governance_build.py tests/valoria/test_module_registrar.py -q -n auto`."
- FALSIFIER and CONTROL (CI-01): "In a scratch worktree: (a) blank one `requires_typed_note` on a row whose `requires_typed` is null → the import must fail (`data/verbs.py`'s presence check); (b) change one roster value → gate 1 must report the file unequal. Both seen, then reverted, before the real edit is read as green."
- GATE (CI-01): "1. *Parsed-object equality.* A scratch probe (not committed): `yaml.safe_load` each file at the batch's base and at the edit; delete every mapping key equal to `note` or ending in `_note`, and compare. Expected: equal for both files. Then compare the **set of rows that carry** each of `requires_typed_note`, `effect_decline_note`, `requires_decline_note`, `formation_decline_note`: expected equal. 2. `python -c "import engine.season.data"` exits 0 (the loaders' own refusals run at import). 3. The headless hash and the realm hashes at seeds 0 and 2 equal the batch's opening reading. 4. A reading for the close, not a threshold: `wc -c` of the two files before and after." With `python tools/export_season_registries.py --check` → current.
- HASH MOVERS: none ("Declared hash movers. None").
- DEPENDS ON: EXISTS-IN-TREE `engine/season/data/verbs.py` (the `requires_typed_note`, `effect_decline_note`, `requires_decline_note` presence checks), `engine/season/manifest/registry.py` (the same), `tests/valoria/test_module_registrar.py` (`formation_decline_note`); V12 Batch B03 ("the census edits to these files land first"), Batch B16L (its renames in both files), Batch B03g (`tools/export_season_registries.py`).
- GLOSSARY: none (CI-01 step 5).
- COST and TIER: edit, large by volume; "two `valoria-author` lanes, `sonnet`, effort `high`, one per file (N−1 would leave one 350 KB file to a lane already holding the other)"; the integrator merges the two worktrees (disjoint files) and runs step 6 once.
- LANDS IT: B03a's two producers, `isolation: worktree`, fanned (the skill §0.3); a `WIP checkpoint: B03a.01` at each hand-back; one `Item: B03a.01` commit, `[skip ci]`.

### B03a.02 — the source says what it does; its history lives in the commits · CI-02 · BUILD · HASH EQUAL
- SOURCE: CIP CI-02 ("Scope", "What dies", "What is preserved" 1–6, "Earning", "Exact edits" 1–4, "Tests", "Gate", "Falsifier and control"); CIP §3.2's row (`boot` added by A-102); closes H-03 (its source half).
- ADVANCES: none of the nine; reading cost ("52 % of the non-blank lines of non-test Python are comment or docstring; 60 to 65 % in `loop/`, `state/`, `decision/`, `queries/`, `seam/`").
- INSTRUCTION (CI-02, copied): "**Scope.** Non-test `*.py` under `engine/season/{loop,state,decision,queries,data,seam,manifest}`, `engine/season/epistemic.py`, `gaps.py`, `trace_log.py`, `engine/substrate/`, `engine/dice_engine/`, `modules/`" and `engine/season/boot/` (CIP §3.2: "`boot` added by A-102: game code once B03c lands before B03a"). "**Not** `engine/season/harness/` (eleven of its files build their `--help` from `__doc__`, and it is an instrument package), not tests …, not `tools/`."
  "**What dies.** In docstrings and comments: accounts of what the code used to do, who caught which defect, measurement logs, revision histories (`REV 4, TWICE`), the names of deleted files, a second telling of a rule that a cited row already states."
  "**What is preserved.** 1. A module docstring's statement of what the module does, what it owns, where its inputs come from and the Layer 1 row or ED id that governs it. 2. A function docstring's contract: inputs, return, what it raises and why. 3. A comment that explains a line a reader would otherwise misread. 4. Every `# [JUSTIFIED: …]`, `# [DECLARED-DIVERGENCE: …]`, `[ASSUMPTION; …]` tag and `# noqa`, byte-identical and on the same code line or the line directly above it (`tools/ci_sim_fabrication_check.py` reads a tag per line; `layer-conformance` THE CONTROL). 5. Jordan's words where a comment quotes them, with their date. 6. Every string that is code: the `law=` and `needs=` arguments of a refusal are arguments of a call and are not touched." Added by this plan (UNDECIDED (1)): **7. The trailing comment of every module-scope assignment that `tools/export_sim_params.py` exports, byte-identical** (its `_comment` reads it into that row's `note`, and `_citation` its cite, so the artifact stays current with no rebuild; CI-02's own gate 4).
  "**Exact edits.** One lane per package (`loop`, `state`, `decision` + `epistemic.py`, `queries`, `data` + `manifest` + `engine/substrate` + `engine/dice_engine`, `seam`, `modules/combat`, `modules/mass_battle` + the small modules): eight lanes, disjoint files, `isolation: worktree`." With `gaps.py` and `trace_log.py` in the `decision` lane and `boot/` in the `data` lane (UNDECIDED (2)).
  "1. Before editing a file, list the tests that read it as text: `grep -rlE "getsource|ast\.parse|read_text\(\)" engine/season/tests tests/valoria` and, in those, the names of this file's functions. A docstring or comment a test matches on is kept verbatim.
  2. Edit comments and docstrings only, by the rules above. Do not reorder, rename, re-indent or reflow code; do not delete a docstring outright where the function has one (its first sentence stays), so no `__doc__` becomes `None`.
  3. Order within a lane: largest prose first (`W1`'s last table: `queries/world_q.py`, `modules/mass_battle/hierarchy/units.py`, `state/gate.py`, `modules/mass_battle/orchestration.py`, `decision/options.py`, `data/verbs.py`, `state/world.py`, `data/fixtures.py`).
  4. `loop/driver.py`'s docstring after CI-08: what the driver is, the seven steps bound at the foot of the file, the tokens it mints; nothing about the docstring's own past."
  The comments CI-07 left naming `build_realm` or `populated` in the 19 files of `loop/`, `state/`, `data/`, `queries/`, `decision/` and `epistemic.py` (CIP part 2 CI-07 step 5: "are CI-02's") name `boot/realm.py` after this item.
- WHERE: every non-test `*.py` of the scope above (comments and docstrings only).
- TESTS: "None added. The suites run once at the batch close (CLAUDE.md §0.4); mid-batch, each lane runs the test files step 1 listed for its package."
- FALSIFIER and CONTROL (CI-02): "In a scratch worktree: (a) change one comparison operator in an edited file → gate 1 must name the file; (b) move one `[JUSTIFIED: …]` tag off its line → gate 2 must go red. Both seen and reverted before the gate's green is read." Added with rule 7: (c) edit one exported assignment's trailing comment → `export_sim_params.py --check` must go red; seen and reverted.
- GATE (CI-02, copied): "1. *AST equality modulo docstrings*, per edited file (a scratch probe, not committed):
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
  run as `python probe.py <base-sha> $(git diff --name-only <base-sha> -- '*.py')`. Expected: `AST-EQUAL`. Comments are not in the tree and docstrings are stripped, so equality means no code token moved. 2. `GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python tools/ci_sim_fabrication_check.py` green. 3. The headless hash and the realm hashes at seeds 0 and 2 equal the opening reading. 4. `python tools/export_engine_params.py --check`, `python tools/export_sim_params.py --check`, `python tools/export_composition.py --check` all current (the exporters read these files). 5. At the close, the suites once. 6. A reading for the close: `W1`'s table re-run (the probe is `census.py` in this lane's scratchpad; it is thirty lines of `ast` and `tokenize` and may be rewritten from the method line of `W1`)." Gate 5 and 6 are the batch gate's.
- HASH MOVERS: none ("Declared hash movers. None").
- DEPENDS ON: EXISTS-IN-TREE `tools/ci_sim_fabrication_check.py`, `tools/export_sim_params.py::_comment`, `::_citation`; V12 Batch B03 ("CI-08 trims `driver.py`'s imports first; the census deletions remove files this item would otherwise edit"), Batch B03c (`boot/` in scope), Batch B16L (its renames land first), V12 B03a.01 ("Lands in: B03a, after CI-01").
- GLOSSARY: none (no term changes).
- COST and TIER: edit, the largest by volume; "eight `valoria-author` lanes, `sonnet`, effort `high`; no critic fan (the AST probe is the control …)".
- LANDS IT: B03a's eight producers, `isolation: worktree`, fanned (file-disjoint packages; fire one, await its first token, then the rest, CLAUDE.md §10 point 3); a `WIP checkpoint: B03a.02` at each hand-back (the skill, CHECKPOINTS); the integrator runs gate 1 over the union, then one `Item: B03a.02` commit, `[skip ci]`.

### B03a.99 — re-pin and close readings: the EQUAL readings recorded · E-1 · BUILD · HASH EQUAL (records)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.12.
- ADVANCES: none; the batch's record.
- INSTRUCTION: (1) The headless hash and the realm hash at seeds 0, 1, 2, one season, against B03c's close (`reading @<sha>`): all equal is the expected reading; a moved hash reverts the item whose diff reaches it ("A moved hash at any gate below is a defect in the edit: revert the item", CIP §3.1). (2) Every line of the BATCH GATE, the AST probe over the whole batch range included. (3) The close's readings in this commit's body (§5.12), with the two size readings. Nothing is re-pinned.
- WHERE: none but the commit body.
- TESTS: none new.
- FALSIFIER and CONTROL: a moved hash, a non-`AST-EQUAL` file, a stale exporter. Control: B03c's close readings.
- GATE: the BATCH GATE above, every line.
- HASH MOVERS: none.
- DEPENDS ON: V12 B03a.01, B03a.02.
- GLOSSARY: none.
- COST and TIER: reading; `sonnet`, `medium`.
- LANDS IT: B03a's producer; `Item: B03a.99`, the batch's last commit (no `[skip ci]`).

| STOP. Batch B03a-prose closes here |

---
