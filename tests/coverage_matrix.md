# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md

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

## 2026-07-25 — ED-MB-0042 RETRACTED: the flip was measured against an arm that couldn't recover

**The flip below was made and then withdrawn the same day. Do not cite its numbers.**

`between_turn_recovery` and `reset_morale_between_battles` both write the morale **scalar**, which
`eff_morale` stops reading the moment cells are seeded — so with `PC_CELL_MORALE` ON they are **silent
no-ops**. Verified directly: knock a body's cells to 2.0, call both, and it is still at 2.0. The gauge's
multi mode runs multi-turn battles and resets morale between them, so **the ON arm fought with morale
that never recovered and the OFF arm's did.** "The loser breaks earlier" is exactly what a body that
cannot recover would also produce. The two arms were not comparable and I reported the gain without
checking that they were.

This is the **same defect class** as the `erode_morale` silent no-op caught earlier in this lane — a
scalar write shadowed by the cell aggregate. I fixed that one instance and never swept for the pattern,
so it recurred, in the same session, and this time it reached a shipped default and a golden re-record.
**The lesson is about scope of fix, not about morale:** when a defect's cause is "a representation
change orphaned its writers", the unit of repair is *every writer*, found by grep, not the one that
happened to fail.

Reverted: default back OFF, `_PINNED_OFF` back to `'0'`, both goldens back to their pre-flip digests
(`241f04e5…` / `dc3d3414…`), `test_default_is_gated_off` restored with the retraction reason.

**Two genuine defects were found by the failing suite and are KEPT** (both real bugs in the phase-1/2b
work, independent of the flip):

1. **Born-broken subunits.** `seed_cell_morale()` ran in `Subunit.__post_init__`, but a subunit whose
   morale is `None` inherits from its parent Unit and the `_unit` back-ref is not set until
   `Unit.__post_init__` — strictly later. So an inheriting subunit seeded every cell at `eff_morale`'s
   no-parent fallback of **0**, i.e. every cell broken at birth, emitting no combat weight and never
   recovering (once cells exist, `eff_morale` reads them and never falls back to the correct parent
   scalar). Now seeded from `Unit.__post_init__` for inheriting subunits. The gauge path passes morale
   explicitly, which is exactly why the targeted tests and the measurement were green while ten
   unrelated suite tests were not.
2. **A 1-ulp aggregate defeating an identity.** The troop-weighted mean of N *equal* values is that
   value mathematically but not in floats (15 cells at 6.0 → `5.999999999999999`). `_morale_sigma`
   divides by `morale_start`, so a body at full morale reported σ = −1.8e−16 instead of 0 — enough to
   cross a `DAMAGE_BY_DEGREE` boundary and turn a 6.0 exchange into a 0.0 one. A uniform body now
   returns its cells' value exactly. **My own test hid this**: it asserted the t=0 identity with
   `pytest.approx`, which is precisely the assertion that cannot see an ulp. Now `==`.

**Blocker for re-flipping** is not another gauge run — it is the scalar-write sweep. Known sites:
`between_turn_recovery` (unit + atom), `reset_morale_between_battles` (unit + atom), the rout write
`u.morale = 0.0`, `Unit.erode_morale`, and `core/state.py`'s `atom.morale = atom.eff_morale`.

## 2026-07-25 — ED-MB-0042 (RETRACTED, see above): PC_CELL_MORALE flipped ON (archived — condensed)

The same-day flip, retracted hours later — its ON/OFF arms were not comparable (scalar morale
writes the cell aggregate shadows). Do not cite its numbers. **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29, ED-MB-0057).

## 2026-07-25 — ED-MB-0041 phase 2b: local break was UNREACHABLE; the missing symmetry (archived — condensed)

Phase 2 could not fire: bodies had erosion AND a break-point, cells had erosion only, so a cell had
to be destroyed twice over to break and the body always won that race by construction. An
asymmetry, not a magnitude. Cells given their own du Picq break-point; `check_cell_breaks` runs
before contagion and cohesion. **Full detail: `tests/coverage_matrix_archive_part2.md`** (moved
2026-07-29 under the register size cap, ED-MB-0052 — nothing dropped, only relocated).

## 2026-07-25 — ED-MB-0041 phase 2: local break, cell-scale contagion, and the half of phase 1 never wired (archived — condensed)

Cells got their OWN du Picq break-point (phase 2 was unreachable without it — bodies had erosion
AND a break-point, cells had erosion only, so a cell had to be destroyed twice over to break).
8-neighbourhood break contagion; `cohere_cells` wired (it had shipped with ZERO live call sites, so
the phase-1 measurement was of aggregate-up only). **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29 under the register size cap,
ED-MB-0051 — nothing dropped, only relocated).

