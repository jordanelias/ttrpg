## LANE K — EMERGENT NARRATIVE, ARCS & ARTICULATION

### COVERAGE
files_assigned: 48 (39 in `arcs/`, 1 `articulation/`, 5 `audit/2026-06-28-narrative-state-articulation/`, 3 `audit/2026-06-28-distillation-coherence/`)
files_opened: 24
files_read_closely: 16 (full text: `emergent_arcs_experimental.md`, `emergent_campaign_arcs.md`, `emergent_scenarios.md`, `articulation_layer_v30.md`, all 4 narrative-state-articulation docs, `open_decisions.md`; substantial portions: `narrative_scenario_chains.md`, `throughline_resolutions_v30.md`, `arc_expansion_v30.md`, `arc_narrative_analysis.md`, `gm_ref/arcs_01_04.md`, `gm_ref/arcs_46_55_resolved.md`)
skipped: `verification_addendum.md` (distillation audit's own supersession corrections; not narrative-bearing) · 10 of 12 individual arc-batch files (`arcs_16_19` through `arcs_46_55` unresolved, ~arcs 5–45) plus their index twins — sampled early (01–04), late-resolved (46–55), and the cross-batch meta-analysis instead, per the triage instruction · ~85% of `arc_expansion_v30.md` body (Parts II–IV: dozens of per-NPC arc-profile fills beyond the one Almud example read for structure) — the methodology section (Part I) and one worked profile fully establish the canonical pattern; the remainder is repetition of that pattern across NPCs · body of `distillation_coherence_report.md` beyond its executive summary and a targeted grep (its content is Key-substrate/resolver taxonomy hygiene, correctly out-of-scope per the combat/tooling exclusion, except the one finding below that is directly narrative-load-bearing).

### FINDINGS

**F-K-1 — The three-tier articulation architecture (PP-688)**
- SOURCE: `articulation/articulation_layer_v30.md` §1–§4
- CATEGORY: mechanism
- SUBSTANCE: The Key log records what *happened*; articulation determines what the player *experiences as story*, via three tiers: Tier 1 is an always-on "protagonist UI lens" (Concern queue, memory salience, Bonds/Knot/Belief/Inspiration registers) with zero prose generation; Tier 2 is a 10-condition trigger ruleset (scar acquired, coup attempted, contested succession, mission shift, exposed covert betrayal, knot formed/ruptured, severe peninsular strain, cross-faction cascade clustering, belief revised) that fires 5–15s "cut scenes" scored by a significance function (`stakes_weight + protagonist_alignment + cascade_event_weight + accumulated_narrative_weight`, range 0–13); Tier 3 is an annual omniscient-voice chronicle over top-N Keys by a parallel universal-track significance function. §10: "PP-688 raises full-engine story-fraction estimate to ~75–85% (substrate alone produces ~15%)."
- WHY IT MAY STILL MATTER: This is the single most complete answer in the corpus to "how does machine state become readable narrative" — a fully specified, numerically parameterized pipeline, not a vague aspiration.
- STATUS IN DOC: Self-contradictory — see DEAD ENDS.
- REDISCOVERED IN: single source (but is the substrate the 4 narrative-state-articulation audit docs build on).

**F-K-2 — Accumulated narrative weight: an anti-starvation guarantee**
- SOURCE: `articulation/articulation_layer_v30.md` §3.3
- CATEGORY: mechanism
- SUBSTANCE: Every un-articulated Key adds its `stakes_weight` to a per-actor/per-faction counter that resets only when a cut scene featuring that actor fires. Effect: an NPC or faction that keeps generating only low-stakes Keys eventually has an ordinary Key push their accumulated weight over a threshold and trigger a cut scene anyway — narrative attention is guaranteed to circulate, not just accrue to whoever is loudest that season.
- WHY IT MAY STILL MATTER: A small, general, reusable answer to a real problem (narrative starvation of background actors) independent of whether the rest of PP-688 survives.
- STATUS IN DOC: same header ambiguity as F-K-1.
- REDISCOVERED IN: single source.

**F-K-3 — The Key substrate as narrative graph + single update rule**
- SOURCE: `audit/2026-06-28-narrative-state-articulation/00_key_io_review.md` §2, §5
- CATEGORY: ontology
- SUBSTANCE: Every consequential change is a typed, append-only Key with universal fields (`causes[]`, `targets[]`, `scale_signature`, `symbolic_dimensions`, `visibility`, `permanence`). One update rule mutates state: validate → append → resolve observers via `armature · symbolic_dimensions · impact_vector` → apply `stat_deltas` under strict bucket discipline (pool/derived_value/track/clock) → propagate cross-scale via Domain Echo → update the causal graph. §5: "The Key log is a normalized narrative graph: nodes = actors/factions/territories/artifacts; edges = Keys... structurally identical to Dwarf Fortress's `history_event` model."
- WHY IT MAY STILL MATTER: This is the substrate every articulation and arc mechanism in the corpus is built on; the DF parallel is independently verified by an external prior-art survey (F-K-6), which is a strong signal it's the right abstraction.
- STATUS IN DOC: ANALYSIS (review of canon, no canon edited).
- REDISCOVERED IN: `03_articulation_nlg_architecture.md` §10 ("no new required Key fields anticipated" — the metadata is already sufficient).

**F-K-4 — Canonical NPC arc structure: a three-state machine driven by 8 conditioner types**
- SOURCE: `arcs/arc_expansion_v30.md` lines 1–53 ("PART I: METHODOLOGY REFERENCE")
- CATEGORY: ontology
- SUBSTANCE: "Methodology: Follows npc_behavior_v30 §5 Arc Emergence State Machine. Each arc has: (A) default, (B) branch-condition transformation, (C) crisis/collapse." Every arc profile defines a branch condition (game-state trigger), a Conviction shift, a Resonant Style shift, a behavioral consequence, and a risk. Conditioners are typed: Scar-based, Environmental (world-track thresholds), Political (faction stat events), Relational (Knot/Disposition), Generational, Cross-NPC, Thread-state, Obligation.
- WHY IT MAY STILL MATTER: This is the corpus's most precise, load-bearing answer to "what is an arc, structurally": a *named state label owned per-NPC* (A/B/C), whose *transitions* are recognized over state other systems own (world clocks, faction stats, other NPCs' arc states). Ownership and recognition are split, not conflated.
- STATUS IN DOC: **CANONICAL — approved 2026-04-17**, but a 2026-04-19 in-file override strikes the Niflhel-specific sections and requires Coup-Counter-based conditioners be re-derived against the 4-stage Löwenritter autonomy replacement ("arc structure remains valid as illustration; translate mechanics").
- REDISCOVERED IN: single source for the canonical formalism (worked independently, in looser form, by the illustrative docs in F-K-5).

