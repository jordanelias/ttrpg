# THROUGHLINES OF THE 2026-08-31 SESSION — the design and its code shape

## Status: PROPOSED (2026-08-31). Ten throughlines drawn from an adversarial review of a merged design
## PR and the rebuild that followed it. **Nothing in this session executed.** No simulation was run, no
## test was written, no number was measured, no engine behaviour was observed. Every claim below is an
## argument about text, and `CLAUDE.md` §0.2 applies without exception: **done means it runs, and none
## of this runs.** Where a section says a mechanism works, that is a claim about what a document says.

---

## §0.0 · CITATION CONVENTION, AND WHY IT IS NOT THE SUITE'S OWN

| form | resolves to |
|---|---|
| `SUP:NNN` | `proposals/2026-08-31-ideal/10_SUPERSEDING.md` — the reviewed design, 2,017 lines |
| `REV:NNN` | `proposals/2026-08-31-ideal/20_FABLE5_ADVERSARIAL_REVIEW.md` — the review, 1,823 lines |
| `ARCH:NNN` | `proposals/2026-08-31-ideal-v2/01_ARCHITECTURE.md` |
| `LOOP:NNN` | `proposals/2026-08-31-ideal-v2/02_THE_SEASON_LOOP.md` |
| `COMP:NNN` | `proposals/2026-08-31-ideal-v2/03_COMPENDIUM.md` |
| `PORT:NNN` | `proposals/2026-08-31-ideal-v2/04_GODOT_IMPLEMENTABILITY.md` |
| `KTI:NNN` | `proposals/2026-08-29-valoria-from-scratch/03_knowledge_telling_investigation.md` |
| `SWEEP` · `PART` · `F6` · `REVIS` | `proposals/_session_provenance/2026-08-31-fable5-review/v2/{EVENTS_AND_SWEEP,THE_PARTITION,F6_RULED,REVISIONS}.md` |

⚠ **This document deliberately does not use the v2 suite's own `NN:LLL` shorthand, because that
shorthand is ambiguous.** `ARCH:37`, `LOOP:24` and `COMP:34` define `NN:LLL` as line LLL of
`proposals/2026-08-29-valoria-from-scratch/NN_*.md`. `PORT:40` defines `01:NNN · 02:NNN · 03:NNN` as
*"line NNN of the numbered document in **this** directory."* **The same token names different documents
depending on which of the five files you are reading, and neither key mentions the other.** The
consequences are live and are recorded at §10 and §13.

---

## §0 · WHAT THE SESSION WAS, AND WHAT IT PRODUCED

An adversarial review of a merged design PR, then a rebuild of the design from that review, audited by
five parallel runners, a keys audit and a corpus sweep.

**Stage 1 — the review.** A read-only antagonist pass over `SUP` (2,017 lines), the terminal deliverable
of PR #343, itself the product of two prior agonist→antagonist rounds logged at `SUP` §17.5. It filed
34 findings and carried 33 (`REV:44`; `_session_provenance/2026-08-31-fable5-review/MANIFEST.md:24`),
across four tiers, and closed with a ranked list of ten changes.

**Stage 2 — the review reviewed.** A structurally independent antagonist broke **four** of its claims,
including the one it had called #1 (`REV:46-56`). All four were absence claims, and the review's own
re-verification had caught none of them. Correction provenance, from the same manifest at `:22-23`:
**2 from Jordan · 4 from the independent critic · 7 from the reviewer's own re-check** — 13 corrections
across 12 findings, and the seven self-caught ones were all counts, scopes and wordings.

**Stage 3 — the rebuild.** A synthesis brief (`ARCH_CORE.md`, 189 lines) was put to five parallel
runners on separate axes. It did not survive. Dispositions at `REVIS:4`, `:78`, `:147`, `:211`, `:298`:

| runner | axis | FATAL | MAJOR | MINOR | rebutted |
|---|---|---|---|---|---|
| 3 | scope | 2 | 11 | 6 | 0 |
| 1 | fidelity | 3 | 8 | 10 | 0 |
| 2 | factuality | 1 | 5 | 4 (+2 obs) | 0 |
| 5 | correctness | 6 | 11 | 7 | 0 |
| 4 | keys | 982-line audit · 38 objects · 20 reference edges | | | 0 |

**12 FATAL · 35 MAJOR · 27 MINOR, all accepted, none rebutted** (`REVIS:346`) — and the arithmetic
checks. The deliverable was then written from the dispositions rather than from the brief.

**Stage 4 — the rulings.** Jordan resolved three forks the audits could not: the world is in **flux**
(`F6:2-6`), state changes partition **on their subject** (`PART:2-6`), and creation and deletion are
state changes.

**Stage 5 — the sweep.** A corpus sweep over `proposals/`, commissioned only after Jordan twice pointed
at material nobody had read. It found four already-designed mechanisms the suite had presented as new
or missing.

**What shipped:** five documents at `proposals/2026-08-31-ideal-v2/` — 161 + 2,186 + 1,205 + 949 + 941
= **5,442 lines** — plus the provenance directory, committed with its errors intact.

**What follows is about the design.** The method observations are compressed into §13, deliberately.

---

## §1 · EXISTENCE WAS THE REGISTER NO CHARACTER TOUCHED

**The claim.** The design could change the state of everything and could barely change **which things
exist**; in a design whose thesis is that every active decision is a character's, no character could
bring a Site, a Container or an Office into the world or take one out of it.

**The evidence.** `REV:180-189` gives a five-item list — the operations in 2,017 lines that change
existence — and each verifies against the subject:

| # | operation | `SUP` | driver |
|---|---|---|---|
| 1 | death | `:648`, P1 SETTLE, *"metabolism and nature only"* | decider-free |
| 2 | de-individuation | `:654`, P7; `:209` | decider-free |
| 3 | eviction of a claim | `:654`, *"ledgers evict lowest salience"* | decider-free |
| 4 | individuation | `:654`; `:203-204`, fires when *"an event names one of its members"* | decider-free |
| 5 | holdings passing on death | `:304-307`, the hearth's succession pointer | decider-free, fired by (1) |

Four of the five are subtractive; **individuation is the only additive operation, and nothing a
character does fires it.** `holdings` occurs exactly twice in `SUP` (`:307`, `:352`), both descriptive:
it is state no act reads, writes or moves.

⚠ **Two corrections to the form this claim is usually stated in, both applied here.**

**First, the list is about existence and nothing else.** `REV:176-177` retitles it in place: *"this is the
list of operations that change **EXISTENCE**. It is not a list about tenure."* The tenure version of the
claim was broken four ways at `REV:156-166` — `transfer` moves `stores` by an act (`SUP:1425-1427`),
`confer`/`revoke` change office tenure (`SUP:423`), Admission changes a person's address
(`SUP:311-313`), and tellings create claims constantly. The surviving sentence is `REV:170-171`, and it
is the one to quote:

