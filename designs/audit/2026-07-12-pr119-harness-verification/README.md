# PR#119/#125 provisional-mechanic verification via `tools/sim_harness/`

**Status: PROPOSED, read-only.** Mirrors PR#125's own framing ("NOT canon") — this doc
verifies claims already on the table (PR #119's 12 authored items, PR #125's stress-test +
reconciliation findings), it ratifies nothing. No `## Status:` line in any PR#119 doc changes
as a result of this pass.

## What this is

Nine [`tools/sim_harness/`](../../../tools/sim_harness/) **provisional adapters**
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

**Two coverage passes, not one.** The first pass (8 adapters) tests each of PR#119's 12 items
in isolation or in a tight, closely-related pair, with independent random draws per mechanic.
That is real coverage but cannot see an interaction that only appears when two proposals share
state over time. The second pass — `pr119_integrated_campaign.py` — runs all 11 season-scoped
items (everything except the one-off §1.0b Recognition Fork) as a single, persistent,
multi-season campaign on ONE real Goldenfurt `Settlement`, so later mechanics read the real
state earlier mechanics wrote. See "Interdependency & emergence" below.

Adapters: `tools/sim_harness/adapters/pr119_governance/` (`goldenfurt_fixture.py` + 9
`pr119_*.py` adapters + `campaign_stats.py`, a standalone world-state statistics pass over the
integrated campaign). Runs recorded live in `references/audit_registry.jsonl`
(`audit_type: simulation_balance`) and as full JSONL traces under `tools/sim_harness/results/`
(gitignored — re-run to reproduce; every run is seed-deterministic).

## Findings — single-mechanic pass

