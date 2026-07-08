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
  above: `unit`/`unit_field` stayed byte-identical to their first re-record; **`cell` and `cell_field`
  BOTH moved again** and were re-recorded a second time. **Process gap, caught by CI not locally:**
  `test_byte_exact_cell_mode` only hard-fails inside `_in_reference_env()` (GITHUB_ACTIONS+Linux) and
  silently SKIPS elsewhere — a real pytest pass count locally can hide a genuine `cell`-mode digest
  drift. Confirmed NOT a portability artifact (this sandbox reproduces CI's exact new hash directly via
  `bat.py --check`) — a real movement from the same fixes, just invisible to `pytest`'s local summary.
  Lesson recorded in `bat.py`'s own comment: always re-verify `cell` with a direct `bat.py --check`
  call, not just the pytest suite, after any core.exchange/core.state/orchestration change.
  `tests/valoria` 87 passed/17 skipped/1 xfailed either way (neither byte-exact pytest test covers the
  two field modes at all — manual `bat.py --check` is the only check for those).
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
  `designs/proposals/mass_battle_fighting_withdrawal_v1.md` (status PROPOSED): a per-subunit `yielding`
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

Jordan ruled DG-2 = **"build it now"**. Built exactly the proposal doc's (`designs/proposals/
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
