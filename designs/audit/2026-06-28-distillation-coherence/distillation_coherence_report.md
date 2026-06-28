<!-- STATUS: AUDIT — analytic instrument output, not canon. Self-exempting (Class A analysis). -->
<!-- Investigation: whole-project distillation + cross-scale resolution coherence. -->
<!-- Method: 12-cluster shape-card map (multi-agent, Sonnet) + main-loop synthesis. -->
<!-- The 7 cross-cut lenses + adversarial verification phase were killed by a transient
     server-side rate limit; this synthesis was authored in the main loop from the full
     cached map data + direct reads of key_substrate/scale_transitions/module_contracts +
     the methodology skills. Findings flagged [VERIFY] would most benefit from the deferred
     adversarial pass. -->

# Valoria — Distillation & Cross-Scale Coherence Investigation
**Date:** 2026-06-28 · **Scope:** every runtime system, the Key substrate, the resolver layer, the scale-transition fabric.

---

## 0. Executive summary (plain language)

You asked two things: *how far can each system be distilled into a more coherent form*, and *how can we strengthen the way systems resolve and relate across scales* — given that the architecture is "nested arrays and wrappers that propagate information across scales," aimed at one coherent game engine.

The honest headline: **the systems themselves are already well-distilled. The coherence debt is almost entirely in the connective tissue — the seams, the labels, and a handful of systems that quietly opt out of the shared machinery.** Every mapper independently said "do not touch the single update rule" and "do not collapse the 4-axis conviction matrix." Those two primitives — **the sigma resolver** (what happens) and **the armature dot-product** (what it means) — are genuinely the engine's spine, and they're sound.

What is *not* coherent yet, in descending leverage:

1. **Six canonical systems write state silently, off the Key bus.** `territorial_piety` (PT/CI), `ci_political` (CI milestones, the Theocracy attempt), `victory` (era transitions), the **Mending Stability world-clock** (which no module even owns), Coherence threshold-crossings, and settlement events. The substrate's whole promise — *save = initial state + Key log, replay = re-run the log* — is broken wherever this happens, and the articulation/chronicle layer is blind to these events. **This is the single biggest thing standing between you and "one coherent engine."**

2. **The resolver looks like 7 kinds but is really 2.** Combat, mass battle, thread operations, social contest, fieldwork actions are *all* the sigma-leverage engine — they're just wearing a stale `dice_pool` label, and social/mass have never been formally verified against it. Domain actions are the bare-stat variant of the *same* math. Everything else isn't a "resolver" at all — it's accounting, clocks, reads, or catalogs.

3. **State buckets are systematically mislabeled** in one fixable direction (counters that only climb toward a threshold are tagged "track" but are really "clock"), and two combat values (Initiative, Poise) need a bucket that doesn't exist yet (a mean-reverting signed float).

4. **A handful of phantom/duplicate modules** (`settlement_economy`, `npc_memory`, `scene_timer`+`audit`, `campaign_architecture`) inflate the architecture without adding behavior.

None of this requires redesigning a single mechanic. The work is *unification and seam-closure*, which is exactly your second goal. The recommendations below are ranked by leverage and tagged **free-win / structural / needs-your-call**.

---

## 1. The meta-finding: two primitives, everything else is bookkeeping

The deepest "more unified for a game engine" statement the corpus supports:

> **Valoria has exactly two universal primitives, and they are duals.**
> - The **sigma resolver** turns *will + advantage* into an *outcome* (the contest engine).
> - The **armature dot-product** turns an *event* into *meaning-for-an-observer* (the interpretation engine: `Σ axis: observer.armature[axis] × key.symbolic_dimensions[axis] × key.impact_vector[axis]`).
>
> Everything else a system "does" is one of four non-resolving operations over the outputs of those two: **accounting** (fold Keys at the season boundary), **clock-advance** (monotone counter toward a threshold), **state-read** (pure query), or **manifest** (catalog / orchestrate).

If you hold those two primitives + four operations as the whole vocabulary, every one of the 25 systems becomes a thin wrapper that (a) consumes Keys, (b) applies one primitive or one operation, (c) emits Keys. That is the `BaseEngine + EngineModule` shape the Godot combat slice already proves. The rest of this report is how to get every system there.

