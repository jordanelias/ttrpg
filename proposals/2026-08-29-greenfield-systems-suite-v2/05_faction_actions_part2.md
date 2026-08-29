# 05 (part 2) — Faction actions: the action set, resolution, contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`05_faction_actions.md`](05_faction_actions.md) — **part 1 first; this continues it**
## Part 1: §§0–4 (the playing surface, the per-tier gate, the per-post budget, `appeal`,
## `act.contest_influence`) — and the `## Overrides` block, which governs both parts
## Part 2: §§5–10 (the eight action rows, the resolution shape, the two effects constraints,
## J-N and J-O, the module contracts, the property audit)

---

## 5. The action set — eight rows, one shape

An action is a **row, never a branch.** Adding one is a registry edit.

```yaml
- action: <id>
  remit_kinds: [<post kinds whose remit may contain this>]
  tiers: [<rungs at which it is available>]              # NEW (v2) — §1.1
  binds: {<slot>: <registry id>}                          # NEW (v2) — §4.5
  attrs: [<attr_a>, <attr_b>]                             # keys on descriptors.ATTRIBUTES; never literal
  target: <what supplies target_score for derive_ob>
  ob_site: {target: <gauge id>, shape: U|SO|DO|BI|GATE,          # NEW (v2) — 01 §6's obstacle-
            pool_min: <int>, pool_max: <int>,                     # reachability gate, in 00 §7's
            ob_modifier_min: <int>, ob_modifier_max: <int>,       # EXACT field names (corrected;
            pool_opposed_min: <int>, pool_opposed_max: <int>}     # this page's earlier three-field
                                          # form was its own invention). `pool_*` are 6-18 for every
                                          # row by §6's pool shape and are SITE-LOCAL, not global —
                                          # there is no POOL_MAX in `engine/`. A DO/BI row without
                                          # `pool_opposed_*` is UNEVALUABLE, not passing (01:621)
  symbolic_vector: {hierarchical: ±, sacred: ±, instrumental: ±, traditional: ±}
  signal_weight: {<world signal>: <weight>}
  cost: {budget: 1, gauge_deposits: [...]}
  effects: {overwhelming: [...], success: [...], partial: [...], failure: [...]}   # TOTAL over four
```

| family | what it does | shape | `derive_ob` target |
|---|---|---|---|
| **`act.muster`** | raise a unit at a place (§5.2) | **gate** | — |
| **`act.govern`** | act on a place you hold — deposit into its `acceptance`, `condition` and `accrual` gauges, or name a facility-tier advance. **`08`'s eight settlement rows are rows of this family** (§5.5) | **U** | the place's own condition |
| **`act.campaign`** | declare a campaign against an adjacent holding (§5.1) | gate, then a declared seam | — |
| **`act.treat`** | offer a bilateral agreement — **creates a `treaty` edge with its terms in its tags** (O-5.5; `12` owns the kind) | **SO** | the counterparty's `acceptance` |
| **`act.commission`** | appoint, recall, or attempt custody — routes to `04` | gate / **SO** | per `04` |
| **`act.inquire`** | spend an action to learn (§5.3) | **U** | the concealing party's relevant score, where one exists |
| **`act.contest_influence`** *(v2)* | raise presence at a place you do not hold (§4) | **DO + lead Ob** | the defending institution's presence **lead** over the challenger's (§4.1) |
| **`act.charter`** *(v3)* | charter a new faction entity on a standing founding claim (§5.4) | **gate** | — |

**`tiers:` and `remit_kinds:` are what make this a *whole-game* action registry rather than a faction
one.** A row with `tiers: [settlement], remit_kinds: [governor]` is a settlement verb; a row with
`tiers: [peninsula], remit_kinds: [head]` is a national one; **the dispatcher cannot tell them apart**,
which is precisely what §10.1's S-property claims and what O-5.11 makes literally true (§5.5).

**`act.motion` is cut, not moved (O-5.12).** `12 §5`'s `ad.motion` is the fuller design of the same
event and is self-contained — its own `remit: [head, minister]`, its own `post.budget` cost,
`price(magnitude)` against the proposer's `standing`, a monotone `vote_bar(magnitude)`, and a published
`vote_weight`. A post-holder raising a motion invokes `ad.motion` directly, and `fa.gate` counts it in
`action_modules` (§1) like any other row. **One motion, one owner.**

### 5.1 `act.campaign` is a gate over a declared seam, not a stub

Force-on-force resolution is out of this suite's scope, and saying so **with a specified seam** is
different from leaving a hole.

| | |
|---|---|
| **the gate** (here) | the target is adjacent to a held node; a `commander` post is filled; the committed units exist and are assigned to the field |
| **the seam** | `resolve_force(attacker_units, defender_units, place) → Degree` — one call, one return, on the single-owned ladder |
| **the consumption** (here) | the degree drives an Entry Terms fork: on a lesser margin the taken place keeps its arrangements and seeds `acceptance.legitimacy` high; on a decisive one it does not and seeds low |

Its interface is fully specified in both directions, so the caller is complete and testable against a
stand-in, and the seam returns a `Degree` — the same currency every other action consumes — so whatever
implements it cannot introduce a second degree semantics for one event class.

### 5.2 `act.muster` — two economies, separated at birth

Four of four surveyed franchises implement the levy and the professional soldier as **different
economies, not different tiers.** Building one muster now and splitting it later means splitting a
mechanic that has already accreted grounding, effects and goldens; building two channels from the start
costs one extra registry row.

| | **`act.muster.levy`** | **`act.muster.contract`** |
|---|---|---|
| pays with | the place's `accrual.entitlement` gauge | the faction's `treasury` **stock** gauge (§5.2a) |
| rationed by | how fast entitlement accrues — a property of the place | how much money there is |
| upkeep | none | recurring, larger when assigned to the field |
| quality | bounded by the place's `condition` band | bounded by price |
| consent cost | a deposit into `acceptance.support`, scaled by the unit's quality tier | the same deposit at the same scale |

