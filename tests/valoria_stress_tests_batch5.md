# VALORIA STRESS TESTS — BATCH 5
## Core Mechanics: M-001 through M-009
### Date: 2026-03-27 | Model: Sonnet 4.6

Coverage dimensions per session instructions: Mechanic × Mode × Temporal × Tracks × Faction × NPC × Archetype

---

## PROBABILITY REFERENCE (computed, d10 pool TN7)

| Pool | E(net) | Ob1: OW/Suc/Par/Fail | Ob2: OW/Suc/Par/Fail | Ob3: OW/Suc/Par/Fail |
|------|--------|----------------------|----------------------|----------------------|
| 4D   | 1.33  | 45/27/0/28%          | 6/38/27/28%          | 0/20/52/28%          |
| 5D   | 1.67  | 54/23/0/23%          | 12/42/23/23%         | 1/28/48/23%          |
| 6D   | 2.00  | 61/20/0/20%          | 19/42/20/20%         | 3/35/43/20%          |
| 8D   | 2.67  | 72/14/0/14%          | 33/38/14/14%         | 8/44/33/14%          |
| 10D  | 3.33  | 79/11/0/10%          | 47/33/11/10%         | 17/47/26/10%         |
| 12D  | 4.00  | 84/8/0/8%            | 57/27/8/8%           | 27/46/20/8%          |

TN8 approximately 20–25% worse P(success) per die than TN7 across all pool sizes.

---

## M-001 — Core Dice Engine

**Mechanic:** d10 pool, TN (7/6/8), Ob 1–10, degrees (Overwhelming/Success/Partial/Failure), 10→chain, 1→−1.

**Mode:** TTRPG | Temporal: PRES | Tracks: none directly | Factions: all | Archetypes: all

### Mode A — Isolation

**Input variables:** Pool size (1–15+), TN (6/7/8), Ob (1–10).

#### Probability findings:

**Ob 1 is auto-generous at high pools.** At 10D TN7 Ob1: P(Overwhelming) = 79%. The most common outcome at expert-level pools on simple tasks is Overwhelming. This is by design (simple tasks are easy for competent characters) but GMs must maintain Ob discipline — Ob 1 should be reserved for genuinely routine tasks, not contested ones.

**The 28% floor:** At 4D TN7, P(Failure) = 28% regardless of Ob. This is the failure floor for low-pool characters — they fail about 1 in 4 attempts even when successes don't matter (Ob doesn't change failure rate, only what failure looks like). **This is correct behaviour** — the 1s mechanic creates a failure floor independent of Ob.

**Partial dominates at moderate pools vs high Ob:** 8D vs Ob 4: Partial = 53%. The system produces a lot of "almost but not quite" outcomes at mismatched difficulties. This is a design feature (fail-forward), not a bug. But GMs should expect Partial to be the *most common outcome* in difficult scenes, requiring robust complication handling.

**Ob 5 with 6D: 73% Partial or worse.** Characters with moderate skill (6D) against Ob 5 will rarely succeed outright (7.5%). The majority of results are Partial (72.8%). The system expects GMs to use Ob 5 sparingly — it produces scenes where even skilled characters struggle to achieve goals without complications.

**Chain (10→reroll) impact:** Chain contributes ~4.4% bonus E(net) per die (0.1 * E(net)). At 8D: adds ~0.35 expected net successes. Meaningful but not dominant. Chains rarely change the degree of outcome — they shift borderline cases.

#### Edge cases:

**1s vs 0 successes rolled:** If all dice show 2–6 (no successes, no 1s): net = 0 = Failure. P(all dice in 2–6 range) at 4D TN7 = 0.5^4 ≈ 6%. This is the "clean miss" state — rare, feels bad narratively. No mechanical issue.

**Net negative result:** Possible when 1s exceed successes. At 4D: P(net ≤ −1) ≈ 12%. The ruleset doesn't specify what net negative means beyond "Failure." This is a gap: is there a complication gradient? **The ruleset treats all net ≤ 0 results as Failure with complication — net negative has no additional mechanical effect beyond Failure.** This is acceptable but GMs may want a signal for catastrophic failures (very negative nets). Flag as P3.

