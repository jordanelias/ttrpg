# VALORIA — FULL MECHANICAL SCOPE MAP & AUDIT PLAN
## Date: 2026-03-29
## Purpose: Inventory all systems, flag untested/inconsistent areas, produce prioritized audit plan

---

# SYSTEM INVENTORY

## A. Core Engine (stage1)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Dice (d10 pool, TN, DoS) | §1.1–1.6 | Implicit in all sims | — | Stable |
| Momentum | §1.7 | SIM-X-06, X-07 | — | Stable; combat-tested |
| Beginner's Luck | §1.8 | None | — | Untested in isolation |
| Fibonacci Group Bonus | §1.9 | SIM-X-07 (mass), PP-149 | — | Edge case: Break Through stacking (PP-149) |
| Attributes (10-stat) | §2.1–2.2 | Implicit | G-097 (CLOSED) | BUG-002 name fix applied |
| Derived Scores | §2.3 | Implicit | G-119 | **Thread pool formulas wrong in §16.2** |
| Combat Pool Construction | §3.4 | SIM-X-01, X-06, X-07 | — | Tested |
| Wounds/Incapacitation | §3.8 | SIM-X-06, X-07 | **PP-131** | **PP-131 invalidated all prior combat sim data** |
| Stamina | §3.9 | SIM-X-06 | — | Tested |

## B. Characters (stage2)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Histories | §4.1 | Implicit | — | Stable |
| Beliefs | §4.2 | SIM-X-05 (Debate) | PP-144 | Belief bonus to Debate untested |
| Inspirations | §4.3 | SIM-X-02 | G-040 | **Mid-campaign acquisition needs design** |
| Thread Sensitivity | §4.4 | Batch 01–08, SIM-X | G-128 | **World track scope contradiction** |
| Intelligibility/Coherence | §4.5 | Batch 01–08 | G-106 (CLOSED), G-109 | **§4.5 vs §5.10 contradiction (CLOSED)** |
| Certainty | §4.6 | Batch 01–08 | — | Tested |
| Knots | §4.7 | SIM-X-05 (strain) | — | Tested in Grand Debate |
| Circles | §4.8 | None | G-054 | **Needs redesign** |
| Resources | §4.9 | None | G-048, G-054 | **Degradation undefined; needs redesign** |
| Advancement (CP) | §4.10 | None | G-053 | **Spending menu expansion needed** |
| Composure | §4.11 | SIM-X-02, X-05 | G-099 | **Mid-debate incapacitation unresolved** |

## C. Thread Operations (stage3)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Diagnosis | §5.1.2 | Batch 01–08 | PP-150 | Concealment pool revision pending |
| Leap | §5.1.3 | Batch 01–08 | PP-135, PP-141 | **Involuntary Leap chain prevention (P1)** |
| Weaving | §5.1.4 | Batch 01–08, SIM-X | PP-145 | Debate effect untested |
| Pulling | §5.1.4 | Batch 01–08 | G-118, G-125 | **No degree table; no social counter** |
| Locking | §5.1.4 | Batch 01–08 | — | Tested |
| Dissolution | §5.1.4 | Batch 01–08 | G-127, PP-136 | **Residue drains wrong track** |
| Mending | §5.1.4 | Batch 01–08 | — | Tested |
| Collective Ops | §5.1.5 | Batch 03–04 | G-116, G-117, G-134 | **Lattice scaling + anchor-drop undefined** |
| Coherence track | §5.2 | Batch 01–08, SIM-X | PP-139, PP-142 | Crisis in combat + during contact — patches pending |
| Co-Movement | §5.3 | Batch 01–08 | — | Version C confirmed |
| Rendering Stability | §5.4 | SIM-X-08 | — | Tested in seasonal cascade |
| Threadcut Beings | §5.5 | Batch 05–07, SIM-F | PP-137, PP-138, PP-140, PP-143 | **4 patches pending (De-Act, stabilisation, self-Pull, Coherence replacement)** |
| Cross-Mode Thread | §5.6 | None | G-057, G-120 | **Board game Thread procedure needs design** |

