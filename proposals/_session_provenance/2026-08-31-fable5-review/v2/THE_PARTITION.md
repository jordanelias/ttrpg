# THE PARTITION — Jordan's rule for what drives a state change (2026-08-31)
# Verbatim: "Think in terms of state changes. If the state change corresponds to an aspect of human
# society as limited to the peninsula (polities, institutions, offices, organizations, occupations,
# religion, settlements, marriage, etc) then it is driven by character choices. If the state change
# does not correspond to an aspect of human society, like weather or non-peninsular like Altonian
# Empire or tears in metaphysical substrate, then it is still an event that acts upon the game world."

## THE RULE, stated once

> **Partition every state change by its SUBJECT.**
>
> | the subject of the change is… | the change is driven by |
> |---|---|
> | **peninsular human society** — polities, institutions, offices, organizations, occupations, religion, settlements, marriage | **a character's choice. Always. No exceptions.** |
> | **anything else** — weather, the non-peninsular (the Altonian Empire), tears in the metaphysical substrate | **an event acting on the world** |

**This replaces an enumeration with a principle**, and that is the whole of its value. `SUP:1633-1643`
licensed *"these four, and only these four"* decider-free channels with **no test for membership** — so
the list could not be checked, could not be extended, and was wrong three ways at once: matter events
were licensed with **nothing that generates one**, `wear` was unwritable, and a 58-card event deck had
no home. **A partition on the subject is decidable, so every future case answers itself.**

## THE NO-FALLBACK RULE IS NOW TRUE INSTEAD OF APPROXIMATELY TRUE

`SUP:1600-1605` reads *"if no person acts, the thing does not occur."* As written that is false — the
world has weather. Correctly scoped by the partition:

> **If no person acts, no SOCIAL thing occurs.** Non-social change occurs regardless.

**That is a stronger rule, not a weaker one**, because it is now exactly true and its domain is named.

## WHAT IT SETTLES, CASE BY CASE — each was open or wrong

| case | prior state | under the partition |
|---|---|---|
| **`wear` on a site** | proposed as a special case an hour ago | **an event.** A harbour silts because harbours silt. **Tending it is a choice.** Both move one quantity, which is precisely Jordan's flux model, and the partition explains why without special-casing either |
| **the Altonian Empire** | ⚠ **I RULED THIS THE OTHER WAY AND WAS WRONG.** `FORKS.md` F5 said *"generate persons, and take no exception"* | **an event source.** Off-board polities are non-peninsular by definition, so they act as events. **No off-map realm needs simulating**, which is a large deletion, and §1.1 is preserved *properly* rather than by straining — §1.1 governs persons, and Altonia is not a person |
| **the event deck** | zero citations in three documents; no home in the architecture | **the event channel's content.** It needs no licence beyond the partition's second row |
| **tears in the metaphysical substrate** | absent entirely | **events.** The Thread layer gains a channel it never had |
| **a body ageing and failing** | licensed as "metabolism", channel 1 | **an event** — biology is not a social aspect |
| **a person being killed by Aldwin** | same channel, indistinguishable | **a choice.** The subject test separates what the old enumeration could not: *this body failed* and *this man was murdered* are different changes with different drivers |
| **marriage, legitimation, fostering, succession-naming** | acts | **choices**, confirmed — Jordan lists marriage by name |
| **birth as demographic weight** | conflated with birth-as-act | **an event.** The envelope moves; *whose* child is legitimate is a choice. This closes the write-class contradiction the checker filed as MJ-4 |
| **founding a settlement · establishing an office · founding a faction · conferring a role** | `mint`/`efface` acts | **choices**, confirmed — all are named society aspects |

## THE ARCHITECTURAL CONSEQUENCE

**`Event` becomes a first-class source alongside `Act`, not a list of exceptions.** The engine has two
change-drivers and the partition says which applies:

```
Act   : a character's choice          -> state changes whose subject is peninsular human society
Event : the world acting on itself    -> state changes whose subject is anything else
```

Both resolve through the same machinery — witnessed by presence, per person, claims deposited by the
ordinary rules — so **an event is as disputable as an act**, which the epistemic layer needs. Nobody
agrees about the weather either.

⚠ **What must NOT be inferred.** The partition does **not** license an event that changes a social
quantity. An event may sink a ship, silt a harbour, or break the Thread over a province; it may **not**
depose a praefect, dissolve a guild, convert a parish, or move standing, regard, commitment or
grievance. **Those subjects are society's and belong to characters.** An event's *consequences* reach
society only through what people then choose to do about it — which is the entire game.

