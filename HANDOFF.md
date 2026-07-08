# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## History

Full narrative for the work below (2026-06-24 through 2026-07-02) moved to
`handoffs/HANDOFF_archive.md` (2026-07-08, token-efficiency pass) — this file had drifted from
"index" to a full append-only session log. Nothing was deleted, only relocated; the archive is
frozen, do not resume work from it.

Per-lane continuity now lives in `handoffs/HANDOFF_<LANE>.md`, using the same 9 lane codes as
the `ED-<LANE>-NNNN` editorial namespace (`ED-IN-0001`, `CLAUDE.md` §3). This file is the
**index** plus genuinely cross-cutting items — read the lane file(s) relevant to your session
before starting work, and keep your own updates scoped to your lane's file (or this one, only
for cross-cutting items).

| Lane | Subsystem | File |
|---|---|---|
| `MB` | Mass battle | `handoffs/HANDOFF_MB.md` |
| `PC` | Personal / scene combat | `handoffs/HANDOFF_PC.md` |
| `FI` | Field investigation | `handoffs/HANDOFF_FI.md` |
| `SC` | Social contest | `handoffs/HANDOFF_SC.md` |
| `FA` | Faction actions | `handoffs/HANDOFF_FA.md` |
| `WR` | World | `handoffs/HANDOFF_WR.md` |
| `IN` | Infrastructure / cross-cutting | `handoffs/HANDOFF_IN.md` |
| `GO` | Godot conversion | `handoffs/HANDOFF_GO.md` |
| `SE` | Settlements | `handoffs/HANDOFF_SE.md` |

**Why the split:** the ID-collision incidents that motivated `ED-<LANE>-NNNN` (two same-session
concurrent-allocation collisions on the flat sequence within one PR — see `ED-1094`'s ledger
entry) are the same failure class that makes one shared `HANDOFF.md` a merge-collision magnet
once multiple lane-sessions run concurrently. This is a **partial, deliberate exception** to the
repo's earlier "one continuity surface" consolidation (`deprecated/session_machinery/` retired
per-topic session-log files because they rotted independently) — the difference is this split is
keyed to the SAME lane taxonomy the ID system already enforces, not an ad-hoc per-topic split,
and this root file remains the one stable SessionStart entry point.

**Full detail on the split itself, and every historical decision predating it, is filed at
`handoffs/HANDOFF_IN.md`'s Decisions log** — this root file does not duplicate that history.

## Next actions

_(Reserved-ID state healthy as of 2026-07-01: **LB-21 executed** — `id_reservations.yaml` v3
verified live max, allocated ED 1081–1087 to the month-overview consolidation from
block D, and pre-provisioned disjoint Round-3 block E (ED 1100–1149 / PP 830–849). Allocate
per the file's protocol; never max+1. Since the 2026-07-02 cutover (ED-IN-0001), new EDs
allocate per-lane from `lane_ids` — the flat sequence is frozen.)_

- **JORDAN RULING NEEDED — ED-SC-0015 (Parliamentary total-victory Mandate stacking).** Filed
  2026-07-08 building the FA/SE historical-precedent docket's unblocked items (see
  `handoffs/HANDOFF_SC.md` Pending + `handoffs/HANDOFF_FA.md`): the §10 BG-Vote Total-Victory
  Mandate rider (−1) and the new Parliamentary-Censure §5.4 target effect (−1) compose to −2 on
  the same faction within one motion; currently implemented as stacking (the literal default) but
  explicitly not ratified canon. This is the one item from that same-day build genuinely needing
  Jordan's own call, not routine merge-ratification — everything else in that build (P3-lite Agôn
  harness, Muster/action-mix/conquest-terms rework, 9 settlement/faction design-doc PROPOSED
  sections) ratifies normally on merge per ED-1094.
- **START HERE — Master Workplan v6 is the live steering surface, RATIFIED with the whole
  of PR #78 (2026-07-05, ED-IN-0009/ED-IN-0011 — Jordan: "Ratify commit merge all").** `designs/workplans/valoria_master_workplan_v6.md`: North-Star milestones (M1 one
  playable season · M2 any-seed story bar · M3 Godot slice), per-lane workstreams (status
  stays in `handoffs/HANDOFF_<LANE>.md` — v6 only sequences), and the tiered T0/T1/T2
  Jordan-decision register (§5) that **supersedes the 2026-07-01 `decision_queue.md` as the
  live decision list** (that file is now a dated snapshot; its items 1–3 were refreshed at
  supersession). Steering reconciliation ED-IN-0006 EXECUTED: `roadmap_state.yaml` retired to
  `deprecated/references/`, workplan v5 archived with banner (its J-38 contradiction
  corrected), hierarchy adopted (CURRENT.md → lane handoffs → workplan-derived). Same PR:
  the **narrative engine v2 "Churn Engine"** (`designs/audit/2026-07-05-emergent-narrative-engine/
  narrative_engine_design_v2_churn.md`, five-refuter adversarial pass applied) — **RATIFIED
  in full 2026-07-05 (ED-IN-0011), including F-F/fork-8 at its default** (subtract-only +
  the weight set as versioned data; values revisable anytime). Remaining T0 wall: JD-1 (PC)
  + ED-1051 (engine_clock); fork 10's faction count = ED-FA-0001 (needs_jordan).
