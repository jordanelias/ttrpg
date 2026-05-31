# NERS Verdict — Per-Cell Combat Resolution (proposed engine integration)
Date: 2026-05-31 | Engine: sim_mb_sigma (ratified, commit 0dea67d1) | Prototype: per_cell_combat.py (75908b9e)
Method: valoria-resolution-diagnostic, applied against engine CODE (canon docs set aside per Jordan 2026-05-31),
top-down-anchored to real warfare + the project NERS framework. [SELF-AUTHORED — bias risk: I designed the
prototype; surfacing the criticism an independent reviewer would raise.]

## Grounding (bottom-up, engine numbers)
- T3 native granularity: ~16 troops/cell (Line 25 cells, GappedLine 24), cell size ≈ 0.16.
- Per-cell pool = min(cell_size, command) + command. At size 0.16, cmd 4 → 4.16D for EVERY cell.
  Density lever DEAD: the size term is negligible vs command, so dense and sparse cells roll identically.
- Variance (engine roll_pool): CV ≈ 1.00 at 4D, 0.90 at 5D, 0.71 at 8D, 0.40 at 25D.
  4D is the high-variance small-pool regime the engine does its worst work in (1/√N).

## Diagnostic (Stage 1)
- Phase 0: dice (per-cell pool) + deterministic (density/reserve bookkeeping) + clock (morale→rout). Density = continuous resource.
- Phase 1: stress point = single T3 cell = 4D, routine exposure (every cell, every tick). Density lever dead at this granularity.
- Phase 2: graded-magnitude casualties; swings violently at 4D.
- Phase 3a: non-uniform δσ impact across cell pool sizes (1/√N). 3b/3c: n/a-new.
- Phase 4: morale→effectiveness loop already damped+bounded (morale fix); no new unbounded loop.
- Phase 5: per-cell discrete dice = [INTENT UNDETERMINED] → true finding (implementation default, no safeguard).

## Lessons (Stage 2)
- Lesson 3 (master) VIOLATED: bare 4D pool, load-bearing, routine. → don't roll it: aggregate or go continuous.
- Lesson 2 VIOLATED: non-uniform δσ impact. → express advantages as σ-leverage δσ (uniform via probit axis).
- Lesson 4 partial: morale clock absorbs some; per-cell casualty resolution not clocked.

## Verdict (Stage 3)
VERDICT: non-compliant AS discrete per-cell dice at native (16-troop) granularity.
  N pass — per-cell density/depth is necessary (validated: makes frontage/depth/charge meaningful).
  R FAIL — 4D bare pool, CV~1.0, routine: fragile high-variance magnitude on load-bearing roll [L3].
  S FAIL — density lever dead at native granularity; resolver inconsistent with σ-leverage core [L2/L3].
  E pass — per-cell concept is intuitable; defect is in the resolver, not the concept.

REMEDIATION (worst-first):
  HIGH  small-pool fragility + dead density lever → L3: resolve each block via CONTINUOUS σ-leverage
        (μ-shift, stable at small N) and/or AGGREGATE native cells to ~size-1 blocks (≥~100 troops):
        pool 5→8D, CV 0.9→0.7, density lever restored.
  MED   non-uniform δσ impact → L2: facing/charge/fatigue/envelopment as σ-leverage δσ (engine idiom).

## Re-test (Stage 4)
The validated prototype ALREADY used coarse blocks (rank_density 100 → size 1.0 → 5–8D), which is why its
density lever worked and results were stable. The failure mode appears ONLY if ported at native 16-troop
granularity. Remediation validated by construction; no new defect. [OPEN TRADE-OFF: none — fixes compose.]

## Integration architecture (settled)
1. Aggregate native ~16-troop cells into coarse ~size-1 blocks (≥100 troops) for resolution.
2. Resolve each block via the continuous σ-leverage path (μ-shift) — stable at small N, unifies with core.
3. Facing / charge / fatigue / envelopment enter as δσ (uniform impact), as prototype + σ-head already do.
