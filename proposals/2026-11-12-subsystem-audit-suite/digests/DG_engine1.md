# Digest engine1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: code and data under `engine/season/` (23 files). Read in full, in assignment order. Finding ids `F-CORE-NN` are from `proposals/2026-11-12-subsystem-audit-suite/audits/01_CORE_audit*.md`. Counts quoted below were taken from the live import (`python3 -c` imports of `EFFECTS`, `VERB_TABLE`, `matrix`), not from the files' own prose.

### engine/season/__init__.py
- **What it is:** package docstring only (40 lines, no code); adoption-era (ED-IN-0204 / ED-IN-0203), no author-lane.
- **Status:** none (module docstring). Reading: live, but partly stale prose.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Declares the package has NO `sys.path` insert and every internal import is relative, one identity per module (`:4-18`); remaining `sys.path` mutations are declared seams reaching OUT (flat combat module set, repo root for `engine.dice_engine`, degree sweep) (`:16-18`).
  - Lists the entry points as modules: `harness.headless`, `run_cases`, `report` ("SOLE emitter of runs/ (W15, guardrail G7)"), `corpus_run`, `register --counts`, `delta HEAD` (`:20-27`).
  - Records the control defect: `delta` compares a committed `runs/results.json` against the working-tree copy and regenerates nothing, so `delta` alone prints `PROBE FLIPS 0` whatever changed; "quoted as a control in five commit messages" (`:29-32`). Rule: `report` BEFORE `delta`.
  - Claims `data/files.py` owns every path to a registry the package loads and that a bare grep for the dunder-file name is not the check (`:34-39`).
- **Conflicts / stale:** none in code (no code). The "`report` is the SOLE emitter" claim is a prose claim with no enforcing code here; `tests/test_season_shape.py` is the only candidate reader `[UNVERIFIED]`.
- **Open items:** none.

### engine/season/data/files.py
- **What it is:** the single path-anchor module for the package (269 lines); constants only plus four discovery functions.
- **Status:** none. Reading: live; the most-imported leaf (every loader reads a constant from it).
- **Bears on:** CORE.
- **Content that matters:**
  - Anchor is `DATA_DIR = Path(__file__).resolve().parent` (`:42`) with an import-time `assert` that `CLAUDE.md`, `engine/` exist and the package/engine dir names match (`:55-56`). It is the only module allowed to anchor on its own location.
  - Names the 13 registries this package reads: `write_matrix`, `rosters`, `verb_table`, `hole_register`, `requirements`, `ENDINGS_CLASSIFIED`, `governance_spine`, `offices`, `arrangements`, `cohorts`, `goals` YAML (`:98-130`), plus canon inputs outside the package: `systems/settlements/valoria_geography_v30.yaml` (`:147`), `references/module_contracts.yaml` (`:149`), `references/npc_registry.yaml` (`:158`), `CLAUDE.md` (`:150`).
  - Four discovery functions compute the source corpus rather than listing it: `loop_modules()`, `loop_source()`, `effects_modules()` (name starts `effects`), `decision_modules()`, `package_modules()` (`:183-269`). Each docstring warns a caller must pin a FLOOR or the scan passes by finding nothing.
  - Holds a pre-adoption results path `proposals/2026-09-01-season-loop-tests/runs/results.json` so `delta.py <old rev>` still resolves (`:84`).
  - Points at architecture docs as "doctrine read, never written": `ARCHITECTURE_V2_MD`, `ARCH_PLAN_MD`, `SOURCE_353_MD` (`:90-93`).
- **Conflicts / stale:** `DEGREE_SWEEP_DIR = engine/reference/degree-sweep` (`:136`) and `CLAUDE_MD`, `SOURCE_353_MD`, `ARCH_PLAN_MD`, `ARCHITECTURE_V2_MD` constants: whether anything reads them is [UNVERIFIED] (one grep would tell; `architecture/ARCHITECTURE_V2.md` and `architecture/PLAN.md` may be dead targets). `effects_modules()` docstring says "eight files today ... seven siblings" (`:207-222`); the real set under `loop/` is `effects.py` + `effects_shared.py` + 7 domain files = 9. Docstring also names six siblings elsewhere (`loop/effects.py:48`). Count drift of the kind F-CORE-19 files.
- **Open items:** the file comment says `names_index.yaml`'s constant was deleted as unread (`:159-163`) - an example of the project removing a declared-unread row; no equivalent sweep of the rest is recorded.

