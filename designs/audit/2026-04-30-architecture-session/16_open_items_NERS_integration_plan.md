<!-- [PROVISIONAL: 2026-05-01 — open-items NERS evaluation + integration plan for the 2026-04-30 architecture session] -->
<!-- STATUS: PROVISIONAL — analysis artifact, not canon -->
<!-- AUTHORITY: derived from artifacts 00–15 of designs/audit/2026-04-30-architecture-session/; reads canon/02_canon_constraints.md, references/canonical_sources.yaml, references/throughlines_meta.md -->

# Open Items — NERS All Directions + Integration Plan

**Subject:** All provisional/open items emerging from the 2026-04-30 architecture session (PP-684 / PP-685 / PP-686 / PP-687 / PP-688). Evaluated NERS all directions. Integration plan that resolves dependencies and identifies the remaining Jordan-decisions.

**Date:** 2026-05-01
**Inputs:** artifacts 00–15 of `designs/audit/2026-04-30-architecture-session/`; sim outputs; canon/editorial_ledger_summary.yaml; references/canonical_sources.yaml; canon/02_canon_constraints.md; references/throughlines_meta.md.
**Status:** PROVISIONAL — recommends commit-set + decision-batch; awaits Jordan ratification.

---

## §0 Executive Summary

The architecture session produced five proposals (PP-684 / PP-685 / PP-686 / PP-687 / PP-688) and ~75 distinct provisional or open items. This document evaluates them as a *system* — not item-by-item, but by what each item touches and how items couple across the architecture.

**Three findings drive the integration plan:**

1. **Dependency direction is fixed.** PP-687 substrate ratifies first; PP-684 taxonomy authors in parallel; PP-686 spec is *consumed* by PP-687 (so PP-686 spec-revision and PP-687 spec-finalization are entangled, not sequential); PP-688 articulation reads all three. PP-685 migration is mechanical bookkeeping that follows ratification.

2. **Most "open items" are spec-completeness fills, not architectural decisions.** Of ~75 items, only ~12 are decisions Jordan needs to make. The rest are paragraphs to add. The integration plan separates the two cleanly.

3. **The four NERS directions PP-686 audited as WEAK (lateral S/R, diagonal S, horizontal R) all become STRONG once PP-687 is in place.** This is sim-validated. The integration plan therefore ratifies the substrate first because doing so removes most of PP-686's audit findings *as a side effect*.

**Aggregate NERS verdict on the open-items set, all six directions:**

| Direction | N | R | S | E |
|---|---|---|---|---|
| Top-down | STRONG | STRONG-conditional-on-Phase-5a-UI | STRONG | STRONG |
| Bottom-up | STRONG | STRONG (post-spec-fills) | MODERATE | STRONG |
| Vertical | STRONG | STRONG | STRONG | STRONG |
| Diagonal | STRONG | STRONG | STRONG | STRONG |
| Lateral | STRONG | STRONG | STRONG | MODERATE (vocabulary debt) |
| Horizontal | STRONG | MODERATE-pre-determinism / STRONG-post | MODERATE | MODERATE (pacing unmodeled) |

**No direction is WEAK. Three MODERATE cells reflect (a) bottom-up smoothness pending Memory-query-API / sub-step-ordering specs, (b) lateral elegance pending vocabulary-debt sweep, (c) horizontal robustness/smoothness/elegance pending determinism enumeration and pacing layer.** All three have clear addressing paths in the integration plan.

**The integration plan, in one paragraph:** Land six commits in sequence — (1) PP-687 spec finalization + ratification with the 6 sim refinements baked in, (2) PP-684 taxonomy ratification with Honor-decision resolved, (3) PP-686 spec v2 consuming PP-687 + applying C1–C10, (4) PP-685 migration roster, (5) PP-688 articulation layer formal, (6) all five PPs entered to `canon/patch_register_active.yaml` with PP-674 vetting blocks. Then run a Stage 10 lateral simulation chain that the week's NERS audit flagged as missing. Then begin Phase 5a Godot scope using PP-687 Keys as the event substrate.

---

## §1 Item Inventory by Group

Each group lists its open items with provenance. *Resolved-by-sim* items are noted as such; *spec-fill* vs *Jordan-decision* tags are explicit.

### §1.1 PP-684 — Conviction Taxonomy Revision

| # | Item | Type | Status |
|---|---|---|---|
| 684-1 | 12-Conviction set: Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue | spec | confirmed in conversation; not yet committed to canon |
| 684-2 | Honor as 13th Conviction | Jordan-decision | provisional; affects PP-686 §3.3 role templates if Honor folds into Identity or Virtue |
| 684-3 | Greed explicitly **not** a Conviction; represented via Self-Other orientation axis | spec | conversation-confirmed; needs canonical statement |
| 684-4 | Self-Other orientation as new dimension on actors | spec | sim-validated (sim v2 §1.8); formula `attributed = raw × (1 − 0.5 × max(0, orient))` provisional |
| 684-5 | Cultural background templates as separate authoring layer | spec | sim v2 confirmed; templates not yet enumerated |
| 684-6 | Structured-concentration NPCs (primary 1-3 with 0.6-0.8 weight + cultural background 0.2-0.4 weight) | spec | sim v2 confirmed |
| 684-7 | 4-axis vectorization (hierarchical, sacred, instrumental, traditional) | spec / decision | PP-687 audit P2-1 flagged 4-axis as load-bearing simplification; possible Community vs Identity collapse |
| 684-8 | Conviction → axis matrix (12 × 4 = 48 entries) | spec | PP-687 §3.4 illustrative; calibration deferred |

### §1.2 PP-685 — Conviction Migration Roster

| # | Item | Type | Status |
|---|---|---|---|
| 685-1 | Roster: Reason-tagged characters → new taxonomy | spec (mechanical) | not yet authored |
| 685-2 | Roster: Continuity-tagged characters → new taxonomy | spec (mechanical) | not yet authored |
| 685-3 | Edge cases: characters whose old Convictions don't map cleanly | Jordan-decision (per character) | depends on 685-1, 685-2 |

### §1.3 PP-686 — Faction Behavior Architecture

#### §1.3.1 §6 Open Questions

| # | Item | Type | Status |
|---|---|---|---|
| 686-OQ1 | PP-684 dependency confirmation (10-12 Convictions) | Jordan-decision | resolved by 684-1 ratification |
| 686-OQ2 | Honor as 12th Conviction | Jordan-decision | duplicates 684-2 |
| 686-OQ3 | α calibration (α_base=0.4, α_seniority range, α_institution range) | Jordan-decision | placeholders OK as starting point |
| 686-OQ4 | Public temperament typology (5 temperaments) | Jordan-decision | typology proposed; territory assignment ~30-50 entries |
| 686-OQ5 | Strictness function form (`0.5L − 0.3PS + base`) | Jordan-decision | sim-validated; calibration at Stage 10 |
| 686-OQ6 | Mandate retention vs replacement | Jordan-decision | proposal recommends transitional retention |
| 686-OQ7 | α_temperament + β_temperament = 1 constraint | Jordan-decision | proposal default; alternative is independent scalars |
| 686-OQ8 | Mission shift triggers (enumerate) | Jordan-decision | currently vague — "major state change" |

#### §1.3.2 Audit P1 (block ratification)

