# `engine/season/shape.py` — DECOMPOSITION PLAN (12 modules, 10 steps)

## Status: **PROPOSED. Reference under §0.05 — delete this file and the game behaves identically.**
## Lane: IN. Recorded 2026-09-06, ED-IN-0203. Adjudicated read-only; zero escalations.

> ### ⚠ THE TREE THIS PLANS DOES NOT EXIST ON `main`.
> `engine/season/` was added by PR #371 (`claude/issue-368-architecture-review-2nnilz`). Every
> `shape.py:NNNN` below is against that branch at `480cb43`. A cold reader who cannot find
> `engine/season/` will conclude this cites nothing; it cites a great deal.

**Why this is recorded rather than executed.** The split is a precondition for the epistemic work
(`references/design_rulings_2026-09-06.md` R8), and `epistemic.py` is one of the twelve modules —
so executing before R8's shape settles edits the same file twice. It is recorded because producing
it required a full read of all 6,771 lines and re-deriving it costs that again.

⚠ **Stated plainly: this job has ZERO game yield.** It is licensed only as the precondition of the
items that do. Do not treat a completed split as progress on the milestone (§0.2 — done means it
runs).

---

## 0 · Four seams a clustering-by-concern cannot see

About 85% of the file moves as blocks. What does not:

1. **Namespace coupling through module globals that tests REBIND.** Four names are rebound through
   the `shape` namespace and read by their consumers *through the same module's globals*:
   `S.ALIGNMENT` (read by `align()` at `:3434`), `S._LADDER` (read by `degree_of` at `:6669`),
   `S.belief_contradicts` (called by `Query.opening_set` at `:3287`), and `probes.py`'s
   `_s.contest = spy` (called by `SeasonDriver.resolve` at `:6137`). **Split the owner from the
   reader with a `from x import y` and each rebind becomes a silent no-op on a copied binding.**
   This is the primary silent hazard of the job, ahead of module identity.
2. **Two reflective lookups over `globals()`.** `matrix_rows_without_a_field` (`:1926`) finds carrier
   classes by name in the defining module's globals; `CHANNEL_PREDICATES` (`:4419`) finds `_ch_*` the
   same way. Move the names out and the first reports every kind as `unmodelled` — **a silent
   falsification in the direction its own docstring calls the worse one**; the second raises at
   import (loud).
3. **Import-time registries filled by decorators.** `REQUIREMENT_TYPES` (`:761`),
   `REQUIRES_PREDICATES` (`:4613`), `EFFECTS` (`:4935`). The verb table loads at `:1652` and
   `_build_clause` refuses any form not yet registered (`:1341`), so `OwnLedger` (`:962`) must be
   defined **below** the verb-table load.
4. **Carriers reach upward.** `Person.body`'s default reads `DEFAULT_FIXTURES` (`:2382`);
   `Office.__post_init__` calls `title_domain` (`:2493`), defined 2,150 lines later. And `Query`
   (`:3051`) is two families in one class — resolver-side World-first and person-side asker-first —
   which `architecture/meta/04_CODE_ARCHITECTURE.md:116` says must split **by module**.

**Also true today and worth knowing before trusting any line number here:** the blocking import
gate's own probe already loads every season module **twice under two names**.
`test_engine_does_not_import_systems.py:300` imports `engine.season.corpus_run` by dotted path;
`corpus_run.py:49` does `import shape as S` by bare name, resolving through `__init__.py:29-30`. That
subprocess holds `sys.modules['shape']` **and** `sys.modules['engine.season.shape']` as two objects,
each having run every loader, each with its own `DEFAULT_FIXTURES`, `EFFECTS` and `TRACE`. Harmless
only because nothing compares identities.

Existing line citations are already stale — `shape.py:1486-1487` lists 14 load-time `SystemExit`
sites and three of them are not raises; `hole_register.yaml:1775` cites `emits_at` at line 701 when
it is at `:1476`. Nothing noticed, because nothing reads them.

---

## 1 · The module suite

