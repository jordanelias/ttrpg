# 11 — World Events: conditioned exogenous pressure, bounded, reachable both ways

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## [`07_places_and_settlements.md`](07_places_and_settlements.md) ·
## [`10_the_slate_and_salience.md`](10_the_slate_and_salience.md) +
## [`10_the_slate_and_salience_part2.md`](10_the_slate_and_salience_part2.md) ·
## `engine/substrate/keys.py` · `engine/cross_scale/echo_transport.py` · `engine/autoload/dice_engine.py` ·
## `engine/autoload/season_manager.py` ·
## `audit/2026-08-08-world-churn-audit/06_master_synthesis.md` ·
## `audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` (RATIFIED, ED-IN-0011) ·
## `systems/settlements/governance_play_redesign_v1.md` · `systems/settlements/settlement_layer_v30.md` ·
## `systems/overview/clock_registry_v30.md` · `references/valoria_geography_v30.yaml`

This document is change **G** (`00_INDEX.md:231`). It is new — there is no v1 predecessor to correct.
v1's root cause E, restated in the archived suite's own words: *"the world has no outside — every
input is endogenous."* This page names the outside, bounds how much of it can speak per season, and
proves both that it reaches the world and that the world can hand it back to the player.

## Overrides

**None.** This document adds a registry and two modules; it contradicts no ratified canon, no Jordan
ruling, and no prior document in this suite. Two places where an override was live to take, argued and
declined:

1. **The stochastic mechanism could have been a bespoke roller. It is not — `d_sigma` + `derive_ob`
   are reused as-is.** `01 §6` records that ruling the obstacle without giving it one owner predicted
   "the same fork recurring," backed by a measured precedent of **six private roll/degree
   implementations** before `derive_ob` existed. Building a seventh — a bespoke weighted-draw for
   world events — would re-manufacture the exact defect that ruling closed, for no gain: the margin
   ladder already produces a graded four-band outcome, which is exactly what "conditioned, with a
   stochastic component" needs. **Weighed under `00 §5.3`'s tie-break ("may the best ideas win") and
   reuse wins on its own merits, not out of deference.**
2. **Whether to invent a seventh `Entity` kind for peninsula-scale state (Mending Stability,
   Institutional Pressure, Turmoil — `systems/overview/clock_registry_v30.md:16-19`) was considered
   and declined.** `01 §1`'s own words — *"a settlement, a territory, a province and a country are the
   same object at different tiers"* — already answer this: the topmost `place` node (whatever kind the
   form registry names the peninsula-scope container) is a Place like any other, just at the top of the
   tier ladder, and its gauges are ordinary `place`-owned Gauges (`01 §5`). No new kind is needed and
   none is proposed. **This is the one thing this document needed from the primitive layer that §1
   does not say outright — flagged in the closing report as the finding it is, not smuggled in as a
   fact.**

Nothing here touches `derive_ob`'s formula, the margin ladder, TN 7, or any other ruled surface — it
is a **consumer**, not a claimant, of all three.

---

## 1. What this closes, and what it deliberately leaves alone

**The gap, named precisely.** `governance_play_redesign_v1.md:154`'s pressure homeostat already has a
term for this — `Π_next = clamp(Π + Σ(unserved Needs) + Σ(active Grudges) + Σ(NPC ambitions in motion)
+ external_shock − …, 0, 10)` — and `external_shock` has never been defined by anything on disk. Its
own Crisis family is seeded by *"High Π, stat floors, **external shock**"* (`:196`) and nothing
produces one. **This document is `external_shock`, made mechanical for the first time.**

**What it does not do:**

- **It does not redesign Dearth.** `settlement_layer_v30.md §4.3a` (ED-SE-0008) already owns the
  entitlement-failure chain — Prosperity 0, a cut grain route, or an ill-timed levy — and its own
  framing is explicit: *"Trigger (entitlement failure, not weather)"* (`:759`). This document supplies
  an **upstream cause** for two of those three inputs (a place's Prosperity dropping; a route becoming
  cut) without touching the chain's response verbs, its PS arithmetic, or its framing. A world event
  that deposits into `condition.prosperity` is one more depositor among however many `07`/`08`
  eventually declare — not a second Dearth mechanic.
