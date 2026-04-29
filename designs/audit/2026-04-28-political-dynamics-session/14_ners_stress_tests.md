<!-- [PROVISIONAL: 2026-04-28 session — NERS stress tests, all directions] -->
<!-- STATUS: PROVISIONAL — tests against 12_development_specification.md -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/14_ners_stress_tests.md -->

# NERS Stress Testing: Political Dynamics System — All Directions

**Criteria:** N = Necessary · E = Elegant · R = Robust · S = Smooth  
**Directions:** Top-down · Bottom-up · Vertical · Horizontal · Lateral · Diagonal  
**Source of truth:** `12_development_specification.md`  
**Prior technical tests:** `13_stress_tests_extended.md` (implementation gaps, crashes, undefined behavior)  
**This document:** Design-quality evaluation — does the system earn its complexity?

---

## FRAMEWORK

Each test applies one NERS criterion from one directional perspective. Tests that pass receive a brief confirmation. Tests that fail receive: game-state trace, issue statement, severity classification, and patch or design recommendation.

Severity: **Design-Fail** (violates the criterion structurally) · **Friction** (degrades the criterion; patchable) · **Gap** (criterion underspecified; needs resolution) · **Pass** (criterion met)

---

## NECESSARY

### N-TOP: Does Every Architectural Layer Earn Its Place?

**Probe:** The system has five layers. Evaluate each for necessity: could the system achieve its stated goal (NPCs as autonomous political actors generating emergent dynamics) with the layer removed?

**Layer 1 (Per-NPC Inner State):** Necessary. Without per-NPC state, autonomous behavior is impossible. The full structure (Concerns, Projects, Opinions, Memories, Knowledge, Mood) drives all procedures. No excess.

**Layer 2 (Three-Dimension Armature):** Necessary. Replaces 630 templates. Produces characteristic-derived interpretation. Without the armature, all NPCs interpret events identically. Necessary.

**Layer 3 (Event Impact Matrix):** Necessary. Computed once per event, consumed by all armatures. Without it, each armature would independently compute event effects — O(NPCs × events) vs O(events + NPCs). Also centralizes scope cap enforcement. Necessary.

**Layer 4a (Settlement Meta-Armature + Settlement Signal):** **Marginal.** The Settlement layer is an intermediary between personal events and faction Concerns. Its function: aggregate Passive NPC reactions, apply institutional character weighting, produce a Signal that generates faction-level Concerns. Could personal events propagate directly to faction Concerns with the same 0.7 decay?

What the Settlement layer adds that direct propagation does not: institutional character bias (Cathedral, Market, Fortress, Outpost each have distinct weights), governor-tenure scaling, and Passive NPC Memory aggregation. Without it, the 50 named Passive NPCs have no mechanical role — they exist as flavor.

**Verdict:** Necessary **only if** Passive NPCs are mechanically meaningful. If Passive NPCs are cut or reduced significantly, the Settlement layer becomes unnecessary overhead. If they are retained, the layer is necessary to integrate them. The necessity of the Settlement layer is contingent on the Passive NPC design decision.

**Issue (N-TOP-A):** The dependency is inverted — the Passive NPC design decision (authored count, what they do) should drive whether the Settlement layer is included, not the other way around. The spec assumes both without flagging their dependency. If Passive NPC authoring is reduced to ~10-15 NPCs (from 50) for authoring scope reasons, the Settlement aggregation loses statistical validity.

**Recommendation:** Flag explicitly in §9 authoring scope: "Settlement Meta-Armature statistical validity degrades below ~5-7 Passive NPCs per settlement. If Passive NPC authoring is reduced to <5 per settlement, reconsider whether Settlement Signal produces meaningful output or should be replaced with a simpler governor-direct propagation path."

**Layer 4b (Faction Meta-Armature):** Necessary. Without it, faction-level behavior is the sum of individual NPC behaviors with no institutional character — historically incoherent. The institutional_stability term (preserving faction identity under individual Scar accumulation) is particularly necessary.

**Layer 5 (Four Procedures + Real-Time Mood):** Necessary. The five update mechanisms cover the full temporal profile of NPC life: immediate response (Mood), seasonal deliberation (B, C), ongoing relationship drift (D), ambient social world (E). Each covers distinct behavior that the others don't.

---

### N-BOTTOM: Are All Data Structure Fields Used?

**Probe:** For each field in §2 Per-NPC Data Structures, identify whether it is consumed by at least one procedure in §6.

**Fields audited:**

| Field | §6 Consumer | Verdict |
|---|---|---|
| conviction_primary | §3.2 armature derivation, §5.3 meta-armature, §6.2 Proc E | Used |
| conviction_secondary | §3.2 modify_by_scar_count | Used |
| backstory_tags | Not referenced in any procedure | **Unused** |
| personality (all 4 dims) | §3.2 modify_by_personality, §6.2 DA phase gating | Used |
| mood | §6.1, §6.2 (all procedures gate on mood) | Used |
| mood_set_by | Provenance tracking; not consumed by any procedure | Metadata only |
| mood_duration | §6.1 decay ("each Accounting, Mood decays one step") | Used |
| beliefs | §3.5 Path A/B, §6.2 Proc B Knowledge trigger | Used |
| scars | §3.2 modify_by_scar_count | Used |
| disposition_with_player | §7.1 Read gate, §7.3 Witness Mode selection, §7.4 Crisis Priority | Used |
| certainty | "existing, optional" — zero references in §6 | **Unused** |
| ts | "existing, optional" — zero references in §6 | **Unused** |
| concern_history | Populated in §6.2 Proc B Resolution; never read | **Write-only** |
| Concern.seeking | §3.3 generation, §3.4 resolution, §6.2 Proc E knowledge sharing | Used |
| Concern.ttl | §6.2 Proc B Resolution decay | Used |
| Project.domain_action_required | §6.2 DA Proposal Phase flagging | Used |
| Project.seasons_stalled | §6.2 Proc C stall/failure | Used |
| Project.blocked_by | Not defined in §2.4 (gap from ST-27-A) | Missing |
| Opinion.confidence | §6.2 Proc D drift gating | Used |
| Opinion.evidence_memory_refs | §6.2 Proc D: "Increment reference_count on Memories used" | Used |
| Memory.salience_floor | §6.2 Proc D: reference_count × 0.5 | Used |
| Knowledge.valid | §6.2 Proc B generation trigger | Used |
| Knowledge.knowledge_type | Behavior rules in §2.7 (decay rates) — not enforced in any Proc | **Unimplemented** |
| EventImpact.visibility | §7.5 Factional Exposure (implicitly); no Proc reads it directly | **Effectively unused** |
| EventImpact.active_dimensions | §3.3 generate_concern | Used |

