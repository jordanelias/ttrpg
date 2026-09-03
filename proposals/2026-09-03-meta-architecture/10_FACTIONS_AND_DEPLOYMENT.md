# READINGS · 10 — THE FACTION AS A DEPLOYABLE ABSTRACTION

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL.**
## ⚠ **This document AMENDS the stages** — it is not only a reading. Jordan-directed, 2026-09-03.

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

> ### **THE GENERAL RULE THIS SETTLES, AND IT IS WORTH MORE THAN THE THREE EDITS**
> **AN ABSTRACTION MAY BE FIRST-CLASS FOR CONSUMERS WITHOUT BEING FIRST-CLASS FOR STATE.** The
> question *"should a faction exist as an object?"* was the wrong question, because it conflated
> **deploying** with **owning**. The right pair of questions is: *what does code need to hold?* and
> *what writes it?* — and when the second answer is *nothing*, you have a view, not a carrier.
