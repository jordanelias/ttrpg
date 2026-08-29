# 06 (part 2) — Faction management: the compositions, collapse, the contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`06_faction_management.md`](06_faction_management.md) — **part 1 first; this continues it**
## Part 1: §§1–4 (the `## Overrides` block, the composition, ethos and divergence, blocs, footing)
## Part 2: §§5–11 (the six political compositions, posture, collapse, contracts, loops, surface, audit)

Section numbering continues from part 1 without a break, and every `§n` cross-reference resolves across
both parts. **Part 1 carries this document's `## Overrides` block** — including the amended authority
model it is written under — and every override cited below is argued there, not here.

**Everything in this part is `substrate` except `fm.posture` (§6)**, which is the whole player-facing
surface of both parts: one verb and two reads (§10).

**Every number below is a shape proposal, not a ledger constant.** Where a number is backed it is cited
by `path:line` and named as canon's.

---

## 5. Promotion, demotion, rivalry, contested power, succession, court — six compositions, zero subsystems

Not eight mechanisms. **Post + Tag + Gauge + edge, in different arrangements.** Each row names the
primitives and the owner; nothing in this table is a module this page ships.

| the political thing | the composition | canon it reads |
|---|---|---|
| **promotion fight** | two qualified holders for one post → `04`'s `pm.candidates` returns >1 → the principal chooses → passed-over gets a `Grudge` tag and a `rivalry` edge | `faction_politics_v30.md:53` already ships **Rival Cohort**: *"at Standing 2–4, a named NPC of the same rank competes for advancement"* — the object exists in canon and needed no invention |
| **demotion** | `post_revoke` + a Standing drop + a `Precedent` tag on the person; the persistent **Dishonored** flag is a `Tag` with `ttl: None` | `:61-94` (§1.0a) ratifies the **magnitudes** — one rank default, 2–3 for scandal/heresy/defection, **Standing −1 dismissal** for excommunication or treason (`:76-80`). Cited; not restated as a v2 table |
| **rivalry** | a PP-724 `rivalry` edge with its own semantics — **an escalation track, not a strain track** | `npc_relational_graph_v30.md:180-193` (§3.5), and `01 §7.2` carries the per-kind rule |
| **contested power** | a `Leverage` tag on the post (`01 §4.2`) — custody without deposition — **capped** by `RELATION_SHARE_MAX` (`01 §3.4`) so a custodian biases a holder and never replaces them | `01 §3.4`'s cap is what stops custody being strictly better than holding the post |
| **succession** | head post vacancy (`04`) → competing bloc projects (`09`) → the winner's practice becomes the institution's | **`12` owns succession.** This page supplies ethos, practice and the blocs that contest it |
| **court of influence** | the `patronage` / `sworn-bond` subgraph among a faction's seated posts, plus §3's blocs over it, plus `05`'s `appeal` reading each holder's convictions | **no object at all.** The court is a *reading* of the edge graph. If it needed an object, `00 §1`'s under-distillation test would already have failed |

**And there is still no `if faction == X` anywhere.** Two factions with the same ethos, the same posture
and different post-holders behave differently, because practice differs. Two factions with the same
post-holders and different ethos behave differently, because divergence differs. That is the C fix: a
faction has a character *and* it is a composition.

**A bloc's collapse is PP-724's defection cascade, not a new mechanism.** When a `sworn-bond` or
`liege-vassal` edge inside a bloc breaks, `npc_relational_graph_v30.md:501-519` (§7, BUILT) already
ships the tier-laddered cascade with hop-attenuation, a capped-and-decaying Fragility term, a
Suppress brake and a tier-3 hard cap, and `:521-528` (§8) already ships the once-per-Accounting
faction-aggregate recompute with an explicit **no-double-count** clause. This page adds nothing to it
and defers to its loop-safety verdict, including canon's own `[NEEDS TESTING — SIM-DEFECT]` caveat that
the magnitudes are illustrative and the gain bound is argued rather than measured.

---

## 6. Posture — the one player verb on this page

Three of v1's orthogonal policy switches become **one form field with a registry of rows** (C-2). This
is `00 §1`'s corollary applied where it bites: *prefer one object with a registry of kinds over several
objects.*

