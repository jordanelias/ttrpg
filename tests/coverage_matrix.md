# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md

## 2026-07-25 — ED-MB-0041 Tier-2: dead machinery wired or deleted + provenance retag

Seven items from the deep adversarial audit's Tier-2 list ("wire or delete, no third option"). Every fix
carries a regression test verified to **fail** against the pre-fix code, not merely to pass after it.

- **`dynamic_facings` — DELETED.** A write-only parallel facing store: built by `run_battle`, passed into
  `resolve_engagements` (which never read it), written by `_rotate_defender_facing`; its only reader
  `_atom_avg_facing` had zero call sites in the corpus. The concept is live and better served by
  `Subunit.cell_facing_vec` (discipline-gated slew, rout flip, and what `_octagon_cell_mods` actually
  reads). Behaviour-preserving by construction — **byte-exact goldens confirmed unchanged**.
- **`_front_fixers` — SCOPE FIXED.** Computed inside `resolve_engagements` from that call's pair list,
  which under `CASCADING_ENABLED` is one cascade sub-phase *group*, not the tick. A defender pinned
  frontally in group 0 and flanked in group 1 saw an empty fixer set and wheeled freely — the Cannae
  shape exactly, so the mechanism was dead in the case it exists for. Hoisted to `_compute_front_fixers`,
  computed once per tick, threaded in like `eng_counts`/`atom_sides` already were.
  (`tests/valoria/test_front_fixer_scope.py`, 3 tests.)
- **`cell_last_speed` — MADE AN IMPULSE, plus a charger-role latch (and a correction to my own
  diagnosis).** Both paths `continue`d past a halted cell without touching the speed map, so a cell kept
  the speed it charged in for the rest of the battle — and a cell is halted exactly when it is in contact,
  so every melee cell scored its charge impetus on every tick of a grind. Halted cells (and bodies ordered
  to `hold`) now record 0; the impact tick is unaffected because `halted_cells` is rebuilt from
  *pre*-movement contacts, so the charge still lands once, at impact.
  - That alone collapsed the pike-vs-cavalry retention margin from >0.02 to **0.0035**. The modelling
    error was one level up: `a_mom > b_mom` identifies **who the charger is**, it is not the cause of the
    recoil — the cause is a mounted body pressed onto set poles, and a wall does not stop repelling after
    one tick. The charger role is now **latched at impact** (`atom._pressing`) and held while the pair
    stays in contact; brace, frontal zone, cavalry-only and the reach test are all still re-evaluated
    every tick, so the wall stops repelling the moment it is broken, flanked or out-reached. The latch
    expires when the bodies part and at the battle boundary.
  - **CORRECTION.** I first recorded this as a Tier-3 punt, on the reading that the impulse *cost* gauge
    row C1 (cavalry vs a steady unbraced line — the Burkholder/Sabin anchor), which I had measured at
    85-87%. Bisecting against a clean pre-Tier-2 tree showed the opposite: **C1 is 86.7% at the baseline**,
    and the impulse is what brings it to **48.3%, inside its 35-55 band**. I had attributed a pre-existing
    failure to my own change and written up a trade-off that did not exist. With the latch both anchors
    hold at once. (`tests/valoria/test_charge_momentum_impulse.py` for the impulse,
    `tests/valoria/test_charger_latch.py` for the latch's full lifecycle — set, survives the differential
    going flat, released when the bodies part, cleared at the battle boundary.)
- **`col_grid` — REBUILT FROM LIVE CELLS.** Built once in `Unit.__post_init__` from the spawn footprint;
  `sync_col_grid` refreshed only `density`, only for columns already in the list. Column membership was
  frozen at spawn, so a body that wheeled or drifted occupied columns absent from its own grid — at which
  point `_fatigue_sigma` found no live blocks and returned 0.0 and `_defender_depth` returned 0.0. **No
  fatigue and no depth-based charge absorption, for precisely the manoeuvring units.** Membership and
  per-column `depth` now track live cells (dead cells excluded so an emptied rank stops padding depth);
  stamina/start_density carry over for surviving columns. (`tests/valoria/test_col_grid_rebuild.py`, 3 tests.)
- **Rout triggers — PUT ON ONE CLOCK.** Morale collapse was checked per tick; annihilation
  (`troop_total < SUBUNIT_ROUT_FLOOR`) only at a phase boundary, every `TICKS_PER_PHASE`(=6) ticks, so a
  subunit ground below the floor kept fighting at full effectiveness for up to 5 more ticks.
  `rout_resolution` keeps its boundary check (idempotent), so §A.12 sequencing is untouched.
