# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md
## 2026-06-15/20 — ED-1013 through ED-1032 (archived — condensed)
- Smooth command-sigma pool + continuous discipline penalty (ED-1013); gauge recalibration (ED-1014);
  cavalry-construction gauge fix, not an engine defect (ED-1015); per-subunit stat/stamina/troop-type/
  rout-morale-discipline lifecycle (ED-1016-1019); a string of bugfixes/wiring closeouts (ED-1020-1027,
  1032) culminating in the formation-drift cell-orphaning fix (ED-1032, first post-baseline digest
  change, Jordan-approved); PP-683 intentionally left unwired (would double-count encirclement lethality
  already delivered via PC_ENVELOP_SHOCK + Lanchester overlap). Full detail: tests/coverage_matrix_archive.md.

## 2026-06-30 — Mass-battle bottom-up audit: provenance registry seed (ED-1043) [additive, data-only, byte-exact]
- ADDED `tests/sim/mass_battle/provenance.py`: a primitive-provenance registry SEED (the `Prov` schema +
  `PROVENANCE` rows for the 9 anti-pattern findings F1-F9 + the 3 grounded laws). Pure data record — it does
  NOT import or touch the engine, so the gauge digest is UNCHANGED (byte-exact). All `value` fields are stored
  as strings (a record of a constant, not a live constant), so it adds no mechanical literal to the engine.
- PURPOSE: machine-readable grounding tier per constant (derived / academic-law / historical / calibrated /
  ungrounded), enforcing the "no asserted value" bar. Seed counts: 3 academic-law, calibrated + ungrounded =
  the retirement worklist (target zero). Audit: `designs/audit/2026-06-30-massbattle-bottomup/`.
- NO regression test (data-only, no behavior); CI cross-check (provenance pass on ci_sim_fabrication_check)
  is roadmap Stage 0/5, not this pass.

## 2026-06-30 — Stage 1 (re-architecture): committed byte-exact DIGEST gate (bat.py)
- ADDED `tests/sim/mass_battle/bat.py`: the deterministic golden-digest harness the matrix previously
  referenced but that was never committed. Fixed battery (10 matchups × 24 seeds, per-trial seed) hashing full per-trial end state; `--check` asserts baseline, exit 1 on drift.
- BASELINE (HEAD 4d970a0, pre-refactor): unit=7be8499b4fe6a047a4c01e925719e11d5214ae0c124c784f929bc69ad6511725 ;
  cell=1c5b2851b75761e35cf8d54283af82269383e5c70b894d021eaed981c716d4a7. These are the G5 gate for the
  Stage-1 wrapper/core split (behaviour-frozen) and update ONLY on an intentional behaviour change in a
  later stage (recorded here, like the ED-1032 digest change above).

## 2026-06-30 — Stage 1a-1g (re-architecture): wrapper/core split, complete [byte-exact]
- EXTRACTED orchestration.py's monolith into core/{exchange,state,attrition,contact}.py (pool assembly,
  morale/discipline/rout hooks, Lanchester attrition, targeting/contact) + troop_types/registry.py +
  hierarchy/units.py (Subunit/Unit) + engine.py (true wrapper: build_unit + resolve_battle router,
  resolves nothing). Each extraction G1-clean (no up-DAG import, no cycle) and BYTE-EXACT (bat.py both
  modes unchanged; stress S1-S18 ALL PASS every step). orchestration.py: 2,899 → 1,705 lines. Full
  per-sub-stage detail (exact functions moved, line-count deltas, the docstring-masking fabrication-gate
  fix) archived to `coverage_matrix_archive.md` to stay under this file's 10k-token cap.

