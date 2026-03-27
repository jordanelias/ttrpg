# VALORIA STRESS TESTS — BATCH 5 MODE B
## Interaction Chains: B-02 through B-07
### Date: 2026-03-27 | Model: Sonnet 4.6

Source mechanics consolidated from: stage1, stage2, stage3, stage8, stage9.

**Probability reference (d10 TN7):**
- 4D: E(net)=1.33 | 6D: E(net)=2.0 | 8D: E(net)=2.67 | 10D: E(net)=3.33
- Per-die failure floor (all 1s): ~28% at 4D, ~14% at 8D

---

## B-02 — Wound Incapacitation + Certainty Crisis (Simultaneous)

**Chain:** M-002 output (incapacitation) feeding into M-009 state (Certainty 0 = Rendering Crisis)

**Setup:** A practitioner hits their Wound incapacitation threshold AND Certainty 0 in the same scene.

### Interaction Analysis

**Wound incapacitation:** Character is "unconscious or otherwise unable to act." They cannot take actions.

**Rendering Crisis (Certainty 0):** "A scene event, not a passive state. The character must resolve the dissonance narratively: revise a Belief, withdraw from Thread-active situations, or find a new framework."

**The collision:** Rendering Crisis requires conscious engagement — revising a Belief, making a decision about withdrawal, finding a new framework. These are active narrative and mechanical acts. An incapacitated character cannot perform them.

**Resolution sequence analysis:**

Option 1 — Incapacitation takes precedence: The Rendering Crisis is deferred. Character is physically incapacitated; when they regain consciousness (after Quick Rest / recovery), the Rendering Crisis fires as the first event of the next scene. This is clean but creates a narrative gap — the crisis that caused incapacitation doesn't register until after recovery.

Option 2 — Rendering Crisis fires first: The character experiences the crisis as they collapse — a final moment of existential rupture before losing consciousness. The Belief revision or framework shift happens as a (brief) internal event; when they recover they wake with that resolution already made. No action required while incapacitated.

