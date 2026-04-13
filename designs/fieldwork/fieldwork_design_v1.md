# VALORIA — FIELDWORK SYSTEM v1.1
## Exploration / Investigation / Socializing
## Status: DESIGN — approved for commit. Review corrections applied 2026-04-13.
## Mode applicability: ALL (TTRPG baseline; Hybrid bridging; Board Game abstraction; Godot video game)
## Canon compliance: P-01 (inseparability — applied to Thread-Read operations, not passive discovery), P-03 (rendering = consciousness-performed), P-07 (Calamity = rendered-side mechanism), P-08 (epistemological barrier), P-14 (all modes express inseparability), P-15 (three-layer being-persistence)
## Cross-references: params_core.md, social_contest_system_v2.md, combat_design_v1.md, threadwork_redesign_v25.md, geography_design.md, calamity_radiation.md, clock_registry.md
## Review applied: fieldwork_review.md (2026-04-13). All 11 required corrections + 8 recommended additions incorporated.

---

## CORE PRINCIPLE: INTELLIGIBILITY GRADIENT

Combat resolves physical conflict. Social Contest resolves formal social conflict. Fieldwork resolves the character's engagement with the world outside of structured conflict — the acts of moving through space, assembling knowledge, and building relationships.

Fieldwork's organising metaphor is the **Intelligibility Gradient**. The thread-substrate is not uniformly accessible to consciousness. Near settled centres, intelligibility is dense — the world is fully given to consciousness as coherent, reliable experience. At the periphery (the Southernmost, Einhir ruins, Calamity zones), intelligibility thins. What can be perceived, understood, and related to depends on the perceiver's epistemic capacity.

The rendering itself is always total. A non-sensitive character's world is fully real — their consciousness renders completely. The gradient is in what the substrate makes available to that rendering. Thread configurations that exceed a character's epistemic capacity are not hidden from them; they are ontologically unavailable — the rendering has nothing to process.

The Intelligibility Gradient produces two mechanical consequences:

1. **Perception gates.** What a character can discover at a given depth depends on their Thread Sensitivity (TS), their Certainty, and their Coherence. Two characters standing in the same location inhabit genuinely different experiential worlds — not filtered views of one world.
2. **Rendering strain on deep encounter.** Encountering Thread-adjacent phenomena at depth strains the character's rendering capacity. The character's consciousness confronts configurations that approach or exceed what it can process. This is not co-movement (which requires a Thread operation per P-01) — it is the rendering's encounter with its own limits.

This is the system's philosophical claim: exploration, investigation, and socialising are acts of rendering. The character's consciousness extends into the world — not because the ground has agency (P-07), but because rendering at depth tests the relationship between finite consciousness and the substrate's constitutive structure.

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
- **Exploration depth** = how far from the settled intelligibility you have moved, physically or metaphysically.
- **Investigation depth** = how far beneath the surface of a question you have dug.
- **Social depth** = how far past public presentation you have reached into another person's inner world.

**Ob modifiers (cumulative with base Ob):**
- Hostile faction controls territory or institution: +1 Ob
- Character is foreign to territory (no relevant History): +1 Ob
- Allied faction provides support: −1 Ob
- Character is local resident with relevant History: −1 Ob
- Calamity radiation: +1 Ob per RS band below 60 at current Proximity Rating (see calamity_radiation.md)
- Active Heresy Investigation in territory: +1 Ob to investigation/social actions involving Thread-adjacent topics

Ob floor: 1 (per core engine).

---

## §2 FIELDWORK POOL

**Pool = (Primary Attribute × 2) + History bonus**

Same construction as Contest Pool (social_contest_system_v2.md §3: Primary Attribute × 2 + History bonus). History bonus = relevant History points + 3 (per params_core.md §4.1 character creation).

**[EDITORIAL: ED-NEW-11 — Pool formula ×2 contradiction. This formula matches the Contest system but conflicts with PP-247, which corrected Combat Pool to Agility + History points + 3 (non-doubled) in params_core.md. combat_design_v1.md §1 still states (Agility × 2). Resolve project-wide: either all three systems use doubled attribute, or none do. Ob calibration of the entire Depth Axis depends on this resolution. Current Obs assume the doubled formula. If non-doubled is canonical, all Depth 3+ Obs must be reduced by 1-2.]**

TN: 7 (Standard). TN 6 (Controlled) when unhurried with preparation. TN 8 (Desperate) under duress, exhaustion, or active Calamity exposure.

**History selection:** One History per action, selected by the player, confirmed by GM. The History must be narratively defensible for the specific action (a History of "Einhir Architecture" applies to Examine at a Remnant; it does not apply to Rumour in a tavern). If no History is relevant: pool = (Primary Attribute × 2) + 3 (the base constant without History points).

### §2.1 Primary Attribute by Activity

