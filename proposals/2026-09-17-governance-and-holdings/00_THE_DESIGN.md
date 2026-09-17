# 00 · THE DESIGN — governance at every rung, and the built world, stated once

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## ⚠ **SUPERSEDED 2026-09-17 by `proposals/2026-09-17-governance-and-holdings-r2/`** (`ED-IN-0233`,
## `ED-IN-0234`, `ED-IN-0235`, `ED-SE-0053`) — the round-two suite, written **from** this suite's own
## `AUDIT_VERDICT.md` rather than over it. **Kept as reference; struck where overturned.** Nothing here is
## deleted and nothing here is current. Where the replacement lives: the policy carrier `in_force` and
## every place-scoped read → `02_THE_WRIT_AND_THE_WORD.md`; the fifth question row →
## `01_ATTENTION_AND_REACH.md`; the seat MECHANISM (the bases and the two predicates) →
## `03_SEATS_AND_CONTENT.md`; hearth larders and the delivery move → `04_MATTER_AND_WORKS.md`; the build
## order and the object count → `05_LEDGER_AND_BUILD.md`. **What SURVIVES is listed in the r2 `README.md`,
## not here** — a superseded file is the wrong place to learn what is current.
## **Strike discipline, stated so it is not mistaken for an omission:** the DEFINING sentence of each
## overturned claim is struck in place; its incidental mentions are NOT individually struck, because a
## document struck word-by-word is unreadable and this banner is the notice.
## Lane: `IN` · id: **`ED-IN-0231`**, SHARED with `01_SEATS_AND_POLICY.md`. **This file allocates no id
## and introduces no claim of its own.** Every sentence below is a sentence one of the four subject
## files already argues, measures and ships a falsifier for; what this file adds is *one statement, in
## one vocabulary, in reading order*. That is why it takes no id: a document with no new claim has
## nothing to book against. If a reader finds a claim here that is in no sibling, **that is a defect in
## this file**, not a twelfth design decision.
## Grade under `CLAUDE.md` §0.2: **`paper`**, like every file here. Nothing in this directory executes;
## §D.3 names the three artifacts that would move it and §D.4 says why none has been produced.
## Method: written at tier **`opus`** (`CLAUDE.md` §10 — *multi-doc synthesis*) as the **unification
## pass** over four documents authored in parallel from one plan. Four documents written simultaneously
## from one spec are not one design; they are four readings of a spec, and the differences between them
## are invisible to each author by construction. Every contested number below was **re-measured against
## the working tree on 2026-09-17** rather than chosen between; every contested judgment was adjudicated
## on stated ground — **the code over prose (`CLAUDE.md` §0.05), a ruling over a proposal, a later
## ruling over an earlier, and the file that opened the source over the file that did not.**

---

> **Jordan, on what a policy is:** ***"Policies aren't just a number added to a roll, but a way to
> change or impact how a governed rung functions."*** · ***"They impact emergence."***
>
> **Jordan, on the cascade:** *"a change to how a rung functions will likely have impacts on rungs
> below it. A provincial policy on farming taxation may end up impacting a hearth, you know?"*
>
> **Jordan, on the player:** *"a player whose character can govern a settlement would like to be able
> to explicitly set policies or advance a project to build something."* · *"Players need to have an
> interface with which to engage with the game world."*

---

## THE VOCABULARY, FIXED — read this before anything else

`CLAUDE.md` §4 makes a term a first-class object: it must be **idempotent in meaning** (a reader with no
memory of this repo lands on the same sense) and **idiomatic in choosing** (the word ordinary usage
already supplies). The four files drifted on six terms and two id schemes. **These are the fixed
readings, and they bind the whole directory.**