---

## 2. Lens 1 — Resolver unification

**Finding.** The `resolver` enum has 7 values (`dice_pool, d_sigma, deterministic_accounting, clock_advance, armature_dot_product, state_reader, manifest`), many tagged `[ASSUMPTION]`. The live docs collapse it to **one rolling kernel with two parameterizations + four non-rolling kinds**:

| Real resolver | Systems on it (from the map) | Notes |
|---|---|---|
| **Sigma — Instance A** (pooled, σ-leverage) | personal_combat (all 11 action modules), thread_leap, thread_operations, mass_battle (d10 pool TN7, net-success + degree gate = "Instance A sigma-style"), fieldwork Evidence/Disposition actions | The entire scene-scale contested layer. Already one kernel. |
| **Sigma — Instance B** (bare-stat, legible odds, drawn) | domain_actions (form ratified ED-874), piety crisis d6 (castable) | The **no-pool limit** of the same kernel: on the success line a μ-shift of +δ and an Ob-shift of −δ are identical (`P = Φ((μ−Ob)/σ)`). |
| accounting | faction_state, faction_politics (gates), territorial_piety, ci_political, npc_behavior, settlement_layer, peninsular_strain, knot strain, MS ledger | No draw — a fold over Keys at Accounting. |
| clock | engine_clock, Turmoil, IP, CI, Evidence Track, Thread Fatigue, conviction_scars, persuasion_track (bidirectional), victory streak | Monotone toward a threshold. |
| reader | victory, Disposition, Bonds, npc_memory, miraculous_event (gated emitter) | Pure query / conditional fire. |
| manifest | key_substrate, key_type_registry, scene_slate, game_director, clock_registry, scenario_authoring | Catalog / orchestrate. |

**`armature_dot_product` is not a resolver.** The articulation_layer card showed it's the substrate's §8.2 *interpretation* step used as a sub-step inside an accounting consumer — it's primitive #2, not a module resolver class.

**Distillation.** Collapse the enum to **{sigma (A|B), accounting, clock, reader, manifest}**, recognize armature-dot-product as the substrate interpret step, and reassign every `[ASSUMPTION]` resolver to the live-doc value the map recorded.