- **It does not build a second surfacing path.** Part VI (held, not ratified) forbids exactly this:
  *"A second surfacing path for world clocks, bypassing the deck grammar"*
  (`audit/2026-08-08-world-churn-audit/06_master_synthesis.md:556`). `governance_play_redesign_v1.md
  §2.2` (`:164-187`) already declares a card grammar — `triggers` (state predicates, ALL must hold),
  `weight`, `cooldown`, `excludes`, `follow_on`. **§2 below adopts that exact field shape** for the
  `world_events:` registry rather than inventing a parallel one. Two catalogues (this one and whatever
  `08` ships for endogenous business), one grammar, one downstream candidate pipeline (`10`).
- **It does not touch Knot strain.** `01 §7.5`'s strain-source list is closed and canon-owned
  (`knots_v30.md:160-168`); no row here targets a Knot edge, named or implied.
- **It does not compute salience.** §5 states this at length, because it is the requirement most
  likely to be skipped by a document that has just built something worth showing off.

*Emergent possibility lost if this document were cut entirely:* the world could only ever react to the
player, never act on them — the literal wording of root cause E, and the reason v1's settlements felt
like stat blocks waiting for a governor to arrive rather than places things were already happening to.

---

## 2. The event row

A row is **not** a random draw. It is a registry entry with a **gate** (deterministic; must hold) and,
only once gated-eligible, a **roll** (the stochastic component the task names explicitly — conditioned,
not instead of chance, but never chance alone).

```yaml
event: <id>                          family: Opportunity | Crisis            # existing families only —
                                                                              # §2.3 table below, no new member
origin: exogenous                    # the ONE new field on the existing card shape (§1) — marks rows
                                      # this document seeds, distinct from NPC/directive-seeded rows
scope: place | faction                # never "world" — the top-tier place node IS world scope (Overrides §2)
triggers:                             # gate — state predicates, ALL must hold, never a roll (§2.1)
  - <predicate over identity, form, gauge band, or tag existence>
hazard_pool: <int>                    # E-1's roller — the event's own base severity, a fixed die count
resilience:
  target_score: <gauge id>            # what `derive_ob` reads — the defender's score
  modifiers: <terrain/season adjustment, a property of THIS target in THIS instance>
cooldown: <int seasons, ≥ 1>          # REQUIRED — §3.2
excludes: [<event id>, …]             # mutually exclusive this season, same shape as the card grammar
deposits:                              # leaves 1–2 ONLY — never 3 or 4 (§2.3)
  overwhelming: [...]   success: [...]   partial: [...]   failure: []   # TOTAL over all four bands (P0-3)
follow_on:                             # a Tag, never a scheduled Key (§2.4 — J-N)
  on_fire: {tag: Precedent, key: "we_cooldown:<event>:<target>", ttl: <cooldown>}
emits: world.event_fired               # blocked on P0-1 (`00 §8`), named here so the blocked work is specific
```

### 2.1 The gate — conditioned, never rolled for its own sake

**A world event's gate is exactly a form transition's gate** (`01 §2.2`): a predicate over gauges,
tags, form and identity, read at the moment of evaluation, never a roll. The gate answers *"can this
happen here, now"* — terrain (identity, immutable) and season (world state) narrow eligibility
categorically; a gauge band narrows it temporally. A drought gate that never reads terrain would fire
on a mountain fortress as readily as a floodplain, which is exactly the arbitrariness the task names as
the failure to avoid.

**Season is read, not invented.** `engine/autoload/season_manager.py:22` declares `SEASONS_PER_ARC =
4`; `:34` increments `world.season` once per call. `world.season % SEASONS_PER_ARC` is therefore a real,
already-computable quarter index — this document reads it as a growing/harvest/dormant cycle rather
than adding a field. (The mapping from index to label is this document's own shape proposal, not a
ledger constant — flagged per the anti-fabrication rule.)

### 2.2 The roll — reusing `derive_ob`, the margin ladder, and nothing new

Once gated-eligible: `roll_pool(n=hazard_pool)` against `Ob = derive_ob(target_score, modifiers)`
(`01 §6`), degree from the ratified margin ladder (`00 §5`: Overwhelming ≥ 3, Success ≥ 1, Partial [0,1),
Failure < 0). **The metaphor is exact, not decorative:** the hazard's fixed severity pool contests the
place's own condition — a place with strong `condition.prosperity` presents a higher `target_score`,
therefore a higher Ob, therefore a harder margin for the hazard to clear. A well-run place weathers a
bad season better than a neglected one, for free, out of arithmetic already in the corpus.

**Total over all four bands, never firing only on Partial (P0-3).** Overwhelming/Success/Partial each
carry a declared, non-empty effect (severe/moderate/minor); Failure carries none. Firing on three of
four bands, never exclusively the narrow one, is what P0-3 actually forbids excluding.