- **`PC_WHEEL` — PORTED TO THE LIVE PATH.** Shipped defaulting **ON** and was a no-op: its only consumer
  sat in legacy `advance_cells`, which returns early on the node path. Now a `_resolve_maneuver_goal`
  branch — a body whose whole footprint lies beyond the enemy's frontage turns in on the nearest enemy
  cell rather than marching its spawn file into empty air. Inert for any body with a file inside the enemy
  frontage. **This fixed the broken instrument at gauge row H6**, which read 0.0/0.0 casualties across
  60/60 seeds (audit §5.1) and now resolves.
- **`yielding` — CLEARED AT THE BATTLE BOUNDARY.** The one DG-2 transient `reset_morale_between_battles`
  missed; with rally off nothing else clears it, so a subunit that yielded once stayed flagged for the
  rest of the campaign.
- **Provenance: 24 dangling citations retagged.** Tier-0.1 deleted `tests/sim_verification_ledger.json`;
  24 constants across `config.py`/`bat.py`/`engine.py`/`workbench/server.py` still cited it as
  `[canonical: ...]` — a tag pointing at a file that no longer exists, the one state the audit calls
  unacceptable. All retagged **`[CALIBRATED-DEBT: … — magnitude fitted to engine behaviour, no external
  source]`**, naming the deleted whitelist so the history is not laundered either. `CALIBRATED-DEBT` is a
  fourth honest label beside GROUNDED / JUSTIFIED / DECLARED-DIVERGENCE and says what the others cannot:
  *this number has no source at all*. Twenty-four is the honest count of that debt today.

**Gauge (multi, the resolving mode): 5/20 → 10/20**, verified on the shipped tree. Not a tuning result —
no constant was touched. These fixes had been silently removing effects the model intended to have (or,
for momentum, silently *adding* one: a permanent shock bonus for standing still). Rows now in band: H1,
H2, H3, H7, H8, H11, C1, C3, C5, C7. Still out: H4, H5, H6, H9, H10, R1, R3, C2, C4, C6. The same caveat as Tier-1 applies: the bands were
implicitly fitted around distortions that are now gone, so movement in either direction is expected and
is not evidence about the bands.

**Open, surfaced by this pass:** H3 (Envelopment vs Line) reads 61.0 and its reverse H10 reads 76.7 —
the same physical matchup with the armies swapped between the A and B slots, which should sum to ~100
and sums to ~138. The mirrors (H1 50.0, C3 50.8) are clean, so this is matchup-specific, not a uniform
slot bias. Not diagnosed here.

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

## 2026-07-23 — ED-MB-0032: fractional combat pool ("pool must be fractional")
- Jordan directive: the continuous pool was floored to an integer die count before `roll_pool`,
  discarding the fractional remainder. `roll_pool_fractional`: integer part rolls real d10s, fractional
  remainder contributes its EV (`PER_DIE_NET_EV=0.4`, the TN-7 face-rule EV); sub-1 pool contributes only
  its fractional EV (no floor to a guaranteed die). Sigma-boost reads the fractional pool. Wired into the
  sigma-head `a_net`/`b_net`.
- Verified: pool 3.0 vs 3.7 differ in mean net by ~0.7·0.4; integer pools reduce to `roll_pool`; monotone
  across integer gaps. Gated `PC_FRACTIONAL_POOL` (default OFF → byte-exact, bat.py EXIT=0). Tests:
  `test_fractional_pool.py` (6).
- Gauge ~neutral (correctness/precision fix, not band-optimizer); fair fractional ruler needs its own
  calibration pass. (Archived the 2026-07-02/04/05 blocks to `coverage_matrix_archive_2026-07-23.md`.)

## 2026-07-23 — ED-MB-0031: stochastic rout breakpoint at the historical 15-30% casualty band
- Jordan historical research: "routs occur as early as 15% losses with 30% the upper hand." The canonical
  §A.4 casualty→morale steps don't fire until 50% losses, so units grind to ~90% before breaking. Models
  du Picq will-to-fight collapse: each subunit draws a **fractional** break-point in [ROUT_ONSET=0.15,
  ROUT_CAP=0.30], skewed by resilience (discipline + starting morale) — a steady body holds toward 30%, a
  shaken one breaks toward 15% — and routs when its casualty fraction crosses it.
- Result (rout_probe OFF→ON): loser casualty-at-rout **91.7%→31.8%** (even), 88.8%→30.3% (disc5v3);
  winner ~20%→~10%; length 2.5→1.1 turns.
- Fractional throughout (random draw + fractional band + fractional loss), reproducible under the seeded
  RNG. Gated `PC_STOCHASTIC_ROUT` (default OFF → no draw → **byte-exact**, bat.py EXIT=0; NOT inert when
  on — moves goldens, needs_jordan). Tests: `test_stochastic_rout.py` (7).
