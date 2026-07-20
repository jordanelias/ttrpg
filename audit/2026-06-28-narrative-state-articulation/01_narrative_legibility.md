<!-- STATUS: ANALYSIS — examines PP-688 + the no-LLM legibility problem. Cites canon; edits none. -->
# 01 — Narrative Legibility Without a Runtime LLM (Examination)

The game cannot call an LLM at runtime (`videogame_mode_spec.md` §0: "the engine narrates"). How, then, does a legible story reach the player out of many dynamic emergent arcs and all their atomic beats? This document examines the whole pipeline.

## 1. PP-688 is already a natural-language-generation (NLG) pipeline

The classic NLG pipeline (Reiter & Dale 2000) has four stages. PP-688 (`articulation_layer_v30.md`) already *is* the first two and gestures at the rest:

| NLG stage | PP-688 / Valoria mechanism | Status |
|---|---|---|
| **Content selection** | significance function (§3.2, 0–13) + 10-trigger ruleset (§3.1) + chronicle top-N (§4.3) | **specified** |
| **Document planning** (order + group) | `causes[]` chains + `emitted_at` sequence; per-faction/per-NPC chronicle structure (§4.4) | partial |
| **Microplanning** (aggregation, referring expressions, lexical/register choice) | — | **the gap** |
| **Surface realization** (templates + splicing) | "templates per Phase 5a Godot implementation" (§4.5); Stage-10 A3 **DEFERRED** | **the gap** |

So the unsolved part is precisely **microplanning + realization** — turning selected, ordered atoms into legible on-voice prose. The rest of this bundle targets that gap.

## 2. The atom↔sentence answer

Do we need one coded sentence per atom, each carrying a "narrative key" for sequence and joins, dynamically aggregated? **No** — and the distinction is load-bearing.

- **Many-to-one and lossy.** Most atoms (Keys) are never narrated: significance pruning (PP-688 §3.2) and triggering (§3.1) already drop the long tail. Survivors are *grouped into beats* and *aggregated*: several same-subject atoms collapse into one spliced sentence ("Baralta excommunicated the bishop and seized the tithe-barns"), per NLG aggregation. The voice canon (`narrative_voice_canon_v30.md`) actively *forbids* the one-sentence-per-atom failure mode ("no reaction shot after every event"; "no AI sheen — repetitive cadence") and *requires* intra-sentence splicing.
- **The "narrative key" already exists** — as Key metadata, not a parallel system: `causes[]` → connectives (because/so), `emitted_at` → ordering, `targets[].role` → grammatical roles, `symbolic_dimensions`/`impact_vector` → axis emphasis/lexical choice, `significance` → length & whether it surfaces, `awareness` → callback foregrounding.
- **Bounded, not "crazy."** Factoring (templates ⟂ register-lexicon ⟂ focalizer ⟂ connectives) turns a multiplicative product into an additive sum — hundreds of authored units composed combinatorially, not thousands of baked sentences. Full design in `03_…`.

## 3. Legibility is not only prose — three "show" channels

Per Jenkins (narrative architecture), Marie-Laure Ryan (story = cognitive construct), and Juul (games are present-tense), most legibility should be *shown*, not narrated:

1. **Tier-1 UI lens** (PP-688 §2): Concern queue, Memory salience, Bonds register — always-on, no prose generation.
2. **UI-as-narration** (`valoria_ui_ux_v4_1.md`): the Coherence-corruption ladder (menus jitter → 1-word displacements → ghostly second readings → rearranging menus) narrates state structurally. The third UX oath is literally "the game is felt, not narrated."
3. **Authored-pool sampling**: `visible_actions` (~80 observable-behavior strings) sampled at a disposition threshold; Scene-Slate opportunity templates; Seam Texts (authored scripture with TS-gated annotation). These convey NPC interiority and world state as labels/artifacts, not narrated prose.

**Juul's present-tense insight** gives the budget rule: live play is present-tense, so Tier 1/2 should mostly *show*; heavy recount-prose (past tense) concentrates in **Tier 3** (the annual chronicle = a "legends mode"). That is where the realizer earns its keep.

## 4. Player-as-constructor (the cheapest lever)

The design already cites the artifact-11 idea that "a story is the artifact the mind makes from sequenced consequential happenings." The literature and shipped games confirm this is the highest-leverage no-LLM move:

- **Tynan Sylvester (RimWorld):** "we supply these labels — say this is a person's *sister* — and suddenly everything has new meaning… all you need are a few simple labels, no more complicated than a children's book," and "people's brains just take over." Valoria already emits dense relational labels (Bonds, Knots, Convictions, Disposition, faction ties via Key `targets[]`/armature). Surfacing these legibly is *higher-leverage than generating prose*.
- **DF-Legends traversal** = PP-688's Tier-1 "Why?" causal-graph walk (§2.2) + chronicle search-bar (§2.5): the player reconstructs story by following the narrative graph. The engine supplies legible, provenance-rich events; the player's apophenia supplies connective tissue (Grinblat; Ryan's reparative play).

## 5. Tellability as the design target + the ready-to-hand/breakdown dial

Per Eladhari (retelling = the "fourth narrative layer") and Sych (read in full: *Worlds At Play* 2023; "When the Fourth Layer Meets the Fourth Wall"), an emergent narrative succeeds when it is **tellable to others** — a retelling. So the selection/sifting layer should optimize for *tellability*, not raw magnitude (converges with Nemesis dialogue "designed to be quotable/shareable" and Ryan's curationism).

Sych's Heideggerian frame gives the *when-to-surface* rule: narration should mostly be **ready-to-hand** (transparent — the player lives the story via §3's show channels), with deliberate **breakdown** moments (Tier-2 cut scenes; and the Coherence-degraded rendering register reframed as a *designed* present-at-hand breakdown — see `canon/01_foundations_amendment_self_rendering.md`) that provoke reflection. And per Sych's *critical retellings* + Ryan's *computational art brut*: the uncanny, "seams-laid-bare" emergent outputs are themselves assets players retell. The engine is the player's **storytelling partner** (Kreminski & Wardrip-Fruin), and friction is generative — so the design should preserve surprising specificity, not sand every seam smooth.

## 6. Emergent-arc legibility

Arcs are intersections of ~116 pressure vectors (`references/arcs/*`), made *meaningful* by throughlines (N1–N6 narrative, T-01..T-41 system; `references/throughline_registry.md`), and surfaced as history by Tier 3. The known risk (`designs/arcs/gm_ref/arc_narrative_analysis.md`): accumulation arcs whose payoff arrives after many low-intensity seasons can be invisible — mitigated by authored "intermediate checkpoints." In NLG terms: arcs are *higher-level patterns* detected over low-level Key patterns ("stories from the bottom up"); the detector is story sifting (`03_…` §3).
