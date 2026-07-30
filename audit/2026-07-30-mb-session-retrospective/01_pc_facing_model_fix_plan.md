# `PC_FACING_MODEL` — fix plan

**Date:** 2026-07-30 · **Lane:** MB · **ED:** ED-MB-0061 · **Spec:** `00_lessons.md` §4.5 (S1–S7)

## Status: PROPOSED (merge ratifies per ED-1094, EXCEPT §5's Jordan forks)

---

## §1 — The diagnosis in one line

**`PC_FACING_MODEL` is not broken in its own logic. It is correct code sitting on a substrate that
conflates three geometries into one `CellBox`, so switching it on makes a cell's *facing* change its
*collision volume*.** The fix is substrate-first: separate the shapes, then the facing model has
somewhere sound to stand.

**Measured, not inferred:**

| arm | `test_obb_contact_toi` |
|---|---|
| `PC_CELL_EXCLUSION=0/1`, all else ON | 2 failed (identical) |
| all 15 flipped flags OFF | 6 passed |
| **`PC_FACING_MODEL=0` alone** | **6 passed** |

`PC_FACING_MODEL` accounts for **exactly 2 of the 16** failures. ⚠ **F2 (`rear 0.0 != 2x front`) is
NOT one of them** — it survives `PC_FACING_MODEL=0` and needs its own bisect. Do not fold it in.

---

## §2 — Root cause, and why it is a substrate defect

`geometry.py:365-372` justifies the circle→box substitution as *"the same footprint diameter as the
legacy circle model."* Same diameter **on the axes only**. Consequences:

1. **The body box is rotation-variant.** A unit square's circumradius is 0.7071 against an intended
   body radius of 0.5 — a **41% over-claim in the diagonals**, zero on-axis.
2. **`_slew_facing` therefore re-shapes the collision volume.** Two disjoint bodies can overlap with
   **neither one moving**, purely because one turned.
3. **The swept-SAT certificate is voided.** `_swept_first_overlap_s` states its own precondition:
   *"over one tick the box axes and corner-offsets are CONSTANT — Euclidean motion translates only
   the centre."* A slewing facing violates that outright, so the TOI solve's guarantee does not hold
   in the configuration `PC_FACING_MODEL=1` creates.

That is the whole mechanism for F3/F4, and it also explains F11 (`1 − cos θ` off-axis
self-interpenetration) as the same artefact seen inside one formation.

---

## §3 — The fix, in dependency order

### P1 — Split the three geometries · **substrate, gates everything else**

| concern | shape | owner | rotation |
|---|---|---|---|
| body / exclusion | **circle, r = 0.5** | new `CellBody` | **invariant** |
| facing / damage / FOV | **octagon arc partition, vertex-forward** | `CellBox` (renamed to its real job) | **variant — that is its content** |
| engagement / reach | forward envelope beyond the body | reach envelope | variant, but never consulted for exclusion |

