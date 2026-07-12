# PR#119/#125 provisional-mechanic verification via `tools/sim_harness/`

**Status: PROPOSED, read-only.** Mirrors PR#125's own framing ("NOT canon") — this doc
verifies claims already on the table (PR #119's 12 authored items, PR #125's stress-test +
reconciliation findings), it ratifies nothing. No `## Status:` line in any PR#119 doc changes
as a result of this pass.

## What this is

Seven [`tools/sim_harness/`](../../../tools/sim_harness/) **provisional adapters**
(`canon_row=None` — the harness's own first-class path for testing proposed-but-not-yet-
ratified mechanics; see `tools/sim_harness/README.md` "Provisional adapters") that mechanically
re-test the PR #119 settlement/faction governance proposals and the two PR #125 cross-cutting
findings (the Π pressure homeostat, the two-event-architecture fork), grounded in the real
**Goldenfurt vertical slice** (`designs/territory/goldenfurt_slice/` — S-006, 6 NPC dossiers +
3 minor actors) rather than invented settlements, per the explicit recommendation of
`designs/audit/2026-07-12-settlement-season-stress-sim/reconciliation_with_existing_territory_work.md`:
*"Ground future runs in Goldenfurt... any re-run should seed from goldenfurt_slice... and
should include the existing work in-kernel so it stops re-deriving solved problems."*

