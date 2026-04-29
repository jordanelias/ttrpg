<!-- [PROVISIONAL: 2026-04-28 session — batch 3 stress tests] -->
<!-- STATUS: PROVISIONAL — unique vectors not covered in 13_stress_tests_extended.md or 14_ners_stress_tests.md -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/15_stress_tests_batch3.md -->

# Stress Testing Batch 3: Political Dynamics System

**Prior coverage:**
- `13_stress_tests_extended.md`: Technical correctness — crashes, undefined behavior, implementation gaps. 20 issues.
- `14_ners_stress_tests.md`: NERS across all six directions — 9 design-fails, 8 gaps, 7 frictions.
**This batch:** Novel vectors only. Each test must not overlap prior coverage.

---

## NECESSARY

### N-33: Scar Domain Specificity vs Total Scar Count

**Probe:** Almud (Crown, Faith primary / Reason secondary) has acquired 3 Scars — all from social Contests targeting her *political* Beliefs, none touching her Conviction-domain Beliefs directly. Her total `scar_count` is 3.

**Trace:**
- §3.2 `modify_by_scar_count`: "Scar 3+: secondary leads." The formula uses `scar_count` (§2.2 State: "scars: count of revised Beliefs").
- Almud's 3 Scars are in non-Conviction domains (political theory, governance philosophy). Her Faith and Reason Convictions are untouched.
- The armature now weights Reason above Faith — her secondary Conviction leads her interpretive frame — because three non-Conviction-domain Beliefs were revised.

**Issue (N-33-A — Necessary):** The Scar count indiscriminately counts all Belief revisions regardless of their relationship to the NPC's Conviction. Three peripheral political Beliefs revised → the NPC's core Conviction orientation shifts. This is mechanically wrong: a person who revises three political positions hasn't necessarily undergone a foundational worldview shift. Conviction-domain Belief revisions should weight more heavily toward armature shift than peripheral Belief revisions.

This is a N (Necessary) failure: the scar-count mechanism does more than its job requires. A simpler and more accurate rule would be: only Conviction-domain Scars (Beliefs directly expressing the primary Conviction) trigger armature weight shifts.

**Patch:** Split scar count into two tracked values in §2.2:
```
scars_total: int  (all Belief revisions — existing, preserved for calcification gating)
scars_conviction: int  (Belief revisions in Conviction-domain specifically)
```
`modify_by_scar_count` uses `scars_conviction` for armature weight derivation. `scars_total` continues to gate calcification (§3.5: Belief unchallenged 8+ seasons). This makes the system Necessary — each counter does exactly the job it should.

---

### N-34: Project Horizon vs Stall Threshold

**Probe:** NPC A has a short-horizon Project (horizon: short, 1-3 seasons expected). NPC B has a long-horizon Project (horizon: long, 9+ seasons). Both stall for 8 seasons.

**Trace:**
- §6.2 Procedure C: "if project.seasons_stalled >= 8: execute_failure(project, npc)."
- The stall threshold is fixed at 8 regardless of horizon.
- NPC A's short Project has stalled 2.7–8× its expected duration before failing. The system correctly classifies it as failed (it was supposed to complete in 1-3 seasons and is now 8 seasons in with no progress).
- NPC B's long Project has stalled for 8 of its expected 9+ seasons. A long-horizon project that hasn't completed in 8 seasons may simply be slow, not failed. An 8-season stall on a 9-season horizon Project may be premature failure.

**Issue (N-34-A — Necessary):** A uniform stall threshold doesn't discriminate between project horizons. A short-horizon Project that stalls 8 seasons is clearly failed; a long-horizon Project that stalls 8 seasons may still be viable. The uniform threshold is Necessary (there must be a failure threshold) but not correctly calibrated.

**Patch:** Make stall threshold horizon-proportional. Add to §6.2 Procedure C:
```
stall_threshold:
    short horizon: 4 seasons (generous — 1-3 expected, 4 is clear failure)
    medium horizon: 6 seasons
    long horizon: 12 seasons
```
This makes the threshold Necessary rather than arbitrary.

---

### N-35: Population Disposition Update Trigger

**Probe:** Settlement Meta-Armature includes `population_disposition_weight = 0.1` drawing from `settlement.population_disposition_average`. This average is a statistical value for anonymous population NPCs.

**Question:** What events trigger population Disposition updates? The spec defines NPC Disposition updates through Memories and Procedure D, but population NPCs are statistical — they have no Memories or Procedures.

**Trace:** Population Disposition exists as a value in the Settlement Meta-Armature computation. It contributes 10% weight (normalized). But there is no mechanism in the spec that changes it. If it's authored at game start and never updated, it's static — contributing 10% of a constant value to every Settlement Signal forever.

