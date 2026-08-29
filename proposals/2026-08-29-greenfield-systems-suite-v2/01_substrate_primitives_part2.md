# 01 (part 2) — Substrate: edges, disclosure, the herald, the contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`01_substrate_primitives.md`](01_substrate_primitives.md) — **part 1 first; this continues it**
## Part 1: §§1–6 (the four primitives, form transitions, `derive_ob` and its commensurability gate)
## Part 2: §§7–13 (edges and the Knot, disclosure, the herald, the surface, the contracts, the audit)

Section numbering continues from part 1 without a break, and every `§n` cross-reference resolves across
both parts. Split under `CLAUDE.md` §4's sequential-parts rule (`_part2` in reading order, never
index+infill) because the single file exceeded the 15k-token compliance cap.

**Everything in this part is `substrate`** in the sense of `00 §2.1`. §11 is the whole player-facing
surface of both parts, and it is three read-only affordances and zero verbs.

---

## 7. Edges: a shared container with per-kind semantics (change E, redesigned)

### 7.1 The prohibition, and the three rulings on disk

`audit/2026-08-08-world-churn-audit/06_master_synthesis.md:552` (Part VI, **HELD not ratified** —
`:4`) prohibits **"a unified bond primitive"**: *"Three anti-unification rulings already on disk. The
real gap is **converters** (marriage-as-treaty, retainer-ripening) and a **shared Key surface**."*
The three, found and read rather than taken on summary:

| # | ruling | what it forbids |
|---|---|---|
| **R-1** | **ED-POL-11** — *"Patronage vs. Knot distinction. **Maintained.** Patronage is political/institutional; Knot is spiritual/personal. Use in separate contexts; **do not conflate**."* (`systems/factions/faction_politics_v30.md:1093`) | treating a Knot as a strong patronage tie, or either as a magnitude of the other |
| **R-2** | **PP-724 §0** — *"PC-NPC and NPC-NPC ties compose through shared participation in scenes but **do not collapse into one mechanic**."* (`systems/npcs/npc_relational_graph_v30.md:18`) | one mechanic spanning the PC↔NPC and NPC↔NPC layers |
| **R-3** | **PP-724 §3.3** — *"**Knot strain (PC-NPC) and edge strain (NPC-NPC) do not aggregate into one counter** — they are distinct state and resolved separately"*; *"each relational edge is a **distinct binding**"* (`:162`, `:167`) | a single strain axis, capacity, or break rule across binding kinds |

**All three forbid unifying *semantics*. None forbids sharing *storage*.** That distinction is the
whole of the argument below.

### 7.2 What is cut, and what is adopted — "may the best ideas win"

**v1's six-kind `relation` enum and this suite's own draft eight-kind table are CUT, superseded by
`systems/npcs/npc_relational_graph_v30.md` (PP-724, Class A, PROVISIONAL).** That document already
ships what change E reached for, and better: **six canonical NPC↔NPC edge types**, each with its own
formation conditions, strain sources, capacity, break and rupture rules, decay and period precedent,
plus a decision log arguing the taxonomy's closure on elegance grounds (`:669`). Re-deriving a worse
taxonomy to keep authorship is the failure `00 §1` names.

**Adopted, cited not restated** (`:46-56`): `sworn-bond` (symmetric) · `liege-vassal` (liege→vassal) ·
`kinship` (symmetric; asymmetric parent→child) · `patronage` (patron→client) · `rivalry` · `feud`
(hereditary), strengths 1–3. With them, three rules that are *per-kind* and stay that way: **kinship
does not break by strain** — severance is an institutional act and the historical kinship survives it
(§3.4, `:169-175`; capacity table `:129`; decision log `:672`); **rivalry and feud are escalation
tracks, not strain tracks** (`:674`); **NPC↔NPC Disposition is DERIVED from edge state, never stored**
(`:331-345`, `:675`).

**Three kinds are added in a scope PP-724 declares out of bounds** (it is NPC↔NPC only, `:18`):
`treaty` (faction ↔ faction), `charter` (faction → place) and **`allegiance` (person → faction)**.
Extensions into empty scope, not overrides. `treaty` replaces v1's `Debt`-tag-pair representation,
which was two representations of one relationship while faction enmity was already an edge.

**`client` is not shipped.** Endpoints are ordered, so `patronage(a→b)` read from b's end *is* the
client relation; a `client` row is a perspective variant — `00 §1`'s under-distilled failure. It is a
query helper. Nothing is lost, and PP-724 agrees: it ships `patronage` with a direction, not a pair.

### 7.2.1 `allegiance` — the person→faction track, and why it is one registry row (O-7)

**What is missing without it.** This suite ships exactly two personal meters, `standing` and `exposure`
(§5.2), both **public/private halves of a person's general position** — neither is *toward* anybody.
`disposition.pc_npc` is stored but is **PC↔NPC only**. So there is **no magnitude anywhere in the suite
for how a person stands toward a faction**, and the distillation that correctly cut *"nine parallel
personal meters"* cut this one with them.

**What that costs, measured rather than asserted.** The world-churn census sorts the register's 81
faction-tier arcs into ~7 recurring families and names the largest: *"faction+NPC personal-track
threshold cascade (~12-15 arcs, the ARC-S07 'Torben Loyalty Clock' shape — **the capstone target itself
is the single most duplicated shape in the corpus**)"*
(`audit/2026-07-05-emergent-narrative-engine/_workings_joined.md:1933-1935`; the 138-arc register and
the ~13-shape collapse at `narrative_engine_design_v2_churn.md:21`, `:80`). The **monotone** subcase of
that family — a loyalty counter that only ever runs down to a coup — is already expressible: it is a
ratcheting project, and `09 §3.2` reproduces canon's monotone clock exactly. The **recoverable,
bidirectional** subcase — a person who is turning and can be turned back, which is most of the family
and the whole reason the shape is interesting — is **not**, because there is nothing to move in either
direction. `09`'s `project_kinds` schema makes every advance term *"a predicate over READABLE STATE"*
— and the readable state this one would need does not exist.

