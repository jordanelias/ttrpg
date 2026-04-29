<!-- [PROVISIONAL: 2026-04-28 session — integration test + streamlined architecture] -->
<!-- STATUS: PROVISIONAL — supersedes 05_groundup and 06_iterative on architectural specifics -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/09_integration_test_streamlined.md -->

# Integration Test: Ground-Up Review, Streamlining, and Patches

The previous work produced a multi-layered architecture. This document tests it from the ground up as a unified whole, identifies what to cut, what to merge, and what to keep, and presents a tightened spec.

---

## Part 1: Ground-Up Integration Tests

Eleven end-to-end traces testing the architecture against real game-state scenarios.

---

### T-1: A single social Contest traces through the full system

**Input:** Player wins Total Victory Contest against Confessor. Conviction Scar acquired.

**Trace through architecture:**

**Event fires.** Event Impact Matrix computes:
- material_effects: none (personal-scale event)
- symbolic_effects: Confessor {conviction_contradicted, institutional_threatened}; player {empowered}
- relational_effects: Confessor-player pair {divergent}
- scale_signature: personal
- visibility: semi-public (other NPCs present at the Contest observe)

**Immediate Mood update** (if we keep real-time Mood): Confessor → Distracted.

**At Accounting:**
- Procedure B: Confessor armature reads Matrix. Faith-Conviction seeking tags: {authority-questioned, divine-test, boundary-violation}. Memories: this event. Concern generated: "The player has access to arguments I cannot rebut. Either they are dangerously wrong or I have been."
- Procedure C: Confessor's Project (Church doctrine advocacy, progress 7/10, established). Distracted Mood in the revised spec halts new Projects (progress < 3). **Issue found:** The spec says Distracted halts Project advancement — but this is an established Project (progress 7). Halting it is too severe.
- Procedure D: Confessor's Opinion of player updates. Memory contributes −0.3 to affect_axis (negative: the encounter was painful) but the Opinion has confidence 3 (moderately strong, positive prior). Result: affect_axis drops from +1.2 to +0.9 — still positive. The Confessor finds the player complicated, not hostile.
- Procedure E: Confessor's ambient contact with peers. Distracted Mood should reduce participation probability.

**Settlement cascade:** Confessor's Project at reduced capacity. Three settlement ministry actions go at +1 Ob instead of standard. One fails. That settlement's Settlement Signal shows reduced faith-institutional resonance. Church Faction Meta-Armature generates Concern: "Doctrinal reach is weakening in [settlement]."

**Total cascade:** Contest → Scar → Concern → Settlement → Faction-Concern. Three degrees. Correct behavior but contingent on Project-halting rule.

**Issue T-1-A:** Distracted Mood halts Project advancement for all Projects regardless of how established they are. A project the Confessor has been running for 6 seasons has institutional momentum that continues independently. The halt rule should apply only to new Projects (progress < 3). Established Projects continue at reduced capacity: +1 Ob to Project-advancement actions, not halt.

**Issue T-1-B:** Procedure E should specify that Distracted Mood reduces ambient interaction probability to 20% (from 60% baseline) and skips triggered interactions with low-salience activation. An NPC who is distracted doesn't reach out; they may still respond to high-salience approaches.

---

### T-2: Domain Action proposal competition — realistic load

**Input:** Crown Accounting, Season 8, Year 4. Marshal Ehrenwall (Project: train Torben), Confessor (Project: doctrine advocacy, currently Distracted), Klapp (Project: Stillhelm Codex near completion), Spymaster Kolbrun (Project: identify Niflhel-successor brokers), two Standing 4 Lieutenants with no current Project advancement need.

