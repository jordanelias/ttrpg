# VALORIA PROJECT AUDIT — 2026-04-10 through 2026-04-13

## Scope

Exhaustive audit of all committed work and conversations across ~215 commits, ~25 sessions, covering: cognitive load assessment, crunch cascade analysis, coherency, cogency, mechanical consistency, precedent, contribution quality, errors, and cross-system transitions (TTRPG ↔ Hybrid ↔ Board Game). All game modes and all game systems evaluated with attention to transitions, zooming, interdependencies, emergent arc vectors, and mechanical branching causation chains.

---

## I. VOLUME AND VELOCITY ASSESSMENT

### Raw Numbers (April 10–13)

| Metric | Count |
|--------|-------|
| Commits | ~215 |
| Sessions | ~25 |
| Patches applied | PP-493 through PP-644 + PP-NPC-01 through PP-NPC-04 (~155 patches) |
| Editorial items raised | ~ED-351 through ED-534 (~183 items) |
| Editorial items resolved | ~170+ |
| Simulations run | ~20+ distinct stress tests |
| Design docs created/modified | 25+ canonical v30 docs |
| Infrastructure commits | ~50 |
| Deprecated files | 46+ |
| New systems designed | NPC Behavior, Fieldwork, Scale Transitions, Character Histories |

### Velocity Critique

**Finding: Unsustainable pace with compounding risk.**

The three-day sprint averaged ~70 commits/day. This is extraordinarily high for a mechanically interdependent system of this complexity. While individual commits show correct protocol adherence (atomic commits, checker runs, editorial ledger updates), the aggregate effect is a project state that has transformed so rapidly that no single session has full context of what other sessions changed.

**Evidence of velocity-induced errors:**

1. **Session log overwrite (commit 874826e):** A consolidation session physically overwrote entries from a parallel session generating arcs 41–45. The fix was committed, but the error occurred because two sessions were committing to the same file within hours.

2. **PP numbering collision (PP-506–511 vs PP-512–524):** The diplomacy stress test used PP numbers that collided with Graduated Seizure patches committed in a parallel session. Required a full renumbering pass.

3. **Empty file commit (c3d6b43):** Arcs 51–55 batch 08 initially committed as an empty file, requiring a re-commit.

4. **Stale local state across sessions:** Multiple sessions show evidence of operating on pre-session state that didn't include changes from concurrent work. The bootstrap protocol catches this at session start, but mid-session, context can drift when another session commits between fetches.

**Assessment:** The velocity itself is a structural risk. The project infrastructure (atomic commits, checkers, canonical_sources.yaml) successfully prevents most cascading damage, but the three errors above all trace to parallelism — multiple sessions operating on the same project simultaneously. Recommendation: serialise sessions. One session commits and closes before the next begins.

---

## II. COGNITIVE LOAD AND CRUNCH CASCADE ANALYSIS

### Crunch Inventory

The project now contains the following resolution layers that a player/GM must track:

**TTRPG Mode:**

1. Dice: d10 pool, TN 7, 1s subtract, 10s double — 4 rules per roll
2. Ob system: varies by subsystem — Fibonacci for Thread Depth, floor(Mandate/2)+1 for faction, direct for combat — 3+ distinct Ob derivation formulas
3. Pool construction: differs per subsystem (Spirit×2+History+TPS for Thread; Agi×2+History+3 for Combat; Att+2 for Disposition; Power at TN6 for Volley) — 6+ distinct pool formulas
4. Momentum: 3-threshold system with carry rules
5. Thread contact: TS gating, Coherence tracking, Intelligibility, Dissonance risk, Gap scale model
6. Social: Disposition (−4 to floor(Bonds/2)+1), Knots (pool=Bonds×2+3, tiers), Debate (Conviction Track, Doubt Markers, Concentration, Appraise/Argue/Reinforce)
7. Investigation: Evidence Track, Survey Ob, Cover, Cold Trail → Desperate Trail
8. Combat: Versus resolution with pool-split, 4 categories (Ranged/Melee/Magic/Social), Yield/Disengage mechanics
9. Mass combat: Sub-unit composition, Discipline, Command, Volley, Shield Wall, simultaneous damage, Thread coherence 7-turn window
10. Faction play: Mandate, Stability, Influence, Intel, Loyalty, TC, RS, PI, Coup Counter, Guild Favour — 10+ trackers

**Board Game Mode:**

