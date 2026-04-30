# Vector Audit — Diagnostic Modes Reference

Each mode is a self-contained query over the five graphs (G_cite, G_throughline, G_mu, G_pp, G_tfidf). Modes can be invoked individually after Stages 1-5 are complete; default is to run all 8.

---

## Mode A — Multi-graph hubs

**Question:** Which tokens are top-quintile centrality across multiple structured views?

**Method:** For each of {G_cite, G_throughline, G_mu, G_pp}, compute degree per token using in+out neighbor union. Identify top quintile per graph. Tokens appearing in top quintile across ≥3 of 4 graphs are reported.

**Output format:**
```
| Token | Cite | Throughline | Mu | PP | Note |
| Peninsular Strain | 31 | 4 | 2 | 5 | Highest cross-validated centrality |
```

**v3 reference run finding:** Peninsular Strain + IP were the only multi-graph hubs at ≥3/4 graphs. Single-graph cite hubs (top 17): NPC Behavior (56), CI (46), Settlement Layer (41), etc. — these are reported separately as supplementary because v3 P2 fail meant G_throughline was sparse.

**Action recommended:** Multi-graph hubs are the highest change-impact propagation risk. Schedule explicit change-control review.

---

## Mode B — Implied-but-missing edges

**Question:** Which token pairs are linked by structured metadata but not by any explicit citation?

**Method:** For each cross-class pair (filtered by §3.4 class taxonomy), count metadata-graph links among {G_throughline, G_mu, G_pp}. If ≥2 metadata graphs link AND G_cite does not link, the pair is implied-but-missing. Sort by metadata link strength.

**Output format:**
```
| Links | Strength | Token A | Token B |
|---|---|---|---|
| 3 | 12 | Peninsular Strain | Faction Layer |
```

**v3 reference run finding:** 3 pairs at ≥2 metadata graphs. (Many more at 1 metadata graph — those are reported separately at lower confidence.)

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

**v3 reference run finding:** Top 15 notional pairs revealed CI as largest implicit hub with no metadata coupling — appearing in 9 of top 15 notional pairs.

**Action recommended:** Either add CI to relevant throughlines (formalize the coupling) or downgrade citation visibility (prevent over-reliance on absent metadata).

---

## Mode D — Cascade-without-return

**Question:** What one-way pressure patterns exist in the citation graph?

**Method:** DFS through G_cite from each token; collect chains of length ≥3 with no return path to start node. Group by terminal token (downstream sink).

**Output format:**
```
| Terminal | Chains ending here | Note |
|---|---|---|
| Threadwork | 487 | Foundation — receives, doesn't reference scenes (correct by design) |
| Disposition | 391 | NO own file — concept buried in NPC Behavior + factions |
```

**v3 reference run finding:** Top sinks were correctly foundational (Threadwork, Coherence, Stability, MS). Concerning sinks: Disposition (no own file) + Domain Action (no own file) — buried concepts.

**Action recommended:** Promote buried-concept sinks to first-class docs so they can cite back.

---

## Mode E — Sparse-context tokens

**Question:** Which tokens have minimal corpus footprint AND minimal citation degree?

**Method:** Compute paragraph count + G_cite in+out degree for each token. Tokens in bottom 10th percentile of BOTH are flagged.

**Output format:**
```
| Token | Para | Cite Deg | Status | Concern |
|---|---|---|---|---|
| Conviction Track | 16 | 1 | canonical | Central mechanic, no own file |
| Wager | 4 | 1 | canonical | Mechanic exists, surface-form coverage low |
```

**v3 reference run finding:** 14 multi-graph isolates. Concerning subset: 5 of 7 Convictions, 3 of 4 Pressure Points, Conviction Track itself — all canonical concepts living inline in NPC Behavior.

**Action recommended:** Promote canonical concepts to first-class docs with their own files. Their absence from the citation graph isn't because they're unimportant — it's because they're buried.

---

## Mode F — Throughline orphan check

**Question:** Which throughlines lack textual substantiation in the design corpus?

**Method:** For each throughline, identify its load-bearing systems (from `references/throughlines_meta_infill.md` Load-bearing systems column, added by PP-677). For each design corpus paragraph, count how many of those systems are mentioned. A paragraph counts as "substantiating" if ≥2 systems mentioned. Throughlines with ≤2 substantiating paragraphs are flagged.

**Output format:**
```
| Throughline | Load-bearing systems | Substantiating paragraphs |
|---|---|---|
| T-30 Information Asymmetry | scale_transitions, threadwork, faction_layer | 2 |
```

**Pre-PP-677:** This mode was null because the Load-bearing systems column didn't exist; the table description was too terse for lexical extraction. Future runs benefit from the column.

**Action recommended:** Throughlines with low substantiation either need design substance added OR should be marked as forward-looking (not yet implementable).

---

## Mode G — Vocabulary debt sweep

**Question:** What struck/legacy terminology still appears in active design docs?

**Method:** Parse `canon/supersession_register.yaml` for struck terms. Direct grep for each term across design corpus. Report paragraph count + doc-level concentration per term.

**Output format:**
```
| Term | Para | Docs | Concentration |
|---|---|---|---|
| Game Master | 17 | 3 | threadwork_v30 (12/17), npc_behavior_v30 (3/17), mass_battle_v30 (2/17) |
| Cultural Reformation | 17 | 5 | peninsular_strain_v30 (10/17), 14 in STRUCK markers |
| Coup Counter | 10 | 7 | dispersed; needs design judgment for Graduated Autonomy substitution |
```

**v3 reference run finding:** 3 legacy terms (Game Master, Cultural Reformation, Coup Counter) in 14 distinct docs. Concentration matters: Game Master 11/16 in single doc → single-doc grep-replace handles 69%.

**Action recommended for concentrated debt:** Single-doc grep-replace cleanup. PP-678 demonstrated workflow for Game Master + active CR. Coup Counter needs design judgment per site (substitution to Graduated Autonomy is not 1:1).

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

**v3 reference run finding:** 14 multi-graph isolates. Mostly canonical concepts buried in parent docs (Conviction Track, the 7 Convictions, the 4 Pressure Points, Wager, Thread Revelation).

**Action recommended:** Same as Mode E — promote to first-class docs. Multi-graph isolation of canonical concepts means those concepts can't be discovered, vetted, or maintained as standalone units.

---

## Confidence scoring

Findings inherit confidence from how many graphs agree:

- **High:** Multiple graphs agree (Mode A multi-graph hubs; Mode B with ≥3 metadata graphs)
- **Medium:** Single graph plus context (Mode C notional with high cite weight; Mode D cascade with concerning terminal)
- **Low:** Single graph, sparse context (Mode E sparse tokens with rare context; Mode B with only 2 metadata graphs)
- **Conditional:** Validation outcome modifies all confidence levels (FAILED validation downgrades all findings to "leads, not verdicts")

Confidence is reported per-finding in the weakness register.
