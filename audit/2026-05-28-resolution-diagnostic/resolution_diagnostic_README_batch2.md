# Resolution Diagnostic — 2026-05-28 Audit Batch 2 (closeout)

**Skill:** `valoria-resolution-diagnostic`
**Companion:** `resolution_diagnostic_README.md` (batch 1: faction / combat / threadwork / mass battle)
**This batch:** social contest / investigation / peninsula-victory — the 3 systems skill INITIAL HYPOTHESES predicted clean PASS.

## File index (batch 2)

| File | System | Verdict |
|---|---|---|
| `resolution_diagnostic_social_contest.md` + `ners_verdict_social_contest.md` | Social contest | **NERS-COMPLIANT** — confirms prior 2026-04-08 audit "simulation-clean" |
| `resolution_diagnostic_investigation.md` (Stages 1+3 consolidated) | Investigation / fieldwork | **NERS-COMPLIANT** — exemplar Lesson-4 routing |
| `resolution_diagnostic_peninsula_victory.md` (Stages 1+3 consolidated) | Peninsula / victory | **NERS-COMPLIANT** — deterministic clocks, no dice |

## Cross-batch summary — all 7 systems

| # | System | Verdict | Lesson-level findings |
|---|---|---|---|
| 1 | Faction action layer | **NON-COMPLIANT** | 5 P1 NERS (L3 bare-stat-pool, L3 floor-non-functional, L5 collapse loop, L5 Wealth-Mil cascade, L5 asymmetry) + 2 P1 canon defects |
| 2 | Personal combat | **COMPLIANT** (handoff caveat) | 1 P1 canon drift (PP-717 D2 propagation); L2/L3 trade-off explicitly accepted |
| 3 | Threadwork | **COMPLIANT** | 1 P1 Foundations-vs-design contradiction (Mending cost); 1 P1 Knot TIER-DRIFT (pre-flagged) |
| 4 | Mass battle | **COMPLIANT with backlog** | 1 P1 novel (no Pool Floor) + 5 P1s pre-existing from 2026-04-29 audit |
| 5 | Social contest | **COMPLIANT** | 0 P1; 3 P2 pre-flagged from 2026-04-08 stress test, post-patch status unverified |
| 6 | Investigation / fieldwork | **COMPLIANT** | 0 new; T6 Knot inheritance only |
| 7 | Peninsula / victory | **COMPLIANT** | 0 new; MB2/MB3 inherited (peninsula-side of cross-system gaps) |

**Aggregate verdict:** Valoria's resolution architecture is **broadly NERS-compliant**, with the faction action layer as the single non-compliant system requiring substantive mechanical remediation. All other systems are compliant or compliant-with-canon-cleanup. Pool Floor pattern (combat 5, threadwork 5) is the cross-system L3 architectural safeguard; absence of Pool Floor in faction and mass battle produces the two novel findings of this batch (F1 family in faction, MB5 in mass battle).

**Cross-system patterns confirmed across all 7:**
1. **Pool Floor architectural pattern** — combat / thread have it; faction / mass battle / social do not. Each non-floor system has a different substitute: faction (none — defect), mass battle (unit deletion), social (exit-not-floor via Spent state).
2. **Decrease > Increase asymmetry pattern** — appears in faction (Stab), mass battle (Morale), partially in threadwork (Coherence). Where damped by recoverable arc (threadwork) or session reset (mass battle MB7 remediation), PASS. Where unrecoverable (faction L1 terminal collapse), FAIL.
3. **Cross-scale loop participation** — combat → faction Trigger 5, mass battle → faction Trigger 5, Coherence → RS world track. All cross-scale loops are properly gated; the defects are at the layer-of-origin (faction layer carries the L1/L7 defects).
4. **Canon-coherence as S limiter** — across faction (F2, F8), combat (C2, C3, C6), threadwork (T1, T2, T6, T7), mass battle (MB1-4, MB9), social (SC3-5 status unverified). These are propagation/synchronization defects, not mechanical-design defects. Foundation-grounded canon (P-01-P-15, Amendments) takes precedence; design docs and params files lag by editorial-cycle delays.

## Remaining items aggregated

- **Editorial ledger candidates staged:** 13 entries total across batches (12 in batch 1, 1 in batch 2 social SC1 architectural note). All pending Jordan ratification + commit to canon/editorial_ledger.yaml as separate batch operation.
- **Open Jordan decisions:** 8 from mass battle 2026-04-29 audit (DECISION-MB-01..08) + 3 from social pre-flagged P2s (SC3-5 verification) + 3 from threadwork (T1 row update / T6 tier option / T2 surcharge ratification) = ~14 decisions to ratify.
- **Pool Floor consideration:** if Jordan adopts faction-side F1/F3 remediation (e.g., aggregate NPC pool +2), the architectural pattern strengthens. MB5 architectural choice (no Pool Floor for mass battle) is then more deliberate-by-contrast.

## Confidence calibration (full batch)

`[CONFIDENCE: high]` — across all systems for findings cited inline with `[READ:]` trail; math validations verified against canon

`[CONFIDENCE: medium]` — for items requiring verification of patch status between historical audit dates and 2026-05-28 (no commit-log scan performed this batch)

`[CONFIDENCE: low]` — only for: faction probabilities at stat ≥ 3 until F2 resolves Ob formula; SC3/SC4/SC5 status

**All 7 systems audited.** Resolution diagnostic batch complete.
