# 05 (part 2) — Faction actions: the action set, resolution, contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`05_faction_actions.md`](05_faction_actions.md) — **part 1 first; this continues it**
## Part 1: §§0–4 (the playing surface, the per-tier gate, the per-post budget, `appeal`,
## `act.contest_influence`) — and the `## Overrides` block, which governs both parts
## Part 2: §§5–10 (the eight action rows, the resolution shape, the two effects constraints,
## J-N and J-O, the module contracts, the property audit)

---

## 5. The action set — eight families, one shape

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
  gate: [<predicate over identity, form, gauge band or tag existence>]  # ALL must hold; never a roll
  symbolic_vector: {hierarchical: ±, sacred: ±, instrumental: ±, traditional: ±}
  signal_weight: {<world signal>: <weight>}
  cost: {budget: 1, gauge_deposits: [...]}
  effects: {overwhelming: [...], success: [...], partial: [...], failure: [...]}   # TOTAL over four
```

**The ACTORLESS variant (v3, O-5.13)** — `11`'s world-event rows are rows of this schema, not a second
one. `remit_kinds: []` is the discriminator, and it is already a legal value here (§5.6):

```yaml
  remit_kinds: []            # herald-run, no invoker. Selects the iteration domain AND the pool source
  hazard_pool: <int>         # stands in for attrs + POOL_BASE. ⚠ MUST be in the calibrated band
                             # [6,18]; ob_site.pool_min = pool_max = hazard_pool
  cooldown: <int ≥ 1>        # REQUIRED: no post.budget to be rate-bounded by. 11 §3.2, unchanged
  excludes: [<row id>, …]
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
one.** `tiers: [settlement], remit_kinds: [governor]` is a settlement verb; `tiers: [peninsula],
remit_kinds: [head]` is a national one; `remit_kinds: []` is a world event (§5.6). **The dispatcher
cannot tell them apart**, which is what §10.1's S-property claims and what O-5.11 and O-5.13 make
literally true.

**`act.motion` is cut, not moved (O-5.12) — confirmed against `12`'s sole ownership.** `12 §5`'s
`ad.motion` is self-contained: its own `remit: [head, minister]`, its own `post.budget` cost,
`price(magnitude)` against the proposer's `standing`, a monotone `vote_bar(magnitude)`, a published
`vote_weight`. **This page holds a pointer and no second design** — no motion row, no motion effects
table, no motion `ob_site`. A post-holder raising one invokes `ad.motion`, which `fa.gate` counts in
`action_modules` (part 1 §1) like any other row. **One motion, one owner.**

### 5.1 `act.campaign` is a gate over a declared seam, not a stub

Force-on-force resolution is out of this suite's scope, and saying so **with a specified seam** is
different from leaving a hole.

| | |
|---|---|
| **the gate** (here) | target adjacent to a held node; a `commander` post filled; the committed units exist and are assigned to the field |
| **the seam** | `resolve_force(attacker_units, defender_units, place) → Degree` — one call, one return, on the single-owned ladder |
| **the consumption** (here) | the degree drives an Entry Terms fork: on a lesser margin the taken place keeps its arrangements and seeds `acceptance.legitimacy` high; on a decisive one it does not |

Its interface is specified in both directions, so the caller is complete and testable against a
stand-in, and the seam returns a `Degree` — the currency every other action consumes — so nothing
implementing it can introduce a second degree semantics.

### 5.2 `act.muster` — two economies, separated at birth

Four of four surveyed franchises implement the levy and the professional soldier as **different
economies, not different tiers.** Splitting later means splitting a mechanic that has already accreted
grounding, effects and goldens; two channels from the start cost one extra registry row.

| | **`act.muster.levy`** | **`act.muster.contract`** |
|---|---|---|
| pays with | the place's `accrual.entitlement` gauge | the faction's `treasury` **stock** gauge (§5.2a) |
| rationed by | how fast entitlement accrues — a property of the place | how much money there is |
| upkeep | none | recurring, larger when assigned to the field |
| quality | bounded by the place's `condition` band | bounded by price |
| consent cost | a deposit into `acceptance.support`, scaled by the unit's quality tier | the same deposit at the same scale |

Recruitment is coercive in both channels: the per-unit consent deposit is the live dial, and rarely a
**gate** — a place at the *revolt* band of `acceptance.support` supplies no soldiers either way.
Scoping the gate to that band keeps it from double-counting the dial. `act.muster` is a **`gate`, not a
`d_sigma`**: whether you can afford a unit is answered on the board, and rolling for it is the
wrong-engine defect this tree is most prone to.

**Muster raises no aggregate.** It produces a unit record (`12 §2.1`). Faction military weight is
*derived* from units held; the other way round — mustering raising the number that gates what mustering
can produce — is a loop with no external term at all.

### 5.2a The treasury is a **stock**, not a derivation — the defect and the fix (O-5.10)