1. Domain Actions: per-faction priority trees, NPC AI decision logic
2. Territory control: TCV, Fort Level, Occupation, Seizure, Contention Markers, Casus Belli
3. Diplomacy: Open Pledge, Crown Treaty, Coalition Pairs, Diplomatic Tokens, Resentment
4. Victory: 6+ distinct victory paths with per-faction requirements spanning 12–16 seasons
5. Accounting Phase: all clocks advance, RS/TC/IP/PI interact
6. NPC Behavior: Stance Triangles, Priority Trees, Framework Drift conditions

**Hybrid Mode:**

1. All BG mechanics plus Zoom In/Zoom Out transitions
2. Scene Opportunity system with Ob modifiers from board degree
3. Scale transition rules: Personal → Domain → Mass
4. Thread state persistence across mode transitions

### Crunch Cascade Assessment

**Finding: CRITICAL — The crunch cascade is real and largely unmitigated.**

A "crunch cascade" occurs when resolving one mechanic requires tracking outputs from multiple other mechanics simultaneously. The Valoria system has several identified cascades:

**Cascade 1 — Thread Operations During Faction Play:**
Thread operations require Spirit×2+History+TPS pool → roll vs Fibonacci Depth + Breadth + Distance Ob → resolve with TN 7/8/9 depending on operation type → apply Coherence cost → check for Gap generation → Gap feeds back into RS calculations → RS affects faction Mandate → Mandate affects faction Ob → faction Ob affects NPC actions → NPC actions may trigger more Thread operations. Six interconnected subsystems in one resolution chain.

**Cascade 2 — Mass Battle With Thread Elements:**
Mass battle sub-units have Discipline and Command. Thread-capable units can perform thread operations during battle. Coherence degrades on a 7-turn clock. A Thread-destroyed unit fights in Phase 5 under simultaneous-damage rules. Shield Wall modifies defence pools. All of this resolves within the mass battle framework which itself sits inside the BG faction phase. Four nested resolution layers.

**Cascade 3 — Disposition/Knot/Debate Triangle:**
Socializing uses Disposition (now −4 to variable cap), which feeds into Knot formation (which requires its own Connect roll at Ob = tier minus Disposition), and Knots affect Debate (through Resonant Style sources), and Debate outcomes affect NPC Disposition. The PP-632 redesign made Disposition more elegant (one formula replaces a lookup table) but the three-way cycle remains.

**Cascade 4 — Board Game Accounting Phase:**
At Accounting, all of the following interact: TC advances, RS adjusts, IP ticks, PI increments, Coup Counter evaluates, each NPC evaluates their Priority Tree, each faction evaluates victory conditions, Graduated Seizure checks, Guild Favour checks. The NPC Behavior system (PP-NPC-01 through PP-NPC-04) added four new conditional checks to this phase.

**Mitigation assessment:**

The project has several mitigation strategies in place: the three-layer arc tracking (Structural / Accumulation / Foreground with max 3 foreground cap), the Accounting Phase consolidation, and the principle that Board Game abstracts what TTRPG resolves in detail. However, the PP-632 Disposition redesign, while mathematically cleaner (one formula vs table), still requires tracking Bonds values for both Disposition cap and Knot count cap simultaneously — a player must know Bonds to know what Disposition ceiling is achievable and how many Knots can form. This is a hidden coupling that doesn't appear in any single design doc.

**Recommendation:** A cognitive load pass should be a dedicated session. The current design docs describe each system in isolation. No document maps the full resolution chain a player actually traverses when, for example, a TTRPG session includes a social encounter that escalates to a debate that references Thread operations. A "resolution chain map" document — showing which systems feed which, with pool formulas and Ob derivations side by side — would expose cascades that are invisible when reading individual design docs.

---

## III. COHERENCY AND COGENCY

### Cross-System Pool Formula Coherency

The stat audit session (PP-611–614) and the comparative audit (PP-630–634) both explicitly addressed statistical consistency. Current state:

| System | Primary Pool | TN | Ob Source |
|--------|-------------|-----|-----------|
| Combat (Melee/Ranged) | (Agi×2)+History+3 | 7 | Opponent's pool (Versus) |
| Thread Operations | (Spirit×2)+History+TPS | 7/8/9 | Fibonacci Depth + Breadth + Distance |
| Debate (Argue) | Pool varies by style | 7 | Resistance (audience Stability avg) |
| Investigation (Survey) | Perception+relevant skill | 7 | Territory/Cover/Complexity |
| Disposition (Connect) | Att+2 | 7 | max(1, base Ob − Disposition) |
| Mass Battle (Command) | Cmd stat | 7 | Varied |
| Mass Battle (Volley) | Power at TN6 | **6** | - |

