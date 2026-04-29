<!-- [PROVISIONAL: 2026-04-28 session — top-down audit] -->
<!-- STATUS: PROVISIONAL — holistic audit, drove consolidation in 12 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/11_top_down_audit.md -->

# Top-Down Audit: Political Dynamics Session

This audit reads the system as it now stands across all 10 committed documents and assesses it as a single proposal. The view is from above, not from within any single iteration.

---

## §1 What the System Is

A unified architecture for political dynamics in Valoria, structured in five layers:

**Layer 1 — Per-NPC Inner State.** Each named NPC carries Identity (Conviction primary/secondary, four Personality dimensions), State (Mood, Beliefs, Scars, Disposition with player), Concerns (1-3 active), Projects (1-2 active), Opinions (NPC-NPC only), Memories (5-10), Knowledge (info-rich NPCs).

**Layer 2 — Three-Dimension Armature.** Conviction + Personality + Project domain + Scar count produce weighted interpretive armatures across Agency, Intent, Mechanism dimensions. Armatures interpret events into Concerns. Replaces the original 630-template library; characteristic-derived rather than table-derived.

**Layer 3 — Event Impact Matrix.** Computed once per event from existing data + a 210-entry symbolic resonance table. Lists material effects, symbolic effects (scoped to inner-circles of affected factions), relational effects, scale signature, visibility. Consumed by all armatures interpreting the event.

**Layer 4 — Meta-Armatures at Two Higher Scales.**
- Settlement Meta-Armature: tenure-scaled governor + Passive NPC aggregate + institutional character + population baseline. Weights normalized to 1.0 when tiers are absent.
- Faction Meta-Armature: Standing-weighted inner-circle aggregate + leader 1.5× amplification + institutional_stability (single merged term that decays as inner-circle Scars accumulate).

**Layer 5 — Four Procedures + Real-Time Mood.**
- Real-time Mood (set at event resolution, not batched).
- Procedure B: Concern generation and resolution (with calcified-wrong-Belief gating, Knowledge-triggered Concerns).
- Procedure C: Project advancement (with established-vs-new Project distinction, Domain Action proposal flagging, completed-Project relational legacy).
- Procedure D: Opinion drift (with Memory-reference salience floor, hard clamp on affect_axis bounds).
- Procedure E: Off-screen interactions (60% ambient inner-circle, 10% Distant Contact cross-faction, Knowledge sharing, Gossip propagation; Distracted Mood drops to 20%).

**Connecting mechanism — Domain Action proposals.** NPCs with Project advancement needs propose Domain Actions to their faction. Inner-circle competition resolves selection via Faction Meta-Armature weighting. Conviction-aligned supporters give -1 Ob; conviction-contradicted opposers give +1 Ob. Failed proposals stall the proposer's Project; successful proposals advance it. Generates the political loop.

**Crisis behaviors.** Faction crisis threshold (≥40% inner-circle in Distracted/Grieving) → institutional autopilot. Anomaly detection (≥3 NPCs simultaneously divergent without external cause) → faction-level "internal destabilization" Concern. Minimum inner-circle friction (count <3) → +1 Ob on all Domain Actions.

**Player-side mechanics.** Loyalty Cover (+1 Cover per major loyalty signal, max +2). Witness Mode information cap (3 Read results per Accounting). Player Disposition investment shifts crisis priority. Knowledge access via Disposition gates on sharing sensitivity.

**Cascade attenuation.** ×0.7 signal decay per scale boundary crossed. Salience below 2 generates Concerns but doesn't influence Domain Action selection.

