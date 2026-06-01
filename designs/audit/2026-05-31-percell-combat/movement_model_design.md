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

## FOV — RESOLVED (grounded bottom-up in physiology, top-down in military scholarship; searched 2026-05-31)
Visual physiology: the human horizontal visual field is ~190-210deg (Wikipedia "slightly over 210"; per-eye
~107deg temporal per NCBI clinical figures; binocular overlap ~114deg, monocular periphery ~50deg each side).
=> anatomical REAR BLIND ARC ~150deg, visible +/-105deg. (Jordan proposed 135deg blind; evidence puts it
slightly larger at ~150deg; the difference is within helmet/individual variation. Set REAR_BLIND_DEG=150,
FOV_HALF=105, Class-B tunable.) PINNING models the attentional lock of an engaged soldier SEPARATELY, so
FOV represents raw anatomical perception (the generous max), not the narrower combat-effective field.

Military scholarship validates the whole model:
- Envelopment attacks the flank/rear and induces PSYCHOLOGICAL SHOCK on the defender, not merely casualties
  (US Army doctrine via Wikipedia/EPFL) -> grounds the strong octagon flank/rear penalty + morale effect.
- Textbook envelopment uses a FIXING FORCE that "attacks the enemy's front and 'fixes' them in place so they
  cannot withdraw or shift their focus on the enveloping forces" -> this IS the pinning rule, exactly.
- Clausewitz (Principles of War): reserves "put obliquely behind... can attack the flank of the enemy columns
  which are seeking to envelop us"; "formation in depth... the less secure our flanks, the more corps in the
  rear" -> grounds FLANK-REFUSAL via reserve depth (a deep formation refuses/counters envelopment).
- du Picq: "success in battle is a matter of morale" -> the moral collapse from being struck where one cannot
  face the threat (already the engine's graded-morale anchor).

With FOV_HALF=105 the model resolves textbook-correctly (prototype foundational_demo):
  pinned + flank -> cannot refuse -> RED penalty (fixing force);
  free + flank within FOV -> REFUSES (turns to face -> GREEN);
  free + attacker in dead rear (outside FOV) -> blind -> cannot refuse -> RED (blindsided).

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