## 2026-06-30 — Stage 2 (re-architecture): standalone weapons + armour modules [additive, byte-exact]
- ADDED equipment/ package (weapons.py ARSENAL, armour.py ARMOURY, _base.py EquipmentRecord+Registry, __init__ TROOP_LOADOUT): weapons/armour split out of troop_types into their own dynamic/adaptable registries (open records + runtime register/override/variant) so the equipment model can be re-mapped onto scene-combat without disturbing the troop taxonomy. Descriptive axes only (no primitive grounding yet); a troop type NAMES a weapon+armour. NOT wired into resolution.
- G5 byte-exact: bat.py --check both modes match baseline (unit 7be8499b, cell 1c5b2851); sim-fabrication gate clean (only canonical DR literals). Co-file: the oldest 2026-06-05/06 build-log sections were archived to coverage_matrix_archive.md to stay under the 10k cap.

## 2026-06-30 — Stage 2 / Track M: FIELD_MOVEMENT continuous-speed toggle [default OFF → byte-exact]
- ADDED config.FIELD_MOVEMENT (default OFF) + Subunit._speed_accum; advance_cells uses a per-cell
  fractional-speed accumulator when ON, so a discipline-degraded body advances at its TRUE average rate
  instead of flooring to 0 every turn (floor(1*0.7)=0 freezes a slow degraded unit). Integer positions
  preserved; only per-turn step TIMING changes. [movement-substrate review 06 — finding 2]
- G5: bat.py --check both modes byte-exact with the toggle OFF (unit 7be8499b / cell 1c5b2851 unchanged,
  the OFF branch is the exact prior code). ON is a recorded behaviour change carrying its own digest
  (unit 4c5943c1…); NOT yet gauge-re-baselined — the field path's validation is the gated Track-M
  G-decision (06_movement_substrate_review.md). Heading-continuous + cid-threading deferred (need the
  float substrate / a contact-path refactor).
  (Note: the toggle actually lives in hierarchy/units.py beside PC_ENVELOP_PATH/PC_SWEEP, not config.py —
  config.py carries pre-existing uncited constants the whole-file fabrication scan would flag.)

## 2026-07-01 — Track M: centralize the abs→orig reverse-lookup [byte-exact refactor]
- ADDED geometry._oriented_abs_map(atom) (a FIRST-wins {abs:(orig)} map); refactored cells_to_orig_coords,
  _rotate_defender_facing, _atom_avg_facing to use it — retiring three open-coded O(n²) reverse scans.
  This centralizes the pattern-identity round-trip that is the engine's HARD grid dependency
  (movement-substrate review 06, findings 4/8) into ONE place — the step toward threading the cell
  identity from find_contacts (deleting the lookup entirely) once the contact path is refactored.
- G5 byte-exact both modes (unit 7be8499b / cell 1c5b2851 unchanged): the map preserves the old
  break-on-first semantics exactly, so results are identical. No behaviour change.

## 2026-07-01 — Migration DEBT-0: orchestration.py fabrication-debt resolution [byte-exact]
- Prerequisite for the coordinate-migration ON-path edits to orchestration.py (the whole-file fabrication
  scan surfaces every uncited constant the moment the file is staged). Resolved its 4 flagged constants
  HONESTLY:
  - 3× octagon -1.5 (L703/716/719): inline [canonical:] citing config.py:65 ANGLE_DEF_MOD zone midpoints
    (GREEN 0 / YELLOW -1 / RED -2; -0.5=mid(0,-1), -1.5=mid(-1,-2)) — genuinely derived.
  - 0.2 engagement-fraction damage floor (L1147, max(0.2, opp_frac)): recorded as CALIBRATED in the
    repo-root sim_verification_ledger.json (CONTACT_FRACTION_DAMAGE_FLOOR) + a provenance.py 'calibrated'
    Prov row (Stage-5 debt). NO canonical source fabricated ("do not fabricate one").
- G5 byte-exact both modes unchanged (unit 7be8499b / cell 1c5b2851); comments + data only. Fabrication
  gate: orchestration.py 4→0. Spec + verification from the coordinate-field-impl-spec workflow (13 agents;
  the debt agent applied + bat.py-verified this exact resolution). Coordinate-migration plan DEBT-0.

