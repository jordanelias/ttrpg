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

**G_tfidf is supporting only.** v3's central pivot from v2 was demoting TF-IDF from primary to supporting role. Use it for cross-checking Mode A (multi-graph hubs) and Mode E (sparse-context), never for primary findings.

---

## §2 Diagnostic modes (8)

See `diagnostic_modes.md` for full specifications. Brief:

- A. Multi-graph hubs (top quintile in ≥3 of 4)
- B. Implied-but-missing (≥2 metadata graphs link, G_cite doesn't, cross-class)
- C. Notional edges (G_cite present, no metadata)
- D. Cascade-without-return (G_cite chains length ≥3, no return)
- E. Sparse-context (paragraph ≤10th percentile AND cite degree ≤10th percentile)
- F. Throughline orphan (≤2 substantiating paragraphs per throughline)
- G. Vocabulary debt (direct grep for known-struck terms)
- H. Multi-graph isolates (max degree ≤1 across all graphs)

---

## §3 Procedures

### §3.1 Corpus extraction with banner classifier

**Bypass index routing.** Direct GitHub Contents API for full body content. Index files lack the prose needed for citation graph extraction.

**Scope:** all `design_doc` and `params` paths from `references/canonical_sources.yaml`, plus `canon/00..03`, plus `references/throughlines_meta*.md`, plus key recent provisional design docs.

**Classifier per doc:**
- `STATUS: CANONICAL` or `STATUS: DESIGN` → **design corpus**
- `STATUS: PROVISIONAL` → **design corpus** (provisional design IS design, just unstable)
- `[STRUCK]` banner or `deprecated/` path → **excluded**
- `STATUS: AUDIT` / `STATUS: SESSION` / `WORKPLAN` / file in `designs/audit/*-session/` (non-development_specification) → **discourse corpus**
- Default: design

Primary topology built from design corpus. Discourse corpus is overlay-only for Mode 2.9 (discourse/design ratio).

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

**Document weighting from v2 (1.0/0.7/0.3 by status) is DROPPED.** v3 uses uniform weights; status filtering happens at the diagnostic level. The weights were arbitrary and never validated.

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

**P2 — Conviction class symmetry:** The 7 Convictions show ≤50% coefficient of variation in G_throughline degree. (Tests whether the throughline framework treats Convictions symmetrically.)

**P3 — Citation density smoke test:** G_cite has ≥100 token-edges. Lower = explicit-only parsing, structurally inadequate for filter use.

**Validation FAILED** (P2 specifically) was itself a finding in v3: throughlines lack lexical anchoring of Convictions. PP-677 added Load-bearing systems column to address — future runs should re-test P2 with the new column data.

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

Tokens without primary docs (~55 of 84 in v3 run) cannot be citation sources. Out-only computation gives them artificial degree 0. In+out reveals their actual centrality from being citation TARGETS.

Metadata graphs (G_throughline, G_mu, G_pp) are constructed symmetrically, so out=in=union.

---

## §5 Output structure

Audit folder: `designs/audit/{date}-{audit-name}/`

```
00_workplan.md          # config + pre-committed thresholds (this run)
01_methodology.md       # executed parameters; what changed from prior runs
02_weakness_register.md # PRIMARY DELIVERABLE — narrative findings
03_validation_report.md # P1/P2/P3 results
data/
├── corpus_manifest.json
├── corpus_design.json
├── corpus_discourse.json
├── tokens.json
├── auto_candidates.json
├── pilot.json
├── g_cite.json
├── g_metadata.json
├── g_tfidf.npz
├── validation.json
├── degrees.json
└── multigraph_diagnostics.json
```

---

## §6 What this can't find

1. **Conceptual relationships not lexically encoded.** The throughlines framework relates systems conceptually but the framework's text doesn't always say the system names. Lexical methods can't bridge this gap — hand-curation is the only way. PP-677 partially addresses by formalizing system-token coupling.
2. **Quality of design within a system.** The audit measures connectivity, centrality, citation density — not whether a system's internal design is sound.
3. **Latent design dependencies.** Two systems coupled by shared design assumptions without ever co-occurring or cross-citing are invisible.
4. **Implementation order optimality.** Centrality findings suggest ordering, but the audit doesn't direction-disambiguate citations or capture true dependencies.
5. **Vetting quality of the corpus's hubs.** Identifies what's central, doesn't verify it's correct.

---

## §7 v1 → v2 → v3 lessons embedded in this methodology

The methodology above is not "the way to do it" — it's "the way that works after v1 and v2 failed." Lessons baked in:

- **v1 (TF-IDF only, no validation gate):** produced findings that turned out to be artifacts. v2 added validation; v3 made validation structural.
- **v2 (TF-IDF primary, k-NN Jaccard validation):** validation FAILED (Jaccard 0.222), but the threshold itself was unsatisfiable for small expected_groups, so the failure was partly a methodology defect not a corpus problem. v3 replaced k-NN Jaccard with structural properties.
- **v2 threshold deviation (cosine 0.35 → 0.20 post-hoc):** invalidated those findings. v3 LOCKS thresholds.
- **v2 within-class clustering pollution:** Top 8 of 103 implied-missing pairs were within-class artifacts. v3 §3.4 class taxonomy filters them.
- **v2 out-degree-only:** produced "faction/NPC/Conviction-as-hub" finding that was a paragraph-breadth artifact. v3 in+out union corrects.
- **v2 sparse citation graph:** 11 token-edges; "no citation" was trivially true for nearly any pair. v3 implicit ≥2 mention threshold gives 421 edges.
- **v2 unconventional paragraph-IDF:** undefended; v3 uses standard sklearn.
- **v2 arbitrary document weights (1.0/0.7/0.3):** dropped in v3; uniform weighting.

The lessons are why these procedural choices look the way they do. Don't relax them without understanding why each was tightened.
