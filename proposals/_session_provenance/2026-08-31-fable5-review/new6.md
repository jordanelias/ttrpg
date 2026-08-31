## §6 · THE TEN CHANGES THAT WOULD DO THE MOST, RANKED

Ranked by design bought per unit of change. **Six of the ten are subtractions, and ranks 1–4 are the four
changes that take Jordan's own long-arc trajectories from three of ten transitions to nine of ten**
(§1.2) — which is why they are ranked together, ahead of changes that are individually larger.


### Rank 1 · ADD `mint` AND `efface` TO §6.4's `touches` MODES

**The change.** §6.4 `:689` ships three modes: `mode ∈ {read, alter, exclude}`. Add two:
**`mode ∈ {read, alter, exclude, mint, efface}`.** An act may bring an object into the world or remove
one from it, under the ordinary machinery — witnessed by presence (§1.4), contested where someone objects
(§6.4, as repaired by rank 4), resolved in **P5's existing acts class** (§6.3, no new write class), sized
by §5.3's existing degree bands.

**What it closes with no further mechanism:**

| instance | closes |
|---|---|
| `mint` a **Person** — drawing from #342 `09:539`'s envelope | §2.1, §2.2 · birth, character generation |
| `mint` a **practice rank** — under `02:186-189`'s two conditions | §2.3 · caused advancement, the RPG seat |
| `mint` a **Site** | §2.6 · building, the city-builder seat |
| `mint` a **Container** | §2.6, §4.9 · founding a settlement, the 4X seat |
| `mint` an **Office** | §2.6 · establishment |
| `mint` a **Proposition** | §2.8 · **faction founding**, Jordan's collapsing-royal-factions requirement, and §10.1's flagship emergence sentence becoming true |
| `efface` a **Claim** | the purge limb · the burned register, the silenced teller, the forced recantation |
| `efface` a **Site** | the razing that §10.3's `exclude` limb leaves unbounded at §15.17 |
| `efface` a **Proposition** | a faction dissolving rather than merely emptying |

**Why it is rank 1, and why it is one change rather than eleven.** Every alternative to it is an authored
subsystem — a birth system, a construction system, an advancement system, a founding system, a censorship
system — and each would be a top-level special case, which is the scripting drift `CLAUDE.md` §0 forbids
by name. **Two modes on an existing tuple close eleven gaps, five genre seats and the missing limb of
three of Jordan's five flows**, bottom-up, as a property of the act primitive. It is also the only change
in this list that makes the document's own thesis true: today, in a design whose rule is *every active
decision is made by a character*, **no character can add or remove a single object from the world.**

**One consequence to state rather than discover.** `mint` needs a **cost**, or it is unbounded. The
natural one already exists: an act (§6.1), plus whatever material the thing requires — `stores` for a
building, a person's presence for a birth, `capacity(date)` for an office conferred at a sitting. Rank 2
is what makes that cost coherent.

### Rank 2 · ONE EDGE PRIMITIVE, `Tenure`, REPLACING THREE SPECIAL CASES  *(A10, A12)*

**The change.** The design already has **one edge shape, spelled three times**:

| shipped | at | what it is |
|---|---|---|
| `Holding := (person, office, since, conferrer)` | `:367` | who holds a post |
| `commit(person, faction, Δdegree)` | `:130` | who is committed to a proposition, and how far |
| the hearth's succession pointer | `:302`, `:337` | who transmission runs to |

**§4.2 `:336` already files two of them in the same table cell** — *"`Holding` edges and commitment
edges"* — which is the tree telling you they are one object. Generalise once:

```
Tenure := (subject, object, since, conferrer, degree?)
   object ∈ Office | Site | Node | Faction
```

**Then, with NO new verb — `confer` and `revoke` are already in `remit.acts` at `:423`:**

| object | `confer` | `revoke` | closes |
|---|---|---|---|
| **Office** | appointment | dismissal | **shipped, unchanged** (§4.4, §4.5) |
| **Site** | **enfeoffment** | **confiscation** | **A10** — property can finally move, and by an act |
| **Node** | **annexation** | **secession** | **A12** — *a Kingdom absorbs a Duchy* becomes one call |
| **Faction** | `commit` with its degree | degree to zero is departure | **shipped, unchanged** (§1.3) |

