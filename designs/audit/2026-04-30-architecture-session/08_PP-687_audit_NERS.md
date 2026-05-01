# PP-687 Audit — NERS All Directions

**Subject:** `2026-04-30_PP-687_proposal.md` — Universal Key Substrate
**Auditor:** Claude (independent review of own draft)
**Generated:** 2026-04-30
**Scope:** Comprehensive NERS audit per project Specific Definitions: Necessary, Robust, Smooth, Elegant. Six directions: top-down, bottom-up, vertical, diagonal, lateral, horizontal.

---

## §0 Executive Summary

PP-687 introduces a universal Key substrate as the engine's event-passing layer. The audit finds the proposal **architecturally sound and unusually ambitious** — it does not simply add a system but unifies many existing systems behind a single substrate.

**Verdict matrix:**

| Direction | N | R | S | E |
|---|---|---|---|---|
| Top-down | STRONG | STRONG | STRONG | STRONG |
| Bottom-up | STRONG | MODERATE | MODERATE | STRONG |
| Vertical | STRONG | STRONG | STRONG | STRONG |
| **Diagonal** | **STRONG** | **STRONG** | **STRONG** | **STRONG** |
| Lateral | STRONG | STRONG | STRONG | STRONG |
| Horizontal | MODERATE | MODERATE | MODERATE | STRONG |

**Pattern:** PP-687 scores STRONG in 19 of 24 cells. This is the strongest NERS profile of any proposal audited this week. **The diagonal direction goes from PP-686's WEAK to STRONG — PP-687 is largely the resolution to PP-686's weakest axis.**

**However, four findings worth attention:**

1. **P1: Performance scaling not validated.** The proposal estimates 3,600-9,000 Keys per game; this is plausible but unverified. Performance characteristics of CAUSAL_GRAPH walks at scale, salience computation across all NPCs per Key, and observer-set computation deserve simulation before commit.

2. **P1: Determinism guarantees not specified.** §5.6 promises replay determinism, but concrete requirements (random number sourcing, time-step ordering invariants, floating-point reproducibility for axis-projection math) are not enumerated. If determinism breaks, save/restore breaks.

3. **P2: The 4-axis Conviction matrix is a load-bearing simplification.** PP-687 specifies 4 named axes (hierarchical, sacred, instrumental, traditional). This is a concrete authoring commitment that constrains all downstream NPCs, events, Keys, and Conviction representations. The 4 axes are insufficient for some Renaissance distinctions (e.g., communal vs categorical belonging — Community vs Identity Convictions both score similarly on these 4 axes).

4. **P2: Bootstrap problem during migration.** Phase B (per-system migration) requires that *some* systems still emit/consume non-Key events while others have migrated. The proposal doesn't specify how the substrate handles partial-migration state.

These are addressable in the same revision as the simulation work.

---

## §1 Top-Down Audit (project intent → individual mechanic)

**Project intent:** *positive feedback loop between player decisions and mechanics that produces an engaging Godot videogame world with emergent narratives.*

### N (necessary)

**STRONG.** The cross-system coupling problem is real and structural. The week NERS flagged lateral integration as the project's weakest direction. PP-687 directly addresses that by making cross-system coupling *the default substrate* rather than a per-pair specification problem.

But: necessity is graded. Two cheaper alternatives exist:

- **Alternative A — selective Key adoption.** Migrate doc 12 procedures to consume EventImpact-style records; leave other systems untouched. Captures political-dynamics improvements; doesn't unify across systems. ~3 sessions vs PP-687's 7-9.
- **Alternative B — interface-only contracts.** Define a typed event interface that systems implement individually; no shared Key log; no CAUSAL_GRAPH; no replay. Captures coupling clarity without infrastructure. ~2-3 sessions.

PP-687 is more ambitious than either. The added value is: **(a) save/restore via Key log, (b) replay determinism, (c) walkable CAUSAL_GRAPH for diagonal trace, (d) modding interface as automatic byproduct.** If any of (a)-(d) is undesired, PP-687 is over-built.

