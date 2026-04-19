# VALORIA — COMPLETE THROUGHLINES MAP
## Date: 2026-04-18
## Scope: Every constitutive chain that runs through multiple mechanical systems
## Definition: A throughline is a causal spine connecting 3+ systems such that changing one system's state produces consequences in the others. These are not themes — they are mechanical chains that the engine must implement.

---

## I. ONTOLOGICAL THROUGHLINES

These derive from the Philosophical Foundations and constrain everything.

### T-01: Everything Is Thread
**Chain:** Foundations A1 → every stat in every system → rendered-level thread state
**Systems:** ALL
**What it means:** Health, Composure, Order, Prosperity, Mandate, Stability — all measure thread-configuration state at different scales. Combat wounds are thread disruptions. Political debates are epistemic thread restructuring. Governance is collective rendering maintenance. This is not metaphor; it is the game's ontological commitment.
**Implementation status:** Explicitly stated in combat_v30 §10 (post-rewrite), fieldwork_v30 §2.4, peninsular_strain_v1 §3.1. Implicit but unstated in most other systems. The Thread horizontal integration spec provides constitutive framing for combat and settlement; other systems remain mechanically correct but constitutively unframed.

### T-02: Rendering Is Consciousness-Performed
**Chain:** Foundations A6 / P-03 → investigation Five-Filter Chain → Certainty gates → TS perception tiers → player's perceptual horizon
**Systems:** investigation_systems, fieldwork, player_agency, threadwork visibility, calamity_radiation
**What it means:** The player does not see "the world" — they see what their character's rendering can present. Certainty determines which utterances are available. TS determines what thread events are visible. The radiation matrix produces different perceptual experiences at different RS bands. The game's information architecture IS the rendering.
**Implementation status:** Fully implemented in investigation_systems (Filter 1, Certainty/TS gates), fieldwork (Intelligibility Gradient), threadwork (visibility table + ED-677 rendered-level extension), calamity_radiation (environmental rendering by band). Player_agency Scene Slate now factors thread-state (ED-674).

### T-03: Inseparability
**Chain:** Foundations A2 / P-01 → every Thread operation fires co-movement across all three dimensions → temporal auto-effect + epistemic auto-effect + actualized auto-effect
**Systems:** threadwork (core), fieldwork (Thread-Read fires co-movement), mass_battle (co-movement at mass scale), social_contest (temporal axis conflict penalty)
**What it means:** There is no clean Thread operation. Every intervention on the substrate produces unintended consequences in dimensions the practitioner did not target. This is the game's core mechanic for preventing Thread from being a simple power fantasy.
**Implementation status:** Fully implemented. Co-movement fires in all modes. The three-dimensional auto-effect tables are canonical.

---

## II. CLOCK THROUGHLINES

Time-based pressures that advance regardless of player action. These are the game's structural drivers.

### T-04: RS Decay → Radiation Cascade → Institutional Crisis
**Chain:** RS baseline decay (−1/year) + Gap persistence (−4/season) + Lock drift (−1 to −2/season) + battle costs (−1 to −2/battle) → RS threshold crossing → calamity radiation effects by proximity → spontaneous Gaps → spontaneous threadcut beings → settlement Order loss → faction Stability checks → Mandate erosion → faction vulnerability → more battles → more RS decay
**Systems:** rs_budget, calamity_radiation, peninsular_strain, settlement_layer, faction_layer, victory, mass_battle
**What it means:** The world is dying. The decay is structural — it comes from the Calamity's unhealed damage, not from player action. Player action (battle, Thread operations) accelerates it. Only Mending and WC slow it. This is the positive feedback loop that makes the survival contest urgent.
**Arc register vectors:** ARC-P02, ARC-S15, ARC-S32, ARC-S34
**Convergence markers:** COLLISION C (Tutoring + Southernmost), COLLISION J (Church Siege of Southern Gates)

