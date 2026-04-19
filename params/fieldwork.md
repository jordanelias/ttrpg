<!-- version: v1.0 | source: designs/fieldwork/fieldwork_v30.md | last_updated: 2026-04-13 -->
<!-- PATCHES APPLIED: PP-575 (initial), PP-576 (audit), PP-577 (transitions), PP-578 (threadwork), PP-579 (ontological), PP-580 (extended), PP-581 (P1 resolution), PP-582 (fidelity), PP-632 (Disposition redesign + Knot system) -->

# params_fieldwork.md — Fieldwork System (Exploration / Investigation / Socializing)

## Pool Formula (confirmed ×2 per PP-615)
Fieldwork Pool = (Primary Attribute × 2) + History bonus
History bonus = relevant History points + 3
TN: 7 (Standard) | 6 (Controlled) | 8 (Desperate)
Pool minimum: 5D (Attribute 1, no History: (1×2) + 3 = 5)
Pool maximum: 24D (Attribute 7, History 7: (7×2) + (7+3) = 24)

## Primary Attribute by Activity
| Activity | Sub-type | Primary Attribute |
|----------|----------|-------------------|
| Exploration | Terrain / navigation | Cognition |
| Exploration | Thread-aware | Attunement |
| Exploration | Endurance-based | Endurance |
| Investigation | Physical evidence | Cognition |
| Investigation | Witness / informant | Attunement |
| Investigation | Lore / research | Recall |
| Investigation | Thread-Read | Attunement (+ Thread Pool Score) |
| Socializing | Read | Attunement |
| Socializing | Impress | Charisma |
| Socializing | Connect | Bonds |
| Socializing | Rumour | Charisma |
| Socializing | Negotiate | Attunement |

## Depth Axis
| Depth | Name | Perception Gate | Base Ob |
|-------|------|-----------------|---------|
| 0 | Surface | None | Auto |
| 1 | Settled | Cog ≥ 2 or local History | 1 |
| 2 | Hidden | Cog ≥ 3 or Att ≥ 3 | 2 |
| 3 | Buried | TS ≥ 10 (explore/invest) or Disposition ≥ Bonds − 1 (social, PP-684) | 3 |
| 4 | Liminal | TS ≥ 30 | 5 |
| 5 | Unintelligible | TS ≥ 50; Coherence check Ob 2 | 8 |

Ob modifiers: hostile territory +1, foreign +1, allied −1, local resident −1, RS <60 at Proximity ≤2 +1, active HI +1. Floor: 1.

## Degree Table (core engine — PP-232/PP-249)
| Net | Degree |
|-----|--------|
| ≥ 2×Ob AND ≥ 3 | Overwhelming |
| ≥ Ob | Success |
| 0 < net < Ob | Partial |
| ≤ 0 | Failure |

## Exploration — Discovery Procedure
| Degree | Discovery Quality |
|--------|-------------------|
| Failure | Nothing. Exposure +1. |
| Partial | POI located, unclear. One surface feature. |
| Success | POI located, full detail. One actionable piece. |
| Overwhelming | Full detail + hidden feature below POI's depth. +1 Momentum. |

Multi-character: leader + max 2 assistants. Assistant rolls at same Ob +1. Assistant Success: +1 net to leader. Assistant Failure: +1 Exposure for party.

## Rendering Strain (Depth 3+)
| Depth | Effect |
|-------|--------|
| 3 (Remnant) | Minor. TS ≥ 10: no effect. TS < 10: vague unease. Certainty pressure (GM marks). |
| 4 (Anomaly) | Significant. Coherence check Ob 1 (fail: −1). Certainty −1 if ≥ 3. |
| 5 (Breach) | Severe. Coherence −1 auto. Certainty forced ≤ 2. TS +1. Warning: Coherence ≤ 2 practitioners risk Crisis. |

Non-sensitive at Depth 3+: +0 Exposure (institutionally invisible). Sensitive: +1 Exposure.

## Investigation — Evidence Track
| Scope | Threshold |
|-------|-----------|
| Simple | 3 |
| Complex | 5 |
| Structural | 8 |

Progress by degree: Failure +0, Partial +1, Success +2, Overwhelming +3.
Exposure by degree: Failure +2, Partial +1, Success +0, Overwhelming −1.
One track per investigation regardless of territory. Persistent across sessions.
Progress above threshold: no additional effect.
Let It Ride: failed action on specific target cannot be reattempted same scene.

## Desperate Trail (Fail Forward)
Trigger: 3 consecutive failed investigation actions (net ≤ 0) on same investigation.
Effects: TN → 8. Exposure doubled on failure. GM introduces complication. Partial progress → +2.
Clears: any Success/Overwhelming, or season change. Persists through Compromised.