For a Godot videogame with multi-session play (a)-(d) all matter. PP-687's necessity is conditional on this gameplay scope but firmly STRONG within it.

### R (robust)

**STRONG.** Robustness sub-criteria:

- *Player strategic depth:* every player choice composes through Keys; consequences are walkable. ✓
- *Customization:* scenarios are Key sequences; modding is Key emission; new event types are Class B extensions. ✓
- *Variety in approach:* the substrate is *generative* — interactions emerge from Key composition, not from authored special cases. ✓
- *Player feels important:* CAUSAL_GRAPH lets the player see how their actions cascaded. ✓
- *Player feels they impact world:* Key emissions are consequential; impact_vectors record the change. ✓
- *Emergent narrative without player:* NPCs autonomously emit Keys per their Procedures. ✓
- *Mechanics fully formed:* PARTIAL. The substrate is well-specified; per-type schemas (§4.2) are illustrative for 5 types but the full registry of ~25-30 types is not yet authored.

**6 of 7 strong; 1 partial.** R = STRONG.

### S (smooth)

**STRONG.**

- *Integrates without friction:* unifies multiple existing event channels behind a single substrate. ✓
- *Mechanics interact cleanly:* the §6 integration walk-through covers PP-686, doc 12, conviction_track, scene systems, mass_battle, peninsular_strain, scale_transitions, and Godot — all map cleanly. ✓
- *Scale-zoom:* `scale_signature` field is multi-valued; multi-scale Keys natural. ✓
- *Transitions cleanly between systems:* a single Key flowing through observer resolution → Memory write → consumer subsystem update is the canonical path. ✓
- *Pauses correctly:* lifecycle states (Drafted, Emitted, Persistent, Decayed, Pruned) make pause/resume semantics explicit. ✓
- *Calculation methodology consistent:* dot products, observer set computation, log append. Same primitives across all systems. ✓

**S = STRONG.** This is the proposal's strongest direction.

### E (elegant)

**STRONG.**

- *Logically simple:* one substrate, one update rule, one schema. ✓
- *Clear approach:* each system emits Keys, consumes Keys; no exceptions. ✓
- *No unnecessary overhead:* the schema is minimal; per-type payloads are extensible. ✓
- *Easy to understand:* the model is the chronicle — events, observers, consequences. Period-correct mental model. ✓
- *Player intuits complex outcomes from simple choices:* every choice emits Keys whose consequences are walkable. ✓

E = STRONG.

**Verdict (top-down):** N=STRONG, R=STRONG, S=STRONG, E=STRONG.

---

## §2 Bottom-Up Audit (individual mechanic → engine coherence)

### N (necessary)

**STRONG.** Each component of the substrate is necessary:
- Universal schema: needed for type-uniformity.
- Type registry: needed for typed-payload validation.
- Update rule: needed for canonical event-handling.
- CAUSAL_GRAPH: needed for diagonal trace (existing E-DIAG-A featured behavior).
- Memory as Key references: needed to unify NPC Memory schemas.

### R (robust)

**MODERATE.** Sub-criteria:
- Components have explicit inputs, outputs, derivation. ✓
- Component composition: validation → log append → observer resolution → interpretation → state update → cross-system propagation → graph update. Linear, well-defined. ✓
- Edge cases addressed?
  - Cycle in causes graph: not explicitly handled. **Should be a validator** in §5.1 step 1.
  - Key emitted with no observers (private with empty list): probably valid; spec doesn't say what happens.
  - Concurrent emission within same sub-step: ordering tiebreak unspecified.
  - Replay with non-deterministic system clock: spec promises determinism but doesn't enumerate sources of non-determinism to control.
- Numerical bounds enforced: salience clamps [0, 3]; impact_vector axes signed-magnitude. Per-stat deltas not bounded by substrate (system-specific bounds).

