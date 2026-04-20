# Simulation Coverage Index

**Last updated:** 2026-04-19  
**Scope:** Master reference for all pre-engine-v4 simulation and design work

---

## Reading Order

1. **`designs/architecture/conflict_architecture_proposal.md`** — unified design proposal. Start here. Three-scale model, bishop appointment, graduated Löwenritter autonomy, Niflhel dissolution, Tensions Deck. Supersedes the ignition analysis.
2. **`designs/architecture/tensions_pair_validation.md`** — validates all 15 Tension card pairs against belligerent-target-opportunity criteria. 15/15 pass.
3. **`arc_test_batch3_results.md`** [PARTIALLY SUPERSEDED] — RS decay, Fort constraint, IP/Vanguard, campaign arc shape. These findings are the strategic timeline reference: expansion S1–10, seizure crisis S10–14, external pressure S19–30.
4. **`arc_test_batch4_results.md`** — PI track, RDT/TD, Accord revolt, Löwenritter Coup. Corrects B3-5 suppression race and B3-1 PT values.
5. **`arc_test_batch2_results.md`** — PP-666 stress tests. Corrects B1 sim bugs. Key findings: secession candidate restriction, RM Order=0 threshold, splinter Influence split.
6. **`arc_test_results.md`** [PARTIALLY SUPERSEDED] — PP-666 first pass. Valid for: settlement adjacency, fractional PV, succession contest, RM ascent arc shape. Invalid for: secession cooldown recommendation, RM Inf values, PV totals.
7. **`session_audit_2026-04-19.md`** — quality audit. 7 issues, 20 gaps, methodology notes.
8. **`early_game_ignition_analysis.md`** [SUPERSEDED] — historical precedents for ignition. §2 (six ignition mechanisms) is valid reference. All proposals superseded by conflict_architecture_proposal.

---

## Supersession Map

| Doc | Finding | Status | Superseded by |
|-----|---------|--------|---------------|
| B1 | Secession cooldown (2-season) recommended | ❌ Wrong mechanism | B2: restrict candidates to national factions |
| B1 | RM Inf = 55 | ❌ Sim bug | B2: RM Inf inflated on RM→RM no-ops |
| B1 | PV totals deterministic across seeds | ❌ Sim bug masked variance | B2: corrected dice produce variance |
| B3 | T9 PT buildup from low values | ❌ Wrong starting PT | B4: T9 PT=5 canonical (core.md) |
| B3 | Assert drives CI growth | ❌ Wrong — Piety Yield dominates | B4: Assert irrelevant at T9 PT=5 — but **B4 finding itself INVALIDATED by ED-721**: PT_tier non-linear; T9 yield = 1 CI/season floored, not 5. Assert IS relevant. Re-run pending. |
| B3 | PP-431-COR not modeled | ❌ Wrong suppression model | B4-1: corrected (Challenge replaces structural) |
| Ignition | Niflhel Provocation mechanic | ❌ Niflhel dissolved | Conflict architecture: settlement phenomena |
| Ignition | Tensions Deck 8 cards, draw 2, game-start fire | ❌ Wrong timing + scope | Conflict architecture: 6 external cards, draw 2, S8+ fuse |
| Ignition | Internal tension cards (C3,C5,C6 old versions) | ❌ Internal tensions should be emergent | Conflict architecture: all 6 cards external bilateral |

---

## Consolidated Gap List (20 items)

### Spec patches ready to write (3):
1. `fractional_province_ownership_v30 §2.6` — Secession candidates restricted to national factions (B2)
2. `faction_succession_split_v30 §4` — RM emergence threshold Order=0 clarification (B2)
3. `core.md` — Graduated Löwenritter autonomy replacing binary coup (conflict architecture proposal)

### Design decisions required from Jordan (4):
4. Splinter Influence split — 60/40 same as Mandate, or unsplit? (B2)
5. ~~CI seasonal cap vs Piety Yield at T9 — reduce SW from 5, or raise cap from ±5?~~ — **RESOLVED ED-721 (2026-04-20)**: formula ambiguity. PT_tier formalized as non-linear lookup (PT 5 → 1.0; …); T9 yields 1 CI/season floored. Cap not saturated. **Also ED-722**: SW unified as dynamic infrastructure aggregate.
6. T2 Kronmark garrison — explicit Crown priority tree entry, or accept T2 as exposed? (B3)
7. ~~Almud's father assassination — strike as backstory, make live via Royal Crisis card?~~ — **RESOLVED**: struck per Patch 7 (commit 7da338a); royal_assassination.md fuse spec + npc_behavior_v30 §5.2 Arc D maps for Almud/Torben/Lenneth (commit f63c0b4).

