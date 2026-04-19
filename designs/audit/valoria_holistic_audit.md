# VALORIA — Holistic Audit, Critique & Unification
## Scope: All uploaded documents, all GitHub v30 design docs, all registers, 9 days of conversation history
## Date: 2026-04-15
## Method: Cross-document structural analysis → per-system audit → interdependency mapping → critique → recommendations

---

# EXECUTIVE SUMMARY

Valoria is an exceptionally ambitious project: a tabletop RPG, board game, and Godot videogame built on a rigorous phenomenological metaphysics. Over 9 days (April 6–15), the project produced ~660 patches, 13 canonical v30 design documents, 4 params files, a full headless simulation, a complete emergent arc system, Godot implementation through Phase 12, and extensive infrastructure (bootstrap, hooks, checkers, registers). The design quality is unusually high — the philosophical foundations are load-bearing, not decorative, and the mechanical systems are tightly integrated across scales.

**The project's greatest strength** is its metaphysical integrity: P-01 (inseparability) genuinely constrains every mechanic, and the system honoring that constraint (three-axis Ob, co-movement, Coherence degradation) produces emergent gameplay rather than simulating it. PP-632 (Disposition/Knot unification via Bonds) is the single best example of this design philosophy producing elegant mechanics.

**The project's greatest risk** is document fragmentation. There are now 18+ uploaded reference documents, 13+ v30 design docs, 4 params files, multiple register files, and the uploaded documents often duplicate, contradict, or supersede each other without clear authority. The canonical_sources.yaml and file_index exist to solve this, but the uploaded documents sit outside that system entirely.

---

# PART 1: DOCUMENT ECOSYSTEM — FRAGMENTATION DIAGNOSIS

## 1.1 The Authority Problem

The project has **three concurrent document layers** with unclear precedence:

**Layer 1 — GitHub v30 docs** (canonical_sources.yaml points here). These are the source of truth per project rules. 13+ skeleton/infill pairs plus params files.

