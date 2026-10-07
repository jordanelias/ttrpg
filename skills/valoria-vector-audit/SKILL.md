---
name: valoria-vector-audit
description: >
  Multi-graph triangulation audit over the Valoria design corpus. ALWAYS use this
  skill when asked to: run a topographic analysis, find weaknesses unreachable
  by hand-curation, vectorize the corpus, locate vocabulary debt, find
  citation-graph cascades, identify isolates / hubs / sparse-context tokens,
  detect implied-but-missing connections, or check throughline coverage. Trigger
  on: "topographic audit", "vector audit", "corpus audit", "find weaknesses",
  "find debt", "implied connections", "what's missing", "what's notional",
  "where are the gaps", "rerun topographic", "validate against corpus", or any
  request to surface non-obvious structural properties of the design corpus.
  This skill owns ALL vectorized-audit work — do not reconstruct the pipeline
  inline. Canonical methodology: v3 multi-graph triangulation.
---

# Valoria Vector Audit

## Purpose

> ### ⛔ CORE DOCTRINE — SURFACE, NEVER CULL (read first; survives context loss)
> **The entire point of this tool is to point out WHAT IS MISSING.** A stub, a null, an empty
> contract, an untraceable module, a denylisted system, an unverified pin, a rarely-cited orphan —
> **those are the signal, not the noise.** Never run this pipeline in a "signal-heavy / drop the
> marginal" mode: that hides exactly what the tool exists to expose. Every cull must be a
> *surfaced, reasoned exclusion*, never a silent drop.
> - `vector_audit.audit_exclusions(root)` surfaces every cull (the `SKIP_SYSTEMS` denylist + the
>   `AUDIT_FLOORS`) with reasons — nothing is dropped silently.
> - If you find yourself filtering results to look "cleaner," STOP: that is the failure mode this
>   doctrine exists to prevent.
> - **The `--emit-findings` feed carries ALL EIGHT modes (schema 2).** High-volume modes carry a
>   bounded sample + a true `_total` (never a silent cap). Adding a mode = extend
>   `emit_structural_findings`.
> - **The feed is retain-and-flag.** Emit EVERY finding; the lower-confidence hub×hub Mode-B pairs
>   carry `filtered` + `filter_reason` rather than being dropped, so a reader auditing the feed sees
>   everything and can overrule a flag. No isolate is filtered. Never delete a finding from the feed
>   to raise its signal.
> - The Incompleteness Ledger and its dashboard are retired (`FORK:1e4c6f4`); feed nothing to them.

Surface project weaknesses that hand-curation cannot reliably find: implied-but-missing cross-references, notional citations (cited but content-empty), citation-graph cascades without return paths, hub overload, sparse-context tokens, multi-graph isolates, throughline orphans, vocabulary debt, and discourse/design divergence. Operates over corpus-derived structural graphs, not LLM judgment.

**⚠️ What it is BLIND to (state this with every result).** It sees the design **citation/registry STRUCTURE** — not simulation `.py` behaviour, not the typed `engine/engine_params/` **values**, not actual runtime. A wrong number, a mis-tuned formula, or a broken simulation is invisible to it. And **Mode D (cascade sinks)** uses a capped return-path search that trips heavily on a dense corpus — Mode-D findings are UNVERIFIED LEADS carrying their own trip count, not confirmed gaps.

**Five structural graphs:** `cite` (citation), `throughline` + `mu` (throughlines_meta + throughlines_complete), `pp` (patch co-affects), and **`key`** (`build_g_key`, a token projection of `module_contracts.yaml`'s emit→consume flow). ⚠ **`key` is empty since ED-IN-0232** (the emit/consume interface was deleted with the Key substrate), so the triangulation effectively runs on four graphs. A Key-type token left isolated is surfaced, never filtered as an expected false alarm, and its mechanism is NOT assumed — an orphan/dangling emit (`structure_audit`'s `dangling_emit`), an unemitted/unconsumed Key, or a `derivations`-only cross-module flow this graph does not read.

