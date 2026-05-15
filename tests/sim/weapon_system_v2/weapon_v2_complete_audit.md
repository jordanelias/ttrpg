# Weapon System v2 — Complete Test Audit

**Sessions:** v22 + v23 (2026-05-14)
**Tests executed:** 26 across 9 phases
**Iterations:** 6 formula tuning rounds
**Config tested:** HP=End×5+20, Pool DR (Agi>4→+1D), Mace +2D, Wrong def +2, Crit≥4

---

## Phase Results Summary

| Phase | Tests | PASS | PARTIAL | FAIL | Notes |
|-------|-------|------|---------|------|-------|
| 1. Half-point TN | T1.1-T1.3 | 3 | 0 | 0 | Dice engine validated |
| 2. Weapon-armour | T2.1-T2.4 | 1 | 3 | 0 | Crossovers correct; duration flat |
| 3. Multi-attack | T3.1-T3.3 | 2 | 1 | 0 | Smart protocol validated |
| 4. Defense triangle | T4.1-T4.4 | 0 | 0 | 4 | Simplified to wrong-def +2 |
| 5. Distance | T5.1-T5.3 | 1 | 2 | 0 | Agi advantage 15-20pp (over spec) |
| 6. 2H / longsword | T6.1-T6.3 | 0 | 2 | 1 | Shield +2D insufficient |
| 7. Equal-budget | T7.1-T7.2 | 2 | 0 | 4 | Pass unarmoured arena 3+5 only |
| 8. Crits | T8.1-T8.3 | 2 | 0 | 1 | Crit rate P1 at canonical ≥3 |
| 9. Integration | T9.1 | 1 | 0 | 0 | v9 findings hold |
| **TOTAL** | **26** | **12** | **8** | **10** | |

---

## Phase 1: Half-Point TN ✓

| Test | Status | Finding |
|------|--------|---------|
| T1.1 Hit rate per TN | **PASS** | TN 5.0-8.0: 30-60% per die. Monotonic, ±0.2% of theoretical |
| T1.2 Net hits by gap | **PASS** | 1.0 gap → 59% hit-through. No matchup >80% |
| T1.3 Fractional TN | **PASS** | Single-die rate 50.2% at TN 6.5 (correct: ceil(6.5)=7, P(≥7)+0.5×P(=6)=0.45+0.05=0.50) |

**Decision gate: GO.** Half-point TN system works.

---

## Phase 2: Weapon-Armour Matchups

| Test | Status | Finding |
|------|--------|---------|
| T2.1 AS mirror duration | **PARTIAL** | Duration 3.8-4.0 rounds at all tiers (flat, not doubling). Stamina-dominated outcomes |
| T2.2 Blade vs blunt | **PASS** | AS>Mace at None (53%). Mace>AS at Medium (75%) and Heavy (77%). Crossover at Light ✓ |
| T2.3 Pierce consistency | **PARTIAL** | Spear 53-65% (exceeds 60% ceiling at Medium/Heavy due to TN 6.5 advantage) |
| T2.4 Warhammer dominance | **PARTIAL** | With distance: WH 42-59% (win rate PASS). DPH ratio 1.4-2.4× (exceeds 1.3× threshold) |

**Decision gate: GO with caveats.** Crossovers correct. Duration test reveals stamina dominance. Spear slightly overperforms at Heavy (TN 6.5 + Thrust +2 vs Heavy = strong generalist).

---

## Phase 3: Multi-Attack

| Test | Status | Finding |
|------|--------|---------|
| T3.1 LS attack type | **PASS** | Cut 12.2 DPE vs None > Thrust 9.9. Thrust 9.2 DPE vs Heavy > Cut 7.8. Mordhau 5.4-7.0 (never optimal) ✓ |
| T3.2 Specialist vs versatile | **PASS** | LS vs Mace: 74% None, 52% Heavy. Correct crossover. Spear vs LS: 40-45%. WH vs LS: 40% None, 62% Heavy ✓ |
| T3.3 Smart protocol | **PARTIAL** | Smart vs bash_only: +20-30pp ✓. Smart vs cut_only at None: smart LOSES (43%) — correct, Cut IS optimal at None. Smart advantage context-dependent, not universal |

---

## Phase 4: Defense Triangle ✗ → Simplified

| Test | Status | Finding |
|------|--------|---------|
| T4.1 Modifier swing | **FAIL** | ±0.5→10pp, ±1.0→20pp, ±2D→20pp. All below 25pp target |
| T4.2 Init + triangle | **FAIL** | +0.4pp to +6.3pp (target 8-15pp) |
| T4.3 Specialist penalty | **FAIL** | Mace 19-35% at all modifier levels (target 40-50%) |
| T4.4 Random vs optimal | **FAIL** | 7-8pp gap (target <5pp) |

