# Vector Audit — v1 → v2 → v3 History

This document captures the methodology evolution. Future runs should NOT relax the procedural choices in §3 of `methodology.md` without understanding why each was tightened.

---

## v1 (commit ac8f55aa, 2026-04-29 morning session)

**What it did:** Hand-curated TF-IDF over the design corpus. Produced 12 TOPO findings.

**What was wrong:**
- No validation gate. Findings were treated as authoritative without internal consistency check.
- No citation graph. "Implied connection" findings couldn't be filtered against actual citations.
- Within-class clustering not addressed. Conviction-Conviction pairs scored high cosine and showed up as "missing connections" — taxonomy artifact.
- Single signal (TF-IDF) treated as primary.

**Verdict:** Findings were leads but not verifiable. v1 register kept as historical record; v3 register supersedes for actionable findings.

---

## v2 (PP-676, 2026-04-29 afternoon)

**Pivot from v1:** Added pilot validation (Stage 0), citation graph (Stage 2.5 explicit-only), corpus split (design vs discourse), expected_groups Jaccard validation.

**What v2 did right:**
- Required validation before publishing findings
- Added explicit-citation graph as independent signal
- Class taxonomy filter for within-class pairs (later applied)
- Pre-committed thresholds in workplan

**What went wrong with v2:**

1. **Validation FAILED at Jaccard 0.222** (below 0.30 threshold). v2 reported findings anyway with caveats — but the failure was partly a methodology defect: k=4 k-NN excluded small expected_groups (a 3-token group has max possible Jaccard 0.25 < 0.30 threshold no matter what).

2. **Threshold deviation post-hoc.** v2 lowered cosine 0.35 → 0.20 for implied-missing because "magnitudes turned out lower than expected." This is exactly the unconscious tuning the pre-commit was designed to prevent. Once thresholds shift after seeing data, you can't trust which findings are signal vs. tuning artifact.

