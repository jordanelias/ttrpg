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
**Chain:** Foundations A6 / P-03 → investigation Five-Filter Chain → Truth gates → TS perception tiers → player's perceptual horizon
**Systems:** investigation_systems, fieldwork, player_agency, threadwork visibility, calamity_radiation
**What it means:** The player does not see "the world" — they see what their character's rendering can present. Truth determines which utterances are available. TS determines what thread events are visible. The radiation matrix produces different perceptual experiences at different RS bands. The game's information architecture IS the rendering.
**Implementation status:** Fully implemented in investigation_systems (Filter 1, Truth/TS gates), fieldwork (Intelligibility Gradient), threadwork (visibility table + ED-677 rendered-level extension), calamity_radiation (environmental rendering by band). Player_agency Scene Slate now factors thread-state (ED-674).

**Extension (2026-04-20 ED-729, ED-730).** T-02 grounds the setting's epistemology; its canonical grounding is now specified in `canon/00_philosophical_foundations.md` §4.3 (Confrontation as Constitutive Finitude) and `canon/02_foundations_amendment_leap_mechanism.md` Amendment 1 (reflexive vs outward layer-2 facings). The rendering's finitude is constitutive, not a capacity limitation. Consequence: confrontation with excess being does not damage; only operation against substrate tendency does. Same structural principle recurs at multiple output surfaces (visual per-character filtering, textual Seam Text TS-gating, narrative chronicler divergence, historical tradition split, mechanical auto-effect axes) — the consistency of recurrence is itself the world's ontology becoming legible to the player.

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
**Systems:** ms_budget, calamity_radiation, peninsular_strain, settlement_layer, faction_layer, victory, mass_battle
**What it means:** The world is dying. The decay is structural — it comes from the Calamity's unhealed damage, not from player action. Player action (battle, Thread operations) accelerates it. Only Mending and WC slow it. This is the positive feedback loop that makes the survival contest urgent.
**Arc register vectors:** ARC-P02, ARC-S15, ARC-S32, ARC-S34
**Convergence markers:** COLLISION C (Tutoring + Southernmost), COLLISION J (Church Siege of Southern Gates)

### T-05: TC Accumulation → Church Dominion → Political Restructuring
**Chain:** TC passive advance (+1/season conditional) + Piety Yield from high-CV territories → TC thresholds (40 = Coup Counter trigger, 60 = Seizure active, 75 = freeze/transition, 100 = Theocracy Unification Attempt) → Church territorial expansion → Accord effects in seized territories → faction displacement → political landscape transformation
**Systems:** conviction_track, tc_political_redesign, victory, faction_layer, peninsular_strain (Accord), npc_behavior (Church priority trees)
**What it means:** The Church expands by default. TC rises from institutional momentum. Every other faction must actively suppress it or accept Church dominion. The suppression tools (Varfell Counter-Narrative, Hafenmark Parliamentary Challenge, Baralta Mandate ≥ 4 brake) each have costs. Ignoring TC is a viable short-term strategy that produces long-term crisis.
**Arc register vectors:** ARC-P01, ARC-S03, ARC-S19, ARC-T10, ARC-T14

### T-06: IP Accumulation → Altonian Intervention → External Pressure
**Chain:** IP baseline advance + civil war signals (IP +3/season during inter-faction battles) + TC ≥ 60 signal (IP +2/season) → IP thresholds (30 = Tutoring Demand, 75 = Vanguard deployment, 100 + Altonian diplomacy ≤ 1 = Conquest) → external military pressure → resource diversion from sovereignty contest → expedition maintenance endangered → WC advancement stalled → RS recovery stalled
**Systems:** peninsular_strain, victory, mass_battle, wc_survival_spine
**What it means:** The peninsula's civil wars invite foreign intervention. IP is the mechanism by which Contest 1 (sovereignty) interferes with Contest 2 (survival) — civil war raises IP, which demands military attention, which diverts resources from WC advancement.
**Arc register vectors:** ARC-P06, ARC-T02

### T-07: Turmoil → Accord Erosion → Governance Collapse
**Chain:** Battles advance Strain → Strain thresholds (3 = Mandate checks, 5 = Accord −1, 7 = Accord −1 all non-capitals, 9 = Accord cap at 2 + RS −1/season) → Accord erosion → governance difficulty → more instability → more battles → more Strain
**Systems:** peninsular_strain, faction_layer, settlement_layer, victory (Peninsular Sovereignty requires Accord ≥ 2)
**What it means:** War destroys the capacity to govern. Sustained military conflict produces a positive feedback loop where the population's willingness to be governed (Accord) erodes, making further conflict more likely. The universal victory condition (Peninsular Sovereignty) requires Accord ≥ 2 in all provinces — Strain 9+ caps Accord at 2 in non-capitals, making victory possible only by ending the war.

---

## III. INSTITUTIONAL THROUGHLINES

How each faction's identity produces mechanical consequences across systems.