**Edge cases need a §5.x sub-clause.** R = MODERATE.

### S (smooth)

**MODERATE.** Component interactions:
- Update rule cleanly composes (validate → log → observe → interpret → propagate → graph). ✓
- Memory query interactions: Memory is a derived view of the Key log, but query patterns (filter by time, salience, axis-relevance, target-mention) need explicit query API. Not specified.
- Performance characteristics not analyzed: walking CAUSAL_GRAPH backward to N hops; observer set computation; salience updates per Key. **§5 doesn't include complexity analysis.**

S = MODERATE.

### E (elegant)

**STRONG.** Component-level elegance:
- Single Key schema is one definition. ✓
- Single update rule is ~10 lines of pseudocode. ✓
- Memory as Key reference + salience is two fields. ✓
- CAUSAL_GRAPH is a directed graph; standard data structure. ✓

E = STRONG.

**Verdict (bottom-up):** N=STRONG, R=MODERATE, S=MODERATE, E=STRONG.

---

## §3 Vertical Audit (scale-axis coherence: personal ↔ settlement ↔ territory ↔ peninsula)

### N (necessary)

**STRONG.** Multi-scale Keys with explicit `scale_signature` make scale-bridges first-class. Currently scale-bridges are implicit; PP-687 makes them visible and auditable.

### R (robust)

**STRONG.**
- Personal-scale Keys (scene_event subtypes, state.scar_acquired) integrate with personal_convictions. ✓
- Settlement-scale Keys (settlement signal aggregates) are explicit Key types. ✓
- Territory-scale Keys (DA outcomes, treaty events) carry territory_id targeting. ✓
- Peninsula-scale Keys (env.peninsular_strain_shock, env.crisis) explicit. ✓
- Multi-scale Keys (scene-event in territorial-strategic context) carry multi-element scale_signature. ✓

### S (smooth)

**STRONG.** The scale-zoom is transparent: a Key with `scale_signature: [personal, settlement]` is interpretable at both scales without per-pair adapter code.

### E (elegant)

**STRONG.** Multi-element scale_signature is one field that does the work of N×N pair-couplings. The 16-Accounting trace becomes a forward walk of CAUSAL_GRAPH from a scene-scale Key.

**Verdict (vertical):** N=STRONG, R=STRONG, S=STRONG, E=STRONG.

---

## §4 Diagonal Audit (cross-scale + cross-system interactions)

This is the direction PP-686 audit found WEAK. PP-687 is largely **the resolution** of that weakness.

### N (necessary)

**STRONG.** The diagonal-trace problem (E-DIAG-A featured behavior; PP-686 audit P2-1) is exactly what `causes[]` and CAUSAL_GRAPH solve. The ability to walk forward and backward across the cross-scale + cross-system event chain is the proposal's most distinctive feature.

### R (robust)

**STRONG.**
- Causal chains are walkable, with cycle-freeness as the key invariant (modulo §2 P1 above).
- Cross-system propagation via TYPE_SUBSCRIPTIONS is explicit.
- Long-horizon stress: a 12-year game produces ~3,600-9,000 Keys; CAUSAL_GRAPH walks bounded by N-hop limits. Workable.

### S (smooth)

**STRONG.**
- Diagonal coupling is *the default substrate*, not a per-pair specification.
- The 16-Accounting trace becomes a CAUSAL_GRAPH forward walk: emitting Keys, propagation events, downstream consumers, all visible.

### E (elegant)

**STRONG.**
- The chronicle metaphor is period-correct and player-legible.
- Walking provenance is a familiar mental model (cause → effect chains).

**Verdict (diagonal):** N=STRONG, R=STRONG, S=STRONG, E=STRONG.

**This is the audit's most significant finding.** PP-687 directly addresses what was the project's weakest direction.

---

## §5 Lateral Audit (peer systems at the same scale)

This was PP-686 audit's WEAKEST direction.

### N (necessary)

