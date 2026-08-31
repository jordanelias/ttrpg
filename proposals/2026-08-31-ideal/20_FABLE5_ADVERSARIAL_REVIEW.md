# 20 — ADVERSARIAL REVIEW OF THE TERMINAL DELIVERABLE

## Status: PROPOSED (2026-08-31). Adversarial review of PR #343's terminal deliverable. Nothing here
## ratifies on merge, and nothing here has executed — `CLAUDE.md` §0.2 applies: **done means it runs,
## and none of this runs.**

---

## §0 · WHAT THIS IS, WHAT IT REVIEWED, AND THE HONEST STATE OF ITS OWN EVIDENCE

**What it is.** A read-only adversarial pass over `proposals/2026-08-31-ideal/10_SUPERSEDING.md` (2,017
lines), run as the antagonist half of an agonist→antagonist relay — the same relay whose two previous
rounds are logged at that document's §17.5. The antagonist reads the output and writes nothing to it;
this file is the antagonist's deliverable, and every fix below is stated as a change to be made to
`10_SUPERSEDING.md`, not made here.

**What it reviewed.** The terminal document only, against the #342 suite at
`proposals/2026-08-29-valoria-from-scratch/` and against the scope Jordan set mid-session: **the
seasonal loop is the subject.** Mass battle, personal combat and social contest are the three DEFERRED
subsystems and are out of scope. Everything else is in — world state, clocks, pressures, threats,
churn, character generation, event generation, governance at every scale, advancement, demotion,
obligation, offices, occupations, petitions, orders, field investigation, parliament and parliamentary
debate, factions, competing beliefs, epistemics, memory, truth.

**And Jordan stated the loop's intent directly, in five paired flows:** *"things can be built or
destroyed, people can be born or die, ideas can be disseminated or purged, demands can aggregate
upwards, directives can propagate downwards — the world is always in flux."* Plus two constraints on
factions: *"All starting national royal factions may collapse in the game to be replaced with
dynamically generated ones"*, and *"Power is not static — power is something that happens. Factions are
only as strong as the people under their purview."* §1 audits the document limb by limb against those
sentences, because they are the specification and the document is the answer to them.

**CITATION CONVENTION, stated once.** A bare `:NNN` is a line of `10_SUPERSEDING.md`. A bare `§N` is a
section of `10_SUPERSEDING.md`. **Sections of THIS file are always written `this §N`.** A citation of the
form `NN:LLL` is `proposals/2026-08-29-valoria-from-scratch/NN_*.md`, line `LLL`.

> **THE HONEST STATE OF THIS REVIEW'S OWN EVIDENCE. This is a READING. Nothing here executed.** No
> simulation was run, no test was written, no number was measured, no corpus was re-scored. Every
> finding below is an **argument against text** — a quotation, a comparison against another quotation,
> and an inference. Where a finding says a mechanism cannot work, that is a claim about what the
> document says, not a report of what a program did. Under `CLAUDE.md` §0.2 none of it is done, and it
> cannot be: the subject does not run either.

**What survived re-verification.** Thirty-three findings were filed by the reviewing pass. **All
thirty-three were re-read against disk before being carried here** — quote present at the cited line,
contradiction holding on the text, and not already dispositioned in §17.5's round-1 (C-1..C-24) or
round-2 (D-1..D-16) change logs. **One was MISFILED against the wrong object and is RE-FILED and MERGED;
twenty-seven carry unchanged; five were corrected downward.** All six are marked ⚠ where they appear.

> ⚠ **MISFILED AND RE-FILED — A12, on Jordan's correction, recorded here rather than quietly rewritten.**
>
> **What was filed:** *the containment tree is immutable, so "a Kingdom absorbs a Duchy" is
> inexpressible.* **That was filed against a misreading of the design's own ontology.** Jordan: *"But a
> Kingdom and a Duchy are both factions at the highest scale."* The document says so three times —
> `:71`, *"a faction is a proposition plus a commitment map **at any scale**"*; `:113`, *"Two brothers
> who have sworn to burn out the reeve are a faction; **so is the Church of Solmund**"*; `:318`, *"the
> Church is a faction, a parish is a community."* A realm-spanning polity is a faction by the design's
> own test, so **winning a Duchy's people is §1.3 `:130`'s merger — *"a merger is members of A committing
> to B"* — which is shipped, and which the design gets right.** The reviewer treated Duchy-as-node where
> the design means Duchy-as-faction.
>
> **What is true instead, and it is larger than what was filed.** Jordan again: *"A faction at a
> territory level may **hold** a territory, but a territory is **not** a territorial faction."* Two
> claims — a faction holds a node, and the two objects stay distinct. **The design has neither.** §4.2's
> ownership table `:339` gives the Faction row in full: **`| Faction | its proposition and its commitment
> map |`** and nothing else. Verified by grep: `holds a territory` 0 · `territorial` 0 · the single
> `faction hold` at `:118` is *"does this faction hold a **person** who can act there"*, which is
> membership. **A faction can hold nothing.** So A12 is re-filed against the right object and **merged
> with A10**, which is the same gap seen from the person's side: this §2.10.
>
> This review holds itself to §17.5's standard: a misfiled claim is recorded with what it got wrong,
> not silently replaced by the claim that survived it.

- ⚠ **C1's count is wrong and is corrected.** `contest(` has **three** literal call sites (`:327`,
  `:691`, `:1141`), not four. The fourth (`:1293`) is prose — *"a contested physical act against
  whoever defends the site"* — not a call. Three claimant types across three call sites, with a fourth
  implied in prose. The finding holds; the number does not.
- ⚠ **C3 is narrowed.** *"No form is listed anywhere"* is very slightly overstated: `SAID(Aldwin, C,
  season 12)` at `:238` is one predicate form, given as an **illustration that claims may be subjects
  of claims**, not as a member of a declared roster. The closed set still has no enumeration; it has
  one worked example.
- ⚠ **A7's proposed fix is re-worded because the reviewer's version misreads the document.**
  `season_factor(territory)` is **not** a roll in `10_SUPERSEDING.md`. `:1404` calls it *"the shipped
  territory multiplier that a blockade, a march or a collapsing Order moves"* — i.e. acts move it — and
  the per-season roll is `(3 + d10)/8.5`. The fix therefore has to *declare* `season_factor` a draw, not
  merely reuse one. Corrected at §2.7.
- ⚠ **C15 was filed INVERTED and is turned around.** It was filed as *the terminal document added
  `visibility` to the claim tuple without recording it as a ruling*, on the ground that
  `01_substrate.md:228` ships six fields. **`03_knowledge_telling_investigation.md:21` ships the
  seven-field tuple with `visibility`, and §3.4's own conflict rule selects doc 03 — whose declared
  subject is knowledge — over doc 01.** So the terminal document is following its own rule correctly.
  What survives is narrower and still real: **a fifth vocabulary collision that §3.4's table does not
  record.** Restated at this §4.15.
- ⚠ **C9 is narrowed, also on Jordan's correction.** Filed as *§4.1 specifies ownership for four of seven
  rungs*, read as a governance gap. It is substantially **answered**: political action above Settlement
  runs through **factions and offices**, not through container state, so the upper rungs owning nothing
  is the architecture working. What survives is a **statement gap, not a mechanism gap** — see
  this §4.9.

**Two findings are reclassified rather than demoted, and are labelled where they appear.** **C13** and
**C14** are not contradictions; they are **restructuring proposals**. They are kept because both are
subtractions and C14 answers the design's largest open ruling from architecture, but neither asserts
that the document says something false.

**Nothing was dropped.**

---

## §1 · THE VERDICT IN ONE PAGE

### §1.1 The central finding

Audited limb by limb against Jordan's five paired flows:

| flow | limb A | limb B |
|---|---|---|
| **built / destroyed** | ⚠ **ABSENT.** No act creates a site, container, office or settlement anywhere in 2,017 lines (this §2.6) | **present.** §10.3's `alter` (`:1261`), `exclude` (`:1292`), doc 12's `burn` inherited at `:1305` |
| **born / die** | ⚠ **ABSENT.** `birth`/`natality` = 0 occurrences. #342's demographic envelope and its five mint triggers (`09:533-537`) were dropped (this §2.1) | **present.** P1 `:648`, *"bodies age and die"* |
| **disseminated / purged** | **present, and it is the best material in the suite.** §3 tellings, §9.1 publication by presence and channel, distortion in transit free | ⚠ **ABSENT.** Verified by grep: `purge` 0, `censor` 0, `recant` 0, `erase` 0. `suppress` (5×) is only §8.7's *suppressed grievance* — a person's own act-proposition with an unmet enabling claim, not an act on anyone else's ledger. `strike` (`:1537-1540`) kills a **ground at a venue**, a debate outcome. `burn` (`:1305`) is a reference to #342 doc 12's severity table, never an act here. **No act removes a claim from another person's ledger, destroys a record, silences a teller, or forces a recantation** |
| **demands aggregate upward** | **present and excellent.** §8 petition, backing, carriage, agenda, drop, expiry | — |
| **directives propagate downward** | **present and excellent.** §9.3, one order and thirty-five executors | — |

