# Architecture C — The Director Layer (full working notes)

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
## Date: 2026-07-05 · Lane: IN · Author: arch-C director-layer lane

---

## 0. Thesis: the season scheduler is the spine, not a service

**Premise.** The organizing component of the emergent narrative engine is the **D11 pacing
director** (`articulation_layer_v30.md §7`, currently *deferred*). Everything else — convergence
detection (ED-IN-0003), per-arc lifecycle state, the prose realizer — is a **service the
scheduler calls**, not the spine. The spine is a **season-level scheduler** that owns a tension
curve, beat budgets, a salience economy (foreground/demotion), texture scheduling between scenes,
and slate booking.

**Why scheduling-first is the natural framing (not a stretch):**

1. **There is no GM (charter Premise).** What does a GM *do* turn to turn? Manages pacing:
   decides when to zoom in, what to foreground, when to grant a breather (texture), when to
   escalate. That is a *scheduling* function, not a detection function. Detection tells you a
   story exists; a GM decides whether to *spend a beat on it now*.
2. **The charter already names D11 as the pacing owner.** Q4 (charter L128-129): "director layer
   (articulation §7 D11) owns the tension curve." The charter hands this lane its mandate.
3. **The season scheduler already EXISTS in canon.** `player_agency_v30.md §4` is a deterministic
   season-level scheduler: 7-priority slate (§4.2), a hard 3-5 scene-action envelope (§4.3),
   Witness-Mode overflow (§4.2 Step 1, ED-761). Architecture C does **not** invent a new loop; it
   graduates §7's *deferral* into ownership of the arc-injection priorities *into* §4's slate and
   the tension curve that modulates §4.3's budgets.
4. **C3 says the engine "books venues, never owns resolution."** Architecture C takes *booking*
   literally as the spine: the director is a season-level **booking agent** owning a tension curve
   and beat budgets, booking arc beats into venues/slate slots. Detection and arc state feed the
   booking decision but are subordinate — they populate the candidate pool; the scheduler decides
   what makes the season's slate and at what tempo.

**What this buys structurally:** it *unifies the `game_director`/`scene_slate` ownership conflict*
(`module_contracts.yaml` L342-385, `mechanical.scene_entered` [OPEN — Jordan]). The booker
(director = `game_director`) owns the scene-**lifecycle** Keys and the season loop; the manifest
generator (`scene_slate`) owns the per-season **content** slate. Booking vs manifesting is a clean
seam that the registry's dual-emitter conflict currently lacks.

---

## 1. Q1 — Player affects world (mechanisms)

**Scheduling-first contribution to Q1 = the engagement-window GUARANTEE as a booking invariant.**

- Participation IS Key-emission (charter Q1); participated outcome Keys enter arc `causes[]`
  chains and aggregate up via **Domain Echo** (`scale_transitions_v30.md §5`, Sufficient Scope
  §7). The director does not own resolution (C3) — ordinary engines resolve the booked scene.
- **The director's job:** guarantee the *window* stays open. Charter Q4/C7: "every major arc keeps
  ≥1 open intervention point until converging." That is a **scheduling invariant**: while
  `arc.state ∈ {seeded, active, escalating}` and `arc.tier = major`, the director reserves ≥1
  slate-injection slot per N seasons for that arc. Rides `player_agency_v30.md §4.2` Step 2 (Crisis
  Events) + Step 6 (Territorial) as the injection channel, and §4.3's slate-size envelope as the
  budget it allocates against.
- **Non-participation as input (charter Q1, GD-3):** `player_agency_v30.md §4.4` is *already* the
  autonomous-resolution table ("what happens if the player does not attend" — NPC AI + clock
  advancement resolve it, "often in ways the player would not have chosen"). The director READS
  those unattended-resolution Keys and advances arc lifecycle state — never a pause. Repeatedly
  ignored arcs are **demoted** (salience economy) to texture, never dropped (total accounting).
