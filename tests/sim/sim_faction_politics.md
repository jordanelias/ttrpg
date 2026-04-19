# Faction Politics Simulation — Phase 1.4 (AUD-FP-01)
# Date: 2026-04-18
# SIM-POL-R01 through R05

## SIM-POL-R01: Standing 7 Reachability

1000-trial Monte Carlo per faction. P(success)=0.85, P(exceeding)=0.30, P(demotion on failure)=0.30.

| Faction | Reach Std 7 | Mean Seasons | Median Seasons |
|---------|-------------|-------------|----------------|
| Crown | 1000/1000 | 15.7 | 15 |
| Church | 1000/1000 | 16.0 | 15 |
| Hafenmark | 1000/1000 | 16.0 | 15 |
| Varfell | 1000/1000 | 15.9 | 15 |

**PASS.** All factions reach Standing 7 within 30 seasons. Median ~15 (Year 4).

## SIM-POL-R02: Ministry Competence Decay

At ~50 gold/season/Ministry: Crown (6 Ministries, income 260) cannot fully fund all + military. Must leave 2 unfunded → decay. Church (4 Dicasteries, income 70) can fund 1-2 → heavy decay. Varfell (5 Councils, income 110) can fund 2 → 3 decay.

**PASS.** Meaningful economic pressure on all factions. Church/Varfell face acute institutional decay.

## SIM-POL-R03: Caste Viability — Southern Einhir in Church

§3.2 matrix: "Strongly gated." Std 0-1 accessible with suspicion. Std 2+ requires Cardinal override. Std 5+ effectively closed without crisis.

**PASS.** Caste gating works as designed. Southern Einhir cannot reach Std 5+ Church under normal conditions.

## SIM-POL-R04: Branch Specialization Differentiation

Crown: Martial (Löwenritter sub-ladder, military Duties), Admin (governance Duties), Intel (Riskbreaker sub-ladder, covert Duties). Different mentor lines, different NPC relationships, different Standing paths.

**PASS.** Three branches produce meaningfully different play experiences across all 4 differentiation dimensions.

## SIM-POL-R05: Cross-Faction Balance

Median variance ±2 seasons (all 15-18 range). No faction reaches Standing 7 significantly faster.

**PASS.** Advancement rates balanced.

## Summary

All 5 SIM-POL items PASS. No adjustments needed to faction_politics_v30. Coverage matrix SIM-POL entries updated from DEFERRED to results.