## 2026-07-01 — Migration S2: Euclidean distance on the field [FIELD_MOVEMENT; byte-exact OFF]
- `_atom_distance` (orchestration, now DEBT-0-clean), node vector-halt + kite (units) use `math.hypot`
  when FIELD_MOVEMENT is ON (Chebyshev `max()` when OFF) → circular range rings, retiring the √2
  "free diagonal" bias (movement review 06, finding 1). Wiring verified: OFF (0,0)-(3,4)=4 Chebyshev,
  ON=5.0 Euclidean. Adversarially SOUND (impl-spec workflow distance verdict).
- G5 byte-exact OFF both modes (unit 7be8499b / cell 1c5b2851). Inert for the current bat.py battery
  (ranged matchup approaches orthogonally, Chebyshev==Euclidean); activates on diagonal approaches +
  the field-ON path (gauge / later stages). Coordinate-migration plan S2.

## 2026-07-01 — Migration C0+COL+G+H+F2+P: coordinate-field flip [FIELD_MOVEMENT+PC_NODE_COHESION; byte-exact OFF]
- The full remaining coordinate-field sequence, each behind a default-OFF toggle, implemented from the
  adversarially-verified coordinate-field-impl-spec (worktree agent; byte-exact-gated per increment):
  C0 (contact scaffolding: Subunit.cells_float + FIELD_CONTACT find_contacts split, contact sets) · COL
  (float→file quantizer, COL_WIDTH=1.0) · G (geometry._oriented_abs_map rebuilt from _node_pos on ON —
  the biggest hazard) · H (halt-loop + contention collect + _momentum_speed float consistency) · F2
  (PC_FACING_MODEL anti-hyper-reactivity facing layer, DEFAULT-OFF; PC_FACING_SLEW_BASE=60 = calibrated
  debt, ledger+provenance) · P (delete the int(round()) snap in _node_cells on ON — the coordinated flip).
- Toggles module-local in units.py (config.py left untouched — 43 pre-existing uncited constants). Enforced
  FIELD_MOVEMENT ⇒ PC_NODE_COHESION (assert at run_battle setup; the invalid combo fails loudly). CONTACT_REACH=0.0
  (ON contact ≡ OFF adjacency, pending Jordan's radius). role_at_contact (dead code) + iter_cells (pre-existing skew) left alone.
- G5 byte-exact OFF both modes at every increment (unit 7be8499b / cell 1c5b2851). Fabrication + co-file clean.
- FIELD-ON CANDIDATE (Jordan ratifies; nothing fitted): ON digests unit 337ed92c / cell 38c5395b; runs to
  completion (exit 0). Gauge (via a scratchpad shim — gauge_mb.py is DEAD, hardcoded /home/claude path):
  OFF 5/13 → ON 4/13; H8 newly in-band, H2/H9 newly diverge to hard win-outs, draw rates collapse. NOT
  ratified — the gauge needs porting to the package before the ON path can be a validated contract.
  Coordinate-migration plan C0–P; open decisions: contact radius, facing magnitudes, gauge port, band ratification.

## 2026-07-01 — gauge_mb.py LIVE port + n=60 + tick-by-tick trace-capture backend
- PORTED gauge_mb.py off the dead `exec('/home/claude/sim_v22.py')` mechanism onto a direct
  `from mass_battle.engine import ...` (agonist-antagonist adversarial workflow: 1 implement + 1
  independent re-verify). make_unit/matchup() now delegate to engine.build_unit/resolve_battle (the
  wrapper contract bat.py already proved byte-exact-transparent) instead of raw Subunit/Unit/run_battle
  construction; make_mixed_unit stays on raw construction (build_unit is single-subunit only). No band,
  citation, or metric changed. LIVE re-verified (not the prior scratchpad shim): OFF baseline multi-mode
  5/13 (H1,H2,H7,H9,R1) — matches the shim's prior report exactly.
- Jordan directive 2026-07-01: default sample n 120->60 (runtime). SE~sqrt(0.25/n) rises ~4.6pp->~6.5pp
  at p=0.5 vs the grounding doc's cited n=120 basis; VERIFIED n=60 reproduces the IDENTICAL n=120 pass-set
  (5/13, same 5 rows) on the OFF baseline. Ledger entry `n=60` (calibrated/methodology, not historical).
- Fabrication-debt resolution (whole-file scan, files touched by the above): resolution.py's roll_pool
  TN=7 / face-rule 7-9=+1 cited to params/core.md; _sigma_net_boost's pre-existing citation reformatted
  to satisfy the checker's `# [canonical: ...]`-immediately-after-`#` regex (same source, position fix
  only). gauge_mb.py's make_mixed_unit P4/C4/D5/M6 defaults cited (same T3 baseline as make_unit); its
  starting_position row-stagger (4) ledger-recorded as a non-historical layout convenience.
