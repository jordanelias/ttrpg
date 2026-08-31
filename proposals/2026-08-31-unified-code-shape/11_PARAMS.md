# 11 · THE PARAMETER LEDGER — every constant, its owner, its grade

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L5 — the most granular.** **This document proposes NO VALUES.** It says where each number
## must live, who owns it, and — for every one — whether it is **measured**, **ruled**, or
## **assumption-grade**. A number quoted without that grade is how a guess becomes canon.

---

## §1 · THE RULE

> **A value the engine uses lives where CODE READS IT — a typed exported artifact, or a single owner
> in the source. Never in prose, never in two files, and never transcribed by hand into a literal.**

**Prose is reference.** If a document and the exported row disagree, that is a defect in one of them,
and it is resolved by deciding and then **changing the code** — never by declaring the prose
authoritative.

**Three grades, and every row below carries one:**

| grade | means | may it be cited as a fact? |
|---|---|---|
| **MEASURED** | produced by a run, with the run's control | **yes**, with its control |
| **RULED** | a person decided; no measurement claimed or needed | **yes**, as a decision |
| **ASSUMPTION** | a shape proposal, or a number nobody chose | **NO.** Quoting one as measured is the failure this ledger exists to prevent |

---

## §2 · WHAT IS ALREADY EXPORTED AND OWNED — adopt, do not re-derive

| # | constant | owner | grade | note |
|---|---|---|---|---|
| 1 | the target number | the dice owner | **RULED** | **7, always.** The owner **raises** on any other value. A varying difficulty is an obstacle, not a target number |
| 2 | the face rule | the dice owner | **RULED** | face 1 = **−1**; 2–6 = 0; 7–9 = +1; 10 = +2 |
| 3 | mean per die | the dice owner | **derived** from the face rule | `0.40` |
| 4 | **sigma per die** | the dice owner | **derived** from the face rule | **`0.800`** — and the design line's `0.671` is **exact for a different die**, not an error. §5 |
| 5 | the degree bands | the dice owner | **RULED** | four, on the **margin**: Overwhelming ≥ 3 · Success ≥ 1 · Partial [0,1) · Failure < 0 |
| 6 | the obstacle floor | the leverage owner | **RULED** | pinned; an uncontested attempt routes to a **gate**, never to a zero-obstacle roll |
| 7 | the attribute roster | the descriptor registry | **RULED — count only** | ten ruled; **nine ship and the tenth is unnamed.** §4 |
| 8 | the conviction roster | the descriptor registry | **RULED** | thirteen, closed, **raise on a non-member** |
| 9 | the termination caps | the event substrate | **REQUIRED, NO DEFAULT** | so no fabricated constant enters. **Copy this posture** for the contest depth cap |

---

## §3 · WHAT THIS SHAPE OWES THE PIPELINE — rows that must exist before code reads them

**None of these has a value here.** Each names what it is, who owns it, and what would settle it.

| # | row | owner | grade | what would settle it |
|---|---|---|---|---|
| 10 | **`COND_SCALE`** | params | **RULED** — a representation choice | pick `10_000` and export it. **Never a literal in a source file** |
| 11 | **`wear(site_kind)`**, one row per kind | params | **ASSUMPTION — and it is the most load-bearing unmeasured number in the game** | campaigns across a range of ratios, comparing the distribution of site outcomes. **It sets the entire difficulty curve** |
| 12 | the restoration effect of a tending act | params | **ASSUMPTION** | the same run. **It is the other half of row 11 and neither means anything alone** |
| 13 | `season_factor`'s distribution | params | **ASSUMPTION** | **it multiplies every harvest**, and it blocks `yield` |
| 14 | the ledger cap `L` | params | **ASSUMPTION** | it decides **whether the decisive claim survives eviction** |
| 15 | the view budget `K` and its terms | params | **ASSUMPTION** | *the claim that does not surface* was found by **6 of 6** lanes; this is that number |
| 16 | the `Obstacle > 2 x Pool` refusal threshold | params | **RULED** — a design choice | — |
| 17 | the publicity coefficients | params | **ASSUMPTION — shape proposal** | `07` §5.2 states the shape and says so |
| 18 | the attention-floor coefficient | params | **ASSUMPTION — shape proposal** | as above |
| 19 | the commitment-degree weights | params | **RULED** — a ladder, not a measurement | — |
| 20 | the requisition **burden** coefficient | params | **ASSUMPTION** | ⚠ flagged as doing **more dramatic work than any other coefficient in the design**, and **untested by either exercise** |
| 21 | the Slate budget `B` per difficulty | params | **RULED** — it is canon | 4–5 / 5–7 / 7–9 |
| 22 | the per-band effect coefficients | params | **ASSUMPTION** | and they key to **the owner's four-band enum**, not to a five-band table |
| 23 | the contest depth cap | **caller-supplied** | **NO DEFAULT, EVER** | §2 row 9's posture |
| 24 | age-band boundaries | params | **ASSUMPTION** | — |
| 25 | channel latency values | params | **ASSUMPTION** | — |

