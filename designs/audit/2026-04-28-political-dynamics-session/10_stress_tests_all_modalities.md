<!-- [PROVISIONAL: 2026-04-28 session — intensive stress tests all modalities] -->
<!-- STATUS: PROVISIONAL — stress test findings, patches, and spec additions -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/10_stress_tests_all_modalities.md -->

# Intensive Stress Testing: All Modalities

Tests are designed to find breaks, not confirm function. Each test probes a different modality: cascade depth, simultaneous events, long-run behavior, adversarial inputs, degenerate states, information propagation, edge cases in data structures, and cross-scale boundary conditions.

---

## ST-1: Cascade Depth — How Many Degrees Before Natural Damping?

**Probe:** Player wins Total Victory Contest against Confessor. How many degrees of cascade does the personal event produce before naturally attenuating?

**Trace:**
- Degree 0: Contest → Confessor Scar. Real-time Mood → Distracted.
- Degree 1: Procedure B → Concern generated. Procedure C → established Project continues at +1 Ob. Church ministry action in Settlement S-004 Verdmuld: partial success (vs full success prior).
- Degree 2: Settlement Signal from Verdmuld: reduced faith-institutional resonance, salience 2. Propagates to Church inner-circle Active NPC (Himlensendt). Church Faction Meta-Armature generates Concern: "Doctrinal reach faltering."
- Degree 3: Church Concern biases AI priority tree toward Assert (CI advance) over other Domain Actions this season. If Assert succeeds, CI +2. If CI was on a threshold edge, this flips a game-state condition.
- Degree 4: CI threshold flip alters territory seizure odds next season. Changes territorial conditions.

**Issue found (ST-1-A):** No damping specification. The system propagates indefinitely through state-dependent chains. A personal Contest can, in sufficient game-state conditions, contribute to faction-level territorial change through a valid but fragile causal path.

**Required:** Signal strength decay at each scale transition. Each time a signal crosses a scale boundary (personal→settlement, settlement→faction), its magnitude is attenuated by a decay factor. Settlement Signal strength is the originating Memory's salience × 0.7. Faction Concern salience from Settlement Signal is Settlement Signal strength × 0.7 again. At two transitions, a personal event at salience 4 contributes a faction Concern at salience 4 × 0.49 ≈ 2. A faction Concern at salience 2 influences Domain Action selection at 30% weight vs salience 5 at 100%. The decay prevents runaway cascade sensitivity without eliminating meaningful cross-scale propagation.

**Patch ST-1:** Scale-transition decay factor: 0.7 per boundary crossed. Faction Concern salience = originating event salience × 0.7^(transitions_crossed). Minimum meaningful salience for Domain Action influence: 2. Below 2, Concern generates but doesn't affect Domain Action selection.

---

## ST-2: Simultaneous Crisis — Five Major Events in One Season

**Probe:** Season 8, Year 4:
1. Almud acquires Conviction Scar (Arc transition begins)
2. Hafenmark passes constitutional amendment
3. Player's Vaynard contact discovered by Crown Spymaster
4. Klapp's Stillhelm Codex Project completes (public scholarly challenge to Himlensendt)
5. Vaynard's Thread Sensitivity crosses Active threshold (TS 50+)

All five generate Event Impact Matrices. All five create Concerns in overlapping NPC sets. Moods set in real-time across the session.

**Scene Slate saturation:** Each event generates multiple Outreach scenes.
- Almud's Scar: Crown inner-circle Outreach scenes (each NPC evaluating succession implications)
- Amendment: Hafenmark and Crown inner-circle scenes
- Discovery: Spymaster Demand scene targeting player
- Klapp's completion: Confessor confrontation scene, Klapp-to-player scene
- Vaynard's threshold: Wardens notification, Varfell inner-circle scenes

Estimated scene count next season: 12-18 Priority 1-3 scenes. Player has 3-5 scene actions. Witness Mode fires for 8-14 scenes.

