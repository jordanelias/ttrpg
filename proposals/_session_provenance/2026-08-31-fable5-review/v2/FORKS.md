# THE SIX RESERVED FORKS, WORKED FOR THE IDEAL SYSTEM
# Jordan: "our goal is to design the ideal system." So these are worked, not deferred.
# Each is a PROPOSAL with its cost stated. Five dissolve under a primitive; one is a real taste call.
# ⚠ This document's author overclaimed twice earlier this session. Treat every "dissolves" below as a
# claim to be attacked, and each carries the line that would falsify it.

## The pattern worth naming first

Five of these six were filed as forks because the design lacked a primitive that would let BOTH answers
coexist. A fork of the form *"is X globally A or globally B?"* is usually a missing type parameter.
Where that is what is happening, the ideal answer is **neither branch — it is the parameter**, and the
branch becomes a per-instance authoring choice rather than a world-wide law.

---

## F1 · CONFERRAL BASIS — person-rooted or office-rooted? **DISSOLVES.**

**The fork:** an oath to a man dies with the man (successions rupture every chain beneath them), or an
oath to the Crown-as-institution survives him (the graph resolves, `sovereign_fraction` is total).

**Why it is not a global choice.** `Tenure(kind=hold)` already carries a `conferrer` field, and nothing
requires every office to fill it the same way. So make it what it plainly is: **`Office.conferral`
names the basis, per office.** A warband's oath to its captain is person-rooted and dies with him. A
praefecture is office-rooted and survives its holder. **Both ship, in one primitive, and which one an
office uses is world-authoring — a fact about that institution, not a law of physics.**

**Why this is better than either branch, not a dodge.** It is historically exact — the same peninsula
held personal warbands and institutional magistracies simultaneously, and *the difference between them
was the political question of the age.* It also makes the Löwenritter's warrant *"sworn to the Crown as
institution, not the bloodline"* a **contested design of that order** rather than a global rule, so a
faction can try to convert an office from one basis to the other. That is a new political move that
neither branch offered.

**What it costs:** `sovereign_fraction(root)` is now total only over the office-rooted subgraph, and
person-rooted chains genuinely terminate at dead conferrers. Callers must handle a partial answer.
**Falsifier:** if some caller needs a total sovereignty answer over ALL offices, this fails and one
global basis is forced.

---

## F2 · IS `stores` THE REALM'S DENOMINATOR? **DISSOLVES — into a type parameter.**

**The fork:** mouth-seasons are perishable and bulky, so realm-scale contracts in them make force
logistics-real — or a fungible transferable scalar functions as money whether or not it is called that,
and coin returns by the back door.

**The missing parameter is the MATTER KIND.** `stores` is one scalar because the design refused a
second unit needing conversion (`13:285-287`). Correct refusal, wrong conclusion. Keep one *shape* and
give it a kind:

```
Stores := map[MatterKind -> quantity]
MatterKind := (name, perishability, bulk, edible)
```
`transfer` is unchanged and still needs no conversion — it moves a quantity of ONE kind. Then:
- **grain** — edible, perishable, bulky. Feeds mouths. Cannot cross the realm without spoilage and
  cannot be hoarded across generations.
- **silver** — not edible, imperishable, dense. Cannot feed anyone, so it never satisfies `subsistence`
  directly; it must be *exchanged*, which requires a counterparty who wants it.

**Both answers are now true of different things, which is what an economy is.** Force is
logistics-real where wages are grain, and money exists where they are silver, and *choosing which to
pay in is a real decision with real consequences.* Coin does not "return by the back door"; it walks in
the front, typed, and unable to be eaten.

**What it costs:** §11.5's market path still needs an exchange form — two transfers plus a binding —
and this does not supply one. It makes the market *expressible*; it does not make it *reachable*.
**Falsifier:** if `need(subsistence)` can be satisfied by silver anywhere in the model, the kinds have
collapsed and this is one scalar again.

---

## F3 · S19 — THE ROOTLESS CLUSTER VACANCY. **DISSOLVES.**

**The fork:** an office at the root of its own cluster, whose conferral basis names neither a container
nor a parent office, has no date — so a petition filed there can neither lapse nor be mooted. Content
(a Church that stalls is the design working) or defect (a matter suspended forever)?

