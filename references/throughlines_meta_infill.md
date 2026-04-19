<!-- INFILL — rationale, examples, derivation -->
<!-- Companion to: references/throughlines_meta.md (SKELETON) -->
<!-- Do not use for vetting reference; use skeleton only -->
<!-- [EDITORIAL: PP-672 — throughlines hierarchical framework infill, 2026-04-19] -->

# Throughlines Framework — Infill

## §1 Ω — Rationale per clause

**Why these four clauses.**

The project instructions define Intent of Game as "a positive feedback loop between player decisions and mechanics/system/designs that produces an engaging game world with emergent narratives." This is necessary but not sufficient to anchor vetting — it applies to any well-designed emergent strategy game. The four-clause Ω specializes it to Valoria.

- **(a) Cross-scale consequence** isolates Valoria's specific gameplay: a local decision matters at other scales, not just at its native scale. This distinguishes Valoria from games where strategic and personal play are mechanically isolated (Pillars of Eternity's stronghold vs party-level play; Mount & Blade's faction politics vs character combat). Valoria's cross-scale coupling is the texture the player feels — the reason decisions matter.

- **(b) Personal transformation** commits Valoria to A11 (Epistemic Seduction) and C3 (Confrontation Development). The player ends the game changed — this is the canonical commitment that makes the character-layer meaningful. A game without this is a strategy game with a character sheet; Valoria requires the character to actually transform through engagement.

- **(c) Autonomous world** rules out games-as-puzzles. If everything waits for the player, the world is not a world — it is a problem set. The autonomy clause ensures the game continues producing events when the player is deliberating, traveling, or absent.

- **(d) Non-dominance** is the anti-optimization commitment. Valoria cannot be "solved" — not because it is arbitrary but because its tensions are irreducible (T-20 Two Contests, T-22 Belief Lattice). A mechanic that produces a dominant strategy breaks this.

**What Ω excludes that earlier drafts included.**

The first Ω proposal said "peninsula that resists optimization" but did not commit to substrate ontology. This let through a potential failure: a well-designed generic strategy game could satisfy it without being Valoria specifically. The audit (PP-672 audit pass, F1) caught this. The revised Ω names substrate explicitly — "world whose ontology is the Thread substrate." Without this, a proposal like "medieval politics simulator with clock pressure" would pass Ω; with it, the proposal must ground in Thread or fail.

**What Ω does not require.**

- Does not require that every mechanic touch every clause. Most mechanics serve 1–2 clauses. A new companion dialogue system might serve only (b). A new faction priority tree might serve only (c). The requirement is that the mechanic not actively violate any clause.
- Does not dictate aesthetic tone. "Cross-scale consequence" does not imply grimdark; it implies that a local decision registers elsewhere. The tone of that registration is authorial.
- Does not require explicit Thread-visual language in every mechanic. A tax collection mechanic need not visually show thread-manipulation to satisfy Μ-γ. It must correspond to substrate state (Wealth is substrate-configuration per T-01), but the UI surface can be mundane.

---

## §2 Μ — Rationale per mode

**Why four rather than three.**

Earlier drafts proposed three Μ modes: Generative Tension, Substrate Coherence, Scale Continuity. The audit (F4, F6) identified two problems:

1. "Generative Tension" conflated tension-forces-engagement with independent-agents-producing-events. These are distinct: a single NPC could be under intense tension without producing emergent narrative; a collection of NPCs with priority trees can produce narrative without any individual being tense. The convergence throughlines (T-24) require agent composition, not tension.

2. The three modes were strategic-layer-biased. Personal transformation (Ω-b) had no mechanism. This left the framework approving strategic proposals cleanly and underspecifying personal ones.

Splitting generativity into Μ-α (pressure) and Μ-β (agent composition) resolves the first. The second was addressed by ensuring Μ-δ (cross-scale consequence) explicitly includes personal→strategic and strategic→personal flow, not only strategic→strategic. The personal layer is served by Ω-b, which routes through Μ-β (personal transformation emerges from engagement with autonomous agents like companions, NPCs, institutional AIs) and Μ-δ (transformation at personal scale registers at strategic scale via Standing, Disposition, arc emergence).

**Test distinguishing Μ-γ from Μ-δ.**

These could be the same claim ("it's all substrate" vs "substrate connects scales"). The distinguishing test: a mechanic can satisfy one and violate the other.

