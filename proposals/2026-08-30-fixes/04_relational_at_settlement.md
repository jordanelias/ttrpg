# 04 — Relational at Settlement and Territory

## Status: PROPOSED (2026-08-30) — a fix, not a system. Nothing here ratifies on merge.
## Fixes: `09_GAP_REPORT.md` **D-4** (Relational EMPTY at two consecutive rungs) and **D-5** (a councillor
## has nowhere to stand). Resolves collision **S6**; parameterises **S18**; makes **V19** a table row.
## Composes on: `01_substrate.md` §1.1, §4, §6 · `04_hearth_and_community.md` §4.2, §5, §6, §8, §9
## `08_argument.md` §10 · `12_coercion_and_force.md` §9 · `14_office_and_upper_rungs.md` §1.1, §2.3, §5
## `15_adjudications.md` B-1, B-5
## Sibling fixes filed alongside: `01_the_floor.md` (D-1) · `02_the_act_economy.md` (D-2) ·
## `03_the_missing_needs.md` (D-3) · `05_the_blocked_cores.md` (the §1 headline). Not duplicated here.
## Adds: **one conferral row, four venue rows, and one field derived rather than declared.** No new object, no new act.

---

## 1. The question the report asks, answered by derivation

> *"Ask whether Settlement-scale belonging is genuinely a different thing from Community-scale belonging,
> or the same mechanism at a different rung — and derive the answer rather than asserting it."*

### 1.1 The derivation

Read what each rung owns, in the spine's own words.

**Community owns peer judgment and the admission gate** (01 §4). Its defining property is that its members
know each other's faces: the judging set is *who hears*, and admission is *an act, performed by persons who
already hold standing in the community*.

**Settlement owns the contested zero-sum stake and the first office** (01 §4), and 14 §1.1 states exactly
why the office comes in there:

> *"Settlement is where office first exists in the substrate's sense because it is the first rung whose
> stake is zero-sum across communities that did not admit each other, which is the first place
> `binds = persons-by-presence` is a coherent thing to want."*

Read that against the question and the answer is forced. **Settlement is defined as the rung where belonging
is not by admission.** A settlement that had an admission gate would be a rung whose members had admitted
each other — and `binds = persons-by-presence` would collapse into `members-by-admission`, deleting the one
thing the Settlement rung owns.

> **Ruled: belonging at Settlement and Territory is DERIVED, not conferred. Admission is owned once, at
> Community, and the upper rungs read it.**
>
> ```
> member(p, settlement s) ⟺ address(p) passes through some community c whose parent is s
> member(p, territory t)  ⟺ address(p) passes through some settlement whose parent is t
> ```
>
> One line each. No state, no gate, no roster. Same mechanism, read one rung up.

So the matrix's EMPTY is **half correct and half a category error**, and separating the halves is the whole
of this document:

| what the matrix looked for at Settlement | verdict |
|---|---|
| an admission gate | **must not exist.** Its absence is the rung's identity, not a hole. |
| a judging set rule | **already exists as a derivation.** `JS(act) = { p : hears(p, act) }` (04 §4.1); `publicity ≥ 1.5` reaches settlement-wide by the table's own row. A settlement-scale judging set is produced by publicity, not by membership — which is why a court sitting has one and a workshop does not. |
| a Knot mechanism | **category error.** A Knot is person-to-person (01 §2). It has no rung, and asking for one at Settlement is the matrix's axis forcing a question the object does not answer. |
| an obligation edge | **filed one column over.** 04 §1.4's edges are kin relations owned by the Hearth; the Settlement equivalent is `dispatch` (requisition on an establishment member, 14 §1.1), which is Institutional and is DEMONSTRATED there. |
| a way *in* | **genuinely missing. This is the defect.** |

### 1.2 So what is actually broken

Not an empty rung. **An asymmetric primitive.**

`12 §9`'s `Force` form set is `{seize, restrain, strike, burn, expel, disperse, kill}`, and its table reads:

> *eviction · `expel` · office or custom · changes the target's **address**, which is a containment edit —
> the most severe thing you can do to a person short of killing them.*

