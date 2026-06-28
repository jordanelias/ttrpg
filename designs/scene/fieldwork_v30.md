<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: fieldwork_v30_infill.md -->

<!-- v30 baseline — renamed from designs/fieldwork/fieldwork_design_v1.md on 2026-04-13 -->
# VALORIA — FIELDWORK SYSTEM v1.1
## Exploration / Investigation / Socializing
## Status: DESIGN — approved for commit. Review corrections: 2026-04-13 (v1.1), PP-628 (canon guard), PP-630 (three-axis Ob, Warden Emergence fix, ED-NEW harvest).
## Mode applicability: ALL (TTRPG baseline; Hybrid bridging; Board Game abstraction; Godot video game)
## Canon compliance: P-01 (inseparability — applied to Thread-Read operations, not passive discovery), P-03 (rendering = consciousness-performed), P-05 (three emergence modes — Mode 1/2 distinction added to §3.1), P-07 (Calamity = rendered-side mechanism), P-08 (epistemological barrier), P-14 (all modes express inseparability), P-15 (three-layer being-persistence)
## Cross-references: params_core.md, social_contest_v30.md, combat_design_v1.md, threadwork_redesign_v25.md, geography_design.md, calamity_radiation.md, clock_registry.md
## Review applied: fieldwork_review.md (2026-04-13). All 11 required corrections + 8 recommended additions incorporated.

---

## CORE PRINCIPLE: INTELLIGIBILITY GRADIENT




The Intelligibility Gradient produces two mechanical consequences:

1. **Perception gates.** What a character can discover at a given depth depends on their Thread Sensitivity (TS), their Certainty, and their Coherence. Two characters standing in the same location inhabit genuinely different experiential worlds — not filtered views of one world.


---

## §1 DEPTH AXIS

All fieldwork operates on a shared **Depth Axis** — a graduated scale from fully-intelligible to epistemically inaccessible. Depth determines base Obstacle (Ob), perception prerequisites, and risk.

| Depth | Name | Content | Perception Gate | Base Ob |
|-------|------|---------|-----------------|---------|
| 0 | Surface | Common knowledge, visible terrain, public spaces, obvious landmarks | None | Auto |
| 1 | Settled | Local knowledge, institutional records, established social networks, territorial resources | Cognition ≥ 2 or local History | 1 |
| 2 | Hidden | Concealed evidence, restricted archives, private relationships, guarded locations | Cognition ≥ 3 or Attunement ≥ 3 | 2 |
| 3 | Buried | Suppressed knowledge, Einhir traces, Thread scars, faction secrets, deep personal truths | TS ≥ 10 (exploration/investigation) or Disposition +3 (social) | 3 |
| 4 | Liminal | Active Thread phenomena, Calamity boundary zones, oscillating configurations, ontological structures | TS ≥ 30 | 5 |
| 5 | Unintelligible | The rendering's edge. What exists here exceeds human rendering capacity. The character does not perceive the unintelligible ground. They perceive their rendering's dissolution — the boundary where consciousness encounters what it cannot process. | TS ≥ 50; Coherence check Ob 2 on encounter | 8 |

**Depth applies to all three fieldwork activities:**
- **Investigation depth** = how far beneath the surface of a question you have dug.

**Ob modifiers (cumulative with base Ob):**
- Hostile faction controls territory or institution: +1 Ob
- Character is foreign to territory (no relevant History): +1 Ob
- Allied faction provides support: −1 Ob
- Character is local resident with relevant History: −1 Ob
- Calamity radiation: +1 Ob per MS band below 60 at current Proximity Rating (see calamity_radiation.md)
- Active Heresy Investigation in territory: +1 Ob to investigation/social actions involving Thread-adjacent topics

Ob floor: 1 (per core engine).

---

## §2 FIELDWORK POOL

**Pool = (Primary Attribute × 2) + History bonus**

Same construction as Contest Pool (social_contest_v30.md §3: Primary Attribute × 2 + History bonus). History bonus = relevant History points + 3 (per params_core.md §4.1 character creation).

**[RESOLVED: ED-NEW-11 — Pool formula ×2 confirmed canonical by PP-615 (params_core.md). The doubled formula (Primary Attribute × 2) is consistent across Combat (PP-615), Contest (PP-234), and Fieldwork. Ob calibration is correct as-is.]**

TN: 7 (Standard). TN 6 (Controlled) when unhurried with preparation. TN 8 (Desperate) under duress, exhaustion, or active Calamity exposure.

**History selection:** One History per action, selected by the player, confirmed by GM. The History must be narratively defensible for the specific action (a History of "Einhir Architecture" applies to Examine at a Remnant; it does not apply to Rumour in a tavern). If no History is relevant: pool = (Primary Attribute × 2) + 3 (the base constant without History points).

### §2.2 Core Engine Integration

**Degree table:** Fieldwork uses the core engine degree table (params_core.md). Overwhelming requires net ≥ 2×Ob AND net ≥ 3 (PP-232/PP-249). At Ob 1, Overwhelming requires net ≥ 3 (not net ≥ 2).


**Wounds:** Physical wounds (−1D per wound, cumulative) apply to fieldwork rolls that require physical exertion: Endurance-based exploration, Surveil. Social and cognitive fieldwork (Examine, Interview, Research, Read, Converse, Connect, Impress, Negotiate, Rumour, Reconstruct) is unaffected by physical wounds. Rattled marks (from Contest, per social_contest_v30.md §4 Step 6) apply +1 Ob per mark to social fieldwork actions for the remainder of the scene.

**Inspiration spend:** Before rolling any fieldwork action, a character may spend 1 Inspiration to reduce the Ob by 1 (minimum 1). This follows the same pattern as Inspiration spend for scope shift (stage11 §11.4). A character pursuing their Beliefs through fieldwork can leverage emotional conviction to press through resistance.

**Perception gates:** Gates based on TS are hard — they represent the epistemological barrier (P-08), which is metaphysical, not skill-based. A character below the TS gate cannot perceive what lies at that depth; no amount of effort or penalty will change this. Gates based on attributes (Cognition ≥ 2 for Depth 1, Cognition ≥ 3 for Depth 2) are also hard — they represent the minimum cognitive capacity to process the information. Characters below the gate cannot attempt the action. This is not a Beginner's Luck situation; the gate is about capacity, not training.

### §2.1 Primary Attribute by Activity

| Activity | Sub-type | Primary Attribute | Reasoning |
|----------|----------|-------------------|-----------|
| Exploration | Terrain / navigation | Cognition | Structural analysis, pathfinding, cartography |
| Exploration | Thread-aware | Attunement | Sensing Thread phenomena, reading the substrate |
| Exploration | Endurance-based | Endurance | Forced marches, exposure, harsh terrain |
| Investigation | Physical evidence | Cognition | Examining objects, documents, architecture, forensics |
| Investigation | Witness / informant | Attunement | Reading people, sensing deception, calibrating trust |
| Investigation | Lore / research | Recall | Archives, oral histories, institutional records, precedent |
| Investigation | Thread-Read | Spirit | Perceiving Thread-level configurations via perceptive Leap (§4.5). Pool: (Spirit × 2) + History + TPS (PP-619, PP-626). TS ≥ 30 required. |
| Socializing | Read | Attunement | Determining NPC's true state, hidden motivation |
| Socializing | Impress | Charisma | Making a favourable impression, projecting authority |
| Socializing | Connect | Bonds | Building genuine trust, deepening a relationship |
| Socializing | Rumour | Charisma | Gathering unverified intelligence through social networks |
| Socializing | Negotiate | Attunement | Reaching informal agreement (below Contest threshold — see §5.7) |

### §2.3 System Transition Rules


