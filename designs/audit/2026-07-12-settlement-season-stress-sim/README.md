# 2026-07-12 · Settlement-Season Stress Test

Read-only adversarial stress test of the PR#119 provisional governance mechanics (the 12 authored
comparative-governance items, the governance-ripple substrate, the 58-card event deck), run as a 7-seed ×
5-season agent-driven mechanical play-out with **depth-3 failure-cascade tracing** at every major
probability roll and **gap→rejected-proposal testing**. NOT canon.

## Contents

| File | What |
|---|---|
| **`stress_test_synthesis_v1.md`** | **The deliverable.** Max-effort synthesis with a §0 verification/correction layer (two headline findings shown to be kernel-digest artifacts), mechanic-stress verdicts, recurring cascade patterns, gap catalogue, vindicated rejected proposals, balance observations, ranked findings for Jordan. |
| **`reconciliation_with_existing_territory_work.md`** | **Read second.** Corrects and re-weights the synthesis after reviewing the pre-existing settlement/territory work the sim's kernel omitted (`goldenfurt_slice`, built `sim/territory/` code, the 500-seed `settlement_mgmt_stress_01`, the 2026-06-22 baseline audit + march/hierarchy layer). Shows ~⅓ of the sim's findings are already solved/answered, corroborates its strongest one via the 500-seed batch, and surfaces the genuinely new reconciliations (Compact-vs-Leverage ledger families; §1.0d-into-Goldenfurt-recall; two event architectures). |
| `ground_truth_odds.md` | **Appendix A.** Exact resolver-odds tables computed from repo code — `dice_pool` (`skills/valoria-dice-model/valoria_dice.py`) and `d_sigma` (`sim/autoload/sigma_leverage.py` `p_success`). The oracle every stated roll was verified against. |
| `appendix_B_roll_failures.md` | All 57 traced major-roll failures, one row each: event · resolver · P(success) · L1/L2/L3 depth-3 cascade. |
| `seed_traces/seed_S1..S7*.md` | Full per-season narratives for each seed (setup · 5-season trace · verdict). |

## Headline

The **resolution substrate held** across all 7 adversarial seeds (every governor's downfall routed through
the 5 primitives, no invented mechanics); the two NERS-flagged items (§1.0d, §1.3b) had their **MERGE
verdicts confirmed**. The two loudest "author-everything" alarms from the raw run — the event deck's Crisis
band and §1.3c Ordenanza reachability — were **verified to be artifacts of the compressed kernel the sim ran
on, not holes in canon**. The real structural gaps: §3.3c force-resolver lock, §1.3a stale-assessment strip
with no subsistence floor, the §1.3b/§4.5 actor-cap collision, Π death-spiral (no Grudge decay), and
Mandate saturation at scale. See `stress_test_synthesis_v1.md` §0 and §6.

## Method

13-agent Workflow (5 Sonnet/Haiku kernel extractors → 7 Opus high-effort seed sims → 1 Opus max-effort
synthesis) + a main-session verification pass that recomputed every parseable roll against the engine code
and re-checked the headline findings against the full canonical docs.