**The inscribed shape is the OCTAGON, not a square** (Jordan: *"moreso than a square, we want the
octagon"*). The square was only ever the legacy grid artefact; it carries no meaning in a continuous
field and should not survive the refactor. A regular octagon inscribed in the r=0.5 circle:

| quantity | value |
|---|---|
| circumradius (vertex reach) | **0.5** — vertices touch the exclusion circle exactly |
| apothem (face-centre reach) | `0.5·cos 22.5° = ` **0.46194** |
| area vs the circle | `2√2 R²` vs `πR²` = **90.0%** |

**This closes S1 against S6 exactly, and it is the tell that the spec is right.** The forward
**vertex** sits precisely *on* the exclusion circle, so when two cells are tangent — centres at pitch
1.0 — their forward vertices meet at exactly the contact point. "The point is what touches the
subunit facing line" (S1) and "the circle is the exclusion boundary" (S6) are then the **same
statement**, not two constraints to reconcile. The contact surface *is* the vertex.

Do **not** take the alternative repair (keep a 1.0-wide shape, grow the circle to 0.7071) — it
spaces every formation 41% further apart and invalidates frontage, density, contact and every band
fitted on them.

**Why keep the circle at all** (Jordan, 2026-07-30): *"we may not even need the circle tbh, but it
computes easy for collisions and attack reach radii, and since we're in a field, the octagon can snap
to any degree… circle is good because we have field coordinate movement and orientation and angle of
facing."* Three jobs, each one a reason:

1. **Collision is a scalar comparison.** Circle-vs-circle overlap is `dist < 2r`; the swept case is
   the quadratic `_pair_toi_scale` **already implements** and currently wastes as a mere pre-reject.
   No SAT, no axes, no corner sets, no constant-heading precondition to violate.
2. **Reach is a radius.** An attack envelope measured from the body is naturally polar, so reach
   composes with the body as `r + reach` rather than as a second oriented box.
3. **It decouples orientation from occupancy — which is the whole point.** On a continuous field the
   octagon must snap to *any* angle, not to 8 or 45° steps. A rotation-invariant body is exactly what
   lets facing be continuous and free without occupancy changing underneath it. The circle is not a
   simplification of the octagon; it is the **carrier** that makes the octagon's freedom safe.

**Immediate simplification this buys:** with a circular body the entire swept-SAT machinery for
*exclusion* collapses to the circular quadratic that `_pair_toi_scale` already implements and which
is currently used only as a pre-reject. Body-vs-body TOI becomes exact, cheap, and rotation-proof;
`_pair_toi_box_scale` stays, but only for the reach/engagement envelope where orientation genuinely
matters. **The retired code path is the one causing the defect.**

**Guard (G16 — must fail on DELETION, not perturbation):** a cell that only *rotates*, with zero
translation, must never change its overlap relationship with any neighbour. Mutation: restore the
oriented box as the exclusion volume → guard fails.

### P1b — Re-certify the heading, or slew BEFORE the solve · **the actual proximate cause**

⚠ **A read-only `fable` audit sharpened P1 into something more specific, and it is the real defect.**
The problem is not only that the box is rotation-variant — it is that **the commit rewrites the
heading the solve just certified.** Verified chain, in tick order:

1. `_flat` captures each cell's facing as the one committed at the end of the **previous** tick
   (`units.py:2185`).
2. The swept-SAT solve is exact **for that heading held constant**, and commits each cell at its
   *first-touch* fraction — where "touching" counts as separated by strict SAT.
3. `_commit_cell_position` then writes a **new** `cell_facing_vec[cid]` via `_slew_facing` — up to
   `60°·disc_mult` of rotation — **after** the certificate was issued (`units.py:1672-1676`,
   called from the resolver at `:2318-2319`).
4. A unit square's support half-extent along the contact normal grows from 0.5 to ≤ `√2/2` under
   rotation — ~0.207 per box, ~0.41 for a facing pair. **Bodies committed at exact touch under the
   certified headings strictly interpenetrate under the committed headings.** The test probe measures
   exactly this: it reads the *post-commit* `cell_facing_vec`.
5. Next tick, an already-overlapping cross-side pair solves to `s = 0.0`, which the cross-side loop
   accepts as a freeze — it never *un*-overlaps.

**Why OFF passes:** with the model off, commit writes `cell_facing_vec[cid] = _node_facing`, which
moves only via the body wheel — identity in a head-on clash and a straight charge, so certified and
committed headings coincide. **The defect class therefore survives `PC_FACING_MODEL=0` in any
wheeling engagement**; the flag widened an existing order-of-operations hole from "wheel-only,
quiescent in the tested geometries" to "every engaged cell, every tick."

**The invariant to restore: the heading the TOI certifies is the heading the tick ends with.** Either
slew before propose/solve, or re-certify after rotation. P1's circular body makes this *robust* —
rotation cannot change a circle's extent, so the ordering stops mattering for exclusion — but the
ordering must still be fixed for the reach/engagement envelope, which stays orientation-dependent.

**Guard:** a cell that only *rotates*, with zero translation, must not change its overlap
relationship with any neighbour — and, separately, no pair may be strictly interpenetrating after a
commit. Mutation: restore the post-solve slew → guard fails.

### P2 — ~~Vertex-forward orientation~~ · **RETRACTED: the arcs are ALREADY point-forward**

⚠ **My P2 was wrong and the audit overturned it.** I assumed the octagon was built face-forward.
It is not: `geometry.py:165-185` zones the arcs at **GREEN < 45°, YELLOW 45–90°, RED ≥ 90°**, which
is exactly S6's vertex-forward allocation (2 front faces spanning ±45°, 2 side faces to ±90°, 4 rear
faces over the remaining 180°). A face-forward octagon would place the boundaries at 22.5° / 67.5° /
112.5°. **There is no half-sector displacement to fix**, and "rear lands where nothing lands" is
geometrically impossible — RED is a closed 180° half-plane.

