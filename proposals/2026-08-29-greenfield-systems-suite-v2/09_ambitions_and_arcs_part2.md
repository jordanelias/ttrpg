# 09 (part 2) — Ambitions and Arcs: latency, the player surface, the contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`09_ambitions_and_arcs.md`](09_ambitions_and_arcs.md) — **part 1 first; this continues it**
## Part 1: §§1–7 (the arc grammar, the composition, derived progress, the hook grammar, obstruction,
## the four verbs, arcs as tag chains) — and part 1 carries the `## Overrides` block for both parts
## Part 2: §§8–13 (J-N and J-O, the player surface, the registries, the contracts, the audit)

Section numbering continues from part 1 without a break, and every `§n` cross-reference resolves
across both parts. Split under `CLAUDE.md` §4's sequential-parts rule (`_part2` in reading order,
never index+infill) because the single file exceeded the 14k-token compliance cap.

**Everything in this part is `substrate` in the sense of `00 §2.1` except §9**, which is the whole
player-facing surface of both parts: **one verb and two reads.**

---

## 8. ⚠ J-N — the substrate supplies NO cross-season latency, and this is the constraint that shapes §3

**This is the one constraint on this page that is not a ruling and cannot be argued with. It is what
the code does.** The amended authority model (see the note after `## Overrides`) puts canon and
rulings in scope for override; it does not put the interpreter in scope. **Verified independently
against the tree for this document**, not taken on report:

| claim | verified at |
|---|---|
| `drain_tick` has **zero production callers** — the only callers are four lines in one test | `engine/substrate/keys.py:538`; `tests/valoria/test_key_substrate.py:336,361,376,388` (grep over all `.py` returns nothing else) |
| `next_tick` **raises `TerminationBreach`** if the queue is non-empty, so there is **no cross-season carry** | `engine/substrate/keys.py:593-599` |
| `schedule_emission` increments depth **only when already draining** | `engine/substrate/keys.py:525-536` |
| `DEFAULT_CASCADE_DEPTH_MAX = 0`, self-labelled provisional | `engine/cross_scale/echo_transport.py:102` |

> **The guard prevents cascades outright; it does not schedule them late.** One-hop-per-season latency
> is not a property this design has — it is a mechanism someone would have to build. Filed as open
> ruling **J-N** (`audit/2026-08-08-world-churn-audit/06_master_synthesis.md:532`, **held, not
> ratified** — `:4`).

**What this forbids in this document, and what it forces instead:**

| forbidden | what §3 does instead |
|---|---|
| a project reacting to a Key by emitting a Key that lands next season | there is no such transport |
| a project that is *posted to* — "an actor's move advances my project" | **it advances because the world *IS* a certain way at the accounting boundary.** It reads state |
| accumulating advance deposits during the season for next season's fire | progress is recomputed from current state each boundary; nothing accumulates in transit |
| a stall counter incremented by an emission | stall is the Ambition tag's `ttl`, which runs on **elapsed time**, a pure function (§6.1) |

**This is not a limitation this design works around; it is the reason §3 is a derivation.** A project
that advanced by receiving something would need the transport. A project that advances by *looking*
needs only the boundary, which already runs. **This design therefore requires no latency to be built
and is not blocked on J-N.** J-N is the ruling that would *permit* an alternative, not one this page
waits on; if it rules for reactive chains, §3 and §6 are what to revisit and nothing else here moves.

### 8.1 ⚠ J-O — what this document does and does not lean on

`06_master_synthesis.md:533` files **J-O**: *does the Key mesh deserve promotion from telemetry spine
to churn engine at all*, the alternative being **Keys as an append-only telemetry and causality log
with churn driven at the boundary directly.** Stated so the affected parts are identifiable if J-O
rules the other way:

| depends on Key **consumption**? | survives a "telemetry only" ruling? |
|---|---|
| `am.advance` / `am.fire` / `am.lapse` — **all three read state, consume nothing** | **yes** |
| the arc chain (§7): `Tag.provenance` → Key, `causes[]` | **yes** — that is telemetry and causality, exactly what the alternative keeps |
| the emission side (`mechanical.project_advanced`, `state.project_completed`, `state.project_failed`) | **yes** as a log |
| the `consumes: []` lists in §11 — **already empty** | **not applicable** |
| the Slate candidate hand-off (§9) — if `10` is wired as a Key consumer rather than a boundary read | **the one exposure**, and it is `10`'s, not this document's |

**This document is close to robust under J-O**, and that is a property of §3's derivation, not luck: a
design that advances by reading state does not care whether the mesh is a churn engine or a log.
**This suite takes no position on J-O.**

---

## 9. What the player actually touches

**One verb. Two read-only affordances.** Everything else in both parts runs headless.

| surface | what the player is asked | how often |
|---|---|---|
| **`am.declare`** — commit to a project of their own | choose a project kind from those their posts' remit makes eligible, and bind its slots. Costs **one budget point** | at most once a season, usually far less |
| the **band** of a project they own or can see, and its **published advance terms** | nothing — a read | when the item is on screen |
| a project's **arc chain** — *what has this been, and who moved it* | nothing — a read, on demand, never pushed | on demand |

**Never touched:** any NPC's, bloc's or faction's project (substrate — experienced only as a
situation arriving on the Slate) · `am.advance` / `am.fire` / `am.lapse`, all boundary-run · a
project's **threshold**, its **progress number** or any **forecast** of when it will fire (§3.3) ·
an **obstruct** verb, because there is none (§5).

**Substrate objects here: 1 tag kind · 1 registry block of project kinds · 4 verbs of which 3 are
headless · 0 new gauges · 0 new entity kinds. Surface: 1 verb, 2 reads.** The ratio is the right way
round (`00 §2.3` point 4).

### 9.1 The payoff — long-range agency from a small verb set

The answer to the obvious objection that `00 §2.2`'s single-digit verb budget makes a shallow game.

**Every other verb in this suite resolves inside one season.** An appointment, a directive, a contest,
a response to a Slate item — each is a move whose consequence lands now. A player with only those
verbs is playing a game of *reactions*, however good the reactions are. **`am.declare` is the only
verb whose horizon exceeds one season**, and it converts the entire existing verb set into
instruments of a plan the player chose:

1. **It buys reach without buying breadth.** Declaring does not add options; it makes the options the
   player already had *mean something over time* — every appointment now either serves the ambition
   or does not. **One verb, and the whole existing surface acquires a second axis.**
2. **It makes the world's ambitions legible as opposition.** Because NPC, bloc and faction projects
   use the identical mechanism, the player's ambition and the world's are the same kind of thing and
   collide on the same terms. That is `governance_play_redesign_v1:15`'s P3 — *"the world moves
   whether or not the player does"* — made structural.
3. **It is what makes obstruction dramatic rather than administrative.** A rival's project is not a
   status bar; it is the reason the thing you did for your own reasons three seasons ago mattered.
4. **It is the cheapest possible depth.** One verb, one tag kind, one registry block, three headless
   boundary passes. Measured against the delta brief's test — *could this be removed from the
   player's hands entirely and still change the game?* — the **NPC** half answers yes and is
   substrate; only the player's own declaration answers no, and only it is surface.

**Every verb must justify its slot against a verb not proposed** (`00 §2`). `am.declare` is justified
against **`am.obstruct`**, **`am.abandon`** and **`am.reprioritise`** — all three considered, all
three cut (§12). Obstruction is already every other verb; abandoning is letting the `ttl` run out,
which is a decision the player makes by *not acting*, which is the better version of the choice; and
reprioritising is what declaring a different project already is.

---

## 10. Registry rows and key types — three of the four already exist (O-A3)

### 10.1 The key types: what the tree already has

**`00 §9.2` proposed `project.declared` / `project.fired` / `project.lapsed`. Three of those four
moments are already registered types under ED-935**, with live contract edges, and re-declaring them
would be exactly the duplication `00 §1` names as the under-distilled failure.

