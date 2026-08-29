# 09 — Ambitions and Arcs: a project is a composition, and an arc is a chain you can walk

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## `audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` (RATIFIED, ED-IN-0011) ·
## `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` §11.1 (Jordan ruling) ·
## `systems/factions/political_dynamics_keys_migration_v30.md` (CANONICAL) ·
## `systems/_architecture/key_type_registry_v30.md` · `references/module_contracts.yaml` ·
## `audit/2026-08-11-world-schema-gap-audit/01_gap_register_part2.md` (G-29) ·
## `systems/settlements/governance_play_redesign_v1.md` (PROPOSAL)
## Continues in: [`09_ambitions_and_arcs_part2.md`](09_ambitions_and_arcs_part2.md) — §§8–13

**Change B.** v1's diagnosis, from `ARCHIVED.md`: *nothing initiates.* Every module fired from a
vacancy, a directive or a player action, so the world could only respond. A Project is the object
that lets an entity **want something over time**, and it is **not a new stored primitive** — it is a
composition of `01`'s four.

*Emergent possibility lost if the project were cut:* **nothing in the world would ever pursue
anything, and every event would be an incident rather than a development.**

**This document adds one player verb and three headless ones** — and one rule (§6.4) under which a
**place** declares a project with no verb at all, which is where the world's populations get to act.
Everything else it adds is `substrate` in the sense of `00 §2.1`. Its surface table (§9) is three
rows — **one verb and two reads** — and its substrate table is the rest of both parts.

**In two parts, in reading order** (`CLAUDE.md` §4): **part 1** — the arc grammar, the composition,
derived progress, the hook grammar, obstruction, the four verbs, arcs as tag chains (§§1–7).
**[Part 2](09_ambitions_and_arcs_part2.md)** — J-N and J-O, the player surface, the registries, the
module contracts and the property audit (§§8–13). Section numbers run continuously across both, and
**the `## Overrides` block below covers both parts.**

---

## Overrides

Listed, tiered and argued (`00 §5.3`). **A silent override is the corpus disease this suite exists
to stop**, and three of the six below are this document overriding *its own suite's draft* because
something already on disk beat it — *"may the best ideas win"* cutting against authorship.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-A1** | `01 §3.1`'s closing sentence — *"Six kinds, and the enum closes again at six"* | this suite's own `01` | **Seven.** A project declaration is a forward commitment; every one of the six records something **realized**. The two-part test `01 §3.1` itself specifies is run in §2.1, and the enum closes again at seven. This is `01`'s own procedure executed, not a bypass of it |
| **O-A2** | `01 §5.2`'s **`progress` Gauge** row — *"`progress` (v2) · any project owner"* | this suite's own `01` | **CUT. Progress is derived at read, never stored.** A stored progress is an aggregate over the project's advance terms, and **no aggregate is ever written** (`01 §2.1`, AU-1). This is structurally the same defect `01 §7.3` caught in v1's edge disposition, one document later. §3 |
| **O-A2b** | `references/module_contracts.yaml:343`'s `{name: "projects", bucket: clock, writable: true}` — canon stores project progress as a monotone 0→10 clock | **canonical contract** (`political_dynamics_keys_migration_v30.md:6` is `## Status: CANONICAL`) | A storage divergence, recorded rather than hidden. This design derives the same number, and **the ratchet case is reproduced exactly** (§3.2), so a port keeping canon's stored clock and one deriving it fire on the same season. Only the write leaf differs — and only one of the two obeys AU-1 |
| **O-A3** | `00 §9.2`'s three proposed key types **`project.declared` / `project.fired` / `project.lapsed`** | this suite's own `00` | **CUT as duplicates. Three of the four already exist and are registered** under ED-935: `mechanical.project_advanced` (`key_type_registry_v30.md:446`), `state.project_completed` (`:691`), `state.project_failed` (`:710`), all with `emitting_systems: [npc_behavior]` and live contract edges at `module_contracts.yaml:318-320, :333-335`. Only **formation** is missing, and `audit/2026-08-11-world-schema-gap-audit/01_gap_register_part2.md:281` (G-29) already proposed `state.project_formed` for it. §10 |
| **O-A4** | `systems/settlements/governance_play_redesign_v1.md:241` — *"every significant NPC **advances their ambition by 1**… unless the player or another actor intervened"* | **PROPOSAL, unratified** (`:3`) | Its **schema and its argument are adopted** (§5, §9); its **advance rule is replaced**. A `+1` per season on a stored counter is a timer whose only obstruction is a bespoke intervention. Here advance is a **read of world state**, so obstruction is *any* act that moves a term the project reads — and needs no verb of its own |
| **O-A5** | `proposals/2026-08-18-epistemic-propositions-and-provenance.md §3.4`'s **Condition** row — *"a proposition (or **conjunction**) the engine evaluates"* | a **DESIGN whose five calls are RULED by Jordan** (`:3`), the design itself still PROPOSED | **Generalized, not replaced.** An advance term **is** that Condition, exactly; but a conjunction cannot express *k*-of-*n* or unequal weights, both of which the corpus already contains (§3.2's coup counter). The composite is the more general object and the direction of travel runs **from** this page **to** that one. Ownership splits on the ruled **P4**: P4 owns the leaf predicate vocabulary, `09` owns the composite over it. §3.4 |

