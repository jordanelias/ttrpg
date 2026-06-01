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

## ENGINE PORT — M2/M3 IMPLEMENTED (DORMANT), commit 0b21c20c (2026-05-31)
M2 perception (committed): REAR_BLIND_DEG=150 (visible +/-105deg, grounded in the ~210deg human visual
field), PC_PIN_REACH=1.5. M3 refusal (committed, in _per_cell_angle_mod, gated PER_CELL+PC_REFUSE): each
defender cell is judged against its WORST-flanking attacker and REFUSES (negates the penalty) only if NOT
pinned AND the flanker is within FOV; otherwise the flank/rear penalty lands. This is the fixing-force +
flank-refusal doctrine expressed in the octagon.

RESULT (PC_REFUSE=1, A/B vs wheel-only, multi n=55): envelopment EMERGES —
  H3 Horseshoe-v-Line 47->58 (IN), H4 Cannae 43->50 (IN), H7 GappedLine-v-Line 40->57 (IN),
  H2/H5/H9 also IN. The wheel's rotation finally produces a combat payoff.
BUT three correctness problems block making it the default:
  1. MIRROR BIAS (disqualifying): H1 Line-v-Line -> 57-62% (n=120: 57.3) vs the required ~50. The
     worst-flanking-attacker detection is an extremum, hypersensitive to the sub-cell stagger that integer
     movement + advance_dir sign produce; A and B see systematically different worst angles -> directional bias.
     [The centroid method it replaced averaged this out and was mirror-stable.]
  2. REVERSE-PAIR INVERSION: H10 (Line-v-Horseshoe) and H11 (Arrowhead-v-Horseshoe) go HIGH — the
     enveloped side wins MORE. [ASSUMPTION — basis: geometry] a wheeling enveloper's cells face inward, so in
     the symmetric octagon their rotated facing EXPOSES their own flank to the main enemy line, penalizing the
     enveloper instead of the enveloped. The wheel and the defensive octagon interact backwards.
  3. H6 (RefusedFlank-v-Line) drops to 21.
Per NERS-E this is NOT shippable as default -> retained DORMANT (PC_REFUSE default off; PER_CELL=0 and
PER_CELL=1-default both reproduce the committed wheel engine 120/120), mirroring the dormant Incr6 delta-sigma.

## NEXT (focused, design-led — the two fixes)
F1. MIRROR-STABLE FLANK DETECTION: replace the position-sensitive worst-single-attacker with a method robust
    to sub-cell stagger — e.g. only count an attacker as a flanker if its angle exceeds a margin above the
    octagon YELLOW boundary (so frontal-diagonal neighbours at ~45deg never register), or detect envelopers
    structurally (attackers beyond the defender's frontage span) rather than by raw angle extremum. Must
    restore H1 ~50 and reverse-pair symmetry.
F2. ENVELOPER-SELF-FLANK: a cell that has deliberately wheeled to envelop should not be scored as defensively
    flanked for its rotated facing vs the cells it is NOT engaging. Restrict the per-cell defensive angle to
    the attackers the cell is actually in contact with, or exempt wheeled offensive cells from the self-flank
    penalty. Must fix the H10/H11 inversion.
Then re-run the full 13-test set + NERS Stage-4; confirm PER_CELL=0 unchanged at every step.

## F1/F2 STRUCTURAL FIX — committed 855b619 (2026-05-31, still dormant)
F1/F2 root cause (revised): the mirror bias was NOT the 45deg YELLOW boundary — RED-only didn't fix it
(H1 stayed 63). Integer-movement stagger creates "same-row-beside" attackers (~90deg, RED) asymmetrically
between A and B; any angle-EXTREMUM method inherits the asymmetry. FIX: detect envelopers STRUCTURALLY —
an attacker cell wrapped BEYOND the defender's frontage span [min_col, max_col]. Mirror-stable BY
CONSTRUCTION: equal-width formations produce zero wrappers -> H1 = 50.0. This ALSO fixes F2 (the enveloper
self-flank inversion): the wider side's narrower enemy cannot wrap it, so the enveloper is never penalised
for its own inward-rotated facing -> H10 inversion resolved. RED-zone wrapper penalty = PC_ENVELOP_MOD
(default -1.0), refusal-gated (pinned/blind -> lands; free+sighted -> refused).

RESULT (PC_REFUSE=1, PC_ENVELOP_MOD=-1.0, n=50-60): H1 50, H2 57, H4 49, H7 52, H10 41 -> IN.
REMAINING — needs a depth-resistance mechanic, NOT a scalar:
 - H3 (Horseshoe-v-Line) still HIGH (66-68): width alone over-rewards wide enveloping shapes; the wrap is
   too easy/strong even at low magnitude.
 - H5/H6 (RefusedFlank-v-Horseshoe/Line) LOW (22-47): a REFUSED or DEEP flank should RESIST being wrapped
   (Clausewitz: "formation in depth... more corps in the rear to envelop those enveloping us"; the refused
   column should pivot to face the enveloper). Currently width alone decides wrapping, so RefusedFlank is
   crushed despite its refusal.
 - H9 (Line-v-Arrowhead) LOW (28-32): Arrowhead (widest) over-wraps Line.

## NEXT — DEPTH-RESISTANCE (the missing mechanic)
A wrapped flank cell backed by reserve DEPTH should resist/refuse the wrap (reserves face outward and
counter the envelopers). Scale or negate the wrapper penalty by the defender's local column depth at the
wrapped flank: deep/refused flank -> strong resistance (penalty -> ~0); thin flank -> full penalty. This
should simultaneously pull H3 DOWN (Line's flanks have some depth) and lift H5/H6 (RefusedFlank's refused
column resists). Then re-run the full 13-test set + NERS Stage-4; PER_CELL=0 unchanged at every step.
DORMANT remains until the set is clean enough to consider PC_REFUSE default-on.