| # | Item | Type | Status |
|---|---|---|---|
| 686-P1-1 | Organizational hierarchy / supervisor graph schema | spec | requires §3.2.1 paragraph |
| 686-P1-2 | Aggregate effective_convictions function | spec | sim-resolved: Standing-weighted normalized sum (= C9) |
| 686-P1-3 | DA category schema for Mission alignment | spec | **resolved by PP-687 da_outcome subtypes** |

#### §1.3.3 Audit P2 (block sim verification, not ratification)

| # | Item | Type | Status |
|---|---|---|---|
| 686-P2-1 | NPC behavior coupling: effective vs personal Convictions | spec | **resolved by PP-687 §6.1** (both armatures coexist; context flag chooses) |
| 686-P2-2 | Cascade-per-territory vs cascade-per-faction | Jordan-decision | requires §3.2.2 multi-root cascade allowance OR explicit single-root constraint |
| 686-P2-3 | Strain interaction | spec | **resolved by PP-687 env.peninsular_strain_shock** |
| 686-P2-4 | Edge cases (orphan NPC, zero-vector leader, etc.) | spec | sim-confirmed orphan defect; rule drafted (= C6) |
| 686-P2-5 | Mid-season leader change handling | spec | requires explicit ordering specification |

#### §1.3.4 Sim Calibration Set C1–C10

| # | Item | Type | Status |
|---|---|---|---|
| C1 | Cap Ob_modifier at ±2 (was ±3) | calibration | sim-confirmed effective |
| C2 | Drop strictness reward path | calibration | sim-confirmed redundant (saturates against cap) |
| C3 | drift_coef = 0.55-0.65 (was 0.45) | calibration | needs one more sim run |
| C4 | Crisis-bypass rule: leader.scars ≥ 3 → cascade damping suspended | calibration | sim-required for dramatic visibility |
| C5 | β-fidelity gating during negative outcomes (×0.5) | calibration | sim-confirmed effective |
| C6 | Orphan NPC rule: α=1.0 | calibration | sim-confirmed effective |
| C7 | Self-Other formula `attributed = raw × (1 − 0.5 × max(0, orient))` | calibration | sim-validated provisionally |
| C8 | NPC personal_convictions = primary + cultural background | architecture | sim v2 confirmed |
| C9 | Aggregate as Standing-weighted normalized sum | architecture | sim v1+v2 confirmed |
| C10 | Cultural background templates as separate authoring layer | architecture | sim v2 introduced |

### §1.4 PP-687 — Universal Key Substrate

#### §1.4.1 §9 Open Questions

| # | Item | Type | Status |
|---|---|---|---|
| 687-OQ1 | Schema sign-off (11 universal Key fields) | Jordan-decision | load-bearing; review checkpoint |
| 687-OQ2 | Type registry initial scope (~25-30 types; missing categories?) | Jordan-decision | candidates: economy, sub-DA religious observances, rumor propagation |
| 687-OQ3 | Conviction → axis matrix authoring (12 × 4 = 48 entries; 4 axes correct count?) | Jordan-decision | duplicates 684-7 + 684-8 |
| 687-OQ4 | Visibility list authoring burden | Jordan-decision | derived-from-scene-presence vs explicitly authored |
| 687-OQ5 | Memory salience formula | Jordan-decision | dot-product form provisional |
| 687-OQ6 | Causal graph storage / pruning policy beyond `transient` | Jordan-decision | sim showed sparse graph; old-Key compression optional |
| 687-OQ7 | Phased rollout vs hard cutover | Jordan-decision | proposal recommends phased; hard cutover faster but riskier |
| 687-OQ8 | Naming: "Key" vs alternatives (Event, Record, Atom, Signal, Trace) | Jordan-decision | nomenclature only |
| 687-OQ9 | PP-686 sequencing relationship | Jordan-decision | proposal recommends PP-687 first |
| 687-OQ10 | Stage 10 verification scope (property-test battery) | spec | enumeration: cycle-freeness, salience monotonicity, visibility correctness, replay determinism |

#### §1.4.2 Audit P1

| # | Item | Type | Status |
|---|---|---|---|
| 687-P1-1 | Performance scaling | spec | **sim RESOLVED**: 18,724 keys/sec; sub-ms walks |
| 687-P1-2 | Determinism guarantees enumeration | spec | sim partially resolved; production engine needs RNG/ordering/FP rules |

#### §1.4.3 Audit P2 + Sim Refinements

| # | Item | Type | Status |
|---|---|---|---|
| 687-P2-1 | 4-axis Conviction matrix tradeoff documentation | spec | needs caveat note (= 687-OQ3 / 684-7) |
| 687-P2-2 | Bootstrap rule for partial-migration state | spec | requires §7.3.x sub-clause |
| 687-P2-3 | Cycle handling in causes graph | spec | **sim RESOLVED**: validator |
| 687-P2-4 | Memory query API specification | spec | **sim PROMOTED**: ~1000 entries/NPC at 30 seasons; indexing required |
| 687-P2-5 | Sub-step ordering tiebreak | spec | requires explicit rule (stable sort by emission order) |

#### §1.4.4 Sim §4 Spec Refinements

| # | Item | Type | Status |
|---|---|---|---|
| 687-SIM-1 | §5.3.x Memory query API with axis-relevance + time-window + target-mention indexing | spec | derived from sim |
| 687-SIM-2 | §5.5 sparse CAUSAL_GRAPH note (~85% of Keys have no causes) | spec | implementation hint |
| 687-SIM-3 | §5.6 determinism enumeration (RNG seeded per emission; sub-step deterministic; FP reproducibility) | spec | derived from sim |
| 687-SIM-4 | §5.1 step 5 subscription callback constraint (O(1) or async) | spec | derived from sim |
| 687-SIM-5 | §3.4 axis-count caveat | spec | duplicates 687-P2-1 |
| 687-SIM-6 | §7.3.x partial-migration bootstrap rule | spec | duplicates 687-P2-2 |

### §1.5 PP-688 — Articulation Layer

