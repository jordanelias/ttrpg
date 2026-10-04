# Valoria — Master Workplan v8, part 5: Batch 4 (opens per ruling) · modules and the dice engine (§SM) · the Jordan queue · what the ladder already answered

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094). ⚠ HELD BACK, LOUDLY: every item in §J is OPEN and is Jordan's to answer individually. A merge of this plan answers none of them, and no position gated on one becomes buildable because this file merged.
## Reads after `workplans/valoria_master_workplan_v8_part4.md`.
## Grade under `CLAUDE.md` §0.2: `paper`.

---

## B4. BATCH 4 — JORDAN-GATED; ONE SUB-BATCH PER RULING, AS EACH LANDS

**Reading list:** `proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md` §3.3–§3.5 (the H-item
deliverables, carried below so that file can be deleted once they land — its own header asks for that);
`proposals/2026-09-20-pursuit-basis-worksheet.yaml`; the DRAFT candidates `candidate_pursuit_cells.md`
and `candidate_affiliation_content.md` in the decision-layer proposal (they ratify nothing);
`engine/season/hole_register.yaml` H-146; `ED-IN-0261`'s 2026-09-28 row.

### The cells commit — `12b` · `12c` · `12d` + H6 + H8 · IN · gate J-1 · `opus`/`opus` · one R6-atomic commit · `[design]`

**Atomic because** `data/verbs.py`'s `_load_projection`/`_load_alignment` bind at module scope and refuse
an unrostered key or an all-zero matrix — a partial landing is an `ImportError`. **In one commit:**
`references/descriptor_registry.yaml` (`conviction_roster` → `pursuit_roster`, 15; `axis_roster`, 7;
each with `count`) behind `tools/export_descriptors.py --check`; `engine/substrate/descriptors.py` and
`data/pursuits.py` names; `rosters.yaml` `pursuit_projection` (15 × 7), `alignment` (every verb × 7),
`role_template_pursuits` **plus an explicit validation step** (its read path does not raise on an
unknown name); `references/npc_registry.yaml` values; `references/names_index.yaml`; **the verb split** —
`FIGHT-RENAME` already landed `fight`, so the split adds `kill`, `wound`, `challenge` → `accept` (`accept`
carries `contests: "the body"`), with `loop/effects_combat.py` registrations; `12b`'s schema half — a
`(Person, conviction)` carrier, its `write_matrix.yaml` row, a `queries/person_q.py` confliction Query
derived and never stored, **with a caller** (if nothing reads confliction yet — build-order 6f, `score`
dotting against the basis — the Query waits for 6f, `ID-13`); `refusal_axis` set only if the ruling says
arm H-146, reading the refusing pole from roster data. Audit the direct readers of
`descriptors.CONVICTIONS` that survive Batch 1 (`npe.py`'s died at `29d`; `conviction.py` STAYS — `29e` cancelled, A-24). Re-pin
`test_conviction_roster_single_owner.py` and `test_conviction_spread_solver.py` (declared, §7).
**FALSIFIER:** Jordan's faith pair (the devout-Solmund builder and the Einhir dismantler, both high
`faith` — his own worked example in the worksheet) sits outside the 60° bar (`cos ≤ 0.5`) —
`python -m engine.season.harness.conviction_spread` prints `within_60deg`; the loaders raise on a
partial landing; **`resolvable_verbs()`'s new count is derived from `loop/driver.py`'s definition at the
build, never asserted in advance**; the headless hash moves (declared); the three-arm corpus readout
`ED-IN-0261` used is re-run. **E5:** never interleaved with `8`, `9`. **R:** R-05 (+4 rows),
R-06 reason 2, R-08.

**Then, in order (each its own step):**
- **H7** — the faith-pair test as a standing test; if red, the placement is wrong and the fix goes back to
  J-1, not to the code.
- **H3 = `12`'s scar rebuild** — `Person.scar` becomes `{element: count}`; `_scar` and `scar_step` retire;
  at RESOLVE the act calls `observers_for(w, e, mode, everyone)` and increments one count per observer
  per violated pursuit. The violation predicate (`Σ_axis projection·align < 0`, a sign test) is a
  candidate reading recorded for review, not a ruling; whether the actor counts as an observer is a swept
  arm. Retire the `(Person, axis_count)` row or give it the field — **never both**. **FALSIFIER:** counts
  differ between `fan_out_mode` `presence_only` and `all_five`; a scar on a person who did not observe the
  act → fail; a conviction write reachable from a `Failure` band or from WITNESS's token → fail.
  ⚠ `(Person, pursuits)` movement has **no specified trigger anywhere** (H-62) — describe it; do not build
  around it.
- **H9** — crisis reader, threshold 2 only: the weight shift as a `Fixtures` arm, control `0`, swept.
  **FALSIFIER:** fork divergence at the `total` arm rises above the ED-IN-0261 baseline while the control
  arm is unmoved.
