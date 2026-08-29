# 08 — Settlement management: the governor's one decision

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## `07_places_and_settlements.md` (not yet authored — this document binds to its `place.form`
## interface as declared in `01 §1.1`, not to its content) ·
## `10_the_slate_and_salience.md` (not yet authored — this document emits; `10` ranks and truncates) ·
## `systems/fieldwork/fieldwork_v30.md` §1 (Depth Axis) · `systems/fieldwork/fieldwork_investigation.md`
## §4 · `systems/settlements/settlement_layer_v30.md:162,708` (facility-tier ladder; fieldwork
## settlement-anchoring)
## Produces: one mandatory decision per settlement per season, a substrate that keeps working whether
## or not the player is watching, and the coupling that lets what a settlement builds become something
## it can be investigated for.

---

## A note on authority, read before the rest

Mid-session, Jordan withdrew the standing instruction that a prior ruling binds this suite by default:
*"existing work is not necessarily required to keep all the way through to things like obstacles
being stat/2 or whatever is ratified and canon… I just want the best possible proposal."* This
document was drafted under the older, stricter posture and is finished under the new one. Two
consequences, stated plainly rather than silently absorbed:

1. **`derive_ob`'s `score/2` is evaluated on the merits below (§4.1), not adopted by default.** The
   verdict is to keep it — not because it is ruled, but because nothing about a settlement's
   obstacles asks for a different curve, and the single-owner property (one derivation, not one per
   verb) is an architecture invariant this document has independent reason to want.
2. **The playing-surface cut in this document is bolder than the archived version needed to be**,
   because the licence to override no longer stops at "v1 already gated this." §3 cuts the up-stroke
   verb menu **entirely** as a player-visible object, not merely down-sizes it.

---

## Overrides

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-1** | v1 `08 §4`'s `sm.verb` — a **player-browsable menu**, four verbs × two forks, spent every season | this suite's own v1 | The playing-surface budget (`00 §2`, Jordan 2026-08-29) forbids it outright, not just its size. **Reclassified `class: substrate`** (§3): the same registry rows still run, every season, chosen by the post-holder's own preference exactly as an unattended post already works (`01 §4.4`) — no possibility is lost, only the player's obligation to browse it |
| **O-2** | v1's four always-available directive responses (Comply / Bargain / Commute / Defy), and its bespoke post-scoped `suspicion` gauge | this suite's own v1 | §4 demotes Bargain and Commute from *always offered* to *gated by readable state*, sharpening a rule v1 already half-had for Commute alone. `suspicion` is **retired as a distinct gauge**: it is exactly the person-scoped `exposure` meter `01 §5.2` already ships ("two personal meters, not nine") wearing a settlement-specific name. No new object; an existing one, correctly attributed to the **person**, so it now survives a governor's reassignment instead of resetting at the post |
| **O-3** | v1's `sm.business` contract declaring `resolver: derivation` while writing the `pressure` gauge | this suite's own v1 | `00 §7`'s resolver table is stricter than the one v1 wrote against: *"derivation — never use when anything writes it."* Corrected to `resolver: accrual`, which is what a bounded per-season deposit into a decaying gauge already is (`01 §5.1`). No behavioural change; the tag was wrong, not the module |
| **O-4** | *(evaluated, not taken)* replacing `derive_ob`'s `score/2` for settlement obstacles | — | See the authority note above and `§4.1`. Kept on the merits: the modifier slot already absorbs everything settlement-specific that a bespoke formula would have bought, and single-ownership is worth more than a domain-flavoured curve with no argued advantage |

---

## 1. The gate

Same shape as `05 §1`, one tier down, and not re-derived: a settlement whose governance post is
vacant runs no governance modules this season and emits `faction.action_declined(place,
reason="vacant_governor")`. Recoverable by the same path — the vacancy raises a demand, and
generation is total (`01 §4`). Zero player surface; substrate.

---

## 2. What the player actually touches this season

**One thing, always. Nothing else, unless the Slate decides otherwise.**

| what the player touches | how often | class |
|---|---|---|
| **Respond** to the season's directive | exactly once per held governance post per season — mandatory, bypasses ranking (`10`'s "rare and enumerated" mandatory-item allowance) | surface |
| Respond to a business or investigation item the Slate chose to surface | 0–few, entirely at `10`'s discretion, never guaranteed | surface |

