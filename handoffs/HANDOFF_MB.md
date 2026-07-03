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
