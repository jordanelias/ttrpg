## LANE E — The NPC and the Person (designs/npcs/ + designs/personal/)

### COVERAGE
files_assigned: 25 | files_opened: 24 | files_read_closely: 19

skipped: `npc_character_analyses_v30.md` skeleton — content fully covered via its `_index`/`_infill` pair, skeleton body is blank placeholders (established pattern in this corpus). `npc_behavior_system_v1.md` body — header confirms `## Status: SUPERSEDED — canonical doc is npc_behavior_v30.md`, so treated as historical-only per its own marker, not read past the header. `companion_specification_v30.md` §4–§5 (Combat AI / Mass Combat Role) — personal-combat mechanics, out of lane scope. `edeyja_npc.md` "Player Character Access" / "GM Notes" — procedural GM-facing text, low design-transfer value. `npc_character_analyses_v30_infill.md` — sampled ~8 of 24 per-NPC entries (representative Roster + Ruler Diamond figures); remainder is per-character prose of diminishing marginal value once the pattern (historical-parallel + structural-trap + arc-fork) is established.

### FINDINGS (ranked)

**F-E-1 — 13-Conviction taxonomy with 4-axis vector substrate**
- SOURCE: `designs/personal/conviction_taxonomy_v30.md` §2; `designs/personal/conviction_axis_matrix_v30.md` §2, §5
- CATEGORY: ontology
- SUBSTANCE: Every actor (NPC or PC) holds a value-frame vector over 13 named Convictions (Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor), each with an explicit Renaissance period-equivalent grounding. Each Conviction projects onto a 4-axis interpretive substrate (`hierarchical`, `sacred`, `instrumental`, `traditional`) via a fixed 13×4 matrix with per-cell calibration rationale (e.g. Honor = `[+0.5, +0.4, −0.7, +0.8]`, "the anti-instrumental Conviction"). Composition is a literal weighted dot-product: `armature_position[axis] = Σ personal_convictions[c] × MATRIX[c][axis]`, recomputed at "compute time" — no manual migration when the matrix or weights change.
- WHY IT MAY STILL MATTER: This is a complete, internally-consistent, numerically specified personality substrate — the single most portable artifact in this lane. Any downstream re-implementation of "what does this NPC value" can lift the taxonomy and matrix wholesale.
- STATUS IN DOC: `## Status: CANONICAL` (both), `PROVISIONAL` pending Stage 10 calibration (matrix), promoted from PROVISIONAL after Stage-10 sim pass 12/14.
- REDISCOVERED IN: single source (companion doc pair), but consumed identically by `character_canon_v30.md §3` and `npc_behavior_v30.md §1.2`.

**F-E-2 — Self-Other orientation as an orthogonal scalar (greed/altruism ≠ Conviction)**
- SOURCE: `conviction_taxonomy_v30.md` §2.3, §3
- CATEGORY: ontology / mechanism
- SUBSTANCE: A separate `[-1,+1]` scalar tracks *whom* an actor benefits, deliberately kept off the Conviction vector so two actors can share an identical Conviction profile (e.g. high Utility) yet play completely differently — "Cesare Borgia and a public-spirited republican magistrate may share a high Utility Conviction; what distinguishes them is for whom they instrumentalize." Mechanically: `attributed_outcome = raw_outcome × (1 − 0.5 × max(0, orient))` (self-aggrandizers only get partial credit toward faction Popular Support), and it drifts per season via `κ × Σ(self-benefit outcomes) − κ × Σ(collective-sacrifice outcomes)`, κ=0.03 default — an explicitly *emergent* corruption/redemption arc ("the Macbeth arc... emerging from accumulated outcomes rather than authored beats").
- WHY IT MAY STILL MATTER: A clean, reusable pattern for separating "what someone believes" from "whom they act for," with a stated emergent-arc payoff that doesn't require authored beats.
- STATUS IN DOC: CANONICAL/PROVISIONAL, formula flagged "future Stage 10 calibration may explore... bidirectional scaling."
- REDISCOVERED IN: single source.

