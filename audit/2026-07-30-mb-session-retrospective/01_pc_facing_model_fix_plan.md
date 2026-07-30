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

**Immediate simplification this buys:** with a circular body the entire swept-SAT machinery for
*exclusion* collapses to the circular quadratic that `_pair_toi_scale` already implements and which
is currently used only as a pre-reject. Body-vs-body TOI becomes exact, cheap, and rotation-proof;
`_pair_toi_box_scale` stays, but only for the reach/engagement envelope where orientation genuinely
matters. **The retired code path is the one causing the defect.**

**Guard (G16 — must fail on DELETION, not perturbation):** a cell that only *rotates*, with zero
translation, must never change its overlap relationship with any neighbour. Mutation: restore the
oriented box as the exclusion volume → guard fails.

### P2 — Vertex-forward orientation · needs P1

`CellBox.heading` is currently the box's **depth axis**, with faces built perpendicular to it —
**face-forward**. S1/S7 require the heading to be the **vertex normal**, with the two front faces at
±45°. Arc allocation (S6, regular octagon, 45°/face):

| arc | faces | span |
|---|---|---|
| FRONT | 2 | 0° … ±45° |
| SIDE | 2 | ±45° … ±90° |
| REAR | 4 | beyond ±90° (180° total) |

**Guard:** a cell facing an enemy squarely reports FRONT; rotating it 67.5° reports SIDE; 180°
reports REAR. Under a face-forward octagon these land in the wrong sectors — that is the mutation.

**Check against S5, not just the multipliers:** the payoff of vertex-forward is that a cell at a
perimeter **corner** points its vertex into the gap between two enemies and is engaged on **both**
front faces at once — maximum disadvantage — while a squarely-met cell fights one opponent on one
face. If the implementation does not produce that, it has the geometry without the mechanic.

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