- **Anti-railroad (C7):** pricing over gating — the director attaches an Obligation cost to
  *declining* a booked slot (`player_agency §4.4` already prices declines: Standing −1, Disposition
  −1, +1 Exposure) rather than forcing attendance. The ≥1-window guarantee supplies the
  *opportunity*, never the *obligation*. Seed-testable via the `arc_test_batch` 5-seed method
  (`tests/sim_framework/arc_test_batch{2,3,4}.py`, `SEEDS=[42,77,99,137,201]`): a different choice
  at the window measurably changes the arc's next lifecycle transition and the season tension
  trajectory (charter anti-railroad proof).

**Where scheduling-first risks over-orchestration (C7 railroad):** if the booking guarantee is a
*floor* ("every season must feature the current major arc") instead of a *ceiling*, it becomes a
railroad. Mitigation: the guarantee is **per-arc-until-converging window**, not
**per-season-attendance**; the foreground budget is a CEILING; Witness Mode (§4.2 Step 1) is the
pressure valve when mandatories exceed the envelope.

---

## 2. Q2 — World affects player (mechanisms)

**Scheduling-first contribution = casting-channel arbitration + impulsion cadence.**

- **Casting scheduling.** Charter Q2: ONE tie-graph rule drives every summons channel. The
  tie-graph rule itself lives in `player_agency §4` Steps 3-5 (Duty-aligned, Conviction-aligned via
  ED-746 keyword validator, NPC Outreach/Demand). The **director schedules** how many summons fire
  and in what order: it holds the NPC Outreach/Demand budget (charter Q2: ≤3/season) and the
  Mandatory-Crisis override ordering (`player_agency §4.2` Step 1 internal priority ordering,
  ED-761, 8-item table). Casting explains *why-you* diegetically because the slate entry carries
  its generating tie (`player_agency §4.2b`: each entry tags which Conviction/Duty/game-state
  condition generated it).
- **Position determines native story (charter Q2).** Leaders receive subordinate-originated beats:
  the NPC concern/project engine (`npc_behavior_v30 §5`, Concern queue `articulation §2.1`) points
  upward; the director books these as reports-as-scenes. Its scheduling role is the salience
  economy applied to Q2 *inputs*: rate-limit and prioritize which subordinate concerns surface as
  scenes (against the 3-5 envelope) vs which demote to texture (rumor/document). Anti-spreadsheet
  rule (charter Q2): named actors with wants — the concern queue already carries NPC identity +
  agenda, not report rows.
- **Impulsion (charter Q2):** pressure as choices with deadlines. The director owns the
  diegetic-clock cadence — it schedules forced-choice M-6 turns riding `scale_transitions §4.3.2`
  mandatory triggers + `player_agency §4.2` Step 1.
- **History conditions the option space — four modes (charter Q2).** The director is the
  gate/price/foreclose enforcement point at slate-generation time: **gating** = withhold a slot
  until a TS/Certainty/Coherence/Mandate/clock threshold (the §4.2 priority steps already read
  Standing/Disposition/clock thresholds); **pricing** (preferred) = attach an Obligation cost to a
  booked slot; **foreclosure** = remove an arc from the candidate pool permanently (budgeted to
  majors; Almud Arc-A exemplar), surfaced afterward in chronicle. Every gate cites its ledger cause
  (charter).

**Over-orchestration risk (C2 veto):** the salience economy must never surface as "this NPC was
demoted to background." Demotion manifests only diegetically — the concern becomes a rumor instead
of a summons. The foreground/background ledger is C2-internal.

---

## 3. Q3 — Events legible as narrative (mechanisms)

**Detection is SUBORDINATE but present — legibility is a BUDGETED decision, not an automatic
render.** This is the sharpest scheduling-first claim and the sharpest risk.

- **Convergence detector as a service (closes ED-IN-0003).** At the season boundary the director
  *calls* the detector, which runs the charter Q3 correlation tests (shared `targets[]`, `causes[]`
  overlap, temporal windows, same-direction pressure on a shared stake) over the arc-vector states
  and returns candidate convergences. **The detector rides an existing, sim-validated primitive:**
  `articulation_layer_v30.md §3.1` **trigger 9** — cosine similarity of
  `cascade_fidelity_history[-4:]` over a 4-season window, threshold ±0.40 (Stage 10 A6 calibration,
  corr +0.937 at the canonical Crown/Hafenmark pair). Architecture C **generalizes trigger 9 from
  faction-pairs to arc-vector pairs**: same cosine-over-temporal-window machinery, applied to arc
  pressure histories. This is the concrete detector ED-IN-0003 lacks, built from canon that already
  passed sim.
