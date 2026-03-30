# THREADWEAVING × COMBAT: EXTREME STRESS TEST
## Objective: Break everything. Find exploits, death spirals, degenerate strategies, infinite loops, and dominant strategies.
## Model: Sonnet 4.6 | Date: 2026-03-29
## Rule state: PP-131 through PP-140, GP-01 through GP-06 applied

---

# I. STAT EXTREMES

## X-01: Minimum Viable Practitioner in Combat
**Profile:** TS 30, Focus 2, Spirit 1, Att 1, Agi 1, End 1, no History. TPS 3.
- Combat Pool: (1×2)+0+3 = 5D (minimum)
- HP: (1+6)×(2+1) = 21. Thresholds: 14/7/0.
- Leap pool: 1+0+3 = 4D, TN 7, Ob 2 (TS 30-49). P(≥2 on 4D at TN 7) = ~26%.
- **The Leap itself fails 74% of the time.** This practitioner cannot reliably enter contact.
- If Leap succeeds (26%): 1 operation round. Weaving Object Ob 1: pool 1+0+3 = 4D. P(≥1) = ~76%.
- **Combined probability of successful operation: 26% × 76% = ~20%.** One in five attempts produces an effect.
- **At 1W (-1D):** Leap pool drops to 3D. P(≥2 on 3D) = ~10%. Functionally inoperable.
- **FINDING X-01-F01 (P2):** TS 30-49 practitioners with Ob 2 Leap are gatekept hard. The Leap Ob 2 at TS 30-49 is the dominant limiter, not the operation itself. This is intentional — Stirring practitioners are barely functional. But it creates a cliff: at TS 50 (Ob 1), the same 4D pool has ~76% Leap success. **The TS 50 threshold is the real "you can thread in combat" gate.**

## X-02: Maximum Practitioner in Combat
**Profile:** TS 100, Focus 7, Spirit 7, Att 7, Agi 3, End 3, History 6 (all relevant). TPS 10.
- Combat Pool: (3×2)+6+3 = 15D
- HP: 27 (End 3, standard)
- Leap pool: 7+6+10 = 23D, TN 7, Ob 1. P(≥1) = ~99.97%. Auto-success.
- Weaving pool: 7+6+10 = 23D. Object Ob 1: auto. Structural Ob 5: P(≥5) = ~99.8%.
- Mending pool: 7+7+10 = 24D. Catastrophic Gap Ob 7: P(≥7) = ~98%.
- Lock/Dissolution pool: 7+6 = 13D (no TPS). Personal Lock Ob 5: P(≥5) = ~70%.
- **6 operation rounds per contact.** Can execute 6 sequential operations with Overweave penalty: Ob +0, +1, +2, +3, +4, +5.
- 6th operation at 23D Ob 6: P(≥6) = ~99%. Still near-auto.

**BREAK ATTEMPT — Max practitioner solo clearing:**
Round 1: Diagnosis. Round 2: Leap (auto). Rounds 3-8: 6 operations.
- Op 1: Pull on Enemy A (Personal, Ob 2). -2D to A. Auto.
- Op 2: Pull on Enemy B (Personal, Ob 2+1 overweave = Ob 3). -2D to B. ~99%.
- Op 3: Pull on Enemy C (Personal, Ob 2+2 = Ob 4). -2D to C. ~97%.
- Op 4: Pull on Enemy D (Personal, Ob 2+3 = Ob 5). -2D to D. ~96%.
- Op 5: Pull on Enemy E (Personal, Ob 2+4 = Ob 6). -2D to E. ~99%. Wait — Overweave is +1 per op after the first, not +1 per op total. Ops 2-6: +1, +2, +3, +4, +5. But these are ALL Pulling, same operation type. Does Overweave apply to same-type sequential operations?

**GAP: Overweave applies per operation, not per unique target.** §2.4: "Each operation after the first in the same contact window: +1 Ob (cumulative)." This means op 6 is at base Ob + 5. For Pulling at Ob 2: final op is Ob 7. 23D at Ob 7 = ~95%. **Still near-auto at max stats.**

**Result:** A TS 100 practitioner can Pull -2D on 6 separate enemies in one contact window, debuffing an entire squad. Combined with 15D Combat Pool: this character is a one-person army.

**FINDING X-02-F01 (P1): TS 100 practitioners are categorically dominant.** No mundane combat force can challenge them. The only counters are: (a) another high-TS practitioner, (b) overwhelming numbers (7+ enemies, exhausting the 6-op window), (c) Coherence costs accumulating over time (Personal Pulling at 0 Coherence cost means no Coherence limiter). **There is no combat Coherence cost for Personal-scale operations.** A TS 100 practitioner can Pull every round with zero strategic trade-off beyond action economy.

**FINDING X-02-F02 (P1): No Coherence cost for Personal Pulling creates an unlimited combat ability.** The practitioner can re-enter contact every (Focus+2) rounds and Pull again. Over a 20-round extended fight: 3 contact windows × 6 ops = 18 Pulls at 0 Coherence cost. The only limiter is RS (unchanged on Pull success) and Coherence drain from Partial/Failure results (~5% chance per op). **Personal Pulling is the dominant combat strategy for any practitioner above TS 50 with no meaningful resource cost.**

---

