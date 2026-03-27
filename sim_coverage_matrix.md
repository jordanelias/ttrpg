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
| M-008 | Thread Sensitivity (growth, tiers, passive perception) | Thread | ☐ | ☐ | ✓ B3-008 B3-011 | ✓ B3-013 | In progress |
| M-009 | Certainty Track (costs, 0 = crisis) | Thread | ✓ B3-001 | ☐ | ☐ | ✓ B3-001 | In progress — F52 F53 |
| M-010 | Knots (strain, propagation, thresholds) | Thread | ☐ | ☐ | ✓ B2-007 | ✓ B2-007 | In progress — F16 F17 |
| M-011 | Circles (contact finding) | Social | ✓ B2-008 | ☐ | ☐ | ✓ B2-008 | In progress — F18 |
| M-012 | Resources (expenditure) | Social | ✓ B2-009 | ☐ | ☐ | ✓ B2-009 | In progress — F19 deadlock |
| M-013 | The Leap (contact entry) | Thread Ops | ☐ | ☐ | ✓ B2-010 | ✓ B2-010 | In progress |
| M-014 | Diagnosis | Thread Ops | ✓ B2-011 | ☐ | ☐ | ☐ | In progress |
| M-015 | Weaving (all scales) | Thread Ops | ☐ | ✓ B2-012 | ☐ | ☐ | In progress |
| M-016 | Pulling (all targets) | Thread Ops | ✓ B2-013 | ☐ | ☐ | ✓ B2-013 | In progress — **F25 P1** |
| M-017 | Forced Resolution — Lock | Thread Ops | ☐ | ✓ B2-014 | ☐ | ✓ B2-014 | In progress — F26 |
| M-018 | Forced Resolution — Dissolution | Thread Ops | ✓ B2-015 | ☐ | ☐ | ✓ B2-015 | In progress — F28 |
| M-019 | Past-Oriented Pulling | Thread Ops | ☐ | ☐ | ✓ B3-002 | ✓ B3-002 | In progress — F54 F55 |
| M-020 | Temporal Disjunction Track (0–20) | Thread Tracks | ✓ B3-004 B3-026 B3-028 | ☐ | ☐ | ✓ B3-004 B3-026 | In progress — F59 F60 F100 F101 F104 |
| M-021 | Coherence Track (10→0, dissolution residue) | Thread Tracks | ☐ | ☐ | ☐ | ✓ B2-016 | In progress — **F29 P1** |
| M-022 | Dissolution Residue (sources, handling, use) | Thread | ☐ | ✓ B2-017 | ☐ | ✓ B2-017 | In progress |
| M-023 | Collective Thread Operations | Thread Ops | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-024 | Shifting Objects (creation, deterioration, stabilization) | World | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-025 | Gaps (creation, incursion risk, closure) | World | ☐ | ☐ | ☐ | ☐ | Batch 01 touched |
| M-026 | Monstrous Entities (Mode 1, 2, 3) | World | ☐ | ☐ | ✓ B2-018 | ✓ B2-018 | In progress — F33 |
| M-027 | Southernmost — Zone Entry | Exploration | ☐ | ☐ | ✓ B2-019 | ☐ | In progress — F34 |
| M-028 | Locked Zones | Exploration | ☐ | ☐ | ✓ B2-019 | ☐ | In progress |
| M-029 | The Forgetting | Exploration | ☐ | ☐ | ✓ B2-019 | ☐ | Batch 01 + B2-019 — F34 |
| M-030 | Thread Tension (0–100, thresholds) | Global Tracks | ☐ | ☐ | ✓ B3-005 B3-030 | ✓ B3-005 | In progress — F61 |
| M-031 | Theocracy Clock (0–100, thresholds, events) | Global Tracks | ✓ B3-006 | ☐ | ✓ B3-030 | ✓ B3-006 | In progress — F62 F63 |
| M-032 | Altonian Pressure (0–100) | Global Tracks | ✓ B2-020 B3-025 | ☐ | ✓ B3-025 | ✓ B2-020 B3-025 | In progress — F35 F98 F99 |
| M-033 | Clock Interactions (TT↔TC↔IP cross-effects) | Global Tracks | ☐ | ☐ | ✓ B2-029 | ☐ | Batch 01 + B2-029 |
| M-034 | Faction Stats (Mandate, Reach, Wealth, Stability) | Faction | ✓ B3-021 B3-023 | ☐ | ✓ B2-021 B3-007 B3-021 | ✓ B3-007 | In progress — F64 F65 F92 F93 F94 |
| M-035 | Domain Actions | Faction | ☐ | ✓ B2-021 | ✓ B2-026 | ✓ B2-021 | In progress — F36 |
| M-036 | Parliamentary Vote | Faction | ☐ | ☐ | ✓ B3-009 B3-016 | ✓ B3-016 | In progress — F68 F82 |
| M-037 | Grand Debate | Faction | ✓ B3-015 | ☐ | ✓ B3-009 B3-012 | ✓ B3-015 | In progress — F80 F81 |
| M-038 | Seasonal Accounting | Faction | ☐ | ☐ | ✓ B2-030 B3-030 | ✓ B3-021 | In progress — F107 |
| M-039 | Combat — Initiative | Combat | ✓ B2-022 | ☐ | ✓ B2-022 | ☐ | In progress — F37 |
| M-040 | Combat — Priority Table | Combat | ☐ | ✓ B2-022 | ✓ B2-022 | ☐ | In progress |
| M-041 | Combat — Attack/Defence | Combat | ☐ | ✓ B2-022 | ✓ B2-022 | ☐ | In progress |
| M-042 | Combat — Damage Formula | Combat | ✓ B2-023 | ☐ | ☐ | ✓ B2-023 | In progress |
| M-043 | Combat — Equipment (Weapons, Armour) | Combat | ✓ B2-023 | ☐ | ☐ | ✓ B2-023 | In progress |
| M-044 | Combat — Manoeuvres (Defend, Disarm, Trip, etc.) | Combat | ☐ | ✓ B3-020 | ✓ B3-020 | ✓ B3-020 | In progress — F90 |
| M-045 | Mass Combat | Combat | ✓ B2-024 | ☐ | ☐ | ✓ B2-024 | In progress — F41 |
| M-046 | Thread Operations in Combat | Cross-domain | ☐ | ✓ B2-029 | ☐ | ☐ | Batch 01 + B2-029 |
| M-047 | Thread Events in Social Scenes | Cross-domain | ☐ | ✓ B2-025 | ☐ | ✓ B2-025 | In progress — F42 F43 |
| M-048 | Scale and Scope (transition, multi-scope action) | Cross-domain | ☐ | ✓ B2-026 | ✓ B2-030 | ✓ B2-030 | In progress — F45 F51 |
| M-049 | Inquisitor Operations (CE, investigation procedure) | Institutional | ☐ | ✓ B3-014 | ✓ B3-011 B3-018 | ✓ B3-018 | In progress — F73 F86 F87 |
| M-050 | Riskbreakers (Deniability Debt, CE) | Institutional | ✓ B3-019 | ✓ B3-014 | ✓ B3-019 | ✓ B3-019 | In progress — F79 F88 F89 |
| M-051 | Devout Constraint (TS block, Dissonance Marks) | Character | ☐ | ✓ B2-025 | ☐ | ☐ | Batch 01 + B2-025 |
| M-052 | Concealment (operation hiding from observers) | Thread Ops | ✓ B3-017 | ☐ | ☐ | ✓ B3-017 | In progress — F84 F85 |
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

