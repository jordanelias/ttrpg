# VALORIA — THE IDEAL DESIGN, ENLARGED BY WHAT THE TESTING TAUGHT

## Status: PROPOSED (2026-08-31). **This document supersedes PR #342's seventeen-document suite
## (`proposals/2026-08-29-valoria-from-scratch/`) and the palimpsest that reviewed it
## (`proposals/2026-08-31-ideal/00_THE_SHAPE.md`). Read this one file.**
## Nothing here ratifies on merge. Nothing here has executed. §0.2 of `CLAUDE.md` applies in full:
## **done means it runs, and none of this runs.**

---

## §0 · HOW TO READ THIS, AND WHAT IT IS

**What it is.** The from-scratch design of Valoria — one actor, two structures, three signatures, one
resolver — **enlarged by four objects that testing against 56 NPC seasons and 83 arcs showed the
design needed**, with the repairs that testing also demanded. A reader who has never seen #342 can
read this file alone and have the whole design.

**What it is not.** Not a reconciliation, not a fix-list, not a review. The corrections are folded
in; they are not carried alongside. Where the earlier work is wrong, this document simply says the
right thing and records the change in §17.

**One rule lives in one place.** Every rule below is stated exactly once and cross-referenced by
section number thereafter. If a rule appears twice, that is a defect in this document.

**Citation discipline.** Where a claim rests on a line of #342, the citation is `doc:line` against
`proposals/2026-08-29-valoria-from-scratch/`, read directly, never through another document's
quotation of it. `proposals/2026-08-31-integration/09_citation_ledger.md` is the verified fact base
and wins over any other document in the review suite, including this one's sources.

**Two words about evidence, before any of the design.**

- **No rates about play appear in this document.** Both testing corpora — the NPC-season matrix and
  the arc set — are hand-assembled and elite-heavy. The arc tally is an upper bound on a
  hand-selected set, not a sample of anything. **Two counts appear in this document — §15.9 and
  §17.3 — and both are scoped, labelled and lane-1 only.** Neither is used as a base rate, and there
  are no others. *(An earlier wording of this bullet said counts appear only in §17, which was false
  inside its own section; C-23.)*
- **Every R-line in this document is conditional on L-4, the unanswered playable-seat list**, because
  necessity is measured against the seats a player can actually occupy and that list does not exist.
  §8's enlargement is additionally conditional on **D-2, the act economy** (§6.1), which is the
  largest open ruling in the design. The conditions are stated where they bite; they are not
  answered here and this document does not pretend they are.

### §0.1 · Index

| § | what it owns |
|---|---|
| **1** | The substrate — one actor, two structures, three signatures |
| **2** | The person |
| **3** | Knowledge, claims, and the view |
| **4** | The rungs, and the five owners |
| **5** | The resolution surface — one roll, one obstacle, one contest |
| **6** | The season — seven phases, three write classes |
| **7** | **The calendar, and CONVENING CONDITIONS** *(enlargement 1)* |
| **8** | **The up-stroke — petition, office, standing, the agenda, expiry, multi-petition** *(enlargement 2)* |
| **9** | The down-stroke — dispensation, executors, compliance, reports-as-claims |
| **10** | **Matter, the commons, and option removal** *(enlargement 3)* |
| **11** | **The transfer act** *(enlargement 4)* |
| **12** | Argument and the sitting |
| **13** | No fallback · coincidence · the epistemic payoff |
| **14** | What is refused — the fourteen rows, walked for every new object |
| **15** | Stated limits |
| **16** | Live choices for Jordan |
| **17** | Appendix — what the testing changed, and the relay's change log |

### §0.2 · The design in one page

There is one kind of actor: **a person**. There are two structures over persons: **containment**, a
strict single-parent tree, and **alignment**, an unconstrained set system in which a faction is a
proposition plus a commitment map at any scale. Three signatures carry everything: `choose` takes no
world, `resolve` takes no person, `witness` is per-person and a consensus broadcast is a type error.
There is one resolver, one roll, one obstacle. Containers hold a stake, a judging set and standing
dates; offices hold a remit and their own dates; **nobody** holds an aggregate. Knowledge lives only
in ledgers.

**The four enlargements are one structural promotion seen from four sides.** The standing date stops
being one object among many and becomes the design's spine. A **convening condition** (§7) causes a
date to exist. A **petition** (§8) addresses an office that will answer at one. A **lost option**
(§10) and an **unpaid wage** (§11) are what people convene *about*. And the organising principle
underneath all four is a refusal: **there is no fallback** (§13) — if no person acts, the thing does
not occur.

---

## §1 · THE SUBSTRATE

### §1.1 One actor

Persons act. Nothing else does. Containers do not decide, factions do not decide, settlements do not
decide. Where the setting says *the Crown resolved*, the substrate says: a person holding a post,
holding a view, chose an act, and other persons complied or did not.

### §1.2 Containment is a tree, single-parent on purpose

**Person → Hearth → Community → Settlement → Territory → Province → Realm**, extended upward or
sideways as the world needs. Every person has exactly one parent hearth; every hearth exactly one
community. A person's **address** is their path to the root.

The setting supplies an immediate counterexample — an Einhir smith belongs to the Kettlemakers *and*
to the hamlet outside the wall — and multi-parent containment would state it in one line. It is
refused, and this refusal is the derivation everything else rests on. **If a person can be contained
twice, divided loyalty becomes a set membership and evaporates.** Forcing the second belonging into
alignment makes it a commitment that can be concealed, betrayed and punished for. That friction is
the game.

- **Cut it and you lose:** a defined "one rung up", and therefore any meaning for filtering,
  jurisdiction, or being an outsider anywhere.

### §1.3 Alignment is a set-system with no tier field

A **faction** is a proposition plus a map from persons to a degree of commitment. That is the entire
object. Two brothers who have sworn to burn out the reeve are a faction; so is the Church of Solmund.
Membership is per-person, may be secret, and is held at a degree.

**Scale is derived and gates nothing.** Rolling member addresses up the tree yields `presence(f, n)`,
`density(f, n)` and `footprint(f)` with no declaration anywhere. Capacity to act at a node is not a
property of size; it is the question *does this faction hold a person who can act there* — which
routes through persons, and is a query over members with an address inside the node, each of whom must
be individually `eligible` (`07:180-182`). No act is unlocked or forbidden by a faction's size and no roll takes it as a
term. Scale is not inert, though: §13's revolt comparison reads how many people are actually
committed at a node against what the coercive apparatus there can hold.

**And the profile is never read from true state.** There are two profiles and only one is readable:
the **true** profile, computed from actual memberships, which **nobody** may read; and an
**estimated** profile, computed from *one person's own claim ledger*, readable by that person inside
their own view. Every observer holds a different estimate of the same faction. Underestimation is the
default, produced by the same incomplete ledgers that produce everything else.

**One membership operation:** `commit(person, faction, Δdegree)`. Degree to zero is departure. A
schism is a subset whose commitment migrates to a rival proposition; a merger is members of A
committing to B; growth into a national body is many commits. There is no merge, split, promote, or
found-at-size, so there is nothing left to be discontinuous.

### §1.4 The three signatures

```
choose  : (Person, View)   -> Act        # no world argument. ever.
resolve : (Acts,  World)   -> [Event]    # no person argument.
witness : (Person, Event)  -> [Claim]    # the only bridge, and it is per-person
```

These are the enforcement mechanism, and they work by what they omit.

- **`choose` has no `World`.** Not a masked world, not a read-only world, not a world behind an
  accessor. Omniscience is not something a reviewer must catch; it is something an author cannot
  write.
- **`resolve` has no `Person`.** The world does not know who is asking. This is what keeps the
  resolver from acquiring per-actor special cases, which is how scripting drift begins.
- **`witness` takes the person first**, and there is no signature accepting a collection of persons
  and one event. **Consensus broadcast is a type error.**

`View` must be a distinct type from `World`, with no coercion, no shared supertype, and no field of
`View` holding a `World`. If a `View` can be built from a `World` by masking, someone eventually
masks nothing. **`View` is assembled, not filtered** (§3.3): absence of a claim produces absence in
the view, never a widened interval, because a widened interval is uncertainty and the design needs
ignorance.

⚠ **Plurality note.** #342 ships three spellings of these signatures — `11:57-59` singular,
`01:212-216` singular, `09:819-821` proposing plural. **This document uses the plural `resolve(acts,
world) -> events`**, because one season's acts are resolved together and conflict between them is a
first-class case (§6.3). That is a ruling, not a transcription.

---

## §2 · THE PERSON

Six fields, derived by asking which property becomes unreachable without each.

| field | why it cannot be cut |
|---|---|
| **Address** | without it there is no rung, no jurisdiction, no aggregation |
| **Marks** | ascribed, publicly-read attributes — heritage, caste standing, guild grade, house name, Church standing, visible Thread sensitivity. **These are what make the same act by two persons produce different results.** Without marks, caste is a difficulty slider rather than a structure |
| **Capability** | aptitudes and practices — the pool the resolver rolls (§5.1) |
| **Stance** | one table, `referent → attitude`, referents being persons, factions, propositions and places. Feelings and beliefs-about-value live in the same table because the same routine reads both |
| **Memory** | the claim ledger (§3) |
| **Ties** | ordinary contacts, plus **Knots** — a person's few deep bindings, typed differently because a Knot is a channel with bandwidth. The setting gates Knots on Thread Sensitivity, so roughly half the peninsula cannot form one: every formal institution gates Southern Einhir *out*, and the deepest informal channel gates them *in*. That asymmetry is deliberate; do not later "fix" it |

**Personality is two scalars inside the stance table** — *credulity* (how far a telling moves me) and
*obstinacy* (how hard my existing stance resists contradiction) — and nothing more. A trait that
duplicates a stance is a second copy that can disagree with the first.

**Needs are not a field; they are computed each tick**, and they do not all read the same thing:

| need | reads |
|---|---|
| subsistence — the larder against the mouths | **the world.** You feel hunger whether or not anyone told you |
| standing — regard among your siblings-in-container | **the world.** Their faces are in front of you |
| commitment — a faction proposition you hold, unsatisfied | **the view.** You must believe it unmet |
| exposure — what a dispensation's terms do to your options | **the view.** You must have heard of it, in whatever version reached you |

So needs are never stale relative to the person's view and are **supposed to be stale relative to the
world.** A fisher whose Duke signed a treaty three days ago has no changed need until the crier
reaches him, and if the crier's version is distorted, his need is computed from the distortion.

**A person with no office can still act.** Action eligibility never consults office. Every act is
offered to every person; office changes only whether your decision *binds others*, and marks and
regard change only your odds. **An untrained attempt is legal and is just a small pool** (§5.1);
practice rank *adds verbs* rather than constituting the list; a postless fisher's shortfall arithmetic
is identical to a Duke's. **The design's low end is right and this document does not touch it.**

**Populations are persons at coarse fidelity.** Persons sharing an address, marks and stance are held
as a **cohort** — one record, a weight, evaluated once, applied to all. A cohort **individuates** when
an event names one of its members or its internal stance spread exceeds the point where one answer is
honest. One type, not two: if a cohort were a different type, every mechanism would be written for one
and not the other and the design would acquire an elite-only politics by accident.

**Individuation has an inverse, and it is a design principle rather than a budget cap.** A person
re-merges into a cohort when they hold no Knot, no office, no live petition, and no other person's
ledger names them.

> **A person persists exactly as long as somebody remembers them.**

---

## §3 · KNOWLEDGE, CLAIMS, AND THE VIEW

### §3.1 The claim

```
Claim = (subject, predicate, value, when, source, confidence, visibility)
```

**`when` is a mandatory closed interval and it is universal, never existential** — a claim asserts its
value held *throughout*. If intervals were existential, denial would need a universal over the
complement and the engine would carry two claim logics with two collision rules.

**Collision.** Claims collide iff same subject, same predicate form, same arguments, intersecting
`when`, incompatible values. Collision is computed at deposit time, in one ledger at a time.

**The predicate vocabulary is CLOSED; the referent space is OPEN.** Claims support exactly three
operations — collision, entailment, relevance — and all three are functions of the predicate's *form*.
Open forms mean each operation is authored per form, which is a scripting language with a rules engine
attached. Expressiveness lives in the arguments, and the argument space is the world's own object
namespace, which is open because the world generates persons, places, factions and propositions
continuously.

**Subjects include other claims.** `SAID(Aldwin, C, season 12)` is a claim, which is what makes the
lie a first-class object rather than a flag.

### §3.2 Corroboration fails closed

Sources are `firsthand(event_id)`, `told_by(person, handle)`, `inferred(claim_id…)`, or
`firsthand_via_knot(event_id)`. There is no null source, and **`witness` is the only operation that
mints a root token.** A Knot deposit *reuses* the originating event's id, so five partners feeling one
rupture supply one token — exactly as five men repeating one rumour supply one.

### §3.3 View assembly, and the one multiplication that is all of motivated reasoning

```
view(person, question) -> at most K claims
K = 7 + Focus  + 2 per Knot consulted  − Coherence penalty (Dissonant 1 … Severed 5)

salience(c) = recency(c) × confidence_live(c) × relevance(c, q) × stanceweight(c, person)
stanceweight(c) = clamp(1 + λ·agreement(c), 0.05, 2.0),   λ = obstinacy / 5
```

A Templar with obstinacy 5 holding an exonerating claim about a Southern Einhir smith gets
`stanceweight = 0.05`: the claim is in his ledger, at high confidence, and its salience is one
twentieth of an agreeing claim's. It does not enter the top-K. **He is not hiding it and he is not
lying; he is not thinking of it.** The floor is 0.05 rather than 0 so that a devastating firsthand
contradiction can still cross — motivated reasoning, not a wall. What is attenuated is **retrieval,
not value**.

### §3.4 Where #342's documents disagree: the owning document wins on its own object

#342 is seventeen documents and they contradict each other in several places. **This document does not
resolve those by seniority, by date, or by which is "the spine".** It resolves them by one rule, stated
once and applied uniformly:

> **THE CONFLICT RULE. Where two of #342's documents disagree about an object, the document whose
> declared subject is that object wins.** A document asserting a value it does not derive loses to the
> document that derives it.

*(An earlier version of this document grounded one such ruling on doc 09 being "the spine". That was a
misread: `00_INDEX.md:28` gives spine status to **doc 01 only**, and it left this document ruling for
doc 09 in one place and against it in another with no stated principle. C-6.)*

**The four rulings this document makes under that rule, all of them recorded rather than silent (C-16):**

| collision | ruled | on what ground |
|---|---|---|
| **`K`** — `03:325-329`'s `K = 7 + Focus` against `09:63`'s constant 12 | **`7 + Focus`** | doc 03's declared subject is view assembly; doc 09 asserts a constant it never derives |
| **`exposure`** — five senses across the suite, two of them the same concept implemented incompatibly, and one of them refused by name in a neighbouring document | **the pre-roll odds preview only** (§5.4). The stored-counter sense is not used anywhere in this document | doc 10 owns the resolution surface; a stored exposure counter is refused by `07:556` in the document that owns alignment |
| **practice rank** — `02:153`'s 0–5 against `10:33`'s 0–7 | **0–7**, giving the pool range 1–14 | doc 10's declared subject is *the arithmetic that turns Capability into a die count* (`10:27`); doc 02 owns Capability's composition, not its arithmetic |
| **the Thread term's placement** — `02:197-200` puts a conditional `+ thread_pool` inside the pool expression; `10:192` makes Thread **a second pool through the same `roll`** | **a second pool through the same `roll`** | same ground; and the alternative puts a second addend inside `Pool`, which §14 row 10 forbids in spirit |