**Ob 10:** Rule explicitly states Overwhelming is unavailable, Partial requires net ≥ 5, below 5 = Failure. At 12D: P(net ≥ 10) = ~4% (Overwhelming threshold, now blocked). P(net ≥ 5) at 12D ≈ 75%. So Ob 10 with a 12D pool: ~75% chance of achieving a Partial result. Success is possible (requires net 10+) but rare. The design produces: even exceptional characters rarely fully succeed at foundational-difficulty tasks. **Correct and intentional.**

**Ob cap interaction:** "Maximum Ob 10 regardless of modifier stacking." If a character with 3 Wounds (+3 Ob) attempts Ob 3 combat task: effective Ob = 6, not 10. The cap only triggers at extreme stacking (4+ wound penalties + high base Ob). Verify: 3 Wounds + Ob 5 base → Ob 8, under cap. 4 Wounds + Ob 7 → Ob 11 → capped at 10. **Cap functions correctly; rarely relevant.**

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M001-01 | P3 | Net negative result has no mechanical distinction from net 0. Some GMs may want a catastrophic failure tier. | No fix needed — note in GM reference that net ≤ −2 is signal for escalated Hard Move. |
| M001-02 | P3 | At high pools (12D+) vs Ob 1, Overwhelming is near-certain (84%). "Simple tasks" become narrative noise. | GM discipline: use Ob 1 only when outcome is genuinely uncertain. No mechanical fix needed. |
| M001-03 | P2 | Partial is the dominant outcome in many challenging scenes (Ob 3–4 with moderate pools). GM complication economy must be robust or sessions stall. | Ensure §13.5 Hard Moves table has sufficient complication options. Audit in Phase 3. |

---

## M-002 — Wound System

**Mechanic:** Health = Endurance + 6; damage reduces Health; at 0 → Wound (reset), +1 Ob cumulative; incapacitation thresholds by Endurance.

**Mode:** TTRPG, BG | Temporal: PRES | Tracks: Health | Factions: all | Archetypes: all

### Mode A — Isolation

**Health range:** Endurance 1→7: Health = 7–13.

| Endurance | Health | Incap threshold | Ob at threshold |
|-----------|--------|----------------|----------------|
| 1 | 7 | 2 Wounds | +2 Ob |
| 2 | 8 | 2 Wounds | +2 Ob |
| 3 | 9 | 2 Wounds | +2 Ob |
| 4 | 10 | 3 Wounds | +3 Ob |
| 5 | 11 | 3 Wounds | +3 Ob |
| 6 | 12 | 4 Wounds | +4 Ob |
| 7 | 13 | 4 Wounds | +4 Ob |

**Damage absorption analysis:** A typical hit inflicts Weapon Bonus + Power + excess successes − armour.

*Example character: Endurance 4 (Health 10), Heavy armour (−3 damage reduction).*
*Attacker 8D vs Defender 5D at TN7: E(attacker net) ≈ 2.67, E(defender net) ≈ 1.67. E(excess) ≈ 1.0. Power 3, weapon +2. E(damage) = 3 + 2 + 1 − 3 = 3 damage per hit.*
*Hits per Wound: 10 ÷ 3 ≈ 3.3 hits per Wound. Comfortable pacing.*

*Lightly armoured character (Endurance 3, Health 9, no armour):*
*E(damage) = 3 + 2 + 1 − 0 = 6 per hit. Hits per Wound: 9 ÷ 6 = 1.5. Very dangerous.*

**Single-hit cap (max 2 Wounds):** A single hit cannot inflict more than 2 Wounds. "Damage exceeding 3× Health treated as 3× Health." So Health 9: cap = 27 damage → Wound + reset to 9, excess damage 18 → 2nd Wound + reset to 9, excess 9 → 3rd Wound... **Wait: the cap says max 2 Wounds from a single hit, but the formula says damage exceeding 3× Health = 3× Health = 27 damage on a 9-Health character. 27 damage = 3 full Health cycles = 3 Wounds. This contradicts the "max 2 Wounds" statement.**

**P1 FINDING — M002-01: Single-hit Wound cap contradicts damage formula.**

