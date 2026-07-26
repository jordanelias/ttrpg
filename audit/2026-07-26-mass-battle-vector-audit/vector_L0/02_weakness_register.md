# Weakness register — vector audit v3 (structural findings)

Corpus: 110 design docs, 275 tokens. Validation: **VALIDATED** (2/3). Confidence inherits from validation (methodology §3.8).

**Coverage disclosure (capstone #6):** layer **L0** traces 110 design docs = 5.9% of the repo's 1871 `.md` files — the curated `canonical_sources.yaml` slice — most of `systems/`, all of `engine/`/`sim/`/`tests/`/`canon/` prose not named there is invisible. A green result at this layer is NOT whole-repo coverage. Run `--layer L1` to extend the CITE trace across the whole design tree (L0 stays the validated default; L1 does NOT re-validate).

**Direction disclosure:** Directions this tool does not trace at any layer: non-.md content (sim .py, typed engine/params values) and registry-absent tokens. (The engine Key-propagation graph IS traced now — build_g_key, Direction #5 — as a 5th structural graph.)
Scorecard: cite-edges=15099, hubs=16, implied-missing=35, notional=14662, cascade-sinks=234, sparse=16, isolates=9, vocab-debt-terms=3.
⚠ Mode D reachability hit its traversal cap on 51459 call(s) — some cascade-sinks may be cap artifacts, not true sinks (denser corpus / L1). Treat cascade-sinks as leads here.

## Mode A — multi-graph hubs (highest change-impact)
- **Peninsular Strain** — top-quintile in 4/4 (cite 151, tl 19, mu 23, pp 0)
- **Settlement Layer** — top-quintile in 4/4 (cite 157, tl 16, mu 23, pp 0)
- **Threadwork** — top-quintile in 4/4 (cite 185, tl 24, mu 25, pp 0)
- **Conflict Architecture** — top-quintile in 3/4 (cite 128, tl 10, mu 21, pp 13)
- **Conviction Track** — top-quintile in 3/4 (cite 144, tl 12, mu 23, pp 0)
- **Domain Actions** — top-quintile in 3/4 (cite 150, tl 0, mu 0, pp 13)
- **Duchess Inge Baralta** — top-quintile in 3/4 (cite 160, tl 4, mu 12, pp 0)
- **Factions** — top-quintile in 3/4 (cite 184, tl 14, mu 21, pp 0)
- **Mass Battle** — top-quintile in 3/4 (cite 147, tl 8, mu 0, pp 0)
- **Mass Combat** — top-quintile in 3/4 (cite 147, tl 9, mu 23, pp 0)
- **Miraculous Event** — top-quintile in 3/4 (cite 46, tl 4, mu 12, pp 0)
- **NPC Behavior** — top-quintile in 3/4 (cite 152, tl 11, mu 0, pp 0)
- **Player Agency** — top-quintile in 3/4 (cite 137, tl 8, mu 0, pp 13)
- **Social Contest** — top-quintile in 3/4 (cite 153, tl 6, mu 0, pp 0)
- **Territories** — top-quintile in 3/4 (cite 202, tl 7, mu 21, pp 0)
- **Victory** — top-quintile in 3/4 (cite 149, tl 17, mu 23, pp 0)

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
- Conviction Track ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Derived Stats ↔ Self-Rendering (2 metadata graphs, 0 cite)
- Derived Stats ↔ Solmund (2 metadata graphs, 0 cite)
- Faction Layer ↔ Mass Combat (2 metadata graphs, 0 cite)
- Faction Layer ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Factions ↔ MS Trajectory (2 metadata graphs, 0 cite)
- Factions ↔ Miraculous Event (2 metadata graphs, 0 cite)
- … 15 more (see `data/multigraph_diagnostics.json`)

## Mode C — notional edges (cited, no metadata support)
- Aldric Tormann → Crown (cite weight 183)
- CI Political → Crown (cite weight 183)
- Cardinal Arnlod Olafsson → Crown (cite weight 183)
- Cardinal Osten Jarnstal → Crown (cite weight 183)
- Church → Crown (cite weight 183)
- Conviction Track → Crown (cite weight 183)
- Duchess Inge Baralta → Crown (cite weight 183)
- Einhir → Crown (cite weight 183)
- Factions → Crown (cite weight 183)
- Gerik Strand → Crown (cite weight 183)
- Guilds → Crown (cite weight 183)
- Hafenmark → Crown (cite weight 183)
- Key: scene.witness → Crown (cite weight 183)
- Key: state.succession → Crown (cite weight 183)
- Löwenritter → Crown (cite weight 183)
- Maret Uln → Crown (cite weight 183)
- NPC Roster → Crown (cite weight 183)
- Peder Almstedt → Crown (cite weight 183)
- Prince Torben Almqvist → Crown (cite weight 183)
- Riskbreaker → Crown (cite weight 183)
- … 14642 more (see `data/multigraph_diagnostics.json`)

## Mode D — cascade sinks (one-way "black holes")
- **Audit** — 792 chains terminate here
- **Territories** — 747 chains terminate here
- **Key: mechanical.accounting** — 682 chains terminate here
- **Threadwork** — 676 chains terminate here
- **Knot** — 663 chains terminate here
- **Conviction** — 639 chains terminate here
- **Mass Battle** — 612 chains terminate here
- **Mass Combat** — 612 chains terminate here
- **Disposition** — 609 chains terminate here
- **Restoration Movement** — 601 chains terminate here
- **Church** — 597 chains terminate here
- **Social Contest** — 592 chains terminate here
- **NPC Behavior** — 581 chains terminate here
- **Stability** — 579 chains terminate here
- **Altonia** — 576 chains terminate here
- … 219 more (see `data/multigraph_diagnostics.json`)

## Mode E — sparse-context tokens (gapped regions)
- Active Inquisition (0 paras, cite-deg 0, canonical)
- Body (0 paras, cite-deg 0, canonical)
- Counter-Intelligence (0 paras, cite-deg 0, canonical)
- Game Director (0 paras, cite-deg 6, canonical)
- Key: mechanical.scene_exited (0 paras, cite-deg 0, canonical)
- Key: mechanical.scene_skipped (0 paras, cite-deg 0, canonical)
- Key: scene_outcome.battle_concluded (0 paras, cite-deg 0, canonical)
- NPC Relational Graph (0 paras, cite-deg 0, canonical)
- Scene Timer (0 paras, cite-deg 6, canonical)
- Territorial Piety (0 paras, cite-deg 0, canonical)
- Territory Temperaments (0 paras, cite-deg 0, canonical)
- faction Mandate (cross-module → faction_state) (0 paras, cite-deg 0, canonical)
- faction Treasury income (cross-module → faction_state) (0 paras, cite-deg 0, canonical)
- Fieldwork Knots (1 paras, cite-deg 16, canonical)
- Fractional Province (1 paras, cite-deg 23, provisional)
- Mind (1 paras, cite-deg 12, canonical)

## Mode F — throughline orphans (≤2 substantiating paragraphs)
(none)

## Mode G — vocabulary debt (struck terms still present)
- **Coup Counter** — 57 in 13 docs (top: arcs/arc_expansion_v30.md)
- **Cultural Reformation** — 23 in 9 docs (top: systems/overview/peninsular_strain_v30.md)
- **Game Master** — 21 in 8 docs (top: arcs/throughline_resolutions_v30.md)

## Mode H — multi-graph isolates (structurally disconnected)
- Active Inquisition (cite 0, tl 0, mu 0, pp 0, canonical)
- Body (cite 0, tl 0, mu 0, pp 0, canonical)
- Counter-Intelligence (cite 0, tl 0, mu 0, pp 0, canonical)
- Key: scene_outcome.battle_concluded (cite 0, tl 0, mu 0, pp 0, canonical)
- NPC Relational Graph (cite 0, tl 0, mu 0, pp 0, canonical)
- Territorial Piety (cite 0, tl 0, mu 0, pp 0, canonical)
- Territory Temperaments (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Mandate (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Treasury income (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)
