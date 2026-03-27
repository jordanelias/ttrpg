# VALORIA SIMULATION COVERAGE MATRIX
## Last Updated: 2026-03-27 (Schema v2 — 7-Dimension Tagging Enforced)

**Interaction cell definition:** ≥3 co-mechanics in a single test.
**Required for Phase 3 gate:** ≥28/56 mechanics (50%) with Interaction cell filled.
**Current Interaction coverage:** 25/56 (45%) — 31 mechanics below bar.

---

| ID | Mechanic | Domain | Modes Tested | Temporals | Tracks | Factions | NPCs | Archetypes | Iso | Int(≥3) | Scen | Edge | P1 |
|----|----------|--------|-------------|-----------|--------|----------|------|------------|-----|---------|------|------|----|
| M-001 | Core Dice Engine | Core | TTRPG | PRES | — | — | — | Generic | ✓ | ☐ | ☐ | ✓ | — |
| M-002 | Wound System | Core | TTRPG | PRES | — | — | — | Faction Leader | ✓ | ☐ | ☐ | ✓ | — |
| M-003 | Histories | Character | TTRPG | PAST/CROSS | TC,CERT | Crown,Revolution | Lenneth | Non-TS Scholar | ✓ | ☐ | ✓ | ✓ | — |
| M-004 | Beliefs (CP) | Character | TTRPG | PAST/CROSS | CERT | — | — | Generic | ✓ | ☐ | ✓ | ✓ | — |
| M-005 | Maxims (CP) | Character | TTRPG | CROSS | — | — | — | Generic | ✓ | ☐ | ☐ | ☐ | — |
| M-006 | Inspirations | Character | TTRPG | PRES | — | — | — | Faction Leader | ✓ | ☐ | ☐ | ✓ | — |
| M-007 | Conditions | Character | TTRPG | PRES | COMP,CERT | Crown,Church | Almud,Himlensendt | Generic,Faction Leader | ☐ | ☐ | ☐ | ✓ | — |
| M-008 | Thread Sensitivity | Thread | TTRPG | PAST/CROSS | TC,TS,CERT,CE | Varfell,Church | Vaynard,Klapp | Non-TS Scholar,Practitioner | ☐ | ✓ (≥3) | ✓ | ☐ | — |
| M-009 | Certainty Track | Thread | TTRPG | PAST/CROSS | CERT,ThS,TS,TD | — | — | Practitioner | ✓ | ✓ (≥3) | ☐ | ✓ | — |
| M-010 | Knots | Thread | TTRPG | CROSS | TS,INT | — | — | Practitioner | ☐ | ☐ | ✓ | ✓ | — |
| M-011 | Circles | Social | TTRPG | PRES | FSTAT,IP | Crown,Church | Elske | Faction Leader | ✓ | ☐ | ✓ | ✓ | — |
| M-012 | Resources | Social | TTRPG/BG/HYB | PRES/CROSS | FSTAT | Guilds,Crown | — | Faction Leader | ✓ | ☐ | ✓ | ✓ | — |
| M-013 | The Leap | Thread Ops | TTRPG | PRES | TS,TD,CERT | — | Almud | Practitioner | ☐ | ☐ | ✓ | ✓ | — |
| M-014 | Diagnosis | Thread Ops | TTRPG | PAST | TS | — | Vaynard | Practitioner | ✓ | ☐ | ☐ | ☐ | — |
| M-015 | Weaving | Thread Ops | TTRPG/HYB | PRES/CROSS | TT,TS,CERT,ThS | Revolution,Guilds,Varfell | Maret Uln | Practitioner,Faction Leader | ☐ | ✓ (≥3) | ✓ | ☐ | — |
| M-016 | Pulling | Thread Ops | TTRPG | PRES | TT,TD,TS | — | — | Practitioner | ✓ | ☐ | ☐ | ✓ | F25 |
| M-017 | FR—Lock | Thread Ops | TTRPG | PAST/CROSS | TS,TT,TD,ThS | Varfell,Church | Vaynard,Klapp | Practitioner | ☐ | ☐ | ☐ | ✓ | — |
| M-018 | FR—Dissolution | Thread Ops | TTRPG | PRES | TT,TD | — | — | Practitioner | ✓ | ☐ | ☐ | ✓ | — |
| M-019 | Past-Oriented Pulling | Thread Ops | TTRPG | PAST/CROSS | CERT,ThS,TS,TD | Varfell,Revolution | Maret Uln | Practitioner | ✓ | ✓ (≥3) | ✓ | ☐ | — |
| M-020 | ThS Track (world) | Thread Tracks | TTRPG/BG/HYB | CROSS | ThS,TT,TD | All | — | All Archetypes | ✓ | ✓ (≥3) | ✓ | ✓ | F57 |
| M-021 | Coherence Track | Thread Tracks | TTRPG | CROSS | TS,TD,TT,CERT,ThS | Niflhel | — | Practitioner | ✓ | ☐ | ☐ | ✓ | §4.5 |
| M-022 | Dissolution Residue | Thread | TTRPG | PRES | TD,TS | Niflhel,Varfell | Vaynard | Practitioner | ☐ | ☐ | ☐ | ✓ | — |
| M-023 | Collective Thread Ops | Thread Ops | TTRPG | PRES | TT,ThS,CERT,TD | Revolution | — | Practitioner | ✓ | ✓ (≥3) | ☐ | ✓ | — |
| M-024 | Shifting Objects | World | TTRPG/HYB | CROSS | TT,ThS,CERT | — | — | Practitioner | ✓ | ✓ (≥3) | ☐ | ✓ | — |
| M-025 | Gaps | World | TTRPG/HYB | CROSS | TT,ThS,CERT | — | — | Practitioner | ✓ | ✓ (≥3) | ☐ | ✓ | — |
| M-026 | Monstrous Entities | World | TTRPG/HYB | PRES/CROSS | TT,TS,CERT,CE,TC | Church | Himlensendt | Practitioner,Inquisitor,Knight Templar | ☐ | ☐ | ✓ | ✓ | — |
| M-027 | Southernmost Entry | Exploration | TTRPG | PRES/CROSS | TS,CERT,TD,ThS | Varfell,Revolution | Maret Uln | Practitioner | ☐ | ✓ (≥3) | ✓ | ☐ | — |
| M-028 | Locked Zones | Exploration | TTRPG | PRES | TS,CERT,TD | — | Maret Uln | Practitioner | ☐ | ✓ (≥3) | ✓ | ☐ | — |
| M-029 | The Forgetting | Exploration | TTRPG | PRES/CROSS | CERT,TS,ThS,TD | — | Maret Uln | Practitioner,Non-TS Scholar | ✓ | ✓ (≥3) | ✓ | ✓ | — |
| M-030 | Thread Tension | Global Tracks | TTRPG/BG/HYB | FUT/CROSS | TT,TC,ThS,IP,CERT,FSTAT | All | Multiple | All Archetypes | ✓ | ✓ (≥3) | ✓ | ✓ | — |
| M-031 | Theocracy Clock | Global Tracks | TTRPG/BG/HYB | FUT/CROSS | TC,TT,IP,ThS,FSTAT | Church,Crown,Hafenmark | Himlensendt,Baralta | Faction Leader | ✓ | ✓ (≥3) | ✓ | ✓ | — |
| M-032 | Altonian Pressure | Global Tracks | TTRPG/BG/HYB | FUT/CROSS | IP,TT,TC,FSTAT | Crown,Löwenritter,Altonian | Ehrenwall | Faction Leader | ✓ | ✓ (≥3) | ✓ | ✓ | — |
| M-033 | Clock Interactions | Global Tracks | TTRPG/BG/HYB | CROSS | TT,TC,IP,ThS,FSTAT,TD,CERT | All | Multiple | Multiple Archetypes | ☐ | ✓ (≥3) | ✓ | ✓ | — |
| M-034 | Faction Stats | Faction | TTRPG/BG/HYB | PRES/CROSS | FSTAT,TC,TT,IP,TS | All | Multiple | Faction Leader | ✓ | ☐ | ✓ | ✓ | F112 |
| M-035 | Domain Actions | Faction | TTRPG/BG/HYB | PRES/FUT/CROSS | FSTAT,TT,TC,IP | All | Multiple | Faction Leader,Löwenritter Knight | ☐ | ☐ | ✓ | ✓ | — |
| M-036 | Parliamentary Vote | Faction | TTRPG/BG | PRES/CROSS | FSTAT,TC,TT | Crown,Church,Hafenmark | — | Faction Leader | ✓ | ✓ (≥3) | ☐ | ✓ | F80 |
| M-037 | Grand Debate | Faction | TTRPG | PRES/CROSS | TC,FSTAT,COMP,CERT,IP,TT | Church,Hafenmark,Crown | Baralta,Himlensendt,Almud,Elske | Faction Leader | ☐ | ✓ (≥3) | ✓ | ✓ | — |
| M-038 | Seasonal Accounting | Faction | TTRPG/BG/HYB | CROSS | FSTAT,TT,TC,IP | All | Almud | Faction Leader | ✓ | ☐ | ✓ | ✓ | F83 |
| M-039 | Combat—Initiative | Combat | TTRPG | PRES | — | Crown,Löwenritter,Niflhel | Ehrenwall | Löwenritter Knight,Riskbreaker,Inquisitor | ✓ | ✓ (≥3) | ✓ | ☐ | — |
| M-040 | Combat—Priority Table | Combat | TTRPG/BG | PRES | FSTAT | Crown,Löwenritter,Niflhel | Ehrenwall | Löwenritter Knight,Riskbreaker | ✓ | ✓ (≥3) | ✓ | ☐ | — |
| M-041 | Combat—Attack/Defence | Combat | TTRPG | PRES | — | Crown,Löwenritter | Ehrenwall | Löwenritter Knight | ☐ | ✓ (≥3) | ✓ | ☐ | — |
| M-042 | Combat—Damage Formula | Combat | TTRPG | PRES | — | — | — | Generic,Löwenritter Knight | ✓ | ☐ | ☐ | ✓ | — |
| M-043 | Combat—Equipment | Combat | TTRPG | PRES | — | — | — | Löwenritter Knight | ✓ | ☐ | ☐ | ✓ | — |
| M-044 | Combat—Manoeuvres | Combat | TTRPG | PRES | TT,ThS | Crown,Löwenritter | Ehrenwall | Löwenritter Knight,Practitioner | ✓ | ☐ | ☐ | ✓ | — |
| M-045 | Mass Combat | Combat | TTRPG/BG/HYB | PRES/FUT/CROSS | FSTAT,TT,ThS | Löwenritter,Crown,Church Templars,Revolution | Ehrenwall | Löwenritter Knight,Faction Leader,Practitioner | ✓ | ☐ | ✓ | ✓ | F100 |
| M-046 | Thread Ops in Combat | Cross-domain | TTRPG/BG/HYB | PRES/CROSS | TT,ThS,FSTAT,TD,CERT | Crown,Löwenritter,Revolution | — | Practitioner,Löwenritter Knight | ☐ | ☐ | ☐ | ☐ | — |
| M-047 | Thread Events in Social | Cross-domain | TTRPG | CROSS | TT,TS,CERT | Church,Crown | Himlensendt,Almud | Practitioner,Devout Character | ☐ | ☐ | ☐ | ✓ | — |
| M-048 | Scale Transitions | Cross-domain | TTRPG/HYB | PRES/CROSS | FSTAT,TT,TC,IP | Crown,Church,Guilds,Revolution,Altonian | Almud,Vaynard | Faction Leader,Practitioner | ☐ | ☐ | ✓ | ✓ | — |
| M-049 | Inquisitor Operations | Institutional | TTRPG | CROSS | CE,TC,TS,CERT | Church,Crown | Olafsson,Klapp,Himlensendt | Inquisitor,Knight Templar | ☐ | ✓ (≥3) | ✓ | ✓ | — |
| M-050 | Riskbreakers | Institutional | TTRPG/HYB | PRES/CROSS | DD,TC,FSTAT,CE,TS,COMP | Crown,Church,Löwenritter | Ehrenwall | Riskbreaker,Inquisitor,Devout Character | ✓ | ✓ (≥3) | ☐ | ✓ | — |
| M-051 | Devout Constraint | Character | TTRPG | CROSS | CERT,TC,TS | Church | Himlensendt,Baralta | Devout Character | ☐ | ✓ (≥3) | ✓ | ☐ | — |
| M-052 | Concealment | Thread Ops | TTRPG | PRES/CROSS | CE,DD,TS,TC | Niflhel,Church | — | Riskbreaker,Practitioner,Inquisitor | ☐ | ✓ (≥3) | ☐ | ✓ | F78 |
| M-053 | Quick/Full Rest | Recovery | TTRPG | PRES | — | — | — | Generic | ✓ | ☐ | ☐ | ✓ | — |
| M-054 | Einhir Sites | World | TTRPG/HYB | PAST/CROSS | TT,TS,TC,ThS | Varfell,Revolution,Crown,Church | Vaynard,Klapp,Maret Uln | Non-TS Scholar,Practitioner | ☐ | ☐ | ✓ | ✓ | — |
| M-055 | Restoration Community Weaving | Faction | TTRPG/HYB | PAST/PRES/CROSS | TT,ThS,CERT,TC | Revolution,Church | Maret Uln | Practitioner,Faction Leader | ☐ | ✓ (≥3) | ✓ | ✓ | F89 |
| M-056 | Niflhel Destabilisation | Faction | BG/HYB | CROSS | FSTAT,TC,TT | Niflhel,Church | — | Riskbreaker | ☐ | ☐ | ✓ | ☐ | F84 |

