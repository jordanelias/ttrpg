# VALORIA PHASE 1 AUDIT — PARAMS-LEVEL CROSS-SYSTEM
## Date: 2026-04-04
## Scope: All 8 params files cross-checked for consistency, coherency, crunch cascades, friction, cognitive load
## Method: Automated terminology scan + manual formula/logic review
## Status: Phase 1 of 3 (params only; deep-doc reads in Phase 2/3)

---

## SUMMARY

| Severity | Count | Category |
|----------|-------|----------|
| P1 | 8 | Formula contradictions, terminology propagation failures, spec conflicts |
| P2 | 5 | Cognitive load, stale references, minor inconsistencies |
| P3 | 3 | Documentation gaps, optimization opportunities |

---

## P1 FINDINGS

### AUD-P1-01: Community Weaving — Triple Specification Conflict
**Files:** params_factions.md (3 locations)
**Issue:** Three mutually contradictory specifications for the Restoration Movement's Community Weaving action exist in a single file:

| Spec | Pool | Ob | Target Track | Source |
|------|------|----|-------------|--------|
| TTRPG entry (L42) | Unspecified | 2 (−1 with markers) | Unspecified | stage6 extract |
| Full PP-168 entry (L160) | Influence | Thread Tension ÷ 20 (round up) | Thread Tension | PP-168 |
| PP-195 Procedure (L210) | Mandate + History | 3 | Rendering Stability | PP-195 |

Pool differs (Influence vs Mandate+History). Ob differs (2, TT÷20, or 3). Target track differs (Thread Tension vs Rendering Stability). Either these are two distinct actions that share a name (requiring disambiguation) or PP-195 supersedes PP-168 (requiring the older spec to be struck). Currently unresolvable without editorial input.
**Action:** [EDITORIAL — needs ED assignment] Reconcile: are these one action or two? If one, which spec is canonical? If two, rename to distinguish.

---

### AUD-P1-02: PP-232 Terminology Propagation Incomplete — params_mass_combat
**File:** params_mass_combat.md (11 instances)
**Issue:** PP-232 renamed Strength→Size, Combat Power→Power, Cohesion→Discipline, Coherence Rating/Command Rating→Command. The params header documents the rename, but the body contains 11 stale references:

| Line | Stale Term | Correct Term |
|------|-----------|-------------|
| L25 (Phase 6) | Cohesion checks | Discipline checks |
| L26 (Phase 7) | Cohesion restore | Discipline restore |
| L98 (Military→Quality table) | Max CP / Cohesion ceiling | Max Power / Discipline ceiling |
| L239 (Damage formula) | Strength loss | Size loss |
| L268 (Artillery) | flat Strength damage | flat Size damage |
| L327 (Altonian table header) | Strength / CP / Cohesion | Size / Power / Discipline |
| L356 (Templar tactic) | +2 Cohesion | +2 Discipline |

**Action:** Mechanical fix — no editorial required. Apply find-and-replace in context (mass combat unit stats only; not personal combat STR).

---

### AUD-P1-03: PP-232 Terminology Propagation Incomplete — params_board_game
**File:** params_board_game.md (3 instances)
**Issue:** Same rename (Cohesion→Discipline) not propagated:

| Line | Stale Term | Correct Term |
|------|-----------|-------------|
| L159 | Unit starting Cohesion | Unit starting Discipline |
| L432 | Both Cohesion −1 | Both Discipline −1 |
| L433 | Both at Cohesion 0 | Both at Discipline 0 |

**Action:** Mechanical fix — no editorial required.

---

### AUD-P1-04: Commander Bonus Formula Contradiction — params_mass_combat
**File:** params_mass_combat.md
**Issue:** Two contradictory scope statements for the Military ÷ 3 commander bonus:
1. "Commander Bonus Formulas — Consolidated (ED-033 resolved)" correctly separates: TTRPG uses Command = ⌈(Cha+Cog)÷2⌉; BG uses Military ÷ 3.
2. PP-190 section (later in file): "Applies to all modes (TTRPG mass combat, Hybrid, BG)" for Military ÷ 3.

