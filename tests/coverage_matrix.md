# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md

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

## 2026-07-02 — mass_battle: TOI refactor (archived — condensed)
- Jordan-directed replacement of Stage A/B's halving hack with exact time-of-impact collision solving
  (`resolve_toi_and_commit`) plus reach/facing-gated throttling; 5 real bugs found+fixed. G5 byte-exact
  both grid modes unchanged; mirror cav-vs-cav fully balanced (0-0-30). Full detail:
  `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle Stage D: role wiring (ED-907 L3) + Envelopment/Refused-Flank presets (archived — condensed)
- Wired the previously-inert `Subunit.role`; new `engine.build_envelopment`/`build_refused_flank`
  (ED-909 Unit-level presets, composed from existing primitives, zero new flanking mechanic). LC-8's
  literal shape retirement deliberately deferred pending Jordan sign-off (executed in the next entry).
  One real bug found+fixed (adversarial review): `orders` key not forwarded by `build_army`. G5
  byte-exact unchanged. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle LC-8: retire Horseshoe/RefusedFlank as Subunit.shape values (ED-909) (archived — condensed)
- Jordan-approved retirement: `Horseshoe`/`RefusedFlank` removed from `geometry.CELL_PATTERN_FN`/
  `config.MIN_DISCIPLINE`; only `Line`/`Arrowhead`/`GappedLine`/`Column` remain valid subunit-level
  shapes; envelopment/refused-flank now exist only as Unit-level `build_envelopment`/`build_refused_flank`
  compositions. `reset_positions` fixed (per-subunit own spawn column, was one shared shape anchor).
  `bat.py`/`gauge_mb.py` battery migrated + re-baselined, byte-exact verified. `tests/valoria`
  81 passed/10 skipped. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle workbench: multi-subunit preset dispatch + visualization battery (archived — condensed)
- Workbench extended to visualize real multi-subunit compositions (`army`/`envelopment`/
  `refused_flank` preset dispatch); a real frontend preset-dispatch bug found+fixed (stale-dropdown
  values silently overriding the actual multi-subunit preset). Two new symmetric multi-subunit-vs-
  multi-subunit presets (`M3`, `OBL`). Verified via Playwright across all 8 presets, both movement
  modes. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — three Jordan rulings executed: field default flip (ED-1089), subunit cap 11 (ED-1090), frontal recoil gate (ED-1091) (archived — condensed)
- ED-1089: `FIELD_MOVEMENT`/`PC_NODE_COHESION` defaults flipped 0→1 (field is now the default engine
  path); CI-gate `_PINNED_OFF` fix (env.pop→explicit pins) closed a real silent-regression risk.
  ED-1090: videogame subunit cap = 11 (`build_army`). ED-1091: frontal-only charge-recoil
  (`PC_RECOIL_FRONTAL`, "a brace cannot repel what it cannot face"). All grid digests byte-identical
  under pins. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — Stage E: Army Configuration Mode (deployment UI) (archived — condensed)
- Click-to-place deployment UI ("Deploy Army" tab, additive to Quick Match): `SUBUNIT_CAP` hoisted to
  module scope; new `/api/roster-options` endpoint (single source, no frontend drift); one shared
  canvas for placement + replay. Verified via Playwright (cap enforcement, role gating, LC-8 shape
  removal all correct). Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-02 — mass_battle: T1-T4 charge-recoil actor/timing/reach ruling (ED-1095) (archived — condensed)
- T1 actor-gate (recoil requires charger troop_type=='cavalry'); T2 brace-setup delay (≥1 tick before
  braced counts); T3 reach-gate (structural, TROOP_TYPE_REACH stays empty pending a separate ruling);
  T4 mounted-archer default kiting (`role='Kite'`). Byte-exact verified. Discovered but not fixed
  here: `envelop`/`sweep`/`wheel` only exist on the legacy grid path, unreachable on the default node
  path (led directly into the next entry's movement/pathing audit). Full detail:
  `tests/coverage_matrix_archive.md`.

## 2026-07-02 — Movement/pathing audit (ED-1096) fix plan execution (ED-MB-0001) (archived — condensed)
- Fable-led audit (ED-1096) + 8-step fix plan executed: node-path drift/reset-position corruption
  fixes, weapon-derived unit_type wiring (gate 2), lateral file-holding + WHEEL facing-stall fixes,
  the waypoint primitive (`_resolve_maneuver_goal`/`_envelop_goal`/`_sweep_goal`/`_kite_goal` —
  first real steering for envelop/sweep/kite on the live node/field path), and `PER_CELL`'s default
  flip to `'1'` (gate 4). A 5-dimension adversarial review found 6 more real defects, all fixed same
  session (kite never ported to the node path; an escort column-override regression; a test-fixture
  toggle leak; two minor dead-param/sentinel-semantics bugs; stale digest-provenance documentation).
  **Disclosed, not fixed:** enabling `PER_CELL`'s previously-inert combat mechanics made a two-subunit
  pinning-body-plus-detachment validator fixture rout before its detour could complete (a combat-pacing
  interaction, not a movement regression) — landed as a loud `xfail`, flagged for whoever next works
  PER_CELL=1 combat balance. All 4 `bat.py` digest modes re-recorded where genuinely changed (grid
  modes confirmed byte-exact where the change was node-path-only); `tests/valoria` 84 passed/10
  skipped/1 xfailed. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-04 — mass_battle: Cannae gauge audit (ED-MB-0002) ratified; DG-3/DG-4 implemented (archived — condensed)
- ED-MB-0002 ratified (PR #73 merge = ratification, ED-1094 convention). Two bug fixes landed first
  (validators.py ghost-cell construction; orchestration.py float-epsilon pool-floor). Root-cause audit
  (RC-1 through RC-5) found composition-coupling defects in the pool/morale accounting layer explained
  the H3-H6 Cannae-pattern gauge collapse, not the "two racing clocks" theory. Jordan ruled DG-3
  ("intensive, per-troop, bottom-up" pool -- combat pool per cell as per troop type/quality/density,
  not a flat subunit-level split) and DG-4 (per-subunit + whole-unit morale blend, wiring already-
  existing agg_morale/derive_rout/cascade_morale_hit machinery, no new state). Both implemented
  (new `pair_pool_contribution` in core/exchange.py; sibling-morale pull in core/state.py +
  hierarchy/units.py). All 4 `bat.py` digest modes re-recorded (shared, non-gated code). DG-5
  (racing-clocks) closed: a frozen-vs-wheeling-wings ablation showed byte-identical outcomes, refuting
  the theory outright. **Honest result: draws GONE (100%→resolves decisively) but H3-H6/C4 now
  OVERSHOOT their bands in the attacker's favor** instead of landing in them -- not a clean fix, a
  change in failure mode. `tests/valoria` green throughout. Full detail: `tests/coverage_matrix_archive.md`.

## 2026-07-05 — mass_battle: Cannae follow-up audit (ED-MB-0003) — 4 defects fixed, DG-1/DG-3 completed, DG-2 captured as workplan

A fresh Fable-5-led adversarial audit of the already-shipped DG-3/DG-4 fix (ED-MB-0002) found the
"RC-1 is fully fixed, remaining gap is pure DG-1/DG-2" story was **false** — 4 concrete engine defects
survived that fix, plus a harness composition bug. Jordan ruled the 3 open decision gates
(AskUserQuestion) the same session; all fixes + ratified decisions implemented, then independently
adversarially reviewed (2 more real bugs found+fixed in that pass).

**Defects found+fixed:**
- **D1** — `orchestration.py`'s `POOL_VARIANT=="C-ii"` branch applied an outer `a_troops_frac`
  (`troop_count/unit.total_troops()`) multiplier to `a_base` BEFORE `pair_pool_contribution`'s own
  internal per-troop normalization — double-diluting a composed subunit's pool by army-size share on
  top of its own troop density. **Fixed per Jordan's ratified "intensive" pool semantics: removed
  entirely** (still computed/used by the untouched `baseline` variant).
- **D2** — `hierarchy/units.py`'s `_envelop_goal` shared one threshold for its phase-1/phase-2
  transition (no hysteresis) — a wing wheeling to its rear waypoint immediately re-crossed the same
  threshold turning in, yanked back to phase 1, forever. **Fixed** with a one-shot `_envelop_committed`
  latch. A second, related bug (**D2b**) in `_node_advance`'s step formula could freeze a body forever
  within 0.5 combined units of ANY goal (a fixed step overshoots when close, and the old code took no
  action below that threshold) — **fixed** by capping the step at `min(step, mag)`.
- **D3** — `orchestration.py`'s `max(1, math.floor(a_pool_raw+1e-9))` floor resurrected a
  routed/broken atom's pool to 1, letting it keep dealing damage post-rout (§A.12 violation). First-pass
  fix (zeroing `a_pool`/`b_pool` for a dead atom) was **found to be a no-op by adversarial review** —
  `roll_pool`/`_sigma_net_boost` (resolution.py) both independently re-floor their own `pool` arg to a
  minimum of 1 internally, so the zeroed input never reached the actual dice math (confirmed by a
  revert-and-diff test: byte-identical digest with/without the first-pass fix). **Corrected fix** forces
  `a_net`/`b_net` to exactly 0 directly for a dead atom (both SIGMA_HEAD and legacy branches).
- **D4** — `percell.py`'s `distribute_casualties` tracked engaged columns as ONE union across a whole
  Unit, letting an uninvolved subunit (e.g. a wide-placed wing 20+ rows from any enemy) absorb a share
  of a DIFFERENT subunit's (the center's) casualties purely by column coincidence. **Fixed** — engagement
  now tracked per-subunit (`eng_by_sub`), with an `any_engaged` whole-unit fallback preserving the
  original degenerate-case semantics.
- **Harness composition bug** (not an engine defect) — `gauge_mb.py`'s `_envelop_army`/`_refused_army`
  fielded a FULL tier's troops per subunit via the legacy tier path, so a 3-subunit envelopment army
  silently fielded 3x (2x for `_refused_army`) its single-subunit opponent's troops — a side effect of
  the LC-8 migration, making every DG-1 composition question untestable. **Fixed**: both now take a
  `total_troops` param (default = the single-subunit baseline) split via the continuous-scale
  troops/concentration path.

**Jordan's rulings (AskUserQuestion, 2026-07-05), implemented:**
- **DG-3 completion = "Intensive (per-troop, partition-invariant)"** — see D1 above.
- **DG-1 = "symmetric at parity + majority pin cavalry wing so long as bottom-up emergent primitives
  approach"** — `_envelop_army`/`_refused_army` rebuilt at force parity (§ above); infantry rows
  (H3/H5/H6) keep the symmetric center+2-wings shape at parity (`pin_frac=1/3` default); cavalry rows
  (C4/C7) rebuilt as majority (2/3) infantry pin + minority cavalry wings via `wing_troop_type`/
  `pin_frac=2/3`, matching Polybius/Livy order of battle, built entirely from `engine.build_envelopment`
  unmodified.
- **DG-2 = "create as workplan"** — NOT implemented. Captured as
  `proposals/mass_battle_fighting_withdrawal_v1.md` (status PROPOSED): a per-subunit `yielding`
  state, facing preserved toward the enemy (unlike rout), commanded-entry first via a discipline-gated
  `'yield'` order, emergent auto-entry flagged default-off pending measurement, reuses `_kite_goal`'s
  reflect vector + the TOI/halt substrate + ED-MB-0001 §6's path-budget formula (NOT the audit's
  originally-proposed "recoil/knock-back idiom," confirmed to not exist as a displacement primitive).

**Adversarial-review pass (independent) — 2 real bugs found+fixed, rest checked out clean:**
1. D3's no-op (above).
2. `wing_speed`/`speed` kwargs in `_envelop_army`/`_refused_army` never reached `Unit.speed` —
   `Subunit` has no `speed` field at all (per-subunit `'speed'` spec keys were pure dead decoration,
   silently dropped by `build_army`), and the Unit-level `speed` was never forwarded to
   `build_envelopment`/`build_refused_flank`. Fixed: per-subunit `'speed'` keys removed (cleanup); real
   `speed=` now forwarded at the Unit level (the only granularity the engine's pursuit-check logic,
   `orchestration.py`'s `routing_unit.speed`/`victor.speed` checks, actually reads).
3. Everything else checked out clean (D2/D2b, D4, Step-4/5's arithmetic, all 4 digests independently
   re-verified).

**Verification:** all 4 `bat.py` digest modes re-recorded across the sequence of fixes (this touches
shared, non-gated combat-resolution code — same as ED-MB-0002's own landing); `unit`/`cell`/`unit_field`
stayed byte-identical through D2/D3(part 2)/D4 (this battery doesn't happen to exercise those bugs on
those 3 modes); only `cell_field` moved at each PER_CELL-gated step, plus `unit`+`cell`+`unit_field`+
`cell_field` ALL moved once at the Step-4 pool-semantics change (shared, non-gated code). `tests/valoria`:
88 passed, 16 skipped (all pre-existing `numpy`-unavailable skips, unrelated to this change), 1 xfailed
(`test_envelop_reaches_rear_node` — its xfail reason/docstring rewritten to retract the now-falsified
"steering mechanism proven correct" claim and record this session's findings).

**Honest gauge result (multi mode, n=30, final/corrected numbers):**

| Row | Before (ED-MB-0002 baseline) | After (this session) | Band | Verdict |
|---|---|---|---|---|
| H3 | 100% draws | 100/0/0 | 55-72 | WIN-OUT |
| H4 | 90% draws | 86.7/6.7/6.7 (val 92.9) | 45-62 | WIN-OUT |
| H5 | 100% draws | 83.3/0/16.7 (val 100) | 48-62 | WIN-OUT |
| H6 | 100% draws | 96.7/3.3/0 | 48-60 | WIN-OUT |
| C4 | 66.7% (val) | 100/0/0 | 75-95 | WIN-OUT |
| C7 | passing (100) | 100/0/0 | 65-100 | OK |

Draws are **entirely gone** — a real, dramatic change from the 100%-draw lock. But every row now
**overshoots decisively in the attacker's favor** instead of landing in-band (except C7, unaffected by
the composition change, which continues to pass). Full 20-row gauge aggregate: **4/20 → 5/20** passing
(H1,C1,C2,C6,C7 — C1 newly passes; every other previously-failing row, including RC-5's 9 untouched
single-subunit rows, remains failing, now mostly via the same overshoot signature rather than draws or
mixed results). **Not a clean net win or loss — a change in which rows fail and how.**

**New, unresolved finding (not decided, disclosed not chased):** a controlled experiment (co-located vs.
spatially-separated equal-troop subunit splits, both vs. an identical single-subunit opponent) suggests
why: `subunit_combat_pool`'s Command-driven score does not scale by a subunit's own troop share, so
multiple SPATIALLY-SEPARATED attacking fronts (center + 2 wings hitting one defender from different
angles) each roll close to a full, independent combat score at once, tempered only by a small
`ENCIRCLEMENT_PENALTY` tax that falls on the *defender*, not the attacker. Co-located splits stayed
roughly partition-invariant (13-16-1 vs a 14-16-0 mirror baseline); spatially-separated splits did not.
Whether this is a genuine partition-invariance defect or the historically-correct mechanism for why real
encirclements are devastating (bands needing reconsideration instead) is **explicitly left open** — a
new architecture question beyond DG-1/DG-3's scope, needing its own Jordan ruling, not a silent tweak.
**DG-5 correction:** the frozen-vs-wheeling ablation's "no race" null result is RE-CONFIRMED for a
DIFFERENT reason — both configurations' wings never reached contact at all (the now-fixed D2 bug), not
because there was genuinely no race.

Branch `claude/mass-battle-cannae-gauge-dg-rulings`. Next: Jordan's ruling on the partition-invariance
question and on DG-2's build sequencing (workplan doc §4).

## 2026-07-08 — mass_battle: partition-invariance fix (ED-MB-0004) + RC-5 preliminary finding

**Jordan's rulings (AskUserQuestion, 2026-07-08):** the partition-invariance question left open by
ED-MB-0003 = **"genuine defect — fix it"** (not the historically-correct-mechanism reading); DG-2
(fighting-withdrawal/yield) = **"build it now"**; RC-5 triage = **start now, in parallel**.

## 2026-07-01 — mass_battle workbench: tick-by-tick visualizer (server + frontend)
- ADDED tests/sim/mass_battle/workbench/{trace.py,server.py,static/index.html} (mirrors
  designs/scene/combat_engine_v1/workbench's pattern: a tiny stdlib HTTP server, no external deps, no
  build step). trace.run_traced_battle() runs ONE battle via engine.build_unit/resolve_battle (the
  wrapper contract, never reaches past it) with tracing on, returning the full 'tick'/'melee'/
  'volley'/'positions' event stream. server.py serves a canvas SPA with playback controls (scrub/play/
  step), a preset picker mirroring gauge_mb.py's named matchups, and per-tick HP/morale/rout/event-log
  panels. VERIFIED end-to-end live (not just imported): all 4 endpoints (GET /, /api/mode, /api/presets,
  POST /api/trace) tested via a running server instance in both PER_CELL=0 (grid) and
  FIELD_MOVEMENT=1 PC_NODE_COHESION=1 PER_CELL=1 (coordinate-field) modes.
- IMPORTANT (documented in server.py): PER_CELL/FIELD_MOVEMENT/PC_NODE_COHESION are read from
  os.environ once at import time and star-imported as independent copies into every consumer — a
  running server's mode is FIXED at process start (no live toggle); comparing grid vs field means two
  server instances. GET /api/mode reports the actual running config.
- FINDING from using the tool (not a bug): confirmed by reading _node_cells() (hierarchy/units.py) that
  the coordinate-field candidate keeps ROW positions integer-rank-snapped by design ("ranks are integer
  bins" — a real military structure) and only bins COLUMNS to their file; positions are not yet fully
  continuous floats end-to-end. Accurately reflected by the visualizer, not a rendering defect.
- Engine untouched by this addition (workbench/ only). G5 byte-exact both modes unchanged (unit
  7be8499b / cell 1c5b2851). Fabrication clean (HTTP status codes + dev port named+ledgered as
  non-sim-mechanical tooling constants, not fabricated citations). Co-file satisfied.

**Partition-invariance fix.** `subunit_combat_pool` is, by Jordan's own DG-3 characterization, a
per-atom COMBAT SCORE (Command + per-subunit discipline/cohesion/stamina), not a per-troop rate —
`pair_pool_contribution` correctly renormalizes when ONE atom is itself split across MULTIPLE enemies,
but does nothing when SEVERAL atoms of one side each independently, fully engage the SAME single
opposing atom (a pinning center + 2 wings all converging on one Line/Arrowhead defender — exactly
H3-H6/C4/C7's shape). Each converging atom got its own near-full `base_pool` with no reduction, so
splitting a fixed total force into more simultaneously-converging atoms multiplied total dice against
that one shared target, purely from the split — the mirror-image of the bug DG-3's "intensive" fix
already closed on the defender side. Confirmed by direct formula trace (no ablation needed): a fully-
engaged atom's `pair_pool_contribution` ≈ its own `base_pool` regardless of troop count, so N converging
atoms contribute ≈N×base_pool for identical total troops.

**Fix** (`core/exchange.py`'s new `_pair_engaged_troops` + `orchestration.py`'s new
`_convergence_scale`/`PC_CONVERGENCE_NORM`, default ON): groups pairs by shared target atom on each
side; for any group of ≥2, computes the troop-weighted-mean base score across the group and the group's
combined own-troop count, derives what ONE merged atom of that combined size would contribute, and
scales every member's own contribution down uniformly so the group's total is capped there. A group of
size 1 (the overwhelming majority of pairs — every single-subunit gauge row) is a no-op by construction
(skipped outright, scale 1.0 via dict-miss). Computed ONCE per tick on the FULL pairs list (before
`CASCADING_ENABLED`'s sub-phase split, which would otherwise fragment a convergence group across
separate `resolve_engagements` calls and under-correct it).

**Verified live, not just via digest motion:** a direct trace of an H3-style envelopment-army-vs-Line
battle confirmed `_convergence_scale` returns a non-trivial scale for 1446/1686 sampled ticks (max
simultaneous-convergence group size 3) — the mechanism genuinely engages this battery, this isn't inert
code. All 4 `bat.py` digests re-recorded (shared, non-gated combat-resolution code, same as every prior
DG-3/DG-4/Step-4 landing in this lane): `unit` 204d4d7…→444afdd4…, `cell` 84e606c…→cc13e17b…,
`unit_field` 79c1910…→4ab1b5a1…, `cell_field` c3de830…→ffe54c49… (full hashes in `bat.py`). `tests/valoria`:
112 passed / 57 skipped / 1 xfailed / 0 failed (7 pre-existing `test_names.py` failures confirmed
unrelated via `git stash` bisection — an environment/fixture issue, not caused by this change).

**Honest gauge result (multi mode, n=60):** the fix does **NOT** move H3/H4/H5/H6/C4's win/loss/draw
split at all — bit-for-bit identical `decA`/`dec_n` to the pre-fix baseline, even though exact per-trial
hp/turn/morale values changed (confirming the digest move is real but small relative to these rows'
dominant mechanism, envelopment/charge-shock morale collapse, not raw pool magnitude). Full 20-row gauge
unchanged at single=2/20, multi=6/20. **This is disclosed honestly, not oversold as a gauge-band fix** —
the partition-invariance defect was real and is now closed, but it was never the dominant lever for
H3-H6's overshoot; DG-1's composition and the still-live envelopment-shock magnitude remain the larger
levers there.

**RC-5 preliminary finding (diagnostic, not a fix):** a controlled A/B-slot-swap experiment on 3 of
RC-5's 9 single-subunit rows found a **slot/deployment-dependent asymmetry that does not track shape
superiority consistently**:

| Matchup | A wins / B wins / draws (n=30) |
|---|---|
| Arrowhead(A) vs Line(B) | 30/0/0 |
| Line(A) vs Arrowhead(B) | 29/1/0 |
| Line(A) vs Line(B) [mirror] | 17/13/0 |
| GappedLine(A) vs Line(B) | 22/8/0 |
| Line(A) vs GappedLine(B) | 2/28/0 |
| GappedLine(A) vs Arrowhead(B) | 11/19/0 |
| Arrowhead(A) vs GappedLine(B) | 2/28/0 |

Arrowhead-vs-Line flips to whichever shape occupies slot A (H2/H9's WIN-OUT in both directions is this,
not two independent shape effects); GappedLine-vs-Line favors GappedLine regardless of slot (a real,
slot-independent shape effect); GappedLine-vs-Arrowhead favors whichever shape occupies slot B. No single
rule (side bias, shape hierarchy) explains all three pairs — a true mirror (Line-Line, Arrowhead absent)
stays near-even (17/13), ruling out a blanket "slot A always wins" engine bug. The likely shared
ingredient across the inconsistent cases: `ANCHOR_MAP`'s per-shape deployment column (Line=9,
Arrowhead=8, GappedLine=7) is applied identically regardless of which side (A/B) carries that shape, so
two different-shaped sides deploy at two different absolute columns — a small (1-2 cell) lateral
deployment offset whose interaction with facing/approach geometry was not traced further this pass.
**Not root-caused to a specific mechanism** — flagged as the next concrete lead for whoever continues
RC-5's triage, not claimed as solved. RC-5's other 6 rows (H7, H8, R1, R3, C1, C3, C5) were not
investigated this pass.

**Verification:** `tests/valoria` full suite green (above); gauge_mb.py re-run both modes (numbers above);
`_convergence_scale` engagement traced directly (not inferred). Filed as ED-MB-0004 (resolves the open
"gauge triage continuation" item).

## 2026-07-08 — mass_battle: DG-2 fighting-withdrawal/yield mechanic, commanded-entry slice built

Jordan ruled DG-2 = **"build it now"**. Built exactly the proposal doc's (`proposals/
mass_battle_fighting_withdrawal_v1.md`) own §4 step 1, the "lowest-risk slice": **state +
commanded-entry only** — no emergent auto-entry (§2.2's second bullet), no "rally"/"pocket" exits
(§2.4, beyond the free "collapse to routed" which needed no new code). Disclosed, not silently
narrowed: whoever continues this should treat emergent-entry/rally/pocket as still open, not covered.

**Built:**
- `Subunit.yielding: bool = False` (new field, default-inert) + a `yield_active` property — the
  single shared gate every consumption site reads: `yielding and eff_discipline >= D_YIELD and
  unit_type != 'ranged'` (discipline-gated + melee-only, per §2.5's anti-abuse requirements; one
  property, not five repeated inline conditions, so the gate can't drift between call sites).
- `'yielding'` added to `_ORDER_SAFE_FIELDS` — a `'yield'` order (`Order('immediate',
  {'yielding': True})`) composes with the EXISTING Stage-C `Order`/`check_orders` machinery with
  zero new order-primitive code, exactly as the doc's §3 table says it should.
- Movement: new `Subunit._yield_goal` (reuses `_kite_goal`'s reflect-through-anchor flee vector,
  always active rather than standoff-band-gated) wired into `_resolve_maneuver_goal` behind
  `yield_active`; step magnitude capped at 1 cell/tick (§2.5's anti-abuse ceiling) at the same site
  `_node_advance` already computes its per-tick step. **Node/field path only** (`_resolve_maneuver_
  goal` is only called from `_node_advance`) — same scope boundary 'envelop'/'sweep' already have;
  the legacy grid `advance_cells` path has its own separate inline dispatch, untouched.
- Facing: a bespoke `yield_active`-gated override at BOTH `cell_facing_vec` write sites (node path
  and legacy grid path), firing **regardless of `PC_FACING_MODEL`** (which defaults OFF) — locks
  facing toward `target_atom`'s centroid even while the anchor moves away. This is the doc's
  "mechanically load-bearing" distinction from rout (which turns away); without this override a
  yielding body would inherit the default raw-movement-vector facing and point in its flee
  direction, reproducing rout's problem.
- Combat pool: `core/exchange.py`'s `subunit_combat_pool` multiplies by `YIELD_POOL_MULT` when
  `yield_active` — "traded ground at a cost", reduced but never zero.
- Anti-abuse: `orchestration.py`'s volley `fire()` refuses to fire for a `yield_active` atom
  (matches the existing 'kite' precedent — already redundant with the melee-only gate, kept for
  defence-in-depth).
- **Both new magnitudes explicitly flagged [CALIBRATED-DEBT]**, per the proposal doc's own §5 (not
  independently derived, reused from the nearest existing precedent, disclosed as such):
  `D_YIELD=3` reuses this file's own `disc_mult` tier break (disc≥5 full speed / disc≥3 0.7x / else
  0.4x — a subunit needs enough order to give ground at all, not the severely-degraded tier);
  `YIELD_POOL_MULT` reuses `PC_SHOCK_HOLD_BRACE` (0.35) verbatim, exactly as the doc's §5 suggested.

**Verification:** all 4 `bat.py` digests confirmed BYTE-IDENTICAL (no re-record needed — `yielding`
defaults False everywhere in the battery, so this is genuinely inert-by-default, not just claimed
to be). New `tests/valoria/test_mass_battle_yield.py` (9 tests): default-inert, discipline gate,
melee-only gate, `_yield_goal`'s flee-vector math, order-safety, pool malus (present/absent), and an
integration test running a real short battle confirming the yielding attacker actually moves AND its
facing vector keeps a non-negative dot product toward its target (stays roughly pointed at the enemy,
not away). Full `tests/valoria` suite: all green, no regressions (see this file's own 2026-07-08
entry above for the exact pass/skip/fail counts, unchanged by this addition).

**Honest measurement (§4 step 2's ask — center-yields-from-tick-0 vs no-yield, n=20, node path,
`build_envelopment` center+2-wings vs a single-subunit Line defender):**

| Configuration | Center hp retained (mean) | Battle turns (mean) | A wins / B wins / draws |
|---|---|---|---|
| No yield (baseline) | 35.8% | 15.65 | 14/0/6 |
| Center orders 'yield' from tick 0 | 40.6% | 16.5 | 0/19/1 |

The center DOES survive marginally better yielding (+4.8pp hp retained) — the mechanism works as
built. But ordering it to yield **unconditionally from the very first tick, for the whole battle**,
collapses the attacking army's win rate from 70% to essentially 0%: a permanently-backpedaling,
pool-discounted center contributes far less offense than the wings' encirclement gains back within
this scenario's timeframe. **This is not evidence the mechanic is broken** — it's the expected cost
of the crudest possible commanded-entry policy (always-on, no timing). Historically, Cannae's yield
was timed to buy exactly enough time for the wings to close, not sustained for the whole battle; this
session did not build or measure a timed/conditional entry (e.g. an `Order` with a `tick:N` trigger,
or an emergent entry keyed to encirclement progress) — flagged as the natural next experiment, not
attempted here. Reported honestly per the doc's own §4 step 2 instruction ("reported honestly
regardless of outcome"), not oversold as "DG-2 helps."

**Not built this pass (disclosed, matching the doc's own staged rollout):** emergent auto-entry
(§2.2), "rally" exit (§2.4's first bullet — morale-recovery-triggered reversion), "pocket" exit
(§2.4's third bullet — blocked-retreat malus removal). The "collapse to routed" exit needed no new
code (existing `derive_rout` fires regardless of `yielding`) and is therefore the only exit path
this build actually has.

## 2026-07-08 — mass_battle: pool abandons Command entirely (ED-MB-0006) — troop type/quality/numbers

Jordan directive (verbatim): "consider abandoning combat pools being related to the commander, and
instead being solely derived from the subunit troop type, quality and numbers." New
`POOL_QUALITY_MODEL` (default ON, `config.py`): base pool = `eff_power x eff_size x
POOL_QUALITY_SCALE` — `eff_power` is the troop-TYPE quality stat (`TROOP_TYPE_STATS`/§B.2, §A.1's
own "Power... determines dice rolled"), `eff_size` is NUMBERS (troops/BLOCK_SIZE, continuously
degrading with casualties), `POOL_QUALITY_SCALE=0.5` renormalizes the product to the historical
T3-baseline magnitude (~8, matching the old command=4/full-cohesion baseline). Discipline/stamina
penalties (`pen`/`stam_pen`) are unchanged. Command is absent from the pool entirely — it still
governs morale, formation-hold speed, order-issuing, and `derive_rout`'s Command-0 condition.
`COMMAND_SIGMA_ENABLED` branches remain selectable (`POOL_QUALITY_MODEL=0`) for A/B. Applied to
both `core/exchange.py:subunit_combat_pool` and `hierarchy/units.py:Unit.base_combat_pool` (the
pursuit/rout path) for consistency. Per Jordan's follow-up ("subunit power is the aggregate or
derivation of cell power"): `eff_power x eff_size` is already exactly that aggregate whenever a
subunit's cells share one troop type (true today — no per-cell troop_type exists yet); documented
as such rather than adding a redundant cell loop, since `pair_pool_contribution`/
`_pair_engaged_troops` already do the real per-cell redistribution for pair-scoped resolution and
will pick up true per-cell power the moment that data exists, no change needed there.

**Verification — all 4 `bat.py` digests re-recorded** (shared, non-gated code): `unit`
d9ca7c7e→444afdd4 is now `d9ca7c7e`, `cell`→`88481bbd`, `unit_field`→`40649feb`, `cell_field`→
`7b3b0a8d` (full hashes in `bat.py`). `tests/valoria`: 121 passed/57 skipped/1 xpassed/7 failed (6
pre-existing `test_names.py` + the expected digest-drift failure now fixed by the re-record) — see
`test_mass_battle_maneuvers.py`'s updated xfail note for the 1 xpass (unexpectedly passing once,
not re-verified across seeds, marker left in place).

**Gauge (multi, n=60): 6/20 → 7/20.** Newly passing: C4 (cavalry envelopment, WIN-OUT before,
now 83.3% — inside its 75-95 band), C5 (shaken-line exploit, now 95%, inside 65-98). Newly
failing/changed: **H4 (the actual Cannae matchup) flips from attacker WIN-OUT to attacker LOSING
badly** (1.7% A / 65% B / 33% draws, was 96.6% A before) — a genuinely mixed, not uniformly
positive, result: giving Size direct pool weight helps the SINGLE-large-subunit cavalry rows
(bigger force = bigger pool, working as intended) but hurts the multi-subunit envelopment-army
rows where the composed army's PER-ATOM numbers are now smaller than the single consolidated
defender's. H1/C1/C3 stay OK-band with mild reshuffled percentages. Single-mode stays 2/20
(structurally uninformative, unaffected).

**Honest, disclosed residual — `lanchester_signature.py`'s law-exponent check.** Melee should
conserve p≤1.4 (linear law); this was tested extensively before landing:
- The PRE-EXISTING Command-driven baseline (`POOL_QUALITY_MODEL=0`, i.e. what was in production
  before today) already **fails this exact check** (p≈1.55) — a previously-undetected gap,
  confirmed unrelated to this session (reproduces identically on the pre-session commit). The
  same baseline's `check_linear` (a 2:1 melee army should win decisively) ALSO fails today
  (big_win=3.0%, i.e. the bigger army loses 97% of the time) — flagged, not chased: a quick trace
  showed this specific check calls `run_battle` for a single 18-tick engagement, which usually
  ends in a draw at this troop ratio (mild ~10-15% casualties either way), so the 3%/97% split may
  be measuring decisive-outcome noise in a rarely-decisive sample rather than a structural defect;
  not confirmed either way, left for whoever next touches this test.
- Under the new model, `check_linear`'s win-rate check now correctly **PASSES** (100% big-army
  win, cas_diff +53.7) — the qualitative "bigger army should win" property is restored. But the
  stricter trajectory-fit exponent check gets WORSE (p≈2.50, not better) — swept extensively
  (sqrt-of-size variant: p≈2.35, barely moved; uniform pool-magnitude scale in
  {1, 0.5, 0.25, 0.2, 0.15, 0.1, 0.0625, 0.03}: plateaus at p≈1.65-1.7 below ~0.15, never reaching
  ≤1.4). Confirmed NOT a Lanchester double-count (disabling `LANCHESTER_ENABLED` entirely leaves
  the exponent completely unchanged at p=2.5) — the amplification is internal to the
  pool→net-successes→`compute_degree` tier→`DAMAGE_BY_DEGREE` pipeline: larger absolute pools have
  proportionally lower variance, so which discrete degree tier (Partial/Success/Overwhelming) each
  side lands in becomes near-deterministic from the pool ratio alone, and that tier assignment
  compounds the ratio rather than passing it through linearly. **Not silently patched** — a uniform
  scale provably cannot fix it (it doesn't change the win/loss ratio the test measures), and fixing
  it for real likely means revisiting `compute_degree`'s threshold logic or the degree/damage
  mapping, not the pool formula alone. Flagged as an open follow-up in `designs/provincial/
  mass_battle_v30.md`'s ED-MB-0006 note and here.

Filed as ED-MB-0006 (supersedes ED-899's Command-only base for the pool term).

## 2026-07-18 — audit-corpus relocation: provenance-comment path fixes only [no mechanical change]
- Repo-wide audit reorg moved `tests/audit/all_directions_ners_v27.md` to
  `audit/lane-a/all_directions_ners_v27.md` (see CLAUDE.md §3). Updated the stale `[canonical: tests/audit/...]`
  provenance comments citing that file in phase4_agi_dominance_2026-05-15.py, phase5_continuous_engine_2026-05-15.py,
  phase6_dominance_solvers_2026-05-15.py, phase7_action_triangle_2026-05-15.py, phase8_smart_ai_v2_2026-05-15.py —
  path text only, no formula/threshold/logic touched. Co-file satisfied (documentation-only trip).

## 2026-07-18b — adversarial-pass follow-up: two more stale path fixes [no mechanical change]
- mass_battle/engine.py comment + phase6_sim_verification_ledger.json `canonical_source` both still cited the
  pre-move `tests/audit/...` path; repointed to `audit/lane-*/...`. Path text only. Register near its 10k-token
  cap — trim to the archive file at the next real entry.
