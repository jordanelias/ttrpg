# Module 12 Report — Faction integration + CI political pool + battle consequences

**Date:** 2026-05-13
**Session:** Mode G Module 12 of `settlement_mgmt_stress_01` — **last functional module before M13 integration runner**
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_12_faction_integration.py`

**Canonical sources read at full depth:**
- `designs/provincial/faction_layer_v30.md` §1 (Stability redesigned), §9 (CI formula)
- `designs/provincial/ci_political_v30.md` §3 (CI as Political Legitimacy)
- `designs/provincial/mass_battle_v30.md` §E.1 (Immediate Battle Consequences), §E.2 (Deferred Accounting Consequences)

## Summary — M12 closes three throughline gaps in one session

Module 12 binds the canonical faction-layer surface and closes three throughline coverage gaps that have persisted since M8's retroactive audit:

1. **T-21 Thread Political Warfare** — PRIMARY. Previously unbound. The faction Mandate / Stability mechanics IS the political warfare layer T-21 names. M12 wires §1 Stability triggers + §9 CI formula + §3.2 CI bonus dice as the canonical mechanism.
2. **T-24 Convergence as Crisis** — PRIMARY. Previously unbound. Multiple Stability triggers converging in one season (e.g., capital loss + Suppress failure) produce emergent crisis. M12 wires the cascade check; T40 validates the canonical "Stability cascade per §1.2 ≥2 attribute losses in one season."
3. **М-6 CHOICE IS FORCED** — PRIMARY at sim level. Previously unbound primary across all 11 prior modules. Capital-territory double-magnitude penalty + Suppress-failure named exception force canonical choice architecture. T39 validates the sovereignty-vs-survival forced choice.

## Isolation tests — 40/40 PASS

Highlights:
- T1–T8: FactionStats + StabilityTrigger surface; canonical -1/-2/-3 magnitudes by trigger + capital-territory escalation
- T9–T13: §9 CI Formula integration — Institutional Momentum (+1/season), Baralta structural suppression (-1 when Mandate ≥ 4), seasonal caps (±3 player DA, ±5 all sources)
- T14–T16: §3.2 CI bonus dice canonical worked examples — CI 28 → +1D, 40 → +2D, 100 → +5D
- T17–T19: §3.3 CI Mandate reduction — 0-29 → 0, 30+ → -1, 90+ → -3
- T20–T22: §E.1 Battle MS penalty (standard -1, Campaign/War -2)
- T23–T27: §E.2 deferred IP/Strain advance via peninsular_strain thresholds
- T28–T31: `apply_battle_consequences` mutates clock_state.ms + surfaces conquered/defender territories
- T32–T34: `bind_faction_standing_delta` translates M3-M11 ActionResult signals to canonical Mandate/Influence/Stability deltas
- T35–T37: throughline + meta-throughline coverage queryable

**Cross-module emergent validations:**
- **T38 Emergent MS composition:** M9 year-decay (72 → 71) + M12 campaign-battle penalty (71 → 69) compose naturally. M9 and M12 both mutate the same clock_state.ms; the composition emerges from shared state.
- **T39 Forced-choice capital penalty:** Capital-territory occupation produces -2 Stability vs -1 for non-capital. Same trigger function, capital flag toggles the magnitude. The doubled penalty IS the forced-choice mechanism.
- **T40 Convergence-as-crisis cascade:** Crown at Stability 4 sustains capital formal loss (-3 → Stability 1) + Suppress failure (-1 → Stability 0 = eliminated). Two triggers in one season → faction eliminated. **The canonical Stability cascade emerges from atomic trigger composition, not from a dedicated cascade controller.**

## Throughline coverage — final tally after M12

| T-NN | Title | Primary М | Modules | M12 contribution |
|---|---|---|---|---|
| T-01 | Everything Is Thread | М-3 | M6 | — |
| T-03 | Inseparability | М-3 | M10 | — |
| **T-04** | MS Decay | М-1 | M9, **M12** | EXTENSION — §E.1 immediate battle MS -1/-2 augments M9 |
| T-05 | CI Accumulation | М-1 | M9 | — |
| T-06 | IP Accumulation | М-1 | M9 | — |
| T-07 | Turmoil | М-1 | M9 | — |
| **T-08** | Church Rendering Reinforcement | М-4 | M4, **M12** | EXTENSION — §3.2 + §3.3 CI political pool |
| T-11/15a/15b/15c | Faction substrate-postures | М-4 | M5 | — |
| T-15 | Player Progression | М-5 | M5, M8, M11 | — |
| T-18 | Radiation Gradient | М-2 | M1, M2 | — |
| T-19 | Southernmost Hidden Front | М-2 | M2, M7 | — |
| **T-20** | Two Contests | М-6 | M7, M8, M11, **M12** | EXTENSION — capital double-magnitude forces sovereignty-vs-survival |
| **T-21** | Thread Political Warfare | М-4 | **M12 NEW PRIMARY** | **closes prior-unbound primary** |
| T-22 | Belief Lattice | М-6 | M4 | — |
| T-23 | NPC Arc Emergence | М-5 | M6, M8, M11 | — |
| **T-24** | Convergence as Crisis | М-5 | **M12 NEW PRIMARY** | **closes prior-unbound primary** |
| T-25 | Generational Arc | М-5 | M8, M9 | — |
| T-26 | Recursion as Setting Structure | М-5 | M11 | — |
| T-27 | Effects Real Explanation Wrong | М-4 | M10 | — |
| T-30 | Information Asymmetry | М-8 | M6, M10 | — |

**Total: 20 distinct throughlines bound across 12 modules** (T-21 and T-24 new primary in M12).

## Meta-throughline final status

| Meta | Primary bindings | Status after M12 |
|---|---|---|
| М-1 PRESSURE IS CONTINUOUS | M9 | bound |
| М-2 GEOGRAPHY HOLDS PRESSURE | M2, M7 | bound |
| М-3 SUBSTRATE GROUNDS ALL | M1, M2, M6 | bound |
| М-4 INSTITUTIONS STAKE POSTURES | M3, M4, M5, M11, **M12** | bound (strongest tally — 5 modules) |
| М-5 SCALES CONNECT | M5, M8, M11 | bound |
| **М-6 CHOICE IS FORCED** | **M12** | **NEWLY BOUND at sim level (last prior-unbound primary closed)** |
| М-7 BORROWINGS OPERATIONAL EXTENSIONS | M10 | bound |

**ALL SEVEN PRIMARY META-THROUGHLINES NOW PRIMARY-BOUND.** This is the structural completion target Module 13 audit will verify.

Note on М-6: character-layer forced-choice throughlines (T-12 Practitioner Arc, T-13 Certainty Journey, T-17 Companion Moral Mirror) remain outside settlement-management sim scope — they belong in character-layer sims. Module 12 binds М-6 at the *institutional choice* layer via Stability triggers, which is the canonical sim-scope binding.

## §1 Stability Triggers — canonical surface

```
StabilityTrigger (enum) — 5 canonical triggers per §1.2:
  TERRITORIAL_OCCUPATION         -1 (capital: -2)
  TERRITORIAL_LOSS_FORMAL        -1 additional (capital: -3 total)
  CAPITAL_OCCUPATION             -2 (direct trigger)
  CAPITAL_LOSS_FORMAL            -3 (direct trigger)
  SUPPRESS_FAILURE               -1 (§9 Step 4 named exception)

