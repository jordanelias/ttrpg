# Coverage Matrix — Weapon System v2 (Active)

Settled entries (dated 2026-07-25 and earlier) are in `tests/coverage_matrix_archive.md`,
which was restored 2026-08-23 after the evacuation deleted it — see that file for why this
one had drifted to 94% of a blocking cap with no working relief valve.

## 2026-07-29 — ED-MB-0055/0056/0057: 51x51 field, cell co-location measured, dead-primitive census

**Field 50 -> 51 (Jordan directive).** Odd, so a mirror matchup has a true centre column instead of
a half-cell bias, and the row budget divides exactly: 5 behind B + 13 (B) + 15 approach + 13 (A) +
5 behind A = 51. **All five goldens BYTE-EXACT** — the battery never approaches the boundary, so the
edge-cornering clamp never fires and the change is inert on every scored row. Two tests hardcoded
the old size (centring against 25 = 50/2, off-board bound 49 = 50−1) and now derive both from
`BATTLEFIELD_SIZE`; the hardcodes were a second owner for a fact `config.py` already holds.

**Measured correction to the spawn geometry:** a formation extends DOWNWARD in row index from
`starting_position` for BOTH sides, so the shipped rows (A=34, B=15) look 19 apart but B's own depth
eats 14 — the true **front-face gap was 5**, which is why bodies were in contact within a couple of
ticks and no approach phase was ever visible.

**Cell co-location (ED-MB-0056), 140 snapshots / 79,226 placements:** 9,970 same-subunit · **3,705
different-subunit** · 39 opposing-side · **17.31% overlap rate**. Root cause of the formation
shearing in the renders, and it makes the contact surface ill-defined — if cells may overlap, the
boundary between them is not a boundary.

**Dead-primitive census (ED-MB-0057):** new `tools/dead_primitive_census.py` works BELOW module
granularity, where the existing instruments cannot see. **118 dead primitives repo-wide** (73
functions + 45 constants of 2,164). The tool's first draft produced **96 false positives** (it
subtracted the definition file, killing every `self._foo()` call) and was repaired before any number
was quoted. MB relevancy analysed in
`audit/2026-07-29-scenario-visualization/00_findings.md` §5.1 — `resolve_internal_collisions`
(highest: built for exactly the co-location defect, never invoked since 2026-05-29) and
`_reach_throttle` (high: would make per-type reach matter in the approach) are the two that matter,
and both are spatial-integrity mechanics switched off for the same stated reason.
## 2026-07-29 — ED-MB-0054 plan-v2 B1c: rekey_cells — SIX stale maps per drift, not the three the audit named

`check_drift` re-keyed `cell_troops` (+ node position state) and nothing else. **Measured over the
`cell` battery: 10 drift events, six maps left holding dead ids in ALL TEN** — `cell_offsets`,
`cell_offsets_c`, `halted_cells`, `cell_last_speed`, `cell_facing_vec`, `_cell_target`. Three more
than the audit listed, and the missed pair is the worse one: `cell_offsets` is **accumulated
displacement**, so `.get(pid, 0)` snaps a drifted body back to its **spawn row** mid-advance.

`Subunit.rekey_cells` is the grid-path analogue of `_rekey_node_state`, mirroring that method's
already-ratified policy rather than inventing one. Displacement → mean offset (centroid preserved);
facing → mean committed facing, **not** the `advance_dir` default; `_cell_target` → redistributed
like `cell_troops`; transient state (halt/merge/speed) → cleared. `cell_morale`,
`cell_start_troops`, `cell_breakpoint` **deliberately untouched** — §6-class rulings, not
derivations, and empty at the shipped flag setting.

**Golden delta, decomposed BEFORE recording: only `cell_field` moved** (`13bd02dd…` → `2a9214eb…`).
Arms: facing-only → the new digest; everything-except-facing → the OLD digest. **Facing preservation
is the sole mover.** On the grid path the corrections fire 10/10 (mean offset 8.96 vs the 0
fall-through, facing (−0.998, 0.067) vs the (−1, 0) default) but never reach a `trial_vector` field.
## 2026-07-29 — ED-MB-0053 plan-v2 §4a: the fifth digest mode, and the mode-key extension that had to precede it

