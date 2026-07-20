# Architecture B — The Arc-Vector Engine (working notes)

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
_Opus lane, 2026-07-05, working tree only. Cites file §section or tags [UNGROUNDED]._

## Thesis

Formalize `references/arcs/` as **runtime DATA**: every register entry compiles to a persistent,
typed `arc_vector` with a lifecycle FSM. The engine is then three verbs over that store —
**tick** (step each vector's FSM on the Key stream + clocks), **detect** (evaluate convergence
vectors, the COLLISION rows, as first-class typed vectors — closes ED-IN-0003), **inject** (feed
arc-tagged candidate scenes into the existing 7-priority slate — closes ED-IN-0004). No new Key
types, no new progression currency (C5), no parallel event system (C3): the engine is a **pure
Key-stream consumer + arc-state owner + slate injector**. Casting reads each vector's
`participating_actors` set against the tie-graph. The one-ledger rule is honoured because
progression tracks (Loyalty, Standing, Conviction, Coup→Autonomy) are literally the vectors'
`trigger` inputs and `pressure_effects` outputs — progression IS the arc I/O.

Grounding for "this is realizable now": the register's own anatomy is already
`trigger → mechanical effects → Direction: sentence` (`01_arc_corpus.md §a`), i.e. already
`trigger → pressure_effects → payload.direction`. The dossier's close read of all 5 register
files finds ~45% compile fully machine-checkable today, ~40% need one buildable field, ~15% are
GM-judgment-irreducible as written (`dossier_register_formalizability.md §3`).

---

## The `arc_vector` schema (from dossier §2, adopted)

```yaml
arc_vector:
  id: string                        # ARC-S07 | TE-01 | BG-CV-01 | COLLISION-C | NPC-ARC-STR
  tier: enum[S, T, P, TE, BG-CV, COLLISION, NPC-ARC]   # 01_arc_corpus.md §a
  scope: { faction: [id]|ALL, territories: [id]|ALL, mode: enum[TTRPG,BG,ALL,Hybrid] }
  activity_mode: enum[
    level_triggered, edge_triggered_once, edge_triggered_retryable,
    clock_escalation,      # multi-stage vector w/ real lifecycle (ARC-S07)
    convergence ]          # second-order: fires over OTHER vectors' state (COLLISION A–J)
  trigger:
    predicate: [ { field: <clock|stat|npc_track|arc_state>.<path>, op, value } ]
    resolves_via: <dice_pool|deterministic_accounting|state_reader|manifest|null>  # module_contracts resolver taxonomy
    temporal_window: <same_season|within_n_seasons|unspecified>   # charter Q3 correlation-test dimension
  pressure_effects: [ { target, delta, cadence: enum[season,immediate,per_attempt,one_time], condition } ]
  payload:                          # internal-only per C2 — never renders as a label
    direction: string               # register's "Direction:" sentence, verbatim
    participating_actors: [actor_id]  # casting surface (Q2) + prose slot fillers (Q4)
    stakes_tags: [enum: gating, pricing, foreclosure, pattern_response, none]   # Q2 four modes
    ledger_cause: [PP-NNN|ED-NNN]   # "every gate cites its ledger cause" (charter Q2)
  lifecycle: { states: [seeded,active,escalating,converging,resolved,dormant,abandoned], terminal: bool }  # Q3 taxonomy
  cross_refs: [arc_vector.id]       # convergence-eligibility surface
  gaps: [ { type, note, cites } ]   # compilation blockers, machine-readable
```

Two worked examples (ARC-S07 Torben Loyalty Clock; COLLISION-C) are fully compiled in
`dossier_register_formalizability.md §5–6` — ARC-S07 is capstone requirement #10.

---

## Where the engine LIVES — three doc:null homes claimed

The registry-inferred scene-orchestration cluster (`03_prior_art_and_module_homes.md §c`) is
exactly the empty shell this architecture fills. I claim/split three:

### 1. `game_director` (`module_contracts.yaml:368-385`, doc:null → I claim it as RUNTIME home)
Home doc = **the runtime arc-vector engine spec.** Owns (charter substrate "engine OWNS"): the
live arc-vector store, actor narrative weight, convergence windows, texture budgets. Runs the
tick→detect→inject loop each season. Resolver stays `manifest` (orchestrator, per
`module_contracts.yaml:372` RU-5 note). **Change vs registry:** `consumes: []` → `consumes: [{type:"*", from: engine}]`
(mirrors `articulation_layer` at `module_contracts.yaml:768`). Emits the existing
`mechanical.scene_entered/exited/skipped` — no new types.

