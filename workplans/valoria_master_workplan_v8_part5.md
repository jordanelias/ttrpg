# Valoria — Master Workplan v8, part 5: Batch 4 (opens per ruling) · systems as modules (30–33) · the Jordan queue · what the ladder already answered

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

## SM. SYSTEMS AS MODULES — `30`–`33` · RULED 2026-10-03 (`ED-IN-0284`); the contract and the placement rule are `A-25`, below

**Reading list** (one Haiku extract, handed to every producer): `references/module_contracts.yaml`
`composition_roles:` · `tools/export_composition.py` · `engine/substrate/composition.py` ·
`engine/season/manifest/{registry,providers}.py` · `engine/season/loop/driver.py` (`resolvable_verbs`,
`SeasonDriver.__init__`) · `engine/season/data/{files,verbs}.py` · `engine/season/verb_table.yaml` (the rows
named per position) · `architecture/meta/04_CODE_ARCHITECTURE.md` §A.2, G.2.1–G.2.2, PART A (T-k), PART D
rows 3, 8, 22, 24, 25, 27 · the test files named under each position.

**What it is.** Jordan ruled (`ED-IN-0284`; his words are verbatim in the ledger row) that every system
under `systems/` is a module that plugs into the season loop, which stays at `engine/season/` as the host.
Layer 1 is already amended to say so (`04` Status, §A.2's seam rows; holonic Status, §41.2, §45). These four
positions stage the code to match. None changes what the game does, so every stage is graded on a byte-
identity control, not on a new behaviour.

**Names, so nobody resolves a collision by guessing.** `30`–`33` are these positions (`31` names the family `31a`–`31e`) and
this section is §SM — not the pre-flight rows `S-1`…`S-10` (`_part3` §P) and not `_part6` §S (Lens B subjects). *System* is a directory under
`systems/` that is a module; *subsystem* keeps meaning only personal combat, social contest and mass battle
(holonic §41.2). The directories with no code — `_architecture`, `articulation`, `npcs`, `ui`, `victory` —
are not systems and no stage touches them (`A-25`).

**Grade under `CLAUDE.md` §0.2: `paper`, every position.** A stage is gated on the previous stage's
falsifiers being OBSERVED, not on its commit existing. A falsifier that fails stops the stage: `git revert`,
never widen (main §0.5).

**THE CONTROL EVERY STAGE KEEPS.** `build_realm(0)`'s `content_hash()` `a918cd1f…` and its one-season hash
`05f022e2…` byte-identical; `python -m engine.season.harness.aperture 4 0` reads the same per-verb funnel
with the control hash EQUAL; `resolvable_verbs()` returns the same set (compare the two sets at the build —
no number is written here); `python tools/export_composition.py --check` OK. The two hashes are dated
readings (`_part6` §H.1), re-read 2026-10-03 on HEAD `52ec9a54` as `build_realm(0)` and then
`populated.run(seasons=1, seed=0, w=w)`, `w.content_hash()` after each. Re-read both on the stage's base
commit before it starts (`CLAUDE.md` §0.1 pt 3, row four).

**What is true today** (each opened 2026-10-03; re-derive by symbol — lines drift):
- *Registration is by import, and nothing observes a drop.* `@provider` and `@effect_for` are plain dict
  writes (`manifest/providers.py:34-42`, `loop/effects_shared.py:39-46`) that run when a module is
  imported; `seam/__init__.py:48-56` records the measured silent drop (`tell` executed 0 times, no error).
  `resolvable_verbs()` (`loop/driver.py:101`) excludes a verb with `writes:` and no effect (`:128`), or with
  no registered provider, without a word. `data/verbs.py::rows_without_a_producer` (`:1064-1070`) is "a
  REPORT" and "a flag", and it reads `writes:` columns against the matrix and never `EFFECTS`, so it could
  not see a dropped effect even if it ran at boot. `tests/valoria/test_season_providers_are_registered.py`
  asserts `personal_combat` and `sigma_leverage` only (`:44`; not `mass_battle`), and its mutation arm
  (`:51-93`) clears `PROVIDERS` and nothing else. **Nothing observes a dropped effect, so `30` adds the
  observer before `31` moves an effect file.**
- *`World.boot` is on no run path.* `loop/driver.py:239-248` says so; `SeasonDriver.__init__` (`:234`) is
  where every run passes and where `check_rows()` is called (`:250`). The adjudication wired its registrar at
  `World.boot` (`state/world.py:1322-1335`), which would execute on no run (`CLAUDE.md` §0.2). `30` wires it
  at `SeasonDriver.__init__`.
- *Tests under `engine/season/tests/` are inside the import ban.* `tests/valoria/test_engine_does_not_import_systems.py`
  exempts `engine/tests/` only (`rel.startswith('tests/')`, `:110`, `:122`), so a test there that imports a
  moved provider counts against `BASELINE_TOTAL = 0`. It reaches the provider through `manifest.PROVIDERS`
  after the registrar has run (the path the engine uses), or the test moves to `tests/valoria/`; its
  assertion is unchanged either way.
- *The corpus helpers walk `engine/season/` by path, and a moved file leaves them silently.*
  `files.loop_modules()` (`data/files.py:182`), `effects_modules()` (`:206`) and `package_modules()` (`:264`)
  each pass over fewer files with a green floor; `files.py:193-195` names the floor-plus-superset discipline
  as the only observer.

**Two orchestrator judgments, marked so each reverts alone (`CLAUDE.md` §0 `needs_jordan` rule 5; Jordan has
ruled neither):** **[ASSUMPTION 1]** a module that registers nothing — threadwork, characters, overview and
world today, and fieldwork, whose tagged rows have `writes: []` — gets no `register.py` and no composition
row until it has something to register, and the loader check that a tagged verb row names a system validates
the `system:` value against the roster of systems, not against registered modules. **[ASSUMPTION 2]** the
registration surface is `composition_roles` in `references/module_contracts.yaml` (an existing blocking
`--check`, no new mechanism, a declared caller for `ID-13`), and verb ownership is a `system:` column in the
one `verb_table.yaml` (`rosters.yaml:43-44`, `04` D-25: no per-module data file) — the adjudicator's
recommendations A and A.

### `30` · the registrar, the `system:` tag and the dropped-effect observer — no file moves · IN · gate `ED-IN-0284` (met) · `opus`/`opus` · `[infrastructure]`

**Grade:** `paper`. **Hash:** unchanged. **R:** none.
**WHERE.**
1. `engine/season/verb_table.yaml`: a `system:` key on EVERY row — the adjudication's assignments, and `host` on
   the rest. `fight` (combat) · `march` (mass_battle) · `convene` (social_contest) · `work` `restore` `transfer`
   `move` `migrate` `found` `build` (settlements) · `confer` `establish` `revoke` `oblige` `levy` (factions) ·
   `examine` `interview` `research` `surveil` `thread_read` `reconstruct` (fieldwork). `host` rows: `release`,
   `tell` `utter` `commit` `give` `create_record` `destroy_record` `survey` `dispatch`, every other row the
   adjudication does not assign, and `open_case` `determine` `issue` `petition` `speak` until `32` re-tags the
   proceedings verbs (the rows `22` adds carry `system: social_contest`). `host` means the loop supplies the
   row's effect itself, and it is the one value that is not a directory. `engine/season/data/verbs.py` refuses a
   row with no `system:` and a value outside roster ∪ {`host`}, naming the row — an optional key would make
   "forgot the tag" and "host by design" the same bytes, and no refusal could observe the first (`CLAUDE.md`
   §0.1 pt 2). `verb_table.yaml` growth meets no size cap
   (`references/atomization_rules.yaml:172-174`, `on_exceed: "skip"`).
2. The roster of systems: one owner, `engine/season/rosters.yaml` (the one rosters file, `:43-44`). It is
   authored once from the `systems/` directory names less the code-less ones; load refuses an entry with no
   `systems/<name>/` directory, and a system added later is a roster edit made on purpose (the loader cannot
   tell a new directory from a code-less one, and does not try).
3. `references/module_contracts.yaml` `composition_roles:` — one row `<system>.register` →
   `systems.<system>.sim.register:register` per module that registers something, cooked into
   `engine/engine_params/composition.json` by `tools/export_composition.py`, whose `--check` imports and
   resolves each target at export (`:15-18`). `30` adds none for a real module (nothing has anything to
   register until `31a`); its covering test plants one.
4. `engine/season/manifest/` — the registrar. It reads the rows through `engine/substrate/composition.py`
   (`ROLES`, `require`), calls each module's `register(host)` once, hands it the host's registration surface
   (a write to `EFFECTS`, `PROVIDERS`, `REQUIRES_PREDICATES`; `32` adds `sides` and `degree`), records which
   module wrote each key, and refuses a second writer of one key. Registration is explicit table writes —
   no decorator. It runs from `SeasonDriver.__init__` before `check_rows()` (`loop/driver.py:250`), is
   idempotent, and `resolvable_verbs()` must not answer from a table the registrar has not filled (it calls
   the registrar, or refuses).
5. Four loader refusals (licensed: `CLAUDE.md` §0.05 cl. 4, "the loader's refusal per data family"), firing at
   driver construction and naming the row and its system — the shape of `check_rows()`
   (`manifest/registry.py:202-219`) and `check_roles` (`:187-199`, a `NoProducer`): (i) a row with no `system:`, or a
   value outside roster ∪ {`host`}; (ii) a writing row whose effect is absent — from the host for `host` rows,
   from the module for tagged rows — replacing `driver.py:128`'s silent exclusion with a refusal (the observer,
   and what `rows_without_a_producer` is not); (iii) a module registering an effect or precondition for a verb whose
   row is not tagged with that module's system; (iv) a prize row in `rosters.yaml: contest_subsystems` that
   names a `provider:` nobody registered (`manifest.has`, `registry.py:80`, is read by `resolvable_verbs()`
   today and asserted by nothing). The converse of (iii) — a tagged row's effect came from its own module — is
   added by `32`'s last item; until then the rows not yet moved are still registered by the host.
