# Simulation Report: SIM-STRESS-03
## Scenarios: Randomized (hash-seeded 2026-04-04)
## 1. contest_faction_boost_crowdsourcing
## 2. contest_church_tribunal_asymmetric
## 3. hybrid_dual_zoom_consequences
## 4. mass_battle_ttrpg_dmg_mod_verification
## 5. mass_battle_feigned_retreat_recognition
## 6. thread_coherence_depletion_war_scale
## Date: 2026-04-04
## Simulator Modes: A, C, D, G, K, M
## Model: Sonnet 4.6

---

## FINDINGS

### Scenarios 1–2: Social Contest

| ID | Severity | Description |
|----|----------|-------------|
| F-S3-01 | Design note | Audience boost available to any orator arguing boosted axis regardless of faction; correct |
| F-S3-02 | P1 | Resistance 4+ renders 3-exchange Formal statistically inert (~10% chance of track movement/exchange). SIM-DEBT-07 pending GM guidance note. |
| F-S3-03 | Design note | Doubt Marker disproportionately strong in high-resistance sessions; by design |
| F-S3-04 | P2 → Resolved | Forfeit does not consume Doubt Marker. Ruling: forfeit = losing; Doubt Marker persists. ED-165 resolved. |
| F-S3-05 | Design note | Inquisitor Obscuring loop: track-movement-free attrition by design |
| F-S3-06 | Design note | Tribunal biased start (6) = one movement ends trial; oppressive by design |
| F-S3-07 | P2 | "Division" undefined in §7 Church Tribunal. ED-166 open. |

### Scenario 3: Hybrid Dual Zoom

| ID | Severity | Description |
|----|----------|-------------|
| F-S3-08 | Design note | PP-252 info advantage (Attunement order) working correctly |
| F-S3-09 | P2 | CF wound on Zoom Out: no BG consequence defined. ED-167 provisional: +1 Ob BG tactic rolls |
| F-S3-10 | P2 | CF killed between sequential Zoom Ins: PC-A has no target. ED-168 provisional: redirect or free Zoom Out |

### Scenario 4: Mass Battle TTRPG Dmg Mod Verification

| ID | Severity | Description |
|----|----------|-------------|
| F-S3-11 | Design note | LightCut vs Medium armour = 0 damage; matches ✗ in weapon effectiveness table |
| F-S3-12 | ✓ RESOLVED | PP-245 TTRPG Dmg Mod produces 4–5 exchange battles. SIM-DEBT-05 CLOSED. |
| F-S3-13 | Design note | Discipline checks rare at scaled Dmg Mod values; concentrated effort required |

### Scenario 5: Mass Battle Feigned Retreat

| ID | Severity | Description |
|----|----------|-------------|
| F-S3-14 | Design note | Feigned Retreat Ob 3: ~26% success for Command 5; difficult by design |
| F-S3-15 | Design note | Recognition scales correctly with Command |
| F-S3-16 | P2 → Resolved | Feigned Retreat Discipline check Ob unspecified. PP-256: Ob 1. ED-169 resolved. |
| F-S3-17 | Design note | Feigned Retreat → Shield Wall tactical loop working correctly |

### Scenario 6: Thread at War Scale

| ID | Severity | Description |
|----|----------|-------------|
| F-S3-18 | GAP | Dissonant mechanical effects not in loaded docs. SIM-DEBT-06. |
| F-S3-19 | Design note | War-scale Ob 5 success ~55% for specialist practitioner; balanced |
| F-S3-20 | GAP | P-25 RS cost overrides require threadwork_redesign_v25.md; partial sim only |
| F-S3-21 | P2 | Coherence recovery during multi-day battle undefined. ED-170 provisional: 1/night rest. |

---

## CONFIRMED WORKING (this session)
- PP-245 (TTRPG Dmg Mod): SIM-DEBT-05 CLOSED
- PP-252 (Multiple Zoom Ins): Attunement ordering confirmed functional
- PP-250 (Zoom In phase-lock): No ghost-unit state in simulation

## SIM-DEBT REGISTER
| ID | Description | Status |
|----|-------------|--------|
| SIM-DEBT-01 | Social contest calibration (Cha×2 pool) | Open |
| SIM-DEBT-03 | Two-genre system re-sim | Open |
| SIM-DEBT-04 | Adjudicator-type pool calibration | Open |
| SIM-DEBT-05 | TTRPG mass battle Dmg Mod | **CLOSED — PP-245** |
| SIM-DEBT-06 | War-scale Coherence/Dissonant effects | Open — requires threadwork_redesign_v25.md §3 |
| SIM-DEBT-07 | High-resistance contest calibration (ED-164) | Open — GM guidance note pending |
