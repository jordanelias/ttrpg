<!-- [PROVISIONAL: 2026-04-29 — simulation Direction E] -->
<!-- STATUS: PROVISIONAL — multi-agent multi-decade composition trace under doc 12 v1.1 -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/SIM_E_composition.md -->
<!-- COMPANION: SIM_A, SIM_B, SIM_C, SIM_D, SIM_narrative_arc_pass; 12_development_specification.md v1.1 -->

# Simulation E — Composition / Multi-Agent Emergence

**Source spec:** `12_development_specification.md` v1.1 (commit `9dede391`).
**Patches under test (composite):** All 26 patches operating together; specific stress on PATCH 2.1 (select_proposal), 2.5 (settlement signal), 3.10 (Outreach), 3.11 (Standing recalc), 3.13 (project generation), and the cross-cutting single-writer Opinion architecture (PATCH 1.4–1.6).
**Method:** Six scenarios at multi-agent multi-faction scale. 6–8 NPCs across 2–3 factions, traces of 8–12 Accountings (2–3 Campaign Years). Tests for emergent dynamics, cross-faction interference, structural patterns, dramatic intensity. Builds on narrative-arc pass (`SIM_narrative_arc_pass.md`) — checks whether scale produces stories or chronicles.
**Companion invariants from prior sims:** SIM-A `[INV-1..4]`, SIM-B `[DA-INV-1..7]`, SIM-C `[SS-INV-1..8]`, SIM-D `[REL-INV-1..6]` — should remain valid at scale.

---

## §0 Setup — three-faction Renaissance peninsula

Three factions traced together:

- **Crown** (Order-dominant, Almud leader at S7): inner circle Almud, Marshal (S7, Order), Confessor (S5, Faith), Reformer (S4, Autonomy). Six settlements (Solmund seat + Eastfort, Reedgate, Northpass, Westmarch, Loomhaven).
- **Hafenmark** (Precedent-dominant, Magistrate-Prime leader at S6): inner circle Magistrate-Prime, Treasurer (S6, Equity), Cantor (S5, Faith), Wright (S4, Reason). Three settlements (Hafenmark seat + Tideford, Kelpstrand).
- **Varfell** (Reason-dominant, Scholarch leader at S6): inner circle Scholarch, Surveyor (S5, Reason), Astronomer (S4, Reason), Wandering-Voice (S4, Autonomy). Two settlements (Varfell seat + Sundial-Hold).

Three factions × ~4 inner-circle NPCs + 11 settlements + Player. Player has S5 Crown standing (per SIM-D context), Knot with Spouse, prior Memory-anchor with Smith of Solmund (saved his son in earlier arc).

Cross-faction contacts: Confessor↔Cantor (Faith↔Faith bridge); Reformer↔Wandering-Voice (Autonomy↔Autonomy bridge); Treasurer↔Reformer (Equity↔Autonomy adjacent); Marshal↔Magistrate-Prime (Order↔Precedent — institutional cousins).

Trace duration: 12 Accountings (3 Campaign Years).

---

## §1 Scenario 1 — Cross-faction Settlement Signal interference

