# VALORIA — FIELDWORK SYSTEM v1.1 — §5 Socializing
## Parent: designs/scene/fieldwork_v30.md
## Status: DESIGN — canonical subsystem file. PP-632 applied 2026-04-13.
## Mode applicability: TTRPG / Hybrid / Board Game / Godot

## §5 SOCIALIZING

### §5.1 Disposition Track

Every named NPC holds a **Disposition** toward each player character. Disposition measures the NPC's willingness to engage, share, and cooperate — outside of formal Contest structures.

**Disposition range: −4 to floor(Bonds/2)+1.**

| Bonds | Max Disposition |
|-------|----------------|
| 1 | +1 |
| 2–3 | +2 |
| 4–5 | +3 |
| 6–7 | +4 |

**Ob rule:** For all social fieldwork actions, **effective Ob = max(1, base Ob − Disposition)**. Negative Disposition adds difficulty directly; positive Disposition reduces it directly. Floor of 1 always applies. Impress and Gift/Bribe are exempt (see §5.2).

| Value | Label | Information Gate |
|-------|-------|-----------------|
| −4 | Hostile | Refuses interaction. Violence possible. |
| −3 | Suspicious | Minimal cooperation. |
| −2 | Wary | Guarded. Surface information only. |
| −1 | Cool | Cautious engagement. Surface information. |
| 0 | Neutral | Standard interaction. Surface information. |
| +1 | Interested | Willing. Settled information accessible. |
| +2 | Friendly | Volunteers. Hidden information accessible. |
| +3 | Trusting | Shares private knowledge. Buried information accessible. |
| +4 | Devoted | Takes personal risk. Liminal information accessible (Knot threshold at Bonds 6–7). |

**Starting Disposition from lifepath:** For each relevant lifepath element — birthplace, upbringing, occupation, lineage — assign ±0.5 based on how that element aligns or conflicts with the NPC's faction, culture, and role. Sum all contributions, take floor. Clamp to [−4, floor(Bonds/2)+1].

Lifepath guidance (±0.5 increments):
- Same birthplace or cultural region: +0.5
- Same occupation, guild, or trade tradition: +0.5
- Same faction (loose affiliation): +0.5 / (full member): +1
- Rival faction: −0.5 / (actively opposed): −1
- Opposing lineage or family conflict: −0.5
- Shared formative history (war, disaster, institution): +0.5

**Disposition is asymmetric:** NPC A's Disposition toward PC B ≠ NPC A's Disposition toward PC C. Each relationship is tracked independently.

**Disposition decay:** Disposition > +2 decays by −1 per season if not maintained (no social action directed at this NPC that season). Disposition ≤ +2 is stable indefinitely.

**Disposition ≤ −3 recovery:** Requires a significant narrative event (rescue, shared danger, public vindication) before social actions can be attempted.

---

### §5.2 Social Actions (Non-Contest)

Social actions outside formal contests use the fieldwork pool. A social action represents one meaningful interaction within a scene.

**Not all social interaction is a social action.** Unrolled conversation — where no specific outcome is sought — is roleplay. The system models purposeful social engagement, not all human contact.

**Effective Ob = max(1, base Ob − Disposition)** applies to all actions below except Impress and Gift/Bribe.

