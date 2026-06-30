# 06 — Movement-Substrate Review: grid vs. coordinate field (adversarial)

**Question (Jordan):** *"Is the field/movement grid even the right call? Does a cell need to occupy a
specific cell on a grid, or does it just need correct relative distance on a coordinate field?"*

**Method:** an adversarial Workflow — a 2-agent structural map of the movement substrate → 5 critique
lenses (discretization artifacts · relative-distance sufficiency · occupancy-as-mechanic ·
coordinate-field design · scale/emergence) → per-finding adversarial verification (refute-or-downgrade) →
synthesis. 43 agents; 31 findings survived verification (4 verify agents hit the schema-retry cap and
were dropped — their lenses are still represented by surviving findings). This is **Track M** in
`05_redesign_workplan.md §2A`.

---

## Verdict

> **A cell does NOT need to occupy a specific grid cell.** Every load-bearing *resolution* consumer reads
> only **relative** quantities. Absolute integer `(r,c)` survives in just three places, none of which
> require true occupancy: (1) contact/contention detection — a king-move proximity threshold trivially
> re-expressible as `dist < r_a + r_b`; (2) exact-equality "same-cell" collisions — one mechanic is **dead
> code**, the other is **live but manufactured by the `int(round())` snap itself**; (3) **column binning**
> for frontage/depth — which wants a 1-D quantizer, not 2-D occupancy. The `PC_NODE_COHESION` path is
> **already a continuous float coordinate field internally** (float `_node_pos` relaxing toward
> `anchor + rotated relational offset`), re-quantized only by `int(round())` at the `cells()` boundary.
>
> **Recommendation: `review-first-no-commit`.** Adopt the coordinate field as the **target direction**,
> but gate the migration behind a decision stage. It is **not a free refactor**: the contact-cardinality,
> cross-side-contention, and column-binning re-expressions are genuine new design the grid was hiding
> inside integer equality, and the metric/speed/heading changes make the field **digest-breaking by
> construction** — so it must ship as an explicitly-recorded behaviour change with a new gauge baseline,
> never a silent swap.

**On lens conflict the project rule is history > theory > games** — the field's wins below are *intended-
physics corrections* (circular range rings, continuous speed, true heading) that must each be **ratified
against the `gauge_mb.py` bands**, not assumed.

---

## What the structural map established (verified)

**Position model.** A cell has a stable pattern identity `cid=(orig_r,orig_c)` + a live position computed
two ways (`config.PC_NODE_COHESION`, default OFF):
- **Legacy integer path:** position is a *pure function* `start + oriented(or_r,or_c) + cell_offsets[cid]·advance_dir + cell_offsets_c[cid]` — two **integer** dicts; no stored live position (`hierarchy/units.py:251-262`, replicated ~8×).
- **Node float path:** `_node_pos[cid]` stores a genuine **float** position, relaxed toward a float `anchor + rotated relational offset` (`units.py:306-380`); **every consumer reads it through `_node_cells()` which snaps `int(round(...))`** (`units.py:298-304`). *The float precision never escapes the node module.*

**Distance model.** Mixed: the load-bearing combat/halt/range metric is **Chebyshev king-move**
(`_atom_distance` `orchestration.py:850`; `find_contacts` two `<=1` tests `core/contact.py:174`); target
*selection* is already **Euclidean** on float centroids (`assign_targets` `core/contact.py:29-36`);
octagon facing/support/roll-up is **relative vector** math (`geometry.py:163-221`, magnitudes cancel).

## What the grid distorts (confirmed findings)

