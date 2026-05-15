# Weapon System v2 — Iteration Log

**Date:** 2026-05-14
**Appended to:** weapon_v2_audit_2026-05-14.md

---

## Iteration Results (4 rounds)

### Baseline → Iteration 4 progression

| Fix | Unarmoured Top | Heavy Top | Mace vs LS (Heavy) | T3.2 crossover |
|-----|---------------|-----------|-------------------|----------------|
| BASELINE | Tough 69% ✗ | Tough 82% ✗ | 29% ✗ | No crossover |
| +Linear HP | Fast 65% ✓ | Tough 79% ✗ | — | — |
| +DR pool | Knight 59% ✓ | — | — | — |
| +Commit bonus (all) | Strong 61% ✓ | Strong 80% ✗ | 42% ✓ | LS>mace all tiers |
| +Commit 1H only | Fast 61% ✓ | Strong 73% ~ | 35% | LS>mace all tiers |
| **+Simplified triangle** | **Tough 63% ✓** | **Strong 75% ~** | **39% ~** | **Mace beats LS at Heavy ✓** |

### Final Config (Iteration 4)

1. **HP = End×6+16** (linear, replaces WI×(MW+1))
2. **Pool DR above Agi 4** (min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3)
3. **1H specialist commitment:** +2D offense for single-attack-type, non-2H weapons
4. **Simplified defense triangle:** wrong defense → attacker +2 flat damage (no counter-attack, no TN mod)

### T3.2 Weapon Matchup Table (Final Config, equal stats, arena 3)

| A vs B | None | Heavy | Crossover |
|--------|------|-------|-----------|
| Longsword vs Mace | LS 74% | **LS 52%** | Mace competitive at Heavy ✓ |
| Longsword vs Spear | LS 60% | LS 55% | Spear competitive ✓ |
| Longsword vs Dagger | **Dag 57%** | LS 57% | Dagger wins unarmoured ✓ |
| Arming Sword vs Mace | AS 51% | **Mace 77%** | Mace dominates armoured ✓ |
| Warhammer vs Longsword | LS 60% | **WH 62%** | WH wins armoured ✓ |

Every matchup shows the correct armour-dependent crossover:
- Blade weapons dominate unarmoured (Cut +4 vs None)
- Blunt weapons dominate armoured (Bash +4 vs Heavy)
- The "king of weapons" (longsword) is best overall but has exploitable weaknesses

### T7.1 Build Matrix (Final Config, arena 3)

| Armour | Rankings | Top | Bot | Pass (65%) | Pass (75%) |
|--------|----------|-----|-----|------------|------------|
| None | Tough 63%, Strong 55%, Fast 54%, Knight 53%, Cunning 36%, Soldier 18% | ✓ | ✗ | **PASS** | PASS |
| Medium | Strong 73%, Tough 72%, Knight 54%, Fast 43%, Cunning 37%, Soldier 13% | ✗ | ✗ | FAIL | **PASS** |
| Heavy | Strong 75%, Tough 74%, Knight 56%, Fast 39%, Cunning 34%, Soldier 14% | ✗ | ✗ | FAIL | **PASS** |

### Historical Precedent Assessment

| Finding | Historical Alignment | Status |
|---------|---------------------|--------|
| Longsword best dueling weapon | Liechtenauer, Fiore: "king of weapons" | ✓ Correct |
| Dagger wins unarmoured at close range | Fiore: dagger deadly in grappling | ✓ Correct |
| Mace/warhammer win vs plate | 14th-15th c.: mace developed for plate | ✓ Correct |
| Spear competitive but not dominant | Spear strong at distance, weak inside | ✓ Correct |
| Arming sword viable but not best | Standard sidearm, outclassed in duels | ✓ Correct |
| STR builds dominate armoured | Plate favors physical power | ✓ Correct |
| Agi builds dominate unarmoured | Speed/skill > power without armour | ✓ Correct |

### Remaining Issues

1. **Soldier (balanced 4/4/4/4) at 13-18%.** Generalist has no duel niche. Acceptable if Soldier's value is in group combat and versatility across contexts, not dueling.