---

## Updated Coverage Summary (After Batch 03)
**Last updated:** 2026-03-27

**Mechanics with any coverage:** 56/56 (100% touched)
**Test cells complete (✓):** ~95/224 (~42%)
**Batches run:** 3 (90 total tests)

### M-021 Correction
M-021 was labelled "Taint Track (0–10)" — corrected to **Coherence Track (10→0)**. Taint was renamed to Coherence in CP14 Stage 17-P2 patch. No live Taint track exists.

### P1 Findings (Must Fix Before Compilation Gate)
| Finding | Mechanic | Issue |
|---------|----------|-------|
| **F25** | M-016 Pulling | Personal-scale Pulling has no counter-mechanic for non-practitioners — bypasses all social resistance/detection |

### High-Priority P2 Findings Requiring Design Decisions
| Finding | Mechanic | Issue |
|---------|----------|-------|
| F53 | M-009 | Intelligibility + Coherence double-compress Certainty maximum |
| F57 | M-021 | Coherence below 4 is mechanically terminal (recovery requires cooperation; cooperation undermined by seduction) |
| F58 | M-021 | +3D Thread bonus at Coherence 2–3 creates perverse Coherence-farming incentive |
| F59 | M-020 | ThS 0 recovery requires 3 seasons — campaign-disrupting |
| F61 | M-030 | TT 80+ may be unwinnable without specific high-TS characters in good ThS condition |
| F64 | M-034/M-035 | Ehrenwall coup trigger #1 undefined |
| F65 | M-034 | Torben loyalty decay rate not specified |
| F68 | M-036/M-037 | Baralta Sovereign Authority near-TC-neutral in expectation due to Heresy Investigation trigger |
| F82 | M-036 | Multi-party Parliamentary Vote resolution undefined |
| F88 | M-050 | "Exposed operation" definition absent — Debt trigger ambiguous |
| F93/F94 | M-034 | Revolution and Niflhel Intel starting values absent from faction table |
| F100 | M-020 | Intelligibility 0 → NPC; recovery paradox (player agency lost before recovery available) |
| F107 | M-038 | Revolution Stability floor near-certain over campaign; recovery procedure absent |

### Phase 3 Gate Remaining Requirements
- All 4 test cells for each mechanic
- All NPC unique-mechanic tests remaining: Almud (full TS Discovery scenario), Maret Uln (full practitioner arc), Torben (loyalty decay), Jarnstal (Templar independent action)
- All track terminal values not yet reached in scenario: Certainty 0 (Rendering Crisis scene), Coherence 0 (monstrous NPC event), ThS 0 (campaign Crisis)
- TD track thresholds (§12.7 unread — F104)
- §7.1 TT full threshold table (only partially confirmed from cross-references)
- §12.7 TD track campaign arc mechanics
- Zero untested P1 interactions (F25 remains open)
