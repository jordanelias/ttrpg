# T2.4 + T6.1 Re-run WITH Distance Mechanics

**Date:** 2026-05-14
**Sim:** `weapon_v2_distance_sim.py`
**Chassis:** v9 duel sim + weapon v2 (half-point TN, Cut/Thrust/Bash, STR mult) + Short/Mid/Long distance
**N:** 3000 per matchup. Equal stats (Agi 4, STR 4, End 4, COG 4, Hist 2). Arena 3. Start range: Mid.
**Protocol:** DISTANCE_ADAPTIVE (extends ADAPTIVE with Establish Distance decisions)

---

## Distance system implemented

- Short/Mid/Long range per engagement
- Optimal range = weapon's Reach axis (no penalty)
- Adjacent range = +1.0 TN on attack
- Opposite range = BLOCKED (can't attack)
- Establish Distance: Agi contest (both roll Agi at TN 7), winner moves range 1 step toward preferred. Cost: 5 stamina. Replaces attack for that round.
- Starting range: Mid (neutral)

## T2.4: Warhammer vs Arming Sword — **STILL FAILS**

| Armour | Warhammer | Arming | Draw | Avg Rds | ED att/suc | Prior (no dist) |
|--------|-----------|--------|------|---------|------------|-----------------|
| None   | 61.5%     | 37.0%  | 1.4% | 5.4     | 4.0/1.5    | 66-85% (dom)    |
| Light  | 68.0%     | 30.8%  | 1.2% | 5.5     | 4.1/1.6    | —               |
| Medium | 73.5%     | 25.4%  | 1.1% | 5.5     | 4.1/1.6    | —               |
| Heavy  | 74.7%     | 24.2%  | 1.1% | 5.5     | 4.1/1.6    | —               |

**Pass criteria:** Warhammer DPS ≤ 1.3× arming at any tier.
**Result:** FAIL at all tiers. Distance reduces WH dominance from 66-85% to 59-74% but STR×3 (= 12 flat at STR 4) overwhelms TN parity at Mid.

**Root cause:** At equal Agi, ED contests are coin flips. Warhammer gets to Long ~40% of fights. When it does, it hits at TN 7.0 vs arming's TN 8.0, and each hit deals net + 12 + Bash mod. The raw damage per connection is too high for TN penalty to compensate.

## T6.1: Longsword vs ALL Weapons — **PARTIALLY IMPROVED**

### None armour

| Opponent   | Reach | LS win | Opp win | Draw | ED att/suc | Prior (no dist) |
|------------|-------|--------|---------|------|------------|-----------------|
| dagger     | Short | 52.7%  | 47.1%   | 0.2% | 4.8/2.6    | 74-86% (dom)    |
| arming     | Mid   | 65.8%  | 33.5%   | 0.7% | 4.3/1.6    | 84%             |
| rapier     | Mid   | 71.1%  | 28.2%   | 0.7% | 4.4/1.7    | —               |
| mace       | Mid   | 68.0%  | 31.3%   | 0.8% | 4.3/1.6    | —               |
| warhammer  | Long  | 51.7%  | 43.4%   | 4.9% | 1.3/1.0    | —               |
| spear      | Long  | 63.3%  | 34.2%   | 2.5% | 1.3/1.0    | —               |

### Heavy armour

| Opponent   | Reach | LS win | Opp win | Draw | ED att/suc | Prior (no dist) |
|------------|-------|--------|---------|------|------------|-----------------|
| dagger     | Short | 63.4%  | 36.3%   | 0.2% | 4.8/2.6    | —               |
| arming     | Mid   | 75.7%  | 23.5%   | 0.8% | 4.1/1.6    | —               |
| rapier     | Mid   | 75.7%  | 23.5%   | 0.8% | 4.1/1.6    | —               |
| mace       | Mid   | 66.8%  | 32.6%   | 0.7% | 3.8/1.4    | —               |
| warhammer  | Long  | 45.7%  | 49.3%   | 5.0% | 1.3/1.0    | —               |
| spear      | Long  | 68.3%  | 29.8%   | 1.9% | 1.3/1.0    | —               |

**Pass criteria:** LS 55-65% overall. No matchup >75%.
**Result:** PARTIAL PASS.
- ✅ vs dagger: 52.7% None, 63.4% Heavy — distance creates real counterplay
- ✅ vs warhammer: 51.7% None, 45.7% Heavy — balanced
- ⚠️ vs arming: 65.8% None (borderline), **75.7% Heavy (FAIL)**
- ❌ vs rapier: 71.1% None, **75.7% Heavy (FAIL)**
- ⚠️ vs mace: 68.0% None (over threshold), 66.8% Heavy (over threshold)
- ⚠️ vs spear: 63.3% None (pass), 68.3% Heavy (over threshold)

## Diagnostic: Adjacent penalty +0.5 variant

Tested reducing adjacent penalty from +1.0 to +0.5. Results barely changed (LS vs arming: 64.5% at None, 72.5% at Heavy). Confirms penalty magnitude is not the root cause.

## Structural analysis

**Why distance helps but doesn't resolve:**

1. **Asymmetric range reward.** At Long, longsword has TN 6.5 vs arming's 8.0 (1.5 gap). At Mid, arming has TN 7.0 vs longsword's 7.5 (0.5 gap). The "I got my range" payoff is 3× larger for the long weapon.

2. **Equal Agi = coin-flip distance control.** Both fighters try ED, both have Agi 4, so range outcome is ~50/50. When longsword wins ED, it gets a 1.5 TN advantage. When arming wins, it gets a 0.5 advantage. Expected value favors longsword.

3. **STR×2 compounds TN.** At Long, longsword deals net + 8(STR×2) + Cut mod. Even if it only gets Long 40% of fights, the per-hit damage at Long is decisive.

4. **Warhammer has a different problem.** Distance barely matters because STR×3 = 12 flat damage makes every connection devastating. Even at TN 8.0 (Mid + adjacent penalty), a warhammer hit deals ~17-20 damage.

## Options for Jordan

### Option A: Raise longsword TN to 7.0
No 2H bonus (or Heavy weight cancels it). Longsword at Long = TN 7.0 (same as arming at Mid). Advantage comes from versatility (Cut/Thrust/Bash) and STR×2, not TN.

### Option B: Shield defense bonus for 1H
Give 1H+shield users +2D defense (already in testing plan T6.2). This compensates for TN disadvantage by improving survivability.

### Option C: Cap warhammer STR mult at ×2
Heavy Blunt = Heavy×2 × Blunt×1.5 = ×3 → cap at ×2. Still strong vs armour via Bash damage table, but per-hit not game-ending.

### Option D: Agi-gated distance advantage
Higher Agi gives ED advantage. Longsword users might have lower Agi (Heavy weapon, STR build). This makes stat allocation part of weapon balance.

### Option E: Accept longsword as best dueling weapon
Historically accurate — the longsword IS the optimal duel weapon. Balance via build-point cost (Heavy weapons require higher STR investment, leaving less for Agi/End). Test with unequal stat builds (T7.1).

---

**Recommendation:** Run T7.1 (equal-budget builds) before deciding. If the Fast(Agi 6, dagger) build can use Agi advantage to control distance and beat Knight(STR 5, longsword), the system may self-balance through stat allocation. The current test uses equal stats, which doesn't test the intended stat-weapon tradeoffs.