**Issue found (ST-2-A):** In a crisis of 5+ simultaneous major events, Witness Mode fires extensively. The player receives Read actions from witnessed scenes. With 12 Witness scenes, the player gains 12 Read results — an information flood that may be overwhelming rather than useful, and which the player cannot act on in real-time.

**Issue found (ST-2-B):** Internal priority ordering (player_agency §4.2) handles sequential priorities but wasn't designed for 5-way simultaneous crisis. The ordering (1. Faction Leader Removal, 2. Heresy Investigation, 3. Stability Crisis, 4. Mass Battle, 5. Knot Partner in Crisis, 6. Companion Arc...) may produce the wrong prioritization in combined crises. Example: Klapp's scholarly confrontation (Priority 6 — Companion Arc) may be more consequential to the player's political strategy than the amendment (which they can't affect directly anyway, Priority 5 by analogy). The priority ordering doesn't account for player investment.

**Patch ST-2-A:** Witness Mode information cap: maximum 3 Read results from a single Accounting's Witness Mode, regardless of how many scenes are witnessed. The player receives the 3 most scene-action-relevant results (those involving NPCs with highest Disposition with player). Remaining Witness scenes produce narrative summary only — "The Cardinal confronted Himlensendt publicly. You weren't there. Consequences pending." This prevents information flood while preserving dramatic weight.

**Patch ST-2-B:** Player investment modifier to crisis priority. Before applying the canonical priority ordering, scenes involving NPCs with Disposition ≥ +3 with the player receive +1 to their priority level (lowering their position number = higher priority). This allows the player's existing relationships to shape which crises they personally attend. A player deeply invested in Klapp attends the scholarly confrontation over a distant amendment they couldn't influence anyway.

---

## ST-3: Long-Run Temporal — Year 15 Behavior

**Probe:** By Year 15 (60 seasons at 4/year), what does the system's state look like?

**Memory saturation:** Each Active NPC has accumulated Memory for 60 seasons. Cap is 10. Memory replacement has been running for approximately 40 seasons. Low-salience early Memories have been displaced.

**Issue found (ST-3-A):** A Memory from Year 1 that was foundational (the player's first significant interaction with Almud, establishing the basis of their entire relationship) has a starting salience of, say, 4. After 60 seasons of decay at -1 per 4 seasons: remaining salience = 4 - 15 = -11. Floor at 0; the Memory's salience is 0 and would be displaced by any new Memory.

By Year 15, the founding Memories of major NPC relationships have been displaced. The player's relationship with Almud at Year 15 is shaped only by the last 10 significant Memories — the first 50 seasons of interactions have been lost. This produces a system where long-term relationships reset over time rather than accumulating history. Historically wrong: real political relationships carry weight precisely because they're long — "we've been through things together" is the argument.

**Issue found (ST-3-B):** Wrong Beliefs from early Concern resolutions (Year 1-3, when NPC information was sparse) may have persisted for 12 years without self-correction. If no high-salience contradicting Memories have arrived for the wrong Belief's domain (the domain just hasn't been active), the wrong Belief is now deeply entrenched with 12 years of behavioral consistency reinforcing it. Self-correction is nearly impossible because the wrong Belief now has accumulated experiential support (the NPC has been interpreting experiences through it for 12 years, each interpretation generating Memories that fit the wrong frame).

**Issue found (ST-3-C):** Established Projects (progress ≥ 3) that have been running for 10+ seasons should have long since completed (success or failure at the 8-season stall threshold). By Year 15, each NPC should be on their 3rd+ Project. The cumulative effect of completed Projects on the political landscape needs specification: what happens to the political landscape when 35 NPCs have each completed 2-3 Projects?

**Patch ST-3-A:** Referenced Memories get a salience floor. Each time a Memory is referenced (in Opinion drift calculation, in Concern resolution, in armature seeking-tag matching), it gains +0.5 salience (max 5). Memories that are repeatedly used to explain the NPC's world maintain relevance. Memories from the founding period of a relationship that have been referenced hundreds of times remain salient; trivial Memories from the same period that were never referenced decay normally. This produces long-term Memory that's weighted by use, not just by original salience.

