# 01 (part 2) — Substrate: the obstacle owner, edges, disclosure, and the seams

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md)

**Reading order:** [00 Index](00_INDEX.md) → [01 · the stored primitives](01_substrate_primitives.md) →
**01 part 2 · the extensions and seams** → [02 Character Generation](02_character_generation.md) → …

Part 1 specified the four things that store state, and carries this suite's `## Overrides` block.
This part specifies the two engine extensions that store nothing, the edge registry, the seams by
which everything above reaches the engine, and the substrate's own module contracts. Section
numbering continues from part 1.

## 6. E-1 — `derive_ob`, the obstacle's owner

```python
def derive_ob(target_score: float, modifiers: float = 0.0) -> float:
    """The obstacle. Jordan, 2026-08-14: an obstacle rolled against a character or faction is
    their corresponding score/2 plus whatever specific modifiers exist for them in that instance."""
    return max(OB_MIN, target_score / 2.0 + modifiers)
```

It belongs beside `roll_pool` in `engine/autoload/dice_engine.py`, for a reason the corpus already
measured: the margin ladder is single-owned and guarded (`degree_from_net`), while the obstacle is
derived locally in most resolving subsystems and arrives at the roller as a bare parameter. **Ruling
the obstacle without giving it an owner predicts the same fork recurring**, and there is a measured
precedent in six private roll/degree implementations.

Three properties, each a defect avoided rather than a feature added:

1. **The result is fractional and stays fractional.** The ladder's contract says both operands may be
   fractional; every existing derivation site rounds or floors, against a ladder built to consume
   fractions. Producers correct when written stopped being correct when the ladder moved beneath
   them. A single owner cannot drift that way.
2. **Modifiers are σ-space, not obstacle-space.** A modifier reaches the roll through
   `sigma_leverage.net_boost` — a μ-shift scaled by `σ_N = 0.8·√Pool` — never as a flat addition to
   `derive_ob`'s output. A flat obstacle shift is worth more to a small pool than a large one, the
   same non-uniformity §5.3 rules out one level down. The `modifiers` argument is reserved for terms
   genuinely *properties of the target* — a fortification, a legal protection, **an incumbent's
   presence level** (`05 §4`) — not for the actor's advantages.
3. **The floor is `OB_MIN`**, so an advantage cannot drive the obstacle below the ruled minimum and
   create a cliff at the floor.

**It adds to the engine and repoints nothing.** The three existing obstacle-derivation sites whose
reconciliation is suspended are a different lane's question, and a greenfield module has no ratified
canon to overwrite.

**One leverage note, because it is the obvious objection.** Raising an attribute adds a die, worth
`≈0.204σ` at pool 5 against `≈0.115σ` at pool 18 — so capability investment is worth about 1.8× as
much to a weak actor as a strong one. That is **non-uniform in the correct direction**: self-damping,
and the shape a bounded system wants. It is a property of the continuous engine, recorded here so a
later reader does not mistake it for an unnoticed P-ii defect.

---

## 7. Edges: a shared container with per-kind semantics (change E, redesigned)

### 7.1 The prohibition this section was written against, and the three rulings on disk

`audit/2026-08-08-world-churn-audit/06_master_synthesis.md:552` (Part VI, **HELD not ratified** —
`:4`) prohibits **"a unified bond primitive"**: *"Three anti-unification rulings already on disk. The
real gap is **converters** (marriage-as-treaty, retainer-ripening) and a **shared Key surface**."*

The three, found and read rather than taken on summary:

| # | ruling | what it forbids |
|---|---|---|
| **R-1** | **ED-POL-11** — *"Patronage vs. Knot distinction. **Maintained.** Patronage is political/institutional; Knot is spiritual/personal. Use in separate contexts; **do not conflate**."* (`systems/factions/faction_politics_v30.md:1093`) | treating a Knot as a strong patronage tie, or either as a magnitude of the other |
| **R-2** | **PP-724 §0 Scope** — *"PC-NPC and NPC-NPC ties compose through shared participation in scenes but **do not collapse into one mechanic**."* (`systems/npcs/npc_relational_graph_v30.md:22`) | one mechanic spanning the PC↔NPC and NPC↔NPC layers |
| **R-3** | **PP-724 §3.3** — *"**Knot strain (PC-NPC) and edge strain (NPC-NPC) do not aggregate into one counter** — they are distinct state and resolved separately."* …*"Each relational edge (Knot or NPC-edge) is a **distinct binding**; events that affect a node propagate independently along each binding."* (`:162`, `:167`) | a single strain axis, or a single break rule, across binding kinds |

