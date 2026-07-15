# Spec §2 / Q3 — Events Legible as Narrative + the Arc-Register Binding

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
## Date: 2026-07-05 · Lane: IN · Section owner: Q3 (arcs)
## Charter authority: `00_engine_charter.md` Q3 (L81–105) + substrate contract (L137–151) + capstones 8/10/11 (L160–163)

> **Q3. How do we make events legible as a narrative?**
>
> There is no GM. The engine must notice that independent mechanical vectors have converged into a
> story, decide it matters, and hold it as a persistent, queryable object — WITHOUT ever surfacing
> a narratological label (C2, `00_engine_charter.md` L28–30). This section defines the object (the
> typed `arc_vector`), the discriminators (story-vs-context, meaningfulness, emergence-vs-noise),
> the lifecycle machine, the concurrency/salience economy that governs how many arcs live at once,
> the NPC slow/fast split, the one-ledger rule, and the PLOT model — and binds all of it to the
> `references/arcs/` register as a compiled data asset.

This section is the **master Q3 spec** and the **arc-register binding**. It owns layers **L0 COMPILE**,
**L1 STORE+TICK**, and **L2 DETECT** of the synthesis architecture (`synthesis.md` §1); it hands off
scheduling/casting (L3/L4) to the Q1/Q2 sections and rendering (L5) to the Q4 section, flagging the
seams explicitly.

---

## §Q3.0 — The load-bearing move: arc membership, not event type

The charter's first Q3 sentence is the whole thesis: **"arc membership decides, not event type"**
(`00_engine_charter.md` L83). A `mechanical.scene_skipped` Key and a `da.covert_betrayal` Key are not
sorted into "story" vs "noise" by their *type*; they are sorted by **whether a live arc-vector has
declared them a lifecycle input**. This inverts the naive design (classify Keys, then assemble arcs)
into the correct one (compile arcs first, then let each arc's own `trigger.predicate` /
`pressure_effects[].condition` decide which Keys it consumes). The register already has this shape —
every entry is `trigger condition(s) → mechanical effects → closing "Direction:" sentence`
(`01_arc_corpus.md` §a) — so the binding is a *compilation*, not an authoring project.

Consequence for the three discriminators below: they are **not three independent classifiers**. They
are three *questions asked of an already-instantiated arc-vector*:

1. **Story-vs-context** (§Q3.1): is this Key inside any live arc's declared I/O?
2. **Meaningfulness** (§Q3.1): does the Key move a slow variable for a tie-graph actor?
3. **Emergence-vs-noise** (§Q3.2): do two arcs' states correlate enough to constitute a *new* arc
   (a convergence) rather than coincidence?

---

## §Q3.1 — Story-vs-context threshold + the meaningfulness test

### The threshold (binary, structural)

A touched Key is **STORY** iff it appears in the resolved I/O of at least one live `arc_vector` —
either matched by a `trigger.predicate` field, named in a `pressure_effects[].condition`, or written
by a `pressure_effects[].target`. Otherwise it is **CONTEXT**. This is a set-membership test over the
live arc-vector store (L1), evaluated per Key at settle time. It is C2-clean by construction: the
STORY/CONTEXT bit is engine-internal and never surfaces (`00_engine_charter.md` L28–30) — the player
sees the *scene* an arc books, never the classification.

This threshold satisfies **capstone #8** ("meaningfulness test passing one beat and failing one context
event", `00_engine_charter.md` L160): a Key matched by ARC-S07's `Loyalty ≤ 3` predicate is STORY; a
routine `env.population_change` with no live arc consumer is CONTEXT and is EXPLICITLY DISCARDED with
reason `no_live_arc_consumer` (total accounting, `00_engine_charter.md` L143–145).

### The meaningfulness test (graded, orthogonal to stakes-loudness)

STORY-membership answers *"is this in an arc"*; the charter demands a *second, orthogonal* filter that
answers *"does this arc-beat matter"* — explicitly **orthogonal to §3.2 stakes-loudness**
(`00_engine_charter.md` L83–86). A loud, high-`stakes_weight` battle can be narratively inert (nothing
about anyone changed); a quiet Loyalty tick can be the hinge of a dynasty. The test generalizes
`articulation_layer_v30.md` §3.2 `significance` from a loudness scalar into a three-factor identity
product:

```
meaningfulness(key, arc) =
    durability(key)        # moves a SLOW variable (Belief / Conviction / Scar / Coherence /
                           #   Resonant Style / voice register) — §Q3.6 slow set. Binary-ish 0|1|2.
  × tie_proximity(key,arc) # tie-graph distance from the touched actor to a
                           #   payload.participating_actor (0 = is one; grows with hops)
  × identity_touch(key)    # changes WHO someone is / what they OWE / what is POSSIBLE
                           #   (Belief/Conviction/Scar/Coherence · Obligation/Standing/Knot ·
                           #    gate/foreclosure) — the charter's three identity clauses (L84–86)
```

**Determinism ruling (applies adversarial MAJOR "float-product boundary nondeterminism").** This is a
product of factors with a downstream threshold; a naive float product plus `>` comparison is
replay-fragile (float summation is non-associative — `propagation_spec_v1.md` O.3 ORD-2 territory) and
diverges Python↔GDScript at the last ULP (the ED-1050 `adef_threshold` port-divergence class, CLAUDE.md
§6). Therefore each factor is quantized to a **small integer grid** (`durability ∈ {0,1,2}`,
`tie_proximity` as an integer hop-distance mapped to `{0,1,2,3}`, `identity_touch ∈ {0,1,2,3}`), the
product is computed in **integer arithmetic**, and the promotion comparison is an **integer** compare
against an `[OPEN — Jordan tuning]` cutoff. `tie_proximity`'s graph distance is made deterministic by
BFS over an insertion-ordered adjacency (ORD-1) with `actor_id` ascending as the total-order tiebreak.
The *cutoff value* is calibration (`[OPEN — Jordan tuning]`); the *integer-arithmetic determinism* is
structure and is ruled here regardless.