**Inherited, not re-decided:** `00 §5.3` O-6 — the **138-arc calibration set is evacuated**, so the
instruction at `narrative_engine_design_v2_churn.md:91` (*"the compiled generator must reproduce them
from their trigger states"*) is neither obeyable nor overridable. §7.2 states it as a **named gap**.

### Adopted on merit, not because it binds — the amended authority model

**Jordan, 2026-08-29 (mid-drafting):** *"existing work is not necessarily required to keep all the way
through to things like obstacles being stat/2 or whatever is ratified and canon"* · *"I just want the
best possible proposal."* So **nothing in the tree is out of bounds** — not ratified canon, not a
prior Jordan ruling. The delta spec's tier-1 *"follow it"* and tier-2 *"integrate, don't duplicate"*
become **evidence to weigh**, and only the `## Overrides` disclosure rule survives intact.

**Two things this document could now override and does not.** Recording the decision *not* to
override is as much a decision as overriding.

| kept | tier it *was* | why it is kept **on merit** | what would have made me drop it |
|---|---|---|---|
| **The arc-vector template + binding-slot grammar** (ED-IN-0011) | ratified canon | **derived from 138 real authored arcs**, not from a preference; and its anti-oatmeal defence — *specificity from binding at instantiation* — is exactly the property a project object needs and a naive generator lacks. Replacing a decomposition drawn from 138 arcs with one drawn from zero would be a worse proposal wearing my name. §1 | if the ~13 shapes could not express the four-verb lifecycle. **They can** — §1's slot table maps it with nothing left over. ⚠ **That is the easy direction; §1.2 runs the converse**, where two shapes are only partly expressible and three fail outright in documents other than this one |
| **The hook grammar** — *the script is the PREDICATE* (2026-08-18) | a Jordan ruling | it **solves scripting drift better than the alternatives**: the authored part is a *predicate over world state*, which cannot special-case an entity, and everything downstream stays emergent. Plus **three worked in-tree precedents**, so it is tested rather than proposed. §4 | if it forced authored content into code branches. **It does not** — §10.2 makes every hook a registry row |

**One place this document does extend past both, argued rather than assumed** (§3.1): the templates
and all three precedents are **unweighted** — a conjunction that must fully obtain, or a counter that
must reach `k`. This design generalizes to a **weighted sum of indicator terms**, subsuming both as
special cases and adding partial progress neither can express. **One formula replacing two shapes**,
which is the elegance criterion's distillation side — listed here rather than slipped in, because it
extends a ruled grammar. **§3.4 states the same extension against the epistemic layer** and files it as
**O-A5**, since that is where the leaf vocabulary is ruled to live.

---

## 1. The arc grammar — a project kind **is** an arc-vector template

**This document authors no arc model, because a better one exists and is ratified.**
`narrative_engine_design_v2_churn.md` (`## Status: RATIFIED (Jordan, 2026-07-05 … ED-IN-0011)`, `:3`)
already names *"ambitions/projects"* among the durable substrate (`:76`) and already owns the arc
question with a specific answer (`:80`):

> **Arc-vector TEMPLATES with binding slots** — the ~13 structural shapes the 138 register arcs
> collapse to … trigger predicates over state-graph FAMILIES × binding slots (faction × territory ×
> settlement × NPC × stake).

and its anti-oatmeal defence (`:93-96`):

> **Specificity from binding at instantiation.** A template bound to THIS settlement's circumstances …
> and THIS NPC's ambition is particular by construction.

**So: a project *kind* is an arc-vector template. Declaring a project is binding its slots.** That is
the whole of v2's arc theory, and it is inherited rather than restated.

| ratified slot | what binds it here |
|---|---|
| faction · territory · settlement · NPC | the project's **owner** and its **target** — any entity id (§2) |
| stake | the project's **terms** — what the fire consequence does, drawn from the four write leaves |
| trigger predicates over state-graph families | the project's **advance terms** (§3), each a predicate over gauges, tags, form and posts |

**What v2 contributes is not arc theory. It is the object a person owns and advances** — the row, the
four verbs, and the demonstration that all of it composes out of `01`.

### 1.1 The two ratified honest residues, honoured

`:97-104` declares two classes of arc that **do not fire**, and this document does not quietly imply
otherwise:

1. **The ~15% GM-judgment-irreducible arcs** (fork 7) — **declared non-firing.** In v2's terms: a
   project kind whose fire consequence is not expressible in the four write leaves is marked
   `firing: false` in its registry row and never instantiated. Its row exists so the gap is countable.
2. **The bespoke-EFFECT NPC arcs** — triggers bind as templates, but effect logic is an authored
   decision procedure, not a slot. In v2's terms: **the effect table is DATA in
   `content_registry.yaml`, or the row is `firing: false`.** It is never an `if owner == X` branch —
   that is scripting drift and `00 §6` principle 2 rejects it.

### 1.2 The check run in the other direction — can the lifecycle express the shapes?

The `## Overrides` table above asks whether the ~13 ratified shapes can express **this object's
lifecycle** and answers yes. **That is the easy direction, and running only it was a real methodological
hole**: the load-bearing question is the converse — *can a project row express the shapes?* **Two of the
ratified shapes are named here because the answer for them is *partly*** — and a partial answer stated as
a pass is the disease this suite exists to stop. (Both are named exactly, not counted: `_workings_joined.md:1931`
identifies them as the two templates the 13 event-tier arcs collapse to, which is why they are the two
this document could check without the evacuated corpus.)

| ratified shape | expressible as a project row? |
|---|---|
| **COLLISION A–J** (8) — *"cross-arc-collision predicate over ≥2 other arcs' state"* (`_workings_joined.md:1931`) | **yes, and only since §3.1's `tag age` term.** *Both arcs live* is two tag-existence terms — an Ambition tag exists exactly while its project is live. What tag-existence alone could **not** say is *within a window*: two grievances three seasons apart and two thirty seasons apart read identically, and a collision that admits any separation is not a collision. `tag age` closes it, over a field the tag already carries |
| **BG-CV-01..05** (5) — *"multi-stat-AND one-time trigger → permanent bump"* | **partial, and the limit is structural.** The multi-stat AND is §3.1's equal-weight conjunction and the one-time trigger is §6.2's terminality — both exact. The **permanent bump** is expressible only where a **discrete** form value happens to exist to move to: `01 §5.1`'s decay law gives every gauge `λ ∈ (0,1]`, `rest` and `λ` are declared at load with **no setter** (`01 §5`), so a gauge deposit *always* relaxes to rest and **a permanent continuous change is forbidden by the substrate.** Permanence lives in leaves 2–4 only — a durable Tag, a post grant, a form transition. Where a shape's "permanent bump" has a form row (`place.kind`, a presence band), it is exact; where it does not, this design **cannot** express it, and no weighting of terms recovers it |

**What this document does *not* claim.** B's shape check also found three shapes that fail outright,
and **none of the three is fixable here**: person↔faction allegiance has no edge kind with a magnitude
(`01`'s registry), belief has one writer (`02`/`08`/`11`), and no one can refuse an offer (`04`'s
`pm.appoint`). They are recorded in this table's neighbourhood because **this is the document where the
shape check is run**, not because this page owns the edits. Do not read §1's "nothing left over" as
covering them; it covers the lifecycle direction only, which is what it says.

---

## 2. A Project is a composition — the explicit table

**Nothing below is a fifth stored kind.** Every column right of the divider is `01`.

| part of a project | primitive it is | where |
|---|---|---|
| the **intent**, its target, its terms, its horizon | a **Tag** on the owner — `kind: Ambition`, `key: (project_kind_id, bindings)`, `ttl: horizon`, `provenance` required | `01 §3` |
| **who owns it**, and **who it targets** | ownership is the tag's `owner_ref` — there is no owner field; targets are entity ids in its `value` payload, and **edges** where the binding is a relationship | `01 §3`, `§7` |
| **progress toward it** | **derived at read** from the project kind's advance terms — nothing stored | §3, O-A2 |
| **what advances it, what fires it, what it does** | a **registry row** on the project kind, in `references/content_registry.yaml` | `00 §9` |
| **the residue when it ends** | a **Precedent** Tag, and the Keys already registered under ED-935 | §10 |
| **what it costs to declare** | one point of the owner's post **budget** Gauge | `01 §5.3` |

**Zero new gauges. Zero new entity kinds. Zero new registry files.** The project kind is a **row** in
a registry `00 §9` already commissions.

### 2.1 The seventh Tag kind — `01 §3.1`'s own two-part test, run (O-A1)

`01 §3.1` closed the tag enum at six and specified the procedure for a seventh: *"A seventh needs the
same two-part argument; 'a mechanic wants somewhere to live' is not it."* Here is the argument.

1. **Every one of the six records something realized; an Ambition records something that has not
   happened.** A Precedent is a thing that was done, a Grudge a thing suffered, a Debt a thing owed,
   a Reputation a thing attributed, a Leverage a hold currently held, a Memory a thing perceived. All
   six have a `value` that is the **magnitude of a fact**. An Ambition's payload is a **target and
   terms** — a commitment about the future. There is no magnitude to carry, and every consumer that
   reads a tag as evidence would read this one as evidence of something that did not occur.
2. **Reusing `Precedent` is false-friend reuse, which is prohibited.** `06_master_synthesis.md:566`
   (Part VI, held) names *"false-friend reuse … the term-vs-concept error, pre-empted twice by the
   corpus."* `01 §3` defines Precedent as a place's or faction's record of what was done there; a
   consumer reading Precedent to answer *"what constrains what may be done next"* would silently
   ingest a future as a past. The collision is semantic, not stylistic.

**Seven kinds, and the enum closes again at seven.** `Ambition` is also the *only* tag kind that is
**not** third-person institutional record **and** not first-person perception — it is first-person
**intent**, which is why neither existing half absorbs it.

⚠ **This is the one place where this document could not compose cleanly out of `01` as written**, and
it is reported as such rather than smuggled. It costs one enum member, not one primitive.

---

## 3. Progress is derived — the ratchet and the conjunction are one shape

### 3.1 The formula

At the accounting boundary, for every live project:

```
progress(P, season) = Σ_i  w_i · [ term_i holds at season ]           # integer basis points
threshold(P)        = declared on the project kind's row
```

Each `term_i` is a **predicate over readable state**, and the admissible term kinds are enumerated —
a closed list, because an open one is where a predicate grammar becomes a scripting language:

| term kind | reads | example |
|---|---|---|
| gauge band | `gauge_band(g, season)` (`01 §5`) | `place.condition.order` at or below `strained` |
| form value | a declared `form_registry.yaml` field | `target.kind == Ruin` |
| tag existence | `tag(owner, kind, key)` exists | a `Precedent:failure_mark.*` is present |
| **tag age** *(added — item 4 below)* | `season − tag.created_season` against a declared window | two grievances appended **within 3 seasons of each other** |
| post holder | a post's `holder_id`, its kind, its tier node | the target's parent tier post is vacant |
| edge state | an edge's `state` / declared per-kind gauge (`01 §7`) | a charter edge is `intact` |
| season index | the absolute season counter | `season >= 8` (the fuse precedent, §4) |

**Nothing is stored, nothing is written, and the resolver is `derivation`** (`00 §7`). This is AU-1
obeyed rather than asserted: a stored progress counter is an aggregate over the terms, and `01 §2.1`
forbids writing one.

⚠ **`tag age` is an addition to the grammar this document shipped in v2, and it is disclosed as one.**
It was added because without it the ratified **COLLISION** shape is only partly expressible (§1.2), and
it costs **no new state**: `created_season` is a field every Tag already carries and that `01 §3.2`
already reads to derive salience. It is a *non-ratchet* term — it can go false as time passes — which is
consistent with §3.2, where monotonicity is a property of ratchet terms only and never of the formula.

**Why this is the same object as the hook grammar (§4).** A conjunction hook — *"Crown eliminated,
**and** Baralta alive, **and** Hafenmark Mandate ≥ 4"* — is the case where every `w_i` is equal and
the threshold is the sum of all of them. A ratchet hook is the case where the terms are tag-existence
predicates (§3.2). **One formula, one registry of kinds** — `00 §1`'s corollary, which says prefer
one object with a registry of kinds over several objects.

**Numbers in this document are shape proposals, not ledger constants.** Where canon already supplies
one — threshold 10, stall 8 seasons — this design adopts canon's and says so.

### 3.2 The monotone counter, without an exemption to the decay law

`00 §4.0b` grants a permission a cautious author would refuse: **a monotone counter that never
decrements is allowed for a hook of this class**, per the Jordan ruling and the coup-counter
precedent. This design takes the permission and **needs no exemption to get it.**

A **ratchet term** is `[ a durable Tag with key K exists on the owner ]`. Tags are append-only, a
durable tag has `ttl: None`, durable tags survive the boundary sweep and survive succession
(`01 §3.3`). **A ratchet term, once true, is true forever — monotonicity by construction, not by
carve-out.** No second decay law, no `λ = 0` gauge (which `01 §5`'s `λ ∈ (0,1]` forbids anyway), no
new stored field.

**The Löwenritter coup counter, reproduced exactly.** Canon: Grandmaster Ehrenwall tracks a private
Autonomy 0–3; at 3 *"the Split fires at the next seasonal accounting"*; one named failure-mark
condition is *"Church Influence reaches 40 while the Crown has taken no action to reduce it that
season"*; and **"Counter never decrements. Once Ehrenwall marks a failure, she does not revise the
assessment"** (`systems/factions/factions_personal_v30_infill.md:74`, `:75`, `:76`).

```yaml
project_kind: loewenritter_split                 # a ROW, not a branch. No faction named in code.
owner_binding: {entity_kind: faction, gate: <holds a military-order charter edge>}
advance_terms:                                   # each a ratchet: a durable Precedent tag's existence
  - {w: 1, term: "tag(owner, Precedent, key=failure_mark.*) exists"}   # counted, not summed by hand
threshold: 3
fire: {guaranteed: true, at: accounting_boundary}
horizon: null                                    # a grievance ledger has no expiry; see §6.1
```

The failure marks are **Precedent tags appended by whatever module observed the failure**, each with
its own provenance. Progress is `count(matching tags)`. It cannot decrement because nothing deletes a
durable tag. **`if faction == Löwenritter` appears nowhere**; the row is data and any faction meeting
`owner_binding` gets one.

### 3.3 Bands, not numbers — and never a forecast

Derived progress is read through **bands**, exactly as a gauge is (`01 §5`, `01 §8`). Three
consequences, and the third is a prohibition this document is bound by:

1. **A project emits on a band crossing, never on a delta.** Recomputing progress every boundary and
   emitting each change would put a Key on the Slate every season for every live project. Band
   crossings are rare by construction and are the anti-strobe discipline applied one layer down.
2. **The player sees the band and the terms, never the number or the threshold.** `01 §8`: publish
   every input, publish a band, never publish the trigger. A project's advance terms are inputs and
   are published; its `threshold` is a trigger and is hidden.
3. ⚠ **A project may never publish how close it is to firing.** `06_master_synthesis.md:564`
   (Part VI, held) prohibits a world-visible imminence Key: *"`threshold_crossed` carries crossing
   **facts**, never forecasts."* Adopted without reservation. `mechanical.project_advanced` carries
   `progress_before` / `progress_after` — **crossing facts about a band that has already been
   crossed** — and nothing else. **No emitter in this document publishes a forecast**, and the
   forecast/imminence terms of `10`'s ratified light are computed by `10` from realized state, never
   handed to it by a project.

### 3.4 An advance term **is** a Condition — and the composite over them is the more general object (O-A5)

`proposals/2026-08-18-epistemic-propositions-and-provenance.md` is `## Status: DESIGN CALLS RULED
2026-08-18` (`:3`) — **five Jordan rulings, P1–P5** — and its §3.4 gives three things over one grammar:

| | who holds it | what it is |
|---|---|---|
| **Fact** | the world | the proposition obtains in world state |
| **Belief** | an agent | a `Holding` — may be false, revisable, with provenance |
| **Condition** | a scripted hook | *"a proposition (or conjunction) the **engine** evaluates"* |

**An advance term is that third row exactly** — not analogously. Its own worked example is one of
mine: *"A Crown Claim's `Hafenmark Mandate ≥ 4` … [is] the same kind of object"* (`:107-109`), and that is
§4's third precedent, term for term. So §3.1's table is not a private grammar; it is the Condition
vocabulary, and it should be **read from a registry rather than restated here.**

**But the weighted sum with a threshold is not a proposition. It is a composite *over* propositions**,
and it is strictly more general than the ruled wording: a conjunction is the case where every `w_i` is
equal and `threshold = Σ w_i` (§3.1), and the ruled grammar has no way to say *three of these five, and
this one counts double.* The division of ownership that follows is clean, and it uses the ruled **P4**
split rather than inventing one:

| layer | owner | why |
|---|---|---|
| the **leaf vocabulary** — which predicates exist and which are engine-evaluable | **P4, ruled**: IN owns engine-evaluable predicates, FI owns claim-only, plus a promotion rule | a hook predicate must be *computable*; a claim predicate need only be *sayable*. §3.1's seven term kinds are all engine-evaluable and belong to IN's half by that test — none of them is claim-only |
| the **composite** — weights, threshold, `required`, `ratchet`, bands | **this document** | it is the object P4 does not have and does not want: a registry of predicates says nothing about how many of them, weighted how, make a thing fire |

**And that flows back.** This is an override of a ruled design's shape, listed rather than slipped in:
the ruled *"proposition (or conjunction)"* should **generalize to the weighted composite**, because the
conjunction it names is already the composite's degenerate case and the corpus contains hooks (`k`-of-`n`
counters, §3.2) that a conjunction cannot express. `## Overrides` **O-A5** records the direction of
travel. Nothing here amends that proposal — it is a proposal, and this is a proposal reading it.

**Two-way benefit, and it is not rhetorical.** The ruled design's **independence metric** —
*"the number of `support_refs` whose `Key.causes` ancestries are disjoint"* (`:85`) — is uncomputable
today because `Key.causes` is unpopulated. This suite's provenance-required-everywhere rule
(`01 §3.3`) is exactly the emission discipline that populates it, and **§5's `supporters` /
`obstructors` derivation is its first consumer**: a set computed by walking `causes[]` for the terms
that moved. A project that fires *is* a corroboration query, run on the world instead of on a witness.

⚠ **Two honest blockers, both the ruled design's own and neither closed by this integration.**
`Key.causes` is populated at three non-test sites, only one of them conditionally non-empty
(`echo_transport.py`, `faction_action.py`, `parliamentary_transfer.py`) — the standing blocker
shrinks *because* of the integration, it does not disappear. And **the content-address hashing rule is
unspecified** (`:260-262`, *"still the first thing to nail down"*); with the leaf vocabulary shared, that now
gates **two** mechanisms rather than one. Neither is this document's to fix; both are named so that a
reader does not mistake the integration for a completion.

---

## 4. The hook grammar — the script is the PREDICATE (Jordan, 2026-08-18)

> **"We can script narrative hooks and sequences so long as we don't script entire arcs. We've done
> it with the coup counter, for example."**
> — Jordan, 2026-08-18 (`proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:618`)

**Under the amended authority model this ruling is evidence, not a fence** (the note after
`## Overrides`) — and it is adopted anyway, on merit: **it is the only formulation in the tree that
stops scripting drift without banning authored content.** The authored part is a *predicate over
world state*, which by its shape cannot name an entity or an outcome; every consequence of it holding
is emergent. And it arrives with **three worked in-tree precedents**, so nothing here is untested.

| precedent | what IS scripted | what is NOT | the project row that expresses it |
|---|---|---|---|
| **Löwenritter coup counter** (`factions_personal_v30_infill.md:74-76`) | a private counter that **never decrements**; a **guaranteed** fire at threshold 3 at the next accounting; a fixed consequence | when it trips, who pushed it there, what the player does, everything downstream | §3.2 — ratchet terms over durable tags, `fire.guaranteed: true` |
| **Royal Assassination fuse** (`conflict_architecture_proposal.md:87`, `:89`; `## Status: CANONICAL`, `:2`) | one per campaign; fires at S8+; ***"succeeds when it fires — no attempt/failure variance"***; target fixed at start | the season within the window, the target, whether the player detects and averts it, the whole consequence arc | a single season-index term, `fire.guaranteed: true`, `resolver: gate` — **no roll** |
| **Baralta's Crown Claim** (`baralta_crown_claim_v30.md:26-40`; `## Status: DESIGN`, `:6`) | a scripted **conjunction of world facts**: Crown eliminated **or** Royal Deposition; then per-claimant conditions — *Baralta alive + Hafenmark Mandate ≥ 4*, *Löwenritter Autonomy ≥ 3*, *CI ≥ 40* | whether those facts ever obtain, by what route, who else qualifies, who wins the resulting contest | §3.1 — equal-weight conjunction, `threshold = |terms|` |

> **The script is the PREDICATE. The arc is emergent.**

**Two permissions taken explicitly**, so a later reader does not read them as drift. **(1) A
guaranteed fire at threshold is allowed** — no attempt/failure variance, as two canonical precedents
do, so **every project's fire is a `gate`, never a `d_sigma`** (`00 §6` principle 4; `01 §2.2`: *the
uncertainty was in getting the state there, and re-rolling at the threshold charges for it twice*).
**(2) A monotone counter is allowed**, and §3.2 takes it without an exemption — `01 §5.1`'s decay law
is untouched by this document.