**The verification net had a hole over exactly the state B1a is about to refactor.** All four
digests run at `PC_CELL_MORALE=0`, where `cell_morale` / `cell_start_troops` / `cell_breakpoint` are
EMPTY — so they pin float-order over every per-cell map *except* the three whose desync motivates
the ownership work, and "if a digest moves, you changed behaviour" was vacuous over cell state.
§4a makes a fifth golden a hard gate on starting B1a; this closes it.

**The key extension was mandatory, not tidy-up.** `bat.py`'s mode key read only `PER_CELL` and
`FIELD_MOVEMENT`, so a run at `PC_CELL_MORALE=1` returned `'cell'` and checked itself against the
flag-OFF golden — a different configuration. That is precisely the ED-1089 shape the
`FIELD_MOVEMENT` clause was added to close, one flag later; recording a fifth mode without
extending the key would have rebuilt the same trap. Extracted as `bat._mode_key(per_cell,
field_movement, cell_morale)` so it can be tested in microseconds instead of by running a battery.

**[ED-MB-0062, 2026-08-01] MODE KEYS ARE NOW ABSOLUTE — Jordan's rename-by-distinction ruling.**
The scheme above was still *relative*: a suffix appeared only when a flag was ON, so absence encoded
"OFF" **relative to the default at recording time**. `cell` never meant "cell-morale off", it meant
"cell-morale not mentioned" — so flipping `PC_CELL_MORALE`'s default (which ED-MB-0001's flags-ON
directive requires) re-points the plain grid run onto the fifth mode's golden and orphans four
recorded keys. Note the key was **already injective**, so the injectivity pin could not see this.
Keys now name every axis with its value: `unit`→`unit_grid_mor0`, `cell`→`cell_grid_mor0`,
`unit_field`→`unit_field_mor0`, `cell_field`→`cell_field_mor0`, `cell_cm`→`cell_grid_mor1`
(the `grid` token was renamed `legacy` on 2026-08-14 — see that dated section below)
(`cell` reserved for the mass-battle GEOMETRY primitive; `mor` for the distinct morale flag).
**No digest changed** — lookup keys only, values carried byte-for-byte, so this is not a re-record
and G11 does not apply. Control: `cell_field_mor0` still matches its golden under the new key, which
a mis-mapped migration would have broken. The three ON configurations (`unit_grid_mor1`,
`unit_field_mor1`, `cell_field_mor1`) now report MISSING honestly — **this is what makes the
all-flags-ON re-base recordable**, and it is the ED-MB-0061 §5 blocker cleared.