**All three forbid unifying *semantics*. None forbids sharing *storage*.** That distinction is what
§7.2 is built on, and it is the whole of the argument.

### 7.2 What is cut, and what is adopted — "may the best ideas win"

**v1's six-kind `relation` enum and this suite's own draft eight-kind table are CUT, superseded by
`systems/npcs/npc_relational_graph_v30.md` (PP-724, Class A, PROVISIONAL).** That document already
ships what change E was reaching for, and ships it better: **six canonical NPC↔NPC edge types**, each
with its own formation conditions, strain sources, capacity, break and rupture rules, decay, and
period precedent — plus a decision log arguing the taxonomy's closure on elegance grounds (`:669`).
Re-deriving a worse taxonomy to keep authorship is exactly the failure `00 §1` names.

| adopted from PP-724, cited not restated | `:46-56` |
|---|---|
| `sworn-bond` (symmetric) · `liege-vassal` (liege→vassal) · `kinship` (symmetric; asymmetric parent→child) · `patronage` (patron→client) · `rivalry` (negative valence) · `feud` (negative valence, hereditary) | the six types, strengths 1–3 |
| **kinship does not break by strain**; severance is an institutional act, and the *historical* kinship survives it | `:334-340` |
| **rivalry and feud are escalation tracks, not strain tracks** — they intensify or de-intensify, they do not "fail" | `:674` |
| **NPC↔NPC Disposition is DERIVED from edge state, never stored** — *"storing both edges + Disposition risks divergence"* | `:331-345`, `:675` |

**Two kinds are added, in a scope PP-724 does not cover** (it is explicitly NPC↔NPC only, `:22`):
`treaty` (faction ↔ faction) and `charter` (faction → place). These are *extensions into an
unoccupied scope*, not overrides. `treaty` replaces v1's `Debt`-tag-pair representation, which was
two representations of one relationship while faction enmity was already an edge.

**`client` is not shipped.** Endpoints are ordered, so `patronage(a→b)` read from b's end *is* the
client relation; a `client` row would be a perspective variant, which is `00 §1`'s under-distilled
failure. It is a query helper, never a row. Nothing is lost: every relationship a `client` row could
express is the `patronage` row it duplicates. PP-724 agrees — it ships `patronage` with a direction,
not a pair.

### 7.3 The container, and exactly what it does and does not unify

```
identity(edge)
├── endpoints : (entity_id, entity_id)   ORDERED where the kind is asymmetric
└── relation  : declared in references/form_registry.yaml, ONE ROW PER KIND

form(edge)
└── state     : from the set THIS KIND admits — declared per kind, never globally

gauges        : declared PER KIND. A kind that has no strain axis has no strain gauge.
tags          : what has passed between them, each with provenance — including a treaty's terms
```

| the container supplies | the container does NOT supply |
|---|---|
| an id, so an edge is a tag owner and a Key target like any entity | formation gates — **each kind's are its own** |
| one **provenance** rule and one **disclosure** contract | strain sources — **each kind's are its own, and they never sum** (R-3) |
| one **Key surface** — `edge.formed` / `edge.transitioned` — which is what Part VI says the real gap is | break and rupture rules — **each kind's are its own** |
| one **store**, so `causes[]` chains cross relationship kinds without a join table | a shared strain counter, a shared capacity, or a shared disposition derivation |

**The test the coordinator set: does a shared container make a Knot look like a strong `sworn`
edge?** No, and here is why it cannot.

| | `sworn-bond` (PP-724) | `knot` (canon, §7.4) |
|---|---|---|
| scope | NPC ↔ NPC | PC ↔ NPC — **a different layer** (R-2) |
| formation gate | edge formation conditions, PP-724 §3 | Disposition +5 **and** TS ≥ 30 **and** Bonds ≥ 5 **and** capacity **and** a roll |
| strain counter | edge strain, capacity 3/5/7 by strength | **its own** −5…+5 bond-strain gauge, tiered |
| do the two counters ever sum? | **never** (R-3, `:162`) | **never** |
| disposition | **derived** from edge state (`:331`) | **stored** — canon tracks PC↔NPC Disposition as a live track, and the formation gate reads it at +5 |
| end state | break, or escalate | **rupture**, Thread-structural, irreversible |
| is it in the taxonomy? | yes, type 1 of six | **NO. A Knot is a distinct binding kind and is not a row in PP-724's six.** |

