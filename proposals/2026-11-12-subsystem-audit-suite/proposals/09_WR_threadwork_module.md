# WR · Threadwork as a registered module, one code path, playable alone

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-17) — edit 2 is read as amended by the census: `threadcut.py` and `co_movement.py` are deleted whole before the move (`17_CENSUS_C1B_01_deletions.md` D3; exact replacement sentence in `17_CENSUS_C1B_03_corrections.md` C-6); `collective.py` and `opposing.py` move as inputs to `work` through `WorkingInput.helpers` and `WorkingInput.opposed_by` and get no composition row of their own (`17_CENSUS_C1B_02_wires.md` W-3, reading 1); an outcome field the host adapter does not read at landing is cut in that commit, not carried (`17_CENSUS_REST_2_wiring.md`, carried-wires table). Nothing else in this proposal changes; WR's own closure (U5d) owns the rest of it.

## Status: PROPOSED

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
   typed record from `queries/inputs.py`, with the host projection in `world_q.py` and every write left in
   the loop. Fieldwork followed (`fieldwork.find`). Ladder step 4: the tree has decided this shape twice.

## The resolution, decided

`systems/threadwork/sim/` becomes `modules/threadwork/`: pure entries over typed records, the practitioner's
Coherence passed in and returned, never stored; one composition role per entry; the host (season) and the
standalone harness both build the same input record and both interpret the same outcome record.

## The edits

### Edit 1 · the typed records (`engine/season/queries/inputs.py`, beside `SubsistInput`)

```python
class Practitioner(NamedTuple):       # one person, as a working reads him: no id lookup, no duck typing
    pid: str
    spirit: int                       # `attr.mind.will` (named Spirit, CR-84), read by the host
    focus: int
    thread_sensitivity: Optional[int] # `Person.thread_sensitivity` (K-3); None cannot Leap
    resting_point: int                # `Person.coherence`'s two numbers, CP-T07-02's carrier
    displacement: int
    resilience: int                   # R-14's term; 0 until its slot is ruled

class WorkingInput(NamedTuple):
    operation: str                    # a `rosters.yaml: thread_operations` member (edit 3)
    actor: Practitioner
    depth: str; breadth: str; distance: str      # the Three-Axis Ob's keys
    target_kind: str                  # "site" | "person" | "self"
    in_equilibrium: bool              # CP-T07-05's read, projected by the host
    draw: object                      # the keyed draw the host mints (`ids.draw_factory`), never an rng of the module's

class WorkingOutcome(NamedTuple):
    degree: str                       # the shared degree ladder's band
    coherence_delta: int              # what the actor's displacement moves by (0 for a Mending, ED-871)
    resting_point_delta: int          # own-configuration Mending only
    strain: int                       # what the target's fabric loses; 0 until H-236's source is ruled
    observed: tuple                   # what a witness would read (CP-T07-08's breach)
```

### Edit 2 · the entries (`modules/threadwork/`, moved from `systems/threadwork/sim/`)

`modules/threadwork/working.py::work(inp: WorkingInput) -> WorkingOutcome` is `_resolve_operation` with its
three side effects removed: no `apply_coherence_delta` (the delta is returned), no `world` argument, no
module store. `coherence.py` keeps its pure arithmetic (`_displacement_band`, the elastic and plastic
steps) as functions over `(resting_point, displacement)`; `_practitioner_state`, `_store`, `reset_all` and
their siblings in `threadcut.py` and `co_movement.py` are deleted. `collective.py` and `opposing.py` take
`tuple[Practitioner, ...]`. `rendering.py` (already struck, "No entry point") is deleted with a `FORK:` row.

`references/module_contracts.yaml`, `composition_roles:` gains

```yaml
  threadwork.work:
    module: threadwork
    entry: step_call          # `fieldwork.find`'s kind: the host calls it inside RESOLVE's fold
    input: WorkingInput
    output: WorkingOutcome
```

and the `threadwork` contract's `sim_module:` re-points to `modules/threadwork/working.py`;
`registry_system: "threadwork"   # Key Type Registry vocabulary` is deleted (the Key substrate is retired,
ED-IN-0232). `rosters.yaml: modules.threadwork.home` becomes `modules/threadwork/`.

The three test files that drive the oracle (`tests/valoria/test_threadwork_resilience.py`,
`test_threadwork_mending_parity.py`, `test_coherence_elastic_plastic.py`) and
`engine/tests/test_thread_mending_ed871.py` build a `WorkingInput` instead of a duck-typed actor; their
expected numbers are unchanged, which is the parity gate.

### Edit 3 · the constants become data the module reads (see audit §14)

`operations.py:73-168` holds the Ob tables (`DEPTH_OB`, `BREADTH_OB`, `DISTANCE_OB`, `MENDING_OB`), the
thread-sensitivity gates (`DEPTH_TS_MINIMUM`, `LEAP_OB_TS_LOW/HIGH`), the cost table
(`COHERENCE_COST_BY_SCALE`) and three magnitudes tagged invented. They move to one typed file under
`engine/engine_params/` behind the existing exporter's `--check` (`tools/export_engine_params.py`), the
shape combat's parameters already have, and the module reads the loaded form. The operation roster
(`leap, weave, pull, past_pull, lock, dissolve, mend`) becomes `rosters.yaml: thread_operations`, read by
the verb table's thread rows (CP-T07-03, -04, -11) and by the loader, so a row naming an operation the
module does not have is refused at import.

### Edit 4 · the standalone scenario (`engine/season/harness/exercises.py`'s overlay, one case)

No new harness. A threadwork exercise is a hand-built world of three rungs (a settlement, a hearth, one
Site below its floor), two persons (a practitioner with `thread_sensitivity` at the gate and a witness),
run through `SeasonDriver.season` with `play_surface.dispatching_chooser` binding the practitioner to a
callback. The choice surface is the thread rows B10-15 lands (`weave`, `lock`, `mend`, `ward`,
`thread_read`); the stakes are the Site's condition against its floor and the practitioner's Coherence
band; the end condition is the Site above its floor, or the practitioner past his human band (CP-T07-07's
permanent set). Outcome legibility is the witness's ledger: what he holds after each working. Until
B10-15 lands the rows, this scenario cannot be played, and the proposal says so rather than supplying a
second chooser.

## The gate that shows it worked

```sh
python -m pytest tests/valoria/test_threadwork_resilience.py tests/valoria/test_threadwork_mending_parity.py \
       tests/valoria/test_coherence_elastic_plastic.py engine/tests/test_thread_mending_ed871.py -q
python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q      # the subprocess import artifact
python tools/export_engine_params.py --check
PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0                 # realm hashes unchanged
```

Passes when the four oracle files are green on the same expected numbers, the import artifact shows no
`systems/threadwork` path under any engine module, the round-trip is clean, and `build_realm(0)` and the
one-season pin are EQUAL.

## The falsifier

Two calls of `work` with equal `WorkingInput` returning different outcomes (held state survived the move);
a `WorkingInput` whose `Practitioner` differs from another only in `resting_point` returning the same
`coherence_delta` band crossing (the state is not being read from the input).

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

Small build (edits 1, 2), edit plus exporter row (edit 3), design-first on B10-15's rows before edit 4
can be played.
