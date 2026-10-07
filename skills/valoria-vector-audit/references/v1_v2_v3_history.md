# Vector Audit — v1 → v2 → v3 History

The v1 and v2 methodologies failed validation; v3 is canonical. The rules their failures produced
are `SKILL.md`'s Common Failure Modes and `methodology.md` §3–§4. This file holds only what may and
may not be changed.

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

Relax only with the failure each prevents in hand (`SKILL.md` Common Failure Modes, or as stated):
- Structural-property validation (never a grouping derived from a prior — circular)
- Uniform document weighting — status weights (1.0/0.7/0.3) were never validated
- Standard sklearn TF-IDF — a custom paragraph-IDF is unconventional and undefended
- Token deduplication (§3.3) and the Stage 0 pilot gate

If a finding requires relaxation to surface, it's not a methodology problem — it's a finding about what the methodology can't see (which goes in §6 of methodology.md "What this can't find").