### T-05: TC Accumulation → Church Dominion → Political Restructuring
**Chain:** TC passive advance (+1/season conditional) + Piety Yield from high-CV territories → TC thresholds (40 = Coup Counter trigger, 60 = Seizure active, 75 = freeze/transition, 100 = Theocracy Unification Attempt) → Church territorial expansion → Accord effects in seized territories → faction displacement → political landscape transformation
**Systems:** conviction_track, tc_political_redesign, victory, faction_layer, peninsular_strain (Accord), npc_behavior (Church priority trees)
**What it means:** The Church expands by default. TC rises from institutional momentum. Every other faction must actively suppress it or accept Church dominion. The suppression tools (Varfell Counter-Narrative, Hafenmark Parliamentary Challenge, Baralta Mandate ≥ 4 brake) each have costs. Ignoring TC is a viable short-term strategy that produces long-term crisis.
**Arc register vectors:** ARC-P01, ARC-S03, ARC-S19, ARC-T10, ARC-T14

### T-06: IP Accumulation → Altonian Intervention → External Pressure
**Chain:** IP baseline advance + civil war signals (IP +3/season during inter-faction battles) + TC ≥ 60 signal (IP +2/season) → IP thresholds (30 = Tutoring Demand, 75 = Vanguard deployment, 100 + AER ≤ 1 = Conquest) → external military pressure → resource diversion from sovereignty contest → expedition maintenance endangered → WC advancement stalled → RS recovery stalled
**Systems:** peninsular_strain, victory, mass_battle, wc_survival_spine
**What it means:** The peninsula's civil wars invite foreign intervention. IP is the mechanism by which Contest 1 (sovereignty) interferes with Contest 2 (survival) — civil war raises IP, which demands military attention, which diverts resources from WC advancement.
**Arc register vectors:** ARC-P06, ARC-T02

### T-07: Peninsular Strain → Accord Erosion → Governance Collapse
**Chain:** Battles advance Strain → Strain thresholds (3 = Mandate checks, 5 = Accord −1, 7 = Accord −1 all non-capitals, 9 = Accord cap at 2 + RS −1/season) → Accord erosion → governance difficulty → more instability → more battles → more Strain
**Systems:** peninsular_strain, faction_layer, settlement_layer, victory (Peninsular Sovereignty requires Accord ≥ 2)
**What it means:** War destroys the capacity to govern. Sustained military conflict produces a positive feedback loop where the population's willingness to be governed (Accord) erodes, making further conflict more likely. The universal victory condition (Peninsular Sovereignty) requires Accord ≥ 2 in all provinces — Strain 9+ caps Accord at 2 in non-capitals, making victory possible only by ending the war.

---

## III. INSTITUTIONAL THROUGHLINES

How each faction's identity produces mechanical consequences across systems.

### T-08: Church as Rendering Reinforcement
**Chain:** Faith Conviction → Certainty 5 selection → TC generation → CV maintenance → Heresy Investigation → AP accumulation → Thread suppression → population TS suppression → practitioner scarcity → reduced Thread capability → Church institutional dominance
**Systems:** conviction_track, npc_behavior (Church priority tree), params_core (Certainty Track), fieldwork (Exposure → AP), faction_politics_expanded (Church rank ladder requires Certainty), threadwork (Church Heresy Investigation via TC trigger PP-182)
**What it means:** The Church's institutional function is rendering-reinforcement. Every mechanism it controls — CV maintenance, Heresy Investigation, Excommunication, Certainty-indexed rank advancement — works to prevent the population from perceiving the substrate. This is not malice; it is the institutional expression of Faith Conviction. The Church genuinely believes rendering is sufficient.

