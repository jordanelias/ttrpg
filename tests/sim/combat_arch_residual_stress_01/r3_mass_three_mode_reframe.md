# R3 — Mass-Battle Three-Mode Reframe
## Module 3 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** A coverage + D edge cases
**Source question:** `tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §4 R3`
**Question text:** *"Canonical mass_battle_v30 Parts A (TTRPG), B (Board), D (World Bridge) coexist. Chunk 5 recommends deprecating Part A and reframing Part B as off-screen abstract resolution. Decision needed: is Jordan committed to this reframe, or does some TTRPG/board structure need preserving for design parallels with canonical fieldwork modes?"*

**Decision shape:** full reframe / partial / preserve

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R3-L01 | three_mode_framing | TTRPG/Hybrid (Part A); Board Game (Part B); Hybrid Handoff (§B.5) | designs/provincial/mass_battle_v30.md | header L9 | "Three-mode: TTRPG/Hybrid (Part A); Board Game (Part B); Hybrid Handoff (§B.5)" |
| R3-L02 | part_a_unified_resolution | Mass battle uses same dice engine as personal combat | designs/provincial/mass_battle_v30.md | §A.1 OVERVIEW | "Mass battle uses the same dice engine as personal combat." |
| R3-L03 | part_a_effective_pool | Effective Combat Pool = min(Size, Command) + Command | designs/provincial/mass_battle_v30.md | §A.1 OVERVIEW | "**Effective Combat Pool = min(Size, Command) + Command** (PP-233)" |
| R3-L04 | part_b_design_principle | BG battles resolve in single Priority 2 slot, 3–5 minute total resolution | designs/provincial/mass_battle_v30.md | §B.1 DESIGN PRINCIPLE | "BG battles resolve in a single Priority 2 slot. Total resolution time: 3–5\nminutes." |
| R3-L05 | part_b_strategic_depth_locus | Strategic depth lives in preparation, not execution | designs/provincial/mass_battle_v30.md | §B.1 | "Strategic depth lives in preparation (unit composition, order\nchoice, tactic card selection), not in turn-by-turn execution." |
| R3-L06 | b5_phase_lock_protocol | Zoom In fires only at three legal phase-lock points | designs/provincial/mass_battle_v30.md | §B.5 HYBRID HANDOFF | "Zoom In may only fire at one of three legal phase-lock points:\n- **After Phase 1** (orders placed, nothing resolved — cleanest entry)\n- **After Phase 3** (manoeuvre complete, pre-Engagement)\n- **After Phase 6 Step 1** (all damage applied, no ghost units)" |
| R3-L07 | canonical_status | Canonical, approved 2026-04-17 | designs/provincial/mass_battle_v30.md | header | "Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance)" |

---

## 2. Reframing the question against actual canon

The synthesis (chunk 5) framed three modes as: TTRPG (Part A), Board (Part B), World Bridge (Part D). It recommended deprecating "TTRPG mode" and making "Hybrid" the videogame default.

**The v30 canon already executed the merger.** Per R3-L01, Part A is labeled "TTRPG/Hybrid" — they are not separate modes. The synthesis was written against a framing that no longer reflects current canon. R3 must be re-asked against actual structure:

**Actual structure (post-PP-232/PP-233 merger, canonical 2026-04-17 R3-L07):**
| Part | Scope | Resolution time | Use case |
|---|---|---|---|
| **A** | TTRPG/Hybrid unified unit-scale resolution (full canonical math: dice, Pool, Wounds, Stamina, Threadwork) | per-round real-time | Hero present in battle; scene-zoom available; unit-by-unit detail |
| **B** | Board-Game abstract resolution (Effective Pool collapsed; Tactic Cards; pre-printed unit stats) | 3–5 minutes total (R3-L04) | Hero absent or strategic-layer focus; offscreen battles |
| **§B.5** | Hybrid Handoff: zoom from BG to scene at three legal phase-lock points (R3-L06) | trigger-driven | Player wants to engage at scene scale mid-BG-battle |
| **§D.1–D.3** | Post-battle World Bridge: named officers, scenes at battle site, player morale | per-battle | After-battle narrative |
| **§E** | Battle Consequences (canonical ED-542) | per-battle | Victory/defeat downstream effects |

**The "TTRPG mode" the synthesis wanted to deprecate doesn't exist as a distinct mode under v30 canon.** TTRPG and Hybrid are the same thing (Part A). The deprecation has already happened.

**The remaining R3 question is therefore narrower:** which I-tier from the synthesis's interface ladder maps to which Part?

---

## 3. I-tier ↔ mass-battle Part mapping

From `tests/stress/combat_videogame_arch_2026-05-01/04_q3_scene_mass.md` and synthesis §3:

| Phase | I-tier | Mass-battle Part used | Player experience |
|---|---|---|---|
| 0 spike | — | Part A only (single-zone test) | Substrate validation |
| 1 MVP | I1 (modal zoom) | Part B as primary; Part A only via §B.5 zoom | Strategic + occasional scene-zoom |
| 2 v0.2 | I4 (parallel scenes) | Part A primary at unit scale; hero plays scene-scale on sub-region | Both scales concurrent, distinct |
| 3 v1.0 | I2 (continuous-zoom) | Part A always; spawn individuals at zoom threshold | Camera-driven scale traversal |
| 4 ongoing | refinements | All parts available | Mode-appropriate selection |

**Key insight:** the videogame's default mass-battle resolution evolves across phases. There is no single "videogame default" that holds across the full ship path. The architecture must support mode-switching by phase.

---

## 4. Candidates

| ID | Name | Description |
|---|---|---|
| **C3.1** | Preserve as-is | v30 canon already executed the TTRPG→TTRPG/Hybrid merger. Three-mode framing accurate. Add I-tier mapping notes (Section 3) as documentation, no mechanical change. |
| **C3.2** | Full reframe per synthesis | Rename "TTRPG/Hybrid" → "Unit-scale videogame default"; rename "Board Game" → "Abstract off-screen resolution." Cosmetic — naming change only since merger already done. |
| **C3.3** | Partial restructure | Reorganize: Part A = "Default unit-scale" (per-round); Part B = "Abstract resolution" (offscreen / strategic-layer); §B.5 = "Scale-traversal bridge" (zoom). Add explicit phase-mapping table to top-of-file. |

---

## 5. NERS at full grain — 24 cells per candidate

Criteria locked at module start (consistent with R1 v2 / R2):

### C3.1 — Preserve as-is + I-tier mapping doc note

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | v30 canon already coherent (R3-L07 canonical 2026-04-17). I-tier mapping note clarifies use without mechanical change. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | All Part A canonical math (R3-L02, R3-L03) preserved. Part B simplification (R3-L04) preserved. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Phase-lock protocol (R3-L06) preserves scale-traversal points. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork at mass scale (§A.10) unchanged; Wound penalty universal (PP-716) propagates correctly. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Fieldwork and personal-scale interface unchanged. |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Phase 1 MVP through Phase 3 v1.0 supported by current canon as-is. |

**Verdict C3.1:** 24/24 ✓. Cleanest option — canon already did the work; only documentation needs updating.

### C3.2 — Cosmetic reframe (rename Parts)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ⚠ | Rename burden across mass_battle_v30, params/mass_combat, scale_transitions_v30, plus all references in design docs. ⚠ E because renaming is propagation-heavy with no mechanical gain. ⚠ S because the rename creates a discontinuity in editorial-history references (PP-232/PP-233 patch trail uses old names). |
| Bottom-up | ✓ | ⚠ | ✓ | ⚠ | All math unchanged; only labels change. ⚠ on cross-reference churn. |
| Vertical | ✓ | ✓ | ✓ | ✓ | No vertical impact. |
| Diagonal | ✓ | ⚠ | ✓ | ⚠ | Cross-system references in fieldwork_v30, threadwork_v30, combat_v30 all need rename propagation. |
| Lateral | ✓ | ⚠ | ✓ | ⚠ | Hybrid Handoff rename to "Scale-traversal bridge" — neither term is more accurate than the other. |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Future-proofing argument: clearer videogame-era naming. ⚠ removed since this is the only direction where rename has positive value. |

**Verdict C3.2:** 18/24 ✓, 6 ⚠. No ✗. Pure cost: heavy propagation work for cosmetic clarity. Marginal value.

### C3.3 — Partial restructure with phase-mapping table

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Adds phase-mapping table at top of mass_battle_v30; no internal restructure. Useful documentation. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Mechanical content unchanged. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Phase-mapping makes vertical scale-traversal explicit. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | No cross-system impact. |
| Lateral | ✓ | ✓ | ✓ | ✓ | No lateral impact. |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Phase-mapping documents the I-tier evolution explicitly — Phase 0/1/2/3 use cases clearly attributed to Part A/B/§B.5. |

**Verdict C3.3:** 24/24 ✓. Adds documentation value over C3.1.

### Cross-candidate summary

| Candidate | N pass | E pass | R pass | S pass | Verdict |
|---|---|---|---|---|---|
| C3.1 Preserve as-is + I-tier note | 6/6 | 6/6 | 6/6 | 6/6 | **PASS — minimum work, full canonical preservation** |
| C3.2 Cosmetic rename | 6/6 | 4/6 (2⚠) | 6/6 | 4/6 (2⚠) | **PASS but high propagation cost for low value** |
| C3.3 Phase-mapping table | 6/6 | 6/6 | 6/6 | 6/6 | **PASS — adds documentation value** |

C3.1 and C3.3 differ only by the addition of the phase-mapping table to the top of mass_battle_v30. Both are mechanically equivalent to current canon.

---

## 6. Mode D — Edge cases

