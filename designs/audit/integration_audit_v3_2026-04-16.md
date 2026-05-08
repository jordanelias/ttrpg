Now let me read the other core documents:

I now have a thorough picture of the full system. This is going to be a substantial working document — a proper audit v3 foundation. Let me write it.

---

# VALORIA — Integration Audit v3: Player-World Connection
## Full-System Critique, Gap Registry, Patches, and Scenario Tests
## Date: 2026-04-16
## Scope: All fifteen uploaded documents, read in their entirety. Focus: systems connecting the player character to the game world.

---

# PART 0: AUDIT OF AUDIT V2

Before the new work, what v2 gets right and what it still misses.

**What v2 resolved correctly:**

The Companion specification is now implementable. Combat command timing is correctly placed in the declaration phase. Knot-strain departure model is philosophically and mechanically sound. The three Presence Rules as load-bearing premises (not conclusion) is the document's best structural decision — every player-world connection mechanic either satisfies or violates those three rules, and the test is immediately applicable. The non-standard actor protocols are substantially improved: Ministry, Guilds, Niflhel, and Wardens each now have sufficient mechanical specificity for implementation. The Domain Echo cap clarification (territory-scale Echoes don't count against the ±2 faction-stat cap) resolves the most consequential ambiguity in the integration proposal. The Dialogue Lattice Composure carry (ID-10) and the WR/WC formal definition are both correct and well-specified.

**What v2 still misses:**

Twelve structural problems. They are documented in Part 2 of this audit.

**One matter that supersedes everything else:**

The user has provided a canonical clarification about combat resolution that conflicts with a specific line in combat_v30 and requires a formal patch before any companion command specification can be considered complete. This is addressed first, in Part 1, because everything downstream from combat inherits its resolution model.

---

# PART 1: COMBAT — THE SIMULTANEOUS RESOLUTION SPECIFICATION

## 1.1 The Conflict

The user has established: **all actions resolve simultaneously after declaration. Strike, Feint, and all other actions fire at the same moment in the fiction.**

combat_v30 §2 says:
> "3. Action declarations (simultaneous, blind)"
> "4. Resolution (per priority order within declared actions)"

"Per priority order" implies sequential resolution — Strike resolves, then Feint resolves. This contradicts simultaneous resolution.

Additionally, the Feint rule contains: *"sequential per initiative, not fixed Ob"* — which, read literally, implies Feint resolves in a sequence ordered by initiative. This is also in conflict.

Both conflicts are resolvable without altering the Priority table's existence — only its meaning.

## 1.2 The Resolution: Priority as Effect-Interaction Order, Not Sequencing

**The Priority table does not describe the sequence in which characters act.** It describes the order in which mechanically interacting effects are applied when multiple declared actions produce effects that depend on one another. All actions fire simultaneously in the fiction. When their effects interact, the interaction is resolved using the Priority table as a tiebreaker and a sequencer for effect application.

**The revised Round Structure (replacing §2 Step 4):**

```
Phase 1 — O/D Split Declaration (sequential, not blind):
  1a. Lower first-to-speak holder declares Offence/Defence split.
  1b. Higher first-to-speak holder sees that split, then declares their own.
  [This is unchanged from current rules. Initiative advantage is informational.]

Phase 2 — Action Declaration (simultaneous, blind):
  All parties declare their action type simultaneously.
  Companion commands are written here, alongside the player's O/D declaration.
  Commands are not blind to the companion — they are private tactical communication.
  Commands are not observable by the opponent.

Phase 3 — Reactive Resolution (before simultaneous):
  Rescue declarations processed. Redirect checks resolve.
  Dodge allocations set (full pool → passive Defence for one incoming ranged attack).
  Full Guard allocations set.
  [These must precede Phase 4 because they modify which targets receive which attacks.]

Phase 4 — Simultaneous Resolution (all actions fire at once in the fiction):
  All Strike, Feint, Disarm, Tie Up, Retrieve, Escape, Leap effects apply.
  In the fiction: everything happens at the same moment.
  For mechanical application of interacting effects, use the Priority sequence:
    P1 (Strike): damage applied first. If this incapacitates a Feinting party → Feint expires (PP-293).
    P2 (Feint): pool reduction confirmed if Feinting party survived P1.
    P3 (Disarm, Tie Up, Retrieve): grapple effects applied.
    P4 (Establish Distance, Escape): repositioning confirmed if not Tied Up from P3.
    P5 (Leap): full-round Thread commitment; vulnerability window assessed from P1 Strike results.

Phase 5 — Damage Tracking, Stamina, Initiative Transfer
```