**Re-point in the same commit.**
- `tests/valoria/test_engine_does_not_import_systems.py` `R04_PENDING_SUBSYSTEMS` (`:607-610`) shrinks to
  `{'_architecture', 'articulation', 'npcs', 'ui', 'victory'}` — the code-less names, kept because they are
  not modules (`A-25`). `test_r04_pending_composition_roles_can_only_shrink` permits a shrink and would
  otherwise refuse the first `<system>.register` row. The comment above the set (`:598-606`) describes a
  retirement window that no longer exists: reword it to "ED-IN-0284 (2026-10-03): every system under
  `systems/` is a module of the loop; these five are the code-less directories that are NOT systems (`_part5`
  A-25). A composition role targeting one of them is a defect: nothing can register from a directory with no
  code."
- `tests/valoria/test_season_providers_are_registered.py`: the first test also asserts every provider the
  `rosters.yaml: contest_subsystems` prize rows name (this adds `mass_battle`); the `_MUTATION` arm
  (`:51-93`) also clears `EFFECTS` and asserts `resolvable_verbs()` strictly shrinks.
- A covering test for the registrar and the four refusals, each with a planted violation naming its row
  (`CLAUDE.md` §0.1 pt 2): a planted module's effect lands in `EFFECTS`; a second writer of one key refuses;
  a deleted composition row refuses naming the row and its system; a row with no `system:`, or an off-roster
  one, refuses; a writing row with
  its effect cleared refuses naming the verb; a module registering for another system's row
  refuses; a prize row whose provider is not registered refuses naming the prize.