| the word | means, here and nowhere else | ~~what it is not~~ |
|---|---|---|
| **seat** | one `Seat` type — a post with a scope, a remit, a conferral basis and a revocation basis. The engine carrier is `Office` | ~~*title*~~ and ~~*office*~~ as separate types. A title is **a value of `revocation.conjuncts`**, not a kind (`ARCH §B.7` call 1) |
| **post** | the seat's name string, from which **nothing may be inferred** | ~~a discriminator~~. Reading purview off a post string is the live defect (§A.2) |
| **purview** | what a seat governs: the `contain` closure of its `scope`, plus the holder's own `hold` Tenures, asked of **the seat exercised** | ~~*domain*~~, ~~*scope*~~ used for the same thing. `scope` is the seat's **one** rung (or none) |
| **policy** | a `Record` of kind `dispensation`, scoped to at most one rung, naming one **clause** and one `OUGHT` Proposition as its **terms**, held by its issuer | ~~*instrument*~~ as a second noun, ~~a modifier~~, ~~a flag on a territory~~ |
| **clause** | one of seven — `draw: spend: sit: levy: admit: bear: hear:` — each either reordering a step, changing an option set, or ~~creating~~ **conditioning** a date (the `Date` is `convene`'s — §A.4, corrected 2026-09-17) | ~~*dispensation*~~ for the clause. The `dispensation` is the Record; the clause is what it says |
| **reach** | a **declared operand** on the policy, `near | all`. A superior spends an act to declare `all` | ~~the ordinary word~~ in `verb_table.yaml:261`'s *"its reach is the domain the issuer governs"*. Two senses, named (`03` §A.4) |
| **a `works`** | the multi-season construction: a `Record` of kind `works` with act-declared stages | ⛔ ~~*a work*~~ (collides with the live verb `work`, *labour at a site*) and ⛔ ~~*a project*~~. **RULED `01` §A.12; `02` and `03` used both and are corrected in place** |
| **fabric** | the built thing itself — a `Site`, which has a `condition` | ~~*building*~~ used for the plot |
| **address / plot** | the `Rung` a fabric hangs from. A building **stands on** a `hearth`; it **is not** one | ⛔ ~~"a building IS a hearth"~~ (`venues.yaml:21-22`), **narrowed by `02` §A.1.2** and corrected in `03` |
| **sworn** | `members(w, policy.terms)` — everyone with a live `commit` to the policy's Proposition | ~~*entrenchment*~~, which already means *seasons a holder has held a thing*. Two ladders for one word is an **S** defect |

**Two id schemes, unified 2026-09-17, because they collided:**

- **`ARCH`** = `architecture/meta/04_CODE_ARCHITECTURE.md`; **`AX`** = `architecture/meta/01_AXIOMS.md`.
  ~~`04 §B.7`~~ and ~~`01:443`~~ read as pointers into *this directory*, and `04_BUILD_ORDER.md` really
  does have a `§A.3` of its own. A bare `01`/`02`/`03`/`04` now always means a file here. Cite `ARCH`
  by section; where a section pointer still carries a line, **the section is authoritative**.
- **Falsifiers and loops are prefixed per file** — `SP-n` (`01`), `BW-n` (`02`), `SU-n` (`03`),
  `BO-n` (`04`); loops `SP-L±n`, `BW-L±n`, `SU-Ln`. ~~`D-1` meant four different things and `L−1` meant
  three~~, and inside `03` `L-1` meant both a read licence and a loop.

---

# PART A · THE DESIGN

## §A.1 · The whole of it, in one page

**A seat is a place in the world that may take certain kinds of act over certain ground.** It is one
type. It carries a `post`, an optional `scope` (a rung; null means a cluster with no place), a `remit`
of acts, a `conferral` basis saying which act fills it, a `revocation` basis saying what emptying it
requires, and nothing else. **It never carries who holds it, who serves it, or a modifier of any kind.**
Who holds it is a `hold` Tenure owned by the holder. Who serves it is a set of `oblige` edges. *Owner:
`01` §A.1, and it is `ARCH §B.7` entire — ratified Layer 1, merely unbuilt.*

**A policy is a sentence somebody uttered, put in force through a seat, and held like any other
possession.** Mechanically: a `Record` of kind `dispensation`, whose `rung` is the one rung it names,
whose `subject_matter` carries the clause and the `reach` operand, whose terms are an `OUGHT`
Proposition somebody `utter`ed at a venue, and whose possession is an ordinary `hold` Tenure minted by
the opening act. **It is in force while a living person holds it.** *Owner: `01` §A.7.*

**A built thing is two objects and one thing.** The **fabric** is a `Site` with a `condition`; the
**address** is the `Rung` its `rung` field names. The seam between them is **occupancy, derived and
never stored**: `occupiable(w, site) ⇔ w.rungs[site.rung].kind == "hearth"`. A wall has no household,
therefore no hearth, therefore no store, no date and no `contain` edge — not a special case for walls,
but what *nobody lives in a wall* means in this vocabulary. *Owner: `02` §A.1.*

**The cascade is one Query and no propagation object.** `in_force(w, rung, clause)` walks `contain`
ancestors from a rung upward and returns the nearest live policy conditioning that clause — unless a
farther one declared `reach: all`. MATTER calls it; four `requires` conjuncts call it; the question
filters call it. Nothing is told, nothing is stored, nothing can go stale. *Owner: `01` §A.8.*

**The player's surface is a function of what their character holds.** Not of the world. Three read
licences and nothing else: **L-1** my own ledger, **L-2** `Sensation`'s two scalars, **L-3** state I am
an endpoint of. Every cell is HELD, STALE, UNHELD or CONTRADICTED, and the surface **never marks a
claim false**, because that would delete every deception mechanism in the game at once. *Owner: `03`
§A.1.3.*

**Building costs acts, terms, matter, wear and other people — and none of those is a cap.** *Owner:
`02` §A.8.*

## §A.2 · The one defect that makes all of it unreachable, and it is measured

**Purview is read off a post STRING.** `titles_held` filters on `title_domain(post) is not None`
(`predicates.py:151-152`, and `title_domain` lives at `data/rosters.py:459`), and sixteen of the
nineteen posts in the built world — *Chief Parliamentary Clerk*, *Cardinal Justice*, *Royal Marshal*,
*Skald-Chief* — are not on the eleven-name `titles.domains` roster. **So sixteen of nineteen
seat-holders have purview over nothing, including their own seat's rung.**

`ARCH §B.7` already rules the repair and grades it MECHANICAL: ***purview is asked of the seat
exercised, not the actor*** — `Act.via : SeatId?`, and every purview walk uses `via.scope`. *A regent
has the seat's purview.* `Act.via` appears **nowhere** in `engine/season/*.py`.

**And the seat cannot be filled either.** Every one of the nineteen seats has an **empty `conferral`
and an empty `revocation`** basis; `_req_confer` refuses an office with no conferral basis
(`predicates.py:181-182`) and `_req_revoke` one with no revocation basis (`:234-235`). *A plan that
fixes the eligibility model and not the content fixes nothing.*

## §A.3 · What a seat does, per rung — and one axis does most of the work

The ladder is `person < hearth < community < settlement < territory < province < duchy < realm`, and
the title ladder is total over it by Jordan's own ruling. **What makes the rungs different is not
scale.** As you climb, your clauses reach more people and **your claims about them get coarser and
older** — a King's knowledge of a hamlet is a second-hand cohort claim three seasons stale, because
that is what is in his ledger. **The fog at the top of the ladder is epistemically honest rather than a
UI convenience,** and it falls out of `AX-2` plus the cohort rule with nothing authored.

The per-rung table — what each seat decides, who opposes it, what a season there feels like, and what
drama the rung generates **with no player present** — is `01` §A.16, eight rungs, and it is not
restated here.

**Two measured cautions that belong with it.** (1) **The historical corpus is silent below settlement
scale**, so person, hearth and community are derived or invented, and their only numeric source is a
design document in a superseded tree — cited for intent, never as a value (`CLAUDE.md` §0.05). (2)
**The province is the one rung where two of Jordan's own rulings pull against each other**:
`rosters.yaml` carries `province` as a `rung_kind` with a Count, while the 2026-07-13 ruling makes a
province *"an emergent aggregation that exists only while its constituent territories share a common
faction holder"* (`scale_hierarchy_v1.md:32`) and `build_realm` builds **zero**. The later ruling
governs; the kind stays declared and uninstantiated. That is exactly why the Count is the one seat
whose scope is recomputed every season and the one seat that can outlive its own country. ⚠ *2026-09-17 NERS pass:* a scope recomputed every season is not `ARCH §B.7`'s `scope?` — one rung, declared at `establish` — and a set of territories is the `domain: RungId[]` shape `01` §A.1 refuses. Under §B.7 the Count is a **cluster** seat whose clauses reach by `binds`, the **unbuilt diagonal** (`01` §A.7.5), not by the walk of §A.5.

## ~~§A.4 · The policy, end to end~~

> ⚠ **SUPERSEDED 2026-09-17 — `../2026-09-17-governance-and-holdings-r2/02_THE_WRIT_AND_THE_WORD.md` (`ED-IN-0234`).** The instrument below is
> withdrawn entire: `holonic_ARCHITECTURE.md` §37.3 forbids by name the broadcast and the state write this
> section's MATTER half performs, and Jordan's ruling this session forbids the churn it puts in the
> contents. What survives is the ambition — *"a way to change or impact how a governed rung functions"* —
> carried by a writ that is handed to an executor whose act moves the world.

**Seven clauses, onto the closed seven `requires` forms, using three of them.** `draw:` and `spend:`
are read only by MATTER. `sit:` has two readers — it writes the rung's dates *and* gates `convene` (⚠ it attaches a convening condition and names the rung's dates; **the `Date` object is still minted only by `convene`** — `(Date, due_at)` is `[RES]`, *"CAL struck"*, `write_matrix.yaml:93-100`; corrected 2026-09-17).
`levy:`, `admit:`, `bear:` and `hear:` gate an act. A clause conjunct is `all: [<the verb's own cell>,
<the clause's cell>]`, which the grammar already implements; **an eighth form refuses at load**, and
that refusal is the design statement rather than a limitation. *Owner: `01` §A.9.*

