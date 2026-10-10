# Valoria — Master Workplan v9, part 4: IN lane I — B-A and B-L (adoption, the module stages §SM), what B-C and B-E left open (the telling tail's G5, G8), the re-plug builds and the mode designs' reviews

## Status: part of v9 — see `workplans/valoria_master_workplan_v9.md`
## Reads after `workplans/valoria_master_workplan_v9_part3.md`; IN lane II (IN-08..13, 21–23, 26–28, 30–38, 40, 45, 48, 49, 51) is `_part5`.
## Grade under `CLAUDE.md` §0.2: `paper`. Line numbers drift; re-derive every site by its symbol before editing it.

---

## 4.0 How to read this part

- **Home of** IN-03..07, 14, 18, 46, 47, 52; each full entry lives here once. Aliases resolve here: `PC-09` = IN-04 (`31b`), `MB-09` = IN-05 (`31c`), `SE-02` = IN-07 (`36`), `SM-6` = IN-46. IN-06 (`33`) is the re-plug half of `FI-05` and `WR-05`; their reader halves (IN-32, IN-35) are `_part5`'s.
- **Entry fields.** `STATE` (`B` buildable · `BLK:<ids>` · `J:<id>` · `ask-then:<id>`) · `LANE` · `BATCH` (`_part3` §B: B-A … B-Z; a late position is slotted by §B.0's rules R1–R9) · `R` (THE NINE rows moved, `_part2`) · `WHAT` · `DEPS` (D data · F file-collision · I instrument · J Jordan-gate · R ordering-by-ruling; `_part3` §A) · `EDITS` (`_part3`'s collision matrix) · `EXIT` · `FALSIFIER` · `SOURCE`.
- **The four designs landed at B-C** as PROPOSED documents under `proposals/2026-10-07-*.md` (never `.designs/` or `systems/`, `CLAUDE.md` §1, §3), each HELD BACK from ratification-on-merge (ED-1094) until its review. What remains of IN-06 and IN-07 is the build (B-S, B-T; §4.5); IN-46 and IN-47 have no build position until their designs are reviewed (§4.2; their entries say what the review adds).
- **Carried blocks** follow the line that names their source lines, and are the source's words. The only edits: a citation of a retired plan file re-pointed to its v9 handle or its `FORK:` ref; a spent clause or closed row deleted; v8 position numbers kept as aliases. The source files retire at adoption (ED-IN-0286): `v8_part5.md:L` and `telling:L` (`workplans/2026-10-01-telling-workplan.md`) read at that `FORK:` ref.
- **Prose is reference (`CLAUDE.md` §0.05).** No entry is the reason a behaviour is correct; each names the instrument that shows it. A figure here carries the command that re-derives it and the date it was read; re-run before relying on it.

## 4.1 B-A — ADOPT

Members, entry gate and exit instrument: `_part3` §B. B-A is the adoption patch (`_part8` §K). The one-line CI fix that had left `main` red (`personal_combat` joining `RETIRED_CONTRACTS`, `tests/valoria/test_flow_skeletons.py`) is built — `7b619328` on the adoption branch, 95 passed — so it is not a position here (`CLAUDE.md` §2: finished positions leave the plan); `main` reads green once the branch merges.

## 4.2 What B-C left open — IN-14, IN-46, IN-47

B-C (INSTRUMENTS + RECORDS) is closed; its finished positions left the plan and the commits are their record (`CLAUDE.md` §2). Three positions here outlive it: IN-14 (part-finished at B-B, ask-then) and the two mode designs that landed at B-C and wait on a review with no build batch (IN-46, IN-47). IN-50, diagnosed at B-C, landed at B-I (`5fa6ac16`). The IN-06 and IN-07 designs also landed at B-C; their builds are §4.5's.

