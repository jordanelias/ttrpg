<!-- INFILL — rationale, examples, derivation -->
<!-- Companion to: references/throughlines_meta.md (SKELETON) -->
<!-- Do not use for vetting reference; use skeleton only -->
<!-- [EDITORIAL: PP-672 — throughlines hierarchical framework infill, 2026-04-19] -->
<!-- [EDITORIAL: PP-676 — load-bearing systems column added per topographic v3 §V3-2, 2026-04-29] -->
<!-- [EDITORIAL: PP-674 — tier N (Necessity) added, framework enforcement details, 2026-04-19] -->

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

| T | Title | Primary М | Secondary М | Justification | Load-bearing systems |
|---|---|---|---|---|---|
| T-01 | Everything Is Thread | М-3 | — | Ontological — all stats are substrate state. Defines substrate-grounds-all pattern. | threadwork, derived_stats, self_rendering |
| T-02 | Rendering Consciousness-Performed | М-3 | — | Ontological — perception is substrate-filtered. Participates in substrate grounding. | self_rendering, leap_mechanism, threadwork |
| T-03 | Inseparability | М-3 | М-5 | Primary ontological (every op = substrate op). Secondary scale-connecting (co-movement fires at all scales). | threadwork, scale_transitions, self_rendering |
| T-04 | MS Decay | М-1 | — | Clock — continuous pressure from Calamity damage. Canonical pressure pattern. | clocks, ms_trajectory, peninsular_strain, threadwork |
| T-05 | CI Accumulation | М-1 | — | Clock — continuous pressure from institutional momentum. | clocks, tc_political, faction_layer |
| T-06 | IP Accumulation | М-1 | — | Clock — continuous pressure from external intervention. | clocks, peninsular_strain, victory |
| T-07 | Turmoil | М-1 | — | Clock — continuous pressure from accumulated war. | peninsular_strain, clocks, victory, tensions_deck, royal_assassination_fuse |
| T-08 | Church Rendering Reinforcement | М-4 | — | Institutional — Church's substrate-posture is rendering-reinforcement. | factions, faction_layer, threadwork, conviction_track |
| T-09 | Varfell Thread Progressive | М-4 | — | Institutional — Varfell's posture is thread-progressive. | factions, faction_layer, threadwork, conviction_track |
| T-10 | **STRUCK** (Niflhel dissolved) | — | — | Niflhel dissolved as faction. Thread exploitation distributed to settlement-level phenomena. | — |
| T-11 | Crown Pragmatic | М-4 | — | Institutional — Crown's posture is instrumentalist. | factions, faction_layer, conviction_track, threadwork |
| T-15a | Hafenmark Unmediated Sovereigntist | М-4 | М-6 | Primary institutional (divine-right governance rejects ecclesial monopoly). Secondary forced-choice (Thread revelation threatens TS-0 Baralta). | factions, faction_layer, conviction_track, baralta, threadwork |
| T-15b | Löwenritter Substrate-Agnostic Protector | М-4 | М-6 | Primary institutional (military duty, substrate irrelevant). Secondary forced-choice (revelation means military tools fight wrong war). | factions, faction_layer, military_layer, mass_combat, conviction_track, threadwork |
| T-15c | RM Substrate-Heritage Reclaimer | М-4 | М-6 | Primary institutional (unknowing substrate inheritance via Einhir practice). Secondary forced-choice (Embrace/Denial/Schism at revelation). | factions, faction_layer, conviction_track, threadwork |
| T-12 | Practitioner Arc | М-6 | М-1 | Primary forced-choice (Coherence cost forces engagement decisions). Secondary pressure (Coherence depletes). | threadwork, conviction_track, derived_stats |
| T-13 | Certainty Journey | М-6 | М-3 | Primary forced-choice (irreversible descent opens capabilities, closes relationships). Secondary substrate-grounded. | threadwork, derived_stats, conviction_track, solmund_philosophy, solmund |
| T-14 | Conviction Architecture | М-6 | — | Forced-choice — Scar accumulation forces arc transitions. | conviction_track, factions, faction_layer |
| T-15 | Player Progression | М-5 | — | Scale-connecting — personal Standing ladder produces settlement→province→faction progression. | scale_transitions, settlement_layer, faction_layer, factions |
| T-16 | Knot Propagation | М-5 | М-3 | Primary scale-recursive (Knot Strain propagates through bonded contacts). Secondary substrate-grounded. | threadwork, scale_transitions, factions |
| T-17 | Companion Moral Mirror | М-6 | — | Forced-choice — Thread power vs relational bonds. | threadwork, conviction_track, factions |
| T-18 | Radiation Gradient | М-2 | М-3 | Primary geography-holds-pressure (MS damage manifests spatially). Secondary substrate-grounded (radiation IS substrate state). | territories, ms_trajectory, threadwork, settlement_layer |
| T-19 | Southernmost Hidden Front | М-2 | М-1 | Primary geographic (location-specific convergence point). Secondary pressure-feeding (expedition failure advances decay). | territories, peninsular_strain, settlement_layer, victory, mass_combat, military_layer |
| T-20 | Two Contests | М-6 | — | Forced-choice — sovereignty vs survival, insufficient resources for both. | victory, peninsular_strain, faction_layer, conflict_architecture, mass_combat |
| T-21 | Thread Political Warfare | М-4 | М-3 | Primary institutional (distinct faction doctrines). Secondary substrate-grounded (shared MS track). | factions, faction_layer, threadwork, conflict_architecture, mass_combat |
| T-22 | Belief Lattice | М-6 | М-3 | Primary forced-choice (cooperation requires Belief revision, which is Scar-accumulation). Secondary substrate-participating. | conviction_track, threadwork, social_debate |
| T-23 | NPC Arc Emergence | М-5 | — | Scale-connecting — personal arc → faction Domain Echo → political shift → new arc triggers. | scale_transitions, faction_layer, factions, conflict_architecture, faction_succession_split |
| T-24 | Convergence as Crisis | М-5 | — | Scale-connecting — multiple throughlines intersecting at various scales produce emergent crisis. | conflict_architecture, scale_transitions, victory, tensions_deck |
| T-25 | Generational Arc | М-5 | — | Scale-connecting — 30-year clock transforms personal standings into institutional reality. | campaign_architecture, scale_transitions, faction_layer, peninsular_strain |
| T-26 | Recursion as Setting Structure (TL-3) | М-5 | М-3 | Primary scale-recursive (same dynamic at multiple scales). Secondary substrate-grounded. | scale_transitions, threadwork, factions |
| T-27 | Effects Real, Explanation Wrong (TL-4) | М-4 | М-6 | Primary institutional (faction interpretive-frame coherent-but-wrong). Secondary forced-choice (argument fails; frame-crack requires confrontation). | factions, faction_layer, threadwork |
| T-28 | Confrontation/Leap/Operation Triad (TL-5) | М-3 | М-6 | Primary substrate-grounded (three-phase engagement with substrate). Secondary forced-choice (each phase has decision architecture). | threadwork, leap_mechanism, conflict_architecture |
| T-29 | Baralta as Accidental Prophylaxis Cracker (TL-8) | М-4 | М-8 | Primary institutional (Baralta's partial prophylaxis-crack is formation-structural). Secondary access-gated (crack admits substrate content into receptive capacity). | baralta, factions, threadwork, miraculous_event, solmund |
| T-30 | Information Asymmetry as Core Mechanic (TL-7) | М-8 | М-5 | Primary access-gated (different receptive capacities at different observer-nodes). Secondary scale-recursive (asymmetry operates at all scales). | scale_transitions, threadwork, faction_layer |
| T-31 | Reflexive Suspension | М-3 | М-6 | Primary substrate-grounded (Leap geometry = suspension of layer 2 reflexive facing). Secondary forced-choice (entry commit and exit timing). М-7 ✓, М-8 primary, М-9 ✓, М-11 primary. | leap_mechanism, threadwork, derived_stats |
| T-32 | Sincere Structural Closure | М-4 | М-6 | Primary institutional (Church position formation-structural). Secondary forced-choice (frame-shift pathway). М-7 ✓, М-8 ✓, М-9 primary extension. | factions, faction_layer, conviction_track |
| T-33 | TS as Developmental Arc | М-3 | М-6 | Primary substrate-grounded (receptive-capacity expansion). Secondary forced-choice (confrontation Hold/Turn-Away). М-7 ✓, М-8 ✓, М-10 ✓, М-11 primary extension. | threadwork, derived_stats, conviction_track |
| T-34 | Distal Interoception through Knot Tethers | М-5 | М-3 | Primary scale-connecting (knot-channels cross geographic distance). Secondary substrate-grounded. М-7 ✓, М-8 ✓, М-9 ✓, М-10 primary extension. | threadwork, scale_transitions, factions |
| T-35 | Unified Uncanny Capacity Synthesis | М-3 | М-4 | Primary substrate-grounded (uncanny register emerges from TS-band receptive capacity). Secondary institutional (formation + frame). М-7 ✓, М-8 primary extension, М-9 ✓. | threadwork, derived_stats, factions |
| T-36 | Relational Ontological Identity (TS 50–69 C0) | М-5 | М-3 | Primary scale-connecting (companion knots load-bearing at ontological scale). Secondary substrate-grounded. М-7 ✓, М-8 ✓. | threadwork, scale_transitions, factions |
| T-37 | Stimulus Resistance Triplet | М-3 | М-8 | Primary substrate-grounded (three resistance modes at integration-failure loci). Secondary access-gated. М-7 ✓, М-8 ✓, М-9 ✓. | threadwork, derived_stats |
| T-38 | Real as Continuous Amplitude | М-3 | М-2 | Primary substrate-grounded (amplitude is continuous substrate-excess). Secondary geography-holds-pressure. М-7 ✓, М-8 ✓, М-10 primary extension. | threadwork, ms_trajectory, territories |
| T-39 | Textual Mode Typology | М-4 | М-3 | Primary institutional (four-mode faction-output typology). Secondary substrate-grounded. М-7 ✓, М-8 ✓, М-9 ✓. | factions, faction_layer, social_debate |
| T-40 | TS as Taxonomic Expansion | М-5 | М-3 | Primary scale-connecting (taxonomic categories admit scale-spanning content at thresholds). Secondary substrate-grounded. М-7 ✓, М-8 ✓, М-10 ✓, М-11 primary extension. | threadwork, derived_stats, scale_transitions |
| T-41 | Damaged Substrate Is Non-Agential | М-3 | М-4 | Primary substrate-grounded (damage-as-substrate-state without moral agent). Secondary institutional (Church-demonology as interpreter output per T-27). М-7 ✓, М-9 primary extension, М-10 ✓. | threadwork, factions, ms_trajectory |

Coverage: 40 of 41 + T-15a/b/c (T-10 struck; T-15a/b/c added; T-26..T-41 from v3.1 synthesis). Primary distribution: М-1: 4 · М-2: 2 · М-3: 14 · М-4: 11 · М-5: 8 · М-6: 5 · М-7..М-11: cross-cutting extensions primarily on T-31..T-41.

М-7..М-11 primary extensions: М-8 primary on T-30, T-35. М-9 primary extension on T-32, T-41. М-10 primary extension on T-34, T-38. М-11 primary extension on T-31, T-33, T-40.

### §3.4 М-7 detailed specification — Borrowings Are Operational Extensions

**Pattern.** Every scholarly-lineage concept the framework adopts contributes a component to a composite operational assembly. Each component is structurally continuous with its source; each is deployed within the framework's operational architecture rather than preserved in source-native register. The composite is framework-original in assembly; components have clean precedent.

**Instances.** Husserl epoché (radicalised into reflexive-only suspension + operational Leap); Metzinger PSM (opacity as TS arc); Block phenomenal-vs-access (reflexive = access); Global Workspace (specialist-level thread work); Kierkegaard leap and repetition (First Leap + iterability); Lacan Real and Symbolic (monstrosity as non-Symbolic-nettable); apophatic theology + Ein Sof (tzimtzum-grounded structural wall at ground; non-apophatic cartographic middle per ED-738); Lurianic Kabbalah (tzimtzum + tikkun without qelippot); clinical-trauma phenomenology family (anosognosia, Capgras, Cotard, DPDR, structural dissociation); Gibsonian ecological psychology; Kaplan ART; Clark-Chalmers extended mind; Tolmanian and Lynchian wayfinding; Prinzhorn and Dubuffet art brut.

**Derivation.** 25+ cells across Sessions 1–7. Canonical acknowledgment pending (canon/00 §1.2 extension per ED-738 §8).

**Parent Μ.** Μ-γ + Μ-β.

### §3.5 М-8 detailed specification — Access Is Vertical-Position Gated (Within the Renderable)

**Pattern.** What any being can receive of the game world is gated by position relative to the waterline of ordinary rendering (canon/01 Am 3 explicit): ordinary perception above the waterline; reflexive + outward facing at the waterline; below-waterline content receivable during Leap contact (canon/02 Am 1) or at TS-cultivated receptive capacity. All renderable content is in principle describable within conditions-dependent receptive-capacity constraints per ED-738. The renderable terminates at the Ein Sof structural wall for all beings.

**Per receptive-capacity correction (ED-738 §5).** TS expansion is expansion of what can be received, not what is given. Different observers encounter the same given; different waterlines per observer-TS admit different content into receptive capacity.

**Instances at T-level.** T-30, T-31, T-32, T-33, T-35, T-27, T-28, T-37, T-40.

**Derivation.** 9+ cells across Sessions 1–7.

**Parent Μ.** Μ-β + Μ-γ. Dependencies: М-8 → М-4 (institutions stake substrate-postures within access-gated receptive-capacity bands).

### §3.6 М-9 detailed specification — Ontological Inversion of Clinical Phenomenology

**Pattern.** Framework adopts clinical trauma-phenomenology vocabulary while inverting causal direction. Clinical vocabulary preserved (anosognosia, Capgras, Cotard, neglect, aphasia, TBI, split-brain, DPDR, structural dissociation, agnosia, Jentschian uncanny, Mori valley, solastalgia); the condition is rendered as real in the world (substrate ontological), not delusional in the patient (perceiver pathology). Clinical phenomenology provides phenomenological precision; ontological inversion provides framework-specific moral and dramatic weight.

**Instances (12+ confirmed across Sessions 1–7).** Clinical anosognosia ↔ Prophylaxis; Clinical Capgras ↔ Fragmented band; Clinical Cotard ↔ Coherence 0 freefall; Clinical hemispatial neglect ↔ non-sensitive formation; Clinical split-brain confabulation ↔ Church doctrinal output; Clinical DPDR ↔ Coherence-degraded inner phenomenology; Clinical art-brut pathologisation ↔ Coherence-degraded expression as state-accurate rendering; Clinical agnosia ↔ stimulus resists predication; Clinical category resistance ↔ framework category resistance; Ordinary place attachment ↔ framework knot-profile; Clinical solastalgia ↔ knotted-territory MS drop; Jentsch animate-or-inanimate binary ↔ ontological third category.

**Derivation.** 12+ instances across Sessions 1–7 Observation 7.

**Parent Μ.** Μ-γ + Μ-α. Dependencies: М-9 → М-7 (sub-pattern of composite assembly specific to clinical-trauma borrowings).

### §3.7 М-10 detailed specification — Environment as Constitutive Medium (Bounded by the Renderable)

**Pattern.** Environment is constitutive of practitioner capacity, not backdrop. Framework integrates 4E cognition (embodied, embedded, extended, enactive) at the substrate-ontological register: Gibsonian direct perception of substrate-specifying invariants; ART restorative environments supporting developmental registers; ontologically-reciprocal place attachment via knot profile; Clark-Chalmers extended cognitive coupling through knot channels; Tolmanian and Lynchian substrate-topological cognitive mapping at non-Euclidean scale. Environment co-constitutes what the practitioner can perceive, do, and know — bounded by М-8's renderable terminus.

**Per ED-738.** М-10 operates within the renderable. Ein Sof is not an environment; it is structural ground. Environment's constitutive role tapers toward the renderable terminus but does not cross.

**Instances at T-level.** T-33, T-38, T-16, T-34, T-40.

**Derivation.** Five-cell convergence (S6-C32..C36) + supplementary evidence across Sessions 1–7.

**Parent Μ.** Μ-δ + Μ-γ. Dependencies: М-10 → М-3; М-10 → М-2.

### §3.8 М-11 detailed specification — Voluntary and Involuntary Capacity Duality

**Pattern.** The same structural phenomenological capacity yields opposite valences depending on agency and context. Capacity is neutral; mode of engagement (chosen and cultivated with support vs undergone without support) determines developmental trajectory. Framework systematically treats the same capacity in different modes as producing trained skillful outcomes or pathological destabilising outcomes.

**Instances.**
- DPDR phenomenology: involuntary at Coherence degradation (distressing) ↔ voluntary at high-TS opacity practice (cultivated).
- Peritraumatic dissociation: involuntary trauma protection ↔ cultivated confrontation training.
- Meta-awareness: involuntary at Coherence degradation ↔ cultivated at TS development.
- Automatic expression: involuntary adjacent to Coherence-degraded output ↔ cultivated craft in inner-tradition cartographic register.
- Below-waterline perceptual relocation: involuntary at Leap reflexive suspension ↔ cultivated at high-TS voluntary opacity.

**Implication.** UX design distinguishes voluntary and involuntary registers for phenomenologically similar states. Integration-supportive conditions is the mechanism by which involuntary encounters become cultivated capacities. Pedagogy is the structural mechanism converting pathology-adjacent into developmental.

**Derivation.** Five-instance convergence across Sessions 1, 3, 5, 7.

**Parent Μ.** Μ-α + Μ-γ. Dependencies: М-11 → М-6.

---

*[EDITORIAL: ED-738-adjacent — М-7..М-11 derived from S1–S7 audit synthesis per designs/audit/rigorous_audit_synthesis_s1_s7_v3_1.md.]*

### §3.2 М-dependencies explained

**М-2 presupposes М-1.** Geography is how continuous pressure distributes spatially. Without pressure (М-1), there is no uneven distribution to be geographic. Radiation Gradient (T-18) only makes sense if MS is decaying (a specific instance of М-1's pressure-is-continuous).

**М-4 presupposes М-3.** Faction substrate-postures are postures *on* the substrate. Without substrate grounding (М-3), there is nothing for factions to take postures toward. The Church's rendering-reinforcement, Varfell's thread-progression, Crown's instrumentalism — each is a stance on how to relate to Thread. No Thread, no stance.

**М-5 presupposes М-3.** Cross-scale consequence propagates because all scales share the substrate. A personal Thread operation produces peninsula-scale co-movement because both are operations on the same medium. Without shared substrate, scales would need separate mechanics and the framework would be approving multiple incommensurable game-systems under one name.

**М-6 presupposes М-1.** Forced choice requires scarcity. Without continuous pressure, resources replenish and choices are not forced. М-1 creates the conditions under which choices become sacrificial rather than additive.

### §3.3 Why reclassifications from PP-671

The previous meta-throughlines document (PP-671) had misclassifications caught by audit:

- Old М-1 "Decay-as-default" lumped T-16 Knot Propagation as a decay mechanic. But Knot Propagation is not primarily about decay — it is a scale-recursive relational mechanic. Removed from М-1; moved to М-5 (primary) with М-3 (secondary).

- Old М-1 included T-18 Radiation Gradient and T-19 Southernmost Hidden Front. These are geographic, not clock-based. They feed decay but their structural pattern is spatial. Split off into new М-2 (Geography holds pressure).

- Old М-2 "Substrate as universal medium" included T-08 (Church), T-13 (Certainty), T-18, T-21, T-22. Most were secondary participations. The primary substrate-grounding T's are T-01, T-02, T-03 — the ontological throughlines. Revised М-3 primary list to these three.

- Old М-3 "Institutional identity" included T-05 (CI accumulation). But T-05 is clock-based, not identity-based. The Church HAS an identity (T-08) distinct from the fact that CI accumulates over time (T-05). Removed T-05 from М-3 (now М-4); left it in М-1 where it belongs.

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

**Τ check:** touches T-04 (MS from battles), T-07 (Strain), T-18 (geographic through edge types). All chains intact.

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

**Fantasy imposition.** A mechanic drawn from game-design convention (RPG, fantasy strategy, roguelike) rather than from Renaissance-era political-leadership dynamics. Example: "legendary weapons with unique properties," "class-based character abilities," "dungeon crawl encounters," "artifact collection quests." These originate from genre tropes, not the subject matter. Violates N.

**Duplicate coverage.** A proposed mechanic models a dynamic that is already mechanized elsewhere. Example: adding a "siege morale" stat when settlement Order already models the social fabric under siege. The proposal adds surface area without adding coverage. Violates N — extend existing, don't duplicate.

**Edge case mechanic.** A proposed mechanic models a dynamic that was real in the Renaissance but rare. Example: a dedicated "poisoning heir" mechanic — poisoning happened (Cesare Borgia, Catherine de Medici rumors) but was not a load-bearing dynamic distinct from Social Contest / Intrigue. Violates N — abstract into existing rather than dedicate mechanical surface.

**Abstractable.** A proposed mechanic models a dynamic that is real and load-bearing but already adequately covered by existing abstract mechanics. Example: a "portrait commissioning" stat. Patronage politics was central (Medici art patronage shaped Florentine faction dynamics), but its political function — expressing Wealth, building Prestige, signaling Faction loyalty — is covered by existing Wealth + Social Contest + Stature. Dedicated stat would add surface without insight. Violates N.

**Rest state.** A mechanic or state that allows the player to stop making decisions and accumulate advantage passively. Example: a "consolidation season" where all decay pauses while the player builds infrastructure. Violates Ω-c (autonomy — world stops pressing) and Μ-α (pressure — no pressure to engage).

**Dominant strategy.** A choice that pays more than alternatives in all situations. Example: a Thread operation that gives a strategic benefit with no Coherence cost. Violates Ω-d and М-6. Note: a choice that dominates in *some* situations is not a dominant strategy; dominance requires context-independence.

**Flavor-only.** A mechanic using Thread/rendering language without operating on substrate state. Example: a dialogue option called "Thread persuasion" that applies a +2 bonus to social check with no MS cost, no TS requirement, no Coherence effect, no Certainty shift. The name is Thread; the mechanic is not. Violates Μ-γ.

**Scale break.** A mechanic that operates in one scale with no traceable consequence at other scales. Example: a scene-level "Thread sensing" skill that reveals information but whose use doesn't register in province-scale Church AP, doesn't accumulate Exposure, doesn't produce Knot strain in witnessing NPCs. Violates Μ-δ.

**Reskinned attractor.** A new faction given an existing faction's substrate-posture with different name/flavor. Example: adding a "Southern Church" faction that mechanically duplicates Church's CI accumulation, rendering-reinforcement AP mechanics, etc. Violates М-4 — new faction must have distinct substrate-posture, not palette-swap.

**Event without stakes.** Mechanic fires in scenarios without player action, but the stakes of those scenarios cannot be read from game state. Example: a random "a merchant was robbed" event that triggers but has no attached NPC with stake, no connected arc, no consequence if not pursued. Violates Q-robust's dramatic-legibility test.

**Special-cased.** Rule with conditional exceptions that don't derive from general principles. Example: "Siege Order decay is -1/season, except at Gransol where it's -0.5/season, except when it's winter where it's -2/season, except when Hafenmark controls adjacent territory where it's..." — each except-clause is a special case. Violates Q-smooth (doesn't compose) and Q-elegant (can't be stated concisely).

**Cost-hidden.** Capability UI that shows gains but omits costs. Example: a Thread Weaving ability tooltip showing "Target NPC Disposition +2" without showing "CI +1, MS -1, Conviction Scar on Faith-convicted observer." Violates М-6.

**Strategic-only.** Mechanic operates at peninsula scale with no personal-layer touchpoint. Example: a new peninsula-wide "Economic Crisis" clock that affects only faction-level Wealth without producing scene-level opportunities, NPC arc triggers, or character-level consequences. Violates Ω-b.

**Personal-only.** Mechanic operates at scene scale with no strategic consequence. Example: a new companion-conversation topic that produces +1 Disposition but doesn't feed into any strategic mechanic, doesn't contribute to Knot formation, doesn't register in faction Stability. Violates Ω-a.

**Authored emergence.** Mechanic claims to produce emergent narrative but actually triggers pre-authored scripted events. Example: a "random encounter" system that selects from a fixed list of scripted encounters based on game-state flags. The emergence is authorial, not compositional. Violates Μ-β.

---

## §7-A Subtractive dispositions (the Failure Lexicon's missing verdict half) — ED-IN-0027, 2026-07-08

The Failure Lexicon above names *why* a mechanic doesn't deserve to exist, but §8.2's failure-behavior table only ever routes to a *constructive* disposition (build/wire/redesign/flag/iterate). For a **new proposal** that is correct — you don't add what fails N. But for an **existing action** already in the corpus, "flag Jordan, iterate" leaves over-articulation in place forever: the framework could describe the disease and never prescribe removal. The skeleton's §8.2-A supplies the subtractive verdicts (KEEP/REFINE/DISTILL/MERGE/PRUNE/CUT); this note records the two design commitments behind it.

**Why "as-if-built" is the governing rule.** A subtractive audit that penalized unbuilt actions would just be a second wiring-backlog under a hostile name — and it would fight the additive resolution program, which owns wiring debt. Keeping build-state out of the verdict is what makes the two programs *complementary*: the subtractive pass decides *what is worth building* (design merit, judged counterfactually); the additive pass decides *how to build what survives*. A stub can be a KEEP; a fully-wired action can be a CUT. The moment a verdict leans on "it isn't wired yet," it has changed subject from design to schedule, and is void.

**Why the two guards (downstream-naming + inverted critic) are not optional.** Without the downstream-naming requirement, "cut" is free — every reviewer can prune on taste and nothing is accountable; requiring each cut to name the Stratum/OPT/lane task it retires makes a cut a *measurable scope reduction* or nothing at all. Without the inverted-critic steelman, a pessimist default over-cuts by construction (the whole point is to demand each action justify itself, which biases toward removal); forcing an independent pass to argue *for* each condemned action, as-if-built, and only upholding the cut if that argument fails against source, is what keeps disciplined pessimism from becoming vandalism. In the 2026-07-08 corpus run this gate overturned 2 of 37 candidates (one for the as-if-built violation itself) and softened 2 more — evidence the guard bites.

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

Editorial ledger entry ED-717 (Hafenmark/Löwenritter/RM institutional-attractor gaps) was resolved at the framework level by T-15a/b/c additions and then propagated into all three faction design docs: Hafenmark §8.4 (factions_personal_v30) — DONE 2026-04-19; Löwenritter §8.9 — DONE 2026-04-19; RM §8.8 — DONE 2026-04-19. ED-717 fully closed.

---

## §9 Open questions (for future revision)

- **When to restructure М further.** If new systems (like PP-666 three-system patch) reveal a consistent pattern not captured by existing М, the framework should expand. Current: 6 patterns. Open: is there a 7th М for "Temporal recursion" (T-03 co-movement across time, T-25 generational arc, T-13 irreversibility) or are those adequately covered by М-5?
- **Hafenmark/Löwenritter/RM substrate-postures.** ED-717 flagged a framework-level gap. Resolved at the framework: T-15a/b/c added (see §3.1). Propagation into faction design docs complete 2026-04-19 (factions_personal_v30 §8.4 Hafenmark, §8.8 RM, §8.9 Löwenritter). All three factions now carry М-4 substrate-posture specifications. М-4 vetting of cross-faction proposals references the relevant T-throughline directly. involving them defaults to "undefined baseline."
- **Retroactive canon audit.** Existing canon is grandfathered. When is the right time for a systematic pass applying this framework retroactively? Probably after engine_v4 smoke-test produces concrete data about which mechanics are load-bearing.

---

## §10 N — NECESSITY TIER (PP-674)

### §10.1 Why N sits above Ω

Ω asks: does this belong in Valoria as game experience? N asks: does this belong in Valoria as a simulation of Renaissance-era political leadership? Both must pass, but they're different questions.

A mechanic can satisfy Ω and still fail N. Example: a cleanly-designed relic hunt system. It might produce cross-scale consequence (Ω-a), personal transformation (Ω-b), autonomous events (Ω-c), irreducible tradeoff (Ω-d). It might even ground in substrate (Μ-γ). But relic hunting is not a load-bearing dynamic of Renaissance political leadership. It's a fantasy-game convention. Complexity for its own sake.

The user's design constraint — *"we don't want complexity for the sake of it — we just have a complex game because there were many ways in which the leader of a political faction during Renaissance era could succeed fail or die"* — is a constitutive rule about what mechanics earn their place. N codifies it.

N sits as tier-0 (above Ω) because subject-grounding is prior to experiential fit. A proposal that fails N does not proceed to belonging vetting because there is nothing to be experiential-about. You cannot ask "is this a Valoria experience?" if the thing isn't Valoria material to begin with.

### §10.2 What counts as subject grounding

Valoria's subject matter is the political leadership class of the Renaissance Italian peninsula and its analogues — faction heads, condottieri, churchmen, merchant princes, landholding nobility, mercenary captains. The dynamics that were load-bearing for these people:

- **Succession** (named winners, partition on narrow claims, dynastic marriage leverage, illegitimate heirs, regency crises)
- **Excommunication politics** (papal interdict, consecration refusal, heresy accusations as political weapon)
- **Condottiere loyalty** (switching sides mid-campaign, bankruptcy-triggered betrayal, contract renegotiation under duress)
- **City-state coalitions** (Leagues, mutual defense pacts, betrayal of allies, diplomatic isolation)
- **Food and grain politics** (famine-triggered revolts, trade-route leverage, granary control)
- **Parliamentary / senatorial factional blocs** (voting coalitions, bribery, exile via vote)
- **Assassination and exposure** (successful removal, failed plots exposed, protection through faction loyalty)
- **Financial ruin** (bank collapse, bankruptcy, usury-triggered excommunication — Medici/Pazzi dynamics)
- **Territorial loss/gain** (siege, bypass, occupation, treaty concession)
- **Thread/heresy politics** (in Valoria's counterfactual) — how substrate-doctrine functions mechanically as Renaissance-era religious-political contest would

These are the *actually happened repeatedly, consequentially, to real people* category. Mechanics that model them earn their complexity.

### §10.3 What fails N

- **Fantasy imposition.** Legendary weapons, artifact hunts, named magic items, class-based abilities, adventurer-party composition, random encounter tables, dungeon crawls, loot systems. These are RPG/strategy-game conventions from genres with different source material. Rejected.

- **Duplicate coverage.** A "merchant caravan" mechanic when the Trade Network already models economic exchange. A "siege morale" mechanic when settlement Order already models the same dynamic. Rejected — extend existing, don't duplicate.

- **Edge case mechanic.** A dedicated "cardinal-bribing" mechanic. Bribery existed; it was not a load-bearing dynamic separate from Parliamentary Manoeuvre or Social Contest. Rejected — abstract into existing.

- **Abstractable.** A dedicated "portrait commissioning" stat. Patronage of art mattered; its political function is covered by existing Wealth + Prestige + Domain Actions. Rejected — existing abstractions suffice.

### §10.4 What passes N

- **PP-666 succession split** — Medici/Pazzi fracture, Habsburg partitions, Visconti breakup. Load-bearing. Pass.
- **Hypothetical Hafenmark Food Vulnerability** — Italian city-states repeatedly collapsed on grain supply (Ferrara 1481, Florence during sieges, Genoa 1528). Pass.
- **Hypothetical condottiere contract renegotiation** — Francesco Sforza turned sides repeatedly; Hawkwood switched employers; mercenary captain bankruptcy triggered cascades. Load-bearing. Pass.
- **Hypothetical papal interdict mechanic** — repeatedly decisive (Venice 1508, Florence 1376). Pass.

### §10.5 Authority on N

Jordan is subject-matter authority. Claude cannot autonomously judge whether a dynamic was load-bearing in the Renaissance — that requires specific historical knowledge Jordan has and Claude does not. Claude's role: flag when a proposal appears to fail N, articulate the failure in Failure Lexicon terms, present to Jordan for decision.

Claude can surface pattern-level concerns (e.g., "this looks like fantasy imposition because the proposal references X which I don't recall from the subject matter"). Claude cannot issue the binding verdict.

### §10.6 N interaction with Ω

Because N is tier-0, Ω vetting does not fire until N passes. However, the two tiers are independent in the sense that Ω failures still need to be raised even if N passes — a subject-grounded mechanic can still fail Ω (e.g., a historically-real "permanent peace treaty" mechanic would pass N but fail Ω-d).

In practice, the vetting workflow is:
1. N check — does this earn its existence?
2. If N pass → Ω check — does this produce the Valoria experience?
3. If both pass → Μ / М / Τ → Q.

### §10.7 Rewritten worked examples (N-updated)

**Merchant caravan minigame** (previously failed at Μ-γ). Now fails at N: **fantasy imposition**. The caravan minigame is a game-design convention, not a Renaissance-political-leadership dynamic. Note: if the proposal were instead "Trade Network crisis mechanic" — grounded in the Medici bank failure, the Venice-Ottoman trade route politics, the Genoese financial collapse — it would pass N and proceed to Ω vetting (where it would likely also pass, being substrate-grounded economic pressure).

**"Legendary weapon" system** (hypothetical). Fails N: **fantasy imposition**. Named magical weapons are a fantasy-RPG convention. The Renaissance-real analogue would be named military formations (the Swiss Guard, the Compagnia Bianca) or specific condottiere bands — those could pass N if proposed.

**PP-666 succession split** (previously passed Ω/Μ/М/Q). Now also passes N: **succession fracture is load-bearing**. The Medici inheritance dispute of 1434, Visconti partition of 1402, Habsburg partitions 1521, Pazzi conspiracy 1478 — succession on narrow claims was the single most common cause of faction-layer crisis in the era. Dedicated mechanic is earned.

---

## §11 Framework enforcement (PP-674)

### §11.1 Why enforcement matters

A framework that is advisory is not a framework. The previous state (PP-672) committed the framework document but had no enforcement — Claude could skip vetting on any commit, and would. PP-674 adds hard enforcement at the commit layer.

### §11.2 Enforcement mechanism

`valoria_hooks.vetting_gate(additions)` fires during `pre_commit_gate` when additions include `canon/patch_register_active.yaml`. It parses the patch register, finds PP entries with `id >= PP-674`, and for each verifies:

- The entry has a `vetting:` block.
- The block has `class:` with value A/B/C/D/E.
- If class is A or B, the block has all six required keys: `class`, `necessity`, `omega`, `mu`, `m_ratings`, `q`.

Failures raise RuntimeError, blocking the commit. CI runs the same check externally after push, so the gate cannot be bypassed by editing hooks in-container.

Grandfathering: entries with `pre-framework: true` are exempt. This applies to PP-001..PP-673.

### §11.3 Required `vetting:` block structure

```yaml
- id: PP-XXX
  date: YYYY-MM-DD
  # ... normal fields ...
  vetting:
    class: A                         # A|B|C|D|E
    necessity: pass                  # N result; pass | fail | flagged
    omega: pass                      # Ω result; pass | fail | flagged
    mu: [Μ-α, Μ-δ]                  # modes primarily served
    m_ratings:
      M-1: "+"                       # per §3 rubric: + | ✓ | − | ○
      M-2: "○"
      M-3: "✓"
      M-4: "○"
      M-5: "+"
      M-6: "+"
    q: pass                          # pass | iterate | skip
```

Class C/D/E can use minimal form: `vetting: { class: C }`.

### §11.4 Task type: `design_proposal`

New task type in `TASK_REQUIRED_FILES`. Requires loading `references/throughlines_meta.md` before any design_proposal work begins. Use this task gate when proposing a new mechanic — ensures framework skeleton is in context.

### §11.5 Auditable audit trail

Every Class A/B patch from PP-674 onward has a permanent vetting record in the patch register. This produces:

- A reviewable history of why each system was approved.
- Data for pattern-detection — are certain М's consistently violated? Are N failures flagged but merged anyway?
- A self-validating protocol — PP-674 itself carries a vetting block (the first).

### §11.6 What enforcement does NOT do

- Does not vet Class C/D/E proposals substantively. Minimal class marker suffices.
- Does not re-vet existing (pre-PP-674) mechanics. Grandfathered.
- Does not enforce framework text — if the framework document changes, existing vetting records become inconsistent but are not retroactively invalidated.
- Does not catch misclassification — a Class A proposal misclassified as Class C will skip vetting. The classification itself requires human judgment.

The enforcement catches *procedural* framework violations (missing vetting blocks). *Substantive* framework violations (wrong M ratings, false N pass) require Jordan's review — hence the authority chain.

---

# Solmund Throughlines (PART 8) — moved to appendix

The Stage 4 Solmund split appended PART 8 content here as prose, but conflict-eval finding MEDIUM-03 noted that downstream tooling parsing the canonical T-NN table format would not see those entries. The PART 8 content has been **moved to** `references/throughlines_meta_solmund_appendix.md` (2026-04-25 follow-up).

That appendix holds 5 throughlines (T-A..T-E placeholders) and implementation priorities, awaiting Jordan's integration into the canonical throughlines table with real T-NN numbers + parent_meta (М-NN) assignments.