### engine/season/data/matrix.py
- **What it is:** the write-matrix loader and `Step`/`WriteClass` enums (276 lines), a "pure move" out of `shape.py` (decomposition step 2).
- **Status:** none. Reading: live; the gate's table.
- **Bears on:** CORE.
- **Content that matters:**
  - `Step` has seven members (CALENDAR, MATTER, DELIBERATE, RESOLVE, ENCOUNTER, WITNESS, CENSUS) (`:39-50`); `WriteClass` four (CALENDAR, MATTER, ACTS, INTERIOR) (`:53-57`). The step-to-class map `_STEP_CLASS` is a hand-written Python dict (`:67-80`) under a `roster-exempt: MECHANISM` comment; ENCOUNTER shares ACTS with RESOLVE (`:77`).
  - `_load_write_matrix` (`:144-189`) enforces: unknown keys rejected (loader invariant 10), `class:` column cross-checked against step-to-class derivation, duplicate `(kind, field)` is `SystemExit`. `MatrixRow` carries `kind, field, steps, social (True/False/None), by, emits, unproduced`.
  - `MATRIX` is read at import (`:193`); live count 42 rows, 6 `MATRIX_RETIRED` entries, `PARTITION_ASSUMED == {}` (measured by import).
  - `matrix_row` is the one lookup; a missing or retired cell raises `Unspecified` with law "S30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION" (`:249-265`). `partition_lookup(kind, field, thing="")` keeps a dead `thing` parameter "that carried the defect" for probe callers (`:268-276`).
  - `assume_partition_row` + `ASSUMPTIONS_USED` is a deliberately live channel so "zero assumed rows" is a measurement; read by `harness/report.py:260` and `tests/test_season_shape.py:34,1404-1414`. Nothing in the live engine calls `assume_partition_row` (grep: only the test) - it exists so a count of zero can be observed.
- **Conflicts / stale:** the `thing` parameter on `partition_lookup` is ignored (`:268-270`) - dead by its own admission; whether callers still pass it is [UNVERIFIED]. `MATRIX_RETIRED` is parsed from a second `load_yaml(WRITE_MATRIX_YAML.read_text())` (`:216-219`), i.e. the file is read and parsed twice at import.
- **Open items:** the `unproduced:` column on a `RES` row is checked "in data/verbs.py once the verb table exists" (`:126-132`); that check lives outside this file.

### engine/season/decision/questions.py
- **What it is:** person-side question assembly: `assemble`, `aggregate_questions`, `view_ids` (117 lines); moved from `decision.py` by unit L1 of the layer-1 conformance plan.
- **Status:** none. Reading: live; AX-2 island (no `World` import/name/attribute/string).
- **Bears on:** CHAR, CORE.
- **Content that matters:**
  - `assemble(p, question, k, rule="recent", questions=(), odds=None)` returns a `View(p.id, view_ids(...), k, question, questions, odds)`; `question is None` is a legal state (quiet season) and a wrong type raises `InstrumentDefect` (`:22-51`).
  - `aggregate_questions(qs, rule)` folds several questions into one under `QUESTION_AGGREGATION` (`first`, `all`, `one_per_source` named in prose); `all`/`one_per_source` WIDEN referents and classes by union rather than raising the question count, and mint id `q:agg:<rule>:<first id>` (`:54-85`). Open design register row `H-54` ("#353 says NOTHING about this").
  - `view_ids(p, q, k, rule)` bounds a View to K claim ids (`H-53`); rules in `rosters.yaml: view_builder_rules`: `recent` (default, "the incumbent", not argued for), `highest_confidence`, `question_relevant` (`:88-117`).
