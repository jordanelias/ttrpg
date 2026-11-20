# Codebase improvement proposal — part 2: items CI-06 to CI-11, the deletion list, notes for v12

## Status: PROPOSED (part 2 of `master/CODEBASE_IMPROVEMENT_PROPOSAL.md`; nothing here is applied)

Reconciled: 2026-11-12, A-102 (lane `unified/work/A102_112_APPLIED.md`): CI-07 rewritten for the ruled destination `engine/season/boot/` (see its own line); §5 item 6 marked answered.

The form of each item, the baselines and the rules are in part 1, §1.

---

## CI-06 · The chooser is composed in one place

**Finding.** H-02. `engine/season/harness/probes.py::chooser` (`:278-292`) composes the shipped chooser
(`make_chooser` over the world's settings, the act-id mint and the per-person draw); its docstring says
`soak`, `interactions` and `storybar` *"still compose it by hand"*, and they do
(`harness/soak.py:267-269`, `harness/storybar.py:304-307`, `harness/interactions.py:238-241`).

**What dies.** Two hand compositions (six lines). **Preserved:** each instrument's chooser, draw for draw,
including `storybar`'s `draw_seed` arm (its docstring, `:295-299`: the seed replaces `w.world_seed` for the
chooser's draw *and nothing else*).

**Earning.** E4: `probes.chooser` is the one place the composition lives, and `soak` and `storybar` are
the two sites that would otherwise carry it. `interactions.py` is **left**: its `run` reads `mint` and
`draw` again below the composition (`:278`, `:288`, `:309` of that file: `CH.sample_order(..., draw)`,
`mint(p.id, ...)`, `attribute_top(..., draw, ...)`), so it needs the parts and not only the chooser; its
three lines stay and the owner's docstring says so.

**Exact edits, in order.**

1. `harness/probes.py::chooser`: signature `chooser(w, only=None, verbs=None, draw_seed=None)`; the `draw=`
   argument becomes `draw_factory(w.world_seed if draw_seed is None else draw_seed, lambda: w.tick)`.
   Docstring: the sentence about hand composition now names `interactions` alone and why.
2. `harness/soak.py:267-269`: replace the `mint = ...` and `ch = make_chooser(...)` lines with
   `ch = P.chooser(w, verbs=resolvable_verbs())`, importing `from . import probes as P`; drop the imports
   that fall unused (`make_chooser`, `H`, `draw_factory`, each only if no other line of the file reads it).
   The `w.fixtures = w.fixtures.sweep(...)` line stays **above** it (its comment: *"BEFORE the chooser"*).
3. `harness/storybar.py:304-307`: `ch = P.chooser(w, verbs=resolvable_verbs(), draw_seed=draw_seed)`; the
   same import care. `storybar.py` is a serial instrument file in U3 (§1.1, C3-K7): this edit lands in B03,
   before any batch in that list opens it.

**Tests.** None added. Covering: the test files that import `soak` and `storybar`
(`grep -rl "harness.soak\|harness import soak\|storybar" engine/season/tests`), run once.

**Gate.** `python -m engine.season.harness.soak` and `python -m engine.season.harness.storybar`, each at
its smallest documented invocation, print the same content hashes as on the batch's base (each prints
them; `storybar`'s `--draw-seeds` arm included, since that is the parameter added);
`grep -n "make_chooser(" engine/season/harness/*.py` prints `probes.py` (two lines: the owner and the
probe at `:1051` with its own mint) and `interactions.py` only.

**Falsifier and control.** In a scratch worktree, before the edit: change the purpose string in
`probes.chooser`'s mint (`"act:"` → `"act2:"`) → `populated`'s hash must move and `soak`'s must **not**
(it does not go through the owner yet). After the edit: the same plant moves both. That pair shows the
routing happened.

**Declared hash movers.** None. **Depends on:** `U5a_CORE_owed_edits` (edits `probes.py` earlier in B03).
**Enables:** B06 (`11_GO_one_draw_owner`: what `draw_factory` returns changes in one composition).
**Lands in:** B03. **Lands it:** one lane, `sonnet`, `medium`. **Cost class:** edit.

---

## CI-07 · The realm builder has a home in the game code, and a person is placed one way — the move into `engine/season/boot/` (A-102)

Reconciled: 2026-11-12, A-102 (Jordan: `J-H-01` option A, a tenth module; lane `unified/work/A102_112_APPLIED.md`). No longer held. The Layer 1 text is applied (node `L1-A102`, `ED-IN-0359`: `04` §A.2's `boot/` line and row, PART D rows 46 and 53, F.31; `hol` §45, §47), so the move lands against amended text and no step below edits `architecture/`. The option table is replaced by the ruled destination; the edits are the same as drafted, with the paths named and the path-keyed scans added (step 7).

**Finding.** H-02. `build_realm` and the 23 module-level functions defined before it are in
`engine/season/harness/populated.py` (`:98` to `:1995`); six harness files assign the stores directly at
71 sites.

**What dies.** The realm's construction as part of an instrument file; the repeated four-line placing of a
person (`populated.py:515-518`, `:693-696`). **Preserved:** every world the builder makes, byte for byte
(its content hash before a season is run, at seeds 0, 1, 2, with each of the seven arms flipped once).

**Where it goes (A-102, ruled).** A tenth module, `engine/season/boot/`, holding three files:
`boot/__init__.py` (docstring only: the module's one sentence from `04` §A.2, *"the realm builder and the
chooser's set-up: reads the authored data, constructs the World, holds no token after construction; imports
no instrument"*; it re-exports nothing), `boot/realm.py` (the builder, steps 1, 2 and 4) and
`boot/chooser.py` (the chooser's set-up, step 3). Path constants in `engine/season/data/files.py`, beside
`HARNESS_DIR` (`:44`) and `LOOP_DIR` (`:176`): `BOOT_DIR = PACKAGE_DIR / "boot"`, `REALM_PY = BOOT_DIR /
"realm.py"`, `BOOT_CHOOSER_PY = BOOT_DIR / "chooser.py"`. `BOOT_DIR` is **not** added to `loop_modules()`
(`data/files.py:183`), which lists the steps; `package_modules()` (`:258`) discovers the new files by
`rglob` with no edit.

**Exact edits, in order** (A-102: option A).

1. *Closure first.* By `ast`, list which of the 23 functions `build_realm` reaches (a function it does not
   reach stays where it is), and every name the reached set reads from
   `harness/probes.py` (imported as `P`) and `harness/run_cases.py` (`load_cases`, `seed_pursuits`,
   `wants_of`; `populated.py:92-93`). A name only the builder reads moves with it; a name both sides read
   moves to `boot/realm.py` and the harness imports it from there. `boot/` imports nothing
   from `harness/` when this step is done (the direction `W2` shows today for every non-harness file;
   `04` PART D row 53). The relative imports of the moved code change from `..` (the harness's parent)
   to `..` from `boot/` (the same depth, so `from ..data import cast, files` and its siblings at
   `populated.py:70-89` stay textually the same); `from . import probes as P` and
   `from .run_cases import …` (`:90-91`) are replaced by imports of the moved names or deleted.
2. Move into `boot/realm.py`, without editing bodies: `_load`, `_slug`, `_index_anchor`, `resolve_anchor`, `seat_anchor`,
   `_mentions`, `_institutions`, `institution_of`, `surname_index`, `concerns_of`, `cohort_rows`,
   `temperament_rows`, `seat_cohorts`, `guard_rows`, `_first_holder`, `_seat_id`, `acquaintance_pairs`,
   `seed_acquaintances`, `seat_guards`, `mint_planned_works`, `goals_missing`, `seed_goals`, `seed_arms`,
   `build_realm`, and the module constants they read (`GEOGRAPHY`, `VENUES`, `ROSTER`, …). `census`, `run`,
   `creed_sweep` and `main` stay in `harness/populated.py` and import the builder.
3. `harness/probes.py::chooser` (`:278-292`, after CI-06 gives it `draw_seed`) moves to
   `boot/chooser.py::chooser` as the game's composition of its chooser (`make_chooser` over `w.fixtures`,
   the act-id mint `H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")`, `draw_factory`); its imports are
   `decision.make_chooser` and `state.ids.H, draw_factory`, nothing from `harness/`. `harness/probes.py`
   imports it (`from ..boot.chooser import chooser`) for its callers; `run` stays an instrument.
4. One function that places a person, in `boot/realm.py`,
   `place_person(w, pid, name, rung, *, home=None, weight=1, **fields) -> Person` (the word is *place*, not
   *seat*: a seat is an office in this tree): the `Person`, its person
   `Rung`, the `contain` Tenure `t_{pid}_in` and the `reside` Tenure `t_{pid}_home` (the ids at
   `populated.py:517-518`). The two `populated` sites call it. Each of the other five builders
   (`probes.tiny_world`, `scarce`, `governance_spine`, `headless.build_world`, `corpus_run.build_at`) calls
   it **only where the ids and the order of the four writes are the same**; a site that differs is left and
   listed in the commit, because changing an id moves a hash.
5. Re-point every importer in the same commit; leave no alias in `harness/populated.py` (CLAUDE.md §0.05
   cl. 3; the decomposition's precedent of deleting its facade). The importers are those
   `grep -rl "build_realm" engine tools tests --include=*.py` lists: 87 files under `engine/season/tests`,
   six under `tests/valoria`, 18 under `harness/`, `tools/m1_acceptance.py`, `tools/export_npc_roster.py`.
   The 19 files of `loop/`, `state/`, `data/`, `queries/`, `decision/` and `epistemic.py` that *name*
   `build_realm` or `populated` in a comment are CI-02's. (Re-read 2026-11-12: 133 files name `build_realm`;
   90 under `engine/season/tests`, `tests/valoria`, `tools` and `harness/` carry an import line naming
   `populated` or `build_realm`, by `grep -rlE "(from|import) .*(populated|build_realm)"`; the rest name
   it in comments.) The rewrite per file is mechanical and is the one form
   `from engine.season.boot.realm import build_realm` (or `from ..boot.realm import …` inside the package);
   a file that also uses `populated.run`, `census`, `creed_sweep` or `main` keeps its `populated` import for
   those. Verify with `grep -rnE "populated\.(build_realm|seat_cohorts|seat_guards|resolve_anchor|place_person)"
   engine tools tests --include=*.py` printing nothing.
6. `tools/export_sim_params.py::_realm_arm_records` (CI-05): its path becomes `files.REALM_PY`.
7. **The path-keyed scans that named the builder's old home** (read 2026-11-12; each changes in the same
   commit, and the change is to a path, never to what the scan asserts):
   - `engine/season/tests/test_cr20_attributes.py:236` (`build = root / "harness" / "populated.py"`, the one
     file allowed to assign `attributes`/`heritage`) and `engine/season/tests/test_k3_thread_sensitivity.py:222`
     (`_BUILD`, the one file allowed to assign the carrier): both become `files.REALM_PY`.
   - The scans that skip the instrument and will now reach the builder: `test_season_shape.py::_model_modules`
     (`:679-680`, `"harness" not in m.parts`; read by `test_d6_no_constant_is_hardcoded_in_a_body`,
     `test_h115_the_fourteen_load_time_raises_are_unchanged`, `test_jordan_no_definition_is_hardcoded_in_a_body`)
     and `test_cp_t03_07_body_ceiling.py::_season_sources` (`:282`, skips `tests` and `harness`). `boot/` is
     game code (A-102), so these scans SHOULD see it: run the four tests on the moved tree; a hit that a
     same-value move to its register row clears is cleared in this batch (hash EQUAL); a hit that needs a
     ruling or a value change is not fixed here: `boot` is added to that one scan's skip tuple with a
     comment naming `04` §A.2's `boot/` row ("construction is not a season write") and the hit count in the
     commit body. `[UNVERIFIED: the hit counts on a moved tree were not measured by this lane]`
     `[ASSUMPTION: a skip with a named reason, not a body edit, keeps the batch a pure move — basis: A-102 "a
     pure move: no outcome changes"; revert: clear the hits in a later batch and drop the skip]`
   - `test_g2_token.py:43` (`APPARATUS = ("harness/", "tests/")`, where calling `mint_token` is allowed):
     unchanged; `boot/` calls no `mint_token` (`populated.py` names it only in a docstring, `:718`), and
     `boot/` must not join `APPARATUS` (row 53's twin: it holds no token after construction).
8. Layer 1: **done** (A-97, node `L1-A102`, `ED-IN-0359`); this batch edits no file under `architecture/`.

**Tests.** Add `engine/season/tests/test_boot_module.py` (the module's own file):
`test_importing_boot_pulls_in_no_instrument`: in a fresh subprocess (`subprocess.run([sys.executable, "-c",
…])`), `import engine.season.boot.realm, engine.season.boot.chooser`, then assert no key of `sys.modules`
starts with `engine.season.harness`, with a floor
(`assert len([m for m in sys.modules if m.startswith("engine.season")]) > 20`) so an import that loaded
nothing cannot pass (`04` PART D row 53's MECHANICAL grade; the shape of
`test_importing_every_engine_module_pulls_in_no_subsystem`). `test_no_harness_import_line_in_boot`: by
`ast`, every `Import`/`ImportFrom` node in `files.BOOT_DIR.rglob("*.py")` names no `harness` module, with
`assert checked >= 3` files. Change: nothing else but import lines and the step-7 paths.

**Gate.** For seeds 0, 1, 2: `build_realm(seed).content_hash()` equal to the base; the same for each arm
flipped once at seed 0; the realm hashes after one season at seeds 0 and 2 equal the opening reading;
`python tools/m1_acceptance.py --summary` rows 1, 2 and 4 PASS; `python tools/export_npc_roster.py --check`
current; `python tools/export_sim_params.py --check` current; the new test green. **Hash EQUAL is the
gate**: the base readings are taken on the batch's base commit by the same script before any file moves,
and a single differing hash fails the batch (a pure move moves nothing; A-102). The covering pytest run is
`python tools/tests_for_diff.py`'s list for the diff, once, at the close (CLAUDE.md §0.4), which for ~90
re-pointed test files is effectively `pytest engine/season/tests tests/valoria -n auto`.

**Falsifier and control.** In a scratch worktree: add `1` to the weight `seat_cohorts` gives one cohort →
the build hash at seed 0 must move (the control sees the builder). Revert. Then import the moved builder
with `engine.season.harness` blocked (`sys.modules["engine.season.harness"] = None`) → it must import.

**Declared hash movers.** None. **Depends on:** A-102 (answered; `J-H-01` closed); `L1-A102` (APPLIED);
CI-05, CI-06. **Lands in:** `B03c-boot` (IN), joined to the U3 order after B03 and before the first batch
that edits the builder (`unified/U3_DEPENDENCY_ORDER.md` §1, the B03c row); every later proposal that edits
`populated.py`'s builder (29 by `U3` §5.1) is re-pointed to `boot/realm.py` by its symbol name. **Lands it:**
one `valoria-author` lane, `sonnet`, `high`, for steps 1 to 4, 6 and 7; the importer re-pointing (step 5,
about 90 files of import lines) on `haiku`, batched. **Cost class:** small build (a move), wide by file count.

---

## CI-08 · The driver imports what it uses

**Finding.** H-09. `engine/season/loop/driver.py` imports 112 names and references 33. The docstring
(`:18-28`) says the rest are held for `engine/reference/degree-sweep/sweep_core.py`; measured, none is
(`master/HOLISTIC_AUDIT_part2.md` H-09, falsifier: of 26 `S.<name>` reads only `SeasonDriver` and
`resolvable_verbs` resolve through the driver alone, and no file obtains any of the 79 through the driver).

**What dies.** 79 imported names and the docstring paragraph that defends them. **Preserved:** every
import-time registration. Three of the driver's import statements name modules that register tables when
imported: `..seam` (the providers; `seam/__init__.py:49`: *"IMPORTING `wrappers` IS WHAT REGISTERS THE
PROVIDERS"*), `..loop.effects` (the `@effect_for` bodies) and `..loop.predicates`. Where every name of
such a statement is unused, **the statement becomes a bare module import with its reason in a comment**;
it is not deleted.

**The 79** (from `ast`: imported at module scope, never read as a name in the module; `annotations`
excluded): `CHANNEL_PREDICATES, Callable, Candidate, Claim, Collision, ContestError, Fixtures, Forbidden, H,
InstrumentDefect, LEDGER_DERIVED_STEMS, LedgerReader, NoProducer, OBSERVATION_DEPOSIT_MODES, Office, Person,
Proposition, Question, ROOT, Record, Resolution, Rung, SITE_YIELD, STRATA, Scene, Sensation, Site,
StateChange, Step, Tenure, UNKNOWN, Ungraded, Unowned, Unspecified, VerbRow, Verdict, View,
WITNESS_CHANNELS, WorldReader, act_refs, aggregate_questions, agreement, assemble, binding_from_act,
binding_of, body_band_penalty, budget, cache, claim_subjects, combat_degree, containing_rung_of, contest,
contest_subsystem, decision, degree_ladder, degree_of, effect_for, entrenchment, evaluate, files, hashlib,
inspect, itertools, json, ladder_error, make_chooser, matrix_row, observers_for, occasioned_by,
opening_set, operands_for, pack_scenes, person_side_eligible, random, re, requires_predicate, standing_of,
store_kind_of, view_ids`. The lane re-derives the list on its base (the file will have moved) rather than
trusting this one.

**Exact edits, in order.**

1. Re-derive the list (ten lines of `ast`: names bound by `Import`/`ImportFrom` at module scope minus the
   `ast.Name` ids in the module). Note that the bindings at the foot of the file (`:575` on) import the
   seven steps and are read there.
2. Delete each unused name from its statement. A statement left empty is deleted, **except** the three
   registering modules above, which become `from .. import seam  # registers the providers` and the like.
3. Rewrite the docstring's two paragraphs at `:18-28` as one sentence: the driver constructs the tokens,
   binds the seven steps and owns `resolvable_verbs`.
4. `engine/reference/degree-sweep/sweep_core.py`: no change.

**Tests.** None added. Covering: the two tests that import the sweep arms
(`engine/season/tests/test_season_shape.py`, from `:14247`), `tests/valoria/test_engine_does_not_import_systems.py`.

**Gate.** `python -c "import engine.season.loop.driver"` exits 0;
`python -c "import runpy; runpy.run_path('engine/reference/degree-sweep/sweep_core.py')"` exits 0; the
headless hash and the realm hashes at seeds 0 and 2 equal the opening reading (an unregistered provider
or effect would refuse the first contest or write and move the hash: 48 contests in the first season at
seed 0); the covering tests green.

**Falsifier and control.** In a scratch worktree: delete the `..seam` import outright → the realm run must
fail or its hash move (the control sees a lost registration). Restore. Delete one name the driver does
read (`Token`) → the import must fail.

**Declared hash movers.** None. **Depends on:** nothing in B03 edits this file before it. **Lands in:**
B03. **Lands it:** one lane, `sonnet`, `medium`. **Cost class:** edit.

---

## CI-09 · Personal combat is a package, and its path seam is gone

**Finding.** H-08. `modules/combat/` is fifteen files that import each other by bare name behind five
`sys.path` inserts; the host reaches two of its modules and one of its constants through
`engine/substrate/pc_engine.py`.

**What dies.** `engine/substrate/pc_engine.py` (50 lines); the path inserts at
`modules/combat/{wrapper.py:7, contact.py:13, combat_systems.py:4, core.py:14-17}`; the allow-list entry
`PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}` (`tests/valoria/test_engine_does_not_import_systems.py:250`);
the top-level module names `core`, `config`, `geometry`, `weapons`, `vocabulary`, `attributes`, `contact`,
`wrapper`, `combatant` and the rest. **Preserved:** every fight, blow for blow; the exported constants
(`combat_engine_v1.json` byte-identical); the composition target `modules.combat.fight:fight`, unchanged.

**Earning.** The seam's stated reason is that the workbench loads the set flat, so a dotted import would
give the modules a second identity (`pc_engine.py:5-8`). Re-pointing the workbench removes the reason;
nothing else earns the flat form.

**Exact edits, in order.**

1. List every flat importer first (the edit set):
   `grep -rnE "^\s*(import|from) (core|config|geometry|weapons|vocabulary|attributes|contact|tradition|traditions|wrapper|combatant|combat_systems|weapon_physics|ability_primitives)\b" --include=*.py .`
   and `grep -rln "pc_engine" --include=*.py .`. At `4dc8a7b`: the 15 module files, 15 files under
   `systems/combat/`, `tools/export_engine_params.py:127-132`, 23 files under `tests/valoria` and 4 under
   `engine/season/tests` that name the module's directory or load its files, and the pc_engine users
   (`engine/season/seam/wrappers/combat.py`, five season test files, two `tests/valoria` files).
2. Add `modules/combat/__init__.py` (a one-line docstring).
3. In each module file, make sibling imports relative, keeping every alias: `import core` →
   `from . import core`; `import combat_systems as S` → `from . import combat_systems as S`;
   `from config import CFG` → `from .config import CFG`; and so on for the sites at `wrapper.py:8-10`,
   `combat_systems.py:7-12`, `combatant.py:7-9`, `contact.py:14-15`, `core.py:22`, `:42`,
   `ability_primitives.py:76`, `tradition.py:13`, `:17`, `weapon_physics.py:37`, `weapons.py:828`, `:906`,
   `fight.py:50`. Delete the four path-insert lines and `core.py`'s repository-root insert (`:16-17`).
4. `modules/combat/fight.py`: `from engine.substrate import pc_engine` goes; `wrapper, combatant =
   pc_engine.load()` (`:72`) becomes `from . import wrapper, combatant` at module scope.
5. The host's one data read. `engine/season/seam/wrappers/combat.py:170-171` checks a roster term against
   `loaded[0].DUEL_TERMS`, a module constant read through the path seam. Give it a composition row of the
   kind the exporter already has for constants (`tools/export_composition.py:70`, `_KINDS = ('callable',
   'value')`), in `references/module_contracts.yaml` after `combat.fight`:

   ```yaml
     combat.duel_terms:
       target: "modules.combat.wrapper:DUEL_TERMS"
       kind: value
       needed_by: "engine/season/seam/wrappers/combat.py — the roster check of `duel_terms` and `challenge_terms` against the engine's closed set."
   ```

   then `python tools/export_composition.py`; the check reads `composition.require("combat.duel_terms")`.
6. `engine/season/seam/wrappers/combat.py::_probe` (`:107-115`): availability becomes "the entry
   resolves": `composition.require("combat.fight")` inside the same `try`, returning the callable.
   `engine()` and `load_error()` keep their names and their meaning. Tests that index the old tuple
   (`engine()[0].core`, `pc_engine.load().wrapper`: `test_season_shape.py:9833-9838`,
   `test_cr85_faculty_replaces_history.py:90`, `test_cp_t03_03_kit.py:87-88`, `test_cp_t03_04_arms.py:117`,
   `test_pc10b_challenge_record.py:132`) import `modules.combat.<name>` **inside the test function or its
   pytest fixture**, never at module scope: `test_importing_every_engine_module_pulls_in_no_subsystem` imports the
   season's test modules (`test_cr85_faculty_replaces_history.py:44-45` says so).
7. `systems/combat/combat_engine_v1/workbench/*.py`: each `sys.path.insert(..., 'modules', 'combat')` line
   becomes one insert of the repository root, and `import wrapper` becomes `from modules.combat import
   wrapper` (likewise `config`, `core`, `combatant`). `tools/export_engine_params.py:127-132` likewise.
8. Delete `engine/substrate/pc_engine.py`; write its `FORK:` row (§4); empty the allow-list
   (`PATH_SEAM_ALLOWED = set()`) and trim the comment above it; correct the line in
   `engine/substrate/__init__.py` that names the file.
9. `unified/U1_GLOSSARY.md`: no row (no term changes).

**Tests.** Add to `engine/season/tests/test_combat_module.py`:
`test_a_fight_leaves_no_flat_module_behind`: in a fresh subprocess, resolve `combat.fight`, run one fight
on the input the file's existing tests already build, then assert
`not ({"core", "config", "wrapper", "combatant", "weapons", "geometry"} & set(sys.modules))` and
`"modules.combat.core" in sys.modules`. Change: `tests/valoria/test_engine_does_not_import_systems.py`
(the allow-list is empty) and the tests of step 6.

**Gate.**

1. The realm hash at **seed 2**, one season, equals the opening reading (combat is entered in that season:
   155 functions, `W4`); the seed-0 hash too (it cannot see this edit and is a control on everything else).
2. `python tools/export_engine_params.py --check` current with **no rebuild** (byte-identical artifact);
   `python tools/export_composition.py --check` current, one role more.
3. `python tools/ci_golden_modes_check.py` green (the combat goldens, by its registry role).
4. `python tools/freshness_gate.py` passes, or the one pin it names is re-recorded and said so
   (`references/canonical_sources.yaml:80` points at `modules/combat/`).
5. `grep -rn "sys.path.insert" modules/combat engine/substrate` prints nothing; the new test green; the
   workbench's `balance.py` runs its smallest documented invocation.

**Falsifier and control.** In a scratch worktree, before the edit: add `1` to one literal on a line of
`modules/combat/core.py` that a fight executes → the seed-2 hash must move and the seed-0 hash must not
(that pair is what shows which seed sees combat). After the edit: leave one bare `import core` in
`wrapper.py` → the new test must fail (two identities) or the import must raise.

**Declared hash movers.** None. **Depends on:** B03a (CI-02 edits the same files' comments first).
**Lands in:** `B13-pc-package` (PC), before B05 and B14. **Lands it:** one `valoria-author` lane, `sonnet`,
`high` (the import closure is one unit; a second lane would have to hold the same closure), with
`[UNVERIFIED: the exact lines in the 27 test files; step 1's greps list them.]` **Cost class:** small
build, wide by file count (about 60 files); [estimate] two to three hours of agent time.

---

## CI-10 · Three things nothing reads are deleted

**Finding.** H-10 (the part no other proposal carries). Rows and symbols the census lanes found are theirs
(`17_CENSUS_C1A_01`, `C1B_01`, `REST_1`) and are not repeated.

| delete | size | what was searched (C5) and found |
|---|---|---|
| `tools/join_audit_workings.py` | 253 lines | whole-word name over `engine modules tools tests skills .claude .github .githooks`: no caller (`W6`). Its subject, the audit corpus's nested working tier, is retired as a category (CLAUDE.md §3); its products (`.audit/*/_workings_joined.md`) stay; its test was dropped at ED-IN-0312 (`references/restructure_ledger.md:3100`) |
| `tools/verify_handoff_split.py` | 662 lines | the same search: no caller. A falsifier for one migration, the handoff split of 2026-09-13 (ED-IN-0221), which is done; its test was dropped at ED-IN-0312 (`restructure_ledger.md:3118`) |
| `tools/link_values_pointers.py`, `tests/valoria/test_link_values_pointers.py`, `engine/engine_params/value_pointer_links.json` | 176 lines, the test, 23,151 bytes | the artifact is opened by its generator and that test only (`W5` §2); the tool is in no CI job, hook or registry row (`W6`); one comment names it (`engine/season/data/cast.py:432`) |

**What is preserved.** Every gate, export and run. **Earning attacked:** E1 none (no rule names them),
E2 none (no run reads them), E3 none (`[UNVERIFIED: workplan v11 was not searched for the three names;
STAGES step 5 does that and may carry one]`), E4 none.

**Exact edits, in order.**

1. Re-run the search on the base:
   `grep -rnw -e join_audit_workings -e verify_handoff_split -e link_values_pointers -e value_pointer_links --include=*.py --include=*.yml --include=*.yaml --include=*.json --include=*.md .`
   outside `registers/`, `.audit/`, `research/`, `proposals/` and `references/restructure_ledger.md`.
   Expected: the files themselves, the test, and the comment at `data/cast.py:432`.
2. `git rm` the five files. Edit the comment at `data/cast.py:432` so it names no deleted tool.
3. Write the five `FORK:` rows of §4 into `references/restructure_ledger.md` (a shallow clone runs
   `git fetch --unshallow` first, CLAUDE.md §2).
4. `tools/build_identifier_census.py:269` reads the keys of every `engine/engine_params/*.json`: run it as
   CI runs it (the job step in `.github/workflows/valoria-ci.yml` that names it). If an identifier now
   reads as unknown, it was known only through the deleted link file; correct the document that uses it.

**Tests.** `tests/valoria/test_link_values_pointers.py` is deleted with its subject. None added.

**Gate.** Step 1's grep, re-run, prints only ledger and history lines;
`python tools/broken_dependency_checker.py` and `python tools/valoria_local.py` as CI runs them, green;
`python tools/export_game_constants.py --check` and `python tools/export_sim_params.py --check` current;
hashes equal (nothing at runtime read any of the five).

**Falsifier.** A caller: any line step 1 prints that is an import, a subprocess call or a workflow step.
If one appears, that file is not deleted and the row is struck.

**Declared hash movers.** None. **Depends on:** nothing. **Lands in:** B03, first. **Lands it:** one lane,
`sonnet`, `low`. **Cost class:** edit.

---

## CI-11 · The act-count instrument (`harness/aperture.py`) prints which engines a run entered

**Finding.** H-01. Six of sixteen composition rows were entered by none of three realm runs, and no
instrument says so: the act-count instrument reports per verb, and a verb that executes need not enter the
engine behind it (`march` is attempted at seed 0 in the first season; `resolve_field` is entered 0 times).

**What dies.** Nothing. **What is added:** one block on an existing instrument, and its test. It is an
instrument reading of the game (which engines the season reached), not a check on a process artifact, and
it blocks nothing.

**Exact edits, in order.**

1. `engine/season/harness/aperture.py`: a function
   `engines_entered(run: Callable[[], Any]) -> tuple[Any, dict | None]` that, on Python 3.12 or later, takes
   a monitoring tool id (`sys.monitoring.use_tool_id`), and for each role of
   `engine.substrate.composition.ROLES` whose resolved target has a `__code__` enables `PY_START` on that
   code object alone (`sys.monitoring.set_local_events`), counting entries per role; runs `run()`; frees
   the tool id in a `finally`; returns `run`'s value and `{role: count}`. Where the interpreter is older
   or the tool id is taken, it returns `None` for the counts and the block says why. A `kind: value` row
   has no code object and is listed as `value`.
2. `measure_world` (`:595`) wraps its seasons in it and stores the counts as `m["engines"]`.
3. `report` (`:978`) gains a block after the per-verb lines:

   ```
   ENGINES (composition rows entered in this run)
     fieldwork.find              62
     settlements.housing         79
     social_contest.roll         48
     ...
     rows entered 6 of 16
   ```

   every row printed, zeros included, sorted by role.
4. `pooled_report` (`:941`) prints, per role, the number of seeds whose run entered it.

**Tests.** Add to `engine/season/tests/test_aperture.py`:
`test_the_engines_reading_counts_an_entry_it_can_see`: inside `engines_entered`, call one module entry
through its row once (`composition.require("settlements.fortification")` on a built `FortInput`, or the
row the file's existing tests can already build an input for); assert that role reads `1` and that another role reads `0`,
and assert the counts are not `None` on the interpreter CI uses (a named skip below 3.12). The file's
existing control (the measured arm ends in the same `content_hash()` as `populated.run`) is what shows
the reading does not move the world.

**Gate.** `python -m engine.season.harness.aperture 1 0`: its `CONTROL` line reads as before, and the
block prints. Expected at `4dc8a7b`: `social_contest.roll` 48 and `fieldwork.find` 62 (both season-only
calls, `W3`); `settlements.housing`, `larder_draw`, `produce`, `subsist` non-zero (their counts depend on
whether the build is inside the measured span, and `W3`'s 79, 1, 1, 1 include it); ten rows at 0,
`combat.fight` and `mass_battle.resolve_field` among them; `rows entered 6 of 16`.

**Falsifier and control.** In a scratch worktree: remove the `set_local_events` call → the new test must
fail (the role reads 0, not 1). Restore.

**How later batches use it.** A batch that claims to bring an engine into play quotes the block before and
after at a named seed and season count in its close (`reading @<sha>`), beside `--requirements`. It is a
reading, never a threshold, and no count from it goes in a pointer index (CLAUDE.md §1).

**Declared hash movers.** None. **Depends on:** nothing. **Lands in:** B02. **Lands it:** one lane,
`sonnet`, `medium`. **Cost class:** edit.

---

## 4. The deletion list, with `FORK:` row text

Rows for `references/restructure_ledger.md`, in the table's own form (`| old | new | STATUS |`; an
exact-file row each, CLAUDE.md §1, §8). `<sha>` is `git log -n1 --format=%h -- <path>` on the batch's base,
the last commit touching the file, so the text there is the file; `<date>` is the landing date.

```
| `tools/join_audit_workings.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: no caller in engine, modules, tools, tests, skills or CI; its subject, the audit corpus's nested working tier, is retired as a category (`CLAUDE.md` section 3) and its test was dropped at ED-IN-0312. `<sha>` is the last commit touching it, so the text there is the file) |
| `tools/verify_handoff_split.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: no caller; a one-time falsifier for the handoff split of 2026-09-13 (ED-IN-0221), which is complete; its test was dropped at ED-IN-0312. `<sha>` is the last commit touching it, so the text there is the file) |
| `tools/link_values_pointers.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: its one output, `engine/engine_params/value_pointer_links.json`, was read by nothing but this tool and its test; in no CI job, hook or registry row. `<sha>` is the last commit touching it, so the text there is the file) |
| `tests/valoria/test_link_values_pointers.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: deleted with its subject, `tools/link_values_pointers.py`. `<sha>` is the last commit touching it, so the text there is the file) |
| `engine/engine_params/value_pointer_links.json` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: a generated artifact no engine, module, exporter or port file read. `<sha>` is the last commit touching it, so the text there is the file) |
| `engine/substrate/pc_engine.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B13, item CI-09: the one path seam into `modules/combat/`, retired when that directory became a package; the host reaches the module through the composition rows `combat.fight` and `combat.duel_terms`. `<sha>` is the last commit touching it, so the text there is the file) |
```

Symbols deleted without a file deletion (no `FORK:` row; the commit is the record): CI-03 `_ROLL_ROLE` and
the `importlib` import in `seam/wrappers/sigma.py`; CI-06 the two hand compositions; CI-08 the 79 imported
names in `loop/driver.py`; CI-09 the four path inserts in `modules/combat/` and `PATH_SEAM_ALLOWED`'s one
member.

## 5. Notes for v12's author

1. **One ordering rule for additions to the two registries** (H-07). After B03a, a batch that adds a
   roster to `rosters.yaml` or a row to `verb_table.yaml` adds it at the end of the block its family
   already occupies, never in the middle of another batch's block, so that two open batches' additions are
   separate hunks. This binds a reader; no check is built for it (CLAUDE.md §0.1 pt 5).
2. **Cite by symbol.** After B03a every `path:line` into an edited file is stale. v12's content-owner
   entries name the file and the symbol or key; a line number is a convenience.
3. **Seeds.** A gate that must see personal combat names seed 2 (entered in season 1); seed 0 enters it
   in none of three seasons. A gate that must see a fought field names seed 0 at three seasons or seed 2 at
   one (`W4`).
4. **Runtimes measured on this machine** (for sizing, STAGES practice 5; one reading each, not a
   benchmark): `register --requirements` 0.6 s; `m1_acceptance --summary` 20 s; build plus one realm
   season about 8 s; seasons two, three and four at seed 2 take 16, 32 and 65 s, so a season's cost roughly
   doubles with each season played; four seasons at seed 2, 120 s.
5. **CI-06 before B06.** With the chooser composed once, `11_GO_one_draw_owner`'s change to the chooser's
   draw is one edit in `probes.chooser` and one in `interactions.py`.
6. ~~**What moves when `J-H-01` is answered late.** CI-07 is a pure move and lands at any IN-lane boundary;
   until then proposals keep citing `harness/populated.py::build_realm`.~~ *(A-102, 2026-11-12: answered;
   CI-07 lands as `B03c-boot` after B03; proposals keep citing `populated.py`'s builder by symbol until B03c
   lands and are re-pointed to `boot/realm.py` by symbol.)*

## 6. What this proposal does not carry, and why

| not carried | why |
|---|---|
| splitting `world_q.py`, `rosters.yaml` or `verb_table.yaml` into families | attacked and not earned yet (`HOLISTIC_AUDIT_part2.md` §6, attack 5): a split is relocation, `04` §A.2 names `world_q` as a member, and the reading cost is mostly prose that CI-01 and CI-02 remove |
| routing the nine direct `composition.require` sites through `MODULE_ENTRIES` | both routes return one cached object; unifying them adds an import edge `04` §A.2 does not give (H-05) |
| retiring `systems/*/sim` | retention is ruled (ED-IN-0283); the per-subsystem retirements are carried (`05_SC_sc05_kernel_retirement`, `09_WR_threadwork_module`, the census deletions) |
| typed outcomes at the contest seam | carried: `03_PC_typed_outcome_one_door` (B14), `04_MB_typed_outcome_and_one_path` (B17) |
| one draw owner; one roller; the environment reads in mass battle | carried: B06, B05, B41 |
| the tests' own prose and goldens; `requirements.yaml`'s `measured:` | carried: B02 |
| the remaining tools under `tools/` | process apparatus: delete or leave, and nothing but CI-10's three is shown unread (H-13) |
| the three roots of authored data | a placement note with no shown cost (H-11) |
| moving role-name constants out of `queries/world_q.py` | a lateral coupling noted in §5 of the audit; relocation with no reader's lookup improved |
