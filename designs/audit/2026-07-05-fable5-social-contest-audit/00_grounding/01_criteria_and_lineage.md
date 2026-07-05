# Criteria and Lineage — what this audit judges against

## Status: RATIFIED — 2026-07-05 (PR #80 merge + Jordan post-merge instruction 'Ratify all'; ED-1094 merge-ratifies convention). D6 sequencing adopted; candidates filed as ED-SC-0002..0010 + ED-IN-0012..0013 (see ed_options.md ID map).
## Date: 2026-07-05

## 1. Two NERS definitions (both applied, kept distinct)

**(a) Rolling-engine NERS** — `skills/valoria-resolution-diagnostic/SKILL.md`.
Necessary / Robust / Smooth / Elegant, verdicted on a *rolling engine* against five properties:
P-i legible odds, P-ii uniform/in-band leverage, P-iii bounded+monotonic response, P-iv graded/
recoverable output, P-v right engine for the pool regime. Social contest is **Instance A**
(σ-leverage continuous engine, healthy pools ~5–18D). Prior verdicts: NERS-COMPLIANT
(`designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_social_contest.md`), confirming the
2026-04-08 simulation-clean audit. Applied here only as an **annex re-check** (D2): has the
Stage 1a–3 rebuild (σ-kernel unification, armature δσ) invalidated any prior P-i..P-v basis?

**(b) Qualitative / North-Star NERS** — `references/throughlines_meta.md` (PP-672/674), the
framework PR #77 used and the primary lens here (D2). Tiers:

| Tier | Owner | Test |
|---|---|---|
| **N** — Necessity | Jordan (flag-never-reject) | does the subsystem earn its complexity? |
| **Ω** — Intent (4 clauses) | — | (a) cross-scale consequence, (b) personal transformation, (c) autonomous world, (d) non-dominance |
| **Μ** — 4 causal modes / **М** — 11 meta-patterns / **Τ** — 41 throughlines | — | is the subsystem a live limb of the declared causal spines? |
| **Q** — Quality | Claude (Q-fail = iterate, not reject) | Q-robust / Q-smooth / Q-elegant, incl. the dramatic-legibility test |

## 2. Playability bars (D4)

- **Dramatic-legibility three-question walk** (`designs/audit/workplan_v2_throughline_2026-04-26.md §5`,
  the canonical bar): from readable game-state, answer *whose position is at risk / what each actor
  wants / what happens if no one acts*.
- **Cognitive-load ceilings** (`designs/audit/2026-05-08-meta-audit-immersion.md`): 3–4 per-decision
  consultations for personal scenes; a system can pass N/E/R/S and still destroy immersion.
- **Legibility contract** (`designs/audit/2026-07-01-contest-player-interaction/`
  `player_interaction_walkthrough_v1.md §0`, DRAFT, Agôn-only): "every number the resolver uses is a
  number the player can see before committing"; hidden values must degrade to a consequence class.
- Context: PR #77 F-3 — the playability bar "has no maintained home"; UI spec v4.1 is stale/contaminated.

## 3. Throughlines in scope (D3)

From `references/throughlines_complete.md` (throughline = "a causal spine connecting 3+ systems…
mechanical chains that the engine must implement"):

- **T-03 Inseparability** — temporal-axis conflict penalty fires in social contest (P-01/P-14 co-movement).
- **T-14 Conviction as Moral Architecture** — Piety Track, Composure.
- **T-17 Companion as Moral Mirror** — Solidarity Resonant Style.
- **T-23 NPC Arc Emergence** — Composure/Piety Track feed.
- **T-24 Convergence Markers** — the "emergent narrative engine"; PR #77 F-2: that engine has no engine.

Meta layer: М-1..М-11 patterns under modes Μ-α (pressure-as-engagement) / Μ-β (autonomous-agent
composition) / Μ-γ (substrate ontology) / Μ-δ (cross-scale consequence).

## 4. Philosophical bars (D2/D3/D5)

- **P-14** (board/VG modes must express inseparability) — the direct bar: thread junctures
  `social_contest_v30.md §9.3–9.4b` vs the rebuilt kernel.
- **P-01** (three dimensions co-move) — underlies the same junctures and T-03.
- **P-03** (rendering = consciousness-performed) — no neutral engine narrator; outcome presentation
  routes through a chronicler/perspective.
- **P-10/P-12** — Coherence/drift effects of in-contest Weaving (R-65) must be tridimensional.

## 5. Interaction-surface specs (D5)

- **Domain echoes:** `designs/architecture/scale_transitions_v30.md §5` (trigger/amount/timing caps,
  §5.4 Debate→Domain Echo PP-108, §5.5 Accord, §5.6 Thread) × `designs/scene/social_contest_v30.md §6`
  (Memory win → Mandate +1; Projection win → +1D first Domain Action; Compromise → none;
  §6.1 Obligations as the second transport channel).
- **Narrative emergence:** `skills/valoria-arc-generator/SKILL.md` (arc discipline: "no single player
  decision caused this"); T-24 convergence markers (`references/arcs/arc_register_events.md §VI`);
  the `tests/emergent_arc_skeleton_test_*` prose corpus (design intent, **not** behavioral contract —
  CLAUDE.md §3).
- **Prose:** `skills/prose-writer/SKILL.md` — the **Ratchet Principle** (political scenes never resolve
  as mutual accommodation; the space between principals narrows), chronicler focalization (4 voices,
  P-03), "prose can gesture at systems without exposing numbers", Solmund-voice override for
  ecclesiastical speech.

## 6. Verdict idiom

Each dimension closes with `**PASS / PARTIAL / PARTIAL FAIL / FAIL (flag n)** — one-line basis`,
mirroring PR #77 §0, plus an evidence table with working-tree citations. Severity P1–P3 and novelty
tags follow PR #77's vocabulary.