| Action | Primary Attribute | Base Ob | Effect |
|--------|-------------------|---------|--------|
| Read | Attunement | 1 (Surface) / 2 (Hidden) / 3 (Buried) | Determine NPC's current Disposition, one Belief, emotional state, or hidden motivation. Degree determines specificity. |
| Converse | Charisma | 2 | Shift Disposition. Gather Settled-depth information. |
| Connect | Bonds | 3 | Deepen relationship. Requires Disposition ≥ 0. Unlocks higher Disposition levels. Also the Knot Formation roll (§5.6). |
| Impress | Charisma | floor(NPC Cognition / 2) + 1 | Make favourable impression at first meeting. Sets initial Disposition above default. **Disposition not subtracted** — this is pre-relationship; Disposition is what Impress produces. |
| Rumour | Charisma | 2 (tavern/market) / 3 (hostile territory) | Gather one piece of unverified information. Reliability unknown. |
| Negotiate | Attunement | floor(NPC's highest relevant stat / 2) + 1 | Reach informal agreement (below Contest threshold — see §5.7). |
| Gift/Bribe | — (no roll) | — | +1 Disposition before first social action. Narrative value required. One per NPC per season. **Not at Disposition ≤ −3** (hostile or suspicious NPCs reject gifts from strangers). |

**Disposition shift by degree:**

| Degree | Disposition Change | Additional |
|--------|-------------------|------------|
| Failure | −1 | Exposure +1. Cannot attempt same action type with this NPC for remainder of scene. |
| Partial | +0 (contact maintained) | — |
| Success | +1 | One piece of information at the new Disposition's gate level. |
| Overwhelming | +2 | Information + NPC volunteers something unsolicited. +1 Momentum if Belief-aligned. |

---

### §5.3 Sincerity Gate

If a character's stated Belief contradicts genuine engagement with the NPC — the character is instrumentally building trust to extract information — the GM may call a **Sincerity Check** when the player declares a Connect or Converse action.

**Sincerity Check:** Spirit, TN 7, Ob 1.

| Degree | Effect |
|--------|--------|
| Failure | The NPC senses the instrumentality. Disposition does not increase; may decrease by −1. |
| Partial | The NPC does not notice, but the character feels the dissonance. No Momentum from this interaction. |
| Success | The character manages genuine engagement despite instrumental intent. Normal result. |
| Overwhelming | The instrumentality dissolves — the character discovers genuine interest. Normal result + mark potential Belief revision. |

The Sincerity Gate is not a punishment for strategic play. It is the NPC's rendering of the character's intentions. Use sparingly — only when the player's approach is clearly at odds with their character's Beliefs.

---

### §5.4 Information Gates

| Access Method | Depth 0 (Surface) | Depth 1 (Settled) | Depth 2 (Hidden) | Depth 3 (Buried) | Depth 4 (Liminal) |
|--------------|-------|--------|--------|--------|---------| 
| Exploration | Auto | Cognition ≥ 2 | Cognition ≥ 3 | TS ≥ 10 | TS ≥ 30 |
| Investigation | Auto | Ob 1 | Ob 2 | Ob 3 + TS ≥ 10 | Ob 5 + TS ≥ 30 |
| Socializing | Any Disposition | Disposition ≥ 0 | Disposition ≥ +1 | Disposition ≥ +2 | Disposition ≥ floor(Bonds/2)+1 |

---

### §5.5 Socializing and Beliefs

- **Belief-aligned social success:** +1 Momentum (cap 4). Counts as Belief achievement.
- **Belief-challenging social success:** No Momentum; GM marks potential Belief revision opportunity.
- **Social action that requires betraying a Belief:** Certainty pressure. Resolves at session end.

---

### §5.6 Knot Integration

**Ontological basis:** Knots are not Thread operations. They are constitutive relational bonds — being-with-others (Mitsein) in the world. Any character can form Knots, regardless of Thread Sensitivity. Thread practitioners can work *through* Knots (remote Thread-Read §2.6, relational contagion P-12), but the Knot itself is an ontological fact of the relationship, not a Thread construct.

**Knot Pool:** (Bonds × 2) + 3 points total.

**Knot Tiers:**

| Tier | Point Cost |
|------|-----------|
| Close | 5 |
| Medium | 2 |
| Loose | 1 |

**Maximum Knot count:** floor(Bonds/2)+1 (same formula as Disposition ceiling — Bonds governs relational depth in both directions).

**Pool by Bonds:**

| Bonds | Points | Max Knots | Optimal allocation |
|-------|--------|-----------|--------------------|
| 1 | 5 | 1 | 1 Close (exactly full) |
| 2 | 7 | 2 | 1 Close + 1 Medium (exactly full) |
| 3 | 9 | 2 | 1 Close + 1 Medium + 2 unspent |
| 4 | 11 | 3 | 2 Close + 1 Loose (exactly full) |
| 5 | 13 | 3 | 2 Close + 1 Medium + 1 unspent |
| 6 | 15 | 4 | 3 Close (points full; 1 slot unused) |
| 7 | 17 | 4 | 3 Close + 1 Medium (exactly full) |

**Unspent points** are live capacity — unrealised relational potential. Not a resource to bank. Available for future Knot formation as relationships develop.

**Formation — three conditions must all be met:**

1. Relationship at max Disposition for the character: floor(Bonds/2)+1.
2. Available points in pool ≥ tier cost.
3. **Knot Formation scene:** one dedicated Connect roll, base Ob = tier (Loose 1 / Medium 2 / Close 3), with Disposition subtracted as normal (effective Ob = max(1, tier − Disposition), but since Disposition is already at max, effective Ob = 1 for Loose, max(1, 2 − max) for Medium, max(1, 3 − max) for Close).

| Degree | Outcome |
|--------|---------|
| Failure | The moment doesn't land. Disposition holds at max. Retryable next season. No points spent. |
| Partial | Knot forms at one tier below intended. Points for lower tier spent. |
| Success | Knot forms at intended tier. Points spent. |
| Overwhelming | Knot forms at intended tier. +1 Momentum. |

**Knot effects:**
- Automatic Disposition maintenance (no seasonal decay at any level while Knotted)
- +1D on all social actions with the Knot partner
- Shared Composure buffer (per social_contest_v30.md §4 Step 6)
- Relational contagion (P-12): Thread-shift propagates through Knots for Thread practitioners

**Breaking:**

*Rupture (betrayal, deliberate severance):* Points return to pool. Disposition → −4 (floor). Composure damage = tier cost (Close: 5, Medium: 2, Loose: 1 — damage absorbed by Composure track; overflow to Rattled marks). The wound is in the relationship.

**Simultaneous Rupture cap (PP-633):** When multiple Knots rupture in the same scene, total Composure damage from Rupture is capped at floor(Composure × 0.75) rounded down, minimum = the highest single-tier cost among rupturing Knots. Prevents catastrophic stacking incapacitation while preserving severity. Disposition → −4 and all non-Composure consequences apply per Knot regardless of cap.

*Loss (death, permanent absence):* Points return to pool. Disposition track removed — the relationship no longer exists as a social object. Coherence −1 (layer-2 self-rendering is disrupted when a constitutive being-with is removed from the world; mandatory per P-12 and Amendment 01 §three-layer being-persistence). Composure damage = tier cost. The wound is in the self.

The distinction matters: rupture leaves a wound in the relationship. Loss leaves a wound in the self.

---

### §5.7 Contest Escalation and Negotiate Boundary

**Negotiate** applies only when: (a) parties share a goal but disagree on method, or (b) the outcome is not consequential enough for full Contest. If the situation meets Contest initiation conditions (social_contest_v30.md §1), the interaction is a Contest. The GM does not offer a choice — the situation's structure determines the mechanic.

Escalation preserves Disposition, applied as Piety Track offset: ±1 per 2 Disposition points, capped at ±2.

---

### §5.8 Niflhel Social Toolkit Extension

- **Available:** Read, Connect, Negotiate. One-on-one only.
- **Unavailable:** Impress, Rumour.
- **Exposure modifier:** +2 per social action.
- **Primary pool:** Attunement (all Niflhel social actions, per Contest §9.7).
- **Thread Insight (TS ≥ 30 only):** Free Thread-Read before Negotiate or Read. Base Ob = floor(target TS / 30, round up), min 1. Does not consume a scene action; generates +1 Exposure.
