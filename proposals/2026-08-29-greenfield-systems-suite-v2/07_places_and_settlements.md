# 07 — Places and settlements: the Place object, growth/decay, presences, strata, terrain

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## `systems/settlements/settlement_layer_v30.md` · `systems/settlements/valoria_geography_v30.yaml` ·
## `systems/mass_battle/mass_battle_v30.md` · `systems/settlements/valoria_political_hierarchy_v30.md`
## Produces: the Place identity/form split, its growth/decay transition rows, presences, strata, terrain
## Cites, does not design: `05` (`act.contest_influence`), `06` (faction treasury aggregate), `08`
## (governance verbs, facility-building), `09` (projects — including the founding override below),
## `10` (the Slate — every emission here is a candidate, not a push), `11` (world events), `12`
## (terrain → mass-battle seam), `04` (caste gating, appointment)

Scope, per assignment: **changes A and F** — the Place object, growth/decay form transitions with
mandatory hysteresis, presences, strata, terrain. Near-zero playing surface: this is substrate. §9
is the whole player-facing surface of this document.

## Overrides

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **07-O-1** | v1 `07 §1`'s `owner_faction` as a **stored identity field** on Place | this suite's own v1 | a second source of truth for "who controls this place" next to the governor post's `principal` (`01 §4`) is exactly the redundancy the write rule exists to prevent. **Cut.** Control is *derived*: `controller(place) = principal of the currently-held governor post sited here`, `None` if vacant. §1.2 |
| **07-O-2** | Canon's **four independent Church infrastructure axes** as four separately-stored fields (`settlement_layer_v30.md §1.5`: Religious Building tier / Templar Station / Inquisitor Base / Church Governor, each an independent binary or tier) | ratified canon (Class A, this section CANONICAL) | argued in §4.4: re-implemented as **one continuous `presence.church` gauge** (already declared by `01 §5.2`) **plus typed `facilities[]` entries** carrying the discrete building state. Nothing canon distinguishes is lost — each axis is still individually true or false per settlement — only the *storage shape* changes, from four ad hoc fields to the two primitives this suite already has. Axis 4 (Church Governor) collapses cleanly into `controller(place) = Church`, which 07-O-1 already gives for free |
| **07-O-3** | **My own task brief's instruction, resting on the current canon census** — "settlement count is fixed at 35; growth converts a node's form, it never adds nodes" (`settlement_layer_v30.md:310,437` — 35 Kingdom settlements, 37 with the two special-case march-targets) | *(per the 2026-08-29 authority amendment)* a design constraint drawn from canon's **current state**, not a Jordan ruling or a closure canon asserts — argued on merit in §3.5 | Canon **itself** anticipates a variable set: *"if/when Warden-led healing succeeds, settlements may emerge in T15 Askeheim... Future Class A"* (`valoria_political_hierarchy_v30.md:136`). §3.5 designs founding/ruin as a form transition on **pre-declared placeholder nodes**, so the *adjacency graph stays static at load* (the stability property the census argument protects) while the *active* settlement count varies at runtime. Zero new primitives, zero graph mutation, one new `kind` value doing two canon-anchored jobs at once |

**Not overridden:** the four-leaf write rule, the disclosure contract, the herald shape, `derive_ob`,
and everything else `01`/`01 part 2` establish. This document composes on them without exception.

---

## 1. The Place object

### 1.1 Identity and form, per `01 §1.1`'s normative table — plus one field it left silent

```
identity(place)  IMMUTABLE
├── site_id          : str
├── founding_season  : int
├── terrain          : one of eight registry-declared types (§6)
└── parent           : node_id | None    ← ADDED (see note)

form(place)      MUTABLE, only through a declared transition (§3)
├── kind        : registry-declared — Ruin·Outpost·Village·Town·City·Seat·Fortress·Cathedral·Port·Mine
├── tier        : settlement | territory | province | country (`00 §3.1`'s containment axis)
├── facilities[]: typed rows {kind, tier?} — what is built here (§1.3)
└── presences{} : {institution_id: level_gauge} — §4

gauges  : acceptance.{legitimacy,support} · condition.{order,prosperity,defense} · pressure ·
          presence.<institution> · accrual.entitlement          — all P-4, declared once (`01 §5.2`)
tags    : Precedent · Grudge · Debt · Reputation · Leverage · Memory, on this place as owner
posts   : [post_id] sited here, per §1.3
residents (derived) : persons whose `origin_node` is this place, absent a later relocation
                       tag (§8's WR gap — 03 owns the mechanism; not designed here)
```

