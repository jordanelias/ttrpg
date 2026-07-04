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

## 2026-07-02 — Movement/pathing audit (ED-1096) fix plan execution, in progress (ED-MB-0001)
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
  Both node tests now pass for real (no longer `xfail`); grid arm unaffected; full suite 85
  passed/10 skipped/0 xfailed (the 81-baseline + these 4 maneuver tests, all now passing;
  [2026-07-02 adversarial-review correction] an earlier version of this line stale-copied the
  pre-session 81 baseline itself as if it were the new total — verified by checking out this
  step's own commit and re-running the suite).
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
- **Task #77 full verification.** Field digests re-recorded (`unit_field b1963d03.../cell_field
  1f0742c5...`). [2026-07-02 adversarial-review correction] An earlier version of this entry claimed
  the change was "isolated to step 7" — WRONG, per a direct worktree bisection (see `bat.py`'s
  EXPECTED-dict comment for the full commit-by-commit digest trail): steps 1, 4, 5, AND 7 each
  independently changed `unit_field`, not step 7 alone. The one claim that DOES hold: gate 4's
  `PER_CELL` default flip contributes zero ADDITIONAL divergence on top of those four steps, since
  this measurement pins `PER_CELL='0'` explicitly and cannot be reached by that flip. All 4 digest
  modes re-confirmed byte-exact against
  their (2 unchanged, 2 re-recorded) baselines. Functional probe via `workbench/trace.py`
  (default toggles, no validator-forced overrides): a `build_envelopment` wing tracked tick-by-tick
  wheeled from its start (row 36, col 21) to row 14.4, col 32.8 — genuinely wrapping past and behind
  the defender (col ~20.6), not walking a straight line; `sweep` similarly displaced its subunit
  laterally (col 10.0→8.0) toward the flank. Both confirm step 7's mechanism works in a real,
  default-toggle multi-subunit battle, not just the validator harness.
  `gauge_mb.py` re-run under the new PER_CELL=1 default (per gate 4's own text): single=2/20,
  multi=4/20 (H1, C7, C2, C6 pass). Confirms the SAME interaction already diagnosed and disclosed
  above at battle-composition scale: H3/H4(Cannae)/H5/H6 — the actual historical Envelopment/
  RefusedFlank matchups — lose 0-13% instead of the expected 45-72% band, consistent with an
  envelopment composition's pinning center routing before its wings complete their maneuver.
  Recorded, not chased — per this session's (and this repo's) standing discipline against
  retuning magnitudes to fit a band; the underlying combat-balance/pacing question is the same
  open follow-up flagged in the gate-4 finding above, not a new one.
- **Task #79 adversarial review (5-dimension Workflow, sonnet finders + opus verify) — 6
  CONFIRMED findings, all fixed same session, not deferred:**
  1. **Kite never ported to the node path (critical).** Step 7 built `_envelop_goal`/`_sweep_goal`
     but no `_kite_goal` — a mounted_archers subunit (gate 2 correctly gives it
     `instructions=('kite',...)`) fell through to plain centroid steering and closed to melee on
     the live default path, the exact bug class this audit exists to fix, for a 4th instruction
     the first pass missed. Fixed: new `Subunit._kite_goal` wired into `_resolve_maneuver_goal`,
     reusing `PC_KITE_STANDOFF`/`VOLLEY_MAX_RANGE`/`reach_for` verbatim (no new magnitude), matching
     the legacy block's exact toward/away/in-band semantics. Verified: a mounted_archers subunit
     now holds standoff distance 6.5-8.3 against a Line (inside the [5,8] band) instead of closing
     to melee.
  2. **Escort column-override (moderate).** Step 4's sibling-column-holding fallback overrode
     ANY escort's live-tracking column with its fixed spawn file the instant the escorted unit's
     column diverged (e.g. on envelop/sweep/wheel) — defeating Stage C's own escort machinery.
     Fixed: `escort_of is not None` checked before the sibling-count branch.
  3. **Test fixture leak (moderate).** `_movement_toggles`'s save/restore omitted
     `PC_ENVELOP_PATH`/`PC_SWEEP`, contradicting its own docstring — latent today (no other
     in-process test consumes it yet) but real. Fixed: added to the saved/restored set.
  4. **`_rekey_node_state`'s dead `new_ids` param (minor, PLAUSIBLE not CONFIRMED — harmless today,
     fixed anyway).** Never read; silently re-derived from `_oriented(self)`. Fixed: now asserts
     `new_ids` matches, converting a silent future trap into a loud failure.
  5. **`build_army`'s `unit_type=None` sentinel (minor, latent).** `sp.pop('unit_type',
     unit_type_for(tt))` only derives when the key is ABSENT, unlike `build_unit`'s `if unit_type
     is None: derive`. Fixed to match `build_unit`'s semantics.
  6. **Documentation provenance (moderate+minor).** `bat.py`'s "step 7 alone" digest-provenance
     claim and this file's "isolated to step 7"/"81 passed" lines were factually wrong (direct
     bisection: steps 1/4/5/7 all independently changed the digest; true count was 85 not 81) —
     corrected above and in `bat.py`.
  One REFUTED (bat.py battery has no weapon-mapped-troop_type regression coverage — real gap, not
  a concrete defect per the review's own bar; not fixed, flagged as a future coverage item, not
  silently dropped). All 4 digest modes byte-exact after every fix (kite/escort fixes are provably
  inert against the existing battery — neither a kite-instructed nor an escort_of subunit exists in
  it); full suite 84 passed/10 skipped/1 xfailed unchanged.
- **Remaining, not yet done:** step 8 (lower-severity hardening, parallelizable); re-producing the
  Cannae visualization to confirm the fix end-to-end — done (task #78, delivered as an Artifact).

## 2026-07-04 — mass_battle: Cannae gauge audit (ED-MB-0002) ratified; DG-3/DG-4 implemented
- **ED-MB-0002 ratified** (PR #73 merge = ratification, ED-1094 convention); DG-3/DG-4 ruled by Jordan
  same day in chat, recorded as an addendum in `designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/
  README.md` (PR #75). Two independent bug fixes landed first: `validators.py`'s `_attacker_envelop`
  ghost-cell construction bug (`starting_position` assigned after `__post_init__` already ran — added a
  `col=` param to `_line()` instead); `orchestration.py`'s float-epsilon pool-floor bug (`math.floor(x)`
  → `math.floor(x + 1e-9)`).
- **DG-3 implemented, bottom-up (Jordan's own correction of a first-pass eng_counts-division attempt —
  "misleading... should be per-cell troop density... bottom-up... solves multiple engagements"):** new
  `core/exchange.pair_pool_contribution()` redistributes a subunit's unchanged combat-score
  (`subunit_combat_pool`) across a specific contact pair by ACTUAL troop density in the engaged cells
  (`cell_troops`) plus depth-weighted support (reusing `support_engage_frac`'s `SUPPORT_WEIGHTS` falloff)
  — replaces the flat divide-by-simultaneous-pair-count with an exact troop-weighted split.
  `a_troops_frac` (a separate, pre-existing multi-SUBUNIT Command-sharing dampener) kept as an outer
  multiplier, orthogonal to this fix. Known accepted residual, same discipline as Stage A's TOI
  multi-body approximation: a cell simultaneously adjacent to 2+ enemy atoms double-contributes its
  troop share (dogpile edge case, not solved).
- **DG-4 implemented ("a blend of per-subunit as well as whole unit... more likely to wilt if other
  subunits losing, more likely to rally if other subunits winning"):** `build_army` now defaults every
  subunit to its own real starting morale (closing RC-1(b)'s double-count by construction — no new
  state); new `Subunit.pull_morale()` + a continuous per-phase term in `core/state.morale_check_phase`
  pulls each subunit's morale toward its LIVING SIBLINGS' troop-weighted aggregate (new
  `MORALE_SIBLING_PULL=0.15`, tagged Class-B/Jordan-vetoable — the mechanic is ruled, the magnitude is
  not derived from any existing primitive). RC-1(c) (subunit-scale casualty trigger vs shared pool)
  auto-resolves as a side effect — both sides of that mismatch are now subunit-scale.
- **Perf finding, fixed:** `support_engage_frac` was still called unconditionally for every pair even
  though C-ii no longer reads its result — duplicated the same abs→orig cell-coordinate conversion
  `pair_pool_contribution` does internally. Made conditional on `POOL_VARIANT != "C-ii"`. Profiling
  (cProfile on an envelop-army trial) showed the DOMINANT remaining cost is pre-existing Stage-A TOI
  physics (`resolve_toi_and_commit`/`_pair_toi_scale`, 679K calls, ~2.2s of 4.7s), not this fix's own
  code (`resolve_engagements` ~0.6s) — multi-subunit field-path battles are inherently more expensive
  under the existing TOI system; `bat.py`'s full battery now takes ~1-4 min per mode instead of
  seconds (disclosed, not a hang — confirmed by direct profiling and isolated single-trial timing).
- **Adversarial review (general-purpose agent) — 4 findings, all fixed, none moved the recorded
  digests (confirmed by re-running `bat.py --check` all 4 modes post-fix — all still match):**
  1. **(HIGH)** `pair_pool_contribution` recomputed the cell layout from `CELL_PATTERN_FN[shape](tier)`
     (the legacy tier-only pattern) instead of iterating `atom.cell_troops` directly — silently
     zeroed the whole pool for any continuous-scale (`troops=`/`concentration=`) subunit whose real
     footprint (`footprint_for`) extends beyond that small legacy rectangle (confirmed by repro: a
     tier=4/troops=8000 Line's real 70-cell footprint vs. the tier's own 35-cell pattern — pool
     contribution was silently 0.0, now correctly non-zero). Fixed: iterate `cell_troops.items()`
     directly (the same authoritative, footprint-aware source `cells()`/`check_drift` already use).
     Masked in the current battery only by coincidence (existing fixture troop counts happen to stay
     inside the legacy rectangle).
  2. **(HIGH)** The sibling-morale pull ran AFTER this-phase's own casualty/exhaustion erosion, so a
     healthy sibling's pull could retroactively rescue a subunit from a same-phase rout its own
     casualties would have caused, before `rout_resolution` ever saw the eroded value — a materially
     stronger mechanic than "more likely to rally," and an unintended side effect of call ordering.
     Fixed: reordered so the sibling-pull (using a phase-start snapshot) applies BEFORE self-erosion —
     a sibling's state can soften/harden the morale a subunit ENTERS its own erosion with, but can no
     longer erase that erosion's result; self-erosion keeps the final say on this-phase rout.
  3. **(MEDIUM)** Siblings were aggregated from already-mutated live values within the same per-atom
     loop (Gauss-Seidel order-dependency, biased toward whichever subunit iterates first) rather than
     a fixed phase-start snapshot. Fixed as part of the same reorder above (one snapshot dict built
     once per unit before the loop).
  4. **(LOW, dormant)** `build_army`'s `kw.setdefault('morale', morale)` no-ops if a spec explicitly
     sets `'morale': None` (key present, not absent) — silently keeps that one subunit on the
     shared-pool double-erosion path DG-4 exists to close. No current caller does this, but fixed
     (explicit `if kw.get('morale') is None:` check, matching this file's own `unit_type` precedent).
- **Verified:** all 4 `bat.py` digests changed from the pre-DG-3/DG-4 baseline and re-recorded (expected
  — touches shared, non-gated combat-resolution code). Re-checked after the 4 adversarial-review fixes
  above: `unit`/`cell`/`unit_field` stayed byte-identical to their first re-record (the current
  battery/gauge doesn't happen to exercise those bugs on those 3 modes); `cell_field` alone moved
  AGAIN and was re-recorded a second time — its `PER_CELL=1`+`FIELD_MOVEMENT=1` combination
  (continuous-scale subunits, multi-subunit rows, real morale/rout timing) is exactly what Findings
  1-3 touch. `tests/valoria` 87 passed/17 skipped/1 xfailed (neither pytest byte-exact test covers
  field modes — only `bat.py --check` run by hand catches `cell_field`'s movement).
- **Gauge re-run (n=20, reduced from the standard 60 for turnaround — `gauge_mb.py`'s own `__main__`
  hardcodes n=60 with no CLI override, confirmed by reading it):** **honest result: the fix did NOT
  close the targeted gap.** Aggregate counts are unchanged from the pre-fix baseline (single 2/20, multi
  4/20) but the COMPOSITION shifted: multi-mode H1 (mirror Line-vs-Line, previously passing) now reads
  60/40 (WIN-OUT, band 42-58) while C1 (previously failing) now reads 45/55 (OK, band 35-55) — a
  trade, not a net gain. **H3, H5, H6 (three of the four actual Cannae-pattern target rows) remain
  UNRESOLVED (100% draws) in both single and multi mode** — worse than the pre-fix "0-13% losses"
  framing in one sense (that at least resolved decisively, if in the wrong direction) and better in
  another (no longer a rout, just a stalemate) — either way, not inside the historical band. **H4
  (Cannae proper)** improved from a decisive loss to `WIN-OUT` (0/10, 90% draw) — still fails, still
  undershoots. **C4** improved from the disclosed 0-13% range to 66.7% (`WIN-OUT`, 75-95 band, 70%
  draw) — real movement toward the band, still short. This is disclosed, not hidden: RC-1's
  accounting-layer fix was never proven (RC-3 was explicitly "confounded, not proven") to be
  gauge-scale-sufficient on its own, and this n=20 read is the first real evidence on that question —
  it looks like RC-1 alone is necessary but not sufficient; DG-1/DG-2 (composition/yield-mechanic, both
  still open) are the more likely remaining levers, not a bug in this fix.
- **Frozen-wings ablation (§2 step 4) — CLOSES DG-5 cleanly:** H3/H4/H5/H6 read byte-identical
  A%/decA%/draw% whether wings wheel normally or are frozen in place for the whole battle (`n=30`
  each). **No maneuver-timing race exists** — confirms the fixture-scale finding generalizes to gauge
  scale. DG-5 is not a live question; the bottleneck is entirely elsewhere (most likely DG-1's
  composition question, given H3/H5/H6's total non-resolution above).
- **C4-vs-C7 trace (§2 step 5) — single-mechanism, fully explained:** varying only the defender's
  `stance`/`discipline` (`n=30` each): baseline 16.7%; `+discipline=8` alone: 16.7% (zero effect);
  `+stance='hold'` alone: 76.7% (the entire gap); `+both` (=C7): 76.7% (no additional discipline
  contribution). **`stance='hold'` alone fully accounts for the C4→C7 divergence** — discipline plays
  no role.
- **Not yet done:** `test_envelop_reaches_rear_node`'s xfail re-evaluation (next); DG-1/DG-2 remain
  open and are now the better-evidenced next lever given the gauge results above.
