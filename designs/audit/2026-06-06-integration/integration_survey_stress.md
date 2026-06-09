# Integration Survey + Mechanical Stress — `sim/` Package (Stages 2–4)

**Status:** Audit / survey + stress record. Class-C findings, Jordan-vetoable.
**Date:** 2026-06-06. **Scope:** the unified `sim/` package (62 modules).
**Pipeline:** wire (Stage 2 — committed `db639e51`) → survey (Stage 3) → stress + log (Stage 4).
**Method:** AST dependency + status scan of all 62 `sim/` modules; in-container execution of `mc_v18` — no-regression baselines (seeds 42, 7) + a 44-campaign time-bounded stress battery.

`[READ:]` sim/autoload/{game_state,scene_slate,season_manager,victory,dice_engine,registry}.py · sim/peninsular/season.py · sim/cross_scale/{zoom_in_out,handoff_rules,scene_dispatch}.py · sim/personal/{combat,contest}.py · sim/mc_v18.py · sim/provincial/faction_action.py · full-tree AST scan.

---

## SCOPE CAVEAT (load-bearing — read first)

The personal / thread / world layers are **structurally wired** to the strategic loop (Stage-2 seam) but **semantically inert**: the context-derivation bridge (aggregate faction state → concrete scene actors) and the outcome→echo mapping are unbuilt (flagged gaps), so personal-scene outcomes do not yet feed strategic state. This stress therefore exercises **the strategic layer + the wired-but-inert seam**, NOT a fully-composed multi-scale system. Findings are scoped accordingly. "Wire every mechanic system" is, after this pass: spine + seam wired and running; semantic multi-scale composition gated on the derivation bridge.

---

## STAGE 2 — WIRE (recap; committed `db639e51`)

`sim/cross_scale/scene_dispatch.py` (new) + `mc_v18` caller-side hook connect the seam: trigger-eval → `scene_slate` → `zoom_in` → live resolver → `zoom_out`. Verified: triggers fire on real world-state; injected actors resolve end-to-end via `run_contest`; `run_batch(10)` byte-identical to baseline (side-effect-free). 7 of 8 §4.3.2 triggers deferred (world-state schema absent) — flagged, not faked.

---

## STAGE 3 — SURVEY: modularity / architecture / logic

**Inventory.** 62 modules — 12 `[CANONICAL]` (live), 28 substantial-but-untagged, 32 stub. Scales: `autoload` (spine), `personal`, `provincial`, `territory`, `peninsular`, `thread`, `world`, `cross_scale` (bridge), `mc_v18` (driver).

**Layering — sound overall.** Cross-layer import direction is correct: scale layers → `autoload` spine (provincial→autoload ×12, personal→autoload ×7, …); `cross_scale` → personal/autoload (bridge depends on what it connects); `mc_v18` → autoload/provincial/peninsular/cross_scale (driver orchestrates). No leaf-depends-on-driver inversions.

**Findings (severity-ranked):**

| # | Area | Severity | Finding |
|---|---|---|---|
| A | Modularity | low–med | **Spine inversion.** `game_state` lazy-imports 9 leaf modules (personal/provincial/territory/thread/world) for `from_dict` deserialization (lines 307–347, function-local). One module cycle `game_state ↔ world.npe`, **import-safe** via the lazy imports. Docstring claims "root primitive — Dependencies: none" — **drift**. Mitigated, not a breakage risk. Fix: shared state-types module, or structural typing in the spine. |
| B | Logic boundary | **NULL (clean)** | **No LIVE module imports a STUB** — all cross-layer edges examined; the 32 stubs are leaf-isolated. This is *why* the strategic loop runs without touching stub code. Examined, nothing found. |
| C | Cohesion | med | `massbattle.py` = **1905 lines** (bare port of a 2143-line monolith). Single god module — maintainability/auditability concern. |
| D | Status hygiene | low | 32/62 stub (44%) + 28 untagged — over half the package is provisional/stub or status-unclear; docstring `Status:` tags inconsistent. |
| E | Architecture | note | Lateral scale↔scale coupling (provincial→personal, thread→peninsular/personal, world→territory, peninsular→world) — some cross-scale logic lives in the scale layers rather than `cross_scale`. Acceptable; track it. |

---

## STAGE 4 — MECHANICAL STRESS (44-campaign battery, time-bounded; strategic layer)

