# Social contest, proposal 3: authority first

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

One of three competing proposals on the common base `2026-10-30-social-contest-armature.md` (**ARM**, read with its
§I corrections as given). Rulings `R-1..R-41` and `S-1..S-8` are cited from
`2026-10-30-social-contest-primitives-and-kinds.md` §1. Code is cited at file:line from this checkout; figures marked
*measured* were run by me on `build_realm(0)` at world build (season 0, one seed: counts, not rates). Scripts:
`/tmp/claude-0/-home-user-ttrpg/b9ffadb9-a21e-55d5-8bf9-c652527b3c6b/scratchpad/proposals/C/` (`measure.py`,
`m2.py`, `flow.py`). Canadian spelling.

---

## 1. Executive overview

Valoria's social contests are the arguments, trials, petitions, negotiations and parliamentary votes by which persons
in the world change what other persons hold, owe and may do. There is no game master: the engine resolves every act
with one σ-leveraged roll, and the result is written into the world as a fact others learn.

This proposal organises the subsystem around **authorities**: the parties themselves, the polity (crown and duchies)
and the church. A contest is *what an authority does with a matter*. Before any die is rolled the engine asks which
authority takes the matter, whether another authority already holds it (a contest over the forum), whether a seat of
that authority sits over the place, and whether the party answers the summons. The dice then resolve the acts inside
the proceeding, exactly as in the armature, with one addition: a seat's weight is scaled by how the territory's
residents regard that seat's faction. After the determination the engine asks who holds the arm that executes it,
and whether the losing side carries the matter to another authority.

What is different: crown-over-church, jurisdiction fights and appeals are native. The four routes by which real
crowns checked real church courts (deny the arm, expel the officer, carry the case elsewhere, refuse the summons)
are each an existing verb given a reader. The roll changes least of the three proposals.

What it costs: five new readers on existing verbs, one data column, a handful of row keys and one barrier index; all
of it is unreachable from computed play until computed cases name a row (today none do). It needs five answers from
Jordan, chiefly whether the church may reach beyond Himmelenger (T9) and whether a barrier index built from other
persons' ledgers may be read inside the fold.

---