**What proposes Domain Actions?**
- Marshal: Project advancement this season requires "Crown military deployment." Proposes.
- Confessor: Distracted, Project at reduced capacity, but still eligible to propose if Project advancement need exists. His Project needs a Domain Action for doctrinal expansion, but Distracted Mood makes the proposal at +1 Ob. Does he propose? Per personality: high institutional_deference (+1) means he suppresses personal proposals when distracted. No proposal.
- Klapp: Project nearing completion (progress 9/10). His Project doesn't require a Domain Action — it's investigative (Stillhelm Codex research). No Domain Action proposal.
- Kolbrun: Project requires intelligence-gathering Domain Action. Proposes.
- Two Lieutenants: No Project need this season. No proposals.

**Result:** Two proposals (Marshal, Kolbrun) in different domains (military, intelligence). No competition — both can proceed independently. Inner-circle competition mechanism doesn't fire this season.

**Assessment:** This is the typical case. Competition is rare (same-domain proposals from multiple NPCs). The full competition mechanism is invoked infrequently, which is correct.

**Issue T-2-A:** The evaluation logic "does this NPC have a Domain Action need this season?" isn't lazy — it's specified as "each NPC evaluates." For 35 Active NPCs across all factions, that's still 35 evaluations per Accounting even if most return null. The evaluation should be lazy: NPCs with active Project advancement needs are flagged during Procedure C. Only flagged NPCs generate Domain Action proposals. Non-flagged NPCs don't evaluate.

---

### T-3: Event Impact Matrix — does it actually enrich armature input?

**Input:** Crown-Varfell military alliance signed.

**Matrix computed:**
```
material_effects:
  Crown: capacity_gain (military cooperation)
  Varfell: capacity_gain (intelligence sharing)
  Church: capacity_loss (symbolic — rival faction empowered)
  Hafenmark: relational_shift (Crown-Varfell alliance changes peninsula balance)

symbolic_effects:
  Confessor (Faith): conviction_contradicted (Varfell's Consequentialist framework)
  Klapp (Reason): conviction_aligned (diplomatic pragmatism)
  Marshal (Order): conviction_neutral (military alliance, institutional stability)
  Kolbrun (Autonomy): conviction_aligned (intelligence sharing opens operational space)
  Vaynard (Reason/Consequentialist): conviction_aligned (treaty serves Varfell interests)

relational_effects:
  Crown-Varfell: convergent
  Crown-Hafenmark: divergent (balance shift)
  Church-Crown: divergent (Crown prioritized secular alliance over ecclesiastical)

scale_signature: [faction, peninsula]
visibility: public
```

**Each armature reads its Matrix row.** The Confessor doesn't receive "treaty signed" — he receives "treaty signed that contradicted my Conviction, threatened my institution, and diverged my relationship with Crown." His Concern generation is immediately more specific:

Seeking tags: {faithless-counsel, strategic-miscalculation, divine-abandonment}. The armature selects via Faith-Conviction weights. Most salient seeking tag: faithless-counsel (Faith armature weights individual-actor agency + corruption mechanism + ideological intent).

Without Matrix: Confessor generates "Why did Almud sign a treaty?" → vague seeking.
With Matrix: Confessor generates "Who provided the faithless counsel that led Almud to sign this treaty?" → specific target for subsequent investigation.

**Assessment:** The Matrix genuinely enriches the input. The Concern generated is more actionable and legible. The computational overhead is justified on quality grounds. The earlier "reduces computation" claim was overstated — it provides richer input at marginal additional cost.

**Issue T-3-A:** The symbolic_effects table for the Matrix requires knowing each NPC's primary Conviction at Matrix-compute time. This is available (Identity data). But the Matrix is computed per-event, not per-NPC — so it must list symbolic_effects for all potentially-affected NPCs. For a faction-wide event like a treaty, that's 35+ NPC rows. The Matrix is not a small object.

**Fix T-3-A:** Matrix symbolic_effects need only list NPCs who are directly materially or institutionally affected. For events at the faction scale, this is the inner-circle NPCs of affected factions (~10-15 NPCs per affected faction). For personal-scale events, 2-5 NPCs. Scale-appropriate list, not all 35 NPCs.

---

### T-4: Settlement Meta-Armature weights — justified?