- **Coupled next:** lower per-tick lethality (battles now end at ~30% but in ~1.1 turns; casualty chunks
  overshoot the break-point) + fractional dice, then re-gauge vs Dupuy/Sabin.

## 2026-07-23 — ED-MB-0030: conditional orders (own_strength trigger + locked distance-conditional)
- Jordan directive: "conditionals — a unit only starts retreating when the opponent is within X /
  advancing then withdrawing when X." **Verified** the existing `Order` primitive already covers the
  DISTANCE case: `Order(trigger='enemy_range:D', behavior={'stance':'retreat'|'yielding':True})` fires
  when the subunit closes within D; `stance`/`yielding` are both `_ORDER_SAFE_FIELDS`; `build_army`
  forwards the spec `orders` key. Locked in with `test_conditional_orders.py` (fires on close; does not
  fire out of range) — no redundant knob added (bottom-up reuse).
- **Added** the missing `own_strength:FRAC` trigger: fires once `troop_total()/_start_troops <= FRAC` —
  a unit reacting to its OWN attrition (withdraw a spent body, commit a weakened one, brace when
  thinned). Wired in `units.py` Order validation + `_ORDER_TRIGGER_KINDS` + `contact.py` `check_orders`;
  reuses the `_start_troops` spawn denominator (no new state).
- Byte-exact (orders default `()`; goldens carry none; bat.py EXIT=0). Tests: 8 in
  `test_conditional_orders.py`.

## 2026-07-23 — ED-MB-0029: intent as an offence/defence resolution axis
- Jordan directive: "hold-and-defend vs rout-the-other resolve differently — intent makes a big
  difference." `stance` (was movement-speed only) is now a signed offence/defence **commitment** in the
  exchange: `cX` ∈ {aggressive +1, balanced 0, hold/retreat −1} enters the sigma head as delta-sigma net
  `ns_a += (cA·OFF + cB·DEF)·SIGMA_PER_D` (own press + enemy exposure/blunting), symmetric for B —
  uniform-impact like the octagon/puncture terms, **not** a raw damage multiplier.
- Anchored to the §A tactic-card **asymmetry** (Disciplined Defence +1D; Standard Advance no effect) →
  `DEF=1.0 > OFF=0.5`: a holding pin **survives** a pressing foe (buys time, Cannae centre); aggression
  is punished vs a steady wall.
- Effect (intent_probe, OFF→ON): hold-vs-balanced holder casualties 67→57 & win 35%→50%;
  aggressive-vs-hold holder wins 65/35.
- Gated `PC_INTENT_RESOLUTION` (default OFF; balanced=0 → inert; byte-exact, bat.py EXIT=0). Tests:
  `test_intent_resolution.py` (8). Detail: `rotation_model_v1.md`.

## 2026-07-23 — ED-MB-0028: cell-level closing-ranks lifecycle (T1 Phase 1a)
- Foundational primitive for Jordan's rotation directive: `Subunit.close_ranks()` reflows a subunit's
  **living** troops front-rank-first (`orig_r` asc) toward each cell's spawn density (`_cell_target`),
  depleting the rear. A **deep** formation holds full front-cell density — hence full front combat pool
  (`_pair_engaged_troops` weights by engaged-front-cell troops) — until depth is spent; a shallow one
  thins at the front immediately. Makes literal the reserve the depth machinery only abstracted;
  `PC_REFILL_FLOOR` was never wired.
- Conservation exact; relational (troops close toward the front, no scattered holes); emptied cells keep
  key at 0.0 (functional coverage-shrink, no cell-set mutation — Phase 1b handles literal dissolution).
- Wired into the tick **after** both units' casualties (stays simultaneous) + col-grid resync.
- Gated `PC_CLOSE_RANKS` (default OFF → byte-exact; bat.py 4 modes EXIT=0). Effect: DEEP(3×4) vs
  SEMI(6×2) **81%→94%** ON. Tests: `test_close_ranks.py` (7). Detail: `rotation_model_v1.md`.

## 2026-07-23 — ED-MB-0027: honest-gauge measurement integrity (density held at 100/cell)
- Fixed the confirmed #1 gauge distortion (fiat register M1): the per-cell **density mismatch** between
  `make_unit→build_unit` (legacy tier footprint, ~16/cell) and the composed presets (`concentration=100`).
  Density enters `_lanchester_strength` **linearly**, so the ~8× gap — not flanking geometry — drove
  H3/H4/C4 to a fiat 100% (null test: dense-vs-thin, zero envelopment, already 100%).
