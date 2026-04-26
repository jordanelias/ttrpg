# atoms_pending/2026-04-25 — Consolidation Plan (v2)

**Status:** PENDING JORDAN APPROVAL — do not execute until signed off.

## Correction from v1

v1 (commit `e9a1c9c3`) treated consolidation as canon dispersal — atoms ingested into existing canon registers (`editorial_ledger.yaml`, `patch_register_active.yaml`, `designs/`, etc.). This was a misread of intent.

**v2 reframe:** Consolidation = assembly of atoms into their own topical documents. Each consolidated document is an audit subject. Canon ingestion is a separate, post-audit decision (Stage 4, out of scope here).

## Plan in one paragraph

316 atoms decompose into **10 topics** — each becoming one consolidated document at `_consolidated/<topic_id>.md`. Topics align with cross-source ID clusters (throughlines, PP-675) plus per-source coherent bodies (Solmund, threadwork, faction balance, etc.). Stage 1 = approve decomposition. Stage 2 = produce 10 consolidated docs. Stage 3 = audit each doc against its checklist (output: 10 audit reports). Stage 4 = post-audit canon decisions (separate plan, not assembled here). Stage 5 = archive workspace.

## Why this is different from v1

| dimension | v1 (incorrect) | v2 (corrected) |
|---|---|---|
| consolidation target | existing canon files | new docs at `_consolidated/<topic>.md` |
| audit timing | implicit during ingestion | explicit Stage 3 against assembled docs |
| canon mutations | mixed in throughout | deferred to separate post-audit plan |
| Solmund handling | route to designs/world/ + designs/npcs/ during Stage 1 | becomes one consolidated doc; canon route is post-audit |
| reviewable artifact | spread across 30+ commits | 10 consolidated docs + 10 audit reports |

## Topic decomposition

All 316 atoms assigned to exactly one topic via strict sequential assignment (zero-overlap, zero-orphan).

