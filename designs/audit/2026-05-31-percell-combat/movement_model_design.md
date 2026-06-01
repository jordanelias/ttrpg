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

## [CORRECTION] MIRROR IS NOT UNBIASED — depth-resistance added but M3 still mirror-biased (2026-05-31)
Prior claim (855b619) that structural wrap detection is "mirror-stable BY CONSTRUCTION (H1 50.0)" is
FALSIFIED. n=100 at a different seed base showed H1 57.8 / H3 68.4, and a direct diagnostic confirmed M3
shifts the mirror: Line-v-Line refuse-off vs refuse-on at seed+222 = 54.1 -> 57.8; at seed+1,000,000 =
45.4 -> 50.0. Refuse-on is NOT identical to refuse-off and consistently favours A by ~+4.

Root cause: the static "equal width -> no wrappers" argument does NOT hold during the DYNAMIC battle —
integer movement + the advance_dir sign make A's and B's column spans DRIFT unequally, so wrappers appear
asymmetrically even in a nominal mirror. M3's wrapper/RED detection (an extremum-style test) amplifies that
sub-cell asymmetry into a consistent directional bias; the refuse-off centroid path averages it out (which
is why the wheel-only mirror sits ~50 with only seed noise: 54.1/45.4). The structural fix REDUCED the bias
(from +7-12 down to +4) but did not remove it.

DEPTH-RESISTANCE (committed, dormant): PC_ENVELOP_DEPTH_RESIST=0.3 scales the rear-wrap penalty by the
wrapped column's depth (reserves resist the wrap; Clausewitz). This is a real BALANCE gain — H3 falls from
~80 to ~60-68 (borderline IN/HIGH, seed-dependent), and at n=50 the set reached 6 IN (H1/H2/H3/H4/H10/H11)
with H5/H7/H9 near-miss. But it does NOT touch the mirror bias (orthogonal: detection asymmetry, not magnitude).