**Note the second precedent's status caveat, carried honestly:** `baralta_crown_claim_v30.md:6` is
`## Status: DESIGN`, not canonical. **Two canonical precedents plus one design-tier one; the ruling
rests on the first two**, and this document's shape does too.

### 4.1 Generate solvable, let the world erode it

The same ruling's generalization (`:660-670`): *"Solvability is a generation-time precondition, never
an ongoing constraint."* Applied here: **a kind's conjunction may be guaranteed reachable at
declaration and is never maintained against the sim.** A project whose target place is sacked or
whose terms another actor makes unreachable **lapses** (§6.1) — not a bug in the hook but the
texture, and why `lapse` is a real outcome rather than a consolation.

### 4.2 The extension, and why it still stops scripting drift

All three precedents are **singular authored hooks** — one coup counter, one fuse per campaign, one
crown claim. This document generalizes the grammar to a **population**: every NPC, bloc and faction
holds projects built from the same object. That is a real extension of the ruling's scope, and it is
where a drift objection would land, so here is the answer — four guards, each checkable:

| the drift risk | what blocks it | falsifier |
|---|---|---|
| a hook that names an entity — `if faction == X` | a kind's `owner_binding` is a **predicate**, never an id; instantiation binds slots at runtime (`churn:93`) | §13.3 row 5 — grep for a literal entity id in any row |
| a hook that names an outcome | `fire.effect` must terminate at one of `01 §2.1`'s **four write leaves** *and* be reachable by a module already in some post's remit (§6.2) | §13.3 row 3 |
| an inexpressible effect smuggled in as code | the kind is marked **`firing: false`** and **counted** (§1.1) — the ratified honest-residue discipline (`churn:97-104`) applied to this object | the count of `firing: false` rows is a number, not a feeling |
| a hook that is really a scripted arc | the script is one **predicate** and one **consequence**. Everything between the world reaching the predicate and everything after the consequence is emergent, including who pushed it there (§5) | §13.3 row 7 — if progress never falls from an unrelated actor's action, these are timers |