### T-08: Church as Rendering Reinforcement
**Chain:** Faith Conviction → Truth 5 selection → TC generation → CV maintenance → Heresy Investigation → AP accumulation → Thread suppression → population TS suppression → practitioner scarcity → reduced Thread capability → Church institutional dominance
**Systems:** conviction_track, npc_behavior (Church priority tree), params_core (Truth Track), fieldwork (Exposure → AP), faction_politics_v30 (Church rank ladder requires Truth), threadwork (Church Heresy Investigation via TC trigger PP-182)
**What it means:** The Church's institutional function is rendering-reinforcement. Every mechanism it controls — CV maintenance, Heresy Investigation, Excommunication, Truth-indexed rank advancement — works to prevent the population from perceiving the substrate. This is not malice; it is the institutional expression of Faith Conviction. The Church genuinely believes rendering is sufficient.

**Extension (2026-04-20 ED-730, ED-733, ED-735).** The Church's rendering-reinforcement is driven by a specific category-identification error named in `canon/02_foundations_amendment_leap_mechanism.md` Amendment 5: the Church collapses confrontation (perception) with operation (substrate engagement), and within operation collapses restorative / manipulative / destructive types into a single suspect category. The error is sincere and theologically coherent — the Church's Ficinian Cardinal emanation self-understanding (ED-733, canonical) is a genuine theological structure — but structurally incorrect at the framework layer. This conflation is the *generative engine* of the design: it produces the Perceptual Prophylaxis, the moral terror, the Heresy Investigation machinery, and the recursive rediscovery dynamic (T-26). Player mechanical consequences are distributed across Truth pressure in Church territory, Miracle Investigation aporia (§22.1 consolidated guide), triple-interpretation faction conflict, Rendering Strain, and the suppressed Practitioner Witness Tradition (`systems/world/worldbuilding_v30.md` §3.7).

### T-09: Varfell as Thread Progressive
**Chain:** VTM advancement → WR advancement → WC advancement → RS recovery → Thread capability improvement → more VTM advancement
**Systems:** victory (WR/WC tracks), faction_politics_v30 (Warden ladder, VTM), threadwork (WC effects), npc_behavior (Varfell priority tree, Vaynard arc)
**What it means:** Varfell is the faction whose institutional interest aligns with substrate maintenance. The three Vaynard paths (Intelligence, Southernmost, Thread Supremacy) represent different strategies for this alignment. Path B (Southernmost Dominion) makes WC Varfell's primary objective — the faction whose political interest IS the survival contest.
**Arc register vectors:** ARC-S01, ARC-S13, ARC-S16, ARC-S27, ARC-T21

### T-10: STRUCK — Niflhel Dissolved
**STRUCK** (conflict_architecture_proposal). Niflhel dissolved as faction. Thread Harvest replaced by settlement-level Thread exploitation sites. Quiet One becomes independent settlement-tied NPC.

### T-11: Crown as Pragmatic Instrumentalist
**Chain:** Royal Decree + Thread Liaison + institutional succession → Thread-as-tool when advantageous, Thread-as-threat when dangerous → reactive rather than principled Thread engagement
**Systems:** params_board_game (Crown Thread Liaison, Royal Decree), npc_behavior (Crown priority tree, Almud arc), victory (Crown victory conditions)
**What it means:** The Crown's relationship to Thread is determined by political context, not ontological commitment. Thread Liaison allows the Crown to benefit from allied Thread operations without institutional Thread commitment. Almud's potential Discovery Event (ARC-S17: TS 28→30) is the moment where the instrumentalist position fails — the King cannot treat Thread as a tool once he perceives it directly.
**Convergence markers:** COLLISION B (Practitioner King), COLLISION F (Succession Triangle)

---

## IV. PERSONAL THROUGHLINES

Individual-scale chains that shape the player and NPC experience.


