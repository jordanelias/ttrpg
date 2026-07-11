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
- `designs/architecture/complete_systems_reference.md` — NPC list, faction list
- `references/throughlines_meta.md` — T-NN framework header
- `references/throughlines_meta_infill.md` — T-NN table (parsed for G_throughline)
- `canon/patch_register_active.yaml` — PP affects: lists for G_pp

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

The full pipeline lives in `scripts/vector_audit.py` and runs in sequence:

| Stage | What | Output |
|---|---|---|
| 0 | Pilot validation (8 well-understood tokens, sanity check tokenization) | `data/pilot.json` |
| 1 | Corpus extraction with banner classifier (design vs discourse) | `data/corpus_*.json`, `data/corpus_manifest.json` |
| 2 | Token curation: seed + auto-extract with disambiguation rules | `data/tokens.json`, `data/auto_candidates.json` |
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
Direct grep for known-struck terms (parsed from `canon/supersession_register.yaml`). Reports paragraph count + doc-level concentration per legacy term.

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
- `scripts/vector_audit.py` — full pipeline, runs all stages

## Cross-references

- Original execution: `designs/audit/2026-04-29-topographic-analysis/` (v1, v2, v3 all on file)
- Workplan v3: `designs/audit/2026-04-29-topographic-analysis/00_workplan.md`
- Weakness register: `designs/audit/2026-04-29-topographic-analysis/02_weakness_register.md`
- PP-676 / ED-762 (v2+v3 execution)
- PP-677 / ED-764 (throughlines load-bearing systems column — restored Mode F)
- PP-678 / ED-765 (vocabulary debt sweep workflow demonstrated)

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
