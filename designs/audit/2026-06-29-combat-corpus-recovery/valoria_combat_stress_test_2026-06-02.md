# Valoria Combat Engine — Comprehensive Stress Test & Validation
**2026-06-02 · combat_engine_v1 (committed) · validated against martial manuals + historical research (primary) and the four-state probability matrix (weighted reference)**

`[READ: weapon_matchup_matrix_v2.md §4/§8/§9 + A0–A3 CSVs; HEMA manual corpus (half-swording, displacement, hilts/quillons, spear); historical research (poleaxe vs mace, plate vs percussion, KCD community consensus as a weak signal)]`
`[SELF-AUTHORED — bias risk: I built this engine; findings below are surfaced as an independent reviewer would, worst-first, no false balance.]`

## WEIGHTING (per Jordan's framing + matrix §9)
- **Primary anchor:** martial manuals + historical research (qualitative consensus). A pass here matters most.
- **Secondary reference:** the four-state matrix — an expert-JUDGMENT model (its own §9), so the bar is DIRECTION + TIER agreement, not exact digits. Treated as weighted evidence, not ground truth.
- **Hard invariants:** mirror ~50, no-one-shot, the 95% cap, mastery dominance, feint symmetry/cap. These must hold absolutely.

## VERDICT
**Structurally sound; two hard-invariant bugs and one magnitude class remain.** The engine reproduces the qualitative
manual/historical consensus well (spear primacy, armour rotation, cut-collapse, clinch-in-armour, guard coherence,
skill dominance). Two genuine invariant violations were found by the stress battery (95%-cap leak; armour
non-monotonicity). The dominant quantitative error vs the matrix — percussion (mace) over-credited and the
longsword's half-sword/bind package under-credited in plate — is now HISTORICALLY ANCHORED, not matrix-chased.

---

## FINDINGS (worst-first)

### F1 — [HARD-INVARIANT BUG] The 95% upset cap leaks above 95% across multi-bout fights
A maximal mismatch (all-7/H7 vs all-1/H1) returns **97%**, not ≤95%. `UPSET_FLOOR=0.05` is applied per-bout but the
best-of-bouts aggregation re-concentrates above the cap. **Severity: high** — it is a stated design invariant (every
fight must remain winnable/losable within [5%,95%]). Fix: apply the upset floor to the FIGHT result, not per-bout, or
lower the per-bout floor so the aggregate lands ≤95%.

