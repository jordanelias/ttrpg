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
   and declined.** `07_places_and_settlements.md:44` already gives `form(place).tier` the value
   `country` at the top of its ladder (`settlement | territory | province | country`) — so the
   peninsula-scope container is a `place` like any other, just at the top rung, and its gauges are
   ordinary `place`-owned Gauges (`01 §5`). No new kind is needed and none is proposed. **Two things
   this document needed from its neighbors that neither says outright, flagged here rather than
   smuggled in as settled fact:** (i) which node counts as that top rung is `07`'s to name, not
   assumed by this document; (ii) `07 §1.1:48-49`'s own declared place-gauge list (`acceptance.*,
   condition.*, pressure, presence.<institution>, accrual.entitlement`) does not yet include a
   peninsula-wide clock like Institutional Pressure — `we.altonian_pressure` (§7) proposes
   `institutional_pressure` as a new `place`-owned Gauge on that top-tier node, using `01 §5`'s
   primitive and no new kind, but its registration is `07`'s or `12`'s to confirm, not this
   document's to claim by using it in an example row.

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

## 2. The event row — an actorless `05 §5` action row, not a second schema

**Field by field, this catalogue's row and `05 §5`'s action row are one object, not two — the same
finding `05p2:349-350` and `08:432-433` reach about their own seam, reached here independently.** A
gate over state; `d_sigma` through `derive_ob`; effects total over four bands under the same P0-3
audit; a per-row rate bound; one obstacle-site declaration each; the same `10 §2.1` candidate hand-off.
**Two real deltas, not a parallel catalogue's worth:**

1. **`remit_kinds: []`.** A `05` row is invoked by a post-holder (`05p2 §6`: *"the actor is the
   post-holder invoking the module — never 'the faction'"*); a world event has no holder at all. An
   empty remit is already a legal value in `05`'s own grammar — it is what marks a row nobody chooses
   to invoke, herald-driven instead (§2.2 below).
2. **`hazard_pool`.** `05`'s rows roll `attr[a] + attr[b] + POOL_BASE` — a named person's own two
   attributes (`05p2 §6`). A `remit_kinds: []` row has no person to draw attributes from, so it needs
   its own fixed pool size in the same slot `05` reserves for the actor's attribute pair. `hazard_pool`
   *is* that slot's value for a holderless row, not a second pool concept.

Everything else below is `05 §5`'s field, reused by name where `05` already declares it, and this
catalogue's own addition only where it answers a question a `05` row never has to ask (a card family
for the Slate's deck grammar, a per-row `cooldown` in place of the budget economy that naturally
rate-limits an actor — see §3.2 — and `excludes`, needed here because two of *this catalogue's* rows
compete for one target the way two of one *actor's* options compete through `appeal`, which a
holderless row does not have):

```yaml
event: <id>                          # = 05's `action:` field, renamed for this catalogue's readability
family: Opportunity | Crisis          # THIS CATALOGUE'S OWN — the Slate's deck grammar (§1), which a
                                      # `05` row never carries because it is chosen by a holder, not
                                      # drawn as a card; existing families only, §2.3, no new member
origin: exogenous                    # THIS CATALOGUE'S OWN — the ONE new field on the existing card
                                      # shape (§1), marking rows this document seeds
scope: place | faction                # never "world" — the top-tier place node IS world scope (Overrides §2)
remit_kinds: []                       # DELTA 1 — always empty here; §2.2 argues why this is not a
                                      # weaker gate than `05`'s C1 clause, it is the clause's own
                                      # inapplicable-by-construction case
triggers:                             # = 05's gate half — state predicates, ALL must hold, never a
                                      # roll (§2.1); `05`'s per-post gate and this catalogue's per-row
                                      # gate are the identical shape at a different iteration axis (§6)
  - <predicate over identity, form, gauge band, or tag existence>
hazard_pool: <int>                    # DELTA 2 — stands in for 05's `attr[a]+attr[b]+POOL_BASE` where
                                      # there is no actor to draw attributes from; the event's own base
                                      # severity, a fixed die count
