<!-- [PROVISIONAL: 2026-04-29 — topographic analysis workplan, pre-execution] -->
<!-- STATUS: PROVISIONAL — workplan proposal; analytic instrument, not gameplay mechanic -->
<!-- AUTHORITY: PP-676, ED-760 -->

# Topographic Analysis Workplan — Vectorized Corpus Investigation

**Date:** 2026-04-29
**Status:** PROVISIONAL
**Scope:** Build a corpus-derived topographic view of Valoria's design space — semantic vectorization of all canonical and provisional content — to surface weaknesses that hand-curation cannot reach.
**Source:** Jordan directive 2026-04-29 — "use the artifact to investigate ways the project is weak" / "topographical approach with vectorized tokens and dynamic connective lines."
**Audience:** Claude. **Not a player tool, not a Jordan-facing UI.** This is an analytic instrument for evaluating the design from a perspective hand-curation cannot supply.
**Related:** PP-676, ED-760. Companion to v2 of the connections artifact (separate session, hand-curated edges).

---

## §0 Why this is genuinely different from the connections artifact

The connections artifact (v1, v2 forthcoming) treats each system as a discrete node and asks: *do these systems intersect?* The answer comes from a designer's read — mine in v1, mine-after-audit in v2. Either way, the topology reflects whose hand drew it.

The topographic approach asks a different question: *based on the actual textual evidence in the canonical corpus, how does the conceptual space cluster?* The topology is derived, not drawn. Two systems are close if the corpus repeatedly co-locates them, regardless of whether anyone has explicitly connected them in a design doc. Two are far apart if the corpus rarely puts them in the same neighborhood, regardless of whether they're nominally related.

The diagnostic value is highest in the **gap between the two views**:
- Edges hand-curation drew that the corpus doesn't substantiate → notional connections without textual substance
- High corpus similarity that hand-curation missed → implied connections that should be made explicit
- Hand-curated hubs that the corpus shows as peripheral → over-claimed importance
- Corpus-central tokens that hand-curation under-emphasized → under-developed importance

These gaps are weaknesses no amount of hand-auditing finds, because they require comparing hand-curated structure against an independent measurement.

---

## §1 N — Necessity case

| N question | Answer |
|---|---|
| Renaissance dynamic modeled? | None — analytic instrument, not gameplay |
| Already covered by existing mechanics? | No — no existing tooling derives topology from textual evidence |
| Different player situations? | N/A |
| Load-bearing in subject? | N/A — meta-tooling |
| Lost by abstracting? | We lose the ability to detect implied-but-missing connections, propagation gaps, status disagreements, and Μ servicing imbalances that hand-curation can't surface. These are real failure modes the project has already exhibited (the salience-4/5 cliff, the symbolic_effects table consumed by nothing, NPC Standing static — all surfaced by simulation, but topography would have flagged them earlier as structural anomalies) |

**N verdict: pass** — analytic infrastructure. Same self-exempting category as PP-674, PP-675.

---

## §2 Analytic targets — what the topography is built to surface

### 2.1 Implied-but-missing edges
Pairs with high corpus co-occurrence but no explicit cross-reference in any design doc. Highest-value diagnostic. Candidates the v2 audit would otherwise miss.

### 2.2 Notional edges (over-claimed connections)
Edges hand-curated that turn out to have low corpus similarity. The connection exists in the designer's head but isn't substantiated by textual content. Either rewrite the spec to make the connection real, or remove the claim.

### 2.3 Status-disagreement edges
Strongly-similar pairs where one node is canonical and one is provisional. Propagation gap candidates: provisional design poking at canonical territory, or canonical design implicitly assuming provisional behavior.

### 2.4 Cascade-without-return chains
Sequences of high-similarity edges that flow one direction without a return path. The project intent statement (Ω) requires *positive feedback loop*. One-way cascades are by definition pressure without feedback — a known failure pattern.

### 2.5 Hub overload
Tokens with high similarity to many other tokens. Single point of failure: any spec error there cascades widely. Topology doesn't distinguish *load-bearing* from *over-extended* — the analysis must.

### 2.6 Sparse-context tokens
Tokens that appear in canon but with thin surrounding context. Either under-developed concepts that should be elaborated, or vocabulary debt where a term is referenced without being defined.

### 2.7 Empty regions
Areas of the projected space that should plausibly contain something but don't. Conceptual gaps. The hardest diagnostic to formalize and the most generative when it works.

### 2.8 Μ servicing audit
Map each Μ mode (α / β / γ / δ) to its corpus footprint. Imbalances visible as topographic asymmetry: if Μ-α PRESSURE has a dense cluster at peninsula scale and nothing at scene scale, that's an Ω-d violation candidate (pressure should be felt at every scale, every action paying what it buys).

### 2.9 Throughlines coverage
For each of the 41 throughlines, locate its primary corpus footprint. Throughlines without a clear topographic home are at risk of being orphaned in implementation.

---

## §3 Technique

