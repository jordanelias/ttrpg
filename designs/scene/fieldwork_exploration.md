# VALORIA — FIELDWORK SYSTEM v1.1 — §3 Exploration
## Parent: designs/scene/fieldwork_v30.md
## Status: DESIGN — canonical subsystem file. See parent for full cross-references.
## Mode applicability: TTRPG / Hybrid / Board Game / Godot

## §3 EXPLORATION

### §3.1 Points of Interest (POI)

Each territory contains discoverable Points of Interest categorised by Depth. POIs are the atomic unit of exploration content. A territory's POI list is fixed at game setup (TTRPG: GM prepares; BG: printed on territory cards; Godot: authored in scene data).

**POI Categories:**

| Category | Depth | Examples | Discovery Effect |
|----------|-------|---------|-----------------|
| Landmark | 0 | Cities, major roads, visible ruins, rivers | Navigation aid. Auto-discovered on territory entry. |
| Resource | 1 | Mines, farmland, trade routes, harbours | Territory bonus: Prosperity +1, Muster Ob −1, Trade Ob −1, or equivalent. |
| Secret | 2 | Hidden passages, concealed archives, smuggling routes, abandoned settlements | Tactical advantage: ambush positions, escape routes, intelligence caches. |
| Remnant | 3 | Einhir ruins, Thread scars, Locked Zones, Calamity artifacts | Thread-level content: Thread Debt reduction, TS advancement opportunity, rendering strain (§3.4). |
| Anomaly | 4 | Active Thread phenomena, oscillating zones, rendering failures, Snapped Zone boundaries | Dangerous content: Coherence check on entry, RS effects, possible monstrous emergence (Mode 1 or Mode 2). |
| Breach | 5 | The rendering's edge. Unintelligible ground proximate. | Existential content: rendering strain (§3.4). The character confronts what rendering cannot process. |

**POI per territory:** A territory has between 2 and 6 POIs depending on size and narrative density. Southern territories (high Proximity Rating) have more Remnants and Anomalies. Northern territories have more Resources and Secrets. Askeheim (T15) is entirely Anomaly/Breach territory.

**Conditional POI availability:** Not all POIs are discoverable at all times. POIs may be gated by: RS band (a Remnant becomes visible only when RS drops below 60), season (a Snapped Zone oscillates into accessibility in Winter only), faction control (a Secret accessible only while the controlling faction holds the territory), or prior discovery (discovering POI A reveals the existence of POI B). The GM records conditional gates at setup. In Godot, conditional gates are authored per-POI.

### §3.2 Discovery Procedure

1. **Declare intent.** The character states what they are looking for (a specific type of POI, general survey, or a named objective). The GM determines which POI category is relevant and its Depth.
2. **Check perception gate.** If the character does not meet the perception prerequisite for the POI's Depth, discovery is impossible. The character perceives nothing — the POI is not hidden from them; it is ontologically unavailable to their rendering. Inform the player that nothing further is found at their current capacity. No roll wasted.
3. **Roll.** Pool: (Primary Attribute × 2) + History bonus, TN 7, Ob per Depth table (§1). Attribute selection per §2.1 based on exploration sub-type.
4. **Resolve by degree.**

