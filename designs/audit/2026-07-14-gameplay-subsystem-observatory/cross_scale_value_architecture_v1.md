# Cross-Scale Value Architecture — Three Axes (v1)

## Status: FILED — 2026-07-14 · ED-IN-0064 · companion to `subsystem_synthesis_v1.md` + `directional_coverage_v1.md`

> A re-cut of the observatory findings along three architectural axes Jordan named: **(1)** the executable object
> stack (wrappers · engines · modules · adapters); **(2)** the Key/data plane (keys · schema · I/O location) and
> **(2.a)** transport of values across scales / propagation between subsystems; **(3)** aggregation/differentiation
> and escalation/de-escalation of value *weights* across scales — i.e. **how the system manages the context of
> content** as it moves between scales. Grounded in the same working-tree run; **leads, not verdicts** (L0 gate
> FAILED 1/3); **all fixes HELD-BACK (ED-1094)**. These three axes are three *planes* of the same architecture —
> objects, data, and semantics — and each has a distinct debt profile.

---

## Axis 1 · Wrappers · Engines · Modules · Adapters — the executable object stack

**The intended stack.** Valoria's code is meant to layer as
**Adapter → Engine → Module → Wrapper(resolver-family) → dice/accounting primitive**:

- **Engine** — the per-subsystem resolver object. The canonical form is `personal_combat`'s `CombatEngine`, which
  `extends BaseEngine`. `references/module_contracts.yaml` treats each of its 27 modules as the **conversion unit** —
  one engine or service per entry.
- **Module** — a sub-resolver *inside* an engine. Realized in exactly one place: `personal_combat` hosts an
  11-EngineModule sub-list (`strike`/`wound` ported, `armour_defeat` folded, 8 pending). The other 26 contracts are
  **flat** — no engine→module decomposition.
- **Wrapper** — the resolver-family that adapts a subsystem's inputs into a resolution call: `d_sigma` (continuous
  d+σ), `dice_pool` (v30 pool), `deterministic_accounting`, `state_reader`, `manifest`, `clock_advance`. Social
  contest has this literally — `sim/personal/contest/wrapper.py` wraps its four contest games (with the Consensus
  game a `NotImplementedError` STUB).
- **Adapter** — the boundary layer. `tools/sim_harness/adapters` (an import cut-vertex, **out-17**) adapts the sim
  reference to the campaign/test harness; the Godot data-manifest adapters (`engine_manifest.gd`,
  `key_type_resource.gd`) mirror `module_contracts.yaml` into Godot resources.

**What the observatory found about this stack.**

1. **The stack is realized for 1 of 27.** Only `personal_combat` instantiates engine→module. The **spine that would
   make the pattern real everywhere** — `BaseEngine`, `EngineModule`, `KeyBus`, `GameState`, `Resolver` — is
   **defined nowhere in the corpus** (grep-confirmed: zero `class_name` matches). So outside the combat slice, the
   wrapper→engine→module→adapter stack is a *design intent*, not a built layer; the Godot skeleton cannot compile.
2. **Import cycles mark where object boundaries are muddy.** G_code found 3 cycles: the **9-module `sim.personal.contest`
   SCC** (an engine whose internals — appraise/armature/dictionaries/faction/modes/resolver/rhetoric/wrapper — are
   mutually coupled rather than layered), `massbattle↔units`, and `game_state↔npe`. A clean engine/module layering
   would be a DAG; these SCCs are the object-boundary debt.
3. **Cut-vertices are the load-bearing joints — and they are adapters/dispatchers, not engines.** The 14 code
   cut-vertices are led by `game_state`, `sim_harness.adapters`, `faction_action`, `echo_transport`, `scene_dispatch`.
   The system's single-points-of-failure are the **transport/adapter layer**, not the subsystem engines — which is
   architecturally telling: the engines are replaceable, the plumbing is not.
4. **Contract↔code identity is a BLACK HOLE.** Nothing joins the 27 contract "engines" to G_code's 173 code
   modules; a plain name-match resolves only **3/27** (the code spells `mass_battle` as `massbattle`, folds
   `faction_state` into `faction_action.py`). So the object layer's *identity* — which code module *is* which
   contract engine — is unverified. A fabricated engine entry would pass unchallenged.

**Solution direction (HELD-BACK).** The missing map is `canon/mechanics_index.yaml`'s `sim_module:` field — a
contract-engine ↔ code-module join that would close the black hole (GAP-I4). The missing *layer* is the Gate-0 spine
(`BaseEngine`/`EngineModule`/`KeyBus`) from `godot_conversion_strategy_v1.md` — authoring it is what promotes
"engine hosts modules, adapter bridges to runtime" from combat-only to universal. Until both exist, the stack is
real for combat and aspirational elsewhere.