**What is actually missing is S5's mechanic, not the arc convention.** The octagon exists *only* as
three angular zones; there is no octagonal geometric object, bodies are squares, and
`_octagon_cell_mods` resolves against a local attacker **centroid bearing**, not face-to-face. So the
corner-disadvantage payoff — a perimeter corner cell splitting its frontage across two enemies — has
no substrate to exist in. **P2 becomes: build the octagon as a real object and resolve engagement
face-to-face**, which depends on P1 and on S2's subunit perimeter.

This is G17 landing on me a second time: I had a mechanism that explained the symptom, and it was
wrong because I never checked the arc boundaries in source before proposing to rotate them.

### P3 — One owner for heading · needs P2

S7 makes facing and movement **one vector**. Today `_node_facing`, `_node_facing0`,
`cell_facing_vec`, `advance_dir` and the per-tick movement vector are separate state for it, and any
two can disagree — the same failure shape `rekey_cells`/`check_drift` found one tier down
(ED-MB-0054, six stale per-cell maps). Collapse to a single owner with derived views.

**Guard:** a write-sweep in the style of `test_morale_write_sweep.py` — its `_CELL_OWNED` registry is
field-parameterised, so heading joins by adding one key (§0.1 point 1).

### P4 — Re-enable and re-measure

Only after P1–P3: re-run the bisect. F3/F4 must pass with `PC_FACING_MODEL=1`. Then re-measure
ED-MB-0059's headline with a corrected `_depth` (G18) — the −48.6%/−74.4% figures were computed with
a biased metric **and** in the pre-flip environment, so they must not be cited until re-taken.

---

## §4 — What this does NOT fix

`PC_FACING_MODEL` accounts for 2 of 16 failures. **F1** (`PC_FRICTION_CEV` one-sided advantage),
**F2** (rear damage 0.0), **F5**–**F8** are untouched by this plan and each needs its own single-flag
bisect before being called pre-existing. Per G17, the tidy story — "a half-sector octagon rotation
explains rear-damage-zero" — is **already dead**: F2 survives `PC_FACING_MODEL=0`.

---

## §5 — For Jordan

1. **P1 is a substrate change**, so it moves every golden. It should ride *with* the all-ON re-base
   (Phase 0), not before it — otherwise the oracle is re-based twice.
2. **Does the circle replace the box for exclusion everywhere, or only on the field path?** The grid
   path is the frozen byte-exact oracle; making it circular moves it too.
3. **`CONTACT_REACH`** remains a magnitude with no ledger-backed value (F18).

---

## §6 — Further findings from the read-only `fable` audit (2026-07-30), not in §3

Each verified in source by an agent that never saw the producer's reasoning.

