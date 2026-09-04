# From a generator to a system with feedback — the execution plan

## Status: **PROPOSED. HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Planner: `fable` tier, per `CLAUDE.md` §10 (Jordan's 2026-07-28 ruling: fable is licensed for
## **read-only audit, planning/decomposition, orchestration and guardrail** — NOT synthesis or
## artifact authorship). It planned; it wrote no game code and no design document.

This is the operational follow-on to `README.md`'s findings. **It is not a design document** — it
is a work order with falsifiers, execution artifacts and the two prompts per item that
`CLAUDE.md` §10's agonist→antagonist relay needs.

---

## 0 · What the planning review OVERTURNED in this sweep's own findings

I asked it to contradict me. It did, on four counts, and all four are verified against the tree.
**They are corrected in `README.md` and in the register rows; they are repeated here because they
change the ORDER of the work below.**

| # | my claim | the correction | verified at |
|---|---|---|---|
| **1** | *"the design's worked example is one type mismatch from running"* — this report's headline action | **One type mismatch AND one operand.** The corpus's refusals are **operand-gap** refusals: `pack_scenes` puts only `subject` on the payload, so `_req_transfer` reads an empty `from` and refuses a well-stocked granary. **Opening the belief channel first would teach every witness a FALSE fact.** `H-94` is ON the critical path | `shape.py:2739` and its own comment; `_req_transfer` `:3532-3535` |
| **2** | *"zero of 4,800 claims are falsy"* | **A theorem, not a sample.** `witness` mints `Claim(cid, pid, subj, e.kind, True, …)` — predicate is the Event kind, value is a literal `True`, always. I sampled what the code states | `shape.py:4782` |
| **3** | *"the engine has no native x-instead-of-y moment"* | **Half wrong.** 15 slots vs ~7 candidates at the default — but `interactions_per_scene` is swept `1/3/unbounded` on `H-76`, and at `1` it is **5 slots vs 7: the budget binds natively.** `H-117` re-kinded from `ABSENT_RULE`; the defect underneath is `H-96` (alphabetical survival) | `shape.py:952`, `:1020` |
| **4** | *"12 interpersonal verbs carry no degree column"* framed as a defect | **§27.4's design.** An uncontested attempt routes to a gate, never an Ob=0 roll. **Speech is not owed a degree.** The real defect is narrower: no verb claims `a proposition`/`a standing`, and Jordan already said those can wait | `rosters.yaml:347`, `:356-360` |

⚠ **One more, load-bearing on any future forking test:** RESOLVE re-sorts acts by `(stratum, hash)`
(`shape.py:4570-4571`), so **within-budget rank order is inert at RESOLVE by design.** Only a fork
that changes the *set* is a fork.

---

## 1 · The architecture — how a consequence becomes a constraint without `choose` reading the world

Four edges must be live. Today:

| edge | where | state |
|---|---|---|
| **E1 world → belief** | WITNESS deposit, `shape.py:4782` | present, **wrong payload** (predicate = Event kind, value = `True`) |
| **E2 belief → candidate set** | clause 4 `belief_contradicts` `:2537`; clause 3 via Q2 | **severed / degenerate** |
| **E3 belief → ranking** | §F2 score `:2447-2472` | **dead** — no verb writes any interior field (`H-62`) |
| **E0 exclusivity** | `pack_scenes` / `ask_budget` | binds only at `interactions_per_scene=1` |

Plus a precondition the sweep missed: **E1 must carry TRUE facts**, i.e. acts must be well-formed
(`H-94`), or the first thing the opened channel does is propagate instrument defects as beliefs.

