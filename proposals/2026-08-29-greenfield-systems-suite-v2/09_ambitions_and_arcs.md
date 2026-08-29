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

**Change B.** v1's diagnosis, from `ARCHIVED.md`: *nothing initiates.* Every module fired from a
vacancy, a directive or a player action, so the world could only respond. A Project is the object
that lets an entity **want something over time**, and it is **not a new stored primitive** — it is a
composition of `01`'s four.

*Emergent possibility lost if the project were cut:* **nothing in the world would ever pursue
anything, and every event would be an incident rather than a development.**

**This document adds one player verb and three headless ones.** Everything else it adds is
`substrate` in the sense of `00 §2.1`. Its surface table (§9) is three rows; its substrate table is
the rest of the page.

---

## Overrides

Listed, tiered and argued (`00 §5.3`). **A silent override is the corpus disease this suite exists
to stop**, and three of the five below are this document overriding *its own suite's draft* because
something already on disk beat it — *"may the best ideas win"* cutting against authorship.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-A1** | `01 §3.1`'s closing sentence — *"Six kinds, and the enum closes again at six"* | this suite's own `01` | **Seven.** A project declaration is a forward commitment; every one of the six records something **realized**. The two-part test `01 §3.1` itself specifies is run in §2.1, and the enum closes again at seven. This is `01`'s own procedure executed, not a bypass of it |
| **O-A2** | `01 §5.2`'s **`progress` Gauge** row — *"`progress` (v2) · any project owner"* | this suite's own `01` | **CUT. Progress is derived at read, never stored.** A stored progress is an aggregate over the project's advance terms, and **no aggregate is ever written** (`01 §2.1`, AU-1). This is structurally the same defect `01 §7.3` caught in v1's edge disposition, one document later. §3 |
| **O-A2b** | `references/module_contracts.yaml:343`'s `{name: "projects", bucket: clock, writable: true}` — canon stores project progress as a monotone 0→10 clock | **canonical contract** (`political_dynamics_keys_migration_v30.md:6` is `## Status: CANONICAL`) | A storage divergence, recorded rather than hidden. This design derives the same number, and **the ratchet case is reproduced exactly** (§3.2), so a port keeping canon's stored clock and one deriving it fire on the same season. Only the write leaf differs — and only one of the two obeys AU-1 |
| **O-A3** | `00 §9.2`'s three proposed key types **`project.declared` / `project.fired` / `project.lapsed`** | this suite's own `00` | **CUT as duplicates. Three of the four already exist and are registered** under ED-935: `mechanical.project_advanced` (`key_type_registry_v30.md:446`), `state.project_completed` (`:691`), `state.project_failed` (`:710`), all with `emitting_systems: [npc_behavior]` and live contract edges at `module_contracts.yaml:318-320, :333-335`. Only **formation** is missing, and `audit/2026-08-11-world-schema-gap-audit/01_gap_register_part2.md:281` (G-29) already proposed `state.project_formed` for it. §10 |
| **O-A4** | `systems/settlements/governance_play_redesign_v1.md:241` — *"every significant NPC **advances their ambition by 1**… unless the player or another actor intervened"* | **PROPOSAL, unratified** (`:3`) | Its **schema and its argument are adopted** (§5, §9); its **advance rule is replaced**. A `+1` per season on a stored counter is a timer whose only obstruction is a bespoke intervention. Here advance is a **read of world state**, so obstruction is *any* act that moves a term the project reads — and needs no verb of its own |