### T-09: Varfell as Thread Progressive
**Chain:** VTM advancement → WR advancement → WC advancement → RS recovery → Thread capability improvement → more VTM advancement
**Systems:** victory (WR/WC tracks), faction_politics_expanded (Warden ladder, VTM), threadwork (WC effects), npc_behavior (Varfell priority tree, Vaynard arc)
**What it means:** Varfell is the faction whose institutional interest aligns with substrate maintenance. The three Vaynard paths (Intelligence, Southernmost, Thread Supremacy) represent different strategies for this alignment. Path B (Southernmost Dominion) makes WC Varfell's primary objective — the faction whose political interest IS the survival contest.
**Arc register vectors:** ARC-S01, ARC-S13, ARC-S16, ARC-S27, ARC-T21

### T-10: Niflhel as Accelerationist
**Chain:** Harvest (Dissolution Residue collection) → RS acceleration → substrate instability → more Gaps → more threadcut beings → more Harvest material → Niflhel capability growth
**Systems:** npc_behavior (§8.8 Niflhel priority tree with Harvest gate), wc_survival_spine, rs_budget, arc_expansion (Quiet One arc)
**What it means:** Niflhel is the only faction whose strategic interest structurally diverges from RS preservation. Their Harvest requires Dissolution — the operation that damages the substrate most. The RS-monitoring subroutine in §8.8 gates Harvest intensity, but the structural incentive remains: Niflhel benefits from substrate damage up to the point of Rupture.
**Arc register:** The Quiet One (arc_expansion_v1) — Thread extraction operative

### T-11: Crown as Pragmatic Instrumentalist
**Chain:** Royal Decree + Thread Liaison + institutional succession → Thread-as-tool when advantageous, Thread-as-threat when dangerous → reactive rather than principled Thread engagement
**Systems:** params_board_game (Crown Thread Liaison, Royal Decree), npc_behavior (Crown priority tree, Almud arc), victory (Crown victory conditions)
**What it means:** The Crown's relationship to Thread is determined by political context, not ontological commitment. Thread Liaison allows the Crown to benefit from allied Thread operations without institutional Thread commitment. Almud's potential Discovery Event (ARC-S17: TS 28→30) is the moment where the instrumentalist position fails — the King cannot treat Thread as a tool once he perceives it directly.
**Convergence markers:** COLLISION B (Practitioner King), COLLISION F (Succession Triangle)

---

## IV. PERSONAL THROUGHLINES

Individual-scale chains that shape the player and NPC experience.

### T-12: The Practitioner Arc (Depletion-Recovery Loop)
**Chain:** TS growth → Coherence depletion from operations → threshold effects (Dissonant at 5, Fractured at 3, Severed at 1) → Rendering Crisis → Anchoring Scenes → resolution → −1 TS permanent → recovery → resume operations → TS growth continues
**Systems:** threadwork (Coherence, Crisis), npc_behavior (§4.3 Coherence AI thresholds), params_core (Coherence 0 transition), player_agency (Conviction × Thread events)
**What it means:** The practitioner career is cyclical. Each cycle transforms the practitioner — they are not the same being after a Crisis. The −1 TS cost of recovery is the price of pulling back from the substrate. For NPCs, the Coherence AI thresholds (ED-672) govern self-limitation. For the player, the four narrative beats (ED-681) make the cycle experientially meaningful.
**Arc register vectors:** ARC-S04 (Rendering Debt), ARC-S34 (Edeyja Burnout)

### T-13: Certainty as Ontological Journey
**Chain:** Starting Certainty (from lifepath, ED-678) → Thread witnessing triggers (−1 per first witnessing, First Leap, Coherence 0 event, Southernmost exposure) → Certainty descent (5→0) → epistemic transformation → dialogue availability shifts (Certainty Gate) → institutional relationship changes (Church hostility at C0, Thread-community acceptance) → Conviction Scar susceptibility changes (+1 Scar at C5, −1 at C0)
**Systems:** params_core (Certainty Track), character_histories (lifepath derivation), investigation_systems (Filter 1, Gate Type 4), npc_behavior (§3.4 Certainty scaling on Scars), fieldwork (Certainty-indexed NPC responses)
**What it means:** The Certainty Track is the game's measure of ontological transformation. It is not a skill or a stat — it is the character's answer to the question "what is real?" The journey from C5 (orthodox) to C0 (Thread-accepted) cannot be reversed (A11, epistemic seduction). Each step opens capabilities and closes relationships.