**F-E-3 — Structured concentration + 8 cultural-background templates**
- SOURCE: `conviction_taxonomy_v30.md` §4–§5
- CATEGORY: derivation
- SUBSTANCE: An NPC's Conviction vector is not flat — 1–3 "primary" Convictions weighted 0.6–0.8 (the defining frame) plus a "cultural background" distribution weighted 0.2–0.4 drawn from one of 8 named templates (`varfell_alpine`, `crown_lowland`, `valorian_court`, `ecclesiastical`, `hafenmark_procedural`, `lowenritter_military`, `restoration_reformist`, `einhir_traditional`). Sim v2 found structured-concentration NPCs "produce smoother aggregate vectors and more interpretable armatures" than flat 13-way distributions, and it reduces authoring load: designer picks 1–3 primaries + a cultural label, engine fills the rest.
- WHY IT MAY STILL MATTER: Solves the "how does a designer author 40 NPCs without hand-tuning 13 numbers each" problem with a measured (not just asserted) authoring-cost reduction.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: single source.

**F-E-4 — Per-Conviction crisis model supersedes aggregate Scar counter (PP-718)**
- SOURCE: `conviction_track_v1.md` §2 (superseded taxonomy but canonical mechanic); `conviction_track_v1_pp718_vetting.md` (ratification)
- CATEGORY: mechanism
- SUBSTANCE: Under the legacy single-primary model, moral-injury "Scars" accumulated to one aggregate counter; crisis fired at 3+. PP-718 rewrote this so **each Conviction Scars independently** — a Cardinal with Faith+Authority+Honor primaries now needs 3 Faith-events *or* 3 Authority-events *or* 3 Honor-events, not any 3 combined. The vetting doc's own worked argument: aggregate told the engine "2/3 toward crisis" when in fact two of three primaries were untouched — multi-primary NPCs are *more* resilient, matching "the Habsburg-Catholic combination was load-bearing for Charles V's longevity." The crisis-table d6 (roll on the wounded axis) was also rewritten: roll 5 changed from legacy "Autonomy survival" to a Self-Other-orientation override, since Autonomy was renamed Liberty.
- WHY IT MAY STILL MATTER: A precise, well-argued fix for a real category error (collapsing a vector state back to a scalar at exactly the moment it's most interpretively significant) — the underlying critique generalizes to any multi-dimensional stress/wound system.
- STATUS IN DOC: `conviction_track_v1.md`: `[SUPERSEDED 2026-05-10 — PP-717]` for its §1 taxonomy, but "§2/§3 remain canonical." Vetting doc: "Overall: Class B vetting passes... 5+·5✓·1○·0−."
- REDISCOVERED IN: single source; internal self-correction (initial 7+/3✓ rating was later recalibrated to 5+/5✓ to avoid double-crediting PP-684).

**F-E-5 — Thread-witnessing → Conviction Scar trigger matrix (the world-to-belief seam)**
- SOURCE: `conviction_track_v1.md` §3
- CATEGORY: seam / mechanism
- SUBSTANCE: A per-event × per-Conviction table specifies exactly which Convictions Scar when an NPC witnesses a given Thread operation (e.g. "Dissolution of a living being" Scars Faith/Order/Reason/Equity(if powerless victim)/Precedent/Autonomy(if unwilling); "Mending a Gap" Scars nothing). Certainty level scales severity (±1 at C5/C0); capped at 1 Scar/season/NPC from witnessing; "Mending never produces Scars."
- WHY IT MAY STILL MATTER: This is the actual causal bridge from world-state events (a system explicitly out-of-lane) into personal belief-state (in-lane) — the concrete mechanism by which "the world acts on the person."
- STATUS IN DOC: canonical (ED-663/664).
- REDISCOVERED IN: single source.

**F-E-6 — NPC-NPC Relational Graph: six typed edges with a full Knot-mirrored lifecycle**
- SOURCE: `designs/npcs/npc_relational_graph_v30.md` §1–§4 (PP-724)
- CATEGORY: mechanism / ontology
- SUBSTANCE: Six canonical edge types between NPCs — sworn-bond, liege-vassal, kinship, patronage, rivalry, feud — each with directionality, strength 1–3, period precedent, a specific Resonant Style it activates (e.g. liege-vassal → Authority style; sworn-bond → Solidarity), and its own strain-capacity table (sworn-bond/liege-vassal 3/5/7 by strength; patronage 2/4/6). Kinship and feud explicitly **cannot** break by strain — they transition instead (cooperative→strained→severed-by-institutional-act, or escalate/de-escalate on a rivalry↔feud ladder) because "modeling [kinship] as breakable-by-strain misrepresents Renaissance kin-politics." Feud **auto-transmits along strong kinship edges on death** — named as "the load-bearing ROTK-style mechanic for emergent multigenerational narrative... without it, feuds dissipate at each death."
- WHY IT MAY STILL MATTER: This fills a gap the corpus itself names as pre-existing and real: "Faction emergence requires '2 NPC officers with Disposition +3' — the question of what officers feel about each other had no canonical answer." It's a complete, well-precedented (explicitly cites KOEI ROTK and CK3) social graph substrate.
- STATUS IN DOC: `PROVISIONAL — Class A canonical document`; strain/formation mechanics fully specified, four sub-parts (B1.2–B1.4) explicitly deferred.
- REDISCOVERED IN: single source, but architecturally derived wholesale from the Knot lifecycle (`fieldwork_v30 §5.6b`) — an explicit, acknowledged reuse, not independent rediscovery.

**F-E-7 — "Disposition must be derived, never stored" (explicit structural rule, applied twice)**
- SOURCE: `npc_relational_graph_v30.md` §4.7; `conviction_axis_matrix_v30.md` §6
- CATEGORY: derivation
- SUBSTANCE: NPC-NPC Disposition is computed live from the edge graph — `disposition = base + Σ(edge.strength_signed) − strain_pressure_penalty` — with the explicit rationale "Storing both edges + Disposition risks divergence; deriving from edges keeps the substrate single-sourced." Independently, `armature_position` (the 4-axis projection) is likewise never stored: "existing armature_position values recompute on next Accounting; no manual migration required (engine reads matrix at compute time)."
- WHY IT MAY STILL MATTER: This is exactly the kind of structural insight the brief calls out — "X must be derived, never stored" — articulated twice, in two separately-authored PPs (PP-684 and PP-724, nine days apart), converging on the same anti-desync principle.
- STATUS IN DOC: both canonical/decided (Decision Log entry in relational graph §13: "Derived vs separately tracked → Derived").
- REDISCOVERED IN: `conviction_axis_matrix_v30.md §6` and `npc_relational_graph_v30.md §4.7` — plausibly independent (different PPs, different authoring sessions).

**F-E-8 — Defection cascade with an explicit, bounded loop-safety argument**
- SOURCE: `npc_relational_graph_v30.md` §7
- CATEGORY: mechanism
- SUBSTANCE: When a sworn-bond/liege-vassal edge breaks, the shock propagates outward: tier-1 strain hits third-party edges *attenuated by hop-distance* (½ per additional hop); a "Fragility" stat (+1 per cascade-caused break, hard-capped at +3, decaying −1/season) lowers the sever-threshold for remaining faction members; the player can spend a "Suppress" action (−1 to a targeted node-cluster's sever check) to brake it; propagation advances at most one hop-ring per Accounting and hard-caps at tier-3. The doc states its own loop-safety verdict explicitly: "Net per-cycle gain < 1 ⇒ damped; reach and depth finite ⇒ bounded" — but flags this as a design argument, not sim-measured.
- WHY IT MAY STILL MATTER: A rare example in this corpus of a positive-feedback game mechanic (multi-officer defection cascades, the ROTK signature) designed *with its own termination proof attached*, including a player-facing lever to interrupt it — directly reusable as a template for any cascade/contagion mechanic.
- STATUS IN DOC: `[B1.2 — BUILT 2026-06-09, ED-1000; sim-tuning pending]`; magnitudes explicitly flagged `[NEEDS TESTING — SIM-DEFECT]`.
- REDISCOVERED IN: single source.

**F-E-9 — Geographic hop-distance strain scaling for NPC ties**
- SOURCE: `npc_relational_graph_v30.md` §6
- CATEGORY: seam / mechanism
- SUBSTANCE: Cross-territory relational strain scales by BFS hop-distance on the settlement-adjacency graph — same/adjacent ×1.0, 2-hop ×1.25, 3-hop ×1.5, 4+-hop ×2.0 — but only for "universal" strain triggers (background divergence); direct hostile-action triggers and rupture triggers explicitly do **not** scale ("the strain is bound to the event, not background ambient pressure"). Thread-witnessed ties bypass distance entirely if both NPCs have TS≥30. Officer reassignment fires a one-time strain "shock" (not a recompute) when hop-tier crosses a boundary.
- WHY IT MAY STILL MATTER: A worked seam between settlement geography (another lane's subject) and personal relational state, with the useful distinction "which trigger categories are geographic vs event-bound" already worked out and tabulated.
- STATUS IN DOC: `[Implemented PP-725/B1.4]`, worked examples "retuned PP-726."
- REDISCOVERED IN: single source.

**F-E-10 — Two distinct NPC decision architectures: local-conviction fork vs global priority tree**
- SOURCE: `npc_behavior_v30.md` §4.1 (lines 451–479), §8.1 (lines 768–782)
- CATEGORY: mechanism
- SUBSTANCE: Named NPCs in TTRPG mode use a 4-step **local** procedure: (1) Institutional Filter — what does the faction reward; (2) Conviction Filter — does it align with personal Conviction, if yes take it; (3) Decision Fork, resolved by *Scar count* (0 Scars → Conviction wins; 1 Scar → whichever Conviction the last Scar didn't address; 2+ → roll crisis table; Stability≤1 → survival overrides everything); (4) Resonant Style Interaction — **suspended if a PC is present and engages Contest**, meaning PC-facing decisions can literally pause on player action. Separately, faction-level Board-Game NPCs use a **global** 7-level priority tree evaluated against visible world stats (Stability≤2 survival, Conviction-critical threat, framework-aligned opportunity, institutional default, secondary Conviction, reactive, pass) with zero PC-presence dependency.
- WHY IT MAY STILL MATTER: Directly answers the brief's question — "can it see world state, or only what it perceives?" Answer: **both, at different scales**, cleanly separated. Personal-scale decisions are locally gated on scene-presence and PC Contest engagement; faction-scale decisions read global numeric thresholds with no perception model at all.
- STATUS IN DOC: CANONICAL (approved 2026-04-17).
- REDISCOVERED IN: single source, self-consistent across both modes.

**F-E-11 — Resonant Style: named structural vulnerability per NPC, mapped to argument types**
- SOURCE: `npc_behavior_v30.md` §1.3, `npc_behavior_v30_infill.md` (lines 20–24)
- CATEGORY: mechanism
- SUBSTANCE: Every named NPC has a primary + secondary "Resonant Style" (Evidence / Consequence / Authority / Solidarity) naming the *specific argument shape* that can move them, each tied to why their Conviction is vulnerable to it (e.g. Solidarity requires "an active Knot with the NPC" and only works via relational obligation). Secondary activates only after primary engagement fails ("escalation path"). This is the mechanical surface the social-contest system targets.
- WHY IT MAY STILL MATTER: A compact, reusable pattern for "how is this character persuadable" that's mechanically legible rather than pure GM adjudication.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: single source; consumed by both the Knot system (§4.5 corroboration) and the relational graph (edge-type → Resonant Style coupling), i.e. adopted as a load-bearing primitive across three independently-committed docs.

**F-E-12 — Arc Emergence as a threshold-driven branching state machine, not authored beats**
- SOURCE: `npc_behavior_v30.md` §5.1–§5.2 (Almud Arc Map A–F)
- CATEGORY: mechanism
- SUBSTANCE: Named-NPC arcs branch on measurable state crossings, not scripted triggers: Almud's Arc A ("The Reformer") requires *Certainty ≤ 1 AND Löwenritter Autonomy = Loyal simultaneously* — the doc explicitly notes this narrow AND-gate is deliberate: "reform from within is supposed to be the most demanding path... this is working as designed." Arc D/E/F (royal-assassination outcomes) are mutually exclusive by a single sub-roll. A separate "Constrained sub-arc" state (ED-586) suspends Mandate-costing arc behaviors when faction Mandate < 3 without altering Conviction/Resonant Style — only the priority sequence shifts, and progress/Scar-count persist through it.
- WHY IT MAY STILL MATTER: A concrete worked example of narrative-as-emergent-from-numeric-thresholds rather than flowchart authoring — directly reusable as a template for branching character arcs driven by legible player-visible variables.
- STATUS IN DOC: CANONICAL, with `[PROVISIONAL]` full-detail deferred to `arc_expansion_v1.md`.
- REDISCOVERED IN: single source; template reused identically for 5 named NPCs (Almud, Himlensendt, Baralta, Vaynard, Edeyja).

**F-E-13 — Named-NPC roster capacity/tiering as an explicit scalability solution**
- SOURCE: `npc_behavior_v30.md` §11 (lines 1217–1259); `character_canon_v30.md` §9
- CATEGORY: mechanism
- SUBSTANCE: NPCs are classified Active (full per-season tracking, soft cap ~35, companion-app primary surface) / Passive (~30, stable Disposition only) / Background (identity-only, unlimited). Demotion is priority-ordered (off-screen ≥4 seasons → low-inertia Disposition ≥4 seasons → faction removal → player-declared), and reversible. Inner-circle NPCs (23 total across 4 factions + Cardinals) are structurally exempt from demotion below Passive. A companion audit (`character_canon §9.2`) later found the ~14 Tier-3 NPCs fall *below* the prose-writer's stated minimum texture floor.
- WHY IT MAY STILL MATTER: Directly solves "how many NPCs can a persistent-state engine actually track," with a working answer (soft cap + reversible demotion) and an honest self-audit of where the answer under-delivers.
- STATUS IN DOC: CANONICAL (PP-661).
- REDISCOVERED IN: single source, later consumed/audited by `character_canon_v30.md`.

**F-E-14 — Knot system: Bonds gates eligibility, does not cap the bond itself**
- SOURCE: `designs/personal/knots_v30.md` §1–§2, §6
- CATEGORY: mechanism
- SUBSTANCE: A Knot (max relational depth, Disposition +5) requires Bonds ≥5 to *form* but Disposition itself is a flat −5..+5, not Bonds-scaled (explicitly corrected: ED-912 resolved a prior drift where two docs disagreed on this). Post-formation, relationship health is tracked on a bidirectional strain gauge (Distant: −2..+5, starts at 0; Close: −5..+5, starts at −2 "buffered") — positive strain is wear toward rupture, negative is resilience. Five distinct paid use-sites (remote Thread-read, Composure buffer, counsel extraction, Coherence anchoring, corroboration) each cost strain, with break (capacity exceeded) and rupture (5 immediate bypass triggers, e.g. public citation of private counsel) as separate end-states with different consequences.
- WHY IT MAY STILL MATTER: A fully worked relationship-depth economy (distinct from the graph in F-E-6, which explicitly imitates it) — reusable wherever a game wants "how deep can this bond get, and what does spending it cost."
- STATUS IN DOC: `## Status: CANONICAL — Pass 2g synthesis`; three internal contradictions were flagged and resolved (ED-912).
- REDISCOVERED IN: architecturally the *template* the relational graph (F-E-6) explicitly copies — acknowledged reuse.

**F-E-15 — Unified character-generation questionnaire: same schema authors PCs and NPCs**
- SOURCE: `designs/personal/character_generation_questionnaire_v30.md` §1–§4
- CATEGORY: derivation / ontology
- SUBSTANCE: One 12–16 question, 4-stage (Origin/Formation/Vocation/Catalyst) questionnaire derives the entire character-state object (Conviction weights, Self-Other, cultural template, skills, first Belief) for **both** PCs and NPCs — same questions, different answerer (player vs designer). Each answer produces not just a stat delta but a "textural hook" — a specific queryable memory/place/person the engine can later surface in prose. NPC→PC transitions (retiring into an NPC) inherit the NPC's hooks with a ~5-question "revision questionnaire." Explicit synthesis claim: "Convictions gate REACTIONS... Histories gate ACTIONS... the player never touches a stat sheet."
- WHY IT MAY STILL MATTER: A genuinely novel authoring-interface idea (derive mechanical state from narrative choice, uniformly across PC/NPC) that was never built — a real, well-argued proposal that could still be worth resurrecting independent of this engine.
- STATUS IN DOC: `## Status: DESIGN DIRECTION (not yet authored — direction confirmed, question set pending)`.
- REDISCOVERED IN: single source.

**F-E-16 — Companion vs Recruited-NPC: same relationship threshold, two different scale-tracks**
- SOURCE: `designs/npcs/companion_specification_v30.md` §1
- CATEGORY: ontology
- SUBSTANCE: Disposition ≥ +3 toward an NPC is the *single* eligibility gate, but the NPC can be activated at personal scale (Companion — travels with PC, persistent scene-level state, max 2 active, dedicated departure scene on ending) or faction scale (Recruited — operates within BG structure, ending is just "Mandate −1"), and the doc notes "a single NPC may be both" via the officer-governor path.
- WHY IT MAY STILL MATTER: Clean worked example of one relational threshold cleanly forking into two independently-tracked consequence-tracks at two different scales, rather than either merging them or duplicating state.
- STATUS IN DOC: CANONICAL.
- REDISCOVERED IN: single source.

**F-E-17 — The "Ruler Diamond": axis-positioned leaders + subjective blind-spot layer**
- SOURCE: `designs/npcs/npc_foils_v30_infill.md` (Part One: Axis Analysis; Part Two: Subjective Perspectives)
- CATEGORY: narrative
- SUBSTANCE: Four faction leaders (Almud, Lenneth, Baralta, Vaynard) are positioned on four shared political axes (settlement relationship, Einhir/caste stance, Church relationship, basis of authority); every pairwise conflict is derived from axis-distance rather than authored per-pair, with a named historical parallel per pairing (e.g. Almud↔Lenneth = "Manuel I Komnenos and Empress Eirene"). A second layer gives each ruler's *subjective, wrong* view of the other three, explicitly including a stated blind spot per view (e.g. "What Almud cannot see: that his uncertainty is itself a decision").
- WHY IT MAY STILL MATTER: A reusable two-layer technique — objective axis-map generates conflict pairs; subjective blind-spot layer generates dramatic irony — for any small cast of faction leaders.
- STATUS IN DOC: `## Status: DESIGN` (not ratified); `[EDITORIAL: characterization per ED-393–ED-401, provisional]`.
- REDISCOVERED IN: single source.

**F-E-18 — Deliberate NPC "flaws" as exploitable AI, and the BG↔TTRPG "Mode Bridge" doctrine**
- SOURCE: `designs/npcs/npc_roster_v30_infill.md` (Design Principle; per-NPC "Behavioral AI" entries; "Mode bridge" notes)
- CATEGORY: mechanism / narrative
- SUBSTANCE: Design Principle states every named NPC (bar Edeyja) carries "a structural compromise" that functions as "an emergent arc trigger" — e.g. Maret Uln's CONFLICTED flaw makes her hesitate 1 season against RM targets, which is explicitly "exploitable... opponents who recognise the pattern can predict when Varfell will fail to act." Separately, the "Mode Bridge" doctrine states a BG-layer numeric abstraction (e.g. a rising Deniability Debt) is *caused* by a TTRPG-layer personal decision (a Riskbreaker's aborted mission), and the Hybrid "Zoom In" mechanic is explicitly the player-facing mechanism for discovering that causal chain.
- WHY IT MAY STILL MATTER: Two related, transferable ideas: (a) author AI imperfection as content, not bug; (b) make a strategic-layer number causally traceable to a specific personal-scale decision a player can go find.
- STATUS IN DOC: `## Status: CANONICAL` (roster doc), Behavioral AI content flagged `[EDITORIAL: all... flagged for user review]`.
- REDISCOVERED IN: the "structural incentives, not individual malice" framing (npc_roster's caste finding) and Edeyja's "conflict-as-disturbance" cumulative-cost model (`edeyja_npc.md`) independently converge on the same idea — bad systemic outcomes emerge from uncoordinated actor behavior, not a villain.

**F-E-19 — NPC Recruitment procedure with a Hook (leverage) sub-mechanic**
- SOURCE: `npc_behavior_v30.md` §9.5 (lines 987–1044)
- CATEGORY: mechanism
- SUBSTANCE: A 4-step recruitment procedure (Identify → Approach → Offer → Resolve-by-degree) with Ob scaling to the NPC's current Disposition toward their faction (+4/+5 = not recruitable, a "genuine loyalty gate"). Weak/Strong Hooks (leverage) reduce Ob but burn on failure ("NPC goes public... recruiting faction takes Mandate −2"). Defection isn't a player roll — it fires automatically from the Priority Tree "when the Belief-contradiction condition is met."
- WHY IT MAY STILL MATTER: A complete worked economy for "poaching" NPCs across factions with proportionate risk/cost, distinct from and complementary to F-E-16's Companion track.
- STATUS IN DOC: CANONICAL (PP-642).
- REDISCOVERED IN: single source.

### DEAD ENDS

- **Legacy 9-Conviction taxonomy** (`conviction_track_v1.md §1`: Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity/Community/Warden) — `[SUPERSEDED 2026-05-10 — PP-717]`, replaced wholesale by the 13-Conviction set (F-E-1). Its §2/§3 mechanics survived (per-Conviction Scars), only the label set died.
- **Knot tier "Loose/Medium/Close" 3-tier model** (`complete_systems_reference` Part 8, PP-632) — struck by `knots_v30 §2` in favor of the "Distant/Close" bidirectional strain gauge; resolved by Jordan ruling ED-912, 2026-06-28 ("TIER-DRIFT-001... RESOLVED").
- **"Composure damage 5" citation** in `articulation_layer_v30 §2.4` — corrected to the canonical 4 per `fieldwork_v30 §5.6b` (COMPOSURE-DRIFT-001, resolved with the tier fix).
- **Niflhel's "Amoral Consequentialism" faction Framework Drift row** (`npc_behavior_v30 §7.1`) — "Ethical framework dissolved with faction (ED-757)"; the faction itself was struck from canon, taking its drift mechanic with it.
- **`character_canon_v30.md` PART B (actual per-NPC sheets)** — the consolidated schema (F-E group above) was fully specified but never populated: "PART B — NPC SHEETS pending Q1 scope decision (37 NPCs full vs Tiers 1+2 only)." A complete, load-bearing schema exists as a shell with zero authored content.

### OPEN QUESTIONS NEVER ANSWERED

- **Community vs Identity 4-axis collapse.** Both `conviction_taxonomy_v30 §2.2` and `conviction_axis_matrix_v30 §4.1` flag that these two Convictions project to near-identical 4-axis positions and recommend a 5th axis "if Stage 10 calibration finds the collapse load-bearing." No resolution found anywhere in this lane's corpus.
- **Baralta's cultural-template misfiling.** `character_canon_v30.md §11 D6`: `conviction_migration_roster_v30 §2.3` places Baralta (Hafenmark sovereign) under "Ecclesiastical Faction" with the `ecclesiastical` cultural template, contradicting her own faction. Explicitly flagged "Surface, do not fix... defer to Jordan" — no resolution found.
- **Relational-graph B1.2/B1.3/B1.4 full mechanics.** `npc_relational_graph_v30 §12`: defection-cascade resolution, faction-Cascade centrality-weighted integration, and settlement-coupling stress-testing are all "hook only," explicitly deferred, and their magnitudes are self-flagged `[NEEDS TESTING — SIM-DEFECT]` (not yet sim-measured, per §7/§8).
- **`conviction_track_v1 §3` Coherence-1 "Severed" strain value (TRUNC-DRIFT-001).** `knots_v30 §11` flags this row as "truncated in extract; full canon text needs verification" — no resolution found in this lane.
- **Character-generation questionnaire's opacity-vs-transparency and branching-vs-universal questions.** `character_generation_questionnaire_v30 §6` lists both as open items requiring a decision; the doc's own status ("DESIGN DIRECTION, not yet authored") confirms neither was ever settled.