**Issue (N-35-A — Necessary):** Population Disposition is computed but never updated in any procedure. It is Necessary that this value changes (settlement populations respond to starvation, military occupation, prosperity). A static population Disposition is not Necessary to include — it adds complexity without adding dynamic value. Either update it (add a trigger) or remove it from the Meta-Armature and simplify the weight formula.

**Patch:** Add a population Disposition update rule to §5.1. Two minimal options:
- Option A: Population Disposition updates at Accounting based on the current Faction Disposition toward Order/Prosperity stat. If Order/Prosperity > threshold: Disposition shifts +0.1/season. Below threshold: -0.1/season. Capped at ±3.
- Option B: Remove population_disposition_weight from the Settlement Meta-Armature; redistribute its 10% weight proportionally to the other tiers (institutional character → 22%, governor → remains). Simpler, no phantom update needed.

Recommend Option A if the provincial Order/Prosperity stat is already tracked (the extra weight is free). Recommend Option B if it isn't.

---

## ELEGANT

### E-36: Inner-Circle Competition Evaluation Function (Undefined)

**Probe:** §6.2 DA Proposal Phase: "if len(proposals_in_faction) > 1 AND any pair shares domain: winner = faction_meta_armature.select_proposal(proposals_in_faction)."

**`select_proposal` is not defined anywhere in the spec.** The Faction Meta-Armature is a weighted armature vector (Agency × Intent × Mechanism dimensions). How does an armature vector evaluate between competing proposals?

**Trace:** Two Church inner-circle NPCs propose theological DAs:
- NPC Himlensendt: Project domain "doctrinal", goal "centralize teaching authority."
- NPC Bishop Klausen: Project domain "doctrinal", goal "expand parish literacy."

The Faction Meta-Armature is Faith-dominant, institutional_stability 0.4. How does this armature select between two faith-doctrinal proposals with different project goals?

**Issue (E-36-A — Elegant, Critical):** The selection function is entirely abstract. "Faction Meta-Armature evaluates" is design intent, not a spec. The actual evaluation must compare each proposal's alignment with the armature's weights. But proposals are described by `project_domain` (a tag) and `goal` (text). The armature weighs Agency/Intent/Mechanism — not project domains directly. There is no defined mapping from project domain + goal to armature dimension alignment.

Without this function, the inner-circle competition is unimplementable. This is more severe than a gap — it's a missing core algorithm.

**Patch:** Define `select_proposal` in §6.2:
```
function select_proposal(proposals, faction_meta_armature):
    scores = {}
    for proposal in proposals:
        # Map project_domain to armature dimension alignment
        domain_alignment = lookup_domain_armature_alignment(proposal.project_domain)
        # Score = dot product of armature weights × domain_alignment vector
        score = sum(
            faction_meta_armature.weights[dim] * domain_alignment[dim]
            for dim in [Agency, Intent, Mechanism]
        )
        # Modifier: proposing NPC's Standing weight
        score *= standing_weight(proposal.npc.standing)
        scores[proposal] = score
    return max(scores, key=scores.get)
```
Requires an authored table: `domain_armature_alignment` maps each project_domain tag to alignment values per armature dimension. This is a small additional authoring item (~15-20 domain tags × 3 dimensions).

---

### E-37: Mood Vindicated and Resolved — Trigger Conditions Absent

**Probe:** §6.1 Mood transition table includes Vindicated and Resolved. Mood transition examples (same section) list:
- Successful DA proposal → Confident
- Treaty contradicting Conviction → Anxious or Humiliated
- Knot partner death → Grieving
- Conviction Scar → Distracted
- Public political defeat → Humiliated

**No examples trigger Vindicated or Resolved.**

**Issue (E-37-A — Elegant):** Two of eight Moods have no specified triggers. Their mechanical effects are defined (Vindicated: -1 Ob to action aligned with vindicating event; Resolved: -1 Ob to consistent actions, +1 Ob to inconsistent) but no event type produces them in the transition examples.

Without trigger conditions, Vindicated and Resolved cannot be set by the engine. They are mechanically defined but experientially inert.

**Patch:** Add to §6.1 Mood transition examples:
- Vindicated: NPC's Concern resolves with Memory evidence that directly confirms their prior Belief (strong match, high confidence). NPC interpretation is confirmed, not challenged. Duration: 1-2 seasons.
- Resolved: NPC completes their active Project (progress = 10). The Project completion consolidates purpose. Duration: 1-2 seasons (replaced by new Project goal emerging).

---

### E-38: Symbolic vs Armature Resonance — Two Independent Interpretation Systems