If PP-190 is correct, the TTRPG Command formula from PP-232 is overridden. If the consolidated table is correct, PP-190's scope note is wrong.
**Action:** Mechanical fix. PP-232 is more recent than PP-190. The consolidated table (TTRPG=attribute-derived, BG=Military÷3) is correct. Strike the "applies to all modes" note from PP-190.

---

### AUD-P1-05: Discipline Degradation Trigger vs PP-231 Asymmetry Rule Contradiction
**File:** params_mass_combat.md
**Issue:** The Discipline degradation trigger formula is: "total Size lost this turn > Discipline → Discipline −1." PP-231 (later in the same file) states: "Discipline degradation is an asymmetry mechanic... Symmetric engagements between equal-Power units do not trigger Discipline degradation."

The trigger formula has no asymmetry condition — it fires on any Size loss exceeding Discipline, including symmetric engagements. These statements directly contradict.
**Action:** [EDITORIAL — needs ED assignment] Either add an asymmetry precondition to the trigger (e.g., "fires only when attacker Power > defender Power, or Size loss caused by Thread/Artillery"), or revise PP-231 to remove the asymmetry constraint. Simulation needed to determine which produces better gameplay.

---

### AUD-P1-06: Varfell BG Starting Stats Stale — params_factions
**File:** params_factions.md
**Issue:** The BG column for Varfell lists Mandate 3, Wealth 3. params_board_game (PP-191/PP-195 corrections) sets Varfell BG to Mandate 4, Wealth 4. params_factions was not updated.
**Action:** Mechanical fix. Update params_factions Varfell BG row to Mandate 4, Wealth 4.

---

### AUD-P1-07: Attribute Renames Not Propagated — params_factions + params_threadwork
**Files:** params_factions.md (2 instances), params_threadwork.md (2 instances)
**Issue:**
- params_factions L225-226: Maret Vossen described as "Presence 5+" and Aldric Hann as "Lower Presence." Should be Charisma (PP-234).
- params_threadwork Coherence degradation table L199-200: "−1D social/Memory" and "−2D social/Memory" — "Memory" here refers to the attribute (now Recall), not the contest genre. Should be "social/Recall."
**Action:** Mechanical fix — no editorial required.

---


### AUD-P1-08: BG Overwhelming Threshold — ED-031 vs PP-179 Contradiction
**Files:** params_board_game.md, canon/editorial_ledger.yaml
**Issue:** ED-031 resolved as "BG Overwhelming = Ob+1 surplus. Intentional divergence from TTRPG 2×Ob." But PP-179 subsequently set the BG degree table to "matches TTRPG" (≥ 2× Ob). These contradict. Additionally, the TTRPG Overwhelming floor (net ≥ 3 regardless of Ob, from PP-232) is not stated in the BG degree table.
**Action:** [EDITORIAL — ED-142] Confirm: does BG use 2×Ob (PP-179, current params) or Ob+1 (ED-031 resolution)? State Overwhelming floor explicitly in BG table.

---
## P2 FINDINGS

### AUD-P2-01: Focus Range Inconsistency — params_threadwork
**File:** params_threadwork.md
**Issue:** Practitioner Stats table lists Focus range as "1–5+" but params_core establishes all attributes as range 1–7 (advancement max 7). Contact Rounds = Focus, so the range should be 1–7.
**Action:** Mechanical fix. Correct Focus range to 1–7 in params_threadwork.

---

### AUD-P2-02: Combat Pool Minimum Not in params_core
**Files:** params_core.md vs params_combat.md
**Issue:** params_combat states Combat Pool minimum is 5. params_core defines Combat Pool = (Agi×2) + History + 3 but does not state the minimum 5 floor. The derived score table should carry the minimum.
**Action:** Add "minimum 5" to params_core Combat Pool entry.