**Layer 2 — Uploaded reference documents** (Jordan's files). These include:
- `valoria_canonical_definitive_r2.md` — a distillation of Layer 1
- `valoria_complete_systems_v1.md` — a parallel distillation
- `valoria_unified_videogame_spec_r2.md` — a videogame-oriented rewrite
- `valoria_comprehensive_audit.md` — an audit of Layer 1 against Godot
- `valoria_cross_conversation_review.md` — corrections to Layers 1 and 2
- `valoria_simulation_review.md` — simulation results not in Layer 1
- `valoria_three_day_audit.md` — holistic critique
- Multiple system-specific documents (NPC behavior, stability/occupation/treaty, fieldwork, emergent arcs, character histories, certainty redesign, range consistency audit, formula unification)

**Layer 3 — Conversation artifacts** (never committed). Design decisions made in chat that may or may not have been propagated to Layers 1 or 2.

**The problem:** Layer 2 documents were produced by Claude sessions that read from Layer 1 at various points in time. Some Layer 2 documents correct Layer 1 errors. Some contain stale data that Layer 1 has since fixed. Some propose changes that were never committed. There is no systematic way to determine which Layer 2 content is canonical, which is superseded, and which is pending.

**Specific conflicts identified:**

| Topic | Layer 1 (GitHub) | Layer 2 (uploaded) | Resolution |
|-------|-----------------|-------------------|------------|
| TC ceiling | clock_registry_v30: 0–75 (freeze) | canonical_definitive_r2: 0–100 (no freeze) | tc_political_redesign_v30 proposes 100 but is status PROPOSAL. **clock_registry is stale.** |
| PI (Parliament Integrity) | clock_registry_v30: 0–20, start 7 | canonical_definitive_r2: STRUCK | peninsular_strain_v1 replaces PI with Political Stability 0–10. **clock_registry is stale.** |
| IP starting value | clock_registry_v30: 5 | canonical_definitive_r2: 20 | peninsular_strain_v1 sets 20. **clock_registry is stale.** |
| RS starting value | clock_registry_v30: TTRPG 60 / BG 72 | canonical_definitive_r2: 72 | Videogame-only means single value. **clock_registry is stale.** |
| Disposition range | params_core: −4 to floor(Bonds/2)+1 (PP-632) | complete_systems_v1: same | **Consistent.** |
| Territory scale | Various 0–5 references | canonical_definitive_r2: 0–4 | J-7 open decision. **Unresolved.** |
| Church Seizure Ob | victory_v30: 7−CV | canonical_definitive_r2: 6−Piety on 0–4 | J-6 open decision. **Unresolved.** |

## 1.2 Recommendation: Single-Source Consolidation

The uploaded documents should be treated as **working notes, not canonical sources**. Their value is in identifying gaps and corrections in Layer 1. The corrections they identify should be propagated into Layer 1 (GitHub) and then the uploaded documents should be deprecated.

The clock_registry_v30.md is the most urgently stale file on GitHub. It still references PI (struck), uses old IP starting value, and has TC at 75. It needs a full update from peninsular_strain_v1 and tc_political_redesign_v30.

---

# PART 2: METAPHYSICAL INTEGRITY

## 2.1 Foundations Hold

The philosophical foundations (P-01 through P-15) are internally consistent and mechanically expressed. Key validations:

- **P-01 (Inseparability):** Every Thread operation produces co-movement across temporal, epistemic, and actualized dimensions. The three-axis Ob system (Depth + Breadth + Distance) correctly encodes this — each axis represents a different dimension of the operation's scope.
- **P-02 (Ein Sof = infinite positive being):** No monster stat block frames its origin as evil or chaos. Threadcut beings are rendering failures, not villains.
- **P-03 (Rendering = consciousness-performed):** The GM-as-rendering-engine design is philosophically correct. The videogame adaptation must find a computational analogue — this is the deepest open design problem.
- **P-05 (Three emergence modes):** Mode 1 (un-rendering), Mode 2 (over-rendering), Mode 3 (displacement) are mechanically distinguished in threadwork_v30 and fieldwork_v30.
- **P-15 (Three-layer being-persistence):** Coherence 0 does not destroy the practitioner's ability to perceive threads — it destroys their ability to render themselves as rendering them. This is correctly expressed in the Dissonance mechanics.

## 2.2 Metaphysical Risks

**Risk M-1: Videogame rendering of consciousness-performed rendering.** P-03 states rendering is what minds do, not an external mechanism. In the TTRPG, the GM is the rendering engine. In the videogame, the game engine is the rendering engine. This creates a philosophical tension: the game's metaphysics says reality is consciousness-dependent, but the game itself computationally determines reality. The videogame spec (r2) does not address this tension.

**Proposed resolution:** The videogame's computed world-state represents what the protagonist's consciousness is rendering. NPC actions and world events that happen off-screen are not rendered until the protagonist becomes aware of them — which is when they enter the player's information state. This aligns P-03 with the videogame's information architecture: the game world is a rendering, not an objective reality, and the protagonist's perception is the rendering engine.

**Risk M-2: Mending immunity to opposition.** The PP-632 derivation (Mending targets substrate absence, not thread presence, therefore opposition cannot engage it) is philosophically elegant but creates a mechanical asymmetry: Mending is the only Thread operation that cannot be contested. In the videogame, this means a player performing Mending near an opponent faces no Thread-based counter. The only counter is physical (combat interruption) or institutional (Church investigation). This is probably correct — Mending is literally repairing reality, and opposing it would mean trying to keep reality broken — but it gives Mending-focused characters a significant safety advantage in Thread operations.

**Risk M-3: N-way opposing operations.** The rule that 3+ simultaneous practitioners produce automatic lattice collapse with Gap formation is philosophically justified but mechanically extreme. In a videogame where NPC practitioners may operate simultaneously without player awareness, this could produce Gaps in locations the player never visited. The videogame needs a visibility/proximity check: N-way collapse only fires if the operations are on the same thread target, not merely in the same territory.

## 2.3 Best Practice: PP-632 as Design Standard

PP-632 (Disposition/Knot unification) exemplifies the project's best design methodology:

1. **Single governing attribute (Bonds)** determines both Disposition ceiling and Knot capacity via the same formula: floor(Bonds/2)+1.
2. **Ob formula is universal:** max(1, base Ob − Disposition) replaces a lookup table.
3. **The design is philosophically grounded:** relational depth is finite, and the depth of any one relationship constrains how many relationships of that depth you can maintain.
4. **The formula is simulation-validated:** Neutral→Bonded = 6–8 actions across 3–4 seasons (SIM-DEBT-FW-03).

Every future mechanic should meet this standard: one formula, philosophically derivable, simulation-validated, replacing any lookup table or special case.

---

# PART 3: CROSS-SCALE SYSTEM AUDIT

## 3.1 Universal Pool Formula Consistency

The universal pool formula is **(Primary Attribute × 2) + History (0–3D) + 3**, minimum 5D, TN 7. This is correctly applied across:

| System | Pool | Verified |
|--------|------|----------|
| Personal Combat | (Agi×2)+H+3 | ✓ params_combat |
| Social Contest | (Attr×2)+H+3 (Attr varies by adjudicator) | ✓ social_contest_v30 |
| Fieldwork (all actions) | (Primary×2)+H+3 | ✓ fieldwork_v30 |
| Stealth | (Primary×2)+H+3 | ✓ fieldwork_v30 |
| Knot formation | (Bonds×2)+3 (no History) | ✓ PP-632 — intentional exception |

**Thread pool exception:** (Spirit×2)+H+TPS replaces the +3 with TPS. This is the only structural deviation from the universal formula and is justified: Thread Pool Score is a practitioner-specific capacity that replaces the base competence bonus.

**Mass combat exception:** min(Size, Command) + Command. This is a different formula entirely, justified by the fact that mass combat uses unit stats, not personal attributes. J-1 asks whether this should be (min(Size,Command)×2)+H+3 for consistency. The current formula is more elegant — it naturally caps effectiveness when units are depleted below their command capacity.

**Finding:** The universal pool formula is rigorously consistent. The two exceptions (Thread TPS, mass combat unit pool) are both justified by domain-specific requirements.

## 3.2 Universal Obstacle Formula Consistency

**Ob = floor(stat/2) + 1** is confirmed canonical (proposal_formula_range_unification.md, applied).

Cross-checked against all params files:

| Context | Formula | Status |
|---------|---------|--------|
| Govern Ob | floor(Prosperity/2)+1 | ✓ Applied |
| Diplomacy vs NPC | floor(Stability/2)+1 | ✓ Applied |
| Crown Treaty Ob | floor(Mandate/2)+1 | ✓ Applied |
| Appraise Ob | floor(Cha/2)+1 | ✓ PP-614 |
| NPC Approach Ob | floor(highest Disp/2)+1 | ✓ |
| Church Seizure Ob | 6−Piety (0–4 scale) | ✗ DIFFERENT — inverted subtraction, not floor formula. Intentional per J-6. |

**Finding:** The formula unification is complete. The Church Seizure Ob is the only remaining non-floor formula, and it's intentionally different (higher Piety = easier seizure, expressed as subtraction rather than floor division).

## 3.3 Health/Resource Parallels

The cross-system parallel table from the canonical registry is verified correct:

| Concept | Combat | Mass Combat | Contest | Thread |
|---------|--------|-------------|---------|--------|
| Health | Wound Threshold (End+6) | Type Health × Size | Composure (Cha+6) | Coherence (10→0) |
| Endurance | Stamina (End+1) | Discipline (1–7) | Concentration (Foc+Rec) | Contact Rounds (Focus) |
| Degradation | −1D/Wound | Size loss, Discipline break | +1 Ob/Rattled | −1 Coherence/op |
| Collapse | Incapacitation | Rout | Spent (−2D, resets) | Rendering Crisis |

**Gap identified:** Fieldwork has no explicit health/resource parallel. Extended investigation should have a cost — currently, a character can investigate indefinitely within a season with no resource drain except Exposure (which is detection risk, not personal cost). Consider whether Fieldwork operations should drain Stamina (physical investigation), Concentration (mental investigation), or neither (investigation is inherently sustainable).

## 3.4 Scale Transition Integrity

The three-scale model (Personal → Territory → Peninsula) is mechanically expressed through Domain Echo:

- **Sufficient Scope** (personal action has territory-level consequence): OW = ±2 faction stat, Success = ±1, Partial = narrative only, Failure = −1.
- **Zoom In** triggers (territory event produces personal scene): 5 defined triggers. **Insufficient for 120+ arcs.**
- **Zoom Out** (personal scene concludes, returns to strategic layer): automatic at scene end.

**Critical finding (confirmed from three_day_audit):** The Hybrid mode's promise depends on Zoom In triggers, and only 5 exist. The videogame needs at least 20–30 Zoom In triggers covering: NPC arc moments, territory-state thresholds (Accord 0 Revolt, Piety extremes), clock thresholds (MS band transitions, CI milestones), and discovery events (Thread Wound formation, Warden contact). This is the largest videogame design gap.

---

# PART 4: FACTION BALANCE AUDIT

## 4.1 Simulation Baseline

valoria_sim v4 results (20/20 tests passing):

| Outcome | Board Game | Hybrid |
|---------|-----------|--------|
| Church Theocracy | 53% | 45% |
| Crown Treaty | 14% | 16% |
| Timeout | 32% | 39% |
| Hafenmark collapse | 27.8% | — |
| Crown collapse | 3.4% | — |
| Average game length | 13.3 years | 14.5 years |

## 4.2 Church Dominance Problem

Church wins more than half of all simulated campaigns. The tc_political_redesign_v30 addresses this via:
- Conditional passive (requires T9 control + Stability ≥ 3)
- CI milestones with increasing political costs at 40/55/65/80
- Political legitimacy bonus (floor(CI/20) bonus dice) — makes Church stronger in political contests but also makes opposing Church mechanically harder, which paradoxically could accelerate TC in some scenarios
- TC ceiling raised to 100 (from 75) — this makes Theocracy Unification harder to achieve, not easier

**Unvalidated (ED-539, P1):** The compound effect of TC reform + TCV revaluation + Seizure Accord ≥ 2 has not been simulated. These three changes simultaneously buff Church acquisition tools, increase the cost of resistance, and add a quality gate. The net effect on Church win rate is unknown.

## 4.3 Hafenmark Fragility

27.8% collapse rate is a design problem. Hafenmark's structural vulnerabilities:
- Landlocked (no naval access, trade route dependency)
- Categorical Imperative framework (+1 Ob on ad hoc/precedent-breaking actions) — the most restrictive ethical framework
- Defensive military posture (AI Priority 6: Military defensive only)
- Parliamentary toolkit depends on Mandate, which other factions can erode

**What tc_political_redesign does:** Adds Accord-aware governance to NPC AI trees. Whether this reduces Hafenmark's collapse rate is an **unvalidated P1 item**.

## 4.4 Crown and Varfell

Crown Treaty at 14% is low but potentially intended — Crown's real strength is the Thread path, which the sim may not fully model (Varfell Path B VTM is incomplete in the sim). Crown's Almud NPC has the deepest character specification (Beliefs, Conviction Wounds, suppressed Reason) but "no BG mode expression" per the NPC audit.

Varfell's 3 victory paths (Thread Mastery, Southernmost Dominion, Partition) give it strategic flexibility, but VTM advancement is sim-gated (PP-NPC-04 cooldown). The Varfell chain fragility (Sigurdshelm T12 as single chokepoint) was flagged as BALANCE-002 (P2, resolved).

## 4.5 Restoration Movement Actor Problem

RM has victory conditions (Cultural Revolution: Piety ≤ 1 in 8+ territories, MS ≥ 40) but **no mechanical actor in BG mode**. No card hand. No Priority Tree in board_game_v30. Yrsa Vossen has an AI priority stack in npc_behavior_v30, but she is not a faction leader — RM is a latent faction that emerges through territory-level Piety drift.

**In the videogame, the player IS the RM actor.** This works if the player chooses an RM-aligned character. But NPC-RM needs at minimum: Community Weaving as a Domain Action (Ob 3, per threadwork), Piety drift from Presence, and a trigger for RM Emergence (formal faction status with Mandate, Influence, etc.).

---

# PART 5: NPC SYSTEM AUDIT

## 5.1 NPC Audit Scores (from designs/npcs/npc_comprehensive_audit.md)

| NPC | Score | Key Gap |
|-----|-------|---------|
| Haelgrund | 39/40 | None — best-specified NPC |
| Almud | ~35/40 | No BG mode expression |
| Himlensendt | ~34/40 | Arc B (Crisis of Faith) underspecified |
| Baralta | ~32/40 | Succession undefined |
| Vaynard | ~30/40 | VTM path linearity |
| Ehrenwall | ~30/40 | Post-coup AI not implemented |
| Lenneth | 28/40 | Zero mechanical expression |
| Elske | 24/40 | Zero characterization |
| Torben | ~26/40 | Conviction undefined by design |

## 5.2 NPC Simulation Patches

PP-NPC-01 through NPC-04 are correctly specified and address real simulation failures:
- PP-NPC-01 (Crown Decree gate): prevents Almud death spiral. Correct.
- PP-NPC-02 (Coup determinism): requires active Church Assert. Correct — passive TC should not trigger regime change.
- PP-NPC-03 (Church drift conditioning): prevents runaway CI. Correct — conditions on Stability + CI + yearly cycle.
- PP-NPC-04 (Varfell cooldown): prevents unbounded VTM. Correct — without cooldown, VTM advances every season.

## 5.3 Conviction-to-AI Integration Quality

The 7-conviction taxonomy (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity) maps cleanly to the 4 pressure point types (Evidence, Consequence, Authority, Loyalty). The mapping to Contest styles (Citation, Vision, Suppression, Insinuation) is complete. The ethical framework Ob modifiers are asymmetric and faction-specific — this is the system's best feature, creating genuine strategic differentiation in how each faction approaches the same mechanical actions.

**Finding:** The Haelgrund ↔ Torsvald parallel (hidden TS in institutions that would reject them) is flagged as "the most valuable unwritten NPC interaction." This should be a priority for the next TTRPG content session.

---

# PART 6: COMBAT & CONTEST CALIBRATION

## 6.1 Combat

All combat calibration data from SIM-STRESS-04/05/06 is consistent with params_combat:
- PP-285 (Rescue no Defence): confirmed — armour DR only, +2 Momentum.
- PP-294 (Feint partial commitment): confirmed — N dice min 3, rest for Defence.
- Group combat Fibonacci scaling: confirmed (+1D at 2v1 through +5D cap at 8+).
- Weapon system three-axis (Reach × Weight × Type): TN 5 to 8 range covers the full spectrum.

**No combat issues found.** The combat system is the most stable subsystem.

## 6.2 Social Contests

Calibration confirmed:
- ±1 Cha = 25–30% Grand Contest win rate (correctly non-dominant).
- ±4 Cha = Total Victory in 2 exchanges (appropriately decisive for large stat gaps).
- Expert Judge vs Crowd reverses advantage (Cog-heavy vs Cha-heavy) — adjudicator type matters.
- Coalition Grand Contest shared pool (14) handles 5 exchanges without Spent.

**Finding:** The contest system is well-calibrated but has the steepest learning curve of any subsystem. The two genres (Precedent/Prospect) × two orientations (Revealing/Obscuring) × four styles (Citation/Vision/Suppression/Insinuation) create a 2×2×4 = 16-cell decision space that must be internalized before a player can make meaningful tactical choices. The videogame needs clear UI guidance for this.

## 6.3 Mass Combat

PP-508 (splitting dominates concentration +9% to +45%) is the critical tactical finding. Counters (Narrow Pass terrain, Feigned Retreat) are specified. Unit Health = Type Health × Size is Jordan's directive but **unvalidated by simulation (P1)**.

The seven-phase structure (Strategy → Volley → Manoeuvre → Thread → Engagement → Cascade → Reform) is comprehensive but represents significant per-round cognitive load. For the videogame, phases can be automated; for BG, this is the most complex subsystem to execute at a table.

---

# PART 7: THREAD OPERATIONS

## 7.1 Post-PP-619 State

The Thread system is the most heavily patched subsystem (PP-600 through PP-632). Current canonical state:
- Single pool: (Spirit×2)+History+TPS
- TN encodes operation type: 7/8/9
- Three-axis Ob: Depth (Fibonacci 1,2,3,5,8,13) + Breadth + Distance
- Gap self-closure by scale
- Scale hierarchy rule (X cannot hold while X+1 persists)

**This is mechanically clean.** The 30-patch sprint produced a system that is simpler and more elegant than its predecessor. The three-axis Ob is the standout design: it converts a single number (total Ob) into a meaningful statement about what the practitioner is attempting (how deep, how wide, how far).

## 7.2 Coherence Economy

War-scale: 7-turn battle = 10→3 (Dissonant). 9+ turns = Severance risk. Recovery: +1/season non-practice, +1 from Knot Anchoring.

**Finding:** Coherence recovery is slow (2/season maximum). A practitioner who operates at war-scale in a battle starts the next season at Coherence 3, takes one season to reach 5, another to reach 7. Full recovery from Dissonant to Stable (10) takes 3.5 seasons minimum. This creates a natural rhythm: major Thread operations are seasonal events, not routine actions. This is correct — Thread work should feel consequential.

## 7.3 Community Weaving

RM-specific, Ob 3, restores MS +1 to +2. This is the only non-practitioner-gated Thread operation — Community Weaving represents collective cultural memory, not individual Thread manipulation. It's philosophically grounded in P-15 (three-layer being-persistence: personal memory, cultural practice, Thread substrate).

---

# PART 8: FIELDWORK

## 8.1 System Health

Fieldwork (fieldwork_v30.md, 63K chars) is the newest subsystem and the most thoroughly simulation-validated:
- Evidence Track pacing: 3–5 scenes for 5-threshold (high pool), 4–6 (low pool)
- Cover calibration: 3 = 3 scenes, 9 = full season, 12+ = near-immune
- Disposition economy: Neutral→Bonded = 6–8 actions, 3–4 seasons
- Sincerity Gate: 37% failure on instrumental Connect
- Church Attention Pool: ~11% of max TC acceleration over 4 seasons

**Finding:** The Sincerity Gate (Spirit TN 7 Ob 1, 37% failure rate) is the fieldwork system's most elegant mechanic. It means that trying to befriend someone for instrumental reasons has a meaningful chance of failing — and the failure is detectable (the NPC may notice the insincerity). This produces emergent social gameplay: players must decide whether to risk the Sincerity Gate or invest in genuine connection.

## 8.2 Fieldwork-to-Thread Integration

All Thread operations may advance the Evidence Track contextually. Knot-mediated remote Thread-Read costs +1 Knot strain per use, detection causes Disposition −3. These are well-specified cross-system interactions.

---

# PART 9: EMERGENT ARC SYSTEM

## 9.1 Architecture

The v8 arc system uses **vectors** (sustained pressures) rather than triggered events. This is the correct architecture for a game with this many interacting systems — discrete triggers would produce a combinatorial explosion, while vectors create a pressure landscape that the GM (or videogame AI) navigates.

~120+ arcs organized as: Clock Vectors (P01–P05), Faction Vectors (faction-specific), Territory Vectors (territory-specific), NPC Vectors (character-specific), Collision Events (multi-vector intersections).

## 9.2 Trigger Distribution (from arc evaluation session)

- **Overtriggered:** Church faction (too many arcs from TC thresholds alone)
- **Undertriggered:** Crown (too few territory-based triggers), Hafenmark (almost no arcs below Season 8), Varfell (VTM path too linear)
- **Missing:** Territory-based triggers (arcs from specific territory state changes)

**This confirms the three_day_audit finding:** the arc system needs territory-based triggers for the videogame. The player explores territories; arcs should fire from what the player discovers in those territories, not only from peninsula-level clock thresholds.

---

# PART 10: GODOT IMPLEMENTATION

## 10.1 Current State

Phases 1–12 implemented (as of April 15 "echoes" session):
- BoardContainer with territory map
- BattleContainer with general Command from Cha+Cog
- check_victory covering all canonical victory conditions
- Nested zoom (Phase 10.1)
- Season loop runnable end-to-end

## 10.2 Implementation Gaps

- check_victory uses pre-peninsular_strain victory conditions (ED-537, P2)
- GameMode enum still exists (Jordan directed videogame-only)
- No Phase 1 data extraction (attribute lists, derived formulas, degree table)
- No UI/UX design
- No art direction
- No audio design
- Conversion ledger "Tested" column blank across all items

## 10.3 Godot-Specific Findings from Uploaded Files

The Godot files in files3.zip (SkillEffectResolver.gd, Constants_Additions.gd, Enums_Additions.gd, CharacterCreationManager.gd, EventBus_Additions.gd) represent Phase 0 extraction. They define data types and enums but no gameplay logic. The character creation manager references attributes but doesn't implement the 31-point allocation or min/max constraints from params_core.

---

# PART 11: CHARACTER SYSTEM

## 11.1 Histories

character_histories_v2.md (59K chars) defines ~40+ histories organized by attribute relevance. The skill sparking system (SkillSparkingSystem.gd, history_skill_integration.md) integrates histories with gameplay through contextual sparking — a history becomes relevant when the scene matches its domain, granting +1D.

## 11.2 Certainty Redesign

The certainty_redesign_and_audit.md redefines Certainty as an oscillating 0–5 track (Orthodox to Accepted) rather than a deterioration track. This is philosophically superior: both poles represent coherent worldviews, not "correct" vs "broken." Movement is driven by Thread encounter and Church reinforcement.

**Finding:** The certainty redesign should be propagated to params_core if not already. Certainty is referenced by NPC behavior (Himlensendt Certainty 5, Almud Certainty 3) and by Contest mechanics (Certainty can modify argument effectiveness).

## 11.3 Range Consistency

The audit_range_consistency.md identifies the complete scale taxonomy:
- 0–7/1–7: attributes, faction stats, unit stats
- 0–5: territory tracks (CV/Piety, Prosperity, VTM, etc.)
- 0–4: territory tracks (Accord, Piety, Fort Level — per J-7 pending)
- 0–10: Coherence, Exposure, Conviction Track
- 0–100: MS, CI, IP, TS

**The J-7 decision (confirm 0–4 uniform territory scale) is blocking.** Some docs use 0–5, some use 0–4. Until J-7 resolves, every territory-scale formula is potentially stale.

---

# PART 12: OPEN DECISIONS BLOCKING PROGRESS

| ID | Decision | Impact | Recommendation |
|----|----------|--------|----------------|
| J-1 | Mass combat pool formula | Consistency vs elegance | Keep current — min(S,C)+C is more elegant than universal formula for unit-scale |
| J-3 | RM rethink timing | RM actor problem | Defer until videogame playtesting reveals whether latent-faction works |
| J-4 | Lenneth/Elske/Haelgrund stance triangles | NPC completeness | Do next — these are the highest-value unwritten NPC mechanics |
| J-5 | Accord × Exposure interaction | System integration | Specify: high Exposure in low-Accord territory should increase detection risk |
| J-6 | Church Seizure Ob on 0–4 Piety | Balance | 6−Piety gives Ob 2 at Piety 4, Ob 6 at Piety 0. This is correct — high piety = easy seizure |
| J-7 | Confirm 0–4 uniform territory scale | Range consistency | **Must resolve.** 0–4 is cleaner (maps to 5 named states per track). Resolve and propagate. |
| J-8 | Confirm CI milestones | Balance | Confirm — sim data supports milestones |
| J-9 | Confirm Spiritual Weight values | Balance | Confirm — T9=5 is correct for Church seat |

---

# PART 13: UNVALIDATED COMPOUND INTERACTIONS

These are the highest-priority simulation needs:

| ID | Interaction | Priority | Risk |
|----|------------|----------|------|
| ED-538 | Accord + Political Stability + battle consequences | P1 | Could produce runaway instability spiral |
| ED-539 | TC reform + TCV 5 + Seizure Accord ≥ 2 compound | P1 | Three simultaneous Church changes without combined validation |
| — | Accord-aware NPC AI vs Hafenmark collapse rate | P1 | The 27.8% collapse rate may or may not improve |
| — | Dynastic Proclamation + Cultural Reformation | P1 | Two new acquisition tools never simulated |
| — | Unit Health = Type Health × Size | P1 | Jordan directive not yet validated against mass combat balance |

---

# PART 14: RECOMMENDATIONS — PRIORITIZED

## Priority 1: Resolve blocking decisions

1. **J-7 (territory scale 0–4).** Resolve and propagate to all documents. This unblocks Church Seizure Ob (J-6) and territory-track formula consistency.
2. **J-8 and J-9 (CI milestones, Spiritual Weight).** Confirm and commit.
3. **clock_registry_v30.md update.** This file is severely stale — update from peninsular_strain_v1 and tc_political_redesign_v30.

## Priority 2: Simulation validation

4. **Run ED-538 and ED-539 compound simulations.** These are the highest-risk unvalidated interactions.
5. **Re-run valoria_sim with Accord-aware NPC AI.** Determine whether Hafenmark collapse rate improves.
6. **Validate Unit Health = Type Health × Size** against existing mass combat balance.

## Priority 3: Design completion

7. **Write stance triangles for Lenneth, Elske, Haelgrund (J-4).** These are the most impactful unwritten NPC specifications.
8. **Define 20–30 Zoom In triggers for videogame.** The hybrid/videogame mode depends on these.
9. **Specify RM as mechanical actor.** Community Weaving as Domain Action, Piety drift from Presence, Emergence trigger.

## Priority 4: Document consolidation

10. **Deprecate uploaded Layer 2 documents.** Propagate all corrections into GitHub v30 docs. Stop maintaining parallel reference documents.
11. **Merge peninsular_strain_v1 into victory_v30.** peninsular_strain is a PROPOSAL that supersedes sections of victory_v30 — it should be integrated, not left as a separate document.
12. **Merge tc_political_redesign_v30 into board_game_v30/clock_registry_v30.** Same issue — proposals that are effectively canonical should be integrated into their parent documents.

## Priority 5: Videogame-specific

13. **Resolve P-03 (consciousness-performed rendering) for videogame.** Define the computational model of rendering.
14. **Design the UI/UX layer.** The game's complexity demands exceptional information design — this is the largest unaddressed videogame risk.
15. **Define onboarding sequence.** How does a new player learn the metaphysics, the faction dynamics, and the system interactions?

---

# PART 15: WHAT WORKS BEST — DESIGN HIGHLIGHTS

1. **PP-632 (Disposition/Knot via Bonds).** One formula, two applications, philosophically grounded, sim-validated. The design quality benchmark.

2. **Three-axis Thread Ob (Depth + Breadth + Distance).** Converts an abstract difficulty number into a meaningful statement about the operation's scope. Players know what they're attempting because the Ob tells them.

3. **Ethical Framework Ob Modifiers.** Each faction's moral philosophy creates genuine mechanical asymmetry. Crown's Virtue Ethics makes public, principled action easier but covert action harder. Church's Divine Command makes doctrine-aligned action easier but Thread truth catastrophic (+2 Ob). This is faction differentiation through worldview, not stat differences.

4. **NPC Conviction-to-AI Integration.** The three-step decision procedure (Institutional Filter → Conviction Filter → Decision Fork based on Conviction Wound count) is simple, deterministic, and produces emergent behavior. A wounded NPC acts differently from an unwounded one — not because of a scripted arc, but because the decision procedure routes differently.

5. **Sincerity Gate.** Spirit TN 7 Ob 1 (37% failure) on instrumental social connection. Elegant, philosophically grounded (genuine connection requires genuine openness), and produces meaningful player decisions.

6. **Calamity Radiation.** Dynamic geographic susceptibility based on MS band × node distance from Askeheim. The radiation zone expanding as MS drops IS the visual expression of the Catastrophe spreading. Mechanically simple, narratively powerful.

7. **Vector-based emergent arcs.** Pressures, not triggers. The GM/AI runs pressures and observes what they produce. This is the correct architecture for a system with 120+ potential narrative threads.

8. **Battle consequences (MS −1, IP +2, Political Stability +1).** Three global clocks all advance from a single battle. Every military action has costs beyond the tactical outcome. This makes violence expensive without prohibiting it — exactly the right incentive structure for a political simulation.

---

# APPENDIX A: FILE STATUS MATRIX

| File | Source | Status | Action |
|------|--------|--------|--------|
| valoria_canonical_definitive_r2.md | Uploaded | Mostly current | Deprecate after propagating corrections to GitHub |
| valoria_complete_systems_v1.md | Uploaded | Mostly current | Deprecate — duplicates canonical_definitive |
| valoria_cross_conversation_review.md | Uploaded | Corrections list | Propagate remaining corrections, then deprecate |
| valoria_simulation_review.md | Uploaded | Sim data reference | Commit sim results to GitHub tests/ if not already |
| valoria_comprehensive_audit.md | Uploaded | Godot gap analysis | Use for Phase 1 planning, then deprecate |
| valoria_three_day_audit.md | Uploaded | Critique | Reference only — findings are addressed or acknowledged |
| valoria_unified_videogame_spec_r2.md | Uploaded | Videogame spec | **Keep active** — this is the primary videogame reference |
| npc_behavior_system_v1.md | Uploaded | Pre-v30 version | Superseded by npc_behavior_v30.md on GitHub |
| audit_npc_behavior_system.md | Uploaded | Audit of above | Reference only |
| stability_occupation_treaty_parliament_v1.md | Uploaded | PP-403 repeal | Subsumed into faction_layer_v30 and peninsular_strain_v1 |
| emergent_arc_system_v8.md | Extracted | Arc register v8 | **Keep active** — may not be fully committed |
| character_histories_v2.md | Extracted | Character content | Check commit status |
| fieldwork_design_v1_corrected.md | Extracted | Pre-v30 version | Superseded by fieldwork_v30.md |
| certainty_redesign_and_audit.md | Extracted | Design proposal | Check if propagated to params_core |
| proposal_formula_range_unification.md | Extracted | Applied | Superseded — changes committed |
| audit_range_consistency.md | Extracted | Audit | Reference only — J-7 decision pending |
| simulation_strategy_v8.md | Extracted | Sim planning | Reference only |
| clock_registry_v30.md | GitHub | **STALE** | Urgent update needed |
