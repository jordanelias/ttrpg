# Coverage Matrix — archive slice, cut 2026-07-25

Sections moved out of `tests/coverage_matrix.md` to keep it under the 15,000-token register cap
(`tools/ci_register_size_check.py`). Content is verbatim; nothing was condensed or dropped. This
slice covers the ED-MB-0011..ED-MB-0021 span (spatial-model v2 Stages B-F, the octagon damage
multiplier and its review batch, multi-unit deployment geometry, DG-6, the perimeter primitive and
the per-troop-type density cap).

## 2026-07-23 — ED-MB-0021: P-DEC-3 per-troop-type density cap
- Jordan-ratified mechanism (spatial_model_v2_plan §9 P-DEC-3): a cavalry cell holds fewer troops than an
  infantry cell ("fewer horses than men fit per unit area") — a per-troop-type density cap, NOT a larger box.
- `cell_cap_for(troop_type)` (config): mounted types (cavalry/knights_templar/mounted_archers) cap at 100
  (half of `CELL_CAP=200`); foot types keep the full cap. Threaded into `footprint_for(…, troop_type)` +
  its two callers. A mounted body deploys over MORE cells (wider frontage); the combat density factor drops
  naturally via the higher `ncells` (no attrition edit).
- **Gated OFF** (`PC_TROOP_DENSITY_CAP`, default 0) → byte-exact (cell_cap_for → CELL_CAP; and the byte-exact
  cavalry rows use tier mode, not footprint_for). The cavalry cap **value** (100) is a calibration →
  `needs_jordan` on the value + default-flip (mirrors ED-MB-0016).
- Tests: `tests/valoria/test_troop_density_cap.py` (4) — OFF byte-exact, ON caps mounted lower, cavalry
  deploys wider, None-type uses full cap.