`cell_cm` = **`b42343dbd508d1e9…`**. **CONTROL (§0.1 #4):** it DIFFERS from the `cell` golden
(`f58a9cb4…`), so the mode genuinely exercises seeded cell morale rather than silently reproducing
the flag-off battery — had they matched, the fifth golden would have been ceremony. Deterministic
2/2. Recorded on Linux/Python 3.11.15.

**Placement, corrected mid-task.** The first draft put the fifth mode's `--check` in
`tests/valoria`. That is three more full batteries (~7 min locally, more hosted) inside a job
already measured at ~9–11m43s against a **16-minute cap** — buying a mysterious mid-run
cancellation, not coverage. Moved to the dedicated golden job, and
`tools/ci_field_golden_check.py` → **`tools/ci_golden_modes_check.py`**: it was already the single
owner of "run `bat.py --check` in a pinned configuration outside the unit-test budget", and the
fifth mode is a GRID mode, so the field-only name would have misfiled it or spawned a second owner.
Every reference repointed (workflow, `ci_checks_registry.yaml`, the pin-drift test). All three modes
green.

Guards: `test_mode_key_discriminates_every_digest_toggle` asserts the key is **injective over the
eight-configuration toggle cube** (a one-example check would pass with any two toggles conflated)
and that every recorded `EXPECTED` key is one `_mode_key` can actually emit — mutation-verified by
deleting the `_cm` clause. `test_mode_selectors_cover_every_out_of_budget_golden_mode` extended to
an exact-set assertion over the three modes, each selector cross-checked against what its name
claims, plus: `cell_cm` is the ONLY mode permitted to override the `PC_CELL_MORALE` pin.
## 2026-07-29 — ED-MB-0052 plan-v2 §5 C1: per-phase casualty attribution, with conservation as the gate

Every hp loss is now tagged with SOURCE and TICK through the existing `start_trace`/`trace_event`
seam. Four sites, the complete set (grepped `\.hp =` across engine + hierarchy + percell): the
per-turn melee and volley application in `run_battle`, `pursuit_damage`, and
`freed_attacker_damage`. The fifth `.hp =` is `hp = hp_max` at construction, not damage.

**Conservation is the gate, and it holds EXACTLY** — 20 seeds × 2 sides, `Σ attributed == before −
after` with zero drift, asserted as equality rather than `approx` (an exactness claim tested with a
tolerance is not a weak test, it is an absent one). Two subtleties are encoded rather than assumed:
loss is attributed from the **clamped** movement, not nominal damage (they differ on the killing
blow, so a nominal-damage conservation claim fails on every annihilation); and the melee/volley
split is proportional to nominal share of that clamped total, so the parts sum to the whole.

**Instrumenting never restructures the instrumented.** Attribution brackets each existing assignment
(before/after); the arithmetic and ordering are byte-identical. A single apply-and-tag owner would be
tidier and would also change float ordering — the exact class of "harmless" change this lane keeps
being burned by.

**⚠ THE MERGE GUARD'S FIRST MUTATION WAS VACUOUS, AND RUNNING IT IS WHAT SHOWED THAT.** Planting
`random.random()` *inside* `attribute_hp_loss` moved NO digest — because with tracing off the
function is never called at all on the `bat.py` path (the main site is gated by `tracing_on()`, and
pursuit/freed-attacker fire only in `run_multi_unit_battle`, which the battery does not use). So the
mutation proved nothing, and had it been reported as "mutation-verified" it would have been false.
Re-planted at the seam's own call site, unconditional and hot: digest moved
`241f04e5… → bb5acf02…`. **Both results together are the guard** — one shows the instrumentation is
structurally unreachable when off, the other shows the digest is genuinely sensitive at that point,
so byte-exactness there is evidence and not vacuity.

All four goldens byte-exact with tracing off. Guards:
`tests/valoria/test_casualty_attribution.py` (5) — conservation across 20 seeds with an
`assert checked >= 20` non-vacuity counter; source/tick well-formedness; a ranged matchup asserting
`volley` rows actually appear (non-vacuity for the SPLIT, not just the total — a conservation test
alone passes happily if every loss is filed under one label); inertness with tracing off; and an
in-suite mutation that untags the melee path and asserts conservation then FAILS.
## 2026-07-29 — ED-MB-0051 plan-v2 A2: degree-boundary epsilon — the prediction FAILED, and the prediction was the thing that was wrong

**A2 predicted "this moves no digest in any of the four modes" and made digest movement a STOP
CONDITION. Two digests moved. Investigated, not re-recorded on sight.**

Decomposition (each arm run alone): the **degree-epsilon arm alone reproduces the new digest
exactly**; the **sigma-zero-snap arm alone reproduces the OLD digest exactly** — the chokepoint snap
is behaviour-neutral, the boundary guard is the sole mover.

Flip census, whole battery, guarded-vs-unguarded verdict compared per `compute_degree` call:

| mode | calls | flips | transitions | flip distance |
|---|---|---|---|---|
| `unit` | 17,312 | **0** (0.000%) | — | — |
| `cell` | 31,958 | **38** (0.119%) | all `Partial → Success` | 2.22e-16 … 8.88e-16 |
| `unit_field` | 18,152 | **0** (0.000%) | — | — |
| `cell_field` | 20,412 | **14** (0.069%) | all `Partial → Success` | 2.22e-16 … 4.44e-16 |

Every flip is `net` **1–4 ulp** below a *continuous* `ob` that it equals mathematically — five to six
orders TIGHTER than the 1e-9 epsilon, so the epsilon's width is not load-bearing (any value in
[8.9e-16, 1e-9] gives the same result). One direction only: the guard never demotes.