**The fix is one registry row and zero new primitives.** §7.3 already declares edge gauges **per kind**,
so an `allegiance` row simply declares one:

```
relation: allegiance      endpoints: (person → faction), ORDERED       # asymmetric by construction
form(state) : {aligned, wavering, estranged}      # a per-kind state set, like every other kind's
gauges      : allegiance.strength — a STORED gauge, private to this kind, bounded, geometric decay (§5.1)
tags        : the favours, slights and oaths that moved it, each with provenance
```

**Why it is STORED and not derived, in §2.1's vocabulary.** Allegiance is a **stock, not an aggregate**:
it is the accumulated residue of favours granted, slights borne and oaths sworn, and **current state
does not recompute it** — two people holding identical posts under identical ethos, one of whom was
passed over three seasons ago, are in different states and only the history says so. Contrast NPC↔NPC
disposition, which PP-724 derives precisely because it *is* recomputable from the edge graph (§7.3, O-3).
The two verdicts are opposite because the two quantities are different in kind, and §2.1's test is what
separates them.

⚠ **R-1, R-2 and R-3 are untouched, and this is not a courtesy claim.** An `allegiance` edge is
**neither a Knot nor an NPC↔NPC tie.** Its endpoints are a *person and a faction*, so it lies outside
PP-724's declared scope entirely (`:18`) — R-2's PC↔NPC/NPC↔NPC layer distinction does not reach it,
because it is on neither layer. Its gauge is `allegiance.strength`, declared per kind, which **never
sums with edge strain or Knot strain** (R-3) and is not a magnitude of either. And it is
political/institutional, which is exactly the side of ED-POL-11's line **patronage** is on — R-1 forbids
conflating patronage with the Knot, and this row is on the patronage side of that line, not across it.
The three rulings govern person↔person bindings; this is the first person→*institution* binding the
container has held.

**Why an edge and not a person gauge.** A person may stand differently toward four factions at once, so
a gauge on the person would need a key — which is an edge with the naming hidden. The edge also gives
the track a tag owner (the slights that produced it) and puts it in the one store where `causes[]`
chains across binding kinds (§7.3), which is how *"he turned because of what was done to his brother"*
becomes a queryable chain rather than a coincidence.

### 7.3 The container, and exactly what it does and does not unify

```
identity(edge) : endpoints (ORDERED where the kind is asymmetric) · relation (one registry row per kind)
form(edge)     : state — from the set THIS KIND admits, declared per kind, never globally
gauges         : declared PER KIND. A kind with no strain axis has no strain gauge, and a kind
                 whose magnitude is a STOCK (allegiance, §7.2.1) declares a stored one. Never global.
tags           : what has passed between them, with provenance — including a treaty's terms
```

| the container supplies | the container does NOT supply |
|---|---|
| an id, so an edge is a tag owner and a Key target like any entity | formation gates — **each kind's are its own** |
| one **provenance** rule and one **disclosure** contract | strain sources — **each kind's are its own, and they never sum** (R-3) |
| one **Key surface** (`edge.formed` / `edge.transitioned`) — *which is what Part VI says the real gap is* | break and rupture rules — **each kind's are its own** |
| one **store**, so `causes[]` chains cross relationship kinds without a join table | a shared strain counter, capacity, or disposition derivation |

**The test set for this section: does a shared container make a Knot look like a strong `sworn`
edge?** No, and here is why it cannot.

| | `sworn-bond` (PP-724) | `knot` (canon, §7.5) |
|---|---|---|
| scope | NPC ↔ NPC | PC ↔ NPC — **a different layer** (R-2) |
| formation | PP-724 §3 edge conditions | Disposition +5 **and** TS ≥ 30 **and** Bonds ≥ 5 **and** capacity **and** a roll |
| strain | edge strain, capacity 3/5/7 by strength | **its own** −5…+5 tiered bond-strain gauge |
| do the counters ever sum? | **never** (R-3) | **never** |
| disposition | **derived** from edge state (`:331`) | **stored** — canon's PC↔NPC track; the gate reads it at +5 |
| end state | break, or escalate | **rupture** — Thread-structural, irreversible |
| in PP-724's taxonomy? | yes, type 1 of six | **no. A Knot is a distinct binding kind and is not one of the six.** |

The last three rows are the answer. A kind whose disposition is *stored* while another's is
*derived*, whose strain is a different object with different bounds, and whose end state is a
different transition, is not a magnitude of the other. **The container holds them; it does not equate
them.**

⚠ **This corrects a v1 defect, found by taking PP-724 seriously.** v1 put a `disposition` **Gauge on
every edge**. For NPC↔NPC pairs that stores a value PP-724 derives — and deriving it is not merely
PP-724's preference, it is **this suite's own write rule**: a stored NPC↔NPC disposition is an
aggregate over edge strengths, and no aggregate is ever written (§2.1). **v1 violated its own rule and
PP-724 caught it.** Disposition is stored for PC↔NPC, derived for NPC↔NPC, and **allegiance is stored
for person→faction** — three verdicts, each falling out of §2.1's one test rather than out of taste: the
NPC↔NPC value is recomputable from the edge graph, the other two are path-dependent stocks. Per-kind
semantics, in the substrate, doing real work.

### 7.4 Converters — the gap Part VI actually names