| # | finding |
|---|---|
| **A1** | **`PC_FACING_SLEW_BASE = 60` is an explicitly UNRATIFIED magnitude that the flip made live.** Its own inline tag still reads *"NOT ratified — do not enable"* (`units.py:52`) and `provenance.py:159-164` still records *"F2 ships DEFAULT-OFF and NOT enabled"* — a provenance record the flip rendered false. A magnitude nobody ratified is now governing every engaged cell's rotation. |
| **A2** | **FOV-gated TARGETING is documented but does not exist.** `units.py:53` says the blind arc *"GATES reaction/targeting"*; the only consumer is the pin check. `assign_targets`' 'nearest' sets `target_atom` unconditionally, and the ATTENTION slew consults neither `PC_FACING_FOV_GATE` nor `FOV_HALF_DEG`. **So a cell physically turns to face a rear attacker the octagon model says it cannot perceive** — the blind-arc invariant is defeated for any non-halted cell. |
| **A3** | **Two competing latency models own "cells cannot turn instantly":** `FACING_REACTION_TICKS` (2 ticks, ED-MB-0018) holds the *penalty*, while `_slew_facing` (60°/tick·disc) rotates the *state*. With the model ON both run concurrently on different clocks. §8: one rule, one owner. |
| **A4** | **Canon conflict on the sightline.** `mass_battle_v30.md:155` specifies a **135° forward arc with a 15-cell perception range**; the code implements a **210°** visible arc (`REAR_BLIND_DEG=150`, `FOV_HALF_DEG=105`) and **no perception-distance limit anywhere**. Two canon owners disagree and the head doc loses silently. |
| **A5** | **Two FALSE canonical citations on the audited lines.** `geometry.py:183-184` cite *"mass_battle_v30.md §A.3b — 45deg octagon GREEN boundary"* and *"§octagon"* — sections that do not exist, in a head doc containing **zero** occurrences of "octagon". This is CLAUDE.md §7's leaky-anti-fabrication-gate pattern sitting on the exact lines this mechanic reads. |
| **A6** | **A prior measurement is falsified and still stands.** `HANDOFF_MB.md:698-699` records a 2026-07-22 stress result *"S4: PC_FACING_MODEL … SAFE when activated"*. The flip disproves it; that probe evidently never ran the OBB interpenetration invariant. Needs an explicit supersession note. |
| **A7** | **F2's real mechanism, and it is not the octagon.** The test's premise (*"same dice, same contact cells, only the arc differs"*) is structurally false: the arms differ in `advance_dir`, which flips orig-frame support depth, so the front-facing defender's contacted rank has a full support stack and the rear-facing one has **zero**. That changes the defender's pool → the b-roll's dice consumption → the attacker's coupled degree; and `Partial → 1` with `eff_dr = 1` gives `max(0, 1−1) = ` **exactly 0.0**. The arc multiplier is bounded `[1.0, 2.0]` and *cannot* produce 0. **`PC_FRACTIONAL_POOL` is the concrete candidate that re-landed seed 5's RNG stream — bisect it first.** |
| **A8** | **A third facing owner:** `engaged_frontage` uses subunit-level `_node_facing`/`advance_dir`, ignoring per-cell committed facing (`core/contact.py:334-335`). Low severity, but it is a fourth entry for P3's collapse. |
| **A9** | `PC_REACH_FACING_GATE` and `_effective_reach` are **dead code** (zero call sites, retired at `units.py:2219-2220`) and are not named in B3's wire-or-delete list, which covers only `_reach_throttle`. |

---

## §7 — RECONCILED PLAN (my P-items × the `fable` skeleton plan's R-items)

The skeleton plan supersedes §3's numbering. §3 is kept as the *diagnosis*; §7 is the work.

