# Scene Combat + Contest! Audit Decisions
**Date:** 2026-05-17
**Scope:** Scene combat (Agility-OP) + Contest! (open balance items + jargon rename)
**Session:** Opus 4.7 audit, ratified by Jordan 2026-05-17

## Context

Audit triggered by user observation that scene combat had an ability "too powerful" (later clarified: Agility-OP). Question expanded to "pull all systems and critique them against d10/TN/obstacle paradigm," then scoped back to deep audit of scene combat + Contest! per user election (Option A).

Continuous engine (ED-833, 2026-05-15) already canonical for Godot — d10 paradigm retired at math layer. Structural inheritance (pool grammar, TN tiers, Ob, degrees) carries forward; that is the audit's actual subject.

## Decision 1 — Combat: C4 direction set (formerly proposed C2 + C4)

Combat Pool single-attribute defect mechanically traced to `params/combat.md`:
> Combat Pool = (Agility × 2) + Relevant History + 3, min 5

Phase 8 (ED-838): "~100% Fast cond win at 17D vs 11D in skilled-vs-skilled play. Pool size determines outcome at large gaps; action triangle modifies magnitude but does not invert dominance."
Phase 10 (ED-839): "Even with all corrections and reforms, Fast vs Titan finishes at 70/30."

**Direction set: C4 (stance + interaction-type system, BattleCON-modeled).** C2 (weapon-keyed primary attribute) deferred as fallback.

**Caveat:** pure Contest!-style stance import does NOT fix Agi-OP standalone (pool-vs-pool net-success comparison still favors larger pool). C4 must be BattleCON-strength — stance counters that bypass pool comparison via fixed pool-reduction effects, defense bypass, or non-pool resolution properties.

**Resolves open question from ED-838:** Reframing 2 (niche dominance by attribute) accepted *with softening* — Agi-build retains scene-combat advantage at meaningful magnitude, not ~100%; cross-system niche sims required (Phase 11+).

## Decision 2 — Contest!: ED-295 (Head-On stalls) → Option D

Audience resistance erodes per exchange. Long contests resolve organically.
Pattern: Slay the Spire stacking debuff / Combat Commander Recovery.
Spec: TBD via params/contest.md edit. Magnitude TBD via sim or playtest.

## Decision 3 — Contest!: ED-296 (Echo Match negative movement) → floor fix

Apply `max(0, (margin − 1) + Cha modifier − Foc defence)` floor to REINFORCE → Echo Match resolution.
Pure bug fix, not design. Ships in next contest.md commit.

## Decision 4 — Contest!: ED-297 (Coalition Push magnitude) → accepted

Coalitions mechanically dominate solo advocacy by canonical design — reflects parliamentary politics. ~5 track movement/exchange vs solo ~0 is canonical, not bug. No tuning required.
ED-297 closed.

## Decision 5 — Infrastructure: M3 + print_status_block hook drift filed

`h.completeness_gate` specced in architecture V2.3 but unimplemented in `valoria_hooks.py`.
`g.print_status_block` referenced in PI `<bootstrap_script>` but unimplemented in `github_ops.py`.
M2-M3-M4-M5 enforcement framework cannot operate while these are missing.

Until landed: manual attestation substitutes (this session demonstrated the pattern).
Infrastructure task; not blocking design work but blocks audit-process maturity.

## Decision 6 — Contest! jargon → plain-English rename

| Old (canonized) | New (replaces) |
|---|---|
| Memory (genre) | Past |
| Projection (genre) | Future |
| Revealing (orientation) | Direct |
| Obscuring (orientation) | Indirect |
| Precedent (style) | Cite Precedent |
| Suppression (style) | Bury Precedent |
| Vision (style) | Propose Vision |
| Insinuation (style) | Imply Consequence |
| CLASH | Head-On |
| REINFORCE | Echo Match |
| CROSS | Cross-Time |
| AMPLIFY | Coalition Push |
| Doubt Marker | Suspicion Token |

Doc propagation: next commit (contest.md + social_contest_v30).

## Audit Coverage Attestation

**Direct reads this session:**
- params/combat.md (full)
- params/contest.md (full)
- designs/scene/combat_v30 (index + infill)
- designs/scene/social_contest_v30 (index + infill)
- params/core.md (full)
- canon/02_canon_constraints.md (full)
- canon/00_philosophical_foundations_rules.md (full)
- designs/personal/character_generation_questionnaire_v30.md (full)
- references/canonical_sources.yaml (full)
- session_log_current.md (full)

**Not read directly (transitive citations only):**
- `tests/sim/phase8_smart_ai_v2_2026-05-15.md` — Phase 8 magnitudes cited via params/combat.md embedded summary
- `tests/sim/phase10_str_stam_reform_2026-05-16.md` — Phase 10 cited same way
- `designs/audit/2026-05-14-balance-audit/integration_plan_v3_2026-05-15.md`
- Integration engine `mc_v17.py`

Phase 8 + Phase 10 sim reports should be read directly during the BattleCON study (next task) to close the transitive-citation gap.

## Next Actions

1. **T6:** doc propagation commit — rename + math fixes in params/contest.md and social_contest_v30 (index + infill).
2. **T7+:** BattleCON study — mechanic-extraction memo, C4 draft spec, Phase 11 sim plan. Include direct Phase 8/10 reads.
3. **Open for later:** cross-system niche dominance sims (Phase 11+) to validate Reframing 2; tools/index_gen.py M6 rewrite; M3 + print_status_block hook implementation.
