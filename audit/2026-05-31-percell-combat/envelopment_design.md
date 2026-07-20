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

## IMPLEMENTATION STATUS (2026-05-31, committed)
P1/P2 DONE + committed (e822c1d9): the WHEEL. In advance_cells, an overhang cell (column beyond the
enemy frontage span) targets the nearest enemy cell instead of its own column -> wheels inward, and
cell_facing_vec rotates inward. Horseshoe now has 4/18 cells with lateral facing (was 0/18). Gated
PER_CELL+PC_WHEEL; PER_CELL=0 reproduces committed 120/120. Jordan's rotation hypothesis is now FIXED
in the engine: cells rotate to face their movement vector.

P3 (combat payoff via _per_cell_angle_mod centroid->nearest-attacker): ATTEMPTED, REVERTED. Making each
defender cell judge the nearest attacker (the wheeled cell) instead of the centroid DID fire the octagon
flank detection, but the effect was the wrong shape: H3 (the target) did NOT rise (43, still low), H4 rose
to 56, H11 went HIGH (62), H6/H9 worsened. Net aggregate worse, target unmet -> reverted (NERS-E). Engine
unchanged from e822c1d9.

WHY P3 didn't land H3: Horseshoe's overhang is only 2 columns (8 and 14) beyond a 5-wide Line (9-13). Two
wing cells wheeling cannot meaningfully WRAP a 5-wide Line within the battle horizon — the wrap is too
shallow to flip the matchup, and the symmetric nearest-attacker rule also lets the Line's own geometry
register flanks, shifting reverse-pair matchups (H11) unpredictably. The rotation is necessary but not
sufficient; a decisive envelopment payoff needs MORE: deeper/faster wheel penetration so wing cells reach
behind the enemy flank, AND likely an asymmetric "who is enveloping whom" gate so only the genuine
encircler's wheeled cells confer the flank penalty (not both sides' incidental geometry).

OPEN (next, design-led): (a) tune wheel depth/speed so overhang cells reach the enemy flank+rear, not just
abreast; (b) gate the flank-penalty to the side with net overhang (the encircler), to avoid reverse-pair
noise; (c) then P4 validate H3/H5/H6 rise without breaking H4/H11/mirror + NERS Stage 4. The rotation
foundation (P1/P2) is in place and committed; the payoff is a focused follow-on, not a re-architecture.