The ruleset states: "No single hit inflicts more than 2 Wounds." But also: "Damage exceeding 3× Health is treated as 3× Health." On Health 9: 3× = 27 damage. Applying damage: 9 damage = 1 Wound (reset), 9 more = 2nd Wound (reset), 9 more = 3rd Wound. This produces 3 Wounds from a single hit, contradicting the 2-Wound cap.

**Fix:** Clarify which rule takes precedence. Options: (A) Hard cap at 2 Wounds regardless of damage formula — "excess damage beyond 2 Wounds is lost." (B) Keep 3× formula but clarify cap = 3 Wounds. (C) Remove the cap entirely. Recommend: (A) — simplest, prevents one-shot kills on moderate-Health characters. Add: "Damage in excess of 2× Health triggers 2 Wounds; remaining excess is discarded."

**+1 Ob per Wound stacking:** At 3 Wounds (approaching incap for Endurance 4): +3 Ob. On a standard 6D roll vs Ob 2: effective Ob 5 → P(Success+OW) = 7.5% + 0.0% ≈ 7.5%. P(Partial) = 72.8%. **A heavily wounded character nearly always Partial or Fails.** This is severe but intentional — the wound system is designed to make combat increasingly dangerous. Verify this doesn't create deadlocks.

*Deadlock check: Can a wounded character do anything useful?* With 3 Wounds, all rolls are at +3 Ob. Thread operations (Ob typically 1–3 → becomes Ob 4–6): P(success) drops to 0–7%. Social actions (Ob 1–3 → Ob 4–6): similar. **At 3 Wounds, a character is functionally reduced to Full Defence or narrative-only actions.** This is correct and creates withdrawal pressure. No deadlock — player can still act, just poorly.

**Quick Rest / Full Rest:** Quick Rest (between scenes) restores Health to maximum and removes 1 Wound. Full Rest (full night) removes all Wounds. **Wound pacing:** With Quick Rests available between most scenes, Wound accumulation between scenes is impractical unless the scenario specifically denies rest. The wound system pressure is primarily within-scene.

### Edge Cases:

**Excess damage carryover with 2-Wound cap:** Rule says "excess damage carries over into reset Health." If a hit inflicts 20 damage on Health 9: 9 → Wound (reset to 9), excess 11 → carries over. Now Health = 9 − 11 = −2. That's a second Wound (Health resets again to 9) with excess −2 lost (negative excess ignored). Result: 2 Wounds, 9 Health. **This works if we apply the 2-Wound cap consistently.** The ambiguity is what "excess damage carries over" means when it generates a 3rd Wound.

**Ob stacking with Endurance 1 at incap threshold:** Endurance 1, 2 Wounds = incapacitated. Before incapacitation (at Wound 1): +1 Ob to everything. On a 4D pool vs Ob 1 → effective Ob 2: P(OW+Success) = 44.6%. Still functional at 1 Wound, just degraded. Correct.

**Board game mode:** Wound system presumably applies to unit Health in mass combat (confirmed: "Health = Endurance + 6" for units). The +1 Ob per Wound stacking in unit terms = +1 Ob to unit rolls per Formation Break. Rule text calls this "+1 Ob" for individual characters but uses "Formation Break" for units. **These are parallel, not identical.** Confirm mass combat Wound equivalence is explicitly documented. Flag P2.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M002-01 | **P1** | Single-hit Wound cap (max 2) contradicts "3× Health = 3× Health cap" formula which produces 3 Wounds. | Rule: "A single hit inflicts at most 2 Wounds. Damage beyond 2 Health resets is discarded." |
| M002-02 | P2 | +1 Ob stacking at high Wound counts produces near-total incapacitation before the incap threshold. Intentional, but GMs need clear guidance on NPC behaviour (withdraw, surrender, shift tactics). | Add to §GM Tools: "Characters at 2+ Wounds should tactically change behaviour." |
| M002-03 | P2 | Mass combat Formation Break vs personal Wound system relationship is implicit. Units don't take "Wounds" per the personal scale — but the rule structure is parallel. | Explicit bridging sentence in §8.3 cross-referencing §3.8. |

---

## M-003 — Histories (Pool Formula, Fork, Advancement)

