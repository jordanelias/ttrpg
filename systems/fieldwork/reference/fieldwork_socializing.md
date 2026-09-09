# VALORIA — FIELDWORK SYSTEM v1.1 — §5 Socializing
## Parent: designs/scene/fieldwork_v30.md
## Status: DESIGN — canonical subsystem file. PP-632 applied 2026-04-13.
## Mode applicability: TTRPG / Hybrid / Board Game / Godot

## §5 SOCIALIZING

### §5.1 Disposition Track

Every named NPC holds a **Disposition** toward each player character. Disposition measures the NPC's willingness to engage, share, and cooperate — outside of formal Contest structures.

**Disposition range: −5 to +5** (flat; NOT Bonds-capped — ED-912). Canonical spec: fieldwork_v30 §5.1.

**Ob rule:** stepped table (ED-912 — replaces the old `max(1, base Ob − Disposition)` direct subtraction). Floor Ob 1 always applies. Impress and Gift/Bribe are exempt (see §5.2).

| Value | Label | Ob mod | Information Gate |
|-------|-------|--------|-----------------|
| −5 | Hateful | +5 | Active enmity. Will harm given opportunity. |
| −4 | Hostile | +4 | Refuses interaction. Violence possible. |
| −3 | Antagonistic | +3 | Openly uncooperative. Obstructs. |
| −2 | Suspicious | +2 | Minimal cooperation. |
| −1 | Wary | +1 | Guarded. Surface information only. |
| 0 | Neutral | 0 | Standard interaction. Surface information. |
| +1 | Warm | −1 | Willing. Settled information accessible. |
| +2 | Friendly | −1 | Volunteers. Hidden information accessible. |
| +3 | Trusting | −2 | Shares private knowledge. Buried information accessible. |
| +4 | Devoted | −2 | Takes personal risk. Liminal information accessible. |
| +5 | Bonded | −3 | Knot candidate (Bonds ≥ 5 + TS ≥ 30). Deepest access. |

**Starting Disposition from lifepath:** For each relevant lifepath element — birthplace, upbringing, occupation, lineage — assign ±0.5 based on how that element aligns or conflicts with the NPC's faction, culture, and role. Sum all contributions, take floor. Clamp to [−5, +5] (ED-912).

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
| Socializing | Any Disposition | Disposition ≥ +1 | Disposition ≥ +2 | Disposition ≥ +3 | Disposition ≥ +4 |

---

### §5.5 Socializing and Beliefs

- **Belief-aligned social success:** +1 Momentum (cap 4). Counts as Belief achievement.
- **Belief-challenging social success:** No Momentum; GM marks potential Belief revision opportunity.
- **Social action that requires betraying a Belief:** Truth pressure. Resolves at session end.

---

### §5.6 Knot Integration

**Ontological basis:** Knots are constitutive relational bonds — being-with-others (Mitsein) in the world, **Thread-bound** (TS ≥ 30 required for at least one party — ED-912, supersedes the old "any character"). Thread practitioners work *through* Knots (remote Thread-Read §2.6, relational contagion P-12), but the Knot itself is an ontological fact of the relationship.

**Prerequisites (all required):** Disposition **+5** (Bonded) · (PC or NPC) TS ≥ 30 · PC **Bonds ≥ 5** · Knot count < floor(Bonds/2)+1 · no existing Knot with this NPC.

**Maximum Knot count:** floor(Bonds/2)+1. Bonds is the relational *capacity* gate; it no longer caps Disposition (ED-912).

**Tiers: Distant / Close** (2-tier). A Distant Knot is upgradeable to Close via 3 further social scenes at Disposition +5 (knots_v30 §3.3).

**Formation:** Spirit pool (Spirit × 2) vs TN 7, **Ob 2**.

| Degree | Outcome |
|--------|---------|
| Failure | The moment doesn't land. Disposition holds at +5. Retryable next season. |
| Partial | No Knot forms. Disposition holds at +5. |
| Success | **Distant** Knot forms (strain starts at 0). |
| Overwhelming | **Close** Knot forms directly (strain starts at −2, the Close buffer). +1 Momentum. |

**Strain — bidirectional −5..+5 bond-strain gauge** (ED-912; replaces the point-cost model). Distant −2..+5 (start 0); Close −5..+5 (start −2). +1 strain per stress-use (remote Thread-Read, Composure buffer, counsel retrieval, sustained Disposition < +3 for 2 seasons). **Rupture at +5.** Reinforcement: −1/season at Accounting when Disposition ≥ +3 and no strain added. **−5 = Tempered** (Close — absorbs the next rupture trigger once, then resets to 0).

**Knot effects:**
- Automatic Disposition maintenance (no seasonal decay while Knotted)
- +1D on all social actions with the Knot partner
- Shared Composure buffer (per social_contest_v30.md §4 Step 6)
- Relational contagion (P-12): Thread-shift propagates through Knots for Thread practitioners

**Breaking:**

*Rupture (strain reaches +5, OR betrayal — public citation of private counsel):* Disposition → **−3**; **4 Composure** damage (absorbed by the Composure track; overflow to Rattled marks). The wound is in the relationship.

**Simultaneous Rupture cap (PP-633):** When multiple Knots rupture in the same scene, total Composure damage is capped at floor(Composure × 0.75) rounded down, minimum = 4 (one break). Disposition → −3 and all non-Composure consequences apply per Knot regardless of cap.

*Loss (death, permanent absence):* Knot removed — the relationship no longer exists as a social object. Coherence −1 (layer-2 self-rendering is disrupted when a constitutive being-with is removed from the world; mandatory per P-12 and Amendment 01 §three-layer being-persistence). **4 Composure** damage. The wound is in the self.

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
