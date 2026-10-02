# Valoria — Master Workplan v8, part 4: Batch 2 (the gate-free core of THE NINE) · Batch 3 (proceedings and the tails)

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094). Same status and held-back list as `valoria_master_workplan_v8.md`; this part carries no decision of its own.
## Reads after `workplans/valoria_master_workplan_v8_part3.md`, whose O-sections (batches, edges, census, run discipline, stopping rule) bind every item here.
## Grade under `CLAUDE.md` §0.2: `paper`. Each item carries the text it needs from the retired plans; none points at a retired file as its owner.

---

## B2. BATCH 2 — THE GATE-FREE CORE OF THE NINE

**Reading list** (one Haiku extract): this part's B2 items; `engine/season/requirements.yaml` R-01…R-09
`measure:`/`blocks:` lines; `engine/season/hole_register.yaml` rows H-62, H-79, H-85, H-94, H-98,
H-116, H-126, H-127, H-146, H-148, H-156, H-163, H-165, H-175; `verb_table.yaml` rows `tell`, `fight`,
`march`, `give`, `oblige`, `commit`, `release`, the six inquiries, and the ten rows with no
predicate/effect; `write_matrix.yaml` `Person` rows; `rosters.yaml` `requires_operands`,
`combat_degree_bands`, `verb_capability`, `field_*_weight`; `decision/options.py` (`opening_set`,
`operands_for`, `_derive_operand`); `seam/ladder.py` (`combat_degree`, the general branch);
`seam/wrappers/sigma.py` (`_pool_of`, `_obstacle_of`); `loop/effects_combat.py::_eff_march` (the M4
stance write — the stored half of regard); `harness/corpus_run.py::build_at`; `harness/populated.py`'s
seat builder; `engine/season/offices.yaml` header; `proposals/2026-09-04-degree-sweep/wd_collect.py`.

### `11` · U6 — R-01/R-02 corpus measurement · IN · **DONE 2026-10-02: first measurement 2026-10-01, re-take 2026-10-02** · the acceptance command is kept here because `requirements.yaml` cites it