- **R2 (closing-distance/facing/grip/contact redesign) — I0→I8 COMPLETE (2026-07-03), PR #72
  (branch `claude/scene-combat-closing-distance-mg18pq`), awaiting review/merge.** Implemented the full
  ratified plan (`designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md`) per
  its own per-increment discipline (implement → `pytest tests/valoria -q` at the enumerated 8-red baseline,
  zero new red at every increment → targeted acceptance checks → `capabilities.py`/`state_graph.py`
  self-tests → commit). All 9 Jordan-decisions (JD-1..JD-9) taken at the plan's own stated default per this
  session's task framing (a fresh session picking up an already-ratified plan). I8's capstone measurement +
  findings record: `designs/audit/2026-07-02-scene-combat-closing-distance-redesign/i8_capstone_audit.md` —
  **the one open finding**: the plan's ~55-75%/~30-45% reach-class/dagger CONTESTED-balance target is
  **not yet met** (reach-class weapons run 75-93% vs arming; not inverted, but above the band), traced to
  the SAME pre-existing Phase-B mass-model calibration debt already carried by the 3 accepted `[PHASE-C
  FLAG]` reds (`test_gap_game_poleaxe_spikes_plate`/`test_anchor_is_near_one`/`test_lunge_quality_...`) —
  explicitly out of R2's scope, deferred to Phase C's engine-scale re-tune (re-annotated, not silently
  patched). **Next action, if a Phase C recalibration effort starts:** read the capstone audit doc's item 1
  table first — it's the widest-scope measurement of the drift to date.
- **START HERE — month-overview + consolidation (2026-07-01).** The month's comprehensive
  review, the consolidation execution/reconciliation logs, and the **single consolidated
  23-item Jordan decision queue** live at
- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec now
  RATIFIED (2026-07-02).** The month's comprehensive review, the consolidation
  execution/reconciliation logs, and the **single consolidated 23-item Jordan decision queue**
  live at `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see
  `decision_queue.md` first — every gated item below is indexed there). **Doctrine ratification**
  (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`) and **J-38 propagation-spec
  authorship** (ED-1093, `designs/architecture/propagation_spec_v1.md` — supplies `engine_clock`'s
  candidate home doc; the `doc:null`/[ASSUMPTION] grade stays unflipped until ED-1051 is
  separately resolved) are both **CANONICAL** as of PR #58 (ED-1094 merge-ratifies-by-default).
  The propagation spec's own §5 carries its ranked open items (OF-7/OF-B1 amendments, D.6/OF-D6
  double-count, `decay()` spec, RNG-MODEL-COLLISION, cap constants, ORD-3/ORD-4) — ratification
  did not resolve these, only fixed the spec's home-doc status. Remaining highest-leverage queued
  decisions: Track-2 residuals (below), field-ON, the values_master regenerate-vs-retire call,
  the duplicate compilation homes, and item 19 (Agent-Teams/subagent-roster adoption).
