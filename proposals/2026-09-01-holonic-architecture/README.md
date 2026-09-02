# The season loop, holonically — the architecture, and the guide to building it in Godot

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.** Nothing here runs.

> ### ⚠ **A SUCCESSOR EXISTS: `proposals/2026-09-02-executable-architecture/ARCHITECTURE_V2.md`**
> **This document was TESTED BY EXECUTION and the result was that no case ran end to end.** An
> instrument implementing it was built, run against **46 NPCs and 97 arcs**, and attacked by four
> independent read-only passes producing 56 findings.
>
> **Parts I–VI here are RIGHT and the successor inherits them whole**, including every Part VIII
> refusal — 41 of 62 probe PASSes were raised by a gate, a type or a law in this shape itself.
> **What the successor changes is what this document declines to say**: L4's `social:` column is
> keyed on *things* rather than `(kind, field)` and cannot be applied; the ~25 verbs named across
> nine sections have no declared writes, so a resolver has no body; and §61–§62's prose lists become
> a register of ~~**39 holes**~~ holes with owners, grades and defaults — **the count was wrong and
> is computed now**, `ARCHITECTURE_V2.md` §VII.3 carries the correction:
> `python ../2026-09-01-season-loop-tests/tracer/register.py --counts`.
>
> **Read this document first — it is still where the architecture is argued.** Read the successor
> for what an implementation needs that this does not supply. The evidence for both is at
> `proposals/2026-09-01-season-loop-tests/`.


| file | what it is |
|---|---|
| **`ARCHITECTURE.md`** | **the proposal.** Ten parts, from the one sentence down to GDScript hazards. Read Parts I–II before writing a line |
| `03_DROPPED_IN_CHAIN.md` | the evidence appendix — 27 things the chain decided and then lost, four re-verified by hand, with the corrections four adversarial lanes forced |

**`ARCHITECTURE.md` replaces the three documents this directory carried in its first revision**
(`00_ADJUDICATION`, `01_THE_CONTRACT_HIERARCHY`, `02_THE_WRAPPER_LAYER`). They are not superseded in
place because the second revision changed the thesis, not the details — see `ARCHITECTURE.md` §0.2,
which lists every retraction rather than quietly dropping them.

## Scope — the rule that decides what counts as evidence

**The only sources are the design chain PR #337 → #352**, head = #351's `04_UNIFIED_SHAPE.md`. No file
under `engine/`, no subsystem `sim/`, and **no decision ratified before #337** is authority. Where an
in-chain document rests a claim on older material, the claim travels as **that document's own
proposal, at its own strength**.

## The answer

> **The season loop is already holonic. It never uses the word.** `01_THROUGHLINE.md`'s **R-1** and
> **R-2** under LAW 3 are the container contract — *a rung reads only its own state, may compute an
> aggregate over its descendants on demand but never receive or store a pushed one; upward influence
> is emitting an aggregate, downward influence is emitting a refraction; no module reaches through
> another* — and **T5**/**T6** already make both directions structural.

**What is missing is not a wrapper. It is the `Event` record** — the object on which four other
missing pieces are stated, and which the chain wrote once and then dropped. `ARCHITECTURE.md` §19,
§54.4.

## What the second revision retracts

Four read-only Fable lanes ran against the first revision and their corrections were judged as a set.
**Three of them killed its central proposal, independently.**

- **The wrapper is void.** The head has no targeted module emission to check — `Event` carries no
  target and no actor, and *"the only transport the suite defines is a chain of `tell` acts."*
- **Its direction rule contradicted the design.** A dispensation *"travels by being noticed, not down
  a chain of posts"*; `scope` *"enumerates EXECUTORS, not places"*; venues may be containerless and
  offices may have no containment node at all.
- **"Two of six steps partition" was two tests applied to two groups.** The honest frame is
  per-**owner**, and under it only RESOLVE's ordered fold and WITNESS's fan-out are global bodies.
- **The act budget is RULED at ~5, in chain** — and the first revision called it Jordan's open call,
  as did #351 §4.2 and #352 §6. All three missed the same file.

Full list, with lanes and evidence: `ARCHITECTURE.md` §0.2.

## What it does not do

- **It does not close the termination debt.** Four arcs plus the King are spirals; nothing bounds one
  across seasons. §40.1 is honest that the clock refusal is an argument for not making it worse.
- **It does not specify T6's distortion**, or pick a side on emitter- versus receiver-side refraction.
- **It escalates nothing.** Both candidate escalations dissolved: the budget is ruled, the log question
  is decided. What remains is unfinished specification, named in Part IX.
- **Nothing executes.** Part X §66 lists ten artifacts that would change that, and marks the five that
  cannot be satisfied by writing.

**No `ED` allocated** — a gap in a PROPOSED architecture gets no ID; the adoption decision gets one.
