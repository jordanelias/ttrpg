# Weakness register — vector audit v3 (leads, not verdicts)

Corpus: 110 design docs, 276 tokens. Validation: **FAILED** (1/3). Confidence inherits from validation (methodology §3.8).

**Coverage disclosure (capstone #6):** this L0 layer is a CURATED slice — 110 design docs = only 6.0% of the repo's 1822 `.md` files. Everything outside `_canonical_paths()` (most of `systems/`, all of `engine/params/`/`sim/`/`tests/`/`canon/` prose not named in `canonical_sources.yaml`) is structurally invisible to L0 — a green result here is NOT whole-repo coverage.
Scorecard: cite-edges=14865, hubs=10, implied-missing=32, notional=14542, cascade-sinks=235, sparse=16, isolates=11, vocab-debt-terms=3.

## Mode A — multi-graph hubs (highest change-impact)
- **Conflict Architecture** — top-quintile in 3/4 (cite 126, tl 10, mu 21, pp 13)
- **Conviction Track** — top-quintile in 3/4 (cite 142, tl 6, mu 23, pp 0)
- **Duchess Inge Baralta** — top-quintile in 3/4 (cite 160, tl 4, mu 12, pp 0)
- **Factions** — top-quintile in 3/4 (cite 185, tl 14, mu 21, pp 0)
- **Mass Combat** — top-quintile in 3/4 (cite 147, tl 9, mu 23, pp 0)
- **Peninsular Strain** — top-quintile in 3/4 (cite 149, tl 14, mu 23, pp 0)
- **Settlement Layer** — top-quintile in 3/4 (cite 156, tl 10, mu 23, pp 0)
- **Territories** — top-quintile in 3/4 (cite 201, tl 7, mu 21, pp 0)
- **Threadwork** — top-quintile in 3/4 (cite 184, tl 18, mu 25, pp 0)
- **Victory** — top-quintile in 3/4 (cite 148, tl 11, mu 23, pp 0)

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
- Duchess Inge Baralta → Crown (cite weight 183)
- Prince Torben Almqvist → Crown (cite weight 183)
- Church → Crown (cite weight 183)
- Hafenmark → Crown (cite weight 183)
- Varfell → Crown (cite weight 183)
- Löwenritter → Crown (cite weight 183)
- Guilds → Crown (cite weight 183)
- Standing → Crown (cite weight 183)
- Conviction Track → Crown (cite weight 183)
- Factions → Crown (cite weight 183)
- NPC Roster → Crown (cite weight 183)
- Aldric Tormann → Crown (cite weight 183)
- Cardinal Arnlod Olafsson → Crown (cite weight 183)
- Cardinal Osten Jarnstal → Crown (cite weight 183)
- Gerik Strand → Crown (cite weight 183)
- Maret Uln → Crown (cite weight 183)
- Peder Almstedt → Crown (cite weight 183)
- Wardens → Crown (cite weight 183)
- Einhir → Crown (cite weight 183)
- … 14522 more (see `data/multigraph_diagnostics.json`)

## Mode D — cascade sinks (one-way "black holes")
- **Audit** — 806 chains terminate here
- **Conviction** — 747 chains terminate here
- **Key: mechanical.accounting** — 709 chains terminate here
- **Threadwork** — 686 chains terminate here
- **Knot** — 677 chains terminate here
- **Territories** — 655 chains terminate here
- **Church** — 641 chains terminate here
- **Disposition** — 635 chains terminate here
- **Mass Battle** — 621 chains terminate here
- **Mass Combat** — 621 chains terminate here
- **Social Contest** — 614 chains terminate here
- **Stability** — 609 chains terminate here
- **NPC Behavior** — 609 chains terminate here
- **Scene Slate** — 564 chains terminate here
- **Crown** — 554 chains terminate here
- … 220 more (see `data/multigraph_diagnostics.json`)

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
- Fractional Province (1 paras, cite-deg 22, provisional)
- Mind (1 paras, cite-deg 11, canonical)

## Mode F — throughline orphans (≤2 substantiating paragraphs)
- T-10 — 0 subst. (—)

## Mode G — vocabulary debt (struck terms still present)
- **Coup Counter** — 57 in 13 docs (top: arcs/arc_expansion_v30.md)
- **Cultural Reformation** — 23 in 9 docs (top: systems/overview/peninsular_strain_v30.md)
- **Game Master** — 21 in 8 docs (top: arcs/throughline_resolutions_v30.md)

## Mode H — multi-graph isolates (structurally disconnected)
- Active Inquisition (cite 0, tl 0, mu 0, pp 0, canonical)
- Body (cite 0, tl 0, mu 0, pp 0, canonical)
- Counter-Intelligence (cite 0, tl 0, mu 0, pp 0, canonical)
- Key: mechanical.scene_exited (cite 0, tl 0, mu 0, pp 0, canonical)
- Key: mechanical.scene_skipped (cite 0, tl 0, mu 0, pp 0, canonical)
- Key: scene_outcome.battle_concluded (cite 0, tl 0, mu 0, pp 0, canonical)
- NPC Relational Graph (cite 0, tl 0, mu 0, pp 0, canonical)
- Territorial Piety (cite 0, tl 0, mu 0, pp 0, canonical)
- Territory Temperaments (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Mandate (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)
- faction Treasury income (cross-module → faction_state) (cite 0, tl 0, mu 0, pp 0, canonical)

---

## §Disposition + backtrace correction (2026-07-21, expanded 276-token universe)

**The "FAILED (1/3)" verdict is largely an instrument artifact, not a corpus indictment** —
established by adversarial backtrace:
- **P2 conviction-symmetry** is structurally UNSATISFIABLE: `throughlines_meta_infill.md` routes
  all 7 convictions through the aggregate `conviction_track` slug, so their throughline-degree is
  permanently `[0,…,0]` → `cv=999` → guaranteed FAIL. The symmetry it means to check HOLDS on the
  cite axis (CV≈0.11). **Not a finding.**
- **P1** is partly a token-coverage effect. **P3 passes hard** (14865 edges ≥ 100). The corpus is
  densely, correctly connected at its strategic core.

**Real signal (leads, not verdicts):**
- **Mode A** — the change-impact spine (Territories, Factions, Threadwork, Settlement Layer,
  Peninsular Strain, Victory, Mass Combat, Conviction Track, Conflict Architecture, Duchess Inge
  Baralta). Only Conflict Architecture is patch-wired (pp 13); the rest are pp 0.
- **Mode B (headline)** — `Clocks` is in 6 of 32 implied-but-missing pairs (↔Victory/Threadwork/
  Faction Layer/Peninsular Strain/MS Trajectory/Royal Assassination Fuse): the temporal spine binds
  distant subsystems in structure but is un-cited in prose. Quantitative corroboration of the
  engine_clock gap (ED-1051). Same pattern for Campaign Architecture.
- **Modes E/H (expansion payoff)** — 11 isolates are defined-but-orphaned granules: Keys
  `mechanical.scene_exited/scene_skipped/scene_outcome.battle_concluded` (the last is the FABRICATED
  emit ED-MB-0010 — its isolation corroborates it was never real); actions `Active Inquisition`,
  `Counter-Intelligence` (no domain_actions home, ED-FA-0002); values `faction Mandate/Treasury
  income`; `Body`/`Mind`/`Territorial Piety`/`Territory Temperaments`/`NPC Relational Graph`.

**Artifacts to discount:** Mode C notional (14542; the uniform `* → Crown` co-occurrence fan-in,
grows with token count, not real per-pair debt); Mode D top sink `Audit` (bare token catching
audit-doc mentions — the real terminal beneath is `Key: mechanical.accounting`).

**Held back for Jordan (v4, do not auto-ratify — flips a verdict / touches locked validation):**
redefine P2 to the cite axis + fix the `mean==0 → cv=999` sentinel; P1 token coverage; author the
domain_actions home (ED-FA-0002) so action verbs stop floating. No `ED-<LANE>` allocated this run.