| R | item | absorbs | before re-base? | Jordan? |
|---|---|---|---|---|
| **R0** | Circular body / exclusion (`CellDisc`) | P1 | **rides with re-base** | scope: field-only |
| **R1** | One owner for heading (S7) | P3 | rides with re-base | — |
| **R2** | Tick ordering — slew in its own phase, before propose | **P1b** | rides with re-base | — |
| **R3** | Octagon arc partition as an owned primitive | ~~P2~~ | **yes, independent** | — |
| **R4** | Reach as a radius | — | rides with re-base | reach arc span |
| **R5a** | Perimeter derivation | S2 | **yes, independent** | — |
| **R5b** | Perimeter *conditioning* of cells (S4) | — | after re-base | S4/S7 lateral motion |
| **R6** | Face-to-face engagement + corner disadvantage (S5) | P2's real content | after re-base | emergent split; `FACING_REACTION_TICKS` |
| **R7** | Re-derivation register (measured-on-the-square) | — | attached to R0/R4/R6 | — |
| **R8** | Separation of pre-existing overlap (F10) | — | after re-base | build or defer |

### Three things the skeleton plan established that §3 had wrong or missing

1. **`perimeter.py` already exists** — hull faces, outward normals, target points, sharp-tip
   detection, `approach_alignment` — wired into `_envelop_goal` only. R5a *composes on it*; it must
   not be re-implemented (§8). S2 is under-wired, not absent.
2. **R2 is required even though R0 makes exclusion ordering-proof.** A circular body means rotation
   cannot change occupancy — but the *engagement/arc* surface stays heading-dependent, so without
   the reorder contact can still fire (or fail to) on a heading the solve never saw.
3. **The minimum viable slice is NOT the smallest diff.** R2 alone would green both
   `test_obb_contact_toi` failures (headings are identity in those two fixtures) — and it is
   **rejected**: it ships the retired substrate, leaves F11 intact, and is a **G13-shaped win**, a
   metric the wrong system can pass. The ruled slice is **R0-core + probe port**.

### The probe must be ported, and this is not optional

`_CommitProbe` (`test_obb_contact_toi.py:89-118`) measures **square** `obb_overlap`. On circular
bodies, cells committed at tangency (dist = 1.0) will *always* register rotated-square overlap — so
the old instrument reports failure on a correct engine. **The instrument cannot measure the new
substrate.** Port it to the engine's own predicate (strict disc overlap, G18), and note the bonus:
penetration depth on circles is exactly `2r − dist`, which retires the `_depth` bias class (F15)
permanently rather than patching it.

### R7 — what must be re-derived, not ported (§0.1 point 4)

Everything fitted on the square substrate: the `2.6` broad-phase cap (`contact.py:321`, derived from
the √2/2 half-diagonal → re-derive as `2·(0.5 + max reach)`); `R_body = hypot(0.5, 0.5)`; the gauge
bands in `bat.py`; ED-MB-0059's retracted headline; **the Lanchester frontage calibration** — a disc
projects width `2r = 1.0` at *every* orientation where the box projected 1.0–1.414, so rotated-
engagement frontage shrinks and the Stage-D gauge must be re-run; the F12 packing baselines; and
`PC_FACING_SLEW_BASE = 60`, which is unratified (A1) and now **doubly** load-bearing because heading
is also travel (S7).

### Consolidated Jordan-ruling register

1. Grid-path scope — recommend **field-only** (the grid oracle never enters
   `resolve_toi_and_commit`, which is field-gated); confirm.
2. Reach arc span — FRONT only (±45°) proposed; does SIDE get none?
3. **S4 × S7 tension:** may a cell translate laterally for perimeter infill *without* turning, and at
   what rate? Heading is the forward normal, but conditioning implies non-forward correction motion.
4. Corner disadvantage — confirm it is an **emergent pool/frontage split**, with no named multiplier.
5. `PC_FACING_SLEW_BASE = 60` ratification; and whether `FACING_REACTION_TICKS` retires in favour of
   the physical slew (two owners of one latency, A3).
6. **A4 canon conflict:** `mass_battle_v30.md:155` says 135° sightline + 15-cell perception range;
   the code has 210° and **no distance limit at all**. Which owner wins?
7. R8 separation impulse — build or defer.
8. Standing: the golden mode matrix; `CONTACT_REACH`'s magnitude; ED-MB-0059 headline re-measure.

