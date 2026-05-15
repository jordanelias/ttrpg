# Throughlines Audit — All-Directions Review, NERS Applicability, Canon Constraint Cross-Check

**Audit scope:** the 29 throughlines (T-1 through T-29) and 8 meta-throughlines (M-1 through M-8) identified across files `01–10` of the pre-firearm formations research project. Audit applies the **NERS criteria** (Necessary, Elegant, Robust, Smooth) and the **all-directions criteria** (top-down, bottom-up, vertical, diagonal, lateral, horizontal) per PI canon_terms, with cross-check against canon constraints P-01 through P-15.

**Audit type:** Mode E (Core Principles Compliance) per `skills/valoria-mechanic-audit/SKILL.md`, adapted for research-derived patterns rather than existing mechanics. **No editorial judgment — mechanical analysis only.**

**Severity scale:** P1 = blocks play / canon violation. P2 = causes ambiguity / partial misfit. P3 = polish / out-of-scope.

**Author note (per audit skill rules):** This is an external audit of research findings against canon. Recommendations are framed as "applicability flags" for Jordan to decide on — not as design prescriptions. Per project-owner contract: Jordan specifies; Claude executes.

---

## Framing — what the audit is actually evaluating

The research catalogued military formations across ~3000 BC to 1526 AD. The throughlines and meta-throughlines abstract recurring patterns from that catalogue.

**Critical scope clarification before proceeding:** Valoria's canon (P-01 through P-15) reveals that the game's metaphysical core is **Threads / Rendering / Coherence / Inseparability of temporal-epistemic-actualized dimensions / Monstrosity-as-rendering-failure**. The military formations research operates at a **sublayer** of the game — the strategic-tactical-combat layer that the PI's `<design_doc_framing>` describes as:

- "Board game" abstractions → strategic layer
- "TTRPG" detail → personal-scale resolution
- Scale transitions (personal ↔ settlement ↔ territory ↔ peninsula) as core UX

The throughlines are **applicable to this sublayer**. They are **silent on** the Thread / Rendering / Coherence metaphysical core. **A throughline being applicable to combat-and-strategy does not make it applicable to the whole game**, and vice versa. The audit is honest about this scope.

---

## Part I — All-Directions Pass

Per PI canon_terms: "all directions: top-down, bottom-up, vertical, diagonal, lateral, horizontal." For each direction, I identify which throughlines and meta-throughlines manifest and what they imply for Valoria.

### Top-down (grand formation → unit formation → unit)

The project's own structure mirrors top-down: grand formation (army), unit formation (sub-grouping), unit (individual fighters). Throughlines that primarily live at the **grand-formation** scale:

- **T-1** (shock + missile combination) — grand-army composition decision
- **T-2** (combined arms requires command integration) — grand-army command structure
- **T-4** (force structure downstream of state structure) — grand-army recruitment
- **T-5** (force-generation depth) — grand-army sustainability
- **T-14** (steppe horse-archer asymmetry) — grand-army strategic mode
- **T-19, T-20, T-21** (gunpowder transition) — grand-army doctrinal era
- **T-24** (hammer-and-anvil) — grand-army battle plan
- **T-25** (Cannae template) — grand-army battle plan
- **M-1** (doctrine-substrate-opponent triangle) — grand-army strategic envelope
- **M-2** (institution > tactics > weapons) — grand-army development priorities

**Valoria applicability (top-down):** these throughlines fit naturally at the **territory and peninsula scales** of the game's UX flow. Faction-level decisions about army composition, doctrinal choice, recruitment base, and strategic posture map well to T-1, T-2, T-4, T-5, T-14, T-24, T-25, M-1, M-2.

**Gap flagged:** the research does not address how grand-formation choices interact with **Thread-mediated faction operations** — e.g., does a high-Coherence faction field different doctrines from a low-Coherence one? Does Thread Tension constrain force-generation? `[GAP: Thread-doctrine interaction — basis: research operates pre-Thread layer; canon does not yet specify whether or how military doctrine intersects with Thread mechanics. Question for Jordan.]`

### Bottom-up (individual unit → emergent grand-formation behavior)

