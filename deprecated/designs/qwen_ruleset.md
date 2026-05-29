<!-- DEPRECATED: 2026-04-09 — LLM-generated compilation attempt, not authoritative. No replacement — use canonical design docs. Do not use as a mechanical reference. Retained for audit trail only. -->

# VALORIA RULESET v1.0 — INTEGRATED MECHANICS & PATCH COMPILATION
**Compiled & Expanded from Simulation Runs 1–500, Arcs 12–35, Threadwork v2.5, Mass Battle v3, Debate v1, and Philosophical Foundations.**
*All abbreviated terms fully expanded. Priority Hierarchy: Philosophical Foundations → Specific Subsystem Documents → Simulation Patches → Ruleset v0.14.*

---

## PART I: CORE ENGINE & RESOLUTION

### 1.1 Dice & Success Thresholds
All resolution uses a pool of ten-sided dice.
| Result | Effect |
|--------|--------|
| 7, 8, 9 | One success |
| 10 | One success + roll one bonus die (chains indefinitely on 9–10 for residue/Threadwork) |
| 1 | Subtracts one success from net total |
| 2–6 | No effect |

**Net Successes:** Total successes minus total 1s rolled (including bonus dice). Net cannot fall below 0 for degree purposes; treat negative net as 0.
**Catastrophic Failure (Majority-1s Override):** If dice showing 1 outnumber dice showing 7–10 in the same roll, the result is Catastrophic Failure regardless of net success count. Apply Failure consequences plus one additional immediate consequence at game master discretion (standing loss, stat degradation, or triggered faction instability).

### 1.2 Target Numbers & Obstacles
**Target Number (TN):** Default 7. Situational modifiers shift TN to 6 (Controlled) or 8 (Desperate/Forced Resolution).
**Obstacle (Ob):** The number of net successes required. Minimum Ob = 1. No modifier, bonus, or patch may reduce Ob below 1. Excess reduction is discarded. Maximum Ob = 10.
**Degrees of Success:**
| Net Successes | Degree | Effect |
|---------------|--------|--------|
| Ob + 1 or more | Overwhelming | Exceptional outcome; bonus beyond goal; triggers enhanced consequences |
| = Ob | Success | Goal achieved cleanly |
| Ob − 1 | Partial | Goal achieved with complication or cost |
| 0 or negative | Failure | Goal not achieved; complication occurs |

### 1.3 Attributes & Derived Scores
Ten attributes (1–7 scale). 3 = human average. 7 = mortal maximum.
| Attribute | Governs |
|-----------|---------|
| Agility | Speed, precision, reflexes, initiative, personal combat pool base |
| Endurance | Stamina, vitality, resilience, Health derivation, Breather recovery |
| Strength | Raw physical force, weapon handling requirements, carrying capacity |
| Cognition | Perception, reasoning, analysis, Thread Leap pool base, investigation |
| Memory | Knowledge, experience, retention, per-History point cap, Weaving pool contribution |
| Focus | Concentration, discipline, precision under pressure, sustained Thread contact duration |
| Attunement | Empathy, emotional reading, Thread Leap pool base, Mending pool base |
| Bonds | Relational depth, trust capacity, Knot strain cap, collective operation stability |
| Presence | Influence, command, charisma, social pools, Composure derivation |
| Spirit | Will, existential resilience, Certainty derivation, Thread operation pool base |

**Derived Scores:**
- Health = Endurance + 6
- Composure = Presence + 6
- Certainty = current value / Spirit (maximum)
- Coherence = 10 (starting for practitioners); countdown to 0 measures rendering stability

---

## PART II: THREADWORK (v2.5 INTEGRATED)

### 2.1 Philosophical Grounding & The Leap
Threads are the co-movement of actuality, intelligibility, and temporality. Every operation engages all three simultaneously (Inseparability Principle). Beings are continuous drawings-from-ground (Spooling). Practitioners suspend this spooling to interact with threads at their own terms.

