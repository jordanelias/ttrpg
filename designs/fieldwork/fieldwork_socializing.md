# VALORIA — FIELDWORK SYSTEM v1.1 — §5 Socializing
## Parent: designs/fieldwork/fieldwork_design_v1.md
## Status: DESIGN — canonical subsystem file. See parent for full cross-references.
## Mode applicability: TTRPG / Hybrid / Board Game / Godot

## §5 SOCIALIZING

### §5.1 Disposition Track

Every named NPC holds a **Disposition** toward each player character. Disposition measures the NPC's willingness to engage, share, and cooperate — outside of formal Contest structures.

**Disposition range: −3 to +5.**

| Value | Label | Effect on Social Ob | Information Gate |
|-------|-------|---------------------|-----------------|
| −3 | Hostile | +3 Ob | Refuses interaction. Violence possible. |
| −2 | Suspicious | +2 Ob | Minimal cooperation. Monosyllabic. |
| −1 | Wary | +1 Ob | Guarded responses. Surface information only. |
| 0 | Neutral | +0 Ob | Standard interaction. Surface information. |
| +1 | Interested | +0 Ob | Willing to engage. Settled information accessible. |
| +2 | Friendly | −1 Ob | Volunteers information. Hidden information accessible. |
| +3 | Trusting | −1 Ob | Shares private knowledge. Buried information accessible. |
| +4 | Devoted | −2 Ob | Takes personal risk for the character. Liminal information accessible. |
| +5 | Bonded | −2 Ob | Knot candidate. Deepest personal access. |

**Starting Disposition** is determined by faction alignment, social context, and NPC personality:
- Same faction: +1
- Allied faction: 0
- Neutral faction: 0 or −1
- Rival faction: −1 or −2
- Hostile faction: −2 or −3
- Personal factors (Beliefs, shared History, prior interaction): ±1 per factor (GM discretion)
- Reputation (per core engine): Reputation 3+ in character's favour: +1 starting Disposition

**Disposition is asymmetric:** NPC A's Disposition toward PC B ≠ NPC A's Disposition toward PC C. Each relationship is tracked independently.

### §5.2 Social Actions (Non-Contest)

Social actions outside formal contests use the fieldwork pool. These are individual rolls, not the exchange structure of social_contest_system_v2.md. A social action represents one meaningful interaction within a scene.

**Not all social interaction is a social action.** Unrolled conversation — where no specific outcome is sought — is roleplay. It may inform the GM's Disposition adjustments but does not require a roll. Characters sharing a meal, swapping stories, or commiserating do not need mechanical resolution. The system models purposeful social engagement, not all human contact.

