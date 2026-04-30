# Continued Audit — Batch 6
<!-- generated: 2026-04-29 | scope: social_contest, fieldwork, frac_province, ci_political -->

## APPLIED THIS SESSION

### 778bdcd — 20 auto-fixes (mass_battle, params, peninsular_strain, victory, derived_stats, canonical_sources)
### b7dcc20 — 4 stale-doc fixes (§0.3 Strain, Step 4d, Accord frozen, faction_layer §2.3)
### 63fda93 — CI-01: Church Prominent definition (OR Church controls territory)
### 0343b3bb — Batch 5 findings committed
### 82cc36d — FW-01 Domain Echo cap, FRAC-01 zero-guard, FRAC-03 Fragmentation Ob additive
### b208922 — ci_political §4.4 ED-743, CI 55 "Church Prominent" → "Institutional Reach"

## CONFIRMED CONSISTENT (batch 6)

- Social contest Composure→CT coupling: indirect via pool quality. N/E confirmed.
- Social contest CROSS + dual Obscuring: only larger-movement side triggers Doubt Marker. Clean.
- Fieldwork pool formula: consistent with combat and contest across all three systems.
- TS gates: hard capacity-based gates, no Beginner's Luck. Design pillar confirmed.
- Rattled→social fieldwork coupling: clean cross-system. S confirmed.
- Hybrid fieldwork offset vs contest track offset: different mechanisms, both correct.
- BG Parliament Church weakness: intended asymmetry. Church uses CI/Seizure path.
- Fractional PV math: formula correct.
- Fractional province Accord: controller penalised by adversary settlement. Intended.
- Fragmentation→Secession→RM: confirmed designed emergence pathway. R confirmed.
- CI bonus dice progression (floor CI/20): N/R/E confirmed. Large bonus at CI 80 intentional.
- Varfell 2× Tribune vs 1× Legionary: intentional tension (covert sustain + military expansion).
- Church Pontifex cooldown 2 seasons: BG abstraction of Thread cost. S confirmed.
- AI Priority 4 2-front counter (HF Suppress + Crown Treaty at CI 55): N/R confirmed.

## NEW GAPS

### [CI-02] Mass Seizure Ob — two different formulas
ci_political §2.1: Ob = 10 − PT − infrastructure (floor 1).
victory_v30 §3.2 (referenced but not fetched): Ob = 7 − PT.
ci_political adds "infrastructure" as a modifier; victory_v30 uses simpler base.
JORDAN DECISION NEEDED: which formula is canonical, and what is "infrastructure"?

### [CI-03] "Church Prominent" naming collision — FIXED (b208922)
CI 55 milestone renamed to "Institutional Reach." No longer collides with CI generation Prominent.

## JORDAN DECISIONS (batch 6 additions)

- CI-02: Mass Seizure Ob formula — 10−PT−infra (ci_political) vs 7−PT (victory_v30)?
- SOC-01: Hybrid §11 BG vote winner initiative carry-over (from batch 5)
- SOC-02: Chain contest lobbying vs carry-forward starting track (from batch 5)
- FW-02: Knot detection Cognition direction (from batch 5)
- FRAC-02: Consolidation Ob — ceiling vs floor convention (from batch 5)
- FRAC-04: Universal victory "all 15 territories" = all Seats confirmed? (from batch 5)

## CUMULATIVE APPLIED THIS SESSION (all batches)

Commits: 778bdcd, b7dcc20, 63fda93, 82cc36d, b208922
Files edited: mass_battle_v30, params/mass_combat, peninsular_strain_v30, victory_v30, 
              derived_stats_v30, canonical_sources, faction_layer_v30, ci_political_v30,
              fieldwork_v30, fractional_province_v30, military_layer_v30
Auto-fixes applied: ~30 across 11 files
Jordan decisions identified (total, all batches): ~26
Items confirmed consistent and closed: ~35
Bloat cut (reclassified as not-real-issues): 23
