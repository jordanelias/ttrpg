# Cluster C-EMERGE dossier

_Sonnet evidence cluster; read-only on the repo (all instrumentation was in-process monkeypatching;
run outputs archived to the session scratchpad, paths at the end). Archived verbatim by the Fable
orchestrator (2026-07-07)._

## Invocation + wall-time notes

Entry point: `sim/mc_v18.py` — `run_campaign(seed, max_seasons=50, params=None) -> CampaignResult` and `run_batch(n, base_seed=0, params=None) -> BatchResult`. A campaign advances `world.season` via `sim.peninsular.season.run_season` (advance_season → `_faction_actions_callback` → `run_accounting`) until a `victory.check_all_factions` winner appears or `CAMPAIGN_SEASONS` (default 50) is exhausted, then falls back to a territory/L score winner. `sim/tests/test_mc_v18_regression.py` pins `run_batch(n=2, base_seed=0)` as the CI golden (~5s, per its docstring).

Measured wall-times: single `run_campaign(seed=0)` = 1.81s. Batch means: n=16 @ 50 seasons ≈ 2.37s/campaign (37.84s total); n=8 @ 20 seasons ≈ 1.13s/campaign; n=10 @ 50 seasons, base_seed=42 ≈ 1.96s/campaign. Total probe wall-time ~90s.

## Batch results

**Batch A — n=16, base_seed=0, 50 seasons:** Crown 43.8% (7) · Varfell 43.8% (7) · Church 12.5% (2) · Hafenmark 0.0% (0).

