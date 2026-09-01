## LANE F — WORLD, TERRITORY & SETTLEMENT

### COVERAGE
files_assigned: 40 | files_opened: 26 | files_read_closely: 14
skipped: solmund_voice_v30.md, solmund_philosophy_v30.md, solmund_artifacts_v30.md, solmund_master_document.md, narrative_voice_canon_v30.md — pure lore/voice per brief, no world rule found on a heading-level scan; character_histories_v30_index/_infill.md — PC lifepath creation, not NPC *behavior* (out of scope); calamity_radiation_v30_infill.md, geography_v30_infill.md, worldbuilding_canon_audit_v30_infill.md, southernmost_v30_infill.md — companion infill files, skeleton doc already carried the load-bearing tables; worldbuilding_canon_audit_v30.md, southernmost_v30.md, geography_v30.md (world/), march_layer_v30.md, event_deck.md, faction_systems_overview_v30.md, worldbuilding_v30.md — headings/key-sections only, superseded or peripheral to the five subjects; settlement_layer_v30_index.md, valoria_map_v30.svg, adjacency_map.jsx — indices/visualizations reconfirming data already extracted from primary sources.

### FINDINGS (ranked)

**F-F-1 — Settlement governance redesigned as AP-constrained "choosing under constraint," replacing 4 free stat-pumps**
- SOURCE: territory/governance_play_redesign_v1.md:4, :13, :31, :41-52
- CATEGORY: governance | mechanism
- SUBSTANCE: Diagnoses that the shipped design (`Develop/Fortify/Pacify/Administer`, one free action/season, `settlement_layer_v30 §3.2`) collapses governance to "roll one die a season." Replaces it with an **Administration Points** budget (`AP = 2 + FacilityTier_s`, range 2-5/season, non-carrying) spent across 8 verbs (Develop, Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate), each forcing a *method* choice that hands power to a different faction (e.g. Fortify via Garrison/Militia/Walls) so optimizing the stat costs politically.
- WHY IT MAY STILL MATTER: A complete, costed alternative to the currently-canonical 4-verb governance loop, explicitly diagnosing why the shipped version is mechanically thin.
- STATUS IN DOC: **PROPOSAL**, drafted 2026-06-22, "extends/replaces `settlement_layer_v30 §3.2`."
- REDISCOVERED IN: single source (built out fully in the goldenfurt_slice companion set, but that is an application, not independent rediscovery).

**F-F-2 — Legitimacy/Popular Support are per-SETTLEMENT, not per-faction; Mandate is a size-weighted saturating aggregate (Jordan ruling, supersedes prior canon)**
- SOURCE: territory/settlement_layer_v30.md:147-179 (§1.8)
- CATEGORY: ontology | derivation | governance
- SUBSTANCE: Jordan ruling (2026-05-30) explicitly **supersedes** the faction-level L/PS in `PP-686 v2`. L (0-7, slow/institutional) and PS (0-7, fast/populace) attach to the settlement. Settlement Weight `W_s = base(Type) + Prosperity_s + FacilityTier_s` (range 1-11) scales how much a settlement's acceptance counts. Faction Mandate `= clamp(round(7·T/(T+K)), 0, 7)`, K=6, where `T = Σ_s W_s·(q_s/7)` and `q_s = 0.5L_s+0.5PS_s` — a saturating form giving diminishing returns per settlement (one developed province of large settlements > many hamlets, but bounded 0-7 regardless of total holdings). Feedback is stabilizing: settlements ≥1 below Mandate drift L+1, ≥1 above drift PS−1, capped ±1/season. A 30-season sim is cited as converging without runaway.
- WHY IT MAY STILL MATTER: A fully-specified, numerically-anchored answer to "what makes a faction legitimate," derived bottom-up from the actual civic unit rather than authored abstractly — exactly the kind of structural insight ("X must be derived from the finest tier, not asserted at the coarse one") the brief flags as valuable independent of whether the code ever shipped it.
- STATUS IN DOC: canonical section of a doc marked `## Status: CANONICAL`; the ruling itself is dated and attributed, not marked provisional.
- REDISCOVERED IN: single source, but note it explicitly overturns three other docs' prior model (`faction_behavior_v30`, `faction_state_authoring_v30`, `faction_canon_v30`) — a corrected convergence rather than an independent one.