**Probe:** The spec has two mechanisms for NPC interpretation of events:
1. **Armature** (§3): NPCs interpret events through weighted Agency/Intent/Mechanism dimensions derived from Conviction/Personality/Scars. Produces Concerns.
2. **Symbolic resonance** (§4.1, §10): 210-entry Conviction × event-type table produces `{aligned, neutral, contradicted}` for symbolic_effects in the Event Impact Matrix.

**Question:** How do these two systems interact? Does a Faith-aligned symbolic resonance also modify the NPC's armature interpretation? Or are they parallel systems that each feed different outputs?

**Trace:** Event: "Crown restricts Church appointments." Faith NPC Himlensendt.
- Armature: Himlensendt's Faith Conviction + high institutional_deference → armature weighs institutional-force Agency heavily. Concern question: "What institutional pressure is the Crown responding to?"
- Symbolic resonance: Crown-Church event with Conviction = Faith → `contradicted` (Crown is opposing Church authority, which contradicts Faith values). This enters symbolic_effects for Faith-aligned inner-circle NPCs.

**Issue (E-38-A — Elegant):** The spec never defines what symbolic_effects DO downstream. They appear in the Event Impact Matrix as a field. But no procedure reads symbolic_effects to produce any mechanical output. The armature produces Concerns. What does symbolic resonance produce?

Looking at the Matrix structure (§4.1): `symbolic_effects[]: actor_id, conviction_resonance, institutional_resonance`. These fields are authored per event. But §6.2 procedures don't consume them. They don't modify Mood, Concern salience, Opinion drift, or anything else.

**Issue (E-38-B — Necessary):** If symbolic_effects are never consumed by any procedure, the 210-entry authored table is pure waste. This is a Necessary failure: either define what symbolic_effects produce, or remove them and save 210 authored entries.

**Patch:** Define symbolic_effects consumption in §4.1 or §6.2:
"symbolic_effects feed Concern salience modifiers during Procedure B generation: if NPC's Conviction is `contradicted` by the event's symbolic_effects → Concern salience +1. If `aligned` → Concern salience -1 (NPC understands the event through their own framework, less uncertain). This means ideologically challenging events generate higher-urgency Concerns in affected NPCs — mechanically connecting the symbolic resonance table to NPC behavior."

---

## ROBUST

### R-39: Scene Slate Discretionary Budget — Does the Player Get Any?

**Probe:** Player has 5 scene actions per season. Evaluate what mandatory Priority 1-3 content exists in a typical mid-campaign season (Year 4).

**Mandatory scene content (typical):**
- Priority 1: Faction leader removal attempt (rare, but possible) — 1 scene
- Priority 2: Heresy investigation in Verdmuld — 1 scene
- Priority 3: 3 Concern-driven Outreach scenes (Himlensendt, Almud, Baralta have active Concerns about player) — 3 scenes

Total mandatory: 5 scenes. Player's full budget consumed.

**Discretionary budget for:** Investigation, Knot maintenance, Standing advancement scenes, proactive social building, merchant/fieldwork scenes → **0.**

**Issue (R-39-A — Robust):** In a politically active mid-campaign season, the player may have zero discretionary scene actions. All 5 actions are consumed by mandatory content bubbling up from NPC Concerns and existing crises. The Robust criterion requires the system to let the player "think strategically" and "customize characters" — but this requires discretionary budget.

A player who wants to investigate Himlensendt's Project or build Disposition with a new NPC is structurally prevented from doing so by the NPC-driven scene demand.

**Issue (R-39-B — Smooth):** Concern-generated Outreach at Priority 3 means NPCs pursuing the player (from their Concerns) compete directly with the player pursuing NPCs (Investigation, Read actions). In a politically rich campaign, NPCs always have the initiative — the player reacts to NPC-driven scenes rather than directing their own political agenda.

**Patch:** Add to §7.6 NPC Outreach Generation: "Concern-driven Outreach scenes are generated as available content, not mandatory scenes. A player who declines to attend a Priority 3 Outreach scene: the NPC's Concern remains active and the scene is offered again next season at the same priority. Missing a Concern-driven Outreach scene is not a missed consequence — it is a deferred conversation. Only Priority 1-2 scenes carry missed-consequence weight." This restores player agency without losing NPC Concern expressiveness.

---

### R-40: NPC Standing Mobility — Static or Dynamic?

**Probe:** The Faction Meta-Armature weights inner-circle NPCs by Standing (S4: 0.3, S5: 0.5, S6: 0.7, S7: 1.0, leader: ×1.5). These weights are specified as fixed. Does NPC Standing change during a campaign?

**Trace:** Marshal Ehrenwall (Standing 6, Crown inner-circle) fails 3 consecutive Domain Action proposals. His Project stalls and fails. Historically, a military commander who fails repeatedly loses political influence. Does Ehrenwall's Standing drop?

