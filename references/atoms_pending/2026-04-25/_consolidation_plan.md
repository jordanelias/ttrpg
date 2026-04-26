# atoms_pending/2026-04-25 — Consolidation Plan (v1)

**Status:** PENDING JORDAN APPROVAL — do not execute until signed off.

**Inputs:** `_priority_queue.yaml`, `_id_clusters.yaml`, `_source_roadmap.yaml`
**Scope:** 316 atoms across 10 source masters; 26 cross-source ID clusters; 141 unique canonical IDs.

## Plan in one paragraph

Six stages. Stage 0 establishes ground truth (which IDs already exist). Stage 1 routes Solmund through Jordan editorial review (independent path). Stage 2 consolidates the 26 cross-source ID clusters — highest leverage, closes 4–9 atoms each. Stage 3 routes remaining mechanical atoms per source to their declared target paths. Stage 4 verifies audit/consolidation sources against canon (mostly should already be captured). Stage 5 reduces session-log atoms to ID-presence diffs (verification only, not ingestion). Stage 6 archives the staging folder. Stages 1 and 2 can run in parallel; 3–5 depend on 2; 6 closes everything.

## Dependency graph

```
Stage 0 ──┬──> Stage 2 (clusters) ──┬──> Stage 3 (mechanical)
          │                          ├──> Stage 4 (audit verify)
          │                          └──> Stage 5 (session diff)
          └──> Stage 1 (Solmund editorial — parallel, independent)
                                              │
                                              v
                                          Stage 6 (archive)
```

## ID inventory (Stage 0 input)

| kind | unique IDs | register target |
|---|---|---|
| ED | 71 | `canon/editorial_ledger.yaml` |
| M | 11 | `references/throughlines_meta.md` |
| PP | 37 | `canon/patch_register_active.yaml + patch_register_*_archive.yaml` |
| T | 21 | `references/throughlines_meta.md` |
| TC | 1 | `designs/provincial/ — disambiguate Theocracy Counter vs Conviction Track per occurrence` |

## Stage 0 — Pre-flight ID verification

**Goal:** For every canonical ID referenced across the 316 atoms, classify as known (in register) or unknown (needs new entry). Output drives the rest of the plan.

**Blocks:** all subsequent stages

**Actions:**
- Fetch canon/editorial_ledger.yaml; cross-check 71 unique ED-NNN; flag unknowns as new-registration candidates.
- Fetch canon/patch_register_active.yaml + archives via canon/patch_register_index.md; cross-check 37 unique PP-NNN.
- Fetch references/throughlines_meta.md; cross-check 21 T-NN and 11 M-NN; flag unknowns.
- Produce _id_verification_report.yaml: per-ID known/unknown/needs-update.

**Inputs (sample):**
- `_id_inventory.yaml`

**Expected commits:** 1 (`[infrastructure]` — verification report only)
**Jordan decision required:** no
**Estimated duration:** short — single fetch + comparison

## Stage 1 — Solmund editorial review

**Goal:** Solmund cultural guide is editorial-path content with [PROVISIONAL:] marker. Single editorial-block hand-off; no mechanical work until Jordan approves.

**Blocks:** all designs/world/ + designs/npcs/ work touching Solmund
**Parallel with:** Stage 2

**Actions:**
- Bundle all 32 solmund atoms (1 P2 + 4 P3 + 27 unscored) as a single editorial review document.
- Hand off to Jordan for line-level approve/reject/modify per cluster (Di Cicco principle, voice registers, faction pathways, etc.).
- On approval: route approved content to designs/world/, designs/npcs/ via [editorial] commits with [EDITORIAL: ED-NNN — description] markers.
- On rejection: archive rejected atoms; do not commit.

**Inputs (sample):**
- `solmund_master_document__25__22-faction-response-pathways (41 lines, signal=18)`
- `solmund_master_document__31__28-implementation-priorities (63 lines, signal=15)`
- `solmund_master_document__23__20-the-mechanism-rendered-world-change-event-rwce (30 lines, signal=12)`
- `solmund_master_document__29__26-system-connections (21 lines, signal=10)`
- `solmund_master_document__05__2-five-theological-poets-tonal-registers (36 lines, signal=8)`
- `... 27 more atoms in solmund_master_document/`

**Expected commits:** 0–6 depending on approval breadth (`[editorial]` per design doc updated)
**Jordan decision required:** **yes**
**Decision points:**
- Approve / reject / modify each thematic block (Di Cicco principle, voice registers, artifact taxonomy, philosophical frameworks, faction engagement pathways, mechanical audit).
- Confirm target paths within designs/world/ vs designs/npcs/.
**Estimated duration:** depends on Jordan availability — review block first, code work follows

## Stage 2 — Cross-source ID-cluster consolidation

**Goal:** For each canonical ID referenced by atoms across ≥2 sources, reconcile drift and update the register. This is the highest-leverage work because each consolidation closes 4-9 atoms at once.

**Blocks:** Stage 3 (mechanical ingestion may reference these IDs)