**Why this is correct:**

The simultaneous fiction is preserved — in the narrative, both combatants commit, move, and land at the same moment. The Priority table handles the mechanical question of "what happens when a Strike would kill the Feinting party before the Feint's effect fires?" The answer is Priority 1 resolves first, which means if the Strike incapacitates before the Feint effect applies, the Feint expires. This is not sequential agency — it is simultaneous action with priority-ordered mechanical accounting.

This model matches how v2 correctly resolved the companion command timing: command during Phase 2 (declaration), companion executes during Phase 4 (simultaneous resolution).

## 1.3 The Feint "Sequential per Initiative" Language — Patch

The current Feint description: *"sequential per initiative, not fixed Ob."*

This creates confusion about whether Feint breaks simultaneous resolution. The correct meaning is:

**When both parties declare Feint in the same round**, the Versus rolls are processed in initiative order (higher initiative Feint processed first) because the Feint checks against the opponent's Defence pool, and if both Feints succeed, the question of "whose pool is reduced for the interaction" requires a sequencing rule. The higher initiative Feint processes its result first; the lower initiative Feint then checks against whatever pool the opponent retains.

**Proposed patch to Feint description:**

> **Simultaneous resolution note:** Feint declarations are simultaneous with all other actions. The Versus roll fires in Phase 4 simultaneously with all other effects. If both parties declare Feint in the same round, the Versus rolls are processed in initiative order (not because Feint is a sequential action, but to resolve the interdependency of two pool-reduction checks in the same round). "Sequential per initiative, not fixed Ob" refers to this inter-Feint resolution order only.

## 1.4 Two Strikes — The Mutual Damage Case

Under simultaneous resolution: if both A and B declare Strike, both damage each other. Neither Strike is blocked by the other going "first." The Priority table does not create a scenario where A's Strike prevents B's Strike from resolving — both resolve at Priority 1 simultaneously.

**This is the expected behavior.** It creates the fiction of a brutal exchange where neither party backed down. Both characters can die in the same round. This is simultaneously the most dramatic outcome and the correct one.

**Implication for companion and multi-combatant scenes:** The Fibonacci group bonus (bonus Offence dice for outnumbering) represents coordinated simultaneous pressure, not sequential attacks. This is already correctly framed.

---

# PART 2: NEW GAP REGISTRY

Problems not identified or not resolved by audit v2.

---

**GAP-01: Priority 1 Scene Slate overload has no triage rule**

*Nature:* Structural.

The Scene Slate Priority 1 means "mandatory presentation." In some game states, multiple Priority 1 entries can fire simultaneously: W-05 (Niflhel counter-op) + W-07 (Warden Emergency at WR 3+) + W-10 (Vanguard Deployment at IP 75) could all fire in the same season. The player has 3–4 scene actions at Normal/Hard difficulty. Three Priority 1 entries means the player cannot attend to all of them.

The current design says "selecting one costs a scene action. Not selecting one allows the event to resolve through NPC AI." This is correct as a design principle but there is no formal cap on Priority 1 entries per season, no rule about which NPC AIs handle unresolved P1 entries, and no specification of what "NPC AI handles it" produces as a concrete output.

*Gap:* Maximum simultaneous Priority 1 entries uncapped. NPC AI resolution outputs unspecified.

---

**GAP-02: Dominant Belief theme for Network recognition is undefined**

*Nature:* Mechanical precision gap.

Audit v2 §2.2: Network recognition requires "all four or more NPCs share at least one Conviction alignment with the player's dominant Belief theme (derived from the existing Belief tag structure)."

"Dominant Belief theme" has no formal definition. A player with three Beliefs tagged [NPC: Vaynard][System: Thread], [Faction: RM][Territory: Gransol], and [NPC: Edeyja][System: Warden-Work] has three distinct themes with no single dominant one. The algorithm for deriving "dominant theme" is unspecified.

*Gap:* No algorithm to derive dominant Belief theme from three potentially divergent Beliefs.

---

**GAP-03: Leave scene Composure starting value is undefined for Companion departure**

*Nature:* Mechanical.

Audit v2 §2.1: The companion departure leave scene is "a Social Contest (private negotiation type, Attunement adjudicator, 1 exchange)."