**Finding: Volley TN6 is the only TN exception in the entire system.** Everything else resolves at TN7 (standard), TN8 (Binding/POP Thread operations), or TN9 (POP Binding). The Volley exception is documented (PP-503) but represents a design decision that breaks the otherwise universal TN7 baseline. This is mechanically defensible (volley represents mass fire, not individual skill) but creates a teaching burden: "everything is TN7 except one thing."

**Finding: Pool construction is inconsistent across subsystems.** Combat uses Agi×2+History+3. Threadwork uses Spirit×2+History+TPS. Disposition uses Att+2. There is no unifying pool construction principle. Each subsystem derives its pool from different attributes with different multipliers and different additive terms. This is arguably intentional (different activities test different capabilities) but the lack of a shared grammar (e.g., "all pools = Primary×2 + Secondary + Modifier") means players must memorise each system's formula independently.

**Assessment:** The PP-611–614 stat audit caught and corrected several inconsistencies (Stamina formula, Combat Pool, mass battle RS×3 multiplier). The current state is *internally consistent within each system* but *grammatically inconsistent across systems*. Whether this is a problem depends on design philosophy: Burning Wheel (the apparent primary influence) does this same thing. But Burning Wheel has a single pool construction principle (stat + skill). Valoria has at least 5.

### Cross-System Mechanic Naming Coherency

**Finding: Naming inconsistencies remain despite cleanup passes.**

1. "Remembrancer" → "Witness" rename (PP-635–638) was applied across the codebase. Clean.
2. "Certainty" has had multiple definitions across sessions. PP-607 defined it one way, PP-553 redesigned it. The canonical definition is in params_core but the name "Certainty" appears in older arc files with the prior meaning.
3. "Dissolution" vs "Severing" — Thread terminology was standardised in the threadwork redesign, but some arc files still reference the older "Dissolution" terminology when describing Thread failure outcomes that should be "Severing."
4. "Mandate" is used by both Crown and Church factions with different mechanical meanings (Crown Mandate governs legitimacy; Church Mandate governs institutional authority and Ob for TC Suppress). PP-547 standardised the TC Suppress Ob to floor(Mandate/2)+1, which applies to *Church* Mandate — but some arc files reference "Mandate" without specifying whose.

### Mechanical Value Consistency

The params files are the canonical extracted values. Cross-checking reveals:

**Finding: Torben Loyalty starting value was corrected from 7 to 3 (PP-498/PP-599).** This was a significant error — Torben at Loyalty 7 would never defect, removing the entire succession crisis arc. The correction to 3 with a split decay model (active decay below 4, passive above 5) is mechanically sound and narratively essential.

**Finding: Thread Sensitivity values were corrected.** Almud TS 28→0 (ED-364). Almud is a non-sensitive — the original value of 28 was fabricated. This was a consequential error: a TS-28 Almud would be a moderate practitioner, fundamentally changing his characterisation from "pragmatic politician" to "politically active threadworker."

**Finding: Lenneth TS intentionally undefined.** Lenneth's TS is arc-dependent — it should not have a fixed value until her arc resolves. Sessions correctly flagged this as ED-358b (P3, non-blocking) rather than fabricating a number.

---

## IV. TRANSITIONS AND MODE ZOOMING

### TTRPG ↔ Hybrid ↔ Board Game Frame

The scale_transitions_design_v1 (PP-594, now scale_transitions_v30.md) was created during this sprint. It consolidates stage11 + various patches. Key transition mechanics:

**Zoom In (BG → TTRPG/Hybrid):**
- Triggered by SceneOpportunity from DomainActionSystem
- Board degree maps to Ob modifier: FAILURE → +1, SUCCESS → −1, OVERWHELMING → −2
- Player can decline (abstract consequences apply)
- Scene resolves, results feed back to board state via `_apply_scene_result()`

**Zoom Out (TTRPG → BG):**
- Clock-driven: season ends → all personal actions resolve → Accounting Phase
- Thread state persists across transition (Coherence, POP, existing Gaps)
- Active Knots persist, Disposition carries

**Finding: The Zoom In trigger for NPC arcs is the most significant unresolved transition gap.**

The arc system produces 120+ arcs across 8 batches. These arcs have emergence conditions (clock thresholds, NPC track values, faction stat breakpoints). In BG mode, arcs manifest as clock events and mechanical effects. In TTRPG mode, the GM interprets them narratively. In Hybrid mode, the question is: *when does a board-state threshold trigger a Zoom In for an NPC arc moment?*