**Resolution:** Lever conflict identified. Replaced with wrong-defense = +2 flat damage. No TN mod, no counter-attack. Specialists unaffected. Versatile weapons exploit ~33% of the time for +2 damage.

**Historical basis:** HEMA defense selection is tempo-based, not hit-rate-based. Simplified model aligns better.

---

## Phase 5: Distance

| Test | Status | Finding |
|------|--------|---------|
| T5.1 Positional game | **PASS** | Spear 72% from Long, dagger 83% from Short. Directionality correct |
| T5.2 Mid weapon | **PARTIAL** | AS at Mid: 49-61% vs dagger/spear. At specialist optimal: AS 16-28% (devastating). AS is viable at Mid, destroyed at specialist range — correct but harsh |
| T5.3 Distance + init | **PARTIAL** | Agi asymmetry: +15-20pp (exceeds 5-10pp target). Agi strongly controls distance. May over-value Agi for distance-dependent matchups |

**Structural finding:** Distance creates a real positional game. The 15-20pp Agi advantage for distance control is larger than spec but mechanically correct — faster fighters SHOULD control distance. The question is whether this over-values Agi relative to other stats.

---

## Phase 6: Two-Handed / Longsword

| Test | Status | Finding |
|------|--------|---------|
| T6.1 Longsword dominance | **PARTIAL** | LS 47-58% vs Mid weapons (PASS). LS 70-77% vs Long weapons at same reach (FAIL — needs separate lever) |
| T6.2 2H vs 1H+shield | **FAIL** | LS 60-69% vs AS+shield(+2D). Shield +2D insufficient to match TN 6.5 advantage. Shield needs +3D or +4D |
| T6.3 2H cap | **PARTIAL** | LS at TN 6.5 (capped) is 70-80% vs AS. Cap is necessary but LS still dominant |

**Historical note:** Shield fighting (sword+buckler, sword+kite) was historically the dominant medieval combat system for professionals. LS dueling was an elite practice. Shield undervaluation is a design concern — shields should provide 50-55% vs 2H weapons per spec.

**Recommendation:** Shield bonus +3D or +4D defense. This is a params-level change.

---

## Phase 7: Equal-Budget

### Full 6-Condition Matrix

| Condition | Top Build | Top% | Pass 65%? | Bot Build | Bot% |
|-----------|-----------|------|-----------|-----------|------|
| Arena 0, None | Tough | 82.4% | ✗ | Soldier | 19.9% |
| Arena 0, Heavy | Tough | 85.6% | ✗ | Soldier | 16.8% |
| **Arena 3, None** | **Tough** | **62.0%** | **✓** | **Soldier** | **18.2%** |
| Arena 3, Heavy | Strong | 75.7% | ✗ | Soldier | 14.2% |
| **Arena 5, None** | **Strong** | **59.9%** | **✓** | **Soldier** | **16.2%** |
| Arena 5, Heavy | Strong | 79.5% | ✗ | Soldier | 12.5% |

**Pattern:** Only unarmoured conditions at arena 3+ pass. All Heavy conditions fail. Arena 0 fails (no stunt dice → pure attrition → Tough always wins).

**Root causes of Heavy failure:**
- Blade weapons deal 0-1 damage per hit vs plate (Cut +0, Thrust +2)
- With HP ~40, blunt needs ~3 hits to kill. Blade needs ~8-10 hits
- STR×3 + Bash +4 = 16 base damage. STR×1 + Cut +0 = 5 base damage. 3.2× ratio
- This gap is historically accurate (cutting weapons ARE useless vs plate) but produces >75% win rates for blunt

**Root cause of Arena 0 failure:**
- Without arena stunt (+0D offense), attacks are weak (7D vs 6D, both at TN 7)
- Fights become stamina attrition. Highest End wins by outlasting
- This is a duel system issue, not a weapon system issue — arena stunt is load-bearing for the duel model

### T7.2 Protocol Swing

| Matchup | Swing |
|---------|-------|
| ADAPTIVE vs AGGRESSIVE (AS mirror) | 7pp |
| ADAPTIVE vs AGGRESSIVE (Fast) | 12pp |

**PARTIAL PASS.** Below 15pp target. Simplified protocol model (offense split only) underestimates full v9 swing (feints, taunts, reactive declarations).

---

## Phase 8: Crits

| Test | Status | Finding |
|------|--------|---------|
| T8.1 Cut crit vs armour | **PASS** | Crit DPH 1.3-1.5× non-crit. Crits devastating unarmoured, modest vs Heavy ✓ |
| T8.3 Bash crit lethality | **PASS** | 100% of Bash crits vs Heavy ≥ half HP. Bash crit is the knockout blow ✓ |
| T8.x Crit rate | **P1 FINDING** | Canonical ≥3: 60% crit rate with arena. Crits are the norm, not special events |

