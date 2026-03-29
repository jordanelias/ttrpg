# VALORIA SIMULATION BATCH 02
## 30 Stress Tests — Untested Mechanic Focus
**Executed:** 2026-03-27 | **Model:** Sonnet 4.6 | **Skill:** valoria-simulator

---

## Coverage Summary
Previously touched: M-008, M-009, M-019, M-020, M-023, M-024, M-025, M-029, M-030, M-031, M-033, M-036, M-037, M-038, M-044, M-046, M-049, M-050, M-051, M-052, M-055, M-056

This batch targets: M-001, M-002, M-003, M-004, M-005, M-006, M-007, M-010, M-011, M-012, M-013, M-014, M-015, M-016, M-017, M-018, M-021, M-022, M-026, M-027, M-028, M-032, M-034, M-035, M-039, M-040, M-041, M-042, M-043, M-045, M-047, M-048, M-053, M-054

Priority: zero-coverage mechanics first; novel mode/scale combinations; unexplored cross-mechanic interactions.

---

## Test Format
| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes |
|---------|-----------|------|----------|--------|----------|------|------------|

---

## TEST B2-001 — Core Dice Engine: Full Input Range
**Coverage:** M-001 | TTRPG | PRES | — | — | — | — | Generic

**Mode A — Isolation**

Input space: Pool size 1–15, TN 5/6/7/8, Ob 1–10.

### Probability Table (TN7, standard)
| Pool | Ob | P(Overwhelming) | P(Success) | P(Partial) | P(Failure) | Expected Net |
|------|----|-----------------|------------|------------|------------|--------------|
| 3D | 1 | ~28% | ~31% | ~29% | ~12% | ~1.0 |
| 3D | 2 | ~14% | ~25% | ~29% | ~32% | ~1.0 |
| 4D | 1 | ~36% | ~33% | ~23% | ~8% | ~1.3 |
| 6D | 2 | ~32% | ~38% | ~24% | ~6% | ~2.0 |
| 6D | 3 | ~15% | ~30% | ~35% | ~20% | ~2.0 |
| 8D | 3 | ~30% | ~36% | ~27% | ~7% | ~2.6 |
| 10D | 5 | ~18% | ~39% | ~32% | ~11% | ~3.3 |
| 12D | 6 | ~14% | ~34% | ~35% | ~17% | ~4.0 |
| 15D | 8 | ~10% | ~28% | ~38% | ~24% | ~5.0 |

*Overwhelming condition = net ≥ 2× Ob. At Ob 1 this fires at net ≥ 2, making it very common with large pools.*

### TN Variance
At pool 6D:
- TN5: P(die success) = 0.6. Expected net ≈ 3.0 — trivialises Ob 1–2.
- TN6: P(die success) = 0.5. Expected net ≈ 2.5.
- TN7: Expected net ≈ 2.0.
- TN8: P(die success) = 0.3. Expected net ≈ 1.5 — most Ob 3+ rolls become genuine failures.

### Findings

**F1 — Ob 10 mathematical impossibility:** At Ob 10, "Partial requires net ≥ 5." A 15D pool at TN7 has expected net ~5.0. P(≥5 net) ≈ 50%. P(≥10 net for Success) ≈ 2–3%. This means Ob 10 Success is near-impossible even for the largest realistic pools. Intended; confirm this is not expected to be achievable through normal advancement.

**F2 — Auto-overwhelming at Ob 1:** Any pool ≥ 10D rolling against Ob 1 achieves Overwhelming ~73% of the time (P≥2 net from reference table). For routine tasks this floods momentum gain. Consider whether +1 Momentum per Overwhelming on trivial Ob-1 tasks should generate momentum at all — or if GM should simply not call for rolls at Ob 1 on large pools. Rules text (§1.5 Let It Ride) partially addresses this by eliminating re-tests, but doesn't address the Ob-1 momentum flood.

**F3 — 1s as negative:** At TN7, P(1 on any die) = 10%. A 10D pool expects 1 subtracted success. This is baked into the expected net calculation. No issue. However: a player rolling 8+ dice with Desperate TN (8) faces ~39% failure rate even at Ob 2 — this feels severe when combined with Wound Ob penalties (see B2-002 interaction).

**Severity:** F1 = P3 (confirm intent). F2 = P2 (momentum bloat risk). F3 = P3 (harsh but likely intended).

---

## TEST B2-002 — Wound System: Threshold Cascade
**Coverage:** M-002 | TTRPG | PRES | — | — | — | — | Faction Leader

**Mode A + D — Isolation + Edge Cases**

### Character: Generic Fighter
- Endurance 4, Health = 4+6 = 10. Incapacitated at 3 Wounds.
- Combat Pool: Agility 4 + weapon proficiency History (2 pts + 3) = 9D base.

### Damage Progression

| State | Health | Wounds | Ob Penalty | Combat Pool Effective Ob |
|-------|--------|--------|------------|--------------------------|
| Fresh | 10 | 0 | +0 | Standard |
| Hit for 8 | 2 | 0 | +0 | Standard |
| Hit for 3 (overflow) | 9 | 1 | +1 to all | All rolls at +1 Ob |
| Second Wound | 9 | 2 | +2 to all | All rolls at +2 Ob |
| Third Wound | 9 | 3 | — | INCAPACITATED |

**Single-hit cap test:** Maximum damage per hit = 2 Wounds (§3.8). "Damage exceeding 3× Health is treated as 3× Health." With Health 10: cap fires at damage 30+. This is unreachable through normal combat (weapon bonus max ~4 + excess successes from large pool). Cap is functionally inert under normal play.

**Overflow mechanics:**
- Hit for 12 damage on Health 10 = 10 (incapacitation), overflow = 2. Wound taken, Health resets to 10, 2 damage applied → Health 8.
- Same hit never exceeds 1 Wound. Single-hit cap verified functional.

### Edge Case: Two-Wound Single Hit
"No single hit inflicts more than 2 Wounds." When can a single hit apply 2 Wounds?
- Health 10, damage = 22 (exceeds 2× Health). Wound 1: overflow = 12. Health resets to 10. 12 > 10 again: second Wound. Health resets to 10, overflow 2. Health 8. Two wounds applied.
- Damage 22 at normal play: Weapon Bonus max ~4. To reach 22, need 18 excess successes. At 15D TN7 (max pool): expected net ~5. This requires ~18 net successes — practically impossible. Cap is safety net only.

### Findings
**F4 — Ob Penalty Accumulation at Desperate TN:** Character with 2 Wounds attempting desperate action (TN8) at Ob 3. Pool 9D → effective Ob 3+2 = 5. At TN8, expected net per die ≈ 0.2. 9D expected net ≈ 1.8. P(≥5 net) < 5%. In desperate situations, a 2-Wound character is mechanically near-useless. This feels intentional as "retreat or die" pressure — verify design intent.

**F5 — Health = Endurance + 6 formula:** Low-Endurance character (End=1): Health 7. One serious hit (damage 8) → overflow 1 → Wound 1. Incapacitated at 2 Wounds (§3.8: End 1–3). Such a character is two serious hits from incapacitation with minimal buffer. Fragile archetype works as described. No issue.

**F6 — Wound Ob on Thread operations:** Wound penalties apply to ALL rolls including Thread operations (Leap Ob = TS-tier Ob + 1 per Wound). A TS 30–49 character (Leap Ob 2 base) with 2 Wounds attempts Leap at Ob 4. Pool: Attunement + History. Typical pool 6D. P(≥4 net at TN7 6D) ≈ 35%. Heavily wounded practitioners should avoid combat — works as pressure. No mechanical issue.

**Severity:** F4 = P3 (intentional). F5 = P3 (intentional). F6 = P3 (intentional).

---

## TEST B2-003 — Histories: Pool Formula and Fork
**Coverage:** M-003 | TTRPG | PAST | — | — | — | — | Non-TS Scholar

**Mode A — Isolation**

### Pool Formula
History pool = Primary Attribute + (History points + 3).
- Example: Attunement 5, "Einhir Scholar" 3 points → pool = 5 + (3+3) = 11D.
- Minimum pool with History: Attribute 1 + (0 pts + 3) = 4D.
- Maximum realistic pool: Attribute 7 + (cap pts + 3). History cap = Memory score. Memory max 7. If History cap = 7 pts, pool = 7 + (7+3) = 17D.

### Fork Mechanic
When two Histories apply to a task, player Forks: rolls both, takes better result.

**Fork Probability Advantage:**
- Two independent pool-6D rolls at Ob 3. P(success on one roll) ≈ 45%. P(at least one success from two rolls) = 1 − (0.55)² = 1 − 0.30 = **70%.** Fork is a major advantage.
- Two pool-8D rolls at Ob 3. Single P(success) ≈ 66%. Fork P = 1 − (0.34)² = **88%.**

### Advancement via Test Track
Tested History advances automatically. Verified: no CP cost for test-track advancement — growth is play-driven.

### Findings
**F7 — Fork exploitation at Ob 1:** Two applicable Histories, each at pool 8D vs Ob 1. Single P(overwhelming) ≈ 82%. Fork means both rolls likely achieve Overwhelming. Rules say "take better result" — so only one result applies. No exploitation issue. However: Fork effectively guarantees Overwhelming on trivial tasks with two relevant Histories. GMs should avoid calling for rolls where both Histories apply and task is trivial (§1.5 Let It Ride governs this).

**F8 — History cap = Memory:** Maximum History points per History = Memory score. Memory max 7. Pool ceiling = 7 + 10 = 17D. At TN7, expected net ≈ 5.6 — this is a campaign-veteran number appropriate for late-game. No runaway scaling; Memory attribute is the hard cap.

**F9 — New History at 0 points (5 CP):** History pool with 0 points = Attribute + 3. This is a fixed-cost unlock that immediately gives +3 over raw attribute. For social skills (Circles, Resources), this significantly expands pool before investment. Design intent is that narrative justification gates acquisition. No mathematical issue.

