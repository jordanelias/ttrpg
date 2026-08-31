# 08 · THE FUNCTION SURFACE — every signature in the system

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L4 — the call layer.** `02_ONTOLOGY.md` says what exists; this says what may be called on it.
## **The enforcement in this shape is not a rule anyone remembers. It is a parameter list that fails.**

---

## §1 · THE THREE, AND WHAT THEY OMIT

```
choose  : (Person, View, Sensation) -> Act        # NO World, ever
resolve : (Act[], World)            -> Event[]    # NO Person
witness : (Person, Event)           -> Claim[]    # per person; a collection is not spellable
```

| signature | the omission | what the omission refuses |
|---|---|---|
| `choose` | **no `World`** | omniscience is not something a reviewer must catch; it is something an author cannot write |
| `resolve` | **no `Person`** | the resolver cannot acquire a per-actor special case, which is how scripting drift begins |
| `witness` | **person first, one event** | consensus broadcast has no signature to be spelled in |

**And the fourth function, which is not a decision function and therefore may take a world:**

```
sense : (Person, frozen_world) -> Sensation       # two scalars, computed, stored nowhere
```

**`sense` is the ONLY bridge from world truth into `choose`'s arguments, it returns exactly two floats,
and it is called at exactly one site.** That single call site is the convention's home, and it is where
the constraint is documented — because [engine] a value type prevents **widening**, not **substitution**.

---

## §2 · THE QUERY CATALOGUE — the side column IS the enforcement

**A `Query` is never stored and always recomputed. Two classes, and the split is enforced by the
parameter list rather than by a table a reader must honour.**

### §2.1 Resolver-side — `World` FIRST, always

**Calling any of these from inside `choose` fails at the call site for want of an argument.**

| # | signature | returns | notes |
|---|---|---|---|
| 1 | `leaders(w, prop, rung)` | Person[] | resolver-side, **for the resolver only.** Comparator: *commitment degree x backing raisable*. **Deposition is this returning somebody else** |
| 2 | `presence(w, prop, rung)` | int | barrier-built index; never a scan per call |
| 3 | `density(w, prop, rung)` | ratio | |
| 4 | `footprint(w, prop)` | Rung[] | a faction's extent — **derived, never a `scale` field** |
| 5 | `sovereign_fraction(w, root)` | **(fraction, undetermined_count)** | **a PAIR, because the conferral graph is not total** — §2.3 |
| 6 | `condition_at(w, rung)` | int \| **undefined** | coarse read; **undefined at a Rung with no Sites**, and the verb gate does not fire |
| 7 | `verbs(w, site, c)` | **Verb set** | **world truth**, as against `opening_set`'s claim-derived account |
| 8 | `judging_set(w, rung, act)` | Person[] | who hears what happened here |
| 9 | `draw_share(w, site, person)` | ratio | barrier-built denominator |
| 10 | `share(w, actor, site)` | ratio | |
| 11 | `filter_share(w, channel)` | ratio | **derived volume — how much of what travels a channel a given person controls.** This is what makes an under-steward with no standing structurally outrank a minister |
| 12 | `capacity(w, date)` | int | **the one cap**; `seat_items` is deleted |
| 13 | `enforcer_presence(w, dispensation, rung)` | int | what compliance reads |
| 14 | `hold_force(w, rung, targets, giver)` | int | raisable coercive force. **Named with its arguments, never as a bare token** |
| 15 | `establishment_of(w, office)` | Person[] | |
| 16 | `conferral_path(w, office)` | Office[] \| **cycle** | **iterative, with a visited set** — the graph cycles on purpose |
| 17 | `retention(w, facet)` | ratio | **the obstacle owner for investigation: the world sets it, as facet decay.** Nobody adjudicates difficulty |
| 18 | `docket_of(w, date)` | DocketItem[] | |

### §2.2 Person-side — takes the asker, and may read the asker's **own interior** and nothing else