**`in_force` is a Query BEHIND the predicate and never an operand.** A clause cell binds only the act's
own operands; the policy it tests against is *found by the walk*. So no cell names a dispensation, no
ninth operand is coined, and `H-94` — which blocks `comply`, `evade / defy` and `refract` on exactly
that missing operand — **is not a precondition of this design and must not be scheduled as one.**

**The uniformity rule is what keeps a clause from being a special case.** A clause's terms are a
predicate over what the loop can already read off a person at that rung — their marks, their live
`commit` edges, their presence, their `hold`s — and **a clause conditioning another person's options
may not name a person id.** Two things fall out: scripting drift becomes unspellable in a policy (you
cannot write *"except Björn"*), and **every policy has beneficiaries and burdened, both computable**.
Nobody authors *the guilds resent the grain law*; the guilds are the set the predicate excludes.

**Three prices, three different acts.** Striking a policy is a superior's `revoke` through a seat whose
basis reaches. Repealing it is the issuer's own `release`. Letting it lapse is **nobody's act**: the
issuer dies, the `hold` ends, and `in_force` stops returning his row. Therefore **the first season of a
reign is spent re-issuing what the successor wants to keep** — act by act, out of about five, in
public — and what he lets lapse, **the sworn notice, because their commits did not lapse with the
hold.** That is the medieval *confirmatio* arriving from a liveness check that already runs
(`matter.py:73-78`).

**And there is no policy-effects readout.** Not by restraint — by construction on the chooser's side
(`decision/` cannot reach a `World`), and by the read licences on the surface's. What the Count has
instead is a ledger containing, three seasons later, a fading `told_by` claim; and because `causes[]`
is required and non-empty, the chain back to his own clause **exists in the data and can be shown to
him at the moment somebody tells him, not before.**

## ~~§A.5 · The cascade, as arithmetic~~

> ⚠ **SUPERSEDED 2026-09-17.** The arithmetic is sound and the SITE is wrong: nothing addresses a place.
> `../2026-09-17-governance-and-holdings-r2/02_THE_WRIT_AND_THE_WORD.md` replaces the MATTER cascade with delivery to a person, and
> `../2026-09-17-governance-and-holdings-r2/04_MATTER_AND_WORKS.md` (`ED-SE-0053`) owns what the matter economy does instead — reaching the
> 211 hearths **with no content move and no new store**.

There is no cascade step and no cascade object. There is MATTER, whose ordering two clauses condition,
and one walk that finds them:

```
MATTER at rung r:
  1. yield(r) -> r.stores                                   (Rung, yield) -- "only here"
  2. spend: = in_force(w, r, 'spend:')     the declared stage draws, in the order the clause names
  3. levy:  = in_force(w, r, 'levy:')      the share DEMANDED of r.stores (read by demanded()); NOTHING LEAVES HERE
  4. draw:  = in_force(w, r, 'draw:')      mouths fed from r.stores IN THE ORDER the clause names
  5. short  = what step 4 could not cover  -> (Person, body)     [UNBUILT]
```

