# Architecture A — The Minimal Detector (full working notes)

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
Lane: Architecture A of the Emergent Narrative Engine effort. Premise assigned: the **smallest
coherent change** that closes ED-IN-0003 + ED-IN-0004 and makes computed emergence *arrive and
render*, adding **no new arc-lifecycle state** beyond what detection strictly needs.

---

## 0. Thesis

Four surgical moves, each riding existing canon, no new narrative-direction module:

1. **Convergence-marker registry** — the 8 COLLISION markers of `arc_register_events.md §VI`
   transcribed as typed predicates over state the engine already READS, checked once per season
   at `ACCOUNTING_BOUNDARY`, emitting `meta.convergence_marker`. (ED-IN-0003)
2. **Articulation trigger-table completion** — `articulation_layer_v30.md §3.1`'s 10-trigger
   table extended with the triggers §6.3/§6.4 already claim fire but the table omits, plus the
   four ED-681 thread beats (`threadwork_v30 §3.7`) and `meta.convergence_marker`. (ED-IN-0004 + C6)
3. **NLG realizer graduated to PROPOSED** — `03_articulation_nlg_architecture.md` given a
   fragment schema + one worked example (ARC-S07), filling the §5 `emit_cut_scene` socket. (Q4)
4. **Slate injection via existing priority steps** — `meta.convergence_marker` routes into
   `player_agency_v30.md §4`'s existing 7-priority slate; NO new slate step. (Q1)

The design **deliberately does not** author `game_director`/`scenario_authoring` home docs, does
not build a general correlation detector, and does not add per-arc lifecycle state. That restraint
is the whole premise — and Section 7 states honestly where it costs the four questions.

---

## 1. Anchor point: the detector is an Accounting step

`propagation_spec_v1.md §O.-/table` (line 46): `run_season` composes exactly three steps —
`SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY` — the last a fixed **five-step** composition
(`accounting.py:37-79`). The table (line 52) already lists ACCOUNTING_BOUNDARY as the home of
"CI calc; MS year-end decay; insurgency triggers/promotion; NPC ecology; engine_clock emits
`mechanical.accounting`." **The convergence detector is a 6th deterministic step appended here.**

Why this anchor and not the Key stream:
- Convergence markers are **conjunctions over end-of-season aggregate state** (Church Stability,
  TC/CI, Torben Loyalty, territory control). They are naturally evaluated *after* the same-season
  deltas land, which is exactly the deferred-apply timing the boundary already enforces
  (`propagation_spec §A1 ECHO-DEFERRAL`, line 267; `scale_transitions_v30 §5.5 AUD-SET-02`).
- Running at the boundary means the detector reads settled state, avoiding mid-tick races. Its own
  emitted `meta.convergence_marker` re-enters the **same cascade_depth-capped drain** (line 56), so
  the termination guarantee already covers it — no new re-entrancy reasoning needed.
- Determinism: `(season_index, sub_step_index)` is a total order (`propagation_spec §SSI-3`); the
  detector appends its Keys in a fixed marker-iteration order → replay-identical (PP-687 §6 V4).

---

## 2. Mechanism 1 — Convergence-marker registry (ED-IN-0003, the detector AND the applier)

### 2.1 The 8 markers as data
`arc_register_events.md §VI` gives 8 COLLISION entries (A, B, C, D, E, F, G, J — H/I absent). Each
is already, structurally, a **trigger predicate → combined-effects** pair:

| Marker | Trigger (conjunction of arc/state conditions) | Combined effect |
|---|---|---|
| A Church Double Fracture | Klapp conversion (ARC-S21) ∧ Olafsson exposure (ARC-S06) | Church Stability −3; TC/CI generation pauses |
| B Practitioner King | Almud Discovery (ARC-S17 TS28→30) ∧ Elske installed (ARC-S23) ∧ Torben in Altonia (ARC-S07) | Crown distributes; TC +3, RS/MS improves |
| C Tutoring + Southernmost | Torben Loyalty ≤3 (ARC-S07) ∧ Southernmost Ritual failure (ARC-T04) | RS/MS +8, IP +2, TC +2; cascade |
| D Niflhel Weaponises | Church-Niflhel exposure ∧ 218AG perpetrator=Niflhel ∧ Varfell Collection held | leverage over all factions |
| E Einhir Elder / Baralta | Witness testimony (ARC-T23) ∧ Baralta claim (ARC-S19) ∧ Klapp archive | Grand Debate; Church Stability −3 |
| F Succession Triangle | deed-presumption weak (Coup Counter ≥2 ∨ Almud ∨ Torben loss) ∧ ARC-S26 ∧ ARC-S35 | three-way contest |
| G Einhir Triangle | Lenneth ∧ Baralta ∧ Vaynard programmes all active | no stable resolution |
| J Church Siege | Church controls T9+T2 (TE-28) ∧ TC/CI ≥60 ∧ RS/MS ≤39 | corridor + substrate destabilization |

**Typed predicate form** (minimal — no new schema beyond a predicate DSL over existing fields):
```
convergence_marker:
  id: COLLISION_A
  activity_mode: edge_triggered_once
  trigger: {all_of: [
    {field: npc_track.klapp.converted, op: "==", value: true},        # ARC-S21 state
    {field: arc_state.ARC-S06.investigation, op: "==", value: exposed}]}
  combined_effects: [{target: church.stability, delta: -3, cadence: once},
                     {target: clock.CI, op: pause_generation, condition: "church.stability<=4"}]
  participating_actors: [Klapp, Olafsson, <Church cardinals>]
  constituent_arcs: [ARC-S21, ARC-S06]
```
Every `field` must resolve to a registry-declared state path (conformance rule §6.4-1). This is the
**concrete form of ED-IN-0003's "detector/applier."**

### 2.2 The detector (the missing computation)
```
# accounting.py step 6 (NEW), runs at ACCOUNTING_BOUNDARY
def detect_convergence(world, fired_set):
    for m in CONVERGENCE_REGISTRY:                       # fixed iteration order (determinism)
        if m.id in fired_set: continue                   # edge_triggered_once dedup
        if eval_predicate(m.trigger, world):             # pure read of settled state
            key = emit("meta.convergence_marker",
                       payload={marker_id, constituent_arcs, combined_effects,
                                participating_actors},
                       causes=[<the constituent arcs' most-recent state Keys>],  # causes[] populated
                       targets=participating_actors,
                       scale_signature=<max scale of constituents>)
            fired_set.add(m.id)
        else:
            log_discard(m.id, reason="predicate_false")  # C.5 total accounting — never silent
```

### 2.3 The applier (the other half of ED-IN-0003)
`combined_effects` are **not** applied inline. They are queued as **deferred-apply `stat_deltas`**
on the exact ECHO-DEFERRAL path the boundary already runs (`propagation_spec §A1`, line 267): the
`meta.convergence_marker` Key is appended live (preserving causes[]), its deltas applied once at the
boundary's deferred-apply pass. **No new apply machinery** — this is why the applier is minimal.

### 2.4 The one new owned state
`convergence_fired_set` — a per-campaign set of `marker_id`s already fired. This is the *entire*
new state the premise permits: it is edge-once dedup, NOT arc lifecycle. Markers are otherwise
stateless; a marker's "window" is just re-evaluation each Accounting (no owned window object).

### 2.5 Blockers inherited from the corpus (register-formalizability dossier)
- **COLLISION C is un-buildable as written**: ARC-T04 ("Southernmost Ritual") is a dangling
  register ID (referenced from `arc_register_territory.md:33` + `arc_register_events.md:38`,
  defined nowhere; citation "[UNNAMED — ED-416]" resolves to two unrelated ledger entries). 1 of 8
  markers is blocked pending authoring. [dossier: register-formalizability]
- **Coup Counter is STRUCK** (ED-781 supersedes ED-589; `params/factions_personal.md:68,103-107`),
  replaced by a 4-stage Löwenritter Autonomy track — but COLLISION-F still triggers on the numeric
  Counter (`≥2`) with no remap authored. Predicates for A/F/G need the migration first. [dossier]
- The register uses legacy names **TC** (→ CI, ED-782) and **RS** (→ MS, ED-731) throughout;
  trivial alias-resolution at transcription time, not a structural gap. [dossier]

---