**F-F-3 — Political hierarchy corrected through three iterations to fix a granularity error conflating siege-targets with sub-features**
- SOURCE: territory/valoria_political_hierarchy_v30.md:1-11, §1.1 (L29-42), §2.3 (L68-72)
- CATEGORY: ontology | derivation
- SUBSTANCE: PP-726 establishes `Valn(geography) → Kingdom → Duchy(3) → Province(14) → Territory=Settlement(35+2 special)`, with the settlement as the sole siege-target and everything else (districts, garrison towns, mines, watchtowers, shrines — 22 of the old 36 "settlement" entries) collapsed into **sub-features** of a parent settlement, non-siegeable and non-adjacent-graph-participating. This corrects **two prior attempts** at the same problem: PP-666/ED-710 (placeholder), then PP-723 (49 edges/36 nodes, still wrong granularity — mixed siege-targets with districts), superseded by PP-726 (56 edges/37 nodes, correct). Provinces are also **state-machines**: a province whose settlements split faction-alignment "fractures" into named sub-provinces (north/south or east/west), symmetric on reunification (§2.3).
- WHY IT MAY STILL MATTER: The three-attempt history is itself the lesson — "settlement" is a genuinely hard atomic unit to define correctly, and the failure mode (conflating a city with its watchtower) is a concrete trap for any future spatial-schema rewrite. The province-fracturing state-machine is a distinct, un-costed mechanic (see Open Questions).
- STATUS IN DOC: Class A, **PROVISIONAL** substrate canon (per the doc's own header); it supersedes PP-666/ED-710/PP-723 outright.
- REDISCOVERED IN: `settlement_layer_v30.md` Part 2 (§2.1-2.3) is the same PP-726 ruling applied to the sibling doc — not independent, but shows the ruling required rewriting the registry, the adjacency graph, AND the governance doc simultaneously.

**F-F-4 — The Goldenfurt vertical slice: a full end-to-end play loop worked out to the level of exact card responses and Ledger writes**
- SOURCE: territory/goldenfurt_slice/{npc_cast.md, event_deck.md, sim_build_spec.md}
- CATEGORY: mechanism | npc | governance
- SUBSTANCE: 6 fully-specified NPC dossiers (goal/method-escalation/timeline/fires_card/autonomous-advance/leverage/trajectory) wired into a 28-card pressure-driven deck (7 families: Petition/Friction/Opportunity/Crisis/Intrigue/Ambition/Thread) and an implementable sim spec (dataclasses, a Π homeostat, an ambition tick). The collision map is deliberate: Hedda (law, β-conduct) vs Orsk (commerce, α-outcomes) is the central rivalry; every `Hold Court` ruling pleases one and wrongs the other; Hedda's secret (sheltering her smuggler brother Tomas) is her exploitable point of failure.
- WHY IT MAY STILL MATTER: This is the single most concrete "here is exactly how it has to work" artifact in the whole corpus — a reference implementation a future engine build could port near-verbatim, including its own bug list (below).
- STATUS IN DOC: **PROPOSAL**, 2026-06-23; explicitly "content + spec only; none of it runs" until the settlement registry (S0) lands.
- REDISCOVERED IN: single source (a deliberately-built worked example, not independent).

**F-F-5 — Adversarial verification found a mis-signed pressure formula and a "no-acceptable-out" vise, both fixed in-doc**
- SOURCE: territory/goldenfurt_slice/verification_findings.md:13, 26 (CG-1, deck-F3)
- CATEGORY: problem-only | mechanism
- SUBSTANCE: A 4-lens skeptic pass (deck-balance / NPC-collision / churn-integrity / sim-completeness) found the Π-pressure decay term `-decay_toward(3)` was **mis-signed** — it only pulled pressure *down*, pinning a quiet settlement toward Π=0 and contradicting the design's own anti-stall claim; fixed to a bidirectional `sign(3-Π)·min(1,|3-Π|)` restoring term. Separately, a Church "Curate's Offer" card (G204) was found to be a true no-acceptable-out vise (every branch either raises pressure or feeds an escalation chain) — fixed by adding a secular relief option.
- WHY IT MAY STILL MATTER: A concrete, generalizable methodology finding: a homeostat/pressure-release formula needs its *sign* checked adversarially, not just its magnitude — the same class of defect the wider repo's `§0.1` measurement-discipline rules were later written to catch, independently discovered here a month earlier and inside actual game content rather than process apparatus.
- STATUS IN DOC: ✅ fixed in commit (CG-1); ✅ fixed in v1.1 (deck-F3).
- REDISCOVERED IN: single source.

**F-F-6 — Territorial neglect (not conquest) is a canonical path to insurgency; dissolution favors historically-modal outcomes over "player wins forever"**
- SOURCE: world/insurgency_pipeline_v30.md:107-116 (§4.1), 229-252 (§6.2-6.3)
- CATEGORY: world-churn | mechanism
- SUBSTANCE: An Insurgency forms when **2+ contiguous territories sit Uncontrolled for 2 consecutive seasons** — pure neglect, no faction action required, distinct from the separate RM-specific Latent-influence trigger (WA≤−2 AND ≥3 territories PT≤1 AND MS≤50). Per Jordan ruling ED-881 (2026-05-29), dissolution follows **RAND's *How Insurgencies End*** precedent (89 cases): military defeat, **sponsor withdrawal** (the RAND-strongest predictor — an external backer collapsing/defecting starves the insurgency's legitimacy even with territory intact), negotiated amnesty, or persistent stalemate — evaluated in that priority order each Accounting, replacing an earlier version that "could previously only escalate, never represent the modal real outcome of insurgent defeat" (§6.3).
- WHY IT MAY STILL MATTER: This is the clearest answer in the corpus to "does the world model decay from neglect" — yes, explicitly, at the territorial-control layer, with a citation-backed defeat model. It is a genuinely separate mechanism from the faction-emergence ladder (§F-F-9 below).
- STATUS IN DOC: **CANONICAL**; §6.2/§6.3 marked **RATIFIED (ED-881, 2026-05-29, Jordan-directed)**.
- REDISCOVERED IN: single source.