## Evidence Quality Tags
| Source | Tag | Admissibility |
|--------|-----|---------------|
| Examine | Verified | Court, Contest, Domain Action |
| Interview | Testimonial | Contest (Memory); −1 if hostile witness |
| Research | Documentary | Court, Contest (+2D Recall) |
| Surveil | Observational | Intelligence, Contest; high Exposure |
| Thread-Read | Thread-verified | TS ≥ 30 only. Inert Knowledge for non-sensitives. Church inadmissible. |
| Rumour | Unverified | Directional only |
| Reconstruct | Derived | As strongest constituent |

Thread-verified evidence: half value (round down, min 0) for non-sensitive Evidence Track.
Resolved investigation produces Finding (strongest tag). Combined Findings: +1D Argue per additional (max +2D).

## Thread-Read (Perceptive Leap)
Requirements: TS ≥ 30. Standard Leap procedure. Co-movement fires (P-01).
Pool: (Att × 2) + History bonus + Thread Pool Score (TS ÷ 10). TN: 7.
Coherence: per scale table (Object/Personal = 0; Relational = −1; Territorial = −1; Structural = −2).
Evidence: +2 (Success), +3 (Overwhelming).

## Thread Operation Investigative Yield (contextual — GM determines)
| Operation | Typical Yield |
|-----------|---------------|
| Thread-Read | +2/+3 (direct perception) |
| Weaving | +1 if co-movement reveals |
| Pulling | +2/+3 (reveals hidden/frozen) |
| POP | +2/+3 (displaces; orphan = evidence) |
| Locking | +1 (preserve) / +2 (resistance reveals structure) |
| Dissolution | +2 (concealment destroyed) / +1 (Gap topology) |
| Mending | +1 (reveals original) / +2 (opens access) |

Mending arc: severity reduction yields +1/+2/+2/+3 across four reductions.

## Disposition Track (PP-632)
Range: −4 to Bonds (PP-684 revised from floor(Bonds/2)+1). Asymmetric per-NPC per-PC.

| Bonds | Max Disposition |
|-------|----------------|
| 1 | +1 |
| 2 | +2 |
| 3 | +3 |
| 4 | +4 |
| 5 | +5 |
| 6–7 | +5 (capped by Disposition max) |

**Ob rule: effective Ob = max(1, base Ob − Disposition).** Direct subtraction; no stepped table.
Negative Disposition adds difficulty. Positive Disposition reduces it. Floor 1 always applies.
Impress is exempt (it produces starting Disposition; Disposition is not yet established).

| Value | Label | Info Gate |
|-------|-------|-----------|
| −4 | Hostile | Refuses interaction. Violence possible. |
| −3 | Suspicious | Minimal cooperation. |
| −2 | Wary | Guarded. Surface only. |
| −1 | Cool | Cautious. Surface only. |
| 0 | Neutral | Standard. Surface. |
| +1 | Interested | Settled information. |
| +2 | Friendly | Hidden information. |
| +3 | Trusting | Buried information. |
| +4 | Devoted | Liminal information. Knot threshold at Bonds 6–7. |

**Starting Disposition — lifepath derivation (PP-632):**
For each relevant lifepath element, assign ±0.5 based on alignment/conflict with NPC faction, culture, and role. Sum, take floor, clamp to [−4, floor(Bonds/2)+1].
- Same birthplace/cultural region: +0.5
- Same occupation/guild/trade: +0.5
- Same faction (loose): +0.5 / (full member): +1
- Rival faction: −0.5 / (actively opposed): −1
- Opposing lineage or family conflict: −0.5
- Shared formative history (war, disaster, institution): +0.5

Shift by degree: Failure −1, Partial +0, Success +1, Overwhelming +2.
Decay: > +2 decays −1/season without contact. ≤ +2 stable indefinitely.
Recovery from ≤ −3: requires significant narrative event before social actions.
Post-Contest: winner Disposition +1 with adjudicator, loser −1.
NPC learns investigation revealed their secrets: −2 (exception: +1 if NPC wanted truth).


## Knot System (PP-632 — see params/threadwork.md for full mechanics)
Knots are being-with (Mitsein), not Thread operations. Any character. TS not required.

Pool = (Bonds × 2) + 3. Max count = floor(Bonds/2)+1.
Tiers: Close (5pts) / Medium (2pts) / Loose (1pt).
Formation: max Disposition + Connect roll (Ob = tier, Disposition subtracted, floor 1).
Effects: +1D social with partner; no Disposition decay; shared Composure buffer;
  relational contagion (P-12) for practitioners; Knot-mediated Thread-Read (TS 30+, +1 strain/use).
Rupture: Disposition →−4; Composure damage = tier cost.
Loss: Disposition track removed; Coherence −1; Composure damage = tier cost.
Full mechanics: params/threadwork.md §Knot Mechanics.

