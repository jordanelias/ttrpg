## LANE B — WORLD, TOPOGRAPHY & SETTLEMENT (archives/audit)

**Note on "topographic analysis":** confirmed within the first three files (`00_workplan.md`, `01_methodology.md`) that this directory is a citation-graph/TF-IDF audit of the *design corpus's own document structure* (84 vocabulary tokens across 43 docs, five metadata graphs), not game-world geography. Budget was reallocated accordingly: light extraction of world/settlement-relevant spillover from the topographic corpus, heavy reading of the three genuinely substantive directories.

### COVERAGE
files_assigned: 27 | files_opened: 27 | files_read_closely: 8
skipped:
- `03_validation_report.md` (topographic) — grepped only; pure hypothesis-testing on the corpus's own graph structure, no additional world/settlement content beyond `02_weakness_register.md`.
- `data/*.json` ×16 (topographic/data/) — raw graph/layout/token arrays backing prose already extracted from `02_weakness_register.md`; verified structurally (type/length), no independent prose.
- `valoria_ecosystem_reconciled_report_2026-06-09.md`, `valoria_workplan_R2_2026-06-09.md` (ecosystem-reconciliation) — targeted grep confirmed pure repo-process/CI/hooks/editorial-ledger audit content, matching the brief's hard exclusion; only two in-scope manifest lines were folded in (`designs/world/` 22 files, `designs/npcs/` 18 files — worldbuilding/geography/NPC canon, no further detail given).

### FINDINGS (ranked)

**F-B-1 — Faction Mandate and Province Accord are explicitly recomputed each season from settlement primitives, never stored independently**
- SOURCE: `2026-06-10-settlement-analysis/settlement_flattened_map.md` §II.A, state register table
- CATEGORY: derivation
- SUBSTANCE: `W_s = base(Type) + Prosperity_s + FacilityTier_s` (1–11); `q_s = 0.5·L_s + 0.5·PS_s` (0–7); `T = Σ_held W_s·(q_s/7)`; `Mandate = clamp(round(7T/(T+K)), 0, 7)`, K=6 — a saturating aggregation that bounds any single settlement's leverage over faction-wide Mandate. `Province Accord = floor(mean(Order over province settlements))`, single-settlement passthrough with a Seat +1 tie-break. Legitimacy/PopularSupport live per-settlement keyed to the controlling faction, aggregated up via weighted means.
- WHY IT MAY STILL MATTER: direct evidence for the "derive vs. store" design question — faction/province meta-stats are architecturally treated as pure functions of settlement state, recomputed every Accounting.
- STATUS IN DOC: `[C]` canonical.
- REDISCOVERED IN: mirrored (same formulas) in `settlement_flowchart.mermaid` CALCS subgraph — same session/sources, not independent.

**F-B-2 — Mandate drift is mean-reverting and sim-verified convergent; Temperament drift is one-directional and only provisional**
- SOURCE: `settlement_flattened_map.md` §I.F, §II.C (Temperament row)
- CATEGORY: world-churn
- SUBSTANCE: Mandate feedback: `q_s ≥1 below Mandate → L+1 (cap 7)`, `q_s ≥1 above → PS−1 (floor 0)`, capped ±1/settlement/season inside a ±2 faction seasonal cap — doc states this is "negative (stabilizing) feedback, Stage-4 sim-verified bounded/convergent over 30 seasons." Contrast: province Temperament is a continuous (α,β) pair over five typologies — pragmatic .7/.3, traditional .3/.7, balanced .5/.5, principled .2/.8, outcomes-only .9/.1 — with drift `+= 0.1 × strain_delta`, clamped ±1, that always trends toward outcomes-only with no symmetric pull-back.
- WHY IT MAY STILL MATTER: two "world drift" mechanics in the same design have opposite dynamical character (one provably converges, one has irreversible directional pressure), and only the tested one was actually verified.
- STATUS IN DOC: Mandate drift `[C]`; Temperament `[P]` provisional, "settlement grain deferred Stage 6b."
- REDISCOVERED IN: single source.