The spec defines Standing changes only for the player (existing Standing ladder system). NPC Standing within their faction is mentioned as an input to Meta-Armature weighting but there is no NPC Standing mobility rule.

**Issue (R-40-A — Robust):** If NPC Standing is static, the Faction Meta-Armature weight distribution never changes from game start (except via player reaching Standing 5+). A politically dynamic faction should have NPCs rising and falling in institutional influence based on Project success, Domain Action outcomes, and political alignment. Static Standing produces a fixed power structure — the same voices carry the same weight for the entire campaign.

This reduces robustness: "allows for customization" and "emergent narrative hooks" are weakened when the faction's power distribution never shifts. A failing Marshal who retains full Meta-Armature weight feels unrealistic and removes a strategic lever for players.

**Patch:** Add to §5.3 Faction Meta-Armature or §6.2 Procedure C: "NPC Standing is recalculated at Campaign Year boundary (not per-season — institutional advancement/demotion is slow). NPC Standing increases by 1 if: Project completed AND at least one successful DA proposal this year. NPC Standing decreases by 1 if: Project failed AND three consecutive DA proposal failures this year. Standing cannot drop below S4 (inner-circle minimum) or exceed S7 without specific authored events. Standing changes update Meta-Armature weights at the next Year's start."

---

### R-41: Adversarial Crisis Masking — Manufacturing External Events to Suppress Anomaly Detection

**Probe:** Player is running covert destabilization operations inside Crown faction: engineering NPC Disposition drops toward Almud, manufacturing political defeats for Crown inner-circle. Player knows anomaly detection requires "no major external crisis event this season" to fire.

Player deliberately engineers a border skirmish (by providing intelligence to a neighboring faction) that qualifies as a "major external crisis" — suppressing the anomaly detection trigger while their destabilization continues undetected.

**Trace:**
- Anomaly detection condition (§5.4): "≥3 inner-circle NPCs simultaneously {Disposition-with-leader < baseline} AND ≥2 negative Mood states AND **no major external crisis event this season**."
- Player-manufactured border skirmish → scale_signature includes {faction}, material_effects magnitude ≥2 (per patch ST-22) → qualifies as major external crisis.
- Anomaly detection suppressed. Player's internal destabilization goes undetected.

**Issue (R-41-A — Robust):** The anomaly detection suppressor was designed to prevent false positives (NPCs reacting to external pressure being misread as internal conspiracy). But the suppressor creates a strategic exploit: a sophisticated player can permanently disable anomaly detection by maintaining a low-level external crisis, masking any internal manipulation.

**Assessment:** This is arguably the INTENDED robust strategic space — a player who is sophisticated enough to manufacture external crises to mask internal operations is playing the game correctly. This isn't a failure; it's a feature of the system's depth.

**However**, the system should detect repeated patterns. A faction experiencing simultaneous external crisis AND anomaly-pattern indicators every season for 3+ seasons is statistically abnormal.

**Patch (optional, robustness enhancement):** Add to §5.4: "Anomaly detection persistence: if anomaly-pattern indicators (≥3 NPCs below baseline, ≥2 negative Moods) persist for 3+ consecutive seasons despite ongoing external crises, Faction Meta-Armature generates an additional Concern: 'External pressure alone does not explain our internal difficulties' at salience 3. This fires even during active external crises if the pattern is persistent." This creates a second-order anomaly detection that can't be indefinitely suppressed by manufactured crises.

---

### R-42: Passive NPC Memory Cap and Replacement

**Probe:** Passive NPC village mayor in Verdmuld. Lite architecture: "Conviction, Disposition, 1 Concern, 1 Opinion of player, 3 Memories." A major event season fires 4 Memory-generating events affecting this NPC.

**Trace:**
- 3-Memory cap hit on fourth event.
- Replacement rule: §2.6 for Active NPCs: "lowest-salience Memory dropped or merged." But §2.6 is written for Active NPCs. Passive NPC Memory replacement rule is not separately specified.
- Does the same replacement logic apply to Passive NPCs? Or does the 3-Memory cap use a different replacement priority?

**Issue (R-42-A — Necessary):** Memory replacement rules for Passive NPCs are unspecified. Passive NPCs participate in Settlement Signals (their Memories are aggregated). If Passive NPCs use identical replacement logic to Active NPCs, the system is consistent. But if Passive NPC Memory replacement is undefined and implementations choose arbitrary rules, Settlement Signal aggregation becomes inconsistent across implementations.

**Patch:** Add to §1 NPC Tier Stratification or §2.6: "Passive NPC Memory replacement follows identical rules to Active NPC replacement (lowest salience, timestamp tie-break, merge when same event_type + overlapping participants). The rules apply to the 3-Memory cap exactly as they do to the 10-Memory cap."

---

## SMOOTH