**The mechanism.** RESOLVE(*t*) evaluates a verb's `requires` against the world and **records what
it read** as `(subject, predicate, value)` observations on the Event — success *or* refusal.
WITNESS(*t*) deposits those as claims. DELIBERATE(*t+1*) evaluates **the same `requires`
declaration** against a reader over the person's own ledger: KNOWN-false removes the candidate,
UNKNOWN keeps it (§F1's asymmetry, verbatim). **L2 holds** because the reader is the ledger, not
the world. **T3 holds** because a stale belief yields a wrong act → a refusal → a fresh observation
→ a corrected belief: a damping loop with period one season, which is the design's own worked
example finally executing.

**The chosen shape, ranked first of five:** *type `requires` per `F.24a` and give the one
declaration three readers* — the fold predicate over a `WorldReader`, the observations the Event
carries, and the person-side contradiction test over a `LedgerReader`. Same evaluator, two data
sources. The predicate vocabulary is **derived** from the forms, never listed twice (`ID-12`).

**Rejected, with reasons:** a claim→predicate mapping table (a second declaration of a fact the
`requires` cell already states — `H-72`'s own cite says §42.2.1 forbids inventing it); widening
`PERSON_PREDICATES` (that roster is `marks[]`'s vocabulary, read by `agreement()`/`standing_of()`
to pair identity claims — widening it makes `standing` pair refusals as identity claims);
letting `choose` consult a Query (L2); widening `Sensation` (§18.2 — exactly two scalars).

**Degrees compose on top; they are not a new primitive.** A degree is a magnitude on E1. The
selector that turns `wound_state` into one of the verb's three declared branches is **data on the
verb row using the same predicate grammar as `requires`** — one small grammar serving `requires`,
`degree_from` and the ledger. That is the emergence discipline in `CLAUDE.md` §0, and it is not a
second resolver: the subsystem computed the outcome; the fold reads it.

---

## 2 · Sequenced work items

`P` = primitive, `C` = composes on top.

| id | item | kind | depends on |
|---|---|---|---|
| **W-0** | Instrument prerequisites: `content_hash` over state (`H-118`); degree branches raise `Unspecified` not `SystemExit` (`H-115`); `corpus_run` passes `contest_max_depth`; **arm 9 gains a NATIVE fork** at the budget boundary | P | — |
| **W-A** | Typed `requires` grammar; one `evaluate(req, reader, binding)`; `WorldReader` + `LedgerReader`; fold and `belief_contradicts` both read it | **P** | W-0 |
| **W-C** | Operands on the Candidate, derived person-side; unformable Candidates **decline**; delete every silent operand default | **P** | W-A |
| **W-B** | `Event.observed`; the fold attaches what the predicate read; WITNESS deposits one claim per observation | **P** | W-A, W-C |
| **W-D** | The acceptance run: arm 9 at a binding fixture point, with positive **and** negative controls | C | W-0..W-C |
| **W-E** | Degree reaches the fold: `kill / wound` end to end (`H-113`, `H-114`, `H-119`) | C | W-A, W-0 |
| **W-F** | Interior consequence: outcome → `Person.stance` (`H-62`) — **gated on W-D's result** | C | W-B, W-E |
| **W-G** | Antagonist-only audit: nothing smuggled a speech degree or a second resolver | guard | W-A..W-F |

**The acceptance criterion (W-D), under §0.2:** reconvergence **strictly below 100%** on at least
one lane, with a planted contradiction flipping the next decision (positive control) and
`observation_deposit=off` returning reconvergence to 100% at the same fixture point (negative
control). Anything else is not done.

**Model tiering** per §10: W-0 `sonnet`/`sonnet` · **W-A `opus`/`opus`** (a wrong form silently
mis-refuses 32 verbs) · **W-C `opus`/`opus`** · W-B `sonnet` producer / **`opus` critic** (the error
— false beliefs — is silent) · W-D `sonnet`/`sonnet` · **W-E `opus`/`opus`** (§27.2 exposure) ·
**W-F `opus`/`opus`** (AX-3 and drift) · W-G `sonnet` critic only.

**Cache discipline** (§10 fact 1): fire W-A's producer and await its first token before fanning
anything out — every later item depends on it. W-B and W-E may then run in parallel worktrees
(`isolation: worktree`) returning fixed-format summaries.

---

## 3 · The relay, and the two blocks every prompt prepends

Per §10 the relay is **stateless**: dispatch the producer, capture its **output** (diff + command
output + register rows), dispatch the critic **with that output only, never its reasoning**, via
`subagent_type: "valoria-critic"` (which declares `tools: Read, Grep, Glob` — independence is
structural, not asserted in a prompt), reconcile in the orchestrator.

**Reconciliation rule** (§0, amended 2026-08-19): a critic finding becomes an edit to the thing
under review, or at most one paragraph in the commit message. **At most one ledger row, and only if
it survives §0's five tests.** A finding needing no ruling is fixed in the commit or dropped.

The verbatim COMMON PRODUCER BLOCK, COMMON CRITIC BLOCK and all eight item prompt-pairs are held in
`runs/OPUS_PROMPTS.md` so they can be copied without reflowing.
