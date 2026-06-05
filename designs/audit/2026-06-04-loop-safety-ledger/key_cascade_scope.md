# Valoria — Key-Engine Cascade & Ripple Scope Map

**Scope exercise · 2026-06-04 · bottom-up from canonical reads**
Subject: how a single consequential event propagates through the engine, ripples across systems, and compounds into emergent narrative — and where those ripples are bounded vs. unbounded.

---

## §0 Scope, method, grounding

**What this traces:** the Universal Key Substrate (PP-687) + Key Type Registry (PP-687) + Articulation Layer (PP-688) as the propagation engine, and the cross-system ripple topology the three define. This is the architecture that *connects* Valoria's systems; it is not a per-mechanic catalogue of each system in isolation.

**What it does not trace:** the internal resolution of individual systems (combat dice, social contest exchanges, faction L/PS formulae). Those are the *sources and sinks* of Keys; their internals are out of scope except where a loop closes through them.

**Method:** every claim below traces to a direct read this session. Sources: `key_substrate_v30.md` (§1, §2.2–2.3, §4.1–4.8, §5, §6, §8, §9–§11), `key_type_registry_v30.md` (§3, §8, §9), `articulation_layer_v30.md` (§1, §3.1–3.4, §4, §5). Loop-classification lens borrowed from `valoria-resolution-diagnostic` Phase 4 (damper / cap separation). Where a loop's closure is my synthesis from topology edges rather than a single doc statement, it is marked `[synthesis]`; where a damper/bound is not directly verified, `[UNVERIFIED]`.

**One foundational fact (substrate §1):** *"Keys are the engine's only event substrate. No system maintains a private event channel; every system emits Keys and consumes Keys."* Therefore every ripple in Valoria — without exception — is a Key. There is one cascade mechanism, not many.

---

## §1 The atomic cascade — one Key, emitted

A single emission runs one rule (`on_key_emitted`, substrate §4.1). It is the *only* state-update path in the engine:

```
1. VALIDATE        type ∈ registry; 8 universal invariants (§2.3);
                   causes[] already-logged AND acyclic (BFS, §4.6) → else ValueError
2. LOG             append to immutable KEY_LOG (append-only)
3. OBSERVERS       compute_observers(key)  (§4.2)
                     = source_actor ∪ targets[] ∪ (public ? actors_in_scale(scale_signature)) 
                       ∪ semi_public_observers ∪ private_observers
4. INTERPRET+APPLY for each observer:
                     interpretation = armature.interpret(key)      # dot-product on Conviction axes
                     salience       = compute_salience(...)         # §4.5, clamp 0–3
                     observer.memory.record(key.id, salience)
                     observer.apply_state_changes(key.stat_deltas)  # raw mechanical state
5. PROPAGATE       for system in TYPE_SUBSCRIPTIONS[key.type]:
                     system.consume(key)   # callbacks O(1) or async-queued — no sync stall
6. CAUSAL GRAPH    for cause in key.causes: CAUSAL_GRAPH.add_edge(cause → key.id)
7. AWARENESS       for cause in key.causes: cause.awareness += 0.1 (clamp 0–1)
```

**Immediate fan-out (sim-validated, §10):** average **13.4 observers per Key**. One event touches ~13 actors' memory/state synchronously before any cross-system or narrative ripple. At reference scale (30 seasons × 35 NPCs × 6 factions × ~90 events/season) that is 2,703 Keys in 144 ms — performance is not the constraint.

### Two parallel ripple channels in every Key
A Key carries effect along two decoupled tracks that coexist (§2.2):

| Channel | Field | Path | Lands as |
|---|---|---|---|
| **Symbolic** | `impact_vector` + `symbolic_dimensions` | armature dot-product → per-observer *interpretation* → memory salience | belief / disposition / concern / behavior change |
| **Mechanical** | `stat_deltas` | applied directly to observer state | Treasury, Discipline, L/PS, Composure, etc. |

The same betrayal both moves a Treasury number (mechanical) and rewrites how three witnesses read the betrayer (symbolic). Neither is derived from the other.

---

## §2 The Key as ripple-carrier — the fields that propagate

The ripple's *shape* is entirely determined by the emitted Key's fields (§2.2):

