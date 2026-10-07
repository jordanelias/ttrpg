# Valoria — Master Workplan v9, part 4: IN lane I — B-A, B-B, B-C, B-E and B-L (adoption, close-30, instruments and records, the telling tail, the module stages §SM), the re-plug and mode designs

## Status: part of v9 — see `workplans/valoria_master_workplan_v9.md`
## Reads after `workplans/valoria_master_workplan_v9_part3.md`; IN lane II (IN-08..13, 21–23, 25–28, 30–38, 40, 45, 48, 49, 51) is `_part5`.
## Grade under `CLAUDE.md` §0.2: `paper`. Line numbers drift; re-derive every site by its symbol before editing it.

---

## 4.0 How to read this part

- **Home of** IN-02..07, 14..20, 24, 29, 39, 41..43, 46, 47, 50; each full entry lives here once. Aliases resolve here: `PC-09` = IN-04 (`31b`), `MB-09` = IN-05 (`31c`), `SE-02` = IN-07 (`36`), `GO-02` = IN-42, `SM-6` = IN-46. IN-06 (`33`) is the design half of `FI-05` and `WR-05`; their build halves (IN-32, IN-35) are `_part5`'s.
- **Entry fields.** `STATE` (`B` buildable · `BLK:<ids>` · `J:<id>` · `ask-then:<id>`) · `LANE` · `BATCH` (`_part3` §B: B-A … B-Z; a late position is slotted by §B.0's rules R1–R9) · `R` (THE NINE rows moved, `_part2`) · `WHAT` · `DEPS` (D data · F file-collision · I instrument · J Jordan-gate · R ordering-by-ruling; `_part3` §A) · `EDITS` (`_part3`'s collision matrix) · `EXIT` · `FALSIFIER` · `SOURCE`.
- **A design position** (IN-06, IN-07, IN-46, IN-47) writes its design as a PROPOSED document under `proposals/` (never `.designs/` or `systems/`, `CLAUDE.md` §1, §3; the precedent is WR-04, `_part7`) and builds nothing. A design that has a build position (IN-06 → B-S, IN-07 → B-T) is built there; IN-46 and IN-47 have none until their designs are reviewed (their entries say what the review adds).
- **Carried blocks** follow the line that names their source lines, and are the source's words. The only edits: a citation of a retired plan file re-pointed to its v9 handle or its `FORK:` ref; a spent clause or closed row deleted; v8 position numbers kept as aliases. The source files retire at adoption (ED-IN-0286): `v8_part5.md:L` and `telling:L` (`workplans/2026-10-01-telling-workplan.md`) read at that `FORK:` ref.
- **Prose is reference (`CLAUDE.md` §0.05).** No entry is the reason a behaviour is correct; each names the instrument that shows it. A figure here carries the command that re-derives it and the date it was read; re-run before relying on it.

## 4.1 B-A — ADOPT

Members, entry gate and exit instrument: `_part3` §B. B-A is the adoption patch (`_part8` §K). The one-line CI fix that had left `main` red (`personal_combat` joining `RETIRED_CONTRACTS`, `tests/valoria/test_flow_skeletons.py`) is built — `7b619328` on the adoption branch, 95 passed — so it is not a position here (`CLAUDE.md` §2: finished positions leave the plan); `main` reads green once the branch merges.

## 4.2 B-B and B-C — CLOSE-30 and INSTRUMENTS + RECORDS

Members, order, lanes, entry gate and exit instrument of both: `_part3` §B (the one copy of the batch table). Both open after B-X (closed at `1438d44`); they run in parallel sessions, and B-C merges after B-B where the two share `references/module_contracts.yaml` and the `rosters.yaml` comments (IN-02's fixes against IN-42's row and IN-43's comments).

**B-B — DRIVER + CLOSE-30** (IN-02 → IN-41 → IN-29 → IN-14; one session, the full suites once at its head). Hash movers declared at the batch exit: IN-29 (a mover wherever a date fires), IN-14 if the budget moves, IN-02 only if a Phase 2–3 fix moves a control hash, and any PC/MB lane whose own EXIT declares one. The pre-change `build_realm(0)` hashes are re-read on the batch's base commit before the first edit (§4.3's control).

