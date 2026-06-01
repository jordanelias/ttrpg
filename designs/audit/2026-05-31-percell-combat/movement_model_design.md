# Foundational Movement + Perception Model — Design (prototype-validated)
Date 2026-05-31 | Jordan directives | Prototype: envelopment_proto.py (foundational_demo) | [SELF-AUTHORED — bias risk]

## THE FOUNDATIONAL ERROR (confirmed)
The engine's advance_cells uses column-local targeting: every cell aims at (enemy_centroid_row,
ITS_OWN_starting_column). Movement is therefore FORWARD-ONLY; cells cannot move laterally or backward,
and because facing = movement vector, they can never face anything but straight ahead. This is the
critical foundational error Jordan flagged. It is WHY envelopment/flanking/refusal cannot work.

## THE MODEL (Jordan's 5 directives — all prototype-validated)
1. MOVEMENT FREEDOM: a cell steps toward its tactical objective in ANY direction (forward/lateral/
   backward). move_step() shows all three; the existing r_step/c_step math already supports any sign —
   only the column-local objective restricts it.
2. FACING FREEDOM: facing = movement vector (already line 847); becomes meaningful once movement is free.
3. PINNING: a cell engaged in its front arc is pinned and CANNOT rotate to defend a flank. is_pinned():
   enemy adjacent (<=~1.5) within the front (<45deg) arc.
4. FIELD OF VIEW: a cell cannot perceive/react to a threat outside its FOV (measured from the facing tip).
5. REFUSAL GATE: a cell may rotate to meet a threat ONLY if (not pinned) AND (threat within FOV).
   Pinned-or-blind defenders take the octagon flank/rear penalty (envelopment lands); free-and-sighted
   defenders refuse (turn to face -> GREEN). This is flank-refusal done correctly.

## OPEN — FOV ANGLE INTERPRETATION (needs Jordan confirmation; 1-line switch)
"135 degree field of view calculated solely from the tip of their facing." Two readings:
  (A) 135deg TOTAL cone => visible if angle-from-facing <= 67.5deg. Consequence: a 90deg side/flank
      attacker is already BLIND; only near-frontal threats are refusable. Flanking is devastating.
  (B) visible out to 135deg from facing (270deg total) => blind only in the rear 90deg cone
      (angle > 135deg). Consequence: you CAN react to a 90deg flank attack you can see; only a deep
      rear envelopment (>135deg) blindsides you.
Prototype currently uses (A). I suspect (B) is intended ("from the tip of their facing" = arc extends
135deg from the facing direction). FOV_HALF is the single switch: (A) 67.5, (B) 135.

## PORT PLAN (into sim_mb_sigma, gated PER_CELL; PER_CELL=0 stays the ratified engine exactly)
M1. MOVEMENT: in advance_cells, replace pure column-local targeting with per-cell objective selection:
    - enemy in my file/front -> engage forward (keeps the line; ~current behaviour).
    - overhang (no enemy in my column span) -> wheel toward nearest enemy flank (already in: PC_WHEEL).
    - reactive: a visible, unpinned flank/rear threat -> reposition/turn toward it (lateral/BACKWARD wheel).
    Keep formation cohesion via the existing collision/contention resolution.
M2. PERCEPTION: add _angle_from_facing, _in_fov(FOV), _is_pinned helpers (ported from the prototype).
M3. REFUSAL in the octagon: in _per_cell_angle_mod, a flanked defender cell that can_refuse() rotates to
    face the attacker (penalty -> ~GREEN); one that cannot (pinned OR outside FOV) keeps facing and takes
    the full flank/rear penalty. This REPLACES the dormant _envelopment_sigma (geometry, not delta-sigma; NERS-N/E).
M4. VALIDATE: H3/H5/H6 (enveloping shapes) should rise as their wheels reach pinned/blind flanks; H4/H11/
    mirror must hold. Re-run NERS Stage-4. Confirm PER_CELL=0 unchanged at every step.

NOTE: this is a foundational movement re-architecture. It is gated entirely behind PER_CELL so the ratified
engine (PER_CELL=0) is never at risk; each M-step is validated toggle-off-exact before commit.