resilience:                           # = 05's `ob_site` block, same fields, this catalogue's names
  target_score: <gauge id>            # = ob_site.target — what `derive_ob` reads, the defender's score
  modifiers: <terrain/season adjustment, a property of THIS target in THIS instance>
  M_max: <number>                     # = ob_site.ob_modifier_max — REQUIRED, 01 §6.1.1 pt.3 (§2.2)
cooldown: <int seasons, ≥ 1>          # THIS CATALOGUE'S OWN — REQUIRED, §3.2. `05`'s rows are
                                      # rate-bounded by the actor's scarce `post.budget` instead; a
                                      # holderless row has no budget to spend, so it needs an explicit
                                      # per-row bound in its place, not a weaker one
excludes: [<event id>, …]             # THIS CATALOGUE'S OWN — mutually exclusive this season; the
                                      # holderless equivalent of two of one actor's options competing
                                      # through `appeal`, which is unavailable here (§6)
durability_bp: <int>                  # the candidate contract's realized-state term — §5, 10 §2.1
identity_touch_bp: <int>              # the candidate contract's realized-state term — §5, 10 §2.1
mandatory: <bool>                     # default false — 10 §5.4's rare, enumerated bypass
deposits:                              # = 05's `effects:` field, this catalogue's name — leaves 1–2
                                      # ONLY, never 3 or 4 (§2.3)
  overwhelming: [...]   success: [...]   partial: [...]   failure: []   # TOTAL over all four bands (P0-3)
follow_on:                             # a Tag, never a scheduled Key (§2.4 — J-N)
  on_fire: {tag: Precedent, key: "we_cooldown:<event>:<target>", ttl: <cooldown>}