| PR#119 item | Adapter · decision point | n | Verdict | Result | Call vs. #125 / reconciliation doc |
|---|---|---|---|---|---|
| §1.0b Recognition Fork (ED-FA-0019) | `pr119_recognition_accountability` · `recognition_fork` | 100 | PASS | Confirm 57 / New-Grant 43 — even branch coverage, no structural issue | Not separately examined by #125; clean bill of health |
| §1.0c Court Attendance/Hostage-Kin (ED-FA-0020) | same · `court_attendance_skip` | 100 | PASS | Attended 73 / Skipped 27 | Not separately examined by #125; clean bill of health |
| §1.0d Performance Audit (ED-FA-0021) | same · `performance_audit_vs_g606` | 100 | PASS (0 flags; informative, not degenerate) | both-fire 25 / only-PA 5 / only-G606 12 / neither 58 | **SHARPENS** the reconciliation doc's §A.2 "likely DUPLICATES Goldenfurt's recall" claim: a real, non-trivial 25% co-fire rate under the shared-signal model over a *6-season* window — the integrated campaign below (a 20-season window) sharpens this further into near-certainty |
| §1.1a Clerk Capacity (ED-SE-0022) | `pr119_clerk_capacity` · both | 100 | PASS | AP growth: grows 17 / capped 34 / dismissed 49; corruption: discovered 93 / undiscovered 7 | **Closes the scope gap** the first commit of this doc flagged. Standalone: no structural collision. Composed: see "Interdependency & emergence" — this item turns out to be the single biggest lever on every OTHER item's outcome |
| §2.5a Guild entry fork (ED-FA-0022) | `pr119_guild_ladder` · `entry_fork` | 100 | PASS | 4-way split, no collision vs. Orsk (NPC-G02) | Clean bill of health |
| §2.5a Guild mastership fork (ED-FA-0023) | same · `mastership_fork` | 100 | PASS | 3-way split | Clean bill of health |
| §1.3c Ordenanza Ratification (ED-SE-0023) | same · `ordenanza_ratification` | 100 | PASS | overwhelming 33 / success 42 / partial 20 / failure 5 (real dice roll via `valoria_dice`) | Clean bill of health; correctly composes with the existing dice engine rather than re-deriving it |
| §1.3a Locked Extraction Figures / `Compact` (ED-SE-0018/19) | `pr119_ledger_family_collision` · both | 100 | PARTIAL (1 flag) | `collision_confirmed` 100/100; `Compact` tag **silently accepted** as an unrecognized 6th kind 100/100 | **CONFIRMS + SHARPENS** the reconciliation doc's ★ top actionable finding against live code, not prose: `ledger.TAG_KINDS` already has 5 members (`{Precedent, Grudge, Debt, Reputation, Leverage}`), so `Compact` would be a 6th, not "the fifth" — and `ledger_add()` has **zero validation**, so shipping §1.3a as-authored today would silently corrupt the ledger schema, not error. Recommend blocking ratification until §1.6 either reuses `Leverage` or the built `TAG_KINDS` is deliberately extended |
| §1.3b Bind the Cells (ED-SE-0020) | `pr119_bind_the_cells` · both | 100 | PASS | Goldenfurt's real 9 actors / 5-household cells = 1 full cell + remainder 4 (`cells_remainder`); liability cascade: no-stack 7 / partial 61 / Cell-Revolt 32 | **SHARPENS** the reconciliation doc's §B.2 three-granularity finding with a concrete number against Goldenfurt's real cast, not an abstract count; the liability-cascade math itself is stable and playable — the gap is purely the missing population-granularity layer, not the consequence mechanic |
| §3.3b Za patron-lapse (ED-SE-0021) | `pr119_subnational_factions` · `za_patron_lapse` | 100 | PASS | intact 66 / shored-up 16 / lapse 18 | Clean bill of health |
| §3.3c Seggio Council / Mandate-Challenge (ED-SE-0024) | same · `seggio_removal_path` | 100 | PARTIAL (1 flag, expected — see adapter docstring) | `violent_removal_available` 100/100 via a real `infrastructure.seizure_ob_modifier()` call | **CONFIRMS** the reconciliation doc's §A.3 CRITICAL→MEDIUM down-tiering with an executable proof: the violent path is real, capped, live code; `DEGENERATE_DISTRIBUTION` firing every run mechanically demonstrates the softer political Mandate-Challenge path is not probabilistically rare — it is **totally unreachable**, no resolver exists |
| Π pressure homeostat (`sim_build_spec.md` §5, CG-1) | `pr119_pressure_homeostat` · `pi_trajectory_band` | 500 | PARTIAL (1 flag) | `runaway_high` 500/500 from Goldenfurt's real Π=4 start | **CORROBORATES + SHARPENS** the doubly-confirmed (#125 narrative sim + the prior 500-seed `settlement_mgmt_stress_01` batch) negative-death-spiral finding, and identifies a specific mechanical culprit: `restore_toward(3)`'s magnitude is capped at exactly 1/season, so once net per-season pressure churn exceeds ~1, no restoring force can arrest the climb — **CG-1 fixed the downward-stall bug but does not by itself guarantee the town stays in-band.** The integrated campaign below reproduces this a third way, from real ledger-tag accumulation instead of a proxy draw |
| L/PS inert (ED-FA-0004) | `pr119_structural_gaps` · `lps_inert_check` | 100 | PASS | `inert_confirmed` 100/100 (real source-text scan of `registry.py`/`ledger.py`/`settlement.py`) | **CONFIRMS** the reconciliation doc's §C.5 finding directly against live source, not the inline code comment's own self-report |
| Two event architectures (predicate-sweep vs. card-deck) | same · `event_architecture_fork` | 100 | PASS | `both_present` 100/100 (real filesystem check) | **CONFIRMS** §C.3: both `tests/sim/settlement_mgmt_stress_01/` and the card-deck substrate (`goldenfurt_slice/event_deck.md`) are live in the repo simultaneously, no reconciling decision on record |

## Interdependency & emergence — `pr119_integrated_campaign`

**Method.** `pr119_integrated_campaign.py`'s `run_campaign()` runs one Goldenfurt `Settlement`
through up to 20 seasons (~5 year-arcs), composing 11 of PR#119's 12 items on **shared, real
state** — every write is a real `sim/territory/ledger.py` tag, a real `registry.Settlement`
field, or a real `infrastructure.py`/`registry.py` function call, not an independent draw per
mechanic. `campaign_stats.py` (a standalone script reusing the SAME `run_campaign()`, not a
re-derivation) gathers per-trial numeric world state the harness's own branch-count trace
doesn't capture. Three parameter regimes, 500 trials each (1,500 total), to check whether
findings are an artifact of one harsh parameter choice or hold generally:

