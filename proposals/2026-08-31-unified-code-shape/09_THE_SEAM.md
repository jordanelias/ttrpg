# 09 · THE SEAM — how a contest plugs into the season loop

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L4.** **SCOPE, stated first and enforced throughout: this document specifies how personal
## combat, social contest and mass battle ATTACH to the season loop. It says NOTHING about what happens
## inside one, and that is deliberate.** Each is a system with its own design, its own lane and its own
## canon; none of that is this suite's business. **What is this suite's business is the four lines where
## they touch the loop, and getting those four lines wrong is how an integration fails.**

---

## §1 · THE WHOLE SEAM, IN ONE PARAGRAPH

**A contest is the season loop, nested.** It attaches at exactly one place — **RESOLVE** — where a
conflict subdivides the tick and runs the same steps over a smaller person set on a shorter clock. It
returns **Events**, which flow into the same WITNESS the season's own Events flow into.

> **A battle, a hearing, an examination committee and two brothers arguing over a barn are THE SAME CALL
> with different act vocabularies.** That is the entire integration story, and any part of it that needs
> a second story is a defect.

```
contest : (World, Rung, prize, claimant[], depth, max_depth) -> Event[]
```

**Six arguments and every one of them is load-bearing:**

| argument | why it is there |
|---|---|
| `World` **first** | it is a resolver-side call. **Calling it from inside `choose` fails at the call site** |
| `Rung` | a contest happens **somewhere**; the judging set, the venue and the witnesses all derive from it |
| `prize` | what is being allocated. **A contest with no prize is a fight scene, and this engine has no use for one** |
| `claimant[]` | **persons**, always. Not factions, not units, not sides |
| `depth` | how deep the nesting is |
| `max_depth` | **caller-supplied, with NO DEFAULT** — §4 |

---

## §2 · THE FOUR LINES WHERE A SUBSYSTEM TOUCHES THE LOOP

**Everything a deferred subsystem needs from the season loop, and everything the season loop needs back,
is four lines. If a fifth appears, something has leaked.**

| # | direction | the line |
|---|---|---|
| **1** | loop -> subsystem | **the call.** RESOLVE routes a conflict to `contest(...)` when the touch graph says two acts contest the same subject, or when an act's `contests[]` names one |
| **2** | subsystem -> loop | **Events.** A contest returns Events into the same log, with `causes[]` naming the acts that caused it. **Not state writes. Not stat deltas applied in place. Events** |
| **3** | loop -> subsystem | **the persons.** Claimants, their capability, their marks, their stances — **read, never written**, and the subsystem writes nothing about a person except through a returned Event |
| **4** | subsystem -> loop | **the outcome's degree**, from the **one** ladder. A subsystem does not have a ladder |

**And the four things that are NOT lines, because each was tried somewhere and each is a leak:**

- **No state write from inside a contest.** A contest that adjusts a settlement's order directly has
  bypassed the write matrix, the witness layer and the log at once.
- **No second resolver.** A contest is `resolve` at a smaller scale, not a different function.
- **No faction parameter.** A battle whose combatants are factions has deleted Law 1 at the seam — and
  **that is exactly what the running bridge does today**, constructing a combatant labelled with a
  faction id and a history derived from a faction stat.
- **No subsystem-specific key type family.** A contest's outcome is an Event like any other.

---

## §3 · THE DEGREE LADDER IS SHARED, AND THE ONLY VARIATION IS A DECLARED VETO

**There is one ladder for every scale of the game.** A duel, a debate, a siege and an examination all
resolve on the same four bands, read off the **margin** — how far the dice cleared the obstacle — never
off the obstacle's own size.

**The one permitted variation is a declared, demote-only extension:** a subsystem's wrapper may pass an
extension that **vetoes an Overwhelming and can do nothing else.** It is passed **by the subsystem's
wrapper, never resolved by the engine** — the engine does not know which subsystems exist.

> **This is the executing precedent for the whole seam and it is worth naming as such:** *one resolver,
> subsystem variation by declared extension, injected by the wrapper.* **Whatever a deferred subsystem
> needs that the general ladder does not give it, it declares — it does not fork.**

> ⚠ **AND THE COLLISION THAT MUST BE RESOLVED BEFORE ANY SUBSYSTEM PORTS.** The design corpus carries a
> **five-band** ladder and describes it as shipped; the executing single owner implements **four**. **A
> five-band ladder is an amendment to the one owner, made once, in that file — never a parallel enum in a
> subsystem.** Any coefficient table keyed to band names keys to **the owner's** enum, and if the owner
> gains a band, the table gains a row. **Two ladders is the failure this seam exists to prevent.**

---

## §4 · NESTING, AND THE CAP THAT MUST NOT HAVE A DEFAULT

**A contest can open a contest.** A battle contains an exchange; an exchange can contain a duel; a
hearing can contain a challenge to a witness's standing.

