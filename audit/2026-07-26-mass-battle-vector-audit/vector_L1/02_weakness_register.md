# Weakness register — vector audit v3 (structural findings)

Corpus: 239 design docs, 275 tokens. Validation: **VALIDATED** (2/3) — L0-calibrated thresholds, NOT re-validated for L1. Confidence inherits from validation (methodology §3.8).

**Coverage disclosure (capstone #6):** layer **L1** traces 239 design docs = 12.8% of the repo's 1873 `.md` files — the whole DESIGN tree (systems/engine/canon/godot/proposals); still excludes arcs/ narrative, workplans/, tests/, deprecated/, audit prose, and non-.md. A green result at this layer is NOT whole-repo coverage.

**Direction disclosure:** L1 extends the corpus-breadth direction and the CITE graph ONLY. NOT extended: the throughline/mu/key graphs (registry-derived: throughline from throughlines_meta + throughlines_complete, mu from throughlines_meta, key from module_contracts), the token universe (registry-derived; a token absent from names_index/proper_noun/module_contracts is invisible at EVERY layer), non-.md content (sim .py, engine/params values), and the P1/P2/P3 thresholds (calibrated on L0 — the verdict below is NOT re-validated for the L1 corpus).
Scorecard: cite-edges=14968, hubs=16, implied-missing=36, notional=14629, cascade-sinks=248, sparse=13, isolates=4, vocab-debt-terms=3.
⚠ Mode D reachability hit its traversal cap on 62882 call(s) — some cascade-sinks may be cap artifacts, not true sinks (denser corpus / L1). Treat cascade-sinks as leads here.

## Mode A — multi-graph hubs (highest change-impact)
- **Peninsular Strain** — top-quintile in 4/4 (cite 146, tl 19, mu 23, pp 0)
- **Settlement Layer** — top-quintile in 4/4 (cite 166, tl 16, mu 23, pp 0)
- **Threadwork** — top-quintile in 4/4 (cite 188, tl 24, mu 25, pp 0)
- **CI Political** — top-quintile in 3/4 (cite 143, tl 2, mu 14, pp 0)
- **Conflict Architecture** — top-quintile in 3/4 (cite 119, tl 10, mu 21, pp 8)
- **Conviction Track** — top-quintile in 3/4 (cite 132, tl 12, mu 23, pp 0)
- **Domain Actions** — top-quintile in 3/4 (cite 157, tl 0, mu 0, pp 8)
- **Duchess Inge Baralta** — top-quintile in 3/4 (cite 159, tl 4, mu 12, pp 0)
- **Factions** — top-quintile in 3/4 (cite 186, tl 14, mu 21, pp 0)
- **Mass Battle** — top-quintile in 3/4 (cite 146, tl 8, mu 0, pp 0)
- **Mass Combat** — top-quintile in 3/4 (cite 146, tl 9, mu 23, pp 0)
- **Miraculous Event** — top-quintile in 3/4 (cite 48, tl 4, mu 12, pp 0)
- **NPC Behavior** — top-quintile in 3/4 (cite 158, tl 11, mu 0, pp 0)
- **Social Contest** — top-quintile in 3/4 (cite 141, tl 6, mu 0, pp 0)
- **Territories** — top-quintile in 3/4 (cite 190, tl 7, mu 21, pp 0)
- **Victory** — top-quintile in 3/4 (cite 148, tl 17, mu 23, pp 0)

## Mode B — implied-but-missing (metadata links, no citation)
- CI Political ↔ Clocks (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Faction Layer (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Clocks ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Clocks ↔ Royal Assassination Fuse (2 metadata graphs, 0 cite)
- Clocks ↔ Threadwork (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Faction Succession Split (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Leap Mechanism (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Tensions Deck (2 metadata graphs, 0 cite)
- Conviction Track ↔ Derived Stats (2 metadata graphs, 0 cite)
- Conviction Track ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Derived Stats ↔ Self-Rendering (2 metadata graphs, 0 cite)
- Derived Stats ↔ Solmund (2 metadata graphs, 0 cite)
- Faction Layer ↔ Faction Succession Split (2 metadata graphs, 0 cite)
- Faction Layer ↔ Mass Combat (2 metadata graphs, 0 cite)
- Faction Layer ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Faction Layer ↔ Victory (2 metadata graphs, 0 cite)
- Faction Succession Split ↔ Factions (2 metadata graphs, 0 cite)
- Faction Succession Split ↔ Scale Transitions (2 metadata graphs, 0 cite)
- … 16 more (see `data/multigraph_diagnostics.json`)

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
- Löwenritter → Crown (cite weight 183)
- Maret Uln → Crown (cite weight 183)
- NPC Roster → Crown (cite weight 183)
- Peder Almstedt → Crown (cite weight 183)
- Prince Torben Almqvist → Crown (cite weight 183)
- Riskbreaker → Crown (cite weight 183)
- Standing → Crown (cite weight 183)
- … 14609 more (see `data/multigraph_diagnostics.json`)

## Mode D — cascade sinks (one-way "black holes")
- **Valoria** — 920 chains terminate here
- **Church** — 900 chains terminate here
- **Threadwork** — 841 chains terminate here
- **Knot** — 830 chains terminate here
- **Stability** — 767 chains terminate here
- **Audit** — 758 chains terminate here
- **Conviction** — 749 chains terminate here
- **Key: mechanical.accounting** — 742 chains terminate here
- **Duchess Inge Baralta** — 738 chains terminate here
- **Hafenmark** — 731 chains terminate here
- **Charisma** — 725 chains terminate here
- **Crown** — 725 chains terminate here
- **TS** — 723 chains terminate here
- **CI** — 719 chains terminate here
- **Factions** — 714 chains terminate here
- … 233 more (see `data/multigraph_diagnostics.json`)

## Mode E — sparse-context tokens (gapped regions)
- Counter-Intelligence (0 paras, cite-deg 0, canonical)
- Key: mechanical.scene_exited (0 paras, cite-deg 0, canonical)
- Key: mechanical.scene_skipped (0 paras, cite-deg 0, canonical)
- Key: scene_outcome.battle_concluded (0 paras, cite-deg 0, canonical)
- faction Mandate (cross-module → faction_state) (0 paras, cite-deg 0, canonical)
- faction Treasury income (cross-module → faction_state) (0 paras, cite-deg 0, canonical)
- Key: scene.insult (1 paras, cite-deg 27, canonical)
- Body (2 paras, cite-deg 8, canonical)
- Event Impact Matrix (2 paras, cite-deg 29, provisional)
- Holonic Container Doctrine (2 paras, cite-deg 19, canonical)
- Key: env.disaster (2 paras, cite-deg 17, canonical)
- Key: da.economic_intervention (3 paras, cite-deg 27, canonical)
- Key: mechanical.season_change (3 paras, cite-deg 19, canonical)

## Mode F — throughline orphans (≤2 substantiating paragraphs)
(none)

## Mode G — vocabulary debt (struck terms still present)
- **Coup Counter** — 101 in 27 docs (top: arcs/arc_expansion_v30.md)
- **Game Master** — 75 in 22 docs (top: systems/_architecture/hybrid_gaps_v30.md)
- **Cultural Reformation** — 24 in 10 docs (top: systems/overview/peninsular_strain_v30.md)

## Mode H — multi-graph isolates (structurally disconnected)
- Counter-Intelligence (cite 0, tl 0, mu 0, pp 0, canonical)
- Key: scene_outcome.battle_concluded (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Mandate (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Treasury income (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)