- **Meaningfulness gate as a budget filter.** The director decides which returned convergences
  *matter enough to book* against the foreground budget, via the charter Q3 meaningfulness test:
  durability × tie-proximity × identity-touch (changes who someone IS / what they OWE / what is
  POSSIBLE, for a tie-graph actor). Noise is explicitly backgrounded, never silently dropped
  (total accounting); false positives cost player trust.
- **Arc taxonomy + lifecycle state — director-OWNED.** The director owns the generalized per-arc
  lifecycle-state field for all ~110 register arcs (`references/arcs/`). The only such field that
  exists today (`module_contracts.yaml` L150 `arc state`, bucket: clock) is scoped ONLY to
  `npc_behavior` (T-23 NPC arcs — dossier "register-formalizability" finding 4.1); the director
  extends it to the ~100 faction/clock/territory/collision arcs that currently block COLLISION
  detection. States: seeded → active → escalating → converging → resolved/dormant/abandoned
  (charter Q3). Persistent, queryable — the substrate the salience economy operates over.
- **Salience economy (director-owned).** Foreground budget + promotion/demotion + background
  dignity. Rides `articulation §3.3`'s per-actor `unarticulated_weight` starvation accumulator,
  **generalized to arcs** (charter Q3 verbatim: "§3.3 accumulator generalized to arcs"). An arc
  going un-foregrounded accumulates weight; eventually a routine beat trips a higher-significance
  foreground. Background arcs stay re-promotable — the accumulator never zeroes them out of
  existence (background's dignity). **Concurrency budget per tier** (charter Q3): the director caps
  how many major/medium/minor arcs foreground at once — this IS the tension-curve mechanism
  (season tension = weighted Σ of foregrounded-arc stakes; scheduled against a target curve).

**Over-orchestration risk (doc-10 §8.5 NOT-list: "no designed dramatic timing"):** a target
tension curve, imposed too rigidly, manufactures timing the substrate didn't earn — violating the
emergence premise. Mitigation: the curve is a budget **CEILING** (how many beats may foreground),
never a **SCRIPT** (which beat fires when). The director never *creates* a beat; it only chooses
among beats the substrate already emitted. If no convergence is present, the season is quiet — the
director does not fabricate one.

---

## 4. Q4 — Narratives present for the player (the director's home turf)

Scheduling-first delivers **most genuinely** here; the charter names the director as tension-curve
owner (Q4 L128-129).

1. **Beat budget & pacing — the rationing articulation §3 lacks.** `articulation §7` states
   plainly that cut scenes currently "fire whenever triggers match" — *no rationing*. The director
   supplies it: it allocates the 3-5 scene-action envelope (`player_agency §4.3`, difficulty-scaled
   4-9 opportunities) across surfaces — how many Tier-2 cut scenes (`articulation §3`, "ONLY
   interruption medium, 5-15s, rationed" — charter Q4), how many slate (participating) scenes, how
   much texture. Beat qualification rides `articulation §3.2` significance (0-13, 5s/10s/15s tiers)
   + §3.3 accumulator (starvation floor).
2. **Texture scheduling between scenes — the immersion-audit gap.** (`02_prose_render_stack.md`
   (e)6; 2026-05-08 immersion audit.) The director schedules texture (rumor/overheard/documents)
   into inter-scene gaps for demoted/background arcs. **Texture is the demotion DESTINATION:** a
   demoted arc's beats don't vanish (total accounting) — they render as texture. Texture Keys route
   to the Tier-1 ambient lens (`articulation §2`, never modal).
3. **Watching-vs-participating ratio enforcement — a scheduling invariant.** Charter Q4: "every
   major arc keeps ≥1 open intervention point until converging and routes through ≥1 playable
   scene." The director tracks per-arc participated-beat count vs watched-beat count (Witness Mode
   ED-761, cut scenes, chronicle = watching; slate scenes + texture = participating). Invariant: a
   major arc cannot be all-watched before `converging` — the booking guarantee reserves ≥1 slate
   (participating) slot. CI-checkable (§6 conformance).
4. **Slate booking.** The director merges arc-injected candidates into `player_agency §4.2`'s slate
   — it is the arbiter that populates Steps 2/6 from the arc candidate pool.

**Over-orchestration risk (C2):** the tension curve must never surface (UI ceiling 3-4 trackers;
mechanical vocabulary never surfaces — charter Q4). Anti-oatmeal ERA is a *bake* gate, not a
runtime knob (dossier "content-economics"/"nlg-graduation"). The director's budgets are invisible
by construction.

---

## 5. Substrate contract

### 5.1 States OWNED (holonic containment — director owns these, reads everything else)

- **per-arc lifecycle-state field** {seeded, active, escalating, converging, resolved, dormant,
  abandoned} for all ~110 register arcs — the generalized ED-IN-0003 field (dossier finding 4.1;
  extends `module_contracts.yaml` L150 `arc state` beyond NPC scope).
- **per-arc accumulated narrative weight** — generalization of `articulation §3.3`
  `unarticulated_weight` from actors to arcs.
- **foreground/background salience ledger** — which arcs foregrounded this season; per-tier
  concurrency counts.
- **convergence-window state** — open convergence candidates from the detector, with temporal-
  window bounds (charter Q3 correlation dimension).
- **texture budget** — per-season texture-slot allocation.
- **tension-curve state** — target curve + current season tension = Σ foregrounded stakes.
- **watching/participating ratio counters** per arc.
- **the season scene-queue** — ORD-4 (`propagation_spec_v1.md` L118, L382): "scene-queue state
  belongs on World, not module scope … `scene_slate._queue`'s module-global fix." The director owns
  it **on World scope**, resolving the module-global determinism bug ORD-4 flags.

### 5.2 States READ

clocks (`clock_registry`), faction stats (`faction_behavior_v30`), NPC state (`npc_behavior_v30`),
arc-register DATA (`references/arcs/`), player Standing/Convictions/Obligations
(`player_agency_v30`), Coherence/Certainty (`threadwork_v30 §3.3`, `params/core.md`) for register
routing.

### 5.3 Keys IN (subscription model)

Subscribes to ALL Key emissions like `articulation §5` `on_key_emitted`. Filtering ladder
trigger → significance → accumulate → discard (charter substrate contract). Cadence tied to
`propagation_spec_v1` ORD-3/ORD-4. Replay-deterministic (same Key log → same narrative state,
PP-687 §6 V4). Specifically consumes: resolved-scene outcome Keys (`scene.*`), `mechanical.accounting`
(annual boundary), strategic Keys feeding arc triggers (`domain_actions`, `faction_politics`,
`peninsular_strain` per §12.4 down-seams), `meta.cascade_cluster_event` (existing convergence
primitive, `articulation §3.1` trigger 9).

### 5.4 Keys OUT — TOTAL ACCOUNTING

| Key | Disposition | Registry action |
|---|---|---|
| `mechanical.scene_entered` | RENDERED (booking) — **director owns it** | remove from `scene_slate.emits` (resolves conflict) |
| `mechanical.scene_exited` / `mechanical.scene_skipped` | RENDERED | already `game_director` per registry |
| `meta.arc_state_changed` (NEW Class B) | CONSUMED-INTO-STATE + RENDERED (chronicle) — the ED-IN-0003 *applier* output; C2: internal, never a surfaced label | ADD to `key_type_registry_v30`; consumers: articulation (chronicle), director |
| `meta.convergence_detected` (NEW Class B) | CONSUMED-INTO-STATE (booking) + causes[] walk; C2 internal | ADD to registry; consumers: director, articulation §4 chronicle |
| texture Keys | RENDERED (Tier-1 ambient) | route per `articulation §2` |

Per-class disposition of the subscribed stream: outcome `scene.*` → CONSUMED-INTO-STATE (advance
lifecycle) / ACCUMULATED (unarticulated weight) / DISCARDED-with-reason (meaningfulness fail);
strategic trigger Keys → CONSUMED-INTO-STATE; everything else → ACCUMULATED then DISCARDED per
ladder. **Nothing silent** (charter). Every emitted Key registered with ≥1 declared consumer whose
`consumes:` names it (charter); `targets[]`/`causes[]` populated per §12.3 discipline.

### 5.5 Edges (declared-vs-implemented, for the engine itself)

- director → `scene_slate`: books candidates into slate. Declared: `player_agency §4.2` Steps 2/6.
  Implemented: **GAP** (the injection point).
- director → `articulation §3`: supplies the *rationing* to cut-scene firing. Declared:
  `articulation §7` D11 deferral. Implemented: **GAP** (this is the D11 gap Architecture C closes).
- convergence detector → director: candidate convergences. Declared: ED-IN-0003. Implemented: GAP.
- director → chronicle (`articulation §4`): arc-resolution punctuation for the `causes[]` walk.
  Declared: charter Q3 PLOT "resolution = punctuation." Implemented: partial (chronicle exists;
  arc-resolution feed is new).

### 5.6 Six directions (each with ordering/determinism, per `scale_transitions §12.1`)

- **up:** participated scene outcome → arc state via Domain Echo (`§5`); observer order ORD-3.
- **down:** director books a strategic-arc beat onto a personal slate slot — it is literally a
  §12.4 down-seam emitter (`scenario_authoring → settlement_layer` is on the §12.4 list); must
  populate sub-scale `targets[]` per §12.3.
- **lateral:** peer/rival standing arcs, same-scale shared `scale_signature` (§12.1).
- **diagonal:** convergence = `causes[]`-chained cross-scale (Thread Echo §5.6 pattern); the
  detector operates on diagonal chains.
- **forwards:** lifecycle transitions advance (seeded→…→resolved) — experienced as pressure.
- **backwards:** chronicle + `causes[]` walk (`articulation §2.5`, §4) — recognized as story.

**Determinism:** the director's scheduling is a pure function of Key log + seed (PP-687 §6 V4;
replay re-executes `on_key_emitted` over KEY_LOG → identical state). **CONDITIONAL on ORD-3/ORD-4**
(`propagation_spec_v1` L112/L118): until ORD-4 lands (scene-queue on World), parallel replay is
non-deterministic — the director *inherits* this open precondition, it cannot rule it.