**No actor, so `remit` does not gate this.** ED-IN-0201's "no leader, no action" clause (`00 §5`) binds
modules a **post-holder** invokes. A world event has no holder — weather does not sit a post — so the
C1 gate is inapplicable by construction, not overridden. `we.fire`'s `remit: []` records this the same
way `substrate.form` does (`01 part2 §12`): herald-applied, never post-invoked.

### 2.3 What a world event's effects may do, and may not

| may | may not |
|---|---|
| `gauge_deposit` on a **place** or **faction**-owned gauge, with provenance = the fired Key | fire a form transition directly — it deposits into the gauge an EXISTING transition's gate reads, and that transition fires on its own, at its own Accounting, through its own declared module (`01 §2.4`) |
| `tag_append` (Precedent/Grudge/Debt/Reputation), provenance required | grant or revoke a Post — officeholder lifecycle is `04`'s, not this document's; a plague depresses `condition.order` and lets `04`'s own audit/recall machinery read the consequence, it does not reach into `substrate.post` itself |
| append the cooldown tag that gates its own recurrence (§2.4) | write an aggregate of any kind (AU-1) — Mandate, an Altonian-relationship score, a faction's total standing are all off-limits as deposit targets |
| target a shared flag another document's gate already reads (§1 — the route-cut tag) | invent that flag's storage if another document already owns it; where ownership is undecided, the tag key proposed here is a **named shape proposal for `07`/`12` to confirm or rename**, not a claim of ownership |

This is `01 §2.4`'s "what a form transition may not do" table, applied one leaf down. **The scope
discipline is the same move twice**: a narrow object stays narrow by naming what it refuses, not by
trusting a reader to infer the boundary.

### 2.4 Persistence across seasons is a Tag, never a scheduled Key — naming J-N

**The substrate supplies no cross-season latency, verified against the tree independently of the
audit's claim:** `engine/substrate/keys.py:538` (`drain_tick`) has zero production callers (grepped
across `engine/` and `systems/`); `engine/substrate/keys.py:593`'s `next_tick` **raises**
`TerminationBreach` at `:599` if the queue is non-empty. There is no transport that lands an emission
in a later season. **Filed as J-N** (`00 §5.1`), and named here per that section's own instruction to
every document that would otherwise assume it.

**What this forbids:** a "three-season drought" may **not** be one event scheduling two future Keys.
**What replaces it:** a fired event appends a Tag (`follow_on.on_fire`, §2's schema) with a `ttl`. A
**continuation row** for the same hazard class declares that tag's presence as part of *its own* gate
next season — so a sustained drought is three independent seasons of the same row re-evaluating a gate
that happens to still read true, each one a fresh roll against the (now-lower) resilience score, never
a single event reaching forward in time. This is `01 §5.1`'s decay law and `01 §2.2`'s "every gate
reads current state" applied to exactly the two cross-season channels the substrate actually has
(`01 part2 §9.3`) — nothing here needs a third.

*Emergent possibility lost if the event row (gate + roll + leaf-1/2-only effects) were cut:* nothing
would ever happen to a place that nobody chose to do to it — no bad season, no lean year, no reason a
governor's competence is tested by anything but another person's move.

---

## 3. Rate bounds, proven

> *"An event class that never fires is decoration; one that fires every season is weather."* Both
> failure directions get a checkable bound, not a hope.

### 3.1 G-1 — at most one fire per target per season, structural

`we.fire` evaluates the eligible set for a season-target in a declared priority order and, once a
target has fired (any non-Failure band, any row), removes that target from further rolls **this
season**. This is a code-level exclusivity, not a probability: no target can carry two exogenous
world-event effects in the same season, whatever the individual rows' odds.

### 3.2 Per-row frequency ceiling — `cooldown ≥ 1`, checked at load

Every row's `cooldown` is required and `≥ 1` (`01 §2.3`'s `dwell ≥ 1` precedent, one leaf over). Given
G-1 and a required cooldown, a single row's maximum fire count over a campaign of `S` seasons is
`⌈S / cooldown⌉` — an arithmetic ceiling, not a claim about typical play.

> **Falsifier.** A load-time test iterating every declared `world_events` row and asserting `cooldown`
> is present and `≥ 1`. A row that omits it, or declares `0`, fails at load — the same shape as `01
> §2.3`'s hysteresis guard, because an uncooled row and a hysteresis-free gauge are the same failure:
> something that should have a floor on its own recurrence and does not.

### 3.3 The global ceiling — checked against a real existing cap, not invented