**Both runs landed (PR #451).** At `2x3`, over 143 cases, reconvergence reads none 77.13 % · actor 43.03 % · total 38.47 % (baseline, `c2ee345a`) and none 77.22 % · actor 42.59 % · total 38.58 % (re-take, `8b03e518`, across `14`, `13d-iii` and `17-cast`): no arm moved by half a point, against a 96 % bar, so R-02 is `met` and R-01 stays `not_met` (`engine/season/requirements.yaml`, whose dated paragraphs label each figure; `proposals/2026-09-04-degree-sweep/runs/WD_LOG.txt` is the committed record, the 36 cells are untracked and rebuilt by the commands below). The instrument's run-to-run noise is not measured. Re-run it only when a build changes what a fork can reach.
**Acceptance — verbatim** (carried from U6; slices re-derived for 143):

```
cd proposals/2026-09-04-degree-sweep
for m in none actor total; do for s in default narrow 2x3; do \
  for r in "0 36" "36 72" "72 108" "108 143"; do python wd_chunk.py $m $s $r; done; done; done
python wd_collect.py
cd - && python -m engine.season.harness.corpus_run
```

**Acceptance point is `2x3`, not the shipped default** (U6's own correction: the acceptance is
cell-dependent). **Declare the prior before running:** `2x3` has read **100.00 %, zero divergences**
and never below the bar. **OBSERVABLE:** reconvergence **< 96 % at `2x3`**, cells committed under
`runs/`. **FALSIFIER:** ≥ 96 % ⇒ both rows stay `not_met` and the commit names which channel is still
closed — **H-116 first** (`belief_contradicts` narrows only on `PERSON_PREDICATES`, so a deposited
consequence about a non-person cannot narrow a later candidate set). Do not re-pin. **Control:** the
`none ≥ default` arm is the only control this instrument yields; say so. `fan_out_mode` is R-07's
fixture, not this one's. **Not here any more:** `test_n3`'s floors and the reverted build-order item 4 (`budget()` counting
`granted_acts`) belong to the telling workplan's T4, which re-pins the floors and closes that question
(main §0.6); re-land item 4 only after T4, against T4's floors. **R:** R-01, R-02 — on the printed number only. **Records:** both rows' `measured:` paragraphs
cite the run and its tree; R-02's `measure:` comment re-pointed off the retired plan (`_part6` §H.3).

### `ED-FI-0009` · a degree producer for the six inquiries · FI · gate `8` (E7); reads better after `13`-rest · `sonnet` build, `opus` critic · `[design]`

**What the tree rules:** investigation is not a seam (`rosters.yaml`'s ruling forbids giving the
inquiries a prize); the loop IS the mechanism — RESOLVE → WITNESS, *"Claims graded by degree; Failure
emits `finding.none` and deposits nothing"* (closed at ladder step 3 on 2026-09-06, work item 4.5).
What is missing is a degree producer. `ED-FI-0009` is `open`, `needs_jordan: true` (J-22, 2026-10-01: its stop condition hit, see its last ledger row); its earlier carve's
obstacle column, attribute gate and depth derivation were overturned by a critic and are **not** to be
re-introduced.
**INSTRUCTION.** Compose on the single owners: the actor's pool from `sigma.py::_pool_of` (capability via
`rosters.yaml: verb_capability`, else `pool_default`), the obstacle from `_obstacle_of`'s existing
default for a non-person subject, and the degree from `dice_engine.degree_from_net` — the one ladder.
**Stop condition:** R-09's set-equality test pins exactly one roll owner (S27.2). If producing an
inquiry degree cannot route through that owner without a `contests:` shape, stop and register — that is
the design question, not a reason to add a second resolver. Depth has no carrier; build none. Effect
target: `loop/effects_information.py` (the inquiries' effects) — `Failure` deposits nothing.
**FALSIFIER:** `corpus_run`'s `DEGREES RESOLVED` is non-empty for an inquiry; a `Failure` inquiry
deposits no claim (asserted on a seeded case); the one-roll-owner test stays green. **Hash:** corpus pins
move (declared). **R:** R-05 (graded, not only executed), R-09 (a third graded chain).

### `10` · U5 / R-07 — CARVED OUT to the telling workplan (main §0.6)

Nothing here. Position `10` belongs to `workplans/2026-10-01-telling-workplan.md` (RATIFIED 2026-10-01),
which re-scoped it to `T0`→`G8`: `tell` writes no stance, and regard is computed at read. This plan's
earlier rewrite of `10` (a stored stance write on a resolved `fight`) is **withdrawn** — G1 counts a
judged deed at read, so a stored deed write would be a second route to one fact. The AX-7 wiring that
rode along stays registered and unbuilt until the telling workplan's T6 closes (`_part3` E16).

### `13`-rest · W28-cast: the remaining overlays · IN · **STOPPED at its pilot (the user's rule)** · `sonnet` author, `opus` critic · `[design]`

**Pilot run 2026-10-02 (`17-cast`):** eight differentiated NPC overlays; DISTINCT EXECUTED SETS 41 with none, 41 with the pilot, 26 with a uniform fixture cast (seed 0, an instrument that was not committed). ⚠ **The metric could not have shown this pilot working**: all eight cases were singletons in the no-overlay arm, so the ceiling on a rise from them was 0 (not +5). What moved: 2 of 8 cases (NPC-038 on its `ought:` keys, NPC-083 on its `office:` keys, whose second office seats an institution as a person), mean verbs 6.62 → 7.25. `knows:` is refused at load: seeding an initial belief needs a sixth `Claim`-construction site or pre-history Events through the existing witness sites (`01_AXIOMS.md` AX-7), neither built, and nothing in the plan's observables needs it. An ought's `predicate` is a declared non-causal label (`H-185`). **Whether to scale is the user's, on a better observable** (per-case set change against the no-overlay arm, Q4 referents). The text below is the original instruction.


41 NPC + 97 ARC `cast:` overlays in `engine/season/cases/exercises/*.yaml` (never `cases/chain/*.yaml` in
place). Schema: `who_acts`, `one_line`, `knowledge`; entries naming a player become `WAITS-ON-PLAYER`. NPC
lane first. **`capability` is authored only where both hold:** the case text names a vocation a key in
`rosters.yaml: verb_capability` covers, **and** a magnitude has a source. `capability`'s scale is
unruled (H-126/H-127 `assumption`); `NPC-088`'s `3` was a named judgment call, not canon. **Do not repeat
that judgment 138 times** — where no source exists, leave `pool_default` and record it; the scale is J-13.
**FALSIFIER:** a `one_line` token-matched from the case prose; a `capability` with no named source.
**Critic:** checks the `WAITS-ON-PLAYER` split and every authored number. **Hash:** corpus pins move
(declared). **R:** R-06, R-09 (only as far as sourced `capability` reaches).

### `27` · WR-SCOPE remainder · WR · gate — · `opus`/`opus` · `[design]`

**BUILT 2026-10-01 (PR #451):** both `rendering.py` stubs struck with their reasons at the site (the season has no clock to wire them to: `loop/census.py`, ED-WR-0011 option A); `ED-WR-0003` closed at ladder step 2
(an `ED-WR-0003` superseding row); `attempt_mending` calls `recover()` and costs > 0 (only tests call it; `environment_in_equilibrium` defaults to False);
`threadwork/sim/{co_movement,opposing}.py` import neither `ms_track` nor `knots`, which unblocks `29a`-ms and `29f`. **Remainder, each outside this position's scope** (`HANDOFF_WR.md`):
the `R-14` practitioner-resilience term (arithmetic unruled); Mending aimed at the mender's own configuration (`coherence.mend_resting_point` has no non-test caller); and
`collective.py`'s and `opposing.py`'s Mending feedback. **R:** none.

**Batch 2 close:** agonist/antagonist → `/code-review` → `/simplify` → `layer-conformance` (Lens B on
`14`'s fold) → terminal Opus critique → `/close` (full suite once). The forward
sweep's check 1 **must** re-run `register --requirements`, `corpus_run`, `aperture 4 0` and compare
against `_part2`'s readings; every row that moved gets a `measured:` paragraph in the same close.

---

## B3. BATCH 3 — PROCEEDINGS CORE, THE TAILS, AND THE LAST DELETIONS

**Reading list** (one Haiku extract): this part's B3 items; `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md`
PHASE 2 steps 11–16, PHASE 3, PHASE 4; `04_VERBS.md`'s `speak` spec (in that proposal);
`rosters.yaml` prize rows (`interim: true`) and the `chronicle` channel; `epistemic.py`'s `chronicle`
admission; `data/requires.py`'s `cardinality` form (raises today); `seam/ladder.py`'s extension site;
`engine/season/arrangements.yaml` header; H-161, H-163, H-173, H-174; `loop/effects_information.py`
(`_eff_open_case`, `_eff_determine`) and `loop/effects_shared.py` (`_new_oblige_term`, `_oblige_term`).

### `22` · PROC-B, steps 11–16 — the contest-resolution core · SC · gate `13d-iii` (E11) · `opus`/`opus` (arrangements transcription `sonnet`) · `[design]`

**State (2026-09-30, `a1282b02`):** steps 6/7/9/10 DONE at `18`/`19`; step 8 built (a citation); step 7
carries a caveat — `judging_set`'s `matter` parameter is not load-bearing yet. `arrangements.yaml` holds
3 of 12 rows (deliberately; its header says so) and `standing_routes` does not exist — step 6's DONE rests
on a falsifier its row count does not satisfy as written; re-grade at step 12. **Size it as its own build,
possibly sub-batched** — the 2026-09-30 attempt found it is a new provider, an obstacle model and
degree-keyed effects, not a routine addition.
- **Step 11 (rest):** C-7's vote-quorum conjunct. `cardinality` has no implementation
  (`data/requires.py` raises on it). It needs a second referent — which Proposition is "the disposition"
  a bench member's `commit` targets — that no operand derives; and `commit` never executes (H-156). A
  naive fix makes `determine` refuse always and reddens two passing tests. Implement the form, or state
  in the commit why it waits on J-4 (H-161 holds the gap).
- **Step 12:** `speak` — a typed cell, `contests: "a matter"`, four bands (the `speak` spec in
  `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md` — design intent, never the reason it is right); `_eff_speak` in `loop/effects_information.py` only if `writes:` is non-empty.
- **Step 13:** the two prize rows drop `interim: true` and repoint from `sigma_leverage` — **a row
  change, not a code change** (ED-SC-0033 cl. 2); `chronicle` deleted (`rosters.yaml`, `epistemic.py`); the
  `rung=` fix (C-8) reads `world_q.place_of`, not a `Scene.place` field (there is none).
- **Step 14:** the obstacle. **Contradiction 3, resolved (carried):** take the obstacle **CEILING**, its
  value injected and swept (`sigma_leverage`), never a pool floor — a ceiling caps how hard a matter can
  get; a floor raises everyone's competence, a statement about people. M-7 fails at the 1D floor
  (`p_success` 0.0006 at Ob 3). The seam's own obstacle site is deleted (ED-SC-0033 cl. 3, one owner).
  `ED-SC-0038` is RULED; its per-matter / single-margin pick is this step's build decision.
- **Step 15:** the provider — `engine/season/seam/wrappers/proceedings.py`, resolved **by string at
  boot**, returning **a Margin, never a winner** (`04` provider rule); a misspelled manifest row fails at
  boot naming the row.
- **Step 16 — THE BAR (M2's first gate):** two seeded proceedings run end to end with zero authored acts,
  twice, byte-identical including the hash, and `causes[]` walks from the determination back to the date
  that raised it.

**FALSIFIER:** a planted `if arrangement.id == "tribunal"` reddens the closure test; M-7 re-run at the
floor clears Ob ≥ 4 after the ceiling; THE BAR as stated. **Hash:** corpus + realm move (declared).
**Lens B:** the provider returns a Margin; the obstacle has one owner. **R:** R-05 (`speak`, `determine`
executing), R-09 (`speak` graded), M2. **Latent questions it reaches:** H-173 (a sentence vs a service
`oblige`) and H-174 (jurisdiction by presence or residence) become live the moment `determine` executes in
a shipped world — `_part5` §L says when they escalate.

### `22a` → `23` → `22b` · proceedings PHASE 3 · PART-E-0/2 · proceedings PHASE 4 · SC/IN · gate `22` · `sonnet` producer once the shape is fixed, `opus` critic

- **`22a`** — proceedings PHASE 3 (steps 17–21), after `22` (and `15d`, DONE).
- **`23`** — typed id wrappers over the same `H` output (`content_hash` folds identical strings — the
  byte-identity control); the `data/` loaders behind one entry; the remaining loader invariants, **each
  with a planted violation naming its row**: invariant 4 (only what S-8 found still flat), invariant 7
  (F.20b's three body-literal Event kinds as declared columns — *"the loop as built cannot run under the
  loader as specified"*). Enumerate the effects corpus through `data/files.py::effects_modules()`, never a
  hand list. CI runs no type-checker, so the **runtime** grade is the real one and the commit says so.
  **FALSIFIER:** a `SeatId` passed as `Act.actor` is not refused in the fold → fail. **Hash:** none.
  (A declared departure: PART E steps 0 and 2 were "unscheduled by design" in the arc-sequence spine;
  scheduled here.)
- **`22b`** — proceedings PHASE 4 (steps 23–27; step 22 = `Tenure.term`, DONE at `17b`).

### `24h` P5 · S5 revolt as a Query · SE/IN · gate — · `{parallel worktree}` · `opus` · `[design]`

The revolt **Query** in `queries/world_q.py` or `queries/faction_q.py` — a read, never a write — the
season successor of `systems/world/sim/insurgency_pipeline.py` (deleted at `29d`, PR #450). **FALSIFIER:** the
Query writes nothing (AX-2; the Query family by module); a seeded realm where its preconditions hold
returns ≥ 1, one where they do not returns 0. **R:** R-06/R-07 texture (the world generating drama with
nobody watching — NERS R).

### `24h` P6 · forswearing · SE/IN · gate `14` (E9), after `22`'s `verb_table.yaml` edits · `opus` · `[design]`

`repudiate`'s costs (the forswearing half of S5). **FALSIFIER:** a forsworn commitment costs what the row
declares and nothing else; no proper-noun branch. **R:** R-05 texture.

### `29f` → `29e` → `29a`-ms · fieldwork `knots`, characters, `ms_track` · IN · gate `14`, `27` (E2, E3) · `sonnet` · `[cleanup]`

- **`29f`:** `systems/fieldwork/sim/knots.py` (ED-912's ±5 gauge maps to `Tenure.degree`, F.4 — the
  plan said `14` records it, **`14` did not** (it declined `tie / knot`; `H-182` says no position owns `_eff_tie`), so
  `29f` writes the mapping into `H-182`'s cite, not invented, and then deletes); `engine/tests/test_knots_ed912.py` → `FORK:`.
- **`29e`:** `systems/characters/sim/conviction.py` (← `knots.py`); `beliefs.py` already went at `28-0`'s
  follow-up (PR #450). `test_conviction_roster_single_owner.py`'s `systems.characters` site re-pointed.
- **`29a`-ms:** `systems/overview/sim/ms_track.py`.
**FALSIFIER:** `opposing.py` no longer imports `sustain_knot`; nothing imports `apply_ms_delta`;
`grep -rn "systems.overview\|systems.fieldwork\|systems.characters"` returns only fork-ledger rows.
**Hash:** none.

### `2-ii` · RET-SC: the kernel and the veto · IN/SC · gate `22` (E4) · `sonnet` producer, `opus` critic on the veto only, `haiku` for the inbound-site census · `[cleanup]`

**INSTRUCTION (carried from the retired position 2, corrected for what has since landed).**
`systems/social_contest/sim/contest/` (16 files); `parliamentary_{vote,stay}.py` already went at `29b`
(PR #450). `engine/tests/test_contest_kernel.py` → `FORK:`. **Re-derive the deletion set from `git ls-files`, never a
`find` count.** The veto (`degree_extension.py`) is relocated as a forwarded `extension=` at
`seam/ladder.py`'s degree site — a veto that can only demote, never a re-banding (`04`: `seam/wrappers/*`
own nothing and return a Margin). **Keep the logical name** — the prize rows key on it. Repoint every
inbound site: `module_contracts.yaml`, `canonical_sources.yaml`, `descriptor_registry.yaml`,
`lane_assignments.yaml`, `ci_checks_registry.yaml`, the `skills/` files that name it;
`engine/engine_params/sim_params.json`'s `degree_extension.py` row re-derived by its exporter;
`tests/valoria/test_degree_ladder_single_owner.py`'s path-string registry key;
`test_engine_does_not_import_systems.py`'s `systems.social_contest` fixture re-pointed. The `sim-regression`
CI job folds into `unit-tests` here; `test_sigma_leverage_parity.py` (substrate) moves out of
`engine/tests`.
**OBSERVABLE:** `rg -n social_contest engine/ tools/ tests/ references/ skills/` returns only logical-name
rows; content hash stationary; `PROBE FLIPS 0`. **FALSIFIER:** plant a `tell` contest the old extension
demoted, at a pool where it would otherwise read its top band — red before the move, green after; and
`seam/ladder.py::degree_of` never imports `systems.social_contest` (the `NESTED_BASELINE = 0` ratchet).
**Hash:** none. **Lens B:** the veto relocation only.

**Batch 3 close:** as Batch 2. After it, the end-state (`_part6` §E) should hold except for Batch 4's
Jordan-gated rows; the close checks each end-state bullet against the tree and records which still fail.