**F-B-3 — Settlement state is modeled as concurrent orthogonal state machines, not one flat status**
- SOURCE: `settlement_state_graph.mermaid` lines 1–73
- CATEGORY: ontology
- SUBSTANCE: One `SETTLEMENT` node contains three parallel regions that evolve independently: Control/military axis (Held→UnderAssault/UnderSiege/Bypassed/AutoCaptured/Holdout/RMTransition), Governance axis (Governed{FactionGovernorNPC/PlayerGovernor/SubnationalGovernor/BishopGovernor}⇄Unmanaged⇄ChurchGoverned), Civil/economic axis (Stable/Flourishing/Famine/Revolt/BlackMarket). They interact only through shared numeric stats (Order, Defense, Prosperity), so e.g. a settlement can be UnderSiege while independently Flourishing lapses.
- WHY IT MAY STILL MATTER: a reusable structural pattern (concurrent per-entity axes) independent of the specific fields — the faction lifecycle (F-B-4) uses the identical pattern at a different scale.
- STATUS IN DOC: none explicit; diagram's own header calls it "orthogonal axes of one settlement."
- REDISCOVERED IN: same underlying source docs as `settlement_flattened_map.md`, not independent.

**F-B-4 — Faction lifecycle is a settlement-count/Renown-gated ladder with a numbered collapse path**
- SOURCE: `settlement_state_graph.mermaid` "FACTION LIFECYCLE" block; `settlement_flattened_map.md` §III.E, §II.D
- CATEGORY: faction
- SUBSTANCE: Cell→Organization (1st settlement, Renown 3–4)→Movement (2+ settlements, Renown 5+, 2 officers Disp+3)→Faction (4+ settlements/2+ provinces, Renown 7+, 1 Seat, Declaration roll Influence=Renown/2 vs Ob3)→Hegemon (2+ province Seats, Renown 9+, Parliament seat). Collapse: →CityState (last province lost, leader alive; partial sheet — only Influence/Wealth/Stability, no Mandate, no Military unless garrisoned)→Dissolved (leader dead/captured, no successor Standing 4+; settlements go unmanaged, officers become free agents). Founding stats (ED-790): L2/PS3, Influence=floor(Renown/2), Wealth=2+(settlements−1) cap 5, Military 1, Intel 2, Stability 3.
- WHY IT MAY STILL MATTER: a fully numbered faction-power ladder gated on settlement count — concrete answer to "how do factions relate to settlements structurally."
- STATUS IN DOC: `[C]` (hard-gates table); ED-790 cited.
- REDISCOVERED IN: single source (state graph + flattened map, same session).

**F-B-5 — Two explicit world-churn GAPs: undefined baseline Order-decay rate, and unspecified Accounting firing order**
- SOURCE: `settlement_flattened_map.md` §I.G, §III.A, §V items 1–2
- CATEGORY: world-churn / problem-only
- SUBSTANCE: What churns without player action: unmanaged settlement Order −1/season; siege tick −1 Order/season; Mandate mean-reverting drift (F-B-1/2); Temperament drift (F-B-2). But: "a baseline seasonal decay exists (Administer suppresses it...) — rate unstated in read set `[GAP]`", and the entire Accounting firing set (parish bonus, decay, siege tick, revolt check, Mandate drift, event roll, etc.) has "canonical intra-Accounting ordering... unspecified" — doc flags this as consequential because ordering decides whether a settlement surrenders or riots first in the same season.
- WHY IT MAY STILL MATTER: precisely the "world change when nobody acts" question, with a live implementation-blocking ambiguity named exactly.
- STATUS IN DOC: `[GAP]` verbatim, both items.
- REDISCOVERED IN: single source.

**F-B-6 — Settlement stat-damage is a canonical rule with no operating substrate (blocked on a PENDING derived layer), plus a live ×50 vs ×10 numeric contradiction**
- SOURCE: `settlement_flattened_map.md` §II.B, §V item 3; `settlement_flowchart.mermaid` DERIV node
- CATEGORY: problem-only
- SUBSTANCE: `derived_stats §9` defines "Local Economy = Prosperity×50, Garrison Strength = Defense×20+FortLevel×30, Public Order = Order×20" but is marked `[PEND]` "not canonicalized." Separately-canonical §1.3 states a settlement stat takes −1 only "when its derived value sits at 0 through Accounting" — routed through that same pending layer, so "until §9 canonizes, settlement stat damage has no operating substrate `[GAP]`." Also: §1.3's own gloss of "×50" as income conflicts with the canonical Treasury income formula of Prosperity×10 (derived_stats §8.1).
- WHY IT MAY STILL MATTER: a canonical rule that cannot actually fire, plus a genuine numeric contradiction between two nominally-canonical sources.
- STATUS IN DOC: `[PEND]`/`[GAP]` verbatim.
- REDISCOVERED IN: single source.