**These take no `World` and cannot acquire one.** *Their read scope is the asker's ledger, stance,
capability and remits, plus the `Sensation` computed this step* — **not the ledger alone**, which is a
tidier-sounding claim than the design can make and would leave `opening_set` unable to work.

| # | signature | returns | notes |
|---|---|---|---|
| 19 | `assemble(person, question)` | View | **built, not filtered.** At most `K` claims |
| 20 | `opening_set(person, view)` | **Candidate[]** | **claim-derived.** May be wrong — that is the discovery mechanism. **NOT `Act[]`**: typing it as acts makes the option set an authored list rather than a computed one |
| 21 | `entrenchment(person, holding)` | ratio | read off `since`/`until`, never ticked into anything |
| 22 | `norm_as_claimed(person, referent)` | ratio | **their estimate**, from their own ledger. **Nobody may read the true profile** |
| 23 | `address(person)` | Rung[] | the derived view of their one `contain` Tenure |
| 24 | `trace(person, claim)` | provenance tree | **a view, not a store** — *only as good as what they went and got* |
| 25 | `need(person, kind)` | (Proposition, urgency)[] | **ranked, never summed** (`07` §3.1) |
| 26 | `leaders_as_claimed(person, prop, rung)` | Person[] | ⚠ **REQUIRED, and it is not a convenience — see below.** What *this observer* takes the leadership to be, from their own ledger |

> **THIS CATALOGUE IS 26 ROWS — 18 RESOLVER-SIDE (1–18) AND 8 PERSON-SIDE (19–26).** With the three
> top-level signatures, **21 call sites fail for want of an argument** if a decision function reaches for
> world truth; the 8 person-side rows are enforced by the opposite omission — they take no world and
> cannot acquire one. **It converts a table a reader must remember into a call that does not compile.**
>
> ⚠ **DO NOT QUOTE AN ADDITIVE TOTAL.** A figure of *"23"* circulates in three places over a
> differently-scoped table of 20 rows, and it is `3 + 20` — **a sum that names nothing.** An earlier
> draft of this line said *"3 to 28"* — **the identical error, re-minted with a new number.** Name the
> catalogue and its two sides.

>  ⚠ **AND `leaders` NEEDS ITS PERSON-SIDE TWIN, OR COVERT MEMBERSHIP LEAKS AT THE ONE SEAT IT EXISTS
> FOR.** A `commit` edge carries an **avowal** of `avowed | private | covert` (`02` §4.2). A
> resolver-side `leaders` reads the **true** edge set — which is a true-profile read, **and nobody may
> perform one.** The prior design typed the flat form exactly this way and recorded it as a defect.
>
> **So there are two queries, not one.** `leaders(w, ...)` is the world's answer, callable only by
> `resolve`. **`leaders_as_claimed(person, ...)` is what an observer believes**, computed from their own
> ledger — and every consumer that is not the resolver takes the second. **Underestimation is the
> default, a covert cell reads as smaller than it is, and discovering otherwise costs acts.**

### §2.3 The one signature that changed shape, and why

`sovereign_fraction` returns a **pair**, not a float.

**Because `Office.conferral.basis` is per-office** (`02` §2.3.2), the conferral graph is **not total**:
person-rooted chains terminate at dead conferrers, and external roots leave the peninsula entirely. **A
bare float would have to invent a value for the undetermined part**, and every caller would silently
inherit the invention.

**Returning the undetermined count forces every caller to handle a partial answer** — and it turns what
was filed as a defect into a first-class political condition: **a contested succession means no
determinate custody, which means the deciding article is ungradable for every claimant, which means the
sitting closes carried-without-force.** *That is the crisis, expressed as a return type.*

---

## §3 · THE ACT VOCABULARY

**The verb space is OPEN. The mode space is CLOSED.** An act names a verb for readability; **the
resolver reads `changes[]` and never branches on the verb, and never on an Event's kind.**

```
Act := (id, actor, verb, changes[], reads[], contests[], payload)
```