**Severity:** All P3.

---

## TEST B2-004 — Beliefs and Maxims: CP Generation Rates
**Coverage:** M-004, M-005 | TTRPG | CROSS | — | — | — | — | Generic

**Mode A — Isolation**

### Belief CP per Session
Active engagement in a scene: +1 CP. Challenge engaged: +1 CP. Maximum per session from one Belief: +2 CP (active in scene + challenged).

With 3 Beliefs, maximum session CP from Beliefs = 6 CP (all three active + all three challenged). Realistic per-session: 2–4 CP.

### Maxims
Similar to Beliefs but shorter-horizon. No specific text found in §4 for separate Maxim CP rates — ruleset appears to combine Beliefs and Maxims under one CP award table. **Verify: do Maxims generate CP at the same rate as Beliefs, or at a different rate?** Text at §4.2 lists Belief events only. Maxims mentioned in §2 (Attributes) but no separate CP table found.

**[FLAG: POSSIBLE GAP — Maxims CP rate not found in §4.2. Either: (a) Maxims use same table as Beliefs, or (b) Maxims are handled only at domain-action level. Requires ruleset check.]**

### CP Expenditure Rates vs Generation
- Attribute +1 (Attribute score × 3 CP). From score 4→5: 12 CP. From 5→6: 15 CP.
- At 3 CP/session average: Attribute advancement ≈ 4–5 sessions per point. Appropriate pacing.
- Approach Training (8 CP): ~3 sessions minimum if Beliefs fire aggressively. Realistic: 6–8 sessions. Appropriate unlock cost.

### Findings
**F10 — Maxims CP gap:** §4.2 defines Belief CP table. §4.5 (Maxims, per attribute list) does not appear to have a standalone CP table in the compiled ruleset. If Maxims are intended as CP-generators parallel to Beliefs, the mechanic is underdocumented. If Maxims are purely thematic, the ruleset name implies mechanical weight they don't have.

**Severity:** F10 = P2 (documentation gap; may confuse play).

---

## TEST B2-005 — Inspirations: Spend/Stunt Probability Impact
**Coverage:** M-006 | TTRPG | PRES | — | — | — | — | Faction Leader

**Mode A — Isolation**

### Spend (value 1+)
Adds Spirit score in bonus dice when focus is relevant. Spirit max 7.

**Effect at Spirit 5:**
- Base pool 8D + 5 bonus dice = 13D at TN7.
- Without Spend: expected net ≈ 2.6. With Spend: expected net ≈ 4.3. Net gain ≈ +1.7 expected successes.
- P(success Ob 3) without: ~60%. With: ~83%. Spend is significant but not game-breaking.

### Stunt (value 2+)
Auto-successes = relevant attribute (no roll for those). Then Spirit bonus dice. Then remaining pool.

**Example: Cognition 5, Inspiration value 3, base pool 8D, Ob 3:**
- Auto-successes: 5. Already meets Ob 3 — Success guaranteed minimum. 
- Roll 8D (remaining pool) + Spirit bonus dice. Any positive net makes this Overwhelming (5 auto + rolled ≥ 6 total → 2× Ob).
- Stunt effectively guarantees Overwhelming on any Ob ≤ attribute score.

### Stunt Constraint on Collective Operations
"Stunt auto-successes replace rolled dice; helpers' contributed dice do not apply to a Stunt." This prevents Stunt from compounding with collective Thread operations. Key anti-exploit rule.

### Inspiration Attack in Debates
"Inspiration loses 1 point if defending orator achieves net ≤ 0 on an exchange where Character Style + named Inspiration is used." Requires: attacker knows the Inspiration focus, uses Character Style, opponent actually fails (not just loses).

**F11 — Stunt at Ob ≤ Attribute (dominance case):** Any character with Inspiration value 2+ can guarantee Success on any task where Ob ≤ their primary attribute, once per scene per Inspiration. This is intentional "hero moment" design but means that a character with Inspiration in their primary Belief area effectively has per-scene auto-success on that domain.

**F12 — Inspiration Attack discovery barrier:** Attack requires knowing the target's Inspiration focus. Mechanical gap: how does a character discover another's Inspiration focus? Text says "requires prior investigation or Overwhelming social success." Investigation procedure not specified beyond that. GMs must improvise the discovery mechanic.

**Severity:** F11 = P3 (intentional hero moment). F12 = P2 (discovery procedure underdocumented).

---

## TEST B2-006 — Gate Conditions: Bloodied, Rattled, Unmask
**Coverage:** M-007 | TTRPG | PRES | COMP | — | — | — | Generic

**Mode D — Edge Cases**

Conditions from §9.1 (social) and §3.8 (physical).

### Bloodied (Combat)
No explicit "Bloodied" condition found in CP14 ruleset — §3.8 uses Wounds + incapacitation threshold instead. The matrix tag M-007 uses "Bloodied" but the ruleset term is "Wound." Verify if Bloodied is a renamed pre-CP14 condition that was removed.

**[FLAG: M-007 label says "Bloodied, Rattled, Unmask." Ruleset CP14 does not use the term "Bloodied" — it uses Wounds and incapacitation thresholds. Either: (a) Bloodied = entering first Wound, or (b) Bloodied was retired in CP14. Requires matrix correction.]**

### Rattled (Social)
Triggers when accumulated social strain **first equals or exceeds** Composure.
- Rattled: −2D all social rolls (Presence, Cognition, Attunement).
- Persists until: Unmask, scene end, or rest.

**Simultaneous Rattled + Wounds:**
- Social scene turns violent. Character has Wounds (+1 Ob all rolls) AND Rattled (−2D social).
- Effective: −2D pool AND +1 Ob on social exchanges. Double-burden if character is physically and socially damaged simultaneously.
- No cap or interaction rule specified. Stack is additive. Works but can produce very harsh states mid-hybrid scene.

### Unmask
- Clears all social strain. Composure full.
- If mid-Debate: current incomplete exchange voided. Subsequent social Ob = exchange deficit + 1.
- "Debate cannot resume after Unmask."

**Edge Case — Unmask in Grand Debate (5 exchanges), exchange 2:**
- Exchange deficit = 3 (3 exchanges remain). Subsequent social Ob = 3 + 1 = Ob 4.
- This is severe. A player who Unmasked early in a Grand Debate faces Ob 4 for all subsequent social action in the scene. Functionally removes the character from formal debate.
- But: they clear all strain and the scene changes nature. Could be tactically correct if on the verge of Rattled.

**F13 — Bloodied label mismatch:** M-007 uses "Bloodied" but CP14 doesn't. Coverage matrix entry may be tracking a retired condition. Recommend renaming M-007 entry to "Wound Conditions" or verifying pre-CP14 Bloodied condition status.

**F14 — Unmask Ob calculus:** Exchange deficit Ob can reach 4+ in a 5-exchange Grand Debate. This is intentional — Unmask is a drastic play, not an easy out. Works as designed.

**Severity:** F13 = P2 (tracking error). F14 = P3 (intentional).

---

## TEST B2-007 — Knots: Strain Cascade Simulation
**Coverage:** M-010 | TTRPG | CROSS | TS, INT | — | — | — | Practitioner

**Mode C — Full Scenario**

### Setup
Kael, a practitioner.
- Bonds 4, so 4 Knots tracked.
- Knot A (Close, wife Mira): Wrongness threshold 3, Crisis threshold 6. Current strain: 0.
- Knot B (Regular, mentor): Wrongness 5, Crisis 10. Strain: 1.
- Intelligibility: 7 (Strained — +1 strain to Close Knots per 3 sessions).

## State: Season Start
```
Kael — Intelligibility 7, Certainty 4/Spirit 5, TD 6/20
Knot A (Mira, Close): strain 0/3/6
Knot B (Mentor, Regular): strain 1/5/10
TT 35 | TC 28 | IP 20
```

### Event 1 — Thread Operation (Relational Scale)
Kael performs a Relational-scale Pulling.
- Intelligibility: 7 → 6 (Strained, no change of tier — still ×1 strain rate)
- TT: +6 (Relational scale × TT multiplier ×2, assume base TT gain from operation = 3, so +6)
- Certainty: −1 (successful Leap) → Certainty 3

## State: After Operation
```
Kael — Intelligibility 6, Certainty 3/5
TT 41 — crossed 40 threshold (TC starts gaining; Thread operations become more destabilising)
Knot A: strain 0 | Knot B: strain 1
```

### Event 2 — Composure Buffer (Social Scene)
Kael loses a Debate exchange (+2 Composure strain). Redirects 2 Composure strain to Knot A (+1 strain per use, redirected 2 uses).
- Knot A: 0 + 2 = **strain 2** (approaching wrongness threshold 3).
- Composure preserved (no Rattled).

### Event 3 — Intelligibility Decay (3 sessions pass)
Intelligibility at 7–5 tier: +1 strain to all Knots per 3 sessions.
- Knot A: 2 + 1 = **strain 3** → **WRONGNESS TRIGGERED**. Mira begins sensing something off about Kael.
- Knot B: 1 + 1 = strain 2.

### Event 4 — Player Calls Knot A
Desperate roll. Calls Knot A (+2 strain, +3D bonus).
- Knot A: 3 + 2 = **strain 5**. One below Crisis threshold.
- **Wrongness already active** — Mira is visibly disturbed. +3D on the roll proceeds but the narrative cost is escalating.

### Event 5 — Second Relational Operation
Intelligibility: 6 → 5 (still Strained tier). Certainty 2/5.

**3 sessions later:** Intelligibility at 7–5 tier: +1 strain per 3 sessions.
- Knot A: 5 + 1 = **strain 6 → CRISIS**. Mira cannot be Called. She acts: confrontation, departure, or betrayal.
- Knot B: 2 + 1 = strain 3.