## Sincerity Gate
Trigger: GM-called when Belief contradicts genuine engagement.
Pool: Spirit. TN: 7. Ob: 1.
Failure: Disposition unchanged or −1. Success: normal result.

## Gift/Bribe
No roll. Starting Disposition +1. Once per NPC per season. Fails at Disposition ≤ −3 (Suspicious/Hostile NPCs reject gifts from strangers).

## Knot-Mediated Remote Thread-Read (§2.6)
Pool: standard Thread-Read. TN: 7. Ob: Personal (2).
Cost: +1 Knot strain per use.
Detection: Knotted party Spirit TN 7, Ob = practitioner Cog ÷ 2 (min 1). Detection: Disposition −3.

## Non-Sensitive Dissonance (§2.7)
Spirit check TN 7 vs Dissonance Factor (1-4 by severity).
Failure: Spirit −1D remainder of scene. Rotation needed every 3-4 Thread-adjacent scenes.

## Threadcut Being Social (§2.8)
Social actions work. Testimony tag: Testimonial (transmissible to non-sensitives — being translates).
Evidence Track = player-level knowledge. Memory-Pull does not reverse track.

## Cover (Derived Value)
Cover = Cognition + most relevant History for concealment.
| Cover | Noticed | Watched | Compromised |
|-------|---------|---------|-------------|
| 1–3 | 3 | 5 | 7 |
| 4–5 | 4 | 6 | 8 |
| 6–7 | 5 | 7 | 9 |
| 8–9 | 6 | 8 | 10 |
| 10–11 | 7 | 9 | 11 |
| 12+ | 8 | 10 | 12 |

## Exposure Sources
| Source | Exposure |
|--------|----------|
| Failed explore/investigate | +1 (or +2 at Depth ≥ 3) |
| Thread-Read | +1 |
| Sensitive at Depth 3+ POI | +1 (non-sensitive: +0) |
| Surveil | +2 |
| Failed social at Disposition ≤ 0 | +1 |
| Hostile territory per scene | +1 |
| Conspicuous action | +1 |
| Niflhel social action | +2 |
| Combat during fieldwork arc | +1 quiet / +2 conspicuous / +3 public |

Reduction: concealment (Cog ×2, Ob 2) −2; leave territory reset; season reset; cover identity −1/scene; faction support −2/season.

## Exposure → Church AP (§6.5)
Church territory (PT ≥ 3 or Church-controlled): Watched → +1 AP at Accounting. Compromised → +1 AP immediately.
Cap: +1/character/season, +2/territory/season from fieldwork.

## Wounds and Fieldwork (§2.2)
Physical wounds (−1D per wound): apply to Endurance-based exploration and Surveil only.
Social/cognitive fieldwork: unaffected by physical wounds.
Rattled: +1 Ob per mark to social fieldwork actions.
Wounds and Thread ops: +1 Ob to Leap-based Thread ops (concentration, not pool penalty).

## Inspiration Spend
1 Inspiration before rolling → Ob −1 (min 1).

## Contest Escalation (§5.7)
Negotiate applies only when: (a) shared goal, disagree on method, or (b) outcome not consequential enough for Contest.
Opposed + uncertain + consequential → Contest per social_contest_system_v2.md §1.
Disposition maps to Conviction offset: ±1 per 2 Disposition, cap ±2.

## System Transitions (§2.3)
Fieldwork → Combat: action resolves first; Noticed+ → ambusher +1D first exchange Off.
Fieldwork → Contest: Disposition → Conviction offset; evidence → +2D Recall; not consumed.
Fieldwork → Mass Battle: suspension; Evidence freezes; Thread-Read in Phase 4 = intelligence.
Combat → Fieldwork: wounds persist; combat Exposure +1/+2/+3.
Contest → Fieldwork: Appraise → +1 Evidence (Testimonial); Disposition +1/−1 post-Contest.
Mass Battle → Fieldwork: resume from frozen; post-battle examine = 1 fieldwork scene.

## Board Game — Survey Action (§8.1)
Card: Consul Inward. Pool: Influence. Ob: (5 − Proximity Rating) + 1. Min 1.
Success: reveal POI. Overwhelming: POI + Influence +1. Failure: +1 AP if Depth ≥ 3.
| POI | BG Bonus |
|-----|----------|
| Resource | Prosperity +1 |
| Secret | +1D next military/intel action |
| Remnant | Thread op Ob −1 for 2 seasons; Thread Debt token |
| Anomaly | RS −1 immediate; WC +1 eligible |

## Domain Echo from Investigation (§2.5)
Resolved Finding with faction scope → Domain Echo per stage11 §11.5.
May trigger NPC arc events (Discovery Events, Loyalty shifts, clock advances, Coalition triggers).

<!-- patch_history: references/params_fieldwork_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
