# Spatial Model v2 — Euclidean motion + boxed (OBB) footprints, honest facing/frontage/depth/reach

**Status: PROPOSED (max-effort implementation plan). Jordan-directed 2026-07-22.** Supersedes the
circular-cell contact model for the FIELD engine. Companion to `geometric_contact_proposal_v1.md`
(the argument) and `backwards_analysis.md` (the trace that scopes it).

**Ruling captured:** "do facing, frontage, depth, reach honestly. Euclidean motion, boxed footprint."
Decided-open items (P-DEC) are listed in §9 — none block the early stages.

---

## 0. Target model (precise)

A **cell** is a rigid **oriented rectangle (OBB)** of troops:
- **centre** `(r, c)` — continuous float (no snapping, ever, on the live path).
- **facing** `θ` — unit heading vector (already tracked as `cell_facing_vec`, continuous).
- **footprint** = width `w` (along-front / frontage) × depth `d` (front-to-back / rank thickness),
  in lattice units. Nominal standard cell: `w = d = 1` (area 1; a unit square is the OBB special
  case). `CELL_RADIUS = 0.5` is retained only as the half-extent of the standard square
  (`w/2 = d/2 = 0.5`), not as a circle radius.
- **area = w·d**; **density = troops / area** (at 1×1, density = troop count — the ratified reading).
- **weapon reach** `ρ` extends the **front face only** (anisotropic): the engagement envelope is the
  OBB grown by `ρ` on the +facing edge, `0` elsewhere. Reach by weapon class (§9 P-DEC-1):
  non-pole 0.1 / pole 0.2 / pike 0.3 / ranged = projectile band.

**Motion** stays **Euclidean**: a cell advances `v` (float) lattice units/tick along its heading;
`v = base_speed · disc_mult (+ stance) (× cavalry)` from the DG-10 fix. No diagonal (Chebyshev)
speed-up. Standard `v = 1 = one cell length/tick` ("fully displace per tick").

**Collision / contact** is **OBB overlap** (Separating-Axis Theorem, or the cheap reduced form for
axis-near-aligned small boxes), with the front-face reach extension. Replaces
`hypot(Δ) ≤ CELL_RADIUS+reach…` (isotropic circle) with box-vs-box overlap.

**Two metrics, on purpose:** motion = Euclidean; body/collision = box. This is the design.

---

## 1. Invariants / non-negotiables (adversarial guard rails for every stage)

