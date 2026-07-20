# Resolution Diagnostic — 2026-05-28 Audit Batch

**Skill:** `valoria-resolution-diagnostic` (Stage 1–4 per system)
**Scope:** all 7 resolution-bearing systems flagged in skill INITIAL HYPOTHESES, run in extreme detail.
**Session token:** c93a36df1d98ea45
**Status:** Stages 1–4 complete for 4 of 7 systems (faction action layer, personal combat, threadwork, mass battle). Remaining 3 (social contest, investigation, peninsula/victory) deferred to follow-up session per context window discipline.

## File index

| File | System | Verdict | New P1 findings |
|---|---|---|---|
| `resolution_diagnostic_faction.md` + `ners_verdict_faction.md` | Faction action layer | **NON-COMPLIANT** (N pass; R, S, E fail) | F1 bare-stat-pool; F3 anti-death-spiral floor non-functional; F6 L1 collapse loop unbounded; F7 L7 Wealth-0 Mil undamped; F5 decrease>increase asymmetry; F2 conflicting Ob formulas; F8 PP-686 v2 schema drift |
| `resolution_diagnostic_combat.md` + `ners_verdict_combat.md` | Personal combat (handoff caveat held) | **NERS-COMPLIANT under resolution-fitness lens** (N pass; R pass; S partial-fail on canon drift; E pass) | C2 PP-717 D2 Pool DR not propagated; C8 deferred to open handoff (5 directions) |
| `resolution_diagnostic_threadwork.md` + `ners_verdict_threadwork.md` | Threadwork | **NERS-COMPLIANT** (N pass; R pass with gap; S partial-fail on canon contradictions; E pass) | T1 Foundations-vs-design Mending cost contradiction; T6 Knot TIER-DRIFT-001 (pre-flagged); T2/T7 secondary canon defects |
| `resolution_diagnostic_mass_battle.md` + `ners_verdict_mass_battle.md` | Mass battle | **NERS-COMPLIANT with significant backlog** (N pass; R pass; S partial; E pass-with-flag) | MB5 NO POOL FLOOR at mass scale (novel); MB1–MB4, MB9 pre-existing from 2026-04-29 audit pipeline |

## Headline findings (cross-system)

**The faction action layer is the priority remediation target.** 5 NERS-lesson findings + 2 canon defects, all P1. Bare-stat pool resolves pivotal/irreversible Domain Actions at floor pools (Guilds Mil 2 = 2D vs TN 7 → P=0.16); designed anti-death-spiral floor is mathematically inactive (caps Ob at 4 but pool stays 2D, P≈0); L1 collapse loop terminal-unbounded (Stab=0 = termination not bound); L7 Wealth-0 cascade undamped on Military dimension.

**Personal combat is in materially better shape than the faction layer** — by deliberate work. PP-717 D1/D2/D3 ratifications implement Lesson 2/3 explicitly: Pool DR above Agi 4, Pool floor 5, MW cap 3, crit threshold ≥4. The remaining issue is **propagation** — PP-717 D2 ratified in audit but not yet pushed to combat_v30 / params/combat (C2). Skill INITIAL HYPOTHESES "wound at 5D floor (Lesson 2 candidate)" resolves as a **trade-off, not a violation** — the floor IS the Lesson-3 safeguard. C1 re-test confirms: removing the floor to "fix" L2 non-uniformity at floor re-introduces small-pool death spiral.

**Threadwork's core compliance is foundational.** Coherence as continuous resource passes Lesson 6 (intended multi-thresholds per canon/01 Amendment 3, second-clause exempt). P-01 mandatory tri-dimensional co-movement (the "doubly critical" intent_of_game engine loop) is doubly safeguarded (Coherence + RS + Substrate Saturation + Gap self-closure). The headline finding (T1) is a direct **Foundations-vs-design-doc contradiction**: canon/02 Amendment 3 states "Mending's Coherence cost is zero" but threadwork §3.2 lists "Mending | −1". Per project hierarchy Foundations supersedes; §3.2 is stale. One-row fix with significant downstream implications for the Edeyja Mending capability.

**Mass battle is well-bounded by state machine.** The 2026-04-29 audit trio already produced a comprehensive consistency stress-test with 8 auto-approvable patches + 8 Jordan decisions + 27 PROVISIONALs. My role this turn was cross-check + novel-finding surface. The novel finding (MB5) is the asymmetry: mass battle has **no Pool Floor** unlike combat (5) and threadwork (5). The implicit floor is unit deletion (Size→0) — architecturally legitimate but legibility-weak. Three remediation options surfaced; Jordan-decision.

## Cross-system patterns