| verb | key type | status | citation |
|---|---|---|---|
| `am.advance` | **`mechanical.project_advanced`** — payload `project_id, progress_before, progress_after, project_domain` | **registered** (ED-935) | `key_type_registry_v30.md:446-458`; `module_contracts.yaml:333` |
| `am.fire` | **`state.project_completed`** — payload `project_id, project_domain, completion_effect, supporters, obstructors, goal_short` | **registered** | `key_type_registry_v30.md:691-706`; `module_contracts.yaml:335` |
| `am.lapse` | **`state.project_failed`** — payload `project_id, failure_mode, seasons_stalled` | **registered** | `key_type_registry_v30.md:710-723`; `module_contracts.yaml:334` |
| `am.declare` | **`state.project_formed`** — **DOES NOT EXIST** | **the gap**, already found and proposed | `01_gap_register_part2.md:281` (G-29), `BLOCKED on G-17` |

**G-29's own words** (`:281`): *"no key type exists for project or ambition FORMATION … so the moment
an NPC forms a new goal is generated in-process and announced to nothing."* Its proposal —
`state.project_formed`, payload `npc_id, project_id, project_domain, goal_short`, optional
`prior_project_id, formation_cause` — **is adopted as-is**, generalized only in that `npc_id` becomes
an entity id, because blocs and factions declare projects too.

⚠ **Nothing is appended here.** `00 §8` P0-1 blocks any key-type append until
`references/rendering_dispositions.yaml` exists; G-29 blocks it additionally on G-17. **Both blocks
stand.** This section's contribution is that the blocked work is now **one type instead of four**, and
`optional_payload_fields.prior_project_id` is precisely what §5.1's lapse-and-redeclare escalation
needs — which is convergent evidence that G-29's proposal was right before this design existed.

**One adjacent defect, recorded not fixed** (found while verifying): `module_contracts.yaml:1418`
still annotates all three registered types `[unreg]`, while `:362` and `:364` record that ED-935
registered them on 2026-06-14 — **the file contradicts itself about ED-935.** G-29 found the same.
An IN-lane contract-truth item, not this suite's to fix, and nothing here depends on it.

### 10.2 The registry rows

`00 §9` holds the whole suite to **two new registry files**, and this document adds **none**. Project
kinds are a **block** in `references/content_registry.yaml`:

```yaml
project_kinds:
  - id: <kind id>                      # an arc-vector TEMPLATE (§1)
    class: substrate | surface         # surface ONLY for kinds a player may declare
    owner_binding: {entity_kind: person|bloc|faction|place, gate: <predicate>}
    slots: [target, terms]             # the ratified binding slots (:80)
    advance_terms:                     # each: a predicate over READABLE STATE. No RNG. No Key. (§8)
      - {w: <int bp>, term: <predicate>, required: <bool>, ratchet: <bool>}
    threshold: <int bp>                # HIDDEN — a trigger (01 §8)
    bands: [(<bp>, <label>)]           # PUBLISHED — what a reader sees
    horizon: <seasons> | null          # null permitted for ratchet kinds only (§6.1)
    stall_ttl: <seasons>               # the Ambition tag's ttl; canon's default is 8
    fire: {guaranteed: <bool>, effect: <one of the four write leaves>}   # a GATE, never a roll
    firing: true | false               # false = a declared non-firing residue (§1.1). COUNTED.
    residue: {on_fire: <tag>, on_lapse: <tag>}
    disclosure: [{of: progress, inputs: published, presentation: band, trigger: hidden}]
```

**Adding a project kind — and therefore an arc shape — is data.** `00 §6` principle 3.

---

## 11. Module contracts

In `00 §7`'s shape. `consumes:` is empty on all four, which is §8's constraint expressed in the
contract rather than promised in prose, and is why §8.1 can claim robustness under J-O.

