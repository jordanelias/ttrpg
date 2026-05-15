# PP-717 NERS Audit & All-Directions Balance

**Session:** v26
**Scope:** D1-D5 ratified changes (MW cap, pool DR, crit threshold, mace commitment, defense triangle)
**Method:** Mode A (formula validation), Mode C (interaction chains), NERS assessment, 6-directional balance

---

## Mode A: Formula Validation — PASS

All five formulas validated at boundary values (End 0-9, Agi 0-8). No division-by-zero, no negative pools, no impossible states. Health cleanly divisible by WI at all End values. Pool floor (min 5) holds. Crit threshold is a clean integer comparison.

One future-proofing flag: D4 trigger (TN > 7.0, 1H) will auto-qualify any future weapon matching those criteria. Design intent is correct, but new weapons should be checked against this trigger.

## Mode C: Interaction Chains — PASS with 2 downstream flags

All chains are one-directional (no circular deps). No dead-end mechanics. Two downstream effects to monitor:

1. **Mass combat TroopCount** derives from Health. End 6 units drop from 60 → 48 HP. TC thresholds may need recalibration. [ASSUMPTION: TC formula references Health — verify against mass combat params.]

2. **D2 + D3 double reduction.** Pool DR reduces dice count, which reduces net hits, which reduces crit probability. At Agi 6 with arena: pool 15+3=18 off dice, net hits still healthy. At Agi 3 without arena: pool 9 off dice, crits become very rare (~3%). This is the intended gradient — weaker fighters almost never crit, stronger fighters crit meaningfully.

---

## NERS Assessment

### D1: Max Wounds Cap (MW = min(floor(End/2)+1, 3))

**N (Necessary):** YES. Without the cap, End is the dominant stat investment at every armour tier (69-82% win rates for End 6). The cap reduces the gap from 50% HP advantage to 20% while preserving the wound system structure. Removing it worsens balance.

**E (Elegant):** YES. Single parameter change (`min(..., 3)`) to an existing formula. No new subsystems, no new tracking. Players can intuit: "maximum 3 wounds before you're out." The wound intervals (WI = End+6) are unchanged — the cap just limits how many intervals fit before incapacitation.

**R (Robust):** PARTIAL. The cap makes all End 6-7 characters functionally identical in wound count (both get 3 wounds). This reduces differentiation at the top end. End 6 gets 48 HP vs End 7's 52 HP — only 4 HP difference. Players investing that 7th point get diminishing returns on the primary combat stat. This is intentional (preventing End dominance) but may feel punishing to players who invest heavily in End.

**S (Smooth):** YES. The formula change propagates cleanly — WI × (MW+1) still holds, wound penalty (-1D per wound) still works, equipment HP (+4/6/8) is additive and unaffected. The only rough edge is the mass combat downstream (TC thresholds), which needs verification but isn't a friction point in personal combat.

### D2: Pool Diminishing Returns (Agi > 4 → +1D instead of +2D)

**N (Necessary):** YES. Without DR, Fast (Agi 6) has pool 17 vs Strong (Agi 3) at pool 11 — a 55% advantage that overwhelms weapon-specific differences. With DR, the gap narrows to 15 vs 11 (36%). The pool formula is the single largest lever in combat; reducing its range compresses the outcome space to let other factors (weapon, armour, protocol) emerge.

**E (Elegant):** PARTIAL. The `min(Agi,4)×2 + max(0,Agi-4)×1` formula is not as clean as the original `Agi×2`. It introduces a breakpoint that players need to learn. However, diminishing returns are a familiar game concept ("soft cap"), and the breakpoint at 4 (the median attribute) is intuitive — investment above average yields less.

**R (Robust):** YES. The DR creates a meaningful choice: invest in Agi for initiative control and distance (full value) or for raw combat dice (diminishing). This splits Agi's utility into two channels — tactical (raw Agi) and statistical (pool) — giving players more to think about. A player choosing Agi 5 vs Agi 6 weighs +1 pool die against other stat investments.

**S (Smooth):** YES. The DR only affects the Combat Pool formula. All other Agi uses (initiative, distance ED, Thread reactions) use raw Agi. No friction with other systems. Fibonacci group bonus is additive to offense, independent of pool formula.