> **No act creates or destroys a Site, a Container or an Office, and no tenure relation exists over
> Sites or Nodes.**

**Second, there is a sixth existence-changing operation and it is not decider-free.** `ARCH:963` —
*"**A telling deposits claims into ledgers** by presence and channel"* — and a telling is a person's
choice. Claims come into existence by decision. **So both universals fail as stated**, and the proof
holds only when scoped to Sites, Containers and Offices. Stated that way it is still the finding, and
it is now checkable.

**The mechanism.** Existence changes were filed under *metabolism* — the phase where nature acts. The
design placed every creation and destruction it had in P1 and P7, the two decider-free phases, and then
never asked whether the acts class needed any. The gap is not a forgotten rule; it is a **register that
was never opened**, which is why seven separate findings (`REV:272-273`: A1, A2, A3, A6, A9, A10·A12,
A11) turned out to be one finding with seven faces.

**The falsifier.** A single act in `SUP` whose declared effect brings a Site, Container or Office into
being or removes one. `REV:144` credits `alter` (`SUP:1261`), `exclude` (`SUP:1292`) and inherited
`burn` (`SUP:1305`) on the *destroyed* limb — but `SUP:689` defines `exclude` as a conflict mode
(*"mode ∈ `{read, alter, exclude}`"*), and `SUP:1235` has acts touching `condition` *"through the
existing `alter` and `exclude` modes."* **A character can drive a site's condition to zero; the site
still exists.** That is a state change, not an existence change, and the distinction is the same one
§4's plague case turns on.

**What it means for the code.** Existence and state are different registers and the code must say so.
`ARCH:361-362` does: `StateChange := (subject, mode, driver, field?, delta?, spec?)` with
`mode ∈ mint | alter | efface`. **The gap closes by giving the mode set a creation and a deletion
member, not by authoring a birth system, a construction system and a founding system** — which is the
argument `ARCH:1861` makes against every alternative.

---

## §2 · THERE WAS ONE EDGE PRIMITIVE, SPELLED THREE TIMES

**The claim.** `Holding`, the commitment edge and the hearth's succession pointer are one shape; naming
it once produces the tenure relation whose absence §1 records.

**The evidence.** All three spellings are in the subject:

- `SUP:367` — `Holding := (person, office, since, conferrer)`, *"an edge on the **person**"*
- `SUP:130` — *"One membership operation: `commit(person, faction, Δdegree)`"*
- `SUP:304` — the hearth *"owns transmission across time: the **larder**, the **succession pointer**"*

Generalised at `ARCH:253`:

> `Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?, payload?)`

**Nine fields, seven kinds** (`ARCH:280`). `confer` and `revoke` are already in `remit.acts`
(`SUP:421-424`, a *"closed set of five"*: **issue · determine · confer/revoke · dispatch · convene**),
so four operations the design could not express fall out of a naming: enfeoffment and confiscation are
`confer`/`revoke` on `hold` over a Site, annexation is `confer` on `hold` over a Rung (`ARCH:325-326`).

⚠ **`until?` is the field that matters, and it is why this is a design result rather than a tidy-up.**
`ARCH:265` — *"**`until?` is what makes a destroyed tenure a fact.** A revoked tenure is a historical
claim subject."* Without it, the record carrying every disputable political fact could not itself be
disputed. `COMP:441` states the consequence for the prior design: *"nothing pointed at a Tenure in the
prior design, which is why it could not be disputed."* **The design's central thesis — that politics is
argument over claims — did not reach the object the politics is made of.**

⚠ **The "no new verb" generalisation does not survive, and is withdrawn here.** `ARCH:481` —
*"**`remit.acts` is NOT the act vocabulary.** It is the closed five an office's remit makes eligible
somewhere they otherwise are not"* — and `ARCH:2044` records *"at least nine verbs the design itself
names"* outside that set. The four named tenure operations survive as `confer`/`revoke`; the claim that
the design needed no new verb anywhere does not. What is closed is the **mode** set at three
(`ARCH:484-485`), and that is the closure doing the work.

**The mechanism.** Three spellings of one relation, each filed in the section of the document that
needed it, is what a design produces when it grows section by section and nothing indexes objects
across sections. `SUP` §4.2's ownership table already filed two of them in one cell. **The keys audit
found this by asking what has identity, not by reading for correctness** — which is why five other
audits that read for correctness missed it.

**The falsifier.** A property of any one of the three spellings that the other two cannot carry.
`ARCH:328-329` names the near miss and refuses it: *"Membership is not holding: `commit` and `hold` are
different kinds and stay different kinds"* — one relation, distinct kinds, not a collapse.

**What it means for the code.** One table, seven kind values, declared cardinality per kind, one id.
`PORT:134` types it *"`row` in a `TenureStore`"* and notes **N is the largest object count in the
design** — so the consolidation is also the difference between one hot store and three.

---

## §3 · POWER IS A QUERY, NEVER A FIELD

**The claim.** Nothing stores control. A faction is a proposition plus the `commit` edges pointing at
it; leadership, presence, footprint and sovereignty are computed on demand; scale is derived and gates
nothing.

**The evidence.** `ARCH:540-559` is a twenty-row query table with a side column, and `ARCH:561` states
the result:

> **Nothing stores an aggregate. Every one of these is a query, and that is why power is not static.**

`ARCH:540` — `faction(prop) : Proposition → Set[Tenure]`, replacing *"a stored faction object"*.
`ARCH:545` — `sovereign_fraction(root) : Rung → [0,1]`, replacing *"stored control"*. `ARCH:559` —
`regard(p, c)`, replacing *"a stored reputation"*.

⚠ **The query must take an OBSERVER, and the design records what happens when it does not.**
`ARCH:541` — `leaders(prop, c, observer) : (Proposition, Rung, Person) → List[Person]`, side **person**.
`ARCH:535-536` records the failure that forced the observer in: flattening the side column *"typed
`principals` as a **true-profile read, which nobody may perform**"* (`SUP:124-128`) — the same rule that
forbids reading a faction's real membership.