---

## REQUIRED TESTS — High-Interaction Gap

The following 31 mechanics need a test with ≥3 co-mechanics. Suggested groupings prioritise mechanics that share tracks and contexts, so each test covers multiple needs simultaneously.

| Test Spec | Mechanics Addressed | Suggested Co-mechanics | Rationale |
|-----------|--------------------|-----------------------|-----------|
| Core+Wounds+Conditions under stress | M-001, M-002, M-007 | M-039 (combat), M-053 (rest) | All fire in same combat scene; TN/Ob shifts from wounds feed back into dice engine |
| Histories+Beliefs+Inspiration activation | M-003, M-004, M-006 | M-037 (Grand Debate) | Grand Debate is the canonical scene for all three character mechanics to resolve together |
| Maxims+Beliefs conflict in Devout character | M-005, M-007, M-051 | M-051 already ≥3 — add M-005 to next Devout test | Maxims cut but still in matrix; test should surface this formally |
| Knots+Leap+Diagnosis chain | M-010, M-013, M-014 | M-016 (Pulling) | Natural Thread operation sequence: Diagnosis → Leap → Pulling with Knot formation |
| Circles+Resources+Domain Action | M-011, M-012, M-035 | M-034 (Faction Stats) | Social capital mechanics feed directly into faction operations |
| Pulling+Lock+Dissolution chain | M-016, M-017, M-018 | M-021 (Coherence) | FR operations cascade; Coherence is the shared output track |
| Coherence+Dissolution Residue+Knots | M-021, M-022, M-010 | M-016 (Pulling) | Residue and Knots are both Coherence consequences; need multi-mechanic interaction test |
| Monstrous Entities+Inquisitor+Concealment | M-026, M-052, M-049 | already ≥3 in novel connections — verify M-026 tagged | Cross-reference T-07 |
| Faction Stats+Seasonal Accounting+Domain | M-034, M-035, M-038 | M-031 (TC) | Seasonal cycle is the primary context for all three faction operations |
| Damage Formula+Equipment+Manoeuvres | M-042, M-043, M-044 | M-002 (Wounds), M-039 | Full combat resolution requires all four; Wounds is the output |
| Mass Combat+Initiative+Priority Table | M-045, M-039, M-040 | M-002 (Wounds) | Mass combat is scale-up of the individual combat chain |
| Thread in Combat+Manoeuvres+Mass Combat | M-046, M-044, M-045 | already 2 in existing tests; add M-039 | Needs third co-mechanic to cross bar |
| Thread Events in Social+Circles+Grand Debate | M-047, M-011, M-037 | M-031 (TC) | Social scene with Thread intrusion; all three mechanics activate |
| Scale Transitions+Domain+Seasonal | M-048, M-035, M-038 | M-033 (Clocks) | Scale transition is the mechanism by which individual Thread events become faction events |
| Rest+Wounds+Conditions recovery | M-053, M-002, M-007 | M-039 (combat aftermath) | Rest resolves Conditions and Wounds; test as post-combat recovery chain |
| Einhir Sites+Weaving+Past-Oriented Pulling | M-054, M-015, M-019 | M-009 (Certainty) | Sites are the context for Thread operations across time |
| Niflhel Destabilisation+Faction Stats+Riskbreakers | M-056, M-034, M-050 | M-031 (TC) | Niflhel covert ops feed faction stat erosion; Riskbreakers are the mechanism |