**Input:** Weights are 40/30/20/10 (governor / Passive NPCs / institutional character / population).

**Test via extreme cases:**

*Case A: Well-liked governor, Passive NPCs all Faith-aligned, Cathedral settlement, Faith-majority population. All inputs agree.* Meta-Armature = strongly Faith-biased. ✓ Consistent.

*Case B: Governor is Reason-aligned (Framework Tension), Passive NPCs are split (2 Faith, 1 Reason), Cathedral settlement, Faith-majority population.* Meta-Armature:
- Governor: Reason, weight 40% → Reason contributions
- Passive NPCs: 2/3 Faith, 1/3 Reason, weight 30% → predominantly Faith
- Institutional character: Cathedral → Faith, weight 20%
- Population: Faith-majority, weight 10%
Net: Faith 0.30×(2/3) + 0.20 + 0.10 = 0.20 + 0.20 + 0.10 = 0.50 Faith; Reason 0.40 + 0.30×(1/3) = 0.40 + 0.10 = 0.50 Reason. Exactly tied.

A tied settlement is politically contested — the governor's Reason interpretation and the Cathedral's Faith interpretation are exactly in balance. This actually models the Framework Tension dynamic correctly.

*Case C: Governor replaced (new governor, no established relationship). Passive NPC network remains.* Governor's armature is new, low-confidence. Should the 40% weight apply immediately? No — a new governor takes time to establish institutional influence. The 40% weight should scale with governor tenure: new governor (0 seasons): 10%; established (4+ seasons): 40%.

**Issue T-4-A:** Governor weight should scale with tenure, not be fixed at 40%. New governors don't immediately dominate settlement interpretation. This prevents the "swapping governors to instantly shift settlement politics" exploit.

**Critique of weight values:** The 40/30/20/10 split has no derivation — it's design parameters requiring simulation calibration. The spec should present them as adjustable knobs, not authoritative values.

---

### T-5: Faction Meta-Armature — institutional inertia vs. ethical framework anchor redundancy

**Structure:**
```
Faction Meta-Armature = inner-circle aggregate + institutional_inertia(0.3) + ethical_framework_anchor(0.2)
```

**Test:** If Crown's inner-circle aggregate shifts toward Reason (player has joined inner circle at Standing 5 with Reason Conviction, Klapp's arc is advancing), does the meta-armature respond proportionally?

Inner-circle aggregate: 5 NPCs. Player (Reason, Standing 5, weight ~0.5), Klapp (Reason, Standing 4, weight ~0.3), Marshal (Order, Standing 5, weight ~0.5), Confessor (Faith, Standing 7, weight ~1.05), Spymaster (Autonomy, Standing 4, weight ~0.3). Total weight: 2.65.

Reason weight: (0.5 + 0.3) = 0.8 / 2.65 = 30%.
Faith weight: 1.05 / 2.65 = 40%.
Order weight: 0.5 / 2.65 = 19%.
Autonomy weight: 0.3 / 2.65 = 11%.

Institutional inertia (0.3) biases toward "maintaining existing positions" — which means Faith-dominant (Crown's traditional framework). Ethical framework anchor (0.2) is Virtue Ethics (Crown's framework) — which biases toward Order, not Faith specifically.

**Issue found:** The ethical framework anchor and institutional inertia are both pulling toward tradition/stability but in different specific directions. They're operating as overlapping moderators of the same thing. Together they constitute 50% of the meta-armature's non-aggregate component, which means even a dramatic inner-circle shift toward Reason is dampened to: 30% aggregate × 50% weight = 15% Reason contribution vs. old-baseline stabilizers.

This is either too conservative (the institution never adapts) or the dampening is realistic (courts resist individual reform). But the two separate terms are doing one job.

**Consolidation:** Merge institutional_inertia and ethical_framework_anchor into a single **institutional_stability** parameter. Weight: 0.4. Value: the faction's existing dominant Conviction at game-start (Crown: Order/Virtue-Ethics derived; Church: Faith/Divine-Command; etc.). The parameter biases the meta-armature toward the faction's historical interpretation. Scar count in the inner-circle degrades this weight (courts with many Scarred NPCs have weakened institutional stability).