**Inherited, not re-decided:** `00 §5.3` O-6 — the **138-arc calibration set is evacuated**, so the
instruction at `narrative_engine_design_v2_churn.md:91` (*"the compiled generator must reproduce them
from their trigger states"*) is neither obeyable nor overridable. §7.3 states it as a **named gap**.

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
| **The arc-vector template + binding-slot grammar** (ED-IN-0011) | ratified canon | **derived from 138 real authored arcs**, not from a preference; and its anti-oatmeal defence — *specificity from binding at instantiation* — is exactly the property a project object needs and a naive generator lacks. Replacing a decomposition drawn from 138 arcs with one drawn from zero would be a worse proposal wearing my name. §1 | if the ~13 shapes could not express the four-verb lifecycle. **They can** — §1's slot table maps it with nothing left over |
| **The hook grammar** — *the script is the PREDICATE* (2026-08-18) | a Jordan ruling | it **solves scripting drift better than the alternatives**: the authored part is a *predicate over world state*, which cannot special-case an entity, and everything downstream stays emergent. Plus **three worked in-tree precedents**, so it is tested rather than proposed. §4 | if it forced authored content into code branches. **It does not** — §10.2 makes every hook a registry row |

**One place this document does extend past both, argued rather than assumed** (§3.1): the templates
and all three precedents are **unweighted** — a conjunction that must fully obtain, or a counter that
must reach `k`. This design generalizes to a **weighted sum of indicator terms**, subsuming both as
special cases and adding partial progress neither can express. **One formula replacing two shapes**,
which is the elegance criterion's distillation side — listed here rather than slipped in, because it
extends a ruled grammar.

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

---

## 2. A Project is a composition — the explicit table

**Nothing below is a fifth stored kind.** Every column right of the divider is `01`.

| part of a project | primitive it is | where |
|---|---|---|
| the **intent**, its target, its terms, its horizon | a **Tag** on the owner — `kind: Ambition`, `key: (project_kind_id, bindings)`, `ttl: horizon`, `provenance` required | `01 §3` |
| **who owns it** | any entity id — person, bloc, faction, place. **Ownership is the tag's `owner_ref`; there is no owner field** | `01 §3` |
| **who it targets, and who is bound into it** | entity ids in the tag's `value` payload, and **edges** where the binding is a relationship | `01 §7` |
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

Each `term_i` is a **predicate over readable state** — a gauge band, a form value, the existence of a
tag, a post's holder, an edge's state, a season index. **Nothing is stored, nothing is written, and
the resolver is `derivation`** (`00 §7`). This is AU-1 obeyed rather than asserted: a stored progress
counter is an aggregate over the terms, and `01 §2.1` forbids writing one.

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

---

## 4. The hook grammar — the script is the PREDICATE (Jordan, 2026-08-18)

> **"We can script narrative hooks and sequences so long as we don't script entire arcs. We've done
> it with the coup counter, for example."**
> — Jordan, 2026-08-18 (`proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:618`)

**Under the amended authority model this ruling is evidence, not a fence** (see the note after
`## Overrides`) — and it is adopted anyway, on merit, for a reason worth stating: **it is the only
formulation in the tree that stops scripting drift without banning authored content.** The authored
part is a *predicate over world state*, which by its shape cannot name an entity or an outcome; every
consequence of the predicate holding is emergent. And it arrives with **three worked precedents
already in the tree**, so nothing here is invented or untested.

| precedent | what IS scripted | what is NOT | the project row that expresses it |
|---|---|---|---|
| **Löwenritter coup counter** (`factions_personal_v30_infill.md:74-76`) | a private counter that **never decrements**; a **guaranteed** fire at threshold 3 at the next seasonal accounting; a fixed consequence | when it trips, who pushed it there, what the player does, everything downstream | §3.2 — ratchet terms over durable tags, `fire.guaranteed: true` |
| **Royal Assassination fuse** (`conflict_architecture_proposal.md:87`, `:89`; `## Status: CANONICAL`, `:2`) | one per campaign; fires at S8+; ***"succeeds when it fires — no attempt/failure variance"***; target fixed at start | the season within the window, the target, whether the player detects and averts it, the whole consequence arc | a single season-index term, `fire.guaranteed: true`, `resolver: gate` — **no roll** |
| **Baralta's Crown Claim** (`baralta_crown_claim_v30.md:26-40`; `## Status: DESIGN`, `:6`) | a scripted **conjunction of world facts**: Crown eliminated (Mandate 0 + Loyalty 0) **or** Royal Deposition; then per-claimant conditions — *Baralta alive + Hafenmark Mandate ≥ 4*, *Löwenritter Autonomy ≥ 3*, *CI ≥ 40* | whether those facts ever obtain, by what route, who else qualifies, who wins the resulting contest | §3.1 — equal-weight conjunction, `threshold = |terms|` |

> **The script is the PREDICATE. The arc is emergent.**

**Two permissions taken explicitly**, so a later reader does not read them as drift:

- **A guaranteed fire at threshold is allowed.** No attempt/failure variance is required, and two
  canonical precedents do exactly that. **Every project's fire is a `gate`, never a `d_sigma`** —
  `00 §6` principle 4 and `01 §2.2`'s reasoning verbatim: *the uncertainty was in getting the state
  there, and re-rolling at the threshold charges for it twice.*
- **A monotone counter is allowed**, and §3.2 takes it without an exemption to the geometric-decay
  default. `01 §5.1`'s decay law is untouched by this document.

**Note the second precedent's status caveat, carried honestly:** `baralta_crown_claim_v30.md:6` is
`## Status: DESIGN`, not canonical. **Two canonical precedents plus one design-tier one; the ruling
rests on the first two**, and this document's shape does too.

### 4.1 Generate solvable, let the world erode it

The same ruling's generalization (`:660-670`): *"Solvability is a generation-time precondition, never
an ongoing constraint."* Applied here: **a project kind's conjunction may be guaranteed reachable at
declaration and is never maintained against the sim.** A project whose target place is sacked, whose
key ally dies, or whose terms are made unreachable by another actor **lapses** (§6.1) — that is not a
bug in the hook, it is the texture, and it is why `lapse` is a real outcome rather than a consolation.

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

**Advance is a read of world state. Therefore any act that moves a term a project reads obstructs
it — with no obstruct verb, no obstruct module, and no knowledge of the project at all.**

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
   `supporters` and `obstructors` (`key_type_registry_v30.md:691-706`), and Procedure C already
   writes per-supporter and per-obstructor memory references with `salience: 4` and a
   `relationship_tag` (`political_dynamics_keys_migration_v30.md:219-256`). **That is `01 §3.1`'s
   Memory tag kind, arriving from canon** — the two designs converge without either knowing about
   the other, which is the strongest evidence either is right.

**`supporters` / `obstructors` are derived at fire**, not accumulated during the project: the set of
actors whose Keys appear in `causes[]` for the terms that moved. No stored list, no aggregate written.

### 5.1 Adopted from `governance_play_redesign_v1`, on merit (O-A4)

That document is a **PROPOSAL** (`:3`), not ratified, and its advance rule is replaced above. Three
of its ideas are better than anything this document would have invented and are adopted with credit:

- **The dossier's `ambition` + `trajectory` pair** (`:219-232`) — *"the two additions that make NPCs
  churn the world"* (`:237`). `ambition` is the Ambition tag; **`trajectory` is the method-escalation
  rule** (`if ambition blocked: lawful → factional → violent/covert`), and it needs no new machinery:
  a lapsed project's **Precedent residue is a declared advance term of the successor project kind**,
  so escalation is *lapse-and-redeclare*. That is canon's `generate_replacement_project`
  (`political_dynamics_keys_migration_v30.md:196-215`) expressed with zero additions.
- **Speccing for friction** (`:246-250`) — orthogonal convictions, **overlapping ambitions** (two
  owners with the same target force a third party to be kingmaker), cross-cutting relationships.
  Authoring guidance for the registry, not mechanism, and where the density comes from.
- **The four-conflict-surfaces argument** (`:264`) — one well-specified person generates a petition, a
  friction, an intrigue and an ambition. **This is the playing-surface budget's whole thesis** (`00
  §2.2`): depth from *which situation arrives and what it is entangled with*, never from menu breadth.

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
this document adds (§9).

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
reversible pair and `01 §2.3`'s hysteresis requirement does not apply. **State that explicitly**: it
is the one place in this suite where a threshold has no band, and the reason is terminality, not
oversight.

---

## 7. Arcs are tag chains — the answer to "narrative arcs", with no narrative engine

**An arc is not an object.** It is a chain a reader walks:

```
Ambition tag (declared)                       provenance → Key K0
   └─ Precedent / Memory rows deposited by advances and obstructions,
      each with provenance → Ki,  each Ki citing its predecessors in causes[]
        └─ Precedent (fired)  or  Precedent (lapsed)                      provenance → Kn
```

Walking it needs **no new store, no join table and no arc object**: `01 §7.3` puts every edge in the
general entity store precisely so *"`causes[]` chains cross relationship kinds without a join table"*,
and `01 §3.3` requires **non-empty provenance on every tag** precisely so *"`Key.causes[]` is a
biography rather than a write-only chain."* **This document is the consumer those two rules were
written for.**

### 7.1 One stream, projected — and what it buys, at the ratified strength and no higher

`narrative_engine_design_v2_churn.md §1` is ratified on this and is not restated: there is **one beat
stream**, and a character's story, a faction's campaign and the world chronicle are **projections** of
it, filtered by holon. **A project's arc is a projection filtered by the project's tag key** — a
query, not a subsystem. And `§4` is explicit about what its coherence invariants deliver: **a legible
chronicle, not a guaranteed satisfying plot.** This document claims the same and no more; what it adds
is that the chain is **walkable by construction**, every link a required field rather than a convention.

### 7.3 The named gap — the calibration set is gone

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

## 8. ⚠ J-N — the substrate supplies NO cross-season latency, and this is the constraint that shapes §3

**This is the one constraint on this page that is not a ruling and cannot be argued with. It is what
the code does.** The amended authority model (see the note after `## Overrides`) puts canon and
rulings in scope for override; it does not put the interpreter in scope. **Verified independently
against the tree for this document**, not taken on report:

| claim | verified at |
|---|---|
| `drain_tick` has **zero production callers** — the only callers are four lines in one test | `engine/substrate/keys.py:538`; `tests/valoria/test_key_substrate.py:336,361,376,388` (grep over all `.py` returns nothing else) |
| `next_tick` **raises `TerminationBreach`** if the queue is non-empty, so there is **no cross-season carry** | `engine/substrate/keys.py:593-599` |
| `schedule_emission` increments depth **only when already draining** | `engine/substrate/keys.py:525-536` |
| `DEFAULT_CASCADE_DEPTH_MAX = 0`, self-labelled provisional | `engine/cross_scale/echo_transport.py:102` |

> **The guard prevents cascades outright; it does not schedule them late.** One-hop-per-season latency
> is not a property this design has — it is a mechanism someone would have to build. Filed as open
> ruling **J-N** (`audit/2026-08-08-world-churn-audit/06_master_synthesis.md:532`, **held, not
> ratified** — `:4`).

**What this forbids in this document, and what it forces instead:**

| forbidden | what §3 does instead |
|---|---|
| a project reacting to a Key by emitting a Key that lands next season | there is no such transport |
| a project that is *posted to* — "an actor's move advances my project" | **a project advances because the world *IS* a certain way at the accounting boundary.** It reads state |
| accumulating advance deposits during the season for next season's fire | progress is recomputed from current state each boundary; nothing accumulates in transit |
| a stall counter incremented by an emission | stall is the Ambition tag's `ttl`, and `ttl` decays on **elapsed time**, a pure function (§6.1) |

**This is not a limitation this design works around; it is the reason §3 is a derivation.** A project
that advanced by receiving something would need the transport. A project that advances by *looking*
needs only the boundary, which already runs. **This design therefore requires no latency to be built
and is not blocked on J-N.** J-N is the ruling that would *permit* an alternative, not one this page
waits on; if it rules for reactive chains, §3 and §6 are what to revisit and nothing else here moves.

### 8.1 ⚠ J-O — what this document does and does not lean on

`06_master_synthesis.md:533` files **J-O**: *does the Key mesh deserve promotion from telemetry spine
to churn engine at all*, the alternative being **Keys as an append-only telemetry and causality log
with churn driven at the boundary directly.** Stated so the affected parts are identifiable if J-O
rules the other way:

| depends on Key **consumption**? | survives a "telemetry only" ruling? |
|---|---|
| `am.advance` / `am.fire` / `am.lapse` — **all three read state, consume nothing** | **yes** |
| the arc chain (§7): `Tag.provenance` → Key, `causes[]` | **yes** — that is telemetry and causality, exactly what the alternative keeps |
| the emission side (`mechanical.project_advanced`, `state.project_completed`, `state.project_failed`) | **yes** as a log |
| the `consumes: []` lists in §11 — **already empty** | **not applicable** |
| the Slate candidate hand-off (§9) — if `10` is wired as a Key consumer rather than a boundary read | **the one exposure**, and it is `10`'s, not this document's |

**This document is close to robust under J-O**, and that is a property of §3's derivation, not luck: a
design that advances by reading state does not care whether the mesh is a churn engine or a log.
**This suite takes no position on J-O.**

---

## 9. What the player actually touches

**One verb. Three read-only affordances.** Everything else on this page runs headless.

| surface | what the player is asked | how often |
|---|---|---|
| **`am.declare`** — commit to a project of their own | choose a project kind from those their posts' remit makes eligible, and bind its slots. Costs **one budget point** | at most once a season, usually far less |
| the **band** of a project they own or can see, and its **published advance terms** | nothing — a read | when the item is on screen |
| a project's **arc chain** — *what has this been, and who moved it* | nothing — a read, on demand, never pushed | on demand |

| what the player never touches |
|---|
| any NPC's, bloc's or faction's project — they are **substrate** and are experienced only as situations arriving on the Slate |
| `am.advance`, `am.fire`, `am.lapse` — all three are boundary-run |
| a project's **threshold**, its **progress number**, or any **forecast** of when it will fire (§3.3) |
| an **obstruct** verb — there is none. Obstruction is any existing verb that moves a term (§5) |

**Substrate objects here: 1 tag kind · 1 registry block of project kinds · 4 verbs of which 3 are
headless · 0 new gauges · 0 new entity kinds. Surface: 1 verb, 3 reads.** The ratio is the right way
round (`00 §2.3` point 4).

### 9.1 The payoff — long-range agency from a small verb set

The answer to the obvious objection that `00 §2.2`'s single-digit verb budget makes a shallow game.

**Every other verb in this suite resolves inside one season.** An appointment, a directive, a contest,
a response to a Slate item — each is a move whose consequence lands now. A player with only those
verbs is playing a game of *reactions*, however good the reactions are. **`am.declare` is the only
verb whose horizon exceeds one season**, and it converts the entire existing verb set into
instruments of a plan the player chose:

1. **It buys reach without buying breadth.** Declaring does not add options; it makes the options the
   player already had *mean something over time* — every appointment now either serves the ambition
   or does not. **One verb, and the whole existing surface acquires a second axis.**
2. **It makes the world's ambitions legible as opposition.** Because NPC, bloc and faction projects
   use the identical mechanism, the player's ambition and the world's are the same kind of thing and
   collide on the same terms. That is `governance_play_redesign_v1:15`'s P3 — *"the world moves
   whether or not the player does"* — made structural.
3. **It is what makes obstruction dramatic rather than administrative.** A rival's project is not a
   status bar; it is the reason the thing you did for your own reasons three seasons ago mattered.
4. **It is the cheapest possible depth.** One verb, one tag kind, one registry block, three headless
   boundary passes. Measured against the delta brief's test — *could this be removed from the
   player's hands entirely and still change the game?* — the **NPC** half answers yes and is
   substrate; only the player's own declaration answers no, and only it is surface.

**Every verb must justify its slot against a verb not proposed** (`00 §2`). `am.declare` is justified
against **`am.obstruct`**, **`am.abandon`** and **`am.reprioritise`** — all three considered, all
three cut (§12). Obstruction is already every other verb; abandoning is letting the `ttl` run out,
which is a decision the player makes by *not acting*, which is the better version of the choice; and
reprioritising is what declaring a different project already is.

---

## 10. Registry rows and key types — three of the four already exist (O-A3)

### 10.1 The key types: what the tree already has

**`00 §9.2` proposed `project.declared` / `project.fired` / `project.lapsed`. Three of those four
moments are already registered types under ED-935**, with live contract edges, and re-declaring them
would be exactly the duplication `00 §1` names as the under-distilled failure.

| verb | key type | status | citation |
|---|---|---|---|
| `am.advance` | **`mechanical.project_advanced`** — payload `project_id, progress_before, progress_after, project_domain` | **registered** (ED-935) | `key_type_registry_v30.md:446-458`; `module_contracts.yaml:333` |
| `am.fire` | **`state.project_completed`** — payload `project_id, project_domain, completion_effect, supporters, obstructors, goal_short` | **registered** | `key_type_registry_v30.md:691-706`; `module_contracts.yaml:335` |
| `am.lapse` | **`state.project_failed`** — payload `project_id, failure_mode, seasons_stalled` | **registered** | `key_type_registry_v30.md:710-723`; `module_contracts.yaml:334` |
| `am.declare` | **`state.project_formed`** — **DOES NOT EXIST** | **the gap**, already found and proposed | `01_gap_register_part2.md:281` (G-29), `BLOCKED on G-17` |

**G-29's own words** (`:281`): *"no key type exists for project or ambition FORMATION … so the moment
an NPC forms a new goal is generated in-process and announced to nothing."* Its proposal —
`state.project_formed`, family `state_transition`, payload `npc_id, project_id, project_domain,
goal_short`, optional `prior_project_id, formation_cause` — **is adopted as-is**, generalized only in
that `npc_id` becomes an entity id, because a bloc and a faction declare projects too.

⚠ **Nothing is appended here.** `00 §8` P0-1 blocks any key-type append until
`references/rendering_dispositions.yaml` exists; G-29 blocks it additionally on G-17. **Both blocks
stand.** This section's contribution is that the blocked work is now **one type instead of four**, and
`optional_payload_fields.prior_project_id` is precisely what §5.1's lapse-and-redeclare escalation
needs — which is convergent evidence that G-29's proposal was right before this design existed.

**One adjacent defect, recorded not fixed** (found while verifying): `module_contracts.yaml:1418`
still annotates all three registered types `[unreg]`, while `:362` and `:364` record that ED-935
registered them on 2026-06-14 — **the file contradicts itself about ED-935.** G-29 found the same.
An IN-lane contract-truth item, not this suite's to fix, and nothing here depends on it.

### 10.2 The registry rows

`00 §9` holds the whole suite to **two new registry files**, and this document adds **none**. Project
kinds are a **block** in `references/content_registry.yaml`:

```yaml
project_kinds:
  - id: <kind id>                      # an arc-vector TEMPLATE (§1)
    class: substrate | surface         # surface ONLY for kinds a player may declare
    owner_binding: {entity_kind: person|bloc|faction|place, gate: <predicate>}
    slots: [target, terms]             # the ratified binding slots (:80)
    advance_terms:                     # each: a predicate over READABLE STATE. No RNG. No Key. (§8)
      - {w: <int bp>, term: <predicate>, required: <bool>, ratchet: <bool>}
    threshold: <int bp>                # HIDDEN — a trigger (01 §8)
    bands: [(<bp>, <label>)]           # PUBLISHED — what a reader sees
    horizon: <seasons> | null          # null permitted for ratchet kinds only (§6.1)
    stall_ttl: <seasons>               # the Ambition tag's ttl; canon's default is 8
    fire: {guaranteed: <bool>, effect: <one of the four write leaves>}   # a GATE, never a roll
    firing: true | false               # false = a declared non-firing residue (§1.1). COUNTED.
    residue: {on_fire: <tag>, on_lapse: <tag>}
    disclosure: [{of: progress, inputs: published, presentation: band, trigger: hidden}]
```

**Adding a project kind — and therefore an arc shape — is data.** `00 §6` principle 3.

---

## 11. Module contracts

In `00 §7`'s shape. `consumes:` is empty on all four, which is §8's constraint expressed in the
contract rather than promised in prose, and is why §8.1 can claim robustness under J-O.

```yaml
# ALL FOUR: parent: ambitions · scales: all four · tier: null · form: []
#           consumes: []   <- J-N (§8): nothing is ever posted to a project
# The three below `am.declare` are boundary-run by the herald (01 part 2 §9.2, W-5), so all three
# carry remit: [] and budget: null — they are not invocable by any post, including the player's.

- module: am.declare
  class: surface               # the ONLY surface row in this document
  resolver: gate               # eligibility + the remit/caste gate. Declaring is never a roll.
  remit: [head, governor, minister, commander, envoy]       # clerk cannot declare; §9
  budget: {gauge: post.budget, cost: 1}
  emits: [{type: state.project_formed, terminal: false}]    # BLOCKED on P0-1 + G-17 (§10.1)
  state: [{name: tag.ambition, bucket: tag, writable: true, owner: substrate.ledger}]
  transitions: []
  disclosure: [{of: tag.ambition, inputs: published, presentation: exact, trigger: hidden}]

- module: am.advance
  class: substrate
  resolver: derivation         # progress is DERIVED (O-A2). Nothing writes it.
  emits: [{type: mechanical.project_advanced, terminal: false}]   # on a BAND crossing only (§3.3)
  state: []                    # a derivation owns no state — this row is empty on purpose
  transitions: []
  disclosure: [{of: progress, inputs: published, presentation: band, trigger: hidden}]

- module: am.fire
  class: substrate
  resolver: gate               # guaranteed at threshold; no attempt/failure variance (§4)
  emits: [{type: state.project_completed, terminal: false}]
  state: [{name: tag.ambition, bucket: tag, writable: true, owner: substrate.ledger}]  # -> residue
  transitions: [<whichever the kind's fire.effect names; each declared in form_registry.yaml>]
  disclosure: [{of: tag.ambition, inputs: published, presentation: exact, trigger: hidden}]

- module: am.lapse
  class: substrate
  resolver: gate               # ttl expiry / required-term unreachability. Reads elapsed time only.
  emits: [{type: state.project_failed, terminal: false}]
  state: [{name: tag.ambition, bucket: tag, writable: true, owner: substrate.ledger},   # swept
          {name: tag.precedent, bucket: tag, writable: true, owner: substrate.ledger}]  # residue
  transitions: []
  disclosure: [{of: tag.precedent, inputs: published, presentation: exact, trigger: hidden}]
```

**`am.fire` is the only module in this suite whose `transitions:` list is supplied by data.** That is
deliberate and it is the auditable seam: the set of form transitions a project can cause is a grep
over one registry column, per `00 §7`'s rule that a module may only transition a field it declares.

### 11.1 The candidate hand-off — this document produces, `10` ranks

Every emission above is a **Slate candidate**, and this document **does not rank it**.
`narrative_engine_design_v2_churn.md §4`'s **Light Function is RATIFIED (ED-IN-0011)** and
[`10_the_slate_and_salience.md`](10_the_slate_and_salience.md) owns the surfacing side. It is in scope
for override under the amended authority model — **but not by this page**, which is a producer of
candidates and would be re-deriving a ranking function it has no reason to touch. Three bindings this
document holds itself to, reproduced rather than paraphrased:

- **Strictly selective / subtract-only** — the light rations among candidates the churn produced and
  can never inject content, accelerate a clock or emit a pressure-bearing Key (`:197-204`). **A
  project must therefore never be advanced, delayed or fired by the light.** Salience is downstream of
  `am.advance`, never an input to it.
- **Casting is severed from forecast** (`:205-208`) — slate entry keys on **realized state** only. So
  a project's candidate carries `durability`, `tie-proximity`, `identity-touch` and its holon, and
  **never** how close it is to firing (§3.3).
- **No salience or forecast function is designed here.** If `10` needs a light term this document does
  not supply, that is a ruling request, not an edit to this page.

---

## 12. What was cut

| Considered | Verdict | Why |
|---|---|---|
| a **Project entity kind** (a seventh) | **rejected** | it would need its own store, sweep, provenance rule and disclosure contract — all of which Tag already has. §2 |
| a stored **`progress` Gauge** | **CUT** (O-A2) | an aggregate over the advance terms; no aggregate is ever written. §3 |
| a **`+1` per season** advance rule (`governance_play_redesign_v1:241`) | **replaced** (O-A4) | a timer whose only obstruction is a bespoke intervention. §5 |
| an **`am.obstruct`** verb | **rejected — the document's best cut** | obstruction is *any* verb that moves a term a project reads. The verb would make obstruction intentional-only and put a project on the player's menu. §5 |
| an **`am.abandon`** / **`am.reprioritise`** verb | **rejected** | abandoning is letting the `ttl` run out, which the player already does by not acting; reprioritising is declaring a different project |
| a **project→project dependency graph** | **rejected** | a predecessor's residue is a Precedent tag, already a legal advance term; the graph is derived by walking `causes[]`. §7 |
| an **arc object**, store or scheduler | **rejected** | §7 — an arc is a projection of the one beat stream. A second store would fork save/replay and the causal graph |
| three new key types (`00 §9.2`) | **CUT** (O-A3) | three of the four moments are registered already. §10.1 |
| a **cross-season advance carry** | **rejected as non-existent, not as unwanted** | §8 — the transport is not in the tree (**J-N**) |
| a **project-specific salience term** | **rejected** | `10` owns the light. §11.1 |
| **decay on `progress`** | **rejected for ratchet kinds** | §3.2 — monotonicity comes from the append-only tag ledger, not from an exemption to `01 §5.1` |

---

## 13. Property audit

**Scope, and the honest limit. Nothing in this document rolls.** `am.declare`, `am.fire` and
`am.lapse` are **gates**; `am.advance` is a **derivation**. Per the methodology's own rule — and per
`01 part 2 §13`'s precedent — **no N/R/S/E verdict is manufactured for a module with no draw.** The
two properties that do apply are given, then every loop with its bound and every gate with what it
reads. Above all of it sits `00 §0.1`: **a resolution-scoped audit cannot ask whether a design
expresses the game.**

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass, with two of the three bounds arithmetic** | progress is a weighted sum of indicator terms, so it is bounded above by `Σ w_i` **at declaration time**, from the row alone, with no campaign run. Live projects per owner are capped at `PROJECT_CAP` *(a shape proposal)*, so the boundary's cost is `owners × PROJECT_CAP × MAX_TERMS` — linear and declared. Monotone response holds for ratchet terms structurally (§3.2) and is **deliberately absent** for the rest, which is the design: a project can slide back because someone took the ground |
| **P-v** right engine | **pass** | three gates and one derivation. **Fire is a gate on purpose** (§4): the uncertainty was in getting the world there, and re-rolling at the threshold charges for it twice. Nothing here is a `d_sigma` and nothing here is an `accrual` — the accrual reading is exactly the stored counter O-A2 cuts |

### 13.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| declare → advance → fire → consequence changes world → a term of another project moves → that project advances | **`PROJECT_CAP` per owner and the `ttl` horizon.** Every project ends: it fires (terminal) or it lapses (swept) | **unmeasured.** Campaign-reachable, so measurable with a control — `tools/balance_oracle.py` is the instrument, and this is a campaign-level change so both arms genuinely differ |
| lapse → Precedent residue → an advance term of a successor project kind → declare | **the residue is a durable tag under `01 §3.3`'s dedupe**, so it refreshes rather than stacks; and each successor consumes a `PROJECT_CAP` slot | **unmeasured, and this is the loop most likely to run hot.** §5.1's escalation ladder is finite by declaration (`lawful → factional → violent/covert`), but nothing in the substrate enforces that a kind's successor chain terminates. **A registry check should require the successor graph to be acyclic**; it does not exist |
| ratchet terms → progress → fire | **terminating by construction**: ratchet terms are monotone, threshold is fixed, fire is terminal | **bounded** — the only loop here with a proved bound, and it is the coup counter's own property, not this design's |
| project fires → Slate candidate → player attention → player acts → a term moves | **the scene budget** (`10`), and the light is **subtract-only** (`churn:197-204`) so it cannot accelerate a project | **unmeasured**, and the severance is `10`'s to enforce, not this page's |
| obstruction → progress falls → owner's method escalates → new obstruction | **the `ttl` horizon and `PROJECT_CAP`** | **unmeasured** |
| a Key-driven advance cascade within a season | **does not exist.** `DEFAULT_CASCADE_DEPTH_MAX = 0`, and `consumes:` is empty on all four modules (§8, §11) | **not a loop today.** If **J-N** rules for reactive chains this becomes a real loop with no bound yet |

### 13.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| `am.declare` eligibility | the owner's posts and their `remit`; the kind's `owner_binding`; one budget point | the kind is not in the option set — **an absence, not a penalty** (`01 §4.3`) |
| `PROJECT_CAP` | the owner's live Ambition tags, counted | declaration unavailable until one ends |
| `am.fire` threshold | the derived progress against the hidden threshold — **state only, never a received Key** | no fire; the project stays live |
| `am.lapse` horizon | the Ambition tag's `ttl` against the season index — **elapsed time, a pure function** | no lapse |
| `am.lapse` unreachability | any `required: true` term that is permanently false | no lapse |
| `firing: false` | the registry row | the kind is never instantiated, and is **counted** in the honest-residue ledger (§1.1) |
| successor-graph acyclicity | **nothing — this check does not exist** (§13.1) | **an open gap, stated rather than assumed** |

### 13.3 Falsifiers — a claim with no falsifier is not a claim

| claim | falsifier |
|---|---|
| **No aggregate is written.** Progress is derived (O-A2) | a test asserting no module contract in this suite declares a `state:` row named `progress`, and that no write path deposits into one. **Load-bearing on the game:** it is `01 §2.1`'s write rule, and violating it is the defect `01 §7.3` caught in v1 |
| **A project reads state and consumes nothing** (§8, J-N) | a test asserting `am.*` contracts have empty `consumes:`, and a seeded-campaign assertion that no project's progress changes within a tick in response to an emission. **Load-bearing:** if it fails, the design is resting on a transport the tree does not have |
| **Fire is a gate, never a roll** (§4) | a test asserting no `am.*` module has `resolver: d_sigma` and that no fire consequence reaches `roll_pool` |
| **No forecast is published** (§3.3) | `01 §8`'s falsifier extended: no key type emitted here carries a field whose value is a **future** state, and `mechanical.project_advanced` carries only `progress_before` / `progress_after` — both crossings already made |
| **No entity or outcome is special-cased** | a grep asserting no project kind's `owner_binding`, `advance_terms` or `fire.effect` contains a literal entity id. **This is the one falsifier that cannot be run yet** — there are no rows |
| **Monotonicity needs no exemption to the decay law** (§3.2) | a test asserting no gauge declared by this document exists at all (it declares none), and that every ratchet term resolves to a tag-existence predicate on a `ttl: None` tag |
| **Obstruction needs no verb** (§5) | a seeded campaign in which a project's progress falls after an unrelated actor's action, with no module having named the project. **If it never happens, the advance terms are reading state nobody else touches, and the projects are timers after all.** This is the weakest-supported claim on the page and this is how to break it |
| **Every project ends** (§6.1) | a seeded campaign assertion that no Ambition tag survives `max(horizon, stall_ttl)` seasons past its last band crossing, and that live projects per owner never exceed `PROJECT_CAP` |
| **~13 template shapes cover the arc space** | **NOT CLAIMED.** The calibration corpus is evacuated (§7.3). Do not cite the figure as validated coverage |

### 13.4 Reachability, in both directions

The same bar `11` gets, a **content** obligation on the registry rather than a code check. A kind
whose conjunction has **never held** in a seeded campaign is decoration; one that **fires for most
owners most seasons** is weather; and one that is **declared and always lapses** is worse than
either, because it costs a budget point and a `PROJECT_CAP` slot and returns only a residue.

None of the three is checkable until rows exist, and **none of them is checkable at all without the
calibration set §7.3 says is gone.** That is the honest state.