| Regime | `p_comply` | §1.0d streak | `stable` | `recall/demotion` | `rescued` | `fracture/entrenched` | mean seasons survived | mean final Π | mean province Accord |
|---|---|---|---|---|---|---|---|---|---|
| A (default) | 0.50 | 3 | **0** | 436 (87.2%) | 63 (12.6%) | 1 (0.2%) | 10.5 / 20 | 9.98 / 10 | 1.24 |
| B (cooperative governor) | 0.75 | 3 | **0** | 245 (49.0%) | 142 (28.4%) | 113 (22.6%) | 16.3 / 20 | 9.998 / 10 | 1.05 |
| C (B + gentler §1.0d) | 0.75 | 5 | **0** | 241 (48.2%) | 154 (30.8%) | 105 (21.0%) | 16.8 / 20 | 9.997 / 10 | 1.02 |

Reproduce: `python3 -m tools.sim_harness.adapters.pr119_governance.campaign_stats --n 500 --seed 0 [--p-comply 0.75] [--pa-demotion-streak 5]`.

### Headline: recall/demotion dominance is regime-independent

**Zero of 1,500 trials, across three parameter regimes spanning a harsh-to-cooperative
governor and a strict-to-lenient §1.0d threshold, ever reached a `stable_governance` end
state.** Every trial ends either in recall/demotion or a corruption-driven rescue (see below).
Regime C isolates the cause precisely: even with a gentle governor (75% compliant) and a
lenient 5-consecutive-miss §1.0d threshold, `recall_reasons` shows **100% of terminal recalls
route through G606** (0 via `performance_audit`) — because G606's progress is **cumulative,
not streak-based** (capped +1/season, fires at ≥4), so even at 25% non-compliance it reliably
accumulates 4 non-consecutive misses well inside a 20-season window. §1.0d's own
streak-reset design (a single Comply resets `pa_streak` to 0) makes it the FORGIVING mechanic
here; G606, exactly as Goldenfurt already ships it, is the one actually driving outcomes. This
is the single-mechanic pass's 25% co-fire finding (§1.0d row above), generalized and sharpened
by a full campaign: the "duplication" isn't just two mechanics sometimes agreeing — over a
real multi-season horizon, G606 alone accounts for essentially the entire terminal-outcome
distribution, and §1.0d's contribution shrinks to near-zero the more lenient it's tuned.
**This raises, not lowers, the priority of the reconciliation doc's §C.2 recommendation** (merge
§1.0d onto the G606 signal) — tuning §1.0d in isolation cannot fix the dominance problem,
because G606 is the actual driver.

### A genuinely emergent interdependency: Clerk Capacity rescues the recall cascade

§1.1a Clerk Capacity's hidden corruption counter sits on the same Orsk/Konrad bribery web
`npc_cast.md` already authors ("Konrad takes Orsk's coin for advance levy notice"). The
campaign models a Clerk-Corruption Investigate as having a chance to ALSO surface Konrad's
own graft — writing the real `Leverage:konrad-corrupt` tag `event_deck.md`'s EVT-G606 already
treats as the recall-defusing "buried" escape. Result: **a completely unrelated PR#119
AP-economy mechanic mechanically rescues a PR#119 accountability mechanic from firing**, in
30–33% of trials across all three regimes at least once, and permanently (the campaign's
*final* outcome) in 12.6–30.8% depending on regime. Neither §1.0d's nor §1.1a's own text
anticipates this collision — it is only visible once both mechanics share Konrad's real
ledger state in one simulation, exactly the class of finding the single-mechanic pass cannot
produce.

### Π runaway-high reconfirmed a third, independent way

Mean final pressure is 9.98–9.998 / 10 in every regime — essentially every surviving campaign
ends pinned at the ceiling, this time driven by REAL accumulated `Grudge`-family ledger tags
(mean 3.35–5.76 per campaign, written by §1.3b Bind the Cells) rather than the standalone Π
adapter's independent proxy draw. Three methodologically distinct passes (PR#125's LLM-
narrative sim, the isolated `pr119_pressure_homeostat` adapter, and this full campaign) now
agree.

### Real ledger accumulation compounds the confirmed §1.3a bug

