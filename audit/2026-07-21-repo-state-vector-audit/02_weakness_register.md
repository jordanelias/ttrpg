# Weakness register — vector audit v3 (leads, not verdicts)

Corpus: 110 design docs, 176 tokens. Validation: **FAILED** (1/3). Confidence inherits from validation (methodology §3.8).

**Coverage disclosure (capstone #6):** this L0 layer is a CURATED slice — 110 design docs = only 6.0% of the repo's 1821 `.md` files. Everything outside `_canonical_paths()` (most of `systems/`, all of `engine/params/`/`sim/`/`tests/`/`canon/` prose not named in `canonical_sources.yaml`) is structurally invisible to L0 — a green result here is NOT whole-repo coverage.
Scorecard: cite-edges=9582, hubs=6, implied-missing=32, notional=9423, cascade-sinks=164, sparse=11, isolates=3, vocab-debt-terms=3.

## Mode A — multi-graph hubs (highest change-impact)
- **Baralta** — top-quintile in 3/4 (cite 125, tl 4, mu 12, pp 0)
- **Factions** — top-quintile in 3/4 (cite 137, tl 14, mu 21, pp 0)
- **Settlement Layer** — top-quintile in 3/4 (cite 117, tl 10, mu 23, pp 0)
- **Territories** — top-quintile in 3/4 (cite 150, tl 7, mu 21, pp 0)
- **Threadwork** — top-quintile in 3/4 (cite 134, tl 18, mu 25, pp 0)
- **Victory** — top-quintile in 3/4 (cite 114, tl 11, mu 23, pp 0)

## Mode B — implied-but-missing (metadata links, no citation)
- CI Political ↔ Clocks (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Faction Layer (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Clocks ↔ Faction Layer (2 metadata graphs, 0 cite)
- Clocks ↔ MS Trajectory (2 metadata graphs, 0 cite)
- Clocks ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Clocks ↔ Royal Assassination Fuse (2 metadata graphs, 0 cite)
- Clocks ↔ Threadwork (2 metadata graphs, 0 cite)
- Clocks ↔ Victory (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Leap Mechanism (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Tensions Deck (2 metadata graphs, 0 cite)
- Conviction Track ↔ Derived Stats (2 metadata graphs, 0 cite)
- Derived Stats ↔ Self-Rendering (2 metadata graphs, 0 cite)
- Derived Stats ↔ Solmund (2 metadata graphs, 0 cite)
- Faction Layer ↔ Mass Combat (2 metadata graphs, 0 cite)
- Faction Layer ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Factions ↔ MS Trajectory (2 metadata graphs, 0 cite)
- Factions ↔ Miraculous Event (2 metadata graphs, 0 cite)
- MS Trajectory ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- … 12 more (see `data/multigraph_diagnostics.json`)

## Mode C — notional edges (cited, no metadata support)
- CI Political → Crown (cite weight 183)
- Inge Baralta → Crown (cite weight 183)
- Torben → Crown (cite weight 183)
- Church → Crown (cite weight 183)
- Hafenmark → Crown (cite weight 183)
- Varfell → Crown (cite weight 183)
- Löwenritter → Crown (cite weight 183)
- Guilds → Crown (cite weight 183)
- Standing → Crown (cite weight 183)
- Baralta → Crown (cite weight 183)
- Conviction Track → Crown (cite weight 183)
- Factions → Crown (cite weight 183)
- NPC Roster → Crown (cite weight 183)
- Aldric Tormann → Crown (cite weight 183)
- Cardinal Arnlod Olafsson → Crown (cite weight 183)
- Cardinal Osten Jarnstal → Crown (cite weight 183)
- Duchess Inge Baralta → Crown (cite weight 183)
- Gerik Strand → Crown (cite weight 183)
- Maret Uln → Crown (cite weight 183)
- Peder Almstedt → Crown (cite weight 183)
- … 9403 more (see `data/multigraph_diagnostics.json`)

## Mode D — cascade sinks (one-way "black holes")
- **Territories** — 166 chains terminate here
- **Church** — 165 chains terminate here
- **Threadwork** — 163 chains terminate here
- **Stability** — 162 chains terminate here
- **Crown** — 156 chains terminate here
- **Varfell** — 155 chains terminate here
- **Restoration Movement** — 153 chains terminate here
- **Hafenmark** — 152 chains terminate here
- **Conviction** — 151 chains terminate here
- **Wardens** — 150 chains terminate here
- **Mandate** — 147 chains terminate here
- **Einhir** — 142 chains terminate here
- **TS** — 139 chains terminate here
- **Factions** — 138 chains terminate here
- **Order** — 138 chains terminate here
- … 149 more (see `data/multigraph_diagnostics.json`)

## Mode E — sparse-context tokens (gapped regions)
- Body (0 paras, cite-deg 0, canonical)
- NPC Relational Graph (0 paras, cite-deg 0, canonical)
- Territory Temperaments (0 paras, cite-deg 0, canonical)
- Fractional Province (1 paras, cite-deg 23, provisional)
- Mind (1 paras, cite-deg 13, canonical)
- Propagation Spec (1 paras, cite-deg 13, canonical)
- Event Impact Matrix (2 paras, cite-deg 13, provisional)
- Holonic Container Doctrine (2 paras, cite-deg 11, canonical)
- Armature System (3 paras, cite-deg 3, provisional)
- Thread Horizontal Integration (4 paras, cite-deg 3, canonical)
- MS Trajectory (6 paras, cite-deg 20, canonical)

## Mode F — throughline orphans (≤2 substantiating paragraphs)
- T-10 — 0 subst. (—)

## Mode G — vocabulary debt (struck terms still present)
- **Coup Counter** — 57 in 13 docs (top: arcs/arc_expansion_v30.md)
- **Cultural Reformation** — 23 in 9 docs (top: systems/overview/peninsular_strain_v30.md)
- **Game Master** — 21 in 8 docs (top: arcs/throughline_resolutions_v30.md)

## Mode H — multi-graph isolates (structurally disconnected)
- Body (cite 0, tl 0, mu 0, pp 0, canonical)
- NPC Relational Graph (cite 0, tl 0, mu 0, pp 0, canonical)
- Territory Temperaments (cite 0, tl 0, mu 0, pp 0, canonical)

---

## §Disposition (forward-only discipline — SKILL.md)

**Validation FAILED (1/3).** Every finding below is a **lead, not a verdict** — none is
autonomously actioned; none allocates an `ED-<LANE>-NNNN` this run. Dispositions record
whether a lead is (a) corroborating a known open item, (b) an artifact, or (c) a candidate
follow-up deferred to Jordan / the owning lane.

| Mode / finding | Disposition |
|---|---|
| **Validation P1/P2** (foundation-periphery; convictions absent from throughline table, degrees all 0) | **Lead — deferred.** P2's zero conviction-throughline degree is genuine per methodology §3.8: only the aggregate *Conviction Track* appears in `throughlines_meta_infill.md`'s load-bearing column, not the 7 individual conviction axes. Could be nomenclature (axis names ≠ table system names) or a real wiring gap. No action — flagged for a WR/methodology review, not a fabricated fix. |
| **Mode A — hubs** (Baralta, Factions, Settlement Layer, Territories, Threadwork, Victory) | **No action — working as intended.** Expected high centrality for the strategic-layer spine; informational, not debt. |
| **Mode B — implied-missing** (32 cross-class pairs, e.g. Clocks↔Threadwork/Victory, Campaign Architecture↔Faction Layer) | **Lead — deferred.** Candidate cross-reference authoring; corroborates that `engine_clock` (`Clocks`) is under-cited — see Mode E / ED-1051. Deferred to owning lanes; no new ED. |
| **Mode C — notional** (9423, dominated by `* → Crown (weight 183)`) | **No action — artifact.** The uniform weight-183 fan-in to `Crown` is a single dense-doc co-occurrence signature, not 9423 discrete stale refs. Low confidence under FAILED validation; not real per-pair debt. |
| **Mode D — cascade sinks** (164; top: Territories, Church, Threadwork, Stability, Crown) | **No action pending review.** The top sinks are aggregation targets — terminal by design at the strategic layer. Re-examine only if a specific chain is expected to feed back. |
| **Mode E — sparse-context** (Propagation Spec 1 para/cite-deg 13; Body/Mind; Fractional Province) | **Lead — corroborates open item.** *Propagation Spec* sparsity tracks the **already-open T0 blocker ED-1051** (engine_clock ratification target). Body/Mind are the known "IN FLUX" derived-stat aggregates (CLAUDE.md §5). No new ED — folds into existing work. |
| **Mode F — throughline orphan** (T-10, 0 substantiating paras) | **Lead — deferred.** Candidate throughline substantiation; deferred to WR lane. |
| **Mode G — vocabulary debt** (Cultural Reformation 23/9 docs — *struck* in supersession register; Game Master 21/8; Coup Counter 57/13) | **Candidate follow-up — deferred to Jordan.** Only *Cultural Reformation* is formally struck; its hits concentrate in `systems/overview/peninsular_strain_v30.md`. *Game Master* / *Coup Counter* are legacy-but-not-formally-struck and sit mostly in `arcs/` generated narrative + superseded `combat_v30`. Concentrated single-doc grep-replace is the workflow (methodology §7), but touches narrative/historical content — **not** auto-edited here. Recommend a scoped WR/IN cleanup ED if Jordan wants it. |
| **Mode H — isolates** (Body, NPC Relational Graph, Territory Temperaments — degree ≤1 in every graph) | **Lead — corroborates known gap.** Canonical concepts lacking first-class doc homes; overlaps the descriptor-schema-in-flux (CLAUDE.md §5). No new ED — leads for eventual doc authoring. |
| **INSTR-1** — Step-1 input `designs/architecture/complete_systems_reference.md` was a retired path (silently `missing`, 1 input under-read) | **FIXED this run.** Repointed to `systems/_architecture/complete_systems_reference.md` in `vector_audit.py` + SKILL.md Step 1. |
| **INSTR-2** — coverage disclosure divided by a `designs/`-glob (retired → 0 files), printing "0.0% of 0 `.md`" | **FIXED this run.** Denominator is now the whole-repo `.md` count (curated slice = 6.0% of 1821). |

**Net:** 0 blocking findings. 2 instrument bugs fixed. All corpus findings are leads under FAILED
validation; the actionable-but-deferred ones are the Mode G vocab cleanup (Jordan's call) and the
convictions-vs-throughline P2 gap. Mode E/H corroborate the already-tracked ED-1051 / derived-stat-flux work.
