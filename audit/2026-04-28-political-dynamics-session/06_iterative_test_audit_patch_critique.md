<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: Iterative Test-Audit-Patch-Critique (3 Iterations) -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# NPC Autonomous Actor System: Iterative Test-Audit-Patch-Critique

The previous document produced a proposal with 9 edits applied. This document treats that edited proposal as the test object, then audits it honestly, patches, critiques the patches, and repeats. The goal is a system that is mechanically specific, computationally honest, and actually produces the player experience claimed.

---

## Iteration 1

### Test Phase 1

**Probe 1.1: How does Concern resolution actually work?**

The proposal says: "When salience reaches 0, the Concern resolves with whatever information the NPC has accumulated. The resolution may be wrong."

This is not a mechanism. The engine needs to:
1. Know what evidence is relevant to the Concern
2. Weigh that evidence
3. Produce a specific Belief update or Opinion shift

If the Confessor's Concern "Why did Almud agree to the treaty?" encounters three observations — player seen with Vaynard twice, Klapp expressing satisfaction, Almud distracted in council — how does the engine synthesize these into a conclusion? "Whatever information the NPC has accumulated" describes desired behavior without specifying implementation.

**Probe 1.2: The Opinion story field is not computable.**

Opinions store a "story" field as human-readable text. Text is not algorithmically usable by an engine. The structural question: does the story field drive behavior, or is it flavor?

If only affect_axis (−3 to +3) drives Opinion-based behavior, then the elaborate Opinion structure collapses to a scalar with attached prose. The prose matters for dialogue rendering but not for mechanical output. The proposal conflates presentation with computation.

**Probe 1.3: The 30% ambient contact rate is too low, but the right rate may break the system.**

35 Active NPCs in shared inner circles produces ~105 unique co-faction pairs. At 30%/season = ~31.5 ambient interactions. But court members who work together daily should interact far more frequently. 90% would give ~95 ambient interactions. Either rate is defensible, but neither is derived from anything. More importantly: ambient contacts produce affect drift. At 90% × small drift per interaction, after 30 seasons (~the campaign length), every NPC-NPC pair converges toward their structural equilibrium — which may be indistinguishable from "not having done any of this work."

The proposal adds ambient contact to solve the visible-politics problem but doesn't address whether the accumulated drift produces dynamic outcomes or just convergence.

**Probe 1.4: Settlement Signal aggregation is unspecified.**

"Each settlement aggregates its Passive NPCs' Memories into a Settlement Signal." Three NPCs with three different Concerns of different salience values — how is the Signal computed? Mean affect? Dominant Concern? Majority sentiment? Without an aggregation algorithm, Settlement Signal is a named concept without implementation.

**Probe 1.5: Computational budget is fabricated.**

The "~10ms per procedure" estimate has no derivation. Procedure B (Concern generation) involves: event lookup → template matching against library → Conviction filter → salience assignment → text instantiation. Depending on template library size, this could be 2ms or 200ms per NPC. The proposal presents confident estimates for work it cannot know the cost of yet.

**Probe 1.6: Procedures are not independent — deeper than ordering alone.**

Edit G specified an ordering (A→C→B→D→E) to resolve procedure dependencies. But Conviction Scar events (large, immediate Opinion shifts) may require within-season D→E feedback that the ordering doesn't support. If Klapp acquires a Scar during C (Project completion triggers an event), B runs and resolves some Concerns, D then drifts Opinions — but the NPCs whose Opinions just shifted based on this season's events won't select each other for Procedure E interactions until next season. One large event's social consequences are delayed a full season.

For low-salience events this is fine. For politically significant events (Scar acquisition, leader death, betrayal), one-season delay is too slow.

**Probe 1.7: Wrong Beliefs have no self-correction path.**

The Confessor concludes the player is whispering heresy to the king. This is wrong. Mechanically: a wrong Belief persists until a social Contest addresses it. Contests require player engagement. If the player doesn't know the Confessor holds this Belief, they can't engage with it. If the Confessor's Belief generates Heresy Investigation actions without the player realizing why, the consequences are opaque.

No mechanism exists for NPC self-correction of wrong Beliefs. Nor does any mechanism notify the player that a key NPC has formed a significant false Belief about them.

**Probe 1.8: "Observable behavior" has no implementation path.**

The proposal says NPCs advancing their Projects produce "visible actions" the player observes. But:
- Point of observation: where does the player see Ehrenwall and Torben training? When passing through what space?
- Triggering condition: is it always visible, or requires investigation?
- Content: what specifically appears? Pre-authored scene? Procedural description?
- Read action coverage: the current Read action reveals "Disposition, one Belief, emotional state." Project advancement is not in scope. The proposal doesn't specify when Project-related information is surfaced by which player action.

"What the player observes" is the entire player experience of this system. The proposal specifies it least of all.

---

### Audit 1

Issues from probes, ranked by severity:

| # | Issue | Severity | Type |
|---|---|---|---|
| A | Concern resolution has no mechanism (Probe 1.1) | Critical | Missing implementation |
| B | Opinion story field is presentation, not computation — affect_axis is the only driver (Probe 1.2) | High | False claim in proposal |
| C | Ambient contact rate is undetermined; convergence behavior unknown (Probe 1.3) | High | Missing calibration |
| D | Settlement Signal aggregation unspecified (Probe 1.4) | High | Missing implementation |
| E | Computational budget is fabricated (Probe 1.5) | Medium | Overconfident claim |
| F | Large events (Scars, deaths) need within-season Opinion propagation, not next-season (Probe 1.6) | Medium | Ordering gap |
| G | Wrong Beliefs have no self-correction path and no player notification (Probe 1.7) | High | Missing mechanism |
| H | Observable behavior has no implementation path (Probe 1.8) | Critical | Missing implementation |