3. **Within-class clustering not filtered before reporting.** Top 8 of 103 implied-missing pairs were within-class artifacts (Conviction-Conviction scoring high because they're all in the same paragraphs as a taxonomy block).

4. **Token deduplication missing.** `Tensions ↔ Tensions Deck` scored 0.926 cosine — same concept, two tokens.

5. **Citation graph too sparse to filter.** 11 token-edges across 84 tokens. "No citation" was the default for nearly every pair, so "implied-but-missing = high cosine + no citation" reduced to "high cosine."

6. **Out-degree-only computation.** v2 measured cite degree as `len(g_cite[t])` which is OUT-only. Tokens without dedicated docs (55 of 84) had artificial degree 0. The flagship "faction/NPC/Conviction-as-hub" finding was an artifact of TF-IDF cosine paragraph breadth, NOT structural centrality.

7. **expected_groups derived from prior.** v2 tested methodology against my hand-curated grouping guess. Circular: can't distinguish "methodology broken" from "prior wrong."

8. **Two diagnostics produced null results.** Status-disagreement = 0 pairs, empty regions = 0 cells. Either thresholds were wrong or diagnostics didn't apply at this scale.

9. **Auto-extracted tokens unvalidated.** Some auto-finds were probably not first-class concepts.

10. **Promised but never run:** "diagnostics run twice — full and auto-only" was in workplan, never executed.

11. **Discourse corpus extracted, never used.** Workplan said "recent attention overlay"; v2 never built it.

12. **Unconventional paragraph-IDF.** v2 weighted paragraphs containing many tokens lower. Defensible but never validated against standard sklearn.

13. **Arbitrary document weights.** 1.0/0.7/0.3 for canonical/provisional/struck — pulled from air, no justification.

14. **MS Trajectory at 0 paragraphs was a regex bug.** Initial run showed 0 mentions; I added a lowercase variant and got 2. The 0-result should have triggered tokenization debug, not been reported.

**Findings that survived v2 → v3:**
- Settlement Layer downstream sink (turned out to be partially wrong — see v3 §V3-7 — but the methodology of citation-graph cascade analysis was right)
- Vocabulary debt three terms (direct corpus match, methodology-independent)
- Sparse-context analysis (refined in v3)

**Findings that v3 corrected:**
- "Faction/NPC/Conviction-as-hub" structural claim (v3 §V3-1: corpus IS system-anchored when measured correctly)
- "Project documents people, not systems" (same correction)

---

## v3 (PP-676, 2026-04-29 same session)

**Pivot from v2:** TF-IDF demoted to supporting; multi-graph triangulation primary; structural-property validation replacing k-NN Jaccard; in+out neighbor union for degree; expanded citation graph (≥2 mention threshold); within-class filter applied; token dedup explicit.

**v3 validation outcome: 2/3 PASS (P1, P3 pass; P2 fails for structural-finding reason).**

**P2 failure was itself a finding:** throughlines framework lacks lexical anchoring of Convictions. PP-677 added Load-bearing systems column to address. Future v3 runs (post-PP-677) should re-check P2.

**v3 corrected v2's flagship finding:** corpus IS system-anchored. NPC Behavior is the integration spine (cite-degree 56 in+out across 84 tokens). v2's "faction/NPC/Conviction-as-hub" was a TF-IDF cosine artifact.

**v3's lasting findings:**
- §V3-1: NPC Behavior is the integration spine (cite-deg 56). Corpus IS system-anchored.
- §V3-2: Throughlines framework lacks formalized system-token coupling (P2 fail).
- §V3-3: Peninsular Strain + IP only multi-graph hubs at ≥3/4 graphs.
- §V3-4: Top 15 notional pairs reveal CI as largest implicit hub with no metadata.
- §V3-5: 14 multi-graph isolates incl. 5/7 Convictions and 3/4 Pressure Points.
- §V3-6: Discourse/design ratio surfaces over- and under-attention.
- §V3-7: Cascade-without-return downstream sinks (foundation tokens correctly; Disposition + Domain Action concerningly).
- §V3-9: Vocabulary debt 3 terms across 14 docs, concentration mapped.

---

## Lessons baked into v3 methodology

The procedural choices in `methodology.md` §3 are not "the way to do it" — they're "the way that works after v1 and v2 failed." Lessons embedded:

| v3 procedure | Why |
|---|---|
| Standard sklearn TF-IDF | v2's paragraph-IDF was unconventional and undefended |
| Uniform document weighting | v2's 1.0/0.7/0.3 was arbitrary |
| In+out neighbor union for cite-degree | v2 out-only produced flagship-finding artifact |
| ≥2 mention threshold for implicit citations | v2 explicit-only had 11 edges, too sparse to filter |
| Class taxonomy within-class filter | v2 had 103 implied-missing pairs, top 8 were taxonomy artifacts |
| Pre-committed thresholds LOCKED | v2 deviated 0.35 → 0.20 post-hoc, invalidating those findings |
| Structural-property validation (P1/P2/P3) | v2's k-NN Jaccard was unsatisfiable for small expected_groups |
| TF-IDF supporting only, multi-graph primary | v2's TF-IDF-primary produced taxonomy artifacts as "structural findings" |
| Pilot validation gate (Stage 0) | v1 had no sanity check on tokenization |
| Direct GitHub Contents API for fetch | github_ops auto-routes to _index.md files which lack body content for citation graph |

---

## When to deviate from v3 methodology

Tighten further (encouraged):
- Add cross-graph numeric confidence scoring
- Add directional citation analysis to cascade modes
- Sensitivity-test ≥2 implicit-mention threshold (try ≥3)
- Add G_q (quality-tier graph) from PP vetting Q-fail correlations

Relax (forbidden without explicit methodology-revision PP):
- Cosine thresholds in any mode
- Class taxonomy filter
- In+out vs. out-only
- TF-IDF demotion to supporting
- Pre-commit lock on thresholds

If a finding requires relaxation to surface, it's not a methodology problem — it's a finding about what the methodology can't see (which goes in §6 of methodology.md "What this can't find").