### 5.7 Conformance (CI rules, each living once in `tools/`)

1. **booking-guarantee**: every `tier=major` arc with `state ∈ {active, escalating}` has ≥1 slate
   injection within N seasons (C7 anti-railroad + Q4 intervention-point).
2. **watching/participating ratio**: no major arc is all-watched before `converging` (Q4).
3. **total-accounting linter**: every subscribed Key has a disposition tag (extends charter).
4. **C2 lint**: director-owned state (arc labels, tension curve, salience ledger, lifecycle
   names) never appears in any player-facing string (extends the NLG C2 literal-string lint,
   dossier "nlg-graduation").
5. **determinism**: director scheduling replays identically over a seeded batch (PP-687 §6 V4).
6. **scene_entered single-emitter**: only the director emits `mechanical.scene_entered` (resolves
   the registry conflict; a registry-consistency check).

---

## 6. Module contracts — homes claimed

Architecture C claims and *reorganizes* the doc:null cluster (`module_contracts.yaml`):

- **`game_director`** (L368-385) — CLAIMED as the director's home. New home doc:
  `designs/articulation/pacing_director_v1.md`, graduating `articulation §7` D11. `consumes:` now
  populated (all-Key subscription); `emits:` = the scene-lifecycle Keys + the two new `meta.*`.
  Resolves its doc:null.
