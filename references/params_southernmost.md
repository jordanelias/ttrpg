<!-- version: v1.0 | source: designs/setting/southernmost_v30.md | last_updated: 2026-04-13 -->
<!-- PATCHES APPLIED: SIM-STH-E1 (2026-04-13) — combined TT reduction cap added -->
<!-- SIM STATUS: VERIFIED — forgetting checks, expedition Obs, ritual Ob calibrated -->

# params_southernmost.md — Southernmost Mechanics

## Zone Types
| Zone | Thread State | Primary Hazard |
|------|-------------|----------------|
| Snapped | Maximum tension | Objects crumble; configurations disrupt |
| Locked | Frozen at catastrophe moment | Configuration instability; Certainty drain |
| Oscillating | Continuous cycling | Gap formation; monstrous entities |

## Forgetting Check
Pool: Cognition + Recall. TN 8.
TS bonus: TS ÷ 20 (round down) additional dice.
| Exposure | Ob |
|----------|-----|
| Boundary zone < 1 hour | 1 |
| Interior 1–4 hours | 2 |
| Deep interior 4+ hours | 3 |
| Einhir core sites | 4 |

Degree outcomes:
| Degree | Retention |
|--------|-----------|
| Overwhelming | Full facts + TS 40+ retains ontological understanding |
| Success | Facts retained; threat context partially dissolved |
| Partial | Emotional impressions only |
| Failure | Nothing operational |

Testimony Ob penalty (non-practitioners using Southernmost knowledge in Appeals/Debates):
| Exposure depth | Ob penalty |
|----------------|-----------|
| Boundary | +1 |
| Interior | +2 |
| Deep interior / Core | +3 |

Probability reference (7D base, TN8):
| Ob | P(Retain facts) | P(Emotional only) | P(Nothing) |
|----|---------------|-------------------|-----------|
| 1 | 76% | 0% | 24% |
| 2 | 60% | 15% | 24% |
| 3 | 43% | 33% | 24% |
| 4 | 27% | 49% | 24% |

## Southernmost Awareness (Faction Stat)
Scale: 0–7 (or 0–10 for research-intensive factions).
Starting values: see params_factions_ttrpg.md.
Gate: [NAME-PENDING: ED-048] Ritual without Awareness 5+ → +2 Ob.

## Expedition Prerequisites
- Thread Tension ≥ 40
- Practitioner officer TS 30+
- Planning roll: relevant History, Ob 3
- Resources: Ob 3
- Military escort: recommended (1+ unit)

## Expedition Procedure — Multi-Season Extended Action
| Season | Phase | Key Roll |
|--------|-------|---------|
| 1 | Approach | Escort Discipline Ob 1; practitioner Discovery Event |
| 2 | Exploration | Three zones; one encounter per zone |
| 3 | Discovery | Diagnosis: TS 50+ auto; below TS 50: Ob 3 |
| 4+ | Repair (optional) | Extraordinary Repair Weaving Ob 3 |

## Zone Hazard Table
| Zone | Hazard | Roll | Ob | Fail consequence |
|------|--------|------|----|-----------------|
| Border (Snapped) | Shifting Objects | Weave or Agi | 2 | 1 Wound/character |
| Inner (Oscillating) | Monstrous entity | Combat | varies | Gap open, TT +2 |
| Core (Locked) | Config instability | Spirit (non-practitioners) | 2/round | Certainty −1 |

Core zone: Contact duration halved for practitioners.

## [NAME-PENDING: ED-048] Ritual
Requirements: ED-048 Text in possession; Awareness 5+ (else +2 Ob); lead TS 60+; 2 participants TS 20+; 1 season prep.
Roll: Weaving pool, Ob 5. Each participant TS 20+: +1D (max +4D bonus).
| Degree | Result |
|--------|--------|
| Overwhelming | Permanent stabilisation. TT −10. Southernmost settleable. |
| Success | Temporary. TT −6. Accessible 5 seasons. Re-attemptable. |
| Partial | TT −3. Forgetting Ob −1 permanent. Lead cannot retry; new lead required. |
| Failure | TT +8. Mode 3 entity at primary site. Lead Incapacitated. |

Probability reference (lead 18D + participants):
| Participants | Total pool | P(Success+) | P(Overwhelming) |
|-------------|-----------|------------|----------------|
| 0 | 18D | 80% | 42% |
| 2 | 20D | 87% | 53% |
| 4 | 22D | 92% | 63% |

## Extraordinary Repair Weaving
Requirements: Awareness 8+; expedition reaching primary site complete; practitioner TS 50+ assigned to Research.
Research roll: Recall + Einhir Scholar History, Ob 4.
Repair roll (each season): Weaving pool, Ob 3. −1D Core zone contact penalty.
| Degree | TT change | Other |
|--------|-----------|-------|
| Success/Overwhelming | TT −2 permanent | Awareness +1 |
| Partial | TT −1 | Practitioner CD +1 |
| Failure | TT +1 | CD +2 |

After 4-5 successful seasons: Southernmost fully stabilised.

## Combined TT Reduction Cap (SIM-STH-E1, PP-[NEXT])
<!-- PATCH: SIM-STH-E1 applied 2026-04-13 -->
Combined TT reduction from Southernmost operations (Ritual + Extraordinary Repair): max −5 per season.
Rationale: without cap, simultaneous Ritual + Repair can remove up to −12 TT/season,
enabling one-season resolution of the campaign's central threat. Cap preserves campaign tension.

## Crisis Timeline
| Trigger | Event |
|---------|-------|
| TT 50 | Outer winding strain — visible faction event fires; player warning |
| TT 50 sustained 3 seasons without stabilising Weave | Cracking begins — TT +1/season from Southernmost |
| Cracking 3+ seasons without Ritual attempt | Outer winding fails — TT +2/season, permanent until Ritual succeeds |

Stabilising Weave (pause cracking, not reverse): Ob 3, TS 40+, practitioner.

<!-- patch_history: to be created as references/params_southernmost_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
