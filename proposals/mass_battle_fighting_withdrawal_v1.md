# Fighting-Withdrawal / Yield Mechanic — Design Workplan (DG-2)

## Status: PARTIALLY SUPERSEDED — the §4 step-1 yield scope is BUILT (ED-MB-0005, 2026-07-08; tests/valoria/test_mass_battle_yield.py, 9 green). Live record = registers/handoffs/HANDOFF_MB.md. Residual (emergent auto-entry §2.2; rally/pocket exits §2.4; D_YIELD/YIELD_POOL_MULT calibration debt) tracked there, HELD. [## Status: heading added 2026-07-15]

**Status: PROPOSAL — pending Jordan sign-off before implementation.** Not canon yet. Date 2026-07-05.
Ratified scope for THIS document (Jordan, 2026-07-05): *"Create as workplan"* — i.e. this doc captures
the design, it does **not** implement the mechanic. Implementation is a future session's work, gated on
this doc's ratification.

**Lane:** MB (mass battle). **Governing decision gate:** DG-2, first scoped in
`designs/audit/2026-07-04-mass-battle-cannae-gauge-audit/README.md` (ED-MB-0002). This doc supersedes
that audit's brief DG-2 sketch with a full design, informed by a follow-up Fable-5 adversarial audit
(2026-07-05) and this session's own implementation work on DG-1/DG-3's remaining gaps (D2-D4 below).

---

## 0. Why this exists (the gap it closes)

Every state the mass-battle engine tracks for a fighting body falls into exactly two buckets today:

- **Eroding** — a subunit/unit takes casualties, morale/fatigue/cohesion degrade continuously via
  graded curves (`_morale_sigma`, `_fatigue_sigma`), but it fights at full tactical commitment the whole
  time.
- **Routed** — `Unit.derive_rout()` fires (command≤0, or all subunits routed, or `agg_morale()<=0`), and
  the *entire* unit flips `routed=True` **atomically, in one call**: every subunit's combat pool is
  force-zeroed (`Unit.base_combat_pool` / `subunit_combat_pool` both `return 0` the instant `routed` is
  true), every subunit's facing flips to point away from the enemy (`PC_FACING_ROUT`), and the tick loop
  that resolves the engagement **breaks immediately** (`run_battle`, `if unit_a.routed or unit_b.routed:
  break`) — no further ticks execute for that engagement pair at all.

There is **no state in between.** A body either holds at full commitment or, the instant its morale
crosses zero, disintegrates completely in a single tick — no partial withdrawal, no fighting retreat, no
"give ground in good order." Historically, Hannibal's Cannae center did not do either of these things: it
was **designed thin and deliberately traded ground**, absorbing the Roman advance in an ordered, costly,
*slow* withdrawal that bought the time for the wings to close the encirclement — a body that is neither
fully committed nor broken. The engine cannot express this at all today, and per RC-4 of the
2026-07-04 audit, this is a **design gap**, not a bug: nothing is broken, something is simply missing.