## 3. Mechanism 2 — Articulation trigger-table completion (ED-IN-0004 + C6)

### 3.1 The gap (F-4)
`articulation_layer_v30.md §3.1` lists **10** triggers (table lines 81–92). But §6.3/§6.4 already
DECLARE that `state.belief_revised`, `scene.combat_resolved`, and `scene.battle_concluded` "emit
Tier 2 cut scene by default" — the belief case was patched in as trigger #10, but **combat_resolved
was authored under the ED-936 [ASSUMPTION] grant (§6.4 comment) and is NOT in the §3.1 table.** The
§5 socket (`matches_trigger_ruleset(key)`, line 256) only fires what the table lists → the declared
render silently never happens. That is ED-IN-0004.

### 3.2 The completion (pure trigger-table authoring, no mechanism change)
Add to §3.1:
| # | Trigger | Source it discharges |
|---|---|---|
| 11 | `scene.combat_resolved` (any) | discharges §6.4's [ASSUMPTION] claim |
| 12 | `scene.battle_concluded` (any) — confirm listed | §6.4 says "already triggers"; verify |
| 13 | `scene.investigation_resolved` (case closed / trail cross-ref ≥ threshold) | fieldwork venue (Q4 venue matrix) |
| 14 | **ED-681 thread beats** — `state.rendering_crisis_beat` ∈ {Withdrawal, Knot-Anchoring, Place-Anchoring, The-Choice} (`threadwork_v30 §3.7`) | **C6 (hard constraint): these MUST render** |
| 15 | `meta.convergence_marker` (any) | routes Mechanism 1 to the render path |

The §5 socket is untouched — any matched Key already flows to `emit_cut_scene(key, sig)`. Trigger
9 (`meta.cascade_cluster_event`, §3.1 lines 94–112) is already present and already fires; it is
the closest existing analogue to convergence and confirms this pattern is canon-native.

### 3.3 Significance routing
Convergence markers score high on `§3.2 significance` (stakes_weight from scale_signature +
cascade_event_weight) → 10-15s "scene" style. Thread beats carry protagonist_alignment (they are
protagonist-internal) → guaranteed cut scene. No calibration numbers invented (those are
[OPEN — Jordan tuning]).

---

## 4. Mechanism 3 — NLG realizer graduated as PROPOSED (Q4)

Graduate `03_articulation_nlg_architecture.md` (currently architecture-only, its own §10) to a
buildable spec — this is what fills `emit_cut_scene` / the Tier-3 chronicle templater (§5). Per the
NLG-graduation dossier, the minimal graduation delivers:
- A **fragment schema** riding existing Key metadata only (causes[], targets[].role,
  symbolic_dimensions, significance, awareness — `00_key_io_review §1`; NLG §10 already asserts no
  new Key fields). No new substrate.