⚠ **"Deposition needs no verb" is true of faction leadership and false of office, and the same
document says both.** `ARCH:327` — *"Deposition is **not an operation at all** — it is `leaders(prop,
rung)` returning somebody else."* But losing an office is `revoke` on a `hold` Tenure (`ARCH:325-326`),
which is a verb with a conferrer and a witness. **Two meanings of one word, two hundred lines apart,
inside the document that states §10's rule about names.** The headline is therefore scoped: *leadership
of a faction* needs no verb, because leadership of a faction is not stored.

⚠ **`leaders` has three spellings in the deliverable** — `leaders(prop, c, observer)` at `ARCH:541`,
the observer-less `leaders(prop, rung)` at `ARCH:327`, and a third in prose. `ARCH:541` is the one with
the side column behind it; the others are defects in the deliverable, recorded here rather than
smoothed over.

⚠ **"Sovereignty is a reachability query" overstates it.** `ARCH:566-569` records
`sovereign_fraction`'s `root` as a Rung the design declares no invariant for, and rules the function
**partial** — total only over the office-rooted subgraph, with *"callers must handle root-plurality and
a unique root is a political condition, not an invariant."*

**The mechanism.** Every stored aggregate is a second source of truth that some act must remember to
update. Deleting the store deletes the update obligation, and the deletion is what makes *"power is
something that happens"* mechanical rather than aspirational.

**The falsifier.** Any decision procedure that reads a stored control value. The design's own exposure
is `ARCH:566-569`'s partiality: where the root is contested, the query has no total answer, and that is
conceded rather than hidden.

**What it means for the code.** Twenty pure functions with a declared side, no faction table, no
leadership field, no scale enum. The cost is recomputation; §10 records what buys it back.

---

## §4 · THE PARTITION — THE SUBJECT OF A STATE CHANGE DECIDES ITS DRIVER

**The claim, ruled by Jordan** (`PART:2-6`, verbatim):

> **Partition every state change by its SUBJECT.** If the subject is **peninsular human society** —
> polities, institutions, offices, organizations, occupations, religion, settlements, marriage — the
> change is driven by **a character's choice**. If it is anything else — weather, the non-peninsular,
> tears in the metaphysical substrate — it is **an event acting on the world**.

**The evidence.** Restated as the design's own rule at `ARCH:1337-1341`, with the closure that matters:
*"**No licence is needed beyond the partition's second row, and no fifth channel can be smuggled in,
because there is no list to extend.**"*

**What it replaced.** `SUP:1633-1643` licensed *"these four, and only these four"* decider-free
channels **with no membership test** (`PART:17-20`). A list you cannot test is a list you cannot check
or extend.

⚠ **One of the three failures usually cited for that list is a retracted finding, and is restated
here.** *"Matter events were licensed with nothing generating one"* was the review's A7, and the
independent antagonist broke it: `SUP:1346-1349` names the storm as *"a bad `season_factor` roll
closing the channel **for a season**, temporary by construction."* **A generator existed.** The true
statement is narrower and is a better account of the defect: **the licence named no generator in its
own section, and the generator that existed was two hundred lines away and unlinked.** The other two
failures stand — `wear` was unwritable (`SUP:1350-1354`, admitted in place), and an authored event deck
had no home.

**The no-fallback refinement is the partition's soundest limb.** `SUP:1599-1601` reads *"**THERE IS NO
FALLBACK.** If no person acts, the thing does not occur"*, which is false of a world with weather. `PART:25-28` scopes it:
**if no person acts, no SOCIAL thing occurs.** Fully instrumented at `LOOP:780-787`, which refuses an
automatic per-Rung compliance contest on exactly that ground and rules: *"**Where neither side acts,
nothing happens, and the dispensation is simply unobserved.**"*

**The extension: creation and deletion are state changes.** `ARCH:334` records that an earlier version
made `mint`/`efface` *"**modes of an Act**, so only a character could"* create — and the partition moves
them onto `StateChange` (`ARCH:361-362`), giving `ARCH:376-378`:

> **THE BOTTOM-LEFT CELL IS THE CAPABILITY THE ARCHITECTURE DID NOT HAVE: THE WORLD CAN CREATE AND
> DESTROY THINGS.** A landslide exposes a seam nobody knew was there, a faction forms around working
> it, and no character decided the seam should exist.

**The worked case that shows the rule doing work**, `ARCH:489-494`: a plague **kills bodies** — a
non-social subject, so an event `efface`s persons, legal — but *"plague cannot efface"* a settlement,
so **the village empties and "still legally exists" until some office strikes it from the roll.**

⚠ **The partition is decidable given a named subject, and the deliverable concedes a mixed case.**
`ARCH:514-517`: *"A plague is biology but it empties institutions; a famine is weather times tending; a
heresy is religion. **The rule decides each by its subject — event · both · choice**."* **"Both" is not
a partition.** The strong claim and the concession must be stated together: the rule is decidable where
the subject is single, it names a mixed class where the subject is not, and the plague case is decided
by authored fiat about what counts as the subject rather than by the predicate alone.

⚠ **`efface` is not cleared.** `ARCH:1859` — *"**`mint` is CLEAR; `efface` is NOT CLEARED and the
widening is stated.** `efface` on a Rung, Office, Person or Site extends the uncleared discrete limb"* —
the same unbounded-destruction limit `SUP:1302-1306` already admitted for arson. **The extension
inherits an open hole rather than closing one.**

**The falsifier.** A state change whose subject is single and unambiguous and which the rule
nevertheless assigns to the wrong driver — or a fifth channel that has to be smuggled back in.

**What it means for the code.** One `StateChange` type, one `driver` field, and a subject predicate. No
channel registry, no licence table, and no place for a fifth channel to be added.

---

## §5 · THE WORLD'S TRAJECTORY IS AN OUTPUT, NOT A CONSTANT

**The claim, ruled by Jordan** (`F6:2-6`): the world is *"neither dying nor misunderstood — rather, it
is in a state of flux. If the world is not tended to by anyone, it will die. If it is tended to by
everyone, it will thrive."*

**The evidence.** `ARCH:1360`:

> `condition(site) ← clamp( condition(site) + Σ (this season's resolved deltas) − wear(kind(site)), 0, 1 )`

`ARCH:1362` — **`wear` is a per-site-kind constant in the same units as `condition`**, a fraction of
full condition per season. Not weather, not a multiplier, not a roll. `ARCH:1386-1387` gives the three
cases, and the first is the ruling made mechanical:

| tending | arithmetic | outcome |
|---|---|---|
| nobody | `Σ acts = 0`; condition falls by `wear` every season | it crosses a band floor, verbs leave, **the world dies and no person did it** |
| everyone | `Σ restoration ≥ wear` | it holds or climbs — it thrives |

**Why five audits could not dissolve this fork.** The fork as filed was *a real decline the player must
arrest* versus *a fact everyone reports wrongly* (`F6:9-14`). Both branches fix the direction — one at
negative, one at zero with the variance moved into reporting. **Jordan's answer makes the direction an
output.** The missing option was **a sign, not a parameter**, and no amount of optimising inside the
frame produces it.

⚠ **The prior design admitted the cost of the form it had chosen**, `SUP:1350-1354`: *"A fuse that is
act-only cannot model a site that decays with nobody touching it."* Under act-only, an untended site
does not die; it **freezes**. The ruling made that cost unacceptable, because untended decay *is* the
world model.

**And it converts the act economy into the load-bearing scarcity of the game.** `ARCH:1391` — *"under
an act-only fuse restoration was pure gain and neglect was free. **Under `wear`, maintenance is a
permanent tax and neglect has a price.**"* So *how many person-seasons does this harbour cost to keep
open* becomes a real contested quantity, drawn from the one-act-per-person budget of §9.

**The falsifier.** `ARCH:1711-1712` states it against itself: **the ratio of `wear` to a restoration
act's effect sets the world's entire difficulty curve, and no number in this design has been
measured.** Too high and the world dies whatever anyone does; too low and tending is decoration. **The
ruling is unfalsifiable until that ratio is chosen and run**, and nothing in this session ran it.

**What it means for the code.** One constant per site kind, in the parameter table where code reads it
(`CLAUDE.md` §0.05), one row each. `F6:105` calls the net cost *"one constant, zero objects"* — and
`ARCH:1959-1968` actually walks `wear` against the refusal rows rather than glossing them, including
row 12's ban on a scheduled recovery tick, which clears because `wear` moves matter and row 12 governs
standing.

---

## §6 · BELIEF AND TRUTH WERE TWO FUNCTIONS SHARING ONE NAME

**The claim.** `choose` takes no `World`, yet a person must know their options, and the option set reads
hidden world state. The resolution is a split of one function into two, not a new primitive.

**The evidence.** `ARCH:764` names the split; `ARCH:770-772` states it:

> - **`verbs(site, c)` is WORLD TRUTH, read only by `resolve`.**
> - **`opening_set(person, view)` is BELIEF, computed inside `choose` from the person's own ledger,
>   stance, capability, `Sensation`, and the remits they hold.**

Both appear in the query table with sides declared — `ARCH:547`, `verbs`, resolver, *"world truth about
what is possible"*; `ARCH:548`, `opening_set`, person.

**The consequence is better fiction than the alternative**, `ARCH:774-778`: *"A person may therefore
attempt a verb the world has already removed, and discover the harbour silted"* — and the design had
already argued for it, *"the people who notice first are the ones whose practice used that verb."*
`ARCH:440-441` reaches the same place from the event side: a person who spent his season repairing a
harbour a storm had already destroyed **finds it destroyed**.

⚠ **`opening_set` does not work from a ledger alone.** It reads stance, capability, `Sensation` and
remits (`ARCH:771-772`). The cleaner-sounding version of this guarantee is stronger than the design
claims, and the difference is the whole of the next paragraph.

⚠ **`opening_set` returns CANDIDATES, not Acts** (`ARCH:784`) — the prior brief typed it
`Person → [Act]`, which made the option set an authored list rather than a computed one.

### `Sensation` — the one addition the record calls forced

**The enforcement mechanism had no channel for its own central input.** `ARCH:685` types the decision
function `choose : (Person, View, Sensation) -> Act # NO World, ever` — and a person's motive for
acting is need, which is a fact about the world. With no `World` and no channel, **need could not
reach the decision**.

`ARCH:728` states its status plainly: *"**`Sensation` IS THIS DOCUMENT'S PROPOSAL against a problem the
review left open.**"* `ARCH:742` — `Sensation := (subsistence, standing)`, **exactly two scalars**.
`ARCH:755` — *"**A Sensation is UN-NAMEABLE, THEREFORE UNDISPUTABLE.** No person can hold a claim about
another"* — which is what keeps it out of the epistemic layer and out of the claim vocabulary.

**It is a value type, not a store**, and that is the design decision. `PORT:148` types it **`Vector2`**,
*"a built-in value type"*, and calls it **the strongest recommendation in the table**; `PORT:166` warns
that *"a `class Sensation extends RefCounted` throws this away"*, because the moment it is an object it
acquires identity, aliasing and a lifetime.

**The falsifier.** Any mechanism that needs to name, cite, conceal or dispute a `Sensation`. It survived
four attacks in the record and is the only addition of the session the record calls forced rather than
reinvented; §13 explains why that distinction is the one worth tracking.

---

## §7 · THE EPISTEMIC LAYER WAS ALREADY BUILT, AND ITS PROBLEM WAS NOT INVENTION

**The claim.** The knowledge layer shipped in the prior suite with mechanism the session twice believed
absent; what it lacked was **enough happening to disagree about**.

**The evidence** — all in one 980-line document, `KTI`:

| what shipped | where |
|---|---|
| a **closed fourteen-form** predicate vocabulary, each form with shape and use | `KTI:64-79`; count stated `KTI:81`, restated `KTI:118` |
| `relevance(c, q)` defined in full — three cases, `1.0` / `0.3` / `0` | `KTI:342-344` |
| six investigation acts, each with pool, product and cost/risk | `KTI:526-531` — examine · interview · research · surveil · reconstruct · Thread-Read |
| the one derived query, `trace(person, claim)`, *"a view, not a store"* | `KTI:538-540` |

`KTI:519-522` opens the act table with *"Every one is available to any person; the substrate's rule
that action eligibility never consults office binds here without exception"* — the detective seat is not
a seat, it is six acts anyone may take. `KTI:533-536` refuses the obvious apparatus: *"There is no clue
counter, no case object, no investigation skill, and no threshold anyone sets."*

⚠ **The session twice claimed parts of this layer did not exist. Neither claim is simply false, and the
precise account is more useful than the blunt one.**

- **The vocabulary claim was correctly scoped and is true as scoped.** `REV:1215` — *"**The document**
  names one form in 2,017 lines"* — and `REV:14-17` makes a bare `:NNN` a line of `SUP`. **What is
  wrong is the fix**: `REV:1226-1229` proposes authoring *"a value-at-a-subject form, a location form, a
  holding form, a compliance form, an obligation form"* — forms `KTI:64-79` already ships as `QUANTITY`,
  `LOCATED`, `HOLDS` and others, inside a declared set of fourteen. **A correctly-scoped absence claim
  whose repair reinvents the corpus.**
- **The `relevance` claim exists in two versions and the scoped one survives.** Unscoped, at
  `REVIS:195`, banked under *"CONFIRMED — the load-bearing verifications"*: *"`relevance(c, q)` is
  **never defined**"* — false against `KTI:342-344`. Scoped, at `REVIS:295-296`: undefined **at
  eviction**, because `relevance` takes a question `q` and P7's eviction has none in scope. **`KTI` does
  not answer that**, and a second runner ruled it *"correct, and an improvement on the review."*

⚠ **So "already right" is too generous, and "already built" is the accurate word.** Two mechanism
defects in that layer were accepted: `relevance(c,q)` undefined at eviction, and stance-ranked eviction
turning motivated retrieval into motivated deletion. And the layer admits its own closure failure at
`KTI:81-89`: *"the count was twelve until this document was audited against its own use… **leaving the
count at twelve while using fourteen was the defect.**"*

**The mechanism.** An epistemic layer is a machine for producing disagreement, and disagreement needs
facts to be about. The prior suite built the machine and gave it a world where little happened that
anyone could be wrong about. **Every enlargement this session kept — tenure, `wear`, the partition's
event half, minting — is a fact factory feeding it**, which is why the layer needed no new mechanism.

**The falsifier.** A mechanism the layer genuinely lacks that no amount of world-churn would supply.
The two accepted defects above are candidates and neither is about invention.

**What it means for the code.** Fourteen forms, three tables (collision, entailment, relevance; the
first two are |forms|² and sparse), authored once alongside the act list — `KTI:52-57`'s own argument,
and `KTI:91-93`: *"fourteen changes the table's dimension and changes nothing about who authors it or
when."*

---

## §8 · ENFORCEMENT BY OMISSION DEGRADES TO ENFORCEMENT BY CONVENTION IN THE TARGET LANGUAGE

**The claim.** *`choose` has no `World`* and *a consensus broadcast is a type error* are guarantees in
prose and **unenforceable in GDScript**.

**The evidence.** `PORT:78-79` — GDScript has *"no module system, no visibility modifier, no import
graph, and no way to make an identifier unreachable from a function body. Every autoload and every
`class_name` is a global identifier."* `PORT:244-245` quotes the design half-admitting it: *"nothing
enforces it structurally except the absence of a `World` in `choose`'s signature"* — *"that sentence is
the whole of the enforcement in Python and none of it in GDScript."*

**And the port's own skeleton already does the forbidden thing.** This is the best-instrumented claim in
this document, because it is code rather than prose about code:

- `godot/skeleton/engines/combat/modules/strike_module.gd:38,39,67,86,90,138` — a resolver module
  reaching the `GameState` autoload directly from inside its body.
- `godot/skeleton/engines/combat/modules/wound_module.gd:40,63,66` — the same.
- `PORT:283-284` — `godot/scene_tree_architecture.md:16` makes `GameState` an autoload holding *"all
  tracked state"*, and the strategy doc records the live tree's `Meta` autoload as *"the single state
  owner"*. **Both are the exact shape the rule below forbids.**

**And nothing else closes it** (`PORT:293-300`): threads do not sandbox, inner classes scope outward not
inward, and an accessor wrapper is refused by the design itself.

> **What survives is nearly as strong and must be stated as the weaker true thing** (`PORT:253-262`):
> **no live world state may be reachable by a global name** — no autoload, no `class_name` static, no
> `res://` path — and **every resolver-side query takes `World` as its explicit first parameter**, so
> calling one from inside `choose` fails at the call site for want of an argument.
> **Unreachable-by-name, not unwritable.**

⚠ **Every number attached to this claim in circulation is wrong, and they are corrected here.** The
Query table is `ARCH:540-559`: **20 rows — 16 resolver-side, 4 person-side** (the person rows are
`leaders`, `opening_set`, `occupation`, `estimated_profile`). `PORT:270` says *"resolver-side — 12 of
the 20 rows"* and *"person-side — 5 rows"*, which is wrong twice and does not sum to its own 20;
`PORT:899` repeats *"twelve signatures"*. **The correct statement: enforcement by omission goes from
the three top-level signatures, where it is already applied, to the twenty queries, of which sixteen
would take an explicit `World` first parameter.** A widely-repeated "23" is `3 + 20` and names nothing.

⚠ **And the citation `PORT` gives for that table mis-resolves under both of the suite's keys** —
`01:422-443` is the event-mint and conflict-rule section under `PORT`'s own key, and §5.2 Dispensation
under the other. The table is at `ARCH:538-559`. See §10.

**The mechanism.** A guarantee carried by a type system is a property of the program. A guarantee
carried by *the absence of a name in a signature* is a property of the source text, and it survives
translation only into a language that can make a name unreachable. **GDScript cannot**, so the
guarantee degrades to a convention — and a convention that is documented as a type rule is worse than a
documented convention, because it stops the next reader from checking.

**The falsifier.** A GDScript mechanism that makes an identifier unreachable from a function body.
`PORT:293-300` enumerates four candidates and refuses each.

**What it means for the code.** Sixteen signatures gain a first parameter, and one rule about the
autoload table — a decision `PORT:285` records as **still open** in the port spec, and which must now
be decided for this reason, *"which is not currently among the reasons on the table."*

---

## §9 · COHORTS MUST ACT, OR THE POLITICS GOES ELITE-ONLY BY CONSTRUCTION

**The claim.** A cohort is persons at coarse fidelity — **one type, not two** — and it acts. Replacing
it with a demographic envelope makes population *matter*, and matter does not act.

**The evidence.** The rebuild's brief deleted the cohort and the scope runner caught it. `REVIS:6-24`,
accepted in the strongest terms available: *"**COHORTS WERE DELETED. ACCEPT — this is the worst error
in the brief and it is mine.** I replaced the cohort with a demographic envelope and made population
**matter**. Matter does not act."* The consequence, in the same disposition: *"nobody outside the five
minting triggers — all notability triggers — chooses an act, commits to a proposition, or holds
anything… manufactures **elite-only politics by construction**… **including the 'dynamically generated'
replacements for collapsed royal ones**."*

The correction, at `REVIS:16-22` and carried into `ARCH:571-575`, is two objects where there had been
one word:

- **A cohort IS persons, at coarse fidelity** — one record, a weight, evaluated once, applied to all.
  **It acts, one act per season**, holds `commit` edges, carries stance, and can be petitioned, levied
  and roused.
- **A demographic envelope is the inflow reservoir only** — counts by age band for birth and death. It
  is matter, it does not act, and it is **not** the representation of the living population.

**And the design goes further than the summary usually does.** `ARCH:594`:

> `Person := (id, weight, marks, capability, stance, ledger, ties)     -- ONE tuple. weight >= 1`

**One tuple, one `class_name`, and no conversion operation** — individuation is a change of `weight`,
not a change of type. That is what makes the one-type rule mechanical rather than a promise.

### One act per person, at every rung

The word *act* was doing two jobs: **personal attention**, identically scarce for a Duke and a fisher,
and **institutional throughput**, which scales with the people an office employs. The design separates
them by moving the *pool* for an act-by-remit onto the establishment and leaving the *act* on the
holder (`SUP:434-437`; `ARCH:2046`, *"**D-2 is ruled**: one act per person or cohort, universally"*).

`ARCH:1084` — *"the King spends **one** act — `dispatch` — and thirty-five named people each spend"*
their own deciding what to do about it. `ARCH:1506` — *"a Duke's `dispatch` moves thirty-five seasons.
**Same allowance, incomparable reach.**"*

⚠ **The cohort exploit's self-pricing is an argument, not a result.** `REVIS:26-28` states the trade:
individuate to farm acts and you have *"eleven persons acting once each with eleven ledgers and eleven
stances toward you"* — each with the standing option to refuse. **Whether eleven refusals cost more
than an eleven-fold act multiplier gains is unmeasured**, and nothing in this session measured it.

**The mechanism.** The exploit is only priced *because the cohort was acting in the first place*
(`REVIS:28`). Delete the cohort and the pricing argument evaporates along with the politics.

**The falsifier.** A run in which individuating a cohort is dominant. It requires the act economy to
execute, and it has not.

**What it means for the code.** One `Person` type with a weight field, one act allowance keyed on the
record rather than on notability, and an envelope that is read at MATTER and never asked to decide.

---

## §10 · THE SHAPE THE PORT TAKES: BARRIERS, FIELDS, NAMES AND IDS

Four results that look unrelated and are one: **the port is a constraint the design must be authored
against, not a translation performed afterwards.**

### 10a · The loop is four global barriers plus one per-person pure map

`LOOP:31` — six steps, `CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS`, *"and nothing
else"*, with the legacy `P0…P7` (`SUP:641-654`) retired. `LOOP:96-104` — *"**Four barriers, six steps,
and why the counts differ**"*, because `CENSUS` runs after WITNESS's join and needs no join of its own.

**The shape was rediscovered independently and corrected from three barriers to four**, and the reason
`CENSUS` exists is a concurrency defect, not tidiness: `LOOP:938` — *"**De-individuation is
order-dependent, and the prior brief had it inside the per-person map.**"* `LOOP:143` records the same
for individuation, which *"mints a globally addressable object"*.

**What the shape buys is stated at `LOOP:1118`:** *"the per-person maps may run in any order | they
write nothing global — individuation and de-individuation moved to CENSUS, and ids need no
[allocator]."* **That licence is the design's parallelism**, and 10d is what pays for it.

### 10b · Commutativity is a property of the FIELD, not the act

`ARCH:445-447`, declared on the schema rather than decided in the resolver:

> **`additive`** — all writers apply, order-independent: `condition`, `stores`, envelope weights.
> **`exclusive`** — contested: a succession pointer, an office's remit, an address.
> **The default for an undeclared field is `exclusive`.**

With one clamp, stated once (`ARCH:449-451`): *"`additive` is order-independent **only under batching**.
`clamp` does not commute with addition at the bounds. **The resolver sums a season's act deltas per
field and applies the clamp once.**"* An event delta applied at the event barrier is strictly before all
of them and needs no commutativity argument at all.

**And without it the commons does not work at all** — `LOOP:578-582`: under the prior rule, *two acts
conflict iff they share an object and either mode is `exclude`, or both `alter` the same field*
(`SUP:689-691`), **all forty `alter` acts on a harbour conflict pairwise and route to a contest**, the
summation never happens, and the tragedy-of-the-commons shape the design exists to produce is
unreachable. **One word on a field definition replaces a case in the resolver, and the rule gets
shorter.**

### 10c · A name must clear the target engine and the local corpus

`ARCH:151` — *"**`Rung` is the name. `Node` and `Container` are BOTH refused**"*, and the second refusal
corrects the session's own first rename. `ARCH:155` — `Node` collides with Godot's scene-tree base
class. `ARCH:157` — `Container` **is also a Godot built-in**, the `Control`-derived base of
`VBoxContainer`. And `ARCH:159` gives the detail worth keeping:

> **`Node` failed loudly and at once, while `Container` surfaces as a confusing shadow of a UI type.**
> The rename made to fix a collision landed on a **worse** one.

`ARCH:524-531` is the second instance and it points the other way — `Derived` *"collides with this
repository's own vocabulary in the **opposite** sense"*, citing `references/glossary.md:75-82`.
**Confirmed at that file**: Health, Stamina, Coherence, Composure and Momentum are listed under
*Derived Character Stats* as **stored** per-character tracks. `Query` replaces it, being *"the word this
tree already uses for compute-on-demand"*.

⚠ **The third instance is in the deliverable, and nothing caught it.** `ARCH:37`, `LOOP:24` and
`COMP:34` define `NN:LLL` as line LLL of `proposals/2026-08-29-valoria-from-scratch/NN_*.md`.
**`PORT:40` defines `01:NNN · 02:NNN · 03:NNN` as *"the numbered document in this directory."*** The
same token names different documents in different files of one suite, and neither key mentions the
other. It has produced live mis-resolutions — `PORT:270`'s `01:422-443` (§8) and `PORT:771`'s
`03:441-446`, which cites the Tenure inverse-index row for a cycles claim whose home is `COMP:485-492`.

`ARCH:40-41` even ships a *"Namespace key — **read this before any cross-reference**"* warning that *"a
reader who does not hold this table will resolve half the citations in these three documents to the
wrong thing"* — and it governs finding-id families, scopes itself to *"these three documents"*, and does
not catch this. **The rule was stated and not applied inside the document stating it.**

### 10d · Ids, not pointers — right for a reason the design never states

`COMP:485-492` is a table of reference cycles, and `COMP:488` is the load-bearing row: `succeed ∘
contain`: Rung → Person → Rung is *"**yes, and it is the NORMAL case** — the heir lives in the hearth"*,
with the consequence that *"the reference graph is not a DAG; every traversal needs a vis[ited set]."*
Four more reachable cycles follow at `COMP:489-492`.

**Godot has no cycle collector**, so a `RefCounted` cycle is a permanent leak. `PORT:885` states the
result: **ids-not-pointers is load-bearing against `RefCounted`'s absent cycle collector, and the design
does not know it.** `PORT:821` names the danger directly — *"replace the id references with object
references"* is *"the one edit that turns a documented, normal cycle into a permanent leak"*, and it is
the edit the first Godot-fluent reviewer will propose, because it is the idiomatic one.

**Ids mint from the determinism substream** — `ARCH:419`, `id = H(world_seed, tick, subject_id,
purpose)` — which gives unique, order-independent ids **with no shared allocator**. `ARCH:214` states
what that protects: an id service or a counter *"would break the per-person maps' parallelism licence."*
**10a's shape and 10d's ids are the same decision seen twice.**

⚠ One cycle case is already solved in shipped code and not in the design. `COMP:490` says so, and it
checks out: `engine/substrate/keys.py:389-392` — *"invariant 4 (cycle-freedom) holds by construction for
an append-only log whose causes[] may only cite already-logged Keys."*

**The falsifier for all four.** A Godot 4 mechanism that collects reference cycles; a field for which
neither `additive` nor `exclusive` is right; a per-person map that must write something global.

---

## §11 · THE INTERACTIONS

The sections are not independent, and the connections carry more than the sections do.

**§1 and §2 are one arc — the same gap seen as absence and as consolidation.** §1 is the finding
stated as *what is missing*; §2 is the same finding stated as *what already existed three times*. Once
§1 is scoped to existence, §2 carries the whole tenure half, and the two together are `REV:272-273`'s
*"one finding with seven faces."* **The absence framing produced seven work items; the consolidation
framing produced one primitive.** That difference is the argument for looking for the shape before
filing the gap.

**§4 subsumes §5.** `wear` is not a fourth licensed channel — `ARCH:1374` says so outright, *"**`wear`
IS AN EVENT, under §2.4's partition, and it needs no special case at all**"*, and `ARCH:1377` records
that an earlier version argued it in as a fourth thing before the partition removed the need. A harbour
silts because harbours silt; tending it is a choice; **both move one quantity, which is Jordan's flux
model, and the partition explains why without special-casing either.** Two rulings arrived
independently and the second dissolved the first's special case.

**§3 and §9 are both leverage without a stored quantity.** A faction's power is `commit` edges counted
on demand (§3); an office's reach is the establishment's person-seasons spent on demand (§9). Neither
stores a strength number, and in both cases the thing that would be the number — membership, throughput
— is instead *the people*, who can refuse. **`SUP` §1.3's constraint that "factions are only as strong
as the people under their purview" is the same sentence as D-2's act economy**, and neither was written
with the other in view.

**§8, §10c and §10d are all the port constraining the design.** Not translating it, constraining it:
the enforcement claim must weaken (§8), two names must change (§10c), and one representation choice
becomes load-bearing for a reason the design never had (§10d). **In all three the port is the party
that knows something the design does not** — and in §10d it knows the design is right.

**§10a pays for §3 and §10d pays for §10a.** Power as a query (§3) means recomputation, which needs
parallelism, which needs per-person maps that write nothing global (§10a), which needs ids that mint
without an allocator (§10d). **Remove any one and the layer above it becomes a bottleneck.** This chain
is the strongest structural result in the set and no single section states it.

**§7 is what §1, §4 and §5 exist to feed.** The epistemic layer needed facts, not mechanism (§7);
existence changes, event-driven creation and untended decay are three sources of disputable fact that
the prior design did not have. **The enlargements are not features added beside the knowledge layer;
they are its input.**

**§6 and §8 are the same boundary from two sides.** `choose` may not read the world (§6's split
enforces it in the type; §8's rule enforces it in the name table). `Sensation` exists because that
boundary, drawn strictly, cut off the decision's own motive — **the enforcement mechanism had no channel
for its central input**, and the fix was a value type rather than a hole in the boundary.

**§10b is what makes §4's partition implementable.** The partition assigns a driver to every state
change; per-field commutativity is what lets an event's delta and forty acts' deltas land on the same
field in one season without an ordering rule. `ARCH:451` — the event delta *"is strictly before all of
them and needs no commutativity argument at all."*

---

## §12 · WHAT THIS PREDICTS FAILS NEXT

If these are right, the failures are locatable and three of them are named on disk already.

**1. The next reinvention comes from `systems/`, not `proposals/`.** The sweep was scoped to
`proposals/` and says so: `SWEEP:798-808` names two documents it therefore could not see —
**`systems/_architecture/governance_ripple_substrate_v1.md`** (559 lines; *"the only statement of the
draw's weighting formula anywhere in the tree"*, cited zero times by `SUP`, `REV` or the v2 suite) and
**`systems/settlements/governance_play_redesign_v1.md:154`**, which owns the Π homeostat every trigger
in the event deck reads. Its own conclusion: *"**a fourth instance is more likely to come from
`systems/` than from `proposals/`.**"* `CLAUDE.md` §3 calls `systems/` the design source of truth, and
**the sweep never entered it.**

**2. The `wear`-to-restoration ratio is the first thing to fail on contact with a run.** `ARCH:1711-1712`
states it against itself: the ratio *"sets the world's entire difficulty curve, and no number in this
design has been measured."* Every claim in §5 about tending, thriving and dying is a claim about a
number nobody has chosen. **`tools/balance_oracle.py` is a campaign instrument and this is a campaign
question**, so the honest position is that §5 is untested rather than that it is safe.

**3. `efface` is the next uncleared limb to bite.** `ARCH:1859` says so in the deliverable's own refusal
walk — *"`mint` is CLEAR; **`efface` is NOT CLEARED** and the widening is stated"* — extending the
unbounded discrete-destruction limit `SUP:1302-1306` already admitted. §4's extension inherits it.

**4. A Godot-fluent reviewer will propose the leak.** `PORT:821` predicts the specific edit —
*"replace the id references with object references"* — and it is the idiomatic suggestion, which is why
§10d's reason must be written into the design rather than left as a consequence someone rediscovers.

**5. The port's autoload decision will be made for the wrong reasons.** `PORT:285` records it as **still
open** (`godot/godot_conversion_strategy_v1.md`, Part VIII #5) while `godot/scene_tree_architecture.md:16`
already makes `GameState` an autoload holding *"all tracked state"* — *"the exact shape the rule
forbids"*. The decision is live, and §8's reason *"is not currently among the reasons on the table."*

**6. The citation keys will mis-resolve again, and the next one will not be caught either.** Two live
mis-resolutions are recorded at §10c. **Nothing in the suite reconciles the two keys**, and the audits
that could have caught it were reading the documents rather than the addressing scheme between them.

**7. The event deck's home is still unbuilt.** `SWEEP` ranks `2026-08-29-greenfield-systems-suite-v2/11_world_events.md`
(715 lines) first among what the suite had not read — *"the event channel the partition licenses,
already designed"*, carrying rate bounds, two-way reachability and `we.altonian_pressure`. Reading it is
cheaper than authoring the channel again, and §4 makes it urgent rather than optional.

---

## §13 · HOW THESE WERE ARRIVED AT, AND WHY TO DISTRUST THEM

Kept to one section deliberately. The method is not the subject; it is the reason the subject needs
checking.

**Every audit in this session checked derivative documents against each other, and none swept the
corpus.** Two adversarial rounds, a 33-finding review, five parallel runners, a 982-line keys audit and
a Godot audit — all read documents produced by this line of work, against each other. **The sweep was
commissioned only after Jordan twice pointed at material nobody had opened**, and the corpus discoveries
are his; the discovery that four of the review's claims were false was the independent critic's
(`MANIFEST.md:22-23` — 2 corrections from Jordan, 4 from the critic, 7 self-caught, and the seven were
all counts, scopes and wordings).

**The measured cost, re-derived here rather than quoted.** `SWEEP:667-679` reports **108 of 123**
proposal documents over 200 lines cited nowhere by the three surfaces. ⚠ **Recomputed at the tree as it
shipped, with the sweep's own stated method, the figures are 103 of 127** — 190 `.md` under
`proposals/`, 133 over 200 lines, 6 reference surfaces. The method reproduces exactly for most rows and
diverges on one. **The reason is instructive rather than embarrassing:** the sweep ran while the
deliverable was still being edited — commit `4c25cb4` is titled *"WIP — architecture, +35 lines, while
the corpus sweep lands"* — the documents were then revised to cite what it found, and **the sweep's own
table was never recomputed.** Four of its flagship uncited documents are cited at HEAD:
`11_world_events.md` (9), `2026-08-30-fixes/02_the_act_economy.md` (7), `09_ambitions_and_arcs.md` (6),
`10_the_slate_and_salience.md` (4). **They are cited because the sweep worked.**

**Citation count is not coverage**, and the sharpest case needs re-dating. `SWEEP:706-710` — three suite
indexes are cited five times each and *"not one of their 40 constituent chapters is cited even once…
**citing only the index is the signature of not reading.**"* And `KTI` — the document §7 rests on — is
cited **once in `SUP`'s 2,017 lines** and is the **most-cited document in the v2 suite**. The honest
statement is that it was unread at the time of the review and read heavily afterwards.

**Nearly every false claim the session produced was an absence claim** — *"there is no X"* — which is
the only error a derivative-facing audit can reliably make: cheap to produce, rhetorically rewarded, and
**unfalsifiable without a search over the whole corpus**, which is exactly the work every audit skipped.
⚠ The claim is near-true, not clean: *"every licensed non-act channel is a subtraction"* was broken
too, and it is a claim about how a channel works, not about absence. `REV:52` records its refutation —
production has an upper half, `SUP:1603` and the `(3 + d10)/8.5` term.

**Rediscovery held; endorsement did not.** Four findings were rediscovered by runners that could not see
each other, and all four held. The two claims two runners *agreed* on were false — `REVIS:195` banks
*"relevance is never defined"* under *"CONFIRMED — the load-bearing verifications"*, and `REVIS:295-296`
has a second runner calling it *"correct, and an improvement on the review."*

> **Rediscovery across different SEARCHES is evidence. Agreement across different READINGS of the same
> derivative set is not.** `CLAUDE.md` §10's rank-by-independent-rediscovery rule is right, and its
> precondition is that the rediscoverers are looking in **different places**.

**Zero of 76 runner findings were rebutted** (`REVIS:346`). That is the same signal from the producer's
side and it deserves the same suspicion.

**Numbers corrected in this document, each because it did not check out:**

| stated | corrected | why |
|---|---|---|
| the deck is **58** cards | **59** | the body says 59 four times (`grounded_event_card_deck_v1.md:21`, `:273`, `:274`, `:275`); 58 is the abstract's figure and a counterfactual at `:247`, where COURT-07 was **differentiated rather than cut**. The wrong count propagated to three surfaces including `PART:19` |
| enforcement goes from **3 signatures to 23** | **3 → 20, of which 16** | `ARCH:540-559` is 20 rows, 16 resolver-side; `PORT:270`'s *"12 of the 20"* and `PORT:899`'s *"twelve"* are both wrong; "23" is 3+20 and names nothing |
| **108 of 123** uncited | **103 of 127** at the shipped tree | the sweep's table was taken mid-flight and not recomputed |
| *"the review's #1 finding"* — a proposition can never be created | **withdrawn** | `REV:706-710`; a faction is a proposition plus a commitment map, so committing to a newly uttered proposition **is** the faction forming. What survives is that proposition creation is **under-specified** — `SUP:1490`'s one clause, *"no act, no cost, no witness and no phase"* |
| the partition's list was wrong because matter events had no generator | **the generator existed and was unlinked** | `SUP:1346-1349` names the storm as a `season_factor` roll; the review's A7 was broken on it |

**Two figures verified and kept.** **21 of 26** impact types are cleanly social and forbidden to an
event (`SWEEP:418`; the §B6.1 table has exactly 26 rows, and 2 + 3 + 21 = 26 — though `SWEEP:385` opens
the same table calling it *"22 impact types"*, a stray). **Of the nine complete card records, zero are
events** (`SWEEP:443`).

⚠ **But "four-fifths of a deck reclassified" is an estimate and must never be written as a count.**
`SWEEP:470-473` — *"cluster-level estimate, marked as inference… **I did not read these cards; the file
does not contain them**… Treat as an estimate, not a count"* — and `SWEEP:849-851` calls it *"the
weakest claim in this brief and the one most worth attacking."* **The nine records that were read are
also a biased subsample**: all nine are Opportunity, Ambition and Thread cards, and the eighteen
climatic and geopolitical cards — the ones with natural subjects, where the partition would most likely
find events — are not sampled at all. The 21-of-26 result stands on the impact vocabulary; **it does not
license the four-fifths figure.**

**The provenance itself had a hole, and it is worth recording.** Four working documents — the corpus
sweep, the flux ruling, the partition and their manifest — were absent from `main` for part of this
work, because the pull request merged from a head one commit behind the branch. They were restored. **A
provenance record that cannot be reached is not provenance**, and the failure was invisible to
everything in this session except an attempt to open the files.

---

## §14 · THE HONEST LIMITS OF THIS DOCUMENT

**It is one session's account of itself, assembled by the party responsible for most of the errors it
describes.** Three biases follow and none of them is corrected by noticing them.

**It grades the design it produced.** Sections 2 through 6, 9 and 10 describe decisions this line of
work made, and the evidence for them is the documents it wrote. A reader should treat every *"this is
the right primitive"* as a claim by an interested party, and note that the strongest such claim — that
a correct primitive set absorbs new requirements at near-zero cost — is **unfalsifiable from inside**,
because the same author chose both the primitives and the requirements they had to absorb.

**It over-reports failures it caught and under-reports failures it did not.** Every corrected number in
§13 is one somebody found. The class of error this session demonstrably could not detect is **absence**,
and by construction there is no list of the absences that are still there. **§12's first prediction is a
statement about a blind spot, made from inside it.**

**Nothing here executed, and the design does not run.** No claim in this document is a measurement.
Where a section says a mechanism works, it means the document says so and the citation checks out.
Under `CLAUDE.md` §0.2 the entire subject is NOT DONE, and this document does not move it — it is
reference, per `CLAUDE.md` §0.05, and **it may not be cited as the reason a behaviour is correct.**

**The read set is a minority of the corpus.** 103 of 127 proposal documents over 200 lines are cited
nowhere by the three surfaces these ten sections were drawn from, and `systems/` — which `CLAUDE.md` §3
calls the design source of truth — was never swept at all. **These are claims about the documents that
were read.**