**`parent`, added.** `01 §1.1`'s per-kind table lists `site_id, founding_season, terrain` for place
identity and is silent on containment. A settlement's containing node is a physical-map fact, not
game state — it belongs beside `terrain` for the same reason: it is what makes this place *this*
place, not something a season's play changes. Reported per the brief: this is the one thing the
primitive layer did not explicitly supply; adding it costs no new stored *kind*, only a field.
**Adjacency is not an entity field at all** — it lives in the map graph in `references/form_registry.yaml`
(§2), keyed by `entity_id`, the same place v1 kept it (`07 §2` there).

### 1.2 `controller` is derived, never stored (07-O-1)

```
controller(place) = principal of the governor post currently sited here, or None if vacant
```

One consequence for every formula below that used to read `place.owner_faction`: it now reads
`controller(place)`. **Vacancy propagates honestly** — an unheld governor post makes a place
controller-less, which is exactly `01 §4.1`'s vacancy-as-a-first-class-state, not a special case.

### 1.3 Posts are sited by kind — carried from v1, restated against the new roster

A `kind` row declares `sites_posts`. `Village`/`Outpost` site none (per `settlement_layer_v30.md §4.5`'s
own count — Outpost sites **0** Local Actors and, by the same logic, no governance post); `Town`,
`Port`, `Mine` site a `governor`; `Fortress` sites a `governor` and a `commander`; `Cathedral` sites a
`governor` (naturally Church-affiliated, §4.4); `City`/`Seat` site a `governor` and, at `tier: province`
or above, the province's own head/ministers. **Which places have governance is data** — a registry
column, never a branch — carried unchanged from v1 `07 §4`.

---

## 2. `references/form_registry.yaml` — the rows this document contributes

`00 §9.1` folds v1's `tier_registry.yaml` into this file, because the containment ladder is a place's
*form*. This document is the source of the place-kind vocabulary, the node graph, and the
growth/decay transition rows (§3); it adds **rows**, never a file.

```yaml
entity_kind: place
kinds:
  - {kind: Ruin,      tier: settlement, sites_posts: [],                  weight_base: 0}
  - {kind: Outpost,   tier: settlement, sites_posts: [],                  weight_base: 1}
  - {kind: Village,   tier: settlement, sites_posts: [],                  weight_base: 1}
  - {kind: Town,      tier: settlement, sites_posts: [governor],          weight_base: 2}
  - {kind: Port,      tier: settlement, sites_posts: [governor],          weight_base: 2}
  - {kind: Fortress,  tier: settlement, sites_posts: [governor,commander],weight_base: 2}
  - {kind: Mine,      tier: settlement, sites_posts: [governor],          weight_base: 1}
  - {kind: Cathedral, tier: settlement, sites_posts: [governor],          weight_base: 3}
  - {kind: City,      tier: settlement, sites_posts: [governor],          weight_base: 3}
  - {kind: Seat,      tier: settlement, sites_posts: [governor],          weight_base: 3}
  gauge_bounds: {inherits: descriptor_registry.yaml settlement_stats}   # set.legitimacy 0-7 etc.

nodes:
  - {node_id: <id>, kind: <kind>, parent: <node_id|null>, adjacency: [<node_id>...]}
  # 35 Kingdom + 2 special-case march-targets, cited verbatim from settlement_layer_v30.md:437
  # PLUS a bounded set of `kind: Ruin` placeholder nodes (07-O-3, §3.5) — count/siting is a WR
  # content decision (Askeheim marsh polygon per valoria_geography_v30.yaml:748, not fixed here)

transitions: [ALL growth/decay/founding rows — §3]
```