**STRONG.** The N×N pair-coupling problem (every new peer system requires per-pair wiring with every existing peer) collapses to N substrate-couplings (each system plugs into the substrate).

### R (robust)

**STRONG.**
- Peer-system independence: each emits/consumes Keys via its own subscription rule.
- Peer-system composition: TYPE_SUBSCRIPTIONS lets multiple consumers respond to the same Key without coordination.
- Cross-faction Disposition shifts: any system can read DA outcome Keys to update inter-faction relations.

### S (smooth)

**STRONG.**
- Adding a new peer system: implement Key emission + Key consumption; no per-pair work. ✓
- Vocabulary unification: all systems use the same Key field names, scale_signature labels, axis names.

### E (elegant)

**STRONG.**
- Replaces N×N coupling with N×1 substrate couplings.
- Single canonical event substrate is conceptually clean.

**Verdict (lateral):** N=STRONG, R=STRONG, S=STRONG, E=STRONG.

**This is the second-most significant finding.** PP-687 transforms PP-686 audit's weakest direction (lateral) into a strong direction.

---

## §6 Horizontal Audit (sequence/temporal: turn order, phase order, event chaining)

### N (necessary)

**MODERATE.** The temporal aspects covered:
- Key ordering via `emitted_at: (season_index, sub_step_index)`. ✓
- Per-season cascade re-resolution timing (existing PP-686 spec). ✓

Not covered:
- Mid-season event ordering when multiple Keys fire same sub-step. Tiebreak rule needed.
- Cross-Key dependency: a Key requires another Key to have been processed first. Not specified.

### R (robust)

**MODERATE.**
- The Key log is append-only, ordered. ✓
- Replay determinism *promised* but not specified (P1-2 above).
- Sub-step concurrency: not addressed.

### S (smooth)

**MODERATE.**
- Per-season Accounting is the natural sync point.
- Within-season: Keys fire as their triggering systems emit. Order is by sub-step index but tiebreaks for same-sub-step Keys are unspecified.

### E (elegant)

**STRONG.**
- Append-only log is the simplest possible temporal model.
- Sub-step indexing is a one-line specification.

**Verdict (horizontal):** N=MODERATE, R=MODERATE, S=MODERATE, E=STRONG.

**Horizontal is the audit's weakest direction for PP-687.** Specifically: determinism, sub-step ordering, and dependency specification need explicit treatment.

---

## §7 Findings Summary — by Severity

### P1-CRITICAL (block ratification)

**P1-1.** Performance scaling not validated. The 3,600-9,000 Keys/game estimate is plausible but unverified. Specific concerns:
- CAUSAL_GRAPH walks beyond ~500 nodes may be slow for diagnostic UI queries.
- Salience computation across all NPCs per Key emission is O(NPCs × Keys/season). At 35 NPCs and ~10 Keys/season per faction × 6 factions = 60 emissions/season → 2,100 salience computations/season. Manageable but not trivial.
- Memory query patterns at scale (NPC walking 100+ stored Keys to find relevant ones) need indexing strategy.
*Resolution:* simulate a 30-season game with realistic Key density; profile CAUSAL_GRAPH walks and Memory queries; specify indexing strategy if needed.

**P1-2.** Determinism not specified. §5.6 promises replay determinism but doesn't enumerate sources of non-determinism. Required: explicit list of (a) random number sources (must be seeded per Key emission), (b) ordering invariants (must be deterministic when multiple Keys fire same sub-step), (c) floating-point operations (axis-projection math must be reproducible). Without this, save/restore is unreliable.

### P2 (block sim verification)

**P2-1.** 4-axis Conviction matrix is load-bearing. The 4 named axes (hierarchical, sacred, instrumental, traditional) are a concrete commitment that constrains every NPC, event, and Key. Insufficient axes for some Renaissance distinctions (Community vs Identity both score similarly on 4 axes). *Resolution:* either add 1-2 axes (relational? communal-vs-categorical?) or accept the simplification and document the tradeoff.

