# Coverage Matrix — Archive, part 2

Continuation of `tests/coverage_matrix_archive.md` in reading order (CLAUDE.md §4: a document that
outgrows its ceiling splits into `_part2`, `_part3`, … sequentially — the index/infill pair is
retired as a default). Split 2026-07-29 (ED-MB-0051) when part 1 crossed the 50,000-token
compliance ceiling. Content is byte-identical to what part 1 held; nothing was condensed.

The ACTIVE matrix is `tests/coverage_matrix.md`; both archives are history.

---

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


<!-- Relocated from active coverage_matrix.md 2026-07-23 (register-size cap). -->
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

<!-- Relocated from active coverage_matrix.md 2026-07-23 (register-size cap). -->
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



<!-- Relocated verbatim from tests/coverage_matrix.md 2026-07-29 (ED-MB-0048) to keep the
     active matrix under its 15,000-token register cap. Content unchanged. -->

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


<!-- Relocated verbatim from tests/coverage_matrix.md 2026-07-29 (ED-MB-0050) to keep the
     active matrix under its 15,000-token register cap. Content unchanged. -->

## 2026-07-25 — ED-MB-0041: the two gauge invariants that need no band (Jordan-approved)

The win-share gauge cannot tell a double envelopment from two lines colliding — both can produce the
same number, which is how the reachability sweep found a config that passes the Cannae row with
envelopment pathing switched OFF. Two properties close that gap from opposite directions, and neither
needs a band or a judgement call.

**1. Reverse-pair side symmetry** (`audit/.../reverse_pair_symmetry.py`). `decA(X vs Y) + decA(Y vs X)`
must be 100: which army occupies the engine's "side A" slot is bookkeeping, not physics. Distinct from
the pre-existing `symmetry_probe.py`, which tests MIRROR symmetry (identical armies → 50/50) and is
structurally blind to an interaction asymmetry. Measured at n=60:

| pair | fwd | rev | sum | deviation | sigma | verdict |
|---|---|---|---|---|---|---|
| H2/H9 | 49.2 | 65.0 | 114.2 | +14.2 | **+1.6** | OK — *not* a defect |
| H3/H10 | 61.0 | 76.7 | 137.7 | +37.7 | **+4.5** | ASYMMETRIC |
| H4/H11 | 6.7 | 55.0 | 61.7 | −38.3 | **−5.3** | ASYMMETRIC |

**This corrects my own earlier reporting.** I had described all three sums (114.2 / 137.7 / 61.7) as
evidence of a side-dependent mechanism. Reporting the deviation in units of its own standard error
shows H2/H9 is **+1.6σ — consistent with noise**. The defect is confined to the *envelopment* rows,
which localises it far more sharply and is consistent with ED-MB-0039's envelopment-stability
diagnosis. A raw percentage-point threshold would have hidden that distinction entirely.

**2. Casualty/duration realism** — a SECOND scoreboard in `gauge_mb`, reported beside the win-share
count and deliberately *not* folded into it, so the existing 10/20 figure stays comparable with every
number already in the ledger, handoff and PR bodies.
- `matchup()` previously averaged `a_cas`/`b_cas` over **all** seeds regardless of who won — the wrong
  quantity: the sources constrain what the LOSER lost and how much less the WINNER lost, and a near-even
  matchup washes that asymmetry out. Now conditioned on the outcome (`win_cas`/`lose_cas`), plus a
  `capped` rate (seeds that ran to the turn cap without resolving).
- Bands are in-repo or logical consequences of in-repo values, **not invented literature intervals**:
  loser 15–30% is the repo's own rout-onset band (ED-MB-0031); winner <15% is that band's
  *contrapositive* (the winner did not break, so it sits below the break floor); the cap rate is
  structural, not historical.
- **Duration is deliberately NOT banded absolutely.** An engine turn has no defensible mapping to real
  time, so any interval in turns would be fabricated to look grounded. Only the cap-hit rate is banded.
