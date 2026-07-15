# S5 — Worked Season Trace: ARC-S07, "The Torben Loyalty Clock"

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]

_The capstone deliverable. One major arc driven end-to-end through the six-layer Arc-Vector
Engine (synthesis §1), exhibiting all twelve charter capstones (`00_engine_charter.md:153-164`).
Every mechanism carries a working-tree cite; genuine forks are tagged `[OPEN — Jordan]` with a
default; adversarial-review fixes are applied inline and flagged in the determinism sidebars._

---

## S5.0 How to read this trace

**The arc.** ARC-S07 "Torben Loyalty Clock" (`references/arcs/arc_register_factions.md:10-11`):
Altonian institutional pressure (the IP clock) extorts the Crown into sending its heir Torben
abroad for "tutoring"; once abroad, his Loyalty degrades unless covertly maintained, and a lost
heir cascades into the succession, the coup chain, and the Crown's Mandate. Its register
Direction sentence — _"Altonian pressure converts the heir into a lever against the dynasty"_ —
is the realizer's slot source (S5.1). The full decision tree and three endings (retrieved /
Altonian / dead) are hand-authored at `tests/sim/sim_arc_01_irrational_player_arcs.md:24-84`.

**The illustrative PC.** "Ser Halden" — a Crown household agent, former sword-tutor to Torben,
Bonded to Torben, holding a Duty to the Crown. The name and person are illustrative, **not a
canon NPC** [UNGROUNDED — a trace vehicle]; the load-bearing, grounded part is the pair of
tie-graph edges `Bond(Halden, Torben)` + `Duty(Halden, Crown)`, which is what the casting
resolver matches (S5 Beat 1.2, capstone #2).

**Beat schema.** Each beat is reported as the charter's row shape:
`{ Keys in · engine state change · casting/venue · player choice + alternatives · Keys out +
accounting class · surface rendered + register }`, followed by a **determinism sidebar** where an
adversarial fix binds.

**Register annotation.** Every rendered surface carries the NLG bake key
(`dossier_nlg_graduation`): `{ significance-band, coherence-band, ts-band, spirit, certainty-
register, focalizer }`. Coherence bands per `threadwork_v30 §3.3` / `references/coherence-tiers.md`;
Certainty registers per `solmund_voice_v30 §18`; chroniclers carry FIXED Cert/TS pairs
(`prose-writer/SKILL.md:151`: Church Cert-5/TS0, Hafenmark Cert-4/TS0, Restoration Cert-2/TS0,
Warden Cert-0/TS70+).

**Accounting classes** (charter `:143-145`, "TOTAL ACCOUNTING"): every Key touched is exactly one
of **RENDERED** / **ACCUMULATED** / **CONSUMED-INTO-STATE** / **DISCARDED-with-reason** — nothing
silent. Tallied in S5.4.

The trace covers one campaign year, four seasons (arc shape "3–4 seasons",
`sim_arc_01:78`), closing at the year-end omniscient chronicle (`articulation_layer_v30 §2`
Tier-3). The **spine** taken is the partial-failure branch (Loyalty reaches 3 by Autumn) because
it exercises convergence, the coup chain, and foreclosure; the **success** branch is carried in
the divergence table (S5.3, capstone #3) and the seed-42 sketch (S5.6, capstone #11).

---

## S5.1 The compiled `arc_vector` for ARC-S07 (capstone #10 — typed vector + template slots)

This is the L0 compile output (synthesis §2), the frozen typed asset the runtime store reads.
Fields trace 1:1 to the register prose at `arc_register_factions.md:10-11`.

```yaml
arc_vector:
  id: ARC-S07
  title: "Torben Loyalty Clock"
  tier: S                              # standing / slow-burn (01_arc_corpus §a)
  scope: { faction: Crown, territories: ALL, mode: ALL }
  activity_mode: clock_escalation      # the Loyalty track ticks -1/season on contact fail
  trigger:
    predicate:
      - { field: clock.IP, op: ">=", value: 30 }          # IP 30 -> Tutoring Demand
    resolves_via: null                  # the TRIGGER is a clock-threshold READ (IP>=30 via state_reader),
                                        #  NOT a contest. dice_pool belongs to the Covert-Contact
                                        #  pressure-effect CONDITION below (Intel vs Ob 3), not the trigger.
                                        #  Agrees with s2 §Q3.10.
    temporal_window: same-Accounting    # [OPEN - Jordan] fork 3; general convergence uses 4-season cosine
  pressure_effects:
    - { target: track.Torben_Loyalty, delta: -1, cadence: per_season,
        condition: "Covert Contact (Intel vs Ob 3) FAILS this season" }
    - { target: track.Torben_Loyalty, delta: "floor 6", cadence: once,
        condition: "3 consecutive successful contacts" }
    - { target: track.Lowenritter_Autonomy, delta: +1, cadence: edge_once,
        condition: "Torben_Loyalty <= 3" }               # [OPEN - Jordan] fork 1: was Coup Counter +1
    - { target: stat.Crown_Mandate, delta: -2, cadence: cumulative,
        condition: "Torben_Loyalty <= 2" }
  payload:
    direction: "Altonian pressure converts the heir into a lever against the dynasty."
    participating_actors: [Torben, Almud, Elske, Laskaris, Baralta, Ehrenwall]
      # +Baralta: grounded ARC-S07 edge — ARC-S45 "Deed Claim Activates" triggers on Torben Loyalty <= 3
      #  (arc_register_factions.md:38). -Himmensendt: NO ARC-S07 edge (his arcs are Church consecration/
      #  suppression, arc_register_factions.md:103-118 — not tied to the Torben Loyalty clock). Agrees
      #  with s2 §Q3.10 participating_actors.
    stakes_tags: [pricing, foreclosure]  # extraction is PRICED; Altonian-oath is FORECLOSURE
    ledger_cause: { citation: "PP-498 (Torben track, params_board_game.md §Torben; clock_registry_v30.md:27)",
                    gate_of: retrieve_as_loyal_heir,
                    cause: "Torben_Loyalty <= 2 AND Crown_Mandate -2 cumulative" }
  lifecycle:
    state: seeded                        # seeded -> active -> escalating -> converging -> resolved
    terminal: false
  cross_refs: [ARC-S20, ARC-T02, ARC-T13, ARC-S35, NPC-ARC-LAK, COLLISION-C]
    # NPC-ARC-LAK is the SINGLE home for the Laskaris IP+3 flip (Elske Loyalty <= 2). It is carried
    #  HERE as a cross_ref, NOT as an ARC-S07 pressure_effect — ARC-S07 does not write clock.IP; it
    #  feeds the flip's condition. Agrees with s2 §Q3.10 (fix 8). See Beat 4.2 footnote.
  gaps:
    - { type: struck_mechanic, note: "Coup Counter STRUCK (ED-781); remap to Lowenritter Autonomy",
        cites: "params/factions_personal.md; synthesis fork 1" }         # [OPEN - Jordan]
    - { type: dangling_id, note: "COLLISION-C constituent ARC-T04 is dangling; marker non-firing",
        cites: "arc_register_events.md:37-39; synthesis fork 2" }        # [OPEN - Jordan]
    - { type: open_number,
        note: "Torben Loyalty RANGE CONFLICT: the register and sim use start-8 (8->0,
          arc_register_factions.md:11, sim_arc_01:64) but clock_registry_v30.md:27 is canonical 0-7
          start-3. THIS TRACE DEPENDS ON start-8 (Beat 2.1 opens at Loyalty 8). Not silently harmonized.",
        cites: "arc_register_factions.md:11; clock_registry_v30.md:27; tests/sim/sim_arc_01_irrational_player_arcs.md:64" }
        # [OPEN - Jordan: register vs clock_registry range conflict]
```

**Template slots** (the realizer's L5 fragment schema, riding existing Key metadata only —
`causes[]`, `targets[].role`, `symbolic_dimensions`, `significance`, `awareness`; no new Key
fields, per synthesis §6):

| Slot | Type | Bound from | Example fill (spine) |
|---|---|---|---|
| `{heir}` | entity_name | `targets[].actor_id` where role=subject | "Torben" |
| `{sovereign}` | entity_name | scope.faction leader | "King Almud" |
| `{foreign_power}` | place/faction | payload actor (Altonia) | "Altonia" |
| `{lever_phrase}` | axis_label | payload.direction | "a lever against the dynasty" |
| `{loyalty_state}` | stat_delta_phrase | `track.Torben_Loyalty` band → qualitative | "his letters have gone cold" (Loyalty 3) |
| `{cause_connective}` | causal_connective | `causes[]` walk | "because the tutoring demand was never refused" |
| `{chronicler_voice}` | chronicler_voice_tag | focalizer | Restoration Cert-2 / Church Cert-5 |

Per C4, every slot resolves to **qualitative/named** output, never a raw ID or number ("his
letters have gone cold," never "Loyalty −1"; charter `:131`).

**Compile status** (dossier_register_formalizability): ARC-S07 is in the **~40% compile-with-one-
new-field** bucket — everything types except the generalized `lifecycle.state` field (the concrete
form of ED-IN-0003, synthesis fork 5) and the two forks above. It does not need a GM decision
function, so it is not in the ~15% judgment-irreducible bucket.

---

## S5.2 Season timeline

### SEASON 1 — SPRING · Seed + Casting

#### Beat 1.1 — The Tutoring Demand (LEADER beat, subordinate-originated; capstone #5a, #2)

- **Keys in.** `clock.IP` reaches 30 (a **global clock**, `scale_transitions_v30 §4.3.3`,
  aggregating bottom-up from Altonian trade pressure — the §12.1 bottom-up row / §5 Domain Echo
  path feeds faction stats; the IP *clock* itself is READ, not a Domain Echo output). The
  IP-30 crossing fires the Tutoring Demand, a strategic Key that names sub-scale targets per §12.3 (Torben,
  Almud, Laskaris in `targets[]`).
- **Engine state change.** ARC-S07 lifecycle `seeded → active`; the Tutoring Demand fires
  (`edge_triggered_once`). **Laskaris (PROTECTIVE) delays the demand one season**
  (`arc_register_factions.md:11`) — recorded as a `pressure_effects` deferral, not a player pause.
- **Casting / venue.** This is a **leader beat**: the subordinate-originated demand hunts **King
  Almud** as `target` (Q2 "politics Keys hunt the leader as target", charter `:64`). Cast because
  `scope.faction = Crown` and Almud is its leader — the tie-graph position edge. Almud is a
  co-protagonist (one ledger, Q3), so this renders as a **Tier-2 cut scene** the PC *watches*, at
  the **Crown court, T1** (venue: settlement governance event, charter venue matrix `:113-116`).
- **Player choice.** None — Halden is not yet cast; he witnesses (witness-presence casting hook,
  charter `:61`, carried to Beat 1.2).
- **Keys out + accounting.**
  - `meta.arc_state_changed` (seeded→active) — **CONSUMED-INTO-STATE** (Class B, C2-internal).
  - `state.tutoring_demand` **[TRACE-ILLUSTRATIVE]** — **RENDERED** (Tier-2 cut scene). This is an
    illustrative Key NAME for the trace, not a registered `key_type_registry_v30` type; the render
    fires off the demand's *existing* strategic-Key emission, and Stage-0 §3.1 does **not** add a
    `state.tutoring_demand` trigger (do not read this as a Stage-0 deliverable).
  - `env.crisis` seed Key (from `scenario_authoring`, `arc_register_events` BG lineage) —
    **CONSUMED-INTO-STATE** (triggers the lifecycle transition).
  - `env.trade_tariff_fluctuation` in T16 (routine seasonal noise) — **DISCARDED-with-reason:
    `meaningfulness_below_threshold`**, backgrounded to Tier-1 texture as a market rumor
    (capstone #8 FAIL case — see S5.2 meaningfulness note).
- **Surface + register.** Tier-2 cut scene. `{ significance: 10s (stakes 4 + protagonist_align 2,
  per articulation §3.2), coherence: 7–5 Dissonant, ts: 0–29, spirit: n/a (>4), certainty: n/a
  (non-ecclesiastical), focalizer: protagonist }`. The render rides an **existing** §3.1 render
  trigger on the demand's strategic Key (the ED-IN-0004 render-gap close is about the *combat/
  investigation/thread* beats, E9–E11 in s4 §S4.6); the `state.tutoring_demand` label above is
  **[TRACE-ILLUSTRATIVE]** and is NOT claimed as a Stage-0 §3.1 additive trigger.

**Meaningfulness note (capstone #8).** Test = durability × tie-proximity × identity-touch
(charter Q3 `:83-88`; synthesis §3). The **tariff fluctuation FAILS**: it moves no slow variable,
touches no `participating_actor`'s Belief/Conviction/Scar/Obligation, closes no possibility →
score below threshold → texture, never a scene. The demand **PASSES** (moves the succession, ties
to Torben the Bond, touches what is possible for the dynasty). Both are *accounted*: neither is
silently dropped.

#### Beat 1.2 — Halden is called (MEMBER beat, duty-assigned; capstone #2 why-you, #5b, Q2 casting)

- **Keys in.** `game_director` injection request: ARC-S07 (now `active`) needs a covert-contact
  channel and reads `payload.participating_actors` + the tie-graph.
- **Engine state change.** The casting resolver (L4) matches ONE tie-graph rule
  (Duty/Conviction/Bonds/lifepath/Standing/position, charter Q2 `:58-61`): `Bond(Halden, Torben)`
  ∧ `Duty(Halden, Crown)` are the strongest edges to `participating_actors` → Halden is cast.
- **Casting / venue.** **Why-you, diegetic:** _"You taught the boy to hold a sword. The King
  trusts a face Torben already knows."_ The matched edge IS the explanation (charter `:61`, "why
  you, diegetically"). Venue: a **private audience / Bond scene at T1** (Knot/Bond venue,
  charter `:116`) — a **slate scene** (participating).
- **Player choice.** Accept the covert-contact commission (Duty-with-refusal-cost) / decline
  (refusal cost: a Duty strain Key, remembered, never a pause — Q1 `:49-54`).
  **Alternatives are real**: decline routes the Season-2 contact through an NPC agent instead,
  and Halden's non-participation becomes an input (the arc still ticks).
- **Keys out + accounting.**
  - `mechanical.scene_entered` — **RENDERED**; single-sourced from `game_director`
    ([OPEN — Jordan] O-1; see S5.7).
  - `scene.dialogue` (the audience) — **RENDERED** (played slate scene). Emitted by `scene_slate`
    as CONTENT only (synthesis §5).
  - `state.obligation_incurred` (Halden now owes the Crown a delivered duty) — **ACCUMULATED**
    into the ledger-of-you (Q1 `:51`); this becomes the **pricing** currency in Beat 4.1.
- **Surface + register.** `{ significance: 10s, coherence: 7–5, ts: 0–29, spirit: n/a, certainty:
  n/a, focalizer: protagonist }`.

---

### SEASON 2 — SUMMER · The played contact + the player-shaped branch (capstone #3, #6, #7)

#### Beat 2.1 — Covert Contact (the engagement window)

- **Keys in.** Season tick; ARC-S07 `active`, Loyalty at 8 (departure set the clock,
  `sim_arc_01:64`). The season's Covert Contact check is due (Intel vs **Ob 3**,
  `arc_register_factions.md:11`).
- **Engine state change.** Resolves through the **ordinary fieldwork engine** (C3 — the engine
  books the venue, never owns resolution). Outcome writes `track.Torben_Loyalty`.
- **Casting / venue.** **Fieldwork trail / case-board** at **T16 (Altonia-adjacent)** — an Intel
  operation (charter venue matrix, "fieldwork trails/case board" `:116`).
- **Player choice + alternatives** (all diegetic, each citing a ledger cause — Q2 `:73-79`):
  1. **Covert channel** (spend 1 Momentum, Circles Ob 3 → Intel vs Ob 3). The intended play.
  2. **Direct negotiation with Altonia** — **PRICED, not walled** (capstone #6 PRICED): available,
     but exposes Halden as a foreign operative → `Altonian_Intel +1` + a Standing hit, and
     *accelerates* Torben's departure (the IP-B structural-failure branch, `sim_arc_01:60-62,82`).
     **Ledger cause cited:** Standing / foreign-operative exposure. Priced, per C7 "Obligations
     price betrayal, don't wall it."
  3. **Formal Crown Treaty** (resolve diplomatically) — **GATED** (capstone #6 GATED): greyed,
     requires **Altonian diplomacy ≥ 4** (ARC-T17, `arc_register_factions.md:46-47`). Halden's
     Crown lacks the diplomacy standing. **Ledger cause cited:** Altonian diplomacy track < 4.
  4. **Refuse / ignore** — non-participation input; the clock ticks −1 anyway (Q1 `:49-54`).
- **Keys out + accounting.**
  - `scene.investigation_resolved` — **RENDERED** (played; a new §3.1 trigger from Stage-0).
  - `da.covert_contact{outcome}` — **CONSUMED-INTO-STATE**: writes the Loyalty delta and enters
    ARC-S07's `causes[]` (Q1 `:45-48`, "outcome Keys enter the arc's causes[] chain").
  - `meta.arc_state_changed` (if the outcome flips a lifecycle edge) — **CONSUMED-INTO-STATE**.
    _(Conditional, off-spine: this Key fires only on the outcome classes that cross a lifecycle edge —
    e.g. fail→`escalating`; a hold that merely maintains `active` emits none. Not dropped: it is
    absent by branch, and the S5.4 table rows it as the branch-conditional it is.)_
- **Surface + register.** `{ significance: 10s, coherence: 7–5, ts: 0–29, focalizer: protagonist }`.

**The player-shaped branch (capstone #3).** The outcome of *this participated scene* changes
ARC-S07's next lifecycle state — proven by the divergence table S5.3. Two participated-outcome
classes map to **two distinct next `lifecycle.state`s** (holds → `active`/floors at 6 vs fails →
`escalating`), satisfying the **engagement-window-divergence** conformance rule (S5.7 R7).

> **Determinism sidebar — the dice outcome is not the nondeterminism hazard.** The contest resolves
> through the ordinary fieldwork engine on the seeded stream; replay is fine. The hazard the review
> flags lives at Beat 3.2 (float convergence), not here.

---

### SEASON 3 — AUTUMN · Escalation, convergence detection, the followed-only arc

_Spine assumption: the Season-2 contact partially failed (Loyalty 8 → … → 3 by Accounting). The
success branch is S5.3 / S5.6._

#### Beat 3.1 — Loyalty crosses ≤ 3 (escalation; capstone #6 groundwork, fork 1)

- **Keys in.** Season tick; cumulative contact failures put `track.Torben_Loyalty = 3`.
- **Engine state change.** ARC-S07 `active → escalating`. Loyalty ≤ 3 fires
  `track.Lowenritter_Autonomy +1` — **the Coup Counter remap** ([OPEN — Jordan] fork 1;
  **default: 1:1 threshold remap** onto the Löwenritter Autonomy 4-stage track, since the numeric
  Coup Counter is STRUCK, ED-781; `arc_register_factions.md:19-20` ARC-S20 is the chain this
  feeds). This is a **`clock_escalation`** transition — a *passive* crossing.
- **Casting / venue.** No player scene is forced here; it renders as a Tier-2 cut scene of
  Torben's deepening distance, at **T16**, plus a chronicle line. Venue: cut scene AT T16 /
  chronicle.
- **Keys out + accounting.**
  - `meta.arc_state_changed` (active→escalating) — **CONSUMED-INTO-STATE**.
  - `state.autonomy_increment` **[TRACE-ILLUSTRATIVE]** — **ACCUMULATED** (feeds ARC-S20's coup
    chain; this arc→arc feed is **bottom-up substrate delivery (§12.1)**, NOT Domain Echo — "Domain
    Echo" is reserved for the scene→faction cases of §5, per verifier N2).
  - Tier-2 cut scene Key — **RENDERED**.
- **Register.** `{ significance: 10s, coherence: 7–5 → 4–3 as strain rises, ts: 0–29, spirit:
  audible if coherence ≤4 (High → Beckett; Low → Lispector, `02_prose_render_stack.md:18-20`),
  focalizer: protagonist }`.

> **Determinism / C7 sidebar — a passive clock must NOT foreclose here.** Per the foreclosure fix
> (S5.7 R9), `clock_escalation`/`level_triggered` transitions may **never** carry a
> `stakes_tags:[foreclosure]` transition. The Loyalty≤3 crossing raises the *possibility* of
> foreclosure but does not execute it; foreclosure fires only through the **edge-triggered** arc
> event at Beat 4.2. This preserves "foreclosure via arc events only, never silent" (C7, charter
> `:41,77`).

#### Beat 3.2 — Convergence detection (capstone #1 convergence; Q3 emergence-vs-noise)

Two things happen at the **ACCOUNTING_BOUNDARY** (synthesis §3), and BOTH are accounted:

**(i) The register-authored marker COLLISION-C does NOT fire — DISCARDED with reason.**
COLLISION-C (Tutoring + Southernmost, `arc_register_events.md:37-39`) requires `Torben Loyalty ≤ 3`
(satisfied) **coinciding with** the Southernmost Ritual failure (ARC-T04). But **ARC-T04 is a
dangling ID** (defined in no register file; synthesis fork 2). Under the **default (strike the
stale cross-refs)**, COLLISION-C's predicate cannot resolve → the marker is **DISCARDED-with-
reason: `predicate_unresolvable(dangling_id: ARC-T04)`** — logged, never silent (total accounting;
conformance R1 `predicate-field-resolves`). `[OPEN — Jordan]` fork 2 (author ARC-T04 fresh vs
strike; default = strike, COLLISION-C becomes a 1-of-2 degenerate marker).

**(ii) The general cosine backbone detects a REAL convergence — RENDERED.**
The detector's second tier (synthesis §3, generalizing `articulation_layer_v30 §3.1 trigger-9`,
`:94-110`) finds ARC-S07 and **ARC-S20 (Ehrenwall's Count)** correlated: same-direction pressure
on a shared stake (the succession / the Autonomy track), shared `targets[]` (Torben, Crown, the
Löwenritter). This is the charter-Q3 correlation test (shared targets, causes[] overlap, temporal
window, same-direction pressure on a shared stake, `:86-88`) — and it is genuine *emergence*, not
one of the 8 hand-authored whitelist conjunctions.

- **Casting / venue (ambient location, N5).** No forced scene. The convergence renders as a Tier-2
  cut scene **at the T1 Crown court** — the ambient location where the succession/Autonomy pressure is
  legible (the two crises "rhyme" in the same room the dynasty governs) — plus a chronicle line. No
  modal popup: the beat renders AT a place (charter venue rule `:116`).
- **Keys out + accounting.**
  - `meta.convergence_detected{pair: [ARC-S07, ARC-S20], kind: cosine}` — **RENDERED** (Tier-2
    cut scene + chronicle) and feeds the `causes[]` walk (Class B, C2-internal — the label
    "convergence" **never surfaces**; the player sees two crises that rhyme, not "Convergence
    Marker fired").
- **Register.** `{ significance: 15s (stakes 5 + cascade 2), coherence: 4–3 Fragmented, ts: 0–29,
  spirit: audible, focalizer: protagonist }`.

> **Determinism sidebar — three fixes bind here (mandatory, R-rules S5.7).**
> 1. **Anti-fabrication (R5).** The cosine-detected ARC-S07↔ARC-S20 convergence is **outside the
>    register-authored set**, so it is **RENDER/CHRONICLE-ONLY with zero `pressure_effects`**. It
>    changes what the player *sees and can trace*, not the mechanical state. Combined-pressure
>    deltas (e.g. COLLISION-C's authored "RS +8, IP +2, TC +2", `arc_register_events.md:39`) exist
>    ONLY for register-authored convergence vectors, and every such delta must trace to a register
>    line (conformance R5). Wiring a cosine hit to a fabricated delta would violate CLAUDE.md §5/§7
>    anti-fabrication — forbidden.
> 2. **Emit-order (R-ORD).** Detected convergences are deduped by an **order-preserving container
>    keyed by `(conjunction_id, sorted(participating_actor_ids), season_index)`** and sorted before
>    the emit loop — **never a bare `set()`** (which would be a live ORD-2 violation per
>    `propagation_spec_v1 O.3/O.6`; the READ-side sidestep at the Accounting boundary does not
>    absolve the detector's own emit order).
> 3. **Cross-oracle float (R-FP).** The cosine comparison `abs(sim) > 0.40`
>    (`articulation_layer_v30:101`) is **quantized to a fixed-point integer grid and compared as
>    integers**, with the summation order canonicalized (sort terms by `actor_id`) and a published
>    epsilon-band conservative-tie rule; the GDScript port pins identical arithmetic and joins the
>    key-log parity harness (same failure class as the ED-1050 `adef_threshold` port divergence,
>    CLAUDE.md §6). The value **0.40 is `[OPEN — Jordan tuning]`**; the *arithmetic determinism* is
>    structure and is ruled regardless. NB the +0.937 validation was ONE faction pair over 30
>    seasons (`articulation_layer_v30:112`) — generalizing to ~110 arc-vectors is O(N²) boundary
>    coin-flips, which is exactly why quantization is mandatory, not optional.

#### Beat 3.3 — The followed-only arc (capstone #4; capstone #8 PASS case)

- **Keys in.** ARC-T02 (Almud's Belief crisis, `arc_register_factions.md:40-41`) runs in parallel
  from the same IP-30 trigger — Belief 1 (Altonian trade) vs Belief 3 (ethical doubt) collide.
- **Engine state change.** ARC-T02 ticks autonomously; no player Key is consumed (Q1
  non-participation — "FSM steps with zero player Keys", synthesis L1).
- **Casting / venue (ambient location, N5).** **Followed-only**: the PC is NOT in ARC-T02's
  `participating_actors` as a playable role, and the salience budget routes it to **spectator channels
  only** — a **Tier-2 cut scene of Almud alone at the T1 Crown court** (his private chambers / the
  chapel-adjacent study where his Belief crisis plays out) + a chronicle line. **No slate scene, no
  casting hook consumed.** Watching, not participating (charter `:118-121`); the beat still renders AT a
  named place (`:116`).
- **Keys out + accounting.**
  - `state.belief_revised{actor: Almud}` — **RENDERED** (articulation §3.1 trigger 10,
    `articulation_layer_v30:92`, sig=7 mid-tier).
  - Tier-2 cut scene Key — **RENDERED**.
- **Register.** `{ significance: 10s, coherence: 7–5 (Almud is high-function), ts: 0–29,
  certainty: **register applies** — Almud's Belief crisis is ecclesiastical-adjacent → Cert 3
  "faith-as-habit" per `solmund_voice_v30 §18`, focalizer: protagonist-watching }`.

**Meaningfulness note (capstone #8 PASS).** `state.belief_revised{Almud}` **PASSES** the test:
durability (moves the Belief slow variable), tie-proximity (Almud is Torben's father, a tie-graph
actor one edge from the PC's Bond), identity-touch (Belief/Conviction). Contrast Beat 1.1's tariff
(FAILS). The trace thus shows one beat passing and one context event failing, both accounted.

---

### SEASON 4 — WINTER · Resolution, foreclosure, chronicle echo

#### Beat 4.1 — The last intervention window (watching/participating invariant; capstone #6 PRICED)

- **Keys in.** ARC-S07 `escalating`; the FSM is one tick from `converging`. Per the
  **watching/participating invariant** (charter Q4 `:120-121`; conformance R6), a major arc keeps
  **≥1 open intervention point until converging**.
- **Engine state change.** A final slate scene is **OFFERED**: covert extraction of Torben.
- **Casting / venue.** Cast on `Bond(Halden, Torben)`. Venue: a **covert extraction** — an Intel
  op resolving through the personal-combat / infiltration engine (charter venue matrix, "combat
  duels" / "witness mode" `:116-119`) at **T16**. A **slate scene** (participating).
- **Player choice + alternatives.**
  1. **Extract** — **PRICED** (capstone #6): costs the `state.obligation_incurred` to the Crown
     accrued in Beat 1.2 *plus* a new Obligation to Laskaris and a Standing risk (extraction is a
     covert Military/Intel action, `sim_arc_01:67`). **Ledger cause cited:** Obligation + Standing.
  2. **Let it resolve** — non-participation; the FSM converges regardless.
- **Keys out + accounting.**
  - `mechanical.scene_entered` (if extract) — **RENDERED** (game_director single-source, O-1).
  - `scene.combat_strike` / `scene.witness` — **RENDERED** (played or watched).
  - `state.obligation_discharged`/`incurred` — **ACCUMULATED**.

> **C7 / rubber-band sidebar (R6, offer-not-outcome).** The invariant is satisfied by the window
> having been **OFFERED**, NOT taken. The FSM advances on schedule regardless of participation — an
> all-ignored major arc still converges on time and passes CI (which counts *offered* windows, never
> *taken* windows). This reconciles Q4's "keep ≥1 open intervention point" with Q1's "arcs proceed
> autonomously; ignoring a summons is never a pause" (charter `:49-54`, `:120-121`). No arc is ever
> held waiting for the player.

#### Beat 4.2 — Foreclosure: Torben swears the Altonian oath (capstone #6 FORECLOSED)

- **Keys in.** Extraction failed / declined; `track.Torben_Loyalty = 2`, and `Crown_Mandate −2`
  cumulative has crossed (`arc_register_factions.md:11`).
- **Engine state change.** An **EDGE-TRIGGERED arc event** fires — `state.altonian_oath_sworn`
  **[TRACE-ILLUSTRATIVE]** (an illustrative Key name, not a registered type) — the "Torben Altonian"
  ending (`sim_arc_01:37,68`). This **permanently forecloses** the
  `retrieve_as_loyal_heir` path (`payload.ledger_cause`). It also fires `Crown_Mandate −2`
  (Domain Echo aggregate-up, §5), feeding **ARC-S35 Succession Vacuum** (`:31-32`) and promoting
  **Elske** as the only viable heir (`sim_arc_01:68`), and it may flip **Laskaris** (NPC-ARC-LAK,
  `:312-313`, IP +3) if Elske Loyalty ≤ 2.
  _(Conditional, off-spine: the Laskaris IP+3 is **NPC-ARC-LAK's own** pressure_effect fired on its own
  condition — carried as an ARC-S07 cross_ref, never an ARC-S07 pressure_effect (S5.1 note, fix 8/13).
  It fires only if Elske Loyalty ≤ 2; on the traced spine Elske is promoted but not yet ≤ 2, so it is
  off-spine, not dropped.)_
- **Casting / venue.** **Chronicle (Tier-3, mandatory)** + a final Tier-2 cut scene at T16.
- **Keys out + accounting.**
  - `state.altonian_oath_sworn` — **RENDERED** (mandatory Tier-3 chronicle beat, see sidebar) +
    **CONSUMED-INTO-STATE** (forecloses the path, applies Mandate −2).
  - `meta.arc_state_changed` — **CONSUMED-INTO-STATE**.
- **Register.** Chronicle voice, chronicler-selected: **Restoration chronicler (Cert-2, TS0)** if
  the Restoration is present, else **Church (Cert-5)** — the fixed pairs at `prose-writer/SKILL.md:151`.
  `{ significance: 15s→chronicle-paragraph, coherence: PC's live band, ts: chronicler's, spirit:
  n/a in retrospect, certainty: chronicler-fixed, focalizer: chronicler }`.

> **C7 foreclosure sidebar (R9, mandatory-render).** Two rules bind: **(a)** the foreclosure fires
> via an **edge-triggered arc event**, never the passive Loyalty clock crossing of Beat 3.1 — the
> clock raised the possibility, the *event* executes it (charter "via arc events only" `:77`).
> **(b)** every `stakes_tags:[foreclosure]` transition **MUST emit a Tier-3 chronicle beat** — a
> *positive surfacing* check, distinct from discard-with-reason logging. "Surfaced afterward in
> chronicle" (charter `:78`) is thereby a *rendered* guarantee, not merely an *accounted* one. A
> foreclosure `CONSUMED-INTO-STATE` without a rendered chronicle beat FAILS conformance.

#### Beat 4.3 — Resolution + chronicle echo (capstone #1 close; #12 type-check)

- **Engine state change.** ARC-S07 `escalating → converging → resolved` (terminal:true).
- **Casting / venue.** **Year-end omniscient chronicle** (`articulation_layer_v30 §2`, Tier-3) —
  the `causes[]` walk renders the whole arc **backwards as story** (Q3 PLOT "recognized backwards",
  charter `:100-104`): IP-30 → Tutoring Demand → contact failures → Loyalty 3 → the ARC-S07↔ARC-S20
  rhyme → the Altonian oath → the Succession Vacuum. The trail is followable (gossip, the T16
  Intel case-board, the chronicle itself — the `causes[]` walk as in-world media, charter `:122`).
- **Keys out + accounting.** `meta.arc_state_changed` (→resolved) — **CONSUMED-INTO-STATE**; the
  chronicle paragraph — **RENDERED**.

**Rungs traversed (capstone #1, ≥3):** individual (Torben; Halden) → **family** (the dynasty —
Almud father, Elske sibling-heir, the Bond/Knot cluster) → **faction** (Crown; Löwenritter via the
coup chain; Church as antagonist) → **world** (Altonia / IP / peninsula). **Four rungs.** Each rung
carried its beat on the same aggregate-up / distribute-down transport as state (charter `:69-73`).

**Type-check against `scale_transitions_v30` §5/§12 (capstone #12).** ARC-S07 is
transport-conformant: the Loyalty check (individual scale) meets Sufficient Scope — specifically the
**§7.1 sub-condition of a designated representative**: Torben acts as the Crown's **heir / designated
representative**, so his personal-scale Loyalty outcome legitimately echoes to faction scale (not every
personal act qualifies; this one does because the actor carries delegated dynastic standing) — and
echoes to faction via **Domain Echo §5** (`:313` bottom-up). The Loyalty≤2→Mandate−2 delta is that
same scene→faction **Domain Echo** consequence; the **Loyalty≤3→Autonomy** feed is arc→arc and is
**bottom-up substrate delivery (§12.1)**, not Domain Echo (verifier N2 — "Domain Echo" reserved for the
scene→faction cases). The Tutoring Demand strategic Key reaches Torben/Halden by **populating
sub-scale `targets[]` per §12.3** (down-target), the exact discipline the §12.4 down-seam
`scenario_authoring → settlement_layer` names; delivery is **all-directions §12.1** through the one
substrate (no private channel, §12.2). No new mechanism is introduced — the arc rides existing
§5/§12 behaviour (§12.5 NERS note).

---

## S5.3 The player-shaped branch — divergence table (capstone #3; engagement-window-divergence R7)

The Beat 2.1 covert-contact window exposes **≥2 participated-outcome classes**, each mapping to a
**distinct next `lifecycle.state`** — the anti-railroad proof (charter `:54`, "a different choice
at each engagement window measurably changes trajectory"):

| Beat 2.1 outcome | Loyalty trajectory | Next `lifecycle.state` | Downstream that changes |
|---|---|---|---|
| **Contact SUCCEEDS** (Momentum spent, Ob 3 met) | holds; 3 consecutive → **floor 6** | `active` (stable) | Convergence never fires; Torben **retrieved**; minor Crown cost only (`sim_arc_01:66`) |
| **Contact FAILS / refused** (the spine) | −1/season → **3** by Autumn | `escalating` | Autonomy +1; ARC-S07↔ARC-S20 cosine convergence; **foreclosure** available S4 |
| **PRICED direct-negotiation** (IP-B) | −1 **and** `Altonian_Intel +1` | `escalating` (accelerated) | departure *accelerated* this season (`sim_arc_01:60-62`); worse than doing nothing |

Because the two primary classes reach **two distinct successor states**, the window passes the
**engagement-window-divergence conformance rule** (R7): a window whose outcomes collapse to one
successor would be flagged `illusory-choice` at compile. The three branches also differ in *named
actors* (Elske promoted only on the fail spine), *stakes* (minor cost vs succession vacuum), and
*outcomes* (retrieved vs Altonian) — feeding the two-seed sketch (S5.6).

---

## S5.4 Total-accounting table (capstone #9 — zero unaccounted Keys)

Every Key the engine touched across the four seasons, with its class. Nothing silent (charter
`:143-145`).

| Season · Beat | Key | Class | Note / consumer |
|---|---|---|---|
| S1·1.1 | `clock.IP` (→30, aggregate) | CONSUMED-INTO-STATE | triggers ARC-S07 active |
| S1·1.1 | `env.crisis` (seed) | CONSUMED-INTO-STATE | scenario_authoring seed Key |
| S1·1.1 | `state.tutoring_demand` | RENDERED | Tier-2 cut scene (leader beat) |
| S1·1.1 | `meta.arc_state_changed` (seeded→active) | CONSUMED-INTO-STATE | game_director store (Class B) |
| S1·1.1 | `env.trade_tariff_fluctuation` (T16) | **DISCARDED** | reason: `meaningfulness_below_threshold` → texture |
| S1·1.2 | `mechanical.scene_entered` | RENDERED | game_director single-source (O-1) |
| S1·1.2 | `scene.dialogue` (audience) | RENDERED | played slate scene |
| S1·1.2 | `state.obligation_incurred` | ACCUMULATED | ledger-of-you; priced in S4·4.1 |
| S2·2.1 | `scene.investigation_resolved` | RENDERED | played; §3.1 Stage-0 trigger |
| S2·2.1 | `da.covert_contact{outcome}` | CONSUMED-INTO-STATE | writes Loyalty; enters `causes[]` |
| S2·2.1 | `Altonian_Intel +1` (only if IP-B priced path) | ACCUMULATED | Standing ledger |
| S3·3.1 | `meta.arc_state_changed` (active→escalating) | CONSUMED-INTO-STATE | game_director store |
| S3·3.1 | `state.autonomy_increment` (fork 1 remap) | ACCUMULATED | feeds ARC-S20 coup chain |
| S3·3.1 | Tier-2 cut scene (Torben distance) | RENDERED | articulation §3.1 |
| S3·3.2 | COLLISION-C marker | **DISCARDED** | reason: `predicate_unresolvable(dangling_id ARC-T04)` |
| S3·3.2 | `meta.convergence_detected{S07,S20}` | RENDERED | Tier-2 + chronicle; **zero pressure_effects** (R5) |
| S3·3.3 | `state.belief_revised{Almud}` | RENDERED | followed-only cut scene (sig 7) |
| S3·3.3 | Tier-2 cut scene (Almud alone) | RENDERED | spectator channel |
| S4·4.1 | `mechanical.scene_entered` (if extract) | RENDERED | game_director |
| S4·4.1 | `scene.combat_strike`/`scene.witness` | RENDERED | extraction op |
| S4·4.1 | `state.obligation_incurred/discharged` | ACCUMULATED | pricing |
| S4·4.2 | `state.altonian_oath_sworn` | RENDERED **+** CONSUMED-INTO-STATE | mandatory Tier-3 chronicle (R9) + forecloses path |
| S4·4.2 | `Crown_Mandate −2` (Domain Echo) | CONSUMED-INTO-STATE | feeds ARC-S35 |
| S4·4.2 | `meta.arc_state_changed` (escalating→converging) | CONSUMED-INTO-STATE | store |
| S4·4.3 | `meta.arc_state_changed` (→resolved) | CONSUMED-INTO-STATE | terminal |
| S4·4.3 | chronicle paragraph | RENDERED | year-end Tier-3 |

**Two new Class B types both consumer-closed** (synthesis §8, fork 4):
`meta.convergence_detected` (consumers: game_director booking, articulation render, chronicle
`causes[]` walk) and `meta.arc_state_changed` (consumers: game_director state, chronicle,
articulation significance). Both registered in `key_type_registry_v30` with ≥1 declaring consumer
(conformance R2). **Zero unaccounted Keys.**

**Pricing-preference note (R10).** ARC-S07 carries `stakes_tags:[pricing, foreclosure]` and no
bare `gating` on its own transitions — the one GATED *option* (Formal Crown Treaty, Beat 2.1) is
an ARC-T17 diplomacy gate that carries its ledger cause, not an ARC-S07 wall. A compile-time
`gating:pricing` ratio report + a rule requiring every `stakes_tags:[gating]` vector to carry a
`gaps[]` justification make gating the audited exception the charter's "pricing preferred" intends
(charter `:76`).

---

## S5.5 Capstone coverage checklist

| # | Requirement | Where satisfied |
|---|---|---|
| 1 | Major arc seed→scene→convergence→resolution→chronicle, ≥3 rungs | Beats 1.1→2.1→3.2→4.2→4.3; 4 rungs (S5.2 close) |
| 2 | Casting why-you via tie-graph | Beat 1.2 (`Bond(Halden,Torben)`+`Duty`) |
| 3 | Player-shaped branch changes next stage | Beat 2.1 + divergence table S5.3 |
| 4 | Followed-only arc (spectator, no played scene) | Beat 3.3 (ARC-T02, Almud) |
| 5 | Leader beat (subordinate-originated) + member beat (duty-assigned) | Beat 1.1 (Almud) + Beat 1.2 (Halden) |
| 6 | One gated / one priced / one foreclosed, each citing ledger cause | Beat 2.1 (gated: diplomacy<4; priced: Standing) + Beat 4.2 (foreclosed: Loyalty≤2+Mandate−2) |
| 7 | Every beat's venue labeled | Beats 1.1–4.3 (court/Bond scene/case-board/cut scene/extraction/chronicle) |
| 8 | Meaningfulness passing one beat, failing one context event | PASS: Beat 3.3 belief_revised; FAIL: Beat 1.1 tariff |
| 9 | Total accounting: zero unaccounted Keys | S5.4 table |
| 10 | ARC-S07 compiled end-to-end (typed vector + slots + trace) | S5.1 + S5.2 |
| 11 | Two-seed chronicle comparison (differs in actors/stakes/outcomes) | S5.6 |
| 12 | Type-checks against `scale_transitions_v30` §5/§12 | S5.2 close (Domain Echo §5 + all-directions §12) |

---

## S5.6 Two-seed comparison sketch (capstone #11 — and the anti-oatmeal fix)

Using the fixed regression seeds `SEEDS = [42, 77, 99, 137, 201]` (`01_arc_corpus §a`,
`tests/sim_framework/arc_test_batch*`):

| Axis | **Seed 42** | **Seed 77** (the traced spine) |
|---|---|---|
| Beat 2.1 contact | succeeds (Momentum spent) | fails / refused |
| Loyalty trajectory | floors at 6 | → 3 → 2 |
| Convergence | none (ARC-S07↔ARC-S20 cosine below threshold) | fires (RENDER-ONLY) |
| **Named actors** | Torben retrieved; Elske stays background; Laskaris steady | Elske promoted sole heir; **Laskaris flips** (NPC-ARC-LAK) |
| **Stakes** | minor Crown cost | Crown Mandate −2; **Succession Vacuum** (ARC-S35) opens |
| **Outcome** | Torben **retrieved** | Torben **Altonian** (foreclosure) |
| Chronicle | short, protagonist-focalized, Cert n/a | Tier-3, **Restoration/Church chronicler**, foreclosure beat mandatory |

The two chronicles differ in **named actors, stakes, and outcomes** — capstone #11 met at the
data layer.

> **Anti-oatmeal — the honest scope of what this proves (BLOCKER fix).** Because `arc_vector`s are
> **data, not prose**, two seeds are guaranteed to diverge in their **slot fillers** (proper nouns,
> stakes tags, outcome branches) — that divergence *is* structural. **Prose distinctiveness is NOT
> structural** and is **not** established "by construction": the same template cell + a name swap
> can still read as oatmeal (`dossier_content_economics §3 item 2`: data-substitution is "good
> enough for a mechanical register, not obviously good enough for player-facing prose without
> additional arc-specific authored color"). Charter Q4 anti-oatmeal item 3 (`:133-135`) requires a
> **5-seed prose-distinctiveness regression** over the fixed seeds; the certifying instrument —
> **Expressive Range Analysis** — is currently **UNBUILT** (`dossier_nlg_graduation §4 step 5 / §6`).
> Therefore: **building ERA is a Stage-5 blocker**, and **arc-specific authored color beyond
> name-substitution is a distinct bake line item**, not a free byproduct of the vector schema.

---

## S5.7 Conformance rules the trace exercises (each lives once in `tools/`)

The `R` column below is this trace's **local** label; the canonical CI home and numbering is
`s4_substrate.md §S4.9` (`R1–R10`). Where the local number differs from s4's, the **`= s4 R#`**
cross-label is given (stated once here; in-text sidebar references use the local number). Local R1–R4
and R6 coincide with s4; local R5/R7/R8/R9/R10 do **not** — read them through the cross-labels.

| R (local) | s4 R# | Rule | Beat that exercises it |
|---|---|---|---|
| R1 | **s4 R1** | `predicate-field-resolves` (dangling-ID / struck-mechanic) | 3.2 (COLLISION-C / ARC-T04); 3.1 (Coup Counter remap) |
| R2 | **s4 R2** | `consumer-closure` (every emitted Key names ≥1 consumer) | S5.4 (both new Class B types) |
| R3 | **s4 R3** | `total-accounting` (rendered/accumulated/consumed/discarded, no silent drop) | S5.4 |
| R4 | **s4 R4** | `C2 literal-string lint` (no narratological label surfaces) | 3.2 ("convergence" never shown) |
| R5 | **s4 R9** | `convergence-effect-traceability` (cosine-detected outside register = zero pressure_effects; every authored delta traces to a register line) | 3.2 |
| R6 | **s4 R6** | `watching/participating` = **offered** windows, never taken | 4.1 |
| R7 | **s4 R10** | `engagement-window-divergence` (≥2 outcome classes → ≥2 successor states) | 2.1 / S5.3 |
| R8 | **s4 R5** | `scene_entered single-emitter` (game_director only) | 1.2, 4.1 (O-1) |
| R9 | **s4 R8** | `foreclosure` = edge-triggered only + mandatory Tier-3 render | 4.2 |
| R10 | **s4 §S4.9 deferred gate** | `gating:pricing ratio` (gating vectors carry justification) | S5.4 note |
| R-ORD | **s4 R7** | convergence emit-order preserving (no `set()` gates order) | 3.2 sidebar |
| R-FP | **s4 §S4.2** | replay-critical thresholds quantized to integer grid; port-pinned | 3.2 sidebar |
| R-RND | **s4 §S4.2.4** | realizer fragment selection is deterministic (see O-4) | all RENDERED beats |

> **Scheduling / director sidebar (C7, applies to every RENDERED beat).** The L3 director is a
> **stateless budget CEILING**, not a curve-shaper. It may only **SUBTRACT** — ration the 3–5
> scene-action envelope (`player_agency §4.3`) and **demote** overflow to texture — **never INSERT,
> reorder, delay, or time-compress** a beat to hit a dramatic target. This drops the
> "tension-curve" ownership the synthesis inherited from articulation D11 (which is explicitly
> **DEFERRED**, `articulation_layer_v30:304` "does not enforce pacing; cut scenes fire whenever
> triggers match") and reconciles with the standing doc-10 §8.5 NOT-list ("no designed dramatic
> timing", charter `:104-105`): **event timing stays fully emergent**; the director only decides
> which already-emerged beats surface. **Top-N rationing carries a total-order tiebreak** —
> `(salience DESC, tier_rank, arc_vector.id ASC)` (id is unique → total order; forbids unstable
> sort and set/dict-seeded selection). **Salience demotion is player-protected**: any arc with a
> player participated-outcome in `causes[]` within the last K seasons is **demotion-exempt** (or
> floored at foreground) until it resolves/converges — demotion may only touch player-untouched
> arcs, so the director can never railroad attention *away* from an arc the player is chasing.

---

## S5.8 Open flags carried by this trace (fork + default — never silently resolved)

- **O-1 · `mechanical.scene_entered` ownership.** The charter reserves this as `[OPEN — Jordan]`
  (`00_engine_charter.md:148`). This trace **defaults** to `game_director` single-source (citing
  `module_contracts.yaml:392-395`, `scene_timer` already consuming `from:[game_director]`) and
  demotes `scene_slate` to content-only — **but this is a FORK, not a resolution**. It **contradicts
  the canonical `key_substrate_v30 §8.5 L510`** ("scene_slate: scene activation emits
  mechanical.scene_entered"), so the deliverable **requires an explicit edit to §8.5** shipped in
  the same PR (re-attribute emission, or split manifest-Key vs lifecycle-Key). Until §8.5 is edited,
  it remains a fork. `[OPEN — Jordan]`
- **O-2 · Coup Counter migration (fork 1).** Remap Loyalty≤3→(2,3,40) thresholds 1:1 onto the
  Löwenritter Autonomy 4-stage track vs re-author against stage semantics. **Default: 1:1 remap.**
  Blocks Stage 1. `[OPEN — Jordan]`
- **O-3 · ARC-T04 / COLLISION-C (fork 2).** Author the Southernmost Ritual fresh vs strike the two
  dangling cross-refs. **Default: strike** (COLLISION-C becomes degenerate; the cosine backbone
  covers the real convergence). Needs a fresh lane-tagged ED. `[OPEN — Jordan]`
- **O-4 · Realizer fragment-selection determinism (R-RND).** Rule fragment selection as **either**
  zero-randomness (pure function of Key metadata + focalizer + register band) **or** drawn from a
  dedicated render sub-stream seeded from `(campaign_seed, key.id)` so render never perturbs
  simulation draws. **Explicitly forbid** string-hash / dict-iteration / wall-clock selection. This
  is gated on disposing **RNG-MODEL-COLLISION** (propagation O.5) as a **Stage-0 render-lane
  precondition** — without it, "same rendered text" (charter Q4 / propagation O.8) is unbacked.
  **Default: zero-randomness pure function.** `[OPEN — Jordan]`
- **O-5 · Convergence `temporal_window` (fork 3).** same-Accounting (the 8 conjunctions) /
  4-season cosine ±0.40 (the general backbone) / N-season lookback. **Default: both, as stated.**
  The value 0.40 is `[OPEN — Jordan tuning]`; the quantization arithmetic (R-FP) is structure.
  Blocks Stage 3. `[OPEN — Jordan]`
- **O-6 · Bake volume vs Certainty axis (fork 6) — BLOCKER-flagged.** The `~350-450 authored-unit`
  figure (`dossier_content_economics §2.2`) holds **ONLY if Certainty is a runtime lexicon-swap**
  (fork-6 *fallback*). Under the stated **DEFAULT** (Certainty as a frozen-pool axis, charter Q4
  authority `:126`), the honest bake is **low-thousands** — dossier §3 item 3 / §5 item 2 compute a
  **~5–6× multiplier**. Do **not** label 350-450 "feasible" while defaulting to the 5-6× choice:
  carry **low-thousands as the headline** under the default, OR flip fork-6 to lexicon-swap. Dossier
  §5's verdict is CONDITIONAL-feasible ("only if two open items close"), not unconditional.
  Additionally, **per-NPC voice is a distinct bake line item** whose top end is
  `35 NPCs × triggers-per-NPC × variants` (~1,050 units, `dossier_content_economics §3 item 1`),
  **not** the `3–5 × 35` name-swap floor — Q3 "recognizable-yet-dynamic … not a name swapped in"
  (`:96-98`) is an authoring-craft cost the combinatoric factoring does not certify. `[OPEN — Jordan]`
- **O-7 · Stage 2/3 depend on `engine_clock` / ED-1051 (Gate-0).** Stage 2 steps FSMs "on clocks
  each season" and Stage 3 edge-triggers "at the ACCOUNTING_BOUNDARY" — both ride the temporal
  spine, which is `doc:null` pending ED-1051 (`strategic_judgments J-2`, the frozen critical path).
  Gate Stage 2 (clock-stepping) and Stage 3 (Accounting detection) **behind Gate-0/ED-1051**
  (candidate home: `propagation_spec_v1` / ED-1093). Stages 0/1 have no clock dependency and may
  precede it. `[OPEN — Jordan]`
- **O-8 · GM-judgment-irreducible ~15% (fork 7).** ARC-S07 is not in this bucket, but the
  conformance suite must handle arcs that are (ARC-P05, ARC-S29): author a decision function vs
  declare non-firing in `gaps[]`. **Default: declare non-firing (honesty ledger).** `[OPEN — Jordan]`
- **O-9 · Director tension-curve reversal.** The S5.7 scheduling sidebar (and CR-9 / `director-
  subtract-only`) has the director adopt **subtract-only** rationing (RATION/DEMOTE only; never INSERT
  / ADVANCE / reorder / delay / time-compress), which **reverses** the charter's "director … owns the
  tension curve" (Q4 `:128-129`). **Default (recommended): subtract-only** — doc-10 §8.5 "no designed
  dramatic timing" stands (charter `:104-105`); event timing stays fully emergent and any "tension
  curve" is a read-only backward observation, never a steered target. This is a **hard design call
  held back for explicit Jordan sign-off, flagged in the PR body**, not bundled as routine work
  (CLAUDE.md §2 ED-1094). Shared with s1 fork 5, s2 §Q3.11 fork 7. `[OPEN — Jordan]`

---

## Appendix A — Factionless mini-trace (the charter's named acceptance test)

_The charter's on-ramp acceptance test: **"a factionless PC gets playable seasons"** (charter Q2
L67–68; s1 §Q2.3.c ladder). One season, a PC with **zero faction edges** — no Standing, no Duty, no
`scope.faction` membership. The casting rule is the SAME one rule (s1 §Q2.1): with faction/Standing
edges absent, the **Conviction edge** and the **location edge** do the casting (player_agency §4.2
Steps 4 / 6 / 7 fire independent of faction membership). This is the first rung of the ladder —
Conviction/location → settlement arc → Standing/Obligation proto-currency → Outreach._

**The PC.** "Sef" — a factionless Thread-curious traveler currently in **T6 (Stillhelm)**. Standing 0
with every faction; Renown 1. Conviction (player-authored, player_agency §2.3): *"I will preserve the
**Einhir** folk-memory of the southern villages."* — "Einhir" is a Step-4 System keyword
(player_agency §4.2:258), so it fires Conviction-aligned scenes with no faction edge required. The
grounded, load-bearing part is the pair of edges `Conviction(Sef, Einhir-memory)` + `location(Sef, T6)`
[UNGROUNDED — Sef is a trace vehicle].

#### Beat A.1 — The village moot (casting via Conviction + location, NO faction edge)

- **Keys in.** `TE-21` (Folklore Season, `arc_register_territory.md:61`, Restoration Movement | T6)
  is active in T6; its settlement event surfaces a candidate. `game_director` reads the tie-graph:
  no Standing/faction edge exists, but `Conviction(Einhir)` (Step 4) **and** `location(T6)` (Step 6,
  Territorial) both match → Sef is cast. The matched edge IS the why-you (s1 §Q2.1): _"You have been
  asking the old questions in Stillhelm; the elders noticed."_
- **Engine state change.** A settlement arc-vector books a beat; no faction resolution involved (C3).
- **Casting / venue.** **Settlement-governance venue** — a village moot over whether to record or
  suppress the old rites (charter venue matrix `:113-116`) — a **slate scene** (participating). Ambient
  location: the Stillhelm commons, T6.
- **Player choice + alternatives.** Argue to preserve the folk-memory (social contest, Evidence-styled)
  / stay silent (non-participation input; the moot resolves on the elders' own Disposition).
- **Keys out + accounting.**
  - `mechanical.scene_entered` — **RENDERED** (game_director single-source, O-1).
  - `scene.dialogue` (the moot) — **RENDERED** (played slate scene).
  - `state.obligation_incurred{to: village elder}` **[TRACE-ILLUSTRATIVE]** — **ACCUMULATED** into the
    ledger-of-you (this is the proto-faction currency, s1 §Q2.3.c; not a faction Standing).
- **Surface + register.** Slate scene. `{ significance: 10s, coherence: PC live band, ts: 0–29,
  certainty: n/a, focalizer: protagonist }`.

#### Beat A.2 — Standing/Obligation accrual (the proto-currency)

- **Keys in.** Beat A.1 outcome Key re-enters the settlement arc's `causes[]`.
- **Engine state change.** Conviction *pursued* (a genuine step, player_agency §2.3): **+1 Momentum**
  (pursuit reward, §2.3). The durable proto-currency accrued this season is the **Obligation** (Beat
  A.1) + a **local Standing** with the Stillhelm elders (Disposition, not institutional Standing).
  **Renown** is the cross-faction proto-currency that persists with no faction (`player_agency §5.3`
  Staying Independent), and it takes **+1 when this Conviction resolves Fulfilled/Transformed**
  (`player_agency §5.4`, cap +2/season) — the ladder's next-rung payoff, not this season's.
- **Casting / venue.** No scene — a **Tier-1 ambient lens** update (the personal Obligation/Momentum
  tracker) + a **texture** line (the village now speaks of Sef).
- **Keys out + accounting.**
  - `+1 Momentum` (Conviction pursuit) — **ACCUMULATED** (ledger-of-you; §2.3).
  - `state.local_standing{Stillhelm}` **[TRACE-ILLUSTRATIVE]** — **ACCUMULATED** (proto-faction
    currency; Disposition with the elders).
- **Surface + register.** Tier-1 lens + texture. `{ significance: flash, focalizer: protagonist }`.

#### Beat A.3 — The Outreach hook (next season)

- **Keys in.** Next season's casting pass reads the tie-graph: the `Obligation(Stillhelm elder, Sef)`
  edge from Beat A.1 is now the strongest edge to a live vector.
- **Engine state change.** A Restoration-Movement organizer issues an **NPC Outreach**
  (`npc_behavior §8.11`, ≤3/season; player_agency §4.2 Step 5) — **recruitment-as-arc**, the ladder's
  next rung (s1 §Q2.3.c). Cast by the SAME one rule (s1 §Q2.1) on the Obligation edge.
- **Casting / venue.** A **Tier-2 cut scene** (spectator surface carrying a casting hook, s3 §Q4.3)
  that ends on a **next-season slate candidate** — "you could go there."
- **Keys out + accounting.**
  - `state.outreach_offered{from: Restoration organizer}` **[TRACE-ILLUSTRATIVE]** — **RENDERED**
    (cut scene) + **ACCUMULATED** (the slate candidate carried to next season).
- **Surface + register.** Tier-2 cut scene → slate candidate. `{ significance: 10s, focalizer:
  protagonist }`.

**Acceptance test met.** Sef had a playable season (a played moot), accrued proto-currency
(Renown + Obligation) with zero faction edges, and leaves the season with an Outreach hook — the
factionless on-ramp firing entirely on Conviction + location casting, exactly the ladder s1 §Q2.3.c
builds. No beat required a faction Standing, and no beat was a modal popup (each rendered AT T6 or in
the lens/texture, charter `:116`).

---

## Appendix B — Effect-bearing convergence mini-trace (COLLISION-B, register-authored)

_Beat 3.2's convergence (ARC-S07↔ARC-S20) was **cosine-detected** and therefore **RENDER-ONLY, zero
`pressure_effects`** (R5 / s4 R9). This appendix demonstrates the detector's **other** path — a
**register-authored** COLLISION that CARRIES authored combined deltas as `pressure_effects`. We fire
**COLLISION-B "Practitioner King"** (`arc_register_events.md:33-35`)._

**Why COLLISION-B (least-blocked choice).** Its constituents are **ARC-S17** (Almud Discovery Event,
TS 28→30), **ARC-S23** (Elske installed independently), and **ARC-S07** (Torben in Altonia — the
spine's Beat 4.2 foreclosure outcome). **None of the three depends on the STRUCK Coup Counter**, so no
fork-1 remap is needed to fire it. (COLLISION-F, by contrast, lists "Coup Counter ≥ 2" as one of its OR
trigger paths, `arc_register_events.md:50-52` — it would ride the struck mechanic under the fork-1 default
1:1 remap. COLLISION-B is the cleaner demonstration.) ARC-S07 feeds COLLISION-B directly via
"Torben in Altonia," which the traced spine produced at Beat 4.2.

#### Beat B.1 — COLLISION-B fires (register-authored → effect-bearing)

- **Keys in (at the ACCOUNTING_BOUNDARY, over settled state).** Three constituent lifecycle states
  co-occur: ARC-S17 `converging` (Almud's Discovery Event, ARC-S17 `arc_register_factions.md:16`),
  ARC-S23 `resolved` (Elske installed, `arc_register_factions.md:22-23`), ARC-S07 foreclosed
  (Torben Altonian, this trace's Beat 4.2).
- **Engine state change.** The **Tier-A detector** matches the COLLISION-B conjunction
  (`edge_triggered_once`, dedup by the ordered key `(COLLISION-B, sorted(actor_ids), season)` — R-ORD /
  s4 R7, never a bare `set()`). Because COLLISION-B is one of the **8 register-authored** markers, it is
  **effect-bearing**: it applies its authored combined deltas.
- **Casting / venue.** A **Tier-2 cut scene at the T1 Crown court** + a Tier-3 chronicle line — the
  three-bodied dynasty "distributed across three people in three states" (`arc_register_events.md:34`)
  recognized, not played. The label "convergence" **never surfaces** (C2 / R4).
- **Keys out + accounting.**
  - `meta.convergence_detected{conjunction: COLLISION-B, provenance: register_authored}` —
    **RENDERED** (Tier-2 + chronicle) + feeds the `causes[]` walk.
  - `pressure_effect: clock.TC +3` — **CONSUMED-INTO-STATE**. **Traces to a register line**
    (`arc_register_events.md:35` "TC +3 but RS improves"), so it PASSES R5 / s4 R9 provenance — the
    delta is authored, not fabricated.
  - `pressure_effect: RS improvement` (qualitative "RS improves", same register line) —
    **CONSUMED-INTO-STATE**; traces to the same line.
- **Contrast (the effect-bearing seam).** Unlike Beat 3.2's cosine S07↔S20 (zero `pressure_effects`,
  render-only), COLLISION-B mutates clocks/stats **because it is register-authored**. Every delta here
  traces to `arc_register_events.md §VI`; a cosine-detected marker attempting the same would be compiled
  effect-free (R5 / s4 R9). This is the detector's two-path discrimination made concrete.

**Accounting rows (Appendix B):**

| Beat | Key | Class | Note |
|---|---|---|---|
| B.1 | `meta.convergence_detected{COLLISION-B, register_authored}` | RENDERED | Tier-2 + chronicle; deduped ordered key (R-ORD) |
| B.1 | `clock.TC +3` (authored combined delta) | CONSUMED-INTO-STATE | traces `arc_register_events.md:35` (R5 / s4 R9 PASS) |
| B.1 | `RS improvement` (authored, qualitative) | CONSUMED-INTO-STATE | same register line; effect-bearing |

**Verdict.** COLLISION-B exercises the effect-bearing convergence path end-to-end: register-authored →
authored deltas applied → every delta traced to a register line → total-accounting closed. It is the
positive counterpart to Beat 3.2's render-only cosine case, and it fires with **no Coup-Counter
dependency** (no fork-1 remap required).