- **One worked example: ARC-S07 Torben Loyalty Clock** compiled end-to-end (capstone #10) — the
  charter states this IS the required buildable-proof, not a separate ask.
- The two authoring tables converted to runtime lookups: `coherence-tiers.md` weights as a
  **bake-time** generation budget (deterministic exact-match at runtime, not runtime probability);
  `solmund_voice_v30 §18` Certainty registers as a keyed table.
- A literal-string **C2 lint** at bake-audit time (fragments are frozen assets → cheap regression
  gate against "arc"/"convergence"/"Rising Action" surfacing).

Minimalism note: Architecture A takes the NLG proposal **as-is and graduates it**; it does not
redesign the realizer. Pacing director (D11) stays explicitly deferred (loud, per CLAUDE.md
ratification-exception principle) — not required by any capstone. [dossier: nlg-graduation]

---

## 5. Mechanism 4 — Slate injection via existing priority steps (Q1)

`player_agency_v30.md §4` already runs a deterministic 7-priority slate (grounding 3d). Minimal
injection: `meta.convergence_marker` is consumed by `scene_slate` and routed to an **existing**
step by scale —
- major marker (peninsular scale_signature) → **Step 1 Mandatory Crisis** (ED-761 override order;
  overflow → Witness Mode — a spectator channel, capstone #4).
- territorial/minor → **Step 6 Territorial** / **Step 7 Ambient**.

No new slate step, no new priority algorithm. Casting ("why you") uses the existing tie-graph: the
marker's `participating_actors[]` (derived from constituent arcs' scope) intersected with the PC's
Bonds/Duty/Standing (player_agency §4.2). Participation IS Key-emission (charter Q1): the arc-tagged
slate scene resolves through the ordinary subsystem engine (C3 — engine books venues, never owns
resolution), and its outcome Key enters the marker's causes[] chain for the *next* season's
re-evaluation.

### 5.1 Worked capstone trace (ARC-S07 → COLLISION C)
Season N: Torben Covert Contact fails (Intel vs Ob 3) → Loyalty −1 Key. … Loyalty hits ≤3
(ARC-S07 vector). At ACCOUNTING_BOUNDARY, detector evaluates COLLISION-C: `Torben.loyalty<=3 ∧
ARC-T04.ritual==failed`. (If ARC-T04 authored →) emits `meta.convergence_marker[C]` → trigger #15
fires a 15s cut scene (NLG realizer, Coherence/Certainty-registered) → scene_slate Step-1 injects a
Mandatory Crisis at the venue where Torben's lever bites → PC participates → outcome Key → chronicle
paragraph at year-end (Tier 3) with causes[] walk. **Traverses**: individual (Torben) → faction
(Crown) → territory (Altonia). Capstones #1 (partial — see §7), #7 (venue labeled), #9 (accounting),
#10 (ARC-S07 compiled).

---

## 6. Substrate contract

### 6.1 States
- **OWNED** (minimal): (1) `convergence_fired_set` (§2.4 — edge-once dedup, per campaign);
  (2) the §3.3 `unarticulated_weight` accumulators (already owned by articulation, unchanged).
  **No arc-vector states, no owned convergence-window objects, no lifecycle enum.**
- **READ**: all clocks (CI, MS, IP, PI, Löwenritter Autonomy track), faction stats (Mandate/
  Influence/Wealth/Stability/Military), NPC tracks (Torben Loyalty, Certainty, TS), territory
  control — via existing `state_reader` access (holonic containment; charter substrate-contract).

### 6.2 Keys IN
Detection **subscribes to nothing new** — it reads settled state at the boundary, not the Key
stream. Articulation already subscribes to all emissions (`§5`, PP-687 §4.1 step 5). Filtering
ladder (trigger → significance → accumulate → discard) is already the §3/§5 path.

### 6.3 Keys OUT — TOTAL ACCOUNTING
| Key | Emitter | Consumer | Disposition |
|---|---|---|---|
| `meta.convergence_marker` (NEW Class B) | detector (accounting step 6) | articulation (→cut scene/chronicle) + scene_slate (→Step-1/6 inject) | **RENDERED** |
| `scene.combat_resolved`, `scene.investigation_resolved`, 4× thread-beat, `meta.cascade_cluster_event` | existing emitters | articulation (via new §3.1 triggers 11–15) | **RENDERED** (were ACCUMULATED/dropped) |
| combined-effect `stat_deltas` | detector | world (deferred-apply, ECHO-DEFERRAL) | **CONSUMED-INTO-STATE** |
| each non-firing marker, per Accounting | detector | log | **EXPLICITLY DISCARDED (reason: predicate_false)** |

`meta.convergence_marker` registered in `key_type_registry_v30` with ≥1 declared consumer
(articulation + scene_slate); `targets[]`=participating_actors, `causes[]`=constituent-arc state
Keys. Nothing silent.

### 6.4 Edges (declared-vs-implemented) + the scene_entered conflict
- Detector step: **declared here, unimplemented** (this is a spec). Lives inside engine_clock's
  accounting composition; marker DATA lives in a new `references/arcs/convergence_registry.md` (a
  data asset, not a module).
- **scene_entered ownership conflict**: minimal detector **does NOT claim
  `mechanical.scene_entered`** — it emits `meta.convergence_marker` only. `scene_slate` keeps
  `scene_entered`; `game_director`'s duplicate emission (`module_contracts.yaml:349,375`,
  [OPEN — Jordan]) is **left open, not resolved.** This is the honest minimal-scope cost (§7, Q2).

