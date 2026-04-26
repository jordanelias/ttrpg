# Stage 4 Execution Plan

**Status:** prep package ready. Stage 4 itself requires per-item Jordan editorial decisions.

**This plan** breaks Stage 4 into commit-sized work items, each marked with the editorial decision points required.

## Sequencing

1. **Pre-flight resolutions** (no canon mutations — fix surface issues first):
   - Apply Topic 06 sub-decomposition to `_topic_decomposition.yaml`. Single `[infrastructure]` commit.
   - Resolve missing paths per `missing_paths_resolution.md`. Per-path decision: rename, create, or strike reference. Per resolved path: 1 commit.
   - Resolve ED-543 per `ed_543_forensic.md`. Single decision: register or strike.

2. **MENTIONED ID promotion** (per-topic, editorial-bound):
   - Each topic's `_promotion_drafts.yaml` becomes a per-topic editorial review.
   - Per topic: review drafts, fill `[NEEDS-DECISION]` fields, refine `[PROPOSED:]` descriptions, commit register additions.
   - Recommended order (highest-leverage first):

| topic | mentioned IDs | register target | est. commits |
|---|---|---|---|
| `06_mechanical_review_audit` | 27 | editorial_ledger, patch_register | 1–5 `[editorial]`/`[patch]`/`[compilation]` |
| `03_threadwork_design` | 19 | editorial_ledger, patch_register | 1–3 `[editorial]`/`[patch]`/`[compilation]` |
| `08_session_consolidation` | 7 | editorial_ledger, patch_register | 1–1 `[editorial]`/`[patch]`/`[compilation]` |
| `04_faction_balance_three_modes` | 3 | editorial_ledger, patch_register | 1–1 `[editorial]`/`[patch]`/`[compilation]` |
| `01_throughlines_meta` | 2 | editorial_ledger, patch_register | 1–1 `[editorial]`/`[patch]`/`[compilation]` |
| `09_canon_rectification_pp675_ed783` | 2 | editorial_ledger, patch_register | 1–1 `[editorial]`/`[patch]`/`[compilation]` |
| `10_session_log_index` | 2 | patch_register | 1–1 `[editorial]`/`[patch]`/`[compilation]` |

3. **Topic-by-topic content ingestion** (post-promotion):
   - Once IDs are promoted, atom-level content can flow into target design docs.
   - Solmund (02) is the gating editorial review — defer until you decide thematic block-by-block.
   - Topic 05 (v2 historicity) is mostly aligned — light verification pass into `designs/audit/`.
   - Topic 07 (audit s1-s7) is 2 atoms — fold into 08 or skip.
   - Topic 10 (session log index) is verification-only, no ingestion.

4. **Stage 5 — archive `atoms_pending/2026-04-25/`** when all topics resolved.

## Editorial decision points required (Stage 4 cannot proceed without these)

1. **Solmund block-level approval** — 6 thematic blocks (Di Cicco principle, voice registers, artifact taxonomy, philosophical frameworks, faction engagement pathways, mechanical audit). Approve / reject / modify each.
2. **Topic 06 sub-decomposition acceptance** — see `06_sub_decomposition.md`. Confirm the section-prefix split or propose alternative.
3. **ED-543 disposition** — register, strike, or replace with another ED.
4. **3 missing path resolutions** — per-path: rename, create, or strike atom references.
5. **Per-MENTIONED-ID** — fill `[NEEDS-DECISION]` fields in promotion drafts (severity, source, parent, etc.).
6. **Stage 5 archive strategy** — A (move), B (delete), C (front-matter status updates + retain). Choose at the end.

## Risk register (Stage 4 specific)

| id | risk | mitigation |
|---|---|---|
| S4-R1 | Promoting MENTIONED IDs without verifying their canon mentions are authoritative | Each draft includes `canon_mentions` field listing source paths; review each before promotion |
| S4-R2 | Topic 06 sub-decomposition leaves a sub-topic too small to audit usefully | Re-merge sub-topics with <5 atoms with adjacent ones at sub-decomposition apply time |
| S4-R3 | Solmund editorial deferred indefinitely, blocking archive | Time-box: if Solmund review not started in N sessions, archive Solmund atoms separately and continue without |
| S4-R4 | ED-543 registration without authoritative description | Forensic report shows atom contexts and any canon mentions; combine into description; if both empty, strike instead |
| S4-R5 | Editorial-gate hook blocks commits to designs/world/, designs/npcs/, etc. without [EDITORIAL: ED-NNN] markers | Every Solmund-ingest commit must carry the marker; Stage 1 plan already accounted for this |

## Outputs

- `_stage4_prep/06_sub_decomposition.md`
- `_stage4_prep/ed_543_forensic.md`
- `_stage4_prep/missing_paths_resolution.md`
- `_stage4_prep/promotion_drafts/<topic_id>_promotion_drafts.yaml` (one per topic with MENTIONED IDs)
- `_stage4_prep/stage4_workplan.md` — this document