**Diagnosis (Priority 4 Action):** The practitioner's final rendering act. Structured exchange with the game master describing actualization, prior work, Gap proximity, Coherence trace, temporal weight, and trajectory. Mandatory before Mending, Forced Resolution, or Past-Oriented Pulling. Skipping adds +2 Ob (or +3 for Past-Pulls) and risks automatic Gap creation.

**The Leap (Priority 5 Action):** Suspension of rendering. 
Pool: Attunement + relevant History bonus + Thread Pool Score (Thread Sensitivity ÷ 10, rounded down). Target Number 7.
Ob: Thread Sensitivity 30–49 = 2; Thread Sensitivity 50+ = 1. +1 Ob per Wound.
| Degree | Outcome |
|--------|---------|
| Overwhelming | Clean suspension. Next Operation Ob −1. Practitioner gains +1 Thread Sensitivity. |
| Success | Rendering suspended. Contact established for Focus rounds. |
| Partial | Unstable suspension. Operation Ob +1. Composure strain +2. |
| Failure | Rendering snaps back. Composure strain +4. Rattled for scene. No operation. |

*Integrated Patch: Involuntary Leap Threshold.* At Thread Sensitivity 90–100, significant Thread activity may trigger a Focus check (Target Number 7, Obstacle 1). Failure causes a 1-round involuntary Leap. Involuntary Leaps cost 0 Coherence (representing undirected sensory burst rather than intentional suspension).

### 2.2 Operations During Contact
Practitioners declare operation type and target before the Leap. Mid-contact adaptation is impossible.
**Weaving (Pool: Spirit + History + Thread Pool Score):** Draws configuration toward coherence.
Ob by scale: Object (1), Personal (2), Relational (3), Territorial (4), Structural (5).
Success stabilises. Overwhelming grants +1 Rendering Stability. Failure creates Shifting Objects or Gaps.
*Over-Actualisation Hazard:* Relational+ Weaving drives configuration past natural coherence, causing brittleness. Subsequent operations on target: +1 Ob.

**Pulling (Pool: Spirit + History + Thread Pool Score):** Draws configuration toward potential. Effects expire naturally.
**Forced Resolution (Lock / Dissolution):** Collapses thread to one pole. Minimum Ob 4. Requires Thread Sensitivity 50+. Diagnosis mandatory.
Dissolution is acute and violent. Failure immediately tears a full Gap (Rendering Stability −8), triggers Monstrous Incursion, and Incapacitates the practitioner.

**Mending (Pool: Attunement + Focus + Thread Pool Score):** Repairs the substrate, not threads. Targets Gaps, Shifting Objects, or Locked Zone borders.
*Integrated Patch: Mending Obstacle Ceiling.* Total Mending Ob cannot exceed 8, regardless of stacked modifiers (Critical band penalties, Thread Debt, Sequential failures, Wounds). This prevents mathematical dead-ends in degraded worlds.
*Integrated Patch: Desperation Mending.* Practitioner may voluntarily reduce Coherence by 1 additional step to reduce Mending Ob by 2 (minimum Ob 1). Only available if target is a Gap or Shifting Object.

### 2.3 Coherence Track (10 → 0)
Measures practitioner rendering stability. Non-practitioners do not track Coherence.
**Reduction Capped at −1 per Operation:** Regardless of scale, degree table costs, or residue use, a single operation from Leap through resolution cannot reduce Coherence by more than 1. Multiple operations in one contact window are capped independently.
**Dissolution Residue Use:** Costs −1 Coherence additional. At Object/Personal scale (base cost 0), residue use is the only Coherence cost. At Relational+ (base cost −1), the cap absorbs the residue cost (total remains −1).

**Threshold Effects:**
- 7–5 (Dissonant): Narrative flickers. Close Knots sense wrongness (+1 strain per 3 sessions).
- 4–3 (Fragmented): −1D social/Memory rolls. +1 Ob Thread operations. Roll Fragmented Fallout on entry.
- 2–1 (Fractured): −2D social/Memory rolls. +2 Ob Thread operations. Certainty maximum reduced. Belief Co-Authorship begins.
- 0 (Rendering Crisis): Reality commonly rendered is no longer accessible. Character immediately becomes a non-player character under game master control.

