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
  hand-selected set, not a sample of anything. Where a count appears (§17), it is scoped and
  labelled, and it is never used as a base rate.
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
| **8** | **The up-stroke — petition, office, expiry, multi-petition; and the lapse event** *(enlargement 2)* |
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
routes through persons. No act is unlocked or forbidden by a faction's size and no roll takes it as a
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

⚠ #342 carries two incompatible values for K (`03:325-329`'s `7 + Focus`; `09:63`'s constant 12) and
five colliding definitions of `exposure`. **This document uses `K = 7 + Focus` and uses `exposure`
only in the sense of §5.4's pre-roll odds preview.** Both are rulings; §15 records the residue.

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
cluster** (§4.3).

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
| **Container (a rung)** | its stake, its judging set, its standing dates and their convening conditions. **Nothing else** |
| **Office** | its post, node, remit, conferral and revocation rules, establishment, `seat_items`, upkeep — **and its own standing dates and their convening conditions** |
| **Faction** | its proposition and its commitment map |
| **Nobody** | aggregates, norms, densities, needs, openings, scale, reputation |

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

### §4.3 Office, completely

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

**Three costs, all in currencies that already exist:** `seat_items` (an office's standing dates consume
the holder's own hours; holding two offices does not double a day); **publicity** (every act by remit is
public, so an office-holder cannot act quietly — which is why a covert edge and a remit are close to
incompatible); and **upkeep** (the establishment eats; an unpaid establishment does not disperse, it
becomes a faction and treats plunder as wages — see §11.3).

---

## §5 · THE RESOLUTION SURFACE

### §5.1 One roll

Every attempt rolls **N ten-sided dice**. 1–6 scores nothing, 7–9 scores one success, 10 scores two.
Mean = `Pool ÷ 2`, σ ≈ 0.671 per die.

```
Pool(person, practice) = Attribute[relevant](person) + Practice[practice](person)
```