---

## Phase 9: Integration

| Test | Status | Finding |
|------|--------|---------|
| T9.1 v9 findings hold | **PASS** | Arena shifts hierarchy (Fast 57%→33% vs Strong). E7 yield works (2.5% draws). Protocol matters (7pp, simplified) |

---

## Cross-Directional Analysis

### Top-Down: Historical Alignment

| Finding | Historical | Aligned? |
|---------|-----------|----------|
| Longsword best dueling weapon | Liechtenauer, Fiore | ✓ |
| Dagger deadly unarmoured, useless vs plate | Fiore dagger plays | ✓ |
| Mace/hammer beats plate | 14th-15th c. anti-armour evolution | ✓ |
| Spear range-dependent | Spear dominates distance, fails close | ✓ |
| Shield provides meaningful tradeoff | Shield fighting = dominant medieval system | **✗** (shield too weak) |
| Arming sword as viable generalist | Standard military sidearm | **✗** (Soldier trap) |
| STR matters vs armour | Plate favors physical power | ✓ |
| Cut useless vs plate | Cutting weapons bounce off plate | ✓ (too extreme) |

### Bottom-Up: Formula Interactions

| Formula | Effect | Interacts with |
|---------|--------|---------------|
| HP = End×5+20 | Reduces End dominance from 50% gap → 25% gap | Wound interval (still canonical WI=End+6) |
| Pool DR (Agi>4→+1D) | Fast pool 17→15 | Distance control (Agi rolls at TN 7) |
| Mace +2D | Compensates TN 7.5 penalty | Specialist identity vs triangle |
| Wrong def +2 | Rewards versatile weapons ~33% of hits | Initiative (init holder picks counter) |
| Crit ≥4 | Rate drops from 60%→24% (no arena) | Arena stunt (drives crit frequency) |

### Lateral: System Interactions

| System A | System B | Interaction | Status |
|----------|----------|-------------|--------|
| Weapon damage | Armour tiers | Blade-blunt crossover | ✓ Correct |
| Distance | Weapon reach | Range-dependent dominance | ✓ Correct |
| Distance | Agi stat | Distance control | ✓ But over-values Agi (15-20pp) |
| Crit rate | Arena stunt | Arena inflates crits | ✗ P1 finding |
| Protocol | Weapon type | Smart protocol + versatile weapon | ✓ Correct interaction |
| Shield defense | 2H TN bonus | Shield undervalued | ✗ Shield needs +3-4D |
| End stat | HP formula | Durability scaling | ✓ Fixed by linearization |
| Stamina | Arena | Arena 0 = pure attrition | ✗ Arena is load-bearing |

---

## Open Decision Register

| # | Decision | Options | Recommendation | Impact |
|---|----------|---------|----------------|--------|
| D1 | HP formula | Canonical WI×(MW+1) vs End×5+20 | End×5+20 | Fixes End dominance at all tiers |
| D2 | Pool formula | Linear vs DR above Agi 4 | DR above 4 | Prevents Fast dominance unarmoured |
| D3 | Crit threshold | ≥3 (canonical) vs ≥4 vs ≥5 | ≥4 | 24% rate without arena, 41% with |
| D4 | Mace commitment | None vs +2D (TN>7.0, 1H) | +2D | Mace viable at Heavy (39-42%) |
| D5 | Defense triangle | TN mod vs counter vs wrong-def +2 | Wrong-def +2 | Simplest, no specialist penalty |
| D6 | Shield defense bonus | +2D vs +3D vs +4D | +3D (test needed) | Fix T6.2 shield undervaluation |
| D7 | Soldier viability | Accept vs stat-floor bonus | Accept for duels | Generalist value is in group combat |
| D8 | Heavy armour dominance cap | Accept vs reduce Bash table | Accept (historically correct) | 75% threshold |
| D9 | Arena 0 viability | Accept vs base stunt dice | Accept (arena 0 = exhibition, not duel) | Arena 0 is special case |
| D10 | Arming sword TN | 7.0 (current) vs 6.5 | 7.0 (correct for Normal weight) | Changing breaks TN derivation |
| D11 | Distance Agi advantage | 15-20pp (current) vs reduce | Accept (Agi SHOULD control distance) | Correct but large |
| D12 | Spear vs Heavy | 65% (current) vs cap at 60% | Monitor (borderline) | May need Thrust+2→+1 vs Heavy |

---

## Files Committed This Session

| Commit | Files | Content |
|--------|-------|---------|
| a31c528 | sim, audit, ledger | Initial distance sim + defense triangle + equal-budget |
| 329cc2a | iteration log, coverage | Iterations 1-4 |
| 4fd8a42 | iteration log, coverage | Iterations 5-6, crit finding |
| (pending) | This audit, full results | Complete 26-test coverage |