**A converter is a form transition (§2) that CREATES an edge of another kind. It never merges two
kinds and never moves state between them.**

```yaml
converter: marriage_to_treaty
source_kind: kinship    creates_kind: treaty
gate: <both endpoints hold posts in distinct factions AND the kinship edge is cooperative>
source_after: unchanged        # THE SOURCE EDGE PERSISTS. Nothing is consumed.
emits: edge.formed             reversible: false
```

| converter | source → creates | why it is a conversion, not a merge |
|---|---|---|
| `marriage_to_treaty` | `kinship` → `treaty` | the two then have **separate strain, separate break rules, separate parties**. The marriage surviving a denounced treaty is the interesting case, and only separate objects express it |
| `retainer_ripening` | `patronage` at sustained strength → `sworn-bond` | PP-724 ships both with different semantics; ripening is the *transition between them*, which neither type owns |
| `rivalry_to_feud` | `rivalry` → `feud` | PP-724 §2.6 owns the escalation; naming it a converter stops it being re-implemented |

**A converter may not produce a `knot`.** Knot formation is canon's procedure with its own gates and
its own roll; ripening a patronage into a Knot is exactly the conflation R-1 forbids.

### 7.5 The Knot — canon, cited, not designed here

**A Knot is not a strong relationship and must not be modelled as one.** It is Thread-constituted:
gated on Thread Sensitivity, carrying its own strain axis, **rupturing rather than breaking**. *Knots
are constitutive, not contractual.* Everything below is read from canon and cited; this suite designs
none of it, invents no number, and adds it to no taxonomy.

| canon fact | value | citation (`systems/fieldwork/knots_v30.md`) |
|---|---|---|
| gate — disposition | Disposition **+5** with the target | `:68` |
| gate — Thread contact | **either party TS ≥ 30**; TS scale 0–100 hard cap | `:69`; `systems/overview/clock_registry_v30.md:72` |
| gate — capacity | **Knot count < `floor(Bonds/2) + 1`** — **the canonical cap on Knots per person** | `:70`, restated `:31`, `:38` (PP-632) |
| gate — uniqueness | no existing Knot with this NPC | `:71` |
| gate — Bonds | **PC Bonds ≥ 5** (attribute 1–7; it does *not* cap Disposition) | `:72` (ED-912); `:28`, `:40` |
| formation roll | **Spirit × 2 + History (Relationships), TN 7, Ob 2** | `:76` |
| outcome by degree | Overwhelming → Close, strain −2 · Success → Distant, strain 0 · Partial → no Knot, Disposition holds +5 · Failure → no Knot, Disposition drops to +4 | `:78-83` |
| tiers | **Distant** (−2…+5, starts 0) · **Close** (−5…+5, starts −2) | `:49-52` (ED-912) |
| rupture threshold | **strain +5, both tiers**, checked at Accounting | `:54`, `:180` |
| tempered | **strain −5, Close only** — absorbs the next rupture trigger once, then resets to 0 | `:54`, `:180` |
| strain decay | at Accounting, **−1 if no strain added that season AND Disposition ≥ +3** | `:170` |
| strain sources | remote Thread-Read **+1/use** · Composure buffer **+1/use** · counsel re-query **+1** (first free) · FR Lock/Dissolution near a partner **+1** · witnessing a Conviction Scar fire in the partner **+1 at Accounting** · Disposition < +3 for two consecutive seasons **+1 at Accounting** · each opposing-operations event **+1** | `:160-168` |
| break consequence | Disposition → **−3** (floor −5) · **both partners take 4 Composure** · all Knot-mediated benefits cease · the capacity slot frees | `:184-188` |
| **conviction scar** | a **Close** Knot that broke **from positive strain** → **Conviction Scar +1 to both partners** | `:189` |
| rupture triggers (bypass strain) | public citation of private counsel · partner's death · FR Dissolution targeting the partner (**+1 Wound, no armour**) · permanent Conviction shift to an opposing Conviction · player dissolution at Accounting (**2 Composure**) | `:193-201` |
| ⚠ **not settled** | mandatory **−1 Coherence on rupture**, flagged **[UNVERIFIED post-ED-912]** — PP-632 was struck and ED-912 did not restate it | `:203`; same warning at `systems/fieldwork/sim/knots.py:53-56` |

**How it lands, with no new primitive and no shared semantics:** the Knot is an **edge** with
`relation: knot` and **its own registry row, outside PP-724's six**; Distant/Close is a `tier` value
in its **form**; strain is **a Gauge private to this kind**, with `λ` chosen so canon's "−1 per quiet
season at Disposition ≥ +3" *is* the decay rather than a special case, and it never sums with edge
strain (R-3); rupture at +5 is a **form transition** `intact → ruptured`, `reversible: false` — canon's
own irreversibility is why no hysteresis is needed; the capacity cap is a **gate** counting the
person's `knot` edges, with no stored counter; the conviction scar is a **Tag** (`kind: Precedent`)
whose conviction name resolves through `descriptors.resolve_conviction` and **raises** on an unknown
name (§1.2).

⚠ **One gap recorded, not filled.** `tempered → intact` on absorbing a trigger is a **reversible
pair**, so §2.3 requires a declared hysteresis band. Canon states the reset (`:54`) and **states no
band**. That is an FI-lane canon question, not a number this suite may invent. **Q-6** (`00 §5.1`)
likewise stands open, and nothing here depends on the unverified −1 Coherence rule.

*Emergent possibility lost if the shared container were cut and each kind given its own store:*
`causes[]` could not chain across relationship kinds, so a treaty denounced because of a feud
inherited through a marriage would be three unlinked records — and that chain is the mechanism the
whole suite calls a biography.
---