`engine/cross_scale/echo_transport.py:103` declares `DEFAULT_EMISSIONS_PER_TICK_MAX = 64` — a real,
already-existing per-tick emission cap the whole substrate shares (`keys.py:561-565` raises past it).
**This document's necessary (not sufficient) obligation:** the worst-case count of `world.event_fired`
emissions in one season — bounded by G-1 to at most one per registry-declared place-node plus one per
faction, both counts validated at load by whichever document owns the node registry (`07`'s `V-1`/`V-2`
in the v1 predecessor, `01_substrate_primitives.md:...` §1 pattern generalized) — must not by itself
exceed 64.

> **Falsifier.** A load-time test computing `place_node_count + faction_count` from the cooked form
> registry and asserting it is `≤ DEFAULT_EMISSIONS_PER_TICK_MAX`. **What this does not check, stated
> honestly:** every *other* subsystem in this suite (`08`'s business, `09`'s project firings, every
> form transition) shares the same 64-emission budget in the same tick, and reconciling every
> subsystem's declared share against one shared ceiling is cross-suite bookkeeping this document
> surfaces and does not resolve — it is `13`'s build-order to close, not a claim this page makes on
> its own behalf. **Named as an open item, not quietly assumed closed.**

**Anchor, flagged as approximate, not authoritative:** `settlement_layer_v30.md:858` counts **36
settlements**; the worst-case bound above is well inside 64 against that anchor alone, with headroom
left for faction-scoped rows and every other subsystem's simultaneous claim — which is exactly why the
honest caveat above matters: headroom is not the same as a proof the sum stays under 64 once every
subsystem's rows exist.

---

## 4. Reachability, in both directions

The task names this the requirement most likely to be fudged. Both halves get a **procedure**, run at
load, over the finite spaces the registries already declare — not an assertion that it's probably fine.

### 4.1 (a) Every row is reachable — some world state fires it

**Procedure.** For each declared row: enumerate the finite cross-product of (i) every declared `place`
`kind × terrain` pair the form registry admits (`00 §9`'s `references/form_registry.yaml`) and (ii)
every declared band on every gauge the row's `triggers:` predicate reads (`descriptor_registry.yaml`'s
per-gauge `bands` list, itself finite by declaration — `01 §5`). Evaluate the AND-predicate over that
finite space. **A row with an empty satisfying set is unreachable content and fails at load.**

This is the identical shape to `01 §2.3`'s hysteresis check and `07`(v1)'s `V-3`: a property computed
over declared, bounded registry data, with no campaign run and no sampling — because every input the
gate reads is drawn from an enumerable set by construction (terrain is a closed identity enum; bands
are a closed declared list; tags are boolean presence).

> **Falsifier.** The load-time enumeration above, run over every row in `content_registry.yaml`'s
> `world_events:` block; any row whose satisfying set is empty fails the load, named by id.

### 4.2 (b) Every row's effects are reachable BY THE PLAYER

**`07` owns what is reachable at a place** — its facilities, its presences, its investigation surfaces
(`00_INDEX.md:449`: *"presences; strata; terrain"*). This document does not know `07`'s eventual
content, and the procedure below is written so it does not need to: it is **structural**, checking the
*shape* of reachability rather than a hardcoded list of `07`'s facility names.

**Procedure.** For every state row a `world_events` row's `deposits:` names as a target:

1. its `disclosure.inputs` must be `published` (E-2, `01 §8`) — an undisclosed target is invisible by
   construction, whatever else is true of it;
2. it must be **read** by at least one *other* module contract's `gate:` predicate, `derive_ob`
   `modifiers`, or a declared form-transition's gate, where that consuming module's `remit:` is
   **non-empty** — i.e., some post-holder's option set changes in response to this exact gauge or tag.

A target passing (1) but failing (2) is visible but inert: the player can see the number move and can
do nothing that reads it — churn with no purchase, the thing root cause E's own diagnosis (a season
"presenting undifferentiated volume," `ARCHIVED.md`) already named as the failure one layer over.

> **Falsifier.** A load-time closure check over the cooked `module_contracts.json` and
> `form_registry.json`: for every `world_events` deposit target, assert (1) and search for at least one
> contract satisfying (2). A target with no such contract fails, named by row id and target. **This
> check is silent about whether `07` or `08` HAS in fact wired such a contract yet — it fails loudly if
> neither ever does**, which is the honest reading of "reachable": a property this document can require
> and cite, not one it can single-handedly guarantee before its neighbors are written.

---

## 5. Candidates, not surfacing — `10` ranks, this document does not