| field | what it is for |
|---|---|
| `changes[]` | the `StateChange` triples this act proposes. **This is the mechanism** |
| `reads[]` | what the act consulted, **so the conflict graph can see it** |
| `contests[]` | what it disputes, **so the contest router can route it** |

### §3.1 The five remit modes — closed, and they add no verb

**`issue` · `determine` · `confer`/`revoke` · `dispatch` · `convene`.** Each is an ordinary act made
eligible somewhere it otherwise is not. **An office adds no verb and no bonus. It changes two things:
the OPTION SET, and the POOL SOURCE.**

### §3.2 The act families — open, and each is ordinary

| family | acts | available to |
|---|---|---|
| **material** | `work`, `build`, `found`, `transfer`, `levy`, `forestall`, `hoard`, `migrate`, `settle_in_full`, `take_opening` | anyone |
| **epistemic** | `examine`, `interview`, `research`, `surveil`, `reconstruct`, `Thread-Read`, `tell`, `plant`, `cover`, `counsel` | **anyone. Eligibility never consults office** |
| **political-up** | `petition`, `carry`, `forward`, `amend`, `bundle`, `drop`, `back`, `supplicate`, `withdraw` | anyone |
| **political-down** | `issue`, `determine`, `publish`, and at the receiving end `comply`, `evade`, `defy`, `refract` | issuing requires a remit; **receiving does not** |
| **argument** | `plead`, `press`, `descend`, `produce`, `object_to_venue`, `yield`, `propose`, `counter`, `probe` | anyone may enter; **speaking needs standing or a carrier** |
| **coercive** | `force(actor, targets, form, warrant)`, `refuse_levy` | anyone; `warrant in { office, custom, none }` |
| **relational** | `admit`, `expel`, `form_knot`, `rupture`, `requisition`, `marry`, `found_hearth`, `foster`, `disinherit`, `legitimate` | anyone, at the rungs where each is defined |
| **institutional** | `confer`, `revoke`, `dispatch`, `convene`, `compose_agenda`, `subremit` | requires a remit — **except `convene`, which any person holds over their own kin** |

**One act per person per season, drawn from any family.** Investigation costs a season exactly as a
levy does, and **that is what makes an investigation a decision rather than a free action.**

### §3.3 The six investigation acts — and why the layer needs no score

| act | pool | produces | cost / risk |
|---|---|---|---|
| `examine` | Acuity + practice, vs `retention` | `firsthand` facets still persisting | **you are witnessed examining** |
| `interview` | Charisma \| Attunement vs obstinacy | their `SAID` row — **which may be a lie** | **they learn what you are asking**, and can tell others |
| `research` | Focus + literacy | `told_by(record, ...)` with **verified** rootprints | access is an **admission gate held by persons with stances** |
| `surveil` | Agility \| Focus vs concealment | `firsthand` over the interval | duration; **exposure accrues to you** |
| `reconstruct` | Acuity + Will | `inferred` claims and **root identification** | no world risk; **a WRONG reconstruction deposits at real confidence and is acted on** |
| `Thread-Read` | Thread Pool + Attunement | rendering-side facets | Coherence risk; **it produces claims most people cannot be told** |

> **INVESTIGATION'S CURRENCY IS THE `SAID` ROW, WHICH IS WHY IT NEEDS NO SCORE.** A telling deposits
> `SAID(speaker, content, when, place)` **unconditionally, on every outcome** — *doubting a man does
> not unhear him* — so a diligent interviewer accumulates a graph of who said what to whom.
> **There is no clue counter, no case object, no investigation skill, and no threshold anyone sets.**

**Nobody adjudicates difficulty.** `retention` decays with the facet's age and kind, less what was spent
concealing it. **The world already emitted what it emitted, and time is eating it.**

**And `research` is the one gated act — gated by an ADMISSION held by persons**, which a person with no
post routes around three ways: interview an archivist, use a deep channel to someone with access, or
steal. **Every gate is a person, so every gate has a price and a grievance.**

---

## §4 · CONFLICT, AND THE ONE ROUTER