ID-10 in audit v2 resolves Composure carry from a Lattice → Contest escalation. But the companion departure scene is not escalated from a Lattice — it is triggered by the Category B Character Arc trigger C-01. No Lattice session has occurred. The companion has accumulated 3 Belief-contradiction events (each generating +1 Knot strain). There is no specification for what the companion's starting Composure is entering the leave scene. Has the strain from Belief-contradiction events degraded Composure? Is the contest starting at full Composure for both parties?

*Gap:* No starting Composure specification for Character Arc trigger-initiated Contest.

---

**GAP-04: Founded Organization's Domain Action phase placement conflicts with season structure**

*Nature:* Structural/phase order.

Audit v2 §2.3: the Organization's Domain Action "is personal-scale (requires player involvement)."

board_game_v30 / campaign_modes_v30 place Domain Actions in Phase 2 (Strategic Phase), after the Personal Phase (Phase 1). Player_agency_v30 §7.2 confirms this sequence: "Phase 1c — Personal Phase. Phase 2 — Strategic Phase. Domain Actions as existing."

If the Organization's Domain Action requires the player but is executed in Phase 2 (Strategic Phase), where is the player during Phase 2? Logically they are still in the territory where their Personal Phase ended. The action can only fire where the player physically is. This is probably correct — the Organization's Domain Action is constrained to the player's current territory, which is the home territory only if the player ended Phase 1 there. But this isn't stated, and it creates a constraint on Organization play that isn't in audit v2's specification: the player must end Phase 1 in the home territory to execute the Organization's Domain Action.

*Gap:* No specification of where/how the Organization's Domain Action is invoked relative to the player's Phase 1 positioning.

---

**GAP-05: Sincerity Gate applies inconsistently across social actions**

*Nature:* Philosophical coherence / design consistency.

The Sincerity Gate (Spirit TN7 Ob1, ~37% failure on instrumental approaches) fires specifically on Connect actions when intent is instrumental (fieldwork_v30 §5.1, how_to_play §2.1). It does not fire on Impress, Rumour, Interview, Negotiate, or Corroboration.

The gate's philosophical grounding (P-01 inseparability: genuine connection cannot be simulated) implies it should govern any social action where the player's intent is instrumental and the target is a person whose genuine response matters. An instrumental Impress (performing authority to manipulate) is equivalent to an instrumental Connect. An instrumental Corroboration (asking a companion to support you specifically to access their +1D bonus) should fire the gate identically.

The selective application is not a design choice — it's a gap. The investigation proposal acknowledges the Sincerity Gate but doesn't specify which actions it governs. The fieldwork document specifies it only for Connect.

*Gap:* No comprehensive specification of which social actions are Sincerity-gated and why. The current scope (Connect only) is inconsistent with the underlying principle.

---

**GAP-06: Dialogue Lattice escalation trigger is not formally defined**

*Nature:* Blocking mechanical gap.

Audit v2 Part 0, Problem 2 resolves what happens DURING escalation (Composure carry, CT starting position). But it does not define WHEN escalation fires.

The investigation systems proposal describes escalation as a possibility. social_contest_v30 §12 lists "Escalation between social modes" as not yet designed. The escalation trigger is referenced in audit v2 as if it exists ("when the escalation trigger fires during an exploratory conversation") but the trigger itself is never formally defined.

Candidates for the trigger (none formally specified):
- NPC reaches Conviction Wound 1 during a Lattice session
- Player attempts a filter-gated Lattice node for which the NPC's filter is "hostile response" and the topic is a contested one
- NPC's Priority Tree evaluation shifts mid-Lattice (Priority 1 fires, overriding the current Lattice engagement)
- A third party enters the scene mid-Lattice, changing the adjudicator type

*Gap:* Escalation trigger formally undefined. This is a blocking gap because ID-10's Composure carry patch is incomplete without knowing what fires it.

---

**GAP-07: Domain Echo faction-level stacking exploit in multiplayer Board Game mode**

*Nature:* Balance / mechanical.

The Domain Echo cap is ±2 per-season per-stat PER CHARACTER. In multiplayer BG mode, multiple player characters can each contribute ±2 to the same faction stat in the same season. Two characters serving the same faction can jointly produce ±4 on a single stat. Three characters can produce ±6. There is no faction-level cap on stacked personal Echoes.

The ±2 per-character cap was designed to prevent "personal actions shouldn't dominate the faction layer" — but this only prevents any single player from dominating. Coordinated multiplay bypasses this entirely. At high-multiplayer BG play (4 players serving one faction), a single faction stat could shift ±8 from personal Echoes in a single season — enough to move Stability from 3 to max in one season.

*Gap:* No faction-level Echo cap for multiplayer scenarios.

---