```yaml
# a row in references/form_registry.yaml — adding a posture is DATA, never a branch
posture: <id>
fiscal:      {yield_multiplier: <float>, per_season_deposit: {gauge: acceptance.support, delta: <float>}}
muster:      <which act.muster channel 05 prefers>
succession:  <designation | claim-contest>
gate:        <predicate over divergence band, bloc states, footing band>
```

| | |
|---|---|
| **verb** | `fm.posture` — the head post's remit only; costs 1 from that post's `budget` gauge (`01 §5.3`: budget buys **actions**, never modifiers) |
| **resolver** | `gate`. Every posture change is a form transition, so it is gated on state, never rolled (`01 §2.2`) |
| **emits** | `form.transitioned` — a **crossing fact**, never a forecast (`01 §2.2`) |
| **hysteresis** | **REQUIRED**, because posture pairs are reversible. This is what makes v1's *"a faction that oscillates its fiscal stance has a visible record of doing so"* structural instead of a bookkeeping tag: **it cannot oscillate**, because the band and the dwell forbid it |
| **gated by divergence** | §2.4 row 3 — an institution cannot adopt a posture its own officers will not operate |

**Why this is distillation and not amputation.** v1's three switches gave 3 × 2 × 2 = 12 combinations,
most of them incoherent (extraction plus entitlement-first plus designation is not an institution, it
is three sliders). A posture row is a **coherent institutional stance** carrying all three terms at
once, the catalogue is open data, and adding one is a row rather than a fourth switch. What is lost is
the incoherent corners of a cross product; what is gained is that a player reads one word instead of
three, and that a faction's stance can be *gated* as a whole.

**Extraction's cost stays a per-season deposit, not a threshold** — carried from v1 §5 with its
reasoning: what reads as injustice is a *change* in what is taken, not the level of it, so the cost
belongs on every season the posture is held.

*Emergent possibility lost if posture were cut:* an institution could not change its practice without
changing its people — every reform would have to be a purge.

---

## 7. Collapse by gate — and by a gate that can actually be reached

### 7.1 Why not a track

A hit-point track needs three things this design cannot give it and does not want: **a writer for an
aggregate** (AU-1 forbids it), **a poll** to notice zero, and **a flip** from alive to eliminated in one
step. The gate needs none of the three. Nothing detects a collapse; a gate reads a field.

### 7.2 The four bands

Read at the accounting boundary, from state. **No emission carries anything across a season** (§9.3).

| band | gate | what it means |
|---|---|---|
| **Whole** | head post seated | acts at every tier where it holds a post (`05`) |
| **Contracted** | head seated; **no post at province tier or above** | acts locally only. `footing` falls at the higher nodes because the sum has fewer terms — nothing writes it down. Charters whose patron is this faction begin lapsing (§4.4). This is canon's **city-state** (`settlement_layer_v30.md:1073-1075`) with no partial stat sheet, because every stat was already a derivation over what is held |
| **Silent** | head post **vacant** | takes no action at any tier (ED-IN-0201, `05`). Its other posts fall vacant on their own terms; its holdings' governance posts become claimable. Its ledger, ethos and blocs persist |
| **Dissolved** | head vacant **AND** `04` yields **no seatable candidate** for `DISSOLVE_DWELL` consecutive seasons — `pm.candidates` empty, **or** every candidate in it fails `04 §4.0`'s acceptance gate (v3: `04` now lets a person refuse a post, so a non-empty list of refusers is the same institutional fact as an empty one) | `posture → dissolved`, `reversible: false`. Posts revoked, charter edges transitioned to `lapsed`, holdings' governance posts vacant. **The entity and its ethos persist in the store** |

Every band is **visible**, **graded**, and reached by a gate over readable state. Three of the four are
exited in both directions.

### 7.3 The amendment, stated precisely (C-4)

v1 `06 §6` wrote: *"A faction that stops acting can **always** produce a claimant."* Combined with *"no
elimination check"*, that makes every faction immortal — the world can lose a faction's power but never
a faction, so nothing can take its place, and a faction with a vacant head and no candidate sits
forever as a husk that neither acts nor ends. **That is the dead end, and it is what C-4 removes.**

The fix is one distinction, and it preserves the delta spec §9.5 carry-forward rather than dropping it:

> **The immortal seat node guarantees the DEMAND, not the SUPPLY.**

- **Demand is always expressible.** The head post's vacancy resolves at a node that cannot be lost, so
  the world always knows this faction *wants* a head. That is v1's recoverability, unchanged, and it is
  what stops a vacancy being an instant death.
