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
  inline. Successor methodology to one-off pipelines (v1 TF-IDF-only failed
  validation; v2 added pilot+citation but was TF-IDF-primary; v3 multi-graph
  triangulation passed validation 2/3 structural properties).
---

# Valoria Vector Audit

## Purpose

Surface project weaknesses that hand-curation cannot reliably find: implied-but-missing cross-references, notional citations (cited but content-empty), citation-graph cascades without return paths, hub overload, sparse-context tokens, multi-graph isolates, throughline orphans, vocabulary debt, and discourse/design divergence. Operates over corpus-derived structural graphs, not LLM judgment.

**Scope:** **Analytic instrument only**, never gameplay mechanic. Self-exempting on Ω/Μ vetting (Class A, mu: [], M-ratings ○ across the board) — produces evidence for design decisions but is not itself a design decision. Findings are PROVISIONAL leads, not verdicts; methodology validation outcome must be reported with results.

**History:** v1 (commit ac8f55aa) hand-curated TF-IDF, no validation gate. v2 (PP-676) added pilot + citation graph + validation; FAILED validation at Jaccard 0.222. v3 (PP-676) pivoted to multi-graph triangulation, PASSED 2/3 structural properties. **v3 is the canonical methodology.** This skill enshrines v3.

---

## Step 1 — Input Validation (MANDATORY, BLOCKING)

Read the following files from the working tree (use the Read tool) before proceeding. The checkout is authoritative — do not fetch from GitHub and do not work from memory. If a listed file is absent from the working tree, stop and report it.

- `references/canonical_sources.yaml` — systems list (controlled vocabulary)
- `systems/_architecture/complete_systems_reference.md` — NPC list, faction list (moved from the retired `designs/architecture/` 2026-07-19, ED-IN-0071 P4/P5)
- `references/throughlines_meta.md` — T-NN framework header
- `references/throughlines_meta_infill.md` — T-NN table (parsed for G_throughline)
- `registers/patch_register_active.yaml` — PP affects: lists for G_pp

The pipeline ALWAYS bypasses index routing for content reads — index files lack the body content needed for citation graph extraction; read the full files above.

---

## Step 2 — Confirm Run Configuration

| Parameter | Default | Notes |
|---|---|---|
| Corpus scope | full design + foundation | Audit/session corpus split via banner classifier (§3.1 below) |
| Token list | seed (canonical_sources + named NPCs) + auto-extract | Auto threshold: ≥3 docs, ≥10 paragraph mentions |
| Disambiguation | enabled | Required for English-word collisions (Faith, Order, Reason, Equity, etc.) |
| Diagnostics | all 8 | A subset can be requested for partial runs |
| Validation | structural properties P1/P2/P3 | Hard gate: 2/3 to publish as authoritative |
| Implicit citation threshold | ≥ 2 mentions | Body-mention count for G_cite implicit edges |
| Random seed | 42 | t-SNE / force-directed reproducibility |

**Pre-committed thresholds (§3.7) MUST NOT be tuned post-hoc.** Threshold deviation invalidates findings. v2 deviated on implied-missing (0.35 → 0.20) — this is the methodology problem v3 was designed to prevent.

---

## Step 3 — Pipeline Stages

The pipeline's specification is this stage table. **`scripts/vector_audit.py` now implements it**
(stage dispatcher landed 2026-07-13, repo-realignment WS0a): it reads the working tree, builds the
five graphs, runs P1/P2/P3 validation and all 8 diagnostic modes, and writes the outputs below. Run
it directly:

```
python3 skills/valoria-vector-audit/scripts/vector_audit.py --repo-root . --output-dir <run-dir>
```

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

Stages 0 and 5 are **gates**: pilot must produce ≥6/8 intuitive top-3 neighbors; validation must pass ≥2/3 properties.

---

## Step 4 — Diagnostic Modes

Each diagnostic targets a specific structural weakness. Modes can run independently after stages 1-5 are complete.

### Mode A — Multi-graph hubs
Tokens in top quintile by degree in **≥3 of 4 metadata-graphs** (cite, throughline, mu, pp). High confidence centrality. Single-graph hubs reported separately as supplementary.