---

### Patch 1

**Patch A — Concern resolution: Template + Weighted Evidence**

Replace "resolves with whatever information the NPC has accumulated" with a specific mechanism:

Each Concern has a `seeking` tag (set at Concern creation). When Concern resolves, the engine looks in the NPC's Memories for any Memory whose `event_type` tags match the seeking tag. If ≥1 match: resolution uses the matching Memory with highest salience as the basis. If zero matches: resolution defaults to the NPC's prior Belief about the Concern's domain (i.e., they explain the event in terms of what they already believed).

Crucially: the seeking tag is set by the *NPC's Conviction*, not by objective relevance. A Faith-aligned NPC whose Concern is "Why did Almud agree to the treaty?" has seeking tag: `[counsel-corruption, heresy-influence, faithlessness]`. A Reason-aligned NPC has seeking tag: `[strategic-interest, military-necessity, diplomatic-pressure]`. Same event, different resolution paths.

This produces wrong conclusions without any special "make it wrong" flag — it's wrong because the NPC's Conviction structures what they look for. The Confessor doesn't find a Memory about diplomatic pressure, so the resolution falls back to his prior Belief about what corrupts kings: faithless counsel.

**Implementation:** Concern template library (authored, ~200 templates, organized by event type × Conviction) maps each combination to a seeking tag set. This is a data authorship task, not engine work.

**Patch B — Opinion structure: two-layer clarification**

The Opinion structure has two layers that must be explicit:

- **Computation layer:** `affect_axis` (−3 to +3) is the only value the engine uses for behavioral decisions (who to approach, whether to obstruct, who to vouch for). This is derivable from a weighted average of the Opinion's referenced Memories' affect values.

- **Presentation layer:** `story` (prose) and `affect` (text descriptor) are generated for dialogue and player-facing Read results. They are derived from the affect_axis value and the NPC's Conviction + Personality + the content of Evidence Memories. They are rendered, not stored, except as a cache for performance.

Correction to the proposal: the Opinion's computational content is `{subject, affect_axis, confidence, evidence_memory_refs}`. The story and text descriptor are rendered at display time from these inputs + the NPC's Identity. This is simpler to implement and honest about what the engine actually computes.

**Patch C — Ambient contact rate: derived from functional need**

Rather than picking a percentage, derive the rate from what the system needs to accomplish:

**Minimum needed:** an NPC pair that starts at affect_axis 0 (Indifferent) and has structural Conviction alignment (same primary) should converge to affect_axis +1 (mildly positive) within approximately 6 seasons of co-service.

**Implication:** 6 interactions producing small positive drift → each interaction produces +1/6 ≈ +0.17 affect_axis. At 30% per season, expected 0.3 interactions per season → 6 seasons to reach 1.8 interactions → not enough. Need higher rate.

At 60% per season, expected 0.6 interactions per season → 6 seasons = 3.6 interactions × 0.17 = 0.6 drift → still not reaching +1 target from neutral.

**Resolution:** Drift per interaction must scale with alignment. Shared primary Conviction → +0.3 per contact. Different Conviction → +0.05. Same faction, no shared Conviction → +0.1. Using 60% rate and these drift values:
- Shared Conviction pair: 6 seasons × 0.6 contacts × 0.3 drift = +1.08 → converges to mildly positive ✓
- No shared Conviction: 6 seasons × 0.6 × 0.05 = +0.18 → barely moves ✓
- Court contact without shared Conviction shouldn't produce strong relationships

This gives 60% ambient rate with scaled drift, derived from the behavioral requirement. Correct estimate: 105 pairs × 60% = 63 ambient interactions/season.

**Patch D — Settlement Signal: dominant Concern algorithm**

Settlement Signal aggregation algorithm:

1. Collect all Passive NPC Memories from this settlement, created in the last 2 seasons.
2. Weight each by salience × NPC affect value.
3. Group by `event_type` tag.
4. Dominant event_type (highest weighted sum) becomes the Signal's primary tag.
5. Net affect of all Memories = Signal's affect_axis (could be positive, negative, or mixed).
6. If affect_axis > +1: "settlement is stable, notable positive dynamic [primary tag]."
7. If affect_axis between −1 and +1: "settlement is neutral, notable concern [primary tag]."
8. If affect_axis < −1: "settlement is troubled, primary issue [primary tag]."

Signal propagates to the settlement's controlling faction's relevant Active NPC as a Concern with salience = |affect_axis| × 2 (round to nearest integer, min 1). The Concern text is generated from the Signal: "Reports from [settlement] indicate [affect description] centered on [primary tag]."

This is specific, implementable, and computationally cheap.

**Patch E — Computational budget: honest uncertainty**

Remove specific ms estimates from the proposal. Replace with:

"Computational cost per Accounting has not been profiled and cannot be estimated without implementation. Design decisions that affect cost: (1) Concern template library size — library lookup is O(n) on library size per Concern per NPC; (2) Opinion affect_axis computation — O(m) on Memory count per NPC pair; (3) ambient interaction selection — O(n²) on inner-circle NPC count. Recommend implementing Procedure A and B first and profiling before committing to the full procedure set. Introduce per-season computation budget caps: if procedures exceed budget, lower-priority procedures (Procedure E ambient contact, Distant Contact) are skipped for that season."

**Patch F — Large event propagation: Immediate Update flag**

Add an `immediate_update: bool` field to events. Events flagged immediate_update trigger a one-time out-of-sequence Procedure D and E run for the directly-affected NPCs only, within the same Accounting rather than next season. 