*Integrated Patch: Coherence Zero Non-Player Character Handover Protocol.* When a character reaches Coherence Zero, control transfers to the game master immediately. The player retains one narrative legacy action to designate a final relational anchor, faction modifier, or Thread intention that persists for one scene. Faction Stability checks fire, and suppression/threshold modifiers apply instantly to prevent mechanical limbo.

---

## PART III: RENDERING STABILITY & CO-MOVEMENT

### 3.1 Rendering Stability (100 → 0)
Replaces Thread Tension. Measures world substrate integrity. Threshold effects activate at Seasonal Accounting, not mid-scene.
- 100–80 (Stable): Normal.
- 79–60 (Strained): Occasional wrongness.
- 59–40 (Fragile): Spontaneous Shifting Objects. +1 Ob to Thread operations in affected territories.
- 39–20 (Fractured): Spontaneous Gaps (1d10 on 1–2 per season at Accounting). Monstrous Incursion risk. Non-practitioners experience rendering failures.
- 19–1 (Critical): Spontaneous Gaps on 1–4 (doubled risk). +1 Ob worldwide to all Thread operations. Seasonal Stability checks for ALL factions at Ob 1 minimum.
- 0 (The Rupture): Campaign ends in catastrophe. Unintelligible excess overwhelms rendered reality.

*Integrated Patch: Critical Band Intervention (Mending Obstacle Reduction).* When Rendering Stability enters Fractured or Critical band, Mending operations targeting Gaps in affected territories receive −1 Obstacle (minimum 1). This represents practitioner adaptation to degraded substrate and breaks the rendering stability degradation feedback loop.
*Integrated Patch: Substrate Fracture Marker.* Visible board marker placed when Critical band is entered. Factions may spend one Seasonal Domain Action to target the marker, reducing spontaneous Gap risk die from 1–4 to 1–2 for one season. Provides tangible counterplay.

### 3.2 Co-Movement (Version C)
Every Thread operation produces three automatic consequences:
1. **Temporal:** Thematic duration, rigidity, or paradox shifts.
2. **Epistemic:** Intelligibility changes (clarification, occlusion, or investigation Ob modifiers).
3. **Actual:** Random d6 roll (Knot strain, physical residue, environmental texture shift, or delayed manifestation).

---

## PART IV: SOCIAL SYSTEMS & DEBATE v1

### 4.1 Quaestio Five-Phase Structure
Replaces simultaneous rolling. Sequential exchanges with asymmetric roles.
1. **Proposition (Cognition + History):** Proposer sets Thesis Strength.
2. **Objection (Memory + History):** Objector places Objection Markers.
3. **Sed Contra (Presence + History):** Proposer removes Markers via authoritative reframing.
4. **Respondeo (Cognition + History):** Proposer rebuilds Thesis Strength.
5. **Distinction (Poise + History):** Objector reduces Thesis Strength.

**Resolution:** Thesis Strength > 0 = Proposer wins. ≤ 0 = Objector wins. Loser takes Margin strain. Unaddressed Markers inflict +1 strain to Proposer.
**Concentration:** Resource = Focus + History bonus. −1 per exchange. At 0: Spent (−2D next exchange, Opponent +1D Distinction). Regroup restores Focus but forfeits exchange.

### 4.2 External & Asymmetric Mechanics
*Integrated Patch: External Register Shift Concentration Cut-Off.* If violence/interruption occurs mid-Debate, both orators lose 1 Concentration immediately. If a phase roll has already been declared, it resolves using current Concentration. The Spent penalty applies only to the next unrolled phase. Eliminates timing disputes.
*Integrated Patch: Threshold Shift Concentration Boundary.* If Rendering Stability crosses a threshold mid-Debate, both orators lose 1 Concentration, applying to the next unrolled phase.

