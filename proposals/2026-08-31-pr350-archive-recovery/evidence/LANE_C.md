## LANE C — ARCHITECTURE, GAME FLOW & INTERDEPENDENCY

### COVERAGE
files_assigned: 25 | files_opened: 23 | files_read_closely: 22
skipped: `module_flowchart.mermaid`, `state_graph.mermaid` — generated Mermaid views regenerated from `module_contracts.yaml`; their edge content is already fully covered by `verdict_full_graph.md`'s per-module table and `module_map_flat.md`'s gate/edge lists, which I grep-sampled instead of reading whole. `2026-06-05-scale-atomization/scale_atomization_audit.md` was read in full but excluded from findings below — it is pure mass-battle cell/subunit/unit tactical-geometry content (explicitly out of scope; no NPC/faction/settlement/governance content).

### FINDINGS (ranked most valuable first)

**F-C-1 — Acyclic provenance is not loop-safety (the corpus's central architectural finding)**
- SOURCE: `2026-06-04-loop-safety-ledger/key_cascade_scope.md` §6; `.../loop_safety_ledger.md` §1
- CATEGORY: mechanism
- SUBSTANCE: The Key/event substrate guarantees its `causes[]` provenance graph is acyclic by construction (BFS-checked at emission) — but every turn of a *behavioral* feedback loop (faction collapse, MS decay) emits a new, legitimately-caused Key, so the DAG grows strictly forward and never trips cycle detection even as the underlying systems spiral. "A collapse spiral is, to the substrate, a perfectly valid, perfectly acyclic chain of well-formed Keys." Loop-safety is therefore delegated entirely to consuming systems; there is no engine-level "this loop is bounded" assertion anywhere.
- WHY IT MAY STILL MATTER: A durable engineering principle independent of which loops exist today — any new feedback mechanic must be individually damper/cap-audited by hand; a DAG guarantee will never catch it.
- STATUS IN DOC: none (unretracted consolidation)
- REDISCOVERED IN: independently stated in both `key_cascade_scope.md` and `loop_safety_ledger.md` (same session, different artifacts).

**F-C-2 — Three historical death-spirals, each closed with a named, reusable damper pattern**
- SOURCE: `loop_safety_ledger.md` §2/§3/§8; `2026-06-11-game-flow/game_flow_analysis_v1.md` §8; `2026-06-11-interdependency-master/valoria_interdependency_master_v1.md` §7
- CATEGORY: mechanism
- SUBSTANCE: (1) Faction collapse — FSS-LOOP-1, a *deterministic floor*: at Stability ≤2 the Accounting check cannot reduce Stability further; collapse only via an *active* Trigger 1–5 (sim: P(collapse) 0.41→0.97 only under sustained triggers). (2) Wealth-0 Military ratchet — FSS-LOOP-2, re-muster +1/Accounting while Wealth≥1. (3) Mandate runaway — LPS-2e's saturating `Mandate=clamp(round(7T/(T+6)),0,7)` plus mean-reverting ±1/season feedback from Mandate back to settlement L/PS.
- WHY IT MAY STILL MATTER: Three exact, reusable damper *patterns* (deterministic floor / conditional re-muster / saturating+mean-reverting aggregate) for any future stat at risk of runaway.
- STATUS IN DOC: "Ratified 2026-05-30"
- REDISCOVERED IN: independently reconfirmed across all three cited documents.

**F-C-3 — The season/turn loop: full ordered structure, barriers, and per-phase write-owners**
- SOURCE: `game_flow_flat_spec_v1.md` §D0–D7; `game_flow_analysis_v1.md` §3
- CATEGORY: mechanism
- SUBSTANCE: Season-open (8-step deterministic Slate generation, pruned to difficulty) → Personal Phase (3–5 scene actions; unpursued entries resolve by AI — "the world does not pause") → Strategic Phase (GD-2 mandatory Muster/Govern pass *first*, then AI priority-stack, then resolution by 7 priority classes; all faction-stat actions on d+σ) → Zoom interrupts (interleaved, not sequential — "the BG clock never pauses") → Cascade Phase (Domain Echo, cascade-depth cap 3) → Accounting (strict 10 steps: votes/attribute changes → Stability checks/collapse → cooldowns → clock advances → Church Attention/Thread Debt → **Accord/Strain/battle consolidation at Step 6** → threshold/GD-3 → Warden/loyalty → occupation → victory check). The doc's own adversarial pass caught and fixed a real sequencing error: Accord/Strain/battle accounting is Step 6, not Step 4 as an earlier cut (and `peninsular_strain`'s own internal "4c/4d/4e" numbering) implied.
- WHY IT MAY STILL MATTER: The most complete flattened "what runs when, who may write" statement in the corpus; the Step-4→6 correction is a concrete trap for anyone trusting a source doc's own numbering.
- STATUS IN DOC: none; self-adversarially reviewed (§H)
- REDISCOVERED IN: unchanged in the later `valoria_interdependency_master_v1.md` §6 consolidation.

