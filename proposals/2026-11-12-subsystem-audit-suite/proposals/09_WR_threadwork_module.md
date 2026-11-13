# WR · Threadwork as a registered module, one code path, playable alone

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-17) — edit 2 is read as amended by the census: `threadcut.py` and `co_movement.py` are deleted whole before the move (`17_CENSUS_C1B_01_deletions.md` D3; exact replacement sentence in `17_CENSUS_C1B_03_corrections.md` C-6); `collective.py` and `opposing.py` move as inputs to `work` through `WorkingInput.helpers` and `WorkingInput.opposed_by` and get no composition row of their own (`17_CENSUS_C1B_02_wires.md` W-3, reading 1); an outcome field the host adapter does not read at landing is cut in that commit, not carried (`17_CENSUS_REST_2_wiring.md`, carried-wires table). Nothing else in this proposal changes; WR's own closure (U5d) owns the rest of it.

Reconciled: 2026-11-12, U5d closure — folded **A-40**, **A-43**, **A-28** and **A-5**. Edits 1, 2 and 4 are superseded by `09_WR_B_threadwork_session_and_practitioner.md`; edit 3 (the tables as one typed file under `engine/engine_params/`) stands. The working's subject is a Site of a territory (A-40). `knot` is the Thread lane's verb after the `tie` / `knot` split (A-28), so this module's verb list gains it and the requirement instrument's count moves. Every thread roll is the one sampler's (A-5). What zero Coherence does is `U5d_WR_zero_coherence_unknowable.md` (A-43): continuity kept, the person unreadable to others.

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §2 / §1 and C3 §9 (the superseded text of edits 1, 2 and 4 is deleted, not left beside its replacement). Corrected at the documents: R3 asked to delete edits 1, 2 and 4 whole, but the successor keeps two parts of them by name ("the first lane's `Practitioner` stands unchanged"; "the first lane's move stands"), so those two parts are kept and only what the successor replaces is deleted (`WorkingInput`/`WorkingOutcome`, the single composition row, the scenario case); edit 2's sentence on `threadcut.py`, `co_movement.py`, `collective.py` and `opposing.py` now follows the U5a head. Edit 3 gains `knot` (A-28, the head). The gate and the falsifier are narrowed to what this file still lands; tier and batch added (R3 7b-0; U3 B03).
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_2_DONE.md` row 60, "for another lane"; A-28): the Thread lane receives `08_FI_08_knots-season-form.md` §1 (a person witnesses through a knot he owns: `epistemic._ch_witness_key`'s `(pid, anchor) in knots` line, index pair owner first, `queries/cache.py:95`) and §4 (a knot's strain is a reading over the owner's own ledger, `person_q.knot_strain`; a rupture is the owner's own `release` of his edge). That file keeps both as their evidence and lands neither; this file's edits 1-4 do not land them either. They land with the Thread lane's batch (B35, `09_WR_B_threadwork_session_and_practitioner.md`), and the kinds and the threshold of §4 stay a design pass. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "typed record" → "dataclass" (glossary *record*); "Ob" → "obstacle" in prose (glossary *obstacle*).

## Status: PROPOSED

Lands in batch: B03 (hygiene, hash EQUAL) for edit 3, last in U3 §1 item 4; the kept move of edit 2 lands with `09_WR_B_threadwork_session_and_practitioner.md` (B35).
Depends on: `17_CENSUS_C1B_01_deletions.md` D3 (B03) for the move; nothing proposed for edit 3.

Carries finding F-WR-05 of `audits/09_WR_audit.md`, its §9 (playable standalone and integrated), its §14
(capability authoring surface, the threadwork rows) and §6 resolutions R-08 and R-09. Evidence ids (E-nn)
are that file's §12.

## What it changes in `engine/season/` at runtime

**Nothing by itself.** It moves the working's arithmetic to where the season loop is allowed to reach it
and gives it the shape a composition row can name. The loop first calls it when B10-15's CP-T07-02 builds
its host (`seam/wrappers/threadwork.py`); this proposal is the precondition that makes that host
conformant, and is hash EQUAL.

## The problem

`modules/` has no threadwork module, and that is a gap, not a deferral.

1. **Layer 1.** `engine/` names no subsystem by import; a seam resolves a role through
   `engine/substrate/composition.py` to a module registered in `references/module_contracts.yaml`
   (`04` §A.2: "the contest provider ADAPTERS … each builds a typed input from a projection, calls the
   module entry its composition row names"). The one `sys.path` seam is combat's and is shrink-only. So
   CP-T07-02's host cannot import `systems/threadwork/sim/` and conform.
2. **The registered-module contract** (typed input, typed outcome, no token, no game state). The oracle
   keeps state at module level (`systems/threadwork/sim/coherence.py:142`, `_practitioner_state`; the same
   in `threadcut.py:63` and `co_movement.py:76`), takes a duck-typed `actor` (`.spirit`, `.focus`, `.ts`,
   `operations.py:14-18`) and an optional `world` it writes into (`charge_working`, `:277-288`).
3. **One code path.** The plan builds a season host over the oracle; the oracle's own callers are tests
   and one exporter (grep, E-14). A standalone threadwork scene would be a third caller with its own actor
   object. Three callers, three actor shapes, one of them the game.
4. **Precedent.** Settlements had this shape and was moved: IN-07 E1 to E6 made `modules/settlements/` six
   pure entries (`larder_draw`, `subsist`, `produce`, `housing`, `fabric`, `fortification`), each reading a
   dataclass from `queries/inputs.py`, with the host projection in `world_q.py` and every write left in
   the loop. Fieldwork followed (`fieldwork.find`). Ladder step 4: the tree has decided this shape twice.

## The resolution, decided

`systems/threadwork/sim/` becomes `modules/threadwork/`: pure entries over dataclasses, the practitioner's
Coherence passed in and returned, never stored; one composition role per entry; the host (season) and the
standalone harness both build the same input record and both interpret the same outcome record.

## The edits

### Edit 1 · the dataclasses (`engine/season/queries/inputs.py`, beside `SubsistInput`)

```python
class Practitioner(NamedTuple):       # one person, as a working reads him: no id lookup, no duck typing
    pid: str
    spirit: int                       # `attr.mind.will` (named Spirit, CR-84), read by the host
    focus: int
    thread_sensitivity: Optional[int] # `Person.thread_sensitivity` (K-3); None cannot Leap
    resting_point: int                # `Person.coherence`'s two numbers, CP-T07-02's carrier
    displacement: int
    resilience: int                   # R-14's term; 0 until its slot is ruled

