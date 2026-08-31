
### §2.9 · A9 — A FACTION HAS NO LEADER, AND THE DESIGN OWES A DERIVATION IT NEVER SUPPLIES

**The claim.** *"Leader of a faction"* — the endpoint of both of Jordan's trajectories — is not a
sentence the design can express.

**The evidence.** `founder`, `leadership`, `spokesman`, `head_of` return **0** occurrences across all
2,017 lines. `leader` occurs **twice**, at `:435` and `:440`, and **both are §4.4's argument that a
leader is not a modifier** — *"backwards from what a leader is supposed to mean"*, and *"Choosing which
of your people performs the act is the whole of a **leader's** tactical choice."* Both are about office
pools. Neither is about factions. And §1.3 `:112` closes the door explicitly: *"A **faction** is a
proposition plus a map from persons to a degree of commitment. **That is the entire object.**"*

**The refusal is CORRECT, and this finding is not asking for it to be reversed.** A stored `leader`
field on a faction is §14 row 9's `tier`/`level`/`scale` field under a different name — a declared
property of the collective that gates what the collective can do, which is exactly what §1.3 `:116-119`
spent its best paragraph abolishing. **What the design owes is a derivation, and it has none.**

**Why it matters to play.** Every faction mechanism in the document routes through persons — `presence`,
`density`, `footprint`, the revolt comparison at `:120-121`, the estimated profile at `:124-128`. **Only
leadership does not, because it is not there at all.** So a player cannot occupy the seat both of
Jordan's arcs end in, a rival cannot be told *who speaks for the Restoration*, and the negotiating
counterparty in every treaty above the office ladder is undefined.

> **THE FIX, in the design's own idiom and adding no field: `principals(f, n)` is a QUERY, alongside
> `presence(f, n)`, `density(f, n)`, `footprint(f)` and §4.5's `sovereign_fraction(root)`.**
>
> Rank the faction's committed members with an address inside `n` by **commitment degree × backing
> raisable** — both quantities the design already computes (`commit`'s degree at `:130`, backing at
> §8.1 `:843`) — and take the head of the ranking. Then *"leader of a powerless faction with no real
> holdings"* is **a true sentence about a small result set holding nothing**, computed on demand,
> different in every observer's estimate because §1.3 `:124-128` already says the profile is read from
> one person's ledger and never from true state. **Leadership becomes contestable rather than stored**,
> which is the whole design's posture, and nobody has a leader field to look up.

### §2.10 · A10 — `holdings` IS DEAD STATE: PROPERTY EXISTS, AND NOTHING CAN MOVE IT

**The claim.** No act in the design grants, confiscates, forfeits, sells or seizes property.

**The evidence.** `holdings` occurs **twice**, and both are descriptive rather than operative: `:307`,
in the cadet-branch derivation (*"a cadet branch is a hearth whose succession pointer does not lead to
the main line's holdings"*), and `:352`, quoting `04:29-37`'s two hearth stakes. **No act reads it,
writes it, or moves it.**

- **`transfer` does not.** §11.2 `:1424-1427` moves *"the SAME `stores` scalar, mouth-seasons"* — food,
  and nothing else.
- **A dispensation cannot, by definition.** §9.1 `:1121` defines it as *"a change to what a container
  **permits, costs or requires**"*, and the nine typed terms at `:1123-1125` — `PriceTerm`,
  `ProhibitionTerm`, `LevyTerm`, `ExemptionTerm`, `EntryStandardTerm`, `ExcommunicationTerm`,
  `BlockadeTerm`, `TreatyClause`, `OrdenanzaTerm` — contain **no grant, no confiscation, no
  forfeiture, no enfeoffment**. A dispensation changes terms; it does not move things.
- **No verb exists.** `confiscat`, `enfeoff`, `dispossess`, `seize` return **0**. The four occurrences
  of `grant` (`:928`, `:991`, `:992`, `:1906`) are all about a *petition* being granted at a sitting.

**The only route by which property changes hands is the hearth's succession pointer on death** (§4.1
`:304-307`, fired by a P1 body ageing out) — **which is decider-free, and is item 5 of §1.1's list.**

**Why it matters to play.** Trajectory 1 ends *"with no real holdings"*, and the only way to get there is
to die. More broadly: the design's own strongest historical claim is the cadet-branch derivation at
`:305-310` — *"its members' needs are permanently unsatisfied by inheritance and they must seek standing
through the Church, a guild, the Löwenritter, the Restoration, a marriage, or a knife"* — and **not one
of those six routes can end in the acquisition of a holding.** The mechanism that generates the
peninsula's whole nobility problem has no state it can reach.