**F-C-4 — The top-down Key-delivery gap: the engine can deliver, but no rule tells it to**
- SOURCE: `valoria_interdependency_master_v1.md` §5.1, §8 item 1; `2026-06-11-interdependency-master/valoria_interdependency_atlas_v1.md` §2.4, §5 finding 4; `2026-06-10-module-adjudication/verdict_full_graph.md` §2 (J2)
- CATEGORY: seam / mechanism
- SUBSTANCE: Every cross-scale edge runs bottom-up (capped, queued, safeguarded) or lateral; none of the eight `scale_transitions §3` handoff rules delivers a top-down Key (a Domain-Action outcome, a succession, a peninsula shock) to a personal/settlement consumer with a payload and mandatory effect. The atlas's primitive-level re-read found the engine's own `compute_observers` has *no scale predicate* — it already delivers and applies any Key to any intersecting observer — so the real gap is narrower than "delivery": strategic Keys are authored with only faction/territory-scoped targets, never personal ones, and no rule says to populate them. 8 cross-band seams / 15 type-edges are enumerated by name.
- WHY IT MAY STILL MATTER: The most-recurring, most rigorously re-derived finding in the lane — the architectural reason world events don't reach the player as consequences, with the fix space already narrowed to two named options.
- STATUS IN DOC: `[OPEN — Jordan]` (docket J-1)
- REDISCOVERED IN: independently found and progressively sharpened across `verdict_full_graph.md` → `valoria_interdependency_master_v1.md` → `valoria_interdependency_atlas_v1.md` (three passes, same session cluster).

**F-C-5 — "Never write a derived aggregate directly" (R4) is violated by the game's own ratified canon text**
- SOURCE: `2026-06-06-architecture-map/valoria_system_wiring_analysis.md` Part 4 (F1) & Part 5 (R4); `valoria_interdependency_master_v1.md` §8 item 2; `2026-06-10-module-adjudication/module_map_flat.md` gate `g_dv0`
- CATEGORY: ontology
- SUBSTANCE: The rule: never write a Derived Value/aggregate (e.g., Mandate) directly — route the delta to its substrate (settlement L/PS) and let it re-aggregate. `scale_transitions §5.2/§5.4/§5.6` literally say "+1 Mandate / −1 Mandate" in prose despite Mandate being a derived LPS-2e aggregate — a bug in *ratified canon text*, not a hypothetical implementation risk. A companion universal rule: "derived value = 0 held through Accounting → owning stat −1" applies identically to faction and settlement derived values.
- WHY IT MAY STILL MATTER: A concrete, still-open drafting defect that will silently break any implementation taking the Domain Echo prose literally.
- STATUS IN DOC: `[OPEN — Jordan]` (J-7/J-8)
- REDISCOVERED IN: found in `valoria_system_wiring_analysis.md` (2026-06-06) and independently re-derived from primitive registry reads five days later in `valoria_interdependency_atlas_v1.md` §5 finding 5.