Recruitment is coercive in both channels: the per-unit consent deposit is the live dial, and separately
and rarely a **gate** — a place whose `acceptance.support` band is at *revolt* supplies no soldiers in
either channel. Scoping the gate to the revolt band is what keeps it from double-counting the dial.
`act.muster` is a **`gate`, not a `d_sigma`**: whether you can afford a unit is a question whose answer
is on the board, and rolling for it is the wrong-engine defect this tree is most prone to.

**Muster raises no aggregate.** It produces a unit record (`12 §2.1`). Faction military weight is
*derived* from units held; building it the other way — mustering raising the number that gates what
mustering can produce — is a loop with no external term in it at all.

### 5.2a The treasury is a **stock**, not a derivation — the defect and the fix (O-5.10)

**The defect, stated plainly because it was real and this page shipped it.** `06 part 2 §9` declares
`faction.treasury` as `{bucket: gauge, writable: false, owner: fm.derive}` — a derivation. The table
above spends it, and the row below charges recurring upkeep against it. **You cannot decrement a
derivation:** a derivation recomputes from current state every boundary, so every payment is silently
undone at the next accounting and the contract channel is free. Two independent readers found this from
opposite ends — *"what does the muster economy spend?"* and *"does the fiscal spine fit the four write
leaves?"* — which is the strongest signal available that it is not a wording problem.

**The fix is a vocabulary distinction the suite already needed, not a new object.** AU-1 forbids
*storing an aggregate*, and `01 §2.1` now separates the two things that rule was collapsing:

| | **aggregate** — may not be stored | **stock** — is an ordinary gauge |
|---|---|---|
| definition | recomputable from **current** state alone | **path-dependent**: its value carries the history of what was put in and taken out |
| examples here | `capacity(faction, tier)` (§2), `faction.weight`, `faction.footing`, `divergence` | `treasury`, `accrual.entitlement`, `post.budget`, every `condition.*` |
| why the rule | a stored copy can disagree with the world; there is no correct setter | there is no other representation — a spend history is not derivable from anything else |

`treasury` was mislabelled because *"sum of what my places yield"* **looks** like an aggregate — and is
one **until something spends from it.** The precedent shipped a scale down: `accrual.entitlement` funds
the levy channel and is *spent directly* (`07 §8.3`); nobody proposed deriving it.

**So `faction.treasury` becomes a faction-owned gauge**, and it must leave `fm.derive`'s state list —
this is forced, not preferred. `00 §7.1`'s falsifier is *"no state name declared `writable: false` may
appear as a gauge id in `references/descriptor_registry.yaml`"*, and a real spendable treasury **is** a
declared gauge id there (§10.4). Leaving `fm.derive`'s row in place would trip that falsifier the day
the gauge is declared, which is the mechanism working correctly.

```
treasury : gauge, owner substrate.gauge, scale faction, floor 0, geometric decay per 01 §5.1

  +  boundary deposit  Σ over places where controller(place) == faction  of  residual(place)   # 07 §5.1
  −  boundary deposit  Σ over units held  of  upkeep(unit.unit_kind, unit.assignment)          # 12 §2
  −  act.muster.contract's price                                                               # §5.2
```

**All three terms are leaf 1 — a gauge deposit with provenance.** Nothing here is a setter, nothing is
an aggregate, and the two boundary terms are *flows*, which is the shape `07 §5.2` already describes
when it says `residual(place)` *"feeds `06`'s faction-treasury"*. What changes is only that the thing
it feeds is now a gauge with a floor rather than a number recomputed from scratch.

**Its bound is free and checkable at declaration time.** As a gauge it obeys `01 §5.1`'s geometric law,
so it is bounded at `rest + a/λ` with **no campaign run** — which incidentally closes the runaway a
plain accumulator would open (conquer more, bank more, buy more contracts, conquer more). Reading the
decay as flavour: a treasury that is not spent leaks to graft and spoilage. **A faction at the floor
cannot contract-muster** — a gate, on the board, published exact — and that is the whole of the
consequence this page designs.

⚠ **One dependency handed on rather than invented here.** What happens to a unit whose upkeep the
treasury cannot pay is a **`12`** question (its `unit_kind`/`assignment` form transitions are `12`'s,
`:498`), not a `05` one. This page states the constraint — *upkeep must have a consequence, or the
floor gate is the only thing stopping an unbounded standing army and it stops the wrong end* — and
declines to design a disbandment it does not own.

⚠ **The alternative was considered and is NOT shipped.** Pricing contract muster in the post's
`budget` gauge with a recurring `Debt` tag is a valid fallback if the stock route is rejected. It is
**not shipped alongside** this one: two mechanisms for one economy is the shape-divergence defect the
suite exists to stop, and §2.4 already forbids `post.budget` from buying anything but attempts.

### 5.3 `act.inquire` — information **gates**, it never adds dice

Information determining *which arguments you may attempt* is a mechanic worth having; its hard form —
the wrong choice flatly fails — is a special case bolted into a continuous system, which is scripting
drift. The soft form is already a built primitive. `act.inquire` deposits into an information gauge on
the target, and that gauge's band does exactly two things:

1. **It gates the option set.** Rows declaring `requires_information: <band>` are unavailable below it —
   a gate, on the board, published.
2. **Acting against an uninvestigated target declares a `BandExtension` that vetoes Overwhelming**
   (`dice_engine.py:95`, ED-SC-0032). Your ceiling drops; your odds of Success are untouched.

Neither adds a die, shifts an obstacle, or touches the Partial or Failure boundaries. An extension's
only power is to veto the top band — the return channel is structurally bounded to `3 → 2` — and the
seam refuses undeclared context keys rather than swallowing them.
### 5.4 `act.charter` — where a schism finishes, and the hole it closes