**Issue (N-BOTTOM-A — backstory_tags):** `backstory_tags` (§2.1) are authored per NPC (5-8 tags) but consumed by no procedure. They appear to be authoring/narrative reference only. If they are not used mechanically, they are overhead — 35 Active NPCs × 6 tags average = 210 authored tags with no procedural function.

**Patch:** Either (a) define a procedure that reads backstory_tags (e.g., Concern salience modifier when event touches a backstory_tag domain), or (b) move backstory_tags out of the NPC data structure entirely and into the authoring notes. As a mechanical field, backstory_tags must be read by something.

**Issue (N-BOTTOM-B — certainty/ts):** `certainty` and `ts` (§2.2) are flagged "(existing, optional)" and unused in this spec. If they are used by other Valoria systems (Threadwork, Fieldwork), their presence here is correct — they are cross-system fields. If they are not used by any system in the current spec, flag them for removal from the political dynamics state structure to reduce implementation scope.

**Patch:** Add a comment to §2.2: "certainty and ts are existing fields retained for cross-system compatibility. Political dynamics procedures do not read them. Their values are set and consumed by other Valoria systems."

**Issue (N-BOTTOM-C — concern_history write-only):** `concern_history` is appended to at Concern resolution (§6.2 Proc B) and capped at 5 entries. It is never read in Concern generation, resolution, or any other procedure. Its stated purpose (implied: continuity bias preventing Concern repetition) is not implemented. The field accumulates data that is never consumed.

**Patch:** Either (a) add a Concern generation check: "if concern.tag is in npc.concern_history: reduce salience by 1 (recently resolved, lower urgency)" — this implements the continuity bias the field implies, or (b) remove concern_history from the data structure and reduce authoring/storage scope.

**Issue (N-BOTTOM-D — Knowledge.knowledge_type unimplemented):** §2.7 specifies distinct behavior per knowledge_type (ongoing_state decays; historical_event does not; structural decays slowly at -0.1/season). But no procedure implements this — salience decay in Procedure B applies uniformly. The knowledge_type field is authored but behaviorally inert.

**Patch:** Add to §6.2 Procedure B: "For each NPC's Knowledge entries: apply salience decay by knowledge_type: ongoing_state: -1/season standard. historical_event: no decay (permanent). structural: -0.1/season (round down when total decay ≥ 1)."

**Issue (N-BOTTOM-E — EventImpact.visibility unused by procedures):** The `visibility` field (§4.1) specifies who can observe an event (public, semi_public_observers, private_observers). But Concern generation (§6.2 Proc B) iterates "for each NPC in event.affected_npcs" without checking visibility. A private event (witnessed only by 2 NPCs) could generate Concerns in all 35 Active NPCs if the event affects them materially. The visibility field is authored but not enforced.

**Patch:** Add to §6.2 Proc B generation: "before generating a Concern for an NPC, check: if event.visibility.public == false AND npc.id not in event.visibility.semi_public_observers AND npc.id not in event.visibility.private_observers: NPC generates no Concern from this event directly (may receive via Knowledge sharing or Settlement Signal later)." This enforces visibility scope on Concern generation and makes private events meaningfully different from public ones.

---

### N-HORIZONTAL: Are All Sub-Components of Each Procedure Necessary?

**Probe:** Within Procedure E (Off-Screen Interactions), evaluate each sub-component.

**Sub-components:** (1) Ambient inner-circle interaction at 60%, (2) Cross-faction Distant Contact at 10%, (3) Knowledge sharing via Concern seek-tag match, (4) Gossip propagation when cumulative drift > 0.5, (5) Knot partner guaranteed 100% + auto-Concern surfacing.

**(1) Ambient interaction (60%):** Necessary. Core mechanism for relationship drift between scenes.

**(2) Distant Contact (10%):** Necessary. Produces cross-faction NPC relationships and knowledge propagation without player involvement.

**(3) Knowledge sharing:** **Conditional.** Requires Concern seek-tag to match Knowledge fact_tag — a very specific match condition. In practice, how often will an NPC's active Concern seeking tag precisely match another NPC's Knowledge fact_tag? If the tag vocabulary is too large, matches will be rare and Knowledge sharing will rarely fire. If too small, it fires too often (oversimplification). The matching mechanism's effectiveness depends entirely on tag vocabulary design — which is not specified.

**Issue (N-HORIZ-A):** Knowledge sharing via seek-tag match is only as useful as the tag vocabulary. Without a defined tag taxonomy and density guidelines, this mechanism may be either dead (too sparse) or overwhelming (too dense). The spec needs a concrete statement about tag vocabulary scope and expected match frequency.

**(4) Gossip propagation:** **Marginal.** Gossip fires when cumulative drift > 0.5 from one interaction. This means a significant interaction produces a gossip item. The gossip item itself is a ~30 authored template. But gossip doesn't produce any mechanical effect in the spec — it's player-observable information (§7.2) but not a Concern, not a Memory, not a Domain Action modifier. Gossip is output-only from the perspective of NPC mechanics.

**Issue (N-HORIZ-B):** Gossip has no mechanical input. It produces narrative information for the player but does not feed back into NPC behavior. An NPC who is widely gossiped-about does not accumulate any mechanical effect from that gossip. This makes gossip unnecessary from a mechanical standpoint — it is purely a player-informing mechanism. If the cost (30 gossip text templates, §10) is justified by player experience value alone, retain it; but it is not mechanically necessary.

**(5) Knot partner guaranteed 100%:** Necessary but see S-LATERAL below for smoothness concern.

---

### N-LATERAL: Are Cross-System Integration Points Bidirectional Earners?

**Probe:** Each integration point in §8 adds something to an existing system and receives something from it. Evaluate whether each direction earns its place.

| Existing System | Political Dynamics Adds | Existing System Gives |
|---|---|---|
| Disposition track | Nothing — unchanged | Gates Read access, Witness Mode selection |
| Conviction Scars | Scar triggers Mood; generates armature shift | Scar count feeds armature weight derivation |
| Beliefs | Resolved Concerns may produce wrong Beliefs; calcification added | Active Beliefs trigger Knowledge-based Concerns |
| Standing ladder | Player at 5+ enters Meta-Armature | Promotion events generate Memories + Opinion shifts |
| Domain Actions | Failed DAs generate Concerns; inner-circle competition for proposal selection | DA execution advances proposing NPC's Project |
| Scene Slate | Outreach at Priority 3; NPC-NPC outcomes at Priority 4; crisis priority modifier | Scene actions produce Memories |
| Knot system | 100% ambient probability; auto-Concern surfacing | Knot partner death generates Grieving |