| Action | Primary Attribute | Ob | Effect |
|--------|-------------------|-----|--------|
| Read | Attunement | 1 (Surface); 2 (Hidden); 3 (Buried) | Determine NPC's current Disposition, one Belief, emotional state, or hidden motivation. Degree determines specificity. |
| Converse | Charisma | 1 + Disposition modifier (negative Disposition increases Ob) | Shift Disposition. Gather Settled-depth information. |
| Connect | Bonds | 2 + depth of relationship sought | Deepen relationship. Requires Disposition +1 or higher. Unlock higher Disposition levels. |
| Impress | Charisma | floor(NPC Cognition / 2) + 1 | Make favourable impression on first meeting. Sets initial Disposition higher than default. |
| Rumour | Charisma | 1 (in tavern/market); 2 (in hostile territory) | Gather one piece of unverified information. Reliability unknown. |
| Negotiate | Attunement | floor(NPC's highest relevant stat / 2) + 1 | Reach informal agreement (below Contest threshold — see §5.7). |
| Gift/Bribe | — (no roll) | — | Improve starting Disposition by +1 before first social action. Requires a gift of narrative value (GM judgment) or an expenditure of personal resources. One gift per NPC per season. Does not work at Disposition ≤ −2 (Hostile/Suspicious NPCs reject gifts from strangers). |

**Disposition shift by degree:**

| Degree | Disposition Change | Additional |
|--------|-------------------|------------|
| Failure | −1 (social misstep; NPC withdraws) | Exposure +1. Cannot attempt same action type with this NPC for remainder of scene. |
| Partial | +0 (contact maintained, no ground gained) | — |
| Success | +1 | One piece of information at the new Disposition's gate level. |
| Overwhelming | +2 | Information + NPC volunteers something unsolicited. +1 Momentum if Belief-aligned. |

**Disposition decay:** Disposition ≥ +3 decays by −1 per season if not maintained (no social action directed at this NPC). Disposition ≤ +2 is stable indefinitely. This reflects the difference between casual acquaintance (stable) and deep trust (requires ongoing investment).

**Disposition ≤ −2 recovery:** Requires a significant narrative event (gift, rescue, shared danger, public vindication) before social actions can be attempted. A character cannot talk their way out of Hostile through Charisma alone.

### §5.3 Sincerity Gate

If a character's stated Belief contradicts genuine engagement with the NPC — the character is instrumentally building trust to extract information — the GM may call a **Sincerity Check** when the player declares a Connect or Converse action.

**Sincerity Check:** Spirit, TN 7, Ob 1.

| Degree | Effect |
|--------|--------|
| Failure | The NPC senses the instrumentality. Disposition does not increase; may decrease by −1. "Something about the way you ask..." |
| Partial | The NPC does not notice, but the character feels the dissonance. No Momentum from this interaction, even if Belief-aligned. |
| Success | The character manages genuine engagement despite instrumental intent. Normal result. |
| Overwhelming | The attempt at instrumentality dissolves — the character discovers genuine interest. Normal result + mark potential Belief revision. |

The Sincerity Gate is not a punishment for strategic play. It is a mechanical expression of the NPC's rendering of the character's intentions. Consciousness renders other consciousnesses; people perceive bad faith. The GM should use this sparingly — only when the player's stated approach is clearly at odds with their character's Beliefs.

### §5.4 Information Gates

The Depth axis and the Disposition axis are parallel information-access systems:

| Access Method | Depth 0 (Surface) | Depth 1 (Settled) | Depth 2 (Hidden) | Depth 3 (Buried) | Depth 4 (Liminal) |
|--------------|-------|--------|--------|--------|---------|
| Exploration | Auto | Cognition ≥ 2 | Cognition ≥ 3 | TS ≥ 10 | TS ≥ 30 |
| Investigation | Auto | Ob 1 | Ob 2 | Ob 3 + TS ≥ 10 | Ob 5 + TS ≥ 30 |
| Socializing | Any Disposition | Disposition +1 | Disposition +2 | Disposition +3 | Disposition +4 |

A character can access the same information through different routes. The NPC who won't share a Buried secret (requires Disposition +3) might be bypassed entirely by a sensitive investigator who Thread-Reads the relevant site (TS ≥ 30, Ob 3). But Thread-Read carries co-movement costs and Exposure that talking to the NPC does not. There is always a trade-off between access methods.

### §5.5 Socializing and Beliefs

When a social action aligns with or challenges a character's stated Belief, mechanical consequences apply:

- **Belief-aligned social success:** +1 Momentum (if below cap 4). Counts as Belief achievement per core engine.
- **Belief-challenging social success:** No Momentum, but the success creates narrative pressure to re-examine the Belief. GM marks as potential Belief revision opportunity.
- **Social action that requires betraying a Belief:** Certainty pressure — GM marks potential Certainty shift. Does not fire automatically; resolves at session end per accumulated pressure.

### §5.5b Hook Acquisition via Socializing

An Overwhelming result on a **Read** action (§5.2) that reveals a deeply compromising truth about the target NPC produces a **Hook** — leverage usable in NPC Recruitment (npc_behavior_v30.md §9.5).

- **Overwhelming Read → Weak Hook** by default (suggestive but not irrefutable).
- **Overwhelming Read + prior Verified Finding on same NPC** → Strong Hook (irrefutable; GM confirms).

Hooks are tagged to the NPC in the roster. A character who holds a Hook may use it in a subsequent Recruitment approach. Hooks acquired through social fieldwork are personal to the character who performed the Read — they do not transfer to the faction automatically unless disclosed in a formal intelligence scene.

### §5.6 Knot Integration

At Disposition +5 (Bonded), the NPC becomes a Knot candidate per existing threadwork rules. Forming a Knot with a Bonded NPC follows standard Knot procedures (threadwork_redesign_v25.md §8).

**Non-sensitive characters at Disposition +5:** If neither the PC nor the NPC has TS ≥ 30, Knot formation is impossible — Knots require Thread contact. The relationship is as deep as it can be without Thread linkage. Mechanically: no decay, +1D on social actions (these benefits apply at Disposition +5 regardless of Knot status). Relational contagion (P-12) does not apply without a Knot.

Knot-linked characters gain:
- Automatic Disposition maintenance (no decay)
- +1D on all social actions with the Knot partner
- Shared Composure buffer (per social_contest_system_v2.md §4 Step 6)
- Relational contagion risk (P-12): Thread-shift propagates through Knots

### §5.7 Contest Escalation and Negotiate Boundary

**Negotiate** applies only when: (a) parties share a goal but disagree on method (not formally opposed), or (b) the outcome is not consequential enough for full Contest. If the situation meets Contest initiation conditions (social_contest_system_v2.md §1: "two or more parties with opposed positions AND outcome is uncertain and consequential"), the interaction is a Contest, not a Negotiate. The GM does not offer a choice — the situation's structure determines the mechanic.

When a social action fails at Disposition ≤ 0, or when the NPC has strong reason to resist, the GM may declare **escalation**. The interaction transitions from fieldwork to a formal Contest (social_contest_system_v2.md). This is a Register Shift (stage11 §11.2).

Escalation preserves: current Disposition (applied as starting Conviction Track offset, ±1 per 2 Disposition points, capped at ±2). The relationship does not reset — it intensifies.

### §5.8 Niflhel Social Toolkit Extension

Niflhel cannot participate in Formal or Grand Contests (per social_contest_system_v2.md §9.7). Their fieldwork social toolkit is equally restricted:

- **Available actions:** Read, Connect, Negotiate. One-on-one only (Niflhel cannot operate in group social settings).
- **Unavailable actions:** Impress (no institutional social presence), Rumour (excluded from social networks).
- **Exposure modifier:** +2 Exposure per social action (Niflhel existence is conspicuous; any interaction risks notice).
- **Primary pool:** Attunement (per Contest §9.7 — Niflhel social interactions are Attunement-primary regardless of action type).
- **Thread Insight (TS ≥ 30 only):** Before a Negotiate or Read action, Niflhel with TS ≥ 30 may perform a free Thread-Read (Attunement, Ob = floor(target TS / 30, round up), min 1) to perceive one unstated position. This does not consume a scene action but generates +1 Exposure.

---