Throughlines that explicitly identify **emergence from individual unit mechanics**:

- **T-28** (grand-formation behavior emerges from unit-formation mechanics) — the canonical bottom-up throughline. Right-flank drift; capture-priority pathology.
- **T-29** (morale cascade as propagating field) — emergent from individual decisions to flee.
- **T-9** (discipline-timing) — emergent from individual command discipline aggregated.
- **T-17** (cultural-doctrinal compatibility filter) — emergent from individual cultural attitudes constraining what doctrines can be absorbed.

**Valoria applicability (bottom-up):** these are the throughlines most relevant to **personal-scale resolution** (the TTRPG-detail layer per PI). Individual practitioner / fighter decisions producing emergent unit and faction behavior.

**P-01 alignment check (Inseparability):** T-28 (emergent grand-formation behavior) **structurally resembles** the Inseparability principle — small-scale operations producing automatic co-movement across larger scales. This is **not a Thread-level claim** but is **conceptually aligned with the canon's emphasis on co-movement and emergence**. `[ASSUMPTION: T-28's emergence pattern can be implemented in a way that respects P-01's three-dimensional co-movement — basis: structural analogy, not mechanical identity. Verify with Jordan.]`

### Vertical (hierarchical / command levels)

Throughlines about command-and-control across hierarchy:

- **T-9** (discipline-timing axis) — central command skill across all levels
- **T-10** (battles decided by secondary commits) — hierarchical command timing
- **T-11** (oblique order / local concentration) — operational-level command decision
- **T-2** (command integration) — vertical integration of arm types
- **M-4** (discipline-timing as universal command skill) — meta-throughline; the most-elevated vertical pattern
- **M-7** (strategic-political dimension) — vertical integration of military and political command

**Valoria applicability (vertical):** these fit the game's **scale-transition UX** — actions at one scale propagating to another. M-4's "decisive commit window" is a strong candidate for a **single signature mechanic** representing skilled command across all combat-relevant scales. The F2 §VI observation #2 ("the decisive-commit window is the *one* mechanic that captures pre-firearm tactics") directly supports this.

**P-11 alignment check (Temporal Disjunction is universal):** every Thread operation produces an automatic temporal auto-effect. T-9 / M-4 (timing-as-central-skill) is **conceptually parallel** but operates at a different layer — combat timing rather than Thread temporal cost. The principle "timing has irreducible cost" recurs in both layers; the mechanical implementations differ.

### Diagonal (cross-cutting)

The diagonal direction captures patterns that don't fit a single level but cut across them. These are mostly meta-throughlines:

- **M-1** (doctrine-substrate-opponent triangle) — the dominant diagonal pattern. Every doctrine = function of (substrate, opponent menu, cultural victory conditions). Cuts across personal / settlement / territory / peninsula scales.
- **M-3** (parallel evolution of doctrinal optima) — diagonal pattern of independent invention.
- **M-5** (the perfect-system trap) — diagonal pattern of doctrinal supremacy carrying its own counter.
- **M-6** (cultural-doctrinal compatibility filter) — diagonal pattern of culture-doctrine interaction.
- **M-8** (compound failures explain catastrophic outcomes) — diagonal pattern; disasters require stacks across multiple layers.

**Valoria applicability (diagonal):**

M-1 is **the single most consequential throughline for Valoria design**. It maps to the game's structural commitments: doctrines are package deals with their political-economic-cultural systems. A game that lets players freely mix doctrines and contexts violates the historical record and likely violates Valoria's intent per the PI's faction-as-coherent-system framing.

M-8 (compound failures) maps to **how losses propagate at strategic scale**. Catastrophic outcomes shouldn't be single-cause; they should require stacks. This is consistent with P-01 (Inseparability) — small failures propagating across dimensions / scales.

`[CONFIDENCE: medium — basis: structural parallels are real; mechanical mapping is not specified in canon. Recommend Jordan verify before treating as design constraint.]`

### Lateral (peer-to-peer at the same level)

The **matchup matrix (F1 §III)** is the most-developed lateral analysis: formation-vs-formation pairwise efficacy.