**Issue (N-LATERAL-A — Domain Action Concern salience unanchored):** §8 states "Failed Domain Actions generate Concerns" but specifies neither salience nor seeking-tag content for these Concerns. A failed DA is the most mechanically significant single event in the system — it stalls a Project, potentially permanently. The Concern it generates should be calibrated to the failure's significance. Unanchored Concern salience means implementations will choose arbitrarily.

**Patch:** Add to §8: "Failed Domain Action: generates Concern with salience = DA_difficulty_Ob (capped at 5). Seeking tags = project_domain of the failed Project. Example: Military DA fails at Ob 4 → Concern salience 4 seeking military-domain tags."

**Issue (N-LATERAL-B — Scene Slate Priority 4 NPC-NPC outcomes unspecified):** §8 states "NPC-NPC interaction outcomes can spawn Priority 4 events." But what makes an NPC-NPC interaction produce a Scene Slate event rather than just an Opinion drift? Threshold undefined. If every significant Procedure E interaction spawns a Priority 4 event, the Scene Slate is flooded. If none do, Priority 4 NPC-NPC events never appear.

**Patch:** Add to §8 Scene Slate integration: "NPC-NPC interaction spawns Priority 4 Scene Slate entry when: cumulative affect_axis change this season ≥ 0.5 AND at least one of the NPCs has Disposition ≥ +2 with player AND the interaction involves a Project the player has previously investigated. This scopes Priority 4 events to player-relevant relationships and prevents flooding."

---

### N-DIAGONAL: Cross-Scale + Cross-System Integration Necessity

**Probe:** Player at Standing 5+ entering Faction Meta-Armature — is this integration necessary?

**What it adds:** Player's armature contributes weight (Standing 5 = 0.5) to the Faction Meta-Armature aggregate. This means player's Conviction alignment influences which Domain Action proposals succeed.

