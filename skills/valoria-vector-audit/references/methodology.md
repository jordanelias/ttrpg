# Vector Audit Methodology — v3 Multi-Graph Triangulation

## §1 Five graphs

The audit produces five structural graphs over the design corpus and surfaces findings via cross-graph agreement and disagreement.

| Graph | Source | What it captures |
|---|---|---|
| **G_cite** | Body mentions ≥2 + explicit `Cross-references:` + `see X.md` + PP `affects:` | Actual citation structure of the corpus |
| **G_throughline** | T-NN table in `references/throughlines_meta_infill.md`: tokens sharing a throughline | Tokens that participate in the same throughline |
| **G_mu** | Throughlines collapsed by primary/secondary Μ field; tokens within shared Μ collection | Tokens that share an Μ mode |
| **G_pp** | `registers/patch_register_active.yaml` `affects:` lists; tokens whose primary docs co-appear | Tokens touched by the same patch |
| **G_tfidf** | sklearn TfidfVectorizer over paragraphs (supporting only, not primary) | Lexical co-occurrence baseline |

**G_tfidf is supporting only.** Use it for cross-checking Mode A (multi-graph hubs) and Mode E (sparse-context), never for primary findings.

---

## §2 Diagnostic modes (8)

Modes A–H: definitions in `SKILL.md` Step 4, full specifications in `diagnostic_modes.md`, locked thresholds in §3.7.

---

## §3 Procedures

### §3.1 Corpus extraction with banner classifier

**Bypass index routing.** Read full files from the working tree. Index files lack the prose needed for citation graph extraction.

**Scope:** all `design_doc` and `params` paths from `references/canonical_sources.yaml`, plus `canon/00..03`, plus `references/throughlines_meta*.md`, plus key recent provisional design docs.

**Classifier per doc** (owner: `banner_classify()` in `scripts/vector_audit.py`; first match wins):
- `STATUS: CANONICAL` / `DESIGN` / `REFERENCE` / `CURRENT` / `WORKING` → **design corpus**
- `[STRUCK]` banner or `deprecated/` path → **excluded**
- `STATUS: PROVISIONAL` → **design corpus** (provisional design IS design, just unstable)
- `WORKPLAN` / `AUDIT` / `SESSION CLOSE` / `STRESS TEST` banner, or an `audit/` path (non-development_specification) → **discourse corpus**
- Default: design

Primary topology built from design corpus. Discourse corpus is overlay-only for Stage 7 (discourse/design ratio).

### §3.2 Token curation: seed + auto

**Seed list (~70 tokens):** every system from `canonical_sources.yaml` `systems:` block + every named NPC from `complete_systems_reference.md` Part 1.

**Auto-extract layer:** capitalized multi-word terms appearing in ≥3 design-corpus docs AND ≥10 paragraph mentions, filtered against stopword list (Renaissance proper nouns, project meta, common phrases, terms already in seed).

Auto-finds that pass review become tokens; ones that don't get added to stopword list for next run. Track which tokens are seed vs auto in `tokens.json`.

**Legacy terms** (parsed from `registers/supersession_register.yaml`) are added as auto with `status: gap` flag. They're not real tokens for analysis, just present so vocabulary debt mode (G) finds them.

### §3.3 Token deduplication