## D. Setting-Specific (stage4)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Southernmost | §6.1–6.8 | None | G-055, G-095 | **Expedition procedures need design; hybrid management undefined** |

## E. Clocks (stage5)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| RS (100→0) | §7.1 | SIM-X-08 | — | Tested in cascade |
| TC (0→100) | §7.2 | SIM-X-08 | G-103, G-114, G-136 | **TC pause interaction, seizure procedure, brake stat undefined** |
| IP (0→100) | §7.3 | None | G-044 | **Altonian pre-invasion presence undefined; never simulated** |
| Cross-Clock | §7.4 | SIM-X-08 (partial) | — | Single-cascade tested only |
| Passive Drift | §7.5 | None | — | **Never simulated** |
| BG Clock Rep | §7.6 | None | — | **Never tested** |

## F. Factions (stage6)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Faction Stats (6×1–7) | §8.1 | SIM-X-08 | G-133 | **Niflhel Intel stat undefined** |
| Domain Actions | §8.1 | SIM-X-08 | G-098 (CLOSED) | Ob formula fixed |
| Ethical Frameworks | §8.1 | None | — | Confirmed editorial; untested mechanically |
| Leader vs Institution | §8.1 | None | G-020 | **Mechanical separation needs design** |
| 9 Political Axes | §8.1 | None | G-022 | **Gameplay generator design needed** |
| 8 Faction Cards | §8.2–8.9 | SIM-X-05,07,08 | G-032 | **Asymmetric powers need design** |
| Schoenland | §8.10 | None | — | **Never simulated** |
| Parliamentary Vote | §8.11 | None | G-131 | **Coalition formation absent** |
| Seasonal Accounting | §8.12 | SIM-X-08 | G-132 | **Anti-death-spiral floor mentioned but unspecified** |

## G. Territories (stage7)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Territory Properties | §7.1–7.5 | None | G-029 | **15 territories undifferentiated** |
| Control Mechanics | §7.4 | None | G-034, G-037 | **Fortification + post-conquest governance need design** |

## H. Combat (stage8)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Personal Combat | §8.1–8.6 | SIM-X-01, X-06 | **PP-131** | **Wound system invalidated; re-sim needed** |
| Armour | §8.6 | SIM-X-06 | — | Tested |
| Group Combat | §8.8 | SIM-X-07 (partial) | — | Fibonacci + rescue tested |
| Mass Combat | §8.9 | SIM-X-03, X-04, X-07 | G-135, F-27 | **Damage formula unspecified; stalemate unresolved** |
| Siege | §8.9 (partial) | None | G-047, PP-147, PP-148 | **TTRPG siege undefined; BG patches pending** |
| Break Through | — | None | PP-149 | **New action — untested** |

## I. Social (stage9)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Composure/Rattled | §9.1 | SIM-X-02, X-05 | G-099 | Mid-debate incapacitation unresolved |
| Dispositions | §9.2 | None | — | **Never simulated** |
| Rhetoric | §9.3 | None | — | **Never simulated** |
| Reading Exchange | §9.4 | None | — | **Never simulated** |
| Appeals | §9.5 | None | — | **Never simulated** |
| Debates | §9.6 | SIM-X-02, X-05 | F-19, F-21, PP-144, PP-146, PP-151, PP-152 | **6 patches/findings open** |
| Chase | — | None | PP-153 | **New mechanic — untested** |

## J. Advancement (stage10)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Test Track | §10.1 | None | — | **Never simulated** |
| CP Awards | §10.2 | None | — | **Never simulated** |
| CP Spending | §10.3 | None | G-053 | **Menu expansion needed** |
| Renown | §10.5 | None | G-100 | **"Initial advantage" scope undefined** |

