# THE METHOD — the front door

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## **This is the page to read first, and on most days the only one.** Stages 1–4 are the derivation
## that justifies it. **If this page and a stage disagree, the stage is right and this page is stale.**

---

# THE THREE GENERATORS

Everything in the four stages is one of these three at a different altitude.

| | it answers | it decides |
|---|---|---|
| **OWNERSHIP** | *what is this?* | field vs edge vs Query vs cache · module boundaries · who may end a relation · what a write may do |
| **REPRESENTATION** | *does this hold?* | mechanism vs reference · checkable vs asserted · survives a session vs doesn't |
| **PERSONHOOD** | *is this our game?* | only a person acts — so institutions are derived, nothing broadcasts, and emergence comes from removal |

---

# THE THREE QUESTIONS

**Every design question enters here, in this order. Each has a wrong answer that tells you exactly
where the problem is.**

## 1 · WHO OWNS THIS?

| answer | verdict |
|---|---|
| **one**, and it is about one thing | a **FIELD** on that thing |
| **one**, and it is about two things | an **EDGE**, owned by its subject |
| **none possible** — it spans many owners | a **QUERY**. Owned by Nobody, computed, stored nowhere |
| none, but recomputing is too costly | a **BARRIER CACHE** — built at a barrier, discarded at the next |
| ⚠ **two** | **a defect, and you have just located it exactly** |

> ### ⚠ **AND THE QUESTION IS NEVER *"SHOULD THIS EXIST AS AN OBJECT?"***
> That conflates **DEPLOYING** with **OWNING**, and it has no right answer — which is why asking it
> carefully still gets it wrong. **Ask both halves:**
>
> | | |
> |---|---|
> | **what does code need to HOLD?** | if a consumer must iterate it, name it and build it |
> | **what WRITES it?** | if the answer is **nothing**, it is a **VIEW** — built at a barrier, dropped at the next |
>
> **Two yeses give a carrier. Hold-yes and write-nothing give a view. Neither gives a Query.**
>
> ### ⚠ **AND ONCE IT IS A FIELD, ONE MORE QUESTION BEFORE IT IS ADMITTED (`§D.0`, added 2026-09-03)**
> **What kind of assertion is it — DECLARED, THE CASE, or READ OFF?** A declared value whose declaring
> act cannot be named, a case value that changes with no act and none of the three motions, a read-off
> value nothing at a venue could perceive: each is **on the wrong carrier**, and the verdict is
> usually *move it*, not *refuse it*. ⚰ *`judging_set_rule` — which seats decide — sat on a place.*
>
> **FIRST-CLASS FOR CONSUMERS IS NOT FIRST-CLASS FOR STATE.** ⚰ *Four stages concluded a faction is
> not an object — right about ownership, wrong about deployment — and left the battle seam, the squad
> grid, the UI and the AI each recomputing a roster nobody had named.* **The price is real and must be
> stated when taken: a view is a type, and a type can gain a field. Its defence is LIFETIME, not
> ABSENCE, and that is strictly weaker.**

## 2 · WHAT CAN CHECK THIS?

| answer | verdict |
|---|---|
| **data a loader validates** | it holds — a contradiction fails the load, naming the row |
| **code with a falsifier** | it holds — red before, green after, and a later session can re-run it |
| **prose** | ⚠ **it does not exist yet.** Prose is a pointer, never a mechanism |

> **A check is exactly as strong as the representation of the thing it checks.** Before writing any
> guard, ask what form the guarded thing is in. **If it is prose, the guard is prose — type the thing
> first.**

## 3 · WHOSE ACT MAKES THIS HAPPEN?

| answer | verdict |
|---|---|
| a named person, at a venue, paying for it | it is this game |
| matter · bodies · the fading of memory | the three licensed motions, and **only** these |
| ⚠ **nobody's** | **you have found a narrator. Remove it.** |

**Answer all three cleanly and you have a design. Fail one and you have located the problem
precisely — which is worth more than a design you cannot fault.**

---

# THE SIX MOVES OF A SESSION

1. **Derive with the tree closed.** The tree is opened only to falsify. Not because it is wrong —
   because it is **enumerable and derivation is not**, so a session under pressure drifts to it and
   produces the existing tree with better prose. **Enforce by what an agent can reach, not by telling
   it.**
