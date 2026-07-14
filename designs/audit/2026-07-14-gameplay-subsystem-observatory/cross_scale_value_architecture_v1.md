# Cross-Scale Value Architecture — Three Axes (v1, hardened 2026-07-14)

## Status: FILED — 2026-07-14 · ED-IN-0064 · **hardened after a four-agent adversarial + intensification pass**

> A re-cut of the observatory findings along three axes Jordan named: **(1)** the executable object stack
> (wrappers · engines · modules · adapters); **(2)** the Key/data plane (keys · schema · I/O location) and **(2.a)**
> transport of values across scales / propagation between subsystems; **(3)** aggregation/differentiation and
> escalation/de-escalation of value *weights* across scales — how the system **manages the context of content**.
> Grounded in the working-tree run; **leads, not verdicts** (L0 gate FAILED 1/3); **all fixes HELD-BACK (ED-1094)**.
> Every `code:`/`doc:` claim below was code-verified in the hardening pass (file:line cited).

---

## Correction log — Phase 2 (four independent read-only agents: three refute-by-default skeptics + one intensifier)

The first draft of this doc was a single synthesis pass written from accumulated context, without independent
verification. A four-agent pass (opus, read-only) refuted, confirmed, or deepened each claim. **Where this log
conflicts with anything below, this log wins.** What was wrong, and what changed:

- **[BIGGEST ERROR — fixed] "Collision of stresses" misattribution.** The prior draft called collision-of-stresses a
  regime of `holonic_container_doctrine`/`propagation_spec` — the phrase is in **neither** (grep-confirmed); it comes
  from `designs/audit/2026-07-13-cross-scale-governance-grounding/governance_grounding_v1.md` (Cut D). It also
  propped the "un-unified aggregation" claim on **GAP-E1**, which is about **MS distance-falloff + Calamity radiation +
  Peninsular Strain + Π homeostat** — *not* the Accord/Mandate/Treasury formulas. **Fix:** collision-of-stresses is
  now a correctly-attributed co-equal *second* regime (Axis 3 §C), and GAP-E1's "un-unified" verdict is applied to
  its real target (the four radiation systems), not to the nested-aggregation formulas.
- **[SUPERSEDED CANON — fixed] ΔLegitimacy "accelerator, no brake."** Leaned on `faction_behavior_v30 §3.5`, which
  carries a `[SUPERSEDED-BY LPS-1 (settlement_layer §1.8), 2026-05-30]` banner. And "no brake / ratchet to saturation"
  is false: the same formula has a `−λ_violation·score` term + a §3.5.2 violation-erosion subsection, and the *live*
  Mandate↔L/PS loop is Stage-4-sim-verified **mean-reverting, bounded 0–7, convergent over 30 seasons, "no runaway"**
  (`settlement_layer_v30 §1.8`). **Fix:** the real gap is narrowed to *no time-based/entropic decay term* (`decay()`
  deferred), and GAP-E3 notes an E11 suspicion-decay counter already exists in code.
- **[FABRICATION — removed] "~60% built / 40% deferred."** No source; an unsourced number dressed as a measurement.
  Deleted.
- **[WRONG FIELD — fixed] Axis 2 "scale_signature/permanence/time_horizon are default-valued/sparse."** All three are
  **~100% populated at the type level** (50/50/50 across 49 types). The genuinely-sparse field is the *per-instance*
  `targets[]` (0 occurrences in the registry; populated in exactly one live emitter, `echo_transport.py:146`). **Fix:**
  the §12.3 authoring debt is now correctly named as `targets[]`, not the type-level trio.
- **[MISMAPPING — fixed] "The 6 resolver-families are the wrappers."** The sim's own `contest/wrapper.py:4` says *"the
  wrapper ADAPTS + ROUTES; it RESOLVES NOTHING"* — so in the reference, **wrapper ≡ adapter/router**, not the
  resolver-family. **Fix:** Axis 1 now distinguishes the YAML `resolver:` *type-tags* from the code's wrapper=adapter
  objects, and notes ≥3 literal `wrapper.py` files (contest, combat_engine_v1, mass_battle).