The NPC Behavior system (PP-NPC-01–04) defines AI priority trees that produce board actions. The arc emergence conditions (from arc_register.md v8) define when arcs "fire." But there is no document mapping which specific arc emergence conditions should produce a Zoom In prompt for the GM in Hybrid mode. The Zoom In reference card (PP-556) added arc-specific triggers for a few arcs (Haelgrund Defection, TC seizure) but this covers perhaps 5 of 120+ arcs.

**Assessment:** This is the single largest structural gap in the mode transition system. Board Game works (arcs are mechanical effects). TTRPG works (GM reads the arc library). Hybrid's "best of both" promise requires the Zoom In triggers for all major arcs to be specified — otherwise the GM doesn't know when to call a personal scene for an NPC arc moment during board play.

### Godot Implementation Alignment

The Godot sessions (valoria-game repo) produced:

1. GameDirector as autoload with season loop
2. BoardContainer with schematic territory map
3. DomainActionSystem split into roll/scene_for/resolve_abstractly
4. SceneOpportunity carrying board degree and ob_modifier
5. TriggerRuleRegistry for arc emergence
6. CombatContainer with Versus resolution
7. check_victory covering all canonical victory conditions
8. Nested zoom (Phase 10.1)

**Finding: The Godot implementation is architecturally sound but has known gaps.**

The audit identified 23 findings across the codebase. All were committed as fixes. The most architecturally significant: CombatContainer's defender_id wiring was broken (B-01), GameDirector was not an autoload despite requiring global state access, and the season loop's `_zoom_into_scene()` lacked proper canvas layer management.

**Finding: The TriggerRuleRegistry is built but empty.** The infrastructure for arc emergence exists in the Godot codebase, but zero TriggerRule .tres files have been seeded. This means the emergence pipeline exists architecturally but cannot fire. The session handoff explicitly lists 10 priority rules that need creation.

**Finding: NPC disposition tracker integration is incomplete.** The NPC Behavior system (ttrpg repo) defines 13 NPCs with faction dispositions. The Godot implementation needs `npc:{id}:disp_{faction}` trackers registered in Meta._load_npc_data(). This wiring is planned but not committed.

---

## V. INTERDEPENDENCIES AND EMERGENT ARC VECTORS

### Arc System State

The arc system grew from ~35 arcs to 120+ arcs during this sprint:

| Batch | Arcs | Focus |
|-------|------|-------|
| 01 (nongreedy) | 1–4 | System emergence, irrational player behavior |
| 02 | 5–9 | Thread/faction intersection |
| 03 (historical) | 10–18 | Historical parallel arcs |
| 04 | 19–35 | Branching decision points |
| 05 | 36–40 | Interdependent intersecting arcs |
| 06 | 41–45 | Deep mechanical coupling |
| 07 | 46–50 | TC/VTM/Loyalty/RS interdependencies |
| 08 | 51–55 | Contact duration, PI cascade, wound economy |

### Arc Quality Audit

**Finding: Batches 07–08 had the highest fabrication rate.**

The critique session identified and corrected:

- Arc 47: fabricated "PI roll vs Ob 3" — PI is a track, not a pool. Entire arc rebuilt.
- Arc 50: Suppress Ob at Church Mandate 6 corrected from 4 to 2 (formula misapplied).
- Arc 50: Assert triple-stack decomposition was additive, not replacement. Corrected.
- Arc 51: P-15 violation — Coherence 0 modelled as flat NPC conversion, should be TS-gated branching.
- Arc 52: fabricated "Influence −1 from inactivity" — no such mechanic exists.
- Arc 55: same fabricated inactivity decay.

**Pattern:** The fabrication errors cluster around faction mechanics (PI, Influence, Guild Favour) where the design docs are most distributed across multiple files. When the generator operates with incomplete context about which faction mechanics exist vs which are proposed, it fills gaps with plausible-sounding rules.

**Finding: De-escalation arcs are absent.** This was flagged in the narrative analysis session. Every arc ends in victory, defeat, or crisis. No arc traces genuine compromise. The system models factional competition extremely well but has no mechanical pathway for détente. This matters for Hybrid mode: if the BG state produces a diplomatic equilibrium, there is no arc to describe what that equilibrium looks like narratively.

**Finding: Edeyja has zero arcs.** The moral anchor of the setting, the highest-TS character, the Warden-Chief — invisible in the arc portfolio. This was flagged and remains unaddressed. Given Edeyja's role as the character most connected to the Southernmost and Thread cosmology, this gap means the game's central metaphysical question (what happened at the Calamity) has no arc infrastructure to explore.

### Mechanical Branching Causation Chains

The arc register v8 documents the following principal causation chains:

**Chain A — Thread Counter (TC) → Everything:**
TC is the master clock. TC advancing triggers: Church Assert/Suppress evaluation → Mandate changes → Ob changes for all faction actions → NPC priority tree re-evaluation → domain action selection → territory control changes → victory condition evaluation. Every faction's victory path either requires TC management or is affected by it. TC is the single most consequential variable in the system.

**Chain B — Coup Counter → Crown Stability:**
Three independent triggers (TC ≥ 40 unopposed, Torben Loyalty ≤ 2–3, Crown loses 2+ territories without military response) feed a counter ceiling-3. The PP-NPC-02 fix (Coup Counter requires active Church Assert, not passive TC) was critical — without it, the coup was deterministic in 5/5 simulation runs.

**Chain C — RS → Calamity Radiation → Thread Operations:**
Reality Strength decline affects calamity radiation geography → affects Thread operation difficulty at affected locations → affects practitioner Coherence → affects RS feedback. This is a self-reinforcing loop with no equilibrium point unless players actively intervene. The Gap scale model (PP-602–606) provides the self-healing mechanism (Gaps close naturally at their scale), but the radiation geography gradient means this loop is faster in the south than the north.

**Chain D — Disposition → Knot → Debate → NPC Arc:**
PP-632 redesigned Disposition as a derivative of Bonds. Bonds also determines Knot capacity and Disposition ceiling. This means a character's social investment (Bonds score) simultaneously determines how much they can like someone (Disposition cap), how deeply they can connect (Knot count), and how those connections affect their rhetorical capacity (Resonant Style sources). The chain runs: invest in Bonds → higher Disposition ceiling → easier Knot formation → more RS sources → stronger Debate pools → better NPC outcomes → NPC arc advancement.

**Finding: Chain D is elegant but has a first-mover advantage.** A character who invests in Bonds early gets compounding returns through all four links. A character who invests late may find NPC Dispositions already hardened. The Disposition decay threshold (+2) means high Dispositions degrade without maintenance, but the Knot system preserves deep connections against this decay (Rupture requires specific trigger, not passive decay). A player who forms a Strong Knot early locks in a relationship that resists the natural entropy of the Disposition system.

---

## VI. SPECIFIC SYSTEM CRITIQUES

### A. Threadwork (threadwork_v30.md)

**Strengths:**
- Single pool (Spirit×2+History+TPS) unifies all operations. Clean.
- Three-axis Ob (Depth Fibonacci + Breadth + Distance) is mathematically elegant and narratively meaningful.
- TN encoding (7/8/9) maps operation type to difficulty without additional tables.
- Gap scale model provides self-healing for reality damage.
- Opposing Operations (PP-632 §2.6) derived from metaphysics, not grafted on.

**Weaknesses:**
- Mending immunity to opposition (categorically different target — substrate absence vs thread presence) is philosophically necessary but creates an asymmetry: every other Thread operation can be opposed, Mending cannot. A Mender is mechanically invulnerable to direct interference. Whether this is desirable depends on desired play patterns.
- The co-movement rules (serialised Coherence, one epistemic+actual per compound event) are correct but add resolution steps to every multi-practitioner Thread scene.
- POP state tracking across mode transitions is specified but complex: POP persists, Coherence cost applies at transition, existing Gaps in POP state continue to grow.

### B. Combat (combat_v30.md)

**Strengths:**
- Versus resolution with pool-split is clean: one roll resolves attack and defence simultaneously.
- Yield/Disengage mechanics (PP-635–638 ED-512) provide non-lethal exits.
- Wound system integrates with Thread operations (wounded practitioners take Spirit checks to maintain contact).

**Weaknesses:**
- The combat system is the least-changed system in the sprint. Only PP-611–614 (stat audit corrections) and PP-635–638 (Yield/Disengage, Remembrancer→Witness rename) touched it. This is appropriate — stable systems don't need churn — but means combat has not received the same depth of stress testing as faction play, threadwork, or the arc system.
- Mass battle integration is mechanically specified but the cognitive load of running a mass battle (sub-unit Discipline tracking, Command recovery, simultaneous damage, Thread coherence timer) within a session that also includes personal combat and faction actions is extreme.

### C. Board Game (board_game_v30.md)

**Strengths:**
- PP-644 integrated all 17 hybrid gaps into Part Nine, making the board game document self-contained for its mode.
- Victory path balance (PP-540–546) normalised to solo 12–16 seasons, co-victory 10–14 seasons. All four factions within this band.
- NPC Behavior system provides AI decision logic for GM-less play.
- Casus Belli, Treaty, Coalition, Pledge systems provide diplomatic depth.