### Mode B — Implied-but-missing edges
Pairs where ≥2 of {G_throughline, G_mu, G_pp} link them but G_cite does not. Cross-class only (within-class pairs filtered using class taxonomy in §3.4 of `references/methodology.md`). These are connections the structured metadata says exist but no explicit citation has been written.

### Mode C — Notional edges
Pairs where G_cite links them but no metadata graph does. Citation without content support — likely stale ref or vocabulary debt.

### Mode D — Cascade-without-return
Chains of length ≥3 in G_cite with no return path. Surfaces downstream sinks (one-way pressure patterns that violate Ω-d feedback principle).

### Mode E — Sparse-context tokens
Tokens in bottom 10th percentile of paragraph count AND bottom 10th percentile of G_cite degree. Either under-developed or vocabulary debt.

### Mode F — Throughline orphan check
For each throughline, count substantiating paragraphs (paragraphs mentioning ≥2 of throughline's load-bearing systems). ≤2 substantiating = at risk of being orphaned. **Requires `references/throughlines_meta_infill.md` to have the Load-bearing systems column** (added by PP-677). Without that column, this mode degenerates to null — diagnose accordingly.

### Mode G — Vocabulary debt sweep
Direct grep for known-struck terms (parsed from `registers/supersession_register.yaml`). Reports paragraph count + doc-level concentration per legacy term.

### Mode H — Multi-graph isolates
Tokens with degree ≤1 in **every** graph. Conceptually present, structurally disconnected. Often canonical concepts lacking first-class doc status.

---

## Step 5 — Output Format

The skill produces three deliverables in `designs/audit/{date}-{audit-name}/`:

```
00_workplan.md            # config + pre-committed thresholds
01_methodology.md         # executed parameters; what changed from prior runs
02_weakness_register.md   # PRIMARY DELIVERABLE — narrative findings per mode
03_validation_report.md   # P1/P2/P3 structural property results
data/                     # all intermediate JSON/NPZ
```

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

1. **Threshold deviation post-hoc.** v2 lowered cosine 0.35 → 0.20 because magnitudes were lower than expected. Forbidden — if signal is weaker than thresholds, that's a finding, not a tuning opportunity. Pre-committed thresholds in §3.7 of `references/methodology.md` are LOCKED.

2. **Validation criterion mathematically impossible.** v2's k=4 k-NN excluded small expected_groups (3-token groups maxed at Jaccard 0.25 < 0.30 threshold). v3 uses **structural properties** (foundation periphery, conviction symmetry, citation density) that don't depend on group composition.

3. **Within-class clustering pollutes implied-missing.** Convictions cluster with Convictions, factions with factions — this is taxonomy, not a missing connection. Class taxonomy filter in §3.4 of methodology MUST be applied.

4. **Out-degree-only computation.** v2 measured cite degree as `len(g_cite[t])` which is out-only; tokens without dedicated docs (55 of 84) had artificial degree 0. Use **in+out neighbor union** for accurate centrality.

5. **TF-IDF cosine artifact mistaken for centrality.** v2's "faction/NPC/Conviction-as-hub" finding was an artifact of paragraph breadth, not connection strength. v3 demoted TF-IDF to supporting role; multi-graph hub measure (Mode A) is the correct centrality.

6. **Citation graph too sparse to filter.** v1 used explicit-only refs (11 token-edges across 84 tokens); "no citation" was the default for nearly every pair, making the citation-absence filter trivially false. v3 expanded to ≥2 implicit body mentions (421 edges) — citation-absence becomes informative.

7. **Single-doc concentration of legacy terms is the cleanup signal.** Game Master sweep was 11/16 in threadwork_v30.md. Cultural Reformation was 10/15 in peninsular_strain_v30.md. Single-doc grep-replace handles concentrated cleanups; PP-678 demonstrated the workflow.

---

## Output Rules

- All findings cite source token + paragraph count + doc list — no rounded numbers
- Multi-graph confidence (how many graphs agree) is part of the finding, not separate
- Validation result is reported up-front; findings inherit its confidence
- No commit until P1/P2/P3 validation outcome is reported
- Sweep modes (G) produce single-doc concentration reports (essential for actionable cleanup)
- Audit folder is `designs/audit/{date}-{audit-name}/` — never overwritten across reruns; new run = new dated folder

---

## Reference Files

- `references/methodology.md` — v3 multi-graph triangulation specification (full §3 procedure, all pre-committed thresholds, class taxonomy)
- `references/diagnostic_modes.md` — A through H mode specifications with worked examples
- `references/v1_v2_v3_history.md` — methodology evolution, why each pivot was needed (institutional memory)
- `scripts/vector_audit.py` — **runnable pipeline** (stage dispatcher implemented 2026-07-13,
  repo-realignment WS0a; supersedes the 2026-07-11 STUB status noted under ED-IN-0035/0036).
  Implements Stages 1–6 (Stage 0 pilot + Stage 7 discourse overlay reserved), reads the working
  tree only, and writes `data/*.json` + `02_weakness_register.md` + `03_validation_report.md`.
  Reuses the in-file `SEED_TOKENS`/`PILOT_TOKENS`/`CLASSES`/helper scaffolding. `numpy`/`sklearn`
  are optional (only the supporting TF-IDF graph needs them). Invoke via the command in Step 3.
  Note: it reads *today's* corpus, so its numbers differ from the frozen 2026-04-29 archived run.
  P2 conviction-symmetry is **v4 as of 2026-07-21 (ED-IN-0080, Jordan ruling A)**: measured on
  context-gated prose presence (the v3 throughline formulation was unsatisfiable by construction),
  with an all-zero vector reporting NOT MEASURABLE rather than the retired `cv=999` sentinel —
  see methodology §3.8 for the ruling, the thin-pass caveats, and the staged attribute-symmetry
  extension.
- `scripts/structure_audit.py` — the observatory's **architecture layers** (WS0b core, added
  2026-07-13). Companion to `vector_audit.py` (which is the L0 prose layer). Builds **G_code** (AST
  import graph over `sim/` + `tools/` — cycles, cut-vertices, orphans) and **L2** (the
  `module_contracts.yaml` producer→consumer wiring graph — Key emit/consume closure, phantom
  producers, dangling non-terminal emits, `doc:null` modules, cross-scale locality). Stdlib + PyYAML
  only (no numpy/sklearn/networkx — the graph algorithms are implemented in-file), working-tree only,
  deterministic. **Provenance-tagged** (notional/`[ASSUMPTION]`/`doc:null` modules bucketed as
  lower-confidence) and it **measures, never gates** (pytest + import-smoke gate). Invoke:
  `python3 scripts/structure_audit.py --repo-root . --output-dir <run>` → `structure_register.md` +
  `data/*.json`. Regression-pinned in `tests/valoria/test_structure_audit.py` against PR #131's
  hand-caught L2 defects (the mass_battle fabricated emit, the personal_combat dead emits).