Pre-execution merges (known-coupled tokens that shouldn't pollute implied-missing):
- `Tensions Deck` is a strict subset of `Tensions` context — keep both, flag as known-coupled, suppress from implied-missing
- `MS` and `Mending Stability` merged via surface forms
- `CI` (clock) and `CI Political` (system) kept separate

### §3.4 Class taxonomy for within-class filtering

Tokens grouped into classes. Within-class pairs filtered from Mode B (implied-but-missing) — they're expected to score high and pollute the signal.

| Class | Members |
|---|---|
| **conviction** | Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity |
| **pressure_point** | Evidence, Consequence, Authority, Loyalty |
| **faction** | Crown, Church, Hafenmark, Varfell, Löwenritter, Restoration Movement, Guilds |
| **npc** | All named NPC tokens |
| **clock** | MS, CI, IP, PI, TS, TCV |
| **system** | Everything else |

### §3.5 Disambiguation rules

For tokens with English-word collisions, paragraphs MUST contain at least one context-window pattern to count:

| Token | Context patterns |
|---|---|
| Faith | `Conviction|Framework|Divine|Church|Cardinal|doctrine` |
| Order | `Conviction|Framework|Faith|Autonomy|Reason|Equity` |
| Reason | `Conviction|Faith|Order|Autonomy` |
| Equity | `Conviction|Restoration|RM|Distribut` |
| Precedent | `Conviction|Hafenmark|legal` |
| Autonomy | `Conviction|Varfell|Löwenritter` |
| Continuity | `Conviction|Restoration|RM` |
| Evidence | `Pressure Point|Investigation|Evidence Track` |
| Consequence | `Pressure Point|Consequentialist` |
| Authority | `Pressure Point|Authority Challenge|institutional` |
| Loyalty | `Pressure Point|Knot|relational|Disposition` |
| Crown | `Almud|faction|Mandate|Treaty|Torben` |
| Church | `Arne|Cardinal|Piety|Heresy|faction|Confessor|doctrine` |

### §3.6 Standard TF-IDF (supporting only)

```python
TfidfVectorizer(
    lowercase=False,
    token_pattern=r'(?u)\b\w[\w\-]+\b',
    min_df=2, max_df=0.5,
    sublinear_tf=True,
    norm='l2',
)
```

Per-token vector = sum of paragraph TF-IDF vectors weighted by token mention count, then L2 normalized. Cosine similarity matrix is `g_tfidf`.

**Uniform document weights.** Never weight documents by status; status filtering happens at the diagnostic level.

### §3.7 Pre-committed thresholds (LOCKED)

| Diagnostic | Threshold |
|---|---|
| Mode A multi-graph hubs | top quintile by degree in ≥ 3 of 4 graphs |
| Mode B implied-but-missing | ≥ 2 of {G_throughline, G_mu, G_pp} link AND no G_cite edge AND cross-class |
| Mode C notional | G_cite edge AND no metadata link |
| Mode D cascade-without-return | chain length ≥ 3 in G_cite, no return path |
| Mode E sparse-context | paragraph ≤ 10th percentile AND G_cite degree ≤ 10th percentile |
| Mode F throughline orphan | ≤ 2 substantiating paragraphs |
| Mode G vocabulary debt | direct match (parsed from supersession_register) |
| Mode H multi-graph isolates | max degree across all graphs ≤ 1 |

Tie-breaking: alphabetical token order. **No threshold deviation. No post-hoc tuning.** If signal is weaker than thresholds expect, that is a finding, not a tuning opportunity.

### §3.8 Validation — structural properties

Three properties checked. Methodology validates if ≥2 of 3 pass. None depend on prior groupings (avoiding circularity).

**P1 — Foundation periphery:** Foundation tokens (Self-Rendering, Leap, Coherence, Throughlines, Ein Sof) have HIGHER mean degree than corpus median, in BOTH G_cite and G_throughline.

**P2 — Conviction class symmetry (v4, ED-IN-0080):** The 7 Convictions show ≤50% coefficient of
variation in **context-gated prose presence** (the §3.5 disambiguation-gated `paragraph_count`).
Never measure it on G_throughline degree: `throughlines_meta_infill.md` routes all 7 through the
aggregate `conviction_track` slug, so that vector is all-zero by construction. Report the
per-conviction spread alongside the verdict, and disclose the gate's co-mention bias (context words
are partly other conviction names). An all-zero vector reports **NOT MEASURABLE**, never "maximally
asymmetric" (no `cv=999` sentinel); a not-measurable P2 does not count as a pass. Attribute-class
symmetry joins as a second probe on the same measure and bar only once the descriptor-registry
attribute roster is stable **and** the attributes have disambiguation contexts.

**P3 — Citation density smoke test:** G_cite has ≥100 token-edges. Lower = explicit-only parsing, structurally inadequate for filter use.

A failing property is reported as a finding, never tuned away.

---

## §4 Degree computation

**Use in+out neighbor union, never out-only.**

```python
def neighbors_union(graph, t):
    out_nbrs = set(graph.get(t, {}).keys())
    in_nbrs = set(src for src, tgts in graph.items() if t in tgts)
    return out_nbrs | in_nbrs

deg_cite = {t: len(neighbors_union(g_cite, t)) for t in token_names}
```

Tokens without primary docs cannot be citation sources, so out-only computation gives them artificial degree 0; in+out counts them as citation TARGETS.

Metadata graphs (G_throughline, G_mu, G_pp) are constructed symmetrically, so out=in=union.

---

## §5 Output structure

The run folder's top-level files are listed in `SKILL.md` Step 5. The `data/` that `write_outputs()` writes:

```
data/
├── corpus_manifest.json
├── tokens.json
├── g_cite.json
├── g_metadata.json
├── degrees.json
├── validation.json
└── multigraph_diagnostics.json
```

---

## §6 What this can't find

1. **Conceptual relationships not lexically encoded.** The throughlines framework relates systems conceptually but the framework's text doesn't always say the system names. Lexical methods can't bridge this gap — hand-curation is the only way.
2. **Quality of design within a system.** The audit measures connectivity, centrality, citation density — not whether a system's internal design is sound.
3. **Latent design dependencies.** Two systems coupled by shared design assumptions without ever co-occurring or cross-citing are invisible.
4. **Implementation order optimality.** Centrality findings suggest ordering, but the audit doesn't direction-disambiguate citations or capture true dependencies.
5. **Vetting quality of the corpus's hubs.** Identifies what's central, doesn't verify it's correct.

---

## §7 What may and may not be relaxed

Never relax a §3 procedure without first knowing the failure it prevents (`SKILL.md` Common Failure
Modes; `v1_v2_v3_history.md` for what is locked outright).