### D3: Crit Threshold ≥ 4 (from ≥ 3)

**N (Necessary):** YES. At ≥ 3, crits fire on 60% of hits with arena stunt — making crits the normal case. This devalues crits as special events and makes the Cut crit (mod ×2) and Bash crit (stun -2D) feel routine rather than exciting. At ≥ 4, crit rate drops to 24% with arena, 5% without — crits become "earned" moments.

**E (Elegant):** YES. Single integer change (3 → 4). No new rules, no new mechanics. The crit system itself is unchanged — only the trigger frequency adjusts.

**R (Robust):** YES. Rarer crits make each one more impactful. A Bash crit stun (-2D next round) at 60% frequency is a minor annoyance. At 24% frequency it's a decisive tactical event that swings the fight. This makes combat more varied — some fights have zero crits, some have one game-changing crit. Emergent narrative.

**S (Smooth):** PARTIAL. The interaction with arena stunt creates a context dependency: arena level strongly affects crit rate. Arena 0 (no stunt) → ~5% crits. Arena 5 → ~35% crits. This means "exhibition duels" (arena 0) are almost crit-free while "championship matches" (arena 5) have frequent crits. This is actually a desirable interaction — higher-stakes venues produce more dramatic moments — but it means combat *feels* different at different arena levels.

### D4: Mace Commitment Bonus (+2D offense, TN > 7.0, 1H)

**N (Necessary):** PARTIAL. Without it, mace wins 29% vs longsword at Heavy — unplayably weak despite being the historically correct anti-armour weapon. With +2D, mace reaches 39-42%. The bonus is necessary for mace viability. However, the trigger condition (TN > 7.0, 1H) is narrow — it exists solely for the mace. If there's only one qualifying weapon, the "general rule" is really "mace rule" wearing a mask.

**E (Elegant):** NO. This is the weakest change on elegance. A conditional bonus that applies to exactly one weapon is a patch, not a principle. The underlying problem is that the Blunt TN modifier (+0.5) creates a penalty that the damage tables don't fully compensate. A more elegant solution would adjust the TN derivation itself (e.g., Blunt weapons don't take the +0.5 penalty because their simplicity compensates — they're easier to use, not harder). Or: remove the TN penalty and reduce the Bash damage table to compensate. The current fix works mechanically but reads as "mace was too weak so we gave it extra dice."

**R (Robust):** YES. The +2D offense makes the mace a genuine choice: you sacrifice versatility (one attack type, predictable defense) for raw power (+2D offense, Bash +4 vs Heavy, STR×1.5). Players choosing mace vs arming sword face a real tradeoff. The commitment mechanic also creates design space — future 1H specialist weapons can be tuned by adjusting TN above or below 7.0.

**S (Smooth):** PARTIAL. The +2D is added to offense pool only, which integrates cleanly with the pool-split mechanic. However, it's a new modifier type — "bonus dice based on weapon property" — that doesn't exist elsewhere in the system. Other modifiers are wound penalties, Fibonacci group bonus, or arena stunt. Each has a different source. Adding another source increases cognitive load.

### D5: Defense Triangle (wrong defense = +2 flat damage)

**N (Necessary):** PARTIAL. The +2 damage bonus fires 33% of the time for versatile weapons and 0% for specialists. Expected impact: +0.67 damage per hit, or ~2 damage per duel. On 40 HP, that's 5%. Borderline whether this is meaningful enough to justify the mechanic's existence. A player who never thinks about the triangle loses about 2 HP per duel. The triangle adds tactical depth but its impact is so small that "ignore it and fight normally" is nearly optimal.

**E (Elegant):** YES. The simplest possible triangle: three types, three defenses, +2 on mismatch. No TN modification, no counter-attacks, no stacking. A player learns it in one sentence: "if you pick the wrong defense, the attacker does 2 extra damage." The interaction with initiative (declare-last → see defense → pick counter) adds strategic depth without rule complexity.

**R (Robust):** PARTIAL. The triangle rewards initiative holders with versatile weapons — they see the defense choice and pick the counter attack type. This creates a synergy: versatile weapon + high Agi (initiative) = exploits the triangle. But the +2 damage is so small that this synergy barely registers in outcomes. The triangle doesn't create the emergent "I read his defense and punished it" moments it's designed for — the payoff is too subtle.