Immediate-update events: Conviction Scar acquisition, leader death or deposition, betrayal event (public breach per ED-664), formation or dissolution of a Knot with the player.

This keeps the normal ordering (A→C→B→D→E) for routine events while allowing significant events to propagate within-season without disrupting the ordering for everything else.

**Patch G — Wrong Belief self-correction and player notification**

Two separate mechanisms needed:

*Self-correction:* An NPC holding a wrong Belief will encounter contradicting events over time. When a new Memory contradicts a held Belief, Procedure B generates a Concern: "Was I wrong about [Belief domain]?" The Concern's seeking tag is set to `[contradiction-evidence]`. If over the Concern's ttl (default 4 seasons) the NPC accumulates two or more contradicting Memories with salience ≥ 2, the Belief is flagged for revision. No social Contest required. At the next Accounting after flagging, the Belief becomes a Scar and a revised Belief forms incorporating the contradiction.

This is slower than player-mediated Belief revision (which can happen in one scene) but provides self-correction over 4–8 seasons.

*Player notification:* The player has no direct notification of NPC Beliefs they haven't discovered. This is by design — the political game is about incomplete information. However, two indirect channels exist:

1. Read action result (existing): "detect one Belief." If the player uses Read on an NPC in an unusual context, they may surface the wrong Belief.
2. Behavior signals: an NPC acting on a wrong Belief produces behavior that doesn't match their prior pattern. Observant players notice the inconsistency and investigate. This is the correct mechanism — the player's job is to notice when something is off.

No direct notification. The opacity is the game.

**Patch H — Observable behavior: explicit implementation path**

Project advancement visible actions are surfaced through three mechanisms only:

1. **Ambient scene encounters:** When the player is in the same settlement as an NPC advancing a Project, there is a base 25% chance per player scene action in that settlement of encountering the visible_action in passing (not a full scene — a brief description, an overheard exchange, an observed meeting). The encounter requires no scene action cost. It produces one piece of information: the NPC is doing X.

2. **Read action depth expansion:** Read action at Disposition +2 or higher (Friendly) now surfaces "one active behavior" in addition to emotional state. "Active behavior" is the visible_action label from the NPC's current Project, expressed as one concrete observation. At Disposition +3+, Read surfaces "one active concern" (the Concern seeking tag, expressed as a question the NPC seems to be pursuing).

3. **Investigation:** Surveil action from fieldwork §4.2 applied to a specific NPC reveals their Project's visible_action plus any Project-related Memories visible at current Depth. This costs a scene action and produces more detail than the ambient encounter.

No other path. Pre-authored scenes for Project advancement are not produced unless the Project completes (completion_effects may trigger Scene Slate entries at Priority 2).

---

### Critique of Patch 1

**Patch A creates a massive content authorship dependency.**

The Concern resolution mechanism now requires a template library: ~200 templates organized by event type × Conviction (7 Convictions × ~30 significant event types = 210 combinations). Each template must specify a seeking tag set. This is feasible but represents significant upfront authoring work that will be incomplete at first implementation and will need continuous updating as new event types are added to the game.

The mechanism is correct but the dependency needs to be explicit: the quality of Concern resolution — and therefore the quality of wrong-conclusion generation — is directly proportional to template library coverage. Sparse templates produce generic conclusions. Rich templates produce specific, legible NPC reasoning. The proposal should commit to minimum template counts per Conviction per event category before implementation begins.

**Patch B collapses the Opinion structure in a way that's honest but limits what players can learn from NPCs.**

If the story field is rendered at display time rather than stored, then the player's Read result ("Appraise reveals one Opinion with story content") is generating that story dynamically from affect_axis + Conviction + Personality + Evidence Memories. The generated story may be coherent, but it won't have the specific texture of authored prose — it'll be a templated description that may feel mechanical.

Two options: (a) accept that Read results have this generated feel, or (b) author short Opinion texts for the most politically significant NPC-NPC and NPC-player pairs at game start, with dynamic generation only for pairs that don't have authored content. Option (b) creates an authoring two-tier but produces better player-facing content for the most important relationships.

**Patch C's derived rate (60%) may still produce convergence problems.**

If 60% × 0.3 drift per interaction for shared-Conviction pairs, after 30 seasons (full campaign):
- 30 × 0.6 contacts × 0.3 = 5.4 drift → capped at +3 long before campaign end.

The system would have nearly every shared-Conviction court pair at maximum Collegial by midcampaign. This eliminates the political variation that makes lateral NPC-NPC dynamics interesting. Maximum Collegial means maximum cooperation — courts full of Collegial NPCs are politically inert.

This needs a dampening mechanism: ambient contact drift tapers off as affect_axis approaches extremes. Rate formula: `drift_per_contact = base_drift × (1 - |affect_axis| / 3)`. At affect_axis = 0, full drift. At affect_axis = +2, drift is 1/3 of base. At affect_axis = +3 (cap), drift is zero. This prevents runaway convergence while preserving the value of positive relationship investment.

But dampening also means: negative relationships don't auto-escalate to full Rivalrous from ambient contact alone. Rivalry requires specific high-salience events (position competition, public insult, Conviction clash in a significant decision). Ambient contact between structurally opposed NPCs produces slow convergence to mild negative, not escalating hostility. Escalation needs specific events.

This is more realistic and resolves the convergence problem. Add to Patch C.

**Patch F's immediate_update flag creates ordering inconsistency.**

When a large event flags immediate_update, Procedure D and E run out-of-sequence for affected NPCs. But Procedure D (Opinion drift) uses Memories to compute affect_axis updates. Procedure E (interactions) uses affect_axis to select interaction partners. If D runs immediately on event, it uses Memories that were just created by the event — fine. But E uses the just-updated affect_axis to select interactions, and those interactions create new Memories, which would normally feed into the next D cycle. But we've just run D early.