### F2 — [HARD-INVARIANT BUG] Armour is non-monotonic (medium < light vs an unarmoured foe)
Win% vs a naked opponent (mirror weapon): none 53 → light **80** → medium **58** → heavy 82. Medium armour performs
WORSE than light — a threshold-cliff defect (the diagnostic skill's Lesson 6). Cause: at `medium` the opponent's
`cut_thrust` mode-shifts to a gap-thrust point and claws back armour-defeat σ, but at `light` it does not, so light
paradoxically beats medium. **Severity: high** — armour must be monotonic (more protection ≥ less). Fix: smooth the
mode-shift/defender-shield transition across light→medium→heavy so no rung inverts.

### F3 — [MAGNITUDE, historically anchored] Percussion over-credited; longsword half-sword/bind under-credited in plate
A0→A3 matrix sign-agreement: 76% / 62% / 61% / 68%; mean |Δ| 22–31pp. The bulk of the A2/A3 sign-flips are one
pattern — a plain one-handed **mace beating the poleaxe and the armoured longsword**:
| matchup (A3 plate) | engine | matrix | manuals/history |
|---|---|---|---|
| mace vs poleaxe | 75 | 10 | poleaxe out-reaches + out-swings the mace; mace should LOSE |
| longsword vs mace | 17 | 85 | skilled armoured longsword (half-sword + bind/grapple) should WIN |
| longsword vs arming | 41 | 85 | armoured-combat longsword dominates a one-hand cut-thrust sword |
| rapier vs greatsword | 96 | 25 | a rapier should not dominate a greatsword in plate |
**Historical basis (validated this session):** maces/warhammers ARE the armour-defeat tool ("designed to counter
mail," "dent the armor") — so percussion rising in plate is correct in DIRECTION. But the mace is "better against
*unskilled* or easily-overpowered opponents"; against a skilled equal it lacks reach, tempo, and any bind/parry game.
The engine credits percussion armour-defeat too heavily and gives the mace no penalty for its poor reach/tempo/bind in
the armoured close. **Severity: medium** (direction right, magnitude wrong; it's the largest single error source).
Fix: lower percussion's armour-defeat weight relative to the reach + half-sword-thrust + bind package; ensure the
mace pays its reach/tempo/bind cost in the close.

### F4 — [MAGNITUDE] Reach is near-insuperable to skill at the extreme
H6 dagger vs H3 spear = **6%**. A three-grade skill gap barely dents a reach disadvantage. Manuals + the matrix §8
both rank SKILL as the dominant factor ("skill outweighs all"); a large skill edge should move a reach matchup more
than 6→? **Severity: low–medium.** Related to the long-standing longsword-vs-spear cell (reach persists even when it
should become a liability — the CLINCH primitive, still pending, is the structural fix). Note D5 already shows the
clinch working in ARMOUR (dagger vs spear 6→66 A0→A3); the unarmoured case needs the same reach→clinch decay.

---

## WHAT PASSED (the primary anchor — manuals + history)

**Qualitative consensus — all reproduced:**
- **Spear primacy unarmoured** (reach governs, cross-cultural): spear favoured vs every weapon (91 vs arming, 94 vs
  dagger/mace), weakest vs the rapier's fast in-line thrust (59). ✓
- **Armour rotation:** poleaxe rises A0→A3 (68→77); the sabre's CUT collapses in plate (79→5). Matches "cuts die vs
  plate; percussion/armour-defeat governs." ✓
- **Clinch/grapple decides in armour:** dagger vs spear 6→66 from A0→A3 — once in armour the spear's reach becomes a
  liability and the rondel-in-the-clinch finish dominates (the manuals' armoured-combat reality). ✓ (emergent, not
  hand-set)
- **Skill dominance:** skilled-naked vs unskilled-plate = 51 (skill fully offsets a full armour grade). ✓ (except the
  reach extreme, F4)
- **Half-sword** auto-switches vs plate (mit dem kurzen Schwert). ✓ (magnitude tied to F3)
- **Guard coherence ("don't parry with your hands"):** rapier parry σ +0.29 (swept hilt) >> spear −0.05 (guardless);
  longsword out-binds spear (+0.76) and rapier (−0.87 vs longsword); fore/thumb-ring winding modelled. ✓

**Hard invariants — pass except F1/F2:**
- Mirror 50 (identical fighters); zero-skill mirror 49. ✓
- No-one-shot: max single blow 18 < End-2 Health 24. ✓
- Mastery monotonic in History: H1→H7 = 29/39/49/55/64/76/81. ✓
- Reading monotonic (up to MC noise): 53/86/93/96/95. ✓
- Traditions modest: german vs none = 50 (not dominant). ✓
- Feint symmetric (mirror 50 on/off) and capped at 3; not overpowered (collapses vs a strong reader). ✓
- All-floor vs all-ceiling = 5 (capped, decisive). ✓

---

## STRESS BATTERY (method, for reproducibility)
- **A — degenerate/boundary:** mirror, all-floor-vs-ceiling, max reach gap, naked-vs-plate, zero-skill, plate clinch.
- **B — monotonicity:** win% swept over History / Armour / Reading vs a fixed baseline (found F2).
- **C — weapon matrix:** full mapped 11-weapon set × A0–A3, mean |Δ| + sign-agreement + catalogued sign-flips.
- **D — qualitative historical findings:** spear primacy, armour rotation, skill dominance, half-sword, clinch, guard.
- **E — invariants:** mirror, no-one-shot, 95% cap (found F1), traditions, feint.
- MC n=380–1200/cell; ±2–4pp noise; seeds logged (4001–4003).

## REMEDIATION QUEUE (worst-first)
1. **F1** apply the 95% upset floor to the fight result, not per-bout (hard-invariant; small fix).
2. **F2** smooth the light→medium→heavy mode-shift/defender-shield transition (hard-invariant; threshold-cliff).
3. **F3** rebalance percussion armour-defeat vs the reach/half-sword/bind package; mace pays reach/tempo/bind cost in
   the close (largest matrix error; historically anchored).
4. **F4 / CLINCH** extend the reach→clinch decay to the unarmoured close so skill + getting inside can overcome reach
   (the pending clinch primitive; already proven in armour via D5).

`[CONFIDENCE: high on the qualitative passes and the two invariant bugs (deterministic/observed); medium on exact
matrix magnitudes — the matrix is a judgment model, weighted accordingly. MC noise ±2–4pp.]`

---
# POST-BATTERY ACTIONS (same session) — F1 retested, F2 fixed

## F1 — FALSE POSITIVE (corrected)
The "95%-cap leak (97%)" was **MC noise at n=1200 on one seed**, not a real bug. Re-tested at n=4000: capped rate
= 94.6% (matches the analytic prediction 95.0% within noise). The cap is applied correctly to the FIGHT result and
works. No fix needed. `[CORRECTION: F1 — retest at higher n shows the cap holds; original finding was sampling noise.]`

## F2 — FIXED (major cliff removed; small residual on one rung)
Root cause confirmed: the `cut_thrust` mode-shift was a discrete cliff at the light→medium boundary (cut→point),
so a defender taking MORE armour flipped the attacker into a stronger mode. **Fix (both σ and damage sides):** a
cut-and-thrust head now uses `max(cut, half-sword-point)` capability/transmit at EVERY armour level — the attacker
always picks its best mode, so more defender-armour never makes the attacker stronger. Monotonicity via the rising
per-state threshold. Verified: the medium→heavy inversion is gone (e.g. none 48 / light 46 / medium 64 / heavy 84).
A small residual remains (none ≈ light, occasionally none > light by ≤6pp vs a naked foe) — light armour's shield is
marginally too weak to always beat bare; folded into the A1-mail-dials work (F-A1 below). A1 matrix mean|Δ| improved
27.9→26.1pp; A0/A2/A3 unchanged; invariants hold (mirror 49, no-one-shot 18<24).

## REMAINING (revised, worst-first)
- **F3** percussion over-credited vs the reach/half-sword/bind package in plate (the largest matrix error;
  historically anchored: poleaxe out-reaches/out-swings the mace, and the mace loses to a skilled armoured longsword).
- **F-A1** light-armour rung: give light a small guaranteed net benefit over bare (closes the F2 residual + the
  weakest matrix state, A1 62%). The reference itself tags A1 "medium confidence, mixed."
- **F4 / CLINCH** extend the reach→clinch decay to the unarmoured close (proven in armour, D5) so a large skill edge
  can overcome reach (H6 dagger vs H3 spear currently 6%).

`[CONFIDENCE: high — F1 retested deterministically, F2 fix verified across seeds + matrix no-regression.]`

---
# F3 WORK + CLINCH ATTEMPT (same session)

## F3 — REACH ALIGNMENT (committed eb5535e) — the largest single win this session
Diagnosis (instrumented, not guessed): the mace overperforming in plate was NOT "percussion too strong." The
reference §4 has poleaxe and mace at EQUAL percussion (8); the poleaxe beats the mace on REACH (6 vs 3) and clinch
(5 vs 4). The engine's reach formula gave the mace 6.0 and poleaxe 6.8 — far too close, and the longsword 7.30
(over-reaching; should be ~6.4, below the spear by more). **Fix:** added a per-weapon `reach_adj` so engine reach
tracks the validated §4 reach ordering (mace/warhammer short ~5.4; longsword shorter ~6.4; etc.). **Result: every
state improved** — A0 22.5→18.1pp, A1 27.9→22.2pp (sign +5), A2 sign +8 (→69%), A3 sign +9 (→77%). Mace correctly
sinks unarmoured (mace>arming 17, matrix ~15). Sanity held. This was a structural correctness fix (reach now matches
the period-validated ordering), not a per-cell tune.

## CLINCH primitive — BUILT, VALIDATED, DELIBERATELY NOT COMMITTED
Added the reference §4 `clinch` attribute to all weapons + a `clinch_sigma` module + a closed-phase reach-decay
(armour-scaled), grounded in the reference's explicit "reach falls, clinch rises with armour; the grapple decides
plate" dial. It **fixed the cells it targeted** — longsword>arming-in-plate 53→84 (matrix 85), dagger>spear correctly
armour-scaled (A0 8 / A3 96), longsword>spear A0 19→~30. **But on the aggregate it was a net wash-to-negative:** A1
improved (−1.6pp) but A2 worsened (+3.9pp, sign −7) and A0 sign dropped, even after moderating the medium/heavy
clinch weight. The clinch helped specific sign-correctness at the cost of A2 magnitudes broadly.

**Decision (discipline):** REVERTED the clinch wiring rather than commit a net-negative change. The engine is back at
the clean reach-aligned state (eb5535e). The `clinch` attribute remains as inert data, ready for a focused future
pass. Committing a primitive that's structurally right but not yet a net improvement would be the opposite of the
diligence asked for — better to land the clear win (reach) and leave clinch for proper calibration.

## STATE (end of session)
Committed and live: reach alignment (eb5535e) on top of the F2 fix (c75d6da), guards (e19216c), modularization
(600b8718), and the canonized engine + ratification proposal. **4-state: A0 18.1pp/73%, A1 22.2pp/67%, A2 26.4pp/69%,
A3 28.7pp/77%** — the best aggregate of the session. Clinch built but parked (not committed).

## REMAINING (revised, worst-first)
- **CLINCH calibration** — the primitive is built and grounded; it needs a focused pass to be a net win (likely:
  apply clinch only where the closing weapon has a real clinch edge AND keep A2 magnitudes from overshooting — the
  A2 "transitional" state is the most sensitive). Re-attempt in isolation, not layered with other changes.
- **F3 residual** — mace>poleaxe still ~49 (matrix 10) and longsword>arming-in-plate ~53 without clinch; both are
  what the clinch primitive fixes, so they're really blocked on clinch calibration.
- **F-A1 light-armour rung** (F2 residual + weakest state A1).
- **A1 mail dials** (cut-fade / thrust-rise / percussion-rise tuned distinctly from plate).

`[CONFIDENCE: high — reach win verified across the full matrix; clinch revert verified to restore eb5535e numbers.]`

---
# CONTINUED WORK — clinch re-attempt (parked again) + light-armour fix (committed 3bb5df7)

## CLINCH — re-attempted surgically, PARKED AGAIN (cleaner evidence)
Hypothesis from the first failure: the reach-DECAY (not the clinch term) hurt A2. Re-tested with a gentle,
heavy-focused reach-decay and heavy-concentrated clinch weights, swept against the full 4-state. Result: even
"heavy-only" clinch still regressed A2 (26.7→27.4pp, sign 69→63) and A3 (28.9→30.6pp, sign 77→74) vs the no-clinch
baseline. **Conclusion (now twice-confirmed):** a global clinch σ-term isn't net-positive on this matrix — after the
reach fix, plate cells are mostly sign-correct, so the clinch term mostly perturbs magnitudes, pushing as many cells
wrong as right at medium/heavy. The cells it should fix (mace>poleaxe, longsword>arming-in-plate) need a FAR more
TARGETED instrument (fire only on genuine pure-reach-vs-clinch-weapon mismatches), not a broad term. Reverted again;
`clinch` stays as inert data. Not forcing it.

## F-A1 LIGHT-ARMOUR RUNG — FIXED & COMMITTED (3bb5df7), clean net positive
Diagnosis (instrumented): light armour reduced a cut only 12→11 (RESIST cut at light was 0.35 — 65% got through),
AND the adef term gave the ATTACKER +0.14σ against a light defender (threshold 0.30 too low) — so wearing light
armour was a slight LIABILITY (light vs none ≈ 45%). Both wrong vs the reference (§3: mail "largely defeats cuts";
stiff thrusts/percussion pierce). **Fix:** RESIST cut at light .35→.60 (mail defeats cuts) + ADEF_THRESHOLD light
.30→.70 (so pure cutters like sabre/arming are SHIELDED by mail at −0.6/−0.0, while stiff thrust/percussion —
dagger/spear/mace — still PIERCE at +0.1/+0.0/+0.2; longsword neutral). **Result:** armour now strictly MONOTONIC
across 3 seeds (none~50 < light~55 < medium~62 < heavy~84); A1 sign 67→70%, A2 sign 69→73%, A0/A3 held; invariants
intact (mirror 50, mastery 78, spear>dagger 95, no-one-shot 18<24). Historically grounded, not matrix-chased.

(Commit hit a CollisionError — HEAD moved mid-session, the normal optimistic-concurrency signal; re-fetched + retried
per protocol; verified the fix landed and files coherent.)

## STATE (end of this turn)
Live commits: light-armour fix (3bb5df7) on reach-align (eb5535e), F2 (c75d6da), guards (e19216c), modularization
(600b8718), canonized engine + ratification proposal. **4-state now ≈ A0 17.6pp/73%, A1 22.2pp/70%, A2 26.6pp/73%,
A3 28.6pp/78%** — best of session; the two hard-invariant defects (95%-cap false alarm; armour non-monotonicity) are
both resolved. F2 residual closed.

## REMAINING (worst-first)
- **TARGETED clinch** — a narrow rule for pure-reach-vs-clinch mismatches in armour (spear/pike vs dagger/longsword),
  not a global term. Blocks mace>poleaxe (49 vs 10) and longsword>arming-in-plate. Needs isolated design.
- **A1 mail dials** — now that cuts are shielded at light, retune thrust/percussion-rise at A1 distinctly (A1 still
  the weakest at 22pp, though sign now 70%).
- **A2/A3 magnitude** — mean|Δ| ~27-29pp; the long tail of judgment-model disagreement (matrix §9), lower priority
  than sign-correctness which is now 73-78%.

`[CONFIDENCE: high — light-armour fix verified net-positive across all 4 states + monotonicity across seeds; clinch
revert verified clean; commit landed despite collision (re-fetched, retried, verified).]`

---
# METHOD RECALIBRATION + EMERGENT TIER VALIDATION (per Jordan: not seeking parity; validate top-down vs history)

## Reframing (corrects a drift)
Prior turns drifted toward treating matrix mean-|Δ| / sign-agreement as the objective. Corrected: **the matrix is a
weighted sanity reference, not a fitting target; lopsided matchups are correct emergent outcomes, not errors.** The
real test is whether the primitives are physically sound and the EMERGENT behaviour matches the historical record
top-down. Validation below is by emergent weapon TIER vs the historical/manual consensus; matrix is secondary.

## Emergent tier-list validated TOP-DOWN against the historical record
Ran each weapon's average win% vs the field, per armour state.

**A0 unarmoured** — historically sound: spear top (cross-cultural primacy ✓), staff/greatsword/sabre high (reach +
"perfect length" ✓), **mace (11) and dagger (14) at the bottom** (reference §8: percussion + short weapons sink
unarmoured ✓). Two genuine findings: **rapier tied #1 (80)** is too high (battlefield-equal of the spear overstates a
civilian thrust-specialist — the movement-legibility primitive likely over-rewards the in-line thrust); **longsword
(42)** is a touch low for its historical standing. Both logged for a focused pass.

**A3 full plate** — historically sound AFTER this turn's fix: **poleaxe the apex (83)** ✓ (the preeminent armoured
foot-combat weapon), **dagger/mace rise dramatically** (14→74, 11→72 — the rondel-in-the-grapple + percussion
armour-defeat tools ✓), **cuts collapse** (sabre 5, greatsword 14, rapier 31 at the bottom ✓). These are exactly the
manual/§8 rotations.

## PERCUSSION-AUTHORITY primitive — committed (7272d59), the turn's fix
The tier-list surfaced a physical error the matrix-chasing had missed: the **quarterstaff was top of the plate
tier (83)** — historically wrong (wood does not defeat plate). Root cause: ALL `blunt` heads got identical
armour-defeat regardless of material/mass-concentration. **Fix (emergent, §4-grounded):** added a `percussion`
attribute (§4 values: staff 4, mace/poleaxe 8, warhammer 9, swords 1-4) scaling BOTH blunt armour-defeat σ AND blunt
damage transmit (perc 8 = steel-hammer reference). Now a wooden staff transmits half a steel hammer's percussion
through plate. **Emergent result:** poleaxe correctly becomes the plate apex (83); staff drops to 4th (67), below
every genuine steel armour-defeat weapon — the historically essential ordering. A0 untouched (percussion is zero-
effect unarmoured). Monotonicity holds ([52,56,64,84]); invariants hold (mirror 50, mastery 78); matrix secondary
reference even improved (A2 26.6→25.4, A3 28.6→26.9) — a bonus, not the goal.

(Commit hit a CollisionError — another session is active, 7 handoffs; re-fetched + retried per protocol; verified
the 4 files landed coherently.)

## REMAINING (worst-first, historical-precedent framed — NOT parity-seeking)
- **Rapier over-strong unarmoured** (tied #1; should be strong-but-not-spear-equal) — likely the legibility primitive
  over-rewarding the in-line thrust; revisit legibility magnitude.
- **Longsword slightly under-valued unarmoured** (42; historically upper-mid).
- **Targeted clinch** for genuine pure-reach-vs-clinch mismatches in armour (spear/pike vs dagger inside the point) —
  a narrow rule, not the global term twice-shown to be net-negative.
- **Note:** another session is active in this project (7 handoffs) — handoff consolidation may be warranted per the
  document-consolidation discipline before further multi-session divergence.

`[CONFIDENCE: high — emergent tiers validated against the historical record; percussion fix grounded in §4 + physics,
verified to make the plate ordering historically correct without regressing monotonicity/invariants.]`

---
# GEOMETRY LAYER — committed (36abf82), per Jordan: derive coefficients from physical geometry

## What & why
Jordan: the head categories and hand-set `gap` are categorical PROXIES for geometry; to differentiate curved-vs-
straight edges (cut + its thrust interaction) and point-vs-broad force concentration, weapons need geometric
parameters (curvature, circumference/cross-section). Engineering key: bake the geometry→coefficient SURFACE at build
time so runtime cost is unchanged.

## Built (modular + precomputed, zero runtime cost)
- **`geometry.py`** (new pure module): derives combat coefficients from geometry —
  - `gap_precision(point_concentration, cross_section)`: force concentration (fine point) × RIGIDITY; a fine point on
    a whippy blade (rapier) loses plate-thrust authority, a fine rigid point (estoc/rondel/dagger) keeps it.
  - `thrust_factor(point, rigidity, curvature)`: rises with point+rigidity, FALLS with curvature (offset point).
  - `cut_factor(curvature, edge_keenness)`: keen edge + curvature's draw/slice bonus.
  - `percussion_concentration(strike_concentration)`: beak/pick concentrates vs broad face (for blunt heads).
  - `can_halfsword_thrust(curvature, point)`: a straight usable point can half-sword; a curved blade cannot.
  - `bake(params)`: precomputes the full coefficient surface for one weapon.
- **Geometric parameters** added to every weapon (curvature, point_concentration, cross_section, edge_keenness,
  strike_concentration). Baked ONCE at import — each weapon's `gap` is now geometry-DERIVED (hand-set value
  replaced), and the full baked surface (`geo`) is attached for downstream wiring.

## Calibration discipline (preserve validated work)
Geometry was calibrated to REPRODUCE the validated §4 `gap` column (max |Δ| = 0.12, rest within ~0.10 — inside MC
noise). **Emergent tiers + invariants preserved:** A0 spear top (84), mace/dagger bottom (13/15); A3 poleaxe apex
(86), percussion/armour-defeat high, cuts collapse (sabre 5); monotonicity [51,57,75,91]; mirror 47, mastery 78,
spear>dagger 94, no-one-shot 18<24. The geometry SUBSUMES and refines the head/gap system rather than fighting it.

## Remaining wiring (next, not rushed)
- **Curvature → cut/thrust** is DERIVED (`cut_factor`/`thrust_factor` in the baked surface) but not yet CONSUMED by
  the resolver — the engine still uses head categories for cut/thrust mode selection. Next: have the curved-vs-
  straight cut/thrust tradeoff read the baked `geo.thrust`/`geo.cut`/`geo.halfsword` (so e.g. a straight greatsword
  retains more thrust than a curved sabre, continuously). This is the differentiation Jordan most wants; the surface
  is ready, the consumption is the step.
- Circumference currently enters as `cross_section` (rigidity). A literal cross-section SHAPE (round vs square vs
  diamond) could refine percussion/cut further if needed, but rigidity captures the load-bearing effect for now.

`[CONFIDENCE: high — geometry calibrated to reproduce validated tiers; emergent ordering + invariants verified
preserved; module is pure + baked (zero runtime cost) as specified.]`