The last two rows are the answer. A kind whose disposition is *stored* while another's is *derived*,
whose strain gauge is a different object with different bounds, and whose end state is a different
transition, is not a magnitude of the other. **The container holds them; it does not equate them.**

⚠ **This corrects a v1 defect, found by taking PP-724 seriously.** v1 put a `disposition` **Gauge on
every edge**. For NPC↔NPC pairs that stores a value PP-724 derives — and deriving it is not merely
PP-724's preference, it is **this suite's own write rule**: a stored NPC↔NPC disposition is an
aggregate over edge strengths, and no aggregate is ever written (§2.1, AU-1). **v1 violated its own
rule and PP-724 caught it.** Disposition is therefore stored for PC↔NPC (canon owns that track) and
derived for NPC↔NPC (`:331-345`). Per-kind semantics, in the substrate, doing real work.

### 7.4 Converters — the gap Part VI actually names

*"The real gap is **converters** (marriage-as-treaty, retainer-ripening)."* Agreed, and it is the one
place this design adds machinery rather than adopting it.

**A converter is a form transition (§2) that CREATES an edge of another kind. It never merges two
kinds and never moves state between them.**

```yaml
converter: marriage_to_treaty
source_kind: kinship            # the marriage edge
creates_kind: treaty            # between the two houses' factions
gate: <both endpoints hold posts in distinct factions AND the kinship edge is cooperative>
source_after: unchanged         # THE SOURCE EDGE PERSISTS. Nothing is consumed.
emits: edge.formed
reversible: false               # a treaty is ended by its own rules, not by un-converting
```

| converter | source | creates | why it is a conversion and not a merge |
|---|---|---|---|
| `marriage_to_treaty` | `kinship` | `treaty` | the kin tie and the treaty then have **separate strain, separate break rules and separate parties**. The marriage surviving a denounced treaty is the interesting case, and only separate objects can express it |
| `retainer_ripening` | `patronage` at sustained strength | `sworn-bond` | PP-724 ships both types with different semantics; ripening is the *transition between them*, which neither type owns |
| `rivalry_to_feud` | `rivalry` | `feud` | PP-724 §2.6 already owns the escalation; the converter names it as one, so it is not re-implemented |

**A converter may not produce a `knot`.** Knot formation is canon's procedure (§7.5) with its own
gates and its own roll. Ripening a patronage into a Knot would be exactly the conflation R-1
forbids.

### 7.5 The Knot — canon, cited, not designed here

**A Knot is not a strong relationship and must not be modelled as one.** It is Thread-constituted:
gated on Thread Sensitivity, carrying its own strain axis, and **rupturing rather than breaking**.
*Knots are constitutive, not contractual.* Everything below is **read from canon and cited**; this
suite designs none of it, invents no number, and adds it to no taxonomy.

| canon fact | value | citation |
|---|---|---|
| formation gate — disposition | Disposition **+5** with the target | `systems/fieldwork/knots_v30.md:68` (§3.1 item 1) |
| formation gate — Thread contact | **either party TS ≥ 30** | `knots_v30.md:69`; scale 0–100 hard cap per `systems/overview/clock_registry_v30.md:72` |
| formation gate — capacity | **current Knot count < `floor(Bonds/2) + 1`** | `knots_v30.md:70`, restated `:31` and `:38` (PP-632) — **this is the canonical cap on Knots per person** |
| formation gate — uniqueness | no existing Knot with this NPC | `knots_v30.md:71` |
| formation gate — Bonds | **PC Bonds ≥ 5** (Bonds is an attribute 1–7; it does *not* cap Disposition) | `knots_v30.md:72` (ED-912); `:28`, `:40` |
| formation roll | **Spirit × 2 + History (Relationships), TN 7, Ob 2** | `knots_v30.md:76` (§3.2) |
| outcome by degree | Overwhelming → Close tier, strain −2 · Success → Distant, strain 0 · Partial → no Knot, Disposition holds +5 · Failure → no Knot, Disposition drops to +4 | `knots_v30.md:78-83` |
| tiers | **Distant** (strain −2…+5, starts 0) · **Close** (strain −5…+5, starts −2) | `knots_v30.md:49-52` (ED-912) |
| rupture threshold | **strain +5, both tiers**, checked at Accounting | `knots_v30.md:54`, `:180` |
| tempered | **strain −5, Close only** — absorbs the next rupture trigger once, then resets to 0 | `knots_v30.md:54`, `:180` |
| strain decay | at Accounting, **−1 if no strain was added that season AND Disposition ≥ +3** | `knots_v30.md:170` |
| strain sources | remote Thread-Read **+1/use** · Composure buffer **+1/use** · counsel re-query **+1** (first free) · FR Lock/Dissolution near a partner **+1** · witnessing a Conviction Scar fire in the partner **+1 at Accounting** · Disposition < +3 for two consecutive seasons **+1 at Accounting** · each opposing-operations event **+1** | `knots_v30.md:160-168` (§5) |
| break consequence | Disposition → **−3** (floor −5) · **both partners take 4 Composure** · all Knot-mediated benefits cease · the capacity slot frees | `knots_v30.md:184-188` |
| **conviction scar** | a **Close** Knot that broke **from positive strain** → **Conviction Scar +1 to both partners** | `knots_v30.md:189` |
| rupture triggers (bypass strain) | public citation of private counsel · partner's death · FR Dissolution targeting the partner (**+1 Wound, no armour**) · permanent Conviction shift to an opposing Conviction · player dissolution at Accounting (**2 Composure**) | `knots_v30.md:193-201` |
| ⚠ **not settled** | mandatory **−1 Coherence on rupture** is flagged **[UNVERIFIED post-ED-912]** — its source PP-632 was struck and ED-912 did not restate it | `knots_v30.md:203`; the sim carries the same warning at `systems/fieldwork/sim/knots.py:53-56` |