Meaningfulness is the **budget filter the scheduler (L3) applies** — not a hard gate on arc existence.
A below-cutoff beat is not deleted; it is **backgrounded** (routed to Tier-1 texture, re-promotable via
the §Q3.5 accumulator) — never silently dropped (`00_engine_charter.md` L86, "noise explicitly
backgrounded, never silently dropped").

---

## §Q3.2 — Emergence-vs-noise: correlation tests + the discard path

"Emergence" here has a precise meaning: **two or more independent arc-vectors whose states have
converged into pressure qualitatively different from either alone** — the register's own definition of
a Convergence Marker, "named because the combined pressure is not predictable from the constituent
vectors" (`arc_register_events.md` §VI L25). The detector (L2) must discriminate a real convergence
from coincidental co-timing. This is a **two-tier detector**, both tiers mandatory (`synthesis.md` §3).

### Tier A — the 8 hand-authored COLLISION conjunctions (authoritative, effect-bearing)

`arc_register_events.md` §VI defines 8 named Convergence Markers (COLLISION A, B, C, D, E, F, G, J — no
H/I). Each compiles to a typed `convergence` arc_vector whose `trigger.predicate` references *other*
vectors' `lifecycle.state` and their shared `targets[]`, and whose `pressure_effects[]` carry the
**authored combined deltas** (e.g. COLLISION-C: `RS +8, IP +2, TC +2` in one season,
`arc_register_events.md` L39). These are the register's four correlation dimensions made concrete
(`00_engine_charter.md` L86–89): **shared `targets[]`**, **`causes[]` overlap**, **temporal window**,
**same-direction pressure on a shared stake**.

Evaluated **edge-triggered-once over SETTLED state at the ACCOUNTING_BOUNDARY** — deliberately, to
sidestep ORD-3 mid-cascade nondeterminism (`propagation_spec_v1.md` O.6; the detector reads a settled
snapshot, never mid-drain). Every marker that does *not* fire in a given Accounting is EXPLICITLY
DISCARDED with reason `predicate_false` and logged (total accounting).

**Determinism ruling — the dedup container (applies adversarial MAJOR "convergence_fired_set is a live
ORD-2 violation").** The synthesis names a `convergence_fired_set` for once-only dedup. A bare `set()`
gating emission order is exactly the ORD-2 violation `propagation_spec_v1.md` O.3 forbids and O.6 exists
to correct — set-iteration order is hash-seed-dependent, so `sub_step_index` (SSI-1) would differ →
different `KEY_LOG` → V4 replay fails (`propagation_spec_v1.md` O.8). The "sidesteps ORD-3" claim covers
only the *read* side (settled snapshot); it does **not** absolve the detector's own *emit* order.
Ruling: dedup uses an **order-preserving container keyed by a total order** —
`(conjunction_id, sorted(participating_actor_ids), season_index)` — and detected convergences are
**sorted by that key before the emit loop**. Conformance rule **CR-1** (§Q3.9) asserts no `set()` gates
convergence emission order.

### Tier B — the general cosine-similarity backbone (buildable generality, RENDER-ONLY effect)

The 8 conjunctions are a whitelist; the charter demands *general* correlation-test discrimination, not
a hardcoded 8 (holonic scripting-drift hazard, `holonic_container_doctrine_v1` per C5). The backbone
generalizes `articulation_layer_v30.md` §3.1 **trigger-9**: cosine similarity of
`cascade_fidelity_history[-4:]` over a 4-season window, threshold `abs(sim) > 0.40`, sim-validated at
`corr +0.937` on the Crown/Hafenmark pair (`articulation_layer_v30.md` L94–112). We lift it from
*faction pairs* to **arc-vector pairs**, supplying the `temporal_window` the COLLISION conjunctions
never specify register-wide (`dossier_register_formalizability` §6 open-Q6).

**Determinism ruling (applies adversarial MAJOR "±0.40 boundary + cross-oracle divergence").** `abs(sim)
> 0.40` is a float comparison at a boundary; generalizing from ~5-faction pairs to ~110 arc-vectors is
O(N²) boundary coin-flips, and the `+0.937` validation was one pair over 30 seasons — NOT the arc-pair
regime. Ruling: the cosine numerator/denominator are computed in a **canonical summation order** (terms
sorted by `actor_id`), the result is **quantized to a fixed integer grid** before comparison, an
**epsilon-band with a conservative-tie rule** (ties resolve to *not-fired*) is published, and the
identical fixed-point arithmetic is **pinned in the GDScript port and added to the key-log parity
harness** (same discipline that resolved ED-1050, CLAUDE.md §6). `0.40` and the window length are
`[OPEN — Jordan tuning]`; the arithmetic determinism is structure.

**Effect ruling — the convergence-EFFECT seam (applies adversarial MAJOR "convergence-effect invites
fabrication").** A register COLLISION's combined pressure is an *authored* quantity, "not predictable
from the constituent vectors" (`arc_register_events.md` L25). Therefore a cosine-detected convergence
that is **NOT** one of the 8 register-authored markers has **`pressure_effects[] = []` — it is
RENDER/CHRONICLE-ONLY.** It may raise a `meta.convergence_detected` Key for the `causes[]` walk and for
Tier-2/3 rendering, but it applies **zero mechanical delta**. Mechanical combined-pressure exists ONLY
for register-authored convergence vectors. Conformance rule **CR-2** (§Q3.9): any `convergence`
arc_vector with non-empty `pressure_effects[]` must trace **each delta to a register line**
(`arc_register_events.md` §VI); a cosine-detected vector failing this trace is compiled effect-free.
This closes the fabrication hazard (CLAUDE.md §5/§7, leaky anti-fabrication gate) without collapsing
back to a hardcoded-8 (Tier B still *detects* and *renders* the long tail).

### The discard path (false positives cost trust)

"False positives cost player trust" (`00_engine_charter.md` L89). Every detector evaluation resolves to
exactly one of: **FIRED** (register marker, effect-bearing) · **DETECTED-RENDER-ONLY** (cosine, zero
effect) · **DISCARDED** (`predicate_false` / `below_meaningfulness` / `window_expired`, logged with
reason). Nothing is silently dropped; the discard reason is queryable in the chronicle backend but never
surfaces as a label (C2).

---

## §Q3.3 — Arc taxonomy + lifecycle state machine

### Taxonomy (major / medium / minor by measurable properties)

Tier is **computed at compile from measurable vector properties**, never hand-tagged for drama
(`00_engine_charter.md` L89–92). The five measurable axes:

| Axis | Source | Contributes |
|---|---|---|
| scale span | `scope.territories` count + ladder rungs traversed (`00_engine_charter.md` L69–70) | breadth |
| stakes weight | max `pressure_effects[].delta` magnitude, `articulation §3.2` stakes(1–5) | intensity |
| duration | `activity_mode` (a `clock_escalation` vector persists; `edge_triggered_once` does not) | persistence |
| vector count | `cross_refs[]` cardinality (a convergence-eligible hub scores high) | connectivity |
| protagonist alignment | tie-graph distance from PC to `payload.participating_actors` | proximity |

`tier_rank ∈ {major, medium, minor}` is a deterministic integer bucketing of the weighted axes
(`[OPEN — Jordan tuning]` weights; the *bucketing determinism* is structure — integer thresholds, ties
break to the lower tier). `tier_rank` is a load-bearing input to the L3 rationing total order (§Q3.5)
and to the concurrency budget (§Q3.4).

### Lifecycle state machine (persistent, queryable)

Every non-`level_triggered` arc_vector carries a `lifecycle.state` FSM (`00_engine_charter.md` L92):

```
seeded ──trigger.predicate true──▶ active ──escalation condition──▶ escalating
                                     │                                  │
                                     │                          converging (feeds a COLLISION)
                                     │                                  │
                                     ▼                                  ▼
                                  dormant ◀──re-promotable──  resolved | abandoned  (terminal)
```

- **seeded** — compiled and instantiated, `trigger.predicate` not yet true.
- **active** — predicate satisfied; consuming Keys; emitting `pressure_effects[]`.
- **escalating** — an escalation guard crossed (e.g. ARC-S07 `Loyalty` falling, §Q3.10).
- **converging** — this vector is now a constituent of a live COLLISION conjunction (Tier A).
- **resolved / abandoned** — terminal (`terminal: true`).
- **dormant** — deactivated but **re-promotable** (background's dignity, §Q3.5) — NOT deleted.

`level_triggered` vectors (most `TE-##`, `dossier_register_formalizability` §2) have **no lifecycle**:
active-while-condition-holds, `terminal: false`, no FSM. This is the honest distinction the register
already draws (`arc_register_territory.md`: "active while trigger holds", `01_arc_corpus.md` §a).

**Ownership + closes ED-IN-0003.** The generalized `lifecycle.state` field is the **concrete, buildable
form of ED-IN-0003** (`dossier_register_formalizability` §4 finding 1; audit F-2). Today only
`module_contracts.yaml:150` (`{name: "arc state", bucket: clock}`) exists and it is **scoped to
`npc_behavior` only** (the T-23 mechanism, `01_arc_corpus.md` §d). The ~100 faction/clock/territory/
collision vectors have no equivalent, which is *exactly* what blocks COLLISION detection. **`game_director`
owns the generalized store; the NPC-scoped bucket becomes a specialization it reads** (fork 5, §Q3.11).

**Engagement-window divergence (applies adversarial MAJOR "windows matter once, guaranteed never").**
Capstone anti-railroad requires *a different choice at each engagement window measurably changes
trajectory* (`00_engine_charter.md` L54). A single existence-proof is not a guarantee: an FSM whose
win/lose branches share a successor state is a railroad, uncaught. Conformance rule **CR-3** (§Q3.9):
every `edge_triggered_retryable` or `convergence` vector with the PC in `participating_actors` must
expose **≥2 participated-outcome classes mapping to ≥2 distinct next `lifecycle.state`** (or ≥2 distinct
`pressure_effects` sets). A window whose outcomes collapse to one successor is flagged **illusory-choice
at compile** — a build error, not a runtime surprise.

**Reconciling CR-3 with the arc-generator emergence standard.** CR-3 (a participated window *must*
change the arc's trajectory) sits against the arc-generator's hard rule that *"no single player decision
caused this; it required multiple independent systems running simultaneously"*
(`skills/valoria-arc-generator/SKILL.md:74`). These are not in tension once the player's role is stated
precisely: **the player *selects among* already-emergent branches, and *accelerates or defers* an arc —
the player never *authors* the arc.** An arc-vector exists, is seeded, and ticks because multiple
independent vectors converged (the emergence standard); the participated outcome at an engagement window
picks *which* pre-authored successor `lifecycle.state` the FSM steps to (CR-3), and can advance or delay
its clock — but it cannot conjure a vector, invent a branch the register did not author, or make the arc
about the player alone. The **±2/season stat cap** (`skills/valoria-arc-generator/SKILL.md:80`) and
**multi-vector causation** both still hold: a single choice bounded at ±2/season and selecting among
authored branches cannot *be* the arc's sole cause. So CR-3 guarantees the choice *matters* without
demoting the arc to a plot hook — exactly the arc-generator's "plot hook vs emergent arc" line.

**Foreclosure-via-clock ban (applies adversarial MAJOR "foreclosure fires silently via passive
threshold").** `activity_mode` includes `clock_escalation` / `level_triggered` with ±2/season deltas; a
passive clock crossing a foreclosure threshold with *no arc event* violates the charter's "foreclosure
only via arc events, never silent" (`00_engine_charter.md` L41, L77–78). Two rules: **(a)**
`stakes_tags:[foreclosure]` transitions may originate ONLY from `edge_triggered_once` /
`edge_triggered_retryable` / `convergence` — never from `clock_escalation` / `level_triggered`; a
foreclosing clock crossing must first raise an **edge-triggered arc event**. **(b)** every foreclosure
transition MUST emit a **Tier-3 chronicle beat** — a *positive* surfacing check (CR-4, §Q3.9), distinct
from discard-with-reason logging. Total-accounting (CONSUMED-INTO-STATE) is engine-internal and does NOT
satisfy "never silent"; the mandatory chronicle render does.

---

## §Q3.4 — Coherence as A narrative: concurrency, braiding, causes[]-raising

The charter's Q3 heading "Coherence as A narrative" (`00_engine_charter.md` L93–94) — coherence in the
literary sense, a *coherent* story, not the threadwork Coherence stat — asks that many simultaneous arcs
read as one braided narrative rather than a spreadsheet.

- **Concurrency budget per tier.** A season admits a bounded count of *foreground* arcs per `tier_rank`
  (`[OPEN — Jordan tuning]` caps). The budget is a CEILING (C7, §Q3.5), enforced by L3 rationing; arcs
  over budget are demoted to background (dormant/texture), not deleted.
- **Protagonist-frame braiding.** Concurrent foreground arcs are braided by shared
  `payload.participating_actors` and shared `targets[]` — the same edges the detector reads. Two arcs
  touching the same NPC render as *that NPC's converging pressures*, not two rows.
- **causes[] continuity — the load-bearing rate.** The charter flags "raising the ~15% population rate
  is load-bearing" (`00_engine_charter.md` L94; the substrate-alone story-fraction is ~15%,
  `articulation_layer_v30.md` §10 "substrate alone produces ~15%", PP-688 raising the full-engine
  estimate to ~75–85%). Every outcome Key re-enters the originating arc's `causes[]` chain (Q1
  participation loop, `00_engine_charter.md` L45); a populated `causes[]` is what makes the backward
  chronicle walk (§Q3.7) legible as story. **CR-5** (§Q3.9): every arc-emitted outcome Key has
  `causes[]` populated (no orphan beats).
- **Chronicle callbacks.** Terminal arcs leave a searchable Tier-3 record; later arcs referencing a
  resolved arc's actors render a callback ("as with the Klapp fracture two winters past") sourced from
  the `causes[]` walk — telling reserved for retrospect (Q4 showing-vs-telling, `00_engine_charter.md`
  L124).

---

## §Q3.5 — Salience economy

The salience economy governs *which* live arcs occupy the scarce foreground, with a re-promotion path so
backgrounded arcs keep their dignity (`00_engine_charter.md` L96).

- **Foreground budget.** L3 rations arcs into `player_agency §4.3`'s 3–5 scene-action envelope
  (`00_engine_charter.md` L128). This is a **CEILING, not a floor** (C7) — the director may only
  SUBTRACT (ration/demote), never INSERT (see §Q3.7 director ruling).
- **Promotion / demotion + background re-promotability.** Generalizes `articulation_layer_v30.md` §3.3
  per-actor `unarticulated_weight` starvation accumulator from actors to **arcs**: a backgrounded arc
  accumulates weight as its Keys go un-surfaced; eventually a routine Key promotes it back to foreground
  (background is re-promotable, never terminal — dormant ≠ dead).

**Total-order tiebreak (applies adversarial MAJOR "Top-N rationing has no tiebreak").** Rationing is a
Top-N selection over ~110 arcs with integer salience scores → marginal-slot ties are the *common* case;
an unstable sort or dict/set-seeded selection yields nondeterministic `scene.*` emission → V4 fails, and
this sits on the C7 CEILING selection where a total order is mandatory. **CR-6** (§Q3.9): every
rationing / Top-N selection sorts by the **total order `(salience DESC, tier_rank, arc_vector.id ASC)`**
— `id` is unique so the order is total; unstable sort and set/dict-seeded selection are forbidden. The
same rule extends to `§4.3` chronicle Top-N and `§3.3` notable-individuals Top-N.

**Player-participated demotion exemption (applies adversarial MAJOR "salience demotion railroads away
from player-pursued arcs").** A ceiling still *chooses which* arcs fill the slots; without protection, an
arc the player is actively chasing can be demoted to rumor = soft railroad. Rule: **any arc with a PC
participated-outcome in its `causes[]` within the last K seasons (`[OPEN — Jordan tuning]` K) is
demotion-exempt** — floored at foreground until it resolves or converges. Demotion may touch only
player-untouched arcs. "CEILING not floor" governs *how many*; this governs *which*.

**C2 containment (absolute).** The salience ledger, tension state, and lifecycle labels **NEVER surface**
(`00_engine_charter.md` L28–30). A C2 literal-string lint (CR-7, §Q3.9) applies to **ALL
arc-lifecycle/salience state, not only baked fragments**. Demotion manifests only diegetically — a
summons becomes a rumor; the player never sees "demoted" or "salience −2".

---

## §Q3.6 — Recognizable-yet-dynamic NPCs: slow vs fast variables

NPCs must read as the same person across seasons yet still change (`00_engine_charter.md` L96–98). The
split is a **variable-cadence contract**, enforced by *which* mutations an arc-vector is permitted to
write:

| Class | Variables | Cadence | Who may write |
|---|---|---|---|
| **SLOW** | Convictions (core), Resonant Styles, voice register / Certainty band | **arc-grade only** | only a `durability ≥ 1` arc transition (§Q3.1) |
| **FAST** | opinions, concerns, projects, standing shifts | **every season** | routine Keys, `npc_behavior §5` concern/project engine |

The slow set is exactly the meaningfulness `durability` set (§Q3.1) — a change to a slow variable is what
makes a beat *durable*. The rule prevents both spreadsheet-churn (an NPC's Conviction flipping every
season) and statue-stasis (an NPC who never changes). **CR-8** (§Q3.9): a slow-variable write must carry
an arc `ledger_cause` — no unattributed identity change.

**Per-NPC lexicon overlays — bake-cost caveat (BLOCKER 2 + adversarial MAJOR "per-NPC voice budgeted at
the name-swap floor").** The charter forbids the name-swap level: "two Bonded NPCs … must not read as the
same template with a name swapped in" (`00_engine_charter.md` Q3, recognizable-yet-dynamic). The
content-economics dossier's per-NPC figure (~100–175 units = 3–5 micro-units × 35 Active NPCs,
`dossier_content_economics` §2.2) is a **FLOOR, not a ceiling**: genuine idiolect-differentiated NPCs
needing variants across the ~10 triggers that fire for them is `35 × 10 × (a few variants)` ≈ **1,050
units** — *exceeding the whole 350–450 headline* (`dossier_content_economics` §3 item 1: "bounded in
cardinality (good), NOT bounded in per-unit authoring cost (open risk)"). **Ruling for the bake plan
(Q4 lane owns the number):** per-NPC voice is a **distinct bake line item** whose top end reflects
`35 × triggers-per-NPC × variants`, not `3–5 × 35`; Q3 recognizable-yet-dynamic is an *authoring-craft*
cost the combinatoric factoring does **not** certify, and "feasible" is conditional on budgeting it
(`dossier_content_economics` §5 item 3). This is carried into the render-binding caveat (§Q3.8).

---

## §Q3.7 — One ledger + the PLOT model

### One ledger (no new currency)

Progression **IS** narrative state (`00_engine_charter.md` L99–100; C5 "no new progression currency",
L37). The arc-vector store does **not** introduce a parallel currency: an arc's I/O *are* the existing
progression tracks (clocks, stats, npc_tracks, Obligations, Standing, Scars, Beliefs). NPCs progress
through the **same arcs** — they are co-protagonists, cast by the same tie-graph rule that casts the PC
(Q2, `00_engine_charter.md` L61). Ethics is pattern, not points: Convictions are the ethics ledger,
`npc_memory` + Standing + Cascade read accumulated behavior, and there is **no hidden morality meter**
(P-04, `00_engine_charter.md` L52).

### PLOT — forwards as pressure, backwards as story (under the doc-12 veto)

The charter's PLOT clause: *experienced forwards as pressure and choices, recognized backwards as story*
(`00_engine_charter.md` L100–105). The four moments map to engine mechanisms:

| Plot moment | Mechanism | Surfacing |
|---|---|---|
| **setup** | `scenario_authoring` campaign-skeleton seed Keys (PP-690 realized) + arc seeding (L0) | diegetic scene / world state |
| **escalation / turn** | `lifecycle` transitions + convergence detections (L1/L2) | **INTERNAL** (C2) — felt as pressure/choices, never labeled |
| **resolution** | terminal transition, punctuation | rendered diegetically (a scene, a chronicle beat) |
| **retrospect** | chronicle + `causes[]` walk (backward, §Q3.4) | Tier-3, searchable |

**Director = stateless surfacing ceiling ONLY — no tension curve (applies TWO adversarial MAJORs: "real-
time tension curve un-reconciled with the no-designed-dramatic-timing NOT-list" + "director owns tension
curve graduates a DEFERRED contentless spec").** The synthesis (and charter L128–129) speak of the
director "owning the tension curve" by graduating `articulation §7 D11`. But `articulation_layer_v30.md`
§7 **explicitly DEFERS pacing** ("the articulation layer as specified does not enforce pacing; cut scenes
fire whenever triggers match") and §10 lists **D11 = Deferred** — there is no spec to graduate, and
`doc-10 §8.5`'s NOT-list ("no designed dramatic timing") stands (`00_engine_charter.md` L104–105).
Shaping *when* beats fire toward a rising-action target is itself the over-orchestration C7 forbids, and
C2-non-surfacing answers *surfacing*, not *behavior*. **Ruling: drop tension-curve ownership entirely.**
The director is a **stateless budget CEILING**: it may RATION which already-emerged beats surface
(subtract/demote, §Q3.5) and NOTHING ELSE. It may **never manufacture, insert, reorder, delay, or
time-compress** an underlying event to shape a curve. **Event timing stays fully emergent** (preserving
`doc-10 §8.5`). CR-9 (§Q3.9): the director may only SUBTRACT (ration/demote), never INSERT or advance
timing.

### The CAN / CANNOT plot-shape list

Stating what this plot machine CAN and CANNOT produce is a charter requirement (`00_engine_charter.md`
L104–105, "doc-10 §8.5 NOT-list stands").

**CAN produce:**
- **Convergence-driven crises** — the 8 register COLLISIONs and their qualitatively-new combined
  pressure (`arc_register_events.md` §VI).
- **Escalating clock-arcs** — `clock_escalation` vectors like ARC-S07 that ramp over seasons.
- **Reversal / turn** — a participated outcome flipping an FSM branch (ARC-S07 `floor 6` recovery vs
  `Loyalty 0` elimination-branch to ARC-T13).
- **Braided multi-actor arcs** — shared-`participating_actors` concurrency (§Q3.4).
- **Foreclosure of futures** — permanent closes via arc events, surfaced in chronicle (§Q3.3).
- **Emergent thematic clusters** — cosine-detected alignment/opposition, RENDER-ONLY (Tier B, §Q3.2).
- **Retrospective recognition** — the `causes[]` walk reconstructing a story after the fact.

**CANNOT produce (doc-10 §8.5 NOT-list stands):**
- **No designed dramatic timing** — the engine cannot delay/advance an event to hit a beat-sheet; timing
  is emergent (director-subtract-only ruling above).
- **No authored three-act guarantee** — no promise that any season resolves to a satisfying arc shape;
  arcs may fizzle to `dormant` or `abandoned`.
- **No manufactured antagonist / rising action** — no injecting a conflict that the mechanical substrate
  did not produce (holonic anti-scripting, C5).
- **No narratological surfacing** — the player is never told "this is the climax" (C2).
- **No GM-judgment arcs until authored** — the ~15% GM-judgment-irreducible arcs (ARC-P05, ARC-S29)
  are declared non-firing in `gaps[]` until a decision function is authored (fork 7, §Q3.11); the engine
  will NOT improvise their selection logic.
- **No guaranteed novelty** — the arc space is the compiled register; the engine cannot author a story
  outside its ~110 vectors + their convergences.
- **No single-character heroic arc** (doc-10 §8.5 NOT-list) — the engine does not center a lone
  protagonist as the causal engine of the world; arcs are multi-vector and multi-actor by construction
  (the arc-generator emergence standard, `skills/valoria-arc-generator/SKILL.md:74`, "no single player
  decision caused this"), and NPCs are co-protagonists on the same ledger (§Q3.7), never a supporting cast.
- **No authored mystery / reveal arc** (doc-10 §8.5 NOT-list) — the engine does not withhold a
  pre-authored secret to be "revealed" on a beat-sheet; what looks like a mystery is the `causes[]` walk
  read *backwards* (§Q3.7 PLOT retrospect), assembled from mechanical provenance, not a scripted
  concealment with a planted payoff.
- **No failure-of-the-world model** (doc-10 §8.5 NOT-list) — there is no global "lose state" or authored
  apocalypse the engine steers toward; the world persists and re-scopes (arcs fizzle to `dormant` /
  `abandoned`, factions collapse into new pressure vectors, e.g. ARC-T13), and consequences are local
  and mechanical, never a designed game-over curve.

---

## §Q3.8 — The typed `arc_vector` schema (L0 compile output)

The register compiles to a **frozen typed corpus** — this IS the typed engine-params asset CLAUDE.md §5
demands, and it exports directly to Godot (`synthesis.md` §2; C1-clean frozen asset). Schema (from
`dossier_register_formalizability` §2, reconciled with `synthesis.md` §2):

```yaml
arc_vector:
  id: string                          # ARC-S07 | TE-01 | BG-CV-01 | COLLISION-C | NPC-ARC-STR
  tier: enum[S, T, P, TE, BG-CV, COLLISION, NPC-ARC]         # 01_arc_corpus.md §a ID scheme
  tier_rank: enum[major, medium, minor]                      # COMPUTED (§Q3.3), not authored
  scope: { faction: [id]|ALL, territories: [id]|ALL, mode: enum[TTRPG,BG,ALL,Hybrid] }
  activity_mode: enum[level_triggered, edge_triggered_once, edge_triggered_retryable,
                      clock_escalation, convergence]
  trigger:
    predicate: [ { field: <clock|stat|npc_track|arc_state>.<path>,
                   op: enum[">=","<=","==","flip","consecutive_seasons_true",
                            "count_true_of_n","AND","OR"],
                   value: number|enum|ref-to-arc_vector.id } ]
    resolves_via: enum[dice_pool, deterministic_accounting, state_reader, manifest, null]
    temporal_window: enum[same_season, same_accounting, within_n_seasons, unspecified]  # fork 3
  pressure_effects: [ { target: <clock|stat|npc_track>.<path>,
                        delta: signed_number|formula_string,      # ±2/season cap (arc-generator rule)
                        cadence: enum[season, immediate, per_attempt, one_time],
                        condition: optional_guard } ]
  payload:                              # INTERNAL per C2 — never renders as a label
    direction: string                   # the register's "Direction:" sentence, verbatim — realizer slot source
    participating_actors: [actor_id]    # the casting set (Q2 tie-graph intersection)
    stakes_tags: [enum: gating, pricing, foreclosure, pattern_response, none]
    ledger_cause: [PP-NNN | ED-NNN]     # Q2: every gate cites its ledger cause (CI-checkable)
  lifecycle:
    state: enum[seeded, active, escalating, converging, resolved, dormant, abandoned]  # §Q3.3 FSM
    terminal: bool                      # false for level_triggered (active/inactive only)
  cross_refs: [arc_vector.id]           # convergence-eligibility surface
  gaps: [ { type: enum[missing_clock, missing_field, missing_mechanic, struck_mechanic,
                       gm_judgment, open_number, dangling_id, stale_citation],
            note: string, cites: [file:section] } ]                # the honesty ledger
```

**Compile reality (`dossier_register_formalizability` §3).** ~**45%** compile now (post trivial TC→CI /
RS→MS alias resolution, `clock_registry_v30.md` lines 16–17, ED-731/ED-782); ~**40%** need one buildable
field — chiefly the generalized `lifecycle.state` (ED-IN-0003, §Q3.3); ~**15%** are GM-judgment-irreducible
(ARC-P05, ARC-S29) → declared **non-firing in `gaps[]`** (honesty ledger, fork 7). Territory vectors are
the cleanest tier (~85–90% checkable); clock vectors the worst (2/7 clean). Three corpus defects block
specific vectors and are Jordan forks: **Coup Counter** STRUCK-and-unmigrated (fork 1), **ARC-T04**
dangling (fork 2), plus **Axis 9 Pressure** (ARC-P04) with no clock home
(`dossier_register_formalizability` §4 finding 4 — an open-number gap, not a structural blocker).

**Gating-vs-pricing enforcement (applies adversarial MAJOR "pricing-preferred is an unenforced tag").**
C7 prefers pricing over gating (`00_engine_charter.md` L41, L76), but `stakes_tags` is a bare enum carried
through compile untouched — an all-gating corpus would pass every check. **CR-10** (§Q3.9): compile emits
a **gating:pricing ratio report**, and every `stakes_tags:[gating]` vector must carry a `gaps[]` /
justification note stating **why pricing is infeasible** — making gating the *audited exception* the
charter's "preferred" intends, not a silent default.

### Render binding + anti-oatmeal (the honest bake caveat)

The compiled corpus feeds the L5 realizer (Q4 lane): `payload.direction` is the realizer's slot source,
and two seeds diverge in named actors / stakes / outcomes because the vectors are **data**
(`synthesis.md` §6). **BLOCKER 2 ruling — anti-oatmeal is NOT structural by construction.** Vector-as-data
guarantees only **slot-filler divergence** (proper-noun / stakes / outcome slots differ); it does **not**
guarantee the *rendered prose reads differently* — same fragment cell + a name swap = Compton oatmeal
(`dossier_content_economics` §3 item 2: data-substitution is "good enough for a mechanical register, not
obviously good enough for player-facing prose without additional arc-specific authored color"). Charter Q4
anti-oatmeal item 3 requires a **5-seed prose-distinctiveness regression** (fixed seeds 42/77/99/137/201,
`01_arc_corpus.md` §a) certified by **Expressive Range Analysis** — and ERA is **UNBUILT**
(`dossier_nlg_graduation` §4 step 5 / §6 item 7). **Ruling: prose distinctiveness must be certified by an
ERA bake gate over the 5 fixed seeds; building ERA is a Stage-5 blocker; arc-specific authored color
beyond name-substitution is a distinct bake line item.** The "by construction" capstone-satisfaction claim
is withdrawn; the synthesis's weaker two-seed *data*-divergence is real but is a necessary, not
sufficient, condition.

**BLOCKER 1 ruling — bake volume headline must state both fork-6 resolutions.** The ~350–450-authored-units
figure (`dossier_content_economics` §2.2) is computed **WITHOUT Certainty as a frozen-pool axis**. But the
synthesis's own **fork 6 DEFAULT is to include Certainty** (charter Q4 authority), and gating the frozen
pool on Certainty **multiplies by ~5–6×, pushing the estimate into the low-thousands**
(`dossier_content_economics` §3 item 3 / §5 item 2). **Ruling: ~350–450 holds ONLY if Certainty is a
runtime lexicon-swap (fork-6 fallback); under the DEFAULT (Certainty in the frozen pool) the honest bake
is low-thousands.** The dossier's verdict is CONDITIONAL-feasible ("only if two open items get closed"),
not unconditionally "feasible". This section carries **low-thousands** as the headline under the stated
default; 350–450 is the *conditional* figure, achievable only by flipping fork 6 to lexicon-swap. See
fork 6, §Q3.11.

---

## §Q3.9 — Conformance rules (each lives once in `tools/`, per substrate contract L150–151)

| # | Rule | Guards |
|---|---|---|
| CR-1 | **convergence-dedup-ordered** — no `set()` gates convergence emission; dedup keyed by `(conjunction_id, sorted(actor_ids), season_index)`, sorted before emit | ORD-2 (`propagation_spec_v1.md` O.3), V4 replay |
| CR-2 | **convergence-effect-traces-register** — any `convergence` vector with `pressure_effects[]` traces each delta to an `arc_register_events.md §VI` line; else compiled effect-free | anti-fabrication (CLAUDE.md §5/§7) |
| CR-3 | **engagement-window-divergence** — PC-participating retryable/convergence vectors expose ≥2 outcome classes → ≥2 distinct next states; else flag illusory-choice at compile | C7 anti-railroad (L54) |
| CR-4 | **foreclosure-surfaces** — every `stakes_tags:[foreclosure]` transition originates from an edge/convergence event AND emits a Tier-3 chronicle beat | C7 (L41, L77) |
| CR-5 | **causes-populated** — every arc-emitted outcome Key has non-empty `causes[]` | total accounting (L143), Q3 backward walk |
| CR-6 | **rationing-total-order** — every Top-N selection sorts by `(salience DESC, tier_rank, id ASC)`; no unstable/set-seeded sort | V4 replay, C7 CEILING |
| CR-7 | **C2-literal-string-lint** — on ALL arc-lifecycle/salience state + baked fragments; no narratological label surfaces | C2 (L28–30) |
| CR-8 | **slow-write-attributed** — every slow-variable write carries an arc `ledger_cause` | §Q3.6, no unattributed identity change |
| CR-9 | **director-subtract-only** — the director may ration/demote, never insert/advance/re-time a beat | C7, doc-10 §8.5 NOT-list |
| CR-10 | **gating-priced-or-justified** — compile emits gating:pricing ratio; every `[gating]` vector carries a why-not-pricing note | C7 (L76) |
| CR-11 | **meaningfulness-integer-arithmetic** — meaningfulness + cosine thresholds computed in fixed-point/integer; identical arithmetic pinned in the GDScript port + key-log parity harness | V4, ED-1050 port-parity class |
| CR-12 | **consumer-closure** — every emitted Key (incl. `meta.convergence_detected`, `meta.arc_state_changed`) names ≥1 declaring consumer | substrate contract (L145–146) |

**Harmonization with s4's `R1–R10` conformance scheme (stated once).** s4 (`s4_substrate.md §S4.9`) is
the connective home for the CI rule set and numbers them `R1–R10`; this section's `CR-N` labels map onto
it as follows (where a `CR` has no single s4 `R`, s4 folds it into another rule):

| this file | s4 rule | this file | s4 rule |
|---|---|---|---|
| CR-1 convergence-dedup-ordered | **s4 R7** (no-set()-gates-convergence-order) | CR-7 C2-literal-string-lint | **s4 R4** (C2 literal-string lint) |
| CR-2 convergence-effect-traces-register | **s4 R9** (convergence-effect-provenance) | CR-8 slow-write-attributed | folds into **s4 R2/R3** (consumer-closure + total-accounting `ledger_cause`) |
| CR-3 engagement-window-divergence | **s4 R10** (engagement-window-divergence) | CR-9 director-subtract-only | **s4 §S4.10** (folds into R3/R4; no bare R#) |
| CR-4 foreclosure-surfaces | **s4 R8** (foreclosure-mandatory-render) | CR-10 gating-priced-or-justified | **s4 §S4.9 deferred gate** (pricing-over-gating; no bare R#) |
| CR-5 causes-populated | folds into **s4 R3** (total-accounting linter) | CR-11 meaningfulness-integer-arithmetic | **s4 §S4.2** replay-determinism (key-log parity harness; no bare R#) |
| CR-6 rationing-total-order | **s4 §S4.2.4** Top-N total order (no bare R#) | CR-12 consumer-closure | **s4 R2** (consumer-closure) |

s4's `R1` (predicate-field-resolves) and `R5` (scene_entered single-emitter) have no `CR-N` peer here —
they belong to the compile/substrate lanes, not this section's Q3 detector/lifecycle surface.

---

## §Q3.10 — Worked compilation: ARC-S07 "Torben Loyalty Clock" (capstone #10, end-to-end)

Register source (`arc_register_factions.md:10–11`): `Crown | ALL | ALL`. "IP 30 → Tutoring Demand fires.
Crown options degrade the Loyalty track (8→0) at −1/season when Covert Contact (Intel vs Ob 3/season)
fails. Loyalty ≤ 3 → Coup Counter +1. Loyalty ≤ 2 → Crown Mandate −2 cumulative. Contact maintained 3
consecutive seasons → floor at 6. Laskaris (PROTECTIVE) delays demand 1 season but flips if Elske Loyalty
≤ 2 (IP +3 immediately). Direction: Altonian pressure converts the heir into a lever against the dynasty."

```yaml
arc_vector:
  id: ARC-S07
  tier: S
  tier_rank: major           # spans ALL territories, feeds 3 COLLISIONs, PC-castable via Crown ties
  scope: { faction: [Crown], territories: ALL, mode: ALL }
  activity_mode: clock_escalation
  trigger:
    predicate:
      - { field: clock.IP, op: ">=", value: 30 }     # co-fires ARC-T02 Tutoring Demand, parallel
                                                       # branch (arc_register_factions.md:41
                                                       # "The two arcs run in parallel from the same
                                                       # trigger.")
    resolves_via: null                                 # pure clock-threshold read
    temporal_window: same_season
  pressure_effects:
    - { target: npc_track.Torben.Loyalty, delta: "-1", cadence: season,
        condition: "Covert Contact fails (stat.Crown.Intel vs Ob 3, resolves_via: dice_pool)" }
    - { target: clock.CoupCounter, delta: "+1", cadence: season,
        condition: "npc_track.Torben.Loyalty <= 3"
        # [GAP struck_mechanic] Coup Counter STRUCK (ED-781 supersedes ED-589,
        #  params/factions_personal.md:68,103-107); must remap to Löwenritter Autonomy stage
        #  before this line compiles. FORK 1 default = 1:1 threshold remap. }
    - { target: stat.Crown.Mandate, delta: "-2 cumulative", cadence: season,
        condition: "npc_track.Torben.Loyalty <= 2" }
    - { target: npc_track.Torben.Loyalty, delta: "floor(6)", cadence: one_time,
        condition: "3 consecutive successful Covert Contacts"
        # [GAP missing_field] per-vector consecutive-success streak counter; pattern exists
        #  (Thread Fatigue, module_contracts.yaml:280) but is not generalized. }
    # NOTE: the Laskaris IP+3 flip (Elske Loyalty <= 2) is NOT an ARC-S07 pressure_effect — it is
    #  its own vector NPC-ARC-LAK (arc_register_factions.md:312-313), carried below as a cross_ref
    #  (single home, agrees with s5.1). ARC-S07 does not write clock.IP; it feeds the flip's condition.
  payload:
    direction: "Altonian pressure converts the heir into a lever against the dynasty."
    participating_actors: [Torben, Almud, Ehrenwall/Löwenritter, Laskaris, Elske, Baralta]
    stakes_tags: [pricing, foreclosure]   # reconciled with s5.1: extraction is PRICED (Beat-2.1/4.1
      #  ledger cause), the Altonian oath is FORECLOSURE (retrieve_as_loyal_heir permanently closes).
      #  'gating' dropped — the one GATED *option* (Formal Crown Treaty) is an ARC-T17 diplomacy wall,
      #  not an ARC-S07 transition; 'pattern_response' dropped as weakly grounded (no divergent-summons
      #  edge is authored on this vector). Matches s5 stakes_tags exactly.
    ledger_cause: ["PP-498 (Torben track, params/board_game.md §Torben)"]
  lifecycle:
    state: escalating          # live value; enumerates:
      #  seeded (IP<30)
      #  → active (Tutoring Demand fired, IP>=30)
      #  → escalating (Loyalty falling on failed Covert Contact)
      #  → converging (feeds COLLISION-B / COLLISION-C / COLLISION-F)
      #  → resolved (floor 6 reached) | abandoned (Loyalty 0 → ARC-T13 Crown-elimination branch,
      #    arc_register_factions.md:43-44)
    terminal: false
  cross_refs: [ARC-S20, ARC-T02, ARC-T13, ARC-S35, NPC-ARC-LAK, COLLISION-B, COLLISION-C, COLLISION-F]
    # NPC-ARC-LAK = the Laskaris IP+3 flip's home vector (moved out of pressure_effects, above; agrees
    #  with s5.1). ARC-S35 (Succession Vacuum) is fed by the foreclosure ending.
  gaps:
    - { type: struck_mechanic, note: "Coup Counter increment step (fork 1)",
        cites: ["params/factions_personal.md:68,103-107", "arc_register_factions.md:11"] }
    - { type: missing_field, note: "3-consecutive-success streak counter (ED-IN-0003 family)",
        cites: ["module_contracts.yaml:280"] }
    - { type: open_number, note: "ED-609 (OPEN) — Torben Beliefs/Conviction emergence unspecified
        (first faction to Disposition>=+2 in window sets Torben's initial Conviction). The Loyalty-clock
        MECHANICS do NOT depend on it — ARC-S07 compiles and runs the 8->0 track regardless. It is
        flagged because the meaningfulness identity-touch (§Q3.1) reads Torben's Conviction/Belief as a
        slow variable, and that seeding is not yet formally specified. Disposition: compile leaves ED-609
        OPEN (not a blocker); do not fabricate Torben's initial Conviction.",
        cites: ["canon/editorial_ledger.jsonl (ED-609)", "designs/arcs/arc_expansion_v30.md:758"] }
```

**End-to-end trace (the capstone story path):**

1. **seed → active.** `clock.IP` crosses 30 → `trigger.predicate` true → FSM `seeded → active`; emits
   `meta.arc_state_changed` (Class B, consumer-closed, C2-internal). ARC-T02 (Almud's parallel Belief
   crisis, `arc_register_factions.md:41`) activates on the same trigger — braided by shared
   `participating_actors:[Almud]`.
2. **escalating.** A failed Covert Contact (resolved by the ordinary `dice_pool` engine — C3, the arc
   **books the venue, never owns resolution**) emits an outcome Key that re-enters ARC-S07's `causes[]`
   (CR-5); `Loyalty −1`; FSM `active → escalating`.
3. **story-vs-context + meaningfulness.** The Loyalty-tick Key is STORY (matched by ARC-S07's own
   `pressure_effects` target). Meaningfulness = `durability(Loyalty→heir-turn, slow-ish) ×
   tie_proximity(Torben is a participating_actor = 0 hops) × identity_touch(changes what the dynasty
   OWES/what is POSSIBLE)` → above cutoff → foreground candidate.
4. **participated branch (capstone #3).** If the PC (Crown-tied, cast via §Q2 tie-graph) participates and
   *succeeds* 3 consecutive contacts → `floor(6)` → FSM to `resolved` — a **different next state** than
   the ignored/failed path (`Loyalty 0 → abandoned → ARC-T13`). CR-3 satisfied: ≥2 outcome classes → ≥2
   distinct next states. Ignoring the summons is **remembered, never a pause** — the FSM ticks on schedule
   regardless (Q1 non-participation).
5. **converging → COLLISION.** At the ACCOUNTING_BOUNDARY, if `Torben.Loyalty ≤ 3` co-occurs with the
   COLLISION-C constituent condition, the Tier-A detector fires COLLISION-C (register-authored, effect-
   bearing: `RS +8, IP +2, TC +2`, `arc_register_events.md:39`) — deduped by the ordered key (CR-1),
   emitting `meta.convergence_detected`. (COLLISION-C is itself blocked pending ARC-T04, fork 2 — see
   `dossier_register_formalizability` §6; ARC-S07 still feeds COLLISION-B/F cleanly.)
6. **resolution → chronicle echo (capstone #1).** Terminal transition renders diegetically (a scene at a
   venue, Q4); the annual chronicle records it; a later Baralta arc (ARC-S20, `arc_register_factions.md:38`)
   references it via the `causes[]` walk — recognized *backwards* as story (§Q3.7 PLOT).

**Verdict:** machine-checkable-with-new-field. Every clock/stat is canonical (Torben Loyalty:
`clock_registry_v30.md:27`, range 0–7 start 3 — the register's "8→0" gloss is a **live range conflict the
season trace depends on**, flagged `[OPEN — Jordan]` in s5 §S5.1, not silently harmonized). The two
blockers (Coup Counter migration, streak counter) are **buildable, not GM-judgment**
(`dossier_register_formalizability` §5). **ED-609 (OPEN) is a dependency the compile DOES NOT take on:**
the Loyalty-clock mechanics run without Torben's Conviction-emergence spec; ED-609 is carried in `gaps[]`
as an open-number item because the meaningfulness identity-touch reads Torben's Conviction as a slow
variable whose *seeding* is unspecified — the arc compiles and fires, but the engine must not fabricate
that initial Conviction (anti-fabrication, CLAUDE.md §5/§7).

---

## §Q3.11 — Genuine Jordan forks (stated fork + default — never silently resolved, CLAUDE.md §2 ED-1094)

1. **Coup Counter migration.** Remap numeric thresholds (2, 3, 40) 1:1 onto the Löwenritter Autonomy
   4-stage track, OR re-author arc text against stage semantics. **Default: 1:1 threshold remap** (cheaper;
   unblocks ARC-P03/S20/S56, NPC-ARC-BRA, ARC-T26, COLLISION-F). Blocks compile Stage 1. `[OPEN — Jordan]`
2. **ARC-T04 / Southernmost Ritual.** Author fresh, OR strike the two dangling cross-refs
   (`arc_register_territory.md:33`, `arc_register_events.md:38`; both cite unrelated ED-416 entries).
   **Default: strike the stale cross-refs** (COLLISION-C becomes 7-of-8), defer authoring to a WR-lane arc;
   needs a fresh lane-tagged ED. `[OPEN — Jordan]`
3. **Convergence `temporal_window`.** same-season / same-Accounting / N-season lookback. **Default:
   4-season cosine window (±0.40, quantized per CR-11) for the general Tier-B backbone; same-Accounting
   for the 8 Tier-A conjunctions.** Blocks Detect stage. `[OPEN — Jordan tuning]` for the numbers; the
   arithmetic determinism (CR-11) is structure, ruled regardless.
4. **`lifecycle.state` field ownership.** Class B extension of the `npc_behavior` arc-state bucket
   (`module_contracts.yaml:150`), OR a new `game_director`-owned store. **Default: game_director-owned
   store** (engine OWNS arc-vector state; the NPC bucket stays the specialization it reads). `[OPEN — Jordan]`
5. **GM-judgment-irreducible ~15% (ARC-P05, ARC-S29).** Author a per-arc decision function (C5
   scripting-drift hazard), OR declare non-firing in `gaps[]` until authored. **Default: declare
   non-firing (honesty ledger)**; author case-by-case later. `[OPEN — Jordan]`
6. **Bake key includes Certainty? (BLOCKER 1).** Charter Q4 lists Certainty as a bake axis; NLG §8 omits
   it. **Default (charter authority): include it in the frozen pool → bake is LOW-THOUSANDS**, not 350–450
   (`dossier_content_economics` §3 item 3, ~5–6× multiplier). Fallback if bake cost prohibitive = Certainty
   as a runtime lexicon-swap, which restores the ~350–450 figure. The section headline uses low-thousands
   under the default. `[OPEN — Jordan tuning-adjacent]`
7. **Director tension-curve reversal.** CR-9 (`director-subtract-only`, §Q3.7/§Q3.9) has *all* sections
   adopt **subtract-only** rationing (RATION/DEMOTE only; never INSERT / ADVANCE / reorder / delay /
   time-compress), which **reverses** the charter's "director … owns the tension curve" (Q4 L128–129).
   **Default (recommended): subtract-only** — doc-10 §8.5 "no designed dramatic timing" stands (charter Q3
   L104–105); event timing stays fully emergent, and any "tension curve" is a backward *reading*, never a
   steered target. This is a hard design call **held back for explicit Jordan sign-off and flagged in the
   PR body**, not bundled as routine work (CLAUDE.md §2 ED-1094). Shared with s1 fork 5, s5 O-9.
   `[OPEN — Jordan]`

**Fork-numbering harmonization with s5's `O-1..O-8` scheme (stated once).** s5 (`s5_season_trace.md §S5.8`)
labels the same open forks `O-N`; this section's forks map on as: **fork 1** (Coup Counter) = **s5 O-2** /
synthesis fork 1; **fork 2** (ARC-T04/COLLISION-C) = **s5 O-3** / synthesis fork 2; **fork 3** (temporal_
window) = **s5 O-5**; **fork 6** (Certainty bake axis) = **s5 O-6**; **fork 5** (GM-judgment ~15%) = **s5
O-8**; the **held-back `scene_entered`** call below = **s5 O-1**; the new **fork 7** (director tension-curve)
= **s5 O-9**. This section's **fork 4** (`lifecycle.state` ownership) has no s5 `O-` peer — it lives in the
substrate lane (`s4_substrate.md §S4.11 fork 2`). s5's `O-4` (realizer fragment-selection determinism) and
`O-7` (engine_clock/Gate-0) are render/staging-lane forks with no `Q3` fork peer here (see §Q3.12 seams).

### Held-back hard calls flagged for the PR body (NOT silently resolved — CLAUDE.md §2)

- **`mechanical.scene_entered` ownership** is charter-classified `[OPEN — Jordan]` (`00_engine_charter.md`
  L147–148). The synthesis relabels it "RESOLVED"; this section **restores it as an explicit fork** rather
  than bundle a hard design call into routine work. **Recommended resolution: `game_director`
  single-source** (consistent with `scene_timer` already consuming it `from:[game_director]`,
  `module_contracts.yaml:392–395`), `scene_slate` demoted to content-Key generation. **BUT** this
  contradicts `key_substrate_v30.md` §8.5 (which attributes `scene_entered` emission to `scene_slate`);
  **the resolution is not complete without an explicit edit to `key_substrate_v30.md` §8.5 shipped in the
  same PR.** Until §8.5 is edited, this remains a fork, flagged prominently in the PR body. `[OPEN — Jordan]`

---

## §Q3.12 — Cross-lane seams this section depends on (not resolved here)

- **Q4 render lane owns:** the L5 realizer fragment schema, the ERA bake gate (BLOCKER 2), the bake-volume
  number (BLOCKER 1 / fork 6), and **realizer fragment-selection determinism** — the adversarial MAJOR that
  "same rendered text" (charter Q4, `propagation_spec_v1.md` O.8) is unbacked while RNG-MODEL-COLLISION is
  open (`propagation_spec_v1.md` O.5). Recommended to that lane: fragment selection must be a **pure
  function of Key metadata + focalizer + register band** OR drawn from a **dedicated render sub-stream
  seeded from `(campaign_seed, key.id)`** so render never perturbs simulation draws; forbid
  string-hash/dict-iteration/wall-clock selection; gate on disposing RNG-MODEL-COLLISION as a Stage-0
  precondition.
- **Staging / Gate-0:** the Detect layer's Accounting-boundary evaluation and the Store+tick layer's
  clock-stepping both **ride the temporal spine** — so they are gated behind **engine_clock authoring
  (ED-1051, Gate-0)** per `strategic_judgments` J-2, whose candidate home is `propagation_spec_v1` /
  ED-1093. Stage 0 (render-gap close) and Stage 1 (compile) have no clock dependency and may precede it.
- **ORD-4:** the season scene-queue must relocate from `scene_slate` module scope to World scope
  (`propagation_spec_v1.md` O.7 ORD-4) for the parallel-replay hazard that the 5-seed narrative-regression
  gate depends on.

---

_End §2 / Q3. PROPOSED pending ratification (ratified-on-merge per CLAUDE.md §2 ED-1094; the held-back
scene_entered call in §Q3.11 is flagged for separate PR-body sign-off)._