---

## REQUIRED TESTS — Mode Coverage Gaps

| Priority | Mechanics | Missing Modes | Note |
|----------|-----------|--------------|------|
| High | M-001, M-002, M-006, M-007, M-010, M-013, M-014, M-016, M-018 | BG, HYB | Core + Thread Ops — board game and hybrid expressions needed |
| High | M-039, M-041, M-042, M-043, M-044 | BG, HYB | Combat mechanics — BG combat system untested |
| High | M-047, M-051, M-052, M-053 | BG, HYB | Character-level mechanics in non-TTRPG modes |
| Medium | M-003, M-004, M-005, M-008, M-009, M-011 | BG, HYB | Character background + TS in faction-level modes |
| Medium | M-021, M-022, M-050 | BG, HYB | Thread tracks + institutional mechanics in non-TTRPG modes |
| Medium | M-024, M-025, M-026 | BG | World-level mechanics in board game mode |
| Low | M-015, M-019, M-027, M-028, M-029 | BG | Exploration and specific Thread ops in BG mode |
| Note | M-056 | TTRPG | Currently BG/HYB only — needs individual-scale expression |

---

## PHASE 3 GATE STATUS

| Requirement | Status |
|-------------|--------|
| All 56 mechanics touched | ✓ |
| ≥50% mechanics with Interaction (≥3 co-mechs) | ✗ 25/56 (45%) — 3 more needed |
| All modes per applicable mechanic | ✗ 41 mechanics missing ≥1 mode |
| All temporal dimensions per mechanic | ✗ 56/56 missing ≥1 temporal |
| All named NPCs tested | ✓ |
| All archetypes tested | ✓ |
| All P1 findings resolved | ✗ 11 open |
| 7-dimension tags on all tests | ✗ Schema enforced going forward; retroactive tagging needed for B2–B4 |

---

## P1 FINDINGS (Open)

| # | Mechanic | Issue |
|---|----------|-------|
| F25 | M-016 | Pulling bypasses social counter-mechanics |
| F57 | M-020 | ThS world-track scope vs per-practitioner Fallout contradiction |
| F72 | TLK | Torben Loyalty Clock drain rate absent |
| F78 | M-052 | Concealment mechanic absent from ruleset |
| F80 | M-036 | Parliamentary Vote coalition mechanics missing |
| F83 | M-038 | Anti-death-spiral floor inverts intent (Ob 4) |
| F84 | M-056 | Niflhel Intel stat undefined |
| F89 | M-055 | Community Weaving TT cost scaling unspecified |
| F100 | M-045 | Mass combat damage formula absent |
| F112 | M-034 | Church Stability TC brake fires at start, suppresses TC permanently |
| §4.5 | M-021 | Intelligibility presented as standalone track; is Coherence dimension |