**Patch ST-3-B:** Entrenched wrong Beliefs need a specific counter-mechanism. After 8+ seasons (2 years of game time) without contradicting Memories, a wrong Belief becomes "calcified" — harder to revise. Calcified wrong Beliefs require 3+ high-salience contradicting Memories (up from the standard 2) for self-correction. Social Contest can still break them but at +1 Ob (the Belief is deeply entrenched). This makes early political investment in correcting wrong Beliefs more valuable: uncorrected for 8 seasons, they become significantly harder to shift.

**Patch ST-3-C:** Completed Project legacy. When a Project completes, its effects on the political landscape are specified in completion_effect (existing). But the *NPC's self-conception* also updates: successful completion → +0.5 affect_axis toward NPCs who supported the Project; failed completion → -0.5 toward NPCs who obstructed it. These relationship adjustments persist even as the NPC moves to their next Project. Over 12 years and 3 Projects, this creates lasting relational residue — NPCs who cooperated repeatedly on Projects have deeply positive Opinions; NPCs who repeatedly obstructed each other have deeply negative ones. The long-run political alignment of the inner circle reflects its Project history.

---

## ST-4: Information Propagation Storm — Knowledge Chain Depth

**Probe:** Fact A (salience 4, sensitivity 2) originates with Father Eyvind. How far does it travel?

**Hop 1:** Eyvind → Petra (merchant). Petra's Concern matches seeking tag. Transfer occurs. Petra holds Fact A at salience 3, sensitivity 2.

**Hop 2:** Petra → Bjorn (magistrate). Bjorn's Concern matches. Transfer occurs. Bjorn holds Fact A at salience 2. Salience ≥ 3 threshold for further transfer: NOT met. Propagation stops here.

With salience 4 origin: maximum 2 hops before decay kills propagation. ✓