> ⚠ **Read `10_the_slate_and_salience.md` and the ratified Light Function
> (`narrative_engine_design_v2_churn.md §4`, ED-IN-0011) before assuming otherwise.** This section
> states the boundary once, loudly, because building a second salience score quietly is precisely the
> failure the ratifying session already refused once (`00_INDEX.md:301-303`).

**`world.event_fired` is a realized fact, not a forecast** — it carries what already happened, at the
degree the roll actually produced. The ratified Light Function's own severance rule applies directly:
*"casting is severed from forecast: slate entry and summons key on the tie-graph + REALIZED state only"*
(`narrative_engine_design_v2_churn.md:206-207`). A realized world event is exactly the kind of thing
that rule was written to admit cleanly — it needs no forecast-mass or imminence term because it is not
a prediction of anything; it already happened.

**What this document supplies on the emitted Key, and no more:**

| field | what it carries | who computes it |
|---|---|---|
| `targets[]` | every affected place/faction, with the deltas *that target* received (`01 part2 §9.2`, W-3/W-4) | `we.fire`, at emission |
| the preconditions that held | the gate's realized inputs, disclosed per E-2 | `we.fire`, verbatim from the gate evaluation |
| `causes[]` | the roll's own provenance chain | the herald, per W-1 |
| a declared **durability** | how many seasons this fact stays citable as a "meaningfulness" input — a per-row constant, a shape proposal | the registry row, not derived |

**What this document explicitly does not compute:** tie-proximity, identity-touch magnitude, forecast
mass, imminence, light-inertia carryover, scale-allocation weight, or any combination of them into a
score. Those are `10`'s selection-score terms (`narrative_engine_design_v2_churn.md:239-249`), and `10`
derives tie-proximity and identity-touch from `targets[]` against the realized state graph — which is
why this document's only obligation is to populate `targets[]` richly (§4.2's reachability closure is
what makes that population meaningful) and declare `durability`, never to rank anything itself.

If a term the ratified score needs turns out to be missing from what `world.event_fired` can supply,
that is a **ruling request** for `00`'s open-rulings table, not a license for this document to add a
field unilaterally (`00_INDEX.md §7` — extending the ratified surface is explicitly not this suite's
call).

---

## 6. Module contracts

```yaml
- module: we.eligible
  parent: world_events        class: substrate
  scales: [settlement, territory, peninsula]      tier: null
  resolver: gate               # §2.1 — the gate, never the roll
  remit: []                    # no actor; herald-driven (§2.2)
  budget: null
  consumes: []                 # reads STATE only, never a received Key — same shape as substrate.form
  emits: []                    # a pure filter; produces the eligible set for we.fire, writes nothing
  state: []
  form: []          transitions: []
  disclosure: []                # nothing is disclosed here; nothing is decided here either

- module: we.fire
  parent: world_events        class: substrate
  scales: [settlement, territory, peninsula]      tier: null
  resolver: d_sigma             # §2.2 — the graded, uncertain outcome
  remit: []                     # ED-IN-0201 does not bind an actorless module (§2.2)
  budget: null
  consumes: []
  emits: [{type: world.event_fired, terminal: false}]      # blocked on P0-1, §2
  state:
    # the specific gauge/tag targets are PER ROW, declared in content_registry.yaml — this module
    # owns none of them; it deposits through substrate.gauge / substrate.ledger like any other caller.
    - {name: "<row.resilience.target_score>", bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: "we_cooldown.<event>.<target>",  bucket: tag,   writable: true, owner: substrate.ledger}
  form: []          transitions: []       # never leaf 4 — §2.3
  disclosure:
    - {of: "we.fire.gate_inputs", inputs: published, presentation: band, trigger: hidden}   # E-2
```

Two modules, not one, for the same reason `07`(v1) split `pl.registry` from `pl.gauges` from
`pl.yield`: **a filter and a roll are different resolver kinds** (`gate` vs `d_sigma`), and folding
them into one module contract would hide which half is deterministic from a reader grepping the
contract for resolver type.

---

## 7. `references/content_registry.yaml` — the `world_events:` block

Declared here per `00_INDEX.md:399` (*"world-event rows (`11`)"* — this document's rows, not a new
file). Cooked by the same exporter pattern as every other registry in this suite, blocking `--check`
(`00 §9.1`). **Four worked rows, illustrative of the schema — not a claim about the eventual table's
size**, which is `13`-lane content-authoring work.