**THE FIX is §6 rank 2, and it is a widening rather than an addition.** See `Tenure` below: `confer` and
`revoke` — already in `remit.acts` at `:423` — become enfeoffment and confiscation the moment the thing
conferred may be a site. **No new verb, no tenth dispensation term, and the orphan `holdings` stake is
deleted.**

### §2.11 · A11 — "INVESTIGATOR" IS NOT A SEAT, AND IT IS THE DETECTIVE LINEAGE'S SEAT

**The claim.** The starting position of Jordan's second trajectory does not exist.

**The evidence.** `occupation` and `profession` return **0** occurrences. A person's six fields (`:168-179`)
carry no role that is not an office, and §4.4's office is *"a post whose holder's decision binds persons
who never agreed to it"* — which an investigator's is not. And field investigation, the activity itself,
is **one sentence**, at `:1715-1717`:

> *"**field investigation is the engine's answer to its own epistemics**, not a subsystem: when the same
> fact is disputed and it matters, somebody goes and looks, which is an act, by a person, who can be
> lied to, whose findings are claims like any other."*

**No verb, no cost, no obstacle owner, no resolution path, no phase.** The claim in that sentence is
correct and it is a good claim; it is simply not a mechanism.

**Why it matters to play.** §13.4 `:1712-1717` makes investigation the *only* way the design's central
disputable object is ever settled — *"Settling it requires a named person to go and look, and that
person can be deceived."* Without a verb, the non-delivery-versus-refusal case, which the document calls
*"the design's perfect disputable object"*, is permanently unsettleable by anybody.

**THE FIX, and it needs nothing new — this is the cheapest large win in the document.** Write
`investigate(person, question, subject)` as an ordinary act in §5's terms: the `resistance_pool` is the
concealment of what is hidden, in the same dice-equivalent unit as a lock's fineness (§5.2 `:524`); the
degree bands (§5.3) decide how much comes back and at what cost; the output is **claims deposited in the
investigator's own ledger by `witness`**, with source `firsthand`, exactly as §3.2 `:243` already
requires; and the person he questions may lie, which is already a first-class object at §3.1 `:238`.
**Every part already exists. It is one paragraph of authoring, and it turns the design's best layer into
a playable seat.**

### §2.12 · A12 — THE CONTAINMENT TREE IS STRUCTURALLY IMMUTABLE, AND EVERY BORDER CHANGE IS INEXPRESSIBLE

**The claim.** No node can be added to, removed from, or re-parented within the containment tree, ever,
by anything. The map is fixed at world creation.

**The evidence.** `annex`, `seced`, `conquer`, `vassal`, `absorb`, `border`, `reparent` return **0**
occurrences across all 2,017 lines. (`partition` occurs 4× and `independence` 2×; every one is
`:581`/`:1827`'s *"the exposure partition"* or `:612`/`:1770`'s *"order independence"* — no political
sense anywhere.) §1.2 `:96` declares the ladder — *"Person → Hearth → Community → Settlement → Territory
→ Province → Realm"* — and gives no operation over it. **The only address-changing act in the document
is Admission, and §4.1 `:312-313` scopes it precisely: *"an act by persons who already hold standing,
**changing another person's address** and conferring a mark."*** A person's address, never a node's
parent.

**And this is the correct reading of Jordan's absorption requirement.** *"A Kingdom absorbs a Duchy"* is
not a faction operation — in this ontology a Kingdom and a Duchy are containment **nodes**, at the
`Realm` and `Province`/`Territory` rungs of §1.2's own ladder. Absorption is **re-parenting a node**, and
there is no such operation.

**Why it matters to play.** Annexation, conquest, secession, partition, independence, vassalage, personal
union, the erection of a new duchy out of two counties — **every border change in the genre, in a design
whose named lineage includes grand strategy and 4X.** The strategic layer that `CLAUDE.md` opens by
naming — *"territory control, faction politics, domain actions"* — has no operation on territory.

**It also explains C9 (§4.9).** Territory, Province and Realm own nothing in §4.1 not by oversight but
because **nothing ever happens to them**: they hold no stake anyone can win, and no act can create,
destroy or move them. The three rungs are labels on an unchangeable skeleton.

**⚠ And the neighbouring case is already right, so do not repair it.** *Faction* absorption is shipped
and correct: §1.3 `:131-132`, *"a schism is a subset whose commitment migrates to a rival proposition; a
merger is **members of A committing to B**"* — many person-decisions, no operation on factions. **Do not
propose a merge verb**; §1.3 and §14 row 9 forbid one and are right to. **Only polity absorption fails**,
and it fails on the tree, not on the faction object.

**THE FIX is §6 rank 2.** Under `Tenure`, `confer`/`revoke` on a **Node** is annexation and secession —
performed by a named person exercising a remit, witnessed, contestable, and resolvable through the
shipped compliance contest at §9.2 rather than through a war subsystem.