### Boundary
**EC-D3.B-01 [P3] (any):** §B.5 phase-lock protocol R3-L06 — three legal entry points. If a Zoom In trigger fires during Phase 5 (Engagement), it defers to After Phase 6 Step 1. Already documented; no edge case.

### Cascade
**EC-D3.C-01 [P3] (C3.2 only):** Renaming cascade — every cross-reference in derived_stats_v30 §troop, threadwork_v30 §A.10, fieldwork_v30 §combat-bridge, params/scale_transitions, etc. needs update. Hand-tracked propagation; one missed reference creates stale-text drift (Solmund/Galbados pattern).

### Regression
**EC-D3.R-01 [P3] (any):** None obvious. The three modes are non-recursive.

### Deadlock
**EC-D3.D-01 [P3] (any):** None — phase-lock protocol prevents mid-phase deadlock.

### Crunch cascade
**EC-D3.CR-01 [P3] (C3.2):** 50+ cross-reference updates required across ttrpg repo; one missed = stale text. Bookkeeping cost.

### Ambiguity
**EC-D3.A-01 [P3] (C3.1/C3.3):** "Hybrid Handoff" naming retains TTRPG/board-game era terminology. New readers may infer two modes (TTRPG + Hybrid) instead of one merged Part A. C3.3's phase-mapping table mitigates by making the unification explicit.

### Incoherence
**EC-D3.I-01 [P3] (C3.2):** Synthesis's "TTRPG mode deprecated" reframe is solving a problem that v30 canon already solved (R3-L07 canonical 2026-04-17 merger via PP-232/PP-233). Adopting C3.2 = creating cosmetic churn over already-resolved restructure.

### Optimal play
**EC-D3.O-01 [P3] (any):** Player optimal: choose Part A engagement when wanting scene-zoom narrative beats; choose Part B abstract when wanting strategic-layer pace. Already supported by §B.5 phase-lock protocol. No degenerate strategy.

### Degenerate
**EC-D3.DG-01 [P3] (none):** No degenerate cases for any candidate.

---

## 7. Decision-shape findings

**Recommendation: C3.3 (preserve canonical structure + add phase-mapping table to top of mass_battle_v30).**

**Rationale:**

1. **The synthesis's premise is partially obsolete.** Per R3-L01 and R3-L07, v30 canon already merged TTRPG and Hybrid into Part A on 2026-04-17. The "TTRPG mode deprecation" the synthesis recommended has already been executed. R3 cannot be answered as the synthesis posed it; the question must be re-asked against actual canon.

2. **Re-asked R3 question:** does the v30 three-mode structure (Part A unified resolution; Part B abstract; §B.5 handoff; Part D world bridge; Part E consequences) need restructure for the videogame medium? Answer: **no mechanical restructure needed.** The structure already supports the I1 → I4 → I2 ship path. What's missing is documentation: which Part is the videogame default at which I-tier (Section 3 phase-mapping).

3. **C3.1 (preserve as-is) and C3.3 (preserve + add mapping table) both pass 24/24 NERS.** C3.3 adds modest documentation value; C3.1 is zero work.

4. **C3.2 (cosmetic rename) passes NERS but has 6 ⚠ on E and S** for propagation cost. Solving a problem that's already been resolved. Reject as low-value churn.

**Implementation under C3.3 (single doc edit, no mechanical change):**

- Add a phase-mapping table at the top of `designs/provincial/mass_battle_v30.md` (Section 3 of this module).
- No changes to Part A / Part B / §B.5 / Part D / Part E content.
- No changes to params/mass_combat.md or scale_transitions_v30.md.
- Net cost: ~30 lines of documentation in one file.

**Decision-shape statement for Jordan ratification:**

> Mass-battle three-mode structure preserved as-is per v30 canonical (approved 2026-04-17 per PP-232/PP-233 merger). The synthesis's "deprecate TTRPG mode" recommendation was solving a problem already resolved by canon. Recommended documentation addition: phase-mapping table at top of mass_battle_v30 explicitly attributing Part A / Part B / §B.5 to Phase-0 spike, Phase-1 MVP (I1), Phase-2 v0.2 (I4), Phase-3 v1.0 (I2) per the synthesis ship path.

**Items deferred to Jordan:**

- Confirm: should the synthesis §3 ship-path Phase mapping be inscribed into mass_battle_v30 directly, or kept in stress-test reference docs only?
- If C3.3 adopted: minor PP for the documentation addition.

---

## 8. Module status

| Item | Status |
|---|---|
| Canonical sources fetched at full depth | ✓ |
| Verification ledger entries (7) | ✓ |
| Re-asked question against actual v30 canon | ✓ |
| NERS full-grain analysis (72 cells across 3 candidates) | ✓ |
| Mode D edge cases | ✓ |
| Decision-shape finding | ✓ |
| Synthesis-canon discrepancy noted | ✓ |

**Module 3 status: verified.**