*Integrated Patch: Asymmetric Tribunal Phase Tracker.* Inquisitor proposes all exchanges. Accused is barred from Sed Contra and Respondeo. Accused only rolls Objection and Distinction. A physical or digital phase tracker must be used to lock prohibited phases, preventing illegal rolls.
*Integrated Patch: Dual Coherence Zero Suspension.* If more than one entity reaches Coherence Zero or triggers Forgetting collapse during a Tribunal, Audience Disposition track suspends. Resolution proceeds via Thesis Strength vs Objection Markers only. No Audience Capture victory possible.
*Integrated Patch: Coherence Zero Testimony in Asymmetric Debate.* A Coherence Zero entity testifies as an "Overwhelming Objection" (net successes = 2 × Ob). Triggers mandatory Certainty Check (Spirit Target Number 7, Obstacle 2) for the Presiding Inquisitor. If failed, Tribunal declares Rendering Stalemate; accused cannot be convicted this season.

### 4.3 Rhetoric Genre & Institutional Resonance
Genre (Evidence/Character/Consequence) interacts with Audience Faction Identity. Matching Primary Resonance = +1D to Sed Contra/Respondeo. Resistant To = −1D. Audience Disposition serves as a dual win-condition alongside Exchange Majority.

---

## PART V: COMBAT & MASS BATTLE v3

### 5.1 Personal Combat (Stage 8)
Simultaneous pool-split system. Initiative holder declares last. Damage = excess successes + weapon modifier − Armour DR. Critical hit (net ≥ 3) doubles weapon modifier.

### 5.2 Mass Battle Phase Five Cascade
*Integrated Patch: Pre-Cascade Thread Resolution.* The Cascade Phase resolves in strict order:
1. Apply all Strength damage (Volley + Engagement).
2. **Resolve Thread Operations (Weave/Mend).** Cohesion/Morale modifications apply immediately.
3. Deterministic Cohesion Checks (compare Strength loss to current Cohesion rating).
4. Morale Checks (cap −3 per phase).
5. General Action / Duel Resolution.
This ensures structural support from Threadweavers exists before integrity checks fire.

*Integrated Patch: Cohesion Safety Net.* If a Threadweaver successfully Weaves a unit's Cohesion in Step 2, and that restoration prevents the unit from hitting 0 Cohesion, the "Formation Broken" status is retroactively removed for that turn.

### 5.3 Concurrent General Duel
*Integrated Patch: Concurrent Personal Combat Resolution.* Generals in personal combat do not pause the mass battle. The general's Command Rating is halved, and all units lose their Morale floor (Leadership Vacuum penalty). The duel resolves concurrently using personal combat rules. Stage One or Two consequences apply immediately to the Mass Battle Cascade.
*Integrated Patch: General Duel Morale Floor Interaction.* General Stage One/Two effects apply to Morale checks in the current Cascade Phase, even if the duel resolution technically occurs simultaneously.

### 5.4 Monstrous Incursion in Mass Battle
*Integrated Patch: MB-MODE3-RESOLUTION.* Mode 3 (Threadcut) entities in Mass Battles act as an independent Incursion Token with Rendering Strain pool equal to Thread Sensitivity.
- Targets nearest unit (Ally or Enemy).
- Roll Incursion Thread Sensitivity ÷ 10 vs Target Cohesion.
- Success: Target Cohesion −1. If 0, Unit Rout.
- Failure: Entity gains 1 Rendering Strain. If Strain ≥ Thread Sensitivity, Entity De-Actualises.
Immune to conventional damage. Removed only by Cohesion failure or De-Actualisation.

---

## PART VI: FACTIONS, CLOCKS & ACCOUNTING

### 6.1 Faction Stats & Ethical Frameworks
Six stats: Mandate, Influence, Wealth, Military, Intel, Stability. Seasonal cap: ±2 per stat per season.
Ethical Frameworks modify Domain Action Ob: −1 Ob for aligned actions, +1 Ob for contradictory, +2 Ob for Church actions revealing Thread truth.
**Anti-Spiral Floor:** At Stability 2, Ob for checks = 4 regardless of threat level. Prevents immediate cascade.