- **Fix:** hold density constant at `GAUGE_CONC=100` across every gauge unit by building single AND
  composed units from the same explicit troops/concentration path (`build_army→footprint_for`);
  `GAUGE_TROOPS=600` divides evenly under every split (1/3,2/3,1/2) → exact quantization. Verified all
  unit types build at exactly 100.0/cell, hp_max=600.
- **Fair-ruler result:** H1 mirror 50/50 (was 44/56); envelop/refused/wedge **flip to ~0%** (force-
  splitting is pure downside — geometry converts to no outcome); 15/20 rows flag real engine divergence
  (brace P2 not repelling C2/C6=57 raw; cav mirror C3=71 asym; GappedLine H7/H8 over-strong).
- Bands NOT re-fit (§8 north star). Gauge is a manual harness (no `test_` funcs → not CI); `bat.py` has
  its own `make_unit` → byte-exact goldens unaffected. Detail: `honest_gauge_readout.md`.

## 2026-07-23 — ED-MB-0026: explicit frontage×depth (columns×rows) + gradient-forwarding fix
- `Subunit.width`/`depth`: both set → `footprint_for` builds an exact width×depth rectangular grid
  (density = troops/(w·d) follows) — the coupled tactical axes (wide-shallow = frontage/envelopment;
  narrow-deep = breakthrough/depth). Threaded through `_oriented`, `_spec_span`, `build_army` forwarding;
  Subunit validation now accepts troops + (concentration OR width×depth).
- Closes an ED-MB-0025 gap: `build_army` never forwarded `distribution` (gradient) nor width/depth from the
  spec dict — now all forwarded, so the full deployment-primitive set is reachable via the army-builder.
- Byte-exact unaffected (all inert in tier mode; bat.py uses tier). Tests: `test_deployment_primitives.py`
  (+2 = 9); 138-test mass-battle sweep green.

## 2026-07-23 — ED-MB-0025: explicit subunit deployment primitives + build_envelopment wing fix
- **Explicit density honored:** `footprint_for` now interprets `concentration` as target troops/cell and
  builds the exact implied cell count via `_build_shape_n` (arbitrary-N shape builders) — fixes the M2 bug
  where a 133-troop Line collapsed to 1 cell at every concentration (density silently inert), the root of
  the 8–12× composed-vs-single per-cell density mismatch.
- **Density gradient:** new `Subunit.distribution` ∈ {uniform, front, rear} weights `cell_troops` across
  ranks (front = shock/leading-rank-heavy, rear = depth/Leuctra deep wing), conserving `troop_count`.
- **build_envelopment wing fix:** wings placed relative to the center's *actual* column (honors a pre-set
  `starting_position`) instead of a phantom field-center anchor — pre-fix wings landed at 21/27 while the
  center sat at col 9 (never wrapped); now they straddle it. Explicit wing positions also honored.
- **Verified:** mirror-symmetry (n=120 × 4 seed bases) ~50/50, no bias → combat/movement already Jacobi.
  Honest gauge (matched-density explicit blocks): envelopment 100% → ~40% → density artifact gone, mechanic
  under-performs (real work remains). All 4 bat.py goldens re-recorded (deliberate composed-row change;
  tier mode → density/gradient inert there): unit b70a9348, cell d46c8808, unit_field 3cc40104, cell_field f9c6dea1.
- **Adversarial-review fix:** `build_refused_flank` had the *same* phantom-anchor bug (5th-critic finding) —
  refused wing placed against the field-center, ignoring an explicitly-placed strong wing. Same fix applied
  (honor pre-set positions; place the refused wing on the strong wing's actual span). Latent (the gauge sets
  both positions explicitly → byte-exact unchanged), was uncovered by tests; now covered.
- Tests: `tests/valoria/test_deployment_primitives.py` (7 — incl. refused-flank sibling-fix).