**Sub-stages:**
- **2a — Throughlines T-31..T-41 + meta-throughlines M-1..M-5 (cohesive block)**
  - cluster_ids: `T-36, M-4, T-31, M-3, M-1, T-34, T-32, T-35...`
  - cluster_count: 17
  - atom_count_in_clusters: 93
  - rationale: Throughline + meta-throughline structure is interrelated; partial consolidation would create register drift. Read all atoms in cluster, reconcile, update references/throughlines_meta.md as a single coherent commit.
  - expected_commits: 1–2 (`[editorial]` for ED markers + `[compilation]` for throughlines_meta)
- **2b — PP-675 canon rectification cluster**
  - cluster_ids: `PP-675`
  - rationale: PP-675 is referenced by 6 atoms across 3 sources (canon rectification patch). Verify it exists in patch_register_active.yaml; if so, update propagation_map; if not, register it.
  - expected_commits: 1 (`[patch]` if new) or 0 (if already complete)
- **2c — Other PP clusters**
  - cluster_ids: `PP-508, PP-674, PP-632`
  - rationale: PP-674, PP-540, PP-541, PP-508, PP-632 — each is a separate patch. Consolidate per-cluster into patch_register.
  - expected_commits: 3 (`[patch]` per cluster, only if new)
- **2d — ED-clusters (editorial decisions)**
  - cluster_ids: `ED-738, ED-664, ED-783, ED-665, ED-663`
  - cluster_count: 5
  - rationale: ED-738, ED-664, ED-665, ED-783, ED-663 — for each, verify ledger entry; reconcile cross-source drift if any.
  - expected_commits: 1–5 (`[editorial]` per ED needing update)

**Expected commits:** —
**Jordan decision required:** no
**Estimated duration:** medium — 26 cluster reads + register diffs

## Stage 3 — Per-source mechanical ingestion

**Goal:** Route the 39 P1/P2 atoms NOT covered by cross-source clusters and NOT in solmund/session-logs into their declared target design paths.

**Blocks:** Stage 6 archive
**Depends on:** Stage 2 (shared IDs reconciled first)

**Sub-stages:**
- **3a — VALORIA_SESSION_2026-04-25_MASTER.md → ['session_logs/ (most already captured)']**
  - source_file: VALORIA_SESSION_2026-04-25_MASTER.md
  - role: session_log
  - p1_p2_atom_count: 4
  - expected_commits: 1–2 (`[compilation]` design-doc updates)
- **3b — master_document_2026-04-25.md → ['designs/provincial/faction_*', 'designs/scene/*', 'canon/editorial_ledger.yaml']**
  - source_file: master_document_2026-04-25.md
  - role: mechanical_design
  - p1_p2_atom_count: 10
  - expected_commits: 1–2 (`[compilation]` design-doc updates)
- **3c — threadwork_master.md → ['designs/threadwork/threadwork_v30.md']**
  - source_file: threadwork_master.md
  - role: mechanical_design
  - p1_p2_atom_count: 2
  - expected_commits: 1–2 (`[compilation]` design-doc updates)
- **3d — valoria_master_document.md → ['designs/', 'canon/02_canon_constraints.md']**
  - source_file: valoria_master_document.md
  - role: mechanical_design
  - p1_p2_atom_count: 15
  - expected_commits: 1–3 (`[compilation]` design-doc updates)
- **3e — valoria_master_consolidation.md → ['canon/editorial_ledger.yaml', 'designs/']**
  - source_file: valoria_master_consolidation.md
  - role: consolidation
  - p1_p2_atom_count: 6
  - expected_commits: 1–2 (`[compilation]` design-doc updates)
- **3f — valoria_session_2026_04_25_master_consolidation.md → ['canon/patch_register*.yaml (PP-675)', 'canon/editorial_ledger.yaml (ED-783)']**
  - source_file: valoria_session_2026_04_25_master_consolidation.md
  - role: session_log
  - p1_p2_atom_count: 1
  - expected_commits: 1–2 (`[compilation]` design-doc updates)
- **3g — valoria_master_analysis.md → ['designs/audit/', 'canon/editorial_ledger.yaml']**
  - source_file: valoria_master_analysis.md
  - role: audit
  - p1_p2_atom_count: 1
  - expected_commits: 1–2 (`[compilation]` design-doc updates)

**Expected commits:** —
**Jordan decision required:** no
**Estimated duration:** long — atom-level review + target-path commits across 3-6 design files

## Stage 4 — Audit + consolidation source verification

**Goal:** For each P1/P2 atom in the audit and consolidation masters, verify the content is captured somewhere in canon. If missing, route to appropriate target.

**Blocks:** Stage 6 archive
**Depends on:** Stage 2 (most ED/PP/T/M references should be reconciled first)

**Actions:**
- For each P1/P2 atom in ['master_consolidation.md', 'valoria_master_consolidation.md', 'valoria_master_analysis.md'], cross-reference content claims against current canon state.
- Atoms whose content is fully captured: mark front-matter status=consolidated:verified-existing.
- Atoms with new claims: route to appropriate canon target via [editorial] or [compilation] commit.

**Expected commits:** variable — likely 0–5 depending on coverage gaps
**Jordan decision required:** no
**Estimated duration:** medium — verification-heavy

