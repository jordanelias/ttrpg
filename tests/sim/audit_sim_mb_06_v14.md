# SIM-MB-06 v14 — Historical Audit + NERS Analysis

**Session:** 2026-05-13
**Sim version audited:** v14 (commit `1cc27b2cda822b80c98f6ad0fdd394fc1ef7cd75`)
**Sim version preceding:** v13 (commit `c33aa93aee095df634f6c74f2d116bf6dc7dae6b`)
**Method:** Granular tick-by-tick instrumented record of two battles (H5 RF vs HS outstanding tension, H1 Line vs Line control) compared against (a) historical pre-firearms combat precedents and (b) acclaimed strategy-videogame precedents (Total War Medieval II / Three Kingdoms / Attila, Field of Glory II, Battle Brothers, Mount & Blade Bannerlord). Every existing mechanism and every proposed gap scored against project NERS criteria.
**Effort:** Max — full read of all referenced precedent material, full walkthrough of every tick, NERS scoring against canonical definitions.

## Companion artifacts

- `tests/sim/instrument_battle.py` — reusable instrumentation tool. Patches v14 sim with verbose per-tick logging; rendered markdown record produces the auditable raw data.
- `tests/sim/audit_record_v14_h5.md` — H5 RF vs HS seed 1000000 (the outstanding tension; B wins T8, RF routed at hp=2/20).
- `tests/sim/audit_record_v14_h1.md` — H1 Line vs Line seed 1000000 (control mirror; B wins this seed, statistically symmetric across 500 seeds at 51.6%).

## Audit framing — videogame vs literal history

Valoria is a videogame (Godot 4.6). Player won't experience 1346 — they'll experience what *acclaimed strategy games* have set as the bar for pre-firearms combat. The audit applies *both* frames: literal history grounds the bottom-up mechanism design, acclaimed-game precedent grounds the player-experience design. Where these conflict, player-experience wins (per identity: "videogame, not TTRPG").

**Acclaimed precedent set:**
- **Total War: Medieval II / Three Kingdoms / Attila** — real-time tactical, formation morale, fatigue, charge bonus, rout-then-rally, pursuit
- **Field of Glory II** — turn-based hex, cohesion as separate stat from HP, accumulated army-wide morale failure
- **Battle Brothers** — turn-based small-scale, per-warrior fatigue and resolve
- **Mount & Blade Bannerlord** — formation AI, morale per unit, charge bonus, rout-pursuit

**Common patterns across the acclaimed set:**

1. **Morale-as-separate-state from HP.** Units rout at low morale, not when destroyed. Player sees the rout as a visible event.
2. **Fatigue/cohesion as a third state.** Stamina-equivalent depletes through action; tired units fight worse but recover when out of contact.
3. **Charge bonus.** First impact deals extra damage; bonus expires after contact established. Surfaces cavalry-as-shock-arm.
4. **Formation cohesion check.** Loose/disordered units take penalties. Surfaces drill and discipline as strategic choices.
5. **Multi-phase battle resolution.** Engage → wear → break is visibly distinct, not a single curve to destruction.

## Executive findings — five top-level divergences

These appear when both frames (history + genre) point the same direction:

1. **Per-tick lethality ~5-10× too high.** H5 T2: A loses 15% HP in one tick. Historical: full ~10-15 min phase produced ~5% casualties. Genre: Total War / FoG II show first-contact damage but spread over visible time. Sim's tick-scale matches the historical phase-scale.

2. **No rout-at-casualty-threshold; battles run to ~100% destruction.** Historical: pre-modern formations broke at 5-15% during line fighting. Genre-universal: rout-at-morale-failure is the standard battle-ending event. v14 ends at hp=0 — neither historically nor genre-genre correct.

3. **No stamina/exhaustion.** Combat at full effectiveness regardless of duration. Multiple precedent sources: stamina is THE limiting factor. Every game in the acclaimed set has it.

4. **No rest/recovery between contact periods.** Push-of-pike accounts include explicit rest cycles. Genre: Total War units rest when not in contact. v14 has no withdraw-and-re-engage.

5. **Front-row-faster-than-rear-rank infantry speed is historically backwards.** Real Leuctra mechanism: the whole *unit* advanced obliquely at the same pace. v14's per-row speed (RF front=2, rear=1; HS wings=2, body=0) breaks formation cohesion — HS body detaches from wings in the sim, which would never happen in either history or any acclaimed game.