### 2. `scenario_authoring` (`module_contracts.yaml:744-760`, doc:null → I claim it as OFFLINE home)
Home doc = **the register→typed-vector compiler + `arc_vector` schema + campaign-skeleton seed
Keys.** This is **PP-690 realized** (`03_prior_art_and_module_homes.md §a,c`: doc-11 §7.3 named
`scenario_authoring` the home for "campaign skeletons with seed Keys and inflection-point Keys",
never authored). Authoring-time. Owns the compiled `arc_vector` corpus as a frozen data asset
(analogous to `references/engine_params/combat_engine_v1.json`, `module_contracts.yaml:799`).
Emits existing `env.crisis`/`env.disaster` seed Keys. Resolves the "authoring-time vs runtime
classification [OPEN — Jordan]" gap (`module_contracts.yaml:757`): compilation is authoring-time,
seeding is runtime — the schema is the seam.

### 3. `scene_slate` (`module_contracts.yaml:342-366`, doc:null → I EXTEND + resolve conflict)
Demoted to **pure candidate generator**: runs the 7-priority slate (`player_agency_v30 §4`,
`03_prior_art_and_module_homes.md §d`); consumes the arc-engine's injection requests; emits the
`scene.*` content Keys (dialogue/gift/insult/etc.). **It no longer emits
`mechanical.scene_entered`** — see conflict resolution below.

### Resolving `mechanical.scene_entered` ownership ([OPEN — Jordan], `module_contracts.yaml:349`)
Both `scene_slate` and `game_director` claim it. **Resolution: `game_director` owns it, single-source.**
Rationale rides existing wiring: `scene_timer` already consumes `mechanical.scene_entered/exited/skipped`
`from: [game_director]` (`module_contracts.yaml:392-395`) — never from scene_slate. Single-sourcing
to game_director is consistent with the one existing consumer. scene_slate returns a ranked candidate
list (a manifest read, no lifecycle Key); game_director transitions INTO the chosen scene and emits
the lifecycle Key. This is the charter's requested edge resolution.

---

## Q1 — Player affects world (mechanisms)