**P2-2.** Bootstrap problem during migration. Phase B has partial-migration state where some systems emit Keys and others use legacy event channels. The substrate must function during this transition. *Resolution:* §7.3 needs a sub-clause specifying compatibility: legacy events get wrapped in `meta.legacy_event` Keys; Key emitters during migration tolerate non-Key events. Or: explicit cutover boundary per Phase B stage.

**P2-3.** Cycle handling in causes graph. §5 doesn't enumerate what happens if a cycle is introduced. Validator should reject; or detect and break with a warning. *Resolution:* explicit §5.1.1 cycle handling.

**P2-4.** Memory query API not specified. NPCs query Memory; how exactly? Filter functions, indexing, performance characteristics. *Resolution:* §5.3.1 query API.

**P2-5.** Sub-step ordering tiebreak. *Resolution:* explicit ordering rule (e.g., emission order within a sub-step, with stable sort).

### P3 (improvements)

**P3-1.** Authoring tooling implicit. Authors writing scenarios need a Key-construction interface; engine validation feedback. Outside this proposal's scope but should be noted.

**P3-2.** Modding interface unspecified. PP-687 enables modding but doesn't formalize. Future PP candidate.

**P3-3.** Player-facing UI unspecified. Diagnostic UI for Key chains is mentioned but not designed. Phase 5a Godot scope.

**P3-4.** Pruning policy beyond `transient`. Long games may want compression of old Keys to summary records. Optional optimization.

**P3-5.** Conviction-axis matrix calibration. §3.4 values are illustrative. Stage 10 calibration target.

---

## §8 Comparison to Audit Concerns Anticipated by Proposal

Proposal §10 anticipates audit concerns. Cross-checking actual audit findings vs anticipated:

| Anticipated by §10 | Actual finding | Status |
|---|---|---|
| Schema design risk | (not raised; schema looks sound) | Good — proposal's pre-resolution helped |
| Performance / scale | P1-1 confirmed | Anticipated; needs simulation |
| Migration scope | P2-2 confirmed | Anticipated but needs more detail |
| NPC behavior coupling | resolved per §6.1 | Good |
| Lateral peer-system gaps | resolved per §6 | Good |
| Diagonal opacity | resolved via CAUSAL_GRAPH | Good |
| Player legibility of Key sequences | P3-3 (deferred) | Acceptable scope |
| Modding interface | P3-2 (deferred) | Acceptable scope |
| Authoring overhead | manageable per §7.4 | Acceptable |
| Backward compat | P2-2 needs detail | Anticipated but needs more |

**Proposal anticipated 6/10 concerns; sim and migration concerns need additional work; new findings (P1-2 determinism, P2-1 axis count, P2-3/4/5 horizontal-direction items) emerged.**

---

## §9 NERS Verdict Matrix

| Direction | N | R | S | E |
|---|---|---|---|---|
| Top-down | STRONG | STRONG | STRONG | STRONG |
| Bottom-up | STRONG | MODERATE | MODERATE | STRONG |
| Vertical | STRONG | STRONG | STRONG | STRONG |
| **Diagonal** | **STRONG** | **STRONG** | **STRONG** | **STRONG** |
| **Lateral** | **STRONG** | **STRONG** | **STRONG** | **STRONG** |
| Horizontal | MODERATE | MODERATE | MODERATE | STRONG |

**Aggregate: 19 STRONG / 5 MODERATE / 0 WEAK.** No direction is weak. The strongest profile of any proposal audited this week.

**Strongest direction:** **Diagonal and Lateral both go from PP-686's WEAK → STRONG.** PP-687 directly resolves the project's two weakest directional axes.

**Weakest direction:** **Horizontal robustness.** Determinism, sub-step ordering, dependency handling need explicit specification.

---

## §10 Recommendations

### §10.1 Immediate (before commit of PP-687 to register)