**How it lands on the container with no new primitive and no shared semantics:**

| canon element | where it lands |
|---|---|
| the Knot itself | an **edge**, `relation: knot`, **its own registry row**, outside PP-724's six |
| Distant / Close | a `tier` value in the edge's **form**, exactly as a place carries one; the row declares the strain range each tier admits |
| strain | **a Gauge private to this kind**, `λ` chosen so canon's "−1 per quiet season at Disposition ≥ +3" *is* the decay rather than a special case. It never sums with edge strain (R-3) |
| rupture at +5 | a **form transition** `intact → ruptured`, `gate: strain ≥ 5`, `reversible: false` — canon's own irreversibility is why no hysteresis is required |
| tempered at −5 | `intact → tempered`, and `tempered → intact` on absorbing a trigger — **a reversible pair, therefore requiring a declared hysteresis band** (§2.3). Canon states the reset (`:54`) and **states no band**. **v2 records this as a gap and does not fill it** — the band is an FI-lane canon question, not a number this suite may invent |
| the capacity cap | a **gate** reading `floor(Bonds/2) + 1`, counted from the person's `knot` edges — no stored counter |
| conviction scar | a **Tag** on the person, `kind: Precedent`, provenance = the rupture Key; the conviction name resolves through `descriptors.resolve_conviction` and **raises** on an unknown name (§1.2) |
| a Knot's disposition | **stored**, not derived — canon's PC↔NPC Disposition track, read by the formation gate at +5 |

**Q-6 stands open** (`00 §5.1`): nothing here depends on the unverified −1 Coherence rule.

*Emergent possibility lost if the shared container were cut and each kind given its own store:*
`causes[]` could not chain across relationship kinds, so a treaty denounced because of a feud
inherited through a marriage would be three unlinked records — and that chain is the mechanism the
whole suite calls a biography.

---

## 8. E-2 — The disclosure block

There is no GM. Nobody narrates why a candidate was passed over, why a faction declined to act, or
why a place's pressure rose. The only surveyed evidence bearing on that constraint is a game whose
social layer was loved and whose tactical math was resented *in the same title*, separated by nothing
but whether the model was visible — and whose community fix **exposed the models rather than changing
them**.

> **Publish every input. Publish a band, never a number. Never publish the trigger point.**

Asymmetric on purpose. Five independent sources keep the threshold hidden; four say legibility is
what separates a celebrated system from a resented one. Publishing the trigger destroys the mechanic;
publishing the inputs is what makes the outcome feel principled rather than arbitrary.

```yaml
disclosure:
  - of: pressure
    inputs: published          # every deposit and its provenance is inspectable
    presentation: band         # the player sees "strained", not 6.4
    trigger: hidden            # the player is never told the draw threshold
```

**It is a registry field, not documentation.** A state row without a `disclosure:` block fails the
contract check.

**Three v2 consequences.** (1) A **form transition's gate is a trigger**, so its threshold is hidden
while its inputs are published — the player can see every gauge feeding a settlement's growth and
cannot see the number. (2) **A forecast is a trigger published in instalments** (§2.2), which is why
the imminence-Key prohibition and this contract are the same rule seen from two sides. (3) **The
caste gate is the one ruled exception** (`00 §6` principle 5, `04`): it is an *input*, published in
full, because concealing it would make the system's central injustice invisible.