## 2026-07-23 — ED-MB-0024: DG-2 fighting-withdrawal residuals (emergent entry + rally + pocket exits)
- Completes the three parts ED-MB-0005 deferred after shipping the yield state + commanded entry
  (`proposals/mass_battle_fighting_withdrawal_v1.md` §2.2/§2.4):
  - **Emergent auto-entry** (§2.2, `morale_check_phase`): a disciplined subunit (`eff_discipline >=
    D_YIELD`, `command>0`, non-ranged) crossing the §A.4 `frac<0.50` casualty trigger **enters yielding**
    instead of only eroding. Sets state only — the erosion-brake calibration stays deferred (`needs_jordan`).
  - **Rally exit** (§2.4, `between_turn_recovery`): at the turn-break lull a yielding subunit whose morale
    recovered to `>= YIELD_RALLY_MORALE_FRAC` (0.75) of start reverts to normal combat.
  - **Pocket exit** (§2.4, new `Subunit.pocketed` via `_yield_pocketed`): rearward motion blocked (flee
    vector off-map, or an enemy within `YIELD_POCKET_REACH` in the retreat path) → yielding holds with the
    combat malus **removed** (Cannae's pinned-and-annihilated kill condition). Reuses only `enemy_cells` +
    `BATTLEFIELD_SIZE`, no new collision code.
- **All three gated OFF** (`PC_YIELD_EMERGENT` / `PC_YIELD_RALLY` / `PC_YIELD_POCKET`) → yielding never
  auto-set, rally never fires, `pocketed` never set + the exchange guard reduces to the ED-MB-0005 malus →
  **byte-exact** (bat.py all 4 digests byte-identical). `pocketed` cleared at the battle boundary.
  `needs_jordan` on the three flips, the emergent path's blast radius (§4.3), and both CALIBRATED-DEBT
  magnitudes.
- Tests: `tests/valoria/test_dg2_yield_residuals.py` (10) — emergent on/skip-low-disc/off-inert, rally
  revert/keep/off-inert, pocket map-edge/enemy-behind/open/malus-removed.

## 2026-07-23 — ED-MB-0023: Reserve formation Phase-3-commit rule (PP-MB-04 / §A.6)
- Wires the previously-inert `reserve` instruction (config `ROLE_SPEC` "Reserve"/"Support", zero code
  consumed it) into `run_multi_unit_battle`. A unit held in Reserve (`unit_in_reserve` — any subunit
  carries `reserve`) is **benched turn 1** and its pairing **commits** (re-activates) at
  `RESERVE_COMMIT_TURN`=2 (Phase 3 of the next turn), engaging from Phase 5 of that turn — canonical
  "declare turn N → commit Phase 3 turn N+1 → engage Phase 5 turn N+1", not delayed to N+2. First
  engagement uses the default equal Off/Def split (no Phase 1 window) — already this path's behaviour.
- Termination guard extended so a battle whose only pair is a still-benched reserve doesn't break early.
- **Gated OFF** (`PC_RESERVE_COMMIT`, default 0) → reserve inert, all pairs active turn 1 → byte-exact;
  `run_multi_unit_battle` isn't in the bat.py golden battery → double-safe. `needs_jordan` on the flip +
  the battle-turn-granularity modeling (whole engagements per turn, so "commit P3 / engage P5" collapses
  to "engages from turn 2").
- Tests: `tests/valoria/test_reserve_commit.py` (4) — predicate, ON bench-then-commit-turn-2, OFF inert,
  no-reserve battle unaffected.

## 2026-07-23 — ED-MB-0022: Feigned Retreat tactic (PP-256)
- Wires the previously-inert Feigned Retreat dice-modifier row (mass_battle_v30 §A.12 / §B.4) into the
  field engine's pursuit path. A unit that declares a Feigned Retreat (`Unit.feigned`) withdraws as if
  routing to bait a pursuer; when a Fast victor pursues it, `resolve_feigned_retreat` runs the two-stage
  resolution — (1) pursuing general rolls Command Ob 2 to **recognise** the feint (success → no effect);
  (2) if deceived, a Discipline **Ob 1** check (PP-256). Failing (2) marks the pursuer `overextended`,
  cutting its next engagement pool by `OVEREXTEND_PENALTY` (=2) via a gated branch in `base_combat_pool`.
- **Convention (verified, not a bug):** the checks use the shared `roll_pool` net-successes convention
  (botch die included) that every §A check uses. Realized hold rates: Disc-1 ~40% (matches PP-256 exactly),
  Disc-4 ~74.5% vs the doc's no-botch binomial ~87%. A bespoke botch-free counter was rejected (scale-local
  dialect = CLAUDE.md §10 guardrail).
- **Gated OFF** (`PC_FEIGNED_RETREAT`, default 0) → flags never set + pool branch inert → byte-exact;
  additionally the pursuit path is in `run_multi_unit_battle`, NOT the bat.py single-pair golden battery →
  double-safe. Transient flags cleared at `reset_morale_between_battles`. `needs_jordan` on the default-flip
  + the `OVEREXTEND_PENALTY` magnitude (reuses the §B.4 strategic −2D at field scale — confirm transfer).
- Tests: `tests/valoria/test_feigned_retreat.py` (6) — Disc-rate band + monotonicity, recognise rises with
  Command, overextend only when deceived+failed, non-feigning no-op, gate-OFF inert, pool-penalty ON vs OFF.


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
