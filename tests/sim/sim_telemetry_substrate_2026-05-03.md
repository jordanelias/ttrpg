# Telemetry Substrate Simulation Report

**Date:** 2026-05-03
**Harness:** `tests/sim/sim_telemetry_substrate_2026-05-03.py`
**Substrate:** Phase 5a session 3.5 (`valoria-game` commit `b8b9a4a`)
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
All 8 from `scale_transitions_v30.md §4.3.2` (settlement_revolt, heresy_investigation_target, faction_leader_removal, mass_battle_at_settlement, companion_arc_trigger, knot_partner_crisis, stability_crisis, rank_advancement_recognition). Plus 5 World-State Priority 1 triggers from §4.3.3.

Per-trigger probabilities are calibrated from `engine_v3.py` observations (revolts, succession cascades, battle frequency) and reasoned estimates for the remaining triggers. Full calibration logic is documented inline in the harness `fire_mandatory_triggers()`.

[ASSUMPTION] These probabilities are model defaults. Real telemetry from playtests may shift them, especially for arc-driven triggers (companion, knot).

### Personas

| Persona | Difficulty | Base SA | Slate size | Taste profile |
|---|---|---|---|---|
| `narrative_completionist` | Narrative | 5 | 4-5 | balanced fieldwork/social |
| `normal_balanced` | Normal | 4 | 5-7 | even split |
| `normal_combat_focused` | Normal | 4 | 5-7 | combat-heavy |
| `hard_strategist` | Hard | 3 | 7-9 | strategic-heavy |

Player budget = `sa_base + Standing-modifier + Fatigue-modifier` per `player_agency_v30.md §6.2` (Standing 4-5: +1; 6-7: +2; Wounded: −1; Out of Breath: −1).

### Per-scene durations

[ASSUMPTION] Sourced from `campaign_modes_v30.md §12.3` TABLETOP timing table, halved for videogame mode (computer-paced not GM-paced):

| Trigger | system_id | base_minutes |
|---|---|---|
| settlement_revolt | combat | 8 |
| heresy_investigation_target | social_contest | 10 |
| faction_leader_removal | strategic | 6 |
| mass_battle_at_settlement | mass_battle | 14 |
| companion_arc_trigger | fieldwork | 7 |
| knot_partner_crisis | social_contest | 6 |
| stability_crisis | social_contest | 9 |
| rank_advancement_recognition | fieldwork | 5 |
| (Priority 1 triggers + electives, see harness) |

±25% jitter per scene. **These are placeholders.** Stage 5 of the time-review plan will replace them with measurements from Godot runtime once a playtest harness exists.

### Run scope

400 campaigns total: 4 personas × 100 campaigns × 40 seasons = 16,000 season-runs. Single-process runtime ≈ 5 seconds. Determinism verified (same seed → same `log_hash`).

---

## §3 — Headline findings

### Q1 — Mandatory zoom-in frequency

| Persona | Mean / season | p90 / season | Max observed |
|---|---|---|---|
| narrative_completionist | 1.13 | 1.6 | 1.91 |
| normal_balanced | 1.13 | 1.54 | 1.82 |
| normal_combat_focused | 1.15 | 1.64 | 1.9 |
| hard_strategist | 1.14 | 1.61 | 1.86 |

All four personas converge to **≈ 1.1 mandatory zoom-ins per season**, p90 near 1.6, max observed under 2 across 4,000 seasons each. Persona-independent — mandatories are world-driven, not player-driven, which is the canonical intent.

### Q2 — Saturation rate (any opportunity skipped)

| Persona | Saturation rate |
|---|---|
| narrative_completionist (5 SA) | 36.0% |
| normal_balanced (4 SA) | 95.9% |
| normal_combat_focused (4 SA) | 96.4% |
| hard_strategist (3 SA) | 100.0% |

At Normal, the player triages every season but the rare exception. At Hard, every season requires triage. At Narrative, two-thirds of seasons can pursue everything offered. **This matches the canonical design intent for `player_agency_v30.md §6.1`**: triage is the primary friction.

### Q3 — Mandatory overflow (mandatory triggers cannot all fit in budget)

| Persona | Mandatory overflow rate |
|---|---|
| narrative_completionist | 0.0% |
| normal_balanced | 0.0% |
| normal_combat_focused | 0.0% |
| hard_strategist | 0.0% |

**Across 16,000 simulated seasons, mandatory triggers never exceeded SA budget under modeled probabilities.** Even Hard difficulty (3 SA) absorbs the worst-observed 1.86 mandatories with room left. This is the most consequential structural finding: **the 4 SA budget is not crushed by mandatories under canon §4.3.2 trigger semantics.**