> **Falsifier.** A test asserting every state row carries a disclosure block, none sets
> `trigger: published`, and no emitted key type carries a field whose value is a future state — with
> the caste-gate row as the single declared, named exemption.

---

## 9. The wrapper — a herald that populates `targets[]`, not a distributor

### 9.1 Why this is not the prohibited "world director"

Part VI's strongest negative (`06_master_synthesis.md:551`, **held not ratified**) is *"a distributor
wrapper or 'world director'. Distribution is `targets[]` data plus subscription; a router module is
the god-loop with better PR."* Part III of the same document answers the wrapper-vs-mesh fork and
**refutes both pure forms**, leaving one criterion (`:394`):

> **Aggregate-crossing detection belongs to the aggregator; effect magnitude belongs to the effect's
> owner.**

**This suite adopts that criterion, and the wrapper is reframed to it rather than defended.** Three
assignments follow, and they are what the wrapper is:

1. **The boundary is a herald.** It publishes what it **already computes**. It decides nothing and
   routes nothing. A per-subsystem wrapper is not a central router because there is no central one:
   each wrapper sees only Keys addressed to its own modules, holds no map of other subsystems, and
   cannot reach one — cross-subsystem needs go through `composition.require(role)` (W-2), which is a
   registry lookup, not a dispatch table.
2. **Every effect rule stays local.** Whether a fact scars a person depends on that person's
   convictions; whether a place complies depends on its own acceptance. **The wrapper computes no
   effect magnitude.** It never holds a rule that belongs to a receiver, which is the property that
   separates it from a director.
3. **Distribution is data, not code.** The router a wrapper would centralise **already exists as
   schema** — the five-role `targets[]` vocabulary. **One Key whose `targets[]` names every affected
   place *is* the distribution mechanism.** v1's W-3 was already exactly this; what changes is that
   it is now the wrapper's *definition* rather than one of its rules.

**So the wrapper's whole job is: drain, invoke, and populate `targets[]`.** If a future version of
this document describes it as routing, deciding, or holding a receiver's rule, that version has built
the prohibited thing and this paragraph is the falsifier.

### 9.2 Shape

```
                 engine_clock.run_tick
                          │
        SEASON_TICK ── ACTION ── ACCOUNTING_BOUNDARY
                          │
                    subsystem wrapper          ← resolved by composition role, never imported
                     ├── in:   drain the Keys addressed to this subsystem's modules
                     ├── run:  invoke modules; modules touch primitives and NOTHING else
                     └── out:  publish — at most one Key per resolved module, causes[] cited
                               honestly, targets[] populated at the granularity of each receiver
```

| # | Rule | The failure it prevents |
|---|---|---|
| W-1 | A module never publishes. It returns a result; the wrapper publishes. | Emission scattered across a subsystem is how `causes[]` chains get fabricated or dropped |
| W-2 | A module never imports another subsystem. Cross-subsystem needs resolve through `composition.require(role)`. | The package cycle a function-local import hides from the interpreter without removing |
| W-3 | Fan-out is **one Key with N populated targets, never N Keys** — this *is* the distribution mechanism (§9.1.3). | The re-entrancy meter counts *responses*, not target-array width, so wide legitimate delivery must not look like runaway |
| W-4 | Any Key naming a derived aggregate in `targets[]` carries `stat_deltas: {}` for that target. | Writing an aggregate, which the write rule forbids and the generic per-observer path would do silently |
| **W-5** *(v2)* | A module's result may name a form transition; the wrapper applies it and publishes `form.transitioned`. A module never mutates `form` itself. | Otherwise the fourth write leaf is the one leaf with no single owner, and §2.4's "grep over one field" stops being true |
| **W-6** *(v2)* | **A subscription with no rule content is not declared.** A `consumes:` row must name what the consumer *does* with the Key. | Part VI `:412` — *"a subscription with no rule content is decoration"*. It is also how a `consumes:` list becomes a fiction nobody executes |

**Populating `targets[]` is where granularity increases.** A peninsula-scale Key addressed to eight
places carries eight `targets[]` entries, each with the deltas *that place* receives — not one delta
the receiver must interpret. A sparse `targets[]` delivers blind, the documented failure of the eight
declared down-seams that populate nothing.