## Tick-by-tick H5 audit (RF vs HS, seed 1000000)

See `audit_record_v14_h5.md` for raw data. Key findings per tick:

**T1 (approach):** Both advance. HS body (row 5) static while wings advance — formation cohesion break.

**T2 (initial contact):** Both pools 6 after `-2` angle. A loses 3 HP / 20 (15%) in single tick. Angle mod -2 on both sides means both defenders see "rear" attack from global centroid drift — ghost flank issue. *Historical first-impact (krousis) is plausibly the highest-casualty moment, but sim sustains this rate.*

**T3 (continued contact + size drop):** RF size 3 → 2. Pool degrades 7 → 6. No rotation. 5 rear ranks (20 cells) unengaged and unused.

**T4 (counterattack window):** B finally takes 4 HP. Single-tick variance, not a structural mechanism. No fatigue model means there's nothing exploiting the opening.

**T5-T7 (RF degradation):** Continued 3-4 HP per tick. Total A casualties by T7 = 18/20 = 90%. Discipline penalty fires at T6 (size loss > discipline trigger — too late). Morale check first fires at T5 when size=1 — calibrated for 100%-destruction battles, not historical rout-thresholds.

**T8 (battle ends):** RF routed at size=0. Phase boundary fired at T6 with all 6 hooks no-op (by design).

## Per-existing-mechanism NERS

Canonical NERS definitions (project canon, PI `canon_terms`):
- **N**ecessary: removal worsens experience; supports cohesive experience from all directions
- **E**legant: logically simple; intuit complex outcomes from simple choices; no unnecessary overhead
- **R**obust: strategic thinking; customization; creativity; emergent narrative
- **S**mooth: integrates cleanly; zooms across scales; consistent calculation methodology

| Mechanism | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| Volley-before-melee | ✓ | ✓ | ✓ | ✓ | Genre-standard; cleanly bounded phase. Keep. |
| Per-cell octagon angle (flank/rear) | ✓ | ⚠ | ✓ | ⚠ | Concept is genre-standard; **implementation** (global centroid) creates ghost flanks. Keep concept, fix per G-5. |
| Cross-side speed-priority contention | ✓ | ✓ | ⚠ | ✓ | Currently fires only in asymmetric-speed cases. R light until cavalry exists. |
| Column-local targeting | ✓ | ✓ | ✓ | ✓ | Bottom-up formation discipline. Keep. |
| Cascading engagement (tip-first) | ✓ | ⚠ | ✓ | ⚠ | Concept right (wedge tip arrives first). E/S concerns: sub-phase grouping non-obvious to read; interacts in complex ways. Concept keep; consider simplification later. |
| **Per-row variable speed (RF front=2; HS wings=2 body=0)** | ✗ | ✗ | ✗ | ✗ | **Fails all four.** Oblique-order belongs at multi-unit timing. HS wings detach from body — artifact no acclaimed game shows. **Replace via G-6.** |
| support_engage_frac with 1.0 cap | ⚠ | ✓ | ✗ | ⚠ | Concept (rear ranks contribute) is genre-standard. Cap denies depth's real differentiation; R fails (both formations hit cap). Re-think when stamina lands. |
| Discipline penalty when losing more size than enemy | ✓ | ✓ | ✓ | ⚠ | Genre-standard concept. Trigger calibration too lenient. Fix when morale/stamina recalibration lands. |
| Morale degradation at size_max/2 and size_max/4 | ⚠ | ⚠ | ✗ | ✗ | Triggers too late. **Recalibrate under G-2.** |
| Phase boundary structure (v14) | ✓ | ✓ | ⚠ | ✓ | Scaffolding; R waits on hooks landing. |

## Per-proposed-gap NERS