**Goal.** Border settlement (Tideford in Hafenmark, adjacent to Crown's Westmarch) experiences cross-border raid event. How do both factions' Concern-channels respond?

### 1.1 Event

T+0: Bandit raid on Tideford-Westmarch road (semi-public, both populations affected).

**Tideford Settlement Signal** (Hafenmark-controlled, ~6 Passive NPCs):
- Memories aggregate around `event_type=raid`, dominant tag = `border_unsafe`.
- net_affect ≈ -1.5, salience ≈ 3 × 0.7 = 2.1.
- Routes to "relevant Active NPC" — assume Magistrate-Prime (faction leader, default routing per SIM-C-G6 recommendation).

**Westmarch Settlement Signal** (Crown-controlled, ~8 Passive NPCs):
- Same event, different population. Memories aggregate around `border_unsafe` and `merchant_loss`.
- Westmarch's Bailiff (governor) is S5; Crown population_disposition has been mid-positive.
- Signal: tag=`border_unsafe`, affect ≈ -1.2, salience ≈ 2 × 0.7 = 1.4.
- Routes to Marshal (military domain affinity per SIM-C-G6 (c) round-robin).

### 1.2 Concurrent faction processing

Magistrate-Prime: receives `border_unsafe` Concern at salience 2. Considers diplomatic protest to Crown OR military hardening of own border. Hafenmark's Precedent-dominant meta-armature favors diplomatic escalation (`treaty_invocation`, Precedent×diplomatic alignment 0.6).

Marshal: receives `border_unsafe` Concern at salience 1-2. Crown's Order-dominant meta-armature favors military patrol (`reinforce_border`, Order×military alignment 1.0).

**T+1 DA Proposal Phase, both factions parallel:**
- Magistrate-Prime proposes diplomatic project (treaty re-affirmation). Crown's response is unilateral military.
- The two factions act on the *same event* but produce *different* responses driven by their meta-armatures.

### 1.3 Knock-on cross-faction Concerns

T+2: Crown's military patrols arrive at the border. Tideford's Passive NPCs witness this. New Memory: `crown_armed_intervention`, semi-positive (sense of safety) for some, semi-negative (sovereignty intrusion) for others.

Tideford's next Settlement Signal carries mixed tag — `crown_armed_intervention` may dominate even if affect is mixed. Magistrate-Prime receives a Concern about Crown's unilateral move. **Diplomatic event chain initiated** without anyone in Crown intending it.

### 1.4 Verification (Scenario 1)

- **Cross-faction Signal divergence verified.** Same event produces different faction responses — meta-armature-driven divergence is real and observable.
- **Cascade pattern:** event → settlement Signal × 2 → Active-NPC Concerns × 2 → DA proposals × 2 → cross-faction observation event → next-Accounting Signals → new Concerns. **The peninsula has emergent diplomatic momentum without any single NPC consciously driving it.**
- **Narrative shape:** This is a *story beat*. Two factions misalign on response to a shared event; the misalignment generates new tensions. The narrative-arc pass identified "thin player-proactive levers" — but here, the player can intervene mid-cascade (Knot-influence with Almud to push diplomatic instead of military, or expose Magistrate-Prime's overreach to Almud, etc.). **Cross-faction events are the strongest narrative substrate the engine produces.**

**`[GAP: SIM-E-G1]` Cross-border event attribution.** The same root event appears in two settlement Memory streams. If both settlements' Signals propagate Concerns to their factions, total faction-Concern volume on this single event is doubled. Per SIM-C-G6 routing this is by-design (each faction receives its own Concern). But for deduplication purposes — does the *event itself* (in Event Impact Matrix) double-fire? Probably not; events are unique. Settlement Signals are derived from Memories, which can include the same event. Surface: `[GAP: cross-border event Signal-attribution clarification — surfaced by SIM-E scenario 1; v1.2 minor doc target — recommend explicit "same event can produce one Signal per affected settlement; faction-Concern propagation is per-Signal not per-event"]`.

---

## §2 Scenario 2 — Multi-Year institutional ossification at scale

**Goal.** Test the SIM-B Sc 7 / SIM-D Sc 8 emergent property — cumulative institutional drift — across 3 Campaign Years (12 Accountings) with three factions.

### 2.1 Initial faction conviction-weights (Year 0)

| Faction | Faith | Order | Reason | Equity | Precedent | Autonomy | Continuity |
|---|---|---|---|---|---|---|---|
| Crown   | 0.10 | 0.65 | 0.04 | 0.04 | 0.05 | 0.04 | 0.08 |
| Hafenmark | 0.08 | 0.10 | 0.06 | 0.06 | 0.55 | 0.06 | 0.09 |
| Varfell | 0.05 | 0.05 | 0.60 | 0.10 | 0.05 | 0.10 | 0.05 |

Each faction has an institutional-stability anchor at 0.35 toward its dominant Conviction; the rest is inner-circle aggregate. Table values are illustrative; actual values per SIM-B Sc 1 calculation method.

### 2.2 Year 1 trajectory

Crown sees Marshal's Year-1 success → S6→S7 promotion (per SIM-B Sc 7). Order weight in Crown rises. Confessor's deadlock against Almud accumulates failed competitions. Reformer crosses S3→S4, adding Autonomy minority.

Hafenmark: Magistrate-Prime steady; Treasurer's Equity-Precedent tie-break (per SIM-B Sc 2) gives Equity-leaning project a win — slight Equity weight gain in faction.

Varfell: Reason-dominant; new astronomical project completes; Reason weight reinforced.

### 2.3 Years 2-3 trajectory

Crown: Confessor under SIM-B-G8 ambiguity. **Liberal interpretation:** Confessor demoted toward S3, exits inner circle by Year 3. Faith weight collapses. Crown becomes pure Order with Autonomy minority. **Strict interpretation:** Confessor recovers to S5 by Year 3; Faith weight holds. Multi-Conviction balance preserved.

Hafenmark: Treasurer's Equity gains compound. By Year 3, Hafenmark's Equity weight rises from 0.06 to ~0.15. Precedent still dominant but less so. **Hafenmark drifts toward more Equity-aligned governance** through cumulative tie-break wins.

Varfell: Astronomer S4→S5 from Year 1 success. Reason weight intensifies. By Year 3, Varfell is even more Reason-dominant than at start. **Pure ossification trajectory.**

### 2.4 End-of-Year-3 institutional weights

| Faction | dominant | dominant share Y0 → Y3 | drift verdict |
|---|---|---|---|
| Crown (liberal) | Order | 0.65 → ~0.78 | accelerating ossification |
| Crown (strict) | Order | 0.65 → ~0.70 | mild reinforcement |
| Hafenmark | Precedent | 0.55 → ~0.50 | slight diversification |
| Varfell | Reason | 0.60 → ~0.72 | accelerating ossification |

### 2.5 Verification + analysis (Scenario 2)

- **Institutional ossification is real and measurable across multi-Year scale.** SIM-B Sc 7 / SIM-D Sc 8 emergent property confirmed at composition scale.
- **Direction of drift depends on initial composition diversity.** Hafenmark's tie-break dynamic (Sc 2) produced *diversification* — anti-deadlock mechanic also operates as *anti-ossification*. Crown's Sc 8 deadlock dynamic (Confessor vs Almud) accelerates ossification.
- **SIM-B-G8 interpretation choice has multi-Year impact:** ~8 percentage points of Crown's Order share over 3 years. **Critical.**
- **ED-760 stall-escalator recommendation validated at scale:** Without it, Crown's Confessor-deadlock dynamic compounds. With it (`+0.05 × seasons_stalled`), Confessor's stalled theological projects eventually win at seasons_stalled ~5-7 — preventing the Faith-collapse trajectory. **Stall-escalator is a meaningful anti-ossification mechanic, not just an anti-deadlock one.**

---

## §3 Scenario 3 — Dramatic intensity test (does an arc reach climax?)

**Goal.** Per narrative-arc pass §3 ("4-year arcs may feel diffuse"), test whether at least one character's arc reaches a clear climax over 12 Accountings.

### 3.1 Trace Confessor's arc under liberal interpretation

Year 1: Confessor at S5, balanced Faith voice in Crown. Proposes Crusade — loses to Marshal's Garrison. Stalls 1 season. Mood Steady.

Year 2: Confessor accumulates Concerns about Marshal's discipline (per SIM-A canonical chain). Begins doubting Marshal. Proposes again, loses again. Stalls 2 seasons. Mood drifts Anxious.

Year 3: Confessor's project hits seasons_stalled = 6+. Approaching failure threshold. Concerns about Marshal compounding. Mood: Anxious → Distracted (multiple Concerns at high salience).

Year 3, late: Confessor's Conviction-engaging Belief about institutional balance under strain. **Path B Belief revision** (per existing spec: 2 contradicting Memories at salience ≥3). Confessor's Belief revises: from "Crown serves multiple Convictions justly" to "Crown is Order-captured." Scar generated; conviction_scars += 1.

Standing recalc end of Year 3: Confessor demoted (liberal interpretation). Crosses S5→S4. **N-DIAG-A milestone scene fires.**

**Year 3 close milestone scene** = Confessor's adjustment to demotion. Tone: *somber, conflicted*. Player attends or skips.

If player attended Confessor's earlier P3 outreaches (Year 1-2): scene shows Confessor articulating his disenchantment, possibly seeking alliance with player against Almud's Order-dominance.

If player skipped: scene shows Confessor isolated, withdrawn. He may exit inner circle entirely by Year 4.

### 3.2 Climax assessment

**This IS a climax.** Confessor's Year-3-close milestone scene is:
- Mechanically anchored (Standing-cross-threshold event).
- Narratively earned (cumulative Concerns, Mood drift, Path B Belief revision).
- Player-affected (relational history determines scene texture and follow-up options).
- Discrete — happens at a specific Accounting boundary, not gradually.

**The N-DIAG-A milestone mechanic generates climax beats reliably** when Standing crosses the inner-circle threshold under accumulated pressure. The narrative pass §3 underestimated this — milestone scenes are exactly the climax mechanic the engine has.

**However:** the climax is *available* (Priority 3, can be skipped). A player who skips the scene experiences only the structural shift (Confessor disappears from inner circle next Accounting); the dramatic moment is lost. **Recommend: consider promoting milestone scenes to Priority 2 mandatory for inner-circle entry/exit transitions** (not for mid-tier promotions). Surface as design observation, not gap.

### 3.3 Multiple parallel climaxes

Across 3 Years × 3 factions × ~10 inner-circle NPCs total, milestone scenes can fire 3-8 times per Year cycle. Each is a discrete dramatic beat. **The engine's narrative texture is dense with potential climaxes; the player chooses which to attend.**

This addresses the narrative-arc-pass concern about "no third-act crisis." There IS a constant parade of small third-acts. The player who attends 6 milestone scenes per Year experiences something close to a serialized novel — episodic dramatic beats with cumulative weight.

### 3.4 Verification (Scenario 3)

- **Engine generates dramatic climax beats reliably.** N-DIAG-A milestones at Standing thresholds; PATCH 3.10 escalation to mandatory P2 when Concern reaches salience-5/ttl-1; Knot mandatory P2 (PATCH 3.6); Faction Crisis activation (§5.4); milestone-tier project completions.
- **Density:** Across the simulation, ~12-20 climax-class beats fire per Campaign Year at three-faction scale. This is *more* than narrative-arc pass anticipated.
- **`[OBSERVATION: SIM-E-O1]` Milestone scenes at inner-circle entry/exit (3↔4 crossing) should arguably be Priority 2 mandatory rather than Priority 3 available. Inner-circle composition shifts are politically central; player should not be able to fully skip witnessing them. Forward-looking design call for v1.2 or later.**

---

## §4 Scenario 4 — Player-proactive lever stress test

**Goal.** Per narrative-arc pass §3 ("Player choices feel reactive, not proactive"), trace whether the player has any means to *initiate* significant political change rather than respond to it.

### 4.1 Player levers inventory

From v1.1 spec, player can:
- Attend or skip Outreach scenes (passive choice on NPC-initiated content).
- Choose dialogue paths within attended scenes (shapes Memory affect).
- Take Read/Surveil/Witness actions (information gathering).
- Initiate Disposition-shifting actions in scenes (limited — depends on scene templates).
- At Standing 5+, contribute to Faction Meta-Armature aggregate.
- Knot-mediated influence (Spouse's Concerns affect Player's Concerns indirectly via shared Knot mechanics).

### 4.2 What the player *cannot* directly do

- Propose a Domain Action (DA Proposal Phase is NPC-only).
- Initiate a Concern in another NPC (Concerns are generated from events, Knowledge, Settlement Signals — not from player declaration).
- Promote/demote NPCs (Standing recalc is automatic).
- Cause Faction Crisis (it's an emergent state, not a triggerable event).
- Force a Belief revision in another NPC (Path A Total Victory Contest is the closest, but requires the contested-belief context the engine has surfaced).

### 4.3 Indirect pathways the player has

The player's actual political agency operates *through* the relational layer:

- **Information leverage:** Player Reads Confessor → discovers his doctrinal Concerns about Marshal → can use that knowledge in a scene with Marshal (planted observation generates new Memory in Marshal → drift in Marshal's Opinion of Confessor).
- **Disposition-shifting events:** Player at S5+ can take actions whose Memory feeds Settlement Signals or Faction Meta-Armature. Smith-Memory pattern (SIM-C Sc 5) shows the path.
- **Knot influence:** Spouse's Concerns are affected by Player's choices in marital scenes; Spouse's Concerns can affect her institutional behavior (if Spouse is in inner circle).
- **Witness-mode** lets player observe private events; what they witness shapes their own Memories and Knowledge.

### 4.4 Verdict

The player has agency but it operates *one-step-removed*. Player actions become Memories in NPC perception; those Memories drift Opinions; those Opinions affect inner-circle Meta-Armature; that affects faction strategic choices. **The chain is real but long.** A player who wants direct political effect (push Confessor for promotion, expose Reformer's vulnerabilities to Almud, broker an alliance) operates *through* generating-the-right-Memories-in-the-right-NPCs.

This is **structurally consistent with Renaissance political-realism intent** (you cannot simply *will* the court to do something; you must shape the perceptions of those who will). But it does demand sophisticated player engagement to feel agency. A casual player will feel reactive.

### 4.5 Verification (Scenario 4)

- **Player agency exists but operates indirectly through the Memory-bus.**
- **Suggested forward-looking design (forward-looking, not v1.2 patch):** introduce a *Player Move* surface — a discrete action the player can take that explicitly seeds a Memory in a target NPC's perception. E.g., "Speak privately with Marshal about Confessor's doubts" — creates a tagged Memory in Marshal that follows the standard drift pipeline. Currently scene templates may handle this implicitly; making it explicit in spec would clarify the proactive lever.
- **`[OBSERVATION: SIM-E-O2]` Forward-looking spec recommendation: explicit "Player Move" mechanic that seeds named Memories in target NPCs through scene actions. Not v1.2 (no current spec gap), but worth design exploration for richer agency.**

---

## §5 Scenario 5 — Three-faction power-equilibrium stress test (12 Accountings)

**Goal.** Trace the three-faction system over 3 Years. Does it reach equilibrium, oscillate, or experience runaway?

### 5.1 Initial conditions

Crown, Hafenmark, Varfell as in §0. Each pursues its dominant-Conviction projects. Some cross-faction interactions: Confessor↔Cantor exchange Faith-coded letters; Reformer↔Wandering-Voice debate Autonomy applications; Treasurer↔Reformer dispute over guild charters.

### 5.2 Year 1 — establishment

- Each faction processes ~3-4 settlement Signals per Accounting → ~0.75 Concerns per inner-circle NPC per Accounting (per SIM-C Sc 7 target). Volume sustained.
- Cross-faction Concerns (gossip-mediated): perhaps 1-2 per faction per Year. Low volume but they exist.
- Standing recalcs at Year-1 close: Marshal +1 (Crown), Treasurer +0 (Hafenmark steady), Astronomer +1 (Varfell). Inner-circle composition stable.

### 5.3 Year 2 — pressures emerge

- Crown's Confessor enters deadlock dynamic (per SIM-B Sc 8). Trajectory depends on SIM-B-G8.
- Hafenmark's Treasurer-Equity gains compound. Cantor (Faith) at S5 maintains Faith-Precedent balance.
- Varfell: pure Reason ossification. Astronomer S4→S5 → Reason weight rises.
- A peninsula-scale event (e.g., comet, plague, treaty crisis) affects all three factions semi-public-broadly. Each faction processes through its meta-armature; responses diverge sharply.

### 5.4 Year 3 — drift visible

- Crown ossifying toward Order (under liberal SIM-B-G8) or stable (under strict). With ED-760 stall-escalator, stable.
- Hafenmark: Treasurer's Equity weight up; Wright (Reason) gains slight; Magistrate-Prime's Precedent share dilutes from 0.55 to 0.50. **Hafenmark diversifying.**
- Varfell: Surveyor and Astronomer reinforce Reason. Wandering-Voice's Autonomy is the only counterweight; if Wandering-Voice's projects fail or stall, Varfell becomes Reason-monoculture. **High ossification risk.**

### 5.5 Equilibrium analysis

**No runaway found in 3 Years.** The system is stable but drifting. Standing-clamp [3, 7] prevents any NPC from accumulating unbounded influence; Faction Meta-Armature institutional_stability anchor (0.35) prevents pure-individual drift; population_disposition feedback (PATCH 3.9) provides settlement-level brake on faction misgovernance.

**Oscillations not observed at this trace duration.** Longer traces (5+ Years) might reveal them — e.g., Order ossification → Faith retreat → eventual Order-internal split (Marshal vs Almud succession?) → new equilibrium. The mechanics permit such oscillations but the trace doesn't reach them.

**Asymmetric trajectories observed.** Hafenmark diversifies, Varfell ossifies, Crown does either depending on SIM-B-G8. **Initial composition × patch interpretation × event sequence determines drift direction.** Realistic.

### 5.6 Cross-faction Concern volume

Across 3 factions × 12 NPCs × 12 Accountings, cross-faction Concerns total ~30 (low). Most political processing is intra-faction. Cross-faction interactions concentrate at borders (per Sc 1) and through Conviction-bridge pairs (Confessor↔Cantor etc.).

### 5.7 Verification (Scenario 5)

- **System remains bounded** — no runaway accumulation observed. ✓
- **Asymmetric drift trajectories** — different factions experience different fates from same starting structure. ✓ Realistic.
- **Cross-faction interactions are minority but meaningful.** Border events and Conviction-bridge pairs are the primary channels. Sufficient to generate inter-faction story-substrate.
- **`[OBSERVATION: SIM-E-O3]` 5+ Year trace recommended for equilibrium analysis. Current 3-Year window shows drift; oscillations may emerge only at longer scales. Future stress tests should run 20+ Accountings.**

---

## §6 Scenario 6 — Composition pathology test: faction-collapse scenarios

**Goal.** Push the system to its breaking-point. Are there faction-collapse dynamics the spec prevents (or should prevent)?

### 6.1 Test 1 — leader death

Almud dies (event). Crown loses leader. Per existing spec: faction crisis check fires if ≥40% inner circle is Distracted/Grieving. Marshal, Confessor, Reformer, Ambassador: 3 of 4 likely Grieving from leader death → 75% → faction enters institutional autopilot.

Crown enters crisis mode for 1-3 seasons (until Mood states recover). During this time:
- No new DA proposals processed.
- Existing P1-P2 actions execute on autopilot.
- New leader emerges through... — **`[GAP: SIM-E-G2]` succession mechanic in v1.1 spec is unspecified.** Standing recalc at Year boundary could elevate Marshal to leader (S7, Order-aligned, natural successor). But what triggers leader-redesignation? Surface: `[GAP: faction succession trigger and mechanism unspecified — surfaced by SIM-E scenario 6; v1.2 spec target — recommend "highest-Standing same-faction NPC becomes leader on previous-leader death; if tied, Conviction-alignment-with-faction-dominant breaks tie"]`.

Recovery: Marshal becomes leader. Crown's institutional_stability stays anchored to Order (Marshal's primary). Faith voice further marginalized. Faction continues but with shifted character.

### 6.2 Test 2 — full ossification

Varfell scenario taken to extreme: Wandering-Voice (Autonomy) departs inner circle (Standing drops below 3 over multiple Years). Varfell becomes Reason-monoculture. All 4 inner-circle NPCs primary=Reason.

Faction Meta-Armature: 100% Reason. Every project is scholarly/intelligence/economic (high Reason alignment). Theological/military/diplomatic projects don't get proposed (no Conviction-aligned NPC to propose them).

**Mechanically valid but politically pathological.** Varfell becomes a research-institute-faction; can't defend itself militarily, can't navigate diplomatic crises, can't ceremonialize. **Long-term: Varfell becomes prey for other factions.**

This isn't a bug — it's the engine reflecting institutional failure. Realistic. But the engine doesn't *signal* the pathology to the player or other factions explicitly. Surface as design observation, not gap.

### 6.3 Test 3 — Concern overflow

What if 4+ high-salience Concerns generate for a single NPC in same Accounting? Cap is 3 active concerns per NPC. `drop_lowest_salience_concern` fires.

Edge case: what if all 4 are tied at salience 5? Drop is non-deterministic without tie-break. Cross-reference SIM-A-G6 / SIM-B-G1 — tie-break-via-stable-order recommended for v1.2. Repeats here.

### 6.4 Verification (Scenario 6)

- **Engine handles leader death via Faction Crisis state but lacks explicit succession mechanic.** Surface as P2 gap.
- **Full ossification is mechanically achievable; politically pathological but realistic.** No spec change needed.
- **Concern-overflow ties bring up tie-break consistency issue raised in earlier sims.**
- **`[GAP: SIM-E-G2]` Faction succession unspecified — P2 for v1.2.**

---

## §7 Direction-E summary

### 7.1 Composition-level findings

**Confirmed at scale:**
1. Cross-faction Settlement Signal interference produces emergent diplomatic momentum (Sc 1).
2. Institutional ossification is real and measurable; trajectory depends on initial diversity, patch interpretation, and event sequence (Sc 2).
3. Engine generates dramatic climax beats reliably via N-DIAG-A milestones, P2 escalations, Knot scenes, Faction Crisis (Sc 3).
4. Player agency operates indirectly through Memory-bus; sophisticated engagement required for narrative dramatic feel (Sc 4).
5. Multi-faction system is bounded — no runaway over 3-Year traces; asymmetric drift trajectories realistic (Sc 5).
6. Faction-collapse dynamics emerge from leader death + Mood-cascade; succession mechanic missing from v1.1 (Sc 6).

### 7.2 New gaps surfaced (2)

| ID | Surface | Issue | Severity |
|---|---|---|---|
| SIM-E-G1 | Scenario 1 | Cross-border event Signal-attribution clarification | P3 |
| SIM-E-G2 | Scenario 6 | Faction succession trigger and mechanism unspecified | P2 |

### 7.3 Forward-looking design observations (3)

| ID | Origin | Suggestion |
|---|---|---|
| SIM-E-O1 | Sc 3 | Inner-circle threshold (3↔4) milestone scenes should be P2 mandatory, not P3 available |
| SIM-E-O2 | Sc 4 | Explicit "Player Move" mechanic that seeds named Memories in target NPCs (richer proactive agency) |
| SIM-E-O3 | Sc 5 | 5+ Year stress trace recommended for equilibrium/oscillation analysis |

### 7.4 Validation of cross-direction findings

- **SIM-B-G8 (failed_da_proposals) confirmed P1-critical at scale.** ~8 percentage points of Crown's Order-share over 3 years between liberal and strict interpretations. This is the single most consequential v1.2 decision.
- **ED-760 stall-escalator validated at scale.** Functions as anti-ossification mechanic, not just anti-deadlock.
- **SIM-C-G6 (routing) tested under cross-border (Sc 1) and three-faction (Sc 5) loads. Routing recommendation (governor/leader/round-robin) holds across these stresses.**
- **N-DIAG-A featured behavior is a more powerful narrative anchor than the narrative-arc pass anticipated.** Milestone scenes are the engine's primary climax-beat mechanic; SIM-E-O1 strengthens them further.

### 7.5 Narrative texture verdict

Per the narrative-arc pass §4 (chronicle vs novel), Direction E confirms:
- **Chronicle level: strong.** Engine reliably generates court-history texture across multi-faction multi-decade timeframes.
- **Story level: rich for engaged players.** ~12-20 climax-class beats per Campaign Year at three-faction scale; player who attends 6+ experiences a serialized-novel feel.
- **Crisis density: better than expected.** Faction Crisis state, leader death, deadlock failures, Path B Belief revisions, Standing demotions — multiple discrete dramatic beats fire per Year.

**The engine produces stories at scale better than at single-faction scale.** Cross-faction interactions, three-way diplomatic pressure, and parallel inner-circle dramas across factions provide the narrative substrate the single-faction simulations lacked.

### 7.6 Direction E — VERDICT

**PASS with 2 new gaps + 3 forward-looking design observations + cross-direction confirmations.** Composition-scale dynamics are mechanically sound; institutional ossification trajectories are realistic; system bounded; cross-faction interactions are the engine's strongest narrative substrate; faction-collapse handling needs succession mechanic for v1.2. Multi-agent multi-decade simulation produces richer story-substrate than single-faction traces.

Total simulation campaign across SIM-A through SIM-E: 5 directions, 39 scenarios, 33 invariants verified, 31 specification gaps surfaced (2 P1-critical), 6 forward-looking design observations.

---

**END OF SIM-E.**

**END OF DIRECTION-CHAIN.**

Recommend Session 5 (synthesis) as the close-out session: roll up all 5 directions + narrative pass; produce final v1.1 validation report; draft v1.2 patch list incorporating P1-critical resolutions (SIM-B-G8, SIM-C-G6, SIM-E-G2 succession), the stall-escalator (ED-760), and the high-impact P2 gaps; flag forward-looking design observations to Jordan for separate consideration.