2. **Ask question 1 at every level.** It decides the type, the module, the file, and the closing act.
3. **State no property without its representation** — or a register row that grades its absence. A
   property with neither is not a result; it is work handed forward silently.
4. **Write it where a loader or a falsifier can evaluate it.**
5. **Attack in three directions.** *Did the producer invent?* · *did the producer refuse what the
   design permits?* · **and *did the producer grade something backwards?*** An error against the
   design looks like rigour — one survived four adversarial passes and cost ten arcs. ⚠ **The third
   was added 2026-09-03 (`§G.4.3`) and this page carried two until then.** Its corpse: a design
   audited itself, found seven violations, and **filed a defect in the table of things it had got
   right** — a loop that penalises good governance, listed among *the negative loops that are
   correct*. **Neither invented nor over-refused: misgraded, by the author, inside the section built
   to catch it** — which is the one an author cannot ask of themselves, because the misgrading and
   the confidence come from the same place.
6. **Close on an execution artifact.** A finding is an edit, a row that needs Jordan, or nothing.
   **There is no third state.**

---

# WHAT A STAGE PRODUCES

> **A loader invariant, a type, or a falsifier. The document is the derivation that justifies it, and
> is not the artifact.**

This inverts the apparent hierarchy of the four stages, and the inversion is correct: **Stage 1 looks
foundational and is the argument; Stage 4's twelve loader invariants are the only part that survives a
session boundary intact.**

---

# THE FOUR RULES OF EMERGENCE

1. **Emergence is what is left when you refuse.** You do not build it — **you stop preventing it.**
   Obstruction, scarcity, factional collapse, reputation, deception: five properties, zero
   implementations.
2. **A primitive earns its place by what it makes UNNECESSARY.** Not *what does this enable* —
   **what does this let me delete.**
3. **Interaction must be uniform.** One relation over four object kinds; one fold over every verb.
   **The rule count must not grow with the pair count.** When it starts to, you have stopped composing
   and started scripting.
4. **No primitive may know another's purpose.** A seat does not know its holder; an Event does not
   know its recipient; a site does not know which verbs it gates. **Ignorance is the fuel; ownership is
   the bound.**

> **Emergence = ignorant primitives + uniform composition + bounded ownership.** Remove the ignorance
> and you get scripting; the uniformity and you get N² rules; the bound and you get noise.

---

# THE ONE HAZARD

> ## **DEFERRING TO WHAT EXISTS INSTEAD OF DERIVING FROM WHAT IS TRUE.**

Its signature: **the session opens the tree first**, because the tree can be listed and derivation
cannot — and everything it then produces is the tree with better prose.

**An instruction does not hold against this.** It was demonstrated three times in one session *under
an instruction against it*. Only a **scope** does — and that claim is the least-evidenced thing in the
whole exercise, because no stage here has ever actually run under one. **It is a hypothesis with a
corpse for the hazard and none for the fix.**

---

# THE TEST THAT CLOSES THE CIRCLE

> **If you are about to write a rule whose subject is a specific PAIR — this verb on that object, this
> faction under that one — stop. The rule belongs to one of the two, or it belongs to neither and is
> a Query.**

That is question 1 again, and it is why `H-101` needed no new edge, why closure needed no four verbs,
and why four stages of design **added no primitive at all.**

⚠ **AND THE CLAIM WAS TESTED AFTER THE FACT, WHICH IS THE ONLY REASON IT IS WORTH ANYTHING.** Jordan
ruled two things the design had not anticipated — **a faction is a deployable container**, and
**factions can be at war** — each of which looks like a demand for a new primitive. Neither was:
a faction is a **Query return** over edges that already existed, and a war is a **Proposition with an
owned edge**, the same shape as subordination. **The vocabulary did not grow.**

> **What the design could NOT absorb was their REPRESENTATION** — whose edge a war is, and whether
> `at_war` reaches a verb's `requires` (`F.32`, `F.33`). **A property stated without its
> representation, from a different author, on the first try.** That is rule 3 above failing in the
> wild, and it is the strongest evidence in the exercise that rule 3 is the one that binds.

> **A meta-architecture that answers questions by growing the vocabulary has renamed the problem
> rather than found the shape.**