### T-15b: Löwenritter as Substrate-Agnostic Protector
**Chain:** Martial Honour oath ("Valoria endures, whatever the cost") → governance authority from institutional duty and military capability, not theology or substrate engagement → substrate is irrelevant to national defense → graduated autonomy driven by Crown competence, not Thread politics → Thread revelation: the crisis destroying Valoria has a substrate cause → military tools cannot address substrate decay → forced choice: adapt mission to include substrate defense (requires cooperation with Varfell/Wardens, compromises martial identity) OR maintain military-only mission (fight symptoms while ignoring cause)
**Systems:** params/bg/core (graduated autonomy table), npc_behavior_v30 §2.5 (Ehrenwall: Truth 4, TS 0, Martial Honour), params/bg/npc_priority_trees (Löwenritter P1-P7), params/bg/institutions (Riskbreakers, Lions' Council), victory_v30 §3.6 (Military Regency)
**What it means:** Löwenritter is the Praetorian faction — governance authority derives from the duty to protect, not from faith, divine right, or substrate knowledge. The substrate is irrelevant because national defense is about military capability and institutional loyalty. Ehrenwall's Truth 4 and TS 0 mean she shares conventional Solmundian piety but has zero substrate engagement — her oath is temporal, not metaphysical. The graduated autonomy progression (Loyal→Restless→Autonomous→Split) is driven entirely by Crown competence and military action, never by Thread politics. Thread revelation is Löwenritter's identity crisis: if the existential threat to Valoria is substrate decay, then the military order dedicated to Valoria's survival is fighting the wrong war. The faction whose identity is "protect Valoria at any cost" discovers the cost may be abandoning everything that makes them Löwenritter — martial identity, institutional independence, the belief that strength protects.
**Arc register vectors:** Ehrenwall Arc A/B/C (npc_behavior_v30 §2.5)


### T-15c: RM as Substrate-Heritage Reclaimer
**Chain:** Einhir cultural suppression → community rebuilds governance through consensus cells → hidden Thread-site bonus (threadwork_v30 §5.6): RM governance works better at certain sites without knowing why → Thread revelation: the Einhir heritage was substrate-connected all along → forced choice: Embrace (Thread access validates cultural identity, but risks becoming another faith-governance claim like Church) OR Denial (remain purely political movement, abandon deepest source of cultural identity) OR Schism (movement splits between those who embrace Thread and those who reject it)
**Systems:** victory_v30 §3.5 (Cultural Revolution, RS ≥ 25), settlement_layer_v30 §3.3/§4.3 (consensus cells, RM settlement presence), npc_behavior_v30 §2.6 (Vossen: Truth 2 Skeptic, TS 0, Equity/Continuity), threadwork_v30 §5.6 (hidden Thread-site bonus), params/bg/npc_priority_trees (RM P1-P4)
**What it means:** RM's substrate-posture is unknowing inheritance — the Einhir cultural practices that the Church suppressed were connected to the substrate, but RM rebuilds them as political tradition, not metaphysics. Vossen's Truth 2 (Skeptic) means she already doubts the Solmundian framework that condemned her people, but she has no Thread sensitivity to access what her heritage actually was. The hidden Thread-site bonus is the mechanical expression: RM governance produces better outcomes at Thread-proximate settlements for reasons no one in the movement understands. Thread revelation is simultaneously RM's vindication and its deepest crisis. N5 (The Forgetting) makes this structurally unique among factions: every other faction's substrate-posture is conscious (Church reinforces rendering, Varfell pursues Thread, Crown uses it instrumentally, Hafenmark rejects ecclesial mediation, Löwenritter ignores it). RM is the only faction whose substrate-posture is unconscious — they're doing substrate-aligned governance without knowing it, which means revelation transforms their self-understanding more radically than any other faction.
**Arc register vectors:** Vossen Arc A/B/C (npc_behavior_v30 §2.6), T-11 (RM Identity Arc)

### T-12: The Practitioner Arc (Depletion-Recovery Loop)
**Chain:** TS growth → Coherence depletion from operations → threshold effects (Dissonant at 5, Fractured at 3, Severed at 1) → Rendering Crisis → Anchoring Scenes → resolution → −1 TS permanent → recovery → resume operations → TS growth continues
**Systems:** threadwork (Coherence, Crisis), npc_behavior (§4.3 Coherence AI thresholds), params_core (Coherence 0 transition), player_agency (Conviction × Thread events)
**What it means:** The practitioner career is cyclical. Each cycle transforms the practitioner — they are not the same being after a Crisis. The −1 TS cost of recovery is the price of pulling back from the substrate. For NPCs, the Coherence AI thresholds (ED-672) govern self-limitation. For the player, the four narrative beats (ED-681) make the cycle experientially meaningful.
**Arc register vectors:** ARC-S04 (Rendering Debt), ARC-S34 (Edeyja Burnout)

### T-13: Truth as Ontological Journey
**Chain:** Starting Truth (from lifepath, ED-678) → Thread witnessing triggers (−1 per first witnessing, First Leap, Coherence 0 event, Southernmost exposure) → Truth descent (5→0) → epistemic transformation → dialogue availability shifts (Truth Gate) → institutional relationship changes (Church hostility at C0, Thread-community acceptance) → Conviction Scar susceptibility changes (+1 Scar at C5, −1 at C0)
**Systems:** params_core (Truth Track), character_histories (lifepath derivation), investigation_systems (Filter 1, Gate Type 4), npc_behavior (§3.4 Truth scaling on Scars), fieldwork (Truth-indexed NPC responses)
**What it means:** The Truth Track is the game's measure of ontological transformation. It is not a skill or a stat — it is the character's answer to the question "what is real?" The journey from C5 (orthodox) to C0 (Thread-accepted) cannot be reversed (A11, epistemic seduction). Each step opens capabilities and closes relationships.

### T-14: Conviction as Moral Architecture
**Chain:** Conviction type (Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity) → NPC Conviction Scar accumulation from social + Thread events (§3.3, §3.4) → threshold effects (1 Scar = internal conflict, 2 = arc transition, 3+ = crisis) → arc emergence → NPC behavioral transformation → faction-level consequences (Framework Drift, Stability triggers)
**Systems:** npc_behavior (§3, §5), player_agency (§2 Convictions), companion_specification (§6.1 departure triggers), social_contest (Piety Track, Composure)
**What it means:** Conviction is the NPC's deepest commitment — what they will not abandon without being scarred. The Scar system produces emergent narrative: an NPC who accumulates 3 Scars enters crisis, acts unpredictably, and may transform. Thread operations now feed this system (§3.4), meaning the game's most powerful actions produce the most dramatic NPC responses.

### T-15: Player Progression (Cell → Faction)
**Chain:** Standing 0 (nobody) → Renown accumulation → Standing advancement → settlement governance → provincial authority → faction emergence
**Systems:** faction_politics_v30 (rank ladders 0–7), player_agency (Stature, Renown), settlement_layer (§6 Player Progression), bridge_part1_revisions (Renown track)
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
**Systems:** params_southernmost, wc_survival_spine, ms_budget, victory (WR/WC tracks), mass_battle (Southernmost §A.11)
**What it means:** The Southernmost is where the survival contest is fought. Expeditions to Askeheim are the mechanism for WC advancement. But expeditions require practitioners (TS 30+), military escort, and faction support — all of which compete with the sovereignty contest. The Southernmost is the place where the two contests physically converge.
**Arc register:** ARC-S15 (Spiral), ARC-S34 (Edeyja Burnout), TE-12 (Collector's Chokehold), TE-13 (Warden Threshold)

---

## VII. STRATEGIC THROUGHLINES

Chains that produce emergent strategic dynamics.

### T-20: The Two Contests
**Chain:** Sovereignty contest (territorial control, faction stats, victory conditions) competes with survival contest (RS maintenance, WC advancement, expedition support) for the same resources (military, actions, practitioner Coherence, player time)
**Systems:** wc_survival_spine, ms_budget, victory, peninsular_strain (IP/expedition tension), player_agency (Scene Slate — thread-state vs duty-aligned scenes)
**What it means:** This is the game's central strategic architecture. A player who optimizes for sovereignty ignores WC and RS, risking Rupture. A player who optimizes for survival sacrifices political position. The tension is unresolvable — the player must manage both contests simultaneously with insufficient resources for either. WC 3 is the only endgame survival path, and it requires cross-faction cooperation that the sovereignty contest discourages.

### T-21: Thread Political Warfare
**Chain:** Shared RS track → any faction's Thread aggression damages all factions → mutual deterrence → Lock-and-cede (deny territory by making it ungovernable) → Thread brinksmanship (bait enemy into RS-costly operations) → Thread exploitation sites (settlement-level RS damage as tragedy-of-the-commons)
**Systems:** npc_behavior (§8.5 Varfell brinksmanship, §8.10 Warden RS override), ms_budget, wc_survival_spine
**What it means:** The shared RS track creates a geopolitical doctrine. Aggressive Thread warfare is a credible threat against all factions including the attacker. The strategic behaviors (Lock-and-cede, brinksmanship, Harvest) are not exploits — they are coherent doctrines that the shared RS track generates. For videogame implementation, these must be NPC AI behaviors, not emergent player discoveries alone.
**Arc register:** ARC-S33 (Lattice of Enemies)

### T-22: Belief Lattice → Collective Failure
**Chain:** Practitioners have Beliefs → Beliefs may conflict → collective Thread operations require Belief compatibility checks → directly opposing Beliefs block collaboration → at RS Critical, survival requires cross-faction practitioner cooperation → but practitioners from opposing factions have opposing Beliefs → the world can only be saved by Belief revision, which is a personal transformation, not a political act
**Systems:** threadwork (§2.5 Collective Operations, Belief checks), npc_behavior (Belief revision §3.2), params_core (Truth Track), arc_register (ARC-S33)
**What it means:** The endgame's deepest throughline. The substrate's survival requires collective action. Collective action requires Belief compatibility. Belief revision requires confrontation and Scar accumulation — the very process that destabilizes NPCs. The practitioners who must save the world can only cooperate after their institutional commitments have been broken by the crisis itself. The lattice cannot be dissolved by politics, only by personal transformation.

---

## VIII. NARRATIVE THROUGHLINES

Chains that produce emergent story.

### T-23: NPC Arc Emergence
**Chain:** NPC Stance Triangle → Conviction → Scar accumulation (social + Thread) → threshold crossing → arc state transition (A→B→C) → behavioral change → faction-level consequences → Domain Echo → political landscape shift → new NPC arc triggers
**Systems:** npc_behavior (§5 Arc Emergence), arc_expansion (full arc profiles for 20+ NPCs), arc_register (faction vectors), social_contest (Composure/Piety Track), companion_specification
**What it means:** NPCs are not static. Their arcs emerge from accumulated game state — Scar count, Truth, TS threshold crossings, faction Stability. The arc system is a state machine driven by mechanical inputs. In a videogame, this produces emergent narrative without scripted events: the NPC's arc unfolds because the world pushed them there, not because a writer decided it.

### T-24: Convergence as Emergent Crisis
**Chain:** Multiple independent vectors → simultaneous threshold crossing → combined pressure qualitatively different from components → emergent crisis
**Systems:** arc_register (§VI Convergence Markers — 7+ defined collisions), all faction/territory vectors
**What it means:** The game's biggest narrative moments are not designed — they are structural. COLLISION C (Tutoring + Southernmost) produces RS +8, IP +2, TC +2 in a single season — none of the component vectors predict this combined effect. COLLISION J (Church Siege of Southern Gates) produces the paradox where the Church's political victory destabilizes the substrate through which it is winning. These convergences are the game's emergent narrative engine.

### T-25: The Generational Arc
**Chain:** 30-year game span → Generational Shift clock (+1 per 5 years) → original leaders age (−1/−2/−3 to highest attribute) → succession fires → player's generation becomes the leadership class → player-founded factions become primary actors → the peninsula's political landscape is the player's creation
**Systems:** settlement_layer (§7 Extended Timeline, §7.2 Succession), npc_behavior (arc profiles for succession NPCs), faction_politics_v30 (Torben's Readiness Track, Baralta succession), player_agency (Stature progression)
**What it means:** The game's longest throughline. The first leaders (Almud, Baralta, Vaynard, Himlensendt) are not permanent — they will weaken, retire, or die. The player who rises from Standing 0 to Standing 7 over 30 years IS the succession. The game's endpoint is not "who won" but "what world did the player build?"


### T-26: Recursion as Setting Structure (TL-3)
**Chain:** Solmund threadwork → Church misidentification as miracle → Church founded on misidentification → Mending/Miraculous Event in game-present → threadwork misidentified again → new generation of scripture and Heresy Investigation on the same category error
**Systems:** faction AI (Church priority tree), conviction_track (Truth revision under contradictory evidence), POI system (Seam Text discovery), Miraculous Event response mechanic (per ED-735 integration workplan), arc register (Miracle Investigation arcs)
**What it means:** The Church is structurally reliving its founding error without recognising it, because the Perceptual Prophylaxis reproduces the perceptual conditions under which the original misidentification occurred. The recursion is not a narrative accident; it is the expected consequence of the category error in §T-08 Extension under a non-practitioner majority population. The recursion stops only when the prophylaxis cracks — which is a long-run player-influenceable variable, not a scripted beat.
**Implementation status:** Implicit in Miraculous Event cascade design (PR-14 bundle, pending integration). Needs explicit capture in Church priority tree and Miracle Investigation branching.
**Arc register vectors:** ARC-S32, ARC-S34, arcs touching Southernmost contact events.
**Source:** session_master_2026_04_20.md Part IV TL-3; ED-735.

### T-27: Effects Real, Explanation Wrong (TL-4)
**Chain:** Real observable effect in the rendered world → only institutionally-load-bearing explanation available to the observing faction → faction acts on the wrong explanation → effect continues producing real consequences under the wrong frame → incompatible factional explanations produce triple-interpretation conflict
**Systems:** faction AI (all factions; each has its own wrong frame), conviction_track (Truth under contradictory evidence), fieldwork (Thread-Read), investigation_systems (Filter chain), chronicler divergence
**What it means:** The dominant epistemic signature of the setting. Himmelenger's substrate cleanliness (d4 distance + Solmund's northern passage, not Church grace). Scripture (real acts through rendered shell). Baralta's successes (political skill, not divine favour). MS 72 (Wardens + baseline continuity, not doctrinal validation). Every real effect has a wrong, institutionally-load-bearing explanation available. Player information asymmetry (T-30) turns this into gameplay: the player sees the real mechanism while the characters see the available explanation.
**Implementation status:** Implicit in the triple-interpretation faction design. Seam Text gating operationalises the epistemic split (TS 0–29 reads explanation, TS 30+ reads effect). Needs Conviction Scar targeting tied to specific effect/explanation mismatches.
**Arc register vectors:** Distributed across faction-interpretation arcs; matrix placement deferred.
**Source:** session_master_2026_04_20.md Part IV TL-4.

### T-28: Confrontation / Leap / Operation Triad (TL-5)
**Chain:** Confrontation (perceptual exposure to excess being) → Thread Sensitivity development → Leap (suspension of layer-2 reflexive self-rendering) → Operation (restorative / manipulative / destructive, differential Coherence cost per type) → knot-profile accumulation on character sheet → bidirectional substrate-events through knots
**Systems:** threadwork (§2.3 Leap, §31 Mending Coherence Asymmetry), character sheet (knot-profile tag), coherence system, MS system (vulnerability triggers from knotted-territory MS drops)
**What it means:** The most mechanically load-bearing philosophical framework in the design. The Church conflates all three layers into a single suspect category; the framework keeps them categorically distinct. Confrontation is safe perception (no substrate cost). The Leap is a suspension mechanism (no inherent cost, just the suspension). Operation type determines substrate cost (restorative zero; manipulative proportional; destructive catastrophic). `canon/02_foundations_amendment_leap_mechanism.md` is canonical; `systems/threadwork/threadwork_v30.md` §2.3 and §31 implement it.
**Implementation status:** Foundations committed 2026-04-20 (canon/02). Knot-profile character sheet mechanic specified in canon/02 Amendment 6; Godot implementation pending.
**Arc register vectors:** Distributed across all practitioner arcs.
**Source:** session_master_2026_04_20.md Part IV TL-5; ED-730.

### T-29: Baralta as Accidental Prophylaxis Cracker (TL-8)
**Chain:** Baralta's direct-communion theology (ED-732) → contingency introduced into otherwise-essentialist cognitive frame (deeds > essence) → weakened Perceptual Prophylaxis in populations under her influence → higher per-capita confrontation retention → slow TS development rate lift in Hafenmark over generations → eventual breach of the Church's prophylactic closure in Hafenmark territories
**Systems:** prophylaxis as territorial/factional variable (pending mechanical capture), conviction_track (Truth frame), faction AI (Hafenmark priority tree), Thread Revelation Curve (MS-independent population-level visibility)
**What it means:** Baralta is closer to metaphysical truth than the Church for the wrong reasons. Her framework is historically progressive despite being a wrong mechanism because it opens the perceptual door the Church closes. Her populations, over generations, produce more TS development than Church orthodox populations — not because she teaches practitioners but because her theology loosens the cognitive foreclosure that prevents confrontation from being held. This is a multi-generational throughline; its full effects land after the game's ~30-year span, but gradient effects are present at game start.
**Implementation status:** Theological profile canonical (NPC §6, ED-732). Prophylaxis-as-variable mechanical capture pending — needs design for territorial prophylaxis rating feeding TS development rates and Seam Text visibility.
**Arc register vectors:** ARC-S01, ARC-S13, Hafenmark arc cluster (registry update pending).
**Source:** session_master_2026_04_20.md Part IV TL-8; ED-732.

### T-30: Information Asymmetry as Core Mechanic (TL-7)
**Chain:** Player POV (full-framework access) → Character POV (framework-blind, perception-bounded) → gap between what the player sees and what the character can know → player decisions inform character choices that the character would not make with character-only information → incompatible faction interpretations compound the gap (triple-interpretation spiral)
**Systems:** investigation_systems (Filter chain gates character knowledge), chronicler system (what's recorded vs what happened), Miracle Investigation aporia, Conviction Scenes, the TS visibility tables, the Truth track
**What it means:** The gap between player and character knowledge IS the gameplay. Church sees miracle; player sees Mending. Baralta reads divine favour; player sees political skill. Witness scripture = rendered shell; player sees excess-of-Real substrate. The triple-interpretation faction conflict is the most elaborate expression: three factions, three framework-incompatible frames, and the player navigating all three without any faction having the framework's view. Structural epistemology derives from Foundations P-03 (rendering is consciousness-performed) and §9 Perceptual Prophylaxis.
**Implementation status:** Fully implemented in investigation_systems Filter chain and TS visibility tables. Chronicler divergence specified in design but not yet in code. Conviction Scene UX needs to preserve asymmetry without leaking player-POV information into character dialogue.
**Arc register vectors:** Distributed across all arcs with factional evidence divergence.
**Source:** session_master_2026_04_20.md Part IV TL-7.

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
| T-04 RS Decay | ARC-P02, S15, S32, S34 | ms_budget, calamity_radiation | Fully implemented |
| T-05 TC Accumulation | ARC-P01 | tc_political_redesign, conviction_track | Fully implemented |
| T-06 IP Accumulation | ARC-P06 | peninsular_strain §3.2 | Implemented; base rate GAP noted |
| T-07 Turmoil | Not covered | peninsular_strain §4 | Fully implemented |
| T-08 Church Rendering | ARC-S03, S06, S08, S09, etc. | npc_behavior (Church tree), conviction_track | Fully implemented |
| T-09 Varfell Progressive | ARC-S01, S13, S27 | victory §6 (WR/WC), faction_politics (Warden ladder) | Fully implemented |
| T-11 Crown Instrumentalist | ARC-S14, S17, S28, S45 | params_board_game (Thread Liaison) | Implemented |
| T-12 Practitioner Arc | ARC-S04, S34 | threadwork §3 (Coherence), npc_behavior §4.3 | Implemented (ED-672, ED-681) |
| T-13 Truth Journey | Implicit in Thread vectors | params_core (Truth Track), character_histories (ED-678) | Fully implemented |
| T-14 Conviction Architecture | All NPC arc profiles | npc_behavior §3, §5 (Scars, Arc Emergence) | Implemented (ED-670) |
| T-15 Player Progression | Not covered (player, not arc) | faction_politics (ladders), settlement_layer §6 | Fully implemented |
| T-16 Knot Propagation | Implicit | npc_behavior §5.0b, threadwork (Knot mechanics) | Implemented |
| T-17 Companion Moral Mirror | Not covered | companion_specification §6.1 (Thread departure) | Implemented (ED-666) |
| T-18 Radiation Gradient | ARC-S15 | calamity_radiation (full matrix) | Fully implemented |
| T-19 Southernmost Hidden Front | ARC-S15, S34 | params_southernmost, wc_survival_spine | Implemented |
| T-20 Two Contests | ARC-S32, S33 | wc_survival_spine (explicit), ms_budget | Implemented (ED-669) |
| T-21 Thread Political Warfare | ARC-S33 | npc_behavior §8 (priority tree amendments) | Implemented (ED-679) |
| T-22 Belief Lattice | ARC-S33 | threadwork §2.5 (Collective Operations) | Implemented |
| T-23 NPC Arc Emergence | All faction vectors | npc_behavior §5, arc_expansion | Fully implemented |
| T-24 Convergence as Crisis | §VI Convergence Markers (7+) | arc_register | Fully specified |
| T-25 Generational Arc | Not covered | settlement_layer §7 (Extended Timeline) | Implemented |
| T-26 Recursion (TL-3) | ARC-S32, S34; Southernmost arcs | Miraculous Event cascade (pending ED-735), Church priority tree (pending) | Design complete; Godot implementation pending |
| T-27 Effects Real Explanation Wrong (TL-4) | Distributed across faction-interpretation arcs | Seam Text TS-gating (threadwork §2.3), Filter chain (investigation) | Design complete; Conviction Scar targeting pending |
| T-28 Confrontation/Leap/Operation (TL-5) | All practitioner arcs | canon/02 Leap Mechanism amendment (foundations); threadwork §2.3, §31 | Foundations canonical; knot-profile character sheet pending Godot |
| T-29 Baralta Prophylaxis Cracker (TL-8) | ARC-S01, S13; Hafenmark cluster | NPC §6 Baralta theology (canonical); prophylaxis-as-variable mechanic pending | Theological profile canonical; mechanical capture pending |
| T-30 Information Asymmetry (TL-7) | Distributed across all factional-divergence arcs | investigation Filter chain, TS visibility tables, chronicler divergence | Filter chain + TS gating implemented; Conviction Scene UX pending |

**Count: 30 throughlines identified (25 original + 5 novel from 2026-04-20 atomization). 30/30 have mechanical specification; pending implementations tracked in Status column.**

---

*Every throughline has at least partial system documentation and mechanical implementation. The game's constitutive chains are structurally complete. What remains is simulation validation (do the chains produce the intended dynamics at the intended rates?) and constitutive framing (do the system documents describe their mechanics in Thread terms?).*


---

## VIII. POST-ATOMIZATION THROUGHLINES (T-31..T-41, FROM S1–S7 RIGOROUS AUDIT SYNTHESIS v3.1)

### T-31: Reflexive Suspension
**Chain:** canon/02 Am 1 → practitioner perceives target configuration at TS-band receptive capacity → entry commit locks operation sequence up to (Focus − 1) with pre-declared exit conditions → Leap Roll resolves → reflexive facing suspends, outward facing persists, layer 1 Ein Sof spooling continues → sequence executes as committed, no mid-contact modification → voluntary exit or Fatigue-threshold involuntary exit triggers Retention Roll → reflexive self-rendering reasserts, knots register at substrate depth below reflexive-access threshold per canon/02 Am 2
**Systems:** threadwork_v30 §2.3; canon/02 Am 1; entry-commit UX; contact-phase execution; retention degree outcomes; knot-profile two-layer UX
**What it means:** Player-facing surface is two decisions (entry commit, exit timing). Contact is resolution, not a decision sequence. Canon/02 Am 1 structural commitment means mid-contact modification is unavailable.
**Implementation status:** Proposed. Wave 1 workplan P1.

### T-32: Sincere Structural Closure
**Chain:** canon §9 → observer confronts excess-being → receptive capacity gates what is received → formation auto-generates motor-plausible explanation → no residual dissonance → propositional argument cannot crack → only confrontational experience under integrative conditions produces cracking
**Systems:** Church NPC dialogue generator; canon §9; faction formation; Baralta partial prophylaxis (T-29)
**What it means:** Church position on threadwork is formation-structural anosognosia. Argument cannot shift at framework level; only confrontation under integrative conditions produces frame-drift.
**Implementation status:** Proposed. Wave 1 workplan P3.

### T-33: TS as Developmental Arc
**Chain:** canon §14 → confrontation held under integration-supportive conditions → cumulative receptive-capacity development → band threshold crossings at TS 30, 50, 70, 90 → practitioner waterline lowers; more of substrate-iceberg receivable per canon/01 Am 3 explicit
**Systems:** TS track; Truth track; band-crossing Event Scenes; dialogue registers keyed to TS band; ambient narrative-self content differentiation
**What it means:** TS is a receptive-capacity axis per canon/01 Am 3. Development comes from confrontation under support; substrate-iceberg is invariant across observers; higher TS receives more of the same given at ordinary perception.
**Implementation status:** Proposed. Wave 1 workplans P2, P9, P10.

### T-34: Distal Interoception through Knot Tethers
**Chain:** Practitioner forms knot via operation → knot persists at substrate depth below reflexive-access threshold → knot remains tethered post-surface → continuous seismographic signal via canon/02 Am 6 intelligence-mechanic (no dice roll; somatic interoceptive) → signal reports MS state, vulnerability trigger, affective valence of knotted territories
**Systems:** Knot-profile diagnostic panel; ambient somatic layer; vulnerability-trigger pre-cognitive cues; signal clarity as trait/training variable
**What it means:** Practitioner's somatic awareness of knotted-territory states is framework-original distal sense. Within-character channel for what canon/02 Am 2 says reflexive self-rendering cannot access.
**Implementation status:** Proposed. Wave 2 workplan P15 Layer 2.

### T-35: Unified Uncanny Capacity Synthesis
**Chain:** Observer encounters category-resistant entity or Fragmented-band practitioner → receptive capacity (observer TS band) gates received content → observer formation + interpretive frame processes received content → frame-consistent uncanny register emerges per observer-TS
**Systems:** Dialogue generator observer-TS branching; threadcut rendering (threadwork §6.2); Fragmented-band practitioner outward facing; Providence-being temporal rendering
**What it means:** Framework accommodates Jentsch/Mori/Freud/Heidegger uncanny traditions at specific loci within a single structural account. Same entity, different receptive capacities, different frame-consistent registers.
**Implementation status:** Proposed. Wave 4 workplan P17.

### T-36: Relational Ontological Identity (TS 50–69 Coherence 0)
**Chain:** Career operations → cumulative Coherence depletion → Coherence 0 at TS 50–69 → layer 2 self-rendering ceases → canon/01 Am 4 TS-gated outcome: companion knots become load-bearing → identity sustained through named bonds → knot severance produces structural disassembly → isolation is categorically lethal
**Systems:** canon/01 Am 4; companion system (structurally consequential at this trajectory); knot-profile load-bearing state flag; dialogue generator companion-indexed registers
**What it means:** At this ending-trajectory, practitioner exists through relational bonds rather than autonomous self-coherence. Knot severance is structural disassembly, not grief event. Trajectory-conditional.
**Implementation status:** Proposed. Wave 3 workplan P22.

### T-37: Stimulus Resistance Triplet
**Chain:** Substrate-adjacent stimulus in perception → resistance mode triggers by integration-failure mode → predication resistance (naming fails); grammaticalisation resistance (relational grammatical integration fails); categorisation resistance (taxonomic placement fails)
**Systems:** NPC dialogue three-register templates; environmental substrate-excess amplitude; Seam Text vs Church doctrinal text-generator; unified category-resistance dialogue register
**What it means:** Framework distinguishes three modes of integration-failure with stimuli ordinary perception cannot fully process. All within the renderable; Ein Sof is structural terminus beyond resistance.
**Implementation status:** Proposed. Waves 2+4 workplans P7/P12/P17.

### T-38: Real as Continuous Amplitude (Within the Renderable)
**Chain:** Substrate is excess at all times → every location has substrate-excess amplitude (ordinary/moderate/mid-high/high/extreme) → TS development expands predicate set; extreme amplitude remains beyond highest TS predicate sets
**Systems:** Environmental design amplitude per region; shader/audio register amplitude-scaled; NPC dialogue amplitude-keyed; monstrosity UX as scaled extreme; Gap-proximity gradient
**What it means:** Framework-world has continuously-present substrate excess. No substrate-quiet location. Monstrosity is extreme amplitude of the same spectrum, not separate category.
**Implementation status:** Proposed. Environmental-quality three-composite consolidation + P13 + P21 surface amplitude at UI.

### T-39: Textual Mode Typology
**Chain:** In-world expressive output from practitioner or faction → four distinct production modes: below-waterline cartographic (inner-tradition); Church doctrinal; Coherence-degraded; other-faction doctrinal (Varfell/Baralta/RM) → observer receptive capacity (TS + formation) determines legibility
**Systems:** Text generator four-mode templates; dialogue faction-AI variants per T-27; historical corpus as environmental-storytelling; Church chronicler/Varfell report/Baralta homily/RM lineage-text distinctive generators; TS-correlated text rendering
**What it means:** Framework commits to four distinct in-world textual modes. Each has own grammatical structure; cross-mode reading requires different receptive capacities.
**Implementation status:** Proposed. Wave 2 workplan P12 core.

### T-40: TS as Taxonomic Expansion
**Chain:** Confrontation retention → TS band threshold crossings → new framework-taxonomic categories admitted into receptive capacity. TS 30+ substrate-effect. TS 50+ relational thread-structure, threadcut mode. TS 70+ structural reality, Accord as institution. TS 90+ full substrate topology, environmental-strain awareness
**Systems:** Band-threshold Event Scenes unlock category availability; map UI TS-keyed overlay layers; dialogue generator high-TS taxonomy access; text rendering shift
**What it means:** Higher TS admits more categories into receptive capacity for placing received content. Categories are substrate-supported invariantly; TS expansion admits them.
**Implementation status:** Proposed. Wave 1 workplan P21 + Wave 2 workplan P2.

### T-41: Damaged Substrate Is Non-Agential
**Chain:** Substrate damage (Gap, dissolution residue, Calamity residue, wounded territory, threadcut de-actualisation) → rendering effects (environmental distortion, Coherence pressure, solastalgia) → without moral agency, corruption, demonism, malice, qelippot analog → art direction: desaturation, coldness, absence, wrongness → NPC response: non-moralising recognition or T-27 interpreter output → player response: contain, flee, survive; never defeat via damage
**Systems:** Monstrosity art direction; damaged-substrate zones environmental design; Gap manifestation UX; solastalgia vulnerability triggers; Church demonic framing as interpreter output per T-27
**What it means:** Damaged substrate has no moral agent. Framework refuses demonology-pathway Church doctrine imposes on substrate damage. Ethics flow from substrate-ontology, not moral-adversary framing.
**Implementation status:** Proposed. Multi-proposal: Wave 1 P7 + Wave 2 P5 + Wave 3 P14 solastalgia + art direction design guidance.

**Count: 41 throughlines (30 pre-atomization + 11 novel from S1–S7 rigorous audit synthesis v3.1, post-ED-738). All 11 novel entries have Wave 1–4 workplan mappings.**

*[EDITORIAL: T-31..T-41 derived from audit/lane-a/rigorous_audit_synthesis_s1_s7_v3_1.md per ED-738 pivot. М-7..М-11 meta-throughline additions propagated separately.]*