### 6.5 Six directions
- **LATERAL** (primary): the detector reads across factions/territories at one scale — this IS
  convergence. Ordering: fixed marker-iteration order at the boundary.
- **BACKWARDS**: reading accumulated state = reading history; chronicle callback walks causes[].
- **FORWARDS**: the emitted marker Key flows into slate + articulation (pressure → choice).
- **UP / DOWN / DIAGONAL**: **UNUSED.** The detector performs no aggregate-up or distribute-down
  transform — it is a same-scale reader. Per `propagation_spec_v1` those transforms exist and the
  charter asks for "all six directions each with ordering/determinism notes"; minimal detection
  honestly covers only three. (A fuller architecture would let a marker distribute-down into
  constituent-territory scenes; minimal does not.)

### 6.6 Conformance (CI rules, each living once in `tools/`)
1. **Predicate-field validity**: every marker `trigger.field` resolves to a registry-declared
   state path → auto-flags COLLISION-C (ARC-T04 dangling) and Coup-Counter references (struck).
2. **Consumer closure**: `meta.convergence_marker` has ≥1 `consumes:` declarant.
3. **Total-accounting lint**: every marker is fired-or-discarded-with-reason each Accounting.
4. **C2 literal-string lint**: baked fragments contain no narratological vocabulary.

---

## 7. Sufficiency against the four questions — HONEST

### Q1 Player → world: **PARTIAL**
- **Satisfies**: slate-injection + Key-emission loop genuinely works because it rides existing
  transport — participation IS Key emission; outcome Keys enter the marker's causes[] and change
  the state next season's predicate re-evaluates. Non-participation is also an input (the predicate
  re-fires or doesn't based on whatever the world did). Anti-railroad holds *through stat change*.
- **Falls short**: with **no per-arc lifecycle state** (excluded by premise), the engine cannot
  represent "the arc advanced to *escalating* BECAUSE you participated" as a first-class transition.
  It can only re-evaluate the same static conjunction. Capstone #3 ("participated outcome changes
  the arc's *next stage*") is only demonstrable insofar as the outcome flips a stat inside a marker
  predicate — NOT as arc-stage branching. The register-formalizability dossier's finding 4.1 (the
  generalized per-arc lifecycle field, "the concrete form of ED-IN-0003") is **exactly what
  Architecture A declines to build** — so Q1's deepest requirement is deferred.

### Q2 World → player: **PARTIAL**
- **Satisfies**: casting rides the existing tie-graph; markers name participating_actors[] so
  "why you" is diegetically answerable. The 8 markers arrive as Mandatory Crisis / territorial
  scenes — impulsion with deadlines.
- **Falls short**: the **social-ladder traversal** (individual→family→settlement→territory→
  faction→world) is only partly served — the 8 markers are overwhelmingly faction/territory tier.
  The **family rung** and the **factionless on-ramp** get *nothing new* from a minimal detector
  (they need arc-vector carriers per rung — excluded). **Position-determines-native-story** (leader
  subordinate-originated beats vs member duty beats) is **not addressed at all** by minimal
  detection. game_director/scene_slate conflict stays open → no owner for the leader-beat routing.

### Q3 Events legible as narrative: **STRONGEST FIT, but bounded**
- **Satisfies**: the convergence detector IS the emergence-vs-noise discriminator the charter
  demands for the 8 authored cases — each COLLISION is a hand-authored correlation test (shared
  targets, same-direction pressure on a shared stake). Emitting `meta.convergence_marker` makes
  "the engine noticed independent vectors converged" a real, queryable, rendered event. This is the
  cleanest close of ED-IN-0003.
- **Falls short**: (a) **only 8 markers exist** — the detector is a **whitelist, not a general
  discriminator.** Anything outside those 8 conjunctions is invisible; the charter's general
  "correlation tests / temporal windows / causes[] overlap" discrimination is NOT built. The
  dossier notes NO COLLISION entry even specifies a temporal window, though Q3 names it a required
  dimension. (b) The **meaningfulness test** (durability × tie-proximity × identity-touch) is NOT
  implemented — the detector fires on predicate truth, not a meaningfulness score, so **capstone #8
  (pass one beat, fail one context event) cannot be demonstrated** without adding that test.
  (c) **Arc taxonomy + lifecycle states** (seeded→…→resolved, queryable) are explicitly not built.
  Q3 is answered *for 8 authored convergences* and *not* as a general legibility engine.