**GAP-08: "Witnessed vs. Reported Layer" has no mechanical delivery format**

*Nature:* Implementation gap.

Audit v2 Part 1, Rule 2: "the Domain Echo fires as a stat change... anchored to a witnessed or reported event." The integration proposal correctly identifies the Witnessed/Reported distinction. Neither document specifies:

- Who delivers the Reported layer (faction leader? Named companion? Generic NPC courier?)
- What mechanical format the report takes (Scene Slate entry? Automatic notification? Requires a Research/Interview action to receive?)
- What Priority the report appears at if it is a Scene Slate entry
- Whether the Reported layer can fail (can the player miss a report entirely, learning about the Echo only through territory stat changes?)

This is a videogame implementation gap: the system tells the game engine that a Domain Echo has fired, but not how the player learns about it in a way that satisfies Rule 2 (Every consequence has a scene).

*Gap:* Witnessed/Reported Layer delivery format and Priority are unspecified.

---

**GAP-09: Standing track has no pathway for social degradation outside of Duty failure**

*Nature:* Design gap / completeness.

The Standing track (0–5) advances through Duty success (+1 or +2) and degrades through Duty failure (−1). There is no mechanism for Standing to degrade through social failure with the faction's key NPCs that isn't mediated by a Duty outcome.

A player at Standing 4 can systematically antagonize their faction leader in Social Contests — winning Disposition losses against the leader, arguing against faction priorities, publicly contradicting leadership — without losing a single Standing point, because their Duties are still being completed.

The Disposition system captures the relational cost of these actions (leader's Disposition −1, −2, etc.) but Disposition and Standing are not formally linked. A faction leader at Disposition −3 toward the player still grants them Standing 4 privileges (authority to direct officers, +1 scene action) as long as Duties are being completed.

*Gap:* No coupling between Disposition with faction leader and Standing trajectory. Standing is purely duty-performance-gated, which misrepresents how institutional trust actually works.

---

**GAP-10: Momentum generation sources and cap create systematic waste**

*Nature:* Calibration / mechanical.

Momentum sources across the system, in a single season:
- Belief pursuit: +1 per scene pursuing a Belief (3–5 scenes per season = +3 to +5)
- Belief fulfillment: +2 one-time
- Companion Belief fulfillment: +2 Momentum to player
- Rescue success: +2 (PP-406)
- Social Contest Total Victory win: +1

The cap is 4. A moderately active season (2 Belief-pursuit scenes + 1 Rescue success) generates +4, hitting the cap immediately. Any additional sources are wasted.

More critically: a Belief fulfillment season (+2 one-time) combined with two Belief-pursuit scenes (+2) generates +4 in the first two scenes — all remaining scene actions produce zero Momentum. The cap doesn't create strategic decisions about when to spend Momentum; it creates wasted generation on any active season.

*Gap:* Momentum cap at 4 is too low for the generation rates across a multi-scene season. Either the cap needs to scale with scene count, or some generation sources need to be converted from flat Momentum to other effects.

---

**GAP-11: Evidence Track "Let It Ride" and the 2-scene-action complex scene**

*Nature:* Interaction gap.

fieldwork_v30 §2.2: "Failed fieldwork action on specific target cannot be reattempted same scene." A scene can consume 2 scene actions (for complex/extended scenes). If a player spends 2 scene actions on a complex investigation scene and both primary actions fail (Let It Ride blocks reattempt on the same target), they have spent 2 scene actions from a budget of 3–4 for zero progress. The only recovery is "circumstances changed" — which is undefined.

*Gap:* "Circumstances changed" as the Let It Ride reset condition is undefined. In a 2-scene-action complex scene, a Let It Ride failure doubles the cost of mechanical failure beyond what the scene budget assumes.

---

**GAP-12: WR 1 advancement condition uses "Proximity Rating" which is not defined in fieldwork_v30**

*Nature:* Cross-document terminology conflict.

Audit v2 §3.4, WR 1 advancement: "Player character survives 1 scene in a territory with Calamity Radiation (Proximity Rating ≤ 2) while having TS ≥ 15."

fieldwork_v30 §1 Depth Axis Ob modifiers: "Calamity radiation: +1 Ob per MS band below 60 at current Proximity Rating."

Two different systems use "Proximity Rating." The fieldwork version uses MS (Mending Stability) bands as the actual scaling mechanism. The WR advancement condition uses "Proximity Rating ≤ 2" as a threshold without defining the scale or how it maps to MS bands.

Geography_design.md (referenced but 