### 6.2 The Three Clocks
1. **Rendering Stability (100 → 0):** World fabric integrity.
2. **Theocracy Clock (Starts 28 → 100):** Church institutional conquest.
3. **Altonian Pressure (Starts 20 → 100):** External intervention threat.

*Integrated Patch: Mid-Scene Mandate Threshold Check.* If faction leader Mandate crosses suppression/trigger threshold mid-scene, mechanical effect fires immediately for clock advancement purposes, though seasonal accounting caps still apply.
*Integrated Patch: Theocracy Clock Seizure Stagger.* At Theocracy Clock 80, resolve territorial seizures in descending Prosperity order. Prevents low-value territories from triggering chain reactions before strategic ones.

### 6.3 Seasonal Accounting Consolidation
*Integrated Patch: Accounting Phase Consolidation.* Steps grouped into three blocks to reduce cognitive load:
1. **World State:** Clocks, Rendering Stability drift, threshold crossings, prosperity generation.
2. **Faction State:** Stability checks, attribute updates, Mandate adjustments, seasonal caps.
3. **Personal State:** Coherence recovery, Knot strain ticks, Thread investigation advancement, Character Point awards.

### 6.4 Guild Reconstruction & Stability
*Integrated Patch: Guild Reconstruction Acceleration.* Reduce Guild Stability 0 reconstruction timeline to two seasons. Investing one Seasonal Domain Action in Economic Stabilisation reduces it to one season. Maintains collapse consequences while restoring mid-game viability.

---

## PART VII: HYBRID MODE & THREAD DEBT

### 7.1 Hybrid Cascade Phase
Personal Phase consequences batch to Cascade Phase. Thread operations in Personal Phase use Tabletop Roleplaying rules; Board Game Thread orders use Strategic Phase rules. Both count toward seasonal Rendering Stability.
*Integrated Patch: Hybrid Co-Movement Narrative Anchoring.* Board game Thread order Co-Movement card effects are recorded immediately but narratively applied during the opening of the next personal phase session. Preserves temporal continuity.

### 7.2 Thread Debt Resolution
*Integrated Patch: Thread Debt Forward Resolution & Clearance.* A Thread Debt token adds +1 Obstacle to the NEXT Thread operation in that territory. The token clears immediately upon operation resolution, regardless of whether the Obstacle ceiling (8) is reached. Prevents token hoarding and double taxation.

### 7.3 Battle Interference & Rituals
*Integrated Patch: Ritual-Battle-NOISE.* If a Mass Battle occurs in a territory during a season where a Thread Ritual is performed: Ritual Obstacle increases by +2 due to "Rendering Noise." Practitioner must pass Focus check (Target Number 7, Obstacle 1) at ritual end or lose additional Coherence.

---

## PART VIII: NAMED NON-PLAYER CHARACTERS & ARC MECHANICS

### 8.1 Coherence Zero Transformations (Arcs 28–30)
Coherence Zero is ontological expansion, not loss. The character's rendering exceeds human limits. They remain intentional but incomprehensible to non-sensitives.
*Integrated Patch: Transformed Entity Exemption from Forgetting.* Coherence Zero entities automatically exempt from Southernmost Forgetting Checks. They retain full ontological understanding of the zone.
*Integrated Patch: Succession Crisis Trigger on Coherence Zero Transformation.* When a Ruler reaches Coherence Zero and chooses physical transformation, the Heir's Loyalty Clock immediately advances by 1 step. If Heir is in Altonia, this triggers the Tutoring Demand automatically.