## K. Scale Transitions (stage11)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Scale Table | §11.1 | SIM-X-04 (partial) | G-105 (CLOSED) | Multiplier stacking resolved |
| Handoff Rules | §11.3 | None | G-080 | **12 cross-system handoff types undefined** |
| Scope Shift | §11.4 | None | — | **Never simulated** |

## L. Campaign Modes (stage12)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| TTRPG Mode | §12.1 | — | — | Structural, not mechanical |
| Board Game Mode | §12.2 | None | See BG section | — |
| Hybrid Mode | §12.3 | None | G-074–G-095 | **22 hybrid gaps — entire mode undesigned** |
| Mode Branching | §12.5 | None | G-023 | **Branching instances need documentation** |

## M. NPCs (stage13)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Named NPCs | §13.1–13.5 | SIM-X-05,06,07,08 | G-115 | **3 archetypes lack stat blocks** |
| Institutional Actors | §13.6 | None | — | **Never simulated** |
| NPC Faction Pools | §13.7 | SIM-X-08 | — | Tested in cascade |
| Faction Style Discovery | §13.8 | None | — | **Never simulated** |

## N. GM Tools (stage14)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Session Zero | §14.1 | — | — | Procedural checklist |
| Ob Calibration | §14.3 | None | — | **Never validated against sim data** |
| Discovery Events | §14.6 | None | G-111 | **Devout bypass unreachable** |
| Seasonal Accounting | §14.7 | SIM-X-08 | — | Tested |

## O. Spell Catalog (stage15)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Weaving catalog | §15.1 | SIM-X-01,03,05 | F-04, F-07 | W-24 balance issues open |
| Pulling catalog | §15.2 | Batch sims | — | Tested |
| Locking catalog | §15.4 | Batch sims | — | Tested |
| Dissolution catalog | §15.5 | Batch sims | — | Tested |
| Mending catalog | §15.6 | Batch sims | — | Tested |
| Quick References | §15.9 | — | — | Cross-ref only |

## P. Board Game Mode (stage_bg)
| System | Sections | Sim Coverage | Gap Status | Notes |
|--------|----------|-------------|------------|-------|
| Setup | B1 | None | G-030 | **Component spec needs design** |
| Territory Map | B2 | None | G-029 | **Territory differentiation needed** |
| Faction Cards | B3 | None | G-032 | **Asymmetric powers needed** |
| Turn Structure | B4 | None | G-025, G-026 | **Order set + round procedure need design** |
| Orders | B5 | None | G-059, G-060 | **Simultaneous placement + resolution ordering** |
| Military | B6 | None | G-033, G-046 | **Levy + unit composition need design** |
| Thread/Co-Movement | B7 | None | G-057 | **Thread procedure needs design** |
| NPC AI | B8 | None | G-031 | **Beyond 3-rule skeleton needed** |
| Event Deck | B9 | None | G-050, G-051 | **Event system + seasonal differentiation** |
| Victory/Endgame | B10 | None | G-028, G-021 | **Victory conditions need design** |

---

# COVERAGE SUMMARY

| Category | Systems | Sim-Tested | Untested | Open Gaps | Pending Patches |
|----------|---------|-----------|----------|-----------|-----------------|
| Core Engine | 9 | 7 | 2 | 1 | 1 (PP-131) |
| Characters | 11 | 5 | 6 | 5 | 1 |
| Thread Ops | 13 | 10 | 3 | 8 | 8 |
| Setting | 1 | 0 | 1 | 2 | 0 |
| Clocks | 6 | 2 | 4 | 3 | 0 |
| Factions | 10 | 3 | 7 | 5 | 0 |
| Territories | 2 | 0 | 2 | 3 | 0 |
| Combat | 5 | 3 | 2 | 3 | 3 |
| Social | 7 | 2 | 5 | 1 | 5 |
| Advancement | 4 | 0 | 4 | 2 | 0 |
| Scale Trans | 3 | 1 | 2 | 1 | 0 |
| Campaign Modes | 4 | 0 | 4 | 23 | 0 |
| NPCs | 4 | 2 | 2 | 1 | 0 |
| GM Tools | 4 | 1 | 3 | 1 | 0 |
| Spell Catalog | 6 | 5 | 1 | 2 | 0 |
| Board Game | 10 | 0 | 10 | 12 | 0 |
| **TOTAL** | **99** | **41** | **58** | **73** | **18** |