Formula: `institutional_stability_weight = 0.4 × (1 - (total_inner_circle_scars / max_scars))`.

---

### T-6: NPC Opinions — overlap with Disposition

**Test:** The Confessor has Disposition +2 with the player (Friendly). The Confessor also has an Opinion of the player: affect_axis = +1.2 (slightly positive with moderate confidence).

These should be correlated but they're stored as separate values. Is the distinction meaningful?

Disposition is the player's observable relationship state with the NPC — it gates information access, social Ob modifiers, Knot formation. It's the *operational* relationship.

Opinion is the NPC's internal assessment of the player — it shapes how the NPC interprets the player's actions when the player isn't present, it influences what the NPC says to other NPCs about the player, and it determines how much credit/blame the NPC assigns to the player for events.

**Are they distinct?** Yes but under-specified. Disposition measures the quality of direct interaction; Opinion measures the NPC's internal characterization. An NPC can have Disposition +2 (they interact pleasantly) while holding Opinion affect_axis −0.5 (they think the player is charming but ultimately untrustworthy). The emotional valence of the Opinion can diverge from the transactional quality of the Disposition.

**Issue T-6-A:** The proposal's Opinion structure applies to NPC↔player AND NPC↔NPC relationships. For NPC↔player, Opinion should influence *non-player-present* behavior (how the NPC describes the player to others, how they interpret ambiguous player-related events), not duplicate Disposition. Opinion should not be used as a Disposition proxy. The spec doesn't make this boundary explicit.

**Clarification needed (not redundancy — but boundary specification):** Opinion of player: used only for NPC-initiated social behavior when player is not present. Disposition: used for all player-NPC direct interactions. These don't conflict; they cover different behavioral domains.

---

### T-7: Concerns vs Beliefs — formation path clarity

**Test:** Are two Belief-formation paths (Contest and Concern-resolution) specified without overlap?

- Contest path: immediate, player-mediated, produces Scar (the old Belief becomes a Scar, new Belief forms).
- Concern-resolution path: slow (4-8 seasons), autonomous, produces Belief update (may or may not become a Scar).

**Gap found:** When a Concern resolves to a Belief that *contradicts an existing Belief*, does that also produce a Scar? The proposal says "Concern resolves to a Belief or Opinion update" but doesn't specify whether contradicting an existing Belief via Concern-resolution triggers Scar accumulation.

If it doesn't: NPCs can accumulate new Beliefs via Concern-resolution without Scar cost, potentially diverging significantly from their original Conviction profile without triggering arc transitions.

If it does: Concern-resolution produces the same arc consequences as social Contests, meaning NPCs in rich information environments are pushed through arc transitions faster than intended.