Within-season: event → immediate D (uses new Memory) → immediate E (uses updated affect_axis, creates new Memories) → does D run again at end-of-season Accounting? If yes: the new Memories from immediate E affect D a second time this season. If no: those Memories wait until next season.

Decision: immediate D and E run for *emotional propagation only* — they compute Mood updates (Procedure A extension) and update affect_axis for the directly-affected NPCs. They do not select interaction partners or create new Memories. Full Procedure D and E remain at Accounting's normal sequence. The immediate run is a mood-and-opinion-shock propagation tool, not a full cycle.

**Patch G's self-correction timeline (4-8 seasons) may be too slow for politically consequential wrong Beliefs.**

If the Confessor incorrectly believes the player is whispering heresy to the king, a Heresy Investigation fires within 1-2 seasons. The investigation produces real consequences (exposure, Mandate effects, faction relationships) before the 4-8 season self-correction window closes. By the time the Confessor might revise his wrong Belief, the investigation has already run and produced damage.

This is either a bug (wrong Beliefs shouldn't produce irreversible consequences before self-correction) or a feature (wrong Beliefs are politically dangerous and the player must manage the consequences even of things that aren't their fault). The decision is a design question, not a mechanics question.

Recommendation: flag this as a design decision required from Jordan, not a mechanic to resolve. The proposal should present both options with consequences:
- Option A (bug frame): Self-correction accelerates when the targeted NPC (player) provides contradicting evidence. Investigations from wrong Beliefs are paused pending evidence submission, Ob 2. This is forgiving.
- Option B (feature frame): Wrong Beliefs fire their consequences at normal speed. The player must manage the fallout of the Confessor's incorrect conclusion even while it's wrong. This is harsh but politically realistic — real defamation causes damage before truth emerges.

**Patch H's observable behavior mechanism is thin at Disposition < +2.**

The three surfacing paths (ambient encounter at 25%, Read at +2, Investigation) mean that for NPCs the player hasn't built relationships with (Disposition 0 or −1), Projects are nearly invisible. The player might observe an NPC at 25% chance during a scene, but without Read access, they learn only the visible_action label, not the Project's purpose or progress.

This is realistic (you notice what the spy is doing but not why) but may frustrate players who want to understand the political environment before investing in relationships. Counter-consideration: the frustration is exactly correct — relationships are prerequisites for political intelligence, not just mechanics to advance.

However, there's a gap between ambient encounter (you see Ehrenwall with Torben, you know she's training him) and full Read access (you know she's worried about who Torben will trust as advisor). The gap is too wide: the ambient encounter tells the player *what* is happening but nothing about *why* or *what it means*. Without some accessible layer for interpreting observable behavior, players may see activities they can't contextualize.

**Required additional surfacing path:** Gossip (from Patch D in the previous document) should surface Project-relevant information. When NPCs with high Disposition with the player gossip about each other's activities, the gossip includes context: "Ehrenwall has been spending a lot of time with the Prince. Some say she's grooming him for command, others say she's trying to steer his political circle away from Hafenmark influence." This gives interpretive content without requiring Disposition +2 with Ehrenwall directly.

---

## Iteration 2

### Revised Proposal State

The proposal now has the following confirmed elements:
- Tier stratification (Active/Passive/Population) ✓
- Data structures: Identity, State, Concerns, Projects, Opinions (two-layer: compute/present), Memories, Knowledge ✓
- Concern resolution via Conviction-weighted template library (Concern seeking tags) ✓
- Ambient contact at 60% with dampened drift (1 - |affect_axis|/3 scaling) ✓
- Settlement Signal via dominant Concern algorithm ✓
- Immediate-update for large events (Mood+Opinion shock propagation only, no new Memories) ✓
- Wrong Belief self-correction (4-8 seasons) + design-decision flag on Investigation interaction ✓
- Observable behavior via ambient encounters + Read expansion + Investigation + Gossip ✓
- Procedure ordering: A→C→B→D→E, with immediate-update supplement for large events ✓

**Outstanding content authorship commitments:**
- Template library minimum: 210 Concern templates (7 Convictions × 30 event types)
- Project library: 1+ per Active NPC (35+ starting Projects)
- Opinion seeding: significant pairs authored, dynamic for others
- Knowledge seeding: per information-rich NPC

### Test Phase 2

**Probe 2.1: Integration with existing Conviction Scar system**

The existing system (npc_behavior_v30) triggers Belief revision via social Contest: "Total Victory Contest defeat via Resonant Style." The new system adds Procedure B self-correction (contradicting Memories over 4 seasons). These are two separate Belief revision paths.

What happens when both fire simultaneously? Player wins Total Victory Contest against Klapp in Season 5. Klapp acquires a Scar via existing system. In the same season, Klapp has also accumulated contradicting Memories that would trigger self-correction via Procedure B. Procedure B was about to resolve a different Concern toward a Belief revision.

Two Belief revisions in one season: is that valid? The existing system says Scars accumulate; more Scars push NPCs toward arc transitions. If both paths fire simultaneously, Klapp could acquire 2 Scars in one season and jump directly to arc state B criteria.

**Issue 2.1:** Two Belief revision paths must be explicitly gated from firing on the same Belief in the same season. Rule: if a Belief is revised via social Contest, Procedure B self-correction on that Belief resets (the Contest outcome supersedes the accumulated contradicting evidence).

**Probe 2.2: The Knot system and Opinion/Concern interactions**

Knots (fieldwork §5.6) give +1D on social actions and shared Composure buffer. The new system adds: Knot partners' Projects are immediately visible to each other (their ambient encounters are guaranteed, not 25% chance). Knot partners' Concerns in each other's domain are shared via Knot counsel.

But the proposal doesn't specify this. If it doesn't, Knots remain exactly what they were — mechanical bonuses — and the new system doesn't make Knots more politically meaningful.

**Issue 2.2:** Knot partners should have guaranteed access to each other's Observable behavior (not 25% ambient — automatic). Knot partners should each have one Concern per season about their partner available without needing a Read action (they're paying attention to each other). This makes Knots politically valuable in the new system, not just combat/social combat bonuses.

