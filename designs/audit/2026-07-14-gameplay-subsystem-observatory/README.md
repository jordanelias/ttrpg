# Gameplay-Subsystem Observatory — architecture, connectivity & gaps

## Status: FILED — 2026-07-14 · Lane: IN (cross-cutting) · ED-IN-0064

> **Analytic instrument (FILED), PROPOSED fixes HELD-BACK.** This docket *indexes and graphs* the live corpus —
> per gameplay subsystem: inventory → shape of code architecture → connectivity → gaps, plus a directional
> ("all directions") coverage pass. It flips **no** `## Status:` line, wires **no** inert field, and authors **no**
> fix into canon. Every fix is held back to its lane (ED-1094). **Leads, not verdicts:** the L0 `vector_audit`
> validation gate **FAILED 1/3** (a real corpus finding — the 7 Convictions' throughline isolation). Self-exempting
> on Ω/Μ vetting (Class A) — see `00_workplan.md`.

Jordan-requested, 2026-07-14: *"run vector audit … for each subsystem used in gameplay, inventory and graph
accordingly to identify shape of code architecture followed by connectivity and gaps,"* then *"double check in all
directions"* and *"provide an explanation/discussion piece for each subsystem … where the gaps are and what
solutions exist."*

## Manifest

| File | Contents |
|---|---|
| `README.md` | This index. |
| `00_workplan.md` | Run config + **pre-committed thresholds (LOCKED)** + the Class-A vetting block. |
| `01_methodology.md` | Executed parameters; what changed vs the 2026-04-29 baseline; numpy/sklearn-absent + coverage disclosures; the two-gate verification. |
| **`remediation_plan_v1.md`** | **The resolution program (ED-IN-0066, structure ratified via PR #140; hardened post-merge by the Fable review)** — phases sequencing every finding (incl. PR #139's) to EXECUTED/RULED/CLASSIFIED: instrument hardening → decision docket D1–D16 (Class E explicit-pick vs Class R ratify-by-merge) → CTC sweep → flag-gated wiring → hub grounding → **P5† conditional** Field/Gauge keystone → certification rerun. Leads with "Jordan's 20-minute version" (5 critical rulings). |
| **`fable_review_v1.md`** | **The Fable review, run at Jordan's instruction before finalizing next steps** — direct top-tier pass over this session's outputs + PR #139: P5 demoted to conditional (it un-deferred a standing ruling), the docket split R/E, P4.3 re-scoped to dispositions, the three-band pointer meter, and the verdicts on #139 (Meter-1 adopted with a disposition refinement; its NS3-dam claim not inherited). **Errata:** the frozen run artifacts in this docket (`structure/pointer_register.md`, the nexus HTML chips) predate PR #139's meter relabeling — read "52.7% resolved" as *matched*, not keyed; the P6 rerun regenerates them on the corrected scripts. |
| **`unification_v1.md`** | **The capstone** — one synthesis across the whole docket: the single thesis, the four cuts as one picture, the three loci where all correctness concentrates, the genuine-vs-CTC surface, the epistemic status (three confidence tiers + the five-pass hardening history), and the prioritized action surface. Read this first for the through-line. |
| **`subsystem_synthesis_v1.md`** | **The primary deliverable** — the master graph, 5 Mermaid cuts, 16 per-subsystem sections (inventory/shape/connectivity/gaps), cross-cutting findings, the §8 directional double-check, and the forward-only disposition table. |
| **`subsystem_discussion_v1.md`** | **Per-subsystem discussion/solutions piece** (Jordan's 2nd ask) — readable prose per subsystem: where the gaps are and what solutions exist, typed CTC vs GENUINE with the backing canon/code. |
| **`directional_coverage_v1.md`** | **The "all directions" deep-dive** (Jordan's 3rd ask) — each of the 6 (+temporal) delivery directions in detail, the 16×6 matrix, seam reconciliation, and the solutions roadmap. |
| **`cross_scale_value_architecture_v1.md`** | **Three-axis architecture discussion** (Jordan's 4th ask) — (1) wrappers/engines/modules/adapters, (2) keys/schema/I-O location + transport across scales, (3) aggregation/differentiation + weight escalation/de-escalation across scales (managing the context of content). |
| `gap_register_v1.md` | Two-tier `[COMPLETE-THE-CHAIN]`/`[GENUINE]` classification, evidence-cited (`code:`/`doc:`/`audit:`/`ledger:`), keyed to graph edges + the 5 `GAP-DIR` directional gaps. |
| `adversarial_review_v1.md` | The two independent read-only gates: the refute-by-default critic (**SOUND-WITH-FIXES**, 2 reclassifications) + the six-directional verifier. **Authoritative correction layer.** |
| `subsystem_nexus_artifact.html` | Self-contained interactive graph (pan/zoom, filter by family / edge-status / **direction** / flag; click node or edge; light+dark). Also published as an Artifact. |
| `vector_audit/` | Verbatim `vector_audit.py` output — `02_weakness_register.md`, `03_validation_report.md`, `data/*.json`. |
| `structure/` | Verbatim `structure_audit.py` (+ pointer/formula/gen) output — the G_code + L2 connectivity ground-truth. |
| `graphs/` | Verbatim `contract_flowchart.py` output — `module_flowchart.mermaid`, `state_graph.mermaid`, `module_map_flat.md`. **REGENERATE, never hand-edit.** |

## Headline results (fresh; supersede the stale prose in CLAUDE.md §6)

- **27 modules**, 99 raw / 43 simple wiring edges, 2 L2 cycles, **9 `doc:null`** (not 10), **13 `[ASSUMPTION]`**,
  4 dangling emits, 0 phantom producers. G_code: 173 modules, 268 imports, 3 cycles, 14 cut-vertices.
- **Two hubs carry the world:** `faction_state` (in-13) + `npc_behavior` (in-12), both L2 cut-vertices, both
  `[ASSUMPTION]`-resolver — the highest-leverage grounding target.
- **The "all directions" verdict:** of 7 directions, **2 are live end-to-end** (lateral + bottom-up Domain-Echo
  core), **2 are honest annotation-debt** (the down-seams), **3 hide a genuine gap** — diagonal has *zero
  executable instances*, Accord-echo/territory-transfer are *built-but-uncalled*, temporal `decay()` is *deferred*.
- **The genuine-mechanism surface is small:** after the adversarial gate corrected `MS`-owner and `engine_clock` to
  complete-the-chain, essentially one clean genuine build remains — the **first `causes[]` diagonal exemplar**.

## Provenance

Generated 2026-07-14 by the `valoria-vector-audit` skill's five observatory scripts + `contract_flowchart.py`,
run against the working tree (numpy/sklearn absent → L0 TF-IDF skipped; multi-graph core + 8 modes + P1/P2/P3 ran).
Synthesis fanned out under CLAUDE.md §10 tiering (Sonnet explorers → Opus synthesis + two Opus adversarial gates).
Clears the vector-audit staleness (was #1 stalest family, 305 files since the 2026-04-29 baseline).
`ED-IN-0064` allocated from `references/id_reservations.yaml` (IN `next_free` 64→65, co-committed — which also
repaired a duplicate `IN:` mapping key, finding OBS-IN-1).