```
win-share %:        Varfell 56.8 · Crown 34.1 · Church 9.1 · Hafenmark 0.0
GD-1 early end:     0/44 — NO campaign ended before the 50-season cap
winner at cap:      75% hold >=11/15 territories  (GD-1-at-season-50 vs territory fallback: not distinguished [GAP])
battles/campaign:   mean 34.4  (min 21, max 53, sd 8.5)
surviving factions: mean 1.84  (min 1, max 4)  — heavy consolidation
faction Stability:  min/campaign mean 2.45, floor 0.50; 11% of end-state factions at Sta<=2
seam triggers:      Stability-Crisis fires ~11%, ALL deferred (context-derivation gap)
perf:               scene phase adds per-season cost (44 campaigns / 121s)
```

**Findings (NERS lens, severity-ranked):**

1. **[R-FAIL] Degenerate balance.** Hafenmark **0%** wins (all 44 + seeds 42/7) — a faction with no observed victory path; Varfell **57%** dominance (snowball suspect); consolidation to ~1.84 survivors. Echoes the historical v17 "Church 0% / Varfell 0%" structural-incompleteness pattern, now landing on Hafenmark.
2. **[R/S] Canonical victory inert as a terminator.** 0/44 campaigns ended before the cap ⇒ GD-1 sovereignty was not achieved-and-sustained during seasons 1–49 of any campaign; the winner is decided at the season cap. Whether GD-1 fires on the final season vs the territory-count fallback is not instrumented `[GAP]`. Either way, the designed win condition does not drive game termination.
3. **[R / Phase-4 loop] Faction death-spiral is live.** 11% of end-state factions at Sta≤2, floor 0.50 (full collapse) — the faction-collapse spiral the resolution-diagnostic flagged for the faction layer manifests in the integrated sim (undamped/unbounded toward collapse).
4. **[seam — confirms Stage 2]** Triggers fire on every Stability Crisis (~11%), all deferred to the derivation gap. Wired + gap confirmed at scale; side-effect-free (no-regression holds).

---

## NERS VERDICT (integrated system, as currently composed)

```
SYSTEM: sim/ integrated package — strategic layer driving outcomes;
        personal/thread/world wired-but-inert (derivation + echo gaps).

N  ~partial  Seam wiring is necessary (connects scales). But ~half the package (32 stubs)
             is unexercised apparatus — necessity unverified for those modules.
R  FAIL      Degenerate strategic balance (Hafenmark 0%, Varfell snowball); canonical GD-1
             victory inert as terminator; faction death-spiral (Sta floor 0.50) live.
S  PARTIAL   Scales compose STRUCTURALLY (seam wired, byte-identical no-regression) but not
             SEMANTICALLY (derivation bridge + outcome->echo mapping unbuilt). Personal scenes
             do not feed strategic state.
E  ~pass     Clean scale layering + autoload spine + cross_scale bridge; smells localized
             (spine inversion A; massbattle god module C).
```

---

## REMEDIATION (worst-first)

1. **[R] Faction balance** — diagnose the faction-action economy: why Hafenmark has no victory path; why Varfell snowballs. Run `valoria-resolution-diagnostic` on the faction action layer (Phase-4 loop + small-pool). First confirm with Jordan whether Hafenmark is an intended non-victory faction (0% may be defect or design).
2. **[R] GD-1 victory** — instrument `run_campaign` to attribute wins (GD-1-at-cap vs fallback); determine whether GD-1 conditions are too strict, the sim fails to drive Accord/PS into range, or 50 seasons is too short.
3. **[R / Lesson-5] Faction death-spiral** — the Stability-collapse loop needs a bound/recovery short of full collapse (resolution-diagnostic Lesson 5: a cap or recovery path, not extinction).
4. **[S] Context-derivation bridge + outcome→echo mapping** — the gating gaps for true multi-scale composition. Design decision (Jordan): how does aggregate faction state spawn concrete scene actors, and how do scene outcomes translate to faction-stat echoes?
5. **[Modularity] Spine inversion (A) + massbattle cohesion (C)** — refactors; low priority relative to the balance/victory defects.

## FLAGGED GAPS (not fabricated)
- Context-derivation bridge (aggregate → scene actors) — unbuilt; personal scenes cannot auto-resolve.
- Outcome→echo mapping — unbuilt; scenes side-effect-free on strategic state.
- GD-1-vs-fallback win attribution — not instrumented.
- 32 stub modules — unexercised by the strategic loop.

## OPEN DECISIONS (Jordan)
- Is Hafenmark a victory-seeking faction? (0% may be defect or intent.)
- Context-derivation bridge design.
- Priority: fix strategic balance/victory first, or build the derivation bridge first?

---

Citations:
  - sim/autoload/game_state.py
  - sim/peninsular/season.py
  - sim/cross_scale/zoom_in_out.py
  - sim/cross_scale/scene_dispatch.py
  - sim/mc_v18.py
  - sim/provincial/faction_action.py
  - designs/architecture/scale_transitions_v30.md
