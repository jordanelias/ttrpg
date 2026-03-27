# VALORIA — STRESS TESTS BATCH 5
## Core Combat Engine: M-01 through M-09
### Date: 2026-03-27 · Simulator Modes: A (Isolation) + B (Interaction) + D (Edge Cases)

Probability reference (d10, TN 7): expected net per die ≈ 0.33. P(≥N net) from simulator skill table.
Mass combat uses TN 5: P(die ≥ 5) = 0.6; with 1s: expected net per die ≈ 0.5.

---

## M-01 · POOL SPLIT (OFFENCE / DEFENCE)
### Mode A — Isolation

**Input space:**

| Variable | Range | Typical | Edge |
|---|---|---|---|
| Combat Pool | 5–15+ | 7–9 | 5 (minimum), 15+ (high-skill) |
| Split ratio | 0:all to all:0 | ~50/50 | All offence (reckless), all defence (full guard) |
| Wound count | 0–4 | 0–1 | 4 (near incapacitation) |

**Probability tables — attack (Weapon TN varies; using TN 7 as baseline, TN 6 for typical weapons):**

At TN 6: P(success per die) ≈ 0.5; expected net per die ≈ 0.4 (0.5 − 0.1 from 1s + chain).

| Offence Dice | Defence Dice (opp) | P(hit) | Expected Excess |
|---|---|---|---|
| 3 vs 3 | 3 vs 3 | ~60% | ~0.4 |
| 5 vs 3 | 3 vs 3 | ~80% | ~1.0 |
| 7 vs 3 | 3 vs 3 | ~92% | ~1.8 |
| 3 vs 5 | 5 vs 5 | ~35% | −0.4 (likely miss) |
| 5 vs 5 | 5 vs 5 | ~50% | 0 |
| 9 vs 4 | 4 vs 4 | ~88% | ~1.8 |

**Finding B5-M01-A (Degenerate — Reckless):** Full offence (all dice to attack, 0 defence): opponent hits automatically if they allocate any offence dice. For a 7-die pool all-in offence: expected damage output ~2.8 excess + weapon bonus − armour. Expected incoming: opponent's full pool unopposed. Net trade: you deal heavy damage AND take heavy damage simultaneously. Viable only if you can absorb the hit. Not a dominant strategy at equal pools.

**Finding B5-M01-B (Degenerate — Full Guard):** All dice to defence, 0 offence: opponent cannot score excess successes if your defence pool ≥ their offence pool. At 9D defence vs 5D offence: opponent's expected net ≈ 2.0 − 3.0 = negative → no hit. Fully safe. P(opponent hits) ≈ 5%. **This is the dominant defensive strategy but creates stalemate** — neither combatant acts if both go full guard. Resolves through Stamina drain (must eventually commit offence) or positional manoeuvre. Stalemate is dynamic, not locked. ✓

**Finding B5-M01-C (Cliff at Pool = 5):** Minimum pool 5D. Split options: 1/4, 2/3, 3/2, 4/1. At 2 offence vs 3 defence (opponent): P(hit) ≈ 30%. Low-pool combatants are not meaningless but are significantly disadvantaged. The minimum 5D floor prevents complete helplessness. ✓

**Finding B5-M01-D (Initiative advantage quantified):** Initiative winner declares last. Value: opponent commits to 5O/4D, then you commit 6O/3D (knowing their defence is 4). Your expected hit: ~70%. Without initiative: ~55%. Initiative advantage worth ~15pp hit probability per round. Significant but not decisive. ✓

**P3 Finding — Wounds interaction with pool split:** Wounds add +1 Ob not −1D, so pool split decisions are unchanged by wounds. This is clean — wounded characters fight with the same pool but at penalty to effect. No complexity cascade. ✓

---

## M-02 · WOUND / GATE SYSTEM
### Mode A — Isolation

**Input space:**

| Variable | Range | Notes |
|---|---|---|
| Health | 7–13 (Endurance 1–7) | Most characters 8–10 |
| Wound threshold | 2–4 (Endurance-dependent) | |
| Single hit | 0–30+ theoretically | Capped at 3× Health per hit |
| +1 Ob per Wound | Stacks to +4 | At 4 Wounds: +4 Ob on all rolls |

**Health by Endurance:**
| Endurance | Health | Incapacitation | Wound Ob at incap |
|---|---|---|---|
| 1 | 7 | 2 Wounds | +2 Ob all rolls |
| 3 | 9 | 2 Wounds | +2 Ob all rolls |
| 4 | 10 | 3 Wounds | +3 Ob all rolls |
| 5 | 11 | 3 Wounds | +3 Ob all rolls |
| 6 | 12 | 4 Wounds | +4 Ob all rolls |
| 7 | 13 | 4 Wounds | +4 Ob all rolls |