**Probe 2.3: NPC Projects and Domain Actions — resource conflict**

NPCs have seasonal scene action budgets (Priority tree determines what actions they take). Projects consume discretionary action capacity. But the proposal says Project advancement happens when "the priority tree has discretionary capacity." What counts as discretionary?

If Crown Mandate falls to 2 (triggering Institutional Filter as Priority 1 per npc_behavior §4.1), every Crown NPC's priority tree is occupied with Stability actions. No discretionary capacity. No Project advancement for any Crown NPC this season. Every single Crown NPC's personal Project is frozen.

This produces a realistic scarcity effect (crises interrupt personal agendas) but also means Projects stall together across an entire faction simultaneously, which is too clean. Individual NPCs have different thresholds for when they subordinate personal Projects to institutional demands.

**Issue 2.3:** Project advancement should check the individual NPC's institutional_deference personality value (−2 to +2). High institutional_deference: Project pauses at any Institutional Filter activation. Low institutional_deference: Project continues even at Priority 1 filter, at +1 Ob (they're neglecting institutional duty). This differentiates NPC responses to crises and makes institutional_deference personality a meaningful political characteristic.

**Probe 2.4: Knowledge propagation — who learns what when**

The Knowledge structure enables NPCs to possess specific information (Father Eyvind knows a Hafenmark spy is operating in Niedmark). But how does Eyvind's Knowledge spread to other NPCs?

The proposal says Knowledge is shared based on Disposition gates. But that's player-facing sharing. What about NPC-NPC Knowledge sharing? In the off-screen interaction (Procedure E), do NPCs share Knowledge with each other?

Current answer: unspecified. Knowledge propagation between NPCs is entirely absent.

**Issue 2.4:** Off-screen interactions should have a Knowledge-sharing component. When two NPCs interact (ambient or triggered), if either has Knowledge with salience ≥ 3 and the other NPC's Concerns include a seeking tag that matches the Knowledge fact, the Knowledge is shared. The receiving NPC creates a Memory of learning it. This enables information to flow through the NPC network without player involvement — which is realistic (gossip networks function without the player) and creates situations where the player learns from an NPC something that another NPC told them off-screen.

**Probe 2.5: Mood persistence across large time gaps**

Mood states have durations: "Grieving (2-4 seasons)." But what happens when the player is absent for 4 seasons on an expedition? The Mood simply expires and NPCs return to Steady during the player's absence. On return, the world has moved on emotionally.

This seems correct. But it creates a specific gameplay effect: if the player deliberately delays engaging with a grieving NPC (waits 3 seasons), the NPC's Grief expires. Approaching them after Grief expires gets a different response than approaching them during Grief. The player can strategically time engagement.

Is this a problem? No — strategic timing of social engagement is realistic. But the proposal should acknowledge it explicitly so it can be designed for, not accidentally exploited. 

**Issue 2.5:** Not a bug, a feature. Flag as explicit player strategy: "The timing of social engagement is itself a political tool. A player who waits for an NPC's humiliation to expire before approaching them prevents the conversation from being colored by the Mood state. A player who engages during Grieving may access Vulnerability information not available in other Mood states." Document this as intended behavior in the proposal.

**Probe 2.6: The Read action now surfaces too much**

The original Read action: "Determine NPC's current Disposition, one Belief, emotional state."

Patch H expanded it: "Read at Disposition +2 surfaces one active behavior. Read at Disposition +3 surfaces one active concern."

But Patch G said wrong Beliefs produce no direct player notification — opacity is the game. Concern surfacing via Read creates a near-direct channel: the player can Read every high-Disposition NPC each season and know their active Concerns. After one season of relationship investment, the player has explicit access to the inner political life of their entire network.

This undermines the opacity that makes the system interesting. If Read directly surfaces Concerns at Disposition +3, the player doesn't need to observe behavior and infer intentions — they just Read and learn.

**Issue 2.6 (critical):** Read action expansion goes too far. Revised scope:
- Read at any Disposition: Mood state (existing)
- Read at +2: "active behavior" — one Observable behavior label only (what the NPC is doing, not why)
- Read at +3+: no additional structured information. Instead, at high Disposition, the NPC's dialogue in Outreach scenes becomes more candid — they volunteer partial Concern information naturally, not as a Read output. The opacity is preserved; high Disposition makes the NPC *want* to share, not gives the player a direct data access channel.

**Probe 2.7: The proposal has no failure state for Projects**

Projects have `completion_effect` and `failure_effect` fields. But the proposal doesn't specify what causes Project failure. Progress can stall (institutional_deference personality, crisis suppression), but does stalling become failure? When?

If Projects never fail (they just stall until circumstances clear), the system loses tension. NPCs pursue Projects indefinitely, generating ambient interactions and Concerns, without resolution pressure. If Projects do fail, what triggers failure and what are the consequences?

**Issue 2.7:** Project failure condition: if a Project stalls for 8+ consecutive seasons (progress unchanged), it fails. The NPC generates a significant Memory ("I gave up on X") with affect negative, a Belief update about the domain in which they failed, and Mood → Humiliated or Grieving depending on how central the Project was to their identity (measure: if Project sought outcome aligned with primary Conviction, Grieving; if secondary, Humiliated). The failed Project slot opens for a new Project, which the NPC generates at next Accounting based on current Concerns and available opportunities.