**`weight_base` is cited, not invented**: Seat 3, City 3, Cathedral 3, Town 2, Fortress 2, Port 2,
Village 1, Mine 1, Outpost 1 (`settlement_layer_v30.md:160`). **`Ruin: 0`** is this document's own
addition, argued in §3.5. **A named gap, not filled here:** canon's own Local-Actor count-by-type
table (`settlement_layer_v30.md §4.5`, cited by `00`'s J-M execution at `11.5.4`) has **no row for
`Village`**, despite Village settlements existing in the live node registry (e.g. S-005 Saatfeld,
`:329`). This document does not invent the missing count; it is a citation to route to 03/WR.

### 2.1 Load-time validations — carried from v1 `07 §2.1`, renamed to avoid colliding with the
archived doc's own `V-1..V-4`, and updated for the new roster

| # | validation | the class it kills |
|---|---|---|
| **L-1** | every `parent` resolves to a live node of the tier immediately above | a place sited in a container that does not exist |
| **L-2** | `adjacency` is symmetric and every member is a live node | a one-way edge a graph walk dead-ends on |
| **L-3** | every `kind` is in the declared set above, and declares gauge bounds for every gauge it carries | a kind with no entry in the table that reads it |
| **L-4** | every declared gauge satisfies `rest + max_seasonal_accrual/λ ≤ ceiling` (`01 §5.1`) | a gauge whose accrual sources can pin it at ceiling |

All four are arithmetic over the registry, need no campaign run, and are load-time raises.
**New, v2:** **L-5** — every `reversible: true` transition row satisfies `01 §2.3`'s
`θ↑ − θ↓ ≥ H_MIN(gauge)` and `dwell ≥ 1`. This is `01`'s own falsifier, instantiated here because
place-kind pairs are where it first has teeth.

---

## 3. Growth and decay: the fourth write leaf, applied

### 3.1 No new module — this is the elegance argument for the whole section

`01 §12`'s `substrate.form` already declares `{entity_kind: place, field: kind}` and
`{entity_kind: place, field: tier}` in its `form:` list and `transitions: [ALL declared rows in
references/form_registry.yaml]`. **It is the generic gate-evaluator for every declared transition
row against every entity of the matching kind.** Growth and decay therefore need **zero new
modules** — only data, added to §2's `transitions:` list. This is the strongest instance in this
document of `00 §6` principle 3 ("a module is a registry row, not a branch"): a settlement growing
from Village to Town is a fact about the registry, not a new piece of code.

*Emergent possibility lost if this section were cut:* settlements would be frozen at whatever kind
world-gen assigned them — no growth, no decline, and (per 07-O-3) no frontier ever resettled and no
ruin ever falling. This is change A's namesake defect, concretely.

### 3.2 The civic ladder — Outpost ↔ Village ↔ Town ↔ City

The generic transition shape, per `01 §2.2`:

```yaml
transition: settlement_grow_outpost_to_village
entity_kind: place        field: kind
from: Outpost              to: Village
gate: condition.prosperity_band(place) ≥ Developing, sustained `dwell` seasons     # SHAPE PROPOSAL
cost: none                                     # a gate, never a purchase — 01 §2.2
emits: form.transitioned                       reversible: true
hysteresis: {band: H_MIN(condition.prosperity), dwell: 2}      # computed per 01 §2.3, not invented
class: substrate
```

and its mirror, `settlement_decay_village_to_outpost`, gated on `condition.prosperity_band ≤ Failing`
sustained the same `dwell`. **`Village → Town` and `Town → City` are the same shape**, each keyed to
the next prosperity band up, each declared `reversible: true` with its own `H_MIN`. Four kinds, three
reversible pairs, one generic row shape — a table, not three bespoke designs:

| pair | primary gate driver | why this gauge |
|---|---|---|
| Outpost ↔ Village | `condition.prosperity` sustained | a frontier post becoming a lived-in community is first a subsistence fact |
| Village ↔ Town | `condition.prosperity` **and** `condition.order` sustained | a town implies the governance post `sites_posts` now requires (§1.3) — order must hold before a governor is worth seating |
| Town ↔ City | `condition.prosperity` sustained at a higher band, **and** `facilities[].count ≥` a declared floor | v1 `07 §6`'s facility-progression argument, unchanged: a city is a town that was *built up*, not merely one that got lucky for a season |

**The thresholds above are shape proposals, not ledger constants** — this document does not calibrate
`Developing`/`Failing` band edges or the exact `dwell`; `01 §2.3`'s `H_MIN(g) = max_seasonal_deposit(g)
+ λ_g·(ceiling_g − rest_g)` is computable at declaration time from `descriptor_registry.yaml`'s
`set.prosperity` scale (`0–5`, `:169`) once its λ and depositor caps are fixed, and **L-5** (§2.1)
refuses to load a pair that violates it. That is the whole of what stops a settlement flickering
between Village and Town every season — a property of the arithmetic, not of tuning.

### 3.3 Specialization — Fortress, Cathedral, Port, Mine, as a second pattern, one worked example

The civic ladder is a size axis; **Fortress/Cathedral/Port/Mine are functional specializations**, not
sizes, and canon already treats them as reversible: a Fortress can be **demoted to a civilian Village**
(`settlement_layer_v30.md:502`, "S-020 Spartfell Village — Demoted to Village civilian quarter of
S-021 Spartfell Fortress"). One worked row, generalizing to the others by the same shape:

```yaml
transition: settlement_specialize_town_to_fortress
entity_kind: place        field: kind
from: Town                 to: Fortress
gate: facilities[] contains {kind: garrison} AND condition.defense_band sustained ≥ Fortified
reversible: true            hysteresis: {band: H_MIN(condition.defense), dwell: 2}
```

`facilities[] contains {kind: garrison}` reads **form**, not a gauge, satisfying `01 §2.2`'s "gate over
gauges, tags, form and identity" — and it is why this is a **gate**, never a roll: the uncertainty was
in building and holding the garrison, not in the reclassification. The reverse (`Fortress → Town`) is
what canon's Spartfell example already is, expressed as this suite's fourth write leaf instead of an
ad hoc "demotion" rule. `Cathedral` (gated on `presence.church` + a `religious_building` facility, §4.4),
`Port` (gated on `terrain ∈ {coast, fjord_coast}` — an identity check — plus a `docks` facility), and
`Mine` (gated on terrain + a `shaft` facility) are the same pattern; their rows are declared in the
registry, not re-derived in prose here.

### 3.4 What decays into what — the floor is not silent

An `Outpost` that keeps failing its gate **does not vanish**. Without §3.5, `Outpost` is simply the
floor: gauges pin low, no post is sited, and the place sits there — a legitimate, boring outcome, not
a defect. §3.5 gives it one further floor, `Ruin`, and argues why that costs one registry row rather
than a new mechanism.

### 3.5 Founding and ruin (07-O-3) — one `kind` doing two canon-anchored jobs

**The override, argued.** Canon already names the emergent possibility this closes:
*"if/when Warden-led healing succeeds, settlements may emerge in T15 Askeheim... the duchy assignment
for a healed Askeheim is undecided... Future Class A"* (`valoria_political_hierarchy_v30.md:136`).
Askeheim is also canon's own explicit zero-settlement zone (`settlement_layer_v30.md:310`) and its
Calamity epicenter (`valoria_geography_v30.yaml:748`) — a wilderness of pre-Calamity ruins by the
setting's own premise. **`Ruin` is the same kind value for both stories**: a node that was never
settled and a node that once was and collapsed are indistinguishable in what they *offer* a founder —
bare terrain, no yield, no posts — and distinguishable only in their **Tags** (a Ruin with a `Precedent`
tag citing a prior collapse has a history; a virgin wilderness node does not). One kind, not two.

**Why this preserves graph stability rather than spending it.** The concern the census argument
protects — a fixed adjacency graph the registry, the FI investigation surface and the mass-battle
seam can all rely on — is preserved exactly: `references/form_registry.yaml`'s `nodes:` list is
declared once, at load, and **never gains or loses an entry at runtime.** A bounded number of
`kind: Ruin` placeholder nodes are declared in that same static list (sited in Askeheim's polygon,
count and exact siting a WR content decision, not fixed here) with pre-declared `parent`/`adjacency`
exactly like every settlement node. **Founding and abandonment are then ordinary `kind` transitions on
already-existing entities** — no entity is ever created or destroyed, so the one-write-rule's
"identity is never written" is not even approached.

```yaml
transition: place_found
entity_kind: place        field: kind
from: Ruin                 to: Outpost
gate: a Tag {kind: Precedent, key: founding_claim, owner: this place} exists, deposited by the
      firing effect of a Project (09 am.fire) naming this transition
reversible: false           # a founding is not undone by decay; decay runs Outpost -> Ruin instead
```

```yaml
transition: place_ruin
entity_kind: place        field: kind
from: Outpost               to: Ruin
gate: condition.order AND condition.prosperity both at floor, sustained dwell ≥ 3   # SHAPE PROPOSAL
reversible: false            # re-founding is place_found again, from Ruin, not a reverse of this row
```

**Why neither pair needs `hysteresis:`.** Both are declared `reversible: false` — the founding/ruin
cycle is not a single reversible pair oscillating on one gauge; it is two one-way rows connected
through a third state (`Outpost`), the same shape the Knot's `intact → ruptured` uses (`01 §7.5`) and
for the same reason: **L-5 does not apply to either row**, and that is a property of the declaration,
checked at load, not an exemption granted in prose.

**Verb-free, on purpose.** `place_found`'s gate reads a **Tag**, never a Key and never a player action
directly (`01 §9.3`'s no-latency rule: the gate reads *state left behind*, not a message in flight).
The Tag is deposited by **09's** project-fire effect — a faction or bloc's *ambition* to found a
colony, not a menu item in this document. **Colonization is what a faction's ambition looks like when
it succeeds**, never a `pl.*` verb. This is cited, not designed: `09` owns `am.fire` and the project
composition; `07` only declares the transition the fire effect is permitted to name.

**What is explicitly left open, honestly.** The healed-Askeheim duchy assignment canon itself calls
"undecided" is not resolved here — a founded node's `parent` is fixed at *declaration* time (L-1), so
which province a newly-founded Askeheim settlement belongs to is a WR/political ruling this document
does not make. Count and siting of placeholder nodes: likewise a WR content decision.

*Emergent possibility lost if this subsection were cut:* the world could gain new frontiers and lose
old ones in prose (world events, §7) but never on the map the player actually acts against — every
Calamity-healing arc canon has already gestured at would have nowhere to land.

---

## 4. Presences — the institutional layer

### 4.1 What it is, in one gauge per institution

`presences{}` is `{institution_id: presence.<institution> gauge}`, already declared by `01 §5.2` as
the replacement for "a bespoke Church/Guild/Warden reach field." The institution roster is content,
not code — rows in `references/content_registry.yaml`:

```yaml
presence_kinds:
  - {id: church,       cites: "settlement_layer_v30.md §3.3 row 1"}
  - {id: guild,        cites: "settlement_layer_v30.md §3.3 row 2"}
  - {id: restoration,  cites: "settlement_layer_v30.md §3.3 row 5; peninsular_strain_v30.md:162"}
  - {id: warden,       cites: "settlement_layer_v30.md §3.3 row 6"}
  - {id: military_order, cites: "settlement_layer_v30.md §3.3 row 4 (Löwenritter)"}
  - {id: covert,       cites: "settlement_layer_v30.md §3.3 row 7 (Niflhel) — presence undisclosed
                              until discovered; see §4.5"}
```

Six institution kinds, cited from the live canonical `§3.3` table — this document adds no institution
canon does not already name a subnational management relationship for.

### 4.2 The four things presence does — each closing an absence the delta spec named

1. **What `act.contest_influence` moves.** `05`'s new action family raises a rival's `presence.<inst>`
   against the incumbent's — cited, not designed here.
2. **Gates which facilities may be built, and facilities are FI investigation surfaces.** A
   `religious_building` facility entry requires `presence.church` past a declared band; **once built,
   it is a named, typed thing fieldwork can target** — a Chapel, a Guildhall, a Warden watch-post, each
   an object with a Depth axis (`fieldwork_v30 §…`, cited not restated). **`08` owns the build verb;
   this document owns the fact that a facility, once built, is a citable investigation surface.**
   Niflhel's `covert` presence is the one exception: it gates no visible facility, and its existence is
   a `Memory`/`Precedent` tag a discovering investigator writes, not a `facilities[]` entry — this
   preserves canon's "not visible unless discovered" (`settlement_layer_v30.md §4.2` row 3).
3. **Adds a stratum to the place's economy** — §5.
4. **Is how the Church/RM/Wardens reach a place at all.** Before this section, a place had no
   representation of "who besides the governor operates here"; `presences{}` is that representation,
   at the substrate layer, surfaced only as a situation (§9), never a screen.

### 4.3 Presence is a gauge — it decays and is bounded like every other

`presence.<institution>` follows `01 §5.1`'s geometric law exactly: it is deposited into by that
institution's own actions (`act.contest_influence`, a Project's advance, a world event, §7) and
decays toward a low rest value absent sustained investment — **an institution that stops showing up
fades**, the same shape as every other gauge, no bespoke "influence decay" rule.

### 4.4 The four Church axes, re-derived (07-O-2, argued)

| canon axis (`settlement_layer_v30.md §1.5`) | v2 shape |
|---|---|
| Axis 1 — Religious Building (None/Chapel/Church/Cathedral, mutually exclusive) | one `facilities[]` entry `{kind: religious_building, tier: none\|chapel\|church\|cathedral}`, unlocked by `presence.church` band |
| Axis 2 — Templar Station (binary) | a `facilities[]` entry `{kind: templar_station}`, same gate |
| Axis 3 — Inquisitor Base (binary) | a `facilities[]` entry `{kind: inquisitor_base}`, same gate |
| Axis 4 — Church Governor (binary, "de facto Church territory") | `controller(place) = Church`, i.e. the governor post's principal — **07-O-1 gives this for free, no fourth field needed** |

Nothing canon distinguishes is lost: four independent facts about a settlement are still four
independent facts, individually inspectable (each `facilities[]` entry has its own provenance and
disclosure). What changes is that they are now **one gauge plus typed rows already declared by `01`**,
instead of four bespoke fields — the exact reuse `00 §1`'s under-distillation test asks for
("two objects doing one job").

*Emergent possibility lost if presences were cut entirely:* a place would be numbers with nobody
living in it — no Church, no Guild, no Restoration cell, no Warden watch, ever reachable at the
settlement grain (`06 §3.3`'s whole "subnational faction" layer would have no home).

---

## 5. Strata — the economic/social layering, derived

### 5.1 A stratum is a claim on yield, not a stored primitive

`00 §1`'s corollary ("prefer one object with a registry of kinds") applies at full force here: strata
are **not** a fifth stored kind. They are a **derivation** over `presences{}` and `yield` (§6):

```
claim(place, institution) = yield(place) · share(institution, presence_band(place, institution))
residual(place)           = yield(place) − Σ_institution claim(place, institution)
```

`share` is a registry-declared band→multiplier table, per institution, capped so
`Σ_institution max_share(institution) ≤ 1` — **a load-time check (L-6, alongside L-1..L-5)**, which is
what guarantees `residual ≥ 0` structurally rather than by luck. **This is `05 §4.2`'s custody
discipline one level up**: a claim biases who gets what; it never consumes the whole thing.

**All bands, no numbers.** As with §3.2's growth thresholds, `share`'s specific multipliers are a
shape proposal, not asserted here as calibrated constants.

### 5.2 What a claim feeds

`claim(place, institution)` is the resource a bloc or faction project (`09`) advances with when its
owner holds that presence — the mechanical sense in which "you can feel the Ehrenwall wing's interest
in every appointment" (`00 §2.1`'s own example): a bloc whose faction has a large Church claim at a
place has something concrete to lose if `act.contest_influence` drains it. `residual(place)` is what
feeds `06`'s faction-treasury aggregate through `controller(place)` — the ordinary case where no
institution has meaningfully entrenched itself.

**`residents` (§1.1) are not a claimant.** The population's stake is expressed through
`acceptance.{legitimacy,support}` (already gauges) and Local Actors (`settlement_layer_v30.md §4.5`,
seeded via `03` per the J-M ruling), not through a second accounting channel — adding one would be
exactly the under-distillation §0 forbids.

*Emergent possibility lost if strata were cut:* every institution present at a place would be
scenery — visible in `presences{}` but with nothing at stake, which collapses `act.contest_influence`
(05) into a number-go-up minigame with no material reason to fight over it.

---

## 6. Terrain

### 6.1 Identity, drawn from a closed eight-member registry

`terrain` is part of `identity(place)` (§1.1) — the physical land under a settlement does not change
in ordinary play, and 01's normative table already fixes this. The type is one of the eight declared
in `valoria_geography_v30.yaml:675`: **plains · forest · highland · mountain · mountain_pass ·
fjord_coast · coast · marsh**, assigned at world-gen by which polygon a node's coordinates fall
within (`:676-752`). Mountain terrain (`terrain_cost_matrix: mountain: 999.0`, `:766`, effectively
impassable) sites no settlement in practice, which is why none of the 35 do.

**Genuinely open, not designed here.** Whether a place's terrain may ever change (a Calamity event
turning plains to marsh, say) is left as a question for a later ruling, not decided by silent
omission: `01`'s per-kind table fixes terrain as identity, and this document does not propose an
override against a sibling document at the same authority tier as itself. If that possibility is
wanted, it needs the same treatment §3.5 gave founding — a proposal, argued, not a default.

### 6.2 The seam to mass battle — cited, not duplicated

`mass_battle_v30.md §A.9` derives its own six-row Terrain effect table (River crossing · Uphill ·
Forest/broken · Walls/fortifications · Narrow pass · Open flat) from `valoria_geography_v30.yaml`'s
terrain polygons at the engagement's coordinates (`:547-548`, ED-780) — **a different vocabulary at a
different scale**, not this document's eight identity types read directly. `12_adjacent_systems.md`
owns that mapping. What `07` supplies to it: (a) the place's terrain identity (§6.1); (b) whether a
`facilities[]` entry of kind `garrison`/`walls` is present (§3.3), which is what the mass-battle
`Walls / fortifications` row actually keys on, per `settlement_layer_v30.md`'s own Fortress-chokepoint
example (`:906-910`: a Fortress "cannot be bypassed unless the invader's Military exceeds the Fortress
Defense by 3+"). **07 supplies the facts; 12 supplies the mapping.**

---

## 7. Yield — carried from v1, updated for the primitives that moved

```
yield(place) = base_yield(kind)
             · f(condition.prosperity band)
             · compliance(acceptance band)
             · fiscal_stance_multiplier(controller(place).policy)     # was owner.policy — 07-O-1
```

`compliance` is monotone in the acceptance band, in `[0,1]` — the term that makes extraction
self-limiting, carried verbatim from v1 `07 §5`. **Nothing about the formula's shape changed**; only
`owner` became `controller`, and the place no longer holds its own `accrual.budget` — the governor's
action points are `post.budget` (`01 §12`'s `substrate.post`), not a place gauge, per `01 §5.2`'s
roster moving budget to the post it belongs to (`05 §3`'s per-post budget ruling). `accrual.entitlement`
(the levy channel) stays a place gauge — it is a property of the place's population, not of who
currently holds the governing post.

---

## 8. What in a place is reachable — by world events, by fieldwork, and by nothing at all

### 8.1 World events (`11`) — the exogenous surface

Per `01 §9.3`, a world event may only **read state and deposit** — never target a form field
directly. Reachable: `condition.{order,prosperity,defense}`, `pressure`, `accrual.entitlement`,
`presence.<institution>` (an event can be an institution's own arrival, e.g. a missionary wave), and
Tag appends (a Precedent of "plague, S-014, season 40"). **Not reachable directly:** `kind`, `tier`,
`facilities[]` — an event can crash `condition.order` hard enough that a *later* accounting boundary's
gate finds `place_ruin`'s predicate satisfied, but the event itself never writes `kind`. This is
`01 §2.2`'s "crossing fact, never a forecast" rule doing double duty: an event cannot announce a
demotion in advance any more than a form transition can.

### 8.2 Fieldwork and infrastructure (`08`/FI lane) — the investigation surface

Every `facilities[]` entry is a named target (§4.2 point 2); `terrain` and `kind` are published
identity/form facts (disclosure `exact`, §8.3) an investigator can read without a check; `presences{}`
levels are `band`-disclosed, so an investigator can learn "the Church has a strong hold here" without
the exact gauge. **08 owns the verbs that build facilities and respond to what fieldwork finds; 07
owns the fact that a built thing is a legible object.**

### 8.3 Disclosure, per `01 §8`

| of | inputs | presentation | trigger |
|---|---|---|---|
| `acceptance.*`, `condition.*`, `pressure`, `presence.<inst>` | published | band | hidden |
| `accrual.entitlement` | published | exact (spent directly, §7) | hidden |
| `kind`, `tier`, `facilities[]`, `terrain` | published | exact | hidden — **and no growth/decay gate is ever published** (§3's crossing-fact rule) |
| `controller(place)` | published | exact | n/a — a derivation, not a trigger |

---

## 9. The player surface — everything a player actually touches here

| what the player touches | how | how often |
|---|---|---|
| a place's `condition`/`acceptance`/`pressure` **band** and its `presences{}` **bands** | a Slate item or place summary | whenever a situation there is on screen (`10`) |
| the fact that a place grew, decayed, was founded, or fell to ruin | a `form.transitioned` Key surfaced as a Slate candidate | when it happens, never as a countdown |
| a facility's existence and provenance (an investigation target) | fieldwork, on demand | never pushed |

| what the player never touches |
|---|
| firing a growth/decay/founding/specialization transition directly, or naming its gate |
| depositing into any place gauge, or reading an exact value where the contract says band |
| the `Ruin → Outpost` founding gate — that is a faction/bloc project's business (`09`), not a place menu |
| assigning `presences{}`, `terrain`, or `parent` |

**Substrate objects here: 1 entity kind reused (place) · 10 `kind` values · 4 form fields · 6
gauge families (one is per-institution) · 6 tag kinds reused · 2 new load-time checks (L-5, L-6) · 1
new content_registry block (presence kinds). Surface affordances: 3 reads, 0 verbs.** The ratio this
document's own §0.1 test demands.

---

## 10. Module contracts

Growth, decay, founding and ruin need **no module of their own** (§3.1) — they are rows the shared
`substrate.form` (`01 §12`) already evaluates. What remains for `places` to own:

```yaml
- module: pl.registry
  parent: places            class: substrate
  scales: [settlement, territory, peninsula]     tier: null
  resolver: gate            remit: []             budget: null      consumes: []
  emits: []
  state: [{name: entity, bucket: entity, writable: false, owner: substrate.entity}]   # loaded, not written
  form: []                  transitions: []
  disclosure: [{of: entity, inputs: published, presentation: exact, trigger: hidden}]

- module: pl.gauges
  parent: places            class: substrate
  scales: [settlement, territory]                tier: settlement
  resolver: accrual         remit: []             budget: null      consumes: []
  emits: []
  state:
    - {name: acceptance.legitimacy, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support,    bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.order,       bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.prosperity,  bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.defense,     bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: pressure,              bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: accrual.entitlement,   bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: presence.<institution>,bucket: gauge, writable: true, owner: substrate.gauge}   # one per content_registry row, §4.1
  form: []                  transitions: []
  disclosure: [see §8.3's table — one row per state entry above]

- module: pl.strata
  parent: places            class: substrate
  scales: [settlement]      tier: settlement
  resolver: derivation      remit: []             budget: null      consumes: []
  emits: []
  state: [{name: strata_claim, bucket: gauge, writable: false, owner: pl.strata}]   # read-only view, §5
  form: []                  transitions: []
  disclosure: [{of: strata_claim, inputs: published, presentation: band, trigger: hidden}]

- module: pl.yield
  parent: places            class: substrate
  scales: [settlement, territory]                tier: settlement
  resolver: derivation      remit: []             budget: null      consumes: []
  emits: []
  state: [{name: yield, bucket: gauge, writable: false, owner: pl.yield}]
  form: []                  transitions: []
  disclosure: [{of: yield, inputs: published, presentation: exact, trigger: hidden}]
```

`pl.strata` and `pl.yield` are `writable: false` — nothing writes a claim or an income; both are what
the place's actual state comes to. **The `form:`/`transitions:` fields are empty on every module in
this list**, which is the point of §3.1: the grep that answers "what can change a place's kind" finds
only `substrate.form`, one line, in one file (`01`).

---

## 11. Property audit

**Scope, honestly.** `pl.registry` is a validated load; `pl.gauges` is accrual and decay;
`pl.strata`/`pl.yield` are derivations; the growth/decay/founding/ruin machinery is `substrate.form`'s
`gate` resolver applied to this document's data. **Nothing here rolls. No N/R/S/E verdict is offered
for a store or a gate** (`01 §13`'s own scope limit, inherited) — what follows is the two properties
that do apply, the loops, and the qualitative verdicts as judgments.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass** | every place gauge is bounded per `01 §5.1`; `kind`/`tier` are enumerated, so bounded by construction; `facilities[]` is bounded per-kind by a declared ceiling (v1 `07 §6`, unchanged) |
| **P-v** right engine | **pass** | every transition here is `gate`; `pl.strata`/`pl.yield` are `derivation`. Nothing in this document rolls, and re-rolling a growth threshold would charge twice for uncertainty already spent getting the gauge there (`00 §6` principle 4) |

### 11.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| prosperity ↔ civic-ladder `kind` | `θ↑ − θ↓ ≥ H_MIN`, `dwell ≥ 1`, checked at load (L-5) | **bounded arithmetically** — cannot flicker by construction |
| facility → accrual/defense → specialization `kind` → facility ceiling | v1 `07 §6`'s per-kind facility ceiling | **unmeasured**, campaign-reachable; carried from v1 unchanged |
| `Outpost ↔ Ruin ↔ Outpost` (founding/ruin cycle, §3.5) | **terminating per cycle**: both rows are `reversible: false`, so no single row can oscillate; a fresh cycle needs a fresh Project fire (09) each time, which is itself rate-bounded there | **not this document's loop to bound** — it is 09's project-advance bound, cited |
| `presence.<inst>` ↔ `claim` ↔ institution's own project advance | `Σ max_share ≤ 1` (L-6) bounds total extraction; per-gauge decay (§4.3) bounds unattended growth | **unmeasured** |

### 11.2 The four qualitative verdicts

**Necessary** — one entity kind reused, ten `kind` values (nine canon-cited, one new), four form
fields, six gauge families. Every gauge has a named depositor and consumer; `Ruin`'s necessity rests
on the canon citation in §3.5, not on invention. **Robust** — the two failure directions the corpus
measured (an unrecoverable pinned gauge, a flickering threshold) are closed by `01`'s geometric law
and L-5 respectively; a third the census argument raised (graph instability from variable node count)
is closed by never mutating the graph at all (§3.5). **Smooth** — one decay law, one place-gauge
roster, one growth/decay mechanism (`substrate.form`) reused for size, specialization, and
founding/ruin alike; one derivation pattern (strata) reused rather than a second accounting channel.
**Elegant** — the honest deduction: **`Ruin`/founding is this document's one contested addition.**
It buys a canon-anchored emergent possibility at the cost of one enum value and two one-way transition
rows, with the harder half (the founding gate's content, the province-assignment question) explicitly
deferred rather than fabricated. If a reviewer judges that trade not worth it, the fix is to delete
§3.5 and accept `Outpost` as the true floor (§3.4) — nothing else in this document depends on it.

---

## Property audit — falsifiers (per the author brief)

| claim | falsifier |
|---|---|
| the node graph never gains or loses an entry at runtime (§3.5) | a test asserting the count of `place` entities and the edge set of `references/form_registry.yaml`'s `nodes:` list are identical before and after any seeded campaign run, regardless of how many `place_found`/`place_ruin` transitions fired |
| growth/decay cannot flicker (§3.2, L-5) | the load-time test from `01 §2.3`, instantiated over every place-kind pair this document declares `reversible: true` |
| strata claims cannot exceed yield (§5.1, L-6) | a load-time test summing `max_share(institution)` per place-kind and asserting ≤ 1 |
| `controller(place)` never drifts from the sited governor post (07-O-1) | a test asserting no code path stores a place-level controller field; the only read path is the post query |
| no form transition here is ever named directly by a world event or a Key (§8.1) | a static check that no `11`-lane emitter's result names a `form:` field this document declares — the gate always intervenes |
| a facility, once built, is disclosed `exact` and citable by fieldwork (§8.2) | a test asserting every `facilities[]` entry carries a `disclosure:` row with `presentation: exact` |
