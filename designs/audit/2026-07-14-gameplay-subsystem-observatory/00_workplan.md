# 00 · Workplan & Run Configuration

## Status: FILED — 2026-07-14 · ED-IN-0064

## Scope

Run the vector-audit family over the working tree and, **for each gameplay subsystem**, produce inventory → shape
of code architecture → connectivity → gaps, as a graph, plus a six-directional coverage check and a per-subsystem
discussion/solutions piece. Subsystem set: the **16 player-facing gameplay modules** (personal_combat,
social_contest, mass_battle, threadwork, fieldwork_knots, domain_actions, faction_state, faction_politics,
ci_political, territorial_piety, settlement_layer, peninsular_strain, npc_behavior, piety_track, miraculous_event,
victory) + `settlement_economy` as a degenerate 17th; the 11 infrastructure modules appear as connectivity context.

## Pre-committed thresholds (LOCKED — no post-hoc tuning; SKILL.md §3.7)

| Parameter | Value |
|---|---|
| Corpus scope | full design + foundation (working tree; L0 `_canonical_paths()`) |
| Token list | seed (canonical_sources + named NPCs) + auto-extract (≥3 docs, ≥10 mentions) |
| Disambiguation | enabled |
| Diagnostics | all 8 modes (A–H) |
| Validation gate | structural properties P1/P2/P3 — 2/3 to publish as authoritative |
| Implicit-citation threshold | ≥ 2 body mentions |
| Random seed | 42 |
| Connectivity ground-truth | fresh `structure_audit` L2/G_code (NOT the committed, stale `tools/observability/graph.json`) |

**These were fixed before running.** The gate returned **FAILED (1/3)** — reported up-front, not tuned around
(that failure is itself a finding, GAP-H4). A failed gate downgrades all findings to **leads, not verdicts**;
that framing is carried through every deliverable.

## Run commands (working tree, from repo root)

```
python3 skills/valoria-vector-audit/scripts/vector_audit.py    --repo-root . --output-dir <DIR>/vector_audit
python3 skills/valoria-vector-audit/scripts/structure_audit.py --repo-root . --output-dir <DIR>/structure
python3 skills/valoria-vector-audit/scripts/pointer_audit.py   --repo-root . --output-dir <DIR>/structure
python3 skills/valoria-vector-audit/scripts/formula_audit.py   --repo-root . --output-dir <DIR>/structure
python3 skills/valoria-vector-audit/scripts/gen_audit.py       --repo-root . --output-dir <DIR>/structure
python3 skills/valoria-module-adjudicator/scripts/contract_flowchart.py \
  --contracts references/module_contracts.yaml --registry designs/architecture/key_type_registry_v30.md \
  --outdir <DIR>/graphs
```
`<DIR>` = `designs/audit/2026-07-14-gameplay-subsystem-observatory`. All exited 0.

## Vetting (Class A — analytic instrument, self-exempting)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: []
  m_ratings:
    M-1:  "○"
    M-2:  "○"
    M-3:  "○"
    M-4:  "○"
    M-5:  "○"
    M-6:  "○"
    M-7:  "○"
    M-8:  "○"
    M-9:  "○"
    M-10: "○"
    M-11: "○"
  q: pass
  note: "Multi-graph triangulation + G_code/L2 architecture audit; analytic instrument, self-exempting.
         The exemption covers the INSTRUMENT only — any fix it proposes goes through normal vetting."
```

## Disposition discipline (forward-only)

Every finding resolves to a filed `ED-<LANE>-NNNN` or an explicit no-action line (see `subsystem_synthesis_v1.md`
§7 + `gap_register_v1.md`). This docket = **ED-IN-0064**. Known no-actions: GAP-C1 (ED-MB-0010), GAP-C2, GAP-H8
(ED-SE-0045), the annotation-debt seams. New leads handed to lanes (HELD-BACK, needs_jordan): GAP-C4 (env.crisis
consumer → WR), GAP-DIR-1 (first diagonal exemplar → WR/cross_scale), GAP-DIR-2/3 (uncalled resolvers → FA/SC),
GAP-H5 (CLAUDE.md §6 count refresh → IN). Fixed this run: OBS-IN-1 (duplicate `IN:` key in id_reservations).