- **Supply is bounded and can be empty — and v3 adds a second way for it to be empty that is better
  drama than the first.** A faction can fail to find anyone *qualified*; it can also fail to find anyone
  *willing*. `04 §4.0`'s acceptance gate makes the second reachable, and an institution nobody will
  serve is a more legible end than an institution with nobody left. Both routes feed the same gate.
- `03`'s population is bounded and `04`'s candidate gate is
  real — a rank floor, the caste matrix (`faction_politics_v30.md:653-668`), remit, and canon's own
  successor requirement at **Standing 4+** (`settlement_layer_v30.md:1077`). An empty candidate set is
  a reachable state, and sustaining it for `DISSOLVE_DWELL` seasons is what ends an institution.

⚠ **The gate is `04`'s candidate set being empty — not "Standing 4+" — and the difference matters under
the amended authority model.** Canon's *Standing 4+* is one term inside that gate, and it is cited as
evidence that a rank floor belongs there at all, not adopted as a threshold this page owns. **If the
ratified 0–7 ladder is later replaced — its granularity changed, its rungs renamed, or the whole track
re-derived — §7.2's dissolution band is unaffected**, because it reads *"is the candidate set empty"*
and never *"is anyone at rung 4"*. That independence is deliberate: the collapse gate is the single most
irreversible thing in the game, and binding it to a number in another lane's ladder would make a rank
retune silently able to dissolve a duchy.

`DISSOLVE_DWELL` is a **shape proposal** and its job is to keep a one-season accident from dissolving a
duchy. Canon states the condition (`:1077`) and states no dwell; the dwell is this page's, and it is
flagged as such.

**Reachability bar, in both directions — and this is the falsifiable claim:**

| direction | bar |
|---|---|
| **recovery** | from Silent, a single qualifying candidate re-seats the head and the faction returns to Whole or Contracted. Must be reachable in a seeded campaign |
| **end** | `pm.candidates` must be able to return empty for `DISSOLVE_DWELL` consecutive seasons given `03`'s bounded population and `04`'s gate. **If it cannot, dissolution is unreachable and v1's dead end is back** |

### 7.4 What survives a dissolution, and why that is the interesting part

The faction entity and its **ethos** persist. A later movement can charter a **new** faction citing the
dead one — new `charter_season`, new entity, inherited purpose. That is how a defunct institution
becomes a cause rather than a footnote, it is the Restoration Movement's exact shape, and it costs
nothing: identity is immutable, so a dissolved faction is a perfectly good thing to point at.

---

## 8. Module contracts

**Five modules** (v3: `fm.fisc` is new, C-7), in `00 §7`'s shape. **Every one of them consumes
nothing** — all five read state at the accounting boundary — which is why §9.3's J-N constraint and
§9.4's J-O exposure are both narrow here.

