# Weapon System v2 — Testing Plan
## Date: 2026-05-13
## Status: PLAN — no tests executed yet
## Prerequisite: duel v9 consolidated sim as chassis; extend with weapon v2 mechanics
## Estimated sessions: 2-3

---

## Test structure

Each test section has:
- **Hypothesis** — what we expect, and why
- **Method** — sim parameters, N, controls
- **Pass criteria** — what "working" looks like (ranges, not exact values)
- **Fail action** — what to change if it fails

All tests use N=3000 minimum. Equal stats unless noted (Agi 4, STR 4, End 4, COG 4, Hist 2). Flat duel Stamina (15+End×2). Arena=3 unless noted. Mirror protocols (both ADAPTIVE) unless noted.

---

## Phase 1: Half-point TN validation

Validate that the new TN system produces the intended hit-rate compression without breaking the dice engine.

### T1.1: Hit rate per TN value
**Hypothesis:** TN 6.0 hits ~55% per die. TN 7.5 hits ~35% per die. The spread (6.0→7.5) produces a 1.6× ratio instead of current 2.4× (5→8).
**Method:** Roll 100,000 dice at each TN value (5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0). Measure observed hit rate factoring 1s subtract and 10s chain.
**Pass:** Observed rates within ±2% of theoretical. Monotonic decrease. No TN value produces <25% or >65% hit rate.
**Fail:** Recalibrate modifiers. If the d10 can't resolve half-points cleanly, consider alternative implementation (d20, pool modifier).

### T1.2: Net hits distribution by TN gap
**Hypothesis:** At TN 6.0 vs TN 7.0 (1-point gap), the attacker averages ~0.7 more net hits per exchange than the reverse. At TN 6.0 vs TN 7.5 (1.5-point gap, max spread), ~1.1 more net hits.
**Method:** 10,000 exchanges at each TN pair. 7 offense dice vs 6 defense dice (standard pool at 50/50 split from pool 13). Measure net hit distribution.
**Pass:** Positive mean net hits for the lower-TN attacker. The gap is meaningful but not crushing (no matchup produces >80% hit rate from TN alone).
**Fail:** Adjust modifier scale. If 1.5-point gap is too large, compress to ±0.3 instead of ±0.5.

### T1.3: Fractional TN implementation test
**Hypothesis:** TN 6.5 can be resolved on d10 without breaking the dice engine's chain and subtract rules.
**Method:** Compare three implementations:
  (a) Probabilistic: roll ≥ ceil(TN), but exact floor(TN) has 50% hit chance
  (b) Alternating: odd rounds use ceil, even rounds use floor
  (c) Pool modifier: TN 6.5 = TN 7 with +1D pool bonus
Measure hit rate variance across 100,000 rolls per method.
**Pass:** Method (a) has lowest variance and matches theoretical rate within ±1%.
**Fail:** Use method (c) pool modifier if probabilistic is too noisy.

---

## Phase 2: Weapon matchups by armour tier

Validate that the damage modifier tables + STR multiplier produce historically correct weapon-armour interactions.

### T2.1: Blade vs armour tiers (arming sword mirror)
**Hypothesis:** Blade weapons are devastating unarmoured, useless against plate. Expected: vs None finishes in ~3 rounds, vs Heavy finishes in 8+ rounds or times out.
**Method:** Arming sword (Normal Blade, TN 7.0) mirror at each armour tier. Both ADAPTIVE. Measure: rounds to resolution, damage per hit, win rate symmetry.
**Pass:** Duration roughly doubles from None to Heavy. vs Heavy: >50% of duels reach timeout or yield. Damage per hit vs Heavy < 5 (net + STR×1 + 0 mod).
**Fail:** Blade mod vs Heavy may need to be +1 instead of +0 (complete inability to damage plate is frustrating even if historically accurate).