apply_stability_trigger(stats, trigger, is_capital) -> int
is_eliminated(stats) -> bool   # Stability 0 in BG mode
```

## §9 CI Formula integration

```
CI_INSTITUTIONAL_MOMENTUM = 1                           # Step 1 baseline
BARALTA_STRUCTURAL_SUPPRESSION_MANDATE_THRESHOLD = 4   # Step 5 trigger
BARALTA_STRUCTURAL_SUPPRESSION_MAGNITUDE = 1           # Step 5 effect
CI_PLAYER_DA_SEASONAL_CAP = 3                          # Step 6 player cap
CI_ALL_SOURCES_SEASONAL_CAP = 5                        # Step 6 total cap

ci_institutional_momentum() -> int
ci_baralta_suppression(baralta_mandate) -> int
apply_ci_seasonal_cap(raw_delta, from_player_da) -> int   # clamps at ±3/±5
```

## §3.2 / §3.3 CI Political Pool

```
CI_BONUS_DICE_DIVISOR = 20      # Church bonus dice
CI_MANDATE_REDUCTION_DIVISOR = 30   # anti-Church Mandate reduction

ci_bonus_dice(ci) -> int                    # +1D per 20 CI
ci_mandate_reduction(ci) -> int             # -1 Mandate per 30 CI (cap 3 at CI 90+)
```

Canonical worked-example values match: CI 28 → +1D, 40 → +2D, 60 → +3D, 80 → +4D, 100 → +5D.

## §E.1 / §E.2 Battle Consequences

```
BattleScale (enum) — SKIRMISH, STANDARD, CAMPAIGN, WAR
battle_ms_penalty(scale) -> int             # -1 standard, -2 Campaign/War