## Final State
```
Kael — Intelligibility 5, Certainty 2/5
Knot A (CRISIS — cannot Call, NPC acts)
Knot B: strain 3/5
TT 47 | TC 30 | IP 20
```

### Findings
**F15 — Composure Buffer Acceleration:** Using Knot as Composure buffer (×2 per redirected use) combined with Intelligibility decay creates a double-track deterioration. A practitioner in social conflict can exhaust a Close Knot in 2–3 sessions if using it as a buffer repeatedly. This is a meaningful trade — correct.

**F16 — Crisis Knot locks player out of major asset:** Once in Crisis, Knot cannot be Called AND the NPC acts against the character. No mechanical recovery path is specified for Crisis Knots. Text says "resolution requires a dedicated scene." Procedure for what happens if that scene is delayed indefinitely is absent.

**F17 — Knot strain recovery rate vs accumulation rate:** Close Knots recover −1 strain per season. But a season is ~4 sessions. In 4 sessions: Intelligibility decay +1, potential Combat×1/social×1 = easily +2–3 strain. Net: Knots accumulate strain faster than they heal for active practitioners. This is intentional pressure but creates an endgame where all Knots deteriorate.

**Severity:** F16 = P2 (missing recovery procedure). F17 = P2 (endgame pressure without clear ceiling).

---

## TEST B2-008 — Circles: Faction Linkage and Network Damage
**Coverage:** M-011 | TTRPG | PRES | — | Crown, Church | — | Faction Leader

**Mode A — Isolation**

### Pool Construction
Circles: Presence + highest applicable History bonus. TN 7.

**Example:** Serena, Crown diplomat.
- Presence 5, "Court Connections" History 4 pts → pool = 5 + (4+3) = 12D.
- Reputation with Crown: +3 → +1D per 2 pts = +1D. Final pool = 13D.

**P(Ob 4 — intelligence assets):** 13D TN7 expected net ≈ 4.3. P(≥4) ≈ 74%. Highly connected diplomat reliably reaches Church inner circle. **Note: this pool assumes History is Court Connections — "full bonus for Crown/Church circles." Confirmed applicable.**

### Against Church (hostile Reputation −3):
- −1D per 2 negative pts = −1D. Final pool = 12D.
- Same Ob 4: P(≥4) ≈ 70%. Hostile reputation barely matters at this pool size — only −4% success rate. Network Damage (−1D per 3 accumulated) is more impactful than reputation for established operatives.

### Network Damage Cascade
3 burned contacts in Crown faction = −1D permanent to Crown Circles.
- Serena at 2 Network Damage: pool 13D.
- 3rd contact burned: pool drops to 12D permanently.
- Recovery: 1 Network Damage per season of non-hostile activity.

**F18 — Reputation diminishing impact:** At pool 12+D, faction reputation modifiers (±1D per 2 pts) are near-negligible (2–4% swing on Ob 3–4). Reputation becomes meaningful only when base pool is small (new character, no relevant History). Long-term veteran characters are nearly immune to reputation swings. Possible intent, but reputation as a tracking mechanic loses gameplay weight for experienced characters.

**Severity:** F18 = P2 (mechanical impact attrition).

---

## TEST B2-009 — Resources: Degradation and Recovery
**Coverage:** M-012 | TTRPG | PRES | — | Guilds | — | Faction Leader

**Mode A + D — Isolation + Edge Cases**

### Degradation Paths
| Event | Resources Effect |
|-------|-----------------|
| Partial at any Ob | −1D next roll this season (temporary) |
| Failure at Ob 3+ | −1D permanent until recovered |
| Failure at Ob 5 | −2D permanent |
| Territory conquered (Resources tied there) | −1D permanent |
| Faction collapse (Resources tied there) | −2D permanent |

**Maximum degradation scenario:** Character relies on Guild faction and controls two territories. Both territories conquered + Guild collapses → −2D (faction) + −2D (two territory losses) = −4D permanent. If starting pool was 6D, now 2D. Two consecutive Ob 5 failures: −4D more. Total: character at 0D Resources.

**0D Resources:** No pool to roll. Character cannot procure anything through normal channels. 

**[FLAG: What happens when Resources pool hits 0? Ruleset does not specify whether the minimum pool rule (§3.4, combat pool minimum 5) applies to social/economic skills. Resources at 0D = total poverty with no mechanical floor.** Text says recovery requires "successful Resources roll at Ob ≤ 2." If pool is 0, this roll cannot be made. This is a deadlock — character cannot recover without a pool, but cannot build a pool without a roll.]

### Recovery Rate
One successful Ob ≤ 2 roll = +1D. Or: full season of commerce-focused activity = all lost dice restored.

**Seasonal commerce path bypasses the pool-0 deadlock** — it does not require a roll. So the deadlock only bites if the GM disallows full-season recovery.

**F19 — Resources pool-0 deadlock:** If all lost dice from failures are treated as permanent, and commerce recovery is unavailable (captured character, active conflict season), the character has no mechanical path to Resources recovery. Recommend confirming seasonal commerce recovery is always available regardless of other season activity.

**Severity:** F19 = P2 (potential deadlock).

---

## TEST B2-010 — The Leap: Eligibility and Contact Window
**Coverage:** M-013 | TTRPG | PRES | TS, TD, CERT | — | — | Almud | Practitioner

**Mode C — Scenario (Almud, TS 28)**

Almud attempts the Leap for the first time after TS growth to 32 (post-Discovery Event).

### State: Pre-Leap
```
Almud — Coord 4, End 3, Health 9, Wounds 0, Composure 9
TS 32 (Stirring), Certainty 4/Spirit 4
Approach Training: just acquired via Spontaneous Breakthrough
TT 38 | TC 42 | IP 22
```

**Eligibility check:**
- Approach Training ✓ (just acquired)
- TS 32 (≥30) ✓
- TT 38 (≥20) ✓
- Not in active melee ✓
- Not at incapacitation threshold ✓

### Leap Roll
Pool: Attunement 4 + "Einhir Scholar" History (2 pts + 3) = 4 + 5 = **9D**
TN 7, Ob: TS 30–49 = **Ob 2**.
P(≥2 net, 9D TN7): Expected net 3.0. P(≥2) ≈ 86%.

| Degree | P | Consequence |
|--------|---|-------------|
| Overwhelming (≥4 net) | ~64% | Contact established; Certainty −1; Contact duration: Attunement+3 rounds |
| Success (≥2 net) | ~22% | Contact established; Certainty −1 |
| Partial (1 net) | ~9% | Contact established; Certainty −1; contact duration halved |
| Failure (≤0) | ~5% | No contact; Certainty −1 anyway |

**Post-Leap state (most likely: Overwhelming):**
```
Almud — Certainty 3/4, in Contact
Contact Duration: Attunement 4 + 3 = 7 rounds
TD: will accumulate during contact (Co-Movement)
TT 38 — no TT modifier yet (operation not yet performed)
```

### Findings
**F20 — Certainty loss on Failure:** Certainty −1 even on failed Leap. Almud at Certainty 4 with max 4: failure reduces Certainty to 3. On Certainty 0 → Rendering Crisis. With max Spirit 4 and frequent Leaping: can reach 0 in 4 attempts even with 86% success rate (occasional failures stack).

**F21 — Contact Duration = Attunement + 3 rounds:** Almud (Attunement 4) gets 7 rounds. Mid-Stirring practitioner performing a Relational-scale operation (which typically takes 1–2 rounds to execute) — 7 rounds is adequate but tight in complex scenes. Higher-Attunement practitioners get proportionally more time. Intentional scaling.

**Severity:** F20 = P3 (Certainty drain is intended pressure). F21 = P3 (intentional).

---

## TEST B2-011 — Diagnosis: Information and Ob Reduction
**Coverage:** M-014 | TTRPG | PAST | TS | — | — | Vaynard | Practitioner

**Mode A — Isolation**

Vaynard (TS 55, Attuned) performs Diagnosis on an unknown Shifting Object in his collection.

**Pool:** Attunement 6 + "Thread Research" History (3 pts + 3) = 6 + 6 = **12D**
**TN:** 7. **Ob:** Object-scale Diagnosis = Ob 1 (from scale table: Object = base Ob 1).

P(Overwhelming, 12D, Ob 1): P(≥2 net) ≈ 99%. Diagnosis is near-certain for a high-TS practitioner.

### Information Returned by Degree
**[FLAG: Diagnosis outcome details not fully specified in §5.3 text. The section heading exists but content was not in the read range. Assuming from context: Success = identify configuration type; Overwhelming = full Thread state including history, Originary status, active operations targeting it.]**

**Ob 1 Overwhelming:** Virtually guaranteed. Diagnosis becomes informational rather than challenging — it's a resource expenditure (Certainty −1, contact duration used) not a skill test for high-TS practitioners.

**F22 — Diagnosis triviality at high TS:** For TS 50+ practitioners with good Attunement histories, Diagnosis at Object scale is auto-success. This means information asymmetry (who has Diagnosed what) rather than success/fail is the real play texture. Works for experienced practitioners; new Stirring practitioners (TS 30–49) face genuine Ob 2 vs smaller pools — more tension.

**Severity:** F22 = P3 (intentional scaling).

---

## TEST B2-012 — Weaving: Multi-Scale Ob Verification
**Coverage:** M-015 | TTRPG/HYB | PRES | TT, TS | Revolution, Guilds | — | Practitioner, Faction Leader

**Mode B — Interaction Chain**

**Scenario:** A Revolution practitioner Weaves a trade agreement between the Guilds and the Revolution (Relational scale).

**Scale → Ob:** Relational scale base Ob = 3. TT multiplier ×2.
**TT at 42:** Standard Ob applies (no bonus modifier at TT 40–59).