### T2.2: Blunt inverted curve validation
**Hypothesis:** Mace (Normal Blunt, TN 7.5) is WORSE than arming sword vs unarmoured but BETTER vs Heavy.
**Method:** Mace vs arming sword at each armour tier (both sides same armour). Measure crossover point.
**Pass:** Blade wins at None and Light. Blunt wins at Medium and Heavy. The crossover is at Medium (the "mail" transition point where cutting stops working).
**Fail:** If crossover is at Light, blunt is too strong early. If crossover is at Heavy only, blunt's advantage is too narrow. Adjust +2/+3/+4/+4 curve.

### T2.3: Pierce consistency and STR-dependence
**Hypothesis:** Pierce (rapier, TN 7.0) performs consistently across armour tiers — never best, never worst. vs Heavy: STR 6 rapier significantly outperforms STR 3 rapier.
**Method:** Rapier mirror at each armour tier. Then rapier STR 6 vs STR 3 at Heavy only.
**Pass:** Rapier win rate within 40-60% at all armour tiers (consistent performer). STR 6v3 at Heavy: >60% for STR 6 (STR-dependent gap-finding works).
**Fail:** If Pierce is best at any tier, the "specialist" damage types lose their identity. If STR doesn't differentiate vs Heavy, replace floor(STR/2) with flat +2.

### T2.4: Blunt + STR×3 total damage check
**Hypothesis:** Warhammer (Heavy Blunt, STR×3, TN 6.5 2H) deals ~17-23 damage per hit vs Heavy armour at STR 4-6. This is very high but hits less often than blade weapons.
**Method:** Warhammer vs arming sword at Heavy armour. Measure: damage per successful hit, hits per duel, total damage dealt. Compare DPS (damage per round).
**Pass:** Warhammer DPS ≤ 1.3× arming sword DPS at any armour tier. Warhammer wins at Heavy, loses at None. If warhammer DPS > 1.5× at Heavy, the flat blunt modifier needs reduction.
**Fail:** Reduce flat blunt mod from +4 to +3 vs Heavy. Or cap STR multiplier contribution to damage (STR×3 but capped at STR×2 + STR for the modifier portion).

---

## Phase 3: Multi-attack-type weapon testing

Validate that weapons offering multiple attack types produce correct tactical choices.

