# Gap-closure G1 — sim probes (ablation, n=100, stress, exception net)

_Archived verbatim from the agent's final message (2026-07-07)._

# Gap-Closure Report — G1 (C-FA / C-EMERGE / C-RESPESS probes)

All probes ran via in-process monkeypatching only (restored before script exit). `git status --short` before/after these runs shows no files touched by this session (pre-existing untracked files belong to concurrent lanes, not this probe work). Scripts archived at `/tmp/claude-0/-home-user-ttrpg/1330f8bf-0d8a-5dc5-ac82-f87e25936d9b/scratchpad/gapclosure/`.

## 1. C-FA ablation gap — does removing Crown/Church's unique engines change who wins?

Patched `sim.provincial.faction_action._try_faction_unique` to return `'invalid'` unconditionally (same behavior Varfell/Hafenmark already get), ran both baseline batches ablated:

| Batch | Baseline (KNOWN) | Ablated (this probe) |
|---|---|---|
| n=16, base_seed=0 | Crown 43.8 / Varfell 43.8 / Church 12.5 / Hafenmark 0.0 | Crown 37.5 / **Varfell 56.2** / Church 6.2 / Hafenmark 0.0 |
| n=10, base_seed=42 | **Varfell 90.0** / Crown 10.0 / Church 0.0 / Hafenmark 0.0 | **Crown 60.0** / Church 20.0 / Varfell 20.0 / Hafenmark 0.0 |

Hafenmark stays locked at exactly 0% in **both** ablated batches. In the n=10/seed=42 batch, ablation *increased* Crown's share (10%→60%) and *crashed* Varfell's (90%→20%) — the opposite of "remove the wired factions' advantage and the blocked factions rise."

Root cause (verified by re-reading `faction_take_action`, `sim/provincial/faction_action.py:52-77`): the action selector uses one cumulative roll. When `_try_faction_unique` returns `'invalid'`, the same `roll<0.30` draw falls through into the `roll<0.65` Conquest check. Ablating Crown/Church doesn't cleanly subtract their L-pump benefit — it also converts their 30% unique-slot into *extra Conquest-attempt frequency* (stacking on their native 35%), exactly the undamped Mil→Conquest snowball mechanism C-FA-5 already flagged. This is a genuine confound in the ablation, not a clean counterfactual.

**Verdict on gap 1:** Ablating the wiring asymmetry does **not** rescue Hafenmark and does **not** reliably favor the previously-blocked factions — in one batch it made the concentration *worse*. This closes the C-FA-4 vs C-EMERGE-1/2 tension against "near-dispositive": C-FA-4 is a real, evidenced mechanism, but this probe shows it is entangled with a code-structural confound (unique-slot fallthrough → more conquest) and is **not sufficient** to explain the degenerate win-share pattern on its own. C-EMERGE-1's Hafenmark-specific elimination-lockout trap (0-territory dead-end + Mil=3.0 floor) is unaffected by removing Crown/Church's engines, so it stands as the stronger, independent explanation for Hafenmark's 0%, while overall degeneracy is best read as a compound of both mechanisms plus M2's undamped snowball — not attributable to wiring asymmetry alone.

## 2. C-EMERGE n=100 gap

`run_batch(n=100, base_seed=42)`, 219.6s wall time:

```
win_share:  Crown 36.0 / Church 7.0 / Hafenmark 1.0 / Varfell 56.0
all_winners: Varfell 56 / Crown 36 / Hafenmark 1 / Church 7
battles_mean: 34.3
```

**Verdict on gap 2:** The n=10 sample's 90/10/0/0 extreme does **not** hold at n=100 — the tail settles to a still-skewed but less extreme 56/36/7/1. Critically, **Hafenmark wins once** (1/100), which contradicts a literal "hard trap = impossible to win" reading of C-EMERGE-1; it is instead a very strong (~99%) but not absolute structural disadvantage. This further corroborates C-EMERGE-2: the "~87%" figure is a small-n/seed artifact, not a stable property of the sim, though the qualitative pattern (no faction near a fair 25%, one dominant, one near-zero) is stable across n=10/16/100.

## 3. C-EMERGE mass-battle stress gap — Mil-differential monotonicity

Built minimal faction stubs (`.name`, `.Mil`) and a world stub (`.rng`), called `resolve_mass_battle` directly, 200 seeded battles per Mil pair:

| Pair (A vs B=3) | Attacker win rate | Mean attacker size-pct remaining |
|---|---|---|
| 3 v 3 | 50.5% | 0.672 |
| 4 v 3 | 74.0% | 0.676 |
| 5 v 3 | 90.0% | 0.714 |
| 6 v 3 | 95.5% | 0.737 |
| 7 v 3 | 96.5% | 0.763 |

Marginal deltas: +23.5, +16.0, +5.5, +1.0 — decreasing at every step.

**Verdict on gap 3:** Win rate rises **monotonically** with Mil differential but with strongly **diminishing** returns (concave, saturating toward a ceiling near 100%), not superlinear/compounding. This means the *battle-resolution function itself* is not the source of runaway advantage — it self-limits. The undamped compounding C-FA-5 flags happens one level up, in the strategic loop's uncapped Mil accrual (`_try_muster` +3/+5 per season, no ceiling feeding back into this saturating function), not inside `resolve_mass_battle`. This narrows C-FA-5's mechanism: the snowball is in season-over-season Mil accumulation, not in battle-outcome sensitivity to Mil.

