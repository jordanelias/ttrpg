---
session_id: v21-sim-simultaneous
last_stage: sim_v22_cavalry_pursuit_g11
last_commit: (this commit)
commits: 4
next_action:
  skill: valoria-simulator
  description: Priority 5 — battery band recalibration (D-8). Or comprehensive handoff.
blockers:
  - canonical_sources.yaml freshness stale for params/combat.md (PP-238 editorial)
---

# Session Log — v21 Simultaneous Resolution

## What was done

### Priority 1: True simultaneous resolution (BIAS-1 root fix)

Committed as 805f5f2 in tests/sim/sim_mb_06_v21.py.

Three targeted changes to run_battle:

1. **Target centroid caching** (PRIMARY): all atom target centroids cached before movement. Previously unit_a advanced toward unit_b's pre-move centroid, unit_b toward unit_a's post-move centroid. Created ~10-15% first-arg bias. Now both see pre-move positions.

2. **Simultaneous HP**: both units take damage, then both recalc_size. [canonical: PP-233 "Damage is simultaneous"]

3. **Simultaneous morale**: erosion computed for both, then rout checked for both.

Removed alternating swap band-aid from run_multi_turn_battle.

### Validation

- Mirror Cmd 4v4 (n=40, max_turns=20): A 50.0% / B 42.5% / D 7.5% — p=0.62, consistent with true 50/50
- Cmd 7v1 (n=30): 100% A, avg 2.0 turns — T1 validated
- Cmd 5v3 (n=30): 100% A, avg 5.3 turns — T1 validated
- Rout threshold: ~14.7% in multi-turn, consistent with v20
- Winner by dice: seed 4001 flips winner — processing-order bias eliminated

### Post-commit: GEO-1 closed

The 50/42.5 split was initially attributed to grid geometry (GEO-1). Investigation proved:
- Grid positions symmetric about row 12 (both fronts 4 rows from center)
- Cell speeds identical for both formations
- Formation depths identical (5x7=35 cells)
- Statistical test: z=0.49, p=0.62 — pure noise at n=40
GEO-1 closed. HANDOFF corrected.

## What was NOT done

Priorities 2-5 from v20 handoff. Context at 50-75% after gate overhead.

## Next session priorities (in order)

1. Freed-attacker mechanic — requires multi-unit orchestrator
2. Multi-unit engagement orchestrator (D-3, D-5) — run_multi_unit_battle(pairs)
3. Cavalry / G-11 — pursuit damage
4. Battery band recalibration (D-8)