- **[OVERREACH — fixed] "Cut-vertices are adapters/dispatchers, not engines."** ~6 of the 14 code cut-vertices are
  subsystem engines (`faction_action`, `parliamentary_vote`, `excommunication`, `infrastructure`, `ms_track`,
  `season`); I even mislabeled `faction_action` as an adapter while treating it as an engine elsewhere. **Fix:**
  reframed to "plumbing is a slight majority; engines are ~40%."
- **[OVERREACH — fixed] "Three homes don't cross-check" / "Combat Pool three ways" / "escalated by size."** (a) A
  partial cross-check *exists* (`ci_quantity_vocabulary_check` A17 + `quantity_registry.resolve()` + the resolved
  `tools/registry.py` facade, ED-IN-0057/0058) — the 52.7% figure itself rides on it. (b) Combat Pool is **one stale +
  two agreeing** (`max(5, History+6)`), not three divergent; my `PP-247` tag is itself superseded by ED-901. (c) The
  boundary transform is **quantize-and-throttle**, not weight-escalation (Axis 3 §B).
- **[MAJOR OMISSIONS — added]** the `engine/sigma_leverage_engine_armature.md` defined engine abstraction (Axis 1);
  the shipped **σ-leverage saturation kernel** (Axis 3 §A); the **`Field`/`Gauge` PROPOSED primitive** that already is
  the "future" recommendation (Axis 3 §E); the **quantize-and-throttle escalation math** (§B); **faction→national
  ruled non-nested** + **Territory tier doctrine-only** (§A); the **~27-rule value-transformation census** (§A);
  `tools/registry.py` + `meta.legacy_event` (Axis 2).
- **[CONFIRMED — held up]** the three aggregation formulas (verbatim), Sufficient Scope's priority order + 1/scene cap
  (verbatim, `scale_transitions §3.4/§5.1`), the transport spot-checks (`causes[]` nowhere; `compute_accord_echo` /
  `propose_transfer` zero callers; `ECHO_TRANSPORT` default ON), the two-hub in-13/in-12 `[ASSUMPTION]` finding, the
  F1 guard, the convergence-unproven analysis (bounded-oscillation, D.6 double-count), the 3/27 contract↔code black
  hole, and — correctly — *excluding* `agg.body/mind/social` from cross-scale (they are within-actor).

---

## Axis 1 · Wrappers · Engines · Modules · Adapters — the executable object stack

**The intended stack** is **Adapter → Engine → Module → resolver-family → dice/accounting primitive** — but the
observatory shows the *object identity* of that stack is only partly real, and the code's own vocabulary differs from
the four-layer taxonomy.

- **Engine.** The contract-formalized engine→module decomposition exists for **1 of 27** modules — only
  `personal_combat` carries a `modules:` sub-list (`module_contracts.yaml:844`, 11 EngineModules: strike/wound
  PORTED, armour_defeat FOLDED, 8 PENDING). *But at the code layer the decomposition is broader:* `social_contest`
  (`sim/personal/contest/`, a 9-file package with a `GAMES` router + `MECHANICS` registry) and `mass_battle`
  (`sim/provincial/massbattle.py` `resolve_*`) have genuine engine-internal structure — just not expressed as contract
  `modules:`. So "1 of 27" is a *contract-formalization* count, not a claim that only combat has internal modules.
- **The Godot spine is undefined** — zero `class_name BaseEngine|EngineModule|KeyBus|GameState|Resolver` in any
  `.gd`; the skeleton `extends BaseEngine`/`EngineModule` against nothing, so it cannot compile. (Honest scope: a
  Python `GameState` exists in *test scaffolds* — `tests/sim_framework/state.py` — but `sim/autoload/game_state.py`
  defines `Faction`/`Territory`/`World`, not a `GameState` class, and none is the Godot spine.)