```yaml
# ALL FOUR: parent: ambitions · scales: all four · tier: null · form: []
#           consumes: []   <- J-N (§8): nothing is ever posted to a project
# The three below `am.declare` are boundary-run by the herald (01 part 2 §9.2, W-5), so all three
# carry remit: [] and budget: null — they are not invocable by any post, including the player's.

- module: am.declare
  class: surface               # the ONLY surface row in this document
  resolver: gate               # eligibility + the remit/caste gate. Declaring is never a roll.
  remit: [head, governor, minister, commander, envoy]       # clerk cannot declare; §9
  budget: {gauge: post.budget, cost: 1}
  emits: [{type: state.project_formed, terminal: false}]    # BLOCKED on P0-1 + G-17 (§10.1)
  state: [{name: tag.ambition, bucket: tag, writable: true, owner: substrate.ledger}]
  transitions: []
  disclosure: [{of: tag.ambition, inputs: published, presentation: exact, trigger: hidden}]

- module: am.advance
  class: substrate
  resolver: derivation         # progress is DERIVED (O-A2). Nothing writes it.
  emits: [{type: mechanical.project_advanced, terminal: false}]   # on a BAND crossing only (§3.3)
  state: []                    # a derivation owns no state — this row is empty on purpose
  transitions: []
  disclosure: [{of: progress, inputs: published, presentation: band, trigger: hidden}]

- module: am.fire
  class: substrate
  resolver: gate               # guaranteed at threshold; no attempt/failure variance (§4)
  emits: [{type: state.project_completed, terminal: false}]
  state: [{name: tag.ambition, bucket: tag, writable: true, owner: substrate.ledger}]  # -> residue
  transitions: [<whichever the kind's fire.effect names; each declared in form_registry.yaml>]
  disclosure: [{of: tag.ambition, inputs: published, presentation: exact, trigger: hidden}]

- module: am.lapse
  class: substrate
  resolver: gate               # ttl expiry / required-term unreachability. Reads elapsed time only.
  emits: [{type: state.project_failed, terminal: false}]
  state: [{name: tag.ambition, bucket: tag, writable: true, owner: substrate.ledger},   # swept
          {name: tag.precedent, bucket: tag, writable: true, owner: substrate.ledger}]  # residue
  transitions: []
  disclosure: [{of: tag.precedent, inputs: published, presentation: exact, trigger: hidden}]
```

**`am.fire` is the only module in this suite whose `transitions:` list is supplied by data** — the
auditable seam: the set of form transitions a project can cause is a grep over one registry column,
per `00 §7`'s rule that a module may only transition a field it declares.

### 11.1 The candidate hand-off — this document produces, `10` ranks

Every emission above is a **Slate candidate**, and this document **does not rank it**.
`narrative_engine_design_v2_churn.md §4`'s **Light Function is RATIFIED (ED-IN-0011)** and
[`10_the_slate_and_salience.md`](10_the_slate_and_salience.md) owns the surfacing side. It is in scope
for override under the amended authority model — **but not by this page**, which is a producer of
candidates and would be re-deriving a ranking function it has no reason to touch. Three bindings this
document holds itself to, reproduced rather than paraphrased:

- **Strictly selective / subtract-only** — the light rations among candidates the churn produced and
  can never inject content, accelerate a clock or emit a pressure-bearing Key (`:197-204`). **A
  project is therefore never advanced, delayed or fired by the light**; salience is downstream of
  `am.advance`, never an input to it.
- **Casting is severed from forecast** (`:205-208`) — slate entry keys on **realized state** only, so
  a project's candidate carries `durability`, `tie-proximity`, `identity-touch` and its holon, and
  **never** how close it is to firing (§3.3).
- **No salience or forecast function is designed here.** If `10` needs a term this page does not
  supply, that is a ruling request, not an edit here.

---

## 12. What was cut

