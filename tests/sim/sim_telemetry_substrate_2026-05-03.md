# Telemetry Substrate Simulation Report

**Date:** 2026-05-03
**Harness:** `tests/sim/sim_telemetry_substrate_2026-05-03.py`
**Substrate:** Phase 5a session 3.5 (`valoria-game` commit `b8b9a4a`)
**Methodology version:** v2 (arc-driven trigger correlation; v1 used independent triggers)
**Status:** Stage 5 of time-review plan — partial (mandatory-frequency + saturation answers solid; per-system minutes are tabletop-anchor placeholders pending Godot runtime measurement)

---

## §1 — Purpose

Exercises the SceneTimer + TimeAggregator data-flow by porting both into Python and driving them with synthetic season-loops. Produces the two answers Stage 5 was designed to produce:

1. How often do mandatory zoom-ins fire per season?
2. How often does the 4 SA budget run out before the slate is exhausted?

Plus duration-conditional outputs (per-system minutes, time-per-SA distributions) that depend on placeholder durations from canonical tabletop estimates.

---

## §2 — Methodology

### Substrate port
Python mirrors of `Key`, `KeyStore`, `SceneTimer`, `TimeAggregator` are inline in the harness. Same record schema, same `log_hash()` content-hash determinism, same 5 aggregator queries. **PP-687 V4 invariant verified:** identical seed produces identical `log_hash` across runs (sim self-test in §6).

### Mandatory triggers
All 8 from `scale_transitions_v30.md §4.3.2`. Plus 5 World-State Priority 1 triggers from §4.3.3.

**v2 (current):** two-pass model.
- Pass 1: independent rolls per trigger (same as v1).
- Pass 2: arc-driven correlations. A fired trigger boosts probability of causally-linked siblings the same season.

Correlations modeled:

| If X fires | Y has bonus probability | Rationale |
|---|---|---|
| `stability_crisis` | `settlement_revolt` +30%, `faction_leader_removal` +20% | Stability collapse causes revolt and triggers succession |
| `mass_battle_at_settlement` | `settlement_revolt` +40% | Same contested province |
| `faction_leader_removal` | `companion_arc_trigger` +30% | Companion may be leader or tied to them |
| `heresy_investigation_target` | `knot_partner_crisis` +25% | Investigations target inner-circle |

[ASSUMPTION] Correlation magnitudes are reasoned estimates from arc canon, not measured.

### Personas

| Persona | Difficulty | Base SA | Slate size | Taste profile |
|---|---|---|---|---|
| `narrative_completionist` | Narrative | 5 | 4-5 | balanced fieldwork/social |
| `normal_balanced` | Normal | 4 | 5-7 | even split |
| `normal_combat_focused` | Normal | 4 | 5-7 | combat-heavy |
| `hard_strategist` | Hard | 3 | 7-9 | strategic-heavy |

### Per-scene durations

[ASSUMPTION] Sourced from `campaign_modes_v30.md §12.3` TABLETOP timing, halved for videogame mode. **Placeholders.** Stage 5b will replace with Godot measurement.

### Run scope

400 campaigns total: 4 personas × 100 campaigns × 40 seasons = 16,000 season-runs. Runtime ≈ 5 seconds. Determinism verified.

---

## §3 — v2 (correlation) headline findings

### Q1 — Mandatory zoom-in frequency

| Persona | Mean / season | p90 / season | Max observed |
|---|---|---|---|
| narrative_completionist | 1.31 | 2.02 | 2.37 |
| normal_balanced | 1.26 | 2.05 | 2.21 |
| normal_combat_focused | 1.25 | 1.98 | 2.29 |
| hard_strategist | 1.27 | 1.99 | 2.29 |

Persona-independent (1.25-1.31 mean). p90 lifts to ~2.0 (was ~1.6 in v1) — correlation produces "crisis seasons" where two mandatories fire together about 10% of the time.

### Q2 — Saturation rate (any opportunity skipped)

| Persona | Saturation rate |
|---|---|
| narrative_completionist (5 SA) | 36.6% |
| normal_balanced (4 SA) | 96.0% |
| normal_combat_focused (4 SA) | 95.9% |
| hard_strategist (3 SA) | 100.0% |

Unchanged from v1 — saturation is dominated by elective slate size, not mandatories.

### Q3 — Mandatory overflow

| Persona | Mandatory overflow rate |
|---|---|
| narrative_completionist | 0.0% |
| normal_balanced | 0.0% |
| normal_combat_focused | 0.0% |
| **hard_strategist** | **0.4%** |

**Hard difficulty (3 SA) now breaks 0.4% of seasons — about 1 in 250.** Under v1's independent triggers this was 0%. Under v2's correlation, "crisis seasons" with 3+ correlated mandatories occasionally exceed Hard's 3 SA budget.

This is the substantive finding: **correlation matters at Hard, doesn't matter at Normal.**

### Q4 — Per-system attention distribution (40-season campaign, placeholder durations)

| Persona | combat | social | fieldwork | strategic | mass_battle | threadwork |
|---|---|---|---|---|---|---|
| narrative_completionist | 134 | 442 | 375 | 79 | 32 | 17 |
| normal_balanced | 223 | 305 | 261 | 128 | 35 | 18 |
| normal_combat_focused | 635 | 132 | 115 | 130 | 29 | 19 |
| hard_strategist | 97 | 168 | 151 | 229 | 28 | 19 |