| # | Distortion | Evidence | On a field |
|---|---|---|---|
| 1 | **Chebyshev `√2` anisotropy** — a diagonal of N cells reads the same distance as N orthogonal, so a 45° approach is "in volley band"/"adjacent" at ~1.41× the true separation | `_atom_distance` `orch:850`; node halt `units.py:334`; kite `units.py:405` | Euclidean → circular range rings (intended-physics fix) |
| 2 | **Integer speed floors the discipline signal** — `floor(base·disc_mult)` with the 0.7/0.4 tiers: `floor(1·0.7)=0` *freezes a degraded slow body entirely* | `advance_cells` `units.py:420-435`; `_node_advance:317-324` | `v = base·disc_mult·cav_mult` continuous — and the new load/locomotion primitive (`mass_kg`, pace) is continuous by nature |
| 3 | **`round()` step-split snaps heading to 8 directions** — a speed-1 wheel moves `(1,0)`/`(0,1)`, never a true diagonal, corrupting the envelop/wheel/sweep maneuvers **and the facing vector they feed** | `units.py:530-533` | realized heading = intended heading (the design's stated goal `units.py:465`) |
| 4 | **`abs→orig` exact-integer reverse-lookup** is the real *hard* grid binding — per-cell facing/support/halt all recover `cid` by integer `==` | `geometry.py:242`; `orch:541-547,1016,1025` | thread the stable `cid` on the contact pair (`iter_cells` already yields it) → the math is already relative |
| 5 | **`*_cells` integer lattice** rounds requested concentration to "the closest the discrete geometry allows", special-casing the 3 scales | `footprint_for` `geometry.py:124-135` | one `(centroid, radius, density)` primitive at every granularity |

## What is *actually* grid-dependent (the three survivors)

1. **Contact + cross-side contention** (`find_contacts` `contact.py:174`; `resolve_cross_side_contention`
   `contact.py:125`, **live**, fires 4–14×/battle in asymmetric-speed bands H3/H6/H10). `find_contacts`
   is a **proximity** test (8-neighbourhood incl. diagonals), not occupancy — but it returns the *set/
   cardinality* of contacting pairs, and those cardinalities scale damage (`support_engage_frac`
   `geometry.py:253`; `contact_fraction` `orch:1102-1119`) and Lanchester frontage (`core/attrition.py:24`).
   Re-expressing co-location as footprint-overlap **will** change those digests → genuine new design.
2. **Exact-equality occupancy** — `resolve_internal_collisions` (`units.py:606-672`) is **dead code**
   (uninvoked `orch:1061`, and *gauge-negative* 12/13→9/13 when active); the node "blocked-cell hold"
   (`units.py:372`) is live but reads `enemy_cells` as occupied integer cells. Both are **manufactured by
   the snap** (two floats are never equal) → reframe as overlap/repulsion radius *only if finite capacity
   is wanted*.
3. **Column/file binning** — the genuinely-discrete abstraction: frontage = distinct integer columns,
   depth = rank count, density, casualty spread, `role_at_contact`, Lanchester strength all bucket on
   integer `c` (`percell.py`, `core/attrition.py:24`). This is **real military structure**; it needs a 1-D
   `quantize(x / column_width)`, not 2-D cell occupancy.

## What each substrate does better

**Grid:** byte-exact reproducibility (the `bat.py` G5 digest depends on integer positions); O(1)
exact-equality identity round-trips and set-membership occupancy; *free* column discreteness; the 11
gauge bands were validated against integer-grid behaviour (its quantization is in the baseline).

**Field:** removes the `√2` anisotropy; restores fractional speed + the discipline-degradation signal;
restores true heading (fixes wheel/envelop/sweep + their facing); **unifies unit/subunit/cell** as one
primitive at different radii; turns crowding into honest density/overlap physics (deletes the
snap-manufactured collisions); and **is the natural home for the continuous load/locomotion model the
project is now building** — the integer grid is lossy exactly where `mass_kg`/pace lives.

---

## The staged decision gate (drop-in for the workplan — Track M)

> ### Track M — Movement-substrate decision (gated; feeds Stage 2b + Stage 3)
> **Build (read-only, done):** this review. Direction adopted: coordinate field; migration NOT committed.
> **G-decision — answer before any substrate switch (each measured against `gauge_mb.py`, bands never lowered):**
> 1. **Contact metric** — does `dist ≤ r_a+r_b+reach` reproduce the bands, or does losing the diagonal-
>    inclusive 8-neighbourhood drop contacts that fire today? (Most digest-load-bearing single choice.)
> 2. **Contact cardinality** — can a radius test reconstruct an equivalent discrete contacting-pair *set*
>    (it scales damage + frontage) without re-imposing a lattice?
> 3. **Occupancy/contention** — `resolve_cross_side_contention` is live and digest-affecting (H3/H6/H10);
>    is "faster mover takes contested ground" preserved by a footprint-overlap rule?
> 4. **Column binning** — define the file quantizer for float `x`; confirm frontage = distinct files,
>    depth = rank count, and `role_at_contact`'s `==`/`≤0.5` tests get a tolerance treatment.
> 5. **Dead/asymmetric mechanics** — confirm `resolve_internal_collisions` stays uninvoked (or is
>    re-authored as radius/density) and that dropping it is gauge-neutral.
> 6. **`cid` threading** — confirm `find_contacts` can return `cid` pairs so every `abs→orig` reverse-
>    lookup is deleted (makes facing/support/momentum grid-free with *no new math*).
> **G5 byte-exact posture (non-negotiable):** ship the field as a **parallel substrate behind a default-
> OFF toggle**, mirroring `PC_NODE_COHESION`. Toggle OFF (+ `PER_CELL=0`) must reproduce the `bat.py`
> digest digit-for-digit. The field path **cannot** be byte-exact (the Chebyshev→Euclidean swap +
> `floor()/round()` removals change every non-orthogonal result), so it carries its **own** newly-committed
> golden digest + a written behaviour-change ED entry, with the `gauge_mb.py` 11-band re-baseline recorded
> here and each delta ratified by Jordan as a correction — never fitted away. **If toggle-off byte-exactness
> is impossible, the field is rejected for this stage and the substrate stays grid.**
> **G3 adversarial:** the red-team must break the radius/binning re-expressions (a dropped contact, a
> column miscount, a contention reversal) before any commit.

**Cheap, decoupled first step (recommended, independent of the grid/field decision):** the items that are
*pure wins with no occupancy question* — thread `cid` on the contact pair to delete the `abs→orig`
reverse-lookups (finding 4), and make speed/heading continuous internally (findings 2–3) — can land first
behind the toggle, because they touch only relative math. The genuinely grid-coupled re-expressions
(contact cardinality, contention, column binning) wait for G-decision.
