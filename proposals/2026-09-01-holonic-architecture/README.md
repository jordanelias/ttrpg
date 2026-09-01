# The season loop, holonically — built from the #337 → #352 chain

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.** Nothing here runs.

**Scope, and it decides what counts as evidence.** The only sources are the design chain **PR #337 →
#352**, with **#351's `04_UNIFIED_SHAPE.md` as the head.** No file under `engine/`, no subsystem
`sim/`, and **no decision ratified before #337** is authority — not as support, not as precedent, not
as an incumbent to defer to. Where an in-chain document rests a claim on older material, the claim
travels as **that document's own proposal, at its own strength**. `00` §0 names the one place this cuts
an argument the chain itself makes, and re-derives the conclusion without it.

## The answer

> **The proposition — self-sustaining containers running slices of the season loop, managed by wrappers
> and a comprehensive key system — is, in its load-bearing part, WHAT THE HEAD ALREADY SPECIFIES. It
> never uses the word and never names the object.**

`01_THROUGHLINE.md`'s **R-1** and **R-2** under LAW 3 are the container contract — *a rung reads only
its own state, may compute an aggregate over descendants on demand but never receive or store a pushed
one; upward influence is emitting an aggregate, downward influence is emitting a refraction; no module
reaches through another* — and **T5** and **T6** already make both directions structural. One uniform
container (`Rung`, one type, eight kinds), `contain` as an edge rather than node-parenting, influence
aggregating up and refracting down. **That is a holonic architecture, complete, under another name.**

**Three things are missing, and they are the work:**

| | missing | where |
|---|---|---|
| **M1** | the word, and **the object that owns R-1/R-2** — they are stated once and nothing enforces them | `02_THE_WRAPPER_LAYER.md` |
| **M2** | **a descent** — T5's "filtered at a rung" and T6's "distorts in transit" both need to know, per module, what it may receive and emit. No surface answers that | `01_THE_CONTRACT_HIERARCHY.md` |
| **M3** | **the loop's six steps mapped onto the ladder** — nothing joins them today | `00_ADJUDICATION.md` §4 |

**And M3 is where the proposition is partly wrong: two of the six steps partition per-container
(MATTER, DELIBERATE), four do not, and no container gets a clock** — because the four global barriers
are the only within-tick bound the design has, against a termination debt #351 §6.2 reports as
unbounded.

| file | what it is |
|---|---|
| `00_ADJUDICATION.md` | the answer: three senses of "holonic" separated, four collisions, which steps a container may run, and the head's own N/E/R admission test run on this proposal |
| `01_THE_CONTRACT_HIERARCHY.md` | **M2** — a spine of six levels, two axes that are deliberately not levels, and a generated composite. Cites and departs from two in-chain incumbents (#339, #345) |
| `02_THE_WRAPPER_LAYER.md` | **M1** — one rule, four duties, four nevers. Narrowed by the N-line test to **the emission side only** |
| `03_DROPPED_IN_CHAIN.md` | **24 things the chain decided and then lost**, ranked, each naming the later section that restates its neighbours without it. Four re-verified by hand; the rest reported at sweep strength and marked |

## Method

A Fable 5.1 context sweep of #337–#352 and a second Fable pass hunting dropped rulings (`03`), then
`proposals/2026-09-01-shape-tracer-audit/` read in full against the head, then the head's own suite
read directly. **`03` §1.1 states which of its items were re-verified by hand and which are reported at
sweep strength** — five of them bear directly on `00`–`02`, and one (`D-20`) is a **counter-case to
`00` §C4 that is admitted there rather than argued away**. **This proposal was run against the head's
admission test** (`01_THROUGHLINE.md` §6) rather than exempting itself from it — that test is what
narrowed `02` from a general wrapper layer to an emission-side one, and the narrowing is recorded in
`00` §5 rather than presented as the original design.

**No repository file outside this directory was modified.** No `## Status:` line was flipped, no ledger
row appended, **no `ED` allocated** — a gap in a PROPOSED architecture gets no ID; the adoption
decision gets one (`01_FORWARD_DOCTRINE.md` §2), and the shape-tracer audit set that precedent.

## What this does not do

- **It does not close the termination debt.** #351 §6.2: *"four arcs plus the King are spirals; nothing
  bounds one."* `00` §4.3 shows the barrier structure is the only bound and that a container clock
  removes it — **an argument for not making things worse, not a proof.**
- **It does not specify T6's distortion.** A Dispensation *"distorts in transit"*; how much is
  unspecified in the chain and is not invented here.
- **It does not touch the act budget** (#351 §4.2). Nothing here depends on which way it goes.
- **It escalates nothing.** Both candidate escalations dissolved under the scope rule; what remains is
  unfinished specification, named in `00` §7.
- **Nothing here executes**, which is a weaker position than #351's. Each document's last section says
  what would make it done, and in each case one step cannot be satisfied by writing.