**FALSIFIERS** (observed in this order). (1) The two hashes unchanged. (2) Delete a module's composition row
and driver construction refuses, naming the row that lost its registration and the system it belongs to — at
`30` on the planted module; `31a` re-observes it on `social_contest` and each later item on its own system. (3) The extended `_MUTATION` arm: clearing `EFFECTS`
shrinks `resolvable_verbs()` AND refusal (ii) fires naming the verb on a driver built after the clear — the
first shows the silent drop is real, the second that it is no longer silent. (4) A process that calls
`resolvable_verbs()` and never builds a driver gets the full set or a refusal, never a short set.
(5) `harness.aperture` funnel unchanged; `export_composition --check` OK;
`test_importing_every_engine_module_pulls_in_no_subsystem` green (registration happens at driver
construction, by string, never at import). (6) No floor is re-pinned: no file leaves a corpus at `30`.
⚠ **`ID-13`, READ EXACTLY.** `30` declares no composition role (its only row is planted by its test), so no role
lacks a caller. What `30` leaves unexercised in production is `register(host)` alone; the tag, refusals (i), (ii)
and (iv) and the registrar's pass over the (empty) row set run at every driver construction, and that is its
done-claim. `31a` is the next commit and the first production call of `register(host)`.

### `31a`–`31e` · whole-file moves · IN · gate `30`'s falsifiers observed (`31b`–`31e` also wait on `31a`) · `sonnet`/`opus`, a `haiku` inbound-site census first · `[infrastructure]`

**Grade:** `paper`. **Hash:** unchanged. **R:** none. One commit per item (main §0.4). Each item moves a
file, adds `register.py` and its composition row, replaces the decorator with an explicit write, and
re-points its inbound sites in the same commit. A moved file takes the adjudication's names (`provider.py`;
an `effects_*.py` keeps its own). `systems/<name>/sim/` is created where it was deleted at `29b`–`29d`: exact-
file `FORK:5c5d8ec6` rows exist for those directories' old files (an `__init__.py` among them), so create none
of those names — a namespace package needs no marker — and read `references/restructure_ledger.md` before
naming a file. This does not answer A-24's open question about the PR #450 deletions.
- **`31a` — `seam/wrappers/sigma.py` → `systems/social_contest/sim/provider.py`.** `register.py` writes the
  provider `("contest", "sigma_leverage")`; row `social_contest.register`. The `"a standing"` prize row
  (`rosters.yaml: contest_subsystems`, `interim: true`, `:1134`) is unchanged — its `provider:` is a name.
  **`22` waits for this item (E17).** It also carries the corpus change below and re-points
  `test_season_providers_are_registered.py`'s first test from "importing the seam registers" (import-time
  registration is what the ruling retires) to "constructing the driver registers every provider the prize
  rows name", still in a subprocess so no other test's imports can make it pass. `seam/wrappers/__init__.py:39-41`
  (the `from . import` lines that are the registration today) loses this member; the package, and
  `seam/__init__.py:56`'s import of it, go with the last wrapper. **First check the helpers.** `ED-FI-0009` (`_part4` B2) plans a
  host effect on `sigma.py::_pool_of` and `_obstacle_of`; a host effect may not import a module (`A-25`
  placement rule 4). If the census finds a host reader or a planned one, placement rule 3 splits the helper
  to the host in this commit and the provider imports it. [UNVERIFIED which the FI producer will need — J-22
  is open.]
  *Wording edits deferred to this commit (old → new; found 2026-10-03; nothing else changes).* (a)
  `_part6` D.2 header `:53` "(`references/module_contracts.yaml`; one survives)" → "(`references/module_contracts.yaml`;
  one survived Batch 1 and retires at `31c`; the `<system>.register` rows from `31a` on are the registration
  surface, `_part5` §SM)"; and `:57`, the `mass_battle.resolve_field` cell "**the one survivor (a)** — consumed by
  `seam/wrappers/mass_battle.py`" → "**the one survivor (a)** until `31c`, when the provider imports its own engine and the
  role goes (`ID-13`)" (D.1 `:45` is a dated DONE row: leave it). (b) `_part4:55-56` "the actor's pool from
  `sigma.py::_pool_of` (capability via `rosters.yaml: verb_capability`, else `pool_default`), the obstacle from
  `_obstacle_of`'s existing default for a non-person subject" → "the actor's pool from `_pool_of` (capability via
  `rosters.yaml: verb_capability`, else `pool_default`) and the obstacle from `_obstacle_of`'s existing default for a
  non-person subject — host helpers after `31a`'s split, or the social-contest provider's until then (`_part5` §SM
  `31a`)"; the rest of the sentence is unchanged.