### Q4 Narratives present: **GOOD render path, thin presence**
- **Satisfies**: graduated NLG realizer + completed trigger table genuinely close the render gap —
  a fired marker/beat produces a Coherence/Certainty-registered cut scene or chronicle paragraph.
  Capstone #10 (ARC-S07 end-to-end) is demonstrable. C6 (thread beats render) is closed by trigger
  #14. Watching channels (cut scene, chronicle, Witness Mode) are well served.
- **Falls short**: **texture-between-scenes** (rumor/overheard/documents — the immersion-audit gap)
  is **not addressed**; **trails** (causes[] walk as in-world media) get no dedicated surface;
  **pacing director** stays deferred. Critically, Q4's "**every major arc keeps ≥1 open
  intervention point until converging and routes through ≥1 playable scene**" **cannot be
  guaranteed** — there is no "converging" lifecycle state to keep an intervention window open
  *until*. Minimal detection fires *at* the convergence instant, not across an escalation the
  player can enter earlier. That is the single most visible Q4 shortfall.

---

## 8. Module homes claimed
- **game_director**: **NOT claimed.** Minimal detector leaves the `mechanical.scene_entered`
  conflict (`module_contracts.yaml:349,375`, [OPEN — Jordan]) open. Cost against the charter's
  substrate-contract requirement to "give game_director and/or scenario_authoring home docs."
- **scenario_authoring**: **NOT claimed as a runtime module.** The detector is runtime, not
  authoring-time seeding. The marker-predicate DATA is co-filed as a new
  `references/arcs/convergence_registry.md` data asset (natural sibling of the arc register), NOT a
  module spec.
- **scene_slate**: **partially touched** — the detector emits INTO scene_slate's existing
  7-priority injection; it does not own or author the scene_slate spec (which stays doc:null [GAP]).

The detector's own home: a **step inside engine_clock's accounting composition** (`accounting.py`)
plus the articulation §3.1 extension plus the convergence data registry — **three edits to existing
homes, zero new modules.** That is the architecture's defining minimal move, and Section 7's
shortfalls are the price of it.

---

## 9. Staging
1. **Detector spec + registry data** — transcribe 8 markers to typed predicates; resolve blockers
   (author or strike ARC-T04; author Coup-Counter→Autonomy migration for A/F/G; TC→CI / RS→MS
   aliasing). Add accounting step 6 + `convergence_fired_set`. → **closes ED-IN-0003** (7 of 8
   markers; C blocked on authoring).
2. **Trigger-table completion** — §3.1 triggers 11–15 incl. the 4 thread beats. → **closes
   ED-IN-0004 + C6**; unblocks render of already-declared Keys.
3. **NLG graduation** — fragment schema + ARC-S07 worked example + table→lookup conversion + C2
   lint. → fills the §5 socket; unblocks **capstone #10** and the Q4 render path.
4. **Slate wiring + conformance** — scene_slate consumes `meta.convergence_marker`; the 4
   conformance lints. → unblocks the worked-season trace (capstones #7, #9).

## 10. Risks
- 8 markers are a **whitelist, not a discriminator** — no general emergence detection; Q3's
  temporal-window / correlation-test generality unmet.
- **No arc lifecycle** → capstones #1 (full seed→resolution across 3 rungs), #3 (participated
  outcome changes next *stage*), and Q4's "keep an intervention point open until converging" cannot
  be fully demonstrated. The load-bearing shortfall.
- **COLLISION C un-buildable as written** (ARC-T04 dangling; `[UNNAMED — ED-416]` resolves to two
  unrelated ledger entries) → 1 of 8 markers blocked pending authoring.
- **Coup Counter struck** (ED-781) → markers A/F/G need migration before predicates compile.
- **Meaningfulness test unbuilt** → capstone #8 fails without an addition outside minimal scope.
- **game_director/scene_slate conflict left open** — deferred, not resolved; leader-beat routing
  has no owner.
- **Texture / trails / pacing unaddressed** — Q4 immersion-audit gaps persist.