> **IT DELETES THREE SPECIAL CASES AND ADDS NOTHING.** `Holding`, the commitment edge and the
> succession pointer stop being three tuples with three rules and become one tuple with four object
> kinds. §4.2's Person row loses a distinction; §4.1's Hearth row loses the pointer as a separate stake;
> §4.4's `Office` tuple is untouched.

**And it makes annexation what it historically was.** Not a war subsystem and not a border-painting
operation: **a conferral, performed by a named person exercising a remit, public and witnessed like every
act by remit (§4.4 `:442`), whose subject then either complies or does not — through §9.2's shipped
compliance contest** (`contest(container, prize = compliance-here, claimants = {enforcement,
resistance})`, `:1141`). A Duchy annexed on paper and disobedient in fact is the ordinary output of a
mechanism the design already ships, and §9.3's thirty-five-executor logic applies to it unchanged. **No
new resolver, no new object, no war layer.**

**Why rank 2.** It closes two Tier 1 findings and three of Jordan's ten transitions, it is the largest
**subtraction** in this list, and it is a precondition of rank 1 being cheap: `mint` on a Node needs
somewhere for the new node's parent edge to live, and `Tenure` is that place.

### Rank 3 · `principals(f, n)` — LEADERSHIP AS A DERIVED QUERY  *(A9)*

**The change.** Add one query to §1.3, alongside `presence(f, n)`, `density(f, n)`, `footprint(f)` and
§4.5's `sovereign_fraction(root)`:

```
principals(f, n) = members of f with an address inside n, each individually `eligible` to act
                   there (07:180-182), ranked by  commitment degree × backing raisable
```

Both inputs ship: `commit`'s degree at `:130`, and backing — *"the set of persons who have lent their
stance"* — at §8.1 `:843`. **Nothing is stored, so §14 row 9 `:1742` stays clear** and §1.3's whole
derived-scale argument is untouched.

**Why rank 3, and the payoff is larger than the change.** *"Leader of a faction"* becomes a true
sentence — the seat both of Jordan's trajectories end in. And because it is computed from a person's own
claim ledger like every other faction reading (§1.3 `:124-128`), **every observer holds a different
answer about who leads the Restoration**, which is the design's posture applied to the one faction
property it had left out.

> **AND DEPOSITION NEEDS NO VERB AT ALL.** It is the query returning **somebody else** — because members
> `commit` away, or because the backing a rival can raise has overtaken yours. Both are shipped
> operations by named persons for their own reasons. **That is *"power is not static — power is something
> that happens"* falling out of a query rather than out of a mechanism**, which is the strongest form
> the requirement could take.

### Rank 4 · THE MATTER-EVENT GENERATOR — DECLARE `season_factor` A DRAW  *(A7)*

**The change.** §13.2 `:1640` licenses matter events and §10.6 `:1370-1378` gates them with three
conditions, and **nothing generates one.** Close it by declaring the term the design already reads:
**`season_factor(territory)` is a per-territory, per-season DRAW with a published band, resolved in P1,
and a matter event is an extreme draw on it.**

⚠ **Carrying this review's own correction (§0, §2.7): `season_factor` is NOT currently a roll.** `:1404`
calls it *"the shipped territory multiplier that a blockade, a march or a collapsing Order moves"* — acts
move it — and the per-season roll is `(3 + d10)/8.5` at `:1396`, which is per-holding. **So the fix must
declare a draw, not reuse one.**

**Why it costs nothing structurally.** `season_factor` is already territory-scoped, already impermanent
by construction (`13:70-71` assigns permanence to `base(H)` and impermanence to it), already inside P1's
licensed matter class (§6.3 `:675`), and already an operand of `yield` and of nothing else — **so it
cannot violate D-1's act-only `condition` accumulator, because it never touches `condition`.**

**Why rank 4.** It is the only change that repairs Jordan's *"each season the world changes, with or
without the player"* guarantee, and **it gives the world its first non-subtractive non-act channel**,
because a draw has an upper half. Every other licensed channel is decay. It also closes §15.19's stated
narrowing — a site that decays untouched — at the place §10.4 says it must be closed.

### Rank 5 · ONE `Allowance` PRIMITIVE, AND `capacity(date)` DEMOTED TO A SELECTION CAP  *(C14 + B2)*

**The change.** Make `seat_items` an earmarked sub-budget of the person's act allowance (§4.14), and
delete `capacity(date)`'s cost line from `carry` so it is a cap and never a currency (§3.2).

