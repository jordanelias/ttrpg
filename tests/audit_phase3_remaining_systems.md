# VALORIA PHASE 3 AUDIT — REMAINING SYSTEMS, CROSS-MODE TRANSITIONS, COGNITIVE LOAD
## Date: 2026-04-04
## Scope: Compilation stages, cross-mode handoffs, cognitive load scoring
## Status: Phase 3 of 3 (FINAL)

---

## SUMMARY

| Severity | Count | Category |
|----------|-------|----------|
| P1 | 1 | Structural gap (empty canonical files) |
| P2 | 2 | PP-234 stale terms in compilation stages, hybrid integration pending |
| P3 | 1 | Optimization (cognitive load aids) |

---

## 1. REMAINING COMPILATION STAGES — PP-234 PROPAGATION

### Scanned (9 files)

| File | Status | Fixes Applied |
|------|--------|---------------|
| stage1_core_engine.md | CLEAN | — |
| stage2_characters.md | FIXED | 1× Memory→Recall |
| stage4_southernmost.md | FIXED | 2× Memory→Recall (pool formulas) |
| stage6_factions.md | CLEAN | — |
| stage7_territories.md | CLEAN | — |
| stage10_advancement.md | FIXED | 1× Memory→Recall, 2× Presence→Charisma (CP cost caps) |
| stage12_campaign_modes.md | CLEAN | — |
| stage13_npcs.md | FIXED | 6× Presence→Charisma (NPC stat blocks + Composure formulas) |
| stage14_gm_tools.md | CLEAN | — |

All fixes are PP-234 attribute renames. No structural changes. Mechanical values unchanged.

---

## 2. STRUCTURAL GAPS

### AUD-P1-15: Two Canonical Files Are Empty (0 bytes)

| File | System | canonical_sources status |
|------|--------|------------------------|
| stage5_clocks.md | Clocks | canonical, compilation_current: true |
| stage15_spell_catalog.md | Spell catalog | canonical, compilation_current: true |

Both are listed as canonical and "compilation_current: true" in canonical_sources.yaml, but contain no content. Any system referencing clocks or spells has no authoritative source document. Clock values exist only in params_factions (starting values) and scattered across other docs (TC thresholds, RS thresholds). Spell values exist only in pending patches (R-55, R-56, R-59/60, R-62, R-63, R-64).

**Action:** These need compilation from their scattered sources. Not blocking (clocks are tracked via params; spells are pending patches), but the canonical chain is technically broken for these systems.

---

## 3. CROSS-MODE TRANSITION AUDIT

### Handoff Rules (8 defined in params_scale_transitions)

| Transition | Defined? | Procedure complete? | Issues |
|-----------|----------|-------------------|--------|
| Personal → Thread | ✓ | ✓ | Leap eligibility simplified (PP-232 propagated) |
| Personal → Faction | ✓ | ✓ | Domain Echo via sufficient scope (ED-074 provisional) |
| Personal → Scene | ✓ | ✓ | — |
| Scene → Faction | ✓ | ✓ | Domain Echo cap ED-071 provisional |
| Thread → Faction | ✓ | ✓ | — |
| Thread → Mass | ✓ | ✓ | Phase 4/6 split confirmed (PP-191) |
| Mass → Personal | ✓ | ✓ | 5-exchange max, Command suspended |
| Scene → Mass | ✓ | ✓ | — |

### Phase-Lock Protocol (PP-103)
Legal Zoom In entry points: After Phase 1, After Phase 3, After Phase 6 Step 1. Phase 6 continuation (Steps 2-6) resolves after Zoom Out. Confirmed clean.

### Domain Echo Timing Asymmetry
TTRPG: immediate. Hybrid: queued to accounting. Intentional (PP-109). Documented.

### Hybrid Gap Resolution Status
17 of 17 hybrid gaps resolved in designs/hybrid/hybrid_gaps_resolved.md. 4 "pending" mentions are about propagation to working files (not about unresolved gaps). The 17 resolutions are NOT yet integrated into stage11_scale_transitions.md — documented in file_index as propagation-pending.

**Action (P2):** Integration of hybrid_gaps_resolved.md into stage11 is pending. Not blocking (design doc exists), but compilation is behind. Lower priority than design-layer work.

---

## 4. COGNITIVE LOAD SCORING

### Method
Each system scored on three dimensions (1-3 each):
- **Decisions**: active choices per action unit (round/exchange/phase/season)
- **Lookups**: table references required per resolution
- **Tracking**: state variables maintained simultaneously

Total = Decisions + Lookups + Tracking. Range 3-9.
≤4 = Light | 5-6 = Moderate | 7-8 = Heavy | 9 = Extreme

### Scores by System