emits: world.event_fired               # blocked on P0-1 (`00 §8`), named here so the blocked work is specific
```

**What this is not.** Renaming `event:`/`resilience:`/`deposits:` to `05`'s `action:`/`ob_site:`/
`effects:` outright, rather than declaring them as aliases, is `05`'s call to make across both
catalogues at once — a rename this document does not perform unilaterally on a registry block `05`
does not own. What this section commits to is narrower and load-bearing regardless of that naming
call: **there is one schema**, checkable field-for-field against `05 §5` above, and **the two modules
that used to process it are retired in favour of `05`'s own** (§6).

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

**The commensurability gate (`01 §6.1`), checked per site, not assumed.** `01 §6.1.1` point 3 makes
this a standing obligation on every `derive_ob` caller: *"a module contract declaring a `derive_ob`
site must declare its modifier bound."* Verified rather than assumed, against the cooked registry:
`condition.{prosperity,order,defense}` are this suite's name for `set.{prosperity,order,defense}`
(`engine/engine_params/descriptors.json:97-111` — floor 0, ceiling 5 each, confirmed by direct read,
not carried over from `01`'s own table, which does not spell the renamed key out). At `hazard_pool =
8` (crop failure and route-severed) or `10` (plague, headroom for a declared `M_max = 1` terrain
modifier), `μ = 0.4·N`, `σ = 0.8·√N`: top-band reachability `derive_ob(5, M_max) + 3 ≤ μ + 1.645σ`
holds for both pool sizes (`6.5 ≤ 6.92` at N=8, M_max=1; `6.5 ≤ 8.16` at N=10, M_max=1); bottom-band
reachability holds trivially since `OB_MIN > μ − 1.645σ` at both sizes — **`OB_MIN` is pinned at
**1** (`engine/autoload/sigma_leverage.py:108`, `[canonical: params/core.md §Obstacle Scale]`,
enforced at `:177` and asserted by `engine/tests/test_sigma_leverage_parity.py:355-357`), not
symbolic and not merely `≥ 0`; the real constant makes this inequality stronger, not weaker. **Every `resilience.
target_score` in §7 declares its `M_max` explicitly for exactly this reason**, and `acceptance.
legitimacy` — flagged `UNVERIFIABLE` in `01 §6.2`'s own table (undeclared ceiling under that name) —
is deliberately **not used** as a target anywhere in this document; §7's Altonian-pressure row targets
`condition.order` instead, which is in the confirmed-ceiling family.

**No actor, so `remit` does not gate this.** ED-IN-0201's "no leader, no action" clause (`00 §5`) binds
modules a **post-holder** invokes. A world event has no holder — weather does not sit a post — so the
C1 gate is inapplicable by construction, not overridden. Every row's `remit_kinds: []` (§2) records
this the same way `substrate.form` does (`01 part2 §12`): herald-applied, never post-invoked — and the
same value `05`'s own grammar already accepts, not a second convention (§2 above).

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
faction, both counts validated at load by `07`'s own load-time checks (`07_places_and_settlements.md
§2.1`, carried from v1's `V-1`/`V-2`) — must not by itself exceed 64.

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

This is the identical shape to `01 §2.3`'s hysteresis check and `07`'s own `L-3`/`L-4`
(`07_places_and_settlements.md §2.1`): a property computed over declared, bounded registry data, with
no campaign run and no sampling — because every input the gate reads is drawn from an enumerable set
by construction (terrain is a closed identity enum; bands are a closed declared list; tags are boolean
presence).

> **Falsifier.** The load-time enumeration above, run over every row in `content_registry.yaml`'s
> `world_events:` block; any row whose satisfying set is empty fails the load, named by id.

### 4.2 (b) Every row's effects are reachable BY THE PLAYER

**`07` owns what is reachable at a place, and already names this document by name.**
`07_places_and_settlements.md §8.1` ("World events (`11`) — the exogenous surface") states, independently
of this page: *"a world event may only read state and deposit — never target a form field directly.
Reachable: `condition.{order,prosperity,defense}`, `pressure`, `accrual.entitlement`,
`presence.<institution>` … and Tag appends. **Not reachable directly:** `kind`, `tier`,
`facilities[]`."* **This confirms §2.3's own leaf-1/2-only restriction independently** — the two
documents converged without coordinating, which is stronger evidence than either asserting it alone.

**Procedure**, still stated generally so a later `07`/`08` content change cannot silently break it. For
every state row a `world_events` row's `deposits:` names as a target:

1. its `disclosure.inputs` must be `published` (E-2, `01 §8`) — an undisclosed target is invisible by
   construction, whatever else is true of it. `07 §8.3` already publishes `condition.*` as `band`,
   which covers three of §7's four rows (`we.crop_failure`, `we.plague`, `we.route_severed`'s tag
   target, and the `condition.prosperity` co-deposit under `we.plague`);
2. it must be **read** by at least one *other* module contract's `gate:` predicate, `derive_ob`
   `modifiers`, or a declared form-transition's gate, where that consuming module's `remit:` is
   **non-empty** — i.e., some post-holder's option set changes in response to this exact gauge or tag.
   `08`'s `sm.act` (`08_settlement_management.md:374-393`, `remit: [governor]`) already reads and
   writes `condition.order/prosperity/defense` — a **verified, existing pass** of both checks for
   those same three rows, not merely a structural possibility.

**§7's fourth row does not pass yet, and that is stated here rather than smoothed over.**
`we.altonian_pressure` deposits into `institutional_pressure` — the gauge Overrides §2 already flags
as proposed, not yet declared by `07` or `12`. It has no `disclosure:` block anywhere on disk today,
and no module contract in this suite currently reads it in a gate. **This row fails check (1) and (2)
as of this document alone** — which is honest, not a defect to paper over: §4.2's own falsifier below
would catch exactly this row, named by id, until `07`/`12` registers the gauge and something reads it.
Building the fourth row anyway is deliberate — it is the worked example that shows the peninsula-scale
case, and its failing status is the point §2 of Overrides exists to record.

A target passing (1) but failing (2) is visible but inert: the player can see the number move and can
do nothing that reads it — churn with no purchase, the thing root cause E's own diagnosis (a season
"presenting undifferentiated volume," `2026-08-28-greenfield-systems-suite/ARCHIVED.md`) already named
as the failure one layer over.

> **Falsifier.** A load-time closure check over the cooked `module_contracts.json` and
> `form_registry.json`: for every `world_events` deposit target, assert (1) and search for at least one
> contract satisfying (2). A target with no such contract fails, named by row id and target. **Verified
> by hand for three of this document's own four rows against `07`'s and `08`'s real contracts above;
> `we.altonian_pressure` is a KNOWN, NAMED failure of this exact check today**, not a hidden one — this
> falsifier, run right now, would fail on it, and would keep failing until `07`/`12` declares
> `institutional_pressure`'s disclosure and something gates on it.

---

## 5. Candidates, not surfacing — `10` ranks, this document only satisfies its contract

> ⚠ **Read `10_the_slate_and_salience.md §§0–2` before assuming otherwise.** `10` states its own
> refusal to design a second salience function at length (`10 §0`); this section states the mirror
> obligation — `11` does not design one either, and does not compute any term `10` already owns.

`10 §2.1` defines **the candidate contract every emitter satisfies**, and names `we.fire` as one of
its emitters explicitly: *"`we.fire` | `11` | conditioned exogenous events | Routes **through** the
Slate, never around it — Part VI's second surfacing path prohibition"* (`10 §2.4`). This document
conforms to that contract rather than restating it. Per field:

| candidate field (`10 §2.1`) | how `we.fire` supplies it |
|---|---|
| `emitter`, `kind` | `"we.fire"`; the fired row's `event` id (§2, §7) |
| `anchor` | the fired target's `entity_id` (a place for scope `place`; a faction for scope `faction`) |
| `scale` | `settlement` for a place-scoped fire; `peninsula` for a faction-scoped one touching a peninsula-wide clock (§7's Altonian-pressure row) |
| `subject_refs` | the anchor plus every other entity a `targets[]` delta names (§4.2's closure — populating this richly is this document's real obligation, not ranking) |
| `durability_bp` | **declared per row, a shape proposal** (§7) — how many accountings the fact stays citable. This document supplies the number; `10` decides what it does with it |
| `identity_touch_bp` | **declared per row, a shape proposal** — deliberately low for weather (nobody's convictions are implicated by a bad harvest), higher for Altonian pressure (it bears on a faction's charter relationship, `01 §7.2`) |
| `tie_proximity_bp` | **not supplied — `10` derives it** (C-3, `10 §2.1`) from `subject_refs` against the edge graph. This document supplies the graph inputs (`targets[]`), never the derived term |
| `horizon` | `{band: 0, foreclosure_in: null}` — `world.event_fired` is **realized**, not forecast, so it has no meaningful horizon; §4.2's Light Function severance (`narrative_engine_design_v2_churn.md:206-207`, cited already in `10 §4`) means this null value can only ever affect **render depth**, never whether the candidate is cast |
| `resolver_ref` | an **existing** module that already resolves the response at both fidelities — never a `we.*` module, since `we.fire` produces the fact, it does not resolve a player's reply to it. For a place-scoped fire: `sm.act` (`08_settlement_management.md:374-393` — governor-remit, `d_sigma`, spends `post.budget`, writes exactly the `condition.*`/`acceptance.*`/`accrual.entitlement` gauges this document also deposits into). For the faction-scoped fire: `fa.resolve` (`05_faction_actions_part2.md:222-243` — head/governor/minister/envoy/commander remit, `d_sigma`, same budget shape). **This document names the natural fit; confirming the exact response row is `08`'s/`05`'s content, not this document's to finalize** |
| `responses` | 3–5 ids from `resolver_ref`'s own declared option set (C-5) — this document invents none |
| `mandatory` | `false` on all four worked rows (§7). None claims the rare, enumerated bypass (`10 §5.4`); a future row could, but that is a content decision for whoever authors it, argued the same way `10`'s own mandatory set is argued |
| `witness` | `{channel: post_remit, ref: <the post whose remit includes the resolver_ref module at the anchor>}` for a place/faction with a sited post; `{channel: co_located, ref: <anchor>}` where the player is physically present. **Required, non-empty (C-2)** — a world event with no eligible witness at its anchor does not construct a candidate at all, which is a real, if rare, consequence of §4.2's own closure check finding no consuming post |
| `provenance` | the `world.event_fired` Key's id, published by the herald (W-1) before the candidate is gathered |
| `disclosure_ref` | the deposited gauge/tag's own `disclosure:` block (E-2), already required by §4.2(1) |

**What this document explicitly does not compute:** `tie_proximity_bp`, `cast_score`, `depth_score`,
forecast mass, imminence, or light-inertia carryover — all `10`'s (`10 §4`). Its only two authored
numbers on the candidate are `durability_bp` and `identity_touch_bp`, both declared per row exactly
like `hazard_pool` and `cooldown` — **shape proposals**, not ledger constants.

If a term the ratified contract needs turns out to be unsuppliable by `world.event_fired`, that is a
**ruling request** for `00`'s open-rulings table, not a license for this document to extend the
candidate schema unilaterally (`10 §2.1` — extending the contract is explicitly not this document's
call).

---

## 6. Module contracts — retired, composed on `05`'s dispatcher instead

**Zero new module contracts.** An earlier draft of this section shipped `we.eligible`/`we.fire` as a
second `gate`/`d_sigma` module pair beside `05 §9`'s `fa.gate`/`fa.resolve` — a duplicate dispatcher
for the same two resolver kinds, the exact object T3-2 names. **Both are retired.** `we.eligible` and
`we.fire` remain this document's names for *what a `remit_kinds: []` row does when `05`'s own
dispatcher runs it* — they are no longer modules this document ships, and the table below replaces the
YAML block a prior draft declared here.

| this document's name | who actually runs it |
|---|---|
| **the gate** (§2.1) | `05`'s `fa.gate` (`05p2 §9`), already rung-agnostic — *"`fa.gate` already iterates every declared rung"* (`05p2 §5.5`) — **extended to iterate by target as well as by post**, the one addition a `remit_kinds: []` row needs, since there is no post to iterate by |
| **the roll** (§2.2) | `05`'s `fa.resolve` (`05p2 §9`), **extended to source its pool from `hazard_pool` instead of `attr[a]+attr[b]+POOL_BASE`** whenever a row's `remit_kinds` is empty (§2's DELTA 2) — `derive_ob`, the margin ladder and the effects-total rule are untouched, reused exactly |
| the gate-inputs disclosure (E-2, `01 §8`) | moves to `fa.gate`'s own disclosure list for `remit_kinds: []` rows — publishing which predicate held, never the threshold, same obligation this document always carried |
| the cooldown tag, the deposit targets, the candidate hand-off | unchanged — §2.4, §5. Deposits still go through `substrate.gauge`/`substrate.ledger` like any other caller; no module here owns a gauge or tag, per row, any more than the retired contracts did |

**The one piece with real friction, named rather than smoothed over: §3.1's priority order and G-1's
exclusivity.** `05`'s existing selection step, `fa.select`, ranks an **actor's own** option set by a
softmax over `appeal` (O-5.9) — an ethos-and-holder-conditioned score a holderless row does not have.
G-1 is a different shape: not *"which of my options do I take"*, but *"of every currently
gate-eligible actorless row at this target, which fires, and the rest are excluded this season."*
That is a second, narrower selection rule, keyed by **target** rather than by post, and it cannot be
`fa.select`'s softmax reused as-is — there is no `appeal` to rank without a holder's ethos and
convictions feeding it. **It belongs beside `fa.select`, scoped to `remit_kinds: []` rows only**: for
each target, take the declared priority order among its gate-eligible rows, resolve the first through
the extended `fa.resolve`, and remove the target from this pass on any non-Failure band (§3.1). Naming
where this lives is this document's obligation under the merge — `05`'s owner should not have to
rediscover it from the schema alone.

**The result, at the accounting boundary, is still two things, not one** — matching `08`'s and `05`'s
own emitters (`10 §2.4`): (1) the deposits and Key the herald applies and publishes (W-1, W-5), and
(2) where the roll produced a non-Failure band, a **candidate** conforming to `10 §2.1`'s contract
(§5 above), gathered by `sl.candidates` (`10 part2 §10`) the same way `08`'s `sm.business` and `09`'s
`am.*` are gathered. A fired row **never** presents, ranks, or checks the scene budget (C-6) — it
returns a value and stops. **What this buys:** zero new resolver kinds, zero new modules — the four
rows of §7 are `05`-schema rows with `remit_kinds: []`, dispatched by `05`'s own gate and roll through
the one extension and the one new narrow selection rule named above.

---

## 7. `references/content_registry.yaml` — the `world_events:` block

Declared here per `00_INDEX.md:399` (*"world-event rows (`11`)"* — this document's rows, not a new
file). Cooked by the same exporter pattern as every other registry in this suite, blocking `--check`
(`00 §9.1`). **Four worked rows, illustrative of the schema — not a claim about the eventual table's
size**, which is `13`-lane content-authoring work.

**Terrain values below are the real closed eight** (`07_places_and_settlements.md:395`, verified
against `valoria_geography_v30.yaml:675`): `plains · forest · highland · mountain · mountain_pass ·
fjord_coast · coast · marsh`. No row uses an invented terrain type.

```yaml
world_events:
  - event: we.crop_failure
    family: Crisis                origin: exogenous     scope: place
    triggers:
      - place.terrain in {plains, highland}          # the arable/marginal-arable terrains (§6.1's
                                                       # descriptions: Feldmark/Kronmark plains as
                                                       # breadbasket, highland as "limited arable").
                                                       # `marsh` deliberately EXCLUDED: canon's only
                                                       # marsh polygon is Askeheim, explicitly 0
                                                       # settlements (`settlement_layer_v30.md:310`) —
                                                       # a `place` entity that is never a settlement
                                                       # owns no `condition.prosperity` gauge to deposit
                                                       # into, so admitting `marsh` here is exactly the
                                                       # dead branch §4.1's own reachability check exists
                                                       # to catch. If Askeheim gains a settlement, this
                                                       # is the line to revisit, not before
      - "world.season % 4 == 2"                                  # the growing-season quarter (§2.1)
    hazard_pool: 10                                               # shape proposal — §2.2's gate margin
    resilience: {target_score: condition.prosperity, modifiers: terrain_penalty(place.terrain), M_max: 1}
    cooldown: 2
    excludes: []
    durability_bp: 3000          # shape proposal — a season's bad harvest is citable a few accountings
    identity_touch_bp: 500       # shape proposal — low; weather does not implicate a conviction
    mandatory: false
    deposits:
      overwhelming: [{leaf: gauge_deposit, target: condition.prosperity, delta: -3}]
      success:      [{leaf: gauge_deposit, target: condition.prosperity, delta: -2}]
      partial:      [{leaf: gauge_deposit, target: condition.prosperity, delta: -1}]
      failure: []
    follow_on: {on_fire: {tag: Precedent, key: "we_cooldown:we.crop_failure:<place>", ttl: 2}}
    emits: world.event_fired
    # terrain is a bound SLOT, not three separate rows — plains reads as drought/flood, highland as
    # blight/frost in render only (10's beat-template lexicon; narrative_engine_design_v2_churn.md
    # :346-347's "slot fillers bound from live data" — this document names the slot, not the prose)

  - event: we.plague
    family: Crisis                origin: exogenous     scope: place
    triggers:
      - place.form.kind in {Port, Cathedral}   # contact-bearing KIND, not a presence
                                                # (07_places_and_settlements.md:43 — Port/Cathedral
                                                # are declared `kind` values; conflating a kind with a
                                                # `presence.<institution>` gauge was this row's first
                                                # draft error, corrected here)
      - NOT tag_present(owner=place, kind=Precedent, key="we_cooldown:we.plague:<place>")
    hazard_pool: 10
    resilience: {target_score: condition.order, modifiers: 0, M_max: 0}
    cooldown: 3
    excludes: [we.crop_failure]           # a place does not draw both this season — G-1's global
                                           # exclusivity already forbids the double-fire; excludes:
                                           # is declared anyway for symmetry with the existing card
                                           # grammar (governance_play_redesign_v1.md:176), harmless
    durability_bp: 4000
    identity_touch_bp: 500
    mandatory: false
    deposits:
      overwhelming: [{leaf: gauge_deposit, target: condition.order, delta: -3},
                      {leaf: gauge_deposit, target: condition.prosperity, delta: -1}]
      success:      [{leaf: gauge_deposit, target: condition.order, delta: -2}]
      partial:      [{leaf: gauge_deposit, target: condition.order, delta: -1}]
      failure: []
    follow_on: {on_fire: {tag: Precedent, key: "we_cooldown:we.plague:<place>", ttl: 3}}
    emits: world.event_fired

  - event: we.route_severed
    family: Crisis                origin: exogenous     scope: place        # targets the SETTLEMENT a
                                                                              # severed route serves,
                                                                              # never the terrain tile
                                                                              # the route crosses. §4's
                                                                              # own load check catches
                                                                              # exactly the prior draft's
                                                                              # error: a mountain-pass or
                                                                              # coastal waypoint is not a
                                                                              # `place` entity and owns
                                                                              # no gauge — the roster is
                                                                              # 37 settlements plus Ruin
                                                                              # placeholders, full stop
                                                                              # (`07 §1.1`)
    triggers:
      - place.kind not in {Ruin}                                 # a real, active settlement
      - place has a traced grain route whose path crosses terrain in
        {mountain_pass, fjord_coast, coast}    # settlement_layer_v30.md:816-826 — the dangerous
                                                # terrain is a fact about the ROUTE'S PATH, read off
                                                # the adjacency graph (§2), never off `place.terrain`:
                                                # the targeted settlement may itself sit on plains and
                                                # still depend on a route that crosses a pass
    hazard_pool: 8
    resilience: {target_score: condition.defense, modifiers: 0, M_max: 0}
    cooldown: 2
    excludes: []
    durability_bp: 3000
    identity_touch_bp: 500
    mandatory: false
    deposits:
      overwhelming: [{leaf: tag_append, kind: Precedent, key: "route_cut:<place>", value: severe}]
      success:      [{leaf: tag_append, kind: Precedent, key: "route_cut:<place>", value: moderate}]
      partial:      [{leaf: tag_append, kind: Precedent, key: "route_cut:<place>", value: minor}]
      failure: []
    follow_on: {on_fire: {tag: Precedent, key: "we_cooldown:we.route_severed:<place>", ttl: 2}}
    emits: world.event_fired
    # NOTE: `route_cut:<place>` is a NAMED SHAPE PROPOSAL for the flag `settlement_layer_v30.md
    # :822`'s occupation/blockade/siege cause would ALSO need to write. This document does not own
    # route-cut storage (that lives with the adjacency graph, `07_places_and_settlements.md §7` in
    # its v1 predecessor) — it proposes the key so both an exogenous and a military cause converge on
    # one flag, and defers the final name to whichever document formalizes it.

  - event: we.altonian_pressure
    family: Opportunity            origin: exogenous     scope: faction      # not place — peninsula-scale
    triggers:
      - faction has a charter or treaty edge naming an Altonian counterpart   # 01 §7.2's scope
                                                                                # extensions to PP-724
      - institutional_pressure.band in {rising, high}       # the top-tier place's own gauge —
                                                              # a NEW gauge this row proposes, flagged
                                                              # in Overrides §2, NOT yet 07's/12's own
    hazard_pool: 8
    resilience: {target_score: condition.order, modifiers: 0, M_max: 0}   # read on the faction's seat
                                                                            # place, per 01 §1.4's
                                                                            # `posts` derivation — NOT
                                                                            # acceptance.legitimacy,
                                                                            # flagged UNVERIFIABLE by
                                                                            # 01 §6.2 (§2.2 above)
    cooldown: 4
    excludes: []
    durability_bp: 6000           # a diplomatic demand outlasts a bad harvest
    identity_touch_bp: 2000       # higher — it bears on the faction's own charter relationship
    mandatory: false
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