### IN-02 · `30` · the registrar, the `modules:` roster and the refusals — BATCH-CLOSE Phases 2–3 and the full suites
- STATE: B      LANE: IN      BATCH: B-B (head)      R: —
- WHAT: `30` is built (#456, `5097e49`); its BATCH-CLOSE Phases 2–3 and the full suites did not run, at Jordan's instruction (`registers/handoffs/HANDOFF_IN.md`, the row beginning "Modules plan: `34` (dice engine) and `35` (scan roots) LANDED"). Run them; fix only what they find. The build's WHERE (items 1–5) is its record at `5097e49` (spec `v8_part5.md:172-222`); the close checks the falsifiers, carried below as its checklist. **Hash:** unchanged by intent (falsifier (1)); a fix that moves either control hash is a declared mover, with the pre-change reading, in its commit.
- DEPS: IN-02 → IN-03 (R: E17 — each module stage waits on the previous stage's falsifiers OBSERVED; IN-03 is B-L, after B-K); IN-02 → IN-41 (D)      EDITS: fixes only — `rosters.yaml`, `loop/driver.py`, `module_contracts.yaml` + `composition.json`, `manifest/`, shape pins
- EXIT: falsifiers (1) and (3)–(8) below, each in a fresh subprocess; `python tools/export_composition.py --check`; the full suites once at the batch head (`tests/valoria -n auto`, `engine/season/tests`, `engine/tests`). Falsifier (2) is NOT in this exit: it cannot fire in a fresh process until some row is declared required, so it is observed at IN-03 (its falsifier 3), in B-L; through B-G..B-K the "no row declares" refusal is observed in-process only, and IN-08's EXIT (`_part5`) observes refusals (4) and (5) on the rows it adds, in a fresh subprocess      FALSIFIER: the close is wrong if any of (1), (3)–(8) reds in a fresh subprocess, if `export_composition --check` reports drift, or if a suite reds in a file `30` touched; a Phase 2–3 fix that changes a refusal re-runs that refusal's planted-violation test, and a close that reports (2) green has run it in-process only
- SOURCE: `registers/handoffs/HANDOFF_IN.md`, the row beginning "Modules plan: `34` (dice engine) and `35` (scan roots) LANDED"; `engine/season/manifest/registry.py`; carried below, `v8_part5.md:223-235`:

**Re-pointed in the same commit.** `tests/valoria/test_season_providers_are_registered.py`: the first test also
asserts every provider a prize row names (this adds `mass_battle`); its `_MUTATION` arm (`:51-93`) also clears
`MODULE_ENTRIES`. A covering test with one planted violation per refusal, each in a subprocess.
**FALSIFIERS** (each in a fresh subprocess). (1) Both hashes unchanged; `resolvable_verbs()` the same set.
(2) Delete a planted composition row → driver construction refuses naming it. (3) Clear a prize row's provider →
refuses naming the prize. (4) A verb whose `contests:` no row claims → refuses naming the verb. (5) Clear the
effect of a writing row with no `decline_note:` → refuses naming the verb. (6) One entry registered twice →
refuses. (7) `SeasonDriver(build_realm(0))` constructs. (8) `export_composition --check` OK and
`test_importing_every_engine_module_pulls_in_no_subsystem` green (the registrar resolves by string at driver
construction, never at import).
⚠ **`ID-13`, read exactly.** `30` declares no production composition role — its covering test plants one — so the
registrar's pass over production rows is first exercised at `31a`. The commit says so; `30`'s done-claim is the
refusals running at every driver construction.

### IN-41 · SM-11 + SM-9 · the precondition twin of refusal (a); the `decline_note:` split
- STATE: BLK:IN-02      LANE: IN      BATCH: B-B (after IN-02)      R: —
- WHAT: SM-11 — a declared-absence column, then a refusal at driver construction, for a verb whose untyped precondition nothing evaluates (today `resolvable_verbs()` drops it without a word: the `gated` test, `loop/driver.py:125-127`). SM-9 — split `decline_note:`, which declines an effect on some rows and a formation on others (`oblige`, `destroy_record`), so `30`'s refusal (a) gains its converse arm. Both rows are in §4.5's SM table.
- DEPS: IN-02 → IN-41 (D: extends `30`'s refusals)      EDITS: `loop/driver.py`, `manifest/`, `data/verbs.py`
- EXIT: in a fresh subprocess `SeasonDriver(build_realm(0))` constructs on the shipped tree, and `resolvable_verbs()` returns the same set (compare the two sets; write no number)      FALSIFIER: (1) a planted row with an untyped precondition and no declared absence refuses naming the verb; (2) a planted row with an effect and an effect-declining note refuses; `oblige` and `destroy_record`, whose notes decline formation, construct
- SOURCE: `v8_part5.md:207-210, :375, :377`; `engine/season/loop/driver.py:125-128`

### IN-29 · H-110's successor · CALENDAR's own Events reach `witness()` at barrier 4
- STATE: B      LANE: IN      BATCH: B-B (after IN-41)      R: R-03 (must stay met)
- WHAT: `date_due` and `band_crossed` were folded into `claim_landed` at position `11a`, and H-110 closes DISSOLVED (IN-43's table). What is still open: `season()` calls `self.calendar(...)` and discards its return (`loop/driver.py:423`), and barrier 4 hands `witness()` only `pending_matter + events` (`:481`), so the `date.fired` Event that `11b` made CALENDAR emit lands in `w.log` and in no ledger. Route CALENDAR's own Events into the barrier-4 fan-out beside MATTER's. **A hash mover** wherever a date fires, declared at B-B's exit. **Scope:** CALENDAR's own Events reaching `witness()` and nothing else. `open_case` filling a fired slot so that `convene` has a date (`loop/effects_information.py:199-201`: `convene`'s dates fire VACANT in every computed world) is a step of SC-01 (`_part6`, B-N), not this position's; it takes an IN-29 → SC-01 edge.
- DEPS: IN-29 → SC-01 (D: the fired-slot → `convene` step builds on the routed `date.fired` Events; the edge is `_part3` §A's) [ASSUMPTION: the edge's reason; the edge itself is `_part3` §A's]      EDITS: `loop/driver.py`, `loop/calendar.py` (its return), `engine/season/tests/test_season_shape.py` (the re-pin below)
- EXIT: `python -m pytest engine/season/tests/test_season_shape.py -q -k calendar_a_forced_corpus_date` with its last clause re-pinned from `not claimed_any` to `claimed_any`: over the `forced_by_threshold` corpus worlds, CALENDAR `date.fired` Events reach `witness()` and at least one ledger claim references one; `python -m pytest engine/season/tests -k test_u2_ -q` green      FALSIFIER: today the same test passes on `assert not claimed_any` (the "0 of 0" pin, read 2026-10-06) and turns red at the change unless re-pinned; read the pre-change `build_realm(0)` one-season hash on the base commit (§4.3's control, `05f022e2…` at `52ec9a54`) and declare the post-change hash beside it in the commit
- SOURCE: `engine/season/loop/driver.py:423, :476-481`; `engine/season/queries/world_q.py:1355-1369`; `engine/season/rosters.yaml:534-543`; `engine/season/tests/test_season_shape.py:4486-4551`; `proposals/2026-09-17-governance-and-holdings-r2/01_ATTENTION_AND_REACH.md:977-979`

### IN-14 · BOUND-ATTENTION (H-92, H-10) · `budget()` counts `granted_acts`
- STATE: B      LANE: IN      BATCH: B-B (last: pins)      R: —
- WHAT: re-measure the 2026-09-24 re-plan — `budget()` counts `t.granted_acts`, not every live `hold` — against the T4 tree, then land it if `test_n3`'s floors hold; T4 found the floor a PROPERTY, not a golden. #457: "needs H-92's records-mint-budget repair first".
- DEPS: shape pins only      EDITS: `engine/season/decision/budget.py`, shape pins
- EXIT: `python -m pytest engine/season/tests/test_season_shape.py -q -k test_n3` green with its floors unchanged; `build_realm(0)` hashes declared if they move (a hash mover if the budget moves: B-B's exit declares it)      FALSIFIER: one live `hold` moves releasable scenes by one, control is today (#457 `:166`); a landholding with no granted act buys no scene
- SOURCE: `registers/handoffs/HANDOFF_IN.md`, the row beginning "Build-order item 4 REVERTED"; `engine/season/hole_register.yaml:166` (H-10), `:1142-1147` (H-92); `engine/season/decision/budget.py:18`; `engine/season/tests/test_season_shape.py:8645, :8789`

**B-C — INSTRUMENTS + RECORDS** (IN-19, whose baseline is read on B-X's closing commit `1438d44` before any other B-C lane lands → IN-20, IN-24, IN-39 → IN-43 → IN-50, IN-42; the lanes {FI-04} {WR-04} {GO-03}; the designs IN-06, IN-07, IN-46, IN-47). B-C's members edit no `loop/`, `decision/` or `state/` file, so no count pin and no hash moves; a loop-side repair out of IN-50 slots to the batch its files name. Its HANDOFF line names IN-50's diagnosis (the case, the cause, the batch its repair slots to) and where each design landed.

### IN-19 · STORY-BAR · the M2 instrument
- STATE: B      LANE: IN      BATCH: B-C (head)      R: — (M2)
- WHAT: per #457, "the M2 instrument: cross-person antecedent share and chain-depth distribution per season, N seeds, forcing on against off" — a module under `engine/season/harness/`. M2 has no instrument until this lands.
- DEPS: IN-19 → IN-23, IN-37 (D: the reader first, ID-13; both B-U); IN-19 → IN-21/34 (B-F), IN-35 (B-S), IN-36 (B-V) (I: its forcing-off arm is each forcing position's control); M2: IN-19 → SC-01 step 16 → IN-37 → IN-27 (B-U)      EDITS: `harness/`
- EXIT: the new harness over N seeds on B-X's closing commit `1438d44` (the tree before any other B-C lane lands) reproduces #457's baseline (`:168`, from its §8); the command and its printed reading go in the commit body      FALSIFIER: a planted severed antecedent edge drops the cross-person share; forcing off, the two arms read equal
- SOURCE: `proposals/2026-10-04-forcing-churn-and-the-story-bar.md:168, :196`

### IN-20 · STORY-SOAK · `soak.py` grades
- STATE: B      LANE: IN      BATCH: B-C      R: —
- WHAT: per #457, `harness/soak.py` "exists and grades nothing; add flat cost per season and non-convergence of the act mix" — ID-16's "season 40 resembles season 30" is untested. Every argument stays caller-supplied (its docstring: `ci_sim_fabrication_check` scope).
- DEPS: none (shares the `harness/` directory with IN-19 and IN-24, not a file)      EDITS: `harness/soak.py`
- EXIT: `python -m engine.season.harness.soak --seed S --arm ARM --batches B --seasons-per-batch N --season-wall-ceiling SECONDS --out DIR` prints a per-season cost grade and an act-mix convergence grade      FALSIFIER: a planted per-season cost growth fails the cost grade; a planted single-act mix fails the convergence grade
- SOURCE: `proposals/2026-10-04-forcing-churn-and-the-story-bar.md:170`; `engine/season/harness/soak.py:1-14`

### IN-24 · BOUND-LOOPS (H-106; H-25 merged) · the derived cycle check
- STATE: B      LANE: IN      BATCH: B-C      R: —
- WHAT: per #457, "a signed LOOP row with a bound for every new amplifier; build H-106's derived check, which no plan position schedules". The declared half is the `kind: LOOP` rows of `hole_register.yaml` (H-106's `hole:`); the derived half is computed from the `requires` grammar. H-25 (loop termination) folds here.
- DEPS: none on the graph      EDITS: `harness/` (an instrument)
- EXIT: the instrument prints derived == declared on the shipped tree      FALSIFIER: (1) a planted amplifier with no LOOP row makes derived ≠ declared, naming it; (2) the ratchet (#457 §3 row 3, "Church to theocracy", whose left-unplanned item is "bounded escalation loops", `:83`) is observed rather than assumed: for each LOOP row the instrument prints the declared bound beside the largest value of the looped quantity over N seeded seasons, and a value above its bound fails. The ratchet's amplifier is built by IN-10/IN-12 (B-I onward), so (2) observes nothing on the shipped tree and is first read at the batch that builds the amplifier [ASSUMPTION: the observed quantity and where it is read; #457 names the loop and not the instrument]
- SOURCE: `proposals/2026-10-04-forcing-churn-and-the-story-bar.md:83, :164`; `engine/season/hole_register.yaml:1486-1492` (H-106), `:262` (H-25)

### IN-39 · P-4, P-6 · the two pre-flight checks still open
- STATE: B      LANE: IN      BATCH: B-C      R: R-01 (P-4 before the first `11` re-take, the control at B-G's close), R-04 (P-6 feeds its table)
- WHAT: run `_part3` §P's P-4 (`11-fix`'s determinism attack) and P-6 (the `questions_for` referents offered a seated person in one `corpus_run` case against `build_realm(0)`, H-175); record outputs in the first receipt that needs them. Builds nothing.
- DEPS: IN-39 → the `11` re-takes (R-01; `_part3` O.2 E15: B-G as the control, B-I, B-M)      EDITS: none
- EXIT: P-4, the same cell twice: `cd proposals/2026-09-04-degree-sweep && python wd_chunk.py none default 0 36`, run two times      FALSIFIER: `probed` differs between the two runs of one arm → a determinism defect: stop and register
- SOURCE: `_part3` §P (carried from v8 `_part3` at its `FORK:` ref); `engine/season/hole_register.yaml:3767` (H-175)

### IN-43 · housekeeping · stale rows, stale comments, a blind selector, the hole-register closures, the `mc_v18` mention sweep, the `blocks:` re-point, the failing-case print
- STATE: B      LANE: IN (all)      BATCH: B-C (after IN-19: both edit `harness/corpus_run.py`)      R: R-01, R-09
- WHAT: (1) `mechanics_index.yaml:907` (`domain_echo`; the `module_contracts.yaml` half went with B-X's extraction, `1438d44`); `requirements.yaml:183`; the `rosters.yaml` THE SEAMS comments (`:991`); `mechanics_index.yaml` rows with `sim_module: null` that keep `test_status: validated_*`; `tools/build_fork.py`, which cannot run since the deletions [UNVERIFIED]. (2) R-09's `measure:` (`requirements.yaml:1173`), a THE NINE row's instrument: a selector-only record edit, its `met =` threshold untouched. `u1_` matches no test name (`:1146-1149`; no `def test_u1_` under `engine/season/tests`, read 2026-10-06), so the `-k` becomes the node id it actually runs, `engine/season/tests/test_season_shape.py::test_we_only_a_verb_that_declares_contests_can_be_graded_today` (`:12962`, which carries the margin-producer scan); the `headless` half stays. (3) The hole-register closures in the table below — Layer 2 edits made by this position, not by the adoption commit, because `harness/run_cases.py:341-343` reads the register. Each closed row is re-graded on the register's own precedent (`ruled` where a ruling or a producer closed it, `measured` where a measurement did, `assumption` where an assumption stands) with a `cite:` reading `CLOSED BY IN-43 …` and the evidence named here. (4) Handoff rows and the retired-plan cites in handoffs ride B-A's adoption commit; IN-43 re-checks them.

  Four sub-items. **(i) The `mc_v18` mention sweep.** Jordan, 2026-09-27 (events `968800e2`, `290477d7`): *"we need to move beyond any mention or use of this mc_v18. that is critical."* The sweep's scope is the MENTIONS. `engine/mc_v18.py` and the importer ratchet `tests/valoria/test_mc_v18_is_deprecated.py` are both deleted (`FORK:5c5d8ec6`, `references/restructure_ledger.md:2651-2652`, read 2026-10-06), so there is no importer to leave alone and no roster to shrink; `CLAUDE.md` §0.2's "deprecated in place" paragraph still describes the ratchet, and that is Layer 0 — IN-44's list (`_part8`), not this sweep's. The measure is the command `_part8` §E already uses, `git grep -l mc_v18 -- ':!.audit' ':!.designs' ':!registers/archive' ':!references/restructure_ledger.md' ':!CLAUDE_RATIONALE.md'`: it lists **147** tracked files, re-measured 2026-10-06 at `7b619328` and identical to the 2026-10-01 reading (60 of them sit outside `proposals/`, `research/` and the v8 workplans, which retire at B-A). Each live mention is rewritten to what is true now (the driver was deleted at `28-iii`; its successor is `loop/driver.py::SeasonDriver.season`) or deleted where it only narrated the driver; a frozen record (`registers/archive/`, ledger rows) is never edited, and a provenance string that names `mc_v18` as the source of a fact still live is read before it is changed. Commits go by directory: live code, tests and tools first, then `registers/`, then `proposals/` and `research/` [ASSUMPTION: the order]. No guard is built for it (`CLAUDE.md` §0.1 pt 5: its subject is this repository's process).
  **(ii) The `blocks:` re-point**, a record edit to `engine/season/requirements.yaml`. Each THE NINE row carries a `blocks:` list of ids from retired plans: R-01 `:377` `[W-F, H-111, H-116]`, R-02 `:505` `[W-F, H-111]`, R-03 `:595` `[W17]`, R-04 `:685` `[W10, W13]`, R-05 `:831` `[W10-core, H-65, H-94]`, R-06 `:978` `[W27, H-62]`, R-07 `:1031` `[W-F, W27]`, R-08 `:1076` `[W26, H-62]`, R-09 `:1174` `[W23, H-98]` (read 2026-10-06). Each id is re-pointed to the v9 handle `_part2` names for it, or marked spent; `W-F` is "outcome → `Person.stance` (`H-62`)" (`proposals/2026-09-04-degree-sweep/EXECUTION_PLAN.md:87`), superseded by A-12 and IN-18 G1 (`_part5` §A). No code reads the key (a search of `engine/season/harness/`, `tools/` and `tests/` for `blocks` as a key finds none, 2026-10-06), so it is a reference edit, and every `measure:` line is untouched.
  **(iii) H-52 closes as "assumption stands"** (G-2) [medium; Jordan to correct] — the table's row. **(iv) `corpus_run` prints the failing ARC case:** `main()` prints `check R3: <n> of <m> pass` per lane (`harness/corpus_run.py:1041-1044`) and not which case failed (R-01's `measured:` says so, `requirements.yaml:369-370`); the print adds the ids of the cases whose `R3` is not `True`. A print only; P-4 stays IN-39's, and the diagnosis and repair of the case it names are IN-50's.
- DEPS: IN-19 → IN-43 (F: `harness/corpus_run.py`, the baseline first); IN-43 → IN-50 (D: the printed case id); IN-43 → IN-42 (F: `references/module_contracts.yaml`; B-C merges after B-B where they share it and the `rosters.yaml:991` comment)      EDITS: the comments and rows above; `engine/season/requirements.yaml:1173` and the nine `blocks:` lines; `engine/season/hole_register.yaml` (the rows below); `engine/season/harness/probes.py` (A14, H-56's row); `engine/season/harness/corpus_run.py` (a print); the files the sweep names
- EXIT: `python -m engine.season.harness.register --check` (no new failure) and `--counts` read before and after (the `absent` count falls by the closed rows only); `python -m engine.season.harness.register --requirements` exit 0; `python tools/currency_consistency_check.py`; `python -m pytest tests/valoria/test_tool_input_paths_resolve.py tests/valoria/test_ledger_hygiene.py -q`; the sweep's `git grep -l` command before and after, its residue naming only Layer-0 files and files kept with a reason in the commit body; `python -m engine.season.harness.corpus_run` (about 2.5 minutes) prints the id of every case whose `R3` fails      FALSIFIER: `python -m pytest <R-09's new node id> --collect-only -q` lists exactly that one test (a selector that matches nothing reds it); every closed row's `cite:` names evidence that opens to what the table says; probe A14 no longer raises `Collision`; `git grep -n "workplans/2026-09-\|_v8" registers/handoffs/` names no live owner; `tools/build_fork.py` runs, or retires with a `FORK:` row; the printed ids are exactly the cases behind the ARC `96 of 97` (read 2026-10-02 at `444a00e1`; re-run), and the planted control still flips `R3` False → True; no id in a `blocks:` list names a plan file that no longer exists
- SOURCE: `registers/mechanics_index.yaml:905-909`; `engine/season/requirements.yaml:179-186, :1140-1149, :1173`; `engine/season/rosters.yaml:991`; `engine/season/harness/run_cases.py:341-343`; `engine/season/harness/corpus_run.py:1041-1044`; `engine/season/hole_register.yaml:44-55` (grading rules); `references/restructure_ledger.md:2651-2652`; `registers/handoffs/HANDOFF_IN.md`, the row beginning "Plan v8 Batch 1, Batch A and Batch B — LANDED"

IN-43's hole-register closures (evidence read 2026-10-06; re-open each before editing the row):

| row | disposition | evidence |
|---|---|---|
| H-45 | CLOSED: the six investigation acts are named rows, each with a real `requires` and a `finding.none` refusal (ED-FI-0009, 2026-09-10) | `engine/season/verb_table.yaml:95-96` |
| H-46 | CLOSED as framed: the 13-axes basis is replaced by fifteen pursuits over seven axes (ED-IN-0261); the empty alignment table is IN-08's cells commit (J-1, answered by Jordan 2026-10-06: the two candidate drafts are folded into the build), not this row | `registers/editorial_ledger_in.jsonl:36, :38` |
| H-49 | CLOSED: `(Person, weight)` has a write-matrix row, a writer and readers | `engine/season/write_matrix.yaml:231-233`; `loop/matter.py:290`; `loop/effects_migration.py:171` |
| H-50 | CLOSED: `Tenure.payload` has a writer (the remit grant) and readers | `state/world.py:317`; `write_matrix.yaml:56-59`; `loop/resolve.py:117` |
| H-56 | HALF CLOSED: the within-season reaction is R-03's rounds loop (`met`); re-point probe A14 from its `Collision(needs="a ruling on which sentence binds")` to R-03's statement. The nested-DELIBERATE-in-RESOLVE half is HELD, and the row keeps its grade on that half (strictest part present) | `harness/probes.py:2160-2168`; `requirements.yaml:507-511` |
| H-57 | CLOSED: #453 R-9 (a), adopted with #453's intent (ED-IN-0288) — a grudge ends by `forgive`; AX-5's fading only removes | `architecture/meta/01_AXIOMS.md:128-141` |
| H-61 | CLOSED: superseded by A-25 (ED-IN-0285) — a module receives a typed input record and returns a typed output | `_part5` §A, A-25 |
| H-75 | transfer half CLOSED: `transfer` has its effect; `destroy_record`'s half goes to IN-26 | `loop/effects_economy.py:167` |
| H-91 | CLOSED: `_req_revoke` reads the seat's declared revocation basis (ED-IN-0256) | `loop/predicates.py:408-425`; `data/rosters.py:796` |
| H-105 | staging half CLOSED: `work` stages its declared delta and `restore` has its effect; the residual (no computed `work` declares a delta) is H-165 | `loop/effects_economy.py:21-45, :133` |
| H-108 | `via` half CLOSED: `Act.via` is set at CHOOSE and read at RESOLVE; the row re-scopes to delegation without a `hold`, owned by IN-48 (`_part5`, B-J; regency and family 57 wait on it, #453 `:3299-3300`) | `decision/choose.py:434`; `loop/resolve.py:117`; `state/gate.py:239-242` |
| H-110 | DISSOLVED (ruled): the `band_crossed` question it named no longer exists; the open routing gap is IN-29 | `proposals/2026-09-17-governance-and-holdings-r2/01_ATTENTION_AND_REACH.md:977-979`; `queries/world_q.py:1355-1369` |
| H-52 | CLOSED as "assumption stands" (CLAUDE.md §0's ladder, step 5; G-2) [medium; Jordan to correct]: `own` stays swept as shipped, so `open_case`'s eligibility is the column the verb table records (`assumption`, `own` swept); the row re-grades `assumption` with a `cite:` reading `CLOSED BY IN-43: assumption stands`. Revert: Jordan rules `own` the wrong game (the row's own words: *"the alternative (`own`) is a different game"*), and the row re-opens `absent` | `hole_register.yaml:594-596`; `verb_table.yaml:47-48` |
| H-89 | HELD, not cut: the `scale:` column answers Jordan's 2026-09-02 ask for a governance/management axis; what is missing is a reader (R-04) | `hole_register.yaml:1103-1115` |
| H-98 | HELD (fourth-band half): the fourth band has no source in the data and is not invented | `hole_register.yaml:1351-1353` |
| H-185 | HELD: a reader for an authored ought's `predicate` needs a magnitude nobody has ruled, or the field dropped; nothing planned needs it | `hole_register.yaml:4140-4152` |

A path above with no top-level directory is under `engine/season/`.

### IN-42 · = GO-02 · the `engine_clock` row gets its `doc:` (RULED)
- STATE: B      LANE: IN (GO)      BATCH: B-C (after IN-43)      R: — (M3)
- WHAT: RULED, ED-IN-0125 §(4) C3 (Jordan, 2026-08-04), recorded as "already ruled, not yet applied" in ED-1051's last row: `engine_clock` stands, and its `doc: null` points at the CANONICAL propagation spec rather than a new spine. The edit: `references/module_contracts.yaml`'s `engine_clock` row `doc: .designs/systems/_architecture/reference/propagation_spec_v1.md` — a quarantined `doc:` keeps its `.designs/` prefix (`:122`, ED-IN-0231) — and the row's own comment "`doc:` stays null pending ED-1051" (`:871`) rewritten to cite the ruling. `sim_module:` keeps the season calendar (`loop/driver.py` + `loop/calendar.py`, `:865-870`). Gate-0's first step (`CLAUDE.md` §6). `CURRENT.md:39` still names ED-1051 as `engine_clock`'s home: Layer 0, so it goes on IN-44's list (`_part8`), not into this edit.
- DEPS: IN-43 → IN-42 (F: `references/module_contracts.yaml`); IN-42 → GO-02 → GO-04 (D; GO-04 is B-L's tail and reads the seams after the move)      EDITS: `references/module_contracts.yaml` (one row and its comment)
- EXIT: `python -c "import importlib.util as u; s=u.spec_from_file_location('wb','skills/valoria-vector-audit/scripts/workbench.py'); m=u.module_from_spec(s); s.loader.exec_module(m); print(m.weave('.','engine_clock')[0]['doc_status'])"` prints `declared` (read 2026-10-06: `none`)      FALSIFIER: the same command prints `missing` if the path does not resolve, and `grep -c 'doc: null' references/module_contracts.yaml` must fall by exactly one. No existing test pins this row's `doc:`; the workbench's `_resolve_doc` is the only reader that tells a broken pointer from a null one
- SOURCE: `registers/editorial_ledger.jsonl:293` (ED-1051's last row); `references/module_contracts.yaml:122, :862-871`; `CURRENT.md:39`; `skills/valoria-vector-audit/scripts/workbench.py:134-148`

### IN-46 · = SM-6 · the grid mode's suspension at ENCOUNTER's barrier — design
- STATE: B (design)      LANE: IN (PC)      BATCH: B-C (design; re-read against the `combat` container in B-L); no build batch      R: R-04 (conjunct 3: the `scales:` row "personal combat / grid-based map combat with units")
- WHAT: the design `SM-6` owes (§SM table). A-25 (`_part5` §A) places a grid or map variant as the PLAYABLE mode of the `combat` container, "a `game/` scene, for which the driver suspends", the host taking "the same typed output either way". SM-5 is confirmed by Jordan's own words: *"a grid map-based version where you choose to attack and then in fire emblem style you see the bout, but it's my personal combat engine resolving there for a round — and then a duel version where you actually decide at each step/beat"* (`proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`; RS-6): two modes of ONE engine and no second resolver. What nothing specifies is the suspension. The design says: (1) where the driver suspends — ENCOUNTER (`loop/encounter`, `architecture/meta/04_CODE_ARCHITECTURE.md:177`) runs the ACTS rows a prize row DEFERRED at RESOLVE, shares barrier 3 and `WriteClass.ACTS` with RESOLVE, and is the nearest precedent; (2) what the driver holds while suspended and what resumes it, so that no write token is minted twice and no draw is consumed or skipped (the draw ordinal is per tick, `loop/driver.py:415`); (3) the typed input the host builds and the typed output it takes back, the pair AUTOMATED mode already uses (A-25); (4) how the PLAYABLE and AUTOMATED arms stay replay-equal when the player's choices equal the chooser's. It builds nothing and decides neither of #445 `05`'s held questions (§4.1 and §4.2: J-15, ask-then, attached to M-2 at PC-08). No Jordan ruling is needed. The design lands as a PROPOSED document under `proposals/` [ASSUMPTION: the location, by WR-04's precedent].
- DEPS: none to write it; re-read against the `combat` container once IN-04 has moved it (B-L), and against IN-47's carriers where a party is built from a person      EDITS: one new file under `proposals/`; none in `engine/`
- EXIT: the design reviewed — one document answering (1)–(4), each with the `file:line` of the site it names. **No build position exists, and R-04 conjunct (3) needs every `scales:` row `in_loop`** (`engine/season/requirements.yaml:70-189`; this row `:142-154`, `in_loop: "duel only, via combat_seam.py"`), so R-04, hence M1, cannot read `met` until a build batch exists for IN-46 and IN-47. Once the design is reviewed, `_part3` §B.0 R4/R7 place the build (the suspension edits `loop/driver.py` and `seam/wrappers/combat.py`)      FALSIFIER: at the build, one seeded season run twice — AUTOMATED, and PLAYABLE with scripted choices equal to the chooser's — ends at one `World.content_hash()`, and a scripted choice that differs from the chooser's moves it (the instrument can fail); a suspension that consumes a draw or mints a token twice reds the first
- SOURCE: `proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`; `architecture/meta/04_CODE_ARCHITECTURE.md:177`; `engine/season/requirements.yaml:142-154`; `engine/season/loop/driver.py:415`; A-25 (`_part5` §A); §SM, SM-5 and SM-6

### IN-47 · the character-sheet management space — design (creation, development, chronicling)
- STATE: B (design)      LANE: IN (PC, WR)      BATCH: B-C (design; reviewed against the carriers in B-H); no build batch      R: R-04 (conjunct 3: the `scales:` row "character creation / development / chronicling")
- WHAT: Jordan's 2026-09-05 framing lists *"a character generation/progression/management/chronicling system"* among the systems the game is (`references/what_valoria_is_and_what_runs.md:107`); his 2026-09-30 words "design one character sheet" are the other source [UNVERIFIED: not re-opened]. The `scales:` row says what exists: `Person` carries `pursuits`, `ledger`, `stance` and `capability`, and nothing creates or develops a person — no generation, no progression, no chronicle (`engine/season/requirements.yaml:71-82`; `capability` is empty on 429 of the 430 persons the 143 corpus cases build, measured 2026-10-02 per the row, not re-run). A-25 (`_part5` §A) places creation as the character-sheet management space, which, like the world surface, reads the player's own `View`/`Question`/`Candidate` and emits acts, "owning no game state, as the management spaces do". #445 `09_the_character_sheet.md` reconciles what a person is in code (§1.1 carrier, §1.2 capability, §1.3 the combat build, §1.4 memory and knowledge, §1.5 attributes, §1.6 derived, never stored) and recommends one sheet (§2, §3), on `proposals/2026-08-15-character-and-faction-stats-and-progression.md` (held for Jordan); it is analysis and does not say what creation, development and chronicling are as spaces. The design says, for each, what the space reads, which acts it emits, and which carrier an act reaches through the fold — never a direct write: **creation** — where a person comes from (a cast per case is built, `17`; nothing generates one); **development** — what writes `capability`, `pursuits` and `scar` after creation (IN-12 step 9's `train`, B-Q, writes `capability` only where a case names a vocation; IN-08's chain writes `scar`) and how the space reads those writers without owning them; **chronicling** — what a person's own record of a life is (the ledger, #445 §1.4) and how it is read out (#457 `STORY-READ`, an observer outside the simulation, since Layer 1 forbids salience ranking inside it). No Jordan ruling is needed. The design lands as a PROPOSED document under `proposals/` [ASSUMPTION: the location, and that dividing the sheet into these three spaces is the design's to propose].
- DEPS: IN-47 reads the carriers IN-08 creates (`Person.scar`, `Person.conviction`) and is reviewed against them in B-H; IN-47 ↔ IN-12 step 9 (R: `train` is the capability writer #445 K-4's `practice` verb was)      EDITS: one new file under `proposals/`; none in `engine/`
- EXIT: the design reviewed — one document naming, per space, the typed input it reads, the acts it emits and the carrier each reaches, each with its `file:line`. **No build position exists, and R-04 conjunct (3) needs every `scales:` row `in_loop`** (`engine/season/requirements.yaml:70-189`; this row `:71-82`), so R-04, hence M1, cannot read `met` until a build batch exists for IN-46 and IN-47; `_part3` §B.0 R4/R7 place it once the design is reviewed (a space that emits acts edits `decision/` and `state/carriers.py`)      FALSIFIER: a space that writes a `Person` field outside an act's fold contradicts A-25 and Layer 1's "a module with no token cannot write" (`architecture/meta/04_CODE_ARCHITECTURE.md:158`) and fails the review; at the build, a creation arm switched off reproduces the pre-build hash
- SOURCE: `references/what_valoria_is_and_what_runs.md:100-109`; `engine/season/requirements.yaml:71-82`; `proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md`; `proposals/2026-10-04-forcing-churn-and-the-story-bar.md:169` (`STORY-READ`); A-25 (`_part5` §A)

### IN-50 · the failing ARC R3 case — diagnose, then repair
- STATE: BLK:IN-43 (the print)      LANE: IN      BATCH: B-C (diagnose); the repair slots by `_part3` §B.0 R1–R7 once the case is known      R: R-01
- WHAT: R-01's first clause fails on the ARC lane only: `check R3: 96 of 97 pass` (ARC) against `46 of 46` (NPC), read 2026-10-02 at `444a00e1` (`engine/season/requirements.yaml:365`); `met` needs n of n on both lanes, and nothing owned the one case that fails. IN-43 (iv) prints its id; this position reads that case under `_r3_propagates` (`harness/corpus_run.py:692-728`), which is False in exactly two ways — fewer than two resolved acts (`:707-708`), or no Event whose cause is another person's act (`:720-727`) — and says which, and then which of three kinds the defect is [ASSUMPTION: the taxonomy]: the case's own authoring (a file under `engine/season/cases/`, loaded by `harness/run_cases.py::load_cases`), a loop gap that leaves the case no cross-person edge, or an instrument defect (the check missing an edge that exists; `planted_control` shows the detector works in general, not for this case). The repair is whichever kind it is, and its files are unknown until then, so it slots by `_part3` §B.0: a case file or the instrument is R5 (a B-C lane merging last); a loop gap is R1–R3 (the batch whose entry gate covers its D edges). A gap that only IN-10, IN-11 or IN-13's new cross-person edges close is recorded and left to their `11` re-takes (B-I, B-M), not repaired twice. B-C's HANDOFF line names the case, the cause and the batch the repair slots to.
- DEPS: IN-43 → IN-50 (D: the printed case id)      EDITS: unknown until diagnosed (`engine/season/cases/*`, `harness/corpus_run.py`, or a loop file)
- EXIT: the case id and the failing branch of `_r3_propagates`, read from that case's own run and written in the commit body; then either `python -m engine.season.harness.corpus_run` reads `check R3: 97 of 97 pass` (ARC) with the planted control still flipping False → True, or the later edge that closes it is named with its batch      FALSIFIER: the repair is wrong if any other case's `R3` flips to False, if the control stops flipping, or if the repair is keyed on the case's id (scripting drift: a repair is a rule, never a branch on one entry)
- SOURCE: `engine/season/requirements.yaml:332-335, :365-370`; `engine/season/harness/corpus_run.py:692-728, :1041-1044`; `engine/season/harness/run_cases.py:273`

## 4.3 B-L — MODULES (§SM, carried from v8)

Members, order, entry gate and exit instrument: `_part3` §B. B-L is IN-03 → IN-04 → IN-05, then the tail lanes MB-03, PC-06 M-1 and S-2/L-1, GO-04, with IN-46's design re-read against the moved `combat` container. It is placed after B-K, so THE NINE move first: nothing in B-G..B-K reads a module, and SC-01 (IN-03) and IN-13 (IN-05) are the positions that do; Jordan may run B-L right after B-D with no edge broken. Entry gate: B-B merged (IN-02's falsifiers observed, E17) and B-D1 and B-D2 merged, so that every lane edit to the two closures lands before the move (B-D1: PC-01..04, PC-07, PC-05 item 3; B-D2: MB-01, MB-02, MB-05, MB-06, MB-07, MB-04, each at its pre-move paths). The section's standing preamble, carried from `v8_part5.md:125-171`:

**Ruled:** `ED-IN-0284`, revised by `ED-IN-0285`. The vocabulary, directories, adapter model, module entry kinds,
containers and the retained-modules roster are **`A-25`** (`_part5` §A), stated there once; this section stages the code
and restates none of it.

**Order:** `30` → `31a` → `31b` → `31c` → `22` (SC-01, `_part6`; B-N). `33` and `36` are design work (B-C), their builds B-S and B-T. **Retired ids, never reused:** `31d`, `31e`, `32` (cancelled before anything built them).
**Names:** `30`–`36` are these positions and this is §SM — not the pre-flight rows `S-1`…`S-10` (v8 `_part3` §P, at its `FORK:` ref),
not `_part8` §S. `SM-1`…`SM-15` are this section's open items.

**Reading list** (one Haiku extract, handed to every producer): `A-25`; `references/module_contracts.yaml`
`composition_roles:`; `tools/export_composition.py`; `engine/substrate/composition.py`;
`engine/season/manifest/{registry,providers}.py`; `engine/season/loop/driver.py` (`resolvable_verbs`,
`SeasonDriver.__init__`); `engine/season/seam/ladder.py` and `seam/wrappers/`; `tools/ci_common.py`; the test
files each position names.

**Grade under `CLAUDE.md` §0.2: `paper`, every position.** One commit per position. A stage is gated on the
previous stage's falsifiers being OBSERVED, not on its commit existing; a falsifier that fails stops the stage:
`git revert`, never widen (main §0.5).

**THE CONTROL EVERY STAGE KEEPS.** `build_realm(0)`'s `content_hash()` and its one-season hash byte-identical across
the stage (`a918cd1f…` and `05f022e2…` were the readings at `52ec9a54`; the batches before B-L move them — declared movers
include IN-29, IN-08, IN-34, SC-03a's docket items and PC-02..04 — so each stage's control is the reading on ITS OWN base
commit, taken before the first edit); `python -m engine.season.harness.aperture 4 0` reads the same per-verb funnel with the
control hash EQUAL; `resolvable_verbs()` returns the same set (compare the two sets at the build — no number is
written here); `python tools/export_composition.py --check` OK. The two readings above were taken (v8 `_part6` §H.1, at its `FORK:` ref)
on HEAD `52ec9a54` as `build_realm(0)` then `populated.run(seasons=1, seed=0, w=w)`, `w.content_hash()`
after each; re-read both on the stage's base commit before it starts (`CLAUDE.md` §0.1 pt 3, row four).

**A REFUSAL FALSIFIER RUNS IN A FRESH SUBPROCESS.** `EFFECTS` (`loop/effects_shared.py:39`), `PROVIDERS`
(`manifest/providers.py:34`), the ladder's `_LADDER`/`_LADDER_ERROR` (`seam/ladder.py:92-93`) and `30`'s
`MODULE_ENTRIES` are process globals: in a pytest process another test's imports can fill them, so an in-process
test can pass on a table it did not build. Precedent: `tests/valoria/test_season_providers_are_registered.py`.

**What is true today** (opened 2026-10-03 on `5390fc75`; re-derive by symbol — lines drift):
- *Three verbs call a module* — `fight`, `march`, `tell`, the rows with `contests:`. Every other verb's effect is
  host interpretation, its rules in the gate, `world_q`, the predicates and MATTER (`SM-8`).
- *`World.boot` is on no run path* (`loop/driver.py:238-248`); `SeasonDriver.__init__` (`:234`) calls
  `check_rows()` (`:249-250`), and every run passes there.
- *Nothing observes a drop.* `@provider` and `@effect_for` are dict writes at import (`manifest/providers.py:37-40`,
  `loop/effects_shared.py:42-44`); `resolvable_verbs()` (`driver.py:101`) excludes, each without a word, a verb
  whose untyped precondition nothing evaluates (`:125-127`), a writing verb with no effect (`:128`), and a
  contested verb whose provider is not registered (`:186-189`).
- *The corpus helpers walk `engine/season/` by path* (`data/files.py:182`, `:206`, `:264`): a file that leaves the
  package leaves every scan built on them with a green floor; a floor or superset assertion is the only observer.
- *The path-keyed scans of module code derive their roots from `tools/ci_common.py` `MODULE_CODE_ROOTS`*, so
  `modules/` may now be created. Scans still outside it have an owner below: `tools/evacuation_plan.py`'s R-CODE rule
  (`30`), `tools/ci_pp_frozen_check.py` and `tools/ci_module_shape_check.py` (`31a`), the corpus pin in
  `test_season_shape.py` (`31a`), and `modules/combat/` joining `sim_params.json` (`31b`).


### IN-03 · `31a` · social contest — `seam/wrappers/sigma.py` → a host input builder + `modules/social_contest/` · IN/SC · gate `30` · `opus`/`opus` · `[infrastructure]`
- STATE: BLK:IN-02      LANE: IN (SC)      BATCH: B-L (head)      R: —
- WHAT: the spec carried below; creates `modules/`. Its entry gate is B-L's (B-B merged; B-D1 and B-D2 merged; after B-K unless Jordan runs B-L early).
- DEPS: IN-02 → IN-03 (R); IN-03 → IN-04 (R); IN-03 → SC-01 (R: E17/A-25 — `22` builds its provider on this typed input record; SC-01 is B-N, so B-N's entry gate is B-L merged); IN-03 → PC-06 S-2 (D; a B-L tail lane)      EDITS: `rosters.yaml`, `seam/wrappers/sigma.py`, `module_contracts.yaml` + `composition.json`, `manifest/`, shape pins
- EXIT: both control hashes unchanged (re-read on the base commit) and falsifier (3) observed in a fresh subprocess      FALSIFIER: (1)–(5) below; (3) is IN-02's falsifier (2) in its fresh-process form
- SOURCE: `engine/season/seam/wrappers/sigma.py`; carried below, `v8_part5.md:239-275`:

**Grade:** `paper`. **Hash:** unchanged. **R:** none. Creates `modules/`.
**WHERE.**
1. **The typed input record first.** `resolve` (`sigma.py:125-172`) reads `World` directly — `w.persons` (`:154`;
   `_obstacle_of` at `:119`) and `w.fixtures` (`:158`) — and its docstring admits the signature takes `w`
   (`:44-46`). A host INPUT BUILDER turns `World` into a frozen typed record of exactly what the roll reads
   (claimants; the pool from `_pool_of`, `:90`; the obstacle from `_obstacle_of`, `:105`;
   `obstacle_refusal_multiple`, `:161`). The builder and the input and output types live host-side, where
   projections are built (A-25); the module imports the types (it depends upward on `engine/`), and the host reaches
   the module only by string.
2. **The module entry** in `modules/social_contest/`: it takes the record and a seeded `rng` (already a parameter,
   `:128`, never constructed in the provider — `04 §C.12` rejection 4, docstring `:138-145`) and imports the dice
   engine and the record types, nothing else. One composition row: `entry: verb_call`, `verb: tell`.
3. **The host adapter** keeps `@provider("contest", "sigma_leverage")` (`:125`) and S27.4's refusal: it builds the
   record, calls the entry through `MODULE_ENTRIES`, returns the result. The prize rows keep `interim: true`
   (`rosters.yaml:1134`, `:1152`) until `22` decides.
4. **The corpus.** The margin-producer scan pins `{"seam/wrappers/sigma.py"}` (`test_season_shape.py:13113`) over
   `files.package_modules()`, which does not walk `modules/`: widen it to `ci_common.MODULE_CODE_DIRS` and re-pin under a superset
   assertion naming the moved file, or it passes by finding nothing. That test reaches `tools/` the way the
   `tests/valoria` files that import `ci_common` do (`sys.path.insert(0, <repo>/tools)`); the season package's own
   path owner, `engine/season/data/files.py`, must not re-spell `modules` (a second owner).
5. **Scope.** Lens B's scope gains `modules/` (`skills/layer-conformance/SKILL.md:8`, `.claude/commands/close.md:30`),
   and so do two roots that still name only `systems`: `tools/ci_pp_frozen_check.py`'s `SCAN_ROOTS` (blocking; a PP id
   cited in module code must be under the ceiling) and `tools/ci_module_shape_check.py`'s `RUNTIME_ROOTS`
   (report-only). `31b`'s `git grep -l combat_engine_v1` catches the second only for combat.
   Loop-resident proceedings stay host (A-25).
*Wording edit deferred to this commit:* FI-01's (`_part6`, `ED-FI-0009`) INSTRUCTION and A-21 (`_part5` §A) cite `sigma.py::_pool_of` and
`_obstacle_of`; after the split those are the host input builder's — re-point both.
**FALSIFIERS.** (1) Both hashes unchanged. (2) A module test that imports only `engine/dice_engine/` and the record
types, builds a record by hand and asserts the result record (a `dict`, `status="RESOLVED"`, with `net` and `ob`; no
`Margin` type exists, `sigma.py:44-49`). (3) In a fresh subprocess, delete the composition row → driver construction
refuses naming it (the registrar's first production row). ⚠ `30` observed its own falsifier 2 in the within-process form only: the registrar's "no row declares" refusal fires
only once an earlier construction has filled `MODULE_ENTRIES`, because no data at `30` declares that a row must exist
(A-25: verb rows name no module). This falsifier needs such a declaration — the candidate is the prize row ↔ composition
row agreement (A-25, "two owners say which module is called"), checked at construction — which `31a` places; `31b` (4)
and `31c` (3) read the same. (4) `harness.aperture 4 0`: `tell` executes the same
count, control hash EQUAL. (5) `test_importing_every_engine_module_pulls_in_no_subsystem` green over `modules/`.


### IN-04 · `31b` · combat — wrapper split; the reachable engine → `modules/combat/` · IN/PC · gate `31a` · `sonnet`/`opus`, a `haiku` reachability census first · `[infrastructure]`
- STATE: BLK:IN-03, PC-02, PC-03, PC-04      LANE: IN (PC)      BATCH: B-L (after IN-03)      R: —
- WHAT: the spec carried below; the `sim_params.json` decision is made in this commit; SEAM-LADDER (#457) folds into item 5's T-k reading (`architecture/meta/03_VERBS_AND_LOOPS.md:286`).
- DEPS: IN-03 → IN-04 → IN-05 (R); IN-04 → PC-06 M-1 (D; a B-L tail lane); PC-02/03/04 → IN-04 (F: lane edits first), and so is every other B-D1 edit to the closure — PC-01, PC-07 (J-20 (B): the dead `COVERAGE_GAP['partial']` branch and the `coverage` parameters are deleted before the move), PC-05 item 3 — all landed at B-D1's merge, so the control hashes are read on B-L's base commit, after PC-02/03/04 moved combat outcomes      EDITS: `seam/wrappers/combat.py`, `seam/ladder.py`, `module_contracts.yaml` + `composition.json`, shape pins, the `systems/combat` move
- EXIT: both hashes unchanged; `balance.py` runs; one seed run twice in one process gives one hash      FALSIFIER: (1)–(5) below, and (6): IN-08 (B-G) adds `accept` with `contests: "the body"`, which the prize row `"the body"` already claims (`rosters.yaml` `prizes:`), while this stage's composition row names `verb: fight` and the registrar's `verb:` names one verb — after the split `aperture 4 0` shows `accept` still reaches the one `combat` provider, and whether a second `verb_call` row is needed is read at the split [GAP: the contested-verb check resolves by prize (`loop/driver.py:182-192`), so `accept` is claimed; whether the composition row must also name it (A-25: the prize row and the composition row are the two owners; `manifest/registry.py:104-111` states the one-`verb:` shape) was not traced]
- SOURCE: `proposals/2026-10-04-forcing-churn-and-the-story-bar.md:173`; carried below, `v8_part5.md:278-312`:

**Grade:** `paper`. **Hash:** unchanged. **R:** none.
**WHERE.**
1. Split `seam/wrappers/combat.py` as `31a` split `sigma.py`: a host input builder, and a `verb_call` entry for
   `fight` in `modules/combat/`.
2. Move the reachable set of `systems/combat/combat_engine_v1/` — re-derived by an import walk from `wrapper` and
   `combatant`; `workbench/` and anything unreached stay — to `modules/combat/`, keeping FLAT names: the files
   bare-import each other, so a dotted import would give `wrapper`/`combatant` a second identity
   (`engine/substrate/pc_engine.py:5-8`). `PC_ENGINE_DIR` (`pc_engine.py:29`) is re-pointed;
   `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}` (`test_engine_does_not_import_systems.py:223`) keeps its one
   member. A directory-prefix MOVE row in `references/restructure_ledger.md`; every path reader re-derived with
   `git grep -l combat_engine_v1` (registries under `references/`, `references/canonical_sources.yaml`'s pins read by
   `tools/freshness_gate.py`, `.claude/launch.json`, `tools/`); every export citing a moved file re-derived by its
   own exporter. **Decide, in this commit, whether `modules/combat/` joins `sim_params.json`.** `ci_common`'s
   `('modules', '*')` row puts it under `sim_reference_roots()`, so `tools/export_sim_params.py` would export its
   module-scope constants as `combat.*` beside `combat_engine_v1.json` (which `_scan_dirs`'s docstring says keeps its
   own export), `tools/export_game_constants.py` would prefer the `sim_params` entries, and
   `ci_sim_fabrication_check` would start gating the personal-combat oracle (the KNOWN GAP in its docstring, ED-IN-0119,
   a PC-lane call). Either keep it out at the owner or take all three; a `--build` that re-greens `--check` ships the
   change unobserved.
3. **The bare-name importers left behind.** The commit lists every file under `systems/` that imports the moved
   closure by bare name and re-points each. `systems/combat/combat_engine_v1/workbench/balance.py` is one (it puts
   its parent directory on `sys.path`, `:14-15`), and it is what `CLAUDE.md` §9 routes combat balance to.
4. `systems/combat/sim/combat.py` (DEPRECATED, no importer; its header names ED-900/904/1029) STAYS (`SM-4`).
5. **The `04` T-k reading, recorded.** `combat_degree` (`seam/ladder.py:124-168`) and `field_degree` (`:171-192`)
   STAY in the seam. Write into `seam/ladder.py`'s module docstring that T-k (`04:122`, "the ladder lives once, in
   the seam") is read narrowly: `degree_from_net` is the one margin ladder and `degree_of` (`:195`) its one
   dispatcher; the two reads grade a provider's own result against roster edges (`combat_band_edges`,
   `field_degree_bands`) and hold no band table. Neither `31b` nor `31c` touches the deferred dice-engine read
   (`ladder.py:106-116`).
**FALSIFIERS.** (1) Both hashes unchanged. (2) One seed run twice in ONE process gives one hash (module-level state
surviving between worlds makes the second run differ). (3) After the move `balance.py` still imports its engine and
runs (`__main__`, `:222`), and every other listed importer's covering test is green. (4) In a fresh subprocess,
delete the composition row → driver construction refuses naming it. (5)
`test_the_one_declared_path_seam_is_still_the_only_one`, `engine/season/tests/test_combat_band_edges.py` and
`python tools/freshness_gate.py` green.

### IN-05 · `31c` · mass battle — shed module state; wrapper split; `resolve_field`'s closure → `modules/mass_battle/` · IN/MB · gate `31b` · `sonnet`/`opus`, a `haiku` reachability census first · `[infrastructure]`
- STATE: BLK:IN-04, MB-01, MB-02, MB-05      LANE: IN (MB)      BATCH: B-L (after IN-04)      R: —
- WHAT: the spec carried below. SM-7's test — `modules/**` equals the reachable closure in both directions — lands here (licensed by `CLAUDE.md` §0.1 pt 5: `modules/` is the port's input set).
- DEPS: IN-04 → IN-05 (R); IN-05 → IN-13 (F: `seam/wrappers/mass_battle.py`; IN-13 is B-M), IN-05 → MB-03 (F: `massbattle.py`; a B-L tail lane); MB-01/02/05 → IN-05 (F), and so is every other B-D2 edit to the closure — MB-06, MB-07 (J-18 (A): cap support at the ranks a troop type's weapon reaches) and MB-04, each built at its pre-move paths and landed at B-D2's merge; IN-05 → GO-05 (D: the manifest resource lists `modules/**`)      EDITS: `seam/wrappers/mass_battle.py`, `module_contracts.yaml` + `composition.json`, shape pins, the `systems/mass_battle` move
- EXIT: the provider test end to end; one constructed `march` resolved twice in one process gives one result; SM-7's test green      FALSIFIER: (1)–(4) below; SM-7's test reds on a planted unreached file under `modules/`
- SOURCE: `v8_part5.md:373` (SM-7); carried below, `v8_part5.md:316-335`:

**Grade:** `paper`. **Hash:** unchanged. **R:** none.
**WHERE.**
1. **Shed the module-level state first**, under `systems/mass_battle/sim/`: `rngsource.py:39` `_active` (falls back
   to the stdlib `random`), `terrain.py:82` `_cache`, `resolution.py:15` `_battle_trace` — each becomes per-call
   state or a parameter (AX-4, `04:115`, enforced at D-3, `04:1017`).
2. Split `seam/wrappers/mass_battle.py` as `31a` split `sigma.py`. `loop/sides.py` stays host: it builds the
   claimants the input record carries.
3. Move the reachable closure of `massbattle.py::resolve_field` (an import walk; `workbench/` and anything unreached
   stay) to `modules/mass_battle/`, rewriting its internal `systems.mass_battle.sim.…` imports;
   `mass_battle.resolve_field` (`module_contracts.yaml:103-105`) is re-keyed to the moved target with
   `entry: verb_call`, `verb: march`, and `composition.json` re-derived. A directory-prefix MOVE row; path readers and
   the bare-name importers left in `systems/` listed and re-pointed as at `31b`.
*Wording edit deferred to this commit:* `_part2` R-04's "mass battles / strategy warfare" row "`march` → `seam/wrappers/mass_battle.py`" → "`march` → its
host adapter and `modules/mass_battle/`".
**FALSIFIERS.** (1) Both hashes unchanged — and blind here: the realm fights no field (H-149), so `march` is not
exercised by the control; the commit says so. (2) The targeted probe instead:
`engine/season/tests/test_mass_battle_provider.py` end to end, and one constructed `march` resolved twice in ONE
process with one seed gives one result (nothing observes this today). (3) In a fresh subprocess, delete the
composition row → driver construction refuses naming it. (4) `tests/valoria/test_mass_battle_d1_morale_baseline.py`
and the mass-battle workbench's covering tests green.

## 4.4 B-E — TELLING + SCORE (the telling workplan, absorbed)

Members, order, entry gate and exit instrument: `_part3` §B. B-E is IN-16 → IN-17 → IN-18 → IN-15, then IN-25 and IN-22's reach half (`_part5`), with the lane {PC-06 S-1} (`_part7`). **Entry gate: B-H merged.** IN-08's cells (B-G) and chain (B-H) land first, because G1's judged regard is built on `align_kind` and the pursuit projection (`data/verbs.py:1044-1061`), which IN-08 re-axes, and G2 and IN-25 tune the `score` that 6f rewrites, so the cells land before the code that reads them; G1's `deed:` keys are therefore authored on the 15×7 basis in this batch and re-cell nothing. Never re-take `11` across this batch (E15). Every hash control in it (T7's `intent_disclosure` 0, IN-25's gain 0) is the reading on B-E's own base commit, after every earlier mover. T0–T6 are built (#449); their *As built* text stays at the telling workplan's `FORK:` ref, and ED-IN-0282's superseding row reads "absorbed into v9; nothing re-ruled". `test_season_shape.py` pins move serially. The shapes the tail builds on, carried from `telling:50-61` (paths under `engine/season/`):

| thing | shape | owner |
|---|---|---|
| `Said` | `NamedTuple(subject: str, predicate: str, value: Any, confidence: int, chain: tuple[str, ...], circle: tuple[str, ...] \| None)` | `state/carriers.py` |
| `said_of` | `(claims, subject, fx) -> Said \| None`; today's pick (newest non-`seen`, else newest) | `queries/person_q.py` |
| `Claim.chain` | `chain: tuple = ()`, origin first, replacing the `teller` field; `teller` becomes a property, `chain[-1]` or `None`; hops = `len(chain)` | `state/carriers.py` |
| told deposit | `chain = said.chain + (act.actor,)`; `visibility` stays `"own"`; confidence raw | `loop/witness.py` |
| `LedgerReader` | `(claims, weigh=None)`; `_best` groups matches by `value`; `support(v) = 1 − ∏ over distinct origins (1 − weigh(c))`, origin `chain[0]` (the holder, if firsthand); key `(support, when, confidence)`. At `weigh ≡ 1` it collapses to today's | `queries/person_q.py` |
| `teller_weight(p, fx)` | the `weigh` closure: firsthand 1.0, else `clamp01(told_weight ** hops · relation · record)`; `relation = 1 + rank_gain·rank + regard_gain·clamp(regard/STANCE_MAX, −1, 1)`, `STANCE_MAX = STANCE_VALENCE_SCALE ** 2`; `rank ∈ {−1, 0, +1}` from the hearer's own `office` claims; `record` per T6 (`record(p, x, fx)`, no pair ⇒ 1.0) | `decision/options.py` (`person_q` never imports `decision/`) |
| `regard(p, x, fx)` | `stance_toward + regard_gain·judged + lambda_teller·told_valence`; only the stored half exists until G1; `judged` has no relation factor, so regard never calls weigh | `queries/person_q.py` |
| `with` stem | two persons share `place_of`; UNKNOWN if either has none, and always UNKNOWN person-side | `data/requires.py`, `queries/world_q.py` |
| `tell` row | `requires_typed: {all: [{form: own_ledger, of: subject, conjunct: holds}, {form: relation, of: to, relation: with, conjunct: hearer}]}`, `counterparty: to`, `emits_on_refusal` keyed `holds`/`hearer` → `news.untold` (precedent: `issue`) | `verb_table.yaml` |
| `known_persons` | ids from truthy `exists:Person` claims, `Seen.who`, told `chain[-1]`; minus self and referent | `queries/person_q.py` |

### IN-16 · T7 · declared intent (G9)
- STATE: B      LANE: IN      BATCH: B-E (first)      R: —
- WHAT: Jordan: "Build G9 declared intent as a position". Add the T7 row first (gate T4, T5, the opportunity-key fix), then build: a teller may tell a hearer an act they have CHOSEN-AND-NOT-YET-DONE, as a position and a claim kind (`decision/choose.py` declares; fixture `intent_disclosure`, control 0; a roster for the claim kind; a `world_q` branch), with two hole rows (an `assumption` row, and an `absent` row for intent reconciliation with its field-less `# ABSENT: H-NNN` marker beside `record`'s loop in `decision/options.py`). T7 must NOT rely on an event-kind exclusion in `said_of`; there is none, by ruling.
- DEPS: IN-16 → IN-17 → IN-18 (D); IN-16/IN-18 ↔ IN-15 ↔ IN-10 ↔ IN-22 (F; IN-10 is B-I, after this batch, so the F edge is honoured by B-E landing first)      EDITS: `rosters.yaml`, `decision/choose.py`, `decision/options.py`, `queries/person_q.py`, `loop/witness.py`, `queries/world_q.py`, `fixtures.py`, shape pins
- EXIT: `python -m pytest engine/season/tests/test_told_by_channel.py -q -k t7`      FALSIFIER: `test_t7_*` — at `intent_disclosure` 0 the realm hash equals the pre-T7 hash, read on B-E's base commit before T7's first edit (every earlier hash mover has landed by then); above 0 a hearer holds the teller's chosen-not-done act; self-telling frequency is measured in scratch before shipping, controls recorded first
- SOURCE: `registers/handoffs/HANDOFF_IN.md`, the row beginning "Telling build (`ED-IN-0282`)", "Next, in order" item (1); its gate is landed — T4/T5 (#449) and the opportunity-key fix, `engine/season/data/verbs.py::opportunity_key` (`engine/season/tests/test_told_by_channel.py:1026-1079`)

### IN-17 · the owed telling measurement and the `absent` re-check
- STATE: BLK:IN-16      LANE: IN      BATCH: B-E      R: —
- WHAT: on `build_realm(0)` ×3, the share of `news.untold` that are `hearer` refusals against lost contests, and retries of one `(verb, subject, to)` across rounds (the refusal does not teach the teller the hearer is absent); then re-check `absent` rows H-180, H-181, H-182 at T7, the G3–G7 triggers being met. A CHOOSE-side hearer term is G1's call (IN-18).
- DEPS: IN-16 → IN-17 → IN-18 (D)      EDITS: none in code; a hole row re-graded only where the re-check moves it
- EXIT: both figures in T7's commit body with the command and the md5 of its output      FALSIFIER: the scratch script asserts it counted at least one `news.untold` (`checked >= 1`); each re-checked row cites the run that shows presence (`CLAUDE.md` §0.1 pt 3, row one)
- SOURCE: `registers/handoffs/HANDOFF_IN.md`, the row beginning "Telling build (`ED-IN-0282`)", "Next, in order" items (2), (3)

### IN-18 · G1–G8 · the gated tail
- STATE: BLK:IN-17 (and B-E's entry gate, B-H merged, for IN-08); once IN-17 lands, per gate — G1 trigger met (re-measure M0b on the base commit); G2 stored half; G3–G7 trigger met (M0a > 0); G5 after `oblige` forms (IN-10's sub-step (a), B-I, so G5 is built there and not in B-E); G7 after G2, G3; G8 gated by judgment; step 2a buildable      LANE: IN      BATCH: B-E · B-I (G5 only: it is built at B-I, after IN-10's sub-step (a); `_part3`'s B-I members and card list it)      R: R-07 (G1: ≥ 1 differing pair)
- WHAT: the §5 table, §6 branches and §10 judgments carried below; the judgments are recorded, not ruled by Jordan, and reversible (G8 letters gated; self-disclosure allowed; private whispers not built). In the carried text "Batch 2" is the telling workplan's (T4–T6, landed in #449); v9's batches are the B-letters. **The `deed:` basis:** IN-08 (B-G, B-H) lands before this batch, so G1's `deed:` branch reads the 15×7 table and its `deed:<kind>` cells (H-66) are authored on the new axes in G1's own commit; §6's M0b branch below ("`deed:` cells are authored under H-66 in its commit (wait if plan `12c` is imminent)") reads with `12c` already landed. **R-07, and G1's branch.** G1 is trigger-gated (M0b, re-measured on B-H's merge commit) and its own falsifier is a constructed two-hearer fixture, so the realm reader R-07 needs is this entry's EXIT. M0b ≥ 5 % at `declared`: G1 lands in B-E. M0b < 5 % at `declared` only: G1 lands with `deed:` cells authored under H-66 in its own commit (IN-08 has landed, so the source's "wait if plan `12c` is imminent" is spent), not at control, which could not satisfy the R-07 conjunct [medium; Jordan to correct; revert: Jordan states that G1 ships at control]. M0b < 5 % at both arms: G1 does not land, R-07's regard conjunct has no path in v9, and the finding is recorded on H-62 with nothing invented (the telling workplan's own rule). **G6 and SC-02:** G6 (a private telling deposits `Claim.visibility == (A, B)`; trigger met, §6 below) builds on the `Claim.visibility` field (`state/carriers.py:283`), which SC-02's `22a` deletes as inert (`_part6`, B-P); `22a` re-greps the field's readers at B-P and keeps the field if G6 has landed. CARRY-INTERIOR's falsifier (#457 `:161`: "after a lost field or famine, stance rows change for witnesses, not only participants; weight 0 is the control") is homed here, at G1's regard-at-read, with IN-13's fought field (B-M) as its occasion. **Also owned here: #453 step 2a**, the `tell` widening its build order hands to the telling work — `known_persons` stops discarding the topic (`out.discard(topic)`, `queries/person_q.py:269`), so B, knowing C and holding `(C, x)`, forms a `tell` with `to == C`; `test_t4_one_candidate_per_known_hearer` is re-pinned in the same commit. **The one declared exception to "gate and trigger text carried unchanged":** §5's ties row re-points its prerequisite from plan `14` to IN-32; every other gate and trigger cell is the source's.
- DEPS: IN-17 → IN-18 (D); IN-08 → IN-18 G1, G2 (D: G1's `align_kind` and the pursuit projection, and the `score` G2 tunes, are the table and the scoring IN-08 re-axes and rewrites, so the cells land first: B-G → B-H → B-E); IN-18 G2 → IN-25 (D: the stance term's gain needs G2's polarity in `score`); IN-10's `oblige` sub-step (a) → IN-18 G5 (D; B-I)      EDITS: `rosters.yaml`, `decision/options.py`, `queries/person_q.py`, `loop/witness.py`, `queries/world_q.py`, shape pins (step 2a: `test_season_shape.py:14741-14757`)
- EXIT: per gate, §5's falsifier column; step 2a, `python -m pytest engine/season/tests/test_season_shape.py -q -k "t4_one_candidate_per_known_hearer"` green as re-pinned; at the batch exit `CLAIMS BY SOURCE` and `DISTINCT EXECUTED SETS` diffed and the realm ×1/×3 hash declared; **the R-07 realm reader** (`_part2` R-07), run at B-E's exit when G1 has landed: a two-season `build_realm(0)` run that reads `regard(p, C)` for every pair of hearers holding a claim about one C and asserts `checked >= 1` pair whose regard differs because of a claim or a teller's regard and not from stored stance alone, beside the same run at G1's control arm (judged and told halves at 0), which must show no such pair; G5's falsifier (§5 row G5) is observed at B-I, after IN-10's `oblige` sub-step (a)      FALSIFIER: G1 — two hearers with opposite `pursuits` on a deed's axis and the same deed claim about X: `regard` signs differ, both 0 at control (§5 row G1). Step 2a — before the edit the T4 test passes as written and a person who knows C and holds `(C, x)` forms no `tell` with `to == C`; after it, that `tell` forms and the un-re-pinned test reds (#453 records the step as moving one decline)
- SOURCE: `registers/handoffs/HANDOFF_IN.md`, the row beginning "Telling build (`ED-IN-0282`)", "Next, in order" item (4); `engine/season/queries/person_q.py:260-271`; `engine/season/tests/test_season_shape.py:14741-14757`; `proposals/2026-10-03-verb-coverage-and-gap-fill.md:2459, :2483`; carried below, `telling:297-316` (§5 GATED):

**The rule.** A field lands only in the same commit as its reader and its falsifier; an unfleshed
element is recorded by an `absent` row in `hole_register.yaml` plus a field-less `# ABSENT: H-NNN`
marker where it will go, never a dead carrier or a raising stub. §0.1 pt 5 forbids a guard over them,
so each trigger is a figure an existing instrument prints.

| ID | element | prerequisite | trigger | falsifier | marker site |
|---|---|---|---|---|---|
| G1 | judged regard | T2, T3b | M0b ≥ 5% at `declared` | no planted rows; two hearers, opposite `pursuits` on a deed's axis, same deed claim about X: `regard` signs differ; both 0 at control | `person_q.regard` |
| G2 | polarity in §F2 term 2 | T2, T3b (G1 if built) | none: after Batch 2, on the stored half | grudge on faction F: members choose `march` on F-held rungs more under `declared` than `legacy` (`checked >= 1`); `fight` against the disliked rises | `holder` operand (0 for Rung targets while M0g < 5%) |
| G3 | slant | G1 | M0a > 0 after T4 | the strongly valenced older claim is told under `valence`, the newer neutral one at control | `said_of` |
| G4 | C's move, **droppable** | G2 | M0a > 0 | two-arm count of C's acts naming A; **zero drops the row** | `questions_for`; `occasioned_by` branch [GAP] |
| — | ties | IN-32 (`_eff_tie`, `_part5`) | `aperture 1 0`: `tie / knot` executed > 0 | IN-32's | none here |
| G5 | duty to report | T4 | M0e > 0 | an obligee forms a `tell` to the seat holder; without `oblige`, none | `_from_inferred_claim` |
| G6 | confidences | T4, G1 | M0a > 0 | a private telling deposits `visibility == (A, B)`; retelling outside it emits `confidence.broken` | told branch, circle line |
| G7 | deception | T6, G2, G3 | M0a > 0 | after two caught lies, the liar's `record` is below an honest teller's | `said_of` |
| G8 | letters | T4 | none; ahead of T5 if M0d < 20% | `create_record(letter)` + `give` deposits the said triple as `told_by`, chain ending in the maker | beside the `content:` deposit |

Other `absent` rows and triggers: `stake` (M0h > 0); a default-obstacle sweep (M0i after T4 no higher
than at T0); `Seen.who` as a source (only if M0d counts zero from it); sanctioned silence (`date.fired`
reaching WITNESS, plan position `22`).

§6 M0 branches, carried from `telling:320-324`:

- **Lands regardless:** T1, T2, T3a, T3b, T5, T6, G2 (stored half: loyalty and grudge rows are real), G8.
- **M0a ≈ 0:** G3–G7 wait; re-measure after T4 (it produces person subjects). Still zero: record on H-62; invent nothing. **Re-measured after T4: M0a > 0 (realm person-subject executed 2 of 3), so the G3–G7 trigger is met; the IN-17 re-check of the `absent` rows is owed at T7.**
- **M0b ≈ 0:** at `declared` only, G1 ships at control, or `deed:` cells are authored under H-66 in its commit (wait if plan `12c` is imminent); at both arms, G1 does not land.
- **M0d ≈ 0:** T4 lands, its `test_n3` re-pin is refused, and G8 moves ahead of T5 as the main channel.
- **G8 branch, taken as a judgment, not a rule:** realm M0d 12% < 20%, which licensed G8 ahead of T5; T5 landed first, and G8 stays gated.

§10 decisions still standing, carried from `telling:378-382`:

| # | decision | recommendation |
|---|---|---|
| 1 | **Private whispers** (heard only by the person told). Jordan's alone: it voids T-e (recipiency computed at WITNESS from presence) and T4 is redone | Do not build; absent that wish, nothing escalates |
| 3 | **Self-disclosure** (A tells B about A) | Allow: skip self-subjects only on rows without a counterparty; with `to` as opponent it is not self-contest, and `to == p.id` is still declined |

### IN-15 · AX-7 · the divergence formula, then the wiring
- STATE: BLK:IN-16, IN-18 (then design first)      LANE: IN      BATCH: B-E (after IN-18)      R: —
- WHAT: AX-7 makes the four `Claim`-construction sites a contradiction. Name the divergence FORMULA — how channel, competence and prior belief alter a deposited claim's value or confidence; H-36's `refract` rules the shape, not a magnitude — then wire `agreement`/`standing_of`/`belief_contradicts` into the producers.
- DEPS: IN-16/IN-18 ↔ IN-15 ↔ IN-10 ↔ IN-22 (F; IN-15 lands in B-E, before IN-10 (B-I), and IN-22's reach half (`_part5`, B-E) lands after IN-15 and IN-18)      EDITS: `decision/options.py`, `loop/witness.py`, shape pins
- EXIT: the formula named in the commit, then its covering test under `engine/season/tests/`; realm hash declared      FALSIFIER: one claim told through two channels deposits a different value or confidence; at the formula's control the deposit equals today's (hash equal)
- SOURCE: `registers/handoffs/HANDOFF_IN.md`, the row beginning "`AX-7` makes four `Claim`-construction sites"; ED-IN-0244, ED-IN-0245 (`RR-P`)

## 4.5 Re-plug designs — written in B-C; the builds are B-S (IN-06) and B-T (IN-07)

IN-46 and IN-47, the other two B-C designs, sit with B-C in §4.2: they have no build batch.

### IN-06 · `33` · the unplugged systems — design, not relocation · IN/WR/FI · gate A-11, A-20; `30` built · `opus`/`opus` · `[design]`
- STATE: B (design)      LANE: IN (WR, FI)      BATCH: design B-C · build B-S (entry gate: B-R, B-F and B-D3 merged; the design is re-reviewed after B-G, because it names carriers IN-08 creates)      R: —
- WHAT: the spec carried below. Absorbs A-24's threadwork question (answered: the design is here, buildable now), the WR remainders' seam, FI's knots half (FI-05) and H-47.
- DEPS: IN-06 → WR-01's `engine/season/` reach, IN-32, IN-35, PC-06 K-3 (D: the design names the carriers; all B-S); IN-08 → IN-06's review (D: `Person.pursuits` and the scar counts exist as the cells commit and the chain leave them)      EDITS: composition rows (`module_contracts.yaml` + `composition.json`); the store-shed in each module
- EXIT: the design reviewed, after IN-08's cells and chain (B-G, B-H) so that it names the carriers as they stand; at build (B-S), a plugged row's deletion refuses at driver construction (fresh subprocess)      FALSIFIER: one seed run twice in one process gives equal hashes (below)
- SOURCE: `engine/season/hole_register.yaml` H-182, H-47; carried below, `v8_part5.md:339-350`:

**Grade:** `paper`. Threadwork (`systems/threadwork/sim/`), fieldwork's `knots.py`, characters' `conviction.py` and
overview's `ms_track.py` are reached by nothing, and no position moves them. Re-plugging one is design work:
1. **Shed the store first.** `knots.py:155-156` (`_knots`, `_knot_id_counter`); `conviction.py:82`
   (`_conviction_state`). `ms_track.py` holds no store but writes `world.clocks['MS']` on a `world` argument (`:70`,
   `:91`), and the season `World` carries no `clocks`, so it cannot plug as it stands.
2. **The clause** is AX-4 (`04:115`), enforced at D-3 (`04:1017`); `_knots` also breaches D-10 (`04:1024`). Never
   D-8 (`04:1022`), which grades a stored aggregate.
3. **The carrier each needs:** a knot's (`H-182`: ED-912's gauge → `Tenure.degree` mapping is UNLOCATED; and
   `SM-3`); conviction's (`Person.pursuits` and scar counts — the cells commit, IN-08); `rendering.py`'s stubs (A-20);
   threadwork's re-plugging into `ms_track`/`knots` (A-24).
**FALSIFIER.** A plugged module has a composition row whose deletion refuses at driver construction, and one seed
run twice in one process gives equal hashes.

### IN-07 · `36` · loop-resident computation modules, settlements first — design · SE/IN · gate a design of what each computes (Jordan's); `30` built · `opus`/`opus` · `[design]`
- STATE: B (design)      LANE: IN (SE)      BATCH: design B-C · build B-T (entry gate: B-S merged: `loop/matter.py`, `state/carriers.py` and `module_contracts.yaml` are serial)      R: —
- WHAT: the spec carried below; heir of the retired SE staging rows (`SE-02` = IN-07).
- DEPS: IN-07 → SE-02, SE-04 (D)      EDITS: `step_call`/`query` extractions from `state/gate.py`, `queries/world_q.py`, MATTER; the host bodies deleted
- EXIT: per extraction, the old host body gone (`rg` its symbol) and both hashes unchanged (each read on B-T's base commit)      FALSIFIER: deleting the module's composition row refuses at driver construction; one seed run twice in one process gives one hash (below)
- SOURCE: `engine/season/loop/effects_governance.py:308-347`; carried below, `v8_part5.md:354-361`:

**Grade:** `paper`. Nothing is built before its design says what the module computes. Extract the rules living today
in the gate (`state/gate.py`), `world_q` and the MATTER step into `step_call` and `query` entries with a typed input
and output (A-25); the verb adapters and every MATTER write stay host. Also owns the levy-to-mass-battle feed:
`levy` moves stores, not troops (`loop/effects_governance.py:308-347`), and a season field is one troops-sized
subunit (J-18). IN-49 (`_part5`, B-F) builds `levy`'s question source (H-163 limit 3); the feed from `levy` to a field's troops is this design's.
**FALSIFIER per extraction.** Both hashes unchanged; the rule's old host body is gone (one owner — `rg` its symbol);
deleting the module's composition row refuses at driver construction; one seed run twice in one process gives one
hash.

### §SM open items — owners as v9 adopts them

Carried from `v8_part5.md:365-381`, the owner column re-pointed to the v9 handle and, where Jordan's own words bear on a row, stating them with their date and source (SM-1, SM-2, SM-3, SM-5, SM-6, SM-12, SM-15). Closed at adoption, rows deleted: `SM-4` (the file stays: ED-IN-0283, A-25's legacy home); `SM-8` (a standing fact, stated in §4.3's preamble); `SM-14` (its mitigations are IN-02's roster, IN-04's workbench falsifier and SM-7 at IN-05).

| # | item | owner |
|---|---|---|
| `SM-1` | which module owns the proceedings verbs (`convene` `open_case` `determine` `petition`, `_req_convene`, `arrangements.yaml`); until ruled they stay host | HELD — Jordan's indirect leans conflict (2026-09-06: a new verb "likely belongs in the main system", event e05ed737, against "create the correct verb for the subsystem", event 11b42093); ask-then after SC-01: SC-06 (`_part6`) |
| `SM-2` | `2-ii`, deleting the kernel `systems/social_contest/sim/contest/`, stays HELD | ask-then after SC-01, for the TIMING only: SC-05 (`_part6`); the end state leans adopt, as SM-15 |
| `SM-3` | J-22 option A: fieldwork is a container that is not a `contest()` and needs a second role in `_ROLE_ROSTERS` (`manifest/registry.py:25`) | CONFIRMED in Jordan's words (2026-09-05, event 0d3e3b74): "investigation is not a contest seam. it is its own thing." — FI-02 (`_part6`) |
| `SM-5` | whether a grid or map variant is a MODE of one module (A-25's assumption) or a container of its own | CONFIRMED BY JORDAN'S WORDS: the grid/map version and the duel version are two playable modes of ONE combat engine with no second resolver — "a grid map-based version where you choose to attack and then in fire emblem style you see the bout, but it's my personal combat engine resolving there for a round — and then a duel version where you actually decide at each step/beat" (`proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`); A-25's `[ASSUMPTION]` is his stated intent, and J-11's residual (R-04 conjunct 3) reads "mode" |
| `SM-6` | the suspension design for a playable mode (ENCOUNTER, `04:177`, the nearest precedent) | IN-46 (§4.2: design in B-C, re-read at B-L; SM-5's confirmation does not answer it). No build batch exists, so R-04 conjunct (3), hence M1, cannot read `met` until one does |
| `SM-7` | a test asserting `modules/**` equals the reachable closure in both directions (licensed by `CLAUDE.md` §0.1 pt 5, as `modules/` is the port's input set; recommended, not ruled) | IN-05 (built at `31c`, B-L) |
| `SM-9` | `decline_note:` declines an effect on some rows and a formation on others (`oblige`, `destroy_record`); `30`'s refusal (a) stays one-sided until the column is split | IN-41 (B-B) |
| `SM-10` | Layer-0/Layer-1 text this plan does not edit: `CLAUDE.md` §3, `:407`, `:410`, `:514`; `CURRENT.md:22` and `:41` (the Dice / resolution head still names `engine/autoload/dice_engine.py`, and the currency stamp predates six heads); `04:1000`; `architecture/PLAN.md:1271`; `architecture/VOCABULARY.md:125` | Jordan (IN-44, `_part8`) |
| `SM-11` | the precondition twin of refusal (a): a declared-absence column, then a refusal, for a verb whose untyped precondition nothing evaluates (`driver.py:125-127`) — it was retired `32`'s | IN-41 (B-B) |
| `SM-12` | holonic's `[engine]` tag (defined `:75`; e.g. `:1633`, `:1716`, `:1769`) means the Godot engine and collides with *engine* = the season loop | Jordan (Layer 1; IN-44, `_part8`). For him beside it: his 2026-09-17 preference "please ensure holonic shape for things like decision making so that they aren't directly in season loop" (event 6ef0472d-f017-413f-8470-5ed0e9d02d68) predates A-25 (ED-IN-0284/0285, 10-03), which keeps `decision/` host; the later governs |
| `SM-13` | at the port, each module's path is listed in the generated manifest resource, so export packing sees the targets `load()` resolves by string | GO-05 (`_part7`) |
| `SM-15` | adopt the kernel as the social contest container's automated mode, or keep the interim provider | SC-05 (`_part6`). Jordan LEANS TO ADOPT [medium] (indirect, 2026-09-06: "this subsystem obviously owns all social contests", event 8db01756-69f0-4c2e-9c35-4ad7e544efe4; "orphaned social contest code: retire it", event cd6428c4): end state, the proceedings subsystem owns all social contests and the orphaned `contest/` code retires; the timing stays ask-then after `22`'s measurement |

## Batch exits (B-A, B-B, B-C, B-E, B-L)

The batch table — members, order, entry gate, exit instrument, full-suite close, lanes — is `_part3` §B, its one copy; this part does not repeat it. B-A's structural check is `grep -c '^## Status:' workplans/valoria_master_workplan_v9*.md`, each file reading 1: `tests/valoria/test_single_status_line.py` walks only `.designs/systems` (`:60`, `:87`) and cannot see a workplan.