**None of these is retrofitted into the rest of #342**, and §15.11 records that as a limit.

---

## §4 · THE RUNGS, AND THE FIVE OWNERS

### §4.1 What each rung owns

**Individual** owns the only write path: acts, claims, stance.

**Hearth (family)** owns transmission across time: the **larder** (§11.1), the **succession pointer**,
and the **obligation edge** — kin may `requisition` each other's acts, which surfaces another person's
act as *theirs to refuse*. Cadet branches are not authored; a cadet branch is a hearth whose succession
pointer does not lead to the main line's holdings, so its members' needs are permanently unsatisfied by
inheritance and they must seek standing through the Church, a guild, the Löwenritter, the Restoration,
a marriage, or a knife. Every noble-house intrigue in the setting is that sentence run forward.

**Community** owns peer judgment and the admission gate. The **judging set** is the persons who hear
about your act by default and apply their stance to it. **Admission** is an act by persons who already
hold standing, changing another person's address and conferring a mark. A community holds **no state of
its own**: a norm is the aggregate of member stances, computed on demand.

*A cell people live in is a community; a cell people belong to while living elsewhere is a faction.*
The first cannot be secret, because you cannot hide where you sleep. The same test settles institutions:
the Church is a faction, a parish is a community, and a Dicastery is neither — it is an **office
cluster** (§4.4).

**Settlement** owns the first contested material stake and the first office. The granary opens for the
hamlet or for the Row, never both. Office is a post whose holder's decision binds persons who never
agreed to it.

**Sibling competition is one function.** At every rung, peers inside a shared container compete for
exactly three prizes — the stake, the regard of the container's members, and the container's offices —
through `contest(container, prize, claimants)`, where claimants are **factions**, which need not be
siblings in the tree.

### §4.2 Ownership: who may write what

**This table has FIVE rows. #342's has four (`11:94-99`), and the fifth is required by §7 and §8.**

| owner | holds |
|---|---|
| **Person** | address, marks, capability, stance, claim ledger, ties; `Holding` edges and commitment edges. Everything interior |
| **Container (a rung)** | its stake(s) · its judging set · its standing dates, each date's `capacity` (§4.4), and their convening conditions · **and the matter it holds**: a hearth's `stores`, a site's `condition` (§10.2), and the transmission pointer. **No social aggregate, ever** |
| **Office** | its post, node, remit, conferral and revocation rules, establishment, `seat_items` (§4.4), upkeep — **and its own standing dates and their convening conditions** |
| **Faction** | its proposition and its commitment map |
| **Nobody** | aggregates, norms, densities, needs, openings, scale, reputation |

**Two rows in that table are amendments to #342 and both are stated rather than smuggled.**

**The Office row.** #342's table has four rows (`11:94-99`) and gives offices dates in two places
anyway: `14:91-92` makes `seat_items` a per-holder capacity consumed by *an office's* standing dates,
and `14:325` resolves an appointed office's vacancy by *"a conferral standing date at the parent
office"*. So dates are container-owned **by convention, not by necessity** — which is what lets §8
reach an office cluster that has no containment node.

**The Container row's matter clause.** `01:490-491` says *"Containers hold stakes, judging sets and
dates. Persons hold everything else"* — and **the shipped hearth already contradicts it**: `04:29-37`
declares exactly two stakes (`holdings`, `seat`) and then holds `stores` and `pointer` besides. This
document does not paper over that; it states the general rule the tree is already following:

> **A container may hold MATTER and DATES. It may never hold a SOCIAL AGGREGATE.**
>
> A larder is not derived from persons and does not go stale against them — it is a physical quantity
> that exists whether or not anybody believes in it, and the design already stores it at `04:32-35`.
> A norm, a density, a reputation or an unrest level *is* derived from persons, and storing it is the
> defect `11:214` names. **The line is provenance, not location.**

*(An earlier version of this document added the Office row and did not re-run the same check on its
own enlargement 3, leaving `condition(site)` as container state the table forbade — and leaving
`stores` and the pointer unowned in the same table that was quoting them. C-13.)*

**Why the Office row is required, and why it is not a new kind of state.** #342 already gives offices
dates in two places: `14:91-92` makes `seat_items` a per-holder capacity consumed by *an office's*
standing dates, and `14:325` resolves an appointed office's vacancy by *"a conferral standing date at
the parent office"*. So dates are container-owned **by convention, not by necessity** — and an office
cluster with no containment node (a Dicastery) can therefore still hold one. The row states what was
already true and makes §7's and §8's reach across clusters legal rather than smuggled.

**An office is not a container.** It holds no stake and no judging set, and it is not in the containment
tree. `Holding := (person, office, since, conferrer)` remains an edge on the **person**, exactly as a
commitment edge is. *Who holds the praefecture* is a query, not a field. **Nothing anywhere stores
control.**

**The last row is the load-bearing one.** Every aggregate is a function, never a field. Stored
aggregates are how a design acquires dead state that reads as mechanism.

**R-1.** A rung module may read its own state and any message addressed to it. It may **not** read a
sibling's or a descendant's state directly. It **may compute an aggregate over its descendants on
demand**; it may not receive a pushed one and may not store one. **Compute-on-demand, never push, never
store.**

**R-2.** A rung module writes only its own state. Upward influence is emitting an aggregate; downward
influence is emitting a refraction. No module reaches through another.

**The module tree IS the containment ladder.** Parent–child in code means containment in the world;
nothing else is a parent of anything. `faction/` sits beside `world/`, never inside it — the moment a
faction is a node in the containment tree it acquires a level, and the moment it has a level it cannot
grow across one without an authoring act.

### §4.3 The two capacity quantities, named once and owned once

**Every price charged anywhere in this document is denominated in one of exactly two quantities, and
both are shipped.** They are different quantities with different owners and different consumption
points, and conflating them is how the earlier draft came to charge prices against a unit that no row
of §4.2 owned (C-3).

| quantity | owner | what it is | consumed |
|---|---|---|---|
| **`capacity(date)`** | the **container** (or office) that holds the date | how many items **that sitting hears** — *"a term of the container, and therefore something a dispensation can change"* (`05:184-186`). The Grauwald territory court hears eleven | **at the hearing.** `compose_agenda` admits the top `capacity(date)` items and no more |
| **`seat_items(office)`** | the **office**, and it is spent by its **holder** | *"how many things he can hear or carry in a sitting … Holding two offices does not double a day"* (`14:91-92`). A praefect holds one seat and carries one thing with it (`05:187`) | **at the filing.** `carry` spends one of the carrier's `seat_items` |

**There is no third quantity.** *"Its charter's sitting capacity"* — which the earlier draft used to cap
convening conditions — is not a thing; the cap is `seat_items`, because a fired date consumes the
convener's hours (§7.3 C2).

⚠ **And §17.4's finding is narrower than it read.** The design's missing *"finite, contested, durable
capacity object"* is **the establishment** — the named persons an office employs, which has no capacity
object anywhere. The two quantities above are finite, contested and durable, and they are why `drop`
exists at all.

---

### §4.4 Office, completely

```
Office  := (post, node, remit, conferral, revocation, establishment, seat_items, upkeep, dates)
remit   := (acts[], scope_node, binds)
binds   ∈ { members-by-admission, persons-by-presence }
```

`remit.acts` is drawn from a **closed set of five**, each an ordinary act made eligible somewhere it
otherwise is not: **issue** (a dispensation, §9), **determine** (one person's decision at a venue,
§12), **confer/revoke** (admission over an office rather than a community), **dispatch**
(`requisition` on the establishment), **convene** (setting a standing date and ordering its items,
§7 and §8.4).

**Office changes the option set and the pool source — never a modifier.** A flat shift of size X on a
pool roll is worth `X / (0.671·√Pool)`, which helps a weak side *more* than a strong one, backwards
from what a leader is supposed to mean. So: `eligible(p, act, n)` consults `remit`; and when an act is
performed **by remit**, the pool is drawn from the **establishment** — the named persons the office
employs — not from the holder's own capability. Duke Vaynard's Focus is irrelevant to whether the levy
is collected; the pool is the reeve's, and the reeve has a larder, a stance toward Vaynard, and kin in
the hamlet he is collecting from. **Choosing which of your people performs the act is the whole of a
leader's tactical choice, and it is a choice between pools, not a purchase of a bonus.**

**Three costs, all in currencies that already exist:** `seat_items` (§4.3); **publicity** (every act by remit is
public, so an office-holder cannot act quietly — which is why a covert edge and a remit are close to
incompatible); and **upkeep** (the establishment eats; an unpaid establishment does not disperse, it
becomes a faction and treats plunder as wages — see §11.3).

### §4.5 Conferral is ROOTED IN THE OFFICE — ruled here, not escalated

#342 asserts both answers and resolves neither, and its index files the question as the one thing to
settle before anything is built. **It is settled here, because it has an architectural answer and
`CLAUDE.md` §0's fifth test forbids escalating a call that has one.**

> **`confer` is performed BY REMIT. The conferral basis is the conferring OFFICE, and the act is
> performed by whatever person holds it.**

**Why this is not the answer B-11 forbids.** B-11 forbids an *institution* performing the game's most
consequential act. Office-rooting does not make an institution act: a **named person** still performs
`confer`, exercising a remit, exactly as a named person issues a dispensation or determines at a venue.
What is office-rooted is the **basis** — the authority the act draws on — not the actor. The distinction
is the same one §4.4 already draws when it puts the *pool* for an act by remit on the establishment
while the *act* stays the holder's.

**Three things follow, and they are why the alternative fails.** Person-rooted conferral terminates the
graph at every dead conferrer, so the sovereignty query that every faction's victory condition reads is
undefined across most of it and **the Crown cannot be played across a succession**. Office-rooted, the
graph resolves; `sovereign_fraction(root)` is a reachability query, total and terminating even on a
cyclic graph, and what a contested succession undefines is **the choice of ROOT, not the function** — so
callers must handle root-plurality, and a unique root is a political condition rather than an invariant.
And the design's own strongest evidence points the same way: a military order sworn to *the Crown as
institution, not the bloodline* is a warrant that means nothing if conferral is personal.

*(This was carried as a live choice for Jordan in an earlier version of this document, immediately after
naming the evidence and the direction it pointed — which is exactly the failure `CLAUDE.md` §0's
five-test ordering exists to prevent. C-18.)*

---

## §5 · THE RESOLUTION SURFACE

### §5.1 One roll

Every attempt rolls **N ten-sided dice**. 1–6 scores nothing, 7–9 scores one success, 10 scores two.
Mean = `Pool ÷ 2`, σ ≈ 0.671 per die.

```
Pool(person, practice) = Attribute[relevant](person) + Practice[practice](person)      # 10:30
```