- **`scene_slate`** (L342-366) — SUBORDINATE, stays a separate module. Ownership conflict resolves:
  `scene_slate` emits `scene.*` **content** Keys (combat_strike/dialogue/gift/insult/etc.);
  `game_director` emits scene-**lifecycle** Keys (`scene_entered/exited/skipped`). Remove
  `mechanical.scene_entered` from `scene_slate.emits`. Its "home doc unlocated" resolves to
  `player_agency §4.2` as the authoritative *generation* spec, with `pacing_director_v1` owning
  *arbitration/booking*.
- **`scenario_authoring`** (L744-760) — CLAIMED as a SIBLING seed module (= PP-690's never-authored
  home). Home doc: `scenario_authoring_v1.md`. Its authoring-time-vs-runtime [OPEN — Jordan]
  resolves: authoring-time bake freezes seed Keys into the campaign skeleton (C1 authored-only); the
  director schedules their *release* at runtime. The director consumes its `env.crisis`/`env.disaster`
  seed Keys as arc-seeding inputs (charter Q3 PLOT "setup").
- **`npc_memory`** (L177), **`scene_timer`** (L387) — NOT claimed; unchanged (memory feeds the
  concern queue; scene_timer stays an observability sidecar outside the Key log).

Net: ONE new runtime doc `pacing_director_v1.md` (season loop + tension curve + budgets + salience
economy + arc-lifecycle applier + convergence detector call), ONE new bake-side doc
`scenario_authoring_v1.md`.