### T3.1: Longsword attack type optimality by armour
**Hypothesis:** Longsword Cut is optimal vs None/Light. Longsword Thrust is optimal vs Heavy. Mordhau is never optimal (it's a desperation move with +1.0 TN penalty and STR×1).
**Method:** Longsword (Heavy Blade, TN 6.0 2H) attacks each armour tier with each attack type. Measure damage per round for Cut/Thrust/Bash. Same defender with arming sword.
**Pass:** Cut DPR > Thrust DPR > Mordhau DPR at None/Light. Thrust DPR > Cut DPR at Heavy. Mordhau DPR never exceeds Thrust DPR at any tier. Clear crossover points.
**Fail:** If Mordhau ever beats Thrust, the TN penalty (+1.0) is too small or the Bash damage mods are too high. If Cut beats Thrust at Heavy, the Blade +0 vs Heavy is leaking damage through crits.

### T3.2: Pollaxe versatility advantage
**Hypothesis:** Pollaxe (all 3 attack types at TN 6.0-6.5) wins more duels than mace (Bash only at TN 7.5) across all armour tiers, because the pollaxe picks the optimal attack type per target.
**Method:** Pollaxe (OPTIMAL protocol — always picks best attack type for target armour) vs mace (Bash only). At each armour tier.
**Pass:** Pollaxe wins at None/Light (Blade attack beats Bash damage at low armour). Mace competitive at Heavy (Bash-only damage compensates for TN disadvantage). Pollaxe edge: 55-65% across tiers. Mace edge at Heavy if any: <55%.
**Fail:** If mace never wins any tier, specialist weapons are too weak. Consider: specialist weapons get a "focus" bonus (+0.5 damage per hit for single-type weapons — they've practiced this one thing).

### T3.3: Smart attacker protocol
**Hypothesis:** A protocol that reads target armour and picks the optimal attack type outperforms a protocol that always uses the same attack type by 10-20pp.
**Method:** "Smart" protocol (Cut vs None/Light, Thrust vs Medium/Heavy) vs "Stubborn-Cut" protocol (always Cut) and "Stubborn-Bash" (always Bash). All with longsword.
**Pass:** Smart beats Stubborn-Cut at Heavy by 10-20pp. Smart beats Stubborn-Bash at None by 10-20pp. Smart vs Smart is symmetric.
**Fail:** If Smart only beats Stubborn by <5pp, the attack-type choice doesn't matter enough — the damage modifier gaps need widening.

---

## Phase 4: Defense triangle (Architecture C only)

### T4.1: Triangle modifier measurement
**Hypothesis:** Correct defense choice (Parry vs Cut, Deflect vs Thrust, Brace vs Bash) produces ~10% higher survival rate than incorrect choice. The ±0.5 TN on defense is meaningful but not crushing.
**Method:** Fixed attacker (Cut, 7 offense dice, TN 7.0). Defender at 6 defense dice. Compare defender outcomes: Parry (TN 6.5 defense), neutral (TN 7.0), Brace (TN 7.5). 50,000 exchanges each.
**Pass:** Correct defense blocks ~15% more hits than neutral. Incorrect defense blocks ~15% fewer. Total swing between best and worst defense: ~30% of hits blocked.
**Fail:** If swing < 10%, modifier too small — try ±1.0. If swing > 40%, modifier too large — try ±0.3.

### T4.2: Triangle with initiative
**Hypothesis:** Initiative holder (sees opponent's defense, picks counter-attack) gains ~8-15pp advantage over the non-initiative holder.
**Method:** Duel sim with triangle active. Side A always has initiative. Side A uses "reactive" protocol (sees defense, picks counter). Side B uses random defense type. Mirror stats. 5000 duels.
**Pass:** Side A wins 54-58%. The initiative advantage from the triangle is real but not game-breaking (≤8pp over the duel system's existing ~3pp initiative advantage, total ~11pp).
**Fail:** If >65%, the triangle makes initiative too important — reduces player agency for the non-initiative holder. Consider: defense type declared BEFORE attack type (both sides), so initiative holder sees defense but defender also sees attack.

### T4.3: Specialist weapon penalty in triangle
**Hypothesis:** Mace user (Bash only — opponent always Braces) loses the triangle game by ~5-10pp vs a versatile weapon user. The damage advantage from Bash (STR×1.5, +4 mod vs armour) partially compensates.
**Method:** Mace (ADAPTIVE + always Bash) vs longsword (ADAPTIVE + optimal attack type). Defender protocol: mace user's opponent always Braces. Longsword user's opponent uses random defense. Both Heavy armour (mace's best context). 5000 duels.
**Pass:** Mace loses but by <10pp (45-50% vs longsword). The damage compensation works — mace does more per-hit damage that partially offsets the permanent -0.5 defense TN penalty.
**Fail:** If mace < 40%, specialist penalty too harsh. Options: (a) raise ±0.5 to ±0.3; (b) specialist "commitment" bonus; (c) accept and flag as design intent (specialists trade duel viability for mass combat effectiveness).

### T4.4: Random vs optimal defense
**Hypothesis:** A player who randomly picks defense type (doesn't engage with triangle) performs within 5pp of a player using weapon-default defense type.
**Method:** ADAPTIVE protocol with random defense vs ADAPTIVE with weapon-default defense (arming sword = always Parry). Same attacker using Smart protocol.
**Pass:** Random defense within 45-50%. Weapon-default within 47-53%. The triangle rewards engagement but doesn't crush non-participants.
**Fail:** If random < 40%, the system punishes uninformed players too harshly. The triangle should be an advantage for skilled players, not a trap for casual ones.

---

## Phase 5: Distance rules

### T5.1: Short vs Long positional game
**Hypothesis:** Spear (Long, TN 6.5) dominates at Long range. Dagger (Short, TN 6.0) dominates at Short range. The fight's outcome depends on who controls distance.
**Method:** Spear vs dagger with distance mechanics active. Test at fixed distances: Long (spear optimal), Mid (both penalized), Short (dagger optimal). Then with Establish Distance action available (Agi contest to change range).
**Pass:** At Long: spear 75%+. At Short: dagger 75%+. With distance changes: higher-Agi fighter controls range and wins 60%+ regardless of weapon. Distance IS a fought resource.
**Fail:** If one weapon wins regardless of starting range, the distance system doesn't create a real positional game. Check Establish Distance action economy — is it too cheap/expensive?

### T5.2: Mid weapon performance at non-optimal range
**Hypothesis:** Arming sword (Mid) operates at +1.0 TN penalty at both Long and Short. This makes it a "safe but unexciting" choice — never great, never terrible.
**Method:** Arming sword vs spear at Long, arming sword vs dagger at Short. Both with distance changes enabled.
**Pass:** Arming sword loses both matchups (55-65% for the specialist) but not catastrophically. The Mid weapon is the "generalist" — viable everywhere, optimal nowhere.
**Fail:** If arming sword wins either, the +1.0 penalty is too small. If it loses >70%, the penalty is too large.

### T5.3: Distance + initiative interaction
**Hypothesis:** The fighter with initiative advantage can use Establish Distance reactively — they see the opponent's action and choose to change range if beneficial.
**Method:** Dagger user with initiative vs spear user without. Dagger user protocol: if at Long, Establish Distance to close. If at Short, strike. Compare with initiative reversed.
**Pass:** Initiative holder wins 5-10pp more than non-holder in cross-range matchups. Initiative controls distance, not just strike/defense.
**Fail:** If initiative doesn't affect distance control, the Establish Distance action needs to integrate with the declaration system better.

---

## Phase 6: Two-handed bonus and longsword dominance

### T6.1: Longsword dominance check
**Hypothesis:** Longsword (TN 6.0, STR×2, all 3 attack types, Long reach) is the best duel weapon. This is potentially a problem.
**Method:** Longsword 2H vs every other weapon at equal stats, each armour tier, arena 3. Measure win rate matrix.
**Pass:** Longsword wins 55-65% of matchups. No matchup exceeds 75% (not auto-win). Dagger competitive at Short range. Mace competitive at Heavy armour. The longsword is best overall but has exploitable weaknesses.
**Fail (dominant):** If longsword > 65% across all matchups, it's too good. Reduce 2H bonus to -0.5 total (not -1.0 stacking). Longsword goes from TN 6.0 to TN 6.5.
**Fail (weak):** If longsword < 50% in multiple matchups, the 2H bonus isn't compensating for the no-shield tradeoff. Unlikely given TN 6.0.

### T6.2: Two-handed vs one-handed + shield
**Hypothesis:** Shield provides a defense bonus that competes with the two-handed accuracy bonus. The tradeoff is real.
**Method:** Longsword 2H (TN 6.0, no shield) vs arming sword + shield (TN 7.0, +2D defense from shield). Same stats.
**Pass:** 50-55% for longsword. Close matchup. Shield defense bonus approximately equals the TN accuracy bonus. Different strengths (longsword: offense; arming+shield: defense).
**Fail:** If longsword > 60%, shield is undervalued. If < 45%, shield is too strong (which would be fine — historically, shield fighting is extremely effective).

### T6.3: Two-handed bonus cap test
**Hypothesis:** If the 2H bonus is capped at -0.5 (not stacking), longsword goes to TN 6.5 and the weapon hierarchy rebalances.
**Method:** Re-run T6.1 with 2H bonus = -0.5 flat (not -0.5 weight + -0.5 reach). Compare win rate matrix.
**Pass:** Longsword at TN 6.5 wins 50-60% of matchups. Still good, but dagger (TN 6.0 at Short) and spear (TN 6.5 at Long) are competitive peers.
**Fail:** If longsword at 6.5 drops below 50%, the cap over-nerfs. Keep stacking at -1.0.

---

## Phase 7: Equal-budget build validation

### T7.1: Stat hierarchy with weapon v2
**Hypothesis:** The stat hierarchy changes by weapon type. Heavy blunt builds want STR. Light blade builds want Agi. Pierce builds want STR vs Heavy, Agi otherwise.
**Method:** Equal budget (16 points across Agi/STR/End/COG). Each build paired with its natural weapon and protocol. All-vs-all matrix at arena 0, 3, 5.
**Builds:**
  - Fast (Agi 6/STR 3/End 4/COG 3, dagger, ADAPTIVE)
  - Strong (Agi 3/STR 6/End 4/COG 3, warhammer, AGGRESSIVE)
  - Tough (Agi 3/STR 3/End 6/COG 4, arming sword, ADAPTIVE)
  - Cunning (Agi 4/STR 3/End 4/COG 5, longsword, DUELLIST)
  - Soldier (Agi 4/STR 4/End 4/COG 4, arming sword, ADAPTIVE)
  - Knight (Agi 4/STR 5/End 4/COG 3, longsword, ADAPTIVE)
**Pass:** No build wins >65% of all matchups. Each build has at least one matchup it wins and one it loses. STR builds competitive against armoured targets. Agi builds competitive unarmoured. Arena shifts the hierarchy.
**Fail:** If one build dominates all, the stat-weapon interaction isn't creating enough differentiation. Revisit STR multiplier values or TN modifiers.

### T7.2: Protocol still matters
**Hypothesis:** With weapon v2, protocol matters 15-30pp (down from 20-43pp in v9 because the weapon system absorbs some of the strategic space).
**Method:** Same build, different protocols. Tough with ADAPTIVE vs Tough with STAMINA_FIGHTER. Cunning with DUELLIST vs Cunning with AGGRESSIVE. At arena 3.
**Pass:** Protocol swing 15-30pp. Reduced from v9 but still significant. Player decisions > stat investment.
**Fail:** If protocol swing < 10pp, the weapon system has flattened the strategic space too much. If > 40pp, it hasn't changed anything and the weapon complexity is wasted.

---

## Phase 8: Crit effect validation

### T8.1: Blade crit (×2 mod) vs armour
**Hypothesis:** Blade crit is devastating unarmoured (net 3 + STR + 8 = ~15+ damage) but worthless against plate (net 3 + STR + 0 = ~7 damage). Crit doesn't fix the armour problem.
**Method:** Measure crit frequency and crit damage by armour tier. Longsword vs each armour tier. 5000 duels.
**Pass:** Crit damage vs None > 2× crit damage vs Heavy. Crits matter most unarmoured — correct incentive (blade weapons crit for flesh damage, not armour penetration).
**Fail:** If crit damage is similar across tiers, the ×2 on a +0 mod is still just +0 — which is working correctly. Not really a fail.

### T8.2: Pierce crit (armour downgrade) impact
**Hypothesis:** Pierce crit vs Heavy treats as Medium (+2 instead of floor(STR/2)). This makes pierce crits the high-skill counter to plate — reward consistent performance with gap exploitation.
**Method:** Rapier vs Heavy armour. Measure damage on crit vs non-crit. Compare to blade crit and bash crit at same tier.
**Pass:** Pierce crit vs Heavy adds +1 to +2 effective damage over non-crit (modest improvement). Pierce crit is LESS dramatic than blade crit vs None but MORE useful vs Heavy. Different crit flavors for different contexts.
**Fail:** If Pierce crit vs Heavy produces less damage than Bash non-crit vs Heavy, the armour downgrade isn't worth the crit rarity. Increase to "two tiers lower" or add a flat bonus on top.

### T8.3: Bash crit (×2 mod + stun -2D) lethality
**Hypothesis:** Bash crit is the most impactful crit in the game: ×2 damage mod AND -2D next round. At STR 4 warhammer: net 3 + 12(STR×3) + 8(×2 mod) = 23 damage PLUS stunned. This should end most duels.
**Method:** Measure bash crit frequency and outcome. What % of duels that include a bash crit end on that exchange or the next?
**Pass:** 60%+ of bash crits lead to duel resolution within 2 rounds. The bash crit IS the knockout blow.
**Fail:** If bash crits are too common (>15% of exchanges), the stun effect dominates the duel. Cap stun at -1D instead of -2D. If too rare (<5%), the mechanic is decorative.

---

## Phase 9: Integration tests

### T9.1: Full weapon v2 duel system integration
**Hypothesis:** The weapon v2 system integrates with the duel context layer (flat stamina, free-rider taunt, arena stunt, E7 yield, defense triangle) without breaking any validated duel mechanic.
**Method:** Run the complete v9 duel battery (§1-§7 from duel_stress_test.py) with weapon v2 mechanics active. Compare results to v9 baseline.
**Pass:** All v9 findings hold qualitatively. Protocol > stats. Arena shifts hierarchy. Taunt makes COG meaningful. No new degenerate strategy emerges.
**Fail:** If a previously balanced matchup becomes >70%, the weapon changes introduced an interaction that breaks the duel balance. Isolate which weapon v2 mechanic caused the regression.

### T9.2: Scene combat (Architecture A) sanity check
**Hypothesis:** Multi-attack-type weapons work in group combat. The attack-type choice (by target armour) is a simple AI decision. Defense triangle is OFF (weapon-default defense only). No new overhead.
**Method:** 3v3 skirmish sim. Mixed weapons and armour. AI picks attack type based on target armour (smart protocol). Measure: does the sim run without degeneracy? Do mixed-armour groups produce interesting weapon choices?
**Pass:** No single weapon dominates all 3v3 scenarios. AI correctly switches attack type by target. Fights resolve in reasonable time (3-8 rounds). No infinite loops.
**Fail:** If AI attack-type selection creates analysis paralysis or weird oscillations, simplify to "always use highest-damage attack type" for scene combat.

---

## Execution order

Priority 1 (must pass before any ratification):
- T1.1, T1.2 (TN system works)
- T2.1, T2.2, T2.4 (damage tables produce correct armour interactions)
- T6.1 (longsword dominance check)

Priority 2 (must pass before weapon v2 ratification):
- T2.3 (Pierce consistency)
- T3.1, T3.2, T3.3 (multi-attack works)
- T4.1, T4.2, T4.3 (triangle works in duels)
- T5.1 (distance creates positional game)
- T7.1 (builds differentiate)

Priority 3 (can iterate post-ratification):
- T4.4, T5.2, T5.3 (edge cases)
- T6.2, T6.3 (shield tradeoff, 2H cap)
- T7.2 (protocol still matters)
- T8.1, T8.2, T8.3 (crit effects)
- T9.1, T9.2 (integration)
- T1.3 (implementation method)

---

## Decision gates

After Phase 1-2: **GO/NO-GO on half-point TN + damage tables.** If TN system and damage tables fail, the weapon v2 rearchitecture is rejected and we iterate on the current integer TN system with STR multiplier only.

After Phase 3-4: **GO/NO-GO on defense triangle.** If triangle modifier is too subtle or too harsh, triangle is rejected for duels and defense defaults to weapon type everywhere.

After Phase 6: **GO/NO-GO on two-handed stacking.** If longsword dominates, cap 2H bonus at -0.5.

After Phase 7: **RATIFY or ITERATE.** If builds differentiate and protocol matters, weapon v2 is ratified. If not, iterate on specific values.
