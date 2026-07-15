# Grounding 2 — The prose/render stack (modulation axes, runtime socket, the NLG proposal)

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
_Explorer output, 2026-07-05 planning phase (sonnet lane), verified against the working tree._

## (a) The prose-writer's "layers of change"

`skills/prose-writer/SKILL.md` — a single-voice synthesis of twelve authors, workflow: skeletons
→ PC Coherence tier + TS + Spirit → Solmund Voice canon if ecclesiastical → focalization
(chronicler-mode requires one of four canonical chroniclers, P-03) → beats with cliché-risk
flags → write → audit. Four orthogonal modulation axes:

1. **Coherence** = the author-weighting ladder (`references/coherence-tiers.md`, tied to
   `threadwork_v30 §3.3` bands 10-8 Stable / 7-5 Dissonant / 4-3 Fragmented / 2 Fractured /
   1 Severed / 0 Rendering Crisis): 2D weight tables (Author × TS band) per tier — e.g. Tolkien
   26% → 5% and Lispector 0% → 18% across the descent. Degradation is *calibration-drift of the
   rendering*, "not broken prose."
2. **Spirit** (audible at Coherence ≤4): High Spirit → "Beckett continuation" (will grips;
   closes on the verb — "she walks"); Low Spirit → "Lispector dissolution" (body replaces
   agent; closes on the noun — "the feet move"). Worked in `references/three-axis-test.md`.
3. **Certainty** = register/vocabulary substitution for religious content
   (`designs/world/solmund_voice_v30.md §18` table: 1-2 plain-speech rejection → 3 faith-as-
   habit → 4 folk inhabitation → 5 the-world-is-evidence → 6+ w/ TS30+ mystical encounter) +
   **chronicler selection** (Church Cert-5 / Hafenmark Cert-4 / Restoration Cert-2 / Warden
   Cert-0-TS70+). Canon overlay independent of PC coherence; the PC's *rendering of* it degrades.
4. **TS** gates substrate-perception depth (Borges/Lem weights).

## (b) The articulation runtime socket

`designs/articulation/articulation_layer_v30.md` (PP-688, CANONICAL, Stage-10 sim-validated):
Tier 1 always-on protagonist lens (Concern queue, Memory salience, Bonds/Knot/Belief,
Chronicle search) · Tier 2 trigger-fired 5-15s cut scenes ("not authored") · Tier 3 annual
omniscient chronicle. Extension points: **§3.1** 10-trigger table (any match fires);
**§3.2** `significance = stakes(1-5) + protagonist_alignment(0-3) + cascade(0-2) +
accumulated_weight(0-3)` → 5s/10s/15s tiers; **§3.3** per-actor `unarticulated_weight`
starvation accumulator (reset on feature); **§5** the single deterministic callback
`on_key_emitted_articulation(key)` → `emit_cut_scene(key, sig)` — the socket a realizer fills.

## (c) The already-proposed deterministic realizer (graduate, don't reinvent)

`designs/audit/2026-06-28-narrative-state-articulation/03_articulation_nlg_architecture.md`
(PROPOSAL, drafted as future PP-688 §11): slot-templates × register/lexicon overlay (frozen
**X/Y/Z quadrant grammar: X=Coherence, Y=TS, Z=Spirit**) × focalizer overlay (4 chroniclers +
protagonist) × discourse grammar, composed at runtime from an **offline LLM bake** (§8: the
prose-writer generates and freezes fragment + lexicon pools per (Key-type × X/Y band ×
focalizer); runtime only selects/substitutes/splices — "the no-LLM way to produce the
coherence-indexed voice"). §5: high-Coherence selects clean lexicon; low-Coherence applies
authored degradation rules — rendering failure is a register selection *inside the realizer*.
Companion: `01_narrative_legibility.md` (quotes `videogame_mode_spec.md §0`: "the engine
narrates" — no runtime LLM). A third state→presentation spec exists in `valoria_ui_ux_v4_1.md`
§9.7 (UI corruption ladder per Coherence band — structural analogue).

## (d) Mechanical definitions of the two modulation stats

- **Certainty** (`params/core.md` §Certainty Track, PP-551): 0-5 oscillating transformation
  track (5 Orthodox … 0 Accepted), both poles stable; mechanical effects at each pole (±D in
  Church contexts, Coherence-loss nullification, TS growth, arch-heretic class). Independent of
  Coherence and TS.
- **Coherence** (`threadwork_v30 §3.1-3.3`): 10→0; canonical band table §3.3 (the exact ladder
  the prose tiers key to); cross-coupling at Coherence 2 (caps Certainty ceiling). §3.7 = the
  four ED-681 Rendering-Crisis beats (Withdrawal / Knot Anchoring / Place Anchoring / The
  Choice) — the exemplar of authored beats with mechanical triggers; C6 requires these render.

## (e) Named gaps (the design's Q4 work)

1. **Template/slot schema + worked example**: PP-688 §4.5 says only "templates per Phase 5a";
   no data schema, fragment format, or worked example exists anywhere (incl. Godot skeleton).
2. **Bake protocol unbuilt**: granularity, count budget, storage location open (§8/§10).
3. **Runtime-executable form of the two authoring tables** (coherence-tiers weights; §18
   Certainty registers) unspecified.
4. **Pacing director deferred** (articulation §7, D11) — no governor of WHEN Tier-2/3 beats
   surface vs a tension curve; §7 of the NLG proposal sketches a RimWorld-style director,
   unbuilt.
5. **Oatmeal/coverage risk named, unresolved** (NLG §9) — no Expressive Range Analysis.
6. **Texture-between-cut-scenes** unspecified (2026-05-08 immersion audit: cut scenes are
   "interruption-moments," not connective tissue).