**S (Smooth):** YES. The triangle is independent of all other systems (distance, armour, crits, wounds). It layers on top without friction. The +2 flat damage is the simplest possible integration with the damage formula. No new tracking, no new phases.

---

## All-Directions Balance

### Top-Down: Intent of Game

> "Provide a positive feedback loop between player decisions and mechanics/systems/designs that produces an engaging game world with emergent narratives."

**Assessment:** PP-717 preserves the feedback loop. Player stat allocation decisions (Agi vs End vs STR) map to distinct combat identities (Fast/Tough/Strong) with meaningful tradeoffs. Weapon choice interacts with armour tier to create contextual advantage. The MW cap and pool DR prevent any single stat from dominating, keeping the decision space open.

**Flag:** D5 (defense triangle) has too little impact to qualify as a "player decision → mechanical outcome" link. The +2 damage is noise in the system. Either increase the bonus to make it matter (risk: specialist penalty), reduce the triangle to flavor text, or redesign as a tempo mechanic (counter-attack opportunity, which was tested and found too weak at half-pool).

### Bottom-Up: Individual Mechanics

Each formula validated at boundaries (Mode A). No impossible states, no zero pools, no division errors. All mechanics produce correct outputs at min/max inputs.

**Flag:** D4 trigger condition creates a narrow rule. Bottom-up, it works. But it doesn't emerge from the system — it's imposed on it. A weapon with TN 7.0 (warhammer) gets zero bonus. A weapon with TN 7.5 (mace) gets +2D. The 0.5 TN gap produces a binary outcome. Consider: a graduated bonus based on TN excess over 7.0 (e.g., +1D per 0.5 TN above 7.0) would be more principled.

### Vertical: Attribute Range Scaling

| Attribute | Range | Pre-PP-717 scaling | Post-PP-717 scaling | Assessment |
|-----------|-------|-------------------|--------------------|-|
| End 1→7 | 1-7 | HP 14→65 (4.6×) | HP 14→52 (3.7×) | Compressed ✓ |
| Agi 1→7 | 1-7 | Pool 7→19 (2.7×) | Pool 7→16 (2.3×) | Compressed ✓ |
| STR 1→7 | 1-7 | Damage +1→+7 (weapon×) | Unchanged | Linear ✓ |
| COG 1→7 | 1-7 | Taunt/Composure | Unchanged | Not tested |

Vertical scaling is now more uniform across attributes. End's 3.7× range is closer to Agi's 2.3× range (was 4.6× vs 2.7×). STR remains linear (×weapon multiplier). COG is outside combat scope but should be checked for comparable scaling.

### Diagonal: Cross-System Interactions

| System A | System B | Interaction | PP-717 effect |
|----------|----------|-------------|---------------|
| Combat pool | Wound penalty | Pool - wounds = effective pool | D1 caps max penalty at -3D (was -4D). D2 reduces base pool. Net: smaller pools lose MORE per wound proportionally. Correct — wounded fighters degrade faster. |
| Weapon TN | Armour tier | Damage output | D4 adds mace +2D, partially offsetting TN 7.5 penalty. Diagonal interaction is: higher-TN weapons are compensated if 1H. |
| Arena stunt | Crit threshold | Crit frequency | D3 makes arena level a dial on crit drama. Arena 0 = almost no crits. Arena 5 = frequent crits. Correct — arena difficulty scales dramatic tension. |
| Initiative | Defense triangle | Information advantage | D5 makes initiative valuable for versatile weapons (see defense, pick counter). But the +2 payoff is too small to make this diagonal meaningful in practice. |

**Flag:** The initiative × triangle diagonal should be stronger. Initiative is a core mechanic (Agi-based, deeply embedded). The triangle gives initiative holders a reward, but +2 damage isn't enough to feel it. This weakens initiative's identity as "information advantage."

### Lateral: Peer System Parity

Combat vs Social vs Thread — all use Pool = Attribute × 2 + History + 3 (floor 5). PP-717 changes the Combat Pool to use DR. Social and Thread pools remain linear.