| Field | Controls | Ripple consequence |
|---|---|---|
| `causes[]` (0–3) | provenance | edges in CAUSAL_GRAPH; **the entire emergent-arc layer depends on this being populated** (§2.2 authoring guideline) |
| `targets[]` + role | who is affected, how | role ∈ {subject, object, witness, beneficiary, bystander} disambiguates downstream interpretation |
| `impact_vector` | signed projection on 4 Conviction axes | drives per-observer symbolic reaction |
| `stat_deltas` | raw mechanical change | drives state directly |
| `scale_signature` | scales the event runs at | **cross-scale propagation**: a peninsula+territory treaty ripples at both scales at once |
| `visibility` | who can form Memory | public → all in scale; semi-public → witness list; private → named list |
| `time_horizon` | immediate / near / far | salience factor (1.5 / 1.0 / 0.5) → how long the ripple persists in memory |
| `permanence` | transient / persistent / indelible | lifecycle: transient pruned; persistent decays to 0; indelible never decays |

**Visibility is the ripple's reach valve.** `da.covert_betrayal` is the clearest case (registry §3): `exposed=false` → only source + target know (ripple contained to 2 actors); `exposed=true` → witnesses added to semi-public observers **and a Legitimacy-violation event fires** — the ripple's radius and a secondary cascade both flip on one boolean.

---

## §3 The ripple topology — emitter → type → consumer

Cross-system propagation (§5 step 5) routes by `TYPE_SUBSCRIPTIONS[key.type]`. Consolidated from substrate §8 + each type's `consuming_systems`:

| Emitter | Key types emitted | Consumed by |
|---|---|---|
| `da_framework` | `da.public_governance`, `da.covert_betrayal`, `da.diplomatic_alliance`, `da.antinomian_action`, `da.economic_intervention` | faction_layer, npc_behavior, conviction_track, settlement_economy, articulation |
| `fieldwork` | `meta.knot_formed`, `meta.knot_ruptured`, `state.belief_revised` | npc_behavior, conviction_track, articulation |
| `threadwork` | `meta.thread_woven`, `scene.thread_operation` | conviction_track, npc_behavior, articulation |
| `scene_slate` | `mechanical.scene_activated`, `scene.*` | (scene-scoped consumers) |
| `social_contest` | `scene.dialogue` (persuasion-displacement payload) | npc_behavior, articulation |
| `mass_battle` | `scene_outcome.battle_concluded`, `scene.*` | faction_layer, articulation |
| piety / scar | (consumes `scene.witness`) → emits `state.scar_acquired` | faction_layer (leader scar → Cascade), npc_behavior, articulation |
| turmoil | `env.peninsular_strain_shock` | faction_layer (public-temperament), articulation |
| `miraculous_event` | `meta.miraculous_event` | faction_layer, npc_behavior, articulation |
| `faction_layer` | `state.succession`, `state.coup_attempted`, `mechanical.mission_shift`, L/PS-threshold Keys | (re-consumed by faction_layer + npc_behavior + articulation) |

Two structural observations:

- **`conviction_track` (PP-684) is not a normal node — it is the interpretation substrate.** Every Key's `symbolic_dimensions`/`impact_vector` projects onto its 4-axis matrix; every observer's armature reads through it. It sits *under* the topology, not beside it.
- **`articulation` subscribes to *all* Key emissions (§5).** It is the universal sink. Nothing is emitted that articulation does not see.
- **`faction_layer` is the densest hub** — it consumes `da.*`, leader scars, successions, strain shocks, and the full behavioral stream, and emits state-transition Keys that re-enter the same stream. This is where most cross-system loops close (see §5).

---

## §4 The emergent-narrative cascade — how atomic Keys become arcs

This is the "combinatorial emergent narrative" layer. Atomic Keys compound through five stages:

```
atomic Keys
   │
   ├─► CAUSAL GRAPH (§5)   walk_backward = the chain that produced an event
   │                       walk_forward  = the cascade of its consequences
   │                       awareness accumulates on causes reused in chains (§5.1)
   │
   ├─► ARC PRIMITIVES      meta.knot_formed / meta.knot_ruptured   (Bond arcs)
   │                       meta.thread_woven                       (influence arcs)
   │
   ├─► CASCADE CLUSTERS    Tier-2 trigger 9: cosine_similarity(faction_a, faction_b
   │                       cascade_fidelity history[-4:]) > ±0.40, sustained ≥4 seasons
   │                       → emergent cross-faction alignment/opposition, not authored
   │
   ├─► NARRATIVE WEIGHT    per-actor accumulator; rises as their Keys go un-articulated,
   │                       resets on cut scene (§3.3) — anti-starvation pressure
   │
   └─► ARTICULATION (PP-688)
         Tier 1  protagonist UI lens (concern queue, memory salience, bonds)
         Tier 2  cut scenes on 10 triggers; significance 0–13
                   = stakes_weight + protagonist_alignment + cascade_event_weight
                     + accumulated_narrative_weight   (§3.2); 5 / 10 / 15-sec render
         Tier 3  annual Chronicle (omniscient, 5–12 paragraphs/year), top-N Keys by
                   universal significance, templated from payloads + Conviction
                   interpretations + **causal-graph chains** (§4.5)
```