## 8. E-2 — The disclosure block

There is no GM. Nobody narrates why a candidate was passed over, why a faction declined to act, or why
a place's pressure rose. The only surveyed evidence bearing on that constraint is a game whose social
layer was loved and whose tactical math was resented *in the same title*, separated by nothing but
whether the model was visible — and whose community fix **exposed the models rather than changing them**.

> **Publish every input. Publish a band, never a number. Never publish the trigger point.**

Asymmetric on purpose. Five independent sources keep the threshold hidden; four say legibility is what
separates a celebrated system from a resented one. Publishing the trigger destroys the mechanic;
publishing the inputs is what makes the outcome feel principled rather than arbitrary.

```yaml
disclosure:
  - {of: pressure, inputs: published, presentation: band, trigger: hidden}
    # every deposit and its provenance inspectable · "strained", not 6.4 · never the draw threshold
```

**It is a registry field, not documentation** — a state row without a `disclosure:` block fails the
contract check. **Three v2 consequences.** (1) A **form transition's gate is a trigger**: its threshold
is hidden while its inputs are published, so the player sees every gauge feeding a settlement's growth
and not the number. (2) **A forecast is a trigger published in instalments** (§2.2), which is why the
imminence-Key prohibition and this contract are one rule seen from two sides. (3) **The caste gate is
the one ruled exception** (`00 §6` principle 5, `04`): an *input*, published in full, because concealing
it would make the system's central injustice invisible.

> **Falsifier.** A test asserting every state row carries a disclosure block, none sets
> `trigger: published`, and no emitted key type carries a field whose value is a **future** state — with
> the caste-gate row as the single declared, named exemption.

---


---

## 9. The herald — one per subsystem, populating `targets[]`

### 9.1 Why this is not the prohibited "world director"

Part VI's strongest negative (`06_master_synthesis.md:551`, **held not ratified**) is *"a distributor
wrapper or 'world director'. Distribution is `targets[]` data plus subscription; a router module is the
god-loop with better PR."* Part III of the same document answers the wrapper-vs-mesh fork and **refutes
both pure forms**, leaving one criterion (`:394`):

> **Aggregate-crossing detection belongs to the aggregator; effect magnitude belongs to the effect's
> owner.**

**This suite adopts that criterion and reframes the wrapper to it rather than defending the wrapper.**

1. **The boundary is a herald.** It publishes what it **already computes**. It decides nothing and
   routes nothing. A per-subsystem herald is not a central router because there is no central one: each
   sees only Keys addressed to its own modules, holds no map of other subsystems, and cannot reach one —
   cross-subsystem needs go through `composition.require(role)` (W-2), a registry lookup, not a dispatch
   table.
2. **Every effect rule stays local.** Whether a fact scars a person depends on that person's convictions;
   whether a place complies depends on its own acceptance. **The herald computes no effect magnitude and
   never holds a rule belonging to a receiver** — the property that separates it from a director.
3. **Distribution is data, not code.** The router a wrapper would centralise **already exists as
   schema**: the five-role `targets[]` vocabulary. **One Key whose `targets[]` names every affected place
   *is* the distribution mechanism.** v1's W-3 was already exactly this; what changes is that it is now
   the herald's *definition* rather than one of its rules.

**So the herald's whole job is: drain, invoke, populate `targets[]`.** If a future version of this
document describes it as routing, deciding, or holding a receiver's rule, that version has built the
prohibited thing, and this paragraph is the falsifier.

### 9.2 Shape and rules

```
engine_clock.run_tick →  SEASON_TICK ── ACTION ── ACCOUNTING_BOUNDARY
   subsystem herald (resolved by composition role, never imported)
     in:   drain the Keys addressed to this subsystem's modules
     run:  invoke modules; modules touch primitives and NOTHING else
     out:  publish at most one Key per resolved module, causes[] cited honestly,
           targets[] populated at the granularity of each receiver
```

| # | Rule | The failure it prevents |
|---|---|---|
| W-1 | A module never publishes. It returns a result; the herald publishes. | Emission scattered across a subsystem is how `causes[]` chains get fabricated or dropped |
| W-2 | A module never imports another subsystem; needs resolve through `composition.require(role)`. | The package cycle a function-local import hides from the interpreter without removing |
| W-3 | Fan-out is **one Key with N populated targets, never N Keys** — this *is* the distribution mechanism. | The re-entrancy meter counts *responses*, not target-array width, so wide legitimate delivery must not look like runaway |
| W-4 | Any Key naming a derived aggregate in `targets[]` carries `stat_deltas: {}` for that target. | Writing an aggregate, which the write rule forbids and the generic per-observer path would do silently |
| **W-5** *(v2)* | A module's result may *name* a form transition; the herald applies it and publishes `form.transitioned`. A module never mutates `form`. | Otherwise the fourth write leaf is the one leaf with no single owner, and §2.4's "grep over one field" stops being true |
| **W-6** *(v2)* | **A subscription with no rule content is not declared.** A `consumes:` row must name what the consumer *does* with the Key. | Part VI `:412` — *"a subscription with no rule content is decoration"*, and it is how a `consumes:` list becomes a fiction nobody executes |

**Populating `targets[]` is where granularity increases.** A peninsula-scale Key addressed to eight
places carries eight entries, each with the deltas *that place* receives — not one delta the receiver
must interpret. A sparse `targets[]` delivers blind, the documented failure of the eight declared
down-seams that populate nothing. ⚠ **The double-count hazard is open** (`00` Q-5): every herald here
declares, per emission, **which of its two channels carries the magnitude — and never both.**