- `None` (not `0.0`) when nothing resolved — treating an absent measurement as "the winner lost
  nothing" would turn the engine's most broken rows into its cleanest passes.

**First result, and it is stark.** The H1 *mirror* passes win-share at 50.0 while killing **~85% of the
loser and ~26% of the winner** against a 15–30% / <15% expectation. Casualty-realism scores **0/20**.
The win-share gauge has been reporting a green mirror on a battle that annihilates both sides.

Pinned by `tests/valoria/test_gauge_invariants.py` (8 tests). Both invariants are currently RED and
marked **xfail, not skipped**: the assertion runs every time, does not redden CI for a known-open design
gap, and flips to XPASS the moment it is fixed. Sample size is documented as a **power** limitation
rather than glossed — H3/H10, a +4.5σ defect at n=60, XPASSed at n=24, so an XPASS at suite-n is a
prompt to re-measure at n=60, not evidence of a fix. Also single-sourced the 18/20 turn caps, which
were duplicated literals about to become four copies.


<!-- Relocated verbatim from tests/coverage_matrix.md 2026-07-29 (ED-MB-0051) to keep the
     active matrix under its 15,000-token register cap. Content unchanged. -->

## 2026-07-25 — ED-MB-0041 phase 2: local break, cell-scale contagion, and the half of phase 1 I never wired

**First, a correction to phase 1.** `cohere_cells` shipped with **zero live call sites**. The
modulate-down half of the loop existed, was tested, and never ran in a battle — so the phase-1 gauge
measurement was of **aggregate-up only**. Same dead-machinery pattern this audit exists to find, built
into my own work while documenting the pattern. Now wired.

**Phase 2 mechanisms, all gated behind `PC_CELL_MORALE` (OFF):**
- **Local break** (`cell_broken`) — a cell whose morale reaches 0 stops FIGHTING. Implemented in
  `_pair_engaged_troops`, the single place per-cell troops become emitted combat weight, so no other
  emission path needs to know. `cell_troops` is untouched: the men are still there to be killed and
  still count as casualties. They have stopped being a fighting part of the line, which is what a local
  break *is* — zeroing them would make a break indistinguishable from annihilation.
- **Cell-scale contagion** (`propagate_cell_breaks`) — a broken cell shakes its lattice neighbours, so a
  gap spreads outward from where it opened. Neighbours are the 8-neighbourhood of pattern coordinates,
  so the spread follows the formation's actual shape with no shape-specific code.
- **Formation break** — a subunit whose broken cells hold `CELL_BREAK_ROUT_FRAC` of its live men has
  come apart as a body even with positive aggregate morale. Same shape as `ROUT_CASCADE_FRAC` one scale
  down; same deliberately **unchosen** magnitude.
- **Order matters**: contagion runs *before* cohesion each phase. Reversed, the body would paper over a
  break before it spread and contagion would never do anything.

**The emergent property — nothing says "disciplined units close gaps".** Contagion pushes down, cohesion
pulls toward the body's morale at a discipline-gated rate, and the behaviour falls out of the contest.
Measured over four phases from one broken cell:

| discipline | broken cell | outcome |
|---|---|---|
| 6 | **+3.08** | gap **closed**, broken share 0.00 |
| 1 | **−0.13** | still broken, share 0.11 |

**A test of mine asserted the wrong thing, and being wrong found the mechanism.** I expected cohesion to
lift the *shaken neighbours*. It doesn't — cohesion pulls toward the mean, and freshly-shaken neighbours
sit just *above* a mean the broken cell has dragged down, so they are pulled slightly further down. The
contest that matters is over the **broken** cell: whether the body can haul it back across zero. The
test now asserts that, with the wrong first version recorded in its docstring.

`test_cell_morale.py` now 16 tests. Not yet measured on the gauge — phases 1+2 will be measured together,
since phase 1's number was taken with half the mechanism dead.


<!-- Relocated verbatim from tests/coverage_matrix.md 2026-07-29 (ED-MB-0052) to keep the
     active matrix under its 15,000-token register cap. Content unchanged. -->