[CONFIDENCE: medium — the result is robust across personas and 16k runs, but trigger probabilities are modeling assumptions. If real arcs cluster mandatory triggers (e.g. mid-campaign crisis season firing settlement_revolt + stability_crisis + faction_leader_removal simultaneously), overflow could spike. Re-run with arc-driven trigger correlation modeling needed before strong conclusion.]

### Q4 — Per-system attention distribution

Across 40 seasons (placeholder durations). Headline numbers in minutes per campaign:

| Persona | combat | social | fieldwork | strategic | mass_battle | threadwork |
|---|---|---|---|---|---|---|
| narrative_completionist | 134 | 446 | 372 | 80 | 33 | 18 |
| normal_balanced | 225 | 304 | 257 | 133 | 30 | 19 |
| normal_combat_focused | 624 | 128 | 112 | 128 | 28 | 19 |
| hard_strategist | 91 | 173 | 147 | 228 | 29 | 18 |

Persona taste profiles produce sharply different system distributions. Combat-focused gets ~5x the combat minutes of strategic-focused.

### Q5 — Total campaign hours (placeholder durations)

Sum of all per-system minutes:

| Persona | 40-season campaign | Implied per game-year (4 seasons) |
|---|---|---|
| narrative_completionist | ~18 hours | ~1.8 hr/year |
| normal_balanced | ~16 hours | ~1.6 hr/year |
| normal_combat_focused | ~17 hours | ~1.7 hr/year |
| hard_strategist | ~12 hours | ~1.2 hr/year |

[ASSUMPTION] Placeholder durations. If real measurement shows scenes are 2× longer than tabletop-half, totals scale to 24-36 hours, putting Valoria in the same scale as longer-form grand-strategy titles. Stage 5 substantive question (replacing placeholders with measurements) is unblocked once a Godot playtest harness exists.

---

## §4 — Implications for the 4 SA / season decision

The 4 SA budget at Normal:

- **Does not break.** Mandatories always fit. Player always has 1-3 SA left for elective triage. Designed-tension between elective slate and budget is clean.
- **Saturates at 96%.** Player is making real triage choices every season. This is by design (`§6.1` "Normal is about triage"), not a bug.
- **Time-spend is short** under placeholder durations — about 16 hours for a 40-season Normal campaign. If Valoria targets longer (~40-50 hr) campaigns, either:
  - per-scene durations need to be longer than tabletop-half
  - season count needs to be longer than 40
  - SA needs to be higher (more scenes per season)

The decision between these three knobs is precisely the Stage 0 Jordan-decision flagged in the time-review plan: target campaign hours.

---

## §5 — What this simulation does NOT validate

1. **Per-scene durations.** All minute estimates are tabletop-anchored placeholders. Real measurement requires Godot playtest harness producing real `SceneTimer` JSONL.
2. **Mandatory-trigger probabilities.** Calibrated from limited engine_v3 observations + reasoned estimates. Arc-driven correlation between triggers (e.g. one crisis cascading multiple mandatories in one season) is NOT modeled.
3. **Player skip behavior on Priority 1 triggers.** Modeled as 60% pickup if budget allows, fixed across personas. Real player behavior likely varies more.
4. **GdUnit test pass.** The 8 GdUnit tests in `valoria-game/tests/test_scene_timer.gd` are written but UNVERIFIED — they have not been run against a Godot installation. The Python port verifies the data-flow logic of the substrate, not the GDScript runtime behavior.

---

## §6 — Determinism check (sim self-test)

```
Run 1 (seed=42)  log_hash: 1f24e0cac219e37d
Run 2 (seed=42)  log_hash: 1f24e0cac219e37d   [DETERMINISTIC]
Run 3 (seed=43)  log_hash: 3513baf0950fd03d   [DIFFERENT — seed change reflects in hash]
```

Confirms wall-clock is excluded from KeyStore content-hash, mirroring PP-687 V4 invariant in the GDScript implementation.

---

## §7 — Next actions

| # | Action | Status | Gating |
|---|---|---|---|
| 1 | Run Godot GdUnit suite against `valoria-game` to verify GDScript runtime | NOT-RUN | Godot install + dev cycle |
| 2 | Build Godot playtest harness emitting SceneTimer JSONL | NOT-STARTED | substrate is ready |
| 3 | Replace placeholder durations with measured per-scene elapsed_ms | BLOCKED | requires #2 |
| 4 | Model arc-driven trigger correlation; re-test mandatory overflow | OPEN | model refinement only |
| 5 | Stage 0 — Jordan-decision on target campaign hours | OPEN | Jordan |

[CONFIDENCE: high — substrate data-flow correctness, mandatory-frequency distribution shape, saturation-rate shape]
[CONFIDENCE: medium — absolute minute totals (placeholder-bound)]
[CONFIDENCE: low — mandatory overflow rate under arc-driven correlation (not modeled)]
[GAP: Godot runtime verification — requires execution environment outside this sandbox]