1. **Pool Floor pattern.** Combat and threadwork share Pool Floor 5 as Lesson-3 architectural safeguard. Faction layer has no floor → F1/F3 P1s. Mass battle has no floor → MB5 (mitigated by unit-deletion-as-floor by design).
2. **Decrease>Increase asymmetry pattern.** Faction F5 (5 Stab triggers down vs +1/clean season) shares shape with mass battle MB7 (8 Morale triggers vs +1/Reform). In both, recovery surface broadening (DECISION-MB-03 reset; faction F5 add per-faction stabilization action) is the L5 remediation.
3. **Cross-scale loops.** L1 (combat→faction Trigger 5) and L7 (Wealth-0→Mil cascade) both originate at faction layer; combat-side and mass-battle-side participation is properly gated. Faction-side defects (F6, F7) propagate to cross-scale through the gate; faction-side remediation fixes the cross-scale.
4. **Canon contradictions block S.** Multiple systems have S-FAIL findings rooted in canon-vs-canon disagreement (faction F2, F8; combat C2, C3, C6; threadwork T1, T2, T6, T7). These are propagation/synchronization defects, not mechanical-design defects. Most have a clear authority (Foundations > design > params; audit-ratification > pre-audit doc); propagation work clears them.

## Editorial ledger candidates (staged, not committed — B6 branch protection)

12 candidate entries inline-staged across the 4 verdicts. Summary:

| ID (when assigned) | Type | Severity | System | Source |
|---|---|---|---|---|
| Faction | conflicting Ob formula | P1 | F2 |
| Faction | PP-686 v2 schema drift | P1 | F8 |
| Combat | PP-717 D2 propagation | P1 | C2 |
| Combat | STR multiplier ambiguity | P2 | C6 |
| Combat | OOB-Floor interaction | P2 | C3 |
| Combat | Health super-linear at low End | P2 | C5 |
| Threadwork | Foundations-vs-§3.2 Mending cost | P1 | T1 |
| Threadwork | Knot TIER-DRIFT-001 (pre-flagged) | P1 | T6 |
| Threadwork | FR Coherence surcharge | P2 | T2 |
| Threadwork | COMPOSURE-DRIFT-001 (pre-flagged) | P2 | T7 |
| Mass Battle | No Pool Floor at mass scale (NOVEL) | P1 | MB5 |
| (mass battle pre-existing) | various | mixed | MB1–4, MB9 | 2026-04-29 audit pipeline (separate batch) |

## Departures from skill INITIAL HYPOTHESES (cross-system)

| System | Skill hypothesis | Actual finding |
|---|---|---|
| Faction action layer | "Likely non-compliant, priority target (worked example)" | **CONFIRMED.** Worked-example math holds at canon; 5 NERS findings + 2 canon defects |
| Personal combat | "Likely mostly compliant; watch the flat −1D wound at the 5D floor (Lesson 2 candidate)" | **REFRAMED** — L2 non-uniformity at floor is the trade-off price for L3 floor working. Confirmed via C1 re-test (hypothetical fix FAILS — re-introduces small-pool death spiral) |
| Threadwork | "Likely compliant for operations; Coherence is a depleting resource — validate Lessons 2 and 6" | **CONFIRMED at lesson level**; T1 Foundations contradiction surfaced as headline (not predicted by skill) |
| Mass battle | "Likely compliant, well-bounded spiral: small pools exist but the state machine carries the weight" | **CONFIRMED.** MB5 novel finding (no Pool Floor) is architectural-detail-not-predicted; everything else PASS or already-in-prior-audit |

## Remaining work (deferred to follow-up session)

Per skill INITIAL HYPOTHESES:
- **Social contest** — likely compliant, healthy contested case (5–18D pools). Skill-predicted PASS; targeted read needed for confirmation.
- **Investigation / fieldwork** — likely compliant: deterministic five-filter chain owns decisions; dice only feed Evidence clock.
- **Peninsula / victory** — likely compliant: deterministic clocks, no dice.

Context window discipline: turn-by-turn detail at this level converges to ~3 systems before approaching escalation band. The remaining 3 are skill-predicted PASS, so a tighter batch turn covering all 3 at substrate + spot-check level is appropriate.

## Confidence calibration (cross-batch)

`[CONFIDENCE: high]` — for all worked-example math validations (F1 dice probabilities, C2 audit-vs-canon drift, MB5 floor pool math, T1 Foundations-vs-design contradiction text comparison)

`[CONFIDENCE: medium]` — for resolution-status verification of 2026-04-29 mass battle audit findings (commit-log scan not performed)

`[CONFIDENCE: low]` — for the precise dice probabilities in faction layer at stat ≥ 3 until F2 (conflicting Ob formula) resolves which formula applies

**Citations:** all mechanical claims cited inline per `[READ:]` trail discipline. See individual files for full reads.