---

### Audit 2

| # | Issue | Severity |
|---|---|---|
| 2.1 | Two Belief revision paths can fire simultaneously | High |
| 2.2 | Knots not integrated with new system | Medium |
| 2.3 | Project suppression too uniform across faction during crises | Medium |
| 2.4 | Knowledge propagation between NPCs unspecified | High |
| 2.5 | Strategic Mood timing — feature, not bug, needs documentation | Low |
| 2.6 | Read action expansion breaks opacity that makes system valuable | Critical |
| 2.7 | Project failure condition unspecified | Medium |

---

### Patch 2

**Patch 2.1 — Belief revision gating:**
If a Belief is revised via social Contest this season, Procedure B self-correction for that Belief resets all accumulated contradicting Memory weight to 0. The Contest result is authoritative for that season. Self-correction can resume next season if new contradicting evidence arrives.

**Patch 2.2 — Knot integration:**
Knot partners have guaranteed access to each other's Observable behavior (ambient encounter probability becomes 100% in shared settlements). Each season, Knot partners each receive one Concern about their partner surfaced automatically, without requiring Read action. This requires the engine to check the Knot registry against the Concern list and flag one Concern per Knot partner as "shared awareness." The Concern is surfaced as dialogue in the next interaction with the partner.

**Patch 2.3 — Institutional deference and Project suppression:**
Project advancement check: if faction Institutional Filter is at Priority 1 (crisis), NPC's Project pauses only if institutional_deference ≥ +1. If institutional_deference = 0: Project pauses. If institutional_deference ≤ −1: Project continues but at +1 Ob for all Project-advancement actions (they're cutting corners on their duties). Generates risk: if an NPC at institutional_deference −2 pursues their Project during a faction crisis and the faction leader's Concern system detects the neglect (40% chance of detection per season), the NPC acquires a negative Memory with the faction leader (Disposition risk).

**Patch 2.4 — NPC-NPC Knowledge propagation:**
In Procedure E (off-screen interactions), add a Knowledge-sharing check: if either NPC has Knowledge with salience ≥ 3 and the other NPC has an active Concern whose seeking tag matches the Knowledge fact, the Knowledge transfers. Recipient creates a Memory: "[Source NPC] told me that [Knowledge fact]." The Memory has salience = shared Knowledge salience − 1 (propagated information is slightly less salient than direct experience). Propagation is limited to one degree per season — Knowledge doesn't cascade through the network in one Accounting.

**Patch 2.6 — Read action scope correction:**
Revert Read expansion. Read at Disposition +2: one Observable behavior label only. Read at +3+: no additional structured output. The mechanism for accessing NPC inner state at high Disposition is Outreach candor (NPCs volunteer partial Concern information in dialogue) and Knot awareness (Patch 2.2), not direct data access through Read.

Read is an observation tool, not an interrogation tool. At maximum Disposition, the player knows what the NPC is doing (Observable behavior) and receives unprompted conversation that may reveal their Concerns. This is indirect and realistic.

**Patch 2.7 — Project failure:**
Project stalled for 8+ consecutive seasons → failure. Memory created: negative affect, strength proportional to how aligned the Project was with primary Conviction (fully aligned: affect −3, partial: affect −2, tangential: affect −1). Mood update: Grieving (primary Conviction aligned) or Humiliated (secondary). Failed Project slot opens; new Project generated at next Accounting based on highest-salience current Concern.

---

### Critique of Patch 2

**Patch 2.2 (Knot integration) implies significant content authorship for Concern surfacing.**

"Each season, Knot partners receive one Concern about their partner surfaced automatically." The engine selects which Concern to surface. The surfacing is expressed as dialogue. This dialogue needs authorship: what does an NPC say to reveal that their partner is worried about "counsel-corruption" versus "strategic-interest-conflict"? The same Concern expressed from different NPCs' Mouths requires different dialogue, and each Concern's possible surfaced-dialogue options must be authored.

Rough count: if there are 3 Knot pairs at any time in a campaign (Bonds 5 player with 3 NPCs), and each can hold ~5 different Concerns at any time, we need ~15 Concern-surfacing dialogue variants, times 2 Convictions per NPC = ~30 authored dialogue fragments. That's manageable but not trivial.

**Patch 2.4 (Knowledge propagation) has network latency that may feel arbitrary.**

One-degree propagation per season means: Father Eyvind tells Petra in S5 → Petra's Memory created → Petra can tell the player in S6 if player has Disposition +2 with Petra. Two hops. But what if Petra never talks to the player? The information propagates to Petra and stops. The player misses faction-relevant intelligence because a specific NPC they happen to not know is the bottleneck.

This is realistic (intelligence networks have bottlenecks) but frustrating if the player doesn't know the bottleneck exists. Mitigation: the Gossip system (Patch D, Iteration 1) provides an alternative path — gossip doesn't require direct NPCc to player Knowledge transfer, it generates Scene Slate entries that the player can pursue. Knowledge propagation + Gossip together should ensure most significant Knowledge eventually becomes accessible.

But: what if Knowledge is *suppressed*? A politically inconvenient Knowledge fact (e.g., a faction leader knows about a corruption scandal) — does the faction leader suppress Knowledge propagation? The proposal has no suppression mechanism. Suppression would be a significant political mechanic (rulers who can control information flow gain structural advantage) but it's absent.