### S-43: Knowledge → Belief Trigger vs Procedure Ordering

**Probe:** §2.7: "When high-salience Knowledge (≥4) is acquired and contradicts an active Belief's domain, Procedure B generates a Concern."

Knowledge is acquired via Procedure E Knowledge sharing (which runs AFTER Procedure B in the Accounting sequence: B → DA → C → D → E).

**Trace:**
- Season N Accounting: Procedure E fires. NPC gains new Knowledge (salience 4, contradicts active Belief).
- The Knowledge-triggered Concern condition (§2.7) states "Procedure B generates a Concern" — but Procedure B already ran this Accounting, before E.
- Knowledge acquisition in Season N cannot trigger a Procedure B Concern in Season N.
- Season N+1 Accounting: Procedure B runs. The Knowledge entry now exists. The generation check fires: Knowledge salience ≥4, contradicts Belief domain → generates Concern.

**Issue (S-43-A — Smooth):** The Procedure ordering creates a 1-season lag between Knowledge acquisition and Concern generation. An NPC who learns something important in Season N doesn't begin actively wondering about it until Season N+1.

This is the same lag identified in S-VERT-A for Settlement Signal, but in a different system path. The cumulative effect: significant cross-NPC information propagation chains are consistently delayed by 1 full Accounting at each hop.

**Assessment:** The lag is technically correct given the sequential Accounting model. But it means the system's information propagation has an inherent minimum latency of 1 season per hop. For the player, this means events and their consequences are always at least 1 season apart. This may feel smooth (realistic deliberation time) or disconnected (consequences too delayed). **Flag as a known playtest concern** rather than a failure.

**Patch (optional):** For high-salience Knowledge (salience 5 specifically): immediate Concern generation in Procedure E, without waiting for Procedure B next season. "Priority Knowledge Concern: when an NPC acquires Knowledge at salience 5 during Procedure E, a Concern is immediately generated in the same Accounting pass (appended to npc.concerns; cap enforced). Only for salience-5 (extraordinary information) — standard Knowledge at salience 4 waits for next B." This creates a fast path for the most significant information while preserving the standard seasonal rhythm.

---

### S-44: Player Disposition Across Scale — Mayor Disposition and Settlement Signal

**Probe:** Player has Disposition +3 with mayor of Verdmuld (Passive NPC). The mayor has 3 Memories, all positive-affect, partially generated by player interactions. Settlement Signal aggregates Passive NPC Memories weighted by `npc.local_disposition_with_player`.

**Trace from §5.2:**
```
weight = memory.salience × npc.local_disposition_with_player
```
Mayor's Disposition with player = +3. Mayor's Memories are player-positive. Weight for mayor's Memories in Settlement Signal = salience × 3. Mayor's Memories are substantially overweighted compared to anonymous Passive NPCs with Disposition 0.

**Issue (S-44-A — Smooth):** The Settlement Signal weighting formula uses `npc.local_disposition_with_player` as a Memory weight multiplier. But this field is `Disposition_WITH_PLAYER` — the NPC's relationship to the player. Using this as a general Memory weight means: NPCs who like the player have their Memories weighted more heavily in the Settlement Signal.

This produces a smooth consequence: settlements where the player has invested in relationships are more sensitive to events the player was involved in (those NPCs have high Disposition, their Memories of player-involving events are overweighted). The Signal reflects the player's relational footprint in the settlement.

**However:** The formula weights ALL of the high-Disposition NPC's Memories more heavily — not just player-involving Memories. The mayor's Memory of "the miller's daughter was married" (player-uninvolved) gets weight = salience × 3 just because the mayor likes the player. This is incorrect — Disposition with player shouldn't amplify memories of unrelated events.

**Patch:** In §5.2 compute_settlement_signal: "weight = memory.salience × npc.local_disposition_with_player if memory.participants includes player else memory.salience × 1.0." Non-player Memories use flat weight 1.0; player-involving Memories are amplified by the NPC's Disposition with the player. This correctly scopes the player's relational footprint without distorting unrelated Memory weights.

---

### S-45: Read Action at Disposition +3 — Reveals Only Mood, Not More

**Probe:** §7.1 Read action table:
- Any Disposition: reveals current Mood.
- Disposition +2 (Friendly): reveals one observable behavior label.
- Disposition +3+: "No additional structured information."

**Issue (S-45-A — Smooth / Elegant):** The Read action table shows strictly increasing Disposition unlocking more information — until Disposition +3, which unlocks less than +2. At +2, the player gets behavior label. At +3 (a higher investment), the player gets nothing additional through Read. The Trusting (+3) relationship actually provides fewer mechanical Read benefits than the Friendly (+2) relationship.

