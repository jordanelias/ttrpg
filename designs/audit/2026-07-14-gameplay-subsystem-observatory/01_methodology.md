# 01 · Methodology — Executed Parameters, Disclosures & Verification

## Status: FILED — 2026-07-14 · ED-IN-0064

## What ran

Five deterministic, working-tree-only observatory scripts + the contract flowchart generator (commands in
`00_workplan.md`). All exited 0.

- **L0 prose (`vector_audit.py`)** — 110 design docs, 176 tokens, the 5 metadata/citation graphs, P1/P2/P3
  validation, 8 diagnostic modes (A–H). **Validation FAILED 1/3.**
- **L2 + G_code (`structure_audit.py`)** — the `module_contracts.yaml` producer→consumer wiring (27 modules, 99
  raw / 43 simple edges) + the AST import graph over `sim/`+`tools/` (173 modules, 268 edges). This is the
  connectivity + "shape of code architecture" core.
- **G_pointer / L1 formula / G_generation** (`pointer_audit.py` / `formula_audit.py` / `gen_audit.py`) — quantity
  resolution (52.7 %), the formula-dependency DAG (0 cycles at contract granularity — a lower bound, GAP-J2), and
  currency drift (16 stale pointers, 4 unregistered heads, 1 drift).
- **`contract_flowchart.py`** — regenerated `module_flowchart.mermaid` / `state_graph.mermaid` / `module_map_flat.md`.

## What changed vs the 2026-04-29 baseline

The last committed run (`archives/audit/2026-04-29-topographic-analysis/`) is stale (305 in-scope files changed —
the family was the repo's #1 stalest). **Do not compare finding-for-finding**: this run reads *today's* corpus, and
the pipeline itself was a stub until 2026-07-13/14, so this is the first real run since the dispatcher landed. The
old run also predates the whole L1/L2 architecture layer — the G_code/L2/pointer/formula/gen scripts are new
(WS0b, ED-IN-0052..0056), so the "shape of code architecture" half has no 2026-04-29 antecedent. Where the L0 v3
run reported "NPC Behavior is the integration spine," this run **re-confirms it structurally** (npc_behavior in-12,
L2 cut-vertex).

## Disclosures (a green cell is not whole-repo coverage)

- **numpy / sklearn absent** in this environment → `vector_audit.py`'s supporting TF-IDF graph (Stage 3) was
  skipped; the multi-graph core + all 8 modes + P1/P2/P3 still ran (graceful degradation, as designed). PyYAML
  present; all other layers are stdlib+PyYAML.
- **L0 coverage** = 110 docs = 10.3 % of `designs/` `.md`, 6.3 % of the repo. `params/`/`sim/`/`tests/`/`canon/`
  prose are structurally invisible to L0.
- **Contract↔code correspondence is UNVERIFIED** (3/27 name-map) — a fictional contract entry would pass the L2
  layer unchallenged; closing it needs the `mechanics_index.yaml sim_module:` join (deferred, GAP-I4).
- **`gen_audit`** measures currency-partition health, not v40 adoption; `canon//references//params/` paths can't
  register as LIVE heads (a `designs/`-anchored blind spot in the reused rule).
- **`formula_audit` cycles = 0 is a lower bound** — node identity is the raw derivation string, so the Mandate↔L/PS
  cross-module loop (bare vs annotated legs) is not detected (GAP-J2).
- The committed `tools/observability/graph.json` is stale (2026-07-07, pre-Observatory); we used the freshly-computed
  `structure/data/*.json` as ground-truth and did **not** regenerate `graph.json` (to keep PR scope tight).

## Verification — two independent read-only gates

1. **Adversarial critic (refute-by-default), model Opus.** Verdict **SOUND-WITH-FIXES**: every count/citation
   spot-checked resolves; ED-MB-0010 fabrication correctly screened; `scale_transitions §12` supports the seam
   classification. Two GENUINE items reclassified to complete-the-chain (`MS`-owner, `engine_clock`) — both have
   determining code/canon already present. One date slip fixed (ED-IN-0016 → 2026-07-05). Thesis *strengthened*.
2. **Six-directional coverage verifier, model Opus** ("double check in all directions"). Produced the 16×6 matrix,
   reconciled the machine `!A6` seams to §12.4 (8 match; the 9th is a scale mislabel), and found three directions
   hide a genuine gap beyond annotation-debt (diagonal zero-instances, Accord/transfer uncalled, temporal decay
   deferred). All load-bearing directional claims were then **re-grep-verified by hand** (file:line in
   `directional_coverage_v1.md`).

Both gates' findings are folded into the synthesis + register via the correction banners; `adversarial_review_v1.md`
is the authoritative correction layer.

## Reproduce

`pip install pyyaml && python -m pytest tests/valoria -q` (the observatory scripts are regression-pinned in
`tests/valoria/test_{vector,structure,pointer,formula,gen}_audit.py`), then re-run the `00_workplan.md` commands
into a fresh dated folder. Numbers will differ from this run only if the corpus changed.