## 2026-07-25 — ED-MB-0041 phase 2b: local break was UNREACHABLE; the missing symmetry

**Phases 1+2 measured byte-identical to phase 1** — every one of 20 rows to the decimal, 1/20 casualty
and 8/20 win-share. Not a small effect: *zero*. Byte-identical is a far stronger signal than
disappointing, because a smaller-than-hoped number would have been absorbed as "phase 2 helps a little",
whereas identical across twenty rows can only mean the code never ran in a way that mattered.

**Instrumented: 72 of 144 cells "broken" at EXACTLY −1.0.** The uniformity was the diagnosis — local
damage produces a spread, so one repeated value means a single uniform write. It was the body-wide
stochastic-rout punch (`erode_morale(max(eff_morale + 1.0, 0))`, designed to land at −1.0), which phase
1 routes across all cells. **Cells were breaking as a CONSEQUENCE of the body routing**, strictly after
the event phase 2 exists to precede: `propagate_cell_breaks` only ever saw already-dead bodies, the
formation-break check is guarded by `not atom.routed`, and a routed subunit's emission is already zero.

**The cause was an asymmetry, not a magnitude** — which is why tuning would have been the wrong move:

| | gradual erosion | break-point short-circuit |
|---|---|---|
| body | yes | **yes** — `_stochastic_break`, du Picq 15–30% |
| cell | yes | **none** |

At `MORALE_PHASE_CAP=3` against a 6.0 pool a cell had to be **destroyed twice over** to break by erosion
alone, so the body always won that race by construction.

**Fix (`check_cell_breaks`)**: each cell draws its own break-point in the same historical band, skewed
by discipline, and breaks when its own casualty fraction crosses it — the body's mechanism at the
cell's scale, not a coefficient nudge. Morale values are now a genuine spread (−4.85, −2.79, −1.12,
−0.89, −0.47, +0.13 …) rather than every cell at −1.0.

**⚠ Early measurement shows OVER-FIRING**: single-mode draw rates of 76–100%. Bodies may now break so
early that nothing resolves. Recorded before the multi-mode scoreboard lands, so the concern is on the
record independent of how the final number reads. Flag remains OFF.

> **That concern was WRONG, and the error is instructive.** The flag-OFF control run (below) shows
> H3/H5/H6/H10/R3 at **100% draws in single mode with the flag off too** — the pre-existing tick-cap
> artifact the gauge's own docstring documents, present before phase 2b and unmoved by it. I read
> single-mode rows from a run that had no control beside it and attributed a standing artifact to my
> own change. The rule this cost me: **a number without its control is not a measurement**, and that
> applies to a worrying number exactly as much as to a flattering one.


<!-- Relocated verbatim from tests/coverage_matrix.md 2026-07-29 (ED-MB-0053). -->

## 2026-07-25 — ED-MB-0041 phase 1 FIXES: two defects in the per-cell morale wiring

**1. A silent no-op I introduced — the exact pattern this audit exists to find.** With cell morale
seeded, `eff_morale` reads the CELL MAP and ignores the scalar; but `erode_morale`/`pull_morale` WRITE
the scalar. So enabling per-cell morale silently disabled: the canonical §A.4 casualty/exhaustion
erosion, the DG-4 sibling-coupling pull, and the stochastic-rout punch that drives morale ≤0 to force a
break — meaning **`PC_STOCHASTIC_ROUT`, ratified an hour earlier, stopped working whenever
`PC_CELL_MORALE` was on.** Measured: `erode_morale(4.0)` left the aggregate at 6.0 while writing 2.0 to
a field nobody read. Fixed by routing body-wide morale uniformly across cells: the aggregate is the
weighted mean, so subtracting `amount` from every cell lowers it by exactly `amount`. Scalar and
cellular models stay numerically identical for body-wide effects; cells diverge only through LOCAL
damage, which is the point.