| Degree | Discovery Quality |
|--------|-------------------|
| Failure | Nothing found. Exposure +1 (time spent draws attention or expends resources). |
| Partial | POI located, but details are unclear. One surface feature visible. Follow-up investigation required for actionable information. |
| Success | POI located with full visible detail. One actionable piece of information gained (a bonus, a route, a clue). |
| Overwhelming | POI located. Full detail. One hidden feature revealed (something below the POI's own depth — a Secret within a Resource, a Remnant within a Secret). +1 Momentum. |

**Multi-character exploration:** When multiple characters explore together, one character leads the Discovery Procedure and rolls. Other characters may assist: each assistant rolls their own fieldwork pool at the same Ob +1. Each assistant who achieves Success or better adds +1 to the leader's net successes (improving degree). Each assistant who fails adds +1 Exposure for the entire party (more people = more conspicuous). Maximum 2 assistants per leader.

### §3.3 Movement and Time

**TTRPG:** Moving between territories takes time. Adjacent territories: 1 scene of travel. Non-adjacent: GM determines route, 1 scene per territory traversed. Travel through Calamity-affected territories (Proximity Rating ≤ 2) at RS ≤ 40: Endurance check Ob 1 per territory or take 1 Exposure.

**Exploration within a territory:** Each exploration action (one Discovery Procedure) consumes approximately one scene of in-game time. A character can make 2–3 exploration actions per season before Exposure accumulates meaningfully.

**Hybrid:** TTRPG timing applies during Personal Phase. Movement between territories during Strategic Phase is handled by BG March/movement rules.

**Board Game:** No personal movement. Territory-level exploration abstracted via Survey action (§8.1).

**Godot:** Movement is real-time or area-transition depending on scale. Each territory is a navigable map region with POI nodes. Discovery triggers when the player-character enters a POI's activation radius, subject to perception gates.

### §3.4 Rendering Strain at Depth 3+

When a character discovers a Remnant (Depth 3), Anomaly (Depth 4), or Breach (Depth 5), the encounter strains their rendering capacity. This is **not** co-movement — co-movement requires a Thread operation per P-01 (Inseparability applies to "manipulations of threads," not to passive perception). Rendering strain is the consequence of consciousness encountering configurations that approach or exceed its processing capacity, as described in the Foundations §4.1 (monstrosity as surfeit of being confronting a finite rendering).

**Rendering strain by Depth:**

| Depth | Rendering Strain Effect |
|-------|------------------------|
| 3 (Remnant) | **Minor strain.** Characters with TS ≥ 10: no mechanical effect (their rendering processes Einhir traces without difficulty). Characters with TS < 10 who are present: vague unease (per observation table, params_threadwork.md). **Certainty pressure:** GM marks the character as having encountered something that challenges their operative framework. Certainty movement (if any) resolves at session end per GM judgment — not automatic. |
| 4 (Anomaly) | **Significant strain.** Coherence check Ob 1 (the character's layer-2 unconscious self-rendering is challenged per P-15). Failure: Coherence −1. **Certainty −1** if Certainty ≥ 3 (the evidence is too direct to resist — active Thread phenomena contradict Solmund orthodoxy structurally). TS ≥ 30 characters perceive the anomaly's Thread configuration; TS < 30 characters perceive distortion without detail. |
| 5 (Breach) | **Severe strain.** Coherence −1 automatic (layer-2 failure threshold — the rendering encounters the boundary of what it can process). **Certainty forced to ≤ 2** (the unintelligible ground is directly proximate). **TS +1** (the character's rendering, forced to operate at its absolute limit, permanently expands its capacity — not from perceiving the unintelligible itself, which remains inaccessible, but from perceiving the boundary). **Warning:** A practitioner at Coherence ≤ 2 who enters a Breach risks Rendering Crisis from the encounter alone (Breach −1 + any subsequent Thread operation −1 = Coherence 0). This is intentional — the Breach is the rendering's edge, and a practitioner near their own rendering's edge should not approach it without preparation or support. |

**Thread-Read is the exception.** When a character performs a Thread-Read action (§4.5), they are in active Thread contact via perceptive Leap. This IS a Thread operation. P-01 fires: three-dimensional co-movement auto-effects apply (temporal, epistemic, actualized). Thread-Read is the only fieldwork action that produces co-movement.

**Non-sensitive characters at Depth 3+:** A non-sensitive character (TS < 10) accompanying a sensitive explorer cannot perceive Thread-adjacent POIs directly. They experience: vague unease (TS 0-9 per observation table, params_threadwork.md). They observe the sensitive character's reaction. Any Thread-level information communicated to them becomes Inert Knowledge (per P-08, stage11 §11.6). Non-sensitive characters have a compensating advantage: they generate **+0 Exposure** from encountering Depth 3+ POIs (the Church does not flag non-sensitive presence near Thread sites, because non-sensitive characters are institutionally invisible as Thread investigators). Sensitive characters present at Depth 3+ POIs generate +1 Exposure from their perceptual engagement.

---