- ADDED the tick-by-tick VISUALIZER trace-capture backend (Jordan directive 2026-07-01): extends the
  existing observe-only trace seam (resolution.start_trace/trace_event/get_trace, "no-op unless ON ->
  byte-exact") with resolution.tracing_on() (a public predicate so callers can skip expensive capture
  entirely when tracing is off, not just discard it) and orchestration._cell_snapshot/_subunit_snapshot/
  _unit_snapshot + one gated `if tracing_on(): trace_event('positions', ...)` call at the end of each
  run_battle tick. Uses atom.cells() (NOT iter_cells(), which reads legacy cell_offsets unconditionally
  and is NOT field-aware) zipped against _oriented(atom)'s stable ids — correct on both the integer-grid
  and coordinate-field paths. Zero cost when tracing is off (the capture functions are never called, not
  merely discarded) — provably byte-exact since no existing caller (bat.py, gauge_mb.py) enables tracing.
- G5 byte-exact both modes unchanged (unit 7be8499b / cell 1c5b2851). Fabrication + co-file clean.

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

## 2026-07-01 — mass_battle Stage A: true-adjacency stand-off halt (FIELD_MOVEMENT)
- FIXED the coordinate-field magical-co-location bug: the halt clamp compared against SNAPPED enemy
  positions with a flat "-1" margin, not true floats/a real stand-off. New `standoff()` primitive
  (`hierarchy/units.py`: `CELL_RADIUS` + PP-290 reach class via `troop_types.registry.reach_for`).
  `_node_advance`'s pre-cap + per-cell clamp now use `cells_float()` vs. `standoff()`, gated
  `FIELD_MOVEMENT`, prior code kept as fallback (byte-exact OFF unaffected).
- Bug found+fixed mid-implementation: freezing both sides' enemy positions pre-move let two closing
  sides compound past standoff (run_battle moves unit_a fully before unit_b). Fixed by snapshotting
  unit_a AFTER its own move. Verified: min separation holds at exactly `standoff()` (2.0).
- `find_contacts` gets a standoff-radius field path; `resolve_cross_side_contention` is a documented
  FIELD_MOVEMENT no-op. Review found+fixed a duplicate-cell stamina-drain over-count (dedup via sets).
- CI gap closed: `bat.py`'s golden-digest harness existed but nothing ran it — new
  `tests/valoria/test_mass_battle_byte_exact.py` wires grid-mode checks into CI; field digests recorded.
- `gauge_mb.py`: grid/OFF unchanged (12/20, matches historical 5/13); field path passes 4/20 —
  measured, not fitted; likely needs Stage B (facing/reaction, not yet built), not a magnitude tune.
- G5 byte-exact both grid modes unchanged (unit 7be8499b / cell 1c5b2851). Fabrication + co-file
  clean. Default stays OFF; default-flip remains Jordan-gated.