Attributes run 1–7 (the nine named in the setting, plus the ruled-but-unnamed tenth, which composes
identically because this formula never inspects an attribute's name). Practice runs 0–7, where 0 is
*never trained* — **an untrained attempt is always legal, it is just a small pool.** Realistic pool
runs 1–14. (`10:33`; and see §3.4 for the practice-range collision this rules.)

**Why a pool and not a target number plus modifier.** A difficulty number must be *decided* by
somebody, and that somebody is the GM this game does not have. In a pool, both sides are expressed in
the same unit — small integers already on the person and object schema — so the target is **computed,
never assigned.**

### §5.2 One obstacle, one owner

```
obstacle(context):
    if context.opponent is a person: return OPPOSED
    R = resistance_pool(context)
    if R <= 1: return 0                       # no roll; automatic clean success
    return round_half_up(R / 2)
```

`resistance_pool` is always a dice-equivalent in the identical unit capability uses — a lock's
fineness, a wall's sheerness, a document's forgery quality. Something that is not a person cannot try
harder; it has one performance, fixed at the moment of the attempt. **The obstacle formula is the
roll's own expected value, used deterministically because the resisting thing has no agency to vary.**
If `Obstacle > 2 × Pool` the attempt is impossible and the resolver refuses to roll it: the act must
change under a manoeuvre or it does not happen.

The Masterpiece Examination is the worked institutional case, and it is where the anti-gauge discipline
shows: the committee's resistance pool is computed **on demand** from the individual stances of the
sitting masters toward the candidate's marks. Nothing is stored; there is no caste number. Change the
masters — a schism, a retirement, a bribe — and the number changes with no edit anywhere.

### §5.3 Degrees, and opposed contests

`Margin = successes − Obstacle`.

| margin | band |
|---|---|
| ≤ −2 | **Disaster** |
| −1 | **Failure** |
| 0 | **Costed Success** |
| +1, +2 | **Clean Success** |
| ≥ +3 | **Overwhelming** |

Costed Success is the deliberate middle band — you meet the obstacle exactly and something is given up
for it — and **at balanced pools from 4 to 12 it runs 14–28%**, so it is not a band the system is tuned
never to reach. Disaster remains reachable at every pool size (Pool 14 vs Obstacle 2 is still 0.078%),
because it falls out of the same binomial as every other row rather than from a hand-authored floor.

⚠ **Scoped, because the unscoped claim is false at the bottom (C-19).** *"Every band is reachable
across the entire realistic range"* holds for Pool ≥ 3. **At Pool 1–2 the top band is unreachable**:
Overwhelming needs `successes ≥ Obstacle + 3`, and one die yields at most two successes. That is a
property of the arithmetic and this document does not repair it — a person attempting something at
Pool 1 is not owed a triumph band, and where the obstacle is small enough to matter the resolver
skips the roll entirely (§5.2's `R ≤ 1` floor).

An **opposed contest** is the identical `roll` called twice, with the deterministic obstacle replaced by
an actual draw because there is now someone on the other side capable of having a good day. It is not a
second resolver. Past a pool gap of about 6, the underdog's chance falls under ~11% and keeps
collapsing — and **the honest response is to publish the mismatch, not to hide it behind a menu that
pretends to matter.** The one manoeuvre that is never decorative at a large gap is the one that changes
*which obstacle you are rolling against*: the fisher does not win the doctrinal argument, he routes it
— contests jurisdiction, or converts a private grievance into a backed petition (§8).

### §5.4 The pre-roll exposure, and what it may publish

Before any die is drawn the resolver publishes the inputs a player would need to compute the odds
himself: both pool sizes and the obstacle interpretation (`10:132`). Computing that table **never calls
`roll`** — *"looking at the odds cannot consume the die"* (`10:180`).

**That is a channel, and it needs a rule about what may travel down it**, because the preview is free,
act-free, witness-free, and **asymmetric: `choose` has no `World`, so no NPC can run the same probe.**
An earlier version of this document stated one rule and called it *self-enforcing*. It is not
self-enforcing and it did not cover the cases that matter (C-5). The corrected rule is a partition:

| what resists | what the preview publishes | why |
|---|---|---|
| **material and publicly inspectable** — a lock's fineness, a wall's sheerness, a cliff's grade | **the scalar** | anyone standing there can look at the wall. Publishing it leaks nothing that presence does not already give |
| **a resistance composed from persons' private stances** — a judging set's obstacle, an admission committee | **a BAND, never the scalar** | the scalar is an aggregate of private stances, and §1.3 already forbids anyone reading a true profile rolled up from real state. **This is a change to #342, which publishes the composed scalar** |
| **hidden world state gated behind investigation** — a site's `condition` (§10) | **a band, and the scalar is never an operand of any roll** | so there is nothing finer for a repeated preview to invert out. **This limb is enforced by construction; the other two are publication rules a careless implementer can violate** |
| **the opponent's pool in an opposed contest** | **published, deliberately** | see the rebuttal below |

**On the opponent's pool: this document holds the shipped behaviour and does not treat it as a leak.**
`10:132` publishes both pool sizes as a stated policy — *"the honest response is not to hide the
mismatch behind a menu that pretends to matter — it is to publish it"* — and the alternative is a game
that dresses a 3-vs-14 roll as a rich tactical scene. A pool is also not hidden in the way a stance is:
capability is practised in public, and marks are *"ascribed, publicly-read attributes"* (§2). **The
design chooses legibility here on purpose, and this document does not overturn it.**

**And the showcase example moves accordingly.** §5.2's Masterpiece Examination composes its resistance
from the sitting masters' stances toward the candidate's marks, so under row 2 the candidate previews
**a band**, not the exact aggregate of what the masters privately think of his caste. Discovering which
master is cold is what the knowledge layer is for.

> **THE RESIDUAL, stated rather than hidden (§15.15):** the partition is a rule about publication, and
> only its third row is structurally enforced. A resistance that is *neither* plainly material *nor*
> plainly stance-composed — a forged document's quality, a rival's fortification nobody has seen — has
> no ruled row, and this document does not invent one.

### §5.5 Determinism

Per-attempt substreams derived from a hash of `(world seed, tick, actor id, attempt discriminator)`,
never from a shared sequence. Consequences: showing a player a possibility cannot change what happens;
two attempts resolved in a different order give the same answers; and adding a person somewhere does not
re-phase every other roll in the world. **Order independence is the property to guard, because its
absence is invisible.** Replay is a re-run, not a log, and **no decision function may read the event
log** — a module that reads the log has reintroduced the world into the choosing signature by the back
door, and it will not look like a violation at the call site.

**Three fidelities, one resolver.** Played, witnessed and auto differ only in **who is asked to
choose**, never in how the outcome is computed. Identical `resolve`, identical rolls, identical seeds. A
path that computes an outcome without running the same resolver is a second resolver whatever it is
called, and it will diverge.

---

## §6 · THE SEASON — SEVEN PHASES, THREE WRITE CLASSES

### §6.1 The tick and the scarce thing

**The tick is a season. Every person and every cohort commits exactly one act per season.** An act is
not everything a person does in three months; it is the one discretionary commitment. Subsistence,
craft and travel-in-progress happen *to* you in P1.

⚠ **D-2, THE ACT ECONOMY, IS OPEN AND IS THE LARGEST OPEN RULING IN THE DESIGN.** #342 asserts one act
per season at `09:33` and then narrates a Duke taking seven verbs in one turn under a header claiming
ten (`14:562`) — wrong under every reading, including its own. And `14:91-92`'s `seat_items`
*"consume the holder's own hours"*, which is already a fourth per-holder capacity against `14 §1`'s
*"three quantities and nothing else."* The stake is not bookkeeping: **whether a Duke's season is one
pick among six shapes or a ten-act sweep is the difference between a personnel game and a decree game
at every rung above Settlement**, and it decides whether a player-Duke experiences the top of the ladder
as a demotion. §16 carries it as a live choice; §8.3 and §11.4 state what depends on it.

### §6.2 The seven phases

Phases run in order; within a phase everything is simultaneous.

| | phase | what happens |
|---|---|---|
| **P0** | **CALENDAR** | advance the date · fire due standing dates into a docket · **evaluate convening conditions and schedule the dates they name (§7)** · recompute option availability |
| **P1** | **SETTLE** | **metabolism and nature only**: larders consume against mouths, production resolves, wounds close or fester, bodies age and die, travellers advance a leg, **and a site's condition moves by nature's term alone — `season_factor`, which is weather (§10.4)**. *No social quantity moves here, and no act's effect lands here* |
| **P2** | **NEEDS** | every person and cohort computes needs from its situation. Pure, parallel, never stored |
| **P3** | **VIEW** | top-K claims by salience per person (§3.3); K = 3 per cohort |
| **P4** | **CHOOSE** | `choose(person, view) -> act`, everyone, against the frozen P1 snapshot and their own ledger. The player's submission enters here and nowhere else |
| **P5** | **RESOLVE** | `resolve(acts, world) -> events` |
| **P6** | **WITNESS** | events fan out by presence and channel; `witness` per person |
| **P7** | **RECKON** | claim confidence decays; ledgers evict lowest salience (this is forgetting, not a data limit); cohorts individuate; persons nobody remembers de-individuate |

**Reaction latency at person scale is one season**, so surprise is structurally possible: no policy can
say *"if he does X, I do Y, this turn."* You anticipated or you are late. The exception is that **inside
a contest the tick subdivides**, opening a nested loop of exchanges over a smaller person set on a
shorter clock. Fidelity is how deep that nesting individuates and nothing else.

### §6.3 Three write classes, and the correction that makes them honest

#342 says two things that cannot both be true and are both false as written: that **P5 is the only
writing phase**, and that **P1 is the only phase that changes the world with no act behind it**
(`09:55-56`). P0 already advances the date and writes a docket, which is a world write with no act
behind it, and P1 moves matter. The correct statement, which this document uses:

> **There are exactly three write classes, and no others may be added.**
>
> | class | phase | what may be written | licensed because |
> |---|---|---|---|
> | **calendar** | **P0** | dates and dockets | a date is not an outcome; it is an occasion |
> | **matter** | **P1** | larders, bodies, travel, and a site's condition **under nature's term only** | metabolism and nature — the world is not a caretaker for having weather |
> | **acts** | **P5** | everything else, **including every condition delta an act caused** | a person did something |

**§7's convening conditions add nothing to this list.** They are evaluated in P0 and write dates, which
is what P0 already writes. That is the whole of the answer to the objection that scheduling is a second
writing phase: it is not a new phase and not a new class. If a future object cannot be placed in one of
these three classes, it does not go in the engine.

⚠ **And the classes bind this document too.** An earlier version put an act's effect on a site into P1
as a deferred write, which is neither metabolism nor nature and therefore breaks the licence it had
just stated (C-17). **An `alter`'s effect on a site's condition resolves in P5, like every other effect
of an act.** P1 carries only what weather does. That also removes a one-season offset the earlier
version had to explain away.

### §6.4 Conflict between acts

Every act declares `touches: {(object, mode)}`, mode ∈ `{read, alter, exclude}`. Two acts conflict iff
they share an object and either mode is `exclude`, or both `alter` the same field. Conflicts route to
`contest(container, prize, claimants)`, unchanged. Everything else resolves independently. **Ties break
on a hash of (act-id, world-seed) — never on rank, office or list position**, because a rank-ordered
tiebreak is a hidden power stat that never appears on a factor sheet.

**Resolution strata, each with its reason:** movement first (every stratum below asks who was there),
then binding decisions at docket dates, then contested physical acts, then uncontested material acts,
then social acts last — because social acts are *about* what happened, which is what makes a season's
gossip be about that season's deeds.

---

## §7 · THE CALENDAR, AND CONVENING CONDITIONS *(enlargement 1)*

### §7.1 The object

> **A CONVENING CONDITION is a published predicate attached to a thing that holds standing dates
> which, when it becomes true, SCHEDULES A STANDING DATE. It decides nothing.**

```
ConveningCondition := (holder, predicate, date_form, set_by, set_at)
   holder     ∈ Container | Office                    -- §4.2's two date-holding owners
   predicate  : pure over the holder's own readable state — its stake, the norm of its judging
                set on a named proposition, an R-1 compute-on-demand aggregate over its
                descendants (§4.2), or the calendar.  PUBLISHED AS A BAND, never as a trigger point
   date_form  : (venue, horizon, convener office) — the standing date it will schedule
   set_by     : the person whose act attached it
```

**It is named a convening condition and not a "watch".** #342 uses *the watch* throughout doc 12 for
soldiery — *"twelve men of the praefecture's watch"* (`12:37`), *"there is no such thing as a reliable
watch, only a watch whose margin you have not yet tested"* (`12:99`). Coining *watch* as a calendar
primitive would give one word two shipped meanings, which is exactly the idempotent-vocabulary failure
`CLAUDE.md` §4 records this repository having already paid for once. *Convening condition* is ordinary
charter English — a body's charter states the conditions under which it must be convened — and a reader
with no memory of this design lands on the right meaning cold.

### §7.2 It is a new composition, not the naming of a shipped pattern

**Stated plainly, because the earlier work claimed the opposite and the claim was false.** The corpus
ships the two halves — predicates that gate, and events that schedule — and **never the composition.
There are ZERO exact instances.**

| candidate | verdict |
|---|---|
| `banked_claims` (`04:35`, *"each is a standing date with a watch predicate"*) | **the only verbatim instance, and this document rules it away** — see the dormancy ruling below |
| the vacancy a death emits (`14:193-196`) | **event-driven, not polled.** A death opens a conferral date. Calling it an instance retrofits polling onto an event handler |
| dormant grievance rows re-arming (`05:625-645`) | **not an instance.** The rows are *person-held stance rows*, the check runs on every incoming claim, and what fires is **the person's valuation, not a calendar** |
| vacancy-by-absence (§8.6) | **not shipped.** It is a repair direction, future tense — and it is an instance *of this enlargement*, which is not evidence for it |

**THE DORMANCY RULING, made once and not straddled.** `04:35` says a banked claim is *a standing date
with a watch predicate* held by the hearth; `09:641` says *"There is no flag object; dormancy IS an
act-proposition with an unmet enabling claim"*, unified under P0's recompute. **`09:641` wins**, on
§3.4's conflict rule: doc 09's declared subject is what persists and how, and doc 04's own state table
declares **exactly two stakes** (`04:29-37`) and then names `banked_claims` as a third thing without
deriving it. Two independent grounds agree: a banked claim is *a claim*, and **claims live in ledgers**
(§3.1); and the alternative is a stored flag on a container, which §4.2's amended Container row admits
only for matter. So a banked claim is an act-proposition in a person's stance table with an unmet
enabling claim — not a second object, and **not an instance of this section.**

> So the convening condition stands on its **N-line and its design argument alone**, in the dock, with
> no recurrence argument behind it. That is the honest position and it is where this enlargement must
> be attacked.

**What it generalises, which is a real and smaller claim.** A container's charter already schedules
dates by rule — the tithe reckoning, the quarterly Parliament, the examination. Those rules are
unconditional (*every quarter*). This enlargement widens the rule's admissible form from date-arithmetic
to a published band predicate. Same field, same owner, same phase.

### §7.3 The provenance rule — who attaches one, by what act, at what cost

**Without this, the object is an authored trigger inventory wearing a uniform, and free attachment is a
denial-of-service on any office, because scheduling mints dates and dates consume the holder's hours
(`14:91-92`).** So:

- **C1 · PROVENANCE.** Attaching a convening condition is an exercise of **`convene`** (§4.4's remit
  act), performed *in advance*. Only a person holding an office whose remit includes `convene` at that
  holder may attach one, and only at that holder. It is an act by remit, so it is public (§4.4) and it
  is witnessed like any other.
- **C2 · PRICE, denominated in §4.3's two quantities and no others.** Attaching costs the setter **one
  of his own acts for the season**, exactly as `compose_agenda` does (`05:206`) — it is the same remit
  act. A date it later schedules consumes the convener's **`seat_items`** in the season it fires
  (`14:91-92`). **The cap on live conditions is `seat_items(office)`**, a holder property: an office may
  carry no more live conditions than its holder has hours to sit them, and attaching beyond that
  requires striking one, which is another act. *(An earlier version priced attachment against "the
  sitting's capacity" and capped it against "the charter's sitting capacity", spending two different
  quantities as though they were one. C-3.)*
- **C3 · IT DECIDES NOTHING.** It schedules an occasion. The decision at that occasion is a person's act.
- **C4 · WHAT THE PREDICATE MAY READ.** Own state, an R-1 compute-on-demand aggregate, or the calendar.
  Never a descendant's stored state; never a social quantity that is not itself a computed norm; never
  the true faction profile (§1.3).
- **C5 · VACANCY.** A vacant convener may not attach one, and does not stop the existing ones from
  firing — they are terms already set by an act that was already made, exactly as a dead issuer's
  dispensation keeps its terms. A date that fires with a vacant convener is **a date nobody is
  ordering**, which is the correct behaviour and not a defect (§8.6).

**So the object is not decider-free at its root.** It traces to the act that set it, seasons or
generations earlier, in the same way a banked claim traces to the marriage act that armed it. That is
what keeps it out of §13's falsifier.

### §7.4 What it schedules: a DATE, never an item

**A convening condition schedules a date. It never places an item on an agenda.** Composing the agenda
remains `compose_agenda`, performed by the named convener (`05:190-194` forswears by name *"the engine
deciding which grievances matter with no person in the loop"*), and sitting capacity remains finite.

**The consequence, stated against this document's own interest:** a condition guarantees an *occasion*,
not a *hearing*. The earlier work claimed it restored the endings of arcs that terminated at a counter
with nobody deciding; **the honest claim is that it makes those endings reachable, by a person, at a
sitting somebody must compose.** Whether the matter is reached is still a convener's choice, and §8.4
is where that choice is already priced — by #342, not by this document.

### §7.5 The N-line, narrowed

Cut convening conditions and:

1. **A slow material condition with no petitioner never reaches any calendar.** Supersession (§8.5) only
   *kills* matters; multi-petition (§8.3) needs a petitioner who has both a want and a verb; and the
   world's own worsening has no other route to an occasion.
2. **Foresight cannot outlive the foreseer.** A person who sees a famine coming can convene now; without
   this object he cannot arrange that the question be *asked* after he is dead, out of office, or
   uninterested — which is what a charter provision is for.
3. **§8.6's presence-based vacancy loses its clean carrier.** ⚠ *Not* that it has none: `14:254-256`
   ships **revocation in fact** — *"An office whose `exercise` is zero across its whole scope for two
   standing dates is vacant in the only sense that matters"* — so absence already has a consequence at
   office rungs. What the convening condition adds is narrower and is the part that matters: `exercise`
   is **identically zero at a hearth**, which has no remit, while **presence is defined at every rung
   because every rung has bodies in it**. So the shipped rule reaches the King's council and cannot
   reach the household, and it is the household where the setting's hostage politics lives. *(An earlier
   version of this bullet claimed there was no carrier at all, which `14:254-256` refutes. C-15.)*

**What it does NOT buy, and the earlier work said it did:** it does not make obstruction visible on its
own — §8.4 shows that #342 already priced it — it does not resolve anything, and it does not supply the
three arc endings by itself (§7.4).

**Two attacks that fail, named so the next reader does not re-run them.** *It must read a descendant's
state, violating R-1* — **fails**: the predicate is scoped to own state or an R-1 compute-on-demand
aggregate, which is R-1's licensed form verbatim. *It is identically zero at the hearth, like the
`exercise` predicate that failed before it* — **fails**: a hearth carries dates (`04:122`'s vacancy
sitting), so the object mints its own surface at every rung rather than depending on a remit a hearth
does not have.

---

## §8 · THE UP-STROKE *(enlargement 2)*

### §8.1 Petition, and the respondent

```
Petition(petitioner, proposition, respondent, backing)
respondent ∈ ContainmentNode | Office
```

Produced by a person whose computed need exceeds what their own acts can reach. **Backing** is the set
of persons who have lent their stance to it — that is the aggregation, and it is why there is no crowd
object: *a town's demand* is a petition with four hundred backers.

**The respondent is a node or an office — always a person or a vacancy, never a mechanism.** An office
is held by a person or it is vacant, so B-11's price is paid in full: *you address it to a person, and
that person can drop it.* And it reaches every **office cluster** — the four Dicasteries, the knightly
order, every trans-settlement guild — because a cluster is exactly an office set with no owning node,
and it has offices even where it has no container. **It needs no new object:** an office already exists,
is already conferred, revocable and vacant-able.

⚠ **What it opens is large but not total, and the earlier version of this document overclaimed it.** It
said the retyping *"closes the whole direction of play that was structurally shut"*. **Withdrawn (C-4).**
Filing at a cluster office is now legal, and where that office's vacancy resolves at a parent office it
behaves like any other. **Where it does not, S19 stands and the petition has no clock (§8.5 case 3).**
The retyping opens the door; it does not guarantee a room behind every one.

*(An earlier version typed the respondent as a standing date. That is withdrawn: a date cannot drop a
petition, and typing the respondent as a mechanism trades away the design's central commitment — every
decision is made by a character — to solve a plumbing problem. §17 records it.)*

### §8.2 Carriage, dropping, and standing at an office

A petition cannot enter a container by itself. Some person must perform `carry(person, petition)` — an
act, at a cost:

```
carry(c, P):
  precondition: c holds STANDING at the respondent  (see the rule below)
  precondition: claim(c, "P exists") ∈ ledger(c)
  cost:  one of c's own `seat_items`   (§4.3 — 14:91-92, "how many things he can hear or carry")
  regard_cost(c) = Σ_{j ∈ judging_set} max(0, −stance(j, prop)) × weight(j)
  regard_gain(c) = Σ_{b ∈ backers WHO LEARN c carried} stance(b, prop) × weight(b)
```

> **THE STANDING RULE FOR THE OFFICE FORM — a NEW rule, modelled on F10 and not derived from it.**
> **Standing at an office is standing at the office's node, or leave from a person who holds it.** For an
> office on a cluster root, which has no node, standing is membership in the office's own judging set or
> establishment, or leave from a member.
>
> ⚠ **F10's predicate is narrower than this and is not being widened here (C-24).** `08:155` reads *"you
> are not in the judging set **and** hold no leave from a member"* — judging-set membership, not standing
> at a node. The rule above is modelled on F10's *shape* (a membership test with a leave escape) and
> extends it to a node, which F10 does not say. It is stated as an addition so that nobody later cites
> F10 as its authority. #342's own version of this precondition was written for the **withdrawn**
> date-respondent (§8.1) and was never re-derived, so something had to be written.

A venue's `enter` / `speak` columns (§12.4) are the door and are unchanged.

At the rung above, the carrier chooses: **forward**, **amend** (which the backers may or may not learn
of), **bundle**, or **drop**. **Dropping is an act by a named person at a named time**, and the reason
it exists at all is that seat capacity is finite: a court that hears eleven items and has seventeen
seatholders leaves six carried petitions off the floor.

**The drop is a valuation, not a threshold.** Praefect Aldwin drops the hamlet's grain bundle and
carries his own son's supplication, and the payload of the worked case is not the arithmetic but item
five of it: **his ledger holds no claim that the hamlet can hurt him.** The cell there is concealed
alignment; concealed alignment deposits no claims; a person with no claims about a danger acts from
ignorance, not from uncertainty. A relevance score would make that a tuning question. A man's valuation
over his own ledger makes it *a mistake he had every reason to make*, which is the only version of
filtering that produces politics rather than friction.

**The deposit.** When a backer learns, `m = shortfall_at_raising × weight × amplification(chain)`, and
**the telling's grammar decides where the grudge lands**: a claim naming an actor deposits on him; one
naming only the container deposits on the container. A grudge at a person is discharged by removing the
person; a grudge at a container is not. Nothing was designed to produce that asymmetry — it follows from
stance rows having referents.

### §8.3 A petitioner may address many offices

A petition is not exclusive. A person with a want may put it to several offices, several persons, at
several rungs, in the same season or across seasons. **They are independent objects — each carried
separately, each expiring separately, and none of them cancels another.** There is no dedup and no
*the matter is already before a body* rule; that would be an engine deciding a person's options.

Four consequences:

1. **Vacancy is expensive rather than lethal.** A dead praefect does not mean nothing happens; it means
   *you must spend more to be heard*, and every extra route costs acts and time you may not have. A tax,
   not a wall.
2. **Burying requires monopoly or coordination.** A convener who buries an item only wins if he controls
   every venue that could hear it — which is itself political work, visible and contestable.
3. **Offices come into competition and standing is the prize.** Answering first is worth credit; refusing
   something a rival then grants is visible. Jurisdictional rivalry from the petition rule alone.
4. **It multiplies both failure and luck.** Three petitions can all expire and the petitioner has spent
   three acts for nothing — worse and truer than one refusal. Or two offices both act and the grain
   arrives twice, which is §13.3's coincidence produced out of the up-stroke rather than out of trade.

⚠ **This is where D-2 (§6.1) bites hardest.** Under one act per season, three petitions cost three
seasons of a famine — a real price, and the enlargement is well-shaped. Under a multi-act reading,
**petition-spray dominates** and the scarcity this section relies on evaporates. **The R-line for this
enlargement cannot be ruled until D-2 is.**

### §8.4 Composing the agenda is an ACT, and an omitted petition is a DROP

**This section restates a shipped rule that the earlier version of this document deleted, and withdraws
a repair that was aimed at a premise the tree refutes (C-1, C-2).**

```
compose_agenda(v, container, date):                                          # 05:202-208
  input:   the petitions v HOLDS A CLAIM OF — not the petitions that exist
  act:     v ranks them by his own valuation — the same choose(person, view) every other act
           runs through — and admits the top capacity(date)                  # §4.3
  cost:    ONE OF v'S OWN ACTS FOR THE SEASON                                # 05:206
  regard:  identical in form to carry's, over the judging set and over THE BACKERS OF EVERY
           PETITION HE ADMITS OR OMITS, as and when they learn               # 05:207-208
```

> **`05:211-216`, verbatim and load-bearing: *"An omitted petition is a DROP, and deposits exactly as
> one."*** §8.2's grammar applies unchanged — a telling that names the convener lands on him; one naming
> only the court lands on the praefecture. No new object, no new deposit rule, *"and the grievance from
> an item that never reached the floor is the same substance as the grievance from one a carrier
> abandoned, which is right, because to the hamlet they are the same thing."*

**So burial is already priced, and the design already says so in the strongest terms available to it:**
*"a man who can keep an item off the list for four sittings running has more power over Grauwald than
most of the men who vote on it, and he exercises it by an act that is witnessable, tellable, and
attributable to him by name"* (`05:218-224`).

**⚠ WHAT THIS DOCUMENT GOT WRONG, AND WHY IT MATTERS MORE THAN THE ERROR.** The gating audit found a
dominant option at the convener's seat — *refuse publicly and take a deposit, or say nothing at no cost
at all* — and this document accepted it and engineered a repair: lapse and supersession would emit
witnessable events, and refusal would be terminal where burial was not. **Every part of that is wrong.**

- **The premise is false on disk.** Burial is not silence; it is `compose_agenda`, which costs an act
  and deposits on the omitter by name. The audit reached its finding by reading `05:314-316`'s **lapse**
  — which genuinely is *"not an act by anybody"* — and generalising it to burial, which is a different
  operation performed by a different rule three pages earlier.
- **The repair's own mechanism does not hold either.** *A refusal is terminal* was cited to faults F2 and
  F5; **`08:147` gives F2 the severity `descend`, which concedes a rung and closes nothing**, and
  **`08:150` defeats F5 with any new `support[]`** — which a subsistence petitioner has every season by
  construction, because the deposit reads `shortfall_at_raising` and the famine is deepening.
- **And the recurrence cost fell on the wrong person.** Re-filing costs the *petitioner* an act — his
  only act that season. A war of attrition priced against the challenger is not a repair.

**The invented emission is therefore deleted, not kept alongside a refuted premise.** A sitting is
already an event; whoever was present sees which items were reached; and where no sitting happened at
all, the design's answer is §13.1's, which is that nothing happening is the characteristic outcome and
manufacturing an event there would be manufacturing visibility the design deliberately withholds.

**THE ONE ASYMMETRY THAT SURVIVES, and it is priced rather than asserted.** Refusal and burial do not
have the same *gain*:

| | the matter | the risk to the convener | the cost |
|---|---|---|---|
| **hear it and refuse** | decided | **it may be decided against him** — the venue's `decide_rule` is not always his, and a heard matter can be granted | a deposit, plus an item of `capacity(date)` spent on a matter he did not want |
| **omit it** | not decided | **none.** Nothing can be granted at a sitting it never reached | a deposit, on the same rule, as and when the backers learn |

**So burial is not free and never was; it is merely SAFE.** That is the correct incentive and the design
intends it — it is why the convening office is *"worth holding, worth conferring, worth revoking, and
worth killing for"* (`05:218-224`). What follows for play is §8.3's: **the counter to a burying convener
is not a mechanism, it is another door**, and burying only wins outright where the obstructor controls
every venue that could hear the matter.

**And one residual limit stands, unrepaired (§15.3):** the deposit on an omitting convener is contingent
on the backers **learning**, exactly like every other deposit in the design. Where nobody tells them, the
burial is unpunished — not because it is unpriced, but because the design's epistemics are the price.

### §8.5 A petition expires — and the evaluator is a person

**A petition ends in one of two ways — and at one kind of respondent it does not end at all.**

1. **LAPSE.** The date passed and it was not heard. The trigger is a date — container-local and
   calendar-readable — and this is the one licensed decider-free resolution in the whole design (§13.2).
2. **SUPERSESSION, moved and decided at a venue.** Any party, or the convener, may **move that the matter
   is moot**. It is an ordinary motion on the stasis ladder (§12), pleaded from claims the mover actually
   holds, contestable like any claim, decided by the venue's `decide_rule`, and recorded. It is pleaded
   against the matter's own docketed item and consumes no additional `capacity(date)`; what it costs the
   mover is **an act**.
3. ⚠ **AND A THIRD CASE THE EARLIER VERSION OF THIS DOCUMENT DENIED (C-4): AT A ROOTLESS VACANT OFFICE,
   IT NEVER ENDS.** Both routes above need a date. §8.6 supplies one wherever a vacancy resolves at a
   parent office or at a container. **Where an office is at the root of its own cluster and its conferral
   basis names neither, there is no date, so the petition cannot lapse and there is no venue at which to
   move it moot.** It sits, indefinitely. That is S19, it is not repaired here, and §15.16 and §16 carry
   it. A document claiming *"there is no third"* while shipping the respondent type that creates it was
   asserting closure it had not earned.

**This rules the contradiction the earlier work carried.** #342's shape said in one section that a seat
*filled by other means* supersedes a conferral petition, and in another that **no petition cancels
another, because that would be an engine deciding a person's options.** Both cannot stand. **The second
wins.** A seat filled by other means is not an expiry; it is a **ground** for a motion that the matter is
moot, which somebody must make, and which the petitioner may contest.

⚠ **The rule is about CANCELLATION BY A STATE OF THE WORLD, not about endings generally (C-21).** Lapse
is precisely an ending with no person in it, and it stays. The precise claim is: **no petition is ended
by a fact about the world; it ends by a date passing, or by a person's motion.**

**Why the alternative was unbuildable.** *"The proposition is no longer live"* has **no referent in the
state model**: famine is not stored, propositions are free-form, and liveness is a semantic judgment.
Evaluated by the engine it is either a forbidden stored world-condition or an omniscient oracle — which
is §13.1's *"GM hiding in the engine"* exactly. Evaluated by a person at a venue, from claims he holds,
it is an argument, and the design already has an argument system with named faults for people who plead
things they cannot support.

**What expiry buys, which is a great deal for one rule.** Time pressure on petitioners with no threshold
anywhere — getting heard *soon* matters because the thing you are asking about can stop existing. The
up-stroke becomes lossy in a way that is true to the fiction. And **it prices absence honestly: the cost
of an unfilled seat becomes visible in the petitions that died in it.**

**And supersession is relocation, not decay.** The granary does not stop mattering; it matters
*somewhere else* now, and someone there is asking for the same thing with a better claim on it. **The
contested stake relocates**, with no authoring — you can win the argument and find the prize has moved.
That composes with §7: the granary being needed elsewhere is a *condition*, so it can schedule a sitting
there. Your loss is somebody else's agenda item, and both are the same mechanism.

### §8.6 The vacant office, and vacancy by absence

**A vacant office is not a defect to route around. It is the design's most characteristic outcome, and it
needed consequences rather than elimination.**

> Nothing happening **is** something happening to the petitioner. Food is never sent during the famine.
> Instructions never reach the garrison commander. The grain sits in a granary whose praefect is dead and
> unreplaced, and people starve inside a system working exactly as written.

A petition filed against a vacant office is filed and waits. A conferral date that fires with no convener
is a date nobody is ordering. A three-of-four conclave with two seats empty and a third vacancy pending
is **not a soft-lock**; it is a Church that stalls, and breaking the stall is political work for
characters — a schism, a Crown intervention, an off-map appeal. **Stories, not a mechanism.** The
enlargements exist to price that outcome, never to prevent it.

**Vacancy by absence** is the one place where §7 supplies a genuinely new consequence here. A convening
condition may be written over **presence at the container across the seat's existing horizon table** —
presence is already a substrate roll-up, so the world already knows where bodies are — which, when true,
schedules a vacancy date. It composes where an `exercise`-based predicate did not: `exercise` is
identically zero at a hearth, which has no remit, while **presence is defined at every rung because every
rung has bodies in it.**

What it buys in play: *"make him absent instead of killing him"* — the setting's whole hostage politics —
currently has no mechanical consequence at the hearth rung, because a living absent holder freezes a seat
indefinitely. With it, absence costs a seat. **And the repricing fires on the King's household first**,
which is the correct place for it to bite. Its two falsifiers are named and not run: the deliberate
absence (a head wintering elsewhere, who should not lose his seat) and the hostage repricing's cost at
the top of the ladder.

### §8.7 Grievance, and the road to revolt

**There is no revolt object and no revolt meter.** Grievance is a stance row with a negative attitude
toward a container or a person. Its only mechanical role: a person weighing `commit(p, f, +Δ)` toward a
faction whose proposition opposes the referent they hold grievance toward values that commitment by their
grievance magnitude. **Grievance makes commitment cheap.**

Revolt is therefore many persons committing to a rival proposition until that faction's density at a
node crosses what the settlement's coercive apparatus there can hold — and the people doing it have
names, hearths, and a specific man they blame. A threshold would let the world revolt without anyone
having decided to.

**Suppression makes it worse, and it needs no flag.** ⚠ #342 writes this with a `DORMANT` flag and a
stored re-arm predicate — and §7.2 has just ruled that **there is no flag object**, so shipping one here
would relocate the straddle rather than end it (C-7). Restated in the ruled form, with identical
behaviour:

> A suppressed grievance is **an ordinary stance row at full magnitude whose act-proposition has an
> unmet enabling claim.** It is present the whole time. It does not enter valuation while the enabling
> claim is missing — so the suppression genuinely *worked* — and it enters the moment a claim satisfying
> it lands in the holder's ledger, **at its full magnitude, because nothing ever reduced it.** No flag is
> set, nothing is stored beyond the row, and the "re-arm predicate" is just the proposition's own
> enabling condition, recomputed at P0 like every other option (§6.2).

Rows are inherited at reduced magnitude on succession, so the effect is generational with no generational
mechanism. **Each collision fires lower than the last, and the accumulator does not reset because nothing
resets it.** This is not a settlement gauge: there is no number on Goldenfurt, only rows in the stance
tables of named persons in it, and if those persons die without heirs the rows die with them.

---

## §9 · THE DOWN-STROKE

### §9.1 The dispensation

`Dispensation(issuer, proposition, scope, terms)` (`06:23`) — a change to what a container permits, costs
or requires. **Issuer** is a person holding office, or two such persons for a treaty; **scope** is a list
of containment nodes. There is no bare *effect* field: every term is typed — `PriceTerm`, `ProhibitionTerm`,
`LevyTerm`, `ExemptionTerm`, `EntryStandardTerm`, `ExcommunicationTerm`, `BlockadeTerm`, `TreatyClause`,
`OrdenanzaTerm`. Cut the typed table and every downward effect degenerates into a modifier on a hidden
formula nobody in the world could name, and therefore nobody can reason about, evade, or exploit.

**It travels by being noticed, not by being handed down a chain of posts.** Publishing is a telling
(§3), depositing claims into ledgers by **presence and channel** — the crier, the priest, the guild
notice, the market, a Knot. A person with no post receives it because deposit is never by post.
**Distortion in transit is free:** what reaches the hamlet is often not what the Duke signed.

Then nothing further is needed. The person's own need plus capability plus this new claim yields an
**opening** — `opening_set(person)`, *"exactly one routine, and it is the same routine that lists any
person's available acts at any time, not a new one keyed off Dispensations"* (`06:128-135`), now
evaluated over changed terms. A blockade raises the price of salt; the fisher's son with a boat and a smuggler cousin
sees a run worth making, and **no one authored an opportunity for him.**

### §9.2 A published dispensation does not apply — it lands as a compliance contest

Per relevant node, `contest(container, prize = compliance-here, claimants = {enforcement, resistance})`
— the same function that resolves sibling rivalry (`06:93-96`). No second resolver. The roll reads
**enforcer_presence** (is a person in the issuer's employ actually stationed or dispatched here — zero if
the issuer has no one to send), **local judging-set stance** (derived on demand, never stored), and
**distance**. Failure is never an exception: partial compliance resolved per hearth, quiet evasion, open
defiance, local countermanding by a rival dispensation, or arrears compounding toward the next standing
date.

### §9.3 One order, many executors

**Up-stroke: one want, many addressees (§8.3). Down-stroke: one order, many executors.** Neither is a
channel; both are a set of independent relationships between named persons.

The King issues one dispensation and **what happens is thirty-five separate things**, because
thirty-five praefects, governors and stewards each have to notice it, read it and decide. Compliance is
per-person and per-place, and the roll happens **once per executor**, not once for the realm. So the same
order produces thirty-five different outcomes — which is the design's central thesis, no omniscience and
per-person interpretation, finally applied to the down-stroke instead of only to knowledge.

**Three rules, and the third is the whole of it:**

1. **Scope enumerates executors, not places.** A dispensation scoped *Varfell* resolves against each
   office responsible within Varfell, one compliance decision each.
2. **Delivery is not assumed.** An executor who never received it does not resolve at all — **distinct
   from one who received it and refused**, and the two are indistinguishable from above without an act
   that goes and looks.
3. **Reports are claims, not state.** *"Compliance was rendered"* is a claim by a named person, with all
   the ordinary properties of claims. It can be false, and it is what the centre has instead of knowledge.

**The seats this makes playable**, which the coverage exercise found thin everywhere: the praefect who
**slow-walks** (complies at the letter, at the latest date, with the narrowest reading); the governor who
**over-enforces** to be seen doing it and manufactures a grievance the King never wanted; the steward who
**reports compliance he did not perform**, because a claim is what travels upward and nobody has come to
look; and the one who **complies exactly and is ruined for it**, because his neighbours did not. None of
these needs a new verb. **The middle of the hierarchy stops being a pipe and becomes the place the game
happens.**

**And a directive may carry a reporting date** — *render account at the tithe reckoning*. ⚠ **That is a
date the issuing act SETS, not a convening condition** (C-8): it carries no predicate, it is scheduled
unconditionally by the person who issued the dispensation, and it is an ordinary `convene` performed as a
term. It is not a fifth instance of §7 — §7.2 says there are **zero** — and it places no item on anyone's
agenda, which §7.4 forbids. What it does is surface non-compliance **at a date, where a person decides
what to do about it**, and the deciding is still `compose_agenda` plus a determination.

### §9.4 Vacancy propagates at telling speed

When an office empties, nothing is written to the world; four things become true by computation, and all
four run **at telling speed, not in the same tick**. Every standing dispensation the holder issued keeps
its terms and loses its complier — but compliance drops for each person **as and when a claim of the death
reaches them, and not one moment before.** A synchronous drop would be a polity-facing quantity computed
off true world state, so persons would react to a death they had not heard of.

The correction buys the thing the design wanted anyway: **a withheld death-notice becomes one of the most
powerful acts in the game.** The household that keeps the Duke's body quiet for a season keeps his
dispensations enforced for a season, and the interregnum is smeared along the channels — three days to
the capital, six weeks to the fjord hamlets — so *the map of where obedience has lapsed is exactly the map
of where the news has gone.*

The other three: `licensed_standing` goes to zero on the same rule (the establishment is simply first to
know, being nearest the body); **the office's seat items go unspent**, so every petition queued behind
that seat waits a full standing date and the grievance deposit fires on backers who were not refused but
simply not heard; and a conferral standing date opens at the horizon the holder carries.

---

## §10 · MATTER, THE COMMONS, AND OPTION REMOVAL *(enlargement 3)*

### §10.1 The inversion

The obvious way to model a degrading commons is a place-scoped scalar entering every actor's obstacle.
That is a **flat amount** read as a **modifier** — the wrong side of §14's anti-leverage row on both
counts, and it has no clearance argument.

> **Invert it. Damage to a commons REMOVES AN OPTION. It never adds difficulty.**

This is the exact shape the design already licenses in the other direction — practice rank *adds verbs to
the option list* — and it is what §14's own gloss asks for: *fractions rather than flat amounts,
option-set changes rather than modifiers* (`11:255`).

- A silted harbour does not make sailing harder. It makes **some cargo impossible**, so a different act
  must be chosen.
- A worked-out seam does not raise an obstacle. **The verb that drew from it is gone.**
- Degradation is legible without a gauge: **you can see which verbs are missing.**

Second-order behaviour nobody has to design: because the loss is an option and not a number, **the people
who notice first are the ones whose practice used that verb** — and *"the seam must be restored"* is a
proposition, and the people whose practice used it are already committed to it, so **a political faction
forms out of a physical fact with no authoring at all** (§1.3's faction object, unchanged).

### §10.2 The object, and where its state lives

A **site** is matter the design already owns: a holding, a route, a seam, a channel, a fishery.
`condition(site) ∈ [0, 1]`. Acts touch it through the existing `alter` and `exclude` modes (§6.4); no new
mode is introduced.

> **CROSS-RUNG SEMANTICS — three rules, all composing on R-1 (§4.2):**
> 1. **Primary state lives at the finest node the act names.**
> 2. **Any coarser read is computed on demand.**
> 3. **No coarser rung stores one.**
>
> **The aggregation function is a draw-weighted mean:**
> ```
> condition(n) = Σ_{c ∈ children(n)} condition(c) × draw_share(c, n)
> ```
> where `draw_share` is the child's share of the parent's draw for the relevant good — the same weight
> the larder already computes (§11.1).

**Why a draw-weighted mean and not a sum or a minimum.** What a rung's option set depends on is whether
the rung *as a whole* can still support the verb. A minimum would close a settlement's harbour because one
hearth's boat rotted. A sum is not a condition. Without these three rules the object recreates the defect
it was built to avoid, in mirrored form: **a degraded hearth invisible inside a pristine settlement, and a
condition that is non-zero only at the rung an act happened to name.**

### §10.3 The sizing rule

**Both repair routes end at the same missing thing, and it is this.**

```
Δcondition(site) = − condition(site) × f(degree) × share(actor, site)     -- resolved in P5 (§6.3)

f(Disaster) = f(Failure) = 0 ·  f(Costed) = 1/16 ·  f(Clean) = 1/8 ·  f(Overwhelming) = 1/4
share(actor, site) = the actor's own draw from the site ÷ the site's total draw   ∈ (0, 1]
```

**What the bound means, stated precisely, because the loose version of it is false (C-10):**

> **You can never move more of a site than your own share of it, times a degree fraction.** That is the
> whole claim, and it is exactly `02:211-213`'s *"a fraction of the container's own capacity … sized to
> the container"*.

Two consequences, and the second is the one an earlier version of this document got wrong:

- **At a commons with many drawers, single-act closure is impossible.** One boat among a harbour's forty
  moves at most a fortieth of a quarter of the harbour's condition in a maximum-degree season. **Closure
  is a collective outcome** — many actors, many seasons, crossing a band edge — which is the
  tragedy-of-the-commons shape the mechanism exists to produce: many rational private acts making
  everyone's practice worse, including the actor's.
- ⚠ **At a site with a single drawer, `share = 1`, and one Overwhelming season moves a quarter of the
  condition.** The earlier claim *"a single act never closes an option"* is **false there** and is
  withdrawn. **But this is correct behaviour, not leverage**, and the anti-leverage row says why: it
  forbids *"a personal effect on a group that is not a fraction of that group"* — and at `share = 1`
  **there is no group.** A man working out his own hearth's private seam in one hard season is wrecking
  his own property, and a design that stopped him would be modelling a commons where there is none.

**Falsifier, and it is the one to run:** *one person, one season, maximum-degree `alter` at a site with N
drawers — what fraction of the site's condition moved, and how does it scale with N?* It must be
`≤ 1/4 × share`, and it must **fall as N rises**. If it does not fall with N, the object has leverage and
violates the precedent.

**Deliberate discrete destruction is a different mode, and this document does NOT claim it is cleared.**
Burning a granary or blocking a channel is `exclude`, not `alter`: a contested physical act against
whoever defends the site.

⚠ **The `forestall` precedent does not transfer, and citing it was wrong (C-11).** `forestall` is **a
purchase** — it *"requires … `stores(hearth(person))` sufficient to buy it outright"* and the goods
survive, in the forestaller's own stores (`13:141-144`). Its bound is the actor's ability to pay, and its
effect is a transfer of possession. **Arson has no purchase price and destroys the goods.** The two are
not the same shape and the first does not license the second.

> **So the discrete limb is DEMOTED to a stated limit (§15.17).** One person destroying an undefended
> shared thing is expressible, is bounded only by the `contest` against whoever defends it, and where
> nothing defends it there is no bound at all. **This document does not repair that, and it does not
> introduce it either** — `12`'s willingness table already prices `burn` as a severity level, so the
> shape ships in #342 and this enlargement inherits it. Naming it is the honest move; inventing a bound
> for it here would be inventing a rule for a case the design has already decided to allow.

### §10.4 Band gating, and what `depletion` actually is

**Option closure is band-gated:**
```
verbs(site, n) = { v : condition(n) ≥ floor(v) }
```
Bands are published in full with their inputs and **never with the trigger point that separates one band
from the next**, which is the discipline the larder already runs on (`13:31-32`).

**#342's two slow fuses — ore grade and siltation — are written to run *"every season"* in no phase at
all, and `depletion` appears only as a subtrahend with no definition anywhere** (`13:166-169`,
`13:178-181`). This document closes that, and the earlier version's closure was dimensionally and
directionally wrong (C-9): it subtracted a delta on `condition ∈ [0,1]` from `base(H)`, a yield quantity,
and because the delta is already negative, `base −= Σ(negative)` made **working the seam enrich it.**

> **THE CORRECTED FORM. `base(H)` does not move. `condition` is a multiplier on yield.**
> ```
> yield(H, season) = base(H) × condition(site(H)) × season_factor(territory)
>
> condition(site) +=  Σ (this season's resolved condition deltas at the site)     -- P5, acts
> condition(site) +=  nature's term, via season_factor                            -- P1, weather
> ```
> `alter` deltas are negative; restoration acts are positive; nothing else moves it. Units are consistent
> because `condition` is dimensionless and never leaves `[0,1]`, and the sign is correct because the
> deltas are added, not subtracted.

**So `depletion` is redefined rather than defined:** #342 made it a subtrahend on `base`; here `base` is
constant and depletion **is** the accumulated condition delta. The seam runs out because people worked it,
which is the story the mechanism exists to tell.

⚠ **And the "no authored per-season constant" claim comes off (C-9).** There *is* a non-act term — nature's
— and pretending otherwise was an overclaim. What is true, and is the point worth keeping: **the non-act
term is weather, it is licensed under §13.2 row 1, and it enters through the shipped `season_factor`
rather than through a bespoke per-fuse constant.** Siltation is the same line: accrual is `season_factor`
against the dredging acts that were actually performed and funded.

### §10.5 Exposure, band-quantized

**The obstacle term derived from a site's condition is the band's representative value, never the scalar**
— §5.4's exposure rule, and this is the case that forced it. Without it, the odds preview is a free,
act-free, witness-free probe of hidden world state that only the player can run.

### §10.6 The matter-channel licence, claimed explicitly

**A band edge closing a verb is, by §14's own words, a threshold that fires an outcome.** That row is real
and this document does not pretend otherwise. **The licence is the matter channel, and it is claimed here
rather than assumed**, under three conditions, all of which must hold:

1. **The quantity crossed is matter or bodies — never a social quantity.** The design admits exactly three
   clock-driven quantities: matter, bodies, and the confidence of a memory (`09:562-564`). Standing,
   regard, grievance, cohesion and commitment move only when an act causes an event, and no band edge may
   ever be defined over one of them.
2. **What changes at the edge is an OPTION SET — never a roll term and never an outcome.** Nobody wins or
   loses at a band edge. A verb leaves a list, and a person must now choose differently.
3. **The closure is an event, witnessable by presence at the site.** It has a place and a season, and the
   people who were there can see it; everybody else learns by telling, like everything else.

Under those three, this is the same channel the design already ships and already licenses: a storm plus a
generation of silt closing a channel is a decider-free, state-plus-weather event forcing a realm-scale
crisis, and nobody has ever read it as an actor. **A social threshold remains forbidden. A material one is
the world having weather.**

---

## §11 · THE TRANSFER ACT *(enlargement 4)*

### §11.1 The larder, and the hole

```
mouths(h) = Σ appetite(p)                  stores(h) += draw(h) − mouths(h)
draw(h)   = Σ yield(H, season) − Σ levy(d, h)      margin(h) = stores(h) / mouths(h)
```

Bands run Provisioned → Sufficient → Thin → Hungry → Failing. A shortfall fires no event; it raises
`need(p, subsistence)`, which outweighs stance entirely once it exceeds 1.0, and a person with no office
reaches for one of five channels: requisition kin, petition, take an opening, migrate, or commit to a
rival proposition.

**The hole the testing found is that there is no act by which one person gives another person anything
unsolicited.** `requisition` surfaces another person's act as theirs to refuse, which is a real channel —
but it is a *demand on kin*, and its compliance act presupposes an undefined transfer verb. And the
coercion layer spends coin as live mechanism throughout — retinues costing *coin per season, at a standing
date* (`12:149-151`), *a standing date each season at which coin is due* (`12:510`), *his needs are
computed from a larder that the coin was filling* (`12:516-517`) — while the material layer **refuses a
currency** (`13:285-287`). **The coercion document's central fork rests on an object the material document
refuses to model.** That is a hole in the design, verified line by line with both arms load-bearing; it is
not a filing artifact of a seventeen-document suite.

### §11.2 The act, and the yield term

```
transfer(giver, receiver, amount)          -- amount in the SAME `stores` scalar, mouth-seasons
   precondition: giver and receiver co-present, OR the amount is entrusted to a carrier act
   effect:  stores(hearth(giver)) −= amount ;  stores(hearth(receiver)) += amount
   witnessed: by presence, per person, like any other act

draw(h) = Σ yield(H, season) − Σ levy(d, h) + Σ transfers_in(h) − Σ transfers_out(h)
```

**One clean act plus one yield term. Not a currency.** And a transfer at a distance is a *carrying act* on
the same EV shape the design already uses for a smuggler's run, so it can fail, be skimmed, or arrive
somewhere else — which is what makes a distribution order disobeyable **in the interesting way:
partially** (§9.3).

**What it opens:** the wage-labourer, the bribe, the purchase (a pair of transfers, §11.5), the mercenary,
the corrupt official — **the unsolicited give, the wage and the purchase**, which is exactly the hole the
review narrowed the claim to.

⚠ **What it does NOT open, and an earlier version of this document claimed it did: a material verb for a
person who had none.** That was false and it was a repair of a low end this document twice says it does
not repair (C-14). `13:31-35` gives a person with no office **five** channels — requisition kin, petition,
take an opening, migrate, commit to a rival proposition — and this document quotes them three paragraphs
earlier. **The transfer act changes what can reach a postless person, not what he can do.** Its bearing on
the compliance target's third structural test (*a person with no office can act, petition, and receive an
opportunity*, `11:237-238`) is on the **third limb only**: without it the only thing that can ever reach
you is a dispensation from your own hierarchy, so nothing a stranger does can land on you.

### §11.3 Two attacks that fail, and one claim that comes off

**It does not reopen the currency refusal.** That refusal's stated ground is *"a second unit needing
conversion has no throughline reading it"* (`13:285-287`). A transfer denominates in **the same `stores`
scalar the larder already banks in mouth-seasons.** No second unit, no conversion, ground untouched.

**It does not make bribery inexpressible.** *A transfer is witnessed* was attacked as abolishing the
secret payment. It fails: `witness` is **per-person and presence-based** (§1.4), so a back-room transfer
has exactly its two witnesses and no others. The bribe survives, and it survives as a fact some people
hold and others deny — which is better than a hidden flag.

**And one overclaim comes off.** The transfer act makes the coercion layer's arithmetic **expressible**,
not *implementable*. Doc 12's numbers are coin-denominated throughout, and re-denominating every retinue
cost, arrears schedule and wage into mouth-seasons is **unwritten work**, not a consequence of this act.

⚠ **D-2 again (§6.1).** If a transfer is an act and a person has one act per season, **a lord who pays his
retinue has spent his season.** Under a multi-act reading the objection vanishes. This enlargement's
economics cannot be settled before D-2 is.

### §11.4 `stores` as the realm's denominator is a LIVE CHOICE, not an assumption

Mouth-seasons are **perishable and bulky**. A realm-scale standing contract paid in perishables makes
mercenary retention hostage to transport, and a besieging army's wage bill becomes a logistics problem
rather than a ledger entry. **Two defensible answers, materially different games:**

- **Accept it as a feature.** Force is logistics-real: you can only retain what you can *feed where they
  stand*, which is historically true and mechanically rich, and it makes the transport network a political
  object.
- **Coin returns by the back door.** A fungible, transferable `stores` will function as money whether or
  not it is called that — the flavour of coin dies and the economics of coin comes back.

**Jordan must see this**, and §16 carries it. This document does not choose.

### §11.5 The market path fails as filed; the gift path constructs

**The gift path constructs, step by step, every step shipped or in this document:** famine at a hamlet is
metabolism (§6.2, P1) → locals witness it (§1.4) → claims travel by tellings (§3) → a rival lord who never
met them holds those claims → his stance emits a proposition → he **transfers** stores (§11.2) → grain
reaches hearths that never petitioned him. **Unintended rescue, with every effect tracing to a
self-interested act.**

**The market path does not.** *A factor moving grain for profit because prices made this the destination*
requires two objects that do not exist:

1. **A price signal.** The design prices goods **only where a political act makes it matter this scene**,
   and refuses the continuous market by name. There is no standing price a factor can read at a distance
   and sail toward.
2. **Reciprocity.** *Profit* means receiving something back, which requires a second transfer **plus an
   agreement form binding the pair** — and the transfer act as specified is one-way.

> **STATED AS A LIMIT (§15): rescue-by-gift is reachable; rescue-by-market is asserted.** Making it
> reachable needs an exchange form — two transfers plus a binding — and that form is not written here and
> should not be smuggled in as a consequence of a one-way act.

---

## §12 · ARGUMENT AND THE SITTING

### §12.1 The proposition and the case

```
Proposition = (mood, subject, predicate, value, when, scope)      mood ∈ { HOLDS, OUGHT }
Case        = (holder, motion, rung, grounds[])
Ground      = (proposition, warrant, support[])   # support[] are claim ids from the holder's ledger
```

`HOLDS` is claim-shaped without the epistemic fields; `OUGHT` names a change in a container's terms.
`when` is a mandatory interval exactly as in §3.1, so **assertion and denial collide automatically** and
no rule is needed for *these two people disagree*.

### §12.2 Stasis, and defeat by named condition

Before choosing a tactic, a party diagnoses what the fight is about. Four rungs, strongest first:
**Denial** (it did not happen) · **Definition** (it happened; it is not *that*) · **Quality** (it happened,
it is that, and it was right) · **Jurisdiction** (this chamber may not hear it).

> **The position you stand on is what you conceded, and how you arrived there does not matter.** Opening
> at rung *r* writes every rung above *r* into the record as conceded, exactly as descending to *r* would.
> Descending is irrevocable and public.

**Resolution is by named fault against a checklist, not by a persuasion threshold**, and every fault is
computable from case state and ledgers — which is what lets the whole thing run headless with no GM.
Twelve faults (`08:146-157`), each with a severity: **F1** self-contradiction *(close)* · **F2**
contradicting the record *(descend)* · **F3** silence when pressed *(close)* · **F4** shifting the ground
*(descend)* · **F5** repetition, *defeated by any new `support[]`* *(strike)* · **F6** the quibble
*(close)* · **F7** rootless ground *(strike)* · **F8** conceding and pressing anyway *(close)* · **F9**
deficient pleading *(close)* · **F10** speaking without standing *(strike)* · **F11** incoherent assertion
*(strike)* · **F12** inadmissible challenge *(descend)*. `strike` kills the ground at every venue for
everyone; `descend` concedes a rung and **closes nothing**; `close` force-closes the sitting against the
faulting party.

⚠ **Those two severities are printed here because getting them wrong cost this document a whole invented
mechanism.** An earlier version built its dominance repair on *"a refused matter cannot be re-pleaded"*,
citing F2 and F5 — and **`08:147` gives F2 `descend`, which concedes and closes nothing, while `08:150`
lets any new `support[]` defeat F5**, which a petitioner in a deepening famine has every season by
construction. See §8.4 (C-1).

**Force-close is the normal ending.** A sitting that runs its full budget without a fault is the unusual
case. **Most arguments end because somebody was caught doing something that has a name** — and a
threshold roll cannot distinguish *he was wrong* from *he was caught lying*, which is the interesting one.

### §12.3 What the enlargements do to the argument layer

**The argument machinery stops being ornamental and becomes the resolution layer for everything above.**
It was built for a design that generated relatively few disputes. Now every rung generates them
constantly, and the sitting is where they are put:

- A **convening condition** firing is arguable — *whether the condition is really met* is a `HOLDS`
  proposition with a band on both sides of it.
- A **supersession motion** (§8.5) is an ordinary motion with ordinary faults, which is precisely why it
  is safe to have made a person the evaluator.
- A **lost verb** (§10) makes attribution of slow damage contestable: who caused it, was it inevitable,
  and who profits from which answer.
- A **transfer** (§11) is witnessed by whoever was present and by nobody else, which is exactly the fact
  some know and others deny.

### §12.4 The venue is parameterised, and the door is a predicate

`Venue = (container, prize, standing_date, judging_set_rule, decision_rule, admission_floor,
privileged_custody, exchange_budget, article_count, coupling_depth, veto_holders, record_custody)` — plus
the door: `(convener, enter, speak, admissible_source, attendance_cost)`, where `enter` and `speak` are
predicates over marks, office, standing and commitment degree.

Three things this buys:

- **Exclusion in Valoria is at the second gate, not the first.** A Southern Einhir fisher may walk into
  the Goldenfurt court. He may not *speak* unless a person with standing carries his petition. **Caste is
  not a locked door; it is a room you may stand in silently** — a far more accurate and far more playable
  shape than a ban, and it is one column.
- **The convener holds the cheapest real power in the game — cheap, but not free.** Ordering a sitting's
  items is `compose_agenda`, and a convener who puts three items ahead of yours has killed your petition
  without ever deciding it. ⚠ **`14 §5`'s gloss says he *"has spent nothing"*; doc 05 says he spent an act
  and takes a deposit** (`05:206-208`). **This document rules for doc 05** on §3.4's conflict rule — doc
  05's declared subject is carriage and the agenda — so the correct statement is: *influence measured in
  the volume of things filtered, held by a person with no binding power at all, at the price of one act a
  season and a grievance he cannot see coming.* §8.4 owns this.
- **`admissible_source` is a door for evidence, not a grade.** A venue that hears instruments only cannot
  be reached by forty hamlet witnesses; the chapter sitting that hears witnessed deed only cannot be
  reached by a document — which is why the Löwenritter is caste-open in fact and not by policy.

---

## §13 · NO FALLBACK · COINCIDENCE · THE EPISTEMIC PAYOFF

### §13.1 The rule, and what is genuinely new in it

> **THERE IS NO FALLBACK. If no person acts, the thing does not occur.** No distribution just happens, no
> garrison is assumed paid, no repair is presumed made. **The engine has no caretaker**, because there is
> no GM to be one.
>
> **Production is metabolism** — nature yields, larders consume, bodies age. No act required.
> **Distribution is politics** — grain moves because a named person decided it should. An act, always.

**Most of this was already enforced, and this document does not claim to have invented it.** The split
pre-exists in the spine: P1 excludes every social quantity by phase membership (`09:55-59`), granary
allocation is already a named office-holder at a standing date, and levies are already dispensations. The
principle is a *statement* of the spine, not an addition to it.

> **Its genuinely new content is ONE ruling, and it is worth having: VACANT-ALLOCATOR SEMANTICS.**
>
> **A standing date whose allocating office is vacant fires, allocates nothing, and lapses. The stock
> sits.** It is not redistributed, not held over, not split by default, not allocated by seniority or by
> any other engine rule. The claimants left unfed carry their mouths-deficit straight into their
> hearths' own need computation, by the ordinary larder line and with no crisis object anywhere.

That is the famine writing itself: the grain exists, the granary is full, the praefect is dead, no one has
been conferred, no sitting is convened, no dispensation is issued — **and people starve inside a system
that is working exactly as written.** Nobody did anything wrong. Nothing is authored.

**What it makes possible:** the **vacancy as a strategy** — keep the seat empty and the matters that
needed it die on their own (obstruction by omission, which is how institutions are actually strangled, and
it needs no new verb, only the guarantee that nothing fills the gap). **Neglect becomes attributable, where the
neglect took the form of an act.** A convener who omits an item performed `compose_agenda` and deposits
by name (§8.4); **a seat nobody filled performed nothing and deposits on nobody**, and that asymmetry is
real and is not repaired here (§15.3). **The starving petitioner has somewhere to go**: the
need does not vanish when the petition lapses, it rises. **And a functioning institution becomes visible
as an achievement**, because a non-functioning one is mechanically distinct rather than merely quieter.

### §13.2 The falsifier, and the complete exception list

> **Find a beneficial effect that no person's act produced.**

**Licensed exceptions — these four, and only these four:**

| # | channel | citation |
|---|---|---|
| 1 | **Metabolism and nature** — larders consume, crops yield, wounds close or fester, bodies age, weather happens | P1 (`09:55-59`) |
| 2 | **Matter events** — a storm, a silted channel, a worked-out seam; and §10.6's band-edge closure under its three conditions | `13:178-186`; §10.6 |
| 3 | **The confidence of a memory decaying** — the third admitted clock class | `09:562-564` |
| 4 | **The calendar — LAPSE ONLY.** A date passing with nothing done resolves a matter against whoever needed the affirmative act | `05:314-316`; §8.5 |

**The fourth is licensed narrowly and deliberately, and the two things it does not cover are the two that
mattered.** Licensing *the calendar* wholesale would wave through exactly the cases where the caretaker
question is live. So:

- **Supersession is NOT licensed by this row**, because §8.5 made it a motion by a named person at a venue.
- **A convening condition's scheduling is NOT licensed by this row**, because §7.3 C1 makes it trace to the
  act that set it.

Both were failures of this falsifier in the earlier work, and both are repaired at the mechanism rather
than excused at the exception list. **Lapse alone survives as a genuine decider-free resolution, and it is
shipped, load-bearing, and correct: a deadline that nobody can be blamed for is the whole reason deadlines
work.**

### §13.3 Coincidence is what no-fallback produces

The falsifier is easy to mis-state as *find a beneficial effect that occurs without a named person having
acted*. Consider a famine relieved by grain that arrives from nowhere anyone arranged: a lord who wanted to
be seen as generous, a captain who ran from a storm into the wrong harbour with a full hold. **All acts, by
named persons, for their own reasons — and not one of them intended to save these petitioners.**

> **Coincidence is not an exception to no-fallback. It is what no-fallback PRODUCES** when many people act
> for their own reasons in a world they share.

**And this matters more for play than the harms do.** §13.1's consequences are all ways for the world to
hurt you, and a world that only ever fails you by omission is grim and, worse, **predictable** — the player
learns that absence means loss and stops attending to it. A world where absence sometimes resolves in your
favour by accident is one where you have to keep watching, and where being saved is as unearned and as
memorable as being ruined. It is also the honest model: institutions fail people constantly, and people
also survive constantly for reasons no institution intended.

**Its hard prerequisite is §11.** Without a transfer act, the only thing that can ever reach you is a
dispensation from your own hierarchy — **so the world could harm you by omission and could never save you
by accident.** That is what makes the transfer act load-bearing on this whole register rather than a hole
in the material layer.

### §13.4 The epistemic payoff — the enlargements are fact factories

> **The knowledge layer was never the problem. It was already right.** Claims in ledgers, per-person
> `witness`, view assembly under a budget, corroboration that fails closed, telling as an act that degrades
> by type. **What it lacked was enough happening to disagree about.** A design where little occurs has a
> magnificent epistemics engine idling.

| enlargement | the fact it manufactures | why it is disputable |
|---|---|---|
| **convening conditions** | a matter arrives on a calendar | whether the condition is really met is arguable, and the sitting is where competing accounts must be put |
| **distributed directives** | thirty-five local outcomes | thirty-five local truths; the centre holds claims about them, not knowledge |
| **multi-petition** | several offices holding the same matter | competing accounts of who was asked, who answered, who was ignored — and each office's version flatters itself |
| **option removal** | a verb that used to work and now does not | attribution of slow damage is inherently contested: who caused it, was it inevitable, who profits from which answer |
| **the transfer act** | goods that moved between strangers | witnessed by whoever was present and by nobody else |
| **coincidence** | grain that arrived from nowhere anyone arranged | it has no single cause, so it has as many explanations as there are interested parties |

**The purest case, and the design's perfect disputable object, is non-delivery versus refusal (§9.3).** The
order did not take effect in Hafenmark. Two claims, both sincere, both consistent with everything anyone can
see: *the praefect defied the King* and *the order never arrived.* **Nobody can settle it from where they
stand.** The King has a ledger, not a dashboard. The praefect knows only his own side. The courier — if
there was one — may be dead, lying, or never dispatched. Settling it requires a named person to go and look,
and that person can be deceived.

This is not ambiguity decorating a mechanism. **It is structurally guaranteed by no-fallback**: because
nothing happens by default, **absence has no signature**, and an absence with no signature is the most
disputable thing a world can contain.

**And credit is constructed entirely out of claims.** After an unintended rescue the Duke says his petition
worked; the merchant says he sailed for profit and owes nobody thanks; the Confessor says it is providence;
the praefect says he arranged it, because nobody can prove he did not; and the person who actually made it
happen may never learn that they did. **Nobody is lying. There is no fact of the matter about credit — only
a fact about grain.** A whole political register arising from the absence of a narrator rather than from a
reputation stat.

**Two consequences that follow rather than being added:** a King's realm-picture **degrades by type, at
distance, through the number of mouths it passed through** — so a governor who is good at being believed
outranks one who is good at governing, and that is the game at the top of the ladder. And **field
investigation is the engine's answer to its own epistemics**, not a subsystem: when the same fact is
disputed and it matters, somebody goes and looks, which is an act, by a person, who can be lied to, whose
findings are claims like any other.

> **The loop closes.** Things happen because people act; nothing happens when they do not; both leave traces
> only in what people saw; what people saw is what they say; what they say is disputed; disputes are settled
> at sittings by named persons — **who are acting on claims that may be false.**

---

## §14 · WHAT IS REFUSED — THE FOURTEEN ROWS, WALKED

**The refusal list has fourteen rows, not twelve** (`11:209-222`). Every new object in §§7–11 is walked
against every row. *"Clear by gloss"* is not clearance; each row names the object that comes nearest it and
says why it does not cross.

| # | forbidden | the nearest new object, and the verdict |
|---|---|---|
| **1** | a `World` parameter on any decision function | **Clear.** No enlargement touches `choose`. A convening condition is evaluated in P0 by the calendar, never inside a decision. §7.1 |
| **2** | a `view_of(world, person)` that masks rather than assembles | **Clear.** No enlargement constructs a view. The one place a world quantity nearly leaked into a player's hands is the odds preview, closed by the exposure rule. §5.4 |
| **3** | any function taking `[Person]` and one `Event` | **Clear.** Nothing in §§7–11 fans an event to a set. A closure at a site (§10.6 condition 3), an omitted petition's deposit (§8.4) and a transfer (§11.2) are all witnessed **per person, by presence**, and the deposit on backers is explicitly *"as and when they learn"* (`05:207-208`) — a telling each, never a broadcast |
| **4** | a deposit into a cohort carrying a VALUE rather than a DISTRIBUTION | **The row whose own note says it exists because the defect passed every other row, so it is walked on its own terms — UNIFORMITY — and not by set-vs-value (C-12).** The option-set change itself is clean: a verb leaves the *site's* list and each person's `opening_set` is recomputed per person, so nothing is deposited into the cohort at all. **But the WITNESSING is where this row bites, and it needs a rule:** when a closure is witnessed by a cohort, **the cohort's claim stores the construal spread its members would have produced, and an individuating member DRAWS from it and never inherits it.** Whose fault the silting is, and whether it was inevitable, must vary inside the cohort exactly as it would vary between two named persons. §10.6, §3.1 |
| **5** | a pushed aggregate, or a field one is stored in | **Clear, and this is where the option-removal object had to be engineered rather than asserted.** Coarser conditions are computed on demand by the draw-weighted mean and **stored nowhere**; the primary scalar lives at the finest node an act names and is written only there. §10.2 |
| **6** | a stored aggregate, norm, density, unrest or reputation field | **Clear, and it forced two rulings and one table amendment.** `condition(site)` is *matter*, not an aggregate of persons — §4.2's amended Container row states the general line (**a container may hold matter and dates; never a social aggregate**) and owns it explicitly, which the four-row table did not. And the flag was ruled out of existence twice: at §7.2 for `banked_claims`, and at §8.7 for suppressed grievance, which #342 stores as a flag and this document does not |
| **7** | a knowledge value stored on the thing known | **Clear.** A site's condition is a physical fact, not knowledge of one. Who knows a harbour has silted is claims in ledgers, and the band is published while the scalar is readable by nobody. §10.5 |
| **8** | a second resolver, an auto-resolve formula, a fast path | **Clear.** No enlargement resolves anything. A supersession motion runs through the ordinary argument process; a transfer is an ordinary act; a compliance decision is the shipped `contest`. §8.5, §9.2 |
| **9** | a `tier`, `level` or `scale` field on a faction | **Clear.** Untouched. The faction that forms out of a lost verb is an ordinary proposition plus commitments, with a derived profile. §10.1 |
| **10** | a flat additive modifier from a person onto a roll | **Clear.** The option-removal inversion exists *precisely* to avoid this: damage never enters a roll as a term. Where a site's condition must reach an obstacle, it enters as a band representative, which is a substitution of the pool source, not an addend. §5.4, §10.1 |
| **11** | **a personal effect on a group that is not a fraction of that group** | **The `alter` limb is CLEAR and is what the whole of §10.3 exists for.** `Δ = −condition × f(degree) × share(actor, site)` is a degree-scaled fraction of the site's own condition, sized by the actor's own share — `02:211-213` verbatim — and the effect **falls as the number of drawers rises**, which is the property the row is really about. At `share = 1` there is no group, so the row does not apply. **The `exclude` limb is NOT CLEARED and is demoted to §15.17**: the `forestall` precedent does not transfer (it is a purchase, and the goods survive), and this document declines to invent a bound for a case #342 already allows. **Falsifier stated and runnable: §10.3** |
| **12** | a scheduled recovery tick on standing | **Clear, on the row's own subject.** The row governs **standing** — a social quantity — and no enlargement moves one on a clock: §10's only clock term is `season_factor`, which is weather, and §10.6 condition 1 forbids a band edge over any social quantity. No convening condition may be written over one either (§7.3 C4). *(This document does **not** claim §10.4 has no non-act term; it has one and it is nature's. C-9.)* |
| **13** | a per-entity branch anywhere in the resolver | **Clear.** Every enlargement is a rule over a type, never over a named entity: any office may be petitioned, any date may carry a condition, any site may lose a verb, any person may transfer. **The one place a branch was tempting was exempting Thread acts from the odds preview; §5.4 refuses that route by name.** |
| **14** | an authored per-person opportunity or quest object | **Clear, and improved.** A lost verb, a fired date and an arriving transfer all reach a person through the same computed `opening_set` that any dispensation reaches them through. Nothing is authored for anybody. §9.1, §10.1 |

**And §14's companion refusal, which binds this document as a whole:** *"validators over the design
documents, freshness checkers, guards on the guards, or any apparatus whose subject is the repository's own
process rather than the game"* (`11:243-245`). **This document proposes no validator, guard, register,
checker or process document, and its enlargements require none.**

Four structural tests remain the ones worth running, and none of them has been run because nothing executes
(`11:231-241`): no decision function can see the world · two witnesses of one event can disagree · **a
person with no office can act, petition, and receive an opportunity** (§11.2 is what makes the third limb
reachable) · order independence.

---

## §15 · STATED LIMITS

Every one of these is a thing this design **cannot currently do, or cannot currently justify.** They are
here so that nobody has to rediscover them, and so that no later document can cite this one as though they
were closed.

1. **Convening conditions are a NEW COMPOSITION, not the naming of a shipped pattern. There are zero exact
   shipped instances** (§7.2), and the one verbatim candidate dissolves under this document's own dormancy
   ruling. The object stands on its N-line alone.
2. **A convening condition schedules an occasion, not a hearing** (§7.4). The termination gain is
   materially weaker than the earlier work claimed.
3. **Burial is priced but its price is contingent, and OMISSION IS ASYMMETRIC WITH VACANCY** (§8.4,
   §13.1). An omitting convener deposits *"as and when they learn"*, so where nobody tells the backers he
   pays nothing — the design's epistemics are the price, and that is deliberate. **But a seat nobody
   filled performed no act at all and deposits on nobody**, so *"neglect becomes attributable"* holds for
   omission and **fails for vacancy**. This document does not repair that: manufacturing an event where
   nothing happened is manufacturing visibility §13.1 deliberately withholds.
4. **Petition expiry reads the world in neither of its two forms — and at a rootless vacant office there
   is a third case in which it never ends at all** (§8.5 case 3, §15.16). The intuitive alternative —
   *the world moved on, so the matter is moot* — is **unbuildable**: liveness has no referent in the state
   model, and an engine evaluating it is either a stored world-condition or an oracle.
5. **`stores`-as-realm-denominator is unresolved** (§11.4), and the coercion layer's coin-denominated
   arithmetic needs re-denominating into mouth-seasons before any of it computes. That is unwritten work.
6. **The market path to unintended rescue FAILS as filed** (§11.5). Gift constructs; market needs a price
   signal and an exchange form that do not exist.
7. **Every R-line is conditional on L-4** (the playable-seat list, which does not exist), and §8's
   additionally on **D-2** (the act economy). Under a multi-act reading of D-2, **petition-spray dominates**
   and §8.3's economics fail.
8. **The `:219` clearance in §14 row 11 is an argument, not a measurement.** Its falsifier is stated and
   runnable and **has not been run**, because nothing executes.
9. **The closure-axis count is not citable in its original form.** The cut is not *sitting versus counter*;
   it is ***a person's decision — dated or not — versus a state trigger with no decider***, and the honest
   figure is **12 stable + 3 label-disputed + 2½ lost, lane-1 scope only.** Both published versions of the
   13-member set had different membership and summed to the same number, which is why four downstream
   checks passed it.
10. **The instrument that found the missing objects detects ABSENCE, not FAILURE.** Every unit it scored
    LOST died on a missing *noun*; not one was scored LOST because a claimed composition failed to compose —
    **and nothing was executed, so a compositional failure was undetectable by construction.** No count of
    units "reproduced or transformed" is evidence that the compositions work.
11. **FOUR vocabulary collisions survive inside the design and are ruled rather than fixed** (§3.4): `K`,
    `exposure` (five senses, two of them the same concept implemented incompatibly and one refused by name
    in a neighbouring document), the **practice range** (0–5 against 0–7), and the **Thread term's
    placement** (inside the pool expression against a second pool through the same `roll`). This document
    picks one of each, records all four, and **retrofits none of them into #342.** *(An earlier version
    said two, and ruled the other two silently. C-16.)*
12. **The low end was tested and is right. It is not repaired here, and it must not be "fixed" later**
    (§2). But note that §8.5 and §13.1 **do** touch it — a bottom-rung petition can now die unheard — and
    **no section re-examines the postless season under the enlarged rules.** That work is open.
13. **`vacancy-by-absence` has two named falsifiers that have not been run** (§8.6): the deliberate absence,
    and the cost of the hostage repricing at the top of the ladder.
14. **Nothing in this document has executed.** No claim here is licensed by an execution artifact, and under
    `CLAUDE.md` §0.2 none of it is done.
15. **The pre-roll exposure partition is a publication rule, not a structural guarantee** (§5.4). Only its
    third row — where the scalar is never an operand — is enforced by construction. And **a resistance that
    is neither plainly material nor plainly stance-composed has no ruled row**: a forged document's
    quality, a fortification nobody has seen. This document does not invent one.
16. **S19 IS NOT REPAIRED, AND IT LIMITS ENLARGEMENT 2** (§8.5 case 3, §8.6). A conferral date opens *"at
    the horizon the container carries"* (`14:195`); an appointed office's vacancy resolves *"at the parent
    office"* (`14:325`); **so the horizon is carried by whatever holds the date, which is the substitution
    this document makes and argues rather than performing silently (C-22).** But an office at the root of
    its own cluster, whose conferral basis names neither a container nor a parent office, has **no clock**
    — and a petition filed there can neither lapse nor be moved moot. Review (a) says nobody has ruled
    whether that is the intended Consecration Crisis or a soft-lock, and this document does not rule it
    either (§16).
17. **The DISCRETE limb of option removal is NOT CLEARED against the anti-leverage row** (§10.3, §14 row
    11). One person destroying an undefended shared thing is bounded only by the `contest` against whoever
    defends it, and where nothing defends it there is no bound. The `forestall` precedent does not transfer
    — it is a purchase, and the goods survive. **#342 already allows this shape** (`12`'s willingness table
    prices `burn` as a severity), so this document inherits the gap rather than introducing it, and
    declines to invent a bound for a case the design has decided to allow.
18. **Doc 06 of #342 is not covered by the verified fact base** (`09_citation_ledger.md`'s own coverage
    note), so §9's citations into it are this document's own direct reads and have not been
    independently re-verified.