| what runs without the player | how often |
|---|---|
| the season's business draw (`§5`) | every season, for every settlement, whether attended or not |
| the settlement's own governance effort — development, order, adjudication, construction | every season, chosen by the governor's own preference, whether attended or not |
| investigation-surface bookkeeping (`§6`) | continuous |

**This is the whole answer to `00 §2.3` point 4's ratio test.** One mandatory row against three
substrate rows, and the second table is where the actual government of the settlement happens.

---

## 3. The up-stroke is retired as a player object — what replaces it

v1 shipped `sm.verb`: four verbs (Develop, Order, Court, Build), two forks each, a menu the player
spent `post.budget` against every season. **That object is cut.** Not shrunk — cut, as a thing the
player opens.

**What produces the outcome instead.** The eight registry rows survive unchanged in *content* —
Develop still develops, Build still builds — but move to a single substrate module, `sm.act`
(§8), invoked **by the post**, resolved **by the post-holder's own preference**, every season,
exactly the machinery `01 §4.4` already specifies for an unattended post. There is no second,
cheaper algorithm: an attended governor's post runs the identical module. **What changes is only
whether the player supplied the choice or the holder's convictions did** — and per `01 §4.3`'s
`remit` argument, that difference is a fork in *who chooses*, never a fork in the odds.

**No bespoke "promotion" mechanism is built to let this reach the player anyway.** `sm.act`'s
results are ordinary Keys — a gauge deposit, a tag, occasionally a named form transition (§8) — and
whether any one of them is salient enough to reach the Slate is `10`'s question, answered by the
same Light Function that ranks everything else in the game. Inventing a settlement-specific
escalation rule here would be exactly the shape-divergence `00 §6.2` forbids: a second dialect for
"this subsystem's version of mattering."

*Emergent possibility lost if `sm.act`'s rows were cut instead of merely rehoused:* a settlement
would stop developing, adjudicating, keeping order or building the moment nobody was looking at it —
the opposite of a world with an outside. Cutting the **menu** loses nothing; cutting the **rows**
would.

---

## 4. `sm.directive` and `sm.respond` — the one verb

### 4.1 Which directive fires, and its obstacle

`sm.directive` is unchanged in kind from v1: one typed order — `extract · levy · suppress · install ·
host · cede` — derived from the principal's and the place's own state, consuming no randomness.
Substrate; the principal does not browse a menu either.

**On `derive_ob`.** Bargain is the one branch of this document that rolls, and its obstacle is
`derive_ob(principal.standing)` — `01 §6`'s single owner, unmodified. Weighed against replacing it
(per the authority note): a settlement-specific curve would need an argued reason a governance
negotiation is harder or easier per unit of authority than every other contest in the game, and
there isn't one. What *is* settlement-specific — a principal who already distrusts this particular
governor — belongs in the **modifier**, which `01 §6` reserves for "a term genuinely a property of
the target": `derive_ob(principal.standing, modifiers = +exposure_band(governor))`. That is the
single-owner shape doing the work a bespoke formula would have, at no cost to the invariant.

### 4.2 The response set — two always, two gated

**Comply and Defy are the fork.** Every directive, at every settlement, offers exactly these two,
unconditionally — this is the "governor complies or defies" decision named as `08`'s primary shape.
**Bargain and Commute are not menu items; they are gates.** Each is offered only when the place's or
the post's own readable state admits it — the situation supplies the choice, not a standing option
the player must scan past at a settlement too poor or too weak to use it.

| response | offered when | resolver | what it costs | what it gains |
|---|---|---|---|---|
| **Comply** | always | `gate` | the demanded deposit lands | `standing` deposit up for the governor (person-scoped); the principal's trust |
| **Defy** | always | `gate`, no roll | a `standing` deposit down, an `exposure` deposit up, a `Precedent` tag on the place | the demanded deposit does not land; `acceptance.support` deposit up |
| **Bargain** | gated: `post.budget ≥ 1` **and** `exposure_band(governor) < high` — a governor already under scrutiny has nothing left to spend down | `d_sigma` — SO against `derive_ob(principal.standing, +exposure_band)` | a budget point; an `exposure` deposit even on success | softer terms, scaled by degree |
| **Commute** | gated on the place's own condition gauges (`§4.3`) | `gate` | trades one obligation for another | terms the place can actually meet |