### 9.3 ⚠ The substrate supplies NO LATENCY — binding on everything downstream

Verified against the tree by that audit's adversarial review, **filed as open ruling J-N**
(`06_master_synthesis.md:532`, `:637`): `schedule_emission` increments depth **only when already
draining**; `drain_tick` has **zero production callers**; the live loop calls `accounting_boundary()`
then `next_tick()` directly; **`next_tick` raises `TerminationBreach` if the queue is non-empty**, so
there is **no cross-season carry**; and `DEFAULT_CASCADE_DEPTH_MAX = 0` is a **provisional** safety
bound, self-labelled, sized to the single current emitter.

> **The guard prevents cascades outright; it does not schedule them late.** One-hop-per-season latency
> is **not a property this design has** — it is a mechanism someone would have to build.

| forbidden | the correct shape |
|---|---|
| a module reacting to a Key by publishing a Key that **lands next season** | there is no such transport |
| a transition, project or event designed as "posted to, fires later" | it **reads state at the boundary** and fires because the world *is* a certain way |
| describing the herald as providing propagation over time | it propagates **within a tick**, and nothing else |

**Anything spanning seasons does so by reading state, never by carrying an emission.** That is why every
gauge decays on a *pure function of elapsed time* (§5.1) and every form gate reads current state (§2.2):
those are the only two cross-season channels the substrate actually has. **J-N is the ruling that would
change this**, and if it rules for reactive chains, this section is what to revisit.

### 9.4 ⚠ This page leans on Key consumption — J-O

`06_master_synthesis.md:533` files **J-O**: *does the Key mesh deserve promotion from telemetry spine to
churn engine at all*, the alternative being **Keys as an append-only telemetry and causality log with
churn driven at the boundary directly** — an alternative the audit records as *"never weighed anywhere"*,
and one that can invalidate a whole programme rather than one item. Stated so the affected parts are
identifiable:

| depends on Key **consumption** | survives a "telemetry only" ruling? |
|---|---|
| `consumes:` rows in every module contract; the herald's `in:` drain | **no** — these become boundary reads |
| `causes[]` as the provenance chain, and `Tag.provenance` pointing at a Key | **yes** — that is telemetry and causality, which the alternative keeps |
| every **form transition** (gated on *state*, not on a received Key) and every **gauge** deposit and decay | **yes** |
| the emission side (`form.transitioned`, `edge.formed`, …) | **yes** as a log; only the *reaction* half is at risk |

**The substrate is robust to J-O; the module wiring is not.** Four primitives, four write leaves and the
decay law would all survive a ruling that retires the consumer mesh; §12's `consumes:` lists would be
rewritten as boundary reads. **J-O is not resolved here and this suite takes no position on it.**

---

## 10. What is deliberately not a primitive, and what was cut

A cut list is only credible next to what it refuses to add — and under *"may the best ideas win"* it
must also record what was cut because something on disk beat it.

| Considered | Verdict | Why |
|---|---|---|
| a separate **Accrual** or **Standing/rank** primitive | folded into Gauge | an accrual is a gauge with a positive rest and a rate; a budget is an accrual with a spender; a rank ladder is a bounded meter with bands. Keeping them separate produced nine parallel meters and three rival clocks |
| `custodian_id` as a **field on Post** | folded into Tag | §4.2 — a field carries less (no ttl, no provenance, no decay) at the same conceptual cost |
| a **role** string on Person | rejected | §1.4 — `posts` is derived; there is no field to collide in |
| a **Compact** tag family | rejected | a recurring term-limited claim is `Debt(recurs=True, ttl=term)` |
| a **Knot** primitive | rejected | §7.5 — an edge with its own registry row, its own gates and its own private strain gauge. A sixth stored kind for one canon mechanic is how a substrate stops being one |
| **a v2-invented relation taxonomy** | **CUT, superseded by PP-724** | §7.2. Six period-grounded types with per-type semantics and a decision log already exist on disk. Rebuilding a worse one to keep authorship is the elegance failure, whoever wrote it |
| a **`client`** relation kind | rejected | §7.2 — a reading direction, not a row |
| a **stored NPC↔NPC disposition** | **CUT** | §7.3 — an aggregate over edge strengths, and no aggregate is ever written. v1 violated its own rule; PP-724 caught it |
| a **`Memory`** tag kind | **CUT, and `Holding` admitted in its place** | §3.1 (O-6) — a Memory is a Holding field-for-field, and `key`+`value` cannot carry the false picture that was Memory's entire justification. Enum count unchanged |
| a **`Proposition`** stored kind | rejected | §3.1 — content-addressing makes the store a **memo table**, not state: no history, no owner, never a write target, reconstructible from the tuples the tags carry. This is why P1 (every NPC holds propositions) is affordable |
| a **salience** stored field, or a **second decay law** | rejected | §3.2 — derived at read from `value`, `created_season` and one declared `λ_sal`. **Confidence, by contrast, is stored and does NOT decay** |
| a **`loyalty`/`allegiance` Gauge on the person** | rejected; it is an **edge kind** | §7.2.1 — a person stands differently toward several factions at once, so a person gauge needs a key, which is an edge with the naming hidden. As an edge it also gets a tag owner and a `causes[]` chain |
| **nine parallel personal meters** | still rejected | §5.2. `allegiance` is not a re-opening of that cut: it is **one** track, on the edge rather than the person, and it is the state the corpus's most duplicated arc shape reads |
| a **cross-season emission carry** | **rejected as non-existent, not as unwanted** | §9.3 — the transport is not in the tree; designing on it would be designing on a mechanism nobody built (**J-N**) |
| a **second resolver** | rejected | the only surveyed franchise with two resolution paths is also the only one with a two-decade unfixed divergence, exploited in both directions |
| a **view** primitive | rejected | disclosure stores nothing and resolves nothing; it is a declaration attached to state (E-2), which is what makes it checkable |
| a **central distributor / world director** | rejected, and the wrapper reframed | §9.1 — the herald populates `targets[]` and holds no receiver's rule |