Option 3 — Both fire simultaneously: The character is incapacitated AND in crisis. GM must handle both. Deadlock risk: if crisis resolution requires a roll (it doesn't — §4.6 says "narratively") then an incapacitated character couldn't roll. Since Rendering Crisis is narrative resolution only, Option 3 is technically feasible — GM narrates both consequences together.

**Verdict:** No deadlock (crisis is narrative, not a roll). Option 2 is most cinematically coherent and requires least clarification. **Rule needed:** "If Rendering Crisis and incapacitation occur simultaneously, the crisis resolves narratively in the moment of collapse; no action or roll required."

**Compounding consideration:** The Certainty loss triggers that could produce this situation include "witnessing a monstrous entity" (−1) and "successful Leap" (−1). A practitioner at Certainty 1 performing a Leap in combat against a monstrous entity could hit Certainty 0 AND take the damage that incapacitates them in the same round. This is a realistic scenario, not an edge case.

**Additional compounding: Intelligibility interaction.** §4.6: "Intelligibility reaching 4 or below: −1 to Certainty maximum per Intelligibility level below 5." If a character has Intelligibility 3 (−2 max Certainty) AND Spirit 3, their effective Certainty maximum = 1. One loss event = Rendering Crisis regardless of recovery attempts. This creates a permanent Rendering Crisis loop risk for high-CD practitioners.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B02-01 | P2 | Simultaneous incapacitation + Rendering Crisis has no resolution order. | Add to §4.6 or §3.8: "If Rendering Crisis triggers while the character is incapacitated, it resolves narratively in the moment of collapse with no action required. Resolution is confirmed at first moment of consciousness." |
| B02-02 | P1 | Intelligibility below 5 reduces Certainty maximum permanently. At Intelligibility 3, Spirit 3 character: max Certainty = 1. Any loss triggers crisis. Character cannot recover above max. This creates a permanent crisis loop unless Intelligibility is repaired first. | Confirm intent: is Intelligibility the "gate" that must be repaired before Certainty stabilises? If yes, add explicit statement: "Certainty cannot exceed (Spirit − Intelligibility reduction). Repair Intelligibility to restore maximum." If unintended, cap reduction at −Spirit+1 minimum (max Certainty ≥ 1 always). |
| B02-03 | P3 | A practitioner at Certainty 1 performing a combat Leap near a monstrous entity loses 2 Certainty in one round (Leap −1, entity −1). Expected scenario in late-campaign Thread-combat. No issue — intended pressure — but GMs need awareness. | Note in GM reference. |

---

## B-03 — History Pool + Inspiration + Fork (Triple Pool Addition)

**Chain:** M-003 (History pool) × M-006 (Inspiration spend) × M-003 (Fork)

**Setup:** Player uses all three simultaneously on a single roll.

### Pool Construction

Base pool: Attribute (e.g., 5) + History (e.g., 6 points = +9) = **14D**

Fork (second relevant History): **+1D** → 15D

Inspiration Spend (Spirit score, e.g., 4): **+4D bonus dice** (roll Spirit dice, add results) → effectively 15D + 4D bonus

**Total pool:** 19D effective at peak.

At 19D TN7 Ob3: E(net) ≈ 6.3. P(Overwhelming at Ob3) ≈ 92%+. **An expert character using all available tools almost guarantees Overwhelming on standard tasks.**

**Is this broken?** Let's check constraints:

- Inspiration spend: "once per scene per Inspiration." Hard cap — can't stack multiple Inspirations on one roll? Actually, re-read: "Total Inspiration value ≤ Spirit score." A character with Spirit 4 and two Inspirations (value 2 each, total = 4 = Spirit) — can both be spent on one roll? The rule says "once per scene per Inspiration" — each Inspiration can be spent once per scene. If two Inspirations are both relevant, both can fire in the same scene, but not on the same roll unless stated.

**Ambiguity confirmed:** "Once per scene per Inspiration" — does this mean one Inspiration can only be spent once per scene (restricting frequency), or that only one Inspiration spend is allowed per roll? These are different interpretations.

- Interpretation A: Each Inspiration can be spent once per scene total. Multiple Inspirations can fire on different rolls in the scene, but not twice on the same roll. **Does not prevent two Inspirations spending on the same roll** — each fires once.
- Interpretation B: Only one Inspiration spend per roll. More restrictive.

Under Interpretation A: Two Inspirations (value 3 + value 1) spending on the same roll at Spirit 4 = roll 4 bonus dice (Spirit score, not the Inspiration value? Re-read: "roll Spirit score in bonus dice"). So regardless of which Inspiration fires, the bonus is always Spirit dice. Two Inspirations spending = 2 × Spirit dice = 8D bonus on Spirit 4. That's enormous.

**P1 FINDING — B03-01: Inspiration spend mechanic is ambiguous on whether multiple Inspirations can spend on a single roll, and the bonus is Spirit dice (not Inspiration value), so stacking is severe.**

**Fork count (M003-01 revisited):** Stage2 §4.1 for Histories. The Fork rule states "a second relevant History adds +1D." No "a Fork" with cap specified. Re-read from stage1: "A Fork adds +1D to the existing roll's pool." No cap on number of Forks per roll in either stage1 or stage2. A character with 5 relevant Histories: 4 Forks = +4D. With a 14D base pool + 4 Forks + Spirit bonus dice: potentially 20D+ on a single roll.

**Combined ceiling analysis:**

Realistic peak build — Expert practitioner, Spirit 4, 3 relevant Histories, 2 Inspirations:
- Base: Attunement 5 + Thread History 9 = 14D
- Fork ×2 (other Histories): +2D → 16D
- Inspiration ×2 (Spirit 4 each): +8D → 24D
- E(net at 24D TN7): ≈ 8.0. Ob 4 → P(OW) ≈ 97%.

**Conclusion:** The combined system has no effective ceiling. Expert characters with all tools active achieve near-guaranteed Overwhelming on any task up to Ob 4. This trivialises mid-range obstacles.

**Is this a problem?** Yes and no. The system is designed so that skilled characters are excellent. Ob 5+ remains difficult. But if Ob 4 is the ceiling for most campaign challenges, the economy collapses at expert level.

**Partial mitigation:** Inspiration spend is "once per scene per Inspiration." A scene may have 3–5 meaningful rolls. A character with 2 Inspirations gets 2 bonus-dice rolls per scene. This limits frequency but not severity per-roll.

**Proposed fix pathway:** (1) Clarify Inspiration: one Inspiration spend per roll maximum. (2) Cap Forks at 2 per roll (as flagged in B5). (3) Result: max pool = base + 2 Forks + 1 Inspiration spend = base + 2 + Spirit dice. Ceiling drops to ~19D at peak build — still generous but not trivialising.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B03-01 | **P1** | Inspiration spend bonus = Spirit dice (not Inspiration value). Multiple Inspirations spending on same roll = multiple Spirit-dice rolls. Combined with Forks, pools reach 20D+, trivialising Ob 4 and below. | Clarify: (1) Maximum one Inspiration spend per roll. (2) Maximum two Forks per roll. (3) Document this explicitly in §4.3 and §4.1. |
| B03-02 | P2 | Stunt (Inspiration value 2+): adds "automatic successes equal to relevant attribute." Attribute 5 + Stunt = +5 automatic successes before rolling. Combined with high pool: Ob 5 near-guaranteed. | Stunt auto-successes should likely be capped at Inspiration value, not full attribute. EDITORIAL: confirm intended cap. |

---

## B-04 — Inspiration Spend on Thread Operations

**Chain:** M-006 (Inspiration spend) × Thread ops (stage3)

**Setup:** Practitioner spending Inspiration on a Leap or Weaving roll.

### Analysis

Stage2 §4.3: No Thread operation restriction stated. Stage1 §1.7 (Momentum): explicit restriction "cannot be spent on Thread operation rolls." Stage2 §4.3 (Inspiration): no equivalent restriction.

This is not an oversight — the two economies (Momentum vs Inspiration) are structurally different:
- Momentum: tactical advantage, resets each session, anyone can accumulate
- Inspiration: character identity, costs investment to build, thematically tied to the character's relationships and values

**Case for allowing Inspiration on Thread ops:** A practitioner whose Thread work is driven by a named focus (e.g., "protecting my sister" as an Inspiration) spending that Inspiration on a Weaving to save her is thematically coherent. The mechanics should reflect narrative investment.

**Case against:** Thread operations already have their own pool amplification (TPS, Collective ops, Forks). Adding Spirit dice on top creates the same stacking problem as B-03. At peak: 16D Thread pool + 4D Spirit bonus = 20D. Leap Ob is typically 2–3. P(OW at Ob3, 20D) ≈ 99%.

**Decision needed:** If Inspiration can apply to Thread ops, it should be: one Inspiration per roll, and only when the focus is directly narratively relevant to the specific operation (not just "I'm a practitioner").

**Verdict:** The Momentum restriction likely exists to prevent tactical trivialisation. The same logic applies to Thread ops — they're already resource-expensive (Certainty, TD, TT). Adding Inspiration on top removes the tension. **Recommend: Inspiration may not be spent on Thread operation rolls, same as Momentum.**

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B04-01 | P2 | Inspiration spend on Thread operations unruled. If allowed, combined with TPS and Forks, Thread pools trivialise at expert level. | Add to §4.3: "Inspiration may not be spent on Thread operation rolls (Leap, Weaving, Pulling, Forced Resolution, Diagnosis, Past-Oriented Pulling). The same restriction applies as Momentum (§1.7)." |

---

## B-05 — Rattled Marks + Wound +Ob (Combined Degradation)

**Chain:** M-007 (Rattled condition) × M-002 (Wound +Ob)

**Setup:** Character is both wounded and Rattled mid-scene.

### Combined Penalty Analysis

**Wounds: +1 Ob per Wound (all rolls).**
**Rattled: −1D per mark (social rolls specifically, per stage9 fix).**

*Character: Endurance 3 (incap at 2 Wounds), Spirit 3, Presence 4, History 6 points = 8D social pool.*

| State | Social pool | Effective Ob (vs Ob 2 base) | P(OW+Suc) |
|-------|-------------|---------------------------|-----------|
| Clean | 8D | Ob 2 | 71% |
| 1 Wound | 8D | Ob 3 | 52% |
| 1 Wound + 1 Rattled | 7D | Ob 3 | 46% |
| 2 Wounds | 8D | Ob 4 | 34% |
| 2 Wounds + 1 Rattled | 7D | Ob 4 | 26% |
| 2 Wounds + 2 Rattled | 6D | Ob 4 | 19% |

**At 2 Wounds + 2 Rattled marks:** P(Success or better at Ob 2 social task) = 19%. The character is near-dysfunctional in both physical and social domains. For Endurance 3 (incap at 2 Wounds), this is the terminal state before incapacitation.

**Is this a deadlock?** Character can still act — 19% success rate is low but nonzero. They can retreat, attempt minimal actions, or accept Partial outcomes. No deadlock.

**Key interaction: Do Wounds impose +Ob on social rolls too?** Yes — "+1 Ob per Wound (cumulative, all roll types)." Wounds affect everything: combat, social, Thread. Rattled is social-specific. So a wounded, Rattled character in a Debate is at both −D and +Ob simultaneously. The compounding is severe but terminates at incapacitation, which is the intended design pressure.

**Cross-mode consideration (Hybrid):** In hybrid mode, a character could be physically incapacitated (mass combat wound) while still participating in a social scene (their faction's negotiations). Can an incapacitated character participate in social scenes? Ruleset does not specify. **P2 gap.**

**Rattled stacking confirmation (B5-M007-02 follow-up):** Stage2 §4.11 (Composure and Social Damage) — need to check for explicit stacking rule.

Checking stage2 L314–333:

Stage2 §4.11 is present but the content wasn't fully printed. Key data from stage9 fix context: "−1D to all social rolls per Rattled mark." This confirms Rattled is stackable (marks accumulate) and each mark = −1D. The stacking source: each time Composure drains to 0 in a scene, a new Rattled mark is added and Composure resets. A character in a prolonged social conflict can accumulate 2–3 Rattled marks if their Composure keeps depleting.

**Composure reset confirmation:** Composure = Presence + 6. At Presence 3: Composure 9. In a single scene with an aggressive opponent rolling large Cognition pools: expected Composure strain per exchange ≈ 2–3 strain. Composure 9 / 3 strain = ~3 resets possible per scene (if not terminated by Unmask). That's 3 Rattled marks and −3D on all social rolls. Combined with 2 Wounds (+2 Ob): Social pool effectively 5D at Ob 4 → P(Success) ≈ 6%.

**This is extreme but self-correcting:** The Unmask mechanic exists to exit social scenes. A character accumulating Rattled marks should Unmask, resetting the scene. If they don't (forced scene continuation), the degradation is intentional punishment. No fix needed — but GM guidance on Unmask timing is critical.

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B05-01 | P2 | Incapacitated character's participation in social scenes (especially hybrid mode) is unruled. Can a physically incapacitated character still Debate? | Add to §9 or §12 (hybrid): "A physically incapacitated character may participate in social exchanges as a witness or passive party but cannot initiate social actions or make social rolls until recovering to at least 1 Health." |
| B05-02 | P3 | Three+ Rattled marks in a single scene is theoretically possible (Composure Presence 3 = 9, aggressive 3-reset drain). Creates −3D on all social rolls. Combined with Wounds: near-zero success rate. Intentional pressure but GMs need Unmask awareness. | GM reference note. |

---

## B-06 — TS Tier Advancement × Certainty Maximum (Decoupling Check)

**Chain:** M-008 (TS tier growth) × M-009 (Certainty track)

**Setup:** Does TS advancement affect Certainty maximum or vice versa?

### Analysis

**From stage2 §4.6:** "Certainty maximum = Spirit score." TS tiers do not modify Certainty maximum. Taint levels above 6 do (−1 Certainty max per Taint level above 6, per §4.6 from stage3 context).

**Intelligibility (§4.5) does affect Certainty maximum:** −1 max per Intelligibility level below 5. This is the CD/Coherence Degradation coupling.

**TS advancement pathway:**

TS growth triggers include CE exposure → Spirit check. CE accumulation is from Inquisitor observation of Thread operations. The practitioner's Certainty does not gate TS growth — TS grows from external exposure events, not internal Certainty state.

**Critical question:** Can a practitioner at Certainty 0 perform Thread operations? 

§4.6 Rendering Crisis: "must resolve the dissonance narratively — revise a Belief, withdraw from Thread-active situations, or find a new framework." This is a required narrative action, not a mechanical lock. The ruleset says they "must" do this, but doesn't state they mechanically cannot operate.

**This is a gap:** If Rendering Crisis doesn't mechanically prevent Thread operations, a practitioner could theoretically continue operating at Certainty 0 indefinitely. The rule says "must resolve" but imposes no mechanical enforcement.

**Intent check:** The Rendering Crisis is the primary character development mechanism for practitioners. It should create genuine pressure to stop and engage. A mechanical lock (cannot perform Thread ops while in Rendering Crisis) would enforce this, but may be too heavy-handed for a narrative game.

**Recommended approach:** Add a mechanical cost for ignoring Rendering Crisis: each Thread operation performed while in Rendering Crisis causes +1D Coherence Degradation. This creates pressure without hard-locking the character, and produces narrative consequence (deteriorating Coherence) for practitioners who "push through" the crisis.

**TS ↔ Certainty directional coupling confirmed:** TS growth is driven by exposure events (CE, Originary Locks, Discovery Events) — not by Certainty level. Certainty depletion is a parallel track measuring existential exposure, not TS accumulation. They are co-indicators of Thread engagement, not causally linked. This is correct per P-01 (inseparability) — both tracks move together because both track the practitioner's engagement with the Thread, not because one drives the other. **Intentional decoupling confirmed.**

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B06-01 | P2 | Rendering Crisis (Certainty 0) has no mechanical enforcement — "must resolve" is advisory. Practitioners can continue Thread operations with no mechanical consequence beyond the crisis state. | Add: "Each Thread operation performed while in Rendering Crisis (Certainty 0) causes +1D Coherence Degradation immediately on resolution, regardless of outcome." |
| B06-02 | P3 | Taint 7+ reduces Certainty maximum (−1 per level above 6). At Taint 10: max Certainty = Spirit − 4. Spirit 3 practitioner at Taint 10: max Certainty = −1, clamped to 0. Permanent Rendering Crisis. | Confirm this is intended as the Taint terminal state. If so, document explicitly: "Taint 10 + Spirit ≤ 4 = permanent Rendering Crisis. Recovery requires Taint reduction below (Spirit − 3) first." |

---

## B-07 — Ob Cap × Wound +Ob × Rattled −1D (Combined Penalty Ceiling)

**Chain:** M-001 (Ob mechanics) × M-002 (Wound +Ob) × M-007 (Rattled −1D)

**Setup:** Can combined penalties reduce a character to a state where no meaningful action is possible?

### Maximum Combined Penalty Analysis

**Maximum Wound penalty before incapacitation:**
- Endurance 4–5: 3 Wounds → +3 Ob (incapacitated at 3 Wounds — these penalties apply just before threshold)
- Endurance 6–7: 4 Wounds → +4 Ob

**Maximum Rattled (social only):** Theoretically unlimited marks per scene, but realistically 3 marks before the scene terminates. −3D.

**Ob cap:** 10 maximum regardless of stacking.

**Scenario: 3 Wounds + 3 Rattled marks + facing Ob 4 social task**

Character: Presence 4, History 6 = 9D social pool.
- −3D (Rattled) → 6D
- +3 Ob (Wounds) on Ob 4 base → effective Ob 7

6D vs Ob 7 TN7: P(Overwhelming at Ob7) ≈ 0%. P(Success at Ob7) ≈ 0%. P(Partial) = net > 0 but < 7 — at 6D, E(net) = 2.0. P(net ≥ 7) ≈ 0.1%. P(net > 0) ≈ 80%.

**Result: near-100% Partial or worse at Ob 7.** The character cannot succeed at their intended goal but can produce complications. They are not deadlocked (they can still roll) but success is mechanically impossible.

**Is this a deadlock problem?** Partial outcomes still move the story forward (fail-forward design). A character in this state can: accept Partial outcomes (goal achieved with complication), attempt lower-Ob tasks (Ob 1–2 would be Ob 4–5 after Wounds — marginal success possible), or use Momentum/Inspiration if available.

**Ob cap check:** At 4 Wounds + Ob 4 base → effective Ob 8 (under cap). At 4 Wounds + Ob 7 base → Ob 11 → capped at 10. Cap functions. But at Ob 10, the ruleset states "Partial requires net ≥ 5." 6D pool → P(net ≥ 5) ≈ 5%. Effectively impossible.

**True deadlock test:** Can combined penalties make a Partial outcome impossible? Partial requires net > 0. P(net ≤ 0) at 6D TN7 ≈ 20%. So even in the worst combined state, 80% of rolls produce a Partial or better. **No true deadlock** — the fail-forward design prevents it.

**Minimum Pool protection:** Stage1 §3.4 specifies minimum Combat Pool = 5 dice (with −1D effective at low values). No equivalent minimum for social or Thread pools. A character with Presence 1 + 0 History − 3D Rattled = −2D, which is undefined. **P1 gap: negative pool is unhandled.**

### Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| B07-01 | **P1** | No minimum pool floor for non-combat pools. Presence 1, no History, 3 Rattled marks = 3D − 3D = 0D or negative. Rule undefined. | Add to §4.1 or §1.1: "Minimum pool for any roll: 1D. No combination of penalties may reduce a pool below 1D. Additional penalties beyond 1D pool are ignored but Ob continues to apply normally." |
| B07-02 | P2 | At 4+ Wounds + Ob 3+ base + Ob cap at 10: Partial requires net ≥ 5 (from Ob 10 exception rule). At low pools (5–6D), P(net ≥ 5) ≈ 5–15%. Terminal state functionally worse than true deadlock — character can barely produce Partials. | GM guidance: characters in this state should be given narrative off-ramps (surrender, incapacitation, extraction) rather than being forced to keep rolling. No mechanical fix needed — narrative management. |

---

## CONSOLIDATED FINDINGS — MODE B

| ID | Priority | Mechanic Chain | Finding | Fix Required |
|----|----------|---------------|---------|-------------|
| B02-01 | P2 | M-002 × M-009 | Simultaneous incapacitation + Rendering Crisis has no resolution order | Add rule: crisis resolves narratively in moment of collapse |
| B02-02 | **P1** | M-002 × M-009 × Intelligibility | Intelligibility reduction of Certainty max + Spirit 3 = permanent crisis loop | Confirm intent; if intentional, document explicitly |
| B02-03 | P3 | M-002 × M-009 | Combat Leap near entity = 2 Certainty loss in one round. Expected late-campaign scenario | GM note only |
| B03-01 | **P1** | M-003 × M-006 | Multiple Inspirations + Forks = 20D+ pools, trivialise Ob 4 and below | Max 1 Inspiration spend per roll; max 2 Forks per roll |
| B03-02 | P2 | M-006 Stunt | Stunt auto-successes = full attribute value. May be too generous combined with high pools | EDITORIAL: confirm Stunt auto-success cap = Inspiration value or attribute |
| B04-01 | P2 | M-006 × Thread ops | Inspiration spend on Thread ops unruled; if allowed, stacks severely | Explicitly prohibit: same restriction as Momentum |
| B05-01 | P2 | M-007 × M-002 | Incapacitated character in social scene (hybrid) unruled | Add: incapacitated = no social rolls until 1+ Health recovered |
| B05-02 | P3 | M-007 × M-002 | 3+ Rattled marks theoretically possible; near-zero success rate | GM Unmask awareness note |
| B06-01 | P2 | M-008 × M-009 | Rendering Crisis (Certainty 0) has no mechanical enforcement | Thread op during crisis = +1D CD |
| B06-02 | P3 | M-008 × M-009 | Taint 10 + Spirit ≤ 4 = permanent Rendering Crisis | Confirm as intended terminal Taint state |
| B07-01 | **P1** | M-001 × M-007 | Negative pool (non-combat) is unhandled. Presence 1 + 3 Rattled = 0D or negative | Minimum pool = 1D for all rolls |
| B07-02 | P2 | M-001 × M-002 × M-007 | Terminal wound+Rattled state: Partial near-impossible at Ob10 | Narrative off-ramp guidance in GM tools |

**P1 summary (Mode B):**
1. B02-02: Intelligibility → permanent Certainty max reduction loop
2. B03-01: Pool inflation via stacked Inspirations + Forks (no ceiling)
3. B07-01: Negative pool floor undefined for non-combat rolls

**Editorial decision required:**
- B03-02: Stunt auto-success cap (Inspiration value vs full attribute)

---

## CUMULATIVE P1 REGISTER (Batches 5A + 5B)

| ID | Finding | Status |
|----|---------|--------|
| M002-01 | Wound cap contradicts 3× formula | **FIXED** (stage1) |
| M009-01 | Certainty recovery unspecified | **FIXED** (stage2/3, Spirit Ob2) |
| B02-02 | Intelligibility + Certainty max = permanent crisis loop | Open |
| B03-01 | Pool inflation: Inspirations + Forks uncapped | Open |
| B07-01 | Negative pool floor unhandled (non-combat) | Open |