**Patch T-7-A:** Concern-resolution that contradicts an existing Belief produces a Scar *only if* the contradiction is strong (the new Belief directly negates the old one's domain) AND the resolution is based on multiple high-salience Memories (salience ≥ 3 each). Minor Concern resolutions that partially update a Belief don't produce Scars. Strong contradictions do. This differentiates the two formation paths: Contests produce immediate Scars; Concern-resolution produces Scars only under sustained high-salience pressure.

---

### T-8: Knowledge → Beliefs gap

**Test:** Father Eyvind (Faith-aligned parish priest) learns via Knowledge propagation that a Crown spy is operating in his settlement. Eyvind's Belief: "The Crown defends the faithful." The Knowledge directly challenges this Belief.

**In the current spec:** Eyvind's Knowledge sits in his Knowledge structure. Eyvind can share it with the player at Disposition +3 (sensitivity 3). But the Knowledge doesn't generate a Concern about his Belief. Eyvind keeps believing "The Crown defends the faithful" while knowing a Crown spy is active locally.

**This is wrong.** A person who learns their government is running covert operations in their community does not hold prior beliefs unchanged. The Knowledge should challenge the Belief.

**Patch T-8-A (already proposed in iterative doc but not integrated here):** When a high-salience Knowledge fact (salience ≥ 4) is acquired by an NPC, the engine checks whether any of the NPC's current Beliefs have a Conviction-domain match with the Knowledge fact's domain. If yes, a Concern is generated: "Is [Belief] still accurate given what I now know?" This uses the existing Concern system as the Knowledge→Belief connector. No new mechanism — one new trigger condition.

---

### T-9: Armature four dimensions — Threat-sensitivity is redundable

**Test:** Does Threat-sensitivity do work that active Projects and Conviction don't already do?

Threat-sensitivity: "what domains does this NPC monitor for danger?" Options: {theological, military, economic, personal-standing, institutional-role, succession, knowledge-access}.

For the Confessor (Faith, Project: doctrine-advocacy): Threat-sensitivity should be high on theological and institutional-role. But this is directly derivable: Faith Conviction → monitors theological domain; doctrine-advocacy Project → monitors institutional-role domain. The seeking tags generated from these domains are exactly what the armature's Conviction + Project weighting already produces.

**Test case:** Same event interpreted by two Faith-aligned NPCs, one with high Threat-sensitivity to succession (has a succession-related concern) and one without. The Threat-sensitivity dimension should produce different seeking tags for the succession domain. But: if one NPC has an active Concern about succession, that Concern's seeking tag already biases the armature toward succession-related interpretation. The Concern system does the work Threat-sensitivity was meant to do.

**Confirmation: Threat-sensitivity is redundable.** Remove it as an armature dimension. Three-dimension armature: [Agency, Intent, Mechanism].

Threat domain sensitivity is instead read from: (a) active Project domains (the NPC monitors what they're invested in), (b) active Concerns (the NPC monitors what they're currently worried about), (c) Conviction primary domain (always high sensitivity). No separate dimension needed.

This reduces the authoring obligation: from 7 Convictions × 4 dimensions to 7 Convictions × 3 dimensions = 25% reduction in armature weight entries.

---

### T-10: Procedure A (Mood) — can be eliminated as a batch procedure?

**Current:** Procedure A runs at Accounting. Mood updates batch-processed.

**Problem (from iterative testing):** Large events (Scar, death) need Mood to update immediately to affect this-season's behavior, but batching delays until Accounting.

**Solution already proposed:** Mood updates in real-time at event resolution, not at Accounting. This makes Mood a property of the NPC that the event-resolution engine sets directly.

**Consequence:** Procedure A is eliminated. The remaining procedures are B (Concerns), C (Projects), D (Opinions), E (Interactions). Four procedures instead of five.

**Ordering without Procedure A:** Event resolution sets Mood immediately. At Accounting: B (Concerns from prior-season events, using current Mood) → C (Project advancement, using current Mood) → D (Opinion drift) → E (Interactions).

**Does this eliminate the Immediate Update special case?** Yes. Mood is already current at Accounting because it was set in real-time. No within-season partial re-run needed for Mood propagation. The Immediate Update mechanism was only needed because batched Mood was stale. With real-time Mood, it's abolished.

**Result:** Eliminate Procedure A. Eliminate the Immediate Update special case. Simplify to four procedures (B, C, D, E) with real-time Mood external to the batch Accounting process.

---

### T-11: Full political loop — does it close properly?

**Trace:** Start at a faction Domain Action, end at a player scene.

1. Crown Domain Action proposed by Marshal (advancing training-Torben Project) fires at Accounting (Season 8 Year 4).

2. Event Impact Matrix computed: material_effect {Torben: capacity_gain military}; symbolic_effect {Confessor: conviction_contradicted — sending heir into potential danger without spiritual preparation}; relational_effect {Marshal-Confessor: divergent — Marshal's proposal succeeded over Confessor's implicit objection}.

3. Confessor armature reads Matrix. Concern generated: "Is Torben being shaped into a soldier when he needs to be shaped into a king?" Seeking tags: {spiritual-neglect, militarism, succession-risk}. Mood: Anxious (succession-domain threat activated).

4. Confessor's Opinion of Marshal: affect_axis drops -0.4 (Memory: "She got what she wanted, and Torben's soul is the cost").

5. Procedure E: Confessor and Klapp have ambient contact (60% base). Confessor's Anxious Mood reduces this to 20%. No contact this season.

6. Confessor generates an Outreach scene for next season (Concern-driven, seeking player's Disposition +1+ which exists). Outreach topic: succession concerns, Torben's spiritual preparation.

7. Scene Slate (next season): player receives Confessor Outreach scene. The scene's content reflects the Confessor's Concern — he's not confronting the player about theology; he's worried about Torben's soul. This is a Scene the player couldn't have predicted from any single prior action.

**Loop closes.** Domain Action (faction) → Event Impact Matrix → NPC Concern generation (personal) → Outreach scene (personal). The player enters a political conversation about succession, spiritual authority, and military development — seeded by a Domain Action about a garrison assignment.

**Assessment:** The architecture produces the intended emergent narrative. The loop closes correctly and the player's scene is politically unexpected but causally traceable.

---

## Part 2: Streamlining and Consolidation

Issues found in testing, organized by type:

### Eliminate / Reduce

| Item | Action | Reason |
|---|---|---|
| Procedure A (Mood batch) | **Eliminate.** Mood is real-time. | Duplicate of in-event Mood setting; cause of Immediate Update complexity |
| Immediate Update mechanism | **Eliminate.** | Unnecessary when Mood is real-time |
| Threat-sensitivity dimension | **Remove from armature.** | Redundable from active Projects + Concerns + Conviction |
| institutional_inertia + ethical_framework_anchor (two terms) | **Merge into institutional_stability.** | Both doing same job; separate terms add spec complexity without behavioral distinction |
| 35-NPC Event Impact Matrix symbolic_effects | **Scale to affected NPCs only.** | Full list is too large; only inner-circle of affected factions needed |

### Patch / Specify

| Item | Action |
|---|---|
| Distracted Mood halts all Projects | **Patch:** established Projects (progress ≥ 3) continue at +1 Ob, not halted |
| Domain Action proposal evaluation | **Patch:** lazy evaluation — only flagged-at-Procedure-C NPCs evaluate |
| Governor weight is fixed 40% | **Patch:** governor weight scales with tenure (new: 10%; 4+ seasons: 40%) |
| Concern-resolution → Scar question | **Patch:** strong contradictions (multiple high-salience Memories) → Scar; minor updates → no Scar |
| Knowledge → Beliefs gap | **Patch:** high-salience Knowledge (≥4) triggers Concern if it contradicts a Belief's domain |
| NPC Opinion of player boundary | **Clarify:** Opinion of player covers non-player-present behavior only; Disposition covers direct interactions |
| Distracted Mood and Procedure E | **Patch:** Distracted reduces ambient contact probability to 20% |

---

## Part 3: Revised Architecture

### 3.1 NPC Inner State (streamlined)

```
Identity (static):
  conviction_primary
  conviction_secondary
  personality:
    risk_tolerance: -2 to +2
    social_warmth: -2 to +2
    intellectual_rigor: -2 to +2
    institutional_deference: -2 to +2

State (dynamic, real-time):
  mood: {Steady, Anxious, Confident, Grieving, Vindicated, Humiliated, Distracted, Resolved}
  mood_set_by: event_id (for provenance)
  beliefs: 2-3 structured beliefs (existing)
  scars: count (existing)
  disposition_with_player: -3 to +5 (existing)

Concerns: 1-3 active
  question, source_event, salience, ttl, seeking[3 dims: Agency/Intent/Mechanism], resolution

Projects: 1-2 active
  goal, progress (0-10), project_domain, visible_action, completion_effect,
  failure_effect, institutional_support (bool: established ≥3 progress)

Opinions: NPC-NPC only (not NPC-player)
  subject, affect_axis (-3 to +3), confidence (1-5), evidence_memory_refs[]

Memories: 5-10 high-salience
  timestamp, event_type, participants, affect, salience, detail

Knowledge: (info-rich NPCs only)
  fact_tag, source, salience, sensitivity (1-5)
```

### 3.2 Three-Dimension Armature

```
Armature dimensions: [Agency, Intent, Mechanism]
  (Threat-sensitivity removed — read from active Projects + Concerns + Conviction)

Agency options: {individual-actor, institutional-force, structural-pressure, divine-will, chance}
Intent options: {ideological, strategic, personal-ambition, moral-failure, external-compulsion}
Mechanism options: {corruption, calculation, error, social-pressure, authority-exercise}

Weights derived from:
  conviction_primary → base weights (7 Conviction × 3 dimensions × 5 options = 105 weight entries)
  personality modifiers → small adjustments per dimension
  scar_count → softens primary conviction weight (Scar 0: 100%; Scar 1: 75/25; Scar 2: 50/50; Scar 3+: secondary leads)
  active_project_domain → +0.1 to Agency/Mechanism options in project domain
  active_concerns → +0.1 to seeking tags matching existing Concern domains (continuity bias)
```

### 3.3 Event Impact Matrix (scope-capped)

```
EventImpact:
  event_id, event_type, source_actor
  
  material_effects[]: (directly affected actors only)
    actor_id, type, direction, magnitude

  symbolic_effects[]: (inner-circle NPCs of affected factions only, not all 35)
    actor_id, conviction_resonance, institutional_resonance

  relational_effects[]: (affected pairs only)
    actor_pair, direction

  scale_signature[], time_horizon, visibility
```

### 3.4 Settlement Meta-Armature (with tenure-scaled governor)

```
SettlementMetaArmature:
  governor weight = 0.1 + 0.075 × min(governor_tenure_seasons, 4)
    (scales 0.1 → 0.4 over 4 seasons)
  passive_npc_aggregate: remainder weight after governor
    (scales 0.3 → 0.6 for new governor, 0.3 for established)
  institutional_character: 0.2 (fixed, settlement type determines Conviction bias)
  population: 0.1 (fixed)
```

### 3.5 Faction Meta-Armature (merged stability term)

```
FactionMetaArmature:
  inner_circle_aggregate: Standing-weighted average of inner-circle armatures
    leader weight: 1.5× their Standing weight
  
  institutional_stability: single parameter replacing [inertia + framework_anchor]
    weight: 0.4 × (1 - (total_inner_circle_scars / max_scars))
    value: faction's historical dominant Conviction at game-start
    (decays as inner-circle accumulates Scars — damaged courts resist less)
```

### 3.6 Four Procedures (streamlined from five)

```
REAL-TIME (not batched):
  Mood update: fires at event resolution. Sets NPC mood immediately.

ACCOUNTING SEQUENCE (B → C → D → E):
  B — Concern Generation and Resolution
    Input: last season's event log + current Mood
    Outputs: new Concerns generated; existing Concerns resolved to Beliefs/Opinion-updates
    Scar rule: Concern-resolution produces Scar only if multiple high-salience Memories (≥3 each) 
              contradict an existing Belief directly
    Knowledge trigger: salience ≥4 Knowledge fact in NPC's Knowledge structure → 
                       check if contradicts active Belief domain → generate Concern if yes

  C — Project Advancement
    Input: current Mood, faction priority tree status, Domain Action flags
    Lazy Domain Action flagging: if NPC has project_advancement_need this season, flag for DA proposal
    Established Projects (progress ≥3): advance at +Mood-Ob-modifier (Distracted: +1 Ob)
    New Projects (progress <3): halt on Distracted Mood
    Failure: 8+ seasons stalled → fail + Memory(negative) + Mood + new Project slot

  D — Opinion Drift
    Input: this season's Memories (C completions, B resolutions, E interactions from prior season)
    drift formula: base × (1 - |affect_axis|/3) × conviction_alignment_multiplier
    Updates: affect_axis, confidence (strengthens on confirming Memory, weakens on contradicting)

  E — Off-Screen Interactions
    Budget: Active NPCs: 60% ambient (inner-circle pairs, Conviction-scaled drift)
            10% Distant Contact (cross-faction pairs with prior Memory)
    Distracted Mood: NPC participates at 20% rate (not 60%)
    Selection priority: shared Concerns > intersecting Projects > prior Memory > ambient baseline
    Knowledge sharing: if either has Knowledge salience ≥3 and other has matching Concern seeking tag → transfer
    Gossip: significant affect drift (>0.5) generates gossip item propagating to related NPCs

DOMAIN ACTION PROPOSALS (between C and D):
  Flagged NPCs from C propose Domain Actions to their faction's priority tree
  Inner-circle competition: competing proposals resolved by Faction Meta-Armature weighting
  Ob modifiers: supporting NPCs (conviction_aligned to proposal) -1 Ob; 
                opposing NPCs (conviction_contradicted) +1 Ob
```

---

## Part 4: Revised Authoring Obligations

| Item | Count (revised) | Notes |
|---|---|---|
| Armature weights (3 dims, down from 4) | 105 | 7 Convictions × 3 dimensions × 5 options |
| Personality modifiers | 12 | 4 personality dims × 3 armature dimensions |
| Event dimension profiles | ~270 | 30 event types × 3 dimensions × 3 options (unchanged) |
| Sentence frames | ~15 | 3 dims × 5 options combinations (reduced from 20) |
| Event symbolic resonance table | 210 | 7 Convictions × 30 event types (unchanged) |
| Settlement institutional character bias | 6 | Per settlement type (unchanged) |
| Faction institutional_stability starting value | 7 | One per faction (down from 14 = inertia + anchor) |
| Domain Action sponsor mapping | ~30 | Per faction (unchanged) |
| Starting Projects per Active NPC | 35 | (unchanged) |
| Starting Opinions (NPC-NPC, not player) | ~200 | Reduction from ~350 (player-opinions removed) |
| Knowledge seeding | ~150 | (unchanged) |

**Total: ~1040 entries** (down from ~1070; reduction from removing player-Opinions and collapsing inertia+anchor, offset by the armature dimension count still requiring similar entries even with one dimension removed since option counts are maintained).

Minor reduction in count but more meaningful reduction in conceptual complexity: fewer redundant concepts, cleaner boundaries, no special-case mechanisms.

---

## Part 5: What Was Cut and Why

| Cut item | Reason |
|---|---|
| Procedure A (Mood batch) | Real-time Mood makes it unnecessary; also eliminated Immediate Update complexity |
| Immediate Update mechanism | Consequence of real-time Mood adoption |
| Threat-sensitivity armature dimension | Fully derivable from active Projects + Concerns + Conviction; adds authoring without adding behavior |
| Separate institutional_inertia and ethical_framework_anchor | Both moderated the same thing (tradition-bias); one term does both jobs |
| Fixed 40% governor weight | Governor should earn institutional influence over time; fixed weight allows gaming |
| Opinion of player (separate from Disposition) | Player-NPC covered by Disposition; Opinion covers NPC-NPC only; boundary was blurry |
| 35-NPC Event Impact Matrix symbolic table | Scoped to affected inner-circles only; full 35-NPC list was over-specified |

What was **not** cut:
- Five-field Opinion structure (Opinions of other NPCs need story/evidence for legibility)
- Knowledge structure (information topology is genuinely load-bearing)
- Settlement Meta-Armature (needed for settlement-scale interpretation)
- Faction Meta-Armature (needed for institutional interpretation distinct from leader's personal view)
- Domain Action proposal mechanism (generates the political loop)
- Gossip propagation (needed for NPC-NPC dynamics to be player-visible)