**Why rank 2.** It is the **largest subtraction available**: three capacity-like objects become one
`Allowance(owner, period, size)` and one cap. It **restores §8.4's convener politics**, which is currently
arithmetically impossible and is the best political argument in the document. It **answers D-2 — the
design's self-declared largest open ruling — from architecture rather than escalating it**, which is
`CLAUDE.md` §0's fifth test applied exactly as written. It **prices D-16's cohort exploit out of
existence** rather than forbidding it. And it makes rank 1's `mint` cost sayable, because there is one
budget to charge it against.

### Rank 6 · A NEED IS A CLAIM  *(A5)*

**The change.** Mint needs at P2 as firsthand claims in the person's own ledger, source
`firsthand(body)`; delete the category *need* from §4.2's Nobody row and from §2's prose.

**Why rank 3.** It is the only change that repairs a **structural impossibility** rather than a wrong
value: today there is no legal path from the design's central motivational input to the function that
consumes it, and every act in the game runs through that function. It is also a **subtraction** — one
fewer kind of thing in the design — and it buys hunger as a pleadable ground at a sitting for free. It
ranks below 1 and 2 only because the design has been written *as if* the channel existed, so the fix
changes fewer downstream sentences than the two above.

### Rank 7 · COMMUTATIVITY ON THE FIELD, NOT THE ACT  *(B1)*

**The change.** Declare `condition` additive-alter and succession pointers exclusive-alter on the schema;
§6.4's conflict rule gains the word *non-commutative* and loses nothing else.

**Why rank 4.** §10 — one of the four enlargements, and the one carrying the design's best second-order
behaviour — **does not work at all** as the two sections are written, and the fix is one word on a field
definition rather than a case in the resolver. It ranks here rather than higher because it repairs one
enlargement, where ranks 1–3 repair the substrate. It is also a **precondition of rank 1**: `mint` and
`efface` need the same commutativity question answered (two people founding the same settlement conflict;
two people building different houses do not), and answering it on the field answers it for all five modes
at once.

### Rank 8 · EVICTION ON CLOCK QUANTITIES ONLY, AND P7's WRITE LICENCE STATED  *(B6)*

**The change.** Rank eviction by `confidence_live × recency` only; state P7's write class in §6.3.

**Why rank 5.** It is a **subtraction of a term** that saves the best paragraph in the document from
being false about its own worked example, and it removes a decider-free channel that runs on a social
quantity — which §10.6 condition 1 forbids in general and §13.2's four-item list does not license. It
ranks below the four above because the damage is silent and slow rather than structural: the design still
runs, it just quietly converts motivated retrieval into motivated amnesia over a few seasons. **That
silence is exactly why it must be fixed before anything executes**, because once it does execute nobody
will see it happening.

### Rank 9 · THE THREE ONE-LINE MECHANISM REPAIRS  *(B3, B4, B5)*

**The changes.** Delete §5.2's `if R <= 1: return 0` branch (B3). Add
`precondition: stores(hearth(giver)) ≥ amount` to `transfer` (B4). Give restoration the mirrored form
`Δ = + (1 − condition) × f(degree) × share` (B5).

**Why rank 6.** Three small, independent, high-confidence fixes with no interactions — a **deletion**, a
one-line addition, and one formula that already had a shape waiting for it. Together they restore the
Costed Success band at the low end the design says is right, stop `transfer` minting food, and give the
restoration faction something it can actually achieve. They rank here only because each is local; none
changes how anything else is written.

### Rank 10 · THE TWO TYPING UNIFICATIONS  *(C2, C1)*

**The changes.** `Assertion = (subject, predicate, value, when)`, with `Claim` and `Proposition` as
extensions (C2). Claimants are always a set of persons with a stake (C1).

**Why rank 7.** Both remove a duplicated rule, which is §0 `:21`'s own definition of a defect in this
document, and both are cheap. C2 additionally makes rank 1 cheaper — `mint` on an Assertion covers both a
firsthand claim and a founding proposition, so the primitive gets one instance instead of two. They rank
last because nothing is currently *wrong* because of them; they are the difference between a design that
will stay coherent under extension and one that will grow branches.

**What is deliberately not in the ranking.** §4.3's predicate enumeration (C3) is the largest
implementability gap in the document, and it is not here because it is **not a change, it is unwritten
work** — nobody can rank the cost of writing a vocabulary that does not exist. It should be the first
thing authored after these seven are applied, and §17.1 should stop listing it as settled until it is.

---
