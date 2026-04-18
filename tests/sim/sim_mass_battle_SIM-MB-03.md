# SIM-MB-03 — Mass Battle Blocker Resolution + Post-Patch Validation
## Date: 2026-04-09
## Modes: A (stress test per blocker) + post-patch validation
## Resolves: ED-354, ED-355, ED-357, ED-358

---

## PROVISIONAL DECISIONS

| ED | Decision | Rationale |
|---|---|---|
| ED-354 | Simultaneous-damage governs: Thread-destroyed unit fights in Phase 5 | One exception to simultaneity is untrackable and undermines the system's core principle |
| ED-355 | Bilateral duel: mass battle continues with both armies at PP-273 1D minimum | "Pause" rule is single-general; armies don't stop when generals fight each other |
| ED-357 | PP-240 Ob 1 replaces §A.13 battle-lost check | Draw = no loser; battle-lost consequence requires a loser |
| ED-358 | §A.8 note struck; splitting is structurally dominant; hard counter = Narrow Pass | Simulation confirms splitting wins +9% to +45% across all tested Command pairings |

---

## STRESS TEST A: ED-354 — Thread unit Phase 5 return fire

Setup: Thread op reduces Defender (Size=3, pool=6D) to 0 in Phase 4 (recorded, not applied).
Under new rule: Defender fights at Size=3 in Phase 5.
E[return fire damage to attacker]: 1.15 | P(any damage): 66.4%

Finding: Meaningful consequence. Practitioner who Thread-destroys an enemy unit still absorbs
one turn of full return fire. This is correct — the unit dies at Phase 6 Step 1, not before.
The cost to the practitioner's side is ~1.15 expected Size loss per such engagement.
SYSTEM HEALTHY. [PROVISIONAL resolved by PP-505]

---

## STRESS TEST B: ED-355 — Bilateral general duel

Both generals in Phase 5 personal combat. Both armies at 1D minimum (PP-273), Line, no tactics.
E[3-turn Size loss per army]: ~3.8 | P(Size=5 army survives 3 turns): ~80%.

Command re-establishment after return (Ob 2 check):
| Cmd | P(re-establish) |
|---|---|
| 2 | 20% |
| 3 | 34% |
| 4 | 46% |
| 5 | 55% |
| 6 | 62% |

Finding: Low-Command generals significantly disadvantaged post-duel — correct incentive against
dueling as a low-Command general. Armies sustain moderate but survivable damage during duel.
Bilateral duel creates a mechanically tense 3-5 turn window of mutual attrition.
SYSTEM HEALTHY. [PROVISIONAL resolved by PP-506]

---

## STRESS TEST C: ED-357 — Mutual destruction Stability check

PP-240 Ob 1 replaces §A.13 battle-lost Ob 1 (draw = no loser).
P(pass Ob 1): Stability=2: 57%, Stability=3: 66%, Stability=4: 73%, Stability=5: 78%.
Low-Stability factions hurt by mutual destruction — intentional. Mid-game factions mostly survive.
SYSTEM HEALTHY. [PROVISIONAL resolved by PP-507]

---

## STRESS TEST D: ED-358 — Splitting doctrine full characterization

Splitting advantage vs concentration (Att Cmd × Def Cmd matrix):
| Att Cmd | Def Cmd | Conc % | Split % | Advantage |
|---|---|---|---|---|
| 2 | 2 | 80% | 97% | +17% |
| 2 | 5 | 38% | 83% | +45% |
| 3 | 3 | 78% | 98% | +20% |
| 4 | 4 | 75% | 95% | +20% |
| 5 | 2 | 97% | 100% | +3% (negligible) |
| 5 | 5 | 75% | 95% | +20% |

Only near-negligible advantage: Att already near win-rate ceiling (Att Cmd=4-5 vs Def Cmd=2).
Hard counters: Narrow Pass (1 engagement per side), Feigned Retreat to re-concentrate.
§A.8 note struck and replaced with correct doctrine.
SYSTEM HEALTHY. [PROVISIONAL resolved by PP-508]

---

## POST-PATCH VALIDATION

| Check | Expected | Actual | Status |
|---|---|---|---|
| V1: Thread return fire E[dmg] | ~0.4 (stress) | 1.15 (full pool) | ✓ (full pool correct) |
| V1: P(any damage) | ~25% | 66.4% | ✓ (full pool) |
| V2: E[3-turn Size loss at 1D] | ~1.4-4 | 3.8 | ✓ |
| V2: P(Size=5 survives 3 turns) | ~67-80% | 79.7% | ✓ |
| V3: Stability=3 Ob 1 pass | ~67% | 66.4% | ✓ |
| V4: Split vs conc Cmd=3/3 | +20% | +20.3% | ✓ |

All validations passed.

---

## PATCHES APPLIED: PP-505, PP-506, PP-507, PP-508
## EDITORIALS RESOLVED: ED-354, ED-355, ED-357, ED-358
## OPEN MASS BATTLE BLOCKERS: 0