The chronicle is engine-rendered, not authored, and is the save's portable narrative record across multi-decade campaigns (§4.6). **The causal graph is the spine of all of it** — the chronicle's "what led to what," the "Why?" diagnostic walk, and the awareness-weighting of significant causes all read the same edges.

This realizes the canonical `intent_of_game`: *a positive feedback loop between player decisions and mechanics that produces emergent narrative.* The engine is the mechanism that makes that loop literal — see §5, loop L0.

---

## §5 Feedback-loop catalog — where ripples come back around

A "ripple" that returns to its origin is a feedback loop. The resolution-diagnostic Lesson 5 standard: a loop is a defect when it is **both undamped (gain ≥ 1 per cycle) and unbounded (no cap on the amplified variable)**. Classifying every loop the topology supports:

| # | Loop (edges) | Kind | Damper | Bound | Status |
|---|---|---|---|---|---|
| **L0** | player decision → Key emission → world/state change → articulation (cut scene / chronicle) → player decision | **intended positive** (the game *is* this loop) | player pacing (human in loop) | none mechanical | by design positive; res-diag flags `intent_of_game` itself as a positive loop needing Lesson-5 discipline |
| **L1** | `da.*` → faction_layer L/PS update → Public Expectation / Mission → npc_behavior → more `da.*` (§8.1, §8.6) | reinforcing | L/PS dynamics | L/PS are bounded meters | damped; bound plausible but `[UNVERIFIED]` — needs L/PS cap confirmation |
| **L2** | combat death → faction Stability → muster quality → combat (res-diag worked example; `faction_layer §1.5` + `military_layer §1.5`) | reinforcing collapse | Stability recovery (+1/season) | **floor = 0 = collapse = extinction; no cap short of termination** | **damped but terminally unbounded — a true finding in res-diag** |
| **L3** | cascade_fidelity → cluster detection (trigger 9) → cut scene → player attention → `da` → cascade_fidelity | reinforcing, player-mediated | fires once/regime, refire on transition (detection self-bounds) | regime gating | detection bounded; behavioral closure is L0 |
| **L4** | `scene.witness` / `da.covert_betrayal(exposed)` → `state.scar_acquired` → memory (high salience) → disposition update (§8.3 proc D) → npc_behavior → more conflict | reinforcing grievance | salience decay (§4.5) | persistent decays to 0; **indelible (witnessed death, ruptured Knot) never decays** | damped for persistent; **indelible scars are a permanent ripple source** `[synthesis]` |
| **L5** | turmoil accumulation → `env.peninsular_strain_shock` → faction public-temperament → behavior → turmoil (§8.6, §8.1) | reinforcing | `[UNVERIFIED]` | `[UNVERIFIED]` | **unclassified — damper/bound not read; flag for audit** `[synthesis]` |
| **L6** | `meta.knot_ruptured` → 5 Composure damage (load-bearing) → behavior under low Composure → further rupture risk | reinforcing | Composure recovery `[UNVERIFIED]` | Composure is a bounded resource | partially grounded; recovery unconfirmed |

---

## §6 Engine-level safeguards vs. the behavioral-loop gap — **the central finding**

The substrate provides real, sim-validated safeguards — but they bound the *bookkeeping*, not the *behavior*.

**What the substrate bounds (grounded):**
- **Provenance graph is acyclic by construction** — invariant 4 + §4.6 BFS reject any `causes[]` that would cycle (V1 sim-confirmed). Hard structural guarantee.
- **Memory ripples self-bound** — salience clamped 0–3, decays by horizon factor (§4.5), → decayed → pruned for transient (§4.8). V2 confirmed salience monotone-decreasing absent re-write.
- **Awareness clamped 0–1.** Subscription callbacks O(1)/async (no synchronous cascade stall). Determinism guaranteed within one architecture (§6) — every cascade is exactly replayable from `(initial_state, KEY_LOG)`.

**What it does NOT bound — and this is the load-bearing risk:**