```
conflict(a, b)  iff  a and b share a subject AND
                     ( either contests it
                     | both alter the same `exclusive` field
                     | both create edges that jointly break a declared cardinality )
```

**The third clause is the one that is easy to omit and expensive to omit.** Without it, two succession
pointers on one hearth, two holders of one office and two addresses for one person are **each
individually legal, no conflict fires, and the invariant breaks only after both resolve.**

**Additive vs exclusive is declared per field, and the default for an undeclared field is `exclusive`** —
the safe direction, because an undeclared additive field silently accepts concurrent writes.

**Everything that conflicts routes to `contest`** (`09_THE_SEAM.md`). **One function, three call sites,
no second resolver.**

---

## §5 · THE RESOLUTION KERNEL

```
roll_pool(pool_size, ob)          -> RollResult        # d10s; TN is 7, ALWAYS
derive_ob(target_score, mods)     -> max(OB_MIN, target_score/2 + mods)
degree_from_net(net, ob, ext?)    -> Degree            # FOUR bands, on the MARGIN
```

| | |
|---|---|
| **the die** | face 1 = **−1**; faces 2–6 = 0; 7–9 = **+1**; 10 = **+2**. `mu = 0.40`, `sigma = 0.800` per die |
| **TN** | **7. Always.** A varying difficulty is an **Ob**, not a TN, and the owner **raises** on any other value |
| **the ladder** | `margin = net − ob`; **Overwhelming ≥ 3 · Success ≥ 1 · Partial [0,1) · Failure < 0** |
| **the extension** | a subsystem's wrapper may **veto an Overwhelming** and may do nothing else |
| **the floor** | `OB_MIN`; **an uncontested attempt routes to a GATE, never to an `Ob = 0` roll** |

> ⊕ **`derive_ob` DOES NOT EXIST AND IS OWED.** The ruling — *the obstacle is their corresponding
> score/2 plus whatever specific modifiers exist for them in that instance* — is quoted inside the
> owner with its own **"IMPLEMENTED NOWHERE"** warning, and **two independent design lines converge on
> the same formula.** Build it beside the roller, **as the owner for NEW obstacle sites only**: three
> existing sites diverge, their reconciliation is suspended, and one of the three is stated as canon.
> **Adding a fourth convention while three disagree is how a fifth arrives.**

> ⊕ **AND THE TWO DICE, WHICH ARE NOT ONE DIE WITH AN ERROR IN IT.** The design line declares a die
> with **no botch face** (`mu = 0.5`, `sigma ≈ 0.671`); the executing owner's die scores face 1 as
> **−1** (`mu = 0.40`, `sigma = 0.800`). **Both constants are exact for their own die**, so `0.671` is
> not a mistake to be edited out — it is a different model. **This shape adopts the executing die, and
> that is a declared departure** (`15_ADJUDICATIONS.md` R-18), which changes `mu`, `sigma`, **and
> whether a 1D pool can net below zero.**

---

## §6 · WHAT NO SIGNATURE IN THIS SHAPE MAY BE

| forbidden signature | why |
|---|---|
| `f(World, Person) -> Act` in any form | Law 2; **the whole epistemic layer becomes decoration** |
| `view_of(World, Person) -> View` | someone eventually masks nothing. **`assemble(person, question)`** |
| `f(Person[], Event)` | consensus broadcast; divergent perspective dies |
| `deposit(cohort, value)` | **the row that passed every other guard** — a cohort deposit carries a **distribution** |
| `resolve_fast(...)`, `auto_resolve(...)`, `summarize(...)` | a second resolver whatever it is called |
| any resolver-side Query without `World` first | it becomes callable from `choose` |
| any function with a `faction` parameter that acts | Law 1 |
| `contest(...)` without a caller-supplied `max_depth` | a fabricated constant, and [engine] a crash rather than an error |
| a getter that memoizes inside the parallel map | **a data race AND a stored aggregate at once** |
| anything that reads the event log from inside a decision function | **it is the World, re-entering by the back door, and it will not look like a violation at the call site** |