## 2026-07-23 — perimeter target-point / face-normal geometry primitive (Jordan ruling 2026-07-23)
- New `tests/sim/mass_battle/perimeter.py`: pure-geometry primitive from `perimeter_targeting_geometry_v1.md`.
  A subunit's perimeter carries TARGET POINTS an attacker aims at, each with an outward NORMAL (the
  required approach angle): **major** = face midpoints (normal ⊥ face), **minor** = corners (bisector
  normal), sharp vertex (interior angle ≤ `SHARP_TIP_DEG=60`) flagged (the pointed-formation exception).
  Faces from the convex hull (clean straight + diagonal faces; matches Jordan's drawing). `target_points`,
  `perimeter_faces`, `nearest_target` (the face an attacker engages), `approach_alignment` (how square-on
  a heading is vs the inward normal — the signal a future alignment gate/bonus consumes).
- **Pure geometry, no engine wiring** → zero golden/regression impact. The behavioural wiring
  (approach-along-normal pathing, alignment gate, interception) is the Jordan-gated next step.
- Tests: `tests/valoria/test_perimeter_geometry.py` (7) — Line=4-face rectangle, cardinal face normals,
  Arrowhead sharp-tip flagging, nearest-face targeting, square-on alignment=1.0, degenerate fallback,
  determinism. Known limitation: convex hull bridges a concave gap (GappedLine's lane) — concave/internal-
  face handling is a documented follow-up.

## 2026-07-23 — ED-MB-0019: ED-MB-0018 adversarial-review fix batch
- Jordan directive: "comprehensive max effort adversarial review." Ran 5 structurally-independent read-only
  critics (arc-math, reaction-clock, byte-exact/determinism, multi-side/balance, test-quality) + an
  architectural cell-up audit + a full-campaign gauge A/B (n=60).
- **Reaction-clock lifecycle (R1/R2):** `_react_since` was per-engagement transient state stamped with the
  per-turn tick but stored on the persistent Subunit and never reset → asymmetric re-engagement mis-scored.
  Fixed with a frame-independent, per-tick-idempotent consecutive-tick counter + reset at
  `reset_positions`/`reset_morale_between_battles` (field continuous engagements keep it via the node-skip).
- **Multi-side shock re-triggered (A1/A1-gap, arch #1):** was `eng_counts≥2` (arc-blind pair count) — two
  attackers both in front wrongly shocked (1.75×), one wide wrapping body missed. Now a **nearest-perimeter-
  FACE** bearing model (distinct faces struck), **graded** `×(1+shock·(nsides−1))`.
- **Double-count (arch #2):** `ENCIRCLEMENT_PENALTY` fired on the same trigger, ungated → gated
  `if not PC_OCTAGON_DMG`. **t=None footgun** guarded. **CI `_PINNED_OFF`** now pins `PC_OCTAGON_DMG=1`.
- **Tests strengthened:** T2/T4/T5 tested inputs/stamps not effects → now measure the actual effect; added
  face-model + reaction-reset regressions (6 green). Legacy `PC_OCTAGON_DMG=0` proven byte-identical 240/240
  vs parent. **All 4 bat.py goldens re-recorded under CORRECT envs** (the first cut recorded grid under a
  bare env — wrong digest; grid oracle needs full `_PINNED_OFF` incl `PC_NODE_COHESION=0`).
- **Gauge A/B:** mirror byte-identical; moved rows shift TOWARD bands (H2/H5/H6); no row more over-decisive;
  H3/H4 already 100%-decisive under both flags → octagon deepens the casualty exchange ratio (DG-6 caveat).
- Disclosure: `octagon_damage_model.md` adversarial-review addendum; geometry spec
  `perimeter_targeting_geometry_v1.md`; readiness synthesis `historical_fidelity_readiness.md`.

## 2026-07-23 — ED-MB-0018: octagon facing = damage-received multiplier + reaction delay + multi-side shock
- Jordan directive: "the facing octagon is a **damage-received multiplier** — attacks from behind do ~**2×**
  the damage of from the front; cells **cannot turn instantaneously** (needs a couple-tick reaction); attacked
  from **multiple sides** is **extra bad**, not just a divide-by-two." Replaces the legacy `-2`-dice octagon
  **pool** penalty (too weak — legacy rear was only 1.25× front, flank often 1.00× after `round()`).
- **(1) Arc = damage multiplier.** New `_octagon_dmg_mod` (orchestration.py) computes the pure per-cell
  facing arc — front GREEN **1.0×** / flank YELLOW **1.5×** / rear RED **2.0×** (`mult = 1 − arc·(RED−1)/2`),
  multiplying the **defender's** casualties; the pool/sigma angle-penalty is zeroed under the flag (no
  double-count). Reads the arc against the **LOCAL** attacker centroid (cells within `OCTAGON_LOCAL_REACH=2.0`)
  so a **wide** line's wing cell in a head-on clash stays GREEN instead of mis-reading the enemy centre as an
  oblique flank — verified **front→1.00×, rear→2.00× exactly per-seed**. Compounds with frontal-brace/charge-
  shock stripping → a braced front that parries to 0 is annihilated from behind (Cannae).
- **(2) Reaction delay.** A cell hit outside its front arc keeps its exposed facing until
  `FACING_REACTION_TICKS=2` elapse, and only refuses if it can **see** the threat (≤`FOV_HALF_DEG`=105°) and
  is not frontally **pinned**. A **rear** strike is in the blind arc → never perceived → the 2× persists the
  whole engagement (du Picq: reaction time under surprise).
- **(3) Multi-side shock.** `eng_counts≥2` → extra `×(1+MULTI_SIDE_SHOCK=0.5)` **compounding** (rank-relief
  collapse under encirclement) — worse than a halving.
- **Supersession (deliberate):** under `PC_OCTAGON_DMG=1` (**default ON**) the legacy wrapper/pocket/roll-up
  pool-penalty envelopment machinery goes dormant (wrap→rear arc 2×, pocket→multi-side shock; roll-up dropped,
  depth still tells via Lanchester). Legacy path preserved **verbatim** under `PC_OCTAGON_DMG=0`.
- **I4:** the multiplier runs on both grid+field paths (else field≠grid). Head-on single-subunit rows are
  all-GREEN→mult 1.0→byte-identical; the 3 flanking rows (envelop/cannae/oblique) move. **All 4 `bat.py`
  goldens re-recorded** (ED-909 re-baseline precedent). No constant tuned to the gauge (anchors are Jordan's
  stated design values).
- **Tests:** `tests/valoria/test_octagon_damage.py` (5) — 2.0× rear ratio, front never > rear (local-centroid
  fix), rear penalty persists across the reaction window, seen-flank stamps the reaction clock, multi-side
  shock present. Full `tests/valoria` green.
- **Disclosure:** `audit/2026-07-22-mass-battle-stress-test/octagon_damage_model.md`.
- **Follow-on:** graded ≥2/3/4-side escalation; full-campaign A/B of the default-ON flip once ED-MB-0016
  friction + the conjunctive-envelopment gate land (all three interact on the envelopment rows).

## 2026-07-22 — ED-MB-0017: multi-unit deployment geometry + envelopment pathing fix
- Jordan-flagged from the hierarchy snapshot (overlapping subunits; "double envelopment" with both wings
  on one side; refused flank level with the line). Root cause: `build_army` deployed subunit i at
  `col=15+i*4` (fixed step < subunit frontage).
- **Fix (P-1/P-2/P-3):** `_spec_span` + `_centered_line_cols` (frontage-aware, anchor-centred, provably
  non-overlapping 1–11 subunits, fit-to-field so over-wide armies degrade to overlap instead of crashing
  off-board); `build_envelopment` symmetric opposite-flank wings (mirror double envelopment);
  `build_refused_flank` echeloned-back refused wing.
- **Speed (P-4, Jordan):** envelopers must be fast or they arrive piecemeal. `PC_ENVELOP_SPEED_MULT=2.0`
  (envelop/sweep maneuver = rapid flanking march) + `PC_CAVALRY_SPEED_MULT` 2.0→3.0 (cavalry ~3× an
  infantry march). Measured infantry 1.0 / cavalry 3.0 / cavalry-envelop ~6.0 cells/tick → cavalry double
  envelopment wraps behind by ~t6–8 (was t16–20). Both inert for line-vs-line battles.
- **Adversarial critic (independent):** F1 over-wide-army crash FIXED (fit-to-field, 0/200 fuzz crashes) +
  F2 `gauge_mb.make_mixed_unit` same defect FIXED + F3 odd-wings tested + F4 refused-dynamic tested; F5/F7
  nits follow-on; F8 no-overlap verified sound by construction.
- **Machine-vision comparison:** `research/diagrams/mass_battle_formations/` (schematic vs sim tick-by-tick,
  rendered PNGs + sources).
- **Tests:** `tests/valoria/test_deployment_geometry.py` (16). **I4:** 7 single-subunit byte-exact rows
  unchanged; 3 multi-subunit rows re-baselined in every mode (ED-909 precedent); all 4 goldens re-recorded;
  byte-exact grid oracle green. **Still open:** horseshoe-not-ring (no cavalry rear-transit), single line
  (no triplex depth-lines), envelopment-not-rewarded outcome (DG-6 / ED-MB-0016). Full detail: ED-MB-0017.

## 2026-07-22 — ED-MB-0016: DG-6 grounded partial resolution — per-battle combat-effectiveness (CEV) friction
- Root cause of DG-6 over-decisiveness confirmed: melee pool sums N independent dice → CV self-averages
  ~1/√N → `compute_degree` deterministic from force ratio → 100%/0% vs historical bands. Fix (grounded in
  two research passes; `dg6_friction_resolution.md`): a per-battle, per-side CEV factor `M ~ LogNormal(0,
  σ²)` drawn ONCE per battle (`orchestration._draw_friction_cev`, lazy) multiplying the subunit combat
  pool (`core/exchange`). Law of total variance → scale-invariant outcome variance (Dupuy CEV / Clausewitz
  friction / stochastic-Lanchester). **σ=1.1 calibrated gauge-INDEPENDENTLY** to the Dupuy DLEDB force-
  ratio curve (57/62/70/82% at 1.2/1.5/2/3:1 vs targets 55/62/70/80). `config.PC_FRICTION_CEV`, **default
  OFF** (byte-exact / I4-safe).
- **Verified** (`test_friction_cev.py`, 7): inert-when-off; drawn once/battle not per-turn; large-force
  2:1 collapses ≥95% without friction, stays banded <90% with it (the fix); I1/I2 hold.
- **HONEST FINDING — necessary but NOT sufficient (ships OFF):** uniform friction moves the 20-row gauge
  6/20 → 4/20 — envelopment (H3/H4) stays ~100% (structural, needs a conjunctive gate) and friction
  BREAKS the Stage E brace repel (C2/C6 REPELLED→NOT-REPELLED). Complete DG-6 resolution = friction +
  conjunctive-envelopment gate + brace-repel preservation (follow-on; ED-MB-0016 needs_jordan). No
  constant tuned to the gauge. Full detail: `dg6_friction_resolution.md`.

## 2026-07-22 — ED-MB-0015: spatial-model v2 Stage F — verification + golden re-record + historical revalidation
- Full verification of Stages D+E (no new mechanics). **I1–I7 all hold**: I1 conservation 0 violations /
  300-battle field fuzz; I2/I6 stress-harness S5 (determinism PASS, mirror |skew|=0/48); I3 no live-path
  position integer; I4 byte-exact grid oracle green; I7 facing-away→0 reach. **Stress harness S0–S5 all
  green** (30 mechanics WIRED, 0 engine failures, all off-by-default gates SAFE). Lanchester exponent
  p=2.50 + depth-2 experiment byte-identical (preserved).
- **Field goldens re-recorded** (grid unchanged, I4): `unit_field 2da5183…` (`--check` verified),
  `cell_field 5f5db96…`.
- **P-DEC-4 historical revalidation** (`gauge_mb.py`, history-grounded bands): pre-D baseline (A–C) =
  **10/20**, v2 (A–E) = **6/20** multi — D+E moved the gauge down 4 rows (authorized re-baseline, but
  material). Dominant failure = **DG-6 over-decisiveness**; root cause confirmed: melee pool sums N
  independent dice → CV collapses ~1/√N (measured 0.89→0.06, N=4→1024) → `compute_degree` deterministic
  from force ratio → 100%/0% vs bands. Stage E win: C2/C6 (Cav vs BRACED) REPEL, matching history.
  Per Jordan directive 2026-07-22, the DG-6 grounded resolution (scale-invariant variance) is **underway**
  as a follow-on ED-MB. Full detail: `stage_F_verification.md` + ED-MB-0015.

## 2026-07-22 — ED-MB-0014: spatial-model v2 Stage E — weapon-class reach + pike troop type
- Stage E of `spatial_model_v2_plan.md` (Jordan P-DEC-1). The flat `REACH_SHORT=0.5` placeholder →
  per-troop-type **front-face reach** (`reach_for`/`TROOP_TYPE_REACH`): non-pole melee 0.1, pole/spear
  0.2, **pike 0.3**, cavalry/knights lance 0.2, ranged 0.1 melee sidearm (projectile band stays
  `VOLLEY_MAX_RANGE`). Feeds `cell_boxes_for → obb_front_reach_overlap` (contact) + `resolve_toi_and_commit`
  (TOI halt).
- **Authored the `pike` troop type** end-to-end: `TROOP_TYPE_STATS['pike']` mirrors heavy_infantry (reach
  0.3 the sole differentiator; provisional-by-analogy — §B.2 has no pike row), a `pike` weapon
  (pole/pierce/heavy, anti_cavalry) in `equipment.weapons`, `('pike','medium')` loadout, ShieldWall/Hold/
  Anvil roles.
- **Reach advantage — MEASURED (the gate):** emerges via the already-wired charge-recoil reach gate
  (`PC_RECOIL_CHARGER_GATE`). Braced pike (0.3) / spear-heavy (0.2) repel a cavalry lance (0.2) — defender
  keeps ~96.7% hp, cavalry recoils to ~88.3% — while braced levy (0.1 < 0.2) is run down (~90.7%). The
  anti-cavalry pike role, emergent from the reach data (before Stage E all reaches were 0.5, so the gate
  fired for everyone).
- **Disclosed finding:** reach differentiation does NOT change symmetric standing melee (pike-vs-levy
  standing == levy-vs-levy) — the exchange is mutual once contact fires; reach only shifts contact timing.
  Reach is a charge/brace lever here, not a standing-melee one. A directional-reach exchange term is a
  possible future increment (pike-pins-forever hazard under halt-on-contact) — flagged for Jordan, not
  introduced.
- **Tests:** `tests/valoria/test_reach_weapon_class.py` (10) — reach map, pike authored, reach-advantage
  emergence, standing-melee independence, I7 facing gate, ranged independence, I1×3 seeds + I2 with pike.
- **I4:** `reach_for` reaches the grid path only via the `'kite'` block; the byte-exact battery fields no
  kite units → grid oracle byte-exact green. **[DG-6, not tuned]** standing-melee A/B (Stage D→E)
  negligible (only rotated Arrowhead shifts). PP-290 meter-scale reconciliation flagged for Stage F. No
  balance constant tuned. Full detail: ED-MB-0014.

## 2026-07-22 — ED-MB-0013: spatial-model v2 Stage D — continuous frontage (last live integer removed)
- Stage D of `spatial_model_v2_plan.md`. The melee Lanchester frontage term `len(set(int_col))` (the
  only integer left on the live position/contact path, per `backwards_analysis.md`) → a **continuous
  OBB front-overlap width**. New `geometry.engaged_frontage(a_boxes, b_boxes, heading)` = the union
  length, along a side's frontage axis (⊥ facing), of each engaged cell body's width-interval clipped
  to the enemy's covered meeting span (pure float projection + interval merge; helpers
  `_project_interval`/`_merge_intervals`/`_interval_union_length`). `_find_contacts_standoff` threads
  `a_front`/`b_front` onto each contact pair; `_lanchester_strength` gains `front_width` that replaces
  the integer count when supplied.
- **Scoping:** the snapped `(rank,file)` cell identities are KEPT — they key the formation-lattice
  casualty/density/stamina substrate (`distribute_casualties`/`col_grid`/`_defender_depth`/
  `_fatigue_sigma`), a discrete troop-block identity (I3 defensible-quantization carve-out), NOT a
  live-position integer. Only the frontage MAGNITUDE moved to continuous.
- **I4:** grid/OFF pairs carry no `*_front` key → `orchestration` passes `p.get(...)=None` →
  `_lanchester_strength` falls back to the integer count byte-exact. **Byte-exact grid oracle green (30
  passed).**
- **Tests:** `tests/valoria/test_frontage_conservation.py` (15) — integer-limit reduction,
  fractional-on-offset, **depth-invariant** (depth-2 no longer collapses/inflates), **frontage-capped**
  (Lanchester stays linear), I1 conservation ×5 seeds, I2 determinism, grid-fallback byte-exact.
  maneuvers/movement/yield: 20 passed / 1 xpassed (pre-existing).
- **[DG-6 DISCLOSURE, not tuned]** A/B (12-seed field battery, stash vs current): axis-aligned symmetric
  meetings **byte-identical**; shift only on offset/rotated/width-asymmetric meetings — Line4-vs-Line2
  wide-attacker overkill softens (A_win 12→10/12, defender hp-retained .452→.487) as its frontage caps to
  the narrow defender's meeting width. Lanchester melee exponent **unchanged** (p=2.50 before/after — the
  pre-existing DG-6 pool-variance artifact is frontage-independent). Field goldens NOT re-recorded (Stage
  F, per plan §7). No balance constant tuned. Full detail: `audit/2026-07-22-mass-battle-stress-test/` +
  ED-MB-0013.

## 2026-07-22 — ED-MB-0012: spatial-model v2 Stage B+C — CIRCLE→OBB contact + collide-not-decelerate
- Stage B+C of `spatial_model_v2_plan.md` (Jordan "Euclidean motion, boxed footprint"). (1) **Analytic
  swept-SAT TOI**: replaced the parked scan+bisection (~200k SAT calls/battle, field path 20–60× slow)
  with a closed-form `_swept_first_overlap_s` — each ≤4 SAT axes is a linear-in-`s` overlap band,
  intersect, first-touch = left edge; O(4)/pair, ~15µs. Verified vs the bisection oracle to **1.7e-15
  over 700 seeded fuzzed pairs** (281 touches, 0 mismatches). (2) **Collide-not-decelerate correction**
  (Jordan in-session: "why decelerate instead of collide? / wouldn't that break charging?"). The plan
  made the TOI **halt** surface == the **contact** surface (reach box) — that DEADLOCKS: cells park on
  the `obb_front_reach_overlap` touch boundary where the strict contact predicate is False, so contact
  never fires (head-on Line-vs-Line froze at gap 1.5, 0 casualties). Fix: hard stop = **BODY vs BODY**
  (unit squares, reach 0); contact stays on the reach box (strictly outside the body), so contact fires
  as bodies close through the reach band. Bodies collide; weapons reach across the gap. Reach throttle
  retired (symmetric body-touch cap). **Charging restored** (`_momentum_speed` reads the pre-cap step;
  under the old reach-stop contact never fired so charge shock never triggered). Verified: head-on closes
  to body-touch and trades casualties; Fast cavalry charge reaches contact, deals more than it takes on
  impact (INF −21 vs CAV −10). Tests: `test_obb_contact_toi.py`(7)+`test_obb_primitive.py`(21)=28 passed;
  mass_battle/field subset 57 passed/0 failed. **I4 grid oracle byte-exact 2 passed** (code runs only
  under `if FIELD_MOVEMENT`, orchestration.py:1405). FIELD goldens re-recorded (`unit_field a73237df`,
  `cell_field 9d0b63b9`) — moves the DG-6-gated Cannae gauge (units that froze at range now engage),
  disclosed, no constant tuned. Departs from the plan's shared-surface premise → Stage C + R1 amended,
  flagged for merge-ratification. Full detail: `audit/2026-07-22-mass-battle-stress-test/` + ED-MB-0012.

## 2026-07-22 — ED-MB-0011: DG-10 field-movement freeze fix + field-based stress test (condensed)
- DG-10 (ED-MB-0007) fixed: `_node_advance` floored sub-Discipline-5 velocity to 0
  (`floor(1*0.7)=0`) → most §B.2 troop types (all disc<5) never closed on the live field path. The
  continuous-velocity accumulator meant to prevent it sat dead in the legacy grid `advance_cells`. Fix
  (Jordan-ruled "fields, not grids. no grids."): FIELD-path `step` is the real velocity (no floor, no
  accumulator; anchor/pos already float, consumer uses `min(step,mag)`); whole velocities stay int so
  disc≥5 is byte-exact, fractions advance at true rate. GRID path untouched (`if FIELD_MOVEMENT`) → CI
  byte-exact still 2 passed; FIELD goldens re-recorded (mirror/ranged byte-identical, 8 decisive rows
  move because units degrading below disc-5 mid-battle used to freeze). maneuvers+yield 12 passed/1
  xpassed. MOVEMENT-only; shifts the DG-6-gated Cannae gauge, no balance constant tuned. Full detail:
  `audit/2026-07-22-mass-battle-stress-test/` + ED-MB-0011.