| Activity | Sub-type | Primary Attribute | Reasoning |
|----------|----------|-------------------|-----------|
| Exploration | Terrain / navigation | Cognition | Structural analysis, pathfinding, cartography |
| Exploration | Thread-aware | Attunement | Sensing Thread phenomena, reading the substrate |
| Exploration | Endurance-based | Endurance | Forced marches, exposure, harsh terrain |
| Investigation | Physical evidence | Cognition | Examining objects, documents, architecture, forensics |
| Investigation | Witness / informant | Attunement | Reading people, sensing deception, calibrating trust |
| Investigation | Lore / research | Recall | Archives, oral histories, institutional records, precedent |
| Investigation | Thread-Read | Attunement | Perceiving Thread-level configurations via perceptive Leap (§4.5). TS ≥ 30 required. |
| Socializing | Read | Attunement | Determining NPC's true state, hidden motivation |
| Socializing | Impress | Charisma | Making a favourable impression, projecting authority |
| Socializing | Connect | Bonds | Building genuine trust, deepening a relationship |
| Socializing | Rumour | Charisma | Gathering unverified intelligence through social networks |
| Socializing | Negotiate | Attunement | Reaching informal agreement (below Contest threshold — see §5.7) |

---

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

> **PP-591: Exposure → AP contribution gate.** Fieldwork actions generate Exposure in all cases, but Exposure converts to Attention Pool (AP) contribution ONLY when the fieldwork action involves Thread-sensitive elements (Thread-Read, Depth 3+ discovery, practitioner-detectable activity). Non-sensitive investigation (mundane evidence gathering, social questioning, observation) generates Exposure for Cover/personal risk purposes but does NOT feed AP. This prevents routine investigation from automatically triggering Inquisitor deployment. AP contribution rate unchanged for Thread-sensitive actions: +1/character/season, +2/territory/season cap.

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
| 5 (Breach) | **Severe strain.** Coherence −1 automatic (layer-2 failure threshold — the rendering encounters the boundary of what it can process). **Certainty forced to ≤ 2** (the unintelligible ground is directly proximate). **TS +1** (the character's rendering, forced to operate at its absolute limit, permanently expands its capacity — not from perceiving the unintelligible itself, which remains inaccessible, but from perceiving the boundary). |

**Thread-Read is the exception.** When a character performs a Thread-Read action (§4.5), they are in active Thread contact via perceptive Leap. This IS a Thread operation. P-01 fires: three-dimensional co-movement auto-effects apply (temporal, epistemic, actualized). Thread-Read is the only fieldwork action that produces co-movement.

**Non-sensitive characters at Depth 3+:** A non-sensitive character (TS < 10) accompanying a sensitive explorer cannot perceive Thread-adjacent POIs directly. They experience: vague unease (TS 0-9 per observation table, params_threadwork.md). They observe the sensitive character's reaction. Any Thread-level information communicated to them becomes Inert Knowledge (per P-08, stage11 §11.6). Non-sensitive characters have a compensating advantage: they generate **+0 Exposure** from encountering Depth 3+ POIs (the Church does not flag non-sensitive presence near Thread sites, because non-sensitive characters are institutionally invisible as Thread investigators). Sensitive characters present at Depth 3+ POIs generate +1 Exposure from their perceptual engagement.

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

The GM sets the threshold at investigation opening. The threshold is not known to the player (unless the investigation is institutional — Church Heresy Investigations have published procedure lengths per social_contest_system_v2.md §7).

**Evidence Track progress is persistent across scenes and sessions.** An investigation begun in one session can be continued in the next. Evidence does not decay (knowledge, once assembled, remains assembled). However, the world may change around the evidence — a witness may be killed, a document may be destroyed, a site may be altered by Thread operations.

**Depth-limited resolution:** When the Evidence Track reaches its threshold, the investigation resolves at the deepest depth the investigator has accessed. If the answer lies at Depth 4 but the investigator conducted only Depth 1-3 actions, they receive a partial answer — everything the evidence supports up to the depth accessed. The GM communicates this clearly: "You have assembled a complete picture of everything that is available at your level of perception. There is more, but it is beyond your current reach." Investigation can be reopened at greater depth if the character later acquires the perception prerequisites (gains TS, builds Disposition with a key informant, gains institutional access).

### §4.2 Investigation Actions

Each investigation action represents one scene of focused inquiry. A character can perform 1–2 investigation actions per scene. Each action is a roll.

| Action | Primary Attribute | What it does | Depth access |
|--------|-------------------|-------------|-------------|
| Examine | Cognition | Study physical evidence, architecture, documents, objects | Up to Hidden (2); Buried (3) if TS ≥ 10 |
| Interview | Attunement | Question a witness, informant, or subject | Up to Hidden (2); Buried (3) at Disposition +3 |
| Research | Recall | Consult archives, oral histories, institutional records, Einhir documents | Up to Hidden (2); Buried (3) at institutional access |
| Surveil | Cognition | Observe a location, person, or faction operation over extended time | Up to Hidden (2). +2 Exposure (conspicuous activity). |
| Thread-Read | Attunement | Perceive Thread-level configurations via perceptive Leap (§4.5) | Depth 3–5. TS ≥ 30 required. Co-movement fires (P-01). +1 Exposure. |
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

**Investigative asymmetry, both directions:** Sensitive characters access deeper layers but generate more Exposure and produce institutionally inadmissible evidence. Non-sensitive characters are capped at Depth 2 without social mediation but generate lower Exposure at Depth 3+ POIs (+0 vs +1) and produce universally admissible evidence. The optimal investigation team contains both.

### §4.4 Desperate Trail (Fail Forward)

Trails never go cold — they become more dangerous. After 3 consecutive failed investigation actions (net successes ≤ 0) targeting the same investigation, the investigation enters **Desperate Trail** state. The Evidence Track remains open, but conditions escalate:

- **TN shifts to 8** (Desperate) for all subsequent actions on this investigation. The easy approaches are exhausted; what remains demands risk.
- **Exposure doubles** on failed rolls (+2 base becomes +4; +1 becomes +2). The character is now pressing into places and asking questions that attract serious attention.
- **The GM introduces a complication** — a new obstacle that is itself consequential. The witness who could help is under Church surveillance. The archive is guarded by someone with their own agenda. The site is inside a territory that just changed hands. The complication is not a wall; it is a new situation that must be navigated, producing its own story.
- **Evidence progress on Partial improves to +2** (from +1). The desperation itself produces insight — every remaining action that lands, lands harder, because the investigator is now operating at the edge of what is accessible.

Desperate Trail clears when: (a) any single action produces a Success or Overwhelming result (the breakthrough resets conditions — TN returns to 7, Exposure normalises); or (b) the season changes (new circumstances, new access, fresh start).

**Design principle:** Investigation failures should never produce "nothing happens." A failed Examine reveals that the evidence has been tampered with (who tampered with it?). A failed Interview means the informant was frightened by something (what frightened them?). A failed Research discovers the relevant archive section has been removed (by whom?). Every failure is a clue about the forces working against the investigation.

### §4.5 Thread-Read as Perceptive Leap

Thread-Read is a **perceptive Leap** — the practitioner enters active Thread contact (per threadwork_redesign_v25.md Leap procedure) to perceive Thread-level configurations rather than to manipulate them.

**Procedure:**
1. Declare Thread-Read. Requires TS ≥ 30. The practitioner must not be in melee with a declared attacker.
2. **Leap.** Follow standard Leap procedure: full-round action (Priority 5 in combat time; one scene action in fieldwork time). Vulnerability window applies — the practitioner is in Thread contact and exposed.
3. **Perception.** Roll Attunement × 2 + History bonus, TN 7, Ob per Depth. Add Thread Pool Score (TS ÷ 10, round down) as bonus dice.
4. **Co-movement fires (P-01).** Thread-Read is a genuine Thread operation. Three-dimensional auto-effects apply per threadwork_redesign_v25.md §3.2: temporal auto-effect (Calamity Drift + History Resonance), epistemic auto-effect (Certainty modifier, investigation/testimony consequences), actualized auto-effect (d6 consequence table).
5. **Coherence cost.** Per scale table (stage11 §11.1): Object/Personal scale = 0 auto-cost; Relational+ scale = −1 Coherence.
6. **Evidence progress.** Apply degree result per §4.2 table.

**Thread-Read is the only fieldwork action that produces co-movement.** All other fieldwork actions (Examine, Interview, Research, Surveil, Reconstruct, social actions) are rendering-level activities that do not enter Thread contact and do not trigger P-01.

### §4.6 Contested Investigation

When two parties are investigating the same question (or one party is investigating while another is concealing), the investigation becomes **contested.**

**Concealment Pool:** The concealing party rolls (Cognition × 2) + relevant History, TN 7. Their net successes set a **Concealment Ob** that the investigator must exceed in addition to the base Ob.

This resolves per action, not per investigation. Each investigation action faces: base Ob (from Depth) + Concealment Ob (from opponent's concealment roll for that scene). The concealing party must actively maintain concealment — each scene they are not present to conceal, the Concealment Ob is 0.

**Church Heresy Investigation** is a specific institutional form of contested investigation. The Church's Concealment Ob equivalent is its investigatory bonus (+1D Investigate, +2 Ob for targets in Church territory with Inquisitor). See social_contest_system_v2.md §7 and params_board_game.md §Church Attention Pool for the BG-scale version.

---

## §5 SOCIALIZING

### §5.1 Disposition Track

Every named NPC holds a **Disposition** toward each player character. Disposition measures the NPC's willingness to engage, share, and cooperate — outside of formal Contest structures.

**Disposition range: −3 to +5.**

| Value | Label | Effect on Social Ob | Information Gate |
|-------|-------|---------------------|-----------------|
| −3 | Hostile | +3 Ob | Refuses interaction. Violence possible. |
| −2 | Suspicious | +2 Ob | Minimal cooperation. Monosyllabic. |
| −1 | Wary | +1 Ob | Guarded responses. Surface information only. |
| 0 | Neutral | +0 Ob | Standard interaction. Surface information. |
| +1 | Interested | +0 Ob | Willing to engage. Settled information accessible. |
| +2 | Friendly | −1 Ob | Volunteers information. Hidden information accessible. |
| +3 | Trusting | −1 Ob | Shares private knowledge. Buried information accessible. |
| +4 | Devoted | −2 Ob | Takes personal risk for the character. Liminal information accessible. |
| +5 | Bonded | −2 Ob | Knot candidate. Deepest personal access. |

**Starting Disposition** is determined by faction alignment, social context, and NPC personality:
- Same faction: +1
- Allied faction: 0
- Neutral faction: 0 or −1
- Rival faction: −1 or −2
- Hostile faction: −2 or −3
- Personal factors (Beliefs, shared History, prior interaction): ±1 per factor (GM discretion)
- Reputation (per core engine): Reputation 3+ in character's favour: +1 starting Disposition

**Disposition is asymmetric:** NPC A's Disposition toward PC B ≠ NPC A's Disposition toward PC C. Each relationship is tracked independently.

### §5.2 Social Actions (Non-Contest)

Social actions outside formal contests use the fieldwork pool. These are individual rolls, not the exchange structure of social_contest_system_v2.md. A social action represents one meaningful interaction within a scene.

**Not all social interaction is a social action.** Unrolled conversation — where no specific outcome is sought — is roleplay. It may inform the GM's Disposition adjustments but does not require a roll. Characters sharing a meal, swapping stories, or commiserating do not need mechanical resolution. The system models purposeful social engagement, not all human contact.

| Action | Primary Attribute | Ob | Effect |
|--------|-------------------|-----|--------|
| Read | Attunement | 1 (Surface); 2 (Hidden); 3 (Buried) | Determine NPC's current Disposition, one Belief, emotional state, or hidden motivation. Degree determines specificity. |
| Converse | Charisma | 1 + Disposition modifier (negative Disposition increases Ob) | Shift Disposition. Gather Settled-depth information. |
| Connect | Bonds | 2 + depth of relationship sought | Deepen relationship. Requires Disposition +1 or higher. Unlock higher Disposition levels. |
| Impress | Charisma | floor(NPC Cognition / 2) + 1 | Make favourable impression on first meeting. Sets initial Disposition higher than default. |
| Rumour | Charisma | 1 (in tavern/market); 2 (in hostile territory) | Gather one piece of unverified information. Reliability unknown. |
| Negotiate | Attunement | floor(NPC's highest relevant stat / 2) + 1 | Reach informal agreement (below Contest threshold — see §5.7). |

**Disposition shift by degree:**

| Degree | Disposition Change | Additional |
|--------|-------------------|------------|
| Failure | −1 (social misstep; NPC withdraws) | Exposure +1. Cannot attempt same action type with this NPC for remainder of scene. |
| Partial | +0 (contact maintained, no ground gained) | — |
| Success | +1 | One piece of information at the new Disposition's gate level. |
| Overwhelming | +2 | Information + NPC volunteers something unsolicited. +1 Momentum if Belief-aligned. |

**Disposition decay:** Disposition ≥ +3 decays by −1 per season if not maintained (no social action directed at this NPC). Disposition ≤ +2 is stable indefinitely. This reflects the difference between casual acquaintance (stable) and deep trust (requires ongoing investment).

**Disposition ≤ −2 recovery:** Requires a significant narrative event (gift, rescue, shared danger, public vindication) before social actions can be attempted. A character cannot talk their way out of Hostile through Charisma alone.

### §5.3 Sincerity Gate

If a character's stated Belief contradicts genuine engagement with the NPC — the character is instrumentally building trust to extract information — the GM may call a **Sincerity Check** when the player declares a Connect or Converse action.

**Sincerity Check:** Spirit, TN 7, Ob 1.

| Degree | Effect |
|--------|--------|
| Failure | The NPC senses the instrumentality. Disposition does not increase; may decrease by −1. "Something about the way you ask..." |
| Partial | The NPC does not notice, but the character feels the dissonance. No Momentum from this interaction, even if Belief-aligned. |
| Success | The character manages genuine engagement despite instrumental intent. Normal result. |
| Overwhelming | The attempt at instrumentality dissolves — the character discovers genuine interest. Normal result + mark potential Belief revision. |

The Sincerity Gate is not a punishment for strategic play. It is a mechanical expression of the NPC's rendering of the character's intentions. Consciousness renders other consciousnesses; people perceive bad faith. The GM should use this sparingly — only when the player's stated approach is clearly at odds with their character's Beliefs.

### §5.4 Information Gates

The Depth axis and the Disposition axis are parallel information-access systems:

| Access Method | Depth 0 (Surface) | Depth 1 (Settled) | Depth 2 (Hidden) | Depth 3 (Buried) | Depth 4 (Liminal) |
|--------------|-------|--------|--------|--------|---------|
| Exploration | Auto | Cognition ≥ 2 | Cognition ≥ 3 | TS ≥ 10 | TS ≥ 30 |
| Investigation | Auto | Ob 1 | Ob 2 | Ob 3 + TS ≥ 10 | Ob 5 + TS ≥ 30 |
| Socializing | Any Disposition | Disposition +1 | Disposition +2 | Disposition +3 | Disposition +4 |

A character can access the same information through different routes. The NPC who won't share a Buried secret (requires Disposition +3) might be bypassed entirely by a sensitive investigator who Thread-Reads the relevant site (TS ≥ 30, Ob 3). But Thread-Read carries co-movement costs and Exposure that talking to the NPC does not. There is always a trade-off between access methods.

### §5.5 Socializing and Beliefs

When a social action aligns with or challenges a character's stated Belief, mechanical consequences apply:

- **Belief-aligned social success:** +1 Momentum (if below cap 4). Counts as Belief achievement per core engine.
- **Belief-challenging social success:** No Momentum, but the success creates narrative pressure to re-examine the Belief. GM marks as potential Belief revision opportunity.
- **Social action that requires betraying a Belief:** Certainty pressure — GM marks potential Certainty shift. Does not fire automatically; resolves at session end per accumulated pressure.

### §5.6 Knot Integration

At Disposition +5 (Bonded), the NPC becomes a Knot candidate per existing threadwork rules. Forming a Knot with a Bonded NPC follows standard Knot procedures (threadwork_redesign_v25.md §8).

Knot-linked characters gain:
- Automatic Disposition maintenance (no decay)
- +1D on all social actions with the Knot partner
- Shared Composure buffer (per social_contest_system_v2.md §4 Step 6)
- Relational contagion risk (P-12): Thread-shift propagates through Knots

### §5.7 Contest Escalation and Negotiate Boundary

**Negotiate** applies only when: (a) parties share a goal but disagree on method (not formally opposed), or (b) the outcome is not consequential enough for full Contest. If the situation meets Contest initiation conditions (social_contest_system_v2.md §1: "two or more parties with opposed positions AND outcome is uncertain and consequential"), the interaction is a Contest, not a Negotiate. The GM does not offer a choice — the situation's structure determines the mechanic.

When a social action fails at Disposition ≤ 0, or when the NPC has strong reason to resist, the GM may declare **escalation**. The interaction transitions from fieldwork to a formal Contest (social_contest_system_v2.md). This is a Register Shift (stage11 §11.2).

Escalation preserves: current Disposition (applied as starting Conviction Track offset, ±1 per 2 Disposition points, capped at ±2). The relationship does not reset — it intensifies.

### §5.8 Niflhel Social Toolkit Extension

Niflhel cannot participate in Formal or Grand Contests (per social_contest_system_v2.md §9.7). Their fieldwork social toolkit is equally restricted:

- **Available actions:** Read, Connect, Negotiate. One-on-one only (Niflhel cannot operate in group social settings).
- **Unavailable actions:** Impress (no institutional social presence), Rumour (excluded from social networks).
- **Exposure modifier:** +2 Exposure per social action (Niflhel existence is conspicuous; any interaction risks notice).
- **Primary pool:** Attunement (per Contest §9.7 — Niflhel social interactions are Attunement-primary regardless of action type).
- **Thread Insight (TS ≥ 30 only):** Before a Negotiate or Read action, Niflhel with TS ≥ 30 may perform a free Thread-Read (Attunement, Ob = floor(target TS / 30, round up), min 1) to perceive one unstated position. This does not consume a scene action but generates +1 Exposure.

---

## §6 EXPOSURE

Exposure tracks how much attention the character has drawn through their fieldwork activities — both physical (being seen, leaving traces) and social (asking the wrong questions, contacting the wrong people).

### §6.1 Cover (Derived Value)

**Cover = Cognition + most relevant History for concealment/tradecraft.**

Cover determines Exposure thresholds. Higher Cover shifts thresholds upward, paralleling how Endurance determines Stamina capacity and Charisma determines Composure capacity.

| Cover | Noticed | Watched | Compromised |
|-------|---------|---------|-------------|
| 1–4 | 3 | 5 | 7 |
| 5–6 | 4 | 6 | 8 |
| 7–8 | 5 | 7 | 9 |
| 9+ | 6 | 8 | 10 |

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
| Faction support (allied faction uses resources to shield the character) | −2 per season. Costs the faction 1 Wealth or 1 Influence at BG scale. |

### §6.5 Exposure and Church Attention Pool

In territories where the Church has influence (Piety Track ≥ 3 or Church-controlled), Exposure feeds the Church Attention Pool:
- At Watched threshold: +1 Attention Pool in this territory at next Accounting.
- At Compromised threshold: +1 Attention Pool in this territory immediately. (Not +2 — capped at +1 per character per season to prevent runaway TC acceleration.)

**Cap:** A single character's Exposure contributes at most +1 AP per territory per season. Multiple characters' Exposure in the same territory stacks to a maximum of +2 AP per territory per season from fieldwork sources. This prevents fieldwork-heavy campaigns from generating unbounded TC acceleration through the AP → Heresy Investigation → TC pipeline.

---

## §7 DERIVED VALUES SUMMARY

| Value | Formula | Range | Parallel |
|-------|---------|-------|---------|
| Fieldwork Pool | (Primary Attribute × 2) + History bonus | Variable | Combat Pool; Argue Pool |
| Exploration Ob | Depth base + modifiers | 1–10+ | Ob scale per params_core.md |
| Investigation Threshold | GM-set (3/5/8 by scope) | 3–8 | Clock-style progress track |
| Disposition | Starting value ± social actions | −3 to +5 | Asymmetric per-NPC per-PC |
| Cover | Cognition + most relevant History | 2–14 | Composure (Cha + 6); Stamina (End + Hist + 1) |
| Exposure | 0 + accumulation vs Cover-derived thresholds | 0–10+ | Strain toward Composure threshold |

---

## §8 BOARD GAME MODE

At Board Game scale, fieldwork is abstracted into faction-level actions using existing card types plus one new action variant.

### §8.1 New BG Action: Survey (Consul Inward variant)

**Survey** represents a faction directing resources to explore and develop a territory's hidden assets.

- **Card type:** Consul Inward (uses existing card slot — no new card type required).
- **Pool:** Influence.
- **Ob:** (5 − Proximity Rating) + 1. Minimum 1. Askeheim (Proximity 0) → Ob 6. Lowenskyst (Proximity 5) → Ob 1. Territories closer to the Calamity epicentre are harder to survey safely.
- **Effect on Success:** Reveal one undiscovered POI in the territory. POI provides a territory-level bonus:

| POI Category | BG Bonus |
|-------------|----------|
| Resource | Prosperity +1 in this territory |
| Secret | +1D on next military or intelligence action in this territory |
| Remnant | Thread operation Ob −1 in this territory for 2 seasons; Thread Debt token placed |
| Anomaly | RS −1 at this territory immediately; Warden Cooperation +1 eligible (if Warden Emergence active) |

- **Effect on Overwhelming:** Reveal POI + gain +1 Influence (the discovery enhances the faction's knowledge base).
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

**No new card types.** Survey uses Consul Inward. All other fieldwork maps to existing actions. This preserves the BG action economy.

### §8.3 BG Social Interaction

At BG scale, inter-faction relationships are modelled by existing mechanics: Senator Diplomacy (Ob = floor(target Stability/2) + 1) and Standing/Reputation tracks (0-5 each, per clock_registry.md). Disposition is a personal-scale track that does not apply at faction scale. Player-to-player faction relationships are negotiated, not rolled. NPC faction behaviour is governed by NPC artificial intelligence rules in bg_v05.

---

## §9 HYBRID MODE

Following the established hybrid pattern (social_contest_system_v2.md §11):

### §9.1 Hybrid Fieldwork Procedure

1. **BG layer (Strategic Phase):** The faction plays a Survey, Investigate, Govern, or Diplomacy action at strategic scale. Record the degree as a **Fieldwork Offset** (Failure: −1; Partial: +0; Success: +1; Overwhelming: +2). Cap: ±2.
2. **Set TTRPG conditions:** Apply Fieldwork Offset as Ob reduction to the TTRPG fieldwork scene. Minimum Ob 1.
3. **TTRPG personal scene (Personal Phase):** Run exploration, investigation, or social scene per §§3–5 from adjusted Ob. The PC conducts their personal fieldwork with the faction's strategic support (or hindrance, if the faction's action failed).
4. **Resolution (Cascade Phase):** TTRPG scene determines final outcome. Consequences propagate:
   - Exploration: POI discovered → territory bonus applied at Accounting.
   - Investigation: Evidence Track advanced → if threshold reached, faction intelligence updated.
   - Social: NPC Disposition shifted → at high enough Disposition, NPC provides faction-level intelligence or support (Domain Echo).

### §9.2 Hybrid Fieldwork Timing

Fieldwork scenes occur during Personal Phase. If a Strategic Phase order triggers a fieldwork opportunity (e.g., a Tribune Investigate reveals something that demands personal follow-up), the GM may grant a bonus Personal Phase scene for the follow-up. This bonus scene does not extend the seasonal cap — it replaces one of the standard 2–3 Personal Phase scenes.

Per PP-089: Hybrid season phase order is fixed (Strategic Phase first, Personal Phase second). Fieldwork Offsets from Strategic Phase are available immediately for Personal Phase use.

---

## §10 GODOT VIDEO GAME IMPLEMENTATION

### §10.1 Exploration Map Architecture

Each territory is a navigable area containing POI nodes. POI nodes exist in the scene tree at authoring time but are conditionally visible based on the player-character's perception gates.

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

**Perception gate implementation:** Each POI node has an `is_perceivable(character)` method that checks the character's TS, Cognition, Certainty, and relevant Histories against the POI's depth requirements. POI nodes that fail the perception check are not rendered — they do not exist in the character's world.

**Conditional POI gates:** POIs gated by RS band, season, faction control, or prior discovery are evaluated dynamically. A Remnant that becomes perceivable when RS drops below 60 appears in-world at the moment RS crosses the threshold — the world changes because the substrate's intelligibility has changed.

### §10.2 Intelligibility Gradient Visualisation

The Intelligibility Gradient is the system's signature visual feature. The Godot implementation makes the character's rendering capacity visible — not as a filter over a single objective world, but as the character's genuine experiential reality.

**There is no neutral visual layer.** The Thread configuration constitutes a different experiential reality depending on how the observer's consciousness renders it. The Godot implementation uses different visual presentations for different characters, but this is not a "filter" — each visual is the world as that character genuinely inhabits it. The relationship between rendering and world is constitution/experience (Foundations §3.1), not appearance/reality.

| TS Range | Visual Presentation | Implementation |
|----------|---------------------|----------------|
| 0–9 | The world as settled consciousness renders it. Solid, consistent, complete. | Default scene rendering. No post-processing. |
| 10–29 | Something at the edges. Faint disturbance near Thread-adjacent sites. | Shader: subtle vertex displacement + chromatic aberration within POI activation radius. |
| 30–49 | The substrate's structure becomes part of the character's world. Thread filaments visible as a constitutive layer. | Shader: additive blend layer showing Thread mesh. Activated per-POI. |
| 50–69 | Full thread-sight. The substrate is experienced as a dimension of reality, not a hidden layer. | Shader: persistent overlay on all objects within Calamity zones. NPC aura indicators. |
| 70+ | The boundary of the intelligible. What lies beyond is not darkness or void — it is the rendering's dissolution, the edge of what consciousness can constitute. | Shader: dissolve effect at zone boundaries. Particle systems for surfeit-of-being eruptions. Audio: low-frequency rumble. |

**Certainty-dependent constitution:**

The same POI constitutes a different world for characters at different Certainty values. This is not interpretation or opinion — it is the world as given to that consciousness:

- **Certainty 5 (Orthodox):** Thread phenomena constitute a world where demonic intrusion is real. The visual language uses Church iconography — hellfire palette, sin-associated imagery. The character's rendering genuinely produces this world.
- **Certainty 3 (Questioning):** Thread phenomena constitute an ambiguous world. Undefined shimmer, neutral colour shifts. The character's rendering is uncertain — the world itself is uncertain.
- **Certainty 0 (Accepted):** Thread phenomena constitute a world where the substrate is natural. Calm, structural, the fabric of reality experienced directly. Beauty rather than horror.

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

**Inert Knowledge UI:** When a non-sensitive character receives Thread-verified evidence, the journal displays it with a distinctive visual treatment — grayed out, slightly blurred, with a tooltip: "Your character knows this was said, but cannot fully grasp its implications." The player can *read* the information (maintaining player agency) but the character cannot act on it mechanically (maintaining the epistemological barrier).

### §10.4 Disposition and Dialogue

NPC Disposition drives the dialogue system:

**Disposition meter:** Visible on NPC portrait during interaction. Range −3 to +5 displayed as a segmented bar.

**Dialogue option gating:** Conversation options are filtered by current Disposition + character attributes. A Bond-focused dialogue option requiring Disposition +3 simply does not appear at Disposition +1. The player sees what their character could plausibly say in this relationship.

**Social action as dialogue choice:** Each dialogue node can trigger a social action roll. The player selects the approach (Read, Converse, Connect, Impress, Negotiate, Rumour), the game rolls the pool, and the result determines the conversation branch.

**NPC memory:** NPCs remember prior interactions. A failed social action at Disposition −1 that drops Disposition to −2 should be reflected in dialogue — the NPC references the prior misstep. This is not mechanical complexity; it is authored content gated by state.

### §10.5 Dice Visualisation

d10 pool rolls use a visual system consistent across all Valoria mechanics:

| Die Face | Visual | Colour |
|----------|--------|--------|
| 1 | Skull icon or down-arrow | Red |
| 2–6 | Neutral pip | Gray |
| 7–9 | Success checkmark | Blue |
| 10 | Double success + chain icon | Gold |

Net successes displayed prominently. Degree announced with audio cue and screen flash (Failure: dull red; Partial: amber; Success: blue; Overwhelming: gold pulse).

### §10.6 Season and Clock Integration

Fieldwork actions consume in-game time:
- Each exploration/investigation/social scene = 1 time unit.
- Each season has a budget of 4–6 time units (configurable; represents the available daylight/travel time).
- At season end: Accounting Phase fires automatically. Clocks advance. Faction actions resolve.

**Clock HUD:** RS, TC, IP displayed persistently. PI and faction-specific tracks available on faction screen. Exposure displayed per-territory on map overlay.

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
| ED-NEW-01 | POI catalog per territory. Requires cross-reference with geography_design.md and calamity_radiation.md. Each territory needs 2-6 authored POIs across depth levels with conditional availability gates. | P2 |
| ED-NEW-02 | Named NPC starting Dispositions. Requires cross-reference with existing NPC roster (Vaynard, Baralta, Cardinals, Torben, Elske, Klapp, Almud, Maret Uln, Edeyja). Each named NPC needs faction-indexed starting Disposition values. | P2 |
| ED-NEW-03 | Survey action stat assignment confirmed: Influence. Monitor in simulation — if Survey dominates Govern, consider Ob adjustment. | P2 |
| ED-NEW-04 | Exposure ↔ Church Attention Pool interaction. §6.5 caps at +1/character/season and +2/territory/season from fieldwork. Requires simulation to confirm this prevents runaway TC acceleration. | P1 |
| ED-NEW-05 | Negotiate vs Contest boundary defined (§5.7). Confirm this does not create edge cases where players attempt to Negotiate situations that structurally require Contest. | P2 |
| ED-NEW-06 | Godot POI node architecture (§10.1). Requires validation against Valoria-game repo Godot project structure. | P3 |
| ED-NEW-07 | Evidence Track persistence. Confirm tracking overhead is manageable across 10+ session campaigns. | P3 |
| ED-NEW-08 | Disposition decay rate (§5.2: −1/season above +3). Requires simulation to confirm pacing. | P2 |
| ED-NEW-09 | Thread-Read co-movement effects (§4.5). Confirmed: uses threadwork_redesign_v25.md §3.2 co-movement table directly. No separate fieldwork co-movement table. | P3 |
| ED-NEW-10 | Breach encounter (Depth 5) interaction with combat incapacitation and Coherence crisis. Confirm Coherence −1 auto-cost does not stack with other Coherence costs to produce unintended Coherence 0 spiral. | P1 |
| ED-NEW-11 | Pool formula ×2 contradiction. params_core.md (PP-247) says non-doubled; combat_design_v1.md §1 and social_contest_system_v2.md §3 say doubled. Resolve project-wide. Ob calibration depends on resolution. | P1 |
| ED-NEW-12 | Sincerity Gate (§5.3) uses Spirit. Confirm Spirit is not already overloaded as an attribute (currently: Resolve = Spirit; no other mechanical role). | P3 |
| ED-NEW-13 | Desperate Trail (§4.4): 3 consecutive failures threshold triggers TN 8 + doubled Exposure + GM complication. Confirm TN 8 does not make recovery impossible for low-pool investigators (4D at TN 8: P(≥1) ≈ 60%, still viable). Confirm Partial +2 progress compensates for increased difficulty. | P2 |

### Simulation debt

| ID | Description |
|----|-------------|
| SIM-DEBT-FW-01 | Full fieldwork system simulation: Exploration Ob calibration across all 17 territories at varying RS bands. Confirm P(success) for typical pools against Depth 1-5 Obs. Depends on ED-NEW-11 resolution. |
| SIM-DEBT-FW-02 | Evidence Track pacing: simulate a 5-threshold investigation with mixed action types. Confirm completion in 3-5 scenes (target pacing). |
| SIM-DEBT-FW-03 | Disposition economy: simulate 10-session relationship arc from Neutral to Bonded. Confirm pacing requires meaningful investment (not trivially achievable). Include Sincerity Gate impact. |
| SIM-DEBT-FW-04 | Exposure ↔ Attention Pool feedback loop: simulate 4-season fieldwork-heavy campaign. Confirm capped Exposure feed does not generate TC acceleration beyond ±5/season combined cap. |
| SIM-DEBT-FW-05 | Survey action BG balance: confirm Survey does not dominate Consul Govern. Survey should be situationally valuable, not universally optimal. |
| SIM-DEBT-FW-06 | Cover derived value calibration: confirm Cover 3-4 (low) vs Cover 9+ (high) produces meaningfully different Exposure tolerance without making high-Cover characters immune. |

### Propagation required on approval

| File | Change |
|------|--------|
| references/canonical_sources.yaml | Add fieldwork system entry; set canonical doc |
| references/params_fieldwork.md | New params file — extract all mechanical values |
| references/propagation_map.md | Cross-references to combat, contest, threadwork, board game, geography |
| designs/systems/clock_registry.md | Add Exposure track, Evidence Track, Disposition track, Cover derived value |
| references/params_board_game.md | Add Survey action to Standard Action Ob table |
| references/params_core.md | Confirm attribute usage table includes fieldwork roles |
| compilation/v0.14/stage11_scale_transitions.md | Add Fieldwork → Faction handoff rule |
| tests/coverage_matrix.md | Add SIM-DEBT-FW-01 through FW-06 |
