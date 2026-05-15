# Module Manifest — weapon_v2_distance_sim.py

## Scope: combat (core_engine + combat + derived_stats)
## Purpose: Re-run T2.4 (warhammer) and T6.1 (longsword) with distance mechanics active
## Extends: duel_stress_test.py v9 chassis

| Module | Dependencies | Canonical Source | Status |
|--------|-------------|-----------------|--------|
| roll_engine | none | params/core.md §dice engine | verified (v9 chassis) |
| pool_formula | roll_engine | params/combat.md §Pool Formula | verified (v9 chassis) |
| derived_stats | none | designs/scene/derived_stats_v30.md §4.1 | verified (v9 chassis) |
| flat_stamina | none | N/A — Architecture C duel-specific | verified (v9 chassis) |
| weapon_v2_defs | none | PROPOSED — handoff 2026-05-13 + params/combat.md §STR multiplier | pending |
| damage_v2 | weapon_v2_defs | PROPOSED — handoff Cut/Thrust/Bash tables | pending |
| crit_v2 | damage_v2 | PROPOSED — handoff crit effects | pending |
| distance_system | weapon_v2_defs | PROPOSED — handoff Short/Mid/Long + designs/scene/combat_v30.md §3 (Establish Distance) | pending |
| initiative | pool_formula | designs/scene/combat_v30.md §3 | verified (v9 chassis) |
| feint_pp294 | pool_formula | params/combat.md PP-294 | verified (v9 chassis) |
| taunt | pool_formula | N/A — Architecture C duel-specific | verified (v9 chassis) |
| protocol_distance | distance_system, damage_v2 | N/A — sim protocol | pending |

## Build order
1. weapon_v2_defs + damage_v2 + crit_v2 (weapon table rewrite)
2. distance_system (range tracking, TN adjustment, Establish Distance action)
3. protocol_distance (distance-aware ADAPTIVE protocol + smart attack type)
4. T2.4 battery (warhammer vs arming, 4 armour tiers, N=3000)
5. T6.1 battery (longsword vs all weapons, 4 armour tiers, N=3000)

## Verification plan
- After step 1: single-exchange damage sanity check (5 seeds)
- After step 2: verify range penalties apply correctly (manual trace, 3 seeds)
- After step 3: verify ED action fires at correct times (trace log)
- After step 4-5: compare to prior T2.4/T6.1 results without distance