**Pool:** Attunement 5 + "Thread Practices" History (4 pts + 3) = 5 + 7 = **12D**
**TN:** 7. **Ob:** 3.

P(Success, 12D, Ob 3): P(≥3 net) ≈ 90%. P(Overwhelming ≥6) ≈ 68%.

**TT gain on completion:** Operation TT base (Relational): +3 (base) × TT multiplier from scale ×2 = **+6 TT**.
TT: 42 → 48.

### Interaction: Weaving → Faction Stats
Relational scale Weaving producing a trade agreement. Thread → Faction handoff rule: "targets a faction-level configuration → resolves as Domain Action using Thread pool and faction-scale Ob."

**Domain Action from Weaving:** Guild Wealth Ob = floor(6/2) = Ob 3 (Wealth stat ÷ 2, round up). Same roll.

**Co-Movement:** On a successful Weaving at Relational scale:
- Actual: agreement takes form
- Temporal: accumulated history of Guilds-Revolution relationship shifts (old disputes recede slightly)
- Epistemic: parties involved feel a subtle sense of rightness about the arrangement

**F23 — TT gain from beneficial Weaving:** Even stabilising Thread operations (Weaving things into coherence) generate TT. A practitioner trying to help faction relationships is inadvertently raising TT. This creates a "no free operations" economy — every Thread action has global cost regardless of intent. Philosophically consistent with P-01 Inseparability and P-03 Rendering = consciousness. Correct. No mechanical issue.

**Severity:** F23 = P3 (correct design expression of P-01).

---

## TEST B2-013 — Pulling: Object → Personal → Relational Scale Progression
**Coverage:** M-016 | TTRPG | PRES | TT, TD, TS | — | — | — | Practitioner

**Mode A — Isolation across scales**

### Object Scale Pulling
Target: a locked door (physical mechanism).
**Pool:** 8D. **Ob:** 1 (Object scale). **TN:** 7.
P(Success) ≈ 97%. TT gain = base +2 × TN multiplier ×1 = +2 TT.
Co-movement: Object opened/altered. Temporal: object's actualization history shifts slightly. Epistemic: practitioner experiences micro-perceptual adjustment.
Certainty: −1 (Leap cost, not per operation).

### Personal Scale Pulling
Target: a person's certainty about a belief ("loosen their grip on the conviction").
**Pool:** 8D. **Ob:** 2 (Personal scale). **TN:** 7.
P(Success) ≈ 86%. TT gain = +2 × ×1 = +2 TT.
Epistemic co-movement: target experiences perceptual seduction (P-10) — their certainty about the belief literally destabilises.
TD accumulation on practitioner: +1 TD from P-11.

### Relational Scale Pulling
Target: the bond of obligation between a Guild master and the Crown.
**Pool:** 8D. **Ob:** 3 (Relational scale). **TN:** 7.
P(Success) ≈ 72%. TT gain = +2 × ×2 = +4 TT.
Intelligibility cost: −1.
Social co-movement: the relationship's actualized history shifts. The Crown's claim on the Guild master weakens in ways neither party fully understands.

### Findings
**F24 — TT gain is scale-independent in impact on the operation but scale-dependent in TT cost:** Object and Personal scale both use ×1 multiplier. Practitioner can perform many Object/Personal Pulls in a season with predictable TT cost, but Relational Pulls double the TT impact. Encourages precision: use lowest scale that achieves the goal. Correct mechanical incentive.

**F25 — Personal-scale Pulling as social manipulation:** Pulling a person's Certainty or conviction is a Thread operation with a social target. Compare to Debate (Cognition-based) or Appeal (Presence-based). Thread-based manipulation bypasses social resistance entirely — no Composure track, no Disposition modifier, no Rhetoric counter. A practitioner with a good Pulling pool can achieve social outcomes that would be mechanically impossible through normal social skills. No explicit cross-domain protection rule noted.

**Severity:** F25 = P1 — Thread Pulling as social bypass has no counter-mechanic for non-practitioners. A non-sensitive character cannot detect or resist Personal-scale Pulling. This creates a dominant strategy for practitioner social manipulation.

---

## TEST B2-014 — Forced Resolution Lock: Persistence and Resistance
**Coverage:** M-017 | TTRPG | CROSS | TS, TT, TD | Varfell | — | Vaynard | Practitioner

**Mode B — Interaction**

Vaynard (TS 55) FR-Locks a diplomatic agreement between Varfell and Hafenmark to prevent either party from reconsidering.

**Scale:** Relational. **Ob:** FR at Relational = standard Ob 3 + FR modifier (+1 Ob vs standard Pulling — per §5.7 Forced Resolution is at TN 8 Desperate-equivalent). Wait — §1.2 states "Thread operations use TN 7 (Standard) or TN 8 for Forced Resolution."

**Corrected:** FR at TN 8.
**Pool:** Attunement 6 + History 6 = 12D. **TN:** 8, **Ob:** 3.
P(die success at TN8) = 0.3. Expected net per die ≈ 0.2 net. 12D expected net ≈ 2.4.

P(≥3 net, 12D TN8): Need precise calc. P(die ≥8) = 0.3. Using binomial approximation: P(≥3 from 12 dice at 0.3) ≈ 75%.

**TT gain:** Relational × TT ×2 multiplier. Plus FR operations have higher baseline TT gain (§5.7 states +2 TT per degree for FR). 
TT: +4 minimum (Success) to +8 (Overwhelming).

