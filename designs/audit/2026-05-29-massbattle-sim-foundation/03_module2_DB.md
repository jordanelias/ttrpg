# Mass Battle Sim — Module 2 (D-B: Bottom-Up TroopCount Model) Results

**Date:** 2026-05-29
**Task:** simulation (gated; sim_gate passed; verification ledger present)
**Decision in force:** D-B (complete the bottom-up TroopCount model) — approved by Jordan.
**Commit status:** nothing committed (B6). D-B engine (`sim_v22_db.py`) local; staged for manual push.

---

## Verdict

D-B is implemented and its casualty target is met **emergently** — loser ~25–30%, winner ~20% in decisive matchups, the historically-correct magnitude and asymmetry, falling out of the rout triggers rather than from tuning. `CASUALTY_SCALE` governs pacing, not casualty %. The formation counters remain at the v9 level (5/11 melee), confirming again that the bottom-up accounting does not fix the counters — that is M3. One coupled defect surfaced (morale-erosion mis-dimensioning) and folds into M3.

---

## What D-B implements
TroopCount model completed coherently: HP = soldiers (Size×BLOCK_SIZE, retained), and **all four casualty sources** scaled to soldiers via a single constant `CASUALTY_SCALE`:
- engagement damage (both sides), pursuit damage, freed-attacker damage.
- (Volley left on its existing scale — ranged unification is M5/ED-822, scoped out.)

This is distinct from the prior-turn ratio-restore *proxy* (which reverted HP to Size×h_per_size). D-B keeps the bottom-up soldier model and scales casualties into it.

## Casualty calibration — target MET emergently
Across `CASUALTY_SCALE` ∈ {4…20}, H1 mirror casualty held at **24.8–25.9%** — invariant to scale. The casualty rate at resolution is set by the **casualty-% rout triggers** (~20–30%), not the damage scale. In decisive counters the asymmetry is correct: winner < loser (H3 19.7/29.9; H7 20.2/30.1; H10 21.7/30.5). Historical band (loser 15–30%, winner less): **satisfied without tuning.**

**Consequence:** `CASUALTY_SCALE` is a *pacing* knob, not a casualty knob. CS=20 (= the v9-validated effective lethality, BLOCK_SIZE/h_per_size = 100/5) gives clean **single ≈ multi** (battles resolve in ~1 engagement-turn) at correct casualty %. Adopted as the D-B default — but see the erosion defect: final pacing can't be cleanly set until that's fixed.

## Authoritative result (CS=20, n=60, full gauge)
```
single = 5/13   multi = 5/13   (identical)
melee in-band (5/11): H1, H5, H6, H9, H11
melee OUT (6/11): H2 (Arrowhead vs Line 47, want 50-65 — wedge too weak)
                  H3 (Horseshoe vs Line 67, want 50-65 — slightly strong)
                  H4 (Cannae 37, want 40-60 — just below; horseshoe ~ties wedge)
                  H7 (GappedLine vs Line 70, want 50-65 — too strong)
                  H8, H10
ranged OUT (R1/R3): volley scale not unified — M5/ED-822
```

## CORRECTION
The n=40 sweep suggested CS=20 → 8/11 melee. Authoritative n=60 → **5/11**. The 8/11 was sampling noise (~±8pp at n=40). Reported number is 5/11. `[CORRECTION: prior-turn "8/11 melee at CS=20" — n=40 noise; n=60 authoritative = 5/11]`

## New defect (→ M3)
`erosion = total_dmg / (discipline × command)` uses **raw soldier-scale** damage. Under TroopCount, raw damage is in soldiers (large), so morale erosion is mis-dimensioned — a 1000-soldier and 100-soldier unit taking equal *fractional* loss erode differently. This couples `CASUALTY_SCALE` to win-rates (the sweep's non-monotonic band-count: 5,6,5,3,2,5,8). **Fix:** erode on casualty *fraction* (size-loss units), making erosion scale-invariant so CASUALTY_SCALE purely controls pacing. Coupled to the counters → do it as the first step of M3.

## Confirms F5 / D-C (again)
D-B (TroopCount) melee = 5/11 = v9 engine melee = ratio-restore ~5. The bottom-up accounting does **not** move the counters. The 12/13 high-water was v14's counter tuning specifically. Steer for M3/D-C stands: pursue v14's counter geometry, not the v13+ cell-physics.

---

## Manifest delta
- **M1 — Gauge:** DONE.
- **M2 — D-B TroopCount model:** DONE (model + casualty calibration met emergently; CS=20 default). Caveat: pacing finalization depends on the erosion fix.
- **M3 — Formation counters:** now includes **(3a) fix morale-erosion dimensioning** (casualty-fraction), then **(3b) counter tuning** to bring H2/H3/H4/H7/H8/H10 in-band, per D-C leaning to v14 geometry; **(3c) reconstruct v14-compatible battery** as the counter reference. Validate on the gauge.
- **M4 — Multi-turn dynamics:** after M3 (and after erosion fix, pacing can be set).
- **M5 — ED-822 volley/composition:** ranged (R1/R3) volley-scale unification + composition.
- **M6 — Canon reconciliation:** ratify validated model + constants into §A.7/PP-233.

## Confidence & limits
- `[CONFIDENCE: high]` — casualty target met emergently (~25% loser, asymmetric) is direct measurement, stable across the scale sweep. D-B model edits verified by assertion.
- `[CONFIDENCE: high]` — 5/11 melee at CS=20 (n=60); the n=40 8/11 retracted as noise.
- `[CONFIDENCE: medium]` — erosion-dimensioning is the cause of the band-count scale-sensitivity (strong inference from the sweep + code reading; to be confirmed by implementing the fraction-based fix in M3).
- D-B engine (`sim_v22_db.py`) is local; main untouched (B6). Gauge unchanged (`gauge_mb.py`).