> The acyclic-provenance guarantee is **necessary but not sufficient** for loop safety. Every iteration of a *behavioral* loop (L1–L6) emits a **new Key with a new id, legitimately caused by the prior one**. The DAG therefore grows strictly *forward* and never trips cycle detection — even as the underlying systems spiral. A collapse spiral (L2) is, to the substrate, a perfectly valid, perfectly acyclic chain of well-formed Keys.

**Loop safety is delegated, in full, to the consuming systems** — and the substrate offers no registry, audit, or gate that says which cross-system edge has a damper and which has a cap. There is no engine-level "this loop is bounded" assertion anywhere in PP-687/688. That audit has to be done per-loop, by hand, exactly as the resolution-diagnostic does it. L2 is the proof that the gap bites: a documented, canonical loop that is damped yet terminally unbounded.

---

## §7 Stress points / risks (worst-first)

1. **Behavioral feedback loops are unbounded at the substrate; loop-safety is system-delegated with no central audit (§6).** The #1 ripple risk. The engine cannot stop a degenerate runaway; only per-system dampers/caps can, and there is no inventory of which loops have them. **Fix:** run the resolution-diagnostic Phase-4 pass over every cross-system edge in the §3 topology and produce a loop-by-loop damper/cap ledger. L2 and L5 are the first targets.

2. **Sparse `causes[]` is a load-bearing narrative-quality risk.** Only ~15% of Keys carry causes (§10). The §2.2 guideline is explicit: *"This is not optional for emergent narrative legibility; sparse `causes[]` produces shallow chains."* The entire combinatorial layer (causal walks, chronicle "what led to what," awareness weighting) is only as rich as emitters' diligence in populating `causes[]`. Under-populate, and "combinatorial emergent narrative arcs" degrades to a flat event log. This is a discipline/tooling gap — but it is *the* determinant of whether arcs actually emerge. **Fix:** authoring lint / emitter contract requiring `causes[]` wherever a prior Key is known to have driven the event; measure causes-density as a first-class metric.

3. **Rollout gap → partial cascade / dead edges.** Phase B per-system migration is incomplete (status unverified this session). Un-migrated systems emit legacy events wrapped as `meta.legacy_event`, which downstream consumers **skip** (§7.2). Ripples therefore do not propagate *from* an un-migrated system until it is migrated — the cascade is only as complete as the migration. **Godot Phase 5a is unbuilt**, so none of this executes yet. The architecture is sim-validated, not running.

4. **Ripple magnitudes are uncalibrated.** Salience form (§4.5), significance weights (§3.2), accumulated-weight reset (§3.3), and most Tier-2 trigger thresholds are "calibrate at Stage 10." Trigger 9 is calibrated (±0.40 from Stage-10 A6 evidence); the rest are provisional. The cascade's *topology* is settled; its *gains* are not.

5. **Doc-hygiene drift (minor).** `canon/intent_of_game.yaml` is HTTP 404 — the canonical positive-loop spec survives only as the PI one-liner and an architecture mention. `key_substrate_v30.md` closes with "PROVISIONAL pending ratification" while its header and `canonical_sources.yaml` mark it CANONICAL. Neither changes any verdict; both should be reconciled.

---

## §8 What is verified vs. open

**Verified this session (high confidence):** the atomic cascade mechanism (§1), the ripple-carrier fields (§2), the cross-system topology (§3), the emergent-narrative cascade (§4), the engine-level safeguards and the behavioral-loop gap (§6). Substrate self-reports V1–V6 sim-confirmed.

**Not verified (flagged):** per-loop dampers/caps for L1, L5, L6 (`[UNVERIFIED]`); the loop closures marked `[synthesis]`; Phase B migration completeness and any Godot implementation in `valoria-game`; all Stage-10 calibration values.

---

## §9 Open questions / next steps

- **Loop-safety ledger** — the highest-value follow-on: a Phase-4 damper/cap audit across the §3 topology, closing the §6 gap. Produces a canonical "which ripples are bounded" table.
- **Causes-density discipline** — decide the emitter contract / lint for `causes[]` (risk #2).
- **Rollout truth** — audit Phase B migration state + check `valoria-game` for any Key-substrate code (the open question from the prior turn).
- **Calibration plan** — sequence the Stage-10 magnitude calibrations (risk #4).
- **Doc reconciliation** — recreate or formally retire `intent_of_game.yaml`; strike the stale PROVISIONAL trailer.

*Nothing in this scope changes canon. It is a read-only propagation map. If useful, it belongs in `designs/audit/2026-06-04-key-cascade-scope/` — ask before I commit.*