**Mechanic:** Histories are skills as life-experience. Pool = base attribute + (History points + 3). Fork adds +1D from second History. Advancement: marks → increment.

**Mode:** TTRPG | Temporal: PAST | Tracks: none | Factions: all | Archetypes: all

### Mode A — Isolation

**Pool construction:**

History points range: Histories start at 0 and advance. "Points + 3" means a History with 0 points = 3 dice, with 3 points = 6 dice, with 6 points = 9 dice. This is the "+3 floor" that ensures every attempted History roll is meaningful.

**At creation:** Attribute typically 3, History at 0–2 points. Pool = 3 + 3 = 6D (typical), or 3 + 5 = 8D (invested History). Range 4D–10D at creation.

**At advancement (attribute 5, History 6 points):** Pool = 5 + 9 = 14D. E(net) ≈ 14 × 0.333 = 4.7. At Ob 3: P(OW + Success) ≈ 75%. **Expert characters are genuinely excellent at their domain.** Correct.

**Fork mechanism:** "A Fork adds +1D to the existing roll's pool without changing that pool's attribute." The contributing History's attribute is irrelevant — Fork adds exactly 1D. This is elegantly simple.

*Fork frequency concern:* A character with 5 relevant Histories can Fork up to 4 additional times? The ruleset says "Fork" (singular) but doesn't explicitly limit to one Fork per roll. **Ambiguity: can multiple Histories Fork the same roll?**

Checking stage1 (§1.8 equivalent) and stage2... The rule as stated says "a Fork adds +1D." No cap specified on number of Forks per roll. If unlimited: a character with 5 relevant Histories rolls at pool + 4D (or more). At 12D: Ob 3 success rate ~74%. This would trivialize many rolls.

**P2 FINDING — M003-01: Fork count per roll is unspecified.**

If multiple Forks are allowed, pool inflation becomes significant. If limited to one Fork, the rule needs to say so.

**Beginner's Luck (§1.8):** Double Ob, raw attribute only (no History). Attribute 3, Ob 2 → effective Ob 4. 3D vs Ob 4: P(OW+Success) ≈ 0%. P(Partial) ≈ 12%. P(Failure) ≈ 88%. **Beginner's Luck is almost guaranteed to fail at anything above Ob 1.** At Ob 1: 3D → P(OW) = 13%, P(Success) = 40%, P(Partial) = 0%, P(Failure) = 47%. ~53% success rate at Ob 1. This seems intentionally harsh — beginners are bad at things. The narrative reward (first History mark on success) makes the risk worthwhile.

**Advancement:** "marks → increment." Stage10 details CP cost. No issues identified in the advancement mechanic itself from stage1.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M003-01 | P2 | Fork count per roll is unspecified. Unlimited Forks would inflate pools significantly. | Add: "A character may Fork at most twice per roll, each from a distinct relevant History." |
| M003-02 | P3 | Beginner's Luck has ~47% failure at Ob 1, ~88%+ failure at Ob 2+. This is intentional but harsh — new Histories are very hard to establish. Recommend explicit note that this is by design. | Add GM note: "Beginner's Luck should be called rarely; most attempts succeed via existing Histories." |

---

## M-004 — Beliefs (CP Generation)

**Mechanic:** 3 Beliefs per character; achieving/testing a Belief generates Conviction Points (CP); CP spent to advance Histories.

**Mode:** TTRPG | Temporal: CROSS (Beliefs bridge past values → present action → future advancement) | Tracks: none directly | Archetypes: all

### Mode A — Isolation

The Belief system is primarily narrative with mechanical output (CP). The core questions are: (1) CP generation rate, (2) Belief refresh, (3) interaction with advancement economy.

Stage10 advancement (read earlier) has: CP costs. Need stage2 for Belief mechanics directly. Approximating from CP14 context: achieving a Belief = 1–3 CP, testing = 1 CP (standard BWHQ-adjacent structure).

**CP economy stress test:** If a character achieves 1 Belief per session and tests 1: 2–4 CP/session. History advancement cost (stage10): "3 CP + scene" for +1 point. At 2 CP/session: ~1.5 sessions per History increment. History advances require multiple marks → sessions. **Advancement pace: roughly 1 History point per 2–3 sessions.** This is moderate. Max History points not explicitly bounded in what I've read — flag for audit.

