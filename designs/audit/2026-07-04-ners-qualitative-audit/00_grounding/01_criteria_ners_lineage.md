# Grounding 1 — Qualitative NERS criteria lineage + audit-format precedent

## Status: PROPOSED (audit grounding — Jordan review)
_Explorer output, 2026-07-04 planning phase (sonnet lane). Verified against the working tree at
commit `cb227cf`._

## (a) Where the qualitative NERS criteria actually live

There is **no `canon/definitions.yaml`** in the working tree (any skill citing it is stale).
`canon/02_canon_constraints.md` does not define NERS — it holds only the P-01..P-15 / GD-1..3
tables. The criteria live in two places, one superseded-informal, one currently canonical:

1. **Informal NERS acronym** (Necessary/Robust/Smooth/Elegant, sometimes N-E-R-S), used across
   `designs/audit/**` and `tests/**` (2026-04→06). Fullest surviving textual definition:
   `references/simulation_workplan_v1.md` §2.1 ("NRSE ALL-DIRECTIONS FRAMEWORK", 2026-05-10):
   - **N**: would removing M worsen gameplay? does M support a cohesive experience from all directions?
   - **R**: does M allow strategy, customization, creativity? generate emergent narrative hooks?
     fully formed and error-free?
   - **S**: integrates cleanly with interdependent mechanics? zooms across scales? transitions
     cleanly? calculations consistent with adjacent mechanics?
   - **E**: logically simple? clear approach? no unnecessary overhead? player intuits complex
     outcomes from simple choices?
   Applied along "six directions" (top-down, bottom-up, vertical, diagonal, lateral, horizontal)
   — a multi-angle qualitative audit, never a single-pass mechanical check.

2. **Current canonical vetting authority**: `references/canonical_sources.yaml` key
   `throughlines_framework` → **`references/throughlines_meta.md`** (+ `_infill`), adopted via
   **PP-672** (framework) + **PP-674** (Necessity tier + enforcement). A tiered supersession of
   NERS:
   - **N — Necessity (tier 0, Jordan-owned)**: "earns its existence if it models a real,
     load-bearing dynamic of Renaissance-era political leadership… Complexity is permitted only
     when grounded in the subject matter." Failure modes: fantasy imposition, duplicate coverage,
     edge-case mechanic, abstractable. **N-fail → flag to Jordan, never auto-reject.**
   - **Ω — Intent (tier 1)**: (a) cross-scale consequence, (b) personal transformation,
     (c) autonomous world, (d) non-dominance.
   - **Μ / М / Τ** — causal modes, structural meta-patterns, and the 41 concrete throughlines.
   - **Q — Quality (tier 5, Claude-owned; Q-fail = iterate)**:
     - **Q-robust**: three viable player approaches to any governed situation; visible/traceable
       world-state change; mechanic fires without player action; the **dramatic-legibility test**
       (whose position is at risk / what each named actor wants / what happens if no one acts
       next season — one sentence each, from game-state).
     - **Q-smooth**: composes without special-casing; methodology matches the governing
       subsystem; scale-transition + temporal behavior specified.
     - **Q-elegant**: depth from rule simplicity — core rule restatable after one reading;
       second-order consequences predictable without re-reading; external dependencies
       enumerated and justified.

## (b) Philosophy gates (canon/02_canon_constraints.md)

P-01 inseparability co-movement · P-02 monstrosity-in-the-real · P-03 rendering =
consciousness-performed · P-04 monstrosity ontological, not moral (no alignment) · P-05 three
emergence modes mechanically distinct · P-06 Threadcut beings have no layer 2 · P-07 Calamity is
rendered-side · P-08 epistemological barrier = inaccessibility · P-09 memory pulling
messy/costly/detectable · P-10 Coherence = commensurability with human-mode being · P-11
Temporal Disjunction universal · P-12 drift propagation tridimensional · P-13 forgetting =
rendering failure · **P-14 board/VG modes must express inseparability** · P-15 three-layer
being-persistence.

GD-1 Peninsular Sovereignty sole victory condition · GD-2 deterministic threat response precedes
stochastic action selection · GD-3 Revolt → Insurgency → Faction pipeline.

## (c) Experiential intent / emergent narrative

- Intent-of-game (throughlines_meta_infill §1): "a positive feedback loop between player
  decisions and mechanics/system/designs that produces an engaging game world with emergent
  narratives" — treated as necessary-but-insufficient and specialized into Ω's four clauses.
- `canon/00_philosophical_foundations.md` grounds the transformation clause phenomenologically:
  monstrous confrontation ↔ trauma-structural signature (§4.3) → Thread sensitivity (§14);
  sensitivity deepens and destabilizes engagement (§15); Coherence drift (§16) = tridimensional,
  non-moral, communally propagable transformation.
- `references/throughlines_complete.md`: NPC arcs "emerge from accumulated game state… because
  the world pushed them there, not because a writer decided it"; cross-system **collisions**
  (e.g. Tutoring+Southernmost) are "the game's emergent narrative engine" — the game's biggest
  narrative moments are structural convergences, not scripts.

## (d) Prior NERS-audit format worth reusing

`designs/audit/2026-06-29-combat-corpus-recovery/ners_audit_combat_engine_v1.md` +
`_RECONCILED.md`:
- `[SELF-AUTHORED — bias risk]` flag up front where applicable.
- **Verdict-first table** (one row per criterion, PASS/PARTIAL/STRONG/WEAK + one-line basis).
- **Severity-ranked findings** tagged `[criterion · severity]`, each with an **intent gate**
  (DELIBERATE / NOT-INTENDED / UNDETERMINED).
- Provenance tags: `[READ: file — what was verified]`, `[CONFIDENCE: …]`, `[GAP: …]`.
- **Reconciliation ledger** (claim → critique → fresh evidence → resolution).
- Bottom line = the single highest-value action.

## (e) Playability precedent

`designs/audit/workplan_v2_throughline_2026-04-26.md` §5: playability is a distinct milestone —
"can a designer read the game-state and answer 'whose position is at risk, what each actor
wants, what happens if no one acts'?" — requiring "a human and a screen," not a simulation.
`designs/audit/2026-05-08-meta-audit-immersion.md`: a system can pass N/E/R/S and still destroy
immersion "if it surfaces too much of itself to the player."