**Scope:** **Analytic instrument only**, never gameplay mechanic. Self-exempting on Ω/Μ vetting (Class A, mu: [], M-ratings ○ across the board) — produces evidence for design decisions but is not itself a design decision. Findings are PROVISIONAL leads, not verdicts; methodology validation outcome must be reported with results.

---

## Step 1 — Input Validation (MANDATORY, BLOCKING)

Read the following files from the working tree (use the Read tool) before proceeding. The checkout is authoritative — do not fetch from GitHub and do not work from memory. If a listed file is absent from the working tree, stop and report it.

- `references/canonical_sources.yaml` — systems list (controlled vocabulary)
- `complete_systems_reference.md` and `throughlines_complete.md` — NPC/faction lists and the second throughline→systems source; quarantined under `.designs/` (ED-IN-0231), and the script reads them there
- `references/throughlines_meta.md` — T-NN framework header
- `references/throughlines_meta_infill.md` — T-NN table (parsed for G_throughline)
- `registers/patch_register_active.yaml` — PP affects: lists for G_pp
- `references/module_contracts.yaml` — emit→consume Key flow for G_key (empty since ED-IN-0232)

The pipeline ALWAYS bypasses index routing for content reads — index files lack the body content needed for citation graph extraction; read the full files above.

---

## Step 2 — Confirm Run Configuration

| Parameter | Default | Notes |
|---|---|---|
| Corpus scope | full design + foundation | Audit/session corpus split via banner classifier (methodology §3.1) |
| Token list | seed (canonical_sources + named NPCs) + auto-extract | Auto threshold: ≥3 docs, ≥10 paragraph mentions |
| Disambiguation | enabled | Required for English-word collisions (Faith, Order, Reason, Equity, etc.) |
| Diagnostics | all 8 | A subset can be requested for partial runs |
| Validation | structural properties P1/P2/P3 | Hard gate: 2/3 to publish as authoritative |
| Implicit citation threshold | ≥ 2 mentions | Body-mention count for G_cite implicit edges |
| Random seed | 42 | t-SNE / force-directed reproducibility |

**Pre-committed thresholds (methodology §3.7) MUST NOT be tuned post-hoc.** Threshold deviation invalidates findings.

---

## Step 3 — Pipeline Stages

The pipeline's specification is this stage table. **`scripts/vector_audit.py` implements it**: it
reads the working tree, builds the five graphs, runs P1/P2/P3 validation and all 8 diagnostic modes,
and writes the outputs below. Run it directly:

```
python3 skills/valoria-vector-audit/scripts/vector_audit.py --repo-root . --output-dir <run-dir>
```

**Corpus-breadth layers (`--layer`).** The default **L0** is a CURATED slice — only the
`canonical_sources.yaml` heads; it is the calibrated P1/P2/P3 scope, so a green L0 result is **not**
whole-repo coverage. `--layer L1` extends the trace across the whole **design** tree
(systems/engine/canon/godot/proposals). **Scope honesty — L1 is one direction, not "all
directions":** it extends corpus breadth and the **cite graph only**. It does **NOT** extend the
throughline/mu/key graphs (registry-derived: throughline from `throughlines_meta` + `throughlines_complete`,
mu from `throughlines_meta`, key from `module_contracts` — the same at every layer), the token universe
(registry-derived — a token absent from `names_index`/`proper_noun`/`module_contracts` is invisible at
every layer), non-`.md` content (simulation `.py`, typed params), or the
P1/P2/P3 thresholds (calibrated on L0 — an L1 run reuses them but does **not** re-validate). Narrative
and `workplans/` trees are excluded (would pollute cite with story co-mention). L0 stays the default;
every run's weakness register discloses the layer, the coverage %, AND the un-extended directions —
surface the slice, never let a green slice read as the whole.

It is **working-tree only** (no GitHub fetch) and degrades gracefully without `numpy`/`sklearn` (the
supporting TF-IDF graph is skipped; the multi-graph core still runs). Stage table:

| Stage | What | Output |
|---|---|---|
| 0 | Pilot validation (8 well-understood tokens, sanity check tokenization) | `data/pilot.json` |
| 1 | Corpus extraction with banner classifier (design vs discourse) | `data/corpus_*.json`, `data/corpus_manifest.json` |
| 2 | Token curation: **derived from the live registries** (canonical_sources `systems:` + names_index + proper_noun_registry) layered on the curated disambiguation core — see `derive_tokens()` | `data/tokens.json` |
| 2.5 | Expanded citation graph (explicit refs + implicit ≥2 body mentions + PP affects) | `data/g_cite.json` |
| 3 | Standard sklearn TF-IDF over paragraphs (supporting only) | `data/g_tfidf.npz` |
| 4 | Metadata graphs from throughlines table + Μ collapsing + PP affects | `data/g_metadata.json` |
| 5 | Structural property validation (P1, P2, P3) | `data/validation.json` |
| 6 | Multi-graph diagnostics (8 modes, see Step 4) | `data/multigraph_diagnostics.json` |
| 7 | Discourse/design divergence overlay | `data/discourse_overlay.json` |

Stages 0 and 5 are **gates**: pilot must produce ≥6/8 intuitive top-3 neighbors; validation must pass ≥2/3 properties. ⚠ The script implements Stages 1–6; Stage 0 (pilot) and Stage 7 (discourse overlay) are reserved, so the pilot gate is not run.

---

## Step 4 — Diagnostic Modes

Each diagnostic targets a specific structural weakness and can run independently after stages 1-5. Full method, output format and recommended action per mode: `references/diagnostic_modes.md`; locked thresholds: methodology §3.7.