Flag as a future addition: Knowledge suppression (faction leader can mark a Knowledge fact as "suppressed" — NPCs who receive it via propagation generate a Memory that includes "this is not to be discussed," which reduces their Disposition-sharing sensitivity for that specific fact by +2). Not in scope for this iteration.

**Patch 2.6 creates an internal contradiction with the autonomous actor philosophy.**

Reverting Read at Disposition +3 to reveal no additional structured information means: a player with maximum relationship investment (Disposition +5, potentially Knot-linked) accesses the same Read output as a player with Disposition +2. The information differential between moderate and deep relationship is now: better Outreach candor (dialogue) + Knot Concern sharing (Patch 2.2).

Is this sufficient differentiation? The player who invests 8 seasons building Disposition +5 with an NPC should have meaningfully better intelligence access than someone at +2. The proposed mechanisms (candor, Knot sharing) are real but may feel insufficient given the investment required.

Consider: at Disposition +4, the Read action could reveal the *direction* of the NPC's current primary Concern without specifying its content. "The Marshal's attention is focused outward — she's watching for something beyond the court." This tells the player the Concern domain (external/political/succession/etc.) without naming the Concern. The player must interpret this contextual signal.

This adds one information layer between Disposition +2 (behavioral label) and Disposition +5 (direct Concern through Knot) without breaking opacity. Add to revised specification.

---

## Iteration 3

### Test Phase 3 — Integration Stress Test

**Probe 3.1: Does the system produce different behavior for the same NPC across two runs with different player choices?**

This is the fundamental test of whether the system escapes pattern-matching.

Run A: Player spends Years 1-3 with the Crown, building deep relationships with Almud and Ehrenwall. Ignores Klapp and the Confessor. Agrees to every treaty Almud proposes.

Run B: Player spends Years 1-3 as an independent, building cross-faction contacts with Klapp (Crown), Vaynard (Varfell), and Vossen (RM). Challenges multiple treaties via Hafenmark's parliamentary channels.

**Run A, Year 4:** Klapp has been advancing his Stillhelm Codex Project with no player interaction. His Concerns have generated from faculty events (treaty context shifts, Confessor aging). His Opinion of the player is "present in the court, aligned with Almud, not specifically interested in scholarship." He has found no ally for his Project within his reach. His Concern "Who could support the confrontation with Himlensendt?" has forced-resolved (salience to 0) with no answer — he concludes he must act alone. His Mood is Resolved. His Project completes. The confrontation fires without player involvement at a politically inopportune moment.

**Run B, Year 4:** Klapp has had direct contact with the player throughout Years 1-3. His Opinion of the player is "potential ally — demonstrates intellectual rigor, understands the stakes." His Concern "Who could support the confrontation?" has resolved to "the player." His Project includes the player as a Project-adjacent actor. When the Project completes, Klapp generates an Outreach scene offering the player a role in the confrontation.

The same NPC, same Project, same completing event, produces entirely different political dynamics based on player relationship investment. Run A: Klapp confronts Himlensendt alone and probably loses (no support). Run B: Klapp confronts Himlensendt with the player's support available and probably produces a better outcome.

This is not pattern-matching — the system produced different outcomes from different player histories without a pre-scripted branch. ✓

**Probe 3.2: Does the system avoid producing the same political crisis each playthrough?**

Concern resolution (Patch A) uses Conviction-weighted template libraries. The same treaty event produces different Concerns in different NPCs. Those Concerns resolve differently based on accumulated Memory content. But: in every playthrough, the Crown-Varfell treaty generates Concerns for Faith-aligned NPCs. Those Concerns resolve via the same Faith-conviction seeking tags. The resolution may hit the same conclusion ("heretical counsel corrupted Almud") in most playthroughs.

The specific Memory that is used to resolve the Concern varies by playthrough (which NPCs are around, what the player has done, what other events have occurred). But the seeking tag set is the same. If the seeking tags are Faith-conviction-specific and those tags tend to match the same event types regardless of playthrough, the system might always produce the same wrong conclusion.

**Issue 3.2:** Template library needs within-Conviction variation. A Faith-aligned NPC doesn't always conclude "heretical counsel." The template should select from multiple seeking-tag sets based on:
- NPC's current Mood (Anxious vs. Confident → different default explanation frames)
- NPC's Scar count (high Scars → less certain default explanation, more open to multiple hypotheses)
- NPC's prior Memory of similar events (if the NPC has resolved similar Concerns before, they draw on that resolution)

This requires per-Concern memory in the template library — whether the NPC has "been here before" changes how they interpret new ambiguous events. This adds one more NPC state field: `concern_history: list of resolved Concern tags` (limited to last 5 resolved Concerns). Template selection checks this history.

**Probe 3.3: NPC agency vs. faction AI priority tree — which wins?**

The proposal says Project advancement occurs when "the priority tree has discretionary capacity." But NPC behavior decisions are driven by the AI priority tree (existing npc_behavior §4.1). The proposal adds Project advancement as a discretionary action. This creates two decision systems for the same NPC.

Current specification: faction priority tree runs first; leftover capacity goes to Project. But the existing priority tree has 7 priority levels and NPCs typically consume Priority 1-4 slots, leaving discretionary space at 5-7. Projects go into that space. This is fine for most seasons.

But: what if the NPC's Project is actually *more important to them* than their Priority 5-6 faction activities? The Confessor's institutional duty at Priority 5 is "Altonian diplomacy." His personal Project is "defend Church doctrine from the Varfell alliance's theological implications." His Project is more important to him than attending to Altonian diplomacy. But the current system puts institutional duties first at Priority 5, Project second.