- **`31b` — `seam/wrappers/combat.py` → `systems/combat/sim/provider.py`.** Not `combat.py`:
  `systems/combat/sim/combat.py` sits where the home goes; its header retires it (ED-900/904/1029) and nothing
  imports it: `31b` PROPOSES to delete it with an exact-file `FORK:` row and to remove the
  `tests/valoria/test_degree_ladder_single_owner.py:407` allowlist key in the same commit, held for Jordan's
  word (`A-24`; a deletion in `systems/` was reversed once already); `test_tn7_always.py` is checked for a
  by-path read (it scans `engine` and `systems` by root, and its docstring names the file at `:19`), and
  `engine/engine_params/sim_params.json` and `value_pointer_links.json` cite the file (found 2026-10-03), so
  the deletion would re-derive both with their exporters, never by hand. Row `combat.register`. `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}`
  is unchanged: the one path entry stays `engine/substrate/pc_engine.py`, which the moved provider reaches by
  import (a system may import `engine`). `files.COMBAT_SEAM_PY` (`data/files.py:250`) goes or is re-pointed;
  its only other mention is `seam/__init__.py:25`.
- **`31c` — `seam/wrappers/mass_battle.py` → `systems/mass_battle/sim/provider.py`.** Row
  `mass_battle.register`. The role `mass_battle.resolve_field` (`module_contracts.yaml:103-105`) loses its
  only caller — the module imports its own engine — and goes in the same commit (`ID-13`), with
  `composition.json` re-derived by its exporter. Falsifier: `engine/season/tests/test_mass_battle_provider.py`
  end to end. *Wording edit deferred to this commit:* `_part2:160` "`march` → `seam/wrappers/mass_battle.py`" →
  "`march` → the mass-battle module's registered provider (`systems/mass_battle/sim/provider.py`)".
- **`31d` — `loop/effects_migration.py`, `loop/effects_founding.py` → `systems/settlements/sim/`** (`move`
  `migrate` `found` `build`), names kept. Their helpers (`_operand`, `_decline_ascent`) stay in
  `loop/effects_shared.py`, imported by the module; the `@effect_for` decorators become explicit writes. `data/verbs.py::_derive_openers_from_effects` (`:331`)
  AST-walks `files.effects_modules()`, so the derived openers lose these four verbs silently unless the
  corpus follows (falsifier below).
- **`31e` — `data/arrangements.py` + `arrangements.yaml` → `systems/social_contest/sim/`, CONDITIONAL.**
  ⚠ The adjudication moves both, but its own contract and placement rule 1 keep a data loader in the host,
  and `04` §A.2 (`data/` = "the ONE loader") and PART A's `ID-12 · ID-5 · ID-13` row say the same; its
  conflict table does not list this. Its stated ground is "zero production importers", and what was found
  2026-10-03 is tests only (`test_arrangements.py`, `test_stress_proceedings_rehost.py`, `test_u7_remit.py`).
  **Default build:** the loader stays in `data/`; the YAML moves only if the builder reads rule 2 (canon data
  a loader reads; precedent `systems/settlements/valoria_geography_v30.yaml`, read by path at
  `harness/populated.py:86` and `:470`) to allow it, and the commit says which and why (`CLAUDE.md` §0 rule 5). If the
  loader does move, `test_h115_the_fourteen_load_time_raises_are_unchanged`
  (`engine/season/tests/test_season_shape.py:645`) counts `raise SystemExit` over the model set and re-pins,
  and the YAML's path anchor is re-pointed. Nothing waits on `31e`.