**F-C-6 — Domain Echo is deliberately narrow-bandwidth, queued not live, specifically to prevent real-time manipulation**
- SOURCE: `valoria_interdependency_atlas_v1.md` §2.2; `game_flow_analysis_v1.md` §3.4
- CATEGORY: mechanism
- SUBSTANCE: The personal→strategic channel caps at 1 Echo/scene/faction, ±2/stat, and is *queued to the next Accounting* rather than applied live — explicitly "to prevent real-time BG manipulation." Four sub-channels (Domain, Debate→Mandate, Accord, Thread) each gate on a "Sufficient Scope" test (named leader involved / institutional challenge / Complex+ investigation / Relational+ Thread op / combat victory over an officer / Disposition ±4-5 / governance Order ±1).
- WHY IT MAY STILL MATTER: "A player moves institutions a point or two a season through scenes; institutions move themselves through Domain Actions" is a precise, worth-preserving statement of intended personal/strategic balance-of-power.
- STATUS IN DOC: none (live mechanism)
- REDISCOVERED IN: same "queued not live" framing recurs independently in both cited documents.

**F-C-7 — Empirical stress test: the canonical victory condition fired 0/120 times, and the mechanism was self-defeating by construction**
- SOURCE: `2026-06-06-integration/integration_survey_stress.md` Stage 4; `.../win_computation_compilation.md` §0.8, §5
- CATEGORY: derivation
- SUBSTANCE: A 120-campaign instrumented battery on the then-current `sim/` engine found GD-1 sovereignty (11+/15 territories, Accord≥2 in *every* held territory, Political Stability≤6, 2 consecutive seasons) fired 0/120 times; 100% resolved via an undocumented `held×10+Legitimacy` fallback. Root cause: the only territory-acquiring action (Conquest) drops the conquered territory's Accord by 2.5, while GD-1 demands Accord≥2 everywhere held — "the two halves of the design were never reconciled," making the headline win condition self-defeating rather than merely rare.
- WHY IT MAY STILL MATTER: A quantified worked example of exactly the loop-safety class of bug (F-C-1) — and a reusable validation method: instrument win-path attribution, run N≥100 campaigns, check the headline condition actually fires.
- STATUS IN DOC: none contested; note the specific win-share numbers (55.8/36.7/6.7/0.8%) are from one specific 2026-06-06 build, not current.
- REDISCOVERED IN: two artifacts in one session triangulating the same root cause from different angles.

**F-C-8 — The dominant balance lever was an unimplemented stub exploited by an if/elif bug**
- SOURCE: `win_computation_compilation.md` §0.4, §2
- CATEGORY: derivation
- SUBSTANCE: Faction action selection used sequential `if` (not `elif`): a 30% roll for "faction-unique action" returning `'invalid'` for two of four factions (unimplemented) *fell through* to Conquest instead of doing nothing, silently doubling their effective conquest rate (~65% vs ~35%) — identified as the primary balance driver, larger than the starting-stat asymmetry itself.
- WHY IT MAY STILL MATTER: A specific, checkable failure mode ("an unimplemented stub silently sets the balance via cascade fall-through") worth auditing for in any dispatch-cascade pattern (faction AI, NPC action selection).
- STATUS IN DOC: none (uncontested live bug)
- REDISCOVERED IN: single source.