**The hole, stated first because it was load-bearing and this page was where it died.** `06 §3.5` hands
the chartering act here in as many words — *"the chartering act itself is `05`'s, not this page's —
creating an entity is generation"* (`06:346-350`) — and this document shipped eight action families,
**none of them a charter.** So a bloc reaches `in-schism`, its project *"becomes a founding claim"*,
and the claim had **no executor anywhere in the three documents that share the seam.** Change C's
marquee possibility — a faction emerging from inside an institution, with no faction-emergence
subsystem — terminated in a dangling sentence.

**Why it could not simply fall out of the existing machinery.** `09 §6.2` binds a project fire to
`01 §2.1`'s four write leaves and **entity creation is not one of them**. `07` dodges this at place
scale by pre-declaring `kind: Ruin` placeholder nodes, so a founding is a *form transition* on an
entity that already exists (`07 §3.5`). **Factions have no placeholder equivalent** — a pre-declared
roster of empty faction shells would be authored content standing in for emergence, which is the
scripting `00 §6` principle 2 forbids. The founding must therefore *create*, and creation is
**generation**, which `00 §4.1`'s P-1 already licenses (*"created at load or by generation"*) and which
this page **already does once**: `act.muster` produces a `unit` entity, and `12 §2.1` says so —
*"Muster (`05 §6`) still produces the entity."* `act.charter` is the same act on a different kind.

```yaml
- action: act.charter
  remit_kinds: [head, minister, governor, commander, envoy]   # any seated office; the GATE narrows
  tiers:  [settlement, territory, peninsula]                  # a wing founds where it stands
  binds:  {}
  target: null                                                # a gate does not roll
  cost:   {budget: 1, gauge_deposits: []}
  gate:
    - a Tag {kind: Precedent, key: founding_claim, owner: <the bloc>} exists      # 09 am.fire's leaf 2
    - bloc.state == in-schism                                                     # 06 §3.4, terminal
    - the invoking post is held by a member of that bloc                          # 06 §3.2's members[]
  generates:
    entity_kind: faction
    identity:
      ethos:          practice(bloc.members) FROZEN at the schism season          # 06 §3.5 supplies it
      seat_node:      the tier node of the invoking post                          # 01 §1.1, immutable
      charter_season: this season
    form:
      posture:        the parent faction's posture at the schism season           # 01 §1.1, one enum
  effects:            # a gate has no four-band table; these are its unconditional writes
    - post_revoke / post_grant: each bloc member's post transfers principal to the new faction  # leaf 3
    - tag: a Precedent on the parent faction recording the schism                              # leaf 2
    - gauge: treasury opens at floor                                                            # §5.2a
```

**The gate reads a Tag, exactly as `07`'s `place_found` does, and for the same reason.** `07 §3.5` is
*"verb-free on purpose"* because its gate reads *state left behind*, never a message in flight (J-N,
§8.1). Here the tag is the same artifact from the same producer — `09`'s `am.fire`, leaf 2 — and the
executor is a verb only because an entity must be **created** rather than transitioned. **The producer
set is open:** `bloc.state == in-schism` is the only currently-declared way to deposit
`founding_claim` on a bloc, and a second project kind depositing it (the bottom-up founding canon
prices at `settlement_layer_v30.md:1046`) would need **zero lines here**. That is what keeps this a row
rather than a schism special case.

**Why `gate` and not the roll canon prices (O-5.8).** Canon's Declaration is a Domain Action —
Influence pool = Renown ÷ 2, Ob 3 — because in the ratified design there was nowhere else to put the
uncertainty. Here the uncertainty is **already spent**: the bloc had to form on a connectivity gate,
hold cohesion above `θ↑` for a dwell, reach `in-schism`, and drive a project to its threshold through
`am.advance`. Rolling again at the last step would **charge twice for uncertainty already paid**, which
is verbatim `07 §9.2`'s argument for gating a growth threshold rather than re-rolling it (`00 §6`
principle 4). It also fails P-iv the other way: a failed Declaration roll on a fired project is an
irreversible loss on a routinely-reached roll, and §7 forbids exactly that.

**Canon's ED-790 starting stat sheet is superseded structurally, which is a stronger claim than
overriding it.** `settlement_layer_v30.md:1049-1063` gives a founded faction L 2 / PS 3 / Mil 1 / Sta 3
and the rest. In this suite **every one of those quantities is a derivation** — `practice`,
`divergence`, `footing`, `weight`, `force` are computed by `fm.derive` from what the faction holds, and
`acceptance.{legitimacy,support}` are *place* gauges belonging to the places. A founded faction
therefore **cannot be given** starting values for them; it computes them on its first boundary, and a
new faction is weak because it holds four posts and one node, not because a table said `Mil 1`. The
only thing lost is Renown, which this suite does not carry at all — named as a canon object
deliberately not ported, not as an oversight.

**What this refuses to add.** No `faction_dissolve` (§7's no-elimination rule stands; §1.2's vacancy
path is the recoverable alternative); no charter roll; no faction-count cap — the bound is `06 §3.2`'s
bloc-formation gate and `θ_coherence`, upstream, where it already exists.

*Emergent possibility lost if `act.charter` were cut:* **the game could not produce a new faction, at
all, ever** — the world would ship with its factions and end with them, and change C's whole argument
(an institution that can betray its purpose) would stop one step short of the thing that makes the
betrayal matter.

### 5.5 `08`'s settlement rows land here as rows (O-5.11)

**The collapse is proved by the two documents' own sentences**, not argued: *"a faction action at the
peninsula rung and a settlement verb are the same object at different rungs"* (§10.1) and *"a
governance response and a faction action remain the same object at different tiers"* (`08 §9.2`).
Field by field:

| `08` | here | delta |
|---|---|---|
| `sm.gate` — `resolver: gate`, `scales: [settlement]`, `consumes: [post.vacant]`, emits `faction.action_declined` | **`fa.gate`** — the same, with `scales: [settlement, territory, peninsula]` and `tier: null` | `fa.gate` already **iterates every declared rung** (§1). `sm.gate` is `fa.gate` with the loop unrolled to one iteration |
| `sm.act` — `resolver: d_sigma`, `remit: [governor]`, `budget: {post.budget, 1}`, eight rows | **`fa.resolve`** — `resolver: d_sigma`, `remit: [head, governor, minister, envoy, commander]`, `budget: {post.budget, 1}`, rows | `governor` was already in `fa.resolve`'s remit. The eight rows gain `tiers: [settlement]`, `remit_kinds: [governor]` and are `act.govern` rows |

**What is NOT absorbed, and why the line is there.** `sm.respond` survives in `08` untouched. A
directive arrives *addressed to a holder*, who answers it — the option set is a function of what was
asked, not of what the holder's remit contains. That is a different object from "pick the highest-value
thing your remit allows", and collapsing it would delete the one governance decision `08` leaves the
player. `sm.business` and `sm.directive` are likewise untouched.

**What this costs this page, stated rather than absorbed silently.** `fa.resolve` must now declare
`form:` and `transitions:` — `sm.act` names facility-tier advance rows (`08 §8`), and per W-5
(`01 part 2 §9.2`) a module may **name** a transition the herald applies. So §9's note that *"no module
here declares `form:` or `transitions:`"* is **no longer true** and is corrected there rather than left
standing. That is the honest price: one field, on one module, for eight rows and two modules deleted.

**Zero outcomes lost, zero surface verbs added, zero new machinery.** `08` keeps its single
playing-surface slot for `sm.respond`; this page keeps its single slot for *direct a post's action*.

---

## 6. Resolution — one pool shape, one obstacle owner

Every action here that rolls, rolls the same way.

| element | rule |
|---|---|
| **actor** | the post-holder invoking the module — **never "the faction"** |
| **pool** | `attr[a] + attr[b] + POOL_BASE`, `[a, b]` the row's declared attribute pair, keyed on `descriptors.ATTRIBUTES` |
| **obstacle** | `derive_ob(target_score, target_modifiers)` — E-1 and nowhere else. **In the DO shape, the differential is the `net` and the entrenchment is the `ob`** (§4.1) |
| **modifiers** | σ-space μ-shifts via `sigma_leverage.net_boost`; never extra dice. **One exception, argued and listed at O-5.7:** a *contested* quantity's obstacle derives from the lead, inside `derive_ob` (§4.1) |
| **degree** | `degree_from_net`, unmodified, with an extension only where §5.3 declares one |
| **TN** | never named. `_require_tn7` raises (`dice_engine.py:182`) |

**The pool arithmetic, because P-v turns on it.** Attributes are 1–7, so `attr[a] + attr[b]` spans 2–14
and the pool spans `2 + POOL_BASE … 14 + POOL_BASE`. With `POOL_BASE = 4` — **a shape proposal, the one
bare number on this page, declared in the exported params with this justification attached** — the pool
spans **6–18**, inside the band the continuous engine is calibrated for at both ends. Reachability bar:
*the weakest possible actor on the least-suited pair must still produce a pool inside the calibrated
band.* At `attr = 1, 1` that is pool 6 — satisfied.

**This is also why the pool is one person's score and never an aggregate over a roster.** A
roster-sized pool grows `μ` linearly in roster size while `σ` grows only as `√size`, so `z` grows
without ceiling and the roll becomes decorative for a large faction — and it would put the same action
on two different engines depending on how many people a faction has. **The roster buys actions; it
never buys dice.** That is §2.4's restriction reached from a different direction.

---

## 7. Two constraints binding on every effects table

- **Total over the four bands.** Every action declares an outcome for Overwhelming, Success, Partial and
  Failure, and **no effect is unique to Partial** (P0-3), so a change to the Partial band's width
  degrades the ladder gracefully rather than deleting a mechanic.
- **No Failure branch removes a post or eliminates a faction.** Failure deposits, writes tags and costs
  the budget point. Elimination is only ever the gate closing for want of a candidate, and that is
  recoverable by producing one (§1.2). An irreversible outcome on a routinely-reached roll is exactly
  what P-iv exists to catch, **and a faction takes one of these every season, at every rung.** The
  per-tier gate makes this *more* load-bearing than in v1, not less: there are now more of these rolls
  per season, so a single irreversible branch would fire that much sooner.

---

## 8. What this page assumes about the substrate — J-N and J-O, stated once each

### 8.1 ⚠ J-N — the substrate supplies NO cross-season latency

Verified against the tree by `audit/2026-08-08-world-churn-audit` and reproduced at `01 part 2 §9.3`:
`drain_tick` has zero production callers, `next_tick` **raises `TerminationBreach`** on a non-empty
queue, and `DEFAULT_CASCADE_DEPTH_MAX = 0` is a self-labelled provisional bound. **The guard prevents
cascades outright; it does not schedule them late.** One-hop-per-season latency is not a property this
design has — it is a mechanism someone would have to build.

**What that forbids on this page, concretely:**

| forbidden | the correct shape |
|---|---|
| a contest that "posts a challenge" resolving next season | it resolves **within the tick**, or not at all |
| a multi-season influence campaign carried by an emission | it advances because **presence is a certain way at the accounting boundary** — a gauge read, not a message |
| `fa.gate` reacting next season to a `post.vacant` raised this season | the gate **reads `holder_id`** at the boundary; it does not wait to be told |
| an action whose consequence "arrives later" | its deposits land now and **decay geometrically**, which is the only cross-season channel the substrate has besides reading state |