NET STATUS: envelopment EMERGES and BALANCES far better than any prior version, but M3 remains DORMANT and
is NOT default-viable until the mirror bias is eliminated. The gating problem is fundamental: any position-
sensitive flank detection amplifies the asymmetric integer-movement drift between A (advance -1) and B
(advance +1). Candidate fixes (next): (a) make advance/​wheel rounding exactly symmetric so A/B spans drift
identically; (b) replace the extremum detection with a symmetric net-overhang measure (A's overhang of B
minus B's overhang of A) so a true mirror nets to zero wrappers regardless of drift. Option (b) is the
more tractable and directly targets the asymmetry. PER_CELL=0 and PER_CELL=1/refuse-off remain byte-exact
to the committed wheel engine (verified this session).

## F3 — MIRROR FIXED BY CONSTRUCTION (nominal-width/span gate), 2026-05-31
Fix: a wrapper requires the attacker to be NOMINALLY WIDER than the defender, measured by the column SPAN
of the static oriented pattern (not drifted live positions, and not distinct-column count). Span is
symmetric under the A<->B swap, so a true mirror has equal span -> ZERO wrappers -> the refusal path
contributes nothing. PROVEN: in a Line-v-Line mirror, mod=-1 is byte-identical to mod=0 (envelopment inert)
at multiple seeds -> mirror unbiased BY CONSTRUCTION (not merely on average). SPAN (not count) so a gapped
formation is correctly "wide" by reach.

[CORRECTION] This supersedes the prior-commit flag that M3 "biases the mirror +4". That was an OVERREAD of
sampling variance: at n<=120 the mirror swings ~+/-7 per seed (42-57); the +4 came from two same-direction
seeds, and a third seed gave -5.7. Aggregated over seeds the mirror was ~50 throughout. F3 removes both the
spurious-wrapper noise and the conceptual concern; the mirror is now inert-by-construction.

RESULT (F3 span gate, mod=-1.0, resist=0.3, 2-seed aggregate n=120): 6/10 IN —
  H1 48.6, H2 52.6, H3 64.5 (headline, IN), H4 40.7, H9 36.6, H10 44.0.
  H11 60.2 (marginally HIGH), H5 39.4 LO, H7 43.8 LO, H6 34.6 LO.
Remaining (all NON-mirror, dormant-path only):
 - H5 RefusedFlank-v-Horseshoe LO: a refused/deep flank should RESIST the wrap (needs the refused-flank
   facing mechanic — refused cells face outward to meet envelopers; depth alone is insufficient because the
   refused column is shallow).
 - H6 RefusedFlank-v-Line LO: equal SPAN -> envelopment-inert -> this is the PRE-EXISTING base value, not M3.
 - H7 GappedLine-v-Line LO: the gap dynamics (Line cells sit in the gaps) blunt the wrap; needs inspection.
 - H11 marginally HIGH: Arrowhead (widest) over-wraps Horseshoe; within ~0.2 of band.

STATUS: envelopment EMERGES, is PROVABLY mirror-clean, H3 in band, 6/10 IN. Still DORMANT (PC_REFUSE off);
flipping default-on is Jordan's call pending H5/H7 + a high-n NERS Stage-4. PER_CELL=0 and PER_CELL=1/
refuse-off remain byte-exact to the committed wheel engine (verified).

## H5 / H7 DIAGNOSIS (instrumented, 2026-05-31) — mechanic validated; remaining misses are design questions
Per-tick a_angle_mod/b_angle_mod capture (seed 42, multi-turn), F3 defaults:
 - H7 GappedLine(A)-v-Line(B): A_mod mean +0.000 (0/47 ticks penalised), B_mod mean -0.206 (47/47).
   => the envelopment fires CORRECTLY — Line is wrapped, GappedLine is not. GappedLine still loses in
   aggregate (H7 43.8) because of its OPEN GAP: pattern cols [0,1,2,3,5,6,7,8] (gap at col 4), 24 cells vs
   Line's 25, so it is frontally weaker. The mechanic is right; the gap is a base-combat disadvantage.
   DESIGN QUESTION: should a single gapped line beat a solid line of equal troops (band 50-65)? The open
   gap is a real vulnerability; the manipular gap historically relied on covering depth lines, which a
   single subunit does not have. Either the band is optimistic, or GappedLine's gap should confer a
   non-combat advantage (flexibility/rotation) not modelled here. NOT a mechanic fix to invent — Jordan call.
 - H5 RefusedFlank(A)-v-Horseshoe(B): A_mod mean -0.186 (50/53 penalised), B_mod +0.000.
   Geometry: RefusedFlank cols 0-3 front at row 0 (depth 6); col 4 is a single cell at row 6 — genuinely
   PULLED BACK = the angled refusal. That refusal denies the Horseshoe's wing on the col-4 side, but the
   Horseshoe is a DOUBLE envelopment (both wings, span 7 > 5): the UNREFUSED deep flank (col 0) is wrapped,
   which is the -0.186. So RefusedFlank takes a half-envelopment. A refused-column exemption would not move
   this (the penalty is on the unrefused flank, not col 4).
   DESIGN QUESTION: should a one-side refused flank beat a double-envelopment shape (band 50-65)? Refusing
   one wing blunts the pincer to a single envelopment; whether RefusedFlank's depth then wins is a balance
   call, not a correctness bug. Cranking magnitudes to hit the band without a principled anchor is barred by
   the project-owner contract — Jordan call.

CONCLUSION: the envelopment model is mechanically SOUND and validated — mirror unbiased by construction,
H3 (Horseshoe-v-Line) in band, 6/10 IN. The remaining misses are NOT envelopment bugs: H6 is the
pre-existing base value (equal span -> envelopment-inert), H7 is a base gap-disadvantage where the
envelopment is correct, H5 is a refused-vs-double-envelopment balance question, H11 is marginal (~0.2 over).
These four are design/balance decisions (band expectations, GappedLine gap advantage, RefusedFlank strength)
for Jordan, not mechanic work. M3 remains DORMANT (PC_REFUSE off); the engine default is the ratified
wheel-only PER_CELL=0, byte-exact and untouched.

## POCKET / GAP-TRAP PRIMITIVE (Polybius-grounded), committed 218d69bc — 2026-05-31, dormant
Research (top-down): the manipular quincunx gaps were NOT a weakness vs a rigid line — Polybius/Wikipedia:
gaps "lured hoplites in and disrupted their formation, after which they became disorganized, SURROUNDED,
and easy prey"; gaps in each line were covered by the line behind. So a gapped line should BEAT a solid
line via the gap-trap; band 50-65 is historically right. Missing primitive: an enemy cell that pushes into
a gap is surrounded on both sides.

Primitive (bottom-up): a defender cell with enemy cells LEVEL (same rank) on BOTH lateral sides is pocketed
(PC_POCKET_MOD=-1.0, reach 2), not refusable (cannot turn to face both). Fired ONLY where the wrap did not
(worst_mod==0): the gap-flanking maniples sit WITHIN the defender's frontage span (not wrappers), so the
trapped cell gets the pocket; the Horseshoe's concave wings are BEYOND the span (wrappers), so those cells
take the depth-scaled wrap instead — no double-count. Mirror-safe by construction: parallel lines put
enemies AHEAD (a different rank), never beside on both flanks.

RESULT (2-seed n=100): 7/10 IN (up from 6). H7 GappedLine-v-Line 44.7->48.9 (borderline IN — the gap-trap
emerging); H11 came INTO band (the no-double-count routing); H3 held 60.4 (NOT over-boosted, vs 71 when the
pocket double-counted); H1 mirror 50.6 (clean). Iteration that got here: unrestricted pocket lifted H7 but
double-boosted H3->71; a friendly-beside test wrongly suppressed H7 too; the worst_mod==0 gate cleanly
separates gap-trap (H7) from concave (H3).

Remaining:
 - H5 RefusedFlank-v-Horseshoe LO (39.8): the refused-flank RESISTANCE mechanic is the next piece — a
   refused flank (col 4 pulled back) should deny the enveloping wing on its side; needs the refused cells to
   face/meet the wrapper rather than be wrapped. (Research next: oblique order / refused flank vs envelopment.)
 - H6 RefusedFlank-v-Line LO (22.8, regressed): plausibly CORRECT top-down — a refused flank is WASTED vs a
   frontal line (no flank threat to refuse, just surrendered frontage), so RefusedFlank should lose to an
   equal Line; band 45-60 is likely optimistic. A Jordan band call, not forced here.
STATUS: mirror-clean by construction, H3 in band, gap-trap grounded + emerging, 7/10 IN. DORMANT (PC_REFUSE
off); PER_CELL=0 ratified engine byte-exact and untouched.

## H5 DIAGNOSIS (researched + instrumented), 2026-05-31 — refusal works; the gap is an oblique OFFENSE model
PC_REFUSE flipped default ON (commit b2a7af80): the envelopment model is now active in the per-cell path.
PER_CELL still default OFF -> shipped engine (PER_CELL=0 = base 0dea67d1) byte-exact, unchanged.

Research (top-down, Frederick/Leuthen, Epaminondas/Leuctra, oblique order): refusing a flank (a) WITHDRAWS
and protects the weak flank ("protected that part of the line not yet engaged"), (b) FIXES the enemy facing
it, and (c) lets you CONCENTRATE the strong wing to ROLL UP one enemy flank. It is an OFFENSIVE maneuver,
not a defense against being enveloped.

Instrumentation (per-column worst_mod, RefusedFlank(A) vs Horseshoe(B), abs cols 9-13 = oriented 0-4):
  col 9 (or0) -0.406 | col 10 (or1) -0.435 | col 11 (or2, CENTRE) -0.745 ~pocket | col 12 (or3) -0.336 |
  col 13 (or4, the REFUSED flank) NOT penalised.
=> The refusal WORKS — the withdrawn flank (col 13) is correctly never wrapped. RefusedFlank loses because
its CENTRE is Cannae-pocketed by the Horseshoe's concave as it advances in, and its near-flanks wrapped. The
engine is correctly modelling "advance into a concave -> get enveloped." A refused flank does NOT defend
against that; its historical value is the OBLIQUE OFFENSE (concentrate the deep wing, roll up one Horseshoe
wing before the mouth closes), which the current envelopment-GEOMETRY resolution does not model.

Two honest paths for H5 (band 50-65, gets ~40):
 (a) BAND RECONSIDERATION: a refused-flank formation that simply advances into a Cannae double-envelopment
     SHOULD lose; the band assumes RefusedFlank executes its oblique offense. If the engine resolves shapes
     by advancing-and-enveloping (no concentrated breakthrough maneuver), RefusedFlank-beats-Horseshoe is
     optimistic. Jordan band call.
 (b) OBLIQUE-OFFENSE PRIMITIVE (substantial): model the concentrated strong-wing breakthrough — a deep,
     concentrated wing that contacts a thinner enemy wing rolls it up (local depth/mass breakthrough), giving
     RefusedFlank (and any oblique attacker) an offensive edge that can pre-empt the concave. This is a new
     maneuver primitive (asymmetric concentration + flank roll-up), warranting its own focused build, not a
     scalar. Validate top-down vs Leuthen/Leuctra (the refused-wing-then-roll-up sequence).
RECOMMENDATION: build (b) as the next focused primitive (it also enriches Arrowhead/wedge breakthrough), or
take (a) if the resolution model is meant to stay envelopment-only. NOT forced here.