**F-F-7 — World trajectory (MS 0-100) modeled as three additive forces with asymmetric hysteresis at band edges**
- SOURCE: world/ms_trajectory_v1.md:20-28 (§2), 89-107 (§5.1)
- CATEGORY: world-churn | mechanism
- SUBSTANCE: Substrate integrity (MS) is driven by Force 1 (baseline continuity, decelerating, positive), Force 2 (Warden Mending, positive, front-loaded — Wardens were strongest right after the Catastrophe and have declined ever since under Church prophylaxis), Force 3 (rendered-world violence, always negative, always shallow — wars/revolts can only notch MS, not collapse it). Band crossings (Critical/Fractured/Fragile/Strained/Stable at MS 20/40/60/80) are **hysteretic**: the falling (collapse) edge and the rising (recovery) edge differ by +8 MS — a substrate that fell into Fractured at MS 20 must climb back to MS 28, not 20, to recover — ratified against real regime-shift ecology (Scheffer/Holling) precedent, plus a leading-warning-signal window (12 MS) before a tip.
- WHY IT MAY STILL MATTER: This is the one clean, quantified model in the corpus of "the world getting better or worse over time" with an explicit non-repairing philosophical constraint (P-07: the substrate does not heal itself, humans/Wardens restore it) and a real hysteresis mechanic — directly answers the brief's "world trajectory" question.
- STATUS IN DOC: **CANONICAL** with 2 flagged provisional gaps (§8); §5.1 hysteresis **RATIFIED (ED-882, 2026-05-29)**.
- REDISCOVERED IN: single source; the underlying node-distance map is independently cross-used by `calamity_radiation_v30.md` (same table, different doc).

**F-F-8 — Radiation effects creep inward from the periphery: frontier outposts feel Calamity decay first, the Seat last**
- SOURCE: world/calamity_radiation_v30.md:20-31
- CATEGORY: world-churn | derivation
- SUBSTANCE: Within a province, settlement type modulates *when* an MS-band effect manifests: Outposts near Askeheim feel it one band **earlier** than province level; Fortress/City/Seat feel it one band **later** (institutional buffer); Cathedral gets a population-Certainty buffer but no physical-substrate buffer. Explicit framing: "radiation creeps inward from the periphery. Frontier outposts fall first. The Seat is the last to feel the Catastrophe's reach."
- WHY IT MAY STILL MATTER: A compact, reusable rule for how decay should propagate spatially through any settlement hierarchy (periphery-first) — a pattern independent of the specific Calamity fiction.
- STATUS IN DOC: **CANONICAL**, approved 2026-04-06.
- STATUS: single source.