**Flat files in `engine/season/`, NOT subdirectories**, for three concrete reasons: `_HERE`-relative
paths (`:290, 449, 1407, 4912, 6505, 6600`) stay valid; `test_jordan_no_definition_is_hardcoded_in_a_body`
discovers its corpus by `HERE.glob("*.py")` and would **silently stop scanning** a subdirectory; and
`SOURCE_353_TEXT` returns `""` when its path is wrong (`:4913`), which makes `names_a_verb` charge
every invented verb to the design (`:5832`) — the exact mis-attribution it exists to prevent,
silently. Directories can come later, once both glob-based guards are made recursive.

| layer | module | owns |
|---|---|---|
| 0 | `trace_log.py` *(exists)* | `TRACE` |
| 1 | `gaps.py` | `InstrumentDefect`, `ShapeGap`, `Unspecified`, `Forbidden`, `NoProducer`, `Collision`, `Unowned`, `Ungraded`, `Ineligible`, `expect_refusal` |
| 1 | `ids.py` | `H`, `ROOT` |
| 2 | `data.py` — the ONE loader | `_HERE`, `load_yaml`, `Step`, `WriteClass`, `_STEP_CLASS`, `MatrixRow`, `_load_write_matrix`, `MATRIX`, `MATRIX_RETIRED`, `PARTITION_ASSUMED`, `assume_partition_row`, `_load_rosters`, `roster`, `roster_map`, `table`, the 24 bound rosters, `office_faction`, `title_domain`, `title_rank`, `_load_matter_tables`, `WEAR_RATES`, `BAND_FLOORS`, `SUBSISTENCE_WEIGHTS`, `SITE_YIELD`, `matrix_row`, `partition_lookup`, `rows_without_a_producer`, `NO_PRECONDITION` |
| 3 | `fixtures.py` | `Fixtures`, `DEFAULT_FIXTURES` |
| 3 | `requires.py` — the grammar | `_Unknown`, `UNKNOWN`, `Observation`, `Verdict`, `_as_number`, `_bound`, `COMPARATORS`, `REQUIREMENT_TYPES`, `requirement_form`, `Requirement` + six forms incl. `OwnLedger`, `AllOf`, `TypedRequires`, `_observe`, `evaluate`, `binding_of`, `REQUIRES_STEMS`, `LEDGER_DERIVED_STEMS`, `_require_known_stem`, `_build_clause`, `build_typed_requires`, `LedgerReader` |
| 4 | `verbs.py` | `VerbRow`, `_load_verb_table`, `VERB_TABLE` |
| 5 | `carriers.py` | `Tenure`, `StateChange`, `Event`, `Claim`, `Sensation`, `View`, `Question`, `Candidate`, `Scene`, `Act`, `Person`, `Site`, `Record`, `Proposition`, `Office`, `Rung`, `matrix_rows_without_a_field` |
| 6 | `world.py` — the store + the gate | `_TenureView`, `_entity_digest`, `MATRIX_REFUSAL_LAW`, `World` |
| 7 | `queries.py` | `WorldReader`, the eleven World-first statics of `Query` (`:3053-3171`), `questions_for`, `occasioned_by` |
| 8 | `predicates.py` — governance | `REQUIRES_PREDICATES`, `requires_predicate`, `in_holdings`, `under_purview`, `titles_held`, `highest_title_rank`, `_req_confer`, `_req_revoke`, `_req_dispatch`, `_req_convene` |
| 8 | `effects.py` | `EFFECTS`, `effect_for`, `_operand`, the ten `_eff_*` |
| 9 | `epistemic.py` | `belief_contradicts`, `act_refs`, `claim_subjects`, `_event_place`, the five `_ch_*`, `CHANNEL_PREDICATES`, `observers_for`, and the deposit body at `:6323-6423` as one function |
| 10 | `decision.py` — AX-2's island | `_load_alignment`, `ALIGNMENT*`, `alignment_at`, `align`, `stance_toward`, `urgency`, `make_chooser`, `person_side_eligible`, `containing_rung_of`, `store_kind_of`, `_derive_operand`, `operands_for`, `agreement`, `standing_of`, `_payload_of`, `pack_scenes`, `view_ids`, `body_band_penalty`, `aggregate_questions`, `sense`, and the four person-side statics (`budget`, `opening_set`, `assemble`, `entrenchment`) as module functions |
| 11 | `seam.py` | `ContestError`, `contest_subsystem`, `_LADDER`, `degree_ladder`, `ladder_error`, `Resolution`, `combat_degree`, `degree_of`, `contest` |
| 11 | `combat_seam.py` *(exists)* | as today |
| 12 | `loop.py` | `SeasonDriver`, `as_scenes`, `stratum_of`, `resolvable_verbs`, `names_a_verb`, `SOURCE_353_TEXT` |
| — | `shape.py` | transitional facade; re-exports, owns nothing; deleted at step 10 |