The spec explains this: at +3, NPC "voluntarily reveals partial Concern information through Outreach scene dialogue (candor), not through direct Read access." The intent is clear — Trusting relationships unlock Outreach depth, not Read depth. But the Read table as written creates a misleading progression where higher Disposition appears to be a worse deal for Read actions.

**Issue (S-45-B — Necessary):** The Read action at Disposition 0, +2, and +3 creates a 3-tier system where only +2 has incremental Read value over baseline. The +3 tier's value is entirely outside the Read action (in Outreach scenes). This means there are two separate information systems (Read, Outreach) with separate Disposition gates. Players who invest in Disposition +3 expecting better Read access are structurally disappointed.

**Patch:** Reframe the Read table in §7.1 to make the information architecture explicit: "Disposition +3+: Read action reveals Mood only (same as any Disposition). The value of Trusting relationships is unlocked through Outreach scenes, not Read. Investing to Disposition +3 does not improve Read outcomes; it unlocks NPC-initiated candor in scenes." This is a clarity patch, not a mechanical change. Players should know this before investing in Trusting relationships.

---

### S-46: New Project After Completion — Horizon and Goal Derivation

**Probe:** §6.2 Procedure C: when a Project completes, `generate_new_project(npc)` fires. The spec does not define how the new Project's goal, horizon, domain, or domain_action_required flag are determined.

**Trace:**
- Himlensendt's Project "Consolidate doctrinal authority over parish clergy" completes (progress = 10).
- `generate_new_project(Himlensendt)` fires.
- What is the new Project? What horizon? What domain?

**Issue (S-46-A — Smooth):** Project generation is undefined. The only constraint from §2.4 is "new Projects may also be generated in response to Conviction Scars or Project failures." For completion-triggered replacement, there is no specification.

If new Projects are authored at game-start (one per Active NPC), and replacement Projects are not pre-authored, the engine must procedurally generate them. There is no procedural generation rule.

**Options for how this could work:**
1. **Pre-authored replacement queue:** Each NPC has 2-3 authored Projects in sequence. When one completes, the next in queue activates. Requires ~70-100 additional authored Projects.
2. **Domain-continuation rule:** The new Project is in the same domain as the completed one, with a higher-scale goal. Himlensendt's next Project advances from "parish clergy consolidation" to "theological school establishment." Derivable from context.
3. **Conviction-based procedural:** New Project is derived from NPC's Conviction primary and current Concerns. Faith + current Concern about Crown interference → Project: "Establish independent doctrinal review process."

**Patch:** Add to §6.2 Procedure C and §10 Content Authoring: "Project replacement after completion uses a pre-authored replacement queue (2-3 Projects per Active NPC, sequenced). If the queue is exhausted, the engine generates a Conviction-domain Project using the NPC's current top-salience Concern as the goal basis. The Conviction-based fallback is a minimal authored frame: '{Conviction_action_verb} {Concern_domain}' with horizon = medium and domain = Concern_domain." This specifies the fallback while keeping authored content as the primary path.

---

## ELEGANT

### E-47: Two-Season Settlement Signal Aggregation — Is the Window Necessary?

**Probe:** §5.2 `compute_settlement_signal` aggregates Passive NPC Memories from "last 2 seasons." Why 2 seasons?

**Trace:**
- A 2-season window smooths Signal volatility: a single bad season doesn't swing the Signal dramatically.
- But it also means the Settlement Signal always lags real conditions by up to 2 seasons.

**Issue (E-47-A — Elegant):** The 2-season window is unspecified as to its derivation. Why 2 and not 1 or 3? A 1-season window produces volatile Signals. A 3-season window produces very lagged Signals. The choice affects game pacing — 2-season lag means a rapidly evolving political situation is always 1-2 Accountings behind in its Settlement representation.

More importantly: the window is uniform across all settlement types (city, outpost, village). A city with 20+ Passive NPCs can produce a statistically stable Signal with a 1-season window. A remote outpost with 2-3 Passive NPCs needs a longer window for stability.

**Issue (E-47-B — Elegant):** The 2-season window is not elegant — it's a magic constant with no derivation. A more elegant formulation: window length = max(1, ceil(5 / passive_npc_count)). Sparse settlements use longer windows (more averaging needed); dense settlements use shorter ones. This makes the temporal behavior of the Signal derive from settlement characteristics rather than a flat constant.

**Patch:** Replace the flat "last 2 seasons" with: "Signal window = max(1, round(5 / passive_npc_count, 0)) seasons. Dense settlements (10+ Passive NPCs) use a 1-season window (responsive). Sparse settlements (2-3 Passive NPCs) use 2-3 season windows (smoothed). Remote outposts with 1 Passive NPC use 5-season windows." This is more elegant: the formula derives the window from existing data (NPC count).

---

### E-48: Faction Meta-Armature — max_scars Undefined

