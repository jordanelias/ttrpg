# VALORIA STRESS TESTS — BATCH 09
## Edge Cells + Temporal Coverage Sweep
**Executed:** 2026-03-27 | **Model:** Opus 4.6 | **Skill:** valoria-simulator
**Purpose:** Close remaining 7 cell gaps; sweep PAST/FUT temporal coverage for 38/27 mechanics.

---

## T-B9-01 — PULLING: EDGE CASES (M-016)
**Coverage:** M-016, M-009, M-010, M-021
**Mode:** TTRPG | **Temporal:** PRES/CROSS | **Tracks:** TD,TS,TT,CERT | **Factions:** Crown,Varfell | **NPCs:** Almud,Vaynard | **Archetypes:** Practitioner
**Cells filled:** M-016 Edge

### Mode D — Edge Cases (Exhaustive)

**Boundary — Pull at Ob 10 (maximum):**
Ob 10 Pull: altering foundational causal structure (e.g., erasing a faction's founding event).
Pool: TS/2, TN7. At TS 60 (high-tier): 30D, Ob 10.
P(≥10 net, 30D, TN7): expected net 30 × 0.33 = 9.9. P(≥10) ≈ 45%.
Even the most capable practitioners have ~45% success on Ob 10 Pulls. Below TS 60: near-impossible.
**Ob 10 Pull is appropriately rare and high-stakes.** No degenerate case here.

**Boundary — Pull at TD 20 (terminal):**
At TD 20: Coherence collapse. Practitioner cannot perform Thread operations at all.
Pull at TD 20 is therefore impossible — the mechanic is gated by Coherence collapse before TD 20 is reachable in practice. **Natural ceiling confirmed.**

**Cascade — Pulling a connection shared by multiple entities:**
A Thread connection may link more than two entities (e.g., a covenant bond between three faction leaders). Pulling this connection:
- Affects all entities connected by it simultaneously
- Co-movement fires for each connection (multiple Certainty checks, multiple TT increments)
- No rule specifies whether the practitioner rolls once (targeting the connection) or once per entity
**GAP: Multi-entity connection Pull resolution undefined.** If once: one roll, all entities affected equally. If per entity: pool split (like defence dice), practitioner must divide TS pool across targets. Massive functional difference.
**Proposed fix (extends PP-026 further):** Add: "Pulling a connection shared by N entities uses one roll targeting the connection itself. All entities connected are affected by the outcome. TT cost applies once per Pull, not once per entity."

**Cascade — Pull chain reaction:**
Pulling connection A → connection A was load-bearing for connection B → connection B destabilises.
Automatic cascade: Pulling one connection can cause adjacent connections to loosen.
Mechanic: on Overwhelming Pull, one adjacent connection also shifts (GM selection). On standard Success: only target connection shifts.
This is already implicit in the system but not explicitly stated.
**Finding: Overwhelming Pull should have a cascade clause.** No current rule for it.

**Regression — Pull on a Pull:**
A practitioner attempts to Pull a connection that was itself created by a prior Pull.
The artificial connection is weaker (Knot-adjacent). Roll: Ob −1 (easier to alter something already altered).
But: the prior Pull may have left Residue. Residue +1 Ob. Net: Ob modifier = 0 (cancel out).
**No regression loop here.** Pull on Pull doesn't create infinite recursion. ✓

**Deadlock — All connections at a location are Pulled:**
A location where all Thread connections have been Pulled (all relationships altered): 
What remains? A Thread-void location. This is effectively a Gap (M-025).
**Mechanical implication: exhaustive Pulling of a location creates a Gap.** No rule states this explicitly, but it's the logical consequence of the mechanics.
**Proposed fix:** Add: "When all significant Thread connections at a location are successfully Pulled or Dissolved, the location becomes a Gap (rating 1). This is automatic — no additional roll required."

**Optimal play — Pulling as faction stat manipulation:**
Per F-B8-01 and PP-061: successful Pull on social relationship reduces target Circles −1.
A dedicated practitioner campaign (Almud, TS 8):
- 4 Pull attempts/season at P(success) ≈ 25% each
- Expected successful Pulls: 1/season
- Church Circles (Himlensendt) degraded by −1/season
- After 3 seasons: Himlensendt Circles 3 → 0 (cannot call on institutional support)
**Pulling as a slow-burn strategic campaign is viable but requires multiple seasons.** Not game-breaking; appropriately long-horizon.

**F-B9-01** (P2) — Multi-entity connection Pull undefined. One roll vs per-entity roll is a major functional difference. Proposed fix above.
**F-B9-02** (P3) — Overwhelming Pull cascade clause absent. On Overwhelming, an adjacent connection should also shift. Add as optional GM trigger.
**F-B9-03** (P3) — Exhaustive Pulling = Gap creation. Logical consequence not documented. Add explicit statement.

---

## T-B9-02 — COHERENCE TRACK: EDGE CASES (M-021)
**Coverage:** M-021, M-016, M-013, M-020
**Mode:** TTRPG | **Temporal:** CROSS | **Tracks:** TD,ThS,CERT,TT | **Factions:** Niflhel | **NPCs:** Vaynard | **Archetypes:** Practitioner
**Cells filled:** M-021 Edge

### Mode D — Edge Cases

**Boundary — Coherence 0:**
At Coherence 0: Monstrous Entity transition threshold.
What happens mechanically?
- Character is no longer a "practitioner" in the game-mechanical sense
- They become a Thread-active entity with no human social functioning
- Combat stats: retained but ThS radiation makes them a threat to all nearby characters
- Faction standing: all factions treat as hostile entity (no Circles, no Domain Action participation)
- Recovery: no mechanic found (consistent with F-B8-02 — Coherence is one-way)
**Coherence 0 = effective character death (social/narrative death, not physical).** The character continues to exist but is unplayable in their current form.

**Is there a Coherence 0 → ME transition procedure?** No formal procedure found. The transition from "degraded practitioner" to "Monstrous Entity" happens at Coherence 0 but the mechanics of what an ME does as a character (player or NPC) are not defined.
**F-B9-04 (P1) — ME transition procedure absent.** At Coherence 0, what is the mechanical state of the character? Can players continue to play them? What are their stats? Monstrous Entities appear in T-B8-05 as NPCs/threats but their character mechanics are undefined.
**Proposed fix:** Add ME character state: "At Coherence 0, the character enters the Monstrous state. They retain their TS, TD, and physical stats. They lose: Circles, Beliefs (replaced by Thread-driven compulsions), and social accessibility. They gain: +5D on all Thread operations; radiate ME effects (CE accumulation, ThS elevation) on all nearby characters; cannot communicate in human language below Intelligibility 3. A player may continue playing a Monstrous character if the group consents — this is an advanced arc, not a game-ending event."

**Boundary — Coherence 1:**
At Coherence 1 (one step from ME threshold):
- Social communication severely impaired
- Thread operations: still functional (no Thread penalty from Coherence alone)
- Detection: ThS radiation elevated; Inquisitor CE accumulation accelerated
- Recovery: +1 Coherence via Restoration Community Weaving (PP-062) — but requires community access and successful collective op

**At Coherence 1, recovery via PP-062 requires:**
1. Access to Restoration community (narrative prerequisite)
2. Successful Community Weaving (Ob 2+, pool depends on community TS)
3. Multiple sessions of engagement (each successful Weaving = +1 Coherence)
**Recovery from Coherence 1 requires 1 successful Weaving. From scratch if starting at Coherence 10 dropped to 1: 9 successful Weavings to recover fully.** At 1/season with good circumstances: 9 seasons. Very long-arc recovery. This is appropriate for the level of degradation.

**Cascade — Coherence degradation + ThS elevation feedback:**
At Coherence 3: practitioner radiates elevated ThS. This attracts Inquisitor attention (CE accumulation, investigation triggers).
Inquisitor investigation: CE +1 on practitioner. TS growth check for practitioner (CE accumulation from investigation? Yes — being investigated is Thread-adjacent exposure).
Actually: the practitioner already has TS. CE track is for non-practitioners. Investigations don't add CE to the practitioner being investigated.
But: Inquisitor's TS grows (via CE from proximity to practitioner). At TS 5: Inquisitor perceives Thread passively. More effective at investigation. **The feedback loop is: degraded practitioner → Inquisitor gains TS → Inquisitor becomes more effective → harder for practitioner to operate → more failed ops → more Coherence degradation.** Confirmed vicious cycle.

**Deadlock — Coherence degraded to 2, no Restoration community accessible:**
At Coherence 2, no community available:
- Cannot recover Coherence (no mechanic without community)
- Every Thread op risks further degradation (automatic at TD 10+)
- Cannot reduce TD without ops (wait season for TD −3 per PP-001)
- During wait season: Coherence stable (no ops = no degradation)
**The only path:** stop operating, reduce TD via rest, hope to access a Restoration community before plot forces Thread operation. This is a genuine narrative deadlock if plot requires Thread operation. The mechanic correctly produces this tension — a degraded practitioner in a crisis must choose between helping (risking Coherence 0) and protecting themselves.

**Incoherence — Coherence 0 + TD 20 simultaneously:**
Coherence 0 = ME threshold. TD 20 = Coherence collapse from operations.
Can both reach terminal simultaneously? TD 20 triggers Coherence −1 per op (automatic at TD 10+). If Coherence was at 1 when TD hits 10: Coherence → 0 on the very next Thread op. So yes — simultaneous terminal state is reachable in ~10–15 Thread operations from a mid-game state.
**This is the designed tragedy arc for over-extended practitioners.**

**F-B9-05** (P3) — Recovery time from deep Coherence degradation is campaign-length. From Coherence 1 to 10 via PP-062: 9 successful Weavings minimum. Document as long-arc commitment in Restoration community guidance.

---

## T-B9-03 — SEASONAL ACCOUNTING: ISOLATION + EDGE (M-038)
**Coverage:** M-038, M-034, M-031, M-035
**Mode:** TTRPG/BG | **Temporal:** FUT/CROSS | **Tracks:** FSTAT,TC,TT,IP | **Factions:** All | **NPCs:** — | **Archetypes:** Faction Leader
**Cells filled:** M-038 Isolation, Edge

### Mode A — Isolation (M-038)

**Seasonal Accounting in pure isolation:**
What does the mechanic do when no other faction mechanics fire?

Base procedure:
1. Each faction pays upkeep (stats sum ÷ 6, rounded down, in Wealth).
2. Each faction gains income (Wealth stat ÷ 2, rounded down, per season — base income).
3. Net Wealth change = income − upkeep.
4. Anti-death-spiral floor check.

**Wait — income mechanic not previously isolated.** Is there a baseline income?
Checking batch data: no explicit income mechanic found in prior tests. All Wealth gain was from Domain Actions.
**If there is no baseline income, Seasonal Accounting is purely a drain mechanic.** All factions lose Wealth each season unless they take Economic Domain Actions.

**Testing assumption: no baseline income (Domain Actions only).**
At this assumption: every faction's Wealth decreases by upkeep each season without Domain Action income.
Church: −5 Wealth/season (per T-B7-07). Without tithe (PP-032), Wealth 0 in season 1.
Guilds (Wealth 8): −5/season. Wealth 8 → 3 after season 1 (if no Economic Domain Action).
**All factions need at least one successful Economic Domain Action per season to sustain Wealth.** This is a strong constraint that makes Economic Domain Actions mandatory (not optional) for faction survival.

**F83 — anti-death-spiral floor confirmation:**
At Wealth ≤ 2 (low): recovery action Ob raised to 4.
Standard Economic Domain Action: Ob 2. At Wealth ≤ 2: Ob 4.
For Church (Mandate 7D post-Synod, Ob 4): P(success) ≈ 55%. Better odds than previously noted.
For Revolution (Mandate 3D, Ob 4): P(success) ≈ 15%. **Revolution cannot recover from Wealth ≤ 2.** The anti-death-spiral floor is a death spiral floor for low-Mandate factions.
**F83 confirmed: the mechanism inverts intent for factions with Mandate ≤ 4.** Above Mandate 5, the floor is survivable. Below Mandate 5, it's a trap.

**Proposed fix (PP-003 extension / new PP-069):** 
The anti-death-spiral floor should use the faction's *highest* available stat as the pool, not the stat relevant to the action type. A faction with low Wealth but high Influence could leverage political capital for economic recovery. Currently: pool = economic stat only.
**New PP-069:** "Anti-death-spiral recovery actions may use any faction stat as the pool (player choice), representing the faction drawing on their strongest resource to survive. The Ob floor remains 4."

### Mode D — Edge Cases (M-038)

**Edge 1 — All factions simultaneously at Wealth 0:**
Mass Wealth collapse: all factions hit Wealth 0 in same season (possible after prolonged war or Thread crisis elevating upkeep costs).
Per PP-004: Wealth 0 = Domain Action funding constraint.
Per PP-032: Church tithe partially protects Church (Wealth +2/season).
All factions except Church: cannot fund Domain Actions.
**This is a campaign-ending scenario unless there's an emergency mechanism.** The world grinds to a halt — no political action, no military action, no covert action.
No emergency mechanic found. **F-B9-06 (P2): No faction economic emergency mechanic.** All-faction Wealth collapse should trigger something (emergency Parliament session, IP spike, faction collapse cascade).
**Proposed fix (PP-070):** "If 3+ factions simultaneously reach Wealth 0, an Economic Crisis is declared: all clocks pause for 1 season while factions attempt recovery. TT −2 (crisis focus reduces Thread tension). IP +5 (political crisis from economic collapse). Each faction may attempt one Emergency Resource action at Ob 3 using any stat."

**Edge 2 — Seasonal Accounting with active war:**
During military conflict: upkeep increases (Military stat × 0.5 additional Wealth drain per season of active combat).
At Military 5 active combat: additional Wealth drain = 2–3/season.
Combined with base upkeep: total drain ≈ 7–8 Wealth/season.
Even Hafenmark (Wealth 8) is depleted to 0 within 2 seasons of sustained warfare.
**War is economically decisive.** Factions that initiate war without Wealth reserves will collapse economically within 2 seasons. This is historically realistic and mechanically interesting.

**Edge 3 — Seasonal Accounting triggering TC (Church tithe at high TC):**
At TC > 75: Church upkeep increases (institutional expansion costs more). Additional upkeep +2.
Church upkeep: 5 (base) + 2 (TC > 75) = 7/season. With tithe income +2: net −5/season.
**Even with tithe, Church deteriorates economically at high TC.** This is a natural check on Church expansion — running the Theocracy is expensive.

**F-B9-07** (P2) — War upkeep cost not explicitly specified. The additional Military drain during active combat is reconstructed from context but not explicitly stated in the rules. Add: "During a season of active military conflict, each belligerent faction pays additional upkeep equal to Military stat ÷ 2 (rounded up) in Wealth."

---

## T-B9-04 — MONSTROUS ENTITIES: EDGE CASES (M-026)
**Coverage:** M-026, M-021, M-049, M-051
**Mode:** TTRPG/BG | **Temporal:** CROSS | **Tracks:** CE,TS,CERT,TC,ThS | **Factions:** Church,Varfell,Niflhel | **NPCs:** Vaynard | **Archetypes:** Practitioner,Inquisitor,Devout Character
**Cells filled:** M-026 Edge

### Mode D — Edge Cases

**Boundary — ME at Coherence 0 in a city:**
A Monstrous Entity (Coherence 0, TS 20+) loose in a populated city.
Zone-level ME effect (PP-065): CE +1/scene to all in zone.
City = multiple zones. ME moves through zones.
Over one season (10 sessions): ME could affect 10–15 zones. Each zone: all inhabitants CE +1.
At CE 3 (TS growth threshold): any character in those zones for 3 scenes triggers TS growth check.
**A single ME loose in a city for one season could trigger TS growth checks in hundreds of NPCs.** This is the canonical "the Thread is awakening in the population" scenario.
TC consequence: each TS growth check in a Devout population generates a Dissonance Mark → confirmed Thread manifestation → TC +0.5 (rounded: every 2 growth events = TC +1). 20 growth events in a city: TC +10 in one season.
**ME in a city = TC crisis accelerant.** The Church cannot ignore this.

**Boundary — ME at BG scale (territory):**
Per PP-065: ME in BG mode affects entire territory.
Territory Stability −1 per season of ME presence (population disrupted).
Territory Intel check by controlling faction: automatically succeeds (territory-level event is visible).
**In BG mode, MEs are territory-level events, not personal-scale.** They affect faction stats directly, not individual character mechanics.

**Cascade — Multiple MEs:**
Three MEs active simultaneously in different territories:
TT +3/season (each ME = ambient Thread activity in their territory).
TC: Church must investigate each ME (TC +1 per confirmed investigation per T-B8-07).
At 3 MEs: TC +3/season from investigations alone.
Combined with Church Domain Actions: TC could advance 5–7/season. From TC 45 to TC 50 in 1 season.
**Multiple MEs create a TC cascade that overwhelms normal suppression.** At 4+ simultaneous MEs, TC crosses thresholds faster than any faction can respond.

**Regression — Investigating an ME who was formerly a PC:**
An Inquisitor investigates a Monstrous Entity that was previously a player character.
The ME retains Thread connections to prior Circles/Knots. These connections are now Thread-distorted.
Investigating the ME's connections via Diagnosis: reveals the PC's prior history (Circles, Thread operations performed).
**An ME is a living record of their practitioner history, readable by any diagnostician.** This is not a regression loop — but it's a significant privacy violation for practitioners who fall into ME transition.

**Degenerate — ME with TS 100:**
A theoretical ME at Coherence 0, TS 100 (maximum Thread capability, no social functioning):
Thread operations: 50D pool. TN7. Any Op with Ob ≤ 16 is automatic success (expected net 50 × 0.33 = 16.5).
ThS radiation: ThS +20/scene for all nearby. After 1 scene: ThS in zone = 20+ → any TS ≥ 1 character auto-detects.
**TS 100 ME is a world-level crisis.** No faction can operate normally in their territory. The Church would mobilize everything available.
This is an edge case unlikely in normal play but defines the upper bound of the ME threat.

**F-B9-08** (P1) — ME transition procedure absent (same as F-B9-04 — confirming P1 severity). Coherence 0 has no defined mechanical state. This is the same finding, confirmed from multiple test angles. The ME character sheet is completely absent.

**F-B9-09** (P2) — City-scale ME generates TC crisis in one season. A single ME loose in a city = TC +10 in one season. This should be documented as a GM calibration note — ME containment is not optional; it's an existential Church priority.

---

## T-B9-05 — RISKBREAKERS: EDGE CASES (M-050)
**Coverage:** M-050, M-011, M-034, M-056
**Mode:** TTRPG/HYB | **Temporal:** CROSS | **Tracks:** DD,TC,FSTAT,CE | **Factions:** Crown,Church,Niflhel | **NPCs:** — | **Archetypes:** Riskbreaker,Faction Leader
**Cells filled:** M-050 Edge

### Mode D — Edge Cases

**Boundary — DD 10 (terminal):**
At DD 10: Riskbreaker is burned. Cover blown, faction takes reputation hit.
Reputation hit: controlling faction Circles in target faction −2 AND IP +2 (diplomatic incident).
**Is there a grace period?** No mechanic found. DD 10 is immediate — the Riskbreaker is compromised and the damage is instantaneous.
**Question: can a Riskbreaker extract before DD 10?** Extract procedure: Riskbreaker withdraws before DD 10, sacrificing remaining operational capacity. No DD cost for withdrawal itself; cover remains intact but the Riskbreaker is "burned" (DD reset to 0 on a new identity, but original cover is retired). No rule for this. **GAP: Riskbreaker voluntary extraction not defined.**
**Proposed fix (PP-064 extension):** "A Riskbreaker may voluntarily extract at any DD level. On extraction: DD resets to 0, cover identity is retired (Circles → 0), faction loses the Riskbreaker's intelligence for one season. No IP penalty. Extraction is preferable to DD 10 burn."

**Boundary — DD 0 (clean slate):**
At DD 0: Riskbreaker has full operational capacity. First operation: DD +2 (standard) or +3 (Destabilisation).
No mechanic for maintaining DD 0 between seasons. DD does not naturally decay; it only resets on burn or extraction (proposed). **A Riskbreaker who completes one operation and then rests still has DD 2 next season.** There is no "lying low" mechanic that reduces DD below the accumulated level.
**GAP: No DD natural decay mechanic.** A single operation leaves permanent trace. Proposed fix: Add seasonal DD decay. "At season end, if the Riskbreaker performed no operations this season: DD −1 (lying low reduces accumulated exposure). Minimum DD after decay: 0."

**Cascade — Multiple Riskbreakers compromised simultaneously:**
Two Riskbreakers burned in the same season: IP +4, controlling faction loses all covert capability in target faction.
If Niflhel burns both Riskbreakers in same season: Niflhel has no covert operation capability until replacement (PP-064: one/season to recruit).
**Niflhel is effectively neutralised for 2+ seasons after double-burn.** This is a catastrophic outcome requiring a 2-season rebuild.

**Optimal play — Riskbreaker rotation:**
With PP-064 (one new Riskbreaker per season, Wealth 2):
Rotating 3 Riskbreakers in parallel: each operates for 1 season (DD 0 → 2–5), then rests (DD decays −1/season with proposed decay mechanic) while others operate.
At 3 active Riskbreakers with rotation: sustained covert operation indefinitely.
Wealth cost: 2 Wealth/season to maintain replacement pipeline.
**This rotation strategy is the dominant covert play pattern** — immediately obvious once the mechanics are understood.
**Design note:** The rotation dominance may be intentional (it creates a meaningful Wealth investment for covert capability) or unintentional (it trivialises the DD burn mechanic with enough Wealth). At Niflhel Wealth 5: rotation costs 2/5 of Wealth per season — sustainable but meaningful.

**Incoherence — Riskbreaker with Devout Constraint:**
A Devout character as a Riskbreaker: Devout Constraint blocks Thread perception but Riskbreaker doesn't require Thread operations. DD mechanics function normally. Cover identity: a Devout Riskbreaker's genuine religious identity is actually excellent cover (difficult to suspect). 
**Devout Riskbreaker: mechanically viable. Circles (religious cover) 5 + genuine Devout status = Ob +2 for investigators to expose.** Interesting character archetype — no mechanical gap here.

**F-B9-10** (P2) — Voluntary Riskbreaker extraction undefined. No mechanic for clean withdrawal before DD 10. Proposed fix above (PP-064 extension).
**F-B9-11** (P2) — DD does not naturally decay. Accumulated exposure is permanent unless extracted/burned. Add seasonal decay: DD −1/season of no operations.

---

## T-B9-06 — DEVOUT CONSTRAINT: SCENARIO (M-051)
**Coverage:** M-051, M-008, M-031, M-037, M-049
**Mode:** TTRPG | **Temporal:** PAST/PRES/CROSS | **Tracks:** TC,CERT,CE,TS | **Factions:** Church,Hafenmark | **NPCs:** Baralta,Himlensendt,Klapp | **Archetypes:** Devout Character,Faction Leader,Inquisitor
**Cells filled:** M-051 Scenario

### Mode C — Full Scenario

**Setup:** Baralta (Devout, constitutional legalist) undergoes the Devout faith crisis arc over three scenes. This tests the full M-051 → M-008 → Dissonance Mark accumulation → faith crisis sequence.

**Initial State:**
```
Baralta — TS 2, CE 2, Composure (Poise) 7, Spirit 4, Coord 3
  Beliefs: "Divine authority cannot supersede the Compiled Constitution" (active)
  Dissonance Marks: 0
  Devout Constraint: active

Klapp (Inquisitor) — TS 5 (acquired), CE 4
TC 50 | TT 33
```

#### Scene 1 — Witnessing Thread Manifestation (PAST temporal)

Baralta encounters an Einhir site while surveying disputed territory.
The site's elevated ThS (ThS 18) causes physical manifestations visible to all.
Baralta TS 2: no Thread perception. Sees physical effects (light distortion, inexplicable sound).
Devout interpretation: divine presence. Baralta gains Dissonance Mark 1 (unexplained phenomenon confirms faith AND creates cognitive dissonance with constitutional worldview).

**CE accumulation:** Baralta CE 2 + 1 (Einhir site scene) = CE 3. TS growth check triggers.
Spirit 4D, TN7, Ob 2 → P(≥2 net) ≈ 63%.
Most likely: growth check succeeds. TS 2 → 5 (dormant).

**Devout Constraint at TS 5:** Constraint still active. But TS 5 = Dormant perception.
**The Constraint is now in tension with nascent Thread awareness.** Baralta is beginning to perceive something she cannot name. Each perception creates another Dissonance Mark.

**Scene 1 State Delta:**
```
Baralta — TS 5 (was 2), CE 3, Dissonance Marks: 1
TC: unchanged | TT: unchanged
```

**Proposed fix relevance:** PP-067 (intentional TS development) is not the path here — Baralta's growth is involuntary. The CE 3 threshold fires automatically. This is the designed path for Devout characters.

#### Scene 2 — Klapp's Investigation (PRES temporal)

Klapp investigates the Einhir site. Baralta is present as the constitutional authority on the territory.
Klapp's investigation: Intel 5 + TS 5 = 7D (Intel + Thread-awareness contribution), Ob 2. P(success) ≈ 82%.
Success: Klapp confirms Thread activity. CE +1 to all in scene.
Baralta CE 3 → 4. CE 4: second TS growth check (PP-017). Spirit 4D, TN7, Ob 2 → 63% success.
If succeeds: TS 5 → 8. Baralta now has passive awareness of strong Thread events.

**Devout Constraint conflict:**
Baralta's TS 8: passive awareness begins. She perceives something at the investigation site.
Devout Constraint: blocks her from acknowledging this as Thread activity.
**Dissonance: she perceives Thread activity, cannot name it as such, and must interpret it as divine intervention.**
Dissonance Mark 2 accumulates.

**Klapp's report to Church:** Confirmed Thread activity = TC +1 (→ 51). Synod already active; no new threshold.
Klapp's recommendation: territory should come under Church Inquisition jurisdiction.
Baralta's constitutional position: the Compiled Constitution governs territorial jurisdiction, not Church authority.
**M-037 (Grand Debate) trigger:** Baralta challenges Klapp's jurisdictional claim.
This is a PRES action — the constitutional dispute is in the present.

**Scene 2 State Delta:**
```
Baralta — TS 8 (was 5), CE 4, Dissonance Marks: 2
Klapp CE: 4 → 5 (transformation threshold) → Spirit 3D, Ob 2 → 55% chance TS 5 involuntary
TC: 51 | TT: 33
```

#### Scene 3 — Faith Crisis (CROSS temporal — past informs present)

Baralta reviews her family's historical records (PAST orientation): her ancestor witnessed the original Thread events that predated the Church. The records confirm that the constitutional law she defends was written *with knowledge of Thread phenomena* — the founders knew.

This is a PAST-oriented discovery, not a Thread operation. Historical evidence.
**Dissonance Mark 3:** Baralta's constitutional faith is now complicated — the Constitution accommodated Thread reality, which means the Church's claim that Thread is heresy contradicts the Constitution's own founding context.

**Faith crisis trigger at 3+ Dissonance Marks:**
Devout Constraint weakens. TS growth check fires regardless of Constraint (Constraint override).
Spirit 4D, TN7, Ob 1 (weakened Constraint = lower Ob on this check) → P(≥1 net) ≈ 97%.
Baralta TS: 8 → 12 (awareness threshold crossed). Passive Thread perception becomes active.

**Belief update (M-004 CP award):**
Baralta's Belief "Divine authority cannot supersede the Compiled Constitution" is *affirmed* but deepened — her discovery shows the Constitution already incorporated Thread reality.
CP award: 2 CP (Belief challenged and deepened, not broken).

**New belief formation:**
Baralta may now hold: "The Compiled Constitution already encompasses Thread phenomena — the Church's heresy doctrine violates the Constitution itself."
This is a new Belief, formed from the faith crisis arc. It's a direct consequence of M-051 + M-003 (Histories/records) + M-004 (CP award).

**TC interaction:**
If Baralta publicly advocates this position: TC −2 (undermines Church theological authority claim). IP +3 (constitutional crisis).
**The faith crisis arc transforms Baralta from a passive Church-restrictor to an active Thread-constitutional advocate.** Mechanically coherent character arc.

**Scene 3 State Delta:**
```
Baralta — TS 12 (awakened), CE 4, Dissonance Marks: 3
  Devout Constraint: broken
  Beliefs: updated to Thread-constitutional advocacy
  CP gained: 2
TC: 51 (could go to 49 if Baralta advocates publicly) | TT: 33
```

### Scenario Findings

**F-B9-12** (P3) — Devout faith crisis arc produces a mechanically complete character transformation over 3 scenes. No design issues — the mechanics work as intended. Document as the canonical Devout character arc in character creation guidance.

**F-B9-13** (P2) — Dissonance Mark accumulation rate is high at Einhir sites. Baralta accumulates 3 Dissonance Marks in 3 scenes, triggering faith crisis faster than might be dramatically appropriate for a long campaign. Consider: "Dissonance Marks require at least one scene between accumulations (cannot fire twice in the same scene)." This paces the arc across more sessions.

---

## T-B9-07 — NIFLHEL DESTABILISATION: EDGE CASES (M-056)
**Coverage:** M-056, M-034, M-050, M-031, M-033
**Mode:** BG/HYB | **Temporal:** FUT | **Tracks:** FSTAT,TC,TT,DD,IP | **Factions:** Niflhel,Church,Crown,Revolution | **NPCs:** — | **Archetypes:** Riskbreaker,Faction Leader
**Cells filled:** M-056 Edge

### Mode D — Edge Cases

**Boundary — Destabilisation at Church Stability 0:**
Church Stability 0: faction Crisis (PP-004). TC braking (PP-043: Stability 0 suspends TC gains).
At Stability 0: Niflhel's primary TC-suppression goal is achieved via PP-043 mechanism — Church cannot drive TC while in Crisis.
**But:** Church Crisis also removes Church from Parliament and Grand Debate. PI drops. IP increases.
If Niflhel crashes Church to Stability 0: they may inadvertently destabilise Parliament itself. IP spike could trigger Parliament crisis, which is not Niflhel's goal (they want controllable instability, not collapse).
**Niflhel has an optimal Stability target:** suppress Church Stability to 2–3 (TC braking engaged, but Church still functional enough to maintain Parliament order). Full collapse is counterproductive.

**Cascade — Destabilisation + TC interaction at high TC:**
At TC 75: Church gains +2D on all defensive actions (institutional authority peak).
Destabilisation at TC 75: Church defends with Stability 8 + TC authority bonus.
Effective Ob for Destabilisation: Stability ÷ 3 + 1 (TC bonus) = Ob 4.
Niflhel Intel 7D, TN7, Ob 4 → P(success) ≈ 40%. Still possible but harder.
**TC elevation actively defends against Niflhel.** High TC = Church is harder to destabilise. This is the catch-22: Niflhel must destabilise Church to prevent TC from rising, but high TC makes Church harder to destabilise.

**Cascade — Church drives TC while being destabilised:**
Church takes Domain Action to drive TC (+3) in the same season Niflhel succeeds Destabilisation (−1).
Net: TC +2. Niflhel's action reduces the rate of TC growth but cannot stop it.
**Over 10 seasons with Niflhel operating at full capacity (3 Riskbreakers, rotation per PP-064):**
- Niflhel expected TC reduction: ~1.5/season (60% success × 1 Destab/season × 3 Riskbreakers with rotation → max 3 Destab ops/season → expected TC reduction 1.5–2/season)
- Church expected TC gain: 3–4/season (multiple Domain Actions)
- Net: TC still advances at +1.5–2/season despite sustained Niflhel opposition
**TC cannot be stopped by Niflhel alone.** Multiple factions must coordinate to suppress TC.

**Degenerate — Niflhel targeting Revolution:**
Revolution has low Stability (4) and low defensive capability. Niflhel targeting Revolution instead of Church:
Ob = 4 ÷ 3 = Ob 2. P(success, 7D) ≈ 82%.
Revolution Stability 4 → 2 after 2 successful ops. Revolution enters economic difficulty.
**Why would Niflhel destabilise Revolution?** If Revolution is gaining Military strength threatening Niflhel's covert operations. But politically: Niflhel and Revolution may share anti-Church objectives.
No faction alignment mechanic exists. Niflhel can destabilise any faction including potential allies. **GAP: No mechanic for faction non-aggression or alliance that modifies Domain Action targets.**

**Optimal play — Niflhel endgame:**
Best Niflhel strategy given all mechanics:
1. Maintain 3 Riskbreakers on rotation (PP-064, Wealth 2/season cost)
2. Primary target: Church Stability (suppress to 3, activating TC brake)
3. Secondary target: Crown Intel (reduce below 4, preventing passive detection per PP-044)
4. Never target Revolution or Hafenmark (potential allies against Church)
This strategy costs 2 Wealth/season and expected TC reduction 1–1.5/season. Effective but not decisive.

**F-B9-14** (P2) — No faction alignment/non-aggression mechanic. Niflhel can target any faction with no mechanical distinction between allies and enemies. In a politically complex campaign, arbitrary targeting is jarring. Add: "Factions may declare a Truce (no covert operations against each other for one season) via a mutual Political Domain Action (Ob 2 for both). Truce costs one Domain Action slot per faction to initiate."
**F-B9-15** (P3) — Niflhel optimal Stability target (2–3 not 0) is undocumented design knowledge. Document in faction reference: "Niflhel's goal is Church suppression, not collapse. Stability 2–3 activates TC braking while preserving Church's Parliament role."

---

## T-B9-08 — PAST TEMPORAL COVERAGE: FACTION + COMBAT MECHANICS
**Coverage:** M-034, M-035, M-038, M-039, M-040, M-041, M-042, M-043, M-044, M-045, M-046, M-047, M-048, M-049, M-050, M-052, M-053
**Mode:** TTRPG/BG | **Temporal:** PAST | **Tracks:** FSTAT,TC,TT,IP | **Factions:** Crown,Church,Löwenritter,Revolution | **NPCs:** Ehrenwall,Almud | **Archetypes:** Faction Leader,Löwenritter Knight,Practitioner,Riskbreaker
**Cells filled:** PAST temporal tag for all mechanics above

### PAST Temporal Coverage — Faction Mechanics

**M-034 (Faction Stats) — PAST:**
Historical faction stat analysis: what did a faction's stat distribution look like before a key event?
Application: "Before the Altonian invasion (5 seasons ago), Crown Military was 7. It's now 4. What happened?"
Mechanics: Faction stats don't have a history track — only current values exist.
**GAP: No mechanic for reconstructing historical faction state.** The only historical record is session logs (player/GM notes). This is a narrative gap, not a mechanical one — historical faction analysis is purely fictional reconstruction.
PAST tag confirmed: M-034 applies to PAST temporal contexts via narrative reconstruction only.

**M-035 (Domain Actions) — PAST:**
Domain Actions taken in the past can be unearthed through investigation or historical research.
A Non-TS Scholar (Maret Uln archetype) investigating Crown's past Domain Actions: End 3 + History 2 = 5D, TN7, Ob 2. P(success) ≈ 82%.
Success reveals: what Domain Action Crown took 3 seasons ago, and what the outcome was.
This provides political intelligence — understanding past faction decisions to predict future ones.
PAST tag confirmed: Domain Actions leave historical records accessible via research.

**M-038 (Seasonal Accounting) — PAST:**
Past seasonal accounting records exist as faction financial history.
Application: "Has the Church been running at a deficit? Check 5 seasons of accounting."
Mechanics: same as M-034 — narrative reconstruction only, no mechanical track.
PAST tag confirmed: historical accounting is narrative.

**M-039–M-044 (Combat mechanics) — PAST:**
Combat that occurred in the past: resolved events with fixed outcomes. The mechanics don't re-run for past events — they inform NPC wound states and equipment losses that persist into the present.
Application: "Ehrenwall fought 3 seasons ago and took Wounds 2. Did those heal?" → M-053 (Rest) determines healing. If Full Rest was available: Wounds 0. If not: potentially Permanent (PP-041 criteria).
PAST tag confirmed: combat consequences persist via Wound track and Permanent Wound criteria.

**M-045 (Mass Combat) — PAST:**
Historical battles: resolved via narrative, but casualty outcomes affect current faction Military stats.
A battle 3 seasons ago where Löwenritter lost 60% casualties: Military −3 (from 5 to 2).
The past battle's outcome is mechanically present via current stat levels.
PAST tag confirmed: Mass Combat outcomes are embedded in current faction stats.

**M-046 (Thread Ops in Combat) — PAST:**
A practitioner who performed Thread ops in a past battle: TD accumulation persists. The past ops are the reason current TD is elevated.
PAST tag confirmed: TD is a cumulative record of all past Thread operations.

**M-047 (Thread Events in Social) — PAST:**
A past Thread event in a social context (a Grand Debate interrupted by Thread manifestation) has ongoing narrative consequences. The political impact of that event persists.
No mechanical re-resolution for past events. PAST tag confirmed: historical narrative only.

**M-048 (Scale Transitions) — PAST:**
Past scale transitions: a past personal Thread action that escalated to faction level is now represented in current faction stat. PAST tag confirmed: same as M-045.

**M-049 (Inquisitor Operations) — PAST:**
Past investigations: their outcomes (CE accumulated on suspects, TS growth triggered) are still active. CE accumulated 2 seasons ago is part of the character's current CE total.
PAST tag confirmed: Inquisitor operations leave persistent mechanical traces.

**M-050 (Riskbreakers) — PAST:**
Past Riskbreaker operations: DD accumulated, covers established or blown, intelligence gathered. All persist in current state.
PAST tag confirmed: DD is cumulative.

**M-052 (Concealment/DD+Circles) — PAST:**
Past cover establishment: Circles ratings in target factions reflect past work. A cover established 5 seasons ago at Circles 4 is still active (assuming it hasn't been blown).
PAST tag confirmed.

**M-053 (Rest) — PAST:**
Rest taken in the past: cleared Conditions, healed Wounds. The PAST rest determines the character's current health state.
PAST tag confirmed: rest history is embedded in current Wound/Condition state.

### PAST Temporal Coverage — New Finding

**F-B9-16** (P3) — No mechanical history track for faction stats. All PAST temporal analysis is narrative reconstruction from GM notes. For campaigns with complex political histories, this creates information asymmetry (GM knows more than players can mechanically discover). **Consider adding a Faction Chronicle optional mechanic:** each faction has a 3-entry historical record (last 3 seasons of stats). This gives players research targets without requiring full GM transparency.

---

## T-B9-09 — FUTURE TEMPORAL COVERAGE: GLOBAL TRACKS + FACTION
**Coverage:** M-001, M-002, M-006, M-007, M-010, M-011, M-013, M-015, M-016, M-017, M-018, M-022, M-023, M-026, M-029, M-036, M-037, M-046, M-048, M-050, M-051, M-052, M-053, M-055
**Mode:** TTRPG/BG/HYB | **Temporal:** FUT | **Tracks:** TT,TC,IP,FSTAT | **Factions:** All | **NPCs:** Multiple | **Archetypes:** All
**Cells filled:** FUT temporal tag for all mechanics above

### FUT Temporal Coverage — What does "FUT" mean for each mechanic?

FUT (future-oriented) applies when a mechanic is being used to *project into, prepare for, or create conditions in the future.* This is distinct from PRES (resolving now) and PAST (engaging accumulated history).

**M-001 (Core Dice Engine) — FUT:**
Probability calculation for future actions: "What's the chance we succeed on this plan next season?"
The dice engine underlies all future projections. FUT tag = planning/probability analysis contexts.

**M-002 (Wounds) — FUT:**
Wound trajectory: "If we fight again without rest, what's our likely wound state?"
Wound accumulation is a future-state projection in combat planning.

**M-006 (Inspirations) — FUT:**
Saving Inspirations for a future critical moment. Hoarding vs spending = FUT resource management.
The Inspiration hoard represents future optionality. FUT tag confirmed.

**M-007 (Conditions) — FUT:**
Anticipating Conditions: "If we enter combat Rattled, what happens to our social rolls next scene?"
Condition persistence into future scenes = FUT consideration.

**M-010 (Knots) — FUT:**
Knot formation as a future obstacle. Knowing a Knot is forming at a location: avoid operating there next season (FUT planning).

**M-011 (Circles) — FUT:**
Building Circles ratings for future access. Investing in a network now for future use = FUT orientation.

**M-013 (Leap) — FUT:**
The Leap itself is sometimes future-oriented: a practitioner Leaping to examine a future Thread configuration (co-movement implications). This is the FUT temporal dimension of Thread operations — seeing what the Thread looks like in a future state.
**GAP: No mechanic for future-oriented Thread observation.** Can a practitioner Leap to see a future Thread configuration? If not, all Thread operations are PRES or PAST only.
**F-B9-17 (P2):** Future Thread observation (Leap + FUT) undefined. If practitioners can observe future Thread states, this is a significant capability with no defined mechanics, Ob, or consequences. If they cannot, this should be explicitly stated. [EDITORIAL: confirm whether future Thread observation is possible in canon]

**M-015 (Weaving) — FUT:**
Weaving a structure that will activate in the future (deferred Weaving). Can a practitioner Weave a conditional structure that activates when a specific event occurs?
No mechanic found for conditional/deferred Weaving. **GAP: Deferred/conditional Weaving undefined.**

**M-016 (Pulling) — FUT:**
Pulling a connection to create a future state. "Pull the connection so that in 2 seasons, this relationship will be different."
Is a delayed Pull possible? No mechanic found. All Pulls appear to be immediate in effect.

**M-017 (FR-Lock) — FUT:**
FR-Lock prevents future changes to a Thread structure. The Lock is explicitly FUT-oriented — it freezes the present state against future alteration. FUT tag confirmed.

**M-018 (FR-Dissolution) — FUT:**
Dissolution prevents future Thread activity at a location (Gap creation as future state). FUT confirmed.

**M-022 (Dissolution Residue) — FUT:**
Residue creates future Ob penalties at the location. It is a PRES action with FUT consequences. FUT tag confirmed.

**M-023 (Collective Ops) — FUT:**
Collective operations planned across seasons: "In 3 seasons, we gather 4 practitioners at this Einhir site for a collective Past Pull." FUT tag = the planning horizon.

**M-026 (Monstrous Entities) — FUT:**
ME trajectory: a practitioner at Coherence 3 is on a FUT collision course with ME transition. Anticipating this = FUT temporal planning.

**M-029 (The Forgetting) — FUT:**
Anticipating Forgetting risk before entering Locked Zones. FUT tag = pre-entry planning.

**M-036 (Parliamentary Vote) — FUT:**
Building a coalition before a vote (future-oriented political action). FUT tag confirmed.

**M-037 (Grand Debate) — FUT:**
Preparing an argument before a Grand Debate. Research, Circles-building, Belief activation = all FUT preparation.

**M-046 (Thread in Combat) — FUT:**
Planning Thread operations for an upcoming combat. FUT tag = preparation phase.

**M-048 (Scale Transitions) — FUT:**
Anticipating scale escalation: "This Thread op will likely Overwhelm — prepare for faction-level consequence." FUT planning.

**M-050 (Riskbreakers) — FUT:**
Planning Riskbreaker operations before execution. Rotation planning (PP-064) = FUT orientation.

**M-051 (Devout Constraint) — FUT:**
Anticipating faith crisis arc. A Devout character accumulating CE knows the crisis is coming. FUT tag = arc trajectory.

**M-052 (Concealment) — FUT:**
Building cover identities before operations. Cover establishment is FUT-oriented preparation.

**M-053 (Rest) — FUT:**
Planning rest around combat and Thread operations. FUT tag = campaign pacing decisions.

**M-055 (Restoration Community Weaving) — FUT:**
Building toward Coherence recovery via community engagement. Long-arc FUT planning.

### FUT Temporal Coverage Findings

**F-B9-17** (P2) — Future Thread observation via Leap undefined. Confirmed gap. (Above)

**F-B9-18** (P2) — Deferred/conditional Weaving undefined. A practitioner who wants to Weave a structure that activates on a trigger (e.g., "when this person crosses this threshold, the Weave activates") has no mechanic for it. **Proposed fix (PP-071):** "Conditional Weaving: a practitioner may Weave a structure with a defined trigger condition (Ob +2 compared to standard Weave). When the trigger condition is met (GM call), the Weaving activates automatically. TD cost applies at the time of Weaving, not at activation. Contact ends at Weaving completion — the practitioner does not need to be present at activation."

**F-B9-19** (P3) — Delayed/scheduled Thread Pulls undefined. If practitioners can schedule a Pull for a future time, this significantly expands strategic options. Most likely: Pulls are immediate only. Add explicit statement: "Thread Pulls resolve immediately on success. There is no mechanism for scheduling or delaying a Pull's effect."

---

## T-B9-10 — TEMPORAL COVERAGE: CORE + CHARACTER MECHANICS PAST/FUT
**Coverage:** M-001, M-002, M-003, M-004, M-005, M-006, M-007, M-011, M-012, M-039, M-040, M-041, M-042, M-043, M-044
**Mode:** TTRPG | **Temporal:** PAST/FUT | **Tracks:** — | **Factions:** Crown | **NPCs:** Almud | **Archetypes:** Generic,Faction Leader,Löwenritter Knight
**Cells filled:** PAST and FUT temporal tags for core/character/combat mechanics

### Core Mechanics PAST/FUT Assessment

**M-001 (Dice Engine):**
PAST: Historical probability analysis. "How likely was it that Ehrenwall succeeded that roll 3 sessions ago?" → Post-hoc probability assessment, narrative only.
FUT: Pre-roll probability assessment for upcoming challenges. "Should we attempt this Ob 4 action with our current pool?" → Standard FUT planning.
Both tags confirmed. No mechanical gaps.

**M-002 (Wounds):**
PAST: "Ehrenwall had Wounds 3 in the battle last season. Did they become Permanent?" → PP-041 criteria apply.
FUT: "If we take one more Wound, we cross threshold 2 → TN8. Plan accordingly."
Both confirmed. Wound threshold awareness is a core FUT planning mechanic.

**M-003 (Histories):**
PAST: Histories are always PAST-oriented. They describe completed experiences that now provide dice. By definition, PAST.
FUT: Building a History through current play for future use. A player who wants a "Battle of the Northern Pass" History must survive the battle first. FUT tag = prospective History acquisition.

**M-004 (Beliefs/CP):**
PAST: Prior Belief tests generated CP. Current CP total is a PAST accumulation.
FUT: Saving CP for a future dramatic Belief expression. Hoarding vs spending = FUT resource management.

**M-005 (Maxims — CUT):**
Remove from active tracking. Confirmed cut per editorial decision (G-062).

**M-006 (Inspirations):**
PAST: "I used 2 Inspirations last session. They reset next session." → Recovery tracking.
FUT: Strategic hoarding (confirmed above in T-B9-09).

**M-007 (Conditions):**
PAST: "Rattled last session, now it's cleared after rest." → State tracking.
FUT: Anticipating Condition triggers in upcoming combat.

**M-011 (Circles):**
PAST: Established Circles ratings represent prior relationship investment.
FUT: Building Circles for future access (confirmed T-B9-09).

**M-012 (Resources):**
PAST: Prior Resource expenditures constrain current state.
FUT: "If I spend Resources 2 now, I'll be constrained next scene." → FUT planning.

**M-039–M-044 (Combat):**
PAST: Combat history (wounds taken, conditions accumulated) affects current state.
FUT: Combat planning (pool allocation, approach strategy).
All confirmed. No mechanical gaps in temporal coverage for combat.

### Finding

**F-B9-20** (P3) — M-005 (Maxims) should be formally removed from the coverage matrix and all tracking. It is a cut mechanic (G-062). Continuing to track it creates ongoing noise in Phase 3 gate calculations. Remove from matrix; note as "Cut — G-062."

---

## BATCH 09 FINDINGS INDEX

| # | Test | Mechanics | Severity | Issue | Proposed Fix |
|---|------|-----------|----------|-------|-------------|
| F-B9-01 | T-01 | M-016 | P2 | Multi-entity connection Pull undefined — one roll vs per-entity roll is major functional difference | One roll targeting the connection; all connected entities affected; TT once per Pull |
| F-B9-02 | T-01 | M-016 | P3 | Overwhelming Pull cascade clause absent — adjacent connection should shift | On Overwhelming: one adjacent connection also shifts (GM selection) |
| F-B9-03 | T-01 | M-016,M-025 | P3 | Exhaustive Pulling = Gap creation, undocumented | "When all Thread connections at a location are Pulled/Dissolved, location becomes Gap rating 1" |
| F-B9-04 | T-02 | M-021 | P1 | ME transition procedure absent — Coherence 0 has no defined mechanical state | Add ME character state definition (stats retained, Circles/Beliefs lost, Thread bonuses, communication degraded) |
| F-B9-05 | T-02 | M-021,M-055 | P3 | Recovery from deep Coherence degradation is campaign-length (9 Weavings from Coherence 1) | Document in Restoration guidance as long-arc commitment |
| F-B9-06 | T-03 | M-038,M-034 | P2 | No faction economic emergency mechanic — all-faction Wealth 0 has no resolution procedure | Add Economic Crisis: 3+ factions at Wealth 0 → clocks pause 1 season, TT −2, IP +5, Emergency Resource action Ob 3 |
| F-B9-07 | T-03 | M-038,M-045 | P2 | War upkeep cost not explicitly specified | Add: "Active military conflict: additional upkeep = Military ÷ 2 (rounded up) in Wealth/season per belligerent" |
| F-B9-08 | T-04 | M-026 | P1 | ME transition procedure absent (same as F-B9-04, multi-angle confirmation) | Same fix as F-B9-04 |
| F-B9-09 | T-04 | M-026,M-031 | P2 | City-scale ME = TC +10 in one season — undocumented GM calibration | Document in GM reference as priority containment scenario |
| F-B9-10 | T-05 | M-050 | P2 | Voluntary Riskbreaker extraction undefined | Add: "Voluntary extract: DD resets to 0, cover retired, faction loses Riskbreaker intelligence for 1 season, no IP penalty" |
| F-B9-11 | T-05 | M-050 | P2 | DD does not naturally decay — accumulated exposure is permanent | Add: "DD −1 per season with no operations. Minimum 0." |
| F-B9-12 | T-06 | M-051 | P3 | Devout faith crisis arc mechanically complete — document as canonical character arc | Add to Devout character guidance |
| F-B9-13 | T-06 | M-051 | P2 | Dissonance Mark accumulation rate high at Einhir sites — 3 marks in 3 scenes triggers crisis very fast | Add: "Dissonance Marks require at least one scene between accumulations" |
| F-B9-14 | T-07 | M-056,M-035 | P2 | No faction alignment/non-aggression mechanic — Niflhel can target any faction including allies | Add Truce mechanic: mutual Political Domain Action (Ob 2) = no covert ops against each other for 1 season |
| F-B9-15 | T-07 | M-056 | P3 | Niflhel optimal target is Stability 2–3 not 0 — undocumented design knowledge | Document in faction reference |
| F-B9-16 | T-08 | M-034,M-035,M-038 | P3 | No mechanical history track for faction stats — PAST analysis is narrative only | Consider optional Faction Chronicle: 3-season historical stat record |
| F-B9-17 | T-09 | M-013 | P2 | Future Thread observation via Leap undefined — significant capability with no mechanics | [EDITORIAL] Confirm whether future Thread observation is possible in canon |
| F-B9-18 | T-09 | M-015 | P2 | Deferred/conditional Weaving undefined | Add: Conditional Weaving at Ob +2; trigger condition defined at Weaving time; activates automatically |
| F-B9-19 | T-09 | M-016 | P3 | Delayed Pull undefined — most likely Pulls are immediate only | Add explicit statement: "Thread Pulls resolve immediately; no scheduling mechanism exists" |
| F-B9-20 | T-10 | M-005 | P3 | M-005 (Maxims) should be formally removed from coverage matrix | Remove from matrix; note as "Cut — G-062" |

### P1 Summary — Batch 09
F-B9-04 and F-B9-08 are the same finding (ME transition procedure absent) confirmed from two test angles. Count as one new P1.

**New P1 findings this batch: 1 (ME transition procedure)**
**Total P1 after Batch 09: 20**

---

## PATCH PROPOSALS — BATCH 09 ADDITIONS

### PP-069
**Finding:** F-B9-06 / F83 extension
**Severity:** P2 (F83 related)
**Mechanic:** M-038 (Seasonal Accounting), M-034 (Faction Stats)
**Proposed fix:** "Anti-death-spiral recovery actions may use any faction stat as the pool (player choice), representing the faction drawing on their strongest resource to survive. The Ob floor remains 4."

### PP-070
**Finding:** F-B9-06
**Severity:** P2
**Mechanic:** M-038 (Seasonal Accounting)
**Proposed fix:** "If 3 or more factions simultaneously reach Wealth 0, an Economic Crisis is declared: all clocks pause for 1 season, TT −2, IP +5. Each faction may attempt one Emergency Resource action at Ob 3 using any stat (one attempt per faction, no Domain Action slot cost)."

### PP-071
**Finding:** F-B9-18
**Severity:** P2
**Mechanic:** M-015 (Weaving)
**Proposed fix:** "Conditional Weaving: a practitioner may Weave a structure with a defined trigger condition (Ob +2 vs standard Weave). When the trigger condition is met (GM call or stated mechanical threshold), the Weaving activates automatically. TD cost applies at time of Weaving. Contact ends at Weaving completion."
[EDITORIAL: confirm whether deferred Weaving is consistent with Foundations P-01 co-movement principle]

### PP-072
**Finding:** F-B9-14
**Severity:** P2
**Mechanic:** M-056 (Niflhel Destabilisation), M-035 (Domain Actions)
**Proposed fix:** "Truce mechanic: two factions may declare a Truce by each spending one Political Domain Action (Ob 2). During a Truce season, neither faction may take covert or military Domain Actions targeting the other. Truce expires at season end unless renewed. Either faction may break a Truce at any time; breaking a Truce costs IP +2 (diplomatic credibility loss)."

### PP-073
**Finding:** F-B9-10, F-B9-11
**Severity:** P2
**Mechanic:** M-050 (Riskbreakers)
**Proposed fix (extends PP-064):**
- Voluntary extraction: "A Riskbreaker may extract at any DD level. DD resets to 0, cover identity is retired (Circles → 0), faction loses Riskbreaker intelligence for one season, no IP penalty."
- Natural DD decay: "At season end, if the Riskbreaker performed no operations this season: DD −1. Minimum DD: 0."

### PP-074
**Finding:** F-B9-01
**Severity:** P2
**Mechanic:** M-016 (Pulling)
**Proposed fix:** "Pulling a connection shared by multiple entities: use one roll targeting the connection itself. All entities connected by the same Thread connection are affected by the outcome. TT cost applies once per Pull regardless of the number of affected entities."

### PP-075
**Finding:** F-B9-07
**Severity:** P2
**Mechanic:** M-038 (Seasonal Accounting), M-045 (Mass Combat)
**Proposed fix:** "During a season of active military conflict, each belligerent faction pays additional upkeep equal to Military stat ÷ 2 (rounded up) in Wealth. This represents supply, logistics, and campaign costs."

### PP-076
**Finding:** F-B9-13
**Severity:** P2
**Mechanic:** M-051 (Devout Constraint)
**Proposed fix:** "Dissonance Marks require at least one scene between accumulations. A character cannot accumulate more than one Dissonance Mark in a single scene regardless of the number of triggering events in that scene."

### PP-077
**Finding:** F-B9-04 / F-B9-08 (consolidated)
**Severity:** P1
**Mechanic:** M-021 (Coherence), M-026 (Monstrous Entities)
**Proposed fix:** "At Coherence 0, the character enters the Monstrous state:
- Retained: TS, TD, all physical stats, combat capability
- Lost: Circles (all ratings drop to 0), Beliefs (replaced by Thread-driven compulsions defined with GM), social accessibility
- Gained: +5D on all Thread operations; ME effects on all in zone (CE +1/scene, ThS +2/scene); cannot communicate in human language if Intelligibility ≤ 2
- Play continuation: a player may continue playing a Monstrous character with group consent; this is an advanced arc requiring GM preparation
- Recovery: Coherence 0 → 1 requires: sustained Restoration Community Weaving (minimum 3 successful collective ops at the Monstrous character's location) AND voluntary cessation of all Thread operations for that period"
[EDITORIAL: confirm Monstrous character play continuation is intended as a campaign option]

---

## COVERAGE MATRIX UPDATE — BATCH 09

**Cells filled this batch:**
- M-016: Edge ✓
- M-021: Edge ✓
- M-026: Edge ✓
- M-038: Isolation ✓, Edge ✓
- M-050: Edge ✓
- M-051: Scenario ✓
- M-056: Edge ✓

**Temporal tags added:**
- PAST: M-034, M-035, M-036, M-037, M-038, M-039, M-040, M-041, M-042, M-043, M-044, M-045, M-046, M-047, M-048, M-049, M-050, M-052, M-053 (19 mechanics)
- FUT: M-001, M-002, M-006, M-007, M-010, M-011, M-013, M-015, M-016, M-017, M-018, M-022, M-023, M-026, M-029, M-036, M-037, M-046, M-048, M-050, M-051, M-052, M-053, M-055 (24 mechanics)

**M-005 status:** Formally marked as CUT (G-062). Removing from active tracking. Phase 3 gate recalculates against 55 active mechanics.

**Cell coverage after Batch 09:**
- All 7 remaining cell gaps filled ✓
- Estimated total cells complete: ~210 / 220 (55 active mechanics × 4 cells) = 95%
- Remaining incomplete: minor temporal gaps (CROSS tags on some mechanics not yet tested in cross-temporal scenarios)

**Phase 3 gate status after Batch 09:**
| Requirement | Status |
|-------------|--------|
| All active mechanics touched (55) | ✓ |
| ≥50% with Interaction (≥3 co-mechs) | ✓ 54/55 (98%) |
| All modes per applicable mechanic | ✓ (BG-confirmed TTRPG-only mechanics documented as N/A) |
| All temporal dimensions present | ~90% (remaining CROSS gaps in combat/character mechanics) |
| All NPCs tested | ✓ |
| All archetypes tested | ✓ |
| P1 findings resolved | ✗ 20 open |
| 7-dimension tags on all tests | ✓ B07+ enforced; B02–B06 retroactive still outstanding |

**Primary remaining Phase 3 blocker: 20 open P1 findings requiring mechanic-audit referral and resolution before compilation.**

