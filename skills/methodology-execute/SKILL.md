---
name: methodology-execute
description: >
  METHODOLOGY-EXECUTE — invoked as `/methodology-execute <free-text task>` (e.g.
  `/methodology-execute build out governance branch for faction`), build every item a task or
  workplan area names, THEN verify once per batch rather than once per item. EVERY task,
  assignment or workplan is first expressed as ordered BATCHES — items linked by a shared file or a
  gate are one batch (a plan's own batches are used as stated; grouping is derived only where the
  plan has none) — and a batch is the unit of CONTEXT as well as of verification: when it closes
  its finished positions are deleted from the plan and the next batch opens as a session opens,
  carrying only what the two batches' context sets have in common (their intersection; everything
  else is cleared, never summarised). PHASE 0.1: resolve
  the free text against the live workplan first — one matching position with its GATE already met
  proceeds straight through; more than one matching position, or none at all, STOPS and presents
  the resolved sequence (or the freshly-stated plan) for approval before anything is built, per
  CLAUDE.md §0's "ambiguous or spanning lanes" rule. PHASE 0.2+: read each item's own instruction
  (a workplan position's content-owner entry, or the stated plan for an ad hoc task) and dispatch a
  `valoria-author` producer to build it — one producer by default, fanned into
  `isolation: worktree` lanes only when the instruction itself names independent sub-parts with no
  shared file — then commit. **No full pytest suite, no `/code-review`/`/simplify`/
  `layer-conformance`, and no agonist/antagonist fan or terminal critique after each item** — those
  are BATCH-CLOSE's job, not Phase 0's, run once per batch (§BATCHES) or at the run's own final
  `/close`, never per item.
  BATCH-CLOSE: `methodology-close`'s full Phases 1–3, run once against the batch's commit-range
  diff (its recorded starting SHA through HEAD, since every item already committed) — invoked
  verbatim, not copied here. Use for: "run methodology-execute",
  "/methodology-execute <task>", "build out this phase/area", a workplan position, phase, or
  free-text area of work that has not been built yet and needs both building and verifying before
  `/close`. Not for: a diff that already exists and only needs verifying — use `methodology-close`
  directly; design-quality grading (`ners`); a target that resolves by a draw
  (`resolution-diagnostic`); Layer placement alone with no build to do (`layer-conformance`
  directly).
---

# METHODOLOGY-EXECUTE — build, then close

## Created 2026-09-29, split out of `methodology` (now `methodology-close`) per Jordan's directive that the pipeline also orchestrate the build, not only verify one already built. Revised 2026-10-06 per Jordan: a batch is a partition by shared files and gates, and the unit of context — finished batches are deleted from the plan and cleared from the window before the next opens. Invocable as a project skill through the symlink `.claude/skills/methodology-execute`.

## What this skill owns, and what it copies

| the content | its single owner |
|---|---|
| the build phase — dispatching the producer(s) that write the diff a unit of work specifies, sizing the fan, and integrating parallel write lanes | **this file** |
| batching — the partition of items into batches, each batch's context set, where the boundary falls between many cheap BUILDs and one BATCH-CLOSE, and what is deleted and cleared between batches | **this file** — except a plan's own batch structure where it has one, which is the plan's (§BATCHES) |
| deleting a finished position from the plan | **CLAUDE.md §2** (*"Finished positions leave the plan; the commit is their record"*); this file only says when |
| the sequence, tiers, checklists, the handshake, the guardrails and the falsifiers for verifying the resulting (batch) diff | **`methodology-close`**, invoked by reference — not copied |
| the producer contract — full toolset, a receipt not a transcript, no commit, no full-suite mid-lane | **`.claude/agents/valoria-author.md`** |
| model tiers, the effort ladder, and the fan-out sizing rule ("ask what N-1 would miss") | **CLAUDE.md §10** |
| a workplan position's INSTRUCTION / WHERE / FALSIFIER / GATE | **that position's own content-owner file** — never re-derived or restated here |

**Word discipline, inherited, not re-opened.** `methodology-close` defines *agonist* and
*antagonist* narrowly as read-only review roles, run on `valoria-critic`, and states that the
definition "does not travel forward into `methodology-execute`'s build phase." This file honours
that: every Phase 0 dispatch is `valoria-author`, a **producer**, and is never called agonist or
antagonist. When a build is fanned, the orchestrator's merge step is called the **integrator** —
a third word, not a stretch of either of the first two. Three roles, three words, each read cold
the same way every time, per CLAUDE.md §4.

**Relation to `methodology-close` and to `/close`.** This skill's BATCH-CLOSE *is*
`methodology-close`'s Phases 1–3, unmodified. A change to that sequence is made once, in that
file. This skill adds exactly one thing ahead of it: a phase that writes the diff, for when one
does not exist yet — and it changes *when* the closing phases fire, not what they do.

**Per Jordan's directive when this skill was split from `methodology-close`: the expensive
pass — code-review/simplify/layer-conformance, the agonist/antagonist fan, the terminal critique,
and the full pytest suite — does not run after every item.** CLAUDE.md §0's baseline cadence
("one step is one position and one commit... at end of each step, `/code-review` and `/simplify`")
is written for a session working one position by hand. `methodology-execute` orchestrates many
items in one run, and re-running that cadence per item is the over-fanning CLAUDE.md §10 warns
against, plus the exact "full suite is a close step, not an inner loop" mistake CLAUDE.md §0.4
already forbids. So for a run this skill orchestrates: **every item still gets its own commit
(that part of the baseline cadence is unchanged); the review and test cost is deferred to
BATCH-CLOSE**, below. This is a named, deliberate scoping of the baseline cadence to this skill's
own batch granularity — not a silent departure from it, and not licence to skip BATCH-CLOSE
itself.

---

## THE SHAPE OF A RUN: BATCHES, EACH MANY CHEAP ITEMS AND ONE EXPENSIVE PASS

```
  BATCH k    OPEN ──▶ item 1 ──▶ PHASE 0 · BUILD ──▶ commit ─┐
  (as a      (orient  item 2 ──▶ PHASE 0 · BUILD ──▶ commit ─┼─▶ BATCH-CLOSE (once per batch):
  session    from        ⋮  (repeats for every item)         ┘     PHASE 1 · AGONIST FAN → ANTAGONIST
  opens)     disk)                                                 PHASE 2 · MECHANICAL GATES (+ full pytest suite)
                                                                   PHASE 3 · TERMINAL CRITIQUE
                                                                          │
                                                          EXPUNGE ◀───────┘  (delete the batch from the plan)
                                                              │
       BOUNDARY — keep C(k) ∩ C(k+1) · clear C(k) ∖ C(k+1) · load C(k+1) ∖ C(k)
                                                              │
  BATCH k+1  OPEN ──▶ …
```

**Phase 0 repeats per item; BATCH-CLOSE does not.** Each item is one producer, one commit, and — at
most — the cheap, file-scoped self-check CLAUDE.md §0.4 already allows mid-session (the one test
file the change touches, never the full suite). The expensive layer — the agonist/antagonist fan,
`/code-review`→`/simplify`→`layer-conformance`, the full pytest suite, and the terminal critique —
fires once, against every item's cumulative diff since the last BATCH-CLOSE, at a batch boundary
(§BATCHES) or at the run's own final `/close`. **A batch is also the unit of context:** nothing a
finished batch built, read or found is carried into the next except what the two have in common
(§BATCH BOUNDARY).

This is additive sequencing, not a lowered bar: a producer's own confidence that it built an item
correctly is not evidence of that, which is exactly why BATCH-CLOSE's Phase 1 exists — it is
deferred, not skipped. Reporting a run "closed" when only Phase 0 ran for its items is the same
false claim `methodology-close`'s own falsifier table already catches for a single diff, now
scoped to a batch.

---

## PHASE 0 · BUILD

### 0.1 SCOPE — resolve the invocation's free text before touching anything

`/methodology-execute <task>` hands this skill free text (e.g. *"build out governance branch for
faction"*), not a position handle. A vague area of work is not one buildable unit, and this file
does not guess which unit was meant.

1. **Search the live workplan first.** Run `/currency` and follow `CURRENT.md` to whichever
   document it names as the live plan — this file does not name that document itself, because a
   filename written here would be exactly the stale pointer `CLAUDE.md` §1 exists to prevent. Check
   that document for a position whose handle or `what runs` plausibly matches the text.
2. **Classify what the search found:**
   - **Exactly one position, `GATE` already met** — proceed straight to 0.2 with that position's
     content-owner entry. No confirmation needed: the position's own gate already establishes it
     is buildable now, and building it is exactly what was asked.
   - **More than one matching position** — a free-text area of work ("governance branch for
     faction") will usually name a *cluster*, not one step. Resolve the ordered subsequence
     (respecting each position's own `GATE`), then **stop and present the resolved sequence —
     handles, in order, any unmet gate flagged — before building anything.** This is CLAUDE.md
     §0's own rule, not a new one: *"Anything ambiguous or spanning lanes: get the plan approved or
     ask a focused question."* Naming a whole area of the plan is exactly that case.
   - **No matching position** — a genuinely new, unplanned task. Write the plan per
     `methodology-close` §1.1 / CLAUDE.md §0's first bullet (what changes, in what order, how you
     will verify) and **stop and present it for approval**, unless the task is small enough that a
     one-sentence plan already fully states it and CLAUDE.md §0 lets that stand alone.
3. **Express the resolved sequence as batches** — §BATCHES: the plan's own, where it has them;
   otherwise derived, and presented in the same stop as the sequence, so one approval covers both.
   The single-position case is a one-item batch and needs no confirmation. **Once the batches are
   confirmed, take them in order: for each, BATCH OPEN, then 0.2 onward once per item**
   — one BUILD → integrate → commit per item — **then BATCH-CLOSE, then the BATCH BOUNDARY.**
   **Never one diff spanning several items**: each item keeps its own commit, the one part of
   CLAUDE.md §0's baseline cadence this skill does not defer (see "What this skill owns" above). If a later queued item's `GATE` turns out unmet when its
   turn comes (something outside this run's scope, or a `JORDAN` item), **stop there and report
   it** — do not skip it silently and continue to the next, and do not run BATCH-CLOSE on a batch
   that stopped short without saying so.

### 0.2 Read the unit's instruction — never invented here

Whichever way 0.1 resolved it, take one unit of work at a time:

- a **workplan position** — read its content-owner entry (INSTRUCTION / WHERE / FALSIFIER / GATE)
  in full before dispatching anything; or
- an **ad hoc task** with no workplan position — the instruction is the plan 0.1 step 2 just had
  you write (or the user's own one-sentence statement, if that already sufficed).

Either way, that instruction **is** the plan Phase 1 will check fidelity against. Do not restate
it, paraphrase it, or draft a second version for the producer — hand it the same text you read.

### 0.3 Size the build — one producer is the default

Dispatch one `Agent({ subagent_type: "valoria-author", ... })` to build the entire instruction,
sequentially. No `isolation: worktree` is needed for a single producer — nothing else is writing
this tree concurrently within this run.

**Fan only when the instruction itself names genuinely independent sub-parts that share no file**
— the same test the workplan's own hard-serial-edge tables (e.g. `THE PLAN` part 1 §3.5, and the
2026-09-18 plan's §3.9) exist to catch. Never fan by default, and never size the fan to "how many
files changed" alone — CLAUDE.md §10: *"before spawning N agents, ask what N-1 would miss."* Most
workplan positions are one commit, one step, one producer.

When fanned:

- each producer runs `isolation: worktree`, and is handed **only its own sub-part's instruction**,
  never the others' — the same "handed output, not reasoning" discipline Phase 1 uses to keep
  critics independent, applied here to keep parallel write lanes from cross-contaminating;
- each returns a receipt — path, what changed, one line — `valoria-author`'s own contract, so a
  long build never crosses the orchestrator's window;
- fire the first dispatch alone, wait for its first streamed token, *then* send the rest in one
  message — CLAUDE.md §10 point 3, the same cache-priming step `methodology-close` §1.3 uses for
  its agonist fan.

**Either way — one producer or several — the producer never commits** (0.5); that is always the
**orchestrator's** own next action once a receipt (or, when fanned, 0.4's integration) is in hand.
The default, single-producer path has no worktree to merge, so it skips 0.4 and goes straight from
receipt to the orchestrator's commit.

### 0.4 Integrate — only when fanned

The **orchestrator**, not a subagent, merges each worktree into the working branch, in an order
that respects any named serial edge between the sub-parts, **then commits.** **If two lanes touched
the same file, the split was wrong, not the merge** — stop, do not resolve the collision by hand,
and rebuild that file's portion as one producer instead. A silent auto-merge of a same-file
collision is exactly the failure the `FALSIFIERS` table below is written to catch.

### 0.5 What this phase must not do

- **Never review its own output.** `valoria-author` may verify its own edit runs (it holds `Bash`
  for exactly that), but that is not Phase 1's independent fidelity check, and Phase 0 does not
  attempt to be one.
- **Never commit, and never run the full suite mid-lane** — `valoria-author`'s own file already
  forbids both; this skill adds no exception.
- **Never skip 0.1's gate check** because the instruction "looks buildable" — a position gated on
  another position or on Jordan is not this skill's to build around by reinterpreting its own gate.

---

## BATCHES — the unit of work, of verification and of context

**Whatever this skill is handed — a workplan area, a cluster of positions, an ad hoc task — is a
set of items, and the first thing done with it is to express it as ordered batches.** A batch is
three units at once: what is **built** together, what is **closed** together (one BATCH-CLOSE),
and what is **held in context** together. A single position or a one-sentence task is a one-item
batch, not an exception to the rule.

### The partition — boolean intersection, not a headcount

Read each item's two sets from its own content-owner entry — never guessed, never restated here:

- **files** — what its WHERE edits, plus what its FALSIFIER reads;
- **gates** — what its GATE names (positions, decisions), plus any item whose commit it needs.

Two items are **linked** when their file sets intersect (`files(i) ∩ files(j) ≠ ∅`) or one gates on
the other. **A batch is a connected group of linked items**, ordered so every gate points from an
earlier item to a later one. Items with no link — an empty file intersection and no gate between
them, directly or through a third item — belong to different batches.

Why this and not a phase or a count: linked items are the ones whose interactions BATCH-CLOSE
exists to see (its INTERDEPENDENCIES and FORWARD/BACKWARD sweeps cannot see an interaction between
items that are never in one diff), and they read the same things, so they need one window.
Unlinked items share nothing a joint close could check and nothing worth holding together.
What every item reads — `CLAUDE.md`, `CURRENT.md`, the plan's head — is in every batch and links
none of them.

- **Never cut a shared-file link.** Same-file items stay in one batch and one producer (0.3, 0.4).
- **A large group may be cut along gates only,** each cut pointing forward: the later batch's gate
  is met by the earlier batch's BATCH-CLOSE and expunge having landed. Before cutting, name what
  carrying the whole group would risk (a long run with no verification checkpoint; a batch too
  large for Phase 1's fan or Phase 3's critique to hold); before not cutting, name what a cut
  would miss (an interaction visible only once both halves land). By judgment, never a fixed
  item-count.
- **Merge unlinked groups into one batch only for a stated reason** — a full close pass over each
  would cost more than it can find. The merged batch's context is the union of theirs, so nothing
  is cleared between them.

### Where the batches live — whether it has been done already is the first check

- **The plan names batches** (a Batch heading or column, a phase) → **use them as stated.** The
  plan owns that structure. Test each against the partition; where one cuts a shared-file link,
  gates on a later batch, or lumps unlinked groups, say so at the 0.1 stop and leave the plan's
  grouping standing until it is ruled — this skill does not re-split a plan on its own authority.
- **The plan names none, or there is no plan** → derive them by the partition and present them at
  the 0.1 stop. **Once approved, write them where the next window will look:** into the plan that
  owns the positions or, for an ad hoc task with no plan, into the lane's `HANDOFF_<LANE>.md` Open
  table, one row per remaining batch (its items, files, gates). That is an edit, in the commit that
  opens the first batch. A cleared window finds nothing else: no scratchpad file and no summary
  carries batch state across a boundary.
- **A one-batch task writes nothing.** Its commits are its record.

### The context set — what each batch declares

A batch's **context set**, written `C(k)`, is the reading list BATCH OPEN loads: its items'
content-owner entries, the files they edit and read, the registries their FALSIFIERS run against,
the commits their gates name, and the permanent surface. It is derived from the items' own entries
— what *this* batch needs, not what the last one happened to read. (A plan that already keeps a
per-batch reading list owns it.)

What survives a boundary is the **intersection, `C(k) ∩ C(k+1)`** — in practice `CLAUDE.md` and
the user-level file, this skill and `methodology-close`, `CURRENT.md`, `HANDOFF.md` and the lane
file, the plan's head, and any registry both batches read. What is cleared is `C(k) \ C(k+1)`;
what is loaded is `C(k+1) \ C(k)`. **A fact one batch establishes and the next needs is not
context, it is a dependency:** it travels as a commit, a plan edit or a handoff pointer — already
on disk — and appears in the next batch's `C` as a gate, never as a recollection.
`valoria-author` is told the same: a fact worth keeping goes into the artifact.

### BATCH OPEN — orient as a session opens

1. **Establish currency:** `/currency`, then the lane's handoff and the plan's rows for this batch
   only (CLAUDE.md §0's first bullet).
2. **Load `C(k)` from disk**, the overlap with the last batch included. Do not rely on having read it.
3. **Check every item's gate against the tree**, not against any earlier window's belief that it
   landed (0.5's third rule).
4. **Record the starting commit — `HEAD` — before the first item builds.** After an interruption (a
   batch with item commits and no expunge) it is the parent of the earliest commit whose subject
   names one of the batch's handles (`git log --reverse --grep`; the plan's commit shape names the
   handle); if none does, or the match is ambiguous, ask. Every item commits at once (0.1 step 3),
   so when BATCH-CLOSE runs the tree is clean and there is no uncommitted diff — which is what
   `methodology-close`'s Phase 1 and Phase 3 assume they are handed when run on their own. The
   batch's diff is the **commit range from that SHA to `HEAD`** (`git diff <batch-start-sha>..HEAD`
   for the content; `/code-review`'s own branch/PR-target mode, not its bare "current diff" mode,
   for the dispatch itself), and BATCH-CLOSE hands every phase that range.

### The last batch is also the run's `/close`

When the resolved sequence is exhausted, BATCH-CLOSE is immediately followed by `/close` itself
(full suite — already run by BATCH-CLOSE's Phase 2, not twice — lane validator, commit, handoff),
per that skill's own definition. A mid-run boundary does not invoke `/close`; it runs BATCH-CLOSE,
then the BATCH BOUNDARY.

---

## BATCH-CLOSE · PHASES 1–3, ONCE PER BATCH, BY REFERENCE

Run `methodology-close`'s Phases 1 through 3 **once**, against the **commit-range diff** BATCH OPEN
had you record (`<batch-start-sha>..HEAD`) — not against any single item's diff alone, and not
against a working-tree diff, since nothing is left uncommitted by the time a batch ends.

- Its **Phase 1 precondition** ("there must be a plan to check fidelity against") is satisfied by
  the batch's own instructions taken together — the plan's stated scope for the batch; the union of
  whichever positions 0.1 resolved into it, even if they span more than one of the plan's named
  phases; or the concatenation of the ad hoc instructions 0.2 read for each item in the batch. FIDELITY TO PLAN now means fidelity to *that*, not to one item's `WHERE` in isolation.
- Its **fan sizing, dispatch order, cache-priming step, and reconciliation** (§1.2–1.5) apply as
  written there, sized to the batch's own independent parts — which will usually be larger than a
  single item's, since a batch holds several items' worth of change.
- Its **Phase 2 order, apply-before-next-reads discipline, and the full pytest suite**
  (§2.1–2.4, CLAUDE.md §0.4) run once here, against the batch's full cumulative diff — this is the
  one point in a batch where the full suite runs at all; no item inside the batch ran it.
- Its **Phase 3 tier, escalation trigger, checklist, and the top-down/bottom-up handshake**
  (§3.1–3.7) apply as written there, run against the batch's post-Phase-2 diff. INTERDEPENDENCIES
  and the FORWARD/BACKWARD SWEEPS are more likely to find something real here than at single-item
  scale, precisely because several items have now landed together — that is the case BATCH-CLOSE
  exists to catch that per-item verification would have missed one item at a time.

Nothing in this section is restated in full here; a change to any of it is made once, in
`methodology-close`.

---

## BATCH BOUNDARY — expunge, then clear

Runs after BATCH-CLOSE's reconciliations are committed, and not after the run's last batch (that
is `/close`).

1. **Expunge on disk — one commit, net deletion.** Delete the batch's finished positions from the
   plan, by CLAUDE.md §2 and the plan's own rule for where a finished position's one line goes, and
   delete the lane-handoff Open rows its items occupied. Add no narrative, no "done" row and no
   count (CLAUDE.md §1). The batch's record is its commit range (`git log --grep=<handle>`). A
   position the batch only part-finished stays, narrowed to its receipt's `NOT DONE`. What
   BATCH-CLOSE found and applied is already in the batch's commits; a finding nobody can apply
   without a decision becomes a ledger row only if it is `needs_jordan` after CLAUDE.md §0's
   five-step ladder, and is otherwise dropped — nothing is kept "for the next batch".
2. **Clear the window.** This skill cannot clear its own context and nothing inside one window
   forgets selectively, so the boundary is a **stop**: report in a few lines the batch closed, its
   commit range, and the next batch's handle with whether its gates are met — then tell the user to
   `/clear` (**not `/compact`**: a summary carries forward exactly the `C(k) \ C(k+1)` this rule
   discards) and to re-invoke `/methodology-execute` with the same text. The finished positions are
   gone from the plan, so 0.1 resolves only what remains and BATCH OPEN loads `C(k+1)` from disk.
   The user brings the next batch back; this skill never arms its own (CLAUDE.md §11).
3. **Do not hand a batch to a subagent to obtain the clean window.** A delegate that cannot
   dispatch `valoria-author` and `valoria-critic` cannot run a batch, and a general-purpose
   subagent probed 2026-10-06 held `Skill` but not `Agent`. That is a dated observation: re-run the
   probe before relying on it either way.
4. **If the invocation told the run to continue through several batches in one window**, do — and
   say at each boundary that **context was NOT cleared**: only the on-disk expunge happened, and
   every batch after the first carries the earlier ones' residue. Never report a fresh start the
   window did not have.

---

## GUARDRAILS

- **Phase 0 is additive, never a substitute** (see above). Reporting a batch as "built and closed"
  when only its items' Phase 0 ran, with no BATCH-CLOSE, is a false claim of the same shape
  `methodology-close`'s own falsifier table exists to catch.
- **Deferred is not skipped.** Batching BATCH-CLOSE to the batch boundary defers the expensive
  pass; it never licenses dropping it. A run that builds every item and never reaches a
  BATCH-CLOSE has not closed anything, whatever its commit count.
- **Nothing crosses a boundary but the tree.** A receipt, a finding, a SHA or a decision that is
  not in a commit, the plan, the handoff or the permanent surface does not exist for the next
  batch; if the next batch needs it, the partition missed a link — add the link or write the fact
  down, never reconstruct it from memory. No scratchpad file or summary carries state between
  batches.
- **Expunge deletes; it does not log.** The boundary commit nets out removals. A "batch k done"
  row, count or narrative in the plan or handoff is the growth CLAUDE.md §1 forbids.
- **No new roster entry.** Phase 0 dispatches `valoria-author`; BATCH-CLOSE dispatches
  `valoria-critic`, exactly as `methodology-close` already does. Nothing here mints a third agent
  file.
- **Nothing here is a fixed count.** Producer-fan size, agonist-fan size, and batch size are each
  read from the instruction (or the batch) at hand every time — never a default fan, never a
  fixed item-count per batch.
- **No self-scheduling** (CLAUDE.md §11, as always).
- **Produces edits, not documents.** No directory beyond `skills/methodology-execute/`, no
  findings file, no build log kept past the receipts Phase 0's producers already returned.

## FALSIFIERS

| the claim | what would show it false |
|---|---|
| "one producer was enough" | the instruction itself named independent, file-disjoint sub-parts, and only one dispatch ran with no stated reason to collapse them |
| "the build matched the instruction" | the produced diff's scope is broader or narrower than the instruction's own `WHERE`, or silently substitutes a different fix for the one named — this is exactly what BATCH-CLOSE's FIDELITY TO PLAN lens exists to catch; if it passed anyway, name why |
| "fanned lanes integrated cleanly" | 0.4's merge resolved a same-file collision instead of stopping and rebuilding that file as one producer |
| "the gate was met before building" | a workplan-position item's `GATE` column named a position or a Jordan decision that had not actually landed (an ad hoc item has no `GATE` and is exempt from this one) |
| "the batches were partitioned, not sized" | two items sharing a file sit in different batches, an item's gate is met only by a later batch, or a cut ran along a shared-file link |
| "the batch size was right" | a linked group was carried whole through BATCH-CLOSE with no stated reason not to cut it along its gates, or was cut with no stated reason the whole group would have been too large |
| "the plan's own batches were used" | a batch the plan already names was re-split or merged without a conflict stated at the 0.1 stop |
| "the context was cleared at the boundary" | the next batch's work cites a receipt, finding, SHA or fact that is neither on disk nor in the permanent surface; or two batches ran in one window and the report did not say context was NOT cleared |
| "the batch was expunged" | a finished position is still in the plan after the boundary commit, or that commit added a narrative, a "done" row or a count |
| "BATCH-CLOSE ran once per batch" | the full pytest suite, `/code-review`, `/simplify`, `layer-conformance`, the agonist/antagonist fan, or the terminal critique ran between two items of the *same* batch, or did not run at all before the batch's items were reported done |
| every Phase 1–3 claim, at BATCH-CLOSE | `methodology-close`'s own falsifier table, unchanged, checked against the batch's cumulative post-Phase-0 diff |

**If this skill's guidance conflicts with `CLAUDE.md`, `architecture/`, or `methodology-close`,
they win.** This file and `methodology-close` are methods; those are the rules, and
`methodology-close` is the senior method where the two overlap.