**Weaknesses:**
- The board game is the most complex subsystem in the project. board_game_v30.md is 795 lines post-PP-644. It encompasses: territory control, faction actions, NPC AI, diplomacy, military operations, economic operations, Graduated Seizure, victory conditions, and hybrid transition rules.
- The NPC AI priority trees (PP-NPC-01–04) add conditional logic that must be evaluated every season for every NPC faction. For a physical board game, this means a decision tree that a human player must traverse for each non-player faction — potentially 3 factions × a multi-branch priority tree each. This is CK3-level AI complexity, which works in a video game but may overwhelm a tabletop format.
- **The Restoration Movement (RM) is correctly modelled as not a board game faction.** It emerges mid-game as a player/NPC-led movement. However, the victory architecture assigns RM a victory path (Cultural Revolution) that requires board-game-mechanical territory control. The question is: who executes the RM's Domain Actions? If the RM is NPC-led in BG, it needs a Priority Tree. If player-led, it needs a faction card. Currently, it has neither — it exists as a victory condition but not as a mechanical actor.

### D. Social Systems (fieldwork_v30.md, social_contest_v30.md)

**Strengths:**
- PP-632 Disposition redesign is the best single patch in the sprint. One formula (max(1, base Ob − Disposition)) replaces a lookup table. Bonds governs both ceiling and Knot capacity. Mathematically cleaner and narratively richer.
- Cold Trail → Desperate Trail (PP-575) implements fail-forward for investigation. Failures escalate danger, never halt progress. Correct.
- Evidence Track provides investigation with a clear win condition analogous to victory conditions in faction play.

**Weaknesses:**
- The Debate system (social_contest_v30.md) has the highest audience cognitive load of any subsystem. An audience of 6 NPCs means tracking 6 Stability values averaged to determine resistance. The simulation flagged this (J-01) and the response was to scope it to an existing editorial (ED-055) — effectively deferring the problem.
- Appraise-to-Argue pool ratio of 4:1 (ED-380) means information-gathering is dramatically easier than actual persuasion. This is potentially intentional (knowing is easy, changing minds is hard) but mechanically produces a pattern where Appraise is always worth doing and Argue is always a risk.

### E. NPC Behavior System (npc_behavior_v30.md)

**Strengths:**
- Designed, audited (15 findings), simulated (7 findings, 4 patches), and propagated in a single session. Full lifecycle.
- Stance Triangles and Priority Trees provide deterministic NPC decision logic.
- Framework Drift conditions (PP-NPC-03: Church drift requires Stability ≥ 4 + TC advance + per year) prevent runaway NPC behavior.

**Weaknesses:**
- The system was designed and tested within a single session (~826 lines of design doc). The simulation (SIM-NPC-01) found 4 critical issues in 5 seeds × 12 seasons. All were patched — but finding 4 criticals in the first simulation run suggests the initial design had significant calibration gaps.
- SIM-NPC-02 through SIM-NPC-05 remain registered but unrun. The system has been validated once; the fix-then-revalidate cycle has not been completed.
- The system's interaction with the arc system is undefined. NPC Priority Trees produce Domain Actions. Arc emergence conditions trigger on NPC track values. But the NPC Behavior system does not reference the arc register, and the arc register does not reference NPC Priority Trees. These are two parallel systems that should be interleaved.

### F. Character Histories (character_histories_lifepath.md)

**Strengths:**
- 8 Origins, 7 Formations, 36 Vocations, 7 Catalysts. Comprehensive.
- Thread-adjacent spark additions for non-practitioner Vocations ensure all character types can interact with the Thread system.
- Recall gating system provides a mechanism for unlocking background knowledge during play.

**Weaknesses:**
- 15 open editorial items within the document. This is a high count for a single design doc.
- The Vocation list (36 entries) is large for character creation. At the table, a new player facing 36 choices (after already choosing Origin, Formation, and Catalyst) may experience decision paralysis. The document groups Vocations by faction, which helps, but the list itself is long.
- Starting skill distribution (Origin 1 + Formation 1 + Vocation 2 + Catalyst 1 = 5) was committed to the Godot repo (valoria-game Constants.gd). This is a mechanical value that should live in params_core.md with a cross-reference — currently, it lives only in the Godot codebase and the session log, not in any params file.

---

## VII. ERROR PATTERN ANALYSIS

### Error Categories Across the Sprint