**Issue 3.3:** The priority tree needs a "personal priority insertion" mechanism for Project advancement when the NPC's Conviction alignment with their Project is high. If the Project's goal domain aligns with the NPC's primary Conviction, the Project can displace one Priority 5-6 institutional activity per season. This represents the NPC choosing their personal agenda over a relatively low-stakes institutional duty. At Priority 4 or above, institutional duties win (the stakes are too high to neglect). This makes Conviction-aligned Projects behaviorally dominant without letting NPCs ignore genuine crises.

**Probe 3.4: The Knowledge structure and the existing intel system**

Varfell's Private Collection unique action (params/factions §Varfell) gives "+2D to one Thread-related Domain Action this season OR reveal one hidden faction attribute OR −1 Ob to one Einhir Research action." One option is "reveal one hidden faction attribute." The Knowledge structure now also contains faction-relevant information held by individual NPCs.

Are these the same thing? "Reveal one hidden faction attribute" is a faction-level stat (Mandate, Intel, etc.) — it's not the same as Eyvind knowing about a Hafenmark spy. But they're adjacent — both are "discover something you didn't know about a faction." If the player can both use Varfell's Private Collection AND use Knowledge propagation chains, the overall intelligence available to the player is cumulative. This may produce over-informed players.

**Issue 3.4:** Not a mechanics conflict, but a calibration note: the Knowledge system should primarily surface individual-level, person-specific intelligence (Eyvind knows person X is a spy; Petra knows person Y has been acting strangely). Faction-level stat reveals remain in the Domain Action / intelligence system. The two systems cover different information domains and don't compete. This should be explicitly stated in the specification to prevent implementation scope creep.

---

### Audit 3

| # | Issue | Severity |
|---|---|---|
| 3.1 | Integration test passed — different player histories produce different NPC behavior | N/A (confirmation) |
| 3.2 | Concern templates may produce same wrong conclusions per-playthrough | High |
| 3.3 | Project vs. priority tree competition has no resolution for Conviction-aligned Projects | Medium |
| 3.4 | Knowledge and intel systems should be scoped explicitly as non-competing | Low |

---

### Patch 3

**Patch 3.2 — Within-Conviction template variation:**
Template selection adds NPC concern_history check and Mood modifier. Each Conviction has 3 template variants per event type:
- Variant Alpha: default (used when concern_history has no matching prior)
- Variant Beta: experienced (used when concern_history includes prior Concern of same type — NPC draws on prior experience, seeking tags shift toward more nuanced interpretation)
- Variant Gamma: mood-modified (used when Mood is Anxious or Humiliated — heightened threat frame, seeking tags shift toward more defensive explanations)

Add `concern_history: list[resolved_concern_tag]` (max 5 entries) to NPC State.

**Patch 3.3 — Personal priority insertion:**
If NPC's active Project goal domain aligns with primary Conviction AND Project progress > 0 (not stalled): Project advancement may displace one Priority 5-6 institutional activity per season. Displacement generates a small risk (institutional_deference check at Ob 1; failure means faction leader notes the neglect via a Settlement Signal or inner-circle observation; generates a minor negative Opinion drift toward the NPC from the faction leader). This risk scales with institutional_deference personality: high-deference NPCs rarely displace; low-deference NPCs displace regularly and have higher detection risk tolerance.

**Patch 3.4 — Explicit scope declaration:**
Add to specification preamble: "The Knowledge system tracks person-specific, individual-held information (who knows what about whom). Faction-level intelligence (stats, Domain Action plans, territorial conditions) remains in the existing Intelligence system (Varfell Private Collection, settlement-layer brokers, Standing-gated faction state visibility). The two systems are explicitly non-competing. Knowledge never surfaces faction stats; Intelligence operations never surface personal Knowledge items."

---

### Final Critique

**The system is now mechanically specific but has substantial content authorship obligations that must be acknowledged as pre-launch gates, not aspirational additions.**

Minimum content required before the system is functional:
- 210 Concern templates (7 Convictions × 30 event types × 3 variants Alpha/Beta/Gamma) = 630 authored entries
- 35+ starting Projects with all fields (goal, visible_actions, completion_effect, failure_effect, progress stages)
- ~350 seeded Opinions for significant NPC pairs
- Knowledge seeding per information-rich NPC (~150 starting Knowledge facts across ~30 relevant NPCs)
- Dialogue variants for Knot-surfaced Concerns (~30 authored fragments per the Patch 2.2 estimate)
- Gossip text templates per event type and Concern resolution outcome (~100 gossip fragments)

This is not optional. The system without this content is a framework that runs correctly but produces mechanical outputs without political texture.

**The system still has one unresolved structural tension:** the Immediate Update mechanism (Patch F/Patch 1, for large events) runs a partial Procedure D+A out-of-sequence for affected NPCs. This means that for the most politically significant events — exactly the events where correct propagation matters most — the system runs in a special mode. Special modes introduce bugs. The implementation risk is higher than the proposal acknowledges. Recommend: implement and test the normal Accounting sequence first and completely. Add Immediate Update only after the base system passes a full simulation cycle without bugs. The delay cost (one season for large-event Opinion propagation) is acceptable during early implementation and can be eliminated in a later pass.

---

## What the Proposal Has Become

After three iterations: a mechanically specific architecture that is honest about its costs and gaps, produces differentiated behavior across playthroughs, passes bidirectional cascading tests, integrates with existing Valoria systems without contradiction, and identifies its content authorship obligations explicitly.

What it is not: a finished specification ready for Godot implementation. The content authorship gates are real. The computational budget estimates are honest uncertainty ranges, not confirmed figures. The system's emergent quality — whether it actually produces the political richness described — will only be known after a simulation pass tests the Concern template library against several dozen representative game states.

The system is ready for simulation design. It is not ready for implementation.