```

`WorkingInput` and `WorkingOutcome` are **not** defined here: they are `09_WR_B_threadwork_session_and_practitioner.md`
edit 1's (the session's two integers, the typed refusal, `draws: tuple`). The `Practitioner` above stands
as that file uses it.

### Edit 2 · the entries (`modules/threadwork/`, moved from `systems/threadwork/sim/`)

The move (kept: `09_WR_B_threadwork_session_and_practitioner.md` edit 2 says "the first lane's move
stands"): `modules/threadwork/working.py::work(inp: WorkingInput) -> WorkingOutcome` is
`_resolve_operation` with its three side effects removed: no `apply_coherence_delta` (the delta is
returned), no `world` argument, no module store. `coherence.py` keeps its pure arithmetic
(`_displacement_band`, the elastic and plastic steps) as functions over `(resting_point, displacement)`;
`_practitioner_state`, `_store` and `reset_all` are deleted; `threadcut.py` and `co_movement.py` are
deleted whole before the move (the U5a head: `17_CENSUS_C1B_01_deletions.md` D3); `collective.py` and
`opposing.py` move as inputs to `work` through `WorkingInput.helpers` and `WorkingInput.opposed_by` (the
U5a head, `17_CENSUS_C1B_02_wires.md` W-3). `rendering.py` (already struck, "No entry point") is deleted
with a `FORK:` row.

(Wave 3: the single composition row this edit declared, `threadwork.work` with no declaration of where it
is checked, is deleted here, superseded by `09_WR_B_threadwork_session_and_practitioner.md` edit 2's three
entries, each declared where its kind is checked.)

The `threadwork` contract's `sim_module:` re-points to `modules/threadwork/working.py`;
`registry_system: "threadwork"   # Key Type Registry vocabulary` is deleted (the Key substrate is retired,
ED-IN-0232). `rosters.yaml: modules.threadwork.home` becomes `modules/threadwork/`.