```yaml
world_events:
  - event: we.crop_failure
    family: Crisis                origin: exogenous     scope: place
    triggers:
      - place.terrain in {arid, plains, river_valley, upland}   # NOT coastal/urban-only kinds
      - "world.season % 4 == 2"                                  # the growing-season quarter (§2.1)
    hazard_pool: 4                                                # shape proposal
    resilience: {target_score: condition.prosperity, modifiers: terrain_penalty(place.terrain)}
    cooldown: 2
    excludes: []
    deposits:
      overwhelming: [{leaf: gauge_deposit, target: condition.prosperity, delta: -3}]
      success:      [{leaf: gauge_deposit, target: condition.prosperity, delta: -2}]
      partial:      [{leaf: gauge_deposit, target: condition.prosperity, delta: -1}]
      failure: []
    follow_on: {on_fire: {tag: Precedent, key: "we_cooldown:we.crop_failure:<place>", ttl: 2}}
    emits: world.event_fired
    # terrain is a bound SLOT, not three separate rows — arid reads as drought, river_valley/upland
    # as blight/frost in render only (10's beat-template lexicon, narrative_engine_design_v2_churn
    # :344-351's "slot fillers bound from live data" — this document names the slot, not the prose)

  - event: we.plague
    family: Crisis                origin: exogenous     scope: place
    triggers:
      - place.form.presences.get(port, 0) >= 1  OR  place.kind == Cathedral   # contact-bearing sites
      - NOT tag_present(owner=place, kind=Precedent, key="we_cooldown:we.plague:<place>")
    hazard_pool: 5
    resilience: {target_score: condition.order, modifiers: 0}
    cooldown: 3
    excludes: [we.crop_failure]           # a place does not draw both this season — G-1's global
                                           # exclusivity already forbids the double-fire; excludes:
                                           # is declared anyway for symmetry with the existing card
                                           # grammar (governance_play_redesign_v1.md:176), harmless
    deposits:
      overwhelming: [{leaf: gauge_deposit, target: condition.order, delta: -3},
                      {leaf: gauge_deposit, target: acceptance.legitimacy, delta: -1}]
      success:      [{leaf: gauge_deposit, target: condition.order, delta: -2}]
      partial:      [{leaf: gauge_deposit, target: condition.order, delta: -1}]
      failure: []
    follow_on: {on_fire: {tag: Precedent, key: "we_cooldown:we.plague:<place>", ttl: 3}}
    emits: world.event_fired

  - event: we.route_severed
    family: Crisis                origin: exogenous     scope: place        # targets a waypoint node
    triggers:
      - place.terrain in {mountain_pass, coastal}          # where weather can sever a route at all
      - place in adjacency(<any settlement's traced grain route>)     # settlement_layer_v30.md:816-826
    hazard_pool: 3
    resilience: {target_score: condition.defense, modifiers: 0}
    cooldown: 2
    excludes: []
    deposits:
      overwhelming: [{leaf: tag_append, kind: Precedent, key: "route_cut:<place>", value: severe}]
      success:      [{leaf: tag_append, kind: Precedent, key: "route_cut:<place>", value: moderate}]
      partial:      [{leaf: tag_append, kind: Precedent, key: "route_cut:<place>", value: minor}]
      failure: []
    follow_on: {on_fire: {tag: Precedent, key: "we_cooldown:we.route_severed:<place>", ttl: 2}}
    emits: world.event_fired
    # NOTE: `route_cut:<place>` is a NAMED SHAPE PROPOSAL for the flag `settlement_layer_v30.md
    # :822`'s occupation/blockade/siege cause would ALSO need to write. This document does not own
    # route-cut storage (07/12 do, per adjacency §7 of the v1 07 predecessor) — it proposes the key
    # so both an exogenous and a military cause converge on one flag, and defers the final name to
    # whichever document formalizes it.

  - event: we.altonian_pressure
    family: Opportunity            origin: exogenous     scope: faction      # not place — peninsula-scale
    triggers:
      - faction.identity.ethos has a charter/treaty edge naming an Altonian counterpart   # §2's edge kinds, 01 §7.2
      - institutional_pressure.band in {rising, high}       # the topmost place's own IP gauge (Overrides §2)
    hazard_pool: 3
    resilience: {target_score: acceptance.legitimacy, modifiers: 0}    # read on the faction's own seat
    cooldown: 4
    excludes: []
    deposits:
      overwhelming: [{leaf: gauge_deposit, target: institutional_pressure, delta: +2},
                      {leaf: tag_append, kind: Grudge, key: "altonian_demand", value: 2}]
      success:      [{leaf: gauge_deposit, target: institutional_pressure, delta: +1}]
      partial:      [{leaf: tag_append, kind: Precedent, key: "altonian_overture", value: 1}]
      failure: []
    follow_on: {on_fire: {tag: Precedent, key: "we_cooldown:we.altonian_pressure:<faction>", ttl: 4}}
    emits: world.event_fired
    # institutional_pressure is a GAUGE on the top-tier place node (Overrides §2 — no new entity
    # kind). Its deposit target is the gauge itself, never a faction-scoped aggregate — AU-1 holds.
