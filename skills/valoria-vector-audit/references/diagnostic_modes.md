# Vector Audit — Diagnostic Modes Reference

Each mode is a self-contained query over the five graphs (G_cite, G_throughline, G_mu, G_pp, G_tfidf). Modes can be invoked individually after Stages 1-5 are complete; default is to run all 8. Thresholds are LOCKED in `methodology.md` §3.7. Example rows show shape only.

---

## Mode A — Multi-graph hubs

**Question:** Which tokens are top-quintile centrality across multiple structured views?

**Method:** For each of {G_cite, G_throughline, G_mu, G_pp}, compute degree per token using in+out neighbor union. Identify top quintile per graph. Tokens appearing in top quintile across ≥3 of 4 graphs are reported. Single-graph hubs are reported separately as supplementary.

**Output format:**
```
| Token | Cite | Throughline | Mu | PP | Note |
| Turmoil | 31 | 4 | 2 | 5 | Highest cross-validated centrality |
```

**Action recommended:** Multi-graph hubs are the highest change-impact propagation risk. Schedule explicit change-control review.

---

## Mode B — Implied-but-missing edges

**Question:** Which token pairs are linked by structured metadata but not by any explicit citation?

**Method:** For each cross-class pair (filtered by §3.4 class taxonomy), count metadata-graph links among {G_throughline, G_mu, G_pp}. If ≥2 metadata graphs link AND G_cite does not link, the pair is implied-but-missing. Sort by metadata link strength. Pairs at 1 metadata graph are reported separately at lower confidence.

**Output format:**
```
| Links | Strength | Token A | Token B |
|---|---|---|---|
| 3 | 12 | Turmoil | Faction Layer |
```

**Action recommended:** Add explicit cross-references between flagged pairs. The metadata says they're connected; the docs should too.

---

## Mode C — Notional edges

**Question:** Which citations exist with no structural metadata support?

**Method:** For each G_cite edge, check if metadata graphs (G_throughline, G_mu, G_pp) link the same pair. If none do, the edge is notional. Sort by G_cite weight.

**Output format:**
```
| Cite weight | Source → Target | Reading |
|---|---|---|
| 68 | Faction Layer → Stability | Heavy citation, no metadata coupling |
```

**Action recommended:** For a token recurring across the notional pairs, either add it to relevant throughlines (formalize the coupling) or downgrade citation visibility (prevent over-reliance on absent metadata).

---

## Mode D — Cascade-without-return

**Question:** What one-way pressure patterns exist in the citation graph?

**Method:** DFS through G_cite from each token; collect chains of length ≥3 with no return path to start node. Group by terminal token (downstream sink).

**Output format:**
```
| Terminal | Chains ending here | Note |
|---|---|---|
| Disposition | 391 | NO own file — concept buried in NPC Behavior + factions |
```

**Reading:** A foundational sink receives and does not reference scenes — correct by design. A sink with no own file is a buried concept.

**Action recommended:** Promote buried-concept sinks to first-class docs so they can cite back.

---

## Mode E — Sparse-context tokens

**Question:** Which tokens have minimal corpus footprint AND minimal citation degree?

**Method:** Compute paragraph count + G_cite in+out degree for each token. Tokens in bottom 10th percentile of BOTH are flagged.

**Output format:**
```
| Token | Para | Cite Deg | Status | Concern |
|---|---|---|---|---|
| Piety Track | 16 | 1 | canonical | Central mechanic, no own file |
```

**Action recommended:** Promote canonical concepts to first-class docs with their own files. Their absence from the citation graph isn't because they're unimportant — it's because they're buried.

---

## Mode F — Throughline orphan check

**Question:** Which throughlines lack textual substantiation in the design corpus?

**Method:** For each throughline, identify its load-bearing systems (from `references/throughlines_meta_infill.md` Load-bearing systems column; without it this mode is null). For each design corpus paragraph, count how many of those systems are mentioned. A paragraph counts as "substantiating" if ≥2 systems mentioned. Throughlines with ≤2 substantiating paragraphs are flagged.

**Output format:**
```
| Throughline | Load-bearing systems | Substantiating paragraphs |
|---|---|---|
| T-30 Information Asymmetry | scale_transitions, threadwork, faction_layer | 2 |
```

**Action recommended:** Throughlines with low substantiation either need design substance added OR should be marked as forward-looking (not yet implementable).

---

## Mode G — Vocabulary debt sweep

**Question:** What struck/legacy terminology still appears in active design docs?

**Method:** Parse `registers/supersession_register.yaml` for struck terms. Direct grep for each term across design corpus. Report paragraph count + doc-level concentration per term, counting occurrences inside STRUCK markers separately from live ones.

**Output format:**
```
| Term | Para | Docs | Concentration |
|---|---|---|---|
| Game Master | 17 | 3 | threadwork_v30 (12/17), npc_behavior_v30 (3/17), mass_battle_v30 (2/17) |
| Coup Counter | 10 | 7 | dispersed; needs design judgment for Graduated Autonomy substitution |
```

**Action recommended for concentrated debt:** Single-doc grep-replace cleanup. Where the successor term is not a 1:1 substitute (Coup Counter → Graduated Autonomy), decide per site.

**Action recommended for STRUCK markers:** LEAVE — they're intentional audit trail. Don't erase historical record of strikes.

---

## Mode H — Multi-graph isolates

**Question:** Which tokens are conceptually present but structurally disconnected from everything else?

**Method:** Compute degree per token in each of {G_cite, G_throughline, G_mu, G_pp}. Tokens with `max(degrees) ≤ 1` across all graphs are flagged.

**Output format:**
```
| Token | Cite | TL | Mu | PP | Status | Note |
|---|---|---|---|---|---|---|
| Wager | 1 | 0 | 0 | 0 | canonical | No own file; surface-form rare |
```

**Action recommended:** Same as Mode E — promote to first-class docs. Multi-graph isolation of canonical concepts means those concepts can't be discovered, vetted, or maintained as standalone units.

---

## Confidence scoring

Findings inherit confidence from how many graphs agree:

- **High:** Multiple graphs agree (Mode A multi-graph hubs; Mode B with ≥3 metadata graphs)
- **Medium:** Single graph plus context (Mode C notional with high cite weight; Mode D cascade with concerning terminal)
- **Low:** Single graph, sparse context (Mode E sparse tokens with rare context; Mode B with only 2 metadata graphs)
- **Conditional:** Validation outcome modifies all confidence levels (FAILED validation downgrades all findings to "leads, not verdicts")

Confidence is reported per-finding in the weakness register.