**F-K-5 — "How Arcs Emerge": five parallel mechanical engines, no scripted plot**
- SOURCE: `arcs/emergent_campaign_arcs.md` lines 8–18
- CATEGORY: mechanism
- SUBSTANCE: "Valoria has no scripted plot. Arcs emerge from five mechanical engines running in parallel": the three clocks (Mending Stability/Church Influence/Institutional Pressure), seasonal accounting, NPC trigger conditions, 9 political axes, and Thread operations + co-movement. "The same seed produces different arcs depending on player choices at each branch." Four worked arcs (coup nobody triggered, a Vaynard relationship that raises the very clock it needs to suppress, Niflhel's Thread-harvesting side effect draining the world, Axis 9 going public) each require ≥3 independent systems converging with no single actor's intent explaining the outcome.
- WHY IT MAY STILL MATTER: This is the campaign-scale complement to F-K-4's per-NPC state machine — it names the mechanism by which *system-level* arcs (not owned by any one NPC) arise.
- STATUS IN DOC: Illustrative (Checkpoint-14-derived, "Pre-release reference tool"); the document itself carries a 2026-04-19 note that Arc 1 (Löwenritter Autonomy) and Arc 3 (Niflhel) "reference dissolved systems... remain as pre-dissolution illustrations of emergent structure only."
- REDISCOVERED IN: `arcs/emergent_scenarios.md` (independently formalizes the same five engines as clock thresholds + feedback loops — see F-K-8) and `arcs/narrative_scenario_chains.md` (independently produces the "no single actor chose this" framing for named-NPC arcs).

**F-K-6 — Arc resolution is a recognizer over independently-owned state, not a stored flag**
- SOURCE: `arcs/narrative_scenario_chains.md` lines ~890–905 ("THE ENDGAME CONFIGURATION")
- CATEGORY: derivation
- SUBSTANCE: The campaign's climactic resolution is defined as a 9-row table of independently-owned conditions (Almud's Thread Sensitivity ≥30, Axis 9 resolved publicly, Elske installed, Torben's Loyalty ≥6, MS >40, CI <40, IP <45, Coup Counter ≤1, Southernmost stabilised) — "All nine simultaneously: STABLE." None of these is a field on an "arc" object; each is read live off an NPC, faction, or clock that some *other* system owns. "Done" is computed by re-checking the world, never cached.
- WHY IT MAY STILL MATTER: Directly answers the brief's ownership question for the campaign-level notion of arc (contrast with F-K-4's per-NPC notion, where the state label *is* owned) — see the ontology tension named in F-K-16.
- STATUS IN DOC: none marked; document carries `[E-01] STRUCK (PP-675)` for Arc 1's underlying premise (see DEAD ENDS) but the Endgame table is independent of that strike.
- REDISCOVERED IN: single source.

