<!-- [REPLACEMENT: 2026-04-29 — supersedes v2 of this same file] -->
<!-- [PROVISIONAL: 2026-04-29 — topographic analysis workplan v3, pre-execution] -->
<!-- STATUS: PROVISIONAL — workplan; analytic instrument, not gameplay mechanic -->
<!-- AUTHORITY: PP-676, ED-760 -->

# Topographic Analysis Workplan v3 — Multi-Graph Triangulation

**Date:** 2026-04-29 (third revision, supersedes v1 and v2 same-day)
**Status:** PROVISIONAL — pursued in this session
**Replaces:** v2 (committed earlier 2026-04-29, see commit history). v2 execution exposed thirteen methodology problems; v3 pivots from TF-IDF-primary to multi-graph triangulation with TF-IDF demoted to supporting evidence.

---

## §0 What changed from v2

v2 used a single primary signal (TF-IDF cosine over paragraph co-occurrence) and tried to validate it against expected_groups derived from my prior. Validation failed at Jaccard 0.222. The post-hoc analysis revealed the methodology had structural problems beyond just the failed validation:

| v2 problem | v3 resolution |
|---|---|
| Threshold deviation (0.35 → 0.20 post-hoc) | All thresholds locked in §3.7 BEFORE any run; if signal is weaker than thresholds expect, that's a finding, not a tuning opportunity |
| Validation k=4 mathematically excludes small groups | Validation rebuilt as **structural property checks**, not k-NN Jaccard. Properties true regardless of group composition (e.g. "foundation cluster has lower mean inter-graph degree than periphery") |
| Within-class clustering not filtered | §3.4 explicit class taxonomy; within-class pairs filtered from implied-missing diagnostic |
| Token deduplication missing | §3.3 pre-execution merge for known surface-form duplicates (Tensions/Tensions Deck etc.) |
| Citation graph too sparse to filter | §3.5 EXPANDED citation graph: explicit + implicit (any system name mention in another system's body counts as edge); accept noise, gain signal |
| Two diagnostics produced null | §2 drops empty-regions diagnostic entirely; status-disagreement reformulated as PP-affect-graph cross-reference |
| Validation circularity (prior tested against prior) | §3.8 validation uses **independent structured graphs** (Μ/throughline/PP) as alternate ground truths, then looks for *agreement across graphs*, not agreement with my prior |
| Auto-extracted tokens unvalidated | §3.2 auto picks reviewed against canonical_sources before inclusion; unsure ones flagged not included |
| Promised but never run: full+auto twin diagnostics | Dropped from scope; if needed, future run |
| Discourse corpus extracted, never used | v3 builds the discourse overlay (where editorial attention concentrates) as a real diagnostic |
| Unconventional paragraph-IDF | §3.6 standard term-frequency, log-IDF, document-length-normalized; matches scikit-learn TfidfVectorizer defaults |
| Arbitrary document weights | Dropped. All design docs weight 1.0; status filtering happens at the diagnostic level instead |
| MS Trajectory regex error reported as finding | Pre-execution sanity sweep on every token verifies non-zero match before vectorization proceeds |

v2 findings that **survive without rerun**:
- §1.1 faction/NPC/Conviction-as-hubs (mean-similarity ranking, no thresholding required)
- §1.2 Settlement Layer downstream sink (citation graph only, no TF-IDF)
- §1.4 Wager↔Edeyja (will re-verify in v3 expanded citation graph)
- §1.5 vocabulary debt three terms (direct corpus match, no methodology dependency)
- §1.6 Settlement Layer / CI Political under-coverage (paragraph counts, no methodology dependency)

v3's job: deepen these, find what v2 missed.

---

## §1 N — Necessity case

Same as v1/v2. Self-exempting analytic instrument, vetting Class A.

---

## §2 Diagnostic targets — multi-graph framing

Each diagnostic now operates on multiple graphs, with **agreement across graphs** as the primary confidence signal.

The five graphs:
- **G_cite** — expanded citation graph (explicit + implicit cross-references)
- **G_tfidf** — TF-IDF cosine graph (supporting only)
- **G_mu** — systems sharing an Μ mode (parsed from throughlines_meta_infill Μ contribution lists)
- **G_throughline** — systems sharing a throughline (parsed from throughlines_meta and infill)
- **G_pp** — systems touched by the same patch (parsed from patch_register_active.yaml `affects:` lists)

### 2.1 Multi-graph hub overload
A token is a hub if it is in the top quintile by degree in ≥ 3 of 5 graphs. Single-graph hubs are noise; multi-graph hubs are real connectivity centers.

### 2.2 Implied-but-missing edges (now multi-graph)
Pairs where ≥ 2 of {G_mu, G_throughline, G_pp} link them but G_cite does not. These are pairs the project's structured metadata says are connected, but no explicit citation has been written. **Strict cross-class only** — within-class pairs (Conviction↔Conviction etc.) excluded.

### 2.3 Notional edges
Pairs where G_cite links them (especially explicitly via `Cross-references:`) but no other graph does. Citation without metadata or content support.

### 2.4 Cascade-without-return
Same as v2 §2.4, but now run on G_cite (expanded) instead of just explicit citations. Chains of length ≥ 3 with no return path.

### 2.5 Sparse-context tokens
Tokens with paragraph count ≤ 10th percentile AND degree ≤ 10th percentile in G_cite. Drops tokens that are sparse in paragraph mentions but well-cited (their footprint is structural, not textual).

### 2.6 Throughline orphan check
For each of the 41 throughlines, count paragraphs that substantiate it (heuristic: paragraph mentions ≥ 2 of the throughline's contributing systems per throughlines_meta_infill Μ block). Throughlines with ≤ 2 substantiating paragraphs = at risk of being orphaned in implementation.

### 2.7 Μ servicing imbalance
For each of the 11 Μ modes, count paragraph mentions of contributing systems. Top quintile / bottom quintile ratio is the imbalance score. Highly imbalanced Μ = mode that depends mostly on undocumented systems.

### 2.8 Vocabulary debt sweep
Direct grep for known-struck terms (Game Master, Cultural Reformation, Coup Counter, plus any others surfaced in patch register `[STRUCK]` markers). Reports paragraph count + doc list per legacy term.

### 2.9 Discourse-design divergence
For each token, ratio of (paragraph mentions in discourse corpus / paragraph mentions in design corpus). Tokens with very high ratios are over-discussed (much editorial attention, less actual design substance) — possible over-thinking. Tokens with very low ratios are under-discussed (substantial design, no editorial scrutiny) — possible under-review.

### 2.10 Multi-graph isolates
Tokens with degree = 0 or 1 in **every** graph. These are conceptually present in the corpus but functionally disconnected from everything else.

---

## §3 Technique

### 3.1 Corpus
Same as v2 (43 design docs, 4 discourse, on disk). Reuse v2 corpus_design.json + corpus_discourse.json.

### 3.2 Tokens
Reuse v2 tokens.json (84 tokens, 74 seed + 10 auto). Auto-picks audited:
- KEEP: Ein Sof, Zoom In, Domain Action, Scene Slate, Mass Seizure, Casus Belli, Dynastic Proclamation
- KEEP as legacy markers: Game Master, Cultural Reformation, Coup Counter
- (None of the auto-picks are removed; all clear the canonical-source-or-clearly-major-mechanic test)

### 3.3 Token deduplication

Pre-execution merge:
- `Tensions Deck` is a strict subset of `Tensions` context — keep both but flag as known-coupled (suppress from implied-missing if both appear in a high-cosine pair)
- `MS` and `Mending Stability` already merged in surface forms — verify
- `CI` (Church Influence the clock) and `CI Political` (the doc) — keep separate; CI is the metric, CI Political is the system

No new merges needed. Mostly recording the v2 lessons.

### 3.4 Class taxonomy for within-class filtering

Tokens grouped into classes for filtering:
- **Convictions** (7): Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity
- **Pressure Points** (4): Evidence, Consequence, Authority, Loyalty
- **Factions** (7): Crown, Church, Hafenmark, Varfell, Löwenritter, Restoration Movement, Guilds
- **NPCs** (10): the named NPC tokens
- **Clocks** (6): MS, CI, IP, PI, TS, TCV
- **Systems** (everything else)

Within-class pairs are suppressed from implied-but-missing (Faith↔Reason is by-design; Crown↔Church is by-design; etc.). Cross-class pairs are kept.

### 3.5 Expanded citation graph

For each design doc D and each token T whose primary doc is not D:
- If D's body contains T's primary surface form ≥ 2 times → G_cite has edge (T_of_D, T)
  - Where "T_of_D" = any token whose primary doc IS D
- Plus all explicit refs from v2 (`Cross-references:`, `see X.md`, `supersedes:`)
- Plus all `affects:` lists from `patch_register_active.yaml` mapped through token primary docs

Threshold ≥ 2 mentions filters paragraph-level accidents. Expected output: ~150-300 edges (an order of magnitude denser than v2's 11).

### 3.6 TF-IDF (now supporting only)
Standard scikit-learn TfidfVectorizer over paragraphs as documents, tokens as terms. L2 normalize. No custom IDF formulation.

Used only for:
- Hub overload §2.1 cross-check
- Sparse-context cross-check §2.5
- Discourse-design divergence §2.9 (separate vectorizer per corpus)

NOT used for:
- Implied-but-missing (now multi-graph)
- Status-disagreement (dropped in current form)
- Empty regions (dropped entirely)

### 3.7 Pre-committed thresholds (locked, no exceptions)

If a threshold doesn't produce signal, that is a finding, not a tuning opportunity. Locked:

- Hub overload §2.1: top quintile by degree in ≥ 3 of 5 graphs → all reported
- Implied-but-missing §2.2: ≥ 2 of {G_mu, G_throughline, G_pp} link, G_cite doesn't → top 25 by metadata-link-strength
- Notional §2.3: G_cite explicit edge AND no metadata link AND no other graph link → all reported
- Cascade-without-return §2.4: chain length ≥ 3, no return in G_cite → all reported
- Sparse-context §2.5: paragraph ≤ 10th percentile AND G_cite degree ≤ 10th percentile → all reported
- Throughline orphan §2.6: ≤ 2 substantiating paragraphs → all reported
- Μ servicing imbalance §2.7: ratio top/bottom quintile ≥ 5 → all reported
- Vocabulary debt §2.8: direct match → all reported
- Discourse-design divergence §2.9: discourse:design ratio outside [0.05, 0.5] → all reported
- Multi-graph isolates §2.10: degree ≤ 1 in every graph → all reported

Tie-breaking: alphabetical token order.

### 3.8 Validation — structural properties, not group-Jaccard

Three structural properties checked. Each is true if methodology produces meaningful signal, regardless of which tokens cluster:

**P1 (Foundation periphery):** Foundation tokens (Self-Rendering, Leap, Coherence, Throughlines, Ein Sof) should have HIGHER mean degree across G_cite + G_throughline than the corpus median (foundation tokens are referenced from many places).

**P2 (Conviction class symmetry):** The 7 Convictions should have approximately equal degree in G_throughline (each Conviction maps to faction-aligned throughlines). Standard deviation of Conviction-degree should be < 30% of mean Conviction-degree.

**P3 (Citation density):** G_cite should have ≥ 100 token-edges. v2's 11 was an artifact of overly-strict explicit-only parsing; expanded parsing should easily clear this. If it doesn't, the corpus is structurally under-cross-referenced and that itself is the finding.

Acceptance: ≥ 2 of 3 properties pass → methodology validated. < 2 pass → report disagreement, do not promote findings to authoritative.

P1 and P2 are non-circular (don't depend on my prior groupings). P3 is a methodology smoke test (citation graph extraction works).

---

## §4 Stage execution

### Stage 1 — Build expanded citation graph (this session)
Parse explicit refs (already done in v2). Add implicit refs by token-name mention threshold. Cross-load PP `affects:` lists. Output `g_cite_v3.json`.

### Stage 2 — Build structured-metadata graphs (this session)
Parse throughlines_meta + infill for Μ contribution lists. Build G_mu, G_throughline. Cross-load PP register for G_pp. Output `g_metadata.json`.

### Stage 3 — Standard TF-IDF (this session)
Re-vectorize with standard sklearn TfidfVectorizer. Output `g_tfidf_v3.npz`.

### Stage 4 — Validation (this session)
P1, P2, P3 checks. Gate: ≥ 2 of 3 to proceed to authoritative findings. < 2 → findings reported with caveat banner.

### Stage 5 — Multi-graph diagnostics (this session)
Run all §2 diagnostics. Where multiple graphs agree, finding is high-confidence; where they disagree, finding is informative.

### Stage 6 — Throughline orphan + Μ imbalance (this session)
Use parsed metadata from Stage 2 for §2.6, §2.7.

### Stage 7 — Discourse-design divergence (this session)
Vectorize discourse corpus separately. Compute ratio per token. §2.9.

### Stage 8 — Write outputs (this session)
- Update `02_weakness_register.md` with v3 findings (append, don't replace v2 sections; v3 = §6 onwards)
- Update `01_methodology.md` with v3 parameters
- Add `03_validation_report.md` (P1/P2/P3 results)

### Stage 9 — Commit (this session)
Single safe_commit. Replaces 00_workplan.md (v2 → v3), updates other docs, adds new data files.

---

## §5 What this can't find

Same as v1/v2. Plus: **the validity of the multi-graph approach itself depends on the structured metadata being correct.** If throughlines_meta_infill has errors or is incomplete, G_mu and G_throughline inherit those errors. v3 is more robust than v2 but no methodology with this corpus can produce signal independent of the corpus's own structural quality.

---

## §6 Outputs

```
designs/audit/2026-04-29-topographic-analysis/
├── 00_workplan.md (v3, this doc)
├── 01_methodology.md (updated for v3)
├── 02_weakness_register.md (v2 sections + v3 §6 onwards)
├── 03_validation_report.md (NEW — P1/P2/P3 properties)
└── data/
    ├── (v2 outputs preserved)
    ├── g_cite_v3.json (NEW)
    ├── g_metadata.json (NEW)
    ├── g_tfidf_v3.npz (NEW)
    ├── multigraph_diagnostics.json (NEW)
    └── discourse_overlay.json (NEW)
```

---

## §7 Vetting block

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: []
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
  q: pass
  note: "v3 replacement of v2 (which was replacement of v1). Self-exempting on Ω/Μ — meta-tooling. v3 pivots from TF-IDF-primary to multi-graph triangulation in response to v2 execution finding that TF-IDF is too noisy at this corpus's cross-system signal density. Pursued in same session per Jordan directive."
```