**Carried by `31a`, extended by the rest — the corpus.**
- `data/files.py` `loop_modules()`, `effects_modules()`, `package_modules()` → the host plus the sim
  directory of each registered module, computed from the composition rows with `subsystem_sim_dir(name)`
  (`:157`) and never listed. Consumers in `engine/season/tests/test_season_shape.py`: `package_modules()` at
  `:642`, `:2401`, `:6976`, `:13106`; `loop_modules()` at `:2107`, `:13835`;
  `test_jordan_no_definition_is_hardcoded_in_a_body` (`:2346`); the margin-producer scan whose literal
  expectation `{"seam/wrappers/sigma.py"}` (`:13113`) re-keys to the moved path. Also
  `engine/season/tests/test_g2_token.py`: `_tree_sources` reads `engine/season/` only and its floor is
  `:103`. Corpus = host plus registered modules, floors re-pinned in the same commit (a re-pin is declared,
  `CLAUDE.md` §7), and `04` D-27's literal scan (`:1042`, "a scan of `loop/`, `seam/`, `decision/`") reads the
  same corpus. `decision/` stays the host's: the AX-2 scan is a directory (`files.decision_modules()`, `:235`)
  and nothing leaves it.
- **The instrument that does not exist:** nothing observes a moved file leaving a by-path corpus with a
  green floor. So each re-pin names the file that must now be in the corpus (a superset assertion), not only
  a count.

**Inbound sites** (re-derive with an `ast` walk and `rg 'seam[./]wrappers'`; found 2026-10-03):
`engine/season/tests/test_season_shape.py` `:8398`, `:8447`, `:12793`, `:12860`, `:12882`, `:13165`;
`engine/season/tests/test_mass_battle_provider.py` `:72`, `:84`, `:106`, `:126`, `:149`, `:194`;
`engine/season/tests/test_governance_build.py` `:1052`, `:1089`; `engine/season/tests/test_combat_band_edges.py:41`;
`tests/valoria/test_mass_battle_d1_morale_baseline.py:41`; `engine/reference/degree-sweep/sweep_core.py:77`
(under `engine/`, outside the test exemption); `engine/season/tests/test_migrate_capacity.py:357-367`
(expects `effects_migration.py` in a `files.package_modules()` walk); `engine/season/tests/test_works_founding.py:446`
(`from ..loop import effects_founding`).
**Process surfaces re-pointed in `31a`.** `tools/export_sim_params.py` `SCAN_DIRS` (`:39-43`) is a hand list
that names neither `systems/settlements/sim` nor `systems/factions/sim`, so moved constants would leave the
exporter's scan: derive it from `tools/ci_common.py::sim_reference_roots()` (`:83-101`, already a glob over
`systems/*/sim`; `tools/ci_sim_fabrication_check.py:211` already uses the prefix twin), then re-derive
`engine/engine_params/sim_params.json` and its sibling artifacts with their exporter and run its `--check`,
never by hand (`CLAUDE.md` §0.05 cl. 3). `skills/layer-conformance/SKILL.md:8,205-208` and
`.claude/commands/close.md:30` (Lens B scope: `engine/season/` AND the modules registered into it, as the
Layer-1 Status line now reads). `tools/evacuation_plan.py`'s verdict text for these systems said they stay
only because a composition role targets them; reworded 2026-10-03 (rule ids and verdicts unchanged), so nothing is
left to re-point there. One pointer row in each affected lane's
`registers/handoffs/HANDOFF_<LANE>.md` (SC, PC, MB, SE). **When the last wrapper leaves** (whichever of
`31a`–`31c` lands last), the two path-neutral clauses the Layer-1 amendment left — "`seam/wrappers/` until the
relocation lands" (`04:147-148`) and "`seam/wrappers/*` today" (`04:182`) — are struck in that same commit:
a Layer-1 text edit the amendment pre-announced, to be said as such in the commit message. The exact edits (old → new,
verified 2026-10-03): `04:147-148` "seam/        contest() · ladder · the contest providers: one per deferred subsystem, registered by
the module under `systems/<name>/sim/` that owns it (`seam/wrappers/` until the relocation lands)" → "seam/
contest() · ladder · nothing else: each contest provider is registered by the module under `systems/<name>/sim/`
that owns it (ED-IN-0284)"; `04:182` "the contest providers (`seam/wrappers/*` today; registered by
`systems/<name>/sim/` once relocated)" → "the contest providers (registered by `systems/<name>/sim/`)".
**FALSIFIERS.** The two hashes; the `aperture` funnel; per item, delete that module's composition row and
driver construction refuses naming it; `test_importing_every_engine_module_pulls_in_no_subsystem` green;
`31c`: `test_mass_battle_provider.py`; `31d`: `tenure_kinds_without_an_opener()` (`data/verbs.py:831`)
returns the same list before and after (`succeed`, `tie` and `knot` still reported, `rosters.yaml`
`tenure_kinds`); every re-pinned floor sits under a superset assertion; the one `engine/season/tests` file
covering each touched test.