**Direction rule, stated so it applies without the picture:** *a module imports only from a strictly
lower layer; the registries a decorator fills live in the module that defines the decorated things;
no module below `loop.py` imports `loop.py`.* Three grep-checkable corollaries — `decision.py`
imports neither `world` nor `queries` (`04:116`, *"the decision compiled where `World` is not a
name"*); `combat_seam.py` imports `decision` and `ids`, never `seam` or `loop`; `epistemic.py`
imports nothing from `decision` or `loop`. The graph is acyclic by construction of the layer
numbers, and the one live cycle (`shape.contest` ↔ `combat_seam`, both function-local) dissolves
because `body_band_penalty` lands below the seam.

### The placements a lazy pass would get wrong

| symbol | tempting | ruled | decided by |
|---|---|---|---|
| `WorldReader` (`:1128`) | grammar | `queries` | calls `Query.parent_of`/`presence` and reads `World._STATE_COLLECTIONS` at call time; the grammar must stay reader-agnostic |
| `LedgerReader` (`:1287`) | epistemic | `requires` | needs only `UNKNOWN`; both consumers sit above it |
| `title_domain`, `title_rank` (`:4636`) | governance | `data` | pure roster reads, and `Office.__post_init__` needs them below the resolver |
| `matrix_rows_without_a_field` (`:1903`) | data | `carriers` | its `globals()` lookup must run where the classes are defined; `data` cannot import `carriers` |
| `MATRIX_REFUSAL_LAW` (`:1968`) | data | `world` | its only reader is the gate (`:2804`) |
| `questions_for`, `occasioned_by` | decision | `queries` | both take a `World` first; the AST guard scans for `Person`-first functions with a `World` annotation |
| `sense` (`:4550`) | queries | `decision` | the guard whitelists the NAME inside the scanned file; it must stay where the guard scans |
| the alignment block | verbs | `decision`, **whole** | the sweep rebinds `ALIGNMENT` and `align` reads it through its own globals; splitting makes the H-66 sweep a fake control |
| `stratum_of`, `resolvable_verbs` | verbs | `loop` | read `Act`, `REQUIRES_PREDICATES`, `EFFECTS` — all above `verbs` |
| the person-side `Query` statics | keep `Query` whole | `decision`, as functions | `04:116` splits the families by module. Cost: **56 call sites** across 5 files; a mechanical rename |

**Genuinely ambiguous, left to the implementer:** the ledger eviction (`:6429-6446`). `04:149` gives
`state/ledgers` "the eviction comparator", which makes it `epistemic.py`'s; `test_season_shape.py:265`
pins it inside `witness`. **Whichever moves, the other moves in the same commit.**

---

## 2 · What must not be split

1. `ALIGNMENT` + `align` + `alignment_at` + `ALIGNMENT_DECLARED` — the sweep rebinds the global.
2. `_LADDER` + `degree_ladder` + `degree_of` — same mechanism; `degree_of` is "THE ONE PLACE" a result becomes a token.
3. `VerbRow.writes_at` + `emits_at` (`:1476-1543`) — one polarity, checked against each other at load.
4. The gap taxonomy (`:72-150`) — `InstrumentDefect` is deliberately not a `ShapeGap`; the separation is by class.
5. `Step`/`WriteClass`/`MatrixRow` + `_load_write_matrix` — the loader cross-checks the map against the YAML's `class:` column.
6. `_TenureView` + `World.tenures` + `add_tenure` + `_rehome` — the read/write-asymmetry guard §0.1 pt 1 names.
7. `_operand` + the ten `_eff_*` — "THE OWNER OF THE RULE, AND THREE EFFECTS HAD THEIR OWN COPY".
8. `Fixtures` + `DEFAULT_FIXTURES`.
9. `Event.__post_init__`'s `causes` check and the gate's deliberate absence of one.
10. `season()` — one function, one file.
11. `REQUIRES_STEMS` + `LEDGER_DERIVED_STEMS` with the grammar.

---

## 3 · `SeasonDriver` at 1,151 lines

**It splits by step and it should — but `season()` does not, and the freeze invariant crosses three
steps.** The step bodies never call one another and share exactly three cumulative dicts on `self`
(`resolved`, `scenes`, `act_of`) whose non-resetting is load-bearing. `t` advances at exactly one
line (`:6484`). The freeze is written at `:5630`, read at `:5637`, cleared at `:6064`.

**Ruling:** `loop.py` keeps the class as owner of the three dicts and of `season()`. The four barrier
bodies may move to sibling modules **only as the same methods** (a mixin per step, or module
functions the methods delegate to) so `inspect.getsource(S.SeasonDriver.witness)` and `.resolve` and
`.deliberate` keep resolving to real bodies — eleven tests read them. **The honest state is one
class, one file, ~1,150 lines, and that is acceptable if the split stops at the module boundary.**

---

## 4 · Migration order — each step independently revertible

**The instrument for every step is the same pair:** `python engine/season/delta.py HEAD` prints
`PROBE FLIPS 0` and no `<-- MOVED`; `python engine/season/headless.py --case NPC-088 --seasons 2
--seed 0` prints the same `hash`. The hash is module-layout-invariant by construction —
`_entity_digest` uses dataclass `repr` (`__qualname__`, not `__module__`) and `H` hashes strings —
and `trace_log.py` records no caller file or line, so `TRACE.txt` is invariant too. Plus
`pytest engine/season/tests -q` and `pytest tests/valoria/test_engine_does_not_import_systems.py -q`.

| step | what | artifact beyond the pair |
|---|---|---|
| **0a** | convert the ~21 live `shape.py:NNNN` citations to `shape.py::symbol` (§5) | the grep finds only labelled historical rows |
| **0b** | **dotted imports, `shape.py` still monolithic** — every sibling and test imports `from engine.season import shape as S`; delete `__init__.py:29-30`, `tests/conftest.py:10-12`, `run_cases.py:23`, `report.py:29`, `headless.py:35-36`, and the root insert in `degree_ladder()`. Script entry points keep ONE root insert **guarded by `if __name__ == "__main__"`** | the identity probe (§6 item 1) prints nothing; `PATH_SEAM_ALLOWED` unchanged at two |
| **1** | `gaps.py`, `ids.py` | `assert shape.Forbidden is gaps.Forbidden` |
| **2** | `data.py`, `fixtures.py` — moved as one block so load order is unchanged | `len(data.MATRIX)`, `len(data._ROSTERS)` match |
| **3** | `requires.py`, `verbs.py` — decorator registry and consumer together | the loader still refuses a planted eighth form |
| **4** | `carriers.py`, then `world.py` | `test_h118_content_hash_folds_*` green; the `SystemExit` count re-pointed to the model set and still 28 |
| **5** | `queries.py`, `predicates.py`, `effects.py` | `EFFECTS` and `REQUIRES_PREDICATES` keys diffed identical |
| **6** | `epistemic.py` — **coordinate with the R8 work, do not do it for them** | `test_wb_*` green with `S.belief_contradicts` re-pointed |
| **7** | `decision.py` — the 56 `Query.<person static>` call sites renamed in the same commit | `grep 'import.*\(world\|queries\)' decision.py` → 0; H-66 sweep green |
| **8** | `seam.py`; `combat_seam.py` imports `decision.body_band_penalty` and `ids.H` dotted — **the cycle ends here** | ladder test green with `S._LADDER` re-pointed; the `probes.py` spy re-pointed |
| **9** | `loop.py`; `shape.py` becomes a pure facade | every `inspect.getsource` test green unchanged |
| **10** | re-point the eleven source-scanning tests from `"shape.py"` to the model set; delete the facade; reconcile `CURRENT.md`'s "11 modules" | `grep -rn 'import shape\|from shape' engine/ tests/` → 0 |

**Against PLAN item 1.6.** The split **subsumes 1.6's import half** (step 0b is it) and depends on
nothing. 1.6's composition half — `import combat_seam` as a `composition_roles` row, deleting the
`module_contracts.yaml` read at `:6505`, deleting `World.manifest`, re-basing `World.boot` on
`composition.ROLES` — should land **after step 8** as an edit to `seam.py` and `world.py`, or it is
edited twice. ⚠ Two corrections to 1.6 as written: its artifact *"`grep sys.path` → 0"* is
over-strict for the four script entry points (49 citations invoke them as `python engine/season/<x>.py`),
so either the artifact excludes `__main__`-guarded inserts or those 49 change to `python -m`; and the
identity probe is the real property while the grep is a proxy.

---

## 5 · Citation strategy

101 matching lines for `shape\.py:\d+` in 19 files; **81 under `proposals/2026-09-04-degree-sweep/`,
~20 live in 8 files.**

- **The degree-sweep 81 are FROZEN. Do not touch.** They record the file *as it stood at that run*;
  re-pointing them would make the record describe a file the run never saw.
- **The ~20 live convert to `shape.py::symbol` before step 0b**, on `hole_register.yaml`'s existing
  convention (13 `::` citations already there). After step 10 they become `engine/season/<module>.py::X`.
- **Also convert the three in-file line lists that are already stale** — stale citations are worse
  than converted ones because they stop the next reader checking.
- **No checker.** A line-citation checker is forbidden under §0.1 pt 5, and correctly so.

---

## 6 · Falsifiers, named before the work

1. **Two names for one module.** In a subprocess, import every `engine.season.*` module dotted, run
   `headless.build_world`, then assert no bare-name module resolves to a file under
   `engine/season/`. Today that set is non-empty (§0). **Plant:** add `import shape` to any sibling
   and it must fail. Keyed on **file path**, which cannot be spelled around.
2. **A duplicated rule.** `sorted(EFFECTS)`, `sorted(REQUIRES_PREDICATES)`, `sorted(REQUIREMENT_TYPES)`
   identical to today; `test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` green.
   A second `importlib` call anywhere but `composition.require` is a second resolver.
3. **The source-scanning guards must still be able to FAIL.** Eleven sites read `shape.py` by path.
   Most are self-detecting. **Two are not:** the `"if False" not in SHAPE_CODE` dead-code guard and
   the `caller_supplied_max_depth` guard both **pass vacuously on an empty facade**. And the
   `MODEL`/`CORPUS` split means a literal roster landing in `carriers.py` would be scanned under the
   *corpus* rule — Jordan's no-hardcoding guard **silently narrowed**. Plant a `frozenset({"a","b","c"})`
   in a model module; the guard must go red.
4. **The rebinding rule.** The four rebinds are self-detecting today. Keep them — they are the
   falsifier for *a rebound name is read through the owner's namespace*.
5. **`t` advances once.** AST over `loop.py`: exactly one assignment targeting `w.tick`. **Does not
   exist; write it if and only if the steps leave the class.**
6. **`decision.py` sees no World** — grep plus the existing AST guard re-pointed, control intact.
7. **The hash and the corpus** — `PROBE FLIPS 0`, byte-identical `headless` hash at every step,
   `pytest engine/tests` byte-identical as the negative control.

---

## 7 · What needs Jordan — nothing, with §0's five tests run

| candidate | closes at | by |
|---|---|---|
| whether to split at all | test 3 | `04_CODE_ARCHITECTURE.md:127-139` prescribes nine modules |
| `Query` split by module vs whole | test 3 | `04:116` — "split **by module**, not by first parameter" |
| flat files vs directories | test 5 | three named silent-weakening hazards (§1) |
| `-m` vs guarded root inserts | test 5 | 49 command citations; a guarded insert is not a seam by the gate's own predicate |
| the degree-sweep 81 | test 2 | a finished run's record; irrelevant to the live tree |