**The generalization lowers the drift risk rather than raising it.** A singular authored hook is
special-cased by definition — it exists for one actor. A population of hooks built from one row shape
cannot be, because the shape has nowhere to put the special case.

---

## 5. Obstruction needs no verb — the mechanism, named

The delta brief's hardest requirement: **a project must be obstructable by another actor, or it is a
timer.** Here is the mechanism, and its whole strength is that it costs nothing.

**Advance is a read of world state. So any act that moves a term a project reads obstructs it — with
no obstruct verb, no obstruct module, and no knowledge of the project at all.**

| the project's term reads… | any actor obstructs it by… | with a verb that already exists |
|---|---|---|
| a place's `condition.order` band | driving that place's order down, or holding it up | `08`'s directive/response set |
| an incumbent's `presence.<institution>` level | contesting influence at that place | `05`'s `act.contest_influence` |
| a post's `holder_id` | appointing, recalling, or letting it fall vacant | `04`'s `pm.appoint` / `pm.recall` |
| an edge's `state` | rupturing, tempering or converting the relationship | `01 §7` |
| the absence of a Precedent tag | doing the thing that appends one | any module that appends a tag |

**Three properties fall out, and each is load-bearing.**

1. **Obstruction is never special-cased.** No module branches on a project; no project names an
   obstructor. `00 §6` principle 2 is satisfied structurally rather than by discipline.