- **A — Multi-graph hubs.** Top quintile by degree in **≥3 of 4 metadata-graphs** (cite, throughline, mu, pp). Single-graph hubs reported separately as supplementary.
- **B — Implied-but-missing edges.** ≥2 of {G_throughline, G_mu, G_pp} link the pair but G_cite does not. Cross-class only (class taxonomy, methodology §3.4).
- **C — Notional edges.** G_cite links the pair but no metadata graph does — likely stale ref or vocabulary debt.
- **D — Cascade-without-return.** G_cite chains of length ≥3 with no return path: downstream sinks (one-way pressure patterns that violate Ω-d feedback principle).
- **E — Sparse-context tokens.** Bottom 10th percentile of paragraph count AND of G_cite degree. Either under-developed or vocabulary debt.
- **F — Throughline orphan check.** ≤2 substantiating paragraphs (a paragraph mentioning ≥2 of the throughline's load-bearing systems). **Requires `references/throughlines_meta_infill.md` to have the Load-bearing systems column** (PP-677). Without that column, this mode degenerates to null — diagnose accordingly.
- **G — Vocabulary debt sweep.** Direct grep for known-struck terms (parsed from `registers/supersession_register.yaml`); paragraph count + doc-level concentration per legacy term.
- **H — Multi-graph isolates.** Degree ≤1 in **every** graph. Often canonical concepts lacking first-class doc status.

---

## Step 5 — Output Format

The skill produces these deliverables in the run's `--output-dir`. `designs/audit/` is dissolved and
`.audit/` takes no additions (CLAUDE.md §3); where a run's folder lives is the orchestrator's call.

```
00_workplan.md            # hand-written, before the run: config + pre-committed thresholds
01_methodology.md         # hand-written: executed parameters; what changed from prior runs
02_weakness_register.md   # script — PRIMARY DELIVERABLE, narrative findings per mode
03_validation_report.md   # script — P1/P2/P3 structural property results
data/                     # script — intermediate JSON (methodology §5)
```

The script writes no `pilot.json`, `g_tfidf.npz` or discourse overlay (Stages 0 and 7 are reserved).

Each finding in `02_weakness_register.md` carries:
- Confidence flag derived from how many graphs agree
- Reference to which mode produced it
- Specific token names + counts (no LLM-paraphrased "approximately")
- Recommendation (action, file, target) where the finding is actionable

**Validation outcome is reported in §0 of the register, not buried.** If validation FAILS, findings are explicitly downgraded to "leads, not verdicts" and that framing is preserved through all subsequent sections.

---

## Step 6 — Patch Register Entry

The audit produces a Class A vetting block (analytic instrument, self-exempting):

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: []
  m_ratings:
    M-1: "○"  # ... through M-11: "○"
  q: pass
  note: "Multi-graph triangulation audit; analytic instrument, self-exempting."
```

PP entry references the audit folder; ED entry describes what was found.

---

## Common Failure Modes (learned from v1 → v2 → v3)

1. **Threshold deviation post-hoc.** If signal is weaker than thresholds, that's a finding, not a tuning opportunity. Pre-committed thresholds in §3.7 of `references/methodology.md` are LOCKED.

2. **Validation criterion mathematically impossible or circular.** Validate on **structural properties** (methodology §3.8), which depend neither on group composition nor on a prior grouping.

3. **Within-class clustering pollutes implied-missing.** Convictions cluster with Convictions — taxonomy, not a missing connection. Class taxonomy filter in §3.4 of methodology MUST be applied.

4. **Out-degree-only computation.** Tokens without dedicated docs get artificial degree 0. Use **in+out neighbor union** (methodology §4).

5. **TF-IDF cosine artifact mistaken for centrality.** TF-IDF is supporting only; Mode A is the correct centrality.

6. **Citation graph too sparse to filter.** Explicit-only refs make "no citation" true of nearly every pair; the ≥2 implicit body-mention threshold makes citation-absence informative.

7. **Single-doc concentration of legacy terms is the cleanup signal.** Single-doc grep-replace handles concentrated cleanups.

8. **A zero or null reported instead of debugged.** A token at 0 paragraphs, or a diagnostic returning nothing, triggers a tokenization/threshold debug before it is reported.

9. **Duplicate tokens.** Merge or flag known-coupled tokens (methodology §3.3) before the run; review auto-extracted tokens before they count.

10. **A planned step silently skipped.** Every step `00_workplan.md` (hand-written) names is run or reported as not run.

---

## Output Rules

- All findings cite source token + paragraph count + doc list — no rounded numbers
- Multi-graph confidence (how many graphs agree) is part of the finding, not separate
- Validation result is reported up-front; findings inherit its confidence
- No commit until P1/P2/P3 validation outcome is reported
- Sweep modes (G) produce single-doc concentration reports (essential for actionable cleanup)
- Name the `--output-dir` `{date}-{audit-name}/`; never overwritten across reruns; new run = new dated folder
- Every finding resolves to a filed `ED-<LANE>-NNNN` id (per `references/id_reservations.yaml`'s
  allocation protocol) or an explicit no-action line (e.g. "no action — working as intended," "no
  action — superseded by PP-NNN"), as in `valoria-mechanic-audit`'s disposition table
- Record nothing in a registry: a pass's output is edits plus at most one commit paragraph
  (`CLAUDE.md` §0)

---

## Reference Files

- `references/methodology.md` — v3 multi-graph triangulation specification (full §3 procedure, all pre-committed thresholds, class taxonomy)
- `references/diagnostic_modes.md` — A through H mode specifications, output shape and recommended action
- `references/v1_v2_v3_history.md` — what may and may not be relaxed

Every script below reads the working tree only, is deterministic, and **measures, never gates**.
The five siblings of `vector_audit.py` are stdlib + PyYAML only (no numpy/sklearn/networkx).
Each reuses an existing owner's rule rather than re-deriving it (CLAUDE.md §8) — the module
docstring names the owners; extend them, never re-implement. Given `--output-dir <run>`, each writes
a markdown register (`structure_register.md`, `pointer_register.md`, `formula_register.md`,
`generation_register.md`, `ripple_register.md`, `workbench_<module>.md`) + `data/*.json`.

- `scripts/vector_audit.py` — **runnable pipeline**, the L0 prose layer (Step 3). `numpy`/`sklearn`
  are optional. P2 conviction-symmetry is **v4 (ED-IN-0080)** — methodology §3.8.
- `scripts/structure_audit.py` — **architecture layers**: **G_code** (AST import graph over `CODE_ROOTS` +
  `EXTRA_CODE_ROOTS` — cycles, cut-vertices, orphans) and **L2** (the `module_contracts.yaml`
  producer→consumer wiring graph — Key emit/consume closure, phantom producers, dangling non-terminal
  emits, `doc:null` modules, cross-scale locality). Notional/`[ASSUMPTION]`/`doc:null` modules are
  bucketed as lower-confidence. Invoke:
  `python3 scripts/structure_audit.py --repo-root . --output-dir <run>`. Its gate is pytest
  (`tests/valoria/test_structure_audit.py`) + import-smoke.
- `scripts/pointer_audit.py` — **G_pointer**: does each stat/quantity identifier on the surfaces A17
  scans resolve to a `descriptor_registry`/`names_index` key, or is it hardcoded pointer-debt? A17
  is the CI gate; this is the meter view. The unresolved list is *candidate* debt — triage before
  acting, as some rows are computed/internal quantities. Invoke:
  `python3 scripts/pointer_audit.py --repo-root . --output-dir <run>`. Tests:
  `tests/valoria/test_pointer_audit.py`.
- `scripts/formula_audit.py` — **L1 formula-dependency** DAG (output ← input) from
  `module_contracts.yaml` `derivations` + `descriptor_registry.yaml`: orphan inputs (consumed but
  never produced), multi-definition conflicts, dependency cycles. The orphan list is *candidate*
  debt (triage first). A null-`output` derivation is surfaced via a sentinel node, never dropped.
  Invoke: `python3 scripts/formula_audit.py --repo-root . --output-dir <run>`. Tests:
  `tests/valoria/test_formula_audit.py`.
- `scripts/gen_audit.py` — **G_generation** currency. Partitions the `.md` corpus into LIVE heads vs
  HISTORICAL records (historical docs are never scanned), then detects (1) **stale
  version-pointers** in live heads — superseded, *moved* (a mechanical repoint) or nonexistent (only
  this needs a human); (2) **unregistered canonical heads** (a `## Status: CANONICAL` doc absent from
  `canonical_sources.yaml`); (3) **currency drift** (registered AND superseded). Authoritative
  registration beats the banner content-keyword; archival paths still demote.
  `ci_generation_consistency.py` is the WARN-only gate. Invoke:
  `python3 scripts/gen_audit.py --repo-root . --output-dir <run>`. No test file.
- `scripts/ripple_audit.py` — **L3 cross-scale RIPPLE**: *"if I change X, what ripples — downstream
  AND upstream (provenance) — and WHY does each hop exist?"* One typed directed graph over module
  wiring and quantity derivations, bridged across scales (node kinds, edge types, directions: the
  module docstring). Every hop carries **WHAT**, **HOW** and **WHY** (provenance — never
  synthesized); a `⚠notional` hop passes through a doc:null / [ASSUMPTION]-grade module. Invoke:
  `python3 scripts/ripple_audit.py --repo-root . --output-dir <run>` (`data/ripple_graph.json` is the
  machine-hookable surface), or ad-hoc `--node <X> --direction {up,down,both} --depth N --layers
  <slice>`. `--vector-run <dir>` overlays a vector_audit run's degrees; `--vector-run <dir> --impact
  <token>` ranks every token reachable (undirected) in that run's graph and flags far (≥3 hop)
  cross-subsystem hits with their path. Tests: `tests/valoria/test_ripple_audit.py`. Scope: L1+L2
  only; the L0 doc-citation, G_pointer and G_generation graphs are not folded in.
- `scripts/workbench.py` — the **Reconciliation Workbench**. Holds the **ENGINE** view beside the
  **PROSE** view for a module and flags every **divergence** as a **card**: a question a human
  resolves by moving *either* side — it never auto-reconciles. The `mentioned` edge state (endpoints
  in the doc, relationship unstated) is the siloed-prose fingerprint. Cards carry a **stable id** so
  `references/observatory_dispositions.yaml` (absent today; read as empty) records human answers and
  only OPEN/CHANGED cards surface; the **notional-shadow guard** stops a fabricated contract row from
  being reconciled *to*. Prose matching is heuristic co-mention — a lead, not a verdict. Invoke:
  `python3 scripts/workbench.py --repo-root . --module <name> [--output-dir <run>]`. Tests:
  `tests/valoria/test_workbench.py`.