CONQUEST_ACCORD_RESET_VALUE = 1             # §E.1 conquest → Accord 1
DEFENDER_TERRITORY_BATTLE_ORDER_PENALTY = 1 # §E.1 battle site Order -1

ip_advance_from_contested_territories(n) -> int    # 0-1 → 0; 2-3 → +1; 4-5 → +2; 6+ → +3
strain_advance_from_contested_territories(n) -> int  # +1/territory, cap 3

apply_battle_consequences(...) -> BattleConsequenceReport
```

## bind_faction_standing_delta — signal binding

M3-M11 modules returned `ActionResult.faction_standing_delta` as coarse ±N signals. M12 binds these to canonical FactionDeltaBinding(mandate, influence, stability):

| Raw delta | Mandate Δ | Influence Δ | Stability Δ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| +1 | 0 | +1 | 0 |
| +2 | +1 | +1 | 0 |
| +3 or more | (raw-1) | +1 | 0 |
| -1 | 0 | -1 | 0 |
| -2 | 0 | -1 | -1 |
| -3 or less | 0 | -1 | (raw+1) |

Module 13 integration runner consumes this binding to apply ActionResult signals to faction state.

## Findings status after M12

**No new findings this session.** M12 fetched 3 fresh canonical sources (faction_layer_v30, ci_political_v30, mass_battle_v30) at full depth, and all canonical values matched their stated form — no drift surfaced. The faction-layer / CI / battle-consequence surface is well-maintained relative to the settlement-layer surface where 7 type-taxonomy drifts and 5 documentation drifts have surfaced.

Total: 18 findings (1 resolved, 1 partial, 16 open) — unchanged.

## Cumulative status after M12

- **12 modules verified · 377 isolation tests · ~245 ledger entries · 18 findings**
- **All committed to GitHub at `jordanelias/ttrpg/main`**
- **20 distinct throughlines bound across 12 modules** (T-21, T-24 newly primary)
- **ALL 7 PRIMARY META-THROUGHLINES NOW PRIMARY-BOUND** (М-6 newly bound at sim level via Stability triggers)
- **1 module remaining: M13 (integration runner + NERS audit)**

## Bottom-up emergent — sustained across all 12 modules

Six chains demonstrate composition through shared state:

1. **M6 T43:** Famine → Order → Revolt (pure predicate composition)
2. **M7 T41:** Siege → Order erosion → Revolt (tick + predicate composition)
3. **M9 T35:** 30-year canonical simulation matches §7.1 to the integer (M-1 substrate over 120 seasons)
4. **M10 T27:** Governance failure → black market emergence (M9 + M10 predicate composition)
5. **M11 T30:** Settlement REVOLT → province effect → national effect (Domain Echo functional composition)
6. **M12 T38, T40:** M9 + M12 MS composition; Stability triggers compose into elimination cascade

Each chain emerges from atomic operations with no controller object; composition through shared state and ordered execution.

## Next session — Module 13 (Integration runner + NERS audit) — FINAL MODULE

Module 13 will:
1. **Compose all 12 modules into the per-season integration runner** — extend M9's `per_season_accounting` to also drive M10 dissolution emergence, M11 Domain Echo, and M12 battle consequences
2. **Mode A→B→C→D→50-seed batch** — the canonical Mode G integration progression
3. **NERS framework audit (Necessary/Robust/Smooth/Elegant × 6 directions)** — 24-cell per-direction × per-property grid
4. **Consume the queryable throughline coverage dicts** from M8/M9/M10/M11/M12 to verify coverage matches the throughlines_meta canonical T-NN catalog
5. **Consume the §8.1 SystemImpacts catalogue** from M10 to verify each system has had its impact realized somewhere in M1-M12
6. **F6 Mode-C blocker resolution attempt** — the pre-PP-726 S-ID granularity drift in geography YAML remains; Module 13 will surface whether the sim can proceed past Mode-C or whether F6 is structural
7. **Pattern audit synthesis** — the 7-surfacing type-taxonomy drift family + 5-surfacing documentation drift family are the highest-impact pending editorials; Module 13 will recommend the editorial sequence

After M13, the settlement_mgmt_stress_01 simulation is structurally complete.