**The defect, stated plainly because this page shipped it.** `06 part 2 §9` declares
`faction.treasury` as `{bucket: gauge, writable: false, owner: fm.derive}` — a derivation. The table
above spends it and the row below charges upkeep against it. **You cannot decrement a derivation:** it
recomputes from current state every boundary, so every payment is silently undone at the next
accounting and the contract channel is free. Two readers found it independently from opposite ends —
*"what does the muster economy spend?"* and *"does the fiscal spine fit the four write leaves?"* —
which is the strongest available signal that it is not a wording problem.

**The fix is a vocabulary distinction the suite already needed, not a new object.** AU-1 forbids
*storing an aggregate*; `01 §2.1` now separates the two things that rule was collapsing — an
**aggregate** is recomputable from *current* state (`capacity(faction, tier)`, `faction.weight`,
`divergence`), a **stock** is path-dependent and carries its own in/out history (`treasury`,
`accrual.entitlement`, `post.budget`). **That definition lives once, in `01 §2.1`**, and is cited here
rather than restated as a rule.

`treasury` was mislabelled because *"sum of what my places yield"* **looks** like an aggregate — and is
one **until something spends from it.** The precedent shipped a scale down: `accrual.entitlement` funds
the levy channel and is *spent directly* (`07 §8.3`); nobody proposed deriving it.

**So `faction.treasury` becomes a faction-owned gauge, and it must leave `fm.derive`'s state list —
forced, not preferred.** `00 §7.1`'s falsifier is *"no state name declared `writable: false` may appear
as a gauge id in `references/descriptor_registry.yaml`"*, and a real spendable treasury **is** a
declared gauge id there (§10.4). Leaving `fm.derive`'s row would trip that falsifier the day the gauge
is declared — the mechanism working correctly.

```
treasury : gauge, owner substrate.gauge, scale faction, floor 0, geometric decay per 01 §5.1

  +  boundary deposit  Σ over places where controller(place) == faction  of  residual(place)   # 07 §5.1
  −  boundary deposit  Σ over units held  of  upkeep(unit.unit_kind, unit.assignment)          # 12 §2
  −  act.muster.contract's price                                                               # §5.2
```

**All three terms are leaf 1 — a gauge deposit with provenance.** No setter, no aggregate; the two
boundary terms are *flows*, the shape `07 §5.2` already describes when it says `residual(place)`
*"feeds `06`'s faction-treasury"*. All that changes is that the thing it feeds is a gauge with a floor
rather than a number recomputed from scratch.

**Its bound is free and checkable at declaration time.** As a gauge it obeys `01 §5.1`'s geometric law,
bounded at `rest + a/λ` with **no campaign run** — closing the runaway a plain accumulator would open
(conquer more, bank more, buy more contracts, conquer more); as flavour, an unspent treasury leaks to
graft. **A faction at the floor cannot contract-muster** — a gate, on the board, published exact — and
that is the whole consequence this page designs.