**F-F-9 — Faction emergence/collapse is symmetric: bottom-up (Cell→Hegemon) and top-down contraction (Faction→City-state→dissolution), never simple deletion**
- SOURCE: territory/settlement_layer_v30.md:602-663 (§6.2-§6.3)
- CATEGORY: faction | world-churn
- SUBSTANCE: A 5-stage emergence ladder (Cell→Organization→Movement→Faction→Hegemon) ties directly to settlement-count/province-Seat thresholds and Renown. Collapse is the exact mirror: losing all provinces does not delete a faction — if its leader survives in a personally-controlled settlement, it becomes a **city-state** (partial stat sheet: Influence/Wealth/Stability, no Mandate/Military) that can attempt re-emergence via the same Stage 2→4 pathway. Worked examples given for Hafenmark (Baralta retreats to Gransol) and the Crown (Almud exiled to Stillhelm after a Löwenritter coup).
- WHY IT MAY STILL MATTER: A clean, symmetric state-machine for faction lifecycle that treats "losing everything" as a contraction to be rebuilt from, not a terminal state — directly reusable regardless of whether the specific stat thresholds survive.
- STATUS IN DOC: **CANONICAL**, approved 2026-04-17.
- REDISCOVERED IN: single source; structurally parallel to (but distinct from) the Insurgency pipeline's own 4-stage ladder (F-F-6) — two independently-authored faction-lifecycle models in the same corpus that were never reconciled into one (see Open Questions).

**F-F-10 — Settlement's three derived-value formulas, independently confirmed by the UI spec**
- SOURCE: territory/settlement_layer_v30.md:41-49 (§1.3); ui/valoria_ui_ux_supplement_derived_settlement.md:58
- CATEGORY: derivation | settlement
- SUBSTANCE: Local Economy = `Prosperity × 50` (feeds faction Treasury); Garrison Strength = `Defense × 20 + FortLevel × 30`; Public Order = `Order × 20` (below 0 triggers riot events). Stored stats stay 0-5; these are pure display/derived multipliers, never separately stored.
- WHY IT MAY STILL MATTER: Directly answers the brief's ask for the exact DERIVED list; both a mechanics doc and an independent UI-implementation doc name the identical three values and formulas, which is real (if weak) corroboration they were load-bearing rather than aspirational.
- STATUS IN DOC: **CANONICAL**.
- REDISCOVERED IN: `ui/valoria_ui_ux_supplement_derived_settlement.md` §Part3 (detail panel shows "Local Economy, Garrison Strength, Public Order") — same three names, same doc family (`derived_stats_v30 §3.3`), so a genuine cross-check rather than a coincidence.

**F-F-11 — Province Accord is explicitly DERIVED (floor of mean settlement Order), never stored at province level**
- SOURCE: territory/settlement_layer_v30.md:46-49
- CATEGORY: derivation
- SUBSTANCE: "Province Accord is now the floor of the average Order across all settlements in the province... Province Accord emerges from settlement governance rather than being set directly." Worked example given (Order 4,2,1 → Accord 2). Existing province-level Accord-change rules are redefined to modify settlement Order and let it cascade upward.
- WHY IT MAY STILL MATTER: A textbook instance of exactly the structural principle the brief calls out by name ("X must be derived, never stored") — applied concretely with a formula and worked example, not just asserted.
- STATUS IN DOC: **CANONICAL**; also independently listed as **RESOLVED** in Part 9 open-items (ED-SETT-03, with tie-break rule: Seat gets +1 weight on ties).
- REDISCOVERED IN: `settlement_adjacency_v30.md §2.3` cites the same formula by reference (not independent, but shows it propagated correctly to a sibling doc).