### 3.1 Corpus extraction
- **Bypass `github_ops` index routing.** The router auto-redirects large design docs to their `_index.md` skeleton companions for token efficiency. Semantic vectorization needs full text. Use direct GitHub Contents API or GraphQL with `git/blobs`.
- **Scope:** all `design_doc` and `params` paths from `references/canonical_sources.yaml`, plus `canon/00..03`, plus `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md`, plus `designs/audit/2026-04-29-terminology-conversion/00_workplan.md` and `designs/audit/mass_battle_*_2026-04-29.md` (recent provisional design).
- **Estimated size:** ~150–250k tokens, well within 1M context window. Stage 1 dump confirmed ~150k tokens for the canonical core (47 paths via index-routed fetch; full-text fetch will be larger).
- **Output:** `designs/audit/<date>-topographic-analysis/data/corpus.json` — `{path: full_content}` keyed by repo path. Hash + size manifest committed for reproducibility.

### 3.2 Token curation
- **Seed list (~80 tokens):** every system from `canonical_sources.yaml`, every named NPC from `complete_systems_reference.md` Part 1, every clock (MS / CI / IP / PI / CV / TCV), every Conviction (7), every Pressure Point (4), every Style (4 contest styles), every Mode (the 2 + Zoom-In after PP-675 lands; pre-PP-675 the 3), every Throughline category, every key Foundation concept (Leap, Coherence, Self-Rendering, Knot, TS, Domain Echo, Sufficient Scope, Scar).
- **Auto-extracted (~40 tokens):** capitalized multi-word terms appearing in ≥3 canonical docs and not already in seed list. Filter against false positives (Renaissance proper nouns, parliamentary terminology) using a stopword list.
- **Final list:** ~120 tokens, manually curated. Stored as `tokens.json` with metadata: `{id, surface_forms (synonyms/aliases), scale, status, seed/auto, definition_source_path}`.

### 3.3 Vectorization
- **Granularity:** paragraph-level (split each doc on `\n\n` after first stripping HTML comments and YAML frontmatter). Each paragraph becomes a "document" in TF-IDF terms.
- **Token matching:** for each token's surface forms (case-insensitive, word-boundary), count appearances per paragraph. Build sparse `token × paragraph` matrix.
- **TF-IDF weighting:** standard formula. Weight downward for paragraphs in retired/struck content (banner-detected) and provisional content (banner-detected), so retired material doesn't drag the vector toward dead concepts.
- **Output:** `vectors.npz` — sparse matrix, NumPy.

### 3.4 Similarity + projection
- **Pairwise cosine similarity** over the token vectors. Output: `similarity.npz` (token × token).
- **2D projection:** sklearn `TSNE(perplexity=15, init='pca', random_state=42)`. Alternatively force-directed where similarity is spring strength — easier to interpret, more visually stable across re-runs. Plan: run both, pick whichever gives cleaner clusters; document the choice in the data manifest. Output: `layout.json` — `{token_id: [x, y]}`.
- **Density grid:** kernel density estimate on the 2D layout, producing a `width × height` array suitable for contour rendering. Output: `density.json`.

### 3.5 Diagnostic overlays
For each diagnostic in §2, compute and persist:
- Top-N implied-but-missing edges (corpus_similarity high, hand-curated edge absent)
- Top-N notional edges (hand-curated edge present, corpus_similarity low)
- Status-disagreement edge list (canonical ↔ provisional pairs above similarity threshold)
- Cascade-without-return chain candidates (longest one-way paths in hand-curated edge graph)
- Hub overload report (token degree centrality, top quartile)
- Sparse-context tokens (paragraphs-mentioned count below 3rd-percentile)
- Empty-region candidates (low-density regions adjacent to high-density clusters)
- Μ servicing distribution (per-Μ paragraph counts, weighted by canonicality)

Output: `weakness_register.md` — narrative findings with token-pair specifics + provenance (which docs/paragraphs).

---

## §4 Stage execution with context-safety

**Critical constraint per Jordan:** this analysis must run in a dedicated session. Folding it into other work breaks context.

### Stage 1 — Corpus extraction
Single bash block. Fetches ~250k tokens of full-text corpus via direct GitHub API (bypassing index router). Writes `corpus.json` to `/home/claude/`, then commits it under `designs/audit/<date>-topographic-analysis/data/corpus.json` for reproducibility. **Checkpoint:** at end of stage, dump file count + total chars + hash inline so a vanished turn doesn't lose Stage 1 work.

### Stage 2 — Token curation + vectorization
Single bash block. Builds token list (seed + auto-extracted), tokenizes paragraphs, builds TF-IDF matrix. Writes `tokens.json` and `vectors.npz`. **Checkpoint:** dump token count + vocabulary stats + matrix shape.

### Stage 3 — Similarity + projection
Single bash block. Cosine similarity + t-SNE + density grid. Writes `similarity.npz`, `layout.json`, `density.json`. **Checkpoint:** dump top-10 strongest similarity pairs + 2D coordinate ranges.

### Stage 4 — Diagnostic overlays + weakness register
1–2 bash blocks. Computes each §2 diagnostic, writes `weakness_register.md` as narrative. **Checkpoint:** dump finding counts per category.