| Considered | Verdict | Why |
|---|---|---|
| a **Project entity kind** (a seventh) | **rejected** | it would need its own store, sweep, provenance rule and disclosure contract — all of which Tag already has. §2 |
| a stored **`progress` Gauge** | **CUT** (O-A2) | an aggregate over the advance terms; no aggregate is ever written. §3 |
| a **`+1` per season** advance rule (`governance_play_redesign_v1:241`) | **replaced** (O-A4) | a timer whose only obstruction is a bespoke intervention. §5 |
| an **`am.obstruct`** verb | **rejected — the document's best cut** | obstruction is *any* verb that moves a term a project reads. The verb would make obstruction intentional-only and put a project on the player's menu. §5 |
| an **`am.abandon`** / **`am.reprioritise`** verb | **rejected** | abandoning is letting the `ttl` run out, which the player already does by not acting; reprioritising is declaring a different project |
| a **project→project dependency graph** | **rejected** | a predecessor's residue is a Precedent tag, already a legal advance term; the graph is derived by walking `causes[]`. §7 |
| an **arc object**, store or scheduler | **rejected** | §7 — an arc is a projection of the one beat stream. A second store would fork save/replay and the causal graph |
| three new key types (`00 §9.2`) | **CUT** (O-A3) | three of the four moments are registered already. §10.1 |
| a **cross-season advance carry** | **rejected as non-existent, not as unwanted** | §8 — the transport is not in the tree (**J-N**) |
| a **project-specific salience term** | **rejected** | `10` owns the light. §11.1 |
| **decay on `progress`** | **rejected for ratchet kinds** | §3.2 — monotonicity comes from the append-only tag ledger, not from an exemption to `01 §5.1` |

---

## 13. Property audit

**Scope, and the honest limit. Nothing in this document rolls.** `am.declare`, `am.fire` and
`am.lapse` are **gates**; `am.advance` is a **derivation**. Per the methodology's own rule — and per
`01 part 2 §13`'s precedent — **no N/R/S/E verdict is manufactured for a module with no draw.** The
two properties that do apply are given, then every loop with its bound and every gate with what it
reads. Above all of it sits `00 §0.1`: **a resolution-scoped audit cannot ask whether a design
expresses the game.**

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass, with two of the three bounds arithmetic** | progress is a weighted sum of indicator terms, so it is bounded above by `Σ w_i` **at declaration time**, from the row alone, with no campaign run. Live projects per owner are capped at `PROJECT_CAP` *(a shape proposal)*, so the boundary's cost is `owners × PROJECT_CAP × MAX_TERMS` — linear and declared. Monotone response holds for ratchet terms structurally (§3.2) and is **deliberately absent** for the rest, which is the design: a project can slide back because someone took the ground |
| **P-v** right engine | **pass** | three gates and one derivation. **Fire is a gate on purpose** (§4): the uncertainty was in getting the world there, and re-rolling at the threshold charges for it twice. Nothing here is a `d_sigma` and nothing here is an `accrual` — the accrual reading is exactly the stored counter O-A2 cuts |

### 13.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| declare → advance → fire → world changes → another project's term moves → it advances | **`PROJECT_CAP` per owner and the `ttl` horizon.** Every project ends: it fires (terminal) or it lapses (swept) | **unmeasured.** Campaign-reachable, so measurable with a control — `tools/balance_oracle.py` is the instrument, and a campaign-level change makes its two arms genuinely differ |
| lapse → Precedent residue → an advance term of a successor kind → declare | **the residue is a durable tag under `01 §3.3`'s dedupe**, so it refreshes rather than stacks; each successor consumes a `PROJECT_CAP` slot | **unmeasured, and the loop most likely to run hot.** §5.1's ladder is finite by declaration, but nothing in the substrate enforces that a successor chain terminates. **A registry check should require the successor graph to be acyclic**; it does not exist |
| ratchet terms → progress → fire | **terminating by construction**: terms monotone, threshold fixed, fire terminal | **bounded** — the only proved bound here, and it is the coup counter's property, not this design's |
| fire → Slate candidate → player attention → player acts → a term moves | **the scene budget** (`10`); the light is **subtract-only** (`churn:197-204`) so it cannot accelerate a project | **unmeasured**; the severance is `10`'s to enforce, not this page's |
| obstruction → progress falls → owner's method escalates → new obstruction | **the `ttl` horizon and `PROJECT_CAP`** | **unmeasured** |
| a Key-driven advance cascade within a season | **does not exist.** `DEFAULT_CASCADE_DEPTH_MAX = 0`, and `consumes:` is empty on all four modules (§8, §11) | **not a loop today.** If **J-N** rules for reactive chains this becomes a real loop with no bound yet |