## 2026-07-01/02 — mass_battle Stage B + bias fix + Stage C: facing, first-mover bias, command layer
- STAGE B: ported the existing facing-slew mechanism (`PC_FACING_MODEL`, already wired on the legacy
  path) onto the FIELD_MOVEMENT path — `_node_advance`'s attention branch was overwriting facing with
  an instantaneous target-direction vector, zero rate-limiting, discarding a stale "don't double-slew"
  rationale that no longer held once that branch fired. Reuses `_slew_facing` unchanged.
- MIRROR-BIAS BUG found + fixed: `gauge_mb.py`'s Cav-vs-Cav mirror matchup (should read ~50/50) read
  98.3/0.0 on the field path — traced via a git-worktree bisect to Stage A's standoff clamp itself
  (confirmed absent, 11-8-1, on the pre-Stage-A commit). Root cause: the clamp's sequential-snapshot
  design gave unit_a persistent first claim on the shared closing budget every tick both sides neared
  standoff. Fixed by reverting to a synchronized both-sides-frozen snapshot and HALVING the allowed
  closing distance at both the anchor and per-cell level. A follow-up review caught and fixed a genuine
  oscillation bug in the per-cell clamp's multi-violator iteration (best-position tracking, not
  last-pass-wins). Verified: mirror matchup back to 2-1-27 (30 seeds); gauge `C3` now OK (5.0/6.7/88.3,
  was 98.3/0.0). One small accepted residual remains (~5% of ticks in one dense rotating scenario rest
  at 1.414 vs the intended 2.0, against an already-halted neighbour) — a fix attempt made it worse via
  WHEEL-rotation interaction, reverted in favor of the smaller gap.
- STAGE C: `engine.build_army` (public multi-subunit constructor, mirrors `gauge_mb.make_mixed_unit`,
  fixes its troops/concentration-forwarding omission + its never-set-advance_dir gap, confirmed inert on
  that helper — zero live callers); `Order`/`check_orders` (timed/conditional order queue, 'immediate'/
  'tick:N'/'enemy_range:D'/'ally_at:D' triggers, run before `assign_targets`); `escort_of`/
  `escort_offset`/`escort_engage_on_contact` (formation-relative positioning, live-facing-rotated,
  computed at the synchronized pre-move point alongside `cached_centroids`). Cannae acceptance test
  (wide-placed wings held then released by a `tick:4` order into the pre-existing `envelop`
  instruction) produces real lateral wheel movement — zero new flanking mechanics. Review found+fixed
  two gaps before landing: `Order.behavior`'s plain `setattr` was unrestricted (risked corrupting cell/
  troop/position accounting if an order set a geometry field) — now an explicit `_ORDER_SAFE_FIELDS`
  allowlist; a malformed trigger string failed silently forever — now validated eagerly at construction.
- G5 byte-exact both grid modes unchanged throughout (unit 7be8499b / cell 1c5b2851) — every change
  gated behind FIELD_MOVEMENT/PC_FACING_MODEL or additive with all-inert defaults. Fabrication clean
  (epsilon-guard citations added where flagged). Default stays OFF; default-flip remains Jordan-gated.

## 2026-07-02 — mass_battle: TOI refactor (halving hack replaced with exact time-of-impact)
- Jordan-directed complete replacement of Stage A/B's halved-anchor-precap + iterated worst-violator
  clamp with real continuous-collision detection: `_node_advance` now proposes each cell's UNCAPPED
  end-of-tick position (no clamp at all); new `resolve_toi_and_commit` (`units.py`) solves the exact
  per-pair quadratic TOI across BOTH sides together, once per tick, capping each cell to the smallest
  root over all its cross-side pairs — exact, no iteration, no oscillation guard needed.