**Probe:** §5.3 Faction Meta-Armature:
```
institutional_stability:
    weight: 0.4 × (1 - (total_inner_circle_scars / max_scars))
```
`max_scars` is undefined. The formula requires a denominator.

**Trace:**
- If max_scars = 10: institutional_stability weight decays to 0.4 × (1 - 5/10) = 0.2 when inner-circle has 5 Scars.
- If max_scars = 35 (one per Active NPC): same 5 Scars → 0.4 × (1 - 5/35) = 0.343. Barely decays.
- The denominator determines how quickly institutional character degrades under inner-circle trauma.

**Issue (E-48-A — Elegant):** `max_scars` is a magic constant that must be defined to make the formula Elegant and implementable. The choice encodes the designer's model of how quickly a faction can lose its character. Too low: factions destabilize rapidly. Too high: institutional character is nearly permanent.

**Patch:** Define `max_scars` as the per-faction inner-circle size × 2. Rationale: the maximum plausible Scar load for a functional faction is 2 Scars per inner-circle member (more than this and the faction has structurally transformed). For a Crown inner-circle of 8 Active NPCs: max_scars = 16. This makes max_scars derive from faction composition, not a magic constant. Add to §5.3: "max_scars = inner_circle_active_npc_count × 2. Varies per faction by inner-circle size."

---

## NECESSARY + SMOOTH COMBINED

### NS-49: visible_actions Authoring for Procedurally-Generated Projects

**Probe:** §2.4 Project structure includes `visible_actions: actions taken to advance (player-observable)`. These are authored per Project. §7.2 Observable Behavior Surfacing uses `visible_action` as the content for ambient encounter, Read at +2, and Investigation outputs.

**Trace:** Himlensendt's Project completes. A procedurally-generated replacement Project ("Establish independent doctrinal review process") has no authored `visible_actions`. §7.2 outputs become: ambient encounter with no content ("You notice Himlensendt doing... something"), Read at +2 with no label, Investigation revealing nothing.

**Issue (NS-49-A — Necessary):** If Projects can be procedurally generated (via the §6.2 fallback from S-46-A patch), their `visible_actions` have no authored content. The player-facing observation surface (§7) breaks entirely — it produces empty or null outputs. All three tiers of Observable Behavior Surfacing depend on authored `visible_actions`.

**Issue (NS-49-B — Smooth):** The Observable Behavior surface breaks silently — there's no error, just no content. The player's 25% ambient encounter fires and produces nothing. The Read at +2 reveals no label. Investigations return empty. This is a smooth-failure: the system doesn't crash, but it produces null player experience.

**Patch:** For procedurally-generated Projects, derive visible_actions from a template: "{Conviction_action} in {project_domain} domain. Observed: {Conviction_observable_behavior}." Example: Faith + theological domain → "Himlensendt is conducting extensive consultation with Church scholars." This requires ~20 authored templates (7 Convictions × 3-4 domain categories) — a small authoring cost that keeps the Observable surface functional for generated Projects. Add to §10 Content Authoring.

---

## ROBUST + SMOOTH COMBINED

### RS-50: Calcified Belief Path A — Does Calcification Persist After Scar?

**Probe:** NPC has a calcified Belief (unchallenged 8+ seasons). Player wins a Total Victory Contest targeting this Belief (Path A). Belief becomes a Scar. The Belief domain is now a Scar — the NPC's previous position is gone, replaced by the contest-imposed revision.

**Question:** Is the resulting Scar itself calcified? Does calcification transfer to the post-revision state?

**Trace:**
- Pre-Contest: Belief in domain X, calcified (8+ seasons). Requires 3+ contradicting Memories for self-correction (Path B). Path A at +1 Ob.
- Contest succeeds: Scar applied. Old Belief replaced by revised position.
- New position: has existed for 0 seasons. Calcification counter resets to 0 by definition (it tracks "unchallenged for 8+ seasons" — new position is trivially challenged, it was just revised).

**Assessment: CLEAN.** Calcification does not transfer. The new Belief starts fresh with no calcification. The Scar correctly represents that the NPC's position was recently forcibly revised — and is now subject to standard (not calcified) thresholds for future modification.

**However:**

**Issue (RS-50-A — Robust):** The new post-Contest Belief is authored by the player through the Contest. An NPC whose Belief was calcified for 8+ seasons just had it overturned by social argument. The NPC's armature hasn't changed — it still weights the old seeking-tags. The new Belief may contradict the NPC's Conviction (it was imposed by a Contest, not self-generated). This creates a state where the NPC holds a Belief that their own armature would not generate — a kind of imposed cognitive dissonance.

