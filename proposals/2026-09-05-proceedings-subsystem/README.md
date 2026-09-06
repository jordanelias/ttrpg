# PROCEEDINGS — a game structure for negotiations, trials, tribunals, debates and hearings

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Nothing here runs. It changes no head, no roster, no verb table, no code under test, and allocates
## no `ED`/`PP`. **No `CURRENT.md` row moves.**

Per `CLAUDE.md` §2 a merge ratifies PROPOSED contents *by default*, with one exception — held back
**loudly** in the PR body. **This is that mark**, and it applies to every file in this directory.

---

> ## THE ONE SENTENCE
> **A PROCEEDING IS AN OCCASION AT WHICH PERSONS ADDRESS PERSONS WHO MAY DISPOSE OF A MATTER** — and
> a negotiation, a trial, an interrogation and an excommunication deliberation differ in **the
> relation between three sets of people** (parties · bench · floor), **one declared key** (who may
> dispose), **and what stands between them.**

> ## THE FRAMING, RULED BY JORDAN, 2026-09-05
> *"The subsystem is a game structure, which means that it hosts the parameters, logic, processes,
> mechanics, actions, roles, venues, etc and then the games within it are the negotiation,
> parliamentary debate, tribunal, etc which are **just defined parameters**."*

---

## What it costs — the count, which is the whole argument

| | |
|---|---|
| **new carriers** | ⭐ **ZERO** |
| **new edge kinds** | ⭐ **ZERO** |
| **new verb names invented** | ⭐ **ZERO.** One was invented in draft (`elicit`), found to duplicate an act the tree had already named (`interview`), and the error is recorded at `04_VERBS.md` §B.3 rather than erased |
| **new fields** | **ONE, contested** — and it turns out to be `Tenure.degree`, **a field the architecture already carries with a writer and no reader**, which `F.4` names as its standing falsifier and `ID-13` is about to delete. **This design is its reader** |
| **verb rows changed** | `speak` and `determine` **gain a body** · `convene` is **corrected** · `release` is **landed** · `the six investigation acts` is **split into five rows** |
| **Queries** | three, of which **`judging_set` is already specified, already registered (`H-32`), and already on the executable chain's critical path (`W26`)** |

> **The bar this is written against:** `03_VERBS_AND_LOOPS.md` §F.1 — *four stages of design added no
> primitive.* **A meta-architecture that answers questions by growing the vocabulary has renamed the
> problem rather than found the shape.** A proceedings subsystem is the most tempting place in this
> game to write thirty verbs, and the count above is the only defence against it.

## What it fixes that was already broken

| | |
|---|---|
| **`speak`** writes nothing and nothing anywhere says what it is for | it becomes *addressing a convened body on a docketed matter* — and the verb that opens the contest |
| **`determine`** is graded `absent`, blocked on `Query.judging_set`, which **raises unconditionally** with the law text *"NOTHING IS DECIDED AT A SITTING"* | the Query is supplied. `W26` |
| **`release` does not exist**, so *a person cannot resign an office* and four of seven relations are open-only | landed |
| **`convene`'s `scale: "settlement"`** is a single roster member standing in for a relation | an ordinal floor above the person tier (Jordan, 2026-09-05) |
| **`(Person, stance)`** is one of four matrix rows with **no producing verb**, which blocks build step 2 | `speak` is a producer |
| **the six investigation acts** are one row with `writes: []` — *"the real backlog"* | five become rows with typed preconditions |

## What it does NOT do — stated first, because the register is the honest part

**Five holes sit on its executable path, three `absent` with no default.** `10_LOOPS_AND_GAPS.md`:

- ~~**`P-01`**~~ — ⚠ **WITHDRAWN.** A draft said *no band edges, nothing can resolve, a ruling between this
  and running.* **The band edges are ruled and pinned**; `H-31` grades the margin model `assumption`
  **with a default and a sweep.** The row was an over-escalation and is closed. What survives is
  `P-06`: which key feeds the pool, and the modifier magnitudes — **inject, declare, sweep** (`ID-6`).
- **`P-05`** — **an investigation cannot deposit what it found.** Five new rows emit a degree nothing
  consumes.
- **`P-21`** — ⚠ **nothing here moves a conviction**, so `AX-3`'s normative half has no producer in the
  one place it most belongs.