---

## §16 · LIVE CHOICES FOR JORDAN

Each is a genuine fork where two defensible answers lead to materially different games. None is a question
this document can answer from precedent or architecture, which is the test §0 of `CLAUDE.md` sets before
anything is escalated.

| # | the choice | the two games |
|---|---|---|
| **D-2** | **The act economy.** One act per season, or a holder's several? | **A personnel game** — a Duke picks one thing and chooses which of his people does it — **or a decree game**, where the top of the ladder sweeps. It decides whether a player-Duke experiences the top of the ladder as a promotion or a demotion, and it gates §8.3's and §11.3's economics. `14:91-92`'s `seat_items` is already a fourth per-holder capacity and gives a multi-act reading a live foothold |
| **§11.4** | **Is `stores` the realm's denominator?** | **Logistics-real force** — you retain only what you can feed where they stand, and the transport network becomes political — **or coin returns by the back door**, since a fungible transferable scalar functions as money whether or not it is called that |
| **§8.5** | **Is a rootless cluster vacancy the Consecration Crisis, or a soft-lock?** (S19) | **Content**: a Church that cannot fill a seat is the design working, and breaking the stall is political work for characters — §8.6's whole position. **A defect**: a petition that can neither lapse nor be mooted is a matter suspended forever, which is the failure §8.5 exists to end. Compose `14:239`'s three-of-four conclave with two seats already vacant and it is one death away. Review (a) states plainly that **nobody has ruled which**, and this document does not rule it either — it is the one place where the two readings lead to a materially different Church |
| **§10** | **Is the world dying or misunderstood?** | Whether slow material decline is a real trajectory the player must arrest, or a fact everyone reports wrongly. §10 makes both expressible and does not choose |
| **§2** | **The Coherence-0 ontology.** | Two incompatible readings ship — loss of capacity, versus *a person has become an object*. Three arcs and two named absences turn on it |
| **—** | **Off-board polities.** | Altonia and Schoenland exert real pressure from off the map. *Generate a person* and *allow an actorless pressure* are different games, and the second would be the only exception to §1.1 in the design |

