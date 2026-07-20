# Working notes — S4 Substrate Contract drafter lane

## What I read (working tree only)
- `00_engine_charter.md` IN FULL — premise, Q1–Q4, C1–C7, substrate contract L137-151, capstones.
- `synthesis.md` IN FULL — Arc-Vector Engine w/ subordinate director; L0–L5; §8 new types; §11 forks.
- `03_prior_art_and_module_homes.md` — doc:null cluster (game_director/scene_slate/scenario_authoring/npc_memory/scene_timer), scene-selection today, scene_entered conflict.
- `references/module_contracts.yaml` — lines 140-160 (npc_behavior arc-state bucket:150), 342-404 (scene_slate/game_director/scene_timer), 744-780 (scenario_authoring, articulation :768 wildcard).
- `designs/architecture/propagation_spec_v1.md` — O.1–O.9: ORD-1..4, SSI-1..4, RNG-1..3 + RNG-MODEL-COLLISION, O.6 compute_observers set() ORD-2 violation, O.7 scene_slate._queue ORD-4, O.8 V4, Theorem A/B, cascade_depth vs sub_step_index, one-Key-N-targets.
- `designs/articulation/articulation_layer_v30.md` — §3.1 trigger table (10 triggers; trigger-9 cosine `abs(sim)>0.40`, +0.937 Crown/Hafenmark 30-season), §3.2 significance 0-13, §3.3 accumulator, §6 Class B extensions, §7 pacing DEFERRED, §10 D11 Deferred.
- `designs/architecture/key_type_registry_v30.md` — §1 format, §7 scene.combat_resolved:724 / scene.investigation_resolved:705, §8 meta.knot_formed:800 (Class B exemplar), mechanical.scene_entered:365 (emitting_systems:[game_director]).
- `designs/architecture/key_substrate_v30.md` §8.5 L510 — VERBATIM "scene_slate: scene activation emits mechanical.scene_entered" — the contradiction the scene_entered resolution must edit.
- `strategic_judgments.md` J-2 + `02_interdependency_map.md` — engine_clock doc:null pending ED-1051, home propagation_spec §O.2; Gate-0 critical path.

## Key grounding facts locked
- scene_entered: registry §7 already says `emitting_systems:[game_director]`; substrate §8.5 says scene_slate. GENUINE cross-doc conflict → resolution REQUIRES §8.5 edit in same PR. Restored as fork per charter [OPEN — Jordan] (S4.8).
- convergence dedup `convergence_fired_set` = second live ORD-2 violation (O.3/O.6). Fixed → order-preserving dict keyed by total order; R7.
- Top-N rationing has NO tiebreak in §3.3/§4.3 → total order (salience DESC, tier_rank, id ASC); R-in-S4.2.4.
- cosine ±0.40 + meaningfulness float product = boundary + cross-oracle (Py↔GDScript, ED-1050 class) nondeterminism → quantize to fixed grid / canonical summation order.
- realizer fragment selection undefined + RNG-MODEL-COLLISION open → pure fn or dedicated render sub-stream seeded (campaign_seed,key.id); Stage-0 render-lane precondition.
- convergence-EFFECT seam: register combined pressure is authored ("not predictable from constituents", COLLISION-C RS+8/IP+2/TC+2). cosine-detected outside the 8 = RENDER/CHRONICLE-ONLY, zero pressure. R9.
- foreclosure via passive clock crossing = silent → (a) foreclosure only from edge/convergence modes; (b) mandatory Tier-3 chronicle beat (positive surfacing). R8.
- Stages 2-3 ride the unauthored engine_clock spine → Gate-0/ED-1051 precondition (contra "every stage rides an existing home"). Stages 0-1 unblocked.

## Blockers applied
- BLOCKER-1 bake volume: 350-450 is the fork-6-fallback (Certainty as lexicon-swap) figure; DEFAULT (Certainty in pool) → low-thousands; per-NPC is a distinct line item ~1,050. S4.11 flag 6.
- BLOCKER-2 anti-oatmeal not structural: vector-as-data = slot-filler divergence only; prose distinctiveness needs ERA (UNBUILT, Stage-5 blocker); removed "by construction". S4.11 flag 7 + conformance.

## Majors applied (16)
scene_entered §8.5 edit + fork restoration; convergence dedup ORD-2 (R7); Top-N tiebreak; cosine/meaningfulness fixed-point; realizer RNG sub-stream; convergence-effect provenance (R9); tension-curve reconciliation → subtractive ceiling (S4.10); engagement-window-divergence (R10); foreclosure mandatory-render (R8); pricing-over-gating audit (S4.9 deferred); watching/participating = OFFER-not-outcome (R6); director graduates deferred D11 → drop ownership (S4.10); salience demotion player-protection (S4.9 deferred); scene_entered inconsistent w/ substrate §8.5 (S4.8); Stages 2-3 Gate-0 dep (S4.2.2); director real-time curve vs NOT-list (S4.10).

## Deliverable
`designs/audit/2026-07-05-emergent-narrative-engine/01_workings/spec_sections/s4_substrate.md` — full polished section: S4.1 OWNS/READS per-scale table; S4.2 Keys-in (subscription/cadence/filtering ladder/replay + all determinism rules); S4.3 total-accounting invariant + foreclosure + convergence provenance; S4.4 verbatim module_contracts entries (5); S4.5 verbatim registry entries (2 new Class B); S4.6 declared-vs-implemented edge table (E1-E13); S4.7 six directions; S4.8 scene_entered fork; S4.9 ten conformance rules + 2 deferred gates; S4.10 director subtractive-ceiling reconciliation; S4.11 eight open flags.

## Left open for orchestrator / sibling lanes
- ERA instrument build (Stage-5 blocker) belongs to the render lane (S3) — named here so not dropped.
- Certainty bake-key fork resolution (§6) is render-lane but swings my registry bake-key note.
- The actual §3.1 trigger-table edit + §8.5 edit are deliverables of Stage 0 / this PR; text pinned but not yet written into canon files.
