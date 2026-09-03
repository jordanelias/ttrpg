# READINGS · 10 — THE FACTION AS A DEPLOYABLE ABSTRACTION

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL.**
## ⚠ **This document AMENDS the stages** — it is not only a reading. Jordan-directed, 2026-09-03.
## ✅ **FOLDED IN 2026-09-03 — this is the RATIONALE, and the stages are now the text.** A reader who
## wants the current design reads the stages; this page says *why* they say what they do.

> **Jordan, verbatim:** *"factions can't act by themselves, but they should be available as an
> abstraction for all the people who belong to that faction such that the game code can actually
> deploy it"* — and, separately: *"it should be possible for factions to be flagged at war with
> another one. Factions could also be a container for people and holdings, and I think it would make
> things like mass battles and grid based squad combat etc way easier to define."*

---

# §1 · The ruling, and why it is not a weakening of `AX-1`

Stages 1–3 said *a faction is a Proposition plus its `commit` edges* and stopped there, treating the
faction as **something that does not exist as an object at all.** That was correct about ownership
and **wrong about deployment** — it left every consumer to recompute a set nobody had named.

> ### **A `Faction` IS A FIRST-CLASS OBJECT THAT CODE HOLDS AND DEPLOYS — AND IT IS A RESOLVED VIEW, NEVER A CARRIER.**

```
Faction := ( proposition : PropositionId   -- its identity. Immutable, uttered by a named person
           , members     : PersonId[]      -- live `commit` edges
           , holdings    : RungId[]        -- the union of its members' holds
           , seats       : SeatId[]        -- the seats its members hold
           , head?       : PersonId        -- by the proposition's own rule
           )
```

**Built at a barrier, handed to whatever needs it, discarded there.**

| `AX-1` still holds because | code gets what it needs because |
|---|---|
| it has **no verbs** | it is a real object with real rosters |
| it never appears as `Act.actor` | the battle seam iterates `members` |
| `resolve` has **no faction parameter** | the UI, the AI and the port all take one |

**And the resolved form is strictly better than a stored one: it CANNOT GO STALE.** A stored roster
drifts from the commit edges and needs a reconciliation pass. A resolved one **is** the edges.

## §1.1 · What it must never gain

- **A field of its own.** Any field needs an owner, and a faction has none.
- **A place as an actor.** Not `Act.actor`, not a `contest` claimant, not a `resolve` parameter.
- **A `hold` subject.** That is what brings back **territory held by a banner nobody carries** —
  uncontestable, because the holder can never appear at a venue.

---

# §2 · War — an uttered declaration, not a boolean

⚠ **THE PURE COMMITMENT MODEL HAD A REAL GAP, AND JORDAN'S INSTINCT CAUGHT IT.** It cannot express
**a war that outlives its supporters** — which is the normal historical case. Under commitments
alone, a war evaporates the moment enthusiasm does.

> **A declaration of war is a Proposition somebody UTTERED, plus an owned edge. Peace is `until`
> written on it.**

| | |
|---|---|
| **de jure** | the uttered war, persisting until somebody makes peace |
| **de facto** | the commitment share, which may be near zero |
| **the gap** | *"we are still at war, and nobody will muster"* — a whole genre of play |

**Why not a boolean between two faction objects:** a boolean has **no owner, so nothing can end it
and nobody declared it.** You would get a war nobody started and nobody can stop — and no way to
express a duke who refuses to fight one his king declared.

**So `at_war(A, B)` is a real predicate the combat seam may ask**, backed by a declaration somebody
made and somebody can end.

⚠ **AND THIS IS THE SAME SHAPE AS SUBORDINATION** — an uttered Proposition, an owned edge, and a gap
between the sworn and the actual. **Twice now, which makes it the pattern rather than a special case
for `H-101`.**

---

# §3 · What this buys the subsystems, which was the point

**The seam receives two RESOLVED factions, frozen at entry**, exactly as it receives a read-only
world projection.