---

### AUD-P2-03: Morale Triggers Reference Struck Incapacitation States
**File:** params_mass_combat.md (L134-139)
**Issue:** Morale Degradation Triggers table references "General incapacitated (Stage 1)" and "General killed (Stage 2)." ED-130 struck the Stage 1/Stage 2 system. Should read "General incapacitated" (−1) and "General killed" (−2) without Stage references.
**Action:** Mechanical fix. Remove "(Stage 1)" and "(Stage 2)" parentheticals.

---

### AUD-P2-04: Overwhelming Floor Not Stated in BG Degree Table
**File:** params_board_game.md
**Issue:** TTRPG degree table (params_core) requires net ≥ 3 for Overwhelming regardless of Ob (PP-232). BG degree table states only "≥ 2× Ob" without the floor. At Ob 1, this means BG Overwhelming triggers at net 2 while TTRPG requires net 3. ED-031 is flagged as provisional/ongoing but the BG params should at minimum cross-reference it.
**Action:** Add note to BG degree table: "[ED-031: Overwhelming floor alignment with TTRPG pending]."

---

### AUD-P2-05: Social Contest Cognitive Load — No Reference Card
**System:** Social Contest (params_contest.md)
**Issue:** Each contest exchange requires computing: (1) Read result lookup, (2) genre+orientation selection, (3) corroboration decision, (4) pool assembly (attribute×2 + History + up to +2D bonus), (5) interaction type determination, (6) strain calculation (margin + Cha modifier − Foc defence), (7) track movement, (8) concentration depletion. A 5-exchange Grand Contest produces ~40 bookkeeping operations. No GM reference card exists for the v2 system (prior ED-055 card covered v1 only).
**Action:** [EDITORIAL — needs ED assignment] Create v2 social contest reference card with pre-computed strain tables indexed by margin for common Cha/Foc combinations. Phase 2 work.

---

## P3 FINDINGS

### AUD-P3-01: Thread Operations in Mass Combat — Peak Cognitive Load
**Systems:** params_mass_combat + params_threadwork + params_scale_transitions
**Issue:** A practitioner in Phase 4 of mass combat must simultaneously track: operation selection, scale targeting, pool composition (Spirit + History + Thread Pool Score), Thread Sensitivity requirements, RS cost (×3 multiplier), Coherence cost, contact round countdown, and Rendering Crisis thresholds — 8+ consideration points per decision within a 7-phase turn structure that already carries ~3N+3 decisions (N = unit count).
**Optimization opportunity:** Dedicated mass battle Thread tracking sheet with pre-printed RS costs (×3 already applied) and Coherence countdown boxes. Does not reduce mechanical texture — only reduces lookup friction.
**Action:** Create tracking sheet template (Phase 2 or 3).

---

### AUD-P3-02: "Debate" vs "Contest" Terminology Stale Throughout
**Files:** params_scale_transitions.md, params_factions.md, coverage_matrix.md
**Issue:** ED-136 (P1, open) flags the system rename from "Debate" to "Contest." Until ED-136 resolves, all references to "Debate" in other params files are expected-stale. Post-ED-136, a full terminology propagation pass is required.
**Action:** No action until ED-136 resolves. Log propagation targets: params_scale_transitions (2 instances), params_factions (1), coverage_matrix (many).

---

### AUD-P3-03: params_mass_combat Faction Tactic Cards Incomplete
**File:** params_mass_combat.md
**Issue:** Only Crown and Church tactic cards are specified. Varfell, Hafenmark, Löwenritter, and Restoration Movement are listed as "TBD — pending editorial design." This is a content gap, not a consistency error.
**Action:** Flag for editorial design when faction balance pass is next prioritized.

---

## CRUNCH CASCADE ANALYSIS

### Identified Cascades (bounded — no action required)

