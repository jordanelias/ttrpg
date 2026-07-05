# Handoff — MB (Mass Battle)

Lane-scoped continuity for the `MB` (mass battle) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

## Pending

(none beyond the items tracked under Next actions below.)

## Decisions

(none logged yet under this lane split — prior mass-battle decisions predate the lane-tagged
namespace and are folded into Next actions below, which carries the full narrative.)

## Next actions

- **Mass battle — Stages A–D + LC-8 landed on `main` (2026-06-30 → 2026-07-02, PRs #45/#52/#56/#57/#59).**
  Coordinate-field true-adjacency contact (Stage A), facing/attention/reaction physics (Stage B), the command layer
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
  `using-opus-4-8-ultracode-floating-tiger.md` if resuming this thread).
- **Three Jordan rulings landed 2026-07-02 (all executed same day):**
  1. **ED-1089** — `FIELD_MOVEMENT=1`/`PC_NODE_COHESION=1` are now the DEFAULTS (Stage A step 7 executed;
     "yes, field movement is default."); the grid stays the byte-exact oracle via explicit
     `FIELD_MOVEMENT=0 PC_NODE_COHESION=0` pins (the CI gate was updated from env.pop to explicit '0'
     pins — load-bearing, see `test_mass_battle_byte_exact.py`), and `bat.py`'s field digests were
     re-recorded (they had gone stale vs the LC-8 battery).
  2. **ED-1090** — videogame sub-unit cap is **11** ("subunits can be as high as 11."), lifting the
     TTRPG hard cap of 3; enforced in `engine.build_army`; open reconciliation flagged: Command clamps
     1–7, so >7 commanded subunits needs a future Command-exceeding mechanism (subordinate officers?)
     — future ED.
  3. **ED-1091** — the charge-recoil now zone-gates to the frontal (GREEN) arc (`PC_RECOIL_FRONTAL`,
     default ON; historical-validity condition verified against `mass_battle_gauge_grounding.md`
     §4.3/Burkholder before executing, per Jordan's "c7 if it is historically valid"); gauge row C7
     can now legitimately add a braced+enveloped variant (grounding doc §4.3/§5.7 still says "flagged,
     not fixed" — update on the next gauge pass).
- **Stage E MVP shipped, Stage F investigated (2026-07-02, PRs #62/#64/#65).** Army Configuration Mode
  (click-to-place deployment) landed as an MVP. Stage F ("Charge/Depth/Equipment Physics") was
  investigated before writing new physics code (ED-1092): speed-differential punctures and
  depth-absorption are already DONE; fidelity D1's zone half is done (ED-1091 above), the actor half
  remains OPEN (no canonical predicate exists for "actor-gate," flagged for Jordan); fidelity D2 was
  VERIFIED ALREADY CORRECT by direct numeric probe, no code change needed.
- **Still open:** Stage E's deeper UX beyond the MVP, and the rest of Stage F (actor-gate predicate,
  `PC_CHARGE_*` derive-not-assert — tracked separately as Track M Stage 5, the engine-wide
  calibrated-debt retirement sweep).
- **An orphaned-proposal audit (2026-07-02) also flagged:** `references/
  mass_battle_redesign_workplan_v1.md` is fully superseded (no banner exists — worth a supersession
  marker); `designs/proposals/multiunit_envelopment_plan.md`'s cross-**Unit** spatial envelopment
  ("Path B") is a materially different, still-unbuilt mechanism from the Unit-level `build_envelopment`
  that landed — don't conflate "Envelopment shipped" with "Path B shipped."

## Catch-up (2026-07-04) — this file fell behind; see root HANDOFF.md for the fuller narrative

This lane file wasn't kept in sync since the entries above (predates ED-MB-0001). Condensed summary of
what's landed since, in order — full detail lives in root `HANDOFF.md`'s mass-battle block and
`tests/coverage_matrix.md`'s dated entries:

- **T1-T4 charge-recoil ruling (ED-1095)** executed; **movement/pathing audit (ED-1096)** found
  `envelop`/`sweep`/`wheel`/`kite` only worked on the legacy grid path, unreachable on the live default
  node path since ED-1089's field-movement flip.
- **ED-MB-0001 (2026-07-02, PR #66, merged):** the movement/pathing fix-plan executed end-to-end —
  waypoint primitive gives `_node_advance` real per-tick steering for `envelop`/`sweep`; `PER_CELL`
  default flipped 0→1 (gate 4). Disclosed, not chased: enabling `PER_CELL`'s fatigue/attrition mechanics
  made the H3-H6 Cannae-pattern gauge rows collapse (0-13% losses vs. a 45-72% expected band) — landed
  as a loud `xfail` on `test_envelop_reaches_rear_node`, flagged as the next investigation.
- **ED-MB-0002 (2026-07-04, PR #73 audit + PR #75 ratification):** a Fable-led Workflow diagnosed the
  H3-H6 collapse as composition-coupling defects in the pool/morale accounting layer (RC-1), not the
  "two racing clocks" theory the xfail's own docstring proposed (refuted by gauge row C7). Jordan ruled
  DG-3 (bottom-up per-cell pool split — corrected mid-session from an initial flat-divide attempt per
  Jordan's own "per-cell troop density... bottom-up" feedback) and DG-4 (a blend of per-subunit and
  whole-unit morale, with continuous sibling-pull, wiring already-existing `agg_morale`/`derive_rout`/
  `cascade_morale_hit` machinery). Both implemented on `claude/mass-battle-cannae-gauge-dg-rulings`; all
  4 `bat.py` digests re-recorded (expected — touches shared, non-gated combat-resolution code);
  `tests/valoria` 87 passed/17 skipped/1 xfailed (after an adversarial review found and fixed 4 real
  bugs: a pool-zeroing bug for continuous-scale subunits; a same-phase-rout-masking ordering bug and a
  Gauss-Seidel sibling-aggregation bug in the new morale pull, both fixed by snapshotting siblings and
  running self-erosion last; a dormant `morale: None` footgun in `build_army`). **DG-5 CLOSED**: a
  frozen-vs-wheeling-wings gauge ablation (H3-H6) shows byte-identical outcomes — no maneuver-timing
  race exists at all, refuting the original "two racing clocks" theory outright, not just narrowly.
  C4-vs-C7's gap is fully explained by `stance='hold'` alone (discipline contributes nothing).
  **Honest result: the DG-3/DG-4 fix did NOT close the targeted gap.** Gauge re-run (n=20): aggregate
  pass counts unchanged (single 2/20, multi 4/20) but composition shifted (H1 newly fails, C1 newly
  passes); H3/H5/H6 remain fully unresolved (100% draws); H4/C4 show real but insufficient movement
  toward their bands. RC-1's accounting fix looks necessary but not sufficient — DG-1 (was the
  pinning-force composition ever historically ratified, given it only passed under the now-confirmed
  RC-2 invincibility artifact) and DG-2 (a fighting-withdrawal/yield mechanic) are the better-evidenced
  remaining levers. `test_envelop_reaches_rear_node`'s xfail reason/docstring updated to retire the
  superseded racing-clocks narrative and record this finding instead. **Next action: this is now a
  Jordan-ruling unblock (DG-1/DG-2), not further engine implementation.** RC-5 (9/20 gauge rows failing
  for unrelated reasons) remains a separate, not-yet-opened lane item.

- **ED-MB-0003 (2026-07-05): follow-up Fable-5 audit found 4 more real defects; Jordan ruled all 3
  gates; DG-2 captured as a workplan, not built.** The "RC-1 fully fixed" story was false — D1 (an
  outer army-size dilution multiplier double-diluting a composed subunit's pool, removed per Jordan's
  ratified "intensive/partition-invariant" semantics), D2/D2b (`_envelop_goal`'s hysteresis-free limit
  cycle + `_node_advance`'s step-freeze bug, together the actual reason wings never reached contact —
  both fixed), D3 (routed atoms resurrected to pool 1; first-pass fix was a no-op per adversarial
  review, corrected to force `a_net`/`b_net=0` directly since `roll_pool`/`_sigma_net_boost` re-floor
  pool internally), D4 (`distribute_casualties` cross-subunit column-leak, fixed via per-subunit
  scoping), plus a harness force-ratio bug (`_envelop_army`/`_refused_army` fielding 3x/2x a
  single-subunit opponent's troops, fixed via `total_troops` force parity). **Jordan's rulings
  (AskUserQuestion): DG-3 completion = intensive pool semantics; DG-1 = symmetric-at-parity (infantry)
  + majority-pin/cavalry-wing (C4/C7, Polybius/Livy order of battle); DG-2 = "create as workplan"** —
  `designs/proposals/mass_battle_fighting_withdrawal_v1.md`, PROPOSED, NOT implemented. Independent
  adversarial review caught 2 more real bugs (D3's no-op; `wing_speed` never reaching `Unit.speed`) —
  both fixed. **Honest result: H3/H4/H5/H6/C4's draws are entirely GONE, but every row now OVERSHOOTS
  its band decisively in the attacker's favor** (except C7, still passing). Full 20-row gauge: 4/20 →
  5/20 (C1 newly passes; RC-5's 9 rows untouched). **New, deliberately undecided finding:**
  `subunit_combat_pool`'s Command-driven score may not scale by troop share, letting spatially-separated
  attacking fronts each roll near-full combat strength against one defender at once — genuine defect or
  historically-correct mechanism (with bands needing reconsideration)? Flagged, not silently tuned.
  DG-5 re-confirmed closed for a corrected reason (D2's bug, not a genuine non-race). All 4 `bat.py`
  digests re-recorded; `tests/valoria` 88 passed/16 skipped(numpy)/1 xfailed. See
  `tests/coverage_matrix.md`'s 2026-07-05 entry + ED-MB-0003. **Next action: Jordan's ruling on the new
  partition-invariance question and DG-2's build sequencing — not further unprompted implementation.**
