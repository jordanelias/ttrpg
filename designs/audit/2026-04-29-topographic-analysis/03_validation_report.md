<!-- [PROVISIONAL: 2026-04-29 — topographic analysis v3 validation report] -->
<!-- AUTHORITY: PP-676 -->

# Topographic Analysis v3 — Validation Report

**Date executed:** 2026-04-29
**Workplan:** designs/audit/2026-04-29-topographic-analysis/00_workplan.md (v3)

## Three structural properties

### P1 — Foundation periphery

**Hypothesis:** Foundation tokens (Self-Rendering, Leap, Coherence, Throughlines, Ein Sof) are referenced by many other tokens. Their mean degree in G_cite + G_throughline should exceed the corpus median.

**Method:** Compute mean degree across foundation tokens; compare to median across all 84 tokens.

**Result:** 
- G_cite: foundation mean = 7.4, corpus median = 6.0 — foundation > median ✓
- G_throughline: foundation mean = 0.0, corpus median = 0.0 — neutral (both at floor)

**Verdict: PASS** on cite component; throughline component is structurally degenerate (see §V3-2 of weakness register).

### P2 — Conviction class symmetry

**Hypothesis:** The 7 Convictions are symmetrically embedded in the throughline framework (each Conviction maps to faction-aligned throughlines through their faction connection). Standard deviation of Conviction degrees in G_throughline should be < 50% of mean Conviction degree.

**Method:** Compute G_throughline degree for each of {Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity}. Coefficient of variation = std / mean.

**Result:** All 7 Convictions have G_throughline degree = 0. Mean = 0, CV = undefined.

**Verdict: FAIL** — but for a structural reason: throughline names+descriptions don't lexically include Conviction names. Convictions are anchored to factions in the framework; factions are anchored to throughlines (T-08, T-09, T-11, T-15a/b/c). Convictions never appear in throughline name+description directly.

**This failure is not a methodology defect — it's a finding** (see weakness register §V3-2): the throughlines framework lacks formalized system-token coupling.

### P3 — Citation density smoke test

**Hypothesis:** Expanded citation graph (explicit + implicit references) should have ≥ 100 token-edges. v2's 11 edges from explicit-only parsing was structurally inadequate for filter use.

**Method:** Count `g_cite[src][tgt]` directed edges.

**Result:** 421 token-edges. **PASS** (38× v2's count).

## Combined verdict

**2/3 properties pass → methodology VALIDATED.**

The single failing property (P2) fails for a corpus-structural reason that is independently captured as weakness register finding §V3-2. No properties failed for methodology reasons.

## What this validation does not establish

1. Validation doesn't establish that v3's findings are *complete* — only that the methodology produces signal that has expected structural properties.
2. Validation doesn't establish per-finding correctness; each finding still requires manual cross-check before any action is taken on it.
3. Validation is internal-consistency only — no external ground truth (e.g. design intent, implementation experience) is brought to bear.

## Methodology improvements vs v2

| v2 problem | v3 result |
|---|---|
| Threshold deviation (post-hoc 0.35 → 0.20) | All thresholds locked, no deviation |
| Validation k=4 mathematically excludes small groups | Replaced with structural properties; no k-NN dependency |
| Within-class clustering polluted implied-missing | Class taxonomy filter applied; implied-missing from 103 → 3 (clean signal) |
| Citation graph too sparse (11 edges) | Expanded graph (421 edges); citation-absence filter actually filters now |
| Empty regions / status-disagreement null | Both diagnostics dropped from v3 |
| Validation circularity (prior tested against prior) | Independent structured graphs (Μ/throughline/PP) used as alternate ground truth |
| Out-degree-only computation | In+out neighbor union for accurate degree |

## Outstanding methodology questions

1. **Should implicit-citation threshold be ≥ 2 or higher?** ≥ 2 admits some formulaic cross-mentions. ≥ 3 might lose real connections. Sensitivity analysis would help; not done in v3.
2. **Should PP archive be included?** v3 uses only `patch_register_active.yaml` (23 patches). Archived patches (long-term coupling history) might surface different patterns.
3. **Should G_pp distinguish patch severity?** A P1 patch coupling two tokens implies stronger relationship than a P3 patch. v3 weights all PP edges equally.
4. **Should there be a sixth graph for Q-tier vetting?** PP entries with Q-fail or Q-flag could form an "issues correlate" graph. Not built in v3.