### Systems not yet specified (7):
8. AER generation mechanic — not in any read doc (B3)
9. Warden emergence behavior post-RS40 (B3)
10. Campaign-scale vs standard battle distinction (B3)
11. Coup Counter advancement sources — canonical events that increment (B4)
12. Coup effect on Crown Mandate (B4)
13. Seizure Failure consequences — Stability−1 + Casus Belli chain (B4)
14. Treaty mechanic interaction with Strain recovery (B4)

### Data gaps (6):
15. `settlement_adjacency_map.yaml` not authored (B1)
16. Fractional stake disposition on faction succession split (B1)
17. Contender pools for non-Varfell factions (B1)
18. RM Disposition toward Yrsa Vossen — settlement-level tracking (B1)
19. Consolidation Influence pool source per faction (B1)
20. PI upper-bound effects — Full Parliament band effects trivially met (B4)

---

## Campaign Arc Shape (Reference Timeline)

From B3 simulation at 2 battles/season:

| Season band | Events |
|-------------|--------|
| S1–S4 | Settlement governance friction ignites (5 starting fractional provinces). Tensions Deck fuses burning. Factions managing internal misalignments. |
| S4–S8 | Tension escalation. Bishop appointments possible. CI approaching 50. First military probing. Löwenritter may reach Restless. |
| S8–S12 | **Tension fires** (assassination, heresy, constitutional crisis, etc.). CI reaches 60 — Mass Seizure available. First Seizure attempt likely S10–15. |
| S12–S18 | Varfell breakout attempts. Church infrastructure accumulation visible. RDT/TD track advancing. Accord erosion in contested provinces. |
| S18–S22 | RS enters 79→60 band. IP approaches 75. Vanguard deployment imminent. |
| S22–S28 | Vanguard at T10, advances to T1 by S27. RS enters 59→40 band. Warden emergence. Late-game external pressure. |
| S28+ | Endgame. Victory conditions checked. RS collapse risk. Shared loss possible. |

---

## Coverage Map

| System | Batch | Confidence | Notes |
|--------|-------|------------|-------|
| Settlement adjacency | B1 | Medium | Road edges only; mountain/river/coastal untested |
| Fractional province ownership | B1, B2 | High | Multiple variants; bugs found and fixed |
| Faction succession split | B1, B2 | High | Mandate/Influence levers tested |
| RM emergence | B1, B2 | High | Order=0 threshold validated |
| CI/Mass Seizure timing | B3, B4 | High | PT values corrected in B4 |
| RS decay | B3 | High | Fully deterministic; verified |
| Fort constraint | B3 | High | 3 routes tested; T14 impassable at Mil 4 |
| IP/Altonian Vanguard | B3, B4 | Medium | AER not modeled |
| Hafenmark CI suppression | B3, B4 | High | PP-431-COR corrected in B4 |
| PI track | B4 | High | Stability confirmed; upper-bound effects weak |
| RDT/TD track | B4 | Medium | Simplified CI model |
| Accord revolt cascade | B4 | Medium | Treaty recovery absent |
| Löwenritter Coup | B4 | Medium | Counter advancement stochastic |
| Bishop appointment | — | Not tested | Proposed; needs engine_v4 |
| Graduated Löwenritter autonomy | — | Not tested | Proposed; needs engine_v4 |
| Tensions Deck | — | Not tested | Proposed; pair validation passed analytically |
| Three-scale resolution | — | Not tested | Structural; needs engine_v4 |
| Niflhel dissolution (settlement phenomena) | — | Not tested | Proposed; needs engine_v4 |

---

## Dice System Note

B1–B2 use simplified d10 (TN 7: 7+ = 1 hit). B3–B4 use full canonical d10 (1=−1, 7–9=+1, 10=+2). Same expected value per die (0.4), different variance. Impact on arc-level findings: negligible. Engine_v4 should use full canonical system.