```

**Every numeric value above — `hazard_pool`, `cooldown`, every `delta` — is a shape proposal, not a
ledger constant.** None is cited to a `PP-NNN`/`ED-NNN`; none should be read as calibrated.

---

## 8. What was considered and cut

| Considered | Verdict | Why |
|---|---|---|
| a bespoke weighted-draw / Bernoulli sampler for the stochastic component | **cut** | reuses `d_sigma`/`derive_ob`/the margin ladder instead (Overrides §1) — a seventh private roll implementation is the exact defect `01 §6` was written to end |
| a new `world` Entity kind for peninsula-scale clocks | **cut** | the topmost `place` node already is this, at a different tier (`01 §1`; Overrides §2) |
| a "Calamity aftershock" event family | **cut, not designed** | no canon source defines this term; inventing one here would be exactly the fabrication the brief forbids. If Thread-residue-driven exogenous events are wanted, they belong to whichever document formalizes Thread Exploitation Sites (`settlement_layer_v30.md §4.9`) reading `thread_sensitivity`, not to a term coined in this page |
| a rumour/latency transport so an event's effect could surface a season later | **rejected as non-existent, not as unwanted** | J-N (§2.4) — the transport is not in the tree; designing on it designs on a mechanism nobody built |
| a Knot-targeting event (a "Thread flare" strains a Knot) | **rejected** | `01 §7.5`'s strain-source list is closed and canon-owned; this document adds nothing to it |
| a new card `family` member ("Exogenous") | **rejected; `origin: exogenous` added to the existing schema instead** | `governance_play_redesign_v1.md §2.3`'s families already exist and already name causation loosely (*"Crisis: … external shock"*, `:196`); a new family for the SAME two families (Crisis, Opportunity) already admit is the under-distilled failure `00 §1` names |
| separate registry rows per terrain variant of crop failure (drought/blight/frost as three rows) | **rejected; one row, terrain as a bound slot** | three objects doing one job — `00 §1`'s corollary names exactly this shape and asks for one object with a registry of kinds instead |
| this document computing salience, importance, or a render-priority score | **rejected outright** | `10` owns it; §5 states why at length |

---

## 9. What the player actually touches

**Nothing, directly — and per `00 §2`, that is the design, not a gap.** A world event is substrate; the
*situation* it produces (a Slate item asking the governor to respond to a plague, once `10` ranks it in)
is where the player's existing verbs answer it — not a new one.

| what the player touches | how | how often |
|---|---|---|
| a fired event's **band-disclosed inputs** (E-2) — which gate held, never the threshold | on the Slate item it produced, if `10` surfaces it | whenever such an item is on screen |
| the **consequence** — a gauge moved, a tag exists — through the SAME verbs that already read those gauges (`04`'s recall, `07`'s facility spend, `08`'s directives) | no new verb; the existing option set now includes a response the situation warrants | whenever the situation arrives |

| what the player never touches |
|---|
| the registry row, its gate, its `hazard_pool`, or its cooldown |
| the roll itself, or its margin |
| choosing which event fires, or when |
| ranking a fired event against any other candidate — that is `10`'s Slate, not a player action |

**Zero standing verbs added** — the playing-surface budget this suite is held to (`00 §2.2`) is
satisfied by construction: this document's entire player-facing surface is two rows, both reads,
against nine substrate objects (two module contracts, four registry rows, one new schema field, one
Tag-based persistence convention, one shared route-cut flag proposal). If a later revision of this
document's surface table grows longer than this substrate table, it has the ratio backwards
(`00 §2.3` point 4).

---

## 10. J-O — this document leans on Key consumption for exactly one thing

Per `00 §5.1`/`01 part2 §9.4`, every document depending on Key **consumption** states so, because a
"telemetry only" ruling on J-O would rewrite it. **`we.eligible`'s gate reads STATE, never a received
Key** (`consumes: []` in both module contracts, §6) — so the *reaction* half J-O actually threatens does
not exist here at all. What this document depends on is narrower: **the emission side**
(`world.event_fired` as a log entry `targets[]`/`causes[]` can chain through) — which `01 part2 §9.4`'s
own table already marks as surviving a "telemetry only" ruling. **This document is robust to J-O**,
because it was written against the no-latency constraint from the start rather than assuming a mesh
that reacts to itself.

---

## 11. Property audit

**Scope, honestly.** `we.eligible` is a gate; `we.fire` is `d_sigma`, consuming `derive_ob` and the
margin ladder rather than producing a new resolution mechanism. Both verdicts below apply to those two
modules and to the registry rows they read; neither this section nor any other in this document offers
an N/R/S/E verdict for a gate on its own, per the methodology's own rule (`01 part2 §13`) — the roll
inside `we.fire` inherits the dice engine's own verified properties rather than re-deriving them.

Above both: `00 §0.1`'s scope limit binds this page exactly as it binds every other — a clean audit
below says the mechanism is sound, not that the game is better for having weather in it. That second
question is the one-line loss statements in §1, §2.4 and §8, and they are judgments, not checks.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded | **pass** | G-1 (§3.1) bounds concurrent fires per target to one; `cooldown ≥ 1` (§3.2) bounds per-row frequency arithmetically; §3.3's load-time check bounds worst-case volume against a real existing cap. All three are declaration-time properties, not campaign-observed ones |
| **P-v** right engine | **pass** | `we.eligible` is `gate`; `we.fire` is `d_sigma`, and its uncertainty is genuine (a place's resilience is not known in advance to clear or fail against a fixed hazard pool) — the correct engine for "conditioned, with a real chance either way," as opposed to `accrual` (no roll) or a hand-rolled deterministic table (no chance at all) |

### 11.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| gate holds → roll → gauge deposit → gate condition weakens or strengthens → next season's gate | the gauge's own fixed point `rest + a/λ` (`01 §5.1`), checked at declaration; G-1 additionally bounds concurrent contributions to one per season | **unmeasured** — campaign-reachable, so measurable with a control (a seeded run with `we.fire` disabled vs enabled), and it should be measured before this table's rows are treated as more than a shape proposal |
| fire → cooldown tag → gate blocked → tag expires → gate re-eligible | `ttl = cooldown`, a fixed, declared, finite window (§2.4) | **terminating within one cooldown window** — not a loop with unbounded recurrence, by construction of the tag's own TTL |
| Dearth-trigger convergence (this document's `condition.prosperity` deposit feeding `settlement_layer_v30.md §4.3a`'s existing Prosperity-0 clause) | bounded by `condition.prosperity`'s own gauge bound, which this document does not alter | **not this document's loop to measure** — `07`/`08` own the Dearth chain's own stability question; this page names the coupling (§1) and stops |

### 11.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| `we.eligible`'s `triggers:` | terrain (identity), season index (`world.season % 4`), gauge bands, tag presence — never a received Key | the row is not in this season's eligible set; no roll, no effect |
| `we.fire`'s cooldown check | the `we_cooldown:<event>:<target>` tag's presence and remaining `ttl` | the row is skipped for that target this season regardless of the main gate |
| §4.2's reachability closure | the cooked module contracts and form registry, at load | a `content_registry.yaml` load failure, named by row and target — not a runtime surprise |
| §3.2's cooldown-declared check | the registry, at load | a load failure for the offending row |

### 11.3 The four qualitative verdicts

**Necessary** — one registry block, two modules, one schema field (`origin:`) added to an existing
grammar rather than a new one. §8 records seven candidates refused, three of them ("Calamity
aftershock," a Knot-targeting event, a bespoke sampler) refused specifically because nothing on disk
or in canon licenses them, not because they were merely unwanted. **Robust** — the two failure
directions the task names by name (never fires / fires every season) are closed by G-1 and by
`cooldown ≥ 1`, both load-time checks; the "content that cannot be reached" failure is closed by §4.1's
enumeration; the "content the player cannot act on" failure is closed by §4.2's structural closure
check. **Smooth** — one obstacle owner, one decay law, one disclosure contract, one write rule with
four leaves, all reused, none re-derived. **Elegant** — the corollary in `00 §1` asked for "one object
with a registry of kinds" for exactly this document; §7's four rows are one row shape with a terrain
slot rather than four bespoke mechanisms, and the whole design adds zero standing verbs (§9). The
honest deduction, matching `01`'s own candor about its edge container: **the route-severed row's
shared flag (§7) is the one object in this document whose ownership is genuinely unsettled** — named
as a shape proposal for `07`/`12` rather than asserted as this document's to decide.