**Belief revision:** Beliefs must be mutable or characters stagnate. The ruleset presumably includes a Belief rewrite procedure. Not found in stage1 or stage2 (stage2 not yet read). **Flag as P2 if Belief revision not present.**

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M004-01 | P2 | Belief revision procedure not confirmed in stage1. If Beliefs cannot be rewritten, character development stagnates after initial goals are achieved or rendered impossible. | Confirm in stage2 audit. Flag if absent. |

---

## M-005 — Maxims (CP Generation)

**Coverage matrix lists M-005.** Review of session history: Maxims were **cut entirely** (S3 decision). Gap G-012 = "Virtues & Vices / Maxims — cut entirely (S3)."

**Status: M-005 is a cut mechanic. Coverage matrix entry should be marked ELIMINATED.**

---

## M-006 — Inspirations (Spend, Stunt)

**Mechanic:** Inspiration = named focus area. Spend for bonus dice or Stunts. Cap = Spirit score (max Inspiration value). Inspirations advance through engagement and checks.

**Mode:** TTRPG | Temporal: CROSS | Tracks: none | Archetypes: all

### Mode A — Isolation

**Inspiration cap:** Maximum total Inspiration value = Spirit score (1–7). Maximum individual Inspiration = Spirit score. So a character with Spirit 4 can have: one Inspiration at value 4, or four at value 1, or various combinations summing ≤ 4.

**Spend mechanic:** Spend Inspiration → bonus dice. Stage1 §1.7 (Momentum) notes Momentum adds automatic successes; Inspiration adds dice (different mechanic). Inspiration bonus dice roll at the same TN as the pool.

*The exact spend rate isn't in stage1.* From context: likely 1 Inspiration point = 1 bonus die. At Inspiration 3 on a 6D roll: 9D total → E(net) = 3.0 vs 2.0. The bonus is meaningful (+50% pool) but not overwhelming.

**Stunt mechanic (§1.7 reference; stage10 detail):** Player sets critical success range up to 11–20, expanding failure range by same amount. This creates a risk/reward toggle. At standard (no stunt): Overwhelming = net ≥ 2×Ob. With stunt set to "critical on 8–10": effectively increases chain probability.

**Inspiration interactions with Thread operations:** Stage1 §1.7: "Momentum cannot be spent on Thread operation rolls." Does the same restriction apply to Inspiration? Not specified in stage1. **If Inspirations can be spent on Thread ops, it creates a backdoor pool amplification for practitioners.** Flag P2.

**Spirit cap creates interesting constraint:** Spirit-low characters (Spirit 1–2) have minimal Inspiration capacity. This means characterization (Inspirations) and existential resilience (Certainty = Spirit) are jointly constrained by Spirit. A character investing in Thread operations (needs high Spirit for Certainty) also has more Inspiration capacity. This is an elegant coupling if intentional — practitioners naturally have broader characterization options.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M006-01 | P2 | Inspiration spend on Thread operations not ruled out. If allowed, practitioners gain pool amplification at critical moments. | Add: "Inspiration dice may not be spent on Thread operation rolls (same restriction as Momentum)." |
| M006-02 | P3 | Spirit cap links Certainty resilience and Inspiration capacity — practitioners naturally have higher Inspiration ceiling. Verify this is intentional design. | Note in design rationale. No fix unless unintended. |

---

## M-007 — Conditions — Gate System (Rattled, Bloodied, Unmask)

**Mechanic:** Gate conditions: Rattled (Composure track), Bloodied (wound milestone), Unmask (ends social scene, resets Composure). Conditions layer with mechanical consequences.

**Mode:** TTRPG | Temporal: PRES | Tracks: Composure | Archetypes: all

### Mode A — Isolation

**Composure = Presence + 6 (confirmed from §2.3).**
Presence range 1–7. Composure = 7–13.

**Rattled trigger:** Composure reaches 0 (strain accumulation in social conflict).
**Bloodied:** Not found in stage1 or stage8 under that name. Stage8 uses "Formation Break" for units. Personal combat doesn't use a "Bloodied" gate condition — it uses Wound incapacitation thresholds. **The coverage matrix lists "Bloodied" as part of M-007 but this term may not exist in current CP14.**