| Category | Count | Examples |
|----------|-------|---------|
| Fabricated mechanics | 6+ | PI roll vs Ob 3 (Arc 47), Influence −1 from inactivity (Arcs 52, 55), RS battle ×3 multiplier |
| Formula misapplication | 4+ | Suppress Ob at M6 = 4 not 2, Assert triple-stack additive not replacement, TCV values wrong |
| Cross-session collision | 3 | Session log overwrite, PP numbering collision, stale local state |
| Naming inconsistency | 3+ | Remembrancer/Witness, Dissolution/Severing, ambiguous "Mandate" |
| Missing propagation | 5+ | PP-643 required multiple follow-up commits, params headers repeatedly rebuilt |
| Empty/broken commits | 2 | Arcs 51–55 empty file, victory_architecture_v1.md returned empty |

### Root Cause Analysis

**Fabricated mechanics** trace to context limitations. When generating arc content, the model fills mechanical gaps with plausible inventions rather than flagging "[GAP: mechanic undefined]." The correction sessions (arc critique, canon guard) reliably catch these, but the generate→critique pipeline means fabrications get committed before being caught. Recommendation: arc generation sessions should include a mandatory "flag all unverified mechanics" pass before commit.

**Formula misapplication** traces to the distributed nature of mechanical values. The Suppress Ob formula (floor(Mandate/2)+1) is defined in one location and applied in 5+ locations across design docs, params files, and arc files. A session working from an arc file might not fetch the canonical formula first. Recommendation: all formula applications should include a cross-reference comment to the canonical source (e.g., "See params_factions.md §Suppress Ob").

**Cross-session collisions** trace to parallelism. This is a workflow issue, not a technical one. The infrastructure correctly prevents data loss (atomic commits, checkers) but cannot prevent semantic collisions (two sessions both deciding to renumber editorial items). Recommendation: strict session serialisation, or at minimum, a "session lock" file in the repo.

---

## VIII. CONTRIBUTION ASSESSMENT

### What the Sprint Actually Delivered

**Tier 1 — High-value, stable contributions:**

1. **PP-632 Disposition/Knot redesign.** The single most impactful mechanical change. Replaces a lookup table with one formula, ties Disposition to Bonds (creating a natural social investment → social capability pathway), and properly distinguishes Knot rupture from loss. This is design work that survives.

2. **NPC Behavior System.** A complete subsystem from blank page to simulation-validated in one session. The four simulation-derived patches (Crown Mandate gate, TC awareness for coup, Church drift conditioning, Varfell collection cooldown) are all mechanically necessary corrections.

3. **Threadwork three-axis Ob system (PP-622).** Depth (Fibonacci) + Breadth + Distance. Mathematically elegant, narratively grounded ("how primordial, how much, how far"), and replaces a flat Ob table.

4. **Scale Transitions design doc (PP-594).** First formal specification of Zoom In/Out mechanics. Consolidates scattered rules into one document.

5. **Cold Trail → Desperate Trail (PP-575).** Fail-forward investigation. Small patch, significant play-pattern impact.

**Tier 2 — Valuable but requiring follow-up:**

1. **120+ arcs.** The volume is impressive and the mechanical grounding is strong post-critique. But 5+ fabricated mechanics were found and corrected across the library, and the de-escalation gap remains.

2. **v30 rename and atomization sprint.** 25 docs renamed, 28+ atomized into skeleton/infill, 40 deprecated files moved. Essential infrastructure, but the atomization is structural — no mechanical values changed.

3. **Godot implementation (4 commits to valoria-game).** Architecturally sound. All 8 Phase-tagged TODOs resolved. But the emergence pipeline is empty (zero TriggerRule .tres files), and NPC disposition wiring is incomplete.

4. **Victory path balance (PP-540–546).** Normalises solo 12–16 seasons. Good — but provisional values remain (ED-389 Varfell reveals, ED-392 Varfell+RM territory requirement) awaiting Jordan's decisions.

**Tier 3 — Incremental but necessary:**

1. **Params header rebuilds.** Occurred at least 4 times during the sprint (6584e3e, 0cbc995, 7729f51, f9a6ba2, 8a64a2a). Each rebuild was necessary (new patches required header updates) but the repeated rebuilds suggest the header format is fragile.

2. **Editorial ledger cleanup.** ED dedup passes, renumbering, striking false debts. Necessary hygiene but consumed significant context window.

3. **Propagation map maintenance.** Stale entries resolved, v30 paths updated. Critical for system integrity but not mechanically productive.

---

## IX. PRECEDENT

### Design Influences Visible in the Work

1. **Burning Wheel:** Pool construction (stat-based), Beliefs/Instincts system, Let It Ride principle, Knot terminology (borrowing "Bonds" concept). The Valoria dice system (d10, TN7, 1s subtract, 10s double) is structurally similar to BW's (d6, TN-based) but with more variance.