## 2026-07-25 — ED-MB-0041 phase 1 MEASURED: modest, as predicted; flag stays OFF (archived — condensed)

The phase-1 cell-morale measurement moved the gauge modestly and the flag stayed OFF. Superseded in
substance by the same-day RETRACTION above (its arms were confounded by scalar morale writes the
cell aggregate shadows) — do not cite its numbers. **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29, ED-MB-0053).

## 2026-07-25 — ED-MB-0041 phase 1 FIXES: two defects in the per-cell morale wiring (archived — condensed)

Born-broken subunits (seed_cell_morale ran in Subunit.__post_init__ before the _unit back-ref was
set, so an inheriting subunit seeded every cell at eff_morale's no-parent 0) and the 1-ulp uniform
aggregate that crossed a DAMAGE_BY_DEGREE boundary via _morale_sigma. Both kept; both independent
of the retracted flip. **Full detail: `tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29
under the register size cap, ED-MB-0053 — nothing dropped, only relocated).

## 2026-07-25 — ED-MB-0041 phase 1: the cell is the primitive for MORALE (archived — condensed)

Cells carry morale; the subunit's morale is the troop-weighted mean of its live cells (derived, not
stored); the aggregate pulls its own cells back at a discipline-gated rate. **Full detail:
`tests/coverage_matrix_archive_part2.md`** (moved 2026-07-29, ED-MB-0054).

## 2026-07-25 — ED-MB-0041: PC_STOCHASTIC_ROUT default flipped ON; contagion magnitude deliberately held

**Flipped, on the casualty scoreboard's evidence.** Loser 61-87% → 29-41%, winner 7.8-38% → 3.3-17%,
casualty realism 0/20 → 2/20 — while **win-share drops 10/20 → 7/20**. The count going down and the flip
still being right is the whole case for the second scoreboard. The reachability sweep had tested this
same flag hours earlier, found "passes C4, fails H9", and filed it as a wash; that was the wrong
instrument. Reversible with `PC_STOCHASTIC_ROUT=0`. Both grid goldens re-recorded (the break band
changes *when* a subunit routs, so the whole downstream casualty trajectory moves).

**`ROUT_CASCADE_FRAC` left inert at 1.0** despite measuring better: ⅔-of-line gives casualty 5/20 (and
fixes H6's 79.2% outlier → 29.7%), ⅓-of-line gives 7/20 but costs a win-share row and makes H6
*undershoot* at 14.1%. Held because (a) that is a real trade, not a clear win, and (b) per-cell state
redefines what a "section" is, so any value chosen now is fitted to a granularity about to change.

**Two methodological failures in my own experiment, recorded rather than quietly fixed:**
- **`0.34` and `0.5` returned byte-identical results — not robustness.** Three-subunit armies mean the
  broken share can only be 0, ⅓, ⅔ or 1, so both thresholds first fire at ⅔: I ran one experiment
  twice. Unexamined, "insensitive across a 47% range" would have entered the record as a robust
  plateau. A sweep over a continuous parameter must be checked against the DISCRETENESS of its target.
- **The rows that did not move were the informative ones.** H1/H2/H7/H8/H9 are identical to the decimal
  across every arm because `make_unit` builds them as a SINGLE subunit per side — broken share is 0 or
  1, so no threshold below 1.0 can fire. Inert by construction, not ineffective. An army of one subunit
  has no line to come apart, which is the sharpest argument yet for the per-cell directive: the residual
  30-33% sits on exactly those rows.

## 2026-07-25 — ED-MB-0041: the new instrument immediately overturns a default (PC_STOCHASTIC_ROUT)

**The casualty scoreboard's first act was to show that the win-share gauge has been penalising the
change that makes the engine historically correct.** `PC_STOCHASTIC_ROUT` implements the du Picq
15-30% break band (ED-MB-0031) and ships **OFF**; its own code comment says that without it "units
grind to ~58% before breaking". Measured across all 20 rows:

| | OFF (shipped) | ON |
|---|---|---|
| loser casualties | **61-87%** | **29-41%** (band 15-30) |
| winner casualties | 7.8-37.8% | **3.3-17.4%** (cap 15) |
| casualty realism | 0/20 | **2/20** |
| win-share | 10/20 | 7/20 |

One flag moves the loser from ~84% to ~31% — from annihilation to a few points outside the band — and
the win-share gauge scores it as a **three-row regression**. The reachability sweep had already found
`PC_STOCHASTIC_ROUT=1` "passes C4 and fails H9" and recorded it as a wash; that judgement was made on
the wrong instrument.

**Root cause of the residual, traced.** `Unit.derive_rout` breaks the army only when **every** subunit
has routed (`all(a.routed ...)`), and `run_battle` stops only when a UNIT routs. So sections break at
15-30% each, and then sit on the field absorbing casualties while their siblings fight on — the loser's
*total* climbs well past any individual section's break-point. Armies do not do this; they come apart
once a decisive portion of the line goes and the rest routs by contagion (du Picq: the end of a battle
is moral, not physical).

**New mechanism, gated inert:** `ROUT_CASCADE_FRAC` generalises `all(...)` to a fraction of a unit's
*starting* strength held in broken subunits. **Default 1.0 = exactly the old behaviour** (the share can
only reach 1.0 when no subunit is left unbroken), so goldens and gauge are untouched until the value is
moved. The magnitude is deliberately **unchosen** — the mechanism is du Picq-grounded, the number is
not, and picking one before measuring is the failure this whole audit has been about.
`tests/valoria/test_rout_contagion.py` (9 tests) pins the mechanism and — importantly — the *float
equality* of the inert default: `>= 1.0` on a computed ratio is exactly the kind of expression that
silently becomes 0.9999999 and changes when an army breaks.

**Two self-corrections while building it**, both caught by reading rather than by a failing test:
- My first `_broken_share` docstring said it weights by spawn strength "not the current one, which
  would shrink the numerator". That overstates: `troop_count` is *itself* a static nominal (it returns
  `self.troops`), so there was never a live alternative in play. The real reason to prefer
  `_start_troops` is that it is re-based per BATTLE, so a unit entering its third battle depleted
  measures collapse against what it started that battle with. Comment and test both corrected to the
  true property.
- Two of my own tests failed on harness errors, not engine defects (`troop_count` has no setter;
  5-7 subunits at 8-column spacing deploy off-field).

## 2026-07-25 — ED-MB-0041: the two gauge invariants that need no band (archived — condensed)

Two Jordan-approved gauge invariants that assert a RELATION rather than a historical band, so they
need no calibration: mirror symmetry (a matchup against itself must be ~50/50) and monotonicity in
force ratio. Both wired into the honest gauge; disclosed H3-vs-H10 slot asymmetry (61.0 vs 76.7,
summing to ~138 rather than ~100) surfaced by this pass and NOT diagnosed there.
**Full detail: `tests/coverage_matrix_archive.md`** (moved 2026-07-29 under the register size cap,
ED-MB-0050 — nothing dropped, only relocated).

## 2026-07-25 — ED-MB-0041 Tier-2: dead machinery wired or deleted + provenance retag (archived — condensed)

Seven Tier-2 items ("wire or delete, no third option"), each with a regression test verified to FAIL
against the pre-fix code. `dynamic_facings` deleted (write-only parallel facing store); `_front_fixers`
hoisted to full-tick scope; convergence merged_base made extensive; the charger-latch expiry made
explicit; provenance retagged off the bare-integer self-whitelist. Byte-exact goldens re-recorded where
noted in that section. **Full detail: `tests/coverage_matrix_archive.md`** (moved there 2026-07-29 under
the register size cap, ED-MB-0048 — nothing was dropped, only relocated).

## 2026-07-24 — ED-MB-0041 Tier-1: hp/cell dual-ledger reconciliation
- **Two ledgers fed DIFFERENT mechanics and could diverge permanently.** `hp` drives
  `_lanchester_strength`, `recalc_size` and the single-subunit cohesion fast path; `cell_troops` drives
  `pair_pool_contribution` and `troop_total()`'s `SUBUNIT_ROUT_FLOOR` check. Divergence sources fixed:
  (a) the **pursuit** and **freed-attacker** paths mutated `hp` with *no cell write at all* — so a unit
  ground down by pursuit still fought at full per-troop pool and could never hit the troop-floor rout;
  (b) `distribute_casualties`/`apply_to_subunit` open-coded a single clamped pass that **discarded** any
  share a cell could not absorb, while `hp` took the damage in full.
- **One owner:** new `_apply_with_spill` in `percell.py`; all three distributors now call it (the cellwise
  variant's inline copy deleted). Verified: hp/cell drift is **0.000000** through repeated pursuit damage.
- **CORRECTION to my own first framing.** I initially reported "4400 of 5000 discarded" from a uniform-weight
  probe. That was misleading: with **uniform** weights the old clamped pass and the spill agree (both empty
  everything, and the residual is genuine — nothing left to kill). The real divergence is under **NON-UNIFORM**
  weights — exactly the facing-weighted cellwise path and concentrated fire. Measured properly: two 100-troop
  cells weighted 10:1, 200 damage → **old absorbed 118.2, discarding 81.8; new absorbs 200.0**.
- Pinned by `tests/valoria/test_hp_cell_ledger.py` (3 tests, incl. the non-uniform case and a genuine-shortfall case).

## 2026-07-24 — ED-MB-0041 Tier-1: convergence partition-invariance + volley armour inversion
- **Convergence `factor = 1/N`.** `_convergence_scale`'s `merged_base` was a troop-weighted MEAN while
  `merged_troops` was a SUM, so N bodies converging on one target dealt the damage of **ONE** — firing on
  exactly Cannae/double-envelopment geometry. Made extensive (`sum`). Its premise (size-independent base,
  ED-899) is recorded as SUPERSEDED at `core/exchange.py:7`; under the live `POOL_QUALITY_MODEL` the
  correction now correctly becomes a no-op. **Measured honestly: side-swing 27.6 → 20.0pp (more symmetric),
  but average 38.8 → 35.0 — it does NOT move toward the band. A correctness fix, not a balance fix.**
- **Volley armour inversion (two compounding defects).** `volley_hp_scale` read the target's own
  `min(discipline,command)+dr`, so better armour/discipline/command **strictly increased** that unit's own
  missile casualties (a fossil of the retired `hp = size × h_per_size` model — `hp_max` is now raw troops).
  Separately, `net_after_dr` used a global `RANGED_DR_DEFAULT`, so real armour never protected at all.
  Now: flat `VOLLEY_LETHALITY_SCALE=3` (**exactly the prior gauge baseline** — inversion removed without
  silently re-tuning ranged lethality) + the target's own `eff_dr` routed into the volley.
  **Measured: casualties at dr 0/1/3 = 514.6 / 281.8 / 49.8 — armour is now monotonically protective.**
- **Regression tests, each verified to FAIL on the old code** (a test that passes both ways is worthless):
  `test_partition_invariance.py` (4 failures pre-fix), `test_volley_armour_direction.py` (2 failures pre-fix).
  Process note: my FIRST armour test passed against the buggy code — it measured total battle casualties,
  so melee DR protection masked the volley inversion; and the rewrite then deployed units 18 apart, outside
  `VOLLEY_MAX_RANGE=8`, asserting on all-zeros. Both corrected; it now drives `volley_phase` directly.
- **Goldens re-recorded (both CI-gated grid modes)** — deliberate, verified behaviour change in shared
  non-gated resolution code. `unit` 4c465e09 → c7a2eb3d, `cell` e5f09403 → 733c4547. Suite: 563 passed.

## 2026-07-24 — ED-MB-0041 remediation: Tier-0/Tier-1 execution (adversarial audit)
- **Reach gate silently disabled the braced-wall repel (biggest live defect).** `orchestration.py`'s comment
  claimed *"TROOP_TYPE_REACH is deliberately empty → this half of the gate is a no-op"*. It has **12 entries**
  (ED-MB-0014). The gate needs `reach_for(defender) >= reach_for(charger)`; `infantry 0.1 < cavalry 0.2`, so
  `PC_CHARGE_RECOIL` **never fired** for a braced generic-infantry wall — switching off the
  Courtrai/Bannockburn/Waterloo anchor and causing C2/C6 NOT-REPELLED. Comment corrected; C2/C6 defenders are
  now **pole-armed** (a brace IS a hedge of set poles; pike 0.3 ≥ 0.2 passes).
  **Measured honestly: 100.0 → 95.0 rawA.** The gate defect is confirmed and fixed, but unblocking it is
  **NOT sufficient** — the recoil now fires and is simply too weak (`PC_CHARGE_RECOIL=6 × SIGMA_PER_D=0.2`).
  The subagent's counterfactual of 0.0% did NOT reproduce at n=20. Residual gap is a magnitude problem.
- **C2 ≡ C6 duplicate broken.** They were bit-identical inputs with a fixed seed counted as two passes. C2 is
  now a genuinely DEEP block (3×6), C6 genuinely SHALLOW (6×1), both pole-armed.
- **`refuse_range` 3 → 10.** Measured minimum centroid-to-enemy approach is ~9.5, so the refused-flank release
  order NEVER fired in any caller (none overrides the default). Verified now firing (`_order_idx` 0 → 1), and
  the H6-style matchup produces casualties instead of the previous 0.0/0.0 freeze.
- **Anti-fabrication gate accepts honest provenance.** It recognised only `[canonical: ...]`, so the ONLY way
  to pass was to call a value canonical — a direct incentive for the false tags the audit found. It now also
  accepts `[GROUNDED: ]`, `[JUSTIFIED: ]`, `[DECLARED-DIVERGENCE: ]`, `[CALIBRATED-DEBT: ]` with equal force.
- **False citations corrected** (verified by hand): the 45° octagon boundary cited to `mass_battle_v30.md`
  (which contains **zero** occurrences of "octagon"); `PC_CAVALRY_SPEED_MULT` cited to a §A.7 that has no
  speed ratios; `K_LINEAR`/`LANCHESTER_STRENGTH_REF` cited to a doc whose §6 explicitly declines to supply
  magnitudes.
- **Declared divergences** (Jordan 2026-07-24: canon may be broken for tuning — it must be *visible*):
  `MORALE_EROSION_DAMP` makes the §A.4 cap −2.1 not −3 (comment previously asserted the cap was intact);
  `DISCIPLINE_LOSS_THRESHOLD` replaces canon's variable "> Discipline this turn" with a fixed cumulative 1.0.
- Deleted `tests/sim_verification_ledger.json` (26-entry bare-integer self-whitelist, `source=orchestration.py`).

## 2026-07-24 — ED-MB-0040: cell-primitive damage (the aggregate-smear bug) + historical Cannae oracle
- Jordan directive: "the cell is the primitive… each cell has its own octagon facing… its own capacity to
  receive and issue damage… flank/rear damage is supposed to be cellular… damage is done to cells."
  **BUG FOUND:** `_octagon_dmg_mod` evaluated each defender cell's own arc then **averaged** them into one
  subunit scalar; `distribute_casualties` then spread that total by **density only** — so a rear cell and a
  front cell in the SAME subunit lost identical troops, envelopment could not strip a formation
  shell-inward, and a monolith was near-unbreakable. **This is the upstream cause of BOTH the ED-MB-0038
  granularity workaround and the ED-MB-0039 "engine gap".**
- **FIX:** `_octagon_cell_mods` = the single owner of the per-cell arc; `_octagon_dmg_mod` = its mean
  (byte-identical). Gated **`PC_CELL_DAMAGE`** allocates each pair's casualties to defender **cells** by
  (troops × that cell's own facing mult) via `distribute_casualties_cellwise` (overflow-spilling, cells==hp
  holds under annihilation). Pair total unchanged — only placement. Volley keeps the aggregate spread.
- **Measured:** infantry envelop side-swing **41.0→15.5pp**, side-symmetric avg **43.8→57.8%** (into the
  55-72 band) — ED-MB-0039's "needs a new mechanic" was really this bug. **But** it re-bases the battery
  (gauge **8/20→4/20**: C4 93→71, H11 46→15) since bands were implicitly fitted to the smear → **ships
  GATED OFF**, byte-exactness verified vs the pre-change engine (identical winners + hp to 6dp).
- **HEADLINE (the real oracle):** the historical Cannae OOB (**5000 vs 8600**, real spread/subunit counts)
  yields **Carthage 0/20 both sides, flag ON or OFF** — the engine cannot reproduce history's defining
  envelopment. Missing: **per-cell morale** (local breaking), **a cost to useless depth**, **the elastic
  baiting centre**. Next: re-test all 20 precedents against their REAL orders of battle.

## 2026-07-24 — ED-MB-0038: matched command-granularity honest gauge (envelopment artifact fix)
- The honest gauge's composed enveloper/refused presets always faced a SINGLE-subunit opponent. A
  monolithic subunit is unbreakable by envelopment — flank/rear octagon mult + multi-side shock land on
  its cells but casualties DILUTE across one HP pool (`distribute_casualties`) and no section can rout
  independently, so the ED-1019 per-subunit rout cascade has nothing to bite. This pinned H3/H4/H6 (and
  reverses H10/H11) to 0% regardless of geometry: the density-matched gauge (ED-MB-0027) had unmasked a
  SECOND artifact one axis up — GRANULARITY. `granularity_probe.py`: H3 = 0% @ monolith, ~53% @ 3-command,
  ~95% @ 6-command.
- **FIX** (granularity analog of ED-MB-0027's density-constant): new `_command_army(shape, n_cmd=3)`
  deploys the composed side's opponent as a 3-command tripartite battle line (Polybius VI / triplex acies)
  at constant density, summing to GAUGE_TROOPS. Wired H3/H4/H6/H10/H11.
- **Result:** gauge multi **6 → 8/20** — H3 "full envelopment" flagship **0 → 70.7%** (band 55-72 OK),
  H11 **0 → 45.6** (band 38-55 OK); ZERO regressions (only all-failing envelop rows touched; H1/R1/C3/C4/
  C5/C7 untouched). Refuted en route: naive persistent defender reface (made it worse). Gauge-harness only
  (tests/sim/gauge_mb.py); no engine .py, byte-exact goldens unaffected.
- **Next:** side-asymmetry (H10 envelop-weak-as-B 83%), H4 wedge-centre-punch (0%), H5 refused-too-strong
  (100%), H6 stalemate; Cannae deep-baiting-centre + cavalry-rear; box-brace C2/C6.

## 2026-07-24 — ED-MB-0037: remove superseded dead-mechanic constants + zeroed _envelopment_sigma
- Wire-or-remove sweep, removal half (Jordan "obviously you can unwire a dead mechanic if it's useless").
  Removed constants that were defined+exported but read nowhere and superseded by live mechanics:
  **PC_ENVELOP_SIGMA** + its `_envelopment_sigma` (percell.py) Increment-6 term — dormant at 0.0, the
  unit-level col-grid "wider side" overhang mis-targeted a split envelop army; superseded by the octagon
  flank multiplier + multi-side shock (B6) + perimeter/orbital-wheel envelopment (ED-MB-0035).
  **ROUT_FLOOR_LOSS_PCT** / **ROUT_EXHAUSTION_MORALE_HIT** (superseded by ED-MB-0036 SUBUNIT_ROUT_FLOOR +
  stochastic rout), **PC_FLANK_DEPTH_RESIST** / **PC_FRONT_RANKS** / **PC_FLANK_CAP** (never-wired flank
  scaffolding, superseded by the octagon per-cell angle model), **REACH_LONG** (registry.py, unread).
- **Byte-exact:** every removed term was already 0.0 or unreferenced on the live path; the Increment-6
  `_envelopment_sigma` call added 0.0 and is replaced by a comment. Goldens unchanged (4 modes verified).
- Measured **PC_FACING_MODEL=1 → gauge 3/20** (regresses from 5/20) — confirms its "do not enable"
  calibration-debt (PC_FACING_SLEW_BASE unratified). Left OFF; flagged for Jordan. Gauge holds 5/20.

## 2026-07-24 — ED-MB-0036: wire orphaned MORALE_EROSION_DAMP + SUBUNIT_ROUT_FLOOR
- Wire-or-remove dead-mechanic sweep (Jordan directive). Both were defined+exported but never read.
  **MORALE_EROSION_DAMP** (0.7) → the §A.4 casualty/exhaustion morale erosion (`erode_morale(min(loss,3.0)*
  DAMP)`) — slows the bleed → longer, attritional battles; applied ONLY to gradual erosion, not the
  stochastic-rout punch. **SUBUNIT_ROUT_FLOOR** (80) → `rout_resolution`: a subunit also breaks when its
  troop total falls below the floor (too few to hold), independent of morale.
- Gauge unchanged (5/20, no regression); rout/morale tests green (22 passed). Goldens re-recorded (4 modes).
- Next: remove superseded constants (ROUT floors, PC_FLANK_DEPTH_RESIST, REACH_LONG, structural) + zeroed
  PC_ENVELOP_SIGMA; keep PC_ROTATE_FLOOR/REFILL_FLOOR (planned rotation T2/T3); measure PC_FACING_MODEL.

## 2026-07-24 — ED-MB-0035: wire perimeter.py + cavalry orbital-wheel envelopment + B6
- Orphan audit found **`perimeter.py`** (target-point/face-normal primitive, task #18) built but never
  wired. **Wired** into `_envelop_goal`: infantry enveloping wings turn onto the enemy's nearest FLANK
  face. **Cavalry orbital wheel** (`_envelop_wheel_goal`, Jordan "maintain distance = radius = wheeling"):
  a fast encircler holds a field-coordinate radius (enemy half-extent + `ENVELOP_STANDOFF=8`) and wheels to
  the enemy REAR, then closes — reaches the rear of a MOVING enemy. **B6**: multi-side shock now computed
  once on the full tick (`_compute_atom_sides`) and threaded through cascade sub-phases (was per-sub-phase
  → never fired for a front+rear body).
- **Result:** C4 cav-envelop-vs-Line **6 → 83** (into band 75-95); C7 holds 100; honest gauge **4 → 5 / 20**.
- `PC_ENVELOP_SIGMA` left 0.0 (Incr6 targeting mis-IDs the split army's thin wings; naive enable rewarded
  the defender). Full orphan inventory: `audit/2026-07-22-mass-battle-stress-test/orphaned_mechanics_audit_v1.md`.
- Goldens re-recorded 4 modes; `tests/valoria` maneuver/octagon/perimeter/reserve green (20 passed).

## 2026-07-24 — ED-MB-0034: field-coordinate unification (Fable-audit B1+B2+B3)
- Jordan directive ("nothing is golden"; "we're using field coordinates ... abandon [the spawn lattice]").
  Unified the cell-position accessors onto the live `_node_pos` field, off the dead `starting_position +
  cell_offsets` spawn lattice (not updated on the field path). **B1** `_oriented_abs_map` node branch →
  `_oriented(atom)`, skip absent ids (no `(0,0)` default): wedge contact cells stop collapsing to origin
  (**H2 decA 0.0 → 40.0**); grid branch also → `_oriented` (byte-identical for legacy). **B3** octagon
  `_octagon_dmg_mod`/`_per_cell_angle_mod` → `_oriented_abs_map` (live map; **H1 mirror → 52.5, in band**).
  **B2** `iter_cells` reads live `_node_pos` (feeds col-grid/fatigue/casualties). Added `width`/`depth` to
  gauge `make_unit`.
- **Goldens re-recorded all 4 modes** (nothing-is-golden): `unit`/`cell`/`unit_field`/`cell_field`;
  byte-exact test EXPECTED updated. `tests/valoria` green.
- Honest gauge still ~4/20: the prior 5/20 included FALSE C2/C6 passes (brace "repelling" off the broken
  contact map) — now honestly failing pending the box-brace. **Dominant remaining issue: envelopment
  delivers 0%** (H3–H6) — the split centre is crushed before the wings arrive; needs intent-on + B6 +
  wing timing + box-brace + B2b (col-grid per-tick rebuild). See `full_implementation_plan_v1.md` §1.5.

## 2026-07-24 — ED-MB-0033: Fable logic audit — Part A remediation (9 defects in this session's own work)
- Five Fable-tier read-only adversarial auditors (one per logical lane) traced ED-MB-0027..0032 and found
  9 defects; all fixed. A1 (CRITICAL): `make_unit`→`build_army` filled the §B.2 cavalry preset Power 5
  (spec never forwarded power/discipline) → gauge cavalry silently P4→P5, contaminating C-row verdicts;
  forward power/discipline explicitly. A2 (HIGH): `gauge_run.py` re-implemented the verdict and dropped
  both guards (`dec_n>0`, draw gate) → all-draw R3 false-passed on the `decA=50` sentinel → the reported
  "8/20" was inflated; delegate to `g.run()`. A3 (HIGH): ED-MB-0032's deterministic `frac·EV` mu-shift
  crossed the `net<=0` degree boundary (Jensen gap; sub-1 pools never Failed) → realise the fractional die
  STOCHASTICALLY (one extra die w.p. `frac`) — preserves EV+variance+Failure boundary. A4 (MED): frac-pool
  σ-boost read `sqrt(fractional)` → pass `floor(pool)`. A5 (HIGH): stochastic-break `erode_morale` on a
  None-morale subunit wrote the SHARED pool negative → routed every sibling; materialise own morale first.
  A6 (HIGH): `reset_morale_between_battles` never cleared `_rout_breakpoint` and loss was spawn-based →
  auto-rout on phase 1 of every later battle; clear breakpoint + re-base `_start_troops`. A7 (MED-HIGH):
  `erode_morale(eff+1)` with `eff<=-1` RAISED morale → clamp `max(eff+1,0)`. A8 (MED): `_rout_resilience`
  read LIVE discipline → `eff_discipline_start`. A9 (LOW-MED): `own_strength:FRAC` + numeric trigger
  payloads never range-checked → eager `(0,1)`-strict validation in `Order.__post_init__`.
- Honest re-measurement (A1+A2 corrected, n=20): baseline **5/20**; +`PC_STOCHASTIC_ROUT` **6/20** (R3 now
  correctly UNRESOLVED, not a false pass). Remaining 14 out-of-band rows are Part B pre-existing geometry
  bugs (B1-B4) — move goldens, filed for Jordan ratification.
- Byte-exact: every fix is `PC_*`-gated / campaign-boundary / validator-only → bat.py **4/4 modes**
  (unit, cell, unit_field, cell_field) byte-exact. `tests/valoria` green; `test_fractional_pool.py` updated
  (sub-1 pool now stochastic-EV + can-Fail, replacing the deterministic-EV assertions that codified A3).


## 2026-07-23 — ED-MB-0022 through ED-MB-0032 (archived — verbatim)
- Feigned Retreat (PP-256), Reserve Phase-3 commit (PP-MB-04), DG-2 fighting-withdrawal
  residuals, explicit subunit deployment primitives + frontage×depth, honest-gauge density
  integrity, cell closing-ranks, intent as an offence/defence axis, conditional orders, the
  stochastic-rout breakpoint at the historical 15-30% band, and the fractional combat pool.
  Full text: `tests/coverage_matrix_archive_2026-07-25b.md` (moved verbatim, not condensed).

## 2026-07-22/23 — ED-MB-0011 through ED-MB-0021 (archived — verbatim)
- spatial-model v2 Stages B-F (OBB contact / continuous frontage / weapon-class reach + pike /
  verification + golden re-record), DG-10 field-movement freeze, DG-6 per-battle combat
  effectiveness, multi-unit deployment geometry + envelopment pathing, the octagon
  damage-received multiplier + reaction delay + multi-side shock and its adversarial-review fix
  batch, the perimeter target-point/face-normal primitive, and the P-DEC-3 per-troop-type density
  cap. Full text: `tests/coverage_matrix_archive_2026-07-25.md` (moved verbatim, not condensed).

## 2026-06-15/20 — ED-1013 through ED-1032 (archived — condensed)
- Smooth command-sigma pool + continuous discipline penalty (ED-1013); gauge recalibration (ED-1014);
  cavalry-construction gauge fix, not an engine defect (ED-1015); per-subunit stat/stamina/troop-type/
  rout-morale-discipline lifecycle (ED-1016-1019); a string of bugfixes/wiring closeouts (ED-1020-1027,
  1032) culminating in the formation-drift cell-orphaning fix (ED-1032, first post-baseline digest
  change, Jordan-approved); PP-683 intentionally left unwired (would double-count encirclement lethality
  already delivered via PC_ENVELOP_SHOCK + Lanchester overlap). Full detail: tests/coverage_matrix_archive.md.

## 2026-06-30/07-01 — Re-architecture Stages 1-2 + coordinate-migration DEBT-0/S2/C0-P (archived — condensed)
- Provenance registry seed (ED-1043); bat.py byte-exact digest gate committed (baseline unit=7be8499b/
  cell=1c5b2851); Stage 1a-1g wrapper/core split complete (byte-exact); Stage 2 standalone equipment/
  package (not yet wired into resolution); FIELD_MOVEMENT continuous-speed toggle; abs→orig reverse-
  lookup centralized; Migration DEBT-0 (fabrication-debt resolved honestly, no fabrication); Migration
  S2 (Euclidean distance on the field); Migration C0+COL+G+H+F2+P (the full coordinate-field sequence,
  byte-exact OFF throughout). Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-01 — gauge_mb.py LIVE port + n=60 + tick-by-tick trace-capture backend (archived — condensed)
- gauge_mb.py ported off the dead exec-shim onto live engine.build_unit/resolve_battle (byte-exact
  reproduces prior OFF baseline 5/13); n=120->60 (Jordan directive, verified identical pass-set);
  fabrication-debt resolved; tick-by-tick trace-capture backend added (zero-cost when off). G5
  byte-exact both modes unchanged. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-01 — mass_battle workbench + Stage A: visualizer + true-adjacency stand-off halt (archived — condensed)
- Tick-by-tick visualizer (server + frontend, workbench/) verified live in both grid and field modes;
  Stage A fixed the coordinate-field co-location bug with a new `standoff()` primitive + synchronized
  snapshot (a first-mover-bias bug found and fixed mid-implementation); wired `bat.py`'s golden-digest
  gate into CI. G5 byte-exact both grid modes unchanged throughout. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-01/02 — mass_battle Stage B + bias fix + Stage C (archived — condensed)
- Stage B ported facing-slew to the field path; a mirror-matchup first-mover bias was found and fixed
  (synchronized snapshot + halved closing distance); Stage C landed `engine.build_army`, `Order`/
  `check_orders` timed sequencing, and escort/formation-relative positioning (Cannae acceptance test
  verified real lateral wheel movement, zero new flanking mechanics). G5 byte-exact both grid modes
  unchanged throughout. Full detail: `tests/coverage_matrix_archive.md`.

## Archived 2026-05-29 (pre-v32 sim rows; armature-reset coverage trim)

## 2026-07-08 — mass_battle: partition-invariance fix (ED-MB-0004) + RC-5 preliminary finding

**Jordan's rulings (AskUserQuestion, 2026-07-08):** the partition-invariance question left open by
ED-MB-0003 = **"genuine defect — fix it"** (not the historically-correct-mechanism reading); DG-2
(fighting-withdrawal/yield) = **"build it now"**; RC-5 triage = **start now, in parallel**.

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