- `scripts/pointer_audit.py` — the observatory's **G_pointer** layer (WS0b, added 2026-07-13; the WS1
  registry-work progress meter). For every stat/quantity identifier on the same surfaces A17 scans
  (`module_contracts.yaml` `state`/`derivations` + `sim/*.py` `stat_deltas`/`impact_vector` literals),
  does it resolve to a `descriptor_registry`/`names_index` key, or is it hardcoded pointer-debt? It
  **reuses A17's rule, does not reimplement it** (CLAUDE.md §8) — imports `tools/quantity_registry.py`
  `resolve()` and `tools/ci_quantity_vocabulary_check.py`'s scanners verbatim; A17 is the CI gate, this
  is the graph/meter VIEW. Stdlib + PyYAML only, working-tree only, deterministic. **Measures, never
  gates.** The unresolved list is *candidate* debt — it explicitly flags that some rows are
  computed/internal quantities (e.g. `cumulative_damage`, `L_s`) that A17 calls "expected backlog, not
  a bug," so triage before acting. Invoke:
  `python3 scripts/pointer_audit.py --repo-root . --output-dir <run>` → `pointer_register.md` +
  `data/{g_pointer,pointer_scorecard}.json`. Tests: `tests/valoria/test_pointer_audit.py` (pins the
  §8 reuse-by-identity + the A17 ground-truth count match).