| # | Item | Type | Status |
|---|---|---|---|
| 688-1 | Tier 1 protagonist UI lens (default UI filters by player's observer set, Memory, Disposition) | spec | Phase 5a Godot scope |
| 688-2 | Tier 2 trigger ruleset (~15-25 trigger types + cut scene composition templates) | spec | needs authoring |
| 688-3 | Tier 3 chronicle generator (significance + causal centrality + omniscient prose templates) | spec | needs authoring |
| 688-4 | Significance function (universal track + protagonist track; 4 sub-factors per track) | spec | formulas drafted in artifact 13 |
| 688-5 | Knot/Belief/Inspiration integration into significance | spec | refined in artifact 14; reads canonical mechanics |
| 688-6 | New Key types: meta.knot_formed, meta.knot_ruptured, state.belief_revised | spec | Class B extensions to PP-687 type registry |
| 688-7 | Scene-event payload extensions: belief_engagement_for, inspirations_engaged_for, knot_partners_present | spec | per-type registry additions |
| 688-8 | Cumulative narrative weight tracking on actors | spec | small actor-schema addition |
| 688-9 | Awareness post-emission update (subsequent Keys grow original Key's awareness) | spec | Key emission rule extension |
| 688-10 | Player-triggered chronicle review (mid-year retrospective on demand) | spec | Phase 5a UI; optional |
| 688-11 | Cut scene rendering (Phase 5a Godot work, ~1-2 sessions added) | spec | Godot scope |
| 688-12 | Pacing system (deferred; future PP candidate) | deferred | out of PP-688 scope |

---

## §2 NERS Evaluation — All Directions, All Groups

NERS = Necessary, Robust, Smooth, Elegant. Six directions per project Specific Definitions.

This section evaluates the open-items set as a coupled system. For each direction, the evaluation considers what changes if all spec-fills land *and* a coherent set of Jordan-decisions resolves.

### §2.1 TOP-DOWN — does the open-items set serve the videogame's player experience?

#### N (necessary)

**STRONG.** Every open item, evaluated against the project intent (positive feedback loop between player decisions and mechanics that produces an engaging Godot videogame world with emergent narratives), serves directly:

- Substrate items (PP-687) make events legible to the player and to other systems.
- Faction-architecture items (PP-686) produce the strategic-layer dynamics that drive multi-season play.
- Taxonomy items (PP-684) give NPCs distinguishable interpretive interiors.
- Articulation items (PP-688) convert substrate richness into legible narrative.
- Migration item (PP-685) unblocks the canonical character roster from anachronistic vocabulary.

**Necessity check by leverage:** are any items overbuilt? Three candidates:
1. *PP-687's full ~25-30 type registry up front* — could be staged. Mitigation: Phase A (substrate + 5-10 essential types) then Phase B per consumer system. Already in PP-687 §7.3.
2. *PP-686's non-monotonic strictness function* — mathematically sound but requires Stage 10 calibration. Risk that calibration produces a simpler form. Mitigation: ratify with provisional form, calibrate.
3. *PP-688's Tier 2 trigger ruleset of 15-25 types up front* — could start with 5-7 most consequential triggers (Knot rupture, Belief revision, succession, exposed betrayal, Strain shock) and grow.

None are unnecessary; some are scopable. The integration plan §3 reflects this scoping.

#### R (robust)

**STRONG-conditional-on-Phase-5a-UI.** Robustness sub-criteria, applied to the *integrated* item set:

- **Player strategic depth:** every player choice composes through Keys; consequences walkable; Knot/Belief/Inspiration commitments register canonically. ✓
- **Customization:** scenarios as Key sequences; structured-concentration NPCs distinguishable; faction Mission authorable. ✓
- **Variety in approach:** the substrate is *generative*; emergent arcs in three categories (personal, faction, cross-scale). ✓
- **Player feels important:** scene-completion principle (artifact 14 §1) guarantees every played scene is in the player's throughline. ✓
- **Player feels they impact world:** CAUSAL_GRAPH walks make the player's contribution to downstream events visible. ✓
- **Emergent narrative without player:** NPCs autonomously emit Keys per their Procedures; Cascade re-resolves regardless. ✓
- **Mechanics fully formed:** **PARTIAL until Phase 5a UI lands.** The architecture is structurally complete but the Phase 5a diagnostic UI (faction dashboard, Memory viewer, CAUSAL_GRAPH walker, arc-resolution notifications) is *required* for the player to perceive the architecture's richness. Without UI, robustness is engine-internal, not player-facing.

**The conditional matters.** A player without the diagnostic UI experiences Tier 1 mud + Tier 2 cut scenes + Tier 3 chronicle, but cannot interrogate state or walk causes. Phase 5a is the gating dependency.

#### S (smooth)

**STRONG.** The integrated set is smoother than any subset because PP-687 makes all cross-system coupling automatic:

- Single substrate replaces N×N pair-couplings (lateral S resolved).
- CAUSAL_GRAPH replaces bespoke event-tracing (diagonal S resolved).
- Conviction → axis matrix unifies personal-scale and faction-scale interpretive math (vertical S smoothed).
- Knot/Belief/Inspiration mechanics already exist; significance function reads from them rather than reinventing (artifact 14 caught this; correction is in).
- Multi-tier articulation (Tier 1 mud → Tier 2 punctuation → Tier 3 chronicle) matches lived experience and Renaissance documentary practice.

The remaining smoothness gap is bottom-up: PP-687 sub-step ordering, Memory query API, and determinism enumeration need explicit specs. All three are paragraphs to add, not architectural changes. They are §10.1 immediate items per artifact 08.

#### E (elegant)

**STRONG.** Elegance criteria applied to the integrated set:

- *Logically simple:* one substrate (Keys), one Conviction taxonomy, one armature interpretation function, one significance function, three articulation tiers. Each layer has one canonical form. ✓
- *Clear approach:* every system emits Keys, consumes Keys; same applies to factions, scenes, environment. No exceptions. ✓
- *No unnecessary overhead:* substrate replaces multiple bespoke event channels; significance function reads from existing canonical mechanics rather than reinventing.
- *Easy to understand:* chronicle metaphor (substrate as event log; chronicler as narrator) is period-correct and immediately graspable.
- *Player intuits complex outcomes from simple choices:* validated by sim and worked examples (Almud third year; Bill Clinton vs neighborhood affair).

**Verdict (top-down):** N=STRONG, R=STRONG-conditional, S=STRONG, E=STRONG.

### §2.2 BOTTOM-UP — do individual open items ladder up to architectural coherence?

#### N

**STRONG.** Each open item has explicit purpose:
- 684-1..684-8: each Conviction or matrix entry has a substrate role (armature interpretation, Mission alignment, Public Expectation profiling).
- 686-P1, 686-P2, C1–C10: each closes a specific spec gap or calibrates a specific parameter.
- 687-OQ, 687-P, 687-SIM: each addresses a specific schema, guarantee, or implementation concern.
- 688-1..688-10: each implements a specific narrative-articulation feature.

No item is decorative.

#### R

**STRONG (post-spec-fills).** Sub-criteria:

- **Components have explicit inputs/outputs/derivation:** mostly yes; gaps are exactly the spec-fill items (Memory query API, determinism enumeration, sub-step ordering, supervisor graph schema). All have proposed forms.
- **Components compose cleanly:** sim verified PP-687 cycle detection, performance, observer resolution, and PP-686 integration all compose without surprises.
- **Edge cases:** orphan NPC and zero-vector leader sim-validated; remaining edge cases (cycle in causes graph, Cascade-per-territory question, mid-season leader change) have proposed fixes.
- **Numerical bounds:** all clamps in place (L/PS [0,7], strictness [0,1], salience [0,3], Ob ±2, significance [0,1] across two tracks).

#### S

**MODERATE.** The smoothness gap is concentrated in PP-687 horizontal sub-step concerns:

- **Sub-step ordering tiebreak** (687-P2-5) is the load-bearing missing rule. Two Keys firing same sub-step need a stable-sort tiebreak. Proposed: by emission order. Unspecified.
- **Determinism enumeration** (687-SIM-3 / 687-P1-2) lists three sources — RNG, ordering, FP — but doesn't specify *how* each is controlled at engine level.
- **Memory query API** (687-SIM-1 / 687-P2-4) is sim-flagged as needing indexing; production design left for Stage 10.

These are spec-completeness, not architectural. Once §10.1 items in PP-687 audit land, S goes to STRONG.

#### E

**STRONG.** Component-level elegance:
- Each open item is a single fact, formula, or rule. No item requires conceptual contortion.
- Significance function is ~50 lines of code. Articulation tiers are ~15-25 trigger templates plus chronicle generator. These are small surface areas.
- The Knot/Belief/Inspiration integration (artifact 14) replaces generic substrate measures with *authored* significance signals — read from existing canon, not invented.

**Verdict (bottom-up):** N=STRONG, R=STRONG-post-fills, S=MODERATE, E=STRONG.

### §2.3 VERTICAL — scale-axis coherence (personal ↔ settlement ↔ territory ↔ peninsula)

#### N

**STRONG.** The integrated set explicitly addresses every scale boundary:

- Personal-scale: 12-Conviction taxonomy + Self-Other axis + cultural background + structured concentration. Per-NPC armature.
- Personal→faction: PP-686 Cascade math (`α × personal + (1-α) × supervisor`); PP-687 state.scar_acquired (leader) → mechanical.cascade_resolution.
- Settlement-scale: settlement signal aggregates as Key types; territorial public-temperament weighted-average for faction Popular Support.
- Territory→peninsula: PP-687 multi-element scale_signature; env.peninsular_strain_shock.
- Cross-scale provenance: `scale_signature[]` + CAUSAL_GRAPH walks.

#### R

**STRONG.** Sim §1.3 walked a 4-step diagonal chain (scene insult → DA betrayal → succession → peninsular strain shock) successfully. Each scale's events propagate through the substrate.

The PP-666 trio (settlement adjacency ED-710, fractional province ownership ED-711, faction succession split) remains an open dependency from week-audit §3.1. PP-686 has a soft dependency: Mission territory targeting needs settlement composition, which PP-666 trio provides. **PP-666 trio is *not* in this integration plan** but is referenced as a Phase 1 carryforward.

#### S

**STRONG.** Multi-element `scale_signature` is one field doing the work of N×N pair-couplings. The 16-Accounting trace (per the architecture session §6.7 + sim §1.3) becomes a forward walk of CAUSAL_GRAPH from a scene-scale Key to peninsula-scale consequences.

The single load-bearing unresolved item is **686-P2-2 cascade-per-territory vs cascade-per-faction**. A faction may have parallel hierarchies (Crown's secular + military + household) producing locally-distinct cascades. Proposal recommendation: multi-root cascade allowance with explicit per-cascade-root accounting. Decision needed.

#### E

**STRONG.** The chronicle metaphor + Conviction → axis matrix gives the player a single mental model that operates at every scale: events have meaning, observers interpret, consequences cascade. Same model for personal scene events and peninsula-wide treaties.

**Verdict (vertical):** N=STRONG, R=STRONG, S=STRONG (post 686-P2-2 decision), E=STRONG.

### §2.4 DIAGONAL — cross-scale + cross-system interactions

This was PP-686 audit's WEAK direction; PP-687 transforms it.

#### N

**STRONG.** The richest arcs are diagonal. The integrated set delivers:
- `causes[]` graph + CAUSAL_GRAPH for explicit provenance walking.
- Multi-scale Keys for events that operate at multiple scales simultaneously.
- Symbolic dimensions on every Key for cross-system meaning preservation.
- Significance function that scores diagonal chains by causal centrality (artifact 13 §7).

Sim §1.3 walked a canonical Renaissance arc (insult → betrayal → succession → strain) end-to-end.

#### R

**STRONG.** Diagonal chains walkable forward and backward. Sim showed sparse causal graph (~15% of Keys have causes); this is realistic — most Keys are independent emissions. The architecture supports longer chains; typical use won't stress them.

The only diagonal-direction risk is **causes-population rate** (artifact 10 §10.1). If production stays at ~15%, diagonal arcs are short. Mitigation: PP-687 §3.x authoring guideline requiring causes[] population whenever a Key is emitted *because of* prior Keys. This is a paragraph in PP-687 spec.

#### S

**STRONG.** Diagonal coupling is automatic substrate behavior, not per-pair wiring. Adding a new system requires only Key emission/consumption.

#### E

**STRONG.** The chronicle metaphor maps cleanly: a Renaissance chronicle reads as causal chains across scales and systems. Players grasp this immediately.

**Verdict (diagonal):** all four NERS axes STRONG.

### §2.5 LATERAL — peer systems at the same scale

This was PP-686 audit's WEAKEST direction (4 peer-system specs missing). PP-687 transforms it.

#### N

**STRONG.** Peer systems at every scale gain canonical coupling:
- Personal scale: scene-event Keys + Conviction Scar Keys + Memory Keys + Disposition shifts via standard rule.
- Faction scale: Cascade + Mission + Public Expectation + L/PS all read same Key streams.
- Multi-faction: cross-faction Disposition shifts read from observed Mission alignment / contradiction.
- Cross-system at scale: scene_slate + social_contest + mass_battle + peninsular_strain all Key-mediated.

#### R

**STRONG.** N×N pair-couplings collapse to N substrate-couplings. Each system independent in its emission/consumption pattern. TYPE_SUBSCRIPTIONS lets multiple consumers respond to the same Key without coordination.

Stage 10 lateral simulation chain (week-audit §5.2 #5; PP-686 audit §9.2 #5) remains needed: faction-layer × mass_battle × social_contest at scene scale, plus Strain interaction. **This is the missing simulation pass that the integration plan §3.5 schedules.**

#### S

**STRONG.** Adding a new peer system: implement Key emission + Key consumption; no per-pair work.

#### E

**MODERATE.** Vocabulary debt remains. Standing (personal rank), Mandate (faction acceptance, derived), Legitimacy (component of Mandate), Popular Support (component of Mandate), Disposition (relational), Reputation (composite), and now: Cascade Fidelity, Strictness, Mission alignment, Self-Other orientation, awareness — *eleven* terms for related concepts at the personal-↔-faction interface.

This is PP-686 audit P3-3. Resolution is a glossary-unification pass *after* PP-686 + PP-687 + PP-688 ratify. Until then, the lateral elegance is structural-but-unconsolidated.

**Verdict (lateral):** N=STRONG, R=STRONG, S=STRONG, E=MODERATE (vocabulary debt).

### §2.6 HORIZONTAL — sequence/temporal (turn order, phase order, event chaining)

#### N

**STRONG.** Temporal aspects covered by the integrated set:
- Per-Accounting cascade re-resolution + L/PS drift (PP-686).
- Per-Key emission with `emitted_at: (season_index, sub_step_index)` ordering (PP-687).
- Mid-season vs season-boundary distinction via sub_step_index (PP-687).
- Year-end articulation timing (PP-688 Tier 3).
- Permanence enumeration: transient/persistent/indelible (PP-687 §3.2).
- Mission shift triggers (PP-686 §3.1; needs enumeration per 686-OQ8).

#### R

**MODERATE pre-determinism enumeration; STRONG post.** The current spec promises replay determinism but doesn't enumerate sources of non-determinism. Three are required:
1. RNG seeded per Key emission (not engine-globally).
2. Sub-step ordering tiebreak rule (stable sort by emission order).
3. Floating-point reproducibility level (specify x86_64 + IEEE-754 default rounding).

Also unaddressed:
- **Mid-season leader change handling** (686-P2-5). Spec doesn't say what happens if a leader changes mid-season — does Cascade re-resolve immediately or wait for season-end?
- **Multi-violation same-season ordering** (686 P3-4). Two violations same season: sum, max, or sequential?

These are spec-fills, not architectural changes. Post-fill: STRONG.

#### S

**MODERATE.** Smoothness questions:
- **Cascade re-resolution timing vs DA submission** — PP-686 spec says "each Accounting" but DAs fire mid-season. Resolution: state explicitly that Cascade is end-of-season-only; DAs within a season use the cascade resolved at the prior Accounting.
- **Multi-arc concurrency** (artifact 10 §7) — multiple arcs running simultaneously may overwhelm UI; pacing/prioritization needed.
- **Damping for L/PS oscillation** — sim showed PS pegs ceiling; β-fidelity gating (C5) addressed downside but ceiling-bounce remains. Calibration item.

#### E

**MODERATE.** Append-only log is temporally elegant. Sub-step indexing is one-line. *But:* narrative pacing is not built into the substrate (artifact 10 §7, artifact 11 §6). Players may experience flat stretches or simultaneous overload. The architecture is *temporally honest* but not *narratively paced*.

Pacing system is deferred to a future PP per artifact 10 §10.5 and artifact 11 §7.3 #8. Acceptable scope; not a current gap to fill but a known limitation.

**Verdict (horizontal):** N=STRONG, R=MODERATE-pre-fills / STRONG-post, S=MODERATE, E=MODERATE.

### §2.7 NERS Direction Summary Matrix (open-items set)

| Direction | N | R | S | E |
|---|---|---|---|---|
| Top-down | STRONG | STRONG-conditional-on-Phase-5a | STRONG | STRONG |
| Bottom-up | STRONG | STRONG-post-fills | MODERATE | STRONG |
| Vertical | STRONG | STRONG | STRONG (post 686-P2-2) | STRONG |
| Diagonal | STRONG | STRONG | STRONG | STRONG |
| Lateral | STRONG | STRONG (post Stage 10 sim) | STRONG | MODERATE (vocabulary debt) |
| Horizontal | STRONG | MODERATE-pre / STRONG-post | MODERATE | MODERATE (pacing unmodeled) |

**Aggregate count:** 17 STRONG, 5 STRONG-conditional, 4 MODERATE, 0 WEAK across 24 cells.

**Pattern:**
- The architecture is uniformly strong in necessity, vertically and diagonally clean, and laterally robust where it was previously weak.
- Three remaining MODERATE clusters: bottom-up smoothness (spec fills), lateral elegance (vocabulary debt), horizontal smoothness/elegance (pacing).
- All MODERATE cells have known addressing paths in the integration plan §3.

---

## §3 Integration Plan

The plan resolves dependencies, batches the work into six commits, and identifies the 12 Jordan-decisions that gate ratification.

### §3.1 Sequencing Constraints (mandatory)

| Constraint | Source | Implication |
|---|---|---|
| PP-687 ratifies before PP-686 implements | PP-687 §6.1, §9 #9 + PP-686 audit §9.3 #7 | PP-686 spec consumes PP-687 (DA category schema, NPC behavior coupling, Strain interaction); writing PP-686 first creates rewrite work |
| PP-684 ratifies before PP-686 implementation | PP-686 §4.1 + 686-OQ1 | PP-686 §3.3 role templates reference 12-Conviction taxonomy |
| PP-687 substrate is *consumed* by PP-688 | artifact 12 §0 + §4 | PP-688 reads Keys, emits new Key types, extends per-type registry |
| PP-686 spec-revision resolves PP-686 audit findings | sim evaluations + audit §10 | C1-C10 + spec-fills land in PP-686 v3 |
| PP-684/685 ratification unblocks PP-686 role-template authoring | PP-684 → PP-686 dependency | Honor decision (684-2) gates role template definition |

**These are not negotiable.** Reordering breaks downstream work.

### §3.2 The Six-Commit Plan

Each commit lands a self-contained piece. Commits 1-5 are spec-finalizations; commit 6 is the patch_register entry batch. All commits are PROVISIONAL until Jordan ratifies the underlying proposals.

#### Commit 1 — PP-687 spec finalization (substrate first)

**File:** `designs/architecture/key_substrate_v30.md` (new, Class A canon).
**Plus:** `designs/architecture/key_type_registry_v30.md` (new, Class A canon, ~25-30 types).
**Plus:** Conviction → axis matrix update embedded in key_substrate (or split if Jordan prefers).

**Spec-fills baked in:**
- §3.1 Universal Key fields (11 fields confirmed).
- §3.4 Conviction → axis matrix illustrative values + §3.4.x axis-count caveat (per 687-P2-1 / 687-SIM-5).
- §4 Key type registry initial scope (per 687-OQ2). Recommend 7 type families × 25-30 subtypes:
  - scene_event (5 subtypes)
  - da_outcome (5 subtypes — provides PP-686 P1-3 resolution)
  - mechanical_event (4 subtypes)
  - state_transition (4 subtypes; will extend with PP-688's 3 new types as Class B)
  - environmental (3 subtypes; provides PP-686 P2-3 resolution)
  - scene_outcome (3 subtypes)
  - system_meta (3 subtypes; PP-688 will extend)
- §5.1.1 Cycle detection in causes graph (per 687-P2-3, sim-validated).
- §5.3.1 Memory query API (per 687-P2-4 / 687-SIM-1) with required indexes: by axis-relevance, by time-window, by target-mention.
- §5.5 Sparse CAUSAL_GRAPH note (per 687-SIM-2).
- §5.6 Determinism enumeration (per 687-P1-2 / 687-SIM-3) listing the three required guarantees.
- §5.1 step 5 subscription callback constraint — O(1) or async (per 687-SIM-4).
- §5.x sub-step ordering tiebreak (per 687-P2-5) — stable sort by emission order.
- §3.x causes[] authoring guideline — when an emitter knows the cause, populate causes[].
- §7.3.x partial-migration bootstrap rule (per 687-P2-2 / 687-SIM-6) — legacy events wrapped in `meta.legacy_event` Keys; substrate tolerates non-Key event channels during Phase B.

**Jordan-decisions gating commit 1:**
- 687-OQ1 schema sign-off
- 687-OQ4 visibility list authoring (default-from-scene-presence vs explicit) — recommend default-from-scene with explicit override
- 687-OQ5 Memory salience formula — recommend dot-product form provisional, calibrate at Stage 10
- 687-OQ6 pruning policy — recommend transient-only initially, add compression policy after sim-validated
- 687-OQ7 phased rollout — recommend phased per §7.3
- 687-OQ8 naming — recommend "Key" stays
- 687-OQ10 Stage 10 verification scope — enumerated in §10.1 of audit

**Commit message:** `[infrastructure] PP-687 universal Key substrate spec finalization (PROVISIONAL)`

**Effort:** 1 session.

#### Commit 2 — PP-684 Conviction Taxonomy + Migration Roster

**Files:**
- `designs/personal/conviction_taxonomy_v30.md` (new, Class A canon) — 12 Convictions (or 13 with Honor) + Self-Other axis + 4-axis vectorization + cultural background template framework.
- `designs/personal/conviction_migration_roster_v30.md` (new, Class A canon, mechanical) — per-character mapping from old Reason/Continuity-tagged Convictions to new taxonomy (PP-685).
- Updates to `references/glossary.md` adding all new terms.
- Updates to `references/alias_registry.yaml` mapping old Conviction labels to new.

**Jordan-decisions gating commit 2:**
- **684-2 Honor as 13th Conviction.** Single most important taxonomy decision. Affects PP-686 §3.3 role templates. Recommendation: keep Honor as 13th since multiple role templates (sovereign, military-order) load-bear on it. Folding into Identity creates dual-meaning; folding into Virtue collapses sovereign vs military distinction.
- **684-7 4-axis vectorization (count and labels).** PP-687 audit P2-1 flagged Community vs Identity as collapsing. Two options: (a) accept the simplification and document; (b) add a 5th axis (communal-vs-categorical, or relational). Recommendation: (a) for now, calibrate at Stage 10, treat 5th axis as Class B extension if needed.
- **685-3 Edge-case migration.** Per-character; resolve during roster authoring.

**Commit message:** `[editorial] PP-684 Conviction taxonomy + PP-685 migration roster (PROVISIONAL)`

**Effort:** 1.5 sessions (taxonomy 1 session, roster 0.5).

#### Commit 3 — PP-686 v2 spec consuming PP-687

**File:** `designs/provincial/faction_behavior_v30.md` (new or update, Class A canon).

**v2 changes from v1 (PROVISIONAL proposal):**
- §3.1 Mission alignment categories now reference PP-687 da_outcome subtype enumeration (resolves 686-P1-3).
- §3.2 Cascade math updated to consume PP-687 Keys: `state.scar_acquired` (leader) triggers re-resolution; `mechanical.cascade_resolution` is self-emitted.
- §3.2.1 Organizational hierarchy / supervisor graph as authored faction state (resolves 686-P1-1). Schema: each NPC has optional `supervisor_id` field; leader has null; orphans default to α=1.0 per C6.
- §3.2.2 Cascade-per-territory allowance (resolves 686-P2-2 pending Jordan decision).
- §3.3.1 Aggregate effective_convictions = `normalize(Σ standing_i × effective_i)` (resolves 686-P1-2 = C9).
- §3.4 Public temperament typology (5 temperaments) with territory-level authoring. Faction's effective temperament weights = population-weighted average across territories.
- §3.4.1 Strain interaction: `env.peninsular_strain_shock` Keys consumed by faction's public-temperament dynamics; high Strain shifts effective temperament toward outcomes-only (resolves 686-P2-3).
- §3.5 Strictness function unchanged form, with C2 (drop reward path) applied — Ob calculation uses strictness only as deviation modulator, not reward path.
- §3.7 Ob_modifier capped at ±2 (C1).
- §3.8 Faction state schema includes Legitimacy + Popular Support fields; Mandate retained as derived (transitional per OQ6 default).
- §3.9 NPC behavior coupling Integration Notes (resolves 686-P2-1): NPCs read effective_convictions in faction-role context, personal_convictions in personal-time context; context flag from Key.payload (`role_acting: bool`) chooses.
- §3.10 Edge cases: orphan NPC rule (C6); zero-vector leader fallback (sim §1.7).
- §3.11 Mid-season leader change (resolves 686-P2-5): leader change emits succession Key at sub-step where succession occurs; cascade re-resolution emits at next Accounting; mid-season DAs use prior-Accounting cascade values.
- §3.x Crisis-bypass rule (C4): when leader.scars ≥ 3, cascade damping suspended; new leader Convictions propagate immediately each season until scars < 3.
- §3.x β-fidelity gating: if mission_outcome contribution is negative, β × cascade_fidelity contribution to ΔPS scaled by 0.5 (C5).
- §3.x drift_coef = 0.6 (C3 midpoint of 0.55-0.65 range; calibrate at Stage 10).
- §3.x Self-Other orientation modulator on outcome attribution: `attributed = raw × (1 − 0.5 × max(0, orient))` (C7).
- §3.x Structured-concentration NPCs reference (C8); cultural background templates linked from PP-684 (C10).

**Spec-fills landed:** every PP-686 P1, P2, and C1-C10 item.

**Remaining Jordan-decisions for commit 3:**
- 686-OQ3 α calibration values — recommend defaults (0.4 base / -0.2..+0.4 seniority / -0.2..+0.2 institution); calibrate at Stage 10.
- 686-OQ4 Public temperament typology — recommend 5-temperament typology proposed; territory authoring deferred until territories canonicalize.
- 686-OQ7 α_temperament + β_temperament = 1 — recommend keep constraint; alternative (independent scalars) adds parameters without clear gain.
- 686-OQ8 Mission shift triggers — enumerate: (a) victory-track milestone passes/fails; (b) leader replacement under exceptional circumstances; (c) failed mission_failure_threshold (define threshold ≥ 4 consecutive Mission contradicting outcomes); (d) explicit authored event in scenario.
- 686-OQ6 Mandate retention — recommend transitional retention.
- 686-P2-2 Cascade-per-territory — recommend multi-root allowance.

**Commit message:** `[infrastructure] PP-686 v2 faction architecture spec consuming PP-687 (PROVISIONAL)`

**Effort:** 1.5 sessions.

#### Commit 4 — PP-688 Articulation Layer

**Files:**
- `designs/articulation/articulation_layer_v30.md` (new, Class A canon).
- Updates to PP-687 type registry adding 3 new Key types as Class B extensions (per 688-6).
- Updates to per-type schemas adding 3 payload fields on scene-event Keys (per 688-7).

**Spec contents:**
- §1 Three-tier framing (locked per artifact 12 + 13). Tier 1 mud (default UI lens, protagonist's observer set). Tier 2 trigger cut scenes (significance ≥ 0.55). Tier 3 year-end omniscient chronicle (significance + causal centrality + omniscient prose templates).
- §2 Significance function (universal track + protagonist track) per artifact 13 §1, refined by artifact 14 §3:
  - Universal: `0.25 × (prominence + stakes + expectation_weight + awareness)`.
  - Protagonist: `scene_completion_baseline + knot_bonus + belief_bonus + inspiration_bonus + 0.4 × generic`.
  - Knot/Belief/Inspiration formulas reading canonical mechanics per artifact 14.
- §2.1 Cumulative narrative weight tracking on actors (per 688-8): per-actor cut-scene appearance counter; raises prominence permanently after 3+ appearances.
- §2.2 Awareness post-emission update (per 688-9): when subsequent Keys reference a Key as cause, original Key's awareness grows by +0.1 per subsequent reference (capped at 1.0).
- §3 Tier 2 trigger ruleset — initial 7 most-consequential triggers (subset of artifact 12 §1.2):
  - state.scar_acquired (high salience to protagonist)
  - state.coup_attempted
  - state.succession
  - mechanical.mission_shift
  - da.covert_betrayal with exposed=true
  - meta.knot_formed and meta.knot_ruptured
  - env.peninsular_strain_shock with delta ≥ 1
  - cross-faction Key clustering (5+ Keys involving same two factions in 1-2 seasons) — *ratify Phase B if calibration tractable*
  - state.belief_revised
- §4 Tier 3 chronicle generator — selection algorithm + period-correct prose templates + omniscient voice per artifact 13 §7 + artifact 15 sample.
- §5 New Key types (Class B extensions): `meta.knot_formed`, `meta.knot_ruptured`, `state.belief_revised`. Permanence: indelible.
- §6 Scene-event payload extensions: `belief_engagement_for: {actor_id: aligned/challenging/betraying}`, `inspirations_engaged_for: {actor_id: [inspiration_names]}`, `knot_partners_present: [actor_ids]`.
- §7 Phase 5a Godot scope addendum (cut scene rendering, ~1-2 sessions added per artifact 12 §10).
- §8 Pacing system explicitly out of scope (deferred to future PP per artifact 10 §10.5).

**Jordan-decisions for commit 4:**
- 688-2 / 688-3 trigger ruleset scope: ratify 7 initial triggers, defer 8th (cross-faction clustering) and 9-25 to Phase B per scenario authoring needs?
- 688-12 pacing system — confirm deferral?

**Commit message:** `[infrastructure] PP-688 articulation layer spec (PROVISIONAL)`

**Effort:** 2 sessions.

#### Commit 5 — Conviction → Axis Matrix Calibration Rationale

**File:** `designs/personal/conviction_axis_matrix_v30.md` (new, Class A canon).

The 12 × 4 = 48 entry matrix with calibration rationale per Conviction. Each row carries the values from PP-687 §3.4 plus a brief note grounding the position in Renaissance vocabulary (e.g., why Authority scores +0.9 hierarchical, +0.1 sacred — direct reference to medieval-Renaissance political theology).

This is split from commit 1 because the calibration rationale is its own document; the matrix values are referenced by commit 1's Key substrate spec.

**Effort:** 0.5 session.

**Commit message:** `[editorial] Conviction → axis matrix v30 with calibration rationale (PROVISIONAL)`

#### Commit 6 — Patch Register Entries

**File:** `canon/patch_register_active.yaml` updated with PP-684, PP-685, PP-686, PP-687, PP-688 entries.

Each entry follows PP-674 vetting block format:

```yaml
- id: PP-687
  date: 2026-04-30
  scope: Universal Key substrate
  class: A
  vetting:
    necessity: pass
    omega: pass
    mu: [Μ-α, Μ-β, Μ-γ, Μ-δ]
    m_ratings: {M-1: "+", ..., M-11: "+"}
    q: pass
  status: PROVISIONAL pending Jordan ratification
  applied_commit: <commit-1 SHA>
  blockers: ratification + Stage 10 sim verification
  resolves_eds: []
  superseded_eds: []
  forward_observations:
    - Memory query API needs production indexing
    - Pacing system deferred to future PP
```

Five entries total. **All PROVISIONAL** until Jordan ratifies.

**Effort:** 0.3 session.

**Commit message:** `[patch] PP-684/685/686/687/688 register entries with vetting blocks (PROVISIONAL)`

### §3.3 Total Effort Across the 6 Commits

| Commit | Effort | Cumulative |
|---|---|---|
| 1 (PP-687 spec) | 1.0 | 1.0 |
| 2 (PP-684 + PP-685) | 1.5 | 2.5 |
| 3 (PP-686 v2) | 1.5 | 4.0 |
| 4 (PP-688 articulation) | 2.0 | 6.0 |
| 5 (axis matrix rationale) | 0.5 | 6.5 |
| 6 (register entries) | 0.3 | 6.8 |

**Total: ~6.8 sessions of finalization work** to ratify five proposals. This is the "spec finishing" pass after Jordan ratifies each proposal's open questions.

### §3.4 Jordan-Decision Batch (the 12 that matter)

Of ~75 open items, only 12 require Jordan to choose. The rest are spec-fills that follow the proposals' published recommendations or sim-validated defaults.

| # | Decision | Default recommendation | Affects |
|---|---|---|---|
| **D1** | Honor as 13th Conviction (684-2 / 686-OQ2) | Yes — keep as 13th | PP-684, PP-686 §3.3, PP-685 |
| **D2** | 4-axis count + labels (684-7) | Accept 4 axes; mark 5th as Class B extension if calibration finds Community/Identity collapsing | PP-684, PP-687 §3.4 |
| **D3** | PP-686 cascade-per-territory vs cascade-per-faction (686-P2-2) | Multi-root cascade allowance | PP-686 §3.2.2 |
| **D4** | PP-686 Mission shift triggers (686-OQ8) | Enumerate as 4 triggers per §3.2 above | PP-686 §3.1 |
| **D5** | PP-687 schema sign-off (687-OQ1) | Approve as drafted | PP-687 §3.1 (load-bearing) |
| **D6** | PP-687 type registry initial scope (687-OQ2) | 7 families × 25-30 subtypes per §3.2 above | PP-687 §4 |
| **D7** | PP-687 visibility default (687-OQ4) | Default-from-scene with explicit override | PP-687 §3.2 |
| **D8** | PP-687 phased rollout vs hard cutover (687-OQ7) | Phased per §7.3 | PP-687 §7.3 |
| **D9** | PP-687 naming "Key" (687-OQ8) | Keep "Key" | nomenclature |
| **D10** | PP-688 trigger ruleset initial scope (688-2) | 7 + 1 conditional initial triggers; expand in Phase B | PP-688 §3 |
| **D11** | PP-688 pacing deferral (688-12) | Defer to future PP | scope |
| **D12** | C3 drift_coef value (0.55 / 0.6 / 0.65) | 0.6 midpoint, recalibrate at Stage 10 | PP-686 §3.2 |

**Time-box recommendation:** 60-90 minutes for Jordan to walk all 12. Each is yes/no/defer or pick-one-of-N. Format as a single decision sheet (artifact 17 candidate after this artifact lands).

### §3.5 Stage 10 Verification — What Runs After Ratification

Once the six commits land and Jordan ratifies, two simulation chains run:

#### §3.5.1 Lateral cross-system simulation chain (week-audit §5.2 #5)

The audit-week NERS flagged this as missing. Scope: faction-layer × mass-battle × social_contest at scene scale + Strain interaction. Property-tests:

- A scene-scale insult escalates to mass-battle through social_contest → DA → mass_battle pathway. Does L/PS converge to expected Honest-Defeat or Successful-Tyrant pattern depending on outcomes?
- Strain shock triggers cross-faction Disposition shift; does PP-686 strictness recalibrate as expected?
- Multi-faction concurrent activity: can N=6 factions run simultaneous DA + scene + battle activity without race conditions?

Effort: 1-2 sessions.

#### §3.5.2 Articulation layer simulation chain

Test the significance function and chronicle generator on a 3-year campaign. Property-tests:

- Significance scoring: does the function distinguish Bill-Clinton-affair vs neighborhood-affair as artifact 13 §6 worked example?
- Tier 2 cut scene firing: does the 7-trigger ruleset produce ~2-4 cut scenes per season at expected significance density?
- Tier 3 chronicle: does the year-end chronicle assembly produce period-correct prose from substrate Keys without hallucinating facts?
- Knot/Belief/Inspiration integration: do canonical-mechanic engagements correctly raise player_significance?
- Determinism: same seed produces identical chronicle text.

Effort: 1-2 sessions.

#### §3.5.3 PP-687 production-engine determinism verification

Beyond the simulator's verification, the production engine needs to confirm:
- All RNG sources seeded per Key emission.
- Sub-step ordering deterministic (stable sort by emission order).
- Floating-point reproducibility at architecture-level (spec x86_64 + IEEE-754 default rounding).

This runs *during* Phase 5a Godot implementation, not before. Surface defects flagged for backporting.

### §3.6 Phase 5a Godot Scope Update

PP-687 substantially **simplifies** Phase 5a (per PP-687 §6.9 + workplan v3 addendum §C.3). The first Godot scene becomes:

| Phase 5a Step | Original effort | Updated effort | Why |
|---|---|---|---|
| C3.1 Choose ingestion target | 0 (decision) | 0 | Wager arc still recommended |
| C3.2 GDScript Resource schema | 1 session | 1 session | Same; now also includes Key type registry |
| C3.3 Minimal scene tree | 2 sessions | 2 sessions | Same |
| C3.4 Scale-transition stub | 1 session | 0.5 session | Keys give the transition mechanism for free |
| C3.5 Sim-vs-engine parity | 1 session | 1 session | Same |
| **NEW: Diagnostic UI** | (was deferred) | 2 sessions | faction dashboard + Memory viewer + CAUSAL_GRAPH walker + arc-resolution notifications |
| **NEW: Cut scene rendering** | (was deferred) | 1-2 sessions | Tier 2 + Tier 3 cut scenes per artifact 12 + 15 |
| **Updated Phase 5a total** | 5 sessions | 7.5-8.5 sessions | +2.5-3.5 for UI work |

**The +2.5-3.5 sessions are required by the architecture's robustness conditional.** Without diagnostic UI, the player cannot perceive the substrate's richness; without cut scenes, the articulation layer is invisible. They are not optional.

### §3.7 What This Plan Does *Not* Cover

Explicit out-of-scope for this integration pass:

- **PP-666 trio (settlement adjacency ED-710, fractional province ownership ED-711, succession split).** Carried forward as Phase 1 P2 carryover from week-audit §3.1. PP-686 has soft dependency; not blocking ratification.
- **Workplan v3 ↔ commit ID linkage.** Process item from week-audit risk R5; addressed separately.
- **PROVISIONAL→canonical sweep for prior backlog.** ED-750/751/752/753/754/762/764, PP-297/351/653, etc. Per week-audit risk R6; addressed separately.
- **Mass-battle decision queue (16 items).** Per week-audit §3.4. Separate Jordan-decision sweep.
- **Pacing system.** Per artifact 10 §10.5; future PP.
- **Player-triggered chronicle review (688-10).** Phase 5a UI addition; can defer past initial Phase 5a if needed.
- **Modding interface formal spec.** Future PP candidate; PP-687 enables it.

---

## §4 Risk Register

Risks specific to the integration pass.

| # | Risk | Severity | Probability | Mitigation |
|---|---|---|---|---|
| **IR-1** | PP-687 schema needs revision after Phase B per-system migration surfaces gaps | P1 | medium | §3.2 commit 1's spec review checkpoint; phased rollout per §7.3 isolates per-system risk |
| **IR-2** | Honor decision (D1) reverses, requiring PP-686 role-template rewrite | P2 | low | Decision sheet treats Honor as primary; if reversed, role-template rewrite is bounded (~6 templates) |
| **IR-3** | C3 drift_coef calibration finds 0.55-0.65 range insufficient for visible succession dynamics | P2 | low-medium | Stage 10 sim with extended coefficient range; if needed, fall back to crisis-bypass-only model (C4 alone) |
| **IR-4** | Memory growth exceeds projection; ~3,300 entries/NPC at 100 seasons may stress production | P2 | medium | Index strategy in PP-687 spec (commit 1 §5.3.1); compression rule deferrable per OQ6 |
| **IR-5** | 4-axis vectorization (D2) found insufficient post-Stage-10; need 5th axis | P3 | low | Class B extension; calibrate at Stage 10; rollback path is per-axis matrix update |
| **IR-6** | Tier 2 trigger ruleset (D10) under-fires or over-fires once calibrated | P3 | medium | Threshold tuning is one parameter; observable in Stage 10 articulation sim |
| **IR-7** | Phase 5a Godot scope inflation (UI + cut scenes adds 2.5-3.5 sessions) compounds existing implementation lag | P2 | high | Either accept the inflation as the cost of architectural completeness, or stage Phase 5a UI separately from initial scene work |
| **IR-8** | Stage 10 lateral simulation surfaces previously-unseen faction-layer × mass-battle × social_contest defects | P2 | medium-low | Effort-bounded simulation; defects map to specific commits to revise |
| **IR-9** | Vocabulary debt (lateral E direction) compounds during integration before unification pass runs | P3 | high | Glossary unification scheduled post-ratification; until then, alias_registry handles cross-references |
| **IR-10** | Player-facing UX of Tier 1 ambiguity feels confusing rather than authentic | P2 | low-medium | Phase 5a playtest gate; if reading as confusion-not-mud, increase Tier 2 trigger density |

**No P0 risks.** Highest-probability risks (IR-7 Phase 5a scope; IR-9 vocabulary debt) are scheduling/resourcing, not architectural.

---

## §5 What Success Looks Like

**End of commit 1:** PP-687 substrate spec is finalized as Class A canon document. Schema sign-off from Jordan completes.

**End of commit 2:** PP-684 12-Conviction taxonomy + Self-Other axis is canonical. PP-685 migration roster maps existing characters cleanly.

**End of commit 3:** PP-686 v2 spec consumes PP-687 substrate; resolves all P1 + P2 audit findings; embeds C1–C10 calibration set.

**End of commit 4:** PP-688 articulation layer spec defines significance function + 3-tier framework + initial trigger ruleset. New Key types register as Class B extensions.

**End of commits 5-6:** axis matrix calibration rationale documented; all five PPs in patch_register_active with vetting blocks.

**End of Stage 10 verification:** lateral simulation chain runs; articulation sim runs; production-engine determinism verified during Phase 5a; calibration adjustments backported.

**End of Phase 5a:** first Godot scene executes a Wager arc using PP-687 Keys; sim-vs-engine parity test passes; diagnostic UI surfaces faction state and CAUSAL_GRAPH walks; Tier 2 cut scenes fire on triggers; Tier 3 year-end chronicle generates period-correct prose.

**Long-term success:** the architecture's structural emergence (per artifact 10) materializes as 70-85% "coherent story" experience frequency (per artifact 11 §6 estimate), bounded only by the irreducible variance of pure emergent systems.

---

## §6 What Should Have Been Done Differently in This Session (Reflection)

Per artifact 14 §9 — the prior session's omission of canonical-mechanic search before drafting the significance function. The lesson:

**Always search the repo for existing mechanics before drafting parallel structures.** Knots, Beliefs, Inspirations are well-established; pretending to invent equivalents was wasted effort and risked drift from canon. The integration plan above explicitly references existing mechanics where they apply (Knot lifecycle ED-773; Belief mechanics fieldwork_socializing §5.5; Inspiration mechanics params/core.md L128).

This is a process item, not a content item. The hooks system could enforce: a "search-canonical-sources-before-spec" gate that requires the author to acknowledge having searched for terminology/mechanics before drafting new ones. Out of scope for this artifact but worth noting for future hook enhancements.

---

## §7 Verdict

The open-items set is **structurally sound, dependency-resolvable in a fixed sequence, and substantively complete pending 12 Jordan-decisions and ~6.8 sessions of finalization work.**

The integration plan ratifies five proposals across six commits, runs two Stage 10 simulations, and updates Phase 5a Godot scope. After completion:

- Project's previously weakest NERS directions (lateral, diagonal) become STRONG.
- Player experience extends from happenings (~50%) to coherent story (~70-85%) per artifact 11.
- Substrate enables save/restore, replay, modding, diagnostic UI, and chronicle articulation as automatic byproducts.
- Three remaining MODERATE NERS cells (bottom-up smoothness, lateral elegance, horizontal smoothness/elegance) are addressed by spec-fills, vocabulary-unification pass, and a future pacing PP — none architectural.

This is the largest single architectural advance recorded in the project's session history. The integration plan keeps the work bounded and sequenced.

**Recommendation:** present the 12-decision batch (§3.4) to Jordan as a single sheet for time-boxed review, then execute the six commits in sequence (§3.2), then run Stage 10 verifications (§3.5).

---

**End plan. PROVISIONAL pending Jordan ratification.**
