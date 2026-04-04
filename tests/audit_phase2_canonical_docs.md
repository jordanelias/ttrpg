# VALORIA PHASE 2 AUDIT — CANONICAL DESIGN DOCUMENT REVIEW
## Date: 2026-04-04
## Scope: 5 canonical design docs cross-checked against params files + internal consistency
## Documents audited: threadwork_v25 (85k), bg_v05 (70k), mass_battle_v3 (33k), social_contest_v2 (25k), combat_design_v1 (18k)
## Status: Phase 2 of 3

---

## SUMMARY

| Severity | Count | Category |
|----------|-------|----------|
| P0 (CRITICAL) | 1 | Systemic canonical source integrity failure |
| P1 | 6 | Formula/outcome mismatches between canonical docs and params |
| P2 | 3 | Stale terminology, minor inconsistencies |

---

## P0 FINDING — SYSTEMIC

### AUD-P0-01: PP-232/PP-233 Not Propagated to ANY Canonical Design Document

**Scope:** ALL systems with design-layer canonical docs

PP-232 (the largest mechanical patch in the project) was applied to all params files but to ZERO canonical design documents. PP-233 (mass combat formula) similarly unpropagated. Confirmed by text search:

| Document | PP-232 refs | PP-233 refs | PP-234 refs |
|----------|------------|------------|------------|
| combat_design_v1.md | 0 | 0 | 0 |
| mass_battle_v3.md | 0 | 0 | 0 |
| threadwork_redesign_v25.md | 0 | 0 | 0 |
| valoria_bg_v05.md | 0 | 0 | 0 |
| social_contest_system_v2.md | 0 | 0 | 2 ✓ |

**Impact:** canonical_sources.yaml declares these docs as canonical. Simulations read params files (which have PP-232). The result: the canonical chain is broken. Anyone reading a canonical doc gets pre-PP-232 rules. Anyone reading params gets post-PP-232 rules. These describe different games.

PP-232 changes NOT in canonical docs:
- **Combat:** weapon system rebuild (old TN table → Short/Long×Light/Heavy×Blade/Blunt matrix), wound penalty revised (−1D+Ob → −1D only), Health formula revised, Stamina floor 2, initiative declaration order, armour wield constraint, Mass Mismatch exemptions
- **Mass combat:** unit stat renames (Strength→Size, Combat Power→Power, Cohesion→Discipline, Coherence Rating→Command), Power derived from Size, damage formula updates
- **Mass combat (PP-233):** new core formula Pool = min(Size,Command)+Command. Old formula was min(CP, Strength) — fundamentally different
- **Threadwork:** Spirit added to Leap pool, Leap Failure outcome revised, POP TN corrected to 8, incapacitation threshold removed from Leap eligibility
- **Attributes:** Presence→Charisma, Memory→Recall

**Required action:** Multi-session propagation. Apply PP-232 changes to all 4 affected canonical docs. Estimated effort: 2–3 sessions due to document size and the need to verify each change in context. Until propagation is complete, params files are the de facto mechanical authority, not the canonical docs. This should be reflected in canonical_sources.yaml.

**Interim measure:** Add a stale warning to canonical_sources.yaml for each affected system noting that params is ahead of the canonical doc for PP-232/PP-233 content.

---

## P1 FINDINGS

### AUD-P1-09: combat_design_v1.md — Pre-PP-232 Weapon System
**File:** designs/combat/combat_design_v1.md (L99-123)
**Issue:** Document contains the old weapon TN table (Light Cut TN 5, Heavy Cut TN 6, etc.) while params_combat has the PP-232 Short/Long × Light/Heavy × Blade/Blunt matrix with computed TNs. These are structurally different systems — not a simple terminology swap.
**Action:** Part of PP-232 propagation (P0-01). Requires rebuilding §5 of the combat doc.

### AUD-P1-10: combat_design_v1.md — Wound Penalty Contradiction
**File:** designs/combat/combat_design_v1.md (L209)
**Issue:** Doc says "−1D to all combat rolls AND +1 Ob to all rolls (cumulative)." PP-232 changed to "−1D Combat Pool only (no Ob penalty)." Direct contradiction.
**Action:** Part of PP-232 propagation.

### AUD-P1-11: threadwork_redesign_v25.md — Leap Pool Missing Spirit
**File:** designs/ttrpg/threadwork_redesign_v25.md (L108)
**Issue:** Leap pool = "Attunement + History + Thread Pool Score." PP-232 added Spirit. Params correctly has "Spirit + Attunement + History + Thread Pool Score."
**Action:** Part of PP-232 propagation.

### AUD-P1-12: threadwork_redesign_v25.md — Leap Failure Outcome Mismatch
**File:** designs/ttrpg/threadwork_redesign_v25.md (L121)
**Issue:** Canonical doc says Failure = "4 Composure strain + Rattled for scene + no operation." Params (PP-232) says Failure = "−1D Thread Pool Score for scene." Completely different outcomes with different severity and mechanical effects.
**Action:** Part of PP-232 propagation. Confirm which outcome is intended — params version (PP-232) is presumably correct.