- **Conflicts / stale:** the `question_relevant` return expression (`:115-116`) is a conditional of two list sums where the first branch takes `rest[-(k - min(len(near), k)):]`; when `len(near) == k - 0`... if `k > len(near)` is true the rest slice is `rest[-(k-len(near)):]` which is correct, but when `k == len(near)` the conditional goes to the else branch (fine); when `k - len(near) == 0` impossible in the first branch. Reads correct; but `rest[-(0):]` would return the whole list if ever reached, so correctness relies on the guard `k > len(near)`. [UNVERIFIED by test].
- **Open items:** `H-53` and `H-54` are declared defaults the sweep compares; the file says neither is argued for.

### engine/season/goals.yaml
- **What it is:** world-gen content: authored goals of factions, bodies and seats (v9 IN-66 / FA-05 / FA-06; ED-IN-0293 (8), ED-FA-0039); 493 lines, 41 rows.
- **Status:** none (data file; header comments only). Reading: live, read by `data/goals.py` (the one loader) and `harness/populated.py::seed_goals`, which REFUSES a world seating a faction/body without a row (`build_realm(goals_complete=)` default on) (`:6-9`).
- **Bears on:** FA, CHAR, WR, CORE.
- **Content that matters:**
  - Row schema (`:14-36`): `id`, `org` (exactly one of faction/body/seat), `text`, `object.kind` in `goal_object_kinds` (person, seat_holders, rung, deed_doers, orientation), optional `stance` +/-1, REQUIRED `pursuits` (weights over the canonical fifteen), optional `derives {from, kind}` (acyclic, scope-restricted: body derives from own faction, seat from own body/faction), optional `axis` (no shipped row has one), `source`.
  - `goal_stages:` (CL-THRUST B2.2) is an optional top-level key; none is authored (`:38-50`). A stage's `predicate` is a typed-requires cell asking no world-only stem - person-side only.
  - "It only changes what a person attends to; it never acts, and nothing aggregates (A-31)" (`:11-12`).
  - Provenance quality: nearly every row's `source:` is "[ASSUMPTION; medium; Jordan to correct]"; FA-06's rows read `.designs/systems/factions/...` and `.designs/systems/world/...` "as intent and vocabulary only" (`:186-192`). Only Crown, Löwenritter, Riskbreakers, Inquisitors, Restoration (FA-05) quote the user (ED-IN-0293 rows 3-4, 2026-10-14) and Altonia's `goal_altonia_conquer_valoria` quotes "altonia generically wants to conquer valoria" (`:458`).
  - Rival goals are modelled as `seat_holders` with `stance: -1` toward the rival head's seat (Hafenmark vs `off_confessor`, Church vs `off_restoration_leader`, Restoration vs the Cardinal of Justice and Senior Inquisitor) - and the file itself declares the risk that a -1 `seat_holders` goal "makes those holders referents of a `need` question every season and `fight` forms on them, so violent attempts can rise" (`:178-181`, `:256-257`, `:323-324`).
  - Altonia's conquest goal has `object: rung r_valoria` with `stance: -1` that writes NO stance row (a `rung` object names no person), and the empire's march forms through a Katepano SEAT goal aimed at `set_s_001` Valorsplatz (`:451-483`); the chokepoint `set_s_007` has no Crown member present so a march there is `field.unopposed` (H-233) (`:480-481`).
  - Varfell rows reference `terr_T15`, `terr_T13` (territory rung ids) - a resolution into geography (`:341-351`).
  - Of the 41 rows, most are `orientation` (mints no Proposition; pursuits join the faction's expected vector, IN-69); only a minority mint an OUGHT proposition.
- **Conflicts / stale:** the Crown row records an unresolved source conflict (accommodation vs resistance to Altonia on axis 8, `:200-206`) resolved by authoring an orientation that "takes neither side". `goal_lions_table_coordination` header says the body "holds no seated member in build_realm(0) today" (`:423`) - a row for a body that is never seated in the default realm (dead until seated). `goal_guilds_*` have "no authored head". The seeding refusal (`goals_complete`) implies new factions need a row in the same commit.
- **Open items:** `axis:` and `goal_stages:` are carried by the schema and the loader and authored nowhere (no shipped row) - reachable-by-nothing schema surface, the CORE audit's "reachable by nothing" pattern; every pursuit weight is the author's assumption.

### engine/season/harness/__init__.py
- **What it is:** package docstring only (8 lines).
- **Status:** none. Reading: live, trivially.
- **Bears on:** CORE.
- **Content that matters:**
  - States the one-way dependency: `harness/` depends on `state/ loop/ decision/ seam/ trace_log`; none of those depend on it (`:1-8`). Says `shape.py` "was decomposed away at step 9".
- **Conflicts / stale:** the docstring uses `season.harness` (the pre-adoption dotted path). The same stale prefix appears in `harness/delta.py:10,19`.
- **Open items:** none.

### engine/season/harness/delta.py
- **What it is:** the before-and-after command (102 lines), guardrail G11; compares `git show <rev>:runs/results.json` with the working-tree copy.
- **Status:** none. Reading: live as a CLI; its own header says it "cannot fail" unless `report` is run first.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - MEASURES: counts of probes, gap events, trace counts, probe `by=` and `verdict` distributions, NPC and ARC case verdict counts, and a list of probe verdict flips (`:67-97`). Nothing about game outcomes.
  - CAN FAIL ONLY IF: the working-tree `results.json` was regenerated first. Otherwise `PROBE FLIPS 0` is true by construction (`:8-12`); the file says so in its own docstring (`:8-17`). The tool does not check the file's mtime or hash against a re-run, so it cannot detect the vacuous case itself.
  - It prints a verdict; it never exits non-zero. There is no `sys.exit(1)` on a flip - a flip is an informational line (`:94-98`). Only `at()` raises `SystemExit` (unreadable rev) (`:55`). So it cannot fail as a gate.
  - Reads the pre-adoption path as a fallback so old revs resolve (`:49`).
  - Only consumers found: `.github/workflows/valoria-ci.yml:411` comment (CI does not run it) and prose mentions in `decision_spread.py:76`, `requirements.yaml:522` (a batch quotes `PROBE FLIPS 0`).
- **Conflicts / stale:** both usage lines say `python -m season.harness.report && python -m season.harness.delta <rev>` (`:19`); the real invocation is `python -m engine.season.harness.report` (as `engine/season/__init__.py:25-27` says). A copy-paste of the header fails with `ModuleNotFoundError`.
- **Open items:** none; the vacuity hazard is documented rather than closed.

### engine/season/harness/exercises.py
- **What it is:** the `exercises:` overlay loader and token resolver (327 lines), plan item W10.
- **Status:** none. Reading: live; the only path from a case row to a verdict now that the regex router is gone.
- **Bears on:** CORE, ARCS.
- **Content that matters:**
  - Four token shapes, classified by form, never by a roster of words (`classify`, `:214-228`): `probe:<PID>`, `H-NN` hole (matched by `register.REG_ID_RE`), contains `.` -> Event kind, else verb.
  - Binding is by `need_sha` = first 12 hex of sha256 of the whitespace-normalised need (`:62-65`); a reworded corpus row orphans its annotation LOUDLY (`unbound`, `orphan_cases`) rather than silently re-annotating another (`:139-165`).
  - `resolve()` outcomes: probe -> PASS only if the probe's verdict is PASS; hole -> `absent` blocks, `assumption` is `ok=True, assumed=True` ("DEGRADED rather than PLAYABLE"), `ruled`/`measured` pass; kind -> satisfied when ANY `emits:` column of the verb table or write matrix declares it - "a static table lookup, NOT a run" (`:280-309`); verb -> executes iff `resolvable_verbs` contains it (both a `requires:` predicate and, if it writes, an effect) (`:310-327`).
  - The module's own admission: "25 of the 40 declared kinds are emitted by nothing" (`:41-42`, measured at the time of W10); W4 is named as the item that closes it. That count is a historical figure; the live count is not in the file.
  - Importing the module at top level is safe but the `if __name__` block sits in the MIDDLE of the file (`:187-201`) with the token-resolution code after it - the file is structured as import-time helpers, then a CLI main, then more library functions.
  - `need_terms` is "the one router-shaped operation left", output printed and never read back (`:92-105`).
- **Conflicts / stale:** the `kind` token `ok` means "declared", so a corpus row routed to a kind token passes on a table lookup (the file's own admission). Where this overlaps F-CORE-02 (the corpus checks no case need) it CONFIRMS that routing's weakest tokens pass on static declarations: kind tokens satisfy by declaration, hole tokens by register grade, verb tokens by "executable" not "executed". Only `probe:` tokens reach a run.
- **Open items:** W4 (make every MATTER write emit its declared kind so a run-level check has something to observe) is cited as the closer; the code here still performs the static lookup.

### engine/season/loop/__init__.py
- **What it is:** package docstring for `loop/` (47 lines).
- **Status:** none. Reading: live prose; two counts stale.
- **Bears on:** CORE.
- **Content that matters:**
  - Names the module layout: `driver`, seven step modules (`calendar matter deliberate resolve encounter witness census`), `predicates` (`REQUIRES_PREDICATES`), `effects` (`EFFECTS`), `sides` (`:3-8`).
  - The steps are BOUND ONTO `SeasonDriver` (`SeasonDriver.witness = witness`) rather than delegated to, because replacing a binding with a delegating stub keeps a pure NEGATIVE assertion test passing over a body it no longer reads (`:15-20`).
  - The token: `state/gate.py::Token`, constructed only in `driver.py::mint_token`; five of six steps take it first, `deliberate` gets none (`:28-31`).
  - `predicates` and `effects` may not import the driver (`:33-35`).
- **Conflicts / stale:** says importing `effects` "runs ELEVEN `@effect_for` registrations" (`:37-46`) while the live `EFFECTS` has 52 entries (measured by import) and `effects_*` domain files carry 53 decorator lines; the docstring itself records two previous count-from-memory errors, then repeats the pattern. "`REQUIRES_PREDICATES`: the four hand-written `requires:` cells" (`:6`) is not checked here. Same family as F-CORE-19.
- **Open items:** none.

### engine/season/loop/effects.py
- **What it is:** aggregator for the verb-keyed effects (102 lines) after the Phase-4 split into seven domain siblings.
- **Status:** none. Reading: live; code is 20 lines of imports, the rest is docstring.
- **Bears on:** CORE.
- **Content that matters:**
  - Imports `EFFECTS`, `_oblige_term`, `_operand`, `effect_for` from `effects_shared` and eagerly imports seven domain modules (governance, economy, migration, founding, information, combat, army) for decorator side effects (`:85-96`); re-exports `_eff_kill` and `_renewals` because tests reach them by this module's dotted path (`:101-102`).
  - The contract: an effect no longer mutates and reports; it DESCRIBES - returns a `state/gate.py::Change` naming subjects before anything moves, plus `apply`; the gate reads subjects before and after and mints a receipt for each that MOVED, raising `NoOpReceipt` if none moved (`:22-32`).
  - Rule: "an effect that declines returns `NO_CHANGE`" and the gate's no-op is the refusal (`:44-46`).
- **Conflicts / stale:** docstring says "the eleven `_eff_*`" and "all twelve" (`:4,35`) and "six sibling modules" (`:49`) while listing seven/eight; live `EFFECTS` = 52 (import), decorator lines: governance 10, information 20, combat 7, army 6, economy 5, founding 3, migration 2 (`grep -c`). The domain files are the owners of counts; the prose is wrong in four places.
- **Open items:** none.

### engine/season/loop/resolve.py
- **What it is:** the RESOLVE step: fold, contest dispatch, grade dispatch, scar/crisis writers, accumulator clamp (1299 lines; the one resolver, `04 §A.2`).
- **Status:** none. Reading: live; the single fold every act takes.
- **Bears on:** CORE, PC, MB, SC, FI, CHAR, WR.
- **Content that matters:**
  - `resolve()` (`:996-1200`) sets `w.step = RESOLVE`, canonical-orders all acts by (stratum, `H(world_seed, tick, actor, "order:<verb>:<act id>")`) (`_canonical_order`, `:51-58`), then per act: `_survives` (predecessor removed the actor -> `act.ineligible`), S27.4 refusal when `a.obstacle > multiple * pool`, then three routes: contest (`_contests_of`), graded inquiry (`GRADED_INQUIRIES`), or plain `_fold`.
  - S27.4 obstacle refusal reads `a.obstacle` which the comment says "defaults to None and the computed chooser never sets one" (`:1048-1056`) - the branch is unreachable in computed play and exercised by hand-built acts only.
  - `_admits` (`:187-313`) is the one owner of eligibility -> `requires` -> counterparty check, shared by `_fold` and the contest branch because the contest branch used to skip both (85 of 143 corpus cases became whole-case DESIGN-GAPs on the day `kill/wound` was admitted, 74 of them PARTY-GAP) (`:191-199`). Eligibility alternatives `own` (always true), `remit:<act>` (via `seat_hold`, the seat exercised), `hold:<object>`, `presence:<rung>` (declines every time: "unevaluable (H-33, the presence index)", `:142-156`). Note `own` returns True at the first alternative encountered - an `own` anywhere in the disjunction admits regardless of the others (`:103-104`).
  - `_contest` (`:766-874`) forks on the prize row's manifest `step:`: if the prize row declares a step other than the running one, fold at the row's `declares:` band writing nothing (the "Declared" deferral to ENCOUNTER); otherwise dispatch to the seam and fold at `degree_of(r, target, w.fixtures)`. `contest_max_depth` has NO DEFAULT and is a `Forbidden` if None (`:797-801`) (F-CORE-07 area).
  - The `_fold` write sequence (`:343-578`): act appended to the store (idempotent), `VERB_TABLE.get`, `_admits`, then `row.writes_at(degree)` pairs; the effect runs ONCE on the first pair (`:470-476`) and later pairs are gated check-only closures; `NoOpReceipt` converts to the row's WRITE_CLAUSE refusal; success Events are the `emits_at(degree)` kinds intersected with `earned` and filtered for `confidence.broken`; each kind's Event carries only the receipts of the subjects that earned it (CP-T03-00).
  - `_scar_witnesses` / `_conviction_crisis` (`:617-732`): the ACT writes `(Person, scar)` counts, one per observer per violated pursuit (or held affiliation), through the gate with the ACTS token, then `conviction_after_crisis` at threshold 3 writes `(Person, conviction)`. Nothing is emitted: "`scar.taken` is declared on the row and no reader consumes it" and "`conviction.moved` is declared on the row and no reader consumes it" (`:638-640`, `:707-708`) - two declared event kinds with no consumer.
  - The `_refuse_after_the_fact` pass replaces a staged `work`'s provisional success with the row's refusal when the summed site-condition clamp moved nothing (`:1242-1278`); `resolve` accumulates `(Site, condition)` deltas only and any other staged cell is an `InstrumentDefect` (`:1164-1170`).
  - Cumulative resolver-side state (`resolved`, `scenes`, `act_of`) is never reset across seasons because DELIBERATE at t+1 reads t's acts (`:1122-1128`), a stated hazard: "a session that makes these season-local ... blinds the propagation check silently".
- **Conflicts / stale:** `stratum_of` treats an act whose `stratum` equals the dataclass default (4) as "unset" and consults the verb row (`:1293-1298`), so an act that explicitly names stratum 4 against a verb row of a different stratum is read as unset - a conflation of default and explicit [UNVERIFIED by test]. `_eligible` handles `presence:` by always declining (`:154-156`): any verb whose ONLY eligibility alternative is `presence:` can never be eligible. `matrix_row(kind, fld)` is called "for its side effect only" (`:929`) - a pre-check that duplicates `World.write`'s own refusal, kept so `runs/TRACE.txt` bytes do not move. The doc comment `# THE TOKEN ... mint_token` sits in `driver.py`, not here. The comment at `:381-385` is an `[ASSUMPTION; medium; Jordan to correct]` that `VERB_TABLE` carries every verb the design names; revert recipe cites a commit by trailer, not hash.
- **Open items:** `GRADED_INQUIRIES` routing depends on `verb_capability` naming no inquiry for the obstacle default to hold (`:887-891`): "adding a row for one is the edit that must re-read this" - a latent coupling between `rosters.yaml` and this body.