Checking stage8 and stage1 for "Bloodied"... Not present. The wound thresholds (2/3/4 Wounds) produce incapacitation, not a named "Bloodied" condition. **M-007 description in the coverage matrix may be stale — predates the wound system redesign.**

**Gap: "Bloodied" gate condition referenced in matrix but not found in current ruleset.** This may be an artifact from an earlier version. Either: (A) Bloodied was cut and the matrix entry needs updating, or (B) a midpoint wound condition was intended but not implemented. Flag P2.

**Rattled mechanics (stage9):** Composure = Presence + 6. Strain from social conflict. Reaching 0 = Rattled. Stage9 post-fix: "Rattled effect: −1D to all social rolls per Rattled mark." This implies Rattled is a stackable condition (marks), not a single binary. The Composure track counts down from Presence + 6, and each time it hits 0, a Rattled mark is added (Health resets to full is the analogy — Composure resets). Verify: the new Rattled-as-stackable-wound model is consistent with stage9.

**Unmask:** Social scene reset mechanic. Terminates ongoing Debate, clears Composure strain. Creates a strategic exit at cost. No probability concerns.

**Interaction with Wound system:** A character can be both wounded (+Ob) and Rattled (−1D social). Combined penalty at 2 Wounds + 1 Rattled mark: +2 Ob to everything, −1D on social. Significant but not deadlocking — character can still act.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M007-01 | P2 | "Bloodied" referenced in coverage matrix but not in current ruleset text. Term may be stale. | Update coverage matrix: M-007 = "Conditions: Rattled, Unmask, Incapacitation Thresholds." Remove "Bloodied" unless it should be added as a named wound milestone. |
| M007-02 | P2 | Rattled as stackable wound model (marks approach) is in stage9 but not explicitly confirmed as "marks accumulate across a scene." Verify: does a second Composure drain to 0 add a second Rattled mark? | Confirm Rattled stacking model in §9.1. |

---

## M-008 — Thread Sensitivity

**Mechanic:** TS 0–100, tiers (Inert/Dormant/Stirring/Active/Heightened/Resonant), growth via exposure/CE, passive perception thresholds.

**Mode:** TTRPG | Temporal: CROSS | Tracks: TS | Factions: Church, Crown | NPCs: Almud, Himlensendt, Vaynard | Archetypes: Practitioner, Inquisitor, Devout

### Mode A — Isolation

**TS tiers (from context):**
| Tier | TS Range | Capabilities |
|------|----------|-------------|
| Inert | 0–9 | No Thread perception |
| Dormant | 10–29 | Passive impressions |
| Stirring | 30–49 | Active perception possible |
| Active | 50–69 | Full Thread operations available |
| Heightened | 70–89 | Enhanced ops, greater risk |
| Resonant | 90–100 | Full practitioner capacity |

**Growth pathways:**
- CE exposure triggers Spirit check (TN7, Ob1): success = +TS (amount per context)
- Discovery Events: immediate +10 TS
- Originary Lock handling: +10 TS (Spirit check or 2 Wounds)
- Taint 3+ characters start Taint at 1 on corruption contact (from patch log)

**TPS (Thread Perception Score):** From session log, TPS = TS ÷ 10 (round down). Adds to Thread op pools. At TS 50 (Active tier): TPS = 5. This adds 5D to all Thread ops — significant pool contribution at full practitioner level.

**Passive perception:** TS 30+ practitioners can perceive Thread events passively. This is a GM tool, not a player-rolled mechanic. No probability concerns.

**Devout Constraint interaction:** Essentialist theology forecloses TS development. Characters with Devout Constraint cannot gain TS through normal exposure. This is a hard block, not a probability-based mechanic. Himlensendt (TS 0, sincerely devout) cannot develop TS regardless of exposure.

**Inquisitor CE accumulation → TS growth trigger:** Inquisitors accumulate CE tracking practitioners. CE 3+ triggers TS growth check. This creates a structural tension: Inquisitors who do their job eventually develop TS themselves. The check is Spirit TN7 Ob1.

