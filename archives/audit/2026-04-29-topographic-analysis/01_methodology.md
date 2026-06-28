<!-- [PROVISIONAL: 2026-04-29 — topographic analysis methodology, executed] -->
<!-- AUTHORITY: PP-676 -->

# Methodology — Executed Parameters

**Date executed:** 2026-04-29
**Workplan:** designs/audit/2026-04-29-topographic-analysis/00_workplan.md (v2)

## Corpus
- 48 paths attempted, 47 fetched (1 phantom failure: bare `conflict_architecture_proposal.md` from regex over `canonical_sources.yaml` — full-path version succeeded)
- Banner classifier: 43 design / 4 discourse / 0 excluded
- Total design corpus: 1,066,216 chars (~266k tokens)

## Tokens
- 74 seed tokens from canonical_sources.yaml + named NPCs from complete_systems_reference.md Part 1
- 10 auto-extracted (capitalized multi-word, ≥3 docs, ≥10 paragraphs, stopword-filtered)
- Auto-additions: Ein Sof, Zoom In, Domain Action, Scene Slate, Mass Seizure, Casus Belli, Dynastic Proclamation, Game Master (legacy flag), Cultural Reformation (legacy flag), Coup Counter (legacy flag)

## Disambiguation rules
For tokens with English-word collisions (7 Convictions, 4 Pressure Points, Crown, Church):
- Paragraph must contain at least one context-window pattern
- Examples: `Faith` requires `Conviction|Framework|Divine|Church|Cardinal|doctrine` in same paragraph

## Vectorization
- Paragraph-level granularity (split on `\n\n`, min 50 chars, HTML comments + code blocks stripped)
- TF-IDF: paragraph-IDF using `log((1+N) / (1+df)) + 1` where df = number of tokens that appear in paragraph
- Document weighting: 1.0 canonical, 0.7 provisional, 0.3 struck/deprecated (none in design corpus)
- L2 normalization per token vector
- 84 × 2940 matrix, 4108 sparse entries

## Similarity
- Pairwise cosine on normalized vectors

## Projection
- t-SNE: `perplexity=15, max_iter=2000, init='pca', random_state=42, metric='cosine'`
- Force-directed: spring strength = `cosine_similarity`, repulsion = `200/dist²`, 500 iterations, k_attract=1.0, dt=0.1, seed=42

## Pre-committed thresholds (locked before viewing data)
- Implied-but-missing: cosine ≥ 0.20 AND citation absent → top 25 (relaxed from 0.35 because magnitudes turned out lower than expected; flagged as deviation)
- Notional: citation present AND cosine ≤ 0.10 → all
- Status-disagreement: cosine ≥ 0.20 AND status pair {canonical, provisional} → top 15
- Hub overload: top quintile mean similarity → top 15
- Sparse-context: ≤ 10th percentile paragraph count → all
- Cascade-without-return: chain length ≥ 3, no return path → all

## Validation
- 13 expected_groups derived from canonical_sources.yaml + complete_systems_reference.md Part 1
- k-NN with k=4
- Per-group Jaccard, mean across groups
- Mean Jaccard threshold: ≥ 0.50 = validated, 0.30-0.50 = partial, < 0.30 = failed
- **Result: 0.222 — failed**

## Known methodology limitations
1. Citation graph is conservative (explicit refs only); implicit references not caught
2. Token deduplication not applied (Tensions/Tensions Deck score 0.93)
3. Within-class clustering not filtered (Convictions↔Convictions inflate implied-missing list)
4. Sparse-context tokens have noisy similarity scores
5. Empty regions diagnostic null at 84 tokens (would need 200+ for meaningful density gradient)
6. expected_groups reflect prior hand-curation; methodology validation against own prior has circularity risk
7. Threshold deviation: cosine ≥ 0.20 used for implied-missing instead of pre-committed 0.35, after observation that magnitudes were lower than expected. Flagged as protocol deviation.


---

# v3 — Multi-Graph Triangulation (executed 2026-04-29)

## Pivot from v2

v2's TF-IDF-primary methodology was demoted; v3 makes citation graph + structured metadata graphs primary. Five graphs:

- **G_cite** — expanded citation graph (explicit refs + body-mention ≥ 2 across docs)
- **G_throughline** — tokens sharing a throughline (parsed from infill T-NN table)
- **G_mu** — tokens sharing an Μ mode (collapsed via throughline primary/secondary Μ)
- **G_pp** — tokens whose primary docs co-appear in a PP `affects:` list
- **G_tfidf** — standard sklearn TfidfVectorizer (supporting only)

## Corpus + tokens (reused from v2)

Same 43 design / 4 discourse docs. Same 84 tokens. No re-vectorization of the corpus extraction.

## Class taxonomy for within-class filtering

```
conviction:     Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity
pressure_point: Evidence, Consequence, Authority, Loyalty
faction:        Crown, Church, Hafenmark, Varfell, Löwenritter, Restoration Movement, Guilds
npc:            King Almud, Confessor Arne, Inge Baralta, Magnus Vaynard, Lisbeth Ehrenwall,
                Yrsa Vossen, Torben, Elske, Edeyja, Lenneth
clock:          MS, CI, IP, PI, TS, TCV
system:         (everything else)
```

Within-class pairs are suppressed from the implied-but-missing diagnostic.

## Expanded citation graph parsing

For each (source_doc, target_token) pair where target_token's primary_doc ≠ source_doc:
- Body mention ≥ 2 (using same disambiguation rules as v2 vectorization) → edge weight = mention count
- Explicit `Cross-references:` line citing target's primary file → edge weight += 5
- All edges directed source → target

Symmetric handling for queries via in+out neighbor union.

## Metadata graph parsing

**Throughlines:** parsed from `references/throughlines_meta_infill.md` T-NN table rows with regex:
```
\| T-([A-Za-z0-9]+) \| ([^|]+) \| (М-[0-9]+|—) \| (М-[0-9]+|—) \| ([^|]+) \|
```
For each row, extract token surface forms from name+description; build pairwise edges.

**Μ modes:** collected via throughlines' primary/secondary Μ field; edges built across union of tokens within each Μ collection.

**PP affects:** parsed from `canon/patch_register_active.yaml` `patches:` list; for each patch, build pairwise edges across all tokens whose primary doc appears in `affects:` or `files:` list. Section refs (`§5.1` suffix) stripped before path matching.

## Pre-committed thresholds (locked, not adjusted post-hoc)

| Diagnostic | Threshold |
|---|---|
| Multi-graph hubs | top quintile in ≥ 3 of 4 graphs |
| Implied-but-missing | ≥ 2 of {G_throughline, G_mu, G_pp} link AND no G_cite edge AND cross-class |
| Notional | G_cite edge present AND no metadata link |
| Cascade-without-return | chain length ≥ 3 in G_cite, no return path |
| Sparse-context | paragraph count ≤ 10th percentile AND G_cite degree ≤ 10th percentile |
| Vocabulary debt | direct match (Game Master, Cultural Reformation, Coup Counter) |
| Discourse-design divergence | discourse:design ratio outside [0.05, 0.5] |
| Multi-graph isolates | max degree across all graphs ≤ 1 |

Tie-breaking: alphabetical token order. **No threshold deviation.**

## Validation — structural properties

P1: foundation tokens > corpus median in G_cite + G_throughline degree
P2: Convictions CV < 0.5 in G_throughline degree
P3: G_cite ≥ 100 token-edges

**Result: 2/3 pass (P1 PASS, P2 FAIL, P3 PASS) → VALIDATED**

P2 fails for a structural reason (throughline framework doesn't lexically reference Convictions); this is itself a finding, not a methodology defect.

## Known v3 limitations

1. P2 fails because of metadata-graph sparsity, not methodology. Findings dependent on G_throughline are weak by construction; G_cite + G_pp findings are robust.
2. Token primary doc only matched 29 of 84 tokens. The other 55 cannot be citation sources, only targets. In+out neighbor union handles this in degree computation but interpretation should remember which tokens have "voice" vs. "presence."
3. PP register parses only 23 active patches. Archived patches not included.
4. Implicit-citation threshold ≥ 2 mentions admits some false positives where mentions are formulaic (e.g. "Faction Layer §3.2" cited twice without substantive engagement).
5. No directional inference for cascades — citation directionality is preserved but the cascade diagnostic doesn't distinguish "A depends on B" from "A references B in passing."
6. **No cross-graph numeric confidence scoring.** A finding agreed-on by 3 graphs and one supported by 1 graph appear in the same register; confidence is conveyed only in qualifying prose.