- `scripts/formula_audit.py` — the observatory's **L1 formula-dependency** layer (WS0b, added
  2026-07-13). Builds the quantity-dependency DAG (output ← input) from `module_contracts.yaml`
  `derivations` + `descriptor_registry.yaml`, detecting orphan inputs (a quantity consumed but never
  produced), multi-definition conflicts (the "Combat Pool defined three ways" class), and dependency
  cycles. **Reuses** `tools/quantity_registry.py` `resolve()`,
  `ci_quantity_vocabulary_check._split_bundled`, and `structure_audit.py`'s `tarjan_scc`/`degrees`
  (no reimplementation, §8). Stdlib + PyYAML only, working-tree only, deterministic. **Measures, never
  gates**; the unresolved/orphan list is *candidate* debt (triage first — some are computed/placeholder
  quantities). A malformed derivation with a null `output` is surfaced via a sentinel node, never
  silently dropped. Invoke: `python3 scripts/formula_audit.py --repo-root . --output-dir <run>` →
  `formula_register.md` + `data/*.json`. Tests: `tests/valoria/test_formula_audit.py` (§8
  reuse-by-identity + end-to-end cycle detection + the null-output regression).
- `scripts/gen_audit.py` — the observatory's **G_generation** currency layer (WS0b, added 2026-07-13;
  the WS3 / NS4 v40-transition meter). Partitions the whole `.md` corpus into LIVE heads vs HISTORICAL
  records (so a historical doc's stale refs are *structurally* never scanned), then runs three
  detections: (1) **stale version-pointers** inside live heads — a `_vNN.md` ref that is superseded,
  *moved* (successor exists per the restructure ledger — a trivial repoint), or genuinely nonexistent;
  (2) **unregistered canonical heads** (a `## Status: CANONICAL` doc absent from
  `canonical_sources.yaml`); (3) **currency drift** (registered AND superseded). **Reuses**
  `ci_generation_consistency.py`'s currency rule (`canonical_docs`/`status_of`/`superseded_ids`/
  `RECOGNIZED`), `broken_dependency_checker.py`'s
  `extract_file_refs`/`get_all_repo_files`/`_load_restructure_map`, and `vector_audit.banner_classify`
  — no rule re-derived (§8). Authoritative registration beats the weak banner content-keyword; physical
  archival paths still demote. Stdlib + PyYAML only, working-tree only, deterministic. **Measures, never
  gates** (`ci_generation_consistency.py` is the WARN-only gate). The stale-pointer list is
  severity-triaged (superseded/moved = mechanical repoints; only *nonexistent* needs a human). Invoke:
  `python3 scripts/gen_audit.py --repo-root . --output-dir <run>` → `generation_register.md` +
  `data/g_generation.json`. Tests: `tests/valoria/test_gen_audit.py` (33 tests: §8 reuse-by-identity,
  the LIVE/HISTORICAL discriminator, the moved-vs-nonexistent severity split).
- `scripts/ripple_audit.py` — the observatory's **L3 cross-scale RIPPLE / propagation** layer (added
  2026-07-21). The **qualitative** complement to `vector_audit`'s **quantized** map: where the vector
  audit gives every token numeric coordinates, this makes the typed dependency **chains** explicit and
  traversable in **all directions** and **sliceable** by scale, answering *"if I change X, what ripples —
  downstream (what a change affects) AND upstream (provenance) — and WHY does each hop exist?"* It is a
  **composition, not a new parser** (§8): unifies `structure_audit.build_l2()` (module→module Key wiring,
  the mechanic scale) + `formula_audit.build_contract_edges()` (quantity input→output derivations, the
  value scale) into one typed directed graph, **bridged across scales** (`quantity --reads--> module
  --emits_consumes(Key)--> module --produces--> quantity`). Edge types `emits_consumes` / `derives` /
  `produces` / `reads`, all oriented src→dst = "flows into"; forward-BFS = downstream ripple, backward-BFS
  = provenance. Every hop carries **WHAT** (node kind), **HOW** (edge type), **WHY** (provenance: the Key
  type / formula / contract source — never synthesized). **Provenance-tagged** (`⚠notional` hop = through a
  doc:null / [ASSUMPTION]-grade module). Optional **quantized overlay** (`--vector-run <dir>`) annotates
  name-matching nodes with a vector_audit run's cite/tl/mu/pp degrees, so the qualitative chain and the
  quantized coordinate travel on one node. Stdlib + PyYAML only, working-tree only, deterministic.
  **Measures, never gates.** Invoke: `python3 scripts/ripple_audit.py --repo-root . --output-dir <run>`
  (→ `ripple_register.md` + `data/ripple_graph.json`, the machine-hookable surface other tooling reads),
  or ad-hoc `--node <X> --direction {up,down,both} --depth N --layers <slice>`. **Full-token
  impact query (2026-07-21):** `--vector-run <dir> --impact <token>` loads a vector_audit run's
  exported full-token `G_cite`+metadata graph and does UNDIRECTED transitive reachability —
  "tug anything, see what moves" — ranking every reachable token by graph distance and flagging
  the far (≥3 hop) cross-subsystem *surprising* hits with their path (e.g. `Clocks → Factions →
  Key: mechanical.project_advanced → Game Director`). This unifies the vector audit's QUANTIZED
  graph with ripple's directional reachability into one query. Tests:
  `tests/valoria/test_ripple_audit.py` (§8 reuse-by-identity, bidirectionality, depth/slice, cycle-safety).
  **v1 scope:** L1+L2 (mechanic+value+Key scales). Documented extension points: fold in `vector_audit`'s
  L0 doc-citation graph (design scale), `pointer_audit`'s G_pointer (identifier→key), and `gen_audit`'s
  G_generation (supersedes) as further edge types on the same node namespace — so every
  wrapper/system/subsystem/mechanic/routine/primitive/formula/value/token/key becomes one navigable,
  all-directions, all-scales chain the rest of the toolchain (audits, sim, tests, design) can hook into.