**F-B-7 — Geography: settlement is the atomic node for both political aggregation and military movement; province is a pure emergent grouping**
- SOURCE: `settlement_flattened_map.md` §I.H, §III.B; `settlement_state_graph.mermaid` PROVINCE block
- CATEGORY: world-churn
- SUBSTANCE: 56-edge settlement adjacency (28 intra-province: 7 triangles + 7 singles; 28 inter-province incl. one sea-edge + 3 "resilience routes"); terrain cost matrix (mountain=999 impassable, pass=2.0, bridge=1.0); ≥2-connection rule with one named exception (Schoenland, degree-1, "foreign-exempt pending ED-055"). Armies move via A* at budget 100px/season×Military (cavalry×1.5); invasion is explicitly "path-constrained, no free choice of target." A province becomes Fractured purely when its settlements are held by different factions (named sub-provinces each count as a full province; "Unification bonus lost while fractured") and reunifies when common alignment returns.
- WHY IT MAY STILL MATTER: answers "what is the atomic spatial unit and adjacency" with real numbers; province has no independent existence beyond settlement-ownership pattern.
- STATUS IN DOC: `[C]` for structure; fracture/unify event *triggers* separately `[TBD]`.
- REDISCOVERED IN: single source.

**F-B-8 — NPC Behavior measured as the corpus's integration spine, and undervetted despite it**
- SOURCE: `2026-04-29-topographic-analysis/02_weakness_register.md` §V3-1, §V3-3, §V3-6
- CATEGORY: npc
- SUBSTANCE: Over 84 tokens/43 docs, NPC Behavior has citation in+out degree 56 (highest of any token, ~70% of all others), with Convictions/Pressure Points/Disposition/Standing "all rout[ing] through it." Yet it shows zero recent patch-register activity, discourse ratio 0.20 (low), and 3 of 7 Convictions + 3 of 4 Pressure Points score ratio 0.00 (no editorial scrutiny at all) despite 10–15 paragraphs of substance each.
- WHY IT MAY STILL MATTER: names where integration risk concentrates — an error in NPC Behavior propagates through nearly everything, and it was the least-audited load-bearing piece found.
- STATUS IN DOC: corrects an earlier (v2) claim in the same corpus that the opposite was true — see DEAD ENDS.
- REDISCOVERED IN: single source (v3 self-corrects v2).

**F-B-9 — Canonical NPC/faction primitive roster, several load-bearing concepts with no dedicated file**
- SOURCE: `01_methodology.md` lines 84–91; `02_weakness_register.md` §V3-5, §V3-10
- CATEGORY: ontology
- SUBSTANCE: Convictions (7): Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity. Pressure Points (4): Evidence, Consequence, Authority, Loyalty. Factions (7): Crown, Church, Hafenmark, Varfell, Löwenritter, Restoration Movement, Guilds. Clocks (6): MS, CI, IP, PI, TS, TCV. "Piety Track" is canonical/heavily used but lives inline in `npc_behavior_v30.md`, as do 5 of 7 Convictions and 3 of 4 Pressure Points; recommended (not confirmed executed) split into dedicated `conviction_taxonomy_v1.md` / `pressure_point_taxonomy_v1.md` / `conviction_track_v1.md`.
- WHY IT MAY STILL MATTER: a complete 2026-04-29 checklist of NPC/faction primitive vocabulary, plus a recurring "buried in parent doc" anti-pattern (also true of Disposition, Domain Action).
- STATUS IN DOC: `[C]` concepts; promotion recommendation `[PEND]`.
- REDISCOVERED IN: single source.

