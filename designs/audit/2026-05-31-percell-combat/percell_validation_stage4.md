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
