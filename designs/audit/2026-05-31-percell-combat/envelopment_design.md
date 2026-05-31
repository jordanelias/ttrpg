# Envelopment From the Ground Up — Diagnosis + Design (prototype-validated)
Date 2026-05-31 | Engine: tests/sim/sim_mb_sigma.py | Prototype: envelopment_proto.py
[SELF-AUTHORED — bias risk.] Jordan hypothesis (CONFIRMED): "the front of the cell should be the same as its vector."

## ROOT CAUSE (confirmed empirically)
Every cell's facing vector is forced to straight-ahead. In advance_cells, column-local targeting sets
`cell_target = (enemy_centroid_row, my_OWN_starting_column)` — so each cell aims at its own column,
dc=0, c_step=0, and the recorded facing (line ~847) is always (+/-r_step, 0) = forward.
EMPIRICAL: a Horseshoe's 18 cells after advancing ALL have facing (-2, 0); 0/18 have any lateral
component. Cells never wheel, so they never reach an enemy flank, so the octagon angle (which is
CORRECT) always reads GREEN (frontal). Envelopment cannot emerge. The Incr6 envelopment delta-sigma
failed because it bolted a flank bonus on top of a geometry that never sees a flank — double-counting.

## WHAT ALREADY WORKS (octagon math is sound — proven in prototype)
- A wing POSITIONED at the enemy flank reads YELLOW/RED vs a forward-facing defender (def_mod -1/-2). [panel A]
- Facing = vector-to-objective makes the wing face inward; octagon unchanged, still reads flank zones. [panel B]
- FLANK-REFUSAL is also pure geometry: a defender that TURNS its flank cell to face the envelopers
  converts RED(-2) -> GREEN(0). A deep formation that can spare reserve ranks to reform the flank
  refuses envelopment; a thin one cannot. [panel C]
So envelopment AND its counter both fall out of the existing octagon_angle once cells can wheel + rotate.

## THE FIX (ground-up; three coupled parts, all gated by PER_CELL so toggle-off is exact)
1. LATERAL WHEEL: an overhang/wing cell with NO enemy directly ahead may step toward the nearest OPEN
   enemy flank cell (relax column-local targeting for such cells only). This is the part the engine forbids.
2. FACING = MOVEMENT VECTOR: keep line ~847 but it becomes meaningful — a wheeling cell's facing rotates
   inward automatically (Jordan's principle). No new facing code; the lateral step supplies dc != 0.
3. OCTAGON DOES THE REST: flank/rear def_mod emerge for the wrapped wing; refusal emerges when a deep
   defender reforms (turns) its flank cell. NO separate envelopment delta-sigma (that was the Incr6 error).

## PORT PLAN (next, into sim_mb_sigma, incrementally + gated + validated each step)
P1. Identify "free" overhang cells per tick: cells of the wider side whose column has no opposing enemy
    column within contact range (the overhang beyond the enemy frontage).
P2. For those cells only, set cell_target to the nearest enemy FLANK cell (the outboard end of the enemy
    frontage) instead of their own column -> they wheel inward; facing follows (line 847 already does it).
P3. Deep-defender flank-refusal: when a defender's flank column has reserve depth beyond PC_FRONT_RANKS,
    rotate that flank cell's facing toward the envelopers (reform) -> octagon neutralizes the wrap.
P4. Validate H3/H5/H6 (should rise — enveloping shapes finally get the flank advantage) WITHOUT breaking
    H4 (Arrowhead is convex/centre-heavy, generates little overhang-wheel) or the mirror. Re-run NERS Stage 4.
Note: this is geometry/movement, not a delta-sigma — it should REPLACE the dormant _envelopment_sigma,
not add to it (NERS-N/E). Validate that the octagon flank penalties alone produce the effect.