**Every numeric value above — `hazard_pool`, `cooldown`, `durability_bp`, `identity_touch_bp`, every
`delta` — is a shape proposal, not a ledger constant.** None is cited to a `PP-NNN`/`ED-NNN`; none
should be read as calibrated. `hazard_pool` and `M_max` were sized specifically to clear §2.2's
commensurability gate against `condition.*`'s confirmed 0–5 ceiling (`descriptors.json:97-111`) — that
arithmetic is the one number-shaped claim on this page that is checked rather than merely proposed.

---

## 8. What was considered and cut

| Considered | Verdict | Why |
|---|---|---|
| a bespoke weighted-draw / Bernoulli sampler for the stochastic component | **cut** | reuses `d_sigma`/`derive_ob`/the margin ladder instead (Overrides §1) — a seventh private roll implementation is the exact defect `01 §6` was written to end |
| a new `world` Entity kind for peninsula-scale clocks | **cut** | the topmost `place` node (`tier: country`, `07_places_and_settlements.md:44`) already is this, at a different tier (Overrides §2) |
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
against eight substrate objects (**zero new module contracts** — §6 collapsed onto `05`'s, one
extension each on `fa.gate`/`fa.resolve` and one new target-keyed selection rule, four registry rows,
one new schema field, one Tag-based persistence convention, one shared route-cut flag proposal). If a
later revision of this document's surface table grows longer than this substrate table, it has the
ratio backwards
(`00 §2.3` point 4).