2. **Obstruction can be accidental**, which is where the interesting stories are. A governor who
   raises order for their own reasons has just killed a rival's ambition and may never learn it.
3. **Canon already names the record for it.** `state.project_completed`'s payload carries
   `supporters` and `obstructors` (`key_type_registry_v30.md:691-706`), and Procedure C writes
   per-supporter and per-obstructor memory references with `salience: 4` and a `relationship_tag`
   (`political_dynamics_keys_migration_v30.md:219-256`). **That is `01 §3.1`'s perceptual tag kind,
   arriving from canon** — two designs converging without either knowing about the other, which is
   the strongest evidence either is right. ⚠ **Named by role, not by label, deliberately:** `01`'s own
   T4 edit cuts the `Memory` kind in favour of the ruled **`Holding`** (a `prop_id` + stance +
   `support_refs`, which can carry *what* is misremembered where `key`+`value` cannot). This paragraph
   is indifferent to which name lands — the object is *the first-person record of a perception*, and
   §3.4 is why the Holding version is the better home for it.

**`supporters` / `obstructors` are derived at fire**, not accumulated during the project: the set of
actors whose Keys appear in `causes[]` for the terms that moved. No stored list, no aggregate written.

### 5.1 Adopted from `governance_play_redesign_v1`, on merit (O-A4)