| | |
|---|---|
| **sides** | the two `members` rosters |
| **units** | persons, at weight — one type, no unit class |
| **stakes** | `holdings` and `seats`, for what a defeat costs |
| **frozen** | ⚠ **a unit's side cannot change mid-battle because somebody repudiated three duchies away** |

> **That last row is why the roster must be resolved at the seam boundary rather than per tick, and
> the mechanism already existed** — the barrier cache. The stages under-used it and said "a read-only
> projection" without stating the roster contract.

**For grid squad combat the same thing holds one scale down:** the squad is the members of a faction
present at a rung, resolved once, and every combatant is a `Person`.

---

# §4 · The three edits this makes to the stages

1. **`hold`'s subject stays `Person`** — and **`holdings(faction)` becomes a named Query**, so faction
   holdings are a first-class thing to ASK for without becoming a thing to OWN.
2. **The seam's projection gains a stated roster contract** — sides resolved and frozen at entry,
   explicitly, rather than left implicit.
3. **War joins subordination as the second instance of the uttered-declaration pattern.**

## §4.1 · ⚠ **WHERE THEY ACTUALLY LANDED — and it was more than three**

**Recorded because a fold that reports its own estimate is not a fold.** Three edits were forecast;
**nine files moved** — the seven in the table below, plus this page's own status line and the suite
`README.md` — and two of the extras are the ones worth reading.

| stage | site | what landed |
|---|---|---|
| 1 | **§D.11**, §D.10, `T-h`, **`ID-15`**, §E.1.6, §F.2, §F.4 | the `Faction` view · the general rule · war as the second instance |
| 2 | **§B.1.1**, §E.0 | *not a nesting* ≠ *not a container* · two properties graded ABSENT |
| 3 | **§E.2.1** | the roster contract |
| 4 | **§B.6.1**, §B.10–12, **§C.5.1** | the type · `faction_q` · the seam's contract, with its GDScript price |
| 4 | **D-1, D-14, D-18, D-47..D-51** | one construction rebuilt · one grade **upgraded** · five rows added |
| 4 | F.23, **F.32, F.33**, §F.34, §F.35 | one gap narrowed · two opened · the count corrected |
| 4 | **§G.2.8**, §G.5 | the rule, with a falsifier |
| 0 | **question 1** | the two-question test, at the front door |
| readings | 05, 09 | *"not a type"* corrected where it had already propagated |

> ### **THE TWO EXTRAS THAT WERE NOT FORECAST, AND BOTH ARE COSTS RATHER THAN GAINS**
>
> **1 · A guard was LOST.** *A faction cannot gain a field* was STRUCTURAL **by absence of a type**;
> a type now exists and the defence drops to the view's **lifetime** (D-47). **Strictly weaker, and
> recorded rather than absorbed** — this is the only grade in Part D the amendment reduces.
>
> **2 · Two gaps OPENED** (`F.32` whose edge a war is, so who may make peace when the declarer is
> dead; `F.33` whether `at_war` may appear in a verb's `requires`). **Both are properties stated
> without their representation — the exact failure §F.35 charges to Stage 3, reproduced by a
> different author on the first try.** The finding is not about Stage 3.

**And one thing that did NOT happen, which is the load-bearing result: NO PRIMITIVE WAS ADDED.** A
faction is a Query return over edges that already existed; a war is a Proposition with an owned edge.
**Two rulings that each looked like a demand for new vocabulary cost none** — which is the strongest
test the method in `00_THE_METHOD.md` has been put to, because it was applied after the fact.

> ### **THE GENERAL RULE THIS SETTLES, AND IT IS WORTH MORE THAN THE THREE EDITS**
> **AN ABSTRACTION MAY BE FIRST-CLASS FOR CONSUMERS WITHOUT BEING FIRST-CLASS FOR STATE.** The
> question *"should a faction exist as an object?"* was the wrong question, because it conflated
> **deploying** with **owning**. The right pair of questions is: *what does code need to hold?* and
> *what writes it?* — and when the second answer is *nothing*, you have a view, not a carrier.