---

## §17 · APPENDIX — WHAT THE TESTING CHANGED

### §17.1 What survived the test unchanged

The three signatures and the two structures. The single-parent derivation. The person's six fields and the
computed needs. The claim, the closed predicate vocabulary, the salience multiplication and corroboration
that fails closed. The roll, the obstacle's one owner and one unit, the degree bands. The two strokes.
Office as a mark plus a binding power, with the pool drawn from the establishment. The argument system's
stasis ladder and named faults. Cohorts as persons at coarse fidelity, and de-individuation by memory. Every
refusal in §14.

**And the low end.** The single largest finding of the testing exercise was a false one — that a postless
person had no verbs — and its collapse is a positive result. An untrained attempt is legal and is just a
small pool; rank *adds* verbs; the postless fisher's shortfall arithmetic is identical to a Duke's.

### §17.2 What the testing added

Four objects, in the order they earn their place: **convening conditions** (§7), **petition→office with
expiry and multiplicity** (§8), **option removal** (§10), **the transfer act** (§11). All four are the same
structural promotion — the standing date becomes the spine — seen from four sides.

### §17.3 What the testing took away, or corrected

| what was claimed | what is true |
|---|---|
| the calendar primitive is called *the watch* | **renamed to a convening condition.** *Watch* is doc 12's soldiery (`12:37`, `12:99`), and one word with two shipped meanings is a vocabulary failure this repository has already paid for |
| four shipped instances of the pattern | **zero.** Two halves ship; the composition never does. And the one verbatim candidate dissolves under the dormancy ruling (`09:641` beats `04:35`) |
| a petition's respondent is a standing date | **withdrawn.** A date cannot drop a petition. The respondent is a containment node or an office — always a person or a vacancy, never a mechanism |
| a seat filled by other means expires a petition | **ruled the other way.** Nothing cancels a petition automatically; a filled seat is a *ground* for a motion, which a person must make and the petitioner may contest |
| expiry is *the world moving on*, with no actor | **it needed an evaluator and now has one:** a named person moving at a venue, from claims he holds, contestable like any claim |
| the convener must convene or visibly refuse, and a refusal is witnessed | **the CLAIM was loose and the DEFECT found against it was false.** #342 already prices burial: `compose_agenda` costs an act (`05:206`) and deposits on the omitter by name (`05:207-208`, `05:211-216`). What is true is narrower: **burial is safe, not free** — omitting risks no grant, hearing does |
| *`witness` can see neglect* | **half.** It sees an omission, which is an act. **It cannot see a vacancy, which is not** — and that asymmetry stands unrepaired (§15.3) |
| lapse and supersession must emit witnessable events | **INVENTED AND DELETED.** It was engineered against the refuted dominance premise above, and its own mechanism failed too — F2 is `descend` and closes nothing (`08:147`), F5 falls to any new support (`08:150`), and the recurrence cost landed on the petitioner |
| the four-row ownership table needed an Office row | **it needed two.** The Container row also had to admit **matter** — `stores`, the pointer, `condition(site)` — which the shipped hearth already holds against `01:490-491`. The general line: a container may hold matter and dates, never a social aggregate |
| prices denominated in "the sitting's capacity" | **two shipped quantities, named and owned** (§4.3): `capacity(date)`, a container term consumed at the hearing, and `seat_items`, a holder property consumed at the filing. There was never a third |
| conferral is a live choice for Jordan | **ruled: office-rooted** (§4.5), because it has an architectural answer, and `CLAUDE.md` §0's fifth test forbids escalating one |
| a petition ends in exactly two ways | **two, plus a case where it does not end**: at an office at the root of its own cluster with no parent office, there is no date, so no lapse and no venue (§8.5 case 3). S19 is not repaired |
| the petition retyping *"closes the whole direction of play"* | **withdrawn.** It opens the door; S19 means there is not a room behind every one |
| the watch dissolves the cluster-vacancy deadlock | **retracted.** The deadlock is content, not a bug. A stalled Church is the design working |
| commons damage is a scalar entering an obstacle | **inverted.** It removes an option, with a sizing rule, cross-rung semantics, an aggregation function, and band-quantized exposure |
| the slow fuses run every season | **`condition` is a MULTIPLIER on yield and `base(H)` does not move.** The first attempt at this subtracted a `[0,1]` delta from a yield quantity **and had the sign inverted, so working a seam enriched it**. Acts' deltas resolve in P5; nature's enters P1 through `season_factor` |
| there is no authored per-season constant in the fuses | **overclaim, withdrawn.** There is a non-act term and it is nature's; what is true is that it enters through the shipped `season_factor` rather than a bespoke per-fuse constant |
| a single act never closes an option | **false at a single-drawer site**, where `share = 1` and one Overwhelming season moves a quarter. **Correct behaviour, not leverage** — at `share = 1` there is no group for the anti-leverage row to protect |
| the discrete limb is cleared by the `forestall` precedent | **it is not.** `forestall` is a purchase and the goods survive; arson has no price and destroys them. Demoted to a stated limit (§15.17) |
| the exposure rule is self-enforcing | **only one of its four rows is.** The rest are publication rules, and the opposed contest's pool stays published on `10:132`'s stated policy |
| the transfer act gives the holdingless a material verb they did not have | **false, and a low-end repair.** `13:31-35` gives five channels. It changes what can REACH a postless person, not what he can do |
| the transfer act makes the coercion arithmetic *implementable* | **expressible.** Re-denomination is unwritten work |
| no-fallback is a spine the earlier documents did not carry | **it restates what phase membership already enforced.** Its one genuinely new ruling is vacant-allocator semantics |
| the exception list has two members | **four**, and the calendar's membership is narrowed to lapse alone, because supersession and scheduling were repaired at the mechanism instead |
| there is no act by which one person gives another anything | **overstated.** `requisition` surfaces another person's act as theirs to refuse, and a person with no office has five channels. The real hole is narrower and real: **the unsolicited give, the wage, and the purchase** |
| unintended rescue arrives by market | **half.** The gift path constructs; the market path needs objects that do not exist |
| *13 of 18 arcs close at a sitting; 3 at a counter* | **not citable.** 12 stable + 3 label-disputed + 2½ lost, lane-1 scope, and the axis is decision-versus-trigger, not sitting-versus-counter |