1. Add §5.1.1 cycle detection in causes graph (P2-3).
2. Add §5.3.1 Memory query API specification (P2-4).
3. Add §5.x sub-step ordering tiebreak rule (P2-5).
4. Add §5.6 sub-clauses enumerating determinism guarantees (P1-2).
5. Add §3.4 sub-clause acknowledging axis-count tradeoff (P2-1) — keep 4 axes but document the limitation.
6. Add §7.3.x bootstrap rule for partial-migration state (P2-2).

### §10.2 Short-term (before Phase B implementation)

7. **Run integration sim** against P1-1: build a 30-season Key log with realistic density; profile CAUSAL_GRAPH walks and Memory queries; surface any indexing/compression needs.
8. **Author full Key type registry** (§4) — ~25-30 types with required/optional payload fields. Class A canonical document.
9. **Author Conviction → axis matrix** (§3.4) — 12 × 4 = 48 entries with calibration rationale.

### §10.3 Strategic

10. **Sequence with PP-686:** PP-687 ratifies first; PP-686 spec revision references PP-687; both implement. Don't try to implement PP-686 ahead of PP-687.
11. **Phase 5a benefits:** explicit note that Phase 5a (Godot first scene) effort estimate likely *drops* once PP-687 is available because Keys provide the event substrate for free. Update workplan v3 addendum §C.3 estimate.
12. **Stage 10 verification scope:** explicit property-test battery: (a) cycle-freeness, (b) salience monotonicity, (c) visibility correctness, (d) replay determinism, (e) cross-system propagation correctness.

---

## §11 Strategic Assessment

PP-687 is **the most consequential architectural decision** in the project's recorded history. It composes with — and substantially improves — every system currently in canon:

- doc 12 procedures rewrite to consume Keys (cleaner)
- PP-686 faction architecture reads Keys (resolves 4 audit findings)
- Conviction Track + Threadwork emit Keys (unifies bespoke schemas)
- Scene + social_contest + mass_battle plug into substrate (lateral coupling solved)
- Phase 5a Godot first scene becomes Key-emitting code (faster)
- Save/restore, replay, modding emerge as automatic byproducts

**Cost:** 7-9 sessions implementation, plus the sim and audit work. Front-loaded; the substrate must be designed correctly because every other system will rest on it.

**Benefit:** structural. Once the substrate exists, subsequent design composes through it rather than requiring per-system event schemas. The cross-system coupling problem (the project's weakest direction per the week's NERS) is *solved by default* rather than per-pair.

**Risk:** schema design is load-bearing. If the universal Key fields are wrong, the entire engine is wrong. The proposal's anticipated audit concerns (§10) and this audit's findings (§7) collectively define the schema review checklist.

**Sequencing risk:** if PP-687 is delayed and PP-686 implements first, PP-686 will need a substantial rewrite when Keys arrive. Sequencing PP-687 first is essential.

---

## §12 Verdict

**Status:** PROVISIONAL with **2 P1 items** (performance simulation; determinism specification) and **5 P2 items** requiring resolution.

**Architecture:** STRONG. The universal substrate is conceptually clean, period-correct (chronicle-grounded), and resolves multiple audit findings from PP-686 simultaneously.

**Specification:** mostly complete; the §10.1 immediate items are well-bounded paragraphs.

**Direction strengths:** all six directions score STRONG in at least 3 of 4 NERS axes. **Diagonal and Lateral go from WEAK (PP-686) to STRONG (PP-687).**

**Direction weaknesses:** Horizontal robustness (determinism, sub-step ordering). Bottom-up smoothness (Memory query API). Bottom-up robustness (edge cases).

**Recommendation:** revise to address §10.1 items; run the integration simulation per §10.2 #7; ratify ahead of PP-686 implementation. PP-687 → PP-686 → both implement.

**Net assessment:** the strongest single proposal of this design week. It elevates everything around it.

---

**End audit.**