## X-03: Maximum Fighter vs Minimum Practitioner
**Profile:** P5-max (End 7, Agi 5, STR 6, History 6, HeavyBlunt Long, Heavy armour).
- Combat Pool: (5×2)+6+3 = 19D. HP: 65. Stamina: 7+6+1-2(Heavy) = 12.
- Damage on hit: excess + 6 + 5 = excess + 11. Crit: excess + 6 + 10 = excess + 16.
vs P3 (practitioner, 9D pool, 27 HP, Light armour).
- P5-max attacks: 12D offence at TN 7, P3 defends 9D at TN 8 (HeavyBlunt Def TN).
- P5 hits: ~4.8 successes. P3 blocks: ~3.6. Excess: ~1.2. Damage: 1.2 + 11 = 12.2. DR from Light armour vs HeavyBlunt: 0. **12 damage per hit.**
- P3 at 27 HP: drops to 15 in one hit. Crosses 18 threshold: 1W, -1D. **Second hit: P3 at 8D defence. P5 hits harder. ~13 damage. P3 drops to 2 HP. Crosses 9 threshold: 2W, -2D.** Third hit: incap.
- **P3 is killed in 3 rounds.** Vulnerability window for threading is 3 rounds. **The practitioner dies before completing their first operation.**

**FINDING X-03-F01 (P1): Optimized fighters kill mid-tier practitioners before they can thread.** This is not a bug — it's the intended incentive for protection. But it means a practitioner who enters combat alone against a competent fighter is dead. The 2-round setup (Diagnosis + Leap) is a death sentence against 19D opponents. **Practitioners MUST have bodyguards.** This is a setting-level design consequence: practitioners who go to war need retinues.

---

# II. EXPLOIT CHAINS

## X-04: Infinite Heal Loop
**Setup:** P4 (Focus 5, Spirit 6, End 3, 27 HP) in 1v1 against P1 (11D, 27 HP).
P4 threads every cycle: 2 rounds setup + 4 op rounds = 6 rounds. During 6 rounds, P1 deals ~6 damage/round (average against 7D defence) = ~36 damage. P4's 27 HP is exhausted in ~4.5 rounds. P4 dies before completing the cycle.

**But what if P4 heals?** Op 1-4: all Object Weaving heals on self. Restores 4 × 9 = 36 HP. Damage taken during 6 rounds: ~36. **Net HP change: ~0.** The practitioner breaks even.

**With allies protecting:** P3 engages P1 (diverting attacks). P4 takes 0 damage during the 6-round window. Heals 36 HP on allies. Contact drops. P4 is at full HP. Re-enter: 2 more setup rounds. Total cycle: 8 rounds. P4 heals 36 HP per 8 rounds indefinitely.

**FINDING X-04-F01 (P1): Dedicated healer with protection is an infinite sustain engine.** 36 HP/8 rounds = 4.5 HP/round healing throughput. Against typical damage of 6-10/round per attacker: one healer sustains one fighter against one attacker indefinitely. Against two attackers: healer falls behind (~12-20 damage/round vs 4.5 healing). **The break point is 2 attackers per healed ally.** Beyond that, healing cannot keep up.

**But — Overweave Ob stacking.** Ob 1, 2, 3, 4 for 4 heals. At 15D pool: Op 4 at Ob 4 = ~97%. Still easy. Op 5 at Ob 5 = ~96%. Op 6 at Ob 6 = ~87%. The Overweave penalty is a soft limiter but doesn't break the loop at high pools.

**DEGENERATE STRATEGY IDENTIFIED:** A party of 2 fighters + 1 healer-practitioner is near-unkillable in standard combat. The healer sustains both fighters; the fighters protect the healer. To break this formation, opponents need: (a) 3+ attackers per fighter (overwhelming healing throughput), (b) targeting the healer directly (requires getting past the bodyguards), (c) a hostile practitioner disrupting the healer (Pull on healer, Lock on healer, wound-disruption forcing contact drop).

**PROPOSED FIX:** Overweave on healing should stack faster. Current: +1 Ob per op. Proposed: +2 Ob per healing op specifically (narrative: each successive healing in the same contact window finds diminishing returns as the configuration becomes over-actualized from repeated stabilization). Op 1: Ob 1. Op 2: Ob 3. Op 3: Ob 5. Op 4: Ob 7. At 15D, Op 4 at Ob 7 = ~50%. This caps practical healing at 3 ops per window. **[EDITORIAL: confirm accelerated Overweave for healing, or accept infinite sustain as intended?]**

---

## X-05: Pull Stacking (Multiple Practitioners)
**Setup:** P3, P3b, P3c (three Attuned practitioners) vs P5 (19D pool).
Each Pulls on P5 (Personal, Ob 2). Three separate contact windows (sequential, not simultaneous — each practitioner Leaps independently).

Round 1-3: P3 Diagnoses, Leaps, Pulls P5. P5 at -2D = 17D.
Round 4-6: P3b same. P5 at -4D = 15D.
Round 7-9: P3c same. P5 at -6D = 13D.

**P5 at -6D** from three Pulls. 19→13D. Still functional but degraded.

**Can you reduce to 0D?** Need 10 Pulls (each -2D, from 19D to 0). At 3 ops per contact (Focus 4): need 4 contact windows across 4 practitioners. 4 × 3 rounds = 12 rounds of setup. In 12 rounds of combat, P5 has been fighting the whole time — probably killed several practitioners.

