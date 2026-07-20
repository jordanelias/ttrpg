<!-- STATUS: ANALYSIS — design review + architecture-only proposal. Not canonical; proposes a future PP-688 §11. -->
# Narrative-State Propagation Review + Deterministic Narration Architecture

**Date:** 2026-06-28 · **Class:** design review + architecture-only spec proposal · **Status:** ANALYSIS (no canonical specs edited)

## Thesis (one paragraph)

The Key substrate (PP-687) already gives Valoria a single, closed, replay-deterministic event log; the articulation layer (PP-688) already specifies *which* events become story (significance) and *when* (triggers, chronicle) in three tiers. The one unsolved piece — and the explicit deferral in PP-688 ("templates per Phase 5a"; Stage-10 test **A3 chronicle-prose = DEFERRED, 'requires LLM/template integration'") — is the **deterministic, no-runtime-LLM realizer** that turns a Key into legible, on-voice prose. Every acclaimed narrative game we surveyed, authored (Disco Elysium, Planescape: Torment, Esoteric Ebb) and emergent (Dwarf Fortress, Caves of Qud, Crusader Kings, RimWorld), solves this the **same** way: author a finite, voice-bearing fragment/template corpus, tag each unit with conditions over game state, and at runtime only **select → substitute → splice** (zero generation). The proposal: a **factored, condition-gated NLG pipeline with an offline LLM bake** — reuse PP-688 as the content-selection/planning stages, reuse the existing X/Y/Z voice grammar as the lexicon overlay, add story-sifting (Datalog over the Key log) as the significance/arc-detection layer and a RimWorld-style pacing director to close PP-688's deferred D11 pacing. The answer to "one coded sentence per atom?" is **no** — narration is many-atoms-to-one-sentence, significance-pruned and aggregated, and the per-atom "narrative key" the question intuits already exists as Key metadata.

## Documents

| File | Question | Contents |
|---|---|---|
| `00_key_io_review.md` | How do Keys receive input & generate output? | The single update rule (IN → resolver → OUT), Domain Echo, closure checks; the Key log as a narrative graph. |
| `01_narrative_legibility.md` | How to build legible narrative with no runtime LLM? | PP-688 reframed as the classic NLG pipeline; the atom↔sentence answer; show-don't-tell channels; player-as-constructor; tellability. |
| `02_prior_art_and_methodology.md` | How do acclaimed games (and the literature) solve it? | Mechanism-level survey of authored CRPGs, emergent systems, and the academic lineage; transfer table to Valoria. |
| `03_articulation_nlg_architecture.md` | Architecture proposal | Factored deterministic NLG + offline bake; story sifting; pacing director; dual-register/Coherence; where it slots into PP-688. **Architecture only — no schemas/worked example.** |

## Scope & provenance

- **Architecture-only** decision document (per request). No data schemas, no worked example, no fragment content. `03_…` is drafted as a *proposed* PP-688 §11 to be lifted into `articulation_layer_v30.md` only if ratified.
- **No canonical files edited.** All four docs are new analysis.
- **Prior-art provenance:** external claims carry source URLs in `02_…`. WebFetch was 403-blocked in this environment; most external sources are WebSearch-excerpt-confidence except the two Steven Sych papers, which were read in full from user-provided PDFs. Load-bearing quotes are flagged for verbatim re-check.
