<!-- STATUS: PROPOSAL (architecture-only) — drafted as a future PP-688 §11. Not canonical; no schemas/worked example this pass. -->
# 03 — Deterministic Narration Architecture (Proposal, architecture-only)

A proposed extension to PP-688 (a future `articulation_layer_v30.md` §11) closing the deferred realizer ("templates per Phase 5a"; Stage-10 A3). **Architecture only:** conceptual design + where it slots in. No data schemas, no worked example, no fragment content — those are deferred (see §9).

## 1. Thesis

The realizer is a **factored, condition-gated, deterministic NLG pipeline fed by an offline LLM bake**. This is the convergent architecture of every game in `02_…`: author a finite voice-bearing corpus offline; at runtime only **select → substitute → splice**. It reuses PP-688 wholesale for content-selection and document-planning, and the existing X/Y/Z voice grammar for the lexicon — it adds only the missing microplanning + realization stages, plus story-sifting and a pacing director.

## 2. The four orthogonal factors (compose, don't multiply)

The combinatorial trap is baking finished sentences per (type × tier × focalizer × …). The fix is to keep these factors *orthogonal* and compose at runtime — a product becomes a sum (hundreds of authored units, not thousands of sentences):

1. **Slot-templates** — per Key-type × significance-length band (the DF per-event-type-function pattern). Slots filled from Key payload / `targets[]` / resolved entity names (the CK substitution pattern).
2. **Register/lexicon overlay** — the existing **X/Y/Z quadrant grammar** (`session-handoff-2026-05-06.md` §4: X=Coherence, Y=Thread Sensitivity, Z=Spirit; coarse bands) **frozen as lexicon tables** (the Qud replacement-grammar / Compton-Tracery pattern). Not copied per template — a swappable word-choice layer.
3. **Focalizer overlay** — the 4 canonical chroniclers + protagonist frame (P-03). **Voice-as-focalization is the assembly solution:** the voice tag *is* the inter-fragment transition, so no connective generation is required, and uncertain/contradictory fragments coexist as a named perspective's opinion.
4. **Discourse/connective grammar** — connectives chosen from the discourse relation implied by `causes[]` (cause→"because/so", reversal→"but/yet", sequence→"then"). Plus NLG **aggregation** (collapse same-subject atoms) and **referring-expression generation** (name-then-pronoun) to kill robotic cadence.

## 3. Story sifting = the significance/arc-detection layer

Reframe PP-688's significance function as **story sifting** (James Ryan; Kreminski Felt/Winnow): sifting patterns expressed as **Datalog-style queries over the Key log** (the narrative graph of `00_…` §5). Concretely:
- Low-level patterns over single Keys / short `causes[]` chains feed Tier 2.
- **Arc detection** = sifting patterns over longer `causes[]` chains; **throughlines (N1–N6, T-01..T-41)** are the higher-level patterns these roll up into ("stories from the bottom up").
- Ranking heuristics layered on top: PP-688 significance (kept) + **"Select the Unexpected"** (statistically rare = interesting) + a **tellability** heuristic (Sych: prefer beats a player would retell). Horswill's TED/Simulog shows Datalog-over-event-state runs at frame-rate compiled to native code — buildable at scale.

## 4. Output-mode dial: ready-to-hand vs. breakdown

Per Sych/Heidegger, the realizer has a **transparency dial**:
- **Default ready-to-hand** — *show* via the §3-of-`01_…` channels (Tier-1 UI, UI-as-narration, observable-action labels, present-tense). No prose generated.
- **Escalate to authored prose** only at sifter-flagged **breakdown** beats (Tier-2 cut scenes; Tier-3 chronicle). This is the budget rule that keeps generation rare and tellable.

## 5. Dual-register generation tied to Coherence

Qud's clean-grammar-vs-Markov-corruption split maps directly onto Valoria's Coherence-indexed rendering (`canon/01_foundations_amendment_self_rendering.md`): the **same** factored realizer drives both — high-Coherence selects the clean X/Y/Z lexicon; low-Coherence applies authored degradation rules. The rendering *failure* is a register selection inside the realizer (a *designed breakdown*, §4), not a separate system. This is the no-LLM way to produce the coherence-indexed voice the `prose-writer` skill specifies.

## 6. Micro-reactivity & entity memory

- **Boolean micro-reactivity** (Disco Elysium): cheap flags flip on memorable Keys (reuse `awareness`/`causes[]`); later fragment conditions read them → finite text feels combinatorial. **First-class failure fragments** (anti-passives) so unlucky/low-stat paths aren't sparse; **once-only vs. repeatable** guards so callbacks don't re-fire.
- **Entity-memory selection** (Nemesis / DF anchors): NPC armature/memory already persists per-actor (`00_…` §2); Tier-2 fragment selection reads it so re-encounters reference prior Keys — entity-scale callbacks for free.

## 7. Pacing director (closing PP-688 D11)

PP-688 §7 explicitly defers pacing. Propose a **RimWorld-style pacing director** (with Façade's beat-sequencing as precedent): a deterministic scheduler that governs cut-scene cadence and chronicle density against a significance/tension curve (analogous to wealth-scaled threat-point budgeting), replay-safe. It consumes sifter output and modulates *when* breakdown beats surface — it does not generate text.

## 8. Offline-bake protocol (conceptual)

The voice canon is LLM-authored but the runtime can't infer. Resolution: **bake offline, assemble deterministically.**
- At **design time**, the `prose-writer` skill (LLM) generates and *freezes* fragment + lexicon pools per (Key-type × X/Y band × focalizer). This is exactly Tarn Adams' method ("write the stories you want; build the engine to produce that class") and Valoria's own Threetoe-style "stories → mechanics" pipeline.
- At **runtime**, the engine only evaluates conditions, selects, substitutes, and splices over frozen assets.
- **Determinism/replay**: the runtime path contains zero inference; same Key log → identical output (PP-687 §6 V4). Constraint-safe selection (Horswill CatSAT class) can guarantee no self-contradictory output.

## 9. Oatmeal-problem risk register

Compton's "10,000 Bowls of Oatmeal" is the live risk for a factored fragment corpus. Mitigations: vary only on **perceivable/consequential** axes; cluster fragments into named **beat-kinds**; differentiate by **causal context** (sifting + discourse relations attach the *why*); validate coverage with **Expressive Range Analysis**. Caveat (Sych/Ryan): perceptual *sameness* is the enemy, but uncanny *specificity* — the odd, seams-laid-bare beat — is a tellability asset; don't over-smooth.

## 10. Where it slots in & what stays open

- **Slot-in:** a proposed PP-688 **§11**. The Key registry **already carries the narration metadata** the realizer needs (`causes[]`, `targets[].role`, `symbolic_dimensions`, `significance`, `awareness`) — *no new required Key fields anticipated* (to be confirmed if this graduates past architecture-only).
- **Reuse, don't reinvent:** PP-688 significance/triggers/3-tier structure verbatim as content-selection + doc-planning; the X/Y/Z grammar as the lexicon; `gm_to_engine_conversion.md` patterns as the determinism precedent.
- **Open decisions (deferred):** aggregation tuning; significance/sifting recalibration; director pacing curves; realization home (design-repo frozen assets vs. `valoria-game` GDScript); bake granularity/count budget; whether sifting patterns are authored as Datalog or via an example-driven synthesizer.
- **Proposed evaluation instrument:** judge realizer output by **tellability** (Eladhari fourth-layer; Kreminski "Evaluating AI-based games through retellings"; Sych critical retellings) — would a player anecdote it? — alongside PP-688's Stage-10 battery.