---

## 11. What the player actually touches at this layer

**Almost nothing, and that is the design** (`00 §2`). This document is the richest layer in the suite
and the thinnest surface. Everything below is **read-only**; the substrate exposes **zero verbs**.

| what the player touches | how it reaches them | how often |
|---|---|---|
| a gauge's **band** — never its number | `gauge_band`, on a Slate item or a place summary | whenever the item they chose is on screen |
| the **posts they hold**, their remit and remaining **budget** — disclosed `exact`, because these are inputs to a decision they are making now | the post list | once a season |
| a tag's **existence and provenance** — *why did this actor turn on me* | inspection from a Slate item | on demand, never pushed |

| what the player never touches |
|---|
| creating, editing or deleting an **entity**, an **edge** or a **bloc** |
| firing a **form transition**, or running a **converter** — a marriage becoming a treaty is something they *learn about* |
| appending a **tag** or depositing into a **gauge** directly |
| a gauge's exact **value**, any transition's **threshold**, or any **forecast** of either (§8) |
| **strain**, **salience**, **divergence**, **presence levels**, **allegiance strength** — substrate, surfaced only as a situation |
| another person's **holdings** — what an NPC believes is inferred from what they do, never read off a sheet (§3.1). Only the *player's own* holdings are inspectable, and only as stance plus provenance |