---

## §8 — ADVERSARIAL REVIEW of "green apex octagon snapping in circle" (2026-07-30)

Read-only `fable` critic, structurally independent. **Verdict: P1's engineering core survives; the
geometric closure argument sold with it does not — and three of the spec's own claims are
geometrically unimplementable under S6 as written.** Those last are a conflict *inside* the spec and
need a Jordan ruling, not a patch.

### BREAKS

**D1 — "The contact surface IS the vertex" is OVERTURNED, and worse than I flagged.**
I had already conceded it holds only head-on. The critic sharpened it twice:
- The most common tangent pair in the game is **rank-mates marching abreast**, which touch at each
  other's **±90° SIDE vertex** — nowhere near the forward vertex.
- **The claimed contact point is, by the engine's own convention, not a contact at all.**
  `_sat_separated` counts exact touch as *separated* (`geometry.py:453-464`), `_pair_toi_scale`
  treats `distance == target` as no violation (`units.py:156-165`), and contact fires on the **reach
  envelope before bodies touch** (`units.py:2212-2214`). At reach 0, tangency is precisely the
  zero-casualty standoff deadlock ED-MB-0012 documents. **The vertex never carries a contact event.**

The claim was load-bearing as "the tell that the spec is right". With it gone, S1/S2/S5 revert to
**unreconciled constraints requiring design decisions**, which the "same statement" rhetoric hid.

**D2 — Face-to-face octagon engagement is IMPOSSIBLE at exclusion-legal range. OVERTURNED.**
Flush face-to-face contact of two octagons inscribed in r=0.5 circles needs centre distance
`2·apothem = 0.92388 < 1.0` — **the exclusion circles would have to interpenetrate.** Generic
vertex-touch at tangency needs the bearing ≡ 0 mod 45°, measure zero. **Under circle exclusion the
octagons can never touch.** So S5 is implementable only as bearing-sector bookkeeping — which is
exactly what `octagon_angle` already does — or on reach-extended faces, which nothing specifies.
**R6's "build the octagon as a real object" would build a polygon with no contact events to resolve.**
(Attack 3's annulus worry does *not* land: sectors partition 360°, so there is no dead zone. But that
is also the proof the physical polygon adds nothing over the arc partition.)

**D3 — The corner cell is at ZERO disadvantage under the spec's own multiplier table. OVERTURNED.**
Geometry favours the proposal first: a corner cell tangent to two enemies of a pitch-1.0 line sits at
`h = √3/2`, bearings exactly **±30°** — one on each front face. That sector statement survives. The
payoff does not:
1. **S6 assigns both front faces one class.** FRONT is 0…±45°, live as `ANGLE_DEF_MOD` GREEN = 0,
   multiplier **1.0** (`config.py:199-210`). Both attackers read GREEN. That is **parity — the
   equal-best arc any engaged cell can show.** A cell showing flank (1.5×) or rear (2.0×) is strictly
   worse off. "Maximum disadvantage" has no expression in the multiplier system the same spec defines.
2. **The engine already litigated this exact configuration and ruled it a FALSE POSITIVE.** ED-MB-0018's
   balance-critic fix rebuilt multi-side shock because the arc-blind count fired on *"TWO attackers
   both in the FRONT arc (**a concentric frontal pinch, not an encirclement → false +50%**)"*
   (`orchestration.py:743-752`). **Apex-into-gap is that configuration.** Implementing S5 as claimed
   partially reverses a critic-driven fix.

And the emergence claim is **backwards**: to get the disadvantage you must build face assignment, a
per-face frontage split, and a split-face penalty — none of which exist. The rule *attaches to*
geometry (good design); it does not *fall out of* it.