## WHAT IS STILL OPEN
- **Where the boundary of "peninsular human society" is drawn** for edge subjects: a plague (biology, but
  it empties institutions), a famine (weather times tending), a heresy (religion — society, so choices).
  The rule decides each **by its subject**, and those three resolve to event · both · choice. Harder
  cases will exist and the rule, not a list, is what settles them.
- **The balance question is unchanged and unmeasured:** the ratio of event pressure to what tending can
  offset sets the world's difficulty curve, and nothing in this design has been run.

---

# EXTENSION (Jordan): "A state change includes the creation of a new state or the deletion of a state."

**This unifies the mode set under the partition and takes `mint`/`efface` away from `Act`.**

The v2 architecture makes `mint` and `efface` **act modes** — so only a character could bring a thing
into or out of existence. Under this extension, creation and deletion are just state changes, and the
partition governs them by **subject** exactly like any other. **Therefore events create and destroy
too**, within their half of the partition.

> **ONE CHANGE PRIMITIVE, TWO DRIVERS, AND THE PARTITION PICKS THE DRIVER.**
> ```
> StateChange := (subject, mode, driver)
>    mode   ∈ mint | alter | efface
>    driver ∈ Act(character) | Event(world)
> ```
> **The subject decides which driver is legal. The mode is orthogonal to both.** A character may mint a
> social state; an event may mint a non-social one; neither may reach across.

| | **`mint`** | **`alter`** | **`efface`** |
|---|---|---|---|
| **social subject → a character's choice** | found a settlement · establish an office · found a faction · marry · confer an office · take up an occupation · found a parish | move standing, regard, commitment, grievance · amend a remit · tend a holding | dissolve a guild · abolish an office · strike a village from the roll · annul a marriage · revoke a tenure |
| **non-social subject → an event** | **a new island · a river changing course · a tear opening in the substrate · a new seam exposed by a landslide** | weather · `wear` · a body ageing · Altonian pressure | **a storm destroying a harbour · a seam worked out · a tear closing · a body failing** |

**The bottom-left cell is the one the v2 architecture forbids and Jordan's rule requires**, and it is a
real capability the design did not have: **the world can create and destroy things.** A landslide
exposes a seam nobody knew was there and a faction forms around working it — with no authoring, and
with no character having decided the seam should exist.

## THE WORKED CASE THAT PROVES THE PARTITION IS DOING REAL WORK

**Can a plague efface a settlement?** The subject test answers it, and the answer is historically exact.

- A plague **kills bodies** — non-social subject, so an event `efface`s persons. Legal.
- A settlement is a **named society aspect**, so *its* deletion is a character's choice. **The plague
  cannot efface it.**
- So the village empties, and it **still legally exists** until some office strikes it from the roll.
  That striking is an act, by a named person, at a date, witnessable, contestable, and refusable.

> **Villages do not cease to exist because everyone died. Somebody has to strike them from the roll.**

An enumeration of licensed channels could never have produced that. **A partition on the subject
produces it for free**, and produces the same answer for a dissolved guild, an abandoned parish and a
polity that has lost every subject but not yet been dissolved.

## CONSEQUENCES FOR THE V2 SUITE, precisely

1. **`mint`/`efface` move off `Act` and onto `StateChange`.** `01_ARCHITECTURE.md`'s "one act with five
   modes" becomes **one change with three modes and two drivers**. `read` is not a state change and
   belongs to the conflict declaration; `exclude` is a claim on contention, not a mode of change — both
   need re-siting, and that is real work, not a relabel.
2. **The §14 refusal walk must be re-run for events**, because ten objects were walked against
   `mint`/`efface` **as acts only**. An event-driven `mint` has a different exposure on row 3 (no
   broadcast), row 13 (no per-entity branch) and row 14 (no authored opportunity) — the deck is authored
   content, and row 14 is where that must be argued rather than assumed.
3. **Determinism must cover event-driven mints.** The substream key is `(world_seed, tick, subject_id,
   purpose)` and an event has no actor; `purpose` carries it, but the id of a minted island has no
   subject to key from. This needs stating.
4. **The conflict rule needs an event term.** Two acts conflict by shared object and mode; an event and
   an act touching one object is a new pair the rule does not cover. **An event does not contest** — it
   is not an agent — so the honest form is that events resolve first, in their own barrier, and acts
   resolve against the world they leave.
