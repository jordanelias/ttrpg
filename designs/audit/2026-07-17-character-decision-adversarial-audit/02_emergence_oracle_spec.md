<!-- STATUS: PROPOSED — spec for the minimal n≥100 campaign emergence/balance oracle. -->
<!-- AUTHORITY: ED-IN-0073 umbrella; per-lane candidate C-6 (FA +IN). File on ruling. -->

# Emergence Oracle Spec — the minimal n≥100 campaign characterization

## Status: PROPOSED
## Date: 2026-07-17
## Parent: `00_findings.md` (closes the constructive half of L6, N1–N4, N9)

### Why this exists

The repo asserts emergent, non-degenerate narrative but has **never characterized `mc_v18` at a scale
that could show a degenerate attractor**. The only oracles on file are `test_f7_smoke_oracle.py` (n=8,
self-labeled "NOT balance signal, do not tune to it") and `test_mc_v18_regression.py` (n=2, golden
`{Crown 50, Church 0, Hafenmark 0, Varfell 50}`). The audit found the "87%/0%/0%" citation stale (N4),
GD-2's mandatory pass unbuilt (N1), GD-3 insurgencies firing zero times (N3), and a cascade loop with
no stability argument (L6). This spec is the single instrument that turns all of those from *asserted*
into *measured*. It formalizes the "no balance claim without an oracle + n ≥ 100" bar the audit ecosystem
already set for itself.

---

## §1 What it produces

A deterministic harness that runs `mc_v18` across a fixed seed set (N ≥ 100), extracts a fixed metric
vector per campaign, and reduces to a **distribution summary** (not per-seed rows) that is (a) asserted
against health bands and (b) stored as a drift-checked golden.

Output artifact: `tests/sim/emergence_oracle/summary.json` — per-metric mean, stdev, min, max, and the
band verdicts; plus `content_hash` of the concatenated per-seed key-log hashes for determinism.

---

## §2 Metrics (per campaign, then aggregated)

| Metric | Definition | Guards against |
|---|---|---|
| `win_share[faction]` | fraction of N campaigns each faction wins | degenerate dominance / 0-win lockout (N4, N5) |
| `winner_entropy` | Shannon entropy of the winner distribution (bits) | single-attractor collapse |
| `distinct_winners` | count of factions winning ≥ 1 campaign | monoculture |
| `insurgencies_formed` | mean per campaign | GD-3 dead pipeline (N3) |
| `npcs_generated` | mean emergent NPCs per campaign | GD-3 dead pipeline (N3) |
| `arc_transitions` | mean named-NPC arc branch fires per campaign | arc state machine inert (N2) |
| `mandatory_fires` | mean GD-2 mandatory-pass activations per campaign | GD-2 unbuilt (N1) |
| `campaign_len` | seasons to terminal state; and % hitting the season cap | runaway / premature-lock (L6) |
| `territory_gini` | mean end-state territory-concentration Gini | slow monoculture drift |
| `determinism_ok` | same seed → identical key-log hash across two runs | non-reproducibility (N7) |

---

## §3 Health bands (all `[SEED]` — set provisionally, calibrate on the Phase-1 baseline)

A run **PASSES** iff all hold over the N-seed aggregate:

- **Non-degeneracy:** `max(win_share) ≤ 0.60` **and** `min(win_share over live factions) ≥ 0.05`.
  (Directly catches the 87%/0% class and the Hafenmark absorbing-state, N4/N5.)
- **Variety:** `distinct_winners ≥ 3` **and** `winner_entropy ≥ 1.0 bit`.
- **Liveness (report-only until the mechanisms are built):** `insurgencies_formed > 0` in ≥ 10% of
  campaigns; `arc_transitions > 0` mean; `mandatory_fires > 0` mean. **These are expected to FAIL on the
  current tree (N1–N3) — that failure is the point:** the oracle makes the unbuilt mechanisms visible as
  a red metric instead of a prose caveat nobody runs.
- **Termination:** 100% of campaigns reach a terminal state within the season cap; `campaign_len` stdev
  finite (no runaway).
- **Determinism:** `determinism_ok == true`.

Bands are stored in `bands.yaml` beside the harness so a ruling can move them without touching code.

---

## §4 Mutation checks (cheap causal-inertness guards)