### `32` · splits by row ownership · IN · gate `31`'s falsifiers observed · `sonnet`/`opus` (`opus` for the `sides` and `degree` registrations) · `[infrastructure]`

**Grade:** `paper`. **Hash:** unchanged. **R:** none. Where one file holds two systems' rows, split at the row
boundary: `04` G.2.1's test is the single writer of a value, and where one file writes two modules' rows the
decomposition is wrong at that value. The host's registration surface gains two tables first, a `sides`
derivation and a `degree(result)` read per prize, each a dict write like the existing three. One commit per
item; items 1–4 wait on `31b`, `31c`, `31a`, `31d` respectively, item 5 on `31a`'s corpus work. **The last item to land also adds the converse of `30`'s refusal (iii)**: every
row's effect was supplied by the party its `system:` names (`host` included).
1. **combat:** `seam/ladder.py::combat_degree` (`:124-168`) → the combat module's registered `degree(result)`
   read; `loop/effects_combat.py` `fight` (`_eff_kill`, `:109-271`) with `_scar` (`:39`; its only writer is
   `fight`; the file splits at `:274`) → `systems/combat/sim/`.
2. **mass_battle:** `seam/ladder.py::field_degree` (`:171-192`); `loop/effects_combat.py::_eff_march`
   (`:274-370`); `loop/sides.py:76-118` (the `mass_battle` branch becomes the provider's `sides`; the host
   keeps the default, `:120-121`) → `systems/mass_battle/sim/`.
3. **social_contest:** `loop/effects_governance.py::_eff_convene` (`:224-256`) and
   `loop/predicates.py::_req_convene` (`:455-494`) → `systems/social_contest/sim/`; the calendar step stays
   host (it is a step). Which of `open_case` `determine` `issue` `petition`
   (`loop/effects_information.py:163-321`) are proceedings verbs is decided by the row tag, once, here — the
   adjudication assigns none — and after `22` has settled `determine` and `speak` (that file is `22`'s,
   `_part3` O.3).
4. **settlements:** `loop/effects_economy.py` `work` `restore` `transfer` (`:21-237`; `_rise` goes with
   `work` and `restore`) → `systems/settlements/sim/`. `_renewals` (`:240-307`) stays in the host, beside
   `may_renew` (`state/gate.py:394`), in `loop/effects_shared.py`: moving it with `transfer` would make a
   module call a module (placement rule 6).
5. **factions:** `loop/effects_governance.py` `confer` `establish` `revoke` `oblige` `levy` (`:26-154`,
   `:194-211`, `:259-347`) and `loop/predicates.py` `:147-453` minus `_req_release` (`:315`) →
   `systems/factions/sim/` (new; the `31` caution on `FORK:` names applies). The range also holds
   `_req_dispatch` (`:447-453`): `dispatch` carries `system: host` at `30`, so under placement rule 2 its predicate stays
   host unless its tag is changed to a system (a one-row decision here; J-8 is about `dispatch`'s remit, not its
   owner). A helper in the range that a predicate staying in the host also calls (`office_described_by`,
   `:194`, is the one to check) stays host (placement rule 3). `release` (`_eff_release`,
   `:157-193`) is the generic closer (`04` AX-6, `:119`) and goes to `loop/effects_shared.py`;
   `queries/faction_q.py` (a view, `04` §B.6.1), the gate's seat block (the seat-authority rules live with the
   gate that enforces them, `loop/predicates.py:33-39`) and `offices.yaml` stay host. `confer`, `establish`
   and `revoke` go to factions because under §B.6.1 a faction acts only through a seat.