**Why the prediction failed, and it is a G1 failure inside the correction to G1.** The audit's
"0 flips in 209,778 calls", and the orchestrator's own N=3,120 replication of it, were **both taken
at `PER_CELL=0`** — the one configuration where the incidence really is zero. **S1.2 is NOT
incidence-zero:** in the shipped per-cell modes the 1-ulp defect erases an entire exchange in ~0.1%
of degree calls. A2 is therefore **a live correctness fix, not hygiene**, and the two `PER_CELL=1`
goldens were re-recorded deliberately, with this delta published (rule 4) in the single MB
golden-moving slot.

Controls: both moved modes reproduced their new digest on **two consecutive runs** (2/2); `cell`
reproduced it again with `PYTHONHASHSEED` unset (hash-order independent); both `PER_CELL=0` modes
byte-exact throughout. **Reconciliation** (plan A2's explicit requirement): `units.py`'s exact
uniform-aggregate fix is an EXACTNESS regime and stays authoritative where the answer is derivable;
`compute_degree`'s epsilon is a TOLERANCE for the non-uniform branch, which has no exact answer —
and it is measurably not redundant with it (the 52 flips above occur *with* that fix in place).
Stated in-file at both sites.

Guards: `tests/valoria/test_degree_boundary_epsilon.py` (13), **5/5 mutants killed** — revert the
guard; guard only `Success`; drop the Overwhelming second conjunct; remove the sigma snap; widen the
epsilon 1000×. Every boundary case uses `math.nextafter`, because plan v1's proposed
`compute_degree(ob - 1e-16, ob)` **passes on unfixed code** (`3 - 1e-16 == 3` in float64) — that
vacuity is itself pinned by a test so nobody re-derives it.

⚠ **Process finding:** the first A2 mutation run was CORRUPTED by stale `__pycache__`. CPython
invalidates by `(mtime, size)`, so a same-size edit inside one mtime second is served from cache —
it silently mis-scored 2 of 5 mutants. Both the A2 and I4 matrices were re-run under `python -B`
with caches cleared; the numbers above are from the clean run.
## 2026-07-29 — ED-MB-0050 plan-v2 A6a/A6b: the attrition-law instrument repaired, wired report-only

**The harness did not measure what it claimed, for three independent reasons — one of them not in
the plan.** (1) The `NO_ROUT_MORALE=1e9` pin is a MORALE pin, but `core.state._stochastic_break`
keys on the CASUALTY FRACTION and never reads morale (`return loss_frac >= bp`). That mechanism
landed 2026-07-23 and defaulted ON 2026-07-25 — one day before the audits. (2) The volley scenario
never fired: `stance='hold'` early-returns from all steering, spawn separation is 19 rows and
`VOLLEY_MAX_RANGE` is 8 — measured **0 melee engagements AND 0.00 volley loss** over 10 battles, so
`check_square`'s `inf` was a 0/0 guard. (3) **NEW, found here:** `TRAJ_FLOOR=0.25` stopped the
trajectory at hp≤25, but `Unit.recalc_size` routs outright at `size==0`, i.e. hp<`BLOCK_SIZE`=100 —
the floor was **unreachable** and every trajectory ended in annihilation-rout (measured: side B
routed at ticks 36/35/36 with hp 97.3/97.1/98.9, agg_morale 1e9, troop_total 400 vs a floor of 80).

**Repairs.** `_rout_disabled()` turns `PC_STOCHASTIC_ROUT` off for the trajectory window only (the
other three checks are statements about shipped behaviour and keep rout on — `check_no_annihilation`
is literally "the battle ends by rout"). Volley scenario → `balanced` + the existing `kite`
band-seeking primitive, reused verbatim per plan D4 (change the SCENARIO, not `hold` semantics).
Scenario choice MEASURED, not assumed: hold = 0 engagements/0 loss; balanced = 69 melee engagements
(contaminated); balanced+kite = **0 melee engagements**, volley loss 49.97/243.53 — pure volley.
Floor re-derived from `BLOCK_SIZE`. Clean-stop vs rout ordering fixed so a floor termination is not
mis-scored as a precondition violation.

**Result — the first defensible exponents this repo has.** Preconditions clean (0/40 routed, both
arms). `_best_exponent` now returns identifiability, and the verdict REFUSES a fit whose argmin sits
on a grid endpoint: `melee p=3.20 cv=0.00245 [identifiable]`, `volley p=2.00 cv=0.00327
[identifiable]`. The old `p=2.50` was literally `FIT_P_HI=2.51` — the melee cv objective is monotone
to that ceiling (0.2075→0.0318), exactly as A6a said; widening the grid to 6.01 reveals the real
interior minimum at 3.20. **Volley confirms the square law exactly. Melee is p≈3.2 against a ≤1.4
linear bar — super-square, an ENGINE finding, and an independent re-derivation of ED-MB-0007's
p≈3.2 on clean untruncated data.** `check_square` now measures a real ratio (19.4, cas 1.84/35.77)
and reports a no-exchange result as a FAILED PRECONDITION rather than as `inf`.

**Citation critic:** the entire conserved-quantity block carried `[canonical: mb_lanchester_design.md
§4 …]`. §4 is a five-item prose validation plan — no trajectory protocol, no tick budget, no morale
pin, no fit grid, no exponent bars; "1.4" and "1.6" do not appear in it. Re-labelled `[JUSTIFIED:]`.

**A6b:** CI job `lanchester-signature`, REPORT-ONLY (`|| true`) and registered in
`ci_checks_registry.yaml`. Report-only because the repaired instrument legitimately fails and the
failure awaits fork #2 (two incompatible 2:1 targets) — making it blocking now would either wedge
`main` or force the bar to be tuned to whatever the engine does, which is how a validation target
becomes a rubber stamp. Grid golden `unit` byte-exact; no engine `.py` touched.
## 2026-07-29 — ED-MB-0049 plan-v2 A5a: lanchester scalar-write sweep + two guard defects found by mutation

`lanchester_signature.py`'s no-rout pin was a BARE `ua.morale = ua.morale_start = NO_ROUT_MORALE` —
the silent-no-op class that confounded the retracted `PC_CELL_MORALE` flip. Routed onto
`Unit.set_morale` (unseeded it reduces exactly to `unit.morale = value`, so byte-identical at the
shipped default); `morale_start` stays bare and non-cellular. File added to the sweep guard's
`_ENGINE_FILES`. `test_persubunit_stress.py` deliberately NOT chained in front (A5b, G10).

**Two defects in the guard itself, both found by mutation, neither by reading.**
(1) The sweep regex is line-anchored and could not see a bare write inside a COMPOUND statement
(`ua = _mk(...); ua.morale = ...`) — precisely the shape being swept. Adding the file to the scanned
set without this repair would have produced a guard that passes because it cannot look. Repaired by
letting the anchor step over leading `…;` statements; `test_the_guard_itself_can_fail` now plants a
compound line.
(2) Plan A5a's instruction that `morale_start` "needs a `_CELL_OWNED` whitelist entry or the sweep
gate blocks its own fix" is **wrong**: the field pattern is name-bounded, so `.morale_start =` never
matched the `morale` sweep. The entries were written, mutated away, and everything still passed —
they exempted nothing. Removed rather than kept as harmless: a whitelist line that protects nothing
advertises a protection that does not exist.

**Citation critic (non-negotiable per the plan; 5 pre-existing flagged constants, none introduced).**
`sim_mb_06_v9_historical_spec.md` — uniform P4/C4/D5/M6 — resolves EXACTLY against the source text.
`mass_battle_v30.md §deployment — anchor columns` **DOES NOT RESOLVE**: that doc has no `§deployment`
section and no anchor-column table. Checked derivability instead — measured Line widths 3/5/5/7 at
tiers 1-4 give centres 12/12/11/11, so no centring rule yields 11/10/9/8. Re-labelled `[JUSTIFIED:]`.
The same unresolvable citation is still live at its ORIGIN, `gauge_mb.py:60,64,65,66` — filed, not
chased.

**Falsifier fired, and it re-derives A6a.** The harness now reports its own precondition beside the
number: melee **40/40 trajectories routed** despite the `NO_ROUT_MORALE=1e9` pin, fit window
collapsed to **30 ticks** of a 160-tick budget (per-seed min/median/max 30/35/47); volley 0/40 routed
but at 0.0% casualties both sides (hence the `inf` exchange ratio). So `melee p=2.50` is a fit on
rout-truncated data and `volley p=0.50` a fit on a flat line. Orchestrator-derived, replicating what
had been agent-only (G12). Repair is A6a. Grid golden `unit` verified byte-exact after the sweep.
## 2026-07-29 — ED-MB-0048 plan-v2 A3: sub-phase truncation counted (weight, not fire-count)

`orchestration.py`'s `MAX_SUB_PHASES` `break` was bare — engagement groups past the 5th deal zero
damage that tick, unlogged. Now counted: `truncated_groups`/`truncated_pairs`/`truncated_troops`
(engaged-troop WEIGHT via `_pair_engaged_troops`, the existing single owner — truncation drops the
DEEPEST-sorted groups, a systematic bias a fire-count cannot express) plus `n_groups` as the
control, threaded to `run_battle`'s result. Rides the result dict, not `trace_event` (a no-op unless
tracing is on). `MAX_SUB_PHASES` NOT changed — CALIBRATED-DEBT.
**Orchestrator re-derivation (the audit's row was agent-only/UNVERIFIED, G12): 64,273 resolver
calls across all four `bat.py` modes at the CI pin vector + the honest gauge in each — 0
truncations, max depth-group count 3 vs bound 5.** All four goldens byte-exact with the probe
attached (`audit/2026-07-26-mass-battle-fable-audit/subphase_truncation_probe.py`), which is also
the proof the instrument does not perturb what it measures. Guards:
`tests/valoria/test_subphase_truncation_counter.py` (3) — one drives the bound down to FORCE a
truncation so the counter is shown able to observe one, one asserts silence with headroom, one
asserts incidence zero at the shipped bound *with* a non-vacuity check. 3/3 mutants killed.
## 2026-07-29 — ED-MB-0045 plan-v2 A1a: field goldens bisected + re-recorded after 5 days red

**Relocated verbatim** to `tests/coverage_matrix_archive_2026-07-25b.md` (ED-MB-0061,
2026-07-30) to keep this register under its 15,000-token cap. Nothing condensed or dropped.
## 2026-07-30 — mass_battle: two false canonical citations removed (ED-MB-0061)

**Comment-only; zero behaviour change.** Grid digest re-verified `unit 241f04e5…` (unchanged).

- `geometry.py` `octagon_angle` — two citations removed that do not resolve (`§A.3b` is BATTLEFIELD
  GEOMETRY, banner-superseded; `§octagon` does not exist — the head doc has **zero** occurrences of
  "octagon"). CLAUDE.md §7's leaky-anti-fabrication pattern, on the facing model's own boundary
  constants. Re-pointed at ED-MB-0018. Found by a `fable` audit, re-derived by hand before removal.
- `core/contact.py` — *"Co-location is now geometrically impossible on the field path"* is **false**,
  now retained only as a warning. Refuted by 875 deep cross-side interpenetrations and by
  `test_obb_contact_toi`'s two failures.
## 2026-07-30 — mass_battle: the last unswept absolute-morale write, FILED not fixed (ED-MB-0061)

`test_persubunit_stress.py:191`'s bare `u.morale = 0` is the last unswept absolute-morale write.
HANDOFF_MB named it as a precondition of the `PC_CELL_MORALE` flip — *"sweep them before the flag
flips"* — and it was missed when the flip happened. A bare assignment is a silent no-op once cells
are seeded (`eff_morale` reads the cells and never falls back to the scalar), so at
`PC_CELL_MORALE=1` this harness asserts a rout it never caused. **S13 is therefore vacuous at the
shipped defaults.**

⚠ **The one-line sweep was made, then REVERTED, and the reason is the point.** Touching that file at
all pulls **98 pre-existing uncited constants** (`tier=1`, `col=8`, `command=4`, …) into the blocking
Sim Anti-Fabrication gate, because the gate scans whole changed sim files. That is CLAUDE.md §0.1
point 5's documented trap almost verbatim — *"widening scope has a real cost — sweeping two
out-of-scope harnesses here dragged ~100 pre-existing uncited constants into a blocking gate"* — same
file class, same order of magnitude. A comment-only fix does not help either: **any** edit to the
file triggers the same scan.

The two ways to keep the fix were both worse than the fix: cite 98 constants I did not author (which
is fabrication wearing a citation), or add a co-located `sim_verification_ledger.json` — which, since
this file sits in `tests/sim/mass_battle/`, the LIVE ENGINE directory, would exempt the entire
engine tree's constants from the gate. So the fix is filed rather than forced, per §0.1 point 5's own
instruction to sweep only what the task is load-bearing on. Scope: harness-only; no engine path, no
golden motion, and the engine-side half of this defect class was already closed by ED-MB-0058.
## 2026-08-05 — the evacuation (ED-IN-0145)

The `tests/sim/` stress corpus this matrix indexed was evacuated: ~330 simulation reports, batteries
and manifests, none of which were an executable spec or a code pair. What SURVIVES under `tests/sim/`
and is still covered here is the canon mass-battle engine (`tests/sim/mass_battle/`), the numpy-free
parity oracle (`tests/sim/v32-combat-balance/`), and `gauge_mb.py` — the module two kept shipping-gate
tests import by name.

Rows below that point at evacuated reports are retained as the record of what was covered before the
cut; their subjects live at the fork reference (`c451bcb`). Do not treat a row here as evidence a file
is present.
## 2026-08-14 — the ruled degree ladder reaches the canon engine (ED-IN-0187)

`tests/sim/mass_battle/resolution.py:compute_degree` was rebanded onto Jordan's 2026-08-14 ruling:
the margin `net - ob` decides the band (`>=3` Overwhelming, `>=1` Success, `[0,1)` Partial, `<0`
Failure), replacing the `net >= 2*ob AND net >= 3` bar. The `_DEGREE_EPS` ulp-recovery tolerance is
unchanged in role and now guards the three margin boundaries instead of the old three.

**The ladder is spelled out here rather than imported, and that is deliberate.** This tree is the
canon engine (J2) and takes no `engine.*` dependency; adding one is a porting-architecture call
nobody has made. Equivalence with the owner (`engine/autoload/dice_engine.degree_from_net`) is held
by measurement instead: `tests/valoria/test_degree_ladder_single_owner.py` evaluates both over 1,490
cells (integer + quarter-step) and fails on any divergence, so drift is loud rather than silent.

**Coverage unchanged in extent, sharpened in claim.** `tests/valoria/test_degree_boundary_epsilon.py`
still guards this function and now pins the *adjacent* band at each boundary rather than a distant
one — the old ceiling assertion (`!= "Success"` at a margin of −1e−6) had become unfalsifiable under
the reband, since Success sits three bands away. Scope: the degree function only. No golden motion in
this engine, no change to the RNG path, no new file.

### Field goldens re-recorded (same change, 2026-08-14)

`bat.py`'s `unit_field_mor0`, `cell_field_mor0` and `cell_legacy_mor1` moved with the reband —
`compute_degree` feeds `DAMAGE_BY_DEGREE` on every exchange, so a band change reaches every digest.
Re-recorded from the reference CI run, with the previous values preserved inline.

**Read this before trusting a local green on these modes.** `tests/valoria/test_mass_battle_byte_exact.py`
covers the two legacy-lattice modes and reports skip/xfail locally (documented platform non-portability plus a
pre-existing known-red). The three modes above are gated by `tools/ci_golden_modes_check.py`, a
separate blocking CI job that does not run locally at all. A local suite green says nothing about
them — which is how an adversarial critic's correct prediction got recorded as "overturned" here
before CI settled it.

### Mode-key vocabulary corrected: `grid` → `legacy` (Jordan, 2026-08-14)

> "We have no 'grid' mode in mass battle. It always occurs on a coordinate field. Only the subunits
> can be said to be a grid."

`FIELD_MOVEMENT` defaults to **1** — the coordinate field is the model, not a mode of it.
`FIELD_MOVEMENT=0` is the pre-migration integer lattice (Chebyshev distance, int-rounded positions),
retained only as a byte-exact regression arm; `validators.py:220` already described it as "the legacy
integer path". The golden mode key called it `grid`, which reads as a second way the game can be
played — and was read that way, by me, in ED-IN-0187's own commit message.

Renamed in `bat._mode_key` and the three affected `EXPECTED` keys (`unit_legacy_mor0`,
`cell_legacy_mor0`, `cell_legacy_mor1`), plus the two tests and the CI checker that assert them.
**No digest is touched** — these are lookup labels; every recorded value carries across byte-for-byte.

Coverage is unchanged in extent. What changed is that a cold reader can no longer infer a movement
mode that does not exist. Historical dated entries in `bat.py` keep the old word (no-retrofit,
CLAUDE.md §4) — **except two 2026-07 blocks a blanket replace caught before that rule was written,
which now sit inconsistently beside their unchanged neighbours; disclosed in `bat.py`'s vocabulary
block rather than tidied away.** `validators.py`'s separate `path='grid'|'node'` argument is filed,
not swept.

## 2026-08-24 — the canon mass-battle engine moves to `systems/mass_battle/sim/` (Jordan-directed)

**Coverage is unchanged in extent; every path in this file that reads `tests/sim/mass_battle/` now
lives at `systems/mass_battle/sim/`.** Historical dated entries above keep the old path (no-retrofit,
CLAUDE.md §4) and resolve through the dir-prefix row added to `references/restructure_ledger.md`.

What moved and why: `tests/sim/mass_battle/` (11,342 lines, 28 modules) was ported over
`systems/mass_battle/sim/`, overwriting the 1,905-line engine the campaign had been running. An
audit established that the tree under `tests/` was the game's most developed battle model — a live
test calls it "the canon mass-battle engine", 43 of 156 `tests/valoria` files import it, and every
recent ED-MB batch landed there — while the campaign ran the smaller one. Jordan ruled the port.

**What this means for coverage claims made above.** The paragraph at :314 arguing that a file's
location inside `tests/sim/mass_battle/` (the LIVE ENGINE directory) should not exempt it is now
moot in its literal form and stronger in its substance: the live engine is no longer under `tests/`
at all, so nothing there can claim a test-tree exemption. The claim at :322 — that what is covered
here is the canon mass-battle engine — still holds; only its path changed.

**Not a coverage change, recorded so a reader does not go looking:** `tests/sim/gauge_mb.py` and the
package `__init__.py` files appear in this commit's changeset as deletions rather than additions.
They moved with the engine; nothing was dropped.