**Concrete high-leverage moves:**
- **Formally place social_contest and mass_battle on Instance A** and close **SIM-DEBT-04** (the social contest *is* the combat kernel — the card cites the explicit pool-construction parallel: Composure=Cha×3 ∥ Vitality, strain ∥ damage, Focus defence ∥ Armour — but it's never been verified against σ). This makes combat / social / thread / mass *one verifiable engine*.
- **Fix the Godot `strike_module.gd` ER-2 omission** (it bands degrees on `net≥ob` instead of `net≥ob−0.5`; the Python `core.py` applies the correction). This is a **calibration bug** — the port runs 5–9 pp low on success across the 5–13D band. [VERIFY against the live skeleton.]
- **Keep B distinct from A as a named instance, not a forced merge.** The resolution-diagnostic skill is explicit: do *not* migrate a healthy dice engine to B. Select by the Engine-Selection Rule (pool ≥ 5D + setup axis → A; bare-stat pivotal → B).

---

## 3. Lens 2 — Module dedup & boundary resolution

| Module | Verdict | Action |
|---|---|---|
| **settlement_economy** | Phantom (no doc / state / logic). But it marks a *real* gap: how do territory-scoped economic DAs (`da.economic_intervention`) reach individual settlements, and where does `env.population_change` land (there is no Population stat)? | **Retire the module**; `settlement_layer` consumes `da.economic_intervention` and maps it to a per-settlement Prosperity delta. Decide: is **Population** a settlement stat or implicit in `W_s`? Is **Trade** a settlement stat or a faction stat? (needs-your-call) |
| **npc_memory** | Phantom boundary — no doc; the MemoryReference pool is NPC-internal state written/read only by npc_behavior. | Mark as **owned sub-component of npc_behavior**; formalize `memory_query()` as the one API. Don't register separately until/unless Knowledge is Key-migrated. |
| **scene_timer + audit** | Both are observability/tooling — emit nothing, own no game state, write to sidecars. They inflate the consuming-systems lists of all three `mechanical.scene_*` Keys. | Merge into one **Observability** consumer (TimerRecorder + AuditChecker), or remove from `module_contracts.yaml` entirely. (needs-your-call on runtime-vs-tooling) |
| **scene_slate vs game_director** | Attribution conflict on `mechanical.scene_entered` (substrate §8.5 says scene_slate; registry says game_director). | Rule for **game_director** (it owns the container push / zoom stack in the Godot spec); correct substrate §8.5. scene_slate = the manifest *generator*; game_director = the *orchestrator*. Give scene_slate a home doc (currently split across player_agency §4 + settlement_layer §4.1 + the Godot spec). |
| **faction_politics vs faction_state** | Boundary "unestablished." It *is* definable. | **faction_state** = provincial accounting engine (cascade / mission / L/PS / Mandate). **faction_politics** = player-facing rank-ladder system (Standing / Duties / succession), scene-procedural, delegates all dice to social_contest. Declare `state.standing_change / coup_attempted / succession` as **dual-emitters** with an explicit rule (faction_state fires coup on L<2; faction_politics fires it on succession-contest failure). |
| **campaign_architecture** | Consolidation doc, not a runtime module. | **Retire the stub**; its contents already distribute to victory / threadwork / settlement / peninsular_strain. |
| **miraculous_event / scenario_authoring** | Both are event injectors with stale contract metadata. | Keep separate (resolver classes differ). Fix miraculous_event's `doc:null` (the doc exists) and wrong scales. Add a **`source` field** to `env.crisis`/`env.disaster` so consumers can tell mechanically-derived from author-injected. |

**Bonus structural win (faction_politics):** the **11 rank ladders (4 primary + 7 sub) are one parameterized `Ladder` template** with 8 authored dimensions (InitiationGate, HallTier, Mentor, DemotionTrigger, …). Express once, instantiate from data. Largest single code-surface reduction in the corpus.

---

## 4. Lens 3 — Key contract & type-registry distillation

**The dominant cross-corpus finding.** The substrate's invariant — *every consequential event is a typed Key* (key_substrate §1) — is violated in the highest-value places:

- **Zero-Key canonical systems** (the worst seam): `territorial_piety` (PT/CI changes), `ci_political` (CI milestones + the CI=100 Theocracy attempt), `victory` (era transitions), and the **Mending Stability world-clock** (no owning module, no Key — every Thread op writes it silently). Also Coherence threshold-crossings, settlement events (revolt / flourishing / siege-end), Thread→settlement stat writes, Domain-Echo faction-stat grants, and miraculous_event's Accord write. Each breaks replay determinism and is invisible to the chronicle.
- **F2 unregistered emitted types:** `scene.displacement`, `mechanical.project_advanced`, `state.project_failed/completed`, `scene.draft_da`, `scene.thread_operation`. → register or strike.
- **Naming-form drift:** `scene_outcome.*` vs `scene.*` (canonical is `scene.*`); `scene.thread_operation` vs `meta.thread_woven` — resolve whether these are one event or two (Leap-contact vs operation-completion).
- **Attribution conflicts** kept as dual-emits: `scene.dialogue` (3 emitters), `state.belief_revised` (2). → declare formal multi-emitter sets in the registry.
- **Enum mismatch:** some Class B types use `permanence: structural` / `time_horizon: medium`, which are **not in the substrate §2.1 canonical enums** — those Keys would be rejected at validation. Fix the enum.

**Distillation (not "more types" — *closure*):** add a small **substrate-state Key set** and apply the §12.3 authoring discipline universally:
- `env.ms_delta` + `env.ms_threshold_crossed` (owned by a new **substrate_state** module that owns MS, batched at Accounting to bound Key volume);
- `env.pt_change` + `env.ci_change` + `mechanical.ci_milestone_crossed` + `mechanical.theocracy_attempt`;
- `state.era_transition` (victory);
- a `settlement_event.*` family.

Family count (7 × ~30) is fine — don't reduce it for its own sake. The goal is **emit-closure** (every emitted type registered) and **consume-closure** (every type consumed by ≥1 system).

---

## 5. Lens 4 — Cross-scale propagation & seam closure *(your second goal, directly)*

The all-directions guarantee (scale_transitions §12) is architecturally **complete** — the 8 named handoffs are "authored sugar over the substrate," and direction is an emergent property of a Key's `targets[] / scale_signature / visibility`. The defect is not the mechanism; it's **emitters delivering blind**:

- **"Delivers-blind" down-seams:** strategic/scene emitters fire a Key (or write state) without populating sub-scale `targets[]`. New instances the map surfaced beyond the known §12.4 eight: `mass_battle`'s `scene.battle_concluded` carries victor/casualties but empty `targets[]` for the MS/Accord/Order consequences; social_contest's Domain-Echo DA-bonus and Obligation creation are unkeyed; Thread→settlement throughline writes are silent; cross-system wound impairment (−1D to Thread/Command) is read from actor state, not carried by a Key.
- **The zero-Key systems (Lens 3)** are the extreme case of this seam — they don't reach the bus at all.

**The fix is one discipline, applied everywhere:** every cross-scale Key populates `targets[]` (with `role`), `scale_signature` (including the sub-scale), and `stat_deltas`/`impact_vector` per affected actor. This is the highest-leverage move for "strengthen how systems resolve across scales," because it turns the *aspirational* all-directions guarantee into an *actual* one. Also verify the stub handoffs (§3.6 Thread→Mass is a forward-reference stub) carry real payload rather than decorative citations.

---

## 6. Lens 5 — State-bucket & symbolic-axis taxonomy (the "nested arrays" you described)

**State buckets.** The taxonomy is nearly complete, with one **systematic misclassification** and one **genuine gap**:

- *Systematic clock-vs-track error.* These are tagged `track` but are really **clock** (monotone toward a threshold, even if they decay/reset): Thread Fatigue, `conviction_scars` (indelible!), npc **arc state** (one-way FSM), npc projects, **knot strain**, Exposure, **persuasion_track** (bidirectional clock), Rattled, Concentration. Apply one rule corpus-wide:
  > **pool** = depleting resource that refills · **track** = bounded value that moves *both ways* and mean-reverts · **clock** = counter that advances toward a threshold (decay/reset doesn't make it a track) · **derived_value** = recomputed aggregate, never written directly (F1).
- *Genuine gap — a 5th bucket.* Combat **Initiative** and **Poise** are bounded *signed floats that decay toward a rest point* (Initiative → 0; Poise → 1.0). Neither track nor pool. Add **`state_axis`** = `{value, floor, ceil, rest_point, decay_rate}`. This single bucket also cleanly hosts the 9 pending combat modules' substrate axes.
- *Bonds* is a fixed creation attribute mislabeled `writable track` → make it `derived_value`/manifest constant.

Result: a **5-bucket universal scalar model** `{pool, track, clock, derived_value, state_axis}` + the F1 write-protection rule. That *is* the "cleaner state-vector representation for the KeyBus" you're after — every scalar in the game is exactly one of five kinds with defined read/write/decay semantics.

**Symbolic axes.** All symbolic interpretation flows through one **13-Conviction × 4-axis matrix → armature dot-product**. Keep **4 axes** (the map confirms they're compact and load-bearing; the 5th-axis option is correctly deferred). This one matrix is the universal substrate for NPC armature, faction meta-armature, memory salience, disposition drift, and articulation significance — *do not fragment it*. The only debt: the legacy **7-Conviction matrix** in `conviction_track_v1 §3` was never migrated to the canonical 13 (Reason→Scholastic, Autonomy→Liberty, …). Migrate it.

---

## 7. Lens 6 — Loop/damper integrity & churn preservation

**Loops with confirmed dampers — DO NOT TOUCH:** Mandate↔L/PS (saturating `7T/(T+6)` + ±1 drift, Stage-4 sim-bounded); combat Initiative (multiplicative decay + hard cap — the NERS audit requires *both*); morale cascade (−3/turn cap + 1-turn contagion delay); domain-action↔faction loop (±2 seasonal cap + Mandate saturation + 0.6 cascade damp).

**Loops with missing/unconfirmed dampers — real risks [needs-your-call]:**
- `npc_behavior ↔ social_contest` 2-cycle (opinion oscillation) and the concern→opinion→concern cycle — no damper specified.
- **Coherence degradation spiral** (lower Coherence → harder Leap → more failure → more degradation).
- **MS ↔ Strain spiral** (Collapse → MS−1/season → forced battles → MS−1) — confirmed positive feedback, no canonical damper.
- `territorial_piety` PT↔CI yield loop and the **Community-Weaving low-PT→more-Weaving** loop (the doc itself flags the latter as needing verification).
- **Turmoil runaway** (all three decay channels can be simultaneously blocked mid-crisis).
- `ci_political` CI→pool→territory→PT→CI (bounded only by *counter-action*, no formula damper).

Each needs a cap or a damper sized to per-cycle gain (resolution-diagnostic Lesson 5).

**Churn integrity (your axiom).** Distinguishing *inert* (cut) from *load-bearing-but-slow* (keep):

- **Genuinely inert → distillation targets:** the `g_dv0` derived-value-damage gate (inert pending `derived_stats §9`); the ×50/×20 settlement display values (no consumer); three "modifies Order decay" mechanics that reference a **base Order decay rate that's never defined**; the **Generational Shift / Torben succession** (unreachable — ~40 seasons vs a ~14–20 season campaign, audit A-10); settlement type Prosperity caps (referenced, undefined); legacy struck tables (threadwork single-axis Ob, mass_battle legacy pool formula). **Activate (define the missing value) or strike.**
- **Load-bearing, DO NOT cut** (echoing your infantry-envelopment principle — *slow/rare ≠ inert*): the surplus slate ("more opportunities than scene-actions" *is* the churn axiom); the two-phase Leap; the dual-armature NPC; per-sub-unit mass battle; the bidirectional persuasion track; the unified Thread pool formula; the Appraise-first contest; the Command-asymmetry axiom.

---

## 8. Lens 7 — Engine-shape conformance (the owed ESCP write-up)

Conformance to the `ValoriaKernel → KeyBus → BaseEngine + EngineModule` target, scored on **wrapper / keys / scalars / vectors / plugins / evolvability**:

| Tier | Systems | Why |
|---|---|---|
| **HIGH** (near target) | personal_combat (the worked CombatEngine+modules slice), key_substrate, settlement_layer, faction_state | Clean IN→resolver→OUT; good derivations; combat already proves the plugin shape. |
| **MEDIUM** | threadwork, social_contest, mass_battle, npc_behavior | Right kernel but **monolithic docs** hiding sub-systems; rich **unkeyed state**; stale resolver labels. |
| **LOW** (highest refactor leverage) | **territorial_piety, ci_political, victory** (zero Key integration), **MS** (no owning module), the phantom/tooling modules, **domain_actions** (no home doc, resolver still PROPOSED) | Canonical but blind to the bus; no clean wrapper. |

**ESCP verdict:** the engine *shape* is proven; the work is (a) **decompose the monolith docs** (threadwork → 5 sub-engines; mass_battle → BattleEngine + consequence handlers) into BaseEngine+modules, (b) give every system a **home doc + clean contract**, (c) **bring the zero-Key systems onto the bus**, (d) adopt the **5-bucket + state_axis** scalar model, (e) **express repeated structure as data** (11 ladders → 1 template; 5 Thread ops → 1 resolver + 5 outcome tables — already the de-facto shape; combat 11 actions → BaseEngine plugins, in progress). Item (e) *is* evolvability: new content as data/modules, no code change.

---

## 9. Ranked recommendations

| # | Recommendation | Category | Leverage | Effort |
|---|---|---|---|---|
| 1 | **Bring the 6 zero-Key systems onto the bus + close F-class debt.** New `substrate_state` module owning MS; `env.ms_*`, `env.pt_change`, `env.ci_change`, `mechanical.ci_milestone_crossed`, `mechanical.theocracy_attempt`, `state.era_transition`, `settlement_event.*`. | structural | ★★★★★ | high |
| 2 | **Apply the §12.3 targets[] discipline universally** (populate sub-scale targets/stat_deltas on every cross-scale Key). Turns the all-directions guarantee from aspirational to actual. | structural | ★★★★★ | med |
| 3 | **Fix the systematic clock-vs-track bucket errors + add `state_axis` + fix the permanence enum.** | free-win | ★★★★ | low (editorial) |
| 4 | **Unify the rolling resolver:** label combat/social/mass/thread as Instance A, verify social+mass against σ (close SIM-DEBT-04), apply ER-2 uniformly (fix the Godot strike degree bug), collapse the enum, reassign `[ASSUMPTION]`s. | structural | ★★★★ | med |
| 5 | **Module dedup:** retire `settlement_economy` + `campaign_architecture`; fold `npc_memory`; merge/route `scene_timer`+`audit`; home docs for `domain_actions`, `scene_slate`, `engine_clock`. | free-win + structural | ★★★ | low–med |
| 6 | **Express repeated structure as data:** 11 ladders → 1 `Ladder` template; 5 Thread ops → 1 resolver + 5 outcome tables; finish combat modules as BaseEngine plugins. | free-win (evolvability) | ★★★ | med |
| 7 | **Activate-or-strike inert mechanics:** define base Order decay rate; settlement type caps; resolve/strike Generational Shift; canonize `derived_stats §9` for ×50/×20; strike legacy tables. | free-win | ★★ | low |
| 8 | **Damper design** for the 6 unconfirmed loops (§7), each sized to per-cycle gain. | needs-your-call | ★★★ | med |
| 9 | **Boundary + naming rulings:** faction_state/faction_politics split; piety 3-way rename; `env.crisis` source field; migrate the legacy 7-Conviction matrix. | needs-your-call | ★★ | low–med |

**If you do only three:** #1 (bus the silent systems), #3 (the bucket relabel — nearly free), and #4 (one verified resolver). Together they deliver "one coherent engine" without touching a single mechanic's behavior.

---

## 10. Do-not-touch list (load-bearing — any future "simplification" must preserve)

- The **single update rule** (validate → append → resolve observers → interpret → consume → causal edge). Elegant and universal. Never split.
- The **4-axis Conviction matrix** + armature dot-product (the universal interpretation primitive).
- **Wall-clock kept outside the Key payload** (preserves V4 replay determinism — the SceneTimer sidecar is correct).
- The **surplus scene-slate** ("more opportunities than scene-actions" — the churn axiom in mechanical form).
- The **two-phase Leap** (suspension-then-act), the **dual-armature NPC** (personal vs effective convictions), the **per-sub-unit mass-battle** architecture, the **bidirectional persuasion track**, the **unified Thread pool formula**, the **Appraise-first contest**, the **Command-asymmetry axiom**, the **simultaneous-damage rule**.
- All **confirmed dampers** (Mandate saturation, initiative decay+cap, morale cascade cap, domain-action ±2 cap).

---

## Appendix A — System → real-resolver map (the distilled view)

`sigma-A`: combat (×11 modules), thread_leap, thread_operations, mass_battle, fieldwork actions, social_contest exchange.
`sigma-B`: domain_actions, piety crisis.
`accounting`: faction_state, faction_politics, territorial_piety, ci_political, npc_behavior, settlement_layer, peninsular_strain, knot strain, MS ledger.
`clock`: engine_clock, Turmoil, IP, CI, Evidence Track, Thread Fatigue, conviction_scars, persuasion_track, victory streak.
`reader`: victory, Disposition, Bonds, npc_memory (→ fold), miraculous_event.
`manifest`: key_substrate, key_type_registry, scene_slate, game_director, clock_registry, scenario_authoring.
*interpretation primitive (not a resolver):* armature dot-product (articulation_layer + every accounting consumer's relevance filter).

## Appendix B — Provenance

Map phase: 12 system-cluster shape-cards produced by a multi-agent workflow (run `wf_17a98ab7-f7d`, 12 Sonnet mappers, grounded in the live working tree). Synthesis: main-loop, from the full cached map + direct reads of `key_substrate_v30`, `scale_transitions_v30`, `module_contracts.yaml`, `silo_overlap_matrix.yaml`, and the `valoria-module-adjudicator` / `valoria-resolution-diagnostic` / `valoria-vector-audit` skill methodologies. The 7 cross-cut lenses + adversarial verification phase were lost to a transient server-side rate-limit; findings tagged **[VERIFY]** would most benefit from re-running that adversarial pass.