Optional moves the adjudication names — `harness/arms.py`, `harness/scarce.py`,
`governance_spine.py`/`.yaml`, `harness/conviction_spread.py` — are harness apparatus; this plan schedules
none.
**FALSIFIER per item.** The two hashes; the `resolvable_verbs()` set; delete the module's composition row
and driver construction refuses; the one `engine/season/tests` file covering the touched code; the extended
`_MUTATION`-style test also clears the `sides` and `degree` tables;
`tests/valoria/test_degree_ladder_single_owner.py::test_no_new_hand_rolled_ladder` — its scan roots include
`systems` (`SCAN_ROOTS`, `:458`), so a moved body is still scanned and what can fail is a new offender; its
allowlist keys name none of the moved files. No module imports another (holonic R-2, `:206-207`).
⚠ **T-k, NOT IN THE ADJUDICATION'S CONFLICT TABLE.** `04` PART A T-k reads "the ladder lives once, in the
seam". Reading: `degree_of` (`seam/ladder.py:195`) stays the one dispatcher and `degree_from_net` the one
margin ladder; `combat_degree` and `field_degree` read a module's own result against roster edges
(`combat_band_edges`, `field_degree_bands`) that stay in `rosters.yaml`, and a moved read holds no band table
of its own. If `layer-conformance` Lens B reads T-k against items 1 and 2's degree moves, those two moves
revert alone and the rest of `32` stands.
*Recorded for this stage (wording and one boundary; nothing else changes).* (1) **T-k conforms under the narrow
reading, no Layer-1 amendment.** `04:181` defines the seam ladder as `degree(margin, veto?) -> Degree` over exported
band edges — the margin ladder, which stays (`ladder.py:96-116`, `degree_ladder()`); `degree_of` (`:195-229`) stays
the one dispatcher. `combat_degree` (`:124-168`) and `field_degree` (`:171-192`) read a provider's own result against
roster edges and hold no band table; T-k's hazard (`04:1156`, F.9) is a second margin ladder, which neither is. Write
that reading into `seam/ladder.py`'s module docstring in this stage. `test_degree_ladder_single_owner.py` was opened
2026-10-03: `SCAN_ROOTS` includes `systems` (`:458`) and its allowlist is keyed by path (`:407`), so a moved body is
still scanned and what can fail is a new offender. (2) **The smallest Layer-1 text, only if Lens B objects:** `04:122`
"the ladder lives once, in the seam" → "the margin ladder (`degree(margin) -> Degree`, exported band edges) lives once,
in the seam, with `degree_of` its one dispatcher; a provider whose result is not a margin registers one
`degree(result)` read over the roster's band edges and holds no edges of its own". (3) **This stage must not touch the
`engine.autoload` `sys.path` read at `seam/ladder.py:106-116`** (declared again at `engine/season/__init__.py:17`): it
reaches `engine/autoload/dice_engine.py` by inserting the repo root and degrades to `_LADDER_ERROR` rather than failing,
so a move or rename of that package would surface as a named gap at the ladder, not as a red test.

### `33` · the unplugged systems — design work, not relocation · IN/WR/FI · gate `32`'s falsifiers observed; A-11 and A-20 decide the carrier; A-24's open threadwork re-plugging (Jordan's) · `opus`/`opus` · `[design]`

**Grade:** `paper`. Threadwork (`systems/threadwork/sim/`), fieldwork's `knots.py`, characters' `conviction.py`
and overview's `ms_track.py` register nothing after `32`, and this plan relocates none of their code. World is
a data module (`rosters.yaml: factions`, tier 1; `adjacency_map.jsx`) and registers nothing; characters'
loaders (`data/cast.py`, `data/pursuits.py`) and the AX-2-pinned `decision/options.py` readers stay host.
Re-plugging any of the four is design work, in this order:
1. **Shed the store first.** `knots.py` holds `_knots` and `_knot_id_counter` at module level (`:155-156`; its
   own `[ASSUMPTION]` at `:27-28`); `conviction.py` holds `_conviction_state` (`:82`; `[ASSUMPTION]` at
   `:17-20`). `ms_track.py` has no store but mutates `world.clocks['MS']` on a `world` argument
   (`apply_ms_baseline_decay`, `apply_ms_delta`; `:69`, `:90`), its docstring names `world.clocks['MS']` and a
   dependency on `sim/autoload/game_state` (`:10`, `:27-28`), a module that is deleted, and the season
   `World` carries no `clocks` mapping (`state/world.py`; `04` PART D row 17) — it cannot plug as it stands.
2. **The clause is located.** **The clause is AX-4 (`04:115`, one store per carrier, one write path), enforced
   at D-3 (`04:1017`); `_knots` also breaches D-10 (`04:1024`, two homes for one relation); holonic §47 `:1800`
   is the port form. Cite these, never D-8** (`04:1022`, which grades a stored aggregate). `_conviction_state`
   (`conviction.py:82`) is per-person interior state, AX-3 (`04:117`) and AX-4 (`04:115`). (The Layer-1 amendment moved PART D
   down five lines, so a cite of `04:1017` from before 2026-10-03 lands on row 3.)
3. **The dependency line was not an import** — fixed 2026-10-03: the docstring now names the real late import
   (`systems.characters.sim.conviction`, `apply_conviction_scar`, at the call site `knots.py:349`). The path the
   tests use is the same (`engine/tests/test_knots_ed912.py:142`, `:159`).
4. **The carrier each needs first.** A knot's season carrier (the `knot` Tenure kind and `firsthand_via_knot`
   exist; the `tie / knot` effect was declined at `14`; ED-912's gauge → `Tenure.degree` mapping is UNLOCATED,
   `H-182`); conviction's (`Person.pursuits` and scar counts — the cells commit, `12`, J-1); `rendering.py`'s
   stubs (A-20); threadwork's re-plugging into `ms_track`/`knots`, which is open with Jordan (A-24). `33`
   builds none of it until he answers.