**But: is there a minimum pool?** Combat Pool minimum is 5 (from formula). Pull reducing below 5? No rule prevents it. At 0D, the fighter literally cannot roll dice. They can't attack or defend. Instant hit on every subsequent attack.

**FINDING X-05-F01 (P1): Pull stacking has no floor.** Multiple practitioners can reduce any fighter to 0D pool, making them helpless. The limiter is time and practitioner count — each Pull requires a full contact cycle (2-3 rounds). Against a competent fighter, practitioners die faster than they can stack Pulls. **But against a target who cannot retaliate (e.g., Locked target, or target engaged by allies):** Pull stacking is unlimited. Three practitioners can reduce any target to 0D in ~9-12 rounds if the target is pinned.

**PROPOSED FIX:** Pool reduction from Pulling cannot reduce any pool below half its base value (round up). P5 at 19D: floor = 10D. Three Pulls reduce to max -9D → 10D. This prevents total helplessness while preserving Pull's tactical value.

---

## X-06: Lock + Dissolution Combo
**Setup:** P4 Locks P1 (Personal Lock, Ob 5). P4b then Dissolves the Locked P1 (Personal Dissolution, Ob 5).

**Problem:** Lock freezes P1's configuration. P1 "cannot be Wounded (configuration cannot cross damage threshold)." Does this prevent Dissolution? Lock makes the target "unable to become." Dissolution makes the target "unable to be." These are contradictory ontological states.