That document is a **PROPOSAL** (`:3`) and its advance rule is replaced above. Three of its ideas
beat anything this document would have invented, and are adopted with credit:

- **The dossier's `ambition` + `trajectory` pair** (`:219-232`) — *"the two additions that make NPCs
  churn the world"* (`:237`). `ambition` is the Ambition tag; **`trajectory` is method escalation**
  (`if blocked: lawful → factional → violent/covert`), and it needs no new machinery — a lapsed
  project's **Precedent residue is a declared advance term of the successor kind**, so escalation is
  *lapse-and-redeclare*. That is canon's `generate_replacement_project`
  (`political_dynamics_keys_migration_v30.md:196-215`) with zero additions.
- **Speccing for friction** (`:246-250`) — orthogonal convictions, **overlapping ambitions** (two
  owners, one target, forcing a third party to be kingmaker), cross-cutting relationships. Authoring
  guidance for the registry, not mechanism, and where the density comes from.
- **The four-conflict-surfaces argument** (`:264`) — one well-specified person generates a petition, a
  friction, an intrigue and an ambition. **The playing-surface budget's whole thesis** (`00 §2.2`):
  depth from *which situation arrives and what it is entangled with*, never from menu breadth.

---

## 6. The four verbs

```
am.declare   an entity commits to a project        → Ambition tag + Precedent residue on the target;
                                                     costs one budget point; emits (formation, §10)
am.advance   at the ACCOUNTING BOUNDARY, once, over every live project
             progress = f(owner state, world state, tags)      ← a READ. NO RNG. NO received Key.
am.fire      threshold held → the world initiates: the declared consequence applies, terminal
am.lapse     horizon or stall reached without threshold → expires, leaving a Precedent residue
```

`am.advance`, `am.fire` and `am.lapse` are **never invoked by a post** — the herald runs them at the
boundary (`01 part 2 §9.2`, W-5) and publishes their Keys. `am.declare` is the **one surface verb**
this document adds (§9) — and for **`place`-bound kinds it is not invoked either**: those declare
themselves at the boundary from their own gate (§6.4), which is how the world gets ambitions that no
post-holder authored.

### 6.1 Lapse is the whole reason the queue does not become immortal clutter

**A project with no horizon is pressure that never releases**, and an ambition queue that only grows
is the second-order version of the volume defect `10` exists to fix. Lapse costs **nothing new**:

| lapse condition | the mechanism it uses | already exists at |
|---|---|---|
| **horizon** | the Ambition tag's **`ttl`**. The boundary sweep already drops expired tags | `01 §3.3` |
| **stall** | `tag_append` **dedupes on `(owner, kind, key)` and refreshes in place**, so re-appending the Ambition tag on each band crossing refreshes its `ttl`. **N quiet seasons and it expires.** Canon's `seasons_stalled >= 8` is exactly this with `ttl = 8` | `01 §3.3`; `module_contracts.yaml:350-352`; `political_dynamics_keys_migration_v30.md:196-215` |
| **unreachability** | a term the kind declares `required: true` becomes permanently false — e.g. the target place is destroyed | §4.1 |

**The residue is the point.** Lapse appends a `Precedent` tag on the owner *and* on the target: *the
Guild tried for this charter and failed here.* That residue is a legitimate advance term of a later
project kind, which is how a failed ambition becomes the seed of the next one instead of vanishing.

⚠ **`horizon: null` is permitted for ratchet kinds only** (the coup counter is a grievance ledger and
canon gives it no expiry), and a null-horizon kind must declare `firing: true` with a reachable
threshold. **A non-ratchet kind with no horizon fails the registry check.**

### 6.2 What `am.fire` may do — the four leaves, and nothing else

The consequence is declared on the row and terminates at **exactly one of `01 §2.1`'s four write
leaves** — a gauge deposit, a tag append, a post grant/revoke, or a form transition.

| forbidden in a fire consequence | because |
|---|---|
| a write that is not one of the four leaves | `01 §2.1`. There is no fifth |
| a consequence the owner could not have reached through a module in some post's remit | it would be a power that exists only for project-holders — scripting drift wearing a registry row |
| naming an entity, a faction or an outcome | `00 §6` principle 2 |
| a roll | §4. Fire is a `gate` |
| an effect not expressible as data | then the row is `firing: false` and is **counted** (§1.1) |

**A project is terminal on fire.** It transitions to `fired` and cannot re-fire, so there is no
reversible pair and `01 §2.3`'s hysteresis requirement does not apply — the one place in this suite
where a threshold has no band, and the reason is terminality, not oversight.

### 6.3 Worked kind — the founding project, and the `07` seam it closes