- **There IS a defined engine abstraction the first draft missed:** `engine/sigma_leverage_engine_armature.md` — a
  committed, **system-agnostic "portable resolution engine"** with an explicit **ENGINE-vs-APPLICATION portability
  boundary** and a method for porting the d+σ resolver to "any Valoria dice-resolved system." It is *prose*, self-marked
  **Class B (draft sim-seed, not canonical)** — but it is the nearest thing in the corpus to a defined engine spine, and
  it is exactly where the resolver-family plugs into an engine. The Godot `BaseEngine` is undefined; this armature is not.
- **Wrapper = Adapter, in the reference.** The code's own wrapper concept (`sim/personal/contest/wrapper.py:4`) says
  *"the wrapper ADAPTS + ROUTES; it RESOLVES NOTHING."* So Jordan's *Wrapper* and *Adapter* layers are, in the sim, the
  **same object** — a router, not the resolver. There are **≥3 literal `wrapper.py`** (contest, `combat_engine_v1/`,
  and `mass_battle`'s `engine.py` which contest "mirrors"). The six **resolver-families** (`d_sigma`, `dice_pool`,
  `deterministic_accounting`, `state_reader`, `manifest`, `clock_advance`) are the YAML `resolver:` *type-tags* on the
  27 contracts — category labels, not wrapper objects.
- **Adapters are the healthiest-defined layer** — `tools/sim_harness/adapters` (a cut-vertex, out-17) bridges the sim
  reference to the campaign/test harness; the Godot `engine_manifest.gd`/`key_type_resource.gd` mirror
  `module_contracts.yaml`. But these are *harness/data* adapters; the runtime *KeyBus* adapter is the undefined spine.

**What the object graph reveals.** The 14 code **cut-vertices** are **~8 transport/adapter + ~6 subsystem engines**
(`faction_action` in1/out9, `parliamentary_vote`, `excommunication`, `infrastructure`, `ms_track`, `season`): plumbing
is a slight majority, but engines are ~40% — so "single points of failure are the plumbing" is a *tendency*, not a
clean rule. Three **import cycles** mark muddy boundaries (the 9-module contest SCC; `massbattle↔units`;
`game_state↔npe`). And **contract↔code identity is a black hole** — a name-match resolves only **3/27**
(`scene_slate`, `victory`, `miraculous_event`); even `personal_combat`, the one fully-decomposed engine, is *unmatched*
(`massbattle`≠`mass_battle`, `faction_state` folded into `faction_action.py`). A fabricated engine entry would pass
unchallenged. **Fix (HELD-BACK):** the `mechanics_index.yaml sim_module:` join closes the identity black hole; the
Gate-0 spine makes the engine→module→adapter stack real beyond combat — and the `engine/` armature is the design seed
for that spine.

---

## Axis 2 · Keys · Schema · Location of Inputs and Outputs — the data plane

**One substrate.** All communication is Keys through the single update rule (`key_substrate §4.1`): emit → validate
(registry + invariants + `causes[]` DAG) → append to the immutable `KEY_LOG` → resolve observers (`§4.2
compute_observers`) → apply `stat_deltas`. 49 Key types.

**Where a value's I/O lives — three homes, only *partially* cross-checked.** *Who emits/consumes* lives in
`key_type_registry_v30.md` (`emitting_systems`/`consuming_systems`); *owned state* in `module_contracts.state[]`
(track / clock / pool / **derived_value**, the last read-only under the **F1 guard** — a formal canon rule,
`propagation_spec §42/147`, that no aggregate is ever written directly); *how it's computed* in **untyped `params/`
prose**. These are cross-checked *in part* — `ci_quantity_vocabulary_check` (A17) + `quantity_registry.resolve()` +
the resolved `tools/registry.py` facade (ED-IN-0057/0058) reconcile the *vocabulary* of homes #1–#2, and the doc's own
**52.7% pointer-resolution** figure is produced by exactly that check. The strictly-true residue: **no tool verifies
I/O *consistency* across all three homes, and home #3 (params prose) is outside any check** (A18 unbuilt). So the
dispersion is real but narrower than "don't cross-check."