A Count issues a `levy:` through his provincial seat and **names no settlement and no hearth**. At each
settlement, step 3 calls `in_force(w, S, 'levy:')` and the walk ascends to the province (⚠ **which does not exist in the built world**: `build_realm` builds `province 0`, §A.3, and no `contain` chain names one — `populated.py:317-363` links hearth → community → settlement → territory → duchy → realm. A Count's seat is a cluster seat whose clause travels by `binds`, `01` §A.7.5's **unbuilt diagonal**; the headline runs today from a **duchy** or **territory** seat, and *provincial* is Jordan's intent rather than a constructible step. Corrected 2026-09-17). At each hearth
beneath, the same walk finds the same clause **unless the settlement's own seat has issued a nearer
one**. Step 4 draws mouths against a smaller store. ⚠ **Step 3 corrected 2026-09-17:** it read ~~*the share that leaves r.stores*~~; `02` §A.6 RULES that MATTER moves no matter across a `contain` edge — a tax that collects itself is the fourth clock `AX` **T-c** forbids — and `transfer` binds `from` to the actor's own containing rung. So the share is **demanded** at MATTER and **moved** only by a person's `transfer` at RESOLVE, one season upstream; step 4 draws against a store somebody's act has already reduced, or has not. `01` §A.10 carries the same strike.

> **A named woman in a named house is thinner this season because of a sentence a man she has never
> heard of uttered in a chamber she has never seen. Nobody authored her crisis; it is lines 3, 4 and 5.**

**Three noise sources, all pre-existing, none a modifier.** The yield is already a draw, so *a fifth of
a good harvest is a tithe and a fifth of a bad one is a famine*. The fold is ordered, so **which**
hearth goes short is decided by who reached the store first. And whether the far clause is read at a
rung at all is another person's choice — `reach: all` is an operand somebody declared in an act out of
about five. **That third one is the strongest noise source available, because it is not a die: it is a
politics.**

**The check, stated so it can be run:** no clause has a term that reaches a pool or an obstacle.
`levy:` names a matter kind and a share of matter; `draw:` names an order; `sit:` names a date and a
quorum. **If a later session adds a clause with a numeric term that reaches `pool` or `Ob`, this design
has been broken and that clause is the break.**

**The bottom link is not built and is named as unbuilt.** `matter.py` computes the shortfall and
**deliberately emits nothing**, on L5's rule that a threshold crossing may never produce an outcome.
And today the two halves of the matter economy never meet at all: **37 settlements accumulate 4,810
units a season that nobody is addressed to eat, and 46 people are short every season in rungs that hold
nothing.** The repair is two content moves plus a predicate, not a fourth clock — *a tax that collects
itself is a clock nobody wound, and `AX` **T-c** forbids it.* *Owner: `02` §A.6.*

## §A.6 · How it comes back up

| # | channel | speed | who pays |
|---|---|---|---|
| 1 | **EVASION** — `transfer` the grain before the date, `move` out, `forge` a smaller holding, or simply not work the field | same season | the evader, one act. **The governor never sees it, and it is the commonest channel** |
| 2 | **THE GAP** — `delivered(levy, rung, season)` against `demanded(levy, rung)`, banded | slow, arithmetic | nobody |
| 3 | **THE PETITION** | one date | the petitioner, one act of about five; then a seat-holder's own act to carry it up |
| 4 | **THE COLLISION** — a material signal *and* an interpretive one, both R-1 aggregates over descendants | when both hold | the seat that issued the `sit:` clause that attached the condition |

**Legitimacy is a band on a gap, never a field and never `upkeep`.** Delivering changes nothing; short
adds `petition` to the subject's options and `dispatch`/`revoke` to the holder's; chronically short adds
`repudiate` and `defy` to the subject's and **takes nothing from the holder's — and that asymmetry is
the decay.** Nothing is stored and nothing decays on a clock. A seat hollows out because fewer of its
clauses are read anywhere, which is `in_force` returning somebody else's row.

> **AND THE CONSEQUENCE THAT COSTS NOTHING, BECAUSE IT IS AN ABSENCE.** A rung whose seat never issued
> a `sit:` clause **has no venue**: its grievance has no date to fire at and no channel to leave by. So
> **a governor who convenes nothing is not safe — he has closed the relief valve, and the grievance
> leaves by the only door left: a person's own act, against his body.** A genuine strategic choice with
> no dominant option, made of two absences.

**Non-compliance needs no verb.** A near policy displaces a far one not because it outranks it but
because **the near seat's people are standing there**; the far policy is not void, it is *unenforced*,
still citable, and its issuer may strike the near one if his remit reaches. *Ignoring a decree is the
nearer policy existing.* — ⚠ **and which of those two wins is the one thing in this design that is not
decided. See §C.1, RR-1.**

## §A.7 · The built world

**Five site families, and the discriminator is not the fiction — it is which column of which existing
table the site's condition band reaches.** PRODUCER reaches `site_yield`; VESSEL bounds `Rung.stores`
(the one genuinely absent reader column); ENCLOSURE and HALL reach `band_floors`; DWELLING reaches
`capacity`. **A kind that reaches no new column is not a new family.** Adding a kind is **three
coordinated data edits or the world does not load**, because the loader checks membership in both
directions. *Owner: `02` §A.2.*

**A fortification is an ENCLOSURE `Site` whose condition is its strength — bands, not a level — and
what it gates is somebody else's verb.** One rampart per **quarter**, so a besieger picks a quarter.
Three reads onto mechanisms that already exist and **no siege subsystem**: a terrain row in a mass
battle; a `move` refused by its `contain_path` conjunct; and a contest graded into a negative
`(Site, condition)` delta through the same summing clamp a repair uses with the sign flipped. **A
wall's resistance is not a number** — it is the verbs it removes, the verbs it grants, and the seasons
it takes to grade it down through three bands. *Owner: `02` §A.3.*

**The lifecycle is four moments and exactly one new verb.** `found` a plot (NEW) · open a `works` with
`create_record` (exists and RUNS — its effect body mints the maker's `hold` in the same act) · a stage
ripens at MATTER, and **stops if the maker is gone** · `restore` the fabric against a `ceiling` set by
the matured stages. **Building and repairing are one act at different bands**, which is why there is no
`build`, no `repair`, no `raze`, no `garrison`, no `convert` and no `undertake`. *Owner: `02` §A.4.*

**What is held, and what may never be.** `hold` reaches `Office | Rung | Record | Proposition` and
**never a `Site`**. What is held is the **plot** the fabric keys to, or the **`works` Record** on it.
The ground is not tidiness: make every fabric single-held and `share = 1` everywhere, and **the commons
stops existing as a category** — a harbour, a seam, a road, a wall — and with it the only mechanism in
the design that produces collective ruin from rational private acts. **The cost, stated:** you cannot
confiscate a single building; you confiscate its plot, which takes everything on it. *Owner: `02`
§A.5.*

**And the subject of a `hold` is a Person, only.** Sixteen of the thirty-five live `hold` Tenures in
the built world have a **faction Proposition** as subject, which ratified Layer 1 forbids by name
because it permits *territory held by a banner nobody carries, uncontestable because the holder can
never appear at a venue.* **The fix is content, not schema**: a province "held by the Crown" is held by
a **named person** with a live `commit` to the Crown's Proposition — and **his death is a political
event somebody has to win.**

## §A.8 · What the player sees

**The interface is required and it is inside a decision.** `ARCH §C.11` refuses the obvious escape by
name: *"for a player character the player IS the decision procedure,"* so a split on **who is looking**
breaches `AX-2`. There is no seat from which a surface may look at the world — only a person, what they
hold, and the arithmetic of what they hold.

**Four surfaces** — the place · what I know · the seat · the scene — **plus three chrome rows** (where
I am, what I have left to spend, the season and the date). Everything else in the UI corpus is cut
against an existing carrier: no typed zoom layers (zoom is `parent_of`/`descendants`), no Slate dock
(a `Question` carries referents and every referent has a place), no character sheet (`standing_of`
**is** the gap between told-about-me and my own firsthand claims), no cutscene queue (claims land at
WITNESS and WITNESS is a barrier, so there is nothing to nest), no stat bars, no mode switch.

**The frame is ATTENTION, not capability, and the top-level affordance is CAUSING A QUESTION.** The
engine asks a person about something through exactly four sources — a date with my name in it, a claim
landing about me or mine, a band crossed where I stand, a standing commitment — and `01` proposes a
~~fifth, **Q5 `purview`**, so a governor is asked about a rung he governs and does not own~~ — ⚠ **the
fifth ROW is withdrawn 2026-09-17 and the fifth THING survives as a term:**
`../2026-09-17-governance-and-holdings-r2/01_ATTENTION_AND_REACH.md` (`ED-IN-0233`) makes purview a term of **REACH**, a filter on the four
existing sources, not a fifth source beside them. It also measures why the row was the wrong shape — the
purview limb adds **zero** questions on the tree as it stands, so an N-line asserted for it fails its own
cut and is recorded NARROWED. **Four of the
five askers are things a player can CAUSE**: send somebody, set a date, petition, or swear. So the
surface's deepest control is *making a matter askable*, and the candidate list is what falls out of it
rather than what is rendered at you. *Owner: `03` §A.2.*

**Three display laws that are the design and not decoration.**

1. **Confidently wrong stays indistinguishable from confidently right.** The surface never marks a claim
   false. A correctness mark deletes every deception mechanism in the game at once.
2. **UNHELD is a named absence, not an empty cell.** *"the bin at Gelbgrund · you have never looked"* —
   never "empty".
3. **No percentage, no probability, no outcome projection.** The engine runs one world; there is no
   distribution to read off, and a pre-commit percentage is *a number without a control* rendered as an
   affordance. A `works` shows **stages as named terms with the matured ones struck**, and a
   half-finished fabric renders as **a place with nothing to do in it** — the player reads *not
   finished yet* off the absence of affordances.

**Causation is a WORKSHEET over the player's own claims, never the engine's `causes[]` DAG** — which
is architecturally barred, not merely discouraged. A link is drawn only where the player holds a claim;
where they do not, **a gap, with the named unknown that would close it**. Competing causes show
**unranked**, because ranking them is the engine deciding a person's conclusion. And closing a gap is
an act on a verb that is formable and resolvable today: `reconstruct`.

> **The refusal display is the most important screen in the game.** *You believed the bin held eleven —
> your own eyes, last season. The bin holds three.* Two rows and nothing else: the moment the player
> learns the world is not what they thought, in the only terms that are honest. The data is already on
> the Event.

## §A.9 · What it costs to build, and the five bounds

**Five affordances, every one an existing or proposed act, never a menu of abstractions.** At a plot you
hold — `found` a new plot (with leave), open a `works` naming a kind. At a fabric you are present at —
`restore` it, `work` it, contest it. At a `works` you hold — `confer` it, or `destroy_record` it
(abandon). At a rung you govern — `utter` an order scoped to it and court swearers, which is their act
and their choice. At a store you hold — `transfer` it.

**Five bounds stop a player building everything, and not one of them is a cap.**

| bound | why it is not a cap |
|---|---|
| **acts** | each of `found`, `create_record` and every `restore` is one of about five, at one place, and the actor must be present |
| **terms** | stages ripen on their own schedule — **matter cannot buy time** |
| **matter** | the cost draws from a store that also feeds the people in it — **every building is a decision not to eat** |
| **wear** | everything already built is a standing bill against the same store, so **the more you have built the less you can build** — a bound that tightens with success, which no cap does |
| **other people** | leave, masters, swearers, and whoever is present to break what you raise |

**Sabotage needs no verb.** The stage draws from `stores`; empty the store — a `transfer`, a `levy:`,
or better, **a rival's `spend:` clause at a nearer rung committing the yield elsewhere** — and the
`works` stalls *lawfully*. The saboteur never reads the `works` and has broken no rule.

**And the stall is an EVENT**, therefore witnessable, attributable and citable in an argument — *"the
harbour you promised is three seasons stalled."* A progress bar that simply fails to advance emits
nothing and **dominates by silence**.

---

# PART B · WHAT THE WHOLE DESIGN ADDS, AND WHAT IT MAKES UNNECESSARY

**The bar is `AX` ID-13** — *a declared field must reach a reader, or it is not declared* — so every
addition names its reader, and `ARCH` PART D row 1 forbids an addition that is a new actor, a new
authority or a new modifier.

| added | count | new primitive? |
|---|---|---|
| **verbs** | **1** (`found`) | no — it is the producer two declared write-matrix rows have waited for, and `ARCH §F.20` asks for it by name |
| **effect bodies** | **2** (`found`, `restore`) | no — `restore`'s row is `grade: ruled` with its formula already in it; eleven bodies exist |
| **Queries** | ~~**5**~~ **8** (`in_force`, `delivered`, `demanded`, `ceiling`, `capacity` — **plus `occupiable` and `serves`, RULED in `02` §A.1 / §A.5.5 and counted by nobody, and `character`, `04` item 23**; corrected 2026-09-17) | no — owned by Nobody, storing nothing. `capacity` is already declared in the ratified Query roster; `character` ships only with a consumer named |
| **Record kinds** | **2** (`dispensation`, `works`) | no — the fold is already owed by a ratified position |
| **rosters** | **1** (`record_kinds`), plus **5 site families** as rows on an existing one | no — the loader pattern exists, and a `.kind` matched as a free string is `AX` ID-4's defect |
| ~~**question sources**~~ | ~~**1** (Q5 `purview`)~~ | ⚠ **WITHDRAWN 2026-09-17** — `../2026-09-17-governance-and-holdings-r2/01_ATTENTION_AND_REACH.md` makes it a term of REACH, so the roster gains **no row at all**. And `under_purview` is reflexive where `descendants` is proper: the correct set is `descendants(seat.rung) ∪ {seat.rung}` minus the seat exercised, measured 365 against 364 |
| **terms operands** | **2** (`reach`, a `ttl`) | no — operands on a Record the fold already carries |
| **emission kinds** | **2** (`stage.stalled`, `docket.lapsed`) | no — one rule, and `03` finds it a third use as a STALE cell |
| **predicate conjuncts** | **2**, both inside a single existing owner | no — an eighth `requires` form would refuse at load |
| **surface readings** | **4**, over existing state | no store, no carrier, no verb |
| **content moves** | **2** (fabrics at the rungs people are in; 16 faction holds re-homed) | content, not schema |
| **fixture columns** | **1** (`houses` per DWELLING kind — `02` §B.1 counts it; this table omitted it until 2026-09-17) | ⚠ **an addition**, `[OPEN — Jordan tuning]` |

**Carriers added: 0. Fields on carriers: 0. Write classes, steps, strata, eligibility kinds, tenure
kinds, `requires` forms and operands: 0.**

**And what it makes unnecessary, consolidated across the four files.** Fourteen design-only settlement
verbs (Develop · Fortify · Keep Order · Hold Court · Levy · Survey · Sponsor · Treat · …), each of
which built naively is **a button** — an act resolving instantly against a known number and writing a
stat. Nine building verbs (`build` · `repair` · `raze` · `garrison` · `convert` · `capture` ·
`improve` · `ruin` · `undertake`). A siege subsystem. A propagation table and a stored per-rung policy
map. A `governance_mode` enum — *a mode is a set of policies in force*. `Office.upkeep` decay, a
legitimacy field, a stored popular-support number. `veto_holders`, `judging_set_rule`, `Tenure.payload`,
`Rung.sites`, `budget_office_bonus`, the `is_title` branch and three helpers. Thirteen settlement
gauges as stored fields, a transition registry with its hysteresis, three stat-bar schemes, a
completion percentage, four typed UI layers, a Slate dock, a character sheet, a Codex, a cutscene queue
and a mode switch. **And every "+N to a roll" reading of a policy or a built thing.**

**E, scored LAST and as a ratio (`CLAUDE.md` §0.06).** In: one verb, two effect bodies, ~~five~~ **eight** Queries (three counted by nobody until 2026-09-17), one fixture column,
two Record kinds, one roster, one question source, two operands, two emissions, two conjuncts, four
readings. Out: the list above. **PASS as a ratio, far below one primitive added per primitive removed —
and it would FAIL scored alone**, because the largest moves here are deletions and an amputation always
scores well on tidiness. Said plainly, per §0.06's own instruction.

---

# PART C · THE THREE QUESTIONS

## §C.1 · WHO OWNS THIS?

| the thing | owner | and never |
|---|---|---|
| a seat's remit, conferral, revocation, `binds` | the **Seat**, written once by `establish` | never a holder, never a place |
| possession of a policy, a `works`, a plot, a seat | the **`hold` Tenure**, owned by its subject, **1 per object**, `Person` subject only | never a field on the thing held, never a faction |
| a policy's terms | the **Proposition** — immutable, `frozen` | never editable; renegotiation is a new utterance |
| the issuing seat of a policy | the opening **`Act`**'s `via` | never a field on the Record |
| a fabric's condition | the **`Site`**, one writer per write class | never a `Rung`, never an aggregate |
| a plot, its store, its dates, its records | the **`Rung`** | never a social aggregate — `__setattr__` raises |
| which policy governs a rung · `sworn` · `capacity` · `ceiling` · the delivered/demanded gap | **Nobody.** Queries, resolver-side, World first | never stored, never cached outside the driver |
| what a person believes their seat permits | the **person**, in their own ledger | never a grant field on an edge |
| the ladder | `World.contain_ascends`, single owner | never re-derived |
| the closed sets | `engine/season/rosters.yaml`, read at runtime | never a design document (`CLAUDE.md` §0.05) |

## §C.2 · WHAT CAN CHECK THIS? — and the honest headline is that most of it is MECHANICAL

`ARCH` PART D's own warning governs: *"A row graded MECHANICAL or CONVENTION is here because the reader
will assume it is structural, and the assumption is the failure mode."*

| claim | grade | why |
|---|---|---|
| an eighth `requires` form cannot ship | **STRUCTURAL** | the loader refuses at load, independent of the roster |
| `capability` never gates a verb | **STRUCTURAL** | refused **by name**, even if rostered |
| a policy cannot carry a modifier | **STRUCTURAL** | no numeric field a resolver reads as a bonus, and `Rung` raises on an undeclared attribute |
| a fabric's condition cannot be node-keyed onto a place | **STRUCTURAL at the type** | `Rung` has no condition field; the collapse cannot be spelled |
| `in_force` cannot go stale | **STRUCTURAL** | it is a function; there is no field to initialise and forget |
| `decision/` sees no World | **STRUCTURAL by path** | plus a live AST test |
| purview is asked of the seat, not the actor | **MECHANICAL** | `ARCH §B.7`'s own grade, **and it is violated in running code today** |
| a clause cannot name a person; adding a site kind is three edits | **NOTHING today** for the first (the cell is load-checked, the Record is runtime — `01` §C.2, corrected 2026-09-17) · **MECHANICAL at load** for the second | the coordinated-row check; for the clause, an `issue` effect body that does not exist |
| a `hold` never reaches a `Site` | **MECHANICAL once the conjunct lands — NOTHING today** | ⚠ `add_tenure` checks kind and `contain` ascent and **nothing about object class** |
| the renderer reads only L-1..L-3 | **MECHANICAL** | a path/AST scan — ⚠ **and a `TRACE` assertion alone cannot observe the failure**: four resolver functions emit no `TRACE.query`, `parent_of` among them |
| a policy-effects readout cannot be built on the surface | **MECHANICAL** | ⚠ corrected — see the note below |
| a claim is never marked true or false · no percentage · the clause→form map · Q5's roster position | **CONVENTION** | the check is a reader |

> ### **STRUCTURAL on the surface side: NONE, and that is the finding.**
> `01` graded *"a policy-effects readout cannot be built"* **STRUCTURAL**, on the ground that `decision/`
> cannot import `state/`. **That is true of `choose` and does not reach a renderer**, and `03`
> measured why: the surface's home `engine/season/port/` **does not exist**, `ARCH §A.2`'s read-licence
> table has **no `port/` row**, and the scan that would catch a resolver read has four holes. `AX-2`
> survives for the surface as **discipline plus a scan**, which is what the withdrawn Render Law
> claimed to replace. Claiming STRUCTURAL here would be *a guard that cannot observe what it guards*.

## §C.3 · WHOSE ACT MAKES IT HAPPEN?

**Every state this design renders is deposited by an act, and the actor is named.** The terms are said
by a person's `utter`. The policy is put in force by the holder's `issue`, `via` the seat. The world is
told **per person, differently**, by WITNESS's fan-out. People swear by their own `commit`. **The
clause is then read at a rung it never named by nobody's act** — MATTER calls `in_force`. A shortfall
reaches a body by nobody's act. Somebody evades by their own `transfer`, `move` or `forge`. Somebody
petitions. A convener buries it by ordering a docket, and `docket.lapsed` names his seat in `causes[]`.
A date fires and **nothing is decided**. A bench member blocks by `repudiate`ing his commit — **not by
a veto field, because a veto would make blocking free and anonymous** where a `repudiate` puts the
blocker's name in every ledger the fan-out reaches. The issuer dies and everything he issued falls out
of force, by nobody's act. **The successor re-issues what he wants to keep, out of about five, in
public, each one a choice he can be held to.**

**The loops are enumerated and signed in three registers** — `01` §C.4 (governance, `SP-L±n`), `02`
§A.9 (the built world, `BW-L±n`), `03` §C.3 (the surface, `SU-Ln`). ⚠ **They were all `L±n` and
collided**; the prefixes are this pass's repair. **None of the three is a completeness claim**, because
`AX` ID-16's own derived check is blocked — one half of the cycle graph is data and the other is
English — and each register says so.

## §C.4 · THE RULING LEDGER — three survive, thirteen closed

> ⚠ **SUPERSEDED AS THE OWNER OF THIS COUNT 2026-09-17.** `RR-1` is **closed** at step 2 of `CLAUDE.md`
> §0's gate (irrelevant: no `in_force` walk, no place-keyed clause, so no collision site); `RR-2`
> (`ED-SE-0051`) stays **open and untouched**; `RR-3` **survives**. Round two adds `RR-P`, `RR-A`, `RR-B`
> and `RR-C`. The single ledger is now `../2026-09-17-governance-and-holdings-r2/05_LEDGER_AND_BUILD.md` §6.

**`04` §C.4 and §C.5 are the single owner of both lists. This is the index, not a second copy.**

| | question | owner of the argument | recommendation |
|---|---|---|---|
| **RR-1** | **Policy collision: does the NEARER policy or the HIGHER rank win?** Two defensible options, materially different games — feudal against absolutist. Nothing in the tree decides it, **because no step reads a policy at all** | `01` §C.6 (`ED-IN-0231`, `needs_jordan: true`) | **(a) NEAREST, with a superior's `reach: all` override** — subsidiarity by default, centralism by act. Cost of being wrong: **one comparator line and no data migration** |
| **RR-2** | **`ED-SE-0051` — the bound on the demographic loop: matter only, or matter plus hearth capacity?** Already queued; **Layer 1 is silent**, stated in the row itself | `02` §A.7 | **the CAPACITY arm**, as `capacity(w, rung)` — a Query over DWELLING sites **with a floor**, never a fixture. ⚠ `ED-WR-0011` says the two must be answered **together** |
| **RR-3** | **The zoom-trigger table: adopt the claim-landing replacement, or keep thirteen authored rows?** | `03` §A.7, §C.3 | **(a) adopt.** ⚠ **The weakest of the three**, and `03` argues both halves: the head is `CANONICAL`, *and* it carries a second contradicting `## Status:` line, sits in the retire set, and holds zero `.py` |

**Thirteen candidates were run through `CLAUDE.md` §0's five gates and CLOSED with citations. Do not
re-ask them; `04` §C.5 lists each with its gate and its citation.** ⚠ **This count was itself a
divergence**: `01` listed nine and `04` listed a *different* nine, five in common. The union is
thirteen, and `04` now carries it.

---

# PART D · WHAT WOULD SHOW THIS WRONG

## §D.1 · The claim this whole design stands or falls on

> **A policy changes how a rung FUNCTIONS — the order of a step, the membership of an option set, the
> existence of a date — and never a number added to a roll; and its effect reaches rungs it never
> named, noisily, through one walk.**

**Falsified by** any of: a clause row whose terms bind `amount` or `floor` **and whose reader passes it
to a contest**; a clause for which **no** world exists where flipping its value changes
`World.content_hash()` (then it has no reader and `AX` ID-13 deletes it); a seeded two-arm run in which
the settlement's and the hearth's `stores` are **equal** with the ~~province's~~ **duchy's** `levy:` present and absent (no province rung exists to issue from — §A.5)
(then the walk is not being called); or the distribution of `short` at the hearth being **disjoint**
between arms over ≥30 seeds (then it is arithmetic, not emergence — *this is the row that distinguishes
a design from a spreadsheet*).

## §D.2 · The per-file falsifier suites, and they are prefixed now

`01` ships **SP-1..SP-14**, `02` ships **BW-1..BW-14**, `03` ships **SU-1..SU-15**, `04` ships
**BO-1..BO-10**. ⚠ **Five are expected to FIRE and are shipped anyway**, because `CLAUDE.md` §0.1 pt 3
asks for the test's **outcome** and not for a clean sheet — *a falsifier suite with no expected failures
is a suite that was written after the fact.* The five: `SP-12` (`budget` rises when a person issues a
policy — it does, today); `SP-6` (cannot be written at all until RR-1 is ruled, and writing it first
would pin the fork); `BW-3` (a `hold` on a Site is accepted today); `SU-6` (CALENDAR writes `Date.fired`
with no `emits=`, so the first assertion fails and **the failure is the finding**); `SU-12` (`inferred`
is written nowhere, and the test is written to go red the day the channel is carried).

## §D.3 · The grade is `paper`, and the three cheapest artifacts that would move it

`CLAUDE.md` §0.2: *done means it runs.* **Nothing in this directory executes.** Ranked by cost:

1. **`@effect_for("commit")`** — one effect body on a `grade: ruled`, `own`-eligible, already-formable
   row whose Tenure's subject is the actor, so it is not downstream of the gate. **Artifact:** a person
   `utter`s a Proposition, `commit`s to it, and `questions_for` returns a `need` question about it next
   season — which the corpus already proves carries, since **all 81 of its questions are `need`**.
   *This is the first thing in this suite that could be wrong in public.*
2. **`remit:` evaluable person-side from the holder's own ledger.** **Artifact:** a `Candidate` with
   `verb == "issue"` in some person's option set and absent from a non-holder's. **Control:** the same
   run with the office's `remit_acts` emptied — without it the test passes on a fixture that admits
   everything. It goes **red** against an existing test that asserts the opposite, and that test is
   rewritten as the control.
3. **`found`, with its closer.** **Artifact:** a `rung.founded` and a `site.built` Event in a run's log
   — currently zero and measurable in one grep. ⚠ **A founded Rung has no closer today**, so an
   abandoned hearth is a grain tomb; decide the destroyer or the re-homing rule **in the same commit**
   or the artifact is a leak.

The terminal artifact for the whole subject is `python -m engine.season.harness.register
--requirements` moving **R-04** off `not_met`, whose `measured:` line today reads *"54 of 143 cases are
UNREPRESENTABLE… The strategic layer has no expression in this model."* **Only a run may change that
sentence.**

## §D.4 · What this document is, and the one step it did not take

**This file is reference (`CLAUDE.md` §0.05): delete it and the game behaves identically.** It states
the design once so that an auditor has one object to audit and a reader has one place to start; the
detail, the measurements and the falsifiers live in the four files that own them, and **every one of
them is still the authority for its own subject.**

⚠ **The `§0.4` close gate — `python -m pytest tests/valoria -q -n auto` — was NOT RUN for this
directory**, and the unification pass did not run it either. **It did not need to**: nothing here
touches a `.py`, a roster or a fixture, so no test in the suite can reach these files. Said aloud
rather than implied, per §0's requirement that a skipped step be named. Every number in this file was
re-measured by running the thing that would have shown it wrong, and `README.md`'s measurement block
carries the commands.

---

**END — `00_THE_DESIGN.md`. PROPOSED. HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Grade: `paper`.
No new claim, no new id: `ED-IN-0231`, shared with `01_SEATS_AND_POLICY.md`.**