**Substrate objects here: 6 entity kinds · 7 tag kinds (§3.1; `Ambition` is `09`'s, O-A1) · 6 adopted
relation kinds + 3 scope extensions + Knot held separately · 3 converters · 4 primitives · 2 extensions.
Surface affordances: 3 reads, 0 verbs.** If a later document's surface table is longer than its
substrate table, that document has the ratio backwards.

---

## 12. Module contracts — the substrate's own

Per W-6, every `consumes:` row names what the consumer does with the Key; the substrate's own modules
consume nothing, and none is declared speculatively. Three pure stores share one shape and are given
once rather than three times.

```yaml
# substrate.entity | substrate.ledger | substrate.gauge — the three pure stores.
# Identical but for the row marked *; all: parent: substrate · class: substrate · remit: [] (not
# invocable) · budget: null · consumes: [] · form: [] · transitions: [] · scales: all four · tier: null
- module: substrate.entity
  resolver: derivation
  emits: [{type: person.generated, terminal: false}]
  state: [{name: entity, bucket: entity, writable: false, owner: substrate.entity}]      # *
  disclosure: [{of: entity, inputs: published, presentation: exact, trigger: hidden}]
- module: substrate.ledger
  resolver: derivation      emits: []
  state: [{name: tag, bucket: tag, writable: true, owner: substrate.ledger}]             # *
  disclosure: [{of: tag, inputs: published, presentation: exact, trigger: hidden}]
- module: substrate.gauge
  resolver: accrual         emits: []
  state: [{name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}]          # *
  disclosure: [{of: gauge, inputs: published, presentation: band, trigger: hidden}]

- module: substrate.form
  parent: substrate         class: substrate
  scales: [personal, settlement, territory, peninsula]      tier: null
  resolver: gate            # every transition is a gate; §2.2
  remit: []                 # applied by the herald (W-5), never invoked by a post
  budget: null
  consumes: []              # gates read STATE, never a received Key (§9.3)
  emits: [{type: form.transitioned, terminal: false}]       # a crossing FACT, never a forecast
  state: [{name: form, bucket: entity, writable: true, owner: substrate.form}]
  form:
    - {entity_kind: person,  field: life_stage}     - {entity_kind: person,  field: capability}
    - {entity_kind: person,  field: traits}         - {entity_kind: place,   field: kind}
    - {entity_kind: place,   field: tier}           - {entity_kind: place,   field: facilities}
    - {entity_kind: place,   field: presences}      - {entity_kind: faction, field: posture}
    - {entity_kind: edge,    field: state}          - {entity_kind: edge,    field: tier}  # knot only
    - {entity_kind: unit,    field: unit_kind}      - {entity_kind: unit,    field: assignment}
    - {entity_kind: bloc,    field: members}        - {entity_kind: bloc,    field: state}
  transitions: [ALL declared rows in references/form_registry.yaml]
  disclosure: [{of: form, inputs: published, presentation: exact, trigger: hidden}]

# ONE container, PER-KIND semantics. Everything below that varies by kind is declared in the KIND's
# own registry row, never here. §7.3.
- module: substrate.edge
  parent: substrate         class: substrate
  scales: [personal, settlement, territory, peninsula]      tier: null
  resolver: gate            remit: []        budget: null      consumes: []
  emits: [{type: edge.formed, terminal: false}, {type: edge.transitioned, terminal: false}]
  state:
    # strain is declared PER KIND; a kind with no strain axis (kinship, PP-724 :334) has none, and no
    # two kinds' strain ever sums into one counter (PP-724 :162).
    - {name: edge.strain.<kind>, bucket: gauge, writable: true, owner: substrate.edge}
    # PC<->NPC disposition is STORED (canon's track). NPC<->NPC disposition is DERIVED from edge state
    # and is deliberately NOT a state row here (PP-724 :331-345; O-3).
    - {name: edge.disposition.pc_npc, bucket: gauge, writable: true, owner: substrate.edge}
    # person->faction allegiance is STORED: a path-dependent STOCK, not an aggregate (§2.1, §7.2.1).
    # Declared on the `allegiance` kind ONLY, and it never sums with edge strain or Knot strain (R-3).
    - {name: edge.allegiance.strength, bucket: gauge, writable: true, owner: substrate.edge}
  form: [{entity_kind: edge, field: state}, {entity_kind: edge, field: tier}]
  transitions:
    - knot.intact_to_ruptured     # gate: strain >= 5; reversible: false      (knots_v30 :180)
    - knot.intact_to_tempered     # gate: strain <= -5, Close only            (knots_v30 :54)
    - knot.tempered_to_intact     # reversible pair -> hysteresis REQUIRED; band UNSTATED in canon
    - kinship.cooperative_to_strained
    - kinship.to_severed          # institutional act, not strain            (PP-724 :334-340)
    - patronage.to_sworn_bond     # converter: retainer_ripening             (§7.4)
    - kinship.to_treaty           # converter: marriage_to_treaty            (§7.4)
    - rivalry.to_feud             # converter: PP-724 §2.6 escalation        (§7.4)
    - allegiance.aligned_to_wavering    # reversible pair -> hysteresis REQUIRED (§2.3), band declared
    - allegiance.wavering_to_aligned    #   in references/form_registry.yaml, not here
    - allegiance.wavering_to_estranged  # reversible pair -> hysteresis REQUIRED (§2.3)
    - allegiance.estranged_to_wavering  #   the recoverable half — the subcase §7.2.1 exists for
  disclosure:
    - {of: edge.strain.<kind>, inputs: published, presentation: band, trigger: hidden}
    - {of: edge.disposition.pc_npc, inputs: published, presentation: band, trigger: hidden}
    - {of: edge.allegiance.strength, inputs: published, presentation: band, trigger: hidden}

- module: substrate.post
  parent: substrate         class: substrate
  scales: [settlement, territory, peninsula]                tier: null
  resolver: gate            remit: []        budget: null      consumes: []
  emits: [{type: post.granted, terminal: false}, {type: post.revoked, terminal: false},
          {type: post.vacant, terminal: false}]
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: post.budget, bucket: gauge, writable: true, owner: substrate.post}
  form: []      transitions: []
  disclosure:
    - {of: post, inputs: published, presentation: exact, trigger: hidden}
    - {of: post.budget, inputs: published, presentation: exact, trigger: hidden}
```

`substrate.post`'s two rows disclose **exact**, not band: a post's holder and a budget's remaining
points are things the player acts on directly this season, and hiding them would obscure an input rather
than a threshold. **Note what is absent from `substrate.edge`:** a shared strain counter, a shared
capacity, a shared break rule, and any NPC↔NPC disposition row. Their absence is the container's
compliance with R-1, R-2 and R-3, expressed in the contract rather than promised in prose. **The
`allegiance` rows change none of that** — `edge.allegiance.strength` is a third *separate* gauge on a
third *separate* kind, and the count of shared counters is still zero. Its four transitions are two
reversible pairs, so §2.3's hysteresis guard binds on all four at load time; a loyalty track that
flickers between wavering and aligned every season is the exact failure that guard exists to catch, and
it is the one this kind is most exposed to.

---

## 13. Property audit

**Scope, and the honest limit. Nothing in this document rolls.** `substrate.entity`, `substrate.ledger`
and `substrate.gauge` are stores; `substrate.form`, `substrate.edge` and `substrate.post` are gates;
`derive_ob` is a derivation *consumed by* rollers elsewhere and is not itself a resolution. **No N/R/S/E
verdict is offered for a store or a gate** — manufacturing one for state with no draw is the error the
methodology explicitly names, and v1 was right to refuse it. What follows instead is the two properties
that *do* apply, plus every loop and gate with its bound. (Canon's Knot *formation* does roll — `Spirit
× 2 + History (Relationships)`, TN 7, Ob 2 — but that roll is canon's, at `knots_v30.md:76`, and
auditing it is the FI lane's job, not this page's.)

Above that sits `00 §0.1`: **a resolution-scoped audit cannot ask whether a design expresses the game.**
This page could pass every property below and still be the wrong substrate. The instrument for that
question is the elegance criterion, and its answers here are the one-line loss statements, the §10 cut
list and the `## Overrides` block — judgments, not checks.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass, and the strongest claim in the suite** | every gauge is bounded by declared floor and ceiling and restores geometrically, so the fixed point `rest + a/λ` is finite for every bounded accrual and every `λ ∈ (0,1]`, checked **at load time** against the registry with no campaign run (§5.1). Monotone response is structural. Form is bounded because every form field's value set is enumerated in the registry |
| **P-v** right engine | **pass** | every module here is `gate`, `accrual` or `derivation`. Nothing on this page is uncertain and nothing on this page rolls. **Every form transition is a gate on purpose** (§2.2): the uncertainty was in getting the gauges to the threshold, and re-rolling there charges for it twice |

### 13.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| gauge deposit → band → module gating → deposit | the fixed point `rest + a/λ`, checked at declaration (§5.1) | **unmeasured**; campaign-reachable, so measurable with a control, and it should be measured before any writer lands |
| form transition ↔ its reverse | **`θ↑ − θ↓ ≥ H_MIN` plus `dwell ≥ D`, checked at load** (§2.3) | **bounded arithmetically** — the only loop here with a proved bound, and why hysteresis is mandatory rather than advised |
| Knot strain → rupture → conviction scar → conviction weight → behaviour → strain | **terminating**: rupture is `reversible: false`, so the edge leaves the loop permanently; strain is gauge-bounded −5…+5 per tier (`knots_v30.md:49-52`) | **unmeasured**, and it is **canon's loop, not this suite's** — the FI lane inherits the measurement obligation |
| NPC↔NPC edge strain → derived disposition → behaviour → strain | per-kind capacity (PP-724 §3.1 `:123-134`, decision log `:671`); kinship cannot break by strain at all (§3.4 `:171`); rivalry and feud escalate rather than accumulate toward break (`:674`) | **unmeasured** — and the three kinds are bounded by **three different mechanisms**, which is the per-kind semantics doing its job rather than a gap |
| **do the two strain loops couple?** | **no. By R-3 they never sum.** A node in both takes both effects independently (PP-724 `:162-167`) | **not a loop** — the row exists because a reader will ask, and the answer is the anti-unification property, verified by the *absence* of a shared counter in §12 |
| holding salience → weighting → behaviour → new perception → holding | **`HOLDING_CAP` top-K at the sweep, geometric salience decay, and `RELATION_SHARE_MAX`** (§3.2, §3.4) | **unmeasured**. Three independent bounds is not a measured gain, and this page does not claim it is. ⚠ The store is bounded at `population × HOLDING_CAP` **by construction**, which is the cost P1 created and §3.2 answers |
| **allegiance: slight → allegiance falls → worse treatment → slight** | the gauge's own fixed point `rest + a/λ` (§5.1), plus `RELATION_SHARE_MAX` on every selection function that reads it (§3.4) | **unmeasured, and it is the one new loop this revision adds.** It is campaign-reachable, so it is measurable with a control, and it should be measured before any writer lands. The bound is arithmetic and load-time; the *gain* is not |
| tag append → selection → outcome → tag append | dedupe on `(owner, kind, key)` bounds count by `candidates × posts`; magnitude bounded by the gauge the value deposits into (§3.3) | **unmeasured** |
| **a Key-driven cascade within a season** | **`DEFAULT_CASCADE_DEPTH_MAX = 0`** — the guard **prevents cascades outright** rather than pacing them (§9.3) | **not a loop today.** If **J-N** rules for reactive chains this becomes a real loop with no bound yet, and §9.3 is what to revisit |

### 13.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| tag provenance non-empty | the append call | a refusal at append time |
| form transition gate | gauges, tags, form, identity — **never a roll, never a received Key** | no transition; the entity stays as it is |
| hysteresis band | the registry, at load | **load failure**, not a runtime surprise |
| vacancy (`holder_id is None`) | the post | the faction does not act at that tier (`05 §1`) |
| `remit` | the post's remit list | the module is not in the option set — not a penalty, an absence |
| Knot capacity `< floor(Bonds/2) + 1` | the person's `knot` edges, counted; no stored counter | formation unavailable (`knots_v30.md:70`) |
| Knot Thread contact `TS ≥ 30` (either party) | the person gauge, 0–100 | formation unavailable (`knots_v30.md:69`) |
| converter gate (§7.4) | both endpoints' posts and factions, and the source edge's state | no new edge; the source edge is untouched either way |
| **`derive_ob` commensurability** (§6.1) — top and bottom bands reachable, **after** modifiers, against **the envelope its declared `shape` selects**: one-sided for U/SO/GATE, differential for DO/BI (§6.1.2) | the target gauge's ceiling and floor, the site's modifier bounds, its pool bounds, and — for an opposed site — `pool_opposed_min`/`pool_opposed_max` — **all at declaration time, no campaign run** | **the registry row is rejected when written.** Falsifier: a test evaluating both inequalities for every declared `derive_ob` site under its own shape, failing on any that cannot reach all four bands. **A test that evaluates an opposed site one-sidedly is itself the defect** — it false-passes `Ob ∈ (8.247, 9.783]` at `N_c=18` vs `N_d=6`. Load-bearing on the game: the difference between a live mechanic and one that silently returns Failure forever |
| disclosure block present · `consumes:` row has rule content (W-6) | the contract, at check time | the contract check fails · the row is not declared |

### 13.3 The four qualitative verdicts, applied to the substrate rather than to a resolver

**Necessary** — four primitives, six entity kinds, **seven** tag kinds. The relation taxonomy is
**adopted, not invented**, so its necessity argument is PP-724's own decision log (`:669`) rather than a
claim this page has to make; the **three** additions occupy a scope PP-724 declares out of bounds. §10
records seventeen candidates refused, **four** of them cut because something on disk beat them — and the
newest of the four is the sharpest, because the thing beaten was **this page's own draft**: `Memory`
lost to the ruled `Holding` grammar (O-6). **Robust** — the failure
directions the corpus measured are closed by arithmetic: an unrecoverable pinned gauge by the geometric
law, a flickering threshold by the hysteresis band, and **a silently-dead resolution by the
commensurability gate** (§6.1), which is shape-aware and so does not false-pass an opposed site
(§6.1.2) — all three load-time checks needing no campaign run. A fourth — the
substrate quietly acquiring a latency it does not have — is closed by §9.3 stating the absence rather
than assuming the presence. **One honest hole remains and is named rather than smoothed:
`prac.thread_sensitivity` declares no ceiling in the cooked registry, which makes all three arithmetic
guards inert on it** (§6.2); that row is the FI/IN lane's to correct, and until it is, this document's
robustness claim has a hole it can point at. **Smooth** — one decay law, one obstacle owner, one disclosure contract, one write
rule with four leaves, one registry for the mutable-shape axis, one Key surface for every binding kind.
**Elegant** — six modules, one new registry from this page, no branch on any entity's identity anywhere,
and a player surface of three reads and zero verbs. The honest deduction: **the edge container is the
one object on this page whose elegance is contested**, and §7 argues it rather than assuming it.