So the design **does** have a settlement-scale operation on an address. It has exactly one, it is coercive,
and it is one-directional. An office that can edit an address outward cannot edit one inward.

And the design already noticed the gap without filling it. 04 §9:

> *"`migrate(person, destination)` is an act **requiring admission at the destination** or the founding of a
> hearth there."*

For a destination that is a *community*, 04 §6's table supplies the gate — guild, hamlet, parish, chapter.
For a destination that is a **settlement**, there is no row, no committee and no coefficient vector, so the
stated precondition points at nothing. And "founding a hearth there" needs a portion of holdings, which is a
stake the settlement allocates — so a person with no holding has no second route either.

**The class of person this excludes is exact and it is the same population D-1 and D-10 are about:** the
landless, the expelled, the discharged, the fled, and the refugee. There is no legal way for any of them to
acquire an address anywhere.

---

## 2. The fix at Settlement — one conferral row

### 2.1 Re-target `admit()` a third time

`04 §4.2` defines admission once:

```
admit(committee, candidate, X) -> event conferring a mark and (optionally) an address

support(m, candidate) = α·Σ_marks stance(m→referent)·weight + β·performance
                      + γ·Σ_sponsors standing·staked_regard + δ·stance(m→candidate)
verdict = aggregation_rule over { support(m) : m in committee }
```

`14 §2.3` already re-targets it once, from a community to an **office**, keeping the four coefficients and
the rule that *α, β, γ, δ are weights and never signs*. This document re-targets it a second time, at a
**settlement's residence stake**, and adds one row to `14 §2.3`'s table:

| conferral | committee | α | β | γ | δ | rule |
|---|---|---|---|---|---|---|
| **residence, by a settlement court** | the praefect, with assessors' stances weighting (14 §5) | **1.2** | 0.3 | **1.0** | 0.5 | his determination |

The committee is not new: `14 §5`'s venue table already gives the Goldenfurt settlement court a convener,
a door, a decision rule and standing dates. The mark conferred is `resident of Goldenfurt` — **which is
exactly the mark `expel` removes.**

Read the coefficients the way 04 §6 says to read them, off the arithmetic rather than off a rule:

- **α is the largest term**, because what a gate warden reads is heritage, and a stranger is nothing but his
  marks until he has done something here. A settlement whose assessors hold hostile stances toward Einhir
  heritage keeps the hamlet outside the wall without a single rule saying so.
- **β is nearly dead**, because a stranger has performed no work at this container yet. This is the one gate
  in the peninsula where the Löwenritter's trick — let the deed drown the mark — is structurally unavailable.
- **γ is real**, because a settled town's actual demand of a newcomer is that a resident vouch for him, and
  γ is *sponsors staking regard.* A person with no tie into the settlement scores zero on the only term that
  could rescue him from α.
- **δ moderate**, because a praefect who simply likes a man may let him in, and that is a scandal
  attributable to a named person — the same shape 04 §6 derives for the single-assessor Church gate.

**And the evasion reappears unbidden, which is the best evidence the object is the right one.** 04 §5 found
that raising β at a guild changes nobody's stance, so a committee that wants to exclude routes the same
exclusion through γ and δ. A Crown dispensation ordering settlements to admit on need rather than on
heritage would lower α — and the court would refuse through γ (*no burgher will vouch*) and δ (*personal
dislike, unfalsifiable*). Nobody designed that. It is what happens when you write one formula and let
someone edit one coefficient.

### 2.2 Residence is a stake, and it is the settlement's most characteristic one

The spine allows a container to hold **stakes, judging sets and dates** and nothing else (01 §6). B-1
already allowed the admission vector at Community *as a stake*, on three tests: it is contested, it is
allocated at standing dates, and factions fight over it exactly as they fight over grain. Residence passes
all three, harder:

- **Contested.** 01 §4 defines the Settlement rung by a zero-sum stake — *the granary opens for the hamlet
  or for the Row, not both.* Every admitted resident is another mouth in another claimant hearth, competing
  for the same allocation.
- **Allocated at a standing date.** The court's sitting, which the venue table already carries.
- **Factions fight over it.** The Row wants the Einhir kept outside the wall. The hamlet wants the wall
  opened. That is the oldest fight in the setting and the design had no object for it.