The three test files that drive the oracle (`tests/valoria/test_threadwork_resilience.py`,
`test_threadwork_mending_parity.py`, `test_coherence_elastic_plastic.py`) and
`engine/tests/test_thread_mending_ed871.py` build a `WorkingInput` instead of a duck-typed actor; their
expected numbers are unchanged, which is the parity gate.

### Edit 3 · the constants become data the module reads (see audit §14)

`operations.py:73-168` holds the obstacle tables (`DEPTH_OB`, `BREADTH_OB`, `DISTANCE_OB`, `MENDING_OB`), the
thread-sensitivity gates (`DEPTH_TS_MINIMUM`, `LEAP_OB_TS_LOW/HIGH`), the cost table
(`COHERENCE_COST_BY_SCALE`) and three magnitudes tagged invented. They move to one typed file under
`engine/engine_params/` behind the existing exporter's `--check` (`tools/export_engine_params.py`), the
shape combat's parameters already have, and the module reads the loaded form. The operation roster
(`leap, weave, pull, past_pull, lock, dissolve, mend`, and `knot` once the `tie`/`knot` split lands, A-28)
becomes `rosters.yaml: thread_operations`, read by
the verb table's thread rows (CP-T07-03, -04, -11) and by the loader, so a row naming an operation the
module does not have is refused at import.

### Edit 4 · deleted (wave 3)

Superseded whole by `09_WR_B_threadwork_session_and_practitioner.md` edit 4 (the Warden's season), which
replaces this case and its end conditions; nothing of it is kept here.

## The gate that shows it worked

```sh
python -m pytest tests/valoria/test_threadwork_resilience.py tests/valoria/test_threadwork_mending_parity.py \
       tests/valoria/test_coherence_elastic_plastic.py engine/tests/test_thread_mending_ed871.py -q
python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q      # the subprocess import artifact
python tools/export_engine_params.py --check
PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0                 # realm hashes unchanged
```

Passes when (edit 3, B03) the round-trip is clean, the loader refuses a thread row naming an operation the
roster lacks, the four oracle files are green on the same expected numbers reading the loaded tables, and
`build_realm(0)` and the one-season pin are EQUAL; and (the kept move, B35, under the successor's gate)
the import artifact shows no `systems/threadwork` path under any engine module.

## The falsifier

Edit 3: a table value read from `operations.py` after the move to `engine/engine_params/` (a second copy
survived), or a thread row naming an unrostered operation that loads. The move: two calls of `work` with
equal input returning different outcomes (held state survived the move); the successor's falsifier covers
the session.

## NERS reading

- **N.** Without it, CP-T07-02 either breaks Layer 1 or grows a second path. Holds vertically (season host
  to module), laterally (the settlements and fieldwork precedent) and from the standalone direction.
- **R.** Customisation of characters is where threadwork earns its place: a practitioner's Spirit, Focus,
  sensitivity and accumulated set decide what he can attempt and what it costs him. The records make those
  four inputs explicit and attributable.
- **S.** "Calculations consistent in methodology": the working's degree comes from the shared ladder, its
  draw from the shared mint, its parameters from the shared exporter. Pause: a working is one fold inside
  RESOLVE; a playable working would suspend where a playable fight does (ENCOUNTER's `host`), which is
  CP-T07-11's `ward` routing "a working into a contest" and not built here.
- **E, last.** A move and a signature change, no new mechanism; it deletes three module stores. High.

## Cost class

Edit plus exporter row (edit 3); the kept move is the successor's small build. Tier: `sonnet` (R3 7b-0).
