# Valoria Simulation Coverage Matrix
## Initialized: 2026-03-24 | Last Updated: 2026-03-27 (Batch 02)

| ID | Mechanic | Domain | Isolation | Interaction | Scenario | Edge Cases | Status |
|----|----------|--------|-----------|-------------|----------|------------|--------|
| M-001 | Core Dice Engine (d10, TN, Ob, degrees) | Core | ✓ B2-001 | ☐ | ☐ | ✓ B2-001 | In progress |
| M-002 | Wound System (Health, Wounds, +1 Ob, incapacitation) | Core | ✓ B2-002 | ☐ | ☐ | ✓ B2-002 | In progress |
| M-003 | Histories (pool formula, Fork, advancement) | Character | ✓ B2-003 | ☐ | ☐ | ✓ B2-003 | In progress |
| M-004 | Beliefs (CP generation) | Character | ✓ B2-004 | ☐ | ☐ | ☐ | In progress |
| M-005 | Maxims (CP generation) | Character | ✓ B2-004 | ☐ | ☐ | ☐ | In progress — F10 GAP |
| M-006 | Inspirations (Spend, Stunt) | Character | ✓ B2-005 | ☐ | ☐ | ✓ B2-005 | In progress |
| M-007 | Conditions — Gate System (Bloodied, Rattled, Unmask) | Character | ☐ | ☐ | ☐ | ✓ B2-006 | In progress — F13 label mismatch |
| M-008 | Thread Sensitivity (growth, tiers, passive perception) | Thread | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-009 | Certainty Track (costs, 0 = crisis) | Thread | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-010 | Knots (strain, propagation, thresholds) | Thread | ☐ | ☐ | ✓ B2-007 | ✓ B2-007 | In progress — F16 F17 |
| M-011 | Circles (contact finding) | Social | ✓ B2-008 | ☐ | ☐ | ✓ B2-008 | In progress — F18 |
| M-012 | Resources (expenditure) | Social | ✓ B2-009 | ☐ | ☐ | ✓ B2-009 | In progress — F19 deadlock |
| M-013 | The Leap (contact entry) | Thread Ops | ☐ | ☐ | ✓ B2-010 | ✓ B2-010 | In progress |
| M-014 | Diagnosis | Thread Ops | ✓ B2-011 | ☐ | ☐ | ☐ | In progress |
| M-015 | Weaving (all scales) | Thread Ops | ☐ | ✓ B2-012 | ☐ | ☐ | In progress |
| M-016 | Pulling (all targets) | Thread Ops | ✓ B2-013 | ☐ | ☐ | ✓ B2-013 | In progress — **F25 P1** |
| M-017 | Forced Resolution — Lock | Thread Ops | ☐ | ✓ B2-014 | ☐ | ✓ B2-014 | In progress — F26 |
| M-018 | Forced Resolution — Dissolution | Thread Ops | ✓ B2-015 | ☐ | ☐ | ✓ B2-015 | In progress — F28 |
| M-019 | Past-Oriented Pulling | Thread Ops | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-020 | Temporal Disjunction Track (0–20) | Thread Tracks | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-021 | Taint Track (0–10) | Thread Tracks | ☐ | ☐ | ☐ | ✓ B2-016 | In progress — **F29 P1** |
| M-022 | Dissolution Residue (sources, handling, use) | Thread | ☐ | ✓ B2-017 | ☐ | ✓ B2-017 | In progress — **F31 P1** |
| M-023 | Collective Thread Operations | Thread Ops | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-024 | Shifting Objects (creation, deterioration, stabilization) | World | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-025 | Gaps (creation, incursion risk, closure) | World | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-026 | Monstrous Entities (Mode 1, 2, 3) | World | ☐ | ☐ | ✓ B2-018 | ✓ B2-018 | In progress — F33 |
| M-027 | Southernmost — Zone Entry | Exploration | ☐ | ☐ | ✓ B2-019 | ☐ | In progress — F34 |
| M-028 | Locked Zones | Exploration | ☐ | ☐ | ✓ B2-019 | ☐ | In progress |
| M-029 | The Forgetting | Exploration | ☐ | ☐ | ✓ B2-019 | ☐ | Batch 01 + B2-019 — F34 |
| M-030 | Thread Tension (0–100, thresholds) | Global Tracks | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-031 | Theocracy Clock (0–100, thresholds, events) | Global Tracks | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-032 | Altonian Pressure (0–100) | Global Tracks | ✓ B2-020 | ☐ | ☐ | ✓ B2-020 | In progress — F35 |
| M-033 | Clock Interactions (TT↔TC↔IP cross-effects) | Global Tracks | ☐ | ☐ | ✓ B2-029 | ☐ | Batch 01 + B2-029 |
| M-034 | Faction Stats (Mandate, Reach, Wealth, Stability) | Faction | ☐ | ☐ | ✓ B2-021 | ☐ | In progress |
| M-035 | Domain Actions | Faction | ☐ | ✓ B2-021 | ✓ B2-026 | ✓ B2-021 | In progress — F36 |
| M-036 | Parliamentary Vote | Faction | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-037 | Grand Debate | Faction | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-038 | Seasonal Accounting | Faction | ☐ | ☐ | ✓ B2-030 | ☐ | Batch 01 + B2-030 |
| M-039 | Combat — Initiative | Combat | ✓ B2-022 | ☐ | ✓ B2-022 | ☐ | In progress — F37 |
| M-040 | Combat — Priority Table | Combat | ☐ | ✓ B2-022 | ✓ B2-022 | ☐ | In progress |
| M-041 | Combat — Attack/Defence | Combat | ☐ | ✓ B2-022 | ✓ B2-022 | ☐ | In progress |
| M-042 | Combat — Damage Formula | Combat | ✓ B2-023 | ☐ | ☐ | ✓ B2-023 | In progress |
| M-043 | Combat — Equipment (Weapons, Armour) | Combat | ✓ B2-023 | ☐ | ☐ | ✓ B2-023 | In progress |
| M-044 | Combat — Manoeuvres (Defend, Disarm, Trip, etc.) | Combat | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-045 | Mass Combat | Combat | ✓ B2-024 | ☐ | ☐ | ✓ B2-024 | In progress — F41 |
| M-046 | Thread Operations in Combat | Cross-domain | ☐ | ✓ B2-029 | ☐ | ☐ | Batch 01 + B2-029 |
| M-047 | Thread Events in Social Scenes | Cross-domain | ☐ | ✓ B2-025 | ☐ | ✓ B2-025 | In progress — F42 F43 |
| M-048 | Scale and Scope (transition, multi-scope action) | Cross-domain | ☐ | ✓ B2-026 | ✓ B2-030 | ✓ B2-030 | In progress — F45 F51 |
| M-049 | Inquisitor Operations (CE, investigation procedure) | Institutional | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-050 | Riskbreakers (Deniability Debt, CE) | Institutional | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-051 | Devout Constraint (TS block, Dissonance Marks) | Character | ☐ | ✓ B2-025 | ☐ | ☐ | Batch 01 + B2-025 |
| M-052 | Concealment (operation hiding from observers) | Thread Ops | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-053 | Quick Rest / Full Rest | Recovery | ✓ B2-027 | ☐ | ☐ | ✓ B2-027 | In progress — F46 |
| M-054 | Einhir Sites (preservation, destruction) | World | ☐ | ✓ B2-028 | ☐ | ✓ B2-028 | In progress — F48 |
| M-055 | Restoration Community Weaving | Faction | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-056 | Niflhel Destabilization | Faction | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |

---

## Coverage Summary

**Mechanics with any coverage:** 47/56 (84%)
**Mechanics with zero coverage:** M-034 partial (scenario only), M-040 partial. Truly zero: none remaining after B2 — all mechanics touched in at least one cell.

**Test cells complete (✓):** ~62 cells (Batch 01: ~22 estimated + Batch 02: ~40)
**Total test cells:** 224 (56 × 4)
**Coverage %:** ~28%

## P1 Findings (Must Fix Before Compilation Gate)
| Finding | Mechanic | Issue |
|---------|----------|-------|
| F25 | M-016 Pulling | Personal-scale Pulling bypasses all social counter-mechanics — no non-practitioner resistance |
| F29 | M-021 Taint | Taint/Coherence/Intelligibility nomenclature inconsistency in §5.11 |
| F31 | M-022 Dissolution Residue | "−1 Coherence per use" — Coherence undefined post-CP14; should be Intelligibility or Taint |

## Phase 3 Completion Requirements (Remaining)
- Every mechanic needs all 4 cells covered
- Every faction tested with generic character in faction-relevant mechanics
- Every NPC tested in unique-mechanic scenarios
- Every archetype tested in archetype-defining mechanics
- Every track at: starting / mid-range / threshold / terminal values
- Zero untested P1 interactions

**Next batch priority:**
1. Resolve P1 findings (F25, F29, F31) — mechanic-audit task
2. Cover remaining cells: Interaction chains for M-001/M-002/M-003; Scenarios for M-004/M-005/M-006/M-007
3. All NPC-specific tests (Lenneth, Baralta, Olafsson, Klapp, Ehrenwall cross-faction, Elske)
4. All faction generic character tests (all 9 factions in Domain Actions, seasonal accounting)
5. All track terminal-value tests (TT 100, TC 100, IP 100, Intelligibility 0, Taint 10, TD 20)