**This is the shrink, made precise.** A poor, unscrutinized, low-budget settlement's governor sees
exactly two options — Comply or Defy — every season. A rich, trusted, well-staffed one earns the
other two back **because its own state already proves it can use them**, never because the menu
grew. Four is the ceiling, not the floor, and `00 §2.2`'s "3–5, genuinely different in kind" is read
here as the ceiling it states, not a quota to fill: two responses that differ in kind is already a
real choice, and padding to four when nothing is gated would be `00 §1`'s under-distillation failure
with extra steps.

*Emergent possibility lost if Bargain and Commute were cut outright, rather than gated:* a competent
governor could never trade a resource for softer terms, or reroute an obligation into one the
settlement can actually meet — every directive would flatten into submit-or-rebel with no room for
competence to matter. Gating, not deleting, is what keeps that possibility alive without pricing it
into every season at every settlement.

### 4.3 Commute, and the frequency cap and fail-forward rule, carried unchanged

Commute's terms are a `Debt` tag with `ttl` and `recurs=True` — a claim that fires every season of
its term and expires, not a sixth tag kind (`01 §3.1` still closes the enum at six). **One directive
per settlement per season; a repeated directive of the same type against the same place within a
term costs the principal an escalating `standing` deposit** — carried from v1's frequency-cap
argument unedited: a cap of this shape is cheaper to ship now than to retrofit against an already-
balanced loop later. **Every response is total over the four bands** (P0-3): Failure spends the
point, the deposit does not land, and a `Precedent` tag records what was attempted; nothing here
removes the governor's post — that runs only through `pm.recall` / `pm.audit` (`04`), each requiring
a citable tag or an expired term.

### 4.4 J-N — a Commute term does not carry an emission across seasons, and neither does anything else here

**Stated once, named once, binding on every multi-season object in this document.** The substrate
supplies no cross-season latency (`01 part 2 §9.3`, filed as open ruling **J-N**): there is no
transport by which a Key posted this season arrives next season. A Commute term therefore does not
"schedule" its next firing — the `Debt` tag's `ttl` is **read at the accounting boundary** each
season, and the claim fires because the tag *is still live when read*, never because something was
queued to deliver it. The same is true of any `sm.act` row that spans seasons, and of the
investigation-surface state in `§6`. **If J-N is later ruled the other way, this section is what to
revisit** — nothing here should be re-read as already having latency it does not.

---

## 5. `sm.business` — the ledger emits candidates, it does not present them

Unchanged in its central argument from v1: **the season's business is drawn from the settlement's
own ledger, never authored**, so it needs no content to function and cannot present something the
world has not caused. What changes under change D is the destination of the draw.

```
n = 1 + floor(pressure_band)          # unchanged; 01 §5.2 names pressure the candidate-emission driver
```

| candidate source | becomes |
|---|---|
| an open `Grudge` tag on the place or its governor | someone acts on a grievance this season |
| an unserved `Debt` tag whose term is running | a claim comes due |
| a gauge at or near an extreme band | the condition itself is the business |
| a `Precedent` tag being tested by a new event | the past ruling is cited back |
| an adjacent settlement at an extreme band | a neighbour's crisis is visible from here (`07`) |
| **a facility or presence with an open `investigation_surface` row and a matching unresolved tag (`§6`)** | *(v2)* an investigation opportunity |