- **`P-03`** — `Act` has no `via`, so an adjudicator cannot act **as** a seat (`H-108`).
- **`P-04`** — `Tenure` has no `term`, so no summons has a return day (`T-n` unbuilt).

**`11_NERS.md` fails R's completeness clause, and says so in those words.**

---

## The files

| file | what it is |
|---|---|
| **`00_DERIVATION.md`** | ⭐ **start here.** What a proceeding is, derived from the six axioms with the tree closed. The ownership decomposition, the no-new-primitive account, and eight falsifiers |
| `01_THE_STUDY.md` | the requirement source — the uploaded study, and **the ten things it explicitly refuses to supply** |
| `02_THE_SOCKET.md` | what the season loop actually exposes, **measured at commit `1b1e382`**, and the five things it is missing |
| **`03_PARAMETERS.md`** | ⭐ **the parameter space.** All 27 figures mapped; the fourteen-key arrangement row; **the twelve games as twelve rows**; a thirteenth authored; three the structure refuses |
| **`04_VERBS.md`** | ⭐ **the action set.** The five rows, the fifteen reused, and the fifteen steps mapped — **six of which are cleared by no verb at all** |
| `05_PROCEDURE.md` | what is ordered and what is a map, by the permutation test; the nested run; the ladder |
| `06_RESOLUTION.md` | convictions · ethos · stances · biases — **only two are fields** — the pool, the margin, and where a title enters (**not the pool**) |
| **`07_THE_GAME.md`** | ⭐ **what a player does**, the four decisions, what the engine may and may not show them, and **the twelve as games** |
| `08_SEAM.md` | the signature, the manifest row, two stated amendments, the loader invariants |
| `09_IMPOSSIBILITIES.md` | what has no spelling — **with the grades stated honestly, and the four rows where this design will actually fail** |
| `10_LOOPS_AND_GAPS.md` | six loops signed (**two unsigned, and that is a finding**) · the gap register · what is *not* a gap |
| `11_NERS.md` | the self-audit. **N narrowed · R fails completeness · S passes with one landing · E scored last, as a ratio** |
| `12_BUILD_ORDER.md` | twelve steps with execution artifacts, and **the three that are buildable today with no ruling** |
| **`13_ADVERSARIAL.md`** | ⭐ **the two independent passes** — ~35 findings, 12 applied, 11 registered, 12 named claims that survived a named attack. **And its own first finding is that this file was cited five times before it existed** |
| **`14_THE_WORLD_IN_THE_ROOM.md`** | what a matter IS (the mood selects the genre) · the four worked matters · the eight nouns and their carriers · **the ABOUT-the-world ruling, which fails two of the twelve rows** · and the honest half: the belief→decision edge is **measured-severed** |
| **`15_WHY_IT_IS_A_GAME.md`** | ⭐ **the solver, written out** — and the one change that defeats it: the obstacle must depend on what the room holds |

## Scope — the rule this exercise was under

**Jordan, 2026-09-05: *"Working in /proposals and limited to the contents therein"*, and *"this from
scratch proposal will not refer to any previous work concerning social contests."***

**Honoured as a scope, not as an instruction** (`§G.4.6`). `proposals/2026-09-04-social-contest-branches/`
and `proposals/2026-09-03-governance-corpus-rebuild/` were **not read** — two mapping agents that had
begun on them were stopped when the ruling arrived, and neither's output was seen. The admissible
sources were the uploaded study, `proposals/2026-09-03-meta-architecture/`, the executable chain, and
`CLAUDE.md`.

⚠ **One consequence is a decision this directory does NOT take.** `rosters.yaml:441-446` maps two
contest prizes to a module named `social_contest`. **This design declares its own prize and leaves
both rows untouched** — routing them here would supersede other work by editing one line, which is the
quiet ratification §2 says must be loud or not done. **`02_THE_SOCKET.md` §4 states the option; it is
Jordan's.**

## Method

Two independent derivations under the same brief and the same scope ban — one here, one by a
read-only Fable 5.1 synthesis — then structurally-independent critics with `Read, Grep, Glob` and no
write tools. `13_ADVERSARIAL.md` records where the two agreed, where they did not, and which won.
**Agreement between them is worth something; disagreement was worth more.**