Attributes run 1–7 (the nine named in the setting, plus the ruled-but-unnamed tenth, which composes
identically because this formula never inspects an attribute's name). Practice runs 0–7, where 0 is
*never trained* — **an untrained attempt is always legal, it is just a small pool.** Realistic pool
runs 1–14.

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
for it — and it runs 14–28% across the whole realistic range, so it is not a band the system is tuned
never to reach. Disaster remains reachable at every pool size (Pool 14 vs Obstacle 2 is still 0.08%),
because it falls out of the same binomial as every other row rather than from a hand-authored floor.

An **opposed contest** is the identical `roll` called twice, with the deterministic obstacle replaced by
an actual draw because there is now someone on the other side capable of having a good day. It is not a
second resolver. Past a pool gap of about 6, the underdog's chance falls under ~11% and keeps
collapsing — and **the honest response is to publish the mismatch, not to hide it behind a menu that
pretends to matter.** The one manoeuvre that is never decorative at a large gap is the one that changes
*which obstacle you are rolling against*: the fisher does not win the doctrinal argument, he routes it
— contests jurisdiction, or converts a private grievance into a backed petition (§8).

### §5.4 The pre-roll exposure, and the rule that keeps it safe

Before any die is drawn the resolver publishes the inputs a player would need to compute the odds
himself: both pool sizes, the obstacle interpretation, nothing else. Computing that table **never calls
`roll`** — looking at the odds cannot consume the die.

> **THE EXPOSURE RULE (binding, and §10.5 is the case that forced it):** *a quantity that is hidden
> world state may never be an operand of a roll. Where an obstacle term derives from such a quantity,
> the term is the **band's representative value**, not the scalar.*

This is stronger than *"show the band"* and it is self-enforcing: if the scalar never enters the
arithmetic, there is nothing for a repeated free preview to invert out of it. Without the rule, a player
reads any site's hidden condition at zero cost — no act, no witness, no claim — by previewing an odds
table and subtracting the known terms, **and `choose` has no `World`, so no NPC can run the same probe.**
That is a player-only omniscience channel into hidden world state, and it deletes precisely the theme
the hidden state exists to supply.

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
| **P0** | **CALENDAR** | advance the date · fire due standing dates into a docket · **evaluate convening conditions and schedule the dates they name (§7)** · **emit the lapse and supersession events of dates that have just passed (§8.4)** · recompute option availability |
| **P1** | **SETTLE** | **metabolism only**: larders consume against mouths, production resolves, wounds close or fester, bodies age and die, travellers advance a leg, **and matter carries last season's resolved `alter` effects and nature's term (§10.4)**. *No social quantity moves here* |
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
> | **calendar** | **P0** | dates, dockets, and the events of dates passing | a date is not an outcome; it is an occasion |
> | **matter** | **P1** | larders, bodies, travel, site condition | metabolism and nature — the world is not a caretaker for having weather |
> | **acts** | **P5** | everything else | a person did something |

**§7's convening conditions add nothing to this list.** They are evaluated in P0 and write dates, which
is what P0 already writes. That is the whole of the answer to the objection that scheduling is a second
writing phase: it is not a new phase and not a new class. If a future object cannot be placed in one of
these three classes, it does not go in the engine.

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
with a watch predicate*; `09:641` says *"There is no flag object; dormancy IS an act-proposition with an
unmet enabling claim"*, unified under P0's recompute. **`09:641` wins**, because doc 01 and doc 09 are
the spine (`00_INDEX.md:28`) and because the alternative is a stored flag, which §14 forbids by two rows.
A banked claim is therefore an act-proposition in a person's stance table with an unmet enabling claim —
not a second object, and **not an instance of this section.**

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

- **C1 · PROVENANCE.** Attaching a convening condition is an exercise of **`convene`** (§4.3's remit
  act), performed *in advance*. Only a person holding an office whose remit includes `convene` at that
  holder may attach one, and only at that holder. It is an act by remit, so it is public (§4.3) and it
  is witnessed like any other.
- **C2 · PRICE.** Attaching consumes one item of the sitting's capacity at the sitting where it is set.
  A date it later schedules consumes the convener's `seat_items` in the season it fires. A holder may
  carry no more live conditions than its charter's sitting capacity admits; attaching beyond that
  requires striking one, which is another act at another sitting.
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
is what prices that choice.

### §7.5 The N-line, narrowed

Cut convening conditions and:

1. **A slow material condition with no petitioner never reaches any calendar.** Supersession (§8.5) only
   *kills* matters; multi-petition (§8.3) needs a petitioner who has both a want and a verb; and the
   world's own worsening has no other route to an occasion.
2. **Foresight cannot outlive the foreseer.** A person who sees a famine coming can convene now; without
   this object he cannot arrange that the question be *asked* after he is dead, out of office, or
   uninterested — which is what a charter provision is for.
3. **§8.6's presence-based vacancy has no carrier**, so a living absent holder freezes a seat
   indefinitely and the setting's entire hostage politics has no mechanical consequence.

**What it does NOT buy, and the earlier work said it did:** it does not make obstruction visible on its
own (§8.4 does that), it does not resolve anything, and it does not supply the three arc endings by
itself (§7.4).

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
and it has offices even where it has no container. **This closes the whole direction of play that was
structurally shut**, and it needs no new object: an office already exists, is already conferred,
revocable and vacant-able.

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
  cost:  one ITEM of the sitting's finite capacity
  regard_cost(c) = Σ_{j ∈ judging_set} max(0, −stance(j, prop)) × weight(j)
  regard_gain(c) = Σ_{b ∈ backers WHO LEARN c carried} stance(b, prop) × weight(b)
```

> **THE STANDING RULE, restated for the office form** — #342's version was derived for the withdrawn
> date-respondent and was never re-derived. **Standing at an office is standing at the office's node, or
> leave from a person who holds it.** For an office on a cluster root, which has no node, standing is
> membership in the office's own judging set or establishment, or leave from a member. This mirrors the
> argument system's fault F10 (*speaking without standing, and holding no leave from a member*, §12.2),
> which is the same predicate at the other end of the same process. A venue's `enter` / `speak` columns
> (§12.4) are the door and are unchanged.

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

### §8.4 Lapse and supersession EMIT A WITNESSABLE EVENT — and the dominant option this closes

**The defect, stated first, because the repair is only legible against it.** At the convener's seat,
silent burial dominated public refusal:

| | gain | cost |
|---|---|---|
| **refuse publicly** | the matter dies | an act → witnessed → a grievance deposits |
| **say nothing** | the matter dies, faster | **no act, no event, no claim** |

`05:314-316` is explicit that a lapse is *"not an act by anybody — it is the date passing"* and that
whether the backers learn *"depends entirely on who tells them"*. Identical gain, decaying-to-zero cost.
That is dominance, and it silently gutted every claim that obstruction becomes visible play. Worse, the
claim that *`witness` can see neglect* **contradicts the type signature**: `witness` takes events, and
an omission emits none.

> **THE REPAIR, and it is one object.** At **P0**, when a standing date passes:
> ```
> for each docketed item not reached      ->  emit  LAPSED(item, holder, date, composer)
> for each matter decided moot at the date ->  emit  SUPERSEDED(item, holder, date, mover)
> ```
> Both are ordinary events. Both are **witnessed by presence at the venue**, per person (§1.4), and by
> nobody else. Neither is broadcast.

**Why this does not violate the signature.** An omission still emits nothing. **A date passing is an
event**, and the lapse is a property of the date, not of the omission — which is why P0 can emit it and
why it belongs to the calendar write class (§6.3). And `05:314-316` survives verbatim: the lapse is
still not an act, and the backers — who were not in the room — still learn only if somebody tells them.
What changed is that there is now something a witness actually saw.

**Why the dominance is gone, which the emission alone would not achieve.** The two options no longer
have the same gain:

> **A refusal is TERMINAL. A burial is NOT.** A refused matter is decided and cannot be re-pleaded at
> that venue without new grounds (§12.2, faults F2 and F5). A lapsed matter may be re-filed and
> re-backed. **So refusal costs one deposit and closes the matter; burial costs a deposit each sitting
> and leaves the matter open**, and each recurrence emits another event naming the person who composed
> the agenda that did not reach it.

**Stated limit, in the same breath:** burial remains *cheaper* than refusal, and it remains invisible to
anyone not in the room. That is intended — obstruction should be cheaper than refusal, or nobody would
ever obstruct — but it means *"obstruction becomes play"* is true **only where somebody attends**, and
the design offers no mechanism that puts a witness in a room he did not choose to enter.

### §8.5 A petition expires — and the evaluator is a person

**A petition ends in exactly two ways. There is no third, and no world-state oracle.**

1. **LAPSE.** The date passed and it was not heard (§8.4). The trigger is a date — container-local and
   calendar-readable — and this is the one licensed decider-free resolution in the whole design (§13.2).
2. **SUPERSESSION, moved and decided at a venue.** Any party, or the convener, may **move that the matter
   is moot**. It is an ordinary motion on the stasis ladder (§12), pleaded from claims the mover actually
   holds, contestable like any claim, decided by the venue's decide rule, emitting a record row and a
   `SUPERSEDED` event. It costs an item of the sitting's capacity, so killing a matter is not free.

**This rules the contradiction the earlier work carried.** #342's shape said in one section that a seat
*filled by other means* supersedes a conferral petition, and in another that **nothing cancels another
petition, because that would be an engine deciding a person's options.** Both cannot stand. **The second
wins.** A seat filled by other means is not an expiry; it is a **ground** for a motion that the matter is
moot, which somebody must make, and which the petitioner may contest.

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

**Suppression makes it worse.** A suppressed grievance row is flagged dormant with its **magnitude
preserved, not reduced**, and a recorded re-arm predicate; dormant rows are inherited at reduced
magnitude on succession, and **re-arm at magnitude** the moment a satisfying claim enters any holder's
ledger. The accumulator does not reset because nothing resets it. This is not a settlement gauge: there
is no number on Goldenfurt, only rows in the stance tables of named persons in it, and if those persons
die without heirs the rows die with them.

---

## §9 · THE DOWN-STROKE

### §9.1 The dispensation

`Dispensation(issuer, proposition, scope, terms)` — a change to what a container permits, costs or
requires. There is no bare *effect* field: every term is typed — `PriceTerm`, `ProhibitionTerm`,
`LevyTerm`, `ExemptionTerm`, `EntryStandardTerm`, `ExcommunicationTerm`, `BlockadeTerm`, `TreatyClause`,
`OrdenanzaTerm`. Cut the typed table and every downward effect degenerates into a modifier on a hidden
formula nobody in the world could name, and therefore nobody can reason about, evade, or exploit.

**It travels by being noticed, not by being handed down a chain of posts.** Publishing is a telling
(§3), depositing claims into ledgers by **presence and channel** — the crier, the priest, the guild
notice, the market, a Knot. A person with no post receives it because deposit is never by post.
**Distortion in transit is free:** what reaches the hamlet is often not what the Duke signed.

Then nothing further is needed. The person's own need plus capability plus this new claim yields an
**opening** — computed by the same routine that lists any person's available acts, now evaluated over
changed terms. A blockade raises the price of salt; the fisher's son with a boat and a smuggler cousin
sees a run worth making, and **no one authored an opportunity for him.**

### §9.2 A published dispensation does not apply — it lands as a compliance contest

Per relevant node, `contest(container, prize = compliance-here, claimants = {enforcement, resistance})`
— the same function that resolves sibling rivalry. No second resolver. The roll reads
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

**And a directive may carry a reporting date** — *render account at the tithe reckoning* — which is a
convening condition (§7) in its plainest form, and which surfaces non-compliance at a date where a person
decides what to do about it.

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
Δcondition(site) = − condition(site) × f(degree) × share(actor, site)

f(Disaster) = f(Failure) = 0 ·  f(Costed) = 1/16 ·  f(Clean) = 1/8 ·  f(Overwhelming) = 1/4
share(actor, site) = the actor's own draw from the site ÷ the site's total draw
```

Three things follow, and they are the clearance argument:

- **The effect is a fraction of the container's own capacity, sized to the container** — which is the
  design's named anti-leverage precedent, verbatim (`02:211-213`).
- **No single act at any rung can move more than `1/4 × share`.** One boat among a harbour's forty moves
  at most a fortieth of a quarter of the harbour's condition in a maximum-degree season.
- **So a single act never closes an option.** Closure comes from accumulation — many actors, many
  seasons, crossing a band edge — **which is the tragedy-of-the-commons shape the mechanism exists to
  produce.** Many rational private acts making everyone's practice worse, including the actor's.

**Falsifier, and it is the one to run:** *one person, one season, maximum-degree `alter` — what fraction of
the site's condition moved? If it exceeds the fraction any verb contributes to a container outcome under
`02:211-213`, the object violates the precedent.* Under the formula above it cannot, because `share` is
the same quantity the precedent's "fraction" names.

**Deliberate discrete destruction is a different mode and a different bound.** Burning a granary or
blocking a channel is `exclude`, not `alter`: it is a contested physical act against whoever defends the
site, and it is bounded by **material capacity**, exactly as the shipped `forestall` is — one person may
remove a settlement's entire supply for a season, bounded by `stores(hearth(person))` (`13:141-144`).
**Material leverage bounded by material capacity** is already the design's rule for physical effects, and
this enlargement adopts it unchanged for the discrete case rather than inventing a second one.

### §10.4 Band gating, the P1 integration, and what `depletion` actually is

**Option closure is band-gated:**
```
verbs(site, n) = { v : condition(n) ≥ floor(v) }
```
Bands are published in full with their inputs and **never with the trigger point that separates one band
from the next**, which is the discipline the larder already runs on (`13:31-32`).

**The slow fuses run in P1, and there is no authored per-season constant.** #342's two fuses — ore grade
and siltation — are written to run *"every season"* in **no phase at all**, and `depletion` appears only
as a subtrahend with no definition anywhere (`13:166-169`, `13:178-181`). This document closes both:

```
P1:   base(H) −=  Σ (last season's resolved `alter` effects at H)  +  nature's term
```

`depletion` **is** the sum of the season's resolved `alter` effects plus nature's term. Nothing else. So
**the seam runs out because people worked it**, which is the story the mechanism exists to tell, rather
than because a hidden constant ticks. Siltation is the same line with the sign of the dredging acts:
accrual is nature's term minus the dredging that was actually performed and funded.

⚠ Note the one-season offset and do not read it as a defect: P1 precedes P5, so a season's `alter` effects
land in the following season's settle. That is what *settle* means.

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
the corrupt official — and **a material verb for the holdingless, who previously had none.** It is also
the only enlargement that directly discharges the compliance target's own third structural test — *a
person with no office can act, petition, and receive an opportunity* (`11:237-238`) — because without it,
the only thing that can ever reach you is a dispensation from your own hierarchy.

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
Twelve faults, each with a severity: **F1** self-contradiction · **F2** contradicting the record · **F3**
silence when pressed · **F4** shifting the ground · **F5** repetition · **F6** the quibble · **F7** rootless
ground · **F8** conceding and pressing anyway · **F9** deficient pleading · **F10** speaking without
standing · **F11** incoherent assertion · **F12** inadmissible challenge. Severity is `strike` (the ground
dies, at every venue, for everyone), `descend`, or `close`.

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
- **The convener holds the cheapest real power in the game.** Setting a date and ordering its items is
  `convene`, and a convener who puts three items ahead of yours has spent nothing and killed your
  petition. Influence measured in volume of things filtered, held by a person with no binding power at
  all. §8.4 is what stops that from being free.
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
> any other engine rule. The lapse emits its event (§8.4), and the claimants left unfed carry their
> mouths-deficit straight into their hearths' own need computation.

That is the famine writing itself: the grain exists, the granary is full, the praefect is dead, no one has
been conferred, no sitting is convened, no dispensation is issued — **and people starve inside a system
that is working exactly as written.** Nobody did anything wrong. Nothing is authored.

**What it makes possible:** the **vacancy as a strategy** — keep the seat empty and the matters that
needed it die on their own (obstruction by omission, which is how institutions are actually strangled, and
it needs no new verb, only the guarantee that nothing fills the gap). **Neglect becomes attributable**,
because every effect roots in an act and its absence roots in a named person who did not act — and, since
§8.4, the lapse leaves an event a witness can hold. **The starving petitioner has somewhere to go**: the
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
| 4 | **The calendar — LAPSE ONLY.** A date passing with nothing done resolves a matter against whoever needed the affirmative act | `05:314-316`; §8.4 |

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
| **3** | any function taking `[Person]` and one `Event` | **Clear, and load-bearing.** `LAPSED` and `SUPERSEDED` are witnessed **per person, by presence at the venue**. They are events, not notifications, and there is no signature that would deposit them into the backers. §8.4 |
| **4** | a deposit into a cohort carrying a VALUE rather than a DISTRIBUTION | **Clear.** No enlargement deposits into a cohort. A cohort at a site that loses a verb loses it from its own option set, which is a set operation, not a value deposit. §10.4 |
| **5** | a pushed aggregate, or a field one is stored in | **Clear, and this is where the option-removal object had to be engineered rather than asserted.** Coarser conditions are computed on demand by the draw-weighted mean and **stored nowhere**. §10.2 |
| **6** | a stored aggregate, norm, density, unrest or reputation field | **Clear, and it forced a ruling.** `condition(site)` is *matter*, not an aggregate of persons — the same class as a larder, which the design already stores. And **the dormancy ruling was made against a stored flag**: `09:641` wins, there is no flag object. §7.2 |
| **7** | a knowledge value stored on the thing known | **Clear.** A site's condition is a physical fact, not knowledge of one. Who knows a harbour has silted is claims in ledgers, and the band is published while the scalar is readable by nobody. §10.5 |
| **8** | a second resolver, an auto-resolve formula, a fast path | **Clear.** No enlargement resolves anything. A supersession motion runs through the ordinary argument process; a transfer is an ordinary act; a compliance decision is the shipped `contest`. §8.5, §9.2 |
| **9** | a `tier`, `level` or `scale` field on a faction | **Clear.** Untouched. The faction that forms out of a lost verb is an ordinary proposition plus commitments, with a derived profile. §10.1 |
| **10** | a flat additive modifier from a person onto a roll | **Clear.** The option-removal inversion exists *precisely* to avoid this: damage never enters a roll as a term. Where a site's condition must reach an obstacle, it enters as a band representative, which is a substitution of the pool source, not an addend. §5.4, §10.1 |
| **11** | **a personal effect on a group that is not a fraction of that group** | **This is the row the whole of §10.3 exists for.** `Δ = −condition × f(degree) × share(actor, site)` is a **degree-scaled fraction of the site's own condition, sized by the actor's own share of it** — the design's named precedent verbatim (`02:211-213`). Deliberate discrete destruction is `exclude`, bounded by material capacity, on the shipped `forestall` precedent (`13:141-144`). **Falsifier stated and runnable: §10.3.** |
| **12** | a scheduled recovery tick on standing | **Clear, and it is why §10.4 has no authored constant.** `depletion` is the sum of resolved acts plus nature's term, so nothing recovers or decays on a schedule. And no convening condition may be written over a social quantity that is not a computed norm. §7.3 C4, §10.6 |
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
3. **Obstruction is visible only where somebody attends** (§8.4). Burial remains cheaper than refusal —
   intentionally — and the design has no mechanism that puts a witness in a room he did not enter.
4. **Petition expiry has exactly two forms and neither reads the world** (§8.5). The intuitive third form —
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
11. **Two vocabulary collisions survive inside the design and are ruled rather than fixed** (§3.3): `K` has
    two incompatible definitions and `exposure` has five senses across #342, two of which are the same
    concept implemented incompatibly and one of which is refused by name in the document that neighbours it.
    This document picks one of each and does not retrofit the rest.
12. **The low end was tested and is right. It is not repaired here, and it must not be "fixed" later**
    (§2). But note that §8.5 and §13.1 **do** touch it — a bottom-rung petition can now die unheard — and
    **no section re-examines the postless season under the enlarged rules.** That work is open.
13. **`vacancy-by-absence` has two named falsifiers that have not been run** (§8.6): the deliberate absence,
    and the cost of the hostage repricing at the top of the ladder.
14. **Nothing in this document has executed.** No claim here is licensed by an execution artifact, and under
    `CLAUDE.md` §0.2 none of it is done.

---

## §16 · LIVE CHOICES FOR JORDAN

Each is a genuine fork where two defensible answers lead to materially different games. None is a question
this document can answer from precedent or architecture, which is the test §0 of `CLAUDE.md` sets before
anything is escalated.

| # | the choice | the two games |
|---|---|---|
| **D-2** | **The act economy.** One act per season, or a holder's several? | **A personnel game** — a Duke picks one thing and chooses which of his people does it — **or a decree game**, where the top of the ladder sweeps. It decides whether a player-Duke experiences the top of the ladder as a promotion or a demotion, and it gates §8.3's and §11.3's economics. `14:91-92`'s `seat_items` is already a fourth per-holder capacity and gives a multi-act reading a live foothold |
| **§11.4** | **Is `stores` the realm's denominator?** | **Logistics-real force** — you retain only what you can feed where they stand, and the transport network becomes political — **or coin returns by the back door**, since a fungible transferable scalar functions as money whether or not it is called that |
| **§4.3** | **Is conferral rooted in persons or in offices?** | **Person-rooted**: dead conferrers terminate the graph and the sovereignty query every faction's victory condition reads is undefined across most of it — the Crown cannot be played across a succession. **Office-rooted**: the graph resolves, but an institution performs the game's most consequential act. The design's own evidence points at office-rooted — a military order sworn to *the Crown as institution, not the bloodline* — and the suite asserts both |
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
| the convener must convene or visibly refuse, and a refusal is witnessed | **false as shipped, and repaired.** Non-convening is lapse, which is silent by design. Lapse and supersession now emit witnessable events at the venue, and refusal is terminal while burial is not |
| *`witness` can see neglect* | **a type error, and now a mechanism.** An omission emits no event; a date passing does |
| the watch dissolves the cluster-vacancy deadlock | **retracted.** The deadlock is content, not a bug. A stalled Church is the design working |
| commons damage is a scalar entering an obstacle | **inverted.** It removes an option, with a sizing rule, cross-rung semantics, an aggregation function, and band-quantized exposure |
| the slow fuses run every season | **they run in P1, and `depletion` is defined for the first time** — the sum of the season's resolved acts plus nature's term, so the seam runs out because people worked it |
| the transfer act makes the coercion arithmetic *implementable* | **expressible.** Re-denomination is unwritten work |
| no-fallback is a spine the earlier documents did not carry | **it restates what phase membership already enforced.** Its one genuinely new ruling is vacant-allocator semantics |
| the exception list has two members | **four**, and the calendar's membership is narrowed to lapse alone, because supersession and scheduling were repaired at the mechanism instead |
| there is no act by which one person gives another anything | **overstated.** `requisition` surfaces another person's act as theirs to refuse, and a person with no office has five channels. The real hole is narrower and real: **the unsolicited give, the wage, and the purchase** |
| unintended rescue arrives by market | **half.** The gift path constructs; the market path needs objects that do not exist |
| *13 of 18 arcs close at a sitting; 3 at a counter* | **not citable.** 12 stable + 3 label-disputed + 2½ lost, lane-1 scope, and the axis is decision-versus-trigger, not sitting-versus-counter |

### §17.4 Four findings from the testing that have design content and are NOT dispositioned here

Recorded so they do not vanish a second time, which is how a backlog forms:

1. **The establishment / capacity object.** The design has **no finite, contested, durable capacity object
   at any rung** — it prices remit and forgets establishment. Two independent exercises named the same hole.
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

| round | challenge | disposition |
|---|---|---|
| **1** | *(draft 1 — the pre-relay gating audit's own findings are folded in above and are recorded in §17.3, which is the same operation performed on the earlier work.)* | — |
