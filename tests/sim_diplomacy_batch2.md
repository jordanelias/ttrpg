# Unique Scenario Stress Test — Diplomacy Batch 2 + Interdependency Analysis
## Session: 2026-04-09 | Scope: Post-PP-512–524 new scenarios + interdependency chains
## Patches from this session: PP-525–528 | Remediation: PP-512–524 register + pbg blocks

---

## FETCH LOG
- references/params_board_game.md: ✓ 1576 lines (pre-remediation live)
- references/params_factions.md: ✓ 565 lines
- designs/board_game/victory_architecture_v1.md: ✓ 472 lines
- canon/patch_register.yaml: ✓ 4829 lines

---

## SESSION CONTEXT: REMEDIATION
Last session's commit wrote params_board_game.md patch blocks using PP-500–512 numbering,
but PP-506–511 were already taken by Graduated Seizure patches. The live file was 1576 lines
(not the 1780 expected). Remediated: diplomacy patches renumbered PP-512–524, all missing
blocks re-applied to params_board_game.md, patch register corrected.

---

## UNIQUE SCENARIO TESTS — BATCH 2

### Scenario 8 — Coalition Pivot: Military Compact + Crown Treaty
**Setup:** Varfell (Mil 5) + Löwenritter (Mil 6) Military Compact active, Named Enemy = Church.
Crown offers Varfell Treaty (PP-512, Ob 2). Treaty forms.
**Question:** Does Treaty dissolve Military Compact?
**Finding:** CLEAN. Compact dissolves only on Legionary targeting the other partner. Senator Outward (Treaty) is not Legionary. Instruments are independent. Crown Treaty + Compact coexist. No bleed-over.

### Scenario 9 — Pledge-Treaty Interaction
**Setup:** Varfell Open Pledge "no Spy in T1." Crown-Varfell Treaty forms (Partial). Varfell spies in T1.
**Finding:** Treaty not broken (Spy is Intel, not territorial challenge per Scenario 3 ruling). Pledge IS broken → Sta −1 + CB to all witnesses.
**New gap P2:** Crown-break trigger undefined — does Crown playing Legionary into Treaty partner territory constitute "breaking" Treaty? PP-523 describes consequences but not trigger.
**Patch PP-525:** Crown breaks Treaty by: (a) Legionary targeting partner's held territory, or (b) explicit Phase 1 dissolution declaration.

### Scenario 10 — Diplomatic Alignment Cascade
**Setup:** Church (Inf 6) + Hafenmark (Inf 5) — Diplomatic Alignment active. Alignment grants +1D Diplomacy + "shared Parliamentary motion."
**Finding P1:** "Parliamentary motion" is undefined — effect inoperable without definition.
**Analysis:** (a) Parliamentary Manoeuvre = Hafenmark-specific, Church can't use it; (b) free Senator play = any faction, complex; (c) same-side voter effect = no action spend, thematically correct.
**Patch PP-526:** "Shared Parliamentary motion" = once per season during a Parliamentary Session, Church and Hafenmark count as same-side voters regardless of declared votes. No action spend. Declared at Session start, public.
**Probability:** Hafenmark Diplomat with Alignment +1D vs Church Mandate 5 (Ob 3): 47% (was 38%). +9% from coalition.

### Scenario 11 — Thread Stewardship + Co-Victory
**Finding:** CLEAN. Coalition grants Ob bonuses only; co-victory conditions are stat/track thresholds unaffected by coalition. Coalition aids path (RS maintenance) but doesn't satisfy conditions directly.

### Scenario 12 — Multi-CB Season
**Setup:** Varfell and Löwenritter both hold CB vs Crown, both use them same Phase.
**Finding:** CLEAN. PP-519 cap is per holding faction, not per target. Both CBs legal. Coordinated CB storm is the legitimate payoff for sustained diplomatic pressure. Not degenerate.
Varfell (Mil 4, Ob 2→1 with CB): 75% success. LW (Mil 6, Ob 2→1): 84% success.

### Scenario 13 — Closed Pledge + Resentment Loop
**Setup:** HF breaks Closed Pledge (vote No to block motion). Gain: +1 Standing + Resentment. Cost: Sta −1, PI −1, CB to all witnesses.
**Finding:** CLEAN. Breach is almost never worth it for Hafenmark (PI dependency). Good design.
**New gap P2:** "Witnesses" for Closed Pledge revelation ambiguous — present at making (private, no witnesses) or at revelation?
**Patch PP-527:** Witnesses = all factions at the Accounting where revelation occurs.

### Scenario 14 — Diplomatic Token + Alignment Timing
**Finding:** CLEAN. If Alignment is active at Phase 1, +1D applies to Hafenmark's Diplomat Card roll in Phase 4. Timing is unambiguous. Alignment is a coalition state, not triggered by the card.

### Scenario 15 — Crown Treaty Period Expiry + Victory Check
**Setup:** Treaty formed Season 12, 4-season period. Season 16 Year-End Accounting step 12 fires. Is Treaty active for the step-12 check?
**Finding P2:** Treaty lapse timing within Accounting undefined. Crown could game the 2-Accounting requirement if timing is ambiguous.
**Patch PP-528:** Treaty lapse occurs at Phase 1 of the season AFTER the period ends (Season N+5 for Treaty formed Season N). Accounting of Season N+4 sees Treaty active.

---

## FINDINGS SUMMARY

| ID | Sev | Scenario | Status | Patch |
|----|-----|----------|--------|-------|
| S9-Crown-break-trigger | P2 | 9 | PATCHED | PP-525 |
| S10-Parliamentary-motion | P1 | 10 | PATCHED | PP-526 |
| S13-Closed-Pledge-witnesses | P2 | 13 | PATCHED | PP-527 |
| S15-Treaty-lapse-timing | P2 | 15 | PATCHED | PP-528 |
| S8, S11, S12, S14 | — | 8,11,12,14 | CLEAN | — |

**P1 resolved this batch: 1** (Parliamentary motion definition)
**P2 resolved this batch: 3**

---

## REMEDIATION PATCHES (PP-512–524)
All diplomacy patches from prior session renumbered to PP-512–524 (PP-506–511 were
already taken by Graduated Seizure patches). Full blocks applied to params_board_game.md.
Patch register corrected. Pre-commit audit: 36/36 checks passed.