### Stage 5 — Optional: viewer artifact
Only if Jordan requests. The deliverable is the weakness register, not the visualization. Keep this stage off the critical path.

### Stage 6 — Commit + close
Single `safe_commit` of all data + register + propagation note + session log. Promotes PP-676 from PROVISIONAL → APPLIED.

---

## §5 What this can't find

- **UX failures** — Scene Slate pressure (R-39-A) was the most consequential issue from the political dynamics stress test, and it was about *player experience* (no discretionary actions left), not topology. The corpus can't see this.
- **Computational cost** — runtime profile concerns, content authoring scope (the 210-entry symbolic resonance table) live outside the graph.
- **Tedium / pacing** — every edge is treated as a structural fact, not a player-time cost.
- **Mechanical correctness** — whether a formula is right or balanced is invisible. Topology says "these connect"; it can't say "they connect *correctly*."
- **Authoring debt** — the 1,190-entry political-dynamics authoring scope doesn't show up.
- **Intentional asymmetries** — sometimes one-way cascades or sparse regions are correct (e.g. archives directory). The analysis flags candidates; a designer judges which are real weaknesses.

---

## §6 When to run

Two valid orderings:

**Option A — Before v2 connections audit.** Topographic analysis produces an edge candidate list (top corpus similarities + status-disagreement edges + implied-but-missing edges). The v2 audit then evaluates each candidate manually against the actual specs. The hand-curated v2 inherits corpus-derived suggestions.

**Option B — After v2 connections audit.** Topographic analysis runs against the audited v2 graph. The diagnostic value is the *gap* between the two views: where does corpus-derived topology disagree with hand-audited topology? Disagreements are the highest-value findings.

Recommendation: **B**. The gap analysis is the highest-yield output. v2 first, then this. v2's audited graph becomes input to topographic diagnostics.

---

## §7 Outputs

- `designs/audit/<date>-topographic-analysis/00_workplan.md` (this doc, post-execution updated to APPLIED)
- `designs/audit/<date>-topographic-analysis/01_methodology.md` (executed methodology, parameters, choices)
- `designs/audit/<date>-topographic-analysis/02_weakness_register.md` (the actual findings — primary deliverable)
- `designs/audit/<date>-topographic-analysis/data/corpus.json`
- `designs/audit/<date>-topographic-analysis/data/tokens.json`
- `designs/audit/<date>-topographic-analysis/data/vectors.npz`
- `designs/audit/<date>-topographic-analysis/data/similarity.npz`
- `designs/audit/<date>-topographic-analysis/data/layout.json`
- `designs/audit/<date>-topographic-analysis/data/density.json`
- *(optional Stage 5)* `designs/audit/<date>-topographic-analysis/03_viewer.jsx`

---

## §8 Pre-execution checklist (must satisfy before running)

- [ ] PP-676 promoted from PROVISIONAL → APPLIED on Jordan signoff
- [ ] Dedicated session — no other work folded in
- [ ] v2 connections artifact landed (per Option B recommendation)
- [ ] `canonical_sources.yaml` pruned below threshold (currently 4670/5000)
- [ ] Index-routing bypass technique tested (Stage 1 needs this; verify with a single full-text fetch before bulk pull)

---

## §9 Vetting block

```yaml
vetting:
  class: A
  necessity: pass  # analytic infrastructure for surfacing weaknesses unreachable by hand-curation; §1 N case
  omega: pass  # not a gameplay mechanic; supports Ω vetting indirectly by making weakness candidates visible to the designer
  mu: []  # meta-tooling, doesn't directly serve any Μ mode
  m_ratings:
    M-1: "○"
    M-2: "○"
    M-3: "○"
    M-4: "○"
    M-5: "○"
    M-6: "○"
    M-7: "○"
    M-8: "○"
    M-9: "○"
    M-10: "○"
    M-11: "○"
  q: pass  # workplan structure: phased rollout with context-safety checkpoints, output paths specified, technique grounded in a tested Stage 1 partial run, limits explicitly called out
  note: "Self-exempting on Ω/Μ pattern — same as PP-674, PP-675. Analytic instrument, not gameplay mechanic. Stage 1 partial run completed 2026-04-29 confirmed feasibility (numpy/scipy/sklearn available, corpus fetches at ~150k tokens through index-routed path; full-text fetch will exceed but stays well under 1M context window). Execution deferred to dedicated session per Jordan."
```

---

## §10 Open items / next session

1. Jordan signs off on this workplan (single decision: run it, defer it, or kill it)
2. If run: schedule dedicated session, ideally after v2 connections audit lands
3. If deferred: this workplan stays PROVISIONAL until conditions in §8 are met
4. If killed: archive workplan with reasoning ledger entry

The single-bit decision is whether the gap-analysis between hand-curated and corpus-derived topology is worth the dedicated session. The recommendation is yes — the diagnostic categories in §2 are not reachable any other way, and the project has already exhibited weaknesses (salience cliff, dead resonance table, static Standing) of exactly the structural-anomaly type that this approach is built to catch earlier.
