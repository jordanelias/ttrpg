# Integration Survey + Mechanical Stress — `sim/` Package (Stages 2-4)

**Status:** Audit / survey + stress record. Class-C findings, Jordan-vetoable.
**Date:** 2026-06-06. **Scope:** the unified `sim/` package (62 modules).
**Pipeline:** wire (Stage 2 — committed `db639e51`) → survey (Stage 3) → stress + log (Stage 4).
**Method:** AST dependency + status scan of all 62 `sim/` modules; in-container execution of `mc_v18` — no-regression baselines (seeds 42, 7) + a complete **120-campaign instrumented** stress battery (win-path attribution wraps `victory.check_all_factions`).

> **[CORRECTION — supersedes the initial 44-campaign cut of this doc]** The first pass time-truncated the battery at 44/80 campaigns and left win-attribution uninstrumented. This revision runs the full N=120 with GD-1-vs-fallback instrumented. Two findings changed materially: (1) **Hafenmark 0% → 0.8% (1/120)** — the "no viable path" claim was a small-sample artifact; a path exists but is marginal. (2) **GD-1-vs-fallback gap RESOLVED**: GD-1 victory fires **0/120**, the territory fallback decides **100%** — the canonical victory is categorically inert, not merely rare. Other figures held within sampling noise.

`[READ:]` sim/autoload/{game_state,scene_slate,season_manager,victory,dice_engine,registry}.py · sim/peninsular/season.py · sim/cross_scale/{zoom_in_out,handoff_rules,scene_dispatch}.py · sim/personal/{combat,contest}.py · sim/mc_v18.py · sim/provincial/faction_action.py · full-tree AST scan.

---

## SCOPE CAVEAT (load-bearing — read first)

The personal / thread / world layers are **structurally wired** to the strategic loop (Stage-2 seam) but **semantically inert**: the context-derivation bridge (aggregate faction state → concrete scene actors) and the outcome→echo mapping are unbuilt (flagged gaps), so personal-scene outcomes do not yet feed strategic state. This stress therefore exercises **the strategic layer + the wired-but-inert seam**, NOT a fully-composed multi-scale system. Findings are scoped accordingly. After this pass: spine + seam wired and running; semantic multi-scale composition gated on the derivation bridge.

---

## STAGE 2 — WIRE (recap; committed `db639e51`)

`sim/cross_scale/scene_dispatch.py` (new) + `mc_v18` caller-side hook connect the seam: trigger-eval → `scene_slate` → `zoom_in` → live resolver → `zoom_out`. Verified: triggers fire on real world-state; injected actors resolve end-to-end via `run_contest`; `run_batch(10)` byte-identical to baseline (side-effect-free). 7 of 8 §4.3.2 triggers deferred (world-state schema absent) — flagged, not faked.

---

## STAGE 3 — SURVEY: modularity / architecture / logic

**Inventory.** 62 modules — 12 `[CANONICAL]` (live), 28 substantial-but-untagged, 32 stub. Scales: `autoload` (spine), `personal`, `provincial`, `territory`, `peninsular`, `thread`, `world`, `cross_scale` (bridge), `mc_v18` (driver).

**Layering — sound overall.** Cross-layer import direction is correct: scale layers → `autoload` spine (provincial→autoload x12, personal→autoload x7, ...); `cross_scale` → personal/autoload (bridge depends on what it connects); `mc_v18` → autoload/provincial/peninsular/cross_scale (driver orchestrates). No leaf-depends-on-driver inversions.

**Findings (severity-ranked):**

| # | Area | Severity | Finding |
|---|---|---|---|
| A | Modularity | low-med | **Spine inversion.** `game_state` lazy-imports 9 leaf modules (personal/provincial/territory/thread/world) for `from_dict` deserialization (lines 307-347, function-local). One module cycle `game_state <-> world.npe`, **import-safe** via the lazy imports. Docstring claims "root primitive — Dependencies: none" — **drift**. Mitigated, not a breakage risk. Fix: shared state-types module, or structural typing in the spine. |
| B | Logic boundary | **NULL (clean)** | **No LIVE module imports a STUB** — all cross-layer edges examined; the 32 stubs are leaf-isolated. This is *why* the strategic loop runs without hitting stub code. Examined, nothing found. |
| C | Cohesion | med | `massbattle.py` = **1905 lines** (bare port of a 2143-line monolith). Single god module — maintainability/auditability concern. |
| D | Status hygiene | low | 32/62 stub (44%) + 28 untagged — over half the package is provisional/stub or status-unclear; docstring `Status:` tags inconsistent. |
| E | Architecture | note | Lateral scale<->scale coupling (provincial->personal, thread->peninsular/personal, world->territory, peninsular->world) — some cross-scale logic lives in the scale layers rather than `cross_scale`. Acceptable; track it. |

---

## STAGE 4 — MECHANICAL STRESS (complete 120-campaign instrumented battery; strategic layer)

