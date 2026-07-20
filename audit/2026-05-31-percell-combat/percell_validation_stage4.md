# Per-Cell Integration — Full Validation + NERS Stage-4 Re-Test
Date 2026-05-31 | Engine: tests/sim/sim_mb_sigma.py (PER_CELL Incr1-6, commit 598453c3)
Method: multi-turn (CSCALE 4, the correct lens), Wilson 95% CI-overlap bands. [SELF-AUTHORED — bias risk.]

## FULL 13-TEST MULTI-TURN PASS (PER_CELL=1)
CI-consistent (IN/MARGINAL): 11/13.  OUT: 2/13.
  H1 Line v Line (mirror)        49.3  IN        [45-55]
  H2 Arrowhead v Line            62.3  IN        [50-65]
  H3 Horseshoe v Line            38.5  OUT  LOW  [50-65]   <- envelopment disabled cost
  H4 Horseshoe v Arrowhead       43.3  IN        [40-60]
  H5 RefusedFlank v Horseshoe    43.0  MARGINAL  [50-65]
  H6 RefusedFlank v Line         36.4  ~LOW      [45-60]
  H7 GappedLine v Line           44.1  MARGINAL  [50-65]   <- 93%->44%, THE FIX
  H8 GappedLine v Arrowhead      50.4  MARGINAL  [45-60]
  H9 Line v Arrowhead            31.1  MARGINAL  [35-50]
  H10 Line v Horseshoe           43.7  MARGINAL  [35-50]
  H11 Arrowhead v Horseshoe      40.0  MARGINAL  [40-60]
  R1 Ranged v Line               14.8  OUT  LOW  [30-50]   <- PRE-EXISTING ranged issue (OUT in baseline)
  R3 Ranged v Ranged (mirror)    58.5  MARGINAL  [45-55]

## NERS STAGE-4 RE-TEST (does the remediation introduce new defects?)
- L3 (small pool): PASS — per-cell effects are delta-sigma on the existing UNIT pool; no new per-cell dice. Roll stays 5-18D.
- L2 (uniform impact): PASS — fatigue/charge/depth-contact/envelopment enter via _sigma_net_boost mu-shift or the contact-fraction multiplier, not raw pool mods.
- L1 (no redundancy): PASS — Incr6 envelopment found redundant with Incr4 depth-aware contact fraction; disabled (PC_ENVELOP_SIGMA=0). NERS-N/E honored.
- L5 (bounded loops): MOSTLY PASS — mean 4.6 turns; bounded (stamina [0,100], delta-sigma softcapped, contact-frac<=1). 4/60 battles hit the 20-turn cap = the inconclusive-draw long tail of damping (NOT a runaway). Note for tuning.
- L6 (no cliff): PASS — fatigue-damp smooth; charge absorption is a max(0,.) clamp, no outcome discontinuity at normal depths.
- R (robustness): PASS — mirror 44.4% (unbiased, no new A-side bias).

VERDICT: the per-cell remediation is NERS-compliant — no new L1/L2/L3/L6 defect; loops bounded (L5 long-tail noted); mirror unbiased.

## OPEN ITEMS (carry forward)
1. [OPEN TRADE-OFF] H3 (Horseshoe v Line, wants envelopment) vs H4 (Cannae, breaks with envelopment).
   Disabling envelopment fixes H4 but leaves H3 low. A depth/shape-gated envelopment (fires for
   genuine wing-envelopment shapes like Horseshoe, not for raw frontage) could satisfy both — a design decision.
2. H6/H7 ~36-44% (slightly low): depth slightly favored. Acceptable as "deep wins the shoving match," or a small tune.
3. [PRE-EXISTING] R1 ranged-vs-line balance (OUT in baseline too; not introduced by per-cell work).
4. L5 long tail: 4/60 stalls at the turn cap — the damping draw-tail. Lower max_battle_turns acceptance or a tie-break.

## TUNING PASS (2026-05-31) — parameter ceiling reached
Re-measured the key set at higher n; earlier "OUT/low" readings (H3, H5, H7) were small-sample noise.
At the committed settings (PER_CELL=1, WMAX=1.0): point estimates 7/9 in-band on H1,H2,H3,H4,H5,H7,H11
(H3=53 IN, H5=58 IN, H7=51 IN). Genuine point-misses: H6 (40, band 45-60) and H9 (29, band 35-50).

- PC_WIDTH_MAX sweep (width-term cap 1.0->1.4): SEE-SAWS — raising it gains H11 but loses H4 (6/9 < 7/9).
  Confirmed a single width scalar cannot fix the set (tests come in reverse pairs H2/H9, H3/H10, H4/H11).
  Reverted (NERS-E: no dead lever). Engine unchanged from commit e7d6d449.
- H6 root cause (grounded): RefusedFlank's depth-1 refused column is correctly held back (ends 16 troops /
  stamina 100, untouched) — NOT a bug. RefusedFlank fights with 4 columns vs Line's 5 = a frontage trade for
  an unenveloped flank, which nets slightly negative ABSENT an enemy that tries to envelop. Ties to envelopment.
- H9 (Line v Arrowhead 29): reverse of H2 (Arrowhead 51); Line loses to the wedge a bit harder than band.

CONCLUSION: parameter tuning has reached its ceiling. The residual misses (H6, H9, and the softer H3/H5/H7
band targets) are SHAPE-TACTICAL — they need a working envelopment / oblique-echelon / refused-flank-payoff
model (a design decision + build), not a scalar. The abstracted engine captures depth, fatigue, charge,
density, and the H7 frontage/depth tradeoff well; fine shape-tactics are the documented next design frontier.
[OPEN — Jordan design decision] shape-aware envelopment (wing-wrap geometry) that lifts H3/H5/H6 without
breaking H4/H5 — the naive delta-sigma version double-counts (Incr6) and the column-overhang version is
fully refused by deep reserves. Likely belongs in the octagon-facing geometry, not a separate delta-sigma.