**F-B-10 — CI clock and Mandate are heavily coupled to faction politics with zero formal metadata capturing it**
- SOURCE: `02_weakness_register.md` §V3-4
- CATEGORY: governance
- SUBSTANCE: Top uncaptured citation-weight pairs: Faction Layer→Stability (68), CI→Mandate (58), NPC Behavior→TS (55), Faction Layer→Mandate (54), CI→Restoration Movement (51), NPC Behavior→Stability (48), CI Political→Mandate (44), CI→Crown (44), CI→Church (44), CI→Hafenmark (39), CI→IP (34), CI→Varfell (33). None formalized in throughline/Μ/PP metadata — prose-only couplings.
- WHY IT MAY STILL MATTER: a ranked map of where "how does a faction's legitimacy actually move" lives, useful for reconstructing governance mechanism from prose alone.
- STATUS IN DOC: finding only, recommendation not confirmed executed.
- REDISCOVERED IN: single source.

**F-B-11 — Governor action menu: fixed dice-pool costs, one free action/season**
- SOURCE: `settlement_flattened_map.md` §I.A
- CATEGORY: mechanism
- SUBSTANCE: Develop (Cognition+History, Ob=floor(Prosperity/2)+1 → Prosperity+1); Fortify (Military-stat+History, Ob=floor(Defense/2)+1 → Defense+1); Pacify (Charisma+History, Ob=floor((3−Order)+1) min 1 → Order+1 cap 5); Administer (Attunement+Governance History, Ob=2 → suppresses Order decay this season AND reveals one local NPC's active Conviction). NPC-governor default order: Pacify→Develop→Fortify→Administer, faction-tree override at Stability≤2.
- WHY IT MAY STILL MATTER: exact costing for the single most common settlement interaction; Administer's Conviction-reveal ties governance directly to NPC modelling.
- STATUS IN DOC: structure `[C]`; specific numbers "Calibration `[P]` per ED-SETT-02."
- REDISCOVERED IN: single source.

**F-B-12 — Governance vacancy has a built-in Church annexation default**
- SOURCE: `settlement_flattened_map.md` §III.C
- CATEGORY: governance
- SUBSTANCE: Assignment gated by Standing: 3=Town/Outpost, 4=City/Fortress/Mine, 5=Seat/Cathedral+leader approval. On vacancy: Unmanaged (Order−1/season) until reassigned, OR Church can auto-claim via Pastoral Assumption (Ob1, requires no governor + ≥Chapel) — removable only via Mass Battle, Mandate Challenge Ob6+, or an Overt/Witnessed RM community action.
- WHY IT MAY STILL MATTER: an emergent-pressure design where idle settlements drift toward Church control rather than chaos — a specific, exploitable default worth preserving or deliberately rejecting.
- STATUS IN DOC: `[C]`.
- REDISCOVERED IN: single source.

**F-B-13 — Church institutional build-out is a numerically concrete parallel development track that raises military seizure cost**
- SOURCE: `settlement_flattened_map.md` §I.D
- CATEGORY: mechanism
- SUBSTANCE: Chapel +0.5 Piety-Track/season, Church +1 PT/season, Cathedral +2 PT/season (+0.5 to adjacent territories); Templar +1 Church Influence/season + rival-Domain-Action interrupt; Inquisitor forces a Concealment test/season and +1 Ob to RM governance; Church Governor replaces normal governance, removable only via Mass Battle/Mandate Challenge Ob6+/RM Overt action. Seizure-Ob modifiers stack per settlement: Chapel −0, Church −1, Cathedral −2, Templar −1, Inquisitor −1, Church Governor −2, capped at −4 total.
- WHY IT MAY STILL MATTER: worked example of non-military investment mechanically raising the cost of conquest.
- STATUS IN DOC: `[C]`.
- REDISCOVERED IN: single source.

**F-B-14 — Fortress-City settlement-Weight base is unresolved (2 vs 3), and a named settlement is exactly where it matters**
- SOURCE: `settlement_flattened_map.md` §II.A, §V item 4
- CATEGORY: problem-only
- SUBSTANCE: `base(Type)` table: Seat/City/Cathedral=3, Town/Fortress/Port=2, Village/Mine/Outpost=1; "Cathedral-City → 3 either reading" but "Fortress-City UNRESOLVED 2 vs 3 `[GAP]`" — doc explicitly names the stakes: "Ehrenfeld is precisely where W matters," since W_s feeds Mandate (F-B-1).
- WHY IT MAY STILL MATTER: cheap, precisely-located fix that materially changes a specific settlement's Mandate contribution.
- STATUS IN DOC: `[GAP]`.
- REDISCOVERED IN: single source.

**F-B-15 — Terminology-conversion workplan claims the strategic/scene game loop was always binary, "Hybrid" was purely textual**
- SOURCE: `2026-04-29-terminology-conversion/00_workplan.md` §0, §3
- CATEGORY: ontology
- SUBSTANCE: `scale_transitions_v30 §6` canonized three modes (TTRPG/BG/Hybrid, three transition procedures). Workplan (PP-675, provisional) argues: "the engine already runs on a binary Strategic/Scene state machine. The three-mode framing was textual, not implementation." Proposed replacement: Strategic Mode (peninsula map, seasons advancing, Domain Actions, clocks ticking) ⇄ Scene Mode via Zoom-In/Zoom-Out verbs. Explicitly unaffected: the 8 handoff rules, Sufficient Scope, Domain Echo, Coherence cost, Scene Slate, Zoom-In trigger taxonomy.
- WHY IT MAY STILL MATTER: a load-bearing claim about the top-level game-loop — the world has exactly two states (running with season ticks, or paused at one Scene) — worth checking against the current engine's mode model.
- STATUS IN DOC: `PROVISIONAL — workplan proposal, not canonical until decisions §4 are resolved and PP-675 promotes.`
- REDISCOVERED IN: single source.

### DEAD ENDS
- **v2 topographic finding "the corpus documents people/factions/NPCs, not mechanical systems"** (`02_weakness_register.md` §1.1, restated §V3-13) — RETRACTED by v3, same corpus: "v2 corrects this... the corpus IS system-centered, NPC Behavior is the spine." Killed by methodology error: v2 measured TF-IDF mean cosine (a function of paragraph breadth) and mistook it for citation centrality; broadly-mentioned tokens (Crown, Varfell) scored high on breadth alone.
- **v2 "Settlement Layer downstream sink"** (`02_weakness_register.md` §1.2, lines 65–80) — claimed Settlement Layer receives citations from four major docs via CI but cites none back, violating Ω-d feedback. PARTIALLY CORRECTED at line 444/552: "Settlement Layer is no longer a top sink in v3's expanded graph... it DOES cite back, just not in `Cross-references:` lines — it cites inline." Artifact of explicit-only citation parsing.
- **Old settlement-movement rule "1 edge/season, Military÷2 edges"** (`settlement_flattened_map.md` §I.C) — marked `[SUP]` superseded by ED-780 migration; current canonical movement is A*-budget (100px/season×Military stat, terrain-costed).

### OPEN QUESTIONS NEVER ANSWERED
1. Intra-Accounting firing-set ordering — no canonical sequence given; doc calls for "a ruling or an explicit 'order-independent by design' statement." (`settlement_flattened_map.md` §III.A, §V.1)
2. Baseline seasonal Order-decay rate — never stated despite three mechanics modifying it. (§I.G, §V.2)
3. Fortress-City Weight base, 2 vs 3 — directly affects Ehrenfeld's Mandate contribution. (§II.A, §V.4)
4. `derived_stats §9` (Local Economy/Garrison Strength/Public Order formulas) — PENDING, and the canonical stat-damage rule has no substrate until it lands. (§II.B, §V.3)
5. "Thread Revelation" — canonical, lives inline in Campaign Architecture, no dedicated file: "Should it be split out? Question for Jordan." (`02_weakness_register.md` §V3-5 item 3)
6. Wager↔Edeyja implied connection (v2 finding) — "NOT VERIFIED IN V3," left pending re-check. (`02_weakness_register.md` §V3-13)
7. Hybrid-mode retirement (§4.3, the load-bearing decision) — explicitly gated on Jordan sign-off, "Without this, the vocabulary substitution is incoherent"; no confirmation anywhere in this corpus that it was resolved. (`terminology-conversion/00_workplan.md` §4, §9)
8. Province Fracture/Unify event *triggers* — marked `[TBD]` even though the fracture rule itself is canonical. (`settlement_flattened_map.md` state register / §III.E)