Example: a settlement-only Order stat that does not derive from or feed into province-scale Accord. This stat is substrate-grounded (it measures rendering-configuration of the settlement's social fabric — satisfies Μ-γ). But it does not connect scales — province-scale Accord calculation ignores it. This violates Μ-δ.

Fix: make settlement Order feed into province Accord (floor-average rule, per `settlement_layer §1.3` ED-SETT-03 resolution). Now the stat serves both.

The separation holds because the failure mode is real and specific — you can build substrate-grounded mechanics that don't cross scales.

**Why not more modes.**

Possible candidates considered and rejected:
- *Narrative Coherence*: already covered by Μ-β + Μ-δ. Emergent narrative comes from autonomous-agent composition propagating across scales.
- *Player Authorship*: dangerous. Would let through proposals where the player authors consequences (save-scum, retcon, dialogue-choice-creates-world-fact). Valoria's design rejects this via Ω-d (non-dominance); player authorship of world-fact creates dominance over simulation.
- *Aesthetic Consistency*: not a mechanical claim. Aesthetic is authorial, governed by Jordan's worldbuilding authority.

Four is the minimum coherent set.

---

## §3 М — Derivation walkthrough

### §3.1 Full T→М tag table

| T | Title | Primary М | Secondary М | Justification |
|---|---|---|---|---|
| T-01 | Everything Is Thread | М-3 | — | Ontological — all stats are substrate state. Defines substrate-grounds-all pattern. |
| T-02 | Rendering Consciousness-Performed | М-3 | — | Ontological — perception is substrate-filtered. Participates in substrate grounding. |
| T-03 | Inseparability | М-3 | М-5 | Primary ontological (every op = substrate op). Secondary scale-connecting (co-movement fires at all scales). |
| T-04 | RS Decay | М-1 | — | Clock — continuous pressure from Calamity damage. Canonical pressure pattern. |
| T-05 | TC Accumulation | М-1 | — | Clock — continuous pressure from institutional momentum. |
| T-06 | IP Accumulation | М-1 | — | Clock — continuous pressure from external intervention. |
| T-07 | Peninsular Strain | М-1 | — | Clock — continuous pressure from accumulated war. |
| T-08 | Church Rendering Reinforcement | М-4 | — | Institutional — Church's substrate-posture is rendering-reinforcement. |
| T-09 | Varfell Thread Progressive | М-4 | — | Institutional — Varfell's posture is thread-progressive. |
| T-10 | Niflhel Accelerationist | М-4 | — | Institutional — Niflhel's posture structurally diverges from RS preservation. |
| T-11 | Crown Pragmatic | М-4 | — | Institutional — Crown's posture is instrumentalist. |
| T-12 | Practitioner Arc | М-6 | М-1 | Primary forced-choice (Coherence cost forces engagement decisions). Secondary pressure (Coherence depletes). |
| T-13 | Certainty Journey | М-6 | М-3 | Primary forced-choice (irreversible descent opens capabilities, closes relationships). Secondary substrate-grounded. |
| T-14 | Conviction Architecture | М-6 | — | Forced-choice — Scar accumulation forces arc transitions. |
| T-15 | Player Progression | М-5 | — | Scale-connecting — personal Standing ladder produces settlement→province→faction progression. |
| T-16 | Knot Propagation | М-5 | М-3 | Primary scale-recursive (Knot Strain propagates through bonded contacts). Secondary substrate-grounded. |
| T-17 | Companion Moral Mirror | М-6 | — | Forced-choice — Thread power vs relational bonds. |
| T-18 | Radiation Gradient | М-2 | М-3 | Primary geography-holds-pressure (RS damage manifests spatially). Secondary substrate-grounded (radiation IS substrate state). |
| T-19 | Southernmost Hidden Front | М-2 | М-1 | Primary geographic (location-specific convergence point). Secondary pressure-feeding (expedition failure advances decay). |
| T-20 | Two Contests | М-6 | — | Forced-choice — sovereignty vs survival, insufficient resources for both. |
| T-21 | Thread Political Warfare | М-4 | М-3 | Primary institutional (distinct faction doctrines). Secondary substrate-grounded (shared RS track). |
| T-22 | Belief Lattice | М-6 | М-3 | Primary forced-choice (cooperation requires Belief revision, which is Scar-accumulation). Secondary substrate-participating. |
| T-23 | NPC Arc Emergence | М-5 | — | Scale-connecting — personal arc → faction Domain Echo → political shift → new arc triggers. |
| T-24 | Convergence as Crisis | М-5 | — | Scale-connecting — multiple throughlines intersecting at various scales produce emergent crisis. |
| T-25 | Generational Arc | М-5 | — | Scale-connecting — 30-year clock transforms personal standings into institutional reality. |

Coverage: 25 of 25. Primary distribution: М-1: 4 · М-2: 2 · М-3: 3 · М-4: 5 · М-5: 6 · М-6: 5.

### §3.2 М-dependencies explained

**М-2 presupposes М-1.** Geography is how continuous pressure distributes spatially. Without pressure (М-1), there is no uneven distribution to be geographic. Radiation Gradient (T-18) only makes sense if RS is decaying (a specific instance of М-1's pressure-is-continuous).

**М-4 presupposes М-3.** Faction substrate-postures are postures *on* the substrate. Without substrate grounding (М-3), there is nothing for factions to take postures toward. The Church's rendering-reinforcement, Varfell's thread-progression, Niflhel's accelerationism, Crown's instrumentalism — each is a stance on how to relate to Thread. No Thread, no stance.

**М-5 presupposes М-3.** Cross-scale consequence propagates because all scales share the substrate. A personal Thread operation produces peninsula-scale co-movement because both are operations on the same medium. Without shared substrate, scales would need separate mechanics and the framework would be approving multiple incommensurable game-systems under one name.

**М-6 presupposes М-1.** Forced choice requires scarcity. Without continuous pressure, resources replenish and choices are not forced. М-1 creates the conditions under which choices become sacrificial rather than additive.

### §3.3 Why reclassifications from PP-671

The previous meta-throughlines document (PP-671) had misclassifications caught by audit:

- Old М-1 "Decay-as-default" lumped T-16 Knot Propagation as a decay mechanic. But Knot Propagation is not primarily about decay — it is a scale-recursive relational mechanic. Removed from М-1; moved to М-5 (primary) with М-3 (secondary).

- Old М-1 included T-18 Radiation Gradient and T-19 Southernmost Hidden Front. These are geographic, not clock-based. They feed decay but their structural pattern is spatial. Split off into new М-2 (Geography holds pressure).

- Old М-2 "Substrate as universal medium" included T-08 (Church), T-13 (Certainty), T-18, T-21, T-22. Most were secondary participations. The primary substrate-grounding T's are T-01, T-02, T-03 — the ontological throughlines. Revised М-3 primary list to these three.

- Old М-3 "Institutional identity" included T-05 (TC accumulation). But T-05 is clock-based, not identity-based. The Church HAS an identity (T-08) distinct from the fact that TC accumulates over time (T-05). Removed T-05 from М-3 (now М-4); left it in М-1 where it belongs.

- Old М-4 "Scale-preserving" included T-01 and T-18 and T-19. T-01 is ontological not structural-repetition; T-18/T-19 are geographic. Cleaned up to true scale-connecting T's: T-03 (secondary), T-15, T-16, T-23, T-24, T-25.

Result: six tight М patterns with clean T assignments, each T having a primary home.

---

## §4 Why Q is separated from belonging

Quality and belonging are distinct axes. A proposal can:
- Belong and be well-crafted (ideal).
- Belong and be poorly crafted (needs iteration — keep working).
- Not belong and be well-crafted (reject — polished doesn't mean valid).
- Not belong and be poorly crafted (reject — obvious).

Conflating them makes the first and fourth cases work correctly but mishandles the second and third. A beautifully implemented merchant caravan minigame that doesn't ground in Thread should be rejected regardless of craft. A shoddy first-pass Thread-witnessing mechanic should be iterated on, not rejected, because the shape is correct.

Separating Q from belonging lets reviewers give accurate feedback: "this is vision-aligned but needs execution work" vs "this is clean code but wrong game." The failure modes are different; treating them the same wastes revision cycles.

---

## §5 Worked examples

### §5.1 PP-666 settlement adjacency (Class A, passes)

**Ω check:**
- (a) Cross-scale: settlement-scale army movement produces province-scale control changes. YES.
- (b) Personal: Thread-Witnessed edges allow practitioner Leap between Thread-sensitive settlements — substrate-interaction at personal scale. YES.
- (c) Autonomous: armies at settlements, siege clocks, Order decay from siege — all continue without player action. YES.
- (d) Non-dominance: bypass vs assault vs siege presents three distinct approaches each with costs. No option dominates. YES.

**Ω passes.**

**Μ check:**
- Μ-α Pressure: siege Order decay continues seasonally. Extends pressure mechanics.
- Μ-β Autonomous: army AI moves along edges independently. Supports agent composition.
- Μ-γ Substrate: Thread-Witnessed edge type grounds movement in substrate. Extends ontology.
- Μ-δ Cross-scale: settlement-level battles change province control. Extends scale-connection.

Primary Μ served: Μ-δ (strong cross-scale). No Μ undermined.

**М ratings:**
- М-1 Pressure: ✓
- М-2 Geography: + (edge types encode spatial relationships structurally)
- М-3 Substrate: ✓
- М-4 Institutions: ○
- М-5 Scales: + (settlement↔province explicit)
- М-6 Choice: + (bypass/assault/siege as forced choice)

Three extensions, zero violations. **Passes belonging.**

**Τ check:** touches T-04 (RS from battles), T-07 (Strain), T-18 (geographic through edge types). All chains intact.

**Q check (robust):** three approaches verified. World-state change: province control transfer visible. Player-independent scenario: two NPC factions can battle each other over a settlement without player input; stakes are visible (provincial control at stake).

**Q check (smooth):** methodology uses existing mass_battle_v30 resolution. Scale transition: battle zooms from strategic edge to tactical scene. Temporal: strategic clock pauses during battle scene.

**Q check (elegant):** core rule "armies move along settlement edges; battles fire at destinations" restatable in one reading. Second-order consequence: Fortress settlements become chokepoints because bypass requires Military exceeding Fortress Defense by 3+. Dependencies: existing mass_battle, geography_v30. No special cases.

**Verdict:** build. Already built and committed per PP-666.

### §5.2 Hypothetical Hafenmark Food Vulnerability (Class B, passes)

Extension to existing Hafenmark faction mechanics.

**Μ check:** Μ-α (new pressure source), Μ-γ (Food is substrate-state of economic configuration). No undermining.

**М ratings:**
- М-1 +: new pressure source
- М-3 +: new substrate state
- М-4 +: addresses Hafenmark substrate-posture gap flagged in ED-717
- М-6 +: food security vs military spending tradeoff

Four extensions, no violations. **Passes belonging.**

**Τ check:** touches T-07 (Strain feeds into food scarcity), T-11 (Crown-Hafenmark trade relationships). Chains extended.

**Q checks:** would need full spec to evaluate; shape is correct.

**Verdict:** shape approved. Specify and iterate.

### §5.3 Hypothetical: 10-season peace treaty (Class A, fails)

"Add a 10-season peace treaty mechanic that suspends all combat."

**Ω check:**
- (d) Non-dominance: **FAIL.** For any player losing militarily, this is a dominant strategy — sign treaty, stabilize, build, resume war when favorable.
- (c) Autonomous: **FAIL.** During the 10 seasons, the strategic pressure layer stops. The world stops pressing.

**Ω fails two clauses. Flag to Jordan. Do not proceed past Ω without Jordan's judgment.**

If Jordan approves the concept anyway (perhaps reframed), redesign would need to: preserve pressure (e.g., treaty violation Casus Belli that advances with time), prevent dominance (e.g., treaty imposes its own costs during the period — Mandate penalty, political concessions), and couple to personal scale (e.g., peace treaty creates NPC arc triggers for dissatisfied officers).

### §5.4 Hypothetical: Merchant caravan minigame (Class A, fails)

"Add a standalone merchant caravan trading system with its own resource type."

**Ω check:**
- Does not ground in Thread substrate. The proposal describes a parallel economic layer with no substrate-state correlate.
- Strategic-only — scene-layer caravan operation is proposed but no personal transformation mechanism.

**Μ check:**
- Μ-γ Substrate: **FAIL.** Flavor-only. Thread language absent; mechanic operates as parallel system.

**Ω and Μ both fail on substrate grounding. Flag as flavor-only per Failure Lexicon.**

Redesign option: if caravan trade is actually desirable, ground it in existing substrate — Wealth (already substrate-state per T-01), Trade Network tokens (existing substrate mechanic), Guild management (existing substrate-posture). A caravan system built on these is not flavor-only; it is an interface to existing substrate mechanics.

### §5.5 Hypothetical: Permanent Standing-7 stat boost (Class B, fails)

"When a player reaches Standing 7, they get permanent +2 to their highest stat."

**Ω check:**
- (d) Non-dominance: **FAIL.** Permanent stat boost with no cost. Once earned, it persists with no pressure to lose it.

**Μ check:**
- Μ-α Pressure: **FAIL.** Unearned stability. No ongoing cost, no decay, no maintenance.

**М check:**
- М-1 Pressure: − (violates; provides reward without pressure maintenance)
- М-6 Choice: − (no tradeoff; reward without cost)

**Fails Ω-d, Μ-α, М-1, М-6.** Reject or redesign.

Redesign: the stat boost is fine *if* it has ongoing cost — e.g., Standing 7 brings +2 to a stat but also increases target-level for intrigue actions, or creates a Conviction Scar accumulation rate increase, or a periodic Mandate check. Now the reward is paid for.

### §5.6 Hypothetical: Reskinned Hafenmark institution (Class B, fails)

"Give Hafenmark a Parliament mechanic identical to Crown's Parliament mechanic."

**М check:**
- М-4 Institutions: **FAIL.** Reskinned attractor. Hafenmark would be Crown-with-paint.

**Fails М-4.** Redesign: Hafenmark's Parliament must differ structurally from Crown's — e.g., Hafenmark Parliament votes are weighted by Wealth (commercial oligarchy) rather than Mandate (divine right); Hafenmark Parliamentary motions require specific coalitions reflecting merchant-class interests not military-caste interests.

---

## §6 Μ̄ — Godot translation rationale

| Commitment | Implementation | Why |
|---|---|---|
| Ω-a Cross-scale consequence | Strategic map shows all scales simultaneously | If scales are visible separately (mode-locked), player can't trace cross-scale consequence — breaks the causal reading Ω-a requires. |
| Ω-b Personal transformation | Character state persists; transformation as distinct scenes | A11 Epistemic Seduction is irreversible in canon; implementation must render this as scene-level weight, not a UI flag update. The player witnesses the transformation. |
| Ω-c Autonomous world | Real-time strategic clock; NPCs/factions advance per AI | Turn-based pauses at strategic scale let the player dictate pace → violates autonomy. Continuous clock prevents strategic-layer save-scum. |
| Ω-d Non-dominance | Single save per campaign; commit-on-action | Multiple save slots used for trying-and-reloading difficult choices convert forced choices into puzzles. Commit-on-action prevents save-scum at the decision layer. |
| Μ-α Pressure | Decay vectors visible in world-state UI | Hidden decay = invisible pressure = player cannot feel it. UI surfacing makes pressure an engagement driver. |
| Μ-β Agent composition | Priority trees + faction AIs authoritative | If Jordan or Claude can override NPC decisions, NPC autonomy is fiction. Only explicit player mechanics (Social Contest, Domain Actions, etc.) should change NPC state. |
| Μ-γ Substrate ontology | Rendering-state parameterizes shaders | If Thread-state isn't visually present, the game's ontological commitment is nominal. Shader integration makes it real. |
| Μ-δ Cross-scale consequence | Cross-scale effects animate visibly | Consequences that propagate invisibly are functionally equivalent to not propagating. Animation is the UX version of causal tracing. |

These are requirements for the implementation to honor the framework, not suggestions. A build that ignores them produces a game-shaped-like-Valoria rather than Valoria.

---

## §7 Failure Lexicon — definitions with examples

**Rest state.** A mechanic or state that allows the player to stop making decisions and accumulate advantage passively. Example: a "consolidation season" where all decay pauses while the player builds infrastructure. Violates Ω-c (autonomy — world stops pressing) and Μ-α (pressure — no pressure to engage).

**Dominant strategy.** A choice that pays more than alternatives in all situations. Example: a Thread operation that gives a strategic benefit with no Coherence cost. Violates Ω-d and М-6. Note: a choice that dominates in *some* situations is not a dominant strategy; dominance requires context-independence.

**Flavor-only.** A mechanic using Thread/rendering language without operating on substrate state. Example: a dialogue option called "Thread persuasion" that applies a +2 bonus to social check with no RS cost, no TS requirement, no Coherence effect, no Certainty shift. The name is Thread; the mechanic is not. Violates Μ-γ.

**Scale break.** A mechanic that operates in one scale with no traceable consequence at other scales. Example: a scene-level "Thread sensing" skill that reveals information but whose use doesn't register in province-scale Church AP, doesn't accumulate Exposure, doesn't produce Knot strain in witnessing NPCs. Violates Μ-δ.

**Reskinned attractor.** A new faction given an existing faction's substrate-posture with different name/flavor. Example: adding a "Southern Church" faction that mechanically duplicates Church's TC accumulation, rendering-reinforcement AP mechanics, etc. Violates М-4 — new faction must have distinct substrate-posture, not palette-swap.

**Event without stakes.** Mechanic fires in scenarios without player action, but the stakes of those scenarios cannot be read from game state. Example: a random "a merchant was robbed" event that triggers but has no attached NPC with stake, no connected arc, no consequence if not pursued. Violates Q-robust's dramatic-legibility test.

**Special-cased.** Rule with conditional exceptions that don't derive from general principles. Example: "Siege Order decay is -1/season, except at Gransol where it's -0.5/season, except when it's winter where it's -2/season, except when Hafenmark controls adjacent territory where it's..." — each except-clause is a special case. Violates Q-smooth (doesn't compose) and Q-elegant (can't be stated concisely).

**Cost-hidden.** Capability UI that shows gains but omits costs. Example: a Thread Weaving ability tooltip showing "Target NPC Disposition +2" without showing "TC +1, RS -1, Conviction Scar on Faith-convicted observer." Violates М-6.

**Strategic-only.** Mechanic operates at peninsula scale with no personal-layer touchpoint. Example: a new peninsula-wide "Economic Crisis" clock that affects only faction-level Wealth without producing scene-level opportunities, NPC arc triggers, or character-level consequences. Violates Ω-b.

**Personal-only.** Mechanic operates at scene scale with no strategic consequence. Example: a new companion-conversation topic that produces +1 Disposition but doesn't feed into any strategic mechanic, doesn't contribute to Knot formation, doesn't register in faction Stability. Violates Ω-a.

**Authored emergence.** Mechanic claims to produce emergent narrative but actually triggers pre-authored scripted events. Example: a "random encounter" system that selects from a fixed list of scripted encounters based on game-state flags. The emergence is authorial, not compositional. Violates Μ-β.

---

## §8 Historical note: why PP-671 was insufficient

The previous meta-throughlines document (`throughlines_meta.md` committed as PP-671) identified five patterns and provided definitions, but did not function as a vetting guide. Audit findings (21 issues) included:

- **Ω gap.** PP-671 emphasized negative dynamics (decay, tension, forced choice) without articulating positive output. The project's Intent of Game requires positive feedback loop producing emergent narrative — PP-671's patterns described resistance, not generation.
- **No vetting protocol.** PP-671 said "verify 5 criteria" without rules for when, by whom, or how to resolve conflicts.
- **Misclassifications.** T-18 and T-19 in M-4 (geographic, not scale-preserving). T-05 in M-3 (clock, not identity).
- **No audience specification.** Who uses the document was undefined.
- **No integration with project-intent or quality criteria.** The "Intent of Game" definition, the robust/smooth/elegant criteria — both existed in project instructions but not referenced.
- **Abstract ratings on a satisfaction-check table** where most cells were N/A, providing no guidance.

PP-672 supersedes PP-671 as the vetting framework. The original PP-671 patterns are retained (reclassified as М-1 through М-6 with adjustments) but are no longer the whole story — they are now one tier of a five-tier hierarchy with operational protocol.

Editorial ledger entries ED-717 (Hafenmark/Löwenritter/RM institutional-attractor gaps) persist as open items flagged against М-4.

---

## §9 Open questions (for future revision)

- **When to restructure М further.** If new systems (like PP-666 three-system patch) reveal a consistent pattern not captured by existing М, the framework should expand. Current: 6 patterns. Open: is there a 7th М for "Temporal recursion" (T-03 co-movement across time, T-25 generational arc, T-13 irreversibility) or are those adequately covered by М-5?
- **Hafenmark/Löwenritter/RM substrate-postures.** ED-717 flagged that these factions lack explicit М-4 characterization. Until they get T-throughlines of their own, М-4 vetting of faction proposals involving them defaults to "undefined baseline."
- **Retroactive canon audit.** Existing canon is grandfathered. When is the right time for a systematic pass applying this framework retroactively? Probably after engine_v4 smoke-test produces concrete data about which mechanics are load-bearing.