> **Residence is the stake that meters every other stake**, because it is the only allocation that changes
> who the *other* allocations are divided among. The design had it as a coercive verb and nothing else.

**No new container state.** The settlement holds one more `(α, β, γ, δ, rule)` row — the same object B-1
allowed at Community and 14 §2.3 allowed for offices. The *number* of residents stays a query:
`|{ p : address(p) passes through s }|`. Nothing is stored, counted or capped.

### 2.3 The pair is now symmetric, and the asymmetry that remains is deliberate

```
admit(court, candidate, residence)  →  address edit inward,  at a venue,  by determination
Force(expel, target)                →  address edit outward, by force,    12 §9
```

Two ends of one containment edit. Both verbs already existed; only one had been pointed at this rung.

They are **not** symmetric in cost, and that is correct rather than sloppy: a praefect can evict with the
watch and must sit a court to admit. That is what a wall is. §6 records the long-run consequence.

### 2.4 Closed loops and N-lines

**`admit(·, ·, residence)`**
- *Loop.* Produced by a settlement court's determination at its standing date; carried as the candidate's
  address change plus a `resident of s` mark naming the court as source; consumed by every subsequent
  judging set, by `expected_standing` (04 §2.1), by `contest`'s capacity term at the node, and by
  `Force(expel)`, which is its negation.
- *N-line.* Cut it and nobody can be taken into a settlement. The landless, the expelled, the discharged and
  the fled have no legal address anywhere; `migrate`'s stated precondition points at nothing; and the only
  settlement-scale membership act in the game is a coercive one — which makes every walled town a trap that
  fills only by birth and empties only by force.

**Residence as a stake**
- *Loop.* Produced by the settlement's own carrying capacity — `draw` against `mouths` across the hearths
  inside it; carried as an allocation at the court's date; consumed by admission, by expulsion, and by every
  faction computing capacity at the node.
- *N-line.* Cut it and the granary is contested by a population that cannot change. The settlement's
  defining zero-sum stake has a fixed denominator, and there is no politics about who is inside the wall —
  which is most of the politics of a walled town.

---

## 3. Territory

Run the same derivation one rung up and it comes out differently, which is how you know it is a derivation.

Territory owns **reach**, and 14 §3.1 says what that means: *"Settlement office acts where the holder
stands. Territory office acts where it sends someone."* A territory has no wall and no granary of its own;
its stake is *a roster of persons rather than a thing in a place.* So there is nothing at the Territory rung
for a residence stake to meter, and membership is derived from its settlements by the line in §1.1.

> **Territory × Relational is N/A-by-derivation, and should be marked so rather than filled.** The matrix
> looked for a gate at a rung whose belonging is computed and recorded the absence as EMPTY.

Two things genuinely live in that cell and are filed elsewhere, which is worth stating so nobody fills it
twice:

1. **A territory office's establishment is a membership set at that rung** — entered by `confer`, exercised
   by `dispatch`, left by `revoke`. That is Institutional, and it is DEMONSTRATED there (Holdar, Voss).
2. **Banishment from a territory** is `expel` at larger scope — a dispensation term rather than a single
   Force act. Under §2 its inverse is the same `admit`, determined by the territory office. **One optional
   row, same shape as the settlement row**, offered rather than pressed: the settlement row is the
   load-bearing one and the territory row is a convenience for a duke who wants a man back.

---

## 4. D-5 — a councillor has nowhere to stand

The most populous character type in Valoria, in no venue table (S18): the Varfell Jarl Council and the
Hafenmark Inner Council. The report suspects this is the same fix as D-4. It is the same *method* and a
different object, and the derivation is short.

### 4.1 Is a council a community, a venue, or both?

**Not a community.** 01 §4 supplies its own test: *"A cell people live in is a community; a cell people
belong to while living elsewhere is a faction… you cannot hide where you sleep."* Councillors live
elsewhere. Nobody's address changes when they take a seat, and no mark is conferred by the council — the
mark comes with the office.

**Not a faction.** A faction *is* a proposition (07 §1.1). A council has none; its members disagree, and
that disagreement is its function. A body whose identity was a proposition could not hear a motion against
itself.