**Flag:** This creates an inconsistency. Combat Agi > 4 has diminishing returns. Social Charisma > 4 does not. Thread Attunement > 4 does not. If the DR principle is correct for combat, it should be evaluated for other pools. Otherwise, the systems diverge in their stat-investment philosophy.

**Mitigation:** Combat is the most frequently rolled pool and the most thoroughly simulated. DR may not be needed for Social/Thread if those systems have other compression mechanisms (e.g., Composure caps social damage, Thread Fatigue limits thread actions). But the inconsistency should be documented as an intentional design choice, not an oversight.

### Horizontal: Play Context Variation

| Context | Pre-PP-717 | Post-PP-717 | Assessment |
|---------|-----------|-------------|------------|
| Unarmoured, arena 3 | Tough 69% ✗ | Tough 62% ✓ | Fixed |
| Unarmoured, arena 5 | Fast 57% ✓ | ~55% ✓ | Maintained |
| Heavy, arena 3 | Strong 82% ✗ | Strong 75% ~ | Improved but not PASS |
| Heavy, arena 0 | Tough 86% ✗ | ~80% ✗ | Marginal improvement |
| Unarmoured mirror | Coin-flip | Coin-flip | Correct |
| Cross-armour (sword vs plate) | Blade useless | Blade useless | Historically correct |

**Flag:** Heavy armour at arena 0 remains unbalanced (80%+ for End/STR builds). This is a duel system issue — without arena stunt dice, fights degenerate to attrition. PP-717 doesn't fix this because the root cause is the stamina system (flat stamina, no stunt = no offensive leverage), not the stat formulas.

---

## Summary Scorecard

| Change | N | E | R | S | Issues |
|--------|---|---|---|---|--------|
| D1 MW Cap | ✓ | ✓ | ~ | ✓ | End 6-7 differentiation reduced. Mass combat TC downstream. |
| D2 Pool DR | ✓ | ~ | ✓ | ✓ | Formula breakpoint slightly inelegant. Social/Thread parity gap. |
| D3 Crit ≥4 | ✓ | ✓ | ✓ | ~ | Arena-dependent crit feel. Intended but notable. |
| D4 Mace +2D | ~ | ✗ | ✓ | ~ | One-weapon rule wearing a general mask. Trigger is a patch. |
| D5 Wrong def +2 | ~ | ✓ | ~ | ✓ | Too small to matter (~5% HP per duel). Weakens init identity. |

**Overall:** D1-D3 are solid changes — necessary, well-integrated, minimal side effects. D4 works mechanically but lacks elegance (it's a mace-specific patch). D5 is the weakest — it's clean but so small that it doesn't achieve its stated purpose (making defense type selection meaningful).

---

## Recommendations

### P2: D4 redesign — remove Blunt TN penalty instead

Instead of +2D offense bonus for TN > 7.0:
- Remove the Blunt type modifier (+0.5 TN) from the TN derivation
- Mace base TN drops from 7.5 → 7.0 (matching arming sword)
- Mace is now TN-competitive but limited to one attack type and lower STR mult (×1.5 vs ×2.0 for longsword)
- The "penalty for simplicity" is ALREADY paid through lack of triangle exploitation and predictable defense

This removes the +2D patch entirely. Sim validation needed to confirm mace hits 40-50% vs longsword at Heavy.

### P3: D5 increase or remove

Option A: Increase wrong-defense bonus to +4 flat damage. Expected impact: +1.33/hit, ~4 damage/duel, 10% of HP. Now meaningful.
Option B: Remove the triangle entirely. It adds cognitive load for 5% HP impact. The arming sword (Cut/Thrust) and longsword (Cut/Thrust/Bash) already have versatility advantage through optimal attack type selection without needing a defense triangle.

### P3: Document Pool DR as combat-specific

Add a note to `designs/scene/derived_stats_v30.md` §4 clarifying that DR applies to Combat Pool only, and that Social/Thread pools remain linear. Flag for future evaluation if those systems show stat dominance.

### P2: Verify mass combat TC thresholds

D1 reduces End 6 Health from 60 → 48. Mass combat TroopCount thresholds use Health. Run Mode A on `params/mass_combat.md` to verify TC calculations still produce reasonable army sizes.