**Of twenty-five rows: nine are already owned, five are ruled and owed a row, and ELEVEN are
assumption-grade.** **That ratio is the honest state of the numbers in this design**, and no document
in this suite may quote one of the eleven as though it were measured.

---

## §4 · THE TENTH ATTRIBUTE — a worked example of how to hold an open row

**Ten were ruled. Nine ship. The tenth is unnamed**, and the registry says so in its own banner:
*do not infer the tenth from the aliases.*

**A strong candidate exists** — a name appears in shipped port code in about nineteen places, and a
frozen canon capture tables it. **And it does not close the question**, because that capture carries a
**rival ten-attribute roster** against the registry's nine, and the contract layer records that
**neither roster is wired.**

> **So the row stays open, and the shape's answer is architectural rather than nominal: the roster is a
> REGISTRY READ AT LOAD TIME.** Naming the tenth is then **one row**, not a code change, and the port
> binds no attribute field until it lands. **That is what holding a question open looks like when you
> still have to build.**

---

## §5 · TWO DICE, NOT ONE DIE WITH AN ERROR IN IT

> ⚠ **AN EARLIER DRAFT OF THIS SECTION CALLED `0.671` AN ARITHMETIC ERROR. IT IS NOT ONE, AND THE FIX
> IT PRESCRIBED WOULD HAVE CORRUPTED ITS OWN SOURCES.**

| | design-line die | executing die |
|---|---|---|
| face rule | `1–6` = 0 · `7–9` = +1 · `10` = +2 | **`1` = −1** · `2–6` = 0 · `7–9` = +1 · `10` = +2 |
| `mu` per die | 0.50 | **0.40** (−20%) |
| variance · `sigma` | 0.45 · **0.670820** | 0.64 · **0.800000** |
| can a **1D** pool net below zero? | **no** | **yes**, with p = 0.1 |

**Both constants are exact for their own die.** The design line declares its die and derives `0.671`
from it, in the document that owns the constant; the executing owner declares a botch face and gets
`0.800`. **Neither is a miscalculation.**

**What follows, and it is the part that matters:**

1. **`0.671` is CORRECT wherever the design-line die is in force.** Replacing it with `0.800` while
   leaving `mu = 0.5` and the pool table beside it **breaks that document**. **`sigma` and `mu` come
   from one die: change the die, or change nothing.**
2. **This shape adopts the executing die** — see `15_ADJUDICATIONS.md` **R-18**, where it is recorded
   as a **departure from the design line with its cost priced**, rather than presented as a corrected
   constant.
3. **Every statistic the design line derived from its own die is VOID under that ruling and must be
   RE-DERIVED, not edited** — including any published underdog or disaster probability.
4. **The rule against flat modifiers survives untouched**, because it holds for any `sigma > 0`.

> **Found independently by two lanes that could not see each other, which is the strongest signal this
> process produces.** It is also the cheapest class of defect to propagate and the hardest to notice:
> **nobody re-derives a constant that is sitting in a table.**

---

## §6 · WHAT MUST NEVER BECOME A PARAMETER

| refused as a param | because |
|---|---|
| a target number that varies | it is an **obstacle**; the owner raises on any other value |
| a fifth degree band as a table entry | a band is an **amendment to the one owner**, never a row somebody adds |
| a per-faction or per-person modifier | Law 1's arithmetic — it helps weak pools more, backwards |
| a decay rate on any social quantity | nothing social moves on a clock |
| a default contest depth | a fabricated constant, and [engine] a crash rather than an error at the limit |
| a population target or spawn rate | **nothing generates without a demand, and no clock generates anything** |
| a convergence rate | **`06` §6.1**: if convergence is a game property it is settled by running campaigns, not by tuning a number |
| a "difficulty" scalar | difficulty is `wear` against tending, and it is a **distribution over sites**, not a dial |