```yaml
- module: fm.derive
  parent: faction_management
  class: substrate
  scales: [settlement, territory, peninsula]      # evaluated per node; §4.2
  tier: null
  resolver: derivation
  remit: []                 # not invocable. Nobody spends an action to recompute a derivation.
  budget: null
  consumes: []              # reads state at the boundary (J-N, §9.3); survives J-O (§9.4)
  emits: []
  state:
    - {name: faction.practice,   bucket: gauge, writable: false, owner: fm.derive}
    - {name: faction.divergence, bucket: gauge, writable: false, owner: fm.derive}
    - {name: faction.footing,   bucket: gauge, writable: false, owner: fm.derive}   # per node; §4.2
    - {name: faction.weight,     bucket: gauge, writable: false, owner: fm.derive}
    - {name: faction.force,      bucket: gauge, writable: false, owner: fm.derive}   # units: 12 owns them
    - {name: bloc.pull,          bucket: gauge, writable: false, owner: fm.derive}
    # v3, C-8 (§3.1). `bucket: gauge` is 00 §7.1's declared WART, and this row shows it at its worst:
    # members is a SET of post ids, not a scalar. The bucket enum has no home for a derivation, and
    # inventing a fifth bucket is the error 01 exists to prevent — so the falsifier does the work:
    # `writable: false` guarantees it never acquires a gauge instance. Reported to 01 with the rest.
    - {name: bloc.members,       bucket: gauge, writable: false, owner: fm.derive}
  form: []
  transitions: []
  disclosure:
    - {of: faction.practice,   inputs: published, presentation: band,  trigger: hidden}
    - {of: faction.divergence, inputs: published, presentation: band,  trigger: hidden}
    - {of: faction.footing,   inputs: published, presentation: band,  trigger: hidden}
    - {of: faction.weight,     inputs: published, presentation: exact, trigger: hidden}
    - {of: faction.force,      inputs: published, presentation: band,  trigger: hidden}
    - {of: bloc.pull,          inputs: published, presentation: band,  trigger: hidden}
    - {of: bloc.members,       inputs: published, presentation: exact, trigger: hidden}  # who is in the wing IS the read (§10)

# v3, C-7 — the treasury is a STOCK, not a derivation (§4.6). It left fm.derive because 00 §7.1's
# falsifier forbids a `writable: false` name from being a real gauge id, and it needs one.
# Shape precedent: 07's pl.gauges, the suite's existing boundary-accrual module.
- module: fm.fisc
  parent: faction_management
  class: substrate
  scales: [peninsula]
  tier: null
  resolver: accrual
  remit: []                 # nobody spends an action to collect revenue
  budget: null
  consumes: []              # reads 07's residual(place) over controlled places at the boundary
  emits: []
  state:
    - {name: faction.treasury, bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure:
    - {of: faction.treasury, inputs: published, presentation: exact, trigger: hidden}   # exact BECAUSE spent directly, per 07:537

- module: fm.bloc
  parent: faction_management
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: []                 # blocs are not invoked; they are gated at the boundary
  budget: null
  consumes: []
  emits: [{type: form.transitioned, terminal: false}]      # a crossing fact; §3.4
  state:
    - {name: bloc.cohesion, bucket: gauge, writable: true, owner: fm.bloc}
    - {name: tag,           bucket: tag,   writable: true, owner: substrate.ledger}
  form: [{entity_kind: bloc, field: state}]      # v3, C-8: `members` is DERIVED, never a form field (§3.1)
  transitions:
    - bloc.form_latent          # gate: §3.2
    - bloc.latent_to_open       # reversible pair -> hysteresis REQUIRED (§3.4)
    - bloc.open_to_latent
    - bloc.open_to_schism       # reversible: false
    - bloc.open_to_reconciled   # reversible: false
    - bloc.to_dissolved         # reversible: false
  disclosure:
    - {of: bloc.cohesion, inputs: published, presentation: band, trigger: hidden}

- module: fm.posture
  parent: faction_management
  class: surface                                  # THE ONLY SURFACE MODULE ON THIS PAGE
  scales: [peninsula]
  tier: null
  resolver: gate
  remit: [head]
  budget: {gauge: post.budget, cost: 1}           # buys an action, never a modifier (01 §5.3)
  consumes: []
  emits: [{type: form.transitioned, terminal: false}]
  state:
    - {name: acceptance.support, bucket: gauge, writable: true, owner: substrate.gauge}  # posture's deposit
  form: [{entity_kind: faction, field: posture}]
  transitions: [ALL posture rows declared in references/form_registry.yaml]
  disclosure:
    - {of: acceptance.support, inputs: published, presentation: band, trigger: hidden}

- module: fm.collapse
  parent: faction_management
  class: substrate
  scales: [peninsula]
  tier: null
  resolver: gate
  remit: []                 # nobody spends an action to end a faction; the gate does it
  budget: null
  consumes: []              # reads the head post and 04's candidate set at the boundary
  emits: [{type: form.transitioned, terminal: false}]
  state: []
  form: [{entity_kind: faction, field: posture}]
  transitions: [faction.to_dissolved]             # gate: §7.2; reversible: false
  disclosure: []
```

`writable: false` on all seven derivations **is** the enforceable form of *no aggregate is ever
written*; a contract row declaring one writable is a defect the shape check catches without anyone
remembering the rule. `fm.posture` is the only row with a non-empty `remit`, which is the whole of this
document's player surface.

**The count is still seven, and that is arithmetic rather than luck.** v3 removed `faction.treasury`
from the derivations (C-7 — it is a stock, §4.6) and added `bloc.members` to them (C-8 — it was stored
form and is now derived, §3.1). The two fixes are the *same* fix pointed in opposite directions: v2 had
one stock mislabelled as a derivation and one derivation mislabelled as stored form. **Exactly one
faction-scoped gauge is `writable: true` across this document — `faction.treasury`, in `fm.fisc`** —
which is a one-line grep and the narrowed form of §1's claim.