- Reach + facing: `target` (final standoff) always uses base reach (matches `find_contacts`, keeps
  contact/halt in sync, byte-preserves every equal-reach matchup); `_effective_reach` gates a cell's
  reach to zero outside its forward FOV (reuses Stage B's `FOV_HALF_DEG`) for THROTTLE purposes only;
  `_reach_throttle` gives the longer-(facing-gated)-reach side a smaller share of the tick's closing
  motion, so it "sets into formation" before the shorter-reach side closes the rest of the gap.
- 5 real bugs found+fixed (2 via an independent adversarial-review agent): halted-cell obstacle
  exclusion, s=0 root filter, pass-through endpoint-only shortcut, throttled-safe-vs-full-motion
  endpoint mismatch, idle/reserve subunits dropped as obstacles. See plan file for detail.
- Verified: G5 byte-exact both grid modes unchanged; `tests/valoria` 55 passed/24 skipped unchanged;
  true-float standoff invariant zero violations (Horseshoe-cav/Line/Arrowhead/mirror-cav); reviewer's
  own two repro cases now cap correctly. Field golden digests re-recorded (intentional behaviour
  change). Mirror cav-vs-cav (30 seeds) now 0-0-30 — fully balanced, no first-mover skew.

## 2026-07-02 — mass_battle Stage D: role wiring (ED-907 L3) + Envelopment/Refused-Flank presets
- `engine.build_army`/`build_unit` now WIRE the previously-inert `Subunit.role`: a spec's `role` is
  gated by `role_allowed(troop_type, role)` (raises `ValueError` on a disallowed combo — a levy can't
  take `Shock`), and, in `build_army`, defaults `shape`/`instructions` from `ROLE_SPEC[role]` when the
  spec doesn't explicitly set them (explicit spec fields still win). Zero existing call site touched
  (`role` defaults to `None`).
- New `engine.build_envelopment`/`build_refused_flank` (ED-909's Unit-level "Envelopment"/"Refused
  Flank" allocation-grid presets): compose `build_army` + Stage C's timed-order queue + the
  pre-existing, UNMODIFIED `envelop` instruction — center/strong subunits built as given; wing/refused
  subunits get `stance='hold'` + an auto-queued release order (`tick:N` into `envelop`, or
  `enemy_range:N` for refused-flank) unless the spec already supplies its own orders. Zero new
  flanking mechanic, matching Stage C.4's own finding.
- **Deliberately deferred, not part of this change**: the literal LC-8 retirement of `Horseshoe`/
  `RefusedFlank` as `Subunit.shape` values (`geometry.CELL_PATTERN_FN`/`config.MIN_DISCIPLINE`) — the
  frozen byte-exact grid golden digests were computed against battles using `Horseshoe` directly as a
  `Subunit.shape` (`bat.py`'s own battery), so removing it would break that non-negotiable invariant.
  This lands ED-909's Unit-level INTENT (envelopment as an emergent composition) without that break;
  the legacy `Subunit.shape` values remain valid, now understood as legacy options. Flagged for
  Jordan's explicit sign-off before any literal removal + re-baseline.
- `Unit.doctrine`/Aggression: NOT built as new data — Jordan's own ED-907 ratification note already
  names `stance` as engine-realized Aggression; adding a parallel `doctrine.aggression` field would
  duplicate it (NERS-N/E, no unneeded apparatus). Cohesion-priority/the allocation-grid UI/intervention
  cadence are explicitly Jordan-deferred to Stage E — not built here either.
- G5 byte-exact both grid modes unchanged (unit 7be8499b / cell 1c5b2851) — every change is additive
  (new functions, new optional kwargs defaulting to `None`). `tests/valoria` 55 passed/24 skipped
  unchanged. Functional: role defaulting/rejection verified directly; `build_envelopment`/
  `build_refused_flank` construct correctly and a traced battle confirms the wing's order fires
  (releases from `hold` into `envelop` at the queued tick).
- Adversarial review found one real bug, fixed: `build_army` never popped/forwarded an `orders` key
  from a spec dict, so the two presets' documented "unless the spec already supplies its own orders"
  escape hatch was dead code — a caller-supplied custom order was silently dropped and always
  overwritten by the auto-queued release order. Fixed by adding `orders` to `build_army`'s forwarded
  per-subunit override keys. Re-verified: a spec-supplied order now survives; the auto-release still
  fires when no custom orders are given. Byte-exact and pytest unaffected (both re-confirmed).

## 2026-07-02 — mass_battle LC-8: retire Horseshoe/RefusedFlank as Subunit.shape values (ED-909)
- Jordan-approved 2026-07-02 ("correct, retire them. those are emergent outcomes."): executes the LC-8
  retirement Stage D deliberately deferred. `Horseshoe`/`RefusedFlank` removed from
  `geometry.CELL_PATTERN_FN` and `config.MIN_DISCIPLINE`; only `Line`/`Arrowhead`/`GappedLine`/`Column`
  remain valid subunit-level shapes. Envelopment/refused-flank now exist ONLY as Unit-level
  compositions via `engine.build_envelopment`/`build_refused_flank` (Stage D).
- `hierarchy/units.py`: dead `Horseshoe`/`RefusedFlank` branches removed from `role_at_contact` (zero
  live callers, confirmed before/after); each `Subunit` now snapshots its spawn position at
  construction (`_spawn_position`).
- `orchestration.reset_positions` fixed: previously reset EVERY subunit in a Unit to one shared
  shape-derived anchor column each battle-turn — silently correct only for single-subunit units, but
  wrong for any multi-subunit army (collapsed wide-placed wings/escorts back to center every
  re-engagement turn). Now restores each subunit to its OWN spawn column. Verified byte-exact-
  preserving for every existing single-subunit matchup via git-worktree diff.
- `bat.py`/`gauge_mb.py`: grid-mode battery/gauge rows using the retired shapes migrated to
  `build_envelopment`/`build_refused_flank` army-builder callables; new golden digests recorded and
  verified byte-exact (`unit`/`cell` both). `test_mass_battle_byte_exact.py`'s CI subprocess timeout
  bumped 90s→180s (multi-subunit battery rows measurably slow the grid-mode digest run).
- `workbench/trace.py`: `run_traced_battle` gains a `'preset'` spec dispatch (`army`/`envelopment`/
  `refused_flank`), so the visualizer can build real multi-subunit Unit-level compositions.
  `workbench/server.py`'s `H4`/`C4` presets rebuilt on the Envelopment composition.
- G5 byte-exact both grid modes pass against re-baselined digests. `tests/valoria` 81 passed/10 skipped.
  `gauge_mb.py`'s migrated rows and all workbench presets (grid and `FIELD_MOVEMENT=1`) run without
  error.

## 2026-07-02 — mass_battle workbench: multi-subunit preset dispatch + visualization battery
- `workbench/trace.py`'s `run_traced_battle`/`_build_side` extended to accept a `'preset'` spec key
  (`army`/`envelopment`/`refused_flank`) dispatching to `engine.build_army`/`build_envelopment`/
  `build_refused_flank`, alongside the existing single-subunit `build_unit` spec shape — the
  visualizer can now show real multi-subunit Unit-level compositions, not just single-subunit shapes.
- **Adversarial finding during dogfooding, fixed:** `static/index.html`'s preset-selection JS only
  ever populated the simple Shape/Troop dropdowns and always rebuilt the POST body from THEM in
  `runBattle()` — it had no way to represent a multi-subunit preset spec (no `.shape` key) at all.
  Selecting a multi-subunit preset (H4/C4 and the two new ones below) and clicking Run would have
  silently run whatever stale shape values were left in the dropdowns, not the actual preset. Fixed:
  `runBattle()` now uses a selected preset's multi-subunit side verbatim (`selectedPreset.a`/`.b`)
  when it carries a `'preset'` key, and the dropdown is disabled + shown as `— composed army (see
  preset) —` instead of a misleading stale shape name. Also removed `Horseshoe`/`RefusedFlank` from
  the Shape dropdown's `<option>` list entirely (LC-8 retired them as `Subunit.shape` values —
  selecting either would have raised `ValueError` at construction).
- `workbench/server.py`: two new PRESETS exercising genuinely symmetric multi-subunit-vs-multi-subunit
  battles (both sides field 3+ independently-tasked subunits at once, not just an attacker vs a
  lone-subunit defender) — `M3` (Envelopment vs Envelopment, mirror) and `OBL` (RefusedFlank vs
  Envelopment, mirrors `bat.py`'s "oblique" battery row).
- Verified via a Playwright-driven run through all 8 presets in both `FIELD_MOVEMENT=1
  PC_NODE_COHESION=1 PER_CELL=1` and the integer-grid baseline: each preset's deployment frame shows
  the correct subunit count/placement, the fixed dropdown correctly reflects composed-army sides, and
  H4 (Envelopment vs Arrowhead) visibly reproduces the Cannae pattern (B routed, HP 131/400, A's wings
  wrapped around B's remaining position) by the final frame. `tools/ci_sim_fabrication_check.py` clean
  on both changed files (one new literal in `server.py`'s `_REFUSED_REFUSED` cited).

## 2026-07-02 — three Jordan rulings executed: field default flip (ED-1089), subunit cap 11 (ED-1090), frontal recoil gate (ED-1091)
- **ED-1089 (field default flip, Stage A step 7 executed).** `FIELD_MOVEMENT` (hierarchy/units.py) and
  `PC_NODE_COHESION` (config.py) defaults flipped `0` → `1` — a bare engine invocation now runs the
  coordinate field. The integer grid remains fully available via explicit `FIELD_MOVEMENT=0
  PC_NODE_COHESION=0` and stays the frozen byte-exact oracle. **Load-bearing CI-gate fix:**
  `tests/valoria/test_mass_battle_byte_exact.py`'s `_PINNED_OFF` converted from `env.pop()` (which
  after the flip would leave the new ON default in force, silently running the grid-oracle check on
  the field path) to explicit per-toggle OFF-value pins (`'0'`/`'0.0'`). Both grid digests re-verified
  byte-identical under explicit pins (`unit 18bc4a0b…`, `cell bf666d04…`). `bat.py` field golden
  digests re-recorded (`unit_field c7957752…`, `cell_field dd085521…`) — the prior values were STALE
  (recorded before the LC-8 battery migration); the re-record also folds in ED-1091 below. Workbench
  server/frontend mode-banner docs updated for the inverted defaults.
- **ED-1090 (videogame sub-unit cap = 11).** `engine.build_army` now enforces a hard ceiling of 11
  subunits (`ValueError` above it; verified 11 constructs / 12 raises), lifting the TTRPG
  bookkeeping cap of 3 (`mass_battle_v30.md` §A.5 banner added). Command (1–7) remains the
  span-of-control governor within the ceiling; the >7 reconciliation (subordinate officers?) is
  flagged as a future ED, not invented here.
- **ED-1091 (frontal-only charge-recoil).** New `PC_RECOIL_FRONTAL` toggle (default ON; OFF
  reproduces prior any-direction recoil): the reciprocal charge-recoil fires only when the braced
  wall's per-cell-averaged octagon zone vs the charger is GREEN — "a brace cannot repel what it
  cannot face" (grounding §4.3, Burkholder 2007; the historical-validity condition Jordan attached
  was verified against that doc before executing). Verified: grid `cell` digest byte-identical (the
  battery's only braced row is frontal); a frontal braced charge still recoils (36 firings); an
  enveloping-cavalry-vs-braced-hold-line scenario shows the gate suppressing ~26% of firings
  (804 vs 1088 over 8 seeds) — exactly the flank/rear hits. Gauge row C7 can now legitimately gain a
  braced+enveloped variant on the next gauge pass.