**FALSIFIER.** A plugged system has a composition row whose deletion refuses at driver construction; and after
plugging, one seed run twice in one process gives equal hashes (a store that survives between worlds makes
the second run differ).

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
| A-25 | how do the systems under `systems/` relate to the season loop, and where does a new file go? | ruled by Jordan 2026-10-03 (`ED-IN-0284`) | **RULED: every system under `systems/` is a module that plugs into the season loop, which stays at `engine/season/` as the host** (his words are verbatim in the ledger row). Staged as `30`–`33` (§SM above). Layer 1 was amended in the same ruling (the amended text is in `architecture/meta/04_CODE_ARCHITECTURE.md` and `architecture/holonic_ARCHITECTURE.md`): `04` Status and §A.2's seam rows; holonic Status, §41.2 (`system:`), §45 (`register.gd`). Two conflicts are READ, not amended: `04` G.2.2 ("never along subject") through G.2.1's ownership test, and D-22/D-24 as grading the contest seam rather than an effect's body (holonic §42's `owns:` already lets a module own writes). A-24's OPEN items are unchanged by this ruling and stay open: whether the PR #450 deletions return, `2-ii`, threadwork re-plugging, and `CLAUDE.md` §3 / `CURRENT.md`'s wording.<br>**The contract, six lines.** (1) *Declares*, in the host's files and never a file of its own: `system: <name>` on its verb rows in the one `verb_table.yaml` (every row there carries a `system:`, and `host` on the rows the loop owns); its prize rows in `rosters.yaml: contest_subsystems`; any world-gen rows the host's one loader reads. (2) *Supplies*, by `register(host)` alone, as explicit table writes and never a decorator: an effect for each tagged row whose `writes:` is non-empty, an untyped precondition for each tagged row the typed grammar cannot evaluate, and for each prize it provides the provider, its `sides` derivation and its `degree(result)` read. (3) *Reads* the host freely: `engine/` names no system, and a system imports `engine`. (4) *May not*: construct a `Token` or open a write of its own (an effect body runs inside the fold's open write, as today); add an Event kind (`04` D-25); import another module (holonic R-2); be reached by the host by import; or hold module-level state — [the clause is AX-4 (`04:115`, one store per carrier, one write path), enforced at D-3 (`04:1017`); `_knots` also breaches D-10 (`04:1024`, two homes for one relation); holonic §47 `:1800` is the port form. Cite these, never D-8]. (5) *The host keeps* everything with no registration and no token of its own: steps, the gate and the seat-authority rules in it, `release`, queries, `decision/`, the data loaders, the manifest and the registrar, `seam/contest` and `degree_of`, the witness channels, the harness. (6) *Registering nothing is lawful* (a tagged row with `writes: []`; an unplugged system), and a writing row whose effect is absent — from its module for a tagged row, from the host for a `host` row — REFUSES at driver construction, naming the row.<br>**Placement of a new file, six lines.** (1) It mints a token, holds a store, runs a step, loads a data file, or answers a question nothing writes → `engine/season/`. (2) It carries a verb's body, resolves a prize (provider, sides, degree read), or supplies canon data a loader reads → `systems/<name>/sim/`, `<name>` being the `system:` on the verb, prize or data row. (3) Both → split at the row boundary; the shared helper goes to the host. (4) If the host would need `import systems…` to reach it, it is host code; a module is reached only by a registry row. (5) New data is a tagged row in the host's one file for that family, never a new file under the module. (6) If a module would call another module, stop and route through a host query or a row.<br>**The code-less directories** (Jordan, same ruling): `_architecture` is not a system; `articulation` and `ui` are game presentation, not systems of gameplay; `victory` is a set of conditions, not a system; `npcs` is a decision-making concern but, for the loop's purposes, a centralized register of information like the settlement data (its head stays `references/npc_registry.yaml` and the season's `npcs.yaml` export). None is a plug-in module, none gets a `register.py`, none is deleted, and `R04_PENDING_SUBSYSTEMS` keeps exactly those names.<br>**Corrections applied, not copied, from the adjudication** (a read-only Fable 5.1 pass: model output, not a ruling). (a) `atomization_rules.yaml` has no cap for `engine/season/*.yaml`; its rule is `on_exceed: "skip"` (`references/atomization_rules.yaml:172-174`), so `verb_table.yaml` growth meets none. (b) D-8 (`04:1022`) grades a stored aggregate, so the clause forbidding module-level stores in `knots.py` and `conviction.py` is located before it is cited, never cited as D-8. (c) `knots.py:30-32`'s `sim/personal/conviction` is a docstring dependency line, not a verified import. And a fourth, found while writing this plan: (d) the adjudication wires its registrar at `World.boot`, which is on no run path (`loop/driver.py:239-248`); `30` wires it at `SeasonDriver.__init__`. The `04` line cites here are current ones: the Layer-1 amendment moved PART D down five lines, so the adjudication's `04:1017` is now row 3, not row 8.<br>**Two orchestrator judgments, taken under `CLAUDE.md` §0 `needs_jordan` rule 5 and revertible alone (`_part6` §K item 7): [ASSUMPTION]** (i) a module that registers nothing gets no `register.py` and no composition row until it has something to register, and the loader check that a tagged row names a system validates the `system:` value against the roster of systems; (ii) the registration surface is `composition_roles` in `references/module_contracts.yaml` and verb ownership is a `system:` column in the one `verb_table.yaml` — the adjudicator's recommendations A and A. Jordan has ruled neither. |