- **H10** (gate J-5's C3) — `affiliation_roster` with exporter validation; `Person.conviction: dict`; the
  `incompatible` half-matrix with a loader refusing an unrostered pair; `confliction(p)` derived.
  **FALSIFIER:** two incompatible affiliations at full intensity load, and `confliction` is non-zero.
- **H11** (gate H3, H10, J-5's C4) — H3's mechanism over the affiliation table.
- **`12e`** — H12 (`Person.precedence`) **held on a post-H6 re-measure, not on Jordan** (A-1: the
  precedence band measured a no-op); H13 (crisis threshold 3 on J-5's G-Q6; threshold 1 has **no
  mechanism** anywhere — it stays open, no precedent is forced onto it).
- **6f** — `score` dotting against the new basis (the confliction Query's caller) and 6d's
  `beneficiary:` column, `DONE·UNWIRED` until something produces `orient`. Sequence after H3; no
  separate gate beyond J-1.

### `19b` · U7-disp: `comply` · `evade / defy` · `construe` · IN · gate J-2 · `sonnet`/`opus`

Rows exist, `eligibility: own`, untyped, no predicate; `construe` is `grade: absent`. After `15`/`15c`
(DONE) the cell is `form: own_ledger, of: subject` over a `content:dispensation` claim — `tell`'s form.
Compliance is `writes: []` per the term's own row, so `_eff_comply` may be emission-only and the fold's
write-nothing refusal does not reach it. **Under arm (A)** the three key on the actor's ledger claim and
answer both an `issue`d dispensation and a `dispatch`ed order; **under (B)** `dispatch` gets its own
obey/disobey pair. **COMPLIANCE:** the fold may ask the actor's own ledger through the `PersonInterior`
snapshot the act carries, and no other (`04`'s carve-out). **FALSIFIER:** `comply` evaluable for a
person whose ledger holds no claim of the terms → fail. **R:** R-05 (+3, or +4 with V-1).

### J-3's verbs — `confer` · `establish` · `revoke` reachable from computed play · IN · gate J-3

Built per the option ruled: (i) an `office` operand bound from a question referent of kind Office (needs
a question source about seats — none exists; it would be built here); (ii) read off a held writ/commission
Record (`15c`'s `_from_content_claim` precedent, no new operand name); (iii) withheld from formation.
**FALSIFIER (i)/(ii):** `aperture 4 0` shows each executing ≥ 1 with `Act.via`; a `confer` onto an
already-held office does not deposit a claim about the outgoing holder's Tenure (the re-seating leak
H-71's record names). **R:** R-04, R-05.

### `9` · PC-SURRENDER · PC · gate J-7

If built: Yield (declared in Phase 1; accepted ends the combat, refused leaves the yielder unresisting)
maps onto the seam as a `Margin`/`wound_state` with the loser's outcome — **no fourth band, no fourth
resolver**; say whether a yield maps onto `Untouched`/`Wounded` with the surrender on the result, or the
band roster gains a value, and why. Disengage already exists as emergent behaviour in
`combat_engine_v1/wrapper.py`. Constants go to `config.py`, cited. A PC id-block release precedes any
filing (the PC block is exhausted — administrative). **FALSIFIER:** a planted yield ends the exchange
with zero further rolls (assert the bout count); a yield accepted while the yielder's objective is still
contested in the zone is refused. **E5.** If struck: one ledger row and `ED-PC-0056`'s carry-forward
closed.

### `24g` · the bodies clock + P3 individuation · SE · gate J-6

The live arm of `body_step` (shipped at the control arm `0`; `H-125` swept 0 / 10 / 67). The carrier is
settled (`24f`: cohorts eat, `Person.weight`). P3: CENSUS individuates on a demand kind — a `dispatch` to
a non-existent clerk emits `person.demanded`, and next season a Person exists whose `person.individuated`
cites it. P1's other half — a PERSON-keyed crossing cannot fire the `presence` branch because
`world_q` derives `at` from `w.sites.get(who)`; the repair is `at = parent_of(w, who)` when `who` names a
person. **FALSIFIER:** `Person.weight` or the envelope written by anything but CENSUS/MATTER → fail; a
stored aggregate where a Query is required → fail. **`/code-review` + `/simplify` only** (one number,
with its control arm).

### `24h` P7 · dispensation-as-document · SE/IN · gate J-10

Only if Jordan overturns the written refusal in `verb_table.yaml`'s `comply` typed cell.

### `26` · GO-VERSION · GO · gate J-9

Record the ruled version where code reads it; then ED-1050's deferred module re-export (*"a port never
corrects its oracle in place"*). **Nothing in this repository asserts a version before then.**
**FALSIFIER:** any `.gd` value differing from its `.py` oracle.

---

## SM. MODULES AND THE DICE ENGINE — `30` · `31a` · `31b` · `31c` · design: `33`, `36` · the contract is `A-25`, below

**Ruled:** `ED-IN-0284`, revised by `ED-IN-0285`. The vocabulary, directories, adapter model, module entry kinds,
containers and the retained-modules roster are **`A-25`** (§A), stated there once; this section stages the code
and restates none of it.

**Order:** `30` → `31a` → `31b` → `31c` → `22` (`_part4` B3). `34` (the dice engine) and `35` (scan roots) have landed; the commits are their record. `33` and `36` are design work, gated
as each says. **Retired ids, never reused:** `31d`, `31e`, `32` (cancelled before anything built them).
**Names:** `30`–`36` are these positions and this is §SM — not the pre-flight rows `S-1`…`S-10` (`_part3` §P),
not `_part6` §S. `SM-1`…`SM-15` are this section's open items.

**Reading list** (one Haiku extract, handed to every producer): `A-25`; `references/module_contracts.yaml`
`composition_roles:`; `tools/export_composition.py`; `engine/substrate/composition.py`;
`engine/season/manifest/{registry,providers}.py`; `engine/season/loop/driver.py` (`resolvable_verbs`,
`SeasonDriver.__init__`); `engine/season/seam/ladder.py` and `seam/wrappers/`; `tools/ci_common.py`; the test
files each position names.

**Grade under `CLAUDE.md` §0.2: `paper`, every position.** One commit per position. A stage is gated on the
previous stage's falsifiers being OBSERVED, not on its commit existing; a falsifier that fails stops the stage:
`git revert`, never widen (main §0.5).

**THE CONTROL EVERY STAGE KEEPS.** `build_realm(0)`'s `content_hash()` `a918cd1f…` and its one-season hash
`05f022e2…` byte-identical; `python -m engine.season.harness.aperture 4 0` reads the same per-verb funnel with the
control hash EQUAL; `resolvable_verbs()` returns the same set (compare the two sets at the build — no number is
written here); `python tools/export_composition.py --check` OK. The hashes are dated readings (`_part6` §H.1),
taken on HEAD `52ec9a54` as `build_realm(0)` then `populated.run(seasons=1, seed=0, w=w)`, `w.content_hash()`
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

### `30` · the registrar, the `modules:` roster and the refusals — no file moves · IN · gate none · `opus`/`opus` · `[infrastructure]`

**Grade:** `paper`. **Hash:** unchanged. **R:** none.
**WHERE.**
1. **Entry kinds.** `references/module_contracts.yaml` `composition_roles:` rows gain A-25's entry kind
   (`verb_call` · `step_call` · `query`) and, on a `verb_call` row, its `verb:`. ⚠ The key `kind:` is taken: it holds
   `callable | value`, refused outside `_KINDS` (`tools/export_composition.py:20`, `:69-72`). **[ASSUMPTION,
   `CLAUDE.md` §4: one key, one meaning]** the entry kind is a second key, `entry:`, validated by the exporter beside
   `kind:`; `engine/engine_params/composition.json` re-derived by the exporter.
2. **The `modules:` roster** in `engine/season/rosters.yaml`, each entry with `kind:` and `home:`, validated by the
   loader (`engine/season/data/rosters.py`). It is authored from the list `ED-IN-0284` and `ED-IN-0285` rule (A-25),
   NOT from "the directories with code": that test would drop `factions`, whose directory holds only an untracked
   identifier census. `R04_PENDING_SUBSYSTEMS` (`tests/valoria/test_engine_does_not_import_systems.py`)
   becomes COMPUTED — the `systems/` directories no roster entry names as `home:` — and its comment (a
   retirement window that no longer exists) says so, citing A-25; `test_r04_pending_composition_roles_can_only_shrink`
   reads `target.split('.', 2)[1]`, which names the module for a `modules.<name>…` target too. Point at the
   roster instead of spelling directories: `engine/season/requirements.yaml`'s `subsystem:` entries and its stale
   lines `:60` (`_architecture` "IS IN THE RETIRE SET") and `:84` ("systems/factions (deleted)");
   `tools/evacuation_plan.py`'s two hand lists (`:225-226`, `:240-241`) **and its R-CODE rule**
   (`p.startswith(('engine/', 'systems/'))`, `:382`), derived from `ci_common.MODULE_CODE_DIRS`, with a partition case
   for a `modules/` path in `tests/valoria/test_evacuation_plan.py`: nothing is tracked under `modules/` yet, and at
   `31a` `test_partition_is_total` goes red on the first file otherwise.
3. **The registrar**, in `engine/season/manifest/`, run from `SeasonDriver.__init__` before `check_rows()`
   (`loop/driver.py:249-250`), idempotent: it reads the composition rows through `engine/substrate/composition.py`
   (`ROLES`, `require`), resolves each target by string, and records it in ONE table, `MODULE_ENTRIES`. It writes
   nothing to `EFFECTS` or `PROVIDERS`; `@effect_for` stays (A-25), so `_derive_openers_from_effects` is untouched. A
   row with no `entry:` (today's one row, `mass_battle.resolve_field`) keeps its caller and is re-keyed at `31c`.
4. **Refusals at driver construction, each naming its row** — the shape of `check_rows()`
   (`manifest/registry.py:205`), licensed by `CLAUDE.md` §0.05 `:158` ("the loader's refusal per data family"):
   (a) a writing verb row with no effect and no `decline_note:`, EXEMPTING rows with `contests:` (they take the seam
   path; `tell` writes and has no effect) — replacing `driver.py:128`'s silent exclusion. The shipped tree's writing
   rows with no effect (`carry` `exchange` `forge` `repudiate` `succeed` `tie / knot`) all carry a `decline_note:`,
   so (a) passes (run 2026-10-03). ⚠ The converse arm `ED-IN-0285` names — a row carrying both an effect and a
   `decline_note:`, the two-sided `unproduced:` shape (`data/verbs.py:803-821`) — FIRES on the shipped tree:
   `oblige` and `destroy_record` carry an effect and a `decline_note:` that declines their formation (`14`), not
   their effect. **[ASSUMPTION]** `30` builds (a) one-sided; the converse waits for that column's split (`SM-9`).
   (b) an `entry: verb_call` row whose `verb:` names no verb row.
   (c) the contest roster, both halves: a verb whose `contests:` prize no prize row claims —
   `manifest/registry.py::unclaimed_contest_prizes` (`:259-285`) turns from a returned list into this refusal, and its
   caller (`engine/season/tests/test_season_shape.py:3153`) into a planted-violation test of it; and a prize row whose
   `provider:` nobody registered — after which the `manifest.has` clause in `resolvable_verbs()`
   (`driver.py:186-189`) can no longer be false, and is DELETED.
   (d) one entry registered twice.
5. **One identity per module, its directory name** (A-25): the prize rows' `module:` (`rosters.yaml:1108`,
   `personal_combat` → `combat`) and the module names in `module_contracts.yaml` `modules:`, with their reader
   (`manifest/registry.py:148-182`). `loop/sides.py:76` also reads `module:`, keyed on `mass_battle`, which keeps its
   name; `provider:` names say what runs and are not renamed. Other readers: `rg personal_combat`.
   `engine/engine_params/params_tables.yaml` is a frozen capture and is not edited (`CLAUDE.md` §5).
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

### `31a` · social contest — `seam/wrappers/sigma.py` → a host input builder + `modules/social_contest/` · IN/SC · gate `30` · `opus`/`opus` · `[infrastructure]`

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
*Wording edit deferred to this commit:* `_part4` `ED-FI-0009`'s INSTRUCTION and A-21 cite `sigma.py::_pool_of` and
`_obstacle_of`; after the split those are the host input builder's — re-point both.
**FALSIFIERS.** (1) Both hashes unchanged. (2) A module test that imports only `engine/dice_engine/` and the record
types, builds a record by hand and asserts the result record (a `dict`, `status="RESOLVED"`, with `net` and `ob`; no
`Margin` type exists, `sigma.py:44-49`). (3) In a fresh subprocess, delete the composition row → driver construction
refuses naming it (the registrar's first production row). (4) `harness.aperture 4 0`: `tell` executes the same
count, control hash EQUAL. (5) `test_importing_every_engine_module_pulls_in_no_subsystem` green over `modules/`.

### `31b` · combat — wrapper split; the reachable engine → `modules/combat/` · IN/PC · gate `31a` · `sonnet`/`opus`, a `haiku` reachability census first · `[infrastructure]`

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

### `31c` · mass battle — shed module state; wrapper split; `resolve_field`'s closure → `modules/mass_battle/` · IN/MB · gate `31b` · `sonnet`/`opus`, a `haiku` reachability census first · `[infrastructure]`

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
*Wording edit deferred to this commit:* `_part2:160` "`march` → `seam/wrappers/mass_battle.py`" → "`march` → its
host adapter and `modules/mass_battle/`".
**FALSIFIERS.** (1) Both hashes unchanged — and blind here: the realm fights no field (H-149), so `march` is not
exercised by the control; the commit says so. (2) The targeted probe instead:
`engine/season/tests/test_mass_battle_provider.py` end to end, and one constructed `march` resolved twice in ONE
process with one seed gives one result (nothing observes this today). (3) In a fresh subprocess, delete the
composition row → driver construction refuses naming it. (4) `tests/valoria/test_mass_battle_d1_morale_baseline.py`
and the mass-battle workbench's covering tests green.

### `33` · the unplugged systems — design, not relocation · IN/WR/FI · gate A-11, A-20, A-24's open threadwork question (Jordan's); `30` built · `opus`/`opus` · `[design]`

**Grade:** `paper`. Threadwork (`systems/threadwork/sim/`), fieldwork's `knots.py`, characters' `conviction.py` and
overview's `ms_track.py` are reached by nothing, and no position moves them. Re-plugging one is design work:
1. **Shed the store first.** `knots.py:155-156` (`_knots`, `_knot_id_counter`); `conviction.py:82`
   (`_conviction_state`). `ms_track.py` holds no store but writes `world.clocks['MS']` on a `world` argument (`:70`,
   `:91`), and the season `World` carries no `clocks`, so it cannot plug as it stands.
2. **The clause** is AX-4 (`04:115`), enforced at D-3 (`04:1017`); `_knots` also breaches D-10 (`04:1024`). Never
   D-8 (`04:1022`), which grades a stored aggregate.
3. **The carrier each needs:** a knot's (`H-182`: ED-912's gauge → `Tenure.degree` mapping is UNLOCATED; and
   `SM-3`); conviction's (`Person.pursuits` and scar counts — the cells commit, J-1); `rendering.py`'s stubs (A-20);
   threadwork's re-plugging into `ms_track`/`knots` (A-24).
**FALSIFIER.** A plugged module has a composition row whose deletion refuses at driver construction, and one seed
run twice in one process gives equal hashes.

### `36` · loop-resident computation modules, settlements first — design · SE/IN · gate a design of what each computes (Jordan's); `30` built · `opus`/`opus` · `[design]`

**Grade:** `paper`. Nothing is built before its design says what the module computes. Extract the rules living today
in the gate (`state/gate.py`), `world_q` and the MATTER step into `step_call` and `query` entries with a typed input
and output (A-25); the verb adapters and every MATTER write stay host. Also owns the levy-to-mass-battle feed:
`levy` moves stores, not troops (`loop/effects_governance.py:308-347`), and a season field is one troops-sized
subunit (J-18).
**FALSIFIER per extraction.** Both hashes unchanged; the rule's old host body is gone (one owner — `rg` its symbol);
deleting the module's composition row refuses at driver construction; one seed run twice in one process gives one
hash.

### §SM open items — not decided here; each names its owner

| # | item | owner |
|---|---|---|
| `SM-1` | which module owns the proceedings verbs (`convene` `open_case` `determine` `petition`, `_req_convene`, `arrangements.yaml`); until ruled they stay host | Jordan |
| `SM-2` | `2-ii`, deleting the kernel `systems/social_contest/sim/contest/`, stays HELD | Jordan (A-24) |
| `SM-3` | J-22 option A: fieldwork is a container that is not a `contest()` and needs a second role in `_ROLE_ROSTERS` (`manifest/registry.py:25`) | Jordan (§J J-22) |
| `SM-4` | deleting `systems/combat/sim/combat.py` (would remove `test_degree_ladder_single_owner.py:407`'s key and re-derive `sim_params.json` and `value_pointer_links.json` by their exporters) | Jordan (A-24) |
| `SM-5` | whether a grid or map variant is a MODE of one module (A-25's assumption) or a container of its own | Jordan |
| `SM-6` | the suspension design for a playable mode (ENCOUNTER, `04:177`, the nearest precedent) | Jordan |
| `SM-7` | a test asserting `modules/**` equals the reachable closure in both directions (the critic: licensed by `CLAUDE.md` §0.1 pt 5, as `modules/` is the port's input set; recommended, not ruled) | Jordan |
| `SM-8` | standing: only `fight`, `march` and `tell` call a module today; the rest is host interpretation until `36` | Jordan (`36`'s gate) |
| `SM-9` | `decline_note:` declines an effect on some rows and a formation on others (`oblige`, `destroy_record`); `30`'s refusal (a) stays one-sided until the column is split | `30`'s builder (`CLAUDE.md` §0, rule 5) |
| `SM-10` | Layer-0/Layer-1 text this plan does not edit: `CLAUDE.md` §3, `:407`, `:410`, `:514`; `CURRENT.md:22` and `:41` (the Dice / resolution head still names `engine/autoload/dice_engine.py`, and the currency stamp predates six heads); `04:1000`; `architecture/PLAN.md:1271`; `architecture/VOCABULARY.md:125` | Jordan |
| `SM-11` | the precondition twin of refusal (a): a declared-absence column, then a refusal, for a verb whose untyped precondition nothing evaluates (`driver.py:125-127`) — it was retired `32`'s | IN lane, after `30` |
| `SM-12` | holonic's `[engine]` tag (defined `:75`; e.g. `:1633`, `:1716`, `:1769`) means the Godot engine and collides with *engine* = the season loop | Jordan (Layer 1) |
| `SM-13` | at the port, each module's path is listed in the generated manifest resource, so export packing sees the targets `load()` resolves by string | GO lane |
| `SM-14` | RISK against the `modules/` ruling — the critic's option A (keep `systems/<name>/sim/`): unplugged code left in `systems/` looks unretained; the reachable code is the oracle heads; membership decays unnoticed. Mitigated by the `modules:` roster as the one owner of retention (`30`), `31b`'s workbench falsifier and `SM-7` | Jordan |
| `SM-15` | adopt the kernel as the social contest container's automated mode, or keep the interim provider | `22`'s measurement, then Jordan |

---

## J. THE JORDAN QUEUE — survives all five ladder steps; ranked by what each unblocks

Each item went through `CLAUDE.md` §0's ladder (superseded · irrelevant · answered by a design document ·
answered by precedent · answered by what makes sense for the architecture) and survived: two defensible
options lead to materially different games, or the answer would overwrite ratified canon, or it is a
number or content nobody can derive. **Rank = what it unblocks**, most first.

| # | question | options | consequence | unblocks |
|---|---|---|---|---|
| **J-1** | **C1 + C2** — the 105 projection cells (15 pursuits × 7 axes) and the alignment re-cell over every verb (incl. `kill`, `wound`, `fight`, `challenge`, `accept`), **including the faith-pair placement**; and the per-character / role-template migration to the fifteen (four orphans: `Utility`, `Equity`, `Identity`, `Precedent`). Ledger: `ED-IN-0261` (2026-09-28 row, `needs_jordan: true`) | approve/vet the DRAFT `candidate_pursuit_cells.md` (it **fails** the faith pair at the registry's `.60` clergy weight and passes only at `.45`), or supply your own | the cells commit, H3–H11, `12`, `12e`, 6f, H-146 arming, the verb split | **R-05 (+4 rows), R-06 reason 2, R-08** — the only path to R-08 at all |
| **J-3** | **The `office` operand (H-94)** — the realm attempts `confer` 213, `establish` 74, `revoke` 45 times in four seasons and refuses every one, because no computed act names an office and `office` is not one of the closed eight `requires_operands`. Does the vocabulary gain a seat/office operand, and from what source? | (i) a new `office` operand from a question referent of kind Office (needs a question source about seats); (ii) read it off a held writ/commission Record (`15c`'s precedent; no new name); (iii) withhold the three from formation and keep them hand-built only | (i)/(ii): realm governance verbs become reachable — the R-04 strategic layer; (iii): 332 fewer refusals and no realm governance | **R-04, R-05 (3 rows)**; shapes `22`'s `determine` referent (H-163 limit 2 shares the shape) |
| **J-2** | **`ED-IN-0210`** — is `comply` one verb or two? With **V-1** (held back from #445): split `evade / defy` into two rows on the `ED-FI-0009` precedent? | (A) one `comply` keyed on the actor's ledger claim answers both an `issue`d dispensation and a `dispatch`ed order (evidence leans A); (B) `dispatch` gets its own obey/disobey pair; V-1 yes/no | A: one row, one falsifier; B: two more rows; V-1: a witness's claim distinguishes evasion from defiance | **R-05 (+3 or +4)** via `19b` |
| **J-4** | **H-156** — verbs that are always refused still form and win scene slots (`commit`, `found`, `build`, `survey`; same shape `migrate`, `levy`; and `confer`/`establish`/`revoke` in the realm) — 34% of realm acts. ⚠ The realm figure is sized under `remit_default`, a testing fixture | (a) decline person-side until each verb's own gap closes (the `give`/`petition` precedent); (b) accept the cost as shipped; (c) widen preconditions or grade the verbs so the chooser has a reason | (a) restores `release`'s share and empties the realm of failing attempts; (b) R-01/R-02 measure with the tax in; (c) new typed cells per verb | shapes **R-05**'s counts and **R-01**'s scene share; `22` step 11 (`commit` never executes) |
| **J-22** | **`ED-FI-0009` — how does a degree reach the six inquiries, and does a refused inquiry's `finding.none` deposit?** Step 3 ALREADY CLOSED that they are graded ("Claims graded by degree; Failure emits `finding.none` and deposits nothing", RESOLVE → WITNESS, work item 4.5: `workplans/2026-09-06-season-loop-execution-plan.md:647`, a retired plan at fork ref `0671283`; carried at `engine/season/verb_table.yaml:962-969` and `engine/season/requirements.yaml:687-691`). The position hit its own stop condition on the two parts still open: (i) a degree reaches a verb only through `contests:` — the `emits` arm of the loader check (`engine/season/data/verbs.py:589-604`, a check `ED-FI-0009`'s own 2026-09-10 commit added, not ratified Layer 1 text: `04 §B.13 #12` rules on `writes`) refuses a degree-keyed `emits:` with no `contests:`, and `test_season_shape.py::test_we_only_a_verb_that_declares_contests_can_be_graded_today` pins one roll owner — while `engine/season/rosters.yaml:1031-1034` rules that investigation must not be made a contest to become gradeable; (ii) "Failure deposits nothing" is false today of `finding.none` (WITNESS deposits every Event kind, `engine/season/loop/witness.py:380`) — the same unruled question as `H-111` (`engine/season/hole_register.yaml:1608-1618`, "nobody has ruled"). Figures, the producer's scratch probes and NOT committed: at the shipped fixtures (pool 2, obstacle 2) a graded inquiry fails about 73% of draws (the 73% reproduces analytically, P(net < 2) about .74 on the ED-MB-0066 face map) and `finding.made` falls about 80% (headless, three seasons, three seeds; 76% pooled, 62-86% per seed) | (A) graded, as step 3 answered: a declared routing column that is not a prize, the `emits` arm of the loader check accepting it, a WITNESS rule that skips `finding.none` (which also answers H-111), and either `verb_capability` rows first or an accepted ~80% finding cut; (B) ungraded: the six stay flat and R-05 / R-09 say so — this REVERSES the step-3 answer rather than being a neutral default; (C) a prize, which `rosters.yaml:1031-1034` forbids | A: investigation outcomes vary by skill and a season carries far fewer findings; B: step 3's "graded by degree" is struck, findings stay near-certain, a refused inquiry still deposits as news (H-111's running reading), and R-05 "graded, not only executed" stays unmet for six verbs | `ED-FI-0009`; R-05 (graded), R-09 (a third graded chain) |
| **J-13** | **`capability`'s scale and source (H-126/H-127, `assumption`)** — R-09's roll varies by person only where a person has a `capability`; the one authored value (`NPC-088`'s `3`) was a named judgment call. Where do per-person magnitudes come from? | (i) the authored attribute `stats:` in `references/npc_registry.yaml`, through `verb_capability`'s key mapping; (ii) a rank scale you rule; (iii) leave `pool_default` everywhere a case does not name a vocation | (i)/(ii): R-09 varies by person across the corpus; (iii): R-09 varies by person in a handful of cases | **R-09**; `13`-rest's quality; `ED-FI-0009` |
| **J-11** | **Two of your six scales have no mechanism spec anywhere in code**: grid-based map combat with units (no grid, hex or tile module exists; only quarantined UI documents mention a grid) and character creation / development (nothing creates or develops a person). Are they in scope for the season loop, a separate mode, or later? | in the loop (then a spec is owed); a separate tactical/creation mode outside the season loop; deferred past M1 | decides whether R-04 can ever be `met` on its scale roster | **R-04** conjunct (3); R-05's second clause |
| **J-5** | **C3** the affiliation roster, the ten `incompatible:` cells and intensity; **C4** verb × affiliation engagement; **G-Q6** crisis threshold 3's terminal branch (restabilize, fold or destroyed; per case or fixed) | content; content; per case or fixed | — | H10, H11, H13 (R-06 texture) |
| **J-6** | **`ED-IN-0247` — the `body_step` value** (carrier settled at `24f`) | `0` (control) / `10` / `67` (the H-125 sweep), or another | a realm where dearth kills vs one where it never does | `24g`'s live arm |
| **J-7** | **Position `9`** — build §11.4 Yield/Disengage, or strike it (`ED-PC-0056`) | build (yield as a Margin, no fourth band) / strike | what a duel can end in | `9` |
| **J-8** | **`dispatch` as a remit act** — `offices.yaml`'s remit column (r2 `03`) excludes it; the tree carries it and the realm executes it 2 of 27; `ED-IN-0256` is silent; `remit_default` is "for testing purposes for now" (you, 2026-09-18) | keep it in the per-post remit / delete it per r2 `02` | which seats can `dispatch`; sizes J-4's tax under a real remit | `13d-iii`'s remit half → R-04 |
| **J-9** | **The Godot version**; and **D2**, the tenth attribute (count ruled ten, `ED-IN-0193`) | — | — | `26` → M3 |
| **J-10** | **S5-P7** — overturn the written refusal of dispensation-as-document (`verb_table.yaml`'s `comply` cell) | overturn / keep | overwrites ratified canon either way it is asked | `24h` P7 |
| **J-20** | **The off-hand slot** (`ED-PC-0055`; the retired combat plan v4.1's `⚖6`; the PC proposal's Q9) — `core.COVERAGE_GAP['partial']` is plumbed through `_transmit` and no caller passes it (`systems/combat/combat_engine_v1/core.py:208,401,431`); the roster has no shield, buckler or targe and no slot to hold one, so `main_gauche`, `paired_short` and `hook_sword` are measured in a configuration they were never used in. Is an off-hand in scope for personal combat? | (A) in scope — the proposal's minimum increment: an `offhand` field (default `None`, byte-identical), a buckler through the dead `coverage='partial'` path, a parrying dagger, a paired weapon; (B) out of scope — delete `COVERAGE_GAP['partial']` and the `coverage` parameters, duels stay single-weapon | A: sword-and-buckler and rapier-and-dagger exist and the dead key gets its caller; B: the roster stays single-weapon and the dead branch goes | the off-hand build — `proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` §13 (I-3, I-4) |
| **J-21** | **The katana anchor** (`ED-PC-0051`, the 2026-07-29 row, still `needs_jordan: true`; the retired combat plan v4.1's `⚖1b`) — a native cut edge is graded `rel = eff / CUT_REF_NATIVE` (`systems/combat/combat_engine_v1/core.py:480-481`), anchored on the katana at 1.00 (`core.py:344`): above 1.0 a benefit gated on how much the target yields to an edge, below 1.0 a penalty gated on nothing. That asymmetry is the batch's own choice (`core.py:349`); your 2026-07-29 ruling, *"cutters need to be excellent in contexts where they can CUT"* (`core.py:345-346`), does not name it. The two lowest native edges, greatsword (0.80) and hook_sword (0.71), therefore now prefer their point unarmoured (`tests/valoria/golden_element_parity.json`, `select_mode['none']`), which the row itself calls *"questionable feel"* and says *"the anchor choice is Jordan's to confirm or move"*. The v4.1 adversarial pass returned it to you (`registers/handoffs/HANDOFF_PC_history.md:146-147`); retiring that plan did not answer it, and your *"that looks like fiat"* (`registers/editorial_ledger_pc_archive.jsonl:59`) was about replacing a gate with a derivation, not about an anchor's consequence. The module's other anchors sit on the WEAKEST member of a population (`CUT_AUTH_REF`←hook_sword, `THRUST_AUTH_REF`←bear_spear, `PERC_AUTH_REF_SOFT`←the weakest hammer; `core.py:335`, `:378-380`); the katana is not the weakest native cutter (hook_sword, 0.71, is), so it follows that precedent's form and not its rule. | (A) keep the flip as a guarded asymmetry exactly as batched — the katana stays the anchor, greatsword and hook_sword pick their point unarmoured, and `test_a_poor_edge_is_poor_everywhere` (`tests/valoria/test_combat_cut_grading.py:138`) stays the guard; (B) re-anchor — move `CUT_REF_NATIVE` off one weapon onto a reference taken from the native population (its weakest member, as the module's other anchors do, or a mid-population value), so the grade is relative to the field of sixteen; the direction decides what moves (a lower reference ends the flips and lifts every native cutter above it, a higher one adds penalties), and no value has an external criterion | A: no code change; a greatsword that prefers its point unarmoured is the disclosed cost of grading the edges, and no weapon is exempted by name (scripting drift); B: a re-fit of one exported constant (`engine/engine_params/combat_engine_v1.json`) that moves every native cutter's balance — measured as the build, not asserted here | the PC calibration batch: `CUT_REF_NATIVE`'s value, and re-pinning `golden_element_parity.json` and `combat_armour_reference.json` if it moves |
| **J-18** | **The depth support stack** (`ED-MB-0041`, narrowed 2026-10-01) — your 2026-07-24 per-cell directive includes *"damage only being emitted by cells in direct contact"*, but the pool also counts support from the ranks behind the contact row, weighted by depth behind contact: the first rank behind at **1.0, full weight**, then 0.7 and 0.5, and the fourth and **every rank beyond at 0.3, with no cutoff** (`systems/mass_battle/sim/config.py:139-140`; `core/exchange.py:218-219`; `geometry.py:327-328`). Two of your own statements bear on it and neither settles it: the stack is tagged `[canonical: Jordan handoff §(1)]` (`geometry.py:307`), and your 2026-07-23 closing-ranks directive (`MB_CLOSE_RANKS`, `config.py:357`) is how rear troops become contact troops; depth also already earns relief elsewhere (`MB_DEPTH_ROTATE`, `MB_SHOCK_DEPTH_*`, `MB_ENVELOP_DEPTH_RESIST`). It reaches play: a season field is one troops-sized subunit (`massbattle._weighted_unit`, `massbattle.py:202`), so its depth varies with force size (rank counts per size were not measured). Does the directive reach the support stack? | (A) yes — cap support at the ranks a troop type's weapon reaches; depth's value then lives in the relief terms and the refill; (B) no — the stack stays as built (`[canonical: Jordan handoff §(1)]`), and the directive governs where casualties land (`MB_CELL_DAMAGE`), not what counts toward the pool | A: pool from rear ranks past the cap is removed, which changes how a larger season force scales; B: depth keeps adding pool at every size, down to the 0.3 floor | no plan position; it sets how a larger season force scales in `resolve_field`, and it is a prerequisite the squad-engagement synthesis names for per-cell quality (`proposals/2026-09-25-squad-engagement-synthesis.md:141`) |
| **J-16** | **H-173** — should a determination-opened `oblige` (a sentence) read differently from a service `oblige` to renewal, the witness channel, the one-edge rule and the term fixture? | one carrier read the same everywhere / a per-reader distinction (the opening act's verb is already recoverable) | how disposal is felt in play | nothing until `22` makes `determine` execute in a shipped world — **ask then** |
| **J-17** | **H-174** — does a bench's jurisdiction follow where a person IS (`home_of`) or where he LIVES (`residence_of`)? (The upkeep-target half is answered, A-2.) | presence / residence | whose bench binds a traveller | nothing until a `move` crosses two benches' grounds — **ask then** |
| **J-19** | **The cavalry charge recoil — graded by steadiness, or brace-gated?** (`ED-MB-0041`, narrowed 2026-10-01) — a charge is already resisted by steadiness without any brace: its moral shock is graded always-on by discipline and depth, with hold-or-brace as one multiplier of three (`_charge_shock_sigma`, `systems/mass_battle/sim/resolution.py:194-201`), and its puncture is absorbed by the defender's depth (`orchestration.py:1147-1148`). Only the charger's reciprocal recoil (`MB_CHARGE_RECOIL`) fires solely against a defender carrying the literal `brace` instruction, facing the charge, against a cavalry charger whose reach the defender matches or exceeds (`orchestration.py:1234-1242`; `config.py:385-388`). That gate is yours — bracing is prepared, never instantaneous (ED-1095, `config.py:387`), and only a wall that faces the charge repels it (ED-1091, `config.py:385`) — and the code's stated cause is *"a mounted body being pressed onto a hedge of set poles"* (`orchestration.py:1213-1215`). The recoil's size is already steadiness-graded (`_wall_prep`, discipline × depth, `resolution.py:170-174`); only its gate is brace. Should steadiness also grade the recoil, with `brace` a multiplier instead of a gate? The squad-engagement synthesis queued exactly this, unanswered (`proposals/2026-09-25-squad-engagement-synthesis.md:203-204`). | (A) yes — the recoil is graded by steadiness always-on and `brace` multiplies it, as it already does for the shock; (B) no — the recoil stays brace-gated: its cause is set poles, and steadiness already protects through the shock and the puncture | A: an unbraced, disciplined, deep body repels a charge in part, which moves cavalry-versus-infantry outcomes and recasts the cause from set poles to steadiness; B: only a prepared wall costs a charger anything beyond the existing shock and puncture grading | nothing until a season field can field cavalry (`massbattle._weighted_unit` builds one infantry Line subunit, `massbattle.py:159-161`, `:202`) — **ask then** |
| **J-14** | **Narrative #6** — complication as the modal outcome (re-bands the one degree ladder, `degree_from_net`) | — | moves every scale; overwrites a ratified shape | nothing |
| **J-15** | **Held back from #445:** `05 §4.1` (do unwatched fights resolve in one act or span scenes?) and `05 §4.2` (does duel mode open any closed moment? recommended no) | — | — | nothing in this order |

**Not on the queue, and why:**
- **The MB/PC lane rows** the 2026-09-28 roster listed have been through the ladder (`LADDER-MBPC`,
  2026-10-01: a Haiku extract, a Sonnet ladder pass, an Opus check, then a revision on that check). The pass
  is done. Its rows are appended to the lane **`_archive`** ledgers
  (`registers/editorial_ledger_{mb,pc}_archive.jsonl`), not the live ones: an id lives entirely in one file or
  the other (`tests/valoria/test_ledger_hygiene.py::test_no_ed_has_rows_split_between_a_live_ledger_and_its_archive`)
  and these ids' earlier rows are archived. **Closed at a step:** `ED-MB-0039` (step 1, premise overtaken —
  Jordan's C2 ruling left its (A)/(B) fork untouched and is not the ground), `ED-MB-0041`'s envelopment payoff
  and rout band (1), Command σ-ceiling (4, a prior ruling) and yield split (5), `ED-PC-0047` (5),
  `ED-PC-0052` and `0054` (4), `ED-PC-0053` (5). **Decided, build still owed — the row stays `open`,
  `needs_jordan: false`:** `ED-PC-0016` (1), `ED-PC-0049` (5), `ED-PC-0050` (4), `ED-MB-0045`'s 2:1 band, label
  and rename (5 / 4; its emergence verdict is not ruled). **Survived, now §J rows:** `ED-MB-0041`'s depth
  stack (J-18) and charge recoil (J-19), `ED-PC-0055` (J-20), `ED-PC-0051` (J-21).
- **The naming confirmation** Fable proposed (is the new document THE PLAN or the master) is withdrawn:
  Jordan's retire-all ruling removed the reason they were two documents.

---

## A. ANSWERED BY THE LADDER — closed; do not let any ride back onto §J

Each row names the ladder step and the closing citation. Each ratifies only as *which step answers it,
and which candidate gets attacked* — the answer is decided at its position with the code in front of it,
and an attack that lands sends the question back through the ladder, not to Jordan by default.

| # | question | step | answer / where decided |
|---|---|---|---|
| A-1 | the 2026-09-28 plan's §5.2 thirteen demotions | 1–5 | each with its step (content-hash tiebreak → H-54/H-122, step 4; MB golden → `ED-MB-0016`, step 1; held H5 → step 1; H-111 → one probe, step 5; `ED-MB-0075` → option (2), built; `mass_battle` `state: []` → `04 §C.5.1`, step 3; G-Q5 → post-H6 re-measure, step 5; M-7 / `upkeep` / `kill / wound` → contradictions 3 / 1 / 4; `titles` → `04 §B.7/§E.1`, step 3; d.1 → members' `commit` degree, attacked at `20-iv` and dropped (nothing writes a commit Tenure's `degree`, H-162; the morale source landed from stance instead, PR #450), step 5; `test_n3` floors → declared re-pin unless `11` shows a property, step 5; D-6/D-7 → swept fixtures at `18`; deleting the retire set → `requirements.yaml`'s own gate, not a question — SUPERSEDED 2026-10-02 (A-24); GD-1 → a registered gap) |
| A-2 | H-174 item 2 — the upkeep payment's target | 5 | `home_of` is the architecture's own definition of where a person is |
| A-3 | `24f`'s cohort producer | 3 | `engine/season/cohorts.yaml` — built (ED-WR-0011, `npcs.yaml` header, ED-SE-0051) |
| A-4 | R-04 reason 2's "no Faction-as-actor" | 3 | `04_CODE_ARCHITECTURE.md`: `Faction` is a resolved view with **no verbs**, never `Act.actor`; faction acts are person acts `via` seats |
| A-5 | H-163 limit 1 (rungless seats) | 3 | r2 `03`'s four anchor forms → build item `13d-iii` |
| A-6 | `29d`'s gate on `10` | 5 | the retire gate is "the loop expresses the scale"; `npe.py` has no season reader → re-gated on `29b`; the premise was verified and `29d` landed on it (PR #450) |
| A-7 | `thread_read`'s operand (H-85) | 4 | the row's own default, a two-valued `knowledge_kinds` roster (H-128's swept-fixture shape) — `14` ride-along (`R05-THREAD`) |
| A-8 | the "double `@effect_for('oblige')`" in `effects_governance.py` | — | false alarm: the second is docstring text |
| A-9 | `return_to_game_queue.yaml` | 1 | superseded by its own header (2026-08-19); retired at `ebb43bf0` |
| A-10 | GD-1, the victory requirement | 5 | registered as an `ABSENT_RULE` hole, `H-176`, at `28-iii` (PR #450) |
| A-11 | `ms_track` / `knots` deletions | 4 | wait on `27` (the retired plan's §1.3 disposition) — SUPERSEDED 2026-10-02 (A-24): the modules stay |
| A-12 | **former J-12** (does being told something move the hearer's stance?) **and position `10`'s write target** | 1 | superseded by the telling workplan, RATIFIED 2026-10-01 (main §0.6): `tell` writes no stance; told valence enters regard at read (G1); a judged deed counts there too, so this plan's stored `fight`-write rewrite of `10` is withdrawn |
| A-13 | `destroy_record` unformable for everyone | 4 | needs a record-holding question referent — `give`'s shape, at `14` |
| A-14 | v7's ruling R-7 — does the Churn Engine workstream survive `ED-IN-0204`? | 2 | its head lived under the dissolved `designs/` tree; nothing builds on it |
| A-15 | `21` item 3 — reconcile the M1 progress board | 2 | the board was retired at `ebb43bf0`; m1 row 3 now reads THE NINE |
| A-16 | `14`'s antonym rows `waive`, `deposed`, `fray / loosen` | 3 | `04 §A.3` row 14: the closing half is ONE `release` verb, generic over kind; `revoke` takes away. No new closer rows |
| A-17 | what "built out" means for R-05 | 4 | executes in computed play — U7's own acceptance (*"≥ 1 world — in the corpus, not merely in a hand-built `Act`"*) |
| A-18 | must R-01's `met` include a realm reading? | 5 | no — a row is measured where its `measure:` says; the realm is context |
| A-19 | is U6's `probed` divergence a defect or a property? | 5 | a property (a deposit raises a later-round question — R-03's channel), **conditional on P-4**: same-arm divergence makes it a determinism defect |
| A-20 | where `27`'s `rendering.py` stubs write | 5 | not into the overview clocks (no season analogue, ED-WR-0011 option A); a retained or season-native carrier, or struck |
| A-21 | `ED-FI-0009`'s obstacle source | 4 | `sigma.py::_obstacle_of`'s existing non-person default; one roll owner (S27.2) — stop if that needs a `contests:` shape |
| A-22 | who seats `p_b`/`p_c` from the `cast:` — `13` or `17`? | 1 | `13`'s execution record (2026-09-28 plan §8.7) assigned the remainder to `17` |
| A-23 | Fable's proposal to run FI `ED-FI-0009` as a parallel lane | 5 | serial — it shares `verb_table.yaml` and `effects_information.py` with `14` (`_part3` O.3) |
| A-24 | do the `retire-set` `systems/` trees go — `characters`, `fieldwork`, `overview`, and the merged `29b`–`29d` deletions of `factions`, `world`, `settlements/sim` | ruled by Jordan 2026-10-02 (`ED-IN-0283`) | NO. The `systems/` folders are the homes of their systems. `29e`, `29f` and `29a`-ms (built `21c7133f`, `1b68d590`, `72623b61`) were reversed on this branch and cancelled. OPEN, put to Jordan and not decided here: whether the PR #450 deletions return; `2-ii` (held); threadwork re-plugging into `ms_track`/`knots`; CLAUDE.md §3 and CURRENT.md's season-loop row, which still describe the retire-set |
| A-25 | how do the modules, the containers and the season loop relate, and where does code go? | ruled by Jordan 2026-10-03 (`ED-IN-0284`), revised by `ED-IN-0285` | **the contract, stated once: `### A-25`, below this table.** Staged by §SM; A-24's open items stay open |

### A-25 · the module contract — the one statement (`ED-IN-0284`, revised by `ED-IN-0285`)

Every other surface points here and restates none of it. Reference (`CLAUDE.md` §0.05): §SM's code is the mechanism.
**Vocabulary** (one meaning each, defined again where code invokes it, `CLAUDE.md` §4). *Engine*: the season loop,
`engine/season/`, the host. *Dice engine*: the d10 chain, `degree_from_net` and σ-leverage, `engine/dice_engine/`
(formerly `engine/autoload/`), not the engine. *Module*: running code reached by a composition row, in
`modules/<name>/`; it never reads or writes `World`, holds no token, keeps no state between calls, imports no module.
*Container*: a module with transient state that the player can also play, reached by a seam or a verb. MINIGAME: personal
combat and its tactical grid, mass battle and its strategic map, social contests, fieldwork and investigations; MANAGEMENT
SPACE: governance, faction management, the character sheet; WORLD SURFACE: where the player meets NPCs and events (Tails
Noir, Lacuna, Disco Elysium, Esoteric Ebb, Shadows of Doubt, Pentiment). [ASSUMPTION] a grid or map variant is a MODE of
one module (`SM-5`). *Subsystem*: only personal combat, social contest, mass battle (holonic §41.2). *The fold*: RESOLVE,
`loop/resolve.py`. *Register, registry, ledger, roster*: each defined once, in the docstring of the code invoking it
(`tools/pathres.py`, `data/rosters.py`, `manifest/registry.py`).
**Directories.** `modules/<name>/`: reachable running code only, no data, no prose; membership is static reachability from
the composition targets, the PATH seam's `wrapper`/`combatant` and the registrar's entries. `systems/<name>/` keeps its
name: legacy, workbench, unplugged and design-stub homes; nothing reachable. `engine/season/decision/` stays host (the
AX-2 scan is path-keyed, `04:1131-1132`): the AUTOMATED mode of the management spaces and the world surface. `game/`
(Godot, holonic §45): the playable scenes; the port's `core/modules/<name>/` holds the module and its automated mode.
**The adapter.** A verb is a loop-side adapter: the loop builds a typed INPUT record from a read-only projection of
`World` (host `queries/` build projections), calls the module ENTRY, interprets the typed OUTPUT and writes `World`
through the gate under its own token (`04` D-22, D-24, §A.2 as written). CALL verbs call a module: `fight`, `march`,
`tell`, each declared by `contests:` and a prize row. ACTION verbs change `World` themselves, their results reaching a
module later through a projection (`levy`, `migrate`, `found`, `build`, `transfer`).
**Module entries**, on `references/module_contracts.yaml` `composition_roles:` rows: `verb_call` (a verb's adapter calls
it), `step_call` (a step such as MATTER), `query` (a projection consumer). `EFFECTS`, `@effect_for` and every effect body
stay host; no verb row names a module. Two owners say which module is called — the prize row (`contest_subsystems`) and
the composition row; all else derives (`CLAUDE.md` §0.05 cl. 3). One identity per module: its directory name (`combat`).
**Containers.** Transient state dies with the call; persistent state would be a second store (AX-4, `04:115`) and returns
only through the fold. AUTOMATED mode: headless, for non-player parties and the Python oracle. PLAYABLE mode: a `game/`
scene, for which the driver suspends (`SM-6`). A party test at the seam picks one; the host gets the same typed output
either way. Fieldwork is a minigame that is not a `contest()` (`SM-3`). The world surface is DELIBERATE's player mode
(`season(choose, …)`, `loop/driver.py:330`): it reads the player's own `View`/`Question`/`Candidate` and emits acts,
owning no game state, as the management spaces do. Knowledge and witness are HOST.
**The roster** (one owner from `30`: `rosters.yaml`'s `modules:`, with `kind:` and `home:`). Minigames, the subsystems:
`combat`, `mass_battle`, `social_contest` (→ `modules/` at `31b`, `31c`, `31a`); `fieldwork` (no module code). Management
spaces: governance, faction management, character sheet (host verbs; `decision/`; `systems/characters/`). World surface:
`game/` + host DELIBERATE, unbuilt. Loop-resident: `settlements` (`36`); `overview`, `threadwork` (unplugged; `33`, A-24).
Data registers: `world`, `npcs` (`references/npc_registry.yaml`). Host: decision making (the AX-2 island); proceedings,
which schedule contests (`SM-1`). Not systems, kept as stubs: `_architecture`, `articulation`, `ui`, `victory`.