**Wound Ob cascade on a typical 7D combat pool, Ob 1 base:**
| Wounds | Effective Ob | P(≥1 net, 7D) |
|---|---|---|
| 0 | 1 | ~99% |
| 1 | 2 | ~92% |
| 2 | 3 | ~70% |
| 3 | 4 | ~45% |
| 4 | 5 | ~25% |

**Finding B5-M02-A (Cascade — Wound × Thread ops):** At Wound 2+, Thread operations at Relational scale face Ob 1 (base) + Ob 2 (scale) + Ob 2 (wounds) = Ob 5. P(success, 6D pool, TN 7) ≈ 35%. A heavily wounded practitioner is nearly non-functional in Thread work. This is **intentional and well-calibrated** — taking wounds in combat before attempting Thread ops is a meaningful cost. ✓

**Finding B5-M02-B (Single-hit cap):** Cap at 3× Health. Endurance 3 → Health 9 → cap 27 damage. No realistic weapon produces 27 damage (max realistic: +2 weapon + 10 excess + Brutal +4 = 16). Cap is unreachable in normal play. Serves as a theoretical edge guard only. ✓

**Finding B5-M02-C (Wound reset mechanic):** Health resets to full after each Wound. Implication: a character at Health 1 who takes 8 damage (Health 9) takes exactly 1 Wound and resets to 9 Health — not 2 Wounds. The reset means large-but-sub-double-Health hits produce exactly 1 Wound, no carryover above reset. This is clean. ✓

**Finding B5-M02-D (P2 — excess carryover ambiguity):** Rule states "excess damage carries over into reset Health." Scenario: Health 9, character at Health 1 takes 15 damage. First 1 point → Wound #1, Health resets to 9. Remaining 14 → reduces Health to max(9−14) = 0 → Wound #2. Single-hit cap: no single hit inflicts more than 2 Wounds, so this is the ceiling. But what if Endurance 3 (incapacitation at 2 Wounds)? The character takes 2 Wounds from one attack and is incapacitated — fine. Single-hit cap is correctly stated. ✓

**Finding B5-M02-E (Boundary — Health 0 vs ≤0):** Rule says "When Health reaches 0" — implies exactly 0. Damage can produce fractional results? No — all damage is integers. Excess always produces integer Health values. No boundary ambiguity. ✓

---

## M-03 · STAMINA SYSTEM
### Mode A — Isolation

**Input space:**

| Variable | Range | Notes |
|---|---|---|
| Stamina | 2–8 (Endurance + 1) | Starts full each combat |
| Depletion trigger | Every round with Move, Manoeuvre, or Attack | Not defence-only rounds |
| Catch Breath | Pool ÷ 2, defence-only | Forces vulnerability |
| Breather (voluntary) | Defence-only | Voluntarily take before hitting 0 |

**Stamina depletion rate by combat style:**
| Style | Rounds to Depletion |
|---|---|
| Attack every round (End 2 → Stamina 3) | 3 rounds |
| Attack every round (End 4 → Stamina 5) | 5 rounds |
| Attack every round (End 7 → Stamina 8) | 8 rounds |
| Defence-only rounds (any Endurance) | Unlimited (no depletion) |

**Finding B5-M03-A (P2 — Stamina depletion wording ambiguity):** "Decreases by 1 for every melee round in a row where a character has Moved, Manoeuvred or Attacked." The phrase **"in a row"** implies Stamina resets if the character takes even one defence-only round. This creates a strong tactical incentive to take a free defence-only round every N−1 rounds to avoid ever hitting 0 — effectively neutering the Stamina system for disciplined players.

**Mechanism:** Endurance 4 → Stamina 5. Attack rounds 1–4, then full-guard round 5 (Stamina resets to 5), then attack rounds 6–9, full guard round 10... Indefinitely. Never forced into Catch Breath.

**Severity: P2** — the "in a row" qualifier creates an easy exploit. Intended reading is probably cumulative per combat, not consecutive.

**Proposed fix:** Remove "in a row." Stamina decreases by 1 for every round in which the character has Moved, Manoeuvred, or Attacked. It does not reset on a passive round; only Catch Breath or Breather restore it.