⚠ **The double-count hazard is open and this suite does not resolve it** (`00` Q-5). Every wrapper
here declares, per emission, **which of its two channels carries the magnitude — and never both.**

### 9.3 ⚠ The substrate supplies NO LATENCY — binding on everything downstream

Verified against the tree by that audit's adversarial review and **filed as open ruling J-N**
(`06_master_synthesis.md:532`, `:637`):

- `schedule_emission` increments depth **only when already draining**; `drain_tick` has **zero
  production callers**; the live loop calls `accounting_boundary()` then `next_tick()` directly.
- `next_tick` **raises `TerminationBreach` if the queue is non-empty** — there is **no cross-season
  carry**.
- `DEFAULT_CASCADE_DEPTH_MAX = 0` is a **provisional safety bound**, self-labelled, sized to the
  single current emitter.

> **The guard prevents cascades outright; it does not schedule them late.** One-hop-per-season
> latency is **not a property this design has** — it is a mechanism someone would have to build.

**What that forbids, on this page and every page after it:**

| forbidden | the correct shape |
|---|---|
| a module reacting to a Key by publishing a Key that **lands next season** | there is no such transport |
| a form transition, project or event designed as "posted to, fires later" | it **reads state at the boundary** and fires because the world *is* a certain way |
| describing the wrapper as providing propagation over time | it propagates **within a tick**, and nothing else |

**Anything that spans seasons does so by reading state, never by carrying an emission.** That is why
every gauge decays on a *pure function of elapsed time* (§5.1) and why every form gate reads current
state (§2.2): those are the only two cross-season channels the substrate actually has. **J-N is the
ruling that would change this**, and if it rules for reactive chains, this section is what to revisit.

### 9.4 ⚠ This page leans on Key consumption — J-O

`06_master_synthesis.md:533` files **J-O**: *does the Key mesh deserve promotion from telemetry spine
to churn engine at all*, the alternative being **Keys as an append-only telemetry and causality log,
with churn driven at the boundary directly**. The audit records that the alternative *"is never
weighed anywhere"*, and that J-O can invalidate a whole programme rather than one item.

**Stated so the affected parts are identifiable if J-O rules the other way:**

| what depends on Key **consumption** | survives J-O ruling "telemetry only"? |
|---|---|
| `consumes:` rows in every module contract; the wrapper's `in:` drain (§9.2) | **no** — these become boundary reads |
| `causes[]` as the provenance chain, and `Tag.provenance` pointing at a Key | **yes** — that is telemetry and causality, which is what the alternative keeps |
| every **form transition** (§2.2) — gated on *state*, not on a received Key | **yes** |
| every **gauge** deposit and its decay (§5.1) | **yes** |
| the emission side (`form.transitioned`, `edge.formed`, …) | **yes** as a log; only the *reaction* half is at risk |

**The substrate is therefore robust to J-O and the module wiring is not.** That is worth stating
plainly: four primitives, four write leaves and the decay law would all survive a ruling that
retires the consumer mesh; §12's `consumes:` lists would be rewritten as boundary reads. **J-O is
not resolved here and this suite takes no position on it.**

## 10. What is deliberately not a primitive

| Considered | Verdict | Why |
|---|---|---|
| a separate **Accrual** primitive | folded into Gauge | an accrual is a gauge with a positive rest and a rate; a budget is an accrual with a spender |
| a separate **Standing/rank** primitive | folded into Gauge | a rank ladder is a bounded personal meter with bands; keeping it separate produced nine parallel meters |
| `custodian_id` as a **field on Post** | folded into Tag | §4.2 — a field carries less (no ttl, no provenance, no decay) at the same conceptual cost |
| a **role** string on Person | rejected | §1.4 — `posts` is derived; there is no field to collide in |
| a **Compact** tag family | rejected | a recurring term-limited claim is `Debt(recurs=True, ttl=term)` |
| a **Knot** primitive | rejected | §7.3 — it is an edge with a tier in its form and a strain gauge. A sixth kind of stored thing for one canon mechanic is how a substrate stops being one |
| a **Memory** primitive | rejected; it is a **Tag kind** | §3.1 — the argument for the sixth kind is made there; a primitive would need its own store, sweep and provenance rule, all of which Tag already has |
| a **salience** stored field | rejected | §3.2 — derived at read from `value`, `created_season` and one declared `λ_mem` |
| a **`client`** relation kind | rejected | §7.2 — a reading direction, not a row |
| a **second decay law** | rejected | §3.2, §5.1 — one geometric law, several consumers |
| a **second resolver** | rejected | the only surveyed franchise with two resolution paths is also the only one with a two-decade unfixed divergence, exploited in both directions |
| a **view** primitive | rejected | disclosure stores nothing and resolves nothing; it is a declaration attached to state (E-2), which is what makes it checkable |