**Fieldwork → Combat:** When hostile contact interrupts fieldwork, the current fieldwork action resolves (degree applied, Evidence/Exposure updated). Combat then begins per combat_design_v1.md §3 (initiative by Attunement). If the character was at Exposure ≥ Noticed when interrupted, the interrupting hostile party gains +1D on their first exchange Offence (positional awareness from the character's conspicuousness). Evidence gathered before the interruption is retained regardless of combat outcome.

**Fieldwork → Contest (Escalation):** Per §5.7. Current Disposition maps to Piety Track offset (±1 per 2 Disposition, cap ±2). Evidence from fieldwork may be cited in the Contest for +2D Recall bonus (per social_contest_v30.md §4 Step 3). Evidence cited in a Contest is not consumed — the Evidence Track and its contents persist. The investigation continues after the Contest.

**Fieldwork → Mass Battle (Suspension):** Mass battle suspends all active fieldwork. Evidence Tracks freeze at their current value. Battle actions (including Thread operations in Phase 4) do not consume fieldwork time units. Thread-Read during mass battle: resolves in Phase 4 window, classified as intelligence (not offensive). Co-movement fires. May advance an Evidence Track if the Thread-Read targets an investigation question. Fieldwork resumes after the battle at its frozen state.

**Combat → Fieldwork:** Combat ends; fieldwork resumes as a new scene. Wounds persist (−1D to physical fieldwork per wound, per §2.2). Combat generates Exposure in the current territory: +1 for a quiet fight (subdued, no witnesses), +2 for a conspicuous fight (noise, damage, witnesses), +3 for a public battle (multiple combatants, civilian observers).

**Contest → Fieldwork:** Contest ends; fieldwork resumes. Information gained through a Contest Appraise action (social_contest_v30.md §4 Step 1) may be applied to an active Evidence Track as +1 progress (Partial quality, Testimonial tag). This is automatic — no additional fieldwork action required. Post-Contest Disposition update: adjudicator's Disposition shifts +1 toward the Contest winner, −1 toward the loser.


**Combined Findings in Contest:** Multiple resolved Findings on related topics may be presented as a combined argument. The combined argument uses the strongest constituent reliability tag. Each additional Finding beyond the first adds +1D to the Argue roll (max +2D from combined Findings).

### §2.4 Threadwork During Fieldwork

**Every Thread operation may advance investigation.** Per the Foundations §1, threads constitute all that is experienceable. There is no configuration excluded from Thread operations, and no Thread operation that cannot produce investigatively relevant consequences. The Evidence Track advances when an operation's consequences reveal something relevant to an active investigation, regardless of operation type. The GM determines whether the consequences yield investigation-relevant information.

**Thread Operation Investigative Yield:**

| Operation | Primary Effect | Investigative Yield | Typical Evidence Progress |
|-----------|---------------|--------------------|--------------------|
| Thread-Read | Perception of Thread configuration | Direct: the practitioner perceives what is there | +2 (Success), +3 (Overwhelming) |
| Weaving | Cohering a configuration | Co-movement may reveal adjacent structures; stabilised configs are easier to examine | +1 if co-movement reveals (GM) |
| Pulling (standard) | Opening a configuration | The pulled state reveals what was hidden, frozen, or compressed | +2 (Success), +3 (Overwhelming) |
| Past-Oriented Pulling | Displacing temporal config | The displaced past reveals what was overwritten; orphaned config is evidence | +2 (Success), +3 (Overwhelming) |
| Locking | Freezing a configuration | Preserves evidence against tampering; resistance to Lock reveals internal structure | +1 (preservation); +2 if resistance reveals structure |
| Dissolution | Destroying a configuration | Gap topology IS forensic evidence; concealment destroyed reveals hidden content; Weaver's Thread signature readable from Gap | +2 if concealment destroyed; +1 from Gap topology |
| Mending | Repairing substrate damage | Repairing a Gap reveals original configuration; Mending a Locked boundary opens access | +1 (reveals original); +2 if opens access |
| Collective | Pooled operation (any type) | Same as base type at achieved scale | Same as base type |


**Forensic applications:**

- **Dissolution forensics:** A fresh Gap's topology reflects the structure of what was dissolved. Thread-Read of the Gap (same scene, Ob 3) reveals the original configuration. Additionally, a Woven concealment dissolved by Dissolution reveals both the hidden content AND the concealer's Thread signature — triple evidence (what was hidden, who hid it, when).
- **POP forensics:** The paradox window (PP-193) produces simultaneous perception of past and present states — the practitioner sees what changed and how. The paradox window is the investigation's most powerful perceptual moment.

**Scale, distance, and breadth:**

- **Scale** (stage11 §11.1): Higher scale = broader investigative reach, higher Ob, higher Coherence/MS cost. Territorial Thread-Read perceives an entire settlement's substrate (TS 50+, Coherence −1).
- **Temporal reach (POP only):** Accesses past configurations. Same-session (Ob 3) is the viable investigative range. Generational (Ob 7+) is near-impossible (<0.1% success).



**Wounds and Thread operations:** Physical wounds do not apply −1D to Thread operation pools (Thread operations are consciousness-performed per P-03). Instead, wounds apply +1 Ob to Thread operations requiring Leap — pain disrupts concentration needed to sustain contact.


### §2.5 Domain Echo from Investigation


**Faction-level scope definition:** A Finding has faction-level scope when: (a) it resolves a Structural investigation (threshold 8) on any topic; (b) it resolves a Complex investigation (threshold 5) whose subject directly concerns a named faction's actions, plans, or institutional secrets; or (c) it contains Documentary or Verified evidence implicating a faction's institutional acts — not merely a faction member's personal conduct. A Simple investigation (threshold 3) about a personal matter does not fire Domain Echo unless the subject is a faction officer acting in their institutional capacity.

**Domain Echo timing:** Domain Echo fires at the end of the scene in which the Evidence Track threshold is reached — not mid-scene. At Board Game or Accounting scale, a Domain Echo from a TTRPG investigation fires at the next Accounting if the threshold is reached between Accounting events. Hybrid mode: fires at end of Personal Phase if threshold is reached during Personal Phase; at next Accounting if threshold is reached during Strategic Phase resolution. Domain Echo from investigation is subject to the seasonal faction-attribute cap of ±2 per **season** (stage11 §11.5). *(FW-01 clarification: this seasonal cap applies to investigation-sourced Domain Echoes specifically. Personal-scene Domain Echoes — social contest wins, combat wins per scale_transitions §8 — are subject to the per-scene ±2 cap from scale_transitions and accumulate independently. Investigation and personal-scene Echoes do not share a cap.)*

**NPC learning mechanism:** An NPC learns they were investigated when: (a) the investigator's Exposure reaches Watched threshold in the NPC's territory — the dominant faction's surveillance makes the investigator's activities and target known; (b) a failed investigation action targeting this NPC produced a hostile witness (NPC Disposition ≤ 0 at the time of the failed action — the NPC noted the approach and may report it); or (c) a Finding is publicly cited in a Contest, Domain Action, or formal proceeding in which the NPC or their faction's representatives are present. Covert investigation that stays below Watched threshold and produces no public citation does not trigger the Disposition shift unless a specific Surveil or contested investigation by the NPC uncovers it.


### §2.6 Knot-Mediated Remote Investigation

A practitioner Knotted to an NPC may Thread-Read that NPC's Thread configuration remotely through the Knot connection, without physical presence. The Knot IS the connection — distance does not add Ob.

**Pool:** Standard Thread-Read pool. **TN:** 7. **Ob:** Personal scale (Ob 2).
**Cost per use:** +1 Knot strain. The relational thread bears force from being used as an intelligence channel. The Knotted party may detect the intrusion: Spirit check TN 7, Ob = practitioner's Cognition ÷ 2 (round down, min 1). If the Knotted party detects: Disposition −3 (betrayal of relational trust). The Knot itself does not break — Knots are constitutive, not contractual — but the relationship may be destroyed.

**Evidence yield:** Thread-verified. Inert Knowledge for non-sensitives. Advances Evidence Track normally.

### §2.7 Non-Sensitive Partners and Dissonance


**Failure:** Spirit −1D for remainder of scene. Multiple failures in a season compound — each failure makes subsequent checks harder. Non-sensitive partners degrade over sustained Thread exposure. Recovery: penalty clears at scene end. No permanent damage.


### §2.8 Threadcut Being Social Fieldwork



**Counter-investigation:** A threadcut being perceives Thread-Reads directed at it (it is always in the originary state). It may respond with its own Thread operations: concealing its configuration, Pulling the investigator's memory, or Weaving misdirection. Contested investigation (§4.6) applies. The Evidence Track is player-level knowledge — if the being Pulls the investigator's memory of a prior Thread-Read, the Evidence Track does not reverse (the knowledge persists in notes, allies, and physical records). The character loses conscious access; the investigation's accumulated state persists.

**Knot formation with a threadcut being:** A threadcut being at Disposition +5 becomes a Knot candidate only if the practitioner has TS ≥ 30. The threadcut being is already performing continuous Thread work to maintain its existence — Knotting adds relational load to that self-maintenance. Each Knot use (for remote intelligence per §2.6, for relational co-movement per P-12, or for shared Composure per §5.6) costs the being +1 self-maintenance strain (separate from the +1 Knot strain the practitioner accrues). GM tracks cumulative strain: at strain 5, the being's rendering shows visible instability — facial consistency fails, temporal micro-slippages increase, the originary state bleeds through the maintained rendering. Strain reduces by 1 per season of Knot non-use. This cost does not apply to Knots with organic beings (whose self-rendering is unconscious and not burdened by relational knotting).

---

## §3 EXPLORATION

### §3.1 Points of Interest (POI)

**Settlement anchoring (Throughline T3):** POIs are now assigned per settlement, not per province. Each settlement has 2–4 POIs across Depth levels. POI templates by settlement type and named narrative-critical POIs are defined in settlement_layer_v30 §4.6 and throughline_specifications §T3.3.


**POI Categories:**

| Category | Depth | Examples | Discovery Effect |
|----------|-------|---------|-----------------|
| Landmark | 0 | Cities, major roads, visible ruins, rivers | Navigation aid. Auto-discovered on territory entry. |
| Resource | 1 | Mines, farmland, trade routes, harbours | Territory bonus: Prosperity +1, Muster Ob −1, Trade Ob −1, or equivalent. |
| Secret | 2 | Hidden passages, concealed archives, smuggling routes, abandoned settlements | Tactical advantage: ambush positions, escape routes, intelligence caches. |
| Remnant | 3 | Einhir ruins, Thread scars, Locked Zones, Calamity artifacts | Thread-level content: Thread Debt reduction, TS advancement opportunity, rendering strain (§3.4). |
| Anomaly | 4 | Active Thread phenomena, oscillating zones, rendering failures, Snapped Zone boundaries | Dangerous content: Coherence check on entry, MS effects, monstrous emergence possible. **Mode 1 (Ordinary Incursion):** configuration has no self-awareness and deteriorates across scenes — investigation is time-sensitive; Evidence Track progress from this source halves after the third scene past initial contact as the configuration degrades. **Mode 2 (Providence):** a temporary organized event, not an entity — Interview and social fieldwork actions are unavailable (there is no being to address); investigation accesses the event's Thread configuration via Examine and Thread-Read only. Evidence tag: Observational (Mode 1), Thread-verified (Mode 2). Per P-05: modes are mechanically distinct and require distinct investigation procedures. (PP-628) |
| Breach | 5 | The rendering's edge. Unintelligible ground proximate. | Existential content: rendering strain (§3.4). The character confronts what rendering cannot process. **Threadcut emergence sites:** if a Breach is the confirmed entry point of a known threadcut being (Mode 3), Thread-Read of the site reveals the being's entry configuration — the tear's topology is a forensic record of the being's first moment of active self-maintenance. Evidence yield: +3 regardless of roll degree (Thread-verified tag). The being may detect this investigation (§2.8 counter-investigation applies). |


#### §3.3a Einhir Site World Map Detectability (ED-676, PP-042)

Einhir sites (Remnants, Anomalies, Breaches) render on the world map according to the following TS-gated visibility rules:

| Site type | TS 0–9 | TS 10–29 | TS 30–49 | TS 50+ |
|---|---|---|---|---|
| Remnant (Depth 3) | Invisible. Terrain shows as normal landscape. | Marked as "unusual terrain" — no Thread label. Player sees a question mark icon. | Visible as "Einhir Remnant" with approximate boundary. Examine available. | Full visibility. Thread scar topology visible. Thread-Read available from map. |
| Anomaly (Depth 4) | Invisible. | Invisible. Vague unease in territory description (text-only flavor). | Marked as "disturbance" — general area only, no precise location. Must Examine to locate precisely. | Visible as "Active Anomaly" with precise location and Mode classification (1 or 2). |
| Breach (Depth 5) | Invisible. | Invisible. | Invisible. Territory description mentions rendering strain. | Marked as "Breach Zone" — visible but entering triggers Coherence check (per Depth 5 rules). |

**After Diagnosis:** Once a character with sufficient TS has performed a successful Diagnosis operation (threadwork_v30 §2) on a site, the site becomes permanently visible on the world map at its full detail level for all characters. The practitioner's Diagnosis renders the site intelligible — the information propagates through the party's shared knowledge base.

**Engine implementation:** Site visibility is per-character, calculated from character TS at map render time. Diagnosed sites flag as  and render at max detail for all characters. Sites generate procedurally from territory MS history (low MS = more Remnants/Anomalies; MS ≤ 30 may spawn Breaches).


**Conditional POI availability:** Not all POIs are discoverable at all times. POIs may be gated by: MS band (a Remnant becomes visible only when MS drops below 60), season (a Snapped Zone oscillates into accessibility in Winter only), faction control (a Secret accessible only while the controlling faction holds the territory), or prior discovery (discovering POI A reveals the existence of POI B). The GM records conditional gates at setup. In Godot, conditional gates are authored per-POI.

### §3.2 Discovery Procedure

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

**TTRPG:** Moving between territories takes time. Adjacent territories: 1 scene of travel. Non-adjacent: GM determines route, 1 scene per territory traversed. Travel through Calamity-affected territories (Proximity Rating ≤ 2) at MS ≤ 40: Endurance check Ob 1 per territory or take 1 Exposure.





### §3.4 Rendering Strain at Depth 3+


**Rendering strain by Depth:**

| Depth | Rendering Strain Effect |
|-------|------------------------|
| 3 (Remnant) | **Minor strain.** Characters with TS ≥ 10: no mechanical effect (their rendering processes Einhir traces without difficulty). Characters with TS < 10 who are present: vague unease (per observation table, params_threadwork.md). **Certainty pressure:** GM marks the character as having encountered something that challenges their operative framework. Certainty movement (if any) resolves at session end per GM judgment — not automatic. |
| 4 (Anomaly) | **Significant strain.** Coherence check Ob 1 (the character's layer-2 unconscious self-rendering is challenged per P-15). Failure: Coherence −1. **Certainty −1** if Certainty ≥ 3 (the evidence is too direct to resist — active Thread phenomena contradict Solmund orthodoxy structurally). TS ≥ 30 characters perceive the anomaly's Thread configuration; TS < 30 characters perceive distortion without detail. |
| 5 (Breach) | **Severe strain.** Coherence −1 automatic (layer-2 failure threshold — the rendering encounters the boundary of what it can process). **Certainty forced to ≤ 2** (the unintelligible ground is directly proximate). **TS +1** (the character's rendering, forced to operate at its absolute limit, permanently expands its capacity — not from perceiving the unintelligible itself, which remains inaccessible, but from perceiving the boundary). **Warning:** A practitioner at Coherence ≤ 2 who enters a Breach risks Rendering Crisis from the encounter alone (Breach −1 + any subsequent Thread operation −1 = Coherence 0). This is intentional — the Breach is the rendering's edge, and a practitioner near their own rendering's edge should not approach it without preparation or support. |



---

## §4 INVESTIGATION

### §4.1 Evidence Track

Investigation is a structured process of assembling knowledge. Each investigation has an **Evidence Track** — a progress clock that fills as the investigator gathers pieces.

**Evidence Track range:** 0 to threshold.

| Investigation scope | Threshold | Examples |
|-------------------|-----------|---------|
| Simple question | 3 | "Who stole the seal?" "Where is the hidden passage?" |
| Complex question | 5 | "What is the Church hiding in Himmelenger?" "What happened at the Einhir site?" |
| Structural question | 8 | "How does the Calamity mechanism work?" "What is the Restoration's true plan?" |

The GM sets the threshold at investigation opening. The threshold is not known to the player (unless the investigation is institutional — Church Heresy Investigations have published procedure lengths per social_contest_v30.md §7).

**Evidence Track progress is persistent across scenes and sessions.** An investigation begun in one session can be continued in the next. Evidence does not decay (knowledge, once assembled, remains assembled). However, the world may change around the evidence — a witness may be killed, a document may be destroyed, a site may be altered by Thread operations.

**One track per investigation, regardless of territory.** An investigation into "What is the Restoration's true plan?" might require evidence from T6, T13, and T15. The Evidence Track is unified — progress from any territory contributes to the same track. Exposure, however, is tracked per territory. Investigating in T6 then moving to T13 accumulates Exposure independently in each.

**Depth-limited resolution:** When the Evidence Track reaches its threshold, the investigation does not automatically resolve. The player must perform a **Reconstruct** action (§4.2) to synthesize the accumulated evidence into a conclusion. This is the investigation's climactic moment — the Case of the Golden Idol synthesis, the detective's deduction board.

**Reconstruct as completion:** When Evidence Track ≥ threshold, Reconstruct Ob = 1 (the evidence is sufficient; synthesis is achievable). The Reconstruct degree determines conclusion quality:

| Degree | Conclusion Quality |
|--------|-------------------|
| Failure | Evidence assembled but conclusion is wrong. The player receives a plausible but incorrect interpretation. GM does not reveal the error — the player acts on a false conclusion until contradicted by subsequent evidence or events. Investigation may be reopened. |
| Partial | Correct conclusion but missing context. The "what" is right but the "why" or "who" is incomplete. One follow-up Reconstruct at Ob 1 may fill the gap (requires no additional evidence). |
| Success | Full picture. The player understands what happened, why, and who was involved. Investigation produces a Finding (see §4.3 for reliability tags). |
| Overwhelming | Full picture plus one implication the evidence does not explicitly state — a consequence, a connection, a hidden actor. +1 Momentum. Finding produced at highest reliability tag among constituent evidence. |

If the Evidence Track reaches threshold but the player does not Reconstruct, the evidence persists but no conclusion is drawn. The investigation remains open. The world may change around the evidence (witnesses killed, documents destroyed), but the Evidence Track value does not decrease.

If the answer lies at Depth 4 but the investigator conducted only Depth 1-3 actions, the Reconstruct produces a partial answer — everything the evidence supports up to the depth accessed. "You have assembled a complete picture of everything that is available at your level of perception. There is more, but it is beyond your current reach." Investigation can be reopened at greater depth if the character later acquires the perception prerequisites.


### §4.2 Investigation Actions


| Action | Primary Attribute | What it does | Depth access |
|--------|-------------------|-------------|-------------|
| Examine | Cognition | Study physical evidence, architecture, documents, objects | Up to Hidden (2); Buried (3) if TS ≥ 10 |
| Interview | Attunement | Question a witness, informant, or subject | Up to Hidden (2); Buried (3) at Disposition +3 |
| Research | Recall | Consult archives, oral histories, institutional records, Einhir documents | Up to Hidden (2); Buried (3) at institutional access |
| Surveil | Cognition | Observe a location, person, or faction operation over extended time | Up to Hidden (2). +2 Exposure (conspicuous activity). |
| Thread-Read | Spirit | Perceive Thread-level configurations via perceptive Leap (§4.5). Pool: (Spirit × 2) + History + TPS (PP-619, PP-626). | Depth 3–5. TS ≥ 30 required. Co-movement fires (P-01). +1 Exposure. |
| Reconstruct | Recall | Assemble existing evidence into a coherent picture. No new information gathered — this action synthesises. | Any depth already reached. Ob = (threshold − current progress), min 1. On success: reveals what the assembled evidence implies. |

**Evidence progress by degree:**

| Degree | Progress | Exposure | Additional |
|--------|----------|----------|------------|
| Failure | +0 | +2 | GM may offer a misleading clue (false lead). The investigator does not know whether the clue is genuine. |
| Partial | +1 | +1 | One incomplete detail. Enough to know something is there; not enough to know what. |
| Success | +2 | +0 | One reliable detail. Actionable information. |
| Overwhelming | +3 | −1 (elegant work) | Reliable detail + one bonus revelation from an adjacent line of inquiry. +1 Momentum. |

### §4.3 Evidence Quality and the Epistemological Barrier

Evidence gathered through fieldwork has a **reliability tag:**

| Source | Tag | Can be used as... |
|--------|-----|-------------------|
| Examine (physical) | Verified | Court evidence, Contest corroboration, Domain Action justification |
| Interview (witness) | Testimonial | Contest argument (Memory genre); −1 reliability if witness hostile to presenter |
| Research (archival) | Documentary | Court evidence, Contest corroboration (+2D Recall bonus per Contest §4 Step 3) |
| Surveil | Observational | Intelligence (faction action), Contest argument; Exposure cost makes it expensive |
| Thread-Read | Thread-verified | Actionable only by TS ≥ 30 characters. Inert Knowledge for non-sensitives. Cannot be presented in Church Tribunal as evidence (heretical methodology — this is an institutional restriction, not an epistemic one; the evidence is real but the Church rejects Thread-based methodology). |
| Rumour (social) | Unverified | Not admissible. Directional only — suggests where to investigate, not what happened. |
| Reconstruct | Derived | As strong as weakest constituent evidence. Cannot exceed source reliability. |

**The epistemological barrier (P-08) governs evidence transmission:**
Thread-verified evidence cannot transfer its full epistemic content to non-sensitive receivers. A sensitive investigator who perceives a Thread scar's configuration can *describe* it to a non-sensitive colleague, but the colleague receives Inert Knowledge — they can recite the description but cannot act on it with Thread-level precision. In mechanical terms: Thread-verified evidence contributes to the Evidence Track for non-sensitive investigators at half value (round down, minimum 0).


### §4.4 Desperate Trail (Fail Forward)

Trails never go cold — they become more dangerous. After 3 consecutive failed investigation actions (net successes ≤ 0) targeting the same investigation, the investigation enters **Desperate Trail** state. The Evidence Track remains open, but conditions escalate:

- **TN shifts to 8** (Desperate) for all subsequent actions on this investigation. The easy approaches are exhausted; what remains demands risk.

Desperate Trail clears when: (a) any single action produces a Success or Overwhelming result (the breakthrough resets conditions — TN returns to 7, Exposure normalises); or (b) the season changes (new circumstances, new access, fresh start).



### §4.5 Thread-Read as Perceptive Leap


**Procedure:**
3. **Perception.** Roll (Spirit × 2) + History bonus + Thread Pool Score (TPS = TS ÷ 10, round down), TN 7, Ob per Depth. (PP-619, PP-626: Thread-Read is a Leap; all Leaps use (Spirit × 2) + History + TPS per PP-619. Attunement struck from Thread contact pools.)

4. **Co-movement fires (P-01).** Thread-Read is a genuine Thread operation. Three-dimensional auto-effects apply per threadwork_redesign_v25.md §3.2: temporal auto-effect (Calamity Drift + History Resonance), epistemic auto-effect (Certainty modifier, investigation/testimony consequences), actualized auto-effect (d6 consequence table).
5. **Coherence cost.** Per scale table (stage11 §11.1): Object/Personal scale = 0 auto-cost; Relational+ scale = −1 Coherence.
6. **Evidence progress.** Apply degree result per §4.2 table.


### §4.6 Contested Investigation


**Concealment Pool:** The concealing party rolls (Cognition × 2) + relevant History, TN 7. Their net successes set a **Concealment Ob** that the investigator must exceed in addition to the base Ob.

This resolves per action, not per investigation. Each investigation action faces: base Ob (from Depth) + Concealment Ob (from opponent's concealment roll for that scene). The concealing party must actively maintain concealment — each scene they are not present to conceal, the Concealment Ob is 0.

**Church Heresy Investigation** is a specific institutional form of contested investigation. The Church's Concealment Ob equivalent is its investigatory bonus (+1D Investigate, +2 Ob for targets in Church territory with Inquisitor). See social_contest_v30.md §7 and params_board_game.md §Church Attention Pool for the BG-scale version.

---

## §5 SOCIALIZING

### §5.1 Disposition Track


<!-- [EDITORIAL: ED-912/ED-841 — Jordan ruling 2026-06-23 (revised 2026-06-28): Disposition range = −5..+5 (flat; NOT Bonds-capped). Supersedes PP-632 redesign + PP-684 "ceiling = Bonds". Knot model = strain (ED-773, Option A), reframed as a bidirectional −5..+5 bond-strain gauge (§5.6b). Bonds ≥ 5 retained as an EXPLICIT Knot prerequisite (§5.6a), no longer derived from a ceiling. Stepped Ob table (below) replaces the params direct-subtraction rule. -->
**Disposition range: −5 to +5.** Flat per NPC per PC — the same fixed swing for every character; no Bonds ceiling. Asymmetric: A's Disposition toward B is independent of B's toward A. Relationship *depth* gating (companion eligibility, Knot formation) is expressed by explicit prerequisites (§5.6), not by a Bonds-derived cap.

| Value | Label | Effect on Social Ob | Information Gate |
|-------|-------|---------------------|-----------------|
| −5 | Hateful | +5 Ob | Active enmity. Will harm the character given opportunity. |
| −4 | Hostile | +4 Ob | Refuses interaction. Violence possible. |
| −3 | Antagonistic | +3 Ob | Openly uncooperative. Obstructs. |
| −2 | Suspicious | +2 Ob | Minimal cooperation. Monosyllabic. |
| −1 | Wary | +1 Ob | Guarded responses. Surface information only. |
| 0 | Neutral | +0 Ob | Standard interaction. Surface information. |
| +1 | Warm | −1 Ob | Willing to engage. Settled information accessible. |
| +2 | Friendly | −1 Ob | Volunteers information. Hidden information accessible. |
| +3 | Trusting | −2 Ob | Shares private knowledge. Buried information accessible. |
| +4 | Devoted | −2 Ob | Takes personal risk for the character. Liminal information accessible. |
| +5 | Bonded | −3 Ob | Knot candidate. Deepest personal access. |

**Starting Disposition** is determined by faction alignment, social context, and NPC personality:
- Same faction: +1
- Allied faction: 0
- Neutral faction: 0 or −1
- Rival faction: −1 or −2
- Hostile faction: −2 or −3
- Personal factors (Beliefs, shared History, prior interaction): ±1 per factor (GM discretion)
- Reputation (per core engine): Reputation 3+ in character's favour: +1 starting Disposition


### §5.2 Social Actions (Non-Contest)

Social actions outside formal contests use the fieldwork pool. These are individual rolls, not the exchange structure of social_contest_v30.md. A social action represents one meaningful interaction within a scene.


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



### §5.3 Sincerity Gate


**Sincerity Check:** Spirit, TN 7, Ob 1.

| Degree | Effect |
|--------|--------|
| Failure | The NPC senses the instrumentality. Disposition does not increase; may decrease by −1. "Something about the way you ask..." |
| Partial | The NPC does not notice, but the character feels the dissonance. No Momentum from this interaction, even if Belief-aligned. |
| Success | The character manages genuine engagement despite instrumental intent. Normal result. |
| Overwhelming | The attempt at instrumentality dissolves — the character discovers genuine interest. Normal result + mark potential Belief revision. |


### §5.4 Information Gates

The Depth axis and the Disposition axis are parallel information-access systems:

| Access Method | Depth 0 (Surface) | Depth 1 (Settled) | Depth 2 (Hidden) | Depth 3 (Buried) | Depth 4 (Liminal) |
|--------------|-------|--------|--------|--------|---------|
| Exploration | Auto | Cognition ≥ 2 | Cognition ≥ 3 | TS ≥ 10 | TS ≥ 30 |
| Investigation | Auto | Ob 1 | Ob 2 | Ob 3 + TS ≥ 10 | Ob 5 + TS ≥ 30 |
| Socializing | Any Disposition | Disposition +1 | Disposition +2 | Disposition +3 | Disposition +4 |

A character can access the same information through different routes. The NPC who won't share a Buried secret (requires Disposition +3) might be bypassed entirely by a sensitive investigator who Thread-Reads the relevant site (TS ≥ 30, Ob 3). But Thread-Read carries co-movement costs and Exposure that talking to the NPC does not. There is always a trade-off between access methods.

### §5.5 Socializing and Beliefs


- **Belief-aligned social success:** +1 Momentum (if below cap 4). Counts as Belief achievement per core engine.
- **Belief-challenging social success:** No Momentum, but the success creates narrative pressure to re-examine the Belief. GM marks as potential Belief revision opportunity.

### §5.6 Knot Integration


**Non-sensitive characters at Disposition +5 (Bonded):** If neither the PC nor the NPC has TS ≥ 30, Knot formation is impossible — Knots require Thread contact. The relationship is as deep as it can be without Thread linkage. Mechanically: no decay, +1D on social actions (these benefits apply at Disposition +5 regardless of Knot status). Relational contagion (P-12) does not apply without a Knot.

Knot-linked characters gain:
- Automatic Disposition maintenance (no decay)
- +1D on all social actions with the Knot partner
- Shared Composure buffer (per social_contest_v30.md §4 Step 6)
- Relational contagion risk (P-12): Thread-shift propagates through Knots


### §5.6a Knot Formation Procedure (AUD-NPC-01 resolution; ED-780 prerequisite clarification)

**Prerequisites (all required):**
1. Disposition +5 (Bonded) with the target NPC
2. Either PC or NPC has TS ≥ 30 (Thread contact — per A12, Knots bind threads; substrate must be accessible)
3. PC's current Knot count < floor(Bonds/2)+1 (per params_core §Bonds max Knot count)
4. No existing Knot with this NPC
5. **PC Bonds ≥ 5** (EXPLICIT prerequisite per ED-912 ruling 2026-06-23: Disposition is now a flat −5..+5 with no Bonds ceiling, so this gate is stated directly rather than derived. ED-780's intent — Knots demand deep relational capacity — is preserved as a standalone gate.)

**Bonds prerequisite rationale (ED-780, restated under the flat −5..+5 range):** Reaching the +5 (Bonded) level is necessary but **not sufficient** for a Knot. A character with Bonds 1-4 can reach Disposition +5 with an NPC yet still cannot form a Knot, because Knots demand the deep relational *capacity* that Bonds represents (and their Knot-count slot, floor(Bonds/2)+1, would be only 1-2). This preserves the character-creation tradeoff: low Bonds closes off the Knot-mediated Wager system (social_contest §6.1), Knot-as-Composure-buffer (social_contest §4 Step 6), Knot-mediated Thread-Read (§2.6), and Knot anchoring for Coherence recovery (threadwork §3.5). High Bonds remains the canonical relational-system gate.

When prerequisites are met, a Knot Formation scene appears on the Scene Slate at Priority 2. The scene fires once per eligible NPC per season. If declined, it reappears next season while prerequisites hold.

**Resolution:** Spirit pool (Spirit × 2) vs TN 7, Ob 2.

| Degree | Result |
|---|---|
| Overwhelming (3+ net) | Close Knot forms. Co-movement card drawn (A1/C1: Thread binding is never dimensionally isolated). |
| Success (2 net) | Distant Knot forms. Upgradeable to Close via 3 additional social scenes at Disposition +5 (no roll — time and presence). |
| Partial (1 net) | No Knot. Disposition maintained. NPC aware of the attempt. Cooldown: 2 seasons. |
| Failure (0 net) | No Knot. Disposition −1 (structural asymmetry of intention — A12). Cooldown: 4 seasons. |

**Canon compliance:** A12 (Knots bind threads — Thread contact required), P-12 (relational contagion — formation must be structurally significant), P-15 (second-layer engagement — Spirit check models opening one's rendering to mutual influence), A10 (confrontation development — genuine encounter, not transaction).

### §5.6b Knot Lifecycle (NEW — ED-773)

The Knot lifecycle was previously specified for formation (§5.6a) and use (§2.6, social_contest §3) but not for dissolution. This section specifies how Knots end.

**Strain accumulation:** A Knot accrues *strain* through several mechanisms:
- Knot-mediated remote Thread-Read (§2.6): +1 strain per use.
- Knot-as-Composure-buffer (social_contest_v30 §4 Step 6): +1 strain per use.
- Knot-mediated counsel extraction (npc_behavior §3.5.3 ED-664): +0 strain on extraction itself; +1 strain per subsequent retrieval attempt (single-extraction-per-campaign rule means typically 0 cumulative).
- FR Lock or Dissolution near a Knot partner (threadwork_v30 §6 Knot-substrate inseparability): +1 strain.
- Witnessing Conviction Scar firing in Knot partner (per Piety Track ≥3 Scar count): +1 strain at next Accounting.
- Sustained Disposition reduction (Disposition drops below +3 for **2 consecutive seasons** — defined as: Disposition value at Accounting in season N is below +3 AND Disposition value at Accounting in season N+1 is below +3, both unbroken): +1 strain at Accounting of season N+1. Non-consecutive seasons below +3 do not aggregate. (PP-719 clarification per EC-F2.A-01 fieldwork_lifecycle_stress_01.)

**Knot strain is a bidirectional −5..+5 bond-strain gauge** (ED-912 revision 2026-06-28; replaces the prior one-way 0→capacity accumulator). Positive strain is *wear* toward rupture; negative strain is *resilience* earned through mutual investment.

| Knot Type | Strain range | Starts at | Notes |
|---|---|---|---|
| Distant Knot | −2 … +5 | 0 | Shallower bond; reinforces only to −2. Upgradeable to Close (§5.6a Success). |
| Close Knot | −5 … +5 | −2 | Deeper bond; begins already buffered, can temper to −5. Upgrade Distant→Close shifts current strain by −2 (deepening adds buffer). |

- **Rupture at +5:** when strain reaches +5, the Knot breaks at the next Accounting (the wear-direction ceiling for both types). This is the old "capacity exceeded," now a single shared threshold.
- **−5 = Tempered** (Close only): a maximally reinforced bond **absorbs the next rupture trigger once** — the Knot holds and strain resets to 0 instead of breaking.

**Knot break consequences (strain reaches +5):**
- Disposition with the Knot partner: **−3** (floor −5 per §5.1 Disposition range).
- Both partners take 4 Composure (per A12-derived disorientation: the Thread previously connecting renderings releases force).
- Knot-mediated benefits (Composure shared buffer, +1D social, P-12 contagion, Wager prerequisite, counsel extraction eligibility) cease immediately.
- Knot count slot frees up — player may form a new Knot in a subsequent season per §5.6a procedure.
- For Close Knots that broke from positive strain: Conviction Scar +1 to both partners (the broken Knot leaves perceptual residue per A1/C1 Thread-binding inseparability).

**Rupture (immediate break, bypassing strain accumulation):**

Certain events trigger immediate Knot rupture:

| Trigger | Source | Notes |
|---|---|---|
| Public citation of private counsel (ED-664 §3.5.4) | npc_behavior §3.5.4 | Knot ruptures with Disposition reset to −3 (Antagonistic) — the ED-912 betrayal-rupture value within the −5..+5 range (revised from the prior −4). |
| Knot partner's death | Universal | Disposition becomes irrelevant; Knot partner enters Memory state. Knot-as-buffer can absorb final Composure damage to dying partner per Last Stand rule (player_agency §X — TBD). |
| FR Dissolution targeting Knot partner | threadwork §3.4 | Tears the Knot directly; partner-of-rupture takes +1 Wound (no armor). |
| Permanent Conviction shift to opposing Conviction | npc_behavior §5 | Knot tied to specific Conviction-state; opposite Conviction makes the Thread-binding incompatible. |
| Player explicit dissolution | Player choice | Player may dissolve a Knot at Accounting at any time. Cost: 2 Composure (one-sided release strain). Disposition unchanged (the relationship persists at non-Knotted level). |

**Strain reinforcement (decay toward −5):** strain moves −1 per season at Accounting if no strain was added that season AND Disposition is +3 (Trusting) or higher. Sustained mutual investment pushes the bond past 0 into resilience — Distant Knots floor at −2, Close Knots at −5 (Tempered). This is the reinforcement direction of the bidirectional gauge.

**Threadcut being Knots:** Knots formed with threadcut beings (per §2.6) follow the same lifecycle but use the threadcut being's Coherence as a parallel resource — strain on the Knot also drains the threadcut being's Coherence at +0.5 per strain (round up). When threadcut Coherence reaches 0, the Knot collapses regardless of strain count. This models the threadcut being's continuous Thread-work to maintain existence — adding a Knot adds maintenance cost that competes with their primary survival.

[EDITORIAL: ED-773 — Knot Lifecycle specified in fieldwork §5.6b. Closes the gap surfaced by audit during stress-test 26: Knot strain accumulation was canonized (multiple use-sites add strain) but Knot break/rupture mechanism was not specified. Added strain capacity (Distant 4, Close 7), break consequences (Disposition drop, Composure cost, possible Scar), rupture triggers (ED-664 public citation, partner death, FR Dissolution, Conviction opposition, player choice), strain decay rules (-1/season at sustained Disposition ≥+3 with no strain added). This is what ED-664 §3.5.4 'Knot ruptures' actually means mechanically. Source: 2026-04-25 stress-test 26.]

---

### §5.7 Contest Escalation and Negotiate Boundary



Escalation preserves: current Disposition (applied as starting Piety Track offset, ±1 per 2 Disposition points, capped at ±2). The relationship does not reset — it intensifies.

### §5.8 Niflhel Social Toolkit Extension


- **Exposure modifier:** +2 Exposure per social action (Niflhel existence is conspicuous; any interaction risks notice).
- **Primary pool:** Attunement (per Contest §9.7 — Niflhel social interactions are Attunement-primary regardless of action type).
- **Thread Insight (TS ≥ 30 only):** Before a Negotiate or Read action, Niflhel with TS ≥ 30 may perform a free Thread-Read (Attunement, Ob = floor(target TS / 30, round up), min 1) to perceive one unstated position. This does not consume a scene action but generates +1 Exposure.

### §5.9 NPC-Initiated Social Engagement (NEW)

The socializing system as specified above is entirely player-initiated — the player approaches, the NPC responds. This section adds the reverse: NPCs who seek out the player.

**NPC-initiated social scenes** are generated by npc_behavior_v30 §8.11 (NPC Outreach Generation) and appear in the Scene Slate per player_agency_v30 §4.2 Step 5. When the player pursues an NPC-initiated scene, the following rules apply:

**Outreach scenes (NPC Disposition ≥ +2):** The NPC approaches with an agenda driven by their Conviction. The scene opens with the NPC at their current Disposition. The player may use any social action (Read, Converse, Connect, Negotiate). The NPC's agenda is revealed through conversation — the player does not need to Appraise to discover it. The NPC volunteers the first piece of information for free (they came to talk). Subsequent information follows normal Depth/Disposition gates.

**Demand scenes (NPC Disposition ≤ −2):** The NPC summons the player. The scene opens in the NPC's territory under the NPC's institutional authority. The player may comply (no roll — accept the demand), resist (social contest per social_contest_v30, the NPC as adjudicator), or deflect (Negotiate action, Ob = floor(NPC's highest stat ÷ 2) + 2 — harder than normal Negotiate because the NPC holds power). Successful deflection: demand deferred 1 season, no Disposition change. Failed deflection: demand enforced, Disposition −1.

**NPC arrival timing:** NPC-initiated scenes take place in the player's current territory if the NPC can plausibly reach it, or in the NPC's territory if not (the player must travel to meet the demand). Travel cost applies per §3.3.

---

## §6 EXPOSURE


### §6.1 Cover (Derived Value)

**Cover = Cognition + most relevant History for concealment/tradecraft.**

Cover determines Exposure thresholds. Higher Cover shifts thresholds upward, paralleling how Endurance determines Stamina capacity and Charisma determines Composure capacity.

| Cover | Noticed | Watched | Compromised |
|-------|---------|---------|-------------|
| 1–3 | 3 | 5 | 7 |
| 4–5 | 4 | 6 | 8 |
| 6–7 | 5 | 7 | 9 |
| 8–9 | 6 | 8 | 10 |
| 10–11 | 7 | 9 | 11 |
| 12+ | 8 | 10 | 12 |

### §6.2 Exposure Track

**Exposure: 0 (start of season in each territory).** Accumulates through fieldwork actions.

| Exposure | State | Consequence |
|----------|-------|-------------|
| Below Noticed | Low profile | No effect. |
| Noticed threshold | Noticed | +1 Ob to all fieldwork rolls in this territory for remainder of season. NPCs at Disposition ≤ 0 become aware of the character's activities. |
| Watched threshold | Watched | The dominant faction in this territory may respond. Church: Heresy Investigation eligible. Crown: arrest or surveillance. Varfell: Tribune counter-intelligence. |
| Compromised threshold | Compromised | Current scene ends. The character must leave the territory or go to ground (1 full scene of inactivity). All NPC Dispositions in this territory: −1. Active investigations in this territory: +2 Ob until Exposure resets. |

### §6.3 Exposure Sources

| Source | Exposure Gained |
|--------|----------------|
| Failed exploration/investigation roll | +1 (Failure) or +2 (if Depth ≥ 3) |
| Thread-Read action | +1 (Thread operations are detectable per params_threadwork.md §Observation) |
| Sensitive character present at Depth 3+ POI | +1 (perceptual engagement detectable) |
| Non-sensitive character present at Depth 3+ POI | +0 (institutionally invisible) |
| Surveil action | +2 (extended conspicuous presence) |
| Failed social action at Disposition ≤ 0 | +1 (hostile NPC may report the interaction) |
| Time in hostile territory | +1 per scene (cumulative) |
| Conspicuous action (contacting known dissidents, entering restricted areas, using Thread operations publicly) | +1 per action |
| Niflhel social action | +2 (conspicuous existence) |

### §6.4 Exposure Reduction

| Method | Exposure Reduced |
|--------|-----------------|
| Successful concealment (Cognition × 2, Ob 2) | −2. Requires one scene of active effort. |
| Leave territory | Reset to 0 in new territory. |
| Season change | Reset to 0 in all territories. |
| Cover identity (requires setup: successful Charisma roll Ob 2 before fieldwork begins) | −1 per scene passively (cover absorbs attention). Cover blown on any Compromised result. |
| Faction support (allied faction uses resources to shield the character) | −2 per season. BG: costs 1 Wealth or 1 Influence. TTRPG: requires a successful Diplomacy or social action (Ob 2) establishing the alliance, or an existing narrative alliance. Hybrid: BG resource cost applies. |

### §6.5 Exposure and Church Attention Pool

In territories where the Church has influence (Piety Track ≥ 3 or Church-controlled), Exposure feeds the Church Attention Pool:
- At Watched threshold: +1 Attention Pool in this territory at next Accounting.
- At Compromised threshold: +1 Attention Pool in this territory immediately. (Not +2 — capped at +1 per character per season to prevent runaway CI acceleration.)


---

## §7 DERIVED VALUES SUMMARY

| Value | Formula | Range | Parallel |
|-------|---------|-------|---------|
| Fieldwork Pool | (Primary Attribute × 2) + History bonus | Variable | Combat Pool; Argue Pool |
| Exploration Ob | Depth base + modifiers | 1–10+ | Ob scale per params_core.md |
| Investigation Threshold | GM-set (3/5/8 by scope) | 3–8 | Clock-style progress track |
| Disposition | Starting value ± social actions | −5 to +5 | Asymmetric per-NPC per-PC |
| Cover | Cognition + most relevant History | 2–14 | Composure (Cha + 6); Stamina (End + Hist + 1) |
| Exposure | 0 + accumulation vs Cover-derived thresholds | 0–10+ | Strain toward Composure threshold |

---

## §8 BOARD GAME MODE


### §8.1 New BG Action: Survey (Consul Inward variant)


- **Card type:** Consul Inward (uses existing card slot — no new card type required).
- **Pool:** Influence.
- **Ob:** (5 − Proximity Rating) + 1. Minimum 1. Askeheim (Proximity 0) → Ob 6. Lowenskyst (Proximity 5) → Ob 1. Territories closer to the Calamity epicentre are harder to survey safely.
- **Effect on Success:** Reveal one undiscovered POI in the territory. POI provides a territory-level bonus:

| POI Category | BG Bonus |
|-------------|----------|
| Resource | Prosperity +1 in this territory |
| Secret | +1D on next military or intelligence action in this territory |
| Remnant | Thread operation Ob −1 in this territory for 2 seasons; Thread Debt token placed |
| Anomaly | MS −1 at this territory immediately; Warden Cooperation (WC) +1 eligible when Warden Recognition (WR) ≥ 2 (Wardens recognise the faction as a steward). See params_board_game.md §Warden Cooperation and §Warden Recognition. (PP-630) |

- **Effect on Failure:** No POI found. +1 Church Attention Pool in this territory if the survey targeted Depth ≥ 3 content.

### §8.2 Existing Actions as Fieldwork

| Fieldwork Activity | BG Action | Already Defined | Notes |
|-------------------|-----------|-----------------|-------|
| Investigation (intelligence) | Tribune Investigate | params_board_game.md §Standard Action Ob | Ob 2. Reveals faction stats. |
| Investigation (espionage) | Tribune Spy | params_board_game.md §Standard Action Ob | Ob = floor(target Intel/2) + 1. |
| Socializing (diplomacy) | Senator Diplomacy | params_board_game.md §Standard Action Ob | Ob = floor(target Stability/2) + 1. |
| Socializing (public) | Senator Decree | Already defined | Disposition shift at faction scale. |
| Exploration (governance) | Consul Govern | Already defined | Prosperity development = territory-level exploration. |
| Thread exploration | Thread Operation | Already defined | Pontifex/Weaver card. |


### §8.3 BG Social Interaction

At BG scale, inter-faction relationships are modelled by existing mechanics: Senator Diplomacy (Ob = floor(target Stability/2) + 1) and Standing/Reputation tracks (0-5 each, per clock_registry.md). Disposition is a personal-scale track that does not apply at faction scale. Player-to-player faction relationships are negotiated, not rolled. NPC faction behaviour is governed by NPC artificial intelligence rules in bg_v05.

---

## §9 HYBRID MODE

Following the established hybrid pattern (social_contest_v30.md §11):

### §9.1 Hybrid Fieldwork Procedure

1. **BG layer (Strategic Phase):** The faction plays a Survey, Investigate, Govern, or Diplomacy action at strategic scale. Record the degree as a **Fieldwork Offset** (Failure: −1; Partial: +0; Success: +1; Overwhelming: +2). Cap: ±2.
2. **Set TTRPG conditions:** Apply Fieldwork Offset as Ob reduction to the TTRPG fieldwork scene. Minimum Ob 1.
3. **TTRPG personal scene (Personal Phase):** Run exploration, investigation, or social scene per §§3–5 from adjusted Ob. The PC conducts their personal fieldwork with the faction's strategic support (or hindrance, if the faction's action failed).
4. **Resolution (Cascade Phase):** TTRPG scene determines final outcome. Consequences propagate:
   - Exploration: POI discovered → territory bonus applied at Accounting.
   - Investigation: Evidence Track advanced → if threshold reached, faction intelligence updated.

### §9.2 Hybrid Fieldwork Timing


Per PP-089: Hybrid season phase order is fixed (Strategic Phase first, Personal Phase second). Fieldwork Offsets from Strategic Phase are available immediately for Personal Phase use.

---

## §10 GODOT VIDEO GAME IMPLEMENTATION

### §10.1 Exploration Map Architecture


**Node structure (Godot):**
```
Territory (Node2D / Node3D)
├── NavigableArea
│   ├── PathGraph (navigation mesh or A* grid)
│   └── EnvironmentZones (Calamity radiation visual effects)
├── POI_Landmarks[] (always visible)
├── POI_Resources[] (visible if perception gate met)
├── POI_Secrets[] (visible if perception gate met)
├── POI_Remnants[] (visible if TS ≥ 10; rendering strain triggers on interact)
├── POI_Anomalies[] (visible if TS ≥ 30; environmental hazard zone)
└── POI_Breaches[] (visible if TS ≥ 50; existential encounter zone)
```



### §10.2 Intelligibility Gradient Visualisation



| TS Range | Visual Presentation | Implementation |
|----------|---------------------|----------------|
| 0–9 | The world as settled consciousness renders it. Solid, consistent, complete. | Default scene rendering. No post-processing. |
| 10–29 | Something at the edges. Faint disturbance near Thread-adjacent sites. | Shader: subtle vertex displacement + chromatic aberration within POI activation radius. |
| 30–49 | The substrate's structure becomes part of the character's world. Thread filaments visible as a constitutive layer. | Shader: additive blend layer showing Thread mesh. Activated per-POI. |
| 50–69 | Full thread-sight. The substrate is experienced as a dimension of reality, not a hidden layer. | Shader: persistent overlay on all objects within Calamity zones. NPC aura indicators. |
| 70+ | The boundary of the intelligible. What lies beyond is not darkness or void — it is the rendering's dissolution, the edge of what consciousness can constitute. | Shader: dissolve effect at zone boundaries. Particle systems for surfeit-of-being eruptions. Audio: low-frequency rumble. |

**Certainty-dependent constitution:**



### §10.3 Investigation Journal System

The Evidence Track maps to a **Journal** UI element:

```
Journal
├── Active Investigations[]
│   ├── Question (text)
│   ├── Evidence Track (progress bar: current / threshold)
│   ├── Clues[] (individual evidence items with reliability tags)
│   │   ├── ClueItem { text, source, reliability_tag, depth }
│   │   └── InertKnowledge { text, source, flagged: true }
│   └── Status (open / resolved / desperate_trail / blocked)
├── Resolved Investigations[]
└── Rumour Board (unverified items, no progress tracking)
```


### §10.4 Disposition and Dialogue

NPC Disposition drives the dialogue system:

**Disposition meter:** Visible on NPC portrait during interaction. Range −5 to +5 displayed as a segmented bar.


**Social action as dialogue choice:** Each dialogue node can trigger a social action roll. The player selects the approach (Read, Converse, Connect, Impress, Negotiate, Rumour), the game rolls the pool, and the result determines the conversation branch.


### §10.5 Dice Visualisation

d10 pool rolls use a visual system consistent across all Valoria mechanics:

| Die Face | Visual | Colour |
|----------|--------|--------|
| 1 | Skull icon or down-arrow | Red |
| 2–6 | Neutral pip | Gray |
| 7–9 | Success checkmark | Blue |
| 10 | Double success + chain icon | Gold |


### §10.6 Season and Clock Integration

Fieldwork actions consume in-game time:
- Each exploration/investigation/social scene = 1 time unit.
- At season end: Accounting Phase fires automatically. Clocks advance. Faction actions resolve.

**Clock HUD:** MS, CI, IP displayed persistently. PI and faction-specific tracks available on faction screen. Exposure displayed per-territory on map overlay.

---

## §11 THREE-MODE SUMMARY TABLE

| Mechanic | TTRPG | Board Game | Hybrid | Godot |
|----------|-------|-----------|--------|-------|
| Exploration | Full Discovery Procedure (§3.2) | Survey action (§8.1) | BG Survey → TTRPG Discovery | Navigable map + POI nodes |
| Investigation | Evidence Track (§4.1) | Tribune Investigate/Spy | BG Investigate → TTRPG Evidence Track | Journal + Evidence Track progress bar |
| Socializing | Disposition + social actions (§5) | Senator Diplomacy (existing) | BG Diplomacy → TTRPG social scene | Dialogue system + Disposition meter |
| Perception gates | TS/Cognition/Attunement checked | Faction-level (no individual TS) | PC gates during Personal Phase | Character TS gates POI visibility |
| Rendering strain | Fires on Depth 3+ encounter (§3.4) | Abstracted (Proximity Rating) | Fires during Personal Phase only | Automated trigger on POI interaction |
| Co-movement | Thread-Read only (§4.5) | Co-Movement Card on Thread operation | Fires during Personal Phase on Thread-Read only | Automated trigger on Thread-Read |
| Exposure | Per-character, Cover-derived thresholds (§6) | Implicit in action Ob | Per-character during Personal Phase | Per-territory Exposure meter |
| Depth axis | GM-assigned per scene | Abstracted (Proximity Rating) | GM-assigned; BG Offset applied | Authored per-POI |

---

## §12 OPEN ITEMS AND EDITORIAL FLAGS

### New editorial items

| ID | Description | Priority |
|----|-------------|----------|
| ED-507 (was ED-NEW-01) | POI catalog per territory. Requires cross-reference with geography_design.md and calamity_radiation.md. Each territory needs 2-6 authored POIs across depth levels with conditional availability gates. **FLAGGED — authorial decision.** | P2 |
| ED-508 (was ED-NEW-02) | Named NPC starting Dispositions. Requires cross-reference with NPC roster. Partially addressed by ARC-T23 Remembrancer (ED ledger entry, 2026-04-13). Full NPC Disposition table pending. **FLAGGED — authorial decision.** | P2 |
| ED-496 (was ED-NEW-03) | Survey action stat assignment confirmed: Influence. Monitor in simulation — if Survey dominates Govern, consider Ob adjustment. Resolved: Influence confirmed canonical for Survey (fieldwork_design_v1.md §8.1 states explicitly). SIM-DEBT-FW-05 confirms Survey and Govern occupy different niches. **RESOLVED.** | P2 → RESOLVED |
| ED-497 (was ED-NEW-04) | Exposure ↔ Church Attention Pool interaction. §6.5 caps at +1/character/season and +2/territory/season from fieldwork. **CONFIRMED SAFE** (PP-581 simulation: fieldwork contributes ~11% of max CI acceleration over 4 seasons). **RESOLVED.** | P3 → RESOLVED |
| ED-498 (was ED-NEW-05) | Negotiate vs Contest boundary defined (§5.7): "The GM does not offer a choice — the situation's structure determines the mechanic." Edge cases foreclosed by design. **RESOLVED.** | P2 → RESOLVED |
| ED-509 (was ED-NEW-06) | Godot POI node architecture (§10.1). Requires validation against Valoria-game repo Godot project structure. Deferred until Godot implementation phase. **FLAGGED.** | P3 |
| ED-499 (was ED-NEW-07) | Evidence Track persistence. §4.1 explicitly states "persistent across scenes and sessions." No mechanical overhead beyond GM notes — same as clocks. **RESOLVED.** | P3 → RESOLVED |
| ED-500 (was ED-NEW-08) | Disposition decay rate (§5.2: −1/season above +3). SIM-DEBT-FW-03 confirmed: Neutral→Bonded = 6-8 actions across 3-4 seasons; maintenance actions needed at +3. Pacing appropriate. **RESOLVED.** | P2 → RESOLVED |
| ED-501 (was ED-NEW-09) | Thread-Read co-movement effects (§4.5). Confirmed: uses threadwork_redesign_v25.md §3.2 co-movement table directly. **RESOLVED.** | P3 → RESOLVED |
| ED-502 (was ED-NEW-10) | Breach encounter (Depth 5) + Coherence stacking. **CONFIRMED PROPORTIONAL** (PP-581). Intentional — the Breach is the rendering's edge. **RESOLVED.** | P3 → RESOLVED |
| ED-NEW-11 | Pool formula ×2 — **RESOLVED** by PP-615. params_core.md now confirms (Agility × 2) as canonical. PP-247 note was stale. Fieldwork Ob calibration is correct. | RESOLVED |
| ED-503 (was ED-NEW-12) | Sincerity Gate (§5.3) uses Spirit. Spirit governs: Resolve (Inspiration max), Thread contact wound disruption check (PP-624), Thread-Read pool, Dissonance checks, Sincerity Gate. All are manifestations of metaphysical grounding — Spirit is the appropriate attribute for all. Not overloaded; unified. **RESOLVED.** | P3 → RESOLVED |
| ED-504 (was ED-NEW-13) | Desperate Trail (§4.4). 4D at TN 8: P(≥1) ≈ 60% (viable). SIM-DEBT-FW-02 confirmed pacing. Partial +2 compensates. **RESOLVED.** | P2 → RESOLVED |
| ED-505 (was ED-NEW-14) | Finding + Contest interaction. §4.1 defines Finding reliability. §2.3 Fieldwork→Contest handoff states: Evidence cited = +2D Recall bonus, Evidence not consumed. SIM-DEBT-FW-07 (transition sim) confirmed. **RESOLVED.** | P3 → RESOLVED |
| ED-506 (was ED-NEW-15) | POP Coherence −1 additional: subject to per-op cap of −1 (unlike FR/Binding Operations, which are cap-exempt per PP-196). Total POP Coherence cost = −1 regardless of scale (−1 scale at Relational+ + −1 additional, capped at −1). Note propagated to params_threadwork.md canonical section. **RESOLVED.** | P2 → RESOLVED |

### Items resolved by PP-580 extended threadwork simulation (2026-04-13)

| Item | Resolution |
|------|------------|
| KN-01/02 | Knot-mediated remote Thread-Read: §2.6. +1 Knot strain per use. Detection → Disposition −3. |
| DIS-01/02 | Non-sensitive partner Dissonance: §2.7. Spirit check vs Dissonance Factor. Field team rotation. |
| CI-01/02/03/04 | Threadcut being social fieldwork: §2.8. Testimonial tag. P-08 bridged by being's translation. Evidence Track = player-level knowledge. Counter-investigation possible. |
| MA-02/03 | Mending arcs as investigation: §2.4. Severity reduction = evidence. Multi-season campaign pacing. |
| CW-01 | Community Organizing detectable: §2.4 table (Weaving row covers Community Organizing). |

### Items resolved by PP-579 ontological correction (2026-04-13)

| Item | Resolution |
|------|------------|
| PP-578 TW-11 | FALSE CLAIM STRUCK. "Lock/Dissolution produce 0 Evidence progress" was ontologically incorrect. All Thread operations may advance Evidence Track when consequences reveal investigation-relevant information. §2.4 rewritten. |
| PP-578 TW hierarchy | Replaced with contextual yield model. Investigation yield depends on what is targeted and why, not on operation type. GM determines yield. |
| Domain Echo integration | §2.5 added. Resolved Findings fire Domain Echo per stage11 §11.5. NPC arc cascades follow. |
| NPC Disposition on investigation | §2.5 added. Disposition −2 if NPC learns they were investigated; +1 if NPC wanted truth found. |
| Forensic applications | §2.4 added. Dissolution (Gap topology + concealer signature), Lock (resistance pattern diagnostics), POP (paradox window dual-state). |
| Scale/distance/breadth | §2.4 added. Knot-mediated remote Thread-Read. Collective Thread-Read at Structural scale. Temporal reach via POP recency. |

### Items resolved by PP-578 threadwork transition simulation (2026-04-13)

| Item | Resolution |
|------|------------|
| TW-01 | Leap vulnerability timing: window closes when Thread-Read resolves. §2.4. |
| TW-10 | FR ops suppress fieldwork: one Thread op per action, Thread-Read and FR mutually exclusive. §2.4. |
| TW-12 | Wounds → +1 Ob to Thread ops requiring Leap (not −1D pool). §2.4. |
| TW-05 | POP Coherence −1 additional IS subject to per-op cap (not exempt like FR surcharge). Distinct cost profiles. |

### Items resolved by PP-577 transition simulation (2026-04-13)

| Item | Resolution |
|------|------------|
| F-TRANS-01 | Fieldwork → Combat handoff added (§2.3). Exposure → ambusher advantage. |
| F-TRANS-04 | Evidence not consumed by Contest citation — stated explicitly (§2.3). |
| F-TRANS-06 | Mass battle suspends fieldwork — suspension rule added (§2.3). |
| F-TRANS-07 | Thread-Read in Phase 4 = intelligence, not offensive. Co-movement fires. (§2.3). |
| F-TRANS-10 | Contest Appraise → +1 Evidence Track progress (Testimonial). (§2.3). |
| F-TRANS-12 | Post-battle investigation = 1 fieldwork scene. Battle ≠ fieldwork time. (§2.3). |
| F-TRANS-05 | Post-Contest Disposition shift: winner +1, loser −1 with adjudicator. (§2.3). |
| F-TRANS-09 | Combat Exposure codified: quiet +1, conspicuous +2, public +3. (§2.3). |
| F-TRANS-11 | Combined Findings: +1D per additional Finding in Contest, max +2D. (§2.3). |

### Items resolved by PP-576 audit (2026-04-13)

| Item | Resolution |
|------|------------|
| D-2 (Let It Ride) | Added §2.2. Failed fieldwork action on specific target cannot be reattempted same scene. |
| D-9 (Overwhelming floor) | Added §2.2. Fieldwork uses core engine degree table (net ≥ 2×Ob AND ≥ 3). |
| D-3 (Wounds) | Added §2.2. Physical wounds apply to exertion-based fieldwork only. Rattled applies to social. |
| D-5 (Multi-character) | Added §3.2. Leader + max 2 assistants. Assistant success = +1 net to leader. Assistant fail = +1 Exposure. |
| D-6 (Cross-territory) | Added §4.1. One track per investigation regardless of territory. Exposure per territory. |
| D-7 (Desperate Trail persistence) | Added §4.4. Desperate Trail persists through Compromised. Only clears on Success or season change. |
| D-1 (Perception gates) | Added §2.2. Gates are hard — capacity, not skill. No Beginner's Luck for perception gates. |
| D-4 (Non-sensitive +5) | Added §5.6. Non-sensitive Bonded: no decay, +1D, but no Knot formation or P-12 contagion. |
| D-SIM-5 (Finding reliability) | Added §4.1. Resolved investigation produces Finding with strongest tag. |
| B-2 (Cover plateau) | Fixed §6.1. Extended threshold table: Cover 10-11 = 7/9/11; Cover 12+ = 8/10/12. |
| C-1 (Faction support TTRPG) | Fixed §6.4. TTRPG: requires Diplomacy Ob 2 or existing alliance. |
| E (Inspiration spend) | Added §2.2. Spend 1 Inspiration before rolling to reduce Ob by 1 (min 1). |
| E (Gift/Bribe) | Added §5.2. Gift/Bribe improves starting Disposition +1, no roll, once per NPC per season. |

### Simulation debt

| ID | Description |
|----|-------------|
| SIM-DEBT-FW-01 | **RESOLVED** (PP-583). Ob calibration across Depth 1-5 at 5 pool sizes ± hostile/foreign modifiers. Calibration sound: 5D handles D1, 9D handles D1-2, 13D handles D1-3, 17D handles D1-4, 24D challenges at D5. |
| SIM-DEBT-FW-02 | **RESOLVED** (PP-576 partial, PP-583 complete). 5-threshold investigation completes in 3-5 scenes for high-pool (15-19D). Low-pool (9D): 4-6 scenes at D1-2. Pacing confirmed. |
| SIM-DEBT-FW-03 | **RESOLVED** (PP-583). Neutral→Bonded: ~6-8 actions across 3-4 seasons (with failures and maintenance at +3). Sincerity Gate adds ~37% failure on instrumental Connect. Meaningful investment confirmed. |
| SIM-DEBT-FW-04 | **RESOLVED** (PP-581). AP feedback: fieldwork contributes ~11% of max CI acceleration. +1/char/season +2/territory/season cap is sufficient. |
| SIM-DEBT-FW-05 | **RESOLVED** (PP-583). Survey and Govern occupy different niches. Govern dominates mid-proximity (reliable Prosperity). Survey dominates high-proximity (safe northern territories). Neither dominates the other. |
| SIM-DEBT-FW-06 | **RESOLVED** (PP-583). Cover 3: detected in 3 scenes. Cover 9: full season before detection. Cover 12+: near-immune to casual detection, threatened only by combat+Thread stacking. Appropriate differentiation. |
| SIM-DEBT-FW-07 | **RESOLVED** (PP-577). Transition simulation. All 6 directions functional. |
| SIM-DEBT-FW-08 | **RESOLVED** (PP-578/PP-579). Threadwork × fieldwork. All ops advance Evidence contextually. |
| SIM-DEBT-FW-09 | **RESOLVED** (PP-579). NPC arc stress tests. 7 Domain Echo cascades tested. |
| SIM-DEBT-FW-10 | **RESOLVED** (PP-580). Extended threadwork (Knots, Community Organizing, threadcut beings, Mending, Dissonance). |

### Propagation status

| File | Change | Status |
|------|--------|--------|
| references/canonical_sources.yaml | Fieldwork system entry | **DONE** (PP-575) |
| references/params_fieldwork.md | Mechanical values extraction | **DONE** (PP-583) |
| designs/systems/clock_registry.md | Exposure, Evidence Track, Disposition, Cover tracks | **DONE** (PP-575) |
| references/propagation_map.md | Cross-references to combat, contest, threadwork, BG, geography | PENDING |
| references/params_board_game.md | Survey action in Standard Action Ob table | PENDING |
| references/params_core.md | Attribute usage table includes fieldwork roles | PENDING |
| compilation/v0.14/stage11_scale_transitions_deprecated.md | 9th handoff rule (Fieldwork ↔ all systems) | PENDING |
| tests/coverage_matrix.md | SIM-DEBT-FW-01 through FW-10 (all RESOLVED) | PENDING |