**Finding B5-M03-B (P2 — Breather vs Catch Breath distinction unclear):** Both Breather and Catch Breath result in: defence-only, Stamina restored. Difference: Catch Breath halves combat pool (rounded up); Breather doesn't. But the rule says Breather is "voluntary before Stamina reaches 0" while Catch Breath is forced "once Stamina reaches 0." The mechanical difference (pool penalty) is buried. At the table: players will always prefer Breather over Catch Breath because pool is halved for Catch Breath. The system therefore rewards proactive Stamina management — consistent with design intent. ✓ (functionally sound; P3 wording clarity only)

**Finding B5-M03-C (Boundary — Stamina 0 immediately after hit):** Stamina 1, character attacks. Stamina → 0. They must Catch Breath. But Catch Breath is on their next round. Current round resolves normally (they attacked this round). **Is the Catch Breath mandatory this round or next?** The rule doesn't specify timing. At the table: most natural reading is "character must Catch Breath as their next action." This needs a note.

**Severity: P3** — minor wording issue. Add: "A character whose Stamina reaches 0 must Catch Breath on their next declared action."

---

## M-04 · REACH (SHORT / LONG / PROJECTILE)
### Mode A — Isolation

**Finding B5-M04-A: Reach priority rule creates initiative-like secondary system at Priority 3.**
Reach advantage grants one priority attack before shorter weapon can close. This fires only on first engagement at mismatched range. Once both are at the same range, weapon speed (Fast/Standard/Slow) determines order. The two-tier priority (reach then speed) is clean. ✓

**Finding B5-M04-B (Ambiguity — who has "reach advantage" when both use Long weapons?):** Both using longswords (Long/Standard). Starting at long range: both have same reach. Priority attack for whom? The rule says "longer weapon gets one priority attack" — if equal reach, no priority attack. Correct. ✓

**Finding B5-M04-C (P2 — Projectile range escape):** Rule: "A character must successfully dodge the ranged weapon user's fire to close distance." Mechanic: Dodge roll. But dodge is Defence dice in the pool split — not a standalone check. At what Ob? The rule says "must dodge" without specifying an Ob or what "successfully" means. A character with 8D all-in defence vs a crossbow at projectile range: what's the check?

**Severity: P2** — projectile range closing procedure is incomplete. Missing: explicit Ob for the closing dodge attempt. Proposed fix: Closing vs. projectile: Agility check (standalone, not pool-split), Ob = ranged attacker's net successes that round. On success: character closes to long range. On failure: no closure, take damage normally.

**Finding B5-M04-D (Edge — projectile into melee):** Ranged character "cannot use ranged weapons at short or long melee range." If an archer is engaged in melee by a Short weapon user who has closed — archer cannot fire. Must draw backup weapon (Priority 4) and defend with Agility only at Ob 2 until then. This is a pronounced disadvantage — by design. ✓

---

## M-05 · ZONE-BASED MOVEMENT
### Mode A — Isolation

**Finding B5-M05-A: Zone definition is entirely narrative — no mechanical constraints on zone size or transition cost.** A zone is "a narratively coherent area." Moving between zones costs one action (Manoeuvre or Move, Priority 3). No defined limit on zone count per scene, no speed attribute differentiating zone traversal.

**This is a deliberate design choice** — zones avoid grid complexity. The absence of mechanical constraints is a feature, not a gap. ✓

**Finding B5-M05-B (P3 — Zone transition during Thread contact):** Thread contact maximum duration = Focus score (Contact Rounds). Moving between zones: does this count as losing contact? The rule on Thread operations states contact is lost if "the practitioner is incapacitated, forcibly moved, or loses concentration." Zone transition via normal movement is not "forced" movement. A practitioner can move zones while maintaining contact without interruption — but this isn't explicitly stated. A clarifying note would prevent table disputes.

**Severity: P3** — add note at §5.2: "Moving to an adjacent zone does not break Thread contact unless the target configuration is not present in the new zone."

---

## M-06 · INITIATIVE / PRIORITY
### Mode A + Mode D

**Finding B5-M06-A: Initiative is binary (win/lose), not tiered.** One combatant declares last. There is no partial initiative — no "both tie for one round then reroll" confusion past the initial tie-break. ✓

**Finding B5-M06-B (P3 — Initiative persistence rule):** "Initiative holds for the entire combat unless Reorient changes it." But what if new combatants enter mid-combat? No rule for late entrants. Most natural resolution: late entrants roll initiative and are inserted into the existing order. This needs a note.

**Severity: P3** — add: "Combatants entering an ongoing combat roll initiative immediately on entry; they are inserted into the existing declaration order at their result."