⚠ **One dependency handed on rather than invented.** What happens to a unit whose upkeep the treasury
cannot pay is a **`12`** question (unit form transitions are `12`'s, `:498`). This page states the
constraint — *upkeep must have a consequence, or the floor gate is the only brake on a standing army
and it brakes the wrong end* — and declines to design a disbandment it does not own.

⚠ **The alternative was considered and is NOT shipped.** Pricing contract muster in the post's `budget`
gauge with a recurring `Debt` tag is a valid fallback if the stock route is rejected, but **not
alongside** it: two mechanisms for one economy is the shape-divergence defect the suite exists to stop,
and §2.4 forbids `post.budget` from buying anything but attempts.

### 5.3 `act.inquire` — information **gates**, it never adds dice

Information determining *which arguments you may attempt* is worth having; its hard form — the wrong
choice flatly fails — is a special case bolted into a continuous system, which is scripting drift. The
soft form is a built primitive. `act.inquire` deposits into an `information` gauge on the target, whose
band does exactly two things:

1. **It gates the option set.** Rows declaring `requires_information: <band>` are unavailable below it —
   a gate, on the board, published.
2. **Acting against an uninvestigated target declares a `BandExtension` vetoing Overwhelming**
   (`dice_engine.py:95`, ED-SC-0032). Your ceiling drops; your odds of Success are untouched.

Neither adds a die, shifts an obstacle, or touches the Partial or Failure boundaries. An extension's
only power is to veto the top band — the return channel is bounded to `3 → 2` — and the seam refuses
undeclared context keys rather than swallowing them.
### 5.4 `act.charter` — where a schism finishes, and the hole it closes

**The hole, stated first because this page was where it died.** `06 §3.5` hands the chartering act
here in as many words — *"the chartering act itself is `05`'s … creating an entity is generation"*
(`06:346-350`) — and this document shipped eight action families, **none of them a charter.** So a bloc
reaches `in-schism`, its project *"becomes a founding claim"*, and the claim had **no executor in any
of the three documents that share the seam.** Change C's marquee possibility — a faction emerging from
inside an institution, with no faction-emergence subsystem — terminated in a dangling sentence.

**Why it could not fall out of existing machinery.** `09 §6.2` binds a project fire to `01 §2.1`'s
four write leaves and **entity creation is not one of them**. `07` dodges this at place scale with
pre-declared `kind: Ruin` nodes, so a founding is a *form transition* on an entity that already exists
(`07 §3.5`). **Factions have no placeholder equivalent** — a roster of empty faction shells would be
authored content standing in for emergence, which `00 §6` principle 2 forbids. So the founding must
*create*, and creation is **generation**, which `00 §4.1`'s P-1 licenses (*"created at load or by
generation"*) and which this page **already does once**: `12 §2.1` — *"Muster (`05 §6`) still produces
the entity."* `act.charter` is that act on a different kind.

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

**The gate reads a Tag, exactly as `07`'s `place_found` does and for the same reason** — `07 §3.5` is
*"verb-free on purpose"* because its gate reads *state left behind*, never a message in flight (§8.1).
Same artifact, same producer (`09`'s `am.fire`, leaf 2); the executor is a verb only because an entity
must be **created** rather than transitioned. **The producer set is open:** `in-schism` is the only
declared way to deposit `founding_claim` today, and a second project kind depositing it — the bottom-up
founding canon prices at `settlement_layer_v30.md:1046` — needs **zero lines here.** That keeps this a
row, not a schism special case.

**Why `gate` and not the roll canon prices (O-5.8).** Canon's Declaration is a Domain Action —
Influence pool = Renown ÷ 2, Ob 3 — because the ratified design had nowhere else to put the
uncertainty. Here it is **already spent**: the bloc formed on a connectivity gate, held cohesion above
`θ↑` for a dwell, reached `in-schism`, and drove a project to threshold through `am.advance`. Rolling
again **charges twice for uncertainty already paid** — verbatim `07 §9.2`'s argument (`00 §6` principle
4). It also fails P-iv: a failed Declaration on a *fired* project is an irreversible loss on a
routinely-reached roll, which §7 forbids.

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

**The collapse is proved by the two documents' own sentences**, not argued: §10.1 and `08 §9.2` each
independently say a faction action and a settlement verb are one object at different rungs. Field by
field:

| `08` | here | delta |
|---|---|---|
| `sm.gate` — `gate`, `scales: [settlement]`, `consumes: [post.vacant]`, emits `faction.action_declined` | **`fa.gate`** — identical, at `scales: [settlement, territory, peninsula]`, `tier: null` | `fa.gate` already iterates every declared rung. `sm.gate` is it with the loop unrolled to one iteration |
| `sm.act` — `d_sigma`, `remit: [governor]`, `budget: {post.budget, 1}`, eight rows | **`fa.resolve`** — `d_sigma`, `remit: [head, governor, minister, envoy, commander]`, same budget | `governor` was already in that remit. The eight rows gain `tiers: [settlement]`, `remit_kinds: [governor]` and become `act.govern` rows |

**What is NOT absorbed.** `sm.respond` survives untouched: a directive arrives *addressed to a
holder*, so its option set is a function of what was asked, not of what the holder's remit contains — a
different object from *"pick the best thing your remit allows"*, and collapsing it would delete the one
governance decision `08` leaves the player. `sm.business` and `sm.directive` likewise. **The same test
admits `11`'s rows and keeps `sm.respond`** (§5.6), which is what makes it a test and not a preference.

**The cost, stated rather than absorbed silently.** `fa.resolve` must now declare `form:` and
`transitions:` — `sm.act` names facility-tier advance rows (`08 §8`), and per W-5 a module may **name**
a transition the herald applies. So §9's note that *"no module here declares `form:` or
`transitions:`"* is **no longer true** and is corrected there. One field on one module, for eight rows
and two modules deleted.

**Zero outcomes lost, zero surface verbs added.** `08` keeps its slot for `sm.respond`; this page keeps
its one slot, *direct a post's action*.

### 5.6 The actorless variant — `11`'s world-event rows, and the rule that would have gone missing

**Accepted (O-5.13), and the consistency test is why.** `11`'s author reached the same finding
independently, retired his own `we.eligible`/`we.fire` pair, and named what he needed back rather than
assuming it. §5.5 absorbed `08`'s rows on identical evidence; **refusing `11`'s would have been a
preference dressed as a principle.** The schemas differ in two fields — `remit_kinds: []` and
`hazard_pool`, one optional field each — against a shared gate half, `derive_ob` obstacle, four-band
totality under the same P0-3 audit, per-row rate bound, `ob_site` declaration and `10 §2.1` hand-off.

**Both extensions are the same move, which is why they are cheap: the dispatcher's KEY, POOL and
ORDERING come from the ROW, not from the module.**

| module | the row supplies | actor case | actorless case |
|---|---|---|---|
| `fa.gate` | the **iteration domain** | `posts(faction, tier)` — part 1 §1's loop, verbatim | `targets(row.scope)` |
| `fa.resolve` | the **pool source** | `attr[a] + attr[b] + POOL_BASE` | `hazard_pool`, published on the row |
| `fa.select` | the **ordering source** | softmax over `appeal` (O-5.9) | declared priority, plus G-1 |

**⚠ `hazard_pool` inherits §6's reachability bar — the one constraint the merge would otherwise have
dropped.** §6 requires the weakest reachable actor to produce a pool inside the calibrated band (6 at
`attr = 1,1`). Nothing in `11`'s schema stops a row declaring `hazard_pool: 2`, which rolls outside the
band the continuous engine is calibrated for — the *looks-live-and-is-dead* class this page shipped the
commensurability finding about. **So: `6 ≤ hazard_pool ≤ 18`, checked at load, with
`ob_site.pool_min = pool_max = hazard_pool` so the existing per-site gate evaluates it and no new field
is needed.** `11`'s declared 8 and 10 satisfy it; the bar is for rows nobody has written yet.

**G-1 lands in `fa.select`, scoped by `remit_kinds: []`: a second ORDERING, not a second module.**
`11 §3.1` is right that the softmax cannot be reused — a drought has no ethos, so there is no `appeal`
to rank. But the *object* is the same: **rank the eligible set by a declared ordering, take one, drop
the rest this pass.** Only the key (post vs target) and the ordering source (softmax vs priority) vary.
A second module for a second ordering rebuilds the dispatcher the merge deleted.

```
for target in targets(row.scope):                    # fa.gate's domain
    eligible = [remit_kinds==[] rows whose gate holds here, minus `excludes` losers]
    for row in eligible, by declared priority, ties broken by
              H(campaign_seed ‖ accounting_index ‖ target_id):     # 10 §6.4's substream
        if fa.resolve(row, target) != Failure: break  # G-1: target leaves this pass. 11 §3.1
```

**Deterministic where the actor path draws, deliberately.** O-5.9 restored the draw on a *provenance*
argument — the ratified engine draws for faction actions (`faction_action.py:251`) — and there is no
such precedent for hazards, nor a design reason: a person chooses, weather does not prefer. Only the
**tie-break** draws, ties inside one band being arbitrary.

**⚠ Its own reachability bar, because a fixed priority order is the defect O-5.9 just prosecuted.** A
declared order over a perpetually-eligible set is a fork that never forks. What saves it is temporal,
not structural — `cooldown` and gate predicates move the eligible set season to season — so the bar is
stated rather than assumed: **every declared actorless row must fire at least once across a controlled
campaign pair on `tools/balance_oracle.py`.** A row that never wins its band is unreachable content,
and the fix is the order, not the row.

**The naming call `11 §2` handed here: ONE set of names, no alias table.** Two names for one field is
the `evacuate`/`retire` failure `CLAUDE.md §4` records, and an alias table institutionalises it. So
`event:` → **`action:`**, `resilience:` → **`ob_site:`** (`target_score` → `target`, `M_max` →
`ob_modifier_max`, per `00 §7`'s exact names), `deposits:` → **`effects:`** — **plus one `11` did not
raise: `triggers:` → `gate:`**, the word `00 §7`'s resolver table and `01 §2.2`'s transition rows
already use for this predicate. `family`, `origin`, `scope`, `cooldown`, `excludes`, `durability_bp`,
`identity_touch_bp`, `mandatory` and `follow_on` are **kept unrenamed**: they answer questions an
actor's row never asks, so they are additive, not duplicative.

**Not over-claimed:** `world.event_fired` is still P0-1-blocked exactly as `entity.created` is (§10.3
item 5) — one Key-type registration, three callers — and `11 §3.3`'s shared 64-emission ceiling is
untouched: this page adds no emitter and removes two.

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

**The pool arithmetic, because P-v turns on it.** Attributes are 1–7, so `attr[a] + attr[b]` spans
2–14. With `POOL_BASE = 4` — **a shape proposal, declared in the exported params with this
justification attached** — the pool spans **6–18**, inside the band the continuous engine is calibrated
for at both ends. Reachability bar: *the weakest actor on the least-suited pair must still produce a
pool inside the band.* At `attr = 1,1` that is pool 6 — satisfied, and §5.6 extends the same bar to
`hazard_pool`.

**This is also why the pool is one person's score and never an aggregate over a roster.** A
roster-sized pool grows `μ` linearly in size while `σ` grows only as `√size`, so `z` grows without
ceiling and the roll becomes decorative for a large faction, on a different engine than a small one.
**The roster buys actions; it never buys dice** — part 1 §2.4 from a different direction. An actorless
row's `hazard_pool` is bounded to the same band for the same reason (§5.6).

---

## 7. Two constraints binding on every effects table

- **Total over the four bands.** Every action declares an outcome for all four, and **no effect is
  unique to Partial** (P0-3), so a change to the Partial band's width degrades the ladder gracefully
  rather than deleting a mechanic.
- **No Failure branch removes a post or eliminates a faction.** Failure deposits, writes tags and costs
  the budget point. Elimination is only ever the gate closing for want of a candidate, recoverable by
  producing one (§1.2). An irreversible outcome on a routinely-reached roll is what P-iv exists to
  catch, **and a faction takes one of these every season, at every rung** — the per-tier gate makes this
  *more* load-bearing than in v1, not less, since a single irreversible branch would fire sooner.

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
| `fa.gate`'s `consumes: [post.vacant]` | **no** — it becomes a boundary read of `holder_id`, which §8.1 says it already is in substance. **One line of contract, no design change** |
| everything else here — `appeal`, the budget, `act.contest_influence`, `act.charter`'s tag gate, the actorless rows' gates (§5.6), every effects table | **yes**, all boundary state reads |
| the emission side (`faction.action_declined`, and the rows' own emissions through the herald) | **yes** as a log |

**This page is nearly robust to J-O**, deliberately: the per-tier gate was written as a *state read*
rather than a *Key reaction* because §8.1 says the transport for the latter does not exist. One
constraint doing two jobs.

---

## 9. Module contracts

Shape per `00 §7`. Per W-6 every `consumes:` row names what the consumer does with the Key; none is
speculative. **Three fields below (`iteration_domain`, `pool_source`, `ordering_source`) and
`fa.charter`'s `generates:` are not in that schema yet** — declared rather than hidden, §10.4.

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
  iteration_domain: posts(faction, tier) | targets(row.scope)   # NEW (v3), O-5.13 -- the ROW selects
                                                        # it, via `remit_kinds`. §5.6. O-5.11: 08's
                                                        # `sm.gate` is this module at one rung.
  disclosure_extra: [{of: gate_inputs, inputs: published, presentation: exact, trigger: hidden}]
                                                        # for remit_kinds: [] rows -- 11 §6's
                                                        # obligation, published predicate never bar
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
  ordering_source:                               # NEW (v3), O-5.13 -- the ROW selects it, via
    actor:     {key: post,   law: softmax, over: appeal, constant: APPEAL_TEMPERATURE,
                substream: H(campaign_seed || accounting_index || post_id)}   # 10 §6.4(3), NOT shared
    actorless: {key: target, law: declared_priority, exclusive: one_fire_per_target_per_season,
                substream: H(campaign_seed || accounting_index || target_id)} # TIE-BREAK ONLY: G-1 is
                                                 # deterministic by design. §5.6, 11 §3.1
                                                 # ⚠ NOT A SCHEMA FIELD (§10.4)
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
  pool_source: attrs + POOL_BASE | hazard_pool          # NEW (v3), O-5.13 -- the ROW selects it, via
                                                        # `remit_kinds`. hazard_pool is bounded to
                                                        # [6,18] by §6's bar, extended. §5.6
  remit: [head, governor, minister, envoy, commander]   # `governor` was ALREADY here, which is what
                                                        # made O-5.11's absorption a no-op: 08's
                                                        # `sm.act` is this module at one rung. §5.5
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  ob_sites: []            # DELIBERATELY EMPTY: a dispatcher has no target of its own. Each ROW
                          # carries its `ob_site` (§5) and 01 §6's gate evaluates rows, not this.
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
  ob_sites:                                      # 01 §6's gate, in 00 §7's EXACT field names.
    - target: presence.<institution>             # CORRECTED v3: the earlier three-field form was this
      shape: DO                                  # page's own invention and omitted the two fields
      pool_min: 6                                # 00 §7 makes MANDATORY for DO/BI -- without them an
      pool_max: 18                               # opposed site is UNEVALUABLE, not passing (01:621).
      pool_opposed_min: 6                        # Pools are §6's attr 1-7 twice + POOL_BASE 4, and
      pool_opposed_max: 18                       # SITE-LOCAL: there is no POOL_MAX in `engine/`.
      ob_modifier_max: 2                         # positive `place_terms` only
      ob_modifier_min: -(presence_ceiling)/2      # the lead term, strictly non-positive (O-5.7).
                                                 # ⚠ SYMBOLIC -- the SECOND field blocked on 07's
                                                 #   undeclared ceiling. ⚠ evaluate on the
                                                 #   DIFFERENTIAL's moments: Ob<=8.247, not 9.783
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
                                          # NEW (v3), O-5.10: WRITABLE, owned by substrate.gauge, so
                                          # it leaves fm.derive's `writable: false` list (06 p2 §9).
    - {name: acceptance.support,  bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure:
    - {of: accrual.entitlement, inputs: published, presentation: exact, trigger: hidden}
    - {of: faction.treasury,    inputs: published, presentation: exact, trigger: hidden}
                                          # exact: a decision input this season, as post.budget is
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
  ob_sites: []            # EMPTY, and NOT because there is no site: the target is row-declared and,
                          # for some rows, absent (§5.3). A row with a target declares its own site;
                          # a row without one does not roll. One target here would fabricate it.
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
  remit: [head, minister, governor, commander, envoy]   # any seated office; the GATE narrows, not
                                                 # the remit -- a schism can be led from any chair
  budget: {gauge: post.budget, cost: 1}
  consumes: []                                   # reads the founding_claim TAG at the boundary, not a
                                                 # Key in flight (§8.1). Survives J-O unchanged.
  ob_sites: []                                   # a gate does not roll
  emits: [{type: entity.created, terminal: false}]     # ⚠ P0-1 BLOCKS THIS: `entity.created` is not
                                                 # a registered Key type. `act.muster` needs the same
                                                 # one (12 §2.1) -- one registration, two callers.
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}   # members' posts re-principal
    - {name: tag,  bucket: tag,  writable: true, owner: substrate.ledger} # Precedent on the parent
    - {name: faction.treasury, bucket: gauge, writable: true, owner: substrate.gauge}  # opens at floor
  form: []                                       # it CREATES an entity; it transitions none
  transitions: []
  generates: [{entity_kind: faction, identity: [ethos, seat_node, charter_season], form: [posture]}]
                                                 # ⚠ NOT A SCHEMA FIELD either -- creation is
                                                 # generation (00 §4.1 P-1), not a fifth write leaf,
                                                 # and the schema cannot say so. §10.4.
  disclosure:
    - {of: founding_claim, inputs: published, presentation: exact, trigger: hidden}
    - {of: ethos,          inputs: published, presentation: exact, trigger: hidden}   # 01 §1.1: identity
```

**⚠ CORRECTED (v3): the claim that stood here — *"no module here declares `form:` or `transitions:`"*
— is no longer true.** Absorbing `sm.act` (O-5.11) brings its facility-tier advance rows, so
`fa.resolve` declares `form: [{place, facilities}]` and a named `transitions:` list. **The property it
protected still holds:** per W-5 a module **names** a transition, the herald applies it, and it may only
name a row it declares — `01 §2.4`'s "grep over one field", over one more field. Presence crossings stay
`07`'s, posture `06`'s, appointment `04`'s; `fa.charter` **creates** without transitioning. A faction
action deposits, tags, spends, names — and in exactly one row, generates.

---

## 10. Property audit

**Scope, honestly.** `fa.gate`, `fa.muster` and `fa.charter` are **gates**; `fa.select` is a
**derivation with a declared draw** (O-5.9) — it ranks, it does not roll. `00 §10` forbids
manufacturing a NERS verdict for a module that does not roll, so **no N/R/S/E verdict is offered for
those four** — their loops and gates are §10.2. The audit below is of `fa.resolve`,
`fa.contest_influence` and `fa.inquire`, which roll.

### 10.1 The properties, each with the falsifier that would show it wrong

| property | verdict | falsifier |
|---|---|---|
| **P-i** legible odds | **pass on the odds; WEAKENED on selection, which is O-5.9's honest price.** Pool is a named person's two attributes plus a declared constant — or, for an actorless row, a published constant on the row (§5.6); obstacle is the target's score halved; **the DO differential is two published nets minus a published obstacle.** Selection is now a draw over a published ranking at a published temperature, so a player reads the *distribution* and cannot predict the *pick*: less legible than the argmax draft, more so than the ratified engine's unpublished weight vector (`faction_action.py:234-243`), which is the real comparison | A test asserting every rolling module's `disclosure:` publishes `pool` and `obstacle` at `exact`, that `fa.select` publishes every `appeal` term, **and that `APPEAL_TEMPERATURE` is published `exact` while the draw's outcome is not published before the fact**. If any input to a roll, a ranking **or a draw's weight vector** is unpublished, P-i is false |
| **P-ii** uniform leverage | pass, **with one recorded non-uniformity in the correct direction** (§4.1) | A test asserting no module contract declares a `budget:` whose cost is consumed inside a pool or obstacle expression (`01 §5.3`'s falsifier), **plus**: no action row's modifier reaches the roll except through `sigma_leverage.net_boost` **or** `derive_ob`'s declared instance term, and no row declares both for the same quantity. A modifier applied twice through two channels — the defect §4.1's two-channel draft would have shipped — falsifies it |
| **P-iii** bounded, monotonic | pass, **with two loops stated and both gains unmeasured** (§2.3, §4.4) | `01 §5.1`'s declaration-time check — `rest + max_seasonal_accrual/λ ≤ ceiling` — applied to `presence.<institution>` with `act.contest_influence` counted among its depositors. **A controlled campaign pair on `tools/balance_oracle.py` showing presence share diverging without bound falsifies it** |
| **P-iv** graded, recoverable | pass | A test asserting every action row's `effects` map is **total over the four `Degree` members** and that **no `failure` branch revokes a post or removes a faction**. A row with a Partial-only effect, or an empty Failure branch, falsifies it |
| **P-vi** *(new)* **reachable bands** | ⚠ **UNVERIFIABLE for `act.contest_influence`; declared for the rest** | `01 §6`'s obstacle-reachability gate: `derive_ob(S_max, M_max) + 3 ≤ 0.4·N_max + z·0.8·√N_max`, `z = 1.645`, **per site**, evaluated for a DO site on the differential's moments (§4.1a). **The site's declaration was itself wrong until v3** — it carried three fields of this page's own invention (`target`/`modifier_max`/`pool_max`) where `00 §7` and `01:621` require seven, and **an opposed site missing `pool_opposed_*` is unevaluable rather than passing**, so the row was mis-declaring the very failure class it reports. Corrected at §9. The test that would show this site wrong: **assert the top band is reachable at the site's most favourable configuration** — at `N_c = 18` against `N_d = 6` the envelope is `11.247`, so `derive_ob(presence_ceiling, 2) ≤ 8.247`, which requires `presence.<institution>`'s ceiling `≤ 12`. **It cannot be run today**: that ceiling is `07`'s and is undeclared, and an undeclared ceiling is not a passing one. The worked failure the gate exists to catch is real and in this tree — a 0–100 gauge yields `P(Overwhelming) = 0` |
| **P-v** right engine | pass, **with one declared gap in `00 §7`'s taxonomy rather than a mislabel** | Affordability, eligibility and **chartering** are `gates` (§5.4 argues why a charter must not re-roll uncertainty already spent); contested outcomes are `d_sigma` at pools 6–18; `appeal` is a `derivation` that writes nothing. **The fourth question — *which of several good options does this person take?* — is a choice under declared uncertainty, and `00 §7` has no resolver kind for it.** `fa.select` keeps `derivation` (correct on the rule as written) and declares its `draw:` explicitly; the gap is reported, not papered over. **A test asserting every `resolver:` matches `00 §7`'s table**, that nothing determinate rolls, and that **every module declaring a `draw:` also declares a substream** — a draw on a shared sequential stream falsifies it, and `10 part 2 §10` row 4 is the executable form |

**N** — under ED-IN-0201 this is the layer the ruling is *about*. No roll here is redundant: every
`d_sigma` module resolves something genuinely uncertain and everything determinate is a `gate`. **R** —
the extremes are the weakest actor (pool 6, in band), the largest faction (flat ceiling; pool unchanged,
pools being person-scale at every rung) and the mildest hazard (`hazard_pool` floored at 6, §5.6).
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
| `fa.select` | derivation + draw | `faction.identity.ethos`, holder convictions, world signals, `Leverage` tags; for actorless rows, the declared priority order (§5.6) | `custody_bias` clamped to `±RELATION_SHARE_MAX · structural_range`; every other term is a bounded projection |
| `fa.muster` | gate | `accrual.entitlement`, `faction.treasury` (a **stock**, O-5.10), `acceptance.support` band | the entitlement accrual rate is a property of the place; the treasury is a decaying gauge bounded at `rest + a/λ` and floored at 0; the revolt gate is a hard floor |
| `fa.charter` | gate | the `founding_claim` Tag, `bloc.state`, the invoking post's membership | **the bound is upstream and already exists** — `06 §3.2`'s formation gate and `θ_coherence`. A charter adds no loop of its own; if it did, it would be the one term on this page with no external damper |
| the budget | derivation over gauges | `post.budget` per held post | `FACTION_ACTION_CEILING`, flat and non-scaling (§2.2), **with a stated reachability bar** |

### 10.3 The four claims across both parts that are weakest, named rather than buried

1. **`FACTION_ACTION_CEILING`, `POOL_BASE`, `SHORTLIST_K`, `APPEAL_TEMPERATURE`, `d₁…d₃` and `e₁…e₂` are
   shape proposals, not ledger constants.** None is cited to a `PP-NNN` or an `ED-NNN`, because none has
   one. They are declared with justifications and reachability bars so that tuning them is an act with a
   named target, not a preference.
2. **Both loops' per-cycle gains are unmeasured** (§2.3, §4.4) and stated so. They are campaign-reachable,
   so the instrument exists; running it with a control is work this page does not do.
3. **The DO-plus-lead-obstacle shape is the page's most contestable design call** (§4.1). It is argued,
   listed at O-5.4 and O-5.7, and each half is *reversible in one line*: dropping `net_d` returns the
   SO the delta spec named, dropping the negative instance term returns the absolute-presence obstacle,
   with every other part of the action unchanged either way.
4. **`act.contest_influence` depends on a gauge ceiling that does not exist yet, and the dependency is
   now exact.** `01 §6`'s gate is built and this site declares six of its seven fields; the seventh,
   `presence.<institution>`'s ceiling, is `07`'s and is undeclared. The constraint handed to `07` is
   **`ceiling ≤ 12`** (§4.1a). Until it lands the site is **unverifiable, not passing** — picking a
   ceiling here would be the confounded measurement `CLAUDE.md §0.1` was written about. **This page's own first form of that gate
   was wrong** (2.57× too permissive at pool 5), **and its own declaration of the site was wrong twice
   over** (three fields where seven are required, §9) — which is the strongest argument available that
   the check belongs at one owner and not restated per document.
5. **`act.charter` creates an entity, and creation has no home in the contract schema** (§5.4). It is
   licensed by `00 §4.1`'s P-1 (*"created at load or by generation"*) and precedented on this same page
   by `act.muster` producing a `unit` (`12 §2.1`), so the *design* is not novel — but `00 §7`'s `state:`
   buckets are `entity|gauge|tag|post` with no way to say *"and one of these comes into being"*, and
   `entity.created` is **not a registered Key type**, so **P0-1 blocks the emission.** One registration
   serves two callers. Declared as a dependency rather than assumed away.
6. **`APPEAL_TEMPERATURE` and the actorless priority order are the two shape proposals here with no
   reachability evidence at all.** Both have two-sided bars (part 1 §3.5, §5.6) and **no measurement**;
   both are campaign-reachable, so `tools/balance_oracle.py` with a control is the instrument. A `T`
   picked to look reasonable and never measured is the decorative-threshold failure §2.2 refuses for
   the ceiling — refusing it there and accepting it here would be asymmetric skepticism, not a
   standard.

### 10.4 Dependencies this page declares and does not own

Named here so none is lost at a document boundary — the posture §4.1a already takes with `07`'s ceiling.

| owed by | what | why it blocks something here |
|---|---|---|
| `01 §2.1` | the **aggregate-vs-stock** sentence | O-5.10 and §5.2a cite it. Without it the mislabel that put `writable: false` on a spent treasury recurs — and it recurred once already |
| `01 §5.2` | declare **`treasury`** (faction, stock) and **`information`** (target, **0–5**) in the gauge roster | **neither is in the roster today**, and `fa.muster`/`fa.inquire` each write one. An undeclared gauge escapes `01 §5.1`'s declaration-time bound check — the only bound `information` has |
| `06 part 2 §9` | drop `faction.treasury` from `fm.derive`'s `state:` list | `writable: false` there, writable here. **Two owners for one gauge is worse than the original defect** — same merge as O-5.10 |
| `07` | `presence.<institution>`'s **ceiling ≤ 12** | §4.1a. Now blocks **two** fields of one `ob_sites` row — `target`'s divisor and `ob_modifier_min` |
| `12` | the consequence of **unpaid upkeep** on a unit | §5.2a. Otherwise the treasury floor is the only brake on a standing army, and it brakes the wrong end |
| `11` | §5.6's **four renames** (`event:`→`action:`, `resilience:`→`ob_site:`, `deposits:`→`effects:`, `triggers:`→`gate:`) and the **`6 ≤ hazard_pool ≤ 18`** bar | one schema, or an alias table — and an alias table is two names for one field. The band bar is the constraint the merge would otherwise have dropped |
| `00 §7` | a schema home for **`ordering_source:`**, **`iteration_domain:`**, **`pool_source:`** and for **generation** | §9 declares all four in fields the schema lacks. One gap, not four: the contract says what a module *reads and writes*, never what it *chooses*, *iterates* or *brings into being* |

**And one thing this page was asked to add and REFUSES to add.** `12:544` bills *"whether to order a
unit field ↔ garrison"* to *"one of the existing strategic action-family invocations (`05`)"*. **No such
family exists here, and none should be added.** `12`'s own `ad.unit` contract (`:486-499`) already
declares `remit: [commander]`, `budget: {gauge: post.budget, cost: 1}`, `form: [{unit, assignment}]` and
`transitions: [unit.field_to_garrison, unit.garrison_to_field]` — **the executor already exists in `12`;
what is wrong is the sentence pointing away from it.** Minting an `act.*` family to satisfy a
cross-reference would create a second invoker of one transition pair, which is the shape-divergence
defect, to fix a typo. **The one-line correction belongs in `12:544`**, and meanwhile nothing is
blocked: `fa.gate` counts `ad.unit` in `action_modules` (part 1 §1), so a commander-only faction acts.
