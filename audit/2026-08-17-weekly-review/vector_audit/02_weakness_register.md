# Weakness register — vector audit v3 (structural findings)

Corpus: 217 design docs, 268 tokens. Validation: **VALIDATED** (2/3) — L0-calibrated thresholds, NOT re-validated for L1. Confidence inherits from validation (methodology §3.8).

**Coverage disclosure (capstone #6):** layer **L1** traces 217 design docs = 38.1% of the repo's 570 `.md` files — the whole DESIGN tree (systems/engine/canon/godot/proposals); still excludes arcs/ narrative, workplans/, tests/, deprecated/, audit prose, and non-.md. A green result at this layer is NOT whole-repo coverage.

**Direction disclosure:** L1 extends the corpus-breadth direction and the CITE graph ONLY. NOT extended: the throughline/mu/key graphs (registry-derived: throughline from throughlines_meta + throughlines_complete, mu from throughlines_meta, key from module_contracts), the token universe (registry-derived; a token absent from names_index/proper_noun/module_contracts is invisible at EVERY layer), non-.md content (sim .py, engine/params values), and the P1/P2/P3 thresholds (calibrated on L0 — the verdict below is NOT re-validated for the L1 corpus).
Scorecard: cite-edges=13839, hubs=15, implied-missing=28, notional=13478, cascade-sinks=237, sparse=10, isolates=4, vocab-debt-terms=3.
⚠ Mode D reachability hit its traversal cap on 55175 call(s) — some cascade-sinks may be cap artifacts, not true sinks (denser corpus / L1). Treat cascade-sinks as leads here.

## Mode A — multi-graph hubs (highest change-impact)
- **Mass Battle** — top-quintile in 4/4 (cite 146, tl 12, mu 20, pp 0)
- **Peninsular Strain** — top-quintile in 4/4 (cite 135, tl 16, mu 20, pp 0)
- **Settlement Layer** — top-quintile in 4/4 (cite 155, tl 15, mu 20, pp 0)
- **Threadwork** — top-quintile in 4/4 (cite 172, tl 21, mu 22, pp 0)
- **CI Political** — top-quintile in 3/4 (cite 134, tl 1, mu 12, pp 0)
- **Conflict Architecture** — top-quintile in 3/4 (cite 116, tl 10, mu 20, pp 12)
- **Conviction Track** — top-quintile in 3/4 (cite 134, tl 11, mu 20, pp 0)
- **Domain Actions** — top-quintile in 3/4 (cite 141, tl 0, mu 0, pp 12)
- **Duchess Inge Baralta** — top-quintile in 3/4 (cite 144, tl 4, mu 11, pp 0)
- **Factions** — top-quintile in 3/4 (cite 177, tl 13, mu 20, pp 0)
- **Miraculous Event** — top-quintile in 3/4 (cite 40, tl 4, mu 11, pp 0)
- **NPC Behavior** — top-quintile in 3/4 (cite 145, tl 10, mu 0, pp 0)
- **Social Contest** — top-quintile in 3/4 (cite 146, tl 5, mu 0, pp 0)
- **Territories** — top-quintile in 3/4 (cite 187, tl 7, mu 18, pp 0)
- **Victory** — top-quintile in 3/4 (cite 144, tl 14, mu 20, pp 0)

## Mode B — implied-but-missing (metadata links, no citation)
- Campaign Architecture ↔ Faction Layer (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Campaign Architecture ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Faction Succession Split (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Leap Mechanism (2 metadata graphs, 0 cite)
- Conflict Architecture ↔ Tensions Deck (2 metadata graphs, 0 cite)
- Conviction Track ↔ Derived Stats (2 metadata graphs, 0 cite)
- Conviction Track ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- Derived Stats ↔ Self-Rendering (2 metadata graphs, 0 cite)
- Derived Stats ↔ Solmund (2 metadata graphs, 0 cite)
- Faction Layer ↔ Faction Succession Split (2 metadata graphs, 0 cite)
- Faction Layer ↔ Mass Battle (2 metadata graphs, 0 cite)
- Faction Layer ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Faction Succession Split ↔ Factions (2 metadata graphs, 0 cite)
- Faction Succession Split ↔ Scale Transitions (2 metadata graphs, 0 cite)
- Factions ↔ MS Trajectory (2 metadata graphs, 0 cite)
- Factions ↔ Miraculous Event (2 metadata graphs, 0 cite)
- MS Trajectory ↔ Peninsular Strain (2 metadata graphs, 0 cite)
- MS Trajectory ↔ Settlement Layer (2 metadata graphs, 0 cite)
- Mass Battle ↔ Settlement Layer (2 metadata graphs, 0 cite)
- … 8 more (see `data/multigraph_diagnostics.json`)

## Mode C — notional edges (cited, no metadata support)
- Aldric Tormann → Crown (cite weight 183)
- CI Political → Crown (cite weight 183)
- Cardinal Arnlod Olafsson → Crown (cite weight 183)
- Cardinal Osten Jarnstal → Crown (cite weight 183)
- Church → Crown (cite weight 183)
- Confessor Arne Himlensendt → Crown (cite weight 183)
- Conviction Track → Crown (cite weight 183)
- Duchess Inge Baralta → Crown (cite weight 183)
- Einhir → Crown (cite weight 183)
- Factions → Crown (cite weight 183)
- Gerik Strand → Crown (cite weight 183)
- Grandmaster Ehrenwall → Crown (cite weight 183)
- Guilds → Crown (cite weight 183)
- Hafenmark → Crown (cite weight 183)
- Key: scene.witness → Crown (cite weight 183)
- Löwenritter → Crown (cite weight 183)
- Maret Uln → Crown (cite weight 183)
- NPC Roster → Crown (cite weight 183)
- Peder Almstedt → Crown (cite weight 183)
- Prince Torben Almqvist → Crown (cite weight 183)
- … 13458 more (see `data/multigraph_diagnostics.json`)

## Mode D — cascade sinks (one-way "black holes")
- **Church** — 773 chains terminate here
- **Audit** — 767 chains terminate here
- **Conviction** — 752 chains terminate here
- **Territories** — 746 chains terminate here
- **Threadwork** — 692 chains terminate here
- **CI** — 687 chains terminate here
- **Mandate** — 686 chains terminate here
- **Factions** — 655 chains terminate here
- **Disposition** — 642 chains terminate here
- **NPC Behavior** — 639 chains terminate here
- **Social Contest** — 638 chains terminate here
- **Stability** — 632 chains terminate here
- **Key: mechanical.accounting** — 629 chains terminate here
- **Knot** — 623 chains terminate here
- **Crown** — 603 chains terminate here
- … 222 more (see `data/multigraph_diagnostics.json`)

## Mode E — sparse-context tokens (gapped regions)
- Active Inquisition (0 paras, cite-deg 0, canonical)
- Counter-Intelligence (0 paras, cite-deg 0, canonical)
- Key: mechanical.scene_exited (0 paras, cite-deg 0, canonical)
- Key: mechanical.scene_skipped (0 paras, cite-deg 0, canonical)
- faction Mandate (cross-module → faction_state) (0 paras, cite-deg 0, canonical)
- faction Treasury income (cross-module → faction_state) (0 paras, cite-deg 0, canonical)
- Mind (1 paras, cite-deg 12, canonical)
- Holonic Container Doctrine (2 paras, cite-deg 19, canonical)
- Key: env.disaster (3 paras, cite-deg 17, canonical)
- Key: state.standing_change (3 paras, cite-deg 20, canonical)

## Mode F — throughline orphans (≤2 substantiating paragraphs)
(none)

## Mode G — vocabulary debt (struck terms still present)
- **Game Master** — 68 in 18 docs (top: systems/_architecture/hybrid_gaps_v30.md)
- **Coup Counter** — 46 in 19 docs (top: systems/_architecture/early_game_ignition_analysis.md)
- **Cultural Reformation** — 24 in 10 docs (top: systems/overview/peninsular_strain_v30.md)

## Mode H — multi-graph isolates (structurally disconnected)
- Active Inquisition (cite 0, tl 0, mu 0, pp 0, canonical)
- Counter-Intelligence (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Mandate (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Treasury income (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)