**Long-run mechanisms.** Referenced Memories gain +0.5 salience per use (founding relationship Memories persist if they're being used to interpret current events). Calcified wrong Beliefs (8+ seasons unchallenged) require 3+ contradicting Memories vs standard 2. Project legacy: completed Projects produce ±0.5 affect_axis on supporters/obstructors in subsequent Opinion drift. City-state Domain Actions (collapsed factions) limited to Influence/Wealth.

---

## §2 What the System Achieves

### 2.1 Throughline Completion

The session's central technical accomplishment is **mechanizing T-27 (Effects Real, Explanation Wrong)** for the first time. T-27 was canonically committed but had been deferred — "Conviction Scar targeting tied to specific effect/explanation mismatches" was pending. The Conviction-weighted seeking-tag system in the armature delivers that targeting.

Three additional throughlines are extended (mechanical specifications added where mechanism was implicit):
- **T-14 Conviction Architecture.** Armature mechanizes how Conviction structures interpretation.
- **T-23 NPC Arc Emergence.** Concern → Memory → Belief Revision → Scar provides the explicit chain.
- **T-25 Generational Arc.** Project shifts toward succession positioning operationalize the court-political dimension.
- **T-30 Information Asymmetry.** Knowledge structure + interpretive-frame access (M-8 extension) deepens asymmetry.

### 2.2 Meta-Throughline Extensions

- **М-1 (Pressure continuous):** New pressure source via NPC autonomous Outreach generation.
- **М-5 (Scales connect):** Three new scale-bridges — Settlement Signal, Knowledge propagation, Outreach generation cascade.
- **М-8 (Vertical-position gating):** New gate type — interpretive-frame gating. Same Knowledge fact interpreted differently by different Convictions; player must access the holder's frame.

### 2.3 Architectural Properties

- **Bidirectional cascading verified.** Vertical down (faction → settlement → personal), vertical up (personal → settlement → faction), lateral within and across factions, diagonal cross-scale. All paths tested in T-1 through T-11 and ST-1 through ST-12.
- **Different player histories produce different NPC behavior** (Probe 3.1 in iterative testing). Same NPC, same Project, same completing event → categorically different political dynamics depending on accumulated Memory.
- **Cascade attenuation prevents runaway propagation** (ST-1 patch). Personal events can affect faction decisions but only when the chain is short and salience is high.
- **Faction crisis behavior specified** (ST-6 patch). Mass NPC distraction produces institutional autopilot, not incoherence.

### 2.4 Computational Discipline

The four-procedure structure, real-time Mood, lazy Domain Action evaluation, scope-capped Event Impact Matrix, and Distant Contact reduced-frequency track produce a system whose computational requirements scale linearly with NPC count and event count. Honest about not having profiled actual ms costs.

---

## §3 What's Internally Consistent

Reading across all 10 documents, the architecture is internally consistent in these ways:

**Real-time Mood is global.** Once adopted in ST-10 (integration test), it propagates to all subsequent specifications. Procedure A is fully eliminated. Immediate Update is fully eliminated.

**Three-dimension armature is global.** Threat-sensitivity is removed throughout. Subsequent stress tests don't re-introduce it.

**Single institutional_stability term is global.** The previous separate institutional_inertia + ethical_framework_anchor terms are merged in 09 and remain merged in 10.

**Opinion of player vs Disposition boundary is clear.** Established in 09 (boundary clarification): Disposition for direct interactions, Opinion for non-player-present behavior. NPC-NPC Opinions only. No subsequent specifications muddle this.

**Cascade attenuation is consistent.** Once ×0.7 per boundary is established (ST-1), all subsequent test reasoning uses it.

**affect_axis bounds are consistent.** Hard clamp at ±3 (ST-11) applies globally.

---

## §4 Known Inconsistencies and Open Items

This is what an honest top-down read finds.

### 4.1 Documents 01-08 are not retroactively edited

Documents 01 (gap audit) through 08 (Event Matrix + Meta-Armatures) are committed as written, before the streamlining in 09 and stress test patches in 10. They reference systems that have been changed:
- 04 and 05 still reference Procedure A (Mood batch) and Threat-sensitivity dimension
- 05 and 06 reference 35-NPC Event Impact Matrix scope
- 06's "Patch Set" did not include institutional_stability merger
- 02 and 03 reference RP-balance system that was reframed in 04 to Opinions-with-affect

**Severity:** Documentation, not architecture. The system as it stands is coherent — but a reader of the session in document order encounters superseded specifications without flag. The session index (00) lists documents but doesn't mark which specifications are current vs superseded.

**Recommended fix:** Update 00_session_index.md to flag "current spec" vs "preserved-for-history" status per document. 09 and 10 collectively are "current spec." 01-08 are "stage documents preserved for the design arc; specific mechanisms may have been superseded."

### 4.2 Outstanding Jordan decisions accumulated, not pruned

The session log shows decisions queued at multiple points. No consolidated list exists in 00 reflecting current state. Outstanding items per my read:

1. **Personality dimension calibration** (~140 values across 35 NPCs)
2. **Conviction → armature weight mappings** (105 weights)
3. **Personality → armature modifier rules** (12 modifier entries)
4. **Event dimension profiles** (~270 entries)
5. **Sentence frame templates** (~15 frames)
6. **Conviction × event-type symbolic resonance table** (210 entries)
7. **Settlement institutional character bias** (6 entries)
8. **Faction institutional_stability starting values** (7 entries — one per faction, replaces prior 14)
9. **Domain Action sponsor mapping** (~30 entries)
10. **Starting Projects per Active NPC** (35)
11. **Starting Opinions, NPC-NPC** (~200, reduced from prior estimate by removing player Opinions)
12. **Knowledge seeding** (~150)
13. **Knot integration dialogue fragments** (~30)
14. **Gossip text templates** (~100)
15. **Wrong-Belief Investigation interaction:** Option A forgiving vs Option B harsh. Recommendation: Option B per Ω-d.
16. **Restoring Intelligence as 6th faction stat** (carried from prior session).
17. **LICENSE decision** (GOV-08, from prior session).

Items 1-14 are content authoring; items 15-17 are design decisions.

**Total content authoring:** ~1,138 entries (from current spec). Larger than the original 630-template estimate. Worth examining honestly.

### 4.3 The authoring count grew, not shrank

The original armature pivot (after the template library was rejected) claimed reduction from 630 templates to ~370 entries. By the time meta-armatures, Event Impact Matrix, anomaly tables, Knowledge seeding, Project authoring, NPC-NPC Opinion seeding, dialogue fragments, and Gossip templates are added, the total reaches ~1,138.

**This is honest:** the system does more than the original template library would have. Meta-armatures, Knowledge structures, NPC-NPC dynamics, Domain Action proposal mechanisms, and the political loop are all genuinely additional capability. The ~370-entry claim was premature optimization — it counted only the armature replacement, not the full architecture.

**This requires a recalibration:** Jordan should consider whether ~1,138 entries is a feasible authoring obligation given Valoria's broader content needs. If not, where to cut?

Candidates for cutting:
- **Knowledge seeding (~150 entries):** could be reduced if Knowledge is only authored for the most info-rich NPCs (~10 NPCs at 5-10 facts each = 50-100 entries).
- **NPC-NPC Opinion seeding (~200 entries):** could be reduced by authoring only inner-circle pairs (5 inner-circle × 7 factions × 5 pairs each = 175 entries) and letting other Opinions form dynamically.
- **Gossip text templates (~100 entries):** could start with 30 templates covering high-frequency event types and add over time.

If those reductions apply, total drops to ~700-800 entries. Still substantial; closer to feasible for a single content author over months.

### 4.4 Computational budget is unverified

Throughout the documents, computational claims are acknowledged as estimates without profiling. The honest position (stated in the iterative document) is that profiling must precede commitment to the full system. This holds.

What this means for the implementation path: the system should be implementable in stages, with profiling at each stage. Recommended stage order:
1. Per-NPC inner state + three-dimension armature + Event Impact Matrix → profile basic Concern generation under typical event load.
2. Add Procedure E (off-screen interactions, Gossip propagation) → profile NPC network interaction load.
3. Add Settlement and Faction Meta-Armatures → profile multi-scale event interpretation.
4. Add Domain Action proposal mechanism → profile inner-circle competition.
5. Add long-run mechanisms (Memory salience floors, calcification, Project legacy) → profile Year 15 game state.

Each stage produces a working but partial system that can be tested independently. This is risk mitigation: if Stage 2 reveals computational issues, Stages 3-5 can be redesigned before implementation.

---

## §5 Strengths Honestly Assessed

### 5.1 Concept clarity

The core concept — NPCs with inner states whose interpretations of events drive autonomous behavior — is readable in one sentence and produces predictable system behavior at the framework level (specific outcomes are designed-unpredictable per the goal). The system is not over-engineered relative to its design intent.

### 5.2 Integration with existing Valoria

The system reads from existing structures (Conviction, Belief, Scar, Disposition, Standing, Knot) and adds new derived structures. No existing system is modified. This is rare in a project this size; usually new subsystems require existing-system surgery. Here the integration is genuinely additive.

### 5.3 Bidirectional cascading is verified, not asserted

The 12 stress tests in 10 trace specific cascading patterns vertically, laterally, and diagonally. The Treaty That Broke the Court (8) and Settlement That Defected (8) scenarios show personal → faction → personal loops closing through traceable causal chains. This is the meta-architectural property the design was supposed to produce.

### 5.4 Self-correction mechanisms

The wrong-Belief calcification, Memory salience floors, completed-Project legacy, and faction anomaly detection are responses to issues found in stress testing. The system isn't presented as ideal — it's presented as iteratively patched against found failures. This is more honest than typical design proposals.

### 5.5 Cascade attenuation, not just cascade enablement

Many emergent-system designs enable cascading without preventing runaway. The ×0.7 per scale boundary is a specific damping mechanism. Without it, the system would be unstable in long-run play. Identifying and patching this in stress testing is significant.

---

## §6 Weaknesses Honestly Assessed

### 6.1 Content authoring obligation is large

~1,138 entries (or ~700-800 if cuts applied) is a substantial obligation for a single content author. Valoria's broader content needs (NPC backstories, Threadwork details, settlement specifications, region-specific lore) compete for the same authoring time. This is the system's largest practical risk: it works as designed only if the content is authored. Sparse content produces a thin system.

### 6.2 Validation depth is uneven

12 stress tests in 10 found 17 issues. This is good for finding specific bugs but does not verify the system holistically. Specifically:
- No simulation has been run. The system's behavior across thousands of simulated game states is unknown.
- Specific personality-Conviction combinations have not been hand-tested for realism (e.g., does a low-institutional-deference Faith-aligned NPC behave plausibly? It hasn't been checked).
- Edge cases in Knowledge propagation chains under saturated game state haven't been tested.
- Player-as-Standing-7-Regent-Designate interactions with Faction Meta-Armature haven't been specified clearly.

### 6.3 The vetting block is from before stress testing

Document 07 (vetting) was committed before 09 and 10 were drafted. Its assessment of the architecture is based on the pre-streamlined, pre-stress-tested version. The vetting outcomes (PASS, M-ratings, etc.) likely still hold for the current version, but this hasn't been re-verified. A re-vetting against the current spec would be appropriate before promotion from PROVISIONAL.

### 6.4 The iterative documents accumulated complexity that the streamlining only partially addressed

The journey from 01 (gap audit, 8 gaps) to 10 (stress tests with patches) traversed multiple architectural pivots: Disposition extensions → RP balances → autonomous actor reframing → ground-up mechanical proposal → iterative patches → streamlined → meta-armatures + Event Matrix → stress test patches. The current spec is good but its structure carries the marks of this journey. A cleaned-up integrated specification document (combining the streamlined architecture from 09 with the stress test patches from 10) would be ~25% the length of the cumulative documentation but considerably more readable as a reference.

### 6.5 Player experience claims are inferred, not playtested

The system promises a player experience (NPCs feel like persons, political environment feels emergent, intelligence operations feel meaningful, succession dynamics feel anticipatory). These are inferences from the mechanics, not verified by playtesting. Some mechanics that seem like they'll produce the intended experience may not in practice. Specifically:
- Will players notice gossip propagation at all, or will it feel like ambient noise?
- Will Witness Mode produce dramatic context or just information overload?
- Will NPC Outreach scenes feel character-driven or feel scripted?
- Will Domain Action proposals from inner-circle NPCs feel meaningful or feel like the faction running on rails?

These can only be tested with actual gameplay, which requires implementation, which requires profiling and content authoring first.

---

## §7 Critical Path Forward

### 7.1 Immediate (no decisions blocked)

1. **Update 00_session_index.md** to mark current spec (09 + 10) vs preserved-stage documents (01-08).
2. **Produce a clean integrated specification document** combining the streamlined architecture (09) with stress test patches (10). Single source of truth, ~25% length of cumulative documentation.

### 7.2 Decision-blocked (Jordan input required)

3. **Wrong-Belief Investigation interaction:** Option A vs Option B (recommendation: B per Ω-d).
4. **Authoring scope decision:** ~1,138 vs ~700-800 entries vs lighter still. Determines what gets authored vs what's left to dynamic generation.
5. **Carryover decisions** (Intelligence as 6th faction stat, LICENSE/GOV-08).

### 7.3 Pre-implementation

6. **Re-vetting** against current spec (the Class A vetting in 07 is from pre-streamlined version).
7. **Promotion from PROVISIONAL** to active design — requires editorial ledger entries (ED-XXX) for each major component, patch register entries (PP-XXX) with vetting blocks, integration patches against `designs/npcs/npc_behavior_v30.md`, `designs/architecture/player_agency_v30.md`, `designs/territory/settlement_layer_v30.md`.
8. **Simulation pass** before any code is written. Simulate ~10 game-years across 3-5 player archetypes. Use the simulation to validate computational budget assumptions.

### 7.4 Implementation (after pre-implementation gates)

9. Stage-gated implementation per §4.4 (5 stages, profiling at each).
10. Content authoring on the agreed scope, parallel to implementation stages.
11. Playtesting of partial system at Stage 3 completion (basic political dynamics functional).

---

## §8 Final Assessment

The political dynamics system is a mature design proposal at the boundary between architectural specification and implementation-ready specification. It has:

- A coherent core concept (armature-driven autonomous NPC interpretation)
- Mechanisms specified to the level required for engine implementation (data structures, procedures, ordering)
- Multi-scale integration (NPC, settlement, faction)
- Cascade discipline (attenuation, faction crisis, anomaly detection)
- Long-run viability mechanisms (Memory salience floors, calcification, Project legacy)
- Stress-test-validated patches for found failures

It does not have:

- Implementation (no code)
- Profiling (computational claims unverified)
- Simulation validation (system behavior across many game states unverified)
- Playtest validation (player experience unverified)
- Unified clean specification (current spec is distributed across 10 documents)
- Re-vetting against the post-stress-test version
- Resolution of accumulated Jordan decisions
- Content authoring (the ~1,138 entries remain to be written)

These are appropriate gaps for a design proposal at this stage. They are not bugs in the design; they are the next phases of the project. The design is ready to move from session-iterative work to formal review and pre-implementation planning.

The most important single piece of work remaining before any implementation begins is **the clean integrated specification document** that consolidates the current state into a single coherent reference. Without it, integration patches against existing documents will be error-prone (designers will reference 06 or 08 not knowing they're superseded) and content authoring will fragment.

The session as committed is a substantive contribution to Valoria's political architecture. Its primary value is not in any single document but in the iterative deepening across the 10 documents — gap audit → historical research → directionality revision → philosophical reframe → mechanical specification → iterative patches → vetting → architectural completion → streamlining → stress testing. The journey itself encodes design knowledge that should be preserved even as the current spec is consolidated.
