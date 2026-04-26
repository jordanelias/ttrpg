# Audit Pass — Stage 3 Summary

**Generated:** 2026-04-25
**Audit reports produced:** 10

## Recommendations summary

| topic | atoms | PASS | FLAG | MANUAL | unknown IDs | recommendation |
|---|---|---|---|---|---|---|
| `01_throughlines_meta` | 22 | 1 | 1 | 2 | 3 | **INGEST-WITH-FIXES (specific drift/coverage flags must be resolved before canon ingestion)** |
| `02_solmund_cultural_guide` | 32 | 1 | 0 | 4 | 0 | **EDITORIAL-REVIEW (Jordan only — not Claude-decidable)** |
| `03_threadwork_design` | 71 | 0 | 0 | 4 | 19 | **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)** |
| `04_faction_balance_three_modes` | 50 | 0 | 0 | 4 | 3 | **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)** |
| `05_v2_historicity_correction` | 9 | 1 | 0 | 3 | 0 | **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)** |
| `06_mechanical_review_audit` | 83 | 0 | 0 | 4 | 27 | **SUB-DECOMPOSE-RECOMMENDED (83 atoms; sub-split by section family before canon decisions)** |
| `07_audit_s1_s7_synthesis` | 2 | 0 | 0 | 4 | 0 | **CONSIDER-FOLD (only 2 residual atoms; consider folding into 08_session_consolidation rather than maintaining as standalone audit subject)** |
| `08_session_consolidation` | 19 | 0 | 0 | 4 | 7 | **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)** |
| `09_canon_rectification_pp675_ed783` | 18 | 0 | 0 | 4 | 2 | **MANUAL-REVIEW-REQUIRED (programmatic audit insufficient; substantive content review needed)** |
| `10_session_log_index` | 10 | 0 | 0 | 4 | 2 | **INDEX-ONLY (verify ID presence; no canon ingestion expected)** |

## Recommendation key

- **INGEST-READY** — programmatic audit clean; pending Jordan sign-off at Stage 4
- **INGEST-WITH-FIXES** — specific drift/coverage flags must be resolved before canon ingestion
- **MANUAL-REVIEW-REQUIRED** — programmatic audit insufficient; substantive content review needed
- **EDITORIAL-REVIEW** — Solmund (02): editorial-judgment content; only Jordan can decide
- **SUB-DECOMPOSE-RECOMMENDED** — topic too large to audit/ingest as single unit; sub-split first
- **CONSIDER-FOLD** — too few residual atoms to justify standalone topic
- **INDEX-ONLY** — session-log index; no canon ingestion expected

## Stage 4 inputs

Each `<topic_id>_audit.md` report contains: recommendation, per-checklist-item status, ID-presence verification, path-reference audit, intra-source drift findings, topic-specific findings.

Stage 4 (post-audit canon decisions) is OUT OF SCOPE for this work and will be planned separately based on these audit findings + Jordan input.