---

## 11. What the player actually touches at this layer

**Almost nothing, and that is the design** (`00 §2`). This document is the richest layer in the suite
and the thinnest surface. Everything below is **read-only**; the substrate exposes **zero verbs**.

| what the player touches | how it reaches them | how often |
|---|---|---|
| a gauge's **band** — never its number | `gauge_band`, on a Slate item or a place summary | whenever the item they chose is on screen |
| the **posts they hold**, their remit and their remaining **budget** — disclosed `exact`, because these are inputs to a decision they are making now | the post list | once a season |
| a tag's **existence and provenance** — *why did this actor turn on me* | inspection from a Slate item | on demand, never pushed |

| what the player never touches |
|---|
| creating, editing or deleting an **entity**, an **edge** or a **bloc** |
| firing a **form transition** — every one is a gate the engine evaluates |
| appending a **tag** or depositing into a **gauge** directly |
| a gauge's exact **value**, or any transition's **threshold** (§8) |
| **strain**, **salience**, **divergence**, **presence levels** — substrate, surfaced only as a situation |

**Substrate objects on this page: 6 entity kinds, 6 tag kinds, 8 relation kinds, 4 primitives,
2 extensions. Surface affordances: 3 reads, 0 verbs.** If a later document's surface table is longer
than its substrate table, that document has the ratio backwards.

---

## 12. Module contracts — the substrate's own

```yaml
- module: substrate.entity
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation
  remit: []                      # not invocable; a store
  budget: null
  consumes: []
  emits: [{type: person.generated, terminal: false}]
  state:
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
  form: []                       # the store declares the buckets; it transitions nothing
  transitions: []
  disclosure:
    - {of: entity, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.form
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: gate                 # every transition is a gate; §2.2
  remit: []                      # invoked by the wrapper (W-5), never by a post
  budget: null
  consumes: []
  emits: [{type: form.transitioned, terminal: false}]
  state:
    - {name: form, bucket: entity, writable: true, owner: substrate.form}
  form:
    - {entity_kind: person, field: life_stage}
    - {entity_kind: person, field: capability}
    - {entity_kind: person, field: traits}
    - {entity_kind: place,  field: kind}
    - {entity_kind: place,  field: tier}
    - {entity_kind: place,  field: facilities}
    - {entity_kind: place,  field: presences}
    - {entity_kind: faction, field: posture}
    - {entity_kind: edge,   field: state}
    - {entity_kind: edge,   field: tier}       # Knot Distant/Close; §7.3
    - {entity_kind: unit,   field: unit_kind}
    - {entity_kind: unit,   field: assignment}
    - {entity_kind: bloc,   field: members}
    - {entity_kind: bloc,   field: state}
  transitions: [ALL declared rows in references/form_registry.yaml]
  disclosure:
    - {of: form, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.ledger
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  form: []
  transitions: []
  disclosure:
    - {of: tag, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.edge
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: edge.formed, terminal: false}
    - {type: edge.transitioned, terminal: false}
  state:
    - {name: edge.disposition, bucket: gauge, writable: true, owner: substrate.edge}
    - {name: edge.strain,      bucket: gauge, writable: true, owner: substrate.edge}
  form:
    - {entity_kind: edge, field: state}
  transitions: [edge.strain_to_ruptured, edge.strain_to_tempered, edge.tempered_to_intact]
  disclosure:
    - {of: edge.disposition, inputs: published, presentation: band, trigger: hidden}
    - {of: edge.strain,      inputs: published, presentation: band, trigger: hidden}

- module: substrate.post
  parent: substrate
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: post.granted, terminal: false}
    - {type: post.revoked, terminal: false}
    - {type: post.vacant,  terminal: false}
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: post.budget, bucket: gauge, writable: true, owner: substrate.post}
  form: []
  transitions: []
  disclosure:
    - {of: post, inputs: published, presentation: exact, trigger: hidden}
    - {of: post.budget, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.gauge
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: accrual
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure:
    - {of: gauge, inputs: published, presentation: band, trigger: hidden}
```

`substrate.post` and `substrate.gauge`'s **post** rows disclose **exact**, not band: a post's holder
and a budget's remaining points are things the player acts on directly this season, and hiding them
would obscure an input rather than a threshold. Bands are for values whose precise magnitude is not a
decision the player makes.