Run a small perturbation battery (n≥30 each is enough for a signal) asserting that documented knobs
actually move outcomes — the class of defect `test_f7_victory_threshold_is_a_dead_param` already found
(`VICTORY_THRESHOLD` inert):

- Perturb `VICTORY_THRESHOLD`, expect a measurable shift in `campaign_len` or `win_share` (currently
  expected to FAIL — documents the dead param).
- Zero the state-conditioning multipliers in `faction_action.py`, expect `win_share` to move toward the
  neutral 30/35/20/15 prior (confirms the ED-FA-0012 conditioning is live, not cosmetic).
- Swap two factions' starting positions, expect the win-share asymmetry to swap with them (confirms no
  hard-coded faction identity advantage beyond position).

Any knob that moves nothing is filed as an inert-parameter finding.

---

## §5 Harness shape (deterministic, parallel, no network)

```
tests/sim/emergence_oracle/
  run_oracle.py        # seed loop -> per-campaign metric extraction -> summary.json
  metrics.py           # the §2 extractors, reading mc_v18's own end-state + key log
  bands.yaml           # §3 thresholds (rulable without code change)
  summary.json         # generated artifact (golden)
```

- **Seeds:** a fixed list `SEEDS = range(1000, 1000+N)` (pass timestamps/entropy in as data — scripts
  may not call `Date.now()`/`random` per repo rules; the RNG service is seeded per `(campaign, seed)`).
- **Determinism:** reuse `KeyLog.content_hash()` (`keys.py:400`) per campaign; `determinism_ok` re-runs a
  small subset and compares hashes.
- **Cost:** `N × (single mc_v18 campaign runtime)`. Parallelizable across seeds (embarrassingly parallel;
  no shared state). Budget note: keep N=100 for CI cadence; a deeper N=1000 sweep is a manual/weekly
  target, not per-commit.
- **No new balance numbers are authored** — the harness *reads* `mc_v18`'s existing resolution. It adds
  measurement, not mechanics (respects GD-2's "oracle, not new canon" discipline).

---

## §6 CI integration (phased, report-only first)

| Phase | Deliverable | Gate |
|---|---|---|
| 0 | `run_oracle.py` + `metrics.py`; runs N=100 locally | none |
| 1 | Characterize the **current** tree; commit the baseline `summary.json` | expected RED on liveness + non-degeneracy — **documented, not hidden** |
| 2 | Set provisional `bands.yaml` from the baseline + design intent | none |
| 3 | Weekly CI job (`.github/workflows/`) runs N=100, posts the summary, **report-only** | non-blocking |
| 4 | Flip non-degeneracy + termination + determinism bands to **blocking** once green; keep liveness report-only until N1–N3 are built | blocking on the stable subset |

Per-commit CI stays untouched (a 100-campaign sweep is too heavy); this rides the existing weekly
`audit-refresh` cadence.

---

## §7 What it would have caught (validation of the instrument)

- **N4 degenerate win-share** — a real `max(win_share) > 0.60` breach instead of a stale prose citation.
- **N5 Hafenmark lockout** — `min(win_share) = 0` band failure, mapped to `ED-FA-0005`.
- **N3 GD-3 dead pipeline** — `insurgencies_formed == 0` as a standing red metric.
- **N1 GD-2 unbuilt** — `mandatory_fires == 0`.
- **N2 arc machine inert** — `arc_transitions == 0`.
- **`VICTORY_THRESHOLD` inert** — §4 mutation check.
- **L6 cascade instability** — `campaign_len` / `territory_gini` distribution shape over N; oscillation
  shows as high variance or cap-hitting.

The instrument's own success criterion is honest: **on today's tree it should report multiple RED
metrics.** That is the difference between "emergence is our aspiration" and "here is exactly which
mechanisms do not yet fire, measured, on every run."

---

## §8 Relationship to existing work

- Supersedes the n=8 `test_f7_smoke_oracle.py` as the balance oracle (keep F7 as a fast per-commit smoke;
  this is the weekly characterization). Ties to `ED-IN-0021` (F7 smoke oracle) and `ED-FA-0005`
  (elimination lockout).
- Does **not** touch `faction_action.py` mechanics — it is measurement only. When N1/N2/N3 are later
  built (GD-2 pass, arc state machine, GD-3 reachability), their liveness metrics flip from RED to
  green with no oracle change, which is the point of specifying the metric now.