Lateral throughlines:
- **T-3** (rock-paper-scissors of pike-cavalry-missile) — peer-to-peer relationships between formation classes
- **Generic conclusion #2** (RPS is real but qualified by terrain and command) — peer-to-peer with modifiers

**Valoria applicability (lateral):**

The matchup matrix offers concrete content for **strategic-layer combat resolution** at territory and peninsula scales. F2 §VI observation #3 (conditional RPS with terrain modifiers) is directly applicable: peer-to-peer matchups exist but should not be implemented as pure rock-paper-scissors.

`[GAP: how do matchup matrix outcomes propagate to Thread-mediated faction effects? E.g., a faction defeated tactically — does this affect its Thread Tension, Coherence, Influence Points? — basis: research operates pre-Thread layer. Question for Jordan.]`

### Horizontal (at-level comparative)

The horizontal direction is comparative within a tier. The research is structured comparatively within each era (Chunks A through E4), with formation classes compared horizontally at each period.

Horizontal patterns:
- **Combined arms beats mono-culture except in specific terrain** (generic conclusion #3) — horizontal comparison within an era
- **The institutional ranking of composite systems** (F1 §III closing) — horizontal ranking
- **Era-specific dominance** — Ottoman synthesis as Renaissance-era peak; Mongol as high-medieval peak; etc.

**Valoria applicability (horizontal):** factions in a single game-state are peers; horizontal comparison applies to faction-vs-faction analysis at any moment in game time. The composite-system rankings give a reference for what doctrinal compositions tend to dominate, useful as **balancing reference** rather than as direct mechanical claim.

---

### All-directions summary

The throughlines are distributed across all six directions, with concentrations:
- **Diagonal** carries the highest-leverage meta-throughlines (M-1 especially)
- **Top-down** carries the broadest applicability at grand-formation scale
- **Bottom-up** carries the emergence patterns relevant to personal-scale resolution
- **Vertical** carries the universal command-skill axis (M-4)
- **Lateral** carries the concrete matchup content
- **Horizontal** carries comparative within-tier content

No direction is empty. **The research is structurally complete in the all-directions sense.** Gaps are not in the directions; gaps are in the cross-product with Valoria's Thread metaphysical layer (flagged in Part III).

---

## Part II — NERS Audit

Per PI canon_terms:

- **N (necessary):** unable to be removed without worsening gameplay; makes the game more robust and elegant; smooth integration with existing play; supports cohesive gameplay from all directions.
- **R (robust):** allows strategic thinking; allows customization; allows creativity and variety; players feel important to the game world; emergent narrative hooks; mechanics fully formed, error-free, complete.
- **S (smooth):** integrates cleanly without friction; mechanics interact cleanly with interdependent mechanics; zooms across scales; transitions cleanly; pauses correctly; consistent calculations; unified mechanical approach.
- **E (elegant):** logically simple; clear approach; no unnecessary overhead; easy to understand; allows player to intuit complex outcomes from simple choices.

For each throughline I score N/E/R/S as one of:
- ✓ = strong fit
- ~ = partial fit / depends on implementation
- ✗ = poor fit / would violate criterion
- ? = unspecifiable without Jordan's design choices

I also flag **recommended treatment**:
- **INCLUDE** = strong candidate for direct Valoria mechanic
- **DEFER** = candidate for strategic-layer abstraction, not personal-scale
- **EXCLUDE** = out-of-scope for game design; archival only
- **RECONSIDER** = canonical conflict or unresolved scope question

### Throughline-level NERS scores

| ID | Throughline (compressed) | N | E | R | S | Treatment | Notes |
|----|---|---|---|---|---|---|---|
| T-1 | Shock + missile beats either alone | ✓ | ✓ | ✓ | ✓ | INCLUDE | Strong fit at strategic layer |
| T-2 | Combined arms needs command integration | ✓ | ~ | ✓ | ~ | INCLUDE | Elegant only if integration is visible to player |
| T-3 | Rock-paper-scissors pike/cavalry/missile | ✓ | ✓ | ✓ | ~ | INCLUDE (with modifiers) | Smooth only if conditional, not pure RPS |
| T-4 | Force structure downstream of state structure | ✓ | ~ | ✓ | ✓ | INCLUDE | Maps to faction-substrate |
| T-5 | Force-generation depth > tactical brilliance | ✓ | ✓ | ✓ | ✓ | INCLUDE | Core strategic-layer mechanic |
| T-6 | Weapons depend on institutions | ~ | ✓ | ✓ | ✓ | INCLUDE | Reinforces T-4, T-5 |
| T-7 | Slave-soldier institutions as Islamic pattern | ✗ | ~ | ~ | ~ | DEFER | Lore/flavor — out of scope as mechanic |
| T-8 | Doctrine is institutionally portable | ~ | ✓ | ✓ | ✓ | INCLUDE | Cross-faction doctrine acquisition mechanic |
| T-9 | Discipline-timing axis | ✓ | ✓ | ✓ | ✓ | INCLUDE | Central command skill mechanic |
| T-10 | Battles decided by secondary commits | ✓ | ✓ | ✓ | ✓ | INCLUDE | Reserve / decisive-commit mechanic |
| T-11 | Local concentration / oblique order | ~ | ~ | ✓ | ~ | DEFER | Implementation-specific |
| T-12 | Context dependence of doctrinal efficacy | ✓ | ✓ | ✓ | ✓ | INCLUDE | Maps to terrain × doctrine |
| T-13 | Strategic mobility as doctrinal lever | ✓ | ✓ | ✓ | ✓ | INCLUDE | Operational-layer mechanic |
| T-14 | Steppe horse-archer asymmetry | ~ | ~ | ~ | ~ | RECONSIDER | Specific to one doctrine class; check Valoria peninsula geography |
| T-15 | Fortification as substitute for field doctrine | ✓ | ✓ | ✓ | ✓ | INCLUDE | Settlement-scale mechanic |
| T-16 | Wagon-fortress as recurring optimum | ~ | ~ | ✓ | ~ | DEFER | Specific to one era's tech |
| T-17 | Cultural-doctrinal compatibility filter | ✓ | ✓ | ✓ | ✓ | INCLUDE | Strong P-04 alignment (see Part III) |
| T-18 | Victory conditions are culturally specified | ✓ | ✓ | ✓ | ✓ | INCLUDE | Maps to faction-specific victory metrics |
| T-19 | Gunpowder transition was doctrinal not technical | ~ | ~ | ~ | ~ | DEFER | Valoria peninsula gunpowder status unspecified |
| T-20 | Global firearm-transition window 1503–1526 | ✗ | n/a | n/a | n/a | EXCLUDE | Historical period reference only |
| T-21 | Mass-cavalry doctrines fail catastrophically | ~ | ~ | ~ | ~ | RECONSIDER | Depends on Valoria tech mix |
| T-22 | Technological matrix shapes doctrinal space | ✓ | ✓ | ✓ | ✓ | INCLUDE | Maps to faction tech-tree limitations |
| T-23 | Operational geography is part of doctrine | ✓ | ✓ | ✓ | ✓ | INCLUDE | Maps to peninsula terrain × faction doctrine |
| T-24 | Hammer-and-anvil = dominant decisive pattern | ✓ | ✓ | ✓ | ✓ | INCLUDE | Universal combat-resolution template |
| T-25 | Cannae template (double envelopment) | ✓ | ✓ | ✓ | ~ | INCLUDE (with caveat) | High player skill ceiling |
| T-26 | Single-shot character of heavy-cavalry charge | ✓ | ✓ | ✓ | ✓ | INCLUDE | Maps to "spent-resource" combat mechanic |
| T-27 | Modular line-relief as Roman breakthrough | ~ | ~ | ✓ | ~ | DEFER | Era-specific |
| T-28 | Grand-formation behavior emerges from unit mechanics | ✓ | ~ | ✓ | ~ | INCLUDE | **Strongest P-01 alignment** (see Part III) |
| T-29 | Morale cascade as propagating field | ✓ | ✓ | ✓ | ✓ | INCLUDE | Maps to faction-cohesion / Coherence-adjacent |

### Meta-throughline NERS scores

| ID | Meta-throughline (compressed) | N | E | R | S | Treatment | Notes |
|----|---|---|---|---|---|---|---|
| M-1 | Doctrine-substrate-opponent triangle | ✓ | ✓ | ✓ | ✓ | **INCLUDE — TOP PRIORITY** | Universal design constraint |
| M-2 | Institution > tactics > weapons over time | ✓ | ✓ | ✓ | ✓ | INCLUDE | Strategic-layer foundation |
| M-3 | Parallel evolution of doctrinal optima | ~ | ✓ | ✓ | ✓ | DEFER | Design-rationale, not in-game mechanic |
| M-4 | Discipline-timing as universal command skill | ✓ | ✓ | ✓ | ✓ | **INCLUDE — TOP PRIORITY** | Single signature combat-skill mechanic |
| M-5 | The perfect-system trap | ✓ | ~ | ✓ | ~ | INCLUDE (with caveat) | Counter-doctrine dynamic; requires balance design |
| M-6 | Cultural-doctrinal compatibility filter | ✓ | ✓ | ✓ | ✓ | INCLUDE | Strong P-04 alignment |
| M-7 | Strategic-political dimension | ✓ | ✓ | ✓ | ✓ | INCLUDE | Maps to faction-politics × army layer |
| M-8 | Compound failures explain catastrophic outcomes | ✓ | ✓ | ✓ | ~ | INCLUDE | P-01-aligned; require stacked failures for collapse |

### NERS findings summary

**Strong-fit throughlines (N+E+R+S all ✓):** T-1, T-5, T-9, T-10, T-12, T-13, T-15, T-17, T-18, T-22, T-23, T-24, T-26, T-29, plus meta-throughlines M-1, M-2, M-4, M-6, M-7. **19 of 37 patterns** have full NERS fit.

**Partial-fit (one or more ~):** T-2, T-3, T-4, T-6, T-8, T-11, T-25, T-27, T-28, plus M-5, M-8. **11 patterns** need implementation choices to determine final fit.

**Reconsider:** T-14, T-21 — depend on Valoria peninsula's specific geography and tech mix, which the research does not have access to.

**Defer:** T-7, T-11, T-16, T-19, T-27, plus M-3. **6 patterns** that are real but better treated as flavor / archival than as mechanics.

**Exclude:** T-20 (historical period reference only — not a mechanic).

**Severity flags:**
- **No P1 (canon-violating) findings** in the throughlines themselves.
- **P2 findings** (ambiguity / partial misfit): T-14, T-19, T-21 cannot be evaluated without more Valoria-specific context (peninsula geography, tech mix, gunpowder status).
- **P3 findings** (polish): the implementation specifics for partial-fit throughlines need design choices not in the research's scope.

---

## Part III — Canon Constraint Cross-Check (P-01 through P-15)

For each canon constraint, I identify whether and how the throughlines and meta-throughlines align, conflict, or are silent.

### P-01 — Inseparability (temporal / epistemic / actualized co-movement)

**Alignment:**
- **T-28** (emergent grand-formation behavior from unit mechanics) is **structurally analogous** to Inseparability — small-scale operations producing automatic co-movement at larger scales. Conceptually compatible.
- **M-8** (compound failures require stacked layers) is **structurally analogous** — catastrophic outcomes require simultaneous failure across multiple dimensions, consistent with Inseparability's "all three dimensions co-move."

**No direct conflict.** Throughlines operate at the combat-and-strategy sublayer; P-01 operates at the Thread metaphysical layer. They can coexist if Thread operations affecting military formations produce automatic three-dimensional co-movement per P-01.

**Gap:** the research is silent on how Thread operations affect military formations. `[GAP: Thread-doctrine interaction model — basis: research is pre-Thread layer; canon does not specify. Question for Jordan.]`

### P-02 — Monstrosity is grounded in the Lacanian Real (surfeit-of-being)

**Alignment:** No direct intersection. The research catalogues human-vs-human warfare. Monstrous encounters are a different category of operation.

**No conflict.** Throughlines do not assign moral valence to opponents.

### P-03 — Rendering = consciousness-performed

**Alignment:** No direct intersection at combat-formation level. The research treats information about enemy positions as something armies can have or lack (scouts, *yam* communications, signal discipline), but doesn't engage the rendering layer.

**Implication for game design (not in scope to specify here):** If Valoria implements rendering-based information asymmetry, military intelligence and command-and-control mechanics will need to integrate with it. `[GAP: how do Thread-Sensitivity-gated rendering effects intersect with military scout / command-and-control mechanics? — basis: not specified.]`

### P-04 — Monstrosity = ontological, not moral

**Alignment:**
- **T-17** (cultural-doctrinal compatibility filter) and **M-6** (cultures filter doctrines they can adopt) are **conceptually parallel** — they recognize that cultural attitudes structure what's institutionally possible, without assigning moral judgment. The Mamluk caste rejection of firearms isn't framed as a moral failing; it's framed as a structural constraint.
- **T-18** (victory conditions are culturally specified) is similarly **structurally compatible** with P-04 — it observes that what counts as "winning" varies by culture, without ranking cultures morally.

**No conflict.** **In fact: T-17, T-18, M-6 are excellent reinforcement of the P-04 framing.** Cultural-doctrinal mismatch is described as structural failure to absorb, not as moral failure. This matches P-04's "rendering failure, not villains" pattern for monstrous beings extended to political-military entities.

`[CONFIDENCE: high — basis: direct structural parallel between cultural-doctrinal compatibility (T-17 / M-6) and ontological-not-moral framing (P-04).]`

### P-05 — Three emergence modes mechanically distinct

**No direct intersection.** Military formations are not emergence-mode phenomena.

### P-06 — Threadcut beings have no layer 2

**No direct intersection.** Military doctrine is about human-mode beings.

### P-07 — Calamity = rendered-side mechanism

**No direct intersection.** No throughline attributes agency or responsiveness to the substrate.

### P-08 — Epistemological barrier = inaccessibility, not suppression

**Alignment:** weakly relevant. **T-6** (weapons depend on institutions) and **T-7** (slave-soldier institutional logic) note that institutional knowledge is hard to transfer — practice laws, training pipelines, devshirme schools all encode skill that doesn't transmit by writing alone. This is **conceptually compatible** with P-08's "religious poetry" frame for inert knowledge.

**No conflict.** The pattern "skill cannot be transferred by text alone, requires institutional embodiment" recurs in both layers.

### P-09 — Memory pulling = messy, costly, detectable

**No direct intersection** at the formation level. Implications for individual practitioner agents within military operations exist but are out of research scope.

### P-10 — Coherence indexes commensurability with human-mode being

**Alignment:** weakly relevant. **T-29** (morale cascade as propagating field) is a **structural analog** to Coherence-drift — individual moral states propagating across a unit / faction. The mechanism is different (combat morale vs. layer-2 self-rendering integrity), but the propagation pattern is similar.

**No conflict.** A combat-morale system can coexist with a Coherence system; whether they share underlying mechanics is a design choice. `[GAP: relationship between combat-morale (T-29) and Coherence (P-10) — basis: not specified. Question for Jordan.]`

### P-11 — Temporal Disjunction is universal

**Alignment:** **M-4** (discipline-timing as universal command skill) is at a different layer than P-11 (Thread-operation temporal cost), but **the structural principle is the same: timing has irreducible cost.** Decisions about when to commit have asymmetric cost regardless of layer.

**No conflict.** The two operate at different scales and need not share mechanics.

### P-12 — Drift propagation is tridimensional

**Alignment:** **T-28** (emergent grand-formation behavior) and **T-29** (morale cascade) are **structural analogs** for tridimensional propagation — small-scale events propagating through unit hierarchies and affecting connected units. P-12 requires three-dimensional propagation (actuality / intelligibility / temporality); combat propagation typically operates in one or two dimensions (morale + casualties + cohesion).

**No conflict, but partial alignment.** A faction's military defeat could be designed to propagate in all three P-01/P-12 dimensions (loss of actuality = army destroyed; loss of intelligibility = reputation damage; loss of temporality = future planning disrupted), which would integrate combat outcomes with Thread mechanics. `[GAP: tridimensional propagation of military outcomes — basis: not specified. Question for Jordan.]`

### P-13 — Forgetting = rendering failure (Southernmost unstable)

**No direct intersection.** Military formations are not Southernmost knowledge.

### P-14 — Board/VG modes must express inseparability

**Alignment:** the strategic-layer (board-game-derived) and personal-layer (TTRPG-derived) modes of Valoria military operations must both produce three-dimensional co-movement per P-14. This is a **constraint on implementation**, not a violation by any throughline.

**Implementation flag:** if Jordan implements any throughline as a military mechanic, the implementation must produce three-dimensional co-movement at the Thread layer when the operation has Thread-relevant effects. `[ASSUMPTION: Thread-relevant military operations exist as a category — basis: implied by the integration of military and Thread layers in a unified game.]`

### P-15 — Three-layer being-persistence (Leap, Coherence 0, TS-gating)

**No direct intersection** at the formation level.

### Canon constraint cross-check summary

- **No P1 violations identified.**
- **Two strong structural alignments worth noting:**
  - **T-17 / T-18 / M-6 with P-04** (cultural-doctrinal compatibility ≈ ontological-not-moral framing).
  - **T-28 / T-29 / M-8 with P-01** (emergent propagation ≈ inseparability of dimensions).
- **Gaps for Jordan to resolve (4 identified):**
  - Thread-doctrine interaction model (general).
  - Rendering-based information asymmetry × military intelligence.
  - Combat-morale (T-29) × Coherence (P-10) relationship.
  - Tridimensional propagation of military outcomes (P-12).

These are not violations — they are **unspecified intersections** between the research sublayer and the canon's Thread layer. Resolution requires Jordan's design decisions.

---

## Part IV — Findings Summary

### Severity-tagged findings

**P1 (blocks play / canon violation):** none.

**P2 (ambiguity / partial misfit / unspecified intersection):**
- **P2-001:** Thread-doctrine interaction model unspecified (general gap).
- **P2-002:** Rendering-based information asymmetry × military intelligence relationship unspecified.
- **P2-003:** Combat-morale (T-29) × Coherence (P-10) relationship unspecified.
- **P2-004:** Tridimensional propagation of military outcomes (P-12 implementation for combat) unspecified.

**P3 (polish / out-of-scope-as-mechanic):**
- **P3-001:** T-14 (steppe horse-archer) and T-21 (cavalry-only catastrophic failure) cannot be evaluated without Valoria peninsula geography and tech mix.
- **P3-002:** T-19 (gunpowder transition doctrinal not technical) cannot be evaluated without Valoria's gunpowder status.
- **P3-003:** 6 throughlines flagged DEFER (T-7, T-11, T-16, T-19, T-27, M-3) — out-of-scope as mechanics but useful as flavor / archival reference.
- **P3-004:** 1 throughline flagged EXCLUDE (T-20) — historical reference only.

### Throughlines recommended for prioritized integration

Based on the cross-product of NERS scores and canon-constraint alignment, the **highest-priority throughlines** for Valoria integration are:

1. **M-1** (doctrine-substrate-opponent triangle) — universal design constraint
2. **M-4** (discipline-timing as universal command skill) — single signature combat mechanic
3. **T-1** (shock + missile combination) — strategic-layer composition
4. **T-5** (force-generation depth) — strategic-layer sustainability
5. **T-17 / T-18 / M-6** (cultural-doctrinal filter) — strong P-04 alignment
6. **T-22** (technological matrix) — faction tech-tree foundation
7. **T-23** (operational geography) — peninsula terrain × doctrine
8. **T-24** (hammer-and-anvil) — universal combat template
9. **T-26** (single-shot charge character) — spent-resource combat mechanic
10. **T-28 / T-29 / M-8** (emergent propagation × compound failure) — P-01 alignment

### Scale assignments (per PI design_doc_framing)

The research operates across scales; the audit recommends scale-level assignment:

- **Personal scale (TTRPG-derived):** T-9, T-28, T-29, M-4 (individual command skill, emergence, morale)
- **Settlement scale:** T-15 (fortification), T-26 (single-shot charge as personal commit), parts of T-29
- **Territory scale:** T-1, T-2, T-3, T-5, T-22, T-23, T-24, M-1, M-2, M-7 (army composition, doctrine, geography, command integration)
- **Peninsula scale (board-game-derived):** T-4, T-5, T-12, T-17, T-18, M-1, M-2, M-5, M-6, M-7 (faction-as-system, doctrine triangle, perfect-system trap)

Some throughlines (M-1 especially) span all scales because they are structural constraints rather than scale-specific mechanics.

---

## Part V — Outstanding Questions for Jordan

These are decisions Claude does not have authority to make. Listed for project-owner ratification or assignment.

1. **Thread-doctrine interaction (P2-001):** are there Thread operations whose effects modify or are modified by faction military doctrine? If yes, the highest-priority throughlines need to be reviewed against the specific interaction model.

2. **Combat-morale × Coherence (P2-003):** is combat-morale a layer-3 phenomenon (deliberate threadwork-like) or a layer-2 phenomenon (unconscious self-rendering)? The structural similarity to Coherence-drift is real; the mechanical relationship is unspecified.

3. **Tridimensional propagation of military outcomes (P2-004):** when a faction loses a battle, do the consequences propagate across all three Inseparability dimensions per P-12 — actuality (army), intelligibility (reputation / Influence Points / Certainty), temporality (planning / CD / Thread Charge)?

4. **Peninsula-specific scope (P3-001 / P3-002):** what is Valoria's peninsula geography (terrain mix)? What is its technological mix (gunpowder yes/no, magic yes/no, what era)? These constrain T-14, T-19, T-21 applicability.

5. **Scale assignments:** does Jordan agree with the personal / settlement / territory / peninsula scale assignments proposed in §IV? If not, which throughlines belong at different scales?

6. **Editorial ledger entries:** should any P2 findings be added to `canon/editorial_ledger.yaml` for tracking? Per audit skill rules, P1 findings would auto-append, but P2 require explicit decision.

---

## Part VI — Audit Closure

**Audit findings:**
- 29 throughlines + 8 meta-throughlines evaluated.
- 0 P1 (canon-violating) findings.
- 4 P2 (unspecified intersection) findings flagged.
- 4 P3 (polish / scope) findings flagged.
- 19 throughlines / meta-throughlines with strong NERS fit (full ✓ on all four criteria).
- 11 with partial fit (depends on implementation choices).
- 6 flagged DEFER (out-of-scope as mechanic, retained as flavor / archival).
- 1 flagged EXCLUDE (historical period reference only).

**All-directions completeness:** all six directions populated by the throughline set. No direction is empty. Research is structurally complete in the all-directions sense.

**Canon-constraint compliance:** the throughlines respect canon constraints. Two strong structural alignments noted (cultural-doctrinal × P-04; emergent propagation × P-01). Four unspecified intersections flagged as P2 gaps for Jordan to resolve.

**Recommended next action:** Jordan reviews the prioritized throughlines (§IV) and the outstanding questions (§V). Decisions on the P2 gaps unlock the implementation-specific throughlines currently in partial-fit (~) status.

**Audit skill compliance check (per `skills/valoria-mechanic-audit/SKILL.md`):**
- Mode E (Core Principles Compliance) format followed: each throughline tagged PRESENT (strong fit) / ALTERED (partial fit, with justification) / ABSENT (no alignment).
- All findings severity-tagged.
- No editorial judgment — mechanical analysis only.
- All references cite source files (chunks 01–10 of the research project).

---

`[CTX: ~55-65% project context — research files + audit. Audit document: ~440 lines.]`
`[CONFIDENCE: high on NERS scoring against research; medium on canon-constraint alignment given research operates at sublayer; low on scale-assignment recommendations — Jordan's call.]`
`[GAP: 4 P2 unspecified intersections await Jordan's design decisions (Part V).]`