**It is a defect, and it is caused by an under-specified field, not by a design choice.** Under F1,
`Office.conferral` must name a basis for EVERY office. Make that a completeness requirement: a
conferral rule names a container, a parent office, **or its own judging set.** The third limb is the
one that was missing, and it is how conclaves actually work — **a body with no superior convenes
itself.** The cluster's own members hold the date.

Then the Church that stalls is still fully available as content: the conclave convenes, and the men in
the room fail to agree. **A stall by human disagreement is the design working. A stall because no
object holds a date is a hole**, and this closes the hole without closing the story.

**What it costs:** every office must now have a well-formed conferral rule, which is authoring work.
**Falsifier:** an office whose judging set is empty has no self-convening route either — so the rule
needs a floor, and I do not specify one here.

---

## F4 · THE COHERENCE-0 ONTOLOGY. **NOT A FORK — a state.**

**The fork as filed:** Coherence 0 is loss of capacity, versus *a person has become an object.*

**Both are true of different registers and nothing forces a choice.** Coherence is a Person field. At 0
the person **stops generating acts** — which is a capacity fact — and **remains a Person record**,
because other people's claims about them persist and their ties still exist. "Became an object" is the
in-world *reading* of "no longer acts", and the design already has a machine state for exactly that: a
cohort member is a person who is not currently generating individual acts. So Coherence-0 is
**de-individuation by a different cause**, and needs no new ontology at all.

**What it costs:** a Coherence-0 person who holds an office freezes that seat, and the vacancy-by-
absence rule must reach them or the seat is stuck. **Falsifier:** if anything in the design must ask
*"is this still a person?"* and branch on the answer, this is a real ontological fork after all.

---

## F5 · OFF-BOARD POLITIES. **RESOLVES — generate persons, and take no exception.**

**The fork:** Altonia and Schoenland exert real pressure from off the map. *Generate a person* or
*allow an actorless pressure* — the second being the only exception to §1.1 in the design.

**Take the first, and note that it is now nearly free.** An off-board polity is a **Node outside the
played region** with an establishment — named persons, minted from a demographic envelope exactly like
any other, at whatever coarse fidelity is affordable. Their acts arrive as ordinary events and their
claims travel by ordinary channels, slowly. **§1.1 keeps its no-exception status**, which is worth a
great deal: the moment one actorless pressure is licensed, every future pressure has a precedent.

**Why it is cheap now and was not before.** It was expensive when persons had to be authored. Under the
demographic envelope and mint-on-demand, an off-board realm costs one envelope and a handful of records
that individuate only when someone here hears of them.

**What it costs:** off-board persons are simulated at low fidelity, so their decisions are coarse, and
a player who sails to Altonia finds a thinner world than home. **Falsifier:** if off-board pressure must
respond to on-board events faster than telling-speed, no person-based model can carry it.

---

## F6 · IS THE WORLD DYING OR MISUNDERSTOOD? **A GENUINE TASTE CALL — this one stays Jordan's.**

Whether slow material decline is a real trajectory the player must arrest, or a fact everyone reports
wrongly. **This one does not dissolve, and should not.** It is not a missing primitive — §10 already
makes both expressible, and the machinery is identical either way. It is a question about **what the
game is about**, and the answer changes what a twenty-season campaign feels like without changing one
line of the architecture.

That is the actual signature of a real fork: **the code is the same and the game is different.** The
other five failed that test — each of them changed the code.

---

## SUMMARY

| fork | disposition | what carries it |
|---|---|---|
| D-2 act economy | **proposed: one act per person, universally** | the establishment carries throughput (see `D2_PROPOSAL.md`) |
| F1 conferral basis | **dissolves** | `Office.conferral` is per-office |
| F2 `stores` denominator | **dissolves** | `MatterKind` type parameter |
| F3 S19 | **dissolves** | conferral may name the office's own judging set |
| F4 Coherence-0 | **not a fork** | de-individuation by another cause |
| F5 off-board polities | **resolves** | a Node with an establishment; §1.1 keeps no exception |
| F6 dying or misunderstood | **stays Jordan's** | the code is identical; only the game differs |