1. **Participation IS Key-emission → arc I/O.** Player plays an arc-tagged slate scene;
   game_director emits `mechanical.scene_entered` with the arc's `participating_actors` in
   `targets[]` and the arc's `causes[]` chain populated. The scene resolves through the ordinary
   engine (contest/combat/thread/fieldwork/mass-battle/settlement — C3, "books venues, never owns
   resolution"). Outcome Keys flow back; the arc-vector subscribes to Keys whose
   `causes[]/targets[]` intersect its `participating_actors`, and its `pressure_effects.condition`
   guards + `lifecycle` transition fire on the *participated outcome*. **Concrete:** ARC-S07's
   "Covert Contact fails → Loyalty −1" and "3 consecutive successes → floor 6" are exactly
   participated-outcome-conditioned effects (`dossier §5`). This is the schema's native shape —
   nothing special-cased (C5 holonic guardrail).
2. **Reach scales with position.** Aggregate-up on Domain Echo (`sim/cross_scale/domain_echo.py`,
   `01_arc_corpus.md §d`): member outcome Keys aggregate into faction-scope vectors. Leader
   delegation = the delegated NPC is written into `participating_actors`; the consequence Key
   routes back to the leader as `target`. Factionless: a ladder of low-scope vectors keyed to
   Conviction/Duty (Q2).
3. **Non-participation is an input.** The lifecycle FSM steps on its own clock cadence
   (`pressure_effects.cadence: season`) with zero player Keys — the arc proceeds autonomously
   (GD-3-style, `03_prior_art §a` doc-11). Ignoring a summons writes a `pattern_response`/`foreclosure`
   `stakes_tag`, never pauses. Native to the data model: an unattended vector is still ticked.
4. **The world keeps a ledger of you.** One-ledger (C5): the vector's `trigger.predicate` reads
   Convictions/Standing/Obligations/Scars (via `npc_memory`, `module_contracts.yaml:177`; Standing;
   Cascade) — ethics as *pattern* (P-04, no hidden meter), not points.
5. **Anti-railroad proof (C7):** the FSM branches on participated outcome — ARC-S07: floor-6
   survival branch vs Loyalty-0 → ARC-T13 Crown-elimination branch (`dossier §5`). Seed-testable
   via `arc_test_batch` (`01_arc_corpus.md §a`): a different window choice → measurably different
   `lifecycle` terminal.

## Q2 — World affects player (mechanisms)

1. **ONE tie-graph casting rule reading `participating_actors`.** When a vector needs a scene, the
   casting resolver reads its `payload.participating_actors` + the tie-graph edges (Duty/Conviction
   alignment, Bonds/Knots, lifepath/location, Standing, position — charter Q2). PC is cast if in
   `participating_actors` OR tie-adjacent to one. This *rides* `player_agency_v30 §4`'s 7-priority
   algorithm (`03_prior_art §d`): the vector's `scope`+actors decide which step it lands in — Step 3
   Duty, Step 4 Conviction, Step 5 NPC Outreach, Step 6 Territorial. "Why you" = the matched tie
   edge, surfaced diegetically (C2). **Same rule casts NPCs** into `participating_actors` (co-protagonists).
2. **Position determines native story.** Leaders: the NPC concern/project engine (`npc_behavior_v30 §5`,
   doc-12 procedures) emits concern/project Keys; a vector with `scope.faction = leader's` subscribes
   (Keys-in filter target=leader) and injects them as reports-as-scenes / requests-for-ruling —
   named actors with wants (anti-spreadsheet). Members: `stakes_tags: [pricing]` (duties with refusal
   costs) under T-30 information asymmetry. Factionless on-ramp = a vector ladder Conviction/Duty →
   TE-tier settlement arcs → Standing/Obligation as proto-currency → recruitment-as-arc.
3. **Impulsion = deadlines.** `activity_mode: clock_escalation` + `temporal_window` is the diegetic
   clock; forced-choice turns are the FSM's escalating-state exit conditions.
4. **History conditions the option space — four modes as `stakes_tags`:** gating / pricing (preferred)
   / foreclosure (arc events only, `payload` + `lifecycle: abandoned`) / pattern_response. Each carries
   `ledger_cause` — "every gate cites its ledger cause" is a schema field, CI-checkable.

## Q3 — Events legible as narrative (mechanisms)

1. **Story vs context = arc membership, computed.** An event Key is *story* iff some live vector's
   Keys-in subscription matches it (its `causes[]/targets[]` intersect the vector's
   `participating_actors/scope` AND it passes the significance filter). No live vector claims it →
   ACCUMULATED (weight) or DISCARDED-with-reason. This is the total-accounting ladder itself.
2. **Meaningfulness test (durability × tie-proximity × identity-touch).** Generalizes the
   articulation significance function (`articulation_layer_v30 §3.2`:
   `stakes + protagonist_alignment + cascade + accumulated_weight`): identity-touch = a
   `pressure_effect` targeting Belief/Conviction/Scar/Coherence; tie-proximity = tie-graph distance
   to a `participating_actor`; durability = whether it moves a slow variable. Passes iff it changes
   who someone is / what they owe / what's possible for a tie-graph actor — orthogonal to §3.2
   stakes-loudness, as charter demands.
3. **Emergence vs noise = the convergence detector.** COLLISION rows are first-class
   `activity_mode: convergence` vectors whose `trigger.predicate` references OTHER vectors'
   `arc_state` (COLLISION-C: `arc_state.ARC-T04 == ritual_failure`, `dossier §6`). Detection =
   evaluating convergence predicates each tick over shared `targets[]`, `causes[]` overlap, the
   `temporal_window`, and same-direction pressure on a shared stake. **This IS ED-IN-0003** (F-2:
   8 Convergence Markers, no detector). Noise backgrounded, never silently dropped; false positives
   cost trust (charter Q3).
4. **Taxonomy + lifecycle** are measurable off the data: scale span=`scope` breadth, stakes
   weight=`stakes_tags`, duration=lifecycle age, vector count=`cross_refs`, protagonist alignment.
   States persistent + queryable = the store the engine OWNS.
5. **Coherence as A narrative:** concurrency budget per tier (engine-owned texture budgets);
   `causes[]` continuity — arc-tagged scenes populate `causes[]`, directly attacking the ~15%
   population problem (`03_prior_art §a` doc-10; `§e`.5). Chronicle callbacks = the `causes[]` walk.
6. **PLOT under the doc-12 veto (C2):** forwards as pressure/choices (FSM transitions + convergence
   detections, INTERNAL); backwards as story (chronicle `causes[]` walk); setup = scenario_authoring
   seed Keys (PP-690) + arc seeding. Detection never surfaces as a label.

## Q4 — Narratives present for the player (mechanisms; NLG lane owns the realizer)

1. **Slate injection = arcs become play.** game_director injects arc-tagged candidates into
   scene_slate (`player_agency §4` venue matrix). Every major arc holds ≥1 open intervention point
   until `converging` (lifecycle invariant: an `escalating` vector must carry ≥1 pending injection
   candidate) and routes through ≥1 playable scene (charter Q4, capstone #4 counter-case = a
   followed-only vector with no injection).
2. **Arc-vector payload IS the prose slot set (anti-oatmeal #1).** The realizer (NLG lane —
   `dossier_nlg_graduation.md`) consumes `participating_actors` → named actors, `direction` → causal
   sentence, `stakes_tags`+lifecycle terminal → outcome. Because these are per-vector DATA, the
   two-seed chronicle differs in named actors/stakes/outcomes (capstone #11): the difference is
   produced by the vector's per-seed `lifecycle` branch, and it is *verifiable* because vectors are
   data, not prose. This is the charter's anti-oatmeal #1 realized structurally.
3. **Trails = the `causes[]` walk as in-world media** (charter Q4); investigation (fieldwork) is the
   natural consumer. Requires the causes[] population Stage-3 wiring raises.
4. **Surfaces routed by salience:** Tier-1 ambient / Tier-2 cut scene (only interruption medium) /
   Tier-3 chronicle / texture — the §3.3 `unarticulated_weight` accumulator generalized to vectors
   (engine owns actor narrative weight) drives promotion/demotion; background is re-promotable.
5. **Anti-oatmeal #2/#3 (Expressive Range Analysis + arc_test_batch as NARRATIVE regression)** are
   bake gates on the realizer (NLG lane), but *fed* by arc-vector variety — the ERA range is the
   arc-vector participating-actor × lifecycle-branch space.

---

## Substrate contract

**States OWNED (engine):** the arc-vector store (lifecycle FSM state per vector — the generalized
per-arc lifecycle-state field, dossier §4.1 = ED-IN-0003 concrete form); actor narrative weight
(§3.3 accumulator generalized); convergence windows (the `temporal_window` evaluation state);
texture budgets. **READS:** clocks (`clock_registry_v30`), faction stats (`module_contracts` stat
fields), NPC state (`npc_behavior` — incl. the NPC-scoped `arc state` bucket at
`module_contracts.yaml:150`, which becomes a *specialization* the store reads, preserving holonic
containment: engine owns arc-vector state, reads NPC state).

**Keys IN:** subscription `consumes: [{type:"*", from: engine}]` (mirrors articulation,
`module_contracts.yaml:768`). Cadence tied to `propagation_spec_v1` ORD-3/ORD-4 (charter). Filtering
ladder: **trigger** (any live vector predicate reference this Key's type/target?) → **significance**
(meaningfulness test) → **accumulate** (unarticulated_weight) → **discard-with-reason**. Replay
determinism: same Key log → same arc-vector state (PP-687 §6 V4).

**Keys OUT — TOTAL ACCOUNTING:** the engine emits **ZERO new Key types** (C3). It emits only the
existing `mechanical.scene_entered/exited/skipped` (game_director, registered; consumer scene_timer
+ ordinary engines). Every Key touched is: **RENDERED** (scene played / chronicle), **ACCUMULATED**
(narrative weight), **CONSUMED-INTO-STATE** (arc-vector FSM write), or **DISCARDED-with-reason**
(noise backgrounded). The only new *registered artifact* is the `arc_vector` corpus — a data asset,
not a Key type — so the registry's "every emitted Key has ≥1 declared consumer" invariant is trivially
satisfied (no additions). **This Key-neutrality is Architecture B's cleanest property.**

**Six directions** (each on `propagation_spec_v1` ordering; determinism PP-687 §6 V4):
- **up** member outcome Keys aggregate → faction vectors (`domain_echo.py`, ORD-3).
- **down** faction-scope vector pressure → member-targeted slate injection.
- **lateral** NPC-ARC ↔ NPC-ARC convergence (same-scale COLLISION).
- **diagonal** TE territory vector recruits an NPC into a faction vector (cross-scale).
- **forwards** FSM transitions experienced as pressure/choices (present-moment).
- **backwards** chronicle `causes[]` walk (deterministic re-read, retrospect).

**Conformance (one CI rule each, living once in `tools/`):**
- C-1 every `trigger.field` resolves to a canonical clock/stat/track (catches ARC-T04 dangling-ID class).
- C-2 no vector references a STRUCK mechanic (catches Coup Counter, `dossier §4.2`).
- C-3 every convergence vector specifies `temporal_window` (not `unspecified`) — closes the
  register-wide gap (`dossier §6`, charter Q3).
- C-4 every scene-emitting injection populates `causes[]`/`targets[]` (total accounting; attacks 15%).
- C-5 every gating/foreclosure `stakes_tag` carries a `ledger_cause` (charter Q2).
- C-6 replay: same Key log → same store (PP-687 §6 V4).

---

## Staging

- **Stage 0 (Gate — scenario_authoring):** compile the register to typed vectors; resolve the 3
  corpus defects — Coup Counter→Autonomy remap, ARC-T04/Southernmost Ritual, TC→CI/RS→MS aliases
  (`dossier §4,7`). Ships the ~45% that compile now. Unblocks everything.
- **Stage 1 (game_director):** arc-vector store + lifecycle stepper; read-only over clocks. Unblocks
  autonomous progression (Q1 non-participation, Q2 world-affects-player).
- **Stage 2:** convergence detector over COLLISION vectors — **closes ED-IN-0003**. Needs the
  generalized lifecycle-state field (dossier §4.1) + a ratified `temporal_window` rule. Unblocks Q3
  emergence-vs-noise.
- **Stage 3:** slate-injection wiring (arc-vectors → scene_slate, riding `player_agency §4`) —
  **closes ED-IN-0004**; resolves scene_entered ownership. Unblocks Q1 participation, Q2 casting, Q4 present.
- **Stage 4:** casting resolver (tie-graph over `participating_actors`). Unblocks Q2 why-you.
- **Stage 5:** realizer bake (NLG lane) consuming arc-vector payload + chronicle `causes[]` walk.
  Unblocks Q4 surfaces, capstones #10/#11.

---

## Risks / cost (the honest tradeoff of data-driven arcs)

1. **Authoring becomes engineering, permanently.** Every future arc is a typed-vector authoring
   task, not prose. ~40% of the CURRENT register needs a new buildable field before it runs, and the
   GM-judgment-irreducible ~15% (ARC-P05 "GM rolls institutional tendencies"; ARC-S29 "most
   institutional friction" — `dossier §3,4`) need authored *decision functions* or they silently
   fail to fire. This is the central cost of Architecture B and the biggest maintenance burden.
2. **Scripting-drift hazard (C5 / holonic guardrail).** Authoring a decision function per
   judgment-arc invites special-casing an entity/outcome. Must stay a general rule (weighted-random
   or authored deterministic tie-break declared in schema), never a per-arc hack.
3. **`temporal_window` unspecified register-wide** (`dossier §6`) — convergence has no correlation
   window; charter Q3 names it as required. Blocks Stage 2 until Jordan rules (same-season /
   same-Accounting / N-season lookback). [OPEN — Jordan]
4. **Coup Counter migration** — 1:1 threshold remap onto Löwenritter Autonomy stages vs re-author
   against stage semantics (`dossier §4.2`, open Q). Blocks 5+ entries + COLLISION-F. [OPEN — Jordan]
5. **Per-arc lifecycle-state field ownership** — Class B extension of `npc_behavior` arc-state bucket
   (`module_contracts.yaml:150`) vs new game_director-owned store. I recommend game_director-owned
   (engine OWNS arc-vector state per substrate contract); NPC arc-state stays the NPC specialization
   it reads. [OPEN — Jordan]
6. **ARC-T04 / Southernmost Ritual is unauthored + mis-cited** (`dossier §4.3`): author fresh or
   strike the two stale cross-refs? Needs a fresh ED under the lane-tagged scheme (ED-WR/IN-####),
   as both ED-416 entries are unrelated. [OPEN — Jordan]

## Where data-driven arcs genuinely win

- **ED-IN-0003 + ED-IN-0004 close by construction** (C4): convergence detection and articulation
  triggering are just predicate-evaluation + injection over the store — no bespoke mechanism.
- **Anti-oatmeal #1 is structural, not aspirational:** per-vector `participating_actors`/`direction`
  guarantee two-seed chronicle divergence (capstone #11), and it is *checkable* because arcs are data.
- **Total-accounting is trivially clean:** zero new Key types; the engine is a consumer + state owner
  + injector, so capstone #9 (zero unaccounted Keys) holds by design.
- **The register already has the shape** (`01_arc_corpus.md §a`) — this is compilation, not invention,
  for ~45% of the corpus today.