The dissemination row is the one to read carefully, because the design does ship *lying* (`SAID` claims,
`:238`), *distortion in transit* (`:1123`, *"what reaches the hamlet is often not what the Duke
signed"*), and *not telling*. Those are all ways of **preventing** a claim from spreading. **None of
them removes a claim that has already landed.** An idea, once deposited in a ledger, can only fade —
never be taken out by anybody.

> **THE DESIGN HAS A RICH VOCABULARY FOR CHANGING THE STATE OF THINGS THAT EXIST, AND ALMOST NONE FOR
> CHANGING WHICH THINGS EXIST OR WHO HOLDS THEM.** Stance, `condition`, standing, commitment,
> compliance, confidence, degree — all richly movable by named persons. **Persons, sites, offices,
> containers, propositions, claims and holdings — not one of them can be brought into, removed from, or
> moved between holders by any act in the document.**

**The proof is a five-item list, and it is short enough to check.** The only operations in all 2,017
lines that change what exists or who holds it are:

1. **death** — P1 `:648`, metabolism, **decider-free**
2. **de-individuation** — P7 `:654` and §2 `:212`, **decider-free**
3. **eviction of a claim** — P7 `:654`, **decider-free** (and see this §3.6: it is also an unlicensed channel)
4. **individuation** — P7 `:654`, the single additive operation, firing when *"an event names one of its
   members"* (`:209`) — **decider-free at the point of firing**, and whose four other #342 triggers and
   whole minting procedure (`09:535-548`) were dropped
5. **holdings moving on death** — the hearth's succession pointer, §4.1 `:304-307`, fired by a P1 death.
   **The only route by which property changes hands anywhere in the document** (this §2.10), and it too is
   decider-free

> **ALL FIVE ARE DECIDER-FREE. FOUR OF THE FIVE ARE SUBTRACTIVE.** In a design whose thesis is that
> every active decision is made by a character, and whose §13.1 rule is *"if no person acts, the thing
> does not occur"*, **no character can add or remove a single object from the world, or move a single
> thing from one holder to another.** Existence and tenure are the two registers the persons do not
> touch — and they are the registers that empty on their own.

**And TENURE is worse than existence, because the design does not have the relation at all.** §4.2's
ownership table `:339` gives a faction exactly two possessions — **`| Faction | its proposition and its
commitment map |`** — so **a faction owns nothing: no stake, no site, no node, no seat.** *Power*, which
Jordan defines as the thing factions have, therefore has **no material referent anywhere in the
design.** The same hole on the person's side is `holdings` sitting in §4.1 as dead state that no act
reads, writes or moves. **One missing primitive, two victims** (this §2.10).

**One of the missing objects is far worse than the rest, and it is the single sharpest result in this
review. A PROPOSITION CANNOT BE CREATED BY ANY ROUTE AT ALL** (this §2.8).

§1.3 `:112`: *"A **faction** is a proposition plus a map from persons to a degree of commitment. **That
is the entire object.**"* Founding a faction therefore means minting a proposition, and no operation
anywhere mints one. Persons, claims, sites and cohorts at least change population by a decider-free
channel; **a proposition has no channel of any kind.**

> **AND A FACTION IS THE DESIGN'S POLITY OBJECT AT EVERY SCALE.** `:71`: *"a faction is a proposition
> plus a commitment map **at any scale**."* `:113`: *"Two brothers who have sworn to burn out the reeve
> are a faction; **so is the Church of Solmund**."* `:318`: *"the Church is a faction, a parish is a
> community."*
>
> **So this is not a defect about two brothers founding a conspiracy. NO NEW REALM, DUCHY, CHURCH,
> KNIGHTLY ORDER OR POLITY OF ANY SCALE CAN EVER COME INTO EXISTENCE. The entire political map is frozen
> at world creation, and the only permitted motion is commitment draining out of the propositions the
> world shipped with.** Under §1.3 `:130`'s own rule — *"Degree to zero is departure"* — a faction whose
> commitment reaches zero is gone, and nothing can bring it or any successor back. **The political map is
> therefore not merely static. It is monotonically shrinking.**

**That falsifies a Jordan requirement in its own words.** *"All starting national royal factions may
collapse in the game to be replaced with **dynamically generated ones**."* Collapse is expressible —
`commit` to zero for every member. **Replacement is not**, because a dynamically generated Kingdom **is**
a minted Proposition, and there is no operation that mints one. **The design can lose every realm it
shipped with and grow none.**

**Two further objects are missing and are smaller than that, but real.**

- **A faction has no leader, and the design owes a derivation it never supplies** (this §2.9).
- **`holdings` is dead state** (this §2.10). It occurs twice, both descriptively; no act reads it, writes
  it or moves it, and none of the nine typed Dispensation terms grants, confiscates or forfeits anything.

**And one filed finding in this family was MISFILED and is re-filed.** A12 claimed the containment
tree's immutability made annexation inexpressible; it does not, because a Kingdom is a faction and
winning its people is `commit` at scale. **What is true instead is bigger: no faction can hold a node,
so annexation has no object to transfer** — the Kingdom can win the Duchy's members and still nothing
changes who holds the ground. Merged into A10 at this §2.10. The residue of the original claim — **the
tree cannot gain or lose a node, so no settlement can be founded or razed** — is folded into A6 (this
§2.6), and **re-parenting is moot**: the tree is geography, allegiance lives in factions, and geography
being static about places that already exist is defensible design rather than a defect.

**And that is why the flagship emergence claim in the whole exercise is false as the document stands.**
§10.1 `:1228-1230`, the most-quoted sentence in the suite:

> *"and 'the seam must be restored' is a proposition, and the people whose practice used it are already
> committed to it, so **a political faction forms out of a physical fact with no authoring at all**"*

Nothing makes that proposition exist. Nothing makes anyone committed to it before it does. **The
design's most celebrated emergent behaviour — the one §10 is built to produce and §14 row 9 is cleared
on — rests entirely on the one primitive the document does not have.**

**So A1, A2, A3, A6, A7, A8, A9, A10·A12 and A11 are not nine findings. They are one finding with nine
faces**, and they should be read and fixed as one. This §6's first four ranks are the changes that close
them.

### §1.2 The trajectory test — the central finding measured on Jordan's own arcs

Jordan gave two long-arc player trajectories. **(1)** Start as Duke or King; end as the leader of a
powerless faction with no real holdings. **(2)** Start as an Investigator; end as the leader of a shadow
faction controlling the realm through a puppet ruler. He then added two more by hand — *"lose a faction
(be deposed), acquire a faction."* Decomposed, they need **twelve** transitions.

⚠ **This table's own count was wrong in an earlier version of this file, which said *"three work today"*
while listing four in the WORKS column. Recomputed rather than adjusted: FIVE OF TWELVE WORK TODAY.**

| # | transition | state |
|---|---|---|
| **1** | **lose an office** | **WORKS.** §4.4 `:416`'s `revocation`, and `confer/revoke` is in `remit.acts` at `:423` |
| **2** | **gain an office** | **WORKS.** Conferral, §4.4 and §4.5 |
| **3** | **rule another person's acts through what he believes** | **WORKS, AND IT IS THE DESIGN AT ITS VERY BEST.** See this §1.3 |
| **4** | **found a faction** | ⚠ **FAILS.** No operation mints a Proposition (this §2.8) |
| **5** | **lead a faction** | ⚠ **FAILS.** A faction has no leader and no derivation of one (this §2.9) |
| **5b** | **lose a faction (be deposed)** | ⚠ **FAILS today: no referent.** You cannot be deposed from a position that does not exist (this §2.9); there is no leader field to clear and no verb that clears one. ✅ **Under rank 3's `principals(f, n)` it needs NO VERB AT ALL.** Deposition is not an operation — it is **the query returning someone else**, when members `commit` away from you (§1.3 `:130`, *"Degree to zero is departure"*, shipped) or your backing collapses (§8.2's `regard_cost`/`regard_gain`, shipped). **Nothing is deposed; the ranking changes** |
| **6** | **lose your holdings** | ⚠ **FAILS.** `holdings` is dead state; the only route is dying (this §2.10) |
| **7** | **change occupation** — Duke to faction chief, Investigator to spymaster | ⚠ **FAILS.** `occupation` and `profession` = 0. A person's economic identity is `Practice` and nothing else |
| **8** | **be an Investigator at all** | ⚠ **FAILS.** Field investigation is one sentence with no verb, cost, obstacle owner or resolution path (this §2.11) |
| **9a** | **a faction absorbs another faction** | **WORKS, AND THE DESIGN IS RIGHT TO DO IT THIS WAY.** §1.3 `:131-132`: *"a merger is members of A committing to B"* — many person-decisions, no operation on factions. **Do not propose a merge verb**; §1.3 and §14 row 9 forbid one and are correct |
| **9b-i** | **a polity absorbs another polity — WINNING ITS PEOPLE** | ✅ **WORKS.** ⚠ *Filed as failing; that was a misreading — see this §2.10.* A Kingdom and a Duchy are **factions** (`:71`, `:113`, `:318`), so this is 9a's merger at scale, through the shipped `commit`. **The design gets the hard half of annexation right** |
| **9b-ii** | **a polity absorbs another polity — COMING TO HOLD ITS GROUND** | ⚠ **FAILS.** §4.2 `:339` gives a faction *"its proposition and its commitment map"* and nothing else, so **a Duchy cannot hold its Territory and annexation has no object to transfer** (this §2.10). **Annexation is half-shipped, and the half it ships is the half the design got right** |
| **10** | **the world changes around you while you climb** | ⚠ **FAILS in part.** Three of four licensed channels are decay; the fourth is inert (this §2.7) |

**Note what separates the two columns. Every transition that works is a state change on an object that
already exists — including 9a and 9b-i, which are commitment moving between propositions that already
exist. Every transition that fails is a change to WHAT exists, or to WHO HOLDS IT.** That is
this §1.1's finding arriving on Jordan's own arcs rather than on a grep, which is the strongest corroboration
available to a review that measured nothing.

> **After four fixes — `mint`/`efface` (this §6 rank 1), `Tenure` (rank 2), `principals` (rank 3) and
> the matter-event generator (rank 4) — TEN OF TWELVE TRANSITIONS WORK**: rank 1 closes 4, `Tenure`
> closes 6 and 9b-ii, `principals` closes 5 and 5b, and the generator closes 10. **None of the four adds
> an object to the engine.** Add the one paragraph of authoring named in this §6's closing note — the
> investigative verb — and it is **eleven of twelve**. Transition 7, occupation, is the honest residue:
> it is genuinely unwritten, and it is small.

> **And two of the eleven transitions were added by Jordan AFTER the first pass, and neither required a
> new fix.** Both are closed by `mint`/`efface` and `principals`, which were already on the table — and
> one of them, **deposition, closes with no mechanism whatsoever**, falling out of two operations the
> design already ships. **A fix set that absorbs new requirements without growing is the signature of a
> correct primitive; one that needs a new rule per requirement is a feature list.** This one absorbed
> two and grew by nothing.

### §1.3 Where the design is a direct hit, and it must be said first

**Transition 3 — the control mechanism of Jordan's second trajectory — is already built, needs nothing
added, and is the best argument in the suite for the architecture being right.**

Because `choose` takes no `World` (§1.4 `:143`), **the only way to move another person's act is to
change what he believes.** Feed the puppet claims and his own `choose` produces your acts — out of his
own ledger, for his own reasons, with no puppet flag, no control field, and no branch. §4.2 `:368` states
it flatly: *"**Nothing anywhere stores control.**"* And §13.4 `:1706-1710` makes the shadow ruler's
position exactly what it should be — *"Nobody is lying. There is no fact of the matter about credit"* —
so being the power behind the throne is **a fact some hold and others deny**, contestable at a sitting
like everything else. **The hard half of trajectory 2 is done. Only its endpoints are missing.** That is
the review's actual thesis in one line: **the architecture is right and the vocabulary is incomplete.**

**Jordan: *"Power is not static — power is something that happens. Factions are only as strong as the
people under their purview."* The document answers that sentence exactly, at `:116-119`:**

> *"**Scale is derived and gates nothing.** … Capacity to act at a node is not a property of size; it is
> the question *does this faction hold a person who can act there* — which routes through persons … No
> act is unlocked or forbidden by a faction's size and no roll takes it as a term."*

and §14 row 9 `:1742` forbids the `tier`/`level`/`scale` field that would break it. **That is the
requirement met in the substrate rather than in a feature.** Faction merger (transition 9a) is right for
the same reason and by the same mechanism.

**Five more things are excellent and are not under attack anywhere below.**

- **The epistemics layer (§3, §13.4).** Claims in ledgers, per-person `witness`, corroboration failing
  closed, the salience multiplication at `:254-255`, and `stanceweight` floored at 0.05 so that *"he is
  not hiding it and he is not lying; he is not thinking of it"* (`:260-261`). §13.4's non-delivery-versus-
  refusal case is the best-argued object in the suite. This layer is world-class and the review's only
  finding against it (this §3.6) is a defence of it.
- **The sitting and the stasis ladder (§12).** Four rungs, irrevocable public descent, twelve named
  faults with severities at `:1535-1540`, and force-close as the *normal* ending. **This is the
  best-specified object in the document and it is the standard the rest should be held to.** It is the
  one place where a mechanism is stated with enough precision that an implementer would not have to
  invent anything.
- **The down-stroke's one-order-many-executors (§9.3).** Scope enumerates **executors, not places**;
  delivery is not assumed; reports are claims. Thirty-five outcomes from one order, and the four seats
  it makes playable — the slow-walker, the over-enforcer, the false reporter, the man ruined for
  complying exactly — arrive with **no new verb**.
- **No fallback and vacant-allocator semantics (§13.1).** *"A standing date whose allocating office is
  vacant fires, allocates nothing, and lapses. The stock sits."* The famine writes itself, nobody did
  anything wrong, nothing is authored. That is one ruling and it earns its place.
- **The option-removal inversion (§10.1).** Damage removes an option and never adds difficulty. It
  converts a scalar-in-an-obstacle into an option-set change, satisfies the anti-leverage row on its own
  terms, and produces a political faction out of a physical fact — the right shape, even though §1.1
  shows the last step is currently unreachable.

**And the relay discipline itself (§17.5) is exemplary and should be kept as a repository precedent.**
Two rounds, forty challenges, every one dispositioned FIX / REBUT / DEMOTE with a location; a
self-imposed rule that *"if a claim in this document was challenged and does not appear below, the loop
did not run"*; round 1's largest single change being a **deletion** of a mechanism built on a premise
that turned out false on disk; and round 2's own verdict on itself — **"NINE OF SIXTEEN WERE REGRESSIONS
IN ROUND 1'S OWN TEXT … the newest prose is the most defective prose, and the cheapest repairs were all
subtractions."** That sentence is worth more than most of the design work around it, and this review
found it holding: the findings below cluster on §4.3, §8.4, §10.4 and §14 row 4 — the newest prose.

### §1.4 Tier counts