## 4. C-EMERGE exception-net gap

Patched `sim.mc_v18.faction_take_action` so Crown's call always raises `RuntimeError`; ran 2 full campaigns (seed=0, seed=1) with stdout/stderr captured.

- Crown's action was invoked 60 times total across both campaigns; **all 60 raised, all 60 were silently swallowed**.
- Both campaigns completed normally: 50 seasons each, winner declared (Varfell both times), `battle_count` 31/25.
- Captured stdout: 0 bytes. Captured stderr: 0 bytes.
- `serialize_world()`'s output has no error/exception/fault field at all (`season, arc, winner, battle_count, clocks, factions, territories, practitioners, insurgencies, uncontrolled_streaks, npcs, ...` — nothing fault-related).

**Verdict on gap 4:** Confirmed and quantified. A real fault — even a 100%-failure-rate one, every season, for an entire faction, for an entire campaign — produces **zero observable signal** to an operator: no print, no log, no counter on `CampaignResult`/`BatchResult`, no field in the serialized world state. It is indistinguishable from "Crown had no valid action this season" (which already happens routinely via the `'invalid'` returns). The only way to detect it is external code instrumentation, which an operator running `run_batch` in production would not have.

## 5. C-RESPESS exposure gap — Stability-Crisis queue rate

Instrumented `scene_dispatch.run_scene_phase`/`queue_triggered_scenes`/`dispatch_scenes` across 20 campaigns × 50 seasons (1000 season-checks):

```
total scenes queued: 151        (12.9% of season-checks queue ≥1 scene; 7.55 scenes/campaign mean)
total dispatched: 151, total resolved: 0   (0.0% resolution rate)
deferred_reasons: {"contest:context-derivation gap: no personal contest parties from aggregate faction state": 151}
```

**Verdict on gap 5:** Exposure of the live-dispatch path is real in frequency (~7.6 Stability-Crisis contest scenes queued per 50-season campaign, ~13% of season-checks) but **zero in actual execution** — every single queued scene is deferred before it ever reaches `contest.run_contest` (the deprecated raw-dice stub C-RESPESS-2 flags as the wrong engine). So the wrong-engine defect is currently **dormant/unreachable** given the context-derivation bridge gap; the ~7.6/campaign, ~13%/season-check figure is the exposure rate that would go *live* the moment that bridge is closed, at which point the dice-pool-stub-vs-σ-kernel mismatch becomes an actively-executing defect rather than a latent one.

## 6. C-EMERGE non-mc_v18 entry point gap

Repo-wide search (`.py`, `.md`, `.gd`) for call sites of `generate_npc(`, `propose_treaty(`, and functional use of `sim.thread.*`:

- `generate_npc(`: only its own definition (`sim/world/npe.py:198`) and mentions inside this audit's own dossiers (`cluster_C-EMERGE.md`, `cluster_C-REACH.md`). **Zero callers anywhere**, including `tests/`, `sim/tests/`, `designs/audit/*.py` workbenches, and the Godot skeleton (`designs/godot/`).
- `propose_treaty(`: only its own definition (`sim/provincial/treaty.py:97`, which itself unconditionally `raise`s — it's a stub). Two `.md` files (`tests/coverage_matrix_archive.md`, `tests/sim/v18-integration/module_manifest.md`) mention it in prose/manifests, not code. **Zero callers.**
- `sim.thread.*`: the only non-definition references are internal, deferred imports inside `sim/personal/knots.py` (`apply_coherence_delta`, itself never reached — knots aren't touched by the campaign loop per C-EMERGE-7) and dataclass/type comments in `sim/autoload/game_state.py`. No pytest test in `sim/tests/` or `tests/` exercises `sim/thread/*` directly; `tests/index/test_stubs_table.py` only inserts a status string into a tracking sqlite table, it doesn't call the module.
- Old historical `mc_v5`..`mc_v14` copies and `mass_battle_stress_random.py` under `designs/audit/` are unrelated (pre-v18 balance-audit snapshots / a different battle-engine formation-fuzz harness) — none call any of the three targets.

**Verdict on gap 6:** Confirmed — there is **no other executable entry point anywhere in the repo** (workbench, script, pytest test, Godot skeleton, or historical mc_v* copy) that calls `generate_npc`, `treaty.propose_treaty`, or any `sim.thread.*` function. `mc_v18`'s campaign loop is not just the primary exerciser of these — it is the **sole universe of execution** in the repo, and even it never reaches them (C-EMERGE-6/7). These three are dead code by every currently-executable path, not merely under-exercised by the campaign loop specifically.

---

### Scratch artifacts
`/tmp/claude-0/-home-user-ttrpg/1330f8bf-0d8a-5dc5-ac82-f87e25936d9b/scratchpad/gapclosure/`: `gap1_fa_ablation.py`, `gap2_n100.py` (+ `.out`), `gap3_mb_stress.py`, `gap4_exception_net.py`, `gap5_respess_exposure.py`. No repo files were created, edited, or deleted.