```
win-share %:        Varfell 55.8 · Crown 36.7 · Church 6.7 · Hafenmark 0.8
WIN PATH:           GD-1 victory.check = 0/120 (0%)   |   territory fallback = 120/120 (100%)
early ends:         0/120 ended before the 50-season cap  (GD-1 is the only early-end path)
winner holds >=11:  78/120 (65%) of (all-fallback) winners dominate territorially
battles/campaign:   mean 34.0  (min 12, max 53, sd 8.8)
surviving factions: mean 1.91  (min 1, max 4)  — heavy consolidation
faction Stability:  min/campaign mean 2.54, floor 0.50; 9% of end-state factions at Sta<=2
seam triggers:      Stability-Crisis fires on the ~9% crisis factions, ALL deferred (derivation gap)
perf:               scene phase adds per-season cost (~2.7s/campaign; battery staged across blocks)
```

**Findings (NERS lens, severity-ranked):**

1. **[R-FAIL] Severe balance skew.** Varfell **55.8%** dominance (snowball suspect); consolidation to ~1.91 survivors. Hafenmark **0.8%** (1/120) — by far the weakest (next-weakest Church ~8x higher); a victory path exists but is marginal-to-negligible (CI wide on a single win). *Correction:* the prior 0/44 "no path" was a small-sample artifact — Hafenmark is severely disadvantaged, not path-less. Whether ~1% is a defect or acceptable under the context-gating principle (not all factions equally likely to take the peninsula) is a Jordan call.
2. **[R/S] Canonical victory categorically inert.** GD-1 sovereignty fires **0/120** across ~6,000 season-checks; **100%** of campaigns are decided by the territory-count fallback at the season cap. Since 65% of winners already hold >=11/15 territories, the territory threshold is *not* the blocker — the binding constraints are the non-territorial GD-1 conditions (Accord>=2 in all held / PS<=6 / sustained 2 consecutive seasons). The designed win condition never drives game termination.
3. **[R / Phase-4 loop] Faction death-spiral is live.** 9% of end-state factions at Sta<=2, floor 0.50 (full collapse) — the faction-collapse spiral the resolution-diagnostic flagged for the faction layer manifests in the integrated sim (undamped toward collapse).
4. **[seam — confirms Stage 2]** Triggers fire on every Stability Crisis (~9%), all deferred to the derivation gap. Wired + gap confirmed at scale; side-effect-free (no-regression holds).

---

## NERS VERDICT (integrated system, as currently composed)

```
SYSTEM: sim/ integrated package — strategic layer driving outcomes;
        personal/thread/world wired-but-inert (derivation + echo gaps).

N  ~partial  Seam wiring is necessary (connects scales). But ~half the package (32 stubs)
             is unexercised apparatus — necessity unverified for those modules.
R  FAIL      Severe strategic balance skew (Varfell snowball; Hafenmark ~1%); canonical GD-1
             victory categorically inert (0/120); faction death-spiral (Sta floor 0.50) live.
S  PARTIAL   Scales compose STRUCTURALLY (seam wired, byte-identical no-regression) but not
             SEMANTICALLY (derivation bridge + outcome->echo mapping unbuilt). Personal scenes
             do not feed strategic state.
E  ~pass     Clean scale layering + autoload spine + cross_scale bridge; smells localized
             (spine inversion A; massbattle god module C).
```

---

## REMEDIATION (worst-first)

1. **[R] Faction balance** — diagnose the faction-action economy: why Varfell snowballs; why Hafenmark sits at ~1%. Run `valoria-resolution-diagnostic` on the faction action layer (Phase-4 loop + small-pool). Confirm with Jordan whether ~1% Hafenmark is an intended ceiling or a defect.
2. **[R] GD-1 victory inert (gap now closed)** — the blocker is the **non-territorial** GD-1 conditions, not territory count (65% already clear 11/15). Examine the Accord/PS dynamics and the 2-consecutive-season sustain: either the sim never drives Accord>=2-across-all-held + PS<=6 simultaneously, or the sustain window is unreachable in 50 seasons. Decide whether GD-1 should be loosened or the sim should drive those tracks.
3. **[R / Lesson-5] Faction death-spiral** — the Stability-collapse loop needs a bound/recovery short of full collapse (resolution-diagnostic Lesson 5: a cap or recovery path, not extinction).
4. **[S] Context-derivation bridge + outcome→echo mapping** — the gating gaps for true multi-scale composition. Design decision (Jordan): how aggregate faction state spawns concrete scene actors, and how scene outcomes translate to faction-stat echoes.
5. **[Modularity] Spine inversion (A) + massbattle cohesion (C)** — refactors; low priority relative to the balance/victory defects.

## FLAGGED GAPS (not fabricated)
- Context-derivation bridge (aggregate → scene actors) — unbuilt; personal scenes cannot auto-resolve.
- Outcome→echo mapping — unbuilt; scenes side-effect-free on strategic state.
- 32 stub modules — unexercised by the strategic loop.
- *(Resolved this revision: GD-1-vs-fallback attribution — now instrumented, 0/120 GD-1.)*

## OPEN DECISIONS (Jordan)
- Is Hafenmark's ~1% win rate an intended ceiling or a defect?
- Context-derivation bridge design.
- Priority: fix strategic balance/victory first, or build the derivation bridge first?

---

Citations:
  - sim/autoload/game_state.py
  - sim/autoload/victory.py
  - sim/cross_scale/scene_dispatch.py
  - sim/mc_v18.py
  - sim/provincial/faction_action.py
  - designs/architecture/scale_transitions_v30.md
