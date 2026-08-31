# The stage-4 relay protocol — ITERATIVE CHALLENGE, not a single-pass review
## Jordan-directed, 2026-08-31. This SUPERSEDES the Part 2 / Part 3 relay shape for the
## superseding-proposal stage. It does not supersede it for review stages.

## The instruction, verbatim

> "Ensure that the superseding proposal reconciles and resolves the agonist-antagonist work, ie the
> antagonistic agent isn't writing but actively challenging so the agonist can correct as it goes."

## What changes, and why it matters

**Parts 2 and 3 ran a SINGLE-PASS relay:** agonist writes → antagonist attacks once → **the
orchestrator reconciles in a separate document.** That produced four separate artifacts per body and
left the defect *in* the proposal with the correction *outside* it, in a reconciliation the next
reader has to hold alongside. Part 3 is the worked failure: `11_INTEGRATED.md` still asserts the floor
in §1.1, and only `12_PART3_RECONCILIATION.md` strikes it. **Anyone reading 11 alone reads a struck
claim as standing.**

**Stage 4 runs an ITERATIVE relay instead:**

```
  ROUND 1   agonist drafts  ──────────────►  antagonist challenges (writes nothing)
                  ▲                                      │
                  └──────── challenge returned ──────────┘
  ROUND 2   agonist CORRECTS ITS OWN DRAFT ─►  antagonist re-challenges the corrected draft
  ROUND 3   … until the antagonist's remaining objections are either fixed in the draft
            or recorded IN the draft as stated limits and live choices
```

**The deliverable is ONE document with the corrections already folded in.** Not a proposal plus a
critique. Not a proposal plus a reconciliation. The proposal *is* the reconciled artifact.

## Rules that keep this from degrading into a dialogue

1. **The antagonist still never sees the agonist's reasoning** — only its OUTPUT (the draft file) and
   the working tree. Independence stays structural; `valoria-critic` has Read/Grep/Glob and no write
   tools, so it *cannot* write the proposal whatever its prompt says.
2. **The antagonist writes nothing into the tree, ever.** It returns challenges. The agonist is the
   only writer.
3. **The agonist must not silently accept.** For each challenge it must do one of exactly three
   things, and record which in the document's own change log:
   - **FIX** — correct the draft, and say what changed.
   - **REBUT** — hold the claim, with the evidence that survives the challenge. A rebuttal that
     cannot cite a line loses by default.
   - **DEMOTE** — the claim cannot be established, so it becomes a **stated limit** or a **live
     choice** inside the document rather than a deleted embarrassment.
4. **Convergence is not agreement.** Stop when the remaining objections are recorded, not when the
   antagonist runs out. If a round produces no FIXes, stop — the relay has converged.
5. **A round that discovers a NEW defect in the tree restarts nothing** — it is added to the
   work-list and handled in the same round.
6. **The orchestrator's job shrinks to adjudication of contested rounds**, and to verifying by direct
   read anything load-bearing before it is banked. **It does not write a separate reconciliation** —
   there is nothing left to reconcile if the loop ran correctly. It records the round-by-round ledger
   as an appendix *inside* the proposal.

## Why the earlier shape was still right for the review stages

A review's product IS a verdict, so a single-pass cold read is the correct instrument and its
independence is the whole value. The iterative shape is for **authorship**, where the goal is a
correct artifact rather than an honest verdict about a fixed one.

## The falsifier for this protocol

If the final proposal contains a claim that the antagonist challenged and the document does not record
as FIX, REBUT or DEMOTE, the loop did not run — it was a single pass with extra steps.

---

## ⚠ AMENDED 2026-08-31, Jordan-directed — ONE SINGLE CORRECT DOCUMENT

> *"ie the final proposal output must be one single correct document"*

**The deliverable superseding PR #342 is ONE document, not a suite.** #342 was seventeen documents;
its replacement is one. This binds the agonist absolutely and is not a packaging preference.

**Why it is also the correct engineering call, which is worth stating because it makes the constraint
easier to hold under pressure.** Every contradiction this session spent itself on is a
**cross-document** contradiction, and could not exist in a single document:

| the defect | its shape |
|---|---|
| three spellings of the three signatures | `11:57-59` vs `01:212-216` vs `09:819-821` |
| two practice ranges | `02:153` **0–5** vs `10:33` **0–7** |
| two pool formulas | `02:197-200` has a `thread_pool` term; `10:30` has none |
| two view budgets | `03:325-329` `K = 7 + Focus` vs `09`'s constant **12**, asserted four times |
| `exposure` in five senses, two of them the same concept implemented incompatibly | `03:574-579` **stores and mutates** it; `07:556` **refuses a stored exposure counter by name** |
| the dangling Thread pointer | `02:4` and `02:435` defer to *"doc 04 (Thread)"*; doc 04 is *The Hearth and the Community* and **no Thread owner exists** |
| the ownership rule in two homes | `11:97` and `01:490-491` — amending one leaves the other refusing what the first permits |
| a worked season contradicting the tick rule | `14:562` *"ten acts"*, seven narrated, against `09:33` *"exactly one act per season"* |

**Eight of the twelve known open defects are of this class.** A single document does not *discipline*
them away — **it makes them unrepresentable.** One owner per rule, stated once, is §8's "every rule
lives once" applied to the design surface rather than to the tooling.

**What this costs, stated rather than hidden.** One document will be long, and length is the reason
#342 was split. The mitigations are structural, not aspirational: a rule appears exactly once and is
cross-referenced by section number thereafter; every quantity has exactly one definition site; the
document carries its own index; and anything that would be a second definition is instead a reference.
**If a section cannot be written without restating a rule defined elsewhere in the document, that is
the signal the two sections are one section.**

**Consequence for the loop:** the antagonist's standing check becomes *"is any rule stated twice, and
do the two statements agree?"* — a check that could not be run at all against a seventeen-document
suite without reading all seventeen, which is why nobody ran it on #342.