**Why `faction.weight` and `faction.footing` are not magnitude variants of one another** — the
under-distillation test from `00 §1`, applied where it is closest to failing. `weight` reads **posts and
places held** (what you hold; Jordan's 2026-07-13 ruling that factions hold *people* and that the number
of people and the weight of their positions carry a faction's value). `footing` reads **acceptance
gauges** (what is accepted of you). They diverge in both directions and the divergence is the game: a
conquering occupier is heavy and unaccepted; the Church in a cathedral city is light and accepted. If
they could not diverge, one would be the other's magnitude variant and this document would ship one.

---

## 9. Loops, gates, and the two open rulings

### 9.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| **divergence** — divergence → bloc forms → members act together → appointments shift → practice moves → divergence | `divergence ∈ [0,1]` by arithmetic (§2.3); membership bounded by the faction's post count, which is data-computable | **unmeasured.** Campaign-reachable, so measurable against a control before any writer lands. `tools/balance_oracle.py` is the campaign instrument (`CLAUDE.md` §7); note it is a *campaign* instrument, so a change that is campaign-unreachable gets two identical arms and a fake control |
| **cohesion** — cohesion → bloc state → members act together → cohesion | `rest + a/λ` for bounded per-season accrual, checked **at declaration** from the descriptor registry with no campaign run (`01 §5.1`) | **bounded arithmetically**; per-cycle gain **unmeasured** |
| **bloc state flicker** — `latent ↔ open` | `θ↑ − θ↓ ≥ H_MIN(cohesion)` and `dwell ≥ 1`, checked **at load** (`01 §2.3`) | **bounded arithmetically.** The only loop here with a proved bound, and why hysteresis is mandatory |
| **footing ↔ settlement acceptance** | canon's saturating `T/(T+K)`; `∂footing/∂q` shrinks as `T` grows (`settlement_layer_v30.md:168`) | **MEASURED, and it is canon's measurement, not this suite's**: bounded 0–7 and convergent over 30 seasons under mission shocks (`:173`). The only measured bound cited in this document |
| **defection cascade** — a bloc edge breaks → Fragility → sever threshold → more breaks | hop-attenuation ½/hop, Fragility cap +3 with −1/season decay, Suppress brake, tier-3 hard cap (`npc_relational_graph_v30.md:501-519`) | canon's own verdict is **damped and bounded**, carrying canon's own `[NEEDS TESTING — SIM-DEFECT]`: *"the per-cycle-gain bound is a design argument, not yet sim-measured."* Repeated here rather than upgraded |
| **treasury** *(v3, §4.6)* — residual → treasury → contract muster → units → upkeep → treasury | `rest + a/λ` from `01 §5.1`, checked **at declaration** against the descriptor registry with no campaign run. Upkeep is a *negative* flow, so the loop is self-damping in the direction that matters: more units means less money means fewer units | **bounded arithmetically**; per-cycle gain **unmeasured**, and it is campaign-reachable, so `tools/balance_oracle.py` is the instrument if `05` lands the spender |
| **collapse** | **terminating.** `posture → dissolved` is `reversible: false`, so the faction leaves the loop permanently (§7.2) | not a gain loop; a one-way absorbing state with a dwell in front of it |

### 9.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| bloc formation | divergence, the PP-724 edge graph, conviction distances — **never `knot`** (ED-POL-11) | no bloc; nothing is emitted |
| bloc `latent ↔ open` | cohesion band and the dwell, against the registry at load | load failure for a missing band; no transition at runtime |
| schism | `bloc.pull`, divergence, cohesion, dwell | the bloc stays open; its project keeps advancing (`09`) |
| posture change | the posture row's gate, the divergence band, `post.budget ≥ 1` | the posture is **not in the option set** — an absence, not a penalty (`01 §4.3`) |
| charter lapse | the patron's derived footing at the boundary | privileges lapse automatically; nobody revoked anything (`settlement_layer_v30.md:651-661`) |
| dissolution | the head post's `holder_id`, and whether `04` yields any candidate who both qualifies **and** accepts, for `DISSOLVE_DWELL` seasons | the faction stays Silent — recoverable, and that is the point |
| bloc dissolution *(v3)* | `\|members(b)\| < 2` **and** `cohesion ≤ θ_dissolve` — the gauge term is what keeps a derived-membership gate legal under `01 §2.4` (§3.4) | the bloc stays in its current state |
| charter *(v3, §3.5a)* | **`05`'s gate, not this page's** — `05 part 2 §5.4`'s `act.charter` reads `bloc.state == in-schism`, a `founding_claim` Precedent, and bloc membership; `06` supplies the values and emits the crossing fact | the claim stands and the bloc waits. ⚠ `in-schism` is `reversible: false`, so **if `act.charter` is ever cut the state becomes a silent terminal sink** — §11.1's end-to-end falsifier is written against exactly that |

### 9.3 ⚠ J-N — no cross-season latency, and this page does not assume any

`01 part 2 §9.3` verifies against the tree that `drain_tick` has zero production callers, that
`next_tick` **raises** on a non-empty queue, and that the guard **prevents** cascades rather than
scheduling them late. Filed as open ruling **J-N**.

**Every gate on this page reads state at the accounting boundary.** Divergence is recomputed, cohesion
is read, the candidate set is queried, the patron's footing is derived. **Nothing here is posted to and
fires later.** A dwell requirement is not a latency: it is a gate that reads *how long a condition has
held*, which is a property of current state (a tag's `created_season`, a post's vacancy season), not a
message in flight. **J-N is the ruling that would change this**, and if it rules for reactive chains,
§3.4's transitions and §7.2's bands are what to revisit.

### 9.4 ⚠ J-O — what on this page depends on Key consumption

| | survives a "Keys are telemetry only" ruling? |
|---|---|
| `fm.derive`, `fm.bloc`, `fm.collapse` — all `consumes: []` | **yes.** They are boundary reads already; a J-O ruling changes nothing about them |
| `fm.posture`'s `form.transitioned` emission | **yes as a log.** Only a consumer's *reaction* would be at risk, and nothing on this page consumes |
| `Tag.provenance` pointing at a Key, and `causes[]` as the chain from a grudge to a schism | **yes** — telemetry and causality are what the alternative keeps |

**This document is robust to J-O**, and that is a consequence of designing every gate as a boundary
read rather than a reaction. It takes no position on the ruling.

---

## 10. The player-facing surface

**One verb and two reads, against everything in §§1–8.** `00 §2.3` item 4: if a document's surface
table is longer than its substrate table, the ratio is backwards.

| what the player is asked | how often |
|---|---|
| **`fm.posture`** — as head of a faction, change the institution's posture. Available only from the head post's remit, gated by divergence, costed from that post's budget, hysteresis-bound so it cannot be flipped back next season | rarely — a handful of times per campaign, and never as a menu they browse |

| what the player reads (never operates) | how it reaches them |
|---|---|
| the **band** of their faction's divergence and footing — *"the ministry is drifting"*, *"you are a power in Gransol and nowhere else"* | on a Slate item or a faction summary; band, never a number |
| **that a wing exists, and who is in it** — the bloc's members, not its cohesion value | as a **situation** on the Slate (`10`), never a screen |

| substrate the player never touches |
|---|
| forming, joining, dissolving or naming a **bloc** · `cohesion` · `bloc.pull` |
| `practice`, `divergence` or `footing` as **numbers**, or any band edge |
| the **schism** gate, the **charter-lapse** gate, or the **dissolution** gate — all boundary reads |
| creating, chartering or ending a **faction** — `05` and `12` own the acts; the gates own the rest |
| **collecting revenue** — `fm.fisc` is an accrual at the boundary (§4.6); the player spends the treasury through `05`, and never operates the filling of it |

**Substrate objects: 1 entity kind (bloc) · 7 derivations · 6 bloc form transitions + 1 faction one ·
2 gauges (`bloc.cohesion`, `faction.treasury`) · 0 new registry files. Surface: 1 verb, 2 reads.**
⚠ **v3 moved two objects between buckets and added no new kind of thing.** `faction.treasury` moved
out of the derivations into the gauges (C-7); `bloc.members` moved out of the **form bucket** into the
derivations (C-8) — note the transition count is unchanged at six, because **all six always targeted
`bloc.state` and none ever targeted `members`, which is precisely why storing `members` in `form` was
illegal.** The document gained one module (`fm.fisc`) and **no player verb**.

---

## 11. Property audit

**Scope, and the honest limit. Nothing in this document rolls.** `fm.derive` is a derivation;
`fm.bloc`, `fm.posture` and `fm.collapse` are gates. **No N/R/S/E verdict is offered for a derivation or
a gate** — manufacturing one for state with no draw is the error the methodology names, and v1 was
right to refuse it. Above that sits `00 §0.1`: **a resolution-scoped audit cannot ask whether a design
expresses the game.** This page could pass everything below and still be the wrong model of an
institution; the instrument for that is the elegance criterion, and its answers here are the one-line
loss statements, the `## Overrides` block, and §8's under-distillation defence of `weight` vs `footing`.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass on divergence and footing; bounded-with-unmeasured-gain on the loops** | `divergence ∈ [0,1]` by arithmetic on two normalised vectors — no clamp, no campaign run. `footing ∈ [0,7]` by canon's saturating form, with canon's own 30-season convergence result. `cohesion` **and, from v3, `treasury`** are bounded at `rest + a/λ` at declaration, by the same registry check and with no new arithmetic (§4.6). **Monotone in the aggregate and deliberately not in one officer's distance** (§2.3 pt 4) — a designed non-monotonicity, stated rather than hidden |
| **P-v** right engine | **pass** | every module here is `derivation` or `gate`. A faction's worth, its drift and its wings are computations over state already on the board; rolling for any of them would be a resolution where the answer exists. Every form transition is a gate on purpose (`01 §2.2`) |
| **P-iv** graded failure | **pass, and it is what C-4 restores** | §7's four bands are visible, graded and gated; three of four are exited in both directions; the fourth has a dwell in front of it. **The claim is only true if the end is reachable** — which is the first falsifier below, and the exact thing v1 got wrong |

### 11.1 Falsifiers — a claim with no falsifier is not a claim

| claim | falsifier | load-bearing on |
|---|---|---|
| **Collapse is reachable in both directions** (§7.3) | a seeded campaign in which **at least one faction reaches `dissolved`** and **at least one recovers from Silent to seated**. If dissolution never fires across the seeded set, v1's dead end is back and C-4 failed | the game — whether the world can lose an institution |
| **No aggregate is written, and exactly one faction stock is** (§1, §4.6, §8) | **two halves, and v3 needs both.** (a) no `writable: false` state name appears as a gauge id in `references/descriptor_registry.yaml`, and no `fm.derive` row is declared writable; (b) **exactly one faction-scoped gauge id in this document is `writable: true`, and it is `faction.treasury`** — a second one is a new stored faction stat and the thing §1 forbids. Half (b) is what keeps C-7 from being a hole in AU-1 rather than an exception to it | the write rule itself; it is the one hazard the `bucket:` wart opens |
| **The treasury is a stock and not an aggregate** (§4.6) | a test that `faction.treasury` has **no derivation** anywhere in the suite — no function computes it from current state — and that its only writers are `fm.fisc`'s boundary deposit and `05`'s spends. **If anyone writes a `treasury()` derivation, the C-7 argument is false and the row should go back to `fm.derive`** | the muster economy: whether `05 part 2:68` can be built at all |
| **Bloc membership is derived, never stored** (§3.1, C-8) | a test that no `bloc` entity carries a persisted `members` field, that `fm.bloc`'s `form:` names only `state`, and that `members(b)` recomputed twice in the same season from the same graph returns the same set. **Plus the negative:** mutate a `patronage` edge inside a bloc and assert `members(b)` changes at the *next read* with no transition having fired | the exact defect this suite prosecutes as `01`'s O-3 — a stored snapshot of a graph fact |
| **A schism can finish** (§3.5a, T2-1) | **an end-to-end test, not a unit one:** a seeded campaign in which a bloc reaches `in-schism` **and a new faction entity exists afterwards** whose `identity.ethos` equals `practice(members)` at the schism season and whose `charter_season` is that season. **Unit tests on either side pass while the seam is broken — which is how v2 shipped with no charter at all** — so the test has to span both | the marquee possibility of change C: a new institution emerging from inside an old one |
| **Divergence is bounded without a clamp** (§2.3) | an arithmetic test over the registry alone: for every faction, `ethos` and every `conviction_projection` normalise to `Σ\|w\| = 1`, therefore `divergence ∈ [0,1]`. **Fails at load** if any ethos row is unnormalised | the difference between a bounded measure and one that needs a clamp nobody checks |
| **`divergence` is `None`, not `0.0`, at zero seated posts** (§2.3 pt 3) | a test constructing a faction with every post vacant and asserting every consumer **declines to fire** rather than reading perfect alignment | the Silent band behaving as succession pressure rather than as a healthy institution |
| **Blocs cannot form on spiritual ties** (§3.2, ED-POL-11) | a test that the bloc connectivity set contains exactly PP-724's six kinds and **excludes `knot`**; and that a faction whose officers share only `knot` edges produces **no** bloc | the anti-conflation ruling, honoured by construction |
| **Bloc states cannot flicker** (§3.4) | `01 §2.3`'s load-time hysteresis test, applied to `latent ↔ open`: `θ↑ − θ↓ ≥ H_MIN(cohesion)` and `dwell ≥ 1` | the Slate — a flickering bloc emits a candidate every season |
| **Bloc formation is neither degenerate nor inert** (§3.2) | a reachability test in both directions: at max reachable divergence a faction of ≥4 seated posts yields **≥2 distinct components**; at low divergence it yields **none** | whether a bloc is a gate or a decoration |
| **This page adds no player verb beyond one** (§10) | a test that exactly one module in `06`'s contracts has a non-empty `remit` | the playing-surface budget, `00 §2.2` |
| **The magnitude crosses in one direction only** (§4.5) | a test that no module in this document writes a settlement-owned gauge that `fm.derive` also reads — with `fm.posture`'s `acceptance.support` deposit as the **one declared, named exception**, since it is a posture cost and not a re-derivation | Q-5's double-count hazard, bounded locally |

**Each of these guards satisfies `CLAUDE.md` §0.1 point 5's load-bearing predicate** (`00`'s P0-4): every
one is load-bearing on the game or on an exported artifact, and none guards apparatus. The first and the
last are the two that would be worth building first, because both are cheap and both catch a defect that
is silent.

### 11.2 The four qualitative verdicts

**Necessary** — one new entity kind (bloc), seven derivations each with a named consumer, one form
field, and one stock. The relation taxonomy is PP-724's, adopted not invented; the footing arithmetic
is canon's, adopted not invented; the collapse condition is canon's, restored not invented. What this
page genuinely adds is **divergence**, **the bloc**, and **the summation domain that makes footing
multi-scale** — three objects, each with a stated loss-if-cut. **The treasury (§4.6) is not a fourth
addition:** the quantity was already being spent by `05`; v3 only put it in a bucket that can hold it.

**Robust** — tested at both extremes. A faction with no holdings still has weight from its posts and can
still seat a head. A faction with every holding is bounded by canon's saturating footing and by
`05`'s flat action ceiling, which does not scale with success. A faction with one seated officer is
fully described by that officer, and a faction with none returns `None` rather than a plausible lie.

**Smooth** — a faction, a bloc and a place are the same primitives at different owners; `practice` is one
derivation with three consumers; `footing` is one derivation at three tiers; a bloc's collapse is
PP-724's cascade rather than a second one.

**Elegant** — five modules, one new entity kind, no elimination routine, no per-faction branch, no court
system, no succession system, and a player surface of one verb and two reads. **The honest deduction:
the contested object in this document is still the bloc**, because it is the one thing here that is a new
stored entity rather than a derivation or an adopted mechanism. §3 argues it — no ethos, no treasury, no
posture, one gauge, **membership derived rather than stored (v3, C-8)** — rather than assuming it.

⚠ **And v3 tested that deduction rather than repeating it.** Cutting the bloc and re-deriving a wing on
demand was drafted and **fails on three counts that are not stylistic**: a re-derived component has no
identity, so it cannot accumulate a voting record; it cannot hold `in-schism` as a *terminal* state,
because a derivation has no terminal states; and it **cannot freeze `ethos = practice(members)` at the
schism season**, which is §3.5a's entire handoff and this suite's only route from an existing
institution to a new one. **What the cut correctly identified was the membership storage, and that is
what v3 removed.** If the argument still fails, the correct verdict remains *cut the bloc and lose court
politics and faction emergence*, not *shrink it further* — the shrinking has now been done.