### §17.4 Four findings from the testing that have design content and are NOT dispositioned here

Recorded so they do not vanish a second time, which is how a backlog forms:

1. **The ESTABLISHMENT capacity object.** The design has no finite, contested, durable capacity object for
   *the named persons an office employs* — it prices remit and forgets establishment. Two independent
   exercises named the same hole. ⚠ **Narrowed from the form it was filed in**, which said *"at any
   rung"*: §4.3's two quantities are finite, contested and durable, so the finding is about establishment
   specifically and not about capacity generally (C-3).
2. **The Coherence-0 ontology contradiction** (§16).
3. **The `burden` term's calibration** — doing more dramatic work than any single coefficient in the suite,
   and untested by either exercise.
4. **The procedure-referent question.** Stance referents are `Person | Faction | Proposition | Place`, and a
   *procedure* is not among them, while at least one canon body is made of one. **Likely answerable by
   precedent** — *the rules of order as they stand* is expressible as a Proposition — which makes it a
   design-document answer rather than a Jordan question.

### §17.5 The relay's change log

This document is the product of an iterative agonist–antagonist relay: the antagonist challenges the
**output** and writes nothing; the agonist corrects this file in place. Every challenge is answered by
exactly one of **FIX** (changed, and what changed), **REBUT** (held, with the line that survives the
challenge), or **DEMOTE** (recorded as a stated limit in §15 or a live choice in §16). **If a claim in this
document was challenged and does not appear below, the loop did not run.**