- **Mass battle — Stages A–D + LC-8 landed on `main` (2026-06-30 → 2026-07-02, PRs #45/#52/#56/#57/#59);
  this file previously had zero record of any of it — closing that continuity gap now.** Coordinate-field
  true-adjacency contact (Stage A), facing/attention/reaction physics (Stage B), the command layer
  (`build_army`/timed `Order`s/escort — Stage C), and role/doctrine wiring + `build_envelopment`/
  `build_refused_flank` Unit-level presets (Stage D, ED-907/908/909) are all merged. **LC-8 executed
  2026-07-02 (ED-1088):** `Horseshoe`/`RefusedFlank` retired as `Subunit.shape` values per Jordan's
  go-ahead ("those are emergent outcomes") — only Line/Arrowhead/GappedLine/Column remain valid
  subunit shapes; envelopment/refused-flank exist only as the Unit-level presets above.
  `bat.py`'s grid-mode golden digests were deliberately re-baselined (approved behavior change).
  The workbench (`tests/sim/mass_battle/workbench/`) was extended to visualize the new multi-subunit
  presets — see `tests/coverage_matrix.md`'s 2026-07-02 entries for what shipped and two real bugs
  found/fixed along the way (a `reset_positions` multi-subunit collapse bug; a frontend preset-dispatch
  bug). **Governing plan:** `designs/audit/2026-06-30-massbattle-bottomup/05_redesign_workplan.md` +
  the session's own staged plan (Stages A–F, not yet promoted into the repo — ask the session for
  `using-opus-4-8-ultracode-floating-tiger.md` if resuming this thread). **Three Jordan rulings landed
  2026-07-02 (all executed same day):** (1) **ED-1089** — `FIELD_MOVEMENT=1`/`PC_NODE_COHESION=1` are
  now the DEFAULTS (Stage A step 7 executed; "yes, field movement is default."); the grid stays the
  byte-exact oracle via explicit `FIELD_MOVEMENT=0 PC_NODE_COHESION=0` pins (the CI gate was updated
  from env.pop to explicit '0' pins — load-bearing, see test_mass_battle_byte_exact.py), and bat.py's
  field digests were re-recorded (they had gone stale vs the LC-8 battery). (2) **ED-1090** — videogame
  sub-unit cap is **11** ("subunits can be as high as 11."), lifting the TTRPG hard cap of 3; enforced
  in `engine.build_army`; open reconciliation flagged: Command clamps 1–7, so >7 commanded subunits
  needs a future Command-exceeding mechanism (subordinate officers?) — future ED. (3) **ED-1091** —
  the charge-recoil now zone-gates to the frontal (GREEN) arc (`PC_RECOIL_FRONTAL`, default ON;
  historical-validity condition verified against `mass_battle_gauge_grounding.md` §4.3/Burkholder
  before executing, per Jordan's "c7 if it is historically valid"); gauge row C7 can now legitimately
  add a braced+enveloped variant (grounding doc §4.3/§5.7 still says "flagged, not fixed" — update on
  the next gauge pass). **An orphaned-proposal audit (2026-07-02) also flagged:** `references/
  mass_battle_redesign_workplan_v1.md` is fully superseded (no banner exists — worth a supersession
  marker); `designs/proposals/multiunit_envelopment_plan.md`'s cross-**Unit** spatial envelopment
  ("Path B") is a materially different, still-unbuilt mechanism from the Unit-level `build_envelopment`
  that landed — don't conflate "Envelopment shipped" with "Path B shipped."
  **Stage E (Army Configuration Mode) shipped 2026-07-02** (MVP: click-to-place deployment tab in the
  workbench, `GET /api/roster-options`, `engine.SUBUNIT_CAP` client-enforced). **Stage F investigated
  2026-07-02 (ED-1092):** speed-differential puncture and depth-absorption were already done; fidelity
  D2 (cavalry lethality gated by regime) verified already-correct by direct probe; fidelity D1's zone
  half shipped as ED-1091, its actor half was Jordan-gated (no canonical actor-gate predicate existed).
  **T1–T4 charge-recoil ruling EXECUTED 2026-07-02 (ED-1095)**, closing D1's actor half plus three
  further parts from Jordan's own multi-clause ruling: T1 actor-gate (`PC_RECOIL_CHARGER_GATE` —
  charger must literally be `troop_type=='cavalry'`), T2 brace-setup delay (`PC_BRACE_SETUP_DELAY` +
  `Subunit._brace_since_tick` — brace needs ≥1 full tick of setup, stamped by `check_orders`), T3
  reach-gate (structural only — wires `troop_types.registry.reach_for` into the recoil condition, does
  **not** populate `TROOP_TYPE_REACH`, which stays deliberately empty pending a separate ruling), T4
  mounted-archer default kiting (`build_army` implicitly defaults `role='Kite'` for `mounted_archers`
  with no explicit role/shape/instructions). All four additive/toggle-gated, byte-exact-off preserved
  (verified all 4 `bat.py` digest modes + `tests/valoria` 81 passed/10 skipped).
  **RESOLVED 2026-07-02 (ED-MB-0001) — the movement/pathing fix-plan (ED-1096's root-cause finding)
  is EXECUTED, adversarially reviewed, and verified.** `envelop`/`sweep`/wheel/kite are now real on
  the live default node path, not just the legacy grid path. All 8 fix-plan steps + decision gates 2
  and 4 landed on `claude/mass-battle-audit-5c6nih`: `Subunit._rekey_node_state` fixes check_drift's
  node-state corruption; `reset_positions` is a deliberate no-op for node-path atoms; weapon-derived
  `unit_type` (`troop_types.registry.unit_type_for`) wired into `build_unit`/`build_army`, kite
  decoupled from `unit_type=='ranged'`; lateral file-holding restored (siblings hold their own
  deployment file); the node WHEEL's 180° facing-lerp stall replaced with a rotation-based update;
  the maneuver acceptance validators (`validators.py`'s `v_envelop`/`v_sweep`) re-pointed at the node
  path via a new `path` parameter, landed as `tests/valoria/test_mass_battle_maneuvers.py`; the
  waypoint primitive (`Subunit._resolve_maneuver_goal`/`_envelop_goal`/`_sweep_goal`) gives
  `_node_advance` real per-tick steering for `envelop`/`sweep`, modeled on the legacy per-cell
  two-state machine at anchor granularity; `PER_CELL`'s default flipped `0`→`1` (gate 4, "yes, all
  options/modules must be turned on") unlocking fatigue/charge-shock/brace-recoil/cavalry-speed by
  default. **Decision gates 1 (Command/Discipline-gated conditional tactics) and 3 (facing/attention
  split) remain explicitly DEFERRED** per Jordan's own sequencing ruling ("gates 1 and 3 are to occur
  AFTER we confirm that envelopment/pincer/wheeling/etc with pathing/routing is confirmed to work") —
  not built, by design, not a gap. A 5-dimension adversarial-review Workflow (sonnet finders + opus
  verify) found and fixed 6 more real bugs the same session, the most significant being that kite
  steering had NOT actually been ported to the node path in the first pass either (step 7 built
  `_envelop_goal`/`_sweep_goal` but no `_kite_goal` — mounted_archers still closed to melee) — closed
  via a new `_kite_goal`, verified holding standoff distance 6.5-8.3 against a Line. **Verified:** all
  4 `bat.py` digest modes byte-exact (2 unchanged grid, 2 deliberately re-recorded field, isolated via
  bisection to steps 1/4/5/7); full `tests/valoria` suite green (88 passed/10 skipped/1 xfailed); a
  `build_envelopment` wing tracked tick-by-tick under default toggles genuinely wheels from row 36 to
  row 19 — past the defender's own settled row — not a straight walk-in; delivered to Jordan as an
  interactive Artifact re-tracing the exact H4 (Envelopment vs Arrowhead) scenario shown broken
  earlier in the engagement. **One combat-balance finding disclosed, NOT chased (out of this fix's
  scope, per this repo's standing discipline against retuning magnitudes to fit a band):** enabling
  `PER_CELL`'s previously-inert fatigue/attrition/envelopment-sigma mechanics makes a frontal
  engagement resolve faster than a wide envelopment detour can complete in some compositions —
  confirmed via direct isolation to be a combat-*pacing* interaction, not a movement regression (a
  single-subunit control fight at the same troop ratio favors the attacker 14-0-6/20 seeds; forcing
  `orchestration.PER_CELL=False` alone restores the affected test's pass). Visible at battle scale in
  `gauge_mb.py`'s re-run (H3/H4(Cannae)/H5/H6 lose 0-13% instead of the 45-72% expected band) — landed
  as a loud, documented `xfail(strict=False)` on `test_envelop_reaches_rear_node`, not silently
  patched. **Next action for whoever picks this up:** the underlying combat-balance/pacing question
  (numerically-dominant vs. thin-and-yielding pinning force; a maneuver time-budget separate from the
  frontal fight's own clock) is open and needs either Jordan's design call or a dedicated combat-
  balance pass — then decision gates 1/3 (Command/Discipline-gated conditional tactics; facing/
  attention split) can proceed per the sequencing ruling above. Full detail: `tests/coverage_matrix.md`'s
  2026-07-02 movement/pathing-audit entries; `designs/audit/2026-07-02-mass-battle-movement-pathing-audit/
  README.md`; ledger entry `ED-MB-0001` (canon/editorial_ledger.jsonl) — the first allocation under the
  new `ED-<LANE>-NNNN` namespace (ED-IN-0001, origin/main cutover) that superseded in-progress
  in-code citations of the now-frozen flat `ED-1097`.
  **START HERE — the "next action" above is RATIFIED and its two blocking decision gates are RULED
  (2026-07-04, ED-MB-0002, merged via PR #73):** `designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/
  README.md`, produced by a Fable-led four-lens adversarial diagnose→critique→reconcile Workflow, synthesized
  into a Sonnet-authored fix plan, then ratified by Jordan's merge (ED-1094 merge-ratifies-by-default).
  **The combat-pacing question above turned out to be the wrong frame — demoted, not confirmed:** "two
  racing clocks" is refuted at gauge scale (C7's genuinely multi-subunit envelopment passes; a
  frozen-vs-wheeling-wings ablation, §2 step 4, is proposed to settle it definitively but not yet run).
  The actual ranked root cause is **composition-coupling defects in the pool/morale accounting layer**
  (RC-1, VERY HIGH confidence: a composed subunit's combat pool is scaled down per-pair while a
  single-subunit opponent rolls full pool into every simultaneous engagement; two subunits' independent
  morale triggers double-erode one shared parent pool; PER_CELL's casualty-fraction triggers use
  subunit-scale denominators) — and **the old PER_CELL=0 baseline that used to pass H3-H6 was itself an
  invincibility-bug artifact (RC-2, HIGH confidence), not a working model to restore.**
  **DG-3 and DG-4 RULED the same day (README.md §3 addendum) — AND IMPLEMENTED 2026-07-04, on
  `claude/mass-battle-cannae-gauge-dg-rulings` (PR #75):** DG-3's first implementation attempt (a flat
  divide-by-simultaneous-pair-count) was corrected same-session by Jordan's own follow-up feedback: "Combat
  pool for a subunit is misleading. It should be based upon combat pool per cell as per troop type/
  quality/density... bottom-up... solves issues with multiple engagements." Rebuilt as `core/exchange.
  pair_pool_contribution()` — redistributes a subunit's unchanged combat-SCORE across a specific contact
  pair by ACTUAL troop density in the engaged cells, plus depth-weighted support (reusing
  `support_engage_frac`'s falloff), instead of a flat post-hoc divide. DG-4 ("Subunit morale combination
  of own morale and overall morale; more likely to wilt if other subunits losing, more likely to rally if
  other subunits winning," Jordan verbatim) implemented as: `build_army` now defaults every subunit to its
  own real starting morale (closing the double-count by construction, reusing already-existing
  `agg_morale()`/`derive_rout()`/`cascade_morale_hit()` for whole-unit behavior); PLUS a new continuous
  per-phase sibling-pull term (`Subunit.pull_morale()` + `core/state.morale_check_phase`,
  `MORALE_SIBLING_PULL=0.15` tagged Class-B/Jordan-vetoable) that pulls each subunit's morale toward its
  living siblings' troop-weighted aggregate every phase. **Adversarial review (general-purpose agent)
  found 4 real bugs, all fixed:** `pair_pool_contribution` silently zeroed the pool for any
  continuous-scale (`troops=`/`concentration=`) subunit (recomputed the wrong, legacy tier-only cell
  pattern instead of iterating `cell_troops` directly — fixed); the sibling-morale pull could
  retroactively rescue a subunit from a same-phase rout its own casualties would have caused (reordered
  so self-erosion runs LAST, after a phase-start-snapshot-based pull, giving self-damage the final say);
  the same pull read already-mutated sibling values within one loop pass (Gauss-Seidel order bias — fixed
  via the snapshot); `build_army`'s morale-defaulting silently no-op'd on an explicit `morale: None` spec
  (dormant today, fixed). None of the 4 fixes moved 3 of the 4 `bat.py` digests; `cell_field` alone moved
  again and was re-recorded a second time.
  **DG-5 CLOSED — frozen-wings ablation (H3-H6, n=30, gauge scale):** wheeling and permanently-frozen
  wings produce statistically indistinguishable outcomes. **No maneuver-timing race exists, full stop**
  — the original "two racing clocks" theory this whole investigation started from is refuted at gauge
  scale, not just narrowly-surviving at fixture scope as the audit doc first suggested.
  **C4-vs-C7 fully explained:** varying only the defender's stance/discipline, `stance='hold'` alone
  accounts for the entire ~60-point gap; discipline contributes nothing.
  **Honest headline result — the DG-3/DG-4 fix did NOT close the targeted gap.** Gauge re-run (n=20):
  aggregate counts unchanged from the pre-fix baseline (single 2/20, multi 4/20), but the composition
  shifted (H1 newly fails at 60/40 vs its 42-58 band; C1 newly passes) — a trade, not a net gain. **H3,
  H5, H6 remain fully UNRESOLVED (100% draws)**; H4 (Cannae proper) improved from a decisive loss to a
  90%-draw non-resolution — still fails; C4 moved from the disclosed 0-13% toward 66.7% (still short of
  its 75-95 band, real but insufficient progress). **Reading: RC-1's accounting fix looks necessary but
  not sufficient — DG-1 (was the pinning-force composition ever historically ratified? it passed only
  under the now-confirmed RC-2 invincibility artifact) and DG-2 (a fighting-withdrawal/yield mechanic —
  the engine has no state between "eroding" and "routed") are the better-evidenced remaining levers, not
  a bug in this fix.** `test_envelop_reaches_rear_node`'s xfail reason/docstring updated to match (the
  old racing-clocks narrative retired, replaced with this finding). Verified: all 4 `bat.py` digests
  byte-exact against their re-recorded values (`cell`/`cell_field` needed a second re-record after the
  adversarial-review fixes; CI's reference-env-gated `test_byte_exact_cell_mode` caught a `cell`-mode
  drift local dev couldn't see, since that test only hard-fails in CI and silently skips elsewhere —
  a real process gap, now noted in `bat.py`'s own comment for next time); `tests/valoria` 87 passed/17
  skipped/1 xfailed. A real perf regression was found and fixed along the way (a redundant cell-
  coordinate conversion doubling per-pair cost) — profiling confirmed the DOMINANT remaining cost is
  pre-existing Stage-A TOI physics, not this fix; multi-subunit field-path battles now take ~1-4 min
  instead of seconds in `bat.py`'s own battery, disclosed not hidden.
  **Next action: Jordan's ruling on DG-1/DG-2 is the actual unblock — implementation work on this lane
  is otherwise done for this pass.** A separate, undiagnosed residual (RC-5) also surfaced: 9 of 20 gauge
  rows fail for reasons unrelated to composition coupling at all — flagged as its own not-yet-opened lane
  item, do not fold into this fix.
- **Mass battle — ED-MB-0003 (2026-07-05): 4 more real engine defects found+fixed, DG-1/DG-3 completed,
  DG-2 captured as a workplan doc, NOT implemented.** A fresh Fable-5-led adversarial audit of the
  already-shipped DG-3/DG-4 fix found the "RC-1 fully fixed, remaining gap is pure DG-1/DG-2" story was
  false: D1 (an outer army-size dilution multiplier double-diluting a composed subunit's pool, fixed by
  removing it per Jordan's ratified "intensive/partition-invariant" pool semantics), D2/D2b (a
  hysteresis-free limit cycle in `_envelop_goal` plus a step-freeze bug in `_node_advance` that together
  kept enveloping wings from ever actually reaching contact, both fixed), D3 (routed atoms resurrected to
  combat pool 1, letting them keep dealing damage post-rout — a first-pass fix turned out to be a no-op,
  since `roll_pool`/`_sigma_net_boost` both re-floor pool internally; corrected to force net=0 directly),
  D4 (`distribute_casualties` letting an uninvolved wing absorb a different subunit's casualties by
  column coincidence, fixed via per-subunit engagement scoping), plus a harness bug (`gauge_mb.py`'s
  envelopment/refused-flank army-builders fielding 3x/2x a single-subunit opponent's troops, a side
  effect of the LC-8 migration, fixed via force-parity `total_troops`). **Jordan ruled all 3 open gates
  (AskUserQuestion): DG-3 completion = intensive pool semantics; DG-1 = symmetric-at-parity (infantry
  rows) + majority-pin/cavalry-wing (C4/C7), matching Polybius/Livy order of battle; DG-2 = "create as
  workplan"** — captured as `designs/proposals/mass_battle_fighting_withdrawal_v1.md` (PROPOSED, not
  built). An independent adversarial-review pass caught 2 more real bugs (D3's no-op above; `wing_speed`
  never reaching `Unit.speed` since `Subunit` has no speed field) — both fixed. **Honest result: draws
  are entirely GONE across H3/H4/H5/H6/C4** (a genuine, dramatic change from the 100%-draw lock) **but
  every one of those rows now OVERSHOOTS its band decisively in the attacker's favor** instead of landing
  inside it (except C7, unaffected, still passing). Full 20-row gauge aggregate moved only marginally
  (4/20 → 5/20, multi mode — C1 newly passes; every other previously-failing row, including RC-5's 9
  untouched single-subunit rows, remains failing, now mostly via the same overshoot signature). **New,
  deliberately undecided finding:** a controlled experiment suggests `subunit_combat_pool`'s
  Command-driven score doesn't scale by a subunit's own troop share, so spatially-separated attacking
  fronts (a center + 2 wings) can each roll close to a full combat score against one defender at once —
  whether this is a genuine partition-invariance defect or the historically-correct mechanism for
  devastating encirclements (with the bands needing reconsideration instead) is flagged for Jordan's
  ruling, not silently tuned. DG-5 re-confirmed closed, for a corrected reason (the original ablation's
  wings never reached contact due to the now-fixed D2 bug, not because there was no race). All 4 `bat.py`
  digests re-recorded; `tests/valoria` 88 passed/16 skipped(numpy, unrelated)/1 xfailed. See
  `tests/coverage_matrix.md`'s 2026-07-05 entry for the full numeric record and ED-MB-0003 in the
  editorial ledger. **Next action: this is now a Jordan-ruling unblock on the new partition-invariance
  question and on DG-2's build sequencing — not further unprompted engine implementation.**
- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec
  RATIFIED (2026-07-02); HANDOFF split into per-lane files (2026-07-02).** The month's
  comprehensive review, the consolidation execution/reconciliation logs, and the single
  consolidated Jordan decision queue live at
  `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see `decision_queue.md`
  first — every gated item below is indexed there). Highest-leverage queued decisions:
  **doctrine ratification** (ED-1083, `designs/architecture/holonic_container_doctrine_v1.md`),
  **J-38 propagation-spec authorship** (workplan v5 §3 — unblocks conversion register #1 +
  `engine_clock`/ED-1051), Track-2 residuals (below), field-ON, the values_master
  regenerate-vs-retire call, and the duplicate compilation homes.
- **Scene-combat — merged (`d4bf2af3` PR #40, `8fbc4b66` PR #47); next up, all Jordan-gated:**
  1. **Two Track-2 residuals awaiting Jordan's single-source-target decision** (forward_roadmap Track 2;
     "Still open on `main`" above): (a) `wt`/`spd` cost-path de-leak (`core.py:55`, `systems.py:46`) — an
     autonomous before/after measurement harness can be prepped (roster-wide damage/tempo delta report) without
     flipping the live code; (b) `WP.reach()`/`authority()` vs `systems.reach_base`/`wield_heft` canonical-home
     fork (`weapon_physics.py:193,205`) — a short comparison doc of what each side currently computes and where
     they diverge can be prepped without touching code. Neither decision itself is agent-actionable.
  2. **Close the channel-leverage residual (the §C remainder, Phase 4c).** The affinity budget fixed
     total-competence but not per-channel leverage → spanish broad-strong, chinese broad-weak, only 2 niches. The
     fix is the **effectiveness-functions calibration**: measure each channel's marginal win-leverage, then
     normalise so each paradigm is decisive in *its* context (chinese-burst should win a fast/light-weapon
     context; german-bind the longsword context — currently it doesn't). **Design-laden** (how strong each
     paradigm should be = Jordan). Full detail: `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` §4c.
     Re-measure with `python designs/scene/combat_engine_v1/workbench/balance.py context`.
  3. **The abilities-as-access depth** (Phase 4b / REARCHITECTURE P4 / WS-4's other half): the 7 phase-slots +
     techniques-as-permission + the learning-gate ("can't bind-and-wind / Spanish footwork without having
     trained it"); resolves the dormant `eff_cw`. Carries open decisions flagged Jordan's: affinity
     full-point-buy vs thin, the cyclic node relation, naming. **Also gated: Phase 4a**, the full
     game-theoretic psychological layer (Bayesian-signaling reads, mixed-strategy feints, Stackelberg-timing
     initiative, two within-fight dynamics) — never built, and previously undocumented in the repo. Full detail:
     `designs/scene/combat_engine_v1/phase4_5_plan_v1.md` §Phase 4.
  4. **Tunable magnitudes** (Class-C, workbench-adjustable): `RECOVERY_TEMPO_K` (0.15), `LUNGE_*`,
     `CLOSE_REACH_REF`.
  5. **Phase 5 contact axis** (clinch/disengage/choke; consumes the dead `clinch` primitive) — full detail
     `phase4_5_plan_v1.md` §Phase 5 — and **WS-7 multi-combatant envelope** (gated on ED-911 ratification)
     remain design-gated, no immediate action.
  6. **Stale-branch cleanup (needs Jordan's confirmation before deletion):** `design/scene-combat-v1`
     (local+remote) and `origin/scene-combat-track2-cleanup` are fully merged and redundant. Do not delete
     unilaterally — switch the working branch to `main`, confirm no uncommitted work, then offer deletion as
     a separate explicitly-confirmed step.
- **Done this pass:** unified PR #18's net-new into main → **LB-22 complete** (orchestrator retired to
  `deprecated/skills/`; `valoria-vector-audit` read-path rewritten; `ci_hooks_verifier` Check 4 blocking
  for `skills/`). Earlier passes already landed the coverage_matrix single-source + 12-skill boilerplate
  strip (#16) — kept at main's version during the unify.
- **LB-22 residual (small):** `tools/` analysis utilities still carry `/home/claude` refs (WARN tier in
  `ci_hooks_verifier`); flip the `tools/` scope to blocking only after the GitHub-API→working-tree port
  (`freshness_gate`, `broken_dependency_checker`, `compliance_check`, `extract_*`, `valoria_collator`,
  `valoria_bulk_fix`). `valoria-orchestrator`'s old `tests/registry/test_descriptor_registry.py` import
  is dead (reads `/home/claude/…`, not CI-collected) — left as-is.
- **CI debt blocking-flips (LB-23) — reconciled 2026-07-01 (ED-1082):** `validate_ed_citations`
  is **already blocking** (since 2026-06-29, 0 genuine violations — the old "flip once triaged"
  action here was stale). `freshness_gate`'s remaining report-only step is being closed by the
  month-overview consolidation itself (pin refresh + blocking flip as its final commit); the
  optional K-2 SHA-split (115 `canonical_sha` fields → `references/canonical_freshness.yaml`)
  is a refactor that can follow independently, no longer a precondition.
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0 (index-routes).
- **Ledger-status reconciliation (LA-23, Lane A — mostly done):** flipped ED-841/842/912 `open`→`resolved`
  and filed the never-written ED-938/ED-939 (backfilled from #13; artifacts verified). Dropped the
  report-only `validate_ed_citations` count 748→731. **Residual:** ED-914 left `open` — its mechanical
  parts remain (PP-719 record-or-strike; dead `fieldwork_design_v1` parent-path refs in `params/bg/core.md`,
  `designs/scene/fieldwork_v30.md`, `designs/scene/fieldwork_godot.md`).
- **Design-tier docket awaiting Jordan:** J-31 extended (social-contest deliberative-game findings,
  row #39 → LA-19) and the new **J-36** (Key-bus closure for the 6 off-bus writers, row #40 — gated on
  the distillation report's deferred adversarial pass).
- **Mass-battle coordinate-field engine — Stages A–D merged (2026-07-02, PRs #52/#56); next up, all
  Jordan-gated.** Detailed continuity/history lives in the staged plan file (session-local, not in the
  repo tree): `using-opus-4-8-ultracode-floating-tiger.md`. All four stages are `FIELD_MOVEMENT=1`
  opt-in only — the grid path (`FIELD_MOVEMENT=0`, every existing scenario's default) stayed byte-exact
  throughout (`bat.py`'s frozen `unit`/`cell` digests unchanged across every commit in both PRs).
  - **A** — true-adjacency stand-off halt + an exact time-of-impact (continuous-collision) resolver
    (replacing an earlier halved-clamp heuristic), plus a reach-and-facing-asymmetric closing-budget
    throttle (a longer-reach, correctly-facing body "sets into formation" before a shorter-reach one).
  - **B** — facing/attention/reaction physics (anti-hyper-reactivity) on the field path.
  - **C** — command layer: `engine.build_army` (multi-subunit armies), a timed/conditional `Order`
    queue, and `escort_of`/formation-relative positioning.
  - **D** — wires the previously-inert `Subunit.role` (gated by `role_allowed`); new
    `engine.build_envelopment`/`build_refused_flank` realize ED-909's Unit-level "Envelopment"/"Refused
    Flank" postures as compositions of existing primitives (no new movement/combat mechanic).
  - **Open, Jordan-gated:** (1) **LC-8** — literally retiring `Horseshoe`/`RefusedFlank` as
    `Subunit.shape` values (`geometry.CELL_PATTERN_FN`/`config.MIN_DISCIPLINE`) would break the frozen
    `bat.py` grid digests (its own battery uses `Horseshoe` directly), so it needs an explicit
    sign-off + a deliberate re-baseline — deferred, not done in Stage D. (2) Stage E (Army
    Configuration Mode UI) needs a ruling on whether the videogame keeps the TTRPG's Command-rating
    subunit-cap hard limit of 3 or lifts it (`mass_battle_v30.md` §A.5) before it can be built; Stage E
    is also a genuinely different kind of work (frontend/UI over the now-complete engine primitives),
    not a natural default-continue from A–D. (3) Stage F (charge/depth/equipment physics) is only
    scoped at a high level in the plan — needs real design work before implementation.
  first — every gated cross-lane item is indexed there). For subsystem-specific continuity,
  go to your lane's file in the table above; `handoffs/HANDOFF_IN.md` carries the full
  cross-cutting/governance narrative (doctrine ratification, ED-<LANE>-NNNN namespace creation,
  merge-ratifies-by-default convention, ecosystem-review residuals not owned by another lane).
- **Reserved-ID state:** the flat `ED-NNNN` sequence is FROZEN at `ED-1094` (2026-07-02
  cutover, `ED-IN-0001`). All NEW EDs use `ED-<LANE>-NNNN` — `references/id_reservations.yaml`'s
  `lane_ids` section is the live allocation source; read `next_free` for your lane, allocate,
  bump, co-commit. Never max+1.