**Finding B5-M06-C (Interaction — Priority table × Thread operations):** Thread effects manifest at Priority 1; Thread operations initiated at Priority 5. A practitioner who initiates a Leap at Priority 5 in Round 1: the contact is established by Priority 5 Round 1. Do they need to wait until Priority 1 Round 2 for an operation effect to manifest, or does the operation resolve in the same round? The rule says "Thread operation effects manifesting from prior rounds" are Priority 1. So a Weaving begun at Priority 5 Round 1 manifests at Priority 1 Round 2. **This is a 2-round delay.** For fast fights (2–3 rounds average), Thread operations rarely fire before combat ends. This is an intentional cost — practitioners are not effective in fast ambushes. Narratively appropriate. ✓

**Finding B5-M06-D (P1 — Priority 3 sub-rule B × pool split):** "The longer weapon gets one priority attack before the shorter can reach." This priority attack occurs at Priority 3A (before normal Priority 3 attacks). But pool split happens at Phase 2 (before all resolution). Does the longer weapon's priority attack use their pre-declared Offence pool? Yes — all pools are pre-declared. **But if the longer weapon user didn't know at declaration time that they'd have a priority attack (they didn't know opponent would try to close), their pool split may be suboptimal.**

The rule says the longer weapon user always has priority attack when shorter weapon tries to close. This means: at declaration, if you have a longer weapon, you should always assume the possibility of a closing attempt and pre-allocate offence accordingly. This creates a metagame pressure but no mechanical ambiguity. ✓

---

## M-07 · FIBONACCI GROUP BONUS
### Mode A — Isolation

**Input space:**

| Attackers | Bonus | Total bonus pool contribution |
|---|---|---|
| 2 vs 1 | +2D total (each gets +1D) | +2D |
| 3 vs 1 | +6D total (each gets +2D) | +6D |
| 4 vs 1 | +8D total (each gets +2D?) | +8D |
| 5 vs 1 | +15D total (each gets +3D) | +15D |
| 8 vs 1 | +40D total (each gets +5D) | +40D |

**Note: CP14 §8.1 uses a different table from §1.9.** §1.9: 2=+1D each, 3+=+2D each, 5+=+3D each, 8+=+5D each. §8.1 (Group Attacks): 2=+2D, 3=+3D, 4=+5D, 5=+8D (aggregate, not per-attacker). These are different tables with different framing. **This is a contradiction.**

**Finding B5-M07-A (P1 — Two incompatible Group Bonus tables):**

- §1.9 (Fibonacci Group Bonus): per-attacker bonuses: 2v1→+1D each, 3+v1→+2D each, 5+v1→+3D each, 8+v1→+5D each
- §8.1 (Group Attacks): aggregate bonus totals: 2→+2D, 3→+3D, 4→+5D, 5→+8D

For 2 attackers: §1.9 gives +1D each (+2D total). §8.1 gives +2D aggregate (+1D each if split evenly). Same result.
For 3 attackers: §1.9 gives +2D each (+6D total). §8.1 gives +3D aggregate (+1D each). **Contradiction: §1.9 gives 2× more bonus.**
For 5 attackers: §1.9 gives +3D each (+15D total). §8.1 gives +8D aggregate (+1.6D each). **§1.9 gives ~2× more bonus.**

**Severity: P1** — at 3+ attackers, the two sections produce different outcomes. One must be canonical. §1.9 is the core rules section and should govern. §8.1 appears to be an incorrect simplification. **Fix: Remove §8.1 Group Attacks table; replace with cross-reference to §1.9.**

**Finding B5-M07-B (Degenerate — 8 vs 1):** §1.9: 8+ attackers each get +5D. An 8-person mob each with 5D base pool → each attacker has 10D. Expected hits on single defender (split defence across 8 attackers, ~1D each): each attacker hits near-automatically. This is **intentionally overwhelming** — 8 vs 1 is not a balanced fight. The mechanic correctly models mob advantage without requiring complex sub-systems. ✓

**Finding B5-M07-C (Boundary — "unsupported" definition):** §1.9: bonus applies if opponent is "unsupported" (no ally engaging any attacker). With 3 attackers and 1 defender who has 1 ally: ally engages 1 of the 3 attackers. Do the remaining 2 attackers still get the group bonus? The rule says "no ally is engaging any of the attackers" — so if any ally is engaging any attacker, no bonus applies. **This means a single dedicated protector nullifies all group bonuses.** P2 — likely too strong a nullification. A single ally can cancel group bonuses for 8 attackers.

**Severity: P2** — the "unsupported" definition creates all-or-nothing group bonus nullification. Fix: "If the target has an ally engaging at least one attacker, the group bonus is reduced by one step (e.g., 5v1 with support = 3v1 bonus tier)."