| tier | filed | carried | corrected downward |
|---|---|---|---|
| **1 — fatal** | 12 | 12 | 1 (A7's fix re-worded) |
| **2 — mechanism contradictions** | 6 | 6 | 0 |
| **3 — uniformity, typing, primitives** | 15 | 15 | 3 (C1's count, C3's scope, C15 inverted) · 2 reclassified as proposals (C13, C14) |
| **4 — coverage** | table | table | 0 |
| **total** | **33** | **33** | **4** |


## §2 · TIER 1 — FATAL

Read §2.1, §2.2, §2.3, §2.6, §2.7 and §2.8 as **one finding**. They are listed separately because their
evidence is separate; they have one fix, at this §6 rank 1.

### §2.1 · A1 — THE POPULATION HAS NO INFLOW

**The claim.** The seasonal churn loop has a monotonically non-increasing population.

**The evidence.** #342 `09:533-537` ships the whole mechanism:

> *"The world holds a **demographic envelope** per containment node — counts by age band, marks bundle,
> capability distribution, carried as cohort weight. **Births and deaths move weights.** A **record** is
> minted only when: an event names them · a telling puts them in someone's ledger · they occupy a role
> or office · they enter a Knot · they are individuated as decisive in a contest."*

`10_SUPERSEDING.md` carries the **de-individuation half** — `:212`, *"A person re-merges into a cohort
when they hold no Knot, no office, no live petition, and no other person's ledger names them"*, and P7
at `:654` — and **one** of the five mint triggers, at `:209`: *"A cohort **individuates** when an event
names one of its members."* `grep -ci "birth\|natality"` over the whole file returns **0**. P1 `:648`
carries *"bodies age and die"* and nothing that adds.

**Why it matters to play.** Individuation is not inflow. It moves weight that already exists from a
cohort record into a named record; it does not add a mouth, an heir, a claimant, or a body to the
envelope. Every mechanism the design is proudest of consumes population: cadet branches need younger
sons, succession needs heirs, hostage politics needs a household with people in it, the establishment
eats and must be replaced. **A design whose seasonal tick is the unit of play, and whose population only
falls, has a terminal state and no counter-pressure toward it.**

**This alone falsifies `:15`** — *"A reader who has never seen #342 can read this file alone and have
the whole design"* — because the mechanism that would supply the inflow is in #342 and is not here.

**THE FIX.** Restore #342 `09:533-548` in full: the demographic envelope per containment node, births and
deaths moving cohort weights in P1, and **all five** mint triggers rather than one. Under this §6 rank 1's
primitive, minting a person is `mint` on a Person and draws address, marks, capability and stance from
the cohort plus its dispersion exactly as `09:539` specifies — so this restoration is an *instance* of
the general operation, not a subsystem.

### §2.2 · A2 — CHARACTER GENERATION IS GONE

**The claim.** The design can describe a person and cannot make one.

**The evidence.** #342's object roll-up gives every field a producer. `02:739`: **`Mark | admission,
birth, succession, ordination, grant`**. `02:742`: **`Practice | generation, caused advancement`**.
`10_SUPERSEDING.md` §2 (`:168-179`) specifies **a producer for none of the person's six fields** — the
table's columns are *field* and *why it cannot be cut*. #342 also ships the hard half at `09:539`:
*"Minting draws address from the cohort, marks from the cohort plus its variation, capability from its
distribution conditioned on the naming event, stance from its aggregate plus dispersion."*

**Why it matters to play.** The generation rule is where caste, heritage, guild grade and Thread
sensitivity are *distributed* — and §2 `:172` makes marks *"what make the same act by two persons produce
different results."* Without a producer, the initial distribution of every mark in the world is an
authoring decision made once, off-camera, and never made again. The peninsula's demography stops being
a mechanism and becomes a fixture.

**THE FIX.** Add the producer column to §2's six-field table, sourced from `02:739-750`, and restore
`09:539`'s minting procedure as the body of `mint` on a Person.

### §2.3 · A3 — CAUSED ADVANCEMENT IS GONE, AND WITH IT EVERY CHARACTER'S ABILITY TO IMPROVE

**The claim.** No character in the design can get better at anything.

**The evidence.** #342 `02:186-189`, verbatim:

> *"**Advancement is caused, never ticked.** A practice gains a rank when an attempt at a standard above
> its rank resolves *and* one of: it was witnessed by a person holding the practice higher (a master saw
> it), or it failed at a cost the person actually paid. **There is no experience clock.** This is the
> precedent's refusal of the scheduled recovery tick applied at person scale."*

`10_SUPERSEDING.md` **keeps** §14 row 12 — the scheduled-recovery refusal, at `:1745` — and **drops its
person-scale application**. `grep -ci advancement` returns **0**. §5.1 `:501-505` reads practice rank as
a pool term and hangs the rank-3 and rank-5 verb ladders on it; nothing writes it.

**Why it matters to play.** Advancement and demotion are on Jordan's in-scope list. The rank ladder is
also the design's own model of leadership — `:504`, *"which is the same option-set discipline §4.4
applies to office and §10.1 to a site, at person scale."* With no producer, the ladder is a static
character sheet: the Free Master is a Free Master because he was authored one. **The RPG seat is not
thin; it is absent**, and it is absent by omission rather than by ruling — §17.1 `:1880` lists what
survived unchanged and simply does not mention it.

**THE FIX.** Restore `02:186-189` verbatim into §5, as the producer of the practice-rank field, and
record it in §17.1 as surviving rather than allowing it to vanish silently. Under this §6 rank 1, advancement
is `mint` on a practice rank and stops being a special case.

### §2.4 · A4 — §14 ROW 4's RULE REINVENTS A SHIPPED MECHANISM AND PUTS IT ON AN OBJECT THAT CANNOT HOLD IT

**The claim.** The document's own newest rule relocates a shipped, correct mechanism onto a carrier that
is defined so as to be incapable of carrying it.

**The evidence.** §14 row 4 (`:1737`), the C-12 fix:

> *"when a closure is witnessed by a cohort, **the cohort's claim stores the construal spread its members
> would have produced, and an individuating member DRAWS from it and never inherits it.**"*

#342 `09:541-548` already ships exactly this, and stores it in a **different and better place — at the
channel, not the cohort**:

> *"tellings are stored *at the channel*, not per person, until individuation, so a person minted in
> season 40 is handed the claims their address's channels would have deposited. … **Handed, not copied:**
> each stored channel claim carries the construal distribution … and the minted person **draws from it
> rather than receiving the cohort's reading** — two brothers minted out of the same hamlet in the same
> season can hold opposite construals of the same twenty-year-old proclamation."*

**A cohort cannot hold a spread by construction.** §2 `:206`: *"Persons sharing an address, marks and
**stance** are held as a cohort"* — sharing stance is the membership criterion. §2 `:208` makes the
cohort individuate precisely when *"its internal stance spread exceeds the point where one answer is
honest."* A cohort is the object that exists only while the spread is negligible; asking it to store the
spread asks it to store the reason it should already have split.

**Why it matters to play.** The channel placement is what makes a person minted in season 40 have a
plausible **past** — the channel has a real history, the cohort has only a present. Move the store to the
cohort and every minted person's memory begins at the moment of minting.

**And note the self-inflicted shape of it.** The document applied its own *"zero shipped instances"*
discipline rigorously to convening conditions (§7.2, `:731-741`) and **never re-ran it on its own row-4
rule** — which is round 2's finding, *the newest prose is the most defective prose*, recurring one round
later.

**THE FIX.** Replace row 4's rule with #342's: **construal distributions are stored at the CHANNEL, not
at the cohort**, and an individuating person draws from the channel's stored claims. Cite `09:541-548`.
Row 4 gets shorter and the cohort loses a field it could not hold.

### §2.5 · A5 — `choose` HAS NO CHANNEL FOR NEEDS, AND NEEDS ARE THE MOTIVE FOR EVERY ACT

**The claim.** The design's central enforcement mechanism has no channel for its central motivational
input.

**The evidence.** Four facts, each on disk, that cannot all hold:

- §2 `:183-190`: subsistence and standing read **the world** (*"You feel hunger whether or not anyone
  told you"*); commitment and exposure read **the view**.
- P2 `:649`: needs are *"Pure, parallel, **never stored**"*.
- P4 `:651`: `choose(person, view) -> act` — and §1.4 `:143`, *"**`choose` has no `World`.** Not a masked
  world, not a read-only world, not a world behind an accessor."*
- §4.2 `:340`: the **Nobody** row holds *"aggregates, norms, densities, **needs**, openings, scale,
  reputation."*

There is no path from P2's output to P4's input. Storing needs on the person is forbidden twice (P2's
*never stored*, §4.2's Nobody row). Putting world-derived scalars into the View is forbidden by §1.4
`:155` — *"**`View` is assembled, not filtered**: absence of a claim produces absence in the view"* — and
by §14 row 2. **The document even shows the strain: P4 `:651` says `choose` runs *"against the frozen P1
snapshot and their own ledger"*, which is a world argument in prose that the signature forbids.**

**Why it matters to play.** Subsistence need *"outweighs stance entirely once it exceeds 1.0"* (`:1408`)
and is the trigger for all five of the postless person's channels. It is the single most consequential
number in a person's turn, and there is no legal way for it to reach the function that uses it.

> **THE FIX, and it REMOVES A CATEGORY rather than adding a channel: a need is a sensation, and a
> sensation is a claim.**
>
> Mint needs at P2 as **firsthand claims in the person's own ledger**, source `firsthand(body)` — §3.2
> `:243` already supplies the source vocabulary and forbids a null source. View assembly then picks them
> up at P3 by the ordinary salience rule; `choose` keeps its signature unchanged and gains nothing;
> *"supposed to be stale relative to the world"* (`:191`) becomes automatic rather than asserted; and
> **the category "need" is deleted from the design** — it becomes a claim like everything else, and the
> Nobody row loses an entry.
>
> It also buys something the design wants and currently cannot do: **hunger becomes arguable at a
> sitting** (§12), because a claim is what a `Ground`'s `support[]` is made of (`:1515`).

### §2.6 · A6 — NOTHING IN THE DESIGN CREATES A STRUCTURE; THE WORLD CAN ONLY LOSE THEM

**The claim.** No act founds a settlement, builds a site, creates a container, or establishes an office.

**The evidence, by exhaustive grep of all 2,017 lines.** `establish` appears **15×** and is **always** the
noun `establishment` — the named persons an office employs. `found` appears 5×, `construct*` 8×,
`create*` 1×, `build*` 0× — and every one is ordinary English, never a game verb: `:133` *"found-at-size"*
(inside a refusal), `:964` *"the gating audit found"*, `:1022` *"the respondent type that creates it"*,
`:1170` *"found thin everywhere"*, `:1412` *"the hole the testing found"*, `:1486` *"the gift path
constructs"*, `:1706` *"credit is constructed entirely out of claims"*.

Structurally: §4.4 `:416` defines `Office := (post, node, remit, conferral, revocation, establishment,
seat_items, upkeep, dates)` **with no constructor**. §10.2 defines a site and §10.4 defines the
accumulator that moves its `condition`; **no site ever comes into being.** §1.2 `:96`'s seven-rung ladder
has no act that adds a node.

**And the one refusal in the area is aimed at the wrong target.** §1.3 `:132-133` refuses
*"merge, split, promote, or found-at-size"* — correctly, because founding *at size* would be the
discontinuity the whole set-system exists to avoid. **But refusing found-at-size is not the same as
shipping founding-at-one**, and the document ships neither.

**Why it matters to play.** Combined with §2.1, **every structural quantity in the design is
monotonically non-increasing**: no births, no buildings, no new offices, no new settlements. The city
builder, 4X and management seats are not thin — they have no verb at all. And the strategic layer's
whole point, in a repo whose `CLAUDE.md` opens by naming territory control and domain actions, is that a
player changes what the map contains.

⚠ **AND ONE LIMB OF THIS IS DEFENSIBLE DESIGN RATHER THAN A DEFECT, folded in here from A12's
re-filing.** The containment tree also cannot be **re-parented** — no node changes its parent, ever. On
the original reading that was a finding; on Jordan's ontology it is **moot**, because *"a faction at a
territory level may hold a territory, but a territory is not a territorial faction"*: **the tree is
geography, and allegiance lives in factions.** Geography being static about places that already exist is
correct — a hamlet does not move because a King won a war. **What is NOT defensible is the tree's
inability to GAIN OR LOSE a node**: no settlement can be founded and none can be razed, and that is the
city-builder and 4X seat.

**THE FIX.** this §6 rank 1. `mint` on a Container is founding a settlement; `efface` on one is razing
it; `mint` on a Site is building; `mint` on an Office is establishment. **Re-parenting is not added and
should not be** — who holds the ground is `Tenure` (rank 2), not a parent pointer.

### §2.7 · A7 — THE FOUR LICENSED NON-ACT CHANNELS DO NOT MEET THE SEASONAL-CHANGE GUARANTEE, BECAUSE ONE IS INERT AND THE OTHER THREE ARE DECAY

**The claim.** Absent NPC acts, the world can only run down.

**The evidence.** §13.2 `:1636-1641` licenses **exactly four** non-act channels, *"these four, and only
these four."* Audited:

| # | channel | state |
|---|---|---|
| 1 | **metabolism and nature** — larders, bodies, `yield` | **live** — and every limb of it is consumption or ageing |
| 2 | **matter events** — a storm, a silted channel, a worked-out seam | ⚠ **INERT.** §13.2 `:1640` licenses it and §10.6 `:1370-1378` gates it with three conditions — and **nothing in the document generates one.** There is no matter-event generator anywhere. §10.4 `:1332` makes `condition` **act-only** by ruling (D-1), and §15.19 `:1836` records the narrowing: *"A site that decays with nobody touching it cannot be written as a term in the condition accumulator; it must be a matter event under §10.6's three conditions."* **The one channel that could produce untouched material change was closed, and its replacement was never written** |
| 3 | **memory confidence decay** | **live** — decay |
| 4 | **the calendar, LAPSE ONLY** | **live** — a deadline passing |

So the guaranteed seasonal change, absent NPC acts, is: **larders draw down, bodies age and die, memories
fade, deadlines pass.** Every one is a subtraction. NPC acts are the real churn engine and they are
genuine and good — but §2.1 removes their population's inflow, so even that decays.

**Why it matters to play.** *"The world is always in flux"* is the specification. Flux is not decay. A
world that changes only by running down teaches the player that absence always means loss, which is
precisely the failure §13.3 `:1670-1674` identifies and tries to answer — *"a world that only ever fails
you by omission is grim and, worse, **predictable**"* — and §13.3's answer, coincidence, is entirely made
of NPC acts.

> ⚠ **THE FIX, corrected from the form it was filed in.** The reviewing pass proposed reusing *"the
> `season_factor` roll the design already ships"*. **`season_factor` is not a roll in this document.**
> `:1404` calls it *"the shipped territory multiplier that a blockade, a march or a collapsing Order
> moves"* — acts move it — and the per-season roll is `(3 + d10)/8.5` at `:1396`, which is per-holding,
> not per-territory.
>
> **The corrected fix, still with zero new primitives and no new write class: DECLARE
> `season_factor(territory)` a per-territory, per-season DRAW with a published band, resolved in P1, and
> define a matter event as an extreme draw on it.** A storm is a bad `season_factor`; a good year is a
> good one. It is already territory-scoped, already impermanent by construction (`13:70-71` assigns
> permanence to `base(H)` and impermanence to `season_factor`), already inside a licensed write class
> (P1/matter), and already an operand of `yield` and nothing else — so it **cannot** violate D-1's
> act-only `condition` accumulator, because it never touches `condition`.
>
> **This also gives the world its first non-subtractive non-act channel**, since a draw has an upper
> half. That is the whole of what exception 2 needed and it was never written. **this §6 rank 4.**

### §2.8 · A8 — NO POLITY OF ANY SCALE CAN COME INTO EXISTENCE, AND THE POLITICAL MAP IS MONOTONICALLY SHRINKING

**⚠ This is the review's #1 finding.** It was filed as a defect about founding a conspiracy; Jordan's
clarification that a faction is the design's polity object **at every scale** makes it a defect about
the existence of realms.

**The claim.** A **Proposition** is an object no act can create; a faction is a proposition plus a
commitment map at any scale; therefore **no new realm, duchy, church, knightly order or polity of any
size can ever come into existence**, and the political map is frozen at world creation and can only
drain.

**The evidence.** §1.3 `:112`: *"A **faction** is a proposition plus a map from persons to a degree of
commitment. **That is the entire object.**"* §1.3 `:130-133` ships **one** membership operation:

> *"**One membership operation:** `commit(person, faction, Δdegree)`. Degree to zero is departure. A
> schism is a subset whose commitment **migrates to a rival proposition**; a merger is **members of A
> committing to B**; growth into a national body is many commits."*

`commit` takes a **faction**, not a proposition, and all three worked cases presuppose the target
exists. Searched exhaustively, the document contains **no operation that mints a proposition**. The only
two mentions are `:1490` — *"his stance emits a proposition"*, one clause in a worked example, with no
act, no cost, no witness, no phase, no signature — and `:1742`, §14 row 9, which **clears a refusal row
on the strength of a faction that "forms"** with no operation that forms it. #342 settles the lineage at
`02:746`: **`Conviction signature | authored with each proposition`.** Authored. Content.

**Consequence 1, and it is the whole weight of this finding — THE SCALE.** A faction is not a small
object. `:71`: *"a faction is a proposition plus a commitment map **at any scale**."* `:113`: *"Two
brothers who have sworn to burn out the reeve are a faction; **so is the Church of Solmund**."* `:318`:
*"the Church is a faction, a parish is a community."*

> **So the missing primitive does not block two brothers from founding a conspiracy. IT BLOCKS THE
> EXISTENCE OF POLITIES. No new realm, duchy, church, knightly order, guild, military order or polity of
> any scale can ever come into being. The entire political map is fixed at world creation, and the only
> motion the design permits is commitment draining out of the propositions the world shipped with.**
>
> And §1.3 `:130` makes the drain **irreversible**: *"Degree to zero is departure."* A faction whose
> commitment reaches zero is gone, nothing recreates it, and nothing creates a successor. **The political
> map is therefore not merely static — it is monotonically shrinking**, exactly as the population
> (§2.1), the structures (§2.6) and the licensed non-act channels (§2.7) are. It is the same disease on
> the object the whole strategic layer is made of.

**And it falsifies Jordan's requirement in that requirement's own words.** *"All starting national royal
factions may collapse in the game to be replaced with **dynamically generated ones**."* Collapse is
expressible — `commit` to zero for every member, which the design does elegantly. **Replacement is not,
because a dynamically generated Kingdom IS a minted Proposition, and no operation mints one.** The
design can lose every realm it shipped with and grow none.

**Consequence 2 — §10.1's flagship claim is false.**
`:1228-1230`:

> *"and 'the seam must be restored' is a proposition, and the people whose practice used it are already
> committed to it, so **a political faction forms out of a physical fact with no authoring at all**"*

Nothing makes that proposition exist. Nothing makes anyone committed to it before it does. **The
design's most celebrated emergent behaviour — the one §10 is built to produce and §14 row 9 is cleared
on — rests entirely on the one primitive the document does not have.** The sentence is not merely
unproven; it is unreachable on the document's own object list.

**Why a Proposition is worse than every other missing constructor.** Persons, claims, sites and cohorts
at least change population by a decider-free channel (death, eviction, individuation, P1). **A
proposition has no channel of any kind** — not act, not clock, not metabolism. Once absent, it can never
come to exist.

⚠ **And do NOT read this as a case for a `found_faction` verb or a merge verb.** §1.3 `:131-133` refuses
*"merge, split, promote, or found-at-size"* and is **right** to: founding at size is the discontinuity
the derived-scale argument exists to abolish, and §14 row 9 `:1742` forbids the field that would carry
it. What is needed is founding **at one** — a single person committing to a proposition that did not
exist a moment ago — which is `mint` plus the shipped `commit`, and is continuous by construction.

**THE FIX.** this §6 rank 1, applied to a Proposition. `mint` on a Proposition **is** faction founding;
`efface` on one is a faction dissolving rather than merely emptying. And it repairs `02:746` in the
right direction: **the conviction signature stops being authored content and is derived from the minting
person's stance at the moment of the act** — which is §5.1 `:511`'s own discipline, *"the target is
computed, never assigned"*, applied one level up.


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
> which is the whole design's posture, and nobody has a leader field to look up. **this §6 rank 3.**

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
a playable seat.** It is not in §6's ranking because it is **authoring, not a change** — see §6's closing
note.


---

## §3 · TIER 2 — MECHANISM CONTRADICTIONS

### §3.1 · B1 — §6.4's CONFLICT RULE FORBIDS THE COMMONS

**The claim.** The tragedy-of-the-commons mechanism and the conflict rule are mutually exclusive as
written.

**The evidence.** §6.4 `:689-691`:

> *"Every act declares `touches: {(object, mode)}`, mode ∈ `{read, alter, exclude}`. **Two acts conflict
> iff they share an object and either mode is `exclude`, or both `alter` the same field.** Conflicts
> route to `contest(container, prize, claimants)`."*

§10.3 `:1275-1279` requires the opposite: *"One boat among a harbour's forty moves at most a fortieth of
a quarter … **Closure is a collective outcome** — many actors, many seasons."* And §10.4 `:1333` sums
them: `condition(site) = clamp( condition(site) + Σ (this season's resolved condition deltas), 0, 1 )`.

Under §6.4 as written, all forty `alter` acts on `condition(harbour)` conflict **pairwise** and route to
a contest. The summation at `:1333` never happens; the commons never degrades collectively; §10 does not
work.

**Why it matters to play.** §10 exists to produce *many rational private acts making everyone's practice
worse, including the actor's* (`:1279`). The whole of the enlargement's N-line is that no single actor
did it. Route the forty acts to a contest and thirty-nine of them are losers who did nothing — which is
a competition over the harbour, not a tragedy of it.

> **THE FIX, and it REMOVES A CASE FROM THE RESOLVER: the real criterion is COMMUTATIVITY, and it is a
> property of the FIELD, not of the act.** Declare it once on the schema — `condition` is
> **additive-alter** (all writers apply, order-independent, which §5.5 `:614` already demands anyway); a
> succession pointer is **exclusive-alter** (contested). §6.4's rule then reads *"two acts conflict iff
> they share an object and either mode is `exclude`, or both `alter` the same **non-commutative**
> field"* — one word on a field definition instead of a case in the resolver, and §6.4 gets **shorter**.

### §3.2 · B2 — `capacity(date)` IS DOUBLE-COUNTED: SPENT AT `carry` AND USED AS THE CAP AT `compose_agenda`

**The claim.** The convener's power — which §12.4 `:1583` calls *"the cheapest real power in the game"* —
evaporates entirely under the document's own arithmetic.

**The evidence.** §8.2 `:874` charges `carry` *"one item of the container's standing-date capacity
# 05:176"*. §4.3 `:396` and §8.4 `:944` then use the **same quantity** as the admission cap:
*"`compose_agenda` admits the top `capacity(date)` of what was carried"*. And §4.3 `:396` asserts, in the
same table cell: *"**Carried items may exceed capacity — seventeen seatholders, eleven items — and the
convener chooses among them**."*

**All three cannot hold.** If `carry` spends a slot, then the twelfth carrier has no slot to spend and
cannot carry; carried items can never exceed capacity; and `compose_agenda` selects the top eleven of
eleven, which is not a selection. The convener's choice — the section's entire subject — does not exist.

**Why it matters to play.** §8.4 is the document's best political argument: burial is *"safe, not free"*,
and the convening office is *"worth holding, worth conferring, worth revoking, and worth killing for"*
(`05:218-224`, quoted at `:998`). Every word of it depends on there being more carried items than seats.
The defect is also **new** — it is a residue of the D-5 fix, which restored *"`carry` spends one of
each"* without re-checking what the second one was for.

> **THE FIX: `capacity(date)` is a SELECTION CAP, never a currency. `carry` spends `seat_items` only.**
> Delete the `# 05:176` cost line from §8.2's block and re-word §4.3's `capacity(date)` row from *"a
> carried petition **claims** one of these slots"* to *"a carried petition **competes for** one of these
> slots"*.
>
> **This also repairs §4.3's own thesis, which is currently false in kind.** `:389` claims *"Every price
> charged anywhere in this document is denominated in one of exactly two quantities"* — and one of the
> two is not a price. After the fix the claim is true, and the document has **one** currency and **one**
> cap rather than two of each.

### §3.3 · B3 — `R ≤ 1 → automatic clean success` IS THE FAST PATH §14 ROW 8 FORBIDS

**The claim.** There is an auto-resolve formula that changes the outcome distribution, inside the one
resolver, on a row §14 marks *"Clear."*

**The evidence.** §5.2 `:518-522`:

```
obstacle(context):
    if context.opponent is a person: return OPPOSED
    R = resistance_pool(context)
    if R <= 1: return 0                       # no roll; automatic clean success
```

§5.3 `:538-546` makes the bands a function of margin: margin 0 is **Costed Success**, +1/+2 is **Clean**,
≥ +3 is **Overwhelming**. Rolling at Obstacle 0 therefore yields Costed, Clean or Overwhelming — at Pool
1 the chance of zero successes is 0.6, which is Costed Success, the design's *"deliberate middle band"*
(`:548`). **The fast path returns Clean, always.** §14 row 8 `:1741` forbids *"a second resolver, an
auto-resolve formula, a fast path"* and marks it **Clear**.

**Why it matters to play.** Costed Success is the band the design most wants — *"you meet the obstacle
exactly and something is given up for it"* — and the fast path deletes it at exactly the low end §2
`:200` says is right and §17.1 `:1886` says was the testing's most important positive result. The
untrained fisher at Pool 1 opening an unfine lock should sometimes pay for it.

> **THE FIX: DELETE THE BRANCH.** Resolve at Obstacle 0 like anything else and read the margin off the
> draw. Strictly simpler, removes a second path from the one resolver, restores Costed Success at the low
> end, and lets §14 row 8's *"Clear"* be true. §5.3 `:557`'s cross-reference to *"the resolver skips the
> roll entirely (§5.2's `R ≤ 1` floor)"* goes with it — which incidentally removes the only case where
> Overwhelming's unreachability at Pool 1–2 was being papered over rather than stated.

### §3.4 · B4 — `transfer` HAS NO CONSERVATION PRECONDITION

**The claim.** `transfer` mints mouth-seasons from nothing.

**The evidence.** §11.2 `:1424-1428`:

```
transfer(giver, receiver, amount)          -- amount in the SAME `stores` scalar, mouth-seasons
   precondition: giver and receiver co-present, OR the amount is entrusted to a carrier act
   effect:  stores(hearth(giver)) −= amount ;  stores(hearth(receiver)) += amount
```

The **only** preconditions are co-presence or a carrier. And §11.1 `:1392` states
`stores(h) += draw(h) − mouths(h)` *"**may go negative**: a shortfall is a debt."* So a hearth at −4 may
transfer 1,000 and the receiver is 1,000 richer.

**Why it matters to play.** §11.4 `:1478-1484` makes `stores`-as-realm-denominator a live choice for
Jordan between *logistics-real force* and *coin returns by the back door*. **An unbounded-below fungible
transferable scalar is neither. It is counterfeit**, and it makes the fork undecidable, because the
"coin returns" arm assumes conservation and the "logistics-real" arm assumes the grain physically exists
where it stands. It also breaks §11.5's gift path, the one constructive route to unintended rescue: the
rival lord need not have any grain.

> **THE FIX, one line: `precondition: stores(hearth(giver)) ≥ amount`.** Negative `stores` stays what it
> is — a debt a hearth carries — and stops being a mint. §11.4's fork becomes honest, and §11.3's
> *"No second unit, no conversion, ground untouched"* rebuttal becomes true rather than merely
> denominationally true.

### §3.5 · B5 — RESTORATION HAS NO SIZING RULE, AND THE IMPLIED ONE IS UNUSABLE

**The claim.** A degraded site cannot be brought back, which guts §10.1's political payoff.

**The evidence.** §10.3 `:1261` sizes **damage only**:
`Δcondition(site) = − condition(site) × f(degree) × share(actor, site)`. §10.4 `:1336` is the entire
specification of the other direction: *"`alter` deltas are negative; **restoration acts are positive**."*
No form, no sizing, no bound.

The implied reading — same multiplicative form with the sign flipped — is unusable, because
`Δ = + condition × f × share` is proportional to what is **left**. A site at `condition = 0.05` restores
at 5% of the rate of a healthy one. **A dead site is unrestorable, and the deader it is the slower it
comes back.**

**Why it matters to play.** §10.1 `:1228-1230` is the section's payoff: *"the seam must be restored" is a
proposition, and the people whose practice used it are already committed to it, so a political faction
forms out of a physical fact.* That faction's programme has to be **achievable** or it is a grievance,
not a politics. A restoration faction that can never restore anything is a permanent opposition with no
victory condition — which is not the game §10 advertises.

> **THE FIX, an exact mirror with no new primitive:**
> `Δcondition(site) = + (1 − condition(site)) × f(degree) × share(actor, site)`
>
> Same degree ladder, same `share` term, same clamp, symmetric in form. It is proportional to the
> **headroom** rather than the remainder, so a dead site has a real road back and a healthy one is cheap
> to maintain and expensive to gold-plate — which is the correct shape. It keeps every anti-leverage
> property §14 row 11 `:1743` is cleared on: still a fraction, still scaled by degree, still **falls as
> N rises**, and §10.3's stated falsifier applies to it unchanged.

### §3.6 · B6 — P7's SALIENCE-RANKED EVICTION IS AN UNLICENSED DECIDER-FREE CHANNEL RUNNING ON A SOCIAL QUANTITY, AND IT DESTROYS §3.3's BEST INSIGHT

**The claim.** Forgetting is currently motivated **deletion** rather than motivated **retrieval**, and it
is licensed by nothing.

**The evidence.** P7 `:654`: *"claim confidence decays; **ledgers evict lowest salience** (this is
forgetting, not a data limit)"*. And `salience` is defined at `:254`:

```
salience(c) = recency(c) × confidence_live(c) × relevance(c, q) × stanceweight(c, person)
stanceweight(c) = clamp(1 + λ·agreement(c), 0.05, 2.0),   λ = obstinacy / 5
```

**`stanceweight` is a social quantity** — it is the person's agreement with the claim, scaled by
obstinacy. So eviction is a threshold over a social quantity, firing a permanent outcome, with no decider.

**Three licences are checked and none covers it.** §13.2 `:1636-1641` licenses exactly four channels;
exception 3 is *"the **confidence** of a memory decaying"*, and **eviction is deletion, not decay**.
§10.6 condition 1 `:1370-1373` states the general rule — *"no band edge may ever be defined over"* a
social quantity — naming standing, regard, grievance, cohesion and commitment. **And §6.3 `:672-678`
licenses exactly three write classes by phase: calendar (P0), matter (P1), acts (P5) — "There are exactly
three write classes, and no others may be added."** P7 writes to ledgers, and P7 is none of the three.
The whole of RECKON sits outside the licence the document states two sections earlier.

**Why it matters to play, and this is the part that hurts.** §3.3 `:260-263` is the best paragraph in the
document:

> *"A Templar with obstinacy 5 holding an exonerating claim about a Southern Einhir smith gets
> `stanceweight = 0.05`: the claim is in his ledger, at high confidence, and its salience is one
> twentieth of an agreeing claim's. It does not enter the top-K. **He is not hiding it and he is not
> lying; he is not thinking of it.** … What is attenuated is **retrieval, not value**."*

Under stance-ranked eviction, the Templar's exonerating claim is the lowest-salience row in his ledger
every single season, so it is the **first thing evicted**. Within a few seasons he **genuinely does not
have it** — and the sentence *"what is attenuated is retrieval, not value"* becomes false about the very
example that proves it. Motivated reasoning silently becomes motivated amnesia, the 0.05 floor stops
being *"motivated reasoning, not a wall"*, and the devastating firsthand contradiction that was supposed
to be able to cross has been deleted from the ledger it would have crossed into.

> **THE FIX, and it REMOVES A TERM: rank eviction by `confidence_live × recency` ONLY.**
>
> Those are the two clock quantities exception 3 already licenses, and neither is social. Forgetting
> becomes epistemic — you lose what is old and what you were never sure of. **Retrieval stays motivated;
> the ledger stops being.** §3.3's sentence stays true, the Templar keeps the claim he is not thinking
> of, and the day a firsthand contradiction lands the claim is still there to be crossed to.
>
> **And state P7's write licence explicitly in §6.3** rather than leaving four operations outside a list
> that says it is exhaustive — either as a fourth class (*interior*: a person's own ledger and nothing
> else, which is a genuinely different licence from the other three and is why it is safe) or by
> folding P7 into P1's matter class on the ground that confidence decay is already licensed there. **The
> document must pick one; today it has an unlicensed phase.**

---

## §4 · TIER 3 — UNIFORMITY, TYPING, PRIMITIVES

### §4.1 · C1 — `contest(container, prize, claimants)` HAS THREE CALL SITES AND THREE CLAIMANT TYPES

⚠ **Corrected from the filed form, which said four of each.**

**The evidence.** Three literal calls: §4.1 `:327`, claimants are **factions** (*"where claimants are
**factions**, which need not be siblings in the tree"*); §6.4 `:691`, claimants are **conflicting acts**;
§9.2 `:1141`, `claimants = {enforcement, resistance}` — **two abstract sides**. A fourth site is prose:
§10.3 `:1293`, *"a contested physical act against **whoever defends the site**"* — a defender, and no
call is written.

**Why it matters.** This is the design's most-reused function and it is untyped. Three types today means
three branches inside it tomorrow, which is §14 row 13's per-entity branch arriving through the front
door as a per-*kind* branch.

**THE FIX: claimants are always a set of persons with a stake.** A faction resolves to its committed
members with an address inside the container (which §1.3 `:118-119` already computes); an act-side
resolves to its actor plus anyone who `touches` the same object; `{enforcement, resistance}` resolves to
the persons in the issuer's employ present here, against the persons who would be bound. **One type,
three call sites, no branch** — and it composes with §4.4 `:436`'s establishment rule, which already says
the pool for an act by remit is the establishment's rather than the holder's.

### §4.2 · C2 — `Claim` AND `Proposition` ARE THE SAME PRIMITIVE, DECLARED TWICE

**The evidence.** §3.1 `:220`: `Claim = (subject, predicate, value, when, source, confidence,
visibility)`. §12.1 `:1514`: `Proposition = (mood, subject, predicate, value, when, scope)`, with `:1519`
conceding it outright — *"`HOLDS` is claim-shaped without the epistemic fields."* And both carry the same
`when` rule and the same collision consequence, stated twice: §3.1 `:227-228` (*"Claims collide iff same
subject, same predicate form, same arguments, intersecting `when`, incompatible values"*) and §12.1
`:1520` (*"`when` is a mandatory interval exactly as in §3.1, so **assertion and denial collide
automatically**"*).

**Why it matters.** §0 `:21` states the document's own governing rule: *"**One rule lives in one place.**
… If a rule appears twice, that is a defect in this document."* This is that defect, on the most
load-bearing rule in the epistemics layer.

> **THE FIX, bottom-up, and it is a net subtraction of declared structure:**
> ```
> Assertion   = (subject, predicate, value, when)
> Claim       = Assertion + (source, confidence, visibility)
> Proposition = Assertion + (mood, scope)
> ```
> The `when`-interval rule and the collision rule are then defined **once**, on `Assertion`. §3.1's
> collision and §12.1's *"assertion and denial collide automatically"* stop being two statements of one
> rule and become the same code. It also makes A8's fix cheaper: `mint` on an Assertion covers both a
> firsthand claim and a founding proposition.

### §4.3 · C3 — THE CLOSED PREDICATE VOCABULARY IS NEVER ENUMERATED

⚠ **Narrowed from the filed form.**

**The evidence.** §3.1 `:231-233`: *"**The predicate vocabulary is CLOSED**; the referent space is OPEN.
Claims support exactly three operations — collision, entailment, relevance — and **all three are
functions of the predicate's *form***. Open forms mean each operation is authored per form, which is a
scripting language with a rules engine attached."* **The document names one form in 2,017 lines** —
`SAID(Aldwin, C, season 12)` at `:238` — and names it as an illustration that claims may be subjects of
claims, not as a roster member. §17.1 `:1881` then lists *"the closed predicate vocabulary"* among the
things that survived testing unchanged.

**Why it matters.** A closed set with one example is not closed; it is unspecified. Every operation in
the epistemics layer — collision, entailment, relevance, and therefore `salience`, view assembly, the
argument system's `support[]`, and F11's *incoherent assertion* — is defined as a function of a form that
does not exist yet. **This is the largest implementability gap in the strongest layer of the design**,
and epistemics is on Jordan's in-scope list.

**THE FIX.** Enumerate the closed set in §3.1, with each form's collision, entailment and relevance rule
beside it. `SAID` is one. The document's own worked cases imply several more — a value-at-a-subject form
(`condition(harbour) = low`), a location form (presence roll-ups), a holding form (`Holding(person,
office)`), a compliance form (`:1179`, *"Compliance was rendered"*), an obligation form. **Until the set
is written the layer cannot be built, and §17.1 should not list it as settled.**

### §4.4 · C4 — `remit.acts` IS A "CLOSED SET OF FIVE" HOLDING SEVEN OPERATIONS

**The evidence.** §4.4 `:421-424`: *"`remit.acts` is drawn from a **closed set of five** … **issue** …
**determine** … **confer/revoke** … **dispatch** … and **convene**."* `confer/revoke` is two operations in
one slot — and §4.4 `:426` then splits the fifth: *"⚠ **`convene` names TWO distinct operations and they
are separate acts** (D-6): **setting** a standing date, and **ordering its items**."* **Five slots, seven
operations**, and the document says so itself one line later.

**Why it matters.** `eligible(p, act, n)` consults `remit` (`:436`). A remit that grants `confer` and not
`revoke`, or `convene`-set and not `convene`-compose, is a real and interesting political object — a
prelate who may appoint but not remove, a chair who may schedule but not order the agenda. Bundling them
makes those grants unsayable.

**THE FIX.** Say **seven**, and list them separately: `issue`, `determine`, `confer`, `revoke`,
`dispatch`, `convene_set`, `convene_compose`. The closed-set discipline is preserved and the number
becomes true. §7.3 C1 and C2, which already have to name *which* `convene` operation they charge, get
shorter.

### §4.5 · C5 — COHORTS GET A DIFFERENT VIEW RULE THAN PERSONS, IN THE DOCUMENT THAT FORBIDS EXACTLY THAT

**The evidence.** §2 `:210-211`: *"**One type, not two:** if a cohort were a different type, every
mechanism would be written for one and not the other and the design would acquire an elite-only politics
by accident."* P3 `:650`: *"top-K claims by salience per person (§3.3); **K = 3 per cohort**"* — against
§3.3 `:252`'s `K = 7 + Focus + 2 per Knot consulted − Coherence penalty`.

**Why it matters.** It is a hardcoded constant that makes cohorts a second type in exactly the way §2
forbids — and it is the mechanism by which *"an elite-only politics by accident"* would actually arrive,
since a cohort reasoning on three claims and a named person reasoning on nine will diverge
systematically in favour of the named.

**THE FIX, and it DELETES A CONSTANT.** Cohorts hold no Knots by construction (a Knot is a person's
binding, and §2 `:212` makes holding one a de-individuation blocker), so the `+2 per Knot` term is zero;
a cohort's Focus is its distribution's mean; a cohort's Coherence penalty is its distribution's mean.
**The general formula already yields a small K for a cohort.** Delete `K = 3` from P3 and let §3.3's one
formula run for both, which is what §2 says the design does.

### §4.6 · C6 — `Focus` AND `Coherence` ARE READ BUT OWNED BY NOBODY

**The evidence.** §3.3 `:252` reads both: `K = 7 + Focus + 2 per Knot consulted − Coherence penalty
(Dissonant 1 … Severed 5)`. §2's six fields (`:168-179`) carry neither. §4.2's ownership table
(`:334-340`) carries neither. #342 owns Coherence explicitly at `02:750`: **`Coherence | drift + discrete
writes | the person | mark reads, primaries, tellings, individuation | any cost on Thread use and
betrayal`**.

**And §16 `:1871` makes the Coherence-0 ontology a live choice for Jordan** — *"Two incompatible readings
ship — loss of capacity, versus *a person has become an object*. Three arcs and two named absences turn
on it"* — **about a quantity the document never declares.** §17.4 `:1938` carries it forward as an open
finding, still without declaring the field.

**Why it matters.** This is the same class as §2.1–§2.3: a quantity #342 owned, that this document reads
and does not carry. It is worse than the others because the document escalates a design fork about it to
Jordan while leaving it undefined, which makes the fork unanswerable — you cannot rule on what
Coherence-0 means when Coherence is not a field.

**THE FIX.** Add `Coherence` to §2's field table and to §4.2's Person row, with `02:750`'s producer
(*drift + discrete writes*) and consumers. Add `Focus` the same way, or — if Focus is meant to be an
attribute rather than a field — say so in §5.1, where attributes are declared. The document must not read
a quantity it does not own.

### §4.7 · C7 — A DEFINED SELECTOR WAS REPLACED BY AN ADJECTIVE

**The evidence.** §5.1 `:498`: `Pool(person, practice) = Attribute[relevant](person) +
Practice[practice](person)`. #342 `02:197`: `contributed(actor, attempt) = attr[triad_axis(attempt.practice)]`.

**`triad_axis` is a function; `relevant` is a hope.** Every attempt in the game selects its attribute
through this expression, and as written the selection is made by an adjective with no definition, no
domain and no owner — the exact shape §5.1 `:510-512` refuses two paragraphs later: *"A difficulty number
must be decided by somebody, and that somebody is the GM this game does not have."* An attribute chosen
by *relevance* is decided by somebody.

**THE FIX.** Restore `triad_axis(practice)` from `02:197`, with a citation. The selector becomes a
function of the practice — a property already on the person's schema — and the pool is computed rather
than judged.

### §4.8 · C8 — STANCE REFERENTS DO NOT COVER WHAT THE DESIGN DEPOSITS ON

**The evidence.** §2 `:175`: stance is *"one table, `referent → attitude`, referents being **persons,
factions, propositions and places**."* But §8.2 `:911` deposits grudges on **containers**: *"a claim
naming an actor deposits on him; **one naming only the container deposits on the container**"* — and
§8.7 `:1085` builds the whole road to revolt on *"a stance row with a negative attitude toward **a
container** or a person."* A hearth is a container and is not obviously a place. And §17.4 `:1941` notes
a fifth gap: **procedures** are not referents, *"while at least one canon body is made of one."*

**Why it matters.** §8.7 `:1114` is the design's answer to revolt without a revolt meter — *"there is no
number on Goldenfurt, only rows in the stance tables of named persons in it"* — and those rows have a
referent type the schema does not admit. Grievance-at-an-institution, which the document identifies as
the durable kind (*"a grudge at a person is discharged by removing the person; a grudge at a container is
not"*, `:912`), is unrepresentable.

> **THE FIX, and it REMOVES A CATEGORY:** referent ∈ `Person | Faction | Proposition | Container`.
> **Fold Place into Container** — §1.2's containment ladder is the design's only spatial structure, so
> every place in the design already *is* a container — and express a procedure as a Proposition, which is
> §17.4 `:1941`'s own precedent answer (*"the rules of order as they stand is expressible as a
> Proposition"*). Four referent types instead of five, and every deposit the document performs is legal.

### §4.9 · C9 — §4.1 STOPS AT FOUR OF SEVEN RUNGS AND DOES NOT SAY THE SILENCE IS DELIBERATE

⚠ **NARROWED ON JORDAN'S CORRECTION. The filed version read this as a governance gap; it is a statement
gap.**

**The evidence.** §1.2 `:96` names seven rungs: *"**Person → Hearth → Community → Settlement → Territory
→ Province → Realm**"*. §4.1, titled *"What each rung owns"*, specifies **four** — Individual `:302`,
Hearth `:304`, Community `:311`, Settlement `:321` — and then stops. Territory, Province and Realm are
never mentioned again in that section.

**Why the filed reading was wrong, and this is worth stating because it took a correction to see.** The
finding was filed as *the design has governance at four scales and a naming convention at three*. **It is
substantially answered by the architecture: political action above Settlement runs through FACTIONS and
OFFICES, not through container state.** A faction is a proposition plus a commitment map *"at any
scale"* (`:71`), an office cluster *"has offices even where it has no container"* (§8.1 `:848`), and
`:116` insists *"Scale is derived and gates nothing."* **The upper rungs owning nothing is not an
omission; it is the same refusal that makes the whole alignment layer work.** They are address
aggregation — the thing you roll `presence` and `density` up through — and nothing more.

**What is still true, and it is small but real.** **§4.1 never says that.** A reader reaching the end of
the section cannot tell whether the three missing rungs are a deliberate architectural statement or three
unwritten paragraphs, and this reviewer could not either. A section whose title promises to say what
*each* rung owns, and which covers four of seven in silence, invites exactly the misreading it produced
here — and will invite it again from an implementer deciding whether to give `Territory` a state class.

**THE FIX, one paragraph and no mechanism.** Add a closing line to §4.1: *"Territory, Province and Realm
own nothing of their own. They are address aggregation — the levels `presence`, `density` and
`footprint` roll up through — and every contested thing at those scales is held by a faction, an office
or a person. That is deliberate: a rung that owned a stake would be a polity with a level, which §1.3
abolishes."* Then §1.2's seven-rung ladder is legible and nothing else changes.

### §4.10 · C10 — THE DETERMINISM SCHEME COVERS ONLY ATTEMPTS

**The evidence.** §5.5 `:609`: *"Per-attempt substreams derived from a hash of `(world seed, tick, **actor
id, attempt discriminator**)`, never from a shared sequence."* P1 `:648` rolls things with neither: the
`yield` roll's `d10`, wounds closing or festering, bodies ageing and dying, travellers advancing a leg.
**None has an actor and none has an attempt**, so the scheme does not reach the phase §6.3 `:675` licenses
as an entire write class.

**Why it matters.** §5.5 `:614` names the property to guard: *"**Order independence is the property to
guard, because its absence is invisible.**"* P1 is where the world's own churn happens, and it is
currently outside the guarantee — so adding a hearth somewhere could re-phase every other hearth's harvest
and nothing would show it.

**THE FIX, a generalisation that weakens nothing:**
`(world seed, tick, subject id, purpose)` — where `subject` may be a person, a site, a hearth or a body,
and `purpose` is what an attempt discriminator is a special case of. An attempt is then
`(seed, tick, actor, attempt)` unchanged, and `yield` at a holding is `(seed, tick, holding, "yield")`.
Order independence extends to P1 for free.

### §4.11 · C11 — TWO DIE-READING SEMANTICS, UNDECLARED

**The evidence.** §5.1 `:494`: *"Every attempt rolls **N ten-sided dice**. 1–6 scores nothing, 7–9 scores
one success, 10 scores two."* §11.1 `:1396`: `yield(H, season) = base(H) × condition(site(H)) ×
season_factor(territory) × **(3 + d10)/8.5**` — a **raw uniform d10 read as a magnitude**, with `:1399`
confirming *"it ranges `0.47×base` to `1.53×base` with mean exactly 1.0."*

Two randomisation primitives in a document whose §5 is titled *"One roll"* and whose §5.5 `:620` insists
*"A path that computes an outcome without running the same resolver is a second resolver whatever it is
called, and it will diverge."*

**Why it matters.** Less than the other Tier 3 items, and it may well be correct — nature has no skill,
so a success-counting pool is the wrong instrument for weather. But it is **undeclared**, and an
implementer reading §5 will build one die-reader and then meet the other in §11.

**THE FIX, either limb, but one of them.** Either license the second reading in §5.1 with its reason
stated (*a magnitude drawn by nature, which has no capability to express as a pool*) and note that it is
the only such reading in the design; or express `season_factor`'s draw as a pool and keep one
die-reading in the engine. **Given §2.7's fix makes `season_factor` a declared draw, the second limb is
now the cheaper one and should be preferred.**

### §4.12 · C12 — EIGHT PHASES ARE CALLED SEVEN

**The evidence.** `:54` (*"The season — seven phases, three write classes"*), `:624` (*"§6 · THE SEASON —
SEVEN PHASES"*), `:641` (*"§6.2 The seven phases"*). The table at `:647-654` lists **P0 through P7 =
eight rows**.

**THE FIX.** Say eight, in all three places. It is a one-word correction and it is here only because a
document whose §0 rule is *one rule lives in one place* should not miscount its own spine three times.

### §4.13 · C13 — THE PHASE LIST CONFLATES "BARRIER" WITH "STEP"

⚠ **This is a restructuring proposal, not a contradiction. Nothing in the document is false here.**

**The observation.** Of the eight phases, **P0, P1, P5 and P6 are genuinely global barriers** — calendar,
matter, resolve, witness — and each needs every prior phase complete before it starts. **P2, P3, P4 and
P7 are per-person pure maps**: needs from situation, top-K from ledger, act from view, and reckoning over
one's own ledger. Nothing in P2–P4 reads another person's P2–P4 output.

**THE PROPOSED CHANGE: state the loop as four global barriers plus one per-person map.**

```
season(world):
    P0  CALENDAR    -- global
    P1  SETTLE      -- global; matter
    for each person or cohort, independently:            -- ONE map, not four passes
        needs  <- need(person, frozen_world)
        view   <- assemble(person, needs)
        act    <- choose(person, view)
    P5  RESOLVE     -- global
    P6  WITNESS     -- global
    for each person, independently: reckon(person)        -- interior only
```

**Three things it buys.** It is **faster** — two fewer full-population passes, and needs and views never
materialise as populations. It is **more modular** — the map is one function, `person + frozen snapshot →
(act, ledger delta)`, which is the unit a Godot port would thread. And it **tightens §6.3's own licence**:
the three write classes become **exactly the three global phases that write**, and the per-person map
writes nothing but the person's own interior. That is a strictly stronger statement than §6.3 makes
today, and it is the clean way to close §3.6's P7 licence gap: the interior map is the fourth licence,
and it is safe precisely because it cannot reach anything but the person.

### §4.14 · C14 — THE TWO ALLOWANCES SHOULD BE ONE, AND THAT DISSOLVES D-2, THE DESIGN'S LARGEST OPEN RULING

⚠ **Also a restructuring proposal. It is here because it is the largest primitive reduction available in
the document, and because it answers an escalation from architecture — which is `CLAUDE.md` §0's fifth
test, not an escalation.**

**The observation.** §6.1 `:628` (*"Every person and every cohort commits exactly one act per season"*)
and §4.3 `:399`'s `seat_items(office)` (*"how many things he can hear or carry in a sitting … Holding two
offices does not double a day"*) are **the same kind of object**: a finite, per-period, spendable
allowance owned by an entity and consumed by acts. The document treats them as two quantities and then
spends a live ruling (D-2) and a live exploit (D-16) on the relationship between them.

> **THE PROPOSED CHANGE: one primitive, `Allowance(owner, period, size)`, and make `seat_items` an
> EARMARKED SUB-BUDGET of acts** — hours spendable only on sitting business.

**Four consequences, and the second is the point.**

1. **D-2 stops being a fork and becomes a parameter.** §16's largest open ruling is currently *"one act
   per season, or a holder's several?"* Under one allowance it is *"how large is the earmark"* — a
   number, tunable, with the personnel-game reading at earmark 0 and the decree-game reading at a large
   earmark, and every intermediate available. **The two games §16 says are materially different become
   two settings of one dial**, and a Duke's season stops being a category question.
2. **D-16's cohort exploit prices itself.** §16 `:1866` records it: *"individuate your own cohort and get
   eleven acts instead of one"*. Under one allowance owned by the entity and sized by weight,
   **individuating a cohort SPLITS its allowance; it does not mint one.** The exploit is not forbidden by
   a rule; it does not exist. That is the design's own preferred shape — §8.7 `:1091` refuses a revolt
   meter for exactly this reason.
3. **§4.3's *"exactly two quantities"* becomes one primitive with a tag**, and combined with §3.2's fix —
   `capacity(date)` demoted from a currency to a selection cap — **the design goes from three
   capacity-like objects to one `Allowance` and one cap.**
4. **It composes with §2.1.** A cohort's allowance scales with its weight, so a population that grows has
   more acts in it. Today, with no inflow, the realm's total act budget is also monotonically
   non-increasing.


### §4.15 · C15 — A FIFTH VOCABULARY COLLISION THAT §3.4's TABLE DOES NOT RECORD

⚠ **Inverted from the form it was filed in. The filed version was falsified on disk and is withdrawn.**

**What was filed, and why it is wrong.** The finding was *the terminal document added `visibility` to the
claim tuple without recording it as a ruling*, on the ground that `01_substrate.md:228` gives six fields
— `(subject, predicate, value, when, source, confidence)` — against `10_SUPERSEDING.md:221`'s seven.
**`03_knowledge_telling_investigation.md:21` ships the seven-field tuple with `visibility`**, and §3.4
`:272-274`'s own conflict rule — *"the document whose declared subject is that object wins"* — selects
doc 03, whose declared subject is knowledge, over doc 01. **The terminal document is applying its own
rule correctly. Withdrawn.**

**What survives, and it is real.** Three of #342's documents state the substrate's memory row and they do
not agree: `01:228` and `07:32` give six fields; `03:21` gives seven. **That is a fifth vocabulary
collision, and §3.4's table records four.** §3.4 `:275` presents the table as complete — *"The four
rulings this document makes under that rule, **all of them recorded rather than silent** (C-16)"* — and
C-16's own challenge at `:1976` was *"four vocabulary collisions, not two, and two were ruled silently."*
**The count was wrong again, one round later, in the same direction.**

**Why it matters.** Less than any other Tier 3 item, and it is here for one reason: **the collision is on
the design's most central primitive**, and §3.4's table is the document's own instrument for making sure
no such ruling is silent. A silently-correct ruling on the claim tuple is still a silent ruling, and the
next reader who checks doc 01 will reach the wrong conclusion — as this review's own reviewing pass did.

**THE FIX.** Add a fifth row to §3.4's table: *the claim tuple — `01:228`/`07:32`'s six fields against
`03:21`'s seven — **ruled seven**, on the ground that doc 03's declared subject is knowledge.* One row,
and §3.4's *"all of them recorded"* becomes true. Change *four* to *five* in the same sentence.

---

## §5 · TIER 4 — COVERAGE AGAINST JORDAN'S EXPLICIT LIST

Seasonal loop in scope; mass battle, personal combat and social contest deferred.

### §5.1 Well specified — and this is a long list

Containment ladder §1.2 · factions and derived scale §1.3 and §8.7 · **epistemics, memory and truth §3
and §13.4, the strongest material in the suite** · petitions, carriage, standing, agenda, expiry §8 ·
orders and executors §9.3 · obligation (`requisition`) §4.1 · offices §4.4 · conflict and resolution §5
and §6.4 · clocks §7 · competing beliefs §3.3 and §13.4 · **parliamentary debate §12 — the stasis ladder
plus twelve named faults with severities is the best-specified object in the document and is the model
the rest should be held to.**

### §5.2 Absent, or one line

| subject | state |
|---|---|
| **character generation** | **0.** §2.2 |
| **advancement and demotion** | **0.** `grep -ci advancement` = 0. §2.3 |
| **birth and natality** | **0.** `grep -ci "birth\|natality"` = 0. §2.1 |
| **occupations and roles distinct from office** | **0.** `occupation` and `profession` = 0. A person's economic identity is `Practice` (§2 `:173`) and nothing else; there is no role a person occupies that is not an office. §2.11 |
| **property, grant and confiscation** | ⚠ **`holdings` is DEAD STATE** — two descriptive occurrences, no act that reads, writes or moves it; `confiscat`/`enfeoff`/`dispossess`/`seize` = 0. §2.10 |
| **borders, annexation, secession** | ⚠ **THE CONTAINMENT TREE IS IMMUTABLE.** `annex`/`seced`/`conquer`/`vassal`/`absorb`/`border`/`reparent` = 0; no node can be added, removed or re-parented. §2.12 |
| **faction leadership** | ⚠ **NO LEADER AND NO DERIVATION.** `founder`/`leadership`/`spokesman` = 0; both occurrences of `leader` are §4.4's office-pool argument. §2.9 |
| **field investigation** | ⚠ **ONE SENTENCE**, `:1715-1717`, asserted as *"the engine's answer to its own epistemics, not a subsystem: when the same fact is disputed and it matters, somebody goes and looks, which is an act, by a person, who can be lied to."* **No verb, no cost, no resolution path, no obstacle owner.** The claim is right and the mechanism is absent |
| **threats and pressures** | **0.** `plague` = 0, `invasion` = 0, `threat` = 0. Off-board polities are §16's last unresolved live choice, and §16 `:1873` states the cost honestly: *"allow an actorless pressure … would be the only exception to §1.1 in the design"* |
| **matter-event generation** | ⚠ §13.2 `:1640` **licenses** it and §10.6 `:1370-1378` **gates** it; **nothing generates one.** §2.7 |
| **governance above Settlement** | ⚠ four of seven rungs. §4.9 |
| **`Venue`'s parameters** | ⚠ **17 parameters at `:1571-1574`** — twelve in the tuple, five in the door — and **not one carries a range, a default or a numeric value anywhere in the document.** Two (`enter`, `speak`) get a domain (*"predicates over marks, office, standing and commitment degree"*); one (`admissible_source`) gets two prose illustrations at `:1591-1593`. The remaining fourteen — `admission_floor`, `exchange_budget`, `article_count`, `coupling_depth`, `veto_holders`, `privileged_custody`, `record_custody`, `attendance_cost` and the rest — appear once each, in the tuple, and never again. **In the document meant to be the ideal code shape, its most parameter-heavy object is entirely unvalued** |

### §5.3 The genre lineage, mapped to seats

Jordan names the lineage: grand strategy · strategy · 4X · RPG · city builder · political and economic
simulation · management · interactive fiction · detective · historical precedent. Each implies a seat.

| lineage | the seat in this design | state |
|---|---|---|
| **interactive fiction / political sim** | the sitting: stasis ladder plus twelve named faults (§12) | **BUILT, and it is the best object in the suite** |
| **grand strategy** | the down-stroke: one order, thirty-five executors, reports-as-claims (§9.3) | **BUILT and excellent** — for what a realm *does*. ⚠ For what a realm *becomes*, see 4X below: the map cannot change (this §2.12) |
| **political simulation** | petition, carriage, agenda, burial, expiry (§8) | **BUILT** |
| **historical precedent** | caste at the second gate, cadet branches, hostage politics, non-delivery versus refusal | **BUILT, and it is the design's strongest claim to originality** |
| **detective** | field investigation | ⚠ **ONE SENTENCE** (`:1715-1717`). The epistemics layer that would carry it is world-class. **The detective seat is the largest built-adjacent opportunity in the design — everything it needs already exists** and what is missing is a verb, a cost and an obstacle owner |
| **RPG** | advancement, character growth | ⚠ **GONE** (§2.3) |
| **RPG / world churn** | character generation, birth | ⚠ **GONE** (§2.1, §2.2) |
| **city builder / management** | building, founding, infrastructure | ⚠ **ABSENT** (this §2.6) |
| **4X** | expansion, founding, borders | ⚠ **ABSENT, and worse than thin.** No act adds a node (this §2.6); **no act re-parents one either, so annexation, conquest, secession, partition, independence and vassalage are all inexpressible** (this §2.12); three of seven rungs own nothing (this §4.9) |
| **economic simulation** | market, price, exchange | ⚠ **STATED AS FAILING BY THE DOCUMENT ITSELF** (§11.5 `:1500-1508`, §15.6): gift constructs, market does not |
| **strategy / external threat** | plague, invasion, off-board pressure | ⚠ **ABSENT.** §5.2 |

**Six of eleven seats are built and four of those are excellent. Every one of the five that is missing is
a seat whose verb changes WHICH THINGS EXIST, OR WHO HOLDS THEM** — a person, a rank, a building, a
settlement, a faction, a border, a holding, a fact brought to light. That is this §1.1's finding arriving
from a third independent direction — after the grep and after this §1.2's trajectory table — which is the
strongest form of corroboration available to a review that measured nothing.

---

## §6 · THE TEN CHANGES THAT WOULD DO THE MOST, RANKED

Ranked by design bought per unit of change. **Six of the ten are subtractions, and ranks 1–4 are the four
changes that take Jordan's own long-arc trajectories from three of ten transitions to nine of ten**
(§1.2) — which is why they are ranked together, ahead of changes that are individually larger.


### Rank 1 · ADD `mint` AND `efface` TO §6.4's `touches` MODES

**The change.** §6.4 `:689` ships three modes: `mode ∈ {read, alter, exclude}`. Add two:
**`mode ∈ {read, alter, exclude, mint, efface}`.** An act may bring an object into the world or remove
one from it, under the ordinary machinery — witnessed by presence (§1.4), contested where someone objects
(§6.4, as repaired by rank 7), resolved in **P5's existing acts class** (§6.3, no new write class), sized
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
building, a person's presence for a birth, `capacity(date)` for an office conferred at a sitting. Rank 5
is what makes that cost coherent.

### Rank 2 · `Tenure` — THE MISSING RELATION, AND THE ONE PROPOSAL THAT KEEPS JORDAN'S DISTINCTION  *(A10 · A12)*

**The change.** The design has **no relation by which anything holds anything**. It has a post-holding
edge and a membership edge, and it needs a third that is neither:

```
Tenure := (subject, object, since, conferrer, degree?)
   subject ∈ Person | Faction
   object  ∈ Office | Site  | Node
```

> ⚠ **`commit(person, faction, Δdegree)` is NOT folded into this, and refusing to fold it is the
> proposal's strongest argument.** Jordan: *"A faction at a territory level may hold a territory, but a
> territory is **not** a territorial faction."* **Membership is not holding.** The faction is a
> proposition plus commitments; the territory is a containment node; **the holding is a third object, an
> edge between them.** Every cheaper repair — a `territory` field on the faction, a `ruler` field on the
> node — collapses the two objects Jordan just separated. `Tenure` is the only shape on the table that
> preserves the distinction, and it preserves it by being an edge rather than a field on either end.

**Then, with NO new verb — `confer` and `revoke` are already in `remit.acts` at `:423`:**

| subject → object | `confer` | `revoke` | closes |
|---|---|---|---|
| **Person → Office** | appointment | dismissal | **shipped, unchanged** (§4.4, §4.5) |
| **Person → Site** | **enfeoffment** | **confiscation** | **A10** — `holdings` stops being dead state; property moves by an act |
| **Faction → Node** | **a Duchy holding its Territory; annexation is that tenure changing hands** | **secession** | **A12** — transition 9b-ii |
| *(Person → Faction)* | — | — | **NOT `Tenure`. It is `commit`, and it stays separate** (§1.3 `:130`) |

**It also unifies two of the three edges the document already spells separately** — `Holding :=
(person, office, since, conferrer)` at `:367` and the hearth's succession pointer at `:302`/`:337`, the
latter becoming *tenure of a site transmitted on death* rather than a bespoke stake. **§4.2 `:336`
already files `Holding` and commitment edges in one table cell**, which is the tree signalling that the
edge shape is general; this takes the signal and declines the over-generalisation.

**And it makes annexation what it historically was.** Not a war subsystem and not border-painting: **a
conferral performed by a named person exercising a remit, public and witnessed like every act by remit
(§4.4 `:442`), whose subject then either complies or does not — through §9.2's shipped compliance
contest** (`contest(container, prize = compliance-here, claimants = {enforcement, resistance})`,
`:1141`). A Duchy annexed on paper and disobedient in fact is the ordinary output of a mechanism the
design already ships, and §9.3's thirty-five-executor logic applies to it unchanged. **No new resolver,
no new object, no war layer.** And it composes exactly with the half the design already gets right: the
Kingdom wins the Duchy's **people** by `commit` (§1.3's merger, transition 9b-i) and its **ground** by
`Tenure` (9b-ii), and **those two can come apart** — which is every disputed succession in the setting.

**Why rank 2.** It closes both limbs of the merged A10 · A12 and two of Jordan's twelve transitions; it
is the only change that gives **power a material referent**, since a faction that holds nothing cannot
be strong in any sense the world can see; and it is a precondition of rank 1 being cheap — `mint` on a
Node and `mint` on a Site both need somewhere for *who holds this* to live, and `Tenure` is that place.

⚠ **Its scope was reduced once during this review and the reduction is recorded.** It was first argued
on `Tenure` also absorbing `commit` and re-parenting the containment tree. **Both are withdrawn**:
membership is not holding, and re-parenting is moot because the tree is geography. **The primitive
survived the correction with a smaller job and a better justification**, which is the outcome to prefer.

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

**Why rank 5.** It is the **largest subtraction available** after `Tenure`: three capacity-like objects
become one
`Allowance(owner, period, size)` and one cap. It **restores §8.4's convener politics**, which is currently
arithmetically impossible and is the best political argument in the document. It **answers D-2 — the
design's self-declared largest open ruling — from architecture rather than escalating it**, which is
`CLAUDE.md` §0's fifth test applied exactly as written. It **prices D-16's cohort exploit out of
existence** rather than forbidding it. And it makes rank 1's `mint` cost sayable, because there is one
budget to charge it against.

### Rank 6 · A NEED IS A CLAIM  *(A5)*

**The change.** Mint needs at P2 as firsthand claims in the person's own ledger, source
`firsthand(body)`; delete the category *need* from §4.2's Nobody row and from §2's prose.

**Why rank 6.** It is the only change that repairs a **structural impossibility** rather than a wrong
value: today there is no legal path from the design's central motivational input to the function that
consumes it, and every act in the game runs through that function. It is also a **subtraction** — one
fewer kind of thing in the design — and it buys hunger as a pleadable ground at a sitting for free. It
ranks below the five above only because the design has been written *as if* the channel existed, so it
changes fewer downstream sentences than the two above.

### Rank 7 · COMMUTATIVITY ON THE FIELD, NOT THE ACT  *(B1)*

**The change.** Declare `condition` additive-alter and succession pointers exclusive-alter on the schema;
§6.4's conflict rule gains the word *non-commutative* and loses nothing else.

**Why rank 7.** §10 — one of the four enlargements, and the one carrying the design's best second-order
behaviour — **does not work at all** as the two sections are written, and the fix is one word on a field
definition rather than a case in the resolver. It ranks here rather than higher because it repairs one
enlargement, where ranks 1–4 repair the substrate. It is also a **precondition of rank 1**: `mint` and
`efface` need the same commutativity question answered (two people founding the same settlement conflict;
two people building different houses do not), and answering it on the field answers it for all five modes
at once.

### Rank 8 · EVICTION ON CLOCK QUANTITIES ONLY, AND P7's WRITE LICENCE STATED  *(B6)*

**The change.** Rank eviction by `confidence_live × recency` only; state P7's write class in §6.3.

**Why rank 8.** It is a **subtraction of a term** that saves the best paragraph in the document from
being false about its own worked example, and it removes a decider-free channel that runs on a social
quantity — which §10.6 condition 1 forbids in general and §13.2's four-item list does not license. It
ranks below the seven above because the damage is silent and slow rather than structural: the design still
runs, it just quietly converts motivated retrieval into motivated amnesia over a few seasons. **That
silence is exactly why it must be fixed before anything executes**, because once it does execute nobody
will see it happening.

### Rank 9 · THE THREE ONE-LINE MECHANISM REPAIRS  *(B3, B4, B5)*

**The changes.** Delete §5.2's `if R <= 1: return 0` branch (B3). Add
`precondition: stores(hearth(giver)) ≥ amount` to `transfer` (B4). Give restoration the mirrored form
`Δ = + (1 − condition) × f(degree) × share` (B5).

**Why rank 9.** Three small, independent, high-confidence fixes with no interactions — a **deletion**, a
one-line addition, and one formula that already had a shape waiting for it. Together they restore the
Costed Success band at the low end the design says is right, stop `transfer` minting food, and give the
restoration faction something it can actually achieve. They rank here only because each is local; none
changes how anything else is written.

### Rank 10 · THE TWO TYPING UNIFICATIONS  *(C2, C1)*

**The changes.** `Assertion = (subject, predicate, value, when)`, with `Claim` and `Proposition` as
extensions (C2). Claimants are always a set of persons with a stake (C1).

**Why rank 10.** Both remove a duplicated rule, which is §0 `:21`'s own definition of a defect in this
document, and both are cheap. C2 additionally makes rank 1 cheaper — `mint` on an Assertion covers both a
firsthand claim and a founding proposition, so the primitive gets one instance instead of two. They rank
last because nothing is currently *wrong* because of them; they are the difference between a design that
will stay coherent under extension and one that will grow branches.

**What is deliberately not in the ranking, because it is AUTHORING rather than a change.** Three items
are large and are not rankable, because nobody can rank the cost of writing something that does not
exist yet:

1. **§4.3's closed predicate vocabulary (C3)** — the largest implementability gap in the document, and
   the layer every other mechanism reads through. It should be the first thing authored after the ten
   above are applied, and §17.1 `:1881` should stop listing it as settled until it is.
2. **The investigative verb (§2.11, A11)** — one paragraph, using only shipped machinery, that turns the
   design's best layer into its most-wanted seat. **Cheapest large win in the document.**
3. **`Venue`'s seventeen unvalued parameters (§5.2)** — fourteen of which appear exactly once each, in
   the tuple, and never again.

---


---

## §7 · WHAT THIS REVIEW DID NOT DO

Stated so that nobody cites this file as more than it is.

1. **Nothing executed.** No simulation, no test, no measurement, no corpus re-scoring, no probe of any
   kind. Under `CLAUDE.md` §0.2 nothing here is done, and the subject document does not run either — so
   **every finding is an argument against text**, and every fix is a proposed edit whose consequences are
   reasoned, not observed. Where a finding says a mechanism cannot work, the honest reading is *the
   document as written does not describe a mechanism that works*, not *a program failed*.
2. **It is one reader.** The relay's structural independence is real — this pass never saw the agonist's
   reasoning, only its output — but independence is not plurality. Twenty-eight findings by one reader
   with one set of priors is a sample of one, and the three findings this pass had to correct downward
   during re-verification (§0) are the measured rate at which a filed finding turns out to be
   overstated: **three in twenty-eight, all in the direction of over-claiming.** Apply that prior to what
   is left.
3. **Docs 06 and 12 of #342 remain unverified by the fact base, and this review inherits that.** The
   subject document states it at §15.18 `:1846-1851`: `09_citation_ledger.md`'s own coverage note reads
   *"Not covered: `06_down_stroke.md` and `12_coercion_and_force.md` beyond grep hits"*. Doc 06 carries
   §9, which §5.3 rates as one of the design's best objects; doc 12 carries the coin hole, the watch
   naming ruling and §15.17's `burn` inheritance. **This review read both directly where it cited them
   and re-verified nothing else in either.**
4. **No arc corpus and no NPC-season matrix was re-run.** The testing exercise that produced the four
   enlargements is upstream of this file and was not re-examined. §15.9 and §15.10's warnings about that
   instrument — that it detects **absence, not failure**, and that its closure-axis count is not citable
   in its original form — stand unaudited here.
5. **The findings are against the terminal document only.** `10_SUPERSEDING.md` is 2,017 lines of a
   ~21,000-line suite. #342's seventeen documents were read only where cited. `00_THE_SHAPE.md`, the
   three review files and the NERS audit were read for context and were **not** reviewed. A defect that
   exists only in a superseded document is not a defect and is not reported.
6. **The three deferred subsystems were not read at all.** Mass battle, personal combat and social
   contest are out of scope by Jordan's ruling, and nothing here should be taken as a statement about
   them — including §5.3's genre table, which maps only the seats the seasonal loop is responsible for.
7. **The ten changes in §6 were not checked exhaustively for interaction with each other.** They are
   ranked individually and argued individually. Four interactions are named where they were noticed —
   `Tenure` is a precondition of `mint` on a Node (rank 2), commutativity is a precondition of `mint`
   conflicting correctly (rank 7), `Allowance` is what makes `mint`'s cost sayable (rank 5), and the
   `Assertion` base type makes `mint` on a claim and on a proposition one instance (rank 10) — **but
   nobody enumerated the pairs. There may be more, and finding them is the next round's work, not this
   one's.**