Mean 1.48–2.67 `Compact` tags per campaign (via §1.3a's Negotiate Quota) — each one exercising
the confirmed silent-6th-ledger-family-acceptance bug (`pr119_ledger_family_collision` above)
on a live, evolving settlement, not a single isolated write. A campaign that runs the full 20
seasons routinely accumulates 2–3 unvalidated `Compact` tags before anyone would notice.

### Real cross-scale propagation — settlement → province, with a named asymmetry

Every season calls the real `registry.province_accord()` / `province_effective_prosperity()`
over Goldenfurt plus one explicitly-labeled **synthetic, non-canon** province-mate settlement
(`_SYNTHETIC_PROVINCE_MATE_SID`, static stats, constructed only to make the aggregation
non-degenerate — a single-member province floor-averages to itself and proves nothing). Mean
final province Accord drifts from a flat-2 no-churn baseline down to 1.02–1.24 depending on
regime (longer-surviving campaigns in regimes B/C drift lower). **Named limitation, not
hidden:** this campaign wires only a downward Order term (§1.4's own text: Comply "often
strains the settlement") — no positive-recovery term (e.g. a `Develop`/`Sponsor` Order gain)
is composed this wave, so the downward drift is a real but one-directional demonstration of
the propagation *mechanism*, not yet a validated claim about its *magnitude or balance*.
Flagged as concrete follow-up work, not silently assumed away.

### Za / Seggio: rarely terminal, because recall usually ends the campaign first

Za lapse rate 1.6–15.6% and Seggio entrenchment rate 4.2–13.4% across regimes — both LOWER in
the cooperative regimes (B/C), which is counter-intuitive until read against `mean seasons
survived`: cooperative-governor campaigns survive longer (16.3–16.8 vs 10.5 seasons) giving
Za/Seggio dynamics more time to develop, but the SAME cooperative behavior that extends
survival also strengthens the Za patron's standing (correlated with governor standing, per
the adapter's design) and slows `church_attention` accumulation — the mechanics that would
make Za/Seggio the dominant terminal state are the same mechanics recall-avoidance improves.
Guild influence (mean 2.56–3.97) grows steadily with campaign length via §1.3c Ordenanza — the
one composed mechanic with no negative-feedback path at all in this wave's wiring.

## What this is not

- Not a ratification of any PR#119 item — every `## Status:` line stays as-is.
- Not a claim that the simplified stochastic proxies (documented per-parameter as
  "test-scenario value, not canon-derived" in each adapter's `resolve_params()`) are balanced
  or final numbers — they exist to explore the branch/failure/interdependency space of each
  mechanic and their composition, the same role `balance.py`'s curated sweeps play for
  personal combat, not to set final constants. The three-regime table above exists specifically
  to show which findings are regime-independent (recall/demotion dominance, Π runaway,
  Clerk-Capacity rescue) versus regime-sensitive (Za lapse rate, Seggio entrenchment timing).
- Not full coverage even now: §1.0b Recognition Fork is a one-off event with no season-to-
  season state and is deliberately NOT composed into the campaign; the campaign's Order-recovery
  asymmetry (above) is a named, concrete gap, not a claim of balance; no full pairwise
  ablation (running the campaign with each of the 11 items individually removed, to isolate
  each one's marginal contribution to the dominance finding) has been run — a natural next
  wave, not attempted here.
- Not a replacement for #125's seed-by-seed narrative traces (`seed_traces/seed_S1..S7*.md`),
  which read for texture and cascade *plausibility* in a way a branch-count table cannot; the
  two approaches are complementary, not competing.

## Re-running

```
python3 -m tools.sim_harness.harness --adapter pr119_recognition_accountability --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_clerk_capacity --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_guild_ladder --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_ledger_family_collision --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_bind_the_cells --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_subnational_factions --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_structural_gaps --trials 100 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_pressure_homeostat --trials 500 --seed 0
python3 -m tools.sim_harness.harness --adapter pr119_integrated_campaign --trials 200 --seed 0

# world-state / interdependency statistics (the three-regime table above):
python3 -m tools.sim_harness.adapters.pr119_governance.campaign_stats --n 500 --seed 0
python3 -m tools.sim_harness.adapters.pr119_governance.campaign_stats --n 500 --seed 0 --p-comply 0.75
python3 -m tools.sim_harness.adapters.pr119_governance.campaign_stats --n 500 --seed 0 --p-comply 0.75 --pa-demotion-streak 5
```

Add `--no-registry` for a local dry run of the harness CLI that skips the `audit_registry.jsonl`
append. `campaign_stats.py` never touches the registry — it's a pure statistics pass over
`run_campaign()`.