### 13.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| `am.declare` eligibility | the owner's posts and their `remit`; the kind's `owner_binding`; one budget point | the kind is not in the option set — **an absence, not a penalty** (`01 §4.3`) |
| `am.lapse` unreachability | any `required: true` term that is permanently false | no lapse |
| `PROJECT_CAP` | the owner's live Ambition tags, counted | declaration unavailable until one ends |
| `am.fire` threshold | the derived progress against the hidden threshold — **state only, never a received Key** | no fire; the project stays live |
| `am.lapse` horizon | the Ambition tag's `ttl` against the season index — **elapsed time, a pure function** | no lapse |
| `firing: false` | the registry row | the kind is never instantiated, and is **counted** in the honest-residue ledger (§1.1) |
| successor-graph acyclicity | **nothing — this check does not exist** (§13.1) | **an open gap, stated rather than assumed** |

### 13.3 Falsifiers — a claim with no falsifier is not a claim

| claim | falsifier |
|---|---|
| **No aggregate is written.** Progress is derived (O-A2) | a test asserting no contract in this suite declares a `state:` row named `progress`, and no write path deposits into one. **Load-bearing on the game:** it is `01 §2.1`'s write rule, and violating it is the defect `01 §7.3` caught in v1 |
| **A project reads state and consumes nothing** (§8, J-N) | a test asserting `am.*` contracts have empty `consumes:`, plus a seeded-campaign assertion that no project's progress changes within a tick in response to an emission. **Load-bearing:** if it fails, the design rests on a transport the tree does not have |
| **Fire is a gate, never a roll** (§4) | a test asserting no `am.*` module has `resolver: d_sigma` and that no fire consequence reaches `roll_pool` |
| **No forecast is published** (§3.3) | `01 §8`'s falsifier extended: no key type emitted here carries a field whose value is a **future** state, and `mechanical.project_advanced` carries only `progress_before` / `progress_after` — both crossings already made |
| **No entity or outcome is special-cased** | a grep asserting no project kind's `owner_binding`, `advance_terms` or `fire.effect` contains a literal entity id. **This is the one falsifier that cannot be run yet** — there are no rows |
| **Monotonicity needs no exemption to the decay law** (§3.2) | a test asserting this document declares no gauge at all, and that every ratchet term resolves to a tag-existence predicate on a `ttl: None` tag |
| **Obstruction needs no verb** (§5) | a seeded campaign in which a project's progress falls after an unrelated actor's action, with no module having named the project. **If it never happens, the advance terms read state nobody else touches and the projects are timers after all.** The weakest-supported claim on the page, and this is how to break it |
| **`place_found` is reachable** (§6.3) | a seeded campaign in which a `found_settlement` project fires and `07`'s `place_found` transition follows. **If no such kind exists in `content_registry.yaml`, or none ever fires, `07`'s row is dormant** — and the defect is in this document, not that one |
| **Every project ends** (§6.1) | a seeded campaign assertion that no Ambition tag survives `max(horizon, stall_ttl)` seasons past its last band crossing, and that live projects per owner never exceed `PROJECT_CAP` |
| **~13 template shapes cover the arc space** | **NOT CLAIMED.** The calibration corpus is evacuated (§7.2). Do not cite the figure as validated coverage |

### 13.4 Reachability, in both directions

The same bar `11` gets, a **content** obligation on the registry rather than a code check. A kind
whose conjunction has **never held** in a seeded campaign is decoration; one that **fires for most
owners most seasons** is weather; and one that is **declared and always lapses** is worse than
either, because it costs a budget point and a `PROJECT_CAP` slot and returns only a residue.

None of the three is checkable until rows exist, and **none of them is checkable at all without the
calibration set §7.2 says is gone.** That is the honest state.