**This gap was flagged as the second-most-likely remaining lever (after DG-1's composition question) for
why the Cannae-pattern gauge rows (H3-H6) fail their historical bands.** A 2026-07-05 follow-up session
(see §7) fixed several real engine defects and re-measured: the Cannae rows' **draws are now gone
entirely**, but they overshoot decisively in the attacker's favor instead of landing in the historical
band — meaning DG-2 is **not currently the binding constraint** on those specific rows (see §7's honest
disclosure). DG-2 remains real and worth building for its own sake — historical fidelity to Cannae's
actual tactical content — but it should not be expected, on its own, to be the thing that closes H3-H6's
band gap; a separate, deeper combat-pool-scaling question (§7) is now the better-evidenced lever there.

---

## 1. The mechanism this design rejects, and why

The 2026-07-04 audit's own DG-2 sketch proposed *"converting net-success differential into displacement
via the existing recoil/knock-back idiom."* A follow-up adversarial pass (2026-07-05) checked this against
the actual codebase and found **no such displacement primitive exists.** `PC_CHARGE_RECOIL`
(`config.py`) is purely a **net-success penalty** applied in `resolution.py`'s combat-degree math — it
never moves a cell. The only literal positional displacement anywhere in the engine is
`resolve_cross_side_contention`'s one-step shift-back for two cells caught at the exact same coordinate
(a collision-resolution mechanic, not a combat-outcome one). Reaching for "the recoil idiom" was reaching
for a familiar name, not a real mechanism — building on it would have meant inventing a brand-new
displacement primitive while calling it a reuse, exactly the kind of unacknowledged new-mechanic-in-
disguise this repo's discipline exists to catch.

**The honest carrier is the movement layer**, which already has the right idioms for exactly this kind of
directed, goal-seeking motion:
- `Subunit._kite_goal`'s reflect-through-anchor flee vector (`hierarchy/units.py`) — already computes
  "move away from the threat, along the line from threat through self."
- The TOI (time-of-impact) / standoff-halt substrate (`resolve_toi_and_commit`,
  `_pair_toi_scale`) — already governs how far a body may safely move in one tick without passing through
  an enemy.
- Stance gating (`STANCE_SPEED_MOD`, the `stance == "hold"` early-return in `_node_advance`/
  `advance_cells`) — already the precedent for "a stance changes how (or whether) a body's anchor moves
  this tick," which is exactly the shape a new `yielding` state needs.

No new movement primitive needs inventing; a `yielding` state needs to *compose* these three existing
mechanisms, the same way `escort_of` composed the centroid-tracking + facing-rotation machinery Stage C
already built.

---

## 2. The proposed mechanic

### 2.1 State

A new **per-subunit** state, `yielding: bool = False`, alongside the existing `routed`/`broken` fields on
`Subunit` (`hierarchy/units.py`). Default `False` — inert/byte-exact for every existing subunit and every
existing scenario that never enters it.

**The defining difference from rout: facing is preserved toward the enemy.** A yielding body is still
*fighting*, just giving ground — it has not turned its back. This is mechanically load-bearing: since
`octagon_angle`'s zone gating (GREEN/YELLOW/RED) is a pure function of facing vs. the attacker's position,
a yielding body that keeps facing the threat stays in its own GREEN/YELLOW arc against a pursuer directly
in front of it — the RED-zone rear-shock multiplier (`PC_SHOCK_REAR`, ~10x `PC_SHOCK_FRONT`) and the
`_shaken`-amplifier death-spiral (`PC_SHOCK_SHAKEN_GAIN`) stay capped **unless** the pursuer maneuvers to
its flank or rear — which is exactly the mechanical reward this design gives to a wrapping envelopment
(the wings' whole reason to exist) while NOT collapsing a body that is simply falling back in good order
under frontal pressure.

### 2.2 Entry

Two paths, gated by `eff_discipline >= D_YIELD` (a new threshold — magnitude explicitly **not** proposed
here, see §5):

- **Commanded** — a new `'yield'` order/instruction (composes with the existing `Order`/`check_orders`
  timed-sequencing primitive from Stage C), the deliberate Cannae-center tactic: a general who has planned
  a thin, sacrificial center orders it to give ground from the start or from a timed trigger.
- **Emergent** — at a phase boundary where today's §A.4 casualty-fraction triggers would otherwise push a
  subunit toward the morale-erosion cliff (`core/state.py`'s `morale_check_phase`), a subunit whose
  `eff_discipline >= D_YIELD` and whose parent `Unit.command > 0` enters `yielding` instead of continuing
  the un-braked erosion spiral toward rout; a subunit below the discipline gate erodes/routs exactly as
  today (no change to the low-discipline case). **Ship this path OFF by default at first release** (see
  §4) — it changes rout dynamics in every scenario, not just Cannae rows, and needs its own dedicated
  measurement pass before going live broadly.

### 2.3 While yielding

- **Movement**: reuses `_kite_goal`'s reflect-through-anchor vector (away from the nearest engaged enemy
  centroid), capped by the TOI/standoff substrate exactly like any other movement (so a yielding body
  cannot outrun a genuinely faster pursuer, and cannot pass through friendly/enemy bodies) — **at most 1
  cell/tick**, deliberately slower than a normal advance, so it can never simply disengage cleanly; it is
  *giving ground*, not fleeing.
- **Combat**: fights at a combat-pool malus (magnitude TBD, §5) — reduced but nonzero, matching "traded
  ground at a cost," not "stopped fighting." No volleying while yielding (matches the existing
  `'kite'`/ranged-posture precedent that a body actively repositioning doesn't also fire).
  Fatigue/stamina continue to drain normally.
- **Facing**: locked toward the nearest engaged enemy (not the flee-away vector `_kite_goal` itself uses
  for movement) — this is the mechanical crux of §2.1's "still fighting, not fleeing" distinction; a
  yielding body's MOVEMENT vector and FACING vector are deliberately decoupled, unlike a routing body
  where both point away together.

### 2.4 Exit

Three termination paths:

- **Rally** — at a battle-turn boundary, if morale has recovered above the entry threshold and no
  pressure (no active engaged pair) is present, reverts to normal `stance`/combat.
- **Collapse to routed** — morale falls to `SUBUNIT_ROUT_FLOOR` (or `agg_morale()<=0` at the Unit level)
  regardless of yielding state; the existing `derive_rout()` path fires exactly as today. Yielding is a
  *delay*, not an escape, from rout.
- **Pocket** — if rearward movement is structurally blocked (map edge, a friendly body occupying the only
  retreat path, or an enemy body that has gotten behind it), yielding converts to a hold with the combat
  malus *removed* — this is Cannae's actual kill condition (the center pinned in place with nowhere left
  to give ground, annihilated in place) emerging for free from the existing standoff/collision substrate,
  not a scripted "surrounded" flag.

### 2.5 Anti-abuse gating

- **Melee-only** — ranged troop types already have `kite`; `yielding` is not a second kiting mechanic for
  archers to exploit for permanent standoff.
- **No volleying while yielding** (see §2.3).
- **Speed capped below any realistic pursuer's closing speed** (1 cell/tick ceiling) — a yielding body
  cannot indefinitely maintain a standoff gap against a pursuing enemy the way a true kiter can; it is
  designed to eventually be caught, consistent with "trading ground for time," not "escaping."
- **Cumulative ground given is bounded** by ED-MB-0001 §6's already-Jordan-ratified path-budget formula
  (`0.5 × speed × max-ticks-in-battle`) — reused verbatim, no new constant invented for this purpose.
- **Stamina keeps draining** while yielding (§2.3) — no free rest from repositioning.

### 2.6 Interaction with DG-4's sibling-morale pull

A yielding subunit is **not** `routed`, so `morale_check_phase`'s existing sibling-snapshot logic
(`core/state.py`) still includes it in the troop-weighted aggregate every other subunit pulls toward — the
army correctly *feels* its center bending under pressure (a yielding center drags nearby subunits' morale
down somewhat, exactly the "more likely to wilt if other subunits losing" dynamic Jordan ratified for
DG-4) without any new code: this composes with already-shipped machinery, it does not need new wiring.

---

## 3. What this design reuses vs. invents (accounting, per this repo's anti-fabrication discipline)

| Piece | Reused from | New? |
|---|---|---|
| Directed movement away from a threat | `_kite_goal`'s reflect vector | Reused verbatim |
| Standoff/collision safety while moving | `resolve_toi_and_commit`/`_pair_toi_scale` (TOI substrate) | Reused verbatim |
| Timed/conditional entry | `Order`/`check_orders` (Stage C) | Reused verbatim |
| Cumulative-ground bound | ED-MB-0001 §6 path-budget formula | Reused verbatim |
| Zone-gated shock response | `octagon_angle`/`PC_SHOCK_FRONT`/`PC_SHOCK_REAR`/`PC_SHOCK_SHAKEN_GAIN` | Reused verbatim (facing-preservation is what KEEPS a yielding body in this reused machinery's favorable zone) |
| Sibling morale coupling | DG-4's `pull_morale`/sibling snapshot | Reused verbatim (no new wiring — inclusion is automatic since `yielding != routed`) |
| `yielding: bool` state flag | — | **New** (one boolean field, default-inert) |
| `'yield'` order/instruction | — | **New** (composes the existing Order primitive with a new instruction string) |
| Combat-pool malus magnitude while yielding | — | **New value, needs derivation or explicit calibrated-debt flag** (§5) |
| `D_YIELD` discipline threshold | — | **New value, needs derivation or explicit calibrated-debt flag** (§5) |
| Facing/movement-vector decoupling | — | **New logic** (small, but genuinely new — nothing today separates a subunit's facing target from its movement target) |
| "Pocket" conversion (blocked retreat → brake-removed hold) | Emerges from existing standoff/collision detection | Reused substrate, new INTERPRETATION (no new collision code, just a new response to an existing condition) |

---

## 4. Sequencing / rollout

1. **Build the state + commanded-entry path only.** No emergent auto-entry yet. This is the lowest-risk
   slice: a general can deliberately order a subunit to yield; nothing about existing scenarios' rout
   dynamics changes, since nothing enters `yielding` unless explicitly ordered.
2. **Measure H4 specifically** (Cannae proper — envelopment vs a single defending body — the row this
   mechanic is most directly aimed at) with a hand-authored scenario that orders a thin center to yield,
   before/after, to see whether the mechanic produces the intended "center survives longer, buys time for
   the wings" effect without needing the emergent path at all.
3. **Only after that measurement**, consider the emergent auto-entry path (§2.2) as a separate, explicitly
   flagged, default-OFF addition — it is the part of this design with the largest blast radius (touches
   rout dynamics in every scenario, not just deliberately-yielding ones) and interacts with RC-5's still-
   undiagnosed single-subunit gauge failures (§7) in an unknown way.
4. Every step: full 4-mode `bat.py` digest re-record (expected — this is new, non-inert state once used),
   `tests/valoria` green, adversarial review before considering any step "done," matching this lane's
   standing discipline.

---

## 5. Explicitly NOT decided here — needs empirical validation, not design-table judgment

- **`D_YIELD`'s magnitude** — what discipline threshold gates access to yielding at all. No existing
  primitive derives this; it needs either a grounded derivation (e.g. tied to the existing `MIN_DISCIPLINE`
  per-shape table's own logic) or an explicit `calibrated-debt` flag per this repo's provenance
  discipline (§5 of CLAUDE.md / the Track M provenance ledger), not a bare invented number.
- **The combat-pool malus magnitude while yielding** — same status; needs derivation from a primitive
  (e.g. tied to the existing brace/shock discount idiom, `PC_SHOCK_HOLD_BRACE=0.35`) or flagged debt.
- **Whether emergent auto-entry should ever ship as default-ON** — an empirical question (does it help or
  hurt the OTHER 8 currently-failing gauge rows, particularly RC-5's undiagnosed single-subunit rows?),
  not something to decide from the design table.
- **Whether this mechanic, once built, actually closes any part of H3-H6's remaining band gap** — per §7,
  it is currently NOT the binding constraint on those specific rows; building it is justified on
  historical-fidelity grounds (RC-4) independent of whether it moves those particular gauge numbers, and
  its effect (if any) on them should be measured honestly, not assumed.

---

## 6. Acceptance criteria for a future implementation session

- `bat.py` all 4 digest modes: byte-exact-OFF preserved (this state is opt-in/inert by construction); a
  new digest recorded once the commanded-entry path is exercised by any scenario.
- New unit tests: (a) a yielding subunit's facing stays locked toward its engaged enemy even as it moves
  away; (b) a yielding subunit fighting a purely frontal pursuer never enters the RED octagon zone; (c) a
  yielding subunit that gets flanked/enveloped DOES enter YELLOW/RED normally (the mechanic doesn't
  accidentally grant blanket immunity); (d) the "pocket" conversion fires correctly when retreat is
  blocked; (e) cumulative ground given respects the ED-MB-0001 §6 path-budget bound; (f) a yielding
  subunit cannot outrun a same-speed pursuer indefinitely (no infinite-kiting exploit).
- A hand-authored H4-style scenario (thin yielding center + wings) measured before/after, reported
  honestly regardless of outcome.
- Adversarial review pass before merge, per this lane's standing discipline.

---

## 7. Context this doc's numbers are grounded in — 2026-07-05 follow-up session

The same session that produced this doc also fixed 4 concrete engine defects unrelated to DG-2 itself,
found by a follow-up Fable-5 adversarial audit of the already-shipped DG-3/DG-4 fix (ED-MB-0002):

- **D2** — `_envelop_goal`'s phase-1/phase-2 transition had no hysteresis (same threshold for entry and
  exit), producing a permanent limit cycle where a wing wheels to its rear waypoint, turns in, immediately
  re-crosses the threshold, and gets yanked back to phase 1 — forever. Fixed with a one-shot commitment
  latch.
- **D2b** — `_node_advance`'s per-tick step magnitude could freeze a body forever within a small fixed
  distance of any goal (a fixed integer step that doesn't evenly divide the remaining distance, combined
  with a `mag >= 0.5`-or-nothing movement gate). Fixed by capping the step at the remaining distance so a
  body always closes the exact gap instead of freezing short or perpetually overshooting.
- **D3** — a routed/broken subunit's combat pool was resurrected to a floor of 1 by an unconditional
  `max(1, ...)` guard, letting it keep dealing real damage for many ticks after routing. Fixed to force 0
  for a dead atom regardless of any residual float noise.
- **D4** — `distribute_casualties` tracked engaged columns as ONE union across a whole Unit, letting an
  uninvolved, far-away subunit (e.g. a wide-placed wing) absorb a share of a DIFFERENT subunit's (e.g. the
  center's) casualties purely because their absolute columns happened to overlap. Fixed to scope
  engagement per-subunit.

Plus two Jordan-ratified decisions were implemented: **the intensive (per-troop, partition-invariant) pool
semantics** (removing an outer army-size dilution multiplier that was double-diluting composed subunits'
pools) and **DG-1's composition ratification** (force-parity + majority-infantry-pin/cavalry-wing
composition for the envelopment/refused-flank gauge army-builders).

**Honest result of all of the above, together:** the Cannae-pattern gauge rows' 100%-draw lock is
**broken** — H3/H4/H5/H6/C4 now resolve decisively almost every time, a genuine and dramatic change from
the prior "nothing ever happens" state. But they now **overshoot** their historical bands in the
attacker's favor (WIN-OUT, saturating near 100% where the bands expect a moderate 45-95% range depending
on the row) rather than landing inside them — except C7, which lands cleanly at the top of its wide 65-100
band. A controlled, isolated experiment (co-located vs. spatially-separated equal-troop subunit splits,
both vs. an identical single-subunit opponent) confirms the likely mechanism: `subunit_combat_pool`'s
combat score is driven by shared Command + per-subunit discipline/cohesion/stamina, **not scaled by the
subunit's own share of the army's total troops** — so an army split into multiple *spatially separated*
attacking fronts (a center + two wings, each engaging the single defender from a different angle) can
each roll close to a full, independent combat score against that ONE defender simultaneously, tempered
only by a small, already-flagged-as-insufficient `ENCIRCLEMENT_PENALTY` tax that in this configuration
falls on the *defender*, not the attacker. Whether this is (a) a genuine partition-invariance defect that
needs its own fix (scaling `subunit_combat_pool` by troop share) or (b) the CORRECT emergent mechanism for
why real encirclements are so devastating, and the *bands themselves* need reconsidering, is a **new,
unresolved architecture question this session deliberately did not decide** — it is beyond the scope of
the already-ratified DG-1/DG-3/DG-4 decisions and needs its own dedicated Jordan ruling, not a silent
magnitude tweak. The full 20-row gauge aggregate moved only marginally (4/20 → 5/20 passing, multi mode,
n=30) — this is not a straightforward net improvement or regression, it is a change in *which* rows fail
and *how* they fail (draws → overshoot for the composed-army rows; the 9 RC-5 single-subunit rows remain
failing, now also mostly via overshoot rather than their prior mixed signatures). See
`tests/coverage_matrix.md`'s 2026-07-05 entry and `registers/handoffs/HANDOFF_MB.md` for the full numeric record.