---

## 13. Property audit

**Scope, and the honest limit.** **Nothing in this document rolls.** `substrate.entity`,
`substrate.ledger` and `substrate.gauge` are stores; `substrate.form` and `substrate.edge` are gates;
`derive_ob` is a derivation *consumed by* rollers elsewhere and is not itself a resolution. **No
N/R/S/E verdict is offered for a store or a gate** — manufacturing one for state with no draw is the
error the methodology explicitly names, and v1 was right to refuse it. What is offered instead is the
two properties that *do* apply, plus every loop and gate stated with its bound.

Above that sits `00 §0.1`: **a resolution-scoped audit cannot ask whether a design expresses the
game.** This page could pass every property below and still be the wrong substrate. The instrument
for that question is §1's elegance criterion, and its answers here are the one-line loss statements
and the §10 cut list — judgments, not checks.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass, and it is the strongest claim in the suite** | every gauge is bounded by declared floor and ceiling and restores geometrically, so the fixed point `rest + a/λ` is finite for every bounded accrual and every `λ ∈ (0,1]`. Checked **at load time** against the registry with no campaign run (§5.1). Monotone response is structural: more deposit is never less value. Form is bounded because every form field's value set is enumerated in the registry |
| **P-v** right engine | **pass** | four resolvers, and every module here is `gate`, `accrual` or `derivation`. Nothing on this page is uncertain and nothing on this page rolls. **Every form transition is a gate on purpose** (§2.2): the uncertainty was in getting the gauges to the threshold, and re-rolling at the threshold charges for it twice |

### 13.1 Loops, each with its bound

| loop | sign | bound | gain |
|---|---|---|---|
| gauge deposit → band → module gating → deposit | positive | the fixed point `rest + a/λ`, checked at declaration (§5.1) | **unmeasured**; campaign-reachable, so measurable with a control, and it should be measured before any writer lands |
| form transition ↔ its reverse | oscillatory | **`θ↑ − θ↓ ≥ H_MIN` plus `dwell ≥ D`, checked at load (§2.3)** | **bounded arithmetically** — the only loop on this page with a proved bound, and the reason hysteresis is mandatory rather than advised |
| edge strain → rupture → conviction scar → conviction weight → behaviour → strain | positive | **terminating**: rupture is `reversible: false`, so the edge leaves the loop permanently. Strain is gauge-bounded per tier (canon: −5…+5) | **unmeasured**, and it is canon's loop, not this suite's — `07`/`12` inherit the measurement obligation |
| memory salience → weighting → behaviour → new perception → memory | positive | **`MEMORY_CAP` top-K at the sweep, plus geometric salience decay, plus `RELATION_SHARE_MAX`** (§3.2, §3.4) | **unmeasured**. Three independent bounds is not the same as a measured gain, and this page does not claim it is |
| tag append → selection → outcome → tag append | positive | dedupe on `(owner, kind, key)` bounds count by `candidates × posts`; magnitude bounded by the gauge the value deposits into (§3.3) | **unmeasured** |

### 13.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| tag provenance non-empty | the append call | a refusal at append time |
| form transition gate | gauges, tags, form, identity — **never a roll** | no transition; the entity stays as it is |
| hysteresis band | the registry, at load | **load failure**, not a runtime surprise |
| vacancy (`holder_id is None`) | the post | the faction does not act at that tier (`05 §1`) |
| `remit` | the post's remit list | the module is not in the option set — not a penalty, an absence |
| Knot capacity `< floor(Bonds/2) + 1` | the person's `knot` edges (derived, no counter) | formation is unavailable (`knots_v30.md:70`) |
| disclosure block present | the registry, at contract check | the contract check fails |

### 13.3 The four qualitative verdicts, applied to the substrate rather than to a resolver

**Necessary** — four primitives, six entity kinds, six tag kinds, eight relation kinds. Each entity
kind has at least one module that reads it and one that writes a bucket of it; §10 records six
candidates refused, including two the v2 spec named. **Robust** — the two failure directions the
corpus measured are closed by arithmetic: an unrecoverable pinned gauge by the geometric law, and a
flickering threshold by the hysteresis band. Both are load-time checks. **Smooth** — one decay law,
one obstacle owner, one disclosure contract, one write rule with four leaves, one registry for the
mutable-shape axis. **Elegant** — six modules, one new registry from this page, no branch on any
entity's identity anywhere, and a player surface of three reads and zero verbs.