`07`'s **`place_found`** transition (`07_places_and_settlements.md:242-248`) gates on *"a Tag
{kind: Precedent, key: founding_claim, owner: this place} exists, deposited by the firing effect of a
Project (09 `am.fire`) naming this transition"*, and it is **verb-free on purpose** (`:264`) —
*"colonization is what a faction's ambition looks like when it succeeds"*, never a `pl.*` menu item.
**Nothing else in this suite deposits that Tag**, so without a project kind that does, `07`'s row is a
declared-but-unreachable registry row. This document wires it, and the wiring is a **row, not a verb**:

```yaml
project_kind: found_settlement
class: substrate                       # a faction or bloc ambition; NEVER a player menu item
owner_binding: {entity_kind: faction|bloc,
                gate: <owner holds a post of kind head|governor at target's PARENT tier node>}
slots: [target]     # target MUST be an EXISTING kind: Ruin node (07 §3.5). A project never creates
                    # an entity and never touches the adjacency graph — there is no such write leaf.
advance_terms:                                                        # equal weights -> conjunction
  - {w: 1, term: "target.kind == Ruin", required: true}
  - {w: 1, term: "owner holds a charter edge to target's parent node"}
  - {w: 1, term: "some place adjacent to target is at or above its prosperity band"}
  - {w: 1, term: "owner's post budget accrual band >= <declared>"}    # SHAPE PROPOSAL
threshold: 4        horizon: 12         # SHAPE PROPOSAL, seasons; lapse leaves the residue (§6.1)
fire: {guaranteed: true,
       effect: tag_append{kind: Precedent, key: founding_claim, owner: <target>}}    # write leaf 2
```

⚠ **The `owner_binding` gate above is a CORRECTION, and the defect it fixes was fatal rather than
cosmetic.** v2 shipped `gate: <holds a post whose remit includes founding>`. **A `remit` names
MODULES** — `01 §4.3`: *"a module is invocable only by a post whose remit names it"*, and `00`'s remit
rule says the same — and **no module named or resembling `founding` exists anywhere in this suite**,
because §6.3's whole design is that founding is *verb-free*. So the gate named a module that the design
guarantees will never exist: **no post kind could ever satisfy it, no `founding_claim` Tag could ever be
deposited, `07`'s `place_found` could never fire, and every `kind: Ruin` placeholder node `07 §3.5`
declares was permanent dead weight.** The row existed and could not bind — which is strictly worse than
§13.4's "no rows yet", because a row that cannot bind looks like coverage.

The fix costs a clause. `head`/`governor` are **post kinds** (`04 §3`), a post sits at a **tier node**
(`04 §2`), and `target's parent tier node` is the same object the adjacent advance term already reads
one line down (`owner holds a charter edge to target's parent node`). Nothing new is introduced;
the gate now names two things that exist instead of one that cannot.

**Two properties worth naming.** (1) The fire effect is a **Tag append**; the *transition* stays
`07`'s, applied by the herald when `07`'s own gate next reads that Tag. **`09` never transitions a
place's kind** — it leaves behind the state `07` reads, which is `01 part 2 §9.3`'s no-latency rule
obeyed across a document boundary. (2) `target.kind == Ruin` is `required: true`, so a founding
project whose node someone else settles first **lapses** instead of firing into an occupied node —
§4.1's *generate-solvable-then-erode* doing real work rather than being asserted.

### 6.4 A **place-bound** kind declares itself — closing a registry ghost, and the suite's missing mass actor

**The defect first, because it is this document's and it was invisible.** §10.2's schema admits
`owner_binding: {entity_kind: place}`. But `am.declare` is a **surface** module: it requires a
post-holder whose `remit` names it and it costs **one point of `post.budget`** (§11). **A place holds no
post and owns no budget gauge**, and the three headless verbs advance, fire and lapse — none of them
declares. So a `place`-bound kind is declarable **by nobody**: a row shape the registry admits and no
path in the suite can ever instantiate. A **registry ghost** — the same failure as §6.3's gate, one
schema line further up.

**What the ghost was costing is much larger than a dead schema branch.** Across this suite, control of a
place changes *"by exactly two routes"* — `act.campaign` (force) and `04`'s appointment path
(`05 §4`, *"Nothing here transfers a place, ever"*) — **and `11` ships no unrest row at all** (a grep for `unrest`, `revolt`, `riot` over
`11_world_events.md` returns nothing). Both surviving routes are exercised by an entity that already
holds a post. **So no population can act, anywhere in the suite**, and the two governance patterns the
research corpus verified across four civilizations — **two-signal resonance** and **suppression-backfire**
(`research/governance/conflicts_power_struggles.md:32`, `:37`) — have no revolt-grade instantiation to
live in.

**The rule, and it is one rule.**

> **A project kind whose `owner_binding.entity_kind` is `place` AUTO-DECLARES at the accounting
> boundary, for every place whose `owner_binding.gate` holds, and LAPSES when that gate stops holding.**

**Why this is a gate and not a verb** — five costs it does *not* pay, each checkable:

| what it does not add | why not |
|---|---|
| a verb | **the surface budget is unchanged at one** (`am.declare`, §9). Nobody declares a rising; it is the world doing it |
| a budget point | a place has no post and no `budget` gauge. **The gate *is* the price** — its terms are state a place must actually reach, which is a costlier bar than one budget point, not a cheaper one |
| a module | it is **`am.declare` itself**, invoked by the herald at the boundary with `remit: []` and `budget: null` — the two fields a place has nothing to read for. Same resolver, same `tag.ambition` write leaf, same emission. The declaration write stays in the module that owns it and never leaks into `am.advance`, whose `state:` row is empty on purpose (§11) |
| a key type | `state.project_formed`'s optional `formation_cause` (G-29's field, adopted at §10.1) carries the gate, so an auto-declared project is **not causally anonymous** |
| an exemption | it is `am.lapse` under `01 §3.3`'s ordinary sweep. Nothing is immortal and nothing new decays |