| topic | scope summary | atoms | drift surface | post-audit canon target |
|---|---|---|---|---|
| `01_throughlines_meta` | Throughlines T-31..T-41 + Meta-throughlines M-1..M-5 (consol | 22 | cross-source | references/throughlines_meta.md |
| `02_solmund_cultural_guide` | Solmund Cultural Guide (consolidated) | 32 | single-source | designs/world/, designs/npcs/ — pending Jordan edi |
| `03_threadwork_design` | Threadwork Design Synthesis (consolidated) | 71 | cross-source | designs/threadwork/threadwork_v30.md |
| `04_faction_balance_three_modes` | Faction Balance & Three-Mode Architecture (consolidated) | 50 | cross-source | designs/provincial/faction_*, simulations/ |
| `05_v2_historicity_correction` | v2 Historicity Correction (Three Kingdoms / Sengoku) (consol | 9 | single-source | designs/audit/ |
| `06_mechanical_review_audit` | Mechanical Review & Audit Record (consolidated) | 83 | cross-source | designs/ (multiple subpaths) — likely sub-decompos |
| `07_audit_s1_s7_synthesis` | Rigorous Audit S1-S7 Synthesis (consolidated) | 2 | single-source | canon/editorial_ledger.yaml (verification only) —  |
| `08_session_consolidation` | Session Consolidation 2026-04-25 (consolidated) | 19 | single-source | canon/editorial_ledger.yaml (verification) + desig |
| `09_canon_rectification_pp675_ed783` | Canon Rectification PP-675 / ED-783 (consolidated) | 18 | cross-source | canon/patch_register_active.yaml (verify), canon/e |
| `10_session_log_index` | Session Log Index 2026-04-25 (consolidated) | 10 | cross-source | No content ingestion — verification report only. I |

## Per-topic detail

### `01_throughlines_meta` — Throughlines T-31..T-41 + Meta-throughlines M-1..M-5 (consolidated)

- **scope:** All atom content across sources discussing T-NN/M-NN throughlines. Reconciles drift between master_consolidation §3/§4, valoria_master_document §19.3/§19.4, valoria_master_analysis §7/§8, master_document_2026-04-25 §7.
- **atoms:** 22
- **drift dimensions:**
  - Per-throughline definition wording: master_consolidation may state T-31 differently than valoria_master_analysis.
  - Numbering range: §3 says "T-31..T-41" but some sources reference T-26..T-41 — check coverage gap.
  - Meta-throughline range: master_consolidation §4 says М-7..М-11; valoria_master_consolidation references М-1..М-5. Possibly two different numbering schemes (Cyrillic vs Latin) or two distinct generations. Critical to disambiguate.
  - ED-738 (Ein Sof gradient) anchors throughline interpretation — verify same anchor across sources.
- **audit checks:**
  - Each T-NN appears with a single canonical definition.
  - M-NN numbering scheme is unified (or explicit dual-scheme convention documented).
  - Coverage from T-26 through T-41 verified — no missing IDs.
  - Cross-references to references/throughlines_meta.md are consistent.
- **post-audit canon target:** `references/throughlines_meta.md`

### `02_solmund_cultural_guide` — Solmund Cultural Guide (consolidated)

- **scope:** All 32 solmund_master_document atoms. Editorial-path content; remains [PROVISIONAL:] until Jordan editorial review.
- **atoms:** 32
- **drift dimensions:**
  - Internal only — single source.
- **audit checks:**
  - Internal consistency across Di Cicco principle, voice registers, artifact taxonomy, philosophical frameworks, faction engagement pathways, mechanical audit sections.
  - Cross-references to existing canon (canon/00_philosophical_foundations.md, canon/02_canon_constraints.md, designs/world/worldbuilding_v30.md, etc.) are valid.
  - Mechanical audit section claims (Faction Response Pathways, Miraculous Event) consistent with current designs/.
  - [PROVISIONAL:] / [EDITORIAL:] markers correctly applied per editorial-path rules.
  - No setting/worldbuilding contradictions with existing canon/03_canonical_timeline.md.
- **post-audit canon target:** `designs/world/, designs/npcs/ — pending Jordan editorial review`

### `03_threadwork_design` — Threadwork Design Synthesis (consolidated)

- **scope:** All threadwork_master atoms plus cross-source atoms with threadwork target. Single coherent design synthesis covering substrate language, player feel, system stories, mechanics.
- **atoms:** 71
- **drift dimensions:**
  - Substrate-origin framing (radically unknowable) — verify same framing across atoms.
  - Player-feel claims — check no contradictions.
  - Mechanical specs that pull from valoria_master_document/master_consolidation may be paraphrased differently.
- **audit checks:**
  - Foundational stance is consistent.
  - Three player stories the system produces are listed once authoritatively.
  - Mechanical specifications (when present) match designs/threadwork/threadwork_v30.md.
  - No contradiction between threadwork_master.md framings and master_consolidation §6 (Mechanical Specifications) framings.
- **post-audit canon target:** `designs/threadwork/threadwork_v30.md`

### `04_faction_balance_three_modes` — Faction Balance & Three-Mode Architecture (consolidated)

- **scope:** master_document_2026-04-25.md + PP-540/541 simulation atoms. Three-mode emotional-engagement architecture; Monte Carlo balance findings.
- **atoms:** 50
- **drift dimensions:**
  - P1 vs P2 vs P3 framing of three-mode importance — check no priority disagreement.
  - PP-540/541 simulation result interpretations across sources.
  - Faction-balance audit findings vs holistic audit findings — possible drift.
- **audit checks:**
  - Three-mode architecture is described once authoritatively.
  - Simulation methodology and result claims are reproducible (params/inputs documented).
  - §6.5 framework propagation gaps are real gaps, not artifacts of partial source views.
  - Companion-deliverable references (`faction_balance_audit_2026-04-25.md`, `balance_simulation_report_2026-04-25.md`, etc.) point to actual files in the repo.
- **post-audit canon target:** `designs/provincial/faction_*, simulations/`

### `05_v2_historicity_correction` — v2 Historicity Correction (Three Kingdoms / Sengoku) (consolidated)

- **scope:** valoria_master_analysis.md atoms not already in throughline cluster. v2 cross-lens audit Parts B (Three Kingdoms) and C (Sengoku); 5-tier factual audit; 54-proposal N-check.
- **atoms:** 9
- **drift dimensions:**
  - Internal only — single source.
- **audit checks:**
  - All 5 audit tiers are described once.
  - All 54 proposal N-check entries are present and individually auditable.
  - Cross-references to designs/audit/ files are valid.
  - Historicity claims (e.g., Three Kingdoms / Sengoku) are documented with sources.
- **post-audit canon target:** `designs/audit/`

### `06_mechanical_review_audit` — Mechanical Review & Audit Record (consolidated)

- **scope:** valoria_master_document.md atoms not already pulled by other topics. Master mechanical-review record covering die/TN/wager/conviction/scale-transition/etc. Likely candidate for sub-decomposition during execution if 100+ atoms remain.
- **atoms:** 83
- **drift dimensions:**
  - High volume — may contain internal redundancy that becomes apparent only after consolidation.
  - Section numbering (1.x, 19.x) may need re-anchoring against existing designs/.
- **audit checks:**
  - Sections are non-overlapping or overlap is justified.
  - Mechanical specs match existing designs/ where applicable; new specs are flagged.
  - No internal contradictions across sections.
  - Open Decisions Requiring Jordan (II.2) listed as decision points, not as resolved.
- **post-audit canon target:** `designs/ (multiple subpaths) — likely sub-decompose during consolidation`

### `07_audit_s1_s7_synthesis` — Rigorous Audit S1-S7 Synthesis (consolidated)

- **scope:** master_consolidation.md atoms not already in throughline cluster. Synthesis of multi-stage audit work 2026-04-21/22. Mostly metadata/framework; high ED-738 density.
- **atoms:** 2
- **drift dimensions:**
  - Internal only — single source.
- **audit checks:**
  - Wave 1 workplans match what actually got committed (cross-check against commit history).
  - Open editorial decisions list reconciled against current canon/editorial_ledger.yaml.
  - Methodological notes are consistent.
  - "What this consolidation is not" disclaimers preserved (do not over-canonize).
- **post-audit canon target:** `canon/editorial_ledger.yaml (verification only) — most content already in commit history`

### `08_session_consolidation` — Session Consolidation 2026-04-25 (consolidated)

- **scope:** valoria_master_consolidation.md atoms not in throughline cluster. Full-session synthesis (assessment → critique → foundations → reframing → grounding → methodology).
- **atoms:** 19
- **drift dimensions:**
  - Internal only — single source.
- **audit checks:**
  - Phase narrative (assessment → critique → ...) is coherent.
  - Recent canonical strikes (§2.4) cross-checked against actual commits.
  - Bridge-work claims (§2.1) cross-checked against current state.
  - Scale Transitions Zoom-In trigger families (§2.2) match current designs/.
- **post-audit canon target:** `canon/editorial_ledger.yaml (verification) + designs/ (specific corrections only)`

### `09_canon_rectification_pp675_ed783` — Canon Rectification PP-675 / ED-783 (consolidated)

- **scope:** valoria_session_2026_04_25_master_consolidation.md + cross-source PP-675 atoms. Censured-vocabulary / term-governance work.
- **atoms:** 18
- **drift dimensions:**
  - PP-675 description across 3 sources may use different framings.
  - ED-783 framing (term governance vs vocabulary censuring vs canon rectification) — pick one.
- **audit checks:**
  - PP-675 final spec matches whatever landed in canon/patch_register_active.yaml.
  - ED-783 statement matches canon/editorial_ledger.yaml.
  - Outstanding Work (§10) cross-checked against current next_action queue.
  - Censured Vocabulary list (§2) is the authoritative one.
- **post-audit canon target:** `canon/patch_register_active.yaml (verify), canon/editorial_ledger.yaml (verify), references/propagation_map.md`

### `10_session_log_index` — Session Log Index 2026-04-25 (consolidated)

- **scope:** VALORIA_SESSION_2026-04-25_MASTER.md + valoria_session_master_2026-04-25.md atoms. Index-style consolidated doc — collapses 16 atoms into a single ED/PP coverage report. Most content already in commit history.
- **atoms:** 10
- **drift dimensions:**
  - ED-739 through ED-784 listed in VALORIA_SESSION master vs Sessions B/C/ED-717 in valoria_session_master — different ED ranges from different session phases.
  - Commit-manifest atom may double-count commits also captured in valoria_session_2026_04_25_master_consolidation (canon rectification commits).
- **audit checks:**
  - Every ED listed in commit-manifest atoms exists in canon/editorial_ledger.yaml.
  - Every PP listed exists in canon/patch_register_active.yaml or an archive.
  - Stress-test results (Section 4) referenced from session-log atoms point at simulations/ files that exist.
  - P1 resolutions claimed are reflected in current p1_blocker_count.
- **post-audit canon target:** `No content ingestion — verification report only. Index doc itself archives with the session.`

## Stages

### Stage 1 — Topic decomposition approval
- **goal:** Jordan reviews the 10-topic decomposition. Approve / merge / split topics before document assembly begins.
- **Jordan decision required:** **yes**
- **expected commits:** 0 (pure review) or 1 (`[infrastructure]` decomposition revision)
- **duration:** short — 15–30 min review

### Stage 2 — Document assembly
- **goal:** Produce 10 consolidated documents at references/atoms_pending/2026-04-25/_consolidated/<topic_id>.md. Each doc = atoms reassembled into coherent prose with: front-matter (source atoms list, drift dimensions, audit checklist), main content (cross-source merge), provenance footer.
- **sub-steps:**
  - For each topic, read all assigned atoms.
  - Cross-source clusters: produce drift-table appendix showing per-source phrasing.
  - Single-source topics: stitch atoms back in section_index order, dedupe redundancies.
  - Apply [PROVISIONAL:] / [EDITORIAL:] markers to topics 02 (Solmund) per editorial-path rules.
  - Generate audit checklist appendix per topic (drawn from _topic_decomposition.yaml audit_checks).
- **Jordan decision required:** no
- **expected commits:** 10 (`[infrastructure]` per consolidated doc) — bundle 2-3 per commit if compatible
- **duration:** long — atom-merge + drift-reconciliation per topic

### Stage 3 — Audit pass per consolidated document
- **goal:** Each consolidated doc audited against its checklist + against current canon. Audit produces a report (not a canon mutation).
- **sub-steps:**
  - Stage 0 ID-presence check feeds audit (which IDs already in registers, which are new).
  - Per-topic audit report at _audit_reports/<topic_id>_audit.md.
  - Audit reports summarize: drift findings, gaps vs canon, claim-validity, recommendation (canon-ingest / archive / reject / split).
- **Jordan decision required:** **yes**
- **expected commits:** 10 (`[simulation]` or `[infrastructure]` per audit report)
- **duration:** medium — checklist-driven; some topics need canon fetches

### Stage 4 — Post-audit canon decisions
- **goal:** Based on audit reports, decide per topic: ingest into canon (and where), archive without ingestion, or reject. THIS stage is what my v1 plan incorrectly put first.
- **Jordan decision required:** **yes**
- **expected commits:** 0–N (variable per topic; some topics will produce multiple downstream commits, others zero)
- **duration:** variable — depends on audit findings
- **note:** Stage 4 is OUT OF SCOPE for the consolidation+audit plan. It will be planned separately once audit reports exist.

### Stage 5 — Archive consolidation workspace
- **goal:** Move references/atoms_pending/2026-04-25/ → references/atom_archive/2026-04-25/. Consolidated docs and audit reports preserved with provenance trail.
- **Jordan decision required:** **yes**
- **expected commits:** 1 (`[infrastructure]` archive move)
- **duration:** short

## Risk register

| id | risk | mitigation |
|---|---|---|
| R1 | Topic decomposition assigns one atom to multiple topics → duplicate content in consolidated docs | Each atom assigned to exactly one topic (verified zero-overlap). Cross-source ID-cluster atoms placed in cluster topic; same atom does NOT also appear in source topic. |
| R2 | Solmund topic (02) crosses editorial paths during assembly without [PROVISIONAL:] markers | Topic 02 is the sole editorial-path topic. Front-matter MUST carry [PROVISIONAL:]; editorial_gate hook will block otherwise. |
| R3 | Topic 06 (mechanical review) becomes too large to audit as single document | 125-atom topic explicitly flagged for sub-decomposition during Stage 2 if assembled doc exceeds reviewable size (e.g., 8k+ tokens). Sub-split by section family (1.x die mechanics / 4.x conviction / 19.x throughline-anchored / etc.). |
| R4 | Cross-source drift goes unrecorded if assembly silently picks one phrasing | Drift-table appendix is mandatory for every cross-source topic (01, 03, 04, 09). Per-source phrasing preserved verbatim alongside merged statement. |
| R5 | Audit reports treated as canon decisions (skipping Stage 4 review) | Audit reports are FINDINGS, not actions. Each report's "recommendation" field is advisory. Stage 4 is a separate, future plan. Document this clearly in the audit report template. |
| R6 | Atoms unassigned (orphaned) | Coverage check at decomposition time: 0 unassigned. All atoms assigned. |
| R7 | Topic 10 (session log index) over-summarizes commit history that's already authoritative | Topic 10 explicitly produces an INDEX (ED/PP coverage report), not a re-statement of commit content. Output is a verification table, not prose. |

## Decision points requiring Jordan input

1. **Stage 1 — topic decomposition approval.** 10 topics as defined above. Approve, merge, split, or rename. Particular attention to: topic 06 (mechanical review, 125-ish atoms — possibly sub-decompose now); topic 02 (Solmund — confirm [PROVISIONAL:] handling).
2. **Stage 3 — audit framing per topic.** For editorial-path topics (02 Solmund), Jordan needs to drive audit conclusions. Mechanical topics can be Claude-led with Jordan review at end.
3. **Stage 5 — archive strategy** (defer until Stages 1–4 complete).
4. **Stage 4 (post-audit canon decisions) is OUT OF SCOPE.** Will be planned separately once audit reports exist. Confirm this scope boundary.

## Outputs from this planning step

- `_consolidation_plan.md` — this document (overwrites v1).
- `_consolidation_workplan.yaml` — machine-readable workplan v2 (overwrites v1).
- `_topic_decomposition.yaml` — definitive atom-to-document mapping.
- `_id_inventory.yaml` — retained from v1; still feeds Stage 3 audit pass.