| Gap | N | E | R | S | Priority |
|---|---|---|---|---|---|
| **G-1 Stamina** (depletes in contact, depth permits rotation, low stamina degrades pool) | ✓ | ✓ | ✓ | ✓ | **HIGH** — genre-standard; surfaces depth as strategic choice; cleanly separates "fresh advantage" from raw numbers. |
| **G-2 Rout-at-casualty-threshold** (morale check at phase boundary fires rout at ~25% casualties; pursuit damage next phase) | ✓ | ✓ | ✓ | ✓ | **HIGH** — genre-standard rout event; battle length feels right; commander decisions matter. |
| G-3 Per-tick lethality recalibration | ⚠ | ✓ | ⚠ | ⚠ | Likely falls out of G-1+G-2 (shorter battles via rout = lower total casualties). Defer; recalibrate from observation. |
| **G-4 Formation cohesion** (cells can't detach; sub-units losing parent contact lose autonomous advance) | ✓ | ✓ | ✓ | ✓ | **MEDIUM** — fixes HS-wings-detach; surfaces formation-as-strategy genre-standardly. |
| **G-5 Per-cell nearest-attacker angle** (replace global centroid) | ✓ | ⚠ | ✓ | ✓ | **MEDIUM** — fixes ghost-flank. E concern: implementation (lex-tiebreak asymmetry from earlier this session); needs symmetric form. |
| **G-6 Unit-pace speed** (replaces per-row speed) | ✓ | ✓ | ✓ | ✓ | **MEDIUM-HIGH** — strict improvement; oblique-order moves to multi-unit timing where it belongs. |
| G-7 Rally (degraded non-routed units recover at phase boundary via command roll) | ✓ | ✓ | ✓ | ✓ | **MEDIUM** — completes the rout/rally narrative arc. |
| G-8 Reform after withdrawal (disengaged units can re-engage in next phase) | ⚠ | ⚠ | ✓ | ⚠ | **MEDIUM-LOW** — coupling with G-1/G-2 needs careful design. Defer. |
| G-9 Threadwork | ⚠ | ? | ? | ? | Cannot NERS without design clarification from Jordan — scope unspecified. Hook exists; mechanism deferred. |
| G-10 Macedonian sarissa multi-rank projection | ⚠ | ⚠ | ⚠ | ⚠ | **LOW** — premature without stamina (which subsumes most of this). Defer. |
| **G-11 Cavalry mechanism** (charge-through, end-of-phase displacement, multi-charge cycles) | ✓ | ✓ | ✓ | ✓ | **HIGH** — genre-defining absence; charge bonus is *the* iconic pre-firearms tactic. **Blocked** until battery includes cavalry. Frame scaffolded. |

## H5 reframed for videogame

**Current player experience:** RF dies slowly while HS sits on it. Depth doesn't visibly matter. Player has no read on why one wins.

**After G-1 + G-2:** RF rotates fresh ranks forward (visible stamina restoration); HS wings exhaust (visible stamina depletion in wide-but-shallow formation); HS routs first at morale threshold; pursuit damage applies in next phase. Same target outcome (RF wins 50-65%) reached through a *visible* mechanism the player reads — depth as a tactical choice that pays off in stamina rotation. This is the Total War / Field of Glory pattern, applied to Valoria's design.

## Recommended next cycle

**G-1 + G-2 paired implementation on the existing phase-boundary hooks.** They're coupled:
- Stamina state on each unit; depletes per contact tick; depth permits rotation to refresh; degrades combat pool when low.
- Phase-boundary morale check uses casualty% + stamina state + discipline to determine rout threshold.
- Routed units exit field; pursuit damage applies as next phase's first action.

Implementation pattern:
1. Add stamina to Unit dataclass (init = high, depletes per contact tick observed in find_contacts).
2. Expose accessor for pool calc (degrade pool if stamina low).
3. Populate `stamina_check` hook: apply tick-deltas at phase boundary.
4. Populate `morale_check_phase` hook: compare casualties + stamina vs discipline-modified rout threshold.
5. Populate `rout_resolution` hook: set routed=True on threshold-failing units; queue pursuit damage for next phase.

Verify on instrumented H5 (regenerate via `instrument_battle.py`) plus full battery. Expected: H5 → 50-65% as RF's rotation advantage manifests. Other tests should improve or hold (no acclaimed-game precedent for them getting *worse* under stamina + rout).

## What v14 gets right (preserve)

Volley-before-melee · per-cell octagon angle CONCEPT · discipline degradation under heavy losses (calibration needs work, direction right) · cross-side cell contention via speed differential · column-local targeting · phase structure itself (6-tick lock-in) · cascading engagement resolution by depth · discipline-gated drift (low-discipline units lose advanced formations and revert to Line) · halt-via-pre_pairs at contact line.