1. **Combat damage chain:** 3 layers (pool → hits → damage with STR + weapon mod). Fibonacci group bonus capped at +5. No unbounded stacking. ✓
2. **Faction seasonal accounting:** Multiple Domain Actions → stat changes → clock movements → trigger checks. Bounded by seasonal cap (±2/stat TTRPG; ±3 TC from Domain Actions provisional). ✓
3. **Morale degradation in mass combat:** Multiple triggers per phase, capped at −3/Cascade Phase (Stage 2 death exempt but non-repeatable). Rout contagion prevented from cascading in same turn. ✓

### Identified Cascades (flagged — monitoring required)

4. **Thread RS drain in mass combat (×3 multiplier):** Three Dissolution attempts from RS 60 → E[RS] ≈ 6. Already flagged (PP-201, PP-204 mandatory table warning). The cascade is campaign-ending by design — the question is whether players understand the magnitude before choosing. Monitoring only.
5. **Social contest Rattled+Spent compound:** Low Charisma (Composure 7) + low Focus+Recall (Concentration 4) → Rattled by exchange 2, Spent by exchange 3, rolling 1D at +2 Ob. Functionally eliminated from social contests. This is correct design (social incompetence has consequences) but may surprise players. Recommend: GM guidance note about character viability in formal social contests.

---

## CROSS-MODE VALUE ALIGNMENT

| Value | TTRPG | BG | Hybrid | Consistent? |
|-------|-------|-----|--------|------------|
| Die system | d10, TN 7 | d10, TN 7 | d10, TN 7 | ✓ |
| Degree table | Ob 20 cap, floor 3 | Ob 10 cap, no floor stated | Inherits TTRPG | ED-031 open |
| RS starting | 60 | 72 | Inherits BG when in BG | ✓ intentional |
| TC starting | 0 | 28 | Inherits BG | ✓ intentional |
| Faction stats | Full table | Varfell reduced | Inherits BG+TTRPG | ✓ except AUD-P1-06 |
| Combat Pool | Agi×2+Hist+3 | Military as pool | TTRPG for personal, BG for faction | ✓ intentional |
| Thread ops | Full system | Always skipped | Phase-Lock Protocol | ✓ intentional |
| Domain Echo | Immediate | Via accounting | Queued to accounting | ✓ intentional (PP-109) |
| Command formula | ⌈(Cha+Cog)÷2⌉ | Military÷3 | TTRPG for personal, BG for faction | ✓ except AUD-P1-04 |

---

## OPTIMIZATION OPPORTUNITIES (no texture loss)

1. **Pre-computed strain tables for social contests** — index by margin (0–5) × Cha modifier (0–2) × Foc defence (0–3). Fits on one reference card. Eliminates per-exchange arithmetic.
2. **Mass battle Thread tracking sheet** — pre-print ×3 RS costs, Coherence countdown boxes, contact round tracker. Eliminates mid-phase lookups.
3. **Terminology propagation script** — after ED-136 resolves, a single automated find-and-replace pass for Debate→Contest across all files. Same pattern applicable for any future attribute/system renames.

---

## RECOMMENDED NEXT ACTIONS (by priority)

1. **Apply mechanical fixes (AUD-P1-02, P1-03, P1-04, P1-06, P1-07, P2-01, P2-02, P2-03):** Single atomic commit. No editorial required. ~30 min.
2. **Flag new editorials (AUD-P1-01, P1-05, P2-04, P2-05):** Add to editorial_ledger.yaml. ~10 min.
3. **Phase 2 deep-doc audit:** Read threadwork_v25 (85k), bg_v05 (70k), mass_battle_v3 (33k) canonical docs to check for in-document inconsistencies not visible in params. Next session.
4. **Phase 3:** Remaining systems + cross-mode transition simulation + cognitive load scoring with worked examples. Session after.

---

## PHASE 1 GATE: FINDINGS COMMITTED
All findings above are ready for commit to tests/ as audit output. Mechanical fixes ready for immediate application pending confirmation.
