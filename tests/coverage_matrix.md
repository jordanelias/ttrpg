# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md
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

## 2026-07-02 — Stage E: Army Configuration Mode (deployment UI)
- `engine.py`: `SUBUNIT_CAP` (11, ED-1090) hoisted from a local inside `build_army` to module scope
  and exported via `_WRAPPER_API`, so any other caller — this UI, the future in-game deployment
  screen — reads the single source instead of duplicating the literal.
- `workbench/server.py`: new `GET /api/roster-options` endpoint exposing the live registries
  (`geometry.CELL_PATTERN_FN` keys, `troop_types.TROOP_TYPE_STATS` + the two generic legacy types,
  `roles_for` per troop type, `engine.SUBUNIT_CAP`) — the frontend never hardcodes a second copy of
  a shape/role list that would drift after a future LC-8-style retirement.
- `workbench/static/index.html`: new "Deploy Army" tab alongside the existing "Quick Match" tab
  (additive — Quick Match untouched). Click-to-place deployment: pick shape/troop_type/role
  (role-menu gated per troop type via `/api/roster-options`)/tier/troop-count, click the field (or
  "Place at default position") to add a subunit to the active side's roster; roster list with
  per-entry remove and a live cap counter (client-side cap enforcement mirrors `SUBUNIT_CAP=11`,
  with the server's own `ValueError` as the authoritative backstop). "Start Battle" assembles both
  rosters into the SAME `{'preset':'army','specs':[...]}` spec `trace._build_side` already
  dispatches to `engine.build_army` (zero new backend battle-running path) and hands off to the
  existing replay canvas/scrub/play controls — one rendering surface for both placement and replay,
  per the Stage E decomposition ("the same canvas in a placement state instead of a replay state").
- Verified via a Playwright-driven run: placed 3 heavy_infantry (Line) for side A and 2 cavalry
  (role=Shock) for side B by canvas click, confirmed `Horseshoe` is absent from the shape options
  (LC-8) and `Shock` appears in cavalry's role menu but not e.g. artillery's, started the battle
  (112 replay frames produced, winner determined), confirmed switching back to the Deploy tab
  restores the placement schematic rather than staying on the replay, and confirmed the cap: adding
  an 11th side-A subunit succeeds, a 12th is blocked client-side with the ED-1090-citing alert
  matching the server's own message text.

## 2026-07-02 — mass_battle: T1-T4 charge-recoil actor/timing/reach ruling (ED-1095)
- **T1 (actor-gate).** New `PC_RECOIL_CHARGER_GATE` (config.py, default ON): the reciprocal
  charge-recoil (`PC_CHARGE_RECOIL`) now additionally requires the charging atom's
  `troop_type == 'cavalry'` literally — a defender no longer recoils a charger just for having
  marginally higher per-tick momentum than a braced wall. `mounted_archers` explicitly excluded
  (see T4 — they should never be closing to melee at all).
- **T2 (brace-setup delay).** New `PC_BRACE_SETUP_DELAY` (config.py, default ON) +
  `Subunit._brace_since_tick` (hierarchy/units.py: stamped `0` at construction for a subunit
  deployed already braced; stamped to the firing tick by `core/contact.check_orders` when an
  `Order` adds `'brace'` mid-battle; reset to `-1` on removal). `resolution._subunit_braced`/
  `_unit_braced` are now `t`-parameterized (`t=None` preserves the old instantaneous check) and
  require ≥1 full tick of continuous brace before treating a subunit as braced, for either the
  charge-shock defensive benefit or the reciprocal recoil. `t` threaded through
  `resolve_engagements`/`resolve_engagements_cascading`/`run_battle`'s call site.
- **T3 (reach-gate, structural only).** `PC_RECOIL_CHARGER_GATE` additionally requires the
  defender's `reach_for(troop_type) >= ` the charger's (`troop_types.registry.reach_for`, the
  existing Stage-A primitive) — a charger with genuinely longer reach can strike a wall whose
  weapons can't reach back, so the wall can't retaliate. `TROOP_TYPE_REACH` stays deliberately
  empty (everyone defaults `REACH_SHORT`), so this half is a no-op today pending a separate
  troop-type-to-reach-class ruling — not populated speculatively.
- **T4 (mounted-archer default kiting).** `engine.build_army`: a spec with
  `troop_type == 'mounted_archers'` and no explicit role/shape/instructions implicitly defaults
  `role='Kite'` instead of silently closing to melee. Any explicit caller choice of role, shape,
  or instructions always wins over this default. `build_unit` unchanged (no "unspecified shape"
  case exists there — its `shape` parameter is a required positional).
- Verified: `bat.py --check` byte-exact across all 4 digest modes (`unit`/`cell`/`unit_field`/
  `cell_field`) against the frozen baselines; `tests/valoria` pytest suite 81 passed, 10 skipped.
- **Also discovered, NOT fixed here (flagged in HANDOFF.md):** the `'envelop'`/`'sweep'`
  instructions and the overhang `'wheel'` maneuver (`hierarchy/units.py` `advance_cells`
  ~L802-861) are gated `if PER_CELL and ...` and only exist on the legacy grid path —
  `_node_advance` (the coordinate-field path, DEFAULT since ED-1089) has no equivalent steering at
  all, so every subunit currently just walks a straight line toward the enemy centroid on the path
  actually used by default. Under investigation.

## 2026-07-02 — Movement/pathing audit (ED-1096) fix plan execution, in progress (ED-1097)
Fable-led audit (ED-1096) confirmed the root cause flagged above and 10 further findings; Jordan
answered all 4 decision gates, deferring gates 1 (Command/Discipline-gated conditional tactics) and
3 (facing/attention split) until envelopment/pincer/wheeling pathing is confirmed working. This
entry covers the fix-plan steps landed so far (steps 1, 2, 4, 5, 6 of 8 + decision gate 2; gate 4
and step 7, the waypoint primitive itself, still pending):
- **Step 1 — `check_drift` node-state fix.** ED-1032's re-key on formation drift only ever covered
  `cell_troops`; node-path position state (`_node_pos`/`_node_rel`) was never included, so a drift
  left the old shape's ids behind and cells teleported to `(0,0)` or stacked on the anchor. New
  `Subunit._rekey_node_state(new_ids)` rebuilds node state for the new pattern around the CURRENT
  live anchor (not spawn) — the subunit reorganizes in place. Gated `PC_NODE_COHESION and
  hasattr(a, '_node_pos')`; legacy path untouched.
- **Step 2 — `reset_positions` node-state no-op (minimal form).** `reset_positions` wrote only the
  legacy grid fields, inert on the node path but a stale-data landmine for future code reading
  `starting_position`. Node-path atoms are now explicitly skipped — position genuinely does not
  reset between engagement turns within a battle (Jordan: "nonsensical for them to return to
  starting positions within the same battle"). The full Command-gated conditional-tactics layer
  (decision gate 1) is deferred; this step only stops the corruption.
- **Decision gate 2 — weapon-derived `unit_type`.** `unit_type` now derives from the troop's
  assigned weapon (`mass_battle.equipment.TROOP_LOADOUT`/`loadout_for`, previously unwired) via new
  `troop_types.registry.unit_type_for`, wired into `build_unit`/`build_army` (unmapped types still
  resolve `'melee'`, byte-exact for every existing call site). Corrects ED-1095/T4: a
  `mounted_archers` spec got `role='Kite'` but no `unit_type`, so it neither kited nor volleyed on
  any path. Added a `mounted_archers` entry to `TROOP_LOADOUT` (bow/light). `kite`'s STEERING gate
  no longer requires `unit_type=='ranged'` (Jordan: kite is weapon-independent, best with a bow but
  executable by lance cavalry) — only volley fire itself still requires ranged; the far edge of the
  kite band uses `reach_for(troop_type)` for a melee kiter instead of inventing a new magnitude.
- **Step 4 — lateral file-holding in `_node_advance` (v12 port).** `_node_advance` was a pure
  centroid attractor — every subunit's column steered at the SAME enemy-centroid column, collapsing
  wide-placed wings inward before any maneuver began. A subunit that is one of several siblings in
  a multi-subunit Unit now holds its own deployment file (`_spawn_position`'s column) while its row
  still closes on the enemy; a solo subunit is unchanged. Confirmed via an H4-composition trace:
  wings now hold within ~1-2 columns of their spawn file across the approach, versus collapsing
  from cols 3/17 to ~9.6/13.0 before this fix.
- **Step 5 — node WHEEL 180-degree facing stall.** The facing update was a lerp-normalize that
  degenerates to the zero vector at an exact 180-degree reversal (full discipline), freezing the
  formation's facing forever — exactly the case a wheel-to-rear maneuver needs. Replaced with a
  rotation-based update (same disc-gated rate `kw`, applied as an angular fraction instead of a
  linear vector blend) with a deterministic tie-break at the boundary. Confirmed: a full-discipline
  subunit facing south, target flipped to due north, now smoothly rotates instead of freezing.
- **Step 6 — maneuver acceptance validators re-pointed at the node path.** `validators.py`'s
  `Run:` line only ever pinned `PER_CELL`, leaving `FIELD_MOVEMENT`/`PC_NODE_COHESION` at the
  ambient (node, since ED-1089) default — so V-ENVELOP/V-SWEEP silently measured the dead legacy
  arm whenever anyone actually pinned toggles to make them pass, and measured nothing meaningful
  otherwise. New `validators._set_movement_path('grid'|'node')` + a `path` parameter on
  `v_envelop`/`v_sweep`/`_envelop_reach`/`_sweep_disp`. New
  `tests/valoria/test_mass_battle_maneuvers.py`: grid-path tests are real regression tests (green,
  the mechanism still works there); node-path tests are `xfail(strict=True)` acceptance targets —
  expected red until step 7 lands, and `strict=True` means an unexpected pass is itself a failure,
  so this cannot silently rot into permanent xfail once the fix ships.
- Verified throughout: `bat.py --check` byte-exact across all 4 digest modes unchanged after every
  step; `tests/valoria` pytest suite 81 passed/10 skipped unchanged (plus the 2 new grid-regression
  tests passing and 2 new node-acceptance tests correctly xfailing). Field digests (`unit_field`/
  `cell_field`) intentionally drift as real node-path bugs are fixed — re-record deferred to a
  single batched pass once the remaining steps (waypoint primitive, `PER_CELL` default flip) land.
- **Step 7 — waypoint primitive (`_resolve_maneuver_goal`/`_envelop_goal`/`_sweep_goal`).** Gives
  `_node_advance` a per-tick anchor-level goal (modeled on the legacy per-cell two-state machine)
  when `envelop`/`sweep` is active, gated behind the same `PC_ENVELOP_PATH`/`PC_SWEEP` toggles the
  legacy path uses. Two bugs found/fixed during verification: a missing toggle-gate made ON/OFF
  measure identical behavior; the ported `past`-the-flank predicate was too shallow at anchor
  granularity (fixed by requiring the anchor to reach `rear_r` itself, reusing the existing ±2
  margin constant, not a new magnitude). `validators.py`'s `v_envelop`/`v_sweep` were also missing
  `seeds`/`turns` forwarding, which had been silently masking the fix behind an absorbed `TypeError`
  inside `xfail` — found by re-verifying the mechanism directly instead of trusting "still xfailed."
  Both node tests now pass for real (no longer `xfail`); grid arm unaffected; full suite 81
  passed/10 skipped/0 xfailed.
- **Decision gate 4 — `PER_CELL` default flip to `'1'`.** `config.py:86` default `'0'`→`'1'`, same
  ED-1089 precedent (grid oracle = explicit pin, already the case in `bat.py`/
  `test_mass_battle_byte_exact.py`, so no CI-pin gap). Found and fixed two independently-defaulted
  `os.environ.get('PER_CELL','0')` re-derivations that had drifted out of sync with the new config
  default: `bat.py`'s `compute()` mode-key and `gauge_mb.py`'s cavalry-row gate both mislabeled/
  misgated a bare invocation — fixed by reading the resolved `hierarchy.units.PER_CELL`/
  `config.PER_CELL` instead of re-deriving. Grid digests (`unit`/`cell`) reconfirmed byte-exact;
  field digests (`unit_field`/`cell_field`) diverge from their recorded golden values, but
  identically whether `PER_CELL` is 0 or 1 — confirmed attributable to step 7's intentional
  behavior change, not the gate-4 flip itself (re-record still pending, folded into task #77).
- **Gate-4 finding, disclosed not fixed:** enabling `PER_CELL`'s previously-fully-inert combat
  mechanics (fatigue drain, envelopment-sigma, charge shock) made `test_envelop_reaches_rear_node`
  flip from a reliable pass to a reliable fail — diagnosed as a combat-PACING interaction, not a
  movement regression: the two-subunit "pinning main body + wide-detour detachment" validator
  fixture's main body now frequently routs (~7/8 seeds) around turn 44-56, before the detachment's
  real-physics-timed detour can complete, where the old (PER_CELL=0) combat model never routed
  either side within the 60-turn cap. Confirmed non-movement via: (1) forcing
  `orchestration.PER_CELL=False` alone restores the pass with every other change unchanged; (2) an
  isolated single-subunit fight at the same troop ratio favors the attacker 14-0-6/20 seeds, so the
  defender profile alone isn't favored — it's specific to this two-subunit timing; (3) varying the
  detachment's travel distance barely moved the outcome. Not fixed by retuning `_envelop_goal`
  (band-fitting) or by fixture troop-count tuning (tried, unreliable). Landed as a loud, documented
  `xfail(strict=False)` on `test_envelop_reaches_rear_node` — the underlying combat-balance/pacing
  question (numerically-dominant vs. thin-and-yielding pinning force; a maneuver time-budget
  separate from the frontal fight's own clock) is flagged for whoever next works PER_CELL=1 combat
  balance, out of this movement/pathing fix's scope.
- **Remaining, not yet done:** step 8 (lower-severity hardening, parallelizable); the batched
  field-digest/gauge re-baseline (task #77); an adversarial review pass over steps 1-7 + gate 4
  before landing; re-producing the Cannae visualization to confirm the fix end-to-end.
