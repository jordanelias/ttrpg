# Handoff: Valoria Mass Battle Sim — End of v21 Session

**Date:** 2026-05-14
**Last commit:** (this commit)
**Status:** v21 stable. True simultaneous resolution implemented. BIAS-1 fixed.
**Next priority:** freed-attacker mechanic (priority 2 from v20 handoff)

---

## Bootstrap

Send `bootstrap simulation` then read in order:

1. `references/canonical_sources.yaml` — confirm canonical pointers
2. `designs/provincial/mass_battle_v30.md` — full design doc
3. `params/mass_combat.md` — extracted params (PP-NNN, ED-NNN)
4. `tests/sim/sim_mb_06_v21.py` — current sim
5. `tests/sim/audit_sim_mb_06_v16.md` — 10 gaps identified, priorities set
6. `tests/sim/sim_mb_06_v16_manifest.md` — manifest for last formal version
7. `tests/coverage_matrix.md` — recent sim history
8. This handoff: `tests/sim/HANDOFF_v21.md`

---

## What Changed (v20 → v21)

**True simultaneous resolution (BIAS-1 root fix):**

Three changes to `run_battle`:

1. **Target centroid caching** (PRIMARY FIX): All atom target centroids cached BEFORE any movement. Previously unit_a advanced toward unit_b's pre-move centroid, but unit_b advanced toward unit_a's POST-move centroid — ~10% first-arg bias. Now both sides see pre-move positions symmetrically.

2. **Simultaneous HP application**: Both units take damage, THEN both recalc_size. Previously unit_a HP reduced and recalc_size called before unit_b. [canonical: params/mass_combat.md PP-233 — "Damage is simultaneous. Both sides deal and receive damage before Size is recalculated."]

3. **Simultaneous morale erosion**: Erosion computed for both units, THEN rout checked for both. Previously sequential.

**Removed:** alternating processing order swap in `run_multi_turn_battle` — no longer needed.

---

## Validation Results (v21)

| Test | v20 (alternating swap) | v21 (simultaneous) | Status |
|---|---|---|---|
| Mirror Cmd 4v4 (n=40, max=20) | A 55% / B 40% / D 5% | A 50% / B 42.5% / D 7.5% | bias halved |
| Cmd 7v1 (n=30) | 100% A | 100% A, avg 2.0 turns | validated |
| Cmd 5v3 (n=30) | 100% A | 100% A, avg 5.3 turns | validated |
| Rout threshold (multi-turn) | ~14.7% | ~14.7% | consistent |
| Winner determined by dice | No (processing order) | Yes (seed 4001 flips winner) | validated |

**Residual mirror bias (7.5 pts):** Structural, not processing-order. Source: grid geometry asymmetry (SIDE_A_START_ROW=16 vs SIDE_B_START_ROW=8) and advance_dir (-1 vs +1) affecting pattern orientation.

**Rout threshold note:** v20 handoff cited 29.7-29.8% from single-engagement math. Multi-turn mode produces ~14.7% because between-turn stamina recovery extends battles while morale erosion accumulates across turns. Consistent between v20 and v21.

---

## What's Built (v21, inherited from v20)

Same as v20 handoff. All bottom-up emergent core intact. 8 imposed constants unchanged.

---

## What's Broken / Known Issues

| ID | Severity | Issue | Notes |
|---|---|---|---|
| BIAS-1 | ~~P2~~ RESOLVED | Processing order bias | Fixed in v21. Residual 7.5 pt structural bias from grid geometry. |
| D-4 | P2 | Pursuit damage = 0 for Standard infantry | Canonically correct (A.12). Cavalry (G-11) needed. |
| D-5 | P2 | Morale cascade prototyped but not committed | Real cascade = freed-attacker, not morale check. |
| D-2 | P2 | Shared grid, not per-unit | Sim uses one grid for both units. |
| D-3 | P2 | No multi-unit engagements | 2v1, 3v1, 2v2 not modeled. |
| D-8 | P3 | Battery bands not recalibrated for multi-turn | Single-turn bands stale. |
| D-10 | accepted | Pool insensitive to high casualties | By design — Command dominance axiom. |
| GEO-1 | P3 | Residual structural grid bias | SIDE_A/B_START_ROW asymmetry + advance_dir orientation. |

---

## Next Session — Priority Order

### 1. Freed-attacker mechanic

When one unit routs, the victor attacks adjacent enemies from the flank. The actual Cannae mechanism. Prerequisite: Multi-unit orchestrator (D-3).

### 2. Multi-unit engagement orchestrator (D-3, D-5)

Level-2 battle architecture. `run_multi_unit_battle(pairs)` with morale cascade and freed-attacker.

### 3. Cavalry (G-11)

Pursuit damage to close 1.4x to 2-5x winner/loser casualty ratio.

### 4. Battery band recalibration (D-8)

### 5. Grid geometry symmetry (GEO-1, optional)

---

## Throughline Status

- T1 Generalship: validated, structural
- T2 Cascading degradation: firing correctly
- T3 Combined arms: well-served
- T4 Simultaneous resolution: NOW VALIDATED (v21)
- T5 Systemic weight: level-2 architecture pending
- T6 Scale-invariant dice: validated

---

[ASSUMPTION: residual 7.5 pt mirror bias is structural (grid geometry) not processing-order — basis: bias persists regardless of argument order; v20 to v21 cut bias from 15 to 7.5 pts by eliminating centroid asymmetry]
[CONFIDENCE: high — T1 generalship dominance validated; simultaneous resolution eliminates processing-order artifacts; rout threshold consistent between versions]