**What the player experiences:** The player cannot see the Meta-Armature directly. They experience its effects through: DA proposal success rates (proposals aligned with player's Conviction get -1 Ob modifier), inner-circle competition outcomes, and Outreach scenes. The player has no direct feedback that their Standing 5 milestone changed faction behavior — the effect is invisible unless they notice statistical patterns.

**Issue (N-DIAG-A):** The Standing 5 → Meta-Armature integration is mechanically real but experientially invisible. The player receives no in-game signal that their armature is now part of the faction's interpretive frame. A milestone of this significance should produce observable changes. Without a player-facing signal, the integration is mechanically present but experientially absent — contributing to systems that run silently without player awareness.

**Patch:** Add to §7 Player-Facing Surfaces: "Upon reaching Standing 5, the player's faction leader acknowledges their institutional influence in a mandatory Outreach scene (Priority 1). The scene is narrative but signals that the player's perspective now shapes how the faction interprets events. Subsequent Observable behaviors from inner-circle NPCs may reference player-influenced interpretations." This creates a legible milestone without exposing armature mechanics.

**Probe:** Factional Exposure + Loyalty Cover + Anomaly Detection — is this diagonal chain necessary?

The chain: player covert operations → Factional Exposure accumulates → detection roll each season → loyalty cover reduces detection probability. Separately: inner-circle NPC Dispositions drop (from player manipulation) → Anomaly Detection fires → Loyalty Interview demand scenes.

These are two independent detection paths for adversarial player operations. Is both necessary?

**Issue (N-DIAG-B):** Both detection paths run simultaneously but through completely separate mechanics (Exposure roll vs Anomaly pattern recognition). They can trigger redundantly: a player running covert operations could simultaneously trigger Exposure detection AND Anomaly detection in the same season, producing two overlapping "you've been noticed" events. The spec doesn't specify whether these are additive, independent, or mutually exclusive.

**Patch:** Add to §7.5 and §5.4: "Factional Exposure detection and Anomaly detection are independent mechanisms and can trigger in the same season. If both fire: Exposure detection takes narrative priority (the specific covert act was discovered); Anomaly detection fires as a subordinate investigation (the faction notices broader pattern, not just the specific act). Both scenes are generated; Scene Slate priority ordering applies."

---

## ELEGANT

### E-TOP: Does the Conceptual Model Translate Into Player-Intuitable Experience?

**Probe:** The design intent is NPCs as autonomous political actors with inner lives. The player interacts with NPCs through: Observable behaviors (visible_actions), Read action, Outreach scenes, Gossip, Investigation.

**Test:** Can a player with no knowledge of the underlying system predict NPC behavior from observable information?

**Trace:** Player observes that Confessor Himlensendt is "consulting with parish clergy across three settlements" (visible_action from Project advancement). Player infers Himlensendt is consolidating Church influence. Player wins a Social Contest against a Crown NPC → that NPC acquires a Scar → Distracted Mood → Domain Action proposal suppressed → Church's opposing DA succeeds unopposed → Church CI advances.

The player observes: their victory against a Crown NPC led to unexpected Church success. The causal chain is invisible — the Distracted suppression of Crown's DA opened space for Church.

**Issue (E-TOP-A — Friction):** The system produces emergent consequences the player cannot intuit without knowledge of the underlying procedures. A politically sophisticated player might recognize the correlation (Crown weakened → Church fills vacuum), but the mechanical pathway (Scar → Distracted → DA suppressed → Church unopposed) is invisible and cannot be inferred from observable information. The system is robust but not elegant at the player-experience level.

This is a fundamental tension in the design: autonomous NPCs with complex inner states produce emergent dynamics that exceed player intuition. The question is whether enough information is surfaced to let players make informed decisions, or whether emergent consequences feel arbitrary.

**Assessment:** The system as specified tips toward arbitrary consequences for players who haven't investigated deeply. Gossip and Investigation (§7.2) exist to surface more information — but both cost scene actions. At default information density (no Investigation), the player operates with significant uncertainty about causal chains.

**Recommendation (not a patch — design decision for Jordan):** Define the system's "information poverty" stance explicitly. Two options:
- Option A (opaque by design): Players are meant to operate with incomplete information; emergent consequences feel like a living world, not a puzzle to solve. The system is elegant for the world, not for player prediction.
- Option B (legible by design): Add one feedback mechanism that makes diagonal consequences legible — e.g., "when your action contributed to a faction-level consequence, an Outreach scene from an inner-circle NPC acknowledges it (cryptically or directly) at next Accounting."

---

### E-BOTTOM: Are the Formulas Logically Simple?

**Probe:** Evaluate each core formula for logical simplicity.

**Opinion Drift:** `drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × conviction_alignment_multiplier`

Three factors: base rate, dampening at extremes, Conviction modifier. Intuitive — strong opinions change slowly; shared Conviction amplifies drift. **But:** `conviction_alignment_multiplier` is undefined in the spec. No value table provided.

**Issue (E-BOT-A — Critical):** The Opinion drift formula has an undefined term. `conviction_alignment_multiplier` is referenced in §6.2 Procedure D but its values are not given anywhere in the spec. Procedure E specifies drift VALUES (±0.3, ±0.1, ±0.05) but those appear to be base_drift values, not the full formula output. The relationship between the Procedure E drift values and the Procedure D formula is unclear — are the Procedure E values pre-computed formula outputs, or inputs to the formula?

**Patch:** Clarify in §6.2 Procedure D: "The conviction_alignment_multiplier values: shared primary Conviction = 1.5; different Conviction, same faction = 1.0; different Conviction, different faction = 0.7. These values, combined with the base_drift from Procedure E, produce final drift per interaction. The Procedure E drift values (±0.3, ±0.1, ±0.05) are base_drift inputs to the full Procedure D formula."

**Armature Weight Derivation:** 5 stacked modifiers. Each applies to the same weight vector. The final armature is the cumulative result.

**Issue (E-BOT-B — Gap):** The 5 modifiers apply sequentially, but the spec doesn't define whether they are additive or multiplicative. "modify_by_personality: +0.1 to mechanism.calculation" — does this add 0.1 to an existing weight, or multiply it by (1 + 0.1)? At small values this barely matters; but at multiple stacked modifiers it diverges. With additive: 5 modifiers of +0.1 each could add 0.5 to one option's weight — possibly making it unnormalized. With multiplicative: modifier effects compound.

**Patch:** Add to §3.2: "All armature modifiers are additive to the base weight. After all modifications, normalize the weight vector per dimension so weights sum to 1.0. Normalization prevents modifier stacking from producing unnormalized output."

**Cascade Attenuation:** salience × 0.7 per boundary. Simple and intuitive. **Pass.**

**Salience floor:** reference_count × 0.5, capped at 5. Simple. **Pass.**

**Settlement Meta-Armature weights:** governor_weight = 0.1 + 0.075 × min(tenure, 4). Linear scaling, intuitive. **Pass.**

---

### E-VERTICAL: Is the Scale Transition Mechanism Elegant?

**Probe:** The 0.7 decay factor applies uniformly at every scale boundary regardless of event magnitude, type, or consequence.

**Issue (E-VERT-A — Friction):** Uniform 0.7 decay treats all events identically in propagation terms. A single-combat personal victory and a treaty-signing personal event both decay at 0.7 per boundary. In reality, some personal events (death of a faction leader's heir) should propagate more strongly than others (a routine social exchange). The system has no event-magnitude modifier on cascade decay.

This is an elegance issue because it forces all events to be authored with globally appropriate salience values — the decay is the only scale discriminator. A personal event at salience 5 always produces faction-level salience 2.45 (barely above the 2 threshold for Domain Action influence), while a personal event at salience 4 produces 1.96 (below threshold, inert at faction level). This creates a sharp cliff at salience 4 vs 5 personal events — a small authoring difference produces a binary outcome at faction scale.

**Patch:** Add an optional `propagation_weight` field to EventImpact (default 1.0, range 0.5–2.0). Decay formula becomes: salience × (0.7 × propagation_weight) per boundary. Major events (faction leader's heir death): propagation_weight = 1.5 → effective decay = 0.525/boundary → salience 5 reaches 5 × 0.525 × 0.525 = 1.38 at faction — still below threshold, but a salience 4 event at propagation_weight 1.5 reaches 4 × 0.525 × 0.525 = 1.1... actually this doesn't solve it cleanly. Alternative: reduce threshold from 2 to 1.5 for events with propagation_weight ≥ 1.5. This avoids the sharp binary cliff for major events.

---

### E-HORIZONTAL: Does the Procedure Sequence Have Clean, Non-Overlapping Responsibilities?

**Probe:** Are procedures B, C, D, E doing distinct things, or do they overlap?

**Procedure B:** Concern generation and resolution. Produces: new Concerns, Belief updates, Scars, Opinion drifts (from resolution — see ST-32 issue), Knowledge-triggered Concerns.

**Procedure C:** Project advancement. Produces: progress updates, completions, failures, new Projects, legacy Opinion shifts.

**Procedure D:** Opinion drift from Memories.

**Overlap:** Both B-Resolution and C produce Opinion changes. Both feed into the same Opinion data structure in the same Accounting pass.

**Issue (E-HORIZ-A):** B and C both modify Opinions. D is supposed to be the Opinion procedure. Three procedures write to the same data structure in one Accounting pass. This violates single-responsibility and makes Opinion state difficult to reason about at implementation time — Opinion values mid-Accounting reflect partial B-writes and partial C-writes before D consolidates.

**Patch:** Adopt single-writer model for Opinions. B-Resolution produces Memory entries only (not direct Opinion changes — patch already recommended in ST-32-A). C-Completion produces Memory entries only (not direct Opinion changes). D reads all this-season Memories and applies consolidated drift. Opinion is written exactly once per Accounting, in Procedure D. All pre-D Opinion modifications are converted to Memory creation.

---

### E-LATERAL: Are Cross-System Interfaces Clean Single Points of Contact?

**Probe:** Does the political dynamics system add clean interfaces to Scene Slate, or multiple scattered hooks?

**Scene Slate additions:**
1. Concern-driven Outreach: Priority 3 (§7.6)
2. NPC-NPC interaction outcomes: Priority 4 (§8)
3. Crisis priority modifier: Disposition ≥ +3 NPCs get +1 priority (§7.4)
4. Witness Mode cap: max 3 Read results (§7.3)

**Issue (E-LAT-A — Friction):** Four separate additions to Scene Slate from one system. Each is a scattered hook rather than a clean single interface. The Scene Slate has to be aware of: Concern state (for Priority 3 Outreach), Procedure E outcomes (for Priority 4), NPC Dispositions (for crisis priority modifier), and Witness Mode count tracking. This is four integration points, not one.

**Recommendation:** Define a single Political Dynamics → Scene Slate interface: "At each Accounting, the political dynamics system produces a `PoliticalSlate` object: {outreach_scenes: [(npc, concern, priority)], npc_npc_events: [(npc_a, npc_b, event, priority)], priority_modifiers: [(npc, disposition_value)]}. The Scene Slate consumes PoliticalSlate in one operation." This consolidates four hooks into one handed-off structure, making the integration a clean single boundary.

---

### E-DIAGONAL: Can Players Intuit Cross-Scale, Cross-System Consequences?

**Probe:** Player invests in Confession-style social builds — high Disposition with multiple Church NPCs, deep Investigation of Church inner-circle. Does the system reward this with interpretable Church dynamics?

**Trace:** Player has Disposition +3 with Himlensendt and +2 with two parish bishops. Procedure E fires: Himlensendt's Project (advancing dogmatic curriculum) generates a Domain Action proposal. Player has previously investigated → knows Himlensendt's visible_action. Gossip from a +3 Disposition NPC reveals "she's consolidating doctrinal authority." Church DA succeeds → CI +2 → crosses a territory threshold. Player receives a Scene Slate event about the territorial consequence.

**Assessment:** The chain is legible IF: (1) player invested in Investigation, (2) player maintained high Dispositions for Gossip access, (3) player was present for the Scene Slate territorial event. All three requirements must be met for the diagonal to feel elegant. If any is missing, the consequence feels arbitrary.

**Issue (E-DIAG-A — Friction):** The elegance of the diagonal depends entirely on the player's prior investment in information systems (Investigation, Disposition maintenance, scene presence). Players who haven't invested cannot follow the causal chain. This is consistent with "robust" (rewards strategic investment) but limits elegance — the system's consequences are only intuitable to players who already understand the system.

**This is acceptable** for the target player profile (strategic players willing to invest in relationships). Flag as a known design tradeoff, not a failure.

---

## ROBUST

### R-TOP: Does the System Produce Emergent Narratives Without Player Involvement?

**Probe:** Run a 4-season autonomous simulation with no player actions. What emerges?

**Season 1:**
- Procedure B: Each Active NPC generates Concerns from Season 0 events (game start events). Almud (Crown, Faith/Order, Scar 0): generates Concern about doctrinal direction based on Church's current CI stance. Himlensendt (Church, Faith): generates Concern about Crown's secular appointments. Inner-circle competition: 3 Crown NPCs propose Domain Actions. Faction Meta-Armature selects based on weighted armature aggregate.
- Procedure E: 60% ambient → ~21 inner-circle interactions across all factions. A few Opinion drifts. One Gossip item (cumulative drift >0.5).

**Season 2:**
- Almud's Concern resolves (TTL 3, not yet expired but salience decayed to 3). Resolution: Faith-shaped interpretation of Crown-Church tension. Produces a Belief: "The Church is overreaching into Crown's administrative domain." This Belief is incorrect by design (Church is responding to Crown's secular appointments, not overreaching).
- Himlensendt's Project advances (theological school funding — DA succeeded). Progress 4/10.
- Procedure E: Cross-faction Distant Contact (10%): Himlensendt and a Hafenmark NPC interact. Knowledge sharing: Himlensendt shares Church's doctrinal position. Hafenmark NPC generates Memory: "Church is hardening its theological stance."

**Season 3:**
- Almud's wrong Belief about Church overreach drives her Domain Action proposals: she proposes a Mandate action to restrict Church appointments. Crown inner-circle competition: Marshal supports (Order-aligned), Confessor opposes (Faith-aligned). Net Ob modifier: +1 (one supporter, one opposer, one neutral). Mandate DA has 50% success chance at base → modified odds.
- If DA succeeds: Church-Crown tension escalates. Himlensendt generates Concern: "Crown is encroaching on Church doctrine." A second Faith-shaped NPC (Bishop) generates similar Concern. Their armatures produce convergent seeking-tags → they arrive at similar interpretations independently.
- If DA fails: Almud's project stalls. She generates Concern about why her mandate failed. Crown inner-circle friction surfaces.

**Assessment: ROBUST PASS.** Even this brief trace produces: (1) a wrong-Belief-driven political blunder from the faction leader, (2) independent convergent NPC interpretations at faction level, (3) cross-faction information propagation, (4) genuine inner-circle tension within Crown. All without player involvement. The system earns its complexity.

---

### R-BOTTOM: Do Atomic Mechanics Produce Meaningful NPC Variation?

**Probe:** Two NPCs with the same Conviction (Faith) but different Personality. NPC-A: risk_tolerance +2, social_warmth +2. NPC-B: risk_tolerance -2, institutional_deference +2. Both experience the same event (Crown restricts Church appointments).

**Trace:**
- Base armature weights (Faith): Agency = individual-actor or divine-will dominant; Intent = ideological dominant; Mechanism = authority-exercise or moral-failure dominant.
- NPC-A (high risk_tolerance): personality modifier → +0.1 toward strategic options in Intent dimension. +0.1 toward individual-actor Agency. Produces: "The Crown acted strategically and personally — this is ideological combat."
- NPC-B (high institutional_deference): personality modifier → +0.1 toward institutional-force Agency; -0.1 toward individual-actor. Produces: "This is institutional pressure, not personal — the Crown's bureaucracy is moving against us."

Both Faith NPCs generate Concerns with different seeking-tags. NPC-A seeks "who is the strategic actor behind this?" NPC-B seeks "what institutional force is driving this?" They resolve their Concerns differently → different Beliefs formed → different Project priorities → different Domain Action proposals.

**Assessment: ROBUST PASS.** Personality modifiers produce meaningfully different interpretations even within the same Conviction. Two Faith NPCs are not mechanical clones.

**Issue (R-BOT-A — Gap):** The personality-to-armature modifier table (12 entries: 4 personality dims × 3 armature dimensions) is referenced but not authored in the spec. The example modifiers above are inferences. The actual modifier values are content authoring items (§10) — but their design principles are not stated. A high-risk_tolerance NPC should modify armature in a consistent direction across all event types. Without the authored table, this is unverifiable.

---

### R-VERTICAL: Does Player Cross-Scale Action Feel Meaningful?

**Probe:** Player wins Total Victory Contest against Crown Confessor (personal scale). Cascade reaches faction scale (salience 2.45 per prior analysis). Crown generates faction-level Concern: "Doctrinal commitment weakening?" at salience 2 (barely above influence threshold). This Concern contributes 30% weight toward Church-accommodating Domain Action selection vs the standard Crown assertion.

**Issue (R-VERT-A — Friction):** The player's significant personal victory (Total Victory Contest is the highest personal-scale achievement) produces a barely-relevant faction-level effect (salience 2, threshold-minimum influence). The system correctly attenuates to prevent single actions from dominating faction behavior — but the result is that personal-scale actions feel insignificant at faction scale. Players who want to influence faction politics through personal actions face a fundamental effectiveness wall.

**Assessment:** This is by design (preventing personal actions from disproportionately driving faction decisions) but it reduces the robustness of the "player feels important to the game world" criterion. The system makes players feel important at personal scale (NPC Concerns, Outreach) but not at faction scale unless they operate systematically (multiple actions, sustained pressure).

**Recommendation:** The system is honest about this tradeoff. Make it explicit in design documentation: "Personal actions influence faction dynamics through accumulation, not single victories. Players must sustain a pattern of personal actions to meaningfully shift faction-level behavior. Single-action faction effects are deliberately minimal." This sets correct player expectations.

---

### R-HORIZONTAL: Do Multiple Simultaneous Active Structures Compound?

**Probe:** Himlensendt has: 2 active Concerns (salience 4 each), 1 active Project (progress 6, established), 5 Opinions (two positive, two negative, one neutral), 3 active Memories from this season. All interact in one Accounting.

**Trace:**
- Procedure B: Both Concerns decay (-1 salience). Neither expires yet. No new Concerns (event pool empty this season). 
- DA Phase: Project at progress 6 needs DA this season. Himlensendt proposes a theological DA. Inner-circle competition with one other Church NPC.
- Procedure C: Project advances (DA succeeds, +2 progress → 8/10). 
- Procedure D: 3 new Memories. Two align with existing positive Opinions (Church ally), one contradicts a negative Opinion (enemy did something unexpected). The contradicting Memory: confidence 4 → strong Opinion holds, cognitive dissonance Concern generated. Himlensendt now has 3 Concerns (cap hit if another fires).
- Procedure E: Ambient interactions with 2 inner-circle Church NPCs. Shared Faith Conviction → ±0.3 drift each. Both positive → Church inner-circle cohesion increases.

**Compound effect:** Himlensendt's established Project approaching completion, her positive Church relationships strengthening, and a new Concern about an enemy's unexpected behavior — all simultaneously. The Concern about the enemy will generate Outreach toward that NPC next season (Priority 3). This produces autonomous, characterful NPC behavior: Himlensendt is succeeding professionally (Project near completion) while wrestling with an anomaly in her understanding of an adversary.

**Assessment: ROBUST PASS.** Multiple simultaneous structures compound correctly and produce characterful output.

---

### R-LATERAL: Does the Scar-Mood-Concern-Domain Action Chain Compound Meaningfully?

**Probe:** Player engineers Almud's Scar (via Total Victory Contest on her religious Belief). Chain: Scar → Mood: Distracted → Crown inner-circle Project proposals suppressed (if any NPCs are high-institutional-deference) → Church DA proceeds unopposed → CI advances → Territory threshold crossed.

**Result:** Player's targeted intervention in Almud's personal Belief system compounds through three systems (Conviction/Scar → Political Dynamics Mood → Domain Action → Provincial) to produce a territorial consequence. This is the robustness the system is designed to enable.

**Issue (R-LAT-A — Gap):** The chain requires: (1) Almud to have been near a Scar (needed prior investment), (2) Crown inner-circle NPCs to have active Projects requiring DAs (random, not player-controlled), (3) Church to have a pending DA that was previously losing in competition (situational). The chain is robust in theory but gated by conditions the player cannot directly engineer. Players will attempt this strategy and sometimes find it does nothing (no Crown DA proposals pending, or Church DA wasn't in the same domain, or Almud recovers quickly). 

The strategy is valid but unreliable. Is this the intended level of reliability for major player investment? Define expected success rate of deliberate cross-system manipulation.

---

### R-DIAGONAL: Does Cross-Scale Cross-System Investment Compound Into Leverage?

**Probe:** Player spends 6 seasons building: Standing 5 in Crown (entering Meta-Armature), Disposition +3 with 4 Crown inner-circle NPCs, Faith Conviction alignment with Crown's historical direction, 2 active Investigations into Crown Project domains.

**Expected leverage:** Player's armature in Meta-Armature biases DA selection. Player's Disposition +3 NPCs gossip and Outreach. Player's Investigations give visibility into Project progress. Player's Faith alignment helps Faith-resonant DAs succeed.

**Issue (R-DIAG-A — Friction):** The player's 6-season investment compounds into a meaningful but limited position. The institutional_stability term (§5.3) for Crown is ~0.4 × (1 - scars/max_scars) → at game start, ~40% weight toward Order. Player's armature (Faith) competes against Crown's historical Order character. The player cannot fully overcome institutional_stability through personal alignment alone — it requires inner-circle Scar accumulation to degrade institutional_stability weight.

**Assessment:** This is correct behavior (institutional character should be persistent), but it means even maximum personal investment over 6 seasons produces only moderate faction-level influence. The robustness criterion ("makes players feel important to the game world, feel like they are impacting the game world") may be partially unsatisfied for players who invest heavily in faction alignment but see limited results.

**Recommendation:** Consider whether a 6-season full-investment player should be able to noticeably shift faction behavior, or whether faction change should require 10-15 seasons of sustained investment. Define this in the design document as an intended design parameter, not leave it to emergent tuning.

---

## SMOOTH

### S-TOP: Does the System Output Flow Cleanly Into Player Experience?

**Probe:** At Accounting close, the political dynamics system has produced: 3 Outreach scenes (Priority 3), 1 NPC-NPC event (Priority 4), 2 Mood updates, 6 Opinion changes, 2 Project advancement events. What does the player experience?

**Player-visible output:** 3 Outreach scenes in Scene Slate. 1 NPC-NPC event in Scene Slate. Project advancement appears as: 25% chance per player scene action of encountering NPC's visible_action (§7.2). The Mood updates and Opinion changes are invisible unless the player reads the relevant NPCs.

**Issue (S-TOP-A — Friction):** The system produces rich internal state changes but most are invisible to the player. The player sees 4 Scene Slate entries and occasional ambient NPC behavior. The rest — the 6 Opinion changes, the Mood updates, the armature shifts — happen silently. This is intentional (opaque NPC inner lives) but creates a disconnect between system activity and player perception: a very active political season looks identical to a quiet one from the player's perspective.

**Assessment:** The opacity is justified by the design philosophy. The system is not trying to make itself visible — it's trying to produce a living world. But "smooth" requires that the system's output-to-player-experience handoff is clean. The handoff is through Scene Slate, Observable behaviors, and Gossip — three surfaces. These are clean but limited.

---

### S-BOTTOM: Do Formula Outputs Feed Cleanly Into Next Procedure?

**Probe:** Procedure B-Resolution output (Belief update, Concern resolved, Memory created) → feeds into DA Phase (Procedure between B and C) → feeds into Procedure C.

**Trace:**
- B-Resolution produces: new Belief (for NPC), resolved Concern removed, Memory added, possibly Scar.
- DA Phase reads: npc.active_project.domain_action_required (set by Project, not by B) and npc.mood (set by B-Resolution via Scar → Distracted).
- Procedure C reads: npc.mood (unchanged from what DA Phase saw), npc.active_project.progress, npc.active_project.seasons_stalled.

**Assessment: SMOOTH PASS.** B outputs (Mood changes, Scar) correctly flow into DA Phase and C without format mismatch. The only exception is the double-write issue to Opinions (ST-32/E-HORIZ-A), which is a smoothness failure already flagged.

---

### S-VERTICAL: Are Scale Transitions Smooth or Friction-Generating?

**Probe:** A personal event in Season 3 → Settlement Signal in Season 4 (aggregated over last 2 seasons per §5.2) → Faction Concern at Accounting of Season 4 → Domain Action change at Season 4 DA Phase.

**Issue (S-VERT-A — Friction):** The Settlement Signal aggregates "last 2 seasons" of Passive NPC Memories. This means a personal event's cross-scale consequence is delayed 1-2 seasons. The timeline:
- Season 3: Personal event fires. Event Impact Matrix computed. NPC Concerns generated immediately (Procedure B, Season 3 Accounting).
- Season 4 Accounting: Settlement Signal aggregates Season 2-3 Memories. Signal propagates to faction Concern.
- Season 4 DA Phase: Faction Concern influences Domain Action selection.

A personal event's faction-level consequence appears one full Accounting (season) after the NPC-level consequence. The player interacts with an NPC this season → the faction doesn't respond until next season. Is this smooth?

**Assessment:** The delay is realistic (institutional response lag) but may feel like a broken feedback loop to players who expect immediate systemic consequences. The smoothness criterion ("pauses correctly when other mechanical systems are called for") doesn't apply here — this is a temporal smoothness question. **Flag as a known playtest concern** rather than a structural failure.

---

### S-HORIZONTAL: Does the Procedure Sequence Have Clean Handoffs?

**Probe:** Procedure C → Procedure D. Procedure C produces Project completion with legacy Opinion shifts. Procedure D processes this-season Memories for Opinion drift.

**Issue (S-HORIZ-A):** As established in E-HORIZ-A and ST-32, Procedures C and D both write to Opinion. This is the primary horizontal smoothness failure. The single-writer fix (C produces Memories only, D consolidates) resolves this.

**Additional issue (S-HORIZ-B):** Procedure E fires after D. Procedure E generates interactions that produce Memories and drift. These new Memories are created this season — they won't be processed by D (which already ran). They sit in Memory until next season's D. This means Procedure E's drift effects are delayed by one full Accounting relative to B and C effects. Is this consistent?

**Assessment:** The inconsistency is minor (E fires late in the cycle, its effects are next-cycle) but worth noting. For fast-moving political situations, Procedure E effects always lag one season behind in-scene effects. This is acceptable and arguably realistic (ambient social interactions take time to consolidate into relationship changes). No patch required; clarify in spec.

---

### S-LATERAL: Does Knot Integration Maintain Consistent Opacity Principles?

**Probe:** §7.1 states: "Opacity is preserved at high Disposition — NPCs choose to share, not give the player direct data access." §6.2 Knot integration states: "One Concern about each Knot partner is automatically surfaced per season (no Read action required)."

**Issue (S-LAT-A — Design-Fail):** Knot auto-surfacing of Concerns contradicts the opacity principle. The opacity principle says NPCs share by choice through Outreach scenes (candor); they don't give direct data access. Knot auto-surfacing is direct mechanical access to an NPC's inner state, bypassing the choice-to-share model.

Knot partners are emotionally intimate — surfacing their concerns makes intuitive sense. But the mechanism (automatic Concern surfacing with no Read action, no scene cost) is qualitatively different from Outreach (the NPC initiates a scene and shares through dialogue). Knot surfacing as specified bypasses the narrative layer (the NPC speaks) and delivers mechanical data (the Concern question) directly.

**Patch:** Rephrase Knot integration in §6.2: "Knot partners automatically generate one Concern-driven Outreach scene per season (Priority 2 — elevated above standard Priority 3 Outreach due to intimacy). This is not direct Concern access — it is a guaranteed Outreach scene driven by the partner's active Concern. The player learns about the Concern through the scene's dialogue, not as a mechanical data readout." This preserves opacity (NPC chooses to surface in the scene) while maintaining the elevated Knot relationship mechanic (guaranteed surfacing, not subject to scene action competition).

---

### S-DIAGONAL: Is the Full Personal → Territorial Pipeline Clean at Every Boundary?

**Probe:** Trace the full cross-scale, cross-system pipeline for a player victory:

1. Player wins Total Victory Contest (Scene system) → Conviction Scar on Confessor (Conviction system)
2. Scar → Mood: Distracted (Political Dynamics real-time Mood)
3. Distracted Confessor's established Project continues at +1 Ob → partial success on church ministry DA
4. Partial success DA → Settlement Signal in Verdmuld reduced (Settlement layer, Season + 1)
5. Settlement Signal → Church faction Concern: "Doctrinal reach faltering?" salience 2 (Faction layer, Season + 1)
6. Church Concern at salience 2 → 30% contribution to Domain Action bias toward CI-Assert (Domain Action system)
7. CI-Assert DA selected (inner-circle competition) → CI +2 → territory threshold crossed (Provincial system)

**Boundary analysis:**
- Boundary 1 (Scene → Conviction): Clean. Contest resolution is existing system.
- Boundary 2 (Conviction → Political Dynamics Mood): Clean. Scar triggers Mood in §6.1.
- Boundary 3 (Mood → Project/DA): Clean within spec, pending Grieving gating patch (ST-19).
- Boundary 4 (DA → Settlement Signal): **Lag.** Settlement Signal aggregates 2 seasons of Memories. The DA partial success from Season N appears in Settlement Signal at Season N+1 Accounting.
- Boundary 5 (Settlement → Faction Concern): Clean once lag is accepted.
- Boundary 6 (Faction Concern → DA bias): Clean. Salience ≥ 2 required for influence (met at 2.45 pre-attenuation, 2.0 post-normalization — barely).
- Boundary 7 (DA → Provincial): Existing system, not in scope of this spec.

**Issue (S-DIAG-A — Friction):** The pipeline has one clean entry point (Scar), one dirty lag (Settlement Signal 2-season aggregation), and one barely-passing threshold (salience 2.0 after two ×0.7 attenuations). The barely-passing threshold is the critical fragility: if the personal event was at salience 4 instead of 5, the faction-level Concern would be below the influence threshold entirely (4 × 0.7 × 0.7 = 1.96 < 2). The player's action at salience 4 vs 5 produces binary faction-level effects.

This binary behavior is the same cliff identified in E-VERT-A. The fix is the same: propagation_weight modifier on EventImpact to allow some salience-4 events to maintain influence, and/or slightly lowering the influence threshold from 2.0 to 1.5 for events of high propagation_weight.

---

## SUMMARY TABLE

| Test | Criterion | Direction | Verdict | Severity |
|---|---|---|---|---|
| N-TOP-A | Necessary | Top-down | Settlement layer contingent on Passive NPC count | Gap |
| N-BOT-A | Necessary | Bottom-up | backstory_tags unused mechanically | Friction |
| N-BOT-B | Necessary | Bottom-up | certainty/ts unused — clarify cross-system or remove | Gap |
| N-BOT-C | Necessary | Bottom-up | concern_history write-only; never read | **Design-Fail** |
| N-BOT-D | Necessary | Bottom-up | knowledge_type behavior unimplemented in procedures | **Design-Fail** |
| N-BOT-E | Necessary | Bottom-up | EventImpact.visibility unused in Concern generation | **Design-Fail** |
| N-HORIZ-A | Necessary | Horizontal | Knowledge sharing seek-tag match: no tag vocabulary spec | Gap |
| N-HORIZ-B | Necessary | Horizontal | Gossip: no mechanical input/feedback loop, purely player-informing | Friction |
| N-LAT-A | Necessary | Lateral | DA Failure Concern salience unanchored | **Design-Fail** |
| N-LAT-B | Necessary | Lateral | NPC-NPC Priority 4 Scene Slate threshold undefined | **Design-Fail** |
| N-DIAG-A | Necessary | Diagonal | Standing 5 → Meta-Armature: player receives no signal | Friction |
| N-DIAG-B | Necessary | Diagonal | Exposure + Anomaly can trigger redundantly; not coordinated | Gap |
| E-TOP-A | Elegant | Top-down | System consequences beyond player intuition without Investigation | Design-Fail (by design) |
| E-BOT-A | Elegant | Bottom-up | conviction_alignment_multiplier undefined — formula has undefined term | **Critical** |
| E-BOT-B | Elegant | Bottom-up | Armature modifier additivity vs multiplicativity unspecified | **Design-Fail** |
| E-VERT-A | Elegant | Vertical | Uniform 0.7 decay creates salience-4 vs 5 binary cliff | Friction |
| E-HORIZ-A | Elegant | Horizontal | Procedures B, C, D all write to Opinions (single-responsibility violation) | **Design-Fail** |
| E-LAT-A | Elegant | Lateral | Four scattered Scene Slate hooks vs one clean interface | Friction |
| E-DIAG-A | Elegant | Diagonal | Diagonal chain legible only to heavily-invested players | Acceptable tradeoff |
| R-TOP | Robust | Top-down | System produces emergent dynamics without player | **PASS** |
| R-BOT-A | Robust | Bottom-up | Personality → armature modifier table unauthored; values unverifiable | Gap |
| R-VERT-A | Robust | Vertical | Personal-scale victories feel insignificant at faction scale | Friction |
| R-HORIZ | Robust | Horizontal | Multiple simultaneous structures compound correctly | **PASS** |
| R-LAT-A | Robust | Lateral | Cross-system chain reliable in theory but gated by uncontrollable conditions | Gap |
| R-DIAG-A | Robust | Diagonal | 6-season investment produces limited faction shift; threshold undefined | Gap |
| S-TOP-A | Smooth | Top-down | Rich internal state but limited player-visible output | Acceptable (opacity by design) |
| S-BOT | Smooth | Bottom-up | B → DA → C handoffs clean (modulo ST-32/E-HORIZ-A) | **PASS** |
| S-VERT-A | Smooth | Vertical | Settlement Signal 2-season lag in cross-scale propagation | Friction |
| S-HORIZ-A | Smooth | Horizontal | C and D both write to Opinions (see E-HORIZ-A) | **Design-Fail** |
| S-HORIZ-B | Smooth | Horizontal | Procedure E effects delayed by one Accounting vs B/C | Acceptable |
| S-LAT-A | Smooth | Lateral | Knot auto-surfacing contradicts opacity principle | **Design-Fail** |
| S-DIAG-A | Smooth | Diagonal | Salience-4 vs 5 binary cliff at faction influence threshold | Friction |

---

## ISSUE COUNTS

**Design-Fail (must address before promotion):** 9  
— N-BOT-C (concern_history dead), N-BOT-D (knowledge_type unimplemented), N-BOT-E (visibility unenforced), N-LAT-A (DA failure Concern unanchored), N-LAT-B (Priority 4 Scene Slate threshold), E-BOT-A (conviction_alignment_multiplier undefined), E-BOT-B (armature modifier math unspecified), E-HORIZ-A / S-HORIZ-A (three procedures write Opinions), S-LAT-A (Knot opacity contradiction)

**Gap (requires design decision before implementation):** 8  
— N-TOP-A, N-BOT-B, N-HORIZ-A, N-DIAG-B, R-BOT-A, R-LAT-A, R-DIAG-A, E-TOP-A (design stance decision)

**Friction (patchable, reduces quality):** 7  
— N-BOT-A, N-HORIZ-B, N-DIAG-A, E-VERT-A / S-DIAG-A (same cliff), R-VERT-A, S-VERT-A, E-LAT-A

**Pass:** 4  
— R-TOP, R-HORIZ, S-BOT, S-HORIZ-B, E-DIAG-A, S-TOP-A (last two acceptable tradeoffs)

---

## CONSOLIDATED PATCH PRIORITY

**Fix before any implementation begins:**
1. E-BOT-A: Define conviction_alignment_multiplier values in §6.2 Procedure D.
2. E-BOT-B: Specify armature modifier math as additive + normalize per dimension in §3.2.
3. E-HORIZ-A / S-HORIZ-A: Single-writer Opinion model — B and C produce Memories only; D consolidates all Opinion changes.
4. N-BOT-C: Either implement concern_history as Concern generation salience modifier, or remove from data structure.
5. N-BOT-D: Implement knowledge_type decay behavior in §6.2 Procedure B.
6. N-BOT-E: Enforce EventImpact.visibility in §6.2 Procedure B Concern generation.
7. N-LAT-A: Anchor DA Failure Concern salience to DA difficulty Ob.
8. N-LAT-B: Define Priority 4 Scene Slate trigger threshold.
9. S-LAT-A: Rephrase Knot auto-surfacing as guaranteed Outreach scene (Priority 2), not direct Concern access.

**Fix before promotion to canonical:**
10. E-VERT-A / S-DIAG-A: Add propagation_weight to EventImpact and lower threshold for high-weight events.
11. N-DIAG-A: Add Standing 5 milestone Outreach scene.
12. N-DIAG-B: Coordinate Exposure and Anomaly detection when both fire same season.