### Q5 — Total campaign hours (placeholder durations)

| Persona | 40-season campaign | Per game-year |
|---|---|---|
| narrative_completionist | ~18 hr | ~1.8 hr |
| normal_balanced | ~16 hr | ~1.6 hr |
| normal_combat_focused | ~17 hr | ~1.7 hr |
| hard_strategist | ~12 hr | ~1.2 hr |

[ASSUMPTION] Placeholder-bound. If real measurement shows scenes 2× tabletop-half durations, totals scale to 24-36 hours.

---

## §4 — v1 → v2 comparison

| Metric | v1 (independent) | v2 (correlated) | Δ |
|---|---|---|---|
| Mandatory mean / season (avg across personas) | 1.14 | 1.27 | +11% |
| Mandatory p90 / season | 1.60 | 2.01 | +26% |
| Mandatory max observed | 1.91 | 2.37 | +24% |
| Hard mandatory overflow rate | 0.0% | 0.4% | new |
| Normal mandatory overflow rate | 0.0% | 0.0% | unchanged |
| Saturation Normal | 96% | 96% | unchanged |

**Interpretation:** Correlation lifts cluster-frequency by ~25% at the tail (p90, max). Mean shifts moderately. The structural conclusion holds — 4 SA absorbs mandatories cleanly — but 3 SA shows a small failure mode (0.4%) under arc-driven clustering that was invisible under independent triggers.

---

## §5 — Implications for the 4 SA / season decision

The 4 SA budget at Normal:

- **Holds under correlation.** 16,000 simulated seasons, 0 mandatory overflows.
- **Saturates at 96%.** Designed friction.
- **Time-spend ~16 hr** for 40-season Normal campaign under placeholder durations.

The 3 SA budget at Hard:

- **Breaks rarely (0.4%) under correlation.** Acceptable failure mode for highest difficulty (≈ 1 broken season per 250). Player loses one mandatory scene to auto-resolve, which is exactly what `§4.3.2` specifies happens: "Remaining mandatory scenes resolve through NPC AI with reduced player influence."
- **Saturates at 100%.** Designed.

**Mandatory-overflow is not the bottleneck under modeled trigger semantics, even with correlation.**

---

## §6 — Determinism check (sim self-test)

```
Run 1 (seed=42)  log_hash: 1f24e0cac219e37d
Run 2 (seed=42)  log_hash: 1f24e0cac219e37d   [DETERMINISTIC]
Run 3 (seed=43)  log_hash: 3513baf0950fd03d   [DIFFERENT — seed change reflects in hash]
```

Confirms wall-clock is excluded from KeyStore content-hash, mirroring PP-687 V4.

---

## §7 — Direct answer: how long is a campaign / season / scene

**Canon has no videogame answer for any of these.** The three canonical anchors are tabletop-derived:

| Mode (canon §12.3, §12.4) | 10-season campaign | 1 season real-time | 1 scene |
|---|---|---|---|
| Board Game | 2-4 hr | ~15-20 min | n/a (no scenes) |
| Hybrid | 20-37 hr | 2-2.5 hr | 20-45 min |
| TTRPG | 45-100 hr | 3-8 hr | 60-90 min |

**Videogame (this sim's estimate, placeholder durations):**

| Persona | 40-season campaign | 1 season | Mean scene duration |
|---|---|---|---|
| Narrative | ~18 hr | ~27 min | 5-10 min |
| Normal | ~16 hr | ~24 min | 5-10 min |
| Hard | ~12 hr | ~18 min | 5-10 min |

[CONFIDENCE: low — bound to tabletop placeholders. Real measurement requires Godot playtest.]

These numbers will move with three independent levers Jordan must decide:
1. Target campaign hours (Stage 0 — the gate)
2. Season count per campaign (40 placeholder; engine_v3 default is 120 = 30 game-years = ~48 hr at Normal placeholders)
3. Per-scene videogame durations (measurement, not decision)

---

## §8 — What this simulation does NOT validate

1. **Per-scene durations.** Tabletop placeholders.
2. **Correlation magnitudes.** v2 correlations (0.20-0.40 ranges) reasoned, not measured.
3. **Pass 1 probabilities.** Calibrated from limited engine_v3 observations.
4. **Player skip behavior on Priority 1 triggers.** Stylized at 60% pickup.
5. **GdUnit test pass.** Tests in `valoria-game` written but UNVERIFIED — no Godot install.

---

## §9 — Next actions

| # | Action | Status | Gating |
|---|---|---|---|
| 1 | Run Godot GdUnit suite against `valoria-game` | NOT-RUN | Godot install + dev cycle |
| 2 | Build Godot playtest harness emitting SceneTimer JSONL | NOT-STARTED | substrate is ready |
| 3 | Replace placeholder durations with measured per-scene elapsed_ms | BLOCKED | requires #2 |
| 4 | Refine correlation magnitudes from real arc telemetry | BLOCKED | requires #2 |
| 5 | Stage 0 — Jordan-decision on target campaign hours | OPEN | Jordan |

[CONFIDENCE: high — substrate data-flow correctness, mandatory-frequency distribution shape, saturation-rate shape, determinism preservation, structural conclusion that 4 SA absorbs mandatories]
[CONFIDENCE: medium — absolute minute totals (placeholder-bound), 0.4% Hard overflow rate (correlation-magnitude-bound)]
[GAP: Godot runtime verification — requires execution environment outside this sandbox]