## Stage 5 — Session-log verification skim

**Goal:** Session logs contain index-of-decisions atoms (commit manifests, ED summaries). Treat as verification targets, NOT fresh content. For each ID listed, confirm it exists in the appropriate register.

**Blocks:** Stage 6 archive
**Depends on:** Stage 0 (verification report) + Stage 2 (clusters resolved)

**Actions:**
- For each of the 17 P1/P2 session-log atoms, run an ID-presence check against the verification report from Stage 0.
- Report any IDs listed in session logs but missing from registers — these are the only items requiring action.
- Other session-log content: archive without ingestion (already in commit history).

**Expected commits:** 0–3 (`[editorial]` or `[patch]` for any missing IDs)
**Jordan decision required:** no
**Estimated duration:** short — automated ID diff

## Stage 6 — Archive atoms_pending

**Goal:** Once all atoms are either consolidated or verified-skip, mark the staging folder closed.

**Depends on:** Stages 1–5 complete

**Expected commits:** 1 (`[infrastructure]` archive move)
**Jordan decision required:** **yes**
**Decision points:**
- Choose archive strategy A/B/C.
**Estimated duration:** short

## Risk register

| id | risk | mitigation |
|---|---|---|
| R1 | Editorial-path commits without proper [EDITORIAL: ED-NNN] marker | editorial_gate hook blocks commits to designs/npcs/, designs/world/, designs/arcs/gm_ref/, canon/03_ without markers. Plan honors hook by gating Solmund through Stage 1 review. |
| R2 | Stale references_propagation when patch_register changes without propagation_map co-file update | Hook enforces patch_register writes to include propagation_map.md. Plan flags PP-cluster sub-stages as patch+propagation co-commits. |
| R3 | Throughline drift if T-31..T-41 consolidated piecemeal across multiple commits | Stage 2a treats throughline+meta-throughline as a single cohesive block. Single commit covering all T-NN/M-NN updates to throughlines_meta.md. |
| R4 | TC/CP/TD disambiguation ambiguity (943 TC occurrences, ~149 CP/TD per current next_action) | Out of scope for this plan — already a tracked next_action. Stage 3 may surface additional instances; flag them for the disambiguation pass rather than resolving here. |
| R5 | Session-log P1 atoms (commit manifests) misread as fresh content | Caveat in _prioritization.md flags this. Stage 5 explicitly treats session-log P1 as verification targets, not ingestion targets. |
| R6 | Solmund review block exceeds Jordan reviewable size in single pass | Stage 1 allows splitting solmund into thematic blocks (Di Cicco principle, voice registers, etc.) for incremental review. |
| R7 | Provenance loss if atoms_pending deleted before consolidation status fully tracked | Stage 6 Option C (front-matter status updates) preserves traceability. Recommend C unless storage/cleanliness is the priority. |

## Effort estimate

- **Commit count:** min 14 / expected 31 / max 57
- **Sessions needed:** 3–5 separate Claude sessions; bootstrap+context budget per session limits atom batch size

| stage | token envelope |
|---|---|
| 0 | small (<5k) — small register fetches + diff |
| 1 | medium (10–30k) — 32 solmund atoms + design doc reads |
| 2 | large (40–80k) — cluster reads across 26 clusters |
| 3 | large (40–80k) — per-source mechanical work |
| 4 | medium (15–30k) — verification-heavy |
| 5 | small (<10k) — automated ID diff |
| 6 | small (<5k) — archive move |

## Definition of done per stage

- **Stage 0:** Verification report committed; no IDs unaccounted for.
- **Stage 1:** All 32 solmund atoms either committed to designs/world/ + designs/npcs/ with [EDITORIAL] markers, or marked rejected.
- **Stage 2:** All 26 cross-source ID clusters reconciled into their target registers; cluster atoms marked status=consolidated.
- **Stage 3:** All P1/P2 atoms in mechanical sources committed to their declared target areas or marked verified-existing.
- **Stage 4:** All P1/P2 atoms in audit/consolidation sources verified against canon; gaps closed.
- **Stage 5:** All session-log P1/P2 atoms reduced to ID-presence diff; any missing IDs registered.
- **Stage 6:** atoms_pending/2026-04-25 archived per chosen strategy; folder closed.

## Decision points requiring Jordan input

1. **Stage 1 — Solmund:** Approve / reject / modify by thematic block (Di Cicco principle, voice registers, artifact taxonomy, philosophical frameworks, faction engagement pathways, mechanical audit). Confirm target paths within `designs/world/` vs `designs/npcs/`.
2. **Stage 6 — archive strategy:** Choose A (move to `atom_archive/`), B (delete), or C (front-matter status updates + retain).
3. **Plan approval before any execution.** Stage 0 itself is fetch-only (no canon writes) — could begin once approved without further sign-off.

## Outputs from this planning step

- `_consolidation_plan.md` — this document.
- `_consolidation_workplan.yaml` — machine-readable workplan with full stage detail.
- `_id_inventory.yaml` — flat inventory of all canonical IDs across atoms; feeds Stage 0.
