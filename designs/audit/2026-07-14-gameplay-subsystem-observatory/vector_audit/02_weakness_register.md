# Weakness register — vector audit v3 (leads, not verdicts)

Corpus: 110 design docs, 176 tokens. Validation: **FAILED** (1/3). Confidence inherits from validation (methodology §3.8).

**Coverage disclosure (capstone #6):** this L0 layer is a CURATED slice — 110 design docs = 10.3% of the 1071 `.md` under `designs/`, and only 6.3% of the repo's 1758 `.md` files. Everything outside `_canonical_paths()` (most of `designs/`, all of `params/`/`sim/`/`tests/`/`canon/` prose) is structurally invisible to L0 — a green result here is NOT whole-repo coverage.
Scorecard: cite-edges=9575, hubs=6, implied-missing=34, notional=25, sparse=11, isolates=3, vocab-debt-terms=3.

## Mode A — multi-graph hubs (highest change-impact)
- **Baralta** — top-quintile in 3/4 (cite 124, tl 4, mu 12, pp 0)
- **Conflict Architecture** — top-quintile in 3/4 (cite 107, tl 10, mu 21, pp 9)
- **Factions** — top-quintile in 3/4 (cite 135, tl 14, mu 21, pp 0)
- **Settlement Layer** — top-quintile in 3/4 (cite 117, tl 10, mu 23, pp 0)
- **Territories** — top-quintile in 3/4 (cite 149, tl 7, mu 21, pp 0)
- **Threadwork** — top-quintile in 3/4 (cite 135, tl 18, mu 25, pp 0)

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
- Conflict Architecture ↔ Faction Succession Split (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Leap Mechanism (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Tensions Deck (2 metadata graphs, 0 cite)
- Conviction Track ↔ Derived Stats (2 metadata graphs, 0 cite)
- Derived Stats ↔ Self-Rendering (2 metadata graphs, 0 cite)
- Derived Stats ↔ Solmund (2 metadata graphs, 0 cite)
- Faction Layer ↔ Mass Combat (2 metadata graphs, 0 cite)
- Faction Layer ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Faction Succession Split ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Factions ↔ MS Trajectory (2 metadata graphs, 0 cite)

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

## Mode D — cascade sinks (one-way "black holes")
- **Territories** — 201 chains terminate here
- **Church** — 200 chains terminate here
- **Stability** — 191 chains terminate here
- **Threadwork** — 190 chains terminate here
- **Crown** — 189 chains terminate here
- **Varfell** — 188 chains terminate here
- **Restoration Movement** — 188 chains terminate here
- **Hafenmark** — 186 chains terminate here
- **Wardens** — 184 chains terminate here
- **Conviction** — 183 chains terminate here
- **Mandate** — 178 chains terminate here
- **Einhir** — 175 chains terminate here
- **TS** — 173 chains terminate here
- **Löwenritter** — 171 chains terminate here
- **Altonia** — 170 chains terminate here

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
- MS Trajectory (6 paras, cite-deg 19, canonical)

## Mode F — throughline orphans (≤2 substantiating paragraphs)
- T-10 — 0 subst. (—)

## Mode G — vocabulary debt (struck terms still present)
- **Coup Counter** — 57 in 13 docs (top: designs/arcs/arc_expansion_v30.md)
- **Cultural Reformation** — 23 in 9 docs (top: designs/provincial/peninsular_strain_v30.md)
- **Game Master** — 21 in 8 docs (top: designs/arcs/throughline_resolutions_v30.md)

## Mode H — multi-graph isolates (structurally disconnected)
- Body (cite 0, tl 0, mu 0, pp 0, canonical)
- NPC Relational Graph (cite 0, tl 0, mu 0, pp 0, canonical)
- Territory Temperaments (cite 0, tl 0, mu 0, pp 0, canonical)