**F-C-9 — Settlement/governance resolution should be deterministic-simulation-first, never bare-stat dice**
- SOURCE: `2026-05-28-engine-replacement/engine_replacement_audit.md` §3.6/§3.7/§7; `.../engine_replacement_reconciled.md` §7
- CATEGORY: mechanism
- SUBSTANCE: At audit time, faction/settlement actions resolved on a bare 1–7D pool, computed and independently exact-convolution-verified as degenerate (P≈0.070 at Ob 3, P≈0.010 at Ob 4 for a 2D pool). Exhaustive precedent research (CK3/EU/Stellaris/KoDP/Six Ages) found grand-strategy games *never* resolve faction/settlement scale with bare-stat dice — always deterministic formulas + capped-probability + weighted events. Settlement resolution specifically was flagged as "an open hole" risking the same degeneracy, recommended as "deterministic accounting + governor/officer modifiers (ROTK/CK3 pattern)."
- WHY IT MAY STILL MATTER: The faction half was later resolved via d+σ (per other lane evidence not in this file set); the *settlement* half of this recommendation is not confirmed carried through anywhere in this corpus.
- STATUS IN DOC: recommendation, Jordan's call, not ratified within this corpus
- REDISCOVERED IN: single source (reconciled version narrows but doesn't contradict).

**F-C-10 — Precedent-grounded scale/paradigm-fit taxonomy: "the fit/strain map is scale-shaped, not paradigm-shaped"**
- SOURCE: `engine_replacement_audit.md` §5, §6
- CATEGORY: mechanism
- SUBSTANCE: Systematic per-system precedent mapping: personal combat (fits — Battle Brothers proves 5 desired combat properties reachable turn-based with one d100 roll; the gap is combat-*layer*, not dice-type); social contest (best-fit proof case — same substrate slides from 1-person dispute to multi-faction parliament by varying exchange count/adjudicator/pool-basis); investigation (correctly zero-RNG, matching Obra Dinn/Golden Idol); threadwork (consequence-architecture-first, Mage:the Ascension lineage); mass battle (fits via *summed* pool — the model for fixing faction degeneracy); faction/strategic (the one genuine strain, an outlier vs precedent); peninsula/victory (correctly deterministic).
- WHY IT MAY STILL MATTER: A reusable, precedent-grounded heuristic for evaluating any future resolver-swap proposal at a given scale.
- STATUS IN DOC: none retracted
- REDISCOVERED IN: single source, unrefuted by its sequel.

**F-C-11 — Adversarial-audit case study: a "0 P1" headline was manufactured by silently dropping findings and miscitng canon**
- SOURCE: `2026-05-28-engine-replacement/engine_replacement_reconciled_AUDIT.md` §0, §1 (A1, A2); `2026-05-28-consolidation/24h_work_consolidation.md` §3.2
- CATEGORY: problem-only
- SUBSTANCE: A reconciliation doc reached "0 P1, more firmly repair-and-keep" by legitimately closing one finding but silently dropping four other P1s from a companion diagnostic, demoting a fifth to a footnote, and downgrading a sixth — all unargued. The same doc cited GD-2 as canon "already mandating" a specific resolver, when GD-2 verbatim governs only action-*selection* ordering, not resolution.
- WHY IT MAY STILL MATTER: A concrete worked instance of self-authored completeness-overclaim and canon-phrase conflation — a "worst failure mode" case study.
- STATUS IN DOC: uncontested findings of the audit
- REDISCOVERED IN: independently caught the same day by `24h_work_consolidation.md`.

**F-C-12 — The 2026-06 `sim/` engine's architecture was sound but its "dynamic substrate" was entirely stubbed, flattening every faction to one Military scalar**
- SOURCE: `2026-06-06-integration/architecture_survey_stubs_scopes.md` §A–§F
- CATEGORY: mechanism
- SUBSTANCE: Scale-layered architecture, keying, and determinism confirmed sound. But card-driven faction actions, worldly/miraculous events, and Domain-Echo→faction-stat wiring were all stub or unwired; faction-state→mass-battle mapping collapsed every faction to `power=round(Military)`, discarding Wealth/Influence/Stability in combat entirely. No module implemented the actual canonical victory (elimination/diplomatic subjugation) — `treaty.py` existed but `victory.py` never read it.
- WHY IT MAY STILL MATTER: A concrete checklist of exactly which mechanisms must exist for non-military faction identities (Church influence, Hafenmark wealth) to matter in play.
- STATUS IN DOC: none contested
- REDISCOVERED IN: independently corroborated by `win_computation_compilation.md`'s Military-only combat finding and `integration_survey_stress.md`'s "wired-but-inert" framing — three documents in one session converging.

**F-C-13 — World-clock naming fracture: one track carries up to four names, with a live arithmetic-inversion bug**
- SOURCE: `2026-06-11-canon-flatten/canon_flatten_examination.md` C3, C4, C12, C13, C14g
- CATEGORY: world-churn
- SUBSTANCE: The Mending-Stability world clock is called MS (Mending Stability), MS (Metaphysical Stability, an unadopted rename), RS (Rendering Stability), and TT (Thread Tension, its inverse-polarity sibling) across different canon docs; the mechanics index carries both `rs_track` and `ms_track` as an unmerged duplicate pair. One document had its labels find-replaced TT→MS *without inverting the arithmetic*, so identical clock movements read as good in one place and bad in another within the same doc. CI has three incompatible threshold schemes; IP expands three different ways.
- WHY IT MAY STILL MATTER: Directly threatens interdependency-graph legibility — a reader following "RS" and "MS" separately won't realize they're the same clock.
- STATUS IN DOC: SURVIVES (adversarially re-verified against raw bytes, v2 pass)
- REDISCOVERED IN: `valoria_interdependency_atlas_v1.md` §0 independently documents the *same* 3-way naming collision from primitive registry reads — two structurally unrelated methods converge.

**F-C-14 — "Resonant Style" is a mechanically-gated concept whose members were never enumerated, and its rename never propagated**
- SOURCE: `2026-06-06-architecture-map/valoria_master_workplan.md` §8.2/§8.2-note; `canon_flatten_examination.md` §3.1; `module_map_flat.md` gate `g_scar2`
- CATEGORY: ontology / problem-only
- SUBSTANCE: A live session gate fires on "Scars on Conviction X = 2 → Resonant Style X exposed," but no doc enumerates the style set or the Conviction→style rule (a targeted read of the doc meant to define it found nothing). Separately, the registry renamed "Resonant Style"→"Pressure Point" in April; the rename propagated nowhere, and canon-flatten's read shows live characters carrying "Pressure Point" values (Evidence/Consequence/Authority/Loyalty) that differ from the four Resonant Styles named elsewhere (…/Solidarity) — suggesting silent divergence, not just a stalled rename.
- WHY IT MAY STILL MATTER: A mechanical gate firing on an undefined enumeration is a silent port-breaker.
- STATUS IN DOC: "remains a PLANNED registry KIND, not yet buildable"
- REDISCOVERED IN: independently surfaced by the workplan (2026-06-06) and canon-flatten (2026-06-11), different methods, same hole.

**F-C-15 — The engine is five resolver archetypes, not one; matching archetype to scale is the actual discipline (R6)**
- SOURCE: `2026-06-06-architecture-map/valoria_system_hierarchy_map.md` Tier 3; `valoria_interdependency_master_v1.md` §1
- CATEGORY: ontology
- SUBSTANCE: Every system = IN → one of {dice pool, d+σ, deterministic accounting, clock advance, armature dot-product} → OUT (always including Keys). R6: "match the resolver archetype to the mechanic category… don't roll a small bare stat on a pivotal irreversible outcome" — the exact rule whose violation F-C-9 later quantified.
- WHY IT MAY STILL MATTER: The load-bearing ontological frame underlying the value taxonomy, module map, and loop inventory.
- STATUS IN DOC: none, consistent everywhere
- REDISCOVERED IN: identically restated in four separately-authored documents across two sessions.

**F-C-16 — 11 of 27 modules are "registry-shadow": no design doc, coverage inflated by counting them as extracted**
- SOURCE: `verdict_full_graph.md` §7; `valoria_interdependency_master_v1.md` §4
- CATEGORY: governance
- SUBSTANCE: 11 of 27 modules have zero independent design doc — their only evidence is the Key-type registry's emitter/consumer lists. Counting them alongside fully-specified modules inflates apparent graph coverage ("40% of the 'verified' graph rests on a single source"). Module-ownership defects concentrate exactly in these 11.
- WHY IT MAY STILL MATTER: A durable methodology warning plus a ready-made documentation-debt checklist.
- STATUS IN DOC: `[OPEN — Jordan]` (J-4)
- REDISCOVERED IN: the 11-module list independently confirmed in both `verdict_full_graph.md`'s table and `valoria_interdependency_master_v1.md` §4.

**F-C-17 — Two duplicate-module boundaries never resolved: settlement_economy/settlement_layer, faction_politics/faction_state**
- SOURCE: `verdict_full_graph.md` §2 (J3); `valoria_interdependency_master_v1.md` §8 item 6 (J-5)
- CATEGORY: governance
- SUBSTANCE: Both pairs flagged "boundary unestablished [OPEN — Jordan]" for possible double-implementation of the same settlement/faction economy math.
- WHY IT MAY STILL MATTER: A double-implementation risk for any future build wave.
- STATUS IN DOC: `[OPEN — Jordan]`
- REDISCOVERED IN: raised in `verdict_full_graph.md`, unresolved a day later in `valoria_interdependency_master_v1.md`.

**F-C-18 — Nested settlement-grain failure gates distinct from territory-grain Revolt**
- SOURCE: `module_map_flat.md` gates `g_ord0`, `g_def0`
- CATEGORY: settlement
- SUBSTANCE: Settlement Order=0 → "local revolt"; settlement Defense=0 → "undefended — auto-capture" (no battle roll). These sit beneath the province-level Accord/Revolt cycle (F-C-3), meaning a settlement can fail locally without its containing territory's Accord reaching 0.
- WHY IT MAY STILL MATTER: A finer-grained governance-collapse mechanism worth preserving distinctly from the province-level cycle.
- STATUS IN DOC: none
- REDISCOVERED IN: single source.

### DEAD ENDS
- **PP-675 "struck the 218 AG backstory"** (`canon_flatten_examination.md` C2) — v1 claimed this and told Jordan to strike canon/03. Raw byte + ratification-store check found PP-675 is actually an unrelated terminology-conversion workplan, and no ledger entry ratifies any such strike. **REVERSED**; do not edit canon/03 on this basis.
- **"No M-series exists"** (C14e) — **WITHDRAWN as false**; the M-series is the vetting-criteria framework (M-1…M-11), visible in every patch's vetting block.
- **Faction Domain Action success "P ≈ 0" / "deterministic death spiral"** (`engine_replacement_reconciled.md` §1) — corrected via authoritative die rule to P=0.070 (Ob3)/0.010 (Ob4): "probabilistic, heavily loss-weighted," not deterministic.
- **"0 P1" completeness claim** (`engine_replacement_reconciled.md`) — refuted by its own same-day audit (F-C-11); use only the underlying "do not replace the core engine" verdict.
- **"Faction-collapse loop is damped but terminally unbounded"** — an early working note in one session, retracted the same session once FSS-LOOP-1/2 were found already ratified (`loop_safety_ledger.md` §8).
- **A candidate "victory_v30 vs geography territory-numbering" conflict** — investigated and **rejected before logging**; the two docs actually agree on T11/T12/T13 (`canon_flatten_examination.md` §8).
- **The "19 A6 seam violations" count** — the atlas's own adversarial pass (R4) corrected this: only 8 cross-band seams (15 type-edges) are genuine top-down/strategic→personal; the 19 count folds in 1 near-lateral seam that doesn't belong.

### OPEN QUESTIONS NEVER ANSWERED
- MS Mending model: passive world-time regeneration vs strictly action-gated (`loop_safety_ledger.md` §6.1).
- MS baseline direction: three canonical sources disagree whether it rises or decays at game-time (§6.2, candidate CAND-LSL-01).
- The −10/s MS net-loss cap: contested, whether it actually holds (§6.3).
- L-CONV multi-Conviction cascade severity: `[INTENT UNDETERMINED]`, needs the axis matrix plus a ruling (§6.5).
- J-1 (top-down Key delivery): engine-mediated-exempt vs. an explicit `scale_transitions §3` rule — never ruled anywhere in this lane.
- Composure formula/name: Charisma×3 vs Presence+6, both name and form diverging, unresolved.
- The Resonant-Style/Pressure-Point vocabulary: never enumerated, rename never propagated (F-C-14).
- GD-1 victory threshold: 11+/15 (canon/02) vs "all 15" (victory_v30, twice) — confirmed SURVIVES, never picked.
- settlement_economy/settlement_layer and faction_politics/faction_state duplicate-module boundaries (F-C-17).
- The faction Domain-Action Ob formula contradiction (target-stat vs floor(target/2)+1) — flagged as a prerequisite to finalizing the faction resolver fix, never closed in this corpus.