**Persistence of Lock:**
The Lock maintains the configuration (the agreement's actualisation). Anyone attempting to Pull or dissolve the agreement must overcome Lock resistance: Ob = creating practitioner's TS ÷ 10 = 55 ÷ 10 = **Ob 6** (round up).

**Attempting to dissolve (adversary practitioner, TS 40):**
Pool: Attunement 4 + History 5 = 9D. TN 8 (FR). Expected net ≈ 1.8. P(≥6) ≈ 2%. **Near-impossible.**

### Findings
**F26 — FR Lock as near-permanent configuration:** A high-TS practitioner (TS 70+) creates a Lock at Ob 7 resistance. Even another high-TS practitioner attempting dissolution faces a nearly impossible roll. FR Locks by powerful practitioners are functionally permanent unless specifically targeted with collective operations or Einhir techniques. This is a significant political mechanic — Vaynard-tier characters can "lock in" political arrangements.

**F27 — FR Lock on non-consensual social target:** FR-Locking a diplomatic agreement requires both parties to be Thread configurations, not consenting parties. The parties experience the locked arrangement as "right" (epistemic co-movement) without knowing why. This is mechanically powerful non-consensual social control. Canon-compliant (P-10: epistemic seduction is a natural co-movement), but has roleplay ethics weight.

**Severity:** F26 = P2 (balance consideration for high-TS factions). F27 = P3 (intentional — epistemic seduction is canonical).

---

## TEST B2-015 — Forced Resolution Dissolution: Gap Creation Risk
**Coverage:** M-018 | TTRPG | PRES | TT, TD | — | — | — | Practitioner

**Mode D — Edge Cases**

FR Dissolution: collapses a configuration to its absent pole. Highest-risk Thread operation.

**TN:** 8. Scale matters heavily.

| Scale | Ob | TT Gain (success) | Gap Risk |
|-------|----|-------------------|----------|
| Object | 1 | +1×1 = +1 | None specified |
| Personal | 2 | +2×1 = +2 | None standard |
| Relational | 5 | +5×2 = +10 | None standard |
| Territorial | 8 | +8×3 = +24 | FR failure at this scale → creates second Gap |
| Structural | 8+ | ×5 = +40 | Gap assured |

**Failure consequence:** "FR Dissolution (Ob 4 for Gap closure): destroys entity but creates second Gap on failure." This Ob 4 refers to monstrous entity dissolution — territorial-scale operation.

**Standard FR Dissolution failure:** Ruleset §5.7 says Dissolution Partial result — "goal achieved with a complication." What complication? Not specified as Gap-creation at Personal/Relational scale. Only confirmed Gap-creation at Territorial/higher or monstrous entity contexts.

**[FLAG: FR Dissolution failure/partial at Personal and Relational scale — what is the complication? Text says "complication occurs" on Partial but does not specify for Dissolution. Gap creation may be the appropriate complication for Dissolution specifically but it's not stated. Mechanical gap.]**

### Findings
**F28 — Dissolution failure complication undefined:** At Personal and Relational scale, FR Dissolution Partial result specifies "complication" but the complication for Dissolution is not defined. For Forced Resolution — Lock, a partial might mean "Lock is unstable, decays in 1d4 seasons." For Dissolution, the natural complication would be partial collapse (object/relationship half-dissolved, residue formed). But this is GM inference, not rules text.

**Severity:** F28 = P2 (missing complication definition for Dissolution partial/failure at sub-territorial scale).

---

## TEST B2-016 — Taint Track: Escalation and Plateau
**Coverage:** M-021 | TTRPG | CROSS | TS, TD, TT | — | — | — | Practitioner

**Mode A — Isolation**

Taint Track: 0–10. Gain from: sources not fully enumerated in §4.4 or §5. Search reveals "Taint 0/10" listed in state tracking format (§Skill) but Taint mechanic text was not in scanned sections.

**[FLAG: Taint mechanic text not located in CP14 sections scanned. May be in Part Five (Thread Operations) not yet read. Cannot complete full Taint isolation test. Logging as coverage gap.]**

From state tracking format and §5.11 (Dissolution Residue): "−1 Coherence per use" references an older Coherence track. Post-CP14, Coherence was replaced by Intelligibility. Residue use says "−1 Coherence per use" — this may be a patch error. If Coherence = Intelligibility in this context, residue drains Intelligibility. If Taint is a separate track from Intelligibility, its sources and effects need a dedicated read.

**F29 — Taint/Coherence/Intelligibility text inconsistency:** §5.11 Dissolution Residue says "−1 Coherence per use." CP14 replaces Coherence with Intelligibility. Either: (a) §5.11 wasn't patched and "Coherence" should read "Intelligibility," or (b) Taint and Intelligibility are distinct tracks and residue drains Taint. Requires clarification.

**Severity:** F29 = P1 — Track nomenclature inconsistency in active mechanic.

---

## TEST B2-017 — Dissolution Residue: Power Source Risk
**Coverage:** M-022 | TTRPG | PRES | TD, TS | Niflhel, Varfell | — | Vaynard | Practitioner

**Mode B — Interaction**

Practitioner uses dissolution residue (Potency 3) to boost a Pulling operation.

**Bonus:** +3D to pool. Explode on 9–10 (not just 10). "−1 Coherence per use" (see F29 above).

**Volatility impact:** Standard chaining: explode on 10 only. Residue: explode on 9–10.
P(chain) per die standard = 10%. With residue: P(chain on bonus die) = 20%.

**Expected value increase from 3 bonus dice at 9–10 chain:**
- Standard bonus die: E(successes) ≈ 0.4 (TN7) + 0.1 × E(chain die) ≈ 0.44.
- Residue bonus die: 0.4 (TN7) + 0.2 × E(chain) ≈ 0.48. Marginal improvement per die.
- 3 residue dice: +1.44 expected successes vs +1.32 standard bonus dice.
- Net advantage: **+0.12 expected successes** over standard bonus dice. Residue is barely better than standard bonus dice in expected value but has higher variance (more likely to cascade or fail spectacularly).

**Depletion:** Same source +1 Ob per use. Three uses = Ob +3 on third use. Forces spreading residue use across multiple sources.

### Findings
**F30 — Residue advantage is marginal:** The 9–10 chain bonus provides only ~0.04 additional expected success per bonus die vs. standard chaining. The main value is variance increase. This may be intentional (residue is dangerous, not just powerful) but players expecting a major advantage from residue will be disappointed by the math.

**F31 — Coherence/Intelligibility drain from residue use:** Per F29, this drains an unclear track. If it's Intelligibility: one Intelligibility per use is significant (Intelligibility ranges 0–10 with no passive recovery). High-potency residue as regular power source would be Intelligibility-draining in a way that compounds the practitioner death spiral.

**Severity:** F30 = P3 (expected — variance is the point). F31 = P1 (links to F29 track confusion).

---

## TEST B2-018 — Monstrous Entities: Modes 1–3 Tactical Analysis
**Coverage:** M-026 | TTRPG/HYB | PRES | TT, TS, CERT | — | — | — | Practitioner, Inquisitor

**Mode C — Scenario**

### Setup: Mode 1 Incursion at TT 45
Gap opened in Sudwald (Thread Wound, TT threshold −10 early: fires at TT 35 = TT 45 elsewhere).
Mode 1 entity: Health 6, Martial 3, Cohesion 1. Deteriorates −1 Health/round naturally.

### State: Round 1
```
Entity — Health 6, Martial 3
Combat characters (Crown soldiers, generic): Pool 8D, Coord 4, End 4
Practitioner Kael — TS 52, in Contact window
Certainty: −1 all in scene (entity presence)
TT 45 | TC 31
```

**Entity attack:** Pool 3D vs defender 4D split.
Expected attacker net: 1.0. Expected defender (4D defence split): ≈ 0.7 net (approx, assuming defender commits 2D to defence from 4D total).
**P(entity hits):** attacker net > defender net. P(1.0 > 0.7) — depends on distribution. Rough: P(entity scores net ≥ 1 more than defender) ≈ 40%. Entity is a moderate threat to unarmoured characters.

**Physical damage halved vs entity:** Attacker hits for 3 damage → entity takes 1 (halved). Entity has effective Health = 12 equivalent for conventional combat.

**Entity natural deterioration:** −1 Health/round. 6 rounds until natural dissolution without intervention.

**Practitioner option (Weaving TS 60+ required for entity + Gap closure):** Kael TS 52 — below TS 60 threshold. Cannot use Weaving to close Gap simultaneously with entity. Must use FR Dissolution (Ob 4) for entity — but this risks creating a second Gap on failure.

**Round 6 — Entity at Health 1 (natural):** Dissolves. Leaves dissolution residue. Gap persists. New entity manifests in 1d4 seasons.

### Findings
**F32 — Mode 1 entity is clock management:** Without a TS 60+ practitioner, Mode 1 entities must be waited out (6 rounds) or fought conventionally (Health 12 equivalent). FR Dissolution can accelerate this but risks compounding the Gap. Tactical pressure is appropriate — the entity is a resource drain, not a boss fight.

**F33 — Mode 3 Threadcut Being gap:** Past-Oriented Pulling "auto-produces a Gap" against Threadcut beings. This is stated in §5.15 but no Ob or procedure for dealing with Threadcut beings via other Thread approaches is specified. All standard operations fail or have adverse effects. The only stated defeat mechanisms are: conventional combat (destroys configuration, Gap persists) or extended Weaving (TS 60+, Ob 4). Threadcut beings effectively force collective operations or are campaign-arc threats.

**Severity:** F32 = P3 (intentional). F33 = P2 (Threadcut being mechanics sparse for non-Weaving approaches).

---

## TEST B2-019 — Southernmost Zone Entry: Forgetting Interaction
**Coverage:** M-027, M-028, M-029 | TTRPG | PRES | TS, CERT, TD | — | — | Maret Uln | Practitioner

**Mode C — Scenario**

Maret Uln (TS 58, Varfell/Southernmost, practitioner) leads a Southernmost Expedition.

**Entry requirement:** Must be launched from Askeheim (T13). Non-Thread orders +1 Ob in Askeheim. Practitioners: automatic Discovery Event per season present.

### State: Expedition Entry
```
Maret — TS 58, Certainty 3/Spirit 5, TD 4/20, Intelligibility 8
TT 48 | TC 30 | IP 25
Askeheim: non-Thread orders +1 Ob
```

**Discovery Event at Askeheim (automatic):**
Spirit check TN 7 Ob 1 for TS growth.
Pool: Spirit 5. P(≥1 net) ≈ 93%. 
Expected outcome: TS grows to 63 (+5).

### Forgetting (M-029)
§6.1 Forgetting mechanics not in the scanned range. **[FLAG: Forgetting mechanic text at §6.1 not confirmed from scan. Proceeding from system understanding: Forgetting causes gradual loss of recent memories in the Southernmost, with Memory checks to retain information.]**

**Expected Forgetting interaction with Practitioners:** High TS may protect against or intensify Forgetting (the practitioner perceives more of what the Forgetting is erasing). Specific Ob and pool details require §6.1 read.

### Findings
**F34 — Forgetting + TD interaction:** If Forgetting reduces Memory-based track performance and TD represents temporal disjunction, Southernmost Expedition may create a compounding spiral: high TD (>10) impairs reality-rendering, while Forgetting impairs Memory. Combined: practitioner in the Southernmost loses both their cognitive anchor and their temporal orientation. Requires §6.1 read to confirm whether these interact.

**Severity:** F34 = P2 (potential cascade, pending §6.1 verification).

---

## TEST B2-020 — Altonian Pressure: Escalation Thresholds
**Coverage:** M-032 | TTRPG/BG | FUT | IP, TT, TC | Crown, Löwenritter | — | Ehrenwall | Faction Leader

**Mode A — Isolation + Threshold Testing**

### IP Track: 0–100
§7.3 details:
- IP 30: Altonian tutoring demand for Torben (Crown political pressure event).
- IP 75+: Altonian vanguard deploys to Schoenland (T15). Sea route severed. Altonian spies active.

### State Testing: IP Thresholds
| IP | State | Mechanical Effect |
|----|-------|-------------------|
| 0–29 | Latent | No mechanical effect. Altonia background threat. |
| 30 | Tutoring Demand | Covert contact Ob 3 fires. Torben extraction options activate. |
| 50 | Mid-escalation | [No mid-tier threshold found — gap?] |
| 75 | Vanguard | Schoenland vanguard deploys. Sea route severed. Intelligence all Schoenland actions revealed to Altonia. |
| 100 | Invasion | [Not specified in scanned text — full invasion mechanics?] |

**[FLAG: IP 50 threshold not defined. IP 100 consequence not found in scan. Mid-range and terminal IP mechanics may be in §7.3 or §14.5 which weren't fully scanned.]**

**IP drain mechanic:** How does IP decrease? Seasonal accounting? Player actions? Not visible in §7.3 scan.

**F35 — IP mid-tier gap:** No mechanical events between IP 30 and IP 75. A 45-point stretch with no threshold events means IP accumulates with no feedback pressure until the dramatic vanguard event. This creates a "nothing, nothing, nothing, CRISIS" escalation pattern with no graduated warning.

**Severity:** F35 = P2 (escalation feedback missing mid-tier).

---

## TEST B2-021 — Domain Actions: Dual-Roll Resolution
**Coverage:** M-035 | TTRPG/HYB | PRES | FSTAT | Crown, Church | — | Almud, Himlensendt | Faction Leader

**Mode B — Interaction Chain**

King Almud's personal Debate (Scene) → Domain Echo → Crown Mandate change.

### Setup
Almud (Cognition 5, "Royal Policy" History 3 pts = pool 11D) debates Church Cardinal Himlensendt over Confession jurisdiction. High-stakes formal Debate (3 exchanges).

**Personal Ob:** Himlensendt Disposition: Cool (Ob 3).
**Domain Ob:** Church Influence ÷ 2 = 6 ÷ 2 = Ob 3.

**Exchange 1:**
- Almud: 11D TN7 vs Ob 3. Expected net ≈ 3.6. P(Success) ≈ 75%.
- Himlensendt: NPC pool (Church Mandate pool used for NPC per §8.1). Church Mandate 5 → 5D. Expected net ≈ 1.7. 

**Exchange 1 outcome (most likely: Almud wins):**
- Himlensendt takes +1 Composure strain.
- Domain Echo fires: Church Influence −1 (Almud's position advances constitutionally).
- Crown Mandate +1 (winning public Debate).

**But:** Seasonal cap ±2 per stat per season. Domain Echo changes count toward cap. If Almud wins all 3 exchanges: Church Influence could drop −3, but cap prevents more than −2 per season.

**F36 — Domain Echo double-trigger:** If Almud wins 3 exchanges each triggering a Church Influence −1, the first two fire (−2 total, hitting seasonal cap). Third exchange: Domain Echo is mechanically voided by the cap. Does the player know this mid-Debate? Do they know when the cap fires? Rules text does not specify whether cap notification is player-visible or GM-internal.

**Severity:** F36 = P2 (cap transparency issue).

---

## TEST B2-022 — Combat Initiative and Pool Split
**Coverage:** M-039, M-040, M-041 | TTRPG | PRES | — | Crown, Löwenritter | — | Ehrenwall | Löwenritter Knight

**Mode C — Combat Scenario**

### Setup
Knight-Commander Ehrenwall (Agility 5, "Sword Training" History 4 pts = Combat Pool 5 + (4+3) = 12D) vs. a Crown soldier (Agility 3, pool = 3 + 6 = 9D minimum, use 9D).

### State: Round 1
```
Ehrenwall — Pool 12D, Health 14, Wounds 0
Soldier — Pool 9D, Health 10, Wounds 0
Weapon: both Long reach, starting at Long range.
```

**Initiative:** Ehrenwall Agility 5 vs Soldier Agility 3.
Ehrenwall: 5D TN7 Ob 1. P(success) ≈ 97%.
Soldier: 3D TN7 Ob 1. P(success) ≈ 73%.
Ehrenwall wins initiative (>97% likely). Ehrenwall declares **last**.

**Phase 1 — Soldier declares first:** Attack.
**Phase 1 — Ehrenwall declares last (knowing soldier is attacking):** Attack.

**Phase 2 — Division:**
- Soldier (9D, knowing Ehrenwall will attack): split 5/4 (Offence/Defence) or 4/5.
  - Optimal vs unknown Ehrenwall: rough 5/4 split.
- Ehrenwall (12D, knowing soldier attacked, divides last): sees 5/4 information. Splits 8/4 (heavy offence — commits to decisive strike knowing their offence will be strong).

**Phase 3 — Resolution:**

**Ehrenwall offence:** 8D at Weapon TN. Assume longsword TN = 7. Expected net ≈ 2.6.
**Soldier defence:** 4D TN7 (dodge). Expected net ≈ 1.3.
P(Ehrenwall hit): P(Ehrenwall net > Soldier net). With E(A)=2.6, E(D)=1.3: approximately P(hit) ≈ 72%.
Damage if hit: Weapon Bonus (longsword ~3) + excess successes (≈1.3) − Armour (assume 1) ≈ 3.3. Expected ~3 damage.

**Soldier offence:** 5D at Weapon TN7. Expected net ≈ 1.6.
**Ehrenwall defence:** 4D TN7. Expected net ≈ 1.3.
P(Soldier hit): P(1.6 > 1.3) ≈ 55%.
Damage if hit: Weapon Bonus (shortsword ~2) + excess (~0.3) − Armour 1 ≈ 1.3. ~1 damage.

**Simultaneous damage: both hits apply simultaneously.**

**Round 1 outcome (expected):**
- Ehrenwall hits for ~3 damage. Soldier Health: 10 → 7.
- Soldier hits for ~1 damage. Ehrenwall Health: 14 → 13.

### Findings
**F37 — Initiative advantage is decisive:** Ehrenwall's initiative grants information and last-declare. This allows heavy offence commitment (8/4 vs soldier's 5/4) with knowledge of what the opponent committed to. The information asymmetry is more valuable than raw pool size. A smaller-pool character who wins initiative could consistently outperform a larger-pool character who loses it.

**F38 — Simultaneous damage lethality check:** In this exchange, both characters can take damage in the same round. Against matched opponents (both with strong offence), this creates mutually assured wounding. Two characters each committing 8D offence/2D defence would expect both to hit with moderate damage each round — combat is quick and brutal. This is the design intent (simultaneous pool-split = lethal, consequential).

**Severity:** F37 = P3 (intentional — initiative as information advantage). F38 = P3 (intentional lethality).

---

## TEST B2-023 — Damage Formula: Weapon Bonus Interaction
**Coverage:** M-042, M-043 | TTRPG | PRES | — | — | — | — | Löwenritter Knight

**Mode A — Isolation**

Damage = Weapon Bonus + excess attack successes − Armour Rating (min 0).

**Weapon table not fully scanned.** §8.2 "Weapons and Armour" at line 2375. Known from context: longsword Weapon Bonus ~3, shortsword ~2.

### Damage Scenarios
| Attacker Pool | Defender Pool | Expected Excess | Weapon Bonus | Armour | Expected Damage |
|---------------|---------------|-----------------|--------------|--------|-----------------|
| 8D off vs 2D def | | E(att)=2.6, E(def)=0.7, excess=1.9 | 3 | 0 | 4.9 |
| 8D off vs 4D def | | E(att)=2.6, E(def)=1.3, excess=1.3 | 3 | 0 | 4.3 |
| 8D off vs 4D def | | E(att)=2.6, E(def)=1.3, excess=1.3 | 3 | 2 | 2.3 |
| 4D off vs 4D def | | E(att)=1.3, E(def)=1.3, excess=0 | 3 | 0 | 3.0 |

**Note on tied nets:** "If attack net > defence net: hit." Tie = no hit. With equal pools, P(tie + no-hit) is meaningful — roughly 30% of rounds result in no damage to either party. This creates an attrition pattern: equal combatants regularly exchange inconclusive rounds.

### Findings
**F39 — Armour 2 halves expected damage:** Armour Rating 2 reduces expected damage from 4.3 to 2.3 (roughly halved). Armour is a strong defensive tool. A fully armoured character (Armour 3) against an 8D/4D split attacker: damage = 4.3 − 3 = 1.3 expected. They can survive many more hits. This validates armour as meaningful gear, not cosmetic.

**F40 — Weapon Bonus 3 at 0 excess successes:** Even if attacker barely exceeds defender (excess = 0), Weapon Bonus still applies. Damage floor = Weapon Bonus − Armour. This prevents "defended but barely" from being zero damage. Correct.

**Severity:** All P3 (intended).

---

## TEST B2-024 — Mass Combat Resolution
**Coverage:** M-045 | BG/HYB | PRES | FSTAT | Löwenritter, Crown | — | Ehrenwall | Löwenritter Knight

**Mode A — Isolation**

§8.3 Mass Combat: "Disposition table, single roll per battle" (BG mode).

**[FLAG: §8.3 Mass Combat full text at line 2405 not read. Proceeding from §12 Mode descriptions: Board game uses "Disposition table, single roll per battle." TTRPG uses "Zone-based operational; Zoom In/Out for personal moments."]**

**Board Game Mass Combat (single roll):**
Attacking faction rolls Military pool (d10s, TN7) vs defending faction Military pool. Higher net successes wins. Loser routes.

**Löwenritter (Military 5) attacks Crown-defended territory (Military 4):**
- Löwenritter: 5D TN7. Expected net ≈ 1.65.
- Crown: 4D TN7. Expected net ≈ 1.32.
- P(Löwenritter net > Crown net) ≈ 58%.

**Fortification bonus for defender:** +1D per Fortification level. Crown in Valorsplatz (Fort 2): 4+2 = 6D defence.
- Crown: 6D expected net ≈ 2.0. P(Löwenritter wins) ≈ 42%.

The Fortification system meaningfully equalises: a weaker military faction defending well-fortified territory is competitive.

### Findings
**F41 — BG mass combat P(defender wins) with any fortification:** At Fortification 2+, even a Military 4 defender against Military 7 attacker (max): 4+2=6D vs 7D. P(6D net > 7D net) ≈ 43%. High Fortification gives 40%+ win chance regardless of military size. This may be intentional (sieges require sustained effort) but in BG mode a single Fortification 3 location can resist indefinitely on dice variance.

**Severity:** F41 = P2 (BG mode stalemate risk at high fortification).

---

## TEST B2-025 — Thread Events in Social Scenes
**Coverage:** M-047 | TTRPG | CROSS | TT, TS, CERT | Church, Crown | — | Himlensendt, Almud | Practitioner, Devout Character

**Mode B — Interaction**

A Devout Church official (Himlensendt, TS 0, Devout Constraint) is in a Debate with a practitioner who performs Pulling on the official's conviction mid-scene.

**Social mechanics (Debate):** Himlensendt rolling 5D Cognition vs practitioner's 8D. Normal Debate.

**Thread intrusion:** Practitioner in Contact window (maintained from pre-scene Leap). Attempts Personal-scale Pulling on Himlensendt's theological certainty.

**F25 applies here (from TEST B2-013):** Himlensendt has no defence against Thread Pulling — he cannot detect it (TS 0). No counter-roll. No resistance track. The Pulling can succeed and alter his conviction independent of the Debate outcome.

**Dual resolution:** Debate exchange resolves socially. Thread Pulling resolves mechanically. Both apply simultaneously.

**Himlensendt's Devout Constraint:** Cannot attempt TS growth voluntarily. But Discovery Events bypass the Constraint. Does a successful Personal Pulling (epistemic seduction) constitute a Discovery Event for Himlensendt? If yes: Theological Dissonance Event fires even if Himlensendt doesn't understand why his certainty is shifting.

**F42 — Thread + Social double-layered manipulation:** A practitioner can simultaneously win a Debate (social roll) AND use Thread Pulling to alter the target's certainty (Thread operation). These are parallel resolution tracks with no interaction rule. The combined effect (lost Debate + altered conviction) could exceed what either alone could achieve. No mechanic prevents stacking.

**F43 — Devout character involuntary Dissonance:** If Pulling constitutes a Discovery Event (GM ruling required), Himlensendt could accumulate Dissonance Marks from Thread operations he doesn't know are happening. At 3 Marks, Devout Constraint collapses. This is a viable strategy for destabilising Church characters without them ever being able to defend against it.

**Severity:** F42 = P2 (no cap on combined social+Thread manipulation). F43 = P2 (requires GM ruling — Discovery Event definition may not cover external Pulling).

---

## TEST B2-026 — Scale Transitions: Personal → Faction Handoff
**Coverage:** M-048 | TTRPG/HYB | PRES | FSTAT, TT | Guilds, Revolution | — | — | Faction Leader

**Mode C — Scenario**

A Guilds faction leader negotiates with the Revolution to establish a mutual non-aggression arrangement. Personal Appeal in a scene → Domain Echo → faction Influence adjustment.

### Resolution
**Personal roll:** Presence 5 + "Guild Representative" History 3 = 8D. Ob 3 (Revolution Influence Ob = hostile Disposition). TN 7.
P(Success) ≈ 72%.

**Domain Echo fires automatically from the successful Appeal:**
- Scope: faction-level consequence (non-aggression pact = Influence change).
- Domain Ob: Revolution Influence ÷ 2 = 3 ÷ 2 = Ob 2 (round up).
- **Same roll resolves both:** 8D vs Ob 3 (personal) succeeds → same net successes resolve Domain Ob 2 (faction). Since Ob 3 success implies ≥3 net, Domain Ob 2 automatically succeeds as well when personal succeeds.

**Result:** Personal scene outcome (non-aggression agreed) + Domain Echo (Revolution Influence +1 from Crown acknowledgment of their political legitimacy).

### Findings
**F44 — Domain Echo auto-resolve at lower Ob:** When Domain Ob < Personal Ob, Domain Echo always succeeds if the personal roll does. No friction. This is correct — the personal scene is the harder task; the faction consequence is easier to actualise. Well-designed.

**F45 — Hybrid mode double-count risk:** In hybrid mode, if the same scene is played in TTRPG Personal Phase and the same outcome is applied in BG Strategic Phase, could it trigger Domain Echo twice? Seasonal cap (±2) should prevent this, but the trigger mechanism ("same roll resolves both") may fire in both phases if the scene is described to both the TTRPG and BG players. Needs hybrid-specific clarification.

**Severity:** F44 = P3. F45 = P2 (hybrid double-trigger risk).

---

## TEST B2-027 — Quick Rest / Full Rest: Wound Recovery Rate
**Coverage:** M-053 | TTRPG | PRES | — | — | — | — | Generic

**Mode A — Isolation**

### Recovery Rates
| Rest Type | Time | Health | Wounds |
|-----------|------|--------|--------|
| Quick Rest | Between scenes (minutes–hours) | Restore to max | Remove 1 Wound |
| Full Rest | Full night | Restore all Health | Remove ALL Wounds |
| CP purchase | Between seasons | — | Remove 1 Wound (6 CP) |

### Edge Cases
**Multiple Wounds after single scene:** Fighter with 3 Wounds after a battle. Quick Rest: removes 1 Wound → 2 Wounds. Still at full Ob +2 penalty. Full Rest (next night): removes all Wounds. Fully recovered.

**Wound removal during active threat:** Enemy forces attacking. Can Quick Rest occur "between scenes" during an active multi-scene combat encounter? Rules say "between scenes" — if the GM defines the scene as continuous, Quick Rest is unavailable until scene ends.

**F46 — Quick Rest as tactical resource:** A party that controls when scenes end (controls the narrative) can Quick Rest frequently. In TTRPG mode, GM scene structure determines rest access. In BG mode, there is no scene structure — unclear when Quick Rest applies between board game phases.

**F47 — 6 CP Wound removal:** At 3 CP/session average generation, removing a Wound mid-campaign costs 2 sessions of CP. Between seasons only. This creates pressure to not take Wounds in the first place rather than treating them as recoverable resources. Correct.

**Severity:** F46 = P2 (BG mode rest ambiguity). F47 = P3 (intentional).

---

## TEST B2-028 — Einhir Sites: Preservation and Destruction
**Coverage:** M-054 | TTRPG/HYB | PAST | TT, TS, TC | Revolution, Crown, Church | — | — | Practitioner, Non-TS Scholar

**Mode B — Interaction**

Eisengrund (T9) Einhir ruins. Revolution Community Weaving −1 Ob here. Varfell Private Collection here.

**Church destroys the site (Domain Action):**
- Church Intelligence or Military used? "Control shifts when one faction has only military units present."
- Destroying archaeological/Thread site: Domain Action under what framework? Church Ethical Framework: Divine Command. Destroying Einhir ruin = aligned with theological stance (suppressing pre-doctrinal evidence). −1 Ob.
- Domain Ob: Target configuration = Thread site? No Faction stat directly. GM must determine Ob from Ob calibration guide.

**[FLAG: Mechanic for destroying Thread-significant territories/sites not formally defined. §7.5 describes Thread-Significant Territories' properties but no procedure for their destruction or modification. This is a gap.]**

**F48 — Thread site destruction procedure absent:** Einhir Sites (M-054) have preservation mechanics implied (Community Weaving, Einhir Texts) but no formal destruction Ob or procedure. A faction-level Domain Action to destroy a Thread site has no mechanical anchor.

**Severity:** F48 = P2 (gap in faction–Thread interaction).

---

## TEST B2-029 — Three-Dimensional Co-Movement in Combat
**Coverage:** M-033, M-046 | TTRPG | CROSS | TT, TD, CERT | — | — | — | Practitioner, Löwenritter Knight

**Mode C — Scenario**

**Three dimensions: Actual / Temporal / Epistemic (per Co-Movement Quick Reference, §5.17)**

Practitioner performs a Relational-scale Weaving in the middle of a physical combat — stabilising the bond between two allied soldiers who are about to break and flee.

**Thread Operation:** Relational Weaving. Pool 10D, TN7, Ob 3. P(Success) ≈ 81%.

**On Success — Three-Dimensional Co-Movement:**

| Dimension | What Moves | How |
|-----------|-----------|-----|
| Actual | The soldiers' morale bond coheres — they hold position | Combat mechanical effect: treat as +1D on next allied combined action |
| Temporal | Their accumulated shared history (comrades in arms) is actualised — past becomes present | Temporal: minor Past-Oriented resonance. This scene becomes more "real" in the Thread-sense — a small TD gain +1 |
| Epistemic | Both soldiers feel an inexplicable certainty about each other — seduction toward cohere | P-10: epistemic seduction fires. Both soldiers: Certainty −1 (they feel the uncanny) OR Certainty +1 if framed as reaffirming a Belief |

**Certainty outcome (epistemic dimension):** Certainty cost from co-movement on witnesses? Text specifies Certainty −1 on Leap and on witnessing monstrous entities. Co-movement epistemic effects on bystanders are not given explicit Certainty costs. **[FLAG: Bystander Certainty effect from co-movement not specified.]**

### Findings
**F49 — Co-movement bystander mechanics undefined:** §5.17 Quick Reference describes the three dimensions but does not give mechanical rules for how co-movement affects non-practitioner bystanders. The GM is expected to narrate it, but no Certainty cost, no check, no defined minimum effect.

**Severity:** F49 = P2 (co-movement incomplete as a mechanical specification for bystanders).

---

## TEST B2-030 — Hybrid Mode: Strategic + Personal Phase Integration
**Coverage:** M-048 | HYB | CROSS | FSTAT, TT, TC, IP | All factions | — | Multiple | Multiple Archetypes

**Mode C — Full Scenario (Hybrid Turn Structure)**

### Hybrid Turn (per §12.3)
One hybrid "season" = Strategic Phase (board game) + Personal Phase (TTRPG scenes).

### State: Season 4
```
TT 52 | TC 38 | IP 30 (Torben tutoring demand active)
Factions: Crown M5/I5/W4/Mi4/Sta4, Church M5/I6/W5/Mi4/Sta5
Revolutionary informal presence active in Korntal/Sudwald
```

**Strategic Phase (BG):**
- Crown: Govern order in Border Pass (T4). Roll Crown Military 4D vs Ob 2 (Govern). P(Success) ≈ 83%. If success: +1 Crown Military presence at invasion route.
- Church: Recruit order in Himmelstift (T3). TC +1 (Grand Cathedral property each season controlled). TC: 38 → 39.
- Löwenritter: Fortify Ehrenfeld (T5). Fort 3 → 4 (max for Ehrenfeld).
- Niflhel: Intelligence order in Schwarzmarkt (T10). −1 Ob (Quiet Network property). 

**Domain Echo from Strategic Phase:** Crown Govern success at Border Pass → Crown Military +1? No — Domain Actions from BG orders affect faction stats, not territory Military presence directly. Govern = territorial control maintenance, not Military stat change. Seasonal cap ±2 applies.

**Personal Phase (TTRPG) — IP 30 Event:**
Torben tutoring demand requires covert contact attempt at Int Ob 3. Player can choose to meet or avoid.

**Seasonal Accounting (end of season):**
1. Stability checks: Crown (no active threats) Ob 1. Church (one political threat: Almud's constitutional challenge) Ob 2.
2. TT drift: passive TT change based on active Gaps, Shifting Objects. Sudwald Gap (Thread Wound): TT +4/season.
3. TC +1 (Himmelstift controlled by Church). TC: 39 → 40. **TC 40 threshold check?** [§7.2 TC thresholds not scanned in full — FLAG]
4. IP: no passive drift rule found. Stays at 30 unless player action.

### Findings
**F50 — Hybrid mode seasonal clock accumulation:** In one season, TT +4 (Gap passive), TC +1 (Church property), IP static. At this rate: TT hits 60 in ~2 seasons, TC hits 60 in ~22 seasons, IP requires events to move. Clock rates are asymmetric: TT escalates quickly from environment, TC escalates slowly from Church actions, IP only from specific triggers. This produces reliable mid-campaign crises on TT, late-game Church dominance pressure on TC, and event-driven Altonian crises on IP.

**F51 — Seasonal cap shared across modes:** "Faction attribute may not change by more than ±2 per season regardless of how many sources target them in either phase." This cap applies. In practice: a faction targeted by both BG orders AND TTRPG Domain Echoes in the same season hits the ±2 wall quickly. Players need to coordinate which mode delivers the change — a hybrid coordination mechanic that incentivises inter-mode planning.

**Severity:** F50 = P3 (intentional asymmetric escalation). F51 = P2 (coordination burden — players may not know they're double-targeting until cap fires mid-session).

---

## FINDINGS SUMMARY

| Finding | Severity | Mechanic(s) | Description |
|---------|----------|-------------|-------------|
| F1 | P3 | M-001 | Ob 10 near-impossibility — confirm intent |
| F2 | P2 | M-001 | Ob 1 Overwhelming floods Momentum |
| F3 | P3 | M-001 | Desperate TN + Wound Ob combines harshly |
| F4 | P3 | M-002 | 2-Wound character near-useless in desperate situations — intended |
| F5 | P3 | M-002 | Low-End characters fragile — intended |
| F6 | P3 | M-002 | Wound Ob on Thread ops — intentional pressure |
| F7 | P3 | M-003 | Fork near-guarantees Overwhelming on trivial tasks |
| F8 | P3 | M-003 | 17D max pool — late-game appropriate |
| F9 | P3 | M-003 | New History at 0 pts gives instant +3 pool |
| F10 | P2 | M-004/M-005 | Maxims CP rate underdocumented |
| F11 | P3 | M-006 | Stunt guarantees Overwhelming at Ob ≤ attribute — intended hero moment |
| F12 | P2 | M-006 | Inspiration discovery procedure underdocumented |
| F13 | P2 | M-007 | "Bloodied" label mismatch — condition retired in CP14 |
| F14 | P3 | M-007 | Unmask Ob calculus — intentional drastic cost |
| F15 | P3 | M-010 | Composure buffer acceleration — correct trade |
| F16 | P2 | M-010 | Crisis Knot: missing recovery procedure if scene is deferred |
| F17 | P2 | M-010 | Knot accumulation > recovery for active practitioners |
| F18 | P2 | M-011 | Faction reputation loses mechanical weight at high pools |
| F19 | P2 | M-012 | Resources pool-0 deadlock unless seasonal commerce confirmed |
| F20 | P3 | M-013 | Certainty drain on failed Leap — intended |
| F21 | P3 | M-013 | Contact duration scales with Attunement — intentional |
| F22 | P3 | M-014 | Diagnosis trivial at high TS — intentional scaling |
| F23 | P3 | M-015 | TT gain from beneficial Weaving — P-01 compliant |
| **F24** | P3 | M-016 | TT scale incentive works correctly |
| **F25** | **P1** | **M-016** | **Personal-scale Pulling bypasses all social counter-mechanics — no non-practitioner resistance** |
| F26 | P2 | M-017 | FR Lock near-permanent at high TS — balance check |
| F27 | P3 | M-017 | FR Lock epistemic seduction — P-10 compliant |
| **F28** | P2 | M-018 | FR Dissolution partial/failure complication undefined at sub-territorial scale |
| **F29** | **P1** | **M-021** | **Taint/Coherence/Intelligibility nomenclature inconsistency in §5.11** |
| F30 | P3 | M-022 | Residue advantage is marginal — intended variance play |
| **F31** | **P1** | **M-022** | **Dissolution Residue drains unclear track (Coherence vs Intelligibility)** |
| F32 | P3 | M-026 | Mode 1 entity is clock management — intended |
| F33 | P2 | M-026 | Threadcut Being mechanics sparse for non-Weaving approaches |
| F34 | P2 | M-027/M-029 | Forgetting + TD cascade potential (pending §6.1 read) |
| F35 | P2 | M-032 | IP mid-tier gap (30→75 no threshold events) |
| F36 | P2 | M-035 | Domain Echo seasonal cap not player-visible when it fires |
| F37 | P3 | M-039 | Initiative information advantage — intentional |
| F38 | P3 | M-041 | Simultaneous damage lethality — intended |
| F39 | P3 | M-042/M-043 | Armour 2 halves expected damage — correct |
| F40 | P3 | M-042/M-043 | Weapon Bonus at 0 excess — correct damage floor |
| F41 | P2 | M-045 | BG mass combat stalemate at high Fortification |
| F42 | P2 | M-047 | Thread + social manipulation: no cap on combined effect |
| F43 | P2 | M-047 | Devout Dissonance Mark accumulation from unknown Pulling |
| F44 | P3 | M-048 | Domain Echo auto-resolve at lower Ob — correct |
| F45 | P2 | M-048 | Hybrid mode Domain Echo double-trigger risk |
| F46 | P2 | M-053 | Quick Rest BG mode ambiguity |
| F47 | P3 | M-053 | 6 CP Wound removal pacing — intended |
| **F48** | P2 | M-054 | Einhir Site destruction procedure absent |
| F49 | P2 | M-033/M-046 | Co-movement bystander Certainty mechanics undefined |
| F50 | P3 | M-048 | Hybrid clock accumulation asymmetric — intended |
| F51 | P2 | M-048 | Hybrid seasonal cap coordination burden |

### P1 Findings (Requires Immediate Attention)
1. **F25** — M-016 Personal-scale Pulling: no social counter-mechanic for non-practitioners
2. **F29** — M-021 Taint/Coherence/Intelligibility nomenclature conflict in §5.11
3. **F31** — M-022 Dissolution Residue drains "Coherence" — undefined in CP14 terminology

### P2 Findings (Significant Issues, 23 total)
F2, F10, F12, F13, F16, F17, F18, F19, F26, F28, F33, F34, F35, F36, F41, F42, F43, F45, F46, F48, F49, F51

---

## Coverage Dimension Log

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes |
|---------|-----------|------|----------|--------|----------|------|------------|
| B2-001 | M-001 | TTRPG | PRES | — | — | — | Generic |
| B2-002 | M-002 | TTRPG | PRES | — | — | — | Faction Leader |
| B2-003 | M-003 | TTRPG | PAST | — | — | — | Non-TS Scholar |
| B2-004 | M-004, M-005 | TTRPG | CROSS | — | — | — | Generic |
| B2-005 | M-006 | TTRPG | PRES | — | — | — | Faction Leader |
| B2-006 | M-007 | TTRPG | PRES | COMP | — | — | Generic |
| B2-007 | M-010 | TTRPG | CROSS | TS, INT | — | — | Practitioner |
| B2-008 | M-011 | TTRPG | PRES | — | Crown, Church | — | Faction Leader |
| B2-009 | M-012 | TTRPG | PRES | — | Guilds | — | Faction Leader |
| B2-010 | M-013 | TTRPG | PRES | TS, TD, CERT | — | Almud | Practitioner |
| B2-011 | M-014 | TTRPG | PAST | TS | — | Vaynard | Practitioner |
| B2-012 | M-015 | TTRPG/HYB | PRES | TT, TS | Revolution, Guilds | — | Practitioner, Faction Leader |
| B2-013 | M-016 | TTRPG | PRES | TT, TD, TS | — | — | Practitioner |
| B2-014 | M-017 | TTRPG | CROSS | TS, TT, TD | Varfell | — | Vaynard | Practitioner |
| B2-015 | M-018 | TTRPG | PRES | TT, TD | — | — | Practitioner |
| B2-016 | M-021 | TTRPG | CROSS | TS, TD, TT | — | — | Practitioner |
| B2-017 | M-022 | TTRPG | PRES | TD, TS | Niflhel, Varfell | Vaynard | Practitioner |
| B2-018 | M-026 | TTRPG/HYB | PRES | TT, TS, CERT | — | — | Practitioner, Inquisitor |
| B2-019 | M-027, M-028, M-029 | TTRPG | PRES | TS, CERT, TD | — | Maret Uln | Practitioner |
| B2-020 | M-032 | TTRPG/BG | FUT | IP, TT, TC | Crown, Löwenritter | Ehrenwall | Faction Leader |
| B2-021 | M-035 | TTRPG/HYB | PRES | FSTAT | Crown, Church | Almud, Himlensendt | Faction Leader |
| B2-022 | M-039, M-040, M-041 | TTRPG | PRES | — | Crown, Löwenritter | Ehrenwall | Löwenritter Knight |
| B2-023 | M-042, M-043 | TTRPG | PRES | — | — | — | Löwenritter Knight |
| B2-024 | M-045 | BG/HYB | PRES | FSTAT | Löwenritter, Crown | Ehrenwall | Löwenritter Knight |
| B2-025 | M-047 | TTRPG | CROSS | TT, TS, CERT | Church, Crown | Himlensendt, Almud | Practitioner, Devout |
| B2-026 | M-048 | TTRPG/HYB | PRES | FSTAT, TT | Guilds, Revolution | — | Faction Leader |
| B2-027 | M-053 | TTRPG | PRES | — | — | — | Generic |
| B2-028 | M-054 | TTRPG/HYB | PAST | TT, TS, TC | Revolution, Crown, Church | — | Practitioner, Non-TS Scholar |
| B2-029 | M-033, M-046 | TTRPG | CROSS | TT, TD, CERT | — | — | Practitioner, Löwenritter Knight |
| B2-030 | M-048 | HYB | CROSS | FSTAT, TT, TC, IP | All | Multiple | Multiple |

---

*End sim_batch_02.md*