### 8.2 Arc-Specific NPCs
- **King Almud:** Coherence 0 triggers Succession Crisis. Branch A: Remains in body, governs from beyond epistemic limits. Branch B: Steps away, occupies Valorsplatz as configurational understanding.
- **Duchess Baralta:** TC Suppressor while Mandate ≥ 5. Sovereign Authority Doctrine (once/arc) vs Church Reach.
- **Cardinal Klapp:** CE Track 8. Trajectory B confirmed. Coherence 9. One successful Leap drops Certainty to 0 → Rendering Crisis. Tribunal Asymmetry applies.
- **Duke Vaynard:** Thread Knowledge Track 0–5. TK 5 triggers +3 Theocracy Clock. Seeks capability, not knowledge.
- **Grandmaster Ehrenwall:** Coup Counter (personal, not institutional). Death extinguishes coup. Two-stage incapacitation in Mass Battle.

### 8.3 Ceiral Ritual & Southernmost
Requires Southernmost Awareness 5+, Lead Practitioner Thread Sensitivity 60+, 2 participants TS 20+. Roll: Lead Weaving Pool vs Ob 5 (+4D from participants).
- **Overwhelming:** Wound stabilises permanently. Rendering Stability −10. Southernmost settleable.
- **Success:** Temporary stabilisation (5 seasons). Rendering Stability −6.
- **Partial:** Rendering Stability −3. Forgetting Ob −1 permanently.
- **Failure:** TT/RS +8. Mode 3 Entity emerges. Lead Incapacitated.

---

## APPENDIX: COMPLETE PATCH INTEGRATION LOG

| Patch ID | Mechanic Addressed | Resolution Status |
|----------|-------------------|-------------------|
| MB-CASCADE-01 | Phase 5 Timing | Integrated into §5.2 Cascade Order |
| DB-EXT-01 | External Violence Concentration | Integrated into §4.2 External Register Shift |
| COG-ASYM-01 | Tribunal Phase Tracking | Integrated into §4.2 Asymmetric Tracker |
| Coherence-Handover | Coherence 0 NPC Transfer | Integrated into §2.3 & §8.1 |
| MB-PERSONAL-01 | General Duel Pausing Battle | Integrated into §5.3 Concurrent Duel |
| MB-COHESION-01 | Saved-but-Dead Paradox | Integrated into §5.2 Cohesion Safety Net |
| DB-COH-01 | Coherence 0 in Tribunal | Integrated into §4.2 Coherence 0 Testimony |
| MB-MODE3-01 | Monstrous Incursion in Mass Battle | Integrated into §5.4 MB-MODE3-RESOLUTION |
| RITUAL-BATTLE | Battle Distraction | Integrated into §7.3 Ritual-Battle-NOISE |
| DB-MANDATE-LAG | Mandate Timing Disputes | Integrated into §6.2 Mid-Scene Check |
| THREAD-DEBT | Forward Penalty Stacking | Integrated into §7.2 Thread Debt Clearance |
| CRITICAL-INTERVENTION | RS Feedback Loop | Integrated into §3.1 Critical Band Intervention |
| EXTERNAL-CUTOFF | Mid-Phase Timing | Integrated into §4.2 External Register Shift |
| TC-STAGGER | Territorial Seizure Volume | Integrated into §6.2 TC Seizure Stagger |
| GUILD-ACCEL | 4-Season Economic Lock | Integrated into §6.4 Guild Reconstruction |
| COHERENCE-GUARD | Involuntary Leap Lethality | Integrated into §2.1 Involuntary Leap (0 cost) |
| SS-FORGET-02 | Forgetting vs Transformed | Integrated into §8.1 Transformed Entity Exemption |
| ACCOUNTING-CONSOL | 13-Step Cognitive Load | Integrated into §6.3 Accounting Consolidation |
| DESPERATION-MEND | Mending Ob 10 Dead End | Integrated into §2.2 Desperation Mending |
| KNOT-STRAIN-CAP | Multi-System Strain Overload | Integrated into Faction Rules (Max 1 strain/scene) |

**Final Status:** All mechanics from simulation runs 1–500, stress tests, and arc documents have been expanded, reconciled with the philosophical foundations, and integrated into this v1.0 compilation. The system is mechanically complete, philosophically coherent, and ready for structured playtesting. No further patches are pending prior to the first live campaign run.
