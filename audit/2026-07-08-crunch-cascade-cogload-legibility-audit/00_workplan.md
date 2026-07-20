# Crunch-Cascade / Cognitive-Load / Legibility Audit — Workplan

**Date:** 2026-07-08
**Requested scope:** "a mechanical crunch cascade / cognitive load / legibility audit throughout all active systems and subsystems."
**Status:** COMPLETE — findings below, adversarially verified.

## Method

This audit is a fresh cross-system pass, not a rerun of an existing skill pipeline. It draws
methodology from two precedents already in the corpus:

- `tests/audit/audit_phase3_crossmode_cogload.md` (2026-04-04) — first corpus-native
  cognitive-load scoring (decisions/round × tracked vars) and crunch-cascade check, now three
  months stale (pre-v40, uses retired terminology).
- `designs/audit/2026-07-04-ners-qualitative-audit/01_workings/lenses/lens_playability_legibility.md`
  (2026-07-04) — a recent, still-largely-current cross-scale tracker count and dramatic-legibility
  walk, folded into the NERS qualitative audit and ratified.

Rather than rerun either wholesale, this audit re-establishes each subsystem's *current* (v40,
post-2026-07-05) state per `CURRENT.md`, and for each active subsystem produces:

1. **Tracker inventory** — every named numeric/state track a player or engine must hold, with
   file:line provenance and player-visibility.
2. **Interaction chain map** — upstream/downstream per mechanic; flags for circularity, dead
   ends, unconnected mechanics, amplification loops, and missing interaction rules.
3. **Cascade check** — any chain ≥3 links with no return path or unproven bound.
4. **Cognitive load** — decisions and simultaneously-consulted trackers per typical decision
   point, benchmarked against the corpus's own stated ceilings (2026-05-08 immersion audit: 3–4
   consultations for personal scenes, 7 at ceiling for strategic).
5. **Legibility gaps** — hidden values, inconsistent derived-stat definitions, untranslated
   jargon, missing/stale UI models — rated P1 (blocks play/engine-buildability) / P2 (causes
   ambiguity) / P3 (polish), per the `valoria-mechanic-audit` skill's severity convention.

## Scope — subsystems audited

Per `CURRENT.md`'s subsystem table (2026-07-08 reconcile):

| # | Subsystem | Canonical head(s) audited |
|---|---|---|
| 1 | Personal / scene combat | `designs/scene/combat_engine_v1/` |
| 2 | Mass battle | `designs/provincial/mass_battle_v30.md` + `mass_battle_integration_v30.md` + `tests/sim/mass_battle/*.py` |
| 3 | Social contest | `designs/scene/social_contest_v30.md` + `sim/personal/contest/` |
| 4 | Faction / political | `faction_canon_v30.md` + `faction_layer_v30.md` + `faction_behavior_v30.md` + `faction_state_authoring_v30.md` |
| 5 | Settlement / territory | `designs/territory/settlement_layer_v30.md` (+ adjacency/temperaments) + `governance_play_redesign_v1.md` (PROPOSAL) |
| 6 | Threadwork | `designs/threadwork/threadwork_v30.md` + `thread_horizontal_integration_spec.md` + `params/threadwork.md` |
| 7 | Board game + dice/resolution core | `params/board_game.md` + `params/bg/*` + `params/core.md` |
| 8 | Articulation + NPC behaviour | `designs/articulation/articulation_layer_v30.md` + `designs/npcs/npc_behavior_v30.md` |
| 9 | Cross-scale propagation/aggregation architecture | `designs/architecture/propagation_spec_v1.md` + `holonic_container_doctrine_v1.md` |

Each was audited by an independent sonnet-tier agent (per CLAUDE.md §10 model tiering — mechanic
audits are sonnet-tier work), then adversarially verified by an independent opus-tier critic agent
instructed to re-open every citation, actively hunt for overstatement/staleness/refutation, and
issue a per-finding verdict (CONFIRMED / PARTIALLY-CONFIRMED / REFUTED / NEEDS-RATING-CHANGE),
per CLAUDE.md §10's "agonist→antagonist is a relay" pattern (critic never saw the producer's
reasoning, only its conclusions — independence by construction).

## Deliverables

- `01_findings_<subsystem>.md` × 9 — per-subsystem findings, corrected per adversarial verdict.
- `02_synthesis.md` — **primary deliverable.** Cross-system cascade peaks, a ranked cognitive-load
  table, the consolidated P1/P2/P3 legibility register, and recommendations.

## Adversarial-pass outcome, in brief

Of the ~200 discrete findings across all 9 subsystems: the large majority (~85%) survived
verification as-is. The critic passes caught and corrected: 2 severity downgrades (P1→P2, both
where a "live defect" framing ignored a deprecation banner or an already-ratified deliberate
staging decision), 1 full refutation (a threadwork finding overtaken by a same-day unrelated
commit), 1 arithmetic slip, several currency staleness issues (findings framed as "open/needs
Jordan" that had in fact already been ratified-as-accepted 2026-07-05, just not yet executed),
and a handful of mis-citations (right conclusion, wrong line number). No finding's core substance
was overturned by verification. See `02_synthesis.md` §0 for the full disposition ledger.