**ROUND 1 — 24 challenges (`11_challenges_round1.md`), all dispositioned. 18 FIX · 3 REBUT · 3 DEMOTE.**

| # | challenge | disposition | where |
|---|---|---|---|
| **C-1** | the dominance repair does not work — F2 is `descend`, F5 falls to new support, and the recurrence cost falls on the petitioner | **FIX — the repair is DELETED.** Verified `08:147` and `08:150` directly; both halves fail. The invented `LAPSED`/`SUPERSEDED` emission is gone from §6.2, §8.4, §13.1 and §14 row 3 | §8.4 |
| **C-2** | the dominance DEFECT is itself false — `05:206` costs an act, `05:207-208` deposits on omissions, `05:211-216` says an omitted petition IS a drop | **REBUT the audit's finding, on `05:202-224`, which I read directly.** #342 already prices burial and says so in the strongest terms it has. `05:211-216` is **restored** to the document, the three incompatible cost statements are collapsed to one, and the only surviving asymmetry — burial is **safe**, not free — is stated and priced | §8.4, §12.4 |
| **C-3** | "sitting capacity" is one quantity split into three and owned by nobody | **FIX.** New §4.3 names the **two** shipped quantities, owns each in §4.2, and fixes their consumption points. Every price in §§7–8 re-denominated; §17.4's finding narrowed to *establishment* | §4.2, §4.3, §7.3, §8.2 |
| **C-4** | E1 shipped while S19 is unstated, and *"exactly two ways"* is false at a vacant cluster office | **FIX + DEMOTE.** The container→holder substitution is now explicit and argued on `14:325`; *"closes the whole direction of play"* is **withdrawn**; §8.5 gains **case 3, in which the petition never ends**; S19 is recorded as a limit and as a live choice | §8.1, §8.5, §15.16, §16 |
| **C-5** | the exposure rule is not self-enforcing and §5.4 violates it in its own paragraph | **FIX + REBUT + DEMOTE.** *Self-enforcing* is struck; the rule becomes a four-row partition. **Rebutted on the opponent's pool, citing `10:132`'s stated publish-the-mismatch policy.** Stance-composed resistances now publish a band — a change to #342 — and the Masterpiece example moves with it. The unruled residual is §15.15 | §5.2, §5.4, §15.15 |
| **C-6** | the dormancy ruling's ground is a misread of `00_INDEX:28`, and K is ruled the other way | **FIX.** The spine ground is dropped. New §3.4 states **one conflict rule** — the owning document wins on its own object — and applies it to all four collisions, so dormancy and K are now ruled consistently | §3.4, §7.2 |
| **C-7** | §8.7 ships the dormant flag §7.2 just abolished | **FIX.** §8.7 rewritten with no flag: a suppressed grievance is an ordinary stance row at full magnitude whose act-proposition has an unmet enabling claim, recomputed at P0. Identical behaviour | §8.7 |
| **C-8** | §9.3 reclaims a shipped instance and schedules an item | **FIX.** A reporting date is a date the issuing act **sets**, carries no predicate, is not a fifth instance, and places no item | §9.3 |
| **C-9** | `depletion` has a units error and a sign error, and *"no authored per-season constant"* is false | **FIX.** `base(H)` no longer moves; `condition` is a dimensionless multiplier on yield; deltas are **added**, so working a seam depletes it. The no-constant claim is **withdrawn** — nature's term exists and enters through `season_factor` | §10.4, §14 row 12 |
| **C-10** | *"a single act never closes an option"* is false at `share ≈ 1` | **FIX.** Withdrawn and replaced by the bound's real meaning — *you can never move more than your own share* — plus the reason `share = 1` is correct rather than leverage: there is no group. The falsifier now tests scaling with N | §10.3, §14 row 11 |
| **C-11** | the `forestall` precedent does not transfer — it is a purchase and the goods survive | **DEMOTE.** The precedent is withdrawn; the discrete `exclude` limb is **not cleared** against the anti-leverage row and becomes §15.17, with the note that #342 already allows the shape | §10.3, §14 row 11, §15.17 |
| **C-12** | §14 row 4 is cleared by gloss, on the row that exists because the defect passed every other row | **FIX.** Row 4 rewalked on **uniformity**: the option change deposits nothing, but a cohort's claim **about a closure** must store the construal spread and an individuating member draws from it | §14 row 4 |
| **C-13** | the five-row table does not own `stores`, the pointer, or `condition(site)` | **FIX.** The Container row now owns matter and dates explicitly, with the general line stated — *a container may hold matter and dates, never a social aggregate* — and the amendment to `01:490-491` recorded rather than smuggled | §4.2 |
| **C-14** | *"a material verb for the holdingless"* is refuted three paragraphs earlier and is a low-end repair | **FIX — struck.** Replaced with the accurate N-line (the unsolicited give, the wage, the purchase) and an explicit statement that the transfer changes what can reach a postless person, not what he can do | §11.2 |
| **C-15** | absence-vacancy does have a carrier — `14:254-256` ships revocation in fact | **FIX.** The *"no carrier"* claim is withdrawn; the surviving claim is narrower and better — `exercise` is identically zero at a hearth, presence is not, and the household is where hostage politics lives | §7.5 |
| **C-16** | four vocabulary collisions, not two, and two were ruled silently | **FIX.** All four are ruled in §3.4's table with their grounds, and §15.11 records all four | §3.4, §15.11 |
| **C-17** | P1 now carries act-caused writes, breaking the three-class licence | **FIX.** Act-caused condition deltas resolve in **P5**; P1 carries nature only. Removes the class violation and the one-season offset together | §6.2, §6.3, §10.4 |
| **C-18** | §16 escalates conferral after naming the evidence and the direction | **FIX.** Ruled **office-rooted** in a new §4.5, with the argument that B-11 is not violated because a named person still performs `confer` by remit; removed from §16 | §4.5, §16 |
| **C-19** | the Costed band claim is falsified at Pool 1–2 | **FIX.** Scoped to balanced pools 4–12, and the real falsification stated: **Overwhelming is unreachable at Pool 1–2**, which this document does not repair | §5.3 |
| **C-20** | four sections reproduce docs 06, 07, 08 and 10 with zero citations | **FIX.** Citations added at the load-bearing lines (`06:23`, `06:93-96`, `06:128-135`, `07:180-182`, `08:146-157`, `10:30`, `10:33`), and §15.18 records that **doc 06 is uncovered by the verified fact base** | §1.3, §5.1, §9.1–9.2, §12.2 |
| **C-21** | *"nothing cancels automatically"* generalises against LAPSE, which is exactly that | **FIX.** Reworded to the precise claim: *no petition is ended by a fact about the world; it ends by a date passing, or by a person's motion* | §8.5 |
| **C-22** | an unrecorded container→holder substitution, load-bearing on C-4 | **FIX.** Recorded and argued in §15.16 on `14:325`, and cross-referenced from §8.6 | §15.16 |
| **C-23** | §0's own scoping claim is false in §0 | **FIX.** The bullet now names both count sites (§15.9 and §17.3) and says there are no others | §0 |
| **C-24** | two citation slips, including an unrecorded widening of a fault's predicate | **FIX.** F10 is quoted accurately from `08:155` (*judging set*, not standing at a node), and the office-standing rule is presented as a **new rule modelled on F10**, not derived from it | §8.2 |

**What round 1 cost, recorded because it is the most useful thing in this table:** the largest single
change is a **deletion**. A finding that four stages had taken as settled — the convener's dominant option
— was false against the tree, and this document had built a mechanism on it. **Round 1's best work was
reading `05:202-224` and taking the mechanism out again.**
