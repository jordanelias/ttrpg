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
- **Conflicts / stale:** the `question_relevant` return (`:115-116`) is a one-line conditional whose first arm slices `rest[-(k - min(len(near), k)):]`; that slice is `rest[-0:]` (the WHOLE list) if the arm were reached with `k == len(near)`, and it is kept correct only by the guard `if k > len(near)`. Correct as written, fragile to an edit; [UNVERIFIED by test].
- **Open items:** `H-53` and `H-54` are declared defaults the sweep compares; the file says neither is argued for.

### engine/season/goals.yaml
- **What it is:** world-gen content: authored goals of factions, bodies and seats (v9 IN-66 / FA-05 / FA-06; ED-IN-0293 (8), ED-FA-0039); 493 lines, 38 goal rows (24 of them `kind: orientation`, by grep).
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
  - 24 of the 38 rows are `orientation` (mints no Proposition; pursuits join the faction's expected vector, IN-69); the other 14 mint an OUGHT proposition.
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

### engine/season/manifest/__init__.py
- **What it is:** package docstring plus re-exports (40 lines) for the role-to-provider manifest; `04_CODE_ARCHITECTURE.md` §A.2's `manifest` module (unit L4, ED-IN-0206).
- **Status:** none. Reading: live.
- **Bears on:** CORE.
- **Content that matters:**
  - Consolidates three earlier copies of the role-to-provider rule into `manifest.check_roles()` (was inline in `World.boot`) and `manifest.resolve("contest", prize)` (was `seam/contest.py::contest_subsystem`); `engine/substrate/composition.py::ROLES` is explicitly NOT retired - the engine-wide registry one layer out (`:5-14`).
  - "Resolved at boot" is satisfied at `boot()` / `SeasonDriver.__init__` and not at import, so that readers of one name do not pay for `module_contracts.yaml` (`:15-21`).
  - `__all__` is computed from `globals()` by `__module__` prefix (`:37-40`).
- **Conflicts / stale:** "NO PROVIDER ROW IS LANDED HERE ... was interim `sigma_leverage`" (`:23-26`) is historical; `rosters.yaml` now names `social_contest` for three prizes (measured by import of `roster_map("contest_subsystems","prizes")`).
- **Open items:** none.

### engine/season/manifest/providers.py
- **What it is:** leaf module holding the `PROVIDERS` dict and the `@provider(role, module)` decorator (42 lines).
- **Status:** none. Reading: live; exists to break a real import cycle (`manifest.registry -> seam.wrappers.sigma -> manifest -> manifest.registry`), which took `test_import_cycle_game_state_npe.py` from 3 to 4 cycles (`:5-14`).
- **Bears on:** CORE.
- **Content that matters:**
  - `PROVIDERS: dict` keyed `(str(role), str(module))` to callable (`:34`); `provider()` overwrites silently on a repeated key (`:40`) - no duplicate refusal (contrast `registrar.register_module_entries`, which refuses double registration).
  - `has()` and `call()` are deliberately NOT here but in `registry.py` (`:23-26`).
- **Conflicts / stale:** `registry.py` still says `has()` "no longer imports anything"; but the providers dict is filled by import of `seam/` (`registry.py:107-112`), so an empty table is the failure mode if `seam` is never imported (documented in `seam/__init__.py` per the registrar docstring).
- **Open items:** none.

### engine/season/manifest/registrar.py
- **What it is:** the registrar (163 lines): resolves every `composition_roles:` row carrying `entry:` into the one table `MODULE_ENTRIES`, at driver construction (plan position 30, A-25, ED-IN-0284/0285).
- **Status:** none. Reading: live; `SeasonDriver.__init__` runs `register_module_entries` then `require_entries`.
- **Bears on:** CORE, SC, MB, PC, FI.
- **Content that matters:**
  - `register_module_entries(verb_table)` (`:77-129`) reads `engine.substrate.composition.ROLES`, resolves each target by string via `composition.require`, and REFUSES (a) a `verb:` naming no verb row, (b) one target under two roles, (c) one verb bound by two `verb_call` rows (`[ASSUMPTION, SM-5]`), and (d) a role the table already holds that no row now declares, or holds differently. Idempotent across the many drivers a corpus builds.
  - `require_entries(needs)` (`:132-163`): host-declared needs `((role, entry kind), ...)` from `queries/world_q.py::QUERY_ENTRIES` and `loop/matter.py::STEP_CALLS`; refuses a missing role or a role registered under another `entry:` kind.
  - `ModuleEntry` is a frozen dataclass of `role, entry, verb, target, fn`. The closed `entry:` set (`verb_call`, `step_call`, `query`) is owned by `tools/export_composition.py::_ENTRIES`, not here.
  - The registrar "writes nothing to EFFECTS or PROVIDERS"; `@effect_for` and `@provider` stay host (`:17-19`).
- **Conflicts / stale:** the docstring says "no production composition row carried `entry:` at `30`; `31a` landed the first (`social_contest.roll`)" (`:39-41`) - a history line; the live count of entry rows is not stated (`[UNVERIFIED]`, `composition.ROLES` entries with `entry`).
- **Open items:** the one-`verb_call`-per-verb rule is flagged `[ASSUMPTION, SM-5]` pending a ruling on whether a grid/map variant is its own module (`:105-107`).

### engine/season/manifest/registry.py
- **What it is:** role-to-provider resolution and the driver-construction refusals (716 lines, mostly docstring/history).
- **Status:** none. Reading: live; called by `World.boot` (`check_roles`) and `SeasonDriver.__init__` (the `check_*` family).
- **Bears on:** CORE, SC, FI, PC, MB.
- **Content that matters:**
  - `_ROLE_ROSTERS = {"contest": ("contest_subsystems","prizes"), "inquiry": ("inquiry_modules","findings")}` (`:38-39`): exactly two roles. Live rosters (import measurement): five contest prizes (`the body` -> combat/personal_combat/`combat.fight`, step ENCOUNTER; `a field` -> mass_battle, ENCOUNTER; `a standing`, `a proposition`, `a matter` -> social_contest/`social_contest.roll`, the last with `heard_by: bench`) and one inquiry row (`finding.made` -> fieldwork/`fieldwork.find`).
  - `resolve(role, key)` returns a dict `{module, resolver, doc, provider, step, declares, module_entry, heard_by}` or `None` for an unclaimed key (a real answer); it raises `Unspecified` if the named module is in no contract. `module_contracts.yaml` is parsed once per process (`_CONTRACTS_CACHE`, a bug-fix measured at ~170 s to over 600 s for the season suite, `:42-59`).
  - `check_rows()` (`:217-235`), `check_contest_prizes` (`:330`), `check_inquiry_modules` (`:410`), `check_graded_inquiries` (`:464`), `check_effects` (`:641`), `check_preconditions` (`:679`), `check_estimate_providers` (`:387`) each return the rows checked "so a caller can see the sweep was not empty".
  - `check_effects`/`check_preconditions` are two-sided: a writing verb with no effect needs an `effect_decline_note:`, and a row carrying a note AND an effect (or a `requires_decline_note:` with an evaluable precondition) is refused as stale. This is the construction-time guard that makes `resolvable_verbs()` unable to silently drop a verb.
  - Hard-coded in a body: `HEARD_BY_ROOMS = frozenset({BENCH})` (`:275-276`), `ESTIMATE_ROLE = "estimate"` (`:384`), `_VERB_CALL, _STEP_CALL` strings (`:515`). `_check_module_entry` derives the module from the composition row's `target` as the first package under its root (`parts[1]`), a string-position convention (`:590-591`).
- **Conflicts / stale:** the line numbers quoted in docstrings (`04:136`, `04:682`) cite a Layer-1 prose doc; they are references, not mechanisms. The module doc says `has()` "reads a table somebody else filled": fill happens by import of `seam/wrappers`, so `check_contest_prizes` before `import ..seam` would refuse every provider - an ordering dependency rather than a check.
- **Open items:** `_check_heard_by` supports one room; "A second room is a new reader in `seam/wrappers/sigma.py`, added with it" (`:272-273`).

### engine/season/npcs.yaml
- **What it is:** the authored NPC roster (445 lines, 46 rows), GENERATED by `tools/export_npc_roster.py --build` from `engine/season/cases/NPC*.yaml` and hand-editable afterwards.
- **Status:** none (header says re-`--build` overwrites hand edits; `--check` reports differences without failing, fails only on a row naming a nonexistent case/place). Reading: live; read by `harness/populated.py:95` (`ROSTER`) at world-gen and named in `references/ci_checks_registry.yaml:324-326`.
- **Bears on:** CHAR, FA, CORE, ARCS.
- **Content that matters:**
  - Row fields: `case`, `name`, `institution` (string or null), `home` (a building id from `venues.yaml`, e.g. `b_s_036_cathedral`), `want`, `concerns` (another NPC case id), `tie` in `named | institution | roof | neighbour` (`:18-25`). Measured by parse: 46 rows; `tie` counts neighbour 17, institution 15, named 12, roof 2; `institution` null for 18 rows.
  - `want` is NOT a desire of the person: it is the case's first `core` `season_requires` row, i.e. a DESIGN REQUIREMENT sentence in the form "A person ... must be able to ..." (e.g. NPC-088 `:36-38`, NPC-005 `:71-72`). The header says so: "`want` is its first `core` row of `season_requires`" (`:13-14`). So the engine's per-person "want" text is an engine capability requirement, not a character goal.
  - `concerns` is a graph over case ids chosen by a heuristic (`tie`), not by authored relationship: a `neighbour` tie means "placed in the same building/rung", `roof` the same roof, `institution` the same institution; only 12 rows are `named`. E.g. NPC-088 concerns NPC-004 (`institution`), NPC-075 Orm concerns NPC-012 (`neighbour`).
  - Header invariant: the `name`s and wants are the corpus's and are not authored here - "Inventing an NPC in this file would be exactly the fabrication ED-WR-0011 (OI-05) is filed as a ruling to avoid" (`:12-17`).
  - `institution` strings are a different vocabulary from `rosters.yaml`/`goals.yaml` faction names: `Crown`, `court`, `Altonian`, `Parliament`, `Guild`, `Church`, `Einhir` here versus `Valorsmark`, `Church of Solmund`, `Altonia`, `Guilds`, `Löwenritter` in `goals.yaml`. The mapping lives in `populated.py` (`institution_of` and `references/npc_registry.yaml: faction`); `populated.py:1881` records a falsy-roster-value hazard.
- **Conflicts / stale:** two cast heads coexist - `npcs.yaml` (placement, wants) and `references/npc_registry.yaml` (identity, convictions, role) - declared "disjoint fields" in `ci_checks_registry.yaml:326`. `institution: court` (4 rows) and `institution: Crown` (4 rows) look like one body split in two; `Parliament` and `Hafenmark` have one NPC each. Whether `court` resolves to a faction is `[UNVERIFIED]`. Cross-reference to F-CORE-23 (provided corpus loaded through a repair routine, one case gone) and F-CORE-02 (the corpus runs one template 143 times).
- **Open items:** `home` is a building that exists only through `venues.yaml`; a roster re-export could strand a guard at a stale rung (`cohorts.yaml:172` says so). Nothing in the file records which NPCs are on a player-facing arc, so it cannot answer the arcs charge by itself.

### engine/season/queries/__init__.py
- **What it is:** package docstring only (63 lines) for `queries/`.
- **Status:** none. Reading: live prose; accurate to the file list (`world_q`, `person_q`, `cache`, `faction_q`, `inputs`).
- **Bears on:** CORE, FA, CHAR.
- **Content that matters:**
  - "Nothing here owns state and nothing here writes"; no function in the package takes a write token (`:1-2, :28-31`). §A.2 enumerates four members; `inputs` is a fifth that holds records, not functions (the typed input records for module entries and the `Margin` output record) (`:21-24, :29-31`).
  - The person-side/world-side split is enforced by import: `person_q` imports neither `world_q` nor `faction_q`; `test_person_q_cannot_reach_the_world_side` holds that half (`:46-62`).
  - `faction_q` was added at plan position `20-ii` and `04 §A.2:132` was edited in the same commit "per the contradiction's own resolution"; the file argues this is not "a spec edited to match its implementation" because the spec was internally ambiguous (`:7-20, :33-40`).
  - The package `__init__` imports none of its submodules, deliberately (`:52-55`).
- **Conflicts / stale:** says `world_q` holds "the thirteen World-FIRST functions" (`:3`); the live `world_q` is far larger (not counted here). `readers.py` is described as "GONE" (`:42`).
- **Open items:** none.

### engine/season/queries/cache.py
- **What it is:** barrier-scoped indexes (130 lines): `presence_index`, `tenure_index`, `home_index`.
- **Status:** none. Reading: live; callers are `epistemic.observers_for`, `loop/witness` and `loop/resolve` (via `observers_for`).
- **Bears on:** CORE.
- **Content that matters:**
  - Three indexes: `presence_index(w)` -> `rung -> [person ids]` (key `"presence"`), `tenure_index(w)` -> `TenureIndex(holds: {subject: frozenset(objects)}, knots: frozenset((subject, object)))` over LIVE tenures (key `"tenures"`), `home_index(w)` -> `{person id: containing rung}` (key `"homes"`). All through `w.cache_at_barrier(key, build)` (`World.cache_at_barrier` at `state/world.py:1558`; `discard_caches` at `:1626`).
  - Validity is a convention, not a check: "AT A BARRIER ONLY IS THE WHOLE OF THE DISCIPLINE, AND IT IS NOT ENFORCED BY THIS MODULE" (`:16-24`). A direct caller that mutates tenures between two asks without `discard_caches()` gets a stale answer (`:51-55`). Four call sites of `discard_caches` (calendar, matter, resolve, witness) plus ENCOUNTER (`:43-44`).
  - The §A.2 row names a third index, "subtree aggregates", that "does not exist yet": `world_q.r1_aggregate` and `world_q.single_holder_counter` compute per call (`:26-29`).
  - `home_index` exists because WITNESS's co-location channel rebuilt the whole home map "80,000 builds in one season at `build_realm(0)`" (`:120-124`) - a measured figure in prose, not re-checked.
  - `presence_index` emits one `TRACE.query("presence","resolver")` per rung inside the build to keep `runs/TRACE.txt` byte-identical (`:113-116`).
- **Conflicts / stale:** the docstring says every barrier calls `discard_caches` first - "CALENDAR, ENCOUNTER, MATTER, RESOLVE and WITNESS" (`:43-44`) - while the earlier paragraph names four sites and omits ENCOUNTER (`:18-20`); the later list is the fuller one (CENSUS is not named in either). `"World"` is used as an annotation without an import (`:78`), harmless under `from __future__ import annotations`. Related to F-CORE-09 (per-access scans on the hot path) which cites cost on `w.tenures` scans.
- **Open items:** the subtree-aggregate index; the cache has no assertion that it is read at a barrier.

### engine/season/harness/invariants.py
- **What it is:** eight run-time predicates over a finished `World`, plus a census and a seed sweep (344 lines); the instrument for `tools/m1_acceptance.py` row 5 ("N seeds, zero invariant violations").
- **Status:** none. Reading: live; called by `tools/m1_acceptance.py:85,358-403`, `tests/valoria/test_season_invariant_sweep.py`, `harness/probes.py`, `harness/soak.py`.
- **Bears on:** CORE, WR, CHAR.
- **Content that matters:**
  - MEASURES eight structural properties, only those "NOT ENFORCED ON WRITE": `tenure_interval` (until >= since), `tenure_referent` (live tenure ends name an existing person/rung/office/proposition/site/record/date), `log_ids_unique`, `log_not_from_the_future`, `claim_not_from_the_future`, `body_in_range` (0..`condition_scale`), `stance_row_shape` (valence and weight within `STANCE_VALENCE_SCALE`), `office_singly_held` (`:41-50`, `:95-238`).
  - CANNOT SHOW: any game-outcome property (balance, narrative richness, whether anything of consequence happened, whether the world is playable). It tests data hygiene of a world after it was produced; a world in which nobody does anything passes all eight.
  - CAN FAIL: yes, in principle - it returns a violation list (`violations`, `:273-284`), `sweep` splits new from `DECLARED` (empty map, `:296`). It "REPORTS, DOES NOT RAISE" (`:27-29`); the caller decides. Its own history records over-firing twice (a missing `w.records` in `_entities` invented 136/176 violations; a deleted ninth predicate `ought_names_an_entity` criminalised the probe world's motive), so a clean result depends on predicate narrowness.
  - Anti-vacuity term `carrier_census` + `sweep()['unexercised']` (`:249-270`, `:308-339`): the `headless` world "contains 0 Offices and 0 stance rows" (measured 2026-09-15 per `:255`), so `office_singly_held` and `stance_row_shape` were vacuous there; the census exposes that but `unexercised` is informational - whether `m1_acceptance` fails on it is [UNVERIFIED] (see `m1_acceptance.py:358-403`).
  - `STANCE_VALENCE_SCALE` is imported from `data/cast.py` (single owner); `condition_scale` from `w.fixtures`.
- **Conflicts / stale:** `CHECKS = {name: globals()[name] ...}` (`:242`) couples the roster tuple to function names by string. `_all_tenures` is a one-line wrapper kept "because three predicates share it" (`:78-92`). `office_singly_held` asserts one holder per office, which is a design position (seats) rather than a conservation law; multi-seat bodies are modelled elsewhere, so it is consistent only if bodies are not `w.offices`. [UNVERIFIED]
- **Open items:** Row 5 of m1_acceptance names `hypothesis`; the file explains the repo has no such dependency and the sweep stands in (`:19-25`).

### engine/season/harness/register.py
- **What it is:** the hole-register object and its rules (R0-R3, G6, G8, G12, G13), citation verifier, `THE NINE` requirements checker, and a CLI (763 lines).
- **Status:** none. Reading: live; `--requirements` is a blocking CI job (`:26-28`), rule tests run in `engine/season/tests/test_season_shape.py` (`test_w0_*`, `test_w1_*`).
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Reads `engine/season/hole_register.yaml` (by import measurement: 352 rows; grades measured 167 / assumption 118 / absent 34 / ruled 33; tier 1 307, tier 0 45; kinds WIRING 67, RULING 56, NUMBER 52, MECHANISM 32, PRODUCER 29, SCHEMA_ROW 21, FORMULA 19, ABSENT_RULE 19, COLLISION 12, LOOP 5 ...). Max id H-362. `REG_ID_RE = r"H-\d{2,3}"` (`:123`) is the id shape's single owner (used by `exercises.classify`) and will reject a four-digit id at H-1000.
  - Rules: R0 shape (12 declared keys + optional `sign`), R1 grade in {ruled, measured, assumption, absent}, R2 an `assumption` needs a `site:` and 3 DISTINCT `sweep:` points, R3 an `absent` row carries no `default`, G6 an `absent` row needs a `cite:`, G8 every ARCHITECTURE_V2 Part B defect maps to a row or an existing section, G12 a `cite:` may not say "THIS ROW ... STAYS <other grade>", G13 LOOP rows carry `sign` + (for `+`) a non-`none` bound (`:34-60`, `:188-358`).
  - The register's own admissions: G13 "VALIDATES THE COLUMN'S SHAPE. IT DOES NOT MAKE IT A MECHANISM" and clause 3 is a PRESENCE check - `default: "TBD"` passes (`:315-344`, `:135-136`). The `sign` column has no resolver reader (`:96-100`). `H-106` (the derived loop check) is "unbuilt"; completeness of loop enumeration is "STILL ABSENT" (`:338-344`). This is the substance of F-CORE-21.
  - `check_requirements()` (`:631-701`), the checker for THE NINE: a row at `met` or `partial` must have non-empty `measured:` and a `measure:`; `-k` expressions must name at least one identifier occurring ANYWHERE in the concatenated `tests/` source alongside any `def test_` (`:670-673`: `("def test_" in src) and (n in src)` over the whole concatenated corpus, i.e. a name appearing in a comment or a different test satisfies it); a `python <path>` command must name an existing file with `__main__`. It exits 1 only on a malformed row. It never RUNS the `measure:` command and never checks `measured:` against output. Live statuses (parse): 9 rows - partial 5, met 3, not_met 1. Confirms F-CORE-03 (statuses are strings).
  - `verify_citations` checks `:NNN` line refs and quoted spans against `#353` (`architecture/holonic_ARCHITECTURE.md`), ARCHITECTURE_V2, PLAN, CLAUDE.md or named repo paths, falling back to `.designs/<path>`; a row may not be its own source (`:486-624`). It is a prose-provenance checker for a prose register.
- **Conflicts / stale:** `ARCHITECTURE_V2.md`, `PLAN.md`, `holonic_ARCHITECTURE.md` are all read by this module's rules (G8 parses `# PART B` headings, `:165-181`) - so a Layer-1 `.md` is an INPUT to a gate, which `CLAUDE.md` §0.05 cl.2 limits to `systems/**/*.md` only (these are `architecture/`, not `systems/`; not a violation by letter, but G8 makes a `.md`'s heading structure the head of a check). `--check` was documented as exiting 1 "TODAY, ON G6" (`:62-67`); G6 would pass if all `absent` rows carry cites - live status [UNVERIFIED, not run]. The docstring header says the register passed "99 rows during W10"; it is 352.
- **Open items:** `H-106` (derived loop-cycle check) unbuilt; G13 clause 3 is presence-only by choice.

### engine/season/harness/corpus_run.py
- **What it is:** the corpus RUNNER (1252 lines): builds one synthetic world per case in the 143-case NPC+ARC corpus, runs it N seasons, attributes executions from the Event log, and prints "the bar" (W18, `PLAN.md` Part 6); also holds the overlay readers `rescales()` and `cast_overlay()` over `cases/exercises/*.yaml`.
- **Status:** none. Reading: live as a CLI (`python -m engine.season.harness.corpus_run`); `build_at`, `attribute`, `attempts`, `graded_loss`, `degrees_by_verb`, `bands_that_differ`, `emits_and_writes_nothing`, `seating`, `CAST` are imported by other harness modules and tests.
- **Bears on:** CORE, ARCS, CHAR, FI, SC, PC.
- **Content that matters:**
  - WHAT `build_at(case, seed)` makes (`:467-662`): a containment chain down from the case's `scale:` (the `person` kind removed), one Site per producing kind in `SITE_YIELD`, THREE anonymous people `p_a p_b p_c` (or the case's `cast:` entries, `seat_ids`, up to 26), each with `seed_pursuits(seed, case id, pid)` (a hash draw), and one OUGHT Proposition per person whose subject is NEXT person in a rotation (`pids[(i+1) % len]`) with predicate `wants_of(case)` (the case's first `core` need) unless the cast entry authored an `ought:`. The file itself says the rotation is "the lesser of two wrongs" and that Q4 reads `prop.mood` and `prop.subject` ONLY, so the predicate "is behaviourally inert today" and the 443 to 638 act rise is attributable to the subject (`:580-631`). This confirms F-CORE-02 (the corpus runs one template 143 times): the world varies only by scale chain depth, cast size, authored office and capability, a `forced_by_threshold` Date, and a hash seed.
  - What varies per case (`:12-43`, `:460-464`): `temporal.span_seasons` (an integer for 57 of 143 cases, else `DEFAULT_SEASONS = 2`; clamped by `MAX_SEASONS = 6` "an INSTRUMENT BUDGET, not a rule of the game", `:70-73`), `ENDINGS_CLASSIFIED.yaml`'s `forced_by_threshold` (adds one Date due at tick 1 plus a docket item, `:656-661`), and overlay `scale:`/`office:`/`cast:` blocks. A case with a `scale:` outside `RUNG_KINDS` is `UNREPRESENTABLE` and refused rather than folded onto the nearest rung (`:947-949`).
  - Overlay discipline: every `scale:` re-authoring must carry `why:`, `office:` is validated by constructing a throwaway `Office` (the constructor is the validator), duplicates and unknown keys REFUSE at load (`SystemExit`), `knows:` on a cast entry is refused because it would be a sixth `Claim` construction site (AX-7), and a `capability:` key must be one `VERB_CAPABILITY` draws on (`:92-413`). `WAITS-ON-PLAYER` cast entries are reported and never seated (`:205-222`).
  - WHAT THE BAR MEASURES (`run_case`, `:944-1059`): R1 run completed, R3 "an Act by another person whose `causes[]` walks back to an act of a different person" (`_r3_propagates`, via an id-derivation index), R4 same-seed determinism (a second world, same seasons, `content_hash` equal, any exception counted as False, `:993-995`), R5 every fixture key read appears as a substring in the joined `site:` text of the hole register (`:1002`, `all(k in sites for k in read)` - a substring match against prose), A1 span status. Status vocabulary: HALTS, SPAN-UNAUTHORED, RUNS-UNDECLARED, RUNS-ALONE-UNDECLARED, NO-EXECUTION, UNREPRESENTABLE, INSTRUMENT-DEFECT, DESIGN-GAP.
  - WHAT IT CANNOT SHOW: the headline `RUNS`/`ENDS` is permanently `NOT-COMPUTABLE` (R2/A2/A3 need W10-core, W23, W26, W27, W30), printed as such because `st.get(headline, 0)` had returned a constant 0 and been quoted as a measurement in PR #368 (`:1223-1231`). So no corpus case can be reported as satisfying its own need; "executed" means an Event of the verb's `emits:` kind is in the log for an act that folded (`attribute`, `:758-795`).
  - CAN IT FAIL: yes, per check (R1/R4/R5 per case; INSTRUMENT-DEFECT vs DESIGN-GAP split on exception class, `:962-971`). `planted_control` (`:1062-1086`) plants a cross-person edge and asserts R3 flips False to True - a real control for R3's detector only. There is no control for R4 or R5.
  - Attribution (`:798-814`): act-to-Event by the fold's own id scheme `H(seed, tick, actor, "<kind>:<act id>")` over `range(n+1)` ticks; `attempts` reads the act store (every act entering RESOLVE), `attribute` the fold set (`driver.resolved`), because over the act store an admission refusal whose kind is also an `emits:` kind (`finding.none`) reads as made ("examine 0 -> 85 worlds executing" per `:973-977`). `graded_loss` separates a lost roll from a refusal by `Event.degree == "Failure"`.
  - Ranking-discrimination readout (`main`, `:1108-1141`): counts candidates with a nonzero pursuit score among those whose verb has a celled axis; ties are "broken BY THE DRAW (U4/H-96)", not alphabetically (the earlier comment said alphabetical).
- **Conflicts / stale:** the long comment at `:1101-1105` says ties break alphabetically by verb name while the printed line at `:1139` says "BY THE DRAW (U4/H-96)" - one of the two is stale (the code path is in `decision/choose.py`, not read here). `run_case` builds TWO worlds per case and runs both (`:951-995`), so the corpus costs 2x for the R4 control. `NOT_COMPUTABLE` (`:678-682`) cites plan items (W10-core, W23, W26, W27, W30) by id; whether those are done is [UNVERIFIED]. `README`-level counts ("143 cases", "57 of 143", "47 of 57 unrepresentable", "27 of 46 NPC cases are CHAIN-sourced", "up to 16 span_seasons") are in prose and were not re-counted. Related finds: F-CORE-02, F-CORE-22 (the controlled-comparison instrument cannot tell a null from a fake control), F-CORE-23 (corpus loaded through a repair routine).
- **Open items:** the PLAN's `W29` (lift the 6-season clamp) and `W27` (per-case cast ported into `build_at`, "item 2 of workplans/2026-09-13-work-order.md") are named and unscheduled in this file; `populated.py` is "a second instrument beside [corpus_run], not a replacement" (`:626-630`).