**What caught it was a prediction made before looking.** I stated that phase 1 should move the gauge
*modestly* and that a large swing would be a warning sign rather than a win. H3 swinging ~66 → 40
tripped that immediately. Without the prediction there was a ready-made explanation — "per-cell break
makes bodies come apart earlier" — and a broken configuration would have been banked as a success.

**2. A coupling fault.** `_erode_cell_morale_from_damage` hangs off `_apply_with_spill`, the single
owner of casualty application, which is deliberately duck-typed. Reading `atom.cell_morale` directly
made a MORALE feature impose a structural requirement on the DAMAGE substrate. `getattr` now; the fault
was the coupling, not the test double that exposed it.

**Process note, recorded because it caused a bad push.** I ran `valoria_local --staged | tail -2 && git
commit`. The pipe means the chain sees `tail`'s exit status, not the gate's — so a FAILING co-file gate
was masked and the commit proceeded. Gate output must not be piped when its exit code is what gates the
next command.


<!-- Relocated verbatim from tests/coverage_matrix.md 2026-07-29 (ED-MB-0053). -->

## 2026-07-25 — ED-MB-0041 phase 1 MEASURED: modest, as predicted; flag stays OFF

Measured on corrected code (the first run measured the silent-no-op configuration and was discarded).

| | rout ON baseline | + `PC_CELL_MORALE=1` |
|---|---|---|
| casualty realism | 2/20 | **1/20** |
| win-share | 7/20 | **8/20** |
| loser casualties | 29-41% | 29.8-45.4% |
| **H6 specifically** | **79.2%** | **45.4%** |

**The 2/20 → 1/20 is NOT a regression.** One row crossed a sharp edge: R1 moved 29.9% → 30.2% against a
30.0% ceiling. Calling that "phase 1 lost a row" would be the band-edge artifact already flagged when it
ran the other way, and the caveat has to apply symmetrically or it is just advocacy.

**The real movement is H6, 79.2% → 45.4%** — the row no rout-contagion threshold could touch, because
H6's stubbornness is not at subunit granularity. Per-cell morale reaches it. Win-share also gained a row.

**Verdict: roughly neutral, one structural gain, flag STAYS OFF.** The reason is the one stated *before*
the measurement: **nothing consumes per-cell morale as a break condition yet.** Rout still evaluates the
whole-body aggregate — now better-informed, since it is derived from where damage actually landed, but
still whole-body. The map is populated and correct; nothing reads it to decide a SECTION has gone. That
is phase 2 (local break), and it is where the payoff should appear.

**The prediction is the point.** It was recorded before the first run and held across a discarded
measurement and a corrected one. Its first job was catching the silent no-op (a swing far larger than
predicted); its second is refusing to over-read a neutral result now that the direction is mildly
favourable. A prediction that only fires against bad news is not a control.


<!-- Relocated verbatim 2026-07-29 (ED-MB-0054). -->

## 2026-07-25 — ED-MB-0041 phase 1: the cell is the primitive for MORALE

Jordan's directive ("the cell needs to be the primitive for morale, discipline, quality, stamina,
route, health, armour, facing, damage, troops count") and its earlier statement of the mechanism:
*"cells get modulated by subunit holistic scoring, but the cells themselves are what aggregate into
those scorings in the first place, so a cell should be able to have worse morale than another cell in
same subunit."* **That last sentence was literally unrepresentable** — the cell was the primitive for
geometry only (position, facing, contact, casualty placement); every piece of STATE was a subunit
scalar, so a rear cell being cut down and a front cell holding shared one number.

**Two-way loop, not a broadcast:**
- **AGGREGATE UP** — `eff_morale` is now the troop-**weighted** mean of live cells, derived rather than
  stored. Weighted so a nearly-empty shattered cell cannot drag the body as hard as a full one; a flat
  mean would let a cell holding three men count as much as one holding a hundred, and a body would read
  as broken while nearly all its strength was still steady.
- **MODULATE DOWN** — `cohere_cells` pulls each cell toward the body's holistic value, **signed** (a
  steady body steadies a shaky corner; a disintegrating one drags a firm corner down) and
  discipline-gated, because holding when your neighbours are hit is what discipline names.