**Philosophical analysis (P-06):** Lock arrests the intelligible face. Dissolution tears the intelligible face away. You cannot tear away something that is frozen — the Lock is actively holding it in place. To Dissolve a Locked target, you must first reverse the Lock (Pull, Ob based on original practitioner's TS).

**FINDING X-06-F01 (P1): Lock prevents Dissolution.** A Locked configuration cannot be Dissolved — the Lock must be reversed first. This creates a defensive use for Lock: Locking an ally prevents enemy Dissolution. But the RS cost (-1/round) makes this a desperate trade-off.

**Alternative combo — Lock then abandon:** Lock P1, kill the practitioner (or let contact window expire without releasing), Lock persists permanently. P1 is frozen forever unless another practitioner Pulls the Lock off. RS drains every scene. The Locked person is effectively removed from the game AND damages the world continuously.

**FINDING X-06-F02 (P1): Permanent Personal Lock is a war crime mechanic.** Lock an enemy, die (or have your contact window end with bonus successes extending the Lock), and the target is permanently frozen, draining RS indefinitely. The only counter is another practitioner spending an operation to Pull the Lock (Ob = original TS÷10 - 2). If the Locker was TS 70: Ob 5 to reverse. If TS 100: Ob 8. A TS 100 Lock is nearly irreversible except by another TS 100 practitioner. **This is an existential weapon — politically and mechanically devastating.** Factions should fear practitioners who can Lock living beings. The Church's anti-Thread stance is vindicated.

---

## X-07: Fibonacci + Pull Alpha Strike
**Setup:** 3 fighters + 1 practitioner vs 1 elite target (P5-max, 19D, 65 HP, Heavy armour).
Round 1-2: Practitioner Diagnoses + Leaps (allies engage P5-max).
Round 3: Practitioner Pulls P5-max's armour (Object, Ob 1). Heavy armour DR drops by 1 across all types.
Round 3 (simultaneous): Practitioner Pulls P5-max's personal configuration (Op 2, Ob 2+1 overweave = Ob 3). P5-max at -2D = 17D.

Round 4+: 3 fighters attack. Fibonacci +2D each. Using HeavyBlunt (targeting reduced armour):
- Each fighter: 8D+2D(Fib) = 10D offence at TN 7. P5-max: 17D split 3 ways = ~6D defence each at TN 8.
- Fighter hits: ~4.0 successes. P5-max blocks: ~2.4. Excess: ~1.6.
- Damage: 1.6 + 4(STR) + 5(HB mod) = 10.6 per hit. DR: Heavy vs HeavyBlunt = 1 - 1(Pull) = 0. **Full damage.**
- Three hits: 31.8 damage. P5-max at 65 HP → 33.2 HP. Crosses 52 threshold: 1W, -1D.
- **Round 5:** P5-max at 16D (17-1W). Same attack pattern. ~31 damage. 33→2 HP. Crosses 39 AND 26 AND 13 thresholds: 4W, -4D.
- **Round 6:** P5-max at 12D. One more round finishes.

**Total: 3 rounds of combat (after 2 setup rounds) to kill the toughest possible fighter.** The Pull + Fibonacci + correct weapon type combo is devastating.

**Without the Pull:** Heavy armour vs HeavyBlunt DR = 1. Damage per hit: 10.6 - 1 = 9.6. Three hits: 28.8/round. P5-max at 65: takes ~3 rounds to first wound. Total kill time: ~5-6 rounds of combat. The Pull saved ~2 rounds.

**FINDING X-07-F01 (P2):** Pull + Fibonacci + correct weapon type is the optimal alpha strike but only saves ~2 rounds over pure martial approaches. The Pull's value is marginal when allies are already using the correct weapon counter. **Pull is most valuable when allies DON'T have the right weapon — e.g., all LightCut fighters vs Heavy armour (DR 6→5 from Pull, still near-useless).** In that case, Pulling the armour barely helps. **Pulling the person (-2D) is always better than Pulling armour when allies lack weapon-type advantage.** This confirms C-01's finding: Personal Pull dominates.

---

# III. ECONOMY BREAKS

## X-08: RS Death Spiral via Personal Locks
**Setup:** 3 practitioners simultaneously Lock 3 living beings. RS -3/round.
Combat lasts 5 rounds: RS -15. Over a 10-round extended scene: RS -30.

**Starting at RS 60 (campaign default):** 10 rounds of 3 active Locks = RS 30. Now in Fragile band. Spontaneous Shifting Objects form. Thread ops +1 Ob in affected territories.

**One extended battle with Lock abuse can crash RS from Strained to Fragile.**

**Worst case:** 5 practitioners Lock 5 beings. RS -5/round. 10 rounds: RS -50. From RS 60 to RS 10. **Critical band.** Spontaneous Gaps on 1-4. All Thread ops +1 Ob worldwide. Faction Stability checks every season.

**FINDING X-08-F01 (P1): Mass Locking is an RS weapon of mass destruction.** A coordinated practitioner force can crash RS by 30-50 points in a single extended scene. This is an extinction-level event. **The balancing factors:** (a) Lock pool is small (Spirit+History, ~7-13D) at Ob 5 minimum (~15-70% success per Lock), (b) each practitioner needs 3 rounds of setup, (c) Locking 5 people requires 5 practitioners with TS 50+ — a rare concentration. **But if a faction (Niflhel?) assembles 5 practitioners and orchestrates a Lock assault during a siege, they can end the world in one scene.**

**PROPOSED FIX:** RS drain from Personal Lock should cap at -1 per round regardless of concurrent Locks (the substrate can only strain so fast from a given scene). Multiple Locks in the same zone don't stack RS drain — they produce the same -1/round. Alternatively: Lock RS drain scales with (Lock count)^0.5 instead of linearly. 1 Lock: -1/round. 4 Locks: -2/round. 9 Locks: -3/round. This makes mass Locking less catastrophic while preserving single-Lock consequences.

---

## X-09: Coherence Drain Rate — Campaign Stress Test
**Practitioner profile:** TS 55, starts Coherence 10. Normal campaign: 2 combats per season, 2 Relational ops per season (faction work).
- Per combat: 2 Personal Pulls (0 Coherence each). 1 Personal Weaving heal (0 Coherence). Total combat Coherence: 0.
- Per season (non-combat): 2 Relational ops (Coherence -1 each) = -2.
- **Annual drain: -8 Coherence (4 seasons × -2/season).**
- **Reaches Coherence 0 in ~5 seasons (1.25 years).** At 2 sessions/season, that's ~10 sessions.

**With Object/Personal restriction (no Relational ops):** 0 Coherence drain indefinitely. The practitioner operates at full combat effectiveness forever with zero strategic cost.

**FINDING X-09-F01 (P1): Object/Personal operations have zero Coherence cost, making them strategically free.** A practitioner who restricts to Object/Personal scale — which covers ALL combat operations (heal wounds, Pull enemies, Weave weapons, Diagnose) — never degrades. Coherence is only a concern for practitioners who perform Relational+ operations. **In a campaign focused on personal combat, Coherence is irrelevant.** The Einhir trajectory (small-scale = sustainable, large-scale = destructive) is correctly modelled for Coherence, but the combat system accidentally makes small-scale ops infinitely repeatable with no cost.

**Is this a problem?** Maybe not — the philosophical framing says Object/Personal operations are safe and sustainable. The cost is action economy (2-3 rounds per use). The question is whether combat should have ANY strategic Thread cost. Currently: zero.

---

## X-10: Wound Cascade — One-Shot Analysis
**Can a single blow incapacitate?**

Target: End 1 (21 HP). Attacker: STR 6, HeavyBlunt (+5), crit (excess ≥ 3, modifier doubled).
- Damage = excess + 6 + 10 = excess + 16.
- At excess 5: 21 damage. **Exactly lethal.** 21→0 HP. Incapacitated in one blow.
- At excess 3 (minimum crit): 19 damage. 21→2 HP. 2W (-2D). One more hit finishes.

Target: End 3 (27 HP). Same attacker.
- At excess 11: 27 damage. Lethal. But excess 11 requires 11+ net successes — effectively impossible.
- At excess 5 (crit): 21 damage. 27→6 HP. 2W (-2D). Devastating but not lethal.
- **End 3 cannot be one-shot killed by any normal attack.** Requires 27+ damage.

Target: End 5 (44 HP). Cannot be one-shot under any circumstances. 44 damage requires excess ~28.

**FINDING X-10-F01 (P2):** One-shot kills are possible only against End 1 characters with maximum attacker stats and a crit. End 2+ characters are safe from one-shot. **Multi-wound single blows are common** at End 1-3 (9 HP segments are easily crossed by heavy weapon hits). At End 5+ (11 HP segments), single-wound blows are normal and multi-wound is rare. **The wound system scales correctly — low End characters are fragile, high End characters are durable.** No balance issue.

---

## X-11: Wound System — Minimum Damage Scenario
**Can fights stalemate?**

Both fighters: LightCut Short, Light armour, End 3 (27 HP), Agi 2, STR 2, Hist 2.
- Pool: (2×2)+2+3 = 9D. Split 5/4 or 6/3.
- Offence 5D at TN 5 = ~3.0 hits. Defence 4D at TN 6 = ~2.4 blocks. Excess ~0.6.
- Damage: 0.6 + 2(STR) + 1.5(LCut) = 4.1. DR from Light vs LightCut: 2. **Net damage: 2.1 per round.**
- 27 HP / 2.1 = ~13 rounds to incapacitate.
- But Stamina: 3+2+1 = 6. Depletes 1/round. At round 6: OOB. Half pool (5D), Defence only, opponent +2D.
- OOB round: opponent at 7D+2D = 9D offence vs 5D defence. Hits ~3.6 excess. Damage 3.6+2+1.5-2 = 5.1.
- After OOB: Stamina restores. Resume.
- **OOB cycles every 6 rounds. Each OOB round deals ~5 damage. Total fight: ~13-15 rounds with OOB spikes.**

**FINDING X-11-F01 (P3):** Low-stat mirror matches are long but not indefinite. Stamina OOB cycles create damage spikes that prevent true stalemates. No stalemate possible.

**Edge case — mutual Full Guard:** Both choose Full Guard every round. No one attacks. Infinite stalemate. But this is a voluntary choice, not a mechanical trap. Either player can break the stalemate by attacking. No rule issue.

---

# IV. MULTI-SYSTEM COLLISIONS

## X-12: Involuntary Leap Chain Reaction
**Setup:** P8a (TS 92) and P8b (TS 95) fighting side by side. P3 performs a Thread operation nearby.
- P8a Focus check: 5D TN 7 Ob 1 = ~83% resist. 17% involuntary Leap.
- P8b Focus check: 5D TN 7 Ob 1 = ~83% resist. 17% involuntary Leap.
- P(at least one involuntary Leap) = 1 - (0.83 × 0.83) = ~31%.
- **If P8a involuntary Leaps:** Does this count as a "nearby Thread operation" triggering P8b's check again? The Leap itself is a Thread-adjacent event (rendering suspends) but is NOT an operation (no intentionality, no target).

**Patch PP-141:** Involuntary Leap is NOT a Thread operation. It does not trigger involuntary Leap checks in other Resonant practitioners. Only actual operations (Weaving, Pulling, etc.) trigger the check. Without this patch: involuntary Leap chain reactions could cascade through all Resonant practitioners in a scene, each triggering the next, incapacitating the entire group.

**FINDING X-12-F01 (P1):** Without PP-141, two Resonant practitioners in the same scene create a 31% chance of cascading involuntary Leaps from a single Thread operation. Three Resonant practitioners: 42%. This would be catastrophic and unintended. **PP-141 is essential.**

---

## X-13: Gap + Lock + Dissolution in Same Scene
**Setup:** Round 1-3: P4a Dissolves an Object. Failure. Full Gap opens. Monstrous Incursion. RS -8.
Round 4-6: P4b Locks a Monstrous Entity (to neutralize it). Personal Lock Ob 5. RS -1/round while Locked.
Round 7-9: P4c attempts to Mend the Gap. Mending Ob 5. But zone has +1 Ob from active Lock (E-06 ruling: "+1 Ob to all Thread operations in the same zone"). Mending now Ob 6.
- P4c Mending pool: 17D at Ob 6. P(≥6) = ~91%. Viable but degraded.
- RS state: started at 60. Dissolution failure: -8 = 52. Lock running 3 rounds: -3 = 49. If Mending succeeds: +1 = 50. Net: RS 50.

**But the Monstrous Entity is Locked.** Its configuration is frozen. If the Lock expires (contact window ends), the entity resumes attacking. If the Lock persists: RS drains. The party must choose: release the entity (resume combat) or maintain the Lock (drain RS).

**Finding X-13-F01 (P2):** The Gap + Lock + Mend interaction creates genuine tactical dilemmas with no clean solution. Every option has costs. This is good design — complex Thread situations should not have easy answers. The +1 Ob zone penalty from Lock interfering with Mending is a subtle but meaningful interaction: Locking a problem makes other Thread work harder. **No rule issue; working as designed.**

---

## X-14: Coherence 0 Mid-Contact Window
**Setup:** P3 at Coherence 1 performs a Relational Weaving mid-combat. Coherence drops to 0. Rendering Crisis fires.

**PP-139 says:** Rendering Crisis in combat = incapacitation. But P3 is in contact (rendering suspended). Can Rendering Crisis fire while rendering is already suspended?

**Philosophical analysis:** Rendering Crisis occurs when the practitioner "returns to rendering" and their rendering fails. During contact, rendering is suspended — it cannot fail because it's not active. The Crisis fires on the return.

**Patch PP-142:** Coherence 0 reached during contact: no immediate effect. When contact drops (natural end, wound disruption, or forced), the practitioner returns to rendering and Rendering Crisis fires immediately. Remaining operations in the contact window proceed normally — the practitioner's rendering is already suspended and the Coherence loss doesn't affect the current suspension. The crisis is deferred to the moment rendering reasserts.

**Implication:** A practitioner at Coherence 1 can deliberately perform one more Relational operation knowing it will trigger Rendering Crisis on return. They sacrifice themselves for the final operation. This is a heroic last-act mechanic — the practitioner pushes past their limit for one last Thread intervention.

**FINDING X-14-F01 (P2):** PP-142 creates an intentional "one last act" mechanic. The practitioner can thread past Coherence 0 but collapses on return. No exploit — the collapse is guaranteed. The player makes a deliberate sacrifice. **This is thematically powerful and mechanically clean.**

---

# V. DEGENERATE STRATEGY ANALYSIS

## X-15: The Pull-Bot
**Strategy:** A TS 55+ practitioner with Focus 4+ dedicates entirely to Personal Pulling in combat. Every contact window: Pull 3 enemies at -2D each. 0 Coherence cost. 0 RS cost on success. Re-enter contact every 6 rounds.

**Why this dominates:** 
- More effective than attacking (removes 6D total from enemy forces per window vs ~6 damage from a Strike)
- Zero strategic cost (no Coherence, no RS)
- Harder to counter than a fighter (Defence-only is safer than attacking; no Stamina depletion during threading)
- Scales with targets (more enemies = more value from Pull)

**Counters:**
1. Target the Pull-Bot directly (requires getting past bodyguards)
2. Kill them before they complete setup (requires 19+ damage in 2 rounds)
3. Hostile practitioner Locks the Pull-Bot
4. Overwhelming numbers (if 6+ enemies, Pull-Bot can't debuff them all)

**FINDING X-15-F01 (P1): Personal Pull is the dominant combat strategy.** It's strictly better than any other Thread operation in combat contexts: lower Ob than FR ops, zero Coherence cost (unlike Relational+), temporary but scene-duration effect (adequate for combat), -2D per target (significant). **Recommendations to balance:**

*Option A:* Personal Pull costs Coherence -1 (treat as Relational-equivalent in combat because you're affecting another person's configuration). This makes it expensive over a campaign.

*Option B:* Personal Pull duration in combat = 3 rounds, not end of scene. Requires re-application. Still useful but not set-and-forget.

*Option C:* Personal Pull -1D (not -2D). Half as effective. Still useful but not dominant.

*Option D:* Accept it. The Pull-Bot strategy requires 2-3 rounds of vulnerability, bodyguard protection, and a dedicated character slot. The opportunity cost is real — that practitioner isn't doing anything else.

**[EDITORIAL: Which balancing option, if any? Or accept Pull-Bot as intended?]**

---

## X-16: The Immortal Healer
**Strategy:** TS 55+ practitioner with Focus 5, dedicated to Object Weaving heals. Stays behind allies. 4 heals per window at Ob 1/2/3/4. Restores 36 HP across allies per window. Re-enter every 7 rounds.

**Throughput:** 36 HP / 7 rounds = ~5.1 HP/round. Against typical 6-10 damage/round per enemy: sustains 1 ally against 1 enemy indefinitely. With Overweave acceleration fix (X-04 proposal: +2 Ob per heal): throughput drops to 27 HP / 7 rounds = ~3.9 HP/round. Still strong.

**Counter to the counter:** If Overweave is +2 per heal, the healer can alternate: Op 1 heal (Ob 1), Op 2 Pull enemy (Ob 2+1 = Ob 3), Op 3 heal (Ob 1+2 = Ob 3?). Wait — does Overweave track per operation TYPE or per operation total?

**GAP: Overweave counting.** §2.4: "Each operation after the first in the same contact window: +1 Ob (cumulative)." This is per operation total, not per type. So: Op 1 (anything) Ob +0. Op 2 Ob +1. Op 3 Ob +2. Regardless of type. Alternating heal/Pull doesn't bypass Overweave.

**FINDING X-16-F01 (P2):** Overweave is per-operation, not per-type. No bypass available. The healer's throughput is correctly limited by Overweave stacking. With standard +1 Ob: 4 heals at Ob 1/2/3/4 = 36 HP. With proposed +2 Ob healing acceleration: 3 heals at Ob 1/3/5 = 27 HP. Either way, a single healer sustains a party of 2-3 fighters against moderate opposition. **The Immortal Healer is strong but not broken — it requires a dedicated character slot and 2 bodyguards to protect the healer during setup.**

---

## X-17: The Dissolution Assassin
**Strategy:** TS 70+ practitioner with high Spirit. Enters combat. Dissolves the enemy leader (Personal, Ob 5). On success: instant kill. On Partial: target becomes Shifting Object (delayed kill). On Failure: self-incapacitation + catastrophic Gap.

**At Spirit 7 + History 6 = 13D, Ob 5: ~70% success.**

**This is a 70% chance of instantly killing anyone.** No save. No resistance. No armour. TS 70 is achievable (high investment, but reachable by late-campaign practitioners).

**FINDING X-17-F01 (P1): Personal Dissolution is a 70% assassination ability at optimized stats.** The cost (Coherence -2, RS -5 to -8, possible self-incapacitation on failure) is high but the effect is binary: target dies or you die. This is a suicide mission mechanic — the assassin accepts ~30% self-destruction for ~70% target-kill. **Against a faction leader with 65 HP and Heavy armour, conventional combat takes 10+ rounds. Dissolution takes 3 rounds (setup + op) with 70% success.** Dissolution is strictly superior to conventional combat for assassination.

**Counters:**
1. Bodyguards who identify the practitioner during Diagnosis round and kill them before Leap
2. Allied practitioner who Locks the assassination target (Lock prevents Dissolution per X-06)
3. Allied practitioner who Pulls or Locks the assassin during setup
4. High-TS observer who detects the Diagnosis and warns the target

**[EDITORIAL: Should Personal Dissolution require a resistance roll (target Spirit check)? This would reduce the assassination rate and give the target agency. Proposed: Target rolls Spirit TN 7 Ob 1 to resist. Success: Dissolution downgraded to Partial (Shifting Object, not instant kill). Failure: Dissolution proceeds as rolled.]**

---

# VI. E-01 THROUGH E-03, E-10 (NOW UNBLOCKED)

## E-01: Weaving Stat Output on a Weapon
**GP-03 applied.** P3 Weaves on ally's LightCut weapon (Object, Ob 1). Pool: 12D, Ob 1. Auto.
**Effect:** +1 damage modifier. LightCut goes from +1-2 to +2-3. On a typical hit (excess 1, STR 3): damage goes from 5-6 to 6-7. +1 damage per hit.
**Finding E-01-F01 (P3):** Weapon Weaving is minor — +1 damage per hit for 3 rounds of setup. Over 5 hits: +5 total damage. Compared to Personal Pull (-2D to enemy, preventing ~2 extra damage per round): **Pull is more efficient than weapon Weaving in all scenarios.** Weapon Weaving is only justified when the practitioner has spare operations in a contact window after Pulling.

## E-02: Pulling Stat Output on Armour
**GP-03 applied.** P3 Pulls P5's Heavy armour (Object, Ob 1). Effect: -1 DR all types.
Heavy armour: 6/5/3/1 → 5/4/2/0.
**Finding E-02-F01 (P3):** Armour Pulling is niche. Only matters when allies use weapon types that are currently blocked by DR. HeavyBlunt vs Heavy (DR 1→0): marginal. LightCut vs Heavy (DR 6→5): still useless. **Multiple Pulls stack? If 3 Pulls on same armour: DR -3 all types. Heavy goes to 3/2/0/0. Now LightCut vs Heavy is DR 3 — still painful but not impossible.** Multi-Pull armour stripping requires 3+ operations on the same target's armour. Only viable for a single practitioner with Focus 5+ and spare ops.

## E-03: Weaving Stat Output on a Person (Healing)
**GP-03 applied.** P3 Weaves on P7 (Personal, Ob 2). Pool: 12D, Ob 2. ~97%.
**Effect:** Restore (End+6) = 9 HP. One wound segment healed.
**New wound system interaction:** Healing restores HP but wounds are "not healed" — the track doesn't reset. Does +9 HP move the target above a wound threshold? If P7 at 15 HP (1W, -1D): +9 HP = 24 HP. 24 > 18 (first threshold). Wound removed. Pool penalty removed.
**But the user said "ie wound no longer heals."** Does this mean Weaving can't restore HP? Or just that wounds don't reset automatically?

**Interpretation:** "wound no longer heals" means the HP track doesn't reset on its own — no automatic healing. Weaving is supernatural healing — it CAN restore HP and remove wound penalties. The "no healing" applies to mundane recovery within combat. **Weaving is the only way to heal during combat.**

**FINDING E-03-F01 (P2):** Under the new wound system, Weaving healing is MORE valuable than before (it's the only healing available in combat). This reinforces the healer-practitioner's role as essential to sustained combat. **No rule issue — this is a feature, not a bug.**

## E-10: Weaving a Weapon During Active Use
P2 Weaves own weapon (Object, Ob 1) while in combat. Must Leap (Defence-only) while weapon is in hand.
**Can you Weave an object you're holding?** Thread operations target the object's configuration, not its physical form. The practitioner Diagnoses the weapon's thread, Leaps, and their configuration interacts with the weapon's thread during contact. Physical possession is irrelevant — the interaction is at the Thread level.
**Patch:** No requirement to put the weapon down. Weaving targets the configuration, not the physical object. The weapon is enhanced while held.
**Finding E-10-F01 (P3):** No issue. Weapon Weaving while held is clean. The +1 damage modifier applies from the next round the weapon is used.

---

# VII. ULTIMATE STRESS SCENARIO

## X-18: The Nightmare — Everything At Once
**Setup:** 3v3 combat in a zone with an active Standard Gap. RS 45 (Fragile). One side has a TS 92 Resonant practitioner (P8). Other side has a TS 70 Sensitive practitioner (P4) and a threadcut being (P6).

**Round 1:** P4 Diagnoses P8 (Defence-only). P6 Diagnoses the Gap (Defence-only, no Leap needed — threadcut, but GP-06 says Defence-only during ops). Three fighters engage.

**Round 2:** P4 Leaps (auto). P6 begins Mending the Gap (Att 5 + Focus 6 + TPS 8 = 19D, Ob 5, +1 Ob from nearby Lock? No Lock active. Ob 5. P(≥5) = ~98%).
P8's involuntary Leap check triggered by P4's Leap? No — Leap is not an operation (PP-141). Triggered by P6's Mending? Yes — Mending is an operation. P8 Focus 5 at TN 7 Ob 1 = ~83% resist. 17% involuntary Leap.

**If P8 involuntary Leaps (17%):** P8 is combat-inert for 5 rounds. Their side loses their best fighter. P4's side has massive advantage.

**If P8 resists (83%):** P8 continues fighting. P4 attempts Personal Pull on P8 (Ob 2). P8 at -2D. P8's combat effectiveness drops.

**Round 3:** P6 completes Mending. Gap closes. RS +1 = 46. Co-movement fires: Coherence -1 to P6 (wait — threadcut beings don't track Coherence? They track Rendering Strain). **GAP: Do threadcut beings take Coherence costs from operations?** Threadcut beings don't have organic rendering — they self-render. Coherence measures organic rendering stability. Threadcut beings should track Rendering Strain instead.

**Patch PP-143:** Threadcut beings do not track Coherence. All Coherence costs from operations are replaced by +1 Rendering Strain per operation (already defined in §6.3). This means Mending costs P6 +1 RS (standard external op cost), not Coherence -1.

**Round 3 continued:** P4's Pull on P8 resolves. P8 at -2D. P8's Combat Pool drops from 9D to 7D. P8 is now a below-average fighter AND has 17% involuntary Leap risk from any further Thread operations near them.

**Round 4+:** P4 has 2 more operation rounds (Focus 4). Pulls two more targets (Ob 3, 4 with Overweave). Debuffs the entire enemy team. P6's contact drops (Focus 6 = Round 7 natural end). P6 re-enters combat normally.

**The nightmare resolves in P4+P6's favour.** They closed the Gap, debuffed 3 enemies, and their involuntary-Leap-risk target (P8) is effectively a liability to their own side.

**FINDING X-18-F01 (P1): The Resonant practitioner is a liability in combined arms.** Their involuntary Leap risk makes them dangerous to deploy near allied practitioners AND vulnerable to enemy practitioner operations. P8 is a powerful solo combatant but a team handicap. **This creates a genuine character arc: TS 90+ characters are too powerful to operate near others. Their sensitivity is both their strength and their isolation.** Philosophically correct per P-08 (no consciousness renders the whole).

---

# MASTER FINDINGS TABLE

| ID | Severity | Finding | Proposed Fix |
|---|---|---|---|
| X-01-F01 | P2 | TS 50 is the real combat-threading gate (Ob 2→1 cliff) | None — intentional |
| X-02-F01 | P1 | TS 100 practitioners are categorically dominant | Accept or cap TPS contribution |
| X-02-F02 | P1 | Personal Pull at 0 Coherence cost = unlimited combat ability | See X-15 options |
| X-03-F01 | P1 | Optimized fighters kill mid-tier practitioners in 3 rounds | None — intentional (requires bodyguards) |
| X-04-F01 | P1 | Heal loop: 36 HP/8 rounds with protection = infinite sustain | Accelerate Overweave for healing (+2 Ob) |
| X-05-F01 | P1 | Pull stacking has no floor; can reduce to 0D | Floor at half base pool |
| X-06-F01 | P1 | Lock prevents Dissolution (ontological contradiction) | None — correct |
| X-06-F02 | P1 | Permanent Personal Lock = existential weapon, RS drain forever | None — intended (extremely costly) |
| X-07-F01 | P2 | Pull+Fibonacci+weapon type is optimal but only saves ~2 rounds | None |
| X-08-F01 | P1 | Mass Lock assault crashes RS by 30-50 in one scene | Cap Lock RS drain: no stacking |
| X-09-F01 | P1 | Object/Personal ops have 0 Coherence cost forever | See X-15 options |
| X-10-F01 | P2 | One-shot kills only at End 1 vs max attacker crits | None — correct |
| X-11-F01 | P3 | Low-stat mirrors take 13-15 rounds, no stalemate | None |
| X-12-F01 | P1 | Involuntary Leap chains cascade without PP-141 | PP-141 essential |
| X-13-F01 | P2 | Gap+Lock+Mend creates genuine tactical dilemmas | None — good design |
| X-14-F01 | P2 | Coherence 0 during contact = deferred Crisis on return | PP-142 |
| X-15-F01 | P1 | Personal Pull is the dominant combat strategy | EDITORIAL: A/B/C/D options |
| X-16-F01 | P2 | Healer throughput capped by Overweave correctly | None if Overweave fix applied |
| X-17-F01 | P1 | Personal Dissolution = 70% assassination at optimized stats | EDITORIAL: resistance roll? |
| X-18-F01 | P1 | Resonant practitioners are team liabilities | None — philosophically correct |

**New patches this batch: PP-141 (involuntary Leap not an operation), PP-142 (Coherence 0 deferred during contact), PP-143 (threadcut beings: RS not Coherence).**

---

# CRITICAL EDITORIAL DECISIONS NEEDED

1. **Personal Pull balance (X-15):** 0 Coherence cost, -2D, scene duration. Options A-D listed. This is the single most important balance decision from this simulation batch.

2. **Personal Dissolution lethality (X-17):** Instant incapacitation or resistance roll? 70% kill rate at optimized stats with no counter except practitioner bodyguards.

3. **Heal loop mitigation (X-04):** Accelerated Overweave (+2 Ob per heal) or accept infinite sustain as a feature?

4. **Pull stacking floor (X-05):** Cap at half base pool or allow reduction to 0D?

5. **Mass Lock RS drain (X-08):** Cap concurrent Lock RS drain or allow stacking?