**F-K-7 — Mending Stability, the central decline clock, writes off the Key bus and is invisible to articulation**
- SOURCE: `audit/2026-06-28-distillation-coherence/distillation_coherence_report.md` lines 25, 95
- CATEGORY: problem-only
- SUBSTANCE: "Six canonical systems write state silently, off the Key bus... the Mending Stability world-clock (which no module even owns)... The substrate's whole promise — save = initial state + Key log, replay = re-run the log — is broken wherever this happens, **and the articulation/chronicle layer is blind to these events**. This is the single biggest thing standing between you and 'one coherent engine.'"
- WHY IT MAY STILL MATTER: MS is the clock behind the corpus's most dramatic emergent structure (the "Einhir Spiral," the Rupture, the Southernmost temporal-window arc — F-K-5, F-K-8). If MS changes emit no Key, the entire Tier-2/3 articulation machinery of F-K-1 cannot narrate the world's own central decline — a severe, specific seam between the emergence mechanism and the narration mechanism that a downstream analyst should not assume is closed just because PP-688 is well-specified.
- STATUS IN DOC: AUDIT finding, "Adversarially verified 2026-06-28... all proposals survived" per the file's own header; fix deferred to "Structural program #1" in `open_decisions.md`, not applied.
- REDISCOVERED IN: single source (out of my scope tree otherwise, but load-bearing on this lane's central question).

**F-K-8 — Four named self-reinforcing feedback loops as the formal spine beneath the illustrative arcs**
- SOURCE: `arcs/emergent_scenarios.md` lines 684–743
- CATEGORY: mechanism
- SUBSTANCE: Loop A (Einhir Spiral): practitioner ambition → MS loss → threshold → harder ops → more failure → more MS loss → Gaps → Church Credibility rises → CI/IP rise → faction instability → Mandate drops → Revolution loses Mending access → MS terminal. Loop B (Church Dominance Lock), Loop C (Coherence Cascade), Loop D (Revolutionary Thread Access Window — the window "closes precisely when it's needed most") are structured identically: each is a closed causal cycle with no exit engineered in, named explicitly as "the most dangerous emergent states."
- WHY IT MAY STILL MATTER: These are tighter, more falsifiable formalizations of the same emergence claim in F-K-5 — a downstream designer wanting the actual state-machine rather than prose illustration should start here.
- STATUS IN DOC: none marked (Stage-12/Checkpoint-14 basis, same era as F-K-5's illustrative material — treat with equal caution pending currency check).
- REDISCOVERED IN: `arcs/emergent_campaign_arcs.md` Arc 3/4 (independently describes Loop A and Loop D's mechanics without naming them) — genuine independent convergence.

**F-K-9 — Convergent prior-art law: no acclaimed narrative game generates text at runtime**
- SOURCE: `audit/2026-06-28-narrative-state-articulation/02_prior_art_and_methodology.md` §A–C
- CATEGORY: mechanism
- SUBSTANCE: A mechanism-level survey (Disco Elysium's ~1M-word articy graph with skill-voices and ~211 "anti-passive" failure fragments; Planescape's `.dlg` finite-state-machine dialogue; Dwarf Fortress's `history_event` records rendered by per-type template functions; Caves of Qud's replacement-grammar-over-40k-word corpus with a deliberately corrupted Markov register; Crusader Kings' localization-key substitution; RimWorld's wealth-scaled pacing director; Nemesis' per-entity memory→templated bark) converges on one architecture: author a finite voice-bearing fragment library offline, tag with conditions over game state, and at runtime only select→substitute→splice. "None generate text at runtime."
- WHY IT MAY STILL MATTER: This is an evidenced constraint, not a preference — it forecloses "just call an LLM at runtime" as the answer and gives a concrete menu of proven techniques instead.
- STATUS IN DOC: ANALYSIS; external claims flagged for verbatim re-check where WebFetch was blocked; two source PDFs (Sych) read in full.
- REDISCOVERED IN: single source, but its conclusion is what `03_articulation_nlg_architecture.md` builds on wholesale.

**F-K-10 — Story sifting: significance-as-Datalog-query, and arcs as patterns over the Key graph**
- SOURCE: `audit/2026-06-28-narrative-state-articulation/01_narrative_legibility.md` §6; `03_articulation_nlg_architecture.md` §3
- CATEGORY: derivation
- SUBSTANCE: Reframes PP-688's significance function as "story sifting" (citing Kreminski's Felt/Winnow): low-level patterns over single Keys feed Tier 2; "arc detection = sifting patterns over longer `causes[]` chains; throughlines (N1–N6, T-01..T-41) are the higher-level patterns these roll up into ('stories from the bottom up')." Arcs are *detected*, never a first-class stored object in the substrate.
- WHY IT MAY STILL MATTER: Gives F-K-6's "recognizer, not owner" finding a concrete implementation technique (Datalog-style queries over an event log) rather than leaving it as a design principle with no mechanism.
- STATUS IN DOC: PROPOSAL (architecture-only, drafted as a future PP-688 §11; not canonical).
- REDISCOVERED IN: single source.

**F-K-11 — The four-factor deterministic NLG architecture (offline bake, runtime splice only)**
- SOURCE: `audit/2026-06-28-narrative-state-articulation/03_articulation_nlg_architecture.md` §2, §5, §8
- CATEGORY: mechanism
- SUBSTANCE: Four orthogonal, independently-varying factors compose combinatorially instead of multiplying into baked sentences: (1) slot-templates per Key-type × significance-length band; (2) a register/lexicon overlay — the existing X/Y/Z (Coherence/Thread-Sensitivity/Spirit) grammar frozen as swappable word tables, with high-Coherence selecting the clean lexicon and low-Coherence applying authored degradation rules as "a register selection inside the realizer... not a separate system"; (3) a focalizer overlay (4 chroniclers + protagonist frame) that solves fragment-assembly by making the voice tag itself the transition; (4) discourse/connective grammar derived from `causes[]` (cause→"because," reversal→"but"). Design-time: the `prose-writer` skill generates and freezes fragment pools; runtime: zero inference, same Key log → identical output.
- WHY IT MAY STILL MATTER: A concrete, buildable closure of PP-688's explicitly deferred realizer gap (Stage-10 test A3, "chronicle-prose = DEFERRED, requires LLM/template integration").
- STATUS IN DOC: PROPOSAL, architecture-only, "no data schemas, no worked example, no fragment content."
- REDISCOVERED IN: single source.

**F-K-12 — NPC roster capacity as a three-tier resource with demotion triggers**
- SOURCE: `arcs/throughline_resolutions_v30.md` §5 (lines 232–287)
- CATEGORY: npc
- SUBSTANCE: Named NPCs are classified Active/Passive/Background. Soft cap ≈35 Active; when a 36th becomes Active, one is demoted by priority order: ≥4 seasons off-screen, ≥4 seasons of flat low disposition with no active Duty, faction removal, or player-declared disinterest. Demotion is reversible. Inner-circle NPCs are "structurally Active" — floor-protected while their faction is in play.
- WHY IT MAY STILL MATTER: This directly gates which NPCs *can* be arc-bearing at all under F-K-4/F-K-5 — an arc needs an Active-tier NPC to render, and the coverage-gap finding below (F-K-14) shows this cap is already being hit unevenly.
- STATUS IN DOC: §-level marked "CANONICAL (approved Jordan 2026-04-17)" at document header.
- REDISCOVERED IN: single source.

**F-K-13 — Institutional Facility Slots: settlement capacity as a political-crisis generator**
- SOURCE: `arcs/throughline_resolutions_v30.md` §6 (lines 290–338)
- CATEGORY: seam
- SUBSTANCE: Seats/Cities/Cathedrals etc. have finite Wing/Suite/Chamber slots (e.g., a Seat has 3 Wings). At full capacity, a new rank-holder forces one of three outcomes: an existing holder departs, the settlement pays Wealth −3 to expand capacity (capped +1/settlement/decade), or the claimant is deferred as "Prince-in-Waiting" (an unstable provisional rank requiring a recurring social contest to hold). "This is functionally a political crisis without any political act by any faction" — the crisis is generated by a settlement resource limit, not a decision.
- WHY IT MAY STILL MATTER: A clean worked example of the excluded-scope seam the brief asks to name: a settlement stat (facility slots) generating faction-political consequences with no faction ever acting.
- STATUS IN DOC: CANONICAL (same doc-level marker as F-K-12).
- REDISCOVERED IN: single source.

**F-K-14 — Corpus self-audit: NPC coverage gaps and an emergent-vs-scripted evaluation rubric**
- SOURCE: `arcs/gm_ref/arc_narrative_analysis.md` (five-criterion rubric, lines 1–17; coverage tables, lines ~300–330)
- CATEGORY: problem-only
- SUBSTANCE: A five-axis rubric (Emergence quality / Table experience / Mechanical grounding / NPC fidelity / Thematic coherence, each 1–5) scores 18 arcs; average 21.3/25. Named gaps: **zero arcs feature Edeyja**, "the moral anchor of the setting, the highest-TS character" (18 arcs, 13 named NPCs, and none reach her); five more NPCs never drive an arc; five arc *types* are entirely uncovered (mass combat, Thread-operation-itself, Southernmost/Warden, Altonian invasion, Torben succession). Recommendation: "Reclassify Arcs 10, 14, 18 as *scenario triggers* rather than *emergent arcs* in the arc taxonomy" — an internal signal that some "arcs" in the corpus don't actually meet the multi-system emergence bar.
- WHY IT MAY STILL MATTER: This is a self-administered adversarial check the corpus performed on itself, using a genuinely reusable design instrument (the 5-criterion rubric) — rare in this material, and directly answers "is authored dressing being mistaken for emergence."
- STATUS IN DOC: none marked (internal analysis, Batches 01–03 of 18).
- REDISCOVERED IN: single source.

**F-K-15 — Arc-authoring hazard: mechanics are routinely fabricated and require a verification pass**
- SOURCE: `arcs/gm_ref/arcs_46_55_resolved.md` "Resolution Log" (U-01 through U-11)
- CATEGORY: problem-only
- SUBSTANCE: A 2026-04-13 resolution pass found 11 of the batch's arcs relied on invented or mis-cited mechanics: wrong Coup Counter triggers, wrong MS threshold bands, a fabricated "Read Intel" Domain Action, a fabricated Guild "ethical framework," incorrect Coherence-broadcast semantics. Each was corrected "against fetched sources." U-07 (Public Instability per-action values) remains an open design-layer gap even after resolution.
- WHY IT MAY STILL MATTER: A concrete, repeated failure mode for *any* future process that generates emergent-arc content from a mechanical ruleset: plausible-sounding mechanics get invented rather than looked up, at a rate high enough (11 of ~10 arcs in one batch) to require a dedicated audit pass.
- STATUS IN DOC: "Resolved" per the doc's own log; U-07's underlying gap is explicitly still open.
- REDISCOVERED IN: single source.

**F-K-16 — Unreconciled tension: "arc" names two different objects in this corpus**
- SOURCE: cross-file (`arcs/arc_expansion_v30.md` Part I vs. `arcs/emergent_campaign_arcs.md`/`emergent_scenarios.md`; also `arc_narrative_analysis.md`'s reclassification recommendation, F-K-14)
- CATEGORY: ontology
- SUBSTANCE: The canonical formalism (F-K-4) treats an arc as a per-NPC owned state label (A/B/C) with authored branch conditions — closer to a finite-state machine than an emergent discovery. The illustrative corpus (F-K-5, F-K-8) treats an arc as a post-hoc narrative naming of a causal chain across independently-owned clocks/stats, with no arc-object anywhere in the state model (F-K-6). No document in this lane explicitly reconciles these — `arc_narrative_analysis.md`'s recommendation to reclassify some arcs as "scenario triggers" gestures at the seam without resolving it, and the brief's own question ("must these be the same object, or must they not be") is never directly posed in the corpus.
- WHY IT MAY STILL MATTER: This is exactly the kind of unresolved structural question the brief is prospecting for — worth flagging explicitly rather than silently picking one reading.
- STATUS IN DOC: none — the tension is present but unnamed as such anywhere in the read set.
- REDISCOVERED IN: independently visible from both F-K-4 and F-K-5/F-K-6, which were authored in different sessions and do not cross-reference each other on this point.

### DEAD ENDS
- **Arc 1 "The Hunting Accident" (218 AG assassination investigation)** — `arcs/narrative_scenario_chains.md` lines 20–24: `**[STRUCK — PP-675: entire Arc 1 backstory removed... All branch logic below is invalidated.]**` Replaced by a forward-looking "Royal Crisis Tension Card." Its "no perpetrator, but every faction believes one exists" structural insight (shared-interest-in-suppression political dynamic) remains interesting design thinking but sits under struck canon — cite the insight, never the arc's mechanical triggers.
- **Collision D "Niflhel Weaponises Everything"** — `arcs/narrative_scenario_chains.md`: `**[INVALIDATED by E-01 resolution + PP-675 backstory strike... Retained for reference only.]**`
- **Niflhel as a faction entirely** — struck from `arcs/arc_expansion_v30.md`'s override note and `arcs/emergent_campaign_arcs.md`'s Arc 3: "Niflhel dissolved — Shadow Network phenomena now render at settlement layer... Dalla Virke became independent intelligence broker." Any arc citing Niflhel by name in this tree is pre-dissolution.
- **Coup Counter (binary 0–3)** — superseded by Löwenritter 4-stage graduated autonomy (Loyal/Restless/Autonomous/Split); `arc_expansion_v30.md`'s override gives a rough translation table but flags "arc structure remains valid as illustration; translate mechanics" for every arc that cites the old counter (Almud, Ehrenwall, most cross-NPC conditioners).
- **`arcs/README.md`** self-describes the entire tree as "Superseded design input — NOT a live GM reference... must be regenerated," while the sibling `arcs/gm_ref/README.md` claims the folder is "Currently empty" — directly contradicted by the 12 populated arc-batch files actually present. Treat every `gm_ref/arcs_*.md` file's status as unresolved rather than trusting either README.
- **`articulation_layer_v30.md`'s own status header** carries five different markers in one file (a promotion-comment claiming CANONICAL, an adjacent comment claiming PROVISIONAL, a body line claiming CANONICAL, a body line claiming PROVISIONAL, and a closing line "PROVISIONAL pending ratification") — do not cite this document's ratification state as settled in either direction.

### OPEN QUESTIONS NEVER ANSWERED
- What does King Almud *do* if a Discovery Event gives him Thread Sensitivity — "He has no Approach Training path... Does the most powerful man in Valoria... become one? This is the campaign's central dramatic question if it fires." (`narrative_scenario_chains.md`, Arc 2 §)
- The Revolution's Non-Player-Character "elder" with fragmentary inner-tradition knowledge is cited as pivotal to Collision E but marked `[EDITORIAL — depends on... elder being established]` — never named or canonised in this lane.
- Baralta's Solmund-ordained-authority claim (used as the trigger for Collision E's Grand Debate) is flagged `[EDITORIAL]` throughout and never resolved.
- Public Instability's per-action contribution values (U-07 in the resolution log) — explicitly still a "design-layer gap" after the rest of that batch was resolved.
- PP-688 §7 pacing (D11) is explicitly deferred ("a future PP authored if needed") and the only proposed closure (`03_articulation_nlg_architecture.md`'s RimWorld-style director) is itself unratified architecture-only.
- Tier-3 chronicle prose realization is Stage-10-tested as DEFERRED ("requires LLM/template integration") — the entire deterministic-NLG proposal answering it (F-K-11) has "no data schemas, no worked example, no fragment content" and was never carried into canon within this read set.
- CI threshold-band disagreement across three docs (30/50/70 vs 40/55/65/80/100 vs 75), flagged J-29 in `open_decisions.md`, needed before any Key can key `mechanical.ci_milestone_crossed` — unresolved, blocking the Mending-Stability Key-bus fix in F-K-7.