---

## M-08 · BEGINNER'S LUCK
### Mode A — Isolation

**Input space:** Double Ob, raw attribute only (no History). Typical attributes 2–4.

| Attribute | Normal Ob | Beginner's Luck Ob | Pool | P(success BL) |
|---|---|---|---|---|
| 2 | 1 | 2 | 2D | ~30% |
| 3 | 1 | 2 | 3D | ~50% |
| 3 | 2 | 4 | 3D | ~10% |
| 4 | 2 | 4 | 4D | ~25% |
| 4 | 3 | 6 | 4D | ~3% |

**Finding B5-M08-A (Degenerate — high Ob BL):** Beginner's Luck at Ob 3 (normal) becomes Ob 6 (BL). A 4D pool at Ob 6: P(≥6 net at TN7) ≈ <1%. Functionally impossible. At Ob 4+, Beginner's Luck is non-viable — characters should not attempt difficult tasks without training. **This is correct design.** ✓

**Finding B5-M08-B (Reward inconsistency):** Beginner's Luck success earns "first mark toward a new History." But establishing a new History requires: declaring it in Session Zero OR 2 CP + a scene. BL success alone doesn't establish a History — it earns a first mark on a not-yet-established History. What does that mark apply to? The text says "new History" but there's no existing History to mark.

**Severity: P2** — unclear what "first mark" means without an established History. Fix: "A successful Beginner's Luck roll earns the character a provisional History tag at 0 points; the next relevant scene or CP investment formalises it."

**Finding B5-M08-C: BL exclusions are complete and sensible.** Thread ops, combat proficiency, faction Domain Actions all excluded. No gap. ✓

---

## M-09 · MOMENTUM
### Mode A + Mode D

**Input space:**

| Variable | Range | Notes |
|---|---|---|
| Momentum | 0–4 | Resets each session |
| Gain | +1 per Overwhelming | Also: +1 per Belief achieved |
| Spend | Any amount, before any non-Thread roll | 1 Momentum = 1 auto success |

**Finding B5-M09-A (P2 — Momentum cap of 4 creates hoarding disincentive):** Range 0–4. If a character hits 4 Momentum via a series of Overwhelming successes, all further Overwhelmings don't generate Momentum (capped). There is no incentive to spend Momentum to make room — spending 1 Momentum on a roll where you'd succeed anyway is neutral EV. **At cap: Momentum spend is free (EV neutral) but players are psychologically reluctant to spend resources.** In practice, Momentum likely hoards at 4 and is spent only on high-stakes moments. This is fine strategically but means the session-reset rule does most of the work. The cap itself has minimal in-session effect.

**Severity: P3** — not a mechanical problem. Consider raising cap to 6 for more meaningful in-session use, but current design is functional.

**Finding B5-M09-B: "Cannot be spent on Thread rolls" is clean.** Prevents Momentum from trivialising Thread difficulty. Thread operations have their own risk economy (ThS, Intelligibility, Certainty). ✓

**Finding B5-M09-C (Boundary — can Momentum reduce Ob below 1?):** Spending 3 Momentum on an Ob 2 roll produces 3 auto-successes. Net = 3 ≥ 2 = Success (Overwhelming if 3 ≥ 4? No — 3 < 2×2=4). Net 3 at Ob 2: ≥ Ob = Success. Overwhelming requires net ≥ 2× Ob = 4. So 3 Momentum at Ob 2 buys a guaranteed Success but not Overwhelming. Clean. ✓