**D4 — S1 and S5 are mutually exclusive as stated.** "Apex on the leading edge" pins a cell's heading
exactly perpendicular to that edge. S5's corner cell faces the **gap bisector**, off both normals —
and `_slew_facing` rotates every engaged cell off-normal anyway. **The moment any cell turns, its apex
leaves the facing line; only the circle stays on it.** S1 as a standing invariant holds only at parade
rest. One reading reconciles them — the perimeter as a **Minkowski envelope** of the body circles,
whose rounded corner is an arc of the corner cell's own circle, on which every apex position lies for
a fan of headings — but that is specified nowhere.

### NEW DEFECT NEITHER PLAN SAW

**D6 — The circle LEGALIZES identity-map bin collisions that the square forbade.**
`_oriented_abs_map` file-bins live cells to `(round(r), round(c/COL_WIDTH))` with **FIRST-wins
`setdefault`** (`geometry.py:259-265`). Two points in one bin can be ~1.27 apart — **legal for tangent
r=0.5 circles**, but *overlapping* (hence excluded) for axis-aligned unit squares. So the box model
structurally suppressed this case. On a collision the dropped cell **vanishes from the identity map**
→ `_octagon_cell_mods` falls back to nominal axis-aligned facing (`orchestration.py:1057-1059`) and
contact identities merge (`core/contact.py:324-325`). Worse: S4's "collapse/infill" under circular
exclusion relaxes toward **hex packing** (row pitch 0.866), which row/col binning cannot represent at
all. **R0 "gates everything" but no item covers the identity substrate.** This is where the circle
proposal actually leaks.

### WHAT SURVIVED

- **The S6/P1 separation of concerns, and its causal story, verified in source.** The swept-SAT
  precondition is genuinely violated by the post-certificate slew. A rotation-invariant exclusion body
  kills the exclusion half of that class outright. The `_pair_toi_scale` quadratic to be promoted is
  real, exact, and currently only a pre-reject.
- **The arithmetic**: apothem 0.46194, area 90.0%, circumradius 0.5; and the rejection of the
  r=0.7071 alternative (41% spacing blow-up) is correct.
- **Attack 4 fails in the proposal's favour.** Arc assignment is *already* fully continuous — an
  `acos` with 45°/90° thresholds, `_slew_facing` rotating by arbitrary radians, `cell_facing_vec`
  holding raw floats. Nothing assumes quantised arcs. **"Snapping" is a misnomer for free rotation and
  is harmless.** The only quantisation residue is the axis-aligned *fallback* facing on identity-map
  misses — which is exactly what D6 inflames.
- **P1's G16 guard design** (rotation-only must not change overlap; mutant = restore the box).
- **D7 — the porosity attack does NOT land; the circle is exonerated.** Nothing in the engine reads
  physical body area: F12's metric was pitch-normalised packing + NND, frontage is a projected-width
  union where a tangent circle rank projects the same 1.0/cell, and contact counts cells. F12's
  porosity was clumping *below* pitch (NND 0.68) — which circular exclusion makes **impossible**. The
  circle *strengthens* the anti-porosity invariant.
- **D9 — constants are conservative supersets, not silently falsified.** `R_body` and the 2.6 bound
  stay valid (perf-only; their derivation comments go stale). But `OCTAGON_LOCAL_REACH = 2.0`'s
  "verified front→1.00×, rear→2.00× exactly" lapses until re-taken, since halt geometry changes the
  within-radius attacker set.

### Consequence for §7

- **R6 must not be built as specified.** Either S5 becomes a bearing-sector rule with an explicit
  front-face split (a canon change to front-arc semantics, partially reversing ED-MB-0018), or it is
  withdrawn. **Jordan's call.**
- **R3's face-index addition is unnecessary for engagement** (D2) — keep the arc partition, drop the
  polygon.
- **New R0b: the identity substrate** (D6) — must land with R0 or the circle introduces a fresh defect.
- **P1b must also cover the `yield_active` branch**, which writes an instantaneous un-slewed facing
  *regardless* of `PC_FACING_MODEL` (`units.py:1669-1671`). The plan named only the slew path.