⚠ **One thing it DOES cost, and it is the interesting one: a hysteresis band.** §6.2 argues a project
needs none because *fire is terminal*. **That argument does not cover auto-declaration**, which is a
genuinely **reversible pair** — the same predicate declares and un-declares — and `01 §2.3` requires a
declared band on exactly that shape or the kind strobes on and off every season. **A `place`-bound kind
must therefore declare `hysteresis:` on its `owner_binding.gate`, and it is the only place in this
document where a band is required.** Recorded here rather than discovered later, because §6.2's
terminality sentence would otherwise read as covering it.

**And it obliges one amendment to §6.2, stated rather than smuggled.** §6.2 forbids *"a consequence the
owner could not have reached through a module in some post's remit"* — a test that presumes the owner
**holds a post**, which a place by construction does not. For a place-bound kind the test reads: **the
consequence must be one some module already in this suite reaches.** The point of the clause is
preserved exactly — no power exists only for project-holders — and it becomes checkable for an owner
with no remit.

**The worked kind, built from the verified patterns and nothing else.**

```yaml
project_kind: rising
class: substrate                      # NEVER a menu item — no entity in the game can declare it
owner_binding:
  entity_kind: place
  gate: <settlement-tier place with a governance post>          # auto-declare / lapse predicate
  hysteresis: <band>                                            # REQUIRED — reversible pair, 01 §2.3
slots: [target]                       # target = this place's own governance post
advance_terms:
  # TWO-SIGNAL RESONANCE: both required. A bare grievance fizzles (conflicts_power_struggles.md:32)
  - {w: 1, required: true, term: "condition.order at or below <band>"}            # objective strain
  - {w: 1, required: true, term: "tag(place, Precedent, key=legitimating.*) exists"}  # sanction
  - {w: 1, term: "acceptance.legitimacy at or below <band>"}
  - {w: 1, term: "the strain band has held for >= 3 seasons"}          # §3.1's tag-age term kind
threshold: 3        horizon: 8        stall_ttl: 8               # SHAPE PROPOSALS
fire: {guaranteed: true, effect: post_revoke{post: <target>}}    # write leaf 3 — 04's pm.recall
residue: {on_fire: Precedent:rising.succeeded, on_lapse: Precedent:rising.suppressed}
```

**`required: true` on both signals is the whole of two-signal resonance** — an objective strain **and**
an independent legitimating tag, the Janissary-plus-fatwa shape, with the failure mode the research
names built in: strain alone never reaches threshold, because a `required` term that is false makes the
composite unreachable regardless of the other weights. **Nothing is special-cased**; the legitimating
tag is appended by whatever module observed the sanction, exactly as §3.2's failure marks are.

**Suppression-backfire, and the honest limit on it.** A faction suppresses by force (`act.campaign`
deposits into `condition.order`), the gate goes false, the project lapses, and §6.1's residue lands:
`Precedent:rising.suppressed`, durable. A **successor kind** then declares its gate at a *lower* strain
band and reads that residue as a `required: true` term — so suppression buys quiet now and a cheaper
rising later, which is the pattern `:37` describes. ⚠ **But `threshold` and every band live in a
static registry row, so nothing in this design can LOWER a threshold at runtime** — the effect is
reached by *a second row*, not by mutating the first. That is weaker than the research's wording and is
stated as such: **succession of kinds, not a re-armable threshold.** It also puts real weight on the
successor-graph acyclicity check §13.1 records as **not existing** — a rising→suppressed→rising cycle
is now a concrete way that gap bites, not a hypothetical one.

**What this buys, in one sentence.** Control of a place gains a **third route** — and it is the first
one in the suite that no post-holder exercises, which is what *mass actor* means.

---

## 7. Arcs are tag chains — the answer to "narrative arcs", with no narrative engine

**An arc is not an object.** It is a chain a reader walks:

```
Ambition tag (declared)                       provenance → Key K0
   └─ Precedent rows, and perceptual rows (Memory / Holding — §5), deposited by advances and
      obstructions,
      each with provenance → Ki,  each Ki citing its predecessors in causes[]
        └─ Precedent (fired)  or  Precedent (lapsed)                      provenance → Kn
```

Walking it needs **no new store, no join table and no arc object**: `01 §7.3` puts every edge in the
general store so *"`causes[]` chains cross relationship kinds without a join table"*, and `01 §3.3`
requires **non-empty provenance on every tag** so *"`Key.causes[]` is a biography rather than a
write-only chain."* **This document is the consumer those two rules were written for.**

### 7.1 One stream, projected — and what it buys, at the ratified strength and no higher

`narrative_engine_design_v2_churn.md §1` is ratified on this and is not restated: there is **one beat
stream**, and a character's story, a faction's campaign and the world chronicle are **projections** of
it, filtered by holon. **A project's arc is a projection filtered by the project's tag key** — a
query, not a subsystem. And `§4` is explicit about what its coherence invariants deliver: **a legible
chronicle, not a guaranteed satisfying plot.** This document claims the same and no more; what it adds
is that the chain is **walkable by construction**, every link a required field rather than a convention.

### 7.2 The named gap — the calibration set is gone

`00 §5.3` O-6, inherited: `narrative_engine_design_v2_churn.md:91` makes the 138 register arcs the
**validation/calibration set** and requires the compiled generator to reproduce them from their
trigger states. **`06_master_synthesis.md:565` prohibits the arc compile as specified precisely
because that corpus was evacuated.**

**So this is a gap, not a step.** Stated plainly: **this design has no calibration set.** The
template + binding-slot grammar and the anti-oatmeal defence stand on their own — they do not depend
on the corpus — but *"~13 shapes covers the space"* is currently **unmeasured and unmeasurable in this
tree**. Do not cite the ~13 figure as validated coverage; cite it as the ratified shape count whose
evidence is at the fork. Closing it needs a replacement corpus, which is a content decision.

---

**Continues in [`09_ambitions_and_arcs_part2.md`](09_ambitions_and_arcs_part2.md) — §§8–13:** the
no-latency constraint (**J-N**) that shapes §3 and the **J-O** exposure statement; what the player
actually touches and the long-range-agency argument; the registry rows and the key types that already
exist; the module contracts; and the property audit with its falsifiers.