Every adapter calls **real built code** where it exists (`sim/territory/ledger.py`,
`registry.py`, `infrastructure.py`) and uses clearly-labeled, provisional, hand-transcribed
reference formulas (cited per-value in each adapter's `resolve_params()`) where PR#119's
mechanics have no sim code yet (governance verbs, the Directive generator, the event-deck
engine, and the Π homeostat are all still spec-only per `goldenfurt_slice/README.md`). This
turns PR #125's one-off LLM-narrative claims into deterministic, re-runnable, code-executed
trials — the same claim can be checked again after any future edit by re-running the harness,
not by re-reading a paragraph.

Adapters: `tools/sim_harness/adapters/pr119_governance/` (`goldenfurt_fixture.py` + 7
`pr119_*.py` adapters). Runs recorded live in `references/audit_registry.jsonl`
(`audit_type: simulation_balance`) and as full JSONL traces under `tools/sim_harness/results/`
(gitignored — re-run to reproduce; every run is seed-deterministic).

## Findings

| PR#119 item | Adapter · decision point | n | Verdict | Result | Call vs. #125 / reconciliation doc |
|---|---|---|---|---|---|
| §1.0b Recognition Fork (ED-FA-0019) | `pr119_recognition_accountability` · `recognition_fork` | 100 | PASS | Confirm 57 / New-Grant 43 — even branch coverage, no structural issue | Not separately examined by #125; clean bill of health |
| §1.0c Court Attendance/Hostage-Kin (ED-FA-0020) | same · `court_attendance_skip` | 100 | PASS | Attended 73 / Skipped 27 | Not separately examined by #125; clean bill of health |
| §1.0d Performance Audit (ED-FA-0021) | same · `performance_audit_vs_g606` | 100 | PASS (0 flags; informative, not degenerate) | both-fire 25 / only-PA 5 / only-G606 12 / neither 58 | **SHARPENS** the reconciliation doc's §A.2 "likely DUPLICATES Goldenfurt's recall" claim: a real, non-trivial 25% co-fire rate under the shared-signal model — recommend the doc's own fix (merge §1.0d onto the G606 signal, §C.2) before ratification, not just "worth reconciling" |
| §2.5a Guild entry fork (ED-FA-0022) | `pr119_guild_ladder` · `entry_fork` | 100 | PASS | 4-way split, no collision vs. Orsk (NPC-G02) | Clean bill of health |
| §2.5a Guild mastership fork (ED-FA-0023) | same · `mastership_fork` | 100 | PASS | 3-way split | Clean bill of health |
| §1.3c Ordenanza Ratification (ED-SE-0023) | same · `ordenanza_ratification` | 100 | PASS | overwhelming 33 / success 42 / partial 20 / failure 5 (real dice roll via `valoria_dice`) | Clean bill of health; correctly composes with the existing dice engine rather than re-deriving it |
| §1.1a Clerk Capacity (ED-SE-0022) | — not adapter-tested this pass — | — | — | — | **Scope gap, flagged not hidden**: no dedicated decision point this wave; the opaque-AP-source/Clerk-Corruption interaction is untested |
| §1.3a Locked Extraction Figures / `Compact` (ED-SE-0018/19) | `pr119_ledger_family_collision` · both | 100 | PARTIAL (1 flag) | `collision_confirmed` 100/100; `Compact` tag **silently accepted** as an unrecognized 6th kind 100/100 | **CONFIRMS + SHARPENS** the reconciliation doc's ★ top actionable finding against live code, not prose: `ledger.TAG_KINDS` already has 5 members (`{Precedent, Grudge, Debt, Reputation, Leverage}`), so `Compact` would be a 6th, not "the fifth" — and `ledger_add()` has **zero validation**, so shipping §1.3a as-authored today would silently corrupt the ledger schema, not error. Recommend blocking ratification until §1.6 either reuses `Leverage` or the built `TAG_KINDS` is deliberately extended |
| §1.3b Bind the Cells (ED-SE-0020) | `pr119_bind_the_cells` · both | 100 | PASS | Goldenfurt's real 9 actors / 5-household cells = 1 full cell + remainder 4 (`cells_remainder`); liability cascade: no-stack 7 / partial 61 / Cell-Revolt 32 | **SHARPENS** the reconciliation doc's §B.2 three-granularity finding with a concrete number against Goldenfurt's real cast, not an abstract count; the liability-cascade math itself is stable and playable (32% revolt at a moderate 0.35/season infraction rate) — the gap is purely the missing population-granularity layer, not the consequence mechanic |
| §3.3b Za patron-lapse (ED-SE-0021) | `pr119_subnational_factions` · `za_patron_lapse` | 100 | PASS | intact 66 / shored-up 16 / lapse 18 | Clean bill of health |
| §3.3c Seggio Council / Mandate-Challenge (ED-SE-0024) | same · `seggio_removal_path` | 100 | PARTIAL (1 flag, expected — see adapter docstring) | `violent_removal_available` 100/100 via a real `infrastructure.seizure_ob_modifier()` call | **CONFIRMS** the reconciliation doc's §A.3 CRITICAL→MEDIUM down-tiering with an executable proof: the violent path is real, capped, live code; the `DEGENERATE_DISTRIBUTION` flag firing on every single run mechanically demonstrates the softer political Mandate-Challenge path is not probabilistically rare — it is **totally unreachable**, no resolver exists |
| Π pressure homeostat (`sim_build_spec.md` §5, CG-1) | `pr119_pressure_homeostat` · `pi_trajectory_band` | 500 | PARTIAL (1 flag) | `runaway_high` 500/500 from Goldenfurt's real Π=4 start | **CORROBORATES + SHARPENS** the doubly-confirmed (#125 narrative sim + the prior 500-seed `settlement_mgmt_stress_01` batch) negative-death-spiral finding with a **third, independent, code-executed** result, and identifies a specific mechanical culprit neither prior pass named: `restore_toward(3)`'s magnitude is capped at exactly 1/season, so once net per-season pressure churn exceeds ~1 (plausible under this run's documented test-scenario input rates), no amount of restoring force can arrest the climb — **CG-1 fixed the downward-stall bug but does not by itself guarantee the town stays in-band under sustained pressure.** Scoping caveat: this run tests one input regime (moderate-to-high NPC/need engagement); a "quiet, well-governed town" regime is not covered by Gate-0 and is flagged as future work, not silently assumed away |
| L/PS inert (ED-FA-0004) | `pr119_structural_gaps` · `lps_inert_check` | 100 | PASS | `inert_confirmed` 100/100 (real source-text scan of `registry.py`/`ledger.py`/`settlement.py`) | **CONFIRMS** the reconciliation doc's §C.5 finding directly against live source, not the inline code comment's own self-report |
| Two event architectures (predicate-sweep vs. card-deck) | same · `event_architecture_fork` | 100 | PASS | `both_present` 100/100 (real filesystem check) | **CONFIRMS** §C.3: both `tests/sim/settlement_mgmt_stress_01/` and the card-deck substrate (`goldenfurt_slice/event_deck.md`) are live in the repo simultaneously, no reconciling decision on record |

## What this is not

- Not a ratification of any PR#119 item — every `## Status:` line stays as-is.
- Not a claim that the simplified stochastic proxies (documented per-parameter as
  "test-scenario value, not canon-derived" in each adapter's `resolve_params()`) are balanced
  or final numbers — they exist to explore the branch/failure space of each mechanic, the same
  role `balance.py`'s curated sweeps play for personal combat, not to set final constants.
- Not full coverage of PR#119: §1.1a Clerk Capacity has no dedicated decision point this wave
  (see the findings table) — a real scope gap, named here rather than silently covered.
- Not a replacement for #125's seed-by-seed narrative traces (`seed_traces/seed_S1..S7*.md`),
  which read for texture and cascade *plausibility* in a way a branch-count table cannot; the
  two approaches are complementary, not competing.

## Re-running

```
python3 -m tools.sim_harness.harness --adapter pr119_recognition_accountability --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_guild_ladder --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_ledger_family_collision --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_bind_the_cells --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_subnational_factions --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_structural_gaps --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_pressure_homeostat --trials 500 --seed 0
```

Add `--no-registry` for a local dry run that skips the `audit_registry.jsonl` append.