### T-14: Conviction as Moral Architecture
**Chain:** Conviction type (Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity) → NPC Conviction Scar accumulation from social + Thread events (§3.3, §3.4) → threshold effects (1 Scar = internal conflict, 2 = arc transition, 3+ = crisis) → arc emergence → NPC behavioral transformation → faction-level consequences (Framework Drift, Stability triggers)
**Systems:** npc_behavior (§3, §5), player_agency (§2 Convictions), companion_specification (§6.1 departure triggers), social_contest (Conviction Track, Composure)
**What it means:** Conviction is the NPC's deepest commitment — what they will not abandon without being scarred. The Scar system produces emergent narrative: an NPC who accumulates 3 Scars enters crisis, acts unpredictably, and may transform. Thread operations now feed this system (§3.4), meaning the game's most powerful actions produce the most dramatic NPC responses.

### T-15: Player Progression (Cell → Faction)
**Chain:** Standing 0 (nobody) → Renown accumulation → Standing advancement → settlement governance → provincial authority → faction emergence
**Systems:** faction_politics_expanded (rank ladders 0–7), player_agency (Stature, Renown), settlement_layer (§6 Player Progression), bridge_part1_revisions (Renown track)
**What it means:** The player starts as an individual within an existing faction. Through Standing and Renown, they rise to institutional authority. At Standing 6–7, they may found their own faction. The progression is the game's answer to "why does my character matter?" — you begin as a rendered being subject to institutions, and you end as a being who shapes the rendering itself.

---

## V. RELATIONAL THROUGHLINES

Chains that operate through social bonds.

### T-16: Knot Propagation
**Chain:** Knot formation (Thread bond) → NPC TS transformation → Knot Strain propagation to all bonded contacts (§5.0b) → Scar accumulation in strained NPCs → arc transitions → faction behavioral shifts → Domain Echo
**Systems:** threadwork (Knot mechanics), npc_behavior (§5.0b, §3.4), companion_specification (departure triggers), fieldwork (§2.6 Knot-mediated remote investigation), social_contest (Solidarity Resonant Style)
**What it means:** Relationships are not flavor — they are mechanical bonds. A Knot between the player and an NPC means that the player's Thread transformation strains the NPC, and the NPC's transformation strains the player. The consequence chain is recursive: my Knot partner's crisis becomes my strain, which becomes my arc trigger, which becomes my Knot partner's strain.

### T-17: Companion as Moral Mirror
**Chain:** Companion formation (Disposition ≥ +3, Companionship Scene) → companion Conviction → companion witnesses player Thread actions → Thread departure triggers (Faith/Order/Equity → Dissolution/Lock; Reason/Precedent → POP) → departure scene → Grief Mechanic → player Conviction strained
**Systems:** companion_specification (§6.1 Thread departure), npc_behavior (§3.4 Thread Scar), player_agency (Conviction × Thread events)
**What it means:** The companion is the player's moral consequence made personal. A practitioner who Dissolves a living being in front of a Faith-Conviction companion loses that companion — no appeal, no recovery. The system forces the player to choose: Thread power or relational bonds.

---

## VI. GEOGRAPHIC THROUGHLINES

Chains that operate through space.