**What the observatory found.**
1. **The schema is IN FLUX** (`descriptor_registry.yaml:12`; aggregates `placeholder`). The oft-cited "Combat Pool
   three ways" is really **one stale + two agreeing**: the struck `(Agility×2)+History+3` (pre-ED-901, self-flagged) vs
   the canonical `max(5, History+6)` in both `params/core.md:161` and `module_contracts.yaml:858` — a currency problem,
   not three-way divergence.
2. **Holes are output-side, not input-side.** 0 phantom producers (every `consumes` names a real emitter) but **4
   dangling emits** — `scene_outcome.battle_concluded` (fabricated type, ED-MB-0010), `env.crisis`, `scene.combat_felled`,
   `scene.combat_resolved` — with `env.crisis` being one of those 4 (not a 5th), reaching no concrete consumer.
3. **Pointer-debt is a *location* problem** (52.7% resolve). The unresolved cluster is the values whose *home is
   undecided*: `victory`'s era reads, combat's Wounds/Poise/Initiative, and — the hard case — `npc_behavior`'s
   non-scalar `beliefs/opinions/arc-state` (a Jordan design ruling, GAP-G2).
4. **The direction-carrying discipline is the per-instance `targets[]`, not the type-level tags.**
   `default_scale_signature`/`default_permanence`/`default_time_horizon` are ~100% populated per type (50/50/50);
   `targets[]` occurs **0 times** in the registry and is populated in **one** live emitter (`echo_transport.py:146`).
   Populating `targets[]` **is** the §12.3 debt (Axis 2.a). Note `permanence` (transient/persistent/**indelible**) is
   itself relevant to Axis 3 — an `indelible` Key by definition never decays.
5. **Two misses the first draft's production-side census can't see:** `tools/registry.py` (a *resolved* 2026-07-13
   vocabulary-unification facade — directly undercuts the "not-built" framing) and `meta.legacy_event` (a registered
   type **never emitted** — a Phase-B migration scaffold, retired; the census only audits `module_contracts` I/O, not
   the registry's 49 types for emitter reality).

### Axis 2.a · Transport across scales · propagation between subsystems

**Because direction is emergent** (a Key's `targets[]`/`scale_signature`/`causes[]`, `scale_transitions §12.1`),
transport correctness collapses onto authoring discipline. Of seven directions (verified this pass): **2 live**
(lateral + bottom-up Domain-Echo core, `ECHO_TRANSPORT` default ON, `mc_v18.py:47`), **2 annotation-debt** (the 8
`!A6` down-seams — sparse `targets[]`), **3 dead** (diagonal `causes[]` populated **nowhere** in `sim/`;
`compute_accord_echo` + `propose_transfer` **zero callers**; handoff dispatcher orphaned), **1 deferred** (`decay()`).
**Propagation between subsystems** is a wide producer front → **two hubs (`faction_state` in-13, `npc_behavior` in-12)**
→ thin reader tier, and both hubs are `[ASSUMPTION]`-resolver: **the highest-value flow passes through the
least-certain resolution.** Ground the two hubs first.

---

## Axis 3 · Aggregation / Differentiation · Weight Escalation / De-escalation across scales — managing the context of content

This is the deepest axis, and the hardening pass changed the picture substantially. There are **two regimes** (not
one), the "escalation" is really **compression**, the un-unified surface is **~27 rules** (not three), and the unified
primitive the first draft "reserved for the future" **already exists as a proposed schema**.

### §A · Nested aggregation — three cross-scale rollups, and the rigorous "un-unified" census

The live nested-aggregation rollups (verified verbatim, `settlement_layer_v30 §1.3/§1.8`, `derived_stats §8.1`):

| Up-map | Formula | Rung | Discipline |
|---|---|---|---|
| Order → province **Accord** | `floor(mean settlement Order)` | settlement → **province** | floor-mean (loses distribution) |
| L/PS → faction **Mandate** | `q_s=0.5L+0.5PS; T=Σ W_s·(q_s/7); Mandate=clamp(round(7T/(T+6)),0,7)` | settlement → **faction** | weighted + **saturating** |
| Prosperity → **Treasury** | `Σ settlement Prosperity × 10` | settlement → **faction** | flat sum |

Two corrections to the first draft's framing: (a) canon groups these **2 + 1** — `settlement_layer §1.8` explicitly
unifies **Mandate and Treasury** as the settlement→*faction* rollup, with **Accord** as the settlement→*province*
rollup; "three disciplines one subsystem apart" flattened that tier line. (b) The Mandate `clamp(...,0,7)` (K=6) is
canonical (dropped in the first draft — numerically redundant but incomplete). `W_s = base(Type)+Prosperity+FacilityTier`
is a real **weight-escalation** term — a bigger/richer/more-built settlement's acceptance "counts for more" before it
aggregates (`§1.8:158,162`) — *within* the settlement→faction rollup.

**Making "un-unified" rigorous.** The claim is not "three formulas differ" — it is that there is **no shared
aggregation contract anywhere in the corpus**. The full census (consolidated from
`.../pressure_key_registry_v1.md`) is **~11 live aggregate-up formulas across six saturation postures** — saturating
(Mandate; and σ-leverage, below), weighted-mean (aggregate L/PS `ΣW_s·L_s/ΣW_s`; National Influence
`clamp(round(Σ(TI·franchise)/Σfranchise),1,7)`), floor-mean (Accord), flat-sum (Treasury; `agg.body/mind/social`
placeholder; CI Piety-Yield `Σ(PT-tier·SW)`), and threshold-count (IP `stepwise 0-1→0…6+→+3`; Turmoil `+1/Accord≤1
territory cap+3`) — plus **4 distribute-down rules**, **~3 decay templates + ~7 time-decay-gap quantities** (§D), and
**2 boundary rules** (§B): **≈ 27 distinct value-transformation rules** in all (11 + 4 + 3 + 7 + 2), the derivation
behind the "~27" headline. Two whole rungs have **no**
aggregation: **faction→national is ruled non-nested** ("factions hold *people*, not territory… no canonical formula,"
`scale_hierarchy_v1 §5.1`; `pressure_key_registry_v1.md:76` DOCTRINE-ONLY), and the **Settlement→Territory→Province
stratum is doctrine-only**, blocked on `engine_clock`. So the primitive doesn't just reconcile existing rungs — it must
*supply* aggregation where the architecture deliberately left holes. (`agg.body/mind/social` are within-actor sums —
correctly *excluded* from the cross-scale story, but they are a *sixth* flat-sum instance the primitive would also
subsume.)

### §B · Escalation is quantize-and-throttle, not weight-preservation — the concrete boundary math

The first draft framed up-escalation as "weighted, then gated." The **actual** magnitude transform at the scale
boundary (`sim/cross_scale/domain_echo.py`, `echo_transport.py`) is a lossy compressor:

1. a scene resolves to a **continuous** outcome (real-valued `net_σ`, or a contest verdict);
2. collapsed to **one of four degree bands** (Overwhelming / Success / Partial / Failure);
3. mapped `{Overwhelming:+2, Success:+1, Partial:0, Failure:−1}` (`domain_echo.py:30-35`);
4. **hard-capped ±2** (`ECHO_STAT_CAP`) and **throttled to 1 echo/faction/scene** (`PP_329_...=1`).

So a duel won by a hair and a duel won overwhelmingly both become `Success → +1`, and **no scene can move a faction
stat by more than 2 of its 7 points, ever**. The system *deliberately de-magnifies* per-scene weight to prevent
scene-dominance (PP-329, "prevents compounding"). The real context-management control at the boundary is
**compression to a ~2-bit token**, and **Sufficient Scope** (§3.4 — priority order *Thread op → Combat victory →
Settlement governance → Disposition reach → Investigation completion → Faction-leader-direct → Other*, cap 1/faction/scene;
verified verbatim) decides *whether* the token crosses, while the degree-table sets its coarse sign+magnitude. Caveats:
this whole path is **INERT in the live campaign** except a synthetic emergency-council contest (`scene_dispatch`
"every scene DEFERS"), and Thread Echo (§5.6) has a *separate* significance gate — so Sufficient Scope is not literally
the only up-gate.

### §C · Collision of stresses — the co-equal SECOND regime (correctly attributed)

Distinct from nested aggregation (one directed flow per boundary), **collision of stresses** is an exogenous shock
acting **top-down AND bottom-up in the same tick**, converging on the intermediate (Territory/Province) tiers. This
is the regime the first draft named and then dropped — and it is developed as **Cut D** of the governance docket
(`governance_grounding_v1.md §Cut D`), *not* in `holonic`/`propagation_spec`. It is realized as **four un-unified
radiation systems with no shared primitive — the real referent of GAP-E1:**

1. **Calamity Radiation** — RS-band × node-distance matrix radiating outward from Askeheim; "southern factions face
   existential threat before northern ones notice" (`designs/world/calamity_radiation_v30.md`). A top-down distance-falloff field.
2. **Mending Stability (MS)** — graduated per-territory by node-distance (d1–d5), with logarithmic recovery +
   **hysteresis** (falling 20/40/60, rising +8) + a 12-MS warning window — "the strongest template in the corpus."
3. **Peninsular Strain / Turmoil** — bottom-up `+1/Accord≤1 territory (cap +3)` that then top-down-forces Accord down
   at Fracture/Crisis/Collapse — itself a collision.
4. **Settlement Pressure Π** — a homeostat `clamp(Π + …unserved-needs/grudges/shocks − releases, 0, 10)` with a
   designed-but-unported restoring term toward Π=3.

GAP-E1 flags these four as un-unified; GAP-E2 adds that a collision is **not even modeled** as requiring two
independent signals (a famine reads as a lone settlement problem, never a material-threshold-AND-interpretive-trigger
event). This is where the D.6 double-count and the deferred `decay()` actually *bite* — up-aggregates and down-deltas
meeting on one node in one Accounting.

### §D · De-escalation and convergence — corrected

The first draft's "accelerator with no brake" was wrong on the evidence. There **is** downward force: an event-driven
`−λ_violation·score` erosion term (though that specific formula, `faction_behavior_v30 §3.5`, is **superseded by
LPS-1**), and the *live* Mandate↔L/PS loop is **mean-reverting, bounded 0–7, and Stage-4-sim-verified convergent over
30 seasons with "no runaway"** (`settlement_layer_v30 §1.8`). The **real** gap is narrower and specific: **no
time-based/entropic `decay()` term** — an explicit deferral to Stratum B+ (`key_echo_armature_v1.md:270`, OF-3) — so
event-*builds* accumulate without a general entropy pull. GAP-E3 further notes an **E11 suspicion-decay counter
already exists in code**, un-systematized as a general dampener. On **convergence**: `propagation_spec_v1 §4` proves
per-tick fixpoint and per-cascade termination but **not cross-tick convergence**, and **proves magnitude is bounded**
— so the open risk is **non-settling bounded oscillation, not amplification** (the first draft's "may amplify" was too
strong), conditional on the D.6 double-count being resolved (`§3 D.6`, HIGH). The `holonic_container_doctrine §4`
"termination/convergence artifact" is the reserved reasoning work.

### §E · Managing context of content — the four mechanisms, and the primitive that already exists

The context-management apparatus: **`scale_signature`** (type-level populated; per-instance `targets[]` sparse — the
§12.3 debt); **`causes[]` provenance** (empty — 0 populated instances; the substrate's own "~15%" is a *simulated
projection*, never met live); **`articulation_layer`** (a wildcard **significance-function**, `§3.2`, that reads the
whole stream but **emits no Key that feeds resolution** — its one design-doc emit `meta.cascade_cluster_event` is
unregistered *and* orphan, and cut-scenes/chronicle/the `awareness` field it writes are narrative rendering, not
resolution inputs — so "context observed, not acted on" holds); and the **temporal apparatus** (`permanence`
transient/persistent/indelible + `time_horizon` feeding salience decay — memory-context decay ships; *value* decay
does not).

**The decisive correction:** the unified primitive the first draft "reserved for fable-tier authorship" **already
exists as a PROPOSED schema** — the **`Field`/`Gauge` primitive** (`governance_type_registry_v1.md §4`):
```yaml
field_id, scale_signature, range,
aggregate_fn: <none | weighted_mean | floor_mean | sum | custom>   # generalizes W_s + 7T/(T+6)
propagate_fn: <none | cascade_with_noise>                          # the distribute-down
decay_fn:    <none | linear | homeostat | hysteresis | custom>     # closes OF-3; MS/Π/Turmoil are templates
derived_flags: [...]
```
with a `sim/substrate/fields.py` companion to `keys.py` sketched, blocked on **one Jordan ruling** (OF-3's `decay()`).
And the **saturation half is already shipping one scale down**: `sim/autoload/sigma_leverage.py` is a live, canonical,
*shared* (combat + contest) **weighted-sum → `tanh` soft-cap (M_MAX=1.5) → scale-invariant** weighting kernel
(`net_boost = eff_σ·σ_per_die·√N`, where σ and √N cancel so an advantage shifts the z-score by exactly `eff_σ` at
*every* pool size). That is structurally the **same** weighted-saturating move as Mandate's `7T/(T+6)` — the doc's
claim that it exists "only for Mandate" was false. **The strongest thesis:** the primitive is not blank-slate future
work — it is a *proposed schema* + a *shipped saturation kernel trapped at the sub-resolution grain*. The work is:
**lift σ-leverage's saturation to the cross-scale grain, populate the `Field` schema over the ~27 rules, rule OF-3's
`decay()`, supply the collision primitive (GAP-E1/E2), and close the cross-tick convergence artifact (D.6).**

---

## The three axes as one picture

- **Axis 1 (objects)** — the engine→module→adapter stack is contract-formalized only for combat and undefined in
  Godot, but a *defined* engine abstraction exists in prose (`engine/` armature); in the sim, **wrapper ≡ adapter**;
  contract↔code identity is a 3/27 black hole.
- **Axis 2 (data)** — closed on input, leaky on output, dispersed-but-partially-cross-checked on location; the
  direction-carrying debt is per-instance `targets[]`, and a vocabulary-unification facade (`registry.py`) already exists.
- **Axis 3 (semantics)** — **two regimes** (nested aggregation + collision of stresses), an escalation that is really
  **compression to a 2-bit token**, ~27 un-unified transformation rules across six postures, a real but *event-only*
  de-escalation (time-decay deferred), an unproven-but-bounded convergence — and a **unified primitive that already
  exists as a proposed `Field` schema plus a shipped σ-leverage saturation kernel**.

The through-line, now sharper: the substrate's topology-neutral elegance pushes all correctness onto **authoring
discipline** (`targets[]`/`causes[]`) and **one value-transformation primitive** — and that primitive is *further
along than the first draft claimed*: proposed as a schema, half-shipped as a kernel, blocked on a single `decay()`
ruling and the convergence proof. Everything else the observatory flagged is a symptom that resolves once those land.