**A venue.** `08 §10`'s tuple is `(container, prize, standing_date, judging_set_rule, decision_rule,
admission_floor, privileged_custody, exchange_budget, article_count, coupling_depth, veto_holders,
record_custody)`, and `14 §5` adds the door: `(convener, enter, speak, admissible_source, attendance_cost)`.
A jarl council has all of them, and needs nothing else.

> **A council is a VENUE whose door predicate reads an OFFICE. Its seats are the container's office-prizes,
> already contestable through `contest(container, offices, claimants)` (04 §8). It is not a community, has
> no admission gate, and holds no state.**

So a councillor's "nowhere to stand" was never a missing mechanism. It was **four missing table rows.**

### 4.2 The rows — `14 §5` (the door)

| venue | convener | ENTER | SPEAK | DECIDE | admissible source | standing dates |
|---|---|---|---|---|---|---|
| **Varfell Jarl Council** | the Duke sets the **date only**; item order runs by seniority of deed | seat-holding jarls and their attendants | seat-holders only | majority of seats | witnessed deed and instruments | the muster reckoning; extraordinary on a jarl's vacancy |
| **Hafenmark Inner Council** | Duchess Inge Baralta | those the Duchess summons, plus the Compact's two standing seats | summoned members and seat-holders | the Duchess determines; members' stances weight it | instruments and sworn testimony | monthly; extraordinary on a Crown vacancy |

### 4.3 The rows — `08 §10` (the room)

| Venue | Judging set | Decision rule | Floor | Privileged custody | Veto |
|---|---|---|---|---|---|
| **Varfell Jarl Council** | seat-holding jarls present | majority of seats | G2 | the Council's own muster rolls | **none** |
| **Hafenmark Inner Council** | those summoned, present | the Duchess determines | G1 | the ducal chancery | the Duchess |

### 4.4 Read the two rows against each other — V19 becomes arithmetic

The Jarl Council's `convener: date only` and `veto: none` are not flavour. They are **derived from the
conferral graph**, and they are the mechanical statement of V19 (*"Varfell is structurally not a duchy"*):

> 14 §5 says *"the convener holds the cheapest real power in the game… a convener who puts three items ahead
> of yours has spent nothing and killed your petition."* That power comes from having conferred the seats.
> Vaynard did not confer the jarldoms — they are heritable deed-seats with no living conferrer (14 §1.5's
> last two rows) — **so he holds neither item order nor a veto over his own council.** Baralta, whose Inner
> Council she summons, holds both.

One heritable-versus-appointed field, two duchies that play completely differently, no special case
anywhere. And it explains, without asserting, why the matrix records Baralta as *convener and veto-holder →
CARRIED-WITHOUT-FORCE* while Vaynard's own council is a room he can only call to order.

### 4.5 Closed loop and N-line

- *Loop.* Produced by `convene` setting the standing date (14 §1.1's closed five); carried as the venue
  parameter row plus the seat offices held on persons; consumed by 08's case machinery — motion, grounds,
  stasis ladder, graded proof, the record — and by `contest` when a seat falls vacant.
- *N-line.* Cut the rows and the two most populous decision bodies in Valoria can neither hear a motion nor
  allocate a prize, so a councillor holds an office whose remit is exercisable in no room. Every jarl and
  every inner councillor is a person with binding power and nowhere to use it, which is what the matrix
  measured.

---

## 5. Dominance check

**Does `admit(·, ·, residence)` dominate for a praefect?** Gain compounds: every resident is a person at his
node — capacity in `contest`, a mouth in the tithe, a hand at the wall. Three costs, all compounding, and
they are arithmetic rather than rules:

1. **He raises the denominator on his own supporters.** Each admitted hearth is another claimant against a
   fixed granary allocation, so `04 §1.2`'s margin falls for *every* hearth inside the wall, his own
   backers' included. A praefect who admits freely manufactures the subsistence needs that produce the
   petitions he will have to drop.
2. **The stance is not his.** 04 §5: *"a settlement cannot be made loyal. There is no field to write."* He
   admits a person whose capacity will be counted in whichever faction that person commits to — and 04 §9
   says an outsider arrives with high grievance and no carrier, which is the Restoration's exact recruiting
   profile.
3. **He cannot do it quietly.** 14 §1.3: every act by remit runs at `venue_factor ≥ 1.0`. Each admission is
   read through the candidate's marks by the whole settlement's judging set, so a praefect who admits Einhir
   hearths pays in the Row's stance tables every single time.

**Compounding gain against compounding cost, with the crossing point at how tight the granary is.** Not
dominant, and the fork it creates is the political fork of a walled town, which the design did not have.

**Does a council seat dominate?** The convener power is the cheapest real power in the game, and the two
rows **split it**: at Hafenmark one person holds date, item order and veto; at Varfell the equivalent office
holds only the date. So the same seat is worth different amounts in two duchies for a reason a reader can
trace to one field, which is the opposite of dominance.

**Does the venue door dominate an argument?** No: 08 already owns the weighing. 14 §5's own claim holds —
*a door is a predicate and a verdict is a weighting* — so adding rows adds rooms, not power.

---

## 6. WHAT THIS MIGHT BREAK

**6.1 B-1's stake claim is now load-bearing twice.** The admission vector was allowed at Community as a
stake, flagged by 04 §12 as the place that document strained the spine. Settlement relational now rests on
the same ruling. If a later pass decides the vector is container memory after all, it no longer costs one
guild gate — it takes the whole in-door with it.

**6.2 The settlement needs a `mouths` roll-up it has never needed.** §5's first cost is felt through the
`contest` allocation rather than through a new settlement-level larder, which is deliberate. But somebody
implementing it will be tempted to write `mouths(s)` and then `draw(s)`, and 13 §4's `supply(good, s)`
already exists at that scope. **Two settlement-scale material quantities that could disagree** is exactly
the second-copy failure 01 §6 refuses. Check them against each other before both exist.

**6.3 The Territory ruling contradicts a lane, and its correctness depends on an unresolved canon question.**
Lane 3 asked for territory relational content; I am ruling the cell N/A-by-derivation. But if the jarldoms
are heritable (V19, open), a jarl's seat is attached to a *hearth* seat, and 04's hearth-scale relational
machinery reaches the Territory rung the way Baralta's legitimation reaches the Duchy rung — borrowed,
exactly as doc 01 predicted. **So Territory × Relational is N/A under one branch and borrowed-live under the
other**, and which it is is not mine to settle.

**6.4 A settlement court that can admit can be forum-shopped.** 08 §2's rung 4 (*this chamber may not hear
it*) gains a new object: a candidate refused residence at Goldenfurt petitions Kronmark's court instead, and
the two courts' α rows differ. That is probably good and it is new surface nobody has costed, including how
a first refusal enters the second court's record.

**6.5 The net flow of a hostile court is outward.** `expel` is Force, cheap and immediate; `admit` is a
determination at a sitting. Over a long campaign a settlement with a hostile bench can depopulate with
nobody deciding to — the same shape as 04 §9's *"an excluded member is a leak with no loyalty"*, running at
the rung above. It may be correct; it is unbounded, and nothing currently notices.

**6.6 S6 is resolved here as a by-product, and the resolution should be read as a claim rather than a tidy-up.**
*Is a Restoration cell a faction, a community, or a venue?* Under §4.1's test: **the Movement is a faction,
a cell people live in is a community, and a cell that sits is a venue** — three objects, three names, one
person in all three, which is exactly the parish priest's shape in 14 §7. That settles the collision the
way the design's own precedent settles it. It also means `08 §10`'s existing consensus-cell row was always
live, which has a consequence for a blocked character that document 05 collects.

**6.7 Two of the four coefficients in the residence row are guesses.** α 1.2 and γ 1.0 are chosen to make
the gate behave the way the setting describes a walled town behaving; nothing derives them, and the caste
behaviour of every settlement in the peninsula reads off them. They should be attacked before they are
copied.

---

*One conferral row, two venue rows in each of two documents, one field derived rather than declared. The
admission gate stays where the spine put it, at Community, and the upper rungs read it. What was actually
missing was the inverse of an act the coercion document had already shipped.*