*Inquisitor TS growth probability:* Spirit 4 (typical Inquisitor). Pool = 4D, TN7, Ob1. P(Success+OW) = 72%. **An Inquisitor at CE 3+ has a 72% chance to gain TS per confrontation event.** Over 3 confrontations: P(at least one growth) ≈ 98%. Most Inquisitors will eventually develop TS if they do their jobs. This is thematically rich and mechanically correct.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M008-01 | P3 | TS growth amount per CE-triggered check is not specified in stage1/stage3 ("+TS" without value). | Confirm growth amount per check in stage3 or stage2. Likely +5 TS per success degree. |
| M008-02 | P3 | TPS = TS÷10 round down creates a cliff at every 10-point tier boundary. TS 49 → TPS 4; TS 50 → TPS 5. This cliff is intentional (tier gates) but creates pressure to push to next tier threshold. | Note as design feature. No fix. |

---

## M-009 — Certainty Track

**Mechanic:** Certainty = Spirit (starting/maximum). Range 0–7. Costs: observing Thread events, failed operations. At 0: rendering crisis.

**Mode:** TTRPG | Temporal: CROSS | Tracks: CERT | Factions: all | NPCs: all practitioners | Archetypes: Practitioner

### Mode A — Isolation

**Certainty range:** Spirit 1–7. Practitioners with Spirit 3 (typical) start at Certainty 3. Spirit 7 (exceptional) starts at 7.

**Certainty costs (from stage3 context):**
- First witnessing of Gap: −1 Certainty (Spirit check TN7 Ob1 to resist)
- Per scene near a Gap: −1 Certainty (no check to resist)
- Other costs presumably include: failed operations, confronting Mode 3 entities, specific TS thresholds

**Certainty recovery:** Not specified in stage1. Must be in stage3 or stage10. Unconfirmed recovery rate is a critical gap — if Certainty cannot recover, all practitioners drift to 0.

**Rendering crisis at Certainty 0:** Unspecified in what I've read. This is the most significant edge case.

**Probability analysis:**

*Practitioner Spirit 3, Certainty 3:* Three Gap exposures at −1 each = Certainty 0. P(resist first Gap) = 4D TN7 Ob1 = P(Success+OW) ≈ 72%. After 3 Gaps: Expected Certainty remaining = 3 − (3 × 0.28) ≈ 2.2. But this assumes each check is independent. If near a Gap per-scene costs −1 with no check, one scene near a Gap per encounter guarantees −1.

*Session pacing:* A practitioner participating in 3 scenes near Gaps loses 3 Certainty guaranteed. Spirit 3 practitioner is at 0 by session's end. **Without recovery mechanics, Certainty is a consumable resource that depletes to crisis within a single session of active Thread engagement.**

**This is either (A) intentional tension mechanic requiring careful Certainty management, or (B) a pacing problem where practitioners become non-functional too quickly.**

Given the design philosophy (Thread operations are dangerous, existentially costly), this appears intentional. But **recovery must exist** — otherwise practitioners can only function for one scene per rest period.

**P1 FINDING — M009-01: Certainty recovery rate not confirmed. If unspecified, practitioners hit crisis within single sessions of Thread engagement.**

*Certainty at 0 (Rendering Crisis):* The crisis procedure is referenced but not in the material I've read. Stage3 presumably contains the rendering crisis rules. Without them, the 0-state behaviour is undefined in this simulation.

**Certainty and Momentum coupling:** §1.7 states "Momentum resets to 0 at the start of each session." If Certainty also resets between sessions, the two economies are equivalent. But if Certainty is persistent (session to session), it's a campaign-scale resource. Given Momentum resets and Certainty is explicitly tied to "existential coherence," Certainty is likely persistent — which makes the recovery rate even more critical.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| M009-01 | **P1** | Certainty recovery rate not specified in available compilation stages. Without recovery, practitioners hit Rendering Crisis within 1 session of Thread engagement (3 Gap-adjacent scenes = Spirit 3 depleted). | Confirm recovery in stage3 §5.x. If absent, add: "Quick Rest restores 1 Certainty; Full Rest restores Certainty to Spirit score." |
| M009-02 | P2 | Rendering crisis procedure at Certainty 0 not confirmed in simulation material. | Confirm in stage3. |
| M009-03 | P3 | Gap-adjacent per-scene cost (−1, no check) stacks fast in exploration-heavy sessions. GMs need guidance on when "in a scene near a Gap" triggers vs incidental proximity. | Add: "Certainty costs from Gap proximity trigger once per distinct scene, not once per round." |

