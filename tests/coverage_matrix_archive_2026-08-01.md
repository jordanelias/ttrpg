# Coverage Matrix — archive slice, cut 2026-08-01

Sections moved out of `tests/coverage_matrix.md` to keep it under the 15,000-token register cap
(`tools/ci_register_size_check.py`). **Verbatim; nothing condensed or dropped.** Covers the
2026-07-24 `ED-MB-0033..ED-MB-0037` span — the Fable logic audit's Part-A remediation,
field-coordinate unification, the `perimeter.py`/cavalry-orbital-wheel wiring, the orphaned
`MORALE_EROSION_DAMP`/`SUBUNIT_ROUT_FLOOR` wiring, and the superseded dead-mechanic constant
removal.

Cut during ED-MB-0062 (the absolute-mode-key rename), which needed room in the live matrix to
record what each digest mode now IS. The live file was at 14,655/15,000 — 2.3% headroom — so the
next entry of any size would have breached the cap rather than been written.

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