**Overall tested: 41%**

---

# CRITICAL BLOCKERS (must resolve before further compilation)

1. **PP-131 (wound system overhaul)** — invalidates all prior combat sim data. Must propagate into stage8, stage1, threadweaving_v25, then re-simulate.
2. **PP-141 (P1: involuntary Leap chain)** — cascading Leaps crash the game. Essential patch.
3. **8 editorial decisions pending** — block patch propagation (see valoria_patch_proposals.md bottom).
4. **G-135 (mass combat damage formula)** — mass combat unresolvable without this.
5. **F-27 (mass battle stalemate)** — no resolution mechanism; editorial decision required.

---

# PRIORITIZED AUDIT PLAN

## Priority 1: Resolve blockers (this session if possible)
1. Get user decisions on 8 pending editorial items
2. Propagate PP-131/132 into compilation stages
3. Apply PP-141 (Leap chain prevention)

## Priority 2: Re-simulate invalidated combat (1–2 sessions)
1. Personal combat with new wound system
2. Mass combat with damage formula defined (requires G-135 resolution)
3. Cross-mechanic: combat + Thread with updated wounds

## Priority 3: Fill critical design gaps — TTRPG (2–3 sessions)
| Gap | System | Why Critical |
|-----|--------|-------------|
| G-118 | Past-Oriented Pulling degree table | Most significant Thread op has no outcome table |
| G-125 | Personal Pulling social counter | No non-practitioner defence against Pulling |
| G-099 | Mid-debate incapacitation | Core social mechanic has unresolved edge |
| G-131 | Parliamentary Vote coalitions | Faction game dead without this |
| G-133 | Niflhel Intel stat | Covert faction has no covert stat |
| G-054 | Circles/Resources redesign | Economy system currently non-functional |

## Priority 4: Simulate untested core TTRPG systems (2–3 sessions)
- Social: Dispositions, Rhetoric, Reading, Appeals (stage9 §9.2–9.5)
- Advancement: Test Track, CP economy (stage10)
- Clocks: IP pressure, Passive Drift, cross-clock multi-season
- Factions: Schoenland, Parliamentary Vote, ethical framework mechanical impact
- Scale transitions: Scope Shift, full handoff chain

## Priority 5: Board Game mode (3–5 sessions)
- 12 design gaps (G-025 through G-060)
- Zero simulation coverage
- Entire mode needs: design → compile → simulate → iterate
- Depends on TTRPG systems being stable (shared foundation)

## Priority 6: Hybrid mode (2–3 sessions)
- 22 gaps (G-074 through G-095)
- Depends on both TTRPG and Board Game being stable
- Most complex mode; should be last

## Priority 7: Polish passes
- Ob calibration validation against sim data
- NPC stat block completion (G-115)
- Reference section corrections (G-119)
- Devout bypass fix (G-111)

---

# ESTIMATED TOTAL: 13–19 sessions remaining to complete audit + design + simulation cycle

| Phase | Sessions | Dependencies |
|-------|----------|-------------|
| Blockers + editorial | 1 | None |
| Combat re-sim | 1–2 | Blockers resolved |
| TTRPG design gaps | 2–3 | Editorial decisions |
| TTRPG sim coverage | 2–3 | Design gaps filled |
| Board game design | 3–5 | TTRPG stable |
| Hybrid design | 2–3 | BG + TTRPG stable |
| Polish | 1–2 | All above |

---

# IMMEDIATE NEXT ACTION
Resolve the 8 pending editorial decisions to unblock Priority 1–2.