### AUD-P1-13: threadwork_redesign_v25.md — POP TN Still 7 (Should Be 8)
**File:** designs/ttrpg/threadwork_redesign_v25.md (L298)
**Issue:** Past-Oriented Pulling TN listed as 7. PP-232 corrected to TN 8. Params is correct.
**Action:** Part of PP-232 propagation.

### AUD-P1-14: threadwork_redesign_v25.md — Leap Eligibility Incapacitation Threshold
**File:** designs/ttrpg/threadwork_redesign_v25.md (L102)
**Issue:** Doc has "Not at or above incapacitation Wound threshold (threshold = ceiling(Health ÷ 2))." PP-232 removed this condition ("not a defined mechanic in this context"). The ceiling(Health÷2) formula doesn't correspond to the current wound system.
**Action:** Part of PP-232 propagation.

---

## P2 FINDINGS

### AUD-P2-06: mass_battle_v3.md — 84 Stale Terminology Instances
**File:** designs/mass_combat/mass_battle_v3.md
**Issue:** 84 instances of pre-PP-232 terminology (Strength, Combat Power, Cohesion, Coherence Rating). The entire document uses old unit stat names. Also uses old core formula: min(CP, Strength) instead of PP-233's min(Size, Command) + Command.
**Action:** Part of PP-232/PP-233 propagation. Document-wide find-and-replace plus formula rebuilds.

### AUD-P2-07: threadwork_redesign_v25.md — 3 Stale Memory→Recall Instances
**File:** designs/ttrpg/threadwork_redesign_v25.md (L540-542)
**Issue:** Coherence thresholds table references "Memory-based rolls" (3 instances). Should be "Recall-based rolls" per PP-234 attribute rename. Same issue fixed in params during Phase 1.
**Action:** Part of PP-232 propagation.

### AUD-P2-08: bg_v05 — 12 Stale Terminology Instances
**File:** designs/board_game/valoria_bg_v05_simulation_and_patches.md
**Issue:** 12 instances of stale terms. Cohesion (should be Discipline in TTRPG-layer battle contexts), some Presence references in non-Administrative-Presence contexts. Some may be intentional BG-layer terminology (BG doesn't track unit-level Discipline); requires case-by-case review.
**Action:** Review during PP-232 propagation pass. BG-layer Cohesion references may be intentional abstraction.

---

## CLEAN SYSTEM

### Social Contest System v2 — No Issues Found
designs/contest/social_contest_system_v2.md is internally consistent. Composure = Charisma + 6 throughout. Pool formulas match params. Genre terminology (Memory/Projection) is correct — these are genre names, not attribute names. PP-234 properly referenced. No action required.

---

## CANONICAL SOURCE INTEGRITY ASSESSMENT

| System | Canonical Doc | Params | Aligned? | Gap |
|--------|--------------|--------|----------|-----|
| Core engine | stage1 (compilation) | params_core | ✓ | Minor (Combat Pool min 5 added Phase 1) |
| Characters | stage2 (compilation) | params_core | ✓ | — |
| Threadwork | threadwork_v25 (design) | params_threadwork | ✗ | PP-232 Leap/POP/eligibility changes |
| Combat | combat_design_v1 (design) | params_combat | ✗✗ | PP-232 weapon system, wounds, initiative |
| Mass combat | mass_battle_v3 (design) | params_mass_combat | ✗✗ | PP-232 renames + PP-233 formula |
| Social contest | social_contest_v2 (design) | params_contest | ✓ | — |
| Factions | stage6 + bg_v05 | params_factions | ~✓ | Phase 1 fixes applied; ED-139 open |
| Board game | bg_v05 + bg_proposal_v02 | params_board_game | ~✓ | 12 stale terms; ED-142 open |
| Scale transitions | stage11 (compilation) | params_scale_transitions | ✓ | — |

**Bottom line:** 3 of 9 systems have broken canonical chains. Combat and mass combat are severely broken (different formulas, different systems). Threadwork has targeted mismatches. The params files are the current mechanical truth; the canonical docs are stale.

---

## RECOMMENDED ACTIONS (PRIORITY ORDER)

1. **IMMEDIATE (this session):** Update canonical_sources.yaml with stale warnings for combat, mass_combat, threadwork. Note that params files are the de facto authority for PP-232/PP-233 content until propagation completes.

2. **NEXT SESSION (PP-232 propagation — combat):** Apply PP-232 to combat_design_v1.md. Highest priority because the weapon system is structurally different (not just terminology). ~1 session.

3. **FOLLOWING SESSION (PP-232/233 propagation — mass combat):** Apply PP-232 + PP-233 to mass_battle_v3.md. 84 terminology changes + formula rebuild. ~1 session.

4. **FOLLOWING SESSION (PP-232 propagation — threadwork):** Apply PP-232 to threadwork_redesign_v25.md. Targeted changes (Leap pool, Failure outcome, POP TN, eligibility). ~0.5 session.

5. **LOW PRIORITY (PP-232 propagation — BG):** Review bg_v05 stale terms. Case-by-case — some may be intentional BG abstraction.

---

## PHASE 2 GATE: COMPLETE
Phase 3 (remaining systems + cross-mode transition audit + cognitive load scoring) deferred. The P0 finding (canonical source integrity) supersedes Phase 3 — propagation should take priority.
