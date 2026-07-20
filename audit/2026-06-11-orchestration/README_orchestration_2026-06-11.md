# Orchestration deliverable set — 2026-06-11

**Architecture: one register, three views.** `valoria_master_workplan_v4.md` holds the single unified open register (§2, 28 rows) and the extended decision docket (§3, J-1…J-34). The map and graph are navigation/edge views that point into it by row number and J-key — no defect is tracked twice.

| File | Role |
|---|---|
| `valoria_master_workplan_v4.md` | The working master: reconciliation record (§0, incl. two unresolved value flags), operating model, unified register, docket, lane queues A/B/C, sequencing |
| `valoria_authoritative_map_v1.md` | Navigation surface: document-authority table (§1 — which file is live, for what), governance/canon/mechanics layers, 27-module status, canon↔mechanics spine |
| `valoria_authoritative_graph_v1.md` | Edge layer: nodes, edges by the six canonical directions, quantity lattice, loop inventory (inherited verdicts labelled), coverage verdict |
| `valoria_authoritative_graph.mermaid` | Rendered topology: scales × status-coded modules × direction-typed edges × the 8 J-1 seams × the CI→IP valve |
| `valoria_decision_unblock_graph.mermaid` | Rendered docket DAG: what each Jordan ruling opens, in leverage order |

**Supersession (precise, per atlas R3):** workplan **v4 supersedes v3 — on commit only**; until committed it is the working proposal, and v3 remains the committed master. The map and graph **supersede nothing** — they are synthesis layers over complementary live sources (master v1, atlas v1, canon flatten v2, game-flow v2, per-system set), all of which stay authoritative for their own depth.

**Provenance / landing:** built from the 2026-06-11 upload corpus, then **bootstrapped and verified at commit against live HEAD `d010fe27`** — editorial ledger 653 entries / 0 duplicate IDs; the v2 source layer (canon flatten · interdependency master/atlas · game-flow) confirmed committed. **Landed under `designs/audit/2026-06-11-orchestration/`; v3 bannered as superseded; `lane_assignments.yaml` `source:` repointed to v4 — this commit.** The two value flags (seed-CI 22-vs-28; MS-start "80→60" referent, commit `2edf6432`) remain **OPEN** — Jordan/investigation items, not resolved here. All content PROPOSED and Jordan-vetoable in the sense fixed this session: **authoritative and primary** (the governing surface of open work), not resolved-and-settled; docket §3 is the veto surface; no ED IDs assigned.
