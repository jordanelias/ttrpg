### §2.10 · A10 · A12 — THERE IS NO TENURE RELATION IN THE DESIGN: NOTHING CAN HOLD ANYTHING

**The claim.** No person, hearth or faction can hold a site, a node or any material thing, and no act
moves one from a holder to another. **One missing primitive, two victims** — filed separately as A10
(the person's side) and A12 (the faction's side), and merged here because they are the same gap.

⚠ **A12's ORIGINAL FILING WAS WRONG AND IS RECORDED RATHER THAN REPLACED SILENTLY.** It was filed as
*"the containment tree is structurally immutable, so a Kingdom absorbing a Duchy is inexpressible,
because a Kingdom and a Duchy are containment nodes."* **They are not.** `:71` — *"a faction is a
proposition plus a commitment map **at any scale**"*; `:113` — *"Two brothers who have sworn to burn out
the reeve are a faction; **so is the Church of Solmund**"*; `:318` — *"the Church is a faction, a parish
is a community."* A realm-spanning polity is a faction by the design's own test. **Winning a Duchy's
people is §1.3 `:131-132`'s merger — *"a merger is members of A committing to B"* — which is shipped,
runs through `commit`, and which the design gets right.** The reviewer treated Duchy-as-node where the
design means Duchy-as-faction, and the correct finding lives one level down.

### The evidence, both limbs

**Limb 1 — a faction can hold nothing.** §4.2's ownership table, the Faction row at `:339`, in full:

> `| **Faction** | its proposition and its commitment map |`

**Two possessions, and neither is material.** Verified by grep across all 2,017 lines: `holds a
territory` **0** · `territorial` **0** · `faction holds` **0**. The single `faction hold` phrasing is
`:118`, *"does this faction hold a **person** who can act there"* — which is **membership, not holding**.

**Limb 2 — a person's `holdings` is dead state.** `holdings` occurs **twice**, both descriptive rather
than operative: `:307`, in the cadet-branch derivation (*"a cadet branch is a hearth whose succession
pointer does not lead to the main line's holdings"*), and `:352`, quoting `04:29-37`'s two hearth
stakes. **No act reads it, writes it, or moves it.**

- **`transfer` does not.** §11.2 `:1424-1427` moves *"the SAME `stores` scalar, mouth-seasons"* — food,
  and nothing else.
- **A dispensation cannot, by definition.** §9.1 `:1121` defines it as *"a change to what a container
  **permits, costs or requires**"*, and the nine typed terms at `:1123-1125` — `PriceTerm`,
  `ProhibitionTerm`, `LevyTerm`, `ExemptionTerm`, `EntryStandardTerm`, `ExcommunicationTerm`,
  `BlockadeTerm`, `TreatyClause`, `OrdenanzaTerm` — contain **no grant, no confiscation, no forfeiture,
  no enfeoffment**. A dispensation changes terms; it does not move things.
- **No verb exists.** `confiscat`, `enfeoff`, `dispossess`, `seize` return **0**. The four occurrences of
  `grant` (`:928`, `:991`, `:992`, `:1906`) are all about a *petition* being granted at a sitting.

**The only route by which anything changes hands is the hearth's succession pointer on death** (§4.1
`:304-307`, fired by a P1 body ageing out) — **which is decider-free, and is item 5 of this §1.1's
list.**

### Why it matters to play, and Jordan's sentence is the specification

> **Jordan: *"A faction at a territory level may HOLD a territory, but a territory is NOT a territorial
> faction."*** Two claims in one sentence: **(a)** a faction holds a node — a relation between a faction
> and a containment node; **(b)** the two objects stay **distinct** and must not be collapsed into one.
> **The design has neither half.**

- **Annexation has no object to transfer.** The Kingdom-faction can win every one of the Duchy's members
  by `commit`, and **nothing whatever changes about who holds the ground** — because the Duchy never
  held it. Transition 9b-ii, this §1.2.
- **Power has no material referent.** Jordan defines power as the thing factions have; a faction is a
  proposition and a commitment map, so a faction that has won the whole realm's allegiance **owns
  nothing, taxes nothing, garrisons nothing and can lose nothing but members.**
- **Trajectory 1 ends *"with no real holdings"*, and the only way to get there is to die.**
- **The design's strongest historical claim goes nowhere.** §4.1 `:305-310`: a cadet branch's members
  *"must seek standing through the Church, a guild, the Löwenritter, the Restoration, a marriage, or a
  knife."* **Not one of those six routes can end in the acquisition of a holding.** The mechanism that
  generates the peninsula's whole nobility problem has no state it can reach.

**THE FIX is this §6 rank 2, and it is the only proposal on the table that PRESERVES Jordan's
distinction rather than collapsing it.** `Tenure := (subject, object, since, conferrer, degree?)` with
`subject ∈ Person | Faction` and `object ∈ Office | Site | Node`. **`commit` stays a separate relation
and is NOT folded into it** — because membership is not holding, which is exactly Jordan's point: the
faction is a proposition plus commitments, the territory is a node, and **the holding is a third object,
an edge between them.** `confer` and `revoke` are already in `remit.acts` at `:423`, so **no new verb**.