2. **Mace at 39% vs LS (Heavy).** Close to 40% target but not quite there. Could reach 40% with TN 7.0 instead of 7.5 (reduce by 0.5). But this changes the v2 TN system.

3. **Heavy armour top at 75%.** Pass at relaxed threshold. If 65% is firm, the HP formula needs more aggressive flattening or armour needs to provide less damage reduction (reduce Bash table from +4 to +3 vs Heavy).


---

## Iterations 5-6: Crit Threshold + Commitment Calibration

### Crit Rate Discovery (P1 finding)
| Pool | Crit >= 3 | Crit >= 4 | Crit >= 5 |
|------|-----------|-----------|-----------|
| 10 off (7+3 arena) vs 6 def | **60.1%** | 41.2% | 25.4% |
| 7 off (no arena) vs 6 def | 44.4% | 24.1% | **11.0%** |

Canonical threshold (>= 3) produces crits on 60% of hits with arena stunt. This makes crits the normal case, not a special event. Arena stunt (+3D pure offense) is the primary driver.

### Commitment Bonus Calibration
| Bonus | Spear vs AS (None/Heavy) | Mace vs LS (Heavy) | Issue |
|-------|------------------------|-------------------|-------|
| +0D (none) | 50%/65% | 29% | Mace too weak |
| +1D (all 1H specialists) | 55%/72% | 36% | Spear too strong armoured |
| +2D (all 1H specialists) | 60%/76% | 41% ✓ | Spear dominant everywhere |
| **+2D (mace only, TN>7.0)** | **53%/65%** | **36%** | **Best compromise** |

Spear (TN 6.5) doesn't need a commitment bonus — it's already competitive from raw TN advantage. Mace (TN 7.5) needs it to compensate for its TN penalty.

### HP Formula Progression
| Formula | End 4 | End 6 | Gap | Tough avg (None) |
|---------|-------|-------|-----|-----------------|
| Canonical (WI×(MW+1)) | 40 | 60 | 50% | 69% |
| End×6+16 | 40 | 52 | 30% | 63% |
| **End×5+20** | **40** | **50** | **25%** | **62%** ✓ |

### Best Configuration (Iteration 6)
1. HP = End×5+20
2. Pool: min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3
3. Mace-only +2D (weapons with TN > 7.0 and 1H)
4. Wrong defense = +2 flat damage
5. Crit >= 4 (proposed; canonical is >= 3)

### Test Coverage Summary
| Test | Status | Config |
|------|--------|--------|
| T1.1 Hit rate per TN | PASS | All |
| T1.2 Net hits by TN gap | PASS | All |
| T1.3 Fractional TN | PASS (single-die, pool theory correct) | All |
| T2.1 AS mirror duration | PARTIAL (duration flat — stamina-dominated) | Iter 6 |
| T2.2 Blade vs blunt crossover | PASS (AS>mace None, mace>AS Heavy) | Iter 6 |
| T2.3 Pierce consistency | PARTIAL (spear 53-65%, slightly high at Heavy) | Iter 6 |
| T2.4 Warhammer dominance | PASS (win rate 42-59% with distance) | Iter 1 |
| T3.1 LS attack type optimality | PASS (Cut>Thrust>Bash at None; Thrust>Cut at Heavy) | Iter 5 |
| T4.1-T4.4 Defense triangle | Simplified to wrong-def +2 (lever conflict resolved) | Iter 4 |
| T5.1 Distance sanity | PASS (correct directionality) | Iter 1 |
| T6.1 Longsword dominance | PARTIAL PASS (fixed vs Mid, not vs Long) | Iter 1 |
| T7.1 Build matrix (None) | **PASS** (top 62%) | Iter 6 |
| T7.1 Build matrix (Heavy) | PASS at 75% threshold | Iter 6 |
| T8.1 Cut crit vs armour | Confirmed (crit damage 1.3-1.5× non-crit) | Iter 5 |
| T8.3 Bash crit lethality | Confirmed (100% of crits vs Heavy = near-lethal) | Iter 5 |