**Batch B — n=10, base_seed=42, 50 seasons** (mc_v18's own `__main__` uses base_seed=42): **Varfell 90.0% (9) · Crown 10.0% (1) · Church 0.0% · Hafenmark 0.0%.**

Batch B **reproduces the CLAUDE.md §7 "~87% one faction, two at 0%" calibration almost exactly** (90/10/0/0). Batch A does NOT — a much more even 44/44/12/0 split. **The "~87%" figure is a base_seed=42-batch artifact, not a fixed property of the sim**; what's stable across both base_seeds is *qualitative*: Hafenmark locked at exactly 0% in every batch (17/17 distinct seeds), and a second faction frequently locked at/near 0%.

**Golden comparison:** the existing regression golden (n=2, base_seed=0: Crown 50/Church 50/Hafenmark 0/Varfell 0) is consistent with Batch A's per-seed log (seed 0=Crown, seed 1=Church).

## Ablation results (ablation-readiness finding)

Grepped all of `sim/` for `os.environ`/`os.getenv`/`FLAG` toggles — **zero exist**. The only externally-reachable knob is the `params` dict into `DEFAULT_PARAMS = {'CAMPAIGN_SEASONS': 50, 'VICTORY_THRESHOLD': 11}`.

1. **CAMPAIGN_SEASONS 50→20** (n=8, seed 0): win-share collapsed further — Crown 50/Varfell 50/Church 0/Hafenmark 0. Shortening the horizon amplifies degeneracy (less time for claw-back before the cap).
2. **VICTORY_THRESHOLD is a dead param — confirmed by ablation.** `params={'VICTORY_THRESHOLD': 5}` vs default → **byte-identical** output. `victory.py` hardcodes module-level `VICTORY_THRESHOLD = 15`, never reads params.
3. **No third meaningful flag exists.** `Faction.parliamentary` defaults True and is never reassigned anywhere in sim/.

**Finding: ablation-readiness is essentially absent** — no way to test counterfactuals (disable Church Excommunication; grant Hafenmark unique actions) without editing code.

## Emergence analysis (null-hypothesis verdicts)

Instrumented via in-process monkeypatch across 34 campaign-runs:

- **Scene phase: fires but never resolves.** Batch A (800 season-checks): "Stability Crisis" queued 128 contest scenes; **all 128 (100%) deferred** ("context-derivation gap"), 0 resolved, 0 domain echoes. Verdict: **artifact/scripting, not emergence** — architecturally incapable of feeding strategic state.
- **The other 7 §4.3.2 mandatory triggers never even attempt to fire** — deferred in 800/800 season-checks ("not evaluable against the current aggregate world schema").
- **Insurgency pipeline (GD-3): dead-by-construction.** Requires ≥2 contiguous territories with `owner is None`; no code path ever sets owner to None (conquest transfers between factions and excludes None-owned targets; T15 is excluded from ALL_PLAYABLE_15 and is a singleton). `insurgencies_count == 0` in all 34 campaigns.
- **NPE: wired every season, producer never called.** `simulate_npc_actions` iterates `world.npcs`, but `generate_npc()` — the only populator — has **zero call sites** in sim/. `world.npcs == {}` for every campaign's entire life.
- **Nine further World registries never touched by the campaign loop:** practitioners, treaties, knots, convictions, beliefs, threadcut_beings, territory_infrastructure, npc_drift_state, settlements — their owning modules are never imported by mc_v18/season/accounting/faction_action. Confirmed empty in every serialize_world() output.
- **Zero exceptions** swallowed by `_faction_actions_callback`'s blanket `except Exception: pass` across all 34 campaigns.

**Overall verdict (null-hypothesis-first):** the campaign loop as executed is **faction-territory-accounting plus a Conquest/Muster/Govern/faction-unique roll, full stop.** No cross-subsystem chain fires even once in 34 seeded campaigns. No candidate survives to be called an emergence claim.

**Load-bearing mechanistic finding:** the degenerate win-share is a **hard trap state**, not variance: `if not faction.territories: continue` (a 0-territory faction never acts again; no comeback mechanic) + Hafenmark's starting `Mil=3.0` sitting exactly at the Conquest-eligibility floor (`Mil < 3.0 → invalid`) ⇒ near-certain permanent elimination for Hafenmark (15/16 Batch-A seeds, as early as season 9); no faction ever recorded at 0 territories subsequently won (34/34).

## F7 smoke-oracle spec proposal (candidate text — NOT filed; read-only)

1. **Second pinned golden at the degenerate extreme:** pin `run_batch(n=10, base_seed=42)` exactly — `win_share = {'Crown': 10.0, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 90.0}`, `all_winners = {'Varfell': 9, 'Crown': 1}`, `battles_mean = 33.0` (~20s, CI-affordable). Comment ties it to CLAUDE.md's "~87%" so the prose claim has an executable anchor.
2. **Named zero-assertions for silent-subsystem regression:** expose `scenes_resolved`, `insurgencies_formed`, `npcs_generated` on CampaignResult (or a telemetry sidecar) and assert on both goldens: `insurgencies_formed == 0` ("dead-by-construction; nonzero ⇒ ownership-to-None became reachable — investigate, don't just regenerate"), `npcs_generated == 0` ("generate_npc() has no call site; nonzero ⇒ NPE landed — a feature, bump deliberately"), `scenes_resolved == 0` ("context-derivation bridge gap; nonzero ⇒ the bridge shipped").
3. **Explicit Hafenmark lockout assertion** with the C-EMERGE-1 mechanism in the message.
4. **Dead-param regression test:** assert `VICTORY_THRESHOLD` override is currently a no-op; if it starts failing, someone wired it — assert the new semantics, don't delete.
5. **Wall-time ceiling** (<30s for the module) so the oracle can't silently outgrow CI.

## Findings

- **C-EMERGE-1 · P1 · NEW** — Hafenmark's 0% is a concrete no-comeback elimination-lockout trap (`if not faction.territories: continue`) + starting `Mil=3.0` at the Conquest floor. Evidence: `elimination_timing.json` (15/16 seeds eliminated, earliest season 9); 34/34 campaigns: no 0-territory faction ever won.
- **C-EMERGE-2 · P1 · NEW** — the "~87%" calibration figure is a base_seed=42 artifact; base_seed=0/n=16 gives 44/44/12/0. Stable across seeds: qualitative lockout, not the percentage.
- **C-EMERGE-3 · P2 · NEW** — `_try_faction_unique` blocks Varfell/Hafenmark ('invalid'; "BLOCKED on Pass 2d/2e"); contributing but NOT sufficient for degeneracy — Varfell, also blocked, wins 43.8–90%. Action tallies: 0 unique actions for Varfell/Hafenmark vs 95 (Crown)/83 (Church).
- **C-EMERGE-4 · P1 · KNOWN-TRACKED, now quantified** — scene phase 100% deferral (128/128 queued contests); other 7 triggers 800/800 never-queued.
- **C-EMERGE-5 · P1 · NEW** — insurgency pipeline dead-by-construction (ownership-to-None unreachable).
- **C-EMERGE-6 · P1 · NEW** — NPE producer `generate_npc()` has zero call sites; permanent 0-iteration loop.
- **C-EMERGE-7 · P1 · NEW** — nine World registries unreachable from the campaign loop (import-graph verified).
- **C-EMERGE-8 · P2 · NEW** — `DEFAULT_PARAMS['VICTORY_THRESHOLD']` is dead; victory.py hardcodes 15; ablation-verified byte-identical.
- **C-EMERGE-9 · P2 · NEW** — zero env/config ablation toggles in sim/; only CAMPAIGN_SEASONS is wired.
- **C-EMERGE-10 · P3 · NEW** — `Faction.parliamentary` never reassigned; its gates permanently inert.
- **C-EMERGE-11 · P3 · NEW** — the `except Exception: pass` safety net never fired in 34 campaigns; behavior under real fault unverified.

## Honest gaps (+ archived outputs)

- Did not run the full n=100/base_seed=42 batch (~190s); n=10 already reproduces the pattern; exact tail unconfirmed.
- The nine unreached registries were verified unreachable-from-loop via import-graph grep, not by exercising each module (their internal correctness is C-TW/C-FA/C-NPC/C-SIG scope).
- Non-mc_v18 entry points (Godot skeleton etc.) not checked for generate_npc/thread callers.
- `resolve_mass_battle` not independently stress-tested for its own degeneracy contribution.
- The exception swallow-net was not adversarially fuzzed.
- All instrumentation was in-process monkeypatching; zero repo files created/edited/deleted (verify via git status).

Archived outputs (session scratchpad `…/scratchpad/emergence/`): `run_batch_instrumented.py`, `batch_seed0_n16_seasons50.json`, `batch_seed0_n8_seasons20.json`, `batch_seed42_n10_seasons50.json`, `elimination_probe.py`, `elimination_timing.json`. Reproduction commands recorded in the batch runner's header and the orchestrator's session log.