2. **Crusader Kings:** NPC behavior system Priority Trees, faction AI decision logic, Mandate/Stability/Influence as faction health metrics. The Godot implementation directly acknowledged CK as a reference for "CK3-level AI complexity."

3. **Diplomacy (board game):** Casus Belli, Treaty, Coalition Pairs, Open Pledge mechanics in the BG mode.

4. **COIN Series (GMT):** The asymmetric faction victory conditions, territory control with CV values, and the three-mode structure (TTRPG/Hybrid/BG) echo COIN's multi-faction asymmetric design.

5. **Blades in the Dark:** Clock system as unified progress tracker, fail-forward investigation mechanics (Cold Trail → Desperate Trail).

### Where Valoria Exceeds Precedent

- **Three-mode integration** is genuinely novel. No published game attempts TTRPG ↔ Board Game ↔ Hybrid with shared mechanical state.
- **Thread system cosmology** — the metaphysics-first design (derive mechanics from philosophical foundations, not the reverse) produces a thread system that is narratively coherent in ways that D&D magic or BW's sorcery are not.
- **Arc emergence from mechanical state** — the 120+ arcs emerging from system interactions (clocks, tracks, faction stats) rather than pre-written scenario triggers is structurally more ambitious than any published game's arc system.

### Where Valoria May Be Exceeding Playability

- **The Board Game mode asks humans to execute CK3-level AI.** CK3 runs thousands of AI evaluations per tick. A physical board game requires a human to traverse each NPC's Priority Tree manually. This is the most significant playability concern.
- **The three-mode promise may be unkept if Hybrid Zoom In triggers are not specified for all major arcs.** Currently, Hybrid mode works for combat and debate (SceneOpportunity from DomainActionSystem) but not for narrative arc moments.
- **The TTRPG mode's crunch level (6+ distinct pool construction formulas, 10+ faction trackers, Thread contact with 5+ derived metrics) is above Burning Wheel's already-high bar.** Burning Wheel players regularly report that the full system takes 10+ sessions to learn. Valoria may require more.

---

## X. RECOMMENDATIONS

### Critical (Should block new feature work)

1. **Complete SIM-NPC-02 through SIM-NPC-05.** The NPC Behavior system was validated once. The patches need re-validation.
2. **Create resolution chain map.** One document showing every cross-system interaction chain a player traverses during play. This will expose hidden cascades.
3. **Define RM mechanical actor status.** RM has a victory condition but no faction card and no Priority Tree. Who executes RM Domain Actions?
4. **Specify Hybrid Zoom In triggers for all principal arcs.** Currently 5/120+.

### Important (Should precede compilation)

5. **Cognitive load reduction pass.** The three-mode design inherently multiplies complexity. A dedicated session should identify which mechanics are mode-specific and can be elided when not in that mode.
6. **Starting skill count to params_core.md.** Currently only in Godot Constants.gd.
7. **Pool formula unification assessment.** Evaluate whether 5+ pool construction formulas can share a common grammar without sacrificing system-specific expressiveness.
8. **Seed TriggerRule .tres files in Godot.** The emergence pipeline is built but empty.

### Low Priority (Quality-of-life)

9. **De-escalation arcs.** The system models conflict well but cooperation poorly.
10. **Edeyja arc coverage.** The most important NPC has zero arcs.
11. **Params header format revision.** The repeated rebuilds suggest the format is fragile.
12. **Session serialisation protocol.** Prevent future cross-session collisions.

---

## XI. SUMMARY VERDICT

The three-day sprint transformed the project from a collection of design documents into a mechanically integrated system with formal simulation validation. The infrastructure (canonical sources, atomic commits, dependency checkers, editorial ledger) performed correctly under extreme load — no data loss despite 215 commits and parallel sessions. The quality of the best work (PP-632, three-axis Ob, NPC Behavior, fail-forward investigation) is high.

The principal risks are: cognitive load for players (particularly in TTRPG mode), the Hybrid mode's incomplete Zoom In trigger coverage, the Board Game mode's demand that humans execute CK3-level NPC AI, and the velocity-induced error rate in arc generation (6+ fabricated mechanics corrected post-commit). The system is mechanically ambitious beyond any published precedent in its three-mode integration, which is both its greatest strength and its greatest design risk.

**Project is at a natural pause point.** The design surface area has expanded faster than simulation coverage can validate it. The next productive phase is validation (re-run NPC sims, stress test mode transitions, specify Zoom In triggers) rather than feature expansion.