---

## Axis 2 · Keys · Schema · Location of Inputs and Outputs — the data plane

**The substrate.** All cross-object communication is Keys — "no system maintains a private event channel; every
system emits and consumes Keys" (`key_substrate §1`). One **single update rule** (§4.1): emit → validate (registry +
invariants + `causes[]` DAG) → append to the immutable `KEY_LOG` → **resolve observers** (§4.2 `compute_observers`) →
apply `stat_deltas` to each. 49 Key types in `key_type_registry_v30.md`.

**The schema — and where I/O actually lives.** A Key type's schema fields: `type_id`, `emitting_systems`,
`consuming_systems`, `default_scale_signature`, `default_permanence`, `default_time_horizon`. A module's schema:
`consumes:[{type, from}]`, `emits:[{type, terminal}]`, `state:[{name, bucket, writable}]`, `derivations`, `gates`.
The load-bearing observation is that **a single value's I/O is dispersed across three homes that don't cross-check**:

| Facet | Lives in | Consequence |
|---|---|---|
| **who emits / consumes** a type | `key_type_registry` (`emitting_systems`/`consuming_systems`) | the transport addressing |
| **a module's owned state** | `module_contracts.state[]` (track / clock / pool / **derived_value**) | the F1 guard: `derived_value` is read-only, never written directly |
| **how a value is computed** | `params/*.md` prose tables (untyped) | the pointer-debt gap — 47% of identifiers don't resolve |

**What the observatory found about the data plane.**

1. **The schema itself is IN FLUX.** `descriptor_registry.yaml` marks the 9-attribute roster IN FLUX, aggregates as
   `placeholder`/not-wired; **Combat Pool is defined three different ways** across `values_master`, `params/core.md`,
   and `module_contracts`. There is no typed engine-params file — every value crossing into Godot is hand-transcribed
   prose. So the schema's *canonical form* is unsettled, which is upstream of most pointer-debt.
2. **The holes are output-side, not input-side.** **0 phantom producers** (every `consumes` names a real emitter —
   the input graph is closed) but **4 dangling emits** (outputs consumed nowhere) + `env.crisis` reaching no concrete
   consumer. So inputs are well-addressed; **outputs leak**.
3. **One schema violation is a fabricated `type_id`.** `mass_battle`'s `scene_outcome.battle_concluded` uses a
   *family name* as a type prefix — a schema-discipline breach (ED-MB-0010; canon writes `scene.battle_concluded`).
4. **Pointer-debt is fundamentally a *location* problem.** 52.7% of identifiers resolve to a registry key. The
   unresolved cluster isn't random — it's the values whose *home is undecided*: `victory`'s era reads
   (MS/Accord/PV/PT), combat's Wounds/Poise/Initiative, and — the hard case — `npc_behavior`'s
   `beliefs/opinions/arc-state`, which are **non-scalar structured state** the scalar registry can't place at all
   (GAP-G2, a design ruling). The schema can't yet say *where these live*.
5. **The direction-carrying fields are the sparsely-populated ones.** `scale_signature`, `permanence`, `time_horizon`
   are the schema fields that encode *how far and how long a value reaches* — and they're default-valued. Populating
   them **is** the §12.3 discipline (Axis 2.a). The schema has the slots for context; they're mostly empty.