**Finding B5-M09-D (Optimal play — Momentum × Beginner's Luck):** Spending Momentum on a Beginner's Luck roll halves BL's doubled Ob impact (1 Momentum = 1 success regardless of Ob). At BL Ob 4 (2 raw, Ob 2 base): 4 auto-successes via Momentum guarantees success regardless of pool. **Is this intended?** Momentum on BL: the character is drawing on accumulated advantage (prior Overwhelming moments) to push through an untrained task. Narratively plausible; mechanically allows BL on normally impossible untrained tasks if Momentum is banked. **P3 edge case — not broken but notable.**

---

## MODE B — INTERACTION CHAINS (Critical combat combinations)

### B-CHAIN-01: Pool Split × Wounds × Stamina (Three-way cascade)

**Scenario:** Character with Endurance 3, Health 9, Stamina 4, Combat Pool 8.

**Round 1:** Pool split 5O/3D. Opponent (Pool 7, split 4O/3D).
- Attacker (5D TN6 vs 3D TN7 defence): expected attack net ≈ 5×0.4 = 2.0. Expected defence net ≈ 3×0.33 = 1.0. Expected excess ≈ 1.0. Damage = +1 weapon + 1 excess − 1 armour = 1. Health 9→8.
- Counter-hit (4D TN6 vs 3D TN7): expected excess ≈ (4×0.4) − (3×0.33) = 1.6 − 1.0 = 0.6. Damage = +1 weapon + 0.6 − 0 armour = 1.6. Health 9→7.4 (round to 7).
- Stamina: both attacked → Stamina −1. Character: Stamina 3. Opponent: Stamina 3 (assumed Endurance 3).

**Round 2:** Same split. Character Health 8, Opponent Health ~7.
- Both take ~1–2 damage again. Character reaches Health ~6 by round 3.

**Round 3:** Character at Health 6. Takes 4 damage (excess spike). Health 6→2. No Wound yet.
- Stamina: 3→2. Character at Stamina 2 — no Catch Breath needed.

**Round 4:** Character takes 3 damage. Health 2→0 → Wound #1. Health resets to 9. +1 Ob all rolls.
- Pool: still 8D but all rolls now at +1 Ob. Combat attack was already Ob 1 (hit) → now Ob 2.
- P(hit at Ob 2, 5D TN6) ≈ 60% (was ~80%). Drop in hit probability.
- Stamina: 2→1.

**Round 5:** Stamina 1→0. Must Catch Breath next round. Pool halved to 4D.
- At Wound 1 + Catch Breath: 4D pool, +1 Ob. P(hit) ≈ 35%.

**Finding B5-B01-A: Wound × Stamina collapse is rapid.** A low-Endurance character (Endurance 3) enters a "crisis cascade" by round 5: Wound penalty + forced Catch Breath simultaneously. At this point they are highly vulnerable. This is **correctly calibrated** — Endurance 3 represents a fragile combatant. Players running Endurance 3 should avoid extended melee. ✓

**Finding B5-B01-B (P2 — No Wound recovery mid-combat):** Quick Rest (removes 1 Wound, restores Health) requires "minutes to hours of downtime." There is no mid-combat wound recovery. A character at 2 Wounds (Endurance 3 = incapacitated) is out. No mechanism to "fight through" at penalty beyond incapacitation. This is correct — incapacitation is final unless narrative exception applies. ✓

### B-CHAIN-02: Fibonacci Group Bonus × Pool Split × Defence Splitting

**Scenario:** 3 attackers (each Pool 6) vs 1 defender (Pool 9, full defence declared — 9D defence).

Per §1.9: 3 attackers each get +2D bonus → each attacker has 8D offence.

Defender must split 9 defence dice across 3 attackers: 3D each.

**Each attacker:** 8D TN6 vs 3D TN7.
- Attack expected net: 8×0.4 = 3.2. Defence expected net: 3×0.33 = 1.0. Excess: 2.2.
- P(hit) for each attacker ≈ 90%.

Expected damage per hit: +1 weapon + 2.2 excess − armour. At 0 armour: 3.2 damage per attacker.
With 3 attackers, all hitting: ~9.6 expected damage in one round. Health 9 (Endurance 3): 1 Wound immediately, likely 2 Wounds (incapacitated) within 2 rounds.

**Finding B5-B02-A: 3v1 with group bonus is overwhelming regardless of defender pool.** A 9D full-guard defender cannot survive 3 skilled attackers (Pool 6+). The Fibonacci bonus makes 3v1 a near-guaranteed incapacitation within 2 rounds. This is **intentional** — 3v1 should be lethal. The bonus correctly models gang-up pressure. ✓

**Finding B5-B02-B (P2 — Defence splitting across 3+ attackers is cognitively demanding):** The defender must decide how to split 9 dice across 3 attackers simultaneously. No guidance exists on optimal splitting. If defender knows attacker pools are equal, equal splits are rational (3/3/3). But if one attacker is stronger: concentrate defence on them. **No rule specifies whether defender must split evenly or can concentrate.**

**Proposed fix:** Add explicit note: "The defender distributes defence dice however they choose; the allocation must be declared simultaneously with attackers' declarations and cannot be changed after Offence is revealed."

---

## MODE D — EDGE CASES (Combat engine, all mechanics)

### Boundary: Combat Pool at minimum (5D) × Full Guard × Fibonacci vs 1

Pool 5D, all-defence vs 3 attackers with group bonus (each 6D base + 2D = 8D).
Defender: 5D ÷ 3 ≈ 1–2D per attacker. Each attacker: 8D TN6 vs 1–2D TN7.
P(hit per attacker): ~95%. Expected damage: 3.2 per attacker. Character with Health 9 takes ~9.6 in one round = Wound + near-second Wound. Minimum-pool combatant vs 3v1 = near-instant incapacitation. **Expected and correctly calibrated.** ✓

### Cascade: Wound × Ob stacking maximum

Scenario: 4 Wounds (Endurance 6, not yet incapacitated) + Ob 2 base task = effective Ob 6.
Thread operation at Relational scale (Ob 2) + 4 Wounds = Ob 6. TPS 5D pool + 0D History = 5D.
P(≥6 net at TN7, 5D) ≈ <2%. Functionally impossible. Character must rest before attempting Thread work.
**Maximum Ob 10 cap**: 4 Wounds + Ob 8 (Structural) = Ob 12, capped at 10. The cap correctly prevents absurd stacking. ✓

### Deadlock: Ambush × No combat-capable characters

Scenario: All PCs have Endurance 1 (Health 7) and 0 Combat History. Pool = 5D minimum. Ambush fires — attackers get free Priority 2 round. PCs cannot prevent the Priority 2 attacks (they haven't declared yet). At least one PC likely takes a Wound before any action. Next round: +1 Ob on all actions including attempts to flee. **Flee Ob?** Not defined.

**Finding B5-D01 (P2 — No Withdraw / Flee Ob defined):** The Withdraw manoeuvre exists (Priority 3A) but its Ob is not stated. §8.1: "Withdraw: Sacrifice offensive action; re-establish reach advantage." This is a within-combat positioning manoeuvre, not an escape from combat. **No rule covers escaping combat entirely.** A character who wants to flee a losing fight has no defined procedure.

**Severity: P2.** Proposed fix: Add to §8.1: "Escaping combat: Agility roll, Ob = opponent's Cognition (their awareness of your intent). On Success: character is out of combat but at full Endurance cost (Stamina 0). On Failure: opponent gets one free Priority 3 attack before you exit."

### Crunch Cascade: Peak complexity round count

A maximum-complexity combat round involves:
1. Initiative roll (Agility, 2+ combatants)
2. Declaration phase (all combatants)
3. Pool division (all combatants, secret)
4. Priority 1 (Thread effect manifestation)
5. Priority 2 (ranged — 2 ranged combatants)
6. Priority 3A (manoeuvres — all 7 types possible)
7. Priority 3 (all melee attacks — each pair resolves)
8. Priority 4 (standard actions)
9. Priority 5 (Thread initiation)
10. Priority 6 (reloads)
11. Damage calculation × combatant count
12. Wound checks × combatant count
13. Stamina decrement × combatant count
14. Thread contact round decrement (practitioners)
15. Co-movement roll (d10) per Thread op

For 6 combatants (3v3) with 2 practitioners:

Estimated resolution steps: ~20–25 per round. At 3 rounds (typical combat): 60–75 total resolution steps.

**Finding B5-D02 (P2 — Crunch cascade at 4+ combatants with Thread):** 4v4 with 2 practitioners each attempting Thread operations produces ~30 resolution steps per round. This is table-heavy but manageable with pre-calculated pools. The pre-calculation requirement on the character sheet (noted multiple times in CP14) is essential to keeping this playable. Without it, each Thread pool requires 3 lookups mid-combat. ✓ with pre-calculation enforced.

### Optimal Play: Full-Guard Loop exploitation

**Scenario:** Two high-pool characters (Pool 12 each) both declare Full Guard every round.
- Round 1: Both 12D defence. Neither hits. Stamina decrement? Only if Attack/Move/Manoeuvre declared. Full Guard = 0 Stamina depletion (only Defence declared). Per the "in a row" rule: no Stamina loss. **Both characters can maintain full guard indefinitely.** This is a stalemate.

**The stalemate resolves only through narrative pressure** (someone arrives, environmental change, one combatant has a timed objective). There is no mechanical escape from mutual full-guard stalemate.

**Finding B5-D03 (P2 — Mutual Full-Guard Stalemate):** Two combatants who both declare Full Guard can maintain it indefinitely (no Stamina loss, no damage). Stalemate is unresolvable through combat mechanics alone. This is acceptable if narrative pressure always exists, but a dedicated opponent can force a stalemate as an objective (e.g., delay a PC until reinforcements arrive). **No mechanical incentive to break stalemate exists.**

**Severity: P2.** Proposed fix: "A combatant who declares Full Guard for 2 or more consecutive rounds without any offensive action: Stamina −1 per full-guard round (tension fatigue). This prevents indefinite stalemate without penalising tactical use of one or two defensive rounds."

---

## SUMMARY TABLE

| Test | Mechanic | Mode | Finding | Severity | Fix Required |
|---|---|---|---|---|---|
| B5-M01-A | Pool Split | A | Full offence creates lethal exchange, not dominant strategy | ✓ | None |
| B5-M01-B | Pool Split | A | Full guard dominant defensively; resolved by Stamina | ✓ | None |
| B5-M01-D | Pool Split | A | Initiative advantage ~15pp hit probability | ✓ | None |
| B5-M02-A | Wounds | A | Wound × Thread cascade well-calibrated | ✓ | None |
| B5-M02-D | Wounds | A | Excess carryover math clean | ✓ | None |
| **B5-M03-A** | Stamina | A | "In a row" qualifier allows indefinite Stamina reset exploit | **P2** | Remove "in a row" |
| B5-M03-B | Stamina | A | Breather vs Catch Breath distinction correct | ✓ | P3 wording only |
| **B5-M03-C** | Stamina | A | Catch Breath timing not specified | **P3** | Add timing note |
| **B5-M04-C** | Reach | A | Projectile range closing procedure incomplete — no Ob defined | **P2** | Add Agility check Ob |
| B5-M05-A | Zone movement | A | Narrative zones: correct design | ✓ | None |
| **B5-M05-B** | Zone movement | A | Thread contact across zone transitions undefined | **P3** | Add clarifying note |
| **B5-M06-B** | Initiative | A | Late entrants to combat unspecified | **P3** | Add insertion rule |
| B5-M06-C | Initiative | A | Thread 2-round delay in fast combat: intentional | ✓ | None |
| **B5-M07-A** | Fibonacci | A | §1.9 and §8.1 group bonus tables contradict at 3+ attackers | **P1** | Remove §8.1 table; XRef §1.9 |
| B5-M07-B | Fibonacci | A | 8v1 overwhelming: intentional | ✓ | None |
| **B5-M07-C** | Fibonacci | A | Single ally nullifies all group bonuses (all-or-nothing) | **P2** | Reduce by one tier per ally |
| **B5-M08-B** | Beginner's Luck | A | "First mark" on unestablished History undefined | **P2** | Add provisional History tag rule |
| B5-M09-A | Momentum | A | Cap at 4 creates minor hoarding pressure; functional | P3 | Optional: raise to 6 |
| B5-M09-B | Momentum | A | Thread exclusion clean | ✓ | None |
| **B5-B01-A** | Pool+Wounds+Stamina | B | Low-Endurance crisis cascade by round 5: intentional | ✓ | None |
| **B5-B02-B** | Fibonacci+Pool Split | B | Defence splitting across 3+ attackers needs explicit guidance | **P2** | Add declaration note |
| **B5-D01** | Combat Escape | D | No Flee procedure defined | **P2** | Add Agility escape roll |
| **B5-D02** | Crunch | D | 4v4+Thread: ~30 steps/round; manageable with pre-calc | P2 | Enforce pre-calc note |
| **B5-D03** | Full Guard | D | Mutual full-guard stalemate: indefinite, no mechanical escape | **P2** | Stamina fatigue for consecutive full-guard |

**P1: 1 (M-07-A — duplicate group bonus tables)**
**P2: 7 (M-03-A, M-04-C, M-07-C, M-08-B, B-02-B, D-01, D-03)**
**P3: 3 (M-03-C, M-05-B, M-06-B)**

---

## COVERAGE MATRIX UPDATE

| Mechanic ID | Name | Isolation | Interaction | Scenario | Edge Cases | Status |
|---|---|---|---|---|---|---|
| M-01 | Pool Split | ✓ B5 | ✓ B5 | — | ✓ B5 | Issues found |
| M-02 | Wound/Gate System | ✓ B5 | ✓ B5 | — | ✓ B5 | Pass |
| M-03 | Stamina | ✓ B5 | ✓ B5 | — | ✓ B5 | Issues found |
| M-04 | Reach | ✓ B5 | — | — | ✓ B5 | Issues found |
| M-05 | Zone Movement | ✓ B5 | — | — | ✓ B5 | Pass (minor) |
| M-06 | Initiative/Priority | ✓ B5 | ✓ B5 | — | ✓ B5 | Issues found |
| M-07 | Fibonacci Group Bonus | ✓ B5 | ✓ B5 | — | ✓ B5 | Issues found |
| M-08 | Beginner's Luck | ✓ B5 | — | — | ✓ B5 | Issues found |
| M-09 | Momentum | ✓ B5 | — | — | ✓ B5 | Pass (minor) |

---

*Batch 5 complete — 2026-03-27*