**`sm.business` stops resolving these into the player's face and starts emitting them.** Each drawn
item is addressed, by composition role, to `10`'s intake — not wrapped in a new "Candidate"
primitive (`00 §1`'s corollary: a candidate is a row in its own table, not a subsystem), but carrying
the realized-state terms the Light Function needs: durability (from the source tag's `ttl` or the
gauge's distance from its rest value), tie-proximity and identity-touch (read off `Key.causes[]` and
whether the item touches a post the player holds), and the settlement as its holon. **`10` owns the
exact schema; this document conforms to the terms delta §7.1 names and no more, flagged provisional
until `10` lands.**

Three things this still buys, unedited from v1's reasoning: it closes the loop nothing else in the
corpus closes (a verb's own writes become next season's presented business); it needs no authored
content; it cannot present business the world has not caused, because every tag it draws on carries
provenance.

---

## 6. Investigation ⇄ infrastructure — the coupling, in both directions

**Neither direction is designed here.** What a facility does and what an investigation resolves to
are `07`'s and the FI lane's content respectively. This document owns only the **wiring** between
them, expressed as data against interfaces both already declare: `place.form.facilities[]` and
`place.form.presences{}` (`01 §1.1`), and the Depth-gated investigation actions canon already runs
per settlement (`fieldwork_v30.md §1`; anchored per-settlement at
`settlement_layer_v30.md:708`, gated by the facility-tier ladder at `:162`).

### 6.1 Forward — infrastructure opens the surface

One block, appended to `content_registry.yaml` (`00 §9` — a block, not a file):

```yaml
investigation_surface:                       # illustrative rows — shape proposals, not content
  <opportunity_kind>:
    opens_when: {facility: <facility_kind>, tag_kind: <Tag.kind>, tag_key: <str>}
      # OR: {presence: <institution_id>, gauge: <descriptor id>, band: <label>}
    evidence_domain: <fieldwork's own reliability tags — Documentary | Testimonial | Observational | …>
    reachable_by: [<post kinds whose remit includes sm.respond's investigation fork>]
```

A row opens **only** when both the enabling facility/presence exists in the place's own `form` and a
matching unresolved tag is already on the ledger — the same "conditioned, not arbitrary" discipline
`11` uses for world events, applied one document early because the coupling is local rather than
exogenous. Once open, it is one more row in `§5`'s candidate table: a `customs_house` facility
alongside an unresolved `Grudge(key="trade_dispute")` becomes a smuggling-ledger opportunity; a
`church` presence alongside a low `condition.order` band becomes a parish-corruption opportunity. No
new module — the facility/presence catalogue is `07`'s, the evidence domains are the FI lane's, and
`§5`'s table is the only place they meet.

### 6.2 The settlement's own response is a gate, not an investigation

When an investigation-opportunity candidate is surfaced and the player attends it, `sm.respond` is
reused (§4 is the only response engine this document builds) with a **two-response set, both gates,
no roll at this layer**: **Authorize** (opens the case to the FI lane; a post whose remit names the
row's `reachable_by` may act) or **Suppress** (a `gauge_deposit` toward `pressure`, and the row closes
without resolving). Not attending at all is not a third option to build — it is the same
"unattended post" default every other module already has (`01 §4.4`): the row stays open and the
next season's draw re-offers it, exactly like an unserved `Debt`.

**All of the actual investigation** — Depth, Evidence Track, the Examine/Interview/Research/Surveil
roll set, Exposure — is canon's, at settlement anchoring, and none of it is redesigned or restated
here. This document's job ends at Authorize/Suppress.

### 6.3 Reverse — a resolved investigation writes back through the four leaves

The FI lane's own resolution module — outside this suite, its module contract not yet written —
concludes an investigation and needs a Key addressed to the settlement it targeted. **This is a
named gap, not a design: no such key type exists in `00 §9.2`'s minimum set, and none should be
minted here** — appending one is blocked on P0-1 exactly like every other key type this suite
proposes, and the FI lane, not `08`, should author its own emission's shape. What `sm.business`
commits to, once that Key exists, is the translation:

| the Finding implies | write-leaf used |
|---|---|
| a record of what was found, regardless of verdict | a `Precedent` tag, provenance = the Finding's Key |
| the implicated facility or presence should register the exposure | a `gauge_deposit` on `condition.order` or `presence.<institution>` (sign per verdict) |
| the implicated facility should close | a **named** form transition — `sm.business` *names* it; the herald applies it (W-5, `01 part 2 §9.2`); the transition row itself belongs to `07`'s `form_registry.yaml`, not to this document |

No investigation outcome writes an aggregate and none bypasses the herald. The reliability tag the
FI lane already attaches (`fieldwork_investigation.md §4.3`) is read, not re-derived: a Finding built
on `Unverified` evidence should not carry the same weight into a gauge deposit as one built on
`Documentary` evidence, and that discount is FI's own reliability field doing the work, not a second
scoring system invented here.

*Emergent possibility lost if this coupling were cut:* a settlement's own infrastructure would never
generate anything to investigate, and an investigation would never leave a mark on the place it was
about — two systems in the same game, permanently unaware of each other.

> **Falsifier.** A test asserting every `investigation_surface` row's `opens_when` resolves to a
> field that actually exists on `place.form` or a `Tag.kind` in the closed six, and that no
> `sm.business` write from a resolved Finding targets anything but a Tag append, a Gauge deposit, or
> a named (not applied) form transition. Load-bearing on the game: the difference between a coupling
> and a second write path.

---

## 7. The verb budget, counted against `00 §2`

| | v1 | v2 (this document) |
|---|---|---|
| player-invoked modules | `sm.respond` (always 4 responses), `sm.verb` (freely browsable, 4 verbs × 2 forks) | `sm.respond` only |
| distinct leaf choices reachable in a single season | up to **12** (4 + 8) | **2 to 4**, gated by readable state, never browsable beyond what the state admits |
| menus the player opens without being prompted by a situation | 1 (`sm.verb`) | **0** |
| this document's contribution to the whole-game single-digit verb budget (`00 §2.2`) | — | **1** (`sm.respond`) |

**The cut list, with what replaced each entry:**

| v1 object | cut or kept | what produces the outcome now |
|---|---|---|
| `sm.verb` as a player menu | **cut** | `sm.act`, substrate, run every season by the post-holder's preference (§3) |
| Bargain always offered | **cut down to gated** | offered only when `post.budget` and `exposure_band` admit it (§4.2) |
| Commute always offered | **kept as v1 already gated it**, gate tightened in wording only | unchanged in substance |
| `suspicion` as a bespoke post gauge | **cut** | the person-scoped `exposure` gauge (`01 §5.2`) |
| business presented directly to the player | **cut** | emitted as candidates to `10` (§5) |

---

## 8. Module contracts

```yaml
- module: sm.gate
  parent: settlement_management        class: substrate
  scales: [settlement]                 tier: settlement
  resolver: gate                       remit: []          budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]
  emits: [{type: faction.action_declined, terminal: true}]
  state: []          form: []          transitions: []
  disclosure: [{of: decline_reason, inputs: published, presentation: exact, trigger: hidden}]

- module: sm.business
  parent: settlement_management        class: substrate
  scales: [settlement]                 tier: settlement
  resolver: accrual        # O-3: corrected from v1's `derivation`, which the write to `pressure` violated
  remit: []                            budget: null
  consumes:
    - {type: investigation.resolved, from: ["<FI lane module, not yet contracted>"]}
      # GAP, named in §6.3 — not minted here; blocked on P0-1 like every new key type in this suite
  emits:
    - {type: place.business_item_offered, terminal: false}
      # working name; 10 owns the candidate contract's final shape (§5)
  state:
    - {name: pressure, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  form: []
  transitions: [<named, never applied here — the herald applies; row owned by 07>]
  disclosure:
    - {of: pressure, inputs: published, presentation: band, trigger: hidden}

- module: sm.directive
  parent: settlement_management        class: substrate
  scales: [settlement, territory]      tier: settlement
  resolver: derivation                 remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: [{type: place.directive_issued, terminal: false}]
  state: [{name: tag, bucket: tag, writable: true, owner: substrate.ledger}]
  form: []    transitions: []
  disclosure: [{of: directive, inputs: published, presentation: exact, trigger: hidden}]

- module: sm.respond
  parent: settlement_management        class: surface
  scales: [settlement]                 tier: settlement
  resolver: d_sigma        # Bargain rolls; Comply, Commute, Defy and the investigation fork are gates
  remit: [governor]
  budget: {gauge: post.budget, cost: 1}
  consumes:
    - {type: place.directive_issued, from: [sm.directive]}
    - {type: place.business_item_offered, from: [sm.business]}    # via 10's truncation, not directly
  emits: [{type: place.directive_answered, terminal: false}]
  state:
    - {name: exposure, bucket: gauge, writable: true, owner: substrate.gauge}     # person-scoped; O-2
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}     # person-scoped
    - {name: acceptance.support, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: pressure, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  form: []    transitions: []
  disclosure:
    - {of: exposure, inputs: published, presentation: band, trigger: hidden}
    - {of: response_options, inputs: published, presentation: exact, trigger: hidden}
      # the GATE that decides which of the four is offered is itself published in full — §4.2's
      # availability is an input, never a hidden trigger

- module: sm.act
  parent: settlement_management        class: substrate      # O-1: reclassified from v1's implicit surface
  scales: [settlement]                 tier: settlement
  resolver: d_sigma        # unattended and attended runs are the SAME module; only the chooser differs
  remit: [governor]
  budget: {gauge: post.budget, cost: 1}      # per-row cost overrides in the row, unchanged from v1
  consumes: []
  emits: []             # ordinary state writes only; whether one reaches the Slate is 10's call
  state:
    - {name: condition.order,      bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.prosperity, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.defense,    bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support,   bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: accrual.entitlement,  bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,                  bucket: tag,   writable: true, owner: substrate.ledger}
  form: []
  transitions: [<facility-tier advance rows — owned by 07's form_registry; sm.act may NAME them>]
  disclosure:
    - {of: pool, inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle, inputs: published, presentation: exact, trigger: hidden}
```

`sm.directive` stays `derivation`, not `accrual` or `gate`: which order fires is a read over the
principal's and the place's state with no roll and nothing accrues from it — the pure case the
resolver kind was written for.

---

## 9. Property audit

**Scope.** `sm.gate`, `sm.business` and `sm.directive` do not roll — diagnosed on P-iii and P-v only.
`sm.respond` (Bargain branch) and `sm.act` roll and are diagnosed on all five. Above all of it sits
`00 §0.1`: this section cannot certify that a settlement is worth governing, only that its resolvers
are sound.

| property | verdict | reasoning |
|---|---|---|
| **P-i** legible odds | pass | pool and obstacle for both rolling modules are published exactly; only the tipping point and the pressure draw threshold are hidden (E-2). §4.2's gate conditions for Bargain/Commute are themselves published inputs, never a hidden trigger |
| **P-ii** uniform leverage | pass | every response and every `sm.act` row resolves at a governor-scale pool inside the calibrated band; forks change which gauges move, never the pool or obstacle shape; `post.budget` buys attempts, never a modifier (`01 §5.3`) |
| **P-iii** bounded, monotonic | pass | every gauge here is floor/ceiling-bounded with geometric decay (`01 §5.1`); `pressure`'s fixed point is finite for any bounded accrual, checked at declaration |
| **P-iv** graded, recoverable | pass | every response and every `sm.act` row is total over the four bands (P0-3); Failure is fail-forward (a `Precedent` tag, no removal); no outcome here revokes the governor's post |
| **P-v** right engine | pass | the response table is three resolver kinds matched to three question shapes (deterministic choice / genuine uncertainty / threshold on the place's own state); `sm.directive` and `sm.business` are correctly ungated by a roll they do not need |

### 9.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| `sm.act` → gauge → `sm.business` draw → `sm.act` | gauge ceilings + geometric decay; finite fixed point either way | **unmeasured** — campaign-reachable, should be measured before any writer lands |
| directive response → `standing`/`exposure` → next season's Bargain obstacle → response | `derive_ob`'s floor + `exposure`'s own ceiling; the obstacle cannot exceed `ceiling/2 + max_modifier` | **unmeasured** |
| investigation-surface open → Suppress → `pressure` deposit → business draw → re-offer | dedupe on `(owner, kind, key)` bounds the tag ramp; `pressure`'s own fixed point bounds the re-offer rate | **unmeasured**, and it is the one loop this document adds — flagged rather than assumed safe |
| facility → `sm.act` (Build-shaped rows) → facility tier → `sm.act` | per-kind facility ceiling, named from the other end in `07` | **unmeasured**, unchanged from v1's own admission |

### 9.2 What survives, what was cut, and the honest weak point

**N** — one player verb, gated down to as few as two live options; the fork rule (each response
changes a different gauge pair) is what stops a fifth option ever being a magnitude variant of the
first. **R** — the two failure directions the corpus measured are still closed structurally: the
unrecoverable pressure state by the decay law, and the collapse-to-two-best-options by never
presenting more options than the state has earned. **S** — a governance response and a faction
action remain the same object at different tiers. **E** — five modules, none of them a menu; the one
carrying the most weight, `sm.business`, still needs no authored content because the ledger is the
deck, and now the deck deals to `10` instead of to the player's face directly.

**The weakest claim in this document** is the investigation-surface loop's bound (§9.1, row three):
it is asserted safe by analogy to `pressure`'s already-proven fixed point, but nobody has written the
arithmetic for the compound case — Suppress feeding pressure *and* leaving the tag that re-opens the
surface next season. That compound has not been checked the way §2.3's hysteresis guard was checked
in `01`, and it should be, before `06.1`'s block is treated as more than a shape proposal.