The spec handles this partially: the new Belief can be challenged by Path B Concerns. The NPC's armature will interpret subsequent events and may accumulate contradicting Memories for the imposed Belief, eventually self-correcting back toward their Conviction. This produces a realistic recovery arc.

**No patch required.** Confirm this behavior explicitly in §3.5: "A Belief imposed via Path A Contest may contradict the NPC's Conviction. The NPC's armature will autonomously generate Concerns about it over subsequent seasons. A Conviction-contradicting imposed Belief typically self-corrects within 4-8 seasons through Path B Concern accumulation, unless the player reinforces it with additional Outreach." This makes the dynamic explicit and provides players with a design hook (sustain the imposed Belief through continued relationship investment or watch it erode).

---

## Summary Table

| ID | Criterion | System Area | Issue Type | Severity |
|---|---|---|---|---|
| N-33-A | Necessary | Scar count | Conviction vs peripheral Scar indistinguishable | **Design-Fail** |
| N-34-A | Necessary | Project stall | Stall threshold not horizon-proportional | Friction |
| N-35-A | Necessary | Population Disposition | Update trigger missing — static value in dynamic formula | **Design-Fail** |
| E-36-A | Elegant | DA inner-circle competition | `select_proposal` function undefined — unimplementable | **Critical** |
| E-37-A | Elegant | Mood table | Vindicated and Resolved have no trigger conditions | **Design-Fail** |
| E-38-A | Elegant | Symbolic resonance | symbolic_effects consumed by no procedure | **Design-Fail** |
| E-38-B | Necessary | Symbolic resonance | 210 authored entries with no mechanical output — waste | **Design-Fail** |
| R-39-A | Robust | Scene Slate | Player may have zero discretionary scene actions mid-campaign | **Design-Fail** |
| R-39-B | Smooth | Scene Slate | NPCs always hold initiative; player reacts rather than directs | Friction |
| R-40-A | Robust | NPC Standing | Standing static — faction power distribution never shifts | **Design-Fail** |
| R-41-A | Robust | Anomaly detection | Crisis masking exploit exists; optional persistence counter | Design choice |
| R-42-A | Necessary | Passive NPC Memory | Replacement rules not specified for Passive tier | Gap |
| S-43-A | Smooth | Knowledge → Concern | 1-season lag is structural; cumulative across propagation hops | Friction (known) |
| S-44-A | Smooth | Settlement Signal | Disposition-with-player amplifies ALL Memories, not just player-involving | **Design-Fail** |
| S-45-A | Smooth | Read action | +3 Disposition yields fewer Read benefits than +2 — misleading progression | Friction |
| S-45-B | Necessary | Read action | Two separate information systems (Read/Outreach) with separate gates | Gap |
| S-46-A | Smooth | Project generation | Replacement Project derivation unspecified | **Design-Fail** |
| E-47-A | Elegant | Settlement Signal | 2-season window is a magic constant | Friction |
| E-47-B | Elegant | Settlement Signal | Uniform window regardless of settlement density | Friction |
| E-48-A | Elegant | Faction Meta-Armature | `max_scars` undefined in institutional_stability formula | **Critical** |
| NS-49-A | Necessary | visible_actions | Procedurally-generated Projects produce null Observable Behavior | **Design-Fail** |
| NS-49-B | Smooth | Observable Behavior | Silent null-output failure when visible_actions missing | **Design-Fail** |
| RS-50-A | Robust | Imposed Belief | Post-Contest Belief arc unspecified; correct behavior needs documentation | Clarify |

---

## Issue Counts (Batch 3)

**Critical:** 2 (E-36-A `select_proposal` undefined; E-48-A `max_scars` undefined)  
**Design-Fail:** 11 (N-33-A, N-35-A, E-37-A, E-38-A/B, R-39-A, R-40-A, S-44-A, S-46-A, NS-49-A/B)  
**Gap:** 2 (R-42-A, S-45-B)  
**Friction:** 6 (N-34-A, R-39-B, S-43-A, S-45-A, E-47-A/B)  
**Design choice / clarify:** 2 (R-41-A, RS-50-A)

**Total: 23 issues across 18 unique tests.  
Zero overlap with Batches 1 (13_stress_tests_extended.md) or 2 (14_ners_stress_tests.md).**

---

## Running Totals (All Three Batches)

| Severity | Batch 1 | Batch 2 | Batch 3 | Total |
|---|---|---|---|---|
| Critical | 1 | 1 | 2 | **4** |
| Design-Fail | — | 9 | 11 | **20** |
| High / Significant | 8 | — | — | **8** |
| Gap | 2 | 8 | 2 | **12** |
| Friction / Medium / Low | 13 | 7 | 6 | **26** |
| Clarify / Acceptable | — | 4 | 2 | **6** |
| **Total** | **20** | **25** | **23** | **68** |