**Issue found (ST-4-A):** Knowledge decay rate for the *originator* is unspecified. Does Eyvind's copy of Fact A also decay over time? If yes: after 4 seasons, Eyvind's salience has dropped to 0. The original knowledge source no longer holds the fact. This is wrong for some knowledge (a priest doesn't "forget" he witnessed a spy in his settlement) and right for others (information about a specific tactical deployment becomes stale after the campaign ends).

**Issue found (ST-4-B):** Knowledge rendered obsolete by events. If the spy is arrested in Season 12, Eyvind's Knowledge "Hafenmark spy operating in Niedmark" is now false. The Knowledge structure has no mechanism for updating Knowledge facts as the game state changes. A player could potentially learn from Eyvind in Season 15 that the spy is operating — based on information that's been obsolete for 3 years.

**Patch ST-4-A:** Distinguish Knowledge decay by type:
- Fact-type: `ongoing-state` (spy is *currently* operating): decays at standard rate, becomes invalid when state ends
- Fact-type: `historical-event` (spy *was* arrested): doesn't decay — historical facts remain true
- Fact-type: `structural` (Hafenmark has covert operations in this region): decays very slowly (−0.1/season), may remain relevant for years

Add `knowledge_type: {ongoing_state, historical_event, structural}` to Knowledge record. `ongoing_state` decays normally and is marked invalid when the relevant game state changes. `historical_event` salience is fixed (doesn't decay). `structural` decays at 0.1/season.

**Patch ST-4-B:** Event-driven Knowledge invalidation. When a game-state event occurs that renders an ongoing_state Knowledge fact false (spy arrested, building destroyed, treaty dissolved), all NPCs holding that Knowledge fact have it marked invalid. Their next Concern that would use this Knowledge resolves to "I thought X, but things may have changed" — generating a new Concern about the domain rather than using stale data.

---

## ST-5: Adversarial Player — Systematic Insinuate Farming

**Probe:** Player dedicates all 5 scene actions per season to Insinuate against Crown inner-circle NPCs. 5 NPCs targeted × 4 seasons = 20 Insinuate attempts.

At base 50% success rate (standard Attunement pool vs Ob): ~10 successes. Each reduces target NPC's Disposition with Crown leader by -1. Average effect: each of 5 NPCs reduced by -2 over 4 seasons. Starting at Disposition +2-3 with leader: all end at 0 to +1 — low but not catastrophically low.

**But:** the player has used 20 scene actions on Insinuate instead of other activities. No relationship building, no governance, no intelligence gathering. This costs them relationship development, Standing advancement lag, and Renown stagnation. Ω-d holds: this approach pays its cost in alternative-activity forgone.

**However:** counter-intelligence. Crown Intel roll vs player's Cover per season. If Crown Intel is 5 (pool of 5d10, TN 7): E[successes] ≈ 1.5/season. Player's Cover (Cog + History): a dedicated Insinuate player probably has Cover 3-4. E[Intel successes] ≈ 1.5 vs Ob 3-4: ~10-15% detection probability per season. Over 4 seasons: ~40-50% chance of at least one detection. But detection is probabilistic, not guaranteed.

**Issue found (ST-5-A):** No faction-level anomaly detection beyond individual Intel rolls. A faction leader who observes that multiple inner-circle members are simultaneously behaving strangely (all showing reduced Disposition with the leader, all generating divergent Domain Action proposals, all at Distracted or Humiliated mood for unexplained reasons) should generate a faction-level Concern: "My court is being systematically destabilized." This Concern could lead to an internal investigation (intelligence-focused Domain Action) regardless of whether any individual Intel roll succeeded.

**Patch ST-5:** Faction-level anomaly detection. At Accounting, the Faction Meta-Armature checks: if ≥ 3 inner-circle NPCs simultaneously show Disposition-with-leader < baseline AND at least 2 are in negative Mood states (Distracted, Humiliated, Anxious) without obvious external cause (no major crisis events this season): generate faction-level Concern "Internal destabilization detected?" with salience 4. This Concern drives: faction leader initiates Loyalty Interviews (existing Demand scene mechanic) with flagged NPCs simultaneously. This does not directly expose the player but creates a political environment where NPCs under Insinuate pressure face additional scrutiny from their own leader — some may confess suspicions, some may deflect, generating scenes that may expose the operation.

---

## ST-6: Degenerate State — Mass Distraction

**Probe:** 60% of Crown inner-circle NPCs are Distracted simultaneously (3 of 5 major Scar events in one season).

**Effects on Faction Meta-Armature:**
- Inner-circle aggregate: Distracted NPC armatures produce less decisive seeking-tag weighting (Distracted modifier: +1 Ob to all actions means less confident interpretation). The aggregate becomes ambiguous — multiple domains weighted roughly equally, no dominant interpretation.
- institutional_stability: unchanged (not NPC-dependent in this season).
- Result: Faction Meta-Armature interpretation is muddled. Domain Action selection may be incoherent.

**Effects on Procedure E:**
- 3 of 5 inner-circle NPCs at 20% ambient contact: ~10 inner-circle interactions this season (vs 63 normal). Almost no lateral relationship development.
- Gossip propagation effectively stops — no interactions, no gossip generated.

**Effects on Domain Action proposals:**
- Distracted NPCs with high institutional_deference don't propose.
- Only low-deference NPCs (if any are Distracted) may still propose at +1 Ob.

**Issue found (ST-6-A):** Crown can be effectively paralyzed for one season by a player who engineers 3+ simultaneous Conviction Scars. In principle this requires winning 3 Total Victory social Contests against inner-circle NPCs in a single season, which requires approximately 15 scene actions (5 per Contest minimum). Player has 3-5 scene actions. Impossible in one season directly.

But: Klapp's scholarly confrontation (Project completion) generates Himlensendt's Scar autonomously. If the player engineered Klapp's confrontation AND won a Contest against Marshal AND triggered a third NPC arc — three Scars in one season is feasible through combination of player action and autonomous NPC action.

**Issue found (ST-6-B):** The Faction Meta-Armature has no crisis threshold behavior. When the inner-circle is compromised, the faction should activate survival-mode behavior (existing Priority 1 in all NPC priority trees), not become confused.

**Patch ST-6:** Faction crisis threshold. If ≥ 40% of inner-circle NPCs are Distracted or Grieving simultaneously: Faction Meta-Armature overrides to "institutional autopilot" mode. In autopilot: faction executes only existing Priority 1-2 Domain Actions from pre-existing patterns. No new NPC Project proposals accepted. No inner-circle competition. Faction runs on institutional inertia alone until the following Accounting when Moods may have recovered. Autopilot does not reduce the faction's ability to respond to threats — survival actions still fire. It only suppresses the NPC-autonomous political activity that requires functioning inner-circle engagement.

---

## ST-7: Weight Normalization — Settlement Without Passive NPCs

**Probe:** Remote Outpost S-019 "Stillhelm Watch" has a governor (Warden-affiliated, Continuity Conviction) and anonymous population. Zero named Passive NPCs.

**Weight formula:**
- Governor tenure 6 seasons: 0.1 + 0.075 × 4 = 0.4
- Passive NPC aggregate: 0 (no Passive NPCs)
- Institutional character (Outpost): Autonomy bias, weight 0.2
- Population: Continuity-adjacent (Warden-area population), weight 0.1
- Total: 0.4 + 0 + 0.2 + 0.1 = 0.7. Not 1.0.

**Issue confirmed (ST-7-A):** Weights don't sum to 1.0 when a tier is absent.

**Patch ST-7:** Weight normalization rule. Available weight components summed and normalized to 1.0. Formula: each component's effective weight = raw_weight / sum(all_present_component_weights). For the Outpost: governor 0.4, institutional 0.2, population 0.1 → sum = 0.7 → normalized: governor 57%, institutional 29%, population 14%. The governor becomes dominant when Passive NPCs are absent. This is correct: a Warden outpost without civilian NPCs is shaped almost entirely by the Warden governor's interpretation.

---

## ST-8: Collapsed Faction Inner-Circle Friction

**Probe:** Hafenmark collapses to city-state. Baralta + 1 loyal advisor remain. Inner-circle size: 2.

**Faction Meta-Armature:** Leader (Baralta, Precedent, Standing 7, weight 1.5×), advisor (Faith, Standing 4, weight 0.3). Total weight 1.8. Baralta: 83%, Advisor: 17%.

**Domain Action proposals:** Baralta proposes; advisor either supports or opposes (+1/-1 Ob). No competition (one proposer). No Ob modifiers from other supporting NPCs.

**Issue confirmed (ST-8-A):** Collapsed faction with small inner-circle has LESS friction than full faction. A 5-NPC inner circle has competition, competing proposals, +Ob from opposition. A 2-NPC inner circle has one proposer who always wins, with only +1 Ob from the advisor's potential opposition.

**Patch ST-8:** Minimum inner-circle friction rule. When inner-circle active count < 3: all faction Domain Actions take +1 Ob (institutional stress modifier). This represents: reduced information (only 2 advisors means worse intelligence), uncertain loyalty (2 people can't maintain the institutional confidence of 5), fragmented authority (whoever remains is holding together an institution designed for more people). The modifier stacks with any advisor opposition (+1 Ob additional). A 2-person collapsed faction faces +1 to +2 Ob on all Domain Actions. Mechanically distinguishes collapse from functioning faction even before territorial losses.

---

## ST-9: Factional Exposure Under Loyalty Cover

**Probe:** Player is Crown Standing 5. Same season: attends Crown inner-circle council (major loyalty signal), votes aligned with Almud on a contested Domain Action, AND meets privately with Vaynard representative at an inn.

**Factional Exposure:** Vaynard meeting adds Exposure. Crown Intel roll at Accounting: Intel pool vs Cover.

**Current spec:** Cover = Cog + History. No loyalty-signal modifier. Intel roll is independent of same-season loyalty signals.

**Issue found (ST-9-A):** The system treats Factional Exposure surveillance as context-independent. A player who attends council AND shows strong loyalty signals in the same season faces the same detection probability as one who meets Vaynard without doing anything else.

**Historical accuracy test:** Historical intelligence operations universally leveraged overt loyalty as cover. Walsingham's agents maintained court positions. Venetian bailo diplomats had official cover for intelligence work. Overt institutional participation reduces institutional suspicion of covert activity. The current spec misses this.

**Patch ST-9:** Cover bonus from same-season loyalty signals. Strong loyalty signal (council attendance with aligned vote, Standing advancement action, public defense of faction interest in a crisis) adds +1 to Cover for the season's Factual Exposure calculations. Maximum +2 total bonus from loyalty signals. Loyalty Cover decays each season it's not renewed — it's an active maintenance cost, not a permanent bonus. This makes active faction participation genuinely protective and creates a meaningful strategic choice: invest scene actions in loyalty signaling to maintain cover for cross-faction operations.

---

## ST-10: Deliberate Faction Fragmentation — Intended or Bug?

**Probe:** Player at Standing 5 (Crown) deliberately engineers Confessor vs. Marshal rivalry (Reconcile actions blocked, Treaty proposals chosen to irritate Confessor while satisfying Marshal). Over 4 seasons, inner-circle Regard fragments: Marshal bloc (player + Marshal + Spymaster) vs Confessor bloc (Confessor + Cardinal Klapp).

**Assessment:** Two blocs competing in the same faction = inner-circle paralysis. Domain Action proposals split. Ob modifiers increase across all actions (each bloc opposes the other's proposals). Crown functions at reduced effectiveness.

**Is this a bug?** No — per Ω-d: every action pays what it buys. Fragmenting the court eliminates rivals (Confessor's bloc can't advance their agenda when the player's bloc obstructs them) but weakens the faction (the player's own Domain Action proposals also face +Ob from Confessor's bloc). The player who engineers fragmentation accepts reduced faction effectiveness as the cost of internal political dominance. This is the Byzantine themata-civil rivalry dynamic operating as designed. Confirm as intended.

**Corollary design note:** The player who fragments their faction purely for internal political gain will find external enemies exploiting the weakness (Varfell's AI detects Crown's reduced Domain Action efficiency and times aggressive moves accordingly). The strategic cost is real and external. ✓

---

## ST-11: affect_axis Bound Enforcement

**Probe:** Knot rupture (ED-664: public citation of counsel). Spec says "Disposition resets to −4." Opinion affect_axis for the player: also −4? Outside the [-3, +3] range.

**Drift formula at affect_axis −4:** base × (1 - |-4|/3) = base × (1 - 1.33) = base × (-0.33). Negative drift. Formula produces undefined behavior — drift in negative direction from an already-minimum value, compounding without floor.

**Issue confirmed (ST-11-A):** Discrete events can push affect_axis outside the valid range, breaking the drift formula.

**Patch ST-11:** Hard clamp on all affect_axis writes. Any operation setting affect_axis: clamp(-3, affect_axis, +3). No exceptions. Discrete events that "should" produce extreme values (betrayal, Knot rupture) clamp to ±3. The formula remains valid. The extreme states are representable at ±3 without formula breakage.

Note: Disposition (player relationship) can go to −4 per the Knot-rupture rule. Opinion affect_axis (NPC-NPC) clamps at ±3. These are separate data structures. Disposition's −4 value is handled by the existing fieldwork system rules, not the Opinion drift formula.

---

## ST-12: Unaffiliated NPC Domain Action Projects

**Probe:** Baralta loses all provinces. She and her advisor retreat to S-015 Gransol Parliament (city-state). Baralta's active Project: "Reconstitute Hafenmark through parliamentary coalition" (progress 6/10, established). This Project requires Domain Actions to execute (petition, diplomacy, faction formation).

**Issue found (ST-12-A):** With no faction infrastructure, Domain Action proposals have nowhere to go. Baralta generates a DA proposal (advancing her Project), but no faction AI priority tree receives it.

**Issue found (ST-12-B):** The collapsed faction's "partial stat sheet" (Influence, Wealth, Stability per §6.3 Faction Collapse) means some Domain Actions are still available — specifically Influence and Wealth-based ones. But the Domain Action proposal mechanism assumes full faction stat sheet.

**Patch ST-12-A:** Unaffiliated-NPC Projects with Domain Action requirements automatically downgrade to personal-scale equivalent actions. "Reconstitute Hafenmark" can't fire as a faction Domain Action, but Baralta can still advance it through: fieldwork (investigating parliamentary procedures), social actions (building Disposition with parliamentary members), intelligence gathering. Progress advances at 0.5/season via personal-scale actions vs 1/season via Domain Actions. The Project remains viable but slower without institutional infrastructure.

**Patch ST-12-B:** City-state Domain Actions. Collapsed factions (partial stat sheet) can issue Domain Actions using available stats (Influence, Wealth, Stability). These are limited: only Influence and Wealth Domain Actions, not Military or Mandate-based ones. Ob = floor(relevant_stat / 2) + 1 (same as standard). This lets city-state Hafenmark pursue diplomatic and economic Domain Actions while remaining unable to field armies or issue royal decrees. The city-state is a functional actor, just diminished.

---

## Part 2: Issues Consolidated

| # | Issue | Severity | Patch |
|---|---|---|---|
| ST-1-A | No cascade damping — personal events can ripple to global scale | Critical | Scale-transition decay 0.7× per boundary |
| ST-2-A | Witness Mode information flood under simultaneous crisis | High | Cap 3 Read results from Witness; player-investment priority modifier |
| ST-2-B | Priority ordering not designed for 5-way crisis | Medium | Player Disposition investment shifts crisis priority |
| ST-3-A | Founding relationship Memories displaced by Year 15 | High | Referenced Memories gain +0.5 salience per use; floor at reference count × 0.5 |
| ST-3-B | Wrong Beliefs calcify after 8 seasons unchallenged | Medium | Calcified wrong Beliefs require 3+ contradicting Memories (up from 2); +1 Ob on Contest |
| ST-3-C | Completed Project legacy on relationships unspecified | Low | Successful completion → +0.5 affect_axis toward supporters; failure → −0.5 toward obstructors |
| ST-4-A | Knowledge originator decay unspecified by type | Medium | Three knowledge types: ongoing_state (decays), historical_event (fixed), structural (−0.1/season) |
| ST-4-B | Obsolete Knowledge not invalidated by events | High | Event-driven Knowledge invalidation when ongoing_state fact becomes false |
| ST-5-A | No faction-level anomaly detection beyond individual Intel rolls | High | Faction Meta-Armature anomaly check: ≥3 NPCs simultaneously low-Disposition + negative Mood → faction Concern |
| ST-6-A,B | Mass Distraction produces faction paralysis | High | Faction crisis threshold ≥40% Distracted/Grieving → institutional autopilot |
| ST-7-A | Weights don't sum to 1.0 when tiers are absent | High | Normalize weights to sum = 1.0 when tier is empty |
| ST-8-A | Collapsed faction has less friction than full faction | Medium | Minimum inner-circle friction: inner-circle count < 3 → +1 Ob on all Domain Actions |
| ST-9-A | Factional Exposure ignores same-season loyalty signals | Medium | Loyalty Cover: +1 Cover per major loyalty signal this season, max +2 |
| ST-10 | Deliberate faction fragmentation | Confirmed intended — no patch |
| ST-11-A | Discrete events can set affect_axis outside [-3, +3] | Critical | Hard clamp on all affect_axis writes |
| ST-12-A | Unaffiliated NPC Domain Action Projects break | Medium | Downgrade to personal-scale at 0.5× progress |
| ST-12-B | City-state Domain Actions unspecified | Medium | City-state limited to Influence/Wealth Domain Actions |

---

## Part 3: Revised Specification Additions

**Add to §3.4 Procedures — Procedure B:**
- Calcified wrong Belief threshold: Belief unchallenged 8+ seasons → requires 3+ contradicting Memories for self-correction; social Contest at +1 Ob.
- Knowledge invalidation: ongoing_state Knowledge facts checked against current game state each Accounting; marked invalid if underlying state has changed.
- Knowledge type field added to Knowledge structure: `{ongoing_state, historical_event, structural}`.

**Add to §3.4 Procedures — Procedure C:**
- Completed Project legacy: success → +0.5 affect_axis toward supporting NPCs in Opinion drift pass; failure → −0.5 toward obstructing NPCs.
- City-state Project downgrade: unaffiliated NPC Projects requiring Domain Actions → personal-scale at 0.5× progress rate.

**Add to §3.4 Procedures — Procedure D:**
- Referenced Memory salience floor: Memory referenced in Opinion drift or Concern resolution gains +0.5 salience (max 5, applied after standard decay).
- Hard clamp on affect_axis: all writes clamped to [-3, +3].

**Add to §3.4 Procedures — Procedure E:**
- Witness Mode cap: max 3 Read results per Accounting from Witness Mode.
- Distracted ambient rate: 20% (from 60%).

**Add to §3.5 Settlement Meta-Armature:**
- Weight normalization: normalize all present-tier weights to sum = 1.0 when any tier is absent (typically Passive NPC tier for sparse settlements).
- Governor tenure scaling: 0.1 + 0.075 × min(tenure_seasons, 4).

**Add to §3.6 Faction Meta-Armature:**
- Minimum inner-circle friction: inner-circle active count < 3 → +1 Ob on all Domain Actions (institutional stress).
- Faction crisis threshold: ≥ 40% inner-circle in {Distracted, Grieving} simultaneously → institutional autopilot mode (Priority 1-2 only; no NPC Project proposals).
- Anomaly detection: ≥ 3 inner-circle NPCs simultaneously {Disposition-with-leader < baseline} + negative Mood states + no major crisis event this season → faction Concern "Internal destabilization detected?" salience 4.
- City-state Domain Actions: partial stat sheet factions (Influence, Wealth, Stability only) can issue Influence and Wealth Domain Actions only.

**Add to Event Impact Matrix (§1.2):**
- Scope cap confirmed: symbolic_effects lists inner-circle NPCs of affected factions only, not all Active NPCs.
- Scale-transition decay: signal propagated across a scale boundary reduced by ×0.7. Faction Concern salience from Settlement Signal = salience × 0.7. Faction Concern salience below 2 does not affect Domain Action selection (exists but inert).

**Add to Factional Exposure:**
- Loyalty Cover: same-season major loyalty signals add +1 to Cover for this season's Exposure calculations (max +2). Major loyalty signals: council attendance with aligned vote, Standing advancement action, public faction defense.

**Add to Scene Slate:**
- 5-way crisis triage: NPCs with Disposition ≥ +3 with player receive +1 to their scene priority level. Player investment shapes which crises they personally attend.

---

## Part 4: What Passed Without Issue

These modalities tested clean:

- **affect_axis dampened drift bounds** (ST-11 extended): drift formula naturally prevents runaway escalation; only discrete events could escape bounds, now patched.
- **Deliberate faction fragmentation** (ST-10): correctly produces strategic tradeoff (internal dominance vs external vulnerability). Ω-d holds.
- **Single large event cascade** (T-11 from prior doc): political loop closes correctly through Domain Action → NPC Concern → Outreach scene.
- **Faction collapse behavior** (ST-8 base): the one-NPC scenario produces sensible single-leader dominance, just with too little friction (patched).
- **Knowledge propagation hop limit** (ST-4 base): natural salience decay limits Knowledge to 2-3 hops before the salience threshold kills propagation. No runaway information flood from knowledge propagation alone.
- **Armature behavior under arc transition** (Scar modulation): Scar count softening of Conviction weighting produces smooth behavioral drift as NPCs transform, not abrupt personality flips.
- **Long-run wrong Belief dynamics** (ST-3-B): the calcification mechanism produces realistic path dependency — early political investment in correcting wrong Beliefs has lasting value.