### IN-14 · BOUND-ATTENTION (H-92, H-10) · `budget()` counts `granted_acts`
- STATE: ask-then      LANE: IN      BATCH: B-Z (asked when this position is next scheduled)      R: —
- WHAT (narrowed at B-B's close, `4a2e4494`): MEASURED, NOT LANDED. Counting only `t.granted_acts` takes the 27 NPC-rung lane cases (seed 0, 3 seasons) from `attempt_cases` 20 to 12, below `test_n3`'s floor of 15 (it reads `assert 12 >= 15`, and R-03's `test_u2_the_one_round_arm_reproduces_the_pre_tick_loop` goes red with it); excluding only holds over a Record gives 13, still red, so the loss is H-92's records-mint-budget: the NPC telling transport runs on the budget those holds mint. The figures and the arms are in H-92's cite (`engine/season/hole_register.yaml`). What remains is the repair's SHAPE, which H-10 calls a design call with three defensible forms (more rounds, denser rounds, or a fixed slate of scene-slots office cannot widen), put as an ask-then row in `_part5` §J.2; once ruled, land the change in `budget.py` and re-take `test_n3`'s floors.
- DEPS: the ask-then row (`_part5` §J.2) → this position      EDITS: `engine/season/decision/budget.py`, shape pins
- EXIT: `python -m pytest engine/season/tests/test_season_shape.py -q -k test_n3` green with its floors unchanged; `build_realm(0)` hashes declared if they move (a hash mover if the budget moves: declared at the batch that builds it)      FALSIFIER: one live `hold` moves releasable scenes by one, control is today (#457 `:166`); a landholding with no granted act buys no scene
- SOURCE: `registers/handoffs/HANDOFF_IN.md`, the row beginning "Build-order item 4 REVERTED"; `engine/season/hole_register.yaml:166` (H-10), `:1142-1147` (H-92); `engine/season/decision/budget.py:18`; `engine/season/tests/test_season_shape.py:8645, :8789`

### IN-46 · = SM-6 · the grid mode's suspension at ENCOUNTER's barrier — design landed, review open
- STATE: B (review)      LANE: IN (PC)      BATCH: no build batch; the design is re-read against the moved `combat` container at B-L (a tail lane)      R: R-04 (conjunct 3: the `scales:` row "personal combat / grid-based map combat with units")
- WHAT: the design `SM-6` owes (§SM table) landed at B-C: `proposals/2026-10-07-grid-mode-suspension.md` (PROPOSED; HELD BACK from ratification-on-merge until the B-L re-read). It answers the four questions with a `file:line` per site: (1) the driver suspends at ENCOUNTER (`loop/driver.py:459-460`, `loop/encounter.py:72`) and only at the engine call (`seam/wrappers/combat.py:177`); (2) the scene is a call-out, so the driver's stack holds the state and no token or draw is minted while suspended (the draw ordinal resets per tick at `loop/driver.py:423`); (3) the typed input and output are the pair AUTOMATED already uses (A-25); (4) PLAYABLE and AUTOMATED are replay-equal under six stated conditions. The player's choice set `{engage, withdraw}` is an [ASSUMPTION]. SM-5 stands confirmed by Jordan's words (`proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`; RS-6): two modes of ONE engine and no second resolver; the design decides neither of #445 `05`'s held questions (J-15, ask-then at PC-08). **Found at B-C, for the build:** `fight` is fought at RESOLVE today (the body prize has no `step:`, `rosters.yaml:1107-1110`, read at B-C), so the build gives `fight` `march`'s ENCOUNTER/Declared pair; the per-turn choice parameter lands in the combat engine's `fight`, a THIRD file the entry did not list — `systems/combat/combat_engine_v1/wrapper.py`, under `modules/combat/` once IN-04 moves it (B-L); deferring every fight moves the hash of any seeded season that fights, so the build re-records the seeded goldens and says so. Line cites corrected at B-C: the draw-ordinal reset is `driver.py:423` (the plan had `:415`); A-25's `driver.py:330` is `:355`.
- DEPS: IN-04 (B-L) → the re-read (the moved container); IN-47's carriers where a party is built from a person      EDITS: the re-read, the proposal only; the build, once batched: `loop/driver.py`, `seam/wrappers/combat.py`, the combat engine's `wrapper.py` (`modules/combat/` after B-L), the seeded goldens
- EXIT: the design re-read against the moved `combat` container, each site's `file:line` re-derived. **No build position exists, and R-04 conjunct (3) needs every `scales:` row `in_loop`** (`engine/season/requirements.yaml:70-189`; this row `:142-154`, `in_loop: "duel only, via combat_seam.py"`), so R-04, hence M1, cannot read `met` until a build batch exists for IN-46 and IN-47. Once the design is reviewed, `_part3` §B.0 R4/R7 place the build      FALSIFIER: at the build, one seeded season run twice — AUTOMATED, and PLAYABLE with scripted choices equal to the chooser's — ends at one `World.content_hash()`, and a scripted choice that differs from the chooser's moves it (the instrument can fail); a suspension that consumes a draw or mints a token twice reds the first
- SOURCE: `proposals/2026-10-07-grid-mode-suspension.md`; `proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`; `architecture/meta/04_CODE_ARCHITECTURE.md:177`; `engine/season/requirements.yaml:142-154`; `engine/season/loop/driver.py:355, :423`; A-25 (`_part5` §A); §SM, SM-5 and SM-6

### IN-47 · the character-sheet management space (creation, development, chronicling) — design landed, review open
- STATE: B (review)      LANE: IN (PC, WR)      BATCH: no build batch; reviewed against IN-08's carriers at B-H (closed `c13144b9`)      R: R-04 (conjunct 3: the `scales:` row "character creation / development / chronicling")
- WHAT: the design landed at B-C: `proposals/2026-10-07-character-sheet-spaces.md` (PROPOSED; HELD BACK from ratification-on-merge until the B-H review; the PR body lists it as held back). Each space names the typed input it reads, the acts it emits and the carrier each reaches through the fold, never a direct write: **creation** — no act; a cast entry the world-gen builder seats (`04:1153`); a mid-campaign person is CENSUS's `(Person, exists)` row, triggered by H-51 (SE-01's, B-F); **development** — the player's own `View`/`Question`/`Candidate`, acting into the chooser slot (`loop/driver.py:355`); `stance` and `body` have live writers, `scar`'s writer does nothing at `scar_step=0`, `capability` and `pursuits` have none until IN-12 step 9 builds `train` and `argue` (B-Q); **chronicling** — no act and no field; a `LedgerReader` view, the `causes[]` render outside the game. **REVIEWED at B-H (2026-10-08), verdict PASSES WITH CORRECTIONS, recorded in the proposal's `## Review at B-H`:** no space writes a `Person` field outside an act's fold, so the FALSIFIER does not fire; creation arm C1 cannot be carried out through the cast shape (no `pursuits` key; `corpus_run.py` `CAST_KEYS` is closed) and takes its own fallback (the player picks a person the builder already seated; the playable `choose` dispatches on `p.id`); the carrier claims were stale and are corrected (`Person.conviction` exists, filled by the realm builder only, `{}` for every shipped person; `Person.scar` is written by the fold's `_scar_witnesses` and read by `crisis_weights` and `conviction_after_crisis`; neither writer emits an Event, so chronicling cannot see a scar or a crisis). The hold on ratification-on-merge is released only by Jordan.
- DEPS: IN-08 → the review (D, landed `c13144b9`: `Person.scar`, `Person.conviction`); IN-47 ↔ IN-12 step 9 (R: `train` is the capability writer #445 K-4's `practice` verb was)      EDITS: the review, the proposal only; the build, once batched: `decision/` and `state/carriers.py` (a space that emits acts)
- EXIT: the design reviewed against IN-08's carriers as they stand after H10. **No build position exists, and R-04 conjunct (3) needs every `scales:` row `in_loop`** (`engine/season/requirements.yaml:70-189`; this row `:71-82`), so R-04, hence M1, cannot read `met` until a build batch exists for IN-46 and IN-47; `_part3` §B.0 R4/R7 place it once the design is reviewed      FALSIFIER: a space that writes a `Person` field outside an act's fold contradicts A-25 and Layer 1's "a module with no token cannot write" (`architecture/meta/04_CODE_ARCHITECTURE.md:158`) and fails the review; at the build, a creation arm switched off reproduces the pre-build hash
- SOURCE: `proposals/2026-10-07-character-sheet-spaces.md`; `references/what_valoria_is_and_what_runs.md:100-109`; `engine/season/requirements.yaml:71-82`; `proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md`; A-25 (`_part5` §A)

## 4.3 B-L — MODULES (§SM, carried from v8)

Members, order, entry gate and exit instrument: `_part3` §B. B-L is IN-03 → IN-04 → IN-05, then the tail lanes MB-03 and MB-05r, PC-06 M-1 and S-2/L-1, GO-04, with IN-46's design re-read against the moved `combat` container. It is placed after B-K, so THE NINE move first: nothing in B-G..B-K reads a module, and SC-01 (IN-03) and IN-13 (IN-05) are the positions that do; Jordan may run B-L right after B-D with no edge broken. Entry gate: B-B closed (`4a2e4494`; IN-02's falsifiers observed, E17), B-D1 closed (`9054df80`: the PC lane's edits to the combat closure landed) and B-D2 closed, `b31d2c31`, so that every lane edit to the two closures lands before the move (B-D2: MB-01, MB-02, MB-05, MB-06, MB-07, MB-04, each at its pre-move paths). The section's standing preamble, carried from `v8_part5.md:125-171`:

**Ruled:** `ED-IN-0284`, revised by `ED-IN-0285`. The vocabulary, directories, adapter model, module entry kinds,
containers and the retained-modules roster are **`A-25`** (`_part5` §A), stated there once; this section stages the code
and restates none of it.

**Order:** `30` → `31a` → `31b` → `31c` → `22` (SC-01, `_part6`; B-N). `33` and `36`'s designs landed at B-C (§4.5); their builds are B-S and B-T. **Retired ids, never reused:** `31d`, `31e`, `32` (cancelled before anything built them).
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
include IN-08, IN-34 and SC-03a's docket items, and PC-02..04 moved them at `9054df80` — so each stage's control is the reading on ITS OWN base
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
- STATE: B      LANE: IN (SC)      BATCH: B-L (head)      R: —
- WHAT: the spec carried below; creates `modules/`. Its entry gate is B-L's (B-B closed, `4a2e4494`; B-D1 closed, `9054df80`, and B-D2 closed, `b31d2c31`; after B-K unless Jordan runs B-L early).
- DEPS: IN-02 (landed `5097e49`) → IN-03 (R, satisfied); IN-03 → IN-04 (R); IN-03 → SC-01 (R: E17/A-25 — `22` builds its provider on this typed input record; SC-01 is B-N, so B-N's entry gate is B-L merged); IN-03 → PC-06 S-2 (D; a B-L tail lane)      EDITS: `rosters.yaml`, `seam/wrappers/sigma.py`, `module_contracts.yaml` + `composition.json`, `manifest/`, shape pins
- EXIT: both control hashes unchanged (re-read on the base commit) and falsifier (3) observed in a fresh subprocess      FALSIFIER: (1)–(5) below; (3) is `30`'s falsifier (2) (`tests/valoria/test_module_registrar.py`) in its fresh-process form
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
- STATE: BLK:IN-03 (PC-02, PC-03, PC-04 landed, `9054df80`)      LANE: IN (PC)      BATCH: B-L (after IN-03)      R: —
- WHAT: the spec carried below; the `sim_params.json` decision is made in this commit; SEAM-LADDER (#457) folds into item 5's T-k reading (`architecture/meta/03_VERBS_AND_LOOPS.md:286`).
- DEPS: IN-03 → IN-04 → IN-05 (R); IN-04 → PC-06 M-1 (D; a B-L tail lane); the F edges from the PC lane's edits to the closure (PC-01..04, PC-07, PC-05 item 3) are satisfied, all landed at `9054df80`, so the control hashes are read on B-L's base commit, after PC-02/03/04 moved combat outcomes      EDITS: `seam/wrappers/combat.py`, `seam/ladder.py`, `module_contracts.yaml` + `composition.json`, shape pins, the `systems/combat` move
- EXIT: both hashes unchanged; `balance.py` runs; one seed run twice in one process gives one hash      FALSIFIER: (1)–(5) below, and (6): IN-08 (B-G, `0f998f64`) added `accept` with `contests: "the body"`, which the prize row `"the body"` already claims (`rosters.yaml` `prizes:`), while this stage's composition row names `verb: fight` and the registrar's `verb:` names one verb — after the split `aperture 4 0` shows `accept` still reaches the one `combat` provider, and whether a second `verb_call` row is needed is read at the split [GAP: the contested-verb check resolves by prize (`loop/driver.py:182-192`), so `accept` is claimed; whether the composition row must also name it (A-25: the prize row and the composition row are the two owners; `manifest/registry.py:104-111` states the one-`verb:` shape) was not traced]
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
- STATE: BLK:IN-04      LANE: IN (MB)      BATCH: B-L (after IN-04)      R: —
- WHAT: the spec carried below. SM-7's test — `modules/**` equals the reachable closure in both directions — lands here (licensed by `CLAUDE.md` §0.1 pt 5: `modules/` is the port's input set).
- DEPS: IN-04 → IN-05 (R); IN-05 → IN-13 (F: `seam/wrappers/mass_battle.py`; IN-13 is B-M), IN-05 → MB-03 (F: `massbattle.py`; a B-L tail lane); the B-D2 edits to the closure (MB-01, 02, 04, 05, 06 and MB-07, J-18 (A)) are satisfied, each built at its pre-move paths and landed at `b31d2c31`; IN-05 → GO-05 (D: the manifest resource lists `modules/**`)      EDITS: `seam/wrappers/mass_battle.py`, `module_contracts.yaml` + `composition.json`, shape pins, the `systems/mass_battle` move
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

## 4.4 What B-E left open — IN-18's G5, G8 and the ties row

B-E (TELLING + SCORE) is closed (`ac9724fc`); its finished positions left the plan and the commits are their record (`CLAUDE.md` §2): IN-16, IN-17, IN-15, IN-25, IN-22's reach half and its paying half (`_part5`), PC-06 S-1 (`_part7`), and IN-18's step 2a, G1, G2 and G3. IN-18's G6 landed at B-I (`66bf51f9`; dormant in play, `engine/season/hole_register.yaml` H-204). What outlives it is IN-18's tail, below: G5 at B-I (gated on IN-10's `oblige`, H-203), G8 gated by judgment, the ties row at IN-32. T0–T6 are built (#449); their *As built* text stays at the telling workplan's `FORK:` ref. The shapes G5 and G8 build on, carried from `telling:50-61` (paths under `engine/season/`):

| thing | shape | owner |
|---|---|---|
| `Said` | `NamedTuple(subject: str, predicate: str, value: Any, confidence: int, chain: tuple[str, ...], circle: tuple[str, ...] \| None)` | `state/carriers.py` |
| `Claim.chain` | `chain: tuple = ()`, origin first, replacing the `teller` field; `teller` becomes a property, `chain[-1]` or `None`; hops = `len(chain)` | `state/carriers.py` |
| told deposit | `chain = said.chain + (act.actor,)`; `visibility` stays `"own"`; confidence raw | `loop/witness.py` |
| `tell` row | `requires_typed: {all: [{form: own_ledger, of: subject, conjunct: holds}, {form: relation, of: to, relation: with, conjunct: hearer}]}`, `counterparty: to`, `emits_on_refusal` keyed `holds`/`hearer` → `news.untold` (precedent: `issue`) | `verb_table.yaml` |
| `known_persons` | ids from truthy `exists:Person` claims, `Seen.who`, told `chain[-1]`; minus self (the topic is kept since step 2a, `ac9724fc`) | `queries/person_q.py` |

### IN-18 · G5, G8 · the gated tail (step 2a, G1, G2, G3 landed at B-E, `ac9724fc`; G6 at B-I, `66bf51f9`)
- STATE: G5 BLK on `oblige` forming (IN-10's sub-step (a), B-I), so on a source of claims about seats (`engine/season/hole_register.yaml` H-203; no position schedules it); G8 gated by judgment (§6); the ties row is IN-32's      LANE: IN      BATCH: B-I (G5; `_part3`'s B-I members and card list it)      R: —
- WHAT: the §5 rows still open, the §6 branches they read and the §10 judgments, carried below; the judgments are recorded, not ruled by Jordan, and reversible (G8 letters gated; self-disclosure allowed; private whispers not built). In the carried text "Batch 2" is the telling workplan's (T4–T6, landed in #449); v9's batches are the B-letters. Landed at B-E (`ac9724fc`): step 2a, G1 (live, `judged_gain` and `told_valence_gain` at 0.5, H-192, H-193), G2, G3; G4 dropped; G7 recorded, H-198. CARRY-INTERIOR's falsifier (#457 `:161`) reads G1's landed regard-at-read at IN-13's fought field (B-M; `_part5` IN-13). **The one declared exception to "gate and trigger text carried unchanged":** §5's ties row re-points its prerequisite from plan `14` to IN-32; every other gate and trigger cell is the source's.
- DEPS: IN-10's `oblige` sub-step (a) → IN-18 G5 (D; B-I)      EDITS: G5: §5's marker site `_from_inferred_claim` names no symbol in the tree read at B-E's boundary — re-derive it at B-I by grep before editing
- EXIT: per gate, §5's falsifier column, observed at B-I. (G1's EXIT, the R-07 realm reader `_part2` R-07 defines, ran at B-E's exit: `engine/season/tests/test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone`, whose docstring cites this EXIT.)      FALSIFIER: G5 — an obligee forms a `tell` to the seat holder, and without `oblige` none (§5 row G5)
- SOURCE: carried below, `telling:297-316` (§5 GATED):

**The rule.** A field lands only in the same commit as its reader and its falsifier; an unfleshed
element is recorded by an `absent` row in `hole_register.yaml` plus a field-less `# ABSENT: H-NNN`
marker where it will go, never a dead carrier or a raising stub. §0.1 pt 5 forbids a guard over them,
so each trigger is a figure an existing instrument prints.

| ID | element | prerequisite | trigger | falsifier | marker site |
|---|---|---|---|---|---|
| — | ties | IN-32 (`_eff_tie`, `_part5`) | `aperture 1 0`: `tie / knot` executed > 0 | IN-32's | none here |
| G5 | duty to report | T4 | M0e > 0 | an obligee forms a `tell` to the seat holder; without `oblige`, none | `_from_inferred_claim` |
| G8 | letters | T4 | none; ahead of T5 if M0d < 20% | `create_record(letter)` + `give` deposits the said triple as `told_by`, chain ending in the maker | beside the `content:` deposit |

Rows G1, G2, G3 landed at B-E (`ac9724fc`); G6 at B-I (`66bf51f9`); G4 dropped; G7 recorded, H-198.

Other `absent` rows and triggers: `stake` (M0h > 0); a default-obstacle sweep (M0i after T4 no higher
than at T0); `Seen.who` as a source (only if M0d counts zero from it); sanctioned silence (`date.fired`
reaching WITNESS, plan position `22`).

§6 M0 branches, carried from `telling:320-324`:

- **M0a ≈ 0:** G3–G7 wait; re-measure after T4 (it produces person subjects). Still zero: record on H-62; invent nothing. **Re-measured after T4: M0a > 0 (realm person-subject executed 2 of 3), so the G3–G7 trigger is met.**
- **M0b ≈ 0:** at `declared` only, G1 ships at control, or `deed:` cells are authored under H-66 in its commit; at both arms, G1 does not land. **Not taken: M0b read 36.4 % at `declared`, so G1 landed at B-E (`ac9724fc`) with no `deed:` cell** (kept because `queries/person_q.py`'s `deeds_judged` docstring cites this branch).
- **M0d ≈ 0:** T4 lands, its `test_n3` re-pin is refused, and G8 moves ahead of T5 as the main channel.
- **G8 branch, taken as a judgment, not a rule:** realm M0d 12% < 20%, which licensed G8 ahead of T5; T5 landed first, and G8 stays gated.

§10 decisions still standing, carried from `telling:378-382`:

| # | decision | recommendation |
|---|---|---|
| 1 | **Private whispers** (heard only by the person told). Jordan's alone: it voids T-e (recipiency computed at WITNESS from presence) and T4 is redone | Do not build; absent that wish, nothing escalates |
| 3 | **Self-disclosure** (A tells B about A) | Allow: skip self-subjects only on rows without a counterparty; with `to` as opponent it is not self-contest, and `to == p.id` is still declined |

## 4.5 Re-plug builds — designed at B-C; built at B-S (IN-06) and B-T (IN-07), with the levy-to-field feed (IN-52) after B-T's extractions

IN-46 and IN-47, the other two designs that landed at B-C, sit in §4.2: they have no build batch.

### IN-06 · `33` · the unplugged systems — build (design landed at B-C) · IN/WR/FI · gate A-11, A-20; `30` built · `opus`/`opus`
- STATE: B (build)      LANE: IN (WR, FI)      BATCH: B-S (the design is re-reviewed after B-G/B-H (closed: `0f998f64`, `c13144b9`) before B-S opens, because it names carriers IN-08 creates)      R: —
- WHAT: the design landed at B-C: `proposals/2026-10-07-unplugged-systems-replug.md` (PROPOSED; HELD BACK from ratification-on-merge until the post-B-G/B-H re-review). Per module: knots (`systems/fieldwork/sim/knots.py:155-156`; AX-4 at D-3 and D-10; the strain gauge's home is still unlocated and H-182 leaves it to IN-32, so two candidates are listed, none picked), conviction (`systems/characters/sim/conviction.py:82`; `Person.scar` is keyed per axis while the code keys scars by Conviction name, and IN-08 re-axes 4 → 7, so nothing maps one to the other yet), threadwork (coherence state and rng fallbacks; `(Person, coherence)` has a write-matrix row, `write_matrix.yaml:178`, but no field on `Person` — H-47's "no write-matrix row" is stale), `ms_track` (writes `world.clocks`, which the season `World` lacks: no carrier as written), and the rendering stubs (struck at position 27). Carriers IN-08 creates are marked to-be-confirmed at the re-review. Absorbs A-24's threadwork question, the WR remainders' seam, FI's knots half (FI-05) and H-47. **Found at B-C, for B-S's opener:** (1) **B-S's entry gate is stated inconsistently** — this entry said B-R, B-F and B-D3 merged; WR-01 and PC-06 (`_part7`) say B-R and B-V; `_part3` §B.1's B-S row lists B-R, B-V, B-F and B-D3. Not reconciled here: the B-S opener reconciles it before opening. (2) The move of each closure into `modules/` was missing from EDITS (added below); SM-7's test fails on a target left in `systems/`. (3) The deletion falsifier has no mechanism yet for `query` and `step_call` rows; the design proposes, as an [ASSUMPTION], that the host consumer declares the role it calls and the registrar refuses a declared role with no row. (4) No composition row can land before its caller (`references/module_contracts.yaml:40`). (5) `Person.conviction` must be named at the re-review (the design omits it until then). (6) The three design accounts of the deletion-refusal seam (IN-06, IN-07, IN-03) are reconciled at B-S/B-T. Not opened at B-C: `decision/options.py`'s regard; whether `test_build_realm_determinism`'s two runs share a process.
- DEPS: IN-06 → WR-01's `engine/season/` reach, IN-32, IN-35, PC-06 K-3 (D: the design names the carriers; all B-S); IN-08 → IN-06's re-review (D, landed `c13144b9`: `Person.pursuits`, `Person.conviction` and the scar counts as the cells commit and the chain leave them)      EDITS: composition rows (`module_contracts.yaml` + `composition.json`); the store-shed in each module; the move of each re-plugged closure into `modules/` (SM-7)
- EXIT: the design re-reviewed after IN-08's cells and chain (B-G, B-H; closed `0f998f64`, `c13144b9`), naming the carriers as they stand; at build (B-S), a plugged row's deletion refuses at driver construction (fresh subprocess)      FALSIFIER: one seed run twice in one process gives equal hashes (below)
- SOURCE: `proposals/2026-10-07-unplugged-systems-replug.md`; `engine/season/hole_register.yaml` H-182, H-47; carried below, `v8_part5.md:339-350`:

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

### IN-07 · `36` · loop-resident computation modules, settlements first — build (design landed at B-C) · SE/IN · `30` built · `opus`/`opus`
- STATE: B (build)      LANE: IN (SE)      BATCH: B-T (entry gate: B-S merged: `loop/matter.py`, `state/carriers.py` and `module_contracts.yaml` are serial; the design reviewed)      R: —
- WHAT: the design landed at B-C: `proposals/2026-10-07-settlements-computation-modules.md` (PROPOSED; its levy-feed items HELD BACK for Jordan). It designs six extractions — E1 `larder_draw` + `drawn_under` (a `query`, `queries/world_q.py`), E2 `subsist` (a `step_call`, MATTER, `loop/matter.py`), E3 `produce` (`matter.py`), E4 housing, E5 fabric, E6 fortification (`world_q.py`) — each naming the host body to delete (a symbol to `rg`), its typed input/output and its falsifier; and a shared `require_entries` function, because the registrar refuses only a role it already holds (`manifest/registrar.py:114-120`), so deleting a `step_call` or `query` row would otherwise refuse nothing. Heir of the retired SE staging rows (`SE-02` = IN-07). **Found at B-C:** nothing is extracted from `state/gate.py` (every rule there decides who may write a Tenure, and the gate never reads stores), so it leaves B-T's EDITS; the levy-to-field feed is NOT part of this build — it is IN-52 (below), after these extractions. **Open, reconciled at B-S/B-T:** A2 (a module looked up by role string through `composition.require`) differs from IN-03's `MODULE_ENTRIES` path, and the document gives a revert; the three design accounts of the deletion-refusal seam (IN-06, IN-07, IN-03); the corpus-hash instrument the document names is [UNVERIFIED] (`harness/corpus_run.py` has only R4's same-seed comparison).
- DEPS: IN-07 → SE-02, SE-04 (D); IN-07's extractions → IN-52 (D)      EDITS: `step_call`/`query` extractions from `queries/world_q.py` and MATTER (`loop/matter.py`); the host bodies deleted; the composition rows; the shared `require_entries` — not `state/gate.py`
- EXIT: per extraction, the old host body gone (`rg` its symbol) and both hashes unchanged (each read on B-T's base commit)      FALSIFIER: deleting the module's composition row refuses at driver construction; one seed run twice in one process gives one hash (below)
- SOURCE: `proposals/2026-10-07-settlements-computation-modules.md`; carried below, `v8_part5.md:354-361` (the gate clause and the levy-feed sentences struck at B-C: the gate yields no extraction, and the feed is IN-52's):

**Grade:** `paper`. Nothing is built before its design says what the module computes. Extract the rules living today
in `world_q` and the MATTER step into `step_call` and `query` entries with a typed input
and output (A-25); the verb adapters and every MATTER write stay host.
**FALSIFIER per extraction.** Both hashes unchanged; the rule's old host body is gone (one owner — `rg` its symbol);
deleting the module's composition row refuses at driver construction; one seed run twice in one process gives one
hash.

### IN-52 · the levy-to-field feed · levied stores provision a season field (split from IN-07 at B-C)
- STATE: BLK:IN-49 (B-K), IN-07's extractions (B-T); the arm's flip is ask-then (`_part5` §J.2, LF-1..LF-3)      LANE: IN (SE, MB)      BATCH: B-T (tail lane, after IN-07's build, merging last)      R: —
- WHY B-T: it is the earliest batch whose entry gate covers all three D edges — IN-49 lands in B-K, MB-07 landed in B-D2 (`b31d2c31`, the cap shipped OFF), and the extraction the feed reads lands in B-T itself, so no earlier batch can hold it. §B.0 R1 would put a `march`-row edit in the verb cluster, but no V batch follows B-T, so it runs as B-T's tail lane (R9, §C.2). Shipping OFF, it moves no hash, so B-T's "hashes unchanged per extraction" still holds.
- WHAT: designed at B-C inside IN-07's document (`proposals/2026-10-07-settlements-computation-modules.md`, the feed section; HELD BACK): `levy` moves stores, not troops (`loop/effects_governance.py:308-347`), and a season field is one troops-sized subunit (J-18); a `settlements.provision` query feeds the field. The three [ASSUMPTION]s the design makes are Jordan's (`_part5` §J.2 ask-then): **LF-1** the feed bounds troops by the treasury, using the larder's ration; **LF-2** the defender's treasury is the nearest held rung's stores; **LF-3** the field consumes its ration from the treasury, written by `_eff_march`. The build ships the arm OFF behind a `field_provisioning` fixture; the flip waits on the answer.
- DEPS: IN-49 → IN-52 (D: `levy` executing); MB-07 (landed, `b31d2c31`) → IN-52 (D: how a season force scales: `support_weight` as shipped, the cap OFF; flipping it is MB-07r, a declared mover that re-pins any season-force reading, not a gate); IN-07 → IN-52 (D: the settlements module and its query); IN-05 → IN-52 (F: the moved mass-battle module, B-L)      EDITS: `seam/wrappers/mass_battle.py`, `loop/effects_combat.py` (`_eff_march`), the `march` row (`verb_table.yaml`), the moved mass-battle module (`modules/mass_battle/`), the `field_provisioning` fixture
- EXIT: with `field_provisioning` off, both hashes equal B-T's base; with it on, in a seeded season, a side's fielded troops are bounded by its levied treasury [ASSUMPTION: the EXIT, read from the design's feed section; re-read it there at B-T]      FALSIFIER: the off arm moves a hash → not off; on, a side with an empty treasury fields as many troops as a full one → the bound is not built
- SOURCE: `proposals/2026-10-07-settlements-computation-modules.md` (the feed section and its LF table); `engine/season/loop/effects_governance.py:308-347`; J-18 (`_part5` §J.1)

### §SM open items — owners as v9 adopts them

Carried from `v8_part5.md:365-381`, the owner column re-pointed to the v9 handle and, where Jordan's own words bear on a row, stating them with their date and source (SM-1, SM-2, SM-3, SM-5, SM-6, SM-12, SM-15). Closed at B-B, rows deleted: `SM-9` and `SM-11` (IN-41, landed `4a2e4494`). Closed at adoption, rows deleted: `SM-4` (the file stays: ED-IN-0283, A-25's legacy home); `SM-8` (a standing fact, stated in §4.3's preamble); `SM-14` (its mitigations are `30`'s roster, landed `5097e49`, IN-04's workbench falsifier and SM-7 at IN-05).

| # | item | owner |
|---|---|---|
| `SM-1` | which module owns the proceedings verbs (`convene` `open_case` `determine` `petition`, `_req_convene`, `arrangements.yaml`); until ruled they stay host | HELD — Jordan's indirect leans conflict (2026-09-06: a new verb "likely belongs in the main system", event e05ed737, against "create the correct verb for the subsystem", event 11b42093); ask-then after SC-01: SC-06 (`_part6`) |
| `SM-2` | `2-ii`, deleting the kernel `systems/social_contest/sim/contest/`, stays HELD | ask-then after SC-01, for the TIMING only: SC-05 (`_part6`); the end state leans adopt, as SM-15 |
| `SM-3` | J-22 option A: fieldwork is a container that is not a `contest()` and needs a second role in `_ROLE_ROSTERS` (`manifest/registry.py:27`, re-read at B-C) | CONFIRMED in Jordan's words (2026-09-05, event 0d3e3b74): "investigation is not a contest seam. it is its own thing." — FI-02 (`_part6`) |
| `SM-5` | whether a grid or map variant is a MODE of one module (A-25's assumption) or a container of its own | CONFIRMED BY JORDAN'S WORDS: the grid/map version and the duel version are two playable modes of ONE combat engine with no second resolver — "a grid map-based version where you choose to attack and then in fire emblem style you see the bout, but it's my personal combat engine resolving there for a round — and then a duel version where you actually decide at each step/beat" (`proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`); A-25's `[ASSUMPTION]` is his stated intent, and J-11's residual (R-04 conjunct 3) reads "mode" |
| `SM-6` | the suspension design for a playable mode (ENCOUNTER, `04:177`, the nearest precedent) | IN-46 (§4.2: design landed at B-C, re-read at B-L; SM-5's confirmation does not answer it). No build batch exists, so R-04 conjunct (3), hence M1, cannot read `met` until one does |
| `SM-7` | a test asserting `modules/**` equals the reachable closure in both directions (licensed by `CLAUDE.md` §0.1 pt 5, as `modules/` is the port's input set; recommended, not ruled) | IN-05 (built at `31c`, B-L) |
| `SM-10` | Layer-0/Layer-1 text this plan does not edit: `CLAUDE.md` §3, `:407`, `:410`, `:514`; `CURRENT.md:22` and `:41` (the Dice / resolution head still names `engine/autoload/dice_engine.py`, and the currency stamp predates six heads); `04:1000`; `architecture/PLAN.md:1271`; `architecture/VOCABULARY.md:125` | Jordan (IN-44, `_part8`) |
| `SM-12` | holonic's `[engine]` tag (defined `:75`; e.g. `:1633`, `:1716`, `:1769`) means the Godot engine and collides with *engine* = the season loop | Jordan (Layer 1; IN-44, `_part8`). For him beside it: his 2026-09-17 preference "please ensure holonic shape for things like decision making so that they aren't directly in season loop" (event 6ef0472d-f017-413f-8470-5ed0e9d02d68) predates A-25 (ED-IN-0284/0285, 10-03), which keeps `decision/` host; the later governs |
| `SM-13` | at the port, each module's path is listed in the generated manifest resource, so export packing sees the targets `load()` resolves by string | GO-05 (`_part7`) |
| `SM-15` | adopt the kernel as the social contest container's automated mode, or keep the interim provider | SC-05 (`_part6`). Jordan LEANS TO ADOPT [medium] (indirect, 2026-09-06: "this subsystem obviously owns all social contests", event 8db01756-69f0-4c2e-9c35-4ad7e544efe4; "orphaned social contest code: retire it", event cd6428c4): end state, the proceedings subsystem owns all social contests and the orphaned `contest/` code retires; the timing stays ask-then after `22`'s measurement |

## Batch exits (B-A, B-L)

The batch table — members, order, entry gate, exit instrument, full-suite close, lanes — is `_part3` §B, its one copy; this part does not repeat it. B-A's structural check is `grep -c '^## Status:' workplans/valoria_master_workplan_v9*.md`, each file reading 1: `tests/valoria/test_single_status_line.py` walks only `.designs/systems` (`:60`, `:87`) and cannot see a workplan.
