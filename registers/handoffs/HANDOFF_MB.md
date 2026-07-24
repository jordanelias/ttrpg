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

- **ED-MB-0018 (2026-07-23): octagon facing = DAMAGE-RECEIVED MULTIPLIER + reaction delay + multi-side
  shock** (Jordan directive, verbatim: "the facing octagon is a damage-received multiplier — attacks from
  behind do ~**2×** the damage of from the front; cells **cannot turn instantaneously** (needs a couple-tick
  reaction); attacked from **multiple sides** is **extra bad**, not just divide-by-two"). Replaces the legacy
  `-2`-dice octagon **pool** penalty (too weak: legacy rear was only 1.25× front). New `_octagon_dmg_mod`
  (orchestration.py) → pure per-cell facing arc (front **1.0×** / flank **1.5×** / rear **2.0×**) multiplying
  the defender's casualties; reads the arc against the **LOCAL** attacker centroid (`OCTAGON_LOCAL_REACH=2.0`)
  so a wide line's wing stays GREEN head-on — **verified front→1.00×, rear→2.00× exactly per-seed**. Reaction:
  a cell hit outside its front arc keeps its exposed facing until `FACING_REACTION_TICKS=2` elapse, and only
  refuses if it can SEE the threat (≤105° FOV) and isn't frontally pinned — a **rear** strike is blind → 2×
  persists the whole engagement. Multi-side: `eng_counts≥2` → `×(1+MULTI_SIDE_SHOCK=0.5)` compounding.
  `PC_OCTAGON_DMG` **default ON**; legacy path preserved **byte-exact** under `=0` (the wrapper/pocket/roll-up
  pool machinery goes dormant under the flag — subsumed by arc + shock). Compounds with frontal-brace
  stripping → a braced front that parries to 0 is annihilated from behind (Cannae). **All 4 bat.py goldens
  re-recorded** (grid+field; head-on single-subunit rows all-GREEN→unchanged; envelop/cannae/oblique move).
  `test_octagon_damage.py` (5). Disclosure: `audit/2026-07-22-mass-battle-stress-test/octagon_damage_model.md`.
  **Follow-on:** graded ≥2/3/4-side escalation; full-campaign A/B of the default-ON flip once ED-MB-0016
  friction + the conjunctive-envelopment gate land (all three interact on the envelopment rows).

- **ED-MB-0017 (2026-07-22): multi-unit deployment geometry + envelopment pathing fix** (Jordan-flagged
  from the hierarchy snapshot: overlapping subunits, both envelopment wings on one side, refused flank
  level with the line). Root cause: `build_army` deployed subunit i at `col=15+i*4` (fixed step < subunit
  frontage). Fixed with frontage-aware anchor-centred deployment (`_centered_line_cols`, fit-to-field, no
  overlap 1–11 subunits), symmetric opposite-flank envelopment wings (mirror double envelopment), and an
  echeloned-back refused wing. **Speed (Jordan):** envelopers must be fast — `PC_ENVELOP_SPEED_MULT=2.0`
  (envelop maneuver) + `PC_CAVALRY_SPEED_MULT` 2.0→3.0 (cavalry ~3× infantry); cavalry double envelopment
  now wraps behind by ~t6–8 (was t16–20). Independent adversarial critic run: F1 over-wide crash + F2
  gauge_mb same-defect FIXED, F3/F4 tested. Machine-vision comparison + sources saved to
  `research/diagrams/mass_battle_formations/`. All 4 bat.py goldens re-recorded (3 multi-subunit rows
  re-baselined, ED-909 precedent; 7 single-subunit unchanged; byte-exact green). `test_deployment_geometry.py`
  (16). **Follow-on:** the wrap seals a horseshoe not a full ring (no cavalry rear-transit); single line only
  (no triplex depth-lines); envelopment still often loses the outcome (DG-6 "envelopment not rewarded" —
  ED-MB-0016 friction + a still-needed conjunctive envelopment gate; this fast correct wrap is its precondition).

- **ED-MB-0015 (2026-07-22): spatial-model v2 Stage F — verification + golden re-record + P-DEC-4
  historical revalidation.** All I1–I7 hold; stress harness S0–S5 green; Lanchester exponent + depth-2
  preserved; field goldens re-recorded (`unit_field 2da5183…` verified, `cell_field 5f5db96…`; grid
  unchanged). **P-DEC-4:** gauge pre-D baseline (A–C) = **10/20**, v2 (A–E) = **6/20** multi — D+E moved
  it down 4 rows (authorized re-baseline, but material; see `stage_F_verification.md` §5). Dominant
  failure = **DG-6 over-decisiveness**, root-caused: melee pool sums N independent dice → CV collapses
  ~1/√N → `compute_degree` deterministic from force ratio → 100%/0% vs historical bands. **Now being
  RESOLVED** (Jordan directive 2026-07-22: extend code to resolve standing issues via academic research /
  military theory / mathematics / historical precedent) — the DG-6 grounded resolution (restore
  scale-invariant outcome variance so a large advantage is decisive-but-uncertain/banded) is UNDERWAY as
  a follow-on ED-MB, built on stochastic-Lanchester/breakpoint models + Sabin's *Lost Battles*
  decisiveness bands. **Stage G (retire integer engine)** remains after: note the field engine lives in
  `tests/sim/mass_battle` (not `systems/`), so routing `resolve_mass_battle` (`systems/mass_battle/sim/
  massbattle.py`, called by `systems/factions/sim/faction_action.py:_try_conquest`) onto it needs a
  faction→army adapter + outcome→`{degree,attacker_wins}` mapping + likely a field-engine relocation —
  an architecturally-significant, cross-lane (MB+FA) epic.

- **ED-MB-0014 (2026-07-22): spatial-model v2 Stage E — weapon-class reach + the `pike` troop type.**
  Per `spatial_model_v2_plan.md` §3 Stage E / Jordan P-DEC-1. `reach_for`/`TROOP_TYPE_REACH` now return
  the per-type front-face reach (non-pole 0.1 / pole 0.2 / **pike 0.3** / lance 0.2 / ranged 0.1 sidearm),
  replacing the flat `REACH_SHORT=0.5` placeholder Stages B/C carried; feeds `cell_boxes_for →
  obb_front_reach_overlap` + the TOI halt. Authored the **`pike`** troop type end-to-end (stats mirror
  heavy_infantry — reach 0.3 the sole differentiator, provisional-by-analogy since §B.2 has no pike row;
  pike weapon + ('pike','medium') loadout + ShieldWall/Hold/Anvil roles). **Reach advantage emerges** via
  the already-wired charge-recoil reach gate: braced pike/spear (reach ≥ lance 0.2) repel a cavalry charge
  (defender ~96.7% hp, cavalry recoils ~88.3%), levy (0.1) is run down (~90.7%) — the anti-cavalry pike
  role, emergent from the reach data. **Disclosed finding:** reach differentiation does NOT change
  symmetric standing melee (mutual exchange once contact fires; reach only shifts timing) — reach is a
  charge/brace lever, not a standing-melee one. A directional-reach exchange term (pike-pins-forever
  hazard under halt-on-contact) is flagged for Jordan, NOT introduced. Gates green:
  `test_reach_weapon_class.py` (10); **I4 byte-exact grid oracle green** (no kite in the battery). Two
  items flagged for Stage F: (1) the 0.1/0.2/0.3 scale vs PP-290's 0.5/1.5 meter-grounding needs
  reconciliation (deferred, not overwritten); (2) **P-DEC-3 cavalry density cap (< infantry) deferred** as
  a separate follow-up (kept out of Stage E to keep the reach A/B clean). Next: **Stage F** (full
  verification + field-golden re-record + historical revalidation), then **Stage G** (retire the integer
  `systems/mass_battle/sim` engine, route `resolve_mass_battle` onto the field engine — P-DEC-2 resolved).

- **ED-MB-0013 (2026-07-22): spatial-model v2 Stage D — the LAST live integer on the field contact
  path removed.** Per `audit/2026-07-22-mass-battle-stress-test/spatial_model_v2_plan.md` §3 Stage D.
  The melee Lanchester frontage term `len(set(int_col))` (the only integer left on the live position/
  contact path, per `backwards_analysis.md`) is now a CONTINUOUS OBB front-overlap **width**:
  `geometry.engaged_frontage(a_boxes, b_boxes, heading)` = the union length, along a side's frontage
  axis, of each engaged cell body's width-interval clipped to the enemy's covered meeting span.
  `_find_contacts_standoff` threads `a_front`/`b_front` onto pairs; `_lanchester_strength(front_width=…)`
  consumes it, falling back to the integer count on the grid/OFF path (**I4 byte-exact — grid oracle
  green, 30 passed**). **Scoping call:** the snapped `(rank,file)` cell identities are KEPT — they key the
  formation-lattice casualty/density/stamina substrate (a discrete troop-block identity, I3's
  defensible-quantization carve-out, NOT a live-position integer); only the frontage MAGNITUDE moved to
  continuous. Gates green: `tests/valoria/test_frontage_conservation.py` (15) — integer-limit reduction,
  fractional on offset, depth-invariant, frontage-capped (Lanchester linear), I1 conservation ×5 seeds,
  I2; maneuvers/movement/yield 20 passed/1 xpassed (pre-existing). **DG-6 disclosure (not tuned):** A/B
  12-seed field battery — axis-aligned symmetric meetings byte-identical; shift only on offset/asymmetric
  meetings (Line4-vs-Line2 wide-attacker overkill capped to the narrow defender's meeting width, A_win
  12→10/12, def hp .452→.487). Lanchester melee exponent unchanged (p=2.50 before/after — pre-existing
  DG-6 artifact, frontage-independent). **Field goldens NOT re-recorded (Stage F, per plan §7).** Next
  in this v2 sequence: **Stage E** (weapon-class reach 0.1/0.2/0.3 + author the `pike` troop type, P-DEC-1;
  P-DEC-3 cavalry density cap), then **Stage F** (full verification + digest re-record + historical
  revalidation), then **Stage G** (retire the integer `systems/mass_battle/sim` engine, route
  `resolve_mass_battle` onto the field engine — P-DEC-2 RESOLVED=retire).

- **ED-MB-0011 (2026-07-22): DG-10 field-movement freeze FIXED + full field-based stress test.**
  Jordan asked for a field-based (not grid) stress test with all flags/gates activated on the
  *active* engine (`tests/sim/mass_battle/`, NOT the wired `systems/mass_battle/sim/` bare port,
  which has none of these flags). The stress test surfaced the dominant field-path defect: `_node_advance`
  floored any sub-Discipline-5 body's velocity to 0 (`floor(1×0.7)=0`), so the MAJORITY of canonical
  troop types (levy/light_inf/heavy_inf/archers/crossbow/sling/artillery, all disc<5 per §B.2) NEVER
  advanced to contact on the live field path — every such battle a vacuous 0-casualty draw. This is
  **DG-10** (opened by ED-MB-0007) generalized: the continuous-velocity accumulator meant to prevent it
  was wired only into the legacy grid `advance_cells` and sat dead there. **Jordan ruled in-session**
  ("fields, not grids. no grids." / "if it's broken and not commensurate with system, disable" / "what
  even is the point of the continuous velocity accumulator?"): the `math.floor` is the grid-snap the
  field exists to remove; the accumulator is itself just a Bresenham workaround. **Fix:** on the FIELD
  path `step` is now the real velocity (no floor, no accumulator) — anchor/pos are already floats and
  the sole consumer moves by `min(step,mag)`; whole velocities stay int so disc≥5 rows are byte-exact,
  fractions (disc<5) advance the float anchor at their true 0.7 cells/tick. **Legacy GRID path
  untouched** (gated on `if FIELD_MOVEMENT`) → CI byte-exact grid oracle still passes (2 passed). Field
  goldens (bat.py cell_field/unit_field, NOT CI-checked) re-recorded: mirror/ranged byte-identical, the
  8 decisive rows change because a unit degrading below disc-5 MID-battle used to freeze and now keeps
  moving (trace: wedge seed 0 → disc 3). maneuvers+yield: 12 passed/1 xpassed. **Scope: MOVEMENT only** —
  it shifts the 20-row Cannae balance gauge (frozen units now fight), which is the **DG-6-gated**
  calibration surface; NOT a balance claim, no balance constant tuned. Stress harness + full findings:
  `audit/2026-07-22-mass-battle-stress-test/` (S0 wiring: all 30 MECHANICS resolve; S1 fuzz: 0 engine
  failures / 77.7% contact / 1-of-197 minor cell-vs-hp accounting drift on a clean unit; S3: 12/16 gates
  proven WIRED by A/B, 4 inert-on-scenario incl. by-design-exempt PC_BRACE_SETUP_DELAY; S4: PC_FACING_MODEL/
  FIELD_CONTACT/REFORM_CHECK all SAFE when activated; S5: determinism + perfect mirror symmetry).
  **Next for this lane:** (1) the residual cell-vs-hp accounting drift (RC-1 family, 1/197 clean units)
  and the fragile envelopment-shock validators (V-SHOCK/V-BRACE proxy ≈0) are both DG-6-layer, Jordan-
  gated; (2) DG-6 itself (the resolution-architecture calibration) remains the open highest-leverage gate.

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
  marker); `proposals/multiunit_envelopment_plan.md`'s cross-**Unit** spatial envelopment
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
  `proposals/mass_battle_fighting_withdrawal_v1.md`, PROPOSED, NOT implemented. Independent
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

- **ED-MB-0004 (2026-07-08): partition-invariance fix landed; RC-5 preliminary finding; DG-2 build
  in progress.** Jordan ruled (AskUserQuestion): partition-invariance = **"genuine defect — fix it"**;
  DG-2 = **"build it now"**; RC-5 triage = **start now**. Fixed `subunit_combat_pool`'s Command-driven
  score being troop-count-independent per atom in a way that let >=2 of one side's atoms simultaneously,
  fully engage the SAME single opposing atom (a pinning center + 2 wings converging on one Line/Arrowhead
  defender — H3-H6/C4/C7's exact shape) each roll near-full base_pool, multiplying total dice by the
  convergence-group size for identical total troops. New `core/exchange.py:_pair_engaged_troops` +
  `orchestration.py:_convergence_scale`/`PC_CONVERGENCE_NORM` (default ON) renormalize any such group to
  what ONE merged atom of the combined troops would contribute; verified live via direct trace (fires on
  1446/1686 sampled ticks of an H3-style battle, max group size 3 — not a no-op). All 4 `bat.py` digests
  re-recorded (shared, non-gated code). `tests/valoria`: 112 passed/57 skipped/1 xfailed/0 failed (the 7
  `test_names.py` failures seen locally are PRE-EXISTING and unrelated — confirmed via `git stash`
  bisection, an environment/fixture issue). **Honest result:** gauge re-run (multi, n=60) shows the fix
  does NOT move H3-H6/C4's win/loss/draw split at all (bit-for-bit identical to the pre-fix baseline) —
  the defect was real and is now closed, but was never the dominant lever for these rows' overshoot
  (envelopment/charge-shock morale collapse dominates). Full 20-row gauge unchanged (single 2/20, multi
  6/20). **RC-5 preliminary finding (diagnostic only):** a controlled A/B-slot-swap test on 3 pairs
  (Arrowhead/Line, GappedLine/Line, GappedLine/Arrowhead) found an inconsistent slot-dependent asymmetry
  that tracks neither a uniform side bias nor shape hierarchy (a true Line-Line mirror stays near-even,
  17/13 of 30, ruling out a blanket engine-wide bug) — likely shared ingredient (not traced further):
  `ANCHOR_MAP`'s per-shape deployment column (Line=9/Arrowhead=8/GappedLine=7) applied regardless of
  which side carries that shape, so differently-shaped sides deploy at different absolute columns. Next
  concrete lead for RC-5, not claimed solved; the other 6 rows (H7,H8,R1,R3,C1,C3,C5) untouched. Full
  record: `tests/coverage_matrix.md`'s 2026-07-08 entry + ED-MB-0004 (now resolved).

- **ED-MB-0005 (2026-07-08): DG-2 fighting-withdrawal/yield mechanic — commanded-entry slice built.**
  Per Jordan's "build it now" ruling, built exactly the proposal doc's own §4 step-1 scope: `Subunit.
  yielding`/`yield_active` (discipline-gated, melee-only), a `'yield'` order (composes with existing
  Order/check_orders — `yielding` added to `_ORDER_SAFE_FIELDS`), movement (`_yield_goal`, reuses
  `_kite_goal`'s flee vector, capped 1 cell/tick, node/field path only — same scope as envelop/sweep),
  facing-lock (fires regardless of `PC_FACING_MODEL`, the mechanically load-bearing "faces the enemy,
  unlike rout" distinction), combat-pool malus (`YIELD_POOL_MULT`, reuses `PC_SHOCK_HOLD_BRACE`=0.35),
  and anti-abuse (no volleying while yielding). Both new magnitudes (`D_YIELD=3`, `YIELD_POOL_MULT`)
  flagged `[CALIBRATED-DEBT]`, not independently derived, per the doc's own §5. All 4 `bat.py` digests
  confirmed BYTE-IDENTICAL (genuinely inert-by-default, no re-record needed). New
  `tests/valoria/test_mass_battle_yield.py` (9 tests, all green); full `tests/valoria` suite green, no
  regressions (123 passed/56 skipped/1 xfailed/6 pre-existing-unrelated `test_names.py` failures).
  **NOT built this pass (disclosed):** emergent auto-entry, rally exit, pocket exit — only the free
  "collapse to routed" exit exists (needed no new code).
  **Honest measurement:** center-yields-from-tick-0 (n=20, node path) raises center hp retained
  35.8%→40.6% (the mechanism works) but collapses the attacking army's win rate 70%→0% — an
  unconditional, whole-battle yield trades far more offense than it recoups. Not a broken mechanic;
  Cannae's yield was TIMED, this pass didn't build/measure timed entry — flagged as the natural next
  experiment. Full record: `tests/coverage_matrix.md`'s second 2026-07-08 entry + ED-MB-0005.
  **Next actions for whoever continues this lane:** (1) a timed/conditional yield-entry experiment
  (Order `tick:N` trigger, or emergent entry keyed to encirclement progress) to see whether a properly
  time-boxed yield recovers the army-level win-rate cost while keeping the center-survival benefit;
  (2) RC-5's other 6 untriaged rows (H7,H8,R1,R3,C1,C3,C5) plus tracing the ANCHOR_MAP deployment-column
  asymmetry lead to a root cause; (3) DG-1's composition question and the still-live envelopment-shock
  magnitude remain the larger unaddressed levers for H3-H6's overshoot (the partition-invariance fix
  closed a real defect but was never the dominant one there).

- **ED-MB-0006 (2026-07-08): combat pool abandons Command entirely — troop type/quality/numbers.**
  Per Jordan's direct instruction ("consider abandoning combat pools being related to the commander,
  and instead being solely derived from the subunit troop type, quality and numbers"), new
  `POOL_QUALITY_MODEL` (default ON): base pool = `eff_power × eff_size × POOL_QUALITY_SCALE` —
  troop-TYPE quality (`TROOP_TYPE_STATS`/§B.2) × NUMBERS (troops/BLOCK_SIZE), no Command anywhere.
  `POOL_QUALITY_SCALE=0.5` renormalizes to the historical baseline magnitude. Discipline/stamina
  penalties unchanged. Command still governs morale/formation-speed/orders/`derive_rout`, just not
  the dice pool. Applied consistently to both `subunit_combat_pool` and `Unit.base_combat_pool`
  (pursuit path). `COMMAND_SIGMA_ENABLED` branches remain selectable (`POOL_QUALITY_MODEL=0`) for
  A/B. All 4 `bat.py` digests re-recorded; `tests/valoria` 121 passed/57 skipped/1 xpassed (the
  usual pre-existing `test_names.py` failures aside).
  **Honest, mixed gauge result:** 6/20→7/20 (multi). C4/C5 newly pass (bigger-force cavalry rows
  correctly reward numbers now); **H4 (actual Cannae) flips from attacker-WIN-OUT to attacker
  LOSING badly** (1.7%/65%/33% draws) — composed-army rows lose out because their PER-ATOM numbers
  are now smaller than the single consolidated defender's, an real emergent trade-off, not a bug.
  **Open, disclosed residual:** `lanchester_signature.py`'s law-exponent check (melee should conserve
  p≤1.4) fails under BOTH models — pre-existing baseline already measured p≈1.55 (previously
  undetected, unrelated to this change) and a separate apparent "2:1 army loses 97% of the time"
  reading that a quick trace suggests may be test-methodology noise (single 18-tick `run_battle`
  call rarely resolves decisively at this ratio), not independently confirmed. The new model measures
  p≈2.50, tested extensively (sqrt-numbers variant, 8-point scale sweep) without finding a scale that
  reaches ≤1.4 — plateaus at p≈1.65-1.7, confirmed NOT a Lanchester double-count (disabling
  `LANCHESTER_ENABLED` doesn't change the exponent at all) — the amplification is internal to how
  larger absolute pools reduce variance and make `compute_degree`'s discrete tier assignment
  near-deterministic from the pool ratio alone. **Next action: this needs the degree/damage-tier
  discretization or the Lanchester coefficient's own interaction reconsidered — not another pool-
  formula scale tweak (provably can't fix a ratio-sensitive test).** Full record: `tests/
  coverage_matrix.md`'s third 2026-07-08 entry; canon note in `designs/provincial/mass_battle_v30.md`
  §A.1 (ED-MB-0006).

- **ED-MB-0007 (2026-07-08): full 11-surface agonist-antagonist gauge architecture audit — why
  7/20, and what to do about it.** Per Jordan's direct instruction to investigate "from all
  directions and surfaces" (widened mid-session to explicitly add movement/pathing/routes/
  strategies/tactics/stances/reach, then ranged weaponry), two Workflow waves (7 + 4 surfaces;
  producer → isolated adversarial critic → opus-4.8-max synthesis per wave, then a third
  opus-4.8-max combination pass) fielded 24 subagents across ~1288 tool calls. **Full record:**
  `designs/audit/2026-07-08-mass-battle-gauge-architecture-audit/README.md` (+ `01_wave1_synthesis.md`/
  `02_wave2_synthesis.md` for per-wave detail). **Honest result:** the 13 nominal failures decompose
  to ~9 genuinely-deep engine divergences (C3/H9 are n=60 sampling noise; R1/R3 are
  harness-construction failures). Two mechanisms dominate, both causally proven by reversal
  ablation: **E1**, a cell-count/density plumbing defect (`geometry.py`'s two unreconciled
  cell-count generators → a static, never-recomputed `Unit.ncells` → the Lanchester density term)
  that reverses H3/H10 outright when patched; and **D1**, the super-linear resolution architecture
  ED-MB-0006 already flagged, now measured at melee exponent **p≈3.2 under the live PER_CELL=1
  path** — worse than ED-MB-0006's disclosed p≈2.50, which turns out to have been measured under
  the WRONG `PER_CELL` setting by `lanchester_signature.py`'s own hardcoded default. **These two are
  multiplicative, not competing, and neither alone lands a row in-band — this investigation is
  diagnostic, not curative**, disclosed as a first-class finding. **Granularity directive verdict:**
  the per-cell quality/type axis (veteran-front/levy-rear) is confirmed byte-inert for all 20 rows
  by four independent lines of evidence — a legitimate future architecture, not a gauge fix. The
  per-cell COUNT axis is already the #1 defect (E1). Troop-grounded speed and the entire
  ranged/volley pool were never brought under `POOL_QUALITY_MODEL` and remain ungrounded. **New
  empirical result** (found by the wave-2 synthesis's own probe, not present in either wave in
  isolation): the two cheapest-looking fixes for the ranged rows (R1: correct archer stats; R3:
  the `kite` instruction) are **mutually incompatible** — a correctly-statted discipline-3 archer
  computes a live movement step of exactly zero (no fractional-velocity accumulator on the node
  path), so `kite` cannot rescue a unit physically unable to move. This reverses an earlier reading
  that had listed a ranged-`hold` variant as a safe, contained fix — it is not; it is gated on
  **DG-10**. Ten new engine defects (E1-E10) and a harness-artifact cluster identified and bucketed
  (full detail + file:line citations in the audit README). **Eleven new Jordan-ruling decision
  points opened: DG-6 (the resolution-architecture calibration itself — the deepest, highest-
  leverage call) through DG-16 (tactical/role-layer grounding).** DG-numbering note: an earlier
  combination draft had reused DG-1..DG-5 for these new gates, colliding with the ALREADY-RULED
  namespace from ED-MB-0002/0003/0005 — caught and corrected to the DG-6..DG-16 sequence above
  (crosswalk in the audit README's Appendix). **Not yet implemented:** this ED closes the
  investigation itself; the ~10-item safe-to-fix list and all eleven DG-6..DG-16 rulings remain
  open follow-up work, gated primarily on Jordan's ruling on DG-6.
  **[CALIBRATED-DEBT] flagged, not resolved:** the currently-passing cavalry rows (C4, C5, C7) may
  be passing partly on the same E1/D1 artifacts targeted for removal — the pass count is not
  confirmed monotonic in fixes applied. **Next action for whoever continues this lane: DG-6 first**
  (it gates the highest-leverage fix and several other rulings) — either via Jordan's direct ruling
  or an `AskUserQuestion` pass through DG-6..DG-16 in priority order, then land the safe-to-fix list
  paired with whichever DG-6/DG-7 direction is chosen, then re-run the full 20-row gauge (no surface
  in this audit ran the complete battery — only directional/single-row causal evidence exists for
  any proposed fix).

---

## 2026-07-24 — "Nothing is golden" campaign: Part-A flips + Part-B fixes (IN PROGRESS)

Jordan directive: *"implement all proposals. nothing is golden here."* The byte-exact golden constraint
is LIFTED — goldens become a re-recorded regression snapshot; the **honest gauge is now the primary
oracle**. Full steering doc + 6-phase plan: `audit/2026-07-22-mass-battle-stress-test/full_implementation_plan_v1.md`
(committed). Per-troop damage primitive (Jordan): troop = sub-cell isolate carrying weapon/quality/intent/
morale; density is LINEAR; the σ-head resolves per-troop quality → degree; count scales magnitude. This
resolves B4 = casualties-only-linear (behind a toggle). Decisions locked: PC_ flags KEPT; rotation DEFERRED.

**WORKING-TREE STATE (uncommitted): B1 applied to `tests/sim/mass_battle/geometry.py`** — the
`_oriented_abs_map` node branch now iterates `_oriented(atom)` (the continuous footprint _node_pos is keyed
by) and SKIPS absent ids instead of defaulting misses to origin `(0,0)`. **Verified:** H2 wedge decA
0.0 → 37.5 (audit predicted ~33). ✅

**CRITICAL COUPLING FOUND (do not commit B1 alone):** measuring the FULL gauge after B1 shows the
braced-wall C-rows REGRESS — C2/C6 `REPELLED` → `NOT-REPELLED` (cav wins 87.5% vs a braced wall), net
gauge 5/20 → 4/20. Root: the brace-repel silently relied on the broken `(0,0)`-collapsed contact map
feeding charge-shock / `_wall_prep` / `_defender_depth`; and the octagon-damage path
(`_per_cell_angle_mod`/`_octagon_dmg_mod`, orchestration ~L1156, zone binning ~L1021-1066) is STILL on the
dead `starting_position + cell_offsets` lattice (B3, unfixed) — so after B1 the contact map and the
octagon map DISAGREE. **The geometry frame (B1 + B2 + B3) and the B5 charge-zone fix are COUPLED through
the contact map and MUST land as ONE coherent set, measured together.**

**NEXT ACTION (resume here):**
1. B3 — route `_per_cell_angle_mod`/`_octagon_dmg_mod` onto the same live `_node_pos` identity map (kill
   the dead spawn-lattice open-code at geometry.py ~L259-262 path for these functions).
2. B5 — derive the charge/recoil zone (`_zb`/`_za`, orchestration L1021-1066) from the TRUE arc
   (`a_arc`/`b_arc`) not the `PC_REFUSE`-bundled `angle_mod`.
3. Re-measure the full gauge with B1+B3+B5 together; confirm C2/C6 return to REPELLED AND H2 stays fixed.
4. B2 — rebuild `col_grid` from live file bins per tick + re-center ANCHOR_MAP (H7/H8 fatigue-immunity).
5. Only when the frame set is NET-POSITIVE on the gauge: re-record bat.py goldens (4 modes) as the new
   baseline, update the byte-exact digest tests, run pytest, commit + ledger (ED-MB-0034), PR.

### 2026-07-24 continued — B1+B3 verified correct but NET-NEGATIVE on gauge alone (frame must land whole)

**Verified this increment (code preserved as `audit/2026-07-22-mass-battle-stress-test/frame_step1_B1_B3.patch`,
working tree reverted to keep the branch clean / avoid committing a gauge regression):**
- **B1** (geometry.py `_oriented_abs_map` node branch): iterate `_oriented(atom)`, skip absent `_node_pos`
  ids (no `(0,0)` default). **H2 wedge decA 0.0 → 40.0** ✅ (audit predicted ~33).
- **B1-grid** (same fn, grid branch): iterate `_oriented(atom)` not `oriented_pattern(shape,tier)` — matches
  `cell_offsets` keying (units.py: "_oriented is the sole source of the offset"); byte-identical for legacy
  troops=None. Makes `_oriented_abs_map` the SINGLE identity map. Add `_oriented_abs_map` to geometry `__all__`.
- **B3** (orchestration.py `_octagon_dmg_mod` L903 + `_per_cell_angle_mod` L748): replace the open-coded
  `abs_to_orig` (dead `starting_position+cell_offsets` lattice) with `abs_to_orig = _oriented_abs_map(defender_subunit)`.
  Live `_node_pos` on the field path; byte-identical on grid. H1 mirror → 52.5 (IN BAND).
- **make_unit** (gauge_mb.py): added `width`/`depth` params → spec (for deep-formation rows).

**KEY FINDING — the brace-repel (C2/C6) gap is DEEPER than B1/B3/B5:** with the contact map fixed, a braced
LINE cannot cleanly repel a charge. The reciprocal charge-recoil is depth-gated (`_wall_prep = _disc_prep ×
_depth_prep`; `_depth_prep(1)=0`, `(2)=0.33`, `(3)=0.67`), but the density-matched gauge units are only 2
ranks. Scaling depth at EQUAL FORCE: cav-win 62% (d2) → 40% (d6) → 70% (d8) — depth helps but a narrow-deep
line gets FLANKED by the wider wedge (envelopment), so it never cleanly repels. **A repelling formation is a
SQUARE/BOX (all-around brace), not a frontal deep line.** So C2/C6 need: (a) **B5** (charge/recoil zone from
the true arc, not the PC_REFUSE-bundled angle_mod), AND (b) a **box/square brace primitive** (all-around
facing), AND (c) gauge C-rows scaled up (bigger, deeper, fair force). The old brace-"repel" was an ARTIFACT
of the broken `(0,0)`-collapsed contact map — B1/B3 correctly remove it and expose the real gap.

**Full gauge with B1+B3 alone = 4/20 (was 5/20)** — net -1 because C2/C6 flip (brace-model gap) while the
H-rows improve directionally but aren't yet in band (need B2 + the brace/box work). **CONCLUSION: the
geometry frame (B1+B2+B3) + B5 + the box-brace primitive + the gauge C-row rescale must land as ONE
net-positive set — no piecemeal geometry commit reaches net-positive.** Next increment: apply
`frame_step1_B1_B3.patch`, then build B2 (col_grid live), B5 (arc zone), the box-brace primitive, and the
gauge C-row rescale together; measure the full 20-row gauge; re-record 4 goldens; land as ED-MB-0034.
