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

### `11-fix` · U6's instrument repair · IN · gate — · `sonnet` build, `opus` read · `[simulation]`

**The break** (R-01's `measured:`, 2026-09-30): over the 143-case corpus, `wd_collect.py` fails its
own assertion that `probed` (the deliberation count) does not depend on `observation_deposit_mode` —
`{'none': 21717, 'actor': 21954, 'total': 21897}` — at the first fixture point, so no reconvergence rate
is computed at any point. The tool's comment says why it assumed equality (*"`pack_scenes` is called for
every person with a question, whatever their candidate set"*); since U2 a deposit under `actor`/`total`
can raise a new Q2 question in a later round that `none` never raises.
**INSTRUCTION.** First run pre-flight P-4 (the same cell twice). **If `probed` differs between two runs
of the same arm, stop** — it is a determinism defect; register it and do not touch the assertion. If it
is stable per arm: replace the cross-arm equality with a per-arm report (`probed` printed for each arm),
compute the reconvergence rate per arm over that arm's own deliberations, keep the completeness assertion
(`covers == list(range(len(CASES)))`), derive slice bounds from `len(wd_acceptance.CASES)`, and keep
`arm9_forking.fork_case` imported **unmodified** (`wd_acceptance.py`: a re-implemented probe measuring a
different thing is the confound). **No engine code.**
**FALSIFIER:** the 36-cell sweep completes; `wd_acceptance.json` and `WD_LOG.txt` are rewritten — check
with `md5sum` before and after (`CLAUDE.md` §0.1 pt 3 row 4: a collector that exits 0 and writes nothing
is the failure); the `none ≥ default` control is printed. **Hash:** n/a. **R:** none by itself.

### `11` · U6 — the first corpus R-01/R-02 measurement · IN · gate `11-fix` · `sonnet` runs, `opus` reads the number · `[simulation]`

**Run twice in Batch 2:** (i) the baseline, on HEAD right after `11-fix`; (ii) the re-take after
`13d-iii`, declaring both trees. The pair is the control for what Batch 2's builds did to propagation.
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
(main §0.6); re-land item 4 only after T4, against T4's floors. **Timing:** the baseline is taken before
telling T3a lands or after its T6 closes, never across them (E15). **R:** R-01, R-02 — on the printed number only. **Records:** both rows' `measured:` paragraphs
cite the run and its tree; R-02's `measure:` comment re-pointed off the retired plan (`_part6` §H.3).

### `8` · H-98(b): the wound-count band edge becomes data · IN/PC · gate — · `sonnet` build, `opus` critic · `[patch]`

**What is already built and must not be rebuilt:** `seam/wrappers/combat.py` returns `wound_state` per
party (`felled`, `wounds`, `max_wounds`, `health_remaining`, `health_full`), and `seam/ladder.py` grades
it (`combat_degree`). A fourth band is **forbidden** (`ladder.py`: *"A FOURTH BAND … HAS NO SOURCE IN THE
DATA and is NOT invented"*). Half (a) — the general branch's producer — has no further subject (`tell`
supplies it via `seam/wrappers/sigma.py`).
**INSTRUCTION (b).** The edge is a literal (`if st["felled"]: FELLED` / `WOUNDED if st["wounds"] > 0
else UNTOUCHED`). Move it to data: a `combat_band_edges` row keyed on `combat_degree_bands`, with a
declared sweep (Jordan 2026-09-02: *"definitions are not hardcoded"*), read by `combat_degree`. Grade
H-98 by the half closed. **FALSIFIER:** an edge on a quantity the tracker does not return refuses at
load; an edge set to `wounds > max_wounds` yields `UNTOUCHED` for every fought subject, with `≥ 1`
fought subject asserted. **Hash:** none expected — assert equal. **R:** R-09 (band provenance). **E5:**
never interleaved with the cells commit or `9`.

### `ED-FI-0009` · a degree producer for the six inquiries · FI · gate `8` (E7); reads better after `13`-rest · `sonnet` build, `opus` critic · `[design]`

**What the tree rules:** investigation is not a seam (`rosters.yaml`'s ruling forbids giving the
inquiries a prize); the loop IS the mechanism — RESOLVE → WITNESS, *"Claims graded by degree; Failure
emits `finding.none` and deposits nothing"* (closed at ladder step 3 on 2026-09-06, work item 4.5).
What is missing is a degree producer. `ED-FI-0009` is `open`, `needs_jordan: false`; its earlier carve's
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

### `14` · U7-own — the unbuilt rows · IN · gate telling T4 (E14), E8 · `sonnet` build, `opus` critic · `[design]`

**INSTRUCTION, corrected.** The retired text said "land the verbs in antonym pairs: `commit`+`repudiate`,
`oblige`+`waive`, `succeed`+`deposed`, `tie / knot`+`fray / loosen`, then `forge`, `restore`, `exchange`,
`destroy_record`." Two corrections, both answered at ladder step 3: (1) **the closing half already exists
as ONE verb** — `release`, eligibility `own`, generic over `tenure_kinds \ {contain}` (`04 §A.3` row 14:
*four closing verbs missing → one `release` verb*), and `revoke` takes away. **Do not add `waive`,
`deposed` or `fray / loosen` rows**; if a closer is needed that `release`/`revoke` cannot express, say
which and stop. (2) `restore` executes (24e); `commit` and `oblige` have effects (7a, 17a). So `14`
builds: **`repudiate`** (the second voluntary ender of an ambition — R-06), **`succeed`**, **`tie / knot`**,
**`forge`**, **`exchange`**, **`carry`** — predicate (`requires_typed` in one of the closed forms;
`loop/predicates.py` only where no form fits) and effect each, effect targets: `loop/effects_governance.py`
(`succeed`, `tie / knot`), `loop/effects_information.py` (`repudiate`, `forge`, `exchange`), `carry` by
what it writes.
**Precondition inside the unit:** `decision/options.py` binds one referent to every operand slot, so no
computed act names two distinct parties. **The telling workplan's T4 builds the first half of the fix**
(`operand_bags`, `known_persons`, the contest target read off `row.counterparty`); `14` extends it to
`give`/`oblige`/`exchange` **on those primitives** — a distinct operand per slot where T4's bags do not
already supply one — and puts the counterparty check **in the fold**, not per effect. Never a second
binding mechanism. This is what makes `give` and `oblige` formable in computed play (today 0 formed in
the realm).
**Three decisions this position takes, each by the ladder, each recorded in its commit:**
- **`R05-THREAD` — `thread_read`'s operand (H-85).** Step 4: the row's own default — a two-valued
  `knowledge_kinds` roster, the H-128 swept-fixture shape (A-7). If the critic finds the default
  invents a taxonomy, decline and record `thread_read` as waiting on `27`/`29f`.
- **`destroy_record`'s formability (A-13).** `eligibility: hold:<record>` + presence is unformable for
  everyone; it needs a record-holding question referent — `give`'s shape (step 4).
- **H-165 limit 2 — a person-side works channel.** `found`/`build`/`work` refuse everywhere because no
  computed act declares a works (`create_record` is untyped, so it always mints `text`). Step 4
  candidate: the `15c` content-operand precedent. If it does not fit, leave the three verbs to J-4.
**Ride-along CANDIDATE-WHY:** `Candidate.why` is written once and read nowhere; give it a reader or
remove it — default remove (`04` licenses either, never a hole row).
**COMPLIANCE:** loader invariant 4 — every failable conjunct has a refusal kind (S-8: the clause-keyed
schema exists; use it). **OBSERVABLE:** state the prediction before the commit — landing a reversible pair
moves W-D divergence **up**. **FALSIFIER:** a `Tenure(X, X)` self-loop accepted, or an `oblige` whose
object is a bare string naming no entity (the F7/F8 recurrence that reverted this work once); every new
row that cannot bind its counterparty must DECLINE person-side (`give`/`petition` precedent) so the
always-refused set does not grow — assert the set; any effect branching on a proper noun or a rung-kind
member is scripting drift (`04` PART D 27a/28). **Control:** `report && delta HEAD` per verb — no probe
flips outside the verb. **Hash:** corpus pins move, recorded per verb, never batched. **R:** R-05 (up to
six rows + `give`/`oblige`/`destroy_record` formable), R-06 (`repudiate`), R-01 (counterparty edges).

### `17` · U8 — `ambitions(p)` and the cast seated · IN · gate `14` (E8) · `sonnet`/`opus` · `[design]`

**INSTRUCTION.** `queries/person_q.py::ambitions(p) -> list[PropositionId]` — a person-side READ over live
`commit` edges to OUGHT Propositions (the mechanism R-06 already names). `04`'s row for `queries/person_q`:
writes nothing; may read *"a `PersonInterior` snapshot only"*. Then the remainder `13` left to this
position (2026-09-28 plan §8.7): in `harness/corpus_run.py::build_at`, seat `p_b`/`p_c` from the `cast:`,
resolve the rest of `who_acts` into offices and `WAITS-ON-PLAYER`, `one_line` → the OUGHT Proposition,
`knowledge` → initial Claims. `one_line` is **parsed into a `cast:` block by an author, never
token-matched** (the W10 router lesson). **FALSIFIER:** `ambitions` taking a `World` reddens the
`sense`-is-the-only-World-taker AX-2 test; `NPC-020` (no overlay) builds byte-identically (control: with
`cast:` absent, `build_at` still seats three and the tallies are unchanged). **OBSERVABLE:**
`DISTINCT EXECUTED SETS` rises over the pre-cast arm; Q4 fires for more than one proposition; an 11-actor
case runs. **Hash:** corpus moves for every case gaining a cast (declared). **R:** R-06 reason 1, R-09.

### `13`-rest · W28-cast: the remaining overlays · IN · gate — (merges after `17`) · `sonnet` author, `opus` critic · `[design]`

41 NPC + 97 ARC `cast:` overlays in `engine/season/cases/exercises/*.yaml` (never `cases/chain/*.yaml` in
place). Schema: `who_acts`, `one_line`, `knowledge`; entries naming a player become `WAITS-ON-PLAYER`. NPC
lane first. **`capability` is authored only where both hold:** the case text names a vocation a key in
`rosters.yaml: verb_capability` covers, **and** a magnitude has a source. `capability`'s scale is
unruled (H-126/H-127 `assumption`); `NPC-088`'s `3` was a named judgment call, not canon. **Do not repeat
that judgment 138 times** — where no source exists, leave `pool_default` and record it; the scale is J-13.
**FALSIFIER:** a `one_line` token-matched from the case prose; a `capability` with no named source.
**Critic:** checks the `WAITS-ON-PLAYER` split and every authored number. **Hash:** corpus pins move
(declared). **R:** R-06, R-09 (only as far as sourced `capability` reaches).

### `13d-iii` · rung anchors for seats, the `[NEW]` seats, the remit overlay · IN · gate `17` (E8); remit half J-8 · `sonnet` build, `opus` critic · `[design]`

**The cap it lifts (H-163 limit 1):** 16 of `build_realm`'s 19 seats carry no rung, so a holder's purview
is empty and `levy`/`issue`/`open_case` refuse on `authority` (realm: `levy.unauthorized` 19 of 20).
**INSTRUCTION.** A rung-ANCHOR resolver in `harness/populated.py` over r2 `03`'s four anchor forms
(A-5: answered at ladder step 3); give every live seat its `scope_rung`; mint the `[NEW]` seats
`offices.yaml` marks; delete `rosters.yaml: titles` now that `offices.yaml` owns it (8a's follow-up).
The `remit` overlay for the 19 live seats waits on J-8 for `dispatch` only — land the rest.
**FALSIFIER:** in `aperture 4 0`, `levy.unauthorized` falls and `≥ 1` `levy` or `issue` executes with
`Act.via` set (U9's own acceptance text); every `[NEW]` seat's anchor resolves to a live rung; a computed
`transfer` carries `via` where a seat paid it (H-158 — read, and register if not). **Hash:** `build_realm`
census + hash move (declared); every `[GROUNDED: …]` realm figure in `hole_register.yaml` (H-156, H-163,
H-165) goes stale — the forward sweep re-cites them, never silently. **R:** R-04 (reason 1), R-05.

### `21`-rest · U10's bookkeeping tail · IN · gate `11` (re-take) · `haiku`/`sonnet` · `[editorial]`

Refresh, from one fresh run of each row's own `measure:`: R-01's opening R3 sentence (now 46/46 · 96/97
over 143), R-03's and R-09's `measured:` blocks (dated 2026-09-11), R-09's stale "capability empty on
every corpus person", R-04's `measure:` (to the instrument that reads its stated reasons — `aperture 4 0`'s
per-verb lines — since `corpus_run` prints nothing for it any more), R-02's `measure:` comment. **Item 3
(reconcile the progress board) is closed, ladder step 2** — the board was retired at `ebb43bf0`.
**FALSIFIER:** every edited `measured:` line is reproducible from its row's `measure:` command (the
register refuses an empty one, not a wrong one — the critic must). `register --requirements` exits 0.

### `27` · WR-SCOPE remainder · WR · gate — · `{parallel worktree}` · `opus`/`opus` · `[design]`

Landed (PR #442): `coherence.py` elastic/plastic (`ED-WR-0010`), `operations.py`'s P-25 scale term,
`tests/valoria/test_coherence_elastic_plastic.py`. **Remainder:** the `rendering.py` stubs
(`apply_rs_strain`, `check_calamity_threshold`); `ED-WR-0003` (the "overheard" conditional-observer rule
and the revelation procedures); the mending cost (`attempt_mending` calls `recover()` and costs > 0).
**⚠ One constraint the WR handoff does not state:** the stubs' named targets (substrate tension →
incursions → Accord; MS) are overview clocks that **have no season analogue by architecture**
(`loop/census.py`: *"NO CLOCK GENERATES ANYTHING"*; ED-WR-0011 option A) and that `29a` deleted (PR #450; `ms_track` stays until `29a`-ms). Wire a stub
only to a retained or season-native carrier (the season's `(Person, coherence)` row — RES, `social:
false`, written through a seam Event — is the one the architecture provides); a stub with no such target
is struck with its reason, never wired into `ms_track`. And `27` must leave
`threadwork/sim/{co_movement,opposing}.py` free of `ms_track` and `knots` imports, or `29a`-ms and `29f`
cannot proceed (E2). **FALSIFIER:** the mending test (`recover()` called, cost > 0); each wired stub
executes in a threadwork sim; `ED-WR-0003`'s rule has a test; `grep -n "ms_track\|sustain_knot"
systems/threadwork/sim/` returns nothing. **R:** none (unblocks `29a`-ms, `29f`).

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

- **`29f`:** `systems/fieldwork/sim/knots.py` (ED-912's ±5 gauge maps to `Tenure.degree`, F.4 —
  recorded on `14`, not invented); `engine/tests/test_knots_ed912.py` → `FORK:`.
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