---

## 10. J-O — this document leans on Key consumption for exactly one thing

Per `00 §5.1`/`01 part2 §9.4`, every document depending on Key **consumption** states so, because a
"telemetry only" ruling on J-O would rewrite it. **The gate (§2.1, run by `05`'s `fa.gate`, §6) reads
STATE, never a received Key** for a `remit_kinds: []` row — so the *reaction* half J-O actually
threatens does not exist here at all. What this document depends on is narrower: **the emission side**
(`world.event_fired` as a log entry `targets[]`/`causes[]` can chain through) — which `01 part2 §9.4`'s
own table already marks as surviving a "telemetry only" ruling. **This document is robust to J-O**,
because it was written against the no-latency constraint from the start rather than assuming a mesh
that reacts to itself.

---

## 11. Property audit

**Scope, honestly.** The gate (`we.eligible`'s name for it) is a `gate`; the roll (`we.fire`'s name for
it) is `d_sigma`, consuming `derive_ob` and the margin ladder rather than producing a new resolution
mechanism — and, since §6, run by `05`'s own `fa.gate`/`fa.resolve` rather than by a module this
document ships. Both verdicts below apply to the registry rows §7 declares and to the two resolver
kinds they invoke, whoever runs them; neither this section nor any other in this document offers an
N/R/S/E verdict for a gate on its own, per the methodology's own rule (`01 part2 §13`) — the roll
inherits the dice engine's own verified properties rather than re-deriving them.

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

**Necessary** — one registry block, **zero new modules** (§6 — collapsed onto `05`'s dispatcher, T3-2),
one schema field (`origin:`) and one selection rule (§6's target-keyed priority pass) added to
existing grammars rather than new ones. §8 records seven candidates refused, three of them ("Calamity
aftershock," a Knot-targeting event, a bespoke sampler) refused specifically because nothing on disk
or in canon licenses them, not because they were merely unwanted. **Robust** — the two failure
directions the task names by name (never fires / fires every season) are closed by G-1 and by
`cooldown ≥ 1`, both load-time checks; the "content that cannot be reached" failure is closed by §4.1's
enumeration; the "content the player cannot act on" failure is closed by §4.2's structural closure
check. **Smooth** — one obstacle owner, one decay law, one disclosure contract, one write rule with
four leaves, one action-row schema (§2, shared with `05`), all reused, none re-derived. **Elegant** —
the corollary in `00 §1` asked for "one object with a registry of kinds" for exactly this document;
§7's four rows are one row shape with a terrain slot rather than four bespoke mechanisms, that one row
shape is itself `05`'s and not a second one, and the whole design adds zero standing verbs (§9). The
honest deduction, matching `01`'s own candor about its edge container: **the route-severed row's
shared flag (§7) is the one object in this document whose ownership is genuinely unsettled** — named
as a shape proposal for `07`/`12` rather than asserted as this document's to decide.