**Erosion rides on `_apply_with_spill`**, the single owner of casualty application, so *every* path that
kills men — melee, volley, pursuit, freed-attacker, cellwise facing-weighted — shakes the cells it
killed them in, with no caller needing to remember. Scaled by the FRACTION of the cell destroyed, not
the absolute count: losing 20 of 100 beside you is the same shock at any body size, and an absolute
scale would make dense cells look braver purely for being dense.

Demonstrated: concentrate damage on one cell of three and it holds **4.51 morale while its siblings
hold 5.94** — Jordan's test case, earned in play rather than injected.

`tests/valoria/test_cell_morale.py` (11 tests) pins the directive itself, both directions of the loop,
the troop-weighting, the discipline gate, the fraction-not-count erosion shape, and one invariant worth
calling out: **cohesion CONSERVES the aggregate** (`new_m = m + r(agg−m)` ⇒ weighted mean is unchanged).
If that ever fails, cohesion has become a free morale source and a body could steady itself forever.

Gated `PC_CELL_MORALE`, **default OFF** — verified inert: byte-exact goldens, stochastic-rout and
rout-contagion suites all green unchanged. Not yet measured on the gauge; that is the next step, and the
flag stays off until it is.


<!-- Relocated verbatim 2026-07-29 (ED-MB-0057). -->

## 2026-07-25 — ED-MB-0042 (RETRACTED, see above): PC_CELL_MORALE flipped ON; per-cell breaks subsume the body-level one

Measured against a **same-session flag-OFF control** at the gauge's own n=60, in the resolving (multi)
mode, on both scoreboards:

| | win-share bands | casualty/duration realism |
|---|---|---|
| OFF | 7/20 | 2/20 |
| **ON** | **8/20** | **7/20** |

**The casualty column is the evidence, and it is a mechanism producing a shape rather than a fitted
number.** Loser losses fall out of the 31–40% range into 26–30%: H6's loser goes 79.2% → 48.9%, C7's
39.9% → 32.1%. That is du Picq's claim — a body comes apart before it is destroyed — falling out of
cells that stop being a formation earlier than they stop existing. Nothing was tuned to hit a band.

**Costs, stated not buried.** `single` mode drops 7/20 → 5/20, but both flipped rows (H2 51.4→46.2,
H9 47.5→52.8) are sub-1σ moves across a band edge at n=60 (SE ≈ 6.5pp) in the mode the gauge documents
as non-resolving — not evidence. C4 goes 91.5 → 96.7 against a 95 ceiling (≈0.5σ). Reverse-pair
symmetry improves 3.8σ → 3.4σ; **H4/H11 stays ASYMMETRIC and stays open.**

**Goldens re-recorded, not pinned off.** `unit` and `cell` both move; `_PINNED_OFF` gains
`PC_CELL_MORALE: '1'`. Pinning it off would have kept the digests stable while quietly ending their
coverage of the shipped engine — this flag is not a path selector like `FIELD_MOVEMENT`, it changes the
state model on the path `cell` mode exercises. Same treatment as `PC_OCTAGON_DMG`.

**Unplanned finding: `PC_STOCHASTIC_ROUT` is now inert in the shipped configuration.** With cells
carrying their own break-points, the loser reaches **35.6%** casualties with body-level stochastic rout
OFF and **36.1%** with it ON — no separation. The cells break first (same 15–30% band, discipline-
skewed) and `CELL_BREAK_ROUT_FRAC` ends the body before the subunit-level draw is consulted. Recorded
and pinned by `test_per_cell_break_subsumes_the_body_level_one` rather than acted on: the flag is still
load-bearing on the unseeded fallback path, so it is a retirement **candidate**, not dead code.
`test_loser_breaks_near_historical_band` now pins `PC_CELL_MORALE=OFF` — it measures the body-level
mechanism, and inheriting the live default made its control arm already-broken and the test a no-op.