**Solution direction (HELD-BACK).** A typed engine-params file (numeric operands, structured formulas, explicit
clamps) generated from the prose and round-trip-checked (CLAUDE.md §5's recommended-not-built) would move
computation out of prose into the schema. Registering the placeable pointers is CTC; deciding where non-scalar state
lives is a Jordan ruling. Closing the 4 output leaks is CTC (wire declared consumers).

### Axis 2.a · Transport of values across scales · propagation between subsystems

**One substrate, all directions — transport correctness = authoring discipline.** Direction is not a routing table;
it is an **emergent property** of a Key's `targets[]`, `scale_signature`, and `causes[]` (`scale_transitions §12.1`).
This is the architecture's most elegant decision and its biggest liability at once: because there is no per-direction
channel to be "missing," transport correctness collapses onto whether emitters *populate the addressing fields*. The
directional audit (`directional_coverage_v1.md`) graded the seven directions:

| Transport state | Directions | Meaning |
|---|---|---|
| **LIVE end-to-end** | lateral · bottom-up Domain-Echo core (`ECHO_TRANSPORT` default ON) | the value reaches its observer, verified |
| **ANNOTATION-DEBT** | top-down · down-diagonal (the 8 §12.4 `!A6` seams) | mechanism runs elsewhere; this emitter's sub-scale `targets[]` is blank → delivers *blind* |
| **DEAD** | diagonal (`causes[]` populated **nowhere** — zero instances); Accord-echo + territory-transfer (built resolvers, **zero callers**); handoff dispatcher (orphaned) | the value cannot cross this way at all today |
| **DEFERRED** | temporal (`decay()` unshipped) | values transport across *space* but not across *time* |

**Propagation between subsystems** has a distinct shape from transport-across-scales: the module-pair graph is a
**wide producer front → two integration hubs → thin reader tier**. `faction_state` (in-13) and `npc_behavior`
(in-12) absorb nearly every subsystem's output — and both are L2 cut-vertices *and* both run an unverified
`[ASSUMPTION]` resolver. So the propagation topology's two bottlenecks are also its two least-grounded nodes: **the
places the most value flows through are the places the resolution is least certain.** That is the highest-leverage
grounding target in the whole system.

**Solution direction (HELD-BACK).** Transport: the debt is authoring — populate `targets[]`/`scale_signature` for
the 8 seams (CTC), author the *first* `causes[]` diagonal exemplar (the one genuine build, GAP-DIR-1), wire the two
uncalled resolvers (CTC). Propagation: ground the two `[ASSUMPTION]` hubs before anything else — every downstream
value passes through them.

---

## Axis 3 · Aggregation / Differentiation · Weight Escalation / De-escalation across scales — managing the context of content

This is the deepest axis: not *whether* a value moves, but *how it changes* — and by how much it should *count* — as
it crosses a scale. Valoria has two first-class propagation regimes (`holonic_container_doctrine_v1`,
`propagation_spec_v1`): **nested aggregation** (personal→settlement→territory→province→national) and **collision of
stresses** (an exogenous shock acting up and down at once). The observatory surfaced a **sophisticated but
un-unified** value-transformation layer.

**Aggregate-up (many sub-values → one super-value) — three different disciplines coexist, unreconciled.** From the
live derivations (`module_map_flat §4.4`, verified):

| Up-map | Formula | Discipline | What it costs |
|---|---|---|---|
| Order → province **Accord** | `floor(mean settlement Order)` | **mean** | loses the distribution — masks peripheral collapse (the D4 finding) |
| L/PS → faction **Mandate** | `q_s=0.5L+0.5PS; T=Σ W_s·(q_s/7); Mandate=round(7T/(T+6))` | **weighted + saturating** | the sophisticated one — see below |
| Prosperity → **Treasury** | `Σ Prosperity × 10` | **flat sum** | no weight, no saturation — unbounded linear |

The Mandate aggregation is the model to generalize: **`W_s = base(Type)+Prosperity+FacilityTier` is literally the
"escalation of value weight across scales"** — a bigger/richer/more-built settlement's contribution is *escalated* by
its size before it aggregates, and `7T/(T+6)` **saturates** (diminishing returns as total weight grows). That is
exactly the "manage how much content counts" control Jordan is asking about — realized for Mandate, absent for Accord
(unweighted mean) and Treasury (unweighted sum). **Three aggregation disciplines, one subsystem apart, with no
shared primitive** (governance GAP-E1, "collision primitive not unified").

**Distribute-down (one super-value → many sub-values) — one live path, rate-limited.** Mandate → L/PS:
`drift ±1/settlement/season toward Mandate (damped, mean-reverting; Stage-4 bounded 30 seasons)`. This is
**differentiation by damped mean-reversion** — each settlement's L/PS is pulled toward the faction value, but slowly,
so the down-distribution can't whiplash. It is the *only* live down-differentiation; the governance-type top-down
cascade is doctrine-only. So the system distributes *value* down (Mandate→L/PS) but not *policy/type* down.

**Escalation vs de-escalation of weights — the asymmetry is the gap.**

- **Escalation (up) is gated and prioritized — real context control.** **Sufficient Scope (§7)** is the up-escalation
  gate: a scene value only escalates to the faction scale if it clears a scope threshold, capped at **1 Echo per
  faction per scene**, and **priority-ordered** (Thread op → Combat victory → Settlement governance → Disposition →
  Investigation → Faction-leader-direct → Other). This *is* "managing the context of content": Sufficient Scope
  decides *which* scene content is significant enough to become a strategic consequence, and the priority order is
  the weight ranking. This half exists and is thoughtful.
- **De-escalation (down/decay) is UNSHIPPED — the asymmetry.** There is **no entropy** pulling values back down over
  time. `decay()` is an explicit deferral (GAP-DIR-5; `key_echo_armature`: "ships WITHOUT decay… deferred to
  Stratum B+"). Concretely, `ΔLegitimacy` event-builds with `+λ×seasons_in_role` and **no decay term** (governance
  GAP-B4). So values **escalate but never de-escalate** — over a long campaign, legitimacy/standing/pressure ratchet
  upward toward saturation. The weight-management system has an accelerator and no brake.

**Managing the context of content — the four mechanisms, and where they hold.**

1. **`scale_signature`** — the per-Key context tag: which scales a value is "in context" for. Sparse signatures (the
   §12.3 debt) = values delivered *without* context (blind). *Partly populated.*
2. **`causes[]` DAG** — the provenance context: what a value descends from. **Never populated** — so no value carries
   its causal context (the diagonal gap). *Empty.*
3. **The significance-function / `articulation_layer`** — the repo's explicit context-*weigher*: a universal wildcard
   reader that scores the significance of the entire Key stream for rendering/chronicle. But it **emits nothing** —
   it is a read-only significance meter, *not* a control that feeds weight back into resolution. So context is
   *observed* but not *acted on*. *Read-only.*
4. **The termination artifact / convergence proof** — the deepest one. `holonic_container_doctrine §4` requires an
   aggregate-up/distribute-down primitive *plus a convergence proof*; `propagation_spec_v1` proves only per-tick and
   per-cascade termination, **not cross-tick convergence** (GAP-A4; the D.6 double-count risk). So the system cannot
   yet guarantee that repeated up-then-down cycles **settle** rather than **oscillate or double-count**. Without it,
   aggregating up and redistributing down every season may amplify rather than converge. *Unproven.*

**Synthesis of Axis 3.** Valoria's cross-scale value semantics are richer than most strategy games attempt — a
weighted saturating aggregation (Mandate), a damped mean-reverting distribution, and a gated/priority-ordered
up-escalation (Sufficient Scope). But they are **un-unified and asymmetric**: three different aggregation formulas
with no shared primitive; escalation-up without de-escalation-down (decay deferred); a significance-weigher that
observes but doesn't feed back; and no proof that the up-down loop converges. **"Managing the context of content"
across scales is therefore ~60% built and ~40% deferred** — the escalation and weighting half is real, the decay and
convergence half is the reserved work.

**Solution direction (HELD-BACK).** This is precisely the artifact the doctrine reserved for top-of-stack (fable-tier)
authorship (`holonic_container_doctrine §4` / ED-1083): **one unified aggregate-up/distribute-down primitive** that
takes a weight function (generalizing `W_s`), a saturation curve (generalizing `7T/(T+6)`), a **decay term**
(shipping GAP-DIR-5), and a **cross-tick convergence proof** (closing GAP-A4). Generalize the Mandate pattern into
that primitive; make Accord and Treasury instances of it rather than bespoke formulas; give `articulation_layer`'s
significance score a feedback path if context is meant to *weight* resolution, not just narrate it. That single
primitive would unify Axes 2.a and 3 — transport carries the value, the primitive transforms and bounds it.

---

## The three axes as one picture

- **Axis 1 (objects)** is *aspirational above the combat slice*: the engine→module→adapter stack is real for
  `personal_combat`, undefined elsewhere (the missing spine), with the contract↔code identity unverified.
- **Axis 2 (data)** is *closed on input, leaky on output, dispersed on location*: inputs well-addressed, outputs
  leak, computation stranded in prose, schema in flux — and the direction-carrying fields mostly empty.
- **Axis 3 (semantics)** is *sophisticated but un-unified and asymmetric*: good weighted-saturating aggregation and a
  real up-escalation gate, but three un-reconciled aggregation disciplines, no de-escalation/decay, and no
  convergence proof.

The through-line across all three: **the substrate's elegance (one update rule, topology-neutral direction, one
delivery path) pushes all correctness onto two things — authoring discipline (populate `targets[]`/`scale_signature`/
`causes[]`) and one value-transformation primitive (unify aggregation/differentiation + weight + decay + convergence).**
Those two are the debt. Everything else the observatory flagged — pointer-debt, dangling emits, the seams, the
uncalled resolvers, the two `[ASSUMPTION]` hubs — is a symptom that resolves once those two are addressed.