### T-18: Radiation Gradient
**Chain:** RS band change → calamity_radiation matrix lookup by territory proximity → per-territory effects (Ob modifiers, spontaneous Gaps, threadcut beings, rendering failures) → settlement Order effects (ED-675) → governance difficulty → Accord erosion → victory condition interaction
**Systems:** calamity_radiation, settlement_layer (§4.4), fieldwork (§3.4 Rendering Strain), npc_behavior (NPC reactions to radiation effects), conviction_track (Calamity Drift §1.3 + Thread CV Drift §1.3b)
**What it means:** The Calamity is not a past event — it is a geographic condition that worsens as RS declines. The radiation gradient means the south feels the substrate damage before the north. This creates geographic asymmetry: southern factions (Varfell, Wardens) experience the survival contest directly while northern factions (Crown, Hafenmark) experience it abstractly — until RS drops low enough to reach them.

### T-19: Southernmost as Hidden Front
**Chain:** RS decay → Southernmost Spiral (ARC-S15: RS ≤ 50 → cracking timeline) → Expedition required → military escort required → IP diverts military attention → expedition endangered → WC advancement stalled → RS recovery stalled → more decay
**Systems:** params_southernmost, wc_survival_spine, rs_budget, victory (WR/WC tracks), mass_battle (Southernmost §A.11)
**What it means:** The Southernmost is where the survival contest is fought. Expeditions to Askeheim are the mechanism for WC advancement. But expeditions require practitioners (TS 30+), military escort, and faction support — all of which compete with the sovereignty contest. The Southernmost is the place where the two contests physically converge.
**Arc register:** ARC-S15 (Spiral), ARC-S34 (Edeyja Burnout), TE-12 (Collector's Chokehold), TE-13 (Warden Threshold)

---

## VII. STRATEGIC THROUGHLINES

Chains that produce emergent strategic dynamics.

### T-20: The Two Contests
**Chain:** Sovereignty contest (territorial control, faction stats, victory conditions) competes with survival contest (RS maintenance, WC advancement, expedition support) for the same resources (military, actions, practitioner Coherence, player time)
**Systems:** wc_survival_spine, rs_budget, victory, peninsular_strain (IP/expedition tension), player_agency (Scene Slate — thread-state vs duty-aligned scenes)
**What it means:** This is the game's central strategic architecture. A player who optimizes for sovereignty ignores WC and RS, risking Rupture. A player who optimizes for survival sacrifices political position. The tension is unresolvable — the player must manage both contests simultaneously with insufficient resources for either. WC 3 is the only endgame survival path, and it requires cross-faction cooperation that the sovereignty contest discourages.

### T-21: Thread Political Warfare
**Chain:** Shared RS track → any faction's Thread aggression damages all factions → mutual deterrence → Lock-and-cede (deny territory by making it ungovernable) → Thread brinksmanship (bait enemy into RS-costly operations) → Niflhel as accelerationist (Harvest = RS damage as resource)
**Systems:** npc_behavior (§8.5 Varfell brinksmanship, §8.8 Niflhel Lock-and-cede/Harvest gate, §8.10 Warden RS override), rs_budget, wc_survival_spine
**What it means:** The shared RS track creates a geopolitical doctrine. Aggressive Thread warfare is a credible threat against all factions including the attacker. The strategic behaviors (Lock-and-cede, brinksmanship, Harvest) are not exploits — they are coherent doctrines that the shared RS track generates. For videogame implementation, these must be NPC AI behaviors, not emergent player discoveries alone.
**Arc register:** ARC-S33 (Lattice of Enemies)

### T-22: Belief Lattice → Collective Failure
**Chain:** Practitioners have Beliefs → Beliefs may conflict → collective Thread operations require Belief compatibility checks → directly opposing Beliefs block collaboration → at RS Critical, survival requires cross-faction practitioner cooperation → but practitioners from opposing factions have opposing Beliefs → the world can only be saved by Belief revision, which is a personal transformation, not a political act
**Systems:** threadwork (§2.5 Collective Operations, Belief checks), npc_behavior (Belief revision §3.2), params_core (Certainty Track), arc_register (ARC-S33)
**What it means:** The endgame's deepest throughline. The substrate's survival requires collective action. Collective action requires Belief compatibility. Belief revision requires confrontation and Scar accumulation — the very process that destabilizes NPCs. The practitioners who must save the world can only cooperate after their institutional commitments have been broken by the crisis itself. The lattice cannot be dissolved by politics, only by personal transformation.

---

## VIII. NARRATIVE THROUGHLINES

Chains that produce emergent story.

### T-23: NPC Arc Emergence
**Chain:** NPC Stance Triangle → Conviction → Scar accumulation (social + Thread) → threshold crossing → arc state transition (A→B→C) → behavioral change → faction-level consequences → Domain Echo → political landscape shift → new NPC arc triggers
**Systems:** npc_behavior (§5 Arc Emergence), arc_expansion (full arc profiles for 20+ NPCs), arc_register (faction vectors), social_contest (Composure/Conviction Track), companion_specification
**What it means:** NPCs are not static. Their arcs emerge from accumulated game state — Scar count, Certainty, TS threshold crossings, faction Stability. The arc system is a state machine driven by mechanical inputs. In a videogame, this produces emergent narrative without scripted events: the NPC's arc unfolds because the world pushed them there, not because a writer decided it.

### T-24: Convergence as Emergent Crisis
**Chain:** Multiple independent vectors → simultaneous threshold crossing → combined pressure qualitatively different from components → emergent crisis
**Systems:** arc_register (§VI Convergence Markers — 7+ defined collisions), all faction/territory vectors
**What it means:** The game's biggest narrative moments are not designed — they are structural. COLLISION C (Tutoring + Southernmost) produces RS +8, IP +2, TC +2 in a single season — none of the component vectors predict this combined effect. COLLISION J (Church Siege of Southern Gates) produces the paradox where the Church's political victory destabilizes the substrate through which it is winning. These convergences are the game's emergent narrative engine.

### T-25: The Generational Arc
**Chain:** 30-year game span → Generational Shift clock (+1 per 5 years) → original leaders age (−1/−2/−3 to highest attribute) → succession fires → player's generation becomes the leadership class → player-founded factions become primary actors → the peninsula's political landscape is the player's creation
**Systems:** settlement_layer (§7 Extended Timeline, §7.2 Succession), npc_behavior (arc profiles for succession NPCs), faction_politics_expanded (Torben's Readiness Track, Baralta succession), player_agency (Stature progression)
**What it means:** The game's longest throughline. The first leaders (Almud, Baralta, Vaynard, Himlensendt) are not permanent — they will weaken, retire, or die. The player who rises from Standing 0 to Standing 7 over 30 years IS the succession. The game's endpoint is not "who won" but "what world did the player build?"

---

## THROUGHLINE INTERACTION MATRIX

Where throughlines intersect, the game's deepest strategic dynamics emerge.

| | T-04 RS Decay | T-05 TC | T-06 IP | T-08 Church | T-09 Varfell | T-12 Practitioner | T-20 Two Contests |
|---|---|---|---|---|---|---|---|
| **T-04 RS Decay** | — | TC Seizure in radiation zones | IP diverts from expedition | Church expands into unstable territory | Varfell RS recovery efforts | Practitioner Coherence spent on Mending | Survival contest's driver |
| **T-05 TC** | — | — | TC ≥ 60 → IP +2/season | Church institutional strength | Varfell Counter-Narrative | Thread ops → TC trigger (PP-182) | Sovereignty contest's Church axis |
| **T-06 IP** | IP diverts military from RS tasks | TC feeds IP | — | Church territory provides Altonian targets | Varfell border territories exposed | Practitioners diverted to combat | External pressure on both contests |
| **T-12 Practitioner** | Mending = only individual RS recovery | Thread ops risk TC trigger | War depletes Coherence | Church suppresses practitioners | Varfell employs practitioners | — | Practitioners serve both contests |
| **T-20 Two Contests** | RS is survival axis | TC is sovereignty axis | IP connects contests | Church wins sovereignty but may lose survival | Varfell wins survival but may lose sovereignty | Practitioner resources split between contests | — |

---

## COMPLETENESS CHECK

| Throughline | Arc Register Coverage | System Doc Coverage | Implementation Status |
|---|---|---|---|
| T-01 Everything Is Thread | Implicit in all vectors | Explicit in combat §10, fieldwork §2.4 | Partially framed |
| T-02 Rendering = Consciousness | Implicit | investigation (Filter 1), fieldwork (Intelligibility) | Fully implemented |
| T-03 Inseparability | All Thread vectors | threadwork (co-movement tables) | Fully implemented |
| T-04 RS Decay | ARC-P02, S15, S32, S34 | rs_budget, calamity_radiation | Fully implemented |
| T-05 TC Accumulation | ARC-P01 | tc_political_redesign, conviction_track | Fully implemented |
| T-06 IP Accumulation | ARC-P06 | peninsular_strain §3.2 | Implemented; base rate GAP noted |
| T-07 Peninsular Strain | Not covered | peninsular_strain §4 | Fully implemented |
| T-08 Church Rendering | ARC-S03, S06, S08, S09, etc. | npc_behavior (Church tree), conviction_track | Fully implemented |
| T-09 Varfell Progressive | ARC-S01, S13, S27 | victory §6 (WR/WC), faction_politics (Warden ladder) | Fully implemented |
| T-10 Niflhel Accelerationist | Quiet One (arc_expansion) | npc_behavior §8.8 (Harvest gate) | Implemented (ED-679) |
| T-11 Crown Instrumentalist | ARC-S14, S17, S28, S45 | params_board_game (Thread Liaison) | Implemented |
| T-12 Practitioner Arc | ARC-S04, S34 | threadwork §3 (Coherence), npc_behavior §4.3 | Implemented (ED-672, ED-681) |
| T-13 Certainty Journey | Implicit in Thread vectors | params_core (Certainty Track), character_histories (ED-678) | Fully implemented |
| T-14 Conviction Architecture | All NPC arc profiles | npc_behavior §3, §5 (Scars, Arc Emergence) | Implemented (ED-670) |
| T-15 Player Progression | Not covered (player, not arc) | faction_politics (ladders), settlement_layer §6 | Fully implemented |
| T-16 Knot Propagation | Implicit | npc_behavior §5.0b, threadwork (Knot mechanics) | Implemented |
| T-17 Companion Moral Mirror | Not covered | companion_specification §6.1 (Thread departure) | Implemented (ED-666) |
| T-18 Radiation Gradient | ARC-S15 | calamity_radiation (full matrix) | Fully implemented |
| T-19 Southernmost Hidden Front | ARC-S15, S34 | params_southernmost, wc_survival_spine | Implemented |
| T-20 Two Contests | ARC-S32, S33 | wc_survival_spine (explicit), rs_budget | Implemented (ED-669) |
| T-21 Thread Political Warfare | ARC-S33 | npc_behavior §8 (priority tree amendments) | Implemented (ED-679) |
| T-22 Belief Lattice | ARC-S33 | threadwork §2.5 (Collective Operations) | Implemented |
| T-23 NPC Arc Emergence | All faction vectors | npc_behavior §5, arc_expansion | Fully implemented |
| T-24 Convergence as Crisis | §VI Convergence Markers (7+) | arc_register | Fully specified |
| T-25 Generational Arc | Not covered | settlement_layer §7 (Extended Timeline) | Implemented |

**Count: 25 throughlines identified. 25/25 have mechanical implementation. 0 throughlines are purely aspirational.**

---

*Every throughline has at least partial system documentation and mechanical implementation. The game's constitutive chains are structurally complete. What remains is simulation validation (do the chains produce the intended dynamics at the intended rates?) and constitutive framing (do the system documents describe their mechanics in Thread terms?).*