> **THE DEPTH CAP IS A REQUIRED CALLER-SUPPLIED ARGUMENT WITH NO DEFAULT VALUE.**

**Two reasons, and the second is the one people miss:**

1. **No fabricated constant enters the engine.** A default is a number somebody made up, and it will be
   cited later as though it were measured. The executing substrate already takes this position for its
   own two termination caps: **required constructor arguments, no defaults.**
2. **[engine] In GDScript, exceeding recursion depth is a CRASH, not a catchable error.** An argument
   that *"a nested instance is an instance"* shows the barrier count survives nesting; **it is not a
   bound.** Exceeding the cap must produce a **typed error result**, checked by the caller.

**And the traversals that are not contests but are cyclic by construction** — the conferral path, the
containment path, the tie graph, the claim citation graph — **are iterative with a visited set, never
recursive.** The reference graph is cyclic **on purpose** (`02` §6), so any traversal written as though
it were a tree will hang on the normal case rather than on an edge case.

---

## §5 · REGISTRATION IS A REGISTRY ROW, NEVER AN IMPORT

**A subsystem is attached by declaring a row that names a role and its provider. The engine names the
ROLE; the registry names the MODULE; resolution happens by string.**

**This is proven on both sides and is adopted because it is right, not because it exists:** the oracle
resolves roles by string through one owner, and the port has a manifest doing the same. **A subsystem is
swapped by editing a row.**

> ⚠ **AND THE ANTI-PATTERN TO REFUSE BY NAME.** The one surviving import-shaped seam in the oracle puts
> a subsystem directory on the module path and loads modules **by bare name** — which gives those modules
> a **second identity**, and which was **invisible to every instrument in the repository** until an
> adversarial read found it. It is declared and shrink-only for exactly that reason.
>
> **[engine] The GDScript equivalent — `preload()` by a hardcoded path from inside a resolver body — is
> the same shape with none of the declaration.** **The manifest is the seam. A path literal in a body is
> not.**

**And one consequence for the boot sequence:** the kernel **resolves every registered row at boot**, not
lazily at first use. A missing provider is a startup failure with a name in it, not a `null` three
seasons into a campaign.

---

## §6 · WHAT THE LOOP OWES A SUBSYSTEM, AND WHAT IT DOES NOT

| the loop **owes** | the loop **does not owe** |
|---|---|
| the persons, read-only, with their real capability and stances | a faction-shaped combatant |
| the rung, and through it the venue, judging set and witnesses | a bespoke arena object |
| the obstacle owner, and the one degree ladder | a subsystem-local difficulty model |
| a determinism substream derived from the contest's own id | access to the campaign RNG |
| a depth and a cap | an unbounded stack |
| somewhere to return Events | permission to write state |

**The determinism row is the one that bites.** A subsystem drawing from the campaign generator **shifts
every downstream draw in the whole campaign** — which is how *adding two people* was observed to move a
seeded winner. **A contest draws from `H(world_seed, tick, contest_id, purpose)` and from nothing else.**

---

## §7 · THE ONE THING THIS SEAM MAKES POSSIBLE THAT IS WORTH THE WHOLE DOCUMENT

**Because a contest takes `claimant[]` of **persons** and reads their real capability, marks and stances,
the identity of who fights, argues or examines is a live input rather than a label.**

> Today, at the running bridge, a battle's combatant is **built from a faction**: labelled with a faction
> id, its capability derived from a faction stat. **Two duchies with identical stats fight identically,
> whoever leads them.** And the machinery to do better already exists and is default-on — the unit type
> derives command from a person's attributes when they are supplied, **and the adapter supplies neither,
> passing a hardcoded value instead.**

**One adapter, passing the commander's real attributes instead of a constant, turns every battle in the
game from a comparison of two numbers into a consequence of who was in charge** — and it is the same
change, at the same seam, that makes a hearing depend on who convened it and an examination depend on who
sat on the committee.

**That is the whole reason the seam is specified in a suite that otherwise refuses to discuss these
systems: the throughline runs through it, or it stops there.**

---

## §8 · WHAT THIS DOCUMENT REFUSES

| refused | because |
|---|---|
| any statement about a subsystem's internals | out of scope, by instruction, and each has its own lane |
| a second resolver, an auto-resolve formula, a fast path for any contest | the twenty-year unsolved divergence |
| a subsystem-local degree ladder | one ladder, one owner, demote-only extension |
| a subsystem-local RNG or a draw from the campaign stream | it shifts every downstream draw in the campaign |
| a faction, unit or side as a contest participant | Law 1; claimants are persons |
| a state write from inside a contest | it bypasses the write matrix, the witness layer and the log at once |
| a default depth cap | a fabricated constant, and a crash rather than an error at the limit |
| `preload()` by path literal in a resolver body | a second identity for a module, invisible to every instrument |
| a subsystem key-type family | a contest's outcome is an Event like any other |