- **I1 Conservation:** `Σ cell_troops == hp` for every non-routed/broken unit, every tick (the
  codebase's own volley-test invariant). Never create/destroy troops.
- **I2 Determinism:** same seed + inputs ⇒ identical public outcome, byte-for-byte.
- **I3 No integers on the live field path** for position/contact/contention (the goal). Magnitude
  floors on troops/damage/dice are out of scope (defensible quantization).
- **I4 Grid oracle untouched:** `FIELD_MOVEMENT=0` byte-exact path is frozen; CI
  `test_mass_battle_byte_exact.py` stays green. All v2 work is field-path-only, gated on `FIELD_MOVEMENT`.
- **I5 No silent balance tuning:** every gauge-moving change is A/B'd, disclosed, digest-re-recorded;
  the 20-row Cannae gauge is DG-6-gated — we report shifts, we do not tune constants to a target.
- **I6 Symmetry:** mirror (identical formation both sides, order-cancelled) stays ~0 skew.
- **I7 Reach ⇒ facing:** a cell facing away gets no reach bonus (preserve `_effective_reach`'s rule
  in the OBB form: reach extends the front face, which points where the cell faces).

Each stage below must re-establish I1–I7 (or explicitly, loudly, record an approved change to I5/gauge).

---

## 2. What already exists (leverage, don't rebuild)

| capability | where | reuse in v2 |
|---|---|---|
| continuous float positions | `_node_pos`, `cells_float()` | the OBB centre |
| continuous facing vector | `cell_facing_vec`, `octagon_angle` | the OBB orientation θ |
| facing-gated directional reach | `_effective_reach(base_reach, facing_vec, dr, dc)` | becomes front-face growth |
| Euclidean motion / velocity | `_node_advance` (DG-10 float step) | unchanged — motion metric stays Euclidean |
| geometric halt / no co-location | `resolve_toi_and_commit`, `standoff` | halt at OBB-touch instead of circle-touch |
| geometric contention (already) | field path `resolve_cross_side_contention` = no-op; TOI does it | keep; make TOI OBB-aware |
| frontage / depth mechanics | `_lanchester_strength` (cols), `col_grid`, `_formation_depth` (pattern) | feed from OBB extents |

**Consequence (from `backwards_analysis.md`):** the ONLY live integer left is the engaged-cell
**recording** (`contact.py:292-293`) → frontage/casualty columns. Everything else is already float or
a no-op. So v2 is mostly *upgrading shape fidelity* (circle→OBB) on already-geometric machinery, plus
deleting that one recording snap.

---

## 3. Staged implementation (dependency-ordered; each stage = trace → build → adversarial → gate)

### Stage A — OBB primitive + standard dimensions (foundation, no behaviour change)
- Add `CellBox(cr, cc, w, d, theta, reach_front)` value type + `obb_overlap(a, b)` (SAT) and
  `obb_front_reach_overlap(a, b)` helpers in `geometry.py`. Pure functions, unit-tested in isolation.
- Standard dims `w=d=1`; derive from `footprint_for`/troops later.
- **Trace:** consumers = none yet (dormant). **Adversarial:** property tests — overlap symmetric,
  translation/rotation invariant, reduces to the circle test within tolerance for axis-aligned unit
  boxes at reach 0. **Gate:** new tests green; zero behaviour change (nothing calls it yet).

### Stage B — contact decision on OBB (swap the circle test)
- In `_find_contacts_standoff`, replace `hypot(Δ) ≤ standoff_from_reach(...)` with
  `obb_front_reach_overlap(boxA, boxB)`; boxes built from `cells_float()` centre + `cell_facing_vec`
  θ + standard dims + `_effective_reach`-derived front reach.
- **Trace all directions:** feeds `find_contacts` → `resolve_engagements` (who fights) and the engaged
  set; also `resolve_toi_and_commit` halt radius must match (Stage C) or cells overlap/gap.
- **Adversarial:** (a) does every pre-v2 contact still fire (no missed engagements)? (b) does a
  flank/rear approach now engage *earlier/later* correctly (directional reach)? (c) I1/I2/I6.
- **Gate:** fuzz (0 engine failures, I1 holds), mirror symmetry, and a **directional contact test**
  (pike reaches before sword head-on; neither reaches sideways).

### Stage C — TOI halt on OBB (motion stops at box-touch, not circle-touch)
- `resolve_toi_and_commit` currently caps each cell's advance at the circular `standoff`. Recompute
  the time-of-impact against the **OBB front face** along the Euclidean velocity ray (ray–OBB / expanding-
  box test). Motion stays Euclidean; only the *stop condition* becomes the box.
- **Trace:** halt distance must equal Stage B's contact trigger (or cells interpenetrate / stall short).
  Depends on Stage A/B.
- **Adversarial:** cells never interpenetrate (no overlap > ε post-commit); no permanent stall
  (bodies that should reach contact do); charge closing speed preserved (cavalry still reaches).
  I1/I2.
- **Gate:** trace a charge + a shieldwall meeting; assert touch-not-overlap and no freeze; fuzz.

### Stage D — frontage & depth from OBB extents (delete the last integer: `contact.py:292-293`)
- Replace the `int(round)` engaged-cell recording with the **OBB-overlap-derived engaged frontage**:
  Lanchester `n_eng_cols` becomes the total overlapping **front width** (Σ box-front overlap length /
  standard width), not `len(set(int_col))`. Casualty distribution keys on the same continuous frontage
  partition. Depth continues to come from `col_grid`/pattern (immune — confirmed), now cross-checked
  against OBB depth extent.
- **Trace all directions:** `_lanchester_strength` (frontage), `distribute_casualties` (columns),
  `_defender_depth` (col match), density (`ncells`). This is the balance-moving stage.
- **Adversarial:** I1 conservation under the new partition (hardest check — casualties must still sum);
  frontage is bounded by the meeting width (Lanchester stays *linear*, never square — the law's core
  guarantee); depth-2 no longer "collapses" because frontage is continuous overlap, not integer cells.
- **Gate:** conservation fuzz; the depth-2 experiment (must preserve); Lanchester-signature exponent
  check (melee stays ≤ its bound); **A/B the 20-row gauge** and record the shift (DG-6, disclose).

### Stage E — weapon-class reach wired to the front face
- Add `WEAPON_CLASS[troop_type] → reach` (P-DEC-1 map) feeding the OBB front reach. Ranged unchanged.
- **Trace:** `_effective_reach`/`standoff` now read weapon reach not the flat `REACH_SHORT`.
- **Adversarial:** pike-vs-sword reach advantage emerges (measure); a facing-away cell still gets no
  reach; ranged unaffected. I1/I2.
- **Gate:** reach-advantage test; fuzz; A/B gauge (disclose).

### Stage F — full verification, digest re-record, disclosure
- Re-run: `tests/valoria` (byte-exact grid green = I4), maneuvers/yield, the stress harness S0–S5,
  the depth-2 experiment, Lanchester signature, conservation fuzz (n≥300).
- Re-record field goldens (`cell_field`/`unit_field`) — grid goldens unchanged (I4).
- Write the balance-shift A/B into the audit + ED-MB ledger; flag the gauge delta for DG-6.
- **Final adversarial pass:** independent re-trace outcome→inputs (as in `backwards_analysis.md`)
  confirming no integer remains on the live position/contact path, and I1–I7 all hold.

### Stage G — wired engine (`systems/mass_battle/sim`) reconciliation
- The wired engine is integer-grid end-to-end (no `_node_pos`, no CELL_RADIUS, integer `cell_offsets`,
  integer contact). It cannot host OBBs in place. Two options (P-DEC-2):
  1. **Route `resolve_mass_battle` onto the v2 field engine** and retire the integer engine (preferred;
     the honest "no grids" endgame; larger but deletes a whole grid engine).
  2. Port the OBB model into the wired engine (duplicative; keeps two engines).
- Until decided, the wired engine keeps the ED-MB-0011 DG-10 clamp (disclosed grid stopgap). Stage G
  is gated on P-DEC-2 and is the biggest single step.

---

## 4. Order, parallelism, dependencies

```
A (primitive) → B (contact) → C (TOI halt) → D (frontage/casualty) → E (reach) → F (verify+record)
                                                                                   → G (wired reconcile, gated on P-DEC-2)
```
A is prerequisite for all. B and C are tightly coupled (must agree on the touch surface) — build
together, gate together. D is the balance-moving core. E is additive on D. F gates the merge. G is a
separate epic.

---

## 5. Test architecture (new, per stage)

- `test_obb_primitive.py` — SAT overlap + front-reach properties (Stage A).
- `test_contact_directional.py` — pike>sword head-on, no side/rear reach, contact fires (B/E).
- `test_toi_no_interpenetration.py` — post-commit overlap ≤ ε, no stall (C).
- `test_frontage_conservation.py` — I1 under continuous frontage; Lanchester linear bound (D).
- extend `test_mass_battle_systems_movement.py` + the stress harness depth-2 census (F).
- keep `test_mass_battle_byte_exact.py` green throughout (I4).

## 6. Risk register

| # | risk | mitigation |
|---|---|---|
| R1 | OBB overlap ≠ TOI halt → interpenetration or stall | build B+C together; assert touch-not-overlap invariant |
| R2 | continuous frontage breaks conservation (I1) | frontage as a *partition* of the meeting width; unit-test Σ=hp before wiring |
| R3 | gauge shift misread as a bug | A/B every stage, disclose, DG-6-gate; never tune to target |
| R4 | OBB rotation cost (perf / complexity) | small boxes near-axis-aligned most ticks; use reduced SAT + early-out |
| R5 | facing edge-cases (routed/yielding bodies face away) | reuse `PC_FACING_ROUT`/`_effective_reach` rules; test |
| R6 | determinism drift from float ordering | canonical iteration order (already `_oriented`); no `set` iteration in hot path |
| R7 | scope creep into the wired engine | Stage G fenced behind P-DEC-2; field engine ships first |

## 7. Rollback

Every stage is `FIELD_MOVEMENT`-gated and additive behind the OBB primitive; a stage can be reverted
without touching the grid oracle. Goldens are re-recorded only at F, so pre-F work is behaviour-diffable
against baseline at will.

## 8. What this buys

Honest facing (OBB orientation), honest frontage (front-width overlap), honest depth (box depth extent
cross-checked with pattern), honest directional reach (front-face growth by weapon), all on continuous
Euclidean motion with **no integer on the live position/contact path** — the "no grids" endgame for the
field engine, with the wired engine's reconciliation scoped as Stage G.

## 9. Open decisions needing Jordan (P-DEC) — do not block Stages A–C

- **P-DEC-1 — weapon-class → troop-type map** (for Stage E reach): default proposed in
  `geometric_contact_proposal_v1.md` §P2 (levy/light=0.1, heavy=0.2, cav/knights=0.2, ranged=0.1
  sidearm; no pike type yet). Confirm/edit.
- **P-DEC-2 — wired engine (Stage G):** route `resolve_mass_battle` onto the field engine and retire
  the integer engine (preferred), or port OBB into the wired engine.
- **P-DEC-3 — non-standard cell dims:** do heavier/lighter troop types get non-1×1 footprints (e.g.
  cavalry deeper), or is the box always 1×1 with density carrying mass? (Affects area/density.)
- **P-DEC-4 — gauge re-baseline authority:** the v2 frontage change WILL move the 20-row Cannae gauge;
  confirm re-record is authorized as part of this work (it is a DG-6-adjacent balance shift).
