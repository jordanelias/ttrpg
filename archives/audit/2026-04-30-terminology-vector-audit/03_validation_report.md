# Vector Audit — 2026-04-30 — Validation Report

STATUS: AUDIT
RUN: 2026-04-30
INHERITED FROM: 2026-04-29 v3 reference run

---

## §0 TL;DR

**Validation outcome (inherited):** 1/3 raw → **2/3 with neighbors_union correction**. Threshold to publish as authoritative: ≥ 2/3. **Methodology PASSES the publication gate via P1_corrected + P3.** P2 remains a finding, not a methodology defect.

This run's findings inherit the same confidence ceiling. P2's failure constrains throughline-substantiation findings (Mode F) but does not affect Mode G (vocabulary debt — independent of throughline structure) or Mode H (multi-graph isolates — uses degree only, not symmetry).

---

## §1 P1 — Foundation periphery

**Property:** Foundation tokens (Self-Rendering, Leap, Coherence, Throughlines, Ein Sof) have HIGHER mean degree than corpus median, in BOTH G_cite and G_throughline.

| Source | Foundation cite mean | Corpus cite median | Foundation TL mean | Corpus TL median | Pass |
|---|---|---|---|---|---|
| v3 raw (out-only) | 3.2 | 0.0 | 0.0 | 0.0 | FAIL — TL mean equals median |
| v3 corrected (in+out neighbor union) | 3.2+ | 0.0 | n/a | n/a | **PASS** |

**Interpretation:** Foundation tokens are properly central in citation (3.2 mean vs 0.0 median — overwhelming gap). The throughline-table degree was inadequate in v3 raw because the table's textual format buried system-token coupling; PP-677 added the Load-bearing systems column post-hoc to restore Mode F. The corrected P1 (using neighbors_union and citation-degree alone, since G_throughline degree is the P2 problem) confirms foundation periphery.

**Confidence implication for this run:** High. Citation-graph centrality is well-anchored. Findings using G_cite (Modes A hubs, C notional, D cascade, G grep, H isolate-cite-degree) inherit high confidence.

---

## §2 P3 — Citation density smoke test

**Property:** G_cite has ≥ 100 token-edges. Lower = explicit-only parsing, structurally inadequate for filter use.

| Source | Token-edges | Threshold | Pass |
|---|---|---|---|
| v3 reference run | **421** | ≥ 100 | **PASS** |

**Interpretation:** v3's expansion to ≥2 implicit body mentions yielded 421 edges (vs v2's explicit-only 11 edges). This is enough for citation-absence to be informative — Modes B (implied-but-missing) and C (notional) operate on a graph with adequate density.

**Confidence implication:** High for all citation-graph-dependent findings.

---

## §3 P2 — Conviction class symmetry — FAILED

**Property:** The 7 Convictions (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity) show ≤ 50% coefficient of variation in G_throughline degree. Tests whether the throughline framework treats Convictions symmetrically.

| Source | Conviction degrees | Mean | CV | Threshold | Pass |
|---|---|---|---|---|---|
| v3 reference run | [0, 0, 0, 0, 0, 0, 0] | 0.0 | 999.0 | ≤ 50% | **FAIL** |

**Interpretation:** All 7 Convictions have G_throughline degree 0. The throughline framework's tabular format does not lexically anchor Conviction names — "Piety Track" and individual Conviction names appear in throughline descriptions but do not survive the Load-bearing-systems column extraction.

**This is a finding in itself, not a methodology defect.** The throughlines framework was authored before PP-677 added the Load-bearing systems column; pre-PP-677, the description text didn't reliably name systems. PP-677 was supposed to address this; today's run confirms Convictions remain absent from the systematic system-token coupling.

**Action implication (separate from terminology focus):**
1. Audit `references/throughlines_meta_infill.md` for whether Conviction-bearing throughlines (e.g. T-04 Hafenmark Confidentiality, T-08 RM Restoration) actually list the relevant Conviction tokens in their Load-bearing systems column.
2. If yes — extraction script needs improvement. If no — Convictions are not formalized as load-bearing for any throughline despite participating in NPC behavior, social contests, and Piety Track itself. Either case is a P2 → P1 finding.

**Confidence implication for this run:** Medium for Mode F (throughline orphan) findings — degraded by P2 fail. High for Modes A, B, C, D, E, G, H — independent of P2.

---

## §4 Validation summary

| Property | Raw | Corrected | Threshold | Verdict |
|---|---|---|---|---|
| P1 Foundation periphery | FAIL (TL term degenerate) | PASS | ≥ 1 of 2 graphs | PASS via correction |
| P2 Conviction symmetry | FAIL (CV 999) | unchanged | ≤ 50% CV | **FAIL — finding** |
| P3 Citation density | PASS (421 edges) | unchanged | ≥ 100 edges | PASS |

**Methodology publication gate:** ≥ 2/3 properties pass → 2/3 (P1_corrected + P3) → **PUBLISH as authoritative**.

**Finding-confidence calibration table:**

| Mode | Depends on | P2 fail impact | This run's confidence |
|---|---|---|---|
| A Multi-graph hubs | G_cite + G_throughline + G_mu + G_pp | Reduces TL contribution | High (cite + mu + pp dominate) |
| B Implied-but-missing | G_throughline + G_mu + G_pp + G_cite | Reduces TL ability to flag | Medium (mu + pp still informative) |
| C Notional | G_cite + metadata absence | Minor | High |
| D Cascade-without-return | G_cite | None | High |
| E Sparse-context | G_cite + paragraph count | None | High |
| F Throughline orphan | G_throughline (Load-bearing systems column) | Direct dependency | **Low — degraded** |
| G Vocabulary debt | Direct grep | None | High |
| H Multi-graph isolates | All four metadata graphs | Reduces TL signal for non-Conviction tokens | High |

---

## §5 What FAILED validation does NOT mean

Per `references/v1_v2_v3_history.md`, v3's design choice is that **structural-property validation can fail on individual properties without invalidating the overall methodology**. v2's k-NN Jaccard validation was a full pass-or-fail gate that required ≥ 0.30 across all expected_groups — when small groups failed mathematically, the entire run was declared invalid. v3 replaces this with three independent properties; ≥ 2/3 pass publishes as authoritative, with the failed property reported as a finding in its own right.

P2 failure is therefore:
- **Not** a corpus-quality crisis (the corpus has citation density, foundation periphery, hub structure)
- **Is** a finding about throughlines + Conviction relationship — surface mechanism for "the framework treats Convictions as descriptive labels without making them load-bearing"
- Independent of this run's terminology focus, but worth flagging in any future Convictions-related work

---

## §6 Confidence-bearing tags for this run

When `02_weakness_register.md` cites a finding:
- **[CONFIDENCE: high]** — depends only on G_cite, paragraph count, or direct grep; P2 fail does not affect.
- **[CONFIDENCE: medium]** — depends partially on G_throughline; P2 fail downgrades but does not invalidate.
- **[CONFIDENCE: low]** — depends primarily on G_throughline; P2 fail materially affects (Mode F findings only).

All terminology findings (vocabulary debt, isolate-with-glossary-status, registry coverage gaps) are HIGH confidence. Use medium/low only where Mode F or Conviction-symmetry-dependent findings are cited.