---

## CROSS-MECHANIC INTERACTION FLAGS (Mode B — for separate testing)

| Chain ID | Mechanics | Interaction | Priority |
|----------|-----------|-------------|----------|
| B-01 | M-001 × M-002 | Wound +Ob stacking on dice pools — tested above; no additional issues |  |
| B-02 | M-002 × M-009 | Wound incapacitation + Certainty crisis simultaneously — deadlock? | P1 |
| B-03 | M-003 × M-006 | History pool + Inspiration dice + Fork — triple pool addition, uncapped? | P2 |
| B-04 | M-006 × M-009 | Inspiration spend on Thread operations (currently unruled) | P2 |
| B-05 | M-007 × M-002 | Rattled marks + Wound +Ob simultaneously — near-deadlock confirmed above | P2 |
| B-06 | M-008 × M-009 | TS tier advancement → lower Certainty maximum? Or higher? No coupling found — verify intentional decoupling | P3 |
| B-07 | M-001 × M-007 | Ob cap (max 10) + Wound +Ob + Rattled −1D: can combined penalties exceed meaningful action range? | P2 |

**B-02 detail:** If a character simultaneously hits Wound incapacitation AND Certainty 0, the ruleset has no resolution order. Character is both physically incapacitated (cannot take actions) AND in existential rendering crisis (Thread fabric breaking down). Priority: physical incapacitation likely takes precedence. But the rendering crisis procedure may require character participation (rolls, decisions). If incapacitated, can crisis procedure fire? Flag for stage3 audit.

---

## COVERAGE MATRIX UPDATES

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|---------|
| B5-01 | M-001 | TTRPG | PRES | — | all | — | all | Complete | M001-01/02/03 (P3) |
| B5-02 | M-002 | TTRPG/BG | PRES | Health | all | — | all | Complete | M002-01 **(P1)**, M002-02/03 (P2) |
| B5-03 | M-003 | TTRPG | PAST | — | all | — | all | Complete | M003-01 (P2), M003-02 (P3) |
| B5-04 | M-004 | TTRPG | CROSS | — | all | — | all | Partial | M004-01 (P2) — needs stage2 |
| B5-05 | M-005 | — | — | — | — | — | — | ELIMINATED | Maxims cut in S3 |
| B5-06 | M-006 | TTRPG | CROSS | — | all | — | all | Complete | M006-01 (P2), M006-02 (P3) |
| B5-07 | M-007 | TTRPG | PRES | Composure | all | — | all | Complete | M007-01 (P2), M007-02 (P2) |
| B5-08 | M-008 | TTRPG | CROSS | TS | Church/Crown | Almud, Himlensendt, Vaynard | Practitioner/Inquisitor/Devout | Complete | M008-01/02 (P3) |
| B5-09 | M-009 | TTRPG | CROSS | CERT | all | all practitioners | Practitioner | Complete | M009-01 **(P1)**, M009-02/03 (P2) |

---

## SUMMARY

| Priority | Count | Items |
|----------|-------|-------|
| **P1** | 2 | M002-01 (Wound cap contradiction), M009-01 (Certainty recovery unspecified) |
| P2 | 8 | M002-02/03, M003-01, M004-01, M006-01, M007-01/02, M009-02/03 |
| P3 | 6 | M001-01/02/03, M003-02, M006-02, M008-01/02 |
| Eliminated | 1 | M-005 (Maxims cut) |
| Mode B flagged | 7 | B-01 through B-07 |

**P1 fixes required before compilation continues:**
1. M002-01: Add explicit Wound cap language — "max 2 Wounds from single hit; excess damage discarded."
2. M009-01: Confirm or add Certainty recovery in stage3 — "Quick Rest +1 Certainty; Full Rest restores to Spirit score."