**F-F-12 — Church infrastructure grows through helpfulness, not conquest ("the Geneva trap")**
- SOURCE: territory/settlement_layer_v30.md:105-135 (§1.5-§1.7)
- CATEGORY: governance | world-churn
- SUBSTANCE: Church presence is four independent axes (Religious Building tier / Templar Station / Inquisitor Base / Church Governor) that stack, not a linear ladder. Crucially, a Chapel gives +0.5 Order/season to *any* governor who hosts it, secular or not — "a Crown governor who permits a Chapel... benefits from the social cohesion the parish provides — but also accepts the PT generation that comes with it." A **Pastoral Assumption** rule lets the Church auto-install a governor in any ungoverned settlement with a Chapel (Ob 1). Explicit historical grounding cited: Papal States, Calvin's Geneva, 1979 Iran — "theocracies grew not through hostility but through helpfulness."
- WHY IT MAY STILL MATTER: A genuinely non-obvious institutional-capture mechanic — makes accepting help itself the vector of loss of control, which is more interesting than a Church-vs-Crown war mechanic and ties directly into the Goldenfurt slice's Wessel NPC (Church curate angling for exactly this).
- STATUS IN DOC: **CANONICAL** (marked NEW at authoring, sourced from `historical_precedents_analysis §1.4`).
- REDISCOVERED IN: `territory/goldenfurt_slice/npc_cast.md` NPC-G03 (Wessel's whole arc *is* this mechanic played out) — independent application confirming the mechanic reads as intended in play.

**F-F-13 — Institutional Facility slots are finite, creating structural pressure toward succession, exile, or formal expansion**
- SOURCE: territory/settlement_layer_v30.md:67-97 (§1.4)
- CATEGORY: governance | mechanism
- SUBSTANCE: Seat settlements have exactly 3 Wing slots (Standing-6+ residency); when full and a 4th claimant arrives, the *only* outcomes are an existing holder departing (death/exile/succession), the settlement spending Treasury to expand capacity (+1 Wing/settlement/decade cap), or the claimant accepting a "Prince-in-Waiting" provisional rank requiring a recurring social contest to maintain. Cross-faction Wings at composite-control Seats (e.g. a Church district inside Crown territory) belong to the district's direct controller, not the province controller, and can be ceded as treaty concessions.
- WHY IT MAY STILL MATTER: A scarcity mechanic that manufactures political conflict (someone must lose their seat) rather than requiring the GM/AI to invent one — directly reusable as a pressure-generator for any court/seat system.
- STATUS IN DOC: **CANONICAL** (PP-661).
- STATUS: single source.

**F-F-14 — Territory-level temperament (α/β) and NPC-level ethic are the same axis at two grains**
- SOURCE: territory/territory_temperaments_v30.md:10-20, §2; territory/governance_play_redesign_v1.md:166, 248
- CATEGORY: ontology | npc | world-churn
- SUBSTANCE: `territory_temperaments_v30` authors a 5-point α(outcomes)/β(conduct) typology per province (pragmatic 0.7/0.3 → outcomes-only 0.9/0.1), tied to geography and drifting toward outcomes-only under `env.peninsular_strain_shock`. `governance_play_redesign_v1` explicitly reuses the identical axis as an NPC-level `ethic` field ("already canon at territory grain, now applied at NPC grain" §5.1) — every Goldenfurt NPC dossier carries an α or β tag that determines their escalation ceiling (e.g. Hedda is β and will "never" turn violent).
- WHY IT MAY STILL MATTER: A single scalar axis composed across two different scales (population culture ↔ individual character) is exactly the kind of cross-scale primitive the wider repo's design philosophy (bottom-up composition, no scale-local dialects) values — and here it demonstrably worked, in two independently-authored docs.
- STATUS IN DOC: territory doc **CANONICAL** header but self-contradicts to "PROVISIONAL pending Stage 10 calibration" at its own footer (§6) — treat the numeric weights as provisional even though the doc's own status line says canonical.
- REDISCOVERED IN: `governance_play_redesign_v1.md §5.1` — genuine independent reuse of the same axis at a different grain, not a copy.

**F-F-15 — A national-scale governance-crisis mechanic (Motion of No Confidence + Church veto) exists independently of, and unreconciled with, the settlement-scale governance redesign**
- SOURCE: world/worldbuilding_v30.md:179-192 (§6.2-§6.3)
- CATEGORY: governance | seam
- SUBSTANCE: Parliament can raise a Motion of No Confidence (Influence vs Crown Mandate); the Confessor (Church) can concur or refuse. Concurrence → deposal (Crown Mandate→1, Stability−3, succession chain to Torben or interregnum). Refusal → Church Influence+3, Thread Tension+2. Explicitly noted: "the deposal clause gives the Church structural veto over regime change." A "Constitutional Crisis" event card auto-triggers this when Crown Mandate hits 1 or 3+ territories are lost in a season.
- WHY IT MAY STILL MATTER: This is a *national*-scale deposal mechanic, while `governance_play_redesign_v1`'s AP/verb/deck system operates purely at *settlement* scale and never references it. Neither doc cites the other. If both were built, a player-governor's settlement-level "Defy" choices (which raise national Suspicion, per governance_play_redesign §1.4) have no stated connection to whether *this* national no-confidence mechanic ever fires — a real cross-scale seam nobody has closed.
- STATUS IN DOC: listed as "New Mechanic — All Modes," no supersession marker found.
- REDISCOVERED IN: single source (the absence of cross-reference IS the finding).

**F-F-16 — Cognatic senior succession is settled canon across all three duchies**
- SOURCE: world/worldbuilding_v30_infill.md:57-58 (§7.3)
- CATEGORY: governance | world
- SUBSTANCE: "All duchies follow cognatic senior succession — eldest child inherits regardless of gender." Named consequence: Elske is a legitimate Crown succession candidate.
- WHY IT MAY STILL MATTER: Small but load-bearing — settles a succession-eligibility question that any dynastic/generational-shift mechanic (`settlement_layer §7.1-7.2` Generational Shift clock) needs and would otherwise have to invent per-NPC.
- STATUS IN DOC: no explicit status marker on this line; doc-level header says the parent skeleton is CANONICAL.
- STATUS: single source.

**F-F-17 — The canonical geography YAML contains a live, unresolved internal contradiction: the same settlement IDs mean different places in two blocks of one file**
- SOURCE: territory/valoria_geography_v30.yaml:243-249 (old `settlements:` block, S-006 = "Lowenskyst Fortress") vs. :615 (new `settlement_adjacency:` block, S-004/S-005/**S-006** = the Kronmark intra-province triangle, i.e. S-006 = Goldenfurt per `settlement_layer_v30.md:150`)
- CATEGORY: problem-only
- SUBSTANCE: The file's old 36-entry `settlements:` dict (pre-PP-726, superseded per its own header comment at L537 "PP-726 supersedes PP-723") was never updated when the new PP-726 `settlement_adjacency:` block was added beneath it in the *same file*. Both blocks are live in the working tree; the old block's S-006 and the new graph's S-006 name different real-world places, and nothing in the file itself flags the collision.
- WHY IT MAY STILL MATTER: A concrete contamination hazard for any tool or reader that queries `settlements:` for a name instead of resolving through `settlement_layer_v30 §2.1` — exactly the kind of stale-but-live data the brief warns downstream analysts to watch for.
- STATUS IN DOC: the old block carries no retirement/superseded marker of its own; only the new block's header comment declares the supersession.
- REDISCOVERED IN: cross-checked directly against `settlement_layer_v30.md §2.1` (Kronmark province table, S-006=Goldenfurt) — confirmed by disagreement, not agreement.

**F-F-18 — Insurgency starting stats and post-promotion status rules are the pipeline author's own guesses, flagged as such**
- SOURCE: world/insurgency_pipeline_v30.md:128-130, 175-177, 259-260
- CATEGORY: problem-only | faction
- SUBSTANCE: The doc is unusually honest about its own gaps: Insurgency starting Influence/Stability/Wealth/Military values are "[PROVISIONAL: ... not specified in GD-3; ... Pass 2i derivation. Forward-flag INSURGENCY-STATS-001]"; the rule that a Promoted Faction's parliamentary status is permanent regardless of later PT shifts is likewise "Pass 2i derivation... Forward-flag INSURGENCY-STATUS-MUTABILITY-001"; the unidirectional (never-demotes) suppression model is "Forward-flag INSURGENCY-DEMOTE-DIRECTION-001."
- WHY IT MAY STILL MATTER: Three specific, precisely-named open decisions a future implementer needs to either ratify or revisit — not vague TODOs but exact forward-flag IDs tied to exact clauses.
- STATUS IN DOC: **PROVISIONAL** (each flagged individually); the doc overall is CANONICAL.
- STATUS: single source.

### DEAD ENDS

- **Old 26-territory / 36-settlement adjacency data superseded twice over.** `territory/settlement_adjacency_v30.md` §1.2 presents PP-723's 49-edge/36-settlement graph as canonical, but the same doc's own banner (L1-6) says it is "PARTIALLY SUPERSEDED post PP-723," and the graph it describes is itself superseded again by PP-726 (56 edges/37 settlements) in `valoria_geography_v30.yaml`. The doc carries three different status claims in one file ("PARTIALLY SUPERSEDED" banner / "## Status: CANONICAL" heading / "**Status:** PROVISIONAL" body) — none of them reflect the current PP-726 state. Do not cite this doc's §1.2 numbers.
- **`Almaic Kyriakos`** — flagged in `worldbuilding_canon_audit_v30.md` §7 as "Appears NOWHERE in Canon" despite being referenced in `worldbuilding_v30.md §3.6`; treat as a dangling reference, not established lore.
- **Territory-level temperament weighting** — `territory_temperaments_v30.md §3` computes per-faction aggregate temperament via *uniform* weighting across territories "deferred to Stage 10 sim calibration," and the doc's own §6 sign-off calls the whole authoring "PROVISIONAL pending Stage 10 sim verification" despite its header claiming `## Status: CANONICAL`. Treat the specific α/β numbers as placeholders, not calibrated values.
- **MS trajectory's Himmelenger "R-7" theological-favour explanation** — `ms_trajectory_v1.md §8 Gap 2` explicitly states the Church's claim that Himmelenger's long substrate-clean status is Solmund's grace is a **misattribution** (actual cause: node distance + Solmund's travel route); the alternate framing that the Altonian containment grant genuinely gifted the Church stability "is not adopted here." Don't resurrect the theological explanation as mechanically true.

### OPEN QUESTIONS NEVER ANSWERED

- **Political-value scalars are structural but unquantified.** `valoria_political_hierarchy_v30 §2.4/§5`: the formula `political_value = Σ(territory_value) + Σ(province_unification_bonus)` is canonical in shape, but `territory_value` per settlement-type and the unification-bonus magnitude are explicitly "TBD pending balance pass" — no file in this lane resolves them.
- **Province-fracturing trigger/reunification thresholds.** `valoria_political_hierarchy_v30 §2.3/§5`: the rule (province splits when constituent settlements disagree in faction alignment) is stated, but "specific event triggers and reunification thresholds not yet specified."
- **ED-055 naval-scope expansion** for Schoenland's additional sea routes — flagged open in three separate files (`valoria_political_hierarchy_v30 §5`, `settlement_layer_v30 §2.1`, `march_layer_v30 §6`) and never closed in this corpus.
- **Askeheim healing path / duchy assignment** — if Askeheim heals enough to support settlements, which duchy it joins is explicitly "undecided" (`valoria_political_hierarchy_v30 §5`).
- **Governance redesign's own open balance questions** (`governance_play_redesign_v1 §5.3`): whether the 2-5 AP curve is tight enough, Π-homeostat tuning, and — most concretely — a target of "~8-12 cards per family × settlement-type modifiers ≈ 60-100 base cards + chains" vs. Goldenfurt's single 28-card deck; no other settlement type's deck exists anywhere in this lane.
- **Two independently-built faction-lifecycle ladders never reconciled** (F-F-9 vs F-F-6): `settlement_layer_v30`'s player-driven Stage 1-5 emergence ladder and `insurgency_pipeline_v30`'s world-driven 4-stage pipeline overlap in subject (both describe "a group becomes a faction") but use different stat baselines, different thresholds, and neither cites the other.
- **The national Motion-of-No-Confidence mechanic's relationship to settlement-level Suspicion** (F-F-15) — never addressed by either source doc.
- **Colonial revolt specification** (`ms_trajectory_v1 §8 Gap 1`) — 3-5 unnamed revolts assumed in the trajectory math, never authored.