**J-N is the ruling that would change this.** If it rules for reactive chains, this section is what to
revisit; nothing else on this page depends on the answer.

### 8.2 ⚠ J-O — what here leans on Key *consumption*

`00 §5.1` files J-O: whether the Key substrate deserves promotion from telemetry spine to churn engine
at all, the alternative being an append-only telemetry/causality log with churn driven at the boundary
directly. **Stated so the affected parts stay identifiable if J-O rules the other way:**

| depends on Key **consumption** | survives a "telemetry only" ruling? |
|---|---|
| `fa.gate`'s `consumes: [post.vacant]` | **no** — it becomes a boundary read of `holder_id`, which is what §8.1 says it already is in substance. **One line of contract, no design change** |
| everything else on this page — `appeal` (reads state), the budget (reads a gauge), `act.contest_influence` (reads presence, rolls, deposits), every effects table | **yes** |
| the emission side (`faction.action_declined`, and the action rows' own emissions through the herald) | **yes** as a log |

**This page is nearly robust to J-O**, and deliberately so: the per-tier gate was written as a *state
read* rather than a *Key reaction* precisely because §8.1 says the transport for the latter does not
exist. That is one constraint doing two jobs.

---

## 9. Module contracts

Shape per `00 §7`. Per W-6, every `consumes:` row names what the consumer does with the Key; none is
declared speculatively.

```yaml
- module: fa.gate
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]     # v2: no longer [peninsula] — O-5.1
  tier: null                                     # runs at EVERY declared rung; §1.1
  resolver: gate
  remit: []                                      # not invocable; the boundary runs it
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]   # rule content: re-evaluates the rung's
                                                        # acting_posts set. See §8.2 — this is the
                                                        # ONE J-O-fragile row on the page.
  emits: [{type: faction.action_declined, terminal: true}]   # carries faction, tier, reason
                                                        # O-5.11: 08's `sm.gate` is THIS module with
                                                        # the rung loop unrolled to one iteration.
  state: []
  form: []
  transitions: []
  disclosure: [{of: decline_reason, inputs: published, presentation: exact, trigger: hidden}]

- module: fa.select
  parent: faction_actions
  class: substrate                               # the RANKING is substrate; the player's pick is 10's
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: derivation                           # `appeal` is a read-only ranking and WRITES NOTHING,
                                                 # which is the rule 00 §7 states. But the CHOICE over
                                                 # it draws (O-5.9), and the four resolver kinds have
                                                 # no name for that -- see the schema-gap note below.
  draw:                                          # NOT YET A SCHEMA FIELD. Declared, not hidden.
    over: appeal
    law: softmax
    constant: APPEAL_TEMPERATURE                 # part 1 §3.5, with its two-sided reachability bar
    substream: H(campaign_seed || accounting_index || post_id)    # 10 §6.4(3); NOT a shared stream
  remit: [head, governor, minister, commander, envoy]
  budget: null
  consumes: []
  emits: []
  state: []                                      # nothing written -> `derivation` stays correct
  form: []
  transitions: []
  disclosure:
    - {of: appeal,              inputs: published, presentation: band,  trigger: hidden}
    - {of: APPEAL_TEMPERATURE,  inputs: published, presentation: exact, trigger: hidden}
                                                 # the constant is published; the DRAW is not (§3.5)

- module: fa.resolve
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, governor, minister, envoy, commander]   # `governor` was ALREADY here, which is what
                                                        # made O-5.11's absorption a no-op: 08's
                                                        # `sm.act` is this module at one rung. §5.5
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  ob_sites: []            # DELIBERATELY EMPTY. fa.resolve is a dispatcher: the obstacle's target is
                          # the RESOLVED ROW's `target`, so each action row carries its own `ob_site`
                          # (§5) and 01 §6's gate evaluates rows, not this module. Declaring a site
                          # here would name a target this module does not have.
  emits: []                                      # the herald emits per the resolved row (W-1)
  state:
    - {name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,   bucket: tag,   writable: true, owner: substrate.ledger}
  form:                                          # NEW (v3), O-5.11 -- the price of absorbing sm.act
    - {entity_kind: place, field: facilities}    #   NAMED only; the herald applies it (W-5)
  transitions: [<facility-tier advance rows -- owned by 07's form_registry; NAMED, never mutated>]
  disclosure:
    - {of: pool,     inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle, inputs: published, presentation: exact, trigger: hidden}

- module: fa.contest_influence                   # NEW (v2)
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma                              # DO; the UNDEFENDED path is a gate, §4.2
  remit: [head, governor, minister, envoy]
  budget: {gauge: post.budget, cost: 1}
  consumes: []                                   # reads presence at the boundary; §8.1
  ob_sites:                                      # 01 §6's reachability gate, in 00 §7's EXACT field
    - target: presence.<institution>             # names (CORRECTED v3 -- this page's earlier three-
      shape: DO                                  # field form was its own invention and omitted the
      pool_min: 6                                # two fields 00 §7 declares MANDATORY for DO/BI).
      pool_max: 18                               #   §6: attr 1-7 twice + POOL_BASE 4. Site-local;
      pool_opposed_min: 6                        #   there is no POOL_MAX in `engine/`.
      pool_opposed_max: 18                       #   Without these two a DO site is UNEVALUABLE (01:621)
      ob_modifier_max: 2                         #   positive `place_terms` only
      ob_modifier_min: -(presence_ceiling)/2      #   the challenger's lead term, strictly non-positive
                                                 #   (O-5.7). ⚠ SYMBOLIC: it is the SECOND field on
                                                 #   this site blocked on 07's undeclared ceiling.
                                                 # ⚠ the gate must use the DIFFERENTIAL's moments,
                                                 #   mu=0.4(Nc-Nd), sigma=0.8*sqrt(Nc+Nd) -- STRICTER
                                                 #   than one-sided (Ob<=8.247 vs 9.783). §4.1a
  emits: []                                      # the herald emits; a band crossing is 07's
                                                 # form.transitioned, not a second emission here
  state:
    - {name: presence.<institution>, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: exposure,               bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,                    bucket: tag,   writable: true, owner: substrate.ledger}
  form: []                                       # 07 owns place.presences transitions, NOT this module
  transitions: []
  disclosure:
    - {of: presence.<institution>, inputs: published, presentation: band,  trigger: hidden}
    - {of: pool,                   inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle,               inputs: published, presentation: exact, trigger: hidden}

- module: fa.muster
  parent: faction_actions
  class: substrate
  scales: [settlement, territory]
  tier: settlement
  resolver: gate                                 # affordability is a threshold, not a contest
  remit: [head, governor, commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: accrual.entitlement, bucket: gauge, writable: true, owner: substrate.gauge}   # levy
    - {name: faction.treasury,    bucket: gauge, writable: true, owner: substrate.gauge}   # contract
                                          # NEW (v3), O-5.10. This row is the whole of the fix: the
                                          # gauge is WRITABLE and owned by substrate.gauge, so it
                                          # leaves fm.derive's `writable: false` list (06 part 2 §9).
    - {name: acceptance.support,  bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure:
    - {of: accrual.entitlement, inputs: published, presentation: exact, trigger: hidden}
    - {of: faction.treasury,    inputs: published, presentation: exact, trigger: hidden}
                                          # exact, not band: it is a decision input this season, the
                                          # same reasoning post.budget gets (01 part 2 §12)
    - {of: acceptance.support,  inputs: published, presentation: band,  trigger: hidden}

- module: fa.inquire
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, governor, minister, envoy, clerk]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  ob_sites: []            # DELIBERATELY EMPTY, and NOT because there is no site. fa.inquire rolls
                          # against "the concealing party's relevant score, WHERE ONE EXISTS" (§5.3)
                          # -- the target is row-declared and, for some rows, absent. Each row that
                          # declares a target declares its own `ob_site`; a row with no target does
                          # not roll. Naming a single target here would fabricate one.
  emits: []
  state:
    - {name: information, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: exposure,    bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure: [{of: information, inputs: published, presentation: band, trigger: hidden}]

- module: fa.charter                             # NEW (v3) — §5.4; closes 06 §3.5's dangling seam
  parent: faction_actions
  class: substrate                               # a schism finishing is never a screen
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: gate                                 # O-5.8: the uncertainty was spent in 09's am.advance
  remit: [head, minister, governor, commander, envoy]   # any seated office; the GATE narrows, not the
                                                 # remit — a schism can be led from any chair
  budget: {gauge: post.budget, cost: 1}
  consumes: []                                   # reads the founding_claim TAG at the boundary, never
                                                 # a Key in flight (§8.1). Survives J-O unchanged.
  ob_sites: []                                   # a gate does not roll; nothing to evaluate
  emits: [{type: entity.created, terminal: false}]     # ⚠ P0-1: `entity.created` is a Key type this
                                                 # suite does not yet register. Named as a dependency,
                                                 # not assumed. `act.muster` needs the SAME type for
                                                 # the unit it produces (12 §2.1), so this is one
                                                 # registration for two callers, not a new cost.
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}   # members' posts re-principal
    - {name: tag,  bucket: tag,  writable: true, owner: substrate.ledger} # Precedent on the parent
    - {name: faction.treasury, bucket: gauge, writable: true, owner: substrate.gauge}  # opens at floor
  form: []                                       # it CREATES an entity; it transitions none
  transitions: []
  generates: [{entity_kind: faction, identity: [ethos, seat_node, charter_season], form: [posture]}]
                                                 # ⚠ NOT YET A SCHEMA FIELD either — creation is
                                                 # generation (00 §4.1 P-1), not a fifth write leaf,
                                                 # and the contract schema has no way to say so.
                                                 # Reported to 00 §7's owner with fa.select's `draw:`.
  disclosure:
    - {of: founding_claim, inputs: published, presentation: exact, trigger: hidden}
    - {of: ethos,          inputs: published, presentation: exact, trigger: hidden}   # 01 §1.1: identity
```

**⚠ CORRECTED (v3). The claim that stood here — *"no module here declares `form:` or `transitions:`"* —
is no longer true, and the honest correction is worth more than the tidy sentence.** Absorbing `08`'s
`sm.act` (O-5.11) brings its facility-tier advance rows with it, so `fa.resolve` now declares
`form: [{place, facilities}]` and a named `transitions:` list. **What is still true is the property
that sentence was protecting:** per W-5 (`01 part 2 §9.2`) a module **names** a transition and the
herald applies it, and a module may only name a row it declares — so `01 §2.4`'s "grep over one field"
holds exactly as before, over one more field. Everything else is unchanged: presence band crossings are
`07`'s rows, posture is `06`'s, appointment is `04`'s, and `fa.charter` **creates** an entity without
transitioning one. A faction action deposits, tags, spends, names — and, in exactly one row, generates.

---

## 10. Property audit

**Scope, honestly.** `fa.gate`, `fa.muster` and `fa.charter` are **gates**; `fa.select` is a
**derivation with a declared draw** (O-5.9) — it ranks, it does not roll. `00 §10` and the methodology's
own rule forbid manufacturing a NERS verdict for a module that does not roll, so **no N/R/S/E verdict is
offered for those four** — their loops and gates are §10.2 instead. The audit below is of `fa.resolve`,
`fa.contest_influence` and `fa.inquire`, which roll.

### 10.1 The properties, each with the falsifier that would show it wrong

| property | verdict | falsifier |
|---|---|---|
| **P-i** legible odds | **pass, and still the strongest in the suite.** Pool is a named person's two named attributes plus a declared constant; obstacle is the target's score halved; **the DO differential is two published nets minus a published obstacle.** **Selection is WEAKENED by O-5.9 and the weakening is its honest price**: a draw over a published ranking at a published temperature, so a player reads the *distribution* and cannot predict the *pick*. Strictly less legible than the argmax draft; strictly more than the ratified engine's unpublished weight vector (`faction_action.py:234-243`), which is the real comparison | A test asserting every rolling module's `disclosure:` publishes `pool` and `obstacle` at `exact`, that `fa.select` publishes every `appeal` term, **and that `APPEAL_TEMPERATURE` is published `exact` while the draw's outcome is not published before the fact**. If any input to a roll, a ranking **or a draw's weight vector** is unpublished, P-i is false |
| **P-ii** uniform leverage | pass, **with one recorded non-uniformity in the correct direction** (§4.1) | A test asserting no module contract declares a `budget:` whose cost is consumed inside a pool or obstacle expression (`01 §5.3`'s falsifier, applied here), **plus**: no action row's modifier reaches the roll except through `sigma_leverage.net_boost` **or** `derive_ob`'s declared instance term, and no row declares both for the same quantity. A modifier applied twice through two channels — the defect the two-channel draft of §4.1 would have shipped — falsifies it |
| **P-iii** bounded, monotonic | pass, **with two loops stated and both gains unmeasured** (§2.3, §4.4) | `01 §5.1`'s declaration-time check — `rest + max_seasonal_accrual/λ ≤ ceiling` — applied to `presence.<institution>` with `act.contest_influence` counted among its depositors. **A controlled campaign pair on `tools/balance_oracle.py` showing presence share diverging without bound falsifies it** |
| **P-iv** graded, recoverable | pass | A test asserting every action row's `effects` map is **total over the four `Degree` members** and that **no `failure` branch revokes a post or removes a faction**. A row with a Partial-only effect, or an empty Failure branch, falsifies it |
| **P-vi** *(new)* **reachable bands** | ⚠ **UNVERIFIABLE for `act.contest_influence`; declared for the rest** | `01 §6`'s obstacle-reachability gate: `derive_ob(S_max, M_max) + 3 ≤ 0.4·N_max + z·0.8·√N_max`, `z = 1.645`, **per site**, evaluated for a DO site on the differential's moments (§4.1a). **The site's declaration was itself wrong until v3** — it carried three fields of this page's own invention (`target`/`modifier_max`/`pool_max`) where `00 §7` and `01:621` require seven, and **an opposed site missing `pool_opposed_*` is unevaluable rather than passing**, so the row was mis-declaring the very failure class it reports. Corrected at §9. The test that would show this site wrong: **assert the top band is reachable at the site's most favourable configuration** — at `N_c = 18` against `N_d = 6` the envelope is `11.247`, so `derive_ob(presence_ceiling, 2) ≤ 8.247`, which requires `presence.<institution>`'s ceiling `≤ 12`. **It cannot be run today**: that ceiling is `07`'s and is undeclared, and an undeclared ceiling is not a passing one. The worked failure the gate exists to catch is real and in this tree — a 0–100 gauge yields `P(Overwhelming) = 0` |
| **P-v** right engine | pass, **with one declared gap in `00 §7`'s taxonomy rather than a mislabel** | Affordability, eligibility and **chartering** are `gates` (§5.4 argues why a charter must not re-roll uncertainty already spent); contested outcomes are `d_sigma` at pools 6–18; `appeal` is a `derivation` that writes nothing. **The fourth question — *which of several good options does this person take?* — is a choice under declared uncertainty, and `00 §7` has no resolver kind for it.** `fa.select` keeps `derivation` (correct on the rule as written) and declares its `draw:` explicitly; the gap is reported, not papered over. **A test asserting every `resolver:` matches `00 §7`'s table**, that nothing determinate rolls, and that **every module declaring a `draw:` also declares a substream** — a draw on a shared sequential stream falsifies it, and `10 part 2 §10` row 4 is the executable form |

**N** — under ED-IN-0201 this is the layer the ruling is *about*; it is not optional. No roll here is
redundant: every `d_sigma` module resolves something genuinely uncertain and everything determinate is a
`gate`. **R** — the extremes are the weakest possible actor (pool 6, inside the calibrated band) and the
largest possible faction (flat ceiling; pool unchanged, because pools are person-scale at every rung).
**S** — the same pool shape, the same obstacle owner and the same four primitives as `04` and `08`; **a
faction action at the peninsula rung and a settlement verb are the same object at different rungs**, which
per-tier makes literally true rather than merely analogous — **and O-5.11 cashes that sentence in rather
than admiring it**: `08`'s two modules are deleted and its eight rows run here (§5.5). **E** — eight
families, one contract shape, **no per-faction branch anywhere**, five would-be verbs collapsed into one
binding slot (§4.5), two modules and one duplicate motion design (O-5.12) removed from the suite.

### 10.2 The non-rolling modules — loops, gates, and what each reads

| module | kind | reads | bound |
|---|---|---|---|
| `fa.gate` | gate | `post.holder_id`, `post.remit`, the declared rungs | none needed; it is a predicate. **Recoverable by construction** (§1.2) |
| `fa.select` | derivation | `faction.identity.ethos`, holder convictions, world signals, `Leverage` tags | `custody_bias` clamped to `±RELATION_SHARE_MAX · structural_range`; no other term is unbounded because each is a bounded projection |
| `fa.muster` | gate | `accrual.entitlement`, `faction.treasury` (a **stock**, O-5.10), `acceptance.support` band | the entitlement accrual rate is a property of the place; the treasury is a decaying gauge bounded at `rest + a/λ` and floored at 0; the revolt gate is a hard floor |
| `fa.charter` | gate | the `founding_claim` Tag, `bloc.state`, the invoking post's membership | **the bound is upstream and already exists** — `06 §3.2`'s formation gate and `θ_coherence`. A charter adds no loop of its own; if it did, it would be the one term on this page with no external damper |
| the budget | derivation over gauges | `post.budget` per held post | `FACTION_ACTION_CEILING`, flat and non-scaling (§2.2), **with a stated reachability bar** |

### 10.3 The four claims across both parts that are weakest, named rather than buried

1. **`FACTION_ACTION_CEILING`, `POOL_BASE`, `SHORTLIST_K`, `APPEAL_TEMPERATURE`, `d₁…d₃` and `e₁…e₂` are
   shape proposals, not ledger constants.** None is cited to a `PP-NNN` or an `ED-NNN`, because none has
   one. They are declared with justifications and reachability bars so that tuning them is an act with a
   named target, not a preference.
2. **Both loops' per-cycle gains are unmeasured** (§2.3, §4.4) and are stated as unmeasured. They are
   campaign-reachable, so the instrument exists; running it with a control is work this page does not do.
3. **The DO-plus-lead-obstacle shape is the page's most contestable design call** (§4.1). It is argued,
   listed at O-5.4 and O-5.7, and each half is *reversible in one line*: dropping `net_d` from the
   differential returns the SO the delta spec named, and dropping the negative instance term returns the
   absolute-presence obstacle — with every other part of the action unchanged either way.
4. **`act.contest_influence` depends on a gauge ceiling that does not exist yet, and the dependency is
   now exact rather than general.** `01 §6`'s gate is built; this site declares `pool_max: 18` and
   `modifier_max: 2`; the third field, `presence.<institution>`'s ceiling, is `07`'s and is undeclared.
   The constraint handed to `07` is **`ceiling ≤ 12`** (§4.1a). Until it lands the site's status is
   **unverifiable, not passing** — picking a ceiling here to turn the row green would be exactly the
   confounded measurement `CLAUDE.md §0.1` was written about. **This page's own first form of that gate
   was wrong** (2.57× too permissive at pool 5), **and its own declaration of the site was wrong twice
   over** (three fields where seven are required, §9) — which is the strongest argument available that
   the check belongs at one owner and not restated per document.
5. **`act.charter` creates an entity, and creation has no home in the contract schema** (§5.4). It is
   licensed by `00 §4.1`'s P-1 (*"created at load or by generation"*) and precedented on this same page
   by `act.muster` producing a `unit` (`12 §2.1`), so the *design* is not novel — but `00 §7`'s `state:`
   buckets are `entity|gauge|tag|post` with no way to say *"and one of these comes into being"*, and
   `entity.created` is **not a registered Key type**, so **P0-1 blocks the emission.** One registration
   serves two callers. Declared as a dependency rather than assumed away.
6. **`APPEAL_TEMPERATURE` is the one shape proposal here with no reachability evidence at all.** The
   others have arithmetic behind their bars; this one has a two-sided bar (part 1 §3.5) and **no
   measurement**. It is campaign-reachable, so `tools/balance_oracle.py` with a control is the
   instrument. A `T` picked to look reasonable and never measured is precisely the decorative-threshold
   failure §2.2 refuses for the ceiling, and refusing it there while accepting it here would be
   asymmetric skepticism rather than a standard.

### 10.4 Dependencies this page declares and does not own

Named here so none is lost at a document boundary — the posture §4.1a already takes with `07`'s ceiling.

| owed by | what | why it blocks something here |
|---|---|---|
| `01 §2.1` | the **aggregate-vs-stock** sentence | O-5.10 and §5.2a cite it. Without it the mislabel that produced `writable: false` on a spent treasury recurs — and it has already recurred once |
| `01 §5.2` | declare **`treasury`** (faction, stock) and **`information`** (target, **0–5**) in the gauge roster | **neither is in the roster today**, and `fa.muster` and `fa.inquire` each write one. An undeclared gauge silently escapes `01 §5.1`'s declaration-time bound check, which is the only bound `information` has |
| `06 part 2 §9` | drop `faction.treasury` from `fm.derive`'s `state:` list | it is `writable: false` there and writable here. **Two owners for one gauge is worse than the original defect**, so this must land in the same merge as O-5.10 |
| `07` | `presence.<institution>`'s **ceiling ≤ 12** | §4.1a. It now blocks **two** fields of the same `ob_sites` row — `target`'s divisor and `ob_modifier_min` |
| `12` | the consequence of **unpaid upkeep** on a unit | §5.2a. Without it the treasury floor is the only brake on a standing army, and it brakes the wrong end |
| `00 §7` | a schema home for **`draw:`** and for **generation** | §9 declares both in fields the schema does not have. Reported together because they are one gap: the contract describes what a module *reads and writes*, never what it *chooses* or *brings into being* |

**And one thing this page was asked to add and REFUSES to add.** `12:544` bills *"whether to order a
unit field ↔ garrison"* to *"one of the existing strategic action-family invocations (`05`)"*. **No such
family exists here, and none should be added.** `12`'s own `ad.unit` contract (`:486-499`) already
declares `remit: [commander]`, `budget: {gauge: post.budget, cost: 1}`, `form: [{unit, assignment}]` and
`transitions: [unit.field_to_garrison, unit.garrison_to_field]` — **the executor already exists in `12`;
what is wrong is the sentence pointing away from it.** Minting an `act.*` family to satisfy a
cross-reference would create a second invoker of one transition pair, which is the shape-divergence
defect, to fix a typo. **The one-line correction belongs in `12:544`**, and meanwhile nothing is
blocked: `fa.gate` counts `ad.unit` in `action_modules` (part 1 §1), so a commander-only faction acts.