| System | Unit | Decisions | Lookups | Tracking | Total | Rating |
|--------|------|-----------|---------|----------|-------|--------|
| **Core dice** | per roll | 1 | 1 | 1 | **3** | Light |
| **Personal combat** | per round | 2 (split + action) | 2 (weapon TN + damage table) | 2 (Health, Stamina) | **6** | Moderate |
| **Social contest** | per exchange | 2 (genre+orientation, corroborate) | 2 (interaction type, strain formula) | 3 (track, Composure, Concentration) | **7** | Heavy |
| **Thread operations** | per contact | 2 (op selection, scale) | 2 (op table, RS cost) | 3 (Coherence, RS, contact rounds) | **7** | Heavy |
| **Mass combat** | per turn | 3 (per-unit: formation, movement, split) | 3 (phase structure, damage, Discipline) | 3 (Size, Discipline, Morale per unit) | **9** | Extreme |
| **Thread in mass combat** | per Phase 4 | 3 (op, scale, Lock/Support) | 3 (op table, ×3 RS, threshold) | 3 (Coherence, RS, contact, Rupture threshold) | **9** | Extreme |
| **BG turn** | per season | 2 (card selection, targeting) | 2 (action card, accounting) | 2 (faction stats, clocks) | **6** | Moderate |
| **Hybrid (Zoom In)** | per transition | 3 (entry point, state transfer, mode rules) | 3 (Phase-Lock, handoff table, Echo timing) | 3 (both-mode states, queue, phase position) | **9** | Extreme |
| **Faction Domain Actions** | per action | 1 (target + roll) | 2 (Ob from target stat, ethical modifier) | 1 (faction stats) | **4** | Light |
| **Advancement** | per session-end | 1 (CP allocation) | 1 (cost table) | 1 (CP total) | **3** | Light |

### Peak Load Points (systems scoring 9)

1. **Mass combat** — the combination of per-unit decisions across 7 phases produces ~3N+3 total decision points per turn (N = unit count). With 3 units, 12 decisions. With 5, 18. The phase structure itself is the load source — each phase has distinct resolution rules.

2. **Thread in mass combat** — all Thread system load PLUS mass combat load PLUS the ×3 RS multiplier creates a unique pressure. A practitioner-general must track both systems simultaneously. This is the single highest cognitive load moment in the game.

3. **Hybrid Zoom In** — the transition itself requires tracking state from two game modes, transferring variables per the state_transfer_spec, and switching between TTRPG and BG resolution procedures. Once established, load drops to whichever mode is active.

### Optimization Recommendations (no texture loss)

| System | Load | Aid | Effect |
|--------|------|-----|--------|
| Social contest | 7 (Heavy) | Pre-computed strain table (margin × Cha mod × Foc def) on reference card | −1 Lookups |
| Mass combat | 9 (Extreme) | Phase flowchart card (7 phases with resolution steps) | −1 Lookups |
| Thread in mass combat | 9 (Extreme) | Mass battle Thread sheet with pre-printed ×3 RS costs | −1 Lookups, −1 Tracking |
| Hybrid Zoom In | 9 (Extreme) | State transfer checklist (from state_transfer_spec.md) | −1 Tracking |

These are GM reference aids, not mechanical changes. Total effect: reduce peak loads from 9 to 7-8 (Heavy rather than Extreme).

---

## 5. FULL AUDIT — OPEN ITEMS REGISTRY

### Requires Editorial Decision (user input needed)

| ID | Description | Priority |
|----|-------------|----------|
| ED-139 | Community Weaving: 3 conflicting specs (pool, Ob, target track) | P1 |
| ED-140 | Discipline degradation trigger: no asymmetry condition vs PP-231 rule | P1 |
| ED-142 | BG Overwhelming: ED-031 says Ob+1 but PP-179 says 2×Ob | P1 |
| ED-141 | Social contest v2 GM reference card needed | P2 |

### Excluded (per user direction)

| ID | Description |
|----|-------------|
| SIM-DEBT-03 | Full re-sim under two-genre system |
| SIM-DEBT-04 | Adjudicator-type pool calibration |

### Propagation Pending (low priority)

| Item | Description |
|------|-------------|
| hybrid_gaps_resolved.md → stage11 | 17 resolved hybrid gaps not yet in compilation |
| stage5_clocks.md | Empty canonical file — needs compilation |
| stage15_spell_catalog.md | Empty canonical file — needs compilation |
| ED-136 (Debate→Contest rename) | Blocked on editorial; propagation targets identified |

### Resolved This Session

| Item | Resolution |
|------|-----------|
| AUD-P0-01 | PP-232/PP-233 propagated to all 4 canonical design docs |
| AUD-P1-02 through P1-08 | Params mechanical fixes applied (Phase 1 commit) |
| AUD-P1-09 through P1-14 | Canonical doc formula/outcome mismatches resolved (PP-232 propagation) |
| AUD-P2-01 through P2-08 | Stale terminology fixed in params + canonical docs |
| PP-234 compilation propagation | 4 compilation stages fixed (stage2, 4, 10, 13) |

---

## GATE: PHASE 3 COMPLETE — AUDIT CLOSED

All mechanically resolvable findings from Phases 1-3 have been addressed. Canonical source integrity restored for PP-232/PP-233/PP-234 across all design docs and compilation stages. 4 editorial items remain open requiring user decision. 2 simulation debt items excluded per user direction.
