# Per-Cell Integration Plan / Handoff — sim_mb_sigma
Date 2026-05-31 | Engine: tests/sim/sim_mb_sigma.py (ratified, 0dea67d1)
Prototype: per_cell_combat.py (75908b9e) | Diagnostic: ners_verdict_percell_resolution.md (0ec96591)
[SELF-AUTHORED — bias risk; treat as external on re-test.]

## ROOT CAUSE OF H7 (confirmed in code, not memory)
find_contacts (L1191) pairs every A-cell within Chebyshev-1 of every B-cell. A 9-wide GappedLine
presents MORE cells across the contact front than a 5-wide Line, so it produces more contact
cell-pairs -> _per_cell_angle_mod (L1316) averages more favorable flanking angles AND a wider front
is fed -> but resolution is still ONE pooled exchange off unit.base_combat_pool() (L1288), split by
troop_frac x support_engage_frac. Depth (Line's 5 ranks) only earns a fractional support credit
(support_engage_frac, L578) that cannot offset the width advantage.
=> H7 driver is FRONTAGE WIDTH, not the gap per se. This is exactly the frontage>depth imbalance
   the per-cell prototype fixes (depth = reserves: refill + rotation + flank-refusal; thin = fragile).

## RESOLUTION ARCHITECTURE (settled by the NERS diagnostic)
Do NOT roll per native cell (~16 troops -> 4D, CV~1.0, density lever dead). Instead:
  (1) aggregate native cells into coarse blocks of ~size-1 (>=100 troops): pool 5-8D, density lever live;
  (2) resolve each block-pair via the continuous sigma path (_sigma_net_boost mu-shift), stable at small N;
  (3) facing / charge / fatigue / envelopment ALL enter as delta-sigma (uniform impact), as the engine's
      sigma-head (L1357) and the prototype already do.

## SEAM (precise)
- REUSE unchanged: find_contacts (L1191), octagon_angle (L526)/_per_cell_angle_mod (L1316),
  _momentum_speed (L1219), cells()/oriented_pattern (L507) — all geometry/contact/facing.
- REPLACE only the per-pair resolution arithmetic, L1286-1391, when PER_CELL on:
  instead of a_base*troop_frac*engage_frac (one unit pool), resolve each contacted COARSE BLOCK on its
  own block pool = min(block_size, command)+command, via the sigma path; sum casualties across blocks.
- State today is unit-level only (hp/effective_size/stamina on Unit, L991). cells() is geometry-only,
  NO per-cell state. Per-block state is the new addition.

## INCREMENTS (each behind PER_CELL env toggle; OFF = committed engine EXACTLY; verify parse + toggle-off-reproduce each step)
1. BLOCK STATE: Unit gains a block grid (front-file columns x depth ranks of ~size-1 blocks, density+stamina),
   built in __post_init__ from the formation footprint (frontage = distinct contact columns, depth = ranks).
   Toggle-off: grid unused, unit untouched. Verify 200/200 identical to 0dea67d1 with PER_CELL=0.
2. PER-BLOCK RESOLUTION: in resolve_engagements under PER_CELL, map each contact column to its front block
   each side; resolve block-vs-block via the sigma path (block pool, density-scaled); casualties come off
   the contacted block, then off the unit hp in aggregate (keep unit hp/rout spine intact).
3. DEPTH RESERVES: port refill + fatigue rotation (prototype _refill/_rotate/_rest) onto the block grid;
   stamina drains the engaged front block, rear blocks rest; rotation swaps a fresh rear block forward.
4. FATIGUE delta-sigma: stamina_sigma(front block) into ns per block (thin line can't rotate -> exhausts).
5. CHARGE: charge_pen on Subunit/Unit (cavalry/wedge); depth-absorbed charge delta-sigma (prototype rule).
6. ENVELOPMENT + FLANK-REFUSAL: overhang columns (wider side) engage the narrow side's flank blocks;
   deep side reforms reserve ranks to refuse (prototype ENVELOP_SIGMA / FRONT_RANKS_NEEDED).
7. VALIDATE on gauge_mb_ci.py, H7 FIRST (target: GappedLine 9x3 vs Line 5x5 -> deep is competitive, not 81%),
   then full H1-H11 multi-turn at CSCALE 4. Re-run the NERS diagnostic (Stage 4) on the integrated path.

## TUNABLES TO PORT (all Class-B, validated in prototype 75908b9e; logged, Jordan-vetoable)
STAMINA_DRAIN_PER_CLASH 12, STAMINA_REST_PER_TICK 5, ROTATE_STAMINA_FLOOR 50, STAM_SIGMA_SCALE 1.5,
REFILL_FLOOR_FRAC 0.60, FLANK_DEPTH_RESIST 0.6, FRONT_RANKS_NEEDED 2, ENVELOP_SIGMA 0.5,
CHARGE_SIGMA 0.55, CHARGE_IMPACT_TICKS 3. (Block granularity: ~size-1 = 100 troops/block.)

## CONSTRAINTS
- PER_CELL toggle mandatory; OFF must reproduce 0dea67d1 (the committed canon engine) exactly.
- Resolve at coarse-block granularity via sigma path ONLY (NERS: no bare small-pool dice).
- Keep the unit-level morale/rout spine; per-block density feeds it, does not replace it.
- Commit scope [simulation] for engine edits (co-update coverage_matrix + verification ledger), or
  [cleanup] for audit-dir docs. task_gate('infrastructure') (canon set aside per Jordan).
