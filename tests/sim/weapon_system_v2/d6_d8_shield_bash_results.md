# D6 + D8 Test Results — Shield & Bash Table

**Date:** 2026-05-15 (session v24)
**Prior sessions:** v22 (distance+triangle), v23 (26-test audit)

---

## D6: Shield Defense Bonus

### 2H vs 1H+Shield Parity (LS vs AS+shield, equal stats, arena 3)

| Shield | None | Medium | Heavy | Parity? |
|--------|------|--------|-------|---------|
| +0D | LS 72% | LS 80% | LS 81% | No |
| +2D | LS 63% | LS 69% | LS 70% | No |
| +3D | LS 59% | LS 64% | LS 65% | No |
| **+4D** | **LS 51%** | LS 59% | LS 60% | **Unarmoured only** |
| +5D | LS 47% | LS 54% | LS 55% | ✓ at all tiers |

+4D achieves parity unarmoured. +5D is needed at armoured tiers. But shield bonus in the full build matrix creates a new problem:

### Shield in Full Build Matrix (all 1H builds get shield)

| Mode | None Top | Heavy Top |
|------|----------|-----------|
| No shield | Tough 62% ✓ | Strong 75% ~ |
| Shield +3D def | Tough 79% ✗ | Tough 83% ✗ |

**Shield amplifies Tough.** Adding +3D defense to all 1H users disproportionately benefits the highest-HP build. Tough's game plan is outlast the opponent, and more defense dice directly supports that. Shield makes duels longer, and Tough wins longer duels.

### T6.2: 2H vs 1H+Shield Weapon Matrix (shield +3D)

| Matchup | None | Heavy |
|---------|------|-------|
| LS vs AS+shield | LS 59% | LS 65% |
| LS vs Dagger+shield | **Dag 74%** | Dag 67% |
| WH vs AS+shield | WH 51% | **WH 72%** |
| WH vs Mace+shield | WH 56% | WH 52% |

Shield works weapon-to-weapon (correct tradeoffs). But universal shield in the build matrix creates Tough dominance.

### D6 Resolution

Shield is a **weapon/loadout decision**, not a universal bonus. It should be:
- A distinct weapon slot choice (sword+shield vs longsword)
- With specific TN/damage penalties for the weapon when paired with shield
- Not modeled as simple +ND defense to all 1H weapons

This means shield is a **design-layer** decision (loadout system), not a simple params change. Deferred to design phase.

---

## D8: Bash Table Reduction

Canonical Bash: +2/+3/+4/+4. Proposed: +2/+3/+4/+3 (reduce Heavy by 1).

| Table | Heavy Top | Heavy 2nd | Spread |
|-------|-----------|-----------|--------|
| Canonical (+4) | Strong 75% | Tough 74% | 61pp |
| Reduced (+3) | Tough 76% | Strong 74% | 61pp |

**Barely changes anything.** The Bash modifier is a small term in the damage formula. Strong's advantage comes from STR×3 (= 18 base damage at STR 6), not from the +4 table entry. Reducing +4 → +3 removes 1 point from ~16 total damage per hit.

### Root Cause: The Damage Gap at Heavy

| Weapon | Damage per hit vs Heavy (STR 4) |
|--------|---------------------------------|
| Arming sword (Cut) | net + 4×1 + 0 = net + 4 |
| Spear (Thrust) | net + 4×1 + 2 = net + 6 |
| Mace (Bash) | net + 4×1.5 + 4 = net + 10 |
| Longsword (Cut) | net + 4×2 + 0 = net + 8 |
| Longsword (Thrust) | net + 4×2 + 2 = net + 10 |
| Warhammer (Bash) | net + 4×3 + 4 = net + 16 |

With HP ~40, the warhammer needs 2-3 hits to kill. The arming sword needs 8-10.

**This gap is historically correct.** Cutting weapons ARE useless against plate armour. The question is whether the game should model this accurately or compress for playability.

### D8 Resolution

**Accept the gap at Heavy armour.** The 75% threshold holds. Heavy armour genuinely hard-counters blade weapons — this is correct historical behavior and creates meaningful equipment choice. Players fighting armoured opponents should use blunt weapons or target weak points (Thrust).

The Soldier problem (14% at Heavy) is an artifact of the Soldier using a blade weapon (arming sword) against plate. A Soldier who picks up a mace or warhammer would perform much better. The sim tests fixed weapon assignments — real gameplay allows weapon switching.

---

## Updated Decision Register

| # | Decision | Status | Resolution |
|---|----------|--------|------------|
| D1 | HP = End×5+20 | **TESTED ✓** | Fixes End dominance |
| D2 | Pool DR (Agi>4→+1D) | **TESTED ✓** | Fixes Fast dominance |
| D3 | Crit ≥ 4 | **TESTED ✓** | Rate 24% (no arena), 41% (arena) |
| D4 | Mace +2D (TN>7.0, 1H) | **TESTED ✓** | Mace competitive at Heavy |
| D5 | Wrong-def +2 damage | **TESTED ✓** | Simplified triangle |
| D6 | Shield defense | **DEFERRED** | Needs loadout system design, not simple +ND |
| D7 | Soldier viability | **ACCEPT** | Generalist weak in duels by design |
| D8 | Bash table reduction | **REJECT** | Barely changes results, gap is STR×3 not table |
| D9 | Arena 0 viability | **ACCEPT** | Arena 0 = exhibition, not competitive duel |
| D10 | Arming sword TN | **ACCEPT 7.0** | Correct for Normal weight derivation |
| D11 | Distance Agi advantage | **ACCEPT** | 15-20pp is mechanically correct |
| D12 | Spear vs Heavy | **MONITOR** | 65% borderline, may need Thrust+2→+1 |

### Ratifiable Package (D1-D5)

These five changes form a coherent, tested package:

```
HP = End × 5 + 20
Pool = min(Agi, 4) × 2 + max(0, Agi - 4) × 1 + Hist + 3
Mace commitment: +2D offense if weapon TN > 7.0 and 1H
Defense triangle: wrong defense type → attacker +2 flat damage
Crit threshold: net hits ≥ 4 (from ≥ 3)
```

**Combined effect:** Unarmoured build matrix PASSES at 62% top (under 65% threshold). Heavy passes at 75% (relaxed threshold). Weapon-armour crossovers correct. Historical alignment validated across 5 weapon types and 4 armour tiers.