## Cross-references

- Original execution: `deprecated/archives/audit/2026-04-29-topographic-analysis/` (v1, v2, v3 all on file —
  moved from `designs/audit/` to `deprecated/archives/audit/` at some point after this skill was written;
  corrected 2026-07-11, ED-IN-0036)
- Workplan v3: `deprecated/archives/audit/2026-04-29-topographic-analysis/00_workplan.md`
- Weakness register: `deprecated/archives/audit/2026-04-29-topographic-analysis/02_weakness_register.md`
- PP-676 / ED-762 (v2+v3 execution)
- PP-677 / ED-764 (throughlines load-bearing systems column — restored Mode F)
- PP-678 / ED-765 (vocabulary debt sweep workflow demonstrated)

## Forward-only findings-disposition discipline

Every finding in `02_weakness_register.md` must resolve to either a filed `ED-<LANE>-NNNN` id
(per `references/id_reservations.yaml`'s allocation protocol) or an explicit no-action line (e.g.
"no action — working as intended," "no action — superseded by PP-NNN"). This mirrors the
disposition-table discipline added to `valoria-mechanic-audit`'s output contract in the same
audit-ecosystem consolidation batch. Applies going forward only — the existing
`02_weakness_register.md` from the 2026-04-29 run is not retroactively required to carry this
(no findings-schema existed at that time to check it against).

## Dashboard registry logging (MANDATORY on completion)

When this skill's run concludes — pass, fail, or partial — append one record to the
Valoria audit/simulation-run registry (`references/audit_registry.jsonl`) so the
GitHub Pages dashboard and `tools/ci_audit_registry_check.py` can see it. Do this
every time, not only on request — a skipped append is what makes the dashboard's
verdict table go stale.

```bash
python tools/audit_registry.py append \
  --audit-type vector_audit \
  --subsystem <personal_combat|mass_battle|social_contest|faction_political|settlement_territory|threadwork|fieldwork_investigation|architecture|cross_cutting|corpus_wide> \
  --skill valoria-vector-audit \
  --date <YYYY-MM-DD> \
  --folder "<designs/audit/... path this run's output actually lives at>" \
  --scope "<one-line: what was audited>" \
  --verdict <this skill's own verdict, mapped to PASS|FAIL|PARTIAL|CONFORMANT|NON_CONFORMANT|OPEN|MIXED|CLOSED> \
  --verdict-detail "<one-line context, e.g. a PR number or ratification note>"
```

Pick `--subsystem` from what the run actually targeted (`cross_cutting` if it
genuinely spans several, `corpus_wide` only for a whole-corpus pass — this skill's
own runs are usually `corpus_wide`). See `tools/audit_registry.py`'s module
docstring for the full field/vocabulary reference — this is the single source of
truth for the schema, not this note.