---

## 7. Staging (build order + what each unblocks)

- **Stage 1 — Arc lifecycle field + applier** (closes ED-IN-0003 half): author the generalized
  per-arc lifecycle-state field for all ~110 register arcs (dossier "register-formalizability"
  schema). Unblocks: queryable arc state — everything downstream.
- **Stage 2 — Convergence detector as a service** (closes ED-IN-0003 other half): generalize
  `articulation §3.1` trigger-9 cosine-similarity from faction-pairs to arc-vector pairs; emit
  `meta.convergence_detected`. Unblocks: legibility budgeting (Q3).
- **Stage 3 — Director core**: tension curve + foreground budget + salience economy (generalize
  §3.3 accumulator to arcs) + scene-queue ownership (ORD-4). Unblocks: cut-scene rationing (Q4),
  `scene_entered` conflict resolution.
- **Stage 4 — Slate arbitration + booking guarantee + watching/participating enforcement**: wire
  director → `scene_slate` injection into `player_agency §4.2` Steps 2/6. Unblocks: engagement-
  window guarantee (Q1/C7), casting scheduling (Q2).
- **Stage 5 — Texture scheduler**: demotion destination; texture Keys → Tier-1 ambient. Unblocks:
  the immersion gap (Q4).
- **Stage 6 — Conformance suite + capstone trace**: the six §5.7 rules + ARC-S07 (Torben Loyalty
  Clock) compiled end-to-end (capstone req 10).

---

## 8. Risks

1. **Over-orchestration → railroad (C7).** Booking guarantee as *floor* not *ceiling* funnels every
   season into the current major. Mitigation: budget is a foreground CEILING; guarantee is
   per-arc-until-converging *window*, not per-season attendance; seed-testable.
2. **Designed dramatic timing (doc-10 §8.5 NOT-list).** A target tension curve manufactures timing
   the substrate didn't earn. Mitigation: curve is a budget over EXISTING beats; the director never
   creates a beat.
3. **C2 leak (highest-severity).** The director's *entire state* IS the narratological state the
   doc-12 veto forbids surfacing (tension curve, salience ledger, arc labels, lifecycle names).
   Mitigation: hard internal/external boundary + C2-lint conformance rule; demotion manifests only
   diegetically (summons → rumor).
4. **Determinism fragility.** Scheduling depends on ORD-3/ORD-4 (`propagation_spec_v1`, both OPEN).
   Until ORD-4 lands (scene-queue on World), parallel replay is non-deterministic. Inherited
   precondition, not director-rulable.
5. **Ownership-merge blast radius.** Claiming `game_director` + subordinating `scene_slate` + siding
   `scenario_authoring` touches three doc:null modules and the `mechanical.scene_entered` conflict —
   a Jordan ruling ([OPEN — Jordan]) the architecture proposes but cannot ratify.
6. **Scheduling-first buries emergence.** "Detection subordinate to scheduling" risks the budget
   starving genuine convergences (false negatives). Mitigation: the §3.3-generalized accumulator
   keeps background arcs re-promotable — no arc is permanently starved.

**Verdict.** Scheduling-first genuinely delivers Q4 (presence, cut-scene rationing, texture,
watching/participating ratio — the director's native turf, charter-named) and Q2 casting-channel
arbitration (≤3/season budget). It risks over-orchestration on Q3 (designed timing) and against the
C2 veto — the director's state is *inherently* the narratological state the veto forbids surfacing,
so the internal/external boundary is load-bearing and MUST be CI-enforced (§5.7